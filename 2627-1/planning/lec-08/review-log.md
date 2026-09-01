# Nhật ký rà soát Bài 8

## Quy trình của vòng hiện tại

1. **Phân tích nguồn:** xác định MMDS Chương 4, mục 4.1–4.3 làm nguồn chuẩn; slide MMDS Streams 1–2 làm nguồn bố cục; hai bản PDF Stanford CS246 cục bộ làm đối chiếu (`stanford-cs246/16-streams.pdf`, CS246 ngày 26/02/2026, dùng tại phép đếm K01 và đường cong B11 tr.31–32; `stanford-cs246-2017/streams-2.pdf`, Jeffrey D. Ullman, tạo ngày 01/03/2017, dùng tại ví dụ Bloom 11 bit B05 tr.5–8). Các mốc được xác minh từ nội dung và metadata PDF cục bộ; không suy đoán niên khóa.
2. **Kiểm định storyboard:** đối chiếu từng trang với nguồn, thứ tự chu trình, dữ kiện truyền và tổng thời lượng 120+60 phút.
3. **Năm phản biện độc lập:** (i) góc nhìn sinh viên; (ii) chuyên gia giải thuật và khoa học dữ liệu; (iii) độ chính xác toán học và thuật toán; (iv) phản biện học thuật và giảng dạy; (v) kết nối và mạch viết.
4. **Chỉnh sửa tuần tự:** áp dụng từng quyết định vào HTML, outline và storyboard theo bảng phát hiện dưới đây.

## Bảng phát hiện của vòng hiện tại

| Mức độ | Trang | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|---|
| nghiêm trọng | K03, K05 | Băm "gần đều" không bảo đảm tỷ lệ $a/b$ | Đặc tả chỉ yêu cầu hàm băm xấp xỉ đều; tỷ lệ $a/b$ chỉ đúng khi mỗi giá trị miền có xác suất đúng $1/b$ | Ghi rõ $h$ phải phân bố đều trên toàn miền $\{0,\ldots,b-1\}$ ở K03, K05, outline và storyboard; giữ điều kiện $h(K)<a$ |
| nghiêm trọng | X01 | Thiếu giả thiết nguồn của đề | Đề Ex.4.2.1 (tr.138) đặt định danh university duy nhất toàn cục; bản nháp bỏ sót | Thêm "định danh university là duy nhất toàn cục" vào X01; ghi rõ đáp án/rubric là lời giải giảng viên suy ra từ đề, không in trong sách |
| trung bình | mọi aside.notes | Internal ID và thời lượng rò rỉ vào ghi chú trình bày | Các notes còn chứa P01, K02/K03, K05, R03, R05–R07, B01, B05, B07, B12, X01 và các mốc phút | Xóa/diễn đạt lại toàn bộ mã nội bộ trong notes; mã chỉ còn trong `data-slide-id` và ba tệp planning; xóa mọi thời lượng phút trong notes, giữ trong planning |
| trung bình | B12 | Câu hỏi kiểm tra mâu thuẫn giả định ví dụ | Câu hỏi ngầm giả sử bit 3 của 118 bằng 1, mâu thuẫn với ví dụ 11 bit ở B05 nơi bit 3 của 118 bằng 0 | Đổi câu hỏi dùng một khóa ngoài $S$ khác với 118; notes nêu rõ lý do |
| trung bình | toàn deck | Khả năng tiếp cận: khóa phóng to và cỡ chữ `.tiny`, `.code` thấp | Viewport cũ đặt `maximum-scale=1,user-scalable=no`; `.tiny` là `0.7em`, `.code` là `0.73em` | Bỏ khóa phóng to; nâng `.tiny` lên `0.75em`, `.code` lên `0.76em`; kiểm lại mọi trang ở hai kích thước |
| nhẹ | B00, B11, Ex.4.3.3 | Dẫn nguồn chưa đồng bộ trang | B00 tr.139–140; B11 Stanford tr.31–32; Ex.4.3.3 tr.142 | Đồng bộ trang nguồn ở HTML, outline, storyboard |
| nhẹ | B05 | Quy ước vị trí bit và mô tả thay thế chưa rõ | Nguồn lấy bit lẻ/chẵn 1-based từ phải; mảng hiển thị 0–10 từ trái | Ghi rõ hai quy ước ở B05, storyboard và thuộc tính `alt` trong HTML |
| nhẹ | R00, B00, R03, R04, R07, B09, X04 | Cầu nối giữa các trang còn mỏng | Các trang chuyển ý chưa nêu rõ dữ kiện truyền | Bổ sung câu nối trong notes và storyboard; giữ tổng thời lượng |

