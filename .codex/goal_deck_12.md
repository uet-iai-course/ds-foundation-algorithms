# Goal đồng bộ deck Bài 12

## Goal

Đồng bộ bộ trang chiếu **Bài 12 — Mô hình I/O và sắp xếp ngoài bộ nhớ** với ghi chú bài giảng đã phát hành và các nguồn được ánh xạ, bằng các sửa hẹp về nhãn index và văn phong speaker notes.

## Bằng chứng hoàn thành

- Giữ 53 slide/notes/ID, 7 section ngoài, 46+7 slide, 120+60 phút và 8 SVG.
- Deck, note và planning dùng cùng đặc tả, ký hiệu, ví dụ và kết luận; không thay đổi công thức hay mốc nguồn đã kiểm chứng.
- Mục index dùng nhãn `Bài giảng` và `Ghi chú bài giảng`, với URL doc/deck hiện tại.
- Speaker notes P00, P01, P02, I06, I07, S06, S11, S15, S16, R00, T01 và X01 đã qua `$no-ai-slop`, không còn lời bình kiểu quy trình nhưng vẫn giữ teaching cues cần thiết.
- Bản cuối qua `$quill` mà không tạo `quill.json`, năm reviewer, hai recheck, Chromium, viewer, index, PDF, đường dẫn an toàn và kiểm định Codex Slides hoặc ghi rõ giới hạn công cụ.

## Reader đã duyệt

- Reader kế hoạch phiên `96490`: `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter; giữ nguyên cấu trúc và đề xuất các sửa hẹp.
- Reader nguồn phiên `45983` và lượt kiểm chứng trích xuất phiên `21434`: cùng model/provider; kết luận GO cho nội dung, công thức, ví dụ và recitation.
- False positive của phiên `21434` về lời giải Bài 13.5 đã bị bác bằng kiểm tra trực tiếp: mốc đúng vẫn là PDF trang 5/trang in 95.

## Phạm vi sửa writer

Writer chỉ làm trên dossier tạm và chỉ được:

1. đề xuất hai nhãn index mới;
2. chỉnh speaker notes của 12 ID đã chốt;
3. ghi manifest thay đổi và xác nhận không đổi nội dung toán học, dữ kiện, nguồn hoặc cấu trúc.

Codex chính phải kiểm diff trước khi áp dụng. Không cho writer sửa trực tiếp workspace.

## Trạng thái

**Hoàn tất.** Reader đã GO. Writer DeepSeek phiên `42641` chạy đúng model qua OpenRouter trong `/tmp/lec12-deck-writer`; phiên chỉ hoàn tất hai nhãn Bài 12 trong bản sao index rồi chờ hơn bốn phút, nên điều phối viên dừng minh bạch. Codex đã áp dụng trực tiếp đúng các delta được reader phê duyệt. Năm reviewer hợp lệ đều GO; hai lượt đếm sai section đã được thay bằng tái kiểm độc lập. Chromium, viewer, index, PDF, đường dẫn an toàn và inventory đều đạt. Codex Slides truy cập được nhưng dự án vẫn là draft 0 slide, nên không tuyên bố đã kiểm canvas.
