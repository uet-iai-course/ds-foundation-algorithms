# Nhật ký rà soát Bài 10

## Trạng thái lượt sửa hiện tại

- Giữ 48 trang: 44 trang phần giảng và 4 trang recitation.
- Giữ 6 mạch ngoài, gồm mở bài, ba cụm thuật toán, tổng hợp và recitation.
- Phần giảng được phân bổ 120 phút; ba bài recitation được phân bổ $20+15+25=60$ phút. Thời lượng chỉ ghi trong planning, không xuất hiện trên mặt trang hoặc ghi chú diễn giả.
- Giữ 9 SVG cục bộ; không thêm ảnh raster hay phụ thuộc mạng.
- `2627-1/index.html` đã có thẻ và liên kết đúng cho Bài 10. Lượt sửa này không thay đổi tệp chỉ mục.
- Chưa ghi nhận kiểm định trình duyệt hoặc Codex Slides cuối ở đây. Điều phối viên sẽ bổ sung kết quả sau khi bản sửa vượt kiểm tra tĩnh và trực quan.

## Phân tích nguồn hiện tại

| Cụm | Nguồn đã đối chiếu | Kết luận |
|---|---|---|
| Mã tiền tố và Huffman tĩnh | Nelson–Gailly Chương 3, PDF tr.31–37; Stanford EE398A *Entropy and Lossless Coding*, trang chiếu 18; CMU Assignment 1a | Giữ dữ liệu A–E, bốn lượt ghép và tổng 87 bit của sách. Kraft chỉ xác định miền độ dài khả thi. Lập luận tối ưu trên trang chiếu là phần triển khai phép đổi và quy nạp từ mệnh đề nguồn, không được mô tả như một chứng minh chép nguyên từ nguồn. |
| Huffman thích nghi | Nelson–Gailly Chương 4: Hình 4.2–4.3 ở PDF tr.70–71; `ESCAPE` ở tr.73–74; cập nhật, chống tràn và dựng lại ở tr.75–85; lá mới trọng số 0 ở tr.82–83 | Giữ đúng biến thể Nelson–Gailly, không gắn tên NYT, FGK hay Vitter. Hình 4.2 được vẽ đủ nhánh E và số nút. Hình 4.3 được vẽ đúng thời điểm chỉ A đã tăng: các tổ tiên còn mang trọng số cũ, và bước kế tiếp là nút số 6. |
| Mã hóa số học | Nelson–Gailly Chương 2 và Chương 5, PDF tr.96–104; Stanford EE398A *Arithmetic Coding*, trang chiếu 10–12 và 16; CMU Assignment 1a Problem 3 và đáp án | Nelson–Gailly là nguồn cho “BILL GATES”, tiền tố chung, underflow và ví dụ 100.000 số 0. Stanford chỉ đối chiếu số học hữu hạn và phép dịch; deck không quy tên E1/E2/E3 cho Stanford. Bài CMU cung cấp dòng bit, mô hình và chuỗi caba. |

MMDS không có mô-đun tương ứng cho bài này. Không bổ sung mệnh đề ngoài các nguồn trên.

## Sai khác có chủ ý và ngoại lệ nguồn

- Không dùng Hình 4.1 ở Nelson–Gailly PDF tr.69 vì hình và lời mô tả trọng số không khớp. Dùng Hình 4.2–4.3 và ghi rõ thời điểm của từng hình.
- Bảng giải mã ở Nelson–Gailly PDF tr.99 in nhầm khoảng A thành khoảng của B. Deck dùng bảng mô hình đúng ở tr.97: A thuộc $[0{,}1;0{,}2)$.
- X01 và X02 chuyển ví dụ trong sách thành bài luyện; X03 dùng CMU Assignment 1a Problem 3. Người dùng đã phê duyệt ngoại lệ nguồn cho ba bài ngày 2026-08-28.
- X03 giữ nguyên biểu diễn 11 bit của nguồn. Deck không tuyên bố đây là biểu diễn ngắn nhất và nêu rõ quy tắc kết thúc hoặc đệm thuộc định dạng.

