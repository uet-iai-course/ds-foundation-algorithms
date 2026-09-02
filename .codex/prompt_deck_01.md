# Prompt đồng bộ deck Bài 01

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html` với `2627-1/materials/lec-01/lecture-note.md` và nguồn Bài 01. Đây là yêu cầu sửa deck hiện có, không viết lại lecture note và không mở rộng phạm vi.

## Quyết định đã duyệt

- Giữ 41 trang, 7 mạch ngoài, 120 phút giảng và 60 phút recitation; không thêm, gộp, tách hoặc bỏ trang.
- A03 ghi đủ nguồn Stanford CS246 trang chiếu 7–8.
- D04 giải thích rõ $249.750$ là kết quả theo tổ hợp, còn $250.000$ là xấp xỉ dùng $\binom{n}{2}\approx n^2/2$.
- E01 dùng cùng ký hiệu $y,z$ như lecture note và outline.
- E03 thống nhất nguồn Stanford CS246 trang chiếu 10.
- R02 giữ cả giá trị theo tổ hợp khoảng $999.500$ và xấp xỉ nguồn $1.000.000$, không trình bày hai số như mâu thuẫn.
- Dọn ghi chú diễn giả bằng `$no-ai-slop`: bỏ nhãn và câu mô tả quy trình sản xuất như “Câu nối”, “Trang này”, “Đây là điểm kết chu trình”, “Kết luận phần giảng”, “Chuyển ý”, “Hoạt động”, “mốc bàn giao”, “Kết nối”. Viết lại thành mạch nói trực tiếp khi nội dung đó còn hữu ích.
- Giữ các yêu cầu bắt buộc của recitation: dữ kiện, câu hỏi, sản phẩm cần nộp, đáp án và hướng dẫn chấm. Không xóa nhãn “Câu hỏi:” hoặc “Sản phẩm:” trên mặt trang.
- Không đổi công thức, dữ kiện nguồn, thời lượng, `data-slide-id`, SVG, bố cục, CSS hay đường dẫn.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ được sửa bản sao tạm của HTML.
- Codex chính kiểm diff, nhập thay đổi được duyệt và cập nhật planning.
- Sau sửa phải có năm reviewer độc lập, hai lượt recheck, `$no-ai-slop`, `$quill`, Chromium rộng/hẹp/bàn phím/notes/in và kiểm định Codex Slides khi bề mặt khả dụng.

Không gửi `.env`, bí mật hoặc thông tin xác thực cho worker.
