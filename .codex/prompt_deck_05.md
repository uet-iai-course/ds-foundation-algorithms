# Prompt đồng bộ deck Bài 05

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html` với `2627-1/materials/lec-05/lecture-note.md` và nguồn Bài 05. Đây là sửa hẹp deck hiện có, không mở rộng phạm vi.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **05 — Biểu diễn tương đồng: Shingling và MinHash**, ánh xạ từ buổi gốc 3 và một phần buổi 12.
- Giữ phạm vi MMDS Chương 3, mục 3.1–3.3; LSH và banding thuộc Bài 06.
- Giữ 49 trang, 7 mạch ngoài, 120 phút giảng, 60 phút recitation và 5 SVG; chỉ thay đổi cấu trúc khi reader nguồn chỉ ra lỗi có bằng chứng.
- Giữ bốn bài tập MMDS 3.1.1, 3.2.3, 3.3.2 và 3.3.3; không đổi dữ kiện hay yêu cầu toán học.
- Dùng `$no-ai-slop` để bỏ câu dẫn quy trình, siêu bình luận và nhịp văn máy móc khỏi nội dung cùng ghi chú diễn giả. Dùng `$quill` để rà mạch, ký hiệu và tính liên tục; không tạo `quill.json`.

## Điểm cần rà

- Đối chiếu định nghĩa shingle, Jaccard, MinHash, định lý xác suất, chữ ký và quét ma trận thưa với sách MMDS, slide MMDS và Stanford được ánh xạ.
- Tính lại ví dụ, ma trận chữ ký, bốn bài tập, kỳ vọng, phương sai và cận thời gian–bộ nhớ.
- Rà các trường hợp biên do học phần bổ sung: hợp rỗng, cột rỗng, miền hữu hạn và hàm băm có va chạm.
- Viết lại trực tiếp các câu mang tính điều hướng như “cầu nối”, “trang tiếp theo” hoặc “phần sau” trong ghi chú diễn giả, nhưng giữ quan hệ khái niệm.
- Chuẩn hóa nhãn tài nguyên Bài 05 trong index thành “Ghi chú bài giảng”; không đổi URL.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ xử lý bản sao tạm hẹp.
- Codex chính kiểm diff và chỉ áp dụng thay đổi đã được reader hoặc reviewer chấp thuận.
- Sau sửa phải có năm reviewer độc lập, hai recheck, kiểm tĩnh, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và kiểm tra trạng thái Codex Slides.

Không đọc hoặc gửi `.env`, bí mật hay thông tin xác thực cho worker.
