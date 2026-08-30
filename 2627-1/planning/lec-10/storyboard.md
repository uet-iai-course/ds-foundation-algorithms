# Storyboard Bài 10: Nén dữ liệu không mất thông tin

## Hành trình khái niệm

Dữ liệu lớn làm nổi bật ba chi phí khác nhau: gửi bảng tần suất, mã hóa một dòng chưa biết thống kê trước và lãng phí do từ mã phải dài nguyên bit. Bài học tách hai trục ngay từ đầu: mô hình có thể tĩnh hoặc cập nhật; bộ mã có thể dùng cây Huffman hoặc khoảng số học. Ba cụm lần lượt xét tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học. Mọi bộ giải mã phải tái tạo đúng mô hình, quy tắc mã và điều kiện kết thúc.

## Bản đồ sáu mạch

| Mạch | Chức năng | Kết nối vào | Đầu ra | Đóng góp mục tiêu |
|---|---|---|---|---|
| P — Đặt bài toán và mô hình chung | Nêu đích khôi phục chính xác và tách mô hình khỏi bộ mã. | Tiên quyết: xác suất, cây, hàng đợi ưu tiên. | Ma trận ba cặp lựa chọn được học. | Phân biệt hai trục và điều kiện giao thức. |
| H — Mã tiền tố và Huffman tĩnh | Dẫn từ Kraft đến cây tham lam, giải mã, tính đúng và tối ưu. | Ô tĩnh + Huffman trong ma trận. | Chi phí lượt đếm và đầu mục. | Dựng, giải mã và lập luận tối ưu Huffman. |
| A — Huffman thích nghi | Đồng bộ cây khi chưa có bảng trước, gồm ký hiệu mới, đổi nút và dựng lại. | Nhược điểm đầu mục của mô hình tĩnh. | Chi phí cập nhật mô hình và giới hạn tích lũy trọng số. | Mô phỏng biến thể Nelson–Gailly và các bất biến. |
| R — Mã hóa số học | Thu hẹp khoảng cho cả chuỗi, giải mã, dừng và chuẩn hóa hữu hạn. | Giới hạn độ dài nguyên bit của mã tiền tố. | Quan hệ độ rộng khoảng, số bit và chi phí. | Mã hóa, giải mã và dùng tự thông tin. |
| S — Chọn bộ mã hóa và tổng hợp | Thu hồi hai trục và thông tin giao thức. | Ba cụm thuật toán đã hoàn thành. | Tiêu chí lựa chọn có ràng buộc, không ép đáp án duy nhất. | So sánh chi phí, điều kiện đồng bộ và kết thúc. |
| X — Bài tập recitation | Tạo ba sản phẩm có thể chấm từ dữ kiện nguồn. | Cây A–E, cây thích nghi đầy đủ và mô hình CMU. | Vết ghép và bảng mã; vết đổi nút; bốn khoảng giải mã và giải thích tự thông tin. | Kiểm tra toàn bộ mục tiêu bài học. |

## Chu trình học tập theo cụm

| Cụm | Kiến thức đầu vào và sản phẩm | Tình huống, dữ liệu, giới hạn và đầu ra | Vai trò tám bước và dữ kiện truyền |
|---|---|---|---|
| Huffman tĩnh | Biết cây nhị phân và hàng đợi ưu tiên; tạo cây, bảng mã, vết giải mã, lập luận tối ưu và chi phí. | Kho văn bản có phân phối lệch; ví dụ A–E có 39 ký hiệu với tần suất 15,7,6,6,5; cần dòng bit khôi phục đúng, nhưng lượt đếm và đầu mục có chi phí. | Tình huống H00 → vấn đề H01 → trực giác H02–H03 → chạy tay H04–H08 → hình thức H02,H09 → thuật toán và tính đúng H09–H11 → chi phí H12 → kiểm tra H13. Các trọng số truyền từ bảng sang hàng đợi, cây, bảng mã và tổng 87 bit. |
| Huffman thích nghi | Biết cây Huffman và con trỏ cha; tạo vết ký hiệu mới, vết tăng/đổi, ba bất biến và quyết định dựng lại. | Dòng byte chỉ qua một lượt, chưa biết ký hiệu xuất hiện; hai phía phải tạo cùng dòng bit và cùng cây. Ký hiệu E mới truyền `ESCAPE`, `01000101`, lá E:0 rồi cập nhật. | Tình huống A00 → vấn đề A01–A02 → trực giác A03 → chạy tay A02,A04–A06 → hình thức A03,A07 → thuật toán và tính đúng A07–A08 → chi phí A09 → kiểm tra A10. Trạng thái cuối Hình 4.2 truyền sang đúng một lần tăng và phép đổi Hình 4.3. |
| Mã hóa số học | Biết xác suất và logarit; tạo vết khoảng, vết giải mã, vòng chuẩn hóa và giải thích số bit. | Nguồn 100.000 số 0 có $p(0)=16382/16383$ và $p(\mathrm{EOS})=1/16383$; mã tiền tố vẫn cần một bit mỗi ký hiệu, còn mã khoảng tạo tệp 3 byte theo nguồn. | Tình huống R00 → vấn đề R01 → trực giác R02 → chạy tay R03–R04,R07 → hình thức R05,R08 → thuật toán và tính đúng R06–R07,R09–R11 → chi phí R12 → kiểm tra R13. Khoảng BILL GATES truyền vào công thức, giải mã và điều kiện dừng; độ rộng khoảng truyền sang tự thông tin. |

