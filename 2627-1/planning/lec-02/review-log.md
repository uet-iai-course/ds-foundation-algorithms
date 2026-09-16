# Nhật ký Bài 02

## Đặt lại bài giảng — 2026-09-16

Theo yêu cầu người dùng: xóa toàn bộ nội dung Lecture 02, chỉ giữ một slide trống. Gỡ ghi chú cũ, hình riêng của bài và script sinh hình; gỡ liên kết ghi chú khỏi index. Dàn ý và storyboard cũ được thay bằng trạng thái chờ xây dựng lại. Nội dung trước đó có trong lịch sử Git. Giữ tài liệu nguồn và thư viện dùng chung.

Chỉ commit; không push theo chỉ dẫn mới nhất.

## Soạn lại slide 1

Theo nội dung người dùng chỉ định, thay trang trống bằng slide tiêu đề “Mô hình tính toán Map-Reduce”, kèm tên môn và học kỳ. Đặt trong section “Giới thiệu bài học”. Không khôi phục nội dung cũ.

## Thêm slide 2

Thêm slide “Nội dung” trong section giới thiệu, chưa tự điền đề mục. Bật nút điều hướng để chuyển giữa hai slide. Chưa commit/push.

Bổ sung tạm một dòng “Giới thiệu” trên slide Nội dung theo yêu cầu. Khi có section mới, cập nhật danh sách tương ứng.


## Động lực và yêu cầu mô hình

Duyệt một slide động lực trong section Giới thiệu, sau Nội dung. Giữ ba bài toán của Google từ bài báo2004, hình máy phổ thông và phần dữ liệu. Theo câu hỏi tiếp theo của người dùng, câu chốt phải làm rõ tính chất chung: xử lý tương tự trên từng phần/bản ghi, rồi gộp kết quả cục bộ. Không đưa chữ ký Map/Reduce, khóa hoặc cơ chế chuyển dữ liệu lên mặt slide này. Notes giải thích ba ví dụ và nhu cầu phối hợp máy; đây là động lực mô hình lập trình, không tuyên bố mọi bài toán dữ liệu lớn đều phù hợp. Hình ba máy minh họa, không số đo Google. Không thêm section mới, mục lục vẫn chỉ Giới thiệu. Không phục hồi deck/ghi chú đã xóa; không commit/push.

Theo các chỉ dẫn tiếp theo của người dùng, tách phần dẫn dắt thành slide 3 về Google và slide 4 về bốn yêu cầu: dữ liệu trên nhiều máy; tính toán song song; tính toán gần dữ liệu; phân chia, lập lịch, chống lỗi và phục hồi trong suốt đối với lập trình viên. Người dùng chỉ đạo từng slide nên chưa lập lại cả bài hoặc tài liệu tự học.

### Rà soát phần dẫn dắt

Nguồn đã đối chiếu: MMDS Chương2 trang21–24; slide MMDS/Stanford về cụm máy và hạn chế truyền mạng; bài gốc [Dean–Ghemawat2004](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/), mục1,2.3,3.1,3.3,3.4. Chọn bài gốc cho các công việc cụ thể của Google; không dùng ước lượng số máy hoặc thông số phần cứng cũ như hiện trạng. Hình SVG vẽ trực tiếp, ba máy chỉ là minh họa.

Planner, source reader, writer, storyboard reviewer, năm vai rà soát, editor riêng và flow recheck dùng OpenRouter; requested/observed `z-ai/glm-5.3-flash`, provider `OpenRouter`, hồ sơ ở `/tmp/lec02-intro/`. Writer ghi vào đường dẫn lồng trong thư mục tạm; điều phối viên lấy đúng tệp, bổ sung data-slide-id, bỏ lời khẳng định không được kiểm chứng về Google hiện nay và sửa câu đầu ra của ví dụ chỉ mục. Các yêu cầu tiếp theo của người dùng được tích hợp thành slide4, không mở section mới. Bác góp ý mở rộng mục lục vì người dùng yêu cầu chỉ “Giới thiệu”; bác nhầm tên mục3.1 (đúng là Execution Overview) và yêu cầu đồng nhất mọi dải trang nguồn. Biên tập tiếng Việt và kiểm tra mạch theo no-ai-slop/quill; không khởi tạo sách hoặc khôi phục nội dung cũ.

Kiểm định Chromium: đúng4slide,1section lớn, hình tải được, không tràn, không lỗiJavaScript/HTTP; bản in4trang. Đã xem hình trình chiếu của slide3/4; slide4 ghi đầy đủ phân chia, lập lịch, chống lỗi và phục hồi các tác vụ song song. Mục lục vẫn một dòng “Giới thiệu”. Không commit/push. Không đồng bộ Codex Slides Design Files; giữ giới hạn egress đã xác định trước đó.

## Sửa hình khối và bản sao

Theo yêu cầu người dùng, thay hình mỗi máy một phần bằng ba khối A/B/C, mỗi khối có hai bản sao trên hai máy khác nhau. Nhãn và màu lặp để nhận ra cùng dữ liệu; không dùng màu làm tín hiệu duy nhất. Hai bản sao chỉ minh họa, không mô tả số bản sao mặc định của Google. Cập nhật alt, notes, storyboard và phiên bản URL ảnh. Nguồn: Dean–Ghemawat2004 mục3.4; MMDS2.1.2. Chưa commit/push.

