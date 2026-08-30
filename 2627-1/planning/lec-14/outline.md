# Dàn ý Bài 14: Chỉ mục văn bản và chỉ mục không gian

## Mục tiêu và phạm vi

Sau 120 phút giảng, sinh viên có thể:

- đặc tả và trộn danh sách đảo cho AND, OR và NOT;
- phân biệt độ chính xác và độ bao phủ trong tìm kiếm toàn văn;
- chạy tìm kiếm 1-NN chính xác trên kd-tree và ball tree, kể cả nghiệm đồng hạng;
- chứng minh điều kiện cắt nhánh bằng cận dưới;
- giải thích lọc–tinh lọc của R-tree và Z-order;
- chọn chỉ mục theo đầu ra, giả thiết và đơn vị chi phí.

Phần giảng không giải trước Bài 31.2. Sinh viên thiết kế đống tối thiểu lần đầu trong recitation.

## Nguồn và quyết định

| Cụm | Nguồn | Quyết định |
|---|---|---|
| Chỉ mục đảo | *Database System Concepts* 7e, Chương 31, trang in 13–16; slide 14–16 | Giữ danh sách đảo, phép Boolean, vị trí/tần suất, precision/recall; sửa OR ở slide 14 từ giao thành hợp |
| R-tree | Chương 24, slide 17, 21–24; Auburn PDF trang 10–13 | Giữ hộp bao và nhiều nhánh; tách gom ứng viên khỏi tinh lọc hình thật |
| kd-tree, ball tree | Cornell CS5780, PDF trang 1–5 | Giữ cơ chế và thêm vết số; tách truy vấn ball theo metric khỏi phép dựng Euclid do deck đặc tả |
| Z-order | Auburn COMP7120, PDF trang 12–13, slide nguồn 23–26 | Giữ công thức Morton; sửa hoán vị 6/7 trên hình nguồn để công thức và đủ 16 ô nhất quán |
| Recitation | Ch31 7e Bài 31.2, trang in 25; Ch25 6e Bài 25.2–25.3, PDF trang 1–2 | 31.2 không có lời giải chính thức 7e; 25.2–25.3 dùng lời giải chính thức 6e; chỉ bổ sung điều kiện cần cho đặc tả/chứng minh |

MMDS và Stanford CS246 không áp dụng: các nguồn đó không bao phủ các cấu trúc chỉ mục của bài. Cornell PDF trang 7–12 là Decision Trees nên bỏ. Auburn chỉ có row-order/Z-order; không suy rộng sang Hilbert.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $D$ | tập tài liệu; $S\subseteq D$ là tập nền của NOT |
| $P_t$ | danh sách đảo tăng nghiêm ngặt của thuật ngữ $t$ |
| $n$ | số điểm trong các cụm cây; trong Bài 31.2 là số danh sách, theo phạm vi cục bộ |
| $T=\sum_i|P_i|$ | tổng số mục danh sách trong Bài 31.2 |
| $q$ | điểm hỏi |
| $U$ | nút hoặc miền cây con; không dùng $N$ để tránh lẫn số điểm |
| $p$ | số chiều của vector |
| $\ell$ | sức chứa lá của ball tree, $\ell\ge1$ |
| $\delta$ | metric cho truy vấn ball; phép dựng trong deck dùng chuẩn Euclid trên $\mathbb R^p$ |
| $best,\tau$ | tập nghiệm tốt nhất hiện có và khoảng cách của chúng |
| $\operatorname{LB}(q,U)$ | cận dưới từ $q$ tới mọi điểm trong $U$ |
| $B(c,r)$ | ball tâm $c$, bán kính $r$ |
| $u=x-1,v=y-1,z$ | tọa độ 0-based và mã Morton 1-based |

Quy tắc hòa: trả mọi điểm gần nhất; chỉ cắt khi $\operatorname{LB}>\tau$.

## Đặc tả và vết chính

### Danh sách đảo

