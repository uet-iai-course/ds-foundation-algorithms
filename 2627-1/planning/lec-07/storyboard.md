# Storyboard Bài 7

## Hành trình khái niệm

- **HNSW (thứ tự hiện hành, 03/10/2026):** thừa số “số véc-tơ được đo” A03 → đồ thị lân cận H00 → tham lam, cực tiểu cục bộ H01 (gộp H02) → tìm kiếm chùm H03 → đặc tả H04 → giả mã H05 → bất biến H06 → cạnh dài H06B → đồ thị nhiều tầng H07 → giả mã truy vấn H09 → rút tầng H08 → ví dụ chèn H10 → giả mã chèn H10B → lân cận đa dạng H11 → tham số H12 → chi phí H13 → đối chiếu C00.
- **Lượng tử hóa tích (thứ tự hiện hành, 03/10/2026):** nhu cầu từ H13 → VQ, ví dụ ba tâm và câu hỏi Q00 (gộp Q01) → đặc tả và chi phí Q02 → giới hạn bộ mã lớn Q03 → định nghĩa PQ Q04 → ví dụ mã hóa Q05 → kích thước, so với VQ, kho $10^{10}$ véc-tơ Q07 → ví dụ ADC Q06 → công thức ADC Q08 → bảng tra Q09 → giới hạn quét đầy đủ Q10 → IVF-PQ I00–I04 → đối chiếu C00.
- **IVF-PQ (thứ tự hiện hành, 03/10/2026):** giới hạn quét đủ Q10 → tệp đảo, ví dụ bốn ô I00 → gán và chọn danh sách, câu hỏi bỏ sót $y_3$ I01 → phần dư, truy vấn dư I02 → thuật toán, vết, recall@3 I04 → chi phí thay số I03 → so sánh C00 → tự kiểm C01–C02 → thực nghiệm R06–R08.
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
| H06 | 4 | Phát biểu và chứng minh bất biến “$W$ là $\min(ef,|V|)$ đỉnh của $V$ gần $q$ nhất” (khởi tạo, duy trì, khi dừng); minh họa giới hạn bằng lần chạy $ef=2$. | vết $ef=2$ → $W$ đúng trên $V$, $z\notin V$ | suy ra từ alg.2 |
| H06B | 3 | Thêm trang: ví dụ một chiều cho thấy cạnh dài giảm số bước tham lam từ 6 xuống 3; động cơ của các tầng HNSW. | chỉ cạnh ngắn → thêm cạnh dài | Princeton 09 tr.11–13; HNSW paper §3 tr.3 |
| H07 | 4 | Cấu trúc tầng (tầng 0 chứa mọi điểm, tầng trên là tập con thưa) và cách truy vấn đi xuống, trên cùng 12 điểm của H06B. | $s\to p4\to p8$ ↓ $p8\to p6$ ↓ $p6$ | HNSW paper Fig.1, §3, tr.3; Princeton 09 tr.17 |
| H09 | 4 | Đặc tả và giả mã truy vấn HNSW; hình gọn ba tầng nhắc lại vết $ep=p8$, $p6$. | tìm tầng → $K$ kết quả; $efSearch\ge K$ | HNSW paper alg.5, tr.5 |
| H08 | 3 | Chuyển xuống sau H09. Rút tầng ngẫu nhiên; suy ra $\Pr[\ell\ge k]=p^k$, $p=e^{-1/m_L}$; ví dụ $p=1/16$, tầng cao nhất khoảng 8 khi $N=10^{10}$. | $U,m_L$ → phân phối hình học, $\log_{1/p}N$ tầng | HNSW paper alg.1 dòng 4; §3; §4.1 |
| H10 | 4 | Tách: ví dụ chèn $x=2{,}6$, $\ell=1$, $M=2$ vào đồ thị ba tầng; bảng ba tầng và hình. | pha 1 → $ep=p4$; pha 2 → nối $p2,p4$ (tầng 1), $p3,p2$ (tầng 0) | HNSW paper alg.1, tr.4 |
| H10B | 3 | Tách: giả mã chèn hai pha và định nghĩa $M$, $efConstruction$, $M_{max}$, $M_{max,0}$. | điểm mới → HNSW cập nhật | HNSW paper alg.1, tr.4; §4.1 tr.5–6 |
| H11 | 3 | Quy tắc chọn lân cận đa dạng; ví dụ hai chiều bốn ứng viên so với chọn gần nhất. | $\{c1,c3\}$ → $\{c1,c4\}$ | HNSW paper alg.4, tr.4–5; Princeton 09 tr.18 |
| H12 | 3 | Ba tham số, thời điểm dùng và đánh đổi; câu hỏi giảm độ trễ không xây lại. | $M$, $efConstruction$, $efSearch$ → chọn tham số | HNSW paper §4.1 tr.5–6; §4.2.3 tr.8 |
| H13 | 4 | Chi phí bộ nhớ thay số cho $10^{10}$ véc-tơ (véc-tơ 122,88 TB, cạnh khoảng 2,65 TB); chi phí truy vấn và giới hạn $\log N$; nối sang PQ. | giả định $M=16$ → 98% bộ nhớ là véc-tơ gốc | HNSW paper §4.2 tr.7, §4.2.3 tr.8; Princeton 09 tr.2, 7 |
| Q00 | 6 | Gộp Q01: mở phần 4 từ nhu cầu giảm bộ nhớ; lượng tử hóa véc-tơ trên hình ba tâm, phép tính mã và tái dựng, câu hỏi điểm $y$. | $x=(1{,}7;0{,}4)$ → mã 1, sai số 0,25; $y$ → mã 2, 0,61 | Princeton 08 tr.8–9; PQ paper §II-A tr.2 |
| Q02 | 3 | Đặc tả VQ: đầu vào (bộ mã học bằng k-means), đầu ra và điều kiện sau, chi phí mã hóa $\Theta(kD)$ và lưu $kD$ số. | ví dụ Q00 → $i(x),\widehat x$, chi phí theo $k$ | PQ paper eq.2–5, tr.2; Princeton 08 tr.9–10, 32 |
| Q03 | 2 | Thay số chi phí của một bộ mã $k=2^{64}$, $D=128$: lưu, mã hóa, học. | $9{,}4\cdot10^{21}$ byte → cần bộ mã nhỏ cho mã dài | PQ paper §II-B tr.3; Princeton 08 tr.18 |
| Q04 | 3 | Định nghĩa PQ: chia đoạn, bộ mã con, mã $m\log_2k^*$ bit, tái dựng bằng ghép tâm con; hình $D=8$, $m=4$. | $D$ → $m$ đoạn → mã 32 bit | PQ paper §II-B eq.8–9, tr.3; Princeton 08 tr.29–31 |
| Q05 | 3 | Chạy tay mã PQ hai đoạn: khoảng cách từng đoạn, mã, tái dựng, sai số; hình hai mặt phẳng con. | hai bộ mã → mã $(0,1)$, sai số 0,18 | suy ra từ định nghĩa nguồn |
| Q07 | 4 | Kích thước mã và bộ mã PQ; so với VQ cùng mã 64 bit; thay số cho kho $10^{10}$ véc-tơ (512 byte, 5,12 TB). | $m,k^*,D,b$ → $k^*D$ số, $\lceil mb/8\rceil$ byte | PQ paper §II-B tr.3; Princeton 08 tr.32–33; BIODS tr.17 |
| Q06 | 3 | Chuyển sau Q07. Ví dụ ADC: định nghĩa bằng lời, hình hai đoạn có $q$, bảng hai số hạng, so 0,31 với giá trị đúng 0,07. | mã $(0,1)$ + $q$ → 0,31 | PQ paper eq.13, tr.4; Princeton 08 tr.25–26 |
| Q08 | 3 | Công thức ADC; mỗi số hạng chỉ phụ thuộc $q^{(j)}$ và chỉ số $i_j$, nên mỗi đoạn có $k^*$ giá trị tính trước được. | truy vấn đầy đủ + mã → tổng $m$ số hạng | PQ paper §III-A eq.13, tr.4; Princeton 08 tr.26–27 |
| Q09 | 3 | Bảng tra trên ví dụ hai đoạn (ô của mã $(0,1)$ đánh dấu); chi phí lập bảng, chấm mã so với tính trực tiếp. | $T$ 2×2 → 0,31 và 13,51; $\Theta(k^*D)$, $m$ lần tra | PQ paper §III-A tr.4; Princeton 08 tr.27, 31–32 |
| Q10 | 3 | Thay số quét mã PQ so với quét véc-tơ gốc cho $10^{10}$ véc-tơ; câu hỏi thời gian; nối sang chỉ mở một phần kho. | 5,12 TB, $5{,}12\cdot10^{12}$ lần tra, 5,12 s | PQ paper tr.2, §IV tr.6; Princeton 08 tr.20–22 |
| I00 | 4 | Định nghĩa tệp đảo trên ví dụ bốn ô, mười sáu điểm; vai trò của IVF và PQ trong IVF-PQ. | $q=(6;3{,}5)$, $nprobe=2$ → mở $L_1,L_0$, chấm 8/16 | Princeton 08 tr.21–22; PQ paper §IV tr.6–7 |
| I01 | 3 | Công thức gán vào tâm thô; xếp bốn tâm theo khoảng cách tới $q$; câu hỏi $nprobe=1$ bỏ sót $y_3$. | $q$ → thứ tự $\mu_1,\mu_0,\mu_3,\mu_2$ | Princeton 08 tr.21–22; PQ paper §IV-A, IV-C tr.6–7 |
| I02 | 3 | Phần dư $r(y)$, đẳng thức $\|q-y\|=\|(q-\mu_i)-r(y)\|$, một bảng tra cho mỗi danh sách mở; ví dụ $y_8$. | $r(y_8)$, $\widetilde q_1$, $\widetilde q_0$ → 1,25 | PQ paper §IV-A, IV-B tr.6, eq.31 |
| I04 | 4 | Giả mã truy vấn IVF-PQ; vết trên bốn danh sách ($nprobe=2$, $K=3$); câu hỏi $nprobe=1$. | $y_8,y_3,y_7$; $nprobe=1$ → recall@3 $=2/3$ | PQ paper §IV-C tr.7; Princeton 08 tr.21 |
| I03 | 3 | Chuyển sau I04. Đếm chi phí truy vấn theo ba bước, thay số cho $10^{10}$ véc-tơ với $k_c=10^5$, $nprobe=64$. | $\approx3{,}6\cdot10^9$, ít hơn 1400 lần quét đủ | PQ paper §IV-C tr.7; Princeton 08 tr.22; 09 tr.5 |
| C00 | 5 | So sánh LSH, HNSW, PQ quét đủ, IVF-PQ theo thừa số được giảm, bộ nhớ, truy vấn, tham số; thu hồi tình huống mở đầu bằng số. | 125 TB và 5,2 TB; $3{,}6\cdot10^9$ thao tác | tổng hợp các nguồn; số liệu suy ra từ H13, Q07, Q10, I03 |
| C01 | 4 | Thêm: ba câu tự kiểm (độ thu hồi; tìm kiếm chùm $ef=2$/$ef=3$; bộ nhớ HNSW so 64 GB). | đáp án $1/2$; không/có; 77,7 GB | dữ kiện học phần dựng |
| C02 | 4 | Thêm: ba câu tự kiểm (kích thước PQ $D=960$; ADC bằng bảng tra; số mã IVF-PQ). | 8 byte, 245 760 số; 3,6; 500 000 mã | PQ paper (GIST $D=960$); Princeton 09 tr.5 |

