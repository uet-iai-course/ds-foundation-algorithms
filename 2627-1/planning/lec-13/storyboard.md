# Storyboard Bài 13

## Hành trình khái niệm

Quan hệ lớn và chi phí duy trì (`A00–A03`) → B+-Tree cho điểm và khoảng (`B00–B08`) → cập nhật trực tuyến (`C00–C11`, `C06A`) → đối chiếu B-Tree (`D00–D01`) → băm tĩnh cho điều kiện bằng (`H00–H06`) → Bitmap Index cho nhiều bộ lọc (`M00–M07`, `M00A`) → tổng kết và bài nguồn (`T00–X08`, `X07D`).

Kiến thức đầu vào từ Bài 12 là một nút chỉ mục thường vừa một khối, nên chiều sâu cây chi phối số lần đọc. Vết $m=6$ của bài 14.3(b) truyền từ cấu trúc `B01` sang ví dụ `B03`, hình thức hóa `B02`, tìm kiếm `B04–B08`, cập nhật `C01–C11` và recitation `X02–X06`. Dữ liệu giảng viên truyền từ ví dụ ba hàng `M00A` sang đặc tả `M01`, vết 12 hàng `M02–M03` và bài tự chứa `X07D–X08`.

## Chu trình trọng tâm

### B+-Tree: tìm điểm và khoảng

- Tình huống/vấn đề: `B00`.
- Trực giác: `B01`.
- Ví dụ chạy tay: `B03`, `B05`.
- Hình thức hóa: `B02`.
- Thuật toán và tính đúng: `B04`, `B06`.
- Chi phí: `B07`.
- Kiểm tra: `B08`.
- Sản phẩm: đường tìm, quét chuỗi lá, cận chiều cao và số lần đọc nút.

### B+-Tree: chèn và xóa

- Tình huống: `C00`.
- Trực giác/ví dụ: `C01–C03`, `C07–C09`.
- Hình thức hóa: kế thừa cận sức chứa ở `B02`.
- Thuật toán và tính đúng: `C04–C06`, `C08–C10`.
- Chi phí: `C11`.
- Kiểm tra: câu hỏi ở `C11` và bài `X04–X06`.
- Kiểm tra giữa cụm: `C06A`; kiểm tra chi phí: `C11`; bài nguồn: `X04–X06`.
- Sản phẩm: cây sau Insert 8 và sau Delete 19, phân biệt sao chép/đẩy khóa phân cách.

### Băm tĩnh

- Tình huống: `H00`.
- Trực giác/ví dụ: `H02`.
- Đặc tả: `H01`.
- Thuật toán/tính đúng: `H03–H04`.
- Chi phí/giới hạn: `H05`.
- Kiểm tra: `H06`.
- Sản phẩm: chuỗi ngăn băm phải quét và lựa chọn cấu trúc theo loại truy vấn.

### Bitmap

- Tình huống: `M00`.
- Trực giác/ví dụ: `M00A`.
- Đặc tả: `M01`.
- Ví dụ đầy đủ: `M02–M03`.
- Thuật toán/hình thức: `M04–M05`.
- Tính đúng: `M06`.
- Chi phí: `M04`.
- Kiểm tra: `M07` và bài `X07–X08`.
- Sản phẩm: bitmap ứng viên, công thức NOT có $E$ và $V_{\mathrm{NULL}}$, bước lọc điều kiện dư.

## Bản đồ từng trang