## Ví dụ cộng n số và toán tử tổng quát

Duyệt một slide mới: phép cộng n số → ví dụ 6 số chia 3 máy không trùng → tổng cục bộ → gộp tổng → hai tính chất cho phép đổi thứ tự/nhóm → thay mọi dấu cộng bằng toán tử giao hoán và kết hợp. Để hai công thức tính chất, miền đóng, trường hợp nhóm rỗng và số dấu phẩy động trong notes để giảm tải. Không thêm badge cảnh báo trên mặt như planner đề xuất. Mỗi số chỉ được tính một lần, phân biệt với bản sao lưu trữ ở slide3. Chưa thêm section, mục lục vẫn Giới thiệu; không commit/push.

Writer soạn riêng, điều phối viên lấy phần section từ khung HTML thừa, thay mũi tên ngang bằng ba mũi tên gộp, biên tập notes và làm rõ toán tử mới giữ kết quả của chính phép gộp đó, không nhất thiết bằng tổng số học. Bật KaTeX cục bộ để dựng công thức, không dùng ảnh công thức.

Theo yêu cầu người dùng, đổi tiêu đề slide `lec02-s01-05` thành “Ví dụ: Cộng dãy số”; đồng bộ storyboard, giữ nội dung minh họa. Chưa commit/push.

Người dùng chốt lại tiêu đề: “Ví dụ: Cộng dãy số (song song hoá và cục bộ hoá)”. Đã đồng bộ HTML và storyboard; giữ nguyên nội dung. Chưa commit/push.

## Thêm sơ đồ rack và quy mô các bài toán

Thêm đúng slide `lec02-s01-06` trong Giới thiệu. Planner, writer và reviewer độc lập qua OpenRouter đều xác nhận requested/observed `z-ai/glm-5.3-flash`; hồ sơ `/tmp/lec02-rack/`. Điều phối viên vẽ SVG và giữ script tái sinh; bỏ caption quy trình mà writer thêm, rút nội dung thành hai cột, biên tập thuật ngữ và bổ sung phân biệt HDFS với hệ thống lập lịch. Rà độc lập không phát hiện lỗi nội dung; giữ câu nối trong notes, không thêm chữ lên mặt theo góp ý tùy chọn. Nguồn Apache HDFS Architecture, các mục về đưa tính toán gần dữ liệu, nhân bản, đặt bản sao và phục hồi. Sơ đồ cố ý bỏ quản lý siêu dữ liệu, đã ghi rõ phạm vi. Ba bản sao trên hai rack cho phép từng rack còn đủ A/B khi rack kia lỗi; không cam kết mọi thành phần luôn hoạt động. Đã sửa đường nối bộ chuyển mạch xuyên viền rack sau khi xem ảnh.

Slide `lec02-s01-03` bổ sung quy mô có nguồn gốc cho từng ví dụ; chủ động dùng các năm khác nhau và ghi nhãn để không đánh đồng. Thay ví dụ nhật ký URL bằng đếm truy vấn chứa từ khóa theo thực nghiệm 450 GB của Sawzall. Không dùng 450 GB như số liệu mỗi ngày; không suy số liên kết từ số trang; không coi chỉ mục 8 tỷ trang là một tác vụ MapReduce. Nguồn và phạm vi từng số ở storyboard/notes. Không commit/push.

Kiểm định bản cuối: Chromium hiển thị 6 slide, 1 section lớn; hình tải đủ, không tràn theo kiểm tra phần tử, không lỗi JavaScript/HTTP/KaTeX; bản in 6 trang. Đã xem ảnh slide Google và HDFS, kiểm tra đường nối rack và nhãn bản sao. Mục lục vẫn một dòng Giới thiệu. Chưa commit/push.

## Mở section 2 và đặc tả ví dụ đếm từ

Theo chỉ dẫn mới, thêm đúng hai slide và thêm mục Mô hình tính toán Map-Reduce vào Nội dung. Người dùng làm rõ slide đầu phải nêu khả năng, không giải thích cách làm; bỏ kế hoạch sơ đồ Map/nhóm/Reduce trước khi triển khai writer. Slide thứ hai là đặc tả bài toán đếm từ, ví dụ xuyên suốt section, chưa giải thuật. Công thức số đếm từng văn bản nối với phép cộng đã giới thiệu. Giữ hai section theo tiến độ xây từng bước, không tạo phần còn thiếu của cả bài.

Planner và source reader riêng chạy qua OpenRouter. Lượt source đầu chỉ có mô tả; đã bổ sung trích xuất sách thực tế và chạy lại, xác minh ví dụ2.1–2.2. Writer tạo hai slide; điều phối viên chuyển ký hiệu sang KaTeX, viết lại notes thành lời giảng, bỏ nhãn quy trình và giữ giả thiết/ca rỗng. Nguồn MMDS2.2 trang25–27,2.2.5 và Dean–Ghemawat2004 về khả năng. Không thêm ví dụ số hoặc tự đặt dữ liệu. Chưa commit/push lần sửa này.

