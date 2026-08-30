# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. Đặc tả thuật toán quét-cộng dồn trên kho dữ liệu không vừa bộ nhớ và chứng minh tính đúng bằng bất biến tiền tố.
2. Phân biệt bài toán, biểu diễn dữ liệu, thuật toán, cài đặt và kết quả.
3. Phân tích ba chi phí cùng bảo đảm của một lời giải dữ liệu lớn.
4. Dùng số phép thử và xác suất một phép thử để ước lượng số biến cố trùng ngẫu nhiên.

Phần số chiều lớn chỉ định tuyến, không phải mục tiêu đánh giá. Phần giảng dài 120 phút. Phần bài tập trong cùng bộ trang chiếu dài 60 phút, dùng trực tiếp MMDS Bài 1.2.1 và 1.2.2, trang 8.

## Kiến thức tiên quyết

- Mảng, bảng băm và vòng lặp.
- Ký hiệu độ phức tạp.
- Tổ hợp $\binom{n}{k}$, xác suất độc lập và tính tuyến tính của kỳ vọng.
- Vector, khoảng cách Euclid và số chiều ở mức nhập môn.

## Dàn ý phần giảng

| Phần | Mã trang | Nội dung | Thời lượng |
|---|---|---|---:|
| Mở đầu | P00–P01 | Tình huống và mục tiêu học tập | 5 phút |
| Thuật toán quét-cộng dồn | A00–A08 | Giới hạn bộ nhớ, vết chạy, đặc tả, giả mã, bất biến và chi phí | 32 phút |
| Từ bài toán đến sản phẩm | B00–B07 | Năm tầng của lời giải và hai loại sản phẩm mô hình hóa | 19 phút |
| Mô hình chi phí | C00–C02, C04–C05 | Ba chi phí, một bảo đảm và đặc tả xấp xỉ | 19 phút |
| Tín hiệu giả | D00–D05 | Tình huống lưu trú, mô hình ngẫu nhiên và kỳ vọng số biến cố trùng | 30 phút |
| Định tuyến số chiều lớn | E00–E04 | Khoảng cách, thể tích gần biên và bản đồ 15 bài theo năm nhóm | 15 phút |
| **Tổng** |  |  | **120 phút** |

## Dàn ý phần bài tập

| Hoạt động | Mã trang | Nguồn | Thời lượng | Mốc bàn giao |
|---|---|---|---:|---|
| Dựng ba mô hình thay đổi | R01 | MMDS Bài 1.2.1(a–c), trang 8 | 10 phút | Ba công thức chưa cần tính hết |
| Tính hai thay đổi quy mô | R02 | MMDS Bài 1.2.1(a,b), trang 8 | 15 phút | Hai giá trị và lời giải thích |
| Trùng trong ba ngày | R03 | MMDS Bài 1.2.1(c), trang 8 | 10 phút | Công thức, giá trị, diễn giải |
| Dựng mô hình giỏ hàng | R04 | MMDS Bài 1.2.2 và chú thích 3, trang 8 | 10 phút | Không gian mẫu, số phép thử, kỳ vọng, kết luận |
| Chữa và phản biện mô hình | R05 | MMDS Bài 1.2.2, trang 8 | 15 phút | Lời giải và hai giới hạn giả thiết |
| **Tổng** |  |  | **60 phút** |  |

R00 là trang chuyển phần, không tính vào 60 phút.

## Ánh xạ nguồn

| Nguồn | Phạm vi dùng | Mã trang |
|---|---|---|
| `sources/source.md` | Tên bài, mục tiêu, tình huống kho nhật ký, thứ tự 15 bài | P00–P01, A01, E03–E04 |
| MMDS 3e, trang 1–5 | Khai phá dữ liệu, mô hình, tóm tắt, trích đặc trưng | B00–B07, C04–C05 |
| MMDS 3e, trang 5–8 | Đếm biến cố trùng bằng kỳ vọng (nguyên lý Bonferroni phi hình thức) và ví dụ hồ sơ lưu trú | D00–D05 |
| MMDS 3e, Bài 1.2.1–1.2.2 và chú thích 3, trang 8 | Toàn bộ phần bài tập | R01–R05 |
| MMDS 3e, trang 13 | Lưu trữ thứ cấp và chi phí quét | A01–A02, C00–C02 |
| MMDS 3e, trang 17–19 | Bản đồ chủ đề | E03–E04 |
| Stanford CS246, `01-intro.pdf`, trang chiếu 2–10 | Phạm vi khai phá dữ liệu và dạng dữ liệu | P00, A03, B02, E03 |
| Stanford CS246, `01-intro.pdf`, trang chiếu 62 | Lược đồ kho web và tổng byte theo máy chủ | A01, A04–A08 |
| Blum–Hopcroft–Kannan, PDF trang 9–12 | Dữ liệu hiện đại, bộ nhớ và số chiều lớn | A00, A03, C01, E00–E01 |
| Blum–Hopcroft–Kannan, PDF trang 20–21, Hình 2.2 | Thể tích gần biên | E02 |

