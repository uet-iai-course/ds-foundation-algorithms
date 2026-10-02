# Storyboard Bài 7

## Hành trình khái niệm

- **HNSW:** tình huống P01 → vấn đề A00, H00 → ví dụ tham lam và vết chạy chùm H01–H03 → hợp đồng H04 → thuật toán H05 → bất biến và ngưỡng thay đổi H06 → truyền điểm vào qua tầng H07–H09 → đặc tả chèn tổng quát H10 → chọn cạnh H11 → tham số, chi phí và giới hạn H12–H13 → đối chiếu C00.
- **Lượng tử hóa tích:** tình huống P01 → vấn đề Q00 → ví dụ chạy tay VQ Q01 → hình thức hóa Q02 → giới hạn bộ mã Q03 → trực giác chia đoạn Q04 → mã PQ Q05 → ví dụ ADC số Q06 → không gian mã và bộ nhớ Q07 → ADC hình thức và bảng tra Q08–Q09 → giới hạn quét Q10 → ứng dụng IVF-PQ I00–I04 → đối chiếu C00.
- **IVF-PQ:** vấn đề Q10, I00 → phân vùng và ví dụ chọn tâm I01 → truy vấn dư riêng từng danh sách I02 → chi phí I03 → thuật toán trả mã định danh I04 → thực nghiệm R06–R08.
- **LSH:** chu trình đã hoàn tất ở Bài 6; A03 chỉ nhắc cơ chế và C00 dùng lại để so sánh. Không áp dụng chạy tay hoặc chứng minh lại trong Bài 7 vì sẽ lặp nguồn.

Tình huống mở bài là truy hồi ngữ nghĩa với $N=10^{10}$ véc-tơ, $D=3072$, số thực 32 bit, đoạn 6 chiều và mã tâm 8 bit từ cấu hình BIODS trang 17. Đầu vào là véc-tơ truy vấn; đầu ra là $K$ mục gần truy vấn trong giới hạn bộ nhớ và độ trễ. Dữ kiện truyền sang A00 để nêu chi phí quét, Q07 để tính bộ nhớ mã, Q10 để chỉ ra quét mã vẫn tuyến tính, I00–I04 để cần phân vùng và C00 để đối chiếu cấu trúc. Đầu ra được đo bằng $\operatorname{recall@K}$ cùng độ trễ, chi phí xây dựng và bộ nhớ.

## Từng trang phần giảng

