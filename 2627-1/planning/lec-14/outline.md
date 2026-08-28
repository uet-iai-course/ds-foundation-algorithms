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
| kd-tree, ball tree | Cornell CS5780, PDF trang 1–5 | Giữ cơ chế; thêm vết số tự chứa dựng từ cơ chế vì nguồn không cho đủ tọa độ |
| Z-order | Auburn COMP7120, PDF trang 12–13 | Giữ công thức Morton; sửa hoán vị 6/7 trên hình nguồn để công thức và đủ 16 ô nhất quán |
| Recitation | Ch31 Bài 31.2, trang in 25; Ch25 ấn bản 6, Bài 25.2–25.3, PDF trang 1–2 | Giữ nguyên yêu cầu toán học; chỉ làm rõ miền, vùng tròn đóng và sản phẩm |

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
| $\delta$ | metric; cách dựng Cornell dùng khoảng cách Euclid |
| $best,\tau$ | tập nghiệm tốt nhất hiện có và khoảng cách của chúng |
| $\operatorname{LB}(q,U)$ | cận dưới từ $q$ tới mọi điểm trong $U$ |
| $B(c,r)$ | ball tâm $c$, bán kính $r$ |
| $u=x-1,v=y-1,z$ | tọa độ 0-based và mã Morton 1-based |

Quy tắc hòa: trả mọi điểm gần nhất; chỉ cắt khi $\operatorname{LB}>\tau$.

## Đặc tả và vết chính

### Danh sách đảo

- Mỗi danh sách tăng nghiêm ngặt, không lặp docID.
- AND và OR trộn bằng hai con trỏ trong $O(|P|+|Q|)$; OR xử lý đủ ba quan hệ giữa hai đầu và chép phần đuôi còn lại.
- NOT là $S\setminus P_t$ với $S$ tăng nghiêm ngặt; khi đầu $S$ nhỏ hơn thì xuất, bằng thì bỏ, lớn hơn thì tiến $P_t$; khi một bên cạn chỉ chép đuôi của $S$.
- Vị trí và tần suất là dữ liệu kèm docID, không phải docID lặp.

### R-tree

- `gom(U,Q,A)` chỉ tạo ứng viên có MBR giao $Q$.
- `tinh_lọc(A,Q)` kiểm hình thật.
- Nếu vật thể giao $Q$, mọi MBR tổ tiên của nó giao $Q$; bước gom không bỏ nghiệm.
- Chi phí được tách thành CPU kiểm giao, số nút/trang đã đọc và số ứng viên. Không bịa cận I/O.

### kd-tree

Ví dụ: $q=(3,2)$. Thăm $p=(2,2)$ trước, được $\tau=1$. Miền $x\ge4$ có LB=1 nên phải thăm và thêm $s=(4,2)$ đồng hạng. Miền $x\ge5$ có LB=2 nên cắt. Kết quả $best=\{p,s\}$, $\tau=1$.

Giả mã khởi tạo $(\varnothing,\infty)$, xử lý lá, gán lại trạng thái sau cả hai lời gọi và giữ điểm khi $d=\tau$. Trường hợp xấu đo tới mọi điểm: $O(n)$ phép đo, tương ứng $O(pn)$ phép toán số học cho điểm $p$ chiều.

### ball tree

Với $q=(0,0)$ và $\tau=2{,}5$:

- $(\delta(q,c),r)=(3,1)$ cho LB=2: thăm;
- $(5,2)$ cho LB=3: cắt;
- $(4,1{,}5)$ cho LB=2,5: thăm để giữ hòa.

$\operatorname{LB}(q,B)=\max(0,\delta(q,c)-r)$ cần metric. Phép dựng nhận $S$ hữu hạn và $\ell\ge1$; sau ca cơ sở, chọn $x_0\in S$ tùy ý rồi chọn hai điểm xa. Khi $|S|>\ell$, ta có $|S|\ge2$; chia theo hạng tạo hai nửa không rỗng và nhỏ hơn cha. Với cây cân bằng và sắp lại ở mỗi nút, tổng chi phí dựng là $O(n\log^2n+pn\log n)$; truy vấn xấu dùng $O(n)$ phép đo hay $O(pn)$ phép toán số học.

### Bài 31.2

- Duyệt $n$ danh sách để khởi tạo, kể cả khi tất cả rỗng và $T=0$.
- Mỗi trong $T$ mục vào hoặc ra đống với hạng tối đa $n$.
- Thời gian $O(n+T\log(n+1))$; bộ nhớ $O(n)$.

### Z-order

$$z=1+\sum_{j\ge0}(2u_j+v_j)4^j.$$

Ma trận đúng, từ hàng trên xuống: `6,8,14,16`; `5,7,13,15`; `2,4,10,12`; `1,3,9,11`. Auburn PDF trang 13 đổi chỗ 6/7; deck ghi rõ và sửa. Vùng $x\in\{2,3\},y\in\{2,3\}$ cho mã $\{4,7,10,13\}$.

## Thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài | P00–P02 | 5 |
| Chỉ mục đảo | I00–I12 | 34 |
| Không gian và R-tree | S00–S02, R00, R02, R01, R03 | 18 |
| kd-tree | K00–K03, K06, K04, K05, K07–K09 | 27 |
| ball tree | B00, B02, B01, B03–B07 | 20 |
| Z-order | Z00–Z04 | 11 |
| Tổng hợp | C00–C02 | 5 |
| **Phần giảng** | **49 trang** | **120** |
| Bài 31.2 | X01–X03 | 30 |
| Bài 25.2 | X04–X05 | 10 |
| Bài 25.3 | X06–X08 | 20 |
| **Recitation** | **9 trang kể cả X00** | **60** |
