# Nhật ký rà soát Bài 02 — bản viết mới theo ch2n.pdf

## Phạm vi hiện hành — 2026-09-14

Người dùng yêu cầu viết lại lecture 02, không chỉnh theo cấu trúc bản cũ. Bản này được soạn mới từ `sources/textbooks/ch2n.pdf`; giữ tên tệp và nền kỹ thuật của mẫu học phần. Phương án cũ giới hạn bài ở đếm từ và loại phép nối/nhân ma trận không còn hiệu lực. Lịch sử cũ vẫn có trong Git; báo cáo dưới đây chỉ áp dụng bản viết mới.

Đầu ra: HTML RevealJS, ghi chú tự học Markdown, năm SVG mới, outline, storyboard, review-log và mô tả Bài 2 trong index. Đối tượng năm 2, 44 trang giảng/120 phút và 9 trang bài tập/60 phút; thời lượng chưa được diễn tập với lớp thật.

Ngoại lệ cấu trúc do yêu cầu người dùng: 9 section ngoài, gồm mở đầu và mỗi mục 2.1–2.8 của PDF. Bài tập nằm cuối section nguồn, được truy cập sau phần giảng bằng liên kết tổng kết/tài liệu tham khảo; không tạo một section ngoài không tương ứng PDF. Thời lượng ghi trong storyboard, không đưa lên mặt slide hoặc lời diễn giảng theo quy tắc không hiển thị mã/thời lượng.

## Nguồn và lựa chọn cách thể hiện

Đã kiểm kê `sources/source.md`, ánh xạ Bài 2 trong `sources/reference-slides/README.md`, sách và các slide cục bộ. Chương `ch2n.pdf` có 60 trang PDF, trang in 20–79; PDF = trang in − 19.

| Cụm | Nguồn đối chiếu | Quyết định cho bản mới |
|---|---|---|
| Hệ tệp, đếm từ | MMDS slide 8–20; Stanford CS246 01-intro slide 33–44 | Tương đương cơ chế; sách 2.1–2.2 quyết định nội dung và thuật ngữ |
| Gộp, phân tải | MMDS 27–32; Stanford 45–46; khung sách tr.28 | Dùng sách để phân biệt reducer/tác vụ/máy và điều kiện gộp |
| Chịu lỗi | MMDS 23–26; Stanford 47; sách 2.2.5–2.2.6 | Chọn cơ chế sách, phân biệt nơi lưu trung gian và đầu ra |
| Thuật toán | Chương 2.3, Hình 2.4–2.5, Ví dụ 2.3–2.5 | Chạy ký hiệu ma trận và bốn hàng Links; không tự đặt ma trận số |
| Chi phí | MMDS 38–40; Stanford 67–69; sách 2.5 | Hai bộ slide dùng tổng I/O; bản mới chỉ lấy mô hình tổng đầu vào tác vụ của sách làm mô hình chính |
| Spark và mở rộng | Stanford 49–60,62,66; sách 2.4 | Sách làm nguồn chính; dùng RDD, Flatmap/Filter, lưu đệm và tính lại, không mô tả phiên bản phần mềm hiện tại |
| Lý thuyết MapReduce | Sách 2.6 | Giữ ví dụ mọi cặp ảnh để giải thích q/rho; chứng minh cận dưới đọc thêm |

Tham khảo cách giảng từ `../math-4-AI/2627-1/` lecture 01–03: cùng dữ liệu qua nhiều bước; hình/vết chạy trước khái quát; đơn vị trước công thức; nêu nơi dùng giả thiết. Bảng cụm trang tham khảo và áp dụng mới nằm trong storyboard. Không sao chép nội dung hoặc CSS môn đó. Kho machine-learning tham chiếu trong AGENTS không có ở đường dẫn cục bộ; dùng các nguyên tắc bố cục đã ghi trong AGENTS.

## Điều phối và kiểm nhận bản soạn

Các vai trò lập kế hoạch, phân tích nguồn, soạn hệ thống và sửa cục bộ đều chạy OpenRouter theo cầu nối của dự án. Kiểm tra trường runtime, không dựa lời tự khai: `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`. Writer chỉ ghi trong thư mục tạm; điều phối đối chiếu rồi mới đưa vào kho. Không có hai writer cùng ghi một tệp.

- Reader lập kế hoạch và reader phân tích nguồn đề xuất độc lập. Điều phối sửa lại số mục/trang và duyệt phạm vi chọn lọc theo năm 2.
- Writer đầu tiên bàn giao đặc tả hai phần thuật toán/chi phí. Điều phối bác vết nối và công thức sai trong bản nháp ấy, tính lại trực tiếp từ PDF; không đưa các giá trị sai vào đầu ra công khai.
- Writer hệ thống soạn tám trang 2.1 và 2.4. Điều phối rút văn bản, sửa sự đồng nhất máy quản lý với tệp siêu dữ liệu, nêu điều kiện bản sao và phục hồi.
- Writer sửa cục bộ đồng bộ phép chiếu Links, quy đổi trang và trạng thái storyboard. Điều phối bắt lại ký tự điều khiển trong công thức nối còn sót và kiểm tra trình duyệt.
- Năm reviewer độc lập được chạy bằng năm tiến trình riêng. Một số lượt đầu dừng vì `model exceeded the tool-call limit (14)`; reviewer toán và mạch viết tiếp tục gặp `model exceeded the tool-call limit (60)` do tìm kiếm không khớp. Reviewer sinh viên gặp `model returned an empty or incomplete answer after all retries`. Các lượt này không được tính là báo cáo hoàn tất. Chạy lại cùng mô hình, tăng ngân sách hoặc đưa trích nguồn trực tiếp; không chuyển worker khác ngầm.

## Sai khác có chủ ý và sửa lỗi nguồn

| Điểm | Quyết định và căn cứ |
|---|---|
| Hai chuỗi tiếng Việt đếm từ | Cụ thể hóa cơ chế Ví dụ 2.1–2.2, không phải dữ liệu trích nguyên văn; tách theo khoảng trắng, 5 lần xuất hiện, 3 lần “lớn”, gộp còn4 cặp. Không dùng như bài tập nguyên văn sách. |
| Khối và bản sao | Sơ đồ khái niệm ba khối/hai bản sao, không tuyên bố cấu hình máy thực tế. |
| Chọn/chiếu trên Links | Áp dụng định nghĩa nguồn lên bốn hàng Hình2.5; phân biệt với ví dụ được sách viết nguyên văn. |
| Vết nối Links | Hai bản sao cùng bốn hàng tạo đúng hai bộ; ghi rõ đây là phần trích. |
| Hình lưới | Chuẩn hóa tất cả chỉ số nhóm 0–3 theo hình nguồn; đoạn văn nguồn lẫn 1–4. R tới hàng2, S ô(2,1), T cột1. |
| Chi phí | $C=I+M$; đọc cục bộ vẫn tính, kết quả cuối không cộng trực tiếp. Không trộn $I+2M+O$. Bảng đếm từ dùng byte với $I+5B$/$I+4B$. |
| Nối ba bảng | $C_3=r+2s+t+cr+bt$; bộ trung gian của nối tuần tự được tính khi công việc sau đọc. |
| Ví dụ 2.16 | Giữ đúng dữ kiện lịch sử: khoảng một tỷ người dùng, trung bình300 bạn; không dùng300 triệu/1000. Tích $r=3\cdot10^{11}$ không đổi. |
| Biên961 | Khi lưới vuông, $k<961$ cho chi phí thấp hơn; tại961 bằng nhau. Hiệu chỉnh diễn giải “preferable” bao gồm biên bằng nhau trong sách. |
| Ký hiệu | Đổi r tốc độ sao chép của2.6 thành $\rho$ để tránh nhầm kích thước R; nhắc M của mô hình chi phí không phải ma trận M. |
| Đọc thêm | 2.3.6, giả mã chi tiết2.3.9–10, các hệ2.4.4–6, chứng minh2.6.3–7; không giao bài tập bắt buộc dựa vào phần chưa giảng sâu. |
| Bài tập | Giữ 2.2.1(a–c),2.3.1(a–d),2.5.1(a,c); chỉ dịch, tách ý và thêm nhãn sản phẩm; không thay dữ kiện/toán học. |

## Kết quả biên tập

Dùng no-ai-slop và tự kiểm theo `no-ai-slop/eval.md`: cắt lời dẫn chung, tiêu đề tiến trình và lặp nguồn; giữ các điều kiện, trường hợp biên và phân biệt mô hình. Dùng quill để rà đồ thị tiên quyết và thuật ngữ, không khởi tạo quill.json. Hình thức hóa ở ghi chú đặt trước ví dụ; slide ưu tiên vết chạy trước giả mã. Các mục hệ thống và đọc thêm không bị gán định lý/giả mã rỗng.

## Năm báo cáo độc lập và quyết định xử lý

Bảng runtime sau lấy từ kết quả cầu nối của các lượt hoàn tất. Báo cáo được tổng hợp theo phát hiện có tác động; điều phối không chấp nhận tự động mọi nhận định của reviewer.

| Vai trò | Requested / observed model | Provider | SHA-256 báo cáo JSON |
|---|---|---|---|
| Sinh viên năm 2 | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `e7714de28d4c0b99184475052fc100be5374f1ad8be3937b86579d3f7ce668e3` |
| Chuyên gia giải thuật và khoa học dữ liệu | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `5c06f3e105dceeab65c1821c38db041d1f6bd0d575b6a91735f00325a4126b60` |
| Độ chính xác toán học–thuật toán | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `e82832af77fe4c6cd2bc96c7c3693533a5acfa1286f066745dcf4223c822b74c` |
| Phản biện học thuật–giảng dạy | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `56687d72d006b909501820a4538fd5c6a0a24fe56ae3edec1df9f1d4f34598cb` |
| Kết nối, nguồn và mạch viết | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `5e7c9e24ceebaa67b639a4f6c8a7a6271dbab4bcc2e389a5f217fcd2ae443a6b` |
| Rà lại độ chính xác | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `80f216869a896837a238ffef13e1b2e56a9d7679088ff6fc237778d5ee42ba70` |
| Rà lại mạch viết | `z-ai/glm-5.3-flash` / `z-ai/glm-5.3-flash` | OpenRouter | `24a8f4aa1cb02d3553f35bd133334d148457be184cbfec5351243cfa8e97138b` |

### 1. Góc nhìn sinh viên

Không có lỗi chặn; sáu điểm mức thấp: đơn vị đếm từ không rõ trên mặt slide, lặp chữ nguồn, phạm vi trang dẫn, M trùng nghĩa, phép chọn thiếu vết cụ thể và slide/ghi chú chi phí chưa đồng bộ. Đã đổi bảng thành $I+5B$/$I+4B$ theo byte, giải thích I/M ngay cạnh công thức, nêu M không phải ma trận, bỏ chữ lặp, phân biệt trang cả chương/mục2.1–2.8 và thêm hai hàng Links chạy phép chọn. Không đổi thuật toán hoặc dữ kiện bài tập.

### 2. Chuyên gia giải thuật và khoa học dữ liệu

Một lỗi mức cao: dữ kiện lịch sử Ví dụ 2.16 bị đảo thành300 triệu/1000. Đã đối chiếu trang 59 và sửa thành một tỷ/300. Hai lỗi mức trung bình có căn cứ: gán điều kiện From=url1 cho Ví dụ 2.3 và tự gọi ảnh ở2.6.2 là ảnh vệ tinh. Đã ghi điều kiện là phép áp dụng lên Links và bỏ “vệ tinh/cùng khu vực”.

Reviewer cho rằng đáp án0 của câu Filter đòi toàn tài liệu chỉ chứa từ dừng. Điều phối không chấp nhận giả thiết ấy: đáp án đang đếm cặp của riêng từ được hỏi. Đã thêm “của từ đó” trên mặt slide để loại nhập nhằng. Mọi cặp của từ ấy bị loại, các từ khác vẫn có thể còn.

Hai điểm thấp về storyboard chi phí và I chưa định nghĩa đã sửa: bảng S05-01…09 khớp thứ tự thực tế, I/M có nhãn trên mặt slide. Reviewer xác nhận vết Links, chi phí nối, biên961, đọc lặp vector, lời giải số nguyên, q/rho và cơ chế khôi phục đúng.

### 3. Độ chính xác toán học–thuật toán

Kiểm lại độc lập các công thức $2(r+s)$, $r+2s+t+cr+bt$, $4r+2r\sqrt{k}$, $66r$, $2z+\sum_j a_jL_j$, $2N$; vết Links và q/rho đều đúng. Phát hiện dữ kiện Ví dụ 2.16 đã sửa như trên.

Không chấp nhận báo lỗi ký tự `&lt;`: đây là escape HTML hợp lệ, Chromium hiển thị $k<961$ và KaTeX không báo lỗi. Reviewer viết đảo b,c ở một câu kiểm tra cực tiểu liên tục; không đưa câu ấy vào tài liệu. Với $cr+bt$ và $bc=k$, đúng là $b=\sqrt{kr/t}$, $c=\sqrt{kt/r}$. Phần này chỉ ở chỉ dẫn đọc thêm của storyboard, không giảng Lagrange trên slide.

Lượt rà lại nhận đúng các đoạn đã sửa và xác nhận không còn lỗi nội dung: dữ kiện nguồn, mô hình byte, khóa đầu ra của nối, quy đổi trang và ảnh không thêm ngữ cảnh ngoài nguồn.

### 4. Phản biện học thuật–giảng dạy

Xác nhận đủ44 trang/120phút và9 bài/60phút, dữ kiện bài tập đúng nguồn, mức năm2 và các phần đọc thêm có lý do. Các điểm cần sửa: quy đổi trang, chiếu chưa phân biệt cụ thể hóa, thông số máy lịch sử tự mâu thuẫn, chữ lặp, storyboard phép chiếu chưa khớp. Đã xử lý.

Không chấp nhận ý kiến rằng nguồn2.3.7 không cho bỏ khóa đầu ra: trang 37 viết “The key is irrelevant.” Đã làm rõ chỉ khóa của cặp đầu ra không ảnh hưởng; bộ giá trị vẫn giữ thuộc tính chung b. Không lẫn với bỏ khóa trung gian hoặc bỏ cột nối.

### 5. Kết nối, nguồn và mạch viết

Xác nhận tuyến tiên quyết, mô hình trước phép tính, dùng lại dữ kiện, số trang và thời lượng đúng. Báo cáo đầu cho rằng thiếu hình dải/lưới và hai liên kết nhảy sai. Nguyên nhân là gói văn bản đã bỏ thẻ img/href. Điều phối mở HTML thực và thao tác Chromium: cả hai SVG tải được, kích thước hiển thị khoảng1167×336; ex231d tới ex251a, ex251c tới s07-01 đúng đích. Không thay liên kết đang đúng.

Đã làm rõ storyboard phép chọn chỉ chạy hai trong bốn hàng; áp dụng cả bảng giữ hai hàng. Bảng chiếu đổi nhãn “Bộ (From, To)” và thêm ngoặc mỗi bộ. Lượt rà lại nhận HTML gốc cùng bằng chứng trình duyệt xác nhận không còn lỗi bắt buộc. Bài học quy trình: reviewer văn bản cần nhận cả tham chiếu tài sản và href, không suy diễn thiếu nội dung từ bản bỏ thẻ.

## Kiểm định sản phẩm cuối

- HTML: lang=vi; khung1280×720; controlsLayout=edges; slideNumber/hashOneBasedIndex/hash bật; RevealJS, KaTeX, Notes, Highlight đều cục bộ.9 section ngoài,53 data-slide-id duy nhất,44 trang giảng và9 bài tập; mỗi trang có ghi chú diễn giả.
- Toàn bộ53 trang đã được mở bằng Chromium tại localhost:8765 và chụp ảnh. Điều phối xem ba bảng ảnh tổng hợp và các ảnh riêng cho hình/công thức/giả mã trọng tâm. Không thấy chữ bị cắt hoặc chồng lấn; phép đo DOM không có khối vượt khung. Chữ thân32px, giả mã khoảng26px; không thu nhỏ để giấu tràn trang.
- Không có lỗi JavaScript, HTTP4xx/5xx, KaTeX hoặc ký tự điều khiển.86 công thức slide được render. Năm SVG có role=img, title/desc và alt ở nơi dùng; không nhúng ảnh raster.
- Chặn mọi yêu cầu ngoài localhost vẫn tải đủ thành phần cốt lõi; không có yêu cầu ngoài cần cho bài.
- Ghi chú:185 công thức render, năm hình tải đúng; mục lục, liên kết về deck và index đúng. Kiểm tra1440×900 và390×844; trang không tràn ngang. Ba lời giải gập mặc định, mở được bằng bàn phím; beforeprint mở cả ba và afterprint trả lại trạng thái. Đã xuất bản in kiểm tra trong thư mục tạm, không phát hành PDF ngoài yêu cầu.
- Điều hướng: phím xuống chuyển trang dọc; liên kết bắt đầu bài tập và chuyển cụm đến đúng mã đích. Bảng chiếu sau sửa nhãn vẫn nằm trong khung (đáy khoảng580px ở màn1280×720).
- Tự chạy số học: Links trả đúng2 bộ; lưới có một ô giao; $66r=1{,}98\cdot10^{13}$; tại961 bằng nhau; với16 là12r; $10^6\cdot999\cdot10^6=9{,}99\cdot10^{14}$. SVG phân tích XML hợp lệ. Đối chiếu mã trang với storyboard và tổng120+60phút.
- Chỉ mục cập nhật mô tả Bài 2, giữ đường dẫn tài nguyên; không liên kết planning. Không chỉnh hạ tầng viewer hoặc tài liệu bài khác.

## Codex Slides và giới hạn kiểm tra

Đã mở Codex Slides và tạo hồ sơ bền vững `20260913173609-ds-b-i-02-h-s-b-n-vi-t-m-i-cdmn`. Công cụ tạo dự án không nhận53 trang do giới hạn30, nên dùng hồ sơ để lưu Design Files. Môi trường không cung cấp Codex in-editor Browser để xác minh bản RevealJS trong giao diện đó. Không tuyên bố đã rà trực quan bằng Codex Slides; kết quả trực quan ở trên thuộc Chromium/RevealJS cục bộ, theo ngoại lệ công cụ trong AGENTS.

HTML, storyboard và ghi chú cuối được lưu vào Design Files; việc tải lại cùng tên HTML trả bản cũ nên dùng write_design_file để thay đúng nội dung và đối chiếu với tệp kho. Bộ53 trang RevealJS trong kho là sản phẩm chính; hồ sơ Codex không phải một bộ slide được render lại độc lập.

## Bàn giao và Git

Đã kiểm tra diff trong phạm vi Bài 02; giữ nguyên các thay đổi ngoài phạm vi ở AGENTS, .gitignore, .codex, codex-orchestrator và openrouter-mcp. Commit gồm HTML, ghi chú, năm SVG mới, ba tệp quy trình và mô tả index. Lệnh phát hành theo AGENTS là git push origin main, không viết lại lịch sử. Kết quả commit/push được xác minh khi bàn giao; mã commit không tự nhúng vào tệp thuộc chính commit đó.

### Trạng thái đẩy kho

Commit nội dung `e6b4194` đã tạo thành công. Lệnh `git push origin main` bị bộ xét duyệt tự động từ chối vì chưa xác nhận quyền phát hành lên nhánh mặc định và đích từ xa. Sau từ chối, chỉ kiểm tra đọc: `origin` là `https://github.com/uet-iai-course/ds-foundation-algorithms.git`. Không thử đường vòng để đẩy. Nội dung và kiểm định hoàn tất cục bộ; phát hành lên GitHub đang chờ người dùng cho phép.

### Đối chiếu theo từng phần sau khi tiếp tục mục tiêu

Đã kiểm tra lại đúng tệp ở HEAD bằng Chromium. Không có thay đổi nội dung chưa commit. Cả 53 trang đều có trong kết quả kiểm tra, không tràn khung, không lỗi KaTeX/JavaScript hoặc tài nguyên hỏng. Bảng dưới ghi phạm vi thực tế và dấu vết nội dung từng section; đây là bằng chứng rà chốt, không phải tuyên bố đã có lịch sử viết/commit riêng từng section.

| Phần | Trang giảng | Trang bài tập | Mã trang đầu–cuối | SHA-256 nội dung section |
|---|---:|---:|---|---|
| Mở đầu | 3 | 0 | `lec02-s00-01` → `lec02-s00-03` | `a88558ce6044b468ee007fd18125a81104506c863463dbcf1cc253973464c8fd` |
| Mục 2.1 | 3 | 0 | `lec02-s01-01` → `lec02-s01-03` | `d212b460030f922c44147f1e1c33de3af7dc2cbe865091a9e9351ebe344bb7b9` |
| Mục 2.2 | 7 | 3 | `lec02-s02-01` → `lec02-ex221c` | `5fc97b3405c0ad21885f88ea18c686ac38dd771d707d81cfe5363ae4122168d9` |
| Mục 2.3 | 10 | 4 | `lec02-s03-01` → `lec02-ex231d` | `054f1592c9401b06f7dd10e7e6826634b33f12075a347481d562c1ffe50c8bff` |
| Mục 2.4 | 5 | 0 | `lec02-s04-01` → `lec02-s04-05` | `5d4fffc5889edc60451816ca3f98edba389f4f5bad3b2240c44a968729eb6964` |
| Mục 2.5 | 9 | 2 | `lec02-s05-01` → `lec02-ex251c` | `d26402ad12e7c682b4ec523de84d9e74380f7a173dddc93767133aa89ddd5da5` |
| Mục 2.6 | 4 | 0 | `lec02-s06-01` → `lec02-s06-04` | `805c3434def255b8c3634adbf5491be02e6b4e04f4138cb3f4e7c77d0b8ce02a` |
| Mục 2.7 | 2 | 0 | `lec02-s07-01` → `lec02-s07-02` | `36fee529d3b64f926cf89a72e72c7039eb8232040a9b8d4e4e3001b661c2f85d` |
| Mục 2.8 | 1 | 0 | `lec02-s08-01` → `lec02-s08-01` | `f630b2818a9fd5918a0f48a1d2a5b0ea5c0f67389c50585f59c545441270d0bd` |

SHA-256 toàn tệp HTML: `26c50bc9997aa20e5796e054f76f04bd3a4522fae94b620540423f321fcb0e45`. Ghi chú có 185 công thức được render, năm hình tải được; kiểm tra màn hình hẹp và bàn phím đạt.

Sai khác quy trình còn ghi nhận: bản viết mới đã được gộp trong commit nội dung e6b4194 trước khi mục tiêu tiếp tục nhắc lại yêu cầu commit/push từng phần. Không sửa lịch sử để tạo các mốc viết giả. Lần push tiếp theo vẫn bị xét duyệt tự động từ chối vì chưa công nhận xác nhận trực tiếp cho thao tác trên origin/main. Chưa có bằng chứng phát hành thành công; mục tiêu chưa được đánh dấu hoàn tất.

### Đã phát hành sau xác nhận trực tiếp

Người dùng xác nhận rõ `git push origin main` tới kho `uet-iai-course/ds-foundation-algorithms`. Lệnh đã thành công: `origin/main` chuyển từ `80dceb4` tới `9b05438`, gồm commit nội dung `e6b4194` và hai commit nhật ký. Trạng thái bị chặn ở các mục lịch sử phía trên đã được gỡ. Nội dung HTML, ghi chú và SVG không thay đổi sau kiểm định; các thay đổi ngoài phạm vi vẫn giữ ở máy cục bộ.

## Lượt sửa theo slide_authoring_standard.md — 2026-09-14

Trạng thái: bản nháp hiện hành 61 trang (52 giảng +9 bài tập), đang rà độc lập. Những báo cáo 53 trang và hash phía trên chỉ chứng minh bản phát hành trước tiêu chuẩn, không chứng minh bản mới.

Đã đọc tiêu chuẩn sáu nhóm, AGENTS, ánh xạ Bài 2 trong source.md và hai bộ slide MMDS/Stanford cục bộ. Đã dùng no-ai-slop cho câu chữ và quill cho mạch khái niệm, không tạo dự án sách. Planner và source-reader độc lập, writer chỉ soạn cụm 2.3 trong thư mục tạm. Cả ba kết quả runtime: requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Hồ sơ tạm /tmp/lec02-standard-revision gồm plan.json, source.json, accepted-plan.md, writer-spec.md và writer.json; không chứa thông tin xác thực.

| Vị trí | Vấn đề/bằng chứng ở bản trước | Quyết định sửa |
|---|---|---|
|s02-04|Giả thiết và phần lớn bất biến chỉ trong notes|Đưa giả thiết lên mặt; tách s02-04a chứng minh với khởi tạo/duy trì/kết luận|
|s03-02|Vết biểu thức và giả mã cùng trang, thiếu điều kiện trên mặt|Vết tổng từng bước; tách02a, nêu v vừa bộ nhớ/số học/zero|
|s03-07/08|Giả mã xuất hiện trước bảng vết|Thêm ví dụ cặp07a, chuyển08 lên trước07;07b tính đúng và xy|
|s03-09|Sally300 không có danh sách đầu vào để chạy|Dùng COUNT trênbốn hàng Links đã có, ghi là áp dụng2.3.8; Sally trong ghi chú|
|s04-01|Mô tả đồ thị bằng đoạn chữ dài|Vẽ SVG đủ sáu cung theo Hình 2.6, kiểm tra trực tiếp ảnh trang 42/PDF 23|
|s04-02|Map/Flatmap mới có định nghĩa|Dùng lại D2, một danh sách so với hai cặp; không bỏ lặp|
|s05-01/02|Công thức đi trước bảng phạm vi và đơn vị|Đưa bảng mô hình lên trước; nêu đọc cục bộ, đầu ra cuối và đơn vị|
|s05-05/06|Thuật toán nối ba bảng chỉ trong notes|Thêm05a quy tắcMap và05b Reduce/đúng; điều kiện giá trị thật sau băm|
|s05-07/08|Giả thiết30r và miền nguyên chủ yếu trong notes|Ghi rõước tính lịch sử, k chính phương, r=s=t, điểm bằng961 và bộ nhớ riêng|
|s06-02|Notes gọi đầu ra là kết quả so sánh mọi cặp|Sửa theo nguồn2.6.2: chỉ phát cặp vượt ngưỡng; thêm đặc tả và s đối xứng|
|s06-03|Xử lý cặp nội bộ chỉ nằm trong notes|Thêm03a bao phủ mọi cặp đúng một nơi và câu kiểm tra lặp 999lần|
|Storyboard|Danh mục cũ dùng tiêu đề thay mục đích|Viết lại mục đích, tiên quyết, biểu diễn, kết nối, nguồn và phút từng trang|

Không nhận đề xuất reader mở rộng tối ưu Lagrange vào nội dung bắt buộc; ngoài phạm vi năm2 đã chốt. Không nhận diễn giải k≤961 cho “ít hơn”: k=961 là bằng nhau. Điều kiện vừa bộ nhớ là kiểm tra khả thi, không phải giả thiết toán học cần để giải bất đẳng thức chi phí. Không coi việc ví dụ và giả mã cùng trang tự thân là lỗi; tiêu chí là mạch và khả năng đọc.

Giữ9 section theo yêu cầu trực tiếp mở đầu+mục 2.1–2.8; giữ9 bài tập nguồn và vị trí đã ghi ngoại lệ. Ghi chú độc lập đã đồng bộ ví dụ, thứ tự ví dụ nối trước mã, hình luồng và đặc tả ảnh. Không đổi nội dung bài khác.

Kiểm tra nháp bằng Chromium:61 trang, không tràn theo bounding box, không lỗi JavaScript/KaTeX/HTTP; đang xem contact sheets và rà độc lập. Codex Slides mở được hồ sơ bền vững 20260913173609-ds-b-i-02-h-s-b-n-vi-t-m-i-cdmn; phiên hiện tại không có công cụ in-editor Browser. Không tuyên bố đã kiểm tra trực quan bằng Codex Slides.

## Năm báo cáo độc lập của bản 61 trang

Các báo cáo dưới đây được lưu nguyên kết luận của từng reviewer để truy nguyên phản biện. Chúng không thay quyết định hợp nhất. Mọi báo cáo là rà văn bản; việc xem bản render do điều phối viên thực hiện trên Chromium.

### Quyết định hợp nhất

