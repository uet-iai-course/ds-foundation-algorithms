# Goal hiệu chỉnh bộ trang chiếu Bài 15

## 1. Mục tiêu

Chuẩn bị một bản vá hẹp cho **Bài 15 — Thuật toán kết nối dữ liệu** trong dossier tạm. Bản vá chuẩn hóa nhãn index và làm tự nhiên các ghi chú diễn giả đã được reader chỉ ra, không thay đổi nội dung học thuật, nguồn hoặc cấu trúc bài.

## 2. Đầu vào đã duyệt

- Kế hoạch reader phiên `25176`.
- Reader nguồn phiên `84227`, kết luận `GO`.
- Model reader: `z-ai/glm-5.3-flash`; provider OpenRouter.
- Kiểm kê chuẩn: 60 slide/notes/ID, 7 phần ngoài, 50+10 slide, 120+60 phút, 10 SVG.

## 3. Phạm vi sửa

### Index

- Thẻ Bài 15 giữ `Bài giảng`.
- Đổi `Ghi chú` thành `Ghi chú bài giảng`.
- Không đổi URL deck hoặc URL viewer.

### Ghi chú diễn giả

Áp dụng `$no-ai-slop` tối thiểu tại `P00`, `M00`, `M01`, `N02`, `N08`, `S00`, `S08`, `H02`, `H07`, `H08`, `H09`, `H14`, `C04`, `X07`. Xóa đường dẫn nội bộ và lời kể về quá trình làm deck; giữ nguyên nguồn học thuật, giả thiết, dữ liệu, đáp án và các câu nối thực sự cần cho việc giảng.

Không sửa `C03`: quy trình chọn thuật toán nối là nội dung của bài.

Dùng `$quill` để rà tuyến: đặc tả và mô hình I/O → Nested/Block/Indexed Nested → Sort-Merge → Hash/Grace → bảng chọn → recitation. Không tạo `quill.json`.

## 4. Tệp writer được phép sửa trong dossier tạm

- `2627-1/lecture-15-thuat-toan-ket-noi-du-lieu.html`.
- `2627-1/index.html`.

Không sửa các tệp tương ứng trong workspace ở lượt chuẩn bị này.

## 5. Tiêu chí chấp nhận bản nháp

- Nhãn ghi chú Bài 15 là `Ghi chú bài giảng`; liên kết không đổi.
- Không còn `sources/source.md`, “Deck dùng”, “Giảm tải ký hiệu”, “slide 28 bị ẩn”, “yêu cầu hiệu chỉnh”, “đã hiệu chỉnh” hoặc “deck bổ sung” trong các ghi chú mục tiêu.
- Mỗi ghi chú vẫn là mạch nói hữu ích, không bị rút thành chỉ còn metadata nguồn.
- `C03` không thay đổi.
- 60 slide, 60 notes, 60 ID duy nhất, 7 phần ngoài, 50+10 slide và toàn bộ đường dẫn ảnh giữ nguyên.
- Không có `quill.json`; diff chỉ chạm các dòng thuộc phạm vi đã duyệt.

## 6. Quy trình writer

1. Tạo dossier tạm hẹp, không chứa `.env`, bí mật hoặc thông tin xác thực.
2. Chạy một writer OpenRouter bằng `deepseek/deepseek-v4-flash-0731`, `--json`, `--task-profile write`.
3. Chỉ chấp nhận kết quả khi `requested_model`, `observed_model` và `provider` đúng.
4. Codex chính kiểm diff tạm so với workspace, kiểm lại số slide/notes/ID và báo kết quả. Không áp dụng bản vá, không chạy reviewer, không commit, không push trong lượt này.

## 7. Trạng thái

**Hoàn tất.** Phiên OpenRouter `70707` dùng đúng
`deepseek/deepseek-v4-flash-0731` qua provider OpenRouter. Codex đã kiểm và áp
dụng 14 chỉnh sửa notes cùng một nhãn index, rồi sửa hai lỗi bố cục N05/N09 do
Chromium phát hiện. Năm reviewer đều GO; inventory 60/60/7, Chromium, viewer,
index, PDF và đường dẫn an toàn đều đạt. Codex Slides truy cập được nhưng dự án
vẫn là draft 0 slide, nên không tuyên bố đã kiểm canvas.
