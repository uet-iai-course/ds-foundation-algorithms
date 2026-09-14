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
