# Prompt xây dựng ghi chú Bài 10

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 10 — Nén dữ liệu không mất thông tin**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 10 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng Nelson–Gailly, *The Data Compression Book*, Chương 3–5 làm trục; đối chiếu slide Stanford EE398A, Stanford CS106B và CMU 15-499 đã ánh xạ.
- Phạm vi gồm mã tiền tố và Kraft; Huffman tĩnh; Huffman thích nghi đúng biến thể Nelson–Gailly với `ESCAPE`, `EOS`, tính chất anh em, phép đổi và dựng lại; mã hóa số học với khoảng nửa mở, giải mã, kết thúc và chuẩn hóa hữu hạn; tự thông tin và entropy ở mức giải thích chi phí.
- Không trộn biến thể Huffman thích nghi với FGK, Vitter, nút NYT hoặc thuật ngữ không thuộc nguồn trục. Không mở sang Lempel–Ziv hoặc nén mất dữ liệu của Bài 11.
- Recitation giữ ba bài đã được phê duyệt trong planning ngày 2026-08-28: hai ví dụ Nelson–Gailly được chuyển thành bài luyện và CMU Assignment 1a Problem 3. Không đổi dữ kiện, yêu cầu toán học hoặc nguồn.
- Giữ rõ điều kiện giải mã duy nhất, đồng bộ hai phía, quy tắc kết thúc, khoảng nửa mở, sự khác nhau giữa tự thông tin của chuỗi với entropy của phân phối và ranh giới giữa mô hình lý tưởng với cài đặt số nguyên hữu hạn.

## Tệp đầu ra

- `.codex/goal_lecture_10.md`;
- `2627-1/materials/lec-10/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-10/{outline,storyboard,review-log}.md`;
- chỉ dùng chín SVG hiện có trong `2627-1/img/lec-10/`, trừ khi nguồn buộc phải có thêm hình;
- cập nhật mục Bài 10 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
