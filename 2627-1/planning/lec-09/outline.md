# Dàn ý Bài 9

## Phạm vi và mục tiêu

- Bài 9 theo thứ tự đề xuất: **Dòng dữ liệu: đếm, mômen và cửa sổ**.
- Phần giảng 120 phút; phần bài tập củng cố 60 phút.
- Đầu vào kiến thức: mô hình dòng, hàm băm, xác suất cơ bản, kỳ vọng và lấy mẫu hồ chứa từ Bài 8.
- Sản phẩm: chọn phác thảo theo đại lượng cần ước lượng; chạy và giải thích Flajolet–Martin, Count-Min Sketch, AMS và DGIM; nêu bảo đảm cùng điều kiện áp dụng; cập nhật một tổng suy giảm mũ.
- Ngoài phạm vi: cơ chế HyperLogLog chuẩn, biến thể DGIM sai số tùy ý, Count-Min cho dòng có cập nhật âm và thuật toán tự sinh danh sách khóa nặng.

## Nguồn và quyết định chọn

| Cụm | Khớp chuẩn đầu ra | Độ chính xác và tính hiện thời | Ví dụ hoặc hình | Khả năng Việt hóa | Nguồn được chọn và lý do |
|---|---|---|---|---|---|
| Đếm phân biệt | MMDS và Stanford đều khớp $F_0$. | Sách MMDS và Stanford 2017 cho đúng thứ tự gộp; MMDS Streams 2 tr.25 và Stanford 2026 tr.44 đảo thứ tự. | MMDS có vết băm và bài tập trực tiếp. | Ký hiệu ngắn, dễ vẽ lại. | Sách MMDS tr.142–145 làm chuẩn; Stanford 2017 Streams 2 kiểm tra thứ tự trung bình trong nhóm rồi trung vị giữa nhóm. |
| Count-Min Sketch | Không có trong MMDS Chương 4 hoặc các slide Stanford được ánh xạ. | UMass nêu đầy đủ miền băm, khuếch đại xác suất và tham số khóa nặng. | Có cơ chế va chạm và lập luận Markov. | Có thể Việt hóa mà giữ tên thuật toán. | Chỉ dùng UMass CS514 Lecture 10 với $m=\lceil2k/\varepsilon\rceil$, $t=\lceil\log_2(1/\delta)\rceil$; không trộn dạng tham số khác. |
| Mômen và AMS | Cả hai nguồn khớp $F_2$ và tính không chệch. | Sách MMDS nêu đầy đủ biến hậu tố và chứng minh. | MMDS có ví dụ 910/8110 và vết ba vị trí. | Thuận lợi, ký hiệu nhất quán với sách. | MMDS tr.145–150 làm trục; Stanford 2017 chỉ đối chiếu. |
| DGIM | Cả hai nguồn khớp đếm bit 1 trong hậu tố. | Sách MMDS xác định sáu bất biến và cận 50%; Stanford diễn đạt cập nhật dễ theo dõi. | Hình 4.2 và 4.3 của MMDS nối trực tiếp với bài tập. | Phải vẽ lại mốc phải và phần trái chưa xác định. | MMDS tr.151–157 làm trục; Stanford 2017 Streams 1 tr.13–24 dùng để kiểm tra diễn đạt cập nhật/truy vấn. |
| Cửa sổ suy giảm | Cả hai nguồn khớp ý giảm trọng số theo tuổi. | Sách MMDS cho định nghĩa, tổng hữu hạn và truy hồi. | Hình 4.4 đủ cho so sánh với cửa sổ cứng. | Dễ Việt hóa. | MMDS tr.157–159 làm chuẩn; Stanford 2017 Streams 1 tr.27–29 đối chiếu. |

MMDS được ưu tiên khi hai nguồn tương đương. Slide Stanford 2017 được dùng để kiểm tra thứ tự gộp FM và cách diễn đạt DGIM; không sao chép giao diện hoặc tài sản. Ghi công: <http://www.mmds.org>.

Tệp `umass-cs514/lecture8-hyperloglog.pdf` chỉ đủ cho FM/LogLog, không mô tả đầy đủ HyperLogLog chuẩn. Deck chỉ nêu HyperLogLog là hướng mở rộng.

## Mạch phần giảng

1. P00–A02: tình huống dòng sự kiện và bản đồ chọn cấu trúc, 8 phút.
2. F00–F06: Flajolet–Martin, 22 phút.
3. C00–C04: Count-Min Sketch rút gọn, 14 phút.
4. M00–M07: mômen bậc hai và AMS, 25 phút.
5. D00–D09: cửa sổ bit và DGIM, 36 phút.
6. E00–E01: cửa sổ suy giảm mũ, 7 phút.
7. T00–T01: tổng hợp bảo đảm và giới hạn, 8 phút.

Tổng phần giảng: **120 phút**.

## Bài tập củng cố

| Bài | Nguồn | Phút |
|---|---|---:|
| X01 | MMDS Ex.4.4.1, tr.145 | 12 |
| X02 | MMDS Ex.4.5.1, tr.149–150 | 8 |
| X03 | MMDS Ex.4.5.3, tr.150 | 12 |
| X04 | MMDS Ex.4.6.1, tr.157 | 12 |
| X05 | MMDS Ex.4.6.3, tr.157 | 16 |

Tổng phần bài tập: **60 phút**. X00 chỉ mở phần, không tính thời lượng.

## Thuật ngữ và ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $f_x$, $f_i$ | tần suất của khóa $x$ hoặc khóa thứ $i$ |
| $F_k=\sum_i f_i^k$ | mômen bậc $k$ của dòng |
| $\rho(h(x))$ | số bit 0 liên tiếp ở cuối giá trị băm |
| $R$ | cực đại của $\rho$ đã quan sát |
| $C[j,h_j(x)]$ | ô Count-Min ở hàng $j$ cho khóa $x$ |
| $I$, $c_I$ | vị trí chọn đều và số lần khóa tại $I$ xuất hiện trong hậu tố |
| $N$, $k$ | độ dài cửa sổ DGIM và độ dài hậu tố truy vấn |
| $c$ | hệ số suy giảm, $0<c<1$ |

## Kiểm kê hình và nội dung

- Chín SVG tự vẽ: bản đồ quyết định; vết FM; bảng Count-Min; vết AMS; trạng thái DGIM nền; truy vấn DGIM $k=10$; bài tập DGIM $k=5,15$; trạng thái đầu cho chuỗi gộp; so sánh trọng số cửa sổ.
- Thuật toán: FM, Count-Min, AMS và cập nhật/truy vấn DGIM; truy hồi cửa sổ suy giảm.
- Lập luận: ngưỡng FM dưới mô hình băm lý tưởng; cảnh báo đuôi nặng; nhiễu kỳ vọng, Markov và khuếch đại Count-Min; tính không chệch AMS; bất biến, chi phí và cận sai số DGIM.
- Không có ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.
