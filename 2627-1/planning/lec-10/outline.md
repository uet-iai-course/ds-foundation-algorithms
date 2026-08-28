# Bài 10: Nén dữ liệu không mất thông tin

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. đặc tả bài toán nén không mất thông tin, phân biệt trục mô hình tĩnh/cập nhật với trục bộ mã Huffman/số học;
2. dựng, dùng và giải thích tính tối ưu của mã Huffman tĩnh;
3. mô phỏng cập nhật Huffman thích nghi theo biến thể Nelson–Gailly dùng `ESCAPE`, `EOS` và tính chất anh em;
4. mã hóa, giải mã một thông điệp bằng khoảng nửa mở của mã hóa số học;
5. dùng tự thông tin và entropy để giải thích độ dài của một chuỗi cụ thể;
6. nêu điều kiện đồng bộ, kết thúc dòng, chi phí và giới hạn của ba cặp mô hình–bộ mã được học.

Phần giảng dài 120 phút. Phần bài tập dài 60 phút và nằm sau phần giảng trong cùng tệp HTML.

## Nguồn và quyết định chọn nguồn

| Cụm | Nguồn trục | Nguồn đối chiếu | Quyết định |
|---|---|---|---|
| Mã tiền tố và Huffman | Nelson–Gailly, Ch.3, PDF tr.31–37 | Stanford EE398A, *Entropy and Lossless Coding*; Stanford CS106B, *Huffman Coding*; CMU `compression1-2.pdf` | Giữ dữ liệu A–E và mã của sách; dùng Stanford cho nhịp trực quan cây và hàng đợi; dùng CMU cho Kraft. Viết lại chứng minh trao đổi với mệnh đề, phép đổi và cấu trúc con tối ưu. |
| Huffman thích nghi | Nelson–Gailly, Ch.4, PDF tr.67–71 và phần mã hóa ký hiệu mới | CMU `compression3.pdf` | Chỉ dùng biến thể trong sách: `ESCAPE`, `EOS`, tính chất anh em, đổi nút. Thêm vết ký hiệu mới gồm `ESCAPE`, tám bit thô, lá trọng số 0 và cập nhật. Không dùng tên NYT, FGK hay Vitter. Không dùng Hình 4.1 ở PDF tr.69 vì hình và lời mô tả lệch nhau; dùng Hình 4.2–4.3, tr.70–71. |
| Mã hóa số học | Nelson–Gailly, Ch.2 và Ch.5, PDF tr.96–104 | Stanford EE398A, *Arithmetic Coding*; CMU `compression1-2.pdf` | Giữ ví dụ “BILL GATES” và khoảng nửa mở của sách; dùng dữ kiện 100.000 số 0 cho tình huống lớn; dùng Stanford để trình bày E1/E2/E3 theo cùng quy ước nửa mở. Erratum bảng giải mã chỉ ghi trong ghi chú và nhật ký. |
| Bài tập | Nelson–Gailly, các ví dụ Ch.3–4; CMU Assignment 1a, Problem 3 | CMU solution | Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28: X01–X02 chuyển ví dụ Nelson–Gailly thành bài luyện; X03 dùng CMU Assignment 1a, Problem 3. |

MMDS không bao phủ mô-đun nén này, nên không có cụm tương đương để ưu tiên hoặc Việt hóa.

## Dàn ý và thời lượng

| Phần | Mã trang | Thời lượng |
|---|---|---:|
| Đặt bài toán và mô hình chung | P00–P02 | 9 phút |
| Mã tiền tố và Huffman tĩnh | H00–H13 | 38 phút |
| Huffman thích nghi | A00–A10 | 30 phút |
| Mã hóa số học | R00–R13 | 36 phút |
| Chọn bộ mã hóa và tổng hợp | S00–S01 | 7 phút |
| Bài tập recitation | X00–X03 | 60 phút |

Tổng phần giảng: 120 phút. Phần recitation đủ 60 phút theo ngoại lệ nguồn được người dùng phê duyệt ngày 2026-08-28; không còn lỗi chặn hoặc nghiêm trọng.

## Bản đồ chu trình học tập

| Cụm | Tình huống | Vấn đề | Trực giác | Chạy tay | Hình thức | Thuật toán và tính đúng | Chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| Huffman tĩnh | H00 | H01 | H02–H03 | H04–H08 | H02, H09 | H09–H11 | H12 | H13 |
| Huffman thích nghi | A00 | A01–A02 | A03 | A02, A04–A06 | A03, A07 | A07–A08 | A09 | A10 |
| Mã hóa số học | R00 | R01 | R02 | R03–R04, R07 | R05, R08 | R06, R09–R11 | R12 | R13 |

## Thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Cách dùng |
|---|---|
| mã tiền tố | Không từ mã nào là tiền tố của từ mã khác. |
| $f_s$, $p_s$ | Tần suất và xác suất của ký hiệu $s$. |
| $\ell_s$ | Độ dài từ mã của $s$. |
| $L,H$ | Cận dưới và cận trên của khoảng nửa mở $[L,H)$. |
| $C_s,D_s$ | Cận tích lũy dưới và trên của ký hiệu $s$. |
| $I(x)$ | Tự thông tin của một chuỗi cụ thể, bằng $-\log_2 p(x)$. |
| $H(P)$ | Entropy, tức tự thông tin trung bình theo phân phối $P$. |
| `ESCAPE` | Lá báo ký hiệu chưa có trong cây; theo sau bởi biểu diễn thô của ký hiệu. |
| `EOS` | Ký hiệu kết thúc dòng. |
| tính chất anh em | Có thể liệt kê nút theo trọng số không giảm sao cho hai nút anh em đứng kề nhau. |

## Tài sản trực quan

Tất cả hình được vẽ lại bằng SVG trong `2627-1/img/lec-10/`: cây tiền tố và tám miền Kraft; chuỗi ghép Huffman A–E; cây mã/giải mã; các mức phóng đại khoảng “BILL GATES”; chuẩn hóa giải mã; E1/E2/E3 theo khoảng nửa mở; tăng trọng số; đổi nút; hai đường ống `ESCAPE`/`EOS`.
