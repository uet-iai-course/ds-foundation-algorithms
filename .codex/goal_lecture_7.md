# Goal ghi chú Bài 07

## 1. Goal

Hoàn thiện ghi chú tự học **Bài 07 — Chỉ mục hàng xóm gần đúng** tại `2627-1/materials/lec-07/lecture-note.md`. Tài liệu phải giúp sinh viên đặc tả và đo chất lượng tìm kiếm gần đúng, chạy các thuật toán đồ thị cốt lõi, mã hóa bằng lượng tử hóa tích, ghép IVF với PQ và so sánh LSH–HNSW–PQ–IVF-PQ trên cùng bốn trục.

## 2. Vấn đề trung tâm

Một kho $N$ vector $D$ chiều cần trả $K$ hàng xóm cho mỗi truy vấn. Quét đủ tốn $\Theta(ND)$ phép tính và lưu vector thô có thể vượt ngân sách. Bài 07 xét ba cách cắt chi phí khác nhau: lọc ứng viên bằng băm, điều hướng trên đồ thị và nén vector thành mã; mỗi cách đổi chất lượng lấy độ trễ, thời gian xây dựng hoặc bộ nhớ.

## 3. Bằng chứng hoàn thành

- Người học đặc tả ANN với phá hòa xác định và tính đúng $\operatorname{recall@K}$.
- Người học chạy tham lam, tìm kiếm chùm và `SEARCH-LAYER`, nêu trạng thái, bất biến, dừng và cực tiểu cục bộ.
- Người học mô tả đúng tầng, truy vấn, chèn, chọn/cắt cạnh HNSW và tác động của $M$, `efConstruction`, `efSearch` mà không hứa cận logarit vô điều kiện.
- Người học mã hóa, tái dựng và tính ADC bằng PQ; tính không gian mã, bộ nhớ bảng tâm và chi phí quét.
- Người học đặc tả IVF-PQ với tâm thô, phần dư theo danh sách, $nprobe$, top-$K$ và trường hợp thiếu ứng viên.
- Người học so sánh bốn cơ chế theo recall, độ trễ, thời gian xây dựng và bộ nhớ dưới một workload đã nêu.
- Ba nhiệm vụ Princeton runbook giữ nguyên trạng thái, ô nguồn và yêu cầu; không ghi kết quả chạy cố định.
- Viewer, Markdown, KaTeX, SVG, liên kết, bàn phím, màn hình rộng/hẹp, bản in và ràng buộc an toàn đều đạt trước khi cập nhật index.

## 4. Đầu ra

- `2627-1/materials/lec-07/lecture-note.md`.
- Cập nhật phần ghi chú trong `2627-1/planning/lec-07/{outline,storyboard,review-log}.md`.
- Dùng chín SVG hiện có; chỉ tạo thêm hình khi một lập luận bắt buộc chưa được hỗ trợ.
- Thêm liên kết ghi chú trong `2627-1/index.html` sau khi viewer đạt mọi cổng.
- Không sửa deck trừ khi một sửa đổi dùng chung về ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự buộc phải đồng bộ.

## 5. Đối tượng và tiên quyết

Sinh viên đại học đã học Bài 05–06, vector Euclid, đồ thị có hướng, hàng đợi ưu tiên, xác suất và k-means cơ bản. Ghi chú nhắc ngắn vai trò của LSH, không lặp chứng minh banding.

## 6. Phạm vi nguồn

- `sources/source.md` mục Bài 07 và dòng Bài 07 trong `sources/reference-slides/README.md`.
- Stanford BIODS 271 bài 12 chỉ cho bối cảnh và cấu hình $N=10^{10},D=3072$, đoạn 6 chiều, tâm 8 bit. Không dùng các tỷ lệ hiệu năng thiếu điều kiện.
- Princeton lớp 9 cho trực giác đồ thị; Malkov–Yashunin, *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs*, là nguồn chuẩn cho HNSW.
- Princeton lớp 8 cho VQ, PQ, ADC, IVF-PQ; Jégou–Douze–Schmid, *Product Quantization for Nearest Neighbor Search*, là nguồn chuẩn cho công thức và IVFADC.
- Princeton runbook lớp 8 là nguồn trực tiếp cho ba nhiệm vụ thực hành: ô nền 0–4, 17, 21–24; PQ 82–97; ngân sách 6 byte 98–99; IVF-PQ 148–155.
- Deck, planning và chín SVG Bài 07 dùng để đồng bộ sản phẩm; không thay bài báo làm căn cứ học thuật.
- Ví dụ đồ thị, ADC số và công thức chi phí hệ thống do học phần suy trực tiếp từ cơ chế nguồn phải được gắn nhãn “ví dụ dựng lại” hoặc “suy ra”.