## Hai đề xuất bị loại

1. **Ánh xạ Bloom lệch chỉ số** — bị loại. Nguồn `stanford-cs246-2017/streams-2.pdf` tr.5–8 xác nhận deck đúng: bit lẻ/chẵn lấy 1-based từ phải, mảng hiển thị chỉ số 0–10 từ trái; đây là hai quy ước trình bày khác nhau, không phải lỗi.
2. **$q^k$ là xác suất dương giả chính xác** — bị loại. Trong mảng hữu hạn, trạng thái các bit phụ thuộc nhau và các vị trí truy vấn có thể trùng, nên $q^k$ chỉ là xấp xỉ chuẩn; dạng mũ $(1-e^{-km/n})^k$ là xấp xỉ tiếp theo khi $n$ lớn. Chỉ FPR mảng chia (mảng độc lập) mới chính xác theo $n$ hữu hạn.

## Bài tập và giới hạn nguồn

- X01–X04 lấy trực tiếp từ MMDS Ex.4.2.1 (tr.138) và Ex.4.3.1–4.3.3 (tr.141–142); chỉ dịch, chia bước và thêm sản phẩm/rubric. Đã bỏ các yêu cầu phụ không có trong sách: điều kiện $h(K)<1$ ở X01, so sánh ở X02 và trường hợp $n/m=8$ ở X04.
- Sách không có bài tập hồ chứa trực tiếp; không tự tạo bài. R08 chỉ là câu kiểm tra trong phần giảng.
- Không tạo mã trình diễn hoặc notebook.

## Tài sản

- Sáu SVG trong `img/lec-08/` đều có `role="img"`, `title`, `desc`; nhãn tiếng Việt; không dùng màu làm tín hiệu duy nhất.
- Không dùng ảnh raster, phông chữ mạng hoặc thư viện ngoài kho.

## Quy trình biên tập đã áp dụng

- Tự biên tập theo `no-ai-slop/eval.md`: bỏ lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu, nhận định không có nguồn và nhịp câu lặp máy móc. Đã áp dụng.
- Rà theo nguyên tắc Quill mà **không tạo `quill.json`**: chuỗi mô hình → mẫu theo khóa → hồ chứa → Bloom; thống nhất ký hiệu, thuật ngữ và câu nối. Đã áp dụng.

## Trạng thái kiểm định cuối

