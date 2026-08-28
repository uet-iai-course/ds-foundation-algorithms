# Storyboard Bài 11

## Hành trình khái niệm

P02 tách hai đặc tả. LZ77, LZ78 và LZW phải khôi phục đúng chuỗi; chúng khác nhau ở trạng thái dùng để biểu diễn cụm lặp. JPEG chấp nhận sai số từ lấy mẫu sắc tùy chọn và lượng tử hóa để giảm tốc độ bit. S00 đặt bốn phương pháp cạnh nhau theo nguồn dư thừa, trạng thái và đặc tả khôi phục.

### Chu trình LZ77 — 29 phút

- **Đầu vào và sản phẩm:** sinh viên biết chuỗi byte và mảng; sau cụm có thể mã hóa, giải mã token và giải thích sao chép chồng lấn.
- **Tình huống:** L00 dùng luồng nhật ký đọc một lượt, cửa sổ hữu hạn và dòng bộ ba đầu ra. Tình huống quay lại ở L08 qua bộ nhớ, phạm vi lặp và chi phí bit của token.
- **Trạng thái truyền:** cửa sổ L01 → hai dạng token L02 → ba hàng vết L04 → cận và giả mã L03 → sao chép tuần tự L05–L06 → hai nhánh chứng minh L07 → cận vét cạn L08.
- **Câu nối:** “Cửa sổ cho biết nguồn có thể nằm ở đâu; bộ ba cho biết phải chép gì.” “Ba hàng vết cho ta điều kiện tổng quát của giả mã.” “Sao chép tuần tự là bước cần chứng minh để hai lịch sử tiếp tục giống nhau.”
- L02 chỉ giới thiệu từ vựng; cận hình thức nằm ở L03 nên ví dụ L04 đứng trước thuật toán tổng quát.

### Chu trình LZ78 — 20 phút

- **Đầu vào và sản phẩm:** sinh viên đã biết cây tiền tố; sau cụm có thể dựng cùng từ điển ở hai phía và nêu chính sách khi đầy.
- **Tình huống:** Z00 dùng luồng ký hiệu có cụm lặp xa, đọc một lượt, đầu ra là cặp `(mã cụm, ký tự)`. Z05 dùng lại giới hạn bộ nhớ và độ rộng mã.
- **Trạng thái truyền:** quy tắc một cạnh Z01 → bốn cặp của `aabaacabcabcb` ở Z02 → hai giả mã dùng $D[next]=D[i]+c$ ở Z03 → hai nhánh thường/EOS ở Z04 → biểu diễn mục từ Z05 → hai cặp còn lại Z06.
- **Câu nối:** “Cây cho biết một mục mới dùng lại tiền tố nào.” “Bốn cặp cho thấy hai phía thực hiện cùng phép cập nhật.” “Cùng trạng thái trước cặp đủ để quy nạp.” “LZ78 còn gửi ký tự mới; LZW sẽ suy ra ký tự này.”

### Chu trình LZW — 23 phút

- **Đầu vào và sản phẩm:** sinh viên biết LZ78 và mã số nguyên; sau cụm có thể mã hóa, giải mã và phân biệt mã đến sớm với mã lỗi.
- **Tình huống:** W00 dùng luồng byte lớn, một lượt, bảng chữ cái nạp sẵn và dòng mã nguyên. W06 quay lại độ rộng mã, reset, bộ nhớ và điều kiện mã cụm tiết kiệm bit.
- **Trạng thái truyền:** khởi tạo $D[0..255]$, `next_code=256` ở W00 → vết đầy đủ `ppqpprpqrpqrq` ở W02 → giả mã mã hóa W01 → ba mã đầu được giải lại ở W03 → nhánh `k=next_code` W04 → thuật toán và bất biến W05 → giả thiết băm và biểu diễn (cha, ký tự) W06.
- **Câu nối:** “Bảng chữ cái nạp sẵn cho phép bỏ ký tự khỏi cặp LZ78.” “Mỗi hàng chưa có `wk` trong vết trở thành một nhánh của giả mã.” “Đường thường dựng lại đúng các mục đầu; chỉ còn một mã chưa có nhưng hợp lệ.”

### Chu trình JPEG — 36 phút

