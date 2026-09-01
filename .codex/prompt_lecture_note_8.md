# Prompt xây dựng ghi chú Bài 08

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 08 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng MMDS Chương 4 mục 4.1–4.3 làm trục; đối chiếu `mmds/ch04-streams1.pdf`, `mmds/ch04-streams2.pdf`, `stanford-cs246/16-streams.pdf` và `stanford-cs246-2017/streams-2.pdf`.
- Phạm vi gồm mô hình dòng một lượt, lấy mẫu nhất quán theo khóa, lấy mẫu hồ chứa và Bloom filter.
- Recitation chỉ dùng trực tiếp MMDS 4.2.1 và 4.3.1–4.3.3. Không tự tạo bài hồ chứa, không thêm Rejection Sampling, Flajolet–Martin, moment, DGIM hoặc cửa sổ trượt.
- Giữ đúng ký hiệu, giả thiết xác suất, bất biến và ranh giới giữa công thức chính xác với xấp xỉ.

## Tệp đầu ra

- `.codex/goal_lecture_8.md`;
- `2627-1/materials/lec-08/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-08/{outline,storyboard,review-log}.md`;
- chỉ dùng sáu SVG hiện có trong `2627-1/img/lec-08/`, trừ khi nguồn buộc phải có thêm hình;
- cập nhật mục Bài 08 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
