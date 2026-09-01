# Prompt xác định goal ghi chú Bài 02

Hãy xác định goal cho việc xây dựng ghi chú bài giảng của **Bài 02 — MapReduce và ngăn xếp xử lý dữ liệu lớn**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa bộ trang chiếu và chưa cập nhật `index.html`.

## Đầu vào đã xác định

- Bài: `02 — MapReduce và ngăn xếp xử lý dữ liệu lớn` theo thứ tự đề xuất.
- Tệp trang chiếu hiện có: `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html`.
- Ghi chú đích: `2627-1/materials/lec-02/lecture-note.md`.
- Mức độ: `đầy đủ`.
- Đối tượng: sinh viên đại học đã học Bài 01, ánh xạ khóa–giá trị, bảng băm, phép nhóm, bất biến vòng lặp và độ phức tạp cơ bản.
- Yêu cầu riêng: ghi chú phải đọc độc lập với trang chiếu; dùng cùng ký hiệu và mạch khái niệm; mở rộng đặc tả, vết chạy, tính đúng, điều kiện dùng bộ kết hợp, lệch tải, khôi phục tác vụ và mô hình chi phí khi nguồn hỗ trợ.
- Giới hạn: chỉ xác định goal và kế hoạch; không tạo nội dung ghi chú, không sửa HTML, SVG, planning hoặc index ở bước này.

`Đầy đủ` yêu cầu mọi chủ đề cốt lõi có đủ thành phần áp dụng trong khuôn trình bày, mọi mệnh đề kỹ thuật có nguồn, ví dụ quan trọng được tính lại, thuật toán có đặc tả–tính đúng–chi phí và mỗi cụm có câu hỏi tự kiểm tra. Mức này không cho phép tự thêm chủ đề hoặc mở rộng sang bài khác.

## Phạm vi sơ bộ phải kiểm chứng

Goal phải phục vụ các sản phẩm học tập sau:

1. mô tả đúng ba giai đoạn map, nhóm theo khóa và reduce; phân biệt phần người dùng viết với phần hệ thống thực hiện;
2. đặc tả chương trình MapReduce đếm từ, chạy tay trên dữ liệu nhỏ và chứng minh tính đúng;
3. nêu điều kiện dùng bộ kết hợp, phân tích phân vùng, lệch tải, số Map task và Reduce task;
4. giải thích điều phối, chạy lại tác vụ, tính quyết định hoặc tính an toàn khi chạy lại và giới hạn của cơ chế chịu lỗi;
5. phân biệt quy ước đầu vào tác vụ $I+M$ trong sách MMDS với quy ước vào/ra $I+2M+O$ trong slide MMDS;
6. định vị hệ tệp phân tán, Hadoop MapReduce, DAG và Spark trong ngăn xếp; xác định khi nào MapReduce theo lô phù hợp hoặc không phù hợp.

Không đưa PageRank, phép nối, nhân ma trận–vector, đại số quan hệ hoặc lịch sử API Hadoop vào tuyến chính. Bài tập chỉ dùng trực tiếp MMDS Bài 2.2.1(a–c), trang in 30, PDF trang 11 và Bài 2.3.1(a–d), trang in 40, PDF trang 21; không đổi dữ kiện hoặc yêu cầu toán học.

## Nguồn bắt buộc phải đọc

1. `AGENTS.md`.
2. Mục Bài 02 và các phần liên quan trong `sources/source.md`: năm mạch học tập, tình huống dữ liệu phân tán, mục tiêu–tiên quyết–học liệu, thứ tự đề xuất và ánh xạ từ phần MapReduce của buổi gốc 4.
3. Dòng `Buổi đề xuất 2` trong `sources/reference-slides/README.md`.
4. `sources/textbooks/mmds-3e-ch02-mapreduce.pdf`, đọc toàn Chương 2; ưu tiên mục 2.1, 2.2.1–2.2.6, 2.4, 2.5.1, Bài 2.2.1 và 2.3.1. Kiểm tra trực tiếp trang in 21–30, 40–55 và ánh xạ trang PDF.
5. `sources/reference-slides/mmds/ch02-mapreduce.pdf`, đọc toàn bộ; ưu tiên trang chiếu 2–35 và 38–40. Slide 36–37 về phép nối và 43–48 về phần mềm cũ chỉ dùng để xác nhận ngoài phạm vi.
6. `sources/reference-slides/stanford-cs246/01-intro.pdf`, đọc toàn bộ; ưu tiên trang chiếu 50–60 và 66 cho DAG, Spark và giới hạn của MapReduce theo lô.
7. `2627-1/planning/lec-02/outline.md`, `storyboard.md`, `review-log.md`, năm SVG trong `2627-1/img/lec-02/` và bộ trang chiếu hiện có của Bài 02.
8. `2627-1/material-viewer.html`, `material-viewer.css`, `material-viewer.js`, `material-index.css`, các mẫu trong `materials/_templates/` và `2627-1/index.html`.
9. `openrouter-mcp/README.md` để kiểm tra tên lệnh, quyền của từng vai và `task-profile`.

Với từng cụm, so sánh slide chính thức MMDS và Stanford theo mức khớp mục tiêu, độ chính xác, ví dụ hoặc hình và khả năng Việt hóa. Dùng sách MMDS để kiểm chứng. Nếu hai nguồn tương đương, ưu tiên MMDS; nếu chọn Stanford cho DAG hoặc Spark, ghi lý do cụ thể. Không sao chép CSS, phông chữ hoặc tài sản nhị phân của nguồn.

