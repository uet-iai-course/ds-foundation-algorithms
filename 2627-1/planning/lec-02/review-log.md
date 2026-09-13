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
