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