Tổng phần giảng: **120 phút**.

## Từng trang bài tập

| ID | Phút | Vai trò và sản phẩm hiển thị | Đáp án hoặc hướng dẫn chấm trong notes | Nguồn trực tiếp |
|---|---:|---|---|---|
| R00 | 0 | Nêu sổ thực hành, ô chuẩn bị, bốn mảng dữ liệu (kích thước, vai trò, ánh xạ ký hiệu) và ba nhiệm vụ với ô nguồn. | `xt` $10^6$, `xb` $10^4$, `xq` 100, `gt` 10 hàng xóm | Princeton runbook lớp 8, ô 0–4, 17, 21–24 |
| R01 | 6 | Chạy ô 83–95; dự đoán rồi đối chiếu `code_size`, dạng `pq_centroids`, `xb_codes` với công thức của bài. | 4 byte; $(4,256,16)$; $(10\,000,4)$ | ô 82–95 |
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

### H06 — Bất biến của SEARCH-LAYER

- **Phần:** 3. **Vai trò:** lập luận đúng và giới hạn. **Thời lượng:** 4 phút.
- **Mục đích:** phát biểu bất biến, chứng minh bằng khởi tạo–duy trì–khi dừng, và chỉ ra kết luận chỉ đúng trên tập đỉnh đã thấy.
- **Câu chốt:** $W$ luôn là $\min(ef,|V|)$ đỉnh gần $q$ nhất trong $V$; đỉnh ngoài $V$ không được bảo đảm.
- **Đầu vào:** giả mã H05; câu hỏi $ef=2$ ở H03, nhắc lại bằng hình `do-thi-ef2.svg` (đỉnh đã thấy tô xanh, đỉnh chưa thấy viền đứt, $W$ viền kép). **Thể hiện:** mệnh đề ở dòng đầu; hình bên trái, bảng ba hàng bên phải; câu chốt ví dụ.
- **Kết nối vào–ra:** chứng minh tính đúng của H05; giới hạn “ngoài $V$” tạo nhu cầu điểm vào tốt (H07).
- **Ghi chú diễn giả:** chứng minh bước duy trì; xử lý hòa; ví dụ $ef=2$; tính dừng; trường hợp xấu.
- **Nguồn:** suy ra từ Thuật toán 2, Malkov–Yashunin tr.4; bất biến kiểm bằng chương trình trên đồ thị ví dụ và 3000 đồ thị ngẫu nhiên.
- **Quyết định:** sửa. Bản cũ chỉ liệt kê tính chất của $V$, $C$, $W$, thiếu khởi tạo–duy trì–kết luận (tiêu chuẩn mục 3); phát biểu về $W$ yếu (“trong số đỉnh đã được chấp nhận”); ví dụ chỉ ở ghi chú và dẫn chiếu “ví dụ tìm kiếm chùm”.

