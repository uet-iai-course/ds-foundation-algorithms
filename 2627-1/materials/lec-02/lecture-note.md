# Bài 02 — MapReduce và ngăn xếp xử lý dữ liệu lớn

## Mục tiêu và kiến thức tiên quyết

Sau bài này, sinh viên có thể:

- đặc tả một phép tính MapReduce gồm Map function, Reduce function và các quy ước đầu vào/đầu ra;
- phân biệt Map/Reduce function, mapper/reducer, Map/Reduce task và phần hệ thống thực hiện;
- chứng minh tính đúng của Word Count bằng song ánh và bất biến;
- giải thích điều kiện để combiner bảo toàn ngữ nghĩa, cách phân vùng gây lệch tải và cách hệ thống chạy lại tác vụ;
- định nghĩa riêng hai quy ước chi phí $I+M$ và $I+2M+O$ rồi áp dụng nhất quán;
- định vị DFS, Hadoop MapReduce, DAG và Spark trong ngăn xếp xử lý theo lô.

Tiên quyết: Bài 01 với cặp khóa–giá trị, bảng băm, phép nhóm, vòng lặp, bất biến, độ phức tạp, tệp và bộ nhớ chính so với lưu trữ thứ cấp. Ta khôi phục ngắn ba khái niệm nền: phân biệt *function* với *task*, tính kết hợp–giao hoán, và tổng trên một phân hoạch.

## Ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| $D$ | tập dữ liệu đầu vào (input) |
| $w$ | một từ (khóa) trong Word Count |
| $c(w)$ | số lần xuất hiện của từ $w$ |
| $I$ | tổng kích thước input đi vào Map |
| $M$ | tổng kích thước intermediate đi vào Reduce |
| $O$ | tổng kích thước output |
| $r$ | số Reduce task |
| $h(k)$ | giá trị băm của khóa $k$ |
| $p(k)$ | hàm phân vùng đưa khóa $k$ vào một Reduce task |

Ba tính chất sẽ được dùng nhiều lần trong bài. *Function* là quy tắc biến đổi do người dùng viết; *task* là đơn vị hệ thống lập lịch để thực hiện nhiều lần gọi hàm. Một phép toán $\oplus$ có tính kết hợp nếu $(a\oplus b)\oplus c=a\oplus(b\oplus c)$ và có tính giao hoán nếu $a\oplus b=b\oplus a$. Nếu $D$ được chia thành các phần rời nhau $D_1,\ldots,D_m$, thì tổng trên toàn bộ dữ liệu bằng tổng các tổng cục bộ:

$$
\sum_{x\in D}x=\sum_{i=1}^{m}\left(\sum_{x\in D_i}x\right).
$$

## Bài toán metadata Web và vai trò của giải thuật

Xét một kho metadata Web: mỗi bản ghi chứa URL/host và kích thước của trang. Ta cần tính tổng byte theo host. Dù có thể quét tuần tự và cộng với bộ nhớ nhỏ trên một máy, cách đó bị giới hạn bởi băng thông và thời gian xử lý của chính máy ấy, đồng thời bỏ phí khả năng đọc song song của cả cụm.

Ví dụ này cho thấy vai trò của giải thuật trong Khoa học dữ liệu. Phép cộng chỉ trở thành lời giải dùng được ở quy mô lớn khi ta chọn mô hình truy cập, phân chia công việc, chứng minh tính đúng và chọn đúng đại lượng chi phí. Bài toán dẫn đến ba câu hỏi: dữ liệu nằm ở đâu và được đọc thế nào, công việc được chia ra sao, và chi phí được đo bằng gì.

## Hệ tệp phân tán và data locality

Một cụm gồm nhiều máy và liên kết, nên hỏng hóc là bình thường. Hai biện pháp nền: lưu tệp dư thừa và chia phép tính thành các tác vụ có thể chạy lại độc lập.

Hệ tệp phân tán (DFS) dành cho tệp rất lớn, hiếm khi cập nhật. Tệp được chia thành chunk; mỗi chunk thường được sao chép trên nhiều máy và nhiều rack. Metadata cho biết vị trí các chunk. Vì băng thông mạng đắt hơn truy cập đĩa cục bộ, hệ thống ưu tiên đưa tính toán đến nơi dữ liệu nằm (data locality): một Map task chạy trên máy có chunk input của nó.

