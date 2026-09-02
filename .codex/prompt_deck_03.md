# Prompt đồng bộ deck Bài 03

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-03-pagerank-mo-hinh-va-tinh-toan.html` với `2627-1/materials/lec-03/lecture-note.md` và nguồn Bài 03. Đây là sửa hẹp deck hiện có, không mở rộng phạm vi.

## Quyết định đã duyệt

- Giữ 39 trang, 7 mạch ngoài, 120 phút giảng và 60 phút recitation; không thêm, gộp, tách hoặc bỏ trang.
- Giữ mô hình cột $r=Pr$, sửa nút cụt $\bar P$, damping/teleport $A_\beta$, chứng minh co, cận hậu nghiệm, giả mã có $K_{\max}$ và luồng MapReduce hai tác vụ.
- Giữ dữ kiện $(y,a,m)$, $P_0/\bar P$, $\delta$, $\tau/\varepsilon$, K00 và bốn bài MMDS 5.1.1–5.2.2.
- Dùng `$no-ai-slop` để bỏ tên tệp nội bộ, mã trang và siêu bình luận khỏi nội dung cùng ghi chú diễn giả. Viết thành mạch nói trực tiếp; giữ nguồn, đáp án và hướng dẫn chấm.
- Không đổi công thức, dữ kiện, thuật toán, giả thiết, `data-slide-id`, SVG, CSS, đường dẫn hoặc thời lượng.

## Hồ sơ và index

- Bổ sung $N^-(i)$ vào bảng ký hiệu outline.
- Sửa ký hiệu hỏng trong storyboard thành $\bar P$, $\Delta_t$, $\Theta(n+m)$.
- Thống nhất biến số phần tử 1 trong bài R04 là $q$ giữa deck và lecture note.
- Chuẩn hóa nhãn tài nguyên Bài 03 trong index thành “Ghi chú bài giảng”; không đổi URL.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ sửa bản sao tạm của HTML.
- Codex chính kiểm diff, nhập thay đổi được duyệt và cập nhật note/planning/index.
- Sau sửa phải có năm reviewer độc lập, hai recheck, `$no-ai-slop`, `$quill`, Chromium rộng/hẹp/bàn phím/notes/in và kiểm định Codex Slides khi bề mặt khả dụng.

Không gửi `.env`, bí mật hoặc thông tin xác thực cho worker.