### H06B — Cạnh dài rút ngắn đường đi (trang mới)

- **Phần:** 3. **Vai trò:** nêu vấn đề và trực giác cho cấu trúc nhiều tầng. **Thời lượng:** 3 phút.
- **Mục đích:** chạy tham lam trên ví dụ một chiều có và không có cạnh dài; giải thích vì sao HNSW tách cạnh theo thang độ dài.
- **Câu chốt:** cạnh dài đưa tìm kiếm tới gần $q$ nhanh, cạnh ngắn tinh chỉnh; HNSW đặt hai loại cạnh vào các tầng khác nhau.
- **Đầu vào:** tìm kiếm tham lam (H01). **Thể hiện:** hình `canh-dai-mot-chieu.svg` (hai dãy 12 điểm, $q$ ở tọa độ 6,4; đường tham lam tô cam: 6 bước và 3 bước); câu chốt.
- **Kết nối vào–ra:** sau khi đã có tìm kiếm trên một tầng (H01–H06), nêu giới hạn còn lại là số bước; tạo nhu cầu cho cấu trúc nhiều tầng H07.
- **Ghi chú diễn giả:** khoảng $N$ bước khi chỉ có cạnh ngắn; ý tưởng skip list; cạnh dài phải đặt đúng chỗ (chỉ có $p4$–$p8$ vẫn 6 bước); “zoom-out/zoom-in” của bài báo.
- **Nguồn:** Princeton lớp 9 tr.11–13; Malkov–Yashunin mục 3 tr.3. Ví dụ dựng lại, vết tính lại bằng chương trình.
- **Quyết định:** thêm. Bản cũ chuyển từ bất biến một tầng sang “điểm vào truyền từ tầng cao xuống thấp” mà không nêu vì sao cần nhiều tầng; khái niệm tầng xuất hiện đột ngột.

### H07 — Đồ thị nhiều tầng

- **Phần:** 3. **Vai trò:** mô hình cấu trúc và trực giác truy vấn. **Thời lượng:** 4 phút.
- **Mục đích:** mô tả tập điểm của từng tầng và lần theo truy vấn từ tầng cao xuống tầng 0.
- **Câu chốt:** tầng trên dùng $ef=1$ để đưa điểm vào tới gần $q$; tầng 0 dùng chùm $efSearch$.
- **Đầu vào:** ví dụ một chiều và ý tưởng cạnh dài (H06B), SEARCH-LAYER (H04–H05). **Thể hiện:** hình `do-thi-nhieu-tang.svg` (ba tầng trên cùng 12 điểm, đường cam, mũi tên xuống tại $p8$ và $p6$; vết tính lại bằng chương trình); hai gạch đầu dòng.
- **Kết nối vào–ra:** hiện thực ý tưởng H06B; giao cấu trúc cho giả mã truy vấn H09 và quy tắc rút tầng H08.
- **Ghi chú diễn giả:** điểm có tầng $\ell$ thuộc tầng $0..\ell$; vì sao $ef=1$ ở tầng trên; vết có số khoảng cách; tầng do học phần chọn, HNSW rút ngẫu nhiên.
- **Nguồn:** Malkov–Yashunin Hình 1, mục 3 tr.3; Princeton lớp 9 tr.17.
- **Quyết định:** sửa. Tiêu đề cũ “Điểm vào truyền từ tầng cao xuống thấp” là câu mô tả; hình cũ `hnsw-layers.svg` chữ nhỏ, không gắn với ví dụ; chuỗi $ep_2\to ep_1\to ep_0$ dùng ký hiệu chưa giải thích; trang không nói tầng nào chứa điểm nào.

### H08 — Rút ngẫu nhiên tầng của điểm mới (chuyển sau H09)

- **Phần:** 3. **Vai trò:** hình thức hóa và suy luận xác suất. **Thời lượng:** 3 phút.
- **Mục đích:** tính $\Pr[\ell\ge k]$ từ công thức rút tầng và giải thích vì sao tầng trên thưa dần, số tầng tăng theo $\log N$.
- **Câu chốt:** mỗi tầng giữ khoảng tỷ lệ $p=e^{-1/m_L}$ số điểm của tầng dưới; tầng cao nhất xấp xỉ $\log_{1/p}N$.
- **Đầu vào:** cấu trúc tầng (H07), truy vấn đi qua các tầng (H09); xác suất cơ bản. **Thể hiện:** công thức; dòng suy luận; hai thẻ “Ý nghĩa” và “Ví dụ $m_L=1/\ln16$”; câu chốt thay số $N=10^{10}$.
- **Kết nối vào–ra:** cho biết tập điểm mỗi tầng hình thành thế nào (bổ sung H07); giao $\ell$ cho thao tác chèn H10.
- **Ghi chú diễn giả:** từng bước suy luận; phân phối hình học như skip list; $m_L=1/\ln M$ của bài báo với $M$ định nghĩa ở H10; số liệu mô phỏng.
- **Nguồn:** Malkov–Yashunin Thuật toán 1 dòng 4 tr.4; mục 3 tr.3; mục 4.1 tr.5.
- **Quyết định:** sửa và chuyển vị trí. Bản cũ chỉ có công thức và bảng ký hiệu, không cho thấy công thức sinh phân phối nào; ghi chú dùng $M$ chưa định nghĩa và dẫn chiếu “trang sau”. Rút tầng chỉ dùng khi chèn nên đặt sau giả mã truy vấn, ngay trước H10.

### H09 — Giả mã truy vấn HNSW

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 4 phút.
- **Mục đích:** đọc giả mã truy vấn; chỉ ra lời gọi $ef=1$ ở tầng trên và $efSearch$ ở tầng 0; nêu điều kiện $efSearch\ge K$.
- **Câu chốt:** truy vấn là chuỗi lời gọi SEARCH-LAYER: tham lam ở tầng trên để có điểm vào, chùm $efSearch$ ở tầng 0 để có $K$ kết quả.
- **Đầu vào:** SEARCH-LAYER (H04–H06), cấu trúc tầng (H07), nhắc lại bằng hình `do-thi-nhieu-tang-gon.svg`. **Thể hiện:** dòng đầu vào/đầu ra; giả mã 6 dòng bên trái; hình gọn và dòng vết bên phải.
- **Kết nối vào–ra:** hình thức hóa H07; lời gọi tương tự được dùng trong pha chèn H10; $efSearch$ là núm điều khiển ở H12.
- **Ghi chú diễn giả:** dữ kiện ví dụ; $ef=1$ là tham lam; trả ít hơn $K$ khi đồ thị tới được nhỏ; tính dừng; kết quả gần đúng theo bất biến.
- **Nguồn:** Malkov–Yashunin Thuật toán 5 tr.5.
- **Quyết định:** sửa. Tiêu đề cũ “Truy vấn HNSW dùng hai chế độ” mơ hồ; giả mã cũ dùng tên `điểm_vào`, `phần_tử_gần_nhất`; thiếu đầu vào/đầu ra trên mặt trang; không nối với ví dụ.

