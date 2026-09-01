# Storyboard Bài 14

## Hành trình khái niệm

Kho tài liệu web (`I00`) → danh sách đảo và phép trộn (`I01–I06→I08`) → bố trí trên đĩa (`I07`) → vị trí/tần suất và đánh giá (`I09–I12`) → ảnh vệ tinh và truy vấn không gian (`S00–S02`) → R-tree lọc rồi tinh lọc (`R00→R02→R01→R03`) → 1-NN chính xác trên kd-tree (`K00→K01→K02→K03→K06→K04→K05→K07→K08→K09`) → ball tree (`B00→B02→B01→B03→B04→B05→B06→B07`) → Z-order và tổng hợp (`Z00–C02`) → recitation (`X00–X08`).

## Bảy mạch trình bày

| Mạch | Trang | Chức năng | Kết nối vào | Kết nối ra | Đóng góp mục tiêu |
|---|---|---|---|---|---|
| Mở bài | P00–P02 | Đặt hai miền dữ liệu và tuyến ứng viên–tinh lọc | Bài 13 | Kho web | Chốt đầu ra toàn bài |
| Chỉ mục đảo | I00–I12 | Danh sách đảo, Boolean, đĩa và đánh giá | Thuật ngữ không có khóa số tự nhiên | Ứng viên hình học | AND/OR/NOT và chi phí |
| Không gian và R-tree | S00–R03 | Truy vấn không gian; lọc MBR rồi tinh lọc | Mô hình ứng viên | Cận khoảng cách | R-tree không bỏ nghiệm |
| kd-tree | K00–K09 | Hộp miền, cận dưới và 1-NN chính xác | R-tree và cận khoảng cách | Ball metric | Cận dưới, đồng hạng, chi phí |
| Ball tree | B00–B07 | Truy vấn metric; dựng Euclid có vết | Cùng đặc tả 1-NN của kd-tree | Trở lại truy vấn vùng | Cận ball, tính đúng và dựng |
| Z-order và tổng hợp | Z00–C02 | Morton, đoạn chính xác/gộp, tinh lọc và chọn cấu trúc | B+-Tree Bài 13 | Recitation | Ánh xạ và mô hình chi phí |
| Recitation | X00–X08 | Ba bài nguồn có dữ kiện, sản phẩm và lời giải notes | Phần giảng | Hướng dẫn chấm | Thiết kế và chứng minh |

## Chu trình trọng tâm

### Chỉ mục đảo

- Tình huống/vấn đề: `I00`, kho tài liệu web trên bộ nhớ phụ; đầu ra là docID.
- Trực giác: `I01`; ví dụ: `I02`, `I04`, `I06`.
- Hình thức: `I03`; thuật toán/tính đúng: `I05`, `I08`; sau khi hoàn tất phép trộn mới sang bố trí đĩa `I07`.
- Ứng dụng/chi phí: `I07–I09`; kiểm tra: `I12` qua precision/recall.
- Dữ liệu NOT: $S=[1,2,3,4,6,8]$, $P_t=[2,3,6,8]$, kết quả $[1,4]$. Dữ liệu đánh giá: $G=\{1,3,8\}$, $R_h=\{3,8\}$, $R_l=\{1,2,3,6,8\}$.
- Tuyến lưu trữ: sinh cặp (thuật ngữ, docID) → sắp xếp ngoài → gom danh sách → B+-Tree định vị → đọc tuần tự.

### R-tree

- Vấn đề/trực giác: `S00–S02`, `R00`.
- Ví dụ trước thuật toán: `R02`, cửa sổ Q giao hai MBR.
- Thuật toán/tính đúng: `R01`, gom ứng viên rồi tinh lọc hình thật; chứng minh qua MBR tổ tiên.
- Chi phí/giới hạn: `R03`; tách CPU, trang và ứng viên; chỉ nêu cập nhật có thể làm MBR nở, tăng chồng lấn và gây tách.

### kd-tree

- Tình huống: `K00`, 1-NN trên tập huấn luyện lớn.
- Trực giác: `K01–K03`; nút trong chỉ lưu phép chia/hộp, mọi điểm ở lá; ví dụ số: `K06`.
- Hình thức: `K04`; giả mã `K05` xử lý hết điểm lá, nêu điều kiện trước/sau và dừng; chứng minh: `K07`; chi phí: `K08`; kiểm tra hòa: `K09`.
- Dữ liệu xuyên cụm: $q=(3,2)$, $p=(2,2)$, $s=(4,2)$, $\tau=1$, LB lần lượt 1 và 2.
- Điều kiện cắt: chỉ cắt khi $\operatorname{LB}>\tau$ để giữ mọi đồng hạng.