Năm vai rà độc lập xác nhận đặc tả đúng và mạch phù hợp. Editor riêng sửa câu đầu ra, thêm nguồn MMDS hiển thị và đổi câu dẫn để nối với nhu cầu ở Giới thiệu. Giữ h1 mở phần và tiêu đề tần suất theo yêu cầu; số lần xuất hiện đã được giải nghĩa, không thêm cảnh báo tỷ lệ lên mặt. Bổ sung bốn icon SVG nội dòng theo yêu cầu mới, nhãn/title riêng và bố cục thống nhất; không thêm sơ đồ cơ chế. Flow recheck xác nhận mục lục, hai section, khả năng và ví dụ; giữ câu nối chi tiết trong notes thay vì thêm chữ trên mặt. Tất cả báo cáo dùng requested/observed z-ai/glm-5.3-flash, provider OpenRouter, hồ sơ /tmp/lec02-model/.

Kiểm định bản cuối sau icon: 8 slide, 2 section, mục lục 2 mục; không tràn phần tử, không lỗi JavaScript/HTTP/KaTeX, in 8 trang. Đã xem ảnh hai slide mới, icon và công thức đọc được. git diff --check đạt. Chưa commit/push.

Theo yêu cầu bố cục mới, slide đếm từ dùng lưới 70/30: đặc tả bên trái, hình tập văn bản đi tới bảng số đếm bên phải. Hình dùng cùng ký hiệu, không thêm ví dụ hoặc thay mạch; rút câu đầu ra để vừa cột và giữ nghĩa tổng số lần. Đã xem ảnh ở 1280×720; kiểm tra 8 slide không tràn, không lỗi công thức/JavaScript/HTTP, in 8 trang. Chưa commit/push.

Sửa hình theo phản hồi: mỗi nhãn d₁, d₂, dₙ nằm trên một tờ riêng, dấu … ở giữa các tờ biểu thị phần còn lại; bỏ nhãn cả dãy trên một văn bản. Giữ bố cục 70/30 và đặc tả. Chưa commit/push.

## Hai hàm, điều phối tác vụ và chạy ví dụ đếm từ

Người dùng yêu cầu nối tiếp ba slide: mô tả Map/Reduce, phối hợp và phân phối tác vụ, chạy ví dụ cụ thể. Planner riêng xác nhận hai hàm theo MMDS; source excerpt đã được reader kiểm chứng ở lượt trước và được writer đọc lại. Ví dụ hai văn bản mới được chọn theo yêu cầu minh họa cụ thể, không xem là dữ liệu trích nguyên sách.

Writer soạn ba section riêng. Điều phối viên chuyển giả mã sang code data-trim, rút phần giải thích bộ gộp phụ khỏi mặt slide, làm rõ hệ thống nhóm theo từ và viết lại mô tả luồng dữ liệu trực tiếp giữa máy. Mỗi văn bản gọi Map; một tác vụ có thể gọi nhiều lần. Gán ba tác vụ Map và hai tác vụ Reduce lên ba máy là sơ đồ minh họa, không cấu hình bắt buộc.

Năm báo cáo độc lập xác nhận các số đếm và cơ chế đúng. Bác lỗi thẻ đóng thừa: reviewer được gửi phần đuôi HTML nên không thấy các thẻ mở ngoài; thẻ đóng section/div thuộc cấu trúc Reveal hợp lệ. Kiểm định toàn deck xác nhận hai section lớn và 11 slide. Giữ cách gọi Map-Reduce theo người dùng. Editor riêng làm rõ chia đầu vào và không suy số tác vụ từ số văn bản. Căn lại mũi tên theo các hàng tác vụ sau kiểm tra hình. Hồ sơ OpenRouter ở /tmp/lec02-wordmap/, requested/observed z-ai/glm-5.3-flash, provider OpenRouter. Chưa commit/push.

Điều phối viên phát hiện editor đổi nhầm h3 ở slide hàm thành Tác vụ Map; đã sửa thành Hàm Map/Hàm Reduce và loại nguồn lặp. Rà mạch bản đầy đủ xác nhận không lỗi thực chất, ba bước hàm → tác vụ → chạy ví dụ nhất quán. Kiểm tra Python cho dữ liệu ví dụ trả mèo:2, chó:2, chim:1, tổng5. Kiểm định Chromium bản cuối: 11 slide/2section, không tràn, không lỗi JavaScript/HTTP/KaTeX, bản in11trang. Đã xem cả ba slide mới và căn mũi tên vào đúng hàng tác vụ. Giả thiết số đếm vừa một từ máy và q_w là độ dài danh sách được bổ sung cho mô hình chi phí trong notes. Chưa commit/push.

