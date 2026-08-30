# Nhật ký rà soát Bài 11

## Trạng thái sau lượt chỉnh sửa độc lập

- HTML: `2627-1/lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html`.
- Cấu trúc giữ 48 trang, 7 mạch ngoài; phần giảng 120 phút và recitation 60 phút.
- `2627-1/index.html` đã có liên kết đúng đến bài 11; không cần sửa.
- Đã có kiểm định storyboard, năm báo cáo độc lập, rà lại toán học và mạch viết, kiểm tra tĩnh cùng QA RevealJS cục bộ. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` đã được xử lý.

## Báo cáo lập kế hoạch

Tác tử lập kế hoạch đề nghị sửa cục bộ, giữ 48 trang và 7 mạch. Rủi ro chính: dữ kiện SVG tự dựng, quy ước kết thúc LZ78, chính sách độ rộng LZW, nguồn JPEG, mã nội bộ trong notes và chữ nhỏ.

## Báo cáo phân tích nguồn và quyết định

| Mức độ | Trang hoặc tài sản | Vấn đề | Quyết định đã triển khai |
|---|---|---|---|
| chặn bàn giao | X05 | Yêu cầu không khớp CMU lossy logic 11 | Khôi phục ba mục tiêu biến đổi; hỏi nhược điểm của cosine/Fourier toàn ảnh và cách chia khối để khắc phục. |
| chặn bàn giao | `lz78-trie.svg`, `lz78-roundtrip.svg` | Gán sai $D[2]$ và $D[4]$ | Sửa thành $D[2]=ab,D[4]=c$. |
| chặn bàn giao | `quantization.svg` | Ma trận số tự đặt | Thay bằng hai ô số truy nguyên từ Nelson–Gailly Hình 11.10–11.11, PDF tr. 260–261. |
| chặn bàn giao | `zigzag.svg` | Đường quét không bảo đảm đủ 64 vị trí | Vẽ lại thứ tự zigzag chuẩn qua đủ 64 tâm ô. |
| nghiêm trọng | W06 | Quy tắc đổi độ rộng sau $2^b-1$ không có nguồn | Công bố $T=2^b$ và `MAX`, nhưng để định dạng chốt riêng mốc đổi của bộ mã hóa và bộ giải mã theo early/late-change; dẫn biến thể 12 bit của sách trong notes. |
| nghiêm trọng | Z03–Z04 | Nhầm điều kiện token cuối và thiếu hợp đồng đóng khung | Nêu token thường có thể là token cuối; `(i,EOS)` chỉ dùng khi nguồn hết ngay sau cụm đã biết; bổ sung điều kiện dừng và quy nạp. |
| nghiêm trọng | J00–J11 | Nguồn JPEG và tuyên bố mất dữ liệu chưa chính xác | Chỉ dùng Chương 11; dùng RMS ở PDF tr. 266; dẫn dịch mức ở tr. 268; nói lượng tử không khả nghịch nói chung. |
| nghiêm trọng | L05, L09 và ba SVG LZ77 | Dữ kiện chồng lấn tự dựng | Thay bằng trạng thái CMU với token `(3,4,b)`. |
| nghiêm trọng | Notes | Có mã trang nội bộ và thời lượng | Xóa mã nội bộ và thời lượng khỏi toàn bộ notes; giữ nguồn, chuyển ý và đáp án. |
| trung bình | HTML | Khóa phóng to và chữ phụ dưới chuẩn | Bỏ `maximum-scale`, `user-scalable=no`; tăng cỡ nền và đặt `.small`, `.tiny`, code, bảng để cỡ hiệu dụng không dưới `.75em`. |
| trung bình | X00, index | Ghi “chờ phê duyệt”, báo sai trạng thái index | Bỏ trạng thái chờ; xác nhận index đã có liên kết đúng. |

## Quyết định kỹ thuật

- LZ77 sao chép tuần tự từ trái sang phải; ký tự vừa sinh có thể làm nguồn.
- LZ78 giả sử dòng cặp được đóng khung và EOS nằm ngoài bảng chữ cái.
- LZW giữ bất biến độ trễ một mục: mọi mã nhỏ hơn `next_code` trùng ở hai phía; bộ mã hóa có thể đi trước đúng mục `next_code`. Vì vậy mã chưa có chỉ hợp lệ khi `k = next_code`.
- Vết LZW là dòng mã nguyên đóng khung, không dành mã 256 cho EOS. Định dạng bit hữu hạn phân biệt $T=2^b$ với `MAX`, công bố riêng mã đầu tiên bộ mã hóa ghi bằng $b+1$ bit và mốc bộ giải mã đổi trước khi đọc theo early/late-change; tại `MAX` thì freeze hoặc reset có tín hiệu.
- Lượng tử hóa JPEG là ánh xạ nhiều-một nói chung, nhưng một đầu vào riêng lẻ vẫn có thể tái tạo đúng.
- Zigzag, mã độ dài loạt và mã entropy không làm mất thêm thông tin so với hệ số đã lượng tử.

## Ảnh hưởng của kỹ năng biên tập

- `no-ai-slop`: cắt lời dẫn quy trình, câu tổng kết lặp và diễn đạt phô trương; không thêm ví dụ hoặc số liệu ngoài nguồn. Bản hiển thị và notes đã được tự kiểm theo `eval.md`.
- Quill: rà mạch bảy phần, giữ thứ tự vết chạy trước giả mã, thống nhất $d,\ell,c$, $D[i]$, `next_code`, $C,Q,\hat C,\tilde C$ và cầu nối LZ78 sang LZW. Không tạo `quill.json`.

## Kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | W03–W05, X04 | Bất biến “hai từ điển giống nhau” sai tại ranh giới mã | Bộ mã hóa có thể đã thêm đúng một mục mà bộ giải mã chưa thể suy ra trước khi đọc mã kế | Dùng bất biến độ trễ một mục; phân loại $k<next$, $k=next$, $k>next$. Đã áp dụng. |
| nghiêm trọng | J03, J05, X05 | Bài tập đưa ba mục tiêu biến đổi và giới hạn xử lý toàn ảnh trước khi phần giảng thiết lập | Kiến thức cần cho X05 chỉ nằm trong bài tập | Đưa cầu nối nguồn-backed vào J03–J05, giữ cảnh báo về mô hình tính trực tiếp. Đã áp dụng. |
| trung bình | S01 | Câu kiểm tra chỉ ghép dấu hiệu với tên thuật toán | Không buộc cân nhắc hợp đồng hoặc loại phương án | Đổi thành tình huống kho ảnh có ràng buộc; yêu cầu chọn, nêu lý do và loại ít nhất một phương án. Đã áp dụng. |
| trung bình | X02 | Ký hiệu 2 có thể bị đọc như khoảng lùi $d$ | Phần giảng dùng $(d,\ell,c)$, bài CMU dùng vị trí tuyệt đối | Đổi sang $(p,\ell,c)$, đặt hộp so sánh và buộc phát biểu quy ước. Đã áp dụng. |

Kiểm định xác nhận 48 trang, 7 mạch, phần giảng 120 phút và recitation 60 phút. Recitation dùng đúng nguồn đã chỉ định, bao phủ mục tiêu 1–3, 5 và một phần mục tiêu 4; không thêm bài ngoài nguồn để lấp khoảng trống.

## Năm báo cáo độc lập

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | W02–W03 | Vết LZW thiếu ánh xạ ký tự sang mã | Mã 112–114 xuất hiện trước khi người học biết tương ứng với $p,q,r$ | Hiển thị $p\mapsto112,q\mapsto113,r\mapsto114$ và `next_code=256`; ghi lý do đổi chữ trong notes. Đã áp dụng. |
| trung bình | `lzw-trace.svg`, `jpeg-pipeline.svg`, `zigzag.svg` | Chữ trong hình nhỏ | Cỡ chữ 17–18 px ở hình chiếu lớn | Tăng lên 20 px, rút nhãn khi cần. Đã áp dụng và xác nhận bằng QA trực quan. |
| trung bình | J01, J07, J10 | Quan hệ tốc độ bit–sai số còn rời rạc | Các trang nói riêng kích thước hoặc RMS | Nối bằng mệnh đề có điều kiện: lượng tử mạnh thường giảm kích thước và tăng sai số, không có tỷ lệ cố định. Đã áp dụng. |

### Chuyên gia giải thuật và khoa học dữ liệu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | W00–W06 | Trộn mô hình dòng mã nguyên với biến thể mã hữu hạn | Mã 256 vừa là mục đầu vừa có nguy cơ bị hiểu là EOS; chính sách đầy chưa đóng | Công bố dòng mã nguyên đóng khung, không EOS; tách $T=2^b$ khỏi `MAX`, công bố hai mốc đổi độ rộng theo early/late-change, rồi freeze/reset tại `MAX`. Đã áp dụng. |
| nghiêm trọng | S00 | Bảng kết luận thiếu điều kiện tiết kiệm bit và chi phí trạng thái | Chỉ nêu nguồn lặp, trạng thái, khôi phục | So sánh thêm khi tham chiếu/mã cụm có lợi và tiêu chí tốc độ bit–sai số. Đã áp dụng. |
| trung bình | W06 | Thiếu mô hình chi phí LZW | Chỉ có $O(M)$ bộ nhớ | Thêm mã hóa kỳ vọng $O(n)$ với băm kỳ vọng $O(1)$, giải mã $O(n)$ theo đầu ra, $O(M)$ từ máy. Đã áp dụng cùng giả thiết. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| chặn bàn giao | W05, X04 | Bất biến đồng bộ LZW sai | Bộ mã hóa có thể đi trước bộ giải mã đúng một mục | Thay toàn bộ bằng bất biến độ trễ một mục và yêu cầu rà lại toán học. Đã áp dụng; kiểm định cuối phải rà lại. |
| nghiêm trọng | W06 | Ngưỡng đổi độ rộng và giới hạn cuối bị gộp; mốc đổi cục bộ bỏ qua độ trễ một mục | $T=2^b$ là biên biểu diễn hiện tại, `MAX` là giới hạn cuối; `next_code` của hai phía có thể lệch một mục | Không áp một điều kiện cục bộ cho cả hai phía. Định dạng công bố mã đầu tiên encoder ghi bằng $b+1$ bit và mốc decoder đổi trước khi đọc theo early/late-change; tại `MAX` thì freeze hoặc reset có tín hiệu. Đã áp dụng sau rà toán học. |
| nghiêm trọng | J06, J08, J11 | Thiếu phép lượng tử số và không truyền trạng thái sang zigzag | Hình chỉ có ký hiệu, câu kiểm tra chỉ phân loại bước | Dùng hai ô an toàn từ sách: $(-9,7)\to-1\to-7$ và $(3,11)\to0\to0$; nối lượt zigzag 6, 15 và DC/AC. Đã áp dụng. |
| nghiêm trọng | L06–L07 | EOS chưa bị giới hạn ở token cuối | Bộ giải mã có thể dừng giữa dòng token | Thêm `require đây là token cuối` và dùng giả thiết này trong chứng minh. Đã áp dụng. |

### Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | J03–J06, X05 | Hình thức DCT có trước cầu nối đầy đủ tới mục tiêu biến đổi và chia khối | Người học chưa có lý do chọn biến đổi cục bộ | Nêu ba mục tiêu ở J03, lợi ích và rủi ro chia khối, rồi mới trực giác và công thức. Đã áp dụng, không đổi thứ tự trang. |
| trung bình | J08 | DC sai phân thiếu miền dự đoán | “khối trước” có thể bị hiểu là khác thành phần | Ghi “khối trước cùng thành phần theo thứ tự quét”; restart chỉ để trong notes. Đã áp dụng. |
| trung bình | J11 | Kiểm tra chưa buộc thực hiện phép tính | Chỉ hỏi bước nào khả nghịch | Yêu cầu tính ô $(0,2)$ rồi nối sang lượt zigzag và DC/AC. Đã áp dụng. |

### Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | W07 → J00 | Vai trò trong mạch: kết thúc LZW nhưng chưa đóng hai hợp đồng; kết nối vào là mã chưa có, kết nối ra JPEG đột ngột | Notes thiếu câu thu hồi hợp đồng khôi phục đúng và mở hợp đồng gần đúng | Thêm câu nối từ hợp đồng LZ sang tốc độ bit–sai số JPEG. Đã áp dụng. |
| trung bình | S00–S01 | Vai trò trong mạch: kết luận; kết nối vào bốn thuật toán, kết nối ra bài tập. Tuyến chỉ gọi tên, chưa buộc quyết định | Bảng và câu hỏi có thể trả lời bằng ghép từ khóa | Sửa bảng theo điều kiện/chi phí và đổi câu hỏi thành lựa chọn có loại phương án. Đã áp dụng. |
| nhẹ | Toàn bài | Một số notes dùng câu nối máy móc | Cụm “Câu nối:” lặp | Giữ nội dung chuyển ý nhưng viết thành mạch nói ngắn. Đã áp dụng ở các trang sửa. |

## Đề xuất không áp dụng

- Không thêm thời lượng vào ghi chú diễn giả. Quy định của bài cấm hiển thị thời lượng trong notes; thời lượng vẫn được ghi đầy đủ trong storyboard.
- Không thêm bài recitation mới để bao phủ trọn mục tiêu 4 vì bài tập phải lấy trực tiếp từ nguồn đã chỉ định.
- Không tách thêm trang cho SVG chữ nhỏ; 48 trang và nhịp 120+60 vẫn phù hợp. Tăng cỡ chữ và rút nhãn đã đủ sau QA trực quan.

## Sửa sau QA trực quan

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | J08 | Nội dung bị cắt và đè chân trang ở cả khung rộng lẫn hẹp | Detector tràn không phát hiện, nhưng ảnh chụp QA cho thấy phần cuối trang không còn khoảng an toàn | Giảm hình zigzag xuống 245 px, gộp DC/AC thành hai dòng gọn và bỏ dòng mặt trang lặp lượt 6/15 đã có trong SVG. QA2 ở cả hai khung xác nhận nội dung và chân trang nhìn rõ, không bị cắt. |

## Kiểm định cuối

### Rà lại nội dung

- Tác tử độ chính xác toán học và thuật toán rà lại W06 sau khi tách $T=2^b$, `MAX` và hai mốc early/late-change: `PASS`.
- Tác tử kết nối và mạch viết rà lại toàn bộ bộ trang chiếu: `PASS`; bảy mạch ngoài nối được từ mở bài qua ba họ LZ, JPEG, kết luận và recitation.

### Máy chủ và QA RevealJS

- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại với thông báo `/usr/bin/python3: No module named reloadserver`.
- Máy chủ dự phòng `/tmp/reloadserver.py 8765` phục vụ trang cục bộ thành công.
- Chromium QA2 duyệt đủ 48 trang ở $1280\times720$ và $800\times600$. Cả hai lượt trả `errors=[]`, `katex=0`, `overflow=[]`.
- Kiểm tra bàn phím đạt: trạng thái đầu `(0,0)`; `ArrowRight` tới `(1,0)`; `ArrowDown` tới `(1,1)`.
- Đã xem contact sheet và từng trang có rủi ro. J08 ban đầu đè chân trang; sau khi thu gọn, ảnh QA2 ở cả khung rộng và hẹp cho thấy toàn bộ nội dung cùng chân trang, không bị cắt.

### Codex Slides và chỉ mục

- Dự án Codex Slides `20260827233040-b-i-11-n-n-b-ng-t-i-n-v-n-n-m-t-d-li-u-j6kj` ở trạng thái `draft`, có 0 slide. HTML hiện tại được tải lên dưới dạng material `20260830152855800-pkzz.html`.
- Lệnh mở workspace trả về URL tài nguyên, nhưng phiên này không có khả năng điều hướng Browser trong trình biên tập hoặc xem canvas. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; QA trực quan RevealJS cục bộ đã hoàn tất.
- Liên kết Bài 11 trong `2627-1/index.html` đúng. Không cần sửa tệp chỉ mục.
- Chưa commit hoặc đẩy lên kho từ xa tại thời điểm ghi nhật ký này.

## Kiểm tra tĩnh sau chỉnh sửa

- HTML có 48 mã trang duy nhất, 7 `<section>` ngoài và 48 khối notes.
- Storyboard chứa đủ 48 mã trang; notes không còn mã nội bộ hoặc thời lượng.
- Cả 12 SVG, kể cả hình không được nhúng, phân tích XML hợp lệ và có `role="img"`, `aria-label`; cỡ chữ chính từ 20 px trở lên.
- Đường zigzag có 64 điểm; hai ô ví dụ ở lượt 6 và 15. Mọi ảnh HTML tồn tại; không có raster hoặc URL mạng trong nội dung.
- Notes không có mã nội bộ hoặc thời lượng. `git diff --check` không báo lỗi khoảng trắng.
