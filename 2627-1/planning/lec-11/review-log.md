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

## Ghi chú tự học Bài 11

### Điều phối OpenRouter

- Ba reader dùng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch phiên `33029`, bản đồ chủ đề phiên `61360`, ánh xạ nguồn phiên `19586`. Codex chính hợp nhất thành 11 chủ đề `L11-N01`–`L11-N11`; giữ recitation là đầu ra cốt lõi, mã 256 là mục LZW mới đầu tiên và vị trí zigzag đếm từ 1.
- Writer dùng `deepseek/deepseek-v4-flash-0731`. Phiên `89667` chạm giới hạn gọi công cụ trước khi ghi; phiên thu hẹp `86654` hoàn tất bản nháp trong gốc tạm. Codex chính chỉ đưa tệp cần thiết vào gốc tạm, không gửi `.env`, bí mật hoặc thông tin xác thực.
- Năm reviewer độc lập dùng `z-ai/glm-5.3-flash`: truy nguyên nguồn `5012`, toán–thuật toán `22223`, sư phạm `58467`, mạch viết `51407`, viewer `4502`. Các lỗi có căn cứ đã được sửa trước tái kiểm.

### Phát hiện và quyết định

| Mức | Phát hiện | Quyết định |
|---|---|---|
| nghiêm trọng | Bản nháp có khối tùy biến và hàng rào mã bị hỏng, ký hiệu KaTeX lỗi, hai dấu vết nội bộ và lời giải lạc vị trí | Chuyển thành 10 bộ `exercise`–`hint`–`solution` hợp lệ, sửa bảy khối mã, công thức và xóa toàn bộ dấu vết quy trình |
| nghiêm trọng | Bảng trạng thái LZ77 không khớp năm token | Sửa các tiền tố đã xử lý thành `aac`, `aacaacab`, `aacaacabcaba`; chạy lại giải mã |
| trung bình | Bảng LZ78 ghi tiền tố hàng cuối là `b` dù dùng $D[5]=abc$ | Sửa thành `abcb`; giữ cặp $(5,b)$ và $D[6]=abcb$ |
| trung bình | Ghi chú chưa dùng hai hình khứ hồi LZ77/LZ78 | Chèn hai SVG đúng tại phần chứng minh tương ứng; cả 12 SVG của bài được dùng |
| nhẹ | Một số câu mang giọng hướng dẫn quy trình hoặc lặp cảnh báo | Biên tập lại theo `$no-ai-slop`: giữ mệnh đề, bỏ nhãn quy trình và nhịp câu máy móc |

Hai nhận xét bị bác bỏ sau kiểm chứng độc lập:

- Reviewer mạch cho rằng dòng mã LZW không khớp. Chạy lại thuật toán trên toàn chuỗi `ppqpprpqrpqrq` cho đúng 10 mã `112,112,113,256,114,257,260,113,114,113` và các mục 256–264 `pp,pq,qp,ppr,rp,pqr,rpq,qr,rq`; reviewer toán phiên `22223` cũng xác nhận.
- Reviewer viewer đề nghị đổi đường hình thành `../../img/...`. Viewer giải đường dẫn từ gốc `2627-1/`, nên dạng đúng là `img/lec-11/...`; kiểm thử trình duyệt tải đủ 13 lần dùng ảnh, không có ảnh hỏng.

### Biên tập và tính liên tục

- `$no-ai-slop`: đổi lời dẫn và cảnh báo thành văn xuôi học thuật, bỏ các nhãn như “nguồn ghép”, “ghi chú quan trọng”, “phép tính bắt buộc”, không thêm mệnh đề hoặc ví dụ mới. Bản cuối được tự kiểm theo `eval.md`.
- `$quill`: mạch `N01→N02→N03→N04→N05→N06` và `N01→N07→N08→N09` hội tụ ở `N10→N11`; ký hiệu $(d,\ell,c)$ và $(p,\ell,c)$ không trộn, $EOS$, $D[i]$, `next_code`, $C$, $Q$, $\hat C$, $\tilde C$ nhất quán. Không tạo `quill.json`.

### Kiểm định viewer và index

- Viewer thật ở khung $1280\times720$ và $390\times844$: 51 heading khớp 51 liên kết mục lục, 198 biểu thức KaTeX, không lỗi KaTeX, 13 lần dùng ảnh không hỏng, bảy khối mã có ngôn ngữ, 20 khối gập đóng mặc định, không tràn ngang hoặc lỗi trình duyệt.
- Bàn phím đạt cho liên kết bỏ qua nội dung và `summary`; bản in A4 dài 24 trang, tự mở mọi `hint`/`solution`, ẩn mục lục và thanh thao tác, không có hình vượt khung.
- Viewer từ chối đường dẫn vượt thư mục và từ chối ghép `doc` Bài 10 với `deck` Bài 11.
- Sau khi viewer đạt, index được đổi sang hai tài nguyên Trang chiếu/Ghi chú. Kiểm thử từ index ở hai khung xác nhận đúng một liên kết, nhận focus bàn phím, mở đúng tài liệu, 13 ảnh và không lỗi KaTeX.

### Tái kiểm cuối

- Phiên toán–thuật toán `39844` hết thời gian chờ API và không cho kết luận. Lần thử lại thu hẹp ở phiên `83111` dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter: `PASS` 9/9 cho LZ77, LZ78, LZW, DCT/IDCT, lượng tử, zigzag, RMS, chi phí và năm lời giải.
- Reviewer mạch sư phạm phiên `91975` dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter: `PASS`; xác nhận thứ tự N01–N11, các cầu nối, ký hiệu, EOS, mã 256, độ trễ LZW, ranh giới mất dữ liệu JPEG và văn phong công khai.

## Vòng đồng bộ deck với ghi chú — 2026-09-02

- Reader kế hoạch dùng các phiên `35623`, `28920`; reader nguồn dùng phiên `73243`. Các phiên hợp lệ đều chạy `z-ai/glm-5.3-flash` qua OpenRouter và giữ nguyên 48 trang, 7 mạch, 42+6 trang, 120+60 phút, 12 SVG cùng toàn bộ nội dung toán–thuật toán.
- Writer được gọi đúng `deepseek/deepseek-v4-flash-0731` trên dossier hẹp ở exec session `5667`. Worker đọc đủ mục cần sửa nhưng bị dừng sau hơn bốn phút chờ API, trước khi ghi tệp; không có JSON kết thúc để xác nhận model quan sát/provider. Theo quyền người dùng đã cấp, Codex áp dụng trực tiếp đúng delta hai reader phê duyệt.
- Index Bài 11 dùng nhãn `Bài giảng`, `Ghi chú bài giảng` và `aria-label="Tài nguyên Bài 11"`. Ghi chú §5.2 gộp hai đoạn lặp về DCT, lượng tử hóa và zigzag. Speaker notes P02, L00, L02, L04, W07 được viết trực tiếp hơn, không đổi mệnh đề hoặc nguồn.
- `$no-ai-slop/eval.md`: đạt ở phạm vi sửa. Quill: trật tự và ký hiệu LZ77→LZ78→LZW→JPEG giữ nguyên; không tạo `quill.json`.

### Năm phản biện và kiểm định cuối vòng đồng bộ

