# Goal brief — Ghi chú Bài 01

## 1. Goal

Xây dựng ghi chú tự học độc lập cho Bài 01, giúp sinh viên đặc tả và chứng minh thuật toán xử lý dữ liệu không vừa bộ nhớ, phân biệt các tầng của lời giải, phân tích mô hình chi phí và nhận diện tín hiệu giả khi số phép thử tăng.

## 2. Vấn đề trung tâm

Cho kho nhật ký web gồm các bản ghi $(u_i,s_i)$ với kích thước dữ liệu $D$ lớn hơn bộ nhớ $M$. Cần tính tổng byte theo máy chủ bằng một lượt quét, chứng minh kết quả đúng và xác định chi phí tính toán, bộ nhớ, truy cập dữ liệu.

Từ tình huống này, ghi chú xây dựng kết luận rộng hơn: một lời giải dữ liệu lớn chỉ có ý nghĩa khi đặc tả, biểu diễn, thuật toán, mô hình chi phí và bảo đảm được nêu rõ. Khi khai phá nhiều mẫu, tính khả thi thống kê cũng phải được kiểm tra.

## 3. Bằng chứng hoàn thành

- Đặc tả đầy đủ đầu vào, đầu ra, điều kiện trước, điều kiện sau và mô hình truy cập của thuật toán quét–cộng dồn.
- Có vết chạy kiểm tra được và chứng minh tính đúng bằng bất biến tiền tố.
- Phân biệt được bài toán, biểu diễn, thuật toán, cài đặt và kết quả.
- Phân tích được thời gian, bộ nhớ, số lượt quét và bảo đảm sai số.
- Dựng đúng mô hình ngẫu nhiên cho ví dụ hồ sơ lưu trú và tính được kỳ vọng số biến cố trùng.
- Mọi mệnh đề kỹ thuật có nguồn đến trang hoặc trang chiếu cụ thể.
- Các phần nối thành một tuyến lập luận liên tục và ghi chú đọc được mà không cần mở slide.
- Các tiêu chí trên chỉ dùng để duyệt goal; tiêu chí bàn giao cuối vẫn tuân theo `AGENTS.md`.

## 4. Đầu ra hoàn tất

- `2627-1/materials/lec-01/lecture-note.md`;
- SVG mới hoặc SVG được điều chỉnh trong `2627-1/img/lec-01/`;
- cập nhật phần ghi chú trong:
  - `2627-1/planning/lec-01/outline.md`;
  - `2627-1/planning/lec-01/storyboard.md`;
  - `2627-1/planning/lec-01/review-log.md`;
- hạ tầng viewer cần thiết cho ghi chú đầu tiên;
- nhóm tài nguyên Bài 01 trong `2627-1/index.html`.

## 5. Đối tượng và tiên quyết

Có thể giả định:

- lập trình và vòng lặp;
- mảng, bảng băm và tệp;
- ký hiệu độ phức tạp;
- đại số tuyến tính và xác suất cơ bản.

Cần khôi phục ngắn trước khi sử dụng:

- $\binom{n}{k}$ và phép đếm cặp;
- tính tuyến tính của kỳ vọng;
- giả thiết độc lập;
- phân biệt thời gian kỳ vọng của bảng băm với cận trường hợp xấu;
- véc-tơ, khoảng cách Euclid và số chiều ở mức nhập môn.

## 6. Phạm vi nguồn

| Nguồn | Phần dùng | Vai trò | Mức thẩm quyền |
|---|---|---|---|
| `sources/source.md` | Bài 01, mục tiêu, tiên quyết, thứ tự học phần | Chốt phạm vi cấp học phần | Cao nhất |
| MMDS 3e, Chương 1 | Trang 1–8, 13, 17–19 | Mô hình dữ liệu, tín hiệu giả, bài tập, lưu trữ thứ cấp và định tuyến | Nguồn nội dung chính |
| BHK | PDF trang 9–12; Hình 2.2 ở PDF trang 17 | Dữ liệu hiện đại, giả định RAM và trực giác cao chiều | Nguồn bổ sung đã xác minh |
| Stanford CS246 `01-intro.pdf` | Trang chiếu 2–10 và 62 | Dạng dữ liệu, phạm vi và lược đồ tổng byte theo máy chủ | Nguồn trực quan bổ trợ |
| `2627-1/planning/lec-01/outline.md` và `storyboard.md` | Toàn bộ | Giữ ký hiệu và mạch đã kiểm định | Nguồn biên tập thứ cấp |
| Bộ trang chiếu Bài 01 | Toàn bộ | Đối chiếu thuật ngữ, ví dụ và chuyển ý | Không thay giáo trình làm nguồn sơ cấp |