| ID | Phút | Lý do tồn tại và bước tiến | Đầu vào → sản phẩm | Nguồn |
|---|---:|---|---|---|
| P00 | 0 | Nhận diện bài, ba cấu trúc và cầu nối từ bài toán tìm cặp của Bài 6 sang bài toán truy vấn. | LSH → HNSW, PQ, IVF-PQ | BIODS tr.16–18; Princeton 08–09 |
| P01 | 4 | Mở bằng tình huống truy hồi ngữ nghĩa: quy trình nhúng, dung lượng kho và chi phí quét một truy vấn. | $10^{10},3072$ → 122,88 TB, $3{,}07\cdot10^{13}$ tọa độ mỗi truy vấn | BIODS tr.16–17; tình huống dựng từ cấu hình nguồn |
| P02 | 3 | Nêu sáu phần của bài và ba mục tiêu học tập có sản phẩm cụ thể. | tình huống → dàn bài, mục tiêu | `sources/source.md` |
| A00 | 4 | Đặc tả tìm đúng ($K$-NN, phá hòa theo mã định danh), chi phí quét $\Theta(ND)$ và nới điều kiện thành tìm gần đúng (ANN). | $Y,q,d,K$ → $N_K(q)$, $\widehat N_K(q)$; $3{,}07\cdot10^{13}$ tọa độ | HNSW paper tr.1; PQ paper tr.1 |
| A01 | 3 | Định nghĩa độ thu hồi tại $K$, tính trên ví dụ năm phần tử và kiểm tra bằng một câu hỏi. | hai tập $K$ phần tử → recall@K; $3/5$, câu hỏi $2/5$ | HNSW paper tr.1 |
| A02 | 3 | Nêu bốn trục đánh giá, điều kiện giữ cố định và kiểm tra bằng so sánh A/B. | recall → chất lượng, truy vấn, xây dựng, bộ nhớ | Princeton 08 tr.2–5; Princeton 09 tr.2 |
| A03 | 3 | Tách chi phí truy vấn thành số véc-tơ được đo nhân chi phí một phép đo; gắn LSH, HNSW, PQ, IVF-PQ vào thừa số mỗi cấu trúc giảm. | $\Theta(ND)$ → hai thừa số → bản đồ cấu trúc | MMDS Ch.3; Princeton 09 tr.4,5,7; Princeton 08 tr.2 |
| H00 | 3 | Định nghĩa đồ thị lân cận trên đồ thị ví dụ bảy đỉnh; nêu dữ liệu lưu và ý tưởng đi tới đỉnh gần $q$ hơn. | véc-tơ → đỉnh, cạnh, điểm vào | Princeton 09 tr.7–8 |
| H01 | 7 | Chạy tay tham lam trên đồ thị ví dụ (hình và bảng vết cùng trang); định nghĩa cực tiểu cục bộ. Gộp H02 cũ. | $e:9\to a:7\to b:5$ → dừng ở cực tiểu cục bộ, bỏ $z:1$ | Princeton 09 tr.8, 11–13; ví dụ dựng từ cơ chế nguồn |
| H03 | 5 | Định nghĩa ngắn $C$, $W$, $ef$; chạy tay tìm kiếm chùm $ef=3$ đủ 7 lần mở trên đồ thị ví dụ; câu hỏi $ef=2$. | $e,a,b,s,t,u,z$ → $W=\{z,u,t\}$ | Princeton 09 tr.9; HNSW paper alg.2 |
| H04 | 3 | Đặc tả đầu vào, đầu ra và ba tập trạng thái của `SEARCH-LAYER`; hình trạng thái thật của ví dụ sau khi mở $b$. | $ep$, $ef$, $\ell_c$ → $W$; $C,W\subseteq V$ | HNSW paper tr.4 |
| H05 | 5 | Giả mã `SEARCH-LAYER` theo Thuật toán 2; nối dòng tính lại ngưỡng $f$ với bước mở $s$ của ví dụ. | $V,C,W$ → thuật toán; ngưỡng $8\to7$ | HNSW paper alg.2, tr.4 |
| H06 | 4 | Phát biểu bất biến đúng phạm vi; dùng vết H03 để thấy ngưỡng đổi 8→7. | tiền tố duyệt → trạng thái hợp lệ, không lặp đỉnh | suy ra từ alg.2 |
| H07 | 4 | Truyền điểm vào từ tầng cao xuống tầng thấp trước khi mở rộng ở tầng đáy. | $ep_2\to ep_1\to ep_0\to W$ | HNSW paper Fig.1, tr.3; Princeton 09 tr.17–18 |
| H08 | 2 | Hình thức hóa $U\in(0,1]$, $m_L>0$ và ý nghĩa hệ số mức. | $U,m_L$ → tầng tối đa và độ thưa | HNSW paper alg.1, §4.1, tr.4–5 |
| H09 | 4 | Đặc tả truy vấn HNSW và điều kiện $efSearch\ge K$. | tìm tầng → K kết quả | HNSW paper alg.5, tr.5 |
| H10 | 4 | Đặc tả chỉ mục rỗng, pha tầng trên $ef=1$, pha cập nhật `efConstruction`, chọn ≤M, nối, cắt bằng $M_{max,0}/M_{max}$, truyền $ep\leftarrow W$ và đổi điểm vào khi $\ell>L$. | điểm mới → HNSW cập nhật; danh sách kề sau cắt có thể không đối xứng | HNSW paper alg.1, tr.4–5 |
| H11 | 3 | Nêu quy tắc đa dạng và lý do không chỉ chọn gần nhất. | ứng viên → tối đa M cạnh nhiều hướng | HNSW paper alg.4, tr.5 |
| H12 | 2 | Ánh xạ ba tham số sang ba chi phí. | M, efConstruction, efSearch → núm điều khiển | HNSW paper §4.1, tr.5–7 |
| H13 | 4 | Tách $O(ND)$ lưu véc-tơ, kỳ vọng $O(NM)$ liên kết — suy luận mục 4.2.3 dưới giả thiết bậc trung bình bị chặn theo $M$ — và giới hạn kết luận log. | thuật toán → điều kiện áp dụng; trường hợp xấu tuyến tính | HNSW paper §4.2.3, tr.7; Princeton 09 tr.2 |
| Q00 | 3 | Đặt bài toán nén mất dữ liệu trước PQ. | véc-tơ → mã và tâm tái dựng | Princeton 08 tr.8–10; PQ paper tr.2 |
| Q01 | 3 | Chạy tay lượng tử hóa véc-tơ với ba tâm. | ba khoảng cách → mã 1, sai số 0,25 | suy ra từ định nghĩa nguồn |
| Q02 | 3 | Hình thức hóa phép gán tâm, điều kiện trước/sau và phá hòa. | Q01 → $i(x),\widehat x$ | PQ paper eq.2–5, tr.2 |
| Q03 | 2 | Chỉ ra bộ mã đơn không mở rộng tới mã 64 bit. | $2^{64}$ tâm → bất khả thi | PQ paper tr.3 |
| Q04 | 2 | Cho trực giác chia véc-tơ thành m đoạn và m bộ mã. | $D$ → m không gian con | PQ paper eq.8–9, tr.3; Princeton 08 tr.28–31 |
| Q05 | 3 | Chạy tay mã PQ hai đoạn. | hai bộ mã → mã $(0,1)$ | suy ra từ định nghĩa nguồn |
| Q06 | 3 | Tính ADC số với mã $(0,1)$ từ Q05 và truy vấn đầy đủ. | hai ô tra 0,02 và 0,29 → ADC 0,31 | PQ paper eq.13, tr.4; ví dụ dựng từ cơ chế nguồn |
| Q07 | 4 | Khóa không gian mã, số tâm con, số vô hướng và byte làm tròn. | $m,k^*,D,b$ → $(k^*)^m$, $mk^*$, $k^*D$, $\lceil mb/8\rceil$ | PQ paper tr.3; Princeton 08 tr.32–33 |
| Q08 | 3 | Hình thức hóa ADC và phân biệt phía truy vấn với cơ sở dữ liệu. | truy vấn đầy đủ + mã → khoảng cách gần đúng | PQ paper eq.13, tr.4 |
| Q09 | 2 | Nêu chi phí lập bảng, lưu bảng và chấm mã. | $\Theta(k^*D)$, $\Theta(mk^*)$, $\Theta(m)$ | PQ paper tr.4; Princeton 08 tr.27,31–32 |
| Q10 | 2 | Chỉ ra chi phí tuyến tính và byte mã còn lại ở quy mô P01. | PQ quét đủ → $\Theta(Nm)$, $N\lceil mb/8\rceil$ byte | PQ paper tr.2,6 |
| I00 | 3 | Đặt IVF và PQ vào đúng vai trò. | quét N mã → phân vùng + nén | Princeton 08 tr.20–22,54–55 |
| I01 | 3 | Hình thức hóa miền argmin và chạy ví dụ chọn danh sách gần nhất. | $\mu_0,\mu_1,q$ → mở $L_1$ trước | Princeton 08 tr.21–22; PQ paper tr.6; ví dụ dựng từ cơ chế nguồn |
| I02 | 3 | Dùng truy vấn dư và bảng ADC riêng cho từng danh sách. | $\widetilde q_i=q-\mu_i$, $r(y)=y-\mu_i$ → chấm mã trong $L_i$ | PQ paper §IV-A, tr.6 |
| I03 | 2 | Tách chi phí tâm thô, nprobe bảng ADC và tổng kích thước danh sách; tách riêng phụ phí top-K. | $\Theta(k_cD)+\Theta(nprobe\,k^*D)+\Theta(m\sum_{i\in P}|L_i|)$ | PQ paper tr.6–8 |
| I04 | 3 | Gom thuật toán, điều kiện dừng và trường hợp thiếu K ứng viên. | $q$ → $\min(K,\sum|L_i|)$ mã định danh; đủ K khi tổng ứng viên ≥K | PQ paper §IV, tr.6; Princeton 08 tr.54–55 |
| C00 | 8 | So sánh LSH, HNSW, PQ đầy đủ và IVF-PQ theo lưu/xây, phạm vi quét, núm truy vấn và bốn trục A02. | bốn cơ chế → lựa chọn có điều kiện, không xếp hạng phổ quát | tổng hợp các nguồn |

