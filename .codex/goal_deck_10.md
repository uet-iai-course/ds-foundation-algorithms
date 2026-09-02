# Goal đồng bộ deck Bài 10

## Goal

Đồng bộ bộ trang chiếu **Bài 10 — Nén dữ liệu không mất thông tin** với lecture note đã phát hành và nguồn Nelson–Gailly, Stanford, CMU; giữ nguyên ba bài tập hiện có.

## Bằng chứng hoàn thành

- Deck, note, planning và SVG giữ thống nhất ký hiệu, giả thiết, ví dụ, thuật toán và bảo đảm của Huffman tĩnh, Huffman thích nghi và mã hóa số học.
- Giữ 48 slide/notes/ID, 6 section ngoài, 44+4 slide, 120+60 phút, 9 SVG với 10 lượt dùng và thứ tự R11 → R08.
- Không còn nhãn quy trình hoặc siêu bình luận trong nội dung công khai; không thêm mệnh đề hay số liệu ngoài nguồn.
- Năm reviewer và các tái kiểm cần thiết đạt; bản cuối qua `$no-ai-slop` và `$quill` mà không tạo `quill.json`.
- Chromium, viewer, index, PDF, kiểm tra an toàn đường dẫn và trạng thái Codex Slides đều đạt.

## Tác tử và trạng thái đầu vào

- Reader kế hoạch: phiên OpenRouter `64886`, `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter; giữ cấu trúc và xác định các chỉnh văn phong/index hẹp.
- Reader nguồn: phiên OpenRouter `87526`, cùng model/provider; xác nhận toán, ví dụ, bài tập và chín SVG đúng, không yêu cầu đổi cấu trúc.

## Trạng thái

**Hoàn tất.** Writer DeepSeek chạy trên dossier hẹp, áp dụng các chỉnh đã phê duyệt rồi bị dừng khi chờ API quá lâu ở vòng tự kiểm. Codex đã đối chiếu diff và đưa đúng các delta reader phê duyệt vào kho. Năm reviewer và tái kiểm R00 đều đạt; Chromium, viewer, index, bàn phím, bản in và an toàn đường dẫn đạt. Codex Slides được ghi đúng là draft 0 slide. Chờ commit và push.