Bổ sung quan hệ máy–tác vụ theo phản hồi: một máy chạy nhiều tác vụ; một tác vụ có nhiều lượt thực thi trên nhiều máy để dự phòng. Nguồn đã đối chiếu bài gốc Dean–Ghemawat 2004, mục 3.3/3.6: chạy lại khi lỗi và thực thi dự phòng cho tác vụ chậm. Notes phân biệt tác vụ logic/lượt thực thi, tính toán dư thừa/nhân bản lưu trữ; không cộng trùng kết quả của các lượt. Chưa commit/push.

## Hình thức hóa mô hình Map-Reduce

Người dùng yêu cầu chuyển từ ví dụ sang dạng toán học tổng quát, các pha thực thi và một mô tả thuật toán; bổ sung hình khi có ích. Duyệt năm slide tiếp trong section 2: Map, Reduce, nhóm/phân phối, các pha, giả mã. Hình hỗ trợ kiểu dữ liệu và luồng xử lý; giả mã cuối giữ làm trọng tâm. Không mở section mới hoặc thêm chuỗi nhiều công việc vào phạm vi lần sửa này.

Planner và source reader riêng qua OpenRouter. Chữ ký đầu ra Reduce dùng dãy cặp theo MMDS2.2.3, cho phép miền đầu ra khác miền trung gian; ghi khác biệt với ký hiệu hẹp của Dean–Ghemawat2004§2.2. Bác các nhận xét không đúng của source reader về phép max/bộ gộp, phép nhóm bỏ bản trùng và yêu cầu Reduce phải lũy đẳng để chống lỗi: nhóm giữ mọi đóng góp logic, các lượt thực thi trùng do hệ thống quản lý, không phải cộng thêm rồi buộc Reduce khử trùng. Giao hoán/kết hợp của phép cộng chỉ là trường hợp riêng; kết quả độc lập thứ tự danh sách cần giả thiết phù hợp với hàm Reduce cụ thể. Chi tiết này được kiểm tra lại từ nguồn gốc trước khi giao writer.

Writer tạo năm slide nhưng kèm khung HTML và một số diễn đạt chưa chính xác. Điều phối viên chỉ lấy các section, bổ sung id/class, rút lời dẫn, dựng lại sơ đồ HTML/KaTeX cho Map/Reduce và sơ đồ phân phối/các pha; công thức và giả mã không chuyển thành ảnh. Sửa nhầm tác vụ được gọi nhiều lần thành tác vụ gọi hàm nhiều lần; sửa kết luận sai rằng đầu vào hữu hạn tự bảo đảm kết thúc; nối cách viết Map(d_i) giản lược sang cặp mã/nội dung mà không coi cách giản lược là sai. Ví dụ phân phối dùng phần trích mèo/chó, đã ghi rõ trên mặt để không ngụ ý bỏ nhóm chim khỏi kết quả đầy đủ.

Năm reviewer độc lập xác nhận quy tắc giữ lặp, ca rỗng và vai trò nhóm/phân phối. Chấp nhận làm rõ thứ tự liệt kê I và giả thiết kết thúc/ổn định trên mặt slide. Bác đề nghị dùng tập hợp thay dãy, đổi V2* vì thiếu ngoặc, thêm định nghĩa X trước khi cần và gộp tính xác định với độc lập thứ tự hoặc tính lũy đẳng. X đã được định nghĩa trên slide các pha, L_k đã được giải nghĩa bằng lời trước hình thức hóa. Bác nghi ngờ MMDS không cho Reduce phát nhiều cặp: trích xuất nguồn mục2.2.3 ghi trực tiếp dãy không hoặc nhiều cặp. Editor riêng tiếp nhận những chỉnh sửa đã duyệt. Lượt render đầu phát hiện CSS span của thẻ pha tác động cả span KaTeX, đã giới hạn selector vào con trực tiếp; kiểm định lại sau biên tập.

Bản cuối đã thêm giả thiết hiển thị, giải thích khóa mã văn bản, và làm rõ thứ tự tùy chọn của I. Rà mạch lại từ ví dụ đến tổng quát không phát hiện lỗi lớn; bổ sung notes về việc vòng Map hoàn tất về logic trước Reduce, đồng thời cho phép truyền dữ liệu chồng lấp trong cài đặt. Kiểm định Chromium: 16 slide/2section, không tràn phần tử, không lỗi JavaScript/HTTP/KaTeX, bản in16trang. Đã xem ảnh năm slide mới, công thức trong sơ đồ pha đọc đúng sau sửa CSS. Mục lục giữ2mục, mô tả Bài2 ở trang học phần cập nhật phạm vi hiện có. Hồ sơ /tmp/lec02-formal/: planner, reader, writer,5reviewers,editor,flowrecheck đều requested/observed z-ai/glm-5.3-flash, provider OpenRouter. Chưa commit/push.

## Bổ sung hàm phân phối và Combine