## Cách điều phối

Người dùng cho phép gửi tới OpenRouter nội dung các tệp cần thiết trong workspace để thực hiện nhiệm vụ, ngoại trừ `.env`, `.env.*`, khóa, token, mật khẩu, cookie, khóa riêng, thông tin xác thực và mọi giá trị bí mật. Không đọc, đưa vào prompt hoặc log các nội dung bị loại trừ.

1. Từ `openrouter-mcp/`, chạy song song khi đầu vào ổn định:
   - `uv run openrouter-mcp-reader --repo-root .. --json --task-profile plan "Lập kế hoạch hẹp cho goal ghi chú Bài 02; không sửa tệp."`;
   - `uv run openrouter-mcp-reader --repo-root .. --json --task-profile source "Kiểm kê và ánh xạ nguồn hẹp cho ghi chú Bài 02; không sửa tệp."`.
2. Reader lập kế hoạch xác định mục tiêu, đối tượng, phạm vi, đầu ra, tiêu chí hoàn thành, rủi ro và quan hệ tuần tự–song song.
3. Reader nguồn kiểm kê định nghĩa, ví dụ, hình, mệnh đề, thuật toán, chứng minh, bài tập, nguồn và khoảng trống. Phân biệt mệnh đề nguồn với quyết định biên tập.
4. Giao một reviewer độc lập lập bản đồ chủ đề. Mỗi chủ đề nhận nhãn `cốt lõi`, `cầu nối`, `bổ sung` hoặc `đọc thêm`, kèm nguồn, vai trò, kiến thức đầu vào, sản phẩm học tập, kết nối vào–ra và tác động phạm vi.
5. Codex chính kiểm tra metadata runtime, đối chiếu báo cáo với nguồn, bác đề xuất thiếu căn cứ rồi hợp nhất thành `.codex/goal_lecture_2.md`. Không giao writer trước khi goal được chấp nhận.

Nếu worker OpenRouter lỗi, dừng giai đoạn phụ thuộc và báo nguyên văn lỗi; không đổi ngầm sang model, nhà cung cấp hoặc tác tử khác.

## Điểm cần phân tích trong bản đồ chủ đề

- Kho dữ liệu phân tán và nhu cầu đưa tính toán đến dữ liệu: khối, bản sao, vị trí dữ liệu và giới hạn truyền mạng.
- Hệ tệp phân tán và ranh giới trách nhiệm giữa người dùng, môi trường MapReduce và hệ thống lưu trữ.
- Luồng khóa–giá trị: map, nhóm theo khóa, reduce, Map task, Reduce task, mapper và reducer.
- Word Count: đặc tả, quy tắc tách từ, vết chạy, giả mã, điều kiện dừng, bất biến hoặc lập luận đếm, biên và chi phí.
- Bộ kết hợp: tính đóng, cùng ngữ nghĩa, kết hợp, giao hoán, cây gộp và phản ví dụ khi không an toàn.
- Phân vùng và lệch tải: hàm phân vùng $p(k)$, một khóa về một Reduce task, tải trong task và khả năng lập lịch nhiều task trên máy.
- Chịu lỗi: trạng thái tác vụ, chạy lại, đầu ra trung gian, tính quyết định và hiệu ứng ngoài.
- Hai quy ước chi phí với $I,M,O$: $I+M$ và $I+2M+O$ đo hai đại lượng theo hai quy ước nguồn; không gọi cả hai là byte mạng.
- DAG, Spark và giới hạn của chuỗi MapReduce theo lô; chỉ định vị, không biến bài thành hướng dẫn phần mềm.
- Bài tập MMDS 2.2.1 và 2.3.1: đề, gợi ý, lời giải và kiểm tra giả thiết; giữ nguyên dữ kiện nguồn.

Với mỗi chủ đề, đánh dấu các thành phần áp dụng trong chuỗi `vai trò và nhu cầu → định nghĩa hoặc đặc tả → ví dụ chạy tay → trực quan hoặc hình học → định lý hoặc mệnh đề → thuật toán → chứng minh → ứng dụng, lỗi dễ mắc và kiểm tra`. Ghi `không áp dụng` kèm lý do; không tạo đề mục rỗng.

## Đầu ra bắt buộc

Tạo `.codex/goal_lecture_2.md` bằng tiếng Việt với đúng 13 mục:

1. `Goal`.
2. `Vấn đề trung tâm`.
3. `Bằng chứng hoàn thành`.
4. `Đầu ra`.
5. `Đối tượng và tiên quyết`.
6. `Phạm vi nguồn`.
7. `Bản đồ chủ đề` có `note-topic-id` duy nhất.
8. `Chủ đề bổ sung đề xuất`.
9. `Khuôn trình bày`.
10. `Ngoài phạm vi`.
11. `Rủi ro và điểm cần duyệt`.
12. `Kế hoạch tác tử`.
13. `Trạng thái`.

Goal phải đo được độ bao phủ, tính đúng, khả năng truy nguyên nguồn, tính liên tục và khả năng đọc độc lập với trang chiếu. Chỉ ghi `sẵn sàng soạn` khi nguồn và phạm vi đủ, mọi trang hoặc slide được dùng đã được kiểm tra trực tiếp và mọi chủ đề bổ sung được đưa vào có nguồn đã xác minh. Nếu không, ghi `bị chặn` cùng một yêu cầu cụ thể. Không tạo `quill.json`.
