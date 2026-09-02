# Goal đồng bộ deck Bài 07

## Goal

Đồng bộ bộ trang chiếu **Bài 07 — Chỉ mục hàng xóm gần đúng** với lecture note đã phát hành và nguồn HNSW/PQ/IVF-PQ, giữ đúng ba nhiệm vụ thực hành notebook.

## Bằng chứng hoàn thành

- Deck và lecture note thống nhất hợp đồng `SEARCH-LAYER`, quy ước chỉ số tâm, ký hiệu truy vấn dư, công thức, ví dụ, chi phí và nhiệm vụ notebook.
- Giữ 47 slide/notes/ID, 7 section ngoài, 38+9 slide, 120+60 phút và 9 SVG.
- Không còn câu quy trình, siêu bình luận hoặc đường dẫn nội bộ không cần thiết trong nội dung công khai.
- Năm reviewer và hai tái kiểm GLM đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium, viewer, index, PDF, kiểm tra an toàn đường dẫn và trạng thái Codex Slides đều đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch: phiên OpenRouter `81520`, `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter; giữ cấu trúc 47 slide và phát hiện hợp đồng `ep`, ký hiệu truy vấn dư, nhãn index.
- Reader nguồn: phiên OpenRouter `13583`, cùng model/provider; xác nhận 47 slide trên disk, yêu cầu đồng bộ chỉ số tâm 0-based và tách đúng phạm vi ô notebook.
- Writer: phiên OpenRouter `98265`, `requested_model = observed_model = deepseek/deepseek-v4-flash-0731`, provider OpenRouter; đề xuất đúng các sửa hẹp trong hồ sơ.

## Trạng thái

**Hoàn tất, chờ commit.** Điều phối viên đã bác số đếm 49 từ kết luận tóm tắt của reader nguồn; đếm trực tiếp xác nhận 47 slide. Năm reviewer hợp lệ và hai tái kiểm cuối đều đạt sau khi sửa. Chromium xác nhận 47 trang không tràn ở ba kích thước, 47 notes, 0 lỗi KaTeX; viewer xác nhận 193 công thức, 9 SVG, 6 khối gập, bàn phím, bản in và cổng an toàn đều đạt; index có đúng một liên kết. Codex Slides truy xuất được dự án nhưng dự án nguồn vẫn là draft 0 slide, đã ghi rõ giới hạn trong review log.