- Các lỗi chặn bàn giao và nghiêm trọng của vòng hiện tại (băm gần đều K03/K05; thiếu giả thiết X01) đã được xử lý trong deck, outline và storyboard.
- Hai lượt rà lại độc lập sau chỉnh sửa — độ chính xác toán học/thuật toán và kết nối/mạch viết — đã đọc lại HTML cùng ba tệp planning. Cả hai xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`; các phép tính $1/29$, hồ chứa, ví dụ Bloom 11 bit, $q^k$, $k^*$ và bốn bài tập đều đạt.
- Kiểm tĩnh: 48 trang, 48 mã duy nhất, 48 ghi chú; 7 `<section>` ngoài; 11 tài nguyên cục bộ được tham chiếu và đều tồn tại; không có ảnh raster; không còn mã nội bộ hoặc thời lượng trong ghi chú; `git diff --check` sạch.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Dùng `/tmp/reloadserver.py 8765` làm máy chủ HTTP cục bộ thay thế; bài giảng tải thành công.
- Chromium ở $1280\times720$ và $800\times600$: duyệt đủ 48 trang; không lỗi console, lỗi trang, tài nguyên hỏng, tràn khung, chồng lấn, lỗi KaTeX hoặc chữ dưới 18 px; điều hướng bàn phím lên, xuống, phải đúng. Đã xem bản liên hệ toàn deck và kiểm riêng B05, B10, B11, X01, X03, X04.
- Codex Slides: dự án bền vững `20260827204905-b-i-8-d-ng-d-li-u-m-h-nh-l-y-m-u-v-l-c-skiv` vẫn là bản nháp 0 slide. Tệp HTML cuối đã tải thành material `20260830105531489-g5c4.html`; `open_codex_slides` trả liên kết workspace. Môi trường Codex hiện tại không có công cụ Browser để mở bề mặt này, nên không tuyên bố đã rà trực quan bằng Codex Slides; kiểm RevealJS cục bộ là bằng chứng trực quan cuối.

## Quyết định trước khi soạn ghi chú tự học

- Ba reader độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter đã hoàn tất kế hoạch, ánh xạ nguồn và bản đồ chủ đề; metadata runtime xác nhận đúng model và provider.
- Giữ 11 chủ đề `L08-N01`–`L08-N11`. MMDS Chương 4 mục 4.1–4.3 làm trục; Stanford 2017 chỉ cung cấp ví dụ Bloom 11 bit; Stanford 2026 đối chiếu chứng minh hồ chứa và đường cong FPR.
- Thêm một cầu nối ngắn về thay đổi ngưỡng lấy mẫu theo MMDS 4.2.4; không mở thành thuật toán mới. Không thêm ví dụ số ngoài nguồn.
- Chốt ranh giới: $q=1-(1-1/n)^{km}$ chính xác dưới $km$ phép băm iid; $q^k$ là xấp xỉ chuẩn cho FPR; dạng mũ cần $n$ lớn. Phép tính trực tiếp cho $(1-e^{-1/4})^2=0{,}048929\ldots$, nên sửa số 0,0493 in trong sách thành 0,0489; dùng khoảng 0,02158 cho $n/m=8,k=6$.
- Dùng $r$ cho số vị trí đã thấy ở hồ chứa để tránh xung đột với $n$ bit Bloom. Không thêm Rejection Sampling, Flajolet–Martin, moment, DGIM, cửa sổ hoặc bài hồ chứa tự dựng.

## Soạn, phản biện và kiểm định ghi chú tự học

- Writer chạy qua OpenRouter với `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, chỉ được ghi vào cây tạm đã giới hạn. Bản tạo ra được điều phối viên kiểm tra trước khi áp dụng vào kho.
- Đủ năm vai reviewer độc lập bằng `openrouter-mcp-reviewer`; mọi lượt được chấp nhận có `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`:
  1. nguồn và truy nguyên;
  2. toán học–thuật toán;
  3. mạch sư phạm;
  4. kết nối, tính liên tục và ký hiệu;
  5. viewer, Markdown và khả năng tiếp cận.
