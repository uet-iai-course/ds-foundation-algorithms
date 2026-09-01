# Prompt xây dựng ghi chú Bài 14

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 14 — Chỉ mục văn bản và chỉ mục không gian**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 14 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng *Database System Concepts* 7e, Chương 31 làm trục cho chỉ mục đảo; Chương 24 cho R-tree; Cornell CS5780 cho kd-tree và ball tree; Auburn COMP7120 cho Z-order và cách dùng B+-Tree để quét đoạn Morton.
- Phạm vi gồm danh sách đảo và phép trộn Boolean, vị trí–tần suất, precision/recall, mô hình lọc–tinh lọc, R-tree, truy vấn 1-NN chính xác trên kd-tree và ball tree, dựng ball tree Euclid, Z-order và giới hạn của tuyến tính hóa không gian.
- Giữ thuật ngữ, ký hiệu, giả thiết, ví dụ và thứ tự khái niệm đã được kiểm định trong planning/deck. Phân biệt metric tổng quát của truy vấn ball tree với phép dựng Euclid; phân biệt chi phí RAM với I/O trang.
- Recitation dùng trực tiếp Bài 31.2 của Chương 31 ấn bản 7 và Bài 25.2–25.3 cùng lời giải chính thức ấn bản 6. Không đổi dữ kiện; ghi rõ phần lời giải đống của 31.2 do bài giảng triển khai từ đề và các điều kiện bổ sung cho 25.3.
- Không mở rộng sang tìm kiếm xấp xỉ, HNSW/PQ, xếp hạng học máy, chèn–tách R-tree hay thuật toán Hilbert curve ngoài nguồn.

## Tệp đầu ra

- `.codex/goal_lecture_14.md`;
- `2627-1/materials/lec-14/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-14/{outline,storyboard,review-log}.md`;
- dùng các SVG hiện có trong `2627-1/img/lec-14/`, chỉ thêm hình khi thật sự cần và có nguồn;
- cập nhật mục Bài 14 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
