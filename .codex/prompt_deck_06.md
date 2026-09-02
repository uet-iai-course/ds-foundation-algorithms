# Prompt đồng bộ deck Bài 06

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-06-tim-cap-tuong-dong-bang-lsh.html` với `2627-1/materials/lec-06/lecture-note.md` và nguồn Bài 06. Đây là sửa hẹp deck hiện có, không mở rộng sang Bài 07.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **06 — Tìm cặp tương đồng bằng LSH**, ánh xạ từ một phần buổi gốc 12.
- Giữ phạm vi MMDS Chương 3, §§3.4, 3.6–3.8; §3.5 chỉ khôi phục định nghĩa khoảng cách. HNSW, PQ và IVF-PQ thuộc Bài 07 hoặc ngoài phạm vi.
- Giữ 50 trang, 7 section ngoài, 120 phút giảng, 60 phút recitation và 10 SVG, trừ khi reader chứng minh cần thay đổi cấu trúc.
- Giữ nguyên dữ kiện và yêu cầu của MMDS Bài 3.4.4, 3.6.1 và 3.8.2.
- Dùng `$no-ai-slop` để bỏ câu dẫn quy trình, siêu bình luận và nhịp văn máy móc khỏi nội dung cùng speaker notes. Dùng `$quill` để rà mạch, ký hiệu và tính liên tục; không tạo `quill.json`.

## Sửa có bằng chứng từ reader nguồn

- Không gọi bảng tự dựng ba chữ ký là nguyên văn “Ví dụ 3.11”; ghi rõ đây là ví dụ chạy tay thu gọn theo quy tắc của MMDS Ví dụ 3.11.
- Trong định nghĩa họ LSH, thống nhất biến ngẫu nhiên thành $h\sim F$ và viết xác suất bằng $h$, không đổi sang $f$.
- Làm rõ phần Euclid hai chiều của MMDS là nội dung mở rộng trong lecture note; deck vẫn tập trung vào phép chiếu–dịch $p$-ổn định, không thêm trang.
- Đổi tiêu đề D02 thành “Băm siêu phẳng cho khoảng cách góc” để công thức $1-\theta/\pi$ không bị hiểu là $\cos\theta$.
- Thống nhất hoặc ánh xạ “phát hiện đúng / bỏ sót / va chạm sai” với TP/FN/FP.
- Làm rõ bước sinh cặp trong SVG `luong-ung-vien.svg` mà không đổi thuật toán.
- Chuẩn hóa nhãn tài nguyên Bài 06 trong index thành “Ghi chú bài giảng”; không đổi URL.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ xử lý hồ sơ tạm hẹp.
- Codex chính kiểm diff và áp dụng các sửa được reader hoặc reviewer chấp thuận.
- Sau sửa phải có năm reviewer độc lập, hai recheck, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và kiểm tra trạng thái Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