Tổng phần giảng: **120 phút**.

## Từng trang bài tập

| ID | Phút | Vai trò và sản phẩm hiển thị | Đáp án hoặc hướng dẫn chấm trong notes | Nguồn trực tiếp |
|---|---:|---|---|---|
| R00 | 0 | Nêu notebook, chuỗi ô nền 0–4,17,21–24, trạng thái `d,xt,xb,xq,gt` và quy ước tách thời gian máy. | mỗi sinh viên chạy trước trên chính kernel sẽ dùng; không tạo checkpoint mới | Princeton runbook lớp 8 |
| R01 | 6 | Đọc hai mục “Product Quantization” và “Manual reconstruction”; lập công thức tái dựng véc-tơ tại chỉ số 123. | chỉ số mã chọn tâm ở từng đoạn; `xb` đã có từ ô 17 | ô 82–97 |
| R02 | 9 | Hoàn thiện dòng mã tái dựng, không gọi hàm giải mã. | ghép `pq_centroids[j, xb_codes[123,j]]` theo j | ô 96–97 |
| R03 | 5 | Giải thích ba điều kiện để khớp với giải mã. | đúng thứ tự đoạn, tâm và đủ D tọa độ; rubric 10 điểm | ô 96–97 |
| R04 | 10 | Đọc mục “Compare options for fixed code_size”; dùng kết quả ô 99 đã chạy trước trên cùng kernel. | ba cấu hình 6 byte với d=64; thời gian huấn luyện báo riêng | ô 98–99 |
| R05 | 10 | So sánh MSE, thời gian, dsub và ksub mà không khái quát quá mức. | rubric 10 điểm; không có số cố định | ô 98–99 |
| R06 | 6 | Đọc mục “IVFPQ index”; xây hoặc dùng trạng thái ô 149–151 với `d,xt,xb` đã chuẩn bị. | giải thích cấu hình; thời gian `train` báo riêng | ô 148–151; tài liệu Faiss index factory chỉ kiểm chứng `np` |
| R07 | 9 | Tiếp tục “IVFPQ index” ở ô 152–155 với `xq,gt` từ ô 17,21–24. | $nok/|xq|$; tổng ms, không gắn nhãn độ trễ mỗi truy vấn | ô 152–155 |
| R08 | 5 | Hoàn thiện phiếu báo cáo năm dòng và giải thích xu hướng của phép quét nguồn. | không thêm mục tiêu vận hành hoặc $nprobe$ mới | ô 149–155 |

