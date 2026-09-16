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
