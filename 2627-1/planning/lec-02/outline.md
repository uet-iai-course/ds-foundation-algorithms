# Dàn ý Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Mục tiêu và phạm vi — 2026-09-15

Bài 02 theo thứ tự đề xuất của sources/source.md, từ buổi gốc 4; nguồn MMDS Chương 2, ch2n.pdf. Sinh viên năm 2 đã học lập trình, toán rời rạc và đại số tuyến tính; chưa học CSDL. Sau bài, sinh viên mô tả miền vào–ra của hai hàm, chạy vết và viết giả mã đếm từ/nhân ma trận–vector, giải thích tính đúng và tính chi phí từ đầu vào tác vụ.

Theo yêu cầu mới, bỏ đại số quan hệ và thuật toán nối, cùng ví dụ chi phí và câu hỏi phụ thuộc. Giữ 9 section: mở đầu và 2.1–2.8 theo PDF, ngoại lệ quy tắc 5–7. 50 trang giảng, 8 trang bài tập; 120 + 60 phút thiết kế dự kiến. Không thay dữ kiện hoặc tạo bài tập ngoài nguồn.

## Bản đồ chủ đề

| Chủ đề | Vai trò và tiên quyết | Nguồn | Quyết định |
|---|---|---|---|
| Hệ tệp phân tán | Giới hạn một máy → dữ liệu chia khối cho Map | 2.1 | Giữ |
| Lợi ích và cơ chế | Cụm máy → lợi ích → động lực đọc hai hàm | MMDS trang 21–22,25–30; slide 24–25 | Thêm một bảng đối chiếu sau mở mục 2.2 |
| Hai hàm và nhóm khóa | Vòng lặp,tổng → vết → chữ ký → sơ đồ → giả mã/đúng | 2.2.1–2.2.3 | Thêm formal và hình cầu nối sau ví dụ |
| Gộp, phân công, chạy lại | Đếm từ → tạo tác vụ → phân khóa → gán máy → nơi lưu → phục hồi | 2.2.4–2.2.6 | Mở rộng 2 trang thành 7 trang, thêm 5 sơ đồ |
| Ma trận–vector | Nhân hàng với vector → gom theo hàng → chia dải | 2.3.1–2.3.2 | Giữ |
| Quan hệ và nối | Cần tiên quyết CSDL chưa học | 2.3.3–2.3.10 | Bỏ theo yêu cầu |
| Spark/luồng công việc | Một công việc → chuỗi phụ thuộc, tính lại | 2.4.1–2.4.3 | Giữ; các mở rộng khác đọc thêm |
| Chi phí | Thuật toán → nơi đọc/nhận → bảng → tổng → điều kiện | 2.5.1–2.5.2; Bài 2.5.1a | Giữ đếm từ; thêm đọc dải từ lời giải nguồn |
| Chi phí nối | Phụ thuộc thuật toán đã bỏ | 2.5.3 | Bỏ |
| Bộ nhớ và sao chép | Tải tác vụ → các cặp ảnh → phân công nhóm | 2.6.1–2.6.2 | Giữ; cận dưới 2.6.3–2.6.7 đọc thêm |
| Tổng kết và nguồn | Kiểm tra đúng mục tiêu đã học | 2.7–2.8 | Tự kiểm tra không dùng Links/nối |

## Quyết định điều phối

Giữ đề xuất formal và hình đếm từ của planner. Bác đề xuất giữ chi phí nối sau khi bỏ thuật toán vì tạo tiên quyết ngầm; không thay bảng bằng định nghĩa quan hệ trừu tượng khác. Bác số lượng 61 slide cố định và các bài tập ngoài nguồn do planner đề xuất. Số trang giảm để dành thời gian theo dõi vết và tự giải thích các bước. Hồ sơ nguồn đầu bị cắt đã được bổ sung; Reduce có thể phát 0 hoặc nhiều cặp khác kiểu được xác nhận trực tiếp ở 2.2.3. Không suy ra bảo đảm thứ tự từ chữ ký danh sách; đếm từ dùng phép cộng không phụ thuộc thứ tự.

