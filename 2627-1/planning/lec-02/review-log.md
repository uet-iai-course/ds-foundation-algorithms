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