Tổng recitation: **60 phút**. Bài tập giữ dữ kiện và yêu cầu nguồn; các trang chỉ chia bước và thêm mẫu sản phẩm.

## Storyboard ghi chú tự học

Ghi chú dùng `L07-N01`–`L07-N11` trong outline. Mỗi chủ đề cốt lõi theo vai trò → đặc tả → ví dụ → trực quan → thuật toán/mệnh đề → lập luận đúng → chi phí, giới hạn và kiểm tra.

- `N01–N02` khóa bài toán, phép đo và cầu từ Bài 06; không lặp banding.
- `N03–N06` truyền cùng ví dụ đồ thị từ tham lam sang chùm, `SEARCH-LAYER`, truy vấn và chèn HNSW; bất biến chỉ nói về phần đã thăm.
- `N07–N09` truyền cùng phép chia véc-tơ, mã PQ và bảng ADC sang phần dư IVF-PQ; phân biệt mã, véc-tơ tái dựng và mã định danh trả về.
- `N10` thu hồi tình huống mở bài bằng bốn trục đo, không xếp hạng phổ quát.
- `N11` giữ đúng trạng thái notebook và ba nhiệm vụ nguồn; không thêm bài HNSW hoặc kết quả số cố định.

Các ví dụ đồ thị, ADC và chi phí IVF-PQ do học phần dựng lại hoặc suy ra phải ghi rõ. Mã trang nội bộ và thời lượng không xuất hiện trong ghi chú công khai.

## Chi tiết từng trang (duyệt 03/10/2026)

Mỗi mục ghi: tiêu đề hiện tại; phần; mục đích (việc sinh viên làm được); câu chốt; vai trò trong mạch; kiến thức đầu vào; nội dung và cách thể hiện; kết nối vào–ra; kiểm tra và ghi chú; nguồn; thời lượng; quyết định và lý do. Bảng tóm tắt ở trên giữ thời lượng; khi hai nơi khác nhau, mục chi tiết là bản hiện hành.

### P00 — Chỉ mục hàng xóm gần đúng

- **Phần:** 1, mở đầu. **Vai trò:** nhận diện bài. **Thời lượng:** 0 phút.
- **Mục đích:** gọi đúng tên ba cấu trúc của bài và quan hệ với Bài 06.
- **Câu chốt:** bài xét truy vấn tìm véc-tơ gần nhất trong kho lớn bằng ba cấu trúc HNSW, PQ, IVF-PQ.
- **Đầu vào:** Bài 06 (LSH tìm cặp tương đồng trong một tập). **Thể hiện:** trang tiêu đề; dòng phụ viết đủ tên ba cấu trúc, PQ có diễn giải.
- **Kết nối vào–ra:** từ bài toán tìm cặp của Bài 06 sang bài toán truy vấn; P01 đưa tình huống dữ liệu.
- **Ghi chú diễn giả:** phân biệt tìm cặp và truy vấn; vai trò của ba cấu trúc; nguồn.
- **Nguồn:** BIODS 271 bài 12 tr.16–18; Princeton COS 597A lớp 8–9; hai bài báo gốc.
- **Quyết định:** sửa nhẹ. Dòng phụ cũ “HNSW, lượng tử hóa tích và IVF-PQ” chưa giải thích PQ; ghi chú cũ gọi PQ là “nén khoảng cách” (PQ nén véc-tơ) và ghi sai mã học phần “COS579A”.

