# Prompt đồng bộ deck Bài 11

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html` với `2627-1/materials/lec-11/lecture-note.md` và nguồn Bài 11. Đây là sửa hẹp nội dung hiện có.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **11 — Nén bằng từ điển và nén mất dữ liệu**.
- Giữ 48 slide, 48 `data-slide-id`, 48 speaker notes, 7 section ngoài, 42 slide giảng + 6 slide bài tập, 120+60 phút và 12 SVG.
- Giữ nguyên cấu trúc, thứ tự, nội dung, công thức, thuật toán, chứng minh, dữ kiện, bài tập và nguồn.
- Dùng `$no-ai-slop` cho nội dung hiển thị, speaker notes và ghi chú; dùng `$quill` để rà mạch, thuật ngữ và ký hiệu; không tạo `quill.json`.

## Sửa có bằng chứng từ reader

- Trong card Bài 11 của `index.html`, đổi nhãn “Trang chiếu” thành “Bài giảng”, đổi “Ghi chú” thành “Ghi chú bài giảng”, và thêm `aria-label="Tài nguyên Bài 11"` cho khối `.resource-actions`.
- Gộp hai đoạn lặp ở mục 5.2 của `lecture-note.md` về DCT, lượng tử hóa, lấy mẫu thưa sai màu, zigzag, RLE và mã entropy. Giữ đầy đủ ranh giới bước mất dữ liệu; không thêm mệnh đề.
- Biên tập tối thiểu speaker notes P02, L00, L02, L04 và W07 để bỏ giọng quy trình hoặc câu chuyển ý máy móc. Giữ nguyên ý nghĩa, ký hiệu và truy nguyên nguồn.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên dossier hẹp.
- Codex chính kiểm diff và chỉ áp dụng các sửa có bằng chứng.
- Sau sửa: năm reviewer độc lập, các tái kiểm cần thiết, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer và index.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