- **Đầu vào và sản phẩm:** sinh viên biết đại số tuyến tính cơ bản và mã entropy từ Bài 10; sau cụm có thể phân loại bước mất dữ liệu và mô tả dòng DC/AC.
- **Tình huống:** J00–J01 dùng kho ảnh cần giảm lưu trữ và băng thông, đầu ra gần đúng, tốc độ bit và MSE. J06–J07 nối lượng tử với sai số; J10 quay lại chi phí trên toàn ảnh.
- **Trạng thái truyền:** đường ống J02 → khối và dịch mức J03 → trực giác tần số J05 → DCT hình thức J04 → lượng tử chạy tay J06 → ma trận chất lượng J07 → DC/AC J08 → IDCT J09.
- **Câu nối:** “Đường ống cho biết bước nào cần hiểu trước.” “Mẫu trơn và dao động chuẩn bị cho công thức DCT.” “Hệ số sau làm tròn đi vào dòng DC/AC rồi IDCT, nên phần đã bỏ không thể quay lại.”
- Hình J05 là minh họa định tính; công thức J04 mới là định nghĩa toán học.

## Bản đồ từng trang

| Thứ tự | Mã | Luận điểm và hoạt động | Nguồn | Phút |
|---:|---|---|---|---:|
| 1 | P00 | Đặt Bài 11 sau mã hóa xác suất | Nelson–Gailly Ch.8–11 | 1 |
| 2 | P01 | Công bố năm đầu ra quan sát được | `source.md`, Bài 11 | 2 |
| 3 | P02 | Tách đặc tả khôi phục đúng và gần đúng | CMU LZ logic 2; lossy logic 2, 13 | 3 |
| 4 | L00 | Luồng nhật ký, một lượt, cửa sổ hữu hạn | Nelson–Gailly PDF tr.176–181 | 3 |
| 5 | L01 | Từ điển và vùng nhìn trước | CMU logic 4 | 3 |
| 6 | L02 | Literal, tham chiếu và EOS | CMU logic 4–6 | 3 |
| 7 | L04 | Vết `aacaacabc…` trước giả mã | CMU logic 5 | 3 |
| 8 | L03 | Cận và giả mã cụm dài nhất | CMU logic 4–5 | 3 |
| 9 | L05 | Sao chép chồng lấn | CMU logic 5–6; sách PDF tr.180–181 | 4 |
| 10 | L06 | Giả mã giải mã tuần tự | CMU logic 6 | 3 |
| 11 | L07 | Hai nhánh token thường/EOS trong chứng minh | Suy ra từ đặc tả nguồn | 3 |
| 12 | L08 | $O(nWL)$ vét cạn, $O(n)$ giải mã, $O(W+L)$ bộ nhớ | CMU logic 7–10 | 2 |
| 13 | L09 | Kiểm tra token chồng lấn | Dẫn xuất từ quy tắc CMU | 2 |
| 14 | Z00 | Luồng ký hiệu và từ điển toàn luồng | Nelson–Gailly PDF tr.208–211 | 3 |
| 15 | Z01 | Trực giác cây: thêm đúng một ký tự | CMU logic 11 | 3 |
| 16 | Z02 | Chạy tay bốn cặp đầu | CMU logic 13–14 | 3 |
| 17 | Z03 | Mã hóa và giải mã cùng cập nhật | CMU logic 12, 14 | 3 |
| 18 | Z04 | Quy nạp với token thường và token EOS | Suy ra từ đặc tả nguồn | 3 |
| 19 | Z05 | Chính sách đầy, giả thiết gần tuyến tính và $O(M)$ bộ nhớ | Nelson–Gailly PDF tr.214–219; CMU logic 21 | 3 |
| 20 | Z06 | Kiểm tra hai cặp còn lại | CMU logic 13–14 | 2 |
| 21 | W00 | Cầu nối LZ78→LZW; bảng byte và `next_code` | CMU logic 15 | 3 |
| 22 | W02 | Vết đầy đủ với mã 112–114 và mục 256–264 | CMU logic 17 | 3 |
| 23 | W01 | Khái quát hóa vết thành giả mã mã hóa | CMU logic 17 | 3 |
| 24 | W03 | Giải lại ba mã đầu theo đường thường | CMU logic 19; sách PDF tr.222–227 | 4 |
| 25 | W04 | Trực giác mã bằng `next_code` đến sớm | CMU logic 16 | 3 |
| 26 | W05 | Giả mã đầy đủ và bất biến đồng bộ | CMU logic 16, 19 | 3 |
| 27 | W06 | Độ rộng mã, băm kỳ vọng và $O(M)$ bộ nhớ | CMU logic 21; sách Ch.9 | 2 |
| 28 | W07 | Kiểm tra trường hợp mã chưa có | Dẫn xuất từ logic 16 | 2 |
| 29 | J00 | Kho ảnh và đặc tả gần đúng | Nelson–Gailly PDF tr.240, 250–254 | 3 |
| 30 | J01 | Tốc độ bit và MSE | CMU lossy logic 2–3 | 3 |
| 31 | J02 | Hai vị trí có thể mất dữ liệu | CMU logic 13–16 | 3 |
| 32 | J03 | Không gian màu, khối, dịch mức | sách PDF tr.252–257 | 3 |
| 33 | J05 | Trực giác định tính về tần số | CMU logic 9–12 | 3 |
| 34 | J04 | DCT, miền chỉ số và chuẩn hóa | sách PDF tr.255–258 | 4 |
| 35 | J06 | Chạy tay lượng tử hóa | sách PDF tr.258–261 | 4 |
| 36 | J07 | Ma trận lượng tử và chất lượng | CMU logic 15 | 3 |
| 37 | J08 | DC sai phân; AC zigzag/RLE/entropy | CMU logic 16; sách PDF tr.261–263 | 3 |
| 38 | J09 | IDCT và phần không thể phục hồi | sách Ch.11 | 3 |
| 39 | J10 | Chi phí tuyến tính theo số mẫu | Suy ra từ khối cố định $8\times8$ | 2 |
| 40 | J11 | Kiểm tra hai loại bước mất dữ liệu và DC/AC | CMU logic 13–16 | 2 |
| 41 | S00 | So sánh bốn phương pháp | Tổng hợp nguồn | 3 |
| 42 | S01 | Buộc chọn riêng LZ77, LZ78, LZW, JPEG | Tổng hợp nguồn | 3 |
| 43 | X00 | Giao nhiệm vụ và sản phẩm | CMU logic được chỉ định | 0 |
| 44 | X01 | Hoàn tất vết LZ77 `aacaacabcabaaac` | CMU LZ logic 5 | 12 |
| 45 | X02 | Giải mã `(2,9,e)`, position 0-based | CMU LZ logic 6 | 8 |
| 46 | X03 | Hoàn tất vết LZ78 | CMU LZ logic 13–14 | 12 |
| 47 | X04 | Chứng minh nhánh LZW `k=next_code` | CMU LZ logic 16 | 15 |
| 48 | X05 | Tiêu chí chọn biến đổi | CMU lossy logic 11 | 13 |