![Hệ tệp phân tán: tệp chia chunk, mỗi chunk có bản sao trên nhiều máy và rack](img/lec-02/he-tep-phan-tan.svg)

Mức độ này đủ dùng cho bài: DFS giải thích vì sao input có thể đọc song song và vì sao output hoàn tất của Reduce an toàn (đã ghi vào DFS), còn intermediate cục bộ thì không. Ta không đi sâu vào vận hành HDFS.

DFS tạo điều kiện để đọc nhiều phần dữ liệu cùng lúc. Phần tiếp theo đặc tả phép tính chạy trên các phần đó và cách nối các kết quả cục bộ thành kết quả toàn cục.

## Đặc tả map–nhóm theo khóa–reduce

Người dùng viết hai hàm:

- **Map function**: nhận một phần tử đầu vào, phát 0 hoặc nhiều cặp khóa–giá trị. Khóa không cần duy nhất.
- **Reduce function**: nhận một khóa $k$ và danh sách giá trị $[v_1,\ldots,v_n]$ cùng khóa, phát 0 hoặc nhiều cặp đầu ra.

Hệ thống thực hiện ba bước: chia input thành các chunk; nhóm toàn bộ cặp theo khóa; phân khóa cho Reduce task sao cho mọi cặp cùng khóa đến cùng một task. Đầu vào logic cho reducer là $(k,[v_1,\ldots,v_n])$.

Cần phân biệt bốn khái niệm:

| Khái niệm | Bản chất | Ví dụ |
|---|---|---|
| Map/Reduce function | hàm do người dùng viết | hàm phát $(w,1)$; hàm cộng danh sách |
| mapper/reducer | một lần áp dụng hàm lên một phần tử/khóa | một lần xử lý một từ; một lần xử lý một khóa |
| Map/Reduce task | đơn vị lập lịch, có thể chạy nhiều lời gọi | một task xử lý một chunk, chạy nhiều mapper |
| hệ thống | chia input, nhóm, phân vùng, lập lịch, xử lý lỗi | Master, scheduler, DFS |

::: example Phân biệt reducer và Reduce task
Một Reduce task có thể chạy nhiều reducer: nó nhận nhiều khóa, mỗi khóa là một lần gọi Reduce. Ngược lại, một reducer chỉ là một lần áp dụng hàm cho một khóa.
:::

![Luồng map–nhóm theo khóa–reduce: Map task phát cặp, hệ thống nhóm theo khóa, Reduce task xử lý từng khóa](img/lec-02/luong-mapreduce.svg)

**Tự kiểm tra.** Trong một Map task xử lý một chunk có 10.000 bản ghi, đâu là hàm do người dùng viết và đâu là đơn vị được hệ thống lập lịch?

## Word Count

Word Count trong các Ví dụ 2.1–2.2 của MMDS là trường hợp nhỏ nhất cho thấy đủ ba bước: Map phát khóa, hệ thống nhóm theo khóa và Reduce tổng hợp các giá trị cùng khóa.

### Quy ước của ví dụ

Ta dùng quy ước riêng của ví dụ (không gán cho nguồn): chuyển chữ thường, tách theo khoảng trắng, bỏ dấu câu. Hai tài liệu nhỏ để chạy tay:

- `Dữ liệu lớn` sau chuẩn hóa thành `dữ liệu lớn`;
- `Lớn, lớn!` sau chuẩn hóa thành `lớn lớn`.

### Đặc tả

- **Đầu vào**: một tập tài liệu đã chuẩn hóa theo quy ước trên.
- **Đầu ra**: với mỗi từ $w$, cặp $(w,c(w))$ trong đó $c(w)$ là số lần $w$ xuất hiện.
- **Điều kiện trước**: mỗi tài liệu là một chuỗi từ tách bởi khoảng trắng, không còn dấu câu.
- **Điều kiện sau**: mọi từ xuất hiện đều có đúng một cặp đầu ra; không có cặp nào cho từ không xuất hiện.
- **Biên**: tài liệu rỗng không phát cặp nào; từ xuất hiện nhiều lần trong một tài liệu vẫn đếm từng lần.

### Giả mã