- Đã thêm “(hàm phân phối)” cạnh định nghĩa $p$ theo yêu cầu.
- Thêm `lec02-s02-11` sau mô hình cơ bản, giữ nguyên dữ kiện đếm từ; Combine giảm 5 xuống 4 cặp trung gian. Nguồn MMDS 2.2.4 trang 27–28 và Dean–Ghemawat 4.3.
- Reader kế hoạch, reader nguồn, writer chạy OpenRouter; requested/observed `z-ai/glm-5.3-flash`, provider OpenRouter. Hồ sơ tạm `/tmp/lec02-combine/`. Điều phối chấp nhận kế hoạch một slide; sửa bản writer để giữ giao diện hiện tại, tăng độ rộng hình, tránh chật nhãn.
- Bác cách diễn đạt của reader rằng trung bình “không giao hoán”: vấn đề là không kết hợp. Bác phát biểu Combine chỉ hợp lệ khi Reduce tổng quát kết hợp/giao hoán; đây là điều kiện đủ của cách gộp đang minh họa. Notes làm rõ tương thích, giữ khóa/kiểu, gộp nhiều tầng, chi phí gộp và giới hạn giảm dữ liệu.
- Dùng no-ai-slop để biên tập và quill để giữ mạch: mô hình cơ bản → tối ưu Combine; không tạo dự án sách. SVG nội dòng có mô tả thay thế, số cặp và kết quả tự kiểm đúng.
- Chromium: 17 slide, không tràn khung, không lỗi JavaScript/HTTP/KaTeX; bản in 17 trang. Đã xem ảnh slide Combine. `git diff --check` đạt. Không commit/push.
- Reviewer độc lập OpenRouter (`z-ai/glm-5.3-flash`, requested/observed trùng nhau) kết luận đạt: ví dụ, điều kiện đủ, ghi chú trung bình và vị trí trong mạch không có lỗi cần sửa.

## Khép section mô hình bằng câu hỏi kiểm tra

- Theo yêu cầu, thêm `lec02-s02-12` “Câu hỏi kiểm tra”, có dữ kiện và ba câu về Combine, Reduce, khóa/tác vụ/máy; đáp án trong notes. Dùng lại ví dụ đã có, không thêm bài tập recitation.
- Ghi kế hoạch hai section chính riêng Hệ thống và Chi phí và lợi ích của song song hóa. Chưa soạn hai section này; mục lục vẫn phản ánh hai section hiện có.
- Writer và reviewer OpenRouter requested/observed `z-ai/glm-5.3-flash`, provider OpenRouter; hồ sơ `/tmp/lec02-check/`. Reviewer kết luận đạt. Điều phối làm rõ Combine cũng cộng, sửa “nhiều tác vụ cùng lúc” thành “lần lượt hoặc đồng thời tùy tài nguyên và lịch”.
- Kiểm tra Chromium: 18 slide, không tràn khung, không lỗi JavaScript/HTTP/KaTeX, bản in 18 trang; đã xem ảnh slide mới. `git diff --check` đạt. Không commit/push.

- Theo yêu cầu cuối, bỏ cụm “Map phát (từ, 1)” khỏi dữ kiện hiển thị của slide Câu hỏi kiểm tra; giữ đáp án trong notes. Người dùng đã yêu cầu commit và push các thay đổi Lecture 02.

## Kế hoạch section ví dụ

- Thêm section chính theo yêu cầu: ba bài toán, mỗi bài năm slide riêng đúng thứ tự chỉ định; mở phần và kiểm tra cuối, tổng 17 slide mới. Ngoại lệ thứ tự chu trình học tập được chấp nhận theo người dùng.
- Hai reader OpenRouter requested/observed z-ai/glm-5.3-flash, provider OpenRouter; hồ sơ /tmp/lec02-examples/. Điều phối duyệt thiết kế trong design.md trước writer.
- Không áp dụng phương án reader gộp chạy tay/chứng minh hoặc thêm slide ngoài khuôn; sửa nhầm khóa của trung bình thành khóa chung g, bác trả 0 cho trung bình dãy rỗng và nhận định một từ chỉ nằm trong một Map. Bác ví dụ kiểm tra ma trận sai kích thước của reader. Bản writer phải theo đặc tả đã kiểm tra.
- Ví dụ ma trận dùng 2×2 đầy đủ tọa độ kể cả 0 để giữ đầu ra hàng toàn 0. Đây là quy ước minh họa rõ ràng, không khẳng định các ma trận dữ liệu lớn phải lưu dày. Sách cho phép biết tọa độ qua vị trí hoặc bản ghi.
- Yêu cầu mới về icon/hình được đưa vào đặc tả trước khi soạn; không dùng ảnh raster hoặc nguồn mạng.

### Rà soát và hoàn thiện section 3

