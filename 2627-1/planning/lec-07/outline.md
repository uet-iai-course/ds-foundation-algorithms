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
| $k$ | số tâm của một bộ mã VQ (Q00–Q03) |
| $x$ | điểm mới khi chèn HNSW (H10, H10B); véc-tơ trong ví dụ VQ/PQ (Q00–Q06) |
| $y$ | phần tử của kho; biến lân cận/ứng viên trong giả mã (H05, H06) |
| $\rho=e^{-1/m_L}$ | tỷ lệ điểm giữ lại ở tầng trên (H08, H13); thay $p$ của bài báo để khỏi trùng tên điểm $p1,\ldots,p11$ |
| $a(y)$, $L_i$, $r(y)$, $\widetilde q_i$, $P$ | tâm thô được gán, danh sách đảo, phần dư, truy vấn dư, tập danh sách được mở (I01–I04) |

## Mạch phần giảng — 120 phút

Cập nhật sau lượt duyệt từng trang ngày 03/10/2026; thứ tự là thứ tự trong deck.

| Phần | Trang | Phút | Sản phẩm học tập |
|---|---|---:|---|
| 1. Mở đầu | P00–P02 | 6 | tình huống truy hồi ngữ nghĩa $10^{10}$ véc-tơ, chi phí quét; dàn bài và ba mục tiêu |
| 2. Bài toán và phép đo | A00–A03 | 11 | đặc tả tìm đúng/ANN, recall@K, bốn trục đánh giá, hai thừa số chi phí |
| 3. Tìm kiếm trên đồ thị HNSW | H00, H01, H03, H03B, H04–H06, H06B, H07, H09, H08, H10, H10B, H11–H13 | 44 | đồ thị lân cận, tham lam, chùm, SEARCH-LAYER và bất biến, cạnh dài, nhiều tầng, truy vấn, rút tầng, chèn, lân cận đa dạng, tham số, chi phí |
| 4. Lượng tử hóa tích | Q00, Q02–Q05, Q07, Q06, Q08–Q10 | 28 | VQ, giới hạn bộ mã lớn, PQ, kích thước, ADC, bảng tra, giới hạn quét đủ |
| 5. IVF-PQ | I00–I02, I04, I03 | 16 | tệp đảo, chọn danh sách, phần dư, thuật toán, chi phí thay số |
| 6. Tổng kết | C00–C02 | 15 | so sánh bốn cấu trúc trên tình huống mở đầu; sáu câu tự kiểm |

Gộp: H02 vào H01; Q01 vào Q00. Tách: H03 thành H03 và H03B; H10 thành H10 và H10B. Thêm: H06B, C01, C02. Chuyển: H08 sau H09; Q06 sau Q07; I03 sau I04.

Ghi chú nhất quán: kết luận $\log N$ của HNSW giả thiết mỗi tầng là đồ thị Delaunay chính xác và bậc trung bình bị chặn (mục 4.2.1 bài báo HNSW); bộ nhớ cạnh tính theo kỳ vọng số tầng trên $\rho/(1-\rho)$.

## Bài tập — 60 phút

| Nguồn trực tiếp | Trang | Phút | Điều chỉnh |
|---|---:|---:|---|
| Princeton runbook lớp 8, ô nền 0–4, 17, 21–24; “Product Quantization” và “Manual reconstruction”, ô 82–97 | R00–R03 | 20 | mỗi sinh viên chuẩn bị `d,xt,xb,xq,gt` trên chính kernel sẽ dùng; đọc và làm PQ ở ô 82–97 (có thể chạy 83–95 rồi hoàn thiện 96–97); thời gian máy được báo riêng |
| “Compare options for fixed code_size”, ô 98–99 | R04–R05 | 20 | giữ ngân sách 6 byte và ba giá trị $m\in\{4,8,16\}$ (Faiss `M`); dự đoán $D/m$, $k^*$ trước khi chạy; chạy trước ô 99 trên cùng kernel nếu huấn luyện chậm |
| “IVFPQ index”, ô 148–155 | R06–R08 | 20 | tách xây dựng ở ô 149–151 khỏi truy vấn ở ô 152–155; dùng `xt,xb,xq,gt` từ trạng thái nền |