```text
Map(tài liệu d):
    for w in tách_từ(d):
        phát (w, 1)

Reduce(khóa w, danh sách [1, 1, ..., 1]):
    phát (w, tổng(danh sách))
```

### Vết chạy tay

| Bước | Nội dung |
|---|---|
| Map trên `dữ liệu lớn` | phát `(dữ liệu,1)`, `(lớn,1)` |
| Map trên `lớn lớn` | phát `(lớn,1)`, `(lớn,1)` |
| Nhóm theo khóa | `dữ liệu → [1]`; `lớn → [1,1,1]` |
| Reduce | `(dữ liệu,1)`, `(lớn,3)` |

### Chứng minh tính đúng

::: proof Word Count đếm đúng số lần xuất hiện
**Ý tưởng.** Chứng minh bằng hai bước: mỗi lần xuất hiện tương ứng đúng một số 1, và reducer cộng đúng số 1 của khóa mình.

**Bước 1 — song ánh.** Map phát đúng một cặp $(w,1)$ cho mỗi lần xuất hiện của $w$ trong input. Vì mỗi lần xuất hiện sinh đúng một cặp và mỗi cặp đến từ đúng một lần xuất hiện, có song ánh giữa tập lần xuất hiện của $w$ và tập số 1 mang khóa $w$. Do đó số lượng số 1 mang khóa $w$ bằng $c(w)$.

**Bước 2 — bất biến tổng tiền tố.** Với một reducer xử lý khóa $w$, xét bất biến: sau khi cộng $j$ số hạng đầu, tổng bằng tổng của $j$ số hạng đó. Khởi đầu tổng bằng 0 (tổng của 0 số hạng). Mỗi bước cộng thêm đúng một số 1 nên bất biến được giữ. Khi hết danh sách, tổng bằng tổng toàn bộ số 1 mang khóa $w$, tức $c(w)$ theo Bước 1.

**Kết luận.** Reduce phát $(w,c(w))$ đúng cho mọi $w$.
:::

### Dừng, thời gian, bộ nhớ và dữ liệu trung gian

- **Dừng**: mỗi mapper xử lý hữu hạn từ; mỗi reducer xử lý hữu hạn số 1; nên toàn job dừng.
- **Thời gian**: mỗi mapper tốn thời gian tỉ lệ với độ dài tài liệu; mỗi reducer tốn thời gian tỉ lệ với độ dài danh sách của khóa.
- **Bộ nhớ cục bộ**: reducer chỉ cần một biến tổng, không cần giữ toàn danh sách.
- **Dữ liệu trung gian**: tổng số cặp $(w,1)$ bằng tổng số lần xuất hiện. Nếu kích thước mỗi cặp bị chặn bởi một hằng số, $M$ tỉ lệ với số cặp; $M$ là kích thước dữ liệu, không phải số cặp. Phần chi phí bên dưới sẽ xác định chính xác đại lượng được đếm.

**Tự kiểm tra.** Nếu từ `lớn` xuất hiện thêm hai lần trong tài liệu thứ nhất, những trạng thái nào trong vết chạy thay đổi và cặp đầu ra nào giữ nguyên khóa?

## Combiner

Nguồn MMDS nêu: khi Reduce có tính kết hợp và giao hoán, có thể đẩy phép gộp về phía Map task để giảm dữ liệu trung gian. Phép cộng là ví dụ điển hình.

Điều kiện đóng/cùng kiểu và cùng ngữ nghĩa dưới mọi cây gộp là điều kiện suy ra từ đặc tả, không phải mệnh đề nguyên văn của sách. Để combiner thay được một phần reduce, cần:

- **Đóng và cùng kiểu**: kết quả gộp vẫn là giá trị cùng kiểu với phần tử, để có thể gộp tiếp;
- **Cùng ngữ nghĩa**: gộp theo bất kỳ cây nào cũng cho cùng kết quả với reduce toàn cục.

::: example Phép cộng an toàn
Với phép cộng, gộp cục bộ rồi cộng các tổng cục bộ cho cùng kết quả với cộng toàn bộ. Combiner dùng phép cộng là an toàn.
:::