## Kiểm định storyboard hiện tại

Tác tử kiểm định storyboard rà đủ 48 trang và sáu mạch. Các quyết định chính:

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | A04–A06, X02 | Hai SVG cũ bỏ nhánh E và topology đầy đủ; bài tập không tự chứa đủ dữ kiện để suy ra cha mới. | Hình 4.2–4.3 của nguồn có chín nút, E trọng số 10 và số nút; Hình 4.3 chụp trước khi tăng tổ tiên. | Vẽ lại toàn cây và nhúng cây ban đầu vào bài tập. | Đã áp dụng; X02 yêu cầu đúng một lần tăng $2\to3$. |
| nghiêm trọng | R07–R12 | Tự thông tin đứng trước giao thức dừng và chuẩn hóa hữu hạn, làm đứt cầu nối từ khoảng đến số bit. | Mạch cũ chuyển từ giải mã sang tự thông tin rồi quay lại dừng và cài đặt. | Đổi thứ tự thành giải mã → dừng → hữu hạn → vòng chuẩn hóa → tự thông tin → chi phí. | Đã áp dụng, giữ nguyên mã trang. |
| nghiêm trọng | R11 | Hình ba trường hợp không đủ để thực thi thuật toán; thiếu thứ tự loại trừ và bộ đếm bit chờ. | E1, E2, E3 không độc lập và hành động phát bit khác nhau. | Đưa vòng lặp có thứ tự lên mặt trang, nêu bit chờ và giải mã phản chiếu. | Đã áp dụng. |
| trung bình | H11 | Lập luận tối ưu quá nén trên một trang. | Bốn ý phép đổi, co cặp và quy nạp tranh chỗ. | Tách thành hai trang. | Không tách để giữ 48 trang và nhịp nguồn; đã giảm chữ, đặt tên $x,y,a,b$ và dùng bốn bước ngắn trên cùng trang. |
| trung bình | A07–A09 | Cần phân biệt dựng lại chống tràn với cơ chế quên. | Sách mô tả dựng lại khi đạt ngưỡng và quan sát tác dụng chiết giảm lịch sử, không đưa bảo đảm bám drift. | Thêm một trang riêng về rescale. | Không thêm trang; tích hợp tiền kiểm tra vào giả mã và tách mục tiêu/chi phí ở trang kế cận. |

Sau thay đổi thứ tự phần số học, storyboard đã rà lại hai trang lân cận ở mỗi biên liên quan. Sáu mạch vẫn có chức năng, kết nối vào, đầu ra và đóng góp mục tiêu riêng. Tổng thời lượng không đổi.

## Năm báo cáo rà soát độc lập

