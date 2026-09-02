# Goal đồng bộ deck Bài 08

## Goal

Đồng bộ bộ trang chiếu **Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc** với lecture note đã phát hành và nguồn MMDS/Stanford, giữ nguyên bốn bài tập MMDS.

## Bằng chứng hoàn thành

- Deck, note, planning và SVG thống nhất ký hiệu hồ chứa $r,s$ và ký hiệu Bloom $n,m,k$.
- Giữ 48 slide/notes/ID, 7 section ngoài, 42+6 slide, 120+60 phút và 6 SVG.
- Không còn câu quy trình hoặc siêu bình luận trong nội dung công khai; không thêm mệnh đề hay số liệu ngoài nguồn.
- Năm reviewer và hai tái kiểm GLM đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium, viewer, index, PDF, kiểm tra an toàn đường dẫn và trạng thái Codex Slides đều đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch: phiên OpenRouter `56486`, `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter; giữ cấu trúc và phát hiện các chỉnh văn phong/index hẹp.
- Reader nguồn: phiên OpenRouter `74176`, cùng model/provider; xác nhận toán và nội dung đúng, yêu cầu đồng bộ sáu chỗ ký hiệu $n\to r$ trong planning/SVG.

## Trạng thái

**Hoàn tất, chờ commit.** Hai reader thống nhất không đổi cấu trúc hay phạm vi. Writer DeepSeek chạy trong dossier tạm nhưng hai lượt lần lượt chạm giới hạn công cụ và timeout; Codex chính áp dụng đúng các delta đã được reader phê duyệt. Năm reviewer hợp lệ và hai tái kiểm cuối đều đạt. Chromium xác nhận 48 trang không tràn ở ba kích thước, 48 notes và 0 lỗi KaTeX; viewer xác nhận 325 công thức, 6 SVG, 11 khối gập, bàn phím, in và cổng an toàn đều đạt; index có đúng một liên kết. Codex Slides truy xuất được dự án nhưng dự án nguồn vẫn là draft 0 slide, đã ghi giới hạn trong review log.