::: proof Gộp cục bộ bảo toàn tổng
Giả sử các giá trị của một khóa được chia thành các nhóm $V_1,\ldots,V_m$ theo Map task. Combiner phát một tổng cục bộ $s_i=\sum_{x\in V_i}x$ cho mỗi nhóm không rỗng. Do phép cộng có tính kết hợp và giao hoán,

$$
\sum_{i=1}^{m}s_i=\sum_{i=1}^{m}\sum_{x\in V_i}x=\sum_{x\in V_1\cup\cdots\cup V_m}x.
$$

Vì vậy, mọi cách nhóm các phép cộng theo cây đều cho cùng tổng với Reduce trên toàn bộ danh sách. Tính đóng bảo đảm mỗi tổng cục bộ vẫn là một giá trị mà lần gộp tiếp theo có thể nhận. Tính kết hợp và giao hoán do nguồn nêu; yêu cầu đóng/cùng kiểu được suy ra từ việc combiner có thể chạy nhiều tầng; bảo toàn ngữ nghĩa là điều phải chứng minh cho phép gộp cụ thể.
:::

::: example Phép trung bình là phản ví dụ
Trung bình của các trung bình cục bộ không bằng trung bình toàn cục. Với các giá trị $1,2,3,4,5$ chia thành $1,2$ và $3,4,5$: trung bình cục bộ là $1.5$ và $4$; trung bình của chúng là $2.75$, trong khi trung bình toàn cục là $3$. Dùng trung bình cục bộ làm giá trị combiner vì thế không an toàn.
:::

Cách đúng cho trung bình là dùng trạng thái $(tổng, số\, lượng)$: combiner gộp thành cặp tổng và số lượng, reducer cộng các tổng và các số lượng rồi chia.

Combiner không thay reduce toàn cục: hệ thống không được giả định combiner luôn chạy, nên reduce phải tự đúng trên toàn danh sách. Combiner chỉ giảm dữ liệu trung gian khi nó chạy.

**Tự kiểm tra.** Phép lấy cực đại có thể dùng làm combiner hay không? Nêu tính chất đại số và kiểu của giá trị trung gian.

## Phân vùng và lệch tải

Hàm phân vùng $p(k)\in\{0,\ldots,r-1\}$ đưa mỗi khóa $k$ vào đúng một Reduce task. Một cách cài đặt phổ biến là $p(k)=h(k)\bmod r$. Một khóa chỉ về một Reduce task, nên toàn bộ giá trị của khóa đó nằm trong một danh sách.

Cần phân biệt ba khái niệm:

| Khái niệm | Vai trò |
|---|---|
| reducer | một lần áp dụng Reduce cho một khóa |
| Reduce task | đơn vị lập lịch, chạy nhiều reducer |
| worker | máy thực thi, có thể chạy nhiều task nối tiếp |

![Phân vùng khóa vào Reduce task và bộ kết hợp giảm dữ liệu trung gian](img/lec-02/phan-vung-va-bo-ket-hop.svg)

Lệch tải xảy ra khi các khóa có danh sách giá trị dài ngắn rất khác nhau: một Reduce task nhận khóa nóng sẽ chạy lâu hơn hẳn. Trong mô hình cơ bản, nhiều task không chia được một khóa nóng vì mọi giá trị của khóa phải về cùng một task. Việc gom nhiều khóa ngẫu nhiên vào một task chỉ giúp trung bình hóa tải; việc có nhiều Reduce task hơn số máy giúp máy chạy nối tiếp các task ngắn và linh hoạt lịch, nhưng không tự cân bằng một khóa nóng.

Ví dụ, nếu khóa `the` có 1.000.000 giá trị còn mỗi khóa khác chỉ có 100 giá trị, task nhận `the` phải xử lý ít nhất 1.000.000 giá trị dù $r$ tăng từ 10 lên 10.000. Tăng $r$ chỉ làm task ấy chia sẻ ít khóa nhỏ hơn; nó không tách danh sách của `the`. Đây là hiện tượng lệch giữa thời gian hoàn tất của các Reduce task được MMDS minh họa trong khung ở trang in 28.

Quy tắc chọn số task (chẳng hạn một Map task cho mỗi chunk, hay số Reduce task theo kinh nghiệm) là lựa chọn thực hành của nguồn, không phải định lý. Quá nhiều Reduce task làm số tệp trung gian tăng mạnh.

