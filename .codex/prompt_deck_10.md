# Prompt đồng bộ deck Bài 10

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-10-nen-du-lieu-khong-mat-thong-tin.html` với `2627-1/materials/lec-10/lecture-note.md` và nguồn Bài 10. Đây là sửa hẹp deck hiện có.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **10 — Nén dữ liệu không mất thông tin**.
- Giữ 48 slide, 48 `data-slide-id`, 48 speaker notes, 6 section ngoài, 44 slide giảng + 4 slide bài tập, 120+60 phút và 9 SVG với 10 lượt dùng.
- Giữ mạch mô hình và bộ mã → Huffman tĩnh → Huffman thích nghi → mã hóa số học → tổng hợp → ba bài tập. Không thêm chủ đề, bài tập hoặc số liệu.
- Giữ nguyên thứ tự trang hiện tại, đặc biệt R08 đứng sau R11.
- Dùng `$no-ai-slop` cho nội dung hiển thị, speaker notes và ghi chú; dùng `$quill` để rà mạch, thuật ngữ và ký hiệu; không tạo `quill.json`.

## Sửa có bằng chứng từ hai reader

- Đổi nhãn tài nguyên Bài 10 trong `index.html` từ “Ghi chú” thành “Ghi chú bài giảng”.
- X00 notes: bỏ các câu quy trình nội bộ “ngoại lệ nguồn đã được phê duyệt” và “Storyboard ghi rõ...”, nhưng giữ truy nguyên Nelson–Gailly và CMU. Chỉ sửa nội dung hiển thị X00 nếu cần để câu tự nhiên hơn; không đổi dữ kiện hay yêu cầu.
- H13, A10, R13: bỏ các câu “Kết cụm...” khỏi speaker notes.
- Biên tập tối thiểu P00, H02, H07, R00, R08, R10 để bỏ giọng quy trình hoặc siêu bình luận. Giữ nguyên mệnh đề, công thức, số liệu, nguồn và dữ kiện.
- Giữ nguyên cấu trúc, công thức, chứng minh, bài tập và chín SVG.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên hồ sơ tạm hẹp.
- Codex chính kiểm diff và chỉ áp dụng các sửa có bằng chứng.
- Sau sửa: năm reviewer độc lập, các tái kiểm cần thiết, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