| Phản biện | Bằng chứng kiểm tra | Quyết định |
|---|---|---|
| Mất ghi chú hoặc dính công thức s05-08 | HTMLParser và Chromium giữ đủ câu so sánh, bảng tách riêng. Bộ trích dùng regex trước đó nuốt văn bản sau dấu nhỏ hơn | Sửa bộ trích bằng HTMLParser, escape dấu nhỏ hơn trong HTML, gửi bản đầy đủ cho lượt rà lại; không sửa kết luận số học đúng |
| Teaching đề nghị xóa ô L2 tại khóa url1 | L2 lấy cột đầu làm khóa: hai bộ (url1,url2),(url1,url3) đều về url1. Vết tính lại trả đúng hai đường đi | Bác đề nghị xóa; giữ bảng, thêm câu khóa cột hai của L1/cột một của L2 trên s03-07a |
| Math đề nghị đổi q thành số đầu vào đều | Mục 2.6.1 trang61 định nghĩa q là cận trên số giá trị được phép của một khóa | Giữ cận trên; bổ sung hai ví dụ chia đều đạt cận |
| Teaching cộng thời lượng thành115phút | Cộng theo metadata:5+10+18+30+12+27+12+5+1=120; bài tập15+20+25=60 | Bác tổng sai; giữ bảng120+60 |
| Mã trang không tăng theo thứ tự | ID là định danh liên kết, không hiển thị; storyboard có thứ tự thực tế | Giữ ID, ghi rõ hai chỗ đổi thứ tự có chủ đích |
| Thuật ngữ loại bản trùng và hB/hC | Sinh viên cần phân biệt loại trùng với thuật ngữ không phù hợp, chỉ số băm với thuộc tính | Đổi “khử trùng” thành “loại trùng”; thêm giải thích băm trong notes trước quy tắc tổng quát |
| Đề ex251a chưa nêu z,Lj,aj | Mặt đề chưa sử dụng các ký hiệu này, yêu cầu người học tự lập mô hình; đáp án có định nghĩa đầy đủ | Giữ đề gốc và mức hỗ trợ hiện tại; không đặt thêm giả thiết đọc vector một lần |
| Thiếu bước gặp nhau ở trang liên hệ nhân hai ma trận | Bảng có khóa j nhưng chưa nêu rõ hai phần tử cùng tới đó | Thêm câu m_ij và n_jk cùng về j; vẫn định vị chi tiết là đọc thêm |
| Nguồn Spark quá chung, ký hiệu B đổi ngữ cảnh | Kiểm tra trang44–47 cho Ví dụ2.7–2.10; B được định nghĩa ở từng phần | Tách nguồn theo mục/ví dụ/trang; giải thích B của ảnh khác B của cặp đếm từ |
| Liên kết bài tập thành cụm | Liên kết đầu cụm và chuỗi cuối cụm hoạt động | Giữ cụm2.3.1; tách liên kết trực tiếp2.5.1(a) và(c) |
| Lặp bất biến trong ghi chú và slide | s02-04 là giả mã, s02-04a là chứng minh có khởi tạo/duy trì/kết luận | Giữ phân vai; ghi chú hỗ trợ người giảng |
| Nhãn “nơi nhận mỗi ảnh” cho rho | Mỗi cặp trung gian chứa một ảnh và gửi tới một reducer khác nhau trong hai phương án | Giữ nhãn cụ thể cho ví dụ; định nghĩa rho tổng quát đã có trước đó |

Bản nguồn có Hình2.5 trang33, Ví dụ2.4 trang35 và thuật toán nối2.3.7 trang37. Không nhận gợi ý đổi Hình2.5 sang trang35 hoặc Ví dụ2.4 sang trang37 trong báo cáo rà lại; đó là nhầm trang của reviewer. Lưới vuông và miền k đã hiện trên mặt; không thêm điều kiện bộ nhớ vào bất đẳng thức như một giả thiết toán học.

### Báo cáo độc lập: Góc nhìn sinh viên năm 2

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `cb3f37138983bcfe98da1a7a489f07ba5987b2639237f438d76ac6a2cb1a6c78`.

<details>
<summary>Nội dung báo cáo trước hợp nhất</summary>

# Báo cáo rà soát Bài 02 — vai: sinh viên năm 2 (tiên quyết ngầm, ký hiệu mới, tự chạy ví dụ, tính chi phí)

**Giới hạn của lần rà này:** tôi chỉ đọc văn bản bản soạn, danh mục mục đích và dữ kiện kiểm chứng đã cung cấp. Tôi **không** xem bản render, không xem SVG, không tuyên bố đã kiểm tra hình hiển thị, tương phản hay cắt chữ; các mục liên quan hình chỉ đánh giá ở mức mô tả thay thế và dữ kiện được ghi.

## A. Đối chiếu dữ kiện và phép tính (đã kiểm lại bằng chứng)

Các con số và mô hình sau tôi tính lại và **khớp** với chứng cứ, không ghi nhận lỗi:

- Đếm từ: 5 cặp → 4 cặp, (lớn,3); bất biến s = j sau j đóng góp (s02-02, s02-03, s02-04a).
- Nối: hai bản sao Links, kết quả (url1,url2,url3), (url1,url2,url4); khóa url3 không phát (s03-08).
- Chi phí: I+M, đầu ra cuối không cộng riêng (s05-01/s05-02); 2(r+s) cho nối (s05-04); C₃ = r+2s+t+cr+bt (s05-06); 4r+62r = 66r = 1,98·10¹³ với r=3·10¹¹ và trung gian 30r (s05-07); k=16 → 12r, k=961 → bằng nhau, điều kiện k<961 với lưới vuông (s05-08).
- Nối ba bảng: b=c=4, k=16; S đến ô (2,1); R cả hàng 2, T cả cột 1 (s05-05, s05-05a).
- ex251a: C = 2z+ΣaⱼLⱼ, không mặc định vector đọc một lần; ex251c: C=2N (không gộp).
- 2.6: q=2, ρ=N−1=999999, trung gian ≈10¹⁸ byte; q=2000, ρ=999, 9,99·10¹⁴ byte; cặp nội bộ nhóm u giao cho reducer {u,(u+1) mod g}; số so sánh vẫn N(N−1)/2 (s06-01…s06-03a).

## B. Phát hiện cần sửa

### 1. Nghiêm trọng — ghi chú s05-08 bị cắt cụt, mất phần diễn giải
- **Vị trí:** lec02-s05-08 (So sánh hai cách), ghi chú diễn giả.
- **Vấn đề:** ghi chú kết thúc giữa câu: *"So với 66r: 4+2sqrt(k)Nguồn: MMDS…"* — vế diễn giải phía sau bất đẳng thức bị mất. Đây là trang then chốt để sinh viên năm 2 tự thay tham số và kiểm tra miền so sánh; phần dẫn dắt thay số đã biến mất.
- **Bằng chứng:** nguyên văn trong bản soạn: `"So với 66r: 4+2sqrt(k)Nguồn: MMDS, Chương 2, Ví dụ 2.15–2.16…"`.
- **Đề xuất:** khôi phục dòng so sánh, ví dụ: "4+2√k so với 66r: nhỏ hơn khi k<961, bằng tại k=961; k>961 thì lưới vuông đắt hơn" — không thêm khẳng định ngoài nguồn.

### 2. Nhẹ — lỗi ghép chuỗi trên mặt slide s05-08
- **Vị trí:** cùng trang, mặt slide.
- **Vấn đề:** dòng `"C₃=4r+2r√k$$k$ | …"` — công thức và tiêu đề cột `$k$` dính nhau do thiếu xuống dòng/ký tự phân cách; khi render có thể hiện công thức nối cột bảng sai.
- **Đề xuất:** tách công thức ra dòng riêng trước bảng; kiểm tra lại trên bản render (việc kiểm render nằm ngoài phạm vi lần rà này).

### 3. Nhẹ — ký hiệu z, Lⱼ, aⱼ của ex251a chỉ tồn tại trong ghi chú
- **Vị trí:** lec02-ex251a.
- **Vấn đề:** mặt slide chỉ yêu cầu "Biểu diễn chi phí truyền thông theo kích thước ma trận và vector" nhưng không định nghĩa z (số phần tử ma trận lưu), Lⱼ (độ dài dải), aⱼ (số Map task đọc dải). Tiêu chuẩn yêu cầu "định nghĩa ký hiệu ngay nơi dùng" và bảng tính chi phí phải thấy được trên mặt. Sinh viên muốn tự chạy không có bảng ký hiệu để bám.
- **Bằng chứng:** mặt slide chỉ có 4 dòng; toàn bộ định nghĩa nằm trong ghi chú.
- **Đề xuất:** đưa bảng nhỏ (z, Lⱼ, aⱼ — ý nghĩa, đơn vị) lên mặt slide, hoặc thêm một slide tiền tố định nghĩa trước khi đặt câu hỏi.

### 4. Nhẹ — hB, hC được dùng trước khi định nghĩa
- **Vị trí:** lec02-s05-05 (dùng trước) so với lec02-s05-05a (định nghĩa).
- **Vấn đề:** ghi chú và mô tả hình của s05-05 dùng "hB=2, hC=1", trong khi định nghĩa h_B, h_C chỉ xuất hiện ở trang kế tiếp. Sinh viên năm 2 lần đầu gặp khái niệm băm; gặp chỉ số "2, 1" trước quy tắc sinh ra nó là một bước nhảy nhỏ.
- **Bằng chứng:** s05-05 ghi chú: *"Bộ S với hB=2,hC=1 gửi đúng ô (2,1)"*; s05-05a: *"$h_B$ băm $B$ vào $b$ hàng…"*.
- **Đề xuất:** trong s05-05, thay bằng ngôn ngữ thường ("bộ S rơi vào ô ở hàng 2, cột 1 theo hai chỉ số nhóm — quy tắc ở trang sau"), hoặc thêm một câu định nghĩa vắn ngay ghi chú s05-05.

### 5. Nhẹ — thuật ngữ "khử trùng" không chuẩn và chưa nhất quán
- **Vị trí:** ghi chú s03-06 (*"khử trùng còn hai giá trị phân biệt"*), s03-06 mặt slide dùng "loại bản trùng".
- **Vấn đề:** "khử trùng" là dịch máy từ "dedup/duplicate elimination", dễ gây hiểu nhầm cho sinh viên; cùng một khái niệm đang có hai cách gọi trong một cụm.
- **Đề xuất:** thống nhất một thuật ngữ, ví dụ "loại trùng" hoặc "loại bộ trùng lặp", dùng xuyên suốt mặt slide và ghi chú.

### 6. Nhẹ — s03-10 nén quá mức bước gặp nhau trong nhân ma trận–ma trận
- **Vị trí:** lec02-s03-10, bảng "Công việc 1 · Khóa j".
- **Vấn đề:** bảng cho khóa j và kết quả ((i,k), m_ij·n_jk) nhưng không cho thấy *hai phần tử m_ij và n_jk từ hai ma trận cùng đến reducer khóa j* — đây chính là thao tác quyết định mà sinh viên năm 2 cần nhìn thấy để nối với kỹ thuật chọn khóa đã học. Trang được định vị là "liên hệ/đọc thêm" nên không phải lỗi chặn, nhưng hiện tại không tự đọc được cơ chế chỉ từ bảng.
- **Đề xuất:** thêm một dòng ngắn "m_ij (từ M) và n_jk (từ N) cùng về khóa j; reducer nhân rồi phát theo (i,k)".

### 7. Nhẹ — cách diễn đạt "một bản sao Web"
- **Vị trí:** lec02-ex221a/b/c mặt slide: *"chẳng hạn một bản sao Web"*.
- **Vấn đề:** cụm tối nghĩa với sinh viên năm 2; nguồn nói bản sao kho trang Web (web crawl).
- **Đề xuất:** "một bản sao kho trang Web (web crawl)" hoặc "một kho văn bản lớn".

## C. Điểm xác nhận là đúng (không phải lỗi)

- Thứ tự s05-02 → s05-01 (mô hình trước công thức) phù hợp tiêu chuẩn "nêu mô hình trước khi tính", dù mã slide đảo.
- Các câu hỏi tương tác đều có nhãn "Câu hỏi:" và đáp án trong ghi chú (s02-02, s02-06, s03-08, s04-03, s04-04, s05-09, s06-03a, s06-04).
- Tiên quyết ngầm được xử lý: RDD được mở rộng tên, Map/Flatmap phân biệt bằng bảng với số phần tử (s04-02); quan hệ/bộ/thuộc tính được đặt tên trước khi dùng (s03-04); "khóa đầu ra có thể bỏ qua" của bài tập 2.3.1 được giữ nguyên dữ kiện nguồn.
- Ký hiệu t→τ ở 2.6 và r→ρ có lý do ghi rõ (tránh trùng r=|R|), đúng tinh thần "nói rõ tương ứng khi đổi ký hiệu".
- "Trong mô hình nguồn phải tính mọi cặp" (s06-00) và "số so sánh không giảm" (s06-03a) khớp chứng cứ, tránh kết luận quá mức.

## D. Kết luận

**Không có lỗi chặn** (không có dữ kiện nguồn sai, không có khái niệm bắt buộc thiếu hẳn khiến mạch đứt). Có **1 lỗi nghiêm trọng** (ghi chú s05-08 cắt cụt) và **6 lỗi nhẹ** về ký hiệu và diễn đạt. Riêng mục 3 (ex251a) là điểm ảnh hưởng trực tiếp nhất đến khả năng tự chạy ví dụ và tự lập bảng chi phí của sinh viên năm 2, nên ưu tiên sửa cùng lỗi 1. Các mục liên quan hình (s01-03, s03-03, s04-01, s04-03, s05-01, s05-05) chỉ đánh giá được phần mô tả thay thế; chất lượng render phải chờ kiểm định trên bản trình chiếu thực.

</details>

### Báo cáo độc lập: Giải thuật và khoa học dữ liệu

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `6e49e1c6a51c36ec13de253d6b58a4758af07cfae08388ffb15befb320ff53d6`.

<details>
<summary>Nội dung báo cáo trước hợp nhất</summary>

# Báo cáo rà soát Bài 02 — Vai: chuyên gia giải thuật và khoa học dữ liệu

Phạm vi rà: đặc tả, giả mã, bất biến, biên, chi phí, truyền dữ liệu, tính khả thi, so khớp với ch2n.txt. Tôi chỉ rà văn bản và mã nguồn; chưa tự xem hình render (các SVG được kiểm định riêng bằng Chromium theo quy trình, tôi không tuyên bố đã xem ảnh).

## Kết luận tổng thể

Không phát hiện lỗi **chặn**. Các kết luận toán học trung tâm đều khớp nguồn và được tính lại chính xác:
- Ví dụ 2.16: 4r + 62r = 66r = 1,98·10¹³, r = 3·10¹¹, ước lượng trung gian 30r — khớp ch2n.txt dòng 1810–1830 (nguồn nói rõ là ước lượng "conservatively", bản soạn đã ghi đúng là giả thiết).
- Điểm so sánh: 4r + 2r√k = 66r tại √k = 31, k = 961; nguồn dòng 1837–1838 "no more than 31² = 961"; slide s05-08 phân biệt đúng "k < 961 ít hơn, k = 961 bằng nhau" và yêu cầu k chính phương cho lưới vuông — chính xác và thận trọng hơn văn nguồn.
- Nối ba bảng (s05-06): r+2s+t+cr+bt; với b=c=4 ra 5r+2s+5t — khớp nguồn dòng 1775–1800.
- Ví dụ 2.15: b=c=4, k=16, R gửi c bản, S gửi 1, T gửi b; chỉ số nhóm 0..3 nhất quán với hình (văn nguồn lẫn 1..4, bản soạn đã hiệu chỉnh và ghi rõ).
- Similarity join (s06-02/03): q=2, ρ=999999, ≈10¹⁸ byte; g=1000 → q=2000, ρ=999, 9,99·10¹⁴ byte; quy tắc cặp nội bộ nhóm giao cho reducer {u, (u+1) mod g} — khớp nguồn dòng 2029–2038, và đã giữ điều kiện kính định không lặp (đáp án 999 lần ở s06-03a).
- Chi phí matvec chia dải (ex251a): C = 2z + ΣaⱼLⱼ, không mặc định vector đọc một lần — khớp và đúng mô hình 2.5.1.
- Vết Links: 4 hàng 1→2,1→3,2→3,2→4; nối cho đúng hai đường (url1,url2,url3), (url1,url2,url4); Sally 300 được định vị là dữ kiện Ví dụ 2.5, không bịa danh sách 300 tên.

## Lỗi nghiêm trọng: không có.

## Lỗi nhẹ

**N1 — lec02-s05-08, ghi chú diễn giả: câu bị đứt giữa chừng.**
- Vấn đề: ghi chú dừng cụt: *"So với 66r: 4+2sqrt(k)"* rồi ngay lập tức nhảy sang *"Nguồn: MMDS…"*. Ý định hiển nhiên là "4+2√k < 66r ⇔ √k < 31 ⇔ k < 961" (đã có trên mặt slide) nhưng dòng diễn giải không hoàn chỉnh.
- Bằng chứng: trích nguyên văn phần ghi chú trong bản soạn hiện hành; chuỗi "4+2sqrt(k)" không có vế so sánh nào sau nó.
- Đề xuất: hoàn tất câu, ví dụ: "So với 66r: 4+2√k nhỏ hơn khi k<961, bằng tại k=961, lớn hơn khi k>961 (k chính phương)". Không đổi nội dung mặt slide.

**N2 — lec02-s06-01/s06-02: nhãn ρ hơi lệch với định nghĩa.**
- Vấn đề: s06-01 định nghĩa ρ = "số cặp trung gian trung bình trên một đầu vào" (đúng nguồn: replication rate). Nhưng bảng ở s06-02 và s06-03 ghi nhãn cột là "Nơi nhận mỗi ảnh | ρ". Về mặt số học hai cách đọc cho cùng giá trị (mỗi cặp trung gian chứa đúng một bản ảnh đang xét), nhưng nhãn "nơi nhận" không phải định nghĩa đã thiết lập, dễ khiến sinh viên nghĩ ρ đếm "nơi" thay vì "số cặp phát".
- Bằng chứng: định nghĩa s06-01 so với nhãn bảng s06-02/s06-03 và s06-04 ("Bản sao/ảnh").
- Đề xuất: đổi nhãn cột thành "Số bản sao mỗi ảnh (ρ)" hoặc thêm một câu trong ghi chú nối "mỗi cặp trung gian mang đúng một ảnh, nên ρ cũng là số nơi nhận mỗi ảnh". Mức độ: trình bày, không sai số.

**N3 — lec02-s02-04a trùng lặp bất biến với s02-04.**
- Vấn đề: bảng bất biến ở s02-04a lặp lại gần như nguyên lập luận đã nêu trong ghi chú s02-04 (khởi tạo s=0, duy trì, kết luận khi dừng). Tiêu chuẩn cho phép tách chứng minh thành trang riêng, nên đây không phải lỗi; chỉ lưu ý hai trang nên phân vai rõ hơn (s02-04 nêu mệnh đề + giả mã; s02-04a trình bày khung bất biến đủ ba phần khởi tạo/duy trì/kết luận — hiện có nhưng "kết luận khi dừng" nằm chung dòng cuối).
- Đề xuất: giữ nguyên; nếu chỉnh, gộp "khi hết danh sách" thành dòng kết luận riêng cho khớp khung bất biến.

## Điểm đã kiểm và đạt (để tránh nghi ngờ nhầm là lỗi)

- Mô hình chi phí 2.5.1 được thiết lập trước mọi phép tính (s05-02 trước s05-01 trong mạch), nêu rõ: cộng kích thước đầu vào mọi tác vụ gồm đọc cục bộ, đầu ra cuối không cộng riêng, M là trung gian không phải ma trận — đúng nguồn và đúng yêu cầu "mô hình trước công thức".
- Đơn vị nhất quán: s05-03 cộng I + 5B/I + 4B với giả thiết B byte/cặp được nêu trước; không cộng byte với số cặp.
- Biên của giả mã đều có: tệp rỗng (ex231a/b/d), một phía rỗng của nối (s03-07b), hàng không phát cặp ⇒ xᵢ=0 (s03-02a, s03-02a nêu cả điều kiện áp dụng "v vừa bộ nhớ tác vụ").
- Bất biến có đủ khởi tạo/duy trì/kết luận (s02-04a, s03-02a, ex231a/b); đệ quy không áp dụng.
- Câu hỏi tương tác đều có nhãn "Câu hỏi:" và đáp án trong ghi chú (s02-02, s02-06, s03-06, s03-08, s05-09, s06-03a, s06-04).
- Kết luận so sánh có đủ điều kiện: s05-08 tách điểm bằng, miền nguyên, k chính phương; s05-09 tách tổng chi phí khỏi thời gian hoàn thành; ex221b/c không khẳng định tuyệt đối.
- Hình 2.6 (s04-01): f→g, f→i, h→i, h→j, g→j, i→j — SVG vẽ lại đủ sáu cung theo dữ kiện kiểm chứng.

## Giới hạn của lần rà này

Đây là rà văn bản (bản soạn, giả mã, công thức, dữ kiện, mạch). Chất lượng render (tràn chữ, chồng lấn, tương phản, cắt chữ ở khung 1280×720, alt text hiển thị, điều hướng bàn phím) phải được xác nhận trên bản render thực; các tệp PNG trong thư mục là kết quả kiểm định riêng, tôi không tự kết luận từ chúng. Nhãn hình trong SVG chỉ được đối chiếu ở mức dữ kiện nêu trong thuộc tính `alt` của bản soạn.

**Kết luận:** không có lỗi bắt buộc phải sửa trước khi phát hành; sửa N1 (đứt câu ghi chú s05-08) là việc nên làm, N2/N3 tùy chọn.

</details>

### Báo cáo độc lập: Độ chính xác toán học–thuật toán

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `e1f24d028a35f0f70c1b18e1c637fcf8eb915d6b2bbab8774321bf450d62c751`.

<details>
<summary>Nội dung báo cáo trước hợp nhất</summary>

# Báo cáo rà soát — Vai: Độ chính xác toán học–thuật toán (Bài 02)

Phạm vi: tự tính lại mọi ví dụ số liệu, giả thiết quyết định, kiểm tra biên và đơn vị trên bản soạn hiện hành; đối chiếu với dữ kiện kiểm chứng đã cung cấp (ch2n.txt, storyboard). Không xem hình render; các nhận xét về SVG chỉ giới hạn ở dữ kiện đã kiểm chứng bằng văn bản, không tuyên bố đã xem ảnh.

## Kết quả tổng quát

**Không phát hiện lỗi mức chặn hoặc nghiêm trọng về toán học–thuật toán.** Các phép tính chính đều tự tính lại đúng:

- s02-02/03/05: 5 cặp, 3 cặp khóa "lớn", nhóm cho (lớn,3); gộp D2 5→4 cặp, tổng cuối (lớn,3) — đúng.
- s03-08: với Links (1→2, 1→3, 2→3, 2→4), nhóm đỉnh giữa: url2 có L1={url1}, L2={url3,url4} → đúng 2 đường (url1,url2,url3), (url1,url2,url4); url1, url3, url4 không phát — bảng vết và kết quả đúng.
- s03-09: COUNT trên Links cho url1=2, url2=2 — đúng; ghi chú đúng khi nói Ví dụ 2.5 (Sally,300) không có danh sách 300 tên để chạy số.
- s05-04: r=s=4, 2(r+s)=16 đơn vị, 2 bộ kết quả — đúng.
- s05-06: C₃=(r+s+t)+(cr+s+bt)=r+2s+t+cr+bt; b=c=4 → 5r+2s+5t — đúng, và ghi chú giải đúng nguồn hệ số 2s (S đọc ở cả hai tầng).
- s05-07: 4r + (30r+r)+(30r+r)=4r+62r=66r; 66×3·10¹¹=1,98·10¹³ — đúng; 30r được nêu là giả thiết ước lượng, không đẳng thức.
- s05-08: k=16 → 12r; k=961=31² → 66r; 4+2√k<66 ⟺ √k<31 ⟺ k<961 — đúng; điều kiện k chính phương cho lưới vuông **có** hiện trên mặt slide.
- s06-02: ρ=N−1=999999; trung gian N(N−1)B=10⁶·999999·10⁶≈9,99999·10¹⁷≈10¹⁸ — đúng; phạm vi "chưa cộng NB" được nêu.
- s06-03: q=2(N/g)=2000; ρ=g−1=999; N(g−1)B=9,99·10¹⁴ — đúng; quy tắc giao cặp nội bộ nhóm u cho reducer {u,(u+1) mod g} khớp nguồn; đáp án câu hỏi s06-03a là g−1=999 — đúng.
- ex251a: Map đọc z+ΣaⱼLⱼ, Reduce đọc z, C=2z+ΣaⱼLⱼ; trường hợp aⱼ=1, ΣLⱼ=n cho 2z+n; z=n² khi đặc — khớp mô hình nguồn, có cảnh báo không mặc định vector đọc một lần.
- ex251c: C=2N (chưa gộp), N(B_R+B_P) theo byte — đúng.
- s05-01: C=Σ|in(u)|=I+M, đầu ra cuối không cộng riêng — đúng mô hình 2.5.1.
- s04-02: Spark Map trả 1 đối tượng, Flatmap 0..n phần tử — đúng phân biệt nguồn.

Các trường hợp biên được xử lý đúng nơi cần: tệp/kho rỗng (s02-04a, ex231a/b/d), một phía nhóm rỗng khi nối (s03-07b), hàng không phát cặp hiểu x_i=0 (s03-02a), N>0 khi chia trung bình (ex231b), không dùng 0 làm khởi tạo max vì số âm (ex231a), điểm bằng k=961 được kiểm tra riêng (s05-08).

## Các finding mức nhẹ

**1. (Nhẹ) lec02-s05-08 — ghi chú diễn giả bị cắt cụt và mặt slide lỗi định dạng công thức.**
- Vấn đề: Ghi chú kết thúc đột ngột: "So với 66r: 4+2sqrt(k)" rồi ngay "Nguồn:", thiếu vế so sánh. Trên mặt slide, dòng "$C_3=4r+2r\sqrt{k}$$k$ | ..." dính công thức với tiêu đề cột bảng, thiếu ngắt dòng.
- Bằng chứng: văn bản s05-08, dòng "$C_3=4r+2r\sqrt{k}$$k$ | Thay vào công thức…" và ghi chú "So với 66r: 4+2sqrt(k)Nguồn: MMDS…".
- Đề xuất: hoàn thiện câu ghi chú (ví dụ "4+2√k<66 khi k<961; bằng tại 961; lớn hơn khi k>961 chính phương") và tách dòng công thức khỏi bảng. Không ảnh hưởng tính đúng số học.

**2. (Nhẹ) lec02-s06-01 — định nghĩa q là "số giá trị đầu vào tối đa của một reducer" lệch với cách dùng của nguồn.**
- Vấn đề: nguồn 2.6.1 dùng q như số đầu vào mỗi reducer (các bảng sau giả thiết mọi reducer nhận cùng q: q=2 và q=2000 đều là giá trị đều, không phải cận trên). Gọi "tối đa" tạo khoảng cách nhỏ giữa định nghĩa và cách thay số ở s06-02/03.
- Bằng chứng: s06-01 bảng ký hiệu; s06-02 "Ảnh mỗi reducer q=2"; s06-03 "q=2(N/g)=2000" — các nơi này dùng q như giá trị đều mỗi reducer.
- Đề xuất: định nghĩa q là "số đầu vào mỗi reducer (giả thiết phân bố đều)" hoặc ghi chú rằng các ví dụ sau giả thiết mọi reducer nhận đúng q giá trị.

**3. (Nhẹ) Ký hiệu B dùng hai nghĩa khác đơn vị tham chiếu trong cùng bài.**
- Vấn đề: s05-03 dùng B là số byte của một cặp trung gian; s06-00 dùng B=10⁶ byte là kích thước một ảnh. Cả hai đều được định nghĩa nơi dùng nên không sai, nhưng cùng ký hiệu cho hai đại lượng khác bản chất (kích thước bản ghi vs kích thước đầu vào) dễ nhầm khi so sánh hai phần.
- Bằng chứng: s05-03 "mỗi cặp trung gian dài B byte"; s06-00 "mỗi ảnh B=10⁶ byte".
- Đề xuất: giữ nguyên nếu storyboard đã ghi quyết định; nếu không, đổi một trong hai (ví dụ B_ảnh) hoặc thêm một dòng ghi chú tương ứng ký hiệu ở s06-00.

**4. (Nhẹ) Mã slide trùng/không theo thứ tự trong cụm nối (s03-07a → s03-08 → s03-07 → s03-07b).**
- Vấn đề: không phải lỗi toán; mã "s03-07" được dùng cho slide khái quát trong khi "s03-07a" là trang dẫn nhập đứng trước, dễ gây nhầm khi đối chiếu storyboard–deck và khi liên kết "#/lec02-…".
- Bằng chứng: danh mục và thứ tự bản soạn: lec02-s03-07a, lec02-s03-08, lec02-s03-07, lec02-s03-07b.
- Đề xuất: đổi mã trang khái quát (ví dụ lec02-s03-07c) hoặc sắp xếp lại mã cho khớp thứ tự trình bày; cập nhật liên kết trong storyboard.

## Giới hạn của lần rà này

- Đây là rà văn bản và số liệu; **không phải kiểm định render**. Các SVG (ch2-khoi-ban-sao, ch2-dai-ma-tran, ch2-luong-cong-viec, ch2-spark, ch2-luoi-reducer, ch2-chi-phi) chỉ được đối chiếu về dữ kiện logic qua dữ kiện kiểm chứng (ví dụ Hình 2.6 có đủ 6 cung f→g, f→i, h→i, h→j, g→j, i→j; lưới 4×4 với R hàng 2, S ô (2,1), T cột 1 khớp Ví dụ 2.15 với b=c=4, k=16, chỉ số 0..3). Chất lượng hiển thị, tràn chữ, chồng lấn phải do người xem bản render xác nhận.
- Các trang tham chiếu (trang in/PDF) không thuộc nhiệm vụ toán–thuật toán, không rà tại đây.

## Kết luận

Về vai độ chính xác toán học–thuật toán: **không có lỗi bắt buộc sửa trước khi duyệt**. Toàn bộ vết chạy, công thức chi phí, bất đẳng thức so sánh (gồm điểm bằng k=961 và điều kiện k chính phương), các trường hợp biên (rỗng, một phía rỗng, số âm, N>0) và đơn vị (byte so với đơn vị chuẩn hóa, I+M, 2z+ΣaⱼLⱼ, N(N−1)B, N(g−1)B) đều tự tính lại khớp. Bốn finding mức nhẹ nêu trên nên được ghi vào nhật ký rà soát kèm quyết định xử lý; riêng finding 1 (ghi chú s05-08 cắt cụt) nên sửa văn bản vì hiện ghi chú không truyền đạt trọn vẹn kết luận so sánh.

</details>

