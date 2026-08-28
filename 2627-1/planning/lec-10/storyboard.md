# Storyboard Bài 10: Nén dữ liệu không mất thông tin

## Hành trình khái niệm

Dữ liệu lớn làm nổi bật ba chi phí khác nhau: gửi bảng tần suất, mã hóa một dòng chưa biết thống kê trước và lãng phí do từ mã phải dài nguyên bit. Bài học tách hai trục ngay từ đầu: mô hình có thể tĩnh hoặc cập nhật; bộ mã có thể dùng cây Huffman hoặc khoảng số học. Ba cụm lần lượt xét tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học. Mọi bộ giải mã phải tái tạo đúng mô hình, quy tắc mã và điều kiện kết thúc.

## Ánh xạ từng trang

| Mã | Luận điểm và sản phẩm học tập | Bước trong chu trình, câu nối và nguồn | Phút |
|---|---|---|---:|
| P00 | Đặt tên và vị trí Bài 10. | Mở bài; `sources/source.md`, Bài 10 đề xuất. | 1 |
| P01 | Nêu bốn mục tiêu quan sát được. | Sản phẩm cuối buổi. | 2 |
| P02 | Tách trục mô hình tĩnh/cập nhật khỏi trục bộ mã Huffman/số học; giải thích lựa chọn Nelson–Gailly, Stanford và CMU. | Tiên quyết và truy nguyên nguồn; Nelson–Gailly Ch.2–5; CMU `compression1-2`; MMDS không có mô-đun tương ứng. | 6 |
| H00 | Kho văn bản lớn có phân phối lệch; hai lượt quét và bảng tần suất là chi phí thực. | Tình huống dữ liệu lớn; dữ liệu A–E được dùng lại ở H04–H13; Nelson–Gailly tr.32–37. | 3 |
| H01 | Đặc tả mã không mất thông tin với đầu vào, đầu ra và điều kiện giải mã duy nhất. | Vấn đề; nối sang điều kiện tiền tố. | 2 |
| H02 | Mã tiền tố cho phép đọc dòng bit từ trái sang phải. | Trực giác và hình thức; CMU/Stanford đối chiếu. | 3 |
| H03 | Kraft đo phần sức chứa mà mỗi lá mã chiếm; cây dừng đúng ở các lá 0, 10, 110, 111. | Trực giác hình học; SVG `prefix-tree-kraft` dùng tám ô ở độ sâu 3 thay vì vẽ nhánh dưới một lá; CMU Assignment 1a P4 chỉ làm nguồn đối chiếu, không dùng làm recitation. | 3 |
| H04 | Khởi tạo năm lá A–E với tần suất 15,7,6,6,5. | Ví dụ chạy tay; Nelson–Gailly tr.35. | 2 |
| H05 | Ghép D,E thành 11 rồi B,C thành 13. | Chạy tay; trạng thái truyền sang H06. | 3 |
| H06 | Ghép 11,13 thành 24 rồi A,24 thành 39. | Chạy tay; SVG `huffman-merge-a-e`; Nelson–Gailly tr.35–36. | 3 |
| H07 | Đọc mã A=0, B=100, C=101, D=110, E=111 từ cây. | Chạy tay sang hình thức; Nelson–Gailly tr.36. | 3 |
| H08 | Mã hóa và giải mã bằng đường gốc–lá. | Ứng dụng trực tiếp; SVG `huffman-code-decode`. | 2 |
| H09 | Giả mã hàng đợi ưu tiên, điều kiện dừng và quy tắc hòa. | Thuật toán; Stanford CS106B hỗ trợ cách kể, dữ liệu giữ theo sách. | 3 |
| H10 | Cây nhị phân đầy đủ tạo mã tiền tố và giải mã duy nhất. | Lập luận đúng; điều kiện dừng ở lá. | 2 |
| H11 | Chứng minh tồn tại cây tối ưu đặt hai ký hiệu nhẹ nhất ở một cặp lá anh em sâu nhất, rồi co cặp lá. | Tính tối ưu; nêu phép đổi với $\Delta\le0$ và phản chứng cho cấu trúc con tối ưu; CMU/Stanford đối chiếu. | 4 |
| H12 | Dựng cây $O(k\log k)$, mã hóa tuyến tính theo số bit đầu ra; phải truyền cây/bảng và quy ước trường hợp biên. | Chi phí, trường hợp biên và giới hạn; $k$ là số ký hiệu phân biệt; Nelson–Gailly tr.37, 67. | 4 |
| H13 | Người học chọn hai nút ghép tiếp và giải thích ảnh hưởng của hòa. | Kiểm tra; kết cụm Huffman tĩnh. | 1 |
| A00 | Dòng byte chỉ đi qua một lần và chưa có bảng tần suất. | Tình huống dữ liệu lớn; dùng lại chi phí bảng từ H12; Nelson–Gailly tr.67–68. Không tuyên bố thuật toán tự quên lịch sử hoặc bảo đảm bám drift. | 3 |
| A01 | Bộ nén và giải nén phải khởi tạo, mã hóa/giải mã, cập nhật cùng thứ tự. | Vấn đề; SVG `escape-eof-pipelines`. | 3 |
| A02 | Vết ký hiệu mới E: mã `ESCAPE`, tám bit `01000101`, chẻ nút nhẹ nhất để thêm E trọng số 0, rồi cập nhật E và tổ tiên; `EOS` kết thúc dòng. | Trực giác, ví dụ chạy tay và trường hợp biên; dữ kiện truyền nguyên sang A07–A08; Nelson–Gailly tr.76–81 và phần thêm nút mới. | 3 |
| A03 | Tính chất anh em đặc trưng cây Huffman. | Hình thức hóa; Nelson–Gailly tr.68–69; không dùng Hình 4.1. | 3 |
| A04 | Tăng lá A rồi tăng mọi tổ tiên. | Ví dụ chạy tay; SVG `adaptive-sibling-increment`; Hình 4.2, tr.70. | 3 |
| A05 | Tăng A từ 2 lên 3 phá thứ tự khi còn nút trọng số 2 ở phía sau. | Chạy tay, trạng thái trung gian sang A06; tr.70–71. | 2 |
| A06 | Đổi A với nút cuối có trọng số 2, rồi tiếp tục từ cha mới. | Chạy tay; SVG `adaptive-swap`; Hình 4.3, tr.71. | 3 |
| A07 | Giả mã tăng nút, dừng ngay tại gốc, đổi với nút hợp lệ cuối khối trọng số cũ, rồi lấy cha sau phép đổi. | Thuật toán; loại tổ tiên khỏi ứng viên đổi để phép đổi cây con an toàn. | 4 |
| A08 | Ba bất biến: hai phía có cùng cây; cây giữ tính chất anh em; nhánh mới bắt đầu ở trọng số 0 rồi được cập nhật ngay. | Lập luận đúng bằng quy nạp theo số ký hiệu, gồm riêng trường hợp ký hiệu chưa thấy. | 3 |
| A09 | Cập nhật đi theo chiều cao và cần chỉ mục khối; trọng số cộng dồn không tự quên lịch sử. | Chi phí và giới hạn; giảm trọng số hoặc cửa sổ quên là cơ chế khác, không tuyên bố cận hay bảo đảm drift ngoài nguồn. | 2 |
| A10 | Người học xác định nút đổi với A và cha tiếp theo. | Kiểm tra; kết cụm thích nghi. | 1 |
| R00 | Tệp 100.000 số 0 với $p(0)=16382/16383$ nén còn 3 byte bằng mã số học, so với tối thiểu 12.501 byte bằng Huffman. | Tình huống dữ liệu lớn có quy mô và kết quả từ Nelson–Gailly Ch.5, phần “Where’s the Beef?”; dùng lại ở R01, R12 và S01. | 3 |
| R01 | Huffman bị chặn bởi độ dài nguyên bit; mã số học mã cả thông điệp thành một khoảng. | Vấn đề; Nelson–Gailly tr.96, 104. | 2 |
| R02 | Phân hoạch $[0,1)$ bằng xác suất tích lũy. | Trực giác; khoảng nửa mở tránh hai ký hiệu cùng sở hữu biên; tr.97. | 3 |
| R03 | Bảng chín ký hiệu của “BILL GATES”. | Ví dụ chạy tay; Nelson–Gailly tr.97. | 2 |
| R04 | Sau B, I, L: $[0{,}2;0{,}3)$, $[0{,}25;0{,}26)$, $[0{,}256;0{,}258)$. | Chạy tay; SVG `arithmetic-bill-gates` vẽ đúng tỷ lệ trong từng mức phóng đại và chỉ đánh dấu vị trí khi khoảng cuối dưới độ phân giải; tr.98. | 3 |
| R05 | Công thức $L'=L+(H-L)C_s$, $H'=L+(H-L)D_s$. | Hình thức hóa; điều kiện $0\le C_s<D_s\le1$. | 3 |
| R06 | Bất biến khoảng chứa đúng các thông điệp có tiền tố đã đọc. | Lập luận đúng bằng quy nạp; khoảng lồng nhau. | 3 |
| R07 | Giải mã chọn khoảng chứa $x$ rồi chuẩn hóa $x'=(x-C_s)/(D_s-C_s)$. | Thuật toán và ví dụ; SVG `arithmetic-decode-normalize`; tr.99. | 3 |
| R08 | Phân biệt tự thông tin $I(x)=-\log_2p(x)$ với entropy trung bình $H(P)$ để giải thích độ dài của một chuỗi cụ thể. | Cầu nối hình thức sang CMU Assignment 1a Problem 3; Nelson–Gailly Ch.2. Erratum bảng A được chuyển khỏi mạch chính sang ghi chú và nhật ký. | 2 |
| R09 | Dừng bằng `EOS` hoặc độ dài truyền kèm; xác định quy ước trước khi giải mã. | Trường hợp biên; Nelson–Gailly tr.99. | 2 |
| R10 | Cài đặt hữu hạn giữ hai số nguyên và phát bit khi tiền tố đã cố định. | Cơ chế; Nelson–Gailly tr.100–102; Stanford EE398A đối chiếu. | 3 |
| R11 | Với khoảng nửa mở: E1 dùng $H\le1/2$, E2 dùng $L\ge1/2$, E3 dùng $1/4\le L&lt;H\le3/4$; mỗi trường hợp có phép biến đổi khoảng. | Thuật toán hữu hạn ở mức trực giác; SVG `arithmetic-renormalization`; Stanford `03-arithmetic-coding`; không trộn với quy ước cận trên đóng. | 4 |
| R12 | So sánh ba cặp tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học theo đầu mục, chi phí và giới hạn. | Chi phí, giới hạn, ứng dụng và lựa chọn; giữ hai trục của P02; không coi số thực vô hạn là cài đặt. | 2 |
| R13 | Người học tính khoảng sau B,I và nêu điều kiện dừng. | Kiểm tra; kết cụm số học. | 1 |
| S00 | Nêu bốn nhóm thông tin giao thức phải mang để giải mã đúng. | Tổng hợp xuyên ba cụm; dùng lại mô hình, cây/khoảng và cách dừng. | 4 |
| S01 | Gán ba tình huống đã học vào đúng cặp mô hình–bộ mã. | Kiểm tra cuối có đáp án xác định; dùng lại H00, A00 và R00; tổng phần giảng 120 phút. | 3 |
| X00 | Giao sản phẩm recitation và nêu ba nguồn nội dung. | Mở phần dọc; tổng thời lượng 60 phút theo ngoại lệ nguồn được người dùng phê duyệt ngày 2026-08-28. | 0 |
| X01 | Dựng Huffman A–E, bảng mã, tổng 87 bit; nộp chuỗi ghép và bảng mã. | Ví dụ Nelson–Gailly Ch.3, PDF tr.35–37, được chuyển thành bài luyện theo ngoại lệ đã phê duyệt. | 20 |
| X02 | Mô phỏng hai lần tăng A từ Hình 4.2 đến Hình 4.3; nộp thứ tự nút, phép đổi, cha tiếp theo. | Ví dụ Nelson–Gailly Ch.4, Hình 4.2–4.3, PDF tr.70–71, được chuyển thành bài luyện theo ngoại lệ đã phê duyệt. | 15 |
| X03 | Giải mã 01001110110 với $p(a)=0{,}1$, $p(b)=0{,}2$, $p(c)=0{,}7$ và giải thích độ dài. | CMU 15-499 Assignment 1a, Problem 3, tr.1; đáp án solution tr.2–3; được dùng theo ngoại lệ đã phê duyệt. | 25 |