- Năm reviewer độc lập đã rà góc nhìn sinh viên, giải thuật, toán, giảng dạy và mạch. Tất cả requested/observed z-ai/glm-5.3-flash, provider OpenRouter. Giữ kết luận có bằng chứng: sửa các câu đảo 5/6 trong ví dụ trung bình và ghi chú kiểm tra; sửa ví dụ hai nhóm bằng nhau bị viết thành bất đẳng thức; thay chỉ số Unicode sai trong sơ đồ.
- Điều phối rà thêm đầu vào Reduce sau Combine: danh sách hàng 1 là [13], hàng 2 là [15], không phải các danh sách trước Combine. Làm rõ từ có thể xuất hiện ở nhiều tác vụ; bỏ Combine trong vết chạy công việc đếm cuối để không ngầm giả định tất cả bản ghi nằm trong một tác vụ Map.
- Tác tử chỉnh sửa đầu dừng với lỗi nguyên văn “model exceeded the tool-call limit (10)”. Đã chạy lại cùng vai OpenRouter với giới hạn phù hợp; không đổi nhà cung cấp. Điều phối bác chỉnh sửa nhầm số 5/6 của bài trung bình sang đáp án đếm từ ở lượt sửa lại, khôi phục đúng 2+2=4 đếm trùng chó, kết quả3. Không dựa vào kết luận “đạt” khi báo cáo bỏ sót phép tính sai.
- Biên tập theo no-ai-slop: bỏ câu siêu dữ liệu “Câu nối”, “các giả thiết được nêu gọn”; Việt hóa chunk/mean/scalar/Job. Rà theo quill: giữ cùng dữ kiện, ký hiệu, đầu ra và giả thiết trong mỗi chuỗi năm slide; không tạo quill.json.
- SVG nội dòng có role/nhãn thay thế, icon trên các slide đặc điểm, ba sơ đồ luồng có mũi tên. Bảng và công thức giữ ở HTML/KaTeX; không thêm ảnh vào chứng minh khi không giúp suy luận. Không áp dụng đề xuất thêm hình lặp lại bảng chạy tay trung bình.
- Mục lục và mô tả bài trong index đã cập nhật. Tổng hiện tại 35 slide, ba section chính; số section ngoài 5–7 là ngoại lệ vì người dùng đang xây bài từng phần. Hệ thống và Chi phí còn ở mức kế hoạch.
- Kiểm định 1280×720: 35 slide không tràn, không lỗi JavaScript/HTTP/KaTeX; bản in35trang. Mã slide duy nhất, section lồng đúng, SVG có mô tả thay thế; đã xem trực tiếp hình/bảng mới. Ví dụ tự tính lại cho kết quả (13,15),3,5.
- Rà cuối toán và mạch trên bản đã sửa đều kết luận đạt (final-math.json, final-flow.json). Kiểm tra bàn phím ở chế độ trình chiếu đạt. Màn hình hẹp 390×844 dùng chế độ cuộn tự động của Reveal, không lỗi công thức; phép thử ban đầu giả định mũi tên xuống chuyển ngay một slide đã được sửa để phù hợp chế độ cuộn. Đã xem ảnh hẹp.
- git diff --check đạt. Section mới chưa commit/push; commit/push trước thuộc lần hoàn tất section mô hình.

## Mở rộng ma trận chữ nhật theo yêu cầu
- Đổi A thành p×q, v có q phần tử, y có p phần tử; i chạy1..p, j chạy1..q, đủ pq bản ghi. Nguồn bổ sung: MMDS bài 2.3.2 trang40.
- Ví dụ đổi thành A=[[2,1],[0,3],[1,2]], v=[4,5], y=[13,15,14]. Bảng giữ đủ sáu tích và cặp trung gian; mỗi hàng một tác vụ Map. Sau Combine, Reduce nhận [13],[15],[14].
- Chứng minh xét p hàng, mỗi hàng q tích; thuật toán Map/Combine/Reduce giữ nguyên. Outline và storyboard đã đồng bộ. Các kết quả ví dụ 2×2 trong nhật ký trước đây là lịch sử đã được thay thế.
- Theo yêu cầu tiếp theo, thêm lưu trữ A theo khối có bản sao trên nhiều máy vào slide bài toán và hình slide đặc điểm. Nhãn khối giữ nhất quán giữa các máy; phân biệt bản sao lưu trữ với tác vụ chạy lại, không nhân đôi đóng góp toán học.
- Đổi giao diện ví dụ ma trận thành Map(B), mỗi lần gọi duyệt toàn bộ một khối; thay “phát” bằng yield trong đặc tả. Vết chạy đặt B1/B2/B3 là đầu vào; chứng minh dựa vào phân hoạch các bản ghi vào khối logic, không đếm bản sao.

## Bổ sung ba slide ứng dụng
- Theo yêu cầu, thêm một slide ứng dụng sau chứng minh từng bài, không thay thế năm slide cốt lõi. Tổng section3 thành20slide, toàn deck38slide.
- Đã kiểm chứng biểu diễn truy vấn/tài liệu bằng véc tơ và cosine từ IR6.3.1–6.3.2 trên trang Stanford chính thức. Chỉ chấm điểm theo lô, không khẳng định hệ tìm kiếm thực tế triển khai mỗi truy vấn bằng MapReduce.
- Writer OpenRouter requested/observed z-ai/glm-5.3-flash, provider OpenRouter, hồ sơ /tmp/lec02-applications/. Điều phối sửa thiếu data-slide-id, class và notes; đổi công thức sang KaTeX; bỏ khẳng định sai “chọn trang điểm cao chỉ bằng phép nhân”; giữ điều kiện chuẩn hóa trên mặt slide.
- Ứng dụng đếm từ chỉ cho số cột khi dùng toàn bộ từ vựng, không tự gán chỉ số. Ứng dụng trung bình giữ trang rỗng trong mẫu số; trạng thái(5,2) không phải đầu ra Reduce (đầu ra là2,5).
- Rà ma trận chữ nhật và hình khối nhân bản đã đạt qua rectangle-review; bổ sung nguồn lưu trữ MMDS2.1.2 trên slide bài toán.
- Reviewer cuối xác nhận đặc tả Map(B), ma trận chữ nhật và ba ứng dụng đạt; đã đưa điều kiện véc tơ khác0 lên mặt slide cosine. Kiểm tra Chromium38slide: không tràn, không lỗi JS/HTTP/KaTeX, bản in38trang; đã xem hình Map(B) và cả ba slide ứng dụng. git diff --check đạt. Chưa commit/push.

