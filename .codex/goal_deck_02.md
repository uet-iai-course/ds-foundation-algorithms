# Goal đồng bộ deck Bài 02

## Goal

Đồng bộ bộ trang chiếu **Bài 02 — MapReduce và ngăn xếp xử lý dữ liệu lớn** với lecture note đã phát hành, giữ nguyên nguồn, phạm vi, cấu trúc 42 trang và các bài tập MMDS.

## Bằng chứng hoàn thành

- Deck và lecture note thống nhất thuật ngữ Map/Reduce function, mapper/reducer, Map/Reduce task, ký hiệu Word Count, phân vùng, chịu lỗi và hai quy ước chi phí.
- 42 `data-slide-id` duy nhất, 7 mạch ngoài, 120 phút giảng và 60 phút recitation không đổi.
- Không còn nhãn quy trình sản xuất, tên tệp nội bộ hoặc siêu bình luận trong nội dung hiển thị và ghi chú diễn giả.
- Outline, storyboard và review-log ghi rõ ký hiệu cùng sai khác có chủ ý về quy tắc chuẩn hóa từ trong ví dụ lecture note.
- Nội dung qua năm reviewer và hai tái kiểm GLM; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium xác nhận 42 trang ở khung rộng và hẹp không tràn, không lỗi tài nguyên/KaTeX, dùng được bằng bàn phím; notes và bản in đạt.
- Index dùng URL Bài 02 hiện hành và nhãn “Ghi chú bài giảng”.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch `94510`, reader nguồn `35044`: `z-ai/glm-5.3-flash`, provider OpenRouter.
- Hai reader đều kết luận không cần thêm, gộp, tách hoặc bỏ nội dung. Việc sửa chỉ gồm biên tập notes, đồng bộ planning và nhãn index.
- Writer dùng `deepseek/deepseek-v4-flash-0731` trên bản sao tạm hẹp.
- Năm reviewer và hai recheck dùng `z-ai/glm-5.3-flash`.

## Trạng thái

**Hoàn tất.** Năm reviewer độc lập đã trả báo cáo; hai lượt tái kiểm cuối `9238` và `3922` đều PASS. Kiểm định Chromium, viewer, index, bàn phím, KaTeX, SVG và bản in đều đạt. Không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