| Trang | Bước học tập | Lý do tồn tại / sản phẩm | Nguồn |
|---|---|---|---|
| P00 | mở bài | Nối mô hình I/O của Bài 12 với chỉ mục | ch14.3–4 |
| P01 | mục tiêu | Chốt sản phẩm học tập | ch14.17–59, 71–75; ch24.11–15 |
| P02 | mạch/ký hiệu | Chốt bốn nhánh và $m,K,M$ | tổng hợp nguồn |
| A00 | tình huống | Nêu lợi ích truy vấn và giá cập nhật | ch14.3–4, 11 |
| A01 | đặc tả | Phân biệt khóa tìm kiếm và con trỏ kết quả | ch14.3, 16 |
| A02 | chi phí/kiểm tra | Bốn thước đo và đánh đổi bài 14.1 | ch14.4, 11; bài 14.1 |
| A03 | lựa chọn | Nối loại truy vấn với cấu trúc | ch14.4, 59, 71–73 |
| B00 | tình huống | Một triệu khóa, nút theo khối, cần điểm/khoảng | ch14.17, 24, 27 |
| B01 | trực giác/ví dụ | Cây $m=6$ có nút trong, lá và chuỗi lá | ch14.20–23; lời giải 14.3(b) tr.100 |
| B03 | ví dụ chạy tay | Tìm 23 qua khóa phân cách 19 | ch14.22, 25; bài 14.3(b) |
| B02 | hình thức | Bất biến độ sâu và sức chứa, gốc ngoại lệ | ch14.19, 23 |
| B04 | thuật toán | Tìm điểm; phân biệt khóa duy nhất, khóa ghép và mục trỏ danh sách RID | ch14.25, 28, 40 |
| B05 | ví dụ/ứng dụng | Quét khoảng [7,23] qua chuỗi lá | ch14.21, 26 |
| B06 | tính đúng | Bất biến định tuyến; khóa duy nhất, danh sách RID hoặc cận dưới khóa ghép | ch14.20–22, 25 |
| B07 | chi phí | $f=\lceil m/2\rceil$, $d=O(\log_f K)$; điểm $d+1+D$, khoảng $d+1+L+D$; $N$ là số khối tệp | ch14.24, 27–28 |
| B08 | kiểm tra | Tìm 17, đáp án ẩn | bài 14.3(b) |
| C00 | tình huống | Cập nhật trực tuyến không xây lại cây | ch14.17, 29–39 |
| C01 | ví dụ | Insert 9, 10 chưa tràn | bài 14.4(a,b), lời giải tr.102 |
| C02 | ví dụ | Insert 8 tạo sáu khóa và tách 3–3 | bài 14.4(c), lời giải tr.102 |
| C03 | cơ chế | Tách lá sao chép khóa phân cách 10 | ch14.29–32; bài 14.4(c) |
| C04 | thuật toán | Giả mã chèn cho khóa duy nhất/khóa ghép; RID-list chỉ tăng danh sách | ch14.29–33 |
| C05 | cơ chế/biên | Với $m=6$, đẩy 15; giữ [5,10] và [20,25,30] | ch14.30, 33 |
| C06 | tính đúng | Thứ tự, khoảng và độ sâu sau tách | ch14.29–33 |
| C06A | kiểm tra | Phân biệt sao chép ở lá với đẩy ở nút trong | ch14.30, 33 |
| C07 | ví dụ xóa | Delete 23 đủ chỗ; Delete 19 thiếu | bài 14.4(d,e) |
| C08 | trực giác/thuật toán | Mượn, gộp và lan lên cha | ch14.34–38 |
| C09 | ví dụ | Trạng thái sau xóa 19 trước gộp và cây cuối sau gộp, đủ cạnh và chuỗi lá | lời giải 14.4(b), tr.103 |
| C10 | thuật toán | Giả mã xóa; RID-list chỉ xóa khóa khi danh sách rỗng | ch14.37–38 |
| C11 | chi phí/kiểm tra | Đọc $O(d+1)$, ghi tối đa $O(d+1)$; tăng/giảm gốc | ch14.30, 38–39 |
| D00 | đối chiếu | Vị trí khóa và con trỏ trong hai cây | ch14.46–48 |
| D01 | quyết định | Hệ số phân nhánh và quét khoảng; không xếp hạng I/O tuyệt đối | ch14.46–48 |
| H00 | tình huống | Điều kiện bằng trên tệp lớn | ch14.51–59 |
| H02 | ví dụ | Physics và Elec. Eng. cùng ngăn 3; chưa suy diễn tràn | ch14.53–56 |
| H01 | đặc tả | $h:\mathcal K\to\{0,\ldots,M-1\}$, sức chứa $c$, hệ số tải $\alpha$ | ch14.52 |
| H03 | thuật toán/tính đúng | Tra cứu chuỗi và kiểm khóa thật | ch14.52–54 |
| H04 | cập nhật/biên | Chèn, xóa, khóa trùng và ngăn nhà | ch14.52–54 |
| H05 | chi phí/giới hạn | $1+t+D$; giả thiết băm gần đều và tải được kiểm soát | ch14.53, 57–59 |
| H06 | kiểm tra | Tự chạy vết bốn khoa và kiểm khóa thật | ch14.53–59 |
| M00 | tình huống | Nhiều bộ lọc trên thuộc tính ít giá trị | ch14.71–75; ch24.11–15 |
| M00A | trực giác/ví dụ | Ba hàng đầu tạo Finance=010 và S4=010 | lời giải 14.13, tr.108 |
| M01 | đặc tả | Ánh xạ vị trí bit và bốn dải lương | ch14.71–72; bài 14.13 |
| M02 | ví dụ | Bốn bitmap lương của 12 bản ghi | lời giải 14.13(a), tr.108 |
| M03 | ví dụ/thuật toán | Finance AND S4 rồi lọc lại >=80.000 | lời giải 14.13(b), tr.109 |
| M04 | chi phí | $\lceil R/w\rceil$; $qR$ bit giá trị, tối đa $(q+2)R$ với $E$/NULL; trang bitmap + $D$ | ch14.73, 75; ch24.13, 15 |
| M05 | hình thức/biên | NOT với bảng chân trị của $E,V_v,V_{\mathrm{NULL}}$ | ch24.14 |
| M06 | tính đúng | Bất biến từng vị trí và điều kiện dư | ch24.13–14; bài 14.13 |
| M07 | kiểm tra | Chọn công thức NOT đúng | ch24.14 |
| T00 | tổng hợp | Ma trận truy vấn và I/O của bốn cấu trúc | tổng hợp nguồn |
| T01 | tổng hợp | Ma trận cập nhật và dung lượng: cây $O(d+1)$, bitmap tối đa $(q+2)R$ | tổng hợp nguồn |
| X00 | giao nhiệm vụ | Bốn bài trực tiếp, tổng 60 phút | bài 14.1, 14.3, 14.4, 14.13 |
| X01 | bài 14.1 | Chi phí của quá nhiều chỉ mục, 5 phút | đề tr.43; lời giải tr.99 |
| X02 | bài 14.3(b) | Dữ kiện và vết tách, 5 phút | đề tr.43 |
| X03 | bài 14.3(b) | Cây cuối và kiểm bất biến, 10 phút | lời giải PDF 2/tr.100 |
| X04 | bài 14.4(a,b) | Insert 9, 10, 8 phút | đề tr.43; lời giải tr.102 |
| X05 | bài 14.4(c) | Insert 8 và kiểm bảo toàn khóa, 7 phút | lời giải tr.102 |
| X06 | bài 14.4(d,e) | Delete 23, 19, 10 phút | lời giải tr.102–103 |
| X07D | dữ kiện 14.13 | Bảng đủ 12 ID, tên, khoa, lương, 3 phút | lời giải tr.108 |
| X07 | bài 14.13(a) | Dựng bốn bitmap lương, 5 phút | đề tr.45; lời giải tr.108 |
| X08 | bài 14.13(b) | AND, ứng viên và lọc lại, 7 phút | lời giải tr.109 |

