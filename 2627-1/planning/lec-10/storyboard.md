# Storyboard Bài 10: Nén dữ liệu không mất thông tin

## Hành trình khái niệm

Dữ liệu lớn làm nổi bật ba chi phí khác nhau: gửi bảng tần suất, mã hóa một dòng chưa biết thống kê trước và lãng phí do từ mã phải dài nguyên bit. Bài học tách hai trục ngay từ đầu: mô hình có thể tĩnh hoặc cập nhật; bộ mã có thể dùng cây Huffman hoặc khoảng số học. Ba cụm lần lượt xét tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học. Mọi bộ giải mã phải tái tạo đúng mô hình, quy tắc mã và điều kiện kết thúc.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch"; yêu cầu người dùng 2026-10-14. Mỗi section ngoài trừ mạch mở đầu mở bằng một trang `class="strand-title"`, `id="mach-N"`. Mã theo quy ước của bài: mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch, nên trang tiêu đề mạch dùng `<tiền tố>T`. Trang tiêu đề mạch nằm ngoài chu trình khái niệm; thời lượng 0,5 phút mỗi trang lấy từ trang đầu mạch (cột "Trang đầu mạch"), tổng thời lượng bài không đổi. Deck 48 → 54 trang.

Bản đồ mạch (tên trùng từng chữ với trang Nội dung): 1. Mở đầu (mở bằng trang bìa P00); 2. Mã Huffman tĩnh (`HT`); 3. Huffman thích nghi (`AT`); 4. Mã hóa số học (`RT`); 5. Tổng kết và tự kiểm tra (`ST`); 6. Bài tập vận dụng (`XT`).

| Mã trang | Tiêu đề (tên mạch) | Mục đích | Vị trí | Kiến thức đầu vào | Đầu ra | Ghi chú | Phút | Quyết định |
|---|---|---|---|---|---|---|---:|---|
| P03 | Nội dung | Liệt kê đánh số mọi mạch, tên trùng trang tiêu đề mạch; notes một câu mỗi mạch | mạch mở đầu, sau P01 | Tên bài | Thứ tự và quan hệ các mạch | trang `agenda-slide` | 0,5 (từ trang bìa) | thêm |
| HT | Mã Huffman tĩnh | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 2, `id="mach-2"`, trước H00 | Mục tiêu, hai trục mô hình–bộ mã (P01–P02) | Cây Huffman, tính tối ưu, chi phí và đầu mục | ngoài chu trình khái niệm; tên khác tiêu đề H00 | 0,5 (từ H00) | thêm |
| AT | Huffman thích nghi | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 3, `id="mach-3"`, trước A00 | Huffman tĩnh cần bảng tần suất trước | Cập nhật cây đồng bộ, ba bất biến, ngưỡng dựng lại | ngoài chu trình khái niệm; tên khác tiêu đề A00 | 0,5 (từ A00) | thêm |
| RT | Mã hóa số học | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 4, `id="mach-4"`, trước R00 | Giới hạn từ mã nguyên bit | Mã khoảng, bất biến khoảng lồng nhau, cách dừng | ngoài chu trình khái niệm; tên khác tiêu đề R00 | 0,5 (từ R00) | thêm |
| ST | Tổng kết và tự kiểm tra | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 5, `id="mach-5"`, trước S00 | Ba cách mã đã có | Bốn mục giao thức, câu hỏi chọn cặp | ngoài chu trình khái niệm; tên khác tiêu đề S00 | 0,5 (từ S00) | thêm |
| XT | Bài tập vận dụng | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 6, `id="mach-6"`, trước X00 | Thuật toán của ba cách mã | Ba bài Nelson–Gailly và CMU | ngoài chu trình khái niệm; tên khác tiêu đề X00 | 0,5 (từ X01; X00 không có phút riêng nên X01 giảm 0,5 phút) | thêm |

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–6) ngay sau trang mục tiêu P01 (đứng ngay sau trang bìa), tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 24 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Bài có 6 section ngoài (trong khoảng 5–7), nên trang Nội dung đánh số 1–6. Mạch 5 đặt tên "Tổng kết và tự kiểm tra" theo `AGENTS.md`, vì phần S gồm bốn mục giao thức và câu hỏi chọn cặp.

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

> Các mục trang chiếu dưới đây (và các mục "Hành trình khái niệm", "Bổ sung trang tiêu đề mạch", "Bản đồ sáu mạch", "Chu trình học tập theo cụm", "Liên tục dữ kiện và ký hiệu", "Trạng thái phần recitation") thuộc deck cũ, giữ nguyên chờ làm lại deck; ánh xạ `data-slide-id` ↔ `note-topic-id` sẽ được lập khi làm lại.

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

## Storyboard ghi chú tự học (bản 2026-11-08)

Thay cho bảng `L10-N01…N10` cũ; ánh xạ mã cũ → mới ở `outline.md`, mục "Ghi chú bài giảng (bản 2026-11-08)". Ghi chú: `materials/lec-10/lecture-note.md`. Thứ tự mỗi chủ đề trọng tâm: nhu cầu có số → định nghĩa → ví dụ có lời giải → trực quan → kết quả → thuật toán (tính tay trước giả mã) → chứng minh → ứng dụng và kiểm tra.