## 7. Bản đồ chủ đề

| `note-topic-id` | Nhãn | Chủ đề và sản phẩm | Chuỗi trình bày, nguồn và kết nối |
|---|---|---|---|
| `L07-N01` | cầu nối | Quy mô, ANN, phá hòa, recall@K và bốn trục đo | Vai trò → đặc tả → ví dụ phá hòa → phép đo → chi phí quét → kiểm tra. BIODS, hai bài báo. Dẫn sang hai nhánh chỉ mục. |
| `L07-N02` | cầu nối | LSH trong bản đồ cơ chế | Nhắc đầu vào/ứng viên/hậu kiểm của Bài 06 → phân biệt ngăn, đường, mã. Không có chứng minh mới vì đã hoàn tất ở bài trước. |
| `L07-N03` | cốt lõi | Tìm kiếm tham lam và cực tiểu cục bộ | Vai trò → trạng thái đồ thị → ví dụ $e\to a\to b$ → điều kiện dừng → phản ví dụ bỏ $z$ → kiểm tra. Princeton 09; ví dụ dựng lại. |
| `L07-N04` | cốt lõi | Tìm kiếm chùm và `SEARCH-LAYER` | Đặc tả $C,W,ef$ → vết chạy → giả mã → bất biến trên phần đã thăm → dừng/chi phí/trường hợp xấu → kiểm tra. HNSW Algorithm 2. |
| `L07-N05` | cốt lõi | Kiến trúc, truy vấn và chèn HNSW | Tầng → phân phối mức → truy vấn trên xuống → chèn → chọn cạnh đa dạng/cắt cạnh → lập luận đúng cục bộ → trường hợp biên. HNSW Algorithms 1, 4, 5. |
| `L07-N06` | cốt lõi | Tham số, bộ nhớ và giới hạn HNSW | $M$, `efConstruction`, `efSearch` → đánh đổi → $O(ND)$ vector và kỳ vọng $O(NM)$ liên kết dưới giả thiết → không bảo đảm logarit phổ quát → kiểm tra. |
| `L07-N07` | cốt lõi | Từ VQ đến PQ | Vai trò nén → lượng tử hóa/tái dựng → ví dụ VQ → giới hạn bộ mã đơn → chia $D$ thành $m$ đoạn → mã PQ/tái dựng → sai số và kiểm tra. PQ paper §§II–III. |
| `L07-N08` | cốt lõi | ADC, bảng tra và bộ nhớ PQ | Truy vấn đầy đủ + mã DB → ví dụ ADC 0.31 → công thức → bảng tra → chi phí $\Theta(k^*D)$ và $\Theta(m)$ → quét $\Theta(Nm)$ → kiểm tra. |
| `L07-N09` | cốt lõi | IVF-PQ và mã phần dư | Phân vùng thô → danh sách đảo → phần dư → truy vấn dư/bảng riêng → $nprobe$ → top-$K$/thiếu ứng viên → chi phí có điều kiện. PQ §IV-A, Princeton 08. |
| `L07-N10` | cốt lõi | So sánh bốn cơ chế | Đặt cùng workload → bảng bốn trục → lựa chọn có điều kiện → lỗi xếp hạng phổ quát → kiểm tra. Tổng hợp nguồn, không thêm số hiệu năng. |
| `L07-N11` | cầu nối | Ba nhiệm vụ thực hành | Chuẩn bị kernel → tái dựng PQ → so ba cấu hình 6 byte → IVF-PQ và phép đo `nok/|xq|` → sản phẩm báo cáo. Notebook là nguồn trực tiếp; không áp dụng chứng minh. |

Đồ thị tiên quyết: `L07-N01 → L07-N02`; từ đó tách `L07-N03 → N04 → N05 → N06` và `L07-N07 → N08 → N09`; hai nhánh hội tụ ở `L07-N10`, còn `L07-N11` phụ thuộc `N07–N09` nhưng không phụ thuộc HNSW.

## 8. Chủ đề bổ sung đề xuất

