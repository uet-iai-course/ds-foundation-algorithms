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

## Quy trình và kiểm định ghi chú tự học ngày 2026-09-02

### Tác tử OpenRouter

- Ba reader dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch (session 93306), bản đồ chủ đề (28479) và ánh xạ nguồn trong phạm vi hẹp (42275). Lượt ánh xạ 41422 vượt giới hạn công cụ nên bị loại, không dùng làm bằng chứng.
- Writer dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter (session 31245) trong gốc tạm chỉ chứa đặc tả và tài sản cần thiết. Bản nháp đầu bị loại do vượt giới hạn công cụ và hỏng đoạn cuối; bản viết lại thành công mới được đưa vào kho.
- Năm reviewer độc lập dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter để rà nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer. Lượt reviewer nguồn đầu vượt giới hạn công cụ và được chạy lại trong phạm vi hẹp (session 46136). Các báo cáo hợp lệ đều ghi `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Hai lượt tái kiểm sau sửa về toán–thuật toán và mạch tự học đều `PASS`, không còn lỗi nội dung. Lượt tái kiểm đầu gặp lỗi vận chuyển trong sandbox; các lượt chạy lại qua kết nối được phép mới được tính.

### Quyết định sau năm báo cáo

Đã áp dụng: sửa lỗi chính tả; bổ sung tiên quyết; làm rõ hai nút nhẹ nhất phải được lấy ra khỏi hàng đợi; bổ sung bước thứ hai trong chứng minh đổi; thay mệnh đề không có căn cứ về độ dài đường cập nhật; làm rõ trọng số `ESCAPE` và lá mới; thêm cây vào bài cập nhật để bài tự chứa; nêu quan hệ giữa khoảng chuẩn hóa và thanh ghi số nguyên; rút trùng lặp ở phần dựng lại và hoàn tất; chuyển bảng “BILL GATES” thành hai cột; bỏ mã nội bộ X01–X03 và mọi câu nhắc quy trình phê duyệt khỏi ghi chú công khai.

Không áp dụng: đổi đường dẫn hình thành `../../img/...`, vì viewer chủ động giải quyết đường dẫn từ gốc `2627-1/`; nhận định deck không tồn tại, vì tệp deck cục bộ đã được kiểm; yêu cầu đưa R08 trước chuẩn hóa, vì mạch hiện tại chủ ý đi từ khoảng lý tưởng qua cơ chế hữu hạn rồi mới nối độ rộng với số bit; yêu cầu thêm biến thể NYT/FGK/Vitter, vì ngoài phạm vi nguồn trục.

### Biên tập cuối và tính liên tục

- `$no-ai-slop`: cắt cụm nhấn mạnh thừa, câu mang giọng quy trình và các đoạn tổng kết lặp; giữ nguyên giá trị, giả thiết và kết luận đã được reviewer xác minh. Tự kiểm theo `no-ai-slop/eval.md` không còn lời dẫn rỗng, đối lập giả tạo, kết luận phô trương hoặc mã quy trình trong nội dung công khai.
- `$quill`: rà đồ thị `N01→N02→N03→N04→N05` và `N01→N06→N07→N08`, điểm hội tụ N09 và bài tập N10; thuật ngữ `ESCAPE`, `EOS`, $L,H,C_s,D_s$, tự thông tin và entropy nhất quán. Không tạo `quill.json`.
- Ghi chú không đổi ký hiệu, giả thiết, ví dụ hoặc kết luận dùng chung theo cách buộc phải sửa deck. Việc lặp lại SVG cây thích nghi trong bài tập chỉ làm bài tự chứa.

### Viewer và chỉ mục

- Chromium kiểm ở $1280\times720$ và $390\times844$: 32 heading khớp 32 liên kết mục lục; 104 biểu thức KaTeX, không lỗi; 10 lượt hình, không ảnh hỏng và mọi alt cụ thể; 4 khối bài tập/lời giải gập mặc định; 4 khối mã có ngôn ngữ; không tràn ngang hay lỗi runtime.
- Bàn phím `PASS`: liên kết bỏ qua điều hướng nhận focus, `Enter` tới nội dung và `Enter` mở khối gập. Bản in mở toàn bộ khối gập, ẩn mục lục và thanh hành động; mọi hình nằm trong khung in.
- An toàn đường dẫn `PASS`: từ chối `../AGENTS.md` và từ chối ghép tài liệu Bài 9 với deck Bài 10.
- Sau khi viewer đạt, `2627-1/index.html` mới được thêm liên kết ghi chú Bài 10. Chromium mở liên kết từ thẻ Bài 10 bằng bàn phím ở cả hai kích thước; đúng tiêu đề, deck, nguồn Markdown, 10 lượt hình và không lỗi KaTeX.
- Hai ảnh chụp toàn trang rộng/hẹp đã được điều phối viên xem trực quan; bố cục, hình, bảng, mã và khối bài tập đọc được. Deck không thay đổi.

Trạng thái ghi chú: `PASS`; đủ điều kiện commit và push. Commit và nhánh từ xa được xác minh bằng Git sau khi tạo commit.

## Vòng đồng bộ deck với ghi chú — 2026-09-02

- Reader kế hoạch phiên `64886` và reader nguồn phiên `87526` đều dùng `z-ai/glm-5.3-flash` qua OpenRouter; hai báo cáo giữ nguyên 48 trang, 6 mạch ngoài, 44+4 trang, 120+60 phút, 9 SVG với 10 lượt dùng và toàn bộ nội dung toán–thuật toán.
- Writer được gọi đúng `deepseek/deepseek-v4-flash-0731` trên dossier hẹp. Exec session `72347` đọc đủ dossier và áp dụng các chỉnh hẹp, nhưng sau đó chờ API quá 327 giây ở vòng tự kiểm nên bị dừng minh bạch; không có JSON kết thúc để xác nhận model quan sát và provider. Codex đối chiếu diff và chỉ đưa các delta reader phê duyệt vào kho.
- Index Bài 10 đổi nhãn `Ghi chú` thành `Ghi chú bài giảng`. Speaker notes P00, H02, H07, R00, R08 và R10 được viết trực tiếp hơn; H13, A10 và R13 bỏ nhãn “Kết cụm”; X00 bỏ lời nhắc phê duyệt và storyboard nhưng giữ nguồn Nelson–Gailly/CMU.
- Không đổi nội dung hiển thị, dữ kiện, công thức, thuật toán, chứng minh, bài tập, thứ tự R11→R08, mã trang hoặc SVG.
- `$no-ai-slop/eval.md`: đạt ở phạm vi sửa; không còn các nhãn quy trình đã khoanh vùng. Quill: thuật ngữ, ký hiệu và mạch sáu phần không đổi; không tạo `quill.json`.

### Năm phản biện và tái kiểm vòng đồng bộ

- Nguồn/truy nguyên `36219`, toán–thuật toán `47431`, sư phạm/sinh viên `72104`, văn phong `39981` và kỹ thuật `57678` đều trả `GO`. Tất cả dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter, với dossier dưới 40k token.
- Các phiên `41060` và `53228` chạm giới hạn công cụ; phiên `21696` vượt ngưỡng dossier 40k. Cả ba bị loại khỏi cổng.
- Góp ý nhẹ có giá trị ở R00 được áp dụng: 100.000 số 0 cùng EOS cần 100.001 bit Huffman, tức $100001=8\times12500+1$ và làm tròn thành 12.501 byte. Phiên `79269` bị loại vì tính sai phép chia; tái kiểm nguồn–toán phiên `92757`, cùng model/provider, trả `GO` và xác nhận khớp Nelson–Gailly.
- Không áp dụng nhận xét đổi thứ tự R08/R11 vì đây là quyết định mạch đã được reader nguồn và planning xác nhận. Không có lỗi chặn hoặc nghiêm trọng còn lại.

### Kiểm định cuối vòng đồng bộ

- Chromium duyệt đủ 48 trang ở $1280\times720$, $800\times600$ và $720\times900$: không tràn, lỗi JavaScript, lỗi KaTeX hay tài nguyên tải thất bại. Điều hướng bàn phím và đủ 48 speaker notes đạt; PDF deck có 48 trang.
- Viewer tải đúng tiêu đề, 32 heading, 28 liên kết mục lục, 104 biểu thức KaTeX không lỗi, 10 lượt hình và 4 khối gập đóng mặc định. Bản rộng và hẹp không có cuộn ngang nhìn thấy; bàn phím, bản in 18 trang, mở khối gập, từ chối vượt thư mục và từ chối cặp doc–deck khác bài đều đạt.
- Index có đúng một liên kết ghi chú Bài 10 và mở đúng deck/note, không có lỗi console. Đã xem trực tiếp R08, X00 và bản viewer hẹp; công thức, bố cục và SVG rõ, không chồng hoặc cắt.
- Codex Slides project `20260827223939-b-i-10-n-n-d-li-u-kh-ng-m-t-th-ng-tin-oh97` vẫn là draft 0 slide. Không tuyên bố đã kiểm canvas; bằng chứng hiển thị cuối là RevealJS và viewer cục bộ bằng Chromium.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 2 gồm Bài 07–15; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (5), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`. Mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch nên dùng `<tiền tố>T`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | HT | Mã Huffman tĩnh | Muốn nén văn bản có phân phối lệch, phải gán mã tiền tố ngắn cho ký hiệu xuất hiện nhiều. |
| 3 | AT | Huffman thích nghi | Muốn nén dòng chỉ đi qua một lần, phải cập nhật cây ở hai phía cùng nhịp sau mỗi ký hiệu. |
| 4 | RT | Mã hóa số học | Muốn vượt giới hạn một bit mỗi ký hiệu, phải gán cho cả thông điệp một khoảng có độ rộng bằng xác suất. |
| 5 | ST | Tổng kết và tự kiểm tra | Muốn chọn cặp mô hình và bộ mã, phải biết giao thức cần mang thông tin gì để khôi phục chính xác. |
| 6 | XT | Bài tập vận dụng | Muốn kiểm ba cách mã bằng tính tay, phải chạy chúng trên dữ kiện của Nelson–Gailly và CMU. |