### H10 — Chèn một điểm mới (tách từ H10 cũ)

- **Phần:** 3. **Vai trò:** ví dụ chạy tay trước giả mã. **Thời lượng:** 4 phút.
- **Mục đích:** chạy tay chèn một điểm qua hai pha trên đồ thị ba tầng.
- **Câu chốt:** chèn là truy vấn chính $x$, rồi nối $x$ với các đỉnh gần nó ở từng tầng $\le\ell$.
- **Đầu vào:** đồ thị ba tầng (H07), truy vấn (H09), tầng $\ell$ (H08). **Thể hiện:** dòng dữ kiện; hình `chen-vi-du.svg` (pha 1 cam, cạnh mới xanh đứt) cạnh bảng ba tầng; câu chốt.
- **Kết nối vào–ra:** dùng truy vấn và rút tầng; giao vết cho giả mã H10B và cho câu hỏi chọn lân cận ở H11.
- **Ghi chú diễn giả:** dữ kiện đồ thị, khoảng cách tới $x$; vai trò hai pha; bậc sau khi nối và vì sao không cắt.
- **Nguồn:** Malkov–Yashunin Thuật toán 1–3; vết mô phỏng lại bằng chương trình.

### H10B — Giả mã chèn HNSW (tách từ H10 cũ)

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 3 phút.
- **Mục đích:** đọc giả mã chèn và gọi đúng tên, vai trò của $M$, $efConstruction$, $M_{max}$, $M_{max,0}$.
- **Câu chốt:** pha 1 chỉ tìm điểm vào ở tầng cao hơn $\ell$; pha 2 tìm, chọn $M$ lân cận, nối hai chiều và cắt bậc ở tầng $\le\ell$.
- **Đầu vào:** ví dụ H10. **Thể hiện:** khối giả mã 10 dòng có chú thích pha; một dòng định nghĩa tham số.
- **Kết nối vào–ra:** hình thức hóa H10; dòng “chọn $M$ lân cận” được cụ thể hóa ở H11; các tham số dùng ở H12–H13.
- **Ghi chú diễn giả:** chỉ mục rỗng; mất đối xứng sau cắt; Thuật toán 3 và 4; ràng buộc tham số; $M_{max,0}=2M$ theo mục 4.1.
- **Nguồn:** Malkov–Yashunin Thuật toán 1 tr.4; mục 4.1 tr.5–6.
- **Quyết định (H10 cũ):** tách. Bản cũ có tiêu đề câu mô tả, hình bốn hộp chữ rất nhỏ, một dòng đưa cùng lúc bốn tham số mới; ghi chú diễn giả dài, chứa toàn bộ thuật toán. Ví dụ đặt trước giả mã theo chu trình học.

### H11 — Chọn lân cận đa dạng

- **Phần:** 3. **Vai trò:** cơ chế, ví dụ chạy tay. **Thời lượng:** 3 phút.
- **Mục đích:** áp dụng quy tắc đa dạng để chọn $M$ lân cận và so sánh với chọn gần nhất.
- **Câu chốt:** ứng viên gần một lân cận đã chọn hơn gần $x$ bị loại, nên các cạnh được chọn trải ra nhiều hướng.
- **Đầu vào:** dòng “chọn $M$ lân cận” của giả mã chèn (H10B). **Thể hiện:** dòng quy tắc; hình hai khung `lan-can-da-dang.svg`; bảng quyết định bốn ứng viên.
- **Kết nối vào–ra:** cụ thể hóa H10B; $M$ là núm điều khiển ở H12.
- **Ghi chú diễn giả:** tọa độ ví dụ và lý do đổi sang ví dụ hai chiều; ý nghĩa hình học; hai tùy chọn của Thuật toán 4 nằm ngoài phạm vi; dùng cả khi cắt bậc.
- **Nguồn:** Malkov–Yashunin mục 3, Thuật toán 4 tr.4–5; Princeton lớp 9 tr.18. Phép tính kiểm bằng chương trình.
- **Quyết định:** sửa. Bản cũ dùng $q$ cho điểm mới (xung đột với $q$ là truy vấn); không có hình hay ví dụ; “hướng thoát” là ẩn dụ chưa gắn đối tượng; tiêu đề câu dài.

### H12 — Ba tham số của HNSW

- **Phần:** 3. **Vai trò:** ứng dụng, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** gọi đúng tham số dùng khi chèn và khi truy vấn; chọn tham số để giảm độ trễ không xây lại.
- **Câu chốt:** $M$ và $efConstruction$ cố định khi xây; $efSearch$ đổi theo truy vấn và đánh đổi độ trễ với độ thu hồi.
- **Đầu vào:** giả mã truy vấn (H09) và chèn (H10B). **Thể hiện:** bảng ba cột; hộp câu hỏi.
- **Kết nối vào–ra:** tổng hợp tham số của H09–H11; giao $M$ cho chi phí bộ nhớ H13 và cho bảng so sánh C00.
- **Kiểm tra:** giảm $efSearch$ (giữ $\ge K$); mất độ thu hồi. Đáp án trong ghi chú.
- **Nguồn:** Malkov–Yashunin mục 4.1 tr.5–6, mục 4.2.3 tr.8; Princeton lớp 9 tr.19.
- **Quyết định:** sửa. Tiêu đề cũ “Ba núm điều khiển ba loại chi phí” dùng ẩn dụ; bảng không nói tham số dùng lúc xây hay lúc truy vấn; thiếu câu hỏi kiểm tra cho phần HNSW.

### H13 — Chi phí của HNSW

- **Phần:** 3 (kết phần). **Vai trò:** chi phí, giới hạn, câu nối. **Thời lượng:** 4 phút.
- **Mục đích:** tính bộ nhớ của HNSW cho tình huống mở đầu, tách phần véc-tơ và phần cạnh; nêu điều kiện của kết luận $\log N$.
- **Câu chốt:** HNSW giảm số phép đo nhưng vẫn giữ 122,88 TB véc-tơ gốc, khoảng 98% bộ nhớ.
- **Đầu vào:** $N$, $D$ (P01, nhắc lại bằng số), $M_{max}$, $M_{max,0}$ (H10B), $p$ (H08). **Thể hiện:** dòng giả định; bảng hai thành phần (mỗi điểm, toàn kho); dòng chi phí truy vấn; câu chốt.
- **Kết nối vào–ra:** kết phần 3; tạo nhu cầu biểu diễn gọn (phần 4, Q00); số liệu dùng lại ở bảng so sánh C00.
- **Ghi chú diễn giả:** mô hình bộ nhớ; kỳ vọng số tầng trên $p/(1-p)$ và so với ước lượng của bài báo (302 byte); 8 byte mỗi mã định danh; giả thiết của $\log N$; chi phí xây.
- **Nguồn:** Malkov–Yashunin mục 4.2 tr.7, mục 4.2.3 tr.8; Princeton lớp 9 tr.2, tr.7. Số liệu tính lại bằng chương trình (mô phỏng $E[\ell]=0{,}0664$).
- **Quyết định:** sửa. Tiêu đề cũ là câu dài; bản cũ chỉ có $O(ND)$, $O(NM)$, không thay số nên không thấy véc-tơ gốc chiếm phần lớn bộ nhớ; không có câu nối sang PQ.

