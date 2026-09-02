# Goal hiệu chỉnh bộ trang chiếu Bài 13

## 1. Mục tiêu

Chuẩn bị một bản vá hẹp cho **Bài 13 — Chỉ mục truyền thống và băm tĩnh** trong dossier tạm. Bản vá sửa bốn sai khác đã được reader xác nhận và làm tự nhiên một số ghi chú diễn giả, nhưng không thay đổi phạm vi, nguồn, cấu trúc học tập hoặc nội dung toán–thuật toán đã đạt.

## 2. Đầu vào đã duyệt

- Kế hoạch reader phiên `98497`.
- Phân tích nguồn phiên `48249`, tái kiểm phiên `68155`.
- Model reader: `z-ai/glm-5.3-flash`; provider OpenRouter.
- Kiểm kê chuẩn: 59 slide/notes/ID, 7 phần ngoài, 49+10 slide, 120+60 phút, 10 SVG.

## 3. Phạm vi sửa

### Nội dung bắt buộc

- `lecture-note.md`: sửa `Srini NASA` thành `Srinivasan` trong dữ liệu lời giải 14.13.
- Slide `M05`: chuẩn hóa nhãn cột thành `$V_{\mathrm{NULL}}$`.
- Slide `B07`: thêm vào ghi chú diễn giả rằng hai công thức chi phí là cách đếm của bài giảng từ mô hình khối của nguồn.
- `index.html`: thẻ Bài 13 dùng đúng `Bài giảng` và `Ghi chú bài giảng`, giữ nguyên hai liên kết.

### Văn phong

Áp dụng `$no-ai-slop` tối thiểu cho ghi chú diễn giả `P00`, `P01`, `A03`, `B00`, `C06A`, `C11`, `D01`, `H06`, `M07`, `T01`, `M00A`, `M04`. Với `C05`, giữ nguyên ý “ví dụ độc lập, không phải trạng thái kế tiếp của vết chèn 8” nhưng viết như lời giảng tự nhiên. Không sửa các câu đã rõ chỉ để đồng đều văn phong.

Dùng `$quill` để rà tính liên tục của tuyến: nhu cầu chỉ mục → B+-Tree → cập nhật → B-Tree → băm tĩnh → bitmap → tổng hợp → recitation. Không tạo `quill.json`.

## 4. Tệp writer được phép sửa trong dossier tạm

- `2627-1/lecture-13-chi-muc-truyen-thong-va-bam-tinh.html`.
- `2627-1/materials/lec-13/lecture-note.md`.
- `2627-1/index.html`.
- `2627-1/planning/lec-13/review-log.md` nếu cần ghi nhận chính xác bản vá.

Không sửa tệp tương ứng trong workspace ở lượt chuẩn bị này.

## 5. Tiêu chí chấp nhận bản nháp

- Bốn delta bắt buộc xuất hiện đúng một lần và không kéo theo thay đổi học thuật khác.
- Ghi chú diễn giả đã bỏ lời dẫn quy trình và metadiscourse, nhưng vẫn giữ nguồn, giả thiết, đáp án và câu nối cần cho giảng dạy.
- `C05` vẫn phân biệt rõ ví dụ tách nút trong với vết chèn 8.
- 59 slide, 59 notes, 59 ID duy nhất, 7 phần ngoài, 49+10 slide và toàn bộ đường dẫn ảnh giữ nguyên.
- Không có `Srini NASA`, `$V_{NULL}$` tại cột M05, nhãn index cũ của Bài 13 hoặc `quill.json` trong bản nháp.
- Diff chỉ chạm các dòng thuộc phạm vi đã duyệt.

## 6. Quy trình writer

1. Tạo dossier tạm chỉ chứa các tệp cần đọc/sửa và hướng dẫn biên tập; tuyệt đối không chứa `.env`, bí mật hoặc thông tin xác thực.
2. Chạy một writer OpenRouter bằng `deepseek/deepseek-v4-flash-0731`, `--json`, `--task-profile write`.
3. Chỉ chấp nhận kết quả khi `requested_model`, `observed_model` và `provider` đúng.
4. Codex chính kiểm diff tạm so với workspace, kiểm lại số slide/notes/ID và báo kết quả. Không áp dụng bản vá, không chạy reviewer, không commit, không push trong lượt này.

## 7. Trạng thái

**Hoàn tất.** Writer OpenRouter phiên `7280` dùng đúng
`deepseek/deepseek-v4-flash-0731`; `requested_model` và `observed_model` trùng
nhau, provider là OpenRouter. Phiên thử `10704` hết thời gian trước khi ghi và
không được dùng. Codex đã kiểm diff, áp dụng các sửa được duyệt và chỉnh ba câu
writer còn cụt. Năm reviewer đều GO; Chromium, viewer, index, PDF, đường dẫn an
toàn và inventory đều đạt. Codex Slides truy cập được nhưng dự án vẫn là draft
0 slide, nên không tuyên bố đã kiểm canvas.