Dòng dẫn 19–23 âm tiết; từ khóa 3–5 cụm; ghi chú diễn giả 79–100 âm tiết, viết từ nội dung các trang trong mạch. Số trang 48 → 54. Các trang nội dung đầu mạch (H00, A00, R00, S00, X00) đều có nội dung, không phải trang tiêu đề phần một dòng, và tiêu đề khác tên mạch; giữ nguyên.

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–6) ngay sau trang mục tiêu P01 (đứng ngay sau trang bìa), tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 24 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Bài có 6 section ngoài (trong khoảng 5–7), nên trang Nội dung đánh số 1–6. Mạch 5 đặt tên "Tổng kết và tự kiểm tra" theo `AGENTS.md`, vì phần S gồm bốn mục giao thức và câu hỏi chọn cặp.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Bài 10 còn khối `<style>` riêng và không mang lớp `.course-deck` (có từ trước, ngoài phạm vi). Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 60/60; 54 `data-slide-id` và 5 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/6` mở đúng trang tiêu đề mạch tương ứng (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 677 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng tên các mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 5 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Câu "Mỗi bài nộp…" ở ghi chú XT thay bằng "Lời giải gồm vết tính, trạng thái trung gian và kết luận." Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Viết lại ghi chú bài giảng theo chuẩn giáo trình (2026-11-07/08)

Yêu cầu người dùng (2026-11-07): rà soát ghi chú Bài 10 theo các nguyên tắc về nội dung, văn phong, bố cục và cách diễn giải của từng khối trong `../CLAUDE.md`, `CLAUDE.md` và `AGENTS.md`, giải thích chi tiết, đặc biệt các chứng minh quan trọng, "dùng nguồn MMDS"; sau khi ghi chú hoàn thiện mới làm lại bộ trang chiếu 10 từ ghi chú mới; xong thì commit và đẩy. Hiện trạng: ghi chú cũ 4 702 âm tiết, không khối đánh số, không mục tiêu, tiên quyết, bảng ký hiệu, tình huống, tóm tắt hay bài tập ba mức; $H$ mang hai nghĩa; một số trích dẫn và lời giải CMU bài 3 sai ý. Quy trình: AGENTS.md §"Quy trình tác tử gốc cho một ghi chú bài giảng".

**Nguồn.** MMDS không có chương nén dữ liệu (`sources/reference-slides/README.md`, dòng Bài 10: "MMDS không bao phủ mô-đun này"). Trục nguồn là Nelson–Gailly (NG) Chương 2–5; Stanford EE398A, CS106B và CMU 15-499 (kèm Assignment 1a và lời giải) để đối chiếu và cho các chứng minh mà NG chỉ phát biểu. Không có ghi công `mmds.org`. Đã báo người dùng khi bàn giao.

### Tác tử

| Tác tử | Vai trò | Loại, mô hình, effort (theo lệnh gọi `Agent`) | Đầu ra (scratchpad) | Quyết định |
|---|---|---|---|---|
| lập kế hoạch | phạm vi, phân bổ độ dài, đánh giá bản cũ, chu trình tám bước, 26 chứng minh, bài tập, Q1–Q14 (chỉ đọc) | general-purpose, opus, high | `plan-note.md` | chấp nhận, kèm quyết định Q1–Q20 |
| phân tích nguồn | ánh xạ NG/Stanford/CMU theo trang PDF, tính lại mọi ví dụ, mô phỏng AHUFF.C và ARITH.C, 27 lỗi nguồn (chỉ đọc) | general-purpose, opus, high | `source-dossier.md` | chấp nhận |
| bản đồ chủ đề | 25 chủ đề có nhãn, nguồn, khối dự kiến, thuật ngữ, ký hiệu, mâu thuẫn M1–M15 (chỉ đọc) | general-purpose, opus, high | `topic-map.md` | chấp nhận, chốt M1–M15 |
| soạn, sau đó chỉnh sửa (cùng tác tử, tiếp tục bằng `SendMessage`) | viết lại ghi chú, 9 SVG `note-*.svg` qua `generate_note_svg.py`, phần ghi chú của outline/storyboard; ba vòng chỉnh sửa; tách bài tập | general-purpose, opus, high | `writer-report.md`, `editor-report-{1,2,3}.md` | chấp nhận sau rà lại |
| rà: sinh viên | đọc không deck, tự giải ví dụ và bài tập | general-purpose, opus, high | `rv-student.md` (0/2/5/22) | chấp nhận |
| rà: chuyên gia | giả thiết, biến thể NG, so sánh công bằng, chi phí, 60+ trích dẫn | general-purpose, opus, high | `rv-expert.md` (0/2/7/14) | chấp nhận |
| rà: độ chính xác | tính lại độc lập (bản chuyển AHUFF.C, ARITH.C), 22 chứng minh, tham chiếu | general-purpose, opus, high | `rv-accuracy.md` (0/3/5/12); `rc-accuracy.md` (0/0/0/8); `rc2-accuracy.md` (0/0/0/0) | chấp nhận |
| rà: phản biện học thuật–giảng dạy | tám bước, khối, văn phong tác giả, `no-ai-slop` Detect | general-purpose, opus, high | `rv-pedagogy.md` (0/2/11/15); `rc-pedagogy.md` (0/0/1/9) | chấp nhận |
| rà: mạch, nguồn và kết nối | mạch, đoạn móc nối, cấu trúc, 44 nhóm dẫn nguồn, lệch với deck cũ | general-purpose, opus, high | `rv-storyline.md` (0/0/12/17); `rc-storyline.md` (0/0/0/13) | chấp nhận |

Số trong ngoặc: chặn bàn giao/nghiêm trọng/trung bình/nhẹ.

### Quyết định trước khi soạn (điều phối viên)

- Q1 trục NG thay MMDS (lý do ở trên). Q2 entropy và hai cận đặt trước Huffman. Q3 Shannon–Fano làm ví dụ dẫn, chu trình rút gọn. Q4/Q17/M1 các chứng minh không có trong nguồn được dựng đủ bước: chiều đảo Kraft, cận dưới entropy, cây có tính chất anh em là cây Huffman (không gắn tên Gallager vì nguồn được giao không nêu), bảo toàn tính chất anh em qua tăng–đổi, bit chờ, khoảng con nguyên không rỗng. Q5 ngoài phạm vi kèm nguồn có trang: bất đẳng thức McMillan, cận Fibonacci, bộ giải mã nguyên của Witten–Neal–Cleary (dẫn qua thư mục NG).
- Q6/M3 ký hiệu: khoảng $[a_t;\,a_t+w_t)$, $F(s)$, $G(s)$, tổng số đếm $N$, $\bar\ell$, $\operatorname{wt}(v)$; $H$ chỉ là entropy. Q8 dấu phẩy thập phân, dấu chấm phẩy ngăn đầu khoảng. Q9 trang NG là trang PDF.
- Q10 số sai của sách thay bằng số tính lại kèm một câu nêu số của sách; Q15 hai chỗ lời–mã của NG không khớp (chia đôi cắt cụt và $(w+1)/2$; ngưỡng 4 181 và `MAX_WEIGHT = 0x8000`) được nêu cả hai. Q18 điều kiện "nút đổi không là tổ tiên" là của FGK; trong biến thể NG không xảy ra (Bổ đề 10.24).
- Q16 không raster; SVG cũ của Bài 10 giữ nguyên cho deck cũ, hình ghi chú đặt tên mới `note-*.svg`.
- M15: không có mục "Bản đồ chủ đề" trong ghi chú (nhận xét người dùng 2026-11-04 cho `../rl-plan`: "quá nhiều không cần thiết"); chú thích `note-topic-id` giữ trong thân bài; bảng bốn nhóm ở `outline.md`. Khác với ghi chú Bài 09, không sửa các ghi chú đã công bố.
- Q13 mã chủ đề cũ → mới (đầy đủ ở `outline.md`, mục "Ánh xạ mã cũ → mới"): `L10-N01` → topic-02, 03; `N02` → 04, 05; `N03` → 08–11; `N04` → 14; `N05` → 12, 13, 15; `N06` → 16, 17; `N07` → 18–20; `N08` → 06, 07; `N09` → 21; `N10` → 24.

### Vòng rà 1 (bản đóng băng md5 `d4bfc3d0…`, 31 832 âm tiết)

| Mức độ | Vị trí | Vấn đề | Quyết định và xử lý |
|---|---|---|---|
| nghiêm trọng | Bổ đề 10.38, câu áp dụng sau nó | Phát biểu bỏ qua phép thu hẹp xen giữa các lần khoảng giữa và lần nửa dưới/trên; phản ví dụ trên chính Ví dụ 10.21 (độ chính xác, chuyên gia) | phát biểu lại trên $\psi^{-1}(\mathcal I_1)$ với $\psi(\eta)=2^{m'}(\eta-\tfrac12)+\tfrac12$, thêm bước quy nạp; kiểm vét cạn $R=6$–$8$ (tác tử soạn 8 310 thông điệp, tác tử độ chính xác 4 356 thông điệp, 0 vi phạm); điều phối viên đọc lại chứng minh |
| nghiêm trọng | Ví dụ 10.14 | E có từ mã 3 bit, không phải 4 (sinh viên, độ chính xác, chuyên gia) | sửa: 3 bit, `111` theo AHUFF.C |
| nghiêm trọng | sau Định lý 10.9 | "rút `00` thành `0`" không cho mã tiền tố (sinh viên, độ chính xác) | sửa: đổi `101` thành `11`, $K=7/8$ |
| nghiêm trọng | Nhận xét 10.20 | lặp khẳng định sai của NG tr.52 "từ mã không quá 16 bit"; mô phỏng HUFF.C cho 17–18 bit (chuyên gia) | nêu lời NG một câu; phép co chỉ làm số đếm vừa một byte, không chặn độ dài từ mã |
| nghiêm trọng | mục tiêu 5, 7 | không bài tập cho `ESCAPE`/thêm lá và bit chờ (giảng dạy) | thêm Bài tập 10.16, 10.17 (dữ liệu của chương) |
| nghiêm trọng | 18 dòng "Phạm vi.", 3 dòng "Điều kiện áp dụng." | nêu nguồn gốc chứng minh hoặc trỏ khối khác thay cho phạm vi (giảng dạy) | viết lại thành phạm vi/điều kiện thật; nguồn gốc chứng minh gom vào bảng "Nguồn của các chứng minh" ở mục tài liệu tham khảo |
| trung bình | 23 mục B1–B23 của `merge1.md` | quy tắc gán bit giả mã/ví dụ; đọc hình trên–dưới; mỗi chữ một nghĩa; lá trọng số 0 khi dựng lại; "trường hợp xấu nhất" từ một ví dụ; "tối ưu cho trọng số hiện thời"; so sánh công bằng (khoản cố định của bộ mã nguyên, Huffman khối, giá của mô hình thích nghi); `scale_counts`; bảng chi phí mã số học; nhắc lại A–E bằng số ở Mục 7; mở Mục 3.2; "Trong thực hành" và "Bỏ …" còn thiếu; tài liệu làm chủ ngữ; khối `algorithm`; danh sách song song; phân mức bài tập; bài tập trùng ví dụ (10.14 thêm phần (d)); bài tập lộ đáp số; Ví dụ 10.21 đổi từ "caba" (đáp số bài recitation) sang "cbb"; thuật ngữ cây hoàn hảo; khai báo dữ liệu của bản soạn; trích dẫn NG tr.122, tr.61–62 | đã sửa hết (`editor-report-1.md` §2) |

Bác hoặc không áp dụng: N15 (thêm Count-Min vào Mục 3.4, tùy chọn, ngoài mạch); câu "Bài 11 khai thác …" ở cuối Mục 7 (trỏ tiến, trái "The author's voice"); `note-topic-id` riêng cho 5.2, 5.4 (topic-16, 17 đã phủ).

**Độ dài.** Sau vòng sửa 1 ghi chú có 33 964 âm tiết (vượt trần 32 000). Theo AGENTS.md §"Tiêu chuẩn thứ nhất" ("trên 32 000 âm tiết phải xét tách phần bài tập"), điều phối viên chọn tách phần "Bài tập củng cố" (Bài tập 10.9–10.21) sang `materials/lec-10/exercises.md`, không cắt nội dung toán. Bài tập 10.1–10.8 tự kiểm sau từng mục vẫn ở trong ghi chú. Đánh số liên tục qua hai tệp.

**Vòng sửa 2–3.** Rà lại trên bản v2 (md5 `075ab79c…`): độ chính xác 19/20 phát hiện vòng 1 đã sửa đúng, 8 nhẹ mới; giảng dạy N1, N2, T1–T12 sửa đúng, còn R3 (trung bình: tài liệu làm chủ ngữ ở khoảng 9 chỗ) và 9 nhẹ; mạch 22/29 sửa đúng, 5 sửa một phần, 13 nhẹ. Điều phối viên: R9 — mục D của `merge1.md` cắt dòng "Kiểm tra lại." đã đi quá AGENTS.md §"Kiểm định ghi chú bài giảng"; phục hồi cho chín ví dụ, mỗi dòng một phép kiểm thật. R8: thêm Bài tập 10.18 (mục tiêu 3), 10.19 (mục tiêu 4), bài cũ 10.18–10.19 thành 10.20–10.21. Rà lại hẹp trên bản v3 (md5 `bb16a821…`): độ chính xác 0/0/0/0.

### Dữ liệu của bản soạn (không kèm nguồn, đã tính lại bởi hai tác tử)

Dòng bit giải mã ở Ví dụ 10.3; bộ độ dài $(1,1,2)$; cây phản ví dụ của Mục 4.1; vết thanh ghi 16 bit cho "cbb" (Ví dụ 10.21); bộ giải mã bỏ phép đổi (Tình huống 10.3); dữ kiện Bài tập 10.16 (thêm ký hiệu qua `ESCAPE`), 10.17 (bit chờ) và phần (d) của Bài tập 10.14. Danh sách đầy đủ ở dòng quy ước đầu ghi chú.

### Giáo trình và nguồn đã tham khảo theo mục

| Mục | Nguồn và trang |
|---|---|
| 1 | NG Ch.2 tr.18–25; CMU trang chiếu 2–8; CS106B tr.182 |
| 2 | CMU trang chiếu 13–14, 20–30, 47; EE398A-1 trang chiếu 3–23; CMU-A1 bài 4 |
| 3 | NG Ch.3 tr.30–37, 51–66; CMU trang chiếu 31–38, 56; CS106B tr.130–132 |
| 4 | NG Ch.4 tr.66–95 (Hình 4.2–4.10, AHUFF.C) |
| 5 | NG Ch.5 tr.96–104; CMU trang chiếu 39–51; EE398A-3 trang chiếu 2–9 |
| 6 | NG Ch.5 tr.102–126 (ARITH.C); CMU trang chiếu 52–56; EE398A-3 trang chiếu 10–14; CMU-A1 bài 3 |
| 7, tình huống | tổng hợp; NG tr.22, tr.25; EE398A-1 trang chiếu 21–23 |

CLRS 4e không có trong `sources/`; chi phí Huffman suy từ chi phí đống nhị phân (tiên quyết UET.CS1058). Không có đoạn dịch hoặc chép (mạch: lấy mẫu 44 nhóm dẫn nguồn; giảng dạy: lấy mẫu so sánh).

### Kiểm định ghi chú bài giảng (AGENTS.md §"Kiểm định ghi chú bài giảng")

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| mục tiêu ↔ kết quả ↔ bài tập | đạt | bảng mục tiêu ↔ bài tập trong `exercises.md`; `rc-storyline.md` xác nhận đủ 7 mục tiêu |
| tám bước cho mỗi khái niệm; tính tay trước giả mã, tính đúng, chi phí | đạt | bảng tám bước của `rv-pedagogy.md`, `rc-pedagogy.md`; bảng chi phí Huffman tĩnh, thích nghi, mã số học |
| ký hiệu trong bảng, mỗi chữ một nghĩa | đạt | `rc2-accuracy.md` |
| định lý bốn phần, chứng minh hoặc nguồn có trang | đạt | 22 khối kết quả đủ bốn phần; bảng "Nguồn của các chứng minh" |
| số liệu tính lại độc lập | đạt | script riêng của tác tử độ chính xác (`review1/acc/`, gồm `ahuff.py`, `arith16.py`, `lemma38.py`); vai sinh viên và chuyên gia tính lại độc lập các ví dụ chính; điều phối viên kiểm lại phản ví dụ Bổ đề 10.39 ($\lfloor16\,386/20\,000\rfloor=0$) và Bổ đề 10.38 |
| bài tập có gợi ý và lời giải; bài sách có số bài, mục, trang | đạt | 21 bài; NG tr.32–37, Hình 4.2–4.4; CMU-A1 bài 3, 4A |
| không "xem trang chiếu", câu mảnh, bước bị bỏ | đạt | năm vai rà |
| chứng minh chia bước, `aligned`, đoạn một ý | đạt | `rc-pedagogy.md`; ở 390 px khối nội dung chỉ rộng 230–317 px nên công thức được tách |
| số hiệu liên tục, tham chiếu đúng, khối không lồng, hiển thị | đạt | `check_refs2.py` và script của tác tử độ chính xác: 0 tham chiếu hỏng qua hai tệp; viewer bên dưới |
| đoạn móc nối, "Trong thực hành", nối Bài 09 và Bài 11 | đạt | `rc-storyline.md` |
| giọng kể, tài liệu không làm chủ ngữ | đạt | `rc-pedagogy.md` R3 đã sửa ở vòng 3 (grep thêm 18 câu) |
| nguồn theo mục, không dịch/chép | đạt | bảng trên |
| nhất quán với deck | chưa áp dụng | deck cũ dùng $[L,H)$, $C_s$, $D_s$, E1/E2/E3 và ví dụ cũ; `rv-storyline.md` liệt kê 19 chỗ lệch; deck được làm lại từ ghi chú mới ở giai đoạn sau, index ghi bài giảng "Chưa có" |

### Kiểm định của điều phối viên

- Ghi chú cuối: 31 977 âm tiết (`wc -w`), md5 `bb16a821…`; `exercises.md` 2 667 âm tiết, md5 `01b31228…`; 25 `note-topic-id`; 41 khối chung (10.1–10.41), 21 ví dụ, 3 tình huống, 21 bài tập.
- Chromium Playwright, `python -m http.server` cục bộ, hai tệp qua `material-viewer.html?doc=…&deck=lecture-10-…`: ở 1600×900 và 390×844, 0 lỗi console/trang, 0 request hỏng, 0 tài nguyên ngoài, 0 `.katex-error`, không cuộn ngang trang; ghi chú 46 công thức hiển thị, 0 tràn ở cả hai kích thước; 9/9 SVG tải được (ở 390 px hình nằm trong khung cuộn theo CSS học phần). Bản in: sau `beforeprint` 38/38 (ghi chú) và 26/26 (bài tập) khối `details` mở; xuất PDF được. Với `reloadserver`, viewer báo một lỗi CSP do script tự nạp lại của máy chủ chèn vào; với `http.server` không có lỗi. Đã tự xem ảnh đầu trang 1600 px và giữa trang 390 px.
- Index: thêm thẻ Bài 10 với ghi chú và bài tập; bài giảng "Chưa có" cho tới khi deck mới hoàn thành.

## Làm lại deck từ ghi chú mới (2026-11-08)

Theo yêu cầu người dùng 2026-11-07: sau khi ghi chú hoàn thiện (commit `51cb9ad`), làm lại deck Bài 10 dựa trên ghi chú mới. Deck là bản tóm lược của ghi chú (K3): không ví dụ, số, khẳng định hay nguồn ngoài ghi chú. Không dùng MMDS (như ghi chú), nên không có ghi công `mmds.org`; trang "Nguồn và tài liệu đọc" ghi NG, CMU 15-499, Stanford EE398A/CS106B.

### Tác tử

| Tác tử | Vai trò | Loại, mô hình, effort (theo lệnh gọi `Agent`) | Đầu ra (scratchpad) | Quyết định |
|---|---|---|---|---|
| lập kế hoạch deck | phạm vi, ngân sách 120 + 60 phút, mạch, chu trình, D1–D8 (chỉ đọc) | general-purpose, opus, high | `plan-deck.md` | chấp nhận, kèm K1–K3, D3–D8 |
| phân tích nguồn deck | ghi chú → trang, hình cần vẽ, bài recitation từ sách (chỉ đọc) | general-purpose, opus, high | `source-deck.md` | chấp nhận |
| soạn, sau đó chỉnh sửa (cùng tác tử, tiếp tục bằng `SendMessage`) | deck HTML, 17 SVG qua `generate_deck_svg.py`, selector CSS, phần deck của outline/storyboard; bốn vòng chỉnh sửa | general-purpose, opus, high | `writer-deck-report.md`, `writer-gate-report.md`, `editor-deck-report{,-2,-3}.md` | chấp nhận sau rà lại |
| cổng storyboard | lý do tồn tại, chu trình, trang tiêu đề mạch, mật độ, 120 + 60 phút (chỉ đọc) | general-purpose, opus, high | `review1/gate.md` (0/1/7/14) | qua có điều kiện; G1–G7 |
| rà: sinh viên (đo mật độ) | đọc deck như sinh viên năm hai, tự làm ví dụ và bài tập (chỉ đọc) | general-purpose, opus, high | `review2/rv-student.md` (0/0/7/17) | chấp nhận |
| rà: chuyên gia | khẳng định chuyên môn, giả thiết, so sánh công bằng (chỉ đọc) | general-purpose, opus, high | `review2/rv-expert.md` (0/4/6/7) | chấp nhận |
| rà: độ chính xác | tính lại mọi số, vết, SVG, giả mã bằng script (chỉ đọc) | general-purpose, opus, high | `rv-accuracy.md` (0/0/1/8); `recheck/rc-accuracy.md` (0/0/0/3); `rc2-accuracy.md` (0/0/0/0); `rc3-accuracy.md` (0/0/0/1) | chấp nhận |
| rà: phản biện học thuật–sư phạm, `no-ai-slop` Detect | checklist `slide_authoring_standard.md`, giọng văn (chỉ đọc) | general-purpose, opus, high | `rv-pedagogy.md` (0/0/9/22) | chấp nhận |
| rà: mạch và liên kết (vai trò, kết nối vào/ra) | từng trang: vai trò, kết nối vào/ra (chỉ đọc) | general-purpose, opus, high | `rv-storyline.md` (0/1/10/16); `rc-storyline.md` (0/0/2/13); `rc2-storyline.md` (0/0/0/2); `rc3-storyline.md` (0/0/0/3) | chấp nhận |
| kiểm định cuối | checklist `slide_authoring_standard.md`, kỹ thuật, mật độ, trực quan, đồng bộ kế hoạch, nhất quán ghi chú, git (chỉ đọc) | general-purpose, opus, high | `final/verifier.md` (1/0/2/6: chặn bàn giao là nhật ký này) | đạt có điều kiện → xử lý, xem dưới |
| soạn ghi chú (tác tử của giai đoạn ghi chú, tiếp tục bằng `SendMessage`) | đính chính N1–N5 | general-purpose, opus, high | `note-fix-report.md` | chấp nhận |

Số trong ngoặc: chặn bàn giao/nghiêm trọng/trung bình/nhẹ. Người soạn ghi chú và người soạn deck không chạy cùng lúc.

### Quyết định của điều phối viên

- K1: bảy section ngoài (Mở đầu · mã tiền tố–Kraft–entropy · Huffman tĩnh · Huffman thích nghi · mã số học, gộp Mục 5–6 · tổng kết · bài tập vận dụng). K2: hình vẽ lại bằng `generate_deck_svg.py` (nhãn ≥ 18 px khi chiếu), 9 SVG của deck cũ bị xóa lúc commit. K3: deck tóm lược ghi chú.
- D3: không giảng Ví dụ 10.13. D4: Bài tập 10.11 giữ quy tắc gán bit của ghi chú, nêu bằng nhãn "Quy ước:" trên trang đề; Bài tập 10.14 chỉ phần (a)–(c) theo NG Hình 4.2–4.4, phần (d) (dữ liệu của bản soạn) chỉ ở `exercises.md`. D5: gốc `reveal course-deck lecture-compression`. D6: "Đọc trước:" NG Chương 2–5. D7: luận đề và dòng dẫn "Muốn …, phải …". D8: recitation theo mạch (10.12, 10.11, 10.14, 10.15).
- Cổng storyboard (G1–G7): ngân sách thời gian không thật (trang chứng minh 1 phút) → gộp bảy trang (A11 vào A13B, A13–A13C còn hai trang, K20 vào K19, S09 vào S10, A16 vào A17, A19 vào A18, S08 xuống ghi chú diễn giả), trang chứng minh 1,5–2 phút; danh sách đọc thêm chép vào storyboard; chia/gọt K15, K16, K08, K02, A21, A23, K12; T05 không lộ lời giải; "NG" trên mặt trang thay bằng tên chương trình (HUFF.C, AHUFF.C, ARITH.C) hoặc quy tắc.

### Năm vòng rà (bản đóng băng d2, md5 `d6701316…`) và xử lý

| Mức độ | Trang | Vấn đề | Xử lý |
|---|---|---|---|
| nghiêm trọng | S01 | "ảnh fax hai màu không nén được" sai (chuyên gia) | theo ghi chú: với hai ký hiệu, mọi mã ký hiệu dùng đúng 1 bit mỗi điểm |
| nghiêm trọng | T02, P02 | cận $H\le\bar\ell<H+1$ gắn giả thiết "mã tiền tố" (chuyên gia; phản ví dụ ASCII) | cận dưới cho mọi mã tiền tố, cận trên cho mã tối ưu |
| nghiêm trọng | T03 | gộp cận lý tưởng với điều kiện thanh ghi, bỏ khoản cố định; đơn vị chi phí lẫn (chuyên gia, độ chính xác) | tách hàng lý tưởng/thanh ghi, ghi EOS, bit kết thúc, 16 bit 0; chi phí cùng đơn vị |
| nghiêm trọng | T04 | so sánh dùng hai quy tắc chọn chuỗi bit (5 bit ngắn nhất; 33 bit trung điểm) (chuyên gia; lỗi có từ ghi chú dòng 2003) | ghi chú đính chính N1, deck dùng 6 bit theo Định lý 10.34; bỏ tiêu chí "phân phối lệch" |
| nghiêm trọng | X03 (ghi chú diễn giả) | thời lượng và lời điều phối lớp (mạch) | bỏ; ghi phần trùng với ví dụ tăng A trong storyboard |
| trung bình | 28 phát hiện | A21 điều kiện 16 bit và phá hòa; A23 "Sau khi co:"; A17 cây lược ESCAPE/EOS; H04/H05 quy tắc phá hòa và gán bit; "Huffman A–E" trước mạch 3; A13/A13B thứ tự khởi tạo–duy trì–kết thúc, Bổ đề 10.24 đủ hai vế; T01 dòng $\lambda=87$; P02 ↔ T05 ánh xạ mục tiêu; S10 "Nhu cầu:"; K16, K02/K04 tách định nghĩa khỏi trang ví dụ; H12 $\Sigma'$, $T'$; A10 REBUILD, $W_{\max}$; G08 dòng trực giác và giả thiết; S14 ngoại lệ lũy thừa của $\tfrac12$; X01 định nghĩa cây nhị phân hoàn hảo; thuật ngữ tiếng Anh lần đầu; bốn trang "Bài tập:" trong mạch 2 phút; mật độ | đã sửa (`merge-deck.md` B1–B18; `editor-deck-report.md`) |
| nhẹ | 70 phát hiện | | áp dụng khi sửa lỗi hoặc làm rõ mà không tăng mật độ; mục bác ghi trong báo cáo chỉnh sửa (không thêm cột "Câu chốt", "Nguồn" vào storyboard: nguồn từng trang đã ở ghi chú diễn giả, như Bài 09; T06 giữ "Bài 11: nén bằng từ điển." vì thêm lý do vượt trần 60, lý do ở ghi chú diễn giả) |

Kiểm định cuối (`final/verifier.md`, bản d4): đạt có điều kiện. Chặn bàn giao: nhật ký này chưa có (đã ghi). Trung bình: tiêu đề cột T02 lệch khuôn `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` (đã sửa; ô cột cuối là công thức hoặc tên thuật toán); outline lệch deck ở luận đề và dòng dẫn KT, XT (đã chép nguyên văn). Nhẹ: T03 cột "Thuật toán" theo khuôn; lý do nội dung cho ngoại lệ trần 80 của P04B, T05; ghi chú P04B không tả bố cục; X04C bỏ đối lập. T06 giữ nguyên vì ghi chú không có năm cho CMU, Stanford. Phiếu kiểm `slide_authoring_standard.md`: mọi mục đạt (mục "sai khác nguồn, ngoại lệ có lý do trong nhật ký" đạt sau khi ghi mục này); 17/17 SVG tái tạo trùng byte từ `generate_deck_svg.py`; CSS bỏ selector `.lecture-compression` thì trùng HEAD.

Sau kiểm định cuối, rà lại T02, T03, X04C, P04B: độ chính xác 0/0/0/1 (X04C gọi tự thông tin là số bit phát ra), mạch 0/0/0/3 (X04C lặp; câu mở ghi chú P04B; hai ô T02 mất kết luận). Sửa cả bốn; điều phối viên đối chiếu diff (chỉ bốn chỗ đó) và kiểm lại trình duyệt.

Rà lại: độ chính xác (trang đổi, đính chính N1–N5, dẫn EE398A-1 trang chiếu 20 kiểm trên PDF) 0/0/0/3 rồi 0/0/0/0; mạch (trang đổi ±2, ranh giới, luận đề, ánh xạ mục tiêu) 0/0/2/13 rồi 0/0/0/2. Mọi phát hiện đã xử lý.

### Đính chính ghi chú phát sinh từ vòng rà deck

Ghi chú được sửa trước deck (ghi chú là chuẩn nội dung):

- N1 Mục 7: "6 bit thay cho 8 bit ở Ví dụ 10.19 (chuỗi ngắn nhất: 5 bit)", cùng quy tắc với BILL GATES 33 bit.
- N2 đầu mục HUFF.C: "phép co không bảo đảm điều đó: cận Fibonacci chỉ loại từ mã 17 bit khi gốc nhỏ hơn $4\,181$, còn gốc có thể tới $65\,281$" (bản trước ngầm khẳng định từ mã 17 bit xuất hiện).
- N3 tiêu đề Định lý 10.12: "phần cận dưới của định lý mã hóa không nhiễu của Shannon, Shannon's noiseless coding theorem" (EE398A-1 trang chiếu 20; trang chiếu 10 phát biểu định lý đầy đủ cho khối).
- N4 giới hạn độ dài từ mã của AHUFF.C: "Với biến tích bit 16 bit, …" (NG tr.75).
- N5 `exercises.md` Bài tập 10.12: cây nhị phân hoàn hảo "mọi nút trong có đúng hai con và mọi lá ở độ sâu $\ell_{\max}$".

Ghi chú sau đính chính: 31 992 âm tiết; `exercises.md` 2 674.

### Kiểm định của điều phối viên

- `check_deck.py` (Playwright Chromium, `python -m http.server` cục bộ; đếm âm tiết mặt trang trừ tiêu đề, KaTeX, giả mã, SVG, ô số, ghi chú; sửa ngày 2026-11-08 để không dính chữ giữa các ô bảng và `<li>`): 7 section ngoài, 105 trang (93 giảng, 120 phút; 12 bài tập vận dụng, 60 phút), `data-slide-id` duy nhất; ở 1600×900 và 390×844: 0 lỗi console, 0 request hỏng hay ra ngoài, 0 `.katex-error`, 0 trang tràn khung, không cuộn ngang; `#/2`…`#/7` mở đúng `mach-2`…`mach-7`, phím mũi tên chạy đúng. Mật độ: 34 trang ≤ 40 âm tiết, 63 trang 41–60 (cao nhất H04 59), 8 trang > 60, đều loại trần 80 hoặc có ngoại lệ ghi trong storyboard (T02 80, P02 77, T03 74, T05 69, G13 67, P04B 63, H15 63, X02 63); tối đa 2 công thức hiển thị; ghi chú diễn giả 56–247 âm tiết. Điều phối viên đã xem ảnh 1600 và 390 của P00, P04B, K11, KT, H08, A13, A13B, A17, S06, G11, T02, T03, T04, T05, X02, X04C.
- CSS: `lecture-course.css` chỉ thêm `.reveal.course-deck.lecture-compression …` vào 21 selector của khối Bài 08 (một selector `th` mới cho bảng nén trong `.example-slide .stream-compact`, phạm vi `.lecture-compression`). Bài 02, 03, 08, 09 kiểm ở 1600×900 và 390×844: 0 lỗi console, 0 `.katex-error`, không cuộn ngang; Bài 02, 08, 09 0 trang tràn; Bài 03 báo một phần tử của `lec03-s03-13` ra ngoài khung, có từ trước (deck 03 không mang lớp `lecture-compression`, nên thay đổi CSS không chạm tới).
- Ở 390 px RevealJS chuyển sang chế độ cuộn và bỏ qua `#/N` khi mở trang (như Bài 02, 09); `#/2`–`#/7` kiểm ở 1600×900.
- Ghi chú và bài tập sau đính chính, qua viewer ở 1600×900 và 390×844: 0 lỗi, 0 `.katex-error`, 0 tràn, 9/9 SVG; in: 38/38 và 26/26 khối `details` mở.
- Không raster. 9 SVG của deck cũ (`adaptive-sibling-increment`, `adaptive-swap`, `arithmetic-bill-gates`, `arithmetic-decode-normalize`, `arithmetic-renormalization`, `escape-eof-pipelines`, `huffman-code-decode`, `huffman-merge-a-e`, `prefix-tree-kraft`) không còn tham chiếu trong deck, ghi chú, index; xóa trong commit deck.
- Index: thẻ Bài 10 thêm liên kết bài giảng.