### P01 — Truy hồi ngữ nghĩa trên mười tỷ véc-tơ

- **Phần:** 1, mở đầu. **Vai trò:** tình huống dữ liệu, nêu vấn đề. **Thời lượng:** 4 phút.
- **Mục đích:** mô tả truy hồi ngữ nghĩa thành bài toán tìm véc-tơ gần $q$ và tính dung lượng kho cùng số tọa độ một lượt quét phải xử lý.
- **Câu chốt:** quét toàn kho $10^{10}$ véc-tơ 3072 chiều cho mỗi truy vấn tốn $3{,}07\cdot10^{13}$ lượt xử lý tọa độ trên 122,88 TB dữ liệu.
- **Đầu vào:** véc-tơ, khoảng cách (Bài 05–06). **Thể hiện:** hình `truy-hoi-ngu-nghia.svg` (đoạn văn và câu truy vấn qua cùng mô hình nhúng → kho véc-tơ và $q$ → $K$ đoạn gần nhất); hai thẻ số; hộp câu hỏi.
- **Kết nối vào–ra:** nhận bài toán truy vấn từ P00; giao $N$, $D$ và chi phí quét cho A00 (hình thức hóa $\Theta(ND)$), Q07 và Q10 (bộ nhớ mã PQ), C00 (thu hồi tình huống).
- **Kiểm tra:** thời gian một lượt quét với giả định $10^{12}$ tọa độ/giây; đáp án 30,7 giây trong ghi chú, ghi rõ tốc độ là giả định.
- **Nguồn:** BIODS 271 bài 12 tr.16 (quy trình truy hồi dày đặc), tr.17 (cấu hình $N$, $D$, 32 bit).
- **Quyết định:** sửa. Hình cũ `quy-mo-vector.svg` đưa mã PQ, 512 đoạn, 8 bit và 5,12 TB trước khi PQ được định nghĩa; câu hỏi cũ giả định sẵn khái niệm “mã”; chưa giải thích véc-tơ từ đâu ra; thiếu chi phí quét. Hình cũ được giữ trong ghi chú tự học ở mục PQ, chờ quyết định ở Q07/Q10.

### P02 — Nội dung và mục tiêu

- **Phần:** 1, mở đầu. **Vai trò:** định hướng. **Thời lượng:** 3 phút.
- **Mục đích:** nêu được thứ tự sáu phần và ba việc phải làm được sau buổi học.
- **Câu chốt:** đồ thị giảm số véc-tơ phải đo, PQ giảm chi phí mỗi phép đo, IVF-PQ ghép hai cách; ba mục tiêu là đặc tả và đo, chạy tay, tính chi phí và chọn chỉ mục.
- **Đầu vào:** tình huống P01. **Thể hiện:** bố cục `agenda-slide` như Bài 06: danh sách phần bên trái, ba mục tiêu đánh số bên phải.
- **Kết nối vào–ra:** nhận bài toán truy vấn từ P01; mở phần 2 (A00).
- **Ghi chú diễn giả:** vai trò từng phần; mục tiêu nào được kiểm ở phần nào.
- **Nguồn:** `sources/source.md` (LLO1 Bài 7). **Quyết định:** viết lại. Ba thẻ cũ “Đặc tả / Giải thích / Lựa chọn” không có dàn bài; “chạy tay tìm kiếm” chưa nói tìm trên cấu trúc nào; “PQ đầy đủ”, “bốn trục” dùng trước khi định nghĩa.

### A00 — Bài toán $K$ hàng xóm gần nhất

- **Phần:** 2, bài toán và phép đo (khái niệm/mô hình). **Vai trò:** hình thức hóa. **Thời lượng:** 4 phút.
- **Mục đích:** viết đặc tả tìm đúng và tìm gần đúng, tính chi phí quét đầy đủ.
- **Câu chốt:** tìm đúng cần $\Theta(ND)$; tìm gần đúng trả $K$ điểm có thể thiếu hàng xóm thật để chỉ đo một phần kho.
- **Đầu vào:** $N=10^{10}$, $D=3072$ (nhắc lại số, không dẫn chiếu trang trước); khoảng cách Euclid. **Thể hiện:** dòng đầu vào; hai thẻ song song “Tìm đúng”, “Tìm gần đúng (ANN)”; dòng chi phí thay số.
- **Kết nối vào–ra:** hình thức hóa tình huống P01; giao $N_K(q)$ và $\widehat N_K(q)$ cho A01 (độ thu hồi).
- **Ghi chú diễn giả:** ý nghĩa phá hòa; mô hình chi phí đếm tọa độ; HNSW dùng khoảng cách tổng quát, PQ dùng Euclid bình phương; nguồn.
- **Nguồn:** Malkov–Yashunin tr.1 (K-NNS, K-ANNS “cho phép một số ít sai sót”); Jégou–Douze–Schmid tr.1.
- **Quyết định:** sửa. Tiêu đề cũ “Từ tìm đúng sang tìm gần đúng” là câu kể tiến trình; mặt trang cũ chỉ đặc tả tìm đúng, khái niệm gần đúng nằm trong ghi chú; chi phí chưa thay số quy mô.

