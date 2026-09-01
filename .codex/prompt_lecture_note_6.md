# Prompt xác định goal ghi chú Bài 06

Hãy xác định goal cho ghi chú tự học của **Bài 06 — Tìm cặp tương đồng bằng băm nhạy cảm cục bộ**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa deck và chưa cập nhật index.

## Đầu vào đã xác định

- Bài theo thứ tự đề xuất: `06 — Tìm cặp tương đồng bằng LSH`, ánh xạ từ một phần buổi gốc 12.
- Deck: `2627-1/lecture-06-tim-cap-tuong-dong-bang-lsh.html`.
- Ghi chú đích: `2627-1/materials/lec-06/lecture-note.md`.
- Planning: `2627-1/planning/lec-06/{outline,storyboard,review-log}.md`.
- Đối tượng đã học Bài 05: tập shingle, Jaccard, chữ ký MinHash và định lý xác suất; đã học xác suất độc lập, vector, khoảng cách cơ bản và MapReduce ở Bài 02.
- Mức độ `đầy đủ`: mỗi chủ đề cốt lõi phải có đặc tả, ví dụ kiểm được, lập luận đúng, chi phí, giới hạn và tự kiểm tra; không mở rộng sang HNSW/PQ của Bài 07.

## Sản phẩm học tập phải phục vụ

1. Dùng Ví dụ 3.10 để giải thích vì sao chữ ký MinHash ngắn vẫn không làm phép quét mọi cặp khả thi.
2. Chia chữ ký $p=br$ thành $b$ dải, tạo khóa dải đầy đủ, đặc tả điều kiện ứng viên và suy ra $q(s)=1-(1-s^r)^b$ dưới giả thiết độc lập.
3. Tính Ví dụ 3.12, ngưỡng nửa $s_{1/2}=(1-2^{-1/b})^{1/r}$ và phân tích hướng thay đổi $b,r$ khi giữ $p$ cố định.
4. Đặc tả thuật toán tạo tập ứng viên đã loại trùng, nêu bất biến, dừng, đối chiếu hậu kỳ, chi phí theo $bN$, $A=\sum_B\binom{|B|}{2}$, $|C|$ và dung lượng chữ ký.
5. Phát biểu đúng họ băm nhạy cảm cục bộ theo phân phối $h\sim F$, hai ngưỡng gần/xa và hai cận xác suất; giải thích khuếch đại AND/OR mà không khẳng định gì về vùng giữa.
6. Đặc tả và so sánh họ LSH cho Hamming, cosin và Euclid với đúng miền, nguồn ngẫu nhiên, công thức xác suất hoặc điều kiện áp dụng; không đánh đồng các họ.
7. Phân tích mô hình khớp vân tay trong MMDS §§3.8.4–3.8.5 như một mô hình xác suất của nguồn, không như bằng chứng hiệu năng hiện thời.
8. Giải nguyên trạng MMDS Bài 3.4.4, 3.6.1 và 3.8.2; giữ hai công việc MapReduce, chuỗi AND/OR và mọi xác suất nguồn.

Không dạy HNSW, Product Quantization (PQ), IVF-PQ, Z-order curve, API hay triển khai cụm. Không mang số liệu thực nghiệm hoặc tuyên bố hiện thời ngoài nguồn vào ghi chú.

## Nguồn bắt buộc

1. `AGENTS.md` và mục Bài 06 trong `sources/source.md`.
2. Dòng Bài 06 trong `sources/reference-slides/README.md`.
3. `sources/textbooks/mmds-3e-ch03-finding-similar-items.pdf`, trực tiếp §§3.4, 3.6–3.8; dùng §3.5 chỉ để khôi phục định nghĩa khoảng cách cần cho §3.7; Ví dụ 3.10–3.12, 3.18 và các ví dụ liên quan vân tay; Bài 3.4.4, 3.6.1, 3.8.2.
4. `sources/reference-slides/mmds/ch03-lsh.pdf` và Stanford CS246 `03-lsh.pdf`, `04-lsh_theory.pdf`; so sánh theo từng cụm, chọn nguồn có đặc tả và phân tích xác suất rõ hơn, ghi lý do.
5. Deck, planning và mười SVG hiện có trong `2627-1/img/lec-06/`.
6. Viewer, mẫu Markdown và `2627-1/index.html` để chốt ràng buộc phát hành.

Planning hiện dẫn Datar et al. (2004) cho họ LSH Euclid nhưng tệp bài báo không có trong `sources/`. Không được gán mệnh đề cho bài báo này hoặc mở rộng theo bài báo nếu chưa có nguồn cục bộ; ưu tiên phát biểu đủ căn cứ từ MMDS §§3.7.4–3.7.5. Nếu MMDS không đủ cho một công thức đang có trong deck, phải đánh dấu khoảng trống và dừng phần phụ thuộc thay vì suy diễn.