**Tự kiểm tra.** Với $p(k)=h(k)\bmod r$, tăng $r$ có làm hai giá trị mang cùng khóa đi tới hai task khác nhau không? Giải thích từ định nghĩa của $p$.

## Chịu lỗi và chạy lại tác vụ

Master theo dõi trạng thái từng task: `idle`, `executing`, `completed`. Khi phát hiện worker hỏng, Master đưa các task liên quan về `idle` để lập lịch lại.

| Sự cố | Hành động | Lý do |
|---|---|---|
| Master hỏng | khởi động lại toàn job | không còn ai điều phối |
| Map worker hỏng | làm lại cả task đã xong và đang chạy trên worker đó | intermediate cục bộ đã mất |
| Reduce worker hỏng | chỉ làm lại task đang chạy | output hoàn tất đã ghi vào DFS |

![Khôi phục tác vụ: Map worker hỏng mất intermediate cục bộ, Reduce worker hỏng chỉ mất task đang chạy](img/lec-02/khoi-phuc-tac-vu.svg)

### Điều kiện an toàn khi chạy lại

Đây là lập luận biên tập suy ra từ đặc tả, không phải mệnh đề nguyên văn của nguồn. Chạy lại cho cùng kết quả khi:

- **kết quả quyết định theo input**: cùng input cho cùng output, không phụ thuộc lần chạy;
- **không có hiệu ứng ngoài không kiểm soát**: hàm không gửi email, không ghi bộ đếm ngoài, không thay đổi trạng thái toàn cục.

::: example Phản ví dụ
Một Map function vừa phát cặp vừa gửi email thông báo mỗi lần chạy sẽ gửi email trùng khi task bị chạy lại. Một hàm ghi bộ đếm ngoài cũng đếm sai khi chạy lại. Các hàm này không an toàn khi chạy lại.
:::

Chạy lại giữ cho job hoàn tất sau lỗi, nhưng cũng có thể làm tăng lượng dữ liệu phải đọc và tính lại. Vì vậy, phần tiếp theo tách rõ hai cách đếm chi phí.

## Hai mô hình chi phí

Ta định nghĩa: $I$ là tổng input đi vào Map, $M$ là tổng intermediate đi vào Reduce, $O$ là tổng output.

- **Quy ước sách MMDS**: chi phí truyền thông của một task là kích thước đầu vào của task; chi phí thuật toán là tổng đầu vào của mọi task. Với một job MapReduce, tổng đầu vào task là $I+M$. Sách lưu ý "communication" gồm cả I/O cục bộ, không chỉ byte qua mạng.
- **Quy ước slide MMDS/Stanford**: tổng I/O của các tiến trình là $I+2M+O$, vì intermediate được ghi rồi đọc (mỗi byte trung gian vào đĩa một lần và ra một lần).

Hai quy ước đo hai phạm vi I/O khác nhau, nên không gọi cả hai là byte mạng và không so sánh số trước khi định nghĩa cùng phạm vi.

::: example Ví dụ số nhỏ
Giả sử $I=100$, $M=40$, $O=10$ theo cùng một đơn vị kích thước. Quy ước sách cho tổng đầu vào task là $I+M=140$. Quy ước slide cho tổng I/O tiến trình là $I+2M+O=100+80+10=190$. Chênh lệch $50=M+O$: $40$ đến từ việc dữ liệu trung gian được tính thêm một lần và $10$ đến từ việc output được tính trong mô hình slide. Hai số dùng cùng đơn vị nhưng đo hai phạm vi hạch toán khác nhau, nên hiệu của chúng không phải số byte truyền qua mạng.
:::

**Tự kiểm tra.** Nếu combiner làm $M$ giảm một nửa còn $I$ và $O$ giữ nguyên, mỗi mô hình chi phí giảm bao nhiêu?

## DAG, Spark và giới hạn batch

MapReduce hợp quét tuần tự và job batch một lượt: mỗi job đọc input, xử lý, ghi output. Khi cần nhiều bước, chuỗi nhiều job phải vật chất hóa intermediate giữa các job, gây chi phí I/O đĩa và tuần tự hóa.