Quyết định về BHK: dùng PDF trang 17 cho Hình 2.2. Các công thức và định lý ở trang 18–21 chỉ để đọc thêm, không đưa vào tuyến chính.

## 7. Bản đồ chủ đề

| Mã | Chủ đề | Nhãn | Kết nối vào | Kết nối ra | Quyết định |
|---|---|---|---|---|---|
| N01 | Kho nhật ký không vừa bộ nhớ | cốt lõi | Mục tiêu học phần | Mô hình truy cập | giữ |
| N02 | Dữ liệu hiện đại và giới hạn RAM | cầu nối | N01 | Thuật toán một lượt | giữ |
| N03 | Thuật toán quét–cộng dồn | cốt lõi | N01–N02 | Các tầng của lời giải | giữ |
| N04 | Bài toán, biểu diễn, thuật toán, cài đặt, kết quả | cốt lõi | N03 | Các loại mô hình | giữ |
| N05 | Mô hình thống kê và mô hình dữ liệu theo truy vấn | cốt lõi | N04 | Mô hình chi phí | giữ |
| N06 | Ba chi phí và một bảo đảm | cốt lõi | N05 | Giới hạn thống kê | giữ |
| N07 | Tín hiệu giả và kỳ vọng số biến cố trùng | cốt lõi | N06 | Bài tập mô hình hóa | giữ |
| N08 | Bài tập MMDS 1.2.1–1.2.2 | cốt lõi | N07 | Định tuyến cao chiều | giữ |
| N09 | Trực giác về số chiều lớn | cầu nối | N08 | Bản đồ học phần | giữ ở mức định tuyến |
| N10 | Bản đồ học phần và chọn mô hình theo điểm nghẽn | cầu nối | N09 | Áp dụng khung trong các bài sau | giữ |

## 8. Chủ đề bổ sung đề xuất

Không có chủ đề bổ sung bắt buộc.

- Định lý về thể tích, vùng xích đạo và gần trực giao trong BHK trang 18–21: `đọc thêm`. Đưa vào tuyến chính sẽ vượt mục tiêu định tuyến của Bài 01.
- Bất đẳng thức Markov cho $\Pr(X\ge 1)\leq\mathbb{E}[X]$: dùng như một cầu nối ngắn trong N08 khi cần diễn giải bài tập; không tạo chủ đề riêng.
- Bất biến tiền tố của quét–cộng dồn: giữ trong N03 và ghi rõ đây là lập luận được xây dựng từ đặc tả, không phải định lý trích nguyên văn từ Stanford.

## 9. Khuôn trình bày

| Chủ đề | Thành phần bắt buộc | Không áp dụng |
|---|---|---|
| N01–N02 | nhu cầu, định nghĩa dữ liệu, trực quan, ví dụ, kiểm tra | định lý, thuật toán, chứng minh |
| N03 | toàn bộ chuỗi, gồm đặc tả, vết chạy, giả mã, bất biến, chứng minh, chi phí và trường hợp biên | không |
| N04–N05 | định nghĩa, ví dụ, trực quan, ứng dụng và kiểm tra | thuật toán, chứng minh |
| N06 | định nghĩa mô hình chi phí, trực quan, ứng dụng và kiểm tra | thuật toán và chứng minh mới |
| N07 | mô hình xác suất, ví dụ, suy diễn kỳ vọng, trực quan và kiểm tra | thuật toán; định lý Bonferroni đầy đủ |
| N08 | bài tập, gợi ý, lời giải, kiểm tra giả thiết và giới hạn | thuật toán mới |
| N09 | nhu cầu, công thức khoảng cách, Hình 2.2 và trực giác | chứng minh thể tích, định lý equator |
| N10 | bản đồ, bốn phép kiểm tra và cách áp dụng khung | các thành phần hình thức khác |