### Quyết định của người dùng về nguồn (2026-11-08)

Yêu cầu ban đầu ghi "sử dụng nguồn MMDS". Điều phối viên quét 11 tệp MMDS trong `sources/` (sách 3e Ch.1, 2, 3, 4, 5 và slide mmds.org Ch.2–5) với các từ khóa Huffman, arithmetic coding, Kraft, prefix code, entropy, compression: không có nội dung nào, chỉ một tên hội nghị trong thư mục tài liệu của Ch.3. `sources/reference-slides/README.md` ghi Bài 10 "MMDS không bao phủ mô-đun này". Người dùng được hỏi và chọn **chấp nhận Nelson–Gailly làm trục nguồn**, Stanford EE398A/CS106B và CMU 15-499 để đối chiếu, giữ nguyên ghi chú và deck đã đẩy (`51cb9ad`, `4869732`, `0dfedd7`).

## Sửa ghi chú theo chuẩn 2026-11 (đợt A2, giai đoạn 1, 2026-11-11)

Căn cứ: `prompt_fix_lecture_notes.md`; `AGENTS.md` §"Cấu trúc bắt buộc" mục 5, 6, 10 (commit `761469f`, `91599ec`, `6cd691f`). Điều phối viên: Claude Opus 5.5, effort high, không soạn hay rà.

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Rà văn phong và giọng tác giả (đợt duyệt toàn học phần, bản chưa đổi) | general-purpose | opus | high | không |
| Rà chuẩn giáo trình | general-purpose | opus | high | không |
| Rà độ chính xác toán và thuật toán (ba lượt) | general-purpose | opus | high | không |
| Biên tập (ba vòng, SendMessage) | general-purpose | opus | high | ghi chú |
| Kiểm tra lại mạch, liên kết và văn phong (hai lượt) | general-purpose | opus | high | không |

