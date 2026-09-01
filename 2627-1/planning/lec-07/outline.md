# Bài 7: Chỉ mục hàng xóm gần đúng

## Mục tiêu và phạm vi

Sau buổi học, sinh viên có thể:

- đặc tả tìm $K$ hàng xóm gần đúng và tính $\operatorname{recall@K}$ trên một tập truy vấn;
- chạy tay tìm kiếm tham lam, tìm kiếm chùm và `SEARCH-LAYER` trên đồ thị lân cận;
- giải thích đặc tả tầng, truy vấn, chèn, chọn lân cận và ba tham số chính của HNSW;
- mã hóa, tái dựng và tính khoảng cách bất đối xứng bằng lượng tử hóa tích (PQ);
- mô tả luồng IVF-PQ và phân tích tác động của $nprobe$;
- so sánh LSH, HNSW, PQ quét đầy đủ và IVF-PQ theo độ thu hồi, độ trễ, thời gian xây dựng và bộ nhớ.

Phạm vi không gồm DiskANN, NSG, Vamana, huấn luyện bộ mã tối ưu, OPQ, lượng tử hóa cộng hoặc bảo đảm độ phức tạp phổ quát cho HNSW.

## Tiên quyết

- Bài 5–6: véc-tơ, khoảng cách, MinHash và băm nhạy cảm cục bộ (LSH).
- Đồ thị có hướng, hàng đợi ưu tiên, xác suất và k-means cơ bản.
- Véc-tơ Euclid và phép tách véc-tơ thành các nhóm tọa độ.

## Ký hiệu khóa

| Ký hiệu | Nghĩa |
|---|---|
| $Y=\{y_1,\ldots,y_N\}\subset\mathbb R^D$ | cơ sở dữ liệu véc-tơ |
| $q$ | véc-tơ truy vấn |
| $K$ | số hàng xóm cần trả về |
| $N_K(q),\widehat N_K(q)$ | tập đúng và tập gần đúng |
| $ef$ | bề rộng danh sách động của `SEARCH-LAYER` |
| $M$ | số lân cận mục tiêu của một đỉnh HNSW |
| $m_L>0$ | hệ số mức điều khiển phân phối tầng HNSW |
| $M_{max,0},M_{max}$ | giới hạn bậc ở tầng 0 và các tầng trên; đều ít nhất bằng $M$ |
| $efConstruction,efSearch$ | bề rộng khi chèn và khi truy vấn tầng đáy |
| $m$ | số lượng tử hóa con trong công thức PQ |
| $k^*=2^b$ | số tâm trong mỗi bộ mã con |
| $k_c$ | số tâm thô của IVF |
| $nprobe$ | số danh sách đảo được mở cho một truy vấn |

## Mạch phần giảng — 120 phút

| Cụm | Trang | Phút | Sản phẩm học tập |
|---|---:|---:|---|
| Tình huống và đặc tả ANN | P00–A03 | 20 | chuyển truy hồi trên 10 tỷ véc-tơ thành bài toán, phép đo và khung so sánh |
| HNSW | H00–H13 | 48 | chạy tìm kiếm, phát biểu bất biến, truy vấn, chèn, tham số và giới hạn |
| Lượng tử hóa tích | Q00–Q10 | 30 | mã hóa, tái dựng, ví dụ ADC số, công thức bộ nhớ và giới hạn quét tuyến tính |
| IVF-PQ | I00–I04 | 14 | phân vùng, mã hóa phần dư, $nprobe$ và luồng truy vấn |
| Kết luận | C00 | 8 | đối chiếu bốn cơ chế bằng cùng bốn trục đo; trả lời trực tiếp bài toán mở đầu bằng lựa chọn theo chất lượng truy vấn, chi phí dựng và bộ nhớ |

Ghi chú nhất quán: cận kỳ vọng $O(NM)$ cạnh của HNSW là suy luận ở mục 4.2.3 bài báo HNSW dưới giả thiết bậc trung bình bị chặn theo $M$, không phải kết quả trực tiếp cho mọi đồ thị.

## Bài tập — 60 phút

| Nguồn trực tiếp | Trang | Phút | Điều chỉnh |
|---|---:|---:|---|
| Princeton runbook lớp 8, ô nền 0–4, 17, 21–24; “Product Quantization” và “Manual reconstruction”, ô 82–97 | R00–R03 | 20 | mỗi sinh viên chuẩn bị `d,xt,xb,xq,gt` trên chính kernel sẽ dùng; đọc và làm PQ ở ô 82–97 (có thể chạy 83–95 rồi hoàn thiện 96–97); thời gian máy được báo riêng |
| “Compare options for fixed code_size”, ô 98–99 | R04–R05 | 20 | giữ ngân sách 6 byte và ba giá trị $M_{PQ}$; chạy trước ô 99 trên cùng kernel nếu huấn luyện chậm |
| “IVFPQ index”, ô 148–155 | R06–R08 | 20 | tách xây dựng ở ô 149–151 khỏi truy vấn ở ô 152–155; dùng `xt,xb,xq,gt` từ trạng thái nền |

R00 chỉ mở phần, không tính thời lượng. Lời giải và hướng dẫn chấm nằm trong ghi chú diễn giả.