### ball tree

- Tình huống/trực giác: `B00`.
- Ví dụ số trước công thức: `B02`; hình thức/chứng minh cận: `B01`.
- Giả mã truy vấn `B03` chỉ cần metric, ball chứa điểm và cùng trạng thái $best,\tau,LB$.
- Dựng `B04–B06` chuyên biệt cho $S\subseteq\mathbb R^p$ hữu hạn, khoảng cách Euclid và $\ell\ge1$. Vết dùng bốn điểm $a,b,c,d$, khóa chiếu $(0,4,12,16)$, hai tập con và $(c,r)$ cho cả nút cha lẫn hai lá.
- Chi phí `B07` là suy ra của deck dưới giả thiết cây cân bằng, sắp lại mỗi nút và các phép đo/chiếu/tâm/bán kính tốn $O(p)$ mỗi điểm; không gán cho Cornell.
- Vết: với $\tau=2{,}5$, LB 2 được thăm, LB 3 bị cắt, LB 2,5 vẫn được thăm.

### Z-order

- Vấn đề: `Z00`; trực giác/ví dụ: `Z01`; hình thức: `Z02`.
- Ứng dụng và tinh lọc: `Z03–Z04`; so sánh bốn đoạn đơn với đoạn gộp $[4,13]$ và loại dương tính giả ở `Z04`.
- Dữ liệu xuyên cụm: lưới Morton 4×4 và vùng giữa có $\{4,7,10,13\}$.
- Sai khác: Auburn PDF trang 13 hoán vị 6/7; deck giữ công thức Morton và sửa hình.

## Bản đồ trang, thời lượng và nguồn

| Trang | Phút | Bước tiến | Nguồn |
|---|---:|---|---|
| P00–P02 | 5 | Mục tiêu và mạch ứng viên–tinh lọc | source.md B14 |
| I00 | 3 | Kho web lớn, đầu vào/đầu ra | Ch31 tr.1–3 |
| I01–I03 | 8 | Danh sách đảo, docID, đặc tả | Ch31 tr.13–14 |
| I04–I06 | 9 | Vết AND, giả mã và vết NOT cụ thể | Ch31 tr.14; sửa OR slide 14 |
| I08→I07 | 5 | Hoàn tất OR/NOT rồi bố trí đĩa theo pipeline B12–B14 | Ch31 tr.14 |
| I09–I12 | 9 | Vị trí/tần suất, precision, recall, đánh đổi | Ch31 tr.13–16 |
| S00–S02 | 9 | Ảnh vệ tinh, loại truy vấn, lọc–tinh lọc | Auburn tr.2–3, 10–12; ch24.17 |
| R00 | 2 | Cấu trúc MBR | ch24.21–22 |
| R02 | 3 | Ví dụ hộp chồng lấn | ch24.22–24 |
| R01 | 2 | Gom ứng viên, tinh lọc và chứng minh | ch24.23; Auburn tr.10–11 |
| R03 | 2 | CPU/nút-trang/ứng viên, trường hợp xấu | ch24.24 |
| K00–K03 | 12 | Vấn đề và trực giác tìm gần trước | Cornell tr.1–4 |
| K06 | 2 | Vết số dựng từ cơ chế nguồn | Cornell tr.2–3 |
| K04–K05 | 6 | Cận dưới và giả mã đầy đủ | Cornell tr.2–4 |
| K07–K09 | 7 | Quy nạp, $O(n)$ xấu, hòa | Cornell tr.2–4 |
| B00 | 3 | k-NN lớn và ball | Cornell tr.4–5 |
| B02 | 3 | Vết số LB và $\tau$ | dựng từ Cornell tr.3–5 |
| B01 | 3 | Công thức và bất đẳng thức tam giác | Cornell tr.3–5 |
| B03 | 2 | Giả mã truy vấn đầy đủ | Cornell tr.4–5 |
| B04–B05 | 5 | Vết số và giả mã dựng Euclid tạo $(c,r)$ ở mọi nút | Cornell tr.5; ví dụ do deck dựng |
| B06–B07 | 4 | Dùng lại trạng thái vết; chi phí dựng là suy ra có điều kiện | Cornell tr.4–5 |
| Z00–Z04 | 11 | Đoạn chính xác/gộp, B+-Tree và tinh lọc; Z04 dùng slide 26 | Auburn tr.12–13, slide 23–26; Bài 13 |
| C00–C02 | 5 | Mô hình RAM/trang, precision/recall và kiểm tra tổng hợp | tổng hợp nguồn |
| X00 | 0 | Giao ba bài | nguồn bài tập |
| X01–X03 | 30 | 31.2: đặc tả, thiết kế đống, giả mã+bất biến | Ch31 7e, Bài 31.2, tr.25 |
| X04–X05 | 10 | 25.2: so sánh hai đường truy cập | Ch25 6e, Bài/lời giải 25.2, PDF tr.1 |
| X06–X08 | 20 | 25.3: vùng đóng, dừng, đúng, đồng hạng | Ch25 6e, Bài/lời giải 25.3, PDF tr.2 |

