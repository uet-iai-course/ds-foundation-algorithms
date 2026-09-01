# Prompt xác định goal ghi chú Bài 07

Hãy xác định goal cho ghi chú tự học của **Bài 07 — Chỉ mục hàng xóm gần đúng**, học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027. Đây là bước chốt phạm vi; chưa soạn `lecture-note.md`, chưa sửa deck và chưa cập nhật index.

## Đầu vào đã xác định

- Bài theo thứ tự đề xuất: `07 — Chỉ mục hàng xóm gần đúng`, ánh xạ từ buổi gốc 13.
- Deck: `2627-1/lecture-07-chi-muc-hang-xom-gan-dung.html`.
- Ghi chú đích: `2627-1/materials/lec-07/lecture-note.md`.
- Planning: `2627-1/planning/lec-07/{outline,storyboard,review-log}.md`.
- Đối tượng đã học Bài 05–06, vector, khoảng cách, đồ thị, hàng đợi ưu tiên, xác suất và k-means cơ bản.
- Mức độ `đầy đủ`: mỗi chủ đề cốt lõi phải có đặc tả, ví dụ kiểm được, lập luận đúng, chi phí, giới hạn và tự kiểm tra; không dạy DiskANN, NSG, Vamana, OPQ hoặc bảo đảm phổ quát không có trong nguồn.

## Sản phẩm học tập phải phục vụ

1. Đặc tả tìm $K$ hàng xóm gần đúng, phá hòa, phân biệt đáp án đúng với đáp án gần đúng và tính $\operatorname{recall@K}$.
2. Chạy tay tìm kiếm tham lam, tìm kiếm chùm và `SEARCH-LAYER`; nêu trạng thái, bất biến, điều kiện dừng và trường hợp cực tiểu cục bộ.
3. Giải thích tầng HNSW, truy vấn, chèn, chọn lân cận, cắt cạnh và tác động của $M$, `efConstruction`, `efSearch`; không tuyên bố độ phức tạp logarit vô điều kiện.
4. Đặc tả lượng tử hóa vector, lượng tử hóa tích (PQ), mã hóa, tái dựng, khoảng cách bất đối xứng (ADC), bảng tra, bộ nhớ và giới hạn quét tuyến tính.
5. Đặc tả IVF-PQ: tâm thô, danh sách đảo, mã phần dư, truy vấn dư riêng từng danh sách, $nprobe$, top-$K$ và trường hợp thiếu ứng viên.
6. So sánh LSH, HNSW, PQ quét đầy đủ và IVF-PQ theo độ thu hồi, độ trễ, thời gian xây dựng và bộ nhớ; không xếp hạng phổ quát.
7. Giữ nguyên ba nhiệm vụ thực hành trong Princeton runbook: tái dựng PQ, so cấu hình 6 byte và IVF-PQ. Không bịa kết quả chạy, mục tiêu vận hành hoặc bài HNSW khi nguồn không có.

## Nguồn bắt buộc

1. `AGENTS.md`, mục Bài 07 trong `sources/source.md` và dòng Bài 07 trong `sources/reference-slides/README.md`.
2. Stanford BIODS 271 `L12-approximate-nearest-neighbor.pdf` chỉ cho bối cảnh và cấu hình quy mô; không dùng tuyên bố hiệu năng thiếu điều kiện.
3. Princeton `class-09-graph-indexes.pdf` cho trực giác đồ thị và `class-08-quantization.pdf` cho VQ, PQ, ADC, IVF-PQ.
4. Malkov–Yashunin `hnsw-malkov-yashunin.pdf` và Jégou–Douze–Schmid `product-quantization-jegou-douze-schmid.pdf` là nguồn chuẩn để chốt thuật toán, giả thiết, công thức và giới hạn.
5. `class-08-runbook-for-students.ipynb` là nguồn trực tiếp duy nhất cho ba nhiệm vụ thực hành; giữ trạng thái kernel và ô nguồn được chỉ định trong planning.
6. Deck, planning, chín SVG hiện có, viewer, mẫu Markdown và index.
7. MMDS/Stanford CS246 LSH chỉ dùng làm cầu từ Bài 06; không dạy lại banding.