Recitation giữ 2.2.1(a–c): 15 phút; 2.3.1(a–d): 20 phút; 2.5.1(a): 25 phút. Bỏ 2.5.1(c). Thời gian ý (a) gồm tự lập bảng, trình bày và đối chiếu điều kiện; không sửa yêu cầu toán học.

## Thuật ngữ và ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| $K_i,V_i$ | Miền khóa/giá trị; 1 đầu vào, 2 trung gian, 3 đầu ra |
| $\operatorname{List}(X)$ | Danh sách hữu hạn, giữ lặp, có thể rỗng |
| reducer / tác vụ / máy | Một lần xử lý khóa / đơn vị lập lịch / nơi thực thi |
| $M,v,x$ | Ma trận, vector vào, vector ra |
| $z,L_j,a_j$ trong chi phí | Số phần tử lưu, độ dài dải, số tác vụ đọc dải; j đánh số dải |
| $I,M$ trong chi phí | Kích thước đầu vào Map và Reduce; M ở đây không là ma trận |
| $q,\rho$ | Đầu vào tối đa/reducer; mức sao chép trung bình |
| $s,\tau$ trong phần ảnh | Hàm độ tương tự đối xứng và ngưỡng |

## Cách thể hiện và kiểm định

Áp dụng slide_authoring_standard.md; một luận điểm/trang, vết trước hình thức hóa, bảng đếm trước kết luận chi phí. Hai chữ ký là hai phần của một giao diện nên cùng trang để đối chiếu kiểu trung gian. Sơ đồ riêng làm rõ bước hệ thống giữa hai hàm. Ghi chú mở rộng lập luận, không sao chép slide.

Đầu ra: HTML, 13 SVG được dùng, lecture-note, storyboard, outline, review-log, index. Hai tài sản phép nối cũ giữ để truy nguyên nhưng không nhúng. Kiểm tra 58 ID khớp storyboard, 9 section, 120 + 60 phút; năm vai độc lập và storyboard, biên tập riêng; trình duyệt thực, công thức, ảnh, liên kết, bàn phím và bản in. Kết quả và giới hạn ghi ở review-log.md.

## Nguồn và tham khảo cách dạy

Nguồn nội dung quyết định: `sources/textbooks/ch2n.pdf`, 60 trang PDF, trang in 20–79. Bản đồ học phần và slide tham khảo đã được kiểm kê trong giai đoạn đầu; MMDS/Stanford chỉ đối chiếu, không quyết định cấu trúc thay chương sách. Tham khảo `../math-4-AI/2627-1/` lecture 01–03 ở mức một ý trung tâm, ví dụ trước ký hiệu, nhịp hình–giải thích–kiểm tra; không chuyển nội dung toán của môn đó sang bài này. Mẫu kỹ thuật: `2627-1/lecture-template.html` và `lecture-style.css`. Đường dẫn kho machine-learning được quy định trong AGENTS không có tại môi trường này; áp dụng các nguyên tắc đã nêu trong AGENTS.

## Mở rộng thực thi và phục hồi — 2026-09-15

Giữ kế hoạch phân biệt hàm/tác vụ/tiến trình/máy; tách tạo Map từ dữ liệu, phân khóa cho Reduce và phân bổ lên máy. Bác “mỗi khối bắt buộc một Map” của planner: nguồn chỉ nêu lựa chọn hợp lý; một tác vụ có thể nhận một hoặc nhiều khối. Bác mốc 60 phút mà planner suy ra: toàn bài vẫn 120 phút giảng và 60 phút recitation. Phần 2.2 tăng từ 26 lên 36 phút; 2.3/2.4/2.5/2.6 còn 17/13/18/15 phút. Không thay bài tập.

Các tình huống phục hồi độc lập: Map 0 trên A mất đầu ra cục bộ → giao E đọc lại D1; Reduce 1 trên D đang chạy bị lỗi → giao F đọc tệp Map còn tồn tại. Giữ kết quả Reduce 0 đã hoàn tất. Master phát hiện bằng kiểm tra định kỳ, không đặt timeout ngoài nguồn; Master hỏng cần khởi động lại công việc theo mô hình sách. Thay chữ “người viết” trong hình luồng bằng “lập trình viên định nghĩa”.

