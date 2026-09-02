# Prompt đồng bộ deck Bài 08

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html` với `2627-1/materials/lec-08/lecture-note.md` và nguồn Bài 08. Đây là sửa hẹp deck hiện có.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc**.
- Giữ 48 slide, 48 `data-slide-id`, 48 speaker notes, 7 section ngoài, 42 slide giảng + 6 slide bài tập, 120+60 phút và 6 SVG.
- Giữ mạch mô hình dòng → lấy mẫu theo khóa → lấy mẫu hồ chứa → Bloom filter → chọn cấu trúc → bốn bài MMDS. Không thêm chủ đề, bài tập hoặc số liệu.
- Dùng `$no-ai-slop` cho nội dung hiển thị, speaker notes và ghi chú; dùng `$quill` để rà mạch, thuật ngữ và ký hiệu; không tạo `quill.json`.

## Sửa có bằng chứng từ hai reader

- Chuẩn hóa ký hiệu số vị trí đã xử lý của hồ chứa từ $n$ sang $r$ trong `outline.md`, `storyboard.md` và `img/lec-08/reservoir-trace.svg`; giữ $n$ cho số bit Bloom. Công thức xác suất hồ chứa là $s/r$.
- Đổi “Bloom Filter” thành “Bloom filter” trong thẻ index và đổi nhãn thành “Ghi chú bài giảng”.
- Biên tập speaker notes P01, P02, K06, K07, B09, X00, X05 để bỏ giọng quy trình/checklist và đường dẫn nội bộ không cần thiết, không đổi mệnh đề hay dữ kiện.
- Giữ nguyên cấu trúc, công thức, chứng minh, ví dụ, bài tập và sáu SVG ngoài sửa ký hiệu hồ chứa.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên hồ sơ tạm hẹp.
- Codex chính kiểm diff và chỉ áp dụng các sửa có bằng chứng.
- Sau sửa: năm reviewer độc lập, hai recheck, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
