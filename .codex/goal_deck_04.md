# Goal đồng bộ deck Bài 04

## Goal

Đồng bộ bộ trang chiếu **Bài 04 — PageRank theo chủ đề, liên kết rác và HITS** với lecture note đã phát hành, giữ nguyên nguồn, phạm vi, cấu trúc 41 trang và ba bài tập MMDS.

## Bằng chứng hoàn thành

- Deck và lecture note thống nhất ký hiệu, giả thiết, công thức, ví dụ và kết luận của MMDS mục 5.3–5.5.
- 41 `data-slide-id` duy nhất, 7 mạch ngoài, 120 phút giảng và 60 phút recitation không đổi.
- Không còn tên tệp nội bộ, nhãn quy trình hoặc siêu bình luận trong nội dung hiển thị và ghi chú diễn giả.
- Năm reviewer và hai tái kiểm GLM đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium xác nhận 41 trang ở khung rộng/hẹp không tràn, không lỗi tài nguyên/KaTeX, dùng được bằng bàn phím; viewer, index và bản in đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch `59340`, reader nguồn `28513`: `z-ai/glm-5.3-flash`, provider OpenRouter.
- Hai reader giữ nguyên 41 trang, 7 mạch, phạm vi và ba bài tập.
- Writer dùng `deepseek/deepseek-v4-flash-0731` trên bản sao tạm hẹp.
- Năm reviewer và hai recheck dùng `z-ai/glm-5.3-flash`.

## Trạng thái

**Hoàn tất.** Reader kế hoạch `59340`, reader nguồn `28513`, writer `deepseek/deepseek-v4-flash-0731`, năm reviewer GLM `6374`, `70845`, `68572`, `88073`, `81479` và hai tái kiểm cuối `58341`, `20423` đã hoàn thành với đúng model/provider được duyệt. Bản cuối đã qua `$no-ai-slop`, `$quill`, kiểm tĩnh, Chromium rộng/hẹp, bàn phím, KaTeX, viewer, bản in, an toàn đường dẫn, index và kiểm tra trạng thái Codex Slides. Không tạo `quill.json`; không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
