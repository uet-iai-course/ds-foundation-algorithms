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

Với $N$ lần xuất hiện, map phát $N$ cặp nếu chưa gộp. Reduce của một từ xuất hiện $f$ lần thực hiện $O(f)$ phép cộng và cần một biến tổng khi đọc tuần tự. Các phát biểu này dùng mô hình số học đơn vị; nhóm, truyền dữ liệu và lưu trữ của hệ thống vẫn có chi phí riêng.

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
    phát(i, tổng các giá trị trong V)
```

::: proof
Mỗi phần tử lưu $(i,j,m_{ij})$ đóng góp đúng tích $m_{ij}v_j$ tới hàng $i$, đúng một lần. Nhóm theo $i$ thu đủ các tích của hàng ấy. Bất biến cộng tổng của phần đếm từ áp dụng lại, nên reduce trả đúng $x_i$. Các phần tử 0 bị lược không làm đổi tổng. Hàng không phát cặp phải được hiểu có kết quả 0 hoặc được bổ sung 0 theo quy ước biểu diễn đầu ra.

Lập luận xét số học chính xác. Với số dấu phẩy động, đổi thứ tự cộng có thể làm sai khác nhỏ kết quả tính máy.
:::

Nếu vector không vừa bộ nhớ, chia ma trận thành các dải dọc và vector thành các dải tương ứng. Một tác vụ đọc phần ma trận của dải và dải vector cùng chỉ số. Mọi tích vẫn mang khóa hàng, nên reduce cộng cả các đóng góp từ những dải khác nhau.

![Năm dải dọc của ma trận ghép với năm dải vector tương ứng, theo Hình 2.4.](img/lec-02/ch2-dai-ma-tran.svg)

Các dải chia miền cột thành những phần không giao nhau và phủ hết miền cột. Vì thế mỗi tích được tạo đúng một lần, dù các tích của một hàng xuất phát từ nhiều dải. Điều kiện bộ nhớ áp dụng cho dải vector và trạng thái tác vụ, không chỉ cho số dải. Có thể nhiều tác vụ đọc cùng dải vector; khi tính chi phí phải đếm những lần đọc đó. Nguồn: mục 2.3.1–2.3.2, trang 31–32, Hình 2.4.

## 2.4. Mở rộng MapReduce

MapReduce có hai tầng tính toán chính. Hệ luồng công việc mở rộng thành một đồ thị có hướng không chu trình của các hàm: cung từ $f$ tới $g$ nghĩa là đầu ra của $f$ cung cấp đầu vào cho $g$. Mỗi hàm có thể được thực thi bởi nhiều tác vụ. Phải phân biệt đồ thị các hàm với tập tác vụ thực tế được lập lịch trên máy.

![Đồ thị năm hàm: f đưa vào g và i; h đưa vào i và j; g và i đưa vào j.](img/lec-02/ch2-luong-cong-viec.svg)

Hình vẽ lại Hình 2.6, trang 42. Mỗi tác vụ chỉ chuyển đầu ra sau khi hoàn tất theo tính chất chặn được mô tả ở trang 43; khi hỏng trước lúc đó, tác vụ có thể được chạy lại mà chưa tạo đầu ra trùng cho bước kế tiếp.

Chương giới thiệu Spark qua **tập dữ liệu phân tán có khả năng khôi phục (RDD)**: các phần tử cùng kiểu được chia trên nhiều máy. Kiểu phần tử không bị giới hạn là cặp khóa–giá trị.

| Phép biến đổi | Tác động lên một phần tử |
|---|---|
| Map | Trả đúng một đối tượng |
| Flatmap | Trả không, một hoặc nhiều phần tử |
| Filter | Giữ phần tử nếu vị từ trả đúng |

Trong Ví dụ 2.7, Map có thể biến một tài liệu thành một danh sách cặp (từ,1), nhưng danh sách ấy vẫn là một đối tượng đầu ra. Flatmap phát từng cặp riêng cho từng lần xuất hiện. Không được bỏ các cặp trùng như thể RDD là tập hợp toán học không có lặp.

Dùng lại tài liệu minh họa D2 = “lớn lớn”: Map có thể trả một đối tượng là danh sách [(lớn,1), (lớn,1)]; Flatmap trả hai phần tử (lớn,1) riêng biệt. Đây là áp dụng phép biến đổi của Ví dụ 2.7 vào dữ kiện đã dùng trong bài.

Ví dụ 2.8 dùng Filter để loại những cặp có từ trong danh sách từ dừng. Một từ dừng xuất hiện ba lần sẽ bị loại cả ba cặp.

![Tài liệu được Flatmap thành R1 rồi Filter thành R2; lịch sử biến đổi cho phép tính lại phần bị mất.](img/lec-02/ch2-spark.svg)

Các phép biến đổi mô tả cách tạo dữ liệu; một hành động, chẳng hạn yêu cầu kết quả, kích hoạt tính toán. Lưu đệm cho phép dùng lại dữ liệu đã tính. Lịch sử biến đổi ghi cách khôi phục: từ tệp tài liệu, áp dụng Flatmap rồi Filter để tái tạo phần R2 cần thiết. Chuỗi trên xử lý theo từng phần; các phép biến đổi khác có thể phải trao đổi dữ liệu giữa các máy.

Reduce của Spark được chương mô tả là hành động tổng hợp thành một giá trị, khác với reduce được gọi theo từng khóa của MapReduce. Không suy ra mọi công việc Spark luôn nằm trong RAM hoặc luôn nhanh hơn MapReduce. Tính khả thi còn phụ thuộc dữ liệu, phép biến đổi và bộ nhớ. Nguồn: 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10. TensorFlow, mở rộng đệ quy và hệ đồng bộ theo từng bước ở 2.4.4–2.4.6 là đọc thêm.

## 2.5. Mô hình chi phí truyền thông

### Quy ước trước khi tính

Mục 2.5 định nghĩa chi phí truyền thông của một tác vụ là kích thước đầu vào tác vụ; tổng chi phí là tổng trên tất cả tác vụ:

$$
C=\sum_u|\operatorname{in}(u)|.
$$

Với một công việc MapReduce, gọi $I$ là tổng đầu vào Map, $M$ là tổng đầu vào Reduce sau khi tính đủ các bản sao. Khi đó $C=I+M$. Ký hiệu $M$ ở phần này là kích thước trung gian, không phải ma trận ở mục 2.3. Cả đọc cục bộ cũng nằm trong phép đếm. Đây không phải công thức đo riêng byte đi trên dây mạng.

![Mô hình cộng đầu vào Map I và đầu vào Reduce M; không cộng trực tiếp đầu ra cuối.](img/lec-02/ch2-chi-phi.svg)

Phải dùng một đơn vị nhất quán: byte hoặc bản ghi chuẩn hóa. Nếu độ dài bộ và cặp khác nhau thì nhân số lượng với độ dài tương ứng. Trong chuỗi nhiều công việc, đầu ra của công việc trước được đếm khi tác vụ sau đọc nó. Kết quả cuối không được cộng trực tiếp theo quy ước này; trong hệ thống thật, tạo và ghi kết quả vẫn tốn tài nguyên.

Với vết đếm từ, Map đọc lượng dữ liệu $I$. Chưa gộp thì Reduce nhận 5 cặp; gộp hai lần xuất hiện ở D2 thì nhận 4 cặp. Nếu mỗi cặp dài $B$ byte, hai chi phí là $I+5B$ và $I+4B$, với $I$ tính bằng byte. Không đồng nhất hai tài liệu với hai cặp có kích thước bằng nhau.

### Chi phí nhân ma trận–vector

Quay lại cách chia dải ở mục 2.3.2. Gọi $z$ là số phần tử ma trận được lưu, $L_j$ là độ dài dải vector $j$, $a_j$ là số tác vụ đọc dải đó. Ở đây $j$ đánh số dải. Không gộp cục bộ các tích; dùng đơn vị bản ghi chuẩn hóa.

| Tầng nhận | Lượng dữ liệu | Căn cứ |
|---|---|---|
| Map: ma trận | $z$ | Mỗi phần tử đọc một lần |
| Map: vector | $\sum_j a_jL_j$ | Dải $j$ được đọc $a_j$ lần |
| Reduce | $z$ | Mỗi phần tử phát một tích |

Vì vậy $C=2z+\sum_j a_jL_j$. Nếu mỗi dải có một tác vụ và tổng độ dài vector là $n$, chi phí là $2z+n$. Nếu mỗi dải có $a$ tác vụ thì chi phí thành $2z+an$. Hai trường hợp này suy ra từ công thức, không phải kết quả đo thực nghiệm. Với ma trận đặc, $z=n^2$.

Đơn vị chuẩn hóa không khẳng định mọi loại bản ghi dài bằng nhau theo byte. Nếu độ dài lần lượt là $B_M,B_v,B_P$ byte thì $C=zB_M+(\sum_j a_jL_j)B_v+zB_P$. Chia thêm tác vụ có thể tăng số lần đọc vector; tổng này chưa xác định thời gian thực hoặc tải bộ nhớ lớn nhất. Nguồn: MMDS 2.3.2, 2.5.1 và Bài tập 2.5.1(a), trang 32,54–55,59.

## 2.6. Bộ nhớ và sao chép dữ liệu

Để diễn tả đánh đổi, đặt $q$ là số giá trị đầu vào tối đa một reducer nhận và $\rho$ là số cặp trung gian trung bình trên một đầu vào. Sách dùng $r$ cho đại lượng thứ hai; bài dùng ký hiệu $\rho$ cho đại lượng này.

$$
\rho=\frac{\text{số cặp trung gian phát}}{\text{số phần tử đầu vào}}.
$$

Nếu mỗi giá trị có $B$ byte và reducer giữ đồng thời toàn bộ đầu vào thì phần dữ liệu chiếm tối đa $qB$ byte, chưa tính cấu trúc phụ. $\rho$ không phải số bản sao của khối trong hệ tệp.

### So sánh mọi cặp ảnh

Mục 2.6.2 xét $N=10^6$ ảnh, mỗi ảnh $B=10^6$ byte. Cho hàm độ tương tự đối xứng $s(P_i,P_j)$ và ngưỡng $\tau$; đầu ra gồm các cặp ảnh khác nhau có $s(P_i,P_j)>\tau$. Trong mô hình của nguồn, cần tính độ tương tự cho mọi cặp để quyết định có phát cặp đó hay không. Sách dùng $t$ cho ngưỡng; bài dùng ký hiệu $\tau$. $B$ là số byte mỗi ảnh; ở ví dụ đếm từ, $B$ là số byte mỗi cặp. Một reducer cho mỗi cặp nhận hai ảnh, nên $q=2$. Mỗi ảnh được gửi tới $N-1$ reducer:

$$
\rho=N-1=999999,\qquad C_{\mathrm{trung\ gian}}=N(N-1)B\approx10^{18}\text{ byte}.
$$

Gom ảnh thành $g=1000$ nhóm, mỗi nhóm 1000 ảnh. Mỗi reducer nhận hai nhóm để so sánh chéo; một ảnh đi tới $g-1=999$ reducer. Khi đó

$$
q=2000,\quad \rho=999,\quad C_{\mathrm{trung\ gian}}=9{,}99\cdot10^{14}\text{ byte}.
$$

Dữ liệu ảnh của một reducer là $2\cdot10^9$ byte, tức 2 GB theo đơn vị thập phân, chưa gồm chi phí phụ. Cả hai công thức trên chỉ tính trung gian; nếu dùng tổng của mục 2.5 cần cộng đầu vào Map $NB$.

Mỗi cặp khác nhóm được xét đúng một nơi. Để xét cặp trong cùng nhóm mà không lặp, đánh số nhóm 0 đến $g-1$ và giao các cặp nội bộ nhóm $i$ cho reducer chứa nhóm $i$ và nhóm $(i+1)\bmod g$. Không để mọi reducer có nhóm $i$ đều lặp lại các cặp nội bộ.

Cách gom nhóm giảm truyền ảnh nhờ dùng lại ảnh cho nhiều phép so sánh. Tổng số cặp cần so sánh vẫn là $N(N-1)/2$; không giảm thành tuyến tính theo $N$. Cần kiểm tra bộ nhớ và chi phí so sánh trước khi chọn kích thước nhóm. Nguồn: mục 2.6.1–2.6.2, trang 61–64. Lược đồ ánh xạ và chứng minh cận dưới ở 2.6.3–2.6.7 là đọc thêm.

![Bên trong reducer của hai nhóm kề nhau: bốn cặp chéo trên phần trích nối nét liền; cặp nội bộ nhóm u nối nét đứt và chỉ được giao ở đây.](img/lec-02/ch2-cap-nhom-anh.svg)

Hình minh họa quy tắc của mục 2.6.2, trang 63–64, với $v=(u+1)\bmod g$ và cách đánh số nhóm $0,\ldots,g-1$. Các ký hiệu ảnh chỉ đại diện cho một phần của mỗi nhóm 1000 ảnh. Reducer xét mọi cặp chéo hai nhóm và các cặp nội bộ nhóm $u$ được giao riêng; cặp nội bộ nhóm $v$ thuộc reducer kế tiếp của $v$. Chỉ các cặp vượt ngưỡng tương tự được phát ra.

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