### Q00 — Lượng tử hóa véc-tơ (gộp Q01 cũ)

- **Phần:** 4, lượng tử hóa tích (khái niệm/thuật toán). **Vai trò:** mở phần, trực giác, ví dụ chạy tay, kiểm tra. **Thời lượng:** 6 phút.
- **Mục đích:** mã hóa và tái dựng một véc-tơ bằng bộ mã cho trước, tính sai số.
- **Câu chốt:** mã ngắn ($\log_2 k$ bit) đổi lấy sai số tái dựng.
- **Đầu vào:** véc-tơ gốc chiếm phần lớn bộ nhớ (H13). **Thể hiện:** dòng định nghĩa; hình `luong-tu-hoa-vec-to.svg` (ba tâm, ba ô, $x$ nối tới $c_1$); phép tính bên phải; câu hỏi.
- **Kết nối vào–ra:** đáp nhu cầu giảm bộ nhớ của H13; giao định nghĩa cho đặc tả Q02.
- **Kiểm tra:** $y=(0{,}6;1{,}5)$: $2{,}61$; $4{,}21$; $0{,}61$ → mã 2, sai số 0,61 (tính lại).
- **Nguồn:** Princeton lớp 8 tr.8–9; PQ paper mục II-A tr.2. Ví dụ dựng từ định nghĩa.
- **Quyết định:** gộp. Q00 cũ chỉ có hai thẻ ký hiệu, không hình, không nói nhu cầu; Q01 cũ là ví dụ của cùng khái niệm và câu hỏi của nó có đáp án hiện sẵn trên trang ($0{,}25$).

### Q02 — Đặc tả lượng tử hóa véc-tơ

- **Phần:** 4. **Vai trò:** hình thức hóa, chi phí. **Thời lượng:** 3 phút.
- **Mục đích:** viết đặc tả VQ và tính chi phí mã hóa, lưu bộ mã theo $k$, $D$.
- **Câu chốt:** mã hóa tốn $\Theta(kD)$ và bộ mã chiếm $kD$ số; cả hai tỷ lệ với số tâm $k$.
- **Đầu vào:** định nghĩa và ví dụ Q00. **Thể hiện:** công thức argmin; bảng đầu vào/đầu ra/chi phí.
- **Kết nối vào–ra:** hình thức hóa Q00; chi phí theo $k$ dẫn tới giới hạn bộ mã lớn ở Q03.
- **Ghi chú diễn giả:** k-means và điều kiện Lloyd chỉ cho cực tiểu cục bộ; điều kiện sau từ argmin.
- **Nguồn:** PQ paper mục II-A, pt.2–5 tr.2; Princeton lớp 8 tr.9–10, 32.
- **Quyết định:** sửa. Bản cũ thiếu chi phí nên Q03 phải tự đưa công thức bộ nhớ; tên k-means chỉ có trong ghi chú; cấu trúc ba dòng văn xuôi khó quét.

### Q03 — Giới hạn của một bộ mã lớn

- **Phần:** 4. **Vai trò:** nêu giới hạn tạo nhu cầu. **Thời lượng:** 2 phút.
- **Mục đích:** tính chi phí lưu, mã hóa, học của một bộ mã cho mã 64 bit và kết luận cần cấu trúc khác.
- **Câu chốt:** mã dài với một bộ mã duy nhất đòi hỏi bộ mã khổng lồ; cần tạo mã dài từ các bộ mã nhỏ.
- **Đầu vào:** chi phí theo $k$ (Q02). **Thể hiện:** dòng dẫn (sai số giảm khi tăng $k$; ví dụ SIFT của nguồn); bảng ba dòng thay số; câu chốt.
- **Kết nối vào–ra:** dùng chi phí Q02; tạo nhu cầu chia đoạn ở Q04.
- **Ghi chú diễn giả:** tăng tuyến tính theo $k$ nhưng hàm mũ theo độ dài mã; phép tính; nhận định của bài báo.
- **Nguồn:** PQ paper mục II-B tr.3; Princeton lớp 8 tr.18.
- **Quyết định:** sửa. Tiêu đề cũ là câu; không nói vì sao cần mã 64 bit; công thức không thay số nên “không khả thi” chỉ là khẳng định.

### Q04 — Lượng tử hóa tích (PQ)

- **Phần:** 4. **Vai trò:** trực giác và định nghĩa. **Thời lượng:** 3 phút.
- **Mục đích:** mô tả cách PQ tạo mã dài từ $m$ bộ mã con; tính độ dài mã.
- **Câu chốt:** chia véc-tơ thành $m$ đoạn, mỗi đoạn một bộ mã con nhỏ; mã là bộ $m$ chỉ số, tái dựng bằng ghép các tâm con.
- **Đầu vào:** VQ (Q00–Q02), giới hạn bộ mã lớn (Q03). **Thể hiện:** hình `pq-tach-doan.svg` (tám tọa độ, bốn đoạn, bốn bộ mã 256 tâm, mã 32 bit; màu kèm nhãn “đoạn $j$”); ba gạch đầu dòng.
- **Kết nối vào–ra:** đáp nhu cầu Q03; giao định nghĩa cho ví dụ Q05 và công thức kích thước Q07.
- **Ghi chú diễn giả:** tên đầy đủ; $m\mid D$; học từng bộ mã con; chi phí mã hóa $\Theta(k^*D)$; ký hiệu `M` của Faiss.
- **Nguồn:** PQ paper mục II-B pt.8–9 tr.3; Princeton lớp 8 tr.29–31.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình cũ `pq-split.svg` chữ rất nhỏ; mặt trang không có độ dài mã, cách tái dựng và tên đầy đủ của PQ.

### Q05 — Ví dụ mã hóa PQ

- **Phần:** 4. **Vai trò:** ví dụ chạy tay. **Thời lượng:** 3 phút.
- **Mục đích:** mã hóa một véc-tơ bằng PQ hai đoạn, tái dựng và tính sai số.
- **Câu chốt:** mỗi đoạn mã hóa độc lập; sai số tái dựng là tổng sai số các đoạn.
- **Đầu vào:** định nghĩa PQ (Q04). **Thể hiện:** dòng dữ kiện; hình `pq-vi-du.svg` (hai mặt phẳng con, tâm được chọn tô đặc); bảng khoảng cách và chỉ số; dòng kết quả.
- **Kết nối vào–ra:** cụ thể hóa Q04; mã $(0,1)$ và hai bộ mã được dùng lại ở ví dụ ADC (Q06, có hình biến thể kèm $q$).
- **Ghi chú diễn giả:** tọa độ các tâm; một phép tính mẫu; vì sao sai số cộng theo đoạn; so với VQ bốn chiều.
- **Nguồn:** dựng từ định nghĩa, PQ paper mục II-B tr.3.
- **Quyết định:** sửa. Bản cũ để các khoảng cách (phép tính cần học) và sai số trong ghi chú; không có hình; số thập phân dùng dấu chấm; tiêu đề “Ví dụ PQ ghép hai chỉ số” không nói thao tác.