- Mỗi danh sách tăng nghiêm ngặt, không lặp docID.
- AND và OR trộn bằng hai con trỏ trong $O(|P|+|Q|)$; OR xử lý đủ ba quan hệ giữa hai đầu và chép phần đuôi còn lại.
- NOT là $S\setminus P_t$ với $S=[1,2,3,4,6,8]$, $P_t=[2,3,6,8]$ và kết quả $[1,4]$; khi đầu $S$ nhỏ hơn thì xuất, bằng thì bỏ, lớn hơn thì tiến $P_t$.
- Vị trí và tần suất là dữ liệu kèm docID, không phải docID lặp.
- Tuyến lưu trữ dùng lại Bài 12–13: sinh cặp (thuật ngữ, docID), sắp xếp ngoài, gom danh sách, rồi dùng B+-Tree định vị đầu danh sách liên tiếp.
- Ví dụ đánh giá dùng $G=\{1,3,8\}$, $R_h=\{3,8\}$ và $R_l=\{1,2,3,6,8\}$: $(precision,recall)$ lần lượt là $(1,2/3)$ và $(3/5,1)$.

### R-tree

- `gom(U,Q,A)` chỉ tạo ứng viên có MBR giao $Q$.
- `tinh_lọc(A,Q)` kiểm hình thật.
- Nếu vật thể giao $Q$, mọi MBR tổ tiên của nó giao $Q$; bước gom không bỏ nghiệm.
- Chi phí được tách thành CPU kiểm giao, số nút/trang đã đọc và số ứng viên. Không bịa cận I/O.
- Cập nhật có thể mở rộng MBR, tăng chồng lấn và gây tách nút; bài không dạy thuật toán chèn hoặc tách.

### kd-tree

Ví dụ: $q=(3,2)$. Thăm $p=(2,2)$ trước, được $\tau=1$. Miền $x\ge4$ có LB=1 nên phải thăm và thêm $s=(4,2)$ đồng hạng. Miền $x\ge5$ có LB=2 nên cắt. Kết quả $best=\{p,s\}$, $\tau=1$.

Nút trong chỉ lưu chiều chia, ngưỡng và hộp miền; mọi điểm dữ liệu ở lá. Giả mã khởi tạo $(\varnothing,\infty)$, xử lý hết mọi điểm trong lá, gán lại trạng thái sau cả hai lời gọi và giữ điểm khi $d=\tau$. Điều kiện trước là cây hữu hạn, lá hữu hạn và LB hợp lệ; điều kiện sau giữ mọi nghiệm tốt nhất hoặc đồng hạng; đệ quy đi xuống cây nên dừng. Chỉ cắt khi $\operatorname{LB}>\tau$. Trường hợp xấu đo tới mọi điểm: $O(n)$ phép đo, tương ứng $O(pn)$ phép toán số học cho điểm $p$ chiều.

### ball tree

Với $q=(0,0)$ và $\tau=2{,}5$:

- $(\delta(q,c),r)=(3,1)$ cho LB=2: thăm;
- $(5,2)$ cho LB=3: cắt;
- $(4,1{,}5)$ cho LB=2,5: thăm để giữ hòa.

$\operatorname{LB}(q,B)=\max(0,\delta(q,c)-r)$ và thuật toán truy vấn chỉ cần metric, với điều kiện mỗi ball chứa cây con theo cùng metric $\delta$. Phép dựng của deck chuyên biệt cho tập hữu hạn $S\subseteq\mathbb R^p$, $\ell\ge1$ và chuẩn 2. Vết dùng $a=(0,0),b=(1,0),c=(3,0),d=(4,0)$; $x_0=a,x_1=d,x_2=a$; khóa chiếu $(0,4,12,16)$; hai lá $\{a,b\}$ và $\{c,d\}$ có tâm $(0{,}5,0)$ và $(3{,}5,0)$, cùng bán kính $0{,}5$. Mọi nút, kể cả lá, đều tạo $(c,r)$. Với cây cân bằng, sắp lại mỗi nút và mỗi phép đo/chiếu xử lý $p$ tọa độ, deck suy ra $O(n\log^2n+pn\log n)$; không gán cận này cho Cornell.