## Liên tục dữ kiện và ký hiệu

- Dữ liệu A–E chỉ dùng cho Huffman tĩnh và bài X01; không trộn với bảng chín ký hiệu của “BILL GATES”.
- `ESCAPE` và `EOS` được giới thiệu ở A02. Vết E truyền `ESCAPE`, tám bit thô, lá E trọng số 0 và lời gọi cập nhật; không thay bằng tên nút từ biến thể khác.
- Phần số học dùng khoảng nửa mở $[L,H)$ từ R02 đến R13. Cặp $C_s,D_s$ luôn là cận tích lũy của ký hiệu trong $[0,1)$.
- Tự thông tin ở R08 được dùng trực tiếp để giải thích câu hỏi độ dài của X03; entropy chỉ là trung bình theo phân phối.
- Tình huống ở H00 được dùng lại trong chi phí bảng H12; tình huống A00 được dùng lại trong đồng bộ A08; tình huống R00 được dùng lại khi so sánh độ dài ở R12 và kiểm tra S01.

## Trạng thái phần recitation

X01–X03 có tổng thời lượng 60 phút và có lời giải trong ghi chú. Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28: X01–X02 là ví dụ Nelson–Gailly được chuyển thành bài luyện, còn X03 là CMU Assignment 1a, Problem 3. Lỗi chặn nguồn đã đóng; phần recitation không còn lỗi chặn hoặc nghiêm trọng.