### Phát hiện và quyết định

| mức độ | vị trí | vấn đề | quyết định |
|---|---|---|---|
| trung bình | danh sách 77–84, bảng "Nguồn của các chứng minh", chín câu đính chính NG, khoảng 60 câu bàn nguồn hoặc lấy NG/HUFF.C/AHUFF.C/ARITH.C/CMU làm chủ ngữ | trái quyết định 2026-11-11 | chấp nhận: xóa; viết "nội dung (nguồn)"; tiêu đề Thuật toán 10.23, 10.26, 10.29, 10.40 và Nhận xét 10.28 bỏ "theo NG"/"chương trình" (số hiệu giữ); chứng minh ngoài phạm vi giữ nguồn ở mục tài liệu tham khảo (McMillan; cận Fibonacci NG tr.74–75; Witten, Neal, Cleary 1987, CACM 30(6), tr.520–540) |
| trung bình | 1415, 2045 | "mọi mã trên hai ký hiệu có $\bar\ell=1$" sai (mã {`0`, `10`} với $(0{,}9;0{,}1)$ cho $1{,}1$) | chấp nhận: "ít nhất 1 bit; mã Huffman đúng 1 bit" |
| trung bình | Tình huống 10.3(a) | lượt sửa 1 bỏ chữ "có thể" của nguồn | chấp nhận: khôi phục |
| trung bình | Nhận xét 10.20 | "nên" nối 257 bảng với $65\,536$ byte ($257\cdot256\ne65\,536$) | chấp nhận: tách gạch, bỏ quan hệ nhân quả |
| trung bình | Định nghĩa 10.36 | khoảng giữa, bit chờ định nghĩa trong văn xuôi, chưa có nghĩa vận hành | chấp nhận: nối vào Định nghĩa 10.36 (không tạo số mới), thêm nghĩa vận hành; giữ vị trí khối (thứ tự rút gọn: định nghĩa trước ví dụ tràn dưới) |
| trung bình | bảng ký hiệu | thiếu $J(u)$, $k'$, $\#i$, $c_{\mathrm H}/T_{\mathrm H}$, $\mathcal Q$, $j$, `count` | chấp nhận (24 dòng) |
| trung bình | Bổ đề 10.8, 10.15; Mệnh đề 10.27, 10.33, 10.41 | thiếu đoạn đọc và "Bỏ …" | chấp nhận; phản ví dụ kiểm bằng tính toán |
| trung bình | Mục 6, 7 mở và kết; câu mở phần tình huống; Tình huống 10.1 | mở bằng nguồn; mâu thuẫn Tình huống 10.2; tình huống không có bước áp dụng | chấp nhận |
| nhẹ | 966 | cận gốc $256\cdot255+1$ không đạt được (số đếm sau co ≤ 254) | chấp nhận: $256\cdot254+1=65\,025$ |
| nhẹ | cận Fibonacci, $z_6=K$, mã E/A ở Ví dụ 10.14, 22,81 bit, điều kiện cận trên Hệ quả 10.19, $d\ge d_{s_2}$, dấu "<" của NG cho $N$, trích dẫn mã nguồn NG tr.81, 85 thay lời văn | chấp nhận |
| nhẹ | các điểm văn phong còn lại (Ta/Chúng ta, nhãn "Ý tưởng:", điều hướng, giả mã tiếng Việt, thứ tự trường thuật toán, `aligned`, câu lặp, câu mảnh) | chấp nhận |
| — | đổi thứ tự trực giác–định nghĩa ở 266, 515, 1017, 1467, 1759 | bác bỏ: ghi chú theo §"Cách trình bày một chủ đề" (AGENTS.md dòng 221) |
| — | thêm bài tập sau 3.3, 4.1–4.3, 5.1–5.3, 6.1, 6.3 | bác bỏ: bài tương ứng ở `exercises.md` |
| — | bảng chi phí cho 10.26, 10.29; bỏ Tình huống 10.1 | bác bỏ (nhẹ; bỏ phải đánh lại số) |

Đính chính so với NG (chuyển khỏi ghi chú; người rà độ chính xác xác nhận cả 11 chỗ NG sai, ghi chú đúng): thứ tự ghép của HUFF.C khác lời văn tr.35–36 (Bài tập 10.1); tổng 83,56 bit của NG do làm tròn, đúng là 83,69 bit (Bài tập 10.4); tuyên bố từ mã ≤ 16 bit ở tr.52 không bảo đảm (có cây 17 bit với 175 ký hiệu, số đếm ≤ 247, gốc 28 656); quy ước bit theo vị trí: lời văn tr.81 ngược mã nguồn; Hình 4.4 và lời văn; Hình 4.12 ghi C có W=6, đúng là 5; khoảng của A ở tr.99 in 0,2–0,3, đúng là $[0{,}1;0{,}2)$; "minimum of nine bits" với 8 ký hiệu, đúng là 8; bảng tr.101–102 in range 10000 sau "Shift out 2", đúng là 100 000; `scale_counts` của ARITH.C: lần chia thứ hai không đặt lại số đếm về 1; "sáu lần" ở tr.96 là làm tròn của 6,6. Co trọng số: lời văn tr.75–77 chia đôi bỏ phần lẻ, mã tr.85 làm tròn lên.

Nguồn gốc số liệu chuyển khỏi ghi chú: các dữ kiện không kèm nguồn (danh sách dòng 77–84 cũ) là dữ liệu tính tay do người soạn dựng.

### Kết quả kiểm tra

- Độ dài (`wc -w`): 31 992 → 30 703 (dưới trần 32 000; đích 30 000 của hàng đợi là mềm).
- Khối có số hiệu: 86 khối (ghi chú + `exercises.md`) giữ số và loại; đổi tiêu đề trong ngoặc của Thuật toán 10.23, 10.26, 10.29, 10.40 và Nhận xét 10.28 như đã duyệt.
- Tham chiếu: 81 dẫn chiếu "Loại NN.k" trong ghi chú trỏ tới khối có thật.
- Grep: 0 HUFF.C, AHUFF.C, ARITH.C, "NG in", "lỗi in", "tính tay của chương", "Bài này", "Mục này"; `git diff --check` sạch.
- Trình duyệt (`http.server`, Playwright Chromium): ghi chú và `exercises.md` ở 1600×900 và 390×844, 0 lỗi console, 0 request hỏng, 0 `.katex-error`, không công thức tràn khung, không tràn ngang trang, khối gập mở khi in.
- Giai đoạn 2 (`exercises.md` theo quy tắc nguồn bài tập 2026-11-11: Bài 10 lấy bài từ CMU 15-499 vì NG không có bài tập) làm sau khi ghi chú được push.

## Tệp bài tập theo chuẩn 2026-11 (đợt A2, giai đoạn 2, 2026-11-11)

Căn cứ: `AGENTS.md` §"Cấu trúc bắt buộc" mục 10 và quyết định người dùng 2026-11-11: bài tập lấy từ giáo trình là nguồn chính; NG không có bài tập, nên Bài 10 lấy bài từ nguồn recitation đã duyệt (CMU 15-499, bài tập 1a và lời giải) và giữ hai ví dụ NG đã được duyệt làm bài recitation (ngoại lệ 2026-08-28). Không câu hỏi trang chiếu, không bài tự dựng.

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Lập danh sách bài | general-purpose | opus | high | không |
| Soạn (tác tử biên tập của giai đoạn 1, SendMessage) | general-purpose | opus | high | `exercises.md`, dòng tham chiếu của ghi chú, `storyboard.md`, `outline.md` |
| Rà độ chính xác (hai lượt) | general-purpose | opus | high | không |
| Rà vai sinh viên năm hai | general-purpose | opus | high | không |
| Rà sư phạm và văn phong, `no-ai-slop` Detect (hai lượt) | general-purpose | opus | high | không |

### Danh sách bài sau giai đoạn 2