- Theo yêu cầu, đổi tiêu đề slide thành “Nhân ma trận–véc tơ: Ví dụ”; dùng A4×4, mỗi khối2×2. Giữ đủ16cặp Map trong bảng,8cặp Combine; Reduce nhận [5,4],[2,6],[2,7],[3,8], kết quả(9,8,9,11). Đồng bộ notes ứng dụng cosine và storyboard; đặc tả p×q không đổi.
- Theo yêu cầu mới, chuyển cả ba slide ứng dụng ngay sau phát biểu bài toán, trước đặc điểm/ý tưởng. Giữ mã slide, sửa các câu dẫn “ví dụ trước” để khớp thứ tự mới; cập nhật outline/storyboard.
- Vết chạy bốn khối đã được tự tính lại và reviewer OpenRouter xác nhận đạt; ảnh trình chiếu đã xem, không tràn/lỗi công thức. Kiểm tra thứ tự mới: cả ba ứng dụng nằm ngay sau bài toán; 38 mã slide duy nhất.
- Rà mạch độc lập trên bản đủ20slide xác nhận thứ tự mới và các tham chiếu trước/sau đều đạt. Gói rà lần đầu bị cắt do chọn sai điểm kết thúc HTML; đã sửa gói và chạy lại, không dùng kết luận trên gói thiếu. Chưa commit/push.


## Section 4 — Chi phí và lợi ích của song song hóa (2026-09-16)

- Phạm vi theo yêu cầu: thêm section sau Các ví dụ, cập nhật Nội dung, index và ba tệp quy trình. Hệ thống vẫn ở mức kế hoạch; không phục hồi deck cũ hoặc tự tạo ghi chú/recitation.
- Hai reader OpenRouter lập kế hoạch và ánh xạ nguồn độc lập; requested_model/observed_model đều `z-ai/glm-5.3-flash`, provider `OpenRouter`. Hồ sơ `/tmp/lec02-cost/plan.json`, `source.json` và `design.md`.
- Điều phối duyệt 11 slide: ba đại lượng → tổng công việc → lịch chạy → cộng 16 số → chi phí đầu vào tác vụ → độ trễ/băng thông → đường nối rack dùng chung → Combine → tổng runtime → tăng tốc → kiểm tra. Tách quy ước MMDS và tăng tốc để mỗi slide giữ một việc chính.
- Đối chiếu sách MMDS 2.5.1–2.5.2 và slide MMDS 38–40/Stanford 67–70: sách đếm đầu vào, slide đếm tổng I/O. Giữ C=I+H theo sách; phân biệt C với V qua mạng. Bác nhận xét planner “Combine không đổi C”: khi H giảm, C cũng giảm. Bác nhận xét source “MMDS không bàn nghẽn rack”: mục 2.1.1 bàn đường nối rack dùng chung; ví dụ số là áp dụng mô hình, không trích số đo nguồn.
- Đọc bổ sung nguồn Cornell CS5220 chính thức cho mô hình một thông điệp độ trễ cộng lượng dữ liệu chia băng thông và định nghĩa tăng tốc. Đổi ký hiệu độ trễ thành lambda để tránh L của Reduce; dùng P cho số máy để tránh p số hàng ma trận. Không dùng cấu hình băng thông lịch sử trong sách làm thông số hiện tại.
- Dữ kiện nhỏ do người soạn chọn để minh họa phép tính theo mạch đã trao đổi; không gán là benchmark hoặc bài tập nguyên văn. Giữ giả thiết quyết định trên mặt slide và diễn giải phạm vi trong notes. Số section hiện tại ngoài 5–7 được giữ theo ngoại lệ xây bài từng phần do người dùng chỉ đạo.

### Rà và chỉnh sửa section 4