R00 chỉ mở phần, không tính thời lượng. Lời giải và hướng dẫn chấm nằm trong ghi chú diễn giả.

## So sánh và chọn nguồn theo cụm

| Cụm đích | Nguồn đã so sánh | Nguồn chọn và lý do |
|---|---|---|
| P01–A02 | Stanford BIODS 271 trang 17–18; Princeton lớp 8 trang 2–5; hai bài báo gốc | BIODS chỉ cung cấp cấu hình 10 tỷ véc-tơ và danh mục chỉ mục; Princeton cho khung đánh đổi; bài báo chốt đặc tả và recall. Không dùng tuyên bố giảm độ chính xác 20–30% của BIODS vì thiếu điều kiện. |
| A03 | MMDS Chương 3; Stanford CS246 bài 04; Princeton lớp 9 trang 4–6 | MMDS/CS246 chỉ làm cầu nối LSH từ Bài 6; không lặp lại chứng minh hoặc tham số banding. |
| H00–H13 (gồm H06B, H10B) | Princeton lớp 9 trang 7–19 (tr.11–13 cho ví dụ một chiều H06B); Malkov–Yashunin trang 1–8 | Princeton được chọn cho trực giác đồ thị; ví dụ chạy tay được dựng lại từ cơ chế và ghi rõ. Bài báo gốc chốt `SEARCH-LAYER`, truy vấn, chèn, chọn cạnh, giả thiết và giới hạn. |
| Q00–Q10 | Princeton lớp 8 trang 8–33; Jégou–Douze–Schmid trang 1–4 | Princeton được chọn cho chuỗi VQ → PQ → ADC và hình dễ Việt hóa; bài báo gốc chốt định nghĩa, công thức mã, tái dựng và khoảng cách. |
| I00–I04 | Princeton lớp 8 trang 20–22; lớp 9 trang 5; bài báo PQ trang 6–7 | Princeton cho luồng và gợi ý $k_c\approx\sqrt N$; bài báo chốt lượng tử hóa thô, mã phần dư, gán đa và thuật toán tìm kiếm IVFADC. Ví dụ bốn ô do học phần dựng. |
| C00–C02 | tổng hợp các nguồn trên | Số liệu so sánh suy ra từ H13, Q07, Q10, I03; câu tự kiểm dùng dữ kiện học phần dựng, $D=960$ (GIST, bài báo PQ) và $k_c=32\,000$ (Princeton lớp 9 tr.5). |
| R01–R08 | Princeton runbook lớp 8; tài liệu Faiss về cú pháp factory | Dùng trực tiếp ba nhiệm vụ của notebook; tài liệu Faiss chỉ kiểm chứng hậu tố `np`. Không thay dữ kiện hoặc dùng kết quả cố định làm đáp án; trạng thái chạy trước phải đến từ đúng notebook và kernel của sinh viên. |

Stanford BIODS 271 không được dùng làm nguồn thuật toán vì chỉ tóm tắt và có mệnh đề hiệu năng thiếu điều kiện. Slide Princeton rõ hơn cho giảng dạy, còn hai bài báo gốc là nguồn chuẩn cho giả mã và điều kiện. MMDS và Stanford CS246 chỉ xuất hiện ở cầu nối LSH.

## Kiểm kê hình

Mười chín SVG, tất cả sinh bằng `2627-1/img/lec-07/generate_svg.py` (lượt duyệt 03/10/2026 thay toàn bộ chín SVG viết tay cũ): `truy-hoi-ngu-nghia` (P01), `do-thu-hoi` (A01), `do-thi-vi-du`, `do-thi-tham-lam`, `do-thi-chum`, `do-thi-ef2` (đồ thị bảy đỉnh H00–H06), `search-layer-trang-thai` (H04), `canh-dai-mot-chieu` (H06B), `do-thi-nhieu-tang`, `do-thi-nhieu-tang-gon` (H07, H09), `chen-vi-du` (H10), `lan-can-da-dang` (chỉ dùng trong ghi chú bài giảng §5 từ 2026-10-16, khi trang H11 bị bỏ; giữ tệp), `luong-tu-hoa-vec-to` (Q00), `pq-tach-doan` (Q04), `pq-vi-du`, `pq-vi-du-adc` (Q05, Q06), `tep-dao`, `tep-dao-o`, `tep-dao-du` (I00–I02). Mỗi trang dùng lại ví dụ đều có hình hoặc dữ kiện trên trang. Bảng (bốn trục, bảng tra, so sánh, phiếu bài tập) dựng bằng HTML. Không dùng ảnh raster.

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