Một workflow tổng quát là đồ thị có hướng không chu trình (DAG) nhiều tầng tác vụ. Với DAG, tính chặn (task chỉ phát đầu ra sau khi hoàn tất) cho phép chạy lại task lỗi mà không cần chạy lại toàn workflow. Spark cung cấp RDD, đánh giá lười, cache và lineage để tái tạo dữ liệu; các khái niệm này giúp giải thích vì sao ngăn xếp vượt khỏi một job MapReduce.

![Ngăn xếp xử lý dữ liệu lớn: DFS, MapReduce, DAG và Spark trong xử lý theo lô](img/lec-02/ngan-xep-du-lieu.svg)

So sánh hiệu năng chỉ có điều kiện: Spark thường nhanh hơn nhờ xử lý trong bộ nhớ nhưng cần đủ RAM; Hadoop MapReduce phù hợp với các job một lượt và có thể cùng tồn tại với dịch vụ khác. MapReduce hợp truy cập tuần tự và batch lớn, nhưng kém hiệu quả với truy cập ngẫu nhiên, đồ thị và dữ liệu phụ thuộc.

Trở lại kho metadata Web, Map phát $(host,kích\,thước)$ cho từng bản ghi; combiner cộng các kích thước cùng host trong mỗi Map task; Reduce cộng các tổng cục bộ để nhận tổng byte của từng host. $M$ là kích thước các cặp trung gian đi vào Reduce. Mô hình MapReduce phù hợp vì bài toán cho phép quét tuần tự, phân hoạch theo host và tổng hợp độc lập từng khóa trên nhiều máy.

## Bài tập

### MMDS Bài 2.2.1 — Lệch tải trong Word Count

::: exercise
Giả sử chạy Word Count trên một kho lớn như bản sao Web, dùng 100 Map task và một số Reduce task.

- (a) Không dùng combiner: có kỳ vọng lệch đáng kể giữa thời gian các reducer xử lý danh sách giá trị không? Giải thích.
- (b) Gom ngẫu nhiên reducer vào 10 Reduce task thì lệch có đáng kể không? Nếu dùng 10.000 Reduce task thì sao?
- (c) Dùng combiner ở 100 Map task: lệch có đáng kể không? Giải thích.
:::

::: hint
Phân biệt ba đại lượng: độ dài danh sách theo khóa, tổng tải của một Reduce task, và thời gian hoàn tất job. Combiner giảm số lượng giá trị trung gian nhưng không đổi số khóa.
:::

::: solution
(a) Có. Trong kho Web, một số từ (như "the", "a") xuất hiện rất nhiều lần nên danh sách giá trị của chúng rất dài, trong khi đa số từ xuất hiện ít. Vì mọi giá trị của một khóa phải về cùng một Reduce task, task nhận khóa nóng phải xử lý danh sách dài hơn hẳn. Lệch giữa thời gian hoàn tất của các Reduce task là đáng kể.

(b) Gom ngẫu nhiên các reducer vào 10 Reduce task: mỗi task nhận trung bình nhiều khóa, nên tải được trung bình hóa; lệch giảm đáng kể so với (a) vì khóa nóng được pha trộn với nhiều khóa nhỏ. Với 10.000 Reduce task, mỗi task nhận rất ít khóa; task chứa khóa nóng chia sẻ tải với ít khóa nhỏ hơn nên nổi bật hẳn so với các task còn lại. Khóa nóng luôn thuộc đúng một task ở cả hai trường hợp.

(c) Không còn lệch đáng kể như ở (a). Mỗi Map task phát nhiều nhất một tổng cục bộ cho mỗi từ, nên với 100 Map task, danh sách của một khóa có nhiều nhất 100 giá trị. Khóa không xuất hiện trong mọi chunk có thể có danh sách ngắn hơn, nhưng chênh lệch độ dài giảm mạnh so với khi phát một số 1 cho mỗi lần xuất hiện. Combiner vừa giảm $M$ vừa làm lệch tải giữa các reducer nhỏ đi trong trường hợp này.
:::

### MMDS Bài 2.3.1 — Một tệp số nguyên rất lớn

::: exercise
Thiết kế thuật toán MapReduce nhận một tệp số nguyên rất lớn và tạo đầu ra:

- (a) số nguyên lớn nhất;
- (b) trung bình của mọi số nguyên;
- (c) cùng tập số nguyên nhưng mỗi số chỉ xuất hiện một lần;
- (d) số lượng số nguyên phân biệt trong input.

Trong mỗi ý có thể giả định khóa của cặp đầu ra bị bỏ qua.
:::

::: hint
Với (b) dùng trạng thái $(tổng, số\, lượng)$; với (c) nhóm theo chính số nguyên; với (d) có thể dùng hai job. Với tệp rỗng, (a) và (b) không xác định nếu chưa đặt điều kiện trước.
:::

::: solution
(a) **Số nguyên lớn nhất.** Map phát $(1,x)$ cho mỗi số $x$; Reduce nhận danh sách mọi số và phát $(1,\max)$. Khóa đầu ra bị bỏ qua. Với tệp rỗng, max không xác định; cần điều kiện trước tệp không rỗng.

(b) **Trung bình.** Map phát $(1,(x,1))$ cho mỗi số $x$. Reduce cộng các tổng và các số lượng: phát $(1,(S,N))$ rồi trung bình là $S/N$. Dùng trạng thái $(tổng, số\, lượng)$ để tránh lỗi trung bình của trung bình. Với tệp rỗng, $N=0$ nên trung bình không xác định; cần điều kiện trước tệp không rỗng.

(c) **Loại trùng.** Map phát $(x,x)$ cho mỗi số $x$; Reduce nhận danh sách các giá trị cùng khóa $x$ và phát $(\text{khóa không dùng},x)$ một lần. Nhóm theo chính số nguyên nên mỗi số xuất hiện đúng một lần trong đầu ra; khóa đầu ra bị bỏ qua theo quy ước của đề.

(d) **Số lượng phân biệt.** Dùng hai job: job 1 loại trùng như (c) để tạo tập các số phân biệt; job 2 đếm số cặp đầu ra của job 1 (Map phát $(1,1)$ cho mỗi số phân biệt, Reduce cộng). Hai job cần thiết vì một job MapReduce chỉ nhóm theo khóa; đếm số khóa phân biệt cần trước tiên làm mỗi khóa xuất hiện đúng một lần rồi mới đếm.
:::

## Tự kiểm tra

- Phân biệt được Map function, mapper, Map task và phần hệ thống thực hiện.
- Chứng minh được Word Count bằng song ánh và bất biến tổng tiền tố.
- Giải thích được vì sao combiner phải đóng, cùng kiểu và cùng ngữ nghĩa, và vì sao trung bình cần trạng thái $(tổng, số\, lượng)$.
- Giải thích được vì sao nhiều Reduce task không chia được một khóa nóng.
- Nêu đúng hành động khi Master, Map worker, Reduce worker hỏng và điều kiện an toàn khi chạy lại.
- Định nghĩa riêng $I+M$ và $I+2M+O$ rồi áp dụng nhất quán.
- Định vị DFS, Hadoop MapReduce, DAG và Spark trong ngăn xếp batch.

## Tài liệu tham khảo

- Leskovec, Rajaraman, Ullman, *Mining of Massive Datasets*, 3e, Chương 2: §2.1 (hạ tầng phân tán), §2.2.1–2.2.6 (mô hình, Word Count, combiner, phân vùng, điều phối, chịu lỗi), §2.4 (workflow/DAG/Spark), §2.5.1 (chi phí truyền thông); Bài 2.2.1 (trang in 30/PDF 11) và Bài 2.3.1 (trang in 40/PDF 21).
- Slide chính thức MMDS Chương 2, các slide 2–35, 38–40, ghi công tại `http://www.mmds.org`.
- Stanford CS246 `01-intro.pdf`, các slide 49–60, 62, 66–69 (DAG/Spark, giới hạn batch, metadata Web, chi phí $I+2M+O$).
- Điều kiện combiner mở rộng (đóng/cùng kiểu, cùng ngữ nghĩa dưới mọi cây gộp) và điều kiện an toàn khi chạy lại (kết quả quyết định theo input, không hiệu ứng ngoài) là lập luận biên tập suy ra từ đặc tả nguồn, không phải trích dẫn nguyên văn.

Liên kết deck: [Bài 02 — MapReduce và ngăn xếp xử lý dữ liệu lớn](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html)