- Writer, năm reviewer độc lập (sinh viên, giải thuật, toán, giảng dạy, mạch), reviewer storyboard và editor riêng đều dùng OpenRouter; các lượt hoàn tất có requested_model/observed_model `z-ai/glm-5.3-flash`, provider `OpenRouter`. Hồ sơ `/tmp/lec02-cost/`. Không đọc hoặc đưa bí mật vào các gói nội dung.
- Lượt sinh bản nháp có phản hồi chưa hoàn chỉnh `finish_reason: "error"`; cầu nối tự thử lại trong cùng phiên và hoàn tất. Reviewer storyboard đầu dừng với lỗi nguyên văn `model exceeded the tool-call limit (30)`; đã chạy lại cùng vai/nhà cung cấp với nội dung đóng gói. Không dùng báo cáo thiếu làm bằng chứng đạt.
- Các báo cáo đầu phát hiện thang hình thời gian sai, sơ đồ chi phí thiếu Reduce, ký hiệu n/H chưa rõ, nhãn thừa, notes chứa thời lượng, dữ kiện câu hỏi dày và tổng thời lượng chưa khớp. Điều phối bổ sung lỗi công thức tràn ngang khi xem ảnh, giả thiết còn chỉ nằm trong notes và một số lời diễn giải không chính xác.
- Đã dựng lại sáu SVG có mã tái tạo: lịch tác vụ, cộng song song, đầu vào tác vụ, rack dùng chung, lịch toàn công việc và tăng tốc. Tỷ lệ lần lượt kiểm bằng tọa độ: lịch pha 150 px/giây, cộng 60 px/đơn vị tau, lịch công việc 100 px/giây, so sánh 38 px/giây. Phân biệt rõ bốn máy cộng cục bộ và chỉ một máy gộp; bỏ câu “9 tau nhàn rỗi” sau khi công việc đã hoàn thành.
- Điều phối không chấp nhận kết luận chung “đúng tỷ lệ/đủ giả thiết” của tác tử khi mã và ảnh còn trái kết luận. Sau editor, đã đưa giả thiết lên mặt slide, sửa notes về khởi tạo bằng 0, xóa diễn giải sai về cận tăng tốc, tách công thức dài và định nghĩa ký hiệu trước khi dùng. Nguồn Cornell Performance basics đã được mở và kiểm chứng; không áp dụng đề xuất đổi sang nguồn Intro to Message Passing cho định nghĩa tăng tốc.
- Câu hỏi cuối dùng bảng dữ kiện và ba nhiệm vụ. Nêu rõ bỏ độ trễ và chi phí nhóm trong bài tính, đọc/ghi đã nằm trong Map/Reduce; đáp án 11 giây/2 lần, sau Combine 10 giây/2,2 lần. Phân biệt giảm lượng truyền 20% với giảm thời gian; C cũng giảm khi H giảm.
- Storyboard tính đúng tổng 27,5 phút. Mục lục có bốn phần, index mô tả nội dung hiện tại. Giữ nguyên nội dung 37 slide cũ ngoài mục lục; chỉ thêm 11 slide và CSS giới hạn trong các lớp mới. Ngoại lệ bốn section do xây bài từng phần vẫn áp dụng.
- Biên tập theo no-ai-slop: bỏ câu hỏi tu từ và nhãn quy trình, Việt hóa lời giải thích, cắt chú thích lặp; giữ đủ dữ kiện và giả thiết. Rà theo quill: W/T trước C/V, một đường truyền trước đường dùng chung, Combine trước tổng runtime, runtime trước tăng tốc; giữ P số máy và lambda độ trễ để tránh trùng ký hiệu ở các phần trước. Không tạo quill.json.
- Kiểm tra số học độc lập bằng Python: mọi phân hoạch đều với 1≤P≤n≤64; W=n−1 và T=(n/P+P−2)tau, kể cả P=1 và P=n. Kiểm lại lịch tải, lượng truyền, Combine và đáp án bài kiểm tra. Reviewer toán cuối xác nhận công thức và cả sáu hình đúng; reviewer sinh viên cuối xác nhận ký hiệu, giả thiết và bài tính áp dụng được.
- Kiểm định Chromium cục bộ: 49 slide, bốn section ngoài, mã duy nhất, notes đủ ở 11 slide mới, đường dẫn tài sản hợp lệ, không lỗi JavaScript/HTTP/KaTeX. Đã mở và xem ảnh của cả 11 slide mới; kiểm biên cả phần tử KaTeX, nhãn SVG và hình. Sáu SVG không có nhãn ra ngoài viewBox. Bản in có 49 trang.
- Bàn phím chuyển đúng từ cuối phần Ví dụ sang phần Chi phí, rồi xuống slide tiếp. Màn hình 390×844 dùng chế độ cuộn mặc định của Reveal, không tràn ngang hoặc hỏng hình/công thức; bố cục 16:9 được thu nhỏ nên đọc trên điện thoại cần phóng to. Index hiển thị đúng trên màn hình hẹp.
- Giới hạn công cụ: không đồng bộ/rà trong Codex Slides; tiếp tục dùng bản RevealJS và Chromium cục bộ theo giới hạn egress đã ghi trước. Không tuyên bố đã kiểm định trong Codex Slides.

- Rà cuối mạch (`final-flow.json`) trên 11 slide, hai slide lân cận và storyboard xác nhận đạt; tổng thời lượng 27,5 phút và kết nối vào–ra nhất quán. Rà cuối toán và sinh viên cũng đạt. Đã kiểm lại sau bổ sung số phần và làm rõ tổng số cặp trong bảng Combine: 49 slide/49 trang in, không tràn hay lỗi công thức/tài nguyên.