Không có bước nào ghi `không áp dụng` cho ba thuật toán trọng tâm. Một số bước được gộp để giữ một luận điểm trung tâm trên mỗi trang; mã trang ở bảng trên ghi rõ các phần gộp.

## Ánh xạ từng trang

| Mã | Luận điểm và sản phẩm học tập | Bước trong chu trình, câu nối và nguồn | Phút |
|---|---|---|---:|
| P00 | Đặt tên và vị trí Bài 10. | Mở bài; `sources/source.md`, Bài 10 đề xuất. | 1 |
| P01 | Nêu bốn nhóm mục tiêu: hai trục và giao thức; Huffman tĩnh; mô phỏng `ESCAPE`/`EOS`/phép đổi và giải thích dựng lại; mã số học và tự thông tin. | Chuẩn đầu ra không yêu cầu mô phỏng toàn bộ thủ tục dựng lại; không hiển thị mã trang hay thời lượng. | 2 |
| P02 | Tách trục mô hình tĩnh/cập nhật khỏi trục bộ mã Huffman/số học; giải thích lựa chọn Nelson–Gailly, Stanford và CMU. | Tiên quyết và truy nguyên nguồn; Nelson–Gailly Ch.2–5; CMU `compression1-2`; MMDS không có mô-đun tương ứng. | 6 |
| H00 | Kho văn bản lớn có phân phối lệch; hai lượt quét và bảng tần suất là chi phí thực. | Tình huống dữ liệu lớn; dữ liệu A–E được dùng lại ở H04–H13; Nelson–Gailly tr.32–37. | 3 |
| H01 | Đặc tả mã không mất thông tin với đầu vào, đầu ra và điều kiện giải mã duy nhất. | Vấn đề; nối sang điều kiện tiền tố. | 2 |
| H02 | Mã tiền tố cho phép đọc dòng bit từ trái sang phải. | Trực giác và hình thức; CMU/Stanford đối chiếu. | 3 |
| H03 | Kraft vừa đo sức chứa cây vừa xác định miền độ dài khả thi trước khi tối ưu chi phí. | Trực giác nối sang bài toán tối ưu; SVG `prefix-tree-kraft` dùng tám ô ở độ sâu 3; CMU Assignment 1a P4 chỉ làm nguồn đối chiếu. | 3 |
| H04 | Khởi tạo năm lá A–E với tần suất 15,7,6,6,5. | Ví dụ chạy tay; Nelson–Gailly tr.35. | 2 |
| H05 | Ghép D,E thành 11 rồi B,C thành 13. | Chạy tay; trạng thái truyền sang H06. | 3 |
| H06 | Ghép 11,13 thành 24 rồi A,24 thành 39. | Chạy tay; SVG `huffman-merge-a-e`; Nelson–Gailly tr.35–36. | 3 |
| H07 | Đọc mã A=0, B=100, C=101, D=110, E=111 từ cây. | Chạy tay sang hình thức; Nelson–Gailly tr.36. | 3 |
| H08 | Mã hóa và giải mã bằng đường gốc–lá. | Ứng dụng trực tiếp; SVG `huffman-code-decode`. | 2 |
| H09 | Giả mã hàng đợi ưu tiên, điều kiện dừng và quy tắc hòa. | Thuật toán; Stanford CS106B hỗ trợ cách kể, dữ liệu giữ theo sách. | 3 |
| H10 | Cây nhị phân đầy đủ tạo mã tiền tố và giải mã duy nhất. | Lập luận đúng; điều kiện dừng ở lá. | 2 |
| H11 | Gọi $x,y$ là hai ký hiệu nhẹ nhất và $a,b$ là cặp lá anh em sâu nhất; hai phép đổi không tăng chi phí, rồi co cặp và quy nạp. | Tính tối ưu; deck triển khai lập luận từ các mệnh đề tối ưu trong Nelson–Gailly PDF tr.37 và Stanford *Entropy and Lossless Coding* trang chiếu 18, không quy lời giải đầy đủ cho nguồn. | 4 |
| H12 | Dựng cây $O(k\log k)$, mã hóa tuyến tính theo số bit đầu ra; phải truyền cây/bảng và quy ước trường hợp biên. | Chi phí, trường hợp biên và giới hạn; $k$ là số ký hiệu phân biệt; Nelson–Gailly tr.37, 67. | 4 |
| H13 | Người học chọn hai nút ghép tiếp và giải thích ảnh hưởng của hòa. | Kiểm tra; kết cụm Huffman tĩnh. | 1 |
| A00 | Dòng byte chỉ đi qua một lần và chưa có bảng tần suất. | Tình huống dữ liệu lớn; dùng lại chi phí bảng từ H12; Nelson–Gailly tr.67–68. Không tuyên bố thuật toán tự quên lịch sử hoặc bảo đảm bám drift. | 3 |
| A01 | Bộ nén và giải nén phải khởi tạo, mã hóa/giải mã, cập nhật cùng thứ tự. | Vấn đề; SVG `escape-eof-pipelines`. | 3 |
| A02 | Vết ký hiệu mới E: mã `ESCAPE`, tám bit `01000101`, chẻ nút nhẹ nhất để thêm E trọng số 0, rồi cập nhật E và tổ tiên; `EOS` kết thúc dòng. | Trực giác, ví dụ chạy tay và trường hợp biên; `ESCAPE` ở Nelson–Gailly PDF tr.73–74, lá mới trọng số 0 ở tr.82–83; dữ kiện truyền sang giả mã và bất biến. | 3 |
| A03 | Tính chất anh em đặc trưng cây Huffman. | Hình thức hóa; Nelson–Gailly tr.68–69; không dùng Hình 4.1. | 3 |
| A04 | Trên toàn cây Hình 4.2, tăng A $1\to2$, nút số 5 $3\to4$, nút số 7 $7\to8$ và gốc $17\to18$; nút số 6 và E giữ nguyên. | Ví dụ chạy tay; SVG `adaptive-sibling-increment`; Nelson–Gailly PDF tr.70. Trạng thái cuối truyền nguyên sang lần tăng kế tiếp. | 3 |
| A05 | Từ trạng thái cuối vừa có, thực hiện thêm một lần tăng A từ 2 lên 3 và phát hiện A vượt khối trọng số 2. | Trạng thái trung gian nối trực tiếp sang phép đổi; Nelson–Gailly PDF tr.70–71. | 2 |
| A06 | Đổi A với D; toàn cây Hình 4.3 giữ tổ tiên ở trọng số cũ vì mới chỉ A đã tăng, rồi tiếp tục từ cha mới số 6. | SVG `adaptive-swap`; Nelson–Gailly PDF tr.71. Hình phân biệt thời điểm sau đổi với thời điểm cập nhật xong cả đường. | 3 |
| A07 | Trước cập nhật, kiểm tra ngưỡng; nếu đạt thì thay mỗi trọng số lá bằng $(w+1)//2$ và dựng lại. Sau đó tăng, đổi an toàn và dừng tại gốc. | Thuật toán; cập nhật, chống tràn và dựng lại theo Nelson–Gailly PDF tr.75–85; loại tổ tiên khỏi ứng viên đổi. | 4 |
| A08 | Ba bất biến: hai phía có cùng cây; cây giữ tính chất anh em; nhánh mới bắt đầu ở trọng số 0 rồi được cập nhật ngay. | Quy nạp gồm ký hiệu đã biết, ký hiệu mới và nhánh dựng lại: cùng ngưỡng, phép làm tròn, quy tắc phá hòa và thủ tục tái dựng cho cùng cây. | 3 |
| A09 | Tách chi phí đường cập nhật khỏi chi phí dựng lại; dựng lại phục vụ chống tràn, còn chiết giảm lịch sử chỉ là tác dụng kèm theo. | Chi phí và giới hạn; không suy ra bảo đảm bám phân phối trôi. Nelson–Gailly PDF tr.75–85. | 2 |
| A10 | Người học xác định nút đổi với A và cha tiếp theo. | Kiểm tra; kết cụm thích nghi. | 1 |
| R00 | Tệp 100.000 số 0 với $p(0)=16382/16383$ nén còn 3 byte bằng mã số học, so với tối thiểu 12.501 byte bằng Huffman. | Tình huống dữ liệu lớn có quy mô và kết quả từ Nelson–Gailly Ch.5, phần “Where’s the Beef?”; dùng lại ở R01, R12 và S01. | 3 |
| R01 | Huffman bị chặn bởi độ dài nguyên bit; mã số học mã cả thông điệp thành một khoảng. | Vấn đề; Nelson–Gailly tr.96, 104. | 2 |
| R02 | Phân hoạch $[0,1)$ bằng xác suất tích lũy. | Trực giác; khoảng nửa mở tránh hai ký hiệu cùng sở hữu biên; tr.97. | 3 |
| R03 | Bảng chín ký hiệu của “BILL GATES”. | Ví dụ chạy tay; Nelson–Gailly tr.97. | 2 |
| R04 | Sau B, I, L: $[0{,}2;0{,}3)$, $[0{,}25;0{,}26)$, $[0{,}256;0{,}258)$. | Chạy tay; SVG `arithmetic-bill-gates` vẽ đúng tỷ lệ trong từng mức phóng đại và chỉ đánh dấu vị trí khi khoảng cuối dưới độ phân giải; tr.98. | 3 |
| R05 | Công thức $L'=L+(H-L)C_s$, $H'=L+(H-L)D_s$. | Hình thức hóa; điều kiện $0\le C_s<D_s\le1$. | 3 |
| R06 | Bất biến khoảng chứa đúng các thông điệp có tiền tố đã đọc. | Lập luận đúng bằng quy nạp; khoảng lồng nhau. | 3 |
| R07 | Giải mã chọn khoảng chứa $x$ rồi chuẩn hóa $x'=(x-C_s)/(D_s-C_s)$. | Thuật toán và ví dụ; SVG `arithmetic-decode-normalize`; Nelson–Gailly PDF tr.99. Câu nối: giải mã còn cần quy tắc dừng. | 3 |
| R09 | Dừng bằng `EOS` hoặc độ dài truyền kèm; hoàn tất bằng tiền tố chọn một điểm trong khoảng cuối và đệm theo định dạng chung. | Trường hợp biên; Nelson–Gailly PDF tr.99. Hai phía chia sẻ quy tắc kết thúc, xử lý bit chờ, bit bù và đệm; sau giao thức lý tưởng là cài đặt hữu hạn. | 2 |
| R10 | Cài đặt hữu hạn giữ hai số nguyên, phát bit khi tiền tố cố định và phản chiếu phép dịch ở bộ giải nén. | Cơ chế; Nelson–Gailly PDF tr.100–103; Stanford *Arithmetic Coding* trang chiếu 10–12 và 16 đối chiếu số học hữu hạn. | 3 |
| R11 | Khởi tạo `pending` một lần trước thông điệp; vòng lặp có thứ tự E1, E2, E3 giữ bộ đếm xuyên các ký hiệu và dừng chuẩn hóa khi cả ba điều kiện sai. | Thuật toán hữu hạn; các dòng đặt lại `pending` được tách chủ ý để không tạo dòng mồ côi, lưới trái rộng hơn để tránh tràn. Ghi chú nối đến bước hoàn tất sau EOS/độ dài. Nguồn tiền tố chung/underflow là Nelson–Gailly tr.100–103; Stanford trang chiếu 10–12 và 16 đối chiếu phép dịch. | 4 |
| R08 | Độ rộng khoảng bằng xác suất chuỗi, nên số bit gắn với $I(x)=-\log_2P(x)$; chỉ nguồn không nhớ mới tách thành tổng theo ký hiệu. | Cầu nối từ chuẩn hóa hữu hạn sang chi phí và bài CMU; Nelson–Gailly Ch.2. Erratum bảng A chỉ nằm trong ghi chú và nhật ký. | 2 |
| R12 | So sánh bộ nhớ $O(k)$, đường cao $h$, tra cứu, dựng lại và điều kiện giao thức mà không áp cận thời gian thiếu nguồn. | Chi phí và giới hạn; giữ hai trục mở bài. Câu nối: kiểm tra khoảng và điều kiện dừng. | 2 |
| R13 | Người học tính khoảng sau B,I và nêu điều kiện dừng. | Kiểm tra; kết cụm số học. | 1 |
| S00 | Nêu bốn nhóm thông tin giao thức phải mang để giải mã đúng. | Tổng hợp xuyên ba cụm; dùng lại mô hình, cây/khoảng và cách dừng. | 4 |
| S01 | Chọn một cặp phù hợp cho từng tình huống dưới ràng buộc được đánh dấu, giải thích đánh đổi và nêu thông tin giao thức. | Kiểm tra cuối không ép đáp án duy nhất; thu hồi hai trục mở bài và bốn nhóm thông tin tổng hợp. Tổng phần giảng 120 phút. | 3 |
| X00 | Giao sản phẩm recitation và nêu ba nguồn nội dung. | Mở phần dọc; tổng thời lượng 60 phút theo ngoại lệ nguồn được người dùng phê duyệt ngày 2026-08-28. | 0 |
| X01 | Nộp đủ bốn lượt ghép, cây có nhãn nhánh, bảng mã năm ký hiệu, phép tính tổng 87 bit và nhận xét phá hòa. | Ví dụ Nelson–Gailly Ch.3, PDF tr.35–37, được chuyển thành bài luyện theo ngoại lệ đã phê duyệt. | 20 |
| X02 | Dùng giá trị sau mũi tên làm trạng thái đầu: A=B=C=D=2, số 5=số 6=4, số 7=8, số 9=18; tăng A đúng một lần, đổi với D và tiếp tục từ cha số 6. | Ví dụ Nelson–Gailly Ch.4, Hình 4.2–4.3, PDF tr.70–71. Ảnh được gọi đúng là sơ đồ chuyển tiếp, không phải trạng thái tĩnh; bài tự chứa đủ topology và giá trị đầu. | 15 |
| X03 | Giải mã $0{,}01001110110_2$ thành caba; nộp giá trị thập phân, bốn khoảng toàn cục, tự thông tin xấp xỉ 9,48 bit và nhận xét về kết thúc/đệm. | CMU 15-499 Assignment 1a, Problem 3, tr.1; đáp án tr.2–3. Dòng 11 bit là biểu diễn nguồn cung cấp, không tuyên bố tối thiểu. | 25 |

