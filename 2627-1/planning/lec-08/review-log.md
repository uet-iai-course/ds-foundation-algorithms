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

## Đồng bộ cuối deck–note — 2026-09-02

Giữ nguyên 48 trang, 48 notes/ID, 7 mạch ngoài, 42 trang giảng + 6 trang bài tập, thời lượng 120+60 phút và 6 SVG. Reader kế hoạch phiên `56486` và reader nguồn phiên `74176` đều dùng đúng `z-ai/glm-5.3-flash` qua OpenRouter; hai reader thống nhất không đổi cấu trúc hay phạm vi.

Writer `deepseek/deepseek-v4-flash-0731` chạy trong dossier tạm hẹp. Phiên `11325` áp dụng một phần sửa ký hiệu rồi chạm giới hạn công cụ; phiên `60882` cập nhật index rồi hết thời gian API khi biên tập notes. Hai phiên không được tính là hoàn tất. Theo ủy quyền của người dùng, Codex chính chỉ áp dụng các delta đã được hai reader phê duyệt và đưa toàn bộ kết quả qua năm reviewer.

### Delta đã áp dụng

- Dùng $r$ cho số vị trí đã xử lý của hồ chứa trong outline, storyboard và `reservoir-trace.svg`; giữ $n$ cho số bit Bloom. Sửa R02/R04 planning thành $r<s$, $r\ge s$ và $j\in\{1,\ldots,r\}$; xác suất biên là $s/r$.
- Chuẩn hóa thẻ index thành “Bloom filter” và nhãn “Ghi chú bài giảng”.
- Biên tập `$no-ai-slop` các notes P01, P02, A03, K01, K06, K07, R00, B00, B01, B05, B09, B11, C01, X00, X02, X05: bỏ đường dẫn nội bộ, nhãn quy trình và siêu bình luận; không đổi dữ kiện hay mệnh đề.
- Rà Quill xác nhận mạch mô hình dòng → lấy mẫu theo khóa → hồ chứa → Bloom filter → lựa chọn → bài tập vẫn liền mạch; không tạo `quill.json`.

### Năm reviewer và hai tái kiểm

- Nguồn `67059`: `GO`; xác nhận $r,s,n,m,k$, ví dụ Bloom 11 bit, $p_3,p_4,k^*$ và bốn bài MMDS.
- Toán–thuật toán `63413`: `GO`; tự tính lại K01, quy nạp hồ chứa, Bloom 11 bit, FPR, tối ưu $k$ và bốn bài.
- Góc nhìn sinh viên `86645`: phát hiện hai dòng R02/R04 còn dùng $n$ và ba đường dẫn nguồn nội bộ trong notes; đã sửa.
- Văn phong `3119`: `GO`; không còn lỗi trung bình. Góp ý nhẹ về các câu “Trang này/Cầu nối” đã được áp dụng rộng hơn trong notes.
- Kỹ thuật `22356`: `GO`; xác nhận 48 ID/notes, 7 section, 6 SVG, HTML/KaTeX và khả năng đọc. Các góp ý đổi ID R03/R02 hoặc thêm nội dung B05 bị bác vì thứ tự là chủ ý và ví dụ đã đủ trong hình/notes.
- Tái kiểm văn phong `1278`: `GO`; xác nhận toàn bộ notes đã sửa tự nhiên, không rò mã nội bộ hay đường dẫn.
- Tái kiểm delta `51649`: `GO`; xác nhận năm thay đổi ký hiệu, SVG, X02 và no-ai-slop trên đúng bản cuối.

Các phiên source/style `65709`, `42264` bị loại vì chạm giới hạn công cụ. Hai phiên tái kiểm `32810`, `40683` bị bác do sai số học: $(1-e^{-3/8})^3=0{,}030579\ldots$; với $585=1001001001_2$, vị trí lẻ 9,7,5,3,1 cho $01001_2=9$ và vị trí chẵn 10,8,6,4,2 cho $10010_2=18\equiv7\pmod{11}$. Kết quả này khớp nguồn và hai reviewer đầy đủ.

### Kiểm định phát hành