## So sánh và chọn nguồn theo cụm

| Cụm đích | Nguồn đã so sánh | Nguồn chọn và lý do |
|---|---|---|
| P01–A02 | Stanford BIODS 271 trang 17–18; Princeton lớp 8 trang 2–5; hai bài báo gốc | BIODS chỉ cung cấp cấu hình 10 tỷ véc-tơ và danh mục chỉ mục; Princeton cho khung đánh đổi; bài báo chốt đặc tả và recall. Không dùng tuyên bố giảm độ chính xác 20–30% của BIODS vì thiếu điều kiện. |
| A03 | MMDS Chương 3; Stanford CS246 bài 04; Princeton lớp 9 trang 4–6 | MMDS/CS246 chỉ làm cầu nối LSH từ Bài 6; không lặp lại chứng minh hoặc tham số banding. |
| H00–H13 | Princeton lớp 9 trang 7–19; Malkov–Yashunin trang 1–7 | Princeton được chọn cho trực giác đồ thị; ví dụ chạy tay được dựng lại từ cơ chế và ghi rõ. Bài báo gốc chốt `SEARCH-LAYER`, truy vấn, chèn, chọn cạnh, giả thiết và giới hạn. |
| Q00–Q10 | Princeton lớp 8 trang 8–33; Jégou–Douze–Schmid trang 1–4 | Princeton được chọn cho chuỗi VQ → PQ → ADC và hình dễ Việt hóa; bài báo gốc chốt định nghĩa, công thức mã, tái dựng và khoảng cách. |
| I00–I04 | Princeton lớp 8 trang 20–22, 54–55; bài báo PQ trang 6 | Princeton cho luồng; bài báo chốt lượng tử hóa thô, mã phần dư và IVFADC. |
| R01–R08 | Princeton runbook lớp 8; tài liệu Faiss về cú pháp factory | Dùng trực tiếp ba nhiệm vụ của notebook; tài liệu Faiss chỉ kiểm chứng hậu tố `np`. Không thay dữ kiện hoặc dùng kết quả cố định làm đáp án; trạng thái chạy trước phải đến từ đúng notebook và kernel của sinh viên. |

Stanford BIODS 271 không được dùng làm nguồn thuật toán vì chỉ tóm tắt và có mệnh đề hiệu năng thiếu điều kiện. Slide Princeton rõ hơn cho giảng dạy, còn hai bài báo gốc là nguồn chuẩn cho giả mã và điều kiện. MMDS và Stanford CS246 chỉ xuất hiện ở cầu nối LSH.

## Kiểm kê hình

Chín SVG được dùng trong HTML: quy mô véc-tơ, độ thu hồi tại K, tham lam so với chùm, các tầng HNSW, trạng thái `SEARCH-LAYER`, luồng chèn, phép chia PQ, bảng tra ADC và luồng IVF-PQ. Bảng bốn cơ chế ở C00 được dựng bằng HTML để giữ cỡ chữ máy chiếu. Không dùng ảnh raster.

## Giới hạn nguồn bài tập

Runbook lớp 8 có bài trực tiếp cho PQ và IVF-PQ nhưng không có bài HNSW. Theo quy định không tự đặt dữ kiện, phần recitation chỉ dùng các nhiệm vụ PQ/IVF-PQ của nguồn. Khoảng trống này được ghi trong nhật ký rà soát; phần HNSW được kiểm tra bằng các câu ngắn trong phần giảng, không tính vào 60 phút recitation.

## Bản đồ chủ đề ghi chú tự học

| `note-topic-id` | Nhãn | Chủ đề | Sản phẩm |
|---|---|---|---|
| `L07-N01` | cầu nối | Quy mô, ANN, phá hòa, recall@K | đặc tả và đo chất lượng |
| `L07-N02` | cầu nối | LSH trong bản đồ cơ chế | phân biệt ngăn, đường, mã |
| `L07-N03` | cốt lõi | Tìm kiếm tham lam | chạy tay và nhận diện cực tiểu cục bộ |
| `L07-N04` | cốt lõi | Tìm kiếm chùm và `SEARCH-LAYER` | giả mã, bất biến, dừng, giới hạn |
| `L07-N05` | cốt lõi | Kiến trúc, truy vấn, chèn HNSW | đặc tả các pha và chọn/cắt cạnh |
| `L07-N06` | cốt lõi | Tham số và chi phí HNSW | đánh đổi có điều kiện |
| `L07-N07` | cốt lõi | Từ VQ đến PQ | mã hóa và tái dựng |
| `L07-N08` | cốt lõi | ADC và bộ nhớ PQ | bảng tra, chi phí, giới hạn quét |
| `L07-N09` | cốt lõi | IVF-PQ | phần dư, $nprobe$, top-$K$ |
| `L07-N10` | cốt lõi | So sánh bốn cơ chế | lựa chọn theo bốn trục |
| `L07-N11` | cầu nối | Ba nhiệm vụ runbook | sản phẩm thực hành truy nguyên được |

Đồ thị tiên quyết tách thành nhánh đồ thị `N03→N06` và nhánh nén `N07→N09`, rồi hội tụ ở `N10`. `N11` chỉ phụ thuộc nhánh PQ/IVF-PQ vì nguồn không có bài HNSW.