| Bài | Nguồn | Mức | Mục tiêu |
|---|---|---|---|
| 10.14 | NG Ch.4, Hình 4.2–4.4, tr.69–72 (recitation); bỏ phần (d) tự dựng | nhận biết | 5 |
| 10.10 | CMU-A1 bài 2 (nhiệm vụ gốc: dựng mã giải mã duy nhất không tiền tố) | tính toán | 1, 2 |
| 10.11 | NG Ví dụ A–E, tr.32–37; phá hòa tr.35; gán bit tr.62–63 (recitation) | tính toán | 4 |
| 10.12 | CMU-A1 bài 4A (recitation) | tính toán | 2 |
| 10.13 | CMU-A1 bài 4B | tính toán | 2 |
| 10.9 | CMU-A1 bài 1 (dùng lại số 10.9; bài cũ là câu hỏi trang chiếu) | vận dụng | 3 |
| 10.15 | CMU-A1 bài 3 (recitation) | vận dụng | 3, 6 |

Bỏ: 10.9 cũ (câu hỏi CMU trang chiếu 22, dữ liệu đổi), 10.16 (`ESCAPE` với AB, tự dựng), 10.17 (thanh ghi $R=8$, tự dựng), 10.18, 10.19 (lời và định lý trên trang chiếu CMU 31–32), 10.20 (câu hỏi trang chiếu CMU 49), 10.21 (mở rộng tự dựng của Tình huống 10.3). Deck không dẫn 10.9, 10.16–10.21; ghi chú, `storyboard.md`, `outline.md` đã cập nhật. Mục tiêu 7 (thanh ghi, chọn cặp mô hình–bộ mã) không có bài nguồn; dựa vào Bài tập 10.7, 10.8 của ghi chú. 10.14 trùng các lần tăng của Ví dụ 10.12–10.13: giữ vì là bài recitation đã duyệt, xếp mức nhận biết, lời giải dẫn ví dụ thay vì chép. Lời giải CMU-A1 bài 4A (tr.3) in bất đẳng thức ngược chiều ($2^n\le\sum$); bài trong tệp viết đúng chiều.

### Phát hiện chính và quyết định

| mức độ | bài | vấn đề | quyết định |
|---|---|---|---|
| trung bình | 10.15(b) | gán cho Hệ quả 10.35 "độ dài kỳ vọng $4H$" | chấp nhận: tự thông tin kỳ vọng $4H\approx4{,}63$; số bit kỳ vọng trong $[4{,}63;6{,}63)$ |
| trung bình | 10.14 | lời giải chép Ví dụ 10.12–10.13 | chấp nhận: dẫn ví dụ, nêu tên phép đổi |
| trung bình | 10.9 và ghi chú | ghi chú xếp entropy có điều kiện vào "đọc thêm, không cần cho bài tập" | chấp nhận: sửa dòng tham khảo của ghi chú |
| trung bình | 10.10 | lời giải có ý không được hỏi | chấp nhận: CMU-A1 bài 2 không hỏi giải mã tức thời, cắt |
| nhẹ | 10.9, 10.10, 10.11, 10.12, 10.13, 10.15 | kiểm tra lại không có tác dụng, chỉ số $\varsigma_0$, dẫn sai Nhận xét 10.4, câu chen, từ so sánh không số | chấp nhận |
| — | đổi dữ kiện 10.14 cho khác ghi chú | bác bỏ: thành bài tự dựng |

### Kết quả kiểm tra

- Các lượt rà tính lại mọi số (phân phối dừng và entropy của 10.9; cây và 87 bit của 10.11; ba lần tăng của 10.14; giải mã caba, $I\approx9{,}48$, $\lambda=11$ của 10.15).
- `exercises.md`: 1 985 âm tiết, 7 bài, 7 hint, 7 solution; 80 dẫn chiếu "Loại 10.k" (ghi chú và tệp bài tập) trỏ tới khối có thật.
- Trình duyệt (`http.server`, Playwright Chromium): ghi chú và `exercises.md` ở 1600×900 và 390×844, 0 lỗi console, 0 request hỏng, 0 `.katex-error`, không tràn ngang, khối gập mở khi in.
- Lệch với deck (không sửa trong goal): dòng 43 "Bài tập 10.10 của ghi chú" (nay ở tệp bài tập); trang recitation 10.12 có ghi chú diễn giả "Ở Bước 1" (các bước nay mang tên theo kết quả); trang đề 10.11 có nhãn "Quy ước:" cho quy tắc gán bit (nay ghi nguồn NG tr.62–63); deck không dùng phần (d) của 10.14.


## Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): kiểm tra các deck 01–10 xem deck nào chưa tuân thủ các nguyên tắc của deck mới và chưa khớp với ghi chú bài giảng, ghi bảng phát hiện đầy đủ vào `review-log.md` của từng bài, thời điểm phát hiện là ngày 2026-11-13. Đợt này chỉ đọc: deck, ghi chú và `exercises.md` không đổi (HEAD `45ddcf9`; md5 deck `b026e2a0`, ghi chú `3a31a3bd`, `exercises.md` `37ad24e9`, trùng nhau lúc bắt đầu và lúc kết thúc lượt rà).

**Căn cứ.** `AGENTS.md` dòng 1–190 và 381–650; `slide_authoring_standard.md`; `CLAUDE.md` của học phần ("Course-specific rules", "Writing", "Deck structure and content"); `../CLAUDE.md` ("Writing course content", "The author's voice", gồm các luật 2026-11-04 và 2026-11-09); quy ước tác giả 2026-10-28/29 (`planning/lec-08/review-log.md` mục "Trang bài toán đầu mạch", `planning/lec-08/danh-gia-giang-day.md` "Định hướng chung"); quy ước của deck làm lại từ ghi chú (Bài 09 ngày 2026-11-04, Bài 10 ngày 2026-11-08): deck là bản tóm lược của ghi chú, ký hiệu theo bảng ký hiệu của ghi chú, mục tiêu khớp ghi chú, trang bài toán có hình sau mỗi trang tiêu đề mạch, chứng minh tách trang, mỗi bài recitation có trang "Lời giải:", dẫn chiếu khối ghi chú và bài tập trỏ đúng khối hiện tại.

**Tác tử (theo lời gọi công cụ).** Vai trò: rà soát chỉ đọc (quy tắc deck mới và đối chiếu ghi chú), một tác tử riêng cho Bài 10; loại `general-purpose`, mô hình `opus` (Opus 5.5), effort `high`; `no-ai-slop` chế độ Detect. Không ghi tệp trong kho, không commit. Mười tác tử của mười bài chạy song song (đều chỉ đọc). Điều phối viên: phiên Opus 5.5.

**Quét cơ học của điều phối viên** (Playwright, 1600×900 và 390×844, máy chủ tĩnh cục bộ): 105 trang, 7 section ngoài; trang tiêu đề mạch `mach-2…7` mở đúng `#/2…7`; 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 `fragment`; mã nguồn không có `<style>`, `style=""`, `.dense`; dẫn chiếu `10.k` của deck so với khối hiện có của ghi chú và `exercises.md` (đều tồn tại; loại khối và nội dung do tác tử kiểm). Các cờ quét được tác tử kiểm lại; cờ giả ghi ở mục "Đã kiểm" bên dưới.

**Điều phối viên kiểm lại trên tệp gốc:** mặt trang S01 (html:163) viết "Ảnh fax hai màu: mọi mã ký hiệu dùng đúng 1 bit mỗi điểm" và ghi chú diễn giả lặp lại; ghi chú (note:1376) viết "mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm ảnh, mã Huffman dùng đúng 1 bit". Bài tập 10.10 (K05 dẫn "của ghi chú") nay ở `exercises.md`:43; HUFF.C/AHUFF.C/ARITH.C có trên 16 dòng của deck, 0 dòng của ghi chú. Đúng như báo cáo.

**Quyết định của điều phối viên:** **chấp nhận** báo cáo làm bảng phát hiện của bài. Mọi phát hiện ở trạng thái **mở**; deck chưa được sửa. Cột "phát hiện" ghi thời điểm phát hiện.

**Kết luận:** cần sửa. Deck đúng khuôn deck mới và 124/125 dẫn chiếu 10.k đúng loại và đúng nội dung, nhưng còn một khẳng định toán học sai mà đợt A2 đã sửa trong ghi chú (mặt trang S01 và ghi chú diễn giả T05), một số liệu cũ (H16), mục tiêu học tập 6 so với 7 của ghi chú, bốn dẫn chiếu trỏ sai chỗ, và lớp câu lấy chương trình (HUFF.C, AHUFF.C, ARITH.C) làm chủ ngữ cùng câu đính chính NG mà đợt A2 đã bỏ khỏi ghi chú.

**Số phát hiện:** chặn bàn giao 0 · nghiêm trọng 1 · trung bình 6 · nhẹ 8.