## Câu nối và thay đổi so với nguồn

- `A03→B00`: từ loại truy vấn sang cấu trúc hỗ trợ cả điểm và khoảng.
- `B08→C00`: tìm kiếm đã đúng; tiếp theo giữ bất biến khi dữ liệu đổi.
- `C11→D00`: B+-Tree đã hoàn chỉnh; dùng B-Tree để thấy lựa chọn đặt dữ liệu ở nút trong.
- `D01→H00`: bỏ nhu cầu thứ tự để định tuyến trực tiếp bằng hàm băm.
- `H06→M00`: từ một điều kiện bằng sang nhiều điều kiện trên tập bản ghi.
- `M07→T00`: hợp nhất các cấu trúc theo dạng truy cập.

Thay đổi cục bộ: đặt vết chạy trước hình thức hóa ở `B03→B02`, `H02→H01` và `M00A→M01`; các trang lân cận hai phía đã được rà lại để giữ câu nối. Dùng bài 14.3(b) làm vết giảng, chỉ giữ $m=6$. Tách rõ tách lá sao chép khóa phân cách và tách nút trong đẩy khóa phân cách. Dùng Chương 24 cho NOT, bản ghi đã xóa và NULL. Hình lời giải 14.4 sau Insert 8 được sửa 9 thành 19 để bảo toàn đa tập khóa. Bảng `X07D` làm bài 14.13 tự chứa; đáp án vẫn ẩn trong fragment và ghi chú.

## Thời lượng

Phần giảng: P 6 + A 10 + B 25 + C 35 + D 5 + H 16 + M 19 + T 4 = **120 phút**. Recitation: X01 5 + X02–X03 15 + X04–X06 25 + X07D–X08 15 = **60 phút**. `X00` chỉ giao nhiệm vụ trong thời gian chuyển nhóm.