- **Giữ — bổ sung:** quy tắc phá hòa theo `(khoảng cách, mã định danh)` để $N_K(q)$ xác định khi có khoảng cách bằng nhau. Đây là phần làm chặt đặc tả, không phải thuật toán mới.
- **Giữ — bổ sung:** phân biệt `nok/|xq|` trong notebook là độ chính xác hạng 1 của thí nghiệm, không tự động bằng recall@K tổng quát.
- **Giữ — bổ sung:** chi phí IVF-PQ ba thành phần và số kết quả $\min(K,\sum_{i\in P}|L_i|)$ được ghi là suy ra từ cơ chế nguồn.
- **Bỏ:** bài thực hành HNSW tự dựng, số kết quả notebook cố định, tuyên bố BIODS giảm chính xác 20–30%, phần mở rộng ứng viên của HNSW Algorithm 4 và mọi phương pháp ngoài phạm vi.

## 9. Khuôn trình bày

Mỗi chủ đề cốt lõi đi theo vai trò và nhu cầu; định nghĩa hoặc đặc tả; ví dụ chạy tay; trực quan; mệnh đề hoặc thuật toán; chứng minh hay lập luận đúng; ứng dụng, lỗi dễ mắc và kiểm tra. Phân biệt dữ liệu đầy đủ, mã nén, ứng viên và kết quả top-$K$. Công thức Markdown chỉ dùng `$...$` và `$$...$$`; khối tùy biến không lồng nhau. Văn phong thuần Việt, trực tiếp và không chứa hướng dẫn sản xuất tài liệu.

## 10. Ngoài phạm vi

DiskANN, NSG, Vamana, OPQ, lượng tử hóa cộng, huấn luyện bộ mã tối ưu, triển khai dịch vụ, tuning theo một hệ thống cụ thể, chứng minh lại LSH, phần mở rộng ứng viên HNSW và bảo đảm logarit vô điều kiện.

## 11. Rủi ro và điểm cần duyệt

- `SEARCH-LAYER` chỉ duy trì tập tốt nhất trong phần đồ thị đã khám phá; bất biến không chứng minh tìm được hàng xóm toàn cục.
- Lựa chọn $m_L=1/\ln M$ chỉ có nghĩa khi $M>1$ và là lựa chọn thực nghiệm trong bài báo.
- $O(NM)$ liên kết là suy luận kỳ vọng khi bậc trung bình bị chặn theo $M$, không phải cận cho mọi trạng thái đồ thị.
- Với PQ đoạn đều, cần $m\mid D$; $k^*=2^b$. Không trộn cấu hình 4×8 bit, ngân sách 6 byte và `PQ16x8` của ba phần notebook.
- Xấp xỉ $nprobe\,N/k_c$ chỉ dùng khi danh sách tương đối cân bằng. $nprobe$ không phải số ứng viên.
- `IVF200,PQ16x8np`: giữ đúng chuỗi nguồn; không tự diễn giải hậu tố `np` thành `nprobe`.
- Mọi ví dụ tự dựng phải được tính lại; không gán nó cho slide hoặc bài báo.
- Chỉ dùng `img/lec-07/...` và liên kết deck `lecture-07-chi-muc-hang-xom-gan-dung.html` theo quy ước viewer.

## 12. Kế hoạch tác tử

1. Ba worker GLM độc lập đã lập kế hoạch, ánh xạ nguồn và đề xuất bản đồ chủ đề; lượt bản đồ đầu chạm giới hạn tool-call và được thử lại cùng model trên hồ sơ hẹp.
2. Codex chính đối chiếu trực tiếp hai bài báo, ba bộ slide, notebook, ví dụ và công thức trước khi chấp nhận goal.
3. Writer `deepseek/deepseek-v4-flash-0731` soạn một tệp trong gốc tạm hẹp.
4. Năm reviewer `z-ai/glm-5.3-flash` kiểm nguồn, toán–thuật toán, mạch sư phạm, liên tục và viewer; Codex chính áp dụng sửa đã duyệt, rồi tái kiểm toán/mạch.
5. Dùng `$no-ai-slop` và `$quill` cho bản cuối, không tạo `quill.json`.
6. Kiểm viewer thật; chỉ sau khi đạt mới cập nhật index, commit, push và xác minh SHA `origin/main`.

## 13. Trạng thái

**Hoàn tất.** Ba reader lập kế hoạch/nguồn/chủ đề, writer DeepSeek, năm reviewer GLM và hai lượt tái kiểm GLM đều đã hoàn thành qua OpenRouter với đúng metadata runtime. Codex chính đã sửa bản nháp, biên tập bằng `$no-ai-slop`, rà mạch bằng `$quill`, kiểm viewer thật và chỉ sau đó mới cập nhật index. Không còn lỗi chặn hoặc nghiêm trọng.