Không dùng Stanford trang chiếu 32–61 hoặc 63–70. Trang chiếu 62 là ngoại lệ duy nhất trong khoảng 32–70. Ví dụ bốn bản ghi ở A04 được tự dựng từ lược đồ của trang chiếu 62; không phải dữ liệu thực nghiệm.

## Thuật toán trọng tâm

### Đặc tả và ràng buộc truy cập

- Đầu vào: $L=((u_i,s_i))_{i=1}^{n}$, trong đó $u_i$ là máy chủ và $s_i\in\mathbb{N}_0$.
- Đầu ra: với mỗi máy chủ $u$ đã xuất hiện, $S[u]=\sum_{i:u_i=u}s_i$.
- Điều kiện trước: hai trường hợp lệ và kiểu tổng không tràn.
- Điều kiện sau: bảng có đúng tập máy chủ đã xuất hiện và tổng chính xác cho từng máy chủ.
- Ràng buộc truy cập: dữ liệu được cấp theo thứ tự; thuật toán dùng một lượt quét.

### Bất biến và dừng

Sau $k$ bản ghi, tập khóa của bảng đúng bằng tập máy chủ trong tiền tố; với mỗi khóa $u$, giá trị lưu bằng tổng kích thước của $u$ trong $k$ bản ghi đầu. Mỗi vòng xử lý thêm đúng một bản ghi và dừng sau $n$ bước. Khi $k=n$, hai vế của bất biến suy ra điều kiện sau.

### Chi phí và trường hợp biên

- Thời gian kỳ vọng $O(n)$ nếu mỗi thao tác bảng băm có thời gian kỳ vọng $O(1)$.
- Bộ nhớ $O(h)$ với $h$ là số máy chủ phân biệt.
- Một lượt quét; cận truyền dữ liệu $T_{\text{quét}}\ge D/b$.
- Sai số bằng 0 theo đặc tả.
- Dãy rỗng trả bảng rỗng; kích thước 0 hợp lệ; máy chủ lặp được cộng dồn.
- Nếu bảng $h$ khóa không vừa bộ nhớ, thuật toán không đáp ứng mô hình triển khai đang xét.

## Thuật ngữ và ký hiệu

| Ký hiệu hoặc thuật ngữ | Nghĩa dùng trong bài |
|---|---|
| $D,M,b$ | Kích thước dữ liệu, dung lượng bộ nhớ, băng thông đọc |
| $n,h,d$ | Số bản ghi, số máy chủ phân biệt, số chiều |
| $P,T,H,q$ | Số người, số ngày, số khách sạn, xác suất đi khách sạn |
| mô hình thống kê | Phân phối giả định sinh dữ liệu và các tham số |
| mô hình dữ liệu theo truy vấn | Bản tóm tắt phục vụ một lớp truy vấn; không phải computational model |
| biến cố trùng | Một cặp người cùng một khách sạn trong từng ngày của cặp hoặc bộ ngày đã chọn |
| $X$ ở R05 | Số cặp lượt mua của hai người khác nhau có cùng tập 10 mặt hàng |
| mômen | Đại lượng được gọi là moment trong nguồn tiếng Anh |

## Hình được vẽ lại

| Tệp | Mã trang | Căn cứ |
|---|---|---|
| `kho-nhat-ky-bo-nho.svg` | A01 | MMDS trang 13 và Stanford trang chiếu 62 |
| `giao-thoa-khai-pha-du-lieu.svg` | B02 | Stanford trang chiếu 7; ba hoa văn được dùng thật |
| `phep-thu-va-duong-tinh-gia.svg` | D03 | MMDS trang 7–8 |
| `the-tich-gan-bien.svg` | E02 | BHK Hình 2.2; vành dùng hoa văn chấm |
| `ban-do-hoc-phan.svg` | E03 | MMDS trang 17–18, Stanford trang chiếu 10 và `source.md`; gộp thành năm nhóm bài chữ lớn |

## Thuật ngữ nội bộ

- “Quét-cộng dồn” là thuật ngữ nội bộ của bài, đặt cho thuật toán một lượt quét giữ bảng tổng; nguồn chỉ mô tả hành động, không đặt tên.
