# Goal đồng bộ deck Bài 14

## Goal

Đồng bộ bộ trang chiếu **Bài 14 — Chỉ mục văn bản và chỉ mục không gian** với ghi chú bài giảng đã phát hành và nguồn, tập trung vào ký hiệu ball tree, hai lỗi hiển thị/lập luận trong ghi chú, nhãn index và văn phong speaker notes.

## Bằng chứng hoàn thành

- Giữ 58 slide/notes/ID, 7 section ngoài, 49+9 slide, 120+60 phút và 13 SVG.
- Tập nền NOT vẫn là $S$; tập điểm dựng ball tree thống nhất là $\mathcal X$ trong deck, note, outline và storyboard.
- Câu giải thích cận âm dùng đúng trường hợp $q\in B$; bảng số không hiển thị dấu ngoặc KaTeX thô.
- Index Bài 14 dùng `Bài giảng`, `Ghi chú bài giảng` và có nhãn truy cập đúng.
- Speaker notes đã qua `$no-ai-slop`; mạch và ký hiệu đã qua `$quill` mà không tạo `quill.json`.
- Hai SVG mồ côi có quyết định rõ trong manifest/review log; writer không tự xóa.
- Năm reviewer, hai recheck và các cổng Chromium, viewer, index, PDF, Codex Slides đều đạt hoặc giới hạn công cụ được ghi chính xác trước commit/push.

## Reader đã duyệt

- Planning: các phiên `32738`, `50253`, `68928`, `4241`, `22769`, dùng `z-ai/glm-5.3-flash` qua OpenRouter.
- Source: phiên hợp lệ `62472`, cùng model/provider; xác nhận cấu trúc và nội dung nguồn.
- Inventory đã duyệt: 58 slide/notes/ID, 7 section ngoài, 49+9 slide, 120+60 phút, 13 SVG; `ball-build.svg` và `kofn-heap.svg` mồ côi.

## Phạm vi writer

Writer chỉ sửa bản sao tạm của deck, note, outline, storyboard, index và khi cần `ball-build.svg`; không xóa SVG và không sửa workspace. Writer phải tạo manifest ghi từng thay đổi, bất biến và khuyến nghị xử lý hai SVG mồ côi.

## Trạng thái

**Hoàn tất.** Phiên OpenRouter `19801` dùng đúng model yêu cầu `deepseek/deepseek-v4-flash-0731` nhưng treo ở vòng 5 sau 240 giây và được dừng minh bạch. Sub-agent chuẩn bị lại patch tạm cùng manifest; Codex kiểm và áp dụng từng hunk. Năm reviewer đều GO sau một lượt sửa/tái kiểm văn phong. Chromium, viewer, index, PDF, inventory và đường dẫn an toàn đều đạt. Hai SVG mồ côi được giữ theo quyết định reviewer nguồn. Codex Slides truy cập được nhưng dự án vẫn là draft 0 slide, nên không tuyên bố đã kiểm canvas.