Tổng phần giảng: 120 phút. Tổng recitation: 60 phút.

## Sai khác có chủ ý

- Đổi `position` của bộ ba LZ77 trên slide CMU thành khoảng lùi $d$ trong phần giảng; X02 giữ position của CMU và ghi rõ đánh số từ 0.
- Chọn ký hiệu $EOS$ dành riêng cho trường hợp đầu vào kết thúc đúng sau một cụm khớp; không dùng token cuối riêng.
- Đổi thứ tự L04 trước L03, Z02 trước Z03, W02 trước W01 và J05 trước J04 để chạy tay hoặc trực giác đứng trước hình thức hóa.
- Vẽ lại vết LZW đầy đủ cho `ppqpprpqrpqrq`; bổ sung các hàng kéo dài, mã cuối và mục 263–264 được suy ra trực tiếp từ quy tắc nguồn.
- Tách đường thường W03 khỏi nhánh mã đến sớm W04, rồi hợp nhất ở W05.
- Bổ sung chi phí bit định tính cho LZ; không đưa tỷ lệ nén vì nguồn và định dạng không cho một giá trị cố định.
- Phân biệt lấy mẫu sắc mất dữ liệu tùy chọn với lượng tử hóa mất dữ liệu bắt buộc trong lõi hệ số.
- Bổ sung DC sai phân và AC zigzag/RLE/entropy để hoàn thiện đường ống JPEG cơ sở.
- Không dùng hình DCT như dữ liệu chính xác; J05 và SVG đều ghi đây là minh họa định tính.
- Không đưa MPEG, wavelet, Burrows–Wheeler và ACB vì ngoài chuẩn đầu ra.
- Recitation dùng trực tiếp CMU logic 5, 6, 13, 16 và lossy 11. Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28, chấp nhận ví dụ giáo trình và bài tập CMU.

## Trạng thái phần recitation

X01–X05 giữ nguyên nguồn cụ thể trong bảng và tổng thời lượng $12+8+12+15+13=60$ phút. Ngoại lệ nguồn đã được người dùng phê duyệt ngày 2026-08-28; lỗi chặn đã đóng và không còn lỗi chặn hoặc nghiêm trọng.
