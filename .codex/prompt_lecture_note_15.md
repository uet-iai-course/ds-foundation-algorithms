# Prompt xây dựng ghi chú Bài 15

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 15 — Thuật toán kết nối dữ liệu**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 15 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng *Database System Concepts* 7e, Chương 15 làm trục. Phạm vi gồm Nested-Loop Join theo tuple, Block Nested-Loop Join, Indexed Nested-Loop Join, Sort-Merge Join, Hash Join trong bộ nhớ và Grace Hash Join.
- Giữ mô hình chi phí, ký hiệu, dữ kiện `student/takes`, bố trí bộ đệm, điều kiện bộ nhớ, ví dụ Grace khả thi và các sửa lỗi nguồn đã được kiểm định trong planning/deck.
- Phân biệt lần truyền khối với seek; không cộng chi phí ghi kết quả cuối. Phân biệt $q=M-2$ khi giữ bộ đệm đầu ra với $q=M-1$ khi đầu ra được chuyển tiếp. Không dùng kích thước trung bình phân hoạch thay cho điều kiện cực đại.
- Recitation dùng trực tiếp Bài 15.3–15.5 trong Practice Exercises Chương 15 và đối chiếu Practice Solutions. Không đổi dữ kiện hoặc yêu cầu; ghi rõ các giả thiết vật chất hóa và bố trí bộ đệm dùng khi tính.
- Không mở rộng sang tối ưu thứ tự nhiều phép nối, ước lượng lực lượng, nối song song, outer join, pipelining, nối không gian hoặc cache-conscious join.

## Tệp đầu ra

- `.codex/goal_lecture_15.md`;
- `2627-1/materials/lec-15/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-15/{outline,storyboard,review-log}.md`;
- dùng mười SVG hiện có trong `2627-1/img/lec-15/`, chỉ thêm hình khi thật sự cần và có nguồn;
- cập nhật mục Bài 15 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
