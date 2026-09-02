# Prompt đồng bộ deck Bài 02

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html` với `2627-1/materials/lec-02/lecture-note.md` và nguồn Bài 02. Đây là yêu cầu sửa hẹp deck hiện có, không mở rộng phạm vi.

## Quyết định đã duyệt

- Giữ 42 trang, 7 mạch ngoài, 120 phút giảng và 60 phút recitation; không thêm, gộp, tách hoặc bỏ trang.
- Giữ thứ tự B01 → B05 → B02 vì đặc tả phải đứng trước giả mã; không đổi `data-slide-id`.
- Giữ hai quy ước chi phí ở D03: $C_t=I+M$ và $C_{I/O}=I+2M+O$ đo hai phạm vi khác nhau.
- Giữ quy tắc tách từ tổng quát trên deck. Ghi chú bài giảng chọn một quy tắc cụ thể chỉ cho ví dụ chạy tay; ghi đây là sai khác có chủ ý, không phải mâu thuẫn.
- Dùng `$no-ai-slop` để bỏ nhãn hoặc siêu bình luận trong ghi chú diễn giả như “Câu nối”, “trang này hình thức hóa”, “Đây là mẫu sản phẩm học tập”, “Mục 4 nối”, “Mục 5 buộc”. Viết lại thành mạch nói trực tiếp, giữ nguồn và nội dung sư phạm hữu ích.
- Bỏ tên tệp nội bộ `sources/source.md` khỏi ghi chú diễn giả; có thể giữ mô tả “mục tiêu Bài 2 của học phần”.
- Giữ đáp án, nguồn và hướng dẫn chấm của phần recitation. Không xóa nhãn “Câu hỏi:” hoặc “Sản phẩm:” trên mặt trang.
- Không đổi công thức, dữ kiện nguồn, thuật toán, giả thiết, thời lượng, SVG, CSS hoặc đường dẫn.

## Hồ sơ và index

- Đồng bộ bảng ký hiệu trong outline: dùng $f(w,d)$; bổ sung $h$ và $p(k)=h(k)\bmod r$.
- Ghi trong storyboard/review-log rằng quy tắc chuẩn hóa từ cụ thể chỉ thuộc ví dụ của lecture note.
- Chuẩn hóa nhãn tài nguyên Bài 02 trong index từ “Ghi chú” thành “Ghi chú bài giảng”; không đổi URL.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ sửa bản sao tạm được giao.
- Codex chính kiểm diff, nhập thay đổi được duyệt và cập nhật planning.
- Sau sửa phải có năm reviewer độc lập, hai lượt recheck, `$no-ai-slop`, `$quill`, Chromium rộng/hẹp/bàn phím/notes/in và kiểm định Codex Slides khi bề mặt khả dụng.

Không gửi `.env`, bí mật hoặc thông tin xác thực cho worker.