### A01 — Độ thu hồi tại $K$

- **Phần:** 2. **Vai trò:** định nghĩa, ví dụ, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** tính $\operatorname{recall@K}$ từ tập đúng và tập trả về.
- **Câu chốt:** độ thu hồi là tỷ lệ hàng xóm thật tìm lại được trong $K$ kết quả.
- **Đầu vào:** $N_K(q)$, $\widehat N_K(q)$ từ A00. **Thể hiện:** hình `do-thu-hoi.svg` (hai tập năm phần tử, nét liền/nét đứt) bên trái; công thức, phép thay số và hộp câu hỏi bên phải.
- **Kết nối vào–ra:** đo chất lượng của tập gần đúng ở A00; trục “chất lượng” của A02.
- **Kiểm tra:** chỉ mục trả $\{a,c,f,g,h\}$; đáp án $2/5$ trong ghi chú.
- **Nguồn:** Malkov–Yashunin tr.1; PQ paper tr.7 (quy ước recall@R khác, chỉ ghi ở ghi chú).
- **Quyết định:** sửa. Tiêu đề cũ là câu dài; hình cũ `ann-recall.svg` chữ quá nhỏ khi chiếu; phép tính $3/5$ chỉ có trong hình; chưa có câu hỏi.

### A02 — Bốn trục đánh giá chỉ mục

- **Phần:** 2. **Vai trò:** khung đánh giá, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** nêu bốn trục và điều kiện phải giữ cố định; giải thích vì sao một số đo đơn lẻ không xếp hạng được chỉ mục.
- **Câu chốt:** chỉ mục gần đúng đánh đổi chất lượng lấy thời gian và bộ nhớ, nên phải đo đủ bốn trục trong cùng điều kiện.
- **Đầu vào:** $\operatorname{recall@K}$ (A01). **Thể hiện:** bảng ba cột; hộp câu hỏi A/B.
- **Kết nối vào–ra:** dùng độ thu hồi của A01; bốn trục được dùng lại ở H12–H13, Q10, I03 và bảng so sánh C00.
- **Kiểm tra:** A ($0{,}9$; 5 ms) và B ($0{,}7$; 2 ms); đáp án: chưa xếp hạng được khi chưa có yêu cầu.
- **Nguồn:** Princeton COS 597A lớp 8 tr.2–5; lớp 9 tr.2.
- **Quyết định:** sửa. Tiêu đề cũ “Bốn trục phải đo cùng nhau” mang giọng mệnh lệnh; cột điều kiện có “thứ tự chèn” của HNSW khi HNSW chưa được giới thiệu; lý do cần bốn trục chỉ nằm trong ghi chú.

### A03 — Hai cách giảm chi phí truy vấn

- **Phần:** 2 (kết phần). **Vai trò:** trực giác, bản đồ cơ chế. **Thời lượng:** 3 phút.
- **Mục đích:** chỉ ra mỗi cấu trúc giảm thừa số nào của chi phí truy vấn.
- **Câu chốt:** LSH và HNSW giảm số véc-tơ được đo; PQ giảm chi phí một phép đo và bộ nhớ; IVF-PQ giảm cả hai.
- **Đầu vào:** $\Theta(ND)$ (A00), LSH (Bài 06). **Thể hiện:** đẳng thức chữ chi phí ≈ (số véc-tơ được đo) × (chi phí một phép đo); hai thẻ theo hai thừa số; câu chốt IVF-PQ.
- **Kết nối vào–ra:** kết phần 2; mở phần 3 (HNSW giảm thừa số thứ nhất), phần 4 (PQ giảm thừa số thứ hai), phần 5 (IVF-PQ).
- **Ghi chú diễn giả:** LSH cho truy vấn; giới hạn của từng hướng; LSH không giảng lại.
- **Nguồn:** MMDS Ch.3; Princeton lớp 9 tr.4 (LSH cho truy vấn), tr.5 (phân cụm kèm PQ), tr.7 (đồ thị); lớp 8 tr.2.
- **Quyết định:** viết lại. Tiêu đề cũ “LSH tạo ngăn, HNSW tạo đường, PQ tạo mã” là khẩu hiệu; ba thẻ đưa tên HNSW, PQ mà không nối với chi phí $\Theta(ND)$ vừa tính nên khái niệm xuất hiện đột ngột.