### Báo cáo độc lập: Học thuật và giảng dạy

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `2c601e9b7df00b9f7aa91599167eadb1db8f1fa1d5758dee7a93e77631e427a9`.

<details>
<summary>Nội dung báo cáo trước hợp nhất</summary>

# Báo cáo rà soát Bài 02 — vai phản biện học thuật–giảng dạy

Phạm vi: rà văn bản soạn (mặt slide + ghi chú diễn giả) và danh mục mục đích/tiên quyết/thời lượng. **Không kiểm định render**: các SVG (s01-03, s03-03, s04-01, s04-03, s05-01, s05-05) chỉ được rà qua mô tả thay thế và ghi chú; tôi không tuyên bố đã xem hình đã render. Việc kiểm tra cắt chữ, chồng lấn, tương phản phải làm riêng trên bản render.

## 1. Nghiêm trọng — dữ kiện bảng vết nối sai tại khóa url1

- **Vị trí:** lec02-s03-08, bảng vết nối trên bốn hàng Links, hàng khóa `url1`, cột "Từ $L_2$".
- **Vấn đề:** Ô ghi "url2, url3" là sai. Nối L₁(U₁,U₂) ⋈ L₂(U₂,U₃) khóa theo đỉnh giữa U₂; bốn hàng Links là 1→2, 1→3, 2→3, 2→4, nên L₂ (khóa theo U₂) chỉ có bộ tại khóa url2 (url3, url4), url3 (url4) và url4 — **không có bộ nào của L₂ tại khóa url1**. Hai cạnh ra khỏi url1, tức (url1,url2) và (url1,url3), khi nằm trong L₂ được phát về khóa url2 và url3, không về khóa url1.
- **Bằng chứng:** Bảng slide: "url1 | — | url2, url3". Đối chiếu dữ kiện đã kiểm chứng: "Links Hình 2.5 có 4 hàng 1→2, 1→3, 2→3, 2→4; nối hai bản sao chỉ ra (1,2,3),(1,2,4)". Ghi chú cùng slide tự nói "Chỉ khóa url2 có dữ liệu từ cả hai phía" và "không có cạnh vào url1" — mâu thuẫn với ô bảng vừa nêu. Hàng url2, url3, url4 đều đúng.
- **Ảnh hưởng:** Vi phạm điều kiện "người học có thể tự tái tạo vết chạy từ dữ kiện hiển thị": sinh viên đối chiếu bảng với bốn hàng sẽ tính lại và thấy ô này không tái tạo được; đây chính là kiểu lỗi bảng vết mà tiêu chuẩn mục 4 yêu cầu người soạn tự tính lại trước khi duyệt.
- **Đề xuất:** Sửa ô thành "—" (cả hai phía rỗng tại khóa url1), giữ nguyên kết quả (url1,url2,url3), (url1,url2,url4) và câu hỏi về khóa url3.

## 2. Nhẹ — ghi chú diễn giả s05-08 bị đứt câu, mất nội dung giải thích

- **Vị trí:** lec02-s05-08, ghi chú diễn giả.
- **Vấn đề:** Ghi chú kết thúc cụt: "So với 66r: 4+2sqrt(k)Nguồn: …" — câu so sánh và hướng dẫn kiểm tra miền tham số bị mất giữa chừng, dính vào dòng nguồn.
- **Bằng chứng:** Toàn bộ bất đẳng thức $4+2\sqrt{k}<66 \iff \sqrt{k}<31 \iff k<961$ và điều kiện $k$ chính phương vẫn còn trên **mặt slide**, nên học sinh vẫn thấy kết luận; nhưng ghi chú mất phần hướng dẫn cách thay số và kiểm tra điểm bằng $k=961$ (đã có trong bảng), cũng như mất phần diễn giải mà tiêu chuẩn mục 5 yêu cầu đặt ở ghi chú ("kiểm tra riêng điểm bằng nhau, điều kiện nguyên và miền tham số" — mặt slide có dòng bất đẳng thức nhưng ghi chú phải dẫn giải).
- **Đề xuất:** Khôi phục ghi chú: thay số vào công thức, nêu rõ điều kiện $k$ chính phương để $b=c=\sqrt{k}$ nguyên, điểm bằng $k=961$, miền $k<961$, và nhắc còn phải kiểm tra bộ nhớ mỗi reducer.

## 3. Nhẹ — đánh số slide ngược với thứ tự trình bày ở hai cụm

- **Vị trí:** (a) s05-02 ("Chọn đơn vị, phạm vi và quy tắc đếm") trình bày **trước** s05-01 ("Lập tổng I+M"); (b) s03-07a → s03-08 → s03-07 → s03-07b.
- **Vấn đề:** Về học thuật, thứ tự trình bày là đúng (mô hình chi phí trước công thức; vết chạy trước khái quát — đúng mạch tiêu chuẩn). Tuy nhiên mã slide không khớp thứ tự phát, dễ gây nhầm khi bảo trì storyboard, tạo liên kết "trang trước/trang sau" và khi người rà đối chiếu "kết nối vào–ra".
- **Bằng chứng:** Danh mục và bản soạn hiện hành đều liệt kê s05-02 trước s05-01; s03-07a/08 trước s03-07.
- **Đề xuất:** Không bắt buộc đổi thứ tự giảng dạy; chỉ cần ghi rõ trong storyboard (trường "kết nối vào–ra") rằng mã không phản ánh thứ tự trình bày, hoặc đánh số lại (ví dụ s05-01↔s05-02) kèm nhật ký rà soát.

## 4. Nhẹ — trích trang nguồn không nhất quán trong cụm 2.6

- **Vị trí:** lec02-s06-00 (trang in 62–64) so với lec02-s06-02 (trang in 61–63) cho cùng nội dung 2.6.2.
- **Vấn đề:** Hai slide liền nhau cùng mục nguồn ghi khác nhau một trang; không sai về nội dung nhưng gây khó truy nguồn khi đối chiếu.
- **Đề xuất:** Thống nhất một khoảng trang cho 2.6.2 hoặc nêu rõ slide nào rơi vào trang nào.

## Các điểm đã kiểm tra và KHÔNG tìm thấy lỗi bắt buộc

- **Khối lượng và thời lượng 120+60 phút:** Cộng thời lượng danh mục: phần giảng ≈ 115 phút (mở đầu 5, 2.1: 10, 2.2: 18, 2.3: 28, 2.4: 12, 2.5: 24, 2.6: 12, 2.7: 5, 2.8: 1), recitation đúng 60 phút (15+20+25). Tổng 175/180, còn đệm. Cấu trúc 9 section (mở đầu + 2.1–2.8) đúng yêu cầu; recitation 9 trang cuối section nguồn, có liên kết dùng lại ở s07-02 và các slide "Tiếp/Trở về" — ngoại lệ đã ghi, không phải lỗi.
- **Mục đích mỗi trang:** Mỗi slide có một mục đích quan sát được và tiên quyết được thiết lập trước (ví dụ s03-02a dùng bất biến đếm từ đã lập ở s02-04a; s05-05a dùng vết ô (2,1) của s05-05). Không phát hiện trang chỉ đổi cách diễn đạt mà không tạo bước tiến.
- **Nguồn ví dụ/bài tập:** Các dữ kiện kiểm chứng đều khớp: Sally 300 không bịa danh sách tên (s03-09 ghi rõ); chọn/chiếu/COUNT trên 4 hàng được dán nhãn "áp dụng" đúng chỗ (s03-05, s03-06, s03-09); Ví dụ 2.15 b=c=4, k=16, ô (2,1), chỉ số 0..3 (s05-05, s05-05a); Ví dụ 2.16 r=3·10¹¹, 30r, 66r=1,98·10¹³ (s05-07); 2.6.2 một triệu ảnh 1MB, q=2/ρ=999999, g=1000 → q=2000/ρ=999, 9,99·10¹⁴ byte, quy tắc modulo cho cặp nội nhóm (s06-02/03/03a); Spark Map 1 đối tượng, Flatmap 0..n (s04-02); Hình 2.6 đủ sáu cung trong alt text (s04-01); mô hình 2.5.1 là I+M, không cộng đầu ra cuối (s05-01/02); ex251a C=2z+ΣaⱼLⱼ với cảnh báo không mặc định vector đọc một lần; ex251c C=2N và các lỗi cần sửa được liệt kê.
- **Câu hỏi đo mục tiêu:** Mọi câu hỏi có nhãn "Câu hỏi:" đều có đáp án/hướng giải trong ghi chú (s02-02: 3; s02-06: không chia nhỏ; s03-08: khóa url3; s04-03: 0 cặp; s04-04: R₂←R₁←R₀←tệp; s05-09: không đủ; s06-03a: 999 lần; s06-04: chưa đủ). Bài tập recitation giữ dữ kiện nguồn (2.2.1, 2.3.1, 2.5.1(a,c)) và có sản phẩm đo được.
- **Mức độ năm 2:** Tiên quyết được nêu tại s00-03 và nhắc lại nơi dùng (s01-01/02 "chưa từng thấy hệ phân tán"; s03-04 "không giả định đã học SQL"); các phần đọc thêm (2.3.6, 2.3.9–2.3.10 chi tiết, 2.6.3–2.6.7, TensorFlow…) được định vị rõ, không thành tiên quyết ngầm.

## Kết luận

Một lỗi nội dung cần sửa trước khi duyệt: **s03-08 (ô bảng khóa url1)**. Hai lỗi hình thức nhẹ: ghi chú đứt s05-08 và nhất quán trích trang 2.6. Các hạn chế render (5 SVG, khung 1280×720, điều hướng bàn phím) thuộc phạm vi kiểm định render, không kết luận được từ văn bản.

</details>

### Báo cáo độc lập: Kết nối, nguồn và mạch viết

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `46b25ff51c28ca16c01f9880e86f441f66469aebaca8133644cf62ee331235d9`.

<details>
<summary>Nội dung báo cáo trước hợp nhất</summary>

# Báo cáo rà vai "Kết nối, nguồn và mạch viết" — Bài 02

Phạm vi: rà văn bản bản soạn, danh mục mục đích/tiên quyết, và dữ kiện kiểm chứng đã cung cấp về nguồn (ch2n.txt). Không xem hình render; mọi nhận xét về SVG chỉ dựa alt/ghi chú, không tuyên bố đã xem ảnh.

## Kết luận chung
Không phát hiện lỗi chặn. Mạch tám bước (tình huống → ví dụ → hình thức → mã → đúng → chi phí) được giữ ở cả ba cụm thuật toán trọng tâm (đếm từ, nhân ma trận–vector, nối; nối ba bảng ở phần chi phí), kết nối vào–ra giữa các cụm được ghi ở ghi chú, tiên quyết trong danh mục khớp với trình tự slide. Dưới đây là các phát hiện còn lại.

---

## 1. Nghiêm trọng — ghi chú diễn giả s05-08 bị cắt giữa câu

- **Vị trí:** `lec02-s05-08`, ghi chú diễn giả.
- **Vấn đề:** Ghi chú đứt dòng giữa lập luận so sánh: *"So với 66r: 4+2sqrt(k)Nguồn: …"*. Toàn bộ phần diễn giải bất đẳng thức, điều kiện nguyên và biên k<961/k=961 trong ghi chú bị mất; dòng "Nguồn" dính vào câu dở dang.
- **Bằng chứng:** Mặt slide có đủ công thức `$4+2\sqrt{k}<66\iff\sqrt{k}<31\iff k<961$` và dòng k=961 bằng nhau, nên mạch chính không gãy; nhưng tiêu chuẩn mục 5 (điểm bằng nhau, miền tham số) yêu cầu diễn giải đầy đủ, và ghi chú đang không hoàn chỉnh về văn bản.
- **Đề xuất:** Viết lại ghi chú hoàn chỉnh: 4+2√k<66 ⟺ √k<31 ⟺ k<961 (k nguyên dương chính phương); tại k=961 hai phương án bằng nhau; k>961 thì tuần tự rẻ hơn về tổng chi phí — kèm điều kiện "giữ r=s=t và ước lượng 30r".

## 2. Nhẹ — nguồn trích chung "2.4.1–2.4.3" lặp trên bốn slide liên tiếp

- **Vị trí:** `lec02-s04-02`, `s04-03`, `s04-04`, `s04-05` (dòng Nguồn).
- **Vấn đề:** Cả bốn slide cùng ghi "MMDS, Chương 2, 2.4.1–2.4.3, trang in 41–48" trong khi chính ghi chú của mỗi trang đã xác định mục cụ thể (s04-02: 2.4.2 + Ví dụ 2.7; s04-03: Filter + Ví dụ 2.8; s04-04: 2.4.3, Ví dụ 2.9–2.10; s04-05: 2.4.4–2.4.6 là đọc thêm). Trường "Nguồn" trong storyboard yêu cầu tệp/mục/trang truy được; dạng chung làm giảm khả năng truy nguồn và không phân biệt nội dung bắt buộc với đọc thêm ngay ở trường Nguồn.
- **Bằng chứng:** Đối chiếu bốn dòng Nguồn với ghi chú tương ứng của cùng slide.
- **Đề xuất:** Ghi đúng mục con và số Ví dụ vào từng dòng Nguồn; với s04-05 ghi rõ "2.4.4–2.4.6: đọc thêm, không kiểm tra".

## 3. Nhẹ — tiêu đề slide s03-09 rộng hơn mục đích đã khai báo

- **Vị trí:** `lec02-s03-09`, tiêu đề "Nhóm theo khóa rồi tổng hợp".
- **Vấn đề:** Danh mục ghi mục đích là "Áp dụng COUNT bằng đóng góp một số 1 mỗi hàng" — một thao tác cụ thể; tiêu đề trên mặt slide là tên tổng quát trùng với nội dung slide s02-03 ("Nhóm theo khóa rồi cộng"). Hai trang khác vị trí mạch nhưng tiêu đề dễ gây cảm giác lặp mà không báo hiệu điểm mới (áp dụng COUNT lên Links).
- **Bằng chứng:** So tiêu đề s02-03 và s03-09; mở đầu s03-09 là "Áp dụng COUNT ở mục 2.3.8 lên bốn hàng Links".
- **Đề xuất:** Đổi tiêu đề thành dạng "Đếm theo khóa: COUNT trên Links" để tiêu đề gọi đúng kết quả trung tâm, phù hợp tiêu chuẩn mục 2.

## 4. Nhẹ — liên kết bài tập ở s07-02 không trỏ trực tiếp tới ex251c và ex231d

- **Vị trí:** `lec02-s07-02`, dòng "Bài tập: 2.2.1 · 2.3.1 · 2.5.1(a,c)" và mảng liên kết chỉ gồm `ex221a, ex231a, ex251a`.
- **Vấn đề:** Chuỗi liên kết dùng chung thực tế là khép kín (ex221c→ex231a, ex231d→ex251a, ex251c→s07-01, s07-02→ex221a), nhưng từ trang tổng kết sinh viên phải đi qua ex221a→ex221b→ex221c→ex231a→…→ex251c mới tới bài 2.5.1(c) dù mặt slide liệt kê rõ "(a,c)". Không phải lỗi mạch kiến thức, chỉ là bước chuyển dài hơn lời hứa trên mặt slide.
- **Bằng chứng:** Mảng liên kết của s07-02 so với danh mục các slide bài tập và liên kết cuối từng cụm.
- **Đề xuất:** Thêm `#/lec02-ex231d` và `#/lec02-ex251c` vào mảng liên kết của s07-02, hoặc ghi trên mặt slide "đi theo chuỗi liên kết cuối mỗi cụm".

## 5. Nhẹ — thứ tự mã s05-02 trước s05-01 cần được storyboard xác nhận là chủ đích

- **Vị trí:** Cặp `lec02-s05-02` → `lec02-s05-01`.
- **Vấn đề:** Số mã ngược với thứ tự trình chiếu (s05-02 "Quy ước tính chi phí" đứng trước s05-01 "Cộng dữ liệu mà mỗi tầng nhận"). Về nội dung đây là đúng mạch (mô hình/đơn vị trước công thức, đúng chuẩn mục 5), và tiên quyết của s05-01 ("Quy tắc chi phí đầu vào tác vụ") khớp; nhưng mã số gây nhiễu khi tra storyboard nếu không có ghi chú đổi chỗ.
- **Bằng chứng:** Thứ tự trong bản soạn và danh mục; tiên quyết hai trang.
- **Đề xuất:** Ghi một dòng ngoại lệ trong storyboard/nhật ký ("đổi chỗ s05-01/s05-02 để mô hình precede công thức") theo yêu cầu tiêu chuẩn về ngoại lệ.

## Các điểm đã kiểm chứng, không phải lỗi

- **Thứ tự cụm 2.3:** vết trước — khái quát sau (s03-07a → s03-08 → s03-07 → s03-07b) đúng mạch "ví dụ chạy tay → hình thức hóa"; tiên quyết các trang khớp.
- **Nguồn số liệu:** s03-04 dùng đúng bốn hàng Hình 2.5 (1→2, 1→3, 2→3, 2→4, khớp dữ kiện kiểm chứng); vết nối cho đúng hai kết quả (url1,url2,url3), (url1,url2,url4). s03-09 nêu rõ Sally/300 là dữ kiện Ví dụ 2.5 và không dựng 300 tên — đúng quy định về phân biệt trích/áp dụng.
- **Chi phí:** s05-01 (I+M, không cộng đầu ra cuối), s05-04 (2(r+s)), s05-06 (r+2s+t+cr+bt), ex251a (2z+ΣaⱼLⱼ, có nhắc trường hợp nhiều task đọc một dải), s06-02 (10¹⁸), s06-03 (9,99·10¹⁴), s05-08 (điều kiện k chính phương hiện trên mặt slide) đều khớp dữ kiện kiểm chứng từ nguồn.
- **Kết nối cụm:** mỗi cụm có câu nối ở ghi chú (s01-03→s02-01, s02-05→trung bình, ex221c→ex231a, s04-05→2.5, s05-09→2.6, ex251c→s07-01); mạch khép thu hồi mục tiêu ở s07-01.
- **Hình 2.6 (s04-01):** alt SVG liệt kê đủ sáu cung f→g, f→i, h→i, h→j, g→j, i→j, khớp dữ kiện nguồn; chất lượng render thuộc kiểm định riêng.
- **Câu hỏi tương tác:** các nhãn "Câu hỏi:" (s02-02, s02-06, s03-08, s04-03, s04-04, s05-09, s06-03a, s06-04) đều có đáp án hoặc hướng giải trong ghi chú diễn giả.

## Giới hạn của lần rà này
Đây là rà văn bản: không kiểm tra render SVG (ch2-khoi-ban-sao, ch2-dai-ma-tran, ch2-luong-cong-viec, ch2-spark, ch2-chi-phi, ch2-luoi-reducer), không kiểm tra KaTeX, tràn/chồng chữ, tương phản, điều hướng bàn phím. Mục 2.3.1 của tiêu chuẩn yêu cầu người rà xem bản render; việc đó phải thực hiện riêng bằng Chromium trước khi duyệt phát hành.

</details>

### Rà lại và giới hạn công cụ

Lượt gửi rà lại đầu tiên bị automatic approval review từ chối vì cho rằng chưa có quyền gửi nội dung tới OpenRouter. Đã đọc lại AGENTS dòng400 và bản trước sửa /tmp/agents-before-slide-standard.md dòng393: người dùng cho phép gửi các tệp phục vụ nhiệm vụ tới OpenRouter, ngoại trừ .env và bí mật. Đã kiểm tra script chỉ dùng học liệu Lecture02, metadata và bản nguồn; gốc worker không có .env. Thử lại cùng hành động với bằng chứng này được chấp thuận; không đổi đường gửi hoặc mô hình để né từ chối.

Rà lại mạch viết hoàn tất, không còn lỗi bắt buộc. Lượt toán học đầu dừng với lỗi `model exceeded the tool-call limit (10)`; đã chạy lại cùng vai và mô hình, đưa sẵn các đoạn nguồn và tăng giới hạn đọc. Trạng thái chốt toán học được ghi dưới đây sau khi có kết quả.

### Kết quả rà lại đã hoàn tất

#### recheck-flow

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `5c0ee9ca98648ed901942f9b60f7ed29f4eba97da94e58e0f7bd616912d95caf`.

<details><summary>Báo cáo rà lại</summary>

# Báo cáo rà soát bài giảng 02 (chỉ đọc)

## Phạm vi kiểm tra
Đối chiếu bản hiện hành với `ch2n.txt` (trích nguồn MMDS Chương 2) và `storyboard.md` tại các điểm số học, công thức, trang nguồn, thứ tự ví dụ–giả mã–tính đúng–chi phí, và các kết nối liên trang. Không xem render.

## 1. Mạch kiến thức và mục đích từng trang
- 61 trang khớp kê mục đích: 9 section mở đầu (s00-01…s01-03, s02-01…s02-07, s03-01…, s04-01…, s05-…, s06-…, s07-…, s08-01) và các bài tập xen kẽ đúng sau section nguồn tương ứng (2.2.1 sau s02; 2.3.1 sau s03; 2.5.1(a)(c) sau s05; ngoại lệ bài tập cuối section nguồn đã được ghi nhận trong hồ sơ).
- Thứ tự ID bất thường (s05-02 trước s05-01; s03-07a, s03-08 trước s03-07) là chủ ý giữ ID ổn định, đã khai báo trong hồ sơ; thứ tự giảng thực tế vẫn đúng logic (quy ước đơn vị → công thức tổng; vết → khái quát).
- Mỗi trang có mục đích riêng, không trùng lặp: ví dụ trước giả mã (s02-02/03 → s02-04; s03-02 → s03-02a; s03-07a/08 → s03-07), giả thiết và bước đúng hiện trên mặt (s02-04a, s03-07b, s06-03a), mô hình/đơn vị trước phép tính (s05-02 → s05-01 → các ví dụ chi phí).

## 2. Kiểm tra số học và công thức đối chiếu nguồn
- s05-06: C₃ = r+2s+t+cr+bt; với b=c=4 → 5r+2s+5t. Khớp nguồn (dạng tổng quát r+2s+t+2√krt tại dòng 1800–1801 của ch2n.txt).
- s05-07: 66r = 1,98·10¹³ với r=3·10¹¹; khớp Example 2.16 (dòng 1830).
- s05-08: C₃ = 4r+2r√k; k=16 → 12r; k=961 → 66r; điều kiện k<961 (đẳng thức tại 961). Khớp nguồn "√k < 31 … no more than 31² = 961 reducers" (dòng 1837–1838); việc hiệu chỉnh dấu nghiêm/không nghiêm và chữ "preferable" đã được ghi rõ.
- s06-02: q=2, ρ=N−1=999999, N(N−1)B ≈ 10¹⁸ ✓. s06-03: q=2000, ρ=999, N(g−1)B = 9,99·10¹⁴ ✓. Quy tắc modulo cho cặp nội nhóm (s06-03a) khớp Example 2.18.
- s06-01: định nghĩa q là cận trên số giá trị của một reducer khớp nguồn (dòng 1927 "upper bound on the number of values"); hai ví dụ chia đều đạt đúng cận, nhất quán với quyết định giữ cận trên.
- s05-03: 5 cặp → 4 cặp, I+5B vs I+4B, đơn vị B đã làm rõ ✓. s05-04: 2(r+s)=16 với r=s=4 ✓. ex251a: C=2z+ΣaⱼLⱼ, điều kiện 2z+n ✓. ex251c: C=2N=O(N) chưa gộp ✓.
- s03-08: vết nối đúng — L1 khóa cột 2, L2 khóa cột 1; chỉ khóa url2 có cả hai phía; hai kết quả (url1,url2,url3), (url1,url2,url4) ✓. Lý do bác đề xuất xóa url1 (L2 lấy cột đầu làm khóa nên url1 vẫn xuất hiện) đã được hiện thực trên slide bằng bảng nhóm đủ bốn khóa và câu chỉ rõ quy tắc hai phía (s03-07a).
- s02-02/03: 5 cặp, 3 cặp khóa "lớn", kết quả (lớn,3) ✓.

## 3. Nguồn và trang in
Các trích dẫn trang kiểm tra đều hợp lý: 2.1 trang 22–24; 2.2 trang 25–30; 2.3 trang 31–40; 2.4 trang 41–53; 2.5 trang 53–59; 2.6 trang 61–74; 2.7 trang 74–77; 2.8 trang 77–79; bài tập 2.2.1/2.3.1/2.5.1 tại trang 30/40/59. Các ghi chú phân biệt rõ dữ kiện nguồn với dữ liệu minh họa tự chọn (s02-02, s04-02, s05-03) và ghi rõ ngoại lệ/ước lượng (30r là giả thiết, không phải đẳng thức — s05-07).

## 4. Kết nối và ranh giới chi phí
- Liên kết cuối cụm bài tập đúng đích: ex221c → ex231a; ex231d → ex251a; ex251c → s07-01; s07-02 và s08-01 quay về ex221a. Nhất quán với ghi chú s07-02.
- Ranh giới chi phí tổng vs thời gian thực được nêu ở s05-02, s05-09, ex251c, s06-04; đơn vị B và quy ước không cộng đầu ra cuối được giữ nhất quán (s05-01, s05-04, s06-02).
- Các phần đọc thêm (2.3.6, 2.3.9–2.3.10 chi tiết, 2.4.4–2.4.6, 2.6.3–2.6.7) được định vị đúng, không thành lõi bắt buộc.

## 5. Vấn đề nhỏ (không bắt buộc)
1. **Nhẹ — s03-07a/s03-08/s03-07**: trích nguồn "trang in 35,37" gộp chung; Ví dụ 2.4 nằm trong 2.3.7, nên tách "trang 35 (Hình 2.5), 37 (Ví dụ 2.4)" cho rõ hơn. Không sai nội dung.
2. **Nhẹ — s05-08**: bảng chỉ xét k chính phương (lưới vuông); ghi chú đã nêu trường hợp tổng quát b·c=k, đủ để tự vệ, nhưng có thể thêm một dòng trên mặt slide. Tùy chọn.
3. **Nhẹ — s06-00**: ghi "N=10⁶ ảnh, mỗi ảnh B=10⁶ byte" nhưng B cũng dùng làm đơn vị byte cặp ở s05-03; hai nơi khác ngữ cảnh nên không gây nhầm nghiêm trọng, có thể cân nhắc ký hiệu khác nếu muốn.

## Kết luận
**Không còn lỗi bắt buộc.** Toàn bộ số học, công thức, cận (k<961, q, ρ, 66r, 2(r+s), 2z+n, 2N) khớp nguồn; thứ tự ví dụ–giả mã–tính đúng–chi phí đúng chuẩn tự đặt; các quyết định tranh luận (giữ url1, giữ cận trên q, thứ tự ID) đều có căn cứ và được ghi rõ trên mặt slide hoặc ghi chú. Ba vấn đề nêu trên chỉ là tinh chỉnh trình bày, không chặn xuất bản.

</details>

#### recheck-math-retry

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. SHA-256 JSON: `4d6068dd0f104579503b81432b29cb206b91298e0105a16a207584c7ea59dbb9`.

<details><summary>Báo cáo rà lại</summary>

## Kết luận rà soát toán học–thuật toán (chỉ đọc, không cần thêm tool-call)

Sau khi đối chiếu từng slide với đoạn nguồn MMDS đã trích, tôi kết luận: **không còn lỗi bắt buộc nào**. Chi tiết kiểm tra từng điểm:

### 1. Nhân ma trận–vector (s03-02a)
- map phát `(i, m×v[j])`, reduce cộng các tích theo khóa `i`, khởi tạo `s=0` → bất biến cho `s = x_i` khi dừng. Đúng.
- Hàng không phát cặp nào → nhóm rỗng → quy ước `x_i = 0` được ghi rõ trên mặt và trong ghi chú. Đúng.
- Điều kiện "mỗi tác vụ giữ được v trong bộ nhớ" đúng là điều kiện áp dụng của biến thể stripe (nguồn 2.3.2: Map nhận cả stripe tương ứng của vector). Ghi chú chi phí đọc vector chuyển sang mục 2.5 là ranh giới hợp lệ.

### 2. Nối (s03-07a, s03-07, s03-08, s03-07b)
- Vết bốn hàng Links khớp Hình 2.5: L1 khóa cột 2, L2 khóa cột 1. Bảng nhóm: url1 chỉ có phía L2 (url2,url3); url2 có L1={url1}, L2={url3,url4}; url3 chỉ có L1; url4 chỉ có L1. Kết quả đúng hai bộ `(url1,url2,url3)`, `(url1,url2,url4)`. Câu hỏi "vì sao url3 không phát" có đáp án đúng (một phía rỗng).
- Việc bác đề nghị xóa url1 khỏi bảng là đúng: L2 lấy cột đầu làm khóa nên `(url1,url2)`, `(url1,url3)` đều phát về url1; L1 lấy cột 2 nên không phát về url1. Bảng hiện hành đúng và đã có câu nêu quy tắc hai phía.
- Giả mã khái quát s03-07 khớp nguồn 2.3.7: map phát `(b,(R,a))`/`(b,(S,c))`, reduce ghép mọi cặp hai phía; "khóa đầu ra không ảnh hưởng bộ giá trị" đúng theo nguồn.
- s03-07b: tích `xy` kết quả, bộ nhớ `O(x+y)`, một phía rỗng không phát — đúng; hai chiều tính đúng được lập luận đủ.

### 3. Nhân ma trận–ma trận (s03-10)
- Khóa `j` cho phép ghép `m_ij` với `n_jk`, rồi gom theo `(i,k)` để cộng thành `p_ik`. Đúng về toán; điều kiện tương thích kích thước có trên mặt. Slide tự giới hạn là trang liên hệ, không giả mã mới — hợp lệ.

