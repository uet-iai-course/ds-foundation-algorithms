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
| P00 | 0 | Nhận diện bài, thuật ngữ và cầu nối từ Bài 6. | LSH → HNSW, PQ, IVF-PQ | `sources/source.md`; MMDS Ch.3 |
| P01 | 4 | Mở bằng tình huống truy hồi dữ liệu lớn, nêu đầu vào, đầu ra, bộ nhớ và câu kiểm tra nút thắt. | $10^{10},3072$ → 122,88 TB thô, 5,12 TB mã, vẫn cần chỉ mục | BIODS tr.17; tình huống dựng từ cấu hình nguồn |
| P02 | 3 | Nêu ba sản phẩm quan sát được và mạch bài. | tình huống → đặc tả, giải thích, lựa chọn | `sources/source.md` |
| A00 | 4 | Hình thức hóa $1\le K\le N$, mã định danh phân biệt, phá hòa và chi phí Euclid. | $Y,q,d,K$ → bài toán ANN; $\Theta(ND)$ khi một khoảng cách là $\Theta(D)$ | PQ paper tr.1; HNSW paper tr.1 |
| A01 | 3 | Khóa phép đo chất lượng trước khi so thuật toán. | hai tập K phần tử → recall@K | HNSW paper tr.1 |
| A02 | 3 | Ngăn so sánh một chiều bằng bốn trục đo. | recall → chất lượng, độ trễ, xây dựng, bộ nhớ | Princeton 08 tr.2–5; Princeton 09 tr.2 |
| A03 | 3 | Phân biệt ba cơ chế và giữ LSH làm cầu nối. | Bài 6 → ngăn, đường, mã | MMDS Ch.3; Stanford 04; Princeton 09 tr.4–6 |
| H00 | 3 | Nêu biểu diễn đồ thị, trạng thái và phép tiến. | véc-tơ → đỉnh và cạnh | Princeton 09 tr.7–10 |
| H01 | 4 | Chạy tay tham lam trên đồ thị có khoảng cách nhất quán. | $e:9\to a:7\to b:5$ → dừng cục bộ, bỏ $z:1$ | Princeton 09 tr.8,11–13; ví dụ dựng từ cơ chế nguồn |
| H02 | 3 | Ghi từng trạng thái để tách điều kiện dừng cục bộ khỏi tối ưu toàn cục. | lân cận từng bước → cực tiểu cục bộ | Princeton 09 tr.8–13 |
| H03 | 3 | Theo vết $C,W$ với $ef=3$ để giữ nhánh s và thoát cực tiểu. | $e,a,b,s$ → mở $t$, rồi $u,z$ | Princeton 09 tr.9; HNSW paper alg.2 |
| H04 | 3 | Đặc tả tầng hữu hạn, $ef\ge1$, $1\le|ep|\le ef$ và kiểu đầu ra của `SEARCH-LAYER`. | tập điểm vào không rỗng → W khởi tạo hợp lệ | HNSW paper tr.4 |
| H05 | 5 | Đưa giả mã và tính lại phần tử xa nhất của $W$ sau mỗi cập nhật. | $V,C,W$ → thuật toán tầng có ngưỡng hiện thời | HNSW paper alg.2, tr.4 |
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
| I02 | 3 | Dùng truy vấn dư và bảng ADC riêng cho từng danh sách. | $q_i=q-\mu_i$, $r(y)=y-\mu_i$ → chấm mã trong $L_i$ | PQ paper §IV-A, tr.6 |
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
