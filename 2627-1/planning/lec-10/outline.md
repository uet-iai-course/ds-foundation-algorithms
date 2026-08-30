# Bài 10: Nén dữ liệu không mất thông tin

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. đặc tả bài toán nén không mất thông tin, phân biệt trục mô hình tĩnh/cập nhật với trục bộ mã Huffman/số học;
2. dựng, dùng và giải thích tính tối ưu của mã Huffman tĩnh;
3. mô phỏng `ESCAPE`, `EOS` và phép đổi của Huffman thích nghi theo biến thể Nelson–Gailly; giải thích điều kiện và mục đích dựng lại khi đạt ngưỡng;
4. mã hóa, giải mã một thông điệp bằng khoảng nửa mở của mã hóa số học;
5. dùng tự thông tin và entropy để giải thích độ dài của một chuỗi cụ thể;
6. nêu điều kiện đồng bộ, kết thúc dòng, chi phí và giới hạn của ba cặp mô hình–bộ mã được học.

Phần giảng dài 120 phút. Phần bài tập dài 60 phút và nằm sau phần giảng trong cùng tệp HTML.

## Nguồn và quyết định chọn nguồn

| Cụm | Nguồn trục | Nguồn đối chiếu | Quyết định |
|---|---|---|---|
| Mã tiền tố và Huffman | Nelson–Gailly, Ch.3, PDF tr.31–37 | Stanford EE398A, *Entropy and Lossless Coding*; Stanford CS106B, *Huffman Coding*; CMU `compression1-2.pdf` | Giữ dữ liệu A–E và mã của sách; dùng Stanford cho nhịp trực quan cây và hàng đợi; dùng CMU cho Kraft. Viết lại chứng minh trao đổi với mệnh đề, phép đổi và cấu trúc con tối ưu. |
| Huffman thích nghi | Nelson–Gailly, Ch.4: tính chất và Hình 4.2–4.3 ở PDF tr.67–71; `ESCAPE` ở tr.73–74; cập nhật, chống tràn và dựng lại ở tr.75–85; lá mới trọng số 0 ở tr.82–83 | CMU `compression3.pdf` | Chỉ dùng biến thể trong sách: `ESCAPE`, `EOS`, tính chất anh em, đổi nút và dựng lại. Vết ký hiệu mới gồm `ESCAPE`, tám bit thô, lá trọng số 0 và cập nhật. Không dùng tên NYT, FGK hay Vitter. Không dùng Hình 4.1 vì hình và lời mô tả lệch nhau. |
| Mã hóa số học | Nelson–Gailly, Ch.2 và Ch.5, PDF tr.96–104 | Stanford EE398A, *Arithmetic Coding*, trang chiếu 10–12 và 16; CMU `compression1-2.pdf` | Giữ ví dụ “BILL GATES”, khoảng nửa mở, phát tiền tố chung và underflow theo sách. Dùng Stanford để đối chiếu số học hữu hạn và phép dịch; nhãn E1/E2/E3 là nhãn theo dõi của deck, không quy cho Stanford. Erratum bảng giải mã chỉ ghi trong ghi chú và nhật ký. |
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

## Chức năng của sáu mạch

| Mạch | Chức năng | Kết nối vào | Đầu ra cho mạch sau | Đóng góp vào mục tiêu |
|---|---|---|---|---|
| Đặt bài toán và mô hình chung | Tách mô hình xác suất khỏi bộ mã hóa, đặt yêu cầu khôi phục chính xác. | Kiến thức tiên quyết về xác suất, cây và hàng đợi ưu tiên. | Ma trận lựa chọn và tiêu chí giao thức. | Mục tiêu 1 và 6. |
| Mã tiền tố và Huffman tĩnh | Đi từ miền độ dài khả thi đến thuật toán tham lam và lập luận tối ưu. | Ma trận có ô tĩnh + Huffman. | Chi phí đếm trước và truyền cây làm động cơ cho cập nhật trực tuyến. | Mục tiêu 2. |
| Huffman thích nghi | Xây cây đồng bộ khi chưa biết thống kê, gồm ký hiệu mới, đổi nút và dựng lại. | Nhược điểm đầu mục của mô hình tĩnh. | Phân biệt chi phí mô hình với giới hạn độ dài nguyên bit. | Mục tiêu 3 và 6. |
| Mã hóa số học | Mã cả chuỗi bằng khoảng, thêm cách dừng và chuẩn hóa hữu hạn. | Giới hạn một từ mã nguyên bit cho mỗi ký hiệu. | Quan hệ độ rộng khoảng, tự thông tin và chi phí triển khai. | Mục tiêu 4 và 5. |
| Chọn bộ mã hóa và tổng hợp | Thu hồi hai trục và liệt kê thông tin giao thức cần để giải mã đúng. | Ba cặp đã phân tích. | Tiêu chí lựa chọn và yêu cầu giải trình cho bài tập. | Mục tiêu 1 và 6. |
| Bài tập recitation | Buộc sinh viên tạo cây, vết cập nhật và vết khoảng có thể chấm. | Thuật toán, bất biến và quy ước của năm mạch giảng. | Ba sản phẩm luyện tập kèm hướng dẫn chấm. | Kiểm tra toàn bộ sáu mục tiêu. |

## Bản đồ chu trình học tập

| Cụm | Tình huống | Vấn đề | Trực giác | Chạy tay | Hình thức | Thuật toán và tính đúng | Chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| Huffman tĩnh | H00 | H01 | H02–H03 | H04–H08 | H02, H09 | H09–H11 | H12 | H13 |
| Huffman thích nghi | A00 | A01–A02 | A03 | A02, A04–A06 | A03, A07 | A07–A08 | A09 | A10 |
| Mã hóa số học | R00 | R01 | R02 | R03–R04 | R05, R08 | R06–R07, R09–R11 | R12 | R13 |

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
