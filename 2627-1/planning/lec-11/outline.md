# Bài 11: Nén bằng từ điển và nén mất dữ liệu

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. đặc tả và mô phỏng LZ77 với cửa sổ trượt, literal, tham chiếu, EOS và sao chép chồng lấn;
2. mã hóa, giải mã LZ78 và chứng minh hai phía duy trì cùng từ điển;
3. mã hóa, giải mã LZW, dựng lại từ điển và xử lý mã bằng `next_code` chưa có;
4. mô tả JPEG cơ sở qua khối $8\times8$, DCT/IDCT, lượng tử hóa, DC sai phân, AC zigzag/RLE và mã entropy;
5. phân biệt mất dữ liệu tùy chọn khi lấy mẫu sắc với mất dữ liệu bắt buộc khi lượng tử hóa;
6. chọn phương pháp theo nguồn lặp, đặc tả khôi phục, cận thời gian–bộ nhớ, chi phí token hoặc mã và mức sai số cho phép.

Phần giảng dài 120 phút, gồm 42 trang. Phần bài tập dài 60 phút, gồm 6 trang và nằm sau phần giảng.

## Nguồn và quyết định chọn nguồn

| Cụm | Nguồn trục | Nguồn đối chiếu | Quyết định |
|---|---|---|---|
| LZ77 | Nelson–Gailly, Chương 8, PDF tr.176–207 | CMU `compression3-lz.pdf`, logic 3–10; MIT `lec3-compression.pdf`, PDF tr.12–13 | Dùng bộ ba và vết CMU; đổi `position` thành khoảng lùi trong phần giảng. Dùng sách để chốt sao chép tuần tự, EOS và giới hạn cài đặt. |
| LZ78 | Nelson–Gailly, Chương 9, PDF tr.208–216 | CMU logic 11–14 | Dùng cây, chuỗi `aabaacabcabcb` và cặp `(mã cụm, ký tự)` của CMU; bổ sung bất biến đồng bộ từ đặc tả sách. |
| LZW | Nelson–Gailly, Chương 9, PDF tr.216–228 | CMU logic 15–21 | Dùng chuỗi và quy tắc của vết CMU, ký hiệu hóa thành `p,q,r`; kiểm lại toàn bộ mã phát và các mục 256–264. Nêu `next_code`, nhánh mã chưa có và thời điểm đổi độ rộng. |
| JPEG | Nelson–Gailly, Chương 10–11, PDF tr.229–264 | CMU `compression4-lossy.pdf`, logic 2–16; MIT PDF tr.9–11 | Dùng CMU cho mạch biến đổi; dùng sách chốt DCT/IDCT, lượng tử, DC/AC và zigzag. Mọi hình được vẽ lại. |
| Recitation | CMU logic 5, 6, 13, 16 và lossy 11 | Nelson–Gailly Chương 8–11 | Giữ câu hỏi và vết khuyết CMU. Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28: chấp nhận ví dụ giáo trình và bài tập CMU cho phần recitation. |

MMDS và Stanford CS246 không bao phủ mô-đun này nên không có cụm tương đương để so sánh. Không dùng các nguồn đó.

## Dàn ý và thời lượng

| Phần | Thứ tự trang | Thời lượng |
|---|---|---:|
| Đặc tả và mục tiêu | P00–P02 | 6 phút |
| LZ77 | L00, L01, L02, L04, L03, L05–L09 | 29 phút |
| LZ78 | Z00–Z06 | 20 phút |
| LZW | W00, W02, W01, W03–W07 | 23 phút |
| JPEG | J00–J03, J05, J04, J06–J11 | 36 phút |
| So sánh và lựa chọn | S00–S01 | 6 phút |
| Bài tập recitation | X00–X05 | 60 phút |

Tổng phần giảng: 120 phút. Tổng phần bài tập: 60 phút. Ngoại lệ nguồn đã được phê duyệt ngày 2026-08-28; không còn lỗi chặn hoặc nghiêm trọng.

## Bản đồ chu trình học tập

| Cụm | Tình huống dữ liệu lớn | Vấn đề | Trực giác | Chạy tay | Hình thức | Thuật toán và lập luận đúng | Ứng dụng và chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| LZ77 | L00 | L01 | L01–L02 | L04–L05 | L03 | L03, L06–L07 | L08 | L09 |
| LZ78 | Z00 | Z00–Z01 | Z01 | Z02 | Z03 | Z03–Z04 | Z05 | Z06 |
| LZW | W00 | W00 | W00 | W02, W03 | W01 | W01, W04–W05 | W06 | W07 |
| JPEG | J00–J01 | J01–J02 | J03, J05 | J06 | J04, J06 | J08–J09 | J07, J10 | J11 |

## Thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Cách dùng |
|---|---|
| từ điển cửa sổ | Hậu tố hữu hạn của chuỗi đã xử lý trong LZ77. |
| vùng nhìn trước | Tiền tố chưa mã hóa mà LZ77 tìm cụm khớp. |
| $(0,0,c)$ | Literal LZ77, ghi trực tiếp ký tự $c$. |
| $(d,\ell,c)$ | Tham chiếu LZ77: khoảng lùi, độ dài sao chép và ký tự kế. |
| $EOS$ | Ký hiệu kết thúc dành riêng; không thuộc bảng chữ cái dữ liệu. |
| sao chép chồng lấn | Giải mã tuần tự cho phép ký tự vừa sinh trở thành nguồn. |
| $D[i]$ | Cụm được gán mã $i$ trong LZ78 hoặc LZW. |
| `next_code` | Mã kế tiếp chưa được cấp trong từ điển LZW. |
| DCT, IDCT | Biến đổi cosin rời rạc và biến đổi ngược. |
| $C_{u,v}$, $\tilde C_{u,v}$ | Hệ số DCT gốc và hệ số xấp xỉ sau giải lượng tử. |
| $Q_{u,v}$ | Bước lượng tử của hệ số $(u,v)$. |
| DC, AC | Hệ số một chiều và các hệ số còn lại của khối. |
| zigzag | Thứ tự quét AC từ tần số thấp đến cao. |
| $n,W,L,M$ | Độ dài chuỗi, kích thước cửa sổ, giới hạn cụm khớp và số mục từ điển. |

## Tài sản trực quan

Mười hai SVG trong `2627-1/img/lec-11/`. Ba tệp được chỉnh đáng kể sau rà soát:

- `lzw-trace.svg`: vết đầy đủ, gồm cả lần kéo dài, mã phát và mục từ 256–264;
- `jpeg-pipeline.svg`: phân biệt lấy mẫu sắc mất dữ liệu tùy chọn với lượng tử bắt buộc mất trong lõi;
- `dct-basis.svg`: ghi rõ đây là minh họa định tính, không phải giá trị hàm cơ sở DCT.

Chín SVG còn lại giữ vai trò ban đầu. Không có ảnh raster hoặc tài nguyên mạng trong HTML.
