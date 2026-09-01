# Prompt xây dựng ghi chú Bài 09

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 09 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng MMDS Chương 4 mục 4.4–4.7 làm trục; đối chiếu hai bộ slide MMDS, Stanford CS246 hiện hành và 2017. Chỉ dùng UMass CS514 Lecture 10 cho Count-Min Sketch.
- Phạm vi gồm Flajolet–Martin cho $F_0$, Count-Min Sketch trên dòng chỉ tăng, mômen và AMS cho $F_2$, DGIM cho cửa sổ bit, cùng tổng suy giảm mũ ở mức cầu nối.
- Không dạy cơ chế HyperLogLog chuẩn; không mở rộng Count-Min sang cập nhật âm, không triển khai biến thể DGIM sai số tùy ý hoặc thuật toán tìm khóa nặng.
- Recitation chỉ dùng trực tiếp MMDS 4.4.1, 4.5.1, 4.5.3, 4.6.1 và 4.6.3. Giữ nguyên dữ kiện, yêu cầu và nguồn.
- Giữ đúng mô hình ngẫu nhiên, thứ tự gộp FM, tính không chệch của AMS, bất biến/cận sai số DGIM và ranh giới giữa bảo đảm xác suất với trực giác.

## Tệp đầu ra

- `.codex/goal_lecture_9.md`;
- `2627-1/materials/lec-09/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-09/{outline,storyboard,review-log}.md`;
- chỉ dùng chín SVG hiện có trong `2627-1/img/lec-09/`, trừ khi nguồn buộc phải có thêm hình;
- cập nhật mục Bài 09 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