## Điều phối OpenRouter

Người dùng cho phép gửi tệp cần thiết đã lọc tới OpenRouter, trừ `.env`, khóa, token, mật khẩu, cookie, khóa riêng và thông tin xác thực.

1. Reader/reviewer dùng `z-ai/glm-5.3-flash`; writer dùng `deepseek/deepseek-v4-flash-0731`.
2. Chạy độc lập reader lập kế hoạch (`plan`), reader ánh xạ nguồn (`source`) và reviewer bản đồ chủ đề (`review`). Các vai chỉ đọc.
3. Codex chính đối chiếu báo cáo với nguồn và tự tính lại mọi ví dụ trước khi hợp nhất goal.
4. Sau goal, một writer soạn trong gốc tạm hẹp; năm reviewer GLM kiểm độc lập. Codex chính được phép áp dụng sửa đã duyệt; các thay đổi toán/mạch phải tái kiểm.
5. Worker lỗi thì ghi nguyên văn và thử lại cùng model trên dossier hẹp hơn; không đổi ngầm model, nguồn, phạm vi hoặc cổng.

## Điểm bắt buộc trong bản đồ chủ đề

- Cầu Bài 06: LSH là một cơ chế tạo ứng viên; Bài 07 đặt ba họ cơ chế cạnh nhau nhưng không lặp chứng minh LSH.
- ANN và `recall@K`: tập có đúng $K$ mã định danh, phá hòa xác định, xử lý khoảng cách bằng nhau.
- Tình huống quy mô: chỉ dùng số liệu BIODS có căn cứ; phân biệt bộ nhớ vector thô, byte mã và chi phí quét.
- Đồ thị: tìm kiếm tham lam trước chùm; `SEARCH-LAYER` giữ hai tập ứng viên/kết quả, ngưỡng xa nhất thay đổi và không mở lại đỉnh đã duyệt.
- HNSW: phân phối tầng, truy vấn từ trên xuống, chèn, chọn cạnh đa dạng, cắt cạnh; nêu rõ giới hạn của suy luận $O(NM)$ và tuyên bố logarit.
- PQ: VQ trước PQ; $D$ chia hết cho $m$ nếu dùng các đoạn đều; $k^*=2^b$; mã, tái dựng, SDC/ADC nếu cần phân biệt, bảng tra, bộ nhớ và chi phí.
- IVF-PQ: phân vùng thô, phần dư theo từng tâm, bảng ADC theo truy vấn dư, $nprobe$; không đánh đồng số danh sách mở với số ứng viên.
- So sánh: bốn trục đo giống nhau, nêu điều kiện và workload; không dùng khẩu hiệu “nhanh nhất/tốt nhất”.
- Thực hành: giữ đúng ô nguồn, trạng thái `d,xt,xb,xq,gt`, ngân sách 6 byte và công thức báo cáo; không ghi số kết quả cố định.

Mỗi chủ đề phải đánh dấu chuỗi `vai trò và nhu cầu → định nghĩa/đặc tả → ví dụ chạy tay → trực quan → mệnh đề/thuật toán → chứng minh/lập luận đúng → ứng dụng, lỗi dễ mắc và kiểm tra`. Mục không áp dụng phải có lý do.

## Đầu ra goal

Tạo `.codex/goal_lecture_7.md` bằng tiếng Việt với đúng 13 mục:

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

Chỉ ghi `sẵn sàng soạn` khi đã kiểm trực tiếp hai bài báo, ba bộ slide, notebook, ba nhiệm vụ thực hành và mọi công thức/ví dụ. Không tạo `quill.json`.