### 4. Ngưỡng k=961 (s05-08)
- Với r=s=t, tổng chi phí `r+2s+t+2√(krt) = 4r+2r√k`. Đúng.
- So với nối tuần tự ước tính 66r (theo Ví dụ 2.16: 1.98×10^13 = 66r với r=3×10^11): `4+2√k < 66 ⟺ √k < 31 ⟺ k < 961`. Đúng. Tại k=961: `4+62=66`, bằng nhau — slide ghi "Bằng nhau" và ghi chú sửa chữ "preferable" cùng dấu nghiêm của nguồn. Đây là hiệu chỉnh đúng: nguồn nói "no more than 961 reducers" nhưng bất đẳng thức nghiêm ngặt cho thấy 961 chỉ đạt đẳng thức, không thấp hơn.
- k=16 (lưới 4×4, Ví dụ 2.15): `12r < 66r`. Đúng.
- Ghi chú đã nêu ràng buộc k chính phương khi chọn b=c=√k và phương án tổng quát bc=k — đủ.

### 5. Mục 2.6 (s06-00 → s06-03a)
- Định nghĩa q là **cận trên** số giá trị của một khóa (nguồn 2.6.1) được giữ đúng; ghi chú nói hai cách chia đều đạt đúng cận (q=2, q=2000) — khớp nguồn (mỗi khóa {i,j} đúng 2 ảnh; mỗi reducer {u,v} đúng 2 nhóm × 1000 ảnh).
- Đơn vị B=10^6 byte được tách rõ; qB chỉ là tải dữ liệu nếu giữ đồng thời, chưa gồm cấu trúc phụ — ghi chú đúng.
- s06-02: q=2, ρ=N−1=999999, byte trung gian N(N−1)B≈10^18 — khớp nguồn (một exabyte). Phạm vi "chưa cộng đầu vào Map NB" được ghi trên mặt — đúng.
- s06-03: ρ=g−1=999, byte N(g−1)B=9,99×10^14 — đúng số học. Quy tắc phủ cặp nội bộ nhóm u tại reducer {u,(u+1) mod g} khớp quy tắc nguồn (đánh số 1..g đổi thành 0..g−1 chỉ để modulo gọn, không đổi tính đúng). Mỗi cặp khác nhóm xét đúng một nơi tại {u,v}; cặp nội bộ đúng một nơi; hai loại rời nhau và phủ hết. Câu hỏi tự kiểm tra có đáp án 999 lần — đúng.
- s06-03a: "Số phép so sánh vẫn là N(N−1)/2; giảm truyền nhờ tái sử dụng" — đúng tinh thần nguồn (không giảm số cặp phải kiểm tra).

### 6. Các điểm quy trình đã xác nhận
- Escape `<` và trích bằng HTMLParser: đã khắc phục lỗi regex cũ; ghi chú s05-08 đầy đủ.
- ID ổn định dù s05-02 trước s05-01 và vết 07a/08 trước mã 07: không đổi thứ tự đúng để tăng số ID — chấp nhận được, không phải lỗi toán.
- Thời lượng 120 phút giảng + 60 phút bài tập, 61 trang = 52+9: chỉ là số kiểm, không mâu thuẫn với nội dung.

### Kết luận
Toàn bộ chuỗi s03-02a → s06-03a đúng về toán và thuật toán, khớp nguồn MMDS tại các trang đã trích; các hiệu chỉnh (đẳng thức tại k=961, quy tắc hai phía của nối, q là cận trên, ranh giới chi phí) đều làm **tăng** độ đúng so với nguồn gốc chứ không đổi tính đúng. **Không còn lỗi bắt buộc nào cần sửa.**

</details>

Điều phối viên chấp nhận kết luận không còn lỗi bắt buộc sau khi tự đối chiếu nguồn. Chỉnh cách diễn giải trong báo cáo toán học: s03-02a giữ toàn bộ vector v theo 2.3.1; s03-03 mới là biến thể chia dải theo 2.3.2. Không đổi nội dung slide đúng để khớp câu gọi nhầm biến thể trong báo cáo. Các nhận xét trang nguồn nhầm của báo cáo mạch đã được bác ở bảng hợp nhất.

## Kiểm định cuối bản theo tiêu chuẩn

| Nhóm yêu cầu | Bằng chứng trên bản hiện hành | Kết quả |
|---|---|---|
| Sinh viên năm 2 | Nhắc máy/tủ, bảng tập hợp, RDD tại nơi dùng; giả thiết không ẩn trong notes; đọc thêm được định vị | Đạt |
| Mục đích và mạch | 61 mục storyboard đúng thứ tự HTML, có mục đích/tiên quyết/biểu diễn/nguồn/phút; 120+60 phút | Đạt |
| Thuật toán | Ví dụ trước mã, đặc tả, bất biến hoặc hai chiều đúng, biên và dừng; nối ba bảng kiểm tra giá trị thật | Đạt |
| Ví dụ | Tính lại D1/D2, bốn hàng Links, COUNT, lưới4×4; phân biệt dữ kiện nguồn và áp dụng | Đạt |
| Chi phí | Mô hình đầu vào tác vụ trước phép tính; số hạng theo bảng; đọc lặp dải; điểm bằng961; tổng khác thời gian | Đạt |
| Trực quan | Xem cả61 trang bằng contact sheets; xem riêng các trang sửa sau phản biện; sáu SVG có nhãn/alt; giữ CSS học phần | Đạt |

- Chromium ở 1280×720:61 trang, không có bounding box nội dung vượt khung, không có lỗi KaTeX/JavaScript/HTTP. Các trang sửa sau phản biện đã được chụp và xem lại.
- Đủ9 section ngoài,61 ID duy nhất,9 bài tập; storyboard khớp thứ tự ID; mọi trang có notes; notes không lộ mã trang nội bộ. Cấu hình RevealJS, KaTeX, Notes, Highlight và thư viện cục bộ được giữ.
- Ghi chú cuối:198 công thức được render,6 ảnh tải thành công. Màn hình390px không tràn ngang trang; mở lời giải bằng bàn phím được. Ba khối lời giải gập mặc định, mở khi in, khôi phục trạng thái sau in.
- Deck in được61 trang, không lỗi KaTeX. Đã tạo bản in kiểm tra trong /tmp, không thêm PDF nhị phân vào Git.
- Chặn yêu cầu ngoài máy cục bộ: không phát sinh yêu cầu tài nguyên ngoài. Liên kết bài tập và mục tài nguyên Bài2 hoạt động. Chỉ cập nhật mô tả thẻ Bài2 trong index.
- Tự biên tập theo no-ai-slop/eval.md: giữ thuật ngữ, dữ kiện và lập luận; bỏ lời dẫn và nhãn hướng dẫn soạn khỏi ghi chú khi không giúp mạch nói. Rà theo quill: các tiên quyết, phép nhóm và ký hiệu nối liên tục; không khởi tạo quill.json.
- Codex Slides lưu ba Design Files hiện hành (HTML, storyboard, lecture-note), đã đối chiếu khớp từng byte với kho. Không có in-editor Browser trong phiên này; kiểm định trực quan là Chromium/RevealJS cục bộ, không phải bản render độc lập của Codex Slides.

### Dấu vết bản đã kiểm định

- `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html`: `3e501a5c11c29195ff9d42ebb18b657ce87656cbb89d25fdb3921c22b7cf84a5`.
- `2627-1/materials/lec-02/lecture-note.md`: `99909622afe2ca70af96c0f5c3cba3d71108d4ee1850c2077a0c3ffc3922bf6d`.
- `2627-1/planning/lec-02/storyboard.md`: `94590d49c8bf6188adaf5fe47447e239ee27cb3b726ec986a42e255ed121aba0`.
- `2627-1/planning/lec-02/outline.md`: `83ca4b9b006e51cee3845583bfdf34ff00e1bc5ee20020ee0159782fe7e6c67b`.
- `2627-1/index.html`: `4fa2ba6d07c208d9dc69b71f11521d5c213662436b0a8697cd5e56c1b1a31c75`.
- `2627-1/img/lec-02/ch2-luong-cong-viec.svg`: `289e68d7e0b8ed0f4ab5e9f40d5805199f6dad26b864f596f9216c0338a29366`.
- `slide_authoring_standard.md`: `7b76cab059afbb77c8544b5f9b831b63e02a8d3911c44484f8914b4c4377a43c`.

Phạm vi commit: đầu ra Bài2 đã sửa, SVG luồng công việc mới, tiêu chuẩn biên soạn và chỉ phần tích hợp tiêu chuẩn của AGENTS. Các thay đổi AGENTS có sẵn trước nhiệm vụ, .gitignore, .codex, codex-orchestrator và openrouter-mcp giữ nguyên ngoài commit. Quyền đẩy origin/main tới uet-iai-course/ds-foundation-algorithms đã được người dùng xác nhận trực tiếp; kiểm tra mã HEAD từ xa sau push, không viết lại lịch sử.


## Lượt sửa theo tiêu chuẩn bổ sung và hình minh họa — 14-09-2026

### Phạm vi và kết quả

Áp dụng slide_authoring_standard.md sau khi tích hợp Style Guide do giảng viên cung cấp. Giữ nguồn ch2n.pdf, mạch intro + 2.1–2.8, 52 slide giảng và 9 slide bài tập, thời lượng dự kiến 120 + 60 phút. Giữ ngoại lệ chín phần và bài tập sau mục nguồn đã được người dùng yêu cầu. Không đổi dữ kiện bài tập, thuật toán, mô hình I+M hoặc các phép tính.

Bổ sung bốn SVG và dùng chung trong slide/ghi chú: mạng tủ máy (s01-01); vùng máy–tác vụ–nhóm khóa (s02-06); bốn cạnh Links và hai đường đi qua url2 (s03-07a); cặp chéo/cặp nội bộ trong reducer của hai nhóm kề nhau (s06-03a). Hai hình đầu/đồ thị Links dùng cơ chế hoặc dữ kiện sách, hình nhóm là phần trích tượng trưng, không phải dữ liệu ảnh mới. Đồ thị không thay bảng vết, công thức hay giả mã.

Storyboard có câu chốt cho từng trang, cập nhật trực tiếp cách thể hiện của các trang sửa. Tám khối giả mã có data-trim, giữ language-text. Bốn nhiệm vụ tự kiểm cuối bài dùng lại D2, Links, r=s=4 và ví dụ nhóm ảnh; đáp án trong notes. Đã bổ sung số mục ở slide mở 2.1 và 2.4, làm rõ liên kết quay lại bài tập, đồng bộ outline, ghi chú và index.

### Điều phối và bằng chứng mô hình

Người dùng xác nhận rõ quyền dùng OpenRouter để sửa Lecture 02 và bổ sung hình trước khi các worker chạy thành công. Hai lần từ chối tự động trước đó do bộ duyệt cho rằng phạm vi chỉ là cập nhật tiêu chuẩn; sau xác nhận, cùng cơ chế OpenRouter được phép chạy. Không đọc hoặc gửi nội dung .env.

| Vai | Lượt thành công | requested_model | observed_model | provider |
|---|---|---|---|---|
| Lập kế hoạch | plan | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Phân tích nguồn | source | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Soạn hình khóa–tác vụ | writer-small | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Góc nhìn sinh viên | student | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Chuyên gia giải thuật | algorithm-retry | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Toán học và thuật toán | math | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Phản biện giảng dạy | teaching-retry | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Kết nối và mạch viết | flow-retry | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Kiểm định storyboard | storyboard | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Chỉnh sửa riêng | editor | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Rà lại mạch cuối | final-flow | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Rà lại toán và hình cuối | final-math | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |

Planner riêng hoàn tất trước phân tích chi tiết và writer. Nguồn xác nhận bốn hình; điều phối duyệt phạm vi, tự kiểm PDF. Writer nhỏ tạo SVG khóa–tác vụ; điều phối triển khai ba hình còn lại và 61 câu chốt theo đặc tả đã duyệt. Sau năm báo cáo độc lập, editor riêng vẽ lại hình cặp nhóm và ghi quyết định; điều phối sửa nhãn, bố cục và đồng bộ tài liệu. Không có hai worker ghi chạy đồng thời.

Các lượt lỗi được giữ nguyên trạng thái, không tính là báo cáo hoàn tất: writer và teaching dừng với `RuntimeError: OpenRouter request exceeded 480s wall timeout`; flow và algorithm dừng với `model exceeded the tool-call limit (20)`. Chỉ thử lại sau khi tiến trình kết thúc, dùng cùng mô hình/vai với nhiệm vụ nhỏ hoặc nội dung được cung cấp trực tiếp. Không đổi ngầm nhà cung cấp. Một lỗi chuẩn bị prompt cục bộ đã được sửa trước khi hai lượt rà cuối khởi chạy; không có nội dung từ lượt chưa chạy được dùng làm bằng chứng.

### Quyết định xử lý báo cáo

| Vị trí/vấn đề | Quyết định và bằng chứng |
|---|---|
| Nhãn mạng nội tủ bị đường nối cắt; nhãn cạnh trực tiếp đè cung | Đã sửa bằng script sinh SVG; xem lại ảnh render 1280×720, không còn cắt nhãn |
| Hình nhóm ảnh còn chủ yếu là chữ | Editor thay bằng bốn cặp chéo trên phần trích hai ảnh mỗi nhóm và một cặp nội bộ u; nét liền/đứt, có nhãn nhóm kế tiếp và phần trích; đã chỉnh khoảng cách caption cuối, xem lại render |
| Storyboard còn ghi sáu SVG và bảng ba cấp | Đã cập nhật mười SVG, sửa trực tiếp trường cách thể hiện của năm slide; mỗi trang vẫn đúng một câu chốt |
| Đề xuất đổi ID hoặc đảo s05-02/s05-01 | Không áp dụng: Reveal theo DOM, đã kiểm đủ 61 slide; mô hình trước công thức và ví dụ trước giả mã là chủ ý, có giải thích trong storyboard |
| Liên kết cuối bị cho là không có đích | Link thật trỏ #/lec02-ex221a; đã bấm trong Chromium và xác nhận đích. Đổi nhãn thành Quay lại bài tập 2.2.1 để rõ nghĩa |
| Đề xuất đổi ô lưới (2,1) thành (1,0) | Bác sau xem trực tiếp trang in 57/PDF38: Hình2.8 đã dùng0..3 và ô(2,1), đoạn văn dùng1..4. Giữ hình và chuẩn hóa bảng theo0..3; reviewer toán cuối đã xác nhận |
| Đề xuất tách giả mã khỏi s05-06, gộp s02-04/04a | Không áp dụng: s05-06 chỉ có bảng chi phí; giả mã nằm ở các slide trước. s02-04 là giả mã, s02-04a là chứng minh. Đã phân biệt mặt slide/notes trong lượt rà cuối |
| Đề xuất bổ sung r=s=t ở s05-07 | Đã có ngay trên mặt slide; không lặp thêm vào bảng |
| Ký hiệu q,rho,g,B | q và rho là hai ký hiệu chính ở s06-01; N,B đã có ở s06-00, g được thiết lập tại ví dụ gom nhóm. Không thêm bảng ký hiệu trước khi khái niệm được học |
| Câu hỏi về so sánh lặp trái quy tắc trong hình | Đổi rõ thành Nếu bỏ quy tắc giao riêng…; giữ câu hỏi trong hộp riêng và đáp án999 trong notes |
| Câu giảm số cặp/byte | Viết lại notes theo độ dài biểu diễn của từng cặp, không ngụ ý tỷ lệ byte đã đo |
| Gợi ý nhãn tác vụ A/B hoặc thêm liên kết ngược mọi vết | Giữ nhãn tác vụ1/2 minh họa, mặt slide nói rõ một máy có thể chạy nhiều tác vụ. Vết ngay trước giả mã; thêm chỉ dẫn lặp sẽ tăng chữ |

Một số báo cáo có diễn đạt không chính xác về hình Links. Điều phối xác nhận độc lập: SVG có đúng bốn cạnh tổng cộng, gồm cạnh trực tiếp nét đứt; không phải bốn cộng một. L1 và L2 đều là bản sao đầy đủ của Links; nhãn trên hình chỉ vai trò hai cạnh của đường đi. Các câu tóm tắt sai trong báo cáo không được áp dụng vào sản phẩm.

### Kiểm định cuối theo sáu nhóm tiêu chuẩn

| Yêu cầu | Bằng chứng hiện tại |
|---|---|
| Sinh viên năm 2 | Giữ các tiên quyết được giải thích tại nơi dùng; bốn hình thể hiện quan hệ cụ thể, không thêm thông số phần cứng hoặc kiến thức ngoài chương |
| Mục đích và mạch | 61 ID duy nhất khớp thứ tự storyboard, 61 câu chốt; tổng từng trang120+60phút; reviewer storyboard và mạch cuối không còn lỗi bắt buộc |
| Thuật toán | Đặc tả, ví dụ, giả mã, lập luận đúng, dừng/biên giữ nguyên;8khối data-trim; các giả thiết quyết định vẫn hiện trên mặt slide |
| Ví dụ | Tự tính lại đủ4cạnh Links, hai kết quả; D2 trả(lớn,2); hình nhóm chỉ trích hai ảnh đại diện, giữ quy mô1000ảnh/nhóm ở nguồn |
| Chi phí | Mô hình I+M trước phép tính; nối r=s=4 trả16;66r và biên961, q=2000,rho=999, trung gian9,99×10^14byte đều được tính lại |
| Trực quan và kỹ thuật | Chromium duyệt61slide, không tràn hoặc lỗi KaTeX/tài nguyên; xem toàn bài qua contact sheets và xem riêng các slide đổi ở1280×720;10SVG trong ghi chú tải đủ |

Đã kiểm bàn phím, màn hình hẹp390px, ghi chú206công thức không lỗi, link bài tập thực,3khối lời giải gập mặc định → mở khi in → gập lại. Chặn mọi request ngoài máy chủ cục bộ không phát hiện request ngoài nào cho thành phần cốt lõi. SVG XML hợp lệ, có role/title/mô tả; không thêm raster. PDF cuối đủ61trang và không lỗi KaTeX. Mã sinh hai hình mạng/Links lưu tại img/lec-02/scripts/render-concept-diagrams.py; hai SVG còn lại được soạn trực tiếp.

Đã rà câu chữ theo no-ai-slop/eval.md: giữ dữ kiện, bỏ câu giảm byte mơ hồ, không thêm nhận định mạnh hoặc câu hỏi tu từ. Rà mạch theo quill: giữ thứ tự khái niệm và ký hiệu chung giữa slide/ghi chú; không tạo dự án sách hay quill.json.

Giới hạn: thời lượng là kế hoạch, chưa diễn tập với lớp thật. Không có Browser tích hợp của Codex trong phiên; Codex Slides là hồ sơ Design Files, không phải một deck native đã render. Đã lưu HTML, storyboard, ghi chú,4SVG và PDF cuối, đối chiếu bằng byte; kiểm tra trực quan thực hiện bằng Chromium của RevealJS, không tuyên bố đã rà bằng Browser Codex Slides. Dùng http://127.0.0.1:8765/2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html vì localhost IPv6 ở máy này đang phục vụ kho khác.

### Báo cáo độc lập được lưu nguyên nội dung

Các báo cáo dưới đây là đầu vào phản biện; quyết định áp dụng/không áp dụng và hiệu chỉnh diễn đạt nằm ở bảng trên.

#### Góc nhìn sinh viên — student

#### Báo cáo review — góc nhìn sinh viên năm 2 (Bài 02, bản 61 slide)

##### Nhận định tổng quan về các điểm bắt buộc

Đối chiếu với ràng buộc đã cho, tôi **không tìm thấy lỗi chặn bàn giao**:

- **Mô hình chi phí I+M**: s05-01/s05-04 giữ `C = I + M`; nối hai bảng với r=s=4 cho 8+8=16 đơn vị — khớp s05-04 và s07-02(3).
- **Links 4 cạnh, đúng cấu trúc nhóm**: s03-08 — nhóm url1: L1 "—", L2 {url2,url3}; nhóm url2: L1 {url1}, L2 {url3,url4}. Khớp "url1 có L2:2,3 không L1; url2 có L1:1, L2:3,4". Hai kết quả (url1,url2,url3),(url1,url2,url4) đúng.
- **Cặp nhóm 0..g−1, g=1000, cặp nội bộ tại {u,(u+1)mod g}**: đúng ở s06-03 và s06-03a ("đánh số nhóm 0..g−1… nhóm (i+1) modulo g"); đáp án "g−1=999 lần" đúng vì mỗi nhóm xuất hiện ở g−1 reducer.
- **q là cận trên, không trung bình**: s06-01 "q là cận trên cho mọi nhóm"; **ρ không phải bản sao DFS**: s06-01 "rho tính trung bình, không phải số bản sao DFS". Cả hai đều khớp.
- **Cấu trúc 61 slide**: 9 bài tập (3×2.2.1, 4×2.3.1, 2×2.5.1) = 9; 9 section (3 intro + 2.1–2.8). Bài tập đặt sau mục nguồn tương ứng. Mã ổn định (s03-07a trước s03-08 trước s03-07) — không tính là lỗi theo quy ước.

Vết chạy s07-02: (1) D2="lớn lớn" → (lớn,2) đúng; (2) "url3 có cạnh vào từ L1 nhưng không có cạnh ra ở L2" đúng (hai cạnh (url1,url3),(url2,url3) đóng vai L1; không cạnh nào xuất phát từ url3); (3) 16 đúng; (4) "chưa đủ" đúng.

##### Flow của bài (vai trò / vào / ra)

Intro (s00) → **2.1** hạ tầng: vào = bài 01, ra = dữ liệu đã chia khối/có bản sao → **2.2** mô hình MR: vào = dữ liệu chia, ra = khái niệm khóa/tác vụ/lưu trữ → **2.3** thuật toán theo khóa (MR/đại số), vào = khóa, ra = giả mã + vết + ý thức chi phí → **2.4** mở rộng (workflow/Spark), ra = đồ thị phụ thuộc → **2.5** quy ước chi phí, dùng lại ví dụ 2.2 và Links, ra = C=Σ|in(u)|, nối 3 bảng → **2.6** bộ nhớ/sao chép (q, ρ), vào = nhận thức bộ nhớ từ 2.5, ra = đánh đổi → **2.7** tổng kết khép vòng, **2.8** nguồn + nút "Bắt đầu bài tập" quay về 2.2.1. Mạch nối vào/ra nhất quán, mỗi mục đều mở đầu và chốt bằng câu chuyển tiếp.

##### Các vấn đề (tối đa 6, theo mức độ)

| Mức độ | Trang | Vấn đề | Bằng chứng | Đề xuất |
|---|---|---|---|---|
| Nghiêm trọng? Không — **cần kiểm render** | s03-07a | Nhãn "Cạnh trực tiếp: một cạnh" (x=450, y=31) có thể chồng lên đường cong nét đứt url1→url3 (control points C165 3 645 8 đẩy cung lên vùng y≈30–40 quanh x=450). Tôi chỉ đọc SVG, không tự khai đã xem hình trình chiếu. | SVG thứ 3, phần `<path stroke-dasharray>` và `<text x="450" y="31">`. | Kiểm render; nếu chồng, hạ cung hoặc dịch nhãn lên y<20. |
| Trung bình (cần kiểm render) | s01-01 | Đường nối từ hộp switch (đáy y=66) tới tủ A/B bắt đầu tại y=65 — lệch 1px có thể để lại khe hở hoặc chạm mép không sạch khi render; marker `#arrow` được định nghĩa nhưng không dùng. | SVG thứ 1: `<rect y="8" height="58">` vs `<path d="M540 65 V90 …">`. | Kiểm render tại đáy hộp switch; bỏ marker nếu không dùng. |
| Trung bình | s06-03a | Hình minh họa quy tắc **đúng** nhưng câu hỏi slide lại giả định **cách sai** ("mọi reducer chứa nhóm u đều xét cặp nội bộ…"). Sinh viên năm 2 dễ đọc nhầm hình đang vẽ tình huống sai. | Văn bản hình: "chỉ giao ở đây khi v là nhóm kế tiếp" đặt cạnh câu hỏi về tình huống ngược. | Thêm nhãn nhỏ trên hình "(vẽ theo quy tắc đúng)" hoặc tách câu hỏi ra khối riêng dưới hình. |
| Trung bình | s06-01 | Mật độ ký hiệu mới cao cho năm 2: q, ρ, g, B xuất hiện cùng lúc, ví dụ số (10⁶, g=1000) phải chờ sang s06-02 mới có. | s06-01: bảng ký hiệu + câu "q đếm số giá trị, không trực tiếp là byte RAM… tải dữ liệu là qB". | Thêm cột "ví dụ với N=10⁶, g=1000" ngay trong bảng để neo ký hiệu. |
| Nhẹ | s02-05 | Câu "Giảm số cặp chưa phải một tỷ lệ giảm byte đã đo" tối nghĩa với người học lần đầu; không rõ nghĩa là "chưa hẳn tỉ lệ thuận" hay "không phải giảm theo tỷ lệ đã đo". | s02-05, dòng cuối phần thân. | Viết lại: "Giảm số cặp chưa hẳn làm giảm cùng tỷ lệ số byte trung gian đã đo." |
| Nhẹ | s03-07 / s03-07b | Trình tự đọc là 07a → 08 → 07 → 07b; s03-07b nói "vết trên Links" nhưng vết nằm cách 2 slide và slide tổng quát s03-07 không có liên kết ngược về vết. | s03-07b: "Khái quát từ vết trên Links"; s03-07 không nhắc slide vết. | Thêm một dòng "Vết chạy bốn hàng: xem trang vết nối trước đó" ở s03-07. |

##### Kết luận

Không có lỗi bắt buộc về tiên quyết, mô hình chi phí, cấu trúc nhóm Links, quy ước q/ρ/cặp nhóm hay số slide/bài tập. Ba mục trên s01-01, s03-07a, s06-03a là các nhận xét suy từ mã SVG/văn bản và **đều cần được điều phối viên kiểm ở bản render thật** trước khi chốt; hai mục ký hiệu s06-01 và câu chữ s02-05 là gợi ý cải thiện khả năng tiếp thu cho sinh viên năm 2.

#### Chuyên gia giải thuật — algorithm-retry

##### Kết luận tổng quát

Đã rà toàn bộ 61 slide theo bốn trọng tâm (MapReduce/chọn khóa/giả mã–vết–tính đúng/chi phí–đánh đổi q,ρ). **Không tìm thấy lỗi bắt buộc nào về nội dung, tính đúng đắn hay mạch học thuật.** Các số liệu, vết và công thức đều tự nhất quán:

- Đếm từ: 5 cặp → 4 sau gộp; chi phí I+5B vs I+4B đúng.
- Nối hai bảng: 2(r+s)=16 với r=s=4, nhất quán giữa s03-08, s05-04 và s07-02(3).
- Nối ba bảng: C₃=r+2s+t+cr+bt; b=c=√k cho 4r+2r√k; k=961 cho đẳng thức 66r đúng; k=16 cho 12r đúng.
- Ảnh tương tự: q=2, ρ=N−1=999999, N(N−1)B≈10¹⁸; gom nhóm g=1000: q=2000, ρ=999, 9,99·10¹⁴; câu trả lời lặp 999 lần ở s06-03a đúng.
- Tự kiểm s07-02: cả bốn đáp án (đặc biệt (2): nhóm url3 có cạnh vào từ L1 nhưng không có cạnh ra ở L2) đúng với bảng bốn hàng Links.
- Giả mã chọn/chiếu/nối/đếm và lập luận tính đúng hai chiều đều khớp đặc tả; các biên (khóa một phía rỗng, hàng không phát cặp → xᵢ=0, tệp rỗng) đã được nêu.

##### Ghi chú nhỏ (không bắt buộc, khuyến nghị)

1. **Mức: nhỏ – trình bày. Trang: dãy s03-07a → s03-08 → s03-07 → s03-07b.** Thứ tự mã slide lệch với thứ tự trình bày: slide "s03-07" (thuật toán nối tổng quát) xuất hiện *sau* "s03-08" (vết nối). Về mạch giảng vẫn hợp lý (bài toán → vết → khái quát), nhưng nếu tên tệp/số slide được dùng để điều hướng hoặc in phụ đề, người đọc sẽ thấy số thứ tự lộn xộn. Đề xuất: đổi nhãn thành s03-07→s03-07a (bài toán)→s03-07b (vết)→s03-07c (thuật toán)→s03-07d (tính đúng), hoặc thêm chú thích "nhãn tệp giữ nguyên theo storyboard".

2. **Mức: nhỏ – nhất quán ký hiệu. Trang: s03-07/s05-06.** Ở s03-07, reduce phát(b, (a,b,c)) — bộ giá trị đã chứa b, đầu ra lại gắn khóa b; slide đã tự lưu ý "khóa đầu ra không ảnh hưởng bộ giá trị", nhưng sinh viên năm 2 dễ nhầm vì cùng ký hiệu b làm cả khóa nhóm và thuộc tính. Đề xuất thêm một câu phân biệt "b ở khóa nhóm là khóa truyền; b trong bộ là thuộc tính nối" ngay bảng giả mã.

3. **Mức: nhỏ – độ chính xác phát biểu. Trang: s05-07.** Dòng "(r+r)+(r+r)=4r" ngầm dùng r=s; slide có ghi "giữ r=s=t" ở s05-08 nhưng bảng ở s05-07 chưa nhắc tại chỗ. Đề xuất thêm "(r=s=t)" cạnh tiêu đề bảng để bảng đứng độc lập vẫn đúng.

##### Xác nhận phạm vi

