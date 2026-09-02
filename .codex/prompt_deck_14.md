# Prompt đồng bộ deck Bài 14

Thực hiện theo `AGENTS.md` để đồng bộ `2627-1/lecture-14-chi-muc-van-ban-va-chi-muc-khong-gian.html` với ghi chú, planning và nguồn Bài 14. Đây là sửa hẹp sản phẩm hiện có; giữ nguyên phạm vi, ví dụ, bài recitation và cấu trúc.

## Quyết định đầu vào

- Bài theo thứ tự đề xuất: **14 — Chỉ mục văn bản và chỉ mục không gian**.
- Giữ 58 slide, 58 `data-slide-id`, 58 speaker notes, 7 section ngoài, 49 slide giảng + 9 slide recitation, 120+60 phút và 13 SVG.
- Giữ mạch chỉ mục đảo → R-tree → kd-tree → ball tree → Z-order → tổng hợp → ba cụm recitation.
- Giữ sửa có chủ ý của nguồn: OR dùng hợp thay vì giao bị in nhầm ở slide Chương 31; bảng Morton dùng công thức nhất quán và sửa hoán vị 6/7 của hình Auburn.
- Dùng `$no-ai-slop` để chỉnh tối thiểu nội dung công khai và speaker notes; dùng `$quill` để rà ký hiệu, thuật ngữ và câu nối; không tạo `quill.json`.

## Sửa có bằng chứng

1. Đồng bộ tập điểm dùng để dựng ball tree từ $S$ sang $\mathcal X$ tại B00, B04, B05, B06 và các dòng liên quan trong `outline.md`, `storyboard.md`. Giữ $S$ riêng cho tập nền của NOT. Đồng bộ cả $S_L,S_R,c_S,r_S$ thành $\mathcal X_L,\mathcal X_R,c_{\mathcal X},r_{\mathcal X}$ khi xuất hiện.
2. Trong ghi chú, sửa “Lấy cực đại với 0 để tránh cận âm khi $q\notin B$” thành trường hợp đúng $q\in B$; công thức cận dưới không đổi.
3. Trong bảng ví dụ ball tree của ghi chú, đổi giá trị `1{,}5` đang nằm ngoài math thành `$1{,}5$`; chuẩn hóa ô `2,5` cùng hàng thành `$2{,}5$` nếu cần, không biến số thập phân trong văn xuôi thành mã KaTeX.
4. Trong thẻ Bài 14 của index, đổi `Trang chiếu` thành `Bài giảng`, `Ghi chú` thành `Ghi chú bài giảng`, và thêm `aria-label="Tài nguyên Bài 14"` vào `resource-actions`. Không đổi URL hay thẻ bài khác.
5. Biên tập speaker notes I12, K03, K05, K06, B00, B03, B04, B05, B06 và B07: bỏ lời bình quy trình như “Cầu sang…”, “cụm đã khép”, “phần sau trở lại”; viết ký hiệu `best`, $\tau$, $\delta$, $\operatorname{LB}$, $\ell$, $\mathcal X\subseteq\mathbb R^p$ nhất quán; giữ nguồn, giả thiết, lập luận và chuyển ý sư phạm tự nhiên.
6. Trong ghi chú, bỏ nhãn phô “Nhận xét quan trọng:” trước câu về danh sách đảo; giữ nguyên mệnh đề kỹ thuật.

## Hai SVG mồ côi

- `ball-build.svg` và `kofn-heap.svg` hiện không được deck tham chiếu; writer không được xóa chúng.
- Writer phải kiểm cả hai và ghi khuyến nghị `giữ` hoặc `đề nghị điều phối viên xóa` trong manifest.
- Nếu giữ và chỉnh `ball-build.svg`, phải đổi $S$ sang $\mathcal X$ và làm nhãn vector khớp chiều mũi tên: mũi tên từ $x_1$ tới $x_2$ mang nhãn $x_2-x_1$, hoặc đảo mũi tên để giữ $x_1-x_2$.
- Không sửa `kofn-heap.svg` nếu không có lỗi cụ thể.

## Nguồn và kiểm định phải giữ

- Nguồn chính: *Database System Concepts* 7e Chương 24 và 31, Cornell CS5780, Auburn COMP7120; recitation dùng Bài 31.2 và lời giải 25.2–25.3 đã ánh xạ.
- Không thêm nội dung, mệnh đề, số liệu, hình hoặc bài tập.
- Sau writer: Codex chính kiểm diff rồi mới áp dụng; tiếp theo phải có năm reviewer, hai recheck, kiểm Chromium/viewer/index/PDF và Codex Slides hoặc ghi rõ giới hạn.

## Hệ thống tác tử

- Reader/reviewer: `z-ai/glm-5.3-flash` qua OpenRouter.
- Writer: `deepseek/deepseek-v4-flash-0731` qua OpenRouter trong dossier tạm hẹp.
- Chỉ chấp nhận kết quả `--json` khi metadata model/provider khớp.
- Không đọc hoặc gửi `.env`, khóa, token, mật khẩu, cookie, khóa riêng hay thông tin xác thực cho worker.
