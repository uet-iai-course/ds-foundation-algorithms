# Prompt xây dựng ghi chú Bài 11

Thực hiện đầy đủ quy trình trong `AGENTS.md` để xây dựng ghi chú tự học **Bài 11 — Nén bằng từ điển và nén mất dữ liệu**. Đây là yêu cầu chỉ làm ghi chú: không viết lại deck, trừ khi thay đổi nội dung dùng chung buộc phải đồng bộ.

## Phạm vi bắt buộc

- Đọc `sources/source.md` và dòng Bài 11 trong `sources/reference-slides/README.md` trước khi chọn nội dung.
- Dùng Nelson–Gailly, *The Data Compression Book*, Chương 8, 9 và 11 làm trục; đối chiếu slide CMU 15-499 và MIT 15.564 đã ánh xạ. Không dùng Chương 10 làm nguồn cho JPEG.
- Phạm vi gồm LZ77 với cửa sổ và sao chép chồng lấn; LZ78 với từ điển đồng bộ và quy tắc kết thúc; LZW với bất biến độ trễ một mục, trường hợp `k = next_code` và hợp đồng độ rộng mã; JPEG dựa trên DCT với khối $8\times8$, lượng tử hóa, DC/AC, zigzag, RLE, khôi phục gần đúng và RMS.
- Tách rõ hai đặc tả: LZ77/LZ78/LZW phải khôi phục đúng chuỗi; JPEG cho ảnh tái tạo gần đúng. Không mở sang MPEG, wavelet, Burrows–Wheeler hoặc ACB.
- Recitation giữ năm bài đã được phê duyệt trong planning ngày 2026-08-28, dùng trực tiếp dữ kiện CMU. Không đổi yêu cầu toán học hoặc tạo bài mới.
- Giữ đúng quy ước $(d,\ell,c)$ trong phần giảng LZ77 và $(p,\ell,c)$ ở bài CMU; `EOS` nằm ngoài bảng chữ cái; mã 256 trong vết LZW là mục từ mới đầu tiên, không phải `EOS`.

## Tệp đầu ra

- `.codex/goal_lecture_11.md`;
- `2627-1/materials/lec-11/lecture-note.md`;
- cập nhật phần ghi chú trong `2627-1/planning/lec-11/{outline,storyboard,review-log}.md`;
- chỉ dùng 12 SVG hiện có trong `2627-1/img/lec-11/`, trừ khi nguồn buộc phải có thêm hình;
- cập nhật mục Bài 11 trong `2627-1/index.html` sau khi viewer đạt mọi cổng.

## Điều phối OpenRouter

1. Chạy ba reader độc lập bằng `z-ai/glm-5.3-flash` qua OpenRouter: lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề. Chúng chỉ đọc và không sửa tệp.
2. Codex chính hợp nhất, duyệt đề xuất rồi hoàn thiện goal trước khi writer bắt đầu.
3. Chạy một writer `deepseek/deepseek-v4-flash-0731` trong gốc tạm hẹp. Codex chính kiểm bản nháp trước khi đưa vào kho.
4. Chạy năm reviewer `z-ai/glm-5.3-flash` độc lập: nguồn, toán–thuật toán, mạch sư phạm, tính liên tục và viewer.
5. Codex chính áp dụng các sửa có căn cứ; chạy hai lượt `recheck` về toán–thuật toán và mạch viết.
6. Dùng `$no-ai-slop` và `$quill` cho bản cuối; không tạo `quill.json`.
7. Kiểm viewer thật ở màn hình rộng, hẹp, bàn phím, bản in, đường dẫn an toàn và liên kết từ index. Chỉ commit/push khi toàn bộ cổng đạt.

Mọi worker phải dùng `--json`; chỉ chấp nhận khi `requested_model`, `observed_model` và `provider` đúng. Người dùng cho phép gửi các tệp cần thiết tới OpenRouter, ngoại trừ `.env`, bí mật và thông tin xác thực. Nếu worker lỗi, thử lại cùng model trong phạm vi hẹp hơn; không đổi ngầm model, provider, nguồn hoặc cổng kiểm định.
