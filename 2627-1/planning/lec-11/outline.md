# Bài 11: Nén bằng từ điển và nén mất dữ liệu

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. mô phỏng LZ77, giải thích sao chép chồng lấn và nêu cận theo cửa sổ;
2. mã hóa, giải mã LZ78 và chứng minh hai phía duy trì cùng từ điển;
3. mã hóa, giải mã LZW và xử lý đúng trường hợp `k = next_code`;
4. theo dõi JPEG mất dữ liệu dựa trên DCT qua khối $8\times8$, lượng tử hóa, DC/AC và zigzag;
5. phân biệt khôi phục đúng chuỗi với khôi phục ảnh gần đúng.

Phần giảng gồm 42 trang, 120 phút. Phần recitation gồm 6 trang, 60 phút.

## Nguồn và quyết định

| Cụm | Nguồn trục | Nguồn đối chiếu | Quyết định |
|---|---|---|---|
| LZ77 | Nelson–Gailly Chương 8, PDF tr. 174–180 | CMU `compression3-lz.pdf`, logic 3–10 | Dùng vết `(3,4,b)` của CMU; phần giảng đổi position thành khoảng lùi. |
| LZ78 | Nelson–Gailly Chương 9, PDF tr. 208–213 | CMU logic 11–14, 18 | Dùng chuỗi `aabaacabcabcb`; token thường có thể là token cuối; chỉ dùng `(i,EOS)` khi nguồn hết ngay sau cụm đã biết. |
| LZW | Nelson–Gailly Chương 9, PDF tr. 214–226 | CMU logic 15–19 | Giữ vết CMU, bất biến độ trễ một mục và nhánh `k = next_code`; phân biệt $T=2^b$ với `MAX`, nhưng để định dạng công bố riêng mốc đổi độ rộng của bộ mã hóa và bộ giải mã theo early/late-change. |
| JPEG | Nelson–Gailly Chương 11, PDF khoảng tr. 246–266; dịch mức ở PDF tr. 268 | CMU `compression4-lossy.pdf`, logic 2–16 | Không dùng Chương 10 cho JPEG. Dùng RMS ở PDF tr. 266; lượng tử hóa không khả nghịch nói chung. |
| Recitation | CMU LZ logic 5, 6, 13, 16; lossy logic 11 | Các chương trên | Giữ dữ kiện nguồn; chỉ đổi ký hiệu hoặc chia yêu cầu thành bước. Bao phủ mục tiêu 1–3, 5 và một phần mục tiêu 4. |

MMDS và Stanford CS246 không có cụm tương đương cho bài này.

## Bảy mạch trình bày

| Mạch | Trang | Chức năng | Kết nối vào | Kết nối ra | Đóng góp mục tiêu | Phút |
|---|---|---|---|---|---|---:|
| Mở bài | P00–P02 | Tách hai đặc tả khôi phục | Bài 10 về mã entropy | Chọn trạng thái phù hợp với đặc tả | Mục tiêu 5 | 6 |
| LZ77 | L00–L09 | Cửa sổ, vết chạy, giải mã, chứng minh, chi phí | Khôi phục đúng chuỗi | Từ cửa sổ hữu hạn sang từ điển toàn luồng | Mục tiêu 1 | 29 |
| LZ78 | Z00–Z06 | Cụm tăng dần và đồng bộ hai từ điển | Hạn chế lặp cục bộ của LZ77 | Bỏ trường ký tự để đến LZW | Mục tiêu 2 | 20 |
| LZW | W00–W07 | Dòng mã, nhánh mã chưa có, hợp đồng định dạng | LZ78 phát `(i,c)` | Đối chiếu với đặc tả gần đúng | Mục tiêu 3 | 23 |
| JPEG | J00–J11 | DCT, lượng tử, DC/AC, zigzag, IDCT | Chuyển từ khôi phục đúng sang gần đúng | Cung cấp tiêu chí so sánh | Mục tiêu 4–5 | 36 |
| Kết luận | S00–S01 | Chọn phương pháp theo nguồn dư thừa và trạng thái | Thu hồi bốn thuật toán | Chuẩn bị bài tập | Mục tiêu 5 | 6 |
| Recitation | X00–X05 | Thực hành vết chạy, chứng minh và lựa chọn biến đổi | Dùng trạng thái của sáu mạch trước | Sản phẩm nộp và hướng dẫn chấm trong notes | Mục tiêu 1–3, 5; một phần 4 | 60 |

## Chu trình học tập

| Cụm | Tình huống | Vấn đề | Trực giác | Chạy tay | Hình thức | Thuật toán và lập luận đúng | Chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| LZ77 | L00 | L01–L02 | L01–L02 | L04–L05 | L03 | L06–L07 | L08 | L09 |
| LZ78 | Z00 | Z00–Z01 | Z01 | Z02 | Z03 | Z03–Z04 | Z05 | Z06 |
| LZW | W00 | W00 | W00 | W02–W03 | W01 | W04–W05 | W06 | W07 |
| JPEG | J00–J01 | J02 | J03, J05 | J06 dùng hai ô số từ Hình 11.10–11.11 | J04, J06 | J08–J09 | J07, J10 | J11 |