## Liên tục dữ kiện và ký hiệu

- Dữ liệu A–E chỉ dùng cho Huffman tĩnh và bài X01; không trộn với bảng chín ký hiệu của “BILL GATES”.
- `ESCAPE` và `EOS` được giới thiệu ở A02. Vết E truyền `ESCAPE`, tám bit thô, lá E trọng số 0 và lời gọi cập nhật; không thay bằng tên nút từ biến thể khác.
- Phần số học dùng khoảng nửa mở $[L,H)$ từ R02 đến R13. Cặp $C_s,D_s$ luôn là cận tích lũy của ký hiệu trong $[0,1)$.
- Tự thông tin ở R08 được dùng trực tiếp để giải thích câu hỏi độ dài của X03; entropy chỉ là trung bình theo phân phối.
- Tình huống ở H00 được dùng lại trong chi phí bảng H12; tình huống A00 được dùng lại trong đồng bộ A08; tình huống R00 được dùng lại khi so sánh độ dài ở R12 và kiểm tra S01.

## Trạng thái phần recitation

X01–X03 có tổng thời lượng 60 phút và có lời giải trong ghi chú. Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28: X01–X02 là ví dụ Nelson–Gailly được chuyển thành bài luyện, còn X03 là CMU Assignment 1a, Problem 3. Lỗi chặn nguồn đã đóng; phần recitation không còn lỗi chặn hoặc nghiêm trọng.