## Bổ sung lợi ích theo yêu cầu

Năm lợi ích được diễn đạt bằng cơ chế, không dùng lời quảng bá hay giả định tăng tốc tuyến tính. Giữ đề xuất vị trí/bảng của planner; bác câu chốt nói về việc dạy sinh viên và cụm “đũa thần”. Ở lần bổ sung lợi ích, sửa số lượng planner còn giữ53 thành54trang. Source reader diễn đạt lại “restart Master” chưa đủ: giới hạn MMDS là khởi động lại toàn bộ công việc khi máy bộ điều phối hỏng. Năm video người dùng đưa không truy cập được; dùng MMDS làm nguồn chính, bài báo gốc Dean–Ghemawat2004 xác minh thêm. Không coi nội dung video là đã được kiểm chứng. Phần2.2 vẫn36phút; slide mới lấy2phút từ hai trang đã có.

## Bổ sung đặc tả và đánh giá — kế hoạch được duyệt


Bốn trang dự kiến: đặc tả đếm từ sau sơ đồ hai hàm; thao tác đếm từ sau chứng minh; công việc/bộ nhớ ma trận–vector sau chia dải; số phép so sánh ảnh sau chứng minh bao phủ. Cập nhật giả thiết biểu diễn và đầu ra ngay trong cụm thuật toán. Giữ 9 section, thêm 4 trang thành 58 (50 giảng,8 recitation), 120+60 phút.

Bản đồ bao phủ: đếm từ có đặc tả mới, giả mã/đúng hiện có, đếm thao tác mới và byte mục2.5; combiner có điều kiện đúng hiện có, bổ sung số tổng cục bộ theo tác vụ và bộ nhớ trong ghi chú; ma trận–vector có đặc tả/giả mã/đúng hiện có, thêm điều kiện tọa độ duy nhất, mới công việc/bộ nhớ, tiếp dùng mô hình đọc dải ở2.5; cặp ảnh có đặc tả i<j, Map/Reduce và bao phủ, mới bảng đếm so sánh, giữ q/rho/byte; bài2.3.1 có đánh giá trong lời giải. Spark là phép biến đổi của hệ thống, không thêm bài toán hoặc thuật toán ngoài nguồn.

Đối chiếu nguồn: bác số phép cộng T−D, z−n do source reader suy ra vì giả mã đang khởi tạo0 rồi cộng mọi giá trị. Bác gộp toàn công việc chỉ còn D từ: bộ kết hợp cục bộ theo tác vụ, số gửi phải cộng các số từ phân biệt của từng tác vụ. 2.2.4 ở trang27–28, không phải31. Không dùng metadata ấn bản mà worker tự đoán. Giữ số lần so sánh chính xác N(N−1)/2, không dùng xấp xỉ10^12 trong báo cáo reader. Mọi đánh giá mới ghi là suy ra từ giả mã, không trích nguyên văn sách.

Phân bổ dự kiến: mở5;2.1=8;2.2=38;2.3=20;2.4=10;2.5=15;2.6=18;2.7=5;2.8=1. Bài tập60 giữ nguyên. Không thay nội dung hoặc CSS chung; không cần SVG mới vì phép đếm dùng bảng HTML. Nội dung chuẩn bị trong /tmp, chưa tích hợp trước khi kế hoạch và bản soạn được kiểm tra.

Điều phối chấp nhận hướng bổ sung ba loại chi phí của planner, điều chỉnh thành bốn trang tập trung như trên. Bác bảng tổng hợp thêm ở phần kết vì lặp; bác gộp giả mã và ba loại chi phí lên một trang. Bác khẳng định combiner không đổi số phép cộng và qB là bộ nhớ phụ: phụ thuộc cài đặt; qB là vùng đầu vào. Bác các mức trừ thời gian lớn hơn thời gian slide hiện có. Giữ mô tả Map/Reduce nhóm ảnh đã đủ các bước; bổ sung đặc tả và phép đếm thay vì đổi cú pháp thành mã cho có. Kế hoạch được duyệt để soạn.