### Q06 — Ví dụ khoảng cách bất đối xứng (chuyển sau Q07)

- **Phần:** 4. **Vai trò:** ví dụ chạy tay trước hình thức hóa ADC. **Thời lượng:** 3 phút.
- **Mục đích:** tính khoảng cách bất đối xứng từ truy vấn đầy đủ tới một véc-tơ chỉ còn mã; so với khoảng cách thật.
- **Câu chốt:** ADC ước lượng $\|q-x\|^2$ bằng $\|q-\widehat x\|^2$, cộng theo đoạn; sai lệch đến từ sai số tái dựng.
- **Đầu vào:** mã $(0,1)$ và hai bộ mã của Q05, nhắc lại bằng hình `pq-vi-du-adc.svg` và ghi chú. **Thể hiện:** dòng định nghĩa bằng lời; hình bên trái; $q$, bảng hai đoạn và dòng so sánh bên phải.
- **Kết nối vào–ra:** dùng ví dụ Q05; giao số hạng từng đoạn cho công thức ADC Q08 và bảng tra Q09.
- **Ghi chú diễn giả:** dữ kiện bộ mã; phép tính; tên đầy đủ ADC; vì sao gọi là bất đối xứng; không cần $x$.
- **Nguồn:** PQ paper mục III-A pt.13 tr.4; Princeton lớp 8 tr.25–26.
- **Quyết định:** sửa và chuyển vị trí. Bản cũ mở bằng “Giữ mã … từ ví dụ PQ trước” (dẫn chiếu trang trước, không nhắc lại bộ mã); “khoảng cách bất đối xứng” chưa được giải thích; giá trị đúng 0,07 chỉ ở ghi chú. Chuyển sau Q07 để mạch mã hóa → bộ nhớ → khoảng cách liền nhau.

### Q07 — Kích thước mã và bộ mã PQ

- **Phần:** 4. **Vai trò:** chi phí bộ nhớ, ứng dụng vào tình huống mở đầu. **Thời lượng:** 4 phút.
- **Mục đích:** tính độ dài mã, kích thước bộ mã PQ; so với VQ; tính bộ nhớ mã cho kho $10^{10}$ véc-tơ.
- **Câu chốt:** PQ có $2^{64}$ mã với bộ mã chỉ $32\,768$ số; kho mở đầu còn 5,12 TB mã thay vì 122,88 TB.
- **Đầu vào:** định nghĩa PQ (Q04), giới hạn VQ (Q03), số liệu $N$, $D$ (nhắc lại bằng số). **Thể hiện:** dòng công thức; bảng VQ/PQ ba hàng; câu chốt thay số.
- **Kết nối vào–ra:** giải quyết Q03; thu hồi một phần tình huống P01 (bộ nhớ); tạo nhu cầu tính khoảng cách trên mã (Q06).
- **Ghi chú diễn giả:** suy ra $k^*D$; tích không gian; phép tính 512 byte, 5,12 TB, tỷ lệ 24; phần chưa tính.
- **Nguồn:** PQ paper mục II-B tr.3; Princeton lớp 8 tr.32–33; BIODS bài 12 tr.17.
- **Quyết định:** sửa. Tiêu đề cũ là câu; bản cũ không so với VQ nên không thấy PQ giải quyết Q03 thế nào; số liệu tình huống mở đầu chỉ trong ghi chú.

### Q08 — Khoảng cách bất đối xứng (ADC)

- **Phần:** 4. **Vai trò:** hình thức hóa. **Thời lượng:** 3 phút.
- **Mục đích:** viết công thức ADC và chỉ ra vì sao số hạng mỗi đoạn tính trước được.
- **Câu chốt:** với một truy vấn, số hạng đoạn $j$ chỉ có $k^*$ giá trị khác nhau.
- **Đầu vào:** ví dụ ADC (Q06), định nghĩa PQ (Q04). **Thể hiện:** công thức; hai gạch đầu dòng; câu chốt.
- **Kết nối vào–ra:** hình thức hóa Q06; giao ý “tính trước” cho bảng tra Q09.
- **Ghi chú diễn giả:** vì sao tổng theo đoạn; số hạng của ví dụ; SDC và nhận định của bài báo.
- **Nguồn:** PQ paper mục III-A pt.13 tr.4; Princeton lớp 8 tr.26–27.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hai thẻ “Truy vấn: không lượng tử hóa / Cơ sở dữ liệu: chỉ giữ mã PQ” lặp định nghĩa; ý dẫn tới bảng tra chưa có.

### Q09 — Bảng tra khoảng cách

- **Phần:** 4. **Vai trò:** thuật toán và chi phí. **Thời lượng:** 3 phút.
- **Mục đích:** lập bảng tra cho một truy vấn, chấm mã bằng tra và cộng, so chi phí với tính trực tiếp.
- **Câu chốt:** lập bảng một lần $\Theta(k^*D)$, sau đó mỗi mã chỉ cần $m$ lần tra.
- **Đầu vào:** công thức ADC (Q08), ví dụ hai đoạn (Q05–Q06; dữ kiện ghi trong ghi chú, các ô của bảng hiện trên trang). **Thể hiện:** dòng định nghĩa $T$; bảng HTML 2×2 với hai ô viền đậm cho mã $(0,1)$ (không chỉ bằng màu); dòng chấm hai mã; bảng chi phí.
- **Kết nối vào–ra:** hiện thực Q08; chi phí chấm một mã giao cho Q10 (quét $N$ mã) và I03.
- **Ghi chú diễn giả:** dữ kiện; một ô mẫu; phép đếm $k^*D$; khi nào đáng lập bảng; 512 lần tra so với 3072 tọa độ.
- **Nguồn:** PQ paper mục III-A tr.4; Princeton lớp 8 tr.27, 31–32.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình cũ `pq-lut.svg` chữ rất nhỏ, không có số; chi phí chỉ ở một dòng ký hiệu. Bảng tra dựng bằng HTML theo quy định bảng không dùng ảnh.

### Q10 — Giới hạn của PQ quét đầy đủ