## Tên mạch và trang tiêu đề mạch (2026-10-14)

Mỗi mạch trừ mạch mở đầu mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên trùng từng chữ với trang Nội dung. Deck 56 trang.

| N | Tên mạch | Trang tiêu đề mạch | Trang nội dung đầu mạch |
|---:|---|---|---|
| 1 | Mở đầu | P00 (trang bìa) | — |
| 2 | Bài toán hàng xóm gần đúng | AT | A00 |
| 3 | Tìm kiếm trên đồ thị HNSW | HT | H00 |
| 4 | Lượng tử hóa tích (PQ) | QT | Q00 |
| 5 | Tệp đảo kết hợp PQ (IVF-PQ) | IT | I00 |
| 6 | So sánh và tự kiểm tra | CT | C00 |
| 7 | Bài tập thực hành | RT | R00 |

## Sửa toàn diện theo chuẩn 2026-10-14

Câu luận đề trên trang bìa (quyết định của điều phối viên): "HNSW giảm số véc-tơ được đo, lượng tử hóa tích (PQ) giảm chi phí mỗi phép đo; đổi lại, có thể bỏ lỡ hàng xóm thật." Ba mục tiêu học tập giữ nguyên chữ, khớp ghi chú bài giảng.

| Mạch | Tên | Trang (thứ tự deck) | Số trang | Phút |
|---|---|---|---:|---:|
| 1 | Mở đầu | P00, P03, P02, P04, P05, P01 | 6 | 8 |
| 2 | Bài toán hàng xóm gần đúng | AT, A00–A03 | 5 | 11 |
| 3 | Tìm kiếm trên đồ thị HNSW | HT, H00, H01, H03, H03B, H04–H06, H06B, H07, H09, H08, H10, H10B, H11–H14 | 18 | 42 |
| 4 | Lượng tử hóa tích (PQ) | QT, Q00, Q02–Q05, Q07, Q06, Q08, Q09, Q11, Q10 | 12 | 28 |
| 5 | Tệp đảo kết hợp PQ (IVF-PQ) | IT, I00–I02, I04, I05, I03 | 7 | 16 |
| 6 | Tổng kết và tự kiểm tra | CT, C03, C00, C04, C01, C02, C05 | 7 | 15 |
| 7 | Bài tập thực hành | RT, R00–R08 | 10 | 60 |

Deck 65 trang (55 giảng + 10 bài tập). Mạch 6 đổi tên từ "So sánh và tự kiểm tra" (trang Nội dung P04 và trang tiêu đề mạch CT đã cập nhật); bảng "Tên mạch và trang tiêu đề mạch" phía trên là bản trước đợt sửa.

- **Mạch mở đầu:** thêm P03 "Tiên quyết và quy ước" (ánh xạ mục "Tiên quyết": LSH của Bài 06, tính cộng theo tọa độ; đồ thị có hướng, hàng đợi ưu tiên và k-means ở ghi chú diễn giả), P05 "Vấn đề trung tâm"; tách P02 thành "Mục tiêu học tập" và P04 "Nội dung"; P01 thành trang ví dụ.
- **Mạch kết luận:** thêm C03 "Kết quả và giả thiết không được bỏ", C04 "Câu trả lời cho vấn đề trung tâm", C05 "Nguồn và tài liệu đọc"; C00 đổi sang khuôn `Thuật toán | Đầu vào | Bảo đảm | Chi phí`; C01, C02 thành "Câu hỏi tự kiểm tra". Không ghi công mmds.org vì bài không neo MMDS; không dòng nối Bài 08 vì `sources/source.md` chỉ nêu thứ tự (Bài 8 mở mạch "Dòng dữ liệu và cửa sổ"), không nêu quan hệ nội dung.
- **Tách:** H13 → H13 + H14; Q09 → Q09 + Q11; I04 → I04 + I05.
- **Bảng ký hiệu (bổ sung):** 1 TB là $10^{12}$ byte, 1 GB là $10^9$ byte; tọa độ viết bằng dấu chấm phẩy, ví dụ $(1{,}7;\ 0{,}4)$; $n_c$ là số véc-tơ được đo (định nghĩa ở mô hình chi phí A03 từ lượt 2026-10-27; dùng lại ở Q11, Q10, I03).
- **Thuật ngữ giải nghĩa ở lần đầu trên mặt trang:** HNSW (P03), ANN (A00), độ thu hồi (recall) (A01), tìm kiếm chùm (beam search) (H03), VQ (Q00), ADC (Q08), IVF (I00), MSE (R04); LSH viết "băm nhạy cảm theo tính cục bộ (LSH)" như Bài 06.
- **Mạch 7:** nhãn Thực hành (`practice-badge`, lớp có sẵn); RT 0,5 phút lấy từ R01.