Chế độ `no-ai-slop`: Detect. Dòng `html:` là dòng của tệp HTML (mỗi trang một dòng).

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | phát hiện |
|---|---|---|---|---|---|
| nghiêm trọng | S01 (mặt trang và ghi chú diễn giả), T05 (ghi chú diễn giả) | Lệch ghi chú + sai toán học: khẳng định mọi mã ký hiệu trên hai ký hiệu dùng **đúng** 1 bit, hay có $\bar\ell=1$. Đợt A2 đã sửa đúng câu này trong ghi chú (review-log dòng 388: mã {`0`,`10`} với $(0{,}9;0{,}1)$ cho $\bar\ell=1{,}1$). | html:163 mặt trang: "Ảnh fax hai màu: mọi mã ký hiệu dùng đúng 1 bit mỗi điểm."; html:163 ghi chú diễn giả: "mọi mã ký hiệu dùng đúng 1 bit mỗi điểm ảnh và không nén được gì"; html:232 (T05, lời giải câu 3): "mỗi từ mã dài ít nhất 1 bit và với hai ký hiệu mọi mã ký hiệu có $\bar\ell=1$, nên Huffman dùng $n$ bit". Ghi chú: note:1376 "mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm ảnh, mã Huffman dùng đúng 1 bit"; note:2016 "mã Huffman trên hai ký hiệu có $\bar\ell=1$". | S01: "Ảnh fax hai màu: mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm, mã Huffman đúng 1 bit." (sửa cả câu tương ứng trong ghi chú diễn giả). T05: "mỗi từ mã dài ít nhất 1 bit, và mã Huffman trên hai ký hiệu có $\bar\ell=1$, nên Huffman dùng $n$ bit". | 2026-11-13 |
| trung bình | H16 (ghi chú diễn giả) | Lệch ghi chú: số sai, đợt A2 đã đính chính trong Nhận xét 10.20 (số đếm sau co không vượt 254). | html:87: "còn gốc có thể tới $256\cdot255+1=65\,281$". note:930: "gốc có thể tới $256\cdot254+1=65\,025$, vượt xa $4\,181$"; review-log dòng 395. | Thay bằng "$256\cdot254+1=65\,025$". | 2026-11-13 |
| trung bình | P02 (mặt trang và ghi chú diễn giả), T05 (ghi chú diễn giả); kéo theo `storyboard.md` (bản đồ mạch, dòng 227) | Lệch ghi chú: mục tiêu học tập. Ghi chú có 7 mục tiêu; deck có 6, gộp mục tiêu 2 (mã tiền tố, cây mã, Kraft, dựng mã) và 3 (tự thông tin, entropy, hai cận) thành một, nên mọi số mục tiêu từ 3 trở đi lệch 1 so với ghi chú và bảng "Mục tiêu và bài tập" của `exercises.md`. Mục tiêu deck còn thiếu các ý của ghi chú: giải mã bằng cây mã và dựng mã từ độ dài (mục 2), lập bảng mã, giải mã và đầu mục (mục 4), `ESCAPE`, `EOS`, lá trọng số 0, dựng lại và chứng minh hai phía cùng cây (mục 5). | html:18: sáu dòng, dòng 2 "Kiểm mã tiền tố, tổng Kraft; tính entropy, chứng minh hai cận."; html:232 "kiểm mục tiêu 5", "kiểm mục tiêu 6" (đánh số deck). note:11–17 (bảy mục tiêu); ex:7–15 (bảng ánh xạ theo bảy mục tiêu). | Viết lại P02 theo bảy mục tiêu của ghi chú, mỗi dòng một cụm động từ (dưới trần 80, ≤ 20 âm tiết mỗi dòng; nếu vượt 6 dòng thì ghi ngoại lệ 7 dòng vào storyboard với số âm tiết trước/sau). Đánh lại số mục tiêu trong ghi chú diễn giả P02, T05 và trong storyboard. | 2026-11-13 |
| trung bình | K05, G04, X03, A03 (ghi chú diễn giả) | Lệch ghi chú: dẫn chiếu trỏ sai chỗ sau đợt A2. (1) Bài tập 10.10 nay ở `exercises.md`, không ở ghi chú. (2) Ba trường hợp chuẩn hóa và bit chờ nay thuộc Định nghĩa 10.36 (A2 "nối vào Định nghĩa 10.36"), không phải Thuật toán 10.37. (3) Bài tập 10.14 không còn phần (d) (A2 bỏ phần tự dựng). (4) "dòng cuối" của A03 không có trên mặt trang. | (1) html:43: "(Bài tập 10.10 của ghi chú, theo CMU-A1, bài 2)"; ex:43. (2) html:185: "Ba trường hợp chuẩn hóa của Thuật toán 10.37."; note:1694–1698 (ba trường hợp trong Định nghĩa 10.36). (3) html:250: "Bài tập 10.14 (a)–(c) của tệp bài tập …; phần (d) của tệp bài tập không dùng ở đây."; ex:19–25 chỉ có (a)–(c). (4) html:102: "Phản ví dụ ở dòng cuối là NG, Hình 4.8"; mặt trang A03 chỉ có định nghĩa và công thức. | (1) "Bài tập 10.10 của tệp bài tập". (2) "Ba trường hợp chuẩn hóa của Định nghĩa 10.36, dùng trong Thuật toán 10.37." (3) "Bài tập 10.14 của tệp bài tập" (bỏ vế phần (d)). (4) "Một phản ví dụ: cây A1, B1, C3, D3 …" (bỏ "ở dòng cuối"). | 2026-11-13 |
| trung bình | X02 (mặt trang và ghi chú diễn giả), X02C (ghi chú diễn giả) | Lệch ghi chú (bài recitation ↔ `exercises.md`): quy tắc "bit 0 cho nút lấy ra trước" được ghi là quy ước của ghi chú; `exercises.md` nay ghi nguồn NG tr.62–63 cho quy tắc này. Nhãn "Quy ước:" trên trang đề vì thế mô tả sai bản chất dữ kiện (review-log dòng 459 đã ghi lệch này). | html:247 mặt trang: "Quy ước: phá hòa chọn D trước C; trong mỗi lượt, nút lấy ra trước nhận bit 0."; ghi chú diễn giả: "quy tắc gán bit 'nút lấy ra trước nhận bit 0' là quy ước của ghi chú, khác cách gán trên hình của NG". ex:62: "quy tắc phá hòa chọn D trước C (NG, tr.35) và quy tắc gán bit 0 cho nút lấy ra trước trong mỗi lượt (NG, tr.62–63)". | Mặt trang: đưa hai quy tắc vào dòng đề ("Chạy Huffman tĩnh với phá hòa chọn D trước C và bit 0 cho nút lấy ra trước trong mỗi lượt.") và giữ dòng "Nguồn: … tr.32–37, 62–63." Ghi chú diễn giả: "Quy tắc phá hòa theo NG, tr.35; quy tắc gán bit theo NG, tr.62–63, khác cách gán trên hình tr.35–36." | 2026-11-13 |
| trung bình | mặt trang: H16, A14, A15, A21, A23, G07; ghi chú diễn giả: P10, H15, A02, A04, A10, A13B, A17, A21, A23, S03, G01, G04, G09, AT | Lệch ghi chú + Quy tắc (nguồn chỉ ở ghi chú diễn giả; quyết định A2 2026-11-11 bỏ câu lấy HUFF.C/AHUFF.C/ARITH.C/NG làm chủ ngữ): deck giữ tên chương trình làm chủ ngữ trên mặt trang và tên biến mã nguồn trong ghi chú diễn giả; ghi chú hiện viết "cài đặt", "bộ nén", "giao thức". | html:87 "HUFF.C dùng 257 ký hiệu: 256 giá trị byte và EOS."; html:120 "Mô hình: so sánh và ghi trên mảng nút của AHUFF.C"; html:121 "AHUFF.C khởi tạo hai lá trọng số 1"; html:142 "AHUFF.C dùng unsigned long."; html:143 "($32\,768$ ở AHUFF.C)"; html:200 "Kết thúc của ARITH.C:"; html:28 "còn chương trình HUFF.C phá hòa khác"; html:185 "NG gọi $m$ là underflow_bits"; html:202 "Thủ tục scale_counts của ARITH.C"; html:165 "$F(s)$ giống totals[s] của NG". Ghi chú: note:929 "bảng chữ cái có 257 ký hiệu"; note:1199 "cây khởi tạo chỉ có hai lá: `ESCAPE` ở $\#1$ và `EOS` ở $\#2$"; note:1312 "Ngưỡng $W_{\max}$ được chọn bằng `0x8000`"; note:194 (Bài tập 10.1 mô tả hai quy tắc, không nêu HUFF.C); review-log dòng 387. | Mặt trang: "Bảng chữ cái 257 ký hiệu: 256 giá trị byte và EOS."; "Mô hình: so sánh và ghi trên mảng nút; …"; "Cây khởi tạo: hai lá trọng số 1, ký hiệu thoát … ở $\#1$, EOS ở $\#2$."; "… gốc $4\,181$ đã có thể tràn; cài đặt tích từ mã trong biến 32 bit."; "($W_{\max}=32\,768$)"; "Kết thúc: bit thứ hai của low là 0, …". Ghi chú diễn giả: thay chủ ngữ chương trình bằng "cài đặt"/"bộ nén", giữ số trang NG trong ngoặc; P10 mô tả hai quy tắc phá hòa như Bài tập 10.1 hiện hành. | 2026-11-13 |
| trung bình | ghi chú diễn giả: K15, H04, H16, H17, A02, A23, S07, S10, G02, X01B, T06 | Lệch ghi chú + Quy tắc (không câu đính chính sách; quyết định A2 chuyển 11 chỗ đính chính NG sang `review-log.md`): deck còn các câu "NG in/ghi/viết …, đúng là …". | html:48 "NG (tr.20) gọi $-\log_2p$ là 'entropy của một ký hiệu'"; html:87 "NG (tr.52) viết thêm rằng từ mã không dài quá 16 bit, nhưng phép co không bảo đảm điều đó"; html:88 "NG in $83{,}56$ do làm tròn trước khi nhân"; html:101 "lời văn NG (tr.81) mô tả ngược lại"; html:143 "NG ghi trọng số 6 cho C ở Hình 4.12; giá trị đúng là 5"; html:177 "NG (tr.99) in khoảng của A là $0{,}2$–$0{,}3$"; html:178 "NG viết 'ít nhất chín bit', số đúng với tám ký hiệu là 8"; html:183 "bảng của NG in $10\,000$"; html:246 "Lời giải CMU-A1 (tr.3) in bất đẳng thức của Bước 3 theo chiều ngược lại"; html:233 "Các số in sai của NG đã được thay bằng số tính lại: …". review-log dòng 402. | Xóa các câu đính chính; giữ số đúng như ghi chú (vd. H16 giữ "phép co không bảo đảm từ mã dài không quá 16 bit, vì gốc có thể tới $65\,025$"; S10 giữ "Huffman dùng 8 bit"). | 2026-11-13 |
| nhẹ | K11, H15, G13, P07, T06, X01 (ghi chú diễn giả) | Quy tắc: câu xuất xứ số liệu và lời của người soạn (luật tác giả "no provenance sentences"). | html:45 "Bộ $(1,1,2)$ là dữ liệu tính tay của ghi chú"; html:86 "Các số trong bảng là phép đếm theo giả mã, không phải số đo."; html:25 "Phản ví dụ CMU, trang chiếu 7." (câu cụt, không nói phản ví dụ nào); html:25 "… không thuộc bài này (NG, tr.18–19)"; html:233 "Bài này không dùng MMDS, vì MMDS không có chương nén."; html:245 "Đề CMU gợi ý 'quy nạp'; ghi chú chốt cách đếm lá theo lời giải CMU-A1, nên đề nêu 'bằng cách đếm các lá'." | "Bộ $(1,1,2)$ cho ba ký hiệu"; "Các số trong bảng là phép đếm theo giả mã."; bỏ câu "Phản ví dụ CMU, trang chiếu 7."; "Nén mất thông tin (lossy compression) chỉ yêu cầu bản khôi phục gần bản gốc (NG, tr.18–19)."; bỏ câu MMDS (quyết định nguồn đã ở review-log); bỏ câu về đề CMU. | 2026-11-13 |
| nhẹ | X04 (mặt trang); P09, T03 (ghi chú diễn giả) | Quy tắc (luật 2026-11-09, cắt từ làm mềm khi có số): `no-ai-slop` Detect, mục "Protect the specific fact". | html:253 "Entropy của mô hình chỉ hơn 1 bit một chút." (ex:163 cho $H\approx1{,}157$ bit); html:27 "nên câu đó thường nói về mô hình" (note:178 "nói về mô hình chứ không về bộ mã"); html:230 "nên nén khá chỉ sau vài nghìn byte", "mã số học thường chậm hơn đáng kể". | X04: "Entropy của mô hình là $H\approx1{,}157$ bit mỗi chữ." P09: "nên câu đó nói về mô hình chứ không về bộ mã". T03: "tỷ lệ nén khá chỉ đạt sau vài nghìn byte (NG, tr.25)"; "NG (tr.23) nêu mã số học chậm hơn đáng kể" (câu trích nguồn giữ được, bỏ "thường"). | 2026-11-13 |
| nhẹ | P00, P08, S02, H05, H02 (ghi chú diễn giả) | Quy tắc: chỉ đường, câu lặp mặt trang (`no-ai-slop` Detect: interpretive metadiscourse). | html:13 "Câu luận đề nêu hai cận độ dài: …"; html:26 "định nghĩa kế tiếp đặt tên cho chúng."; html:164 "Định nghĩa kế tiếp viết phép thu hẹp thành công thức với cận dưới và độ rộng."; html:69 "Đây chính là mã 87 bit đã gặp ở mạch trước, nay có thủ tục dựng từ số đếm."; html:66 "theo phép tính ở dòng cuối". | P00: "Huffman có độ dài trung bình dưới …" (bỏ "Câu luận đề nêu hai cận độ dài:"); P08, S02: bỏ câu chỉ đường; H05: "Mã 87 bit có độ dài $(1,3,3,3,3)$ nay dựng được từ số đếm."; H02: "vì đưa A lên độ sâu 1 tiết kiệm 15 bit, đẩy B, C xuống 3 tốn 13 bit". | 2026-11-13 |
| nhẹ | X01B (mặt trang và ghi chú diễn giả) | Lệch ghi chú + Quy tắc (nhãn bước theo kết quả): lời giải Bài tập 10.12 trong `exercises.md` nay đặt tên bước theo kết quả; deck dùng "Bước 1–3" (review-log dòng 459 đã ghi). | html:246 "Bước 1: $c(s)$ là tổ tiên …", "Bước 2: …", "Bước 3: …"; ghi chú diễn giả "Ở Bước 1, …". ex:92–100: "Tập lá của một từ mã.", "Các tập lá rời nhau.", "Đếm lá." | Thay nhãn bằng "Tập lá của một từ mã:", "Các tập lá rời nhau:", "Đếm lá:" (không in đậm) và sửa ghi chú diễn giả tương ứng; thêm dòng kiểm tra của ex:102 ($4+2+1+1=8$) vào ghi chú diễn giả nếu muốn. | 2026-11-13 |
| nhẹ | K02, K16, P00/P06 | Lệch ghi chú (luật tác giả: mọi tên tiếng Anh thông dụng ở lần đầu): thiếu tên Anh có trong ghi chú. | html:41 "Mã tiền tố còn gọi là mã tức thời (instantaneous code)" — note:220 thêm "prefix-free code"; html:49 "Độ dài trung bình (average length)" — note:455 thêm "expected code length"; deck không nêu "lossless compression" — note:145. | K02: "mã tiền tố (prefix code, còn gọi là prefix-free code)"; K16: "(average length, expected code length)"; ghi chú diễn giả P00 hoặc P06: "nén không mất thông tin (lossless compression)". | 2026-11-13 |
| nhẹ | P00, P02, P03, K05, K08, K11, K12, K16, K19, H11, H16, A04, A10, A17, A21, A23, S06, S10, S11, G11, T03, T04, T06 | Quy tắc: ghi chú diễn giả dài hơn 150 âm tiết trên trang không phải chứng minh hay lời giải. | `density.json`: K05 203, H16 208, S10 211, S11 194, T03 194, T04 194, A10 188, T06 185, A17 184, A21 184, G11 182, P00 180, K11 180, A23 179, K08 173, S06 170, K19 169, A04 168, H11 168, K12 166, P02 163, P03 153, K16 151. | Phần lớn độ dài đến từ câu nguồn, đính chính và tên chương trình; sửa ba dòng trung bình ở trên sẽ đưa đa số về dưới 150. Chuyển phần còn lại về ghi chú bài giảng. | 2026-11-13 |
| nhẹ | S01 (mặt trang) | Quy tắc (một ý mỗi dòng, ≤ 20 âm tiết mỗi dòng): dòng thứ ba gộp hai ý (ảnh fax và $1\,000$ ký hiệu xác suất $0{,}999$), xuống hai dòng ở 1600×900. | html:163; ảnh `shots-10/S01.png`: dòng "Ảnh fax hai màu: … $1\,000$ ký hiệu xác suất $0{,}999$: $1{,}44$ so với $1\,000$ bit." chiếm hai dòng. | Tách thành hai dòng: "Ảnh fax hai màu: mã Huffman đúng 1 bit mỗi điểm." và "$1\,000$ ký hiệu xác suất $0{,}999$: $1{,}44$ bit, Huffman $1\,000$ bit." | 2026-11-13 |
| nhẹ | X01 | Quy tắc (quy ước tác giả 2026-10-28/29, trang bài toán có hình sau trang tiêu đề mạch "khi phù hợp"): trang mở mạch bài tập vận dụng không có hình, trong khi đề nói về đếm lá trên cây hoàn hảo. | html:245: không `<img>`; XT → X01. | Tùy chọn: thêm SVG cây hoàn hảo độ sâu 3 với tập lá của mã `0`, `10`, `110`, `111` (dữ kiện của ex:102), nhãn ≥ 18 px. | 2026-11-13 |

### Đã kiểm, không lỗi / bác bỏ cờ quét