### H00 — Đồ thị lân cận

- **Phần:** 3, tìm kiếm trên đồ thị HNSW (thuật toán). **Vai trò:** mở phần, trực giác. **Thời lượng:** 3 phút.
- **Mục đích:** mô tả đồ thị lân cận (đỉnh, cạnh, điểm vào, dữ liệu lưu) và ý tưởng tìm bằng cách đi tới đỉnh gần $q$ hơn.
- **Câu chốt:** chỉ các đỉnh trên đường đi được đo, nên đồ thị giảm thừa số “số véc-tơ được đo” của A03.
- **Đầu vào:** hai thừa số chi phí (A03). **Thể hiện:** hình `do-thi-vi-du.svg` (tọa độ thật; khoảng cách tới $q$: e 9, a 7, b 5, s 8, t 4, u 2, z 1; cạnh e–a, a–b, e–s, s–t, t–u, u–z) và ba gạch đầu dòng.
- **Kết nối vào–ra:** nhận thừa số thứ nhất từ A03; giao đồ thị ví dụ cho H01–H06 (mỗi trang vẽ lại hình, không dẫn chiếu trang trước).
- **Ghi chú diễn giả:** hướng cạnh, tỷ lệ hình; bộ nhớ $N\cdot(\text{véc-tơ}+4\ \text{byte}\times\text{bậc})$; đồ thị do học phần dựng.
- **Nguồn:** Princeton lớp 9 tr.7 (cấu trúc dữ liệu), tr.8 (tìm tham lam); Malkov–Yashunin tr.2.
- **Quyết định:** viết lại. Bản cũ không có hình; thẻ “Trạng thái: đỉnh đã thăm, ứng viên chưa mở…” đưa trạng thái của SEARCH-LAYER trước cả thuật toán tham lam (khái niệm đột ngột, rà phần 1–2 cũng nêu); không nối với A03.

### H01 — Tìm kiếm tham lam (gộp H02 cũ)

- **Phần:** 3. **Vai trò:** ví dụ chạy tay, nêu giới hạn. **Thời lượng:** 7 phút (gộp 4 + 3 của H01, H02 cũ).
- **Mục đích:** chạy tay tham lam trên đồ thị ví dụ và giải thích vì sao điểm dừng chỉ là cực tiểu cục bộ.
- **Câu chốt:** tham lam dừng ở cực tiểu cục bộ $b:5$ vì không quay lui; $z:1$ nằm trên nhánh $s$ đã bị bỏ ở bước đầu.
- **Đầu vào:** đồ thị lân cận (H00), vẽ lại trên trang bằng `do-thi-tham-lam.svg`. **Thể hiện:** câu quy tắc một bước; hình (đường e→a→b tô cam, đỉnh b viền cam) cạnh bảng vết ba hàng; câu chốt định nghĩa cực tiểu cục bộ.
- **Kết nối vào–ra:** dùng đồ thị H00; tạo nhu cầu giữ nhánh dự phòng cho H03 (tìm kiếm chùm).
- **Ghi chú diễn giả:** định nghĩa cực tiểu cục bộ; vì sao điều kiện dừng không bảo đảm toàn cục; dừng do khoảng cách giảm nghiêm ngặt; 4 phép đo.
- **Nguồn:** Princeton lớp 9 tr.8 (tham lam, cực tiểu cục bộ, không quay lui), tr.11–13.
- **Quyết định:** gộp. H01 cũ (hình + một câu) và H02 cũ (bảng vết) cùng một luận điểm; tách hai trang buộc H02 dựa vào hình ở trang trước. Bảng cũ ghi lân cận của $a$ chỉ là $b:5$, thiếu $e:9$; bảng mới liệt kê đủ. Hình cũ `greedy-beam.svg` (vị trí không theo tỷ lệ khoảng cách, gộp hai thuật toán trong một hình) được thay bằng hai biến thể của đồ thị ví dụ.

### H03 — Tìm kiếm chùm

