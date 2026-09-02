# Prompt hiệu chỉnh bộ trang chiếu Bài 13

Hiệu chỉnh hẹp **Bài 13 — Chỉ mục truyền thống và băm tĩnh** theo `AGENTS.md` và các kết luận reader đã được điều phối viên duyệt. Không mở rộng phạm vi, không thêm nguồn, không đổi cấu trúc 59 trang hoặc thời lượng.

## Cơ sở đã duyệt

- Reader lập kế hoạch: phiên `98497`, model `z-ai/glm-5.3-flash`, provider OpenRouter.
- Reader nguồn: phiên `48249`; tái kiểm hẹp: phiên `68155`; cùng model và provider.
- Kiểm kê cố định: 59 slide, 59 ghi chú diễn giả, 59 `data-slide-id` duy nhất, 7 phần ngoài, 49 slide giảng và 10 slide recitation, thời lượng 120+60 phút, 10 SVG.
- Nguồn, phạm vi, ví dụ, công thức, thuật toán và lời giải khác đã đạt; chỉ sửa các delta liệt kê dưới đây.

## Delta bắt buộc

1. Trong lời giải Bài 14.13 của `lecture-note.md`, đổi bản ghi đầu từ `10101 Srini NASA Comp. Sci. 65000` thành `10101 Srinivasan Comp. Sci. 65000`.
2. Ở slide `M05`, đổi nhãn cột `$V_{NULL}$` thành `$V_{\mathrm{NULL}}$` để khớp công thức, ghi chú và ghi chú bài giảng.
3. Trong thẻ Bài 13 của `index.html`, đổi nhãn `Trang chiếu` thành `Bài giảng` và `Ghi chú` thành `Ghi chú bài giảng`. Không đổi URL.
4. Trong ghi chú diễn giả slide `B07`, nói rõ $d+1+J+D$ và $d+1+L+J+D$ là cách đếm của bài giảng suy ra từ mô hình khối của nguồn, không phải công thức trích nguyên văn.

## Biên tập `$no-ai-slop` hẹp

Biên tập ghi chú diễn giả tại `P00`, `P01`, `A03`, `B00`, `C06A`, `C11`, `D01`, `H06`, `M07`, `T01`, `M00A`, `M04`. Xóa lời dẫn quy trình, câu nối kiểu “chuyển sang”, mô tả sản xuất deck và nhịp câu máy móc; giữ nguyên mọi dữ kiện, ký hiệu, giả thiết, kết luận và nguồn.

`H06` chỉ xuất hiện một lần trong danh sách sửa. `C05` phải giữ ý rằng đây là ví dụ độc lập, không nối tiếp vết chèn 8, nhưng diễn đạt tự nhiên và trực tiếp.

Tự kiểm bản sửa theo `no-ai-slop/eval.md`. Dùng nguyên tắc `$quill` để giữ thứ tự khái niệm, thuật ngữ và ký hiệu xuyên suốt; không tạo `quill.json`.

## Ràng buộc đầu ra

- Chỉ sửa các bản sao trong dossier tạm của:
  - `2627-1/lecture-13-chi-muc-truyen-thong-va-bam-tinh.html`;
  - `2627-1/materials/lec-13/lecture-note.md`;
  - `2627-1/index.html`;
  - `2627-1/planning/lec-13/review-log.md` nếu cần ghi đúng các delta đã áp dụng.
- Không sửa SVG, outline, storyboard, CSS, viewer, template hoặc nguồn.
- Không đổi nội dung hiển thị ngoài `M05` và hai nhãn index.
- Không đổi số slide, ID, phần ngoài, thứ tự, thời lượng, công thức, thuật toán, ví dụ hay lời giải ngoài lỗi tên Srinivasan.
- Không chèn mã quy trình, phiên worker, prompt, rubric hoặc thời lượng lên mặt slide hay vào ghi chú diễn giả.
- Không commit hoặc push.

Writer phải trả danh sách tệp đã sửa và mô tả ngắn từng thay đổi. Codex chính sẽ kiểm diff trước khi quyết định áp dụng vào workspace.