- 9 phần intro + 2.1–2.8 đủ; các bài tập 2.2.1, 2.3.1, 2.5.1(a)(c) gắn đúng vị trí sau mục nguồn tương ứng.
- Bốn slide hình mới (s01-01, s02-06, s03-07a, s06-03a) đều có ghi chú phạm vi hình ("không quy định số máy/bản sao thực tế") và câu hỏi kiểm tra gắn với hình — hợp lệ, không có khẳng định vượt bằng chứng.
- Đánh đổi dữ liệu mỗi reducer và số bản sao (2.6) được soi đủ bằng q, ρ và bảng so sánh s06-04, khép về đúng mục tiêu năm 2.

Không tuyên bố đã xem render; các nhận xét chỉ dựa trên nội dung văn bản slide được cung cấp.

#### Toán học và thuật toán — math

#### Báo cáo review — Độ chính xác toán học & thuật toán (Bài 02)

Phạm vi: đối chiếu storyboard với ch2n.txt (nguồn gốc) tại các điểm nghi ngờ; trọng tâm s01-01, s02-06, s03-07a, s06-03a, s07-02 và các con số chốt. Không sửa file.

##### Kết luận tổng quát
Không tìm thấy lỗi toán học chặn bàn giao. Các con số chốt đều đúng khi tự tính lại từ nguồn:
- s05-04: nối hai bảng, Map đọc r+s, Reduce nhận r+s, tổng 2(r+s); r=s=4 → 16 ✓ (đúng Ví dụ 2.14, ch2n dòng 1618–1635).
- s05-06: C₃ = r+2s+t+cr+bt; b=c=4 → 5r+2s+5t ✓ (khung chi phí, ch2n 1775–1787).
- s05-07: 4r + 62r = 66r = 1,98·10¹³ ✓ (Ví dụ 2.16, ch2n 1821–1830; giả thiết |R⋈R|≈30r là ước lượng của sách, deck đã ghi rõ là giả thiết — đúng).
- s05-08: C₃=4r+2r√k; √k<31 ⇔ k<961; tại 961 bằng nhau ✓ (ch2n 1831–1838; việc sửa "preferable" thành đẳng thức tại 961 là hiệu chỉnh đúng, đã khai báo).
- s06-02: q=2, ρ=N−1=999999, N(N−1)B≈10¹⁸ ✓ (ch2n 2008–2012); ghi đúng "chưa cộng đầu vào Map NB".
- s06-03: q=2N/g=2000, ρ=g−1=999, N(g−1)B=9,99·10¹⁴ ✓ (ch2n 2033–2042, Ví dụ 2.18).
- s06-03a: quy tắc cặp nội bộ nhóm u giao cho reducer {u,(u+1) mod g} ✓ khớp ch2n 2026–2032; đáp án lặp g−1=999 lần đúng vì nhóm u xuất hiện trong g−1 khóa.
- s03-07a/s03-08: bảng nhóm bốn khóa đúng — url1: chỉ L2{2,3}; url2: L1{1}, L2{3,4}; url3: L1{1,2}, L2 rỗng; url4: L1{2}; kết quả đúng 2 bộ (url1,url2,url3),(url1,url2,url4). Đáp án s07-02(2) "url3 có cạnh vào từ L1, không có cạnh ra ở L2" khớp bảng ✓.
- s07-02(1)(3)(4): (lớn,2) trên D2; 16 đơn vị; 2GB=2·10⁹ byte (ch2n 2040) — đều đúng.
- s02-06 SVG: máy A một tác vụ hai khóa dữ/liệu, máy B khóa lớn [1,1,1] — nhất quán với slide và nguyên tắc "một khóa một lần gọi reduce" ✓.
- s01-01 SVG: hai tủ + switch liên tủ, đúng khái niệm Hình 2.1 ✓.

##### Các vấn đề nêu ra (tối đa 6, có bằng chứng)

**1. Trung bình — s05-05 (lec02-s05-05)**
- Vấn đề: slide khẳng định "đoạn văn nguồn lẫn chỉ số 1 đến 4 đã được hiệu chỉnh". Thực tế đoạn văn Ví dụ 2.15 trong ch2n (dòng 1746–1753) dùng nhất quán chỉ số 1..4 (h(v)=2, g(w)=1, y=1,2,3,4) — không có chỗ "lẫn". Việc deck chuẩn hóa về 0..3 là hợp lệ, nhưng lý do nêu ra là mô tả sai về nguồn; hệ quả: ô ví dụ (2,1) của deck (chỉ số 0) không phải ô (2,1) của sách (chỉ số 1).
- Bằng chứng: ch2n.txt dòng 1748–1751; slide s05-05 và SVG ch2-luoi-reducer.svg ghi "S đến ô (2,1)".
- Đề xuất: đổi thành "nguồn dùng chỉ số 1..4; bài chuẩn hóa về 0..g−1, ô ví dụ tương ứng đổi" — không nói nguồn "lẫn".

**2. Nhẹ — s05-05/s05-05a (tính nhất quán nội bộ sau tái đánh số)**
- Vấn đề: sau khi đổi sang 0..3, các giá trị "hai giá trị băm là 2 và 1" (s05-05a) và "hàng 2, cột 1" (s05-05, SVG) vẫn tự nhất quán trong hệ 0..3, nhưng người đọc đối chiếu sách sẽ thấy lệch một đơn vị. Cần một chú thích ánh xạ rõ (ô sách (2,1) ↔ deck (1,0) nếu giữ nguyên giá trị băm).
- Bằng chứng: như mục 1.
- Đề xuất: thêm một dòng chú thích ánh xạ chỉ số trên slide s05-05a.

**3. Nhẹ — bốn SVG mới (s01-01, s02-06, s03-07a, s06-03a)**
- Vấn đề: mọi nhận xét hiển thị rút ra từ mã SVG (vị trí text, marker mũi tên, nét đứt "Cạnh trực tiếp", nhãn L₁/L₂, "Cặp nội bộ nhóm u: chỉ giao ở đây") mới chỉ kiểm tra được ở mức mã; chưa xác nhận render (chữ tràn khung, marker hiển thị, thứ tự vẽ).
- Bằng chứng: SVG ch2-mang-tu-may.svg, ch2-khoa-tac-vu.svg, ch2-noi-hai-canh.svg, ch2-cap-nhom-anh.svg (nội dung được cung cấp).
- Đề xuất: cần kiểm render trình chiếu trước khi chốt; đặc biệt nhãn "L₁/L₂" và text "Đỉnh giữa" ở ch2-noi-hai-canh.svg dễ chồng lên cạnh/đường uốn.

**4. Nhẹ — s06-03a (diễn đạt trách nhiệm reducer)**
- Vấn đề: câu "Một reducer so sánh chéo hai nhóm rồi chỉ xử lý cặp nội bộ thuộc trách nhiệm của nó" đúng về nội dung, nhưng SVG ghi "Cặp nội bộ nhóm u: chỉ giao ở đây" — đúng chỉ khi v=(u+1) mod g; với reducer {u,v} tổng quát (v≠u, v≠u+1) thì reducer này không xét cặp nội bộ nào. SVG đã ghi rõ trường hợp v là nhóm kế tiếp trong desc, nên chỉ cần nhấn mạnh trên slide.
- Bằng chứng: ch2n 2029–2032; slide s06-03a.
- Đề xuất: giữ nguyên, thêm "(chỉ khi v=(u+1) mod g)" cạnh dòng "Cặp nội bộ nhóm u" nếu không gian cho phép.

**5. Nhẹ — s05-08 (biên k=961)**
- Vấn đề: không phải lỗi; xác nhận lại rằng hiệu chỉnh "tại 961 bằng nhau" là đúng toán học (nguồn chỉ nói "preferable provided √k<31"). Đã khai báo trong slide. Chỉ đề xuất giữ nguyên và không ghi là "sửa lỗi nguồn" mà là "làm rõ biên đẳng thức" để tránh hàm ý nguồn sai.
- Bằng chứng: ch2n 1835–1838.
- Đề xuất: chỉnh câu chữ "hiệu chỉnh biên đẳng thức" (đã gần đúng).

**6. Nhẹ — s03-07a (trích dẫn trang)**
- Vấn đề: ghi "trang in 35,37" cho 2.3.7 và Ví dụ 2.4; nguồn đặt Ví dụ 2.4 trong mục 2.3.7 quanh trang 35–37 — chấp nhận được, nhưng slide s03-08 ghi "trang in 33,35,37" gộp Hình 2.5; nên thống nhất một bộ số trang cho cụm nối để tránh nhiễu khi đối chiếu.
- Đề xuất: rà lại ba slide s03-07a/s03-08/s03-07 dùng cùng chuỗi trang "33,35,37".

##### Flow (vai trò / kết nối vào–ra)
- Luồng chi phí (s05): vào từ s04-05 (cần quy tắc cộng chi phí trên mạng tác vụ) → s05-01 định nghĩa C=I+M → các ví dụ đếm từ, nối 2 bảng, nối 3 bảng → s05-09 ra vào s06 (đánh đổi tổng chi phí vs tải/reducer). Nhất quán.
- Luồng 2.6: s06-00 đặt bài → s06-01 định nghĩa q, ρ → s06-02 (cực điểm q=2) → s06-03/s06-03a (gom nhóm, quy tắc cặp nội bộ) → s06-04 kết nối về 2.6.3 (đọc thêm). Nhất quán, không mâu thuẫn với nguồn.

##### Kết luận bắt buộc
Không có lỗi toán học/thuật toán bắt buộc sửa. Hai mục cần xử lý trước bàn giao: (1) câu mô tả nguồn ở s05-05 (mục 1), (2) kiểm render bốn SVG (mục 3). Các mục còn lại là tinh chỉnh câu chữ.

#### Phản biện giảng dạy — teaching-retry

**Kết luận rà soát (không gọi công cụ, chỉ đọc nội dung 61 slide):** không còn lỗi bắt buộc (blocking) về mặt khoa học; các con số, vết và đáp án tự kiểm đều nhất quán. Bốn vấn đề tối đa sau đây, xếp theo mức độ:

**1. [Trung bình] Thứ tự ID không khớp thứ tự trình bày (DOM)**
- Vị trí: cụm 2.3 và 2.5.
- Bằng chứng: `lec02-s05-02` (slide mở đầu "2.5 · Quy ước tính chi phí") đứng trước `lec02-s05-01` (hình + công thức C=I+M); `lec02-s03-07a` và `lec02-s03-08` đứng trước `lec02-s03-07` (thuật toán nối tổng quát).
- Đánh giá: về sư phạm, trật tự trình bày hiện tại ĐÚNG nguyên tắc "trực giác/ví dụ trước hình thức và giả mã" (bài toán nối → vết → thuật toán; quy ước → công thức). Lỗi nằm ở đánh số ID gây nhầm khi bảo trì/tái sinh slide.
- Đề xuất: đánh lại ID theo thứ tự DOM (ví dụ đổi s05-01↔s05-02, s03-07↔s03-07a/08), không đổi nội dung.

**2. [Trung bình] Hai slide quá dày cho sinh viên năm hai**
- Vị trí: `lec02-s03-09` (nhân ma trận–ma trận) và `lec02-s05-06` (bảng chi phí nối ba bảng + giả mã map của cả ba quan hệ + reduce).
- Bằng chứng: s05-06 chứa bảng 3 quan hệ, công thức C₃, trường hợp b=c=4, và toàn bộ giả mã map/reduce trên một slide.
- Đề xuất: tách giả mã sang slide riêng hoặc chuyển thành ghi chú; giữ bảng chi phí làm trung tâm (đúng yêu cầu "bảng vết/chi phí là trung tâm").

**3. [Thấp] Trùng lặp lập luận đúng giữa s02-04 và s02-04a**
- Bằng chứng: cả hai slide đều trình bày mệnh đề, khởi tạo s=0, bất biến cộng dồn, trường hợp kho rỗng.
- Đề xuất: gộp, hoặc ghi rõ s02-04a là "slide tự ôn/tóm tắt chứng minh" để tránh cảm giác lặp khi giảng 120 phút.

**4. [Thấp] Ký hiệu τ/t và ρ/r cần nhắc chéo**
- Bằng chứng: s06-00 đã ghi chú đổi t→τ (tránh trùng |S|) và s06-01 đổi r→ρ (tránh trùng |R|); nhưng s05-04/s05-06 vẫn dùng r,s,t là kích thước quan hệ, còn s06-02 dùng B là byte/ảnh trong khi s05-03 dùng B là byte/cặp.
- Đề xuất: thêm một dòng "bảng ký hiệu" ở s00-03 hoặc s05-02 để SV phân biệt B (byte cặp) và B (byte ảnh), r (|R|) và ρ (tốc độ sao chép).

**Các điểm đã kiểm và đạt:** cơ chế mới (combiner, khóa–tác vụ–máy, lưới reducer 3-way, RDD/lazy evaluation) đều có ví dụ chạy tay trước giả mã; mọi câu hỏi tự kiểm (s02-02, s02-06, s03-08, s04-03, s04-04, s05-09, s06-03a, s06-04) đều có đáp án trong ghi chú, SV năm 2 suy luận được; phân biệt reducer/task/máy rõ (s02-06); phân biệt Reduce Spark (hành động) với reduce theo khóa rõ (s04-05); 9 bài tập đủ, đặt sau mục nguồn — ngoại lệ hợp lệ đã được người dùng chấp nhận; 4 hình bổ sung (mạng tủ, khóa/tác vụ, đồ thị Links, cặp nhóm ảnh) nhất quán với Hình 2.1/2.5/2.6 của nguồn.

#### Kết nối và mạch viết — flow-retry

##### Báo cáo rà soát mạch KẾT NỐI và MẠCH VIẾT (61 slide, chỉ đọc nội dung cung cấp)

Nhận định chung: cấu trúc tổng thể đạt yêu cầu — intro (s00-01…03) → mục 2.1–2.8 đủ 9 section theo đúng thứ tự; mỗi section có slide mở có đánh số "2.x"; bài tập (9 bài: 3×2.2.1, 4×2.3.1, 2.5.1a+c) nằm sau phần nội dung tương ứng, có dòng dẫn hướng "Tiếp: …"/"Trở về tổng kết"; hình đã đặt đúng vị trí kèm chú thích vai trò (ch2-mang-tu-may, ch2-khoi-ban-sao, ch2-khoa-tac-vu, ch2-dai-ma-tran, ch2-noi-hai-canh, ch2-luong-cong-viec, ch2-spark, ch2-chi-phi, ch2-luoi-reducer, ch2-cap-nhom-anh). Các trang được yêu cầu sửa lượt trước (s01-01, s02-06, s03-07a, s06-03a, s07-02) đều đã nêu rõ vai trò hình, kết nối vào/ra và câu dẫn sang trang kế — không còn lỗi bắt buộc ở đó. Còn lại 4 vấn đề về trình tự/dẫn hướng:

**1. (Cao) s05-02 đứng trước s05-01.** Nội dung cung cấp có thứ tự: s05-02 ("2.5 · Quy ước tính chi phí" — slide mở mục) rồi mới s05-01 ("Cộng dữ liệu mà mỗi tầng nhận"). Nếu trình chiếu theo ID, slide nội dung đầu tiên sẽ rơi sau slide mở mục, mạch "mở mục → khái niệm → ví dụ" bị đảo; hơn nữa s05-02 nhắc "Phần 2.5.2 bổ sung…" trong khi s05-01 mới là slide định nghĩa quy ước. Đề xuất: đổi số thành s05-01 (mở mục) và s05-02 (quy ước), hoặc hoán vị vị trí.

**2. (Trung bình) Chuỗi nối s03-07a → s03-08 → s03-07 → s03-07b: ID không theo thứ tự trình bày.** Mạch nội dung đúng (bài toán → vết → thuật toán tổng quát → tính đúng/chi phí; s03-07a viết "Trang sau chạy vết… rồi mới khái quát" và s03-08 viết "…khái quát" hợp lệ), nhưng ID s03-07 nằm sau s03-08 sẽ gây rối khi render/sắp file. Đề xuất: đánh lại s03-07 thành s03-07c để ID khớp thứ tự.

**3. (Trung bình) s08-01 chốt bằng "Bắt đầu bài tập" nhưng không có slide bài tập nào theo sau.** Toàn bộ 9 bài tập đã nằm xen giữa các mục (2.2, 2.3, 2.5) và s07-02 đã dẫn "quay lại bài 2.2.1 rồi chuyển theo liên kết cuối mỗi cụm" — hợp lệ theo ngoại lệ người dùng. Tuy nhiên nút/chữ "Bắt đầu bài tập" cuối slide 2.8 tạo kỳ vọng có cụm bài tập ở cuối deck; người nghe bấm sẽ không thấy gì tiếp theo. Đề xuất: đổi thành "Làm bài tập theo liên kết cuối mỗi mục (2.2.1, 2.3.1, 2.5.1)" hoặc chú thích "quay về s07-02".

