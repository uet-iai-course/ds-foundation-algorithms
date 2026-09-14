# Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

Bài này giải thích cách tổ chức phép tính khi dữ liệu nằm trên nhiều máy: chia dữ liệu, chọn khóa để các đóng góp cần nhau gặp nhau, rồi đánh giá lượng dữ liệu phải đọc và truyền. Sau bài học, người học cần viết được map/reduce cho các phép tính cơ bản, giải thích tính đúng và lập bảng chi phí với đơn vị rõ ràng.

Nguồn chính là *Mining of Massive Datasets* (Leskovec, Rajaraman, Ullman), Chương 2, bản `ch2n.pdf` được chỉ định cho học phần. Các số trang dưới đây là **trang in**; số trang PDF bằng số trang in trừ 19; ví dụ trang in 30 là trang PDF 11. Thứ tự các phần giữ nguyên mục 2.1–2.8. Kiến thức đầu vào gồm vòng lặp, hàm, bảng băm, tổng hữu hạn và phép nhân ma trận–vector. Các thuật ngữ hệ phân tán và quan hệ được giải thích trước khi dùng.

[Bộ trang chiếu Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) · [Sách và học liệu MMDS](http://www.mmds.org)

## 2.1. Hệ tệp phân tán

Một kho dữ liệu lớn có thể vượt khả năng lưu trữ hoặc xử lý của một máy. Cụm máy chia công việc cho nhiều máy nối qua mạng. Các máy thường được đặt trong tủ máy; truyền giữa các tủ phải đi qua mạng kết nối. Vì vậy, vị trí dữ liệu có ảnh hưởng tới chi phí thực hiện phép tính.

Nhiều thành phần cũng tạo nhiều vị trí có thể hỏng. Một máy mất có thể làm mất dữ liệu cục bộ; lỗi mạng của một tủ có thể khiến nhiều máy cùng không truy cập được. Hai cơ chế bổ trợ nhau là lưu nhiều bản sao và chia phép tính thành tác vụ có thể chạy lại.

**Hệ tệp phân tán (DFS)** chia một tệp lớn thành các khối và lưu bản sao của khối ở nhiều máy. Đặt bản sao ở các tủ khác nhau giúp tránh mất mọi bản sao khi một tủ hỏng. Siêu dữ liệu cho biết khối của tệp nằm ở đâu. Máy quản lý siêu dữ liệu và tệp siêu dữ liệu là hai đối tượng khác nhau.

![Ba khối có hai bản sao trên ba máy; vị trí bản sao cho phép đọc lại khi mất một máy.](img/lec-02/ch2-khoi-ban-sao.svg)

Hình minh họa cơ chế bằng ba khối và hai bản sao mỗi khối; đây không phải cấu hình bắt buộc của một hệ thống. Khi máy A hỏng, các khối mà nó giữ còn có bản sao ở B hoặc C. Bảo đảm này chỉ đúng nếu còn ít nhất một bản sao truy cập được. Đặt tác vụ gần bản sao đầu vào giúp giảm dữ liệu phải truyền qua mạng.

Môi trường trong chương hướng tới tệp rất lớn, ít cập nhật tại chỗ. Không nên từ đó suy ra mọi cơ sở dữ liệu giao dịch đều thích hợp với cùng mô hình. Hệ tệp giải quyết lưu trữ; phần tiếp theo giải quyết cách phối hợp tính toán. Nguồn: mục 2.1, trang 22–24.

## 2.2. Mô hình MapReduce

### Đầu vào, đầu ra và khóa

Xét bài toán đếm số lần xuất hiện của từng từ trong kho tài liệu. Giả sử cách tách từ đã được xác định. Đầu ra chứa một cặp gồm từ và số lần xuất hiện cho mỗi từ xuất hiện ít nhất một lần. Kho rỗng cho đầu ra rỗng.

MapReduce chia trách nhiệm thành ba bước:

1. Hàm map đọc từng phần đầu vào và phát các cặp khóa–giá trị.
2. Hệ thống nhóm mọi giá trị có cùng khóa, rồi đưa nhóm tới nơi xử lý.
3. Hàm reduce nhận một khóa cùng các giá trị của nó và tạo kết quả.

Trong bài toán đếm từ, khóa là từ, giá trị là một đóng góp đếm. Ví dụ 2.1 của sách mô tả tài liệu $w_1,w_2,\ldots,w_n$ phát $(w_1,1),\ldots,(w_n,1)$. Những cặp bằng nhau vẫn phải được giữ: mỗi cặp biểu diễn một lần xuất hiện.

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

### Khôi phục khi máy hỏng

Theo mô hình MapReduce của chương, đầu vào và đầu ra cuối ở hệ tệp phân tán; đầu ra Map trung gian nằm trên đĩa cục bộ. Nếu máy Map mất, cả tác vụ đang chạy và tác vụ đã xong có trung gian bị mất có thể phải chạy lại. Nếu máy Reduce mất, tác vụ đang chạy được đưa về hàng chờ; kết quả đã hoàn tất trong hệ tệp phân tán vẫn còn theo giả thiết lưu trữ của mô hình.

Cần phân biệt chịu lỗi tác vụ với chịu mọi dạng lỗi. Chương cũng xét lỗi bộ điều phối, có thể đòi hỏi khởi động lại công việc. Nguồn: mục 2.2, trang 25–30, Ví dụ 2.1–2.2.

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

### Quan hệ, phép chọn và phép chiếu

Trong phần này, quan hệ là tập các bộ: mỗi bộ là một hàng, thuộc tính là một cột. Không mặc định đây là ngữ nghĩa bảng cho phép lặp của mọi hệ SQL. Hình 2.5 trích quan hệ Links(From,To):

| From | To |
|---|---|
| url1 | url2 |
| url1 | url3 |
| url2 | url3 |
| url2 | url4 |

Phép chọn giữ những hàng thỏa điều kiện. Áp dụng phép chọn của mục 2.3.4 lên phần trích ở Hình 2.5 với điều kiện From = url1 sẽ giữ hai hàng đầu. Map kiểm tra từng bộ, phát bộ thỏa điều kiện; reduce có thể chỉ chuyển tiếp. Tính đúng đi trực tiếp từ vị từ: mỗi hàng đầu ra thỏa điều kiện, mỗi hàng đầu vào thỏa điều kiện đều được giữ.

Phép chiếu lấy các cột chỉ định rồi bỏ bộ trùng theo ngữ nghĩa tập hợp. Áp dụng phép chiếu của mục 2.3.5 lên phần trích Links (Hình 2.5), cột From cho các giá trị url1, url1, url2, url2 trước khi bỏ trùng. Map dùng phần chiếu làm khóa; reduce phát một lần cho mỗi khóa. Kết quả là {url1, url2}. Nếu chỉ bỏ cột mà không bỏ trùng thì chưa thực hiện phép chiếu tập hợp. Nguồn: mục 2.3.3–2.3.5, trang 32–35; Hình 2.5 và Ví dụ 2.3.

### Phép nối tự nhiên

Cho $R(A,B)$ và $S(B,C)$. Phép nối tạo mọi $(a,b,c)$ sao cho $(a,b)\in R$ và $(b,c)\in S$. Khóa chung $b$ là nơi hai bộ cần gặp nhau. Nhãn nguồn trong giá trị giúp phân biệt phía trái và phía phải.



::: example
Dùng hai bản sao của phần trích Links: $L_1(U_1,U_2)$ và $L_2(U_2,U_3)$. Đầu ra mô tả đường đi dài hai.

| Khóa $U_2$ | Từ $L_1$ | Từ $L_2$ |
|---|---|---|
| url1 | không có | url2, url3 |
| url2 | url1 | url3, url4 |
| url3 | url1, url2 | không có |
| url4 | url2 | không có |

Chỉ khóa url2 có cả hai phía. Ghép hai phía được (url1,url2,url3) và (url1,url2,url4). Đây là toàn bộ kết quả trên **bốn hàng được trích**, không phải toàn bộ kho liên kết của ví dụ nguồn.
:::

```text
map bộ (a,b) của R: phát(b, (R,a))
map bộ (b,c) của S: phát(b, (S,c))

reduce(b, V):
    A ← các a mang nhãn R
    C ← các c mang nhãn S
    với mỗi a trong A:
        với mỗi c trong C:
            phát(b, (a,b,c))
```

::: proof
Mỗi bộ phát từ reduce chứa một phần tử của $R$ và một phần tử của $S$ có cùng $b$, nên thỏa đặc tả nối. Ngược lại, mọi cặp bộ nối được đều có cùng khóa $b$, được gửi tới cùng reducer và được duyệt trong tích hai danh sách. Do đó không bỏ sót kết quả. Một phía rỗng cho tích rỗng. Với đầu vào hữu hạn, các vòng lặp dừng.
:::

Nếu một nhóm có $x$ bộ trái và $y$ bộ phải thì có $xy$ kết quả. Giả mã giữ hai danh sách cần bộ nhớ $O(x+y)$; việc phát kết quả cần ít nhất $\Omega(xy)$ thao tác. Biến thể giữ một phía và đọc phía kia tuần tự có thể giảm trạng thái, nhưng không loại được chi phí tạo kết quả. Nguồn: mục 2.3.7, trang 37; Ví dụ 2.4, trang 35.

### Nhóm và tổng hợp

Với Friends(User,Friend), nhóm theo User để đếm số hàng của mỗi người. Map phát (User,1); reduce cộng. Ví dụ 2.5 cho kết quả (Sally,300). Sách không cung cấp danh sách 300 tên, nên không thể dựng một vết 300 dòng như dữ kiện gốc.

Áp dụng cùng cơ chế COUNT lên bốn hàng Links: dùng From làm khóa, mỗi cạnh đóng góp một số 1.

| Khóa | Giá trị nhận | Trạng thái tổng | Kết quả |
|---|---|---|---|
| url1 | [1,1] | 0 → 1 → 2 | (url1,2) |
| url2 | [1,1] | 0 → 1 → 2 | (url2,2) |

Đây là áp dụng mục 2.3.8 lên dữ kiện Hình 2.5, không phải ví dụ số nguyên văn của sách. Với $N$ hàng hữu hạn, thuật toán dừng sau khi xử lý các nhóm; khi chưa gộp cục bộ có $N$ cặp trung gian và $N$ lần cộng theo mô hình thao tác đơn vị. Nhóm không có hàng không xuất hiện trong đầu ra.

Cơ chế tổng quát là chọn thuộc tính nhóm làm khóa, giữ thuộc tính cần tổng hợp trong giá trị. COUNT đếm hàng, SUM cộng giá trị, AVG giữ tổng và số lượng rồi chia ở cuối. Tính đúng dựa vào phân hoạch đầy đủ theo khóa và bất biến của phép tổng hợp. Nguồn: mục 2.3.8, trang 38; Ví dụ 2.5, trang 35.

### Liên hệ nhân ma trận–ma trận

Với kích thước tương thích, $p_{ik}=\sum_jm_{ij}n_{jk}$. Có thể dùng công việc thứ nhất nối phần tử theo $j$ để tạo các tích mang khóa $(i,k)$; công việc thứ hai cộng theo khóa ô kết quả. Biến thể một công việc phải gửi phần tử tới các ô cần nó. Ít công việc hơn có thể tăng sao chép dữ liệu.

Mục 2.3.6 về các phép tập hợp và giả mã chi tiết của hai biến thể nhân ma trận ở 2.3.9–2.3.10 được dành cho đọc thêm. Phần bắt buộc tập trung vào cơ chế chọn khóa, chạy tay và chứng minh của các thuật toán đã trình bày.

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

### Nối hai bảng

Ví dụ 2.14 xét $R(A,B)\bowtie S(B,C)$, $r=|R|$, $s=|S|$. Mỗi bộ gửi một cặp theo khóa $B$.

| Tầng | Đầu vào chuẩn hóa |
|---|---:|
| Map | $r+s$ |
| Reduce | $r+s$ |
| Tổng | $2(r+s)$ |

Sách kết luận $O(r+s)$ khi bỏ các hệ số kích thước cố định. Với hai bản sao của bốn hàng Links, $r=s=4$, tổng là $8+8=16$ đơn vị. Kết quả nối trên phần trích có hai bộ.

Chi phí này không phải cận thời gian chạy $O(r+s)$ cho mọi phép nối: một nhóm có thể tạo tích số lượng hai phía. Chính sự khác biệt giữa chi phí truyền thông và chi phí tạo kết quả làm việc nêu mô hình trở nên cần thiết.

### Nối ba bảng trên lưới reducer

Xét $R(A,B)\bowtie S(B,C)\bowtie T(C,D)$, kích thước lần lượt $r,s,t$. Băm $B$ vào $b$ nhóm, $C$ vào $c$ nhóm, dùng $k=bc$ reducer mang chỉ số $(i,j)$.

- Bộ $R$ biết nhóm $B$ nhưng chưa biết $C$, nên gửi tới $c$ ô của một hàng.
- Bộ $S$ biết cả $B,C$, nên gửi tới một ô.
- Bộ $T$ biết nhóm $C$ nhưng chưa biết $B$, nên gửi tới $b$ ô của một cột.

![Lưới 4×4: R gửi hàng 2, S gửi ô (2,1), T gửi cột 1.](img/lec-02/ch2-luoi-reducer.svg)

Hình theo Ví dụ 2.15, dùng nhóm 0 đến 3 nhất quán. Trong mỗi ô, phải kiểm tra giá trị $B,C$ thật; trùng nhóm băm chưa có nghĩa nối được.

```text
map R(a,B): với y = 0..c-1, phát((hB(B),y), (R,a,B))
map S(B,C): phát((hB(B),hC(C)), (S,B,C))
map T(C,d): với z = 0..b-1, phát((z,hC(C)), (T,C,d))
reduce(i,j): nối các bộ nhận được theo giá trị B và C thật
```

Mọi bộ ba hợp lệ gặp nhau ở đúng ô $(h_B(B),h_C(C))$. Ngược lại, kiểm tra điều kiện nối trong ô chỉ phát bộ ba hợp lệ. Như vậy thuật toán đầy đủ và không phát lặp cùng bộ ba ở nhiều ô. Các vòng lặp và tập dữ liệu hữu hạn nên dừng.

| Quan hệ | Map đọc | Reduce nhận |
|---|---:|---:|
| $R$ | $r$ | $cr$ |
| $S$ | $s$ | $s$ |
| $T$ | $t$ | $bt$ |

Do đó

$$
C_3=(r+s+t)+(cr+s+bt)=r+2s+t+cr+bt.
$$

Với $b=c=4$, tổng là $5r+2s+5t$. Hai lần $s$ đến từ hai tầng đọc, không phải gửi $S$ hai lần ở Map.

### So sánh với nối tuần tự

Ví dụ 2.16 đặt $r=s=t=3\cdot10^{11}$ và ước lượng quan hệ trung gian lớn gấp 30 một quan hệ đầu vào. Đây là giả thiết về mạng bạn bè trong ví dụ lịch sử của sách, không là quy luật mọi dữ liệu.

Hai công việc nối tuần tự có chi phí:

$$
C_{\mathrm{tuần\ tự}}=2(r+r)+2(30r+r)=66r=1{,}98\cdot10^{13}.
$$

Với lưới vuông $b=c=\sqrt{k}$, cách nối ba bảng có

$$
C_3=4r+2r\sqrt{k}.
$$

Vì $r>0$, $C_3<66r$ tương đương $\sqrt{k}<31$, tức $k<961$. Tại $k=961$, hai cách bằng nhau. Bài hiệu chỉnh dấu biên trong diễn giải “preferable” của nguồn. Lưới vuông yêu cầu $k$ là số chính phương; tổng quát phải chọn $b,c$ nguyên dương thỏa $bc=k$ rồi tính lại $cr+bt$.

So sánh này chỉ có ý nghĩa khi các phương án đáp ứng giới hạn thực thi. Tổng đầu vào nhỏ hơn không bảo đảm tác vụ nặng nhất vừa RAM hoặc hoàn thành sớm hơn. Nguồn: mục 2.5, trang 53–60, Ví dụ 2.14–2.16.

## 2.6. Bộ nhớ và sao chép dữ liệu

Để diễn tả đánh đổi, đặt $q$ là số giá trị đầu vào tối đa một reducer nhận và $\rho$ là số cặp trung gian trung bình trên một đầu vào. Sách dùng $r$ cho đại lượng thứ hai; bài đổi thành $\rho$ để tránh nhầm với $r=|R|$.

$$
\rho=\frac{\text{số cặp trung gian phát}}{\text{số phần tử đầu vào}}.
$$

Nếu mỗi giá trị có $B$ byte và reducer giữ đồng thời toàn bộ đầu vào thì phần dữ liệu chiếm tối đa $qB$ byte, chưa tính cấu trúc phụ. $\rho$ không phải số bản sao của khối trong hệ tệp.

### So sánh mọi cặp ảnh

Mục 2.6.2 xét $N=10^6$ ảnh, mỗi ảnh $B=10^6$ byte. Cho hàm độ tương tự đối xứng $s(P_i,P_j)$ và ngưỡng $\tau$; đầu ra gồm các cặp ảnh khác nhau có $s(P_i,P_j)>\tau$. Trong mô hình của nguồn, cần tính độ tương tự cho mọi cặp để quyết định có phát cặp đó hay không. Sách dùng $t$ cho ngưỡng; bài dùng $\tau$ để tránh nhầm với kích thước quan hệ $T$. Ký hiệu $s$ ở đây là hàm độ tương tự, khác số bộ của quan hệ $S$ trong mục 2.5. $B$ là số byte mỗi ảnh; ở ví dụ đếm từ, $B$ là số byte mỗi cặp. Một reducer cho mỗi cặp nhận hai ảnh, nên $q=2$. Mỗi ảnh được gửi tới $N-1$ reducer:

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

## 2.7. Tổng kết và bài tập

Chọn khóa quyết định dữ liệu nào gặp nhau. Lập luận đúng cần chỉ ra mọi đóng góp cần thiết đều gặp nhau và không bị mất hoặc lặp. Lập bảng đầu vào từng tầng cho biết hệ số sao chép xuất hiện ở đâu; sau đó vẫn phải kiểm tra tải lớn nhất, bộ nhớ và chi phí tạo kết quả.

Các bài dưới đây dịch và tách ý từ đúng bài tập nguồn. Không thay dữ kiện hay yêu cầu toán học. Bài 2.5.1 chỉ chọn ý (a), (c), phù hợp các thuật toán được giảng sâu.

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

### Bài tập 2.5.1(a,c) — Tính chi phí

::: exercise
Biểu diễn chi phí truyền thông theo kích thước quan hệ, ma trận hoặc vector:

(a) Thuật toán nhân ma trận–vector ở mục 2.3.2.

(c) Thuật toán tổng hợp ở mục 2.3.8.

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

(c) Đặt $N=|R|$. Map đọc $N$ bộ và phát một cặp cho mỗi bộ; Reduce nhận $N$ cặp. Không dùng bộ kết hợp, tổng chuẩn hóa là $2N=O(N)$. Nếu bộ đầu vào dài $B_R$ byte và cặp dài $B_P$ byte thì $C=N(B_R+B_P)$. Số nhóm không thay thế được số cặp đầu vào Reduce khi chưa gộp.
:::

## 2.8. Tài liệu tham khảo và hướng đọc

Leskovec, Rajaraman, Ullman. *Mining of Massive Datasets*, Chương 2: *MapReduce and the New Software Stack*, bản `ch2n.pdf`, trang in 20–79. [Trang sách và slide của tác giả](http://www.mmds.org).

Mục 2.8, trang 77–79, liệt kê các tài liệu gốc về hệ tệp, MapReduce và hệ xử lý mở rộng. Ôn mục 2.2–2.3 để viết thuật toán, sau đó dùng 2.5 để đánh giá. Đọc 2.6.3–2.6.7 khi đã nắm $q$, $\rho$ và muốn học các chứng minh cận dưới. Các con số ví dụ hệ thống trong chương giữ vai trò minh họa lịch sử, không được dùng như thông số công nghệ hiện tại.