### Bài 31.2

- Duyệt $n$ danh sách để khởi tạo, kể cả khi tất cả rỗng và $T=0$.
- Mỗi trong $T$ mục vào hoặc ra đống với hạng tối đa $n$.
- Mỗi phần tử đống là `(docID, mã danh sách)`; vòng trong lấy hết đầu bằng $x$, tiến đúng các danh sách và tái chèn đầu mới nếu còn.
- Thời gian $O(n+T\log(n+1))$; bộ nhớ phụ $O(n)$ khi không tính đầu ra, hoặc tổng bộ nhớ $O(n+|A|)$.

### Z-order

$$z=1+\sum_{j\ge0}(2u_j+v_j)4^j.$$

Ma trận đúng, từ hàng trên xuống: `6,8,14,16`; `5,7,13,15`; `2,4,10,12`; `1,3,9,11`. Auburn PDF trang 13 đổi chỗ 6/7; deck ghi rõ và sửa. Vùng $x\in\{2,3\},y\in\{2,3\}$ cho mã $\{4,7,10,13\}$. Có thể dùng bốn đoạn đơn chính xác hoặc đoạn gộp $[4,13]$ chứa dương tính giả; mọi phương án hợp lệ phải phủ mọi mã vùng và phương án gộp phải tinh lọc tọa độ. Z04 dẫn Auburn PDF trang 13, slide nguồn 26.

## Bảy mạch trình bày

| Mạch | Trang | Chức năng | Kết nối vào | Kết nối ra | Mục tiêu |
|---|---|---|---|---|---|
| Mở bài | P00–P02 | Chốt vấn đề, đầu ra và tuyến ứng viên–tinh lọc | Bài 13 về khóa tuyến tính | Kho tài liệu web | Toàn bộ mục tiêu |
| Chỉ mục đảo | I00–I12 | Từ thuật ngữ đến Boolean, bố trí đĩa và đánh giá | Mạch mở bài | Ứng viên hình học | Trộn AND/OR/NOT |
| Không gian và R-tree | S00–R03 | Phân loại truy vấn; lọc MBR rồi tinh lọc hình thật | Tập ứng viên văn bản | Cận khoảng cách | R-tree và lọc–tinh lọc |
| kd-tree | K00–K09 | Hộp miền, cận dưới và 1-NN chính xác | Truy vấn không gian | Ball metric | 1-NN, đồng hạng, tính đúng |
| Ball tree | B00–B07 | Truy vấn metric và phép dựng Euclid có vết | kd-tree | Truy vấn vùng qua khóa | Cận ball, dựng và chi phí |
| Z-order và tổng hợp | Z00–C02 | Đoạn Morton, tinh lọc, mô hình chi phí và chất lượng | B+-Tree Bài 13 | Bài tập nguồn | Ánh xạ, chọn cấu trúc |
| Recitation | X00–X08 | Thiết kế, chứng minh và phân tích ba bài nguồn | Toàn bộ phần giảng | Sản phẩm chấm | 31.2, 25.2, 25.3 |

## Thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài | P00–P02 | 5 |
| Chỉ mục đảo | I00–I12 | 34 |
| Không gian và R-tree | S00–R03 | 18 |
| kd-tree | K00–K09 | 27 |
| Ball tree | B00–B07 | 20 |
| Z-order và tổng hợp | Z00–C02 | 16 |
| **Phần giảng** | **49 trang** | **120** |
| Bài 31.2 | X01–X03 | 30 |
| Bài 25.2 | X04–X05 | 10 |
| Bài 25.3 | X06–X08 | 20 |
| **Recitation** | **9 trang kể cả X00** | **60** |
