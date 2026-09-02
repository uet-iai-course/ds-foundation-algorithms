# Goal đồng bộ deck Bài 01

## Goal

Đồng bộ bộ trang chiếu **Bài 01 — Bài toán dữ liệu lớn và mô hình thuật toán** với lecture note đã phát hành, giữ nguyên nguồn, phạm vi, thời lượng và cấu trúc học tập đã kiểm định.

## Bằng chứng hoàn thành

- Deck và lecture note thống nhất ký hiệu, giả thiết, ví dụ, công thức, quy ước xấp xỉ và nguồn.
- 41 `data-slide-id` duy nhất, 7 mạch ngoài, 120 phút giảng và 60 phút recitation không đổi.
- Không còn nhãn quy trình sản xuất hoặc siêu bình luận trong nội dung hiển thị và ghi chú diễn giả.
- Nội dung qua năm góc rà độc lập và hai lượt tái kiểm bằng GLM; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium xác nhận khung 1280×720 và màn hình hẹp không tràn, không lỗi tài nguyên/KaTeX, dùng được bằng bàn phím, notes và bản in đạt.
- Codex Slides được đọc/kiểm định theo khả năng của phiên; nếu Browser nội bộ không khả dụng, ghi rõ giới hạn và dùng ảnh render RevealJS làm bằng chứng trực quan.

## Phạm vi sửa đã duyệt

1. A03: Stanford CS246 trang chiếu 7–8.
2. D04: phân biệt $249.750$ theo tổ hợp với $250.000$ theo xấp xỉ $n^2/2$.
3. E01: dùng $y,z$ nhất quán với lecture note.
4. E03: Stanford CS246 trang chiếu 10.
5. R02: nêu $999.500$ theo tổ hợp và $1.000.000$ theo xấp xỉ nguồn.
6. Bỏ nhãn quy trình sản xuất trong notes; giữ đáp án, nguồn, hướng dẫn giảng và chấm bài.

Không thêm trang hoặc chủ đề: hai reader độc lập xác nhận lecture note không tạo khoảng trống nội dung cần bổ sung vào deck.

## Tác tử

- Reader kế hoạch phiên `45938`, reader nguồn phiên `19318`: `z-ai/glm-5.3-flash`, provider OpenRouter.
- Writer dùng `deepseek/deepseek-v4-flash-0731` trên bản sao tạm hẹp.
- Năm reviewer và hai recheck dùng `z-ai/glm-5.3-flash`.

## Trạng thái

**Hoàn tất.** Năm reviewer độc lập đã trả báo cáo; hai lượt tái kiểm cuối `50263` và `29457` đều PASS. Kiểm định Chromium, bàn phím, KaTeX, SVG và bản in đều đạt. Không gửi `.env`, bí mật hoặc thông tin xác thực tới worker.