## Thuật ngữ và ký hiệu

| Ký hiệu | Cách dùng |
|---|---|
| $(d,\ell,c)$ | Khoảng lùi, độ dài và ký tự kế trong biến thể LZ77 của phần giảng. |
| $EOS$ | Ký hiệu ngoài bảng chữ cái; không được phát ra khi giải mã. |
| $D[i]$ | Cụm mang mã $i$ trong LZ78 hoặc LZW. |
| `next_code` | Mã chưa cấp nhỏ nhất trong LZW. |
| $C_{u,v},\hat C_{u,v},\tilde C_{u,v}$ | Hệ số DCT, số nguyên lượng tử và hệ số tái tạo. |
| $Q_{u,v}$ | Bước lượng tử. |
| RMS | Căn sai số bình phương trung bình; không thay thế đánh giá cảm nhận. |
| DCT | Biến đổi cosine rời rạc dùng trên từng khối $8\times8$. |
| DC, AC | Hệ số một chiều $C_{0,0}$ và 63 hệ số còn lại. |
| RLE | Mã độ dài loạt dùng cho các loạt 0 sau quét zigzag. |

## Tài sản trực quan

Có 12 SVG trong `2627-1/img/lec-11/`. Các hình LZ77 dùng vết CMU `(3,4,b)`; cây LZ78 có $D[2]=ab,D[4]=c$; lượng tử hóa dùng hai ô số từ Hình 11.10–11.11; zigzag đi qua đủ 64 ô và đánh dấu lượt 6, 15. Không dùng raster hoặc tài nguyên mạng.

## Bản đồ chủ đề của ghi chú tự học

Ghi chú giữ nguyên mục tiêu, ký hiệu và thứ tự khái niệm của deck nhưng mở rộng lập luận, vết chạy và chứng minh. Mỗi chủ đề có một sản phẩm học tập kiểm tra được.

| `note-topic-id` | Nhãn | Chủ đề | Đầu vào | Sản phẩm học tập | Nguồn và quan hệ |
|---|---|---|---|---|---|
| `L11-N01` | cốt lõi | Hai đặc tả khôi phục | Bài 10 về mã entropy | Loại phương pháp trái với yêu cầu bảo toàn | `source.md`, CMU; mở hai nhánh N02 và N07 |
| `L11-N02` | cốt lõi | LZ77: cửa sổ, token, vết chạy | Chuỗi và mảng | Phát đúng năm token, giải thích chồng lấn | Nelson–Gailly Ch.8, CMU logic 3–6; sang N03 |
| `L11-N03` | cốt lõi | LZ77: giải mã, bất biến, chi phí | N02 | Chứng minh khôi phục đúng và nêu cận theo $n,W,L$ | Ch.8, CMU logic 6–10; nêu giới hạn để sang N04 |
| `L11-N04` | cốt lõi | LZ78: từ điển cụm và EOS | Cây tiền tố, N03 | Chạy vết, phân biệt hai nhánh kết thúc, chứng minh đồng bộ | Ch.9, CMU logic 11–14, 18; sang N05 |
| `L11-N05` | cốt lõi | LZW: mã hóa và vết từ điển | N04, mã byte | Sinh đúng dòng 10 mã và các mục 256–264 | Ch.9, CMU logic 15–17; chuẩn bị N06 |
| `L11-N06` | cốt lõi | LZW: giải mã và hợp đồng bit | N05 | Xử lý ba trường hợp của mã kế và độ trễ một mục | Ch.9, CMU logic 16, 19; đóng nhánh khôi phục đúng |
| `L11-N07` | cốt lõi | JPEG: tốc độ bit–sai số và đường ống | N01, đại số tuyến tính | Phân loại đúng bước khả nghịch và mất dữ liệu | Ch.11, CMU lossy logic 2, 13–16; sang N08 |
| `L11-N08` | cốt lõi | DCT khối và lượng tử hóa | N07 | Tính hai ô lượng tử và chỉ ra nơi mất dữ liệu | Ch.11, Hình 11.10–11.11; sang N09 |
| `L11-N09` | cốt lõi | DC/AC, zigzag, RLE, IDCT | N08, mã entropy | Nối hệ số lượng tử với dòng bit và ảnh tái tạo | Ch.11; đóng nhánh gần đúng |
| `L11-N10` | cầu nối | So sánh bốn phương pháp | N03, N06, N09 | Chọn phương pháp theo đặc tả và chi phí trạng thái | Tổng hợp N01–N09; sang N11 |
| `L11-N11` | cốt lõi | Năm bài tập có lời giải | N02–N10 | Mô phỏng, chứng minh và giải thích bằng dữ kiện nguồn | Năm bài CMU đã chọn |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06`; `N01→N07→N08→N09`; hai nhánh hội tụ ở `N10`, rồi sang `N11`. Không có chủ đề bổ sung ngoài nguồn; MIT 15.564 chỉ dùng để đối chiếu tổng quan.
