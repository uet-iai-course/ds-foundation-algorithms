# Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

Bài này giải thích cách tổ chức phép tính khi dữ liệu nằm trên nhiều máy: chia dữ liệu, chọn khóa để các đóng góp cần nhau gặp nhau, rồi đánh giá lượng dữ liệu phải đọc và truyền. Sau bài học, người học cần viết được map/reduce cho các phép tính cơ bản, giải thích tính đúng và lập bảng chi phí với đơn vị rõ ràng.

Nguồn chính là *Mining of Massive Datasets* (Leskovec, Rajaraman, Ullman), Chương 2, bản `ch2n.pdf` được chỉ định cho học phần. Các số trang dưới đây là **trang in**; số trang PDF bằng số trang in trừ 19; ví dụ trang in 30 là trang PDF 11. Thứ tự các phần giữ nguyên mục 2.1–2.8. Kiến thức đầu vào gồm vòng lặp, hàm, bảng băm, tổng hữu hạn và phép nhân ma trận–vector. Các thuật ngữ hệ phân tán được giải thích trước khi dùng; bài không yêu cầu kiến thức CSDL.

[Bộ trang chiếu Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) · [Sách và học liệu MMDS](http://www.mmds.org)

## 2.1. Hệ tệp phân tán

Một kho dữ liệu lớn có thể vượt khả năng lưu trữ hoặc xử lý của một máy. Cụm máy chia công việc cho nhiều máy nối qua mạng. Các máy thường được đặt trong tủ máy; truyền giữa các tủ phải đi qua mạng kết nối. Vì vậy, vị trí dữ liệu có ảnh hưởng tới chi phí thực hiện phép tính.

![Các máy trong hai tủ nối qua mạng nội tủ và bộ chuyển mạch liên tủ.](img/lec-02/ch2-mang-tu-may.svg)

Sơ đồ khái niệm dựa Hình 2.1, trang 23, chỉ vẽ hai tủ để phân biệt các cấp kết nối. Số máy trong hình không quy định quy mô của cụm.

Nhiều thành phần cũng tạo nhiều vị trí có thể hỏng. Một máy mất có thể làm mất dữ liệu cục bộ; lỗi mạng của một tủ có thể khiến nhiều máy cùng không truy cập được. Hai cơ chế bổ trợ nhau là lưu nhiều bản sao và chia phép tính thành tác vụ có thể chạy lại.

**Hệ tệp phân tán (DFS)** chia một tệp lớn thành các khối và lưu bản sao của khối ở nhiều máy. Đặt bản sao ở các tủ khác nhau giúp tránh mất mọi bản sao khi một tủ hỏng. Siêu dữ liệu cho biết khối của tệp nằm ở đâu. Máy quản lý siêu dữ liệu và tệp siêu dữ liệu là hai đối tượng khác nhau.

![Ba khối có hai bản sao trên ba máy; vị trí bản sao cho phép đọc lại khi mất một máy.](img/lec-02/ch2-khoi-ban-sao.svg)

Hình minh họa cơ chế bằng ba khối và hai bản sao mỗi khối; đây không phải cấu hình bắt buộc của một hệ thống. Khi máy A hỏng, các khối mà nó giữ còn có bản sao ở B hoặc C. Bảo đảm này chỉ đúng nếu còn ít nhất một bản sao truy cập được. Đặt tác vụ gần bản sao đầu vào giúp giảm dữ liệu phải truyền qua mạng.

Môi trường trong chương hướng tới tệp rất lớn, ít cập nhật tại chỗ. Không nên từ đó suy ra mọi cơ sở dữ liệu giao dịch đều thích hợp với cùng mô hình. Hệ tệp giải quyết lưu trữ; phần tiếp theo giải quyết cách phối hợp tính toán. Nguồn: mục 2.1, trang 22–24.

## 2.2. Mô hình MapReduce

### Lợi ích của MapReduce

MapReduce giúp khai thác cụm máy bằng cách tách phép tính người lập trình mô tả khỏi việc tổ chức thực thi. Năm lợi ích gắn với các cơ chế sau:

| Lợi ích | Cơ chế tạo ra lợi ích |
|---|---|
| Song song trên nhiều máy | Các phần việc của Map hoặc Reduce được phân chia để nhiều máy xử lý đồng thời. |
| Mở rộng bằng thêm máy | Bổ sung máy phổ thông vào cụm để tăng tài nguyên xử lý các phần việc. |
| Tự phục hồi lỗi máy | Bộ điều phối phát hiện máy thực thi không phản hồi và giao lại các tác vụ bị ảnh hưởng. |
| Lập trình gọn hơn | Lập trình viên định nghĩa Map/Reduce; hệ thống tổ chức phân phối dữ liệu, giao việc và liên lạc giữa các máy. |
| Xử lý gần dữ liệu | Ưu tiên chạy Map ở nơi có bản sao đầu vào hoặc gần nơi đó, giảm lượng dữ liệu phải truyền. |

Các giai đoạn vẫn phụ thuộc dữ liệu của nhau; song song không có nghĩa mọi bước chạy độc lập. Thêm máy không bảo đảm tăng tốc tuyến tính: cần đủ phần việc, phân chia hợp lý và kiểm soát tải lệch theo khóa. Lập trình viên vẫn chịu trách nhiệm chọn khóa và viết hai hàm đúng. Khả năng phục hồi xét lỗi máy thực thi; trong mô hình MMDS, lỗi máy bộ điều phối có thể đòi hỏi khởi động lại cả công việc. Đặt Map gần dữ liệu là ưu tiên, không loại bỏ toàn bộ truyền qua mạng.

Nguồn: MMDS Chương 2, trang 21–22, mục 2.2 trang 25–30; slide MMDS Chương 2, trang 24–25. Đối chiếu [Dean và Ghemawat (2004)](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/), tóm tắt và mục 3.4. Các phần dưới giải thích những cơ chế này qua bài toán đếm từ.

### Đầu vào, đầu ra và khóa

Xét bài toán đếm số lần xuất hiện của từng từ trong kho tài liệu. Giả sử cách tách từ đã được xác định. Đầu ra chứa một cặp gồm từ và số lần xuất hiện cho mỗi từ xuất hiện ít nhất một lần. Kho rỗng cho đầu ra rỗng.

MapReduce chia trách nhiệm thành ba bước:

1. Hàm map đọc từng phần đầu vào và phát các cặp khóa–giá trị.
2. Hệ thống nhóm mọi giá trị có cùng khóa, rồi đưa nhóm tới nơi xử lý.
3. Hàm reduce nhận một khóa cùng các giá trị của nó và tạo kết quả.

Trong bài toán đếm từ, khóa là từ, giá trị là một đóng góp đếm. Ví dụ 2.1 của sách mô tả tài liệu $w_1,w_2,\ldots,w_n$ phát $(w_1,1),\ldots,(w_n,1)$. Những cặp bằng nhau vẫn phải được giữ: mỗi cặp biểu diễn một lần xuất hiện.

### Hình thức hóa hai hàm

Gọi $K_i$ là miền khóa và $V_i$ là miền giá trị: chỉ số $1$ chỉ đầu vào, $2$ chỉ dữ liệu trung gian, $3$ chỉ đầu ra. Ký hiệu $\operatorname{List}(X)$ chỉ danh sách hữu hạn phần tử thuộc $X$, có thể rỗng và giữ phần tử lặp. Giao diện hai hàm là:

$$
\operatorname{Map}:K_1\times V_1\longrightarrow\operatorname{List}(K_2\times V_2).
$$

$$
\operatorname{Reduce}:K_2\times\operatorname{List}(V_2)\longrightarrow\operatorname{List}(K_3\times V_3).
$$

Map được áp dụng cho từng phần tử đầu vào. Hệ thống thu tất cả cặp Map phát, nhóm theo khóa $k$ và chuyển $(k,[v_1,\ldots,v_m])$ cho Reduce. Danh sách chứa **mọi lần xuất hiện** của giá trị đi kèm $k$; không biến danh sách thành tập hợp. Reduce xử lý từng khóa có mặt và có thể phát không cặp nào hoặc nhiều cặp; kiểu khóa và giá trị đầu ra có thể khác kiểu trung gian.

Trong đếm từ, khóa đầu vào có thể là mã tài liệu; Map không dùng mã đó nên giả mã lược tham số này. Giá trị đầu vào là nội dung tài liệu; khóa trung gian và đầu ra là từ; giá trị trung gian là số 1, giá trị đầu ra là số lần xuất hiện. Chữ ký mô tả kiểu dữ liệu, còn thuật toán cụ thể quy định cách phát và cộng. Nguồn: MMDS 2.2.1–2.2.3, trang 25–27.

![Hai tài liệu phát năm cặp; hệ thống gom thành ba nhóm giữ lặp, Reduce trả dữ 1, liệu 1, lớn 3.](img/lec-02/ch2-map-group-reduce.svg)

::: example
Để đọc vết chạy, bài giảng cụ thể hóa công thức của Ví dụ 2.1 bằng hai chuỗi tiếng Việt: D1 là “dữ liệu lớn”, D2 là “lớn lớn”. Đây là dữ liệu minh họa được chọn trong bài giảng, không phải đoạn văn trích từ sách. Đơn vị đếm là chuỗi tách theo khoảng trắng, không phải phân tích từ vựng tiếng Việt.

| Bước | Dữ liệu |
|---|---|
| Map của D1 | (dữ,1), (liệu,1), (lớn,1) |
| Map của D2 | (lớn,1), (lớn,1) |
| Nhóm “lớn” | [1,1,1] |
| Reduce của “lớn” | (lớn,3) |

Hai kết quả còn lại là (dữ,1) và (liệu,1). Số cặp của “lớn” trước khi nhóm là ba, không phải số tài liệu chứa từ ấy.
:::

### Thuật toán và tính đúng

```text
map(tài_liệu):
    với mỗi từ w trong tài_liệu:
        phát(w, 1)

reduce(w, V):
    s ← 0
    với mỗi giá trị v trong V:
        s ← s + v
    phát(w, s)
```

::: proof
Mệnh đề: thuật toán đếm đúng mọi từ xuất hiện, nếu map duyệt đúng từng lần xuất hiện, hệ thống nhóm đúng khóa và số đếm không tràn.

Map tạo đúng một số 1 cho mỗi lần xuất hiện. Do nhóm theo khóa, danh sách của từ $w$ chứa mọi và chỉ những đóng góp của $w$. Bất biến của vòng reduce: sau khi đọc $j$ giá trị, $s$ bằng tổng $j$ giá trị đã đọc. Ban đầu $j=0$, tổng rỗng bằng 0. Mỗi bước cộng đúng giá trị tiếp theo nên duy trì bất biến. Khi hết danh sách, tổng bằng số lần xuất hiện của $w$.

Mỗi tài liệu và mỗi danh sách hữu hạn nên các vòng lặp dừng. Bất biến chứng minh kết quả; chỉ quan sát vết chạy chưa đủ chứng minh cho mọi đầu vào.
:::

### Đặc tả và mô hình đếm thao tác

Đầu vào là một tập hữu hạn tài liệu, được tách theo cùng quy tắc khoảng trắng. Gọi $T$ là tổng số lần xuất hiện và $f(w)$ là số lần từ $w$ xuất hiện. Kết quả chứa đúng một cặp $(w,f(w))$ cho mỗi từ xuất hiện; không chứa khóa chưa xuất hiện. Kho rỗng trả kết quả rỗng. Mỗi lần xuất hiện phải được xử lý đúng một lần về mặt logic.

Trong giả mã chưa gộp, Map phát $T$ cặp. Reduce khởi tạo tổng bằng 0 và thực hiện một phép cộng cho **mỗi** giá trị nhận, nên toàn công việc có đúng $T$ phép cộng, kể cả cộng giá trị đầu vào 0. D1/D2 cho 5 cặp và 5 phép cộng; riêng “lớn” có 3 phép cộng. Với truy cập, cộng và phát một cặp được tính là một đơn vị, công việc duyệt từ đã tách là $O(T)$ khi $T\ge1$, chưa gồm khởi tạo và các lời gọi Map trên tài liệu rỗng. Đây là mô hình thao tác trên dữ liệu đã tách; chưa gồm tách chuỗi, so sánh khóa, nhóm, sắp xếp, truyền dữ liệu hoặc khởi tạo tác vụ. Nếu tính số nguyên có độ dài tùy ý, chi phí cộng còn phụ thuộc số bit.

Một lần gọi Reduce duyệt tuần tự chỉ cần một biến tổng: $O(1)$ từ nhớ phụ theo mô hình trên, ngoài khóa, vùng đầu vào và bộ đệm của hệ thống. Không suy ra cả máy chỉ cần $O(1)$ bộ nhớ hoặc thời gian hoàn thành bằng $T$ chia số máy. Chi phí dữ liệu được tính riêng ở mục 2.5. Các phép đếm này được suy ra từ giả mã dựa MMDS 2.2.1–2.2.3, trang 25–27.

Với bộ kết hợp, nếu tác vụ Map $a$ gộp trọn từng từ và có $d_a$ từ phân biệt, tổng số cặp gửi là $G=\sum_a d_a\le T$. Các từ giống nhau ở hai tác vụ vẫn tạo hai tổng riêng. Nếu bộ kết hợp chỉ chạy trên từng mảnh, phải đếm số tổng thực sự phát; không dùng $G$ này vô điều kiện. Một cách cài đặt giữ bảng tổng theo từ cần $O(d_a)$ bộ đếm, ngoài vùng khóa; đây là lựa chọn cài đặt, không là yêu cầu mọi bộ kết hợp. Tổng công việc có thêm bước gộp; ít cặp truyền hơn không có nghĩa ít phép cộng hơn. Nguồn: MMDS 2.2.4, trang 27–28.


### Gộp cục bộ và đơn vị thực thi

Bộ kết hợp có thể cộng các đóng góp của cùng từ trước khi truyền. Trong D2, hai cặp (lớn,1) trở thành (lớn,2). Reduce cuối cộng 1 và 2 vẫn được 3. Tính kết hợp và giao hoán của phép cộng cho phép đổi cách nhóm; trạng thái gộp phải giữ nguyên ý nghĩa số lần xuất hiện. Không thể thay phép cộng bằng phép max dù max cũng kết hợp và giao hoán.

Bộ kết hợp là tối ưu tùy chọn: thuật toán cuối phải đúng cả khi không có gộp. Để tính trung bình, cần giữ cặp (tổng, số lượng); không lấy trung bình của các trung bình khi nhóm có số phần tử khác nhau.

| Đơn vị | Ý nghĩa |
|---|---|
| Một reducer | Một lần áp dụng reduce cho một khóa và danh sách giá trị |
| Một tác vụ Reduce | Đơn vị lập lịch, có thể xử lý nhiều khóa |
| Một máy | Có thể chạy nhiều tác vụ |

Tăng số tác vụ không tự chia một khóa lớn thành nhiều reducer. Muốn xử lý một khóa nóng theo nhiều giai đoạn phải thay thuật toán.

### Từ hàm đến tác vụ và máy

Lập trình viên định nghĩa hàm Map và Reduce. Hệ thống tổ chức nhiều lần gọi các hàm này thành **tác vụ**, rồi giao cho các **tiến trình thực thi (Worker)** trên máy. Bộ điều phối (Master) tạo, phân công và theo dõi công việc. Một tác vụ Map xử lý các phần tử thuộc phần đầu vào được giao; một tác vụ Reduce xử lý một hoặc nhiều khóa, mỗi khóa là một lần gọi hàm Reduce. Vì vậy số khóa, số tác vụ, số tiến trình và số máy không nhất thiết bằng nhau.

### Tạo tác vụ Map và phân chia đầu vào

Chương trình chọn số tác vụ. Sách nêu cách thường dùng là tạo một tác vụ Map cho mỗi khối đầu vào; nói tổng quát, một tác vụ có thể nhận một hoặc nhiều khối. Một khối có thể chứa nhiều tài liệu; mỗi tài liệu là một phần tử đầu vào và không bị cắt qua hai khối trong mô hình này. Tất cả tác vụ dùng cùng mã Map, nhưng xử lý phần dữ liệu khác nhau.

![D1 trong phần 0 được Map 0 xử lý; D2 trong phần 1 được Map 1 xử lý, cùng hàm Map.](img/lec-02/ch2-tao-tac-vu-map.svg)

Ta đặt D1 và D2 vào hai phần để minh họa; không suy ra một tài liệu luôn tương ứng một tác vụ. Khi số tác vụ nhiều hơn số tiến trình thực thi, bộ điều phối giao việc qua nhiều đợt. Nguồn: MMDS 2.2.1 và 2.2.5, trang 25–26,29.

### Phân chia khóa cho các tác vụ Reduce

Chọn $r$ tác vụ Reduce và một hàm phân chia $h$ đưa mỗi khóa vào một trong các chỉ số $0,\ldots,r-1$. Mọi Map dùng cùng quy tắc. Mỗi Map tạo $r$ tệp trung gian trên đĩa cục bộ, mỗi tệp dành cho một tác vụ Reduce; một tệp có thể rỗng. Với $m$ tác vụ Map, mô hình này có $mr$ tệp trung gian, nên tăng số Reduce cũng tăng số tệp phải quản lý.

![Map 0 và Map 1 dùng cùng h để đưa dữ, liệu về R0 và mọi đóng góp của lớn về R1.](img/lec-02/ch2-phan-vung-reduce.svg)

Ví dụ chọn $r=2$, $h(\text{dữ})=h(\text{liệu})=0$ và $h(\text{lớn})=1$. Đây là phân chia minh họa, không phải giá trị băm mặc định. Tác vụ Reduce 0 nhận hai nhóm khóa; Reduce 1 nhận ba giá trị 1 của khóa lớn từ cả hai Map. Hai Map tạo bốn tệp trong mô hình, trong đó tệp dành cho Reduce 0 của Map 1 rỗng. Khi thu tệp, hệ thống nhóm theo khóa trước khi gọi Reduce. Tăng số tác vụ không tự chia một khóa nóng cho nhiều nơi.

Hàm $h$ quyết định **tác vụ đích**, còn bộ điều phối quyết định **máy chạy tác vụ**. Phân chia khóa có thể do người dùng cung cấp, nhưng mỗi khóa vẫn chỉ thuộc một tác vụ Reduce. Nguồn: MMDS 2.2.2, chú thích trang 27, khung trang 28 và 2.2.5 trang 29.

### Phân bổ lên máy và theo dõi trạng thái

![Bộ điều phối giao Map 0, Map 1 tới A,B và Reduce 0, Reduce 1 tới C,D; Worker báo xong để nhận công việc tiếp.](img/lec-02/ch2-phan-bo-tac-vu.svg)

Hình là phân công minh họa dựa Hình 2.3, không khẳng định bốn tác vụ chạy đồng thời. Worker là tiến trình trên một máy; trong mô hình sách, tiến trình thường chuyên Map hoặc Reduce. Bộ điều phối theo dõi ba trạng thái: **chờ**, **đang chạy tại Worker nào**, **hoàn thành**. Worker rảnh phù hợp được giao tác vụ chờ; khi báo xong, bộ điều phối giao việc tiếp. Một máy có thể lần lượt thực hiện nhiều tác vụ.

Ưu tiên đặt Map gần bản sao dữ liệu giúp giảm truyền đầu vào, không bảo đảm lúc nào cũng có máy phù hợp tại nơi lưu bản sao. Map ghi trung gian cục bộ và báo vị trí, kích thước tệp cho bộ điều phối. Bộ điều phối cung cấp nơi đọc cho Reduce; dữ liệu không phải đi xuyên qua bộ điều phối. Reduce đọc các tệp dành cho mình và ghi kết quả cuối vào hệ tệp phân tán. Nguồn: MMDS 2.2.5, Hình 2.3 trang 28–29; slide MMDS Chương 2, trang 24–25 về thực thi gần dữ liệu và bộ điều phối.

### Phát hiện lỗi và dữ liệu còn lại

Bộ điều phối kiểm tra phản hồi của Worker định kỳ. Khi coi một máy không phản hồi là hỏng, hệ thống đưa các tác vụ bị ảnh hưởng về trạng thái chờ để giao lại. Không giả định một ngưỡng thời gian cụ thể ngoài nguồn.

| Dữ liệu | Nơi lưu | Vai trò khi chạy lại |
|---|---|---|
| Đầu vào Map | Hệ tệp phân tán có bản sao | Nguồn để tính lại |
| Trung gian Map | Đĩa cục bộ máy thực thi Map | Mất máy có thể làm Reduce mất đầu vào |
| Kết quả Reduce đã hoàn thành | Hệ tệp phân tán | Giữ được nếu lớp lưu trữ còn hoạt động |

Giả thiết các bản sao đầu vào và kết quả hoàn thành còn truy cập được. Chịu lỗi máy thực thi không đồng nghĩa chịu mất mọi bản sao dữ liệu.

### Phục hồi khi máy Map hỏng

![Máy A mất phản hồi; Map 0 về chờ, chạy lại trên E từ D1; tệp mới được báo cho Reduce, Map 1 trên B giữ nguyên.](img/lec-02/ch2-phuc-hoi-map.svg)

Nếu máy A chứa Map 0 bị lỗi, tệp trung gian của Map 0 không còn để Reduce đọc. Bộ điều phối đặt các tác vụ Map được giao cho máy đó về chờ, **kể cả đã hoàn thành**, rồi giao Worker khác khi có thể. Trong ví dụ, máy E đọc lại D1 từ hệ tệp phân tán, chạy lại Map 0 và tạo các tệp trung gian thay thế. Bộ điều phối thông báo vị trí mới cho các tác vụ Reduce cần chúng. Map 1 trên B không bị ảnh hưởng nên không chạy lại.

Lý do chạy lại là mất đầu ra cục bộ, không phải phép tính trước đó sai. Để giữ đúng số đếm, dữ liệu tái tạo phải thay thế kết quả của cùng tác vụ logic, không trở thành một lần đóng góp bổ sung. Nguồn mô tả việc làm lại và cập nhật vị trí, không đặc tả một giao thức ghi kết quả cụ thể. Nguồn: MMDS 2.2.6, trang 30.

### Phục hồi khi máy Reduce hỏng

![Máy D hỏng khi chạy Reduce 1; tác vụ về chờ rồi chạy lại trên F từ các tệp Map còn tồn tại. Kết quả Reduce 0 đã hoàn tất được giữ.](img/lec-02/ch2-phuc-hoi-reduce.svg)

Bộ điều phối đưa các tác vụ Reduce **đang chạy** trên máy hỏng về chờ rồi giao lại Worker khác. Trong ví dụ, máy F đọc lại các tệp Map còn tồn tại, chạy lại Reduce 1 và ghi kết quả vào hệ tệp phân tán. Reduce 0 đã hoàn thành có kết quả nằm trên hệ tệp phân tán nên không cần làm lại. Các Map cũng không cần chạy lại nếu tệp trung gian còn truy cập được; nếu đồng thời mất máy Map, phải áp dụng cơ chế phục hồi Map tương ứng.

Trong mô hình được mô tả ở MMDS 2.2.6, nếu chính máy bộ điều phối hỏng thì phải khởi động lại toàn bộ công việc. Đây là giới hạn của mô hình sách, không là kết luận cho mọi hệ thống hiện đại. Nguồn: MMDS 2.2.5–2.2.6, trang 29–30.

## 2.3. Các thuật toán dùng MapReduce

### Nhân ma trận–vector

Cho ma trận $M$ kích thước $n\times n$ và vector $v$ độ dài $n$. Đầu ra là vector $x=Mv$, với

$$
x_i=\sum_{j=1}^{n}m_{ij}v_j.
$$

Ma trận được lưu bằng các bộ $(i,j,m_{ij})$. Trong biểu diễn thưa, các vị trí không lưu được hiểu là 0. Giả sử trước hết mỗi tác vụ Map có thể giữ toàn bộ $v$ trong bộ nhớ. Một phần tử ma trận tạo một tích; các tích cần cộng với nhau có cùng chỉ số hàng $i$.

| Đầu vào của Map | Đóng góp cho hàng $i$ |
|---|---|
| $(i,1,m_{i1})$ | $(i,m_{i1}v_1)$ |
| $(i,2,m_{i2})$ | $(i,m_{i2}v_2)$ |
| $(i,j,m_{ij})$ | $(i,m_{ij}v_j)$ |

```text
map(i, j, m):
    phát(i, m × v[j])

reduce(i, V):
    s ← 0
    với mỗi p trong V: s ← s + p
    phát(i, s)
```

::: proof
Mỗi phần tử lưu $(i,j,m_{ij})$ đóng góp đúng tích $m_{ij}v_j$ tới hàng $i$, đúng một lần. Nhóm theo $i$ thu đủ các tích của hàng ấy. Bất biến cộng tổng của phần đếm từ áp dụng lại, nên reduce trả đúng $x_i$. Các phần tử 0 bị lược không làm đổi tổng. Hàng không phát cặp phải được hiểu có kết quả 0 hoặc được bổ sung 0 theo quy ước biểu diễn đầu ra.

Lập luận xét số học chính xác. Với số dấu phẩy động, đổi thứ tự cộng có thể làm sai khác nhỏ kết quả tính máy.
:::

Nếu vector không vừa bộ nhớ, chia ma trận thành các dải dọc và vector thành các dải tương ứng. Một tác vụ đọc phần ma trận của dải và dải vector cùng chỉ số. Mọi tích vẫn mang khóa hàng, nên reduce cộng cả các đóng góp từ những dải khác nhau.

![Năm dải dọc của ma trận ghép với năm dải vector tương ứng, theo Hình 2.4.](img/lec-02/ch2-dai-ma-tran.svg)

Các dải chia miền cột thành những phần không giao nhau và phủ hết miền cột. Vì thế mỗi tích được tạo đúng một lần, dù các tích của một hàng xuất phát từ nhiều dải. Điều kiện bộ nhớ áp dụng cho dải vector và trạng thái tác vụ, không chỉ cho số dải. Có thể nhiều tác vụ đọc cùng dải vector; khi tính chi phí phải đếm những lần đọc đó. Nguồn: mục 2.3.1–2.3.2, trang 31–32, Hình 2.4.

### Đặc tả biểu diễn và đánh giá phép tính

Lấy $n\ge1$ và $1\le i,j\le n$. Mỗi vị trí khác không của ma trận được lưu đúng một lần; vị trí không lưu mang giá trị 0. Thuật toán trả các cặp $(i,x_i)$ cho hàng có đóng góp; hàng không xuất hiện ở đầu ra được hiểu là 0. Do đó một ma trận không có phần tử lưu trả danh sách rỗng biểu diễn vector không. Các bộ trùng tọa độ không thuộc biểu diễn này: nếu vẫn cộng chúng sẽ đổi ma trận cần tính.

Gọi $z$ là số phần tử được lưu. Với giả mã khởi tạo $s=0$ rồi cộng từng tích, Map thực hiện $z$ phép nhân, phát $z$ cặp và Reduce thực hiện $z$ phép cộng trên toàn công việc. Không dùng $z-n$: hàng rỗng không tạo lời gọi Reduce, còn hàng có dữ liệu vẫn cộng phần tử đầu tiên vào 0. Phép đếm giả sử truy cập vector, cộng và nhân có chi phí đơn vị; đây là mô hình đếm, tách khỏi giả thiết số học chính xác của chứng minh. Chưa tính đọc vector, nhóm khóa hoặc ghi kết quả.

Khi giữ toàn bộ vector, mỗi tác vụ cần chỗ cho $n$ phần tử vector. Khi chia dải, một tác vụ chỉ giữ $L$ phần tử của dải tương ứng và duyệt phần ma trận được giao. Cách tính là: đọc dải vector → với mỗi bộ $(i,j,m_{ij})$ thuộc dải, phát $(i,m_{ij}v_j)$ → hệ thống nhóm theo hàng → Reduce cộng như trước. Các dải phủ hết cột, không giao nhau nên đầu ra không đổi. Bộ nhớ giữ vector là $O(n)$ hoặc $O(L)$ từ nhớ; một lời gọi Reduce dùng thêm một biến tổng nếu duyệt tuần tự. Bộ đệm và vùng quản lý tác vụ vẫn phải tính riêng.

Việc chia dải không giảm số phép nhân/cộng. Nó giảm phần vector cần giữ, nhưng nhiều tác vụ có thể phải đọc lại cùng dải. Mục 2.5 tính khoản này bằng $\sum_j a_jL_j$, trong đó $j$ ở công thức chi phí đánh số dải. Các phép đếm là suy ra từ thuật toán MMDS 2.3.1–2.3.2, trang 31–32, không phải số đo thời gian thực.

## 2.4. Từ chuỗi xử lý văn bản đến Hadoop và Spark

### Bài toán và các bước phụ thuộc

Ta muốn đếm số lần xuất hiện của mỗi từ trong kho tài liệu sau khi bỏ các từ trong danh sách từ dừng. Ví dụ Việt hóa từ MMDS Ví dụ 2.7–2.8 dùng tài liệu A “dữ liệu và giải thuật” và B “dữ liệu lớn”; danh sách dừng chỉ gồm “và”. Ta tách theo khoảng trắng, không phân tích từ ghép. Mỗi từ còn lại phải có đúng một cặp kết quả với số lần xuất hiện của nó. Đầu vào rỗng cho đầu ra rỗng; số đếm được giả sử không tràn.

| Bước | Trạng thái trên A/B |
|---|---|
| Tách từ | A: dữ, liệu, và, giải, thuật; B: dữ, liệu, lớn |
| Bỏ từ dừng | A: dữ, liệu, giải, thuật; B: dữ, liệu, lớn |
| Đếm theo từ | (dữ,2), (liệu,2), (giải,1), (thuật,1), (lớn,1) |

Có 8 lần xuất hiện trước lọc, 7 sau lọc và 5 từ phân biệt. Các tài liệu A/B chỉ dùng trong mục này; không thay D1/D2 của ví dụ đếm từ ở 2.2 và 2.5. Việc Việt hóa làm phép lọc quan sát được bằng một từ quen thuộc, không bổ sung bài tập ngoài giáo trình.

![Chuỗi tách, lọc có hai nhánh: đếm theo từ và đếm tổng số lần xuất hiện còn lại.](img/lec-02/ch2-van-ban-luong.svg)

Mũi tên biểu diễn đầu ra bước trước cung cấp đầu vào bước sau. Đồ thị có hướng không chu trình không có đường phụ thuộc quay trở lại chính một bước. Một hộp không đồng nghĩa một máy hoặc một công việc riêng. Dữ liệu sau lọc còn có thể dùng để đếm tổng số từ, cho 7; nhánh thứ hai chuẩn bị cho nhu cầu dùng lại dữ liệu. Sơ đồ cụ thể hóa ý tưởng luồng công việc ở MMDS 2.4.1, trang 41–43, thay cho các hàm chỉ đặt tên f, g, h, i, j.

### Hadoop: lưu trữ và thực thi

Hadoop gồm nhiều thành phần. Trong phạm vi bài này, **hệ tệp phân tán Hadoop (HDFS)** giữ tệp dưới dạng khối và bản sao; **Hadoop MapReduce** thực hiện các công việc MapReduce trên cụm máy, phân công và khôi phục tác vụ. Đây là tên phần mềm triển khai các vai trò lưu trữ và tính toán đã học, không phải hai thuật toán đếm từ mới. Đối chiếu: [Apache Hadoop](https://hadoop.apache.org/) và [MapReduce Tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html).

![Một công việc Hadoop MapReduce: đọc văn bản HDFS, Map tách và lọc, nhóm theo từ, Reduce cộng, ghi kết quả HDFS.](img/lec-02/ch2-hadoop-van-ban.svg)

Ví dụ trên chỉ cần một công việc MapReduce: trong mỗi lời gọi Map, duyệt các từ của tài liệu, bỏ “và”, phát $(w,1)$ cho từng lần xuất hiện còn lại. Hệ thống nhóm theo khóa, Reduce cộng như phần 2.2. HDFS giữ đầu vào và kết quả công việc; trung gian Map trong mô hình đã học nằm ở đĩa cục bộ. Khi ứng dụng thực sự cần nhiều công việc nối nhau, một công việc có thể đọc tệp kết quả của công việc trước. Không bắt buộc tạo một công việc riêng cho mỗi bước tách, lọc, đếm trong hình.

### Spark: diễn đạt chuỗi biến đổi

Một **tập dữ liệu phân tán có khả năng khôi phục (RDD)** chứa các phần tử cùng kiểu, chia thành nhiều phần. Spark cung cấp các phép biến đổi tạo RDD mới từ RDD đã có. Trên cùng tài liệu A, map(tách) trả một phần tử là danh sách năm từ; flatMap(tách) trả năm phần tử từ riêng biệt. Filter áp dụng sau flatMap giữ bốn phần tử khác “và”. Hai lựa chọn map/flatMap không phải hai bước liên tiếp. RDD giữ các lần xuất hiện lặp, không tự loại trùng.

Giả mã đọc thư mục chứa hai tài liệu A và B; doc_tep và tach_khoang_trang chỉ là tên mô tả, các phép biến đổi còn lại dùng tên của Spark:

```text
van_ban = doc_tep(thu_muc_A_B)
tu = van_ban.flatMap(tach_khoang_trang)
sach = tu.filter(w => w != "và")
cap = sach.map(w => (w, 1))
dem = cap.reduceByKey((a, b) => a + b)
dem.saveAsTextFile(thu_muc_ket_qua)
```

reduceByKey cộng các giá trị theo từng khóa và trả RDD các cặp đếm; saveAsTextFile là hành động yêu cầu tính và ghi kết quả. Reduce của Spark là một hành động gộp thành một giá trị; không dùng nó thay cho reduceByKey trong ví dụ này. Không đưa toàn bộ kết quả của kho lớn về máy điều khiển bằng collect. Nguồn: MMDS 2.4.2–2.4.3, Ví dụ 2.7–2.9, trang 44–47; tên API reduceByKey và saveAsTextFile đối chiếu [Spark RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html).

Tính đúng kế thừa đếm từ: lọc giữ đúng những lần xuất hiện cần đếm, mỗi lần sinh một đóng góp, cộng theo khóa thu đủ và chỉ những đóng góp của từ ấy. Đầu vào hữu hạn và phép tách/lọc hữu hạn bảo đảm dừng. Có 7 cặp logic trước cộng theo khóa; không suy ra có đúng 7 cặp được truyền mạng vì hệ thống có thể gộp cục bộ. Việc duyệt, lọc và ghép cặp là tuyến tính theo số đơn vị từ trong mô hình thao tác đơn vị; tách chuỗi còn phụ thuộc độ dài văn bản. Gom theo khóa có thể cần trao đổi dữ liệu, bộ đệm và đĩa; mục 2.5 phân tích chi phí dữ liệu riêng.

### Tính khi cần, lưu lại để dùng tiếp

Các biến đổi ghi cách tạo dữ liệu; hành động mới yêu cầu tính. Để dùng dữ liệu sạch cho cả ghi số đếm và đếm tổng số từ, có thể gọi sach.cache() trước hành động đầu. Lần tính đầu tạo và lưu các phần; lần sau sach.count() có thể dùng lại phần còn lưu và trả 7. cache() tự nó không thực hiện tính toán ngay.

![Dữ liệu sau lọc được đánh dấu lưu đệm trước hành động đầu; hành động thứ hai dùng lại phần còn lưu.](img/lec-02/ch2-spark-dung-lai.svg)

RDD cache mặc định giữ trong bộ nhớ; nếu không đủ chỗ, một số phần không được giữ và có thể cần tính lại. Có các mức persist dùng bộ nhớ và đĩa. Việc lưu đệm có lợi khi dữ liệu được dùng lại và chi phí giữ nó phù hợp; không bảo đảm mọi dữ liệu đều vừa bộ nhớ hay mọi ứng dụng Spark đều nhanh hơn Hadoop MapReduce. Nguồn: MMDS 2.4.3, trang 46–47; Spark RDD Guide, RDD Persistence.

### Khôi phục theo lịch sử biến đổi

Spark ghi các phép biến đổi đã tạo RDD, gọi là dòng dõi. Nếu phần sạch của A mất, phần B còn lưu và tệp nguồn vẫn đọc được, có thể đọc lại A, tách từ và lọc để tái tạo phần cần dùng. Giữ nguyên phần B còn tồn tại.

![Phần sạch A bị mất được tái tạo từ HDFS qua tách và lọc; phần sạch B còn lưu được giữ nguyên.](img/lec-02/ch2-spark-khoi-phuc.svg)

Tình huống giả sử A/B thuộc hai phần riêng và không còn trung gian phù hợp cho A. Đây là chuỗi biến đổi theo từng phần; sau phép nhóm khóa, tính lại có thể phụ thuộc dữ liệu từ nhiều phần khác. Không đồng nhất một tài liệu với một phần trong mọi ứng dụng, cũng không coi cache là nơi lưu bền vững thay HDFS. Nguồn: MMDS Ví dụ 2.10, trang 47.

Hadoop MapReduce biểu diễn công việc theo Map, nhóm và Reduce; Spark cho phép diễn đạt chuỗi biến đổi RDD và dùng lại kết quả trung gian. Spark có thể đọc HDFS, nên lưu trữ và hệ tính toán phải được phân biệt. Trong ví dụ, reduceByKey là bước cần đưa các đóng góp cùng từ về cùng nơi. Điều này nối sang mục 2.5: muốn đánh giá, phải xác định mỗi tác vụ đọc hoặc nhận những dữ liệu nào.

## 2.5. Đếm dữ liệu mỗi tác vụ nhận

Phần trước đã xác định những bước xử lý và nơi dữ liệu được dùng lại. Phần này đo lượng dữ liệu các tác vụ phải nhận để thực hiện thuật toán. Ta dùng lại đếm từ và nhân ma trận–vector để biết từng số hạng đến từ đâu.

### Mô hình và hai nơi đặt bộ đếm

Theo MMDS 2.5.1, chi phí truyền thông của một tác vụ là kích thước đầu vào tác vụ, kể cả đọc cục bộ. Tổng chi phí là tổng trên tất cả tác vụ:

$$
C=\sum_u|\operatorname{in}(u)|.
$$

Với một công việc MapReduce, gọi $I$ là tổng byte đầu vào Map, $M$ là tổng byte đầu vào Reduce, tính đủ mọi bản gửi. Khi đó $C=I+M$. Ký hiệu $M$ ở đây không phải ma trận của mục 2.3. Phải thống nhất đơn vị trước khi cộng.

![Hai bộ đếm đo văn bản vào Map và các cặp vào Reduce.](img/lec-02/cost-input.svg)

Đầu ra cuối không được cộng trực tiếp theo quy ước này. Nếu tác vụ tiếp theo đọc nó, lần đọc ấy được tính là đầu vào của tác vụ đó. Đây là mô hình lượng dữ liệu nhận, không đo riêng byte trên dây mạng và không dự đoán thời gian chạy. Các slide tham khảo MMDS/Stanford có mô hình cộng cả đọc và ghi $I+2M+O$; bài này chọn mô hình đầu vào của sách theo nguồn chính, không trộn hai quy ước.

### Chạy lại phép đếm trên hai tài liệu

D1 chứa “dữ liệu lớn”, D2 chứa “lớn lớn”. D1 phát ba cặp $(\text{dữ},1)$, $(\text{liệu},1)$, $(\text{lớn},1)$; D2 phát hai cặp $(\text{lớn},1)$. Các cặp giống nhau vẫn được đếm riêng vì biểu diễn những lần xuất hiện khác nhau.

![Ba cặp của D1 và hai cặp của D2 tạo năm bản gửi trung gian.](img/lec-02/cost-five.svg)

Giả sử mỗi cặp có cùng độ dài $B$ byte. Reduce nhận $3B+2B=5B$ byte; Map vẫn đọc $I$ byte văn bản. Vì vậy $C=I+5B$. Hai tài liệu không đồng nghĩa với hai byte hay hai bản ghi cùng kích thước cặp.

![D2 gộp hai cặp lớn một thành một cặp lớn hai; D1 giữ ba cặp.](img/lec-02/cost-combine.svg)

Sau khi gộp cục bộ tại D2, Reduce nhận ba cặp từ D1 và một cặp $(\text{lớn},2)$ từ D2. Theo cùng giả thiết $B$, chi phí trở thành $I+4B$. Đầu vào Map không đổi, kết quả của từ “lớn” vẫn là $1+2=3$. Đây là phép đếm trên ví dụ minh họa của bài, không phải mức tiết kiệm đo trên dữ liệu thực. Nguồn: Ví dụ 2.1, mục 2.2.4 và mô hình 2.5.1.

### Ma trận và các tích: hai khoản khác nhau

Xét thuật toán chia dải ở mục 2.3.2, không gộp cục bộ các tích. Gọi $z$ là số phần tử ma trận được lưu. Mỗi tọa độ lưu đúng một bộ; phần tử không lưu được hiểu là 0. Dùng đơn vị chuẩn hóa: một bộ ma trận, một số vector và một cặp tích đều tính một đơn vị. Quy ước này không khẳng định chúng có cùng độ dài theo byte.

![Mỗi bộ ma trận được Map đọc và tạo một cặp tích để Reduce nhận.](img/lec-02/cost-matrix.svg)

Map nhận $z$ bộ ma trận. Mỗi bộ phát một cặp tích, nên Reduce nhận $z$ cặp. Hai khoản $z$ thuộc hai loại dữ liệu khác nhau; không phải ma trận được đọc hai lần. Ta còn phải đếm vector mà Map cần để tạo tích.

### Dải vector và số lần đọc

Gọi $L_j$ là số phần tử dải vector thứ $j$, $a_j$ là số tác vụ Map đọc toàn bộ dải đó. Ở phần này $j$ đánh số dải, không phải chỉ số cột trong công thức nhân ma trận. Nếu hai tác vụ xử lý hai phần ma trận cần cùng dải dài $L_j$, tổng dữ liệu vector chúng đọc là $L_j+L_j=2L_j$.

![Hai tác vụ đọc cùng một dải dài L j, tạo hai lần nhận dữ liệu.](img/lec-02/cost-stripe.svg)

Tổng quát, dải $j$ đóng góp $a_jL_j$ đơn vị. Cộng trên mọi dải cho $\sum_j a_jL_j$. Dải lưu một bản không có nghĩa nó chỉ được đọc một lần; ta đếm theo tác vụ nhận dữ liệu.

![Ba khoản chi phí gồm bộ ma trận, các lần đọc vector và cặp tích.](img/lec-02/cost-sum.svg)

Vì vậy:

$$
C=\underbrace{z}_{\text{ma trận vào Map}}+\underbrace{\sum_j a_jL_j}_{\text{vector vào Map}}+\underbrace{z}_{\text{tích vào Reduce}}=2z+\sum_j a_jL_j.
$$

Nếu mỗi dải có một tác vụ và các dải phủ vector dài $n$, thì $\sum_j L_j=n$, nên $C=2z+n$. Nếu mỗi dải có $a$ tác vụ, phần vector là $an$, nên $C=2z+an$. Với ma trận đặc, $z=n^2$.

Khi tính byte, gọi $B_M,B_v,B_P$ lần lượt là độ dài bộ ma trận, số vector và cặp tích. Khi đó $C=zB_M+(\sum_j a_jL_j)B_v+zB_P$. Đây là phép suy ra từ thuật toán và mô hình, không phải công thức trích nguyên văn nguồn. Nguồn: MMDS 2.3.2, 2.5.1 và Bài 2.5.1(a), trang 32, 54–55, 59.

### Tổng và nơi nhận nhiều nhất

![R0 nhận hai giá trị, R1 nhận ba; tổng năm và tải lớn nhất ba.](img/lec-02/cost-load.svg)

Quay lại trường hợp chưa gộp trong phân công đếm từ ở 2.2, riêng đầu vào Reduce có tổng $5B$ byte; tác vụ nặng nhất nhận $3B$ byte. Tổng dữ liệu giảm chưa đủ để kết luận thời gian giảm: còn tải lớn nhất, số máy, lịch thực thi, bộ nhớ và công việc tính toán. Mục 2.6 tiếp tục bằng một lựa chọn phân chia làm giảm số bản gửi nhưng tăng dữ liệu mỗi nơi phải nhận.

### Lợi ích thời gian của song song hóa

Tổng công việc và thời gian chờ kết quả là hai đại lượng khác nhau. Xét riêng tầng Reduce chưa gộp của ví dụ trên: R0 nhận 2 giá trị, R1 nhận 3 giá trị. Giả sử hai tác vụ độc lập, dữ liệu đã đến nơi xử lý, các máy có cùng tốc độ, mỗi giá trị mất $c>0$ đơn vị thời gian; bỏ qua khởi động và lập lịch. Đây là mô hình minh họa, không phải số đo thực tế.

![Một máy chạy R0 rồi R1 trong 5c; hai máy chạy đồng thời, hoàn tất sau 3c.](img/lec-02/cost-parallel-time.svg)

Một máy chạy nối tiếp nên $T_1=2c+3c=5c$. Hai máy chạy đồng thời nên thời điểm hoàn tất là $T_2=\max(2c,3c)=3c$. Mức tăng tốc là $T_1/T_2=5/3$, khoảng 1,67 lần. Tổng vẫn là 5 giá trị, tương ứng $5B$ byte đầu vào Reduce và $5c$ thời gian xử lý cộng trên hai máy. Lợi ích ở đây là người dùng nhận kết quả sớm hơn, không phải giảm tổng số thao tác hay tổng byte.

Nếu thêm máy thứ ba mà giữ nguyên hai tác vụ, thời gian vẫn là $3c$: không có tác vụ thứ ba để giao, và tác vụ dài nhất vẫn cần $3c$. Ngay với hai máy, máy xử lý R0 kết thúc sớm hơn và phải chờ R1 một khoảng $c$.

Gọi $W$ là tổng số đơn vị công việc, $p$ là số máy đồng tốc và $w_{\max}$ là công việc của tác vụ nặng nhất. Với các tác vụ độc lập không chia nhỏ, mỗi đơn vị mất $c$, tổng năng lực $p$ máy và tác vụ nặng nhất cho hai giới hạn:

$$
T_p\ge\max\left(\frac{Wc}{p},w_{\max}c\right).
$$

Vế thứ nhất đến từ việc phải thực hiện đủ $Wc$ thời gian xử lý trên $p$ máy. Vế thứ hai đến từ việc tác vụ nặng nhất phải chạy trọn trên một máy. Trong ví dụ, $W=5$, $w_{\max}=3$, nên hai máy không thể hoàn tất sau $2{,}5c$: tác vụ R1 đã cần $3c$.

Khi có đủ tác vụ và chia tải gần đều, thời gian lý tưởng gần $Wc/p$, tức tăng tốc gần $p$ lần so với $Wc$. Đây là điều kiện của mô hình, không phải bảo đảm cho mọi thuật toán. Thời gian toàn công việc MapReduce còn gồm các phần Map, chuyển dữ liệu, lập lịch và chờ phụ thuộc; các phần này có thể chồng lấp tùy cách thực thi, nên không cộng tùy tiện hoặc lấy thời gian tầng Reduce thay cho cả công việc.

Nguồn: lập luận về thời gian hoàn thành và chia đều tác vụ trong MMDS 2.5.2, trang 55–56; các phép tính trên suy ra từ mô hình thời gian giả định và vết đếm từ đã có. Phần 2.6 tiếp tục chọn cách phân chia để giảm bản gửi mà vẫn có đủ tác vụ sử dụng các máy.

## 2.6. Phân chia ảnh để giảm số bản gửi

### Bài toán và phương án từng cặp

Nguồn xét $N=10^6$ ảnh, mỗi ảnh $B=10^6$ byte. Các ảnh có mã duy nhất $1,\ldots,N$. Cho hàm độ tương tự đối xứng $s$ kết thúc trên mỗi cặp và ngưỡng $\tau$. Trả mỗi cặp $(i,j)$ thỏa $i<j$ và $s(P_i,P_j)>\tau$ đúng một lần. Trong mô hình này phải tính độ tương tự của mọi cặp ảnh khác nhau; chưa có cách bỏ qua cặp. Với ít hơn hai ảnh, kết quả rỗng. $B$ ở đây đo byte ảnh, khác $B$ đo byte cặp từ ở 2.5.

![Hai ảnh qua hàm độ tương tự, trả cặp chỉ số nếu vượt ngưỡng.](img/lec-02/cost-image-task.svg)

Map của ảnh $(i,P_i)$ duyệt mọi $j\ne i$ và phát ảnh đến khóa cặp $\{i,j\}$, biểu diễn chỉ số tăng dần. Reduce nhận hai ảnh của khóa, gọi $s$, phát cặp nếu vượt $\tau$. Mỗi cặp có duy nhất khóa và nhận đủ hai ảnh, nên xét đúng một lần. Các vòng duyệt hữu hạn nên thuật toán dừng theo giả thiết về $s$.

![Bốn ảnh đến sáu khóa cặp; mỗi ảnh có ba bản gửi và mỗi khóa nhận hai ảnh.](img/lec-02/cost-four.svg)

Hình dùng trường hợp bốn ảnh của Ví dụ 2.19, Hình 2.9 để nhìn thấy cách gửi. P1 đến ba khóa $\{1,2\},\{1,3\},\{1,4\}$. Các ảnh khác cũng có ba nơi nhận: tổng $4\times3=12$ bản gửi, tức $12B$ byte tải ảnh.

### Đếm byte từ ba yếu tố

Với $N$ ảnh, một ảnh có $N-1$ đối tác. Tổng tải ảnh trung gian bằng số ảnh nhân số nơi nhận mỗi ảnh nhân số byte mỗi ảnh:

$$
C_{\mathrm{ảnh}}=N(N-1)B\approx10^{18}\text{ byte}.
$$

![Ba yếu tố là số ảnh, số nơi nhận mỗi ảnh và byte mỗi ảnh.](img/lec-02/cost-bytes-pair.svg)

Công thức chỉ tính tải ảnh Map gửi tới Reduce, bỏ qua nhãn cặp và chi phí phụ. Nếu áp dụng tổng chi phí của 2.5 trong cùng mô hình tải ảnh, cần cộng thêm đầu vào Map $NB$. Không gọi phần trung gian này là toàn bộ chi phí của công việc.

### Đặt tên các đại lượng để so sánh phân chia

Gọi $q$ là cận trên số giá trị của một khóa Reduce; gọi $\rho$ là số cặp trung gian trung bình phát ra trên một đầu vào. Sách dùng $r$ cho đại lượng thứ hai. Trong mô hình mục 2.6, “reducer” gắn với một khóa, không phải một máy hay một tác vụ xử lý nhiều khóa ở mục 2.2.

$$
\rho=\frac{\text{tổng số cặp trung gian phát}}{\text{số phần tử đầu vào}}.
$$

![Từ hình bốn ảnh: mỗi ảnh gửi ba nơi, mỗi khóa nhận hai ảnh.](img/lec-02/cost-qr.svg)

Với bốn ảnh, $q=2$, $\rho=3$. Với toàn bộ kho ảnh, $q=2$, $\rho=N-1=999999$. Đây là số bản gửi trung gian, không phải số bản sao khối trong hệ tệp. Nếu mỗi giá trị dài $B$ byte, tải ảnh tối đa là $qB$; bộ nhớ chạy thuật toán còn phụ thuộc cách giữ dữ liệu và vùng làm việc của $s$.

### Gom nhóm để dùng lại ảnh đã nhận

Chia đều $N=10^6$ ảnh thành $g=1000$ nhóm, mỗi nhóm $N/g=1000$ ảnh. Map gửi ảnh nhóm $u$ đến mọi khóa cặp nhóm $\{u,v\}$ với $v\ne u$, kèm mã nhóm và mã ảnh. Mỗi khóa nhận hai nhóm để so sánh nhiều cặp bằng dữ liệu đã có.

![Một khóa nhận hai nhóm, mỗi nhóm 1000 ảnh, tổng 2000 ảnh.](img/lec-02/cost-groups.svg)

Một khóa nhận $2N/g=2000$ ảnh nên chọn $q=2000$. Mỗi nhóm ghép với $g-1=999$ nhóm khác, nên mỗi ảnh gửi đến 999 khóa và $\rho=999$.

![Mỗi ảnh nhóm u gửi đến các cặp nhóm chứa u; mỗi nơi nhận hai nhóm.](img/lec-02/cost-group-count.svg)

Ba yếu tố tính byte vẫn như trước, chỉ số nơi nhận thay từ $N-1$ thành $g-1$:

$$
C_{\mathrm{ảnh}}=N(g-1)B=9{,}99\times10^{14}\text{ byte}.
$$

![Gom nhóm thay 999999 nơi nhận mỗi ảnh bằng 999 nơi, cùng số ảnh và kích thước ảnh.](img/lec-02/cost-bytes-group.svg)

Mỗi nơi nay nhận $2000\times10^6=2\times10^9$ byte ảnh, tức 2 GB thập phân. Phạm vi vẫn chỉ là tải ảnh; tổng mô hình 2.5 cần thêm $NB$. Chia đều ở đây dùng dữ kiện của sách; không áp dụng nguyên xi cho mọi $N,g$.

### Bao phủ các cặp và tính đúng

Reduce so sánh mọi cặp chéo hai nhóm. Các cặp trong cùng một nhóm cần được giao riêng, nếu không sẽ bị xét lặp ở mọi nơi chứa nhóm đó. Đánh số nhóm $0,\ldots,g-1$ với $g=1000$; giao các cặp nội bộ nhóm $u$ cho khóa $\{u,(u+1)\bmod g\}$. Chỉ phát cặp chỉ số tăng dần khi độ tương tự vượt ngưỡng.

![Bốn cặp chéo và một cặp nội bộ được giao riêng trên phần trích hai ảnh mỗi nhóm.](img/lec-02/ch2-cap-nhom-anh.svg)

Mỗi cặp khác nhóm có duy nhất cặp nhóm chứa nó. Mỗi cặp cùng nhóm có duy nhất nơi được giao theo vòng. Hai loại không giao nhau và phủ toàn bộ cặp khác ảnh: thuật toán không bỏ sót hoặc xét lặp. Dữ liệu hữu hạn và $s$ kết thúc nên thuật toán dừng. Hình chỉ trích hai ảnh mỗi nhóm; cặp nội bộ nhóm kế tiếp được xử lý ở nơi được giao cho nhóm đó.

### Số so sánh và đánh đổi

Mỗi ảnh có $N-1$ đối tác. Tích $N(N-1)$ đếm cả $(i,j)$ lẫn $(j,i)$, nên chia hai để lấy số cặp khác nhau. Cả hai phương án cần $N(N-1)/2=499\,999\,500\,000$ lần gọi $s$.

![Sáu ô phía trên đường chéo của lưới bốn ảnh biểu diễn sáu cặp; các ô dưới lặp thứ tự.](img/lec-02/cost-comparisons.svg)

Cách từng cặp gọi $s$ một lần tại mỗi khóa. Cách nhóm có $1000^2=1\,000\,000$ cặp chéo tại mỗi khóa; nơi được giao nội bộ một nhóm cần thêm $1000\cdot999/2=499\,500$ lần gọi. Tải lớn nhất là $1\,499\,500$ lần gọi. Kiểm tra tổng: $\binom{1000}{2}\cdot1000^2+1000\binom{1000}{2}=499\,999\,500\,000$.

Nếu mỗi lần gọi có chi phí cố định $c_s$, công việc tính độ tương tự là $c_sN(N-1)/2$. Nếu chi phí thay đổi, phải cộng chi phí từng lần gọi. Chưa tính tạo bản gửi, nhóm khóa, truyền ảnh và ghi đầu ra. Gom nhóm giảm lượng ảnh truyền nhờ dùng lại dữ liệu; số cặp cần so sánh không giảm. Cần kiểm tra bộ nhớ phụ và chi phí của $s$ trước khi kết luận một nơi nhận 2 GB có thể chạy được.

Với 1000 nhóm, có $1000\cdot999/2=499500$ khóa cặp nhóm. Có thể phân các khóa này vào số tác vụ phù hợp với số máy sẵn có, như sách giải thích ở trang 64. Gom nhóm vừa phải giảm bản gửi, vừa phải giữ đủ công việc độc lập để các máy làm đồng thời; số khóa không phải số máy hoặc mức tăng tốc.

Nguồn: MMDS 2.6.1–2.6.2, trang 61–64; ví dụ bốn ảnh từ 2.6.3, Hình 2.9, trang 64–65. Phần lược đồ ánh xạ và chứng minh cận dưới ở 2.6.3–2.6.7 dành để đọc thêm.

## 2.7. Tổng kết và bài tập

Chọn khóa quyết định dữ liệu nào gặp nhau. Lập luận đúng cần chỉ ra mọi đóng góp cần thiết đều gặp nhau và không bị mất hoặc lặp. Lập bảng đầu vào từng tầng cho biết hệ số sao chép xuất hiện ở đâu; sau đó vẫn phải kiểm tra tải lớn nhất, bộ nhớ và chi phí tạo kết quả.

Các bài dưới đây dịch và tách ý từ đúng bài tập nguồn. Không thay dữ kiện hay yêu cầu toán học. Bài 2.5.1 chỉ chọn ý (a), phù hợp thuật toán nhân ma trận–vector đã học.

### Bài tập 2.2.1 — Lệch tải khi đếm từ

::: exercise
Đếm từ trên kho rất lớn, chẳng hạn một bản sao kho trang Web, dùng 100 tác vụ Map.

(a) Không dùng bộ kết hợp ở Map. Thời gian các reducer xử lý danh sách giá trị có lệch đáng kể không? Giải thích.

(b) Gán ngẫu nhiên các reducer vào 10 tác vụ Reduce. Mức lệch có đáng kể không? So sánh với 10000 tác vụ Reduce.

(c) Dùng bộ kết hợp tại 100 tác vụ Map. Mức lệch có còn đáng kể không? Giải thích.

Sản phẩm: lời giải dựa trên độ dài danh sách và cách gán khóa. Nguồn: trang 30, PDF 11.
:::

::: solution
(a) Với phân bố từ tự nhiên, từ phổ biến có danh sách dài hơn nhiều từ hiếm, nên thời gian reduce có thể lệch đáng kể. Không khẳng định mọi dữ liệu đều lệch.

(b) Mười tác vụ thường nhận nhiều khóa mỗi tác vụ, giúp tổng tải được san đều hơn khi gán ngẫu nhiên. Với 10000 tác vụ, một số từ phổ biến dễ chi phối tác vụ chứa chúng hơn. Khóa cực lớn vẫn có thể gây lệch ở cả hai cách; gán ngẫu nhiên không chia nhỏ một khóa. Chưa đủ dữ kiện để kết luận cách nào có thời gian hoàn thành ngắn hơn.

(c) Trong mô hình mỗi tác vụ gộp hoàn toàn từng từ thành một tổng, mỗi từ tạo tối đa 100 giá trị tới Reduce. Danh sách từ phổ biến ngắn đi mạnh nên lệch giảm. Triển khai bộ kết hợp nhiều lần trên nhiều mảnh chưa chắc cho cận 100 này. Map vẫn có thể lệch tải.
:::

### Bài tập 2.3.1 — Thiết kế thuật toán

::: exercise
Cho một tệp số nguyên rất lớn. Thiết kế MapReduce để trả:

(a) Số nguyên lớn nhất.

(b) Trung bình tất cả số nguyên.

(c) Cùng tập số nguyên, mỗi số chỉ xuất hiện một lần.

(d) Số lượng số nguyên khác nhau.

Khóa của cặp đầu ra có thể bị bỏ qua. Sản phẩm: giả mã, ý nghĩa trạng thái và lập luận đúng. Nguồn: trang 40, PDF 21.
:::

::: solution
(a) Map phát (0,x), reduce lấy max. Có thể gộp max cục bộ. Khởi tạo từ phần tử đầu hoặc âm vô cùng, không từ 0 vì đầu vào có thể toàn số âm. Tệp rỗng không có phần tử lớn nhất.

(b) Map phát (0,(x,1)). Reduce cộng hai thành phần thành $(S,N)$ rồi trả $S/N$ khi $N>0$. Bộ kết hợp giữ cùng kiểu trạng thái. Bất biến: $S$ là tổng, $N$ là số phần tử đã đọc. Tệp rỗng không có trung bình.

(c) Map phát (x,1); reduce của mỗi x phát x một lần. Mọi bản sao x về cùng khóa, nên giữ đủ các giá trị khác nhau mà không trùng. Không bảo đảm thứ tự đầu ra.

(d) Một phương án hai công việc: công việc đầu nhóm theo x và phát một số 1 cho mỗi khóa; công việc sau cộng các số 1. Nếu có $D$ giá trị khác nhau, có đúng $D$ đóng góp. Tệp rỗng cần quy ước trả 0. Hai công việc không phải điều kiện bắt buộc trong mọi mô hình: gom mọi số về một reducer rồi dùng tập hợp cũng được, nhưng cần bộ nhớ theo số giá trị khác nhau.
:::

Để đánh giá các lời giải trên, gọi $N$ là số phần tử đầu vào và $D$ là số giá trị phân biệt; chưa dùng bộ kết hợp. Đếm bản ghi theo đơn vị chuẩn hóa, không coi các kiểu bản ghi có cùng số byte. Trong mô hình số học đơn vị, đọc một giá trị và cập nhật một số lượng hữu hạn biến có chi phí hằng số. Chi phí hệ thống nhóm khóa, khởi tạo và ghi kết quả cuối được tách riêng.

| Lời giải | Đặc tả đầu ra và ca rỗng | Công việc xử lý giá trị | Bộ nhớ phụ một reducer | Tổng bản ghi đầu vào các tầng |
|---|---|---|---|---|
| (a) Lớn nhất | Một giá trị lớn nhất; không xác định nếu rỗng | $N-1$ lần so sánh khi $N>0$, khởi tạo từ phần tử đầu | Một giá trị đang lớn nhất | $2N$ |
| (b) Trung bình | $S/N$ khi $N>0$; không xác định nếu rỗng | $N$ lần cộng mỗi thành phần, một lần chia | Tổng và số lượng | $2N$ |
| (c) Loại trùng | Đúng một bản mỗi giá trị; rỗng trả rỗng | Duyệt $N$ giá trị, phát $D$ kết quả | Trạng thái hằng số khi duyệt từng nhóm, ngoài khóa | $2N$ |
| (d) Đếm giá trị khác nhau | Đúng $D$; rỗng trả 0 theo quy ước | Duyệt $N$ giá trị ở công việc đầu, cộng $D$ số 1 ở công việc sau | Trạng thái hằng số mỗi lần gọi, ngoài khóa | $2N+2D$ |

Ở (d), công việc đầu nhận $N$ bản ghi tại Map và $N$ tại Reduce; công việc sau nhận $D$ tại Map và $D$ tại Reduce. Với đầu vào rỗng, không có khóa kích hoạt Reduce; bên gọi phải trả 0 khi không có đầu ra. Các cận bộ nhớ không gồm vùng nhóm, bộ đệm hoặc bảng của hệ thống. Bảng là phân tích các lời giải của Bài 2.3.1 (trang 40) theo mô hình mục 2.5.1 (trang 52–53), không thêm yêu cầu vào đề bài.

### Bài tập 2.5.1(a) — Tính chi phí

::: exercise
Biểu diễn chi phí truyền thông theo kích thước ma trận và vector:

(a) Thuật toán nhân ma trận–vector ở mục 2.3.2.


Sản phẩm: định nghĩa đơn vị, bảng đầu vào Map/Reduce và công thức tổng. Nguồn: trang 59, PDF 40.
:::

::: solution
(a) Gọi $z$ là số phần tử ma trận được lưu, $L_j$ là độ dài dải vector $j$, $a_j$ là số tác vụ Map đọc dải đó. Không gộp cục bộ các tích. Với đơn vị chuẩn hóa:

| Tầng | Đầu vào |
|---|---|
| Map | $z+\sum_j a_jL_j$ |
| Reduce | $z$ |
| Tổng | $2z+\sum_j a_jL_j$ |

Nếu mỗi dải chỉ được một tác vụ đọc và $\sum_jL_j=n$ thì $C=2z+n$. Ma trận đặc có $z=n^2$. Không mặc định vector chỉ được đọc một lần khi một dải phục vụ nhiều tác vụ.

Nếu một bộ ma trận dài $B_M$ byte, một phần tử vector dài $B_v$ byte và một cặp tích dài $B_P$ byte, công thức là $zB_M+(\sum_j a_jL_j)B_v+zB_P$.

:::

## 2.8. Tài liệu tham khảo và hướng đọc

Leskovec, Rajaraman, Ullman. *Mining of Massive Datasets*, Chương 2: *MapReduce and the New Software Stack*, bản `ch2n.pdf`, trang in 20–79. [Trang sách và slide của tác giả](http://www.mmds.org).

Mục 2.8, trang 77–79, liệt kê các tài liệu gốc về hệ tệp, MapReduce và hệ xử lý mở rộng. Ôn mục 2.2–2.3 để viết thuật toán, sau đó dùng 2.5 để đánh giá. Đọc 2.6.3–2.6.7 khi đã nắm $q$, $\rho$ và muốn học các chứng minh cận dưới. Các con số ví dụ hệ thống trong chương giữ vai trò minh họa lịch sử, không được dùng như thông số công nghệ hiện tại.
