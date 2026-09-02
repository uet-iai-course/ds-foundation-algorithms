# Goal đồng bộ deck Bài 03

## Goal

Đồng bộ bộ trang chiếu **Bài 03 — PageRank: mô hình và tính toán** với lecture note đã phát hành, giữ nguyên nguồn, phạm vi, cấu trúc 39 trang và các bài tập MMDS.

## Bằng chứng hoàn thành

- Deck và lecture note thống nhất ký hiệu đồ thị, ma trận chuyển, PageRank, sửa nút cụt, teleport, cận dừng và biểu diễn thưa.
- 39 `data-slide-id` duy nhất, 7 mạch ngoài, 120 phút giảng và 60 phút recitation không đổi.
- Không còn tên tệp nội bộ, nhãn quy trình hoặc siêu bình luận trong nội dung hiển thị và ghi chú diễn giả.
- Planning không còn ký hiệu Markdown hỏng; biến $q$ của bài biểu diễn thưa thống nhất.
- Năm reviewer và hai tái kiểm GLM đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium xác nhận 39 trang ở khung rộng/hẹp không tràn, không lỗi tài nguyên/KaTeX, dùng được bằng bàn phím; viewer, index và bản in đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch `64749`, reader nguồn `78824`: `z-ai/glm-5.3-flash`, provider OpenRouter.
- Hai reader giữ nguyên 39 trang, bảy mạch và phạm vi nội dung.
- Writer dùng `deepseek/deepseek-v4-flash-0731` trên bản sao tạm hẹp.
- Năm reviewer và hai recheck dùng `z-ai/glm-5.3-flash`.

## Trạng thái

**Hoàn tất.** Reader kế hoạch `64749`, reader nguồn `78824`, writer `deepseek/deepseek-v4-flash-0731`, năm reviewer GLM `73999`, `34666`, `44102`, `99442`, `71323` và hai tái kiểm cuối `46957`, `57270` đã hoàn thành với đúng model/provider được duyệt. Bản cuối đã qua `$no-ai-slop`, `$quill`, kiểm tĩnh, Chromium rộng/hẹp, bàn phím, KaTeX, viewer, bản in, an toàn đường dẫn, index và kiểm tra trạng thái Codex Slides. Không tạo `quill.json`; không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