- **Dẫn chiếu `10.k` (trọng tâm 1).** Liệt kê 124 lần nêu số hiệu theo trang (refcheck đếm 125 vì tách "Ví dụ 10.1, 10.5, 10.6" và "Thuật toán 10.37 và 10.40"). Đối chiếu từng số với khối hiện tại: đúng loại và đúng nội dung ở P01 (08.1, 09.37), P02/P07/T05 (Mệnh đề 10.2), P05–P10 (10.1, 10.2, 10.3, 10.4, Bài tập 10.1), K01–K21 (10.5, 10.3 ví dụ, 10.6, 10.7, 10.8(c), 10.4 ví dụ, 10.9 kể cả "Bước 2–3" và "Bước 1–3", 10.10, 10.11, 10.5 ví dụ, 10.12, 10.13, 10.6 ví dụ, Bài tập 10.3), H01–H17 (Ví dụ 10.1/10.5/10.6/10.7/10.8/10.9/10.10, Thuật toán 10.14, Bổ đề 10.15–10.17, Định lý 10.18, Hệ quả 10.19, Nhận xét 10.20, Bài tập 10.4), A01–A20 (10.21–10.29, Ví dụ 10.11/10.12/10.14/10.15/10.16, Tình huống 10.3(b)), S01–S14 (Tình huống 10.2, 10.30–10.35, Ví dụ 10.17–10.19, K08 → Định lý 10.34(b)), G01–G15 (10.36 định nghĩa thanh ghi, Ví dụ 10.20, 10.21, Bổ đề 10.38, 10.39, Thuật toán 10.40, Mệnh đề 10.41, Bài tập 10.7), T04 (Bài tập 10.8 có trong ghi chú), X01–X04C (Bài tập 10.11, 10.12, 10.14, 10.15 của `exercises.md`). Bốn chỗ sai đã nêu ở bảng (K05, G04, X03, A03). Không trang nào dẫn 10.9, 10.13 hay 10.16–10.21 cũ.
- **Bốn bài recitation (trọng tâm 2).** Đúng bốn bài 10.12, 10.11, 10.14, 10.15 theo thứ tự mạch giảng (XT, html:233 ghi chú diễn giả). Đề khớp `exercises.md` (số đếm, cây $\#1$–$\#9$ A2…gốc 18, mô hình $p=(0{,}1;0{,}2;0{,}7)$, dòng `01001110110`, bốn chữ); số bài, nguồn và trang ghi trên trang đề. Lời giải tính lại: X02B–X02C (bốn lượt E5/D6, C6/B7, 11/13, A15/24; mã A=0, E=100, D=101, C=110, B=111; 87 bit; Kraft 1) khớp ex:74–80; X03B–X03C (danh sách sau lần 1, 2, 3; gốc 19, 20, 21; độ dài; Kraft 1) khớp ex:32–38; X04B–X04C ($630/2048=0{,}3076171875$; $\zeta$ mới $0{,}01088$, $0{,}1088$, $0{,}0441$; caba; $w_4=0{,}0014$; $I\approx9{,}48$; $\lambda=11$; $0{,}3077\cdot2^{11}\approx630{,}17$; $H\approx1{,}157$, $4H\approx4{,}63$) khớp ex:174–187; X01B khớp ex:92–100 về nội dung (lệch nhãn bước đã nêu). Mỗi bài có trang "Lời giải:" cùng tiêu đề và hướng dẫn chấm 10 điểm trong ghi chú diễn giả.
- **Số liệu tính lại:** 312/117 bit; Kraft của bốn bộ độ dài; bảng $z_i$; 87, 89, 102, 107 bit; $\Delta=(15-5)(3-1)=20$; $85{,}25$, $2{,}186$, $2{,}231$, $124{,}25$; Bài tập 10.4 (89 bit, $83{,}69$); $\mathrm{fib}(18)=4\,181$; BILL GATES ($w_{10}=4\cdot10^{-10}$, $31{,}22$ bit, các hàng lược của S04, S07, G02 khớp note:1415–1426, 1506–1517, 1710–1721); bảy chữ A ($a_8$, $w_8$, $4{,}386$, `01110`, `011101`); vết cbb (G06–G07: 19 660, 24 247/33 421, 15 726/34 075, 17 561/21 230, …, `011001`, $0{,}390625$); G10 (count 3 và 1); G15 (count 7 và 13); T04 (32 và 33 bit, $65\,280$, 1,3 MB). Đều khớp ghi chú.
- **Mật độ (trọng tâm 4).** P02 77 (trần 80 mục tiêu, 6 dòng) và T02 80 (trần 80 bảng tổng kết, 7 hàng) đạt trần; ngoại lệ 7 hàng của T02 có lý do và số âm tiết trước/sau ở storyboard:225. Các trang trên 60 khác đều có ngoại lệ hợp lệ trong storyboard:214–228: P04B 63 (lý do và 61 → 63), H15 63 và G13 67 (bảng chi phí, 8 và 7 dòng), T03 74 (bảng so sánh), T05 69 (58 → 69), X02 63 (đề recitation). `disp_gt3` rỗng; ghi chú diễn giả không trang nào dưới 40 hay trên 250 âm tiết.
- **Cấu trúc deck mới.** Bìa có câu luận đề; P01 có "Nhắc lại:" và "Ký hiệu:"; Nội dung đánh số khớp `#/2…#/7` (`hash_strand` của check.json); P04 + P04B có vấn đề và bốn câu trả lời có điều kiện; sáu trang tiêu đề mạch có dòng dẫn "Muốn …, phải …" (20–24 âm tiết), từ khóa ≤ 5 (TT không có từ khóa, được phép), ghi chú 82–99 âm tiết. Trang bài toán có hình sau KT, HT, AT, ST, TT: K01, H01, A01, S01, T01. Mỗi mạch nội dung có trang "Câu hỏi:" với lời giải trong ghi chú diễn giả (K21, H17, A20, G15). Cụm thuật toán đủ bước "Đầu vào/Đầu ra", giả mã, đọc giả mã, tính đúng (A13/A13B bất biến, H12 quy nạp, H09 đổi chỗ), "Mô hình:" rồi bảng chi phí (H15, A14, G13). Mạch tổng kết có hai bảng đúng khuôn cột, trả lời có điều kiện, "Câu hỏi: trả lời và nêu kết quả đã dùng.", trang nguồn có liên kết viewer và câu nối Bài 11 khớp note:2106. Nhãn in đậm đều thuộc danh sách cho phép; "Bước k:", "Khởi tạo:", "Kết thúc:", "Về mặt ý tưởng:" không in đậm.
- **Mạch ↔ mục ghi chú.** Mạch 5 gộp Mục 5 và 6 của ghi chú (tiền tố S/G); lý do giữ trong 7 section ngoài ghi ở storyboard:13. Mục 7 → mạch tổng kết. Các khối chỉ ở ghi chú diễn giả (Mệnh đề 10.33 ở S11, Bổ đề 10.24 ở A13B, Mệnh đề 10.27 ở A18, Ví dụ 10.13 chỉ ở recitation) theo quyết định G1 ghi ở storyboard:29; không đề nghị lật lại.
- **Ký hiệu và thuật ngữ:** $\Sigma,k,x_t,f_s,N,p_s,c,c^*,\ell_s,J(u),K,I,H,\bar\ell,\operatorname{cost}(T),\mathcal Q,\operatorname{wt},k',\#i,W_{\max},F,a_t,w_t,z,\lambda,R,Q,G,m,\zeta,\eta,\mathcal I_0,\mathcal I_1,\psi,h$ dùng đúng nghĩa của bảng ký hiệu note:42–67; tên ký hiệu chữ đứng; dấu phẩy thập phân và khoảng nửa mở đúng quy ước.
- **Hình:** 17 SVG, nhãn nhỏ nhất 19,4–21,3 px khi quy về 1280×720 (≥ 18); số liệu trên hình khớp ghi chú (đo bằng `w10/svgsize.py`, ảnh trong `shots-10/`).
- **Cờ quét bác bỏ:** `style_blocks=1` là thẻ do runtime chèn (mã nguồn không có `<style>`); `overflow_1600` rỗng, `hscroll_390` false; S01 bị cắt mép trái ở ảnh chụp đầu là do chụp giữa hiệu ứng chuyển trang (chụp lại sau 1,5 s thì đủ, `shots-10/S01.png`); 0 lỗi console, 0 request hỏng, 0 `.katex-error`. Ghi công MMDS vắng mặt là đúng theo quyết định người dùng 2026-11-08 (review-log dòng 365–367).

## Sửa deck theo bảng phát hiện 2026-11-13

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): sửa deck theo nguyên tắc deck mới và bảng phát hiện của mục "Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)", nội dung thống nhất theo ghi chú bài giảng. Bài 10 không có mục "Quyết định của người dùng (2026-11-13)"; căn cứ thêm là quyết định D10 của điều phối viên (S01 và ghi chú diễn giả T05 viết theo note:1376). Ghi chú bài giảng, `exercises.md`, CSS và deck khác không đổi.

**Tác tử.** Vai trò: tác tử sửa deck (writer), `no-ai-slop` chế độ Edit, tự kiểm theo `eval.md`. Loại, mô hình và effort do điều phối viên ghi từ lời gọi công cụ.

**Phạm vi thay đổi.** 105 trang trước và sau; không thêm, tách, gộp hay bỏ trang; mã trang giữ nguyên. 67 trang sửa (13 trang sửa mặt trang: P02, K02, H16, A14, A15, A21, A23, S01, G07, X01, X01B, X02, X04; các trang còn lại chỉ sửa ghi chú diễn giả). Một SVG mới, `img/lec-10/bai-10-12-cay-hoan-hao.svg` (X01), sinh bằng hàm `bai_10_12` thêm vào `generate_deck_svg.py`; 17 SVG cũ sinh lại trùng từng byte. Xuất xứ của bộ $(1,1,2)$ và các dữ kiện tự dựng khác đã ghi ở đợt A2 ("Nguồn gốc số liệu chuyển khỏi ghi chú"), nên không ghi lại.