- **Phần:** 4 (kết phần). **Vai trò:** chi phí, giới hạn, kiểm tra, câu nối. **Thời lượng:** 3 phút.
- **Mục đích:** tính dữ liệu đọc và số lần tra khi quét mã PQ; so với quét véc-tơ gốc; chỉ ra thừa số còn lại.
- **Câu chốt:** PQ giảm chi phí mỗi phép đo, không giảm số véc-tơ được chấm.
- **Đầu vào:** kích thước mã (Q07), chi phí chấm một mã (Q09), số liệu kho (nhắc lại bằng số). **Thể hiện:** dòng dữ kiện; bảng hai cột; hộp câu hỏi; câu chốt.
- **Kết nối vào–ra:** đóng phần 4; nối A03 (hai thừa số) sang phần 5: chỉ mở một phần kho.
- **Kiểm tra:** $5{,}12$ giây với $10^{12}$ lần tra/giây (giả định), so với 30,7 giây ở P01.
- **Nguồn:** PQ paper tr.2, mục IV tr.6; Princeton lớp 8 tr.20–22.
- **Quyết định:** sửa. Tiêu đề cũ là câu; chi phí chỉ ký hiệu, không so được với lượt quét gốc; “tầng định tuyến” xuất hiện đột ngột.

### I00 — Tệp đảo (IVF)

- **Phần:** 5, IVF-PQ (thuật toán). **Vai trò:** mở phần, trực giác, ví dụ. **Thời lượng:** 4 phút.
- **Mục đích:** mô tả tệp đảo, xác định danh sách được mở với $nprobe$ cho trước trên ví dụ.
- **Câu chốt:** IVF giảm số véc-tơ được chấm; mã PQ trong mỗi danh sách giảm chi phí mỗi lần chấm.
- **Đầu vào:** giới hạn PQ quét đầy đủ (Q10), VQ (Q00–Q02). **Thể hiện:** dòng định nghĩa; hình `tep-dao.svg` (bốn ô, hai ô mở tô màu và viền liền, nhãn “(mở)”; nhãn $y_3$, $y_8$); bảng HTML bốn danh sách; dòng 8/16.
- **Kết nối vào–ra:** nhận thừa số “số véc-tơ được chấm” từ Q10; ví dụ dùng tiếp ở I01–I04.
- **Ghi chú diễn giả:** tên đầy đủ; IVF là VQ thô; tọa độ ví dụ; tương ứng ký hiệu $k'$, $w$ của bài báo và `nlist`, `nprobe` của Faiss.
- **Nguồn:** Princeton lớp 8 tr.21–22; PQ paper mục IV tr.6–7. Ví dụ do học phần dựng.
- **Quyết định:** viết lại. Bản cũ (tiêu đề câu “IVF-PQ định tuyến rồi chấm mã nén”) chỉ có hai thẻ chữ, không hình; dùng “định tuyến”, “véc-tơ dư” chưa giải thích.

### I01 — Chọn danh sách cần mở

- **Phần:** 5. **Vai trò:** hình thức hóa phép gán, ví dụ, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** gán véc-tơ vào danh sách, chọn $nprobe$ danh sách cho một truy vấn; thấy giới hạn khi hàng xóm nằm ở ô bên cạnh.
- **Câu chốt:** mở danh sách theo khoảng cách từ $q$ tới tâm thô; hàng xóm thật gần ranh giới có thể nằm ở danh sách chưa mở.
- **Đầu vào:** ví dụ bốn ô (I00), nhắc lại bằng hình `tep-dao-o.svg` (không đánh dấu danh sách mở để khớp câu hỏi). **Thể hiện:** công thức $a(y)$, $L_i$; hình; bảng bốn tâm và thứ tự; hộp câu hỏi.
- **Kết nối vào–ra:** cụ thể hóa I00; hiện tượng bỏ sót dẫn tới tham số $nprobe$ trong chi phí I03.
- **Kiểm tra:** $y_3$ không được chấm với $nprobe=1$ (9,49 < 15,49 nên $y_3\in L_0$), dù là hàng xóm gần thứ hai ($2{,}34$).
- **Nguồn:** Princeton lớp 8 tr.21–22; PQ paper mục IV-A, IV-C tr.6–7.
- **Quyết định:** sửa. Tiêu đề cũ là câu; ví dụ cũ hai tâm $\mu_0=(0,0)$, $\mu_1=(8,0)$ rời rạc với các ví dụ khác và không cho thấy tác dụng của $nprobe$; ký tự “<” thô từng làm hỏng công thức (đã sửa ở bước chuẩn bị).

### I02 — Mã hóa phần dư

- **Phần:** 5. **Vai trò:** cơ chế và lập luận đúng. **Thời lượng:** 3 phút.
- **Mục đích:** tính phần dư và truy vấn dư; giải thích vì sao mỗi danh sách mở cần một bảng tra riêng.
- **Câu chốt:** $\|q-y\|=\|\widetilde q_i-r(y)\|$ với $y\in L_i$, nên quét $L_i$ bằng ADC với truy vấn dư $\widetilde q_i$.
- **Đầu vào:** ví dụ bốn ô (I00–I01), nhắc lại bằng hình phóng to hai ô dưới `tep-dao-du.svg`; ADC (Q06–Q09). **Thể hiện:** hai công thức; hình; hai gạch đầu dòng; dòng số liệu ví dụ.
- **Kết nối vào–ra:** cụ thể hóa cách chấm trong danh sách; số bảng tra $nprobe$ giao cho chi phí I03 và thuật toán I04.
- **Ghi chú diễn giả:** vì sao phần dư mã hóa tốt hơn; đẳng thức; kiểm tra 1,25; dùng nhầm bảng cho 31,25; một PQ chung cho mọi ô.
- **Nguồn:** PQ paper mục IV-A, IV-B tr.6, pt.31.
- **Quyết định:** sửa. Tiêu đề cũ là câu; không có lý do cho truy vấn dư riêng; dẫn chiếu “ví dụ ngay trước” bằng lời.

### I03 — Chi phí truy vấn IVF-PQ (chuyển sau I04)

- **Phần:** 5. **Vai trò:** chi phí và ứng dụng vào tình huống mở đầu. **Thời lượng:** 3 phút.
- **Mục đích:** đếm chi phí truy vấn theo từng bước của thuật toán, thay số cho kho $10^{10}$ véc-tơ.
- **Câu chốt:** với $k_c=10^5$, $nprobe=64$, một truy vấn cần khoảng $3{,}6\cdot10^9$ thao tác, ít hơn khoảng 1400 lần so với quét đủ mã PQ.
- **Đầu vào:** thuật toán I04, chi phí lập bảng và chấm mã (Q09), số liệu kho (nhắc lại bằng số). **Thể hiện:** dòng giả định; bảng bước × số lần × chi phí × thay số; câu chốt so với Q10.
- **Kết nối vào–ra:** đếm theo các bước của I04; giao số liệu cho bảng so sánh C00.
- **Ghi chú diễn giả:** mô hình đếm; bỏ qua top-$K$; giả thiết cân bằng; phép tính; 3,6 ms; giả định minh họa; tác động của $nprobe$.
- **Nguồn:** PQ paper mục IV-C tr.7; Princeton lớp 8 tr.22, lớp 9 tr.5.
- **Quyết định:** sửa và chuyển vị trí. Tiêu đề cũ là câu; chưa theo mạch đếm bước × số lần × chi phí; không thay số nên không thấy IVF-PQ đáp ứng bài toán; giả thiết cân bằng chỉ ở ghi chú; đứng trước trang thuật toán.

### I04 — Thuật toán truy vấn IVF-PQ