- Nguồn/truy nguyên `19464`, toán–thuật toán `72022`, sư phạm/sinh viên `93254`, văn phong `37783` và kỹ thuật `17226` đều trả `GO`. Tất cả dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter, dossier dưới 40k token.
- Các phiên `52622`, `50924` chạm giới hạn công cụ; `43412`, `38313` hết thời gian API; `84288` bị dừng sau 247 giây không có kết luận. Các phiên này bị loại khỏi cổng. Không có lỗi chặn hoặc nghiêm trọng còn lại.
- Không đổi thứ tự L04 trước L03 vì chu trình trang chiếu chủ ý đưa ví dụ chạy tay trước hình thức hóa. Không sửa quy ước X02 vì mặt trang đã ghi rõ bài CMU dùng vị trí tuyệt đối, đánh số từ 0.
- Chromium duyệt đủ 48 trang ở $1280\times720$, $800\times600$ và $720\times900$: không tràn, lỗi JavaScript, lỗi KaTeX hoặc tài nguyên tải thất bại; điều hướng bàn phím và 48 speaker notes đạt. PDF deck có 48 trang.
- Viewer tải đúng tiêu đề, 51 heading, 41 liên kết mục lục, 198 biểu thức KaTeX không lỗi, 13 lượt hình và 20 khối gập đóng mặc định. Bản rộng/hẹp, bàn phím, bản in 24 trang, mở khối gập, từ chối vượt thư mục và từ chối cặp doc–deck khác bài đều đạt.
- Index có đúng một liên kết ghi chú Bài 11 và mở đúng deck/note, không lỗi console. Đã xem trực tiếp L04, W07 và bản viewer hẹp; bảng, công thức, SVG và văn bản đều rõ, không chồng hoặc cắt.
- Codex Slides project `20260827233040-b-i-11-n-n-b-ng-t-i-n-v-n-n-m-t-d-li-u-j6kj` vẫn là draft 0 slide. Không tuyên bố đã kiểm canvas; bằng chứng hiển thị cuối là RevealJS và viewer cục bộ bằng Chromium.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 2 gồm Bài 07–15; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`. Mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch nên dùng `<tiền tố>T`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | LT | Nén LZ77 với cửa sổ trượt | Muốn nén luồng lớn trong một lượt với bộ nhớ hữu hạn, phải thay cụm lặp gần bằng tham chiếu về cửa sổ. |
| 3 | ZT | Nén LZ78 với từ điển tăng dần | Muốn dùng lại cụm lặp cách xa nhau, phải giữ từ điển cụm tăng dần trong toàn luồng. |
| 4 | WT | Nén LZW | Muốn chỉ phát mã cụm, phải nạp sẵn bảng chữ cái và cho hai phía cùng dựng từ điển. |
| 5 | JT | Nén ảnh mất dữ liệu bằng JPEG | Muốn giảm dung lượng ảnh khi chấp nhận sai số, phải biến đổi khối sang tần số rồi lượng tử hóa. |
| 6 | ST | Tổng kết và tự kiểm tra | Muốn chọn phương pháp nén, phải đối chiếu hợp đồng khôi phục, chi phí trạng thái và điều kiện tiết kiệm bit. |
| 7 | XT | Bài tập vận dụng | Muốn kiểm các vết mã hóa và biến đổi, phải hoàn tất năm nhiệm vụ của CMU 15-499. |

Dòng dẫn 18–23 âm tiết; từ khóa 4–5 cụm; ghi chú diễn giả 78–98 âm tiết, viết từ nội dung các trang trong mạch. Số trang 48 → 55. Các trang nội dung đầu mạch (L00, Z00, W00, J00, S00, X00) đều có nội dung, không phải trang tiêu đề phần một dòng, và tiêu đề khác tên mạch; giữ nguyên.

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–7) ngay sau trang mục tiêu P01 (đứng ngay sau trang bìa), tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 36 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Tên mạch 5 là "Nén ảnh mất dữ liệu bằng JPEG" để khác tiêu đề trang J00 "JPEG mất dữ liệu dựa trên DCT". Mạch 6 đặt tên "Tổng kết và tự kiểm tra" theo `AGENTS.md`, vì phần S gồm bảng đối chiếu và câu hỏi chọn phương án.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Bài 11 còn khối `<style>` riêng và không mang lớp `.course-deck` (có từ trước, ngoài phạm vi). Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 62/62; 55 `data-slide-id` và 6 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/7` mở đúng trang tiêu đề mạch tương ứng (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 677 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng tên các mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 6 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Dựng lại theo nguyên tắc 2026-11 (bắt đầu 2026-11-19)

Căn cứ: `2627-1/planning/lec-11/prompt-xay-dung-bai-11.md`; người dùng chốt Q1–Q10 theo cột "Đề xuất" ngày 2026-11-19 (Q2–Q8 ghi vào `NGUYEN-TAC-HOC-PHAN.md`: GC-DSFA-2, GC-DSFA-3, GC-DSFA-13, NT-DSFA-10, NT-DSFA-11, NT-DSFA-12, VP-DSFA-8). Điều phối viên: Claude Opus 5.5 (`claude-opus-5-5`). Các mục cũ ở trên giữ nguyên làm lịch sử.

### Nhật ký tác tử

| Giai đoạn | Vai | Loại | Mô hình | Nỗ lực | Ghi tệp | Kết quả |
|---|---|---|---|---|---|---|
| I.1 | Lập kế hoạch (ghi `outline.md`) | general-purpose | opus (Claude Opus 5.5) | high | `outline.md` | chấp nhận, kèm quyết định D1–D13 (xem "Duyệt outline") |
| I.2 | Phân tích nguồn (chỉ đọc; báo cáo trong scratchpad) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận (xem "Duyệt phân tích nguồn") |
| I.4 | Soạn ghi chú và SVG (`no-ai-slop` Edit) | general-purpose | opus (Claude Opus 5.5) | high | `lecture-note.md`, `img/lec-11/`, script hình | chấp nhận làm bản đóng băng v1 (27 167 âm tiết, md5 `781229e7`) để rà |
| I.5 | Rà ghi chú: sinh viên năm 2 (chỉ đọc) | general-purpose | opus (Claude Opus 5.5) | high | không (báo cáo scratchpad) | chấp nhận báo cáo |
| I.5 | Rà ghi chú: độ chính xác toán và thuật toán (chỉ đọc) | general-purpose | opus (Claude Opus 5.5) | high | không (báo cáo scratchpad) | chấp nhận báo cáo |
| I.5 | Rà ghi chú: chuyên gia nén dữ liệu (chỉ đọc) | general-purpose | opus (Claude Opus 5.5) | high | không (báo cáo scratchpad) | chấp nhận báo cáo |
| I.5 | Rà ghi chú: sư phạm và văn phong (chỉ đọc, `no-ai-slop` Detect) | general-purpose | opus (Claude Opus 5.5) | high | không (báo cáo scratchpad) | chấp nhận báo cáo |
| I.5 | Rà ghi chú: mạch và móc nối (chỉ đọc) | general-purpose | opus (Claude Opus 5.5) | high | không (báo cáo scratchpad) | chấp nhận báo cáo |
| I.6 | Biên tập ghi chú (cùng tác tử I.4, tiếp tục bằng SendMessage; `no-ai-slop` Edit) | general-purpose | opus (Claude Opus 5.5) | high | `lecture-note.md`, `img/lec-11/note-*.svg`, script hình | xong, bản v2 md5 `3ab5a114` (29 990 âm tiết); chờ kiểm lại |
| I.6 | Kiểm lại: độ chính xác toán và thuật toán (cùng tác tử I.5, SendMessage) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận: 19/19 phát hiện I.5 đã sửa; mới 0 chặn, 0 nghiêm trọng, 2 trung bình, 5 nhẹ → lượt sửa 2 |
| I.6 | Kiểm lại: mạch và móc nối (cùng tác tử I.5, SendMessage) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận: TB1–TB10 đã sửa; mới 0/0/0, 4 nhẹ → lượt sửa 2 |
| I.6 | Biên tập lượt 2 và sửa câu gzip (cùng tác tử I.4) | general-purpose | opus (Claude Opus 5.5) | high | `lecture-note.md` | chấp nhận (v3 md5 `ae0d35e2`, 30 394 âm tiết; sửa câu gzip sau kiểm lại lần 2) |
| I.6 | Đồng bộ `outline.md` (cùng tác tử I.1) | general-purpose | opus (Claude Opus 5.5) | high | `outline.md` | chấp nhận; cập nhật lần 2 đóng R1–R3, D10 |
| II.1 | Chọn bài tập (chỉ đọc) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận (xem "Duyệt danh sách bài tập") |
| II.2 | Soạn `exercises.md` (`no-ai-slop` Edit) | general-purpose | opus (Claude Opus 5.5) | high | `exercises.md` | chấp nhận làm bản đóng băng v1 (md5 `f24f2fee`, 6 bài 11.12–11.17) |
| II.3 | Rà bài tập: thuật toán (cùng tác tử I.5, SendMessage) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận báo cáo (0/0/1/3) |
| II.3 | Rà bài tập: sư phạm và văn phong (cùng tác tử I.5, `no-ai-slop` Detect) | general-purpose | opus (Claude Opus 5.5) | high | không | chấp nhận báo cáo (0/1/4/7) |
| II.3 | Biên tập `exercises.md` (cùng tác tử II.2), hai lượt | general-purpose | opus (Claude Opus 5.5) | high | `exercises.md` | chấp nhận (md5 `d51a0647`) |
| III.1 | Lập storyboard (`no-ai-slop` Edit cho chữ mặt trang dự kiến) | general-purpose | opus (Claude Opus 5.5) | high | `storyboard.md` | đang chạy |

### Duyệt phân tích nguồn (I.2)

Quyết định: **chấp nhận**. Điều phối viên đã kiểm lại: (1) CMU `compression3-lz.pdf` trang chiếu 4 định nghĩa $p$ là "position of the longest match in the dictionary (relative to the cursor)", tức khoảng lùi; câu "bài CMU dùng vị trí tuyệt đối, đánh số từ 0" ở bản cũ (X02, Bài 2 cũ) sai, kết quả `abcdcdcdcdcdce` không đổi; Nelson–Gailly dùng chỉ số trong bộ đệm cửa sổ (PDF 175–176). (2) Hình 11.9 (PDF 258): tự tính $CPC^T$ trực chuẩn với dịch mức 128 cho hàng 0 là `186 -18 15 -9 23 -9 -14 -19`; hình in ô $(0,7)$ là 19, lỗi dấu của sách. Các phát hiện khác ghi nhận để lập kế hoạch:

- LZW độ rộng mã thay đổi ($T=2^b$, early/late change) không có trong nguồn được giao (Nelson–Gailly Chương 9 chỉ có LZW12 cố định 12 bit, 256 là END_OF_STREAM, mã đầu 257); bản dựng lại không đưa nội dung này vào phần chính (VP6).
- Chuỗi `ppqpprpqrpqrq` là chuỗi CMU `aabaacabcabcb` đổi nhãn; vết CMU không chạm nhánh `k = next_code`; cần ví dụ nguồn cho nhánh này (`abababa` hay chuỗi của sách) hoặc ghi lý do.
- Hình 11.11: văn bản nói làm tròn, chương trình và hình theo chia nguyên cắt về 0; ô $(1,3)$ in 11, đúng là −11. Ghi chú dùng làm tròn theo văn bản, chỉ chọn ô cho cùng kết quả ở cả hai cách; đính chính ghi ở đây, không ghi trong ghi chú (VP18).
- `(i,EOS)` của LZ78, restart marker, lấy mẫu thưa màu là quy ước không có trong nguồn trục (lấy mẫu thưa chỉ ở CMU lossy 14, 31).
- `assign1a` và Nelson–Gailly không có bài tập cho Bài 11; nguồn bài tập chỉ là các trang chiếu recitation CMU (BT-DSFA-2).

Báo cáo: scratchpad phiên `lec11-source-analysis.md`, script `lec11_traces.py` (không đưa vào repo).

### Duyệt outline (I.3)

Quyết định: **chấp nhận**, chờ người dùng duyệt theo Q10. Điều phối viên đã đọc mục 0–7 và 13–14 của `outline.md`, đối chiếu với báo cáo phân tích nguồn; số Hình 11.9 hàng 0 đã tự tính lại. Quyết định cho các điểm D của outline mục 13:

| Mã | Quyết định của điều phối viên | Lý do |
|---|---|---|
| D1 | Sáu mạch nội dung; storyboard được tách mạch 5 nếu quá tải | NT10, NT-DSFA-11 |
| D2 | Chấp nhận: một quy ước $(d,\ell,c)$ khoảng lùi; sửa câu sai về CMU | CMU-LZ tc. 4 (đã kiểm) |
| D3 | Chấp nhận mã byte thật 97–99; ghi đổi số ở đây khi soạn | mã $0..255$ là giá trị byte (NG tr. 220) |
| D4 | Chấp nhận lượng tử hóa cả khối Hình 11.9 với $q=2$, làm tròn; ô $(0,7)$ dùng $-19$ | phép tính của chương trên dữ liệu và công thức nguồn; khối duy nhất có điểm ảnh |
| D5 | Chấp nhận | LZ78 `(i,EOS)` dựa Nhận xét 10.4 |
| D6 | Chấp nhận: bỏ đổi độ rộng mã | không có nguồn (VP6) |
| D7 | Ví dụ chính là IWOMBAT (NG tr. 217); cho phép thêm vết tối thiểu `abababa` viết "Giả sử", vì nguồn không có vết đầy đủ chạm nhánh $k=\texttt{next\_code}$ và GC-DSFA-9 cần ví dụ chạy tay; nêu cho người dùng ở điểm dừng | GC10, GC-DSFA-9; nguồn gốc ghi ở đây (VP18) |
| D8, D9, D11, D13 | Chấp nhận như đề xuất | |
| D10 | Chấp nhận CMU-LZ tc. 7 làm bài của `exercises.md`, đề nêu $W=6$, $L=4$ của tc. 5, ghi chỉnh theo BT-DSFA-6 | prompt II.1 cho phép câu hỏi có trên hai bộ slide CMU |
| D12 | Dùng "hệ số AC" (định nghĩa tại chỗ là 63 hệ số còn lại); người soạn tìm nguồn dùng thuật ngữ, nếu không có thì vẫn giữ như tên gọi chuẩn | VP2 (ký hiệu chuẩn) |

### Năm báo cáo rà ghi chú trên bản đóng băng v1 (I.5)

Bản đóng băng: `lecture-note.md` md5 `781229e7fe9949bc18a9a6dec98efa85`, 27 167 âm tiết. Báo cáo đầy đủ ở scratchpad phiên (không đưa vào repo); bảng dưới tóm tắt số phát hiện và các phát hiện mức nghiêm trọng, đã được điều phối viên kiểm bằng chứng.

| Vai | Chặn bàn giao | Nghiêm trọng | Trung bình | Nhẹ |
|---|---:|---:|---:|---:|
| Sinh viên năm 2 | 0 | 3 | 8 | 20 |
| Độ chính xác toán và thuật toán | 0 | 0 | 3 | 15 |
| Chuyên gia nén dữ liệu | 0 | 1 | 7 | 19 |
| Sư phạm và văn phong (`no-ai-slop` Detect) | 0 | 1 | 14 | 26 |
| Mạch và móc nối | 0 | 0 | 10 | 19 |

| Mức độ | Vị trí | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|---|
| nghiêm trọng | Bảng ký hiệu dòng 37; $m$, $s$, $b$, $P$, $H$, $r$, $\alpha$, $\beta$, $x,y$ | Chữ mang nhiều nghĩa, trái câu "mỗi chữ giữ một nghĩa" (VP4, GC7) | $m$: số mẫu, số mã LZW, độ dài cụm, chỉ số Bổ đề 11.27; $s$ hai nghĩa trong Định nghĩa 11.32 | yêu cầu sửa (quyết định 1) |
| nghiêm trọng | Bài tập 11.1(c) | Đề hỏi vì sao "không thể", lời giải và Tình huống 11.1 chỉ ra cách làm được | dòng 171, 183, 1639 (điều phối viên đã đọc) | yêu cầu sửa (quyết định 2) |
| nghiêm trọng | dòng 152, 1657 | Mệnh đề 10.2 bị đọc thành "kéo dài một số đầu vào" | Mệnh đề 10.2 chỉ cho $\lvert\varphi(u)\rvert\ge n$ (điều phối viên đã đọc) | yêu cầu sửa (quyết định 3) |
| nghiêm trọng | Nhận xét 11.35, dòng 1486 | "64 lần so với 8 bit" trái nguồn | CMU-L trang chiếu 17: ".125 bits/pixel (factor of 200)", ảnh màu (điều phối viên đã xem) | yêu cầu sửa (quyết định 4) |

Các phát hiện trung bình và nhẹ được áp dụng theo bảng quyết định gửi biên tập viên (26 quyết định; bác bỏ: đề xuất ra bài `exercises.md` trên dữ liệu mới, trái BT-DSFA-1/2). Các trung bình chính: ghép cận làm tròn với số đo chương trình cắt thương của NG (Tình huống 11.1); giả thiết "không cụm nào khớp" không thể xảy ra (Tình huống 11.2); mã độ dài loạt theo cả ảnh thay vì theo khối như NG; "ảnh xám" thay vì ảnh VGA 256 màu (NG tr. 246); câu nối hai phía ở ranh giới 2→3, 3→4; kết luận Mục 6 sai về chi phí LZ77 và giả thiết; câu hỏi trung tâm chưa trả lời phần văn bản; tóm tắt thiếu số hiệu thuật toán; ba mục tiêu thiếu bài tập; thiếu ví dụ số trước Định nghĩa 11.29, 11.32.

### Kiểm lại sau biên tập (I.6)

| Mức độ | Vị trí (v2) | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|---|
| trung bình | dòng 1154, 1179 | Chữ cũ $m$, $x$ sót sau khi đổi ký hiệu | Bổ đề 11.27 dùng $\mu$; $x$ là chuỗi đầu vào | yêu cầu sửa |
| trung bình | Định nghĩa 11.32, Mệnh đề 11.33, Ví dụ 11.13, Thuật toán 11.34 | Bộ $(r,0)$ đóng khối gán cho NG; NG đếm loạt số 0 xuyên khối (tr. 267, 270–271) | vai thuật toán đọc mã `OutputCode` | yêu cầu sửa: ghi là quy ước của chương, một câu "Trong thực hành" mô tả chương trình NG |
| nhẹ | dòng 1012; Ví dụ 11.14; Tình huống 11.4; ký hiệu tại chỗ; độ phủ mục tiêu 2, 3, 6 | xem báo cáo kiểm lại | | yêu cầu sửa (lượt 2) |

Điều phối viên đã đối chiếu số đo Calgary của Tình huống 11.4 với CMU 15-499 `compression1-2.pdf` trang chiếu 10 (GZIP 2,59; LZ77 3,94 bit mỗi ký tự): khớp. Nguồn này cùng bộ slide CMU 15-499 của học phần (P8).

Kiểm lại lần 2 trên v3 (md5 `ae0d35e27658e9f39c76af7ed7895b41`): vai thuật toán 0/0/0/1 nhẹ (câu "mỗi bộ ba" mô tả sai định dạng gzip ở Tình huống 11.4; yêu cầu sửa, đã giao); vai mạch 0/0/0/0. Mọi phát hiện chặn bàn giao và nghiêm trọng của I.5 đã được giải quyết.

### Nguồn gốc số liệu và chỗ chỉnh so với sách (từ người soạn, VP18, BT8)

Bản đầy đủ do người soạn ghi; chép nguyên văn dưới đây để giữ trong repo. Mục 1–4 viết cho bản v1; các số đã đổi sau biên tập (Tình huống 11.2: 96 000 byte với $\ell=1$, cận phép so $\le2{,}1\cdot10^9$; cận chương trình NG 9,60 / 18,23 / 44,12; mã độ dài loạt theo khối, 31 bộ; $1/(1-\alpha)\approx4{,}25$) ghi ở mục 5–6 và là số hiện hành.

#### Bài 11 — Ghi chú của người soạn (giai đoạn I.4), để điều phối viên đưa vào review-log

Tệp ghi: `ds-foundation-algorithms/2627-1/materials/lec-11/lecture-note.md` (27167 âm tiết theo `wc -w`, 1752 dòng).
Script kiểm phép tính: `scratchpad/lec11_writer_checks.py` (đầu ra `lec11_writer_checks.out`); script hình: `tools/courses/ds-foundation-algorithms/2627-1/img/lec-11/generate_note_svg.py`.

#### 1. Nguồn gốc số liệu tự dựng (không có trong nguồn)

| Vị trí | Số liệu | Cách có |
|---|---|---|
| Mục 1.1, đoạn nhầm lẫn RMS | hai cách tái tạo cùng RMS 2 (64 điểm lệch 2; 4 điểm lệch 8) | "Giả sử", chương dựng |
| Ví dụ 11.1, Bài tập 11.1 | bit mỗi điểm 3,48; 2,30; 1,28; 0,90; 0,64 (CHEETAH), 2,60; 1,78; 1,08; 0,79; 0,60 (CLOWN) | tính từ NG Hình 11.14 |
| Ví dụ 11.14 | vết LZ77 `aabaacabcabcb`, $W=6$, $L=4$: (0,0,a)(1,1,b)(3,2,c)(5,2,c)(3,3,b); 70 / 72 / 90 / 104 bit | chương tính; độ rộng mã LZ78 3 bit và LZW 9 bit viết "Giả sử" |
| Ví dụ 11.6, 11.7 | ba mã cuối 98, 99, 98 và mục 263 = `bc`, 264 = `cb`; vết giải mã đủ 10 mã | chương tính (CMU chỉ in 7 mã đầu) |
| Ví dụ 11.8(b), hình `note-lzw-ma-chua-co.svg` | vết `abababa` → 97, 98, 256, 258 | "Giả sử", theo D7 |
| Bài tập 11.6 | chuỗi toàn chữ a; $n=6$ → 97, 256, 257; $n=r(r+1)/2$ → $r$ mã, mọi mã từ mã thứ hai đi qua nhánh $k=\texttt{next\_code}$ | bài cuối mục do chương dựng (thay đề "ba bộ nén" của outline, nội dung đó đã ở Ví dụ 11.14) |
| Bài tập 11.3(c) | 100 chữ A, $W=4096$, $L=16$: 7 bộ ba, 25 bit mỗi bộ ba, 175 bit | chương tính |
| Bài tập 11.2 | điểm hòa vốn $m=2$ (17 bit), $m=4$ (27 bit) | tính từ 17/27 bit của NG tr.208 |
| Mục 2.3 | 14 bit mỗi bộ ba với $W=6$, $L=4$; hòa vốn 1,75 ký tự | Mệnh đề 11.9(d) |
| Mục 3.3 | 25 bit mỗi cặp với $M=2^{16}$ và trường ký tự 9 bit | Mệnh đề 11.16(d) |
| Ví dụ 11.9–11.13 | trung bình 151,25; tổng hàng 1 220 … 1 176; $F$ thực hàng 0; năng lượng 43 372 / 43 333; tỷ lệ 80 %, 85 %, 4,4 %; $\hat F$ ($q=2$, làm tròn, 30 số khác 0); $\tilde F$; $\tilde P$; RMS điểm ảnh 4,21; RMS hệ số 4,12 ($\sum(F-\tilde F)^2=1\,086$); tỷ số lớn nhất 8/17 ở ô (3,4); dãy zigzag, lượt 55, 30 bộ ba, biên độ 6 + 39 bit | chương tính trên dữ liệu NG Hình 11.9 và công thức NG tr.259–260 (D4 cho phép) |
| Mục 5.1 | IDCT của $F$ đã làm tròn lệch khối gốc tối đa 1 mức xám | chương tính |
| Định lý 11.31, Ví dụ 11.12, Bài tập 11.9, Tình huống 11.1 | $\sum Q^2=5\,856$, $21\,184$, $124\,384$; $\beta(1,2,5)\approx4{,}78$; $9{,}10$; $22{,}04$; nhân đôi 9,57; 18,19; 44,09 | chương tính |
| Phạm vi Định lý 11.31 | làm tròn điểm ảnh cộng tối đa 1/2 vào RMS (bất đẳng thức tam giác), cắt không làm tăng sai số | chương chứng minh |
| Mục 5.4, Tình huống 11.1 | $1\,024$ / $8\,192$ phép nhân mỗi khối; $1\,024\,000$ mỗi ảnh; $\approx1{,}02\cdot10^9$ cả kho; dải $2\,560$ điểm | đếm theo NG tr.255–256, 267 |
| Hình `note-cheetah-byte-rms.svg`, đoạn đọc | giảm 17 577 byte / tăng 6,6 (q 1→5); giảm 5 138 / tăng 6,5 (q 5→25) | tính từ NG Hình 11.14 |
| Tình huống 11.1 | "Giả sử mọi ảnh như CHEETAH.GS": 18,4 MB ($q=2$), 10,2 MB ($q=5$); $q=2$ bảo đảm ngưỡng 10 vì $\beta(2)+0{,}5\approx9{,}60$ | chương tính |
| Tình huống 11.2 | "Giả sử không cụm nào khớp": 192 000 byte (24 bit/điểm), 72 000 byte (LZSS 9 bit); $\approx4{,}2\cdot10^9$ phép so | chương tính từ NG tr.179 |
| Tình huống 11.3 | LZW12: 13 mã × 12 bit = 156 bit = 19,5 byte | chương tính; đã kiểm mã LZW12.C phát `END_OF_STREAM` ở cuối (NG tr.220, 224) |
| Nhận xét 11.25 | hệ số tải $\le3\,839/5\,021\approx0{,}76$; $1/(1-\alpha)\approx4{,}2$ lần dò | chương tính, cận CLRS §11.4 (dưới giả thiết băm đều; ghi chú nói rõ hàm băm của NG không thỏa) |
| Mục 1.2 | mô hình bậc 0 trả cùng số bit cho lần lặp thứ hai của `aac` | lập luận của chương |

#### 2. Chỗ chỉnh so với nguồn (đính chính chỉ ghi ở đây, không ghi trong ghi chú — VP18)

- CMU-LZ tc. 17, 19 in mã 112, 113, 114 cho a, b, c; ghi chú dùng mã byte thật 97, 98, 99 (D3).
- CMU-LZ tc. 5 ghi bộ ba đầu `(_,0,a)`; ghi chú viết $(0,0,\mathrm a)$ như NG tr.175.
- CMU định nghĩa vị trí "relative to the cursor" (khoảng lùi); NG dùng chỉ số trong bộ đệm cửa sổ (tr.175–176). Ghi chú dùng khoảng lùi, nêu cách ghi của NG một câu (D2). NG $(38,9,\mathrm A)$ (tr.176) được viết lại $(1,9,\mathrm A)$ trong Bài tập 11.3.
- NG tr.176: đoạn mã giải nén gọi `fwrite` từ vùng nguồn trước vòng chép (sai khi chồng lấn) — không trích; ghi chú theo văn bản NG tr.176–177.
- NG tr.179 "4 096-byte window, sixteen-byte look-ahead … 12 + 4 + 8 = 24 bit": ghi chú diễn đạt là trường độ dài 4 bit, $\ell\le15$, vùng nhìn trước 16 byte kể cả ký tự kế, để khớp $\lceil\log_2(L+1)\rceil$ của Mệnh đề 11.9.
- NG tr.183 ví dụ "Go To Statement Considered Harmful": các mảnh của cách tối ưu ("Go ", T, o, "Stat") không ghép lại đúng cụm gốc (thiếu dấu cách); ghi chú chỉ dùng tổng 75 / 68 bit.
- NG tr.211: từ điển sau 19 ký tự in mất dấu cách ở mục 3, 5, 8; ghi chú dùng `D␣`, `DA␣`, `␣` (khớp Hình 9.1). Đề lấy 19 ký tự đầu, bỏ "...".
- NG tr.215–216: bảng LZW mất dấu cách ở 259, 260, 261, 265; ghi chú dùng `D␣`, `␣WE`, `E␣`, `B␣`. Tiêu đề bảng NG có dấu cách cuối; ghi chú dùng chuỗi 19 ký tự không dấu cách cuối (khớp "nineteen-character").
- NG tr.217: "decodes code 300 and outputs the IWOMBATI string" — ghi chú dùng `IWOMBAT`; "occurs in the table" hiểu là "trong đầu vào".
- NG LZW12.C: mã 256 = `END_OF_STREAM`, mã đầu 257 — ghi chú dùng quy ước văn xuôi (256 là cụm đầu), biến thể nêu ở Nhận xét 11.25 và Tình huống 11.3.
- NG Hình 11.9 ô (0,7) in 19, tính ra −19 (giá trị thực −18,94); ghi chú dùng −19 (D4).
- NG Hình 11.11 theo phép cắt và có lỗi dấu ô (1,3); ghi chú chỉ dùng ô (0,2), (0,4), (2,0), cho cùng kết quả khi làm tròn và khi cắt (Bài tập 11.8, đoạn sau Mệnh đề 11.30).
- NG tr.259 nói bước lượng tử "from one to 255", mâu thuẫn với công thức ($Q_{77}=376$ ở $q=25$); không dùng câu đó.
- NG tr.264 bảng số bit in "7 to −4", "32 to 64"; ghi chú nêu quy tắc $s=\lfloor\log_2\lvert a\rvert\rfloor+1$ và các khoảng đúng.
- Cột "Ratio" của NG Hình 11.14 không khớp đều với $1-\text{byte}/64\,000$ (ví dụ $q=2$: 71,3 % so với 72 %); ghi chú không dùng cột này.
- Mã độ dài loạt định nghĩa trên dòng nối các khối (như DCT.C để loạt số 0 kéo qua khối, NG tr.267), số 0 cuối dòng suy từ độ dài $64K$; không đưa mã kết thúc khối EOB của JPEG chuẩn (không có trong nguồn).
- "Hệ số AC": NG không dùng; văn bản PDF của CMU-L không trích được chữ (lỗi phông) nên không xác nhận được thuật ngữ trong nguồn; giữ theo D12, định nghĩa tại chỗ (Định nghĩa 11.32).
- Kết quả Wyner–Ziv chỉ có qua CMU-LZ tc. 10 "[Wyner-Ziv 94]"; ghi "Chứng minh nằm ngoài phạm vi học phần", không có trích dẫn đầy đủ.

#### 3. Chứng minh do chương viết (nhãn `bổ sung`, D11)

Bổ đề 11.7, Định lý 11.8, Mệnh đề 11.9, Bổ đề 11.12, Định lý 11.15, Mệnh đề 11.16, Bổ đề 11.21, Mệnh đề 11.22, Định lý 11.23, Mệnh đề 11.24, Bổ đề 11.27, Mệnh đề 11.28, Mệnh đề 11.30, Định lý 11.31, Mệnh đề 11.33, lập luận "từ khối sang ảnh" sau Thuật toán 11.34. Nguồn chỉ phát biểu (CMU-L tc. 12; NG tr.217, 259–260) hoặc không có.

#### 4. Giáo trình đã đối chiếu theo mục (GC25)

- Mục 1: NG tr.246–247, 259, 266, 287; Mệnh đề 10.2.
- Mục 2: NG tr.174–185, 200, 208–209; CMU-LZ tc. 3–10; CLRS §2.1 (cách viết bất biến).
- Mục 3: NG tr.208–213; CMU-LZ tc. 11–14, 18; CLRS §11.2.
- Mục 4: NG tr.213–226; CMU-LZ tc. 15–19; CLRS §11.2, §11.4.
- Mục 5: NG tr.250–289 (đặc biệt 254–268, 287); CMU-L tc. 9–17.
- Mục 6, Tình huống: NG tr.170–171, 179, 208, 213–215, 246–247, 287; CMU-LZ tc. 3, 8, 20.
- Thứ tự trình bày theo outline (không đổi so với NG ngoài việc đặt định nghĩa DCT dạng ma trận trước dạng tổng kép, lý do: Hình 11.6 chỉ trực chuẩn khi $N=8$).

#### 5. Bổ sung sau lượt biên tập I.6 (bản sau md5 3ab5a114…)

Số liệu "Giả sử" và số liệu tự tính mới:

| Vị trí | Số liệu | Cách có |
|---|---|---|
| Mục 1 (đoạn kho ảnh), Tình huống 11.1, Bài tập 11.11 | danh mục 1 000 ảnh "giả sử là ảnh xám 8 bit như các tệp .GS" | NG tr.246 nói ảnh VGA 256 màu theo bảng màu; giả thiết ảnh xám do chương đặt (CG5) |
| Mở Mục 3 | tên riêng 9 ký tự ở vị trí 1 000–1 008 và 11 000–11 008; $W=4\,096$; lịch sử $x[6\,904..10\,999]$ | "Giả sử", minh họa giới hạn cửa sổ theo NG tr.208 |
| Bài tập 11.1(c)–(e) | hệ số chung $q=2$, thêm 5 607 byte (≈21 %); hàng 0 của khối Hình 11.9 và của khối tái tạo (Ví dụ 11.12) cho RMS $\sqrt{17}\approx4{,}12$; $m=1$: 256 ảnh, 255 chuỗi ngắn | số từ NG Hình 11.14 và từ phép tính của chương |
| Bài tập 11.3(c) | $L=15$ (cấu hình NG): 8 bộ ba, 24 bit mỗi bộ ba, 192 bit | chương tính lại (thay 7 bộ ba/175 bit của v1, $L=16$) |
| Bài tập 11.4(d) | chứng minh các cụm đôi một khác nhau | chương dựng |
| 5.2, ví dụ trước Định nghĩa 11.29 | $F_{01}=-18$, bước 5, khoảng $(-22{,}5;\,-17{,}5]$ | từ khối Hình 11.9 |
| 5.3, ví dụ trước Định nghĩa 11.32; Ví dụ 11.13 | "Giả sử khối liền trước có $\hat F_{00}=60$", nên $\delta=2$, bộ ba $(0,2,2)$; 31 bộ (30 bộ ba và bộ $(9,0)$); biên độ 2 + 39 bit | "Giả sử" của chương (thay "khối đầu tiên của ảnh" ở v1) |
| Định nghĩa 11.32 | mã độ dài loạt theo từng khối; loạt số 0 cuối khối mã bằng bộ $(r,0)$ | NG tr.263 ("until the block is complete") và tr.271 (số bit 0 dùng cho loạt số 0 trong DCT.C); không đưa EOB của JPEG chuẩn |
| Ví dụ 11.12 | $E_{\mathrm{RMS}}(A,\tilde A)=4{,}18$ trước làm tròn điểm ảnh, bằng RMS hệ số với $F$ chính xác | chương tính |
| Bài tập 11.10 (mới) | tổng cột của $A$: 173, 198, 110, 215, 180, 163, 180, 269; hàng 1 của $T$ làm tròn 3 chữ số; $F_{01}\approx-17{,}98$ (chính xác $-18{,}00$); 12 bộ ba của vị trí 16–30 | chương tính trên khối Hình 11.9 |
| Nhận xét 11.35, Bài tập 11.9(c), Tình huống 11.1 | cận của chương trình NG $\sqrt{\tfrac1{64}\sum(Q-\tfrac12)^2}+\tfrac12$: 9,60; 18,23; 44,12; tỷ số số đo/cận 0,45; 0,38; 0,25 | theo TT4, chương tính |
| Nhận xét 11.35 | ví dụ CMU-L tc. 17: 0,125 bpp, ảnh màu, "factor of 200"; $24/0{,}125=192$ | sửa theo CG1 (v1 ghi sai "64 lần so với 8 bit") |
| Tình huống 11.2 | "Giả sử mỗi bộ ba chỉ khớp $\ell=1$": 32 000 bộ ba, 96 000 byte; LZSS 72 000 byte; cận $\le2{,}1\cdot10^9$ phép so | thay kịch bản "không cụm nào khớp" (không thể xảy ra với $W=4\,096$, CG2) |
| Tình huống 11.4 (mới) | Calgary corpus, gzip 2,59 bpc, LZ77 3,94 bpc (CMU-I tc. 9–10, đã xem ảnh trang); "Giả sử kho $10^9$ byte": ≈3,2·10⁸ và ≈4,9·10⁸ byte; cận $6{,}6\cdot10^{13}$ phép so | số đo nguồn; cỡ kho do chương giả sử |
| Mục 6 | điểm hòa vốn 1,75; 3; 3,125; 1,125; 1,5 ký tự; trung bình 2,6 / 2,17 / 1,3 ký tự mỗi đơn vị trên `aabaacabcabcb` | chương tính |
| Nhận xét 11.25 | $\alpha\approx0{,}765$, $1/(1-\alpha)\approx4{,}25$ (ghi ≈4,3) | sửa làm tròn theo CG |
| Ví dụ 11.14 | ghi đủ sáu cặp LZ78, gồm $(2,\mathrm c)$, $(5,\mathrm b)$ | theo quyết định 11; bài recitation 11.14 thành bài tự kiểm |
| 5.1 | $256^4\approx4{,}3\cdot10^9$ số hạng cho khối $256\times256$ | chương tính |

Chỗ chỉnh so với nguồn (thêm): NG tr.200 (bắt đầu với mã hẹp rồi tăng) thuộc LZSS, đã bỏ khỏi Nhận xét 11.25 (D6); GIF dẫn NG tr.170 thay CMU-LZ tc. 3; BTLZ ghi "chuẩn của British Telecom" (CMU-LZ tc. 18); bảng lượng tử chuẩn dẫn NG tr.259–260 cho "thử nghiệm của ủy ban JPEG", CMU-L tc. 15 cho bảng số; phép cắt thương dẫn NG tr.261, 269.

#### 6. Lượt sửa thứ hai I.6 (md5 ae0d35e2…)

- Bài tập 11.11(d): "giả sử mã và mã cha mỗi trường 2 byte, ký tự 1 byte" → bảng LZW12 $5\,021\cdot5=25\,105$ byte; LZ77 $W+L+1=4\,112$ byte (chương tính; NG tr.218–219 chỉ cho cấu trúc nút và cỡ bảng).
- Bộ $(r,0)$ đóng khối ghi rõ là quy ước của chương; NG chỉ dẫn cho cách ghi biên độ bằng số bit (tr.263–264). Cách xử lý loạt số 0 của DCT.C (đếm xuyên khối, loạt 1–16 bằng 4 bit, xả ở cuối tệp; tr.267, 270–271) nêu một câu trong Nhận xét 11.35.
- Tình huống 11.4: cận $6{,}6\cdot10^{13}$ ghi là cận của Thuật toán 11.5 với cấu hình giả sử $W=4\,096$, $L=15$, không phải chi phí của gzip.


### Kiểm cuối ghi chú (I.7, điều phối viên)

Bản cuối: `lecture-note.md` md5 `4b9cd9af3fdda50c45031f8d6e181f1d`, 30 407 âm tiết (`wc -w`, trong 12 000–32 000; GC-DSFA-6), 1 869 dòng. Thay đổi sau v3 chỉ là câu gzip ở Tình huống 11.4 (điều phối viên đọc diff).

Kiểm trên viewer (máy chủ tĩnh tạm cổng 8793, đã tắt), URL `2627-1/material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html`, Chromium Playwright:

- 1600×900 và 390×844: 0 lỗi hay cảnh báo console, 0 request hỏng, 0 `.katex-error` trên 2 307 biểu thức, không tràn ngang trang (`scrollWidth` 1585/1600, 375/390), 10/10 SVG tải được; 38 khối gập đóng mặc định; 21 `note-topic-id` hợp lệ (viewer không báo lỗi mã chủ đề). Đã xem ảnh chụp đầu trang rộng và giữa trang hẹp: ma trận $8\times8$ cuộn ngang trong khung công thức, không tràn trang (đã biết).
- In: 38/38 khối gập mở; PDF 95 trang.

Bảng kiểm GC26:

| Mục kiểm | Kết quả | Căn cứ |
|---|---|---|
| Mỗi mục tiêu có kết quả/ví dụ và bài tập | đạt | vai mạch, kiểm lại lần 2: sáu mục tiêu đều có bài (11.1(d)(e), 11.2–11.3(d), 11.4(e), 11.5–11.6, 11.7–11.10, 11.11(d)) |
| GC18 cho khái niệm trọng tâm; tính tay trước giả mã | đạt | I.5 sư phạm; ví dụ số thêm trước Định nghĩa 11.29, 11.32 (I.6) |
| Ký hiệu trong bảng hoặc gọi tên tại chỗ; không dẫn về sau | đạt | kiểm lại lần 2 hai vai: không còn chữ hai nghĩa; 392 tham chiếu trỏ đúng, chỉ danh sách xem trước bốn tình huống (theo mẫu Bài 10) |
| Kết quả đủ phần GC21/GC-DSFA-8, có chứng minh hoặc nguồn có trang | đạt | I.5 thuật toán |
| Ví dụ có kết quả số và kiểm tra; mọi số tính lại độc lập | đạt | vai thuật toán chạy script độc lập (I.5, I.6 hai lần) |
| Bài tập có `hint` và `solution` đầy đủ | đạt | 11 bài, mỗi bài một `hint`, một `solution` |
| Không "xem trang chiếu", câu mảnh; chứng minh chia bước, `aligned` | đạt | I.5 sư phạm, sinh viên |
| Móc nối, "Trong thực hành" (GC14), kết mục (GC15, câu nối một phía) | đạt | vai mạch, kiểm lại |
| VP18–VP23 (`no-ai-slop` Detect) | đạt sau biên tập | I.5 sư phạm; biên tập viên tự rà `eval.md` |
| Giáo trình đã tham khảo theo mục | đạt | mục 4 của ghi chú người soạn ở trên |
| Số hiệu liên tục, khối không lồng, render đúng ở hai kích thước và khi in | đạt | script tham chiếu; kiểm viewer ở trên |
| Nhất quán với deck, bài tập cùng bài | chờ giai đoạn II–III | deck dựng lại sau; `exercises.md` chưa có |

Kết luận giai đoạn I: ghi chú đạt kiểm định, chờ người dùng duyệt theo Q10 trước khi commit `fix(materials-11)`. Thẻ Bài 11 chưa thêm vào `index.html` (deck chưa đạt).

### Duyệt danh sách bài tập (II.1)

Quyết định: **chấp nhận** danh sách 11.12–11.17 (báo cáo scratchpad `lec11-II1-chon-bai.md`): 11.12 CMU-LZ trang chiếu 5 (recitation), 11.13 trang chiếu 6 (recitation), 11.14 trang chiếu 7 (LZSS, không recitation; đề nêu $W=6$, $L=4$ của trang chiếu 5, BT-DSFA-6), 11.15 trang chiếu 13 (recitation), 11.16 trang chiếu 16 (recitation), 11.17 CMU-L trang chiếu 11 (recitation). Câu hỏi loại: CMU-LZ 18 (câu trả lời in trên trang), 26, 27, 30 (Burrows–Wheeler, ngoài phạm vi), CMU-L 5, 25, 32 (lượng tử véc-tơ, wavelet, JPEG2000; ngoài Q9). Quyết định cho năm điểm người chọn bài nêu:

1. Tiêu đề khối theo prompt: `(Tên ngắn; CMU 15-499, compression3-lz.pdf, trang chiếu N)`.
2. 11.17: rút "Cosine or Fourier" thành "biến đổi cosine" (rút gọn theo BT-DSFA-6; biến đổi Fourier không có trong ghi chú, lập luận như nhau); ghi chỗ chỉnh.
3. 11.15: phương án A (giữ ghi chú; đề đòi quá trình: nút hiện tại, tra con, cây đủ sáu nút, kiểm Định lý 11.15(a) sau từng cặp). Lý do: CMU trang chiếu 14 cũng in vết đầy đủ; Ví dụ 11.14 cần các cặp để kiểm 72 bit.
4. Mục tiêu 1 và 6: không có bài nguồn; dựa vào Bài tập 11.1 và 11.11 của ghi chú (BT-DSFA-1, BT9). Phép tính số JPEG dựa vào 11.7–11.10.
5. Trang bài tập tổng hợp của "Tổng kết" (NT-DSFA-10) dùng 11.14.

### Duyệt của người dùng và chỉ mục (I.8)

Người dùng 2026-11-19: "hãy đưa lecture note lên index, commit và push" (duyệt ghi chú theo Q10). Thêm thẻ Bài 11 vào `2627-1/index.html` theo mẫu thẻ Bài 10: "Ghi chú bài giảng" có liên kết viewer; "Bài giảng" và "Bài tập" ghi `Chưa có` (deck dựng lại và `exercises.md` chưa đạt kiểm định). Kiểm Chromium: 1600×900 và 390×844 không lỗi console, không request hỏng, không tràn ngang; nút "Mở ghi chú" mở đúng viewer Bài 11. Liên kết `exercises.md` trong mục "Bài tập củng cố" của ghi chú trỏ tới tệp sẽ có ở commit giai đoạn II.

### Rà bài tập (II.3)

| Mức độ | Vị trí | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|---|
| nghiêm trọng | Bài tập 11.16 | Chép lại chứng minh tổng quát của Mệnh đề 11.22(b) và đoạn sau nó (BT1); câu hỏi phụ không phải phép tính trên dữ kiện (BT-DSFA-6) | vai sư phạm, ghi chú dòng 936–950; vai thuật toán (nhẹ) cùng ý | yêu cầu sửa: giữ câu hỏi của CMU-LZ trang chiếu 16 trên mẫu $\chi S\chi S\chi$, áp Bổ đề 11.21 cho trường hợp của mẫu, kiểm bằng dẫn Mệnh đề 11.22(b), bỏ câu (c); bác đề xuất dựng chuỗi cụ thể (dữ kiện mới) |
| trung bình | 11.15(a) | Hai cặp cuối đã in ở Ví dụ 11.14 | ghi chú dòng 1668–1669 | yêu cầu sửa theo phương án A: câu (a) là vết bước tra con |
| trung bình | 11.17(a) | "Theo ba mục tiêu" nhưng mục tiêu 3 được trả lời bằng lập luận chi phí | vai thuật toán; vai sư phạm | yêu cầu sửa: "dựa trên ba mục tiêu và chi phí tính toán", tách chi phí |
| trung bình | 11.17(b) | Lời giải trùng câu trả lời ở đầu Mục 5.1 | vai sư phạm | sửa một phần: dẫn số hiệu kết quả; bác thêm phép tính khối $16\times16$ (không phải dữ kiện trang chiếu nguồn) |
| trung bình | tiêu đề khối | Ghi tên tệp PDF | vai sư phạm | bác bỏ: giữ dạng tiêu đề của prompt người dùng (II.2) |
| nhẹ | nhiều chỗ | xem báo cáo | | áp dụng, trừ thứ tự bài theo mức (giữ như Bài 10, BT-DSFA-4) |

Kiểm lại trên v2 (md5 `29d98755`): vai thuật toán 0/0/0/0; vai sư phạm 0/0/1/3 (câu tương quan ở 11.17(a) vượt căn cứ NG tr. 255; cụm lộ kết quả ở đề 11.16; hai câu dồn ý) → yêu cầu sửa; điều phối viên đọc diff bản cuối md5 `d51a0647c0527bb16a06f9de53898315`: bốn chỗ đúng như yêu cầu, không đổi số. Đề 11.16 giữ "thêm mục $\chi S\chi$" vì là dữ kiện của trang chiếu 16 ("enters Sc into dictionary").

### Chỗ chỉnh so với trang chiếu nguồn (BT-DSFA-6, BT8; từ người soạn bài tập)

#### Bài 11 — II.2 người soạn `exercises.md`: ghi chú cho điều phối viên

Tệp: `ds-foundation-algorithms/2627-1/materials/lec-11/exercises.md` (6 khối, mỗi khối 1 hint + 1 solution). Không commit. Cập nhật sau lượt biên tập II.3 (quyết định `lec11-II3-quyet-dinh.md`): md5 `29d987556efc66a62e6e33b8447f72d8`. Danh sách chỉnh dưới đây là trạng thái sau II.3.
Script kiểm vết: `scratchpad/lec11_ii2_check.py` (đầu ra `lec11_ii2_check.out`, kết thúc "OK"); kiểm hiển thị: `scratchpad/lec11_ii2_render.py` (1600×900 và 390×844: 0 `.katex-error`, 0 lỗi console, không cuộn ngang trang; bốn bảng lời giải cuộn ngang trong khung bảng ở 390 px; công thức duy nhất từng tràn đã ngắt bằng `aligned`).

#### Danh sách khối

| Mức | Khối | Recitation |
|---|---|---|
| Nhận biết | 11.13 (Bộ ba có độ dài lớn hơn khoảng lùi; CMU 15-499, compression3-lz.pdf, trang chiếu 6) | có |
| Tính toán/chứng minh | 11.12 (Hoàn tất vết LZ77; …, trang chiếu 5) | có |
| | 11.14 (LZSS kiểu gzip; …, trang chiếu 7) | không |
| | 11.15 (Hoàn tất vết LZ78; …, trang chiếu 13) | có |
| | 11.16 (Mã chưa có trong từ điển của bộ giải mã LZW; …, trang chiếu 16) | có |
| Vận dụng | 11.17 (Biến đổi trên toàn ảnh và mã hóa theo khối; CMU 15-499, compression4-lossy.pdf, trang chiếu 11) | có |

Bảng độ phủ: mục tiêu 1 và 6 ghi "—" (dựa vào Bài tập 11.1, 11.11 của ghi chú, theo quyết định II.1 điểm 4).

#### Chỗ chỉnh so với nguồn (BT-DSFA-6)

- **11.12** (LZ tc. 5): dịch; "Dictionary (size = 6)" → $W=6$, "Buffer (size = 4)" → $L=4$ (Định nghĩa 11.4); $(p,l,c)$ → $(d,\ell,c)$; literal `(_,0,a)` → $(0,0,\mathrm a)$; thêm "con trỏ ở $p=8$" (suy từ ba bộ ba đã cho, $1+2+5$); hai "?" → câu (a); thêm (b) giải mã năm bộ ba, chỉ bộ ba $\ell>d$ và bước đọc ô vừa ghi, (c) số bit theo Mệnh đề 11.9(d) — phép tính trên chính dữ kiện.
- **11.13** (LZ tc. 6): dịch; "dict = abcd" → bản giải mã $y=$ `abcd`, $p=4$; $p$ (vị trí tương đối của CMU) → $d$; "What if l > p? (only part of the message is in the dictionary.)" bỏ khỏi đề (II.3: câu đó lộ ý câu (b)), nhiệm vụ còn nguyên ở dữ kiện $(2,9,\mathrm e)$; "What does this give?" → (a), đòi phép gán từng bước; thêm (b) các bước đọc ô vừa ghi. Gợi ý không cho sẵn công thức $2+j$ (II.3). Đọc $2$ là chỉ số tuyệt đối từ 0 cũng cho cùng kết quả (chỉ ghi ở đây).
- **11.14** (LZ tc. 7, không recitation): dịch; "position" → khoảng lùi $d$ (tương đối như tc. 4); nêu $W=6$, $L=4$ của tc. 5 (D10); nêu quy tắc tiến con trỏ, cận $\min(L,n-p)$ (dạng $(0,d,\ell)$ không có ký tự kế), chọn $d$ nhỏ nhất khi hòa (như bước 2.2 Thuật toán 11.5), "Uses the second format if length < 3" viết thành hai điều kiện $\ell\ge3$/$\ell<3$; gọi chữ số đầu là bit cờ (Nhận xét 11.10); "[?]" → (a); thêm (b) hoàn tất dãy và đếm mục mỗi dạng. Khi hòa, quy tắc chọn $d$ không đổi kết quả (mọi lượt có độ khớp lớn nhất duy nhất hoặc ra dạng thứ hai). II.3: "Kiểm tra lại" nêu vì sao Bổ đề 11.7 áp dụng cho mục LZSS ($1\le d\le p$ và điều kiện khớp là hai điều kiện chứng minh dùng).
- **11.15** (LZ tc. 13): dịch; bỏ hình cây đã điền đủ (rút gọn: nút 5, 6 là đáp số); "R" → gốc 0, $D[0]$ rỗng; "Output" → cặp $(i,c)$; phương án A theo II.3: câu (a) là "lập vết bước 2 từ $x_7$: nút hiện tại, kết quả tra con, cặp phát", không còn câu "xác định các cặp còn lại"; (b) "liệt kê mọi mục sau cặp cuối", không nêu số mục; (c) giải mã toàn bộ dãy (bốn cặp đầu và các cặp ở (a)) và kiểm Định lý 11.15(a) sau từng cặp. Hai cặp chỉ đối chiếu với Ví dụ 11.14 ở "Kiểm tra lại". Tc. 14 chỉ dùng đối chiếu.
- **11.16** (LZ tc. 16), viết lại ở II.3 theo mẫu trừu tượng của trang chiếu: "…SSc… where S[0] = c" → đoạn $\chi\,S\,\chi\,S\,\chi$ với cụm $\chi\,S$ đã có mã ($S$ của CMU ứng với $\chi S$, $c$ ứng với $\chi$; ký hiệu theo Mệnh đề 11.22 của ghi chú); $id_1,id_2$ → $k_t,k_{t+1}$; thêm "từ điển của hai phía không giới hạn số mục" (giả thiết của Bổ đề 11.21, không phải dữ kiện số). "What do we do?" tách thành (a) xác định $k_{t+1}=255+t=\texttt{next\_code}$ và vì sao bộ giải mã chưa có mục đó (Bổ đề 11.21(a)(c), đúng trường hợp của mẫu); (b) cụm gán cho $k_{t+1}$ và mục thêm, kiểm bằng cách dẫn Mệnh đề 11.22(b), không chứng minh lại tổng quát. Bỏ câu (c) cũ và chỉ số $s$. Bỏ câu mở "chậm hơn một mục, vì …" (lời giảng giải). Không dựng chuỗi cụ thể (trang chiếu không có). Kiểm máy (giữ): mọi chuỗi độ dài 1–10 trên $\{\mathrm a,\mathrm b,\mathrm c\}$, 44 886 lần $k=\texttt{next\_code}$, 0 lần trái $w\operatorname{first}(w)$, không lần nào $k>\texttt{next\_code}$.
- **11.17** (L tc. 11): dịch; "Goals" → câu dẫn có danh sách đánh số; "Cosine of Fourier" (lỗi in của "Cosine or Fourier") rút thành "biến đổi cosine" (quyết định II.1 điểm 2); II.3: giải nghĩa tại chỗ "khử tương quan" (điểm gần nhau tương quan, hệ số sau biến đổi không còn tương quan) và "hàm cơ sở" (mẫu cosine dựng từ các hàng của $T$, Định nghĩa 11.26); hai câu hỏi → (a), (b) giữ câu chữ nguồn ("vì sao … kém", "khắc phục"); yêu cầu trình bày "dựa trên ba mục tiêu và chi phí tính toán, dẫn số hiệu". Lời giải: mỗi câu tách bốn ý (mục tiêu 1, 2, 3, chi phí và bộ nhớ); mục tiêu 2 ở (a) nêu "mở rộng vùng ít lợi thêm" (NG, tr.255); mục tiêu 3 chỉ dựa trên Định nghĩa 11.29; câu có nguồn dẫn "(NG, tr.255)" thay "Mục 5.1". Tỷ lệ $m/64=1\,000$ tính trên CHEETAH.GS (dữ kiện của ghi chú). Không thêm phép tính khối $16\times16$ (bác, BT-DSFA-6); không dùng wavelet (CMU-L tc. 22, ngoài Q9). Bảng độ phủ ghi "11.17 (mã hóa theo khối và chi phí của DCT)" ở mục tiêu 5.

#### Điểm cần điều phối viên lưu ý

- Đoạn mở ghi "Bài tập 11.12 và 11.15 dùng cùng chuỗi với Ví dụ 11.2 và Ví dụ 11.4" (BT1, quan hệ với ghi chú); 11.15 "Kiểm tra lại" đối chiếu Ví dụ 11.14, 11.16 "Kiểm tra lại" đối chiếu Ví dụ 11.8(b) và Bài tập 11.6.
- Đoạn mở bỏ "Hệ quả" khỏi danh sách loại khối (ghi chú Bài 11 không có Hệ quả).
- Ở 390 px, bốn bảng lời giải (11.12(b), 11.14(b), 11.15(a), 11.15(c)) cuộn ngang trong khung bảng; trang không cuộn ngang.

#### Lượt II.3: phát hiện không áp dụng

- SP trung bình (tiêu đề dùng tên tệp PDF thay CMU-LZ, CMU-L): bác theo quyết định 4, giữ dạng của prompt.
- SP nghiêm trọng, phần đề xuất dựng chuỗi và dòng mã cụ thể cho 11.16: bác theo quyết định 1 (trang chiếu 16 không có chuỗi cụ thể).
- SP trung bình 11.17, đề xuất thêm phép tính khối $16\times16$: bác theo quyết định 3 (dữ kiện mới).
- SP trung bình 11.15, phương án rút Ví dụ 11.14 của ghi chú: không áp dụng (quyết định 2, không sửa ghi chú).
- TT nhẹ (đổi số để 11.12 đứng trước 11.13): bác theo quyết định 5 (xếp theo mức như Bài 10, BT-DSFA-4).
- SP nhẹ đề xuất đổi đề 11.17(a) thành "So sánh …": không áp dụng; quyết định 3 giữ câu hỏi của nguồn ("vì sao … kém").


### Kiểm cuối bài tập (II.4, điều phối viên)

Viewer `material-viewer.html?doc=materials/lec-11/exercises.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html` (máy chủ tĩnh tạm, đã tắt): 1600×900 và 390×844 không lỗi console, không request hỏng, 0 `.katex-error` trên 390 biểu thức, không tràn ngang trang; 12 khối gập đóng mặc định, mở hết khi in. Bốn bảng lời giải cuộn ngang trong khung bảng ở 390 px (11.12(b), 11.14(b), 11.15(a), 11.15(c)), không tràn trang. Đã xem ảnh màn hẹp. Liên kết "Bài tập" thêm vào thẻ Bài 11 của `index.html` (BT13); nút mở đúng tệp; hai liên kết `exercises.md` trong ghi chú trỏ đúng. Độ phủ: mục tiêu 1 và 6 không có bài nguồn, dựa vào Bài tập 11.1 và 11.11 của ghi chú (BT-DSFA-1, BT9).