| phát hiện | xử lý | trang | ghi chú |
|---|---|---|---|
| nghiêm trọng: S01, T05 khẳng định mọi mã ký hiệu trên hai ký hiệu dùng đúng 1 bit (2026-11-13) | sửa theo note:1376 và note:2016: S01 mặt trang "mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm, mã Huffman đúng 1 bit", ghi chú diễn giả S01 cùng câu; T05 câu 3 "mỗi từ mã dài ít nhất 1 bit, và mã Huffman trên hai ký hiệu có $\bar\ell=1$" | S01, T05 | đúng D10; S01 bỏ thêm câu "NG làm tròn thành sáu lần" (đính chính NG) và lời chú về thang của hình |
| trung bình: H16 ghi chú diễn giả $256\cdot255+1=65\,281$ (2026-11-13) | sửa thành $256\cdot254+1=65\,025$ như note:930; bỏ câu NG tr.52 "từ mã không dài quá 16 bit" | H16 | câu còn lại: phép co không bảo đảm từ mã dài không quá 16 bit, vì gốc có thể tới $65\,025$, vượt xa ngưỡng $4\,181$ |
| trung bình: P02 sáu mục tiêu so với bảy của ghi chú (2026-11-13) | viết lại P02 thành bảy mục tiêu đánh số như note:11–17, mỗi dòng 9–16 âm tiết, tổng 80 (đếm lại bằng script tách theo khoảng trắng, khớp `check_deck.py`); đánh lại số mục tiêu trong ghi chú diễn giả P02, T05, bản đồ mạch của `storyboard.md` và `outline.md` | P02, T05 | ngoại lệ 7 dòng ghi trong storyboard (77 → 80 âm tiết, 6 → 7 dòng). Mục tiêu 2 có "giải mã bằng cây", mục tiêu 5 có `ESCAPE`, `EOS`; các ý "lập bảng mã", "lá trọng số 0", "dựng lại", "hai phía cùng cây" của ghi chú không lên mặt trang vì trần 80; trang phục vụ: K04, K11 (mục tiêu 2), A15, A17, A18, A23 (mục tiêu 5) |
| trung bình: K05, G04, X03, A03 dẫn chiếu trỏ sai chỗ (2026-11-13) | K05 "Bài tập 10.10"; G04 "Ba trường hợp chuẩn hóa của Định nghĩa 10.36, dùng trong Thuật toán 10.37"; X03 "Bài tập 10.14", bỏ vế phần (d); A03 "Một phản ví dụ: lá A1, B1, C3, D3, … (NG, Hình 4.8)" theo note:976 | K05, G04, X03, A03 | theo G4 bỏ thêm mọi "của ghi chú", "của tệp bài tập" sau số bài tập (K21, H01, H17, A20, G15, T04, XT, X01, X04); `refcheck.py 10`: 128 đúng, 0 sai, không cụm cũ |
| trung bình: X02 nhãn "Quy ước:" cho quy tắc gán bit (2026-11-13) | hai quy tắc vào dòng đề: "Chạy Huffman tĩnh với phá hòa chọn D trước C, bit 0 cho nút lấy ra trước trong mỗi lượt." (19 âm tiết); bỏ dòng "Quy ước:"; nguồn "tr.32–37, 62–63"; ghi chú diễn giả "Quy tắc phá hòa theo NG, tr.35; quy tắc gán bit theo NG, tr.62–63, khác cách gán trên hình tr.35–36" | X02 | X02C không có câu "quy ước của ghi chú", không cần sửa; X02 63 → 62 âm tiết, 5 dòng |
| trung bình: HUFF.C, AHUFF.C, ARITH.C, NG làm chủ ngữ (2026-11-13) | mặt trang: H16 "Bảng chữ cái 257 ký hiệu", A14 bỏ "của AHUFF.C", A15 "Cây khởi tạo: hai lá trọng số 1, …", A21 "cài đặt dùng `unsigned long`", A23 "$W_{\max}=32\,768$", G07 "Kết thúc:"; ghi chú diễn giả P10 (hai quy tắc phá hòa như Bài tập 10.1), H06, H15, AT, A02, A04, A10, A13B, A17, A18, A21, A23, S03, S10, S11, G01, G04, G05, G09, G13, G15 viết "cài đặt", "bộ nén", "bộ mã thanh ghi", nguồn trong ngoặc | 25 trang | theo G1 bỏ luôn các chi tiết chương trình không có trong ghi chú: `totals`, `scale`, `underflow_bits`, `scale_counts`, phép toán bit `0x3fff`, cách lưu mảng nút (A04, A10), câu "bộ nén chậm nhất thế giới" (A01), câu lan truyền nhớ EE398A-3 (G04) |
| trung bình: câu đính chính NG trong ghi chú diễn giả (2026-11-13) | xóa ở K15, H04, H16, H17, A02, A23, S07, S10, G02, X01B, T06; thêm X03C (Hình 4.4 và lời văn), S01 ("sáu lần"), A06 (NG làm chủ ngữ) | 14 trang | số trên deck là số đúng của ghi chú; các đính chính nằm ở mục A2 (2026-11-11) của tệp này. K15 thay bằng hai nhầm lẫn của note:494 |
| nhẹ: câu xuất xứ và lời người soạn (2026-11-13) | K11 "Bộ $(1,1,2)$ cho ba ký hiệu"; H15 "Các số trong bảng là phép đếm theo giả mã."; P07 bỏ "Phản ví dụ CMU, trang chiếu 7.", câu nén mất thông tin theo ghi chú; T06 bỏ câu MMDS; X01 bỏ câu về đề CMU | K11, H15, P07, T06, X01 | G13 giữ "Các số trong bảng là phép đếm theo giả mã." |
| nhẹ: từ làm mềm (2026-11-13) | X04 "Entropy của mô hình là $H\approx1{,}157$ bit mỗi chữ."; P09 "nói về mô hình chứ không về bộ mã"; T03 "tỷ lệ nén khá chỉ đạt sau vài nghìn byte", "mã số học chậm hơn đáng kể" (theo note:1976) | X04, P09, T03 | thêm K19 bỏ "thường không tối ưu" |
| nhẹ: chỉ đường, câu lặp mặt trang (2026-11-13) | P00 bỏ "Câu luận đề nêu hai cận độ dài:"; P08, S02 bỏ câu chỉ đường; H05 "Mã 87 bit có độ dài $(1,3,3,3,3)$ nay dựng được từ số đếm."; H02 "vì $15-13=2$" | P00, P08, S02, H05, H02 | H02 không lặp nguyên dòng mặt trang như đề xuất, dùng phép trừ cho gọn; thêm K08, K19 bỏ câu chỉ đường |
| nhẹ: X01B nhãn "Bước 1–3" (2026-11-13) | nhãn theo `exercises.md`: "Tập lá của một từ mã:", "Các tập lá rời nhau:", "Đếm lá:" (không in đậm); ghi chú diễn giả và hướng dẫn chấm dùng cùng tên bước; thêm dòng kiểm tra $4+2+1+1=8=2^3$; bỏ câu đính chính lời giải CMU-A1 | X01B | mỗi dòng ≤ 18 âm tiết; 51 → 53 âm tiết |
| nhẹ: thiếu tên Anh (2026-11-13) | K02 mặt trang "còn gọi là prefix-free code hay mã tức thời (instantaneous code)"; P00 ghi chú diễn giả "nén không mất thông tin (lossless compression)"; K16 ghi chú diễn giả "còn gọi là expected code length" | K02, P00, K16 | K16: tên không lên mặt trang vì dòng định nghĩa sẽ 23 âm tiết (trần 20) |
| nhẹ: 23 trang ghi chú diễn giả trên 150 âm tiết (2026-11-13) | gọn còn ≤ 150 ở cả 23 trang (`check_deck.py`): P00 145, P02 149, P03 137, K05 145, K08 148, K11 141, K12 140, K16 142, K19 145, H11 141, H16 144, A04 137, A10 142, A17 144, A21 146, A23 145, S06 144, S10 128, S11 146, G11 149, T03 136, T04 146, T06 131 | 23 trang | phần cắt là câu nguồn, đính chính, tên chương trình, câu lặp mặt trang, câu chỉ đường; không chuyển nội dung sang ghi chú bài giảng (ghi chú đã có). Trên 150 còn K13 160, H12 155, X01B 152 (chứng minh, lời giải), A13B 239, A18 231 (chứng minh), A20 181, T05 240, X03C 163 (lời giải); đều ≤ 250 |
| nhẹ: S01 dòng thứ ba gộp hai ý (2026-11-13) | tách hai dòng: "Ảnh fax hai màu: mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm, mã Huffman đúng 1 bit." và "$1\,000$ ký hiệu xác suất $0{,}999$: $1{,}44$ bit, Huffman $1\,000$ bit." | S01 | 47 → 52 âm tiết, 5 dòng; ảnh 1600×900 đã xem: vừa khung |
| nhẹ: X01 không có hình (2026-11-13) | thêm `bai-10-12-cay-hoan-hao.svg`: cây hoàn hảo độ sâu 3, tám lá 000–111, bốn nút của mã `0`, `10`, `110`, `111` (dữ kiện ex:102) tô cam kèm viền dày; nhãn 20–23 đơn vị trong khung 1 200 × 270; `role="img"`, `<title>`, `<desc>`, `alt` cụ thể | X01 | hình chỉ nêu dữ kiện, không ghi số lá dưới mỗi từ mã để không lộ lời giải |

**Kiểm (G17).** Máy chủ của điều phối viên, cổng 8796. `check_deck.py`: 105 trang, 0 lỗi console/trang, 0 request hỏng, 0 request ngoài, 0 `.katex-error` ở 1600×900 và 390×844, `overflow_1600` rỗng, `hscroll_390` false, `disp_gt3` rỗng, 0 `fragment`, `style_blocks=1` (thẻ runtime), `hash_strand` đúng `#/2…7` → KT, HT, AT, ST, TT, XT. Trang trên 60 âm tiết: P02 80, P04B 63, H15 63, G13 67, T02 80, T03 74, T05 69, X02 62, đều có ngoại lệ trong storyboard. `refcheck.py 10`: 128 đúng, 0 sai. `git diff --check`: sạch. Ảnh đã xem: P02, S01, X01, X01B, X02, A15, A21 (1600×900), X01 (390×844).

### Lượt sửa sau kiểm lại (2026-11-13)

Căn cứ: danh sách đã duyệt của điều phối viên sau hai lượt kiểm lại (1 trung bình, 8 nhẹ). Cùng phạm vi ghi; không commit.

| mục | xử lý | trang |
|---|---|---|
| 1 (trung bình) phép co ở A23 viết như thể làm tròn lên mất tính chất anh em | ghi chú diễn giả theo Bài tập 10.5 (note:1358–1370): "Phép co làm tròn lên, nên không lá dương nào về 0 (NG, mã nguồn, tr.85). Với phép chia đôi bỏ phần lẻ, A3, B3, C6, D6 thành A1, B1, C3, D3; giữ hình dạng cũ thì mất tính chất anh em. Phép làm tròn lên cho A2, B2, C3, D3 và giữ được tính chất đó trên cây này (Bài tập 10.5). Cây vẫn được dựng lại sau phép co." | A23 |
| 2 mục tiêu 5 nêu điều được chứng minh | "Chạy Huffman thích nghi; chứng minh tăng–đổi giữ tính chất anh em." | P02 |
| 3 mục tiêu 1 "mọi thông điệp", mục tiêu 6 "dài dưới" | "Đặc tả nén; chứng minh không mã nào rút ngắn mọi thông điệp."; "Mã hóa, giải mã bằng khoảng; chuỗi bit dài dưới $I(x)+2$." | P02 |
| 4 K19 "Do đó" nối sai | "Mã tiền tố tối ưu không dài hơn mã của định lý, nên cũng có $\bar\ell<H(P)+1$." | K19 |
| 5 X01B thiếu vế lập luận | ghi chú diễn giả: "một lá có hai tiền tố $c(s)$, $c(s')$ thì từ mã ngắn hơn là tiền tố của từ mã dài hơn" (ex:96) | X01B |
| 6 mục tiêu 7 khôi phục "chọn cặp mô hình–bộ mã" | "Chạy mã số học 16 bit, bit chờ; giải thích $N\le2^{R-2}$; chọn cặp mô hình–bộ mã." Mục 2–3–6 cùng giữ trần: bảy dòng 13, 12, 9, 10, 12, 10, 14 = 80 âm tiết (đếm tay bằng script tách theo khoảng trắng, khớp `check_deck.py`). Để vừa 80, "tách mô hình–bộ mã" (mục 1, nay nằm trong "chọn cặp mô hình–bộ mã" của mục 7), "đầu mục" (mục 4) và `ESCAPE`, `EOS` (mục 5) chuyển xuống ghi chú diễn giả P02 | P02 |
| 7 H15 câu quét mảng | "Một cài đặt quét mảng nút thay cho đống để tìm hai nút nhẹ nhất: $O(k)$ mỗi lượt, $O(k^2)$ cho cả cây (NG, tr.54, 62)" | H15 |
| 8 A21 thứ tràn là biến tích bit | mặt trang theo note:1312: "Nếu từ mã được tích trong số nguyên 16 bit, gốc $4\,181=\mathrm{fib}(18)$ đã có thể cho từ mã 17 bit gây tràn." (19 âm tiết, một dòng ở 1600×900); `unsigned long` chỉ còn trong ghi chú diễn giả | A21 |
| 9 lời người soạn và mục lỗi thời | P02 ghi chú diễn giả bỏ "Bảy mục tiêu đánh số như ghi chú"; P07 "Nén mất thông tin (lossy compression) chỉ yêu cầu bản khôi phục gần bản gốc (NG, tr.18–19)."; storyboard (mục Đọc thêm) và outline (Ngoài phạm vi) bỏ `scale_counts`, cách lưu mảng của AHUFF.C, quy ước bit trong lời văn NG. Bài tập 10.15 (X04) thêm vào ánh xạ **mục tiêu 3** trong ghi chú diễn giả P02 và outline, vì `exercises.md` xếp 10.15 ở mục tiêu 3 và 6 (dòng 11, 14), không ở mục tiêu 5 (Huffman thích nghi) | P02, P07 |

**Kiểm lại (G17).** `check_deck.py` (cổng 8796): 105 trang, 0 lỗi console/trang, 0 request hỏng hoặc ngoài, 0 `.katex-error` ở 1600×900 và 390×844, `overflow_1600` rỗng, `hscroll_390` false, `hash_strand` đúng `#/2…7`; trên 60: P02 80, P04B 63, H15 63, G13 67, T02 80, T03 74, T05 69, X02 62 (đều có ngoại lệ). Ghi chú diễn giả: P02 151, K19 133, A23 148, H15 98, X01B 175 (lời giải). A21 60 âm tiết. `refcheck.py 10`: 128 đúng, 0 sai. `git diff --check` trên deck và `planning/lec-10/`: sạch. Ảnh đã xem: P02, A21 (1600×900).

### Kiểm lại và duyệt của điều phối viên (2026-11-13)

**Tác tử (theo lời gọi công cụ).** Sửa deck: `general-purpose`, `opus` (Opus 5.5), effort `high`, `no-ai-slop` chế độ Edit; lượt sửa sau kiểm lại do cùng tác tử (tiếp tục bằng `SendMessage`). Kiểm lại vai A (độ chính xác và khớp ghi chú) và vai B (mạch, cấu trúc, văn phong, `no-ai-slop` Detect): mỗi vai một tác tử `general-purpose`, `opus` (Opus 5.5), effort `high`, chỉ đọc.

| vai | kết luận | phát hiện (chặn/nghiêm trọng/trung bình/nhẹ) | quyết định |
|---|---|---|---|
| A | cần sửa | 0/0/1/4 | chấp nhận; điều phối viên kiểm A23 với Bài tập 10.5 (note:1358–1370): phép co làm tròn lên giữ tính chất anh em trên cây A3, B3, C6, D6; phản ví dụ thuộc phép chia đôi bỏ phần lẻ. Năm mục vào `merge-10.md` (mục 1–5) |
| B | đạt | 0/0/0/6 | chấp nhận; bốn mục vào `merge-10.md` (mục 6–9) |

Lượt sửa sau kiểm lại: 9/9 mục làm; X04 (Bài tập 10.15) gắn mục tiêu 3 theo `exercises.md`:11, 14 thay cho mục tiêu 5 của danh sách — chấp nhận. Ghi chú diễn giả P02 151 âm tiết (vượt mức 150 một âm tiết, nhẹ) — chấp nhận.

Kiểm của điều phối viên sau lượt sửa: `check_deck.py` (Playwright, 1600×900 và 390×844) 105 trang, ID không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, 0 `.katex-error`, không tràn khung, không cuộn ngang ở 390 px, `#/2…7` mở đúng `mach-2…7`; tám trang trên 60 âm tiết đều thuộc loại trần 80 hoặc có ngoại lệ trong storyboard (P02 80, P04B 63, H15 63, G13 67, T02 80, T03 74, T05 69, X02 62). `refcheck.py`: 128 dẫn chiếu `10.k`, 0 sai. `git diff --check` sạch. Điều phối viên tự xem ảnh X01 (hình mới `bai-10-12-cay-hoan-hao.svg`) ở 1600×900 và đọc lại câu A23 sau sửa.

Quyết định: **chấp nhận**; mọi phát hiện của bảng 2026-11-13 đã đóng.