## Điều phối OpenRouter

Người dùng cho phép gửi các tệp cần thiết đã lọc tới OpenRouter, trừ `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực.

1. Reader/reviewer dùng `z-ai/glm-5.3-flash` qua OpenRouter.
2. Chạy một reader lập kế hoạch (`plan`), một reader ánh xạ nguồn (`source`) và một reviewer lập bản đồ chủ đề (`review`). Các vai chỉ đọc và đề xuất độc lập.
3. Codex chính đối chiếu nguồn, tính lại xác suất và hợp nhất goal trước khi writer chạy.
4. Writer dùng `deepseek/deepseek-v4-flash-0731`; năm reviewer và recheck giữ GLM. Codex chính được phép áp dụng trực tiếp các sửa được reviewer phê duyệt.
5. Worker lỗi thì ghi nguyên văn và thử lại cùng model trên dossier hẹp hơn; không đổi ngầm model, nguồn, phạm vi hoặc cổng.

## Điểm bắt buộc trong bản đồ chủ đề

- Cầu từ Bài 05: chữ ký $p\times N$, xác suất một hàng trùng bằng Jaccard trong mô hình lý tưởng, và phần còn thiếu là giảm số cặp.
- Phân dải: khóa phải gồm chỉ số dải và toàn bộ vector $r$ hàng; va chạm mã băm chỉ là cách tìm ngăn, không là bằng chứng hai khóa bằng nhau.
- Xác suất: $s^r$, $(1-s^r)^b$, $q(s)$, điều kiện độc lập, trường hợp biên, ngưỡng nửa và đánh đổi tham số.
- Thuật toán: tập ứng viên không thứ tự đã loại trùng, ngăn đã gom, bất biến sau từng ngăn, hậu kiểm bằng ngưỡng $\tau$, và phân biệt số bản ghi với số từ truyền.
- Định nghĩa họ LSH: khoảng cách hay độ tương đồng phải thống nhất; $d_1<d_2$, $\alpha_1>\alpha_2$, $h\sim F$; không phát biểu bảo đảm cho vùng $d_1<d<d_2$.
- AND/OR: chỉ dùng công thức lũy thừa khi các phép băm độc lập; giữ đúng thứ tự phép ghép của từng ví dụ và bài tập.
- Hamming: chọn tọa độ đều; xác suất va chạm $1-H(x,y)/m$ với $0\le H\le m$.
- Cosin: pháp tuyến ngẫu nhiên đẳng hướng; xác suất cùng dấu $1-\theta/\pi$; vector 0 và Rademacher là trường hợp cần nêu giới hạn.
- Euclid: phát biểu theo đúng MMDS §§3.7.4–3.7.5, gồm hướng chiếu và độ dịch ngẫu nhiên khi nguồn hỗ trợ; không tuyên bố công thức tổng quát thiếu giả thiết.
- Vân tay: phân biệt ngăn “có” theo bộ ba ô với ngăn “không”, nguồn độc lập và hai tầng khuếch đại; ghi rõ đây là mô hình sách.
- Bài tập: 3.4.4, 3.6.1, 3.8.2 giữ nguyên dữ kiện/yêu cầu và có lời giải kiểm được.

Với mỗi chủ đề, đánh dấu thành phần trong chuỗi `vai trò và nhu cầu → định nghĩa/đặc tả → ví dụ chạy tay → trực quan → mệnh đề/thuật toán → chứng minh → ứng dụng, lỗi dễ mắc và kiểm tra`. Mục không áp dụng phải có lý do.

## Đầu ra goal

Tạo `.codex/goal_lecture_6.md` bằng tiếng Việt với đúng 13 mục:

1. `Goal`.
2. `Vấn đề trung tâm`.
3. `Bằng chứng hoàn thành`.
4. `Đầu ra`.
5. `Đối tượng và tiên quyết`.
6. `Phạm vi nguồn`.
7. `Bản đồ chủ đề` có `note-topic-id` duy nhất.
8. `Chủ đề bổ sung đề xuất`.
9. `Khuôn trình bày`.
10. `Ngoài phạm vi`.
11. `Rủi ro và điểm cần duyệt`.
12. `Kế hoạch tác tử`.
13. `Trạng thái`.

Chỉ ghi `sẵn sàng soạn` khi đã kiểm trực tiếp các phần nguồn, ba đề bài và mọi công thức xác suất; mọi bổ sung có căn cứ, không còn khoảng trống làm thay đổi đáng kể kết quả. Không tạo `quill.json`.
