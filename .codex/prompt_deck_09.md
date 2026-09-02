# Prompt đồng bộ deck Bài 09

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-09-dong-du-lieu-dem-momen-va-cua-so.html` với `2627-1/materials/lec-09/lecture-note.md` và nguồn Bài 09. Đây là sửa hẹp deck hiện có.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **09 — Dòng dữ liệu: đếm, mômen và cửa sổ**.
- Giữ 46 slide, 46 `data-slide-id`, 46 speaker notes, 7 section ngoài, 40 slide giảng + 6 slide bài tập, 120+60 phút và 9 SVG.
- Giữ mạch mô hình truy vấn → Flajolet–Martin → Count-Min Sketch → AMS → DGIM → cửa sổ suy giảm → năm bài MMDS. Không thêm chủ đề, bài tập hoặc số liệu.
- Dùng `$no-ai-slop` cho nội dung hiển thị, speaker notes và ghi chú; dùng `$quill` để rà mạch, thuật ngữ và ký hiệu; không tạo `quill.json`.

## Sửa có bằng chứng từ hai reader

- Trong ghi chú bài giảng, đổi ví dụ không có quy mô nguồn “10.000 sự kiện gần nhất” thành “$N$ sự kiện gần nhất”.
- Đổi nhãn tài nguyên Bài 09 trong `index.html` từ “Ghi chú” thành “Ghi chú bài giảng”.
- Bỏ các nhãn quy trình “Cầu nối sang phần sau:” tại F06, C04, M07, D09, E01, T00 và “Cầu nối:” tại C03; viết lại thành mạch nói tự nhiên mà không đổi mệnh đề.
- Biên tập hẹp speaker notes P01, P02, A00, A02, F04, F05, M02, M04, M05, T00, T01 để bỏ giọng quy trình hoặc siêu bình luận. Không đổi nguồn, công thức, chứng minh, ví dụ hay dữ kiện.
- Giữ nguyên cấu trúc, thứ tự, công thức, bài tập và chín SVG.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên hồ sơ tạm hẹp.
- Codex chính kiểm diff và chỉ áp dụng các sửa có bằng chứng.
- Sau sửa: năm reviewer độc lập, các tái kiểm cần thiết, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