## 10. Ngoài phạm vi

- MapReduce, PageRank, sketching, lấy mẫu, MinHash và Locality-Sensitive Hashing.
- Stanford CS246 trang chiếu 32–61 và 63–70.
- Các chứng minh cao chiều trong BHK trang 18–21.
- TF.IDF, hàm băm, chỉ mục và luật lũy thừa của MMDS Chương 1.
- Sổ tay mã, chương trình minh họa hoặc bộ dữ liệu mới.
- Thay dữ kiện toán học của MMDS Bài 1.2.1–1.2.2.
- Tạo `quill.json`.

## 11. Rủi ro và điểm đã quyết định

- Planning và HTML đã chuẩn hóa vị trí Hình 2.2 thành BHK PDF trang 17.
- “Quét–cộng dồn” là thuật ngữ nội bộ; lần đầu phải nói rõ nguồn chỉ mô tả thao tác và không đặt tên thuật toán này.
- Năm tầng của lời giải mở rộng đặc tả cấp học phần bằng “cài đặt” và “kết quả”; phải ghi đây là quyết định biên tập đã có trong outline.
- Bonferroni chỉ được trình bày như nguyên lý phi hình thức theo MMDS, không nâng thành định lý thống kê đầy đủ.
- `materials/lec-01/` và hạ tầng viewer cục bộ đã được tạo và kiểm định.
- Ví dụ bốn bản ghi quét–cộng dồn là ví dụ tự dựng từ lược đồ Stanford, không phải dữ liệu thực nghiệm.

## 12. Kế hoạch tác tử

| Giai đoạn | Vai trò | Hồ sơ | Trạng thái |
|---|---|---|---|
| Lập kế hoạch | OpenRouter reader | `plan` | hoàn tất |
| Ánh xạ nguồn | OpenRouter reader | `source` | hoàn tất |
| Bản đồ chủ đề | OpenRouter reviewer | `review` | hoàn tất |
| Soạn trong thư mục tạm | OpenRouter writer | `write` | hoàn tất |
| Năm lượt rà độc lập | OpenRouter reviewer | `review` | hoàn tất |
| Sửa tuần tự | OpenRouter writer | `write` | hoàn tất |
| Biên tập bản cuối | Codex chính với `$no-ai-slop` | tự kiểm `no-ai-slop/eval.md` | hoàn tất |
| Rà lại phần thay đổi | OpenRouter reviewer | `recheck` | hoàn tất |
| Kiểm định viewer và công bố | Codex chính | kiểm tra cục bộ | hoàn tất |

Mọi worker được chấp nhận đều dùng `z-ai/glm-5.3-flash`; `requested_model` và `observed_model` trùng nhau, provider là OpenRouter.

Trước lượt `recheck`, Codex chính phải đọc toàn bộ `lecture-note.md` và dùng `$no-ai-slop` để biên tập bản cuối. Bước này xóa lời dẫn rỗng, câu tổng kết lặp, nhịp câu máy móc, siêu bình luận và mọi hướng dẫn kiểu quy trình không phục vụ việc tự học. Giữ nguyên mệnh đề, dữ kiện, ký hiệu, giả thiết, ví dụ, kết quả và nguồn. Sau khi sửa, tự kiểm trực tiếp theo `no-ai-slop/eval.md`; nếu có mục không đạt, sửa lại trước khi giao reviewer rà phần thay đổi.

## 13. Trạng thái

`hoàn tất`

Các nguồn bắt buộc và trang được dùng đã được kiểm tra trực tiếp. Không có chủ đề bổ sung cần nguồn mới. Hình 2.2 dùng BHK PDF trang 17; phần trang 18–21 chỉ để đọc thêm. Bản cuối đã qua năm lượt rà độc lập, hai lượt tái kiểm, biên tập `no-ai-slop`, kiểm định viewer và cập nhật index.
