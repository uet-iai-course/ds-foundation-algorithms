# Prompt xây dựng ghi chú Bài 12

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 12 — Mô hình I/O và sắp xếp ngoài bộ nhớ**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 12 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng *Database System Concepts* 7e, Chương 12–13 và phần sắp xếp ngoài bộ nhớ của Chương 15 làm trục; Wisconsin CS764 chỉ bổ sung Replacement Selection.
- Phạm vi gồm phân cấp lưu trữ, bản ghi–khối–khung, buffer manager, mô hình chi phí I/O, tạo dãy ban đầu, trộn nhiều đường, External Merge Sort, vật chất hóa so với truyền dòng, phân tích số lượt và chi phí, đệm dài, Replacement Selection cùng giới hạn của nhận định độ dài trung bình khoảng $2H$.
- Phân biệt $B$ là số khung bộ đệm và $H$ là số bản ghi vừa vùng heap. Trong mô hình trộn chung dành một khung đầu ra, $k=B-1$; biến thể ba khung của Bài 15.1 phải được ghi là biến thể nguồn, không khái quát thành $k=B$.
- Recitation dùng trực tiếp Bài 15.1, 15.9 và 13.5 cùng lời giải chính thức đã ánh xạ trong planning. Không đổi dữ kiện hoặc yêu cầu toán học và không tạo bài mới.
- Giữ các trường hợp biên $N=0$, $0<N\le B$, điều kiện $B\ge3$ khi $N>B$, cùng sự khác nhau giữa số lần truyền khối và số lần định vị.

## Tệp đầu ra

- `.codex/goal_lecture_12.md`;
- `2627-1/materials/lec-12/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-12/{outline,storyboard,review-log}.md`;
- dùng tám SVG hiện có trong `2627-1/img/lec-12/`, chỉ thêm hình khi nguồn và mạch học tập thật sự cần;
- cập nhật mục Bài 12 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