## Lượt sửa sau ba báo cáo rà (2026-10-14)

- **Luận đề:** bỏ "(PQ)": "HNSW giảm số véc-tơ được đo, lượng tử hóa tích giảm chi phí mỗi phép đo; đổi lại, có thể bỏ lỡ hàng xóm thật." (25 token). Tên đầy đủ kèm "(PQ)" chuyển sang mục tiêu 2 ở P02 (lần đầu PQ xuất hiện sau bìa).
- **Vấn đề trung tâm và câu trả lời:** P05 nêu 122,88 TB, ≈30,7 giây mỗi truy vấn và ngân sách giả định của học phần 6 TB bộ nhớ, 10 ms mỗi truy vấn; C04 trả lời bằng TB và giây (HNSW ≈125,5 TB; PQ quét đủ 5,12 TB, ≈5,12 giây; IVF-PQ 5,2 TB, ≈3,6 ms). PQ bị loại vì thời gian, không vì bộ nhớ.
- **Đặc tả ANN (A00):** trả tối đa $K$ điểm; hai nguồn sai số tương ứng hai thừa số chi phí: đo một phần kho, đo bằng khoảng cách xấp xỉ.
- **Thuật ngữ:** "chấm một mã" là phép đo xấp xỉ qua bảng tra (Q11); $n_c$ định nghĩa ở A03 (từ lượt 2026-10-27), dùng ở Q11, Q10 ($n_c=N$), I03 ($n_c\approx nprobe\,N/k_c$). Đồ thị Delaunay giải nghĩa trong ghi chú H14 (từ lượt rà lại mạch 3, 2026-10-28; mặt trang H14 ghép mỗi thừa số với giả thiết của nó). Mục "Thuật ngữ giải nghĩa" ở trên đổi hai điểm: A00 giữ "(approximate nearest neighbor)" nhưng không dùng chữ viết tắt ANN trên mặt trang; P03 viết "LSH" theo câu của điều phối viên, tên đầy đủ "băm nhạy cảm theo tính cục bộ" nằm trong ghi chú P00, P03 và đã giải nghĩa ở Bài 06.
- **Bộ nhớ IVF-PQ** $(512+8)\cdot10^{10}$ byte $=5{,}2$ TB tính ở I03 (mạch 5), trước C00 và C04.
- **Ghi chú bài giảng:** không sửa trong lượt này. Điểm cần đồng bộ khi sửa ghi chú: ngân sách giả định 6 TB và 10 ms; bảo đảm LSH $1-(1-p_1^r)^b$ trong bảng so sánh; "phần dư thường nhỏ hơn" (năng lượng trung bình).

## Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)

Bản hiện hành; các bảng mạch phía trên là lịch sử. Căn cứ: đặc tả sửa của điều phối viên (Phương án A). Mạch "Bài toán hàng xóm gần đúng" cũ gộp vào mạch mở đầu (bỏ trang tiêu đề `AT`); mạch HNSW cũ tách thành mạch đồ thị một tầng và mạch nhiều tầng (thêm trang tiêu đề `NT`). Deck 65 → 63 trang (54 giảng, 9 bài tập). Chi tiết từng trang, âm tiết trước → sau và ngoại lệ ở `storyboard.md`, mục cùng tên.