- Deck thật: 48 trang, 48 notes, 0 lỗi KaTeX; không tràn, lỗi console, lỗi trang hoặc request hỏng ở 1280×720, 800×600 và 720×900. Điều hướng bàn phím đạt; PDF có 48 trang.
- Viewer thật ở 1280×720 và 390×844: 48 heading, 37 mục lục, 325 công thức KaTeX, 6 SVG, 11 khối gập; không lỗi hay tràn. Bàn phím, in và hai cổng an toàn đường dẫn đều đạt; PDF viewer có 20 trang.
- Index có đúng một liên kết note Bài 08 và mở đúng deck/note.
- Dự án Codex Slides `20260827204905-b-i-8-d-ng-d-li-u-m-h-nh-l-y-m-u-v-l-c-skiv` truy xuất thành công nhưng vẫn draft 0 slide ở checkpoint `clarify`; không tuyên bố đã rà canvas Codex Slides.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 2 gồm Bài 07–15; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`. Mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch nên dùng `<tiền tố>T`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | AT | Mô hình tính toán trên dòng | Muốn xử lý dòng không biết độ dài, phải đặc tả trạng thái hữu hạn cập nhật sau mỗi bộ đến. |
| 3 | KT | Lấy mẫu theo khóa | Muốn ước lượng tỷ lệ truy vấn lặp của mỗi người dùng, phải giữ hoặc bỏ mọi bộ của cùng một khóa. |
| 4 | RT | Lấy mẫu hồ chứa | Muốn giữ đúng một số bộ cố định khi chưa biết độ dài dòng, phải thay ngẫu nhiên theo vị trí. |
| 5 | BT | Lọc thành viên bằng Bloom filter | Muốn loại sớm khóa không thuộc tập cho phép, phải đổi một mảng bit hữu hạn lấy một tỷ lệ dương giả. |
| 6 | CT | Tổng kết và chuyển tiếp | Muốn chọn cấu trúc cho dòng truy vấn, phải đối chiếu đơn vị, bảo đảm và giới hạn của ba cấu trúc. |
| 7 | XT | Bài tập vận dụng | Muốn kiểm cách chọn khóa và định cỡ Bloom filter, phải giải bốn bài của giáo trình với dữ kiện giữ nguyên. |

Dòng dẫn 21–22 âm tiết; từ khóa 4 cụm; ghi chú diễn giả 82–98 âm tiết, viết từ nội dung các trang trong mạch. Số trang 48 → 55. Các trang nội dung đầu mạch (A00, K00, R00, B00, C00, X00) đều có nội dung, không phải trang tiêu đề phần một dòng, và tiêu đề khác tên mạch; giữ nguyên.

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–7) ngay sau trang bìa P00, tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 33 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Mạch 6 đặt tên "Tổng kết và chuyển tiếp" theo `AGENTS.md`, vì phần C gồm bảng đối chiếu, áp lại vào dòng truy vấn và nguồn, chưa có câu hỏi tự kiểm tra.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Bài 08 còn khối `<style>` riêng và không mang lớp `.course-deck` (có từ trước, ngoài phạm vi). Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 62/62; 55 `data-slide-id` và 6 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/7` mở đúng trang tiêu đề mạch tương ứng (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 709 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng tên các mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 6 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Câu "Mỗi nhóm nộp một phiếu…" ở ghi chú XT thay bằng sản phẩm của lời giải: khóa đã chọn, phép tính xác suất và lập luận tối ưu. Từ khóa "Ba sản phẩm" ở AT đổi thành "Mẫu, hồ chứa, bộ lọc". Lý do đặt trang Nội dung P03 ngay sau bìa: bài không có trang mục tiêu đứng ngay sau bìa (P01 là trang tình huống dòng truy vấn, P02 là kết quả học tập), nên theo brief đặt P03 sau P00; sắp lại mạch mở đầu theo thứ tự mục tiêu → Nội dung → vấn đề trung tâm là việc của đợt sau. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Duyệt từng mạch, sửa ghi chú và gắn index (2026-10-28)

Yêu cầu người dùng (2026-10-28): duyệt lần lượt các trang Bài 08 theo mạch (mạch đã có trang tiêu đề chưa, trang có đạt và phục vụ chủ đề mạch không, trang muốn nói gì, còn vấn đề gì, đề xuất sửa); sửa để tiêu đề ngắn, học thuật, lập luận chặt, khái niệm không đột ngột; rà lại từ góc nhìn sinh viên; giảm chữ; dùng `no-ai-slop`; dùng hình nhắc lại dữ kiện thay cho dẫn chiếu ví dụ ở trang trước; sau mỗi phần sửa ghi chú bài giảng tương ứng, gắn lên `index.html`, commit và push theo mạch.

### Tác tử

Điều phối viên kiêm kiểm soát chất lượng: phiên chính Claude Opus 5.5 (`claude-opus-5-5`), effort `high`. Mọi tác tử con tạo bằng `Agent`, `subagent_type: "general-purpose"`, `model: "opus"`, `effort: "high"` (theo lời gọi công cụ); sửa tiếp bằng `SendMessage` cho cùng tác tử.

| Vai | Ghi tệp | Sản phẩm | Quyết định của điều phối viên |
|---|---|---|---|
| lập kế hoạch, rà deck theo mạch (55 trang, MMDS 4.1–4.3, mật độ, CSS) | không | `audit-deck-08.md` (scratchpad) | chấp nhận; đã tự kiểm khóa Bloom 29 → (7, 2) dương giả và 118 → (3, 5) bị loại trên mảng $10100101010$ |
| bản đồ chủ đề, rà ghi chú theo chuẩn giáo trình | không | `audit-note-08.md` | chấp nhận; đã kiểm `TOPIC_ID_PATTERN = /^[a-z0-9][a-z0-9-]*$/` (mã `L08-N01` không hợp lệ) và liên kết deck `../../lecture-08-…` sai dạng so với Bài 06 |
| biên tập deck | có | diff | xem từng bước |

Quyết định ký hiệu và quy trình chung ghi ở `decisions-08.md` (scratchpad), tóm tắt: hồ chứa là mảng $W$ (thay $S$); $S$, $m$ là tập khóa Bloom; khóa truy vấn $y$; $u$, $d$ cho số giá trị truy vấn xuất hiện một, hai lần (thay $x$ trùng phần tử dòng); $r$ là số phần tử đã đọc; $p_{FP}$ là xác suất dương giả thật, $p(k)$ là dạng mũ; không KaTeX trong tiêu đề; thứ tự mạch 1: P00 → P04 (mới) → P02 → P03 → P01.

### Bước chuẩn bị: chuyển sang CSS dùng chung và mục index

| Mức độ | Vị trí | Vấn đề | Quyết định |
|---|---|---|---|
| nghiêm trọng | `<head>` | khối `<style>` riêng (cỡ chữ `.88em`, `.small`, `.tiny`, lớp `.grid2`, `.card`, `.check`, `.trace`, `.code`) trái quy định chỉ dùng `lecture-style.css` | bỏ; gốc `.reveal.course-deck.lecture-stream`; trang nội dung `example-slide`; lớp chung `ex-grid2`, `ex-card`, `ex-equation`, `ex-table`, `ex-code`, `ex-note`; lớp riêng `stream-*` trong phạm vi `.lecture-stream` |
| nhẹ | CSS | `stream-question`, `stream-accent`, `stream-figure` trùng giá trị `ann-question`, `ann-accent`, `ann-figure` của Bài 07 | phương án A: giữ phạm vi hẹp, không chạm Bài 07; trùng lặp có chủ ý, việc nâng thành lớp chung để lượt sau (cần kiểm lại Bài 02, 03, 07) |
| nhẹ | P00, h1, giả mã, cấu hình | bìa chưa theo `title-slide`; `h1` ở A00, K00, R00, B00, C00, X00; giả mã `div.code`; thiếu khối nạp KaTeX cho cửa sổ ghi chú | theo mẫu Bài 07 |
| — | `index.html` | Bài 8 chưa có mục | thêm thẻ Bài 8 với liên kết deck; ghi chú để "Chưa có" cho tới khi qua kiểm định |

Không đổi chữ: tác tử biên tập so chữ đã bỏ thẻ của 55 trang kể cả ghi chú diễn giả, không trang nào khác. Kiểm của điều phối viên: đọc diff ba tệp; `check08.py` (Playwright Chromium, cổng 8772) 55 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 phần tử vượt khung, không cuộn ngang; chữ thân nhỏ nhất 28 px trong khung 1280×720 (bảng 25 px, `ex-note` 24 px); P01 72 và X01 78 âm tiết vượt trần từ trước, xử lý ở mạch 1 và 7. Ảnh đã tự xem: P00, K01, X04 (1600×900). Bài 02, 03 ở hai khổ: không phần tử khớp `.lecture-stream`, không lỗi. `git diff --check` sạch.

### Mạch 1. Mở đầu

Trang đổi: P00 (câu luận đề), P04 (mới, "Tiên quyết và quy ước"), P02 ("Mục tiêu học tập"), P03 (sau mục tiêu; "Đọc trước:"), P01 ("Vấn đề trung tâm"). Thứ tự P00 → P04 → P02 → P03 → P01; deck 55 → 56 trang. Ghi chú bài giảng: thay phần đầu tệp bằng phần đầu chương theo khuôn (giới thiệu, liên kết deck tương đối, mục tiêu, tiên quyết chín nhóm, bảng ký hiệu 21 dòng, bản đồ chủ đề `lec-08-topic-01`…`17`); sửa chữ ở các mục cũ ($x\to u$, $B\to b$, $S\to W$). Chi tiết từng trang, âm tiết trước → sau ở `storyboard.md`, mục "Lượt duyệt từng mạch (2026-10-28)".

| Tác tử | Vai | Đầu ra | Quyết định |
|---|---|---|---|
| biên tập deck (tiếp tục bằng `SendMessage`) | sửa deck, storyboard, outline | diff | lượt 1: chấp nhận cấu trúc; lượt 2 sau rà lại: chấp nhận |
| người viết ghi chú (mới) | phần đầu chương, storyboard ghi chú, bản đồ chủ đề trong outline | diff | lượt 1: chấp nhận cấu trúc; lượt 2: chấp nhận |
| rà lại độ chính xác (mới) | số, công thức, nguồn, số hiệu dẫn | `recheck-acc-m1.md` | chấp nhận |
| rà lại mạch, sinh viên, `no-ai-slop` Detect (mới) | thứ tự mạch mở đầu, mật độ, giọng, kết nối | `recheck-story-m1.md` | chấp nhận |

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác, mạch | nghiêm trọng | P00, P01, ghi chú P01, P03; ghi chú bài giảng dòng 3 | khẳng định cả ba cấu trúc dùng bộ nhớ cố định, sai với lấy mẫu theo khóa (mẫu tăng theo dòng, MMDS §4.2.4) | sửa | luận đề 20 âm tiết «Băm khóa giữ trọn nhóm, hồ chứa giữ mẫu cỡ cố định, mảng bit loại hầu hết khóa ngoài tập.»; P01 "mẫu có $\approx r/10$ bộ"; ghi chú: trạng thái quyết định cỡ hằng, mẫu tăng theo dòng |
| độ chính xác, mạch | trung bình | P01, P02, mục tiêu 2 của ghi chú | $s/r$ thiếu $r\ge s$; "vị trí" dễ nhầm với ô của $W$ | sửa | "mỗi phần tử đã đọc … $s/r\ (r\ge s)$" |
| mạch | trung bình | P01 | câu trả lời của từng mạch thiếu điều kiện trên mặt trang; cụm tự đặt trước dấu hai chấm; "trạng thái truy vấn cần" gãy câu | sửa | bốn câu trần thuật mang giả thiết (băm đều; số ngẫu nhiên đều, độc lập; băm đều, độc lập); "trạng thái" giải nghĩa ở ghi chú P04 |
| mạch | trung bình | ghi chú P01 | số 6 hàm băm trông như lấy từ sách | sửa | nêu học phần chọn $k=6$ gần $k^*=8\ln2$; MMDS §4.3.1 dùng một hàm, Ví dụ 4.4 hai hàm |
| mạch | trung bình | ghi chú bài giảng, bản đồ chủ đề | gọi chủ đề bằng mã; đoạn "chu trình rút gọn" là thông tin soạn thảo | sửa | dùng tên và số mục; đoạn soạn thảo chuyển vào storyboard |
| mạch | trung bình | ghi chú bài giảng, mục tiêu và bản đồ | số mục dẫn chiếu chưa khớp thân bài cũ | tồn đọng có chủ đích | **điều kiện chặn công bố ghi chú**: kiểm lại mọi dẫn chiếu mục khi viết xong mạch 7 |
| mạch | trung bình | AT | lời dẫn "trạng thái hữu hạn", cụm khóa "Hợp đồng" | để sau | mạch 2 |
| độ chính xác, mạch | nhẹ (17 mục) | P04, P02, ghi chú P00, P02, P03; ghi chú bài giảng | độc lập chỉ cho hai biến cố; Định lý 06.7 ba bước; miền $\tau$; ba/bốn điều kiện không âm giả; Bài 02 chưa có ghi chú; quan hệ $x_i$ và bộ $t$; "Bài 9"; thuật ngữ Anh của hồ chứa; bảng thuật ngữ trong outline | sửa | theo bảng xử lý của hai tác tử; B06 dùng $x\in S$ cho khóa truy vấn để mạch 5 |

Ngoại lệ mật độ: P01 72 âm tiết, xếp loại trang đối chiếu (trần 80), lý do ở storyboard (bốn câu trả lời có điều kiện, số MMDS). Phần đầu chương của ghi chú 2 890 âm tiết (Bài 06: 2 466): bảng ký hiệu 21 dòng và tiên quyết cho Mục 4 (Bernoulli, tiêu chuẩn lõm chặt, cực tiểu theo dấu đạo hàm).

Kiểm của điều phối viên: đọc diff deck, ghi chú, outline, storyboard; đọc lại câu mở ghi chú sau sửa; `check08.py` toàn deck 56 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 1: P00 51, P04 57, P02 56, P03 39, P01 72 âm tiết; dòng dài nhất 20. Ảnh đã tự xem: P01, P03, P04 (1600×900). Trình xem ghi chú ở 1440×900, 390×844, in: 0 `.katex-error`, không lỗi trình xem, không cuộn ngang trang, liên kết deck tải được; lỗi CSP do máy chủ phát triển chèn script nội tuyến được loại; một cảnh báo KaTeX `\text{bị thay}` ở mục hồ chứa cũ, xử lý ở mạch 4. Ảnh đã tự xem: bảng ký hiệu (1440×900). `git diff --check` sạch.

### Mạch 2. Mô hình tính toán trên dòng

Trang đổi: AT (lời dẫn bỏ "trạng thái hữu hạn", cụm khóa), A05 (mới, "Ví dụ: ba truy vấn trên dòng cảm biến"), A00 (gộp A01; hình mới), A02 ("Chi phí: thuật toán dòng", bảng ba truy vấn), A06 (mới, "Bài tập: trạng thái của phương sai"); bỏ A01, A03; A04 (bảng giữ/bỏ theo người dùng) chuyển sang mạch 3 thành K01B, sau K01. Deck 56 trang. Hình mới `mo-hinh-dong.svg` (vẽ lại MMDS Hình 4.1; dòng viết "5, 3, 0, 4, 7, 2, 5, 1" với nhãn "$x_1=1$ đến trước"; kho lưu trữ nét đứt) và `bang-theo-nguoi-dung.svg`; xóa `stream-model.svg` (không còn trang nào dùng; mũi tên kết quả đi vào ô truy vấn, sai so với MMDS). CSS: thêm `.stream-tall` trong khối `.lecture-stream`. Ghi chú bài giảng: viết lại Mục 1 (1.1–1.6; Định nghĩa 08.1, Thuật toán 08.2, Định nghĩa 08.3, Nhận xét 08.4–08.5, Ví dụ 08.1–08.2, Bài tập 08.1), 2 823 âm tiết; phần bảng giữ/bỏ để dành cho Mục 2.

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác, mạch (điều phối viên phát hiện cùng lúc) | trung bình | A00, `mo-hinh-dong.svg`, ghi chú §1.2 | mũi tên thời gian chỉ sang trái (quy ước MMDS) nên theo hình $x_1=5$, ngược $x_1=1$ của A05 và vết $M$, $T$ | sửa | viết ngược dòng trên hình, nhãn "$x_1=1$ đến trước", sửa desc, alt, ghi chú |
| mạch | trung bình | A04 | phương án lấy mẫu theo người dùng xuất hiện trước lý do (sai lệch của lấy mẫu từng bộ, MMDS §4.2.1) | sửa | chuyển thành K01B sau K01 (đúng vai "phương pháp trước" của cụm thuật toán mạch 3); mạch 2 kết bằng A06 do học phần dựng: trạng thái $r,\sum x_i,\sum x_i^2$, $\sigma_8^2=129/8-(27/8)^2=4{,}734375$ (điều phối viên tự kiểm, và kiểm trực tiếp $37{,}875/8$) |
| mạch | trung bình | A02 | cột "Giá trị lớn nhất" dễ hiểu là mức tối đa; chỉ một truy vấn | sửa | bảng ba truy vấn: 1 từ/1 so sánh; 2 từ/2 phép cộng; $24+3$ từ/4 phép (bộ đệm vòng) |
| mạch | trung bình | A00 | truy vấn thường trực/tức thời chưa giải nghĩa | sửa | "(chạy liên tục)", "(hỏi một lần)" trên dòng Đầu ra |
| mạch | trung bình | toàn mạch, ghi chú | "truy vấn" hai nghĩa | sửa | ghi chú §1 nêu hai nghĩa; dữ liệu gọi "truy vấn tìm kiếm"; mặt trang mạch 3 xử lý ở lượt sau |
| mạch | trung bình | ghi chú KT | còn "Hợp đồng", "trạng thái hữu hạn"; chưa nhận đầu ra mạch 2 | sửa | viết lại; lời dẫn KT để mạch 3 |
| độ chính xác, mạch | trung bình | ghi chú §1 | Nhận xét 08.4 lấy cửa sổ 24 số làm phản ví dụ cho bộ nhớ không đổi theo $r$; Nhận xét 08.5 nói hồ chứa dùng băm; Thuật toán 08.2 thiếu trường hợp biên | sửa | phản ví dụ "chép cả dòng"; Mục 3 lấy ngẫu nhiên từ số rút; $r=0$ trả $-\infty$ |
| độ chính xác | nhẹ | A05, ghi chú | quy mô 10 số/giây, 3,5 TB thuộc cảm biến độ cao mặt biển (§4.1.2), không phải cảm biến nhiệt độ | sửa | tiêu đề "dòng cảm biến"; câu quy mô nêu đúng loại cảm biến |
| độ chính xác | nhẹ | A02, ghi chú | trạng thái cửa sổ đếm thiếu | sửa | tổng chạy, vị trí ghi, số đếm $\min(r,24)$ |
| độ chính xác | nhẹ | K01B | số rút của An (0) khác $h(\text{An})=1$ ở K02 | để sau | mạch 3 |
| mạch | nhẹ (11 mục khác) | AT, A00, A02, outline, storyboard, ghi chú §1 | thuật ngữ Anh, thứ tự câu, meta description, chủ ngữ là bộ trang chiếu, "từ máy" chưa giải nghĩa | sửa | theo bảng xử lý của hai tác tử |

Thời lượng tạm 121,5 phút (K01B mang 2,5 phút sang mạch 3), cân lại ở mạch 3. Ghi chú diễn giả A05, A00 đúng 150 âm tiết (trần).

Kiểm của điều phối viên: đọc diff deck, SVG, ghi chú, planning; `check08.py` toàn deck 56 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 2: AT 37, A05 59, A00 57, A02 58 (trần 80), A06 28 âm tiết; dòng dài nhất 19. Ảnh đã tự xem: A05, A00 (trước và sau sửa hình), A02, A04/K01B (1600×900). Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem, không cuộn ngang trang. Hình trong trình xem kế thừa `min-width: 900px` của CSS trình xem nên cuộn ngang trong khung riêng ở 1440 và 390 (có ở mọi bài, không thuộc phạm vi lượt này). `git diff --check` sạch.

### Mạch 3. Lấy mẫu theo khóa

Trang đổi: KT (lời dẫn ≤ 20 âm tiết/dòng; ghi chú nhận đầu ra mạch 2), K01 ("Ví dụ: ba bộ truy vấn của An", tính tay $1/100$, $18/100$, $1/19$), K09 (mới, "Sai lệch của mẫu từng bộ", $d/(10u+19d)$), K01B (bảng giữ/bỏ chuyển từ mạch 2), K02 ("Hàm băm thay bảng nhãn", hình mới), K04 ("Thuật toán: lấy mẫu theo khóa", gộp đặc tả K03), K05 ("Tính đúng: …"), K06 ("Chọn khóa lấy mẫu"), K07 ("Chi phí: …"), K08 ("Ngưỡng băm và khóa nhiều bộ"); bỏ K00, K03; ghi chú A06 thêm câu nối. Deck 55 trang. Hình: `bam-theo-nguoi-dung.svg` (mới), `bang-theo-nguoi-dung.svg` vẽ lại; xóa `key-sampling.svg` (tỷ lệ 30%, không còn trang nào dùng). Tỷ lệ $1/10$ ($b=10$, $a=1$) thống nhất trong cả mạch theo quyết định của điều phối viên; ví dụ 30% của slide MMDS Streams 1 chỉ nhắc trong ghi chú. Ghi chú bài giảng: ba mục cũ 2–4 thay bằng "## 2. Lấy mẫu theo khóa" (2.1–2.5; Mệnh đề 08.6, Nhận xét 08.7, Định nghĩa 08.8, Thuật toán 08.9, Mệnh đề 08.10, Nhận xét 08.11, Hệ quả 08.12, Thuật toán 08.13, Mệnh đề 08.14; Ví dụ 08.3–08.7; Bài tập 08.2–08.3), 4 627 âm tiết.

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác, mạch | nghiêm trọng | K01 ↔ K01B, K02, hai SVG, ghi chú K01B, K02, K05; Ví dụ 08.4, 08.5, 08.7 | dữ kiện An đổi giữa các trang: K01 ba bộ, các trang sau hai bộ "đồ thị" ("băm" thuộc Bình), nên "tỷ lệ lặp của An trên mẫu là $1/2$" sai (thực là 1) | sửa | một dòng năm bộ dùng chung: (An, "đồ thị"), (Bình, "lọc"), (An, "băm"), (An, "đồ thị"), (Chi, "lọc"); vẽ lại hai hình; tính lại Ví dụ 08.4 (bảng 3 hàng), 08.5 (3, 4, 5 bộ), 08.7 (điều phối viên tự chạy lại: $r=4$ xóa Bình, $\tau=6$; $r=5$ xóa Chi, $\tau=3$) |
| độ chính xác | trung bình | ghi chú, Thuật toán 08.13 | chi phí bỏ sót tới $b$ lần giảm $\tau$ qua giá trị trống khi $b$ rất lớn | sửa | bước dọn dạng nhảy theo MMDS §4.2.4 (chỉ mục theo giá trị băm, $\tau\gets v-1$); kiểm lại bất biến Mệnh đề 08.14 |
| mạch | trung bình | K01, K09 | "tỷ lệ lặp" chưa định nghĩa; mẫu số thiếu bước; lý do $1/29\ne1/19$ chỉ ở ghi chú | sửa | "1 trong 2 truy vấn được gõ lại"; mẫu số $u/10+d/100+18d/100$; một dòng lý do |
| mạch | trung bình | K04, KT | $a$, $b$ chưa có tên; "phát vào dòng mẫu" dịch sát chữ | sửa | "số ngăn $b$", "ngưỡng $a$", "đưa $t$ vào mẫu" |
| độ chính xác, mạch | trung bình / nhẹ | ghi chú K06; ghi chú bài giảng sau Mệnh đề 08.10 | giả thiết "đều theo từng khóa" chỉ cho xác suất biên, ngầm dùng độc lập giữa các khóa | sửa | nêu giả thiết thêm; phản ví dụ họ hàm hằng; "hàm luôn trả 0" thêm $1\le a<b$ |
| mạch | trung bình | A06 → KT | thiếu câu nối | sửa | câu cuối ghi chú A06 |
| mạch | trung bình | K04 | giả mã lệch dấu tiếng Việt trên ảnh chụp | không sửa | do phông monospace của máy chụp headless; mã nguồn NFC; Bài 07 cùng hiện tượng |
| độ chính xác | nhẹ | mở Mục 2, kết Mục 1 | "mọi thống kê trên mọi phần tử có trạng thái cỡ hằng" khái quát quá mức | sửa | "một số thống kê, như giá trị lớn nhất, trung bình và phương sai" |
| mạch | nhẹ (12 mục) | K02, K06, K07, K08, K09, ghi chú | 1,6 GB chưa thuyết phục; dòng nguồn trên mặt trang K07; nhãn Câu hỏi trước dữ kiện ở K08; tên cột K09 | sửa | theo bảng xử lý của tác tử biên tập; "thời gian"/"thời điểm" trong bộ (người dùng, truy vấn, …): deck giữ "thời gian" (khớp "time" của MMDS), ghi chú đồng bộ ở lượt sau |
| mạch | nhẹ | RT | "xác suất biên" đột ngột | để sau | mạch 4 |

Thời lượng tạm 117 phút (mạch 3: 24 phút); 3 phút còn lại phân ở mạch 4–5.

Kiểm của điều phối viên: đọc diff deck, SVG, ghi chú, planning; tự kiểm công thức $dp/(u+(2-p)d)$ với $p=1/10$ cho $d/(10u+19d)$; `check08.py` toàn deck 55 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 3 cao nhất K01B 58, K01 56, K06 55 âm tiết; dòng dài nhất 20. Ảnh đã tự xem: K01, K02 (trước sửa), K01B (sau sửa). Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem, không cuộn ngang trang. `git diff --check` sạch.

### Mạch 4. Lấy mẫu hồ chứa

Trang đổi: RT (lời dẫn không KaTeX, bỏ "xác suất biên"), R00 ("Mẫu cỡ cố định", ví dụ $s=2$ của slide MMDS Streams 1 tr.18), R01 ("Ý tưởng lấy mẫu hồ chứa", so với mẫu theo khóa), R03 ("Ví dụ: vết chạy hồ chứa hai ô"), R04 ("Thuật toán: …", gộp đặc tả R02; giả mã dùng $W$, khởi tạo $r$), R05 ("Tính đúng: …"), R06, R07 ("Chứng minh: xác suất có mặt, phần tử mới/cũ"; giả thiết quy nạp và tính độc lập của $j$ hiện trên mặt trang), R08 ("Chi phí: …"), R09 (mới, "Hồ chứa và mẫu theo khóa" + câu hỏi An 10 bộ); bỏ R02. Deck 55 trang. Hình mới `reservoir-mini.svg`, `reservoir-step.svg`; `reservoir-trace.svg` nâng cỡ chữ. CSS: biến `--r-code-font` trong khối `.lecture-stream` (Consolas, "SF Mono", "Liberation Mono", "Noto Mono", "Courier New", monospace) vì `monospace` phân giải thành DejaVu Sans Mono làm tách dấu tiếng Việt trong giả mã. Ghi chú bài giảng: "## 5." cũ thay bằng "## 3. Lấy mẫu hồ chứa" (Định nghĩa 08.15, Thuật toán 08.16, Định lý 08.17, Mệnh đề 08.18 mọi tập con đồng khả năng (bổ sung), Mệnh đề 08.19, Nhận xét 08.20–08.21, Ví dụ 08.8–08.10, Bài tập 08.4), 3 291 âm tiết; hết cảnh báo KaTeX `\text{bị thay}`; ghi chú đồng bộ "thời gian" trong bộ (người dùng, truy vấn, thời gian).

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch | trung bình | K04, R04, B04 | giả mã tách dấu tiếng Việt (phông DejaVu Sans Mono) | sửa | ngăn xếp phông có tiếng Việt trong phạm vi `.lecture-stream`; tác tử rà đã thử bằng Playwright; điều phối viên xem ảnh R04 sau sửa. Bài 07 còn lỗi, đề xuất nâng thành lớp chung ở lượt sau |
| mạch | trung bình | R00, R03, ghi chú | tên phần tử a, x, c, y, z in nghiêng KaTeX, trùng $a$, $x_i$, $y$ | sửa | chữ đứng |
| mạch | trung bình | R01 | so sánh với mẫu theo khóa sai (mẫu theo khóa không rút số mới mỗi quyết định) | sửa | giống ở quy tắc ngưỡng $j\le s$ / $h(K)<a$; khác ở rút lại mỗi vị trí và có thể thay |
| mạch | trung bình | R04, R05, R07, R08, ghi chú | "độc lập với lịch sử" mơ hồ | sửa | "độc lập với các lần rút trước (và với nội dung $W$)" |
| mạch | trung bình | R08, Mệnh đề 08.19 | "mô hình RAM" lệch mô hình đếm của các mạch trước | sửa | đếm phép toán mỗi phần tử, rút một số đều tính 1 phép, bộ nhớ bằng từ máy |
| mạch | trung bình | `reservoir-step.svg`, R07 | chú thích $4/5$ thiếu điều kiện; R07 chật | sửa | "khi $x_i$ đang ở ô 1"; R07 bỏ hình (trùng R06), thêm dòng ví dụ $\frac24\cdot\frac45=\frac25$ |
| độ chính xác | nhẹ | Nhận xét 08.20 | "lệch như Mục 2.1" sai vì hồ chứa không giữ vị trí độc lập | sửa | dẫn tỷ số $\frac{dp_2}{up+2dp-dp_2}$ với $p_2=\frac{s(s-1)}{r(r-1)}$; bằng $d/(u+d)$ khi và chỉ khi $p_2=p$; lệch xuống khi $s<r$ (điều phối viên tự kiểm) |
| độ chính xác | nhẹ | ghi chú R07 | mô tả sai phép tính của slide MMDS tr.21 | sửa | $(1-\frac{s}{r+1})+\frac{s}{r+1}\cdot\frac{s-1}{s}=\frac{r}{r+1}$ |
| mạch, độ chính xác | nhẹ (9 mục) | R00, R06, R09, `reservoir-mini.svg`, Mệnh đề 08.18 | "khi được giữ"; dòng ví dụ R06; R09 7 dòng → 6; desc hình; biến $y$ trùng khóa truy vấn Bloom → $\ell$ | sửa | — |
| mạch | trung bình | BT | lời dẫn dùng "hữu hạn", "dương giả" chưa định nghĩa | để sau | mạch 5 |

Tác tử độ chính xác tự kiểm vết chạy, $2/3$, $2/4$, $2/5$, bước quy nạp, Mệnh đề 08.18 (liệt kê 12 kết cục với $r=4$, $s=2$), phản ví dụ phụ thuộc ($1/6$), số lần ghi kỳ vọng ($920{,}53$; cận $1\,020{,}04$ và $1\,021{,}03$), $\binom{990}{90}/\binom{1000}{100}\approx6{,}6\cdot10^{-11}$; không có phát hiện từ mức trung bình trở lên. Điều phối viên tự kiểm $100(H_{10^6}-H_{100})\approx920{,}53$.

Thời lượng tạm 116 phút (mạch 4: 25 phút); mạch 5–6 nhận phần còn lại.

Kiểm của điều phối viên: đọc diff deck, CSS, SVG, ghi chú, planning; `check08.py` toàn deck 55 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 4 cao nhất R00, R01, R05 58 âm tiết; R09 6 dòng. Ảnh đã tự xem: R04 (trước và sau đổi phông), R07 (trước sửa). Tác tử biên tập mở Bài 02, 03 ở hai khổ sau khi đổi CSS: không phần tử khớp `.lecture-stream`, không lỗi. Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem, không cảnh báo KaTeX. `git diff --check` sạch.

### Mạch 5. Lọc thành viên bằng Bloom filter

Trang đổi: BT (lời dẫn bỏ "hữu hạn", "dương giả" chưa định nghĩa, cấu trúc "đổi A lấy B"), B00 ("Lọc theo danh sách cho phép", ≥ 20 GB so với 1 GB), B02 ("Ý tưởng Bloom filter", so với mạch 3, nhận xét bit 0), B05 ("Ví dụ: Bloom filter 11 bit, thêm ba khóa", tính tay 159), B05B (mới, "…, kiểm tra hai khóa": 118 bị loại, 29 dương giả), B01 ("Đặc tả Bloom filter", Định nghĩa dương giả/âm giả ngay sau ví dụ), B03, B04 ("Thuật toán: xây Bloom filter / kiểm tra thành viên"), B06 ("Tính đúng: không có âm giả", hai giả thiết, chứng minh trên mặt trang), B07 ("Xác suất một bit bằng 1", mô hình phi tiêu, $k=1$: 0,1175), B08 ("Xác suất dương giả"), B09 ("Ảnh hưởng của số hàm băm", câu hỏi $p(k)\to1$ thay Bài tập 4.3.2 của phần thực hành), B10 ("Số hàm băm tối ưu", "Ý nghĩa:" $q=1/2$; chứng minh đầy đủ ở ghi chú bài giảng và bài tập 4.3.3), B11 ("Ví dụ: tám bit mỗi khóa"), B12 ("Chi phí: Bloom filter", câu hỏi $2\cdot10^9$ địa chỉ: $p(6)\approx0{,}2198$, chọn $k=3$). Deck 56 trang. Hình mới `bloom-11bit-them.svg`, `bloom-11bit-mini.svg`; sửa `bloom-pipeline.svg` (đường nhánh loại thiếu `fill="none"` tô đen che chữ — lỗi có từ trước; nét đứt cho nhánh loại) và `fpr-curve.svg` (vạch $k^*\approx5{,}545$, chữ 26); xóa `bloom-11bit.svg` (không còn dùng). Ghi chú bài giảng: các mục cũ 6–9 thay bằng "## 4. Lọc thành viên bằng Bloom filter" (4.1–4.7; Định nghĩa 08.22, Thuật toán 08.23–08.24, Định lý 08.25, Bổ đề 08.26, Mệnh đề 08.27, Định lý 08.28 chứng minh đủ bước xét dấu bằng tính lõm chặt và phản đối xứng, Hệ quả 08.29, Nhận xét 08.30–08.31, Ví dụ 08.11–08.16, Bài tập 08.5), 4 337 âm tiết; ký hiệu giá trị băm ở Mục 2 đổi $v\to c$ để $v$ chỉ khóa chèn.

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác, mạch, người viết ghi chú | trung bình | B08 mặt trang và ghi chú | lý do của xấp xỉ $q^k$ sai: "$k$ vị trí có thể trùng" (vị trí trùng đã được tính đúng trong $(X/n)^k$) và "bit phụ thuộc ⇒ ≥" sai chiều | sửa | "Xấp xỉ thứ nhất: $p_{FP}=\mathbb E[(X/n)^k]\ge q^k$" (Jensen); "Xấp xỉ thứ hai: … $p(k)\le q^k$"; khớp Mệnh đề 08.27 |
| mạch | trung bình | B05B | chú thích hình không khớp nét vẽ; cột Bit của 118 trái phép dừng sớm | sửa | chú thích theo nét; "0 (dừng)" |
| mạch | trung bình | B10 | dòng Chứng minh thiếu bước xét dấu | sửa | điểm dừng duy nhất, âm trước dương sau $k^*$ |
| mạch | trung bình | ghi chú bài giảng, Định lý 08.28 | thiếu câu nêu hướng trước khi đổi biến | sửa | câu hướng đi + kiểm số $\lambda'(5)<0<\lambda'(6)$ với $n/m=8$ |
| độ chính xác | nhẹ | ghi chú bài giảng (~1034) | lý do các bit phụ thuộc chưa đúng | sửa | $\Pr[B[c]=B[c']=0]=(1-2/n)^{km}<(1-1/n)^{2km}$: tương quan âm; Mệnh đề 08.27 không cần độc lập. Báo cáo rà lại viết bất đẳng thức ngược chiều; người viết ghi chú và điều phối viên kiểm: $1-2/n<(1-1/n)^2$ |
| độ chính xác | nhẹ | ghi chú B11, Ví dụ 08.16 | 0,0235 của slide MMDS Streams 2 tr.14 | sửa | slide viết sai công thức $(1-e^{-1/6})^2$; đúng $(1-e^{-6/8})^6=0{,}0216$; slide CS246 2026 tr.32–33 đã sửa |
| độ chính xác, mạch | nhẹ (9 mục) | B07, B10 ghi chú, B12, B01, B09, B11, `bloom-pipeline.svg`, Ví dụ 08.14 | $B[\ell]\to B[c]$; $x=k\rho\to z$; B12 61 → 45 âm tiết; Đầu ra nêu mảng $B$; hai thẻ B09 chỉ phân biệt bằng màu → "giúp"/"hại"; "mảng đầy gấp đôi" | sửa | — |
| mạch | nhẹ | CT | lời dẫn 22 âm tiết | để sau | mạch 6 |

Sự cố trong lượt viết Mục 4: người viết ghi chú dùng một regex đổi ký hiệu qua ranh giới `$…$` làm hỏng chữ ở Mục 2 trong bản làm việc chưa commit, rồi khôi phục tệp về HEAD bằng `git checkout` (chỉ mất phần sửa của chính nó) và làm lại bằng thay thế chính xác từng dòng; điều phối viên đã yêu cầu không dùng regex qua `$…$` và không dùng `git checkout` lên tệp ở các lượt sau. Diff cuối chỉ chạm các dòng dự định.

Tác tử độ chính xác tự kiểm: mảng 11 bit (khớp Ullman 2017 tr.6), khóa 29, bảng $p(k)$ với $k=1..10$, $k^*$, liệt kê $11^6$ kết cục ($q=0{,}435526$, $p_{FP}=0{,}195081$), chứng minh Định lý 08.28. Điều phối viên tự kiểm $1-e^{-1/8}$, $(1-e^{-1/4})^2$, $p(5)$, $p(6)$, $2^{-5{,}545}$, $p(2)$ và $p(3)$ với $n/m=4$, $(1-e^{-6/11})^2\approx0{,}1768$.

Thời lượng: mạch 5 40,5 phút; tổng tạm 113 phút với mạch 6 cũ (5 phút); mạch 6 cần khoảng 12 phút.

Kiểm của điều phối viên: đọc diff deck, SVG, ghi chú, planning; `check08.py` toàn deck 56 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; mạch 5 cao nhất B01 55, B06 53 âm tiết; dòng dài nhất 19. Ảnh đã tự xem: B05, B05B (1600×900). Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem, không cảnh báo KaTeX. `git diff --check` sạch.

### Mạch 6. Tổng kết và chuyển tiếp

Trang đổi: CT (lời dẫn ≤ 20 âm tiết/dòng), C00 ("Kết quả và giả thiết không được bỏ", bảng ba cột theo mẫu), C03 (mới, "Thuật toán, bảo đảm và chi phí", bảng bốn cột), C01 ("Câu trả lời cho vấn đề trung tâm", có điều kiện và số của tình huống mở đầu), C04, C05 (mới, "Câu hỏi tự kiểm tra, câu 1–2 / 3–4", mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng."; câu 1 → mục tiêu 1, câu 2 → mục tiêu 2 kể cả giả thiết dùng ở bước quy nạp, câu 3–4 → mục tiêu 3), C02 ("Nguồn và tài liệu đọc": MMDS 2020 ấn bản 3 §§4.1–4.3 tr.131–142 và §4.5.5 tr.148–150, slide MMDS, CS246 2026, Ullman 2017, ghi công http://www.mmds.org, liên kết trình xem ghi chú, dòng nối Bài 09 có liên kết deck); ghi chú R00, R01, R04, R05, R07, R08 thêm nguồn MMDS §4.5.5; K01 "tỷ lệ truy vấn tìm kiếm lặp". Deck 59 trang; phần giảng 120 phút (6,5 + 12 + 24 + 25 + 40,5 + 12). Ghi chú bài giảng: "## 10." cũ thay bằng "## 5. Chọn cấu trúc theo câu hỏi" (bảng 9 kết quả, bảng 5 thuật toán, trả lời vấn đề trung tâm, Ví dụ 08.17), "## Tình huống áp dụng và ứng dụng" (Tình huống 08.1–08.3, 08.3 vi phạm giả thiết: xóa địa chỉ bằng đặt bit 0; liên kết Bài 09 Mục 2, Mục 5), "## Tóm tắt chương" (8 câu tường thuật, kết quả theo mục, công thức và thuật toán cần nhớ, giả thiết hay bị quên); mọi dẫn chiếu "Mục k" đã khớp thân bài (điều kiện chặn công bố ghi ở mạch 1 đã gỡ cho phần đã viết). Cả chương 22 062 âm tiết (còn chứa "## 11." và "Tóm tắt nguồn" cũ, xử lý ở mạch 7).

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| độ chính xác | trung bình | ghi chú C02 | "sách không trình bày thuật toán [hồ chứa]" sai: MMDS §4.5.5 tr.148–149 có kỹ thuật chọn vị trí với xác suất $s/n$ và quy nạp; hộp tr.150 nối với lấy mẫu theo khóa | sửa | điều phối viên đối chiếu pdftotext (dòng 829–899 của bản văn bản chương 4); thêm §4.5.5 vào C02 (mặt trang và ghi chú), ghi chú mạch 4 và Mục 3 của ghi chú bài giảng; "không có bài tập hồ chứa" giữ (bài tập §4.5.6 chỉ về mômen) |
| độ chính xác | trung bình | ghi chú bài giảng, Tình huống 08.1 | dùng Mệnh đề 08.10(b) cho ngưỡng giảm dần như thể chính xác | sửa | gần đúng khi mỗi khóa rất nhỏ so với $G$; trường hợp cực đoan khóa có hơn $G$ bộ luôn bị loại (điều phối viên kiểm lập luận) |
| độ chính xác, mạch | trung bình / nhẹ | C01 | "$1/29$" thiếu điều kiện; hồ chứa thiếu $r\ge s$; "băm đều" gắn cả vào không âm giả | sửa | "cho An $1/29$"; "$r\ge s$"; tách câu không âm giả (chỉ cần mảng chỉ được đọc, cùng hàm băm) với câu khoảng 2% (cần băm đều, độc lập) |
| độ chính xác, mạch | nhẹ (8 mục) | C00, C04, K01, tóm tắt chương, Tình huống 08.3 | hàng dương giả thiếu $y\notin S$; C04 câu 2 chưa kiểm phần quy nạp; "truy vấn" hai nghĩa ở K01; khẳng định mới về tập trung quanh $a/b$ ở tóm tắt; Tình huống 08.3 chép lời giải Bài tập 08.5 | sửa | — |
| mạch | nhẹ | C02 | liên kết tới deck Bài 09 khi Bài 09 chưa có trên index | giữ | CLAUDE.md cho phép dòng nối khi `sources/source.md` hỗ trợ (dòng 401, 423, 443); tệp tồn tại, HTTP 200 |
| mạch | nhẹ | ghi chú bài giảng | nhãn "Dẫn ngược lý thuyết" ngoài khuôn | giữ | AGENTS.md §"Ứng dụng ngược về lý thuyết"; ghi chú Bài 06 dùng cùng nhãn |

Ngoại lệ mật độ (trần 80): C00 74 và C03 61 (bảng tổng kết), C01 76 (trang đối chiếu, như P01); lý do ở storyboard. Tác tử mạch rà thêm toàn deck 59 trang từ góc nhìn sinh viên: lập luận giữa các mạch liền, lỗi các lượt 1–5 đã sửa; còn lại ở mạch 7 ("Sản phẩm:", $p_3$, $p_4$, X01 78 âm tiết).

Kiểm của điều phối viên: đọc diff deck, ghi chú, planning; tự kiểm $16\ln2\approx11{,}09$, $2^{-11{,}09}\approx4{,}6\cdot10^{-4}=0{,}0214^2$; `check08.py` toàn deck 59 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang; liên kết trình xem ghi chú và deck Bài 09: HTTP 200. Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem, không cảnh báo KaTeX. `git diff --check` sạch.

### Mạch 7. Bài tập vận dụng

Trang đổi: XT (lời dẫn bỏ nhận xét biên soạn), X01 ("Bài tập: chọn khóa lấy mẫu", dữ kiện trước câu hỏi, ý (a)–(c) bằng `ol.stream-alpha`), X02 ("Bài tập: dương giả với ba và bốn hàm băm", $p(k)$), X03 ("Bài tập: chia mảng bit", quy ước $k\mid n$ và băm đều, độc lập ghi là của học phần), X04 ("Bài tập: số hàm băm tối ưu"), X04B (mới, "Lời giải:" cùng tiêu đề: $\lambda'=\phi(\theta)/(1-\theta)$, $\phi$ lõm chặt trên $(0,1/2)$, phản đối xứng, quy tắc số nguyên); bỏ X00, X05 (trang điều phối lớp). Deck 58 trang; thực hành 60 phút (XT 0,5; X01 14,5; X02 10; X03 15; X04 12; X04B 8). Đề giữ đúng MMDS Ex.4.2.1 (§4.2.5, tr.138), Ex.4.3.1–4.3.2 (§4.3.4, tr.141), Ex.4.3.3 (tr.142); tác tử biên tập và tác tử độ chính xác đối chiếu nguyên văn. CSS: `ol.stream-alpha` trong khối `.lecture-stream` (theme ghi đè `type="a"`). Lượt sửa cuối cùng lượt này: P03 "Đọc trước:" thêm §4.5.5; alt hình K01B khớp năm bộ; ghi chú B06 nêu hai điều kiện tự thỏa của Định lý 08.25; ghi chú B05 ghi năm 2017 (ngày cũ lấy từ siêu dữ liệu PDF). Ghi chú bài giảng: "## 11." cũ thay bằng "## Bài tập củng cố" (ba mức; Bài tập 08.6–08.14, mỗi bài có `hint` và `solution`; Bài tập 08.10–08.13 là bốn bài MMDS, 08.14 mở rộng theo hộp tr.150) và "Tóm tắt nguồn" cũ thay bằng "## Hướng dẫn đọc thêm và tài liệu tham khảo"; đầu Mục 1 thêm hình `cau-truc-chuong.svg` và đoạn đọc hình (AGENTS.md §"Cấu trúc bắt buộc của một chương", mục 7).

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch | trung bình | X01 | dữ kiện chen giữa câu hỏi và danh sách ý | sửa | dữ kiện lên trước; X02, X03 cùng mẫu |
| kiểm định cuối | trung bình | ghi chú (F1) | chữ hai nghĩa: $k$ chỉ số tổng, $p$ tỷ lệ giữ, $T$, $c$ | sửa | $k\to i$, $p\to\eta$, $T\to A$; gạch đầu dòng ký hiệu cục bộ sau bảng ký hiệu |
| kiểm định cuối | trung bình | ghi chú, đầu Mục 1 (F6) | thiếu hình cấu trúc chương có đoạn đọc hình | sửa | `cau-truc-chuong.svg` (ba nhánh, câu hỏi và bảo đảm từng nhánh, hội tụ Mục 5); điều phối viên đã xem ảnh. Lượt đầu điều phối viên bỏ qua yêu cầu này vì tìm sai từ khóa trong AGENTS.md; đã đính chính |
| kiểm định cuối | trung bình | B06, C00, C01 ↔ Định lý 08.25 (F3) | deck hai giả thiết, ghi chú bốn | hòa giải | mặt trang giữ hai giả thiết; ghi chú diễn giả B06 và ghi chú bài giảng nêu hai điều kiện còn lại tự thỏa trong mô hình của bài (hàm tất định; truy vấn sau khi ghi xong) |
| kiểm định cuối, mạch | trung bình | X04 (F4) | câu điều phối lớp trong ghi chú diễn giả | sửa | bỏ |
| kiểm định cuối | trung bình | `review-log.md` (F2) | thiếu mục mạch 7, bảng kiểm định ghi chú và bảng nguồn theo mục | sửa | mục này và hai bảng dưới |
| kiểm định cuối, mạch, độ chính xác | nhẹ (16 mục) | ghi chú (F7, F9–F14), storyboard (F5, F15, F16), alt K01B (F8), X04B, P03, outline, tham khảo | trực giác sau định nghĩa; thiếu "Trong thực hành" sau Mệnh đề 08.14 và "Bỏ …" sau Mệnh đề 08.27; năm câu no-ai-slop; "slide" chưa dịch; câu nối lặp; "định cỡ 1%"; ngày Ullman; năm bản Blum–Hopcroft–Kannan; §1.3.5 tr.13–14; "đáp án và rubric" trong outline | sửa | — |
| kiểm định cuối | nhẹ | trình xem ghi chú | CSS chung của trình xem đặt hình rộng tối thiểu 900 px nên ở 1440 mép phải hình cần cuộn ngang trong khung riêng | tồn đọng | có ở mọi bài; sửa cần đổi `material-viewer.css` dùng chung, ngoài phạm vi lượt này |
| kiểm định cuối | nhẹ | ghi chú, đầu Mục 1 | đoạn mở Mục 1 lặp ý đoạn giới thiệu chương | tồn đọng | không chặn; để lượt rà văn phong ghi chú sau |

Tác tử kiểm định cuối (mới, `general-purpose`, `model: "opus"`, `effort: "high"`) kiểm độc lập toàn deck theo `slide_authoring_standard.md` và ghi chú theo AGENTS.md §"Kiểm định ghi chú bài giảng" (`final-verify-08.md`), rồi kiểm lại sau lượt sửa (`final-verify-08-r2.md`): không phát hiện chặn bàn giao hay nghiêm trọng; mọi phát hiện từ mức trung bình đã xử lý; ghi chú đủ điều kiện liên kết trên index; deck đạt.

#### Kiểm định ghi chú bài giảng (AGENTS.md §"Kiểm định ghi chú bài giảng")

| Mục kiểm | Kết quả | Bằng chứng |
|---|---|---|
| Cấu trúc chương bắt buộc (tiêu đề, giới thiệu ≤ 1 đoạn và liên kết deck, mục tiêu, tiên quyết, bảng ký hiệu, bản đồ chủ đề, Mục 1–5, tình huống, tóm tắt, bài tập ba mức, tham khảo) | đạt | đủ 11 phần; liên kết deck tương đối, HTTP 200 |
| `note-topic-id` | đạt | 17 mã `lec-08-topic-01`…`17`, chữ thường, mỗi mã một lần; trình xem chấp nhận và ẩn |
| Đánh số | đạt | bộ đếm chung 08.1–08.31; Ví dụ 08.1–08.17; Bài tập 08.1–08.14; Tình huống 08.1–08.3; mọi dẫn chiếu khớp |
| Định lý bốn phần, thuật toán đủ thành phần, chứng minh có bước và $\square$ | đạt | Định lý 08.17, 08.25, 08.28; Thuật toán 08.2, 08.9, 08.13, 08.16, 08.23, 08.24 |
| Mục 1 mở đúng mẫu (kết quả bài trước, bài toán có số, điều chương xây dựng, hình cấu trúc chương) | đạt | `cau-truc-chuong.svg` và đoạn đọc hình |
| Ví dụ số trước phát biểu tổng quát, ví dụ giải sau; "Trong thực hành"; đoạn kết mục | đạt | mỗi mục 1–4; Nhận xét 08.5, 08.11, 08.21, 08.31 và đoạn sau Mệnh đề 08.14 |
| Tình huống ≥ 2, một tình huống vi phạm giả thiết, dẫn ngược lý thuyết | đạt | Tình huống 08.1–08.3; 08.3 xóa địa chỉ bằng đặt bit 0 |
| Tóm tắt chương 5–8 câu, kết quả theo mục, công thức cần nhớ, giả thiết hay quên | đạt | 8 câu |
| Bài tập ba mức có gợi ý và lời giải, gồm bài của phần thực hành; mỗi mục tiêu có bài | đạt | Bài tập 08.6–08.14; ánh xạ mục tiêu ở đầu phần bài tập |
| Tham khảo có ghi công `http://www.mmds.org` | đạt | — |
| Giọng văn (không lấy tài liệu làm chủ ngữ; "chúng ta"/"ta" đúng chỗ; không "hãy" ngoài đề; không "Đáp án") | đạt | grep chuỗi cấm = 0 |
| Mỗi chữ một nghĩa | đạt sau sửa F1 | — |
| Độ dài | đạt | 24 159 âm tiết (khung 12 000–32 000) |
| Hiển thị 1440×900, 390×844, in | đạt | 0 `.katex-error`, không lỗi trình xem, không cuộn ngang trang, 40 khối gập mở bằng bàn phím và hiện khi in; lỗi CSP do `reloadserver` chèn script nội tuyến được loại (tác tử biên tập kiểm lại bằng `python3 -m http.server`: không lỗi) |

#### Nguồn và giáo trình đã tham khảo theo mục

| Mục ghi chú / mạch deck | Nguồn nội dung | Tham khảo cách dẫn dắt |
|---|---|---|
| Mở đầu, Mục 1 / mạch 1–2 | MMDS 3e §4.1 tr.131–135 (Hình 4.1, Ví dụ 4.1), §1.3.5 tr.13–14 | CLRS 4e §2.1 (bất biến vòng lặp cho Thuật toán 08.2); giọng *Học máy thống kê* |
| Mục 2 / mạch 3 | MMDS §4.2 tr.136–138; slide MMDS Streams 1 tr.12–16; CS246 2026 tr.13–14 (phép đếm sai lệch) | CLRS 4e §2.1 (Mệnh đề 08.14) |
| Mục 3 / mạch 4 | MMDS §4.5.5 tr.148–149 và hộp tr.150; slide MMDS Streams 1 tr.18–21 | Blum–Hopcroft–Kannan, bản 04/01/2018, §6.1 tr.181 (đọc thêm) |
| Mục 4 / mạch 5 | MMDS §4.3 tr.139–142 (Ví dụ 4.3–4.4); slide MMDS Streams 2 tr.4–14; Ullman 2017 tr.5–8 (ví dụ 11 bit); CS246 2026 tr.32–33 (đường cong) | — |
| Mục 5, tình huống, tóm tắt / mạch 6 | tổng hợp các nguồn trên; ghi chú Bài 09 Mục 2, Mục 5 (liên kết bài sau) | ghi chú Bài 06 (mẫu tình huống, tóm tắt) |
| Bài tập / mạch 7 | MMDS Ex.4.2.1, 4.3.1–4.3.3 | — |

## Tổng kết lượt duyệt từng mạch (2026-10-28)

- Tám commit: fac2f73 (chuẩn bị CSS, index), 1ab32b4 (mạch 1), 3227ef2 (2), 8e0138e (3), 1465082 (4), 6de9aa6 (5), e8f2595 (6) và commit mạch 7 (kèm bật liên kết ghi chú trên index).
- Deck 55 → 58 trang, vẫn 7 mạch; mỗi mạch trừ mở đầu có trang tiêu đề mạch khớp `#/N`; phần giảng 120 phút, thực hành 60 phút. Thêm P04, A05, A06, K09, K01B (chuyển từ A04), B05B, R09, C03, C04, C05, X04B; bỏ A01, A03, K00, K03, R02, X00, X05.
- Hình mới: `mo-hinh-dong.svg`, `bang-theo-nguoi-dung.svg`, `bam-theo-nguoi-dung.svg`, `reservoir-mini.svg`, `reservoir-step.svg`, `bloom-11bit-them.svg`, `bloom-11bit-mini.svg`, `cau-truc-chuong.svg`; sửa `reservoir-trace.svg`, `bloom-pipeline.svg`, `fpr-curve.svg`; xóa `stream-model.svg`, `key-sampling.svg`, `bloom-11bit.svg`. Không raster.
- Ghi chú bài giảng viết lại thành chương giáo trình: 4 943 → 24 159 âm tiết; liên kết trên `index.html`.
- Lỗi nội dung tìm được và đã sửa: bộ nhớ "cố định" gán cho lấy mẫu theo khóa; dữ kiện An lệch giữa các trang; lý do của xấp xỉ $q^k$ (B08) sai; chứng minh $k^*$ thiếu bước xét dấu; khẳng định "sách không trình bày hồ chứa" sai (MMDS §4.5.5); mũi tên thời gian của hình mô hình dòng ngược thứ tự $x_1$; chi phí hạ ngưỡng thiếu số lần giảm $\tau$; số 0,0493 của sách và 0,0235 của slide MMDS được tính lại (0,0489; 0,0216).
- Tồn đọng: (1) lớp `stream-question`, `stream-accent`, `stream-figure` và ngăn xếp phông mã trùng ý với `ann-*` của Bài 07 (Bài 07 còn lỗi tách dấu tiếng Việt trong giả mã) — nên nâng thành lớp chung, cần kiểm Bài 02, 03, 07; (2) CSS chung của trình xem đặt hình tối thiểu 900 px; (3) đoạn mở Mục 1 lặp ý giới thiệu chương; (4) deck Bài 09 được liên kết từ C02 nhưng chưa qua lượt duyệt mới.

Kiểm của điều phối viên trước commit mạch 7: đọc diff deck, CSS (một dòng `ol.stream-alpha`), ghi chú, planning, index; `check08.py` toàn deck 58 trang ở 1600×900 và 390×844: 0 lỗi console/trang, 0 `.katex-error`, 0 yêu cầu mạng ngoài, 0 vượt khung, không cuộn ngang, không dòng > 20 âm tiết; năm trang trên 60 âm tiết đều có ngoại lệ trần 80 (P01 72, C00 74, C03 61, C01 76, X01 68). Ảnh đã tự xem: X01, X04B (1600×900), `cau-truc-chuong.svg`. Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi trình xem. `git diff --check` sạch.

## Lượt biên tập theo bản đánh giá giảng dạy (2026-10-28)

Yêu cầu người dùng (2026-10-28): ghi bản đánh giá giảng dạy 58 slide do người dùng gửi vào một tệp markdown, rồi lần lượt duyệt và chỉnh sửa theo mục tiêu và mười nguyên tắc biên tập của bản đánh giá (mỗi slide một thông điệp; trực quan trước công thức; ví dụ nhỏ chạy tay; phân biệt giả thiết, định lý, chứng minh, kết luận; ký hiệu và điều kiện biên chính xác; không đồng nhất kỳ vọng với giá trị luôn xảy ra hay xấp xỉ với đẳng thức; chứng minh dài chia bước; 16:9 chữ đủ lớn; không hình trang trí; ghi chú giảng viên và câu hỏi khi có giá trị). Bản đánh giá ghi ở `danh-gia-giang-day.md` (cùng thư mục; bỏ phần rác của trang gốc, đổi ký hiệu toán sang `$…$`). Làm theo mạch, commit và push sau mỗi mạch; ghi chú bài giảng đồng bộ cùng mạch.

### Tác tử

Điều phối viên: phiên chính Claude Opus 5.5, effort high. Tác tử con bằng `Agent`, `subagent_type: "general-purpose"`, `model: "opus"`, `effort: "high"`; tiếp tục bằng `SendMessage`.

| Vai | Ghi tệp | Sản phẩm | Quyết định của điều phối viên |
|---|---|---|---|
| lập kế hoạch (mới) | không | `plan-guide-08.md` (scratchpad): quyết định chung, bảng 58 mục, kế hoạch theo mạch, hình mới, số đã kiểm, lỗi của bản đánh giá | chấp nhận; đã tự kiểm $-\ln(0{,}01)/(\ln2)^2\approx9{,}59$, $p(7)\approx0{,}01003$ với $n/m=9{,}585$, $0{,}0214^2\approx4{,}6\cdot10^{-4}$ |
| biên tập deck (tiếp tục) | có | diff | xem từng mạch |
| người viết ghi chú (tiếp tục) | có | diff | xem từng mạch |
| rà lại độ chính xác; rà lại mạch, sinh viên, `no-ai-slop` (tiếp tục) | không | `recheck-acc-g<N>.md`, `recheck-story-g<N>.md` | xem từng mạch |

### Quyết định chung

| Mục | Quyết định | Lý do |
|---|---|---|
| Hoạt cảnh, hiện từng bước, ẩn lời giải, kéo-thả (slide 5, 10, 14, 18, 24, 35, 50, 54) | bác bỏ hình thức; thay bằng trang kế tiếp cùng tiêu đề (B05A → B05B; X01 → X01B; X02 → X02B; X03 → X03B; X04B → X04C) hoặc lời giải trong ghi chú diễn giả | CLAUDE.md "No `fragment`"; AGENTS §trang bài tập |
| Hình, câu hỏi, sơ đồ trên trang tiêu đề mạch (slide 6, 11, 21, 31, 46, 53) | bác bỏ; nội dung đưa vào trang nội dung (ví dụ A07) | AGENTS §Trang tiêu đề mạch |
| Ẩn kết quả khỏi trang Vấn đề trung tâm (slide 5) | bác bỏ | AGENTS: trang Vấn đề trung tâm nêu câu trả lời có điều kiện của từng mạch; C01 thu hồi các số |
| Đổi cấu trúc hai bảng tổng kết (slide 47, 48) | bác bỏ | AGENTS: hai bảng bắt buộc của mạch kết |
| Chia hai buổi 90 phút | bác bỏ | 120 phút giảng + 60 phút thực hành trong một HTML |
| Nhãn, tiêu đề tiếng Anh trên mặt trang | bác bỏ | mặt trang tiếng Việt |
| Nội dung ngoài nguồn trên mặt trang (Flink/Spark, Counting Bloom filter, Welford, concept drift, cluster sampling) | bác bỏ trên mặt trang; Welford và mất chữ số chỉ ở ghi chú bài giảng ("Trong thực hành", dẫn Welford 1962, ghi là bổ sung ngoài nguồn chính) | nguồn nội dung ở `sources/` |
| Dữ liệu tự đặt thay ví dụ xuyên suốt (userID được phép, khảo sát 100 chỗ, mảng 12–16 bit, tỷ lệ 30%) | bác bỏ | ví dụ xuyên suốt đã có: ba bộ của An, dòng năm bộ, mảng 11 bit, lọc thư MMDS |
| Giải trước bài tập trên trang giảng (đạo hàm $k^*$ ở B10; bảng $2\cdot10^9$ địa chỉ ở B12) | bác bỏ | chứng minh $k^*$ thuộc Bài tập 4.3.3; B12 là câu hỏi có lời giải trong ghi chú |
| Lỗi của bản đánh giá (13 chỗ; ví dụ slide 41 "vị trí truy vấn trùng nhau" là nguồn sai số của $q^k$ — sai, đã sửa ở lượt trước; slide 43 $\ell(k)$ trùng ký hiệu, "Ý nghĩa rất đẹp", dẫn "slide 58"; "độc lập với lịch sử"; slide 51 mục tiêu 1% với $k=7$ cho $1{,}004\%$) | không đưa vào deck | chi tiết ở `plan-guide-08.md` mục (v) |
| Trang mới | A07, B05A, X01B, X02B, X03B, X04C (58 → 64 trang) | ví dụ chạy tay; lời giải trang kế tiếp |
| Ghi chú bài giảng | đồng bộ theo mạch, không thêm khối đánh số mới | không dời số hiệu |
| Thời lượng | phần giảng đúng 120 phút sau mạch 5 (storyboard ghi mạch 5 là 40,5 phút nhưng các trang cộng 40: sửa) | — |

### Mạch 1. Mở đầu

Không đổi. Slide 1 (bìa thành sơ đồ có biểu tượng) bác bỏ: bìa theo mẫu `title-slide`, ba đầu ra đã có trong câu luận đề. Slide 2 (ba khối và bảng ký hiệu) một phần: P04 đã có dòng Ký hiệu, thêm khối sẽ vượt trần 60 âm tiết và 6 dòng; phân biệt "hàm băm chọn ngẫu nhiên một lần rồi cố định" và "rút số mới ở mỗi vị trí" đặt ở K02 và R01 (mạch 3, 4). Slide 3 đã đạt. Slide 4 (sơ đồ ba nhánh thay mục lục) bác bỏ: trang Nội dung phải là danh sách đánh số khớp trang tiêu đề mạch; sơ đồ ba nhánh có ở ghi chú bài giảng (`cau-truc-chuong.svg`). Slide 5 bác bỏ trên mặt trang; phân biệt bảo đảm tất định và bảo đảm xác suất đặt ở ghi chú diễn giả C00 (mạch 6). Tác tử rà mạch đồng ý cả năm quyết định.

### Mạch 2. Mô hình tính toán trên dòng

Trang đổi: A07 (mới, "Trạng thái và phép cập nhật", sau A00): định nghĩa trạng thái, phép cập nhật, phép trả lời; ví dụ cửa sổ 4 số trên năm số đầu của dòng MMDS Hình 4.1 khi $x_5=4$ đến; hình mới `trang-thai-cap-nhat.svg` (trạng thái trước, khối cập nhật, trạng thái sau, mũi tên nét đứt quay lại cho $x_6$; ô vừa ghi khung đậm). AT: cụm khóa thêm "Phép cập nhật"; ghi chú AT, A05, A00, A02 chỉnh để nối với A07. A06 giữ (Welford không lên mặt trang). Deck 59 trang; mạch 2 13 phút (tổng tạm 120,5, cân ở mạch 5). Ghi chú bài giảng: §1.4 thêm vết cửa sổ 4 số và hình; Bài tập 08.1 thêm bảng $r,\sum x_i,\sum x_i^2$ sau từng phần tử và đoạn "Trong thực hành" về mất chữ số trong float64 (dòng cộng $10^9$: mỗi $x_i^2$ làm tròn tới bội 128, tổng thiếu đúng 129, kết quả $0{,}0$) và phương pháp Welford ($V_8=37{,}875$; $4{,}7343749866$ trên dòng cộng $10^9$); tham khảo Welford (1962), *Technometrics* 4(3), 419–420.

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch | nhẹ | ghi chú AT | 109 âm tiết, vượt 100 của trang tiêu đề mạch | sửa | 100 |
| mạch | nhẹ | A07, hình | nhãn "số đếm 4" sau 5 số dễ hiểu lầm | sửa | "số trong bộ đệm 4" (bằng $\min(r,4)$) |
| mạch | nhẹ | ghi chú A07, ghi chú bài giảng | dãy $1,5,2,7,4$ ghi "do học phần dựng" nhưng lấy từ MMDS Hình 4.1 | sửa | chỉ cỡ cửa sổ 4 do học phần chọn |
| độ chính xác | nhẹ | ghi chú bài giảng, đoạn mất chữ số | chữ số mất khi làm tròn $x_i^2$ và tổng, không phải ở phép trừ | sửa | nêu ulp 128 và 1 024, tổng thiếu 129 |
| mạch | nhẹ | ghi chú A00; A07 thứ tự định nghĩa trước hình | câu nối vấp; thứ tự | sửa / giữ | câu viết lại; thứ tự giữ vì A05 ngay trước đã cho trực quan có số |
| mạch | nhẹ | ghi chú A07 | 151 âm tiết (mức 150) | chấp nhận | mức nhẹ theo CLAUDE.md |

Kiểm của điều phối viên: đọc diff deck, SVG, ghi chú, planning; tự chạy lại $4{,}734375=303/64$, công thức ngây thơ cho $0{,}0$ và Welford cho $4{,}7343749866244345$ trên dòng cộng $10^9$ (float64); `check08.py` toàn deck 59 trang ở hai khổ: 0 lỗi console/trang, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung, không cuộn ngang, không dòng > 20 âm tiết; mạch 2: A07 50 âm tiết, 4 dòng. Ảnh đã tự xem: A07 (1600×900). Trình xem ghi chú ở ba khổ: 0 `.katex-error`, không lỗi. `git diff --check` sạch. Hai báo cáo rà lại: không phát hiện từ mức trung bình trở lên.

### Mạch 3. Lấy mẫu theo khóa (lượt bản đánh giá)

Trang đổi: K01 (bảng xác suất thay bằng hình cây `cay-hai-bo-do-thi.svg`: bốn lá $1/100$, $9/100$, $9/100$, $81/100$, hệ số 2, có mặt $19/100$; dòng cuối dẫn $1/19$), K09 (dòng cuối "tỷ số hai số đếm kỳ vọng là $1/29$, không phải $1/2$"; ghi chú dạng $\frac{\eta d}{u+(2-\eta)d}$ và kiểm $\eta=1$), K02 (dòng "$h$ được chọn ngẫu nhiên một lần trước dòng, rồi cố định"; dòng kết chuyển vào ghi chú), K05 (nhãn "Mệnh đề (tất định)", "Mệnh đề (xác suất)"; ghi chú "số khóa được giữ trong một lần chạy là ngẫu nhiên"); ghi chú KT ("cụm"), K01B. Giữ K04, K06, K07, K08 (thanh 10 ngăn, thanh 100 ngăn, kéo-thả: bác bỏ theo quyết định chung). Ghi chú bài giảng: hình cây và đoạn đọc hình ở Ví dụ 08.3; Nhận xét 08.7 thêm kiểm $\eta=1$ và lý do tỷ lệ trên mẫu không có kỳ vọng bằng $1/29$ (không xác định khi mẫu không có truy vấn của An); §2.2 thêm "cụm", câu số khóa được giữ là ngẫu nhiên; Nhận xét 08.11 phân biệt chọn $h$ một lần với rút số mới ở Mục 3.

| Vai | Mức độ | Trang chiếu / vị trí | Vấn đề | Quyết định | Xử lý |
|---|---|---|---|---|---|
| mạch | trung bình | K02 | trang chật ở 1600×900 sau khi thêm dòng: tiêu đề sát mép trên, dòng cuối sát chân trang | sửa | dòng kết (lặp nội dung hình) chuyển vào ghi chú; 50 → 41 âm tiết |
| mạch | nhẹ | K05 | nên có nhãn phân biệt tất định/xác suất | sửa | "Mệnh đề (tất định)." / "Mệnh đề (xác suất)." |
| độ chính xác | — | K01, K09, K02, K05 | — | — | không phát hiện; tác tử tự kiểm bốn lá, $1/29$, dạng $\eta$, "với mọi $h$ cố định" |

Điều phối viên đọc diff ghi chú bài giảng của mạch này thay cho vòng rà ghi chú riêng (các đoạn thêm ngắn, không đổi kết quả): đúng và khớp deck. Kiểm: `check08.py` toàn deck 59 trang: 0 lỗi, 0 `.katex-error`, 0 mạng ngoài, 0 vượt khung, không dòng > 20 âm tiết; ảnh đã tự xem: K01, K02 (1600×900). Trình xem ghi chú ở ba khổ (người viết ghi chú chạy): không lỗi. `git diff --check` sạch.