- Reviewer nguồn ba lần đầu không tạo được báo cáo hợp lệ do hết vòng công cụ hoặc lỗi phân tích JSON. Lượt hẹp chỉ đọc bảng tám mệnh đề và bằng chứng trích đã hoàn tất hợp lệ. Góp ý trung bình về số tính lại được xử lý bằng cách ghi rõ $k=6$ và 0,02158 được suy ra từ công thức, không phải số chép từ bài tập. Góp ý nhẹ về chứng minh hồ chứa đã được đối chiếu lại với MMDS Streams 1 tr.18–21.
- Reviewer toán phát hiện số 0,0493 trong sách không khớp công thức. Tính lại cho $(1-e^{-1/4})^2=0{,}048929\ldots$; ghi chú dùng 0,0489 và nêu rõ sai khác với bản in. Các giá trị $p_3\approx0{,}030579$, $p_4\approx0{,}023969$ và $p_6\approx0{,}02158$ đều được tính lại.
- Reviewer sư phạm đề nghị thêm các điểm tự kiểm, nêu biên $r\le s$ và tránh dùng lại một ký hiệu cho hồ chứa và Bloom. Đã bổ sung tự kiểm ở các nút suy luận, dùng $r$ cho số phần tử đã thấy và $\rho=m/n$ cho tỷ số khóa trên bit.
- Reviewer kết nối xác nhận 11 chủ đề `L08-N01`–`L08-N11` tạo thành một tuyến liên tục. Deck được đồng bộ ký hiệu ở cụm hồ chứa và phép tối ưu Bloom. Thứ tự ví dụ–đặc tả của slide và đặc tả–ví dụ của ghi chú được giữ khác nhau có chủ ý theo hai chu trình trình bày trong `AGENTS.md`; không đảo nội dung để tạo đồng nhất hình thức.
- Reviewer viewer không có lỗi chặn hoặc nghiêm trọng. Các khối mã được gắn ngôn ngữ `text`, đường dẫn nguồn dùng HTTPS và mọi SVG được tải qua thẻ ảnh của viewer.
- Hai lượt `recheck` sau chỉnh sửa, một về toán–thuật toán và một về mạch viết, cùng xác nhận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Các góp ý nhỏ cuối đã được áp dụng: biên $r\le s/r>s$, mô tả rõ hai miền ký hiệu, `tra cứu`, cách viết $1\,000$ và khuôn `exercise`/`solution` thống nhất.

### Biên tập cuối

- `$no-ai-slop`: bỏ nhãn nhấn rỗng, câu dẫn theo quy trình và nhịp kết luận lặp; giữ văn phong trực tiếp, có chủ thể và căn cứ. Tự kiểm theo `no-ai-slop/eval.md` không còn lời quảng bá, câu hỏi tu từ, nhận xét vô căn cứ hoặc chỉ dẫn dành cho người soạn trong nội dung công khai.
- `$quill`: rà lại đồ thị tiên quyết và tính liên tục mà không tạo `quill.json`. Chuỗi khái niệm giữ nguyên: mô hình dòng → sai lệch lấy mẫu từng bộ → lấy mẫu theo khóa → điều chỉnh ngưỡng → hồ chứa → Bloom → định cỡ → chọn cấu trúc → bài tập. Ký hiệu $r,s,n,m,k,\tau,\rho$ nhất quán giữa các phần và đã rà tác động sang deck.

### Bằng chứng kiểm định cuối

- Viewer tại `material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html` vượt kiểm tra ở $1280\times720$ và $390\times844$: 48 mục lục khớp 48 heading; 325 biểu thức KaTeX, không lỗi; 6/6 SVG tải được và có văn bản thay thế; 11 khối gập đóng mặc định; 4 khối mã `text`; không lỗi console, lỗi trang, request hỏng hoặc tràn ngang.
- Điều hướng bàn phím mở được liên kết bỏ qua và khối gập. Chế độ in mở toàn bộ khối gập, ẩn mục lục cùng nhóm thao tác; hình không vượt khung. Viewer từ chối cả đường dẫn vượt thư mục và cặp `doc`/`deck` sai số bài.
- Deck được duyệt lại đủ 48 trang ở $1280\times720$ và $800\times600$ sau khi đồng bộ ký hiệu: không lỗi runtime và không trang tràn khung. Kiểm trực quan riêng trang B10 xác nhận $\rho$ cùng công thức hiển thị đúng.
- Mục Bài 8 trên `index.html` có đúng một liên kết ghi chú. Nhấp bằng bàn phím ở màn hình rộng và hẹp mở đúng tài liệu, đúng liên kết deck, đủ 6 hình và không lỗi KaTeX hay tràn ngang.
- `git diff --check` sạch. Không có `.env`, bí mật, thông tin xác thực, tệp tạm hoặc thay đổi ngoài phạm vi Bài 08 trong tập tệp chuẩn bị commit.