Mỗi vai dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`. Các lỗi chặn bàn giao và nghiêm trọng dưới đây đã được xử lý trong bản hiện tại.

### 1. Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | A04–A06, X02 | Không thể theo dõi phép đổi nếu chỉ thấy bốn ô lá, và bài tập phải nhớ topology từ phần giảng. | Cha mới số 6 phụ thuộc toàn cây Hình 4.2. | Vẽ đủ cây, giữ trạng thái trung gian và nhúng cây vào bài tập. | Đã áp dụng. |
| trung bình | toàn bài | `.tiny` có kích thước thực dưới ngưỡng đọc trên máy chiếu. | `.tiny=.72em` nhân với section `.84em`. | Đưa `.small` và `.tiny` lên ít nhất `.9em`. | Đã áp dụng; mã và bảng không bị hạ cỡ. |
| trung bình | S01 | Câu hỏi cũ ngụ ý mỗi tình huống có một đáp án duy nhất. | Nhiều bộ mã có thể phù hợp tùy đầu mục và cài đặt. | Đánh dấu ràng buộc, yêu cầu chọn một cặp phù hợp và giải thích. | Đã áp dụng; thêm yêu cầu nêu thông tin giao thức. |

### 2. Chuyên gia giải thuật và khoa học dữ liệu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | P01, A07, A09 | Mục tiêu có cập nhật thích nghi nhưng thiếu chống tràn và dựng lại của biến thể nguồn. | Nelson–Gailly PDF tr.75–85 có kiểm tra ngưỡng, giảm trọng số lá và dựng lại. | Bổ sung vào mục tiêu, giả mã và phần chi phí. | Đã áp dụng. |
| nghiêm trọng | R12 | Bảng chi phí cũ quá chung và dễ bị đọc như cận thời gian. | Tra cứu khối, tìm khoảng và dựng lại phụ thuộc cài đặt. | Chỉ nêu bộ nhớ $O(k)$, đường cao $h$ và thao tác cụ thể; giữ caveat. | Đã áp dụng. |
| trung bình | P02 | Có thể thêm ô mô hình cập nhật + mã số học để đủ ma trận. | Cặp này có thật nhưng nằm ngoài phạm vi nguồn bài. | Thêm một cụm hoặc ví dụ. | Không áp dụng; ô vẫn ghi ngoài phạm vi để tránh mở rộng nội dung. |

### 3. Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | H11 | Phép đổi cũ không đặt tên rõ hai ký hiệu nhẹ nhất và hai lá anh em sâu nhất. | Một công thức $\Delta$ dùng chỉ số mơ hồ không đủ theo dõi hai phép đổi. | Đặt $x,y,a,b$, nêu từng phép đổi không tăng chi phí, co cặp và quy nạp. | Đã áp dụng; nguồn được ghi như mệnh đề tối ưu, không như chứng minh đầy đủ. |
| nghiêm trọng | R08 | Công thức tích $\prod_i p(x_i)$ được viết không điều kiện cho mọi nguồn. | Công thức chỉ tách được như vậy dưới mô hình không nhớ hoặc độc lập. | Dùng $-\log_2P(x_1\ldots x_n)$ làm công thức chính và nêu điều kiện để tách tổng. | Đã áp dụng. |
| nghiêm trọng | R11 | Thiếu hành động phát các bit chờ; E3 có thể bị hiểu là phát bit ngay. | Underflow cần hoãn quyết định và đảo các bit chờ khi E1/E2 chốt phía. | Thêm `pending`, thứ tự nhánh và hành động phát. | Đã áp dụng; ghi rõ bộ giải nén phản chiếu. |
| trung bình | X03 | Dễ suy ra 11 bit là mã tối thiểu từ tự thông tin xấp xỉ 9,48. | Đề nguồn chỉ cung cấp một biểu diễn có độ dài 11. | Nêu đây không nhất thiết là biểu diễn ngắn nhất và định dạng kết thúc/đệm có chi phí. | Đã áp dụng. |

### 4. Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | H03–H11 | Kraft xuất hiện như kết quả rời, chưa nối sang bài toán tối ưu độ dài. | Trang kế tiếp chuyển thẳng sang dữ liệu A–E. | Nêu Kraft là miền khả thi và Huffman tối ưu chi phí trong miền đó. | Đã áp dụng trên cùng trang để giữ nhịp. |
| nghiêm trọng | R07–R12 | Công thức tự thông tin đúng riêng lẻ nhưng đặt trước cơ chế dừng và hữu hạn. | Sinh viên chưa thấy dòng bit được chốt như thế nào. | Đặt tự thông tin sau vòng chuẩn hóa và trước bảng chi phí. | Đã áp dụng. |
| trung bình | X01 | Sản phẩm “tổng số bit” chưa nói rõ phải mã hóa đủ 39 ký hiệu theo tần suất. | Có thể chỉ ghi con số 87 mà thiếu phép tính. | Yêu cầu bảng mã và đủ năm hạng đóng góp. | Đã áp dụng. |

### 5. Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | R07–R12 | Vai trò trong mạch: giải mã lý tưởng; kết nối vào: bất biến khoảng; kết nối ra cũ: nhảy sang entropy rồi quay lại cài đặt. | Tuyến lập luận đổi tầng trừu tượng hai lần. | Đi theo giải mã → dừng → hữu hạn → chuẩn hóa → số bit → chi phí. | Đã áp dụng và rà lại toàn ranh giới cụm số học. |
| trung bình | S01 | Vai trò trong mạch: kiểm tra tổng hợp; kết nối vào: danh sách giao thức; kết nối ra: recitation. Câu cũ chỉ gán nhãn, chưa thu hồi giao thức. | Người học có thể chọn cặp mà không nêu dữ liệu hai phía phải chia sẻ. | Thêm yêu cầu giao thức và giải thích đánh đổi. | Đã áp dụng. |
| nhẹ | P01 | Bốn mục tiêu chưa thu hồi đầy đủ hai trục mở bài và tự thông tin. | Mục tiêu cũ chỉ liệt kê ba thuật toán. | Viết lại bốn gạch bao phủ mô hình–bộ mã, giao thức và tự thông tin. | Đã áp dụng. |

## Quyết định chỉnh sửa

- Writer duy nhất sửa tuần tự HTML, ba SVG liên quan và ba tệp planning; không sửa CSS dùng chung, template hoặc index.
- Thứ tự trang thay đổi duy nhất là chuyển R08 ra sau R11. Không thêm, xóa, gộp hoặc tách trang.
- Ghi chú diễn giả đã bỏ mã trang nội bộ và thời lượng. Mặt trang không hiển thị thời lượng hay nhãn quy trình.
- Áp dụng `no-ai-slop` cho nội dung hiển thị và ghi chú: cắt lời dẫn rỗng, câu tổng kết lặp và khẳng định tuyệt đối thiếu nguồn; giữ thuật ngữ nhất quán.
- Dùng Quill ở mức khái niệm để rà thứ tự, cầu nối, thuật ngữ và ký hiệu. Không tạo `quill.json`.

## Rà lại cục bộ sau kiểm định trực quan

| Mức độ | Trang chiếu | Phát hiện | Sửa và trạng thái |
|---|---|---|---|
| nghiêm trọng | X02 | SVG Hình 4.2 chứa cả giá trị trước và sau mũi tên, nhưng lời bài gọi nó như một trạng thái tĩnh. | Mặt trang nay chỉ rõ lấy giá trị sau mũi tên: A=B=C=D=2, số 5=số 6=4, số 7=8, số 9=18. Alt và ghi chú gọi đúng đây là sơ đồ chuyển tiếp. Đã đóng. |
| trung bình | P01, A08 | Chuẩn đầu ra cũ có thể bị hiểu là sinh viên phải mô phỏng toàn bộ dựng lại; bất biến đồng bộ chưa xét nhánh rebuild. | Hạ mục tiêu xuống mô phỏng `ESCAPE`/`EOS`/phép đổi và giải thích điều kiện, mục đích dựng lại. Ghi chú bổ sung cùng ngưỡng, phép làm tròn, phá hòa và tái dựng. Đã đóng. |
| nghiêm trọng | R09, R11 | `pending` chưa được nói rõ là trạng thái xuyên ký hiệu; thiếu bước hoàn tất sau EOS hoặc độ dài đã biết. | Ghi rõ khởi tạo một lần, giữ xuyên ký hiệu; bổ sung tiền tố chọn điểm trong khoảng cuối, bit bù, đệm và quy tắc chung ở bộ giải nén. Đã đóng. |
| nghiêm trọng | R11 | Khối mã bị cắt ở khung 1280 × 720; sau lần rút đầu, hai phép gán `pending ← 0` vẫn tự bẻ số 0 thành dòng riêng. | Dùng lưới cục bộ 1,15:0,85, bỏ chú thích dài và tách chủ ý dòng biến đổi khỏi dòng đặt lại `pending`; số dòng render không tăng so với bản bị wrap. Giữ cỡ `.code=.9em`, tương đương 0,756em thực. Đã đóng và xác nhận trực quan `PASS` ở QA3. |
| trung bình | S01 | Câu dẫn vẫn bẻ “lựa chọn:” thành một dòng mồ côi. | Rút thành “Chọn cặp (mô hình, bộ mã) và giải thích theo ràng buộc:”. Đã đóng và xác nhận trực quan `PASS` ở QA3. |

Các sửa trên không đổi số trang, mã trang, thứ tự hoặc sáu mạch ngoài. Kết quả kiểm định RevealJS cục bộ và giới hạn Codex Slides được ghi ngay dưới đây.

## Kiểm định cuối của điều phối viên

- Rà lại toán học và truy nguyên nguồn: `PASS`. Các điểm được kiểm tra lại gồm phép đổi và quy nạp Huffman, trọng số Hình 4.2–4.3, điều kiện dựng lại, thứ tự E1/E2/E3, trạng thái `pending`, bốn khoảng toàn cục của bài CMU và tự thông tin xấp xỉ 9,48 bit.
- Rà lại toàn bộ kết nối và mạch viết: `PASS`. Sáu mạch ngoài có chức năng riêng, nối được từ hai trục lựa chọn đến ba cụm thuật toán, tổng hợp và recitation; kết luận thu hồi yêu cầu giao thức của mở bài.
- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại vì môi trường không có mô-đun `reloadserver` (`No module named reloadserver`). Điều phối viên dùng máy chủ dự phòng `/tmp/reloadserver.py` tại cổng 8765 để kiểm định cục bộ.
- Chromium QA3 duyệt đủ 48 trang ở cả `1280 × 720` và `800 × 600`: `errors=[]`, `katex=0`, `overflow=[]`.
- Điều khiển bàn phím bằng Playwright: `PASS`; `ArrowRight` chuyển từ `(0,0)` sang `(1,0)`, rồi `ArrowDown` chuyển sang `(1,1)`.
- Contact sheet và toàn bộ trang có rủi ro đã được kiểm tra trực quan. Các lỗi R11 bị cắt mã, S01 có từ mồ côi và X02 mơ hồ về trạng thái đầu đã được sửa; ba trang đều `PASS` ở lượt nhìn lại.
- Dự án Codex Slides `20260827223939-b-i-10-n-n-d-li-u-kh-ng-m-t-th-ng-tin-oh97` vẫn là bản nháp với 0 slide. HTML hiện tại đã được tải lên làm material `20260830141906650-7n5t.html`; tài nguyên mở workspace trả về thành công. Bề mặt công cụ hiện tại không có khả năng điều hướng Browser trong trình soạn thảo, nên không tuyên bố đã rà trực quan trên canvas Codex Slides.
- `2627-1/index.html` đã có thẻ Bài 10 và liên kết đúng tới tệp bài giảng; không cần thay đổi trong lượt này.
- Chưa ghi nhận commit hoặc push. Hai bước này chỉ được bổ sung sau khi lệnh Git tương ứng hoàn tất thành công.

## Kiểm toán hoàn tất ngày 2026-08-31

- Ghi chú `X00` từng nhắc “phân bổ thời lượng”, là siêu dữ liệu quy trình không cần cho mạch nói. Đã rút thành câu truy nguyên nguồn và cách chuyển đổi bài tập.
- Không đổi nội dung hiển thị, dữ kiện, yêu cầu, lời giải, số trang, thứ tự hoặc sáu mạch ngoài.
- Kiểm tra lại toàn HTML không còn `phút`, `thời lượng`, `minute` hoặc `duration`; thời lượng 120+60 chỉ nằm trong storyboard.