### Tên mạch và trang tiêu đề mạch

| N | Tên mạch (khớp P04) | Trang tiêu đề mạch | Dòng dẫn | Trang nội dung đầu mạch |
|---:|---|---|---|---|
| 1 | Bài toán hàng xóm gần đúng | P00 (bìa) | — | P03 |
| 2 | Tìm kiếm trên đồ thị lân cận | HT, `id="mach-2"` | Muốn đo ít véc-tơ mà vẫn tới điểm gần $q$, phải đi trên đồ thị lân cận và giữ nhiều hướng. | H00 |
| 3 | Đồ thị thế giới nhỏ phân tầng (HNSW) | NT, `id="mach-3"` | Muốn tới vùng gần $q$ sau ít bước, phải đặt các tầng thưa có cạnh dài phía trên đồ thị chứa mọi điểm. | H06B |
| 4 | Lượng tử hóa tích (PQ) | QT, `id="mach-4"` | giữ | Q00 |
| 5 | Tệp đảo kết hợp PQ (IVF-PQ) | IT, `id="mach-5"` | giữ | I00 |
| 6 | Tổng kết và tự kiểm tra | CT, `id="mach-6"` | giữ | C03 |
| 7 | Bài tập thực hành | RT, `id="mach-7"` | giữ | R00 |

### Mạch phần giảng — 120 phút

| Mạch | Trang (thứ tự deck) | Số trang | Phút | Sản phẩm học tập |
|---|---|---:|---:|---|
| 1. Bài toán hàng xóm gần đúng | P00, P03, P02, P04, P05, P01, A00, A00B, A01, A02, A03 | 11 | 20,5 | tình huống $10^{10}$ véc-tơ; đặc tả tìm đúng (A00) và tìm gần đúng (A00B, tách từ A00); recall@K; bốn trục; mô hình hai thừa số và cột "Lưu véc-tơ gốc" |
| 2. Tìm kiếm trên đồ thị lân cận | HT, H00, H01, H03, H03B, H04, H05, H06 | 8 | 19 | đồ thị lân cận, tham lam, chùm, SEARCH-LAYER, bất biến |
| 3. Đồ thị thế giới nhỏ phân tầng (HNSW) | NT, H06B, H07, H09, H08, H10, H10B, H12, H14, H13 | 10 | 23 | cạnh dài, nhiều tầng, truy vấn, phân phối tầng, chèn, tham số, số phép đo ($\log N$ có điều kiện), bộ nhớ (98% véc-tơ gốc) |
| 4. Lượng tử hóa tích (PQ) | QT, Q00, Q02, Q03, Q04, Q05, Q07, Q06, Q08, Q09, Q11, Q10 | 12 | 28 | VQ, giới hạn bộ mã lớn, PQ, kích thước, ADC, bảng tra, giới hạn quét đủ |
| 5. Tệp đảo kết hợp PQ (IVF-PQ) | IT, I00, I01, I02, I04, I05, I03 | 7 | 17 | tệp đảo, chọn danh sách, phần dư, thuật toán, vết, chi phí |
| 6. Tổng kết và tự kiểm tra | CT, C03, C00, C04, C01, C05 | 6 | 12,5 | bảng giả thiết, bảng thuật toán, câu trả lời vấn đề trung tâm, ba câu tự kiểm, nguồn |

Bỏ: AT (gộp mạch), H11 "Chọn lân cận đa dạng" (phần tùy chọn của thuật toán; nội dung và hình giữ ở ghi chú bài giảng §5), C02 (gộp vào C01). Đổi thứ tự: H14 trước H13, để mạch 3 kết bằng "véc-tơ gốc chiếm khoảng 98% bộ nhớ" mà Q00 nhận vào. Đổi tên trang: H08 "Phân phối tầng của điểm mới"; A00B "Tìm hàng xóm gần đúng" (khác tên mạch 1).

### Bài tập — 60 phút

