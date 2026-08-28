# Storyboard Bài 14

## Hành trình khái niệm

Kho tài liệu web (`I00`) → danh sách đảo và phép trộn (`I01–I08`) → vị trí/tần suất và đánh giá kết quả (`I09–I12`) → ảnh vệ tinh và truy vấn không gian (`S00–S02`) → R-tree lọc rồi tinh lọc (`R00→R02→R01→R03`) → 1-NN chính xác trên kd-tree (`K00→K01→K02→K03→K06→K04→K05→K07→K08→K09`) → ball tree (`B00→B02→B01→B03→B04→B05→B06→B07`) → Z-order (`Z00–Z04`) → chọn cấu trúc (`C00–C02`) → recitation (`X00–X08`).

## Chu trình trọng tâm

### Chỉ mục đảo

- Tình huống/vấn đề: `I00`, kho tài liệu web trên bộ nhớ phụ; đầu ra là docID.
- Trực giác: `I01`; ví dụ: `I02`, `I04`, `I06`.
- Hình thức: `I03`; thuật toán/tính đúng: `I05`, `I08`; `I08` xử lý ba quan hệ $<$, $=$, $>$ và phần đuôi trên các danh sách tăng nghiêm ngặt.
- Ứng dụng/chi phí: `I07–I09`; kiểm tra: `I12` qua precision/recall.
- Dữ liệu `cây=[1,3,4,8]`, `tìm=[2,3,6,8]` truyền từ `I02` qua `I04–I06`.

### R-tree

- Vấn đề/trực giác: `S00–S02`, `R00`.
- Ví dụ trước thuật toán: `R02`, cửa sổ Q giao hai MBR.
- Thuật toán/tính đúng: `R01`, gom ứng viên rồi tinh lọc hình thật; chứng minh qua MBR tổ tiên.
- Chi phí/giới hạn: `R03`; không nêu cận I/O ngoài nguồn.

### kd-tree

- Tình huống: `K00`, 1-NN trên tập huấn luyện lớn.
- Trực giác: `K01–K03`; ví dụ số: `K06`.
- Hình thức: `K04`; giả mã: `K05`; chứng minh: `K07`; chi phí: `K08` với $O(n)$ phép đo và $O(pn)$ phép toán số học; kiểm tra hòa: `K09`.
- Dữ liệu xuyên cụm: $q=(3,2)$, $p=(2,2)$, $s=(4,2)$, $\tau=1$, LB lần lượt 1 và 2.

### ball tree

- Tình huống/trực giác: `B00`.
- Ví dụ số trước công thức: `B02`; hình thức/chứng minh cận: `B01`.
- Giả mã truy vấn dùng cùng $best,\tau,LB$: `B03`.
- Dựng: `B04–B05`, với $S$ hữu hạn, $\ell\ge1$, chọn $x_0$ tùy ý sau ca cơ sở; chứa/phân hoạch/tiến triển và tính đúng: `B06`; chi phí/kiểm tra: `B07`.
- Vết: với $\tau=2{,}5$, LB 2 được thăm, LB 3 bị cắt, LB 2,5 vẫn được thăm.

### Z-order

- Vấn đề: `Z00`; trực giác/ví dụ: `Z01`; hình thức: `Z02`.
- Ứng dụng và tinh lọc: `Z03–Z04`; kiểm tra ở `Z04`.
- Dữ liệu xuyên cụm: lưới Morton 4×4 và vùng giữa có $\{4,7,10,13\}$.
- Sai khác: Auburn PDF trang 13 hoán vị 6/7; deck giữ công thức Morton và sửa hình.

## Bản đồ trang, thời lượng và nguồn