| `note-topic-id` | Mục ghi chú | Vai trò; kết nối vào → ra | Kiến thức đầu vào | Sản phẩm học tập | Thành phần trình bày |
|---|---|---|---|---|---|
| `lec-10-topic-01` | Kiến thức tiên quyết | cầu nối; Bài 08–09, Bài 05 → mọi mục | — | dùng được các phát biểu lại | danh sách có số hiệu |
| `lec-10-topic-02` | 1.1 | mở bài từ Định lý 09.37 và bài toán khôi phục từng bit → đặc tả cho 1.2, 2.1 | 01 | đặc tả mã, Mệnh đề 10.2 | Ví dụ 10.1, Định nghĩa 10.1, Mệnh đề 10.2 có chứng minh, hình cấu trúc chương |
| `lec-10-topic-03` | 1.2 | tách mô hình–bộ mã → bốn thành phần giao thức dùng ở 3.2, 4.3, 6.3 | 02 | Định nghĩa 10.3, Nhận xét 10.4 | Ví dụ 10.2, Bài tập 10.1; chu trình rút gọn (không có định lý, thuật toán) |
| `lec-10-topic-04` | 2.1 | điều kiện giải mã kiểm được → cây mã cho 2.2, 3.2 | 02 | kiểm mã tiền tố, giải mã bằng cây | Định nghĩa 10.5, Ví dụ 10.3, Mệnh đề 10.6 có chứng minh; hình cây và khoảng mã |
| `lec-10-topic-05` | 2.2 | bộ độ dài khả thi → hai cận ở 2.4; Bổ đề 10.8 → Định lý 10.34 | 04 | tính tổng Kraft, dựng mã | Định nghĩa 10.7, Bổ đề 10.8, Ví dụ 10.4 (tính tay trước định lý), Định lý 10.9, Nhận xét 10.10, Bài tập 10.2 |
| `lec-10-topic-06` | 2.3 | thước đo đích → 2.4, 5.1 | 03 | tính $I$, $H$, $\bar\ell$ | Định nghĩa 10.11, Ví dụ 10.5; chu trình rút gọn (đại lượng đo) |
| `lec-10-topic-07` | 2.4 | cận hai phía → giới hạn 102 bit mở Mục 3 | 05, 06 | chứng minh $H\le\bar\ell<H+1$ | Định lý 10.12, 10.13 có chứng minh, Ví dụ 10.6, danh sách bỏ giả thiết, Trong thực hành, Bài tập 10.3 |
| `lec-10-topic-08` | 3.1 | phương pháp trước có số (89 bit) → nhu cầu dựng từ dưới lên | 05, 07 | so sánh 89 và 87 bit | Ví dụ 10.7; chu trình rút gọn theo Q3 (phương pháp trước làm giới hạn, nguồn không có kết quả về nó) |
| `lec-10-topic-09` | 3.2 | thuật toán → tối ưu ở 3.3, danh sách nút ở 4.1 | 04, 07, 08 | chạy Huffman, bảng mã | Ví dụ 10.8 (bảng hàng đợi trước giả mã), hình cây A–E, Thuật toán 10.14, giả mã, Bài tập 10.4 |
| `lec-10-topic-10` | 3.3 | tối ưu → Định lý 10.25, giới hạn nguyên bit mở Mục 5 | 05, 07, 09 | chứng minh tối ưu | Ví dụ 10.9, Bổ đề 10.15–10.17, Định lý 10.18, Hệ quả 10.19, Ví dụ 10.10, danh sách bỏ giả thiết |
| `lec-10-topic-11` | 3.4 | chi phí và đầu mục → nhu cầu thích nghi | 09 | đếm chi phí, đầu mục | Nhận xét 10.20 (bảng bước–số lần–chi phí–đóng góp), Trong thực hành; chu trình rút gọn (phân tích thuật toán đã có) |
| `lec-10-topic-12` | 4.1 | đặc trưng cây Huffman → cập nhật cục bộ | 09, 10 | kiểm tính chất anh em | Ví dụ 10.11, Định nghĩa 10.21, phản ví dụ Hình 4.8, Định lý 10.22 có chứng minh, quy ước bit, hình |
| `lec-10-topic-13` | 4.2 | thuật toán cập nhật → đồng bộ ở 4.3 | 12 | chạy tăng–đổi, chứng minh bất biến | Ví dụ 10.12, 10.13 (bốn lần tăng A trước giả mã), hình, Thuật toán 10.23, Bổ đề 10.24, Định lý 10.25, bảng chi phí, Trong thực hành |
| `lec-10-topic-14` | 4.3 | bộ nén một lượt → chống tràn ở 4.4; Tình huống 10.3(b) | 03, 13 | thêm ký hiệu mới, chứng minh đồng bộ | Ví dụ 10.14 (Hình 4.10), hình, Thuật toán 10.26, Mệnh đề 10.27 có chứng minh, Trong thực hành (khởi đầu nguội, Bài tập 10.16) |
| `lec-10-topic-15` | 4.4 | chặn trọng số → kết luận Mục 4, nối Mục 5 | 13, 14 | ngưỡng Fibonacci, dựng lại | Ví dụ 10.15, Nhận xét 10.28 (lời văn và mã của NG, Q15), Ví dụ 10.16 trước Thuật toán 10.29, Trong thực hành, Bài tập 10.5; Fibonacci chu trình rút gọn |
| `lec-10-topic-16` | 5.1–5.2 | khoảng của chuỗi → dừng và cận ở 5.3–5.4 | 06, 10 | mã hóa, giải mã với số thực | bảng khoảng BILL GATES (tính tay ba ký hiệu trước định nghĩa), Định nghĩa 10.30, Ví dụ 10.17, hình, Mệnh đề 10.31, Thuật toán 10.32, tính đúng, Ví dụ 10.18 |
| `lec-10-topic-17` | 5.3–5.4 | cận độ dài → nhu cầu thanh ghi hữu hạn | 05, 16 | chọn chuỗi bit, cận $<I(x)+2$ | Mệnh đề 10.33, Ví dụ 10.19, hình khoảng mã, Định lý 10.34, Hệ quả 10.35, Trong thực hành, Bài tập 10.6 |
| `lec-10-topic-18` | 6.1 | thanh ghi và phát tiền tố chung → 6.2 | 16, 17 | đọc vết thanh ghi | Định nghĩa 10.36, Ví dụ 10.20; gộp chu trình với topic-19 (hai nhánh của một vòng chuẩn hóa) |
| `lec-10-topic-19` | 6.2 | chuẩn hóa đúng → giải mã ở 6.3 | 18 | chạy ba trường hợp, chứng minh hai bổ đề | Thuật toán 10.37, giả mã, hình ba trường hợp, Ví dụ 10.21 (vết 16 bit cho cbb, có một lần khoảng giữa, dữ liệu của bản soạn), Bổ đề 10.38 (kéo ngược qua $\psi$), 10.39, danh sách bỏ giả thiết, Trong thực hành, Bài tập 10.7 |
| `lec-10-topic-20` | 6.3 | giải mã và kết thúc → Mục 7 | 19, 03 | giải mã nguyên | tính tay hai ký hiệu đầu của cbb trước Thuật toán 10.40, Mệnh đề 10.41 (phác thảo; đầy đủ ngoài phạm vi), bảng chi phí, Trong thực hành (các khoản cố định) |
| `lec-10-topic-21` | 7 | tổng hợp → tình huống | 09–20 | chọn cặp mô hình–bộ mã | bảng Thuật toán–Đầu vào–Bảo đảm–Chi phí, Bài tập 10.8; chu trình rút gọn (tổng hợp) |
| `lec-10-topic-22` | Tình huống | áp dụng ngược về lý thuyết | 02–21 | giải ba tình huống | Tình huống 10.1, 10.2, 10.3 (vi phạm giả thiết), danh mục ứng dụng |
| `lec-10-topic-23` | Tóm tắt | kể lại chuỗi kết quả → Bài 11 | mọi mục | — | đoạn 5–8 câu, kết quả theo mục, công thức, giả thiết hay quên |
| `lec-10-topic-24` | Bài tập | kiểm tra cuối | mọi mục | mười ba bài ba mức, trong tệp `materials/lec-10/exercises.md`; ghi chú giữ đoạn dẫn và liên kết | Bài tập 10.9–10.21 (10.16 thêm ký hiệu qua `ESCAPE`, 10.17 bit chờ với $R=8$, 10.18, 10.19 chứng minh cho mục tiêu 3, 4; 10.20 quy tắc trung điểm; 10.21 bảng mã dùng chung); recitation 10.11 (NG tr.32–37), 10.12 (CMU-A1 bài 4A), 10.14 (NG Hình 4.2–4.4), 10.15 (CMU-A1 bài 3) |
| `lec-10-topic-25` | Tham khảo | đọc thêm | — | — | danh mục có trang, quy ước trang PDF của NG, bảng nguồn của các chứng minh |

Các dữ kiện của bản soạn (Q12, Q19): dòng bit `0101100111` (Ví dụ 10.3); bộ độ dài $(1,1,2)$ (Ví dụ 10.4) và hai bộ đầu của Bài tập 10.2; vết 16 bit cho cbb (Ví dụ 10.21) và phép tính `count` ở Mục 6.3; giá trị `code` của Bài tập 10.7; quy tắc phá hòa, gán bit của Bài tập 10.11; phần (d) của Bài tập 10.14; thông điệp AB của Bài tập 10.16; thông điệp bc với $R=8$ của Bài tập 10.17; cây trọng số A1, B2, C2, D2 sau Định lý 10.22; tệp chỉ gồm Q và Z (Tình huống 10.3(a), Bài tập 10.21); bộ giải mã bỏ phép đổi (Tình huống 10.3(b)); xác suất $0{,}9$ cho điểm trắng ở Tình huống 10.2.