| Nguồn trực tiếp | Trang | Phút |
|---|---|---:|
| ô nền 0–4, 17, 21–24; ô 82–97 | RT, R00, R01, R02 | 20 (0,5 + 0 + 5,5 + 14) |
| ô 98–99 | R04, R05 | 20 |
| ô 148–155 | R06, R07, R08 | 20 |

R03 gộp vào R02: ba điều kiện khớp của tái dựng thành phần giải thích và tiêu chí chấm trong ghi chú R02, vì sổ nguồn ô 96–97 chỉ yêu cầu biểu thức tái dựng và kiểm `True`. Mọi trang bài tập đặt "Câu hỏi:" ngay dưới nhãn Thực hành.

### Kiểm kê hình (2026-10-16)

Mười tám SVG được deck dùng (không đổi tệp nào); `lan-can-da-dang.svg` còn trong `img/lec-07/` và chỉ được ghi chú bài giảng dùng. Không ảnh raster.

### Thuật ngữ ở lần đầu trên mặt trang (thay mục cùng tên của đợt 2026-10-14)

LSH ở P03 ("băm nhạy cảm theo tính cục bộ (LSH)"); PQ ở P02; IVF-PQ ở P04; tìm gần đúng (approximate nearest neighbor) ở A00B, không dùng viết tắt ANN trên mặt trang; độ thu hồi (recall) ở A01; tìm kiếm chùm (beam search) ở H03; HNSW ở H07 ("Đồ thị thế giới nhỏ phân tầng (Hierarchical Navigable Small World, HNSW)"); VQ ở Q00; ADC ở Q08; IVF ở I00; MSE ở R04. Dòng "Ký hiệu: HNSW là …" ở P03 bị bỏ; trước H07, "HNSW" chỉ xuất hiện trong tên mạch 3.

### Lượt sửa 2 sau rà lại (2026-10-16)

- Tên mạch 3 (P04, trang tiêu đề NT, `aria-label`): **"Đồ thị thế giới nhỏ phân tầng (HNSW)"**, cùng mẫu tên mạch 4, 5; hai bảng phía trên của mục 2026-10-16 đã sửa tại chỗ (tên cũ: "Đồ thị nhiều tầng HNSW"). Dòng dẫn NT: "Muốn tới vùng gần $q$ sau ít bước, phải đặt các tầng thưa có cạnh dài phía trên tầng 0." Từ khóa thứ năm: "Tham số và chi phí".
- I05 đổi tiêu đề thành "Ví dụ: truy vấn IVF-PQ".
- Ý tưởng chèn ("Chèn là truy vấn với $x$, rồi nối …") chuyển từ H10B lên dòng đầu H10, trước ví dụ; $efConstruction$ giải nghĩa trên H10.
- H03: $C$ chứa các đỉnh từng vào $W$ nhưng chưa mở; $ef$ là bề rộng chùm. Quy tắc dừng ở dạng "Gợi ý:" trong hộp câu hỏi H03B.
- Ký hiệu điểm của ví dụ một chiều thống nhất dạng $p1,\ldots,p11$ (khớp nhãn SVG); phá hòa theo chỉ số $i$ của $y_i$.
- Kết quả HNSW phát biểu "số phép đo trung bình là $O(\log N)$" dưới giả thiết Delaunay chính xác và bậc bị chặn (H14, C03). Từ 2026-10-28, H14 ghi đủ ba giả thiết: phân phối tầng (số tầng), Delaunay chính xác và tầng rút độc lập với vị trí (số bước mỗi tầng trung bình $\le1/\rho=M$), bậc trung bình bị chặn.
- Số trang, thứ tự trang và thời lượng không đổi. Chi tiết và âm tiết trước → sau ở `storyboard.md`, mục "Lượt sửa 2 sau rà lại".

### Lượt sửa 3 (2026-10-16)

- Dòng dẫn NT: "Muốn tới vùng gần $q$ sau ít bước, phải đặt các tầng thưa có cạnh dài phía trên đồ thị chứa mọi điểm." (bảng mạch phía trên đã sửa tại chỗ).
- Giả mã truy vấn H09 và chèn H10B dùng $ep$ là tập điểm vào, khớp đầu vào của SEARCH-LAYER (H04).
- H10 nêu hai pha bằng hai dòng ($ef=1$ ở tầng $>\ell$; $efConstruction$ và nối $M$ lân cận ở tầng $\le\ell$) trước ví dụ.

