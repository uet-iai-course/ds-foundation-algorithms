# Goal đồng bộ deck Bài 11

## Goal

Đồng bộ bộ trang chiếu **Bài 11 — Nén bằng từ điển và nén mất dữ liệu** với lecture note đã phát hành và nguồn Nelson–Gailly, Stanford, CMU; chỉ sửa nhãn index, một đoạn lặp trong ghi chú và năm speaker notes đã được reader khoanh vùng.

## Bằng chứng hoàn thành

- Deck, note, planning và SVG giữ thống nhất ký hiệu, giả thiết, ví dụ, thuật toán và bảo đảm của LZ77, LZ78, LZW và JPEG dựa trên DCT.
- Giữ 48 slide/notes/ID, 7 section ngoài, 42+6 slide, 120+60 phút và 12 SVG.
- Mục 5.2 không lặp cùng ranh giới mất dữ liệu; không còn giọng quy trình ở năm notes đã khoanh vùng.
- Card Bài 11 có nhãn “Bài giảng”, “Ghi chú bài giảng” và `aria-label="Tài nguyên Bài 11"`.
- Năm reviewer và các tái kiểm cần thiết đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium, viewer, index, PDF và kiểm tra an toàn đường dẫn đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch: các phiên OpenRouter hợp lệ `35623`, `28920`, `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter; giữ cấu trúc và xác định các chỉnh văn phong/index hẹp.
- Reader nguồn: phiên OpenRouter `73243`, cùng model/provider; xác nhận toán, nguồn, bài tập và tài sản đúng, không yêu cầu đổi cấu trúc.

## Trạng thái

**Hoàn tất.** Writer DeepSeek đọc dossier hẹp nhưng bị dừng sau khi chờ API quá lâu trước khi ghi tệp. Codex áp dụng trực tiếp đúng các delta được hai reader phê duyệt. Năm reviewer đều đạt; Chromium, viewer, index, bàn phím, bản in và an toàn đường dẫn đạt. Codex Slides được ghi đúng là draft 0 slide. Chờ commit và push.