Tổng phần giảng 120 phút; tổng recitation 60 phút.

## Kiểm kê 58 trang

Mỗi dòng dưới đây khớp một `data-slide-id` và một khối ghi chú trong HTML. Vai trò chi tiết và nguồn nằm ở bảng bản đồ phía trên.

| ID | Phút | Vai trò |
|---|---:|---|
| P00 | 1 | Tên bài và cầu từ Bài 13 |
| P01 | 2 | Chuẩn đầu ra quan sát được |
| P02 | 2 | Mạch ứng viên–tinh lọc |
| I00 | 3 | Tình huống kho web lớn |
| I01 | 3 | Trực giác chỉ mục đảo |
| I02 | 3 | Ví dụ danh sách tăng |
| I03 | 2 | Đặc tả $P_t$ |
| I04 | 3 | Vết AND |
| I05 | 3 | Giả mã và bất biến AND |
| I06 | 3 | Vết NOT với $S$, $P_t$ và đáp án fragment |
| I08 | 2 | Quy tắc trộn OR/NOT và điều kiện dừng |
| I07 | 3 | Bố trí danh sách trên đĩa sau khi hoàn tất thuật toán |
| I09 | 2 | $G$, hai ngưỡng và hai tập kết quả |
| I10 | 3 | Độ chính xác (precision) |
| I11 | 2 | Độ bao phủ (recall) |
| I12 | 2 | Đánh đổi và kiểm tra |
| S00 | 3 | Tình huống ảnh vệ tinh/trạm xăng |
| S01 | 3 | Phân loại truy vấn |
| S02 | 3 | Trực giác lọc–tinh lọc |
| R00 | 2 | Cấu trúc R-tree |
| R02 | 3 | Ví dụ MBR chồng lấn |
| R01 | 2 | Thuật toán gom và tinh lọc |
| R03 | 2 | Chi phí và giới hạn |
| K00 | 3 | Tình huống 1-NN lớn |
| K01 | 3 | Nút trong lưu phép chia/hộp; mọi điểm ở lá |
| K02 | 3 | Miền hộp thẳng trục của cây con |
| K03 | 3 | Nhánh gần trước; xử lý hết điểm lá |
| K06 | 2 | Vết số $p,s,\tau,LB$ |
| K04 | 3 | Hình thức hóa cận dưới |
| K05 | 3 | Giả mã, điều kiện trước/sau, dừng và cắt nghiêm ngặt |
| K07 | 2 | Chứng minh không bỏ nghiệm |
| K08 | 3 | $O(n)$ phép đo, $O(pn)$ phép toán số học |
| K09 | 2 | Kiểm tra đồng hạng |
| B00 | 3 | Tình huống ball tree |
| B02 | 3 | Vết số LB |
| B01 | 3 | Công thức và chứng minh LB |
| B03 | 2 | Giả mã truy vấn |
| B04 | 3 | Vết số $x_0,x_1,x_2,z,S_L,S_R,c,r$ |
| B05 | 2 | Giả mã dựng Euclid tạo ball cho cả lá |
| B06 | 2 | Vết $(c,r)$ của cha và hai lá; điều kiện metric |
| B07 | 2 | Cận dựng do deck suy ra có điều kiện |
| Z00 | 2 | Vấn đề tuyến tính hóa |
| Z01 | 3 | Ví dụ lưới Morton |
| Z02 | 2 | Công thức xen bit |
| Z03 | 2 | Đoạn chính xác và đoạn gộp có dương tính giả |
| Z04 | 2 | B+-Tree quét đoạn và tinh lọc; Auburn tr.13, slide 26 |
| C00 | 2 | Bảng chọn cấu trúc theo mô hình chi phí |
| C01 | 2 | Quy trình chọn chỉ mục, chất lượng và cập nhật |
| C02 | 1 | Kiểm tra tổng hợp |
| X00 | 0 | Giao ba bài nguồn |
| X01 | 10 | Đặc tả Bài 31.2 |
| X02 | 10 | Thiết kế đống và bất biến |
| X03 | 10 | Vòng lặp đống đầy đủ, hậu điều kiện, thời gian và bộ nhớ phụ/đầu ra |
| X04 | 5 | So sánh đường truy cập Bài 25.2 |
| X05 | 5 | Lời giải Bài 25.2 |
| X06 | 7 | Thiết kế vùng đóng Bài 25.3 |
| X07 | 7 | Dừng và đồng hạng |
| X08 | 6 | Chứng minh và chi phí $j+1$ truy vấn, $O(p|A|)$ tinh lọc |