- **Phần:** 3. **Vai trò:** trực giác và ví dụ chạy tay trước khi hình thức hóa. **Thời lượng:** 5 phút.
- **Mục đích:** chạy tay tìm kiếm chùm, theo dõi $C$ và $W$, giải thích vì sao giữ nhánh dự phòng giúp thoát cực tiểu cục bộ.
- **Câu chốt:** $s$ còn trong $C$ khi nhánh $b$ hết lân cận mới, nên tìm kiếm chùm $ef=3$ đi tiếp tới $z$; $ef=1$ trùng tham lam.
- **Đầu vào:** đồ thị ví dụ, vẽ lại bằng `do-thi-chum.svg`; khái niệm cực tiểu cục bộ (H01). **Thể hiện:** dòng định nghĩa $C$, $W$, $ef$; hình cạnh bảng vết 7 hàng (lớp `ann-compact`); hộp câu hỏi.
- **Kết nối vào–ra:** giải quyết giới hạn của H01; giao vết $C$, $W$ cho đặc tả H04, giả mã H05 và bất biến H06.
- **Kiểm tra:** $ef=2$; đáp án: dừng khi đỉnh kế tiếp $s{:}8$ xa hơn $a{:}7$, trả $\{b,a\}$ (mô phỏng lại theo Thuật toán 2).
- **Nguồn:** Princeton lớp 9 tr.9; Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Bản cũ dùng $C$, $W$, “hàng đợi” trước khi định nghĩa; không có hình; vết dừng ở $s$, phần còn lại chỉ ở ghi chú; câu chốt dài hai dòng.

### H04 — Đặc tả SEARCH-LAYER

- **Phần:** 3. **Vai trò:** hình thức hóa. **Thời lượng:** 3 phút.
- **Mục đích:** nêu đầu vào, đầu ra, điều kiện trước và ba tập trạng thái của `SEARCH-LAYER`; nhận ra tìm kiếm chùm vừa chạy là một lời gọi của nó.
- **Câu chốt:** `SEARCH-LAYER` trả tối đa $ef$ đỉnh gần $q$ nhất trong các đỉnh đã thấy, không phải trong toàn tầng.
- **Đầu vào:** vết chùm $ef=3$ (H03), nhắc lại bằng hình `search-layer-trang-thai.svg` (V = {e, a, b, s}, C = {s}, W = {b, a, s}). **Thể hiện:** hình bên trái; ba dòng đầu vào/đầu ra/trạng thái bên phải.
- **Kết nối vào–ra:** hình thức hóa H03; giao đặc tả cho giả mã H05 và bất biến H06; tham số $\ell_c$ được dùng lại khi có nhiều tầng (H07–H10).
- **Ghi chú diễn giả:** $\ell_c=0$ khi chỉ có một đồ thị; vì sao $1\le|ep|\le ef$; đầu ra chỉ về đỉnh đã thấy; đọc hình.
- **Nguồn:** Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Tiêu đề cũ “Hợp đồng của SEARCH-LAYER” dịch sát “contract”, học phần dùng “đặc tả”; “tầng hữu hạn $\ell_c$” xuất hiện trước khái niệm tầng mà không giải thích; hình cũ `search-layer.svg` chữ nhỏ, không gắn với ví dụ; $V$ xuất hiện lần đầu không định nghĩa.

### H05 — Giả mã SEARCH-LAYER

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 5 phút.
- **Mục đích:** đọc giả mã, chỉ ra dòng khởi tạo, điều kiện dừng, điều kiện chấp nhận và vì sao tính lại ngưỡng $f$.
- **Câu chốt:** $f$ là ngưỡng chấp nhận và phải tính lại sau mỗi thay đổi của $W$; ở ví dụ ngưỡng đổi từ $s{:}8$ sang $a{:}7$ khi mở $s$.
- **Đầu vào:** đặc tả và ba tập (H04). **Thể hiện:** một khối giả mã 13 dòng (`data-trim`); câu chốt nối một bước của ví dụ với dòng tính lại $f$ (nhắc lại $W=\{b,a,s\}$ bằng giá trị, không dẫn chiếu trang).
- **Kết nối vào–ra:** cài đặt đặc tả H04; giao các dòng giả mã cho bất biến H06 và cho lời gọi trong truy vấn H09, chèn H10.
- **Ghi chú diễn giả:** vì sao tính lại $f$; lập luận khi `break` mọi đỉnh của $W$ đã mở; dừng ở đó là đánh đổi; tính dừng.
- **Nguồn:** Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Tiêu đề cũ “SEARCH-LAYER cập nhật ngưỡng sau mỗi điểm” là câu mô tả; giả mã cũ dùng tên `hàng_đợi_gần_nhất`, `lân_cận` và dồn hai thao tác vào một dòng; không có liên hệ với ví dụ.