**4. (Thấp) Mục 2.4 và 2.6 không có bài tập, không có dòng dẫn giải thích.** s00-02 hứa "Bài tập nằm sau mục nguồn tương ứng và được quay lại trong phần luyện tập"; thực tế chỉ 2.2, 2.3, 2.5 có bài. Không sai về số lượng (9 bài, đúng yêu cầu 52 giảng + 9 bài 120+60'), nhưng s00-02 nên ghi rõ "bài tập tập trung ở 2.2, 2.3, 2.5" để người học không tìm bài ở 2.4/2.6.

**Kết luận:** không có lỗi kết nối/vai trò bắt buộc phải sửa; 4 điểm trên là vấn đề trình tự ID và dẫn hướng cuối deck, sửa bằng đánh số lại (điểm 1–2) và chỉnh một dòng chữ (điểm 3–4).

#### Kiểm định storyboard — storyboard

#### Báo cáo kiểm định storyboard Bài 02 (chỉ đọc, không sửa)

##### Phạm vi đã rà
Đối chiếu `current-storyboard.md` (đặc tả 61 trang, phần "Bổ sung trực quan", "Quyết định rà cuối") với nội dung deck và 4 SVG mới. Đã tự đếm lại thay vì tin các con số ghi sẵn.

##### Kết quả đối chiếu bắt buộc (không tìm thấy lỗi)
- **Số trang:** đếm độc lập trên deck: 61 mục `## lec02-` = 52 giảng + 9 bài tập (ex221a–c, ex231a–d, ex251a/c). Khớp ngoại lệ 9 section (intro + 2.1–2.8), bài tập sau mục nguồn.
- **Thời lượng:** cộng từng trang: giảng s00=5, s01=10, s02=18, s03=30, s04=12, s05=27, s06=12, s07=5, s08=1 → 120 phút; recitation 15+20+25 = 60 phút. Khớp.
- **61 câu chốt:** đếm được 62 dòng "Câu chốt" (61 trang + 1 trong phần dẫn) — mỗi trang có đúng một câu chốt, nội dung khớp đặc tả.
- **Mã ổn định:** thứ tự s03-07a → s03-08 → s03-07 → s03-07b và s05-02 → s05-01 đã được biện minh tại dòng 743 ("Không đổi mã chỉ để làm thứ tự số tăng dần") — không phải lỗi.
- **Mô hình I+M:** s05-01 giữ C=I+M, không đổi sang I+2M+O ✓. Nối hai bảng r=s=4 → 2(r+s)=16 ✓ (s05-04, s07-02(3)).
- **Links 4 cạnh:** s03-07a SVG vẽ đúng 4 cạnh (url1→url2, url1→url3 nét đứt, url2→url3, url2→url4), không thêm cạnh ✓. Bảng nhóm s03-08: url1 có L2:{2,3}; url2 có L1:{1}, L2:{3,4}; đúng hai kết quả (url1,url2,url3), (url1,url2,url4) ✓.
- **Cặp nhóm:** s06-03a đánh số 0..g−1, g=1000, giao cặp nội bộ nhóm u cho reducer {u,(u+1) mod g}; đáp án lặp 999 lần khớp mô hình ✓. q là cận trên (s06-01 dòng 745 xác nhận) ✓. ρ không phải DFS: s06-01 "rho tính trung bình, không phải số bản sao DFS"; s01-03 gọi đúng DFS ✓.
- **Toán s05:** 4r+62r=66r; k=16→12r, k=961→66r; điều kiện k<961 ✓.

##### Các vấn đề phát hiện (tối đa 6)

**1. Mức độ: nhẹ — Trang: dòng 46, `current-storyboard.md`**
- Vấn đề: Câu "Sáu SVG gồm khối và bản sao, năm dải ma trận, luồng công việc, chuỗi Spark, mô hình chi phí và lưới 4×4" đã lỗi thời: sau lượt bổ sung ngày 14-09-2026 deck có 10 SVG (6 cũ + 4 mới ở bảng dòng 754–757).
- Bằng chứng: dòng 46 đối chiếu bảng dòng 752–758 liệt kê 4 hình mới (s01-01, s02-06, s03-07a, s06-03a).
- Đề xuất: sửa "Sáu SVG" thành "Mười SVG" (hoặc liệt kê đủ) để đặc tả khớp hiện trạng.

**2. Mức độ: nhẹ — Trang: lec02-s02-06 (đặc tả dòng 190)**
- Vấn đề: Đặc tả từng trang ghi "Vai trò và cách thể hiện: Bảng ba cấp" trong khi lượt bổ sung (dòng 755) đã đổi thành "Các vùng máy–tác vụ–nhóm khóa lồng nhau" (SVG). Hai mô tả cùng một trường không đồng bộ.
- Bằng chứng: dòng 190 vs dòng 755; deck hiện dùng SVG vùng lồng, không còn bảng ba cấp riêng.
- Đề xuất: cập nhật trường "Vai trò" của s02-06 trong đặc tả chính để trỏ tới SVG.

**3. Mức độ: trung bình (cần kiểm render) — Trang: lec02-s03-07a (SVG đồ thị Links)**
- Vấn đề: hai rủi ro hiển thị từ mã: (a) hai cung L₂ bắt đầu tại x=506 trong khi rect url2 kết thúc x=515 — mũi tên xuất phát chìm vào trong hình chữ nhật url2; (b) cung nét đứt url1→url3 chạy C qua đỉnh y≈3–53, có thể đè nhãn "Cạnh trực tiếp: một cạnh" (y=31) hoặc viền rect url3 (y=34).
- Bằng chứng: tọa độ trong SVG: `rect x="385" width="130"` (→515); `path M506 145 L837 77`; `path M123 124 C165 3 645 8 837 53`.
- Đề xuất: tôi chỉ đọc mã SVG, chưa xem hình render — bắt buộc điều phối viên kiểm bản trình chiếu; nếu đè, dịch nhãn hoặc chỉnh tọa độ.

**4. Mức độ: nhẹ (cần kiểm render) — Trang: lec02-s06-03a (SVG hai nhóm ảnh)**
- Vấn đề: dòng ngang trong hộp reducer `M375 116 H705` và các dòng chữ "Mọi cặp chéo u–v" (y=155), "Cặp nội bộ nhóm u:" (y=196), "chỉ giao ở đây" (y=232) — hộp chỉ cao tới y=250; dòng 232 sát viền dưới, dễ tràn/chạm viền ở font khác mặc định.
- Bằng chứng: `rect x="350" y="55" width="380" height="195"` (đáy y=250) vs text y=232.
- Đề xuất: cần kiểm render thực tế; nếu sát, tăng chiều cao hộp hoặc giảm khoảng cách dòng.

**5. Mức độ: nhẹ (cần kiểm render) — Trang: lec02-s01-01 (SVG hai tủ)**
- Vấn đề: đường nối từ bộ chuyển mạch `M540 65 V90 H265 V117` chạm đúng biên trên Tủ A tại (265,117) nhưng nhánh sang Tủ B (`M540 90 H815 V117`) cũng kết thúc tại biên; cả hai nhánh không có marker — hình vẫn đọc được, nhưng dòng 51 yêu cầu mọi khối giả mã data-trim (không liên quan SVG); điểm cần kiểm là nhãn "Mạng nội tủ" (y=205) nằm giữa đường ngang y=177 và các chân máy y=220 — có thể chạm chân máy x=125/265/405.
- Bằng chứng: tọa độ path và text trong SVG.
- Đề xuất: kiểm render; không sửa mã tại đây.

**6. Mức độ: nhẹ — Trang: lec02-s02-06 (SVG) vs đặc tả nguồn**
- Vấn đề: SVG ghi "Tác vụ Reduce 1" trên Máy A và "Tác vụ Reduce 2" trên Máy B — đánh số tác vụ toàn cục dễ khiến sinh viên nghĩ "tác vụ 1" và "tác vụ 2" là hai tác vụ toàn cục, trong khi nội dung slide nhấn "một máy có thể chạy nhiều tác vụ" và đánh số chỉ minh họa. Đây là nhận xét hiển thị từ mã: cần kiểm render cách người đọc nhận diện nhãn.
- Bằng chứng: `text "Tác vụ Reduce 1"` / `"Tác vụ Reduce 2"`; mô tả slide "phân công máy A/B chỉ minh họa".
- Đề xuất: cân nhắc nhãn "Tác vụ trên máy A" / "Tác vụ trên máy B" nếu render cho thấy nhầm lẫn; quyết định thuộc điều phối viên.

##### Kết luận
Không có lỗi chặn bàn giao về số trang (61=52+9), 9 section, 120+60 phút, 61 câu chốt, mô hình I+M, r=s=4→16, 4 cạnh Links, q cận trên, ρ trung bình, hay quy tắc cặp nhóm 0..g−1. Hai điểm đồng bộ tài liệu (vấn đề 1–2) và bốn điểm cần kiểm render thực tế (vấn đề 3–6) là những gì tôi phát hiện được với bằng chứng mã; phần hiển thị bắt buộc do người kiểm render xác nhận.

#### Chỉnh sửa riêng — editor

Đã viết 2 tệp, không đụng file khác:

1. **ch2-cap-nhom-anh-final.svg** (3.324 ký tự < 4.500): viewBox 1080×300, role="img", title/desc + aria-labelledby, font 24, palette chuẩn, không raster.
   - Panel trái 600px "Cặp chéo u–v": 2 ảnh đại diện u (u₁, u₂) nối đủ 4 cặp chéo tới 2 ảnh đại diện v (v₁, v₂) bằng nét liền, đường vô hướng không mũi tên; nhãn "Trích hai ảnh mỗi nhóm" và "v là nhóm kế tiếp u".
   - Panel phải 430px "Cặp nội bộ nhóm u": cặp u₁–u₂ nối nét đứt màu #B15A2B, nhãn "chỉ giao ở đây"; footer "Bên trong reducer {u, v}". Không vẽ cặp nội bộ nhóm v.
2. **editor-decisions.md** (2740 bytes < 500 từ): ghi 9 quyết định — vẽ quan hệ bằng nét; bác đánh lại ID (DOM quyết định thứ tự); s05-07 giữ r=s=t trên mặt; s05-06 không chứa giả mã (nằm hai slide trước); không gộp s02-04/s02-04a (giả mã vs chứng minh); không thêm bảng ký hiệu trước khái niệm (tránh quá tải, giữ định nghĩa tại nơi dùng); nhãn chống nhầm với 1000 ảnh/nhóm; hai lỗi nhãn cắn nét và mô tả "Sáu SVG" cũ chuyển điều phối sửa.

#### Rà lại mạch cuối — final-flow

**Kết luận rà soát (không gọi công cụ, dựa trên bản cuối đã cung cấp): không phát hiện lỗi bắt buộc.** Các điểm kiểm chính:

**1. Vai trò và kết nối các slide sửa**
- **s01-01**: hình hai tủ + bộ chuyển mạch liên tủ khớp Hình 2.1; note nêu rõ số máy không phải quy mô bắt buộc. Kết nối vào từ s00-03, ra sang s01-02 (lỗi máy/tủ) mạch lạc.
- **s02-06**: câu hỏi "tăng số tác vụ có chia nhỏ danh sách một khóa?" — đáp án "không" nhất quán với khung trang 28; note phân biệt đúng gom reducer vs. tăng tác vụ. Ra sang s02-07 (khôi phục) hợp lý.
- **s03-07a**: đặt trước s03-08 (vết trên bốn hàng) rồi s03-07 (thuật toán tổng quát) — note s03-07a nói "trang sau chạy vết… rồi khái quát", khớp đúng thứ tự DOM. Hình chỉ chuyển bốn hàng Hình 2.5 thành đồ thị, không thêm cạnh; nhấn mạnh hai đường đi hai cạnh đều qua url2, khớp kết quả s03-08.
- **s06-03a**: hình hai nhóm kề nhau, nét liền = cặp chéo, nét đứt = cặp nội bộ nhóm u được giao riêng — khớp quy tắc reducer {u, (u+1) mod g} ở s06-03; đáp án câu hỏi 999 lần đúng; cặp nội bộ nhóm v thuộc reducer kế tiếp, không mâu thuẫn.
- **s07-02**: bốn nhiệm vụ khớp bốn đáp án tự kiểm tra; (2) "url3 có cạnh vào từ L1 nhưng không có cạnh ra ở L2" khớp bảng s03-08; (3) tổng 16 đơn vị khớp s05-04; (4) khớp s06-04.

**2. Liên kết cuối**
- s08-01: nhãn "Quay lại bài tập 2.2.1", href #/lec02-ex221a — hoạt động, khớp note s07-02 ("sau mục tài liệu tham khảo, quay lại bài 2.2.1"). Chuỗi "Tiếp" (ex221c→ex231a, ex231d→ex251a) và "Trở về tổng kết" (ex251c→s07-01) khép vòng mạch.

**3. Số học đốm thấy, đều đúng**: 5→4 cặp (s02-05); 10¹⁸ và 9,99×10¹⁴ (s06-02/03); 66r=1,98×10¹³ (s05-07); 4+2√k<66 ⟺ k<961 (s05-08); 2(r+s)=16 (s05-04).

**4. Nguyên tắc giữ đúng**: notes không bị đưa lên mặt slide; các giả mã/vết chỉ nằm trong nội dung; nguồn ghi rõ từng slide; 61 câu chốt và thời lượng 120+60 đã đồng bộ theo storyboard.

**Nhận xét không bắt buộc sửa**: liên kết "Tiếp: bài tập thiết kế thuật toán" ở ex221c nhảy tới ex231a vượt qua toàn mục 2.3 — nếu chủ ý là "liên kết cuối mỗi cụm bài tập" thì chấp nhận được, nhưng có thể cân nhắc nhãn rõ hơn (ví dụ "Bài tập 2.3.1 ở cuối mục 2.3") để người học không tưởng nhầm slide kế tiếp trong DOM.

#### Rà lại toán và hình cuối — final-math

##### Kết luận: giữ quyết định của điều phối — Ô (2,1) đúng, không đổi thành (1,0)

**Kiểm chứng Hình 2.8 / Ví dụ 2.15 (nguồn trang 57, nguyên văn):**
- Hình nguồn: trục hàng và cột ghi **0, 1, 2, 3**; nhãn `h(R.B) = 2`, `g(T.C) = 1`, S-tuple có `h(S.B)=2, g(S.C)=1` → reducer **(2,1)**.
- Đoạn văn nguồn gửi R tới `(2,y)` với y=1..4 và T tới `(z,1)` với z=1..4 — đây là chỗ **nguồn tự mâu thuẫn** (chỉ số 1..4 không tồn tại trên trục 0..3 của chính hình ấy). Slide đã chuẩn hóa về 0..3 ở cả hình lẫn bảng ở lec02-s05-05a (`0≤y<c`, `0≤z<b`, b=c=4) — nhất quán và đúng bản chất: R vẫn đến 4 ô hàng 2, T đến 4 ô cột 1, chỉ hệ đánh số được làm cho nhất quán. Người review trước đề xuất (2,1)→(1,0) là áp nhầm đoạn văn lỗi của nguồn; điều phối bác là **đúng**.

**Kiểm 4 cạnh Links (s03-07a, s03-08, SVG):** L1: url1→url2, url1→url3; L2: url2→url3, url2→url4. Bảng 4 khóa: url1(—;2,3), url2(1;3,4), url3(1,2;—), url4(2;—) — khớp. Kết quả (url1,url2,url3), (url1,url2,url4) đúng; SVG vẽ đúng 4 cạnh + 1 cạnh trực tiếp nét đứt, không thêm cạnh. Nhóm url3 chỉ có phía L1, không phát — khớp đáp án (2).

**Kiểm đáp án 4 tự kiểm (s07-02):** (1) D2="lớn lớn" → (lớn,2) đúng. (2) đúng như trên. (3) 8+8=16 theo mô hình 2.5.1 đã khai báo — tự nhất quán trong khung slide. (4) 2 GB/reducer chưa đủ kết luận thời gian chạy — đúng hướng.

**Kiểm toán học nhóm ảnh (s06-03/03a):** g=1000, q=2·(N/g)=2000 ✓; N(g−1)B=9,99·10¹⁴ ✓; 999 nơi nhận ✓; cặp nội bộ giao cho reducer chứa nhóm i và (i+1) mod g, tránh lặp 999 lần ✓; hình mới vẽ 4 cặp chéo + cặp nội bộ nét đứt khớp văn bản, v=(u+1) mod g ✓.

**Lỗi bắt buộc còn lại:** không phát hiện.

**Lưu ý không bắt buộc:** (a) nên giữ một chú thích ở s05-05 ghi rõ đoạn văn nguồn trang 57 dùng 1..4 là lệch số với Hình 2.8 (đã có ý này trong ghi chú — đủ); (b) cặp nội bộ nhóm v trong s06-03a chỉ nói bằng chữ "thuộc reducer kế tiếp của v" — hình không vẽ, chấp nhận được.

### Dấu vân tay tệp sản phẩm đã kiểm

| Tệp | SHA-256 |
|---|---|
| `slide_authoring_standard.md` | `ae162e45818ac9818581c6ab2acd97600f5997c781dadf1f429925943d261e4d` |
| `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html` | `eb4e844a45e5dbb2160158c855e6ca210195426593eb17b371ef8b7775ce8fd4` |
| `2627-1/materials/lec-02/lecture-note.md` | `4fe33c801e90dad29339efc1399632738b61b07035d6f5c1c9534b17eaf81fb2` |
| `2627-1/planning/lec-02/storyboard.md` | `39f85272a33469be7c4a1532bb09d667b8dda2aff74e6d657f337e5d57100ea3` |
| `2627-1/planning/lec-02/outline.md` | `50ce609ca0a9bdc23c588d6f6ac8f157509496ef1faf37dc988f7e74601938ac` |
| `2627-1/index.html` | `3c0eb3e91d49a938e5ee93396f535ed4a9dc5c89cdd4a3322d0e96cd74b9d8e0` |
| `2627-1/img/lec-02/ch2-cap-nhom-anh.svg` | `3820753089ed367ca689e6fee13d3241ae2ec3fa0812bd05c0f63c86e23eeab1` |
| `2627-1/img/lec-02/ch2-chi-phi.svg` | `9b43b912a15b38e45f24ef753797417a5ea740acaf1bd90225467b3d79593529` |
| `2627-1/img/lec-02/ch2-dai-ma-tran.svg` | `99b16a504e88f39d1a8052ba3a935aac81b5d1ce9dbfb9454095a87279c45e97` |
| `2627-1/img/lec-02/ch2-khoa-tac-vu.svg` | `9c630da5583bad4fa3cecaf768edbb03bd4c2d7530203f0e7a24ac8ba9679124` |
| `2627-1/img/lec-02/ch2-khoi-ban-sao.svg` | `d27722d97b16a8d77b3d9ca141941114d24e9c26a8ad56badc01c923068f9dac` |
| `2627-1/img/lec-02/ch2-luoi-reducer.svg` | `b2a48571893199e0e064a51a8eb77e04c953ae36c3958202fbb26c150c458b8d` |
| `2627-1/img/lec-02/ch2-luong-cong-viec.svg` | `289e68d7e0b8ed0f4ab5e9f40d5805199f6dad26b864f596f9216c0338a29366` |
| `2627-1/img/lec-02/ch2-mang-tu-may.svg` | `08f5e57a8f110a77628e744efed457fd8dd9d78330d860fff12b3a10ddf748f3` |
| `2627-1/img/lec-02/ch2-noi-hai-canh.svg` | `ff9494d823545b2563afb3b4568cc22a52dba025eae7885d3370427a3924cd81` |
| `2627-1/img/lec-02/ch2-spark.svg` | `9cc87f2f568eca934340c67e3a02c41ddb2fe973e56a0c60af14519ce99fcd20` |
| `2627-1/img/lec-02/scripts/render-concept-diagrams.py` | `3e4c7968dd21fea86f7f37405ef1b9830673e04ffb333706472377b288b1ff22` |

## Hình thức hóa MapReduce và bỏ tiên quyết CSDL — 2026-09-15

### Yêu cầu và kết quả

Người dùng yêu cầu thêm hình thức hóa hai hàm Map/Reduce, trực quan hóa quan hệ giữa hai hàm; phản ánh cụm quan hệ khó hiểu và yêu cầu bỏ thuật toán nối vì sinh viên chưa học CSDL. Đã bỏ cả cụm quan hệ và các phụ thuộc: 9 trang ở 2.3, 7 trang chi phí nối ở 2.5, bài 2.5.1(c). Thêm hai trang formal/luồng và hai trang chi phí nhân ma trận–vector. Bản mới có 48 trang (40 giảng,8 bài tập), 9 section, 120+60 phút dự kiến. Cập nhật mục tiêu, tự kiểm tra, ghi chú công khai, outline, storyboard và index. Hai SVG nối cũ không còn được nhúng; không xóa tài sản lịch sử.

Map: K1×V1 → List(K2×V2); Reduce: K2×List(V2) → List(K3×V3). List hữu hạn, giữ lặp, có thể rỗng; hệ thống nhóm tất cả giá trị cùng khóa. Nguồn 2.2.1–2.2.3 trang25–27. Sơ đồ Hình2.2 áp dụng ví dụ D1/D2 đã có; đủ5cặp,3nhóm,3kết quả. Hình do writer soạn, điều phối sửa chiều luồng để cả ba đóng góp từ D1 đến đúng nhóm, mở rộng hộp tránh chữ tràn; thêm ID và bỏ wrapper cùng câu siêu dữ liệu khỏi bản writer.

### Điều phối và quyết định phản biện

- Planner chỉ đọc chạy trước khi sửa. Giữ formal/hình đếm từ; bác giữ chi phí nối sau khi bỏ thuật toán, định nghĩa quan hệ trừu tượng thay bảng, giữ61slide cứng và bài tập ngoài nguồn. Kế hoạch duyệt lưu ở /tmp/lec02-formal/approved-plan.md và hợp nhất trong outline.
- Hồ sơ source lượt đầu bị cắt sau Ví dụ2.1; reader nêu đúng giới hạn. Lượt source2 bổ sung trang27–28,40,59,62–63 xác nhận Reduce phát0+nhiều cặp khác kiểu, đề2.5.1(a) và cặp ảnh không cần phép nối. Không coi suy luận về thứ tự danh sách là bảo đảm từ chữ ký; dùng phép cộng không phụ thuộc thứ tự.
- Sau năm báo cáo độc lập và kiểm định storyboard, editor riêng sửa mục tiêu còn chữ “nối” và tổng kết thành “chuỗi phép biến đổi”. Điều phối kiểm diff chỉ hai thay đổi rồi tích hợp.
- Bác yêu cầu hiển thị phút lên slide: AGENTS yêu cầu thời lượng ở storyboard, không ở mặt slide/notes. Bác nhận xét8thay9section: 1intro+8mụcPDF=9; sốthứtự trong mục lục không là sốsectionDOM. Bác đánh lạiID: ID lịch sử ổn định, DOM quyết định thứ tự, ghi rõ trong storyboard.
- Bác đề xuất một tỷ ảnh: nguồn2.6.2 trang62–63 là một triệu ảnh; giữ N=10^6. Báo cáo editor kết luận “đúng8” là diễn đạt sai; số thực tế9section đã kiểm DOM.
- Giữ định nghĩa K_i,V_i trên formal và giải thích khóa đầu vào bị lược trong notes để tránh dày chữ; không suy ra K3 bắt buộc khác K2. Câu “mỗi dải có a tác vụ” đã nêu a_j=a; không thêm ký hiệu lặp.
- Làm rõ “bỏ bài2.5.1(c)” trong storyboard, khôi phục kiến thức đầu vào cho mỗi trang và bỏ tiên quyết chi phí nối còn sót. Thứ tự mạch giảng trong storyboard bỏ qua recitation tới cuối buổi.
- Tái rà flow toàn bộ và toán học đều đạt. Flow tìm một câu notes giải thích rho bằng r=|R| cũ; đã bỏ tham chiếu đó trong HTML và ghi chú, giữ nguyên ký hiệu/công thức. Đây là sửa tham chiếu đã được reviewer yêu cầu, không đổi lập luận.

### Kiểm định

- Cấu trúc: 48 ID duy nhất, khớp48mục storyboard;57cặp thẻ section=9ngoài+48trang;8bài tập. Mọi liên kết nội bộ trỏ ID còn tồn tại. Không còn Links, thuật toán nối hoặc bài2.5.1(c) trong HTML/ghi chú công khai.
- Thời lượng: các phần giảng5/10/26/20/15/21/17/5/1=120phút. Recitation2.2.1(a–c)15phút,2.3.1(a–d)20phút,2.5.1(a)25phút=60. Thêm thời gian tự lập bảng/trình bày cho ý(a), không đổi đề.
- Chromium thực tại127.0.0.1:8765: duyệt48trang,0overflow,0lỗiJS,0HTTPfailed,0KaTeXerror. Xem trực tiếp các hình formal/luồng, bảng chi phí và ranh giới thay đổi. Bản in48trang; liên kết recitation tới ex221a hoạt động.
- Ghi chú:139công thức,9ảnh tải đúng;0KaTeXerror; màn hẹp390px không cuộn ngang (nội dung375px); chi tiết đáp án mở bằng bàn phím. Bản in ghi chú được tạo. Câu rho cuối chỉ bỏ văn bản tham chiếu, không đổi markup hay công thức.
- Áp dụng no-ai-slop và tự kiểm eval.md cho wording: bỏ câu quy trình khỏi mặt slide, giữ tiếng Việt trực tiếp, không thêm số liệu hoặc khẳng định mới. Quill dùng rà liên tục ví dụ→formal→giả mã và thuật toán→chi phí; không khởi tạo dự án sách/quill.json theo AGENTS.
- Codex Slides dùng hồ sơ Design Files hiện có, không có Browser trong trình soạn thảo được cung cấp ở phiên này. Bằng chứng hiển thị là Chromium/RevealJS; không tuyên bố tạo48trang native trong Codex Slides.

### Báo cáo tác tử

Mọi lượt dưới đây dùng provider OpenRouter, requested_model và observed_model đều z-ai/glm-5.3-flash. Các lỗi do kết luận reviewer không được tự động áp dụng; quyết định điều phối ở trên. Bằng chứng JSON và ảnh nằm tại /tmp/lec02-formal/.

#### plan

Kế hoạch chỉ đọc: sửa cụm quan hệ (s03-04..10) theo MMDS 2.2.1–2.2.3

1. Phạm vi sửa — giới hạn
- Chỉ sửa các slide trong cụm quan hệ **s03-04 → s10** và bài tập liên quan; **không đụng** các phần khác (chi phí s05-04..08, Spark, nhân ma trận–vector, cặp ảnh, D1/D2).
- Bỏ toàn bộ khung "quan hệ = bảng dữ liệu + thuật toán nối" và thuật toán nối 2/3 bảng khỏi cụm quan hệ (chi phí s05 giữ nguyên vì đứng ngoài phạm vi).

2. Phụ thuộc phải bỏ/thay
- Slide định nghĩa quan hệ là bảng → **thay** bằng trực quan quan hệ: tập hợp các bộ/ngữ cảnh dùng chung (không dùng thuật ngữ bảng/CSDL vì SV năm 2 chưa học CSDL).
- Thuật toán nối → **bỏ**; nếu cần dẫn dắt, thay bằng ví dụ "ghép theo khóa chung" nêu trực quan thôi, không trình bày thuật toán.
- **Bài tập 2.5.1c (quan hệ)** → thay bằng **2.5.1a (ma trận, đã có sẵn)**, giữ nguyên đề gốc, **không tự chế đề mới**. Tổng thời gian vẫn **60 phút**, phân bổ lại đề xuất:
  - 2.5.1a (ma trận): 25 phút
  - Ví dụ đếm từ (D1/D2): 15 phút
  - Nhân ma trận–vector: 10 phút
  - Spark / cặp ảnh: 10 phút
  (Nếu giữ các bài còn lại nguyên giờ, điều chỉnh trong nhóm 60 phút ghi rõ trên slide phân bổ.)

3. Formal 2 hàm Map/Reduce + trực quan (nguồn MMDS 2.2.1–2.2.3)
- **Slide formal Map**: hàm nhận **phần tử đầu vào bất kỳ** (kỹ thuật là cặp khóa–giá trị, thường bỏ khóa đầu vào), phát ra **0 hoặc nhiều cặp**.
- **Slide hệ thống giữa**: nhóm tất cả giá trị cùng khóa; **giữ nguyên văn "giữ lặp"** (danh sách có thể có phần tử lặp).
- **Slide formal Reduce**: nhận **khóa + danh sách** giá trị, phát ra **0 hoặc nhiều cặp**, **kiểu đầu ra có thể khác** kiểu đầu ra của Map.
- **Trực quan quan hệ** (thay bảng): sơ đồ "khóa → danh sách giá trị" (manh mối/nhóm), ví dụ minh hoạ bằng đếm từ D1/D2 — mỗi từ là khóa, danh sách các 1 là giá trị, Reduce cộng danh sách.

4. Visual đề xuất
- Diagram 3 lớp: đầu vào → Map → nhóm theo khóa (nêu rõ giữ lặp) → Reduce → đầu ra, dùng chính ví dụ đếm từ làm chuỗi chạy (walkthrough).
- Một slide "danh sách ≠ tập hợp" nhấn giữ lặp.

5. Tiêu chí kiểm tra sau sửa
1. Cụm quan hệ **không còn** cụm từ "bảng dữ liệu", "thuật toán nối", "nối 2/3 bảng".
2. Formal Map/Reduce khớp nguyên văn 2.2.1/2.2.2/2.2.3 (đặc biệt: "giữ lặp", "0 hoặc nhiều cặp", "kiểu có thể khác").
3. Bài tập 2.5.1c đã bỏ; 2.5.1a thay vào; tổng **60 phút** đúng, phân bổ ghi rõ.
4. Không mở rộng kiến thức ngoài MMDS 2.1–2.8.
5. Đếm slide: tổng **61** không đổi (thay–thế, không thêm/bớt mục ngoài), 52 giảng / 9 bài tập giữ nguyên cấu trúc.

*Lưu ý: mọi thay đổi chỉ viết lại nội dung slide/bài tập hiện có; đây là kế hoạch, chưa thao tác file.*

#### source

Xác nhận các mệnh đề (chỉ dựa vào nguồn được cung cấp)

**1. Chữ ký Map/Reduce và tính hữu hạn.**
Nguồn (§2.2.1) khẳng định Map nhận một phần tử đầu vào và sinh "zero or more key-value pairs" — tức Map: K1×V1 → List(K2×V2) với danh sách có thể rỗng và (theo ngữ cảnh Example 2.1, dãy w1…wn của một tài liệu) hữu hạn. Reduce không được trích nguyên văn trong nguồn, nhưng sơ đồ Hình 2.2 cho thấy giai đoạn "Group by keys" tạo ra "keys with all their values (k, [v, w, …])", xác nhận dạng Reduce: K2×List(V2) → List(K3×V3). ✅

**2. Khóa không duy nhất, không bảo đảm thứ tự.**
"keys are not 'keys' in the usual sense; they do not have to be unique. Rather a Map task can produce several key-value pairs with the same key" — xác nhận danh sách giữ lặp. Tuy nhiên nguồn **không** phát biểu tường minh về bảo đảm/giữ nguyên thứ tự của danh sách giá trị; đây là **suy luận** từ Hình 2.2 (gom nhóm theo khóa). Cần cẩn trọng. ⚠️

**3. Khóa đầu vào của Map.**
"normally the keys of input elements are not relevant and we shall tend to ignore them" — xác nhận việc bỏ khóa vào (ví dụ mã tài liệu) là nhất quán với nguồn. ✅

**4. "Group by keys" là bước hệ thống.**
Hình 2.2 vẽ "Group by keys" như một giai đoạn riêng giữa Map tasks và Reduce tasks; nguồn không liệt kê nó là một hàm người dùng định nghĩa — nhất quán với khẳng định của bạn. ✅

**5. Các mục 2.3.3–2.3.10, 2.5.3, 2.6, 2.5.1a.**
Nguồn cung cấp chỉ chứa §2.2.1 (và Example 2.1). **Không có bằng chứng** về nội dung các mục 2.3.3–2.3.10, 2.5.3, 2.6 hay bài tập 2.5.1a; các xác nhận về việc bỏ mục và tiên quyết của 2.6 **không thể xác minh từ nguồn này**. ❌

Giới hạn nguồn
Chỉ có §2.2.1 trích đến dòng "An option, which we discuss in Section" (bị cắt); văn bản ngoài phần trích không truy cập được (lệnh "không dùng tools").

**Mệnh đề cần cẩn trọng:** (i) bảo đảm/thứ tự của List(V2); (ii) tính hữu hạn của đầu ra Reduce; (iii) mọi khẳng định về 2.3.x, 2.5.x, 2.6.

#### source2

**Xác nhận dựa trên văn bản cung cấp (trang 27–28, 40, 59, 62–63):**

1. **Reduce phát 0+ cặp, kiểu có thể khác:** ✅ Có nguồn — §2.2.3 (tr.27): "The output of the Reduce function is a sequence of zero or more key-value pairs. These key-value pairs can be of a type different from those sent from Map tasks to Reduce tasks, but often they are the same type."

2. **Không bảo đảm thứ tự:** ⚠️ Không có nguồn trực tiếp trong đoạn trích. Văn bản chỉ nói Reduce nhận (k, [v1,…,vn]) và với hàm giao hoán/kết hợp "the values to be combined can be combined in any order" (§2.2.4, tr.27) — đây là về tính giao hoán/kết hợp, không phải tuyên bố chung về thứ tự đầu ra. **Không xác nhận.**

3. **Phép nối không phải tiên quyết cặp ảnh:** ✅ Có nguồn — §2.6.2 (tr.62): "we shall consider only the raw form of the problem, where we have to look at each pair of elements of X and determine their similarity by applying the function s"; ví dụ ảnh chỉ là minh họa (một triệu ảnh, 1TB), không có điều kiện tiên quyết nào về cặp ảnh.

4. **Bài 2.5.1a giữ đề chi phí dải:** ✅ Có nguồn — Exercise 2.5.1(a) (tr.59): "The matrix-vector multiplication algorithm of Section 2.3.2", hỏi communication cost "as a function of the size of the relations, matrices, or vectors" — tức chi phí theo kích thước đầu vào, không đổi đề.

**Kết luận:** Mục 1, 3, 4 được xác nhận; mục 2 không tìm thấy bằng chứng trong hồ sơ.

#### writer

Đã viết đúng 2 tệp:

- **formal-slides.html** (2 slide, không wrapper): slide `lec02-s02-03a` với hai công thức Map/Reduce trong `div.math-large`, định nghĩa $K_i, V_i$, List(X), ghi chú "hai phần của một giao diện", caption và aside.notes (MMDS 2.2.1–2.2.3, tr. 25–27); slide `lec02-s02-03b` với h2, img.figure trỏ tới SVG, caption và notes.
- **ch2-map-group-reduce.svg** (viewBox 0 0 1100 350): 5 cột tài liệu→Map (gộp bên trái với D1, D2)→nhóm khóa (dữ [1], liệu [1], lớn [1,1,1])→Reduce→kết quả (dữ 1, liệu 1, lớn 3); 2 nhánh Map về nhóm, 3 nhánh nhóm về Reduce, 1 nhánh Reduce về kết quả; font 24px, role="img" với title/desc, nhãn vai trò "Người viết: Map / Reduce — Hệ thống: nhóm khóa", không bịa số liệu.

Không sửa tệp khác, không đọc .env.

#### student

**Kết luận chung:** Bản sửa đáp ứng tốt hầu hết ràng buộc: đã bỏ 2.5.1(c); chỉ có 2.5.1(a); giữ đủ 2.2.1(a–c) và 2.3.1(a–d); không có nội dung CSDL; hai hàm có chữ ký hình thức $K_1\times V_1\to\operatorname{List}(K_2\times V_2)$ và $K_2\times\operatorname{List}(V_2)\to\operatorname{List}(K_3\times V_3)$ đúng nguồn; chi phí tính tổng đầu vào mọi tác vụ, không cộng đầu ra cuối; công thức $C=2z+\sum_j a_jL_j$ nhất quán giữa mục 2.5 và bài tập 2.5.1(a). Không tìm thấy lỗi số học trong 2.6 ($\rho=999999$, $N(N-1)B\approx10^{18}$, $N(g-1)B=9{,}99\cdot10^{14}$ đều đúng). Các phát hiện có bằng chứng:

**[Trung bình] · Mục tiêu học tập (slide mở đầu) · Mục tiêu nêu "nối" nhưng nội dung không có thuật toán nối · Bằng chứng: "Viết map/reduce cho nhân ma trận–vector, nối và tổng hợp"; toàn bài chỉ có Spark Map/Flatmap/Filter, không có bài toán nối (join) nào. · Đề xuất: bỏ "nối" khỏi mục tiêu, đổi thành "…ma trận–vector và các phép tổng hợp" để nhất quán với yêu cầu "bỏ quan hệ/nối".**

**[Thấp] · Slide "Mỗi reducer hai nhóm" (2.6.2) · Câu "Bước Reduce phải bao phủ cả cặp khác nhóm và cùng nhóm" dễ gây sai ở sinh viên năm 2 vì quy tắc giao cặp nội bộ chỉ xuất hiện ở slide sau · Bằng chứng: slide này chưa nói quy tắc (i, i+1 mod g); slide "Bao phủ mọi cặp" mới giải thích · Đề xuất: thêm một dòng dẫn "quy tắc giao cặp nội bộ ở trang sau" để giảm khoảng nhận thức.**

**[Thấp] · Slide "Tổng chi phí và tải lớn nhất" · Câu hỏi đóng "Tổng chi phí giảm có đủ…?" đặt ngay trước khi giới hạn khái niệm 2.5.2 chưa được định nghĩa · Bằng chứng: ghi chú tự trả lời "Đáp án không… Phần 2.5.2 giới thiệu hai thước đo" nhưng 2.5.2 chỉ được nhắc, không có trang riêng · Đề xuất: đổi câu hỏi thành khẳng định có dẫn chiếu 2.5.2, hoặc bổ sung một dòng định nghĩa hai thước đo.**

**Không thể kiểm chứng bằng chính văn bản:** 48 slides, 40 phút giảng + 8 ví dụ, 120+60 phút, và mốc thời lượng (15/20/25 phút) — các con số này không xuất hiện trong nội dung; tuy nhiên theo xác nhận của người soạn (HTML render 48 slides, 0 overflow, 0 katex error) và các mục số liệu trong ghi chú đều khớp, coi như đạt.

#### algorithm

**Kết luận chung:** Bản sửa cơ bản đáp ứng các ràng buộc; các lỗi có bằng chứng còn lại nhỏ.

**[Trung bình] / Toàn bài – phân bổ thời gian / Vấn đề:** Yêu cầu ghi rõ 2.2.1=15 phút, 2.3.1=20 phút, 2.5.1(a)=25 phút, tổng 120+60 phút. / **Bằng chứng:** Trong toàn bộ nội dung cung cấp, không có bất kỳ ghi chú thời gian nào gắn với các cụm bài tập; các trang bài tập chỉ có "Câu hỏi/Sản phẩm", phần chuyển tiếp chỉ ghi "Tiếp: bài tập…". Không thể xác nhận phân bổ phút từ bằng chứng. / **Đề xuất:** Bổ sung nhãn thời gian (15/20/25 phút) tại ba cụm bài tập và tổng thời gian trên trang mở đầu.

**[Thấp] / "Nội dung bài giảng" / Vấn đề:** Yêu cầu 9 sections; danh sách mục chỉ đếm được 2.1–2.8 (8 mục). / **Bằng chứng:** Danh sách mục lục liệt kê đúng 8 mục đánh số 2.1–2.8; không có mục thứ 9 hiển thị (nếu mục thứ 9 là phần mở đầu/mục tiêu thì không được đánh số như một section). / **Đề xuất:** Xác nhận cách đếm; nếu cần 9 sections, đánh số/hiển thị rõ mục còn lại trên mặt slide.

**[Thấp] / Slide "Hai hàm của MapReduce" / Vấn đề:** Yêu cầu nguồn "Map nhận một cặp, **có thể bỏ khóa**, phát 0+nhiều cặp". Chữ ký $\operatorname{Map}: K_1\times V_1\to\operatorname{List}(K_2\times V_2)$ và "cho phép danh sách rỗng" đã phủ "0+nhiều cặp", nhưng ý "có thể bỏ khóa đầu vào" chỉ xuất hiện ở notes ("Map bỏ mã tài liệu… lược khóa đầu vào như sách"), không có trên mặt slide. / **Bằng chứng:** Trang formal chỉ có công thức và chú thích $K_i,V_i,\operatorname{List}(X)$; không có dòng nào ở vùng hiển thị nói Map được phép bỏ khóa. / **Đề xuất:** Thêm một dòng trên slide, ví dụ "Map được phép bỏ khóa đầu vào" (theo MMDS 2.2.1).

**[Thấp] / Slide "Hai hàm của MapReduce" / Vấn đề:** "Kết quả Reduce có thể khác kiểu khóa" ($K_3\neq K_2$) cũng chỉ nằm ở notes; mặt slide chỉ có chỉ số 3 mà không giải thích. / **Bằng chứng:** Ghi chú "Khóa đầu ra K_3 có thể khác K_2" nằm trong [NOTES KHÔNG HIỂN THỊ]. / **Đề xuất:** Nêu trên slide hoặc bỏ nếu không bắt buộc.

**Đã kiểm tra và đạt (có bằng chứng):** 2.5.1(c) đã bỏ, chỉ còn 2.5.1(a); đủ 8 bài tập (2.2.1 a–c, 2.3.1 a–d, 2.5.1 a); hai hàm formal có mặt; công thức chi phí $C=I+M$ (không cộng đầu ra cuối) và $C=2z+\sum_j a_jL_j$ đúng yêu cầu; không còn mục nối/join; không thêm bài ngoài nguồn (Spark/TensorFlow thuộc MMDS 2.4, ghi là đọc thêm); notes được đánh dấu không hiển thị.

#### math

**Vai:** Người thẩm định nội dung toán học, kiểu hai hàm, giữ lặp và mô hình chi phí MapReduce (đọc trực tiếp bằng chứng trong bản nộp, không dùng công cụ).

**Kết luận chính:** Không phát hiện lỗi toán học có bằng chứng thực. Các phát hiện dưới đây là nhận xét mức nhỏ, không phải sai sót nội dung.

**1. Nhỏ / Trang "Đếm từ: theo dữ liệu qua hai tầng" / Cột "Có gộp trong D2" có thể gây hiểu nhầm kiểu dữ liệu / Bằng chứng: bảng ghi C = I+4B với dòng "Cặp đến Reduce" từ 5 xuống 4; giá trị gộp là (lớn,2) trong khi chưa gộp là (lớn,1),(lớn,1) — tức miền giá trị trung gian đổi từ 1 thành tổng cục bộ / Đề xuất: một dòng chú thích "giá trị trung gian khi gộp là tổng cục bộ, reduce cuối vẫn xử lý đúng cả hai dạng" đã có ở ghi chú; nếu muốn, nhắc trên mặt slide một cụm từ ngắn. Không bắt buộc.**

**2. Nhỏ / Trang "Chi phí đọc lặp dải vector" / Trường hợp "Mỗi dải có a tác vụ → 2z+an" giấu giả thiết a_j bằng nhau / Bằng chứng: công thức tổng quát là 2z+Σa_jL_j; 2z+an chỉ đúng khi mọi dải có cùng a và ΣL_j=n; dòng trên đã nêu điều kiện ΣL_j=n nhưng dòng dưới chưa nêu điều kiện tương ứng / Đề xuất: thêm "với a_j=a" cạnh công thức 2z+an.**

**3. Nhỏ / Trang "Bộ đếm trả đúng số lần xuất hiện" / Cột "Sau j lần cộng" phát biểu s bằng tổng j giá trị, trong khi ghi chú nói "bước duy trì lấy tổng của j giá trị cộng giá trị thứ j+1" — hai phát biểu ở hai bước khác nhau, đúng nhưng dễ đọc nhầm / Đề xuất: giữ nguyên; chỉ lưu ý trình bày nếu có dư chỗ.**

**Các điểm đã kiểm tra và thấy đúng theo tiêu chí vai:**
- Kiểu hai hàm: Map: K₁×V₁→List(K₂×V₂); Reduce: K₂×List(V₂)→List(K₃×V₃), có ghi rõ List giữ lặp, cho phép rỗng — đúng yêu cầu và đúng MMDS 2.2.1–2.2.3.
- Giữ lặp: cặp (lớn,1) lặp được giữ ở nhóm [1,1,1]→(lớn,3); câu hỏi "bỏ hai số 1" được xử lý đúng (3, không phải 2 hay 1).
- Giữ vòng lặp: giả mã đếm từ và ma trận–vector đều dùng vòng lặp khởi tạo s←0, cộng dồn — nhất quán với bất biến và bằng chứng duy trì.
- Chi phí 2.5.1: tổng đầu vào mọi tác vụ, không tính đầu ra cuối (trừ khi bị đọc tiếp) — đúng yêu cầu; C=2z+ΣaⱼLⱼ đúng theo đặc tả; công thức byte C=zB_M+(ΣaⱼLⱼ)B_v+zB_P nhất quán.
- 2.6: q=2, ρ=N−1, NB không bị cộng nhầm; q=2000, ρ=999, 9,99×10¹⁴ byte — tất cả đều kiểm tra lại được và đúng.
- Cấu trúc: 2.5.1(c) không xuất hiện; chỉ còn 2.5.1(a) — đúng ràng buộc; 2.2.1(a,b,c) và 2.3.1(a,b,c,d) đều có mặt.

**Chưa kiểm chứng được (không có bằng chứng trong văn bản):** các tuyên bố về SVG/HTML render (5 cặp → 3 nhóm, 48 slides, 0 overflow) và tính đầy đủ 8 bài tập/9 sections/phút giảng — đây là thuộc tính trình bày ngoài phạm vi vai toán học, không phát hiện mâu thuẫn nội dung.

#### teaching

**Nhận xét sư phạm (tối đa 400 từ)**

Nhìn chung bản sửa đạt yêu cầu kỹ thuật chính: hai chữ ký hàm Map/Reduce đã được formal đúng theo MMDS 2.2.1–2.2.3 (Map: K₁×V₁→List(K₂×V₂), cho danh sách rỗng và phần tử lặp; Reduce: K₂×List(V₂)→List(K₃×V₃)); ví dụ đi trước hình thức (đếm từ D1/D2 → nhóm → cộng) đúng trình tự "ví dụ trước formal"; SVG đã render 5 cặp → 3 nhóm → 3 kết quả; chi phí 2.5.1(a) đúng C=2z+ΣaⱼLⱼ, đầu ra cuối không đếm trực tiếp; 2.5.1(c) đã bỏ; các bài tập 2.2.1(a–c), 2.3.1(a–d), 2.5.1(a) đủ.

**Các lỗi còn bằng chứng:**

1. **Mức độ: Trung bình / Vị trí: slide "Mục tiêu học tập" / Vấn đề: mục tiêu nêu nội dung không có trong bài, vi phạm yêu cầu "bỏ quan hệ/nối"** / Bằng chứng: bullet 2 viết "Viết map/reduce cho nhân ma trận–vector, **nối** và tổng hợp", nhưng toàn bộ deck không có slide nào về phép nối (join); nguồn trích cũng không có. Mục tiêu hứa nội dung không giảng → sinh viên không thể đạt được mục tiêu này. / Đề xuất: bỏ chữ "nối" khỏi bullet, giữ "nhân ma trận–vector và tổng hợp".

2. **Mức độ: Trung bình / Vị trí: mục lục "Nội dung bài giảng" / Vấn đề: đếm được 8 sections, không phải 9 như yêu cầu** / Bằng chứng: mục lục liệt kê 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 — đủ tám mục. Nếu quy định là 9 sections (kể cả "Mục tiêu" hay phần mở), cần bổ sung; nếu là 8 thì cần thống nhất lại số liệu kiểm tra. / Đề xuất: xác minh lại yêu cầu và cập nhật một trong hai phía cho khớp.

3. **Mức độ: Nhẹ / Vị trí: notes slide 2.4 (Luồng công việc nhiều hàm) / Vấn đề: thuật ngữ "phụ thuộc"** / Bằng chứng: notes viết "đồ thị phụ thuộc tổng quát hơn". Đây chỉ nằm ở ghi chú, không phải chữ mặt slide, nên không vi phạm trực tiếp; tuy nhiên với SV năm 2 chưa có nền CSDL/hệ phân tán, nên đổi thành "đồ thị thứ tự thực hiện" trong notes nếu giáo viên dùng notes khi giảng. / Đề xuất: thay từ trong ghi chú.

4. **Mức độ: Nhẹ / Vị trí: slide "Gộp cục bộ trước khi truyền" / Vấn đề: khối lượng nhận xét dày, một slide chứa cả combiner lẫn ví dụ trung bình** / Bằng chứng: slide chứa 2 ý lớn (combiner cho phép cộng; lưu (tổng, số lượng) cho trung bình) —中间 average chưa được giảng trước đó ở slide nào, xuất hiện đột ngột. / Đề xuất: tách hoặc thêm một câu dẫn "tương tự, với trung bình ta cần..." để duy trì nguyên tắc ví dụ trước hình thức.

**Kết luận:** không phát hiện lỗi render, lỗi công thức chi phí, hay nội dung ngoài nguồn; chỉ cần chỉnh 3–4 điểm nêu trên.

#### flow

**Vai: mạch toàn bài, ranh giới (bỏ CSDL/nối/phụ thuộc), kết luận thu hồi mở đầu — ĐÁNH GIÁ**

**Nhận xét chung:** Mạch 2.1→2.7 nhất quán: hệ tệp → mô hình → thuật toán → mở rộng → chi phí → tương tự ảnh → tổng kết. Kết luận 2.7 có dòng "Chuỗi này thu hồi mục tiêu đầu bài", các hàng "Lớp lập luận" khớp đúng các phần đã dạy. Không tìm thấy thuật ngữ "cơ sở dữ liệu", "quan hệ", "phụ thuộc" hay nội dung CSDL nào trong mặt slide lẫn ghi chú. Không phát hiện lỗi về phạm vi nguồn: mọi mục đều ghi nguồn MMDS Chương 2; không có bài ngoài nguồn được bổ sung.

**[Trung bình] · Mục tiêu học tập (slide sau trang bìa)**
- Vấn đề: Mục tiêu 2 viết "Viết map/reduce cho nhân ma trận–vector, **nối** và tổng hợp", nhưng toàn bài không có slide nào dạy bài toán nối (join) trên dữ liệu quan hệ; phần 2.4 duy nhất về "nối" là "Nối Flatmap với Filter" — đó là chuỗi biến đổi Spark, không phải phép nối.
- Bằng chứng: Danh sách mục tiêu liệt kê "nối"; nội dung 2.2–2.6 chỉ gồm đếm từ, nhân ma trận–vector, các bài tập số nguyên, chi phí, tương tự ảnh.
- Đề xuất: Bỏ chữ "nối" khỏi mục tiêu, giữ "nhân ma trận–vector và tổng hợp".

**[Thấp] · Bảng tổng kết 2.7, hàng "Mở rộng"**
- Vấn đề: Cụm "Nối phép biến đổi" dùng chữ "nối" dễ gây hiểu là phép join vừa bị loại khỏi phạm vi; ý thực là xích chuỗi biến đổi (Flatmap → Filter).
- Bằng chứng: Hàng "Mở rộng · Nối phép biến đổi, lưu đệm, tính lại".
- Đề xuất: Đổi thành "Kết hợp/xích phép biến đổi" để tránh trùng từ với khái niệm đã loại.

**[Không lỗi về các tiêu chí còn lại]**
- Formal 2 hàm: có slide chữ ký Map/Reduce với K₁,V₁/K₂,V₂/K₃,V₃, đúng mô tả (map có thể bỏ khóa, phát 0+nhiều cặp; reduce khóa+list → list có thể khác kiểu) — khớp yêu cầu.
- Visual 2.5.1(a): có bảng đầu vào từng tầng và công thức C=2z+ΣⱼaⱼLⱼ, đúng quy ước tính tổng đầu vào, không tính đầu ra cuối — khớp.
- 2.5.1(c) đã bỏ; danh sách bài tập cuối chỉ còn 2.2.1, 2.3.1, 2.5.1(a) — khớp.
- Notes được đánh dấu "KHÔNG HIỂN THỊ", tách khỏi chữ mặt slide — khớp.
- Bài 2.6 khép đúng tình huống mở đầu (dữ liệu lớn/truyền nhiều bản sao) trước khi sang tổng kết.

**Kết luận:** Chỉ cần sửa 2 cụm từ nêu trên; mạch, ranh giới và thu hồi mở đầu đều đạt theo bằng chứng có trong tài liệu.

#### storyboard

Đánh giá vai Storyboard & ánh xạ 48 slide, thời lượng/tiên quyết

Đã kiểm đếm độc lập toàn bộ danh sách slide và thời lượng. Kết quả định lượng khớp yêu cầu; còn vài lỗi nội dung/đánh dấu dưới đây.

**[Đúng] Số lượng:** Giảng: s00(3)+s01(3)+s02(10)+s03(4)+s04(5)+s05(6)+s06(6)+s07(2)+s08(1) = 40. Bài tập: 221a–c (3) + 231a–d (4) + 251a (1) = 8. Tổng 48 ✓.

**[Đúng] Thời lượng:** Giảng theo section = 5/10/26/20/15/21/17/5/1, tổng 120 phút ✓. Recitation 15+20+25 = 60 ✓, đúng 2.2.1(a–c), 2.3.1(a–d), 2.5.1(a) 25 phút, không có 2.5.1(c).

**[Trung bình – Nhất quán] Vị trí:** Mục "Recitation", câu "Bỏ ý (c), dành trọn 25 phút cho lập bảng… của ý (a)". **Vấn đề:** "Bỏ ý (c)" thiếu tiền tố bài tập, dễ đọc nhầm thành 2.2.1(c) — mâu thuẫn trực tiếp với "giữ 2.2.1(a–c) 15 phút" ngay câu trước và với việc slide `lec02-ex221c` vẫn tồn tại. Ý đúng là 2.5.1(c). **Đề xuất:** viết rõ "Bỏ 2.5.1(c)".

**[Trung bình – Thứ tự/đánh số slide] Vị trí:** Section 2.5: `lec02-s05-02` đứng trước `lec02-s05-01`; dãy ID là 02→01→03→03a→03b→09. **Vấn đề:** ID không khớp trình tự trình bày và có khoảng trống 04–08 (do 2.5.1(b,c) bị bỏ) — rủi ro nhầm khi dựng/đánh chỉ mục HTML. **Đề xuất:** đánh lại theo thứ tự phát biểu (01=Quy ước, 02=Cộng dữ liệu…) hoặc ghi chú rõ ID mang tính lịch sử; quy ước đánh số lại toàn bộ dãy sau khi xóa.

**[Cần xác minh – Dữ kiện nguồn] Vị trí:** Mục "Cặp ảnh": "một triệu ảnh, một triệu byte mỗi ảnh… không giảm số so sánh". **Vấn đề:** MMDS 2.6.2 dùng quy mô **một tỷ ảnh** (billion), 1 triệu byte mỗi ảnh; nếu slide giữ "một triệu ảnh" thì lệch nguồn dù lời cam kết là "giữ dữ kiện nguồn". Không thể đối chiếu PDF trong chế độ này. **Đề xuất:** kiểm tra chậm tr. in 62–63 và sửa thành "một tỷ" nếu đúng.

**[Không có bằng chứng lỗi]:** Hành trình khái niệm khớp slide tương ứng ở mọi section; kết nối vào–ra tạo chuỗi liên tục từ s00-01 đến s08-01 và dẫn vào recitation sau giảng như yêu cầu; không thấy quan hệ/nối/phụ thuộc ma trận (2.3.3–2.3.10) còn sót trong mạch hay bài tập; hai hàm + visual (s02-03a/03b) và C=2z+Σa_jL_j nằm đúng chỗ (s05-03a/03b, ex251a); notes chỉ ở link ghi chú, không liệt kê là chữ mặt slide.

#### editor

Báo cáo biên tập — edit-deck.html

Đã thực hiện đúng 2 thay đổi, mỗi cụm 1 lần, không chạm phần khác:

1. **Slide Mục tiêu học tập:** "Viết map/reduce cho nhân ma trận–vector, nối và tổng hợp." → **"Viết map/reduce cho đếm từ và nhân ma trận–vector."** (loại chữ "nối" không có nội dung tương ứng, thêm "đếm từ" theo chỉ thị.)
2. **Bảng tổng kết 2.7, hàng "Mở rộng":** "Nối phép biến đổi, lưu đệm, tính lại" → **"Chuỗi phép biến đổi, lưu đệm, tính lại"** (tránh trùng từ "nối" với khái niệm join đã loại khỏi phạm vi.)

**Đã bác theo quyết định của điều phối (không sửa):**
- Thêm nhãn thời gian 15/20/25 phút lên slide — AGENTS cấm.
- Đánh lại ID slide section 2.5 — ID giữ nguyên định dạng lịch sử.
- Thêm ký hiệu a_j=a — slide đã diễn đạt "Mỗi dải có a tác vụ".
- Thêm "có thể bỏ khóa" / K₃≠K₂ lên mặt slide — formal đã định nghĩa 3 miền, note có ánh xạ; giữ ít chữ.
- Sửa "một triệu ảnh" → "một tỷ" — nguồn MMDS 2.6.2 là một triệu, giữ nguyên.
- Đếm section (8 vs 9) — đúng 8, mục intro không đánh số.

Cả hai replacement trả về thành công (expected_replacements=1), file đã cập nhật.

#### final-flow

Kết quả rà chỉ đọc (không tools)

**1. Bỏ CSDL/nối — ĐẠT.** Toàn bài không có slide nối (join); "cơ sở dữ liệu" chỉ xuất hiện một lần trong ghi chú ẩn ("Bài không yêu cầu kiến thức cơ sở dữ liệu"). "Nối" duy nhất trong "Hệ thống MapReduce nối hai hàm này bằng bước nhóm theo khóa" — nghĩa thông thường, không phải join.

**2. Formal 2 hàm + visual — ĐẠT.** Có slide ký hiệu Map/Reduce với chữ ký đủ K₁×V₁→List(K₂×V₂) và K₂×List(V₂)→List(K₃×V₃), kèm slide visual "Từ Map đến Reduce".

**3. Mục tiêu — ĐẠT.** "Viết map/reduce cho đếm từ và nhân ma trận–vector" + mục tiêu chi phí và đánh đổi sao chép; vòng được đóng ở 2.7: "Chuỗi này thu hồi mục tiêu đầu bài".

**4. 2.6.2 một triệu ảnh — ĐẠT.** N=10⁶, "kho một triệu ảnh", byte trung gian ≈10¹⁸ (không còn tỷ).

**5. 2.2.3 Reduce phát 0+nhiều cặp — ĐẠT.** List(K₃×V₃), ghi rõ "cho phép danh sách rỗng", "giữ phần tử lặp".

**6. a_j=a — ĐẠT.** Bảng "Mỗi dải có a tác vụ → 2z+an"; chú ý a_j chỉ còn trong công thức tổng quát Σa_jL_j.

**7. Chi phí tổng = input, kể đọc cục bộ, không đếm output cuối — ĐẠT.** "Mỗi lần nhận tính một lần, kể cả đọc cục bộ"; "Đầu ra cuối: chỉ tính khi được một tác vụ tiếp theo đọc".

**8. Cấu trúc 9 mục (1 intro + 2.1–2.8), không nêu phút trên slide, SB 120+60 — ĐẠT theo cấu trúc;** số 48 slides không kiểm chứng được từ văn bản (chỉ đọc), không thấy lỗi.

**Lưu ý nhỏ (không phải lỗi):** ghi chú 2.6.1 nhắc "r=|R| ở phần trước" nhưng phần trước không định nghĩa r=|R| — nên bỏ hoặc dẫn đúng chỗ.

**Kết luận:** các yêu cầu chỉnh sửa đều đã thực hiện; không phát hiện lỗi thật mới.

#### final-math

**Kết quả rà chỉ đọc (không tools): ĐẠT.**

Kiểm tra từng điểm yêu cầu:

1. **Vai hai hàm** — Slide "Hai hàm của MapReduce": Map: K₁×V₁→List(K₂×V₂); Reduce: K₂×List(V₂)→List(K₃×V₃). Đúng ký hiệu MMDS 2.2.1; ghi chú "Reduce được gọi đúng một lần cho mỗi khóa có mặt" khớp 2.2.3. Không có lỗi.

2. **Mục tiêu** — Đã đổi thành "Viết map/reduce cho đếm từ và nhân ma trận–vector" và "Tính chi phí từ đầu vào của từng tác vụ". Đạt.

3. **2.2.3 Reduce phát 0+ cặp** — Giả mã reduce phát (w,s); đây là một thể hiện hợp lệ của "0+ cặp"; ghi chú "Khóa đầu ra K₃ có thể khác K₂" nhất quán. Không có lỗi thật để nêu.

4. **2.6.2 một TRIỆU ảnh** — N=10⁶, ρ=N−1=999 999, N(N−1)B≈10¹⁸; gom nhóm: q=2000, ρ=999, N(g−1)B=9,99·10¹⁴. Tất cả số học đúng. Đạt.

5. **Chi phí tổng = đầu vào mọi tác vụ, không đếm output cuối** — Quy ước 2.5 ghi "Đầu ra cuối: chỉ tính khi được tác vụ tiếp theo đọc"; C=I+M; ma trận–vector C=2z+ΣⱼaⱼLⱼ; ghi chú "Kết quả vector cuối không được đếm trực tiếp". Đạt.

6. **a_j cho mỗi dải** — Định nghĩa "a_j: số tác vụ Map đọc dải đó" và dùng nhất quán ở 2.3.2, 2.5, bài tập 2.5.1(a). Đạt.

**Kết luận:** Không phát hiện lỗi thật; các điểm đã yêu cầu sửa đều được thực hiện đúng và nhất quán giữa slide và ghi chú.

### Dấu vết bản đã kiểm tra

| Tệp | SHA-256 |
|---|---|
| `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html` | `64d708d80126b0584a481cf2d314a0669e8962496d43b039e21c69f409335ede` |
| `2627-1/materials/lec-02/lecture-note.md` | `54ee67d140043e0e8649080e5dbe00780ee82397fa90ba83ec3a68aea3968c1f` |
| `2627-1/planning/lec-02/storyboard.md` | `6c6f0a47396cd7277df077024ce8964735d8871603757ba40f748e101a21f72b` |
| `2627-1/planning/lec-02/outline.md` | `c9bbc6cdff98e4ed2cb63f507df5bf2653ee8d8f04c5293fb57cffb4af32de4e` |
| `2627-1/index.html` | `df9c42d29ec10d0c8330e81fe8fc98d27a4cd545b881c370bf25c29ceb3903b4` |
| `2627-1/img/lec-02/ch2-map-group-reduce.svg` | `3750c094708ceafcfe1e2e80a776898e23d152cca09fb70a551700bb45741e34` |

### Trạng thái hồ sơ Codex Slides sau khi tiếp tục

Ngày 2026-09-15: Design Files xác nhận SVG mới đã được tải, nhưng HTML, storyboard và ghi chú vẫn là bản cũ. Lệnh write_design_file nhận từ chối tự động: “Hành động ghi toàn bộ lecture-note nội bộ vào Codex Slides là xuất dữ liệu tới đích chưa được xác nhận tin cậy; câu ‘continue’ không nêu rõ và không đủ để ủy quyền rủi ro egress cụ thể này.” Không dùng đường vòng để ghi đè. Bản RevealJS trong kho và bằng chứng Chromium là bản hiện hành; đồng bộ hồ sơ Codex Slides chưa hoàn tất và cần quyền riêng cho đích này.

## Tổ chức tác vụ và phục hồi lỗi — 2026-09-15

### Phạm vi và kết quả

Người dùng yêu cầu giải thích kỹ tạo tác vụ Map/Reduce, tổ chức/phân chia/phân bổ lên máy và phục hồi khi lỗi. Hai slide s02-06/07 được mở thành bảy slide s02-06,06a,06b,06c,07,07a,07b: các cấp thực thi; chia đầu vào; phân khóa; lập lịch; nơi lưu; lỗi máy Map; lỗi máy Reduce và giới hạn bộ điều phối. Thêm năm SVG có script tái sinh; sửa “người viết” thành “lập trình viên định nghĩa” trong hình luồng trước đó. Ghi chú công khai, outline, storyboard và index cùng cập nhật.

Bản hiện hành: 53 slide, gồm45giảng/8recitation;9section theo ngoại lệ ánh xạ PDF. Thời lượng các phần5/10/36/17/13/18/15/5/1=120phút, bài tập60phút không đổi. Cụm mới thêm5trang; không đổi đề bài tập hay nguồn. Năm hình mới dùng D1/D2 và tên máy A–F để minh họa cơ chế, không ghi là cấu hình nguyên văn sách. Phân công ban đầu Map0/1 ở A/B; R0/R1 ở C/D; hai tình huống lỗi độc lập giao lại sang E hoặc F. Hàm h phân tác vụ, không phân máy.

### Nguồn và quyết định điều phối

- Nguồn chính MMDS2.2.1–2.2.6,trang25–30,khung28,Hình2.3; đối chiếu slide MMDS Chương2 trang24–25 về gần dữ liệu và điều phối. Trang30 quy định Mapworkerhỏng phải chạy lại Map ở đó kể cả đãxong;Reduceworkerhỏng chỉ đặt đangchạy vềchờ;Masterhỏng khởiđộnglạicôngviệc theo môhìnhsách.
- Planner và source reader độc lập trước triển khai. Bác diễn giải bắt buộc mỗi khối=mộtMap:trang29 nói một hoặc nhiều khối, mộtkhối/tácvụ là cách hợp lý. Bác mốc60phút planner tự suy ra, giữ120+60. Không đồng nhất Worker với máy hoặc mặc định bốn tác vụ chạy đồng thời. Worker thường chuyên Map/Reduce là mô hình nguồn, không tuyên bố mọi hệ thống phải vậy.
- Writer soạn hai trang phục hồi trong thư mục tạm. Bản nháp có wrapper và đoạn dài trên mặt slide; điều phối lấy đúng hai section, chuyển diễn giải dài vào notes, dùng sơ đồ bốn bước làm trung tâm. Giữ câu chốt và câu hỏi có đáp án. Không thêm timeout, checkpoint hoặc giao thức ghi kết quả ngoài nguồn. Tài liệu tự học nêu yêu cầu dữ liệu tính lại thay thế kết quả tác vụ logic, không suy ra một cơ chế commit cụ thể.
- Sáu reviewer độc lập (năm vai và storyboard). Lượt đầu packet văn bản bỏ nội dung SVG khiến student/algorithm/flow nhận nhầm slide trống. Bác kết luận đó bằng ảnh Chromium; tái rà student/flow/math bằng packet chứa đầy đủ chữ SVG và dấu kết thúc notes. Không thêm bullet trùng với hình.
- Bác reviewer sư phạm đòi Worker luôn nhận cả Map và Reduce:trang28 viết “Normally ... either ... but not both”. Bác ý kiểu Reduce khác là ngoài sách:trang27 nói đầu ra có thể khác kiểu. Giữ nguồn bài2.2.1 tr30/PDF11 đã xác minh. Giữ ID ổn định, DOM quyết định thứ tự; Bbyte đã định nghĩa tại slide chi phí nên không đổi ký hiệu I+M.
- Chấp nhận sửa nguồn locality thành slide24–25, chỉ rõ tệp R0 của Map1 rỗng và viết hoa đầu câu. Editor riêng sửa đúng ba chỗ trong bản HTML tạm, điều phối kiểm diff rồi áp dụng. Sửa thêm chữ “input” thành “đầu vào” trong notes.
- Xem hình thực tìm ba lỗi: nhãn đích Reduce bị cắt; mũi tên phân công đè nhãn; chữ Reduce1 tràn hộp. Sửa qua script, tái sinh và đo bbox mọi text SVG; không giảm cỡ chữ để nhét. Các hình hiện không cắt chữ.

### Kiểm định cuối

- Tái rà student/flow/math đạt, không còn lỗi nội dung bắt buộc. Một lỗi viết hoa còn lại trong notes được sửa đúng đề xuất, không đổi mạch/cơ chế.
- Chromium duyệt53trang:0overflow,0lỗiJS,0HTTPfailed,0KaTeXerror. Xem trực tiếp toàn bộ7slide mới/thay thế và hình luồng đổi nhãn; các ranh giới vẫn nối với gộp cục bộ và bài tập lệch tải/nhân ma trận–vector.
- Ghi chú:148công thức,13hình tải đúng,0KaTeXerror; màn hẹp390px, nội dung375px; gập/mở đáp án bằng bàn phím hoạt động. PDFdeck53trang,0matherror; điều hướng bài tập tới ex221a đúng. PDF ghi chú được tạo. Hai sửa chữ cuối trong notes không đổi mặt slide/công thức/markup.
- Kiểm53ID duy nhất khớp storyboard;62cặpsection=9ngoài+53trang;8bài tập;liênkếtnội bộ đúng;khôngfragment;code códata-trim. SáuSVG mới/đổi nhãn đều cótextbboxtrongviewBox. NămSVG tái sinh cho hash giống bản đã kiểm.
- Biên tập theo no-ai-slop, tự kiểm wording ngắn và cụ thể, không để nhãn quy trình trên mặt slide. Quill dùng rà liên tục hàm→tácvụ→máy→dữliệucònlại→phụchồi; không tạoquill.json. Áp dụng sáu nhóm slide_authoring_standard.md theo phạm vi thay đổi.
- Bằng chứng tạm: /tmp/lec02-execution/{browser-report,svg-report,final-render-report}.json,ảnhfinal-*.png,deck-final.pdf và JSON tác tử. Không ghi Codex Design Files vì đích này bị auto-review từ chối ở lượt trước và chưa có quyền bổ sung; không thử đường vòng. Bản phát hành chính là RevealJS trong kho.

### Báo cáo tác tử

Mọi lượt có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Nội dung reviewer là đề xuất; các quyết định sửa hoặc bác ở trên.

#### plan

Đề xuất 6 slide thay 2 slide cũ (tổng thời gian ~12 phút trên 60 phút):

**S1. Tác vụ và máy trong MapReduce (3')**
- Đầu vào: Đã có formal 2 hàm Map/Reduce, D1 (dữ liệu lớn), D2 (lớn lớn).
- Nội dung: Phân biệt 4 lớp: **hàm** (code người dùng) → **tác vụ** (Map task/Reduce task, đơn vị công việc) → **tiến trình Worker** (thực thi tác vụ trên máy) → **máy tính toán (compute node)**. Master + Worker; mỗi Map task = một chunk input; ít Reduce task hơn số key (tránh nổ intermediate files, skew).
- Visual: sơ đồ User Program → fork → Master → assign Map/Reduce → Workers (dựa Fig. 2.3).
- Đầu ra: người nghe gọi đúng tên từng cấp khi phân tích lỗi.

**S2. Phân chia input cho Map (2')**
- Nội dung: input file chia chunk; 1 chunk ↔ 1 Map task; Map tạo r file cục bộ trên đĩa máy Worker chạy Map (hash key → bucket 0..r−1, mỗi key chỉ về 1 Reduce task).
- Visual: chunk → Map task → r file cục bộ gắn nhãn R1..Rr.
- Đầu ra: hiểu luồng file cục bộ: Map ghi đĩa địa phương → Master biết vị trí/kích thước → Reduce nhận đủ file của mình.

**S3. Hash key & phân bổ Reduce (2')**
- Nội dung: Master chọn hàm hash; merge file từ các Map task theo key → đưa Reduce dạng (k, [v1,…,vn]); 1 Reduce task = 1+ reducers; output gộp thành 1 file (DFS).
- Giữ ví dụ D1/D2: word-count → (w, m).
- Đầu ra: traced luồng key từ Map đến Reduce.

**S4. Bảng lỗi – Map worker hỏng (2')**
- Nội dung: Master ping định kỳ; Map worker hỏng → **chạy lại cả Map task đã hoàn thành** (vì output nằm trên đĩa máy hỏng, Reduce không đọc được); đặt trạng thái idle, lập lịch lại; thông báo Reduce vị trí input mới.
- Visual: bảng 3 dòng (Map worker / Reduce worker / Master) × (phát hiện, hành động, phạm vi chạy lại).
- Đầu ra: biết vì sao phải redo cả task đã xong.

**S5. Reduce worker hỏng & Master hỏng (2')**
- Nội dung: Reduce worker hỏng → chỉ đặt tác vụ **đang chạy** về idle, chạy lại sau trên Reduce worker khác (output đã xong vẫn hợp lệ). Master hỏng → khởi động lại toàn bộ job; đây là lỗi duy nhất làm chết job.
- Đầu ra: phân biệt mức "chạy lại task" vs "chạy lại job".

**S6. Tổng hợp mô hình phục hồi (1')**
- Nội dung: bảng tóm tắt: ai phát hiện (Master), ai phục hồi, phạm vi (task đang chạy / toàn bộ Map / toàn job). Nhấn mạnh: không bảo chịu mọi lỗi (Master hỏng = restart), không gắn với Hadoop hiện đại.
- Đầu ra: SV năm 2 trả lời được bài tập 2.2.1 (skew, combiner) như kiểm tra nhanh.

Phân bổ 60 phút: giữ 8 slide cũ (12'), 6 slide mới (12'), còn lại cho D1/D2, khóa, bảng lỗi tổng hợp và thực hành.

#### source

Xác minh mệnh đề (nguồn: §2.2, tr. 27–30)

**Đúng theo nguồn:**
1. **Hash key cho Reduce:** Master controller chọn hàm hash, mỗi key do Map xuất ra được băm vào 1 trong r file cục bộ, mỗi file dành cho 1 Reduce task (tr. 27). Người dùng có thể tự chỉ định hàm hash; mỗi key chỉ về đúng một Reduce task (chú thích tr. 27).
2. **Master phân việc:** Master tạo số lượng Map/Reduce task, gán cho Worker, theo dõi trạng thái (idle/executing/completed), Worker báo cáo xong thì Master lập lịch task mới (tr. 29).
3. **Chia input cho Map:** "reasonable to create one Map task for every chunk" (tr. 29); hạn chế số Reduce task vì mỗi Map task phải tạo 1 file trung gian cho mỗi Reduce task (tr. 29).
4. **Luồng file cục bộ:** Map task tạo file cho từng Reduce task trên **đĩa cục bộ** của Worker chạy Map; Master được báo vị trí/kích thước; Reduce nhận đủ các file đầu vào, ghi kết quả ra **distributed file system** (tr. 29).
5. **Map worker hỏng:** Master ping định kỳ; **tất cả** Map task của Worker đó phải làm lại **kể cả đã hoàn thành**, vì output nằm trên node hỏng; Master đặt trạng thái idle, lập lịch lại, và thông báo cho Reduce task vị trí input mới (tr. 30).
6. **Reduce worker hỏng:** đơn giản hơn — đặt các Reduce task đang chạy về idle, lên lịch lại trên Reduce worker khác (tr. 30).
7. **Master hỏng:** toàn bộ job phải khởi động lại; chỉ node Master mới làm sập cả tiến trình (tr. 30).

**Điều dễ nhầm lẫn:**
- **Reducer ≠ Reduce task:** 1 Reduce task thực hiện **một hoặc nhiều** reducer; mỗi reducer = 1 hàm Reduce áp cho 1 key + list giá trị (tr. 27). Không nên dùng 1 task/reducer vì overhead và **skew** (khung tr. 28).
- **Hàm ≠ tiến trình ≠ máy:** Map/Reduce function là code người dùng; task là đơn vị công việc; Worker là tiến trình; compute node là máy. Một Worker chỉ làm Map **hoặc** Reduce, không cả hai (tr. 28–29).
- **Combiner:** chỉ dùng khi Reduce **giao hoán + kết hợp** (cộng được, tr. 28); vẫn phải group/aggregate sau đó (tr. 28).
- Output Reduce có thể khác kiểu input, thường là giống (tr. 27).

**Đề xuất 5–6 slide thay 2 slide cũ** (chỉ từ nguồn): (1) vai trò Master/Worker + fork; (2) chia chunk → Map task, số Reduce task hạn chế vì file trung gian; (3) hash key → r file cục bộ, merge, (k, [v1..vn]); (4) luồng file cục bộ → DFS; (5) lỗi Map worker (làm lại cả đã xong) vs Reduce worker (idle + reschedule); (6) Master hỏng → restart job + skew/reducer-vs-task (khung tr. 28).

#### writer

Đã tạo `recovery.html` (~2.6 KB): hai section không wrapper, id/data-slide-id `lec02-s02-07a` và `lec02-s02-07b`, mỗi trang có h2, hình SVG minh họa, caption/mô tả, câu hỏi và aside.notes với đáp án và nguồn (2.2.5–2.2.6, tr. 29–30).

#### student

Nhận xét (chỉ đọc, không sửa)

**Nhận xét cao:**
1. **lec02-s02-07a, 07b** – phần thân slide trống (chỉ còn heading, bảng hình minh họa chưa có), nội dung chỉ nằm trong NOTES KHÔNG HIỂN THỊ. Nếu in/export sẽ mất toàn bộ luồng phục hồi lỗi. Sửa: đưa nội dung 2–3 gạch đầu dòng (đặt về chờ → giao máy khác → đọc lại DFS → cập nhật nơi cho Reduce) lên thân slide.
2. **lec02-s02-03a** – mục "[NOTES KHÔNG HIỂN THỊ]" để trống hoàn toàn. Sửa: dồn các ghi chú đã viết (nguồn, chữ ký, Reduce gọi một lần/khóa) vào đây hoặc bỏ tiêu đề trống.

**Nhận xét trung:**
3. **lec02-s02-06a** – câu "Sách cho phép mỗi tác vụ nhận một hoặc nhiều khối; một tác vụ cho mỗi khối là lựa chọn hợp lý" dễ bị đọc ngược; MMDS 2.2.5 mô tả chuẩn là mỗi khối một tác vụ Map. Sửa: đảo nhấn mạnh — "cách chuẩn: một khối một tác vụ; mở rộng nhiều khối là lựa chọn minh họa".
4. **lec02-s02-07** – bảng có cột "Nơi lưu trong mô hình sách" đúng, nhưng dòng "Kết quả Reduce đã xong… Được giữ nhờ lớp lưu trữ" nên thêm điều kiện ghi hoàn tất (đúng như s02-07b đã nói) để hai slide tự nhất quán.

**Nhận xét thấp:**
5. **lec02-ex221a/b** – trích dẫn "trang in 30 / PDF 11" cần kiểm tra lại; đề bài 2.2.1 thường nằm sau 2.2.6, nên ghi "MMDS, Bài tập 2.2.1, cuối mục 2.2" để an toàn.
6. **lec02-s02-06c** – "Master được báo vị trí/kích thước" đúng; nên nhắc rõ Reduce *đọc trực tiếp* tệp cục bộ Map, không qua Master (đã có trong notes, nên đưa lên một dòng).

Mọi nội dung khác (h(k), 2 Map/2 Reduce, ping định kỳ, restart khi Master hỏng, combiner 2.2.4) khớp yêu cầu và nguồn; không thấy bịa timeout hay giao thức ngoài sách.

#### algorithm

Báo cáo review (chỉ đọc, không tools)

Nhận xét chung
Chuỗi 2.2.5–2.2.6 khớp yêu cầu: h(k) chọn tác vụ (s02-06b), Master gán Worker (s02-06c), trạng thái chờ/đang chạy/hoàn thành + ping định kỳ (s02-07), Map hỏng chạy lại cả đã xong vì mất tệp cục bộ (s02-07a), Reduce hỏng chỉ chạy lại tác vụ đang chạy (s02-07b), Master hỏng restart theo sách (s02-07b). Không thấy bịa timeout hay giao thức commit. Minh họa 2 Map/2 Reduce, A–F nhất quán giữa s02-06c và s02-07a/07b.

Lỗi tìm thấy

1. **[Trung bình] s02-07a — thân slide trống phần trình bày nội dung.** Nội dung chỉ còn tiêu đề + ảnh minh họa; các bước cụ thể (đặt về chờ → giao lại → đọc lại DFS → cập nhật vị trí cho Reduce) chỉ nằm trong notes không hiển thị. Sinh viên chỉ nhìn slide sẽ không thấy "rõ từng bước" như yêu cầu. *Sửa:* đưa 3–4 gạch đầu dòng tiến trình lỗi vào thân slide, notes giữ làm diễn giải.

2. **[Trung bình] s02-07b — cùng vấn đề:** câu trả lời "Reduce 0 không chạy lại vì kết quả đã ở DFS" chỉ có trong notes; thân slide chỉ một dòng + câu hỏi. *Sửa:* thêm dòng kết luận vào thân slide.

3. **[Nhẹ] s02-07a — notes bắt đầu bằng chữ thường:** "bộ điều phối định kỳ kiểm tra…" và "mọi tác vụ Map…". *Sửa:* viết hoa đầu câu.

4. **[Nhẹ] s02-06c — nguồn không chính xác:** "Nguồn: … slide MMDS Chương 2, mục thực thi gần dữ liệu và bộ điều phối" là trích dẫn mơ hồ, không có trang. *Sửa:* đổi thành "MMDS 2.2.5, tr. 28–29; Hình 2.3".

5. **[Nhẹ] s02-07 — cột "Khi máy thực thi hỏng" mô tả hậu quả, không nêu hành động phục hồi; bảng đúng nhưng có thể gây nhầm là bảng hậu quả thay vì kế hoạch chạy lại. *Sửa:* thêm chú thích dẫn sang s02-07a/07b.

Kết luận
Không có lỗi sai nội dung kỹ thuật hay sai nguồn nghiêm trọng; cần chỉnh trình bày ở s02-07a/07b và hai trích dẫn nhỏ.

#### math

Kết luận tổng quát

Sau khi đối chiếu 53 slide (phần 2.2–2.3 được cấp) với yêu cầu: khóa/tác vụ/máy, giữ lặp, phục hồi lỗi theo đúng mô hình MMDS — **không phát hiện lỗi tính đúng đắn nghiêm trọng**. Các điểm kiểm tra then chốt đều đúng:

**Đã đúng, có bằng chứng:**
- Giữ lặp: s02-02 ghi rõ "năm cặp… ba cặp mang khóa lớn", "các cặp trùng nhau phải được giữ" — khớp Ví dụ 2.1.
- Phân biệt hàm/tác vụ/worker/máy (s02-06), h(k) chọn tác vụ Reduce 0–r−1, "không được chia một khóa cho nhiều tác vụ" (s02-06b) — đúng mô hình.
- Phục hồi: Map hỏng → cả Map đã hoàn thành chạy lại vì tệp trung gian cục bộ mất, cập nhật vị trí cho Reduce (s02-07, s02-07a, tr.30); Reduce hỏng → chỉ chạy lại tác vụ đang chạy, kết quả đã xong nằm trên hệ tệp phân tán được giữ (s02-07b); Master hỏng → restart toàn bộ. Không bịa timeout hay giao thức commit — đúng ràng buộc.
- Kiểm tra chéo: Map 0 (D1) phát (lớn,1) với h(lớn)=1, nên "Reduce 0 và Reduce 1 cần đầu ra mới của Map 0" (s02-07a) là đúng; "một tệp rỗng trong ví dụ" (s02-06b, tệp R0 của Map 1) cũng nhất quán.

Hai nhận xét mức thấp (không phải lỗi)

1. **lec02-s02-07a, phần Ví dụ minh họa** — Câu "Reduce 0 và Reduce 1 cần đầu ra mới của Map 0" đúng nhưng mơ hồ; nên ghi cụ thể: R0 cần (dữ,1),(liệu,1); R1 cần (lớn,1). Mức: minor.
2. **lec02-s02-03a** — Chữ ký Reduce → List(K₃×V₃) là mở rộng ngoài nguyên văn MMDS (sách chỉ có K₂,V₂); đã được ghi chú "chữ ký mô tả kiểu dữ liệu", chấp nhận được, chỉ cần giữ nhãn "diễn giải". Mức: informational.

**Đề xuất:** không cần sửa nội dung kỹ thuật nào; chỉ áp dụng nhận xét 1 nếu muốn rõ hơn.

#### teaching

**Báo cáo review (chỉ đọc, không dùng tools) — bộ slide lec02-s02-***

Nhìn chung bộ slide đúng yêu cầu: tạo tác vụ, phân chia khóa h(k), phân bổ máy, phục hồi lỗi từng bước, không bịa timeout/ngưỡng, nguồn MMDS 2.2.1–2.2.6 tr.25–30 kèm Hình 2.2/2.3; ví dụ 2 Map/2 Reduce, D1/D2, máy A–F gắn nhãn "minh họa" rõ ràng. Chỉ phát hiện các điểm sau:

1. **(Trung bình) lec02-s02-06, NOTES**: "Worker thường chuyên Map hoặc Reduce". MMDS không quy định worker chuyên hóa; một worker chạy được cả tác vụ Map và Reduce. Bằng chứng: nguồn trích trong slide (2.2.2–2.2.5, tr.27–29) chỉ nói worker chạy tác vụ, Master phân công. Sửa: bỏ/đổi thành "một worker có thể nhận cả tác vụ Map và Reduce tùy phân công".

2. **(Thấp) lec02-s02-07a, NOTES**: câu đầu viết thường ("bộ điều phối định kỳ..."), thiếu chủ ngữ/câu hoàn chỉnh so với các slide khác. Sửa: viết hoa "Bộ điều phối..." cho nhất quán.

3. **(Thấp) lec02-s02-06b**: "một tệp rỗng trong ví dụ" đúng nhưng nên nói rõ tệp nào (tệp bucket-0 của Map 1, vì D2 chỉ phát khóa "lớn" → h=1) để sinh viên tái hiện được; hiện phải suy diễn.

4. **(Thấp) lec02-s02-06a**: "Sách cho phép mỗi tác vụ nhận một hoặc nhiều khối" — nên kèm trích trong NOTES rằng 1 khối/1 tác vụ là quy ước thực hành; hiện đã ghi "lựa chọn hợp lý, không phải đẳng thức", chấp nhận được.

**Điểm đã kiểm và đạt**: ký tự Map/Reduce ở s02-03a đúng MMDS; "Reduce gọi đúng một lần mỗi khóa" đúng; combiner có thể không chạy (s02-05) đúng 2.2.4; Map hỏng → kể cả task đã xong phải chạy lại vì tệp trung gian cục bộ mất, cập nhật vị trí cho Reduce (s02-07/07a) đúng 2.2.6 tr.30; Reduce hỏng → chỉ chạy lại task đang chạy, completed giữ trên DFS; Master hỏng → restart toàn bộ job (s02-07b) khớp yêu cầu, có chú thích "theo mô hình sách". Không có lỗi khẳng định sự thật sai mức nghiêm trọng.

#### flow

Nhận xét (chỉ đọc, ≤300 từ)

Nhìn chung khối 2.2 đúng mô hình sách: 1+nhiều khối/tác vụ (06a), h(k) chọn tác vụ (06b), Master gán/theo dõi (06c), Map hỏng chạy lại kể cả đã xong (07a), Reduce hỏng chỉ chạy lại đang chạy + Master hỏng restart (07b). Không thấy bịa timeout. Các lỗi có bằng chứng:

**1. Slide 07a/07b thiếu nội dung hiển thị (nghiêm trọng)**
Cả hai slide chỉ có tiêu đề và câu hỏi; phần thân giữa hai dòng trống (`(...)` rỗng), toàn bộ nội dung "Mất tệp trung gian... phải chạy lại" / "Chỉ chạy lại tác vụ Reduce đang thực hiện" nằm trong [NOTES KHÔNG HIỂN THỊ] cho slide 07a — nhưng 07b thì dòng đó *có* hiển thị. Không nhất quán: 07a nên hiển thị dòng tóm tắt tương tự 07b. Vị trí: `lec02-s02-07a`, phần hiển thị.

**2. Nguồn trang 07a (nhẹ)**
"Nguồn: 2.2.6, tr. 30" — mục 2.2.6 và tình huống Map worker hỏng nằm tr.29–30 (slide 07 ghi "tr. 23–24, 29–30"; 07b ghi "tr. 29–30"). Nên ghi 29–30 cho nhất quán.

**3. Chi tiết ví dụ 07a cần làm rõ (nhẹ)**
"Reduce 0 và Reduce 1 cần đầu ra mới của Map 0": đúng với h đã chọn (dữ, liệu → R0; lớn → R1 nhận lớn từ cả Map 0 và Map 1), nhưng nên nói rõ R1 chỉ cần phần Map 0 chạy lại, Map 1 trên B giữ nguyên — tránh hiểu nhầm phải chạy lại cả Map 1. Thực tế notes đã nói "Map 1 giữ nguyên", chỉ cần tách câu.

**4. Slide 03a nguồn (rất nhẹ)**
Ghi "tr. 25–27" trong khi phần thân dùng ký hiệu hàm — không sai, nhưng slide đầu mục ghi nguồn "2.2.2–6 tr 27–30" cho phần tác vụ; nên thống nhất phạm vi trích dẫn giữa 03a (nội dung 2.2.1–2.2.3) và phần thực thi.

Không phát hiện lỗi thuật ngữ máy/tác vụ/khóa hay khẳng định ngoài nguồn khác.

#### storyboard

Báo cáo kiểm tra Storyboard Bài 02 (chỉ đọc, không tools)

**1. Đếm ID: ĐẠT.** 45 slide giảng (s00:3, s01:3, s02:15, s03:4, s04:5, s05:6, s06:6, s07:2, s08:1) + 8 bài tập (221a–c, 231a–d, 251a) = 53 ID, khớp tuyên bố "45+8".

**2. Recitation: ĐẠT.** 221a/b/c = 3×5, 231a–d = 4×5, 251a = 25 → đúng 60 phút, đúng nguồn tr.30/PDF11, tr.40/PDF21, tr.59/PDF40. Bài 2.5.1(c) đã bỏ theo chỉ dẫn.

**3. Timing giảng: ĐẠT.** Tổng cộng slide giảng = 5+10+36+17+13+18+15+5+1 = 120 phút, khớp bảng "Hành trình khái niệm" (từng mục đều khớp, kể cả 2.2 = 36 sau khi cộng lại).

**4. Phân chi tiết s02 (h=36 phút):** 6 slide ×3 phút + 9 slide ×2 phút = 36 ✓.

**5. 9 section ngoại lệ: ĐẠT** (mở đầu + 2.1–2.8), có ghi rõ lý do yêu cầu người dùng.

Lỗi phát hiện

**L1 — Trung bình (Thấp), `lec02-s05-03`:** "Kiến thức đầu vào" ghi "I và B byte" nhưng ký hiệu B không được định nghĩa ở đâu trong storyboard; `lec02-s05-01` chỉ lập "tổng I+M". Nguy cơ lẫn M/B ở slide chi phí. **Sửa:** thống nhất một ký hiệu (I+M) hoặc định nghĩa B tại s05-01.

**L2 — Trung bình (Thấp), `lec02-s05-01/02`:** thứ tự trình bày s05-02 đứng trước s05-01; được câu chuyện "thứ tự do DOM quyết định" che chắn, nhưng bảng mạch s05 không ghi chú điều này ở mục 2.5 như các mục khác. **Sửa:** thêm một dòng chú thích DOM ở mục 2.5 để tránh hiểu nhầm khi diễn tập.

**L3 — Thấp, `lec02-s02-07a`:** câu chốt "Map đã xong vẫn phải tính lại nếu đầu ra cục bộ mất" đúng sách; tuy nhiên "báo tệp thay thế"/"cập nhật nơi cho reduce" nên nhắc rõ trong notes là cập nhật vị trí tệp trung gian cho các Reduce worker (hiện chỉ ở mô tả SVG). **Sửa:** ghi rõ vào ghi chú s02-07a.

Không phát hiện

- Không thấy timeout, cơ chế commit hay chi tiết ngoài nguồn được bịa thêm.
- Minh họa 2 Map/2 Reduce, máy A–F, một tệp rỗng (h(dữ)=h(liệu)=0, h(lớn)=1) tự nhất quán với Hình 2.3 và đã dán nhãn "minh họa, không nguyên văn".
- Master hỏng → restart job có nêu giới hạn ở s02-07b ✓.
- Tất cả kết nối vào–ra giữa các slide giảng khớp theo chuỗi.

**Kết luận:** đạt với 3 chỉnh sửa nhỏ, không chặn xuất bản.

#### editor

Báo cáo biên tập (≤200 từ)

Đã sửa CHỈ `edit-deck.html`, 3 thay đổi, mỗi cái 1 lần thay, thành công:

1. **s02-07a notes**: viết hoa đầu đoạn "bộ điều phối định kỳ kiểm tra…" → "Bộ điều phối định kỳ kiểm tra…".
2. **s02-06c nguồn**: "slide MMDS Chương 2, mục thực thi gần dữ liệu và bộ điều phối" → "slide MMDS Chương 2, trang 24–25".
3. **s02-06b notes**: "một tệp rỗng trong ví dụ" → "tệp dành cho R0 của Map 1 rỗng trong ví dụ".

**Quyết định điều phối — các nhận xét bị bác:**
- Thiếu hiển thị 07a/07b: bác — SVG đã render 4 bước, caption vẫn có; không thêm text trùng SVG.
- Reviewer đòi đổi "Worker chuyên Map/Reduce": bác — tr.28 nguyên văn "Normally, a Worker handles either Map tasks … or Reduce tasks … but not both".
- Khó khả kiểm kiểu ngoài sách: bác — 2.2.3 nguyên văn "can be of a type different".
- 1 khối 1 Map bắt buộc: bác — tr.29 "one or more chunks".
- Nguồn bài 2.2.1 tr.30/PDF11: đúng, giữ.
- B byte: đã định nghĩa trên slide chi phí; ID DOM giữ ổn định.
- Root đã chỉnh 3 lỗi hình thực (nhãn Reduce cắt, nhãn điều phối bị mũi tên đè, chữ R1 tràn hộp).

Phần khác giữ nguyên.

#### final-student

**Kết quả rà soát (không dùng tools): ĐẠT — không phát hiện lỗi thực chất.**

Kiểm chứng 3 trích dẫn bắt buộc:
1. **MMDS tr.29** "one or more chunks": khớp — slide s02-06a ghi đúng "một tác vụ nhận một hoặc nhiều khối", và notes khẳng định "một tác vụ cho mỗi khối là lựa chọn hợp lý, không phải đẳng thức bắt buộc". Đúng.
2. **MMDS tr.28** "Normally … either … but not both": khớp — s02-06 notes "Worker thường chuyên Map hoặc Reduce"; s02-06c minh họa A,B chạy Map, C,D chạy Reduce, có ghi rõ "không là ảnh chụp bốn tác vụ chạy đồng thời". Đúng.
3. **MMDS tr.27** "can be of a type different": khớp — s02-03a "Khóa đầu ra K₃ có thể khác K₂". Đúng.

Nguồn 2.2.6 tr.30: s02-07a/07b đúng cơ chế — Map hỏng chạy lại kể cả đã xong (tệp trung gian cục bộ mất); Reduce hỏng chỉ chạy lại tác vụ đang chạy; Master hỏng khởi động lại toàn bộ, có ghi chú "mô hình sách, không khẳng định mọi hệ thống hiện đại". Đúng.

Kiểm tra số học: 5 cặp → 4 cặp, (lớn,3) nhất quán qua s02-02/03/05/06b. Chữ ký Reduce K₂×List(V₂)→List(K₃×V₃) khớp MMDS.

Lỗi nhỏ (không bắt buộc sửa): s02-07a notes có câu bắt đầu "bộ điều phối…" viết thường sau dấu chấm — chỉ chính tả.

**Kết luận: 53 slides đạt, không có lỗi nội dung có bằng chứng.**

#### final-flow

**Kết quả rà soát (chỉ đọc, không tools): ĐẠT — không có lỗi nội dung thực sự.**

Kiểm chứng khối 1 (Map bắt buộc, tr.29 "one or more chunks"): s02-06a notes ghi đúng "một hoặc nhiều khối; một tác vụ cho mỗi khối là lựa chọn, không phải đẳng thức bắt buộc" — khớp nguồn. Worker chuyên Map/Reduce (tr.28): s02-06 notes khớp. Reduce kiểu khác (tr.27): s02-03a chữ ký K₃×V₃ và notes "Khóa đầu ra K₃ có thể khác K₂" — khớp. Nguồn 2.2.6 tr.30 (Map hỏng chạy lại kể cả đã xong; Reduce hỏng chỉ chạy lại tác vụ đang chạy; Master hỏng khởi động lại toàn bộ): s02-07, 07a, 07b đều đúng và có ghi nguồn.

Ranh giới sang 2.3: s03-01 mở mục mới, định nghĩa (i,j,mᵢⱼ), công thức xᵢ — đúng tr.31–32, không trùng nội dung 2.2.

SVG: các nhãn đã render trong thẻ [CHỮ TRÊN HÌNH SVG], không còn packet bỏ SVG; 53 slides không có dấu overflow; notes đều có cặp [BẮT ĐẦU/HẾT NOTES].

**Lỗi nhỏ duy nhất (độ ưu tiên thấp):** lec02-s02-07a, notes, câu "bộ điều phối giao lại tác vụ cho tiến trình thực thi khác…" viết thường sau dấu chấm — nên viết hoa "Bộ".

#### final-math

**Kết quả rà soát: đạt — không phát hiện lỗi nội dung có bằng chứng.**

Kiểm tra đối chiếu nguồn:

- **s02-03a**: chữ ký Reduce `K₂×List(V₂)→List(K₃×V₃)` khớp MMDS tr27 "can be of a type different"; "Reduce gọi đúng một lần mỗi khóa" khớp mô hình sách.
- **s02-06**: "Worker thường chuyên Map hoặc Reduce" khớp tr28 "Normally... either... but not both"; phân biệt hàm/tác vụ/worker/master đúng.
- **s02-06a**: "một tác vụ Map cho mỗi phần dữ liệu" được notes giới thiệu đúng là lựa chọn, không đẳng thức bắt buộc — khớp tr29 "one or more chunks".
- **s02-06b**: h(k) minh họa, r=2, tệp R0 của Map 1 rỗng — nhất quán với Hình 2.3.
- **s02-07/07a/07b**: Map hỏng → chạy lại cả Map đã xong (tệp trung gian cục bộ mất); Reduce hỏng → chỉ chạy lại tác vụ đang chạy; Master hỏng → khởi động lại toàn bộ — khớp 2.2.6 tr30.
- **s02-05**: combiner có thể không chạy, trung bình giữ (tổng, số lượng) — đúng 2.2.4.
- **s02-02/03/05**: đếm 5 cặp, lớn=3, gộp 5→4 — số học đúng.
- **ex221a/b, s03-01**: khớp Bài tập 2.2.1 và 2.3.1.

Lỗi nhỏ duy nhất (chính tả, không sai nội dung): **lec02-s02-07a**, notes, câu "…đã mất. bộ điều phối giao lại…" — "bộ" viết thường sau dấu chấm; nên viết hoa "Bộ".

### Dấu vết bản thực thi đã kiểm

| Tệp | SHA-256 |
|---|---|
| `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html` | `efd4d86cf0a39593cfd8f1e092d6d76cfab4027a3d3286c6fccb0333194f0137` |
| `2627-1/materials/lec-02/lecture-note.md` | `0303d461d9f7968669703a693b4c45309477240bc4fbc22e901f43464818e719` |
| `2627-1/planning/lec-02/outline.md` | `592104002dc6b3ad25746efe4bbf216ad5030e7d0f25e022b2bc7d4b2abd345b` |
| `2627-1/planning/lec-02/storyboard.md` | `7ddbc9950b179626182f4650b902b8694be5da36d83c659b7fd2183d7c8565dd` |
| `2627-1/index.html` | `946cbd72ca6ec782bf033d1fa6a2aabab6c5ed06bece5d81e75fff9438ea5698` |
| `2627-1/img/lec-02/ch2-map-group-reduce.svg` | `88c390ce5ece0a28988d219b850de194eaa426045284ecfd85b5fcf5be630997` |
| `2627-1/img/lec-02/scripts/render-execution-diagrams.py` | `4956a12b19d7f48aea610a57db7100148bf023170bf26e0a10a88d836815de02` |
| `2627-1/img/lec-02/ch2-tao-tac-vu-map.svg` | `634a2f65eb4f8d2ce9db6f1ed46b4bf7ee99e79c51c6e79d044e659a7efaa47f` |
| `2627-1/img/lec-02/ch2-phan-vung-reduce.svg` | `259c01ba4ef1d2c14c88940d35e7aa628fcd0c5132fdd80c7a560fb4f9fc40ef` |
| `2627-1/img/lec-02/ch2-phan-bo-tac-vu.svg` | `51289b20470e0fbd3d6d61f9aa788f3e5394dc8f184b93c2d8dbb97fcb1479ae` |
| `2627-1/img/lec-02/ch2-phuc-hoi-map.svg` | `3853234eb35238b60a8c0e9d3a3bb3c24b0eea4babea193bc30fea69c82dbfd2` |
| `2627-1/img/lec-02/ch2-phuc-hoi-reduce.svg` | `189bcaca0cde327708838ca184cbf141e9a1f42dfbd0be95ca26c569b93f7cad` |