### Lượt biên tập theo bản đánh giá giảng dạy (2026-10-27)

- **Mạch 1** có 12 trang: P00, P03, P02, P04, P05, P01, A00, A00B, A01, **A01B**, A02, A03; 19,5 phút (trước 20,5; một phút chuyển sang mạch 2). Bảng "Mạch phần giảng — 120 phút" phía trên giữ bản cũ cho tới khi mọi mạch xong; số liệu hiện hành ở `storyboard.md`, mục cùng tên.
- **Thuật ngữ mới:** độ thu hồi trung bình (mean recall) ở A01B, $\overline{\operatorname{recall@K}}$ trên tập truy vấn $Q$. **Ký hiệu mới:** $Q$ là tập truy vấn (A01B); $n_c$ (số véc-tơ được đo) gọi tên lần đầu ở mô hình chi phí A03, trước Q11.
- **Ví dụ chạy tay mới:** năm điểm với $d(q,y_i)=2{,}5;\ 1{,}2;\ 3{,}0;\ 0{,}8;\ 1{,}7$, $K=3$, $N_3(q)=\{y_4,y_2,y_5\}$ (A00); chỉ mục trả $\{y_4,y_5,y_1\}$ (A00B), $\operatorname{recall@3}=2/3$ (ghi chú A01).
- **Sau rà lại mạch 1:** "chỉ mục (index)" định nghĩa trên mặt trang A00B ("cấu trúc dựng sẵn trên $Y$, quyết định véc-tơ nào được đo và đo thế nào"); P03 viết dạng tổng theo nhóm $\|x-y\|_2^2=\sum_{j=1}^{m}\sum_{i\in G_j}(x_i-y_i)^2$ với $G_1,\ldots,G_m$ là phân hoạch của $\{1,\ldots,D\}$ ($m$ cùng nghĩa số đoạn của PQ ở Q04). Từ "bỏ sót" dùng cho điểm không được đo; "thiếu" dùng khi so hai tập.
- **Mạch 2** có 10 trang: HT, H00, H01, **H01B** (Cực tiểu cục bộ), H03, H03B, **H03C** (vết tìm kiếm chùm, bước cuối), H04, H05, H06; 21 phút (trước 19). Hình mới `cuc-tieu-cuc-bo.svg`. Thuật ngữ: "cực tiểu cục bộ" định nghĩa trên mặt trang H01B (trước ở Kết luận H01); "thấy" (đã tính $d(\cdot,q)$) và "mở" (đã duyệt danh sách lân cận) phân biệt ở H03 và H04.
- **Mạch 3** có 11 trang: NT, H06B, H07, H09, H08, **H08B** (Ví dụ: số điểm mỗi tầng của kho mười tỷ véc-tơ), H10, H10B, H12, H14, H13; 21 phút (trước 23). Mô hình chi phí truy vấn HNSW viết ba thừa số (số tầng × số bước mỗi tầng × bậc) ở H14.
- **Mạch 4** giữ 12 trang; 27 phút (trước 28). "Sai số tái dựng $\|x-\widehat x\|^2$" gọi tên ở Q00; k-means có dòng "Nhắc lại:" ở Q02; $n_c$ ở Q11 là "Nhắc lại:" của A03; đoạn $x^{(j)}$ là nhóm $G_j$ của P03 (Q04 ghi chú, Q08 mặt trang).
- **Mạch 5** có 8 trang: IT, I00, I01, I02, **I02B** (Ví dụ: truy vấn dư theo đúng danh sách), I04, I05, I03; 19 phút (trước 17). Tổng phần giảng về lại 120 phút (19,5 + 21 + 21 + 27 + 19 + 12,5).
- **Mạch 6** có 7 trang: CT, C03, C00, C04, C01, **C01B** (Câu hỏi tự kiểm tra, câu 3–4), C05; 12,5 phút. Phần giảng 60 trang, 120 phút. Mục tiêu 1 (P02) thêm năng lực "giải thích hai nguồn thiếu điểm", kiểm bằng câu tự kiểm 4.
