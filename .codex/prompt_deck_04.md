# Prompt đồng bộ deck Bài 04

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html` với `2627-1/materials/lec-04/lecture-note.md` và nguồn Bài 04. Đây là sửa hẹp deck hiện có, không mở rộng phạm vi.

## Quyết định đã duyệt

- Giữ 41 trang, 7 mạch ngoài, 120 phút giảng và 60 phút recitation; không thêm, gộp, tách hoặc bỏ trang.
- Giữ PageRank theo chủ đề, mô hình cụm thao túng liên kết, TrustRank, khối lượng rác và HITS theo MMDS mục 5.3–5.5.
- Giữ công thức spam farm chính xác hơn dạng xấp xỉ trong sách; giữ cảnh báo hai quy ước hệ số giảm ở Hình 5.17; giữ đặc tả dừng HITS có $\tau$ và cờ, đồng thời ghi rõ đây là làm chặt của học phần.
- Giữ quy ước $P$ cột nguồn đã chia bậc và $L$ hàng nguồn Boolean, ba bài tập MMDS, toàn bộ công thức, SVG và thời lượng.
- Dùng `$no-ai-slop` để bỏ tên tệp nội bộ, câu dẫn quy trình và siêu bình luận khỏi nội dung cùng ghi chú diễn giả. Viết thành mạch nói trực tiếp; không đổi nguồn, dữ kiện, đáp án hoặc hướng dẫn chấm.

## Sửa cục bộ

- Dọn speaker notes P00, P01, T07, H00, Z00 và Z03.
- Viết trực tiếp câu chuyển ý chứa $La^{(2)}$ trong lecture note.
- Chuẩn hóa nhãn tài nguyên Bài 04 trong index thành “Ghi chú bài giảng”; không đổi URL.

## Hệ thống tác tử

- Reader và reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter, chỉ sửa bản sao tạm hẹp.
- Codex chính kiểm diff và chỉ nhập thay đổi đã được duyệt.
- Sau sửa phải có năm reviewer độc lập, hai recheck, `$no-ai-slop`, `$quill`, Chromium rộng/hẹp/bàn phím/notes/in, viewer, index và kiểm định Codex Slides khi bề mặt khả dụng.

Không gửi `.env`, bí mật hoặc thông tin xác thực cho worker.