## Câu nối và sai khác

- `I12→S00`: từ đánh giá tập tài liệu sang tinh lọc ứng viên hình học.
- `S02→R00`: hộp bao cần một cấu trúc phân cấp.
- `R03→K00`: truy vấn phạm vi chuyển sang cận khoảng cách cho điểm gần nhất.
- `K09→B00`: giữ đặc tả 1-NN và quy tắc đồng hạng; thay hộp thẳng trục bằng ball metric.
- `B07→Z00`: khép 1-NN, trở lại truy vấn vùng và dùng B+-Tree Bài 13 trên mã Z-order.
- `Z04→C00`: so sánh theo điều kiện không bỏ nghiệm và đơn vị chi phí.

Vết kd-tree và ball tree là ví dụ dựng từ cơ chế Cornell, không phải dữ liệu số trích nguyên từ nguồn. Truy vấn ball chỉ đúng khi ball chứa cây con theo cùng metric; phép dựng và cận chi phí của deck dùng Euclid. Bài 25.3 được bổ sung điều kiện tập hữu hạn, không rỗng, $r_i\to\infty$ và vùng đóng để hoàn thiện chứng minh. Wrapper là `P`; `I`; `S+R`; `K`; `B`; `Z+C`; `X`, giữ 58 ID; chỉ đổi cục bộ thứ tự `I06→I08→I07`.

## Storyboard ghi chú tự học

| `note-topic-id` | Vai trò và kết nối vào–ra | Kiến thức đầu vào | Sản phẩm học tập | Thành phần trình bày |
|---|---|---|---|---|
| `L14-N01` | Khôi phục Bài 13; mở tuyến ứng viên–tinh lọc | khóa tuyến tính, I/O | phân biệt đáp án với ứng viên | vai trò, đặc tả, kiểm tra; không cần định lý |
| `L14-N02` | Văn bản → danh sách đã sắp | tập hợp, hai con trỏ | chạy AND/OR/NOT; nêu bất biến và chi phí | đủ vai trò, đặc tả, ví dụ, thuật toán, đúng, chi phí |
| `L14-N03` | Danh sách → lưu trữ → đánh giá | Bài 12–13 | phân biệt mục RAM và trang I/O | cầu nối rút gọn; không có định lý riêng |
| `L14-N04` | Kết quả Boolean → chất lượng truy hồi | tập hợp | tính precision/recall trên $G,R_h,R_l$ | định nghĩa, ví dụ, biên, kiểm tra |
| `L14-N05` | Văn bản → truy vấn vùng | hình học cơ bản | giải thích R-tree lọc rồi tinh lọc | đủ chu trình; chứng minh không bỏ nghiệm |
| `L14-N06` | Vùng → cận khoảng cách | metric, đệ quy | chạy và chứng minh 1-NN kd-tree | đủ chu trình; vết do bài giảng dựng |
| `L14-N07` | Hộp → ball metric | N06, bất đẳng thức tam giác | tính $LB$ và chạy truy vấn ball | đủ chu trình; tách khỏi phép dựng |
| `L14-N08` | Truy vấn ball → dựng Euclid | vector, chuẩn 2 | dựng cây, chứng minh tiến triển, phân tích cận | đủ chu trình; cận có điều kiện |
| `L14-N09` | 1-NN → trở lại truy vấn vùng | B+-Tree Bài 13 | mã hóa Morton và tinh lọc đoạn gộp | định nghĩa, vết, thuật toán quét, kiểm tra |
| `L14-N10` | Thu hồi hai tình huống mở bài | N01–N09 | chọn cấu trúc và đúng đơn vị chi phí | bảng tổng hợp và kiểm tra; không có chứng minh mới |
| `L14-N11` | Phần giảng → bài nguồn 31.2 | danh sách đảo, đống | giả mã, bất biến, dừng, chi phí | exercise/hint/solution đầy đủ |
| `L14-N12` | Phần giảng → bài nguồn 25.2–25.3 | R-tree, B+-Tree, vùng | chọn đường truy cập; chứng minh 1-NN qua vùng | exercise/hint/solution; ghi rõ điều kiện bổ sung |

Ghi chú dùng thứ tự định nghĩa trước ví dụ theo khuôn tài liệu tự học; deck vẫn giữ trực giác trước hình thức hóa. Không đổi ký hiệu, kết luận hoặc thứ tự khái niệm dùng chung, nên không cần sửa deck.