| Trang | Phút | Bước tiến | Nguồn |
|---|---:|---|---|
| P00–P02 | 5 | Mục tiêu và mạch ứng viên–tinh lọc | source.md B14 |
| I00 | 3 | Kho web lớn, đầu vào/đầu ra | Ch31 tr.1–3 |
| I01–I03 | 8 | Danh sách đảo, docID, đặc tả | Ch31 tr.13–14 |
| I04–I06 | 9 | Vết AND, giả mã, OR/NOT | Ch31 tr.14; sửa OR slide 14 |
| I07–I08 | 5 | Bố trí đĩa, quy tắc trộn và phần đuôi | Ch31 tr.14 |
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
| B04–B05 | 5 | Cách dựng Cornell, phá hòa | Cornell tr.5 |
| B06–B07 | 4 | Đúng, tiến triển, chi phí dựng/truy vấn | Cornell tr.4–5 |
| Z00–Z04 | 11 | Từ điểm sang mã, đoạn khóa và tinh lọc | Auburn tr.12–13; Bài 13 |
| C00–C02 | 5 | So sánh chi phí và kiểm tra tổng hợp | tổng hợp nguồn |
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
| I06 | 3 | OR và tập nền của NOT |
| I07 | 3 | Bố trí danh sách trên đĩa |
| I08 | 2 | Quy tắc trộn OR/NOT |
| I09 | 2 | Vị trí và tần suất |
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
| K01 | 3 | Quy tắc chia và tiến triển |
| K02 | 3 | Miền hộp thẳng trục |
| K03 | 3 | Nhánh gần trước |
| K06 | 2 | Vết số $p,s,\tau,LB$ |
| K04 | 3 | Hình thức hóa cận dưới |
| K05 | 3 | Giả mã truy vấn |
| K07 | 2 | Chứng minh không bỏ nghiệm |
| K08 | 3 | $O(n)$ phép đo, $O(pn)$ phép toán số học |
| K09 | 2 | Kiểm tra đồng hạng |
| B00 | 3 | Tình huống ball tree |
| B02 | 3 | Vết số LB |
| B01 | 3 | Công thức và chứng minh LB |
| B03 | 2 | Giả mã truy vấn |
| B04 | 3 | Trực giác cách dựng Cornell |
| B05 | 2 | Giả mã dựng, $x_0$, $\ell$ và phá hòa |
| B06 | 2 | Chứa, phân hoạch và tiến triển khi $|S|>\ell$ |
| B07 | 2 | Chi phí dựng/truy vấn và kiểm tra |
| Z00 | 2 | Vấn đề tuyến tính hóa |
| Z01 | 3 | Ví dụ lưới Morton |
| Z02 | 2 | Công thức xen bit |
| Z03 | 2 | Vùng thành nhiều đoạn |
| Z04 | 2 | B+-Tree, tinh lọc và kiểm tra |
| C00 | 2 | Bảng chọn cấu trúc |
| C01 | 2 | Quy trình chọn chỉ mục |
| C02 | 1 | Kiểm tra tổng hợp |
| X00 | 0 | Giao ba bài nguồn |
| X01 | 10 | Đặc tả Bài 31.2 |
| X02 | 10 | Thiết kế đống và bất biến |
| X03 | 10 | Lời giải và $O(n+T\log(n+1))$ |
| X04 | 5 | So sánh đường truy cập Bài 25.2 |
| X05 | 5 | Lời giải Bài 25.2 |
| X06 | 7 | Thiết kế vùng đóng Bài 25.3 |
| X07 | 7 | Dừng và đồng hạng |
| X08 | 6 | Chứng minh đúng và hướng dẫn chấm |

## Câu nối và sai khác

- `I12→S00`: từ đánh giá tập tài liệu sang tinh lọc ứng viên hình học.
- `S02→R00`: hộp bao cần một cấu trúc phân cấp.
- `R03→K00`: truy vấn phạm vi chuyển sang cận khoảng cách cho điểm gần nhất.
- `K09→B00`: hộp thẳng trục chuyển sang ball metric.
- `B07→Z00`: thay cây metric bằng khóa tuyến tính để dùng lại B+-Tree.
- `Z04→C00`: so sánh theo điều kiện không bỏ nghiệm và đơn vị chi phí.

Vết kd-tree và ball tree là ví dụ dựng từ cơ chế Cornell, không phải dữ liệu số trích nguyên từ nguồn. Thay đổi này bổ sung khả năng chạy tay mà không thêm kết luận mới.