- **Phần:** 5. **Vai trò:** thuật toán, ví dụ, kiểm tra. **Thời lượng:** 4 phút.
- **Mục đích:** đọc giả mã truy vấn IVF-PQ, chạy trên ví dụ, tính độ thu hồi khi đổi $nprobe$.
- **Câu chốt:** chỉ phần tử của $nprobe$ danh sách được chấm; hàng xóm ở danh sách chưa mở bị bỏ sót.
- **Đầu vào:** chọn danh sách (I01), phần dư và bảng tra riêng (I02), độ thu hồi (A01). **Thể hiện:** giả mã 8 dòng bên trái; bảng khoảng cách hai danh sách (tự chứa dữ kiện, ghi “ADC giả sử đúng”) và dòng kết quả bên phải; hộp câu hỏi.
- **Kết nối vào–ra:** tổng hợp I01–I02; các bước giả mã là cơ sở đếm chi phí I03.
- **Ghi chú diễn giả:** đặc tả đầu vào/đầu ra; trường hợp ít hơn $K$; dừng; trả mã định danh; giả định ADC đúng; đáp án $2/3$.
- **Nguồn:** PQ paper mục IV-C tr.7; Princeton lớp 8 tr.21.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình `ivfpq-flow.svg` chữ rất nhỏ; danh sách bốn bước thiếu khởi tạo, vòng lặp, cấu trúc giữ $K$ kết quả; không có vết chạy hay kiểm tra.

### C00 — So sánh bốn cấu trúc

- **Phần:** 6, tổng kết. **Vai trò:** đối chiếu, thu hồi tình huống. **Thời lượng:** 5 phút.
- **Mục đích:** so sánh bốn cấu trúc trên cùng bảng và trả lời bài toán mở đầu bằng số liệu bộ nhớ, chi phí truy vấn.
- **Câu chốt:** với kho mở đầu, HNSW cần khoảng 125 TB; IVF-PQ khoảng 5,2 TB và $3{,}6\cdot10^9$ thao tác mỗi truy vấn, đổi lại độ thu hồi phụ thuộc $nprobe$ và sai số mã hóa.
- **Đầu vào:** hai thừa số (A03), bốn trục (A02), số liệu H13, Q07, Q10, I03 (ghi lại bằng số trên trang). **Thể hiện:** dòng giả định; bảng năm cột; câu chốt.
- **Kết nối vào–ra:** thu hồi P01; chuyển sang câu hỏi tự kiểm C01.
- **Ghi chú diễn giả:** không xếp hạng phổ quát; chất lượng phải đo; khi nào HNSW phù hợp; kết hợp hai hướng; phép tính; LSH không thay số.
- **Nguồn:** tổng hợp; MMDS Ch.3; Princeton lớp 8 tr.2–5, lớp 9 tr.2–7; hai bài báo.
- **Quyết định:** sửa. Tiêu đề cũ “Bốn cơ chế trên cùng bốn trục”; bảng chỉ có ký hiệu; câu “Trả lời bài toán mở đầu” là lời khuyên chung, không thu hồi tình huống bằng số.

### C01, C02 — Tự kiểm tra (trang mới)

- **Phần:** 6, tổng kết. **Vai trò:** kiểm tra cuối bài. **Thời lượng:** 4 + 4 phút.
- **Mục đích:** tự kiểm ba mục tiêu của P02 bằng sáu câu ngắn có dữ kiện mới.
- **Câu chốt:** mỗi câu dùng lại một phép tính hoặc thuật toán của bài trên dữ kiện chưa xuất hiện.
- **Thể hiện:** nhãn “Câu hỏi:” và danh sách đánh số ba câu mỗi trang; đáp án và mục tiêu được kiểm trong ghi chú diễn giả.
- **Kết nối vào–ra:** sau C00; mở phần thực hành R00.
- **Kiểm tra (tính lại bằng chương trình):** C01: $1/2$; $ef=2$ không tới $z$, $ef=3$ tới $z$; 77,7 GB > 64 GB. C02: 8 byte, 245 760 số; 3,6; 500 000 mã, $4\cdot10^6$ lần tra.
- **Nguồn:** dữ kiện học phần dựng; $D=960$ là số chiều GIST trong bài báo PQ; $k_c=32\,000$ cho $N=10^9$ theo Princeton lớp 9 tr.5.
- **Quyết định:** thêm. Phần kết cũ chỉ có C00, thiếu 4–6 nhiệm vụ tự kiểm theo tiêu chuẩn mục 2; P02 đã cam kết “So sánh và tự kiểm tra” (việc mở từ lượt rà phần 1–2).

### R00 — Sổ thực hành và dữ liệu

- **Phần:** 7, bài tập. **Vai trò:** mở phần thực hành. **Thời lượng:** 0 phút (đọc trước).
- **Mục đích:** biết dữ liệu dùng trong ba nhiệm vụ và ô nguồn của từng nhiệm vụ.
- **Câu chốt:** `xb` là kho $N=10^4$ véc-tơ 64 chiều, `gt` là tập đúng 10 hàng xóm từ quét đầy đủ.
- **Thể hiện:** dòng tên sổ và ô chuẩn bị; bảng bốn mảng; bảng ba nhiệm vụ.
- **Kết nối vào–ra:** sau phần tự kiểm; mở R01–R08. Ánh xạ `M`, `nbits` của Faiss sang $m$, $b$.
- **Ghi chú diễn giả:** tham số `SyntheticDataset`; `gt` từ `faiss.knn`; ký hiệu Faiss; hướng dẫn chuẩn bị máy; thời gian chạy máy không tính vào thời lượng tại lớp.
- **Nguồn:** sổ Princeton lớp 8, ô 0–4, 17, 21–24.
- **Quyết định:** sửa. Bản cũ không nói dữ liệu gồm gì, đặt đường dẫn nội bộ `sources/…` trên mặt trang và dòng chỉ dẫn điều phối “Thời gian máy được báo riêng”.

### R01 — Nhiệm vụ 1: cấu trúc mã PQ

- **Phần:** 7. **Vai trò:** bài tập vận dụng công thức kích thước PQ. **Thời lượng:** 6 phút.
- **Mục đích:** nối tham số Faiss với $D$, $m$, $b$, $k^*$; dự đoán kích thước mã và bộ mã rồi kiểm bằng số in ra.
- **Thể hiện:** dòng ô 83; bảng ba đại lượng với cột dự đoán và giá trị in ra; dòng sản phẩm.
- **Kết nối vào–ra:** dùng Q04, Q07; giao cấu trúc `pq_centroids`, `xb_codes` cho R02.
- **Ghi chú diễn giả:** đáp án; ý nghĩa ô 94; ô 88–89; hướng dẫn chấm.
- **Nguồn:** sổ thực hành ô 82–95 (đọc trực tiếp nội dung ô).
- **Quyết định:** sửa. Bản cũ yêu cầu “bảng kích thước” mà không nói điền gì; chưa nối tham số Faiss với ký hiệu bài giảng; dòng “Dữ kiện” liệt kê tên biến không giải thích.
