# Storyboard Bài 7

## Hành trình khái niệm

**Bản hiện hành từ 2026-10-16:** bản đồ mạch, thứ tự trang, thời lượng và mật độ nằm ở mục cuối "Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)". Các mục phía trên mục đó là lịch sử.

**Thứ tự hiện hành (2026-10-14, sau lượt sửa theo ba báo cáo rà).** Sáu gạch đầu dòng ngay sau đoạn này là thứ tự hiện hành; bốn gạch dưới nhãn "Bản 03/10/2026" giữ để đối chiếu.

- **Mở đầu:** bìa có luận đề P00 → tiên quyết P03 (LSH chỉ xác minh ứng viên cùng thùng, có thể bỏ sót) → mục tiêu P02 → Nội dung P04 → vấn đề trung tâm P05 (122,88 TB, ≈30,7 giây; ngân sách giả định 6 TB, 10 ms) → ví dụ truy hồi ngữ nghĩa P01 (gấp 3072 lần ngân sách 10 ms).
- **Bài toán:** AT → đặc tả tìm đúng và tìm gần đúng A00 (tối đa $K$ điểm; sai do đo một phần kho hoặc đo xấp xỉ) → độ thu hồi A01 → bốn trục A02 → hai thừa số chi phí A03.
- **HNSW:** HT → H00 → H01 → H03 → H03B → H04 → H05 → H06 → H06B → H07 → H09 → H08 → H10 → H10B → H11 → H12 → bộ nhớ H13 → truy vấn và giả thiết đồ thị Delaunay H14 → bảng giả thiết C03, bảng thuật toán C00, câu trả lời C04.
- **PQ:** QT → VQ Q00 (ba tâm trên mặt trang) → Q02 → Q03 → Q04 → ví dụ mã hóa Q05 (bốn tâm con trên mặt trang) → kích thước mã Q07 → ví dụ ADC Q06 → ADC Q08 → bảng tra Q09 → chi phí bảng tra Q11 (chấm một mã là phép đo xấp xỉ; $n_c$) → PQ quét đủ Q10 ($n_c=N$) → C00, C04.
- **IVF-PQ:** IT → tệp đảo I00 → chọn danh sách, câu hỏi $nprobe=3$ I01 → phần dư I02 → thuật toán I04 → vết, tập đúng $\{y_8,y_3,y_7\}$, câu hỏi recall@3 với $nprobe=1$ I05 → chi phí và bộ nhớ $(512+8)$ byte mỗi véc-tơ I03 → C00, C04 → tự kiểm C01–C02 → thực hành R06–R08.
- **Kết luận:** CT → C03 → C00 → C04 → C01 → C02 → C05.

Bản 03/10/2026:

- **HNSW (thứ tự hiện hành, 03/10/2026):** thừa số “số véc-tơ được đo” A03 → đồ thị lân cận H00 → tham lam, cực tiểu cục bộ H01 (gộp H02) → tìm kiếm chùm H03 → đặc tả H04 → giả mã H05 → bất biến H06 → cạnh dài H06B → đồ thị nhiều tầng H07 → giả mã truy vấn H09 → rút tầng H08 → ví dụ chèn H10 → giả mã chèn H10B → lân cận đa dạng H11 → tham số H12 → chi phí H13 → đối chiếu C00.
- **Lượng tử hóa tích (thứ tự hiện hành, 03/10/2026):** nhu cầu từ H13 → VQ, ví dụ ba tâm và câu hỏi Q00 (gộp Q01) → đặc tả và chi phí Q02 → giới hạn bộ mã lớn Q03 → định nghĩa PQ Q04 → ví dụ mã hóa Q05 → kích thước, so với VQ, kho $10^{10}$ véc-tơ Q07 → ví dụ ADC Q06 → công thức ADC Q08 → bảng tra Q09 → giới hạn quét đầy đủ Q10 → IVF-PQ I00–I04 → đối chiếu C00.
- **IVF-PQ (thứ tự hiện hành, 03/10/2026):** giới hạn quét đủ Q10 → tệp đảo, ví dụ bốn ô I00 → gán và chọn danh sách, câu hỏi bỏ sót $y_3$ I01 → phần dư, truy vấn dư I02 → thuật toán, vết, recall@3 I04 → chi phí thay số I03 → so sánh C00 → tự kiểm C01–C02 → thực nghiệm R06–R08.
- **LSH:** chu trình đã hoàn tất ở Bài 6; A03 chỉ nhắc cơ chế và C00 dùng lại để so sánh. Không áp dụng chạy tay hoặc chứng minh lại trong Bài 7 vì sẽ lặp nguồn.

Tình huống mở bài là truy hồi ngữ nghĩa với $N=10^{10}$ véc-tơ, $D=3072$, số thực 32 bit, đoạn 6 chiều và mã tâm 8 bit từ cấu hình BIODS trang 17. Đầu vào là véc-tơ truy vấn; đầu ra là $K$ mục gần truy vấn trong giới hạn bộ nhớ và độ trễ. Dữ kiện truyền sang A00 để nêu chi phí quét, Q07 để tính bộ nhớ mã, Q10 để chỉ ra quét mã vẫn tuyến tính, I00–I04 để cần phân vùng và C00 để đối chiếu cấu trúc. Đầu ra được đo bằng $\operatorname{recall@K}$ cùng độ trễ, chi phí xây dựng và bộ nhớ.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch"; yêu cầu người dùng 2026-10-14. Mỗi section ngoài trừ mạch mở đầu mở bằng một trang `class="strand-title"`, `id="mach-N"`. Mã theo quy ước của bài: mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch, nên trang tiêu đề mạch dùng `<tiền tố>T`. Trang tiêu đề mạch nằm ngoài chu trình khái niệm; thời lượng 0,5 phút mỗi trang lấy từ trang đầu mạch (cột "Trang đầu mạch"), tổng thời lượng bài không đổi. Deck 50 → 56 trang.

Bản đồ mạch (tên trùng từng chữ với trang Nội dung): 1. Mở đầu (mở bằng trang bìa P00); 2. Bài toán hàng xóm gần đúng (`AT`); 3. Tìm kiếm trên đồ thị HNSW (`HT`); 4. Lượng tử hóa tích (PQ) (`QT`); 5. Tệp đảo kết hợp PQ (IVF-PQ) (`IT`); 6. Tổng kết và tự kiểm tra (`CT`; tên cũ "So sánh và tự kiểm tra", đổi 2026-10-14); 7. Bài tập thực hành (`RT`).

| Mã trang | Tiêu đề (tên mạch) | Mục đích | Vị trí | Kiến thức đầu vào | Đầu ra | Ghi chú | Phút | Quyết định |
|---|---|---|---|---|---|---|---:|---|
| AT | Bài toán hàng xóm gần đúng | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 2, `id="mach-2"`, trước A00 | Kho $10^{10}$ véc-tơ và chi phí quét đầy đủ (P01) | Đặc tả ANN, độ thu hồi tại $K$, hai thừa số chi phí | ngoài chu trình khái niệm; tên khác tiêu đề A00 | 0,5 (từ A00) | thêm |
| HT | Tìm kiếm trên đồ thị HNSW | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 3, `id="mach-3"`, trước H00 | Hai thừa số chi phí truy vấn | SEARCH-LAYER, truy vấn và chèn HNSW, chi phí | ngoài chu trình khái niệm; tên khác tiêu đề H00 | 0,5 (từ H00) | thêm |
| QT | Lượng tử hóa tích (PQ) | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 4, `id="mach-4"`, trước Q00 | HNSW còn giữ véc-tơ gốc | Mã PQ, khoảng cách bất đối xứng, bảng tra | ngoài chu trình khái niệm; tên khác tiêu đề Q00 | 0,5 (từ Q00) | thêm |
| IT | Tệp đảo kết hợp PQ (IVF-PQ) | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 5, `id="mach-5"`, trước I00 | PQ quét đủ vẫn chấm mọi mã | Truy vấn IVF-PQ và chi phí | ngoài chu trình khái niệm; tên khác tiêu đề I00 | 0,5 (từ I00) | thêm |
| CT | Tổng kết và tự kiểm tra (đổi tên 2026-10-14) | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 6, `id="mach-6"`, trước C03 | Bốn cấu trúc, mô hình đếm, bộ nhớ và số thao tác của từng cấu trúc | Bảng giả thiết C03, bảng thuật toán C00, câu trả lời vấn đề trung tâm C04, hai trang tự kiểm tra, trang nguồn | ngoài chu trình khái niệm; tên khác tiêu đề C03 | 0,5 (từ C00) | thêm |
| RT | Bài tập thực hành | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 7, `id="mach-7"`, trước R00 | Công thức PQ và IVF-PQ | Ba nhiệm vụ đo trên sổ thực hành | ngoài chu trình khái niệm; tên khác tiêu đề R00 | 0,5 (từ R00) | thêm |

Trang Nội dung (P02 "Nội dung và mục tiêu"): danh sách `ul` sáu mục thiếu mạch mở đầu; đổi thành `ol` 1–7, thêm mục 1 "Mở đầu", các mục 2–7 trùng từng chữ với tên mạch. Notes thêm một câu cho mạch mở đầu. Trang gộp với ba mục tiêu, mặt trang khoảng 95 âm tiết, vượt trần 80; theo phạm vi đợt này chỉ đánh số, chưa tách. Quyết định: sửa.

## Từng trang phần giảng

| ID | Phút | Lý do tồn tại và bước tiến | Đầu vào → sản phẩm | Nguồn |
|---|---:|---|---|---|
| P00 | 0 | Nhận diện bài, ba cấu trúc và cầu nối từ bài toán tìm cặp của Bài 6 sang bài toán truy vấn. | LSH → HNSW, PQ, IVF-PQ | BIODS tr.16–18; Princeton 08–09 |
| P01 | 4 | Mở bằng tình huống truy hồi ngữ nghĩa: quy trình nhúng, dung lượng kho và chi phí quét một truy vấn. | $10^{10},3072$ → 122,88 TB, $3{,}07\cdot10^{13}$ tọa độ mỗi truy vấn | BIODS tr.16–17; tình huống dựng từ cấu hình nguồn |
| P02 | 2 | Nêu sáu phần của bài và ba mục tiêu học tập có sản phẩm cụ thể. | tình huống → dàn bài, mục tiêu | `sources/source.md` |
| A00 | 4 | Đặc tả tìm đúng ($K$-NN, phá hòa theo mã định danh), chi phí quét $\Theta(ND)$ và nới điều kiện thành tìm gần đúng (ANN). | $Y,q,d,K$ → $N_K(q)$, $\widehat N_K(q)$; $3{,}07\cdot10^{13}$ tọa độ | HNSW paper tr.1; PQ paper tr.1 |
| A01 | 3 | Định nghĩa độ thu hồi tại $K$, tính trên ví dụ năm phần tử và kiểm tra bằng một câu hỏi. | hai tập $K$ phần tử → recall@K; $3/5$, câu hỏi $2/5$ | HNSW paper tr.1 |
| A02 | 2 | Nêu bốn trục đánh giá, điều kiện giữ cố định và kiểm tra bằng so sánh A/B. | recall → chất lượng, truy vấn, xây dựng, bộ nhớ | Princeton 08 tr.2–5; Princeton 09 tr.2 |
| A03 | 2 | Tách chi phí truy vấn thành số véc-tơ được đo nhân chi phí một phép đo; gắn LSH, HNSW, PQ, IVF-PQ vào thừa số mỗi cấu trúc giảm. | $\Theta(ND)$ → hai thừa số → bản đồ cấu trúc | MMDS Ch.3; Princeton 09 tr.4,5,7; Princeton 08 tr.2 |
| H00 | 2 | Định nghĩa đồ thị lân cận trên đồ thị ví dụ bảy đỉnh; nêu dữ liệu lưu và ý tưởng đi tới đỉnh gần $q$ hơn. | véc-tơ → đỉnh, cạnh, điểm vào | Princeton 09 tr.7–8 |
| H01 | 4 | Chạy tay tham lam trên đồ thị ví dụ (hình và bảng vết cùng trang); định nghĩa cực tiểu cục bộ. Gộp H02 cũ. | $e:9\to a:7\to b:5$ → dừng ở cực tiểu cục bộ, bỏ $z:1$ | Princeton 09 tr.8, 11–13; ví dụ dựng từ cơ chế nguồn |
| H03 | 2 | Tách (duyệt lại): quy tắc tìm kiếm chùm trên mặt trang ($C$, $W$, mở đỉnh, thêm/bỏ, dừng) cạnh hình đồ thị ví dụ; $ef=1$ trùng tham lam. | đồ thị H00 → quy tắc chùm | Princeton 09 tr.9; HNSW paper alg.2 |
| H03B | 2 | Tách (duyệt lại): vết $ef=3$ (bảng gộp ba lần mở cuối) cạnh hình đường chùm; câu hỏi $ef=2$. | $e,a,b,s,\{t,u,z\}$ → $W=\{z,u,t\}$ | Princeton 09 tr.9; HNSW paper alg.2 |
| H04 | 2 | Đặc tả đầu vào, đầu ra và ba tập trạng thái của `SEARCH-LAYER`; hình trạng thái thật của ví dụ sau khi mở $b$. | $ep$, $ef$, $\ell_c$ → $W$; $C,W\subseteq V$ | HNSW paper tr.4 |
| H05 | 4 | Giả mã `SEARCH-LAYER` theo Thuật toán 2; nối dòng tính lại ngưỡng $f$ với bước mở $s$ của ví dụ. | $V,C,W$ → thuật toán; ngưỡng $8\to7$ | HNSW paper alg.2, tr.4 |
| H06 | 3 | Phát biểu và chứng minh bất biến “$W$ là $\min(ef,|V|)$ đỉnh của $V$ gần $q$ nhất” (khởi tạo, duy trì, khi dừng); minh họa giới hạn bằng lần chạy $ef=2$. | vết $ef=2$ → $W$ đúng trên $V$, $z\notin V$ | suy ra từ alg.2 |
| H06B | 2 | Thêm trang: ví dụ một chiều cho thấy cạnh dài giảm số bước tham lam từ 6 xuống 3; động cơ của các tầng HNSW. | chỉ cạnh ngắn → thêm cạnh dài | Princeton 09 tr.11–13; HNSW paper §3 tr.3 |
| H07 | 3 | Cấu trúc tầng (tầng 0 chứa mọi điểm, tầng trên là tập con thưa) và cách truy vấn đi xuống, trên cùng 12 điểm của H06B. | $s\to p4\to p8$ ↓ $p8\to p6$ ↓ $p6$ | HNSW paper Fig.1, §3, tr.3; Princeton 09 tr.17 |
| H09 | 3 | Đặc tả và giả mã truy vấn HNSW; hình gọn ba tầng nhắc lại vết $ep=p8$, $p6$. | tìm tầng → $K$ kết quả; $efSearch\ge K$ | HNSW paper alg.5, tr.5 |
| H08 | 3 | Chuyển xuống sau H09. Rút tầng ngẫu nhiên; suy ra $\Pr[\ell\ge k]=p^k$, $p=e^{-1/m_L}$; ví dụ $p=1/16$, tầng cao nhất khoảng 8 khi $N=10^{10}$. | $U,m_L$ → phân phối hình học, $\log_{1/p}N$ tầng | HNSW paper alg.1 dòng 4; §3; §4.1 |
| H10 | 3 | Tách: ví dụ chèn $x=2{,}6$, $\ell=1$, $M=2$ vào đồ thị ba tầng; bảng ba tầng và hình. | pha 1 → $ep=p4$; pha 2 → nối $p2,p4$ (tầng 1), $p3,p2$ (tầng 0) | HNSW paper alg.1, tr.4 |
| H10B | 3 | Tách: giả mã chèn hai pha và định nghĩa $M$, $efConstruction$, $M_{max}$, $M_{max,0}$. | điểm mới → HNSW cập nhật | HNSW paper alg.1, tr.4; §4.1 tr.5–6 |
| H11 | 3 | Quy tắc chọn lân cận đa dạng; ví dụ hai chiều bốn ứng viên so với chọn gần nhất. | $\{c1,c3\}$ → $\{c1,c4\}$ | HNSW paper alg.4, tr.4–5; Princeton 09 tr.18 |
| H12 | 2 | Ba tham số, thời điểm dùng và đánh đổi; câu hỏi giảm độ trễ không xây lại. | $M$, $efConstruction$, $efSearch$ → chọn tham số | HNSW paper §4.1 tr.5–6; §4.2.3 tr.8 |
| H13 | 3 | Chi phí bộ nhớ thay số cho $10^{10}$ véc-tơ (véc-tơ 122,88 TB, cạnh khoảng 2,65 TB); chi phí truy vấn và giới hạn $\log N$; nối sang PQ. | giả định $M=16$ → 98% bộ nhớ là véc-tơ gốc | HNSW paper §4.2 tr.7, §4.2.3 tr.8; Princeton 09 tr.2, 7 |
| Q00 | 4 | Gộp Q01: mở phần 4 từ nhu cầu giảm bộ nhớ; lượng tử hóa véc-tơ trên hình ba tâm, phép tính mã và tái dựng, câu hỏi điểm $y$. | $x=(1{,}7;0{,}4)$ → mã 1, sai số 0,25; $y$ → mã 2, 0,61 | Princeton 08 tr.8–9; PQ paper §II-A tr.2 |
| Q02 | 2 | Đặc tả VQ: đầu vào (bộ mã học bằng k-means), đầu ra và điều kiện sau, chi phí mã hóa $\Theta(kD)$ và lưu $kD$ số. | ví dụ Q00 → $i(x),\widehat x$, chi phí theo $k$ | PQ paper eq.2–5, tr.2; Princeton 08 tr.9–10, 32 |
| Q03 | 2 | Thay số chi phí của một bộ mã $k=2^{64}$, $D=128$: lưu, mã hóa, học. | $9{,}4\cdot10^{21}$ byte → cần bộ mã nhỏ cho mã dài | PQ paper §II-B tr.3; Princeton 08 tr.18 |
| Q04 | 3 | Định nghĩa PQ: chia đoạn, bộ mã con, mã $m\log_2k^*$ bit, tái dựng bằng ghép tâm con; hình $D=8$, $m=4$. | $D$ → $m$ đoạn → mã 32 bit | PQ paper §II-B eq.8–9, tr.3; Princeton 08 tr.29–31 |
| Q05 | 3 | Chạy tay mã PQ hai đoạn: khoảng cách từng đoạn, mã, tái dựng, sai số; hình hai mặt phẳng con. | hai bộ mã → mã $(0,1)$, sai số 0,18 | suy ra từ định nghĩa nguồn |
| Q07 | 3 | Kích thước mã và bộ mã PQ; so với VQ cùng mã 64 bit; thay số cho kho $10^{10}$ véc-tơ (512 byte, 5,12 TB). | $m,k^*,D,b$ → $k^*D$ số, $\lceil mb/8\rceil$ byte | PQ paper §II-B tr.3; Princeton 08 tr.32–33; BIODS tr.17 |
| Q06 | 3 | Chuyển sau Q07. Ví dụ ADC: định nghĩa bằng lời, hình hai đoạn có $q$, bảng hai số hạng, so 0,31 với giá trị đúng 0,07. | mã $(0,1)$ + $q$ → 0,31 | PQ paper eq.13, tr.4; Princeton 08 tr.25–26 |
| Q08 | 2 | Công thức ADC; mỗi số hạng chỉ phụ thuộc $q^{(j)}$ và chỉ số $i_j$, nên mỗi đoạn có $k^*$ giá trị tính trước được. | truy vấn đầy đủ + mã → tổng $m$ số hạng | PQ paper §III-A eq.13, tr.4; Princeton 08 tr.26–27 |
| Q09 | 3 | Bảng tra trên ví dụ hai đoạn (ô của mã $(0,1)$ đánh dấu); chi phí lập bảng, chấm mã so với tính trực tiếp. | $T$ 2×2 → 0,31 và 13,51; $\Theta(k^*D)$, $m$ lần tra | PQ paper §III-A tr.4; Princeton 08 tr.27, 31–32 |
| Q10 | 3 | Thay số quét mã PQ so với quét véc-tơ gốc cho $10^{10}$ véc-tơ; câu hỏi thời gian; nối sang chỉ mở một phần kho. | 5,12 TB, $5{,}12\cdot10^{12}$ lần tra, 5,12 s | PQ paper tr.2, §IV tr.6; Princeton 08 tr.20–22 |
| I00 | 3 | Định nghĩa tệp đảo trên ví dụ bốn ô, mười sáu điểm; vai trò của IVF và PQ trong IVF-PQ. | $q=(6;3{,}5)$, $nprobe=2$ → mở $L_1,L_0$, chấm 8/16 | Princeton 08 tr.21–22; PQ paper §IV tr.6–7 |
| I01 | 3 | Công thức gán vào tâm thô; xếp bốn tâm theo khoảng cách tới $q$; câu hỏi $nprobe=1$ bỏ sót $y_3$. | $q$ → thứ tự $\mu_1,\mu_0,\mu_3,\mu_2$ | Princeton 08 tr.21–22; PQ paper §IV-A, IV-C tr.6–7 |
| I02 | 3 | Phần dư $r(y)$, đẳng thức $\|q-y\|=\|(q-\mu_i)-r(y)\|$, một bảng tra cho mỗi danh sách mở; ví dụ $y_8$. | $r(y_8)$, $\widetilde q_1$, $\widetilde q_0$ → 1,25 | PQ paper §IV-A, IV-B tr.6, eq.31 |
| I04 | 4 | Giả mã truy vấn IVF-PQ; vết trên bốn danh sách ($nprobe=2$, $K=3$); câu hỏi $nprobe=1$. | $y_8,y_3,y_7$; $nprobe=1$ → recall@3 $=2/3$ | PQ paper §IV-C tr.7; Princeton 08 tr.21 |
| I03 | 3 | Chuyển sau I04. Đếm chi phí truy vấn theo ba bước, thay số cho $10^{10}$ véc-tơ với $k_c=10^5$, $nprobe=64$. | $\approx3{,}6\cdot10^9$, ít hơn 1400 lần quét đủ | PQ paper §IV-C tr.7; Princeton 08 tr.22; 09 tr.5 |
| C00 | 5 | So sánh LSH, HNSW, PQ quét đủ, IVF-PQ theo thừa số được giảm, bộ nhớ, truy vấn, tham số; thu hồi tình huống mở đầu bằng số. | 125 TB và 5,2 TB; $3{,}6\cdot10^9$ thao tác | tổng hợp các nguồn; số liệu suy ra từ H13, Q07, Q10, I03 |
| C01 | 5 | Thêm: ba câu tự kiểm (độ thu hồi; tìm kiếm chùm $ef=2$/$ef=3$; bộ nhớ HNSW so 64 GB). | đáp án $1/2$; không/có; 77,7 GB | dữ kiện học phần dựng |
| C02 | 5 | Thêm: ba câu tự kiểm (kích thước PQ $D=960$; ADC bằng bảng tra; số mã IVF-PQ). | 8 byte, 245 760 số; 3,6; 500 000 mã | PQ paper (GIST $D=960$); Princeton 09 tr.5 |

Tổng phần giảng: **120 phút** (cân lại ngày 03/10/2026: 41 trang sau khi tách H03; mở đầu 6, bài toán 11, HNSW 44, PQ 28, IVF-PQ 16, tổng kết 15 phút).

## Từng trang bài tập

| ID | Phút | Vai trò và sản phẩm hiển thị | Đáp án hoặc hướng dẫn chấm trong notes | Nguồn trực tiếp |
|---|---:|---|---|---|
| R00 | 0 | Nêu sổ thực hành, ô chuẩn bị, bốn mảng dữ liệu (kích thước, vai trò, ánh xạ ký hiệu) và ba nhiệm vụ với ô nguồn. | `xt` $10^6$, `xb` $10^4$, `xq` 100, `gt` 10 hàng xóm | Princeton runbook lớp 8, ô 0–4, 17, 21–24 |
| R01 | 6 | Chạy ô 83–95; dự đoán rồi đối chiếu `code_size`, dạng `pq_centroids`, `xb_codes` với công thức của bài. | 4 byte; $(4,256,16)$; $(10\,000,4)$ | ô 82–95 |
| R02 | 9 | Hoàn thiện ô 96 (tái dựng véc-tơ 123 không gọi `decode`) với gợi ý công thức tái dựng; ô 97 in `True`. | ghép `pq_centroids[j, xb_codes[123,j]]` theo $j$ | ô 96–97 |
| R03 | 5 | Với ba điều kiện khớp, nêu hậu quả khi vi phạm, gắn với ký hiệu của $\widehat x$. | đáp án mẫu và rubric 10 điểm trong ghi chú | ô 96–97 |
| R04 | 10 | Ô 99: ba cấu hình 6 byte; dự đoán $D/m$, $k^*$; ghi MSE và thời gian mã hóa–giải mã. | $D/m=16,8,4$; $k^*=4096,64,8$ | ô 98–99 |
| R05 | 10 | Phân tích bảng nhiệm vụ 2: `code_size`, xếp hạng MSE so với nhận định của nguồn, thời gian giải thích bằng $k^*D$. | rubric 10 điểm; không có số cố định | ô 98–99; Princeton 08 tr.32–33 |
| R06 | 6 | Chạy ô 149–151; đọc $k_c$, $m$, $b$, byte mã, $N/k_c$ từ `IVF200,PQ16x8np`; nêu vai trò ô 150, 151. | 200; 16; 8; 16 byte; 50 | ô 148–151; tài liệu Faiss index factory chỉ kiểm chứng `np` |
| R07 | 9 | Chạy ô 152–155; hiểu ba đại lượng đo: $nok/100=\operatorname{recall@1}$, tổng ms của $50\times100$ truy vấn, $nprobe/200$ và số mã được chấm. | đại lượng đo → phiếu R08 | ô 152–155; Princeton 08 tr.4 |
| R08 | 5 | Phiếu năm dòng ($nprobe$ cho sẵn): recall@1, tổng ms, ms mỗi truy vấn, số mã được chấm; đồ thị và giải thích. | $50\,nprobe$ mã; rubric 10 điểm | ô 149–155 |

Tổng recitation: **60 phút**. Bài tập giữ dữ kiện và yêu cầu nguồn; các trang chỉ chia bước và thêm mẫu sản phẩm.

## Storyboard ghi chú tự học

Ghi chú dùng `L07-N01`–`L07-N11` trong outline. Mỗi chủ đề cốt lõi theo vai trò → đặc tả → ví dụ → trực quan → thuật toán/mệnh đề → lập luận đúng → chi phí, giới hạn và kiểm tra.

- `N01–N02` khóa bài toán, phép đo và cầu từ Bài 06; không lặp banding.
- `N03–N06` truyền cùng ví dụ đồ thị từ tham lam sang chùm, `SEARCH-LAYER`, truy vấn và chèn HNSW; bất biến chỉ nói về phần đã thăm.
- `N07–N09` truyền cùng phép chia véc-tơ, mã PQ và bảng ADC sang phần dư IVF-PQ; phân biệt mã, véc-tơ tái dựng và mã định danh trả về.
- `N10` thu hồi tình huống mở bài bằng bốn trục đo, không xếp hạng phổ quát.
- `N11` giữ đúng trạng thái notebook và ba nhiệm vụ nguồn; không thêm bài HNSW hoặc kết quả số cố định.

Các ví dụ đồ thị, ADC và chi phí IVF-PQ do học phần dựng lại hoặc suy ra phải ghi rõ. Mã trang nội bộ và thời lượng không xuất hiện trong ghi chú công khai.

## Sửa toàn diện theo chuẩn 2026-10-14

Căn cứ: `AGENTS.md` ("Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch", "Văn phong và mật độ mặt trang chiếu", "Tiêu chuẩn trang chiếu và ghi chú diễn giả"), `slide_authoring_standard.md`, deck mẫu Bài 06; quyết định của điều phối viên (mục "Bài 07" và "Chung cho mọi bài"). Deck 56 → 65 trang: 55 trang giảng (120 phút) và 10 trang bài tập (60 phút); bảy mạch 6/5/18/12/7/7/10. Từ đây, thứ tự, quyết định, số âm tiết và thời lượng của bảng dưới là bản hiện hành; các bảng "Từng trang phần giảng", "Từng trang bài tập" và các mục "Chi tiết từng trang" phía trên là bản kế hoạch trước đợt sửa (mỗi mục chi tiết có thêm dòng **Sửa 2026-10-14**). Mặt trang và ghi chú hiện hành nằm trong tệp HTML. Thời lượng chỉ ghi ở đây, không trong ghi chú diễn giả. Phần giảng 55 trang (dưới 60) nên không bắt buộc mục phân bổ thời gian riêng.

| Mạch | Tên (khớp trang Nội dung) | Số trang | Phút | Vai trò chu trình của trang mở mạch |
|---|---|---:|---:|---|
| 1 | Mở đầu | 6 | 8 | bìa là trang tiêu đề mạch mở đầu |
| 2 | Bài toán hàng xóm gần đúng | 5 | 11 | AT ngoài chu trình khái niệm |
| 3 | Tìm kiếm trên đồ thị HNSW | 18 | 42 | HT ngoài chu trình khái niệm |
| 4 | Lượng tử hóa tích (PQ) | 12 | 28 | QT ngoài chu trình khái niệm |
| 5 | Tệp đảo kết hợp PQ (IVF-PQ) | 7 | 16 | IT ngoài chu trình khái niệm |
| 6 | Tổng kết và tự kiểm tra (đổi tên từ "So sánh và tự kiểm tra") | 7 | 15 | CT ngoài chu trình khái niệm |
| 7 | Bài tập thực hành | 10 | 60 | RT 0,5 phút lấy từ R01 (sửa mâu thuẫn cũ "lấy từ R00" trong khi R00 bằng 0) |

Cột "Âm tiết" ghi số trước đợt sửa → số hiện hành (sau lượt sửa theo ba báo cáo rà); cột "Dòng" đếm lại sau lượt sửa đó bằng `scratchpad/w07/dong.py`: mỗi đoạn `p`, mục `li`, hàng bảng `tr` kể cả hàng tiêu đề, hộp Câu hỏi, kể cả đoạn chỉ có công thức; giả mã và mã đếm riêng. Âm tiết đếm bằng biến thể của `scratchpad/tools/density.py` có tính trang đầu mỗi section ngoài và bỏ công thức `$...$` (chạy `python3 -I m07.py 2627-1/lecture-07-chi-muc-hang-xom-gan-dung.html`); script đếm chữ trong ô bảng và chuỗi `<code>`. "Dòng" là số đoạn, mục danh sách và hàng bảng kể cả hàng tiêu đề.

| # | Mã | Tiêu đề hiện hành | Quyết định | Âm tiết trước → sau | Trần | Dòng | Phút | Lý do |
|---:|---|---|---|---|---:|---:|---:|---|
| 1 | P00 | Chỉ mục hàng xóm gần đúng | `sửa` | 36 → 49 | — | 4 | 0,5 | câu luận đề của điều phối viên thay dòng phụ; ghi chú mở bằng kết quả Bài 06, viết đủ tên HNSW, bỏ "Bài này"; sửa sau rà: bỏ "(PQ)" khỏi luận đề (25 token) |
| 2 | P03 | Tiên quyết và quy ước | `thêm` | — → 59 | 60 | 5 | 1,5 | mạch mở đầu bắt buộc có Tiên quyết và quy ước; giải nghĩa HNSW ở lần đầu sau bìa; k-means và hàng đợi ưu tiên trong ghi chú (quyết định 8); sửa sau rà: dòng LSH theo Bài 06 (xác minh ứng viên, có thể bỏ sót) |
| 3 | P02 | Mục tiêu học tập | `tách` | 86 → 50 | 80 | 3 | 1 | trang gộp mục tiêu và Nội dung 86 > 80; giữ ba mục tiêu nguyên chữ (quyết định 4); ánh xạ mục tiêu → bằng chứng trong ghi chú; sửa sau rà: PQ viết đủ tên ở lần đầu |
| 4 | P04 | Nội dung | `thêm` | — → 51 | 80 | 8 | 0,5 | Nội dung tách từ P02; mạch 6 đổi tên (quyết định 2); thêm Đọc trước |
| 5 | P05 | Vấn đề trung tâm | `thêm` | — → 60 | 60 | 6 | 1,5 | mạch mở đầu bắt buộc có Vấn đề trung tâm; dòng 2–6 là câu trả lời có điều kiện của mạch cùng số; sửa sau rà: giới hạn tài nguyên bằng số, ngân sách giả định |
| 6 | P01 | Ví dụ: truy hồi ngữ nghĩa trên mười tỷ véc-tơ | `sửa` | 34 → 35 | 60 | 4 | 3 | khuôn trang ví dụ: dữ kiện, hình, hai dòng phép tính thay hai thẻ có chữ, hộp Câu hỏi; sửa sau rà: câu hỏi đổi sang tỷ số với 10 ms |
| 7 | AT | 2.Bài toán hàng xóm gần đúng | `giữ` | 41 → 41 | — | 2 | 0,5 | dòng dẫn và từ khóa đạt chuẩn |
| 8 | A00 | Bài toán $K$ hàng xóm gần nhất | `sửa` | 76 → 60 | 60 | 4 | 3,5 | hai thẻ có câu và câu kết thành bốn dòng Nhu cầu, Đầu vào, Đầu ra (tìm đúng, tìm gần đúng); ANN giải nghĩa; sửa sau rà: tối đa $K$; hai nguồn sai số |
| 9 | A01 | Độ thu hồi tại $K$ | `sửa` | 26 → 33 | 60 | 4 | 3 | định nghĩa bằng "là", "độ thu hồi (recall)"; dòng Ví dụ. |
| 10 | A02 | Bốn trục đánh giá chỉ mục | `sửa` | 79 → 77 | 80 | 6 | 2 | rút ô bảng; ngoại lệ trần 80 (bảng so sánh) |
| 11 | A03 | Hai cách giảm chi phí truy vấn | `sửa` | 75 → 57 | 80 | 6 | 2 | dòng Mô hình và bảng bốn cấu trúc thay hai thẻ có câu và câu kết; sửa sau rà: "đo bằng mã PQ"; ghi chú bỏ câu phạm vi soạn |
| 12 | HT | 3.Tìm kiếm trên đồ thị HNSW | `sửa` | 33 → 33 | — | 2 | 0,5 | ghi chú viết đủ tên HNSW |
| 13 | H00 | Đồ thị lân cận | `sửa` | 56 → 48 | 60 | 3 | 1 | dòng Nhu cầu; định nghĩa bằng "là"; gạch "Tìm" và câu kết sang ghi chú |
| 14 | H01 | Tìm kiếm tham lam | `sửa` | 49 → 40 | 60 | 7 | 4 | tách dòng 29 âm tiết; dòng Ký hiệu; Kết luận có nhãn |
| 15 | H03 | Tìm kiếm chùm | `sửa` | 75 → 53 | 60 | 4 | 2 | dòng Nhu cầu; cặp "tương tự … nhưng …"; "tìm kiếm chùm (beam search)"; quy tắc thêm/bỏ sang ghi chú |
| 16 | H03B | Ví dụ: tìm kiếm chùm trên đồ thị bảy đỉnh | `sửa` | 26 → 35 | 60 | 8 | 2 | tiêu đề "Ví dụ: …"; dòng yêu cầu; sửa sau rà: dòng yêu cầu ghi ba lần mở cuối gộp một hàng |
| 17 | H04 | Thuật toán: SEARCH-LAYER | `sửa` | 38 → 43 | 60 | 4 | 2 | tiêu đề "Thuật toán: SEARCH-LAYER"; "Trạng thái:" thành "Ký hiệu:" |
| 18 | H05 | Thuật toán: SEARCH-LAYER | `sửa` | 8 → 8 | 60 | 1 | 3,5 | tiêu đề "Thuật toán: SEARCH-LAYER"; takeaway thành "Ví dụ."; ghi chú đọc giả mã |
| 19 | H06 | Tính đúng: SEARCH-LAYER | `sửa` | 39 → 54 | 60 | 6 | 3 | tiêu đề "Tính đúng: …"; Bất biến, Điều kiện dừng có nhãn; Ví dụ. |
| 20 | H06B | Ví dụ: cạnh dài trên mười hai điểm thẳng hàng | `sửa` | 47 → 34 | 60 | 3 | 2 | tiêu đề "Ví dụ: …"; dòng Nhu cầu; tách dòng 24, 23; rút ghi chú |
| 21 | H07 | Đồ thị nhiều tầng | `sửa` | 37 → 45 | 60 | 4 | 2,5 | tách dòng 21 thành bốn gạch; câu cạnh dài/ngắn sang ghi chú |
| 22 | H09 | Thuật toán: truy vấn HNSW | `sửa` | 26 → 26 | 60 | 3 | 3 | tiêu đề "Thuật toán: …"; Đầu vào/Đầu ra hai dòng; "Ví dụ." thay ex-note |
| 23 | H08 | Rút ngẫu nhiên tầng của điểm mới | `sửa` | 36 → 53 | 60 | 6 | 3 | khuôn trang kết quả: Nhu cầu, Mệnh đề., Chứng minh., Ý nghĩa:, Ví dụ.; bỏ hai thẻ có câu |
| 24 | H10 | Ví dụ: chèn một điểm vào đồ thị ba tầng | `sửa` | 46 → 37 | 60 | 6 | 3 | tiêu đề "Ví dụ: …"; dòng dữ kiện rút; Kết luận có nhãn; sửa sau rà: tiêu đề không chứa biến; tầng $0,\ldots,\ell$ |
| 25 | H10B | Thuật toán: chèn HNSW | `sửa` | 19 → 15 | 60 | 2 | 3 | tiêu đề "Thuật toán: …"; Đầu vào/Đầu ra; định nghĩa tham số sang ghi chú |
| 26 | H11 | Chọn lân cận đa dạng | `sửa` | 22 → 36 | 60 | 5 | 2,5 | thêm Nhu cầu; sửa sau rà: nhãn hàng $d(\cdot,c1)$ so với $d(\cdot,x)$ |
| 27 | H12 | Ba tham số của HNSW | `sửa` | 71 → 65 | 80 | 5 | 2 | rút ô; ngoại lệ trần 80 (bảng so sánh); sửa sau rà: hộp câu hỏi 17 âm tiết |
| 28 | H13 | Chi phí: bộ nhớ HNSW | `tách` | 83 → 50 | 80 | 6 | 1,5 | 83 âm tiết, dòng 40; giữ bộ nhớ ở H13, chuyển truy vấn sang H14; "Giả định:" thành "Giả thiết:"; một câu kết luận |
| 29 | H14 | Chi phí: truy vấn HNSW | `thêm` | — → 60 | 60 | 5 | 1,5 | tách từ H13: chi phí truy vấn với hai giả thiết của kết luận log N trên mặt trang; sửa sau rà: giải nghĩa đồ thị Delaunay trên mặt trang |
| 30 | QT | 4.Lượng tử hóa tích (PQ) | `giữ` | 39 → 39 | — | 2 | 0,5 | dòng dẫn và từ khóa đạt chuẩn |
| 31 | Q00 | Lượng tử hóa véc-tơ | `sửa` | 38 → 46 | 60 | 6 | 3,5 | dòng Nhu cầu; "lượng tử hóa véc-tơ (vector quantization, VQ)"; tách dòng 24; Ví dụ.; sửa sau rà: ba tâm trên mặt trang |
| 32 | Q02 | Thuật toán: mã hóa VQ | `sửa` | 34 → 36 | 60 | 4 | 2 | tiêu đề "Thuật toán: mã hóa VQ"; bảng ba hàng thành Đầu vào, Đầu ra và một câu chi phí |
| 33 | Q03 | Chi phí: một bộ mã lớn | `sửa` | 76 → 67 | 80 | 7 | 2 | tiêu đề "Chi phí: …"; Nhu cầu, Mô hình; tách dòng 25, 24; Kết luận có nhãn |
| 34 | Q04 | Mã PQ và tái dựng | `sửa` | 26 → 42 | 60 | 4 | 3 | tiêu đề "Mã PQ và tái dựng" để khác tên mạch; Nhu cầu; Định nghĩa.; "tương tự VQ, nhưng …"; sửa sau rà: "($m$ chia hết $D$)" sang ghi chú |
| 35 | Q05 | Ví dụ: mã hóa PQ hai đoạn | `sửa` | 11 → 22 | 60 | 6 | 3 | tiêu đề "Ví dụ: …"; dòng yêu cầu; sửa sau rà: bốn tâm con trên mặt trang |
| 36 | Q07 | Chi phí: kích thước mã và bộ mã PQ | `sửa` | 41 → 43 | 80 | 6 | 3 | tiêu đề "Chi phí: …"; Kết luận có nhãn |
| 37 | Q06 | Ví dụ: khoảng cách bất đối xứng của mã $(0,1)$ | `sửa` | 22 → 22 | 60 | 6 | 3 | tiêu đề "Ví dụ: …" |
| 38 | Q08 | Khoảng cách bất đối xứng (ADC) | `sửa` | 34 → 51 | 60 | 5 | 2 | Định nghĩa. với "asymmetric distance computation"; Kết luận có nhãn; ghi chú bỏ "Bài này" |
| 39 | Q09 | Bảng tra khoảng cách | `tách` | 44 → 20 | 60 | 6 | 2 | 10 dòng; giữ định nghĩa bảng và ví dụ, bảng chi phí sang Q11 |
| 40 | Q11 | Chi phí: bảng tra và chấm mã | `thêm` | — → 55 | 80 | 6 | 1 | tách từ Q09: bảng Bước | Số lần | Chi phí mỗi lần | Đóng góp; sửa sau rà: chấm một mã là phép đo xấp xỉ |
| 41 | Q10 | Chi phí: PQ quét đầy đủ | `sửa` | 59 → 61 | 80 | 7 | 3 | tiêu đề "Chi phí: …"; Kết luận có nhãn; ngoại lệ trần 80 (bảng so sánh); sửa sau rà: $n_c=N$ |
| 42 | IT | 5.Tệp đảo kết hợp PQ (IVF-PQ) | `giữ` | 36 → 36 | — | 2 | 0,5 | dòng dẫn và từ khóa đạt chuẩn |
| 43 | I00 | Tệp đảo (IVF) | `sửa` | 54 → 46 | 60 | 4 | 2,5 | Nhu cầu; "tệp đảo (inverted file, IVF)" bằng "là"; bảng bốn danh sách bỏ (hình đã có); Ví dụ. |
| 44 | I01 | Chọn danh sách cần mở | `sửa` | 13 → 15 | 60 | 7 | 3 | "Đáp án" thành "Lời giải" trong ghi chú; sửa sau rà: câu hỏi đổi sang $nprobe=3$ |
| 45 | I02 | Mã hóa phần dư | `sửa` | 27 → 37 | 60 | 5 | 3 | thêm Nhu cầu; Ví dụ.; sửa sau rà: "thường nhỏ hơn"; bỏ chữ Việt trong công thức |
| 46 | I04 | Thuật toán: truy vấn IVF-PQ | `tách` | 32 → 32 | 60 | 2 | 2,5 | Đầu vào/Đầu ra trước giả mã; vết đối chiếu sang I05 cùng tiêu đề |
| 47 | I05 | Thuật toán: truy vấn IVF-PQ | `thêm` | — → 26 | 60 | 6 | 1,5 | tách từ I04: vết chạy và câu hỏi nprobe = 1; sửa sau rà: tập đúng trên mặt trang |
| 48 | I03 | Chi phí: truy vấn IVF-PQ | `sửa` | 43 → 64 | 80 | 8 | 3 | tiêu đề "Chi phí: …"; Mô hình, Giả thiết; bảng về khuôn chung bốn cột; sửa sau rà: ba chữ số ở cột Đóng góp; bộ nhớ 5,2 TB |
| 49 | CT | 6.Tổng kết và tự kiểm tra | `sửa` | 31 → 41 | — | 2 | 0,5 | đổi tên "Tổng kết và tự kiểm tra" (quyết định 2); dòng dẫn, từ khóa, ghi chú; sửa sau rà: từ khóa 19 âm tiết |
| 50 | C03 | Kết quả và giả thiết không được bỏ | `thêm` | — → 80 | 80 | 8 | 2 | bảng Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán bắt buộc |
| 51 | C00 | Thuật toán, bảo đảm và chi phí | `sửa` | 99 → 77 | 80 | 6 | 3 | đổi sang khuôn Thuật toán | Đầu vào | Bảo đảm | Chi phí (quyết định 3); câu kết 31 âm tiết sang C04; sửa sau rà: hàng LSH có bảo đảm xác suất, chi phí cùng mô hình; "byte mỗi véc-tơ" |
| 52 | C04 | Câu trả lời cho vấn đề trung tâm | `thêm` | — → 69 | 80 | 6 | 2 | trang trả lời vấn đề trung tâm theo thứ tự P05; sửa sau rà: trả lời bằng TB và giây |
| 53 | C01 | Câu hỏi tự kiểm tra | `sửa` | 53 → 50 | 60 | 4 | 3,5 | "Câu hỏi tự kiểm tra"; câu 3 tách; ghi chú nêu kết quả đã dùng, ánh xạ mục tiêu chuyển storyboard |
| 54 | C02 | Câu hỏi tự kiểm tra | `sửa` | 48 → 53 | 60 | 4 | 3,5 | như C01; ol start=4 |
| 55 | C05 | Nguồn và tài liệu đọc | `thêm` | — → 64 | 80 | 5 | 0,5 | trang nguồn; không ghi công mmds.org (quyết định 5); không dòng nối Bài 08 (quyết định 6); sửa sau rà: trang, năm; dòng MMDS |
| 56 | RT | 7.Bài tập thực hành | `giữ` | 40 → 40 | — | 2 | 0,5 | 0,5 phút lấy từ R01 (quyết định 10) |
| 57 | R00 | Sổ thực hành và dữ liệu | `sửa` | 45 → 47 | 80 | 10 | 0 | nhãn Thực hành (quyết định 7) |
| 58 | R01 | Bài tập: mã và tái dựng PQ (a) | `sửa` | 34 → 44 | 80 | 7 | 5,5 | tiêu đề "Bài tập: … (a)"; "Sản phẩm:" thành Câu hỏi; dòng Nguồn; ghi chú có năng lực kiểm và Gợi ý |
| 59 | R02 | Bài tập: mã và tái dựng PQ (b) | `sửa` | 26 → 37 | 80 | 3 | 9 | "Gợi ý:" thành "Nhắc lại:"; "Yêu cầu:" thành Câu hỏi; dòng Nguồn |
| 60 | R03 | Bài tập: mã và tái dựng PQ (c) | `sửa` | 69 → 72 | 80 | 7 | 5 | tách dòng 22; "Sản phẩm:" vào Câu hỏi; dòng Nguồn |
| 61 | R04 | Bài tập: cùng ngân sách 6 byte (a) | `sửa` | 37 → 48 | 80 | 7 | 10 | MSE giải nghĩa; Câu hỏi; dòng Nguồn |
| 62 | R05 | Bài tập: cùng ngân sách 6 byte (b) | `sửa` | 63 → 66 | 80 | 5 | 10 | "Yêu cầu" và "Sản phẩm:" thành Câu hỏi; dòng Nguồn; trần 80; sửa sau rà: "bảng ở trang (a)" |
| 63 | R06 | Bài tập: chỉ mục IVF-PQ (a) | `sửa` | 33 → 38 | 80 | 5 | 6 | "Sản phẩm:" thành Câu hỏi; dòng Nguồn |
| 64 | R07 | Bài tập: chỉ mục IVF-PQ (b) | `sửa` | 33 → 33 | 80 | 4 | 9 | thêm Câu hỏi có ô nguồn (không thêm dòng Nguồn riêng vì trang chật); sửa sau rà: bỏ hàng $nprobe/200$ |
| 65 | R08 | Bài tập: chỉ mục IVF-PQ (c) | `sửa` | 44 → 42 | 80 | 8 | 5 | tách dòng 30; "Yêu cầu:" thành Câu hỏi; dòng Nguồn; sửa sau rà: gộp hai dòng Câu hỏi (8 dòng) |

Tổng phần giảng 8 + 11 + 42 + 28 + 16 + 15 = 120 phút; bài tập 0,5 + 0 + 5,5 + 9 + 5 + 10 + 10 + 6 + 9 + 5 = 60 phút.

**Mật độ (sau lượt sửa theo ba báo cáo rà, 2026-10-14).** Không trang trần 60 nào vượt 60 (P05, A00, H14 bằng 60); không trang trần 80 nào vượt 80 (C03 80, C00 77). Trang trên 60 đều có trần 80: A02, H12, Q03, I03, C03, C00, C04, C05, R03, R05. Không dòng chữ nào vượt 20 âm tiết, trừ dòng dẫn của trang tiêu đề mạch (21–23, trần 25). Câu luận đề trên bìa 25 token (trần 25). Câu cũ "Không dòng chữ nào vượt 20 âm tiết" của bản trước sai ở CT (từ khóa 22) và H12 (hộp câu hỏi 22); cả hai đã rút.

**Ngoại lệ dòng (không phải ngoại lệ âm tiết), đếm lại 2026-10-14.** Trần 6 dòng chữ; trang có bảng tới 8 dòng kể cả hàng tiêu đề. Trang 7–8 dòng vì có bảng: H01 (7, vết chạy), H03B (8, vết chạy 6 hàng, yêu cầu, câu hỏi), Q03 (7), Q10 (7), I01 (7, công thức, bảng 5 hàng, câu hỏi), I03 (8), C03 (8), P04 (8, bảy mạch và Đọc trước), R01, R03, R04 (7), R08 (8, phiếu 6 hàng, câu hỏi, nguồn; trước lượt sửa là 9). Ngoại lệ trên 8: R00 (10 dòng, hai bảng dữ kiện của sổ thực hành). Giả mã hoặc mã đứng riêng kèm tối đa hai dòng: H05 (15 dòng giả mã), H09 (8), H10B (12), I04 (10), R02 (7), R06 (5), R07 (mã 10 dòng kèm câu hỏi và bảng 3 hàng; hàng $nprobe/200$ bỏ để trang cách chân trang xa hơn).

**Loại kiểm tra theo mạch.** Mạch 2: câu hỏi trong trang A01, A02 (lời giải trong ghi chú). Mạch 3: câu hỏi trong trang H03B, H12. Mạch 4: câu hỏi trong trang Q00, Q10. Mạch 5: câu hỏi trong trang I01, I05. Mạch 6: hai trang "Câu hỏi tự kiểm tra" C01, C02, lời giải trong ghi chú. Mạch 7: chín trang bài tập thực hành theo sổ Princeton COS 597A lớp 8, gợi ý, lời giải và hướng dẫn chấm trong ghi chú.

**Ánh xạ câu tự kiểm tra → mục tiêu (chuyển từ ghi chú diễn giả C01, C02).** Câu 1 → mục tiêu 1; câu 2 → mục tiêu 2; câu 3 → mục tiêu 3; câu 4 → mục tiêu 3; câu 5 → mục tiêu 2; câu 6 → mục tiêu 3.

**Chu trình các cụm (bổ sung).** Mở đầu theo khuôn: bìa có luận đề → P03 → P02 → P04 → P05 → P01 (ví dụ dẫn nhập có số). HNSW: H13 (bộ nhớ) và H14 (truy vấn, giả thiết $\log N$) là bước chi phí. PQ: Q09 (ví dụ bảng tra) → Q11 (chi phí bảng tra). IVF-PQ: I04 (thuật toán) → I05 (vết cùng tiêu đề) → I03 (chi phí). Kết luận: C03 → C00 → C04 → C01, C02 → C05; không khái niệm mới.

**Ánh xạ trang mới ↔ chủ đề ghi chú.** P03, P05 → chủ đề mở đầu và bài toán; H14 → chủ đề chi phí HNSW; Q11 → chủ đề bảng tra; I05 → chủ đề truy vấn IVF-PQ; C03, C00, C04 → chủ đề so sánh; C05 → toàn bài. Ghi chú bài giảng không đổi.

### P03 — Tiên quyết và quy ước (thêm 2026-10-14)

- **Loại phần và mục đích:** mở đầu; nêu hai kết quả dùng lại, ký hiệu kho/truy vấn, giải nghĩa HNSW, quy ước đơn vị.
- **Dữ kiện, ký hiệu kế thừa:** LSH (Bài 06); tính cộng theo tọa độ của bình phương Euclid.
- **Thao tác của sinh viên và sản phẩm:** nhận ra ký hiệu $Y,q,K$ và hai công cụ dùng ở ADC, phần dư.
- **Đối tượng trung tâm:** năm dòng nhãn.
- **Kiến thức đầu vào:** Bài 06; tập hợp, véc-tơ.
- **Bằng chứng kiểm:** dùng đúng $\|x-y\|^2$ cộng theo đoạn ở Q08, I02.
- **Kết nối vào–ra:** P00 → P03 → P02.
- **Nguồn:** MMDS Ch.3; Jégou và cộng sự §II-A; Princeton lớp 9 tr.9.
- **Thời lượng:** 1,5 phút.
- **Quyết định:** `thêm`; âm tiết — → 57.

### P04 — Nội dung (thêm 2026-10-14)

- **Loại phần và mục đích:** mở đầu; liệt kê bảy mạch và đọc trước.
- **Dữ kiện, ký hiệu kế thừa:** tên mạch.
- **Thao tác của sinh viên và sản phẩm:** đọc trước ba nguồn.
- **Đối tượng trung tâm:** hai `ol` 1–4, 5–7; dòng Đọc trước.
- **Kiến thức đầu vào:** —.
- **Bằng chứng kiểm:** đọc trước trước buổi học.
- **Kết nối vào–ra:** P02 → P04 → P05.
- **Nguồn:** `sources/reference-slides/README.md` dòng Bài 7.
- **Thời lượng:** 0,5 phút.
- **Quyết định:** `thêm` (tách từ P02); âm tiết — → 51.

### P05 — Vấn đề trung tâm (thêm 2026-10-14)

- **Loại phần và mục đích:** mở đầu; bài toán kho $10^{10}$ véc-tơ và câu trả lời có điều kiện của từng mạch.
- **Dữ kiện, ký hiệu kế thừa:** $N$, $D$ của BIODS.
- **Thao tác của sinh viên và sản phẩm:** đọc sáu dòng như bản đồ bài; đối chiếu ở C04.
- **Đối tượng trung tâm:** Nhu cầu + `ol start="2"`.
- **Kiến thức đầu vào:** P01 sau trang này dùng cùng số.
- **Bằng chứng kiểm:** C04 trả lời đúng thứ tự.
- **Kết nối vào–ra:** P04 → P05 → P01.
- **Nguồn:** BIODS 271 bài 12 tr.17.
- **Thời lượng:** 1,5 phút.
- **Quyết định:** `thêm`; âm tiết — → 60.
- **Sửa sau rà 2026-10-14:** dòng Nhu cầu nêu giới hạn tài nguyên bằng số đã có trong bài (122,88 TB, ≈30,7 giây với $10^{12}$ lượt mỗi giây); dòng cuối nêu ngân sách giả định 6 TB và 10 ms; dòng HNSW nêu giới hạn giao cho mạch 4 ("giữ véc-tơ gốc"); dòng PQ, IVF-PQ dùng "đo"; `ol start="2"` thành `ul`. Âm tiết 60/60, 6 dòng. Ghi chú: phép tính 122,88 TB và 30,7 giây, nguồn gốc của giả định, bỏ câu siêu dữ liệu. Vì P05 đã nêu 30,7 giây, câu hỏi của P01 đổi thành "gấp bao nhiêu lần 10 ms" (lời giải 3072).

### H14 — Chi phí: truy vấn HNSW (thêm 2026-10-14)

- **Loại phần và mục đích:** chi phí; số phép đo và hai giả thiết của kết luận $\log N$.
- **Dữ kiện, ký hiệu kế thừa:** H13 (bộ nhớ), phân phối tầng H08.
- **Thao tác của sinh viên và sản phẩm:** nêu hai giả thiết không được bỏ.
- **Đối tượng trung tâm:** năm dòng: Mô hình, Giả thiết, kết quả, giới hạn, Kết luận.
- **Kiến thức đầu vào:** H08, H13.
- **Bằng chứng kiểm:** C03 hàng "Truy vấn HNSW".
- **Kết nối vào–ra:** H13 → H14 → QT.
- **Nguồn:** Malkov và Yashunin mục 4.2.1, tr.7–8.
- **Thời lượng:** 1,5 phút.
- **Quyết định:** `thêm` (tách từ H13); âm tiết — → 58.

### Q11 — Chi phí: bảng tra và chấm mã (thêm 2026-10-14)

- **Loại phần và mục đích:** chi phí; đếm lập bảng, chấm mã, tính trực tiếp.
- **Dữ kiện, ký hiệu kế thừa:** Q09 (bảng $T$).
- **Thao tác của sinh viên và sản phẩm:** so $m$ lần tra với $D$ lượt tọa độ.
- **Đối tượng trung tâm:** bảng Bước | Số lần | Chi phí mỗi lần | Đóng góp.
- **Kiến thức đầu vào:** Q08, Q09.
- **Bằng chứng kiểm:** Q10, I03 dùng $m$ lần tra mỗi mã.
- **Kết nối vào–ra:** Q09 → Q11 → Q10.
- **Nguồn:** Jégou và cộng sự §III-A; Princeton lớp 8 tr.31–32.
- **Thời lượng:** 1 phút.
- **Quyết định:** `thêm` (tách từ Q09); âm tiết — → 53.

### I05 — Thuật toán: truy vấn IVF-PQ (vết) (thêm 2026-10-14)

- **Loại phần và mục đích:** thuật toán; vết chạy đối chiếu ở trang kế tiếp cùng tiêu đề.
- **Dữ kiện, ký hiệu kế thừa:** I04 (giả mã), I01 (khoảng cách).
- **Thao tác của sinh viên và sản phẩm:** chạy tay $nprobe=2$, trả lời $nprobe=1$.
- **Đối tượng trung tâm:** bảng hai danh sách; hộp Câu hỏi.
- **Kiến thức đầu vào:** I00–I02.
- **Bằng chứng kiểm:** recall@3 $=2/3$ (lời giải trong ghi chú).
- **Kết nối vào–ra:** I04 → I05 → I03.
- **Nguồn:** Jégou và cộng sự §IV-C.
- **Thời lượng:** 1,5 phút.
- **Quyết định:** `thêm` (tách từ I04); âm tiết — → 24.

### C03 — Kết quả và giả thiết không được bỏ (thêm 2026-10-14)

- **Loại phần và mục đích:** tổng kết; bảy kết quả cạnh giả thiết.
- **Dữ kiện, ký hiệu kế thừa:** mọi kết quả mạch 2–5.
- **Thao tác của sinh viên và sản phẩm:** nêu phản ví dụ khi bỏ giả thiết (ghi chú).
- **Đối tượng trung tâm:** bảng ba cột bảy hàng.
- **Kiến thức đầu vào:** mạch 2–5.
- **Bằng chứng kiểm:** C01 câu 2, C02 câu 6.
- **Kết nối vào–ra:** CT → C03 → C00.
- **Nguồn:** hai bài báo gốc.
- **Thời lượng:** 2 phút.
- **Quyết định:** `thêm`; âm tiết — → 80.

### C04 — Câu trả lời cho vấn đề trung tâm (thêm 2026-10-14)

- **Loại phần và mục đích:** tổng kết; trả lời P05 theo đúng thứ tự bằng con số.
- **Dữ kiện, ký hiệu kế thừa:** P05; H13, Q07, Q10, I03, C00.
- **Thao tác của sinh viên và sản phẩm:** đối chiếu sáu mục với con số.
- **Đối tượng trung tâm:** `ol start="2"`.
- **Kiến thức đầu vào:** mạch 2–5.
- **Bằng chứng kiểm:** đúng thứ tự P05.
- **Kết nối vào–ra:** C00 → C04 → C01.
- **Nguồn:** số suy ra từ các trang chi phí; BIODS tr.17.
- **Thời lượng:** 2 phút.
- **Quyết định:** `thêm`; âm tiết — → 65.
- **Sửa sau rà 2026-10-14:** trả lời bằng TB và giây: HNSW ≈125,5 TB vượt 6 TB; PQ quét đủ 5,12 TB vừa bộ nhớ nhưng ≈5,12 giây; IVF-PQ 5,2 TB, ≈3,6 ms; dòng cuối nêu cả hai điều kiện (6 TB, 10 ms, giả định). Dòng 3–5 không chép cột Chi phí của C00. Ghi chú: phép tính từng con số; câu sai "chỉ IVF-PQ trong bốn cấu trúc vừa" thay bằng "PQ quét đủ chiếm 5,12 TB, ít hơn IVF-PQ, nên bị loại vì thời gian chứ không vì bộ nhớ"; HNSW và LSH vượt bộ nhớ. Âm tiết 69/80, 6 dòng.

### C05 — Nguồn và tài liệu đọc (thêm 2026-10-14)

- **Loại phần và mục đích:** tổng kết; nguồn, liên kết ghi chú.
- **Dữ kiện, ký hiệu kế thừa:** —.
- **Thao tác của sinh viên và sản phẩm:** mở ghi chú bài giảng.
- **Đối tượng trung tâm:** ba dòng Nguồn, liên kết viewer.
- **Kiến thức đầu vào:** —.
- **Bằng chứng kiểm:** liên kết viewer mở được.
- **Kết nối vào–ra:** C02 → C05 → RT.
- **Nguồn:** `sources/reference-slides/README.md`; trang đầu các PDF.
- **Thời lượng:** 0,5 phút.
- **Quyết định:** `thêm`; âm tiết — → 50.

## Chi tiết từng trang (duyệt 03/10/2026)

Mỗi mục ghi: tiêu đề hiện tại; phần; mục đích (việc sinh viên làm được); câu chốt; vai trò trong mạch; kiến thức đầu vào; nội dung và cách thể hiện; kết nối vào–ra; kiểm tra và ghi chú; nguồn; thời lượng; quyết định và lý do. Bảng tóm tắt ở trên giữ thời lượng; khi hai nơi khác nhau, mục chi tiết là bản hiện hành.

### P00 — Chỉ mục hàng xóm gần đúng

- **Sửa 2026-10-14:** quyết định `sửa`: câu luận đề của điều phối viên thay dòng phụ; ghi chú mở bằng kết quả Bài 06, viết đủ tên HNSW, bỏ "Bài này". Âm tiết mặt trang 36 → 50. Thời lượng mới: 0,5 phút.

- **Phần:** 1, mở đầu. **Vai trò:** nhận diện bài. **Thời lượng:** 0 phút.
- **Mục đích:** gọi đúng tên ba cấu trúc của bài và quan hệ với Bài 06.
- **Câu chốt:** bài xét truy vấn tìm véc-tơ gần nhất trong kho lớn bằng ba cấu trúc HNSW, PQ, IVF-PQ.
- **Đầu vào:** Bài 06 (LSH tìm cặp tương đồng trong một tập). **Thể hiện:** trang tiêu đề; dòng phụ viết đủ tên ba cấu trúc, PQ có diễn giải.
- **Kết nối vào–ra:** từ bài toán tìm cặp của Bài 06 sang bài toán truy vấn; P01 đưa tình huống dữ liệu.
- **Ghi chú diễn giả:** phân biệt tìm cặp và truy vấn; vai trò của ba cấu trúc; nguồn.
- **Nguồn:** BIODS 271 bài 12 tr.16–18; Princeton COS 597A lớp 8–9; hai bài báo gốc.
- **Quyết định:** sửa nhẹ. Dòng phụ cũ “HNSW, lượng tử hóa tích và IVF-PQ” chưa giải thích PQ; ghi chú cũ gọi PQ là “nén khoảng cách” (PQ nén véc-tơ) và ghi sai mã học phần “COS579A”.

### P01 — Truy hồi ngữ nghĩa trên mười tỷ véc-tơ

- **Sửa 2026-10-14:** quyết định `sửa`: khuôn trang ví dụ: dữ kiện, hình, hai dòng phép tính thay hai thẻ có chữ, hộp Câu hỏi. Âm tiết mặt trang 34 → 40. Tiêu đề hiện hành: “Ví dụ: truy hồi ngữ nghĩa trên mười tỷ véc-tơ”. Thời lượng mới: 3 phút.

- **Phần:** 1, mở đầu. **Vai trò:** tình huống dữ liệu, nêu vấn đề. **Thời lượng:** 4 phút.
- **Mục đích:** mô tả truy hồi ngữ nghĩa thành bài toán tìm véc-tơ gần $q$ và tính dung lượng kho cùng số tọa độ một lượt quét phải xử lý.
- **Câu chốt:** quét toàn kho $10^{10}$ véc-tơ 3072 chiều cho mỗi truy vấn tốn $3{,}07\cdot10^{13}$ lượt xử lý tọa độ trên 122,88 TB dữ liệu.
- **Đầu vào:** véc-tơ, khoảng cách (Bài 05–06). **Thể hiện:** hình `truy-hoi-ngu-nghia.svg` (đoạn văn và câu truy vấn qua cùng mô hình nhúng → kho véc-tơ và $q$ → $K$ đoạn gần nhất); hai thẻ số; hộp câu hỏi.
- **Kết nối vào–ra:** nhận bài toán truy vấn từ P00; giao $N$, $D$ và chi phí quét cho A00 (hình thức hóa $\Theta(ND)$), Q07 và Q10 (bộ nhớ mã PQ), C00 (thu hồi tình huống).
- **Kiểm tra:** thời gian một lượt quét với giả định $10^{12}$ tọa độ/giây; đáp án 30,7 giây trong ghi chú, ghi rõ tốc độ là giả định.
- **Nguồn:** BIODS 271 bài 12 tr.16 (quy trình truy hồi dày đặc), tr.17 (cấu hình $N$, $D$, 32 bit).
- **Quyết định:** sửa. Hình cũ `quy-mo-vector.svg` đưa mã PQ, 512 đoạn, 8 bit và 5,12 TB trước khi PQ được định nghĩa; câu hỏi cũ giả định sẵn khái niệm “mã”; chưa giải thích véc-tơ từ đâu ra; thiếu chi phí quét. Hình cũ được giữ trong ghi chú tự học ở mục PQ, chờ quyết định ở Q07/Q10.

### P02 — Nội dung và mục tiêu

- **Sửa 2026-10-14:** quyết định `tách`: trang gộp mục tiêu và Nội dung 86 > 80; giữ ba mục tiêu nguyên chữ (quyết định 4); ánh xạ mục tiêu → bằng chứng trong ghi chú. Âm tiết mặt trang 86 → 47. Tiêu đề hiện hành: “Mục tiêu học tập”. Thời lượng mới: 1 phút.

- **Phần:** 1, mở đầu. **Vai trò:** định hướng. **Thời lượng:** 2 phút.
- **Mục đích:** nêu được thứ tự sáu phần và ba việc phải làm được sau buổi học.
- **Câu chốt:** đồ thị giảm số véc-tơ phải đo, PQ giảm chi phí mỗi phép đo, IVF-PQ ghép hai cách; ba mục tiêu là đặc tả và đo, chạy tay, tính chi phí và chọn chỉ mục.
- **Đầu vào:** tình huống P01. **Thể hiện:** bố cục `agenda-slide` như Bài 06: danh sách phần bên trái, ba mục tiêu đánh số bên phải.
- **Kết nối vào–ra:** nhận bài toán truy vấn từ P01; mở phần 2 (A00).
- **Ghi chú diễn giả:** vai trò từng phần; mục tiêu nào được kiểm ở phần nào.
- **Nguồn:** `sources/source.md` (LLO1 Bài 7). **Quyết định:** viết lại. Ba thẻ cũ “Đặc tả / Giải thích / Lựa chọn” không có dàn bài; “chạy tay tìm kiếm” chưa nói tìm trên cấu trúc nào; “PQ đầy đủ”, “bốn trục” dùng trước khi định nghĩa.

### A00 — Bài toán $K$ hàng xóm gần nhất

- **Sửa 2026-10-14:** quyết định `sửa`: hai thẻ có câu và câu kết thành bốn dòng Nhu cầu, Đầu vào, Đầu ra (tìm đúng, tìm gần đúng); ANN giải nghĩa. Âm tiết mặt trang 76 → 56. Thời lượng mới: 3,5 phút.

- **Phần:** 2, bài toán và phép đo (khái niệm/mô hình). **Vai trò:** hình thức hóa. **Thời lượng:** 4 phút.
- **Mục đích:** viết đặc tả tìm đúng và tìm gần đúng, tính chi phí quét đầy đủ.
- **Câu chốt:** tìm đúng cần $\Theta(ND)$; tìm gần đúng trả $K$ điểm có thể thiếu hàng xóm thật để chỉ đo một phần kho.
- **Đầu vào:** $N=10^{10}$, $D=3072$ (nhắc lại số, không dẫn chiếu trang trước); khoảng cách Euclid. **Thể hiện:** dòng đầu vào; hai thẻ song song “Tìm đúng”, “Tìm gần đúng (ANN)”; dòng chi phí thay số.
- **Kết nối vào–ra:** hình thức hóa tình huống P01; giao $N_K(q)$ và $\widehat N_K(q)$ cho A01 (độ thu hồi).
- **Ghi chú diễn giả:** ý nghĩa phá hòa; mô hình chi phí đếm tọa độ; HNSW dùng khoảng cách tổng quát, PQ dùng Euclid bình phương; nguồn.
- **Nguồn:** Malkov–Yashunin tr.1 (K-NNS, K-ANNS “cho phép một số ít sai sót”); Jégou–Douze–Schmid tr.1.
- **Quyết định:** sửa. Tiêu đề cũ “Từ tìm đúng sang tìm gần đúng” là câu kể tiến trình; mặt trang cũ chỉ đặc tả tìm đúng, khái niệm gần đúng nằm trong ghi chú; chi phí chưa thay số quy mô.

### A01 — Độ thu hồi tại $K$

- **Sửa 2026-10-14:** quyết định `sửa`: định nghĩa bằng "là", "độ thu hồi (recall)"; dòng Ví dụ.. Âm tiết mặt trang 26 → 33. Thời lượng mới: 3 phút.

- **Phần:** 2. **Vai trò:** định nghĩa, ví dụ, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** tính $\operatorname{recall@K}$ từ tập đúng và tập trả về.
- **Câu chốt:** độ thu hồi là tỷ lệ hàng xóm thật tìm lại được trong $K$ kết quả.
- **Đầu vào:** $N_K(q)$, $\widehat N_K(q)$ từ A00. **Thể hiện:** hình `do-thu-hoi.svg` (hai tập năm phần tử, nét liền/nét đứt) bên trái; công thức, phép thay số và hộp câu hỏi bên phải.
- **Kết nối vào–ra:** đo chất lượng của tập gần đúng ở A00; trục “chất lượng” của A02.
- **Kiểm tra:** chỉ mục trả $\{a,c,f,g,h\}$; đáp án $2/5$ trong ghi chú.
- **Nguồn:** Malkov–Yashunin tr.1; PQ paper tr.7 (quy ước recall@R khác, chỉ ghi ở ghi chú).
- **Quyết định:** sửa. Tiêu đề cũ là câu dài; hình cũ `ann-recall.svg` chữ quá nhỏ khi chiếu; phép tính $3/5$ chỉ có trong hình; chưa có câu hỏi.

### A02 — Bốn trục đánh giá chỉ mục

- **Sửa 2026-10-14:** quyết định `sửa`: rút ô bảng; ngoại lệ trần 80 (bảng so sánh). Âm tiết mặt trang 79 → 77. Thời lượng mới: 2 phút.

- **Phần:** 2. **Vai trò:** khung đánh giá, kiểm tra. **Thời lượng:** 2 phút.
- **Mục đích:** nêu bốn trục và điều kiện phải giữ cố định; giải thích vì sao một số đo đơn lẻ không xếp hạng được chỉ mục.
- **Câu chốt:** chỉ mục gần đúng đánh đổi chất lượng lấy thời gian và bộ nhớ, nên phải đo đủ bốn trục trong cùng điều kiện.
- **Đầu vào:** $\operatorname{recall@K}$ (A01). **Thể hiện:** bảng ba cột; hộp câu hỏi A/B.
- **Kết nối vào–ra:** dùng độ thu hồi của A01; bốn trục được dùng lại ở H12–H13, Q10, I03 và bảng so sánh C00.
- **Kiểm tra:** A ($0{,}9$; 5 ms) và B ($0{,}7$; 2 ms); đáp án: chưa xếp hạng được khi chưa có yêu cầu.
- **Nguồn:** Princeton COS 597A lớp 8 tr.2–5; lớp 9 tr.2.
- **Quyết định:** sửa. Tiêu đề cũ “Bốn trục phải đo cùng nhau” mang giọng mệnh lệnh; cột điều kiện có “thứ tự chèn” của HNSW khi HNSW chưa được giới thiệu; lý do cần bốn trục chỉ nằm trong ghi chú.

### A03 — Hai cách giảm chi phí truy vấn

- **Sửa 2026-10-14:** quyết định `sửa`: dòng Mô hình và bảng bốn cấu trúc thay hai thẻ có câu và câu kết. Âm tiết mặt trang 75 → 57. Thời lượng mới: 2 phút.

- **Phần:** 2 (kết phần). **Vai trò:** trực giác, bản đồ cơ chế. **Thời lượng:** 2 phút.
- **Mục đích:** chỉ ra mỗi cấu trúc giảm thừa số nào của chi phí truy vấn.
- **Câu chốt:** LSH và HNSW giảm số véc-tơ được đo; PQ giảm chi phí một phép đo và bộ nhớ; IVF-PQ giảm cả hai.
- **Đầu vào:** $\Theta(ND)$ (A00), LSH (Bài 06). **Thể hiện:** đẳng thức chữ chi phí ≈ (số véc-tơ được đo) × (chi phí một phép đo); hai thẻ theo hai thừa số; câu chốt IVF-PQ.
- **Kết nối vào–ra:** kết phần 2; mở phần 3 (HNSW giảm thừa số thứ nhất), phần 4 (PQ giảm thừa số thứ hai), phần 5 (IVF-PQ).
- **Ghi chú diễn giả:** LSH cho truy vấn; giới hạn của từng hướng; LSH không giảng lại.
- **Nguồn:** MMDS Ch.3; Princeton lớp 9 tr.4 (LSH cho truy vấn), tr.5 (phân cụm kèm PQ), tr.7 (đồ thị); lớp 8 tr.2.
- **Quyết định:** viết lại. Tiêu đề cũ “LSH tạo ngăn, HNSW tạo đường, PQ tạo mã” là khẩu hiệu; ba thẻ đưa tên HNSW, PQ mà không nối với chi phí $\Theta(ND)$ vừa tính nên khái niệm xuất hiện đột ngột.

### H00 — Đồ thị lân cận

- **Sửa 2026-10-14:** quyết định `sửa`: dòng Nhu cầu; định nghĩa bằng "là"; gạch "Tìm" và câu kết sang ghi chú. Âm tiết mặt trang 56 → 48. Thời lượng mới: 1 phút.

- **Phần:** 3, tìm kiếm trên đồ thị HNSW (thuật toán). **Vai trò:** mở phần, trực giác. **Thời lượng:** 2 phút.
- **Mục đích:** mô tả đồ thị lân cận (đỉnh, cạnh, điểm vào, dữ liệu lưu) và ý tưởng tìm bằng cách đi tới đỉnh gần $q$ hơn.
- **Câu chốt:** chỉ các đỉnh trên đường đi được đo, nên đồ thị giảm thừa số “số véc-tơ được đo” của A03.
- **Đầu vào:** hai thừa số chi phí (A03). **Thể hiện:** hình `do-thi-vi-du.svg` (tọa độ thật; khoảng cách tới $q$: e 9, a 7, b 5, s 8, t 4, u 2, z 1; cạnh e–a, a–b, e–s, s–t, t–u, u–z) và ba gạch đầu dòng.
- **Kết nối vào–ra:** nhận thừa số thứ nhất từ A03; giao đồ thị ví dụ cho H01–H06 (mỗi trang vẽ lại hình, không dẫn chiếu trang trước).
- **Ghi chú diễn giả:** hướng cạnh, tỷ lệ hình; bộ nhớ $N\cdot(\text{véc-tơ}+4\ \text{byte}\times\text{bậc})$; đồ thị do học phần dựng.
- **Nguồn:** Princeton lớp 9 tr.7 (cấu trúc dữ liệu), tr.8 (tìm tham lam); Malkov–Yashunin tr.2.
- **Quyết định:** viết lại. Bản cũ không có hình; thẻ “Trạng thái: đỉnh đã thăm, ứng viên chưa mở…” đưa trạng thái của SEARCH-LAYER trước cả thuật toán tham lam (khái niệm đột ngột, rà phần 1–2 cũng nêu); không nối với A03.

### H01 — Tìm kiếm tham lam (gộp H02 cũ)

- **Sửa 2026-10-14:** quyết định `sửa`: tách dòng 29 âm tiết; dòng Ký hiệu; Kết luận có nhãn. Âm tiết mặt trang 49 → 40. Thời lượng mới: 4 phút.

- **Phần:** 3. **Vai trò:** ví dụ chạy tay, nêu giới hạn. **Thời lượng:** 4 phút.
- **Mục đích:** chạy tay tham lam trên đồ thị ví dụ và giải thích vì sao điểm dừng chỉ là cực tiểu cục bộ.
- **Câu chốt:** tham lam dừng ở cực tiểu cục bộ $b:5$ vì không quay lui; $z:1$ nằm trên nhánh $s$ đã bị bỏ ở bước đầu.
- **Đầu vào:** đồ thị lân cận (H00), vẽ lại trên trang bằng `do-thi-tham-lam.svg`. **Thể hiện:** câu quy tắc một bước; hình (đường e→a→b tô cam, đỉnh b viền cam) cạnh bảng vết ba hàng; câu chốt định nghĩa cực tiểu cục bộ.
- **Kết nối vào–ra:** dùng đồ thị H00; tạo nhu cầu giữ nhánh dự phòng cho H03 (tìm kiếm chùm).
- **Ghi chú diễn giả:** định nghĩa cực tiểu cục bộ; vì sao điều kiện dừng không bảo đảm toàn cục; dừng do khoảng cách giảm nghiêm ngặt; 4 phép đo.
- **Nguồn:** Princeton lớp 9 tr.8 (tham lam, cực tiểu cục bộ, không quay lui), tr.11–13.
- **Quyết định:** gộp. H01 cũ (hình + một câu) và H02 cũ (bảng vết) cùng một luận điểm; tách hai trang buộc H02 dựa vào hình ở trang trước. Bảng cũ ghi lân cận của $a$ chỉ là $b:5$, thiếu $e:9$; bảng mới liệt kê đủ. Hình cũ `greedy-beam.svg` (vị trí không theo tỷ lệ khoảng cách, gộp hai thuật toán trong một hình) được thay bằng hai biến thể của đồ thị ví dụ.

### H03 — Tìm kiếm chùm

- **Sửa 2026-10-14:** quyết định `sửa`: dòng Nhu cầu; cặp "tương tự … nhưng …"; "tìm kiếm chùm (beam search)"; quy tắc thêm/bỏ sang ghi chú. Âm tiết mặt trang 75 → 53. Thời lượng mới: 2 phút.

- **Phần:** 3. **Vai trò:** trực giác và ví dụ chạy tay trước khi hình thức hóa. **Thời lượng:** 4 phút.
- **Mục đích:** chạy tay tìm kiếm chùm, theo dõi $C$ và $W$, giải thích vì sao giữ nhánh dự phòng giúp thoát cực tiểu cục bộ.
- **Câu chốt:** $s$ còn trong $C$ khi nhánh $b$ hết lân cận mới, nên tìm kiếm chùm $ef=3$ đi tiếp tới $z$; $ef=1$ trùng tham lam.
- **Đầu vào:** đồ thị ví dụ, vẽ lại bằng `do-thi-chum.svg`; khái niệm cực tiểu cục bộ (H01). **Thể hiện:** dòng định nghĩa $C$, $W$, $ef$; hình cạnh bảng vết 7 hàng (lớp `ann-compact`); hộp câu hỏi.
- **Kết nối vào–ra:** giải quyết giới hạn của H01; giao vết $C$, $W$ cho đặc tả H04, giả mã H05 và bất biến H06.
- **Kiểm tra:** $ef=2$; đáp án: dừng khi đỉnh kế tiếp $s{:}8$ xa hơn $a{:}7$, trả $\{b,a\}$ (mô phỏng lại theo Thuật toán 2).
- **Nguồn:** Princeton lớp 9 tr.9; Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Bản cũ dùng $C$, $W$, “hàng đợi” trước khi định nghĩa; không có hình; vết dừng ở $s$, phần còn lại chỉ ở ghi chú; câu chốt dài hai dòng.

### H04 — Đặc tả SEARCH-LAYER

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Thuật toán: SEARCH-LAYER"; "Trạng thái:" thành "Ký hiệu:". Âm tiết mặt trang 38 → 43. Tiêu đề hiện hành: “Thuật toán: SEARCH-LAYER”. Thời lượng mới: 2 phút.

- **Phần:** 3. **Vai trò:** hình thức hóa. **Thời lượng:** 2 phút.
- **Mục đích:** nêu đầu vào, đầu ra, điều kiện trước và ba tập trạng thái của `SEARCH-LAYER`; nhận ra tìm kiếm chùm vừa chạy là một lời gọi của nó.
- **Câu chốt:** `SEARCH-LAYER` trả tối đa $ef$ đỉnh gần $q$ nhất trong các đỉnh đã thấy, không phải trong toàn tầng.
- **Đầu vào:** vết chùm $ef=3$ (H03), nhắc lại bằng hình `search-layer-trang-thai.svg` (V = {e, a, b, s}, C = {s}, W = {b, a, s}). **Thể hiện:** hình bên trái; ba dòng đầu vào/đầu ra/trạng thái bên phải.
- **Kết nối vào–ra:** hình thức hóa H03; giao đặc tả cho giả mã H05 và bất biến H06; tham số $\ell_c$ được dùng lại khi có nhiều tầng (H07–H10).
- **Ghi chú diễn giả:** $\ell_c=0$ khi chỉ có một đồ thị; vì sao $1\le|ep|\le ef$; đầu ra chỉ về đỉnh đã thấy; đọc hình.
- **Nguồn:** Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Tiêu đề cũ “Hợp đồng của SEARCH-LAYER” dịch sát “contract”, học phần dùng “đặc tả”; “tầng hữu hạn $\ell_c$” xuất hiện trước khái niệm tầng mà không giải thích; hình cũ `search-layer.svg` chữ nhỏ, không gắn với ví dụ; $V$ xuất hiện lần đầu không định nghĩa.

### H05 — Giả mã SEARCH-LAYER

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Thuật toán: SEARCH-LAYER"; takeaway thành "Ví dụ."; ghi chú đọc giả mã. Âm tiết mặt trang 8 → 8. Tiêu đề hiện hành: “Thuật toán: SEARCH-LAYER”. Thời lượng mới: 3,5 phút.

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 4 phút.
- **Mục đích:** đọc giả mã, chỉ ra dòng khởi tạo, điều kiện dừng, điều kiện chấp nhận và vì sao tính lại ngưỡng $f$.
- **Câu chốt:** $f$ là ngưỡng chấp nhận và phải tính lại sau mỗi thay đổi của $W$; ở ví dụ ngưỡng đổi từ $s{:}8$ sang $a{:}7$ khi mở $s$.
- **Đầu vào:** đặc tả và ba tập (H04). **Thể hiện:** một khối giả mã 13 dòng (`data-trim`); câu chốt nối một bước của ví dụ với dòng tính lại $f$ (nhắc lại $W=\{b,a,s\}$ bằng giá trị, không dẫn chiếu trang).
- **Kết nối vào–ra:** cài đặt đặc tả H04; giao các dòng giả mã cho bất biến H06 và cho lời gọi trong truy vấn H09, chèn H10.
- **Ghi chú diễn giả:** vì sao tính lại $f$; lập luận khi `break` mọi đỉnh của $W$ đã mở; dừng ở đó là đánh đổi; tính dừng.
- **Nguồn:** Malkov–Yashunin Thuật toán 2 tr.4.
- **Quyết định:** sửa. Tiêu đề cũ “SEARCH-LAYER cập nhật ngưỡng sau mỗi điểm” là câu mô tả; giả mã cũ dùng tên `hàng_đợi_gần_nhất`, `lân_cận` và dồn hai thao tác vào một dòng; không có liên hệ với ví dụ.

### H06 — Bất biến của SEARCH-LAYER

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Tính đúng: …"; Bất biến, Điều kiện dừng có nhãn; Ví dụ.. Âm tiết mặt trang 39 → 54. Tiêu đề hiện hành: “Tính đúng: SEARCH-LAYER”. Thời lượng mới: 3 phút.

- **Phần:** 3. **Vai trò:** lập luận đúng và giới hạn. **Thời lượng:** 3 phút.
- **Mục đích:** phát biểu bất biến, chứng minh bằng khởi tạo–duy trì–khi dừng, và chỉ ra kết luận chỉ đúng trên tập đỉnh đã thấy.
- **Câu chốt:** $W$ luôn là $\min(ef,|V|)$ đỉnh gần $q$ nhất trong $V$; đỉnh ngoài $V$ không được bảo đảm.
- **Đầu vào:** giả mã H05; câu hỏi $ef=2$ ở H03, nhắc lại bằng hình `do-thi-ef2.svg` (đỉnh đã thấy tô xanh, đỉnh chưa thấy viền đứt, $W$ viền kép). **Thể hiện:** mệnh đề ở dòng đầu; hình bên trái, bảng ba hàng bên phải; câu chốt ví dụ.
- **Kết nối vào–ra:** chứng minh tính đúng của H05; giới hạn “ngoài $V$” tạo nhu cầu điểm vào tốt (H07).
- **Ghi chú diễn giả:** chứng minh bước duy trì; xử lý hòa; ví dụ $ef=2$; tính dừng; trường hợp xấu.
- **Nguồn:** suy ra từ Thuật toán 2, Malkov–Yashunin tr.4; bất biến kiểm bằng chương trình trên đồ thị ví dụ và 3000 đồ thị ngẫu nhiên.
- **Quyết định:** sửa. Bản cũ chỉ liệt kê tính chất của $V$, $C$, $W$, thiếu khởi tạo–duy trì–kết luận (tiêu chuẩn mục 3); phát biểu về $W$ yếu (“trong số đỉnh đã được chấp nhận”); ví dụ chỉ ở ghi chú và dẫn chiếu “ví dụ tìm kiếm chùm”.

### H06B — Cạnh dài rút ngắn đường đi (trang mới)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Ví dụ: …"; dòng Nhu cầu; tách dòng 24, 23; rút ghi chú. Âm tiết mặt trang 47 → 34. Tiêu đề hiện hành: “Ví dụ: cạnh dài trên mười hai điểm thẳng hàng”. Thời lượng mới: 2 phút.

- **Phần:** 3. **Vai trò:** nêu vấn đề và trực giác cho cấu trúc nhiều tầng. **Thời lượng:** 2 phút.
- **Mục đích:** chạy tham lam trên ví dụ một chiều có và không có cạnh dài; giải thích vì sao HNSW tách cạnh theo thang độ dài.
- **Câu chốt:** cạnh dài đưa tìm kiếm tới gần $q$ nhanh, cạnh ngắn tinh chỉnh; HNSW đặt hai loại cạnh vào các tầng khác nhau.
- **Đầu vào:** tìm kiếm tham lam (H01). **Thể hiện:** hình `canh-dai-mot-chieu.svg` (hai dãy 12 điểm, $q$ ở tọa độ 6,4; đường tham lam tô cam: 6 bước và 3 bước); câu chốt.
- **Kết nối vào–ra:** sau khi đã có tìm kiếm trên một tầng (H01–H06), nêu giới hạn còn lại là số bước; tạo nhu cầu cho cấu trúc nhiều tầng H07.
- **Ghi chú diễn giả:** khoảng $N$ bước khi chỉ có cạnh ngắn; ý tưởng skip list; cạnh dài phải đặt đúng chỗ (chỉ có $p4$–$p8$ vẫn 6 bước); “zoom-out/zoom-in” của bài báo.
- **Nguồn:** Princeton lớp 9 tr.11–13; Malkov–Yashunin mục 3 tr.3. Ví dụ dựng lại, vết tính lại bằng chương trình.
- **Quyết định:** thêm. Bản cũ chuyển từ bất biến một tầng sang “điểm vào truyền từ tầng cao xuống thấp” mà không nêu vì sao cần nhiều tầng; khái niệm tầng xuất hiện đột ngột.

### H07 — Đồ thị nhiều tầng

- **Sửa 2026-10-14:** quyết định `sửa`: tách dòng 21 thành bốn gạch; câu cạnh dài/ngắn sang ghi chú. Âm tiết mặt trang 37 → 45. Thời lượng mới: 2,5 phút.

- **Phần:** 3. **Vai trò:** mô hình cấu trúc và trực giác truy vấn. **Thời lượng:** 3 phút.
- **Mục đích:** mô tả tập điểm của từng tầng và lần theo truy vấn từ tầng cao xuống tầng 0.
- **Câu chốt:** tầng trên dùng $ef=1$ để đưa điểm vào tới gần $q$; tầng 0 dùng chùm $efSearch$.
- **Đầu vào:** ví dụ một chiều và ý tưởng cạnh dài (H06B), SEARCH-LAYER (H04–H05). **Thể hiện:** hình `do-thi-nhieu-tang.svg` (ba tầng trên cùng 12 điểm, đường cam, mũi tên xuống tại $p8$ và $p6$; vết tính lại bằng chương trình); hai gạch đầu dòng.
- **Kết nối vào–ra:** hiện thực ý tưởng H06B; giao cấu trúc cho giả mã truy vấn H09 và quy tắc rút tầng H08.
- **Ghi chú diễn giả:** điểm có tầng $\ell$ thuộc tầng $0..\ell$; vì sao $ef=1$ ở tầng trên; vết có số khoảng cách; tầng do học phần chọn, HNSW rút ngẫu nhiên.
- **Nguồn:** Malkov–Yashunin Hình 1, mục 3 tr.3; Princeton lớp 9 tr.17.
- **Quyết định:** sửa. Tiêu đề cũ “Điểm vào truyền từ tầng cao xuống thấp” là câu mô tả; hình cũ `hnsw-layers.svg` chữ nhỏ, không gắn với ví dụ; chuỗi $ep_2\to ep_1\to ep_0$ dùng ký hiệu chưa giải thích; trang không nói tầng nào chứa điểm nào.

### H08 — Rút ngẫu nhiên tầng của điểm mới (chuyển sau H09)

- **Sửa 2026-10-14:** quyết định `sửa`: khuôn trang kết quả: Nhu cầu, Mệnh đề., Chứng minh., Ý nghĩa:, Ví dụ.; bỏ hai thẻ có câu. Âm tiết mặt trang 36 → 53. Thời lượng mới: 3 phút.

- **Phần:** 3. **Vai trò:** hình thức hóa và suy luận xác suất. **Thời lượng:** 3 phút.
- **Mục đích:** tính $\Pr[\ell\ge k]$ từ công thức rút tầng và giải thích vì sao tầng trên thưa dần, số tầng tăng theo $\log N$.
- **Câu chốt:** mỗi tầng giữ khoảng tỷ lệ $p=e^{-1/m_L}$ số điểm của tầng dưới; tầng cao nhất xấp xỉ $\log_{1/p}N$.
- **Đầu vào:** cấu trúc tầng (H07), truy vấn đi qua các tầng (H09); xác suất cơ bản. **Thể hiện:** công thức; dòng suy luận; hai thẻ “Ý nghĩa” và “Ví dụ $m_L=1/\ln16$”; câu chốt thay số $N=10^{10}$.
- **Kết nối vào–ra:** cho biết tập điểm mỗi tầng hình thành thế nào (bổ sung H07); giao $\ell$ cho thao tác chèn H10.
- **Ghi chú diễn giả:** từng bước suy luận; phân phối hình học như skip list; $m_L=1/\ln M$ của bài báo với $M$ định nghĩa ở H10; số liệu mô phỏng.
- **Nguồn:** Malkov–Yashunin Thuật toán 1 dòng 4 tr.4; mục 3 tr.3; mục 4.1 tr.5.
- **Quyết định:** sửa và chuyển vị trí. Bản cũ chỉ có công thức và bảng ký hiệu, không cho thấy công thức sinh phân phối nào; ghi chú dùng $M$ chưa định nghĩa và dẫn chiếu “trang sau”. Rút tầng chỉ dùng khi chèn nên đặt sau giả mã truy vấn, ngay trước H10.

### H09 — Giả mã truy vấn HNSW

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Thuật toán: …"; Đầu vào/Đầu ra hai dòng; "Ví dụ." thay ex-note. Âm tiết mặt trang 26 → 26. Tiêu đề hiện hành: “Thuật toán: truy vấn HNSW”. Thời lượng mới: 3 phút.

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 3 phút.
- **Mục đích:** đọc giả mã truy vấn; chỉ ra lời gọi $ef=1$ ở tầng trên và $efSearch$ ở tầng 0; nêu điều kiện $efSearch\ge K$.
- **Câu chốt:** truy vấn là chuỗi lời gọi SEARCH-LAYER: tham lam ở tầng trên để có điểm vào, chùm $efSearch$ ở tầng 0 để có $K$ kết quả.
- **Đầu vào:** SEARCH-LAYER (H04–H06), cấu trúc tầng (H07), nhắc lại bằng hình `do-thi-nhieu-tang-gon.svg`. **Thể hiện:** dòng đầu vào/đầu ra; giả mã 6 dòng bên trái; hình gọn và dòng vết bên phải.
- **Kết nối vào–ra:** hình thức hóa H07; lời gọi tương tự được dùng trong pha chèn H10; $efSearch$ là núm điều khiển ở H12.
- **Ghi chú diễn giả:** dữ kiện ví dụ; $ef=1$ là tham lam; trả ít hơn $K$ khi đồ thị tới được nhỏ; tính dừng; kết quả gần đúng theo bất biến.
- **Nguồn:** Malkov–Yashunin Thuật toán 5 tr.5.
- **Quyết định:** sửa. Tiêu đề cũ “Truy vấn HNSW dùng hai chế độ” mơ hồ; giả mã cũ dùng tên `điểm_vào`, `phần_tử_gần_nhất`; thiếu đầu vào/đầu ra trên mặt trang; không nối với ví dụ.

### H10 — Chèn một điểm mới (tách từ H10 cũ)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Ví dụ: …"; dòng dữ kiện rút; Kết luận có nhãn. Âm tiết mặt trang 46 → 36. Tiêu đề hiện hành: “Ví dụ: chèn điểm $x=2{,}6$ vào đồ thị ba tầng”. Thời lượng mới: 3 phút.

- **Phần:** 3. **Vai trò:** ví dụ chạy tay trước giả mã. **Thời lượng:** 3 phút.
- **Mục đích:** chạy tay chèn một điểm qua hai pha trên đồ thị ba tầng.
- **Câu chốt:** chèn là truy vấn chính $x$, rồi nối $x$ với các đỉnh gần nó ở từng tầng $\le\ell$.
- **Đầu vào:** đồ thị ba tầng (H07), truy vấn (H09), tầng $\ell$ (H08). **Thể hiện:** dòng dữ kiện; hình `chen-vi-du.svg` (pha 1 cam, cạnh mới xanh đứt) cạnh bảng ba tầng; câu chốt.
- **Kết nối vào–ra:** dùng truy vấn và rút tầng; giao vết cho giả mã H10B và cho câu hỏi chọn lân cận ở H11.
- **Ghi chú diễn giả:** dữ kiện đồ thị, khoảng cách tới $x$; vai trò hai pha; bậc sau khi nối và vì sao không cắt.
- **Nguồn:** Malkov–Yashunin Thuật toán 1–3; vết mô phỏng lại bằng chương trình.

### H10B — Giả mã chèn HNSW (tách từ H10 cũ)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Thuật toán: …"; Đầu vào/Đầu ra; định nghĩa tham số sang ghi chú. Âm tiết mặt trang 19 → 15. Tiêu đề hiện hành: “Thuật toán: chèn HNSW”. Thời lượng mới: 3 phút.

- **Phần:** 3. **Vai trò:** thuật toán. **Thời lượng:** 3 phút.
- **Mục đích:** đọc giả mã chèn và gọi đúng tên, vai trò của $M$, $efConstruction$, $M_{max}$, $M_{max,0}$.
- **Câu chốt:** pha 1 chỉ tìm điểm vào ở tầng cao hơn $\ell$; pha 2 tìm, chọn $M$ lân cận, nối hai chiều và cắt bậc ở tầng $\le\ell$.
- **Đầu vào:** ví dụ H10. **Thể hiện:** khối giả mã 10 dòng có chú thích pha; một dòng định nghĩa tham số.
- **Kết nối vào–ra:** hình thức hóa H10; dòng “chọn $M$ lân cận” được cụ thể hóa ở H11; các tham số dùng ở H12–H13.
- **Ghi chú diễn giả:** chỉ mục rỗng; mất đối xứng sau cắt; Thuật toán 3 và 4; ràng buộc tham số; $M_{max,0}=2M$ theo mục 4.1.
- **Nguồn:** Malkov–Yashunin Thuật toán 1 tr.4; mục 4.1 tr.5–6.
- **Quyết định (H10 cũ):** tách. Bản cũ có tiêu đề câu mô tả, hình bốn hộp chữ rất nhỏ, một dòng đưa cùng lúc bốn tham số mới; ghi chú diễn giả dài, chứa toàn bộ thuật toán. Ví dụ đặt trước giả mã theo chu trình học.

### H11 — Chọn lân cận đa dạng

- **Sửa 2026-10-14:** quyết định `sửa`: thêm Nhu cầu. Âm tiết mặt trang 22 → 36. Thời lượng mới: 2,5 phút.

- **Phần:** 3. **Vai trò:** cơ chế, ví dụ chạy tay. **Thời lượng:** 3 phút.
- **Mục đích:** áp dụng quy tắc đa dạng để chọn $M$ lân cận và so sánh với chọn gần nhất.
- **Câu chốt:** ứng viên gần một lân cận đã chọn hơn gần $x$ bị loại, nên các cạnh được chọn trải ra nhiều hướng.
- **Đầu vào:** dòng “chọn $M$ lân cận” của giả mã chèn (H10B). **Thể hiện:** dòng quy tắc; hình hai khung `lan-can-da-dang.svg`; bảng quyết định bốn ứng viên.
- **Kết nối vào–ra:** cụ thể hóa H10B; $M$ là núm điều khiển ở H12.
- **Ghi chú diễn giả:** tọa độ ví dụ và lý do đổi sang ví dụ hai chiều; ý nghĩa hình học; hai tùy chọn của Thuật toán 4 nằm ngoài phạm vi; dùng cả khi cắt bậc.
- **Nguồn:** Malkov–Yashunin mục 3, Thuật toán 4 tr.4–5; Princeton lớp 9 tr.18. Phép tính kiểm bằng chương trình.
- **Quyết định:** sửa. Bản cũ dùng $q$ cho điểm mới (xung đột với $q$ là truy vấn); không có hình hay ví dụ; “hướng thoát” là ẩn dụ chưa gắn đối tượng; tiêu đề câu dài.

### H12 — Ba tham số của HNSW

- **Sửa 2026-10-14:** quyết định `sửa`: rút ô; ngoại lệ trần 80 (bảng so sánh). Âm tiết mặt trang 71 → 69. Thời lượng mới: 2 phút.

- **Phần:** 3. **Vai trò:** ứng dụng, kiểm tra. **Thời lượng:** 2 phút.
- **Mục đích:** gọi đúng tham số dùng khi chèn và khi truy vấn; chọn tham số để giảm độ trễ không xây lại.
- **Câu chốt:** $M$ và $efConstruction$ cố định khi xây; $efSearch$ đổi theo truy vấn và đánh đổi độ trễ với độ thu hồi.
- **Đầu vào:** giả mã truy vấn (H09) và chèn (H10B). **Thể hiện:** bảng ba cột; hộp câu hỏi.
- **Kết nối vào–ra:** tổng hợp tham số của H09–H11; giao $M$ cho chi phí bộ nhớ H13 và cho bảng so sánh C00.
- **Kiểm tra:** giảm $efSearch$ (giữ $\ge K$); mất độ thu hồi. Đáp án trong ghi chú.
- **Nguồn:** Malkov–Yashunin mục 4.1 tr.5–6, mục 4.2.3 tr.8; Princeton lớp 9 tr.19.
- **Quyết định:** sửa. Tiêu đề cũ “Ba núm điều khiển ba loại chi phí” dùng ẩn dụ; bảng không nói tham số dùng lúc xây hay lúc truy vấn; thiếu câu hỏi kiểm tra cho phần HNSW.

### H13 — Chi phí của HNSW

- **Sửa 2026-10-14:** quyết định `tách`: 83 âm tiết, dòng 40; giữ bộ nhớ ở H13, chuyển truy vấn sang H14; "Giả định:" thành "Giả thiết:"; một câu kết luận. Âm tiết mặt trang 83 → 50. Tiêu đề hiện hành: “Chi phí: bộ nhớ HNSW”. Thời lượng mới: 1,5 phút.

- **Phần:** 3 (kết phần). **Vai trò:** chi phí, giới hạn, câu nối. **Thời lượng:** 3 phút.
- **Mục đích:** tính bộ nhớ của HNSW cho tình huống mở đầu, tách phần véc-tơ và phần cạnh; nêu điều kiện của kết luận $\log N$.
- **Câu chốt:** HNSW giảm số phép đo nhưng vẫn giữ 122,88 TB véc-tơ gốc, khoảng 98% bộ nhớ.
- **Đầu vào:** $N$, $D$ (P01, nhắc lại bằng số), $M_{max}$, $M_{max,0}$ (H10B), $p$ (H08). **Thể hiện:** dòng giả định; bảng hai thành phần (mỗi điểm, toàn kho); dòng chi phí truy vấn; câu chốt.
- **Kết nối vào–ra:** kết phần 3; tạo nhu cầu biểu diễn gọn (phần 4, Q00); số liệu dùng lại ở bảng so sánh C00.
- **Ghi chú diễn giả:** mô hình bộ nhớ; kỳ vọng số tầng trên $p/(1-p)$ và so với ước lượng của bài báo (302 byte); 8 byte mỗi mã định danh; giả thiết của $\log N$; chi phí xây.
- **Nguồn:** Malkov–Yashunin mục 4.2 tr.7, mục 4.2.3 tr.8; Princeton lớp 9 tr.2, tr.7. Số liệu tính lại bằng chương trình (mô phỏng $E[\ell]=0{,}0664$).
- **Quyết định:** sửa. Tiêu đề cũ là câu dài; bản cũ chỉ có $O(ND)$, $O(NM)$, không thay số nên không thấy véc-tơ gốc chiếm phần lớn bộ nhớ; không có câu nối sang PQ.

### Q00 — Lượng tử hóa véc-tơ (gộp Q01 cũ)

- **Sửa 2026-10-14:** quyết định `sửa`: dòng Nhu cầu; "lượng tử hóa véc-tơ (vector quantization, VQ)"; tách dòng 24; Ví dụ.. Âm tiết mặt trang 38 → 45. Thời lượng mới: 3,5 phút.

- **Phần:** 4, lượng tử hóa tích (khái niệm/thuật toán). **Vai trò:** mở phần, trực giác, ví dụ chạy tay, kiểm tra. **Thời lượng:** 4 phút.
- **Mục đích:** mã hóa và tái dựng một véc-tơ bằng bộ mã cho trước, tính sai số.
- **Câu chốt:** mã ngắn ($\log_2 k$ bit) đổi lấy sai số tái dựng.
- **Đầu vào:** véc-tơ gốc chiếm phần lớn bộ nhớ (H13). **Thể hiện:** dòng định nghĩa; hình `luong-tu-hoa-vec-to.svg` (ba tâm, ba ô, $x$ nối tới $c_1$); phép tính bên phải; câu hỏi.
- **Kết nối vào–ra:** đáp nhu cầu giảm bộ nhớ của H13; giao định nghĩa cho đặc tả Q02.
- **Kiểm tra:** $y=(0{,}6;1{,}5)$: $2{,}61$; $4{,}21$; $0{,}61$ → mã 2, sai số 0,61 (tính lại).
- **Nguồn:** Princeton lớp 8 tr.8–9; PQ paper mục II-A tr.2. Ví dụ dựng từ định nghĩa.
- **Quyết định:** gộp. Q00 cũ chỉ có hai thẻ ký hiệu, không hình, không nói nhu cầu; Q01 cũ là ví dụ của cùng khái niệm và câu hỏi của nó có đáp án hiện sẵn trên trang ($0{,}25$).

### Q02 — Đặc tả lượng tử hóa véc-tơ

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Thuật toán: mã hóa VQ"; bảng ba hàng thành Đầu vào, Đầu ra và một câu chi phí. Âm tiết mặt trang 34 → 36. Tiêu đề hiện hành: “Thuật toán: mã hóa VQ”. Thời lượng mới: 2 phút.

- **Phần:** 4. **Vai trò:** hình thức hóa, chi phí. **Thời lượng:** 2 phút.
- **Mục đích:** viết đặc tả VQ và tính chi phí mã hóa, lưu bộ mã theo $k$, $D$.
- **Câu chốt:** mã hóa tốn $\Theta(kD)$ và bộ mã chiếm $kD$ số; cả hai tỷ lệ với số tâm $k$.
- **Đầu vào:** định nghĩa và ví dụ Q00. **Thể hiện:** công thức argmin; bảng đầu vào/đầu ra/chi phí.
- **Kết nối vào–ra:** hình thức hóa Q00; chi phí theo $k$ dẫn tới giới hạn bộ mã lớn ở Q03.
- **Ghi chú diễn giả:** k-means và điều kiện Lloyd chỉ cho cực tiểu cục bộ; điều kiện sau từ argmin.
- **Nguồn:** PQ paper mục II-A, pt.2–5 tr.2; Princeton lớp 8 tr.9–10, 32.
- **Quyết định:** sửa. Bản cũ thiếu chi phí nên Q03 phải tự đưa công thức bộ nhớ; tên k-means chỉ có trong ghi chú; cấu trúc ba dòng văn xuôi khó quét.

### Q03 — Giới hạn của một bộ mã lớn

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Chi phí: …"; Nhu cầu, Mô hình; tách dòng 25, 24; Kết luận có nhãn. Âm tiết mặt trang 76 → 67. Tiêu đề hiện hành: “Chi phí: một bộ mã lớn”. Thời lượng mới: 2 phút.

- **Phần:** 4. **Vai trò:** nêu giới hạn tạo nhu cầu. **Thời lượng:** 2 phút.
- **Mục đích:** tính chi phí lưu, mã hóa, học của một bộ mã cho mã 64 bit và kết luận cần cấu trúc khác.
- **Câu chốt:** mã dài với một bộ mã duy nhất đòi hỏi bộ mã khổng lồ; cần tạo mã dài từ các bộ mã nhỏ.
- **Đầu vào:** chi phí theo $k$ (Q02). **Thể hiện:** dòng dẫn (sai số giảm khi tăng $k$; ví dụ SIFT của nguồn); bảng ba dòng thay số; câu chốt.
- **Kết nối vào–ra:** dùng chi phí Q02; tạo nhu cầu chia đoạn ở Q04.
- **Ghi chú diễn giả:** tăng tuyến tính theo $k$ nhưng hàm mũ theo độ dài mã; phép tính; nhận định của bài báo.
- **Nguồn:** PQ paper mục II-B tr.3; Princeton lớp 8 tr.18.
- **Quyết định:** sửa. Tiêu đề cũ là câu; không nói vì sao cần mã 64 bit; công thức không thay số nên “không khả thi” chỉ là khẳng định.

### Q04 — Lượng tử hóa tích (PQ)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Mã PQ và tái dựng" để khác tên mạch; Nhu cầu; Định nghĩa.; "tương tự VQ, nhưng …". Âm tiết mặt trang 26 → 44. Tiêu đề hiện hành: “Mã PQ và tái dựng”. Thời lượng mới: 3 phút.

- **Phần:** 4. **Vai trò:** trực giác và định nghĩa. **Thời lượng:** 3 phút.
- **Mục đích:** mô tả cách PQ tạo mã dài từ $m$ bộ mã con; tính độ dài mã.
- **Câu chốt:** chia véc-tơ thành $m$ đoạn, mỗi đoạn một bộ mã con nhỏ; mã là bộ $m$ chỉ số, tái dựng bằng ghép các tâm con.
- **Đầu vào:** VQ (Q00–Q02), giới hạn bộ mã lớn (Q03). **Thể hiện:** hình `pq-tach-doan.svg` (tám tọa độ, bốn đoạn, bốn bộ mã 256 tâm, mã 32 bit; màu kèm nhãn “đoạn $j$”); ba gạch đầu dòng.
- **Kết nối vào–ra:** đáp nhu cầu Q03; giao định nghĩa cho ví dụ Q05 và công thức kích thước Q07.
- **Ghi chú diễn giả:** tên đầy đủ; $m\mid D$; học từng bộ mã con; chi phí mã hóa $\Theta(k^*D)$; ký hiệu `M` của Faiss.
- **Nguồn:** PQ paper mục II-B pt.8–9 tr.3; Princeton lớp 8 tr.29–31.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình cũ `pq-split.svg` chữ rất nhỏ; mặt trang không có độ dài mã, cách tái dựng và tên đầy đủ của PQ.

### Q05 — Ví dụ mã hóa PQ

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Ví dụ: …"; dòng yêu cầu. Âm tiết mặt trang 11 → 18. Tiêu đề hiện hành: “Ví dụ: mã hóa PQ hai đoạn”. Thời lượng mới: 3 phút.

- **Phần:** 4. **Vai trò:** ví dụ chạy tay. **Thời lượng:** 3 phút.
- **Mục đích:** mã hóa một véc-tơ bằng PQ hai đoạn, tái dựng và tính sai số.
- **Câu chốt:** mỗi đoạn mã hóa độc lập; sai số tái dựng là tổng sai số các đoạn.
- **Đầu vào:** định nghĩa PQ (Q04). **Thể hiện:** dòng dữ kiện; hình `pq-vi-du.svg` (hai mặt phẳng con, tâm được chọn tô đặc); bảng khoảng cách và chỉ số; dòng kết quả.
- **Kết nối vào–ra:** cụ thể hóa Q04; mã $(0,1)$ và hai bộ mã được dùng lại ở ví dụ ADC (Q06, có hình biến thể kèm $q$).
- **Ghi chú diễn giả:** tọa độ các tâm; một phép tính mẫu; vì sao sai số cộng theo đoạn; so với VQ bốn chiều.
- **Nguồn:** dựng từ định nghĩa, PQ paper mục II-B tr.3.
- **Quyết định:** sửa. Bản cũ để các khoảng cách (phép tính cần học) và sai số trong ghi chú; không có hình; số thập phân dùng dấu chấm; tiêu đề “Ví dụ PQ ghép hai chỉ số” không nói thao tác.

### Q06 — Ví dụ khoảng cách bất đối xứng (chuyển sau Q07)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Ví dụ: …". Âm tiết mặt trang 22 → 22. Tiêu đề hiện hành: “Ví dụ: khoảng cách bất đối xứng của mã $(0,1)$”. Thời lượng mới: 3 phút.

- **Phần:** 4. **Vai trò:** ví dụ chạy tay trước hình thức hóa ADC. **Thời lượng:** 3 phút.
- **Mục đích:** tính khoảng cách bất đối xứng từ truy vấn đầy đủ tới một véc-tơ chỉ còn mã; so với khoảng cách thật.
- **Câu chốt:** ADC ước lượng $\|q-x\|^2$ bằng $\|q-\widehat x\|^2$, cộng theo đoạn; sai lệch đến từ sai số tái dựng.
- **Đầu vào:** mã $(0,1)$ và hai bộ mã của Q05, nhắc lại bằng hình `pq-vi-du-adc.svg` và ghi chú. **Thể hiện:** dòng định nghĩa bằng lời; hình bên trái; $q$, bảng hai đoạn và dòng so sánh bên phải.
- **Kết nối vào–ra:** dùng ví dụ Q05; giao số hạng từng đoạn cho công thức ADC Q08 và bảng tra Q09.
- **Ghi chú diễn giả:** dữ kiện bộ mã; phép tính; tên đầy đủ ADC; vì sao gọi là bất đối xứng; không cần $x$.
- **Nguồn:** PQ paper mục III-A pt.13 tr.4; Princeton lớp 8 tr.25–26.
- **Quyết định:** sửa và chuyển vị trí. Bản cũ mở bằng “Giữ mã … từ ví dụ PQ trước” (dẫn chiếu trang trước, không nhắc lại bộ mã); “khoảng cách bất đối xứng” chưa được giải thích; giá trị đúng 0,07 chỉ ở ghi chú. Chuyển sau Q07 để mạch mã hóa → bộ nhớ → khoảng cách liền nhau.

### Q07 — Kích thước mã và bộ mã PQ

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Chi phí: …"; Kết luận có nhãn. Âm tiết mặt trang 41 → 43. Tiêu đề hiện hành: “Chi phí: kích thước mã và bộ mã PQ”. Thời lượng mới: 3 phút.

- **Phần:** 4. **Vai trò:** chi phí bộ nhớ, ứng dụng vào tình huống mở đầu. **Thời lượng:** 3 phút.
- **Mục đích:** tính độ dài mã, kích thước bộ mã PQ; so với VQ; tính bộ nhớ mã cho kho $10^{10}$ véc-tơ.
- **Câu chốt:** PQ có $2^{64}$ mã với bộ mã chỉ $32\,768$ số; kho mở đầu còn 5,12 TB mã thay vì 122,88 TB.
- **Đầu vào:** định nghĩa PQ (Q04), giới hạn VQ (Q03), số liệu $N$, $D$ (nhắc lại bằng số). **Thể hiện:** dòng công thức; bảng VQ/PQ ba hàng; câu chốt thay số.
- **Kết nối vào–ra:** giải quyết Q03; thu hồi một phần tình huống P01 (bộ nhớ); tạo nhu cầu tính khoảng cách trên mã (Q06).
- **Ghi chú diễn giả:** suy ra $k^*D$; tích không gian; phép tính 512 byte, 5,12 TB, tỷ lệ 24; phần chưa tính.
- **Nguồn:** PQ paper mục II-B tr.3; Princeton lớp 8 tr.32–33; BIODS bài 12 tr.17.
- **Quyết định:** sửa. Tiêu đề cũ là câu; bản cũ không so với VQ nên không thấy PQ giải quyết Q03 thế nào; số liệu tình huống mở đầu chỉ trong ghi chú.

### Q08 — Khoảng cách bất đối xứng (ADC)

- **Sửa 2026-10-14:** quyết định `sửa`: Định nghĩa. với "asymmetric distance computation"; Kết luận có nhãn; ghi chú bỏ "Bài này". Âm tiết mặt trang 34 → 51. Thời lượng mới: 2 phút.

- **Phần:** 4. **Vai trò:** hình thức hóa. **Thời lượng:** 2 phút.
- **Mục đích:** viết công thức ADC và chỉ ra vì sao số hạng mỗi đoạn tính trước được.
- **Câu chốt:** với một truy vấn, số hạng đoạn $j$ chỉ có $k^*$ giá trị khác nhau.
- **Đầu vào:** ví dụ ADC (Q06), định nghĩa PQ (Q04). **Thể hiện:** công thức; hai gạch đầu dòng; câu chốt.
- **Kết nối vào–ra:** hình thức hóa Q06; giao ý “tính trước” cho bảng tra Q09.
- **Ghi chú diễn giả:** vì sao tổng theo đoạn; số hạng của ví dụ; SDC và nhận định của bài báo.
- **Nguồn:** PQ paper mục III-A pt.13 tr.4; Princeton lớp 8 tr.26–27.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hai thẻ “Truy vấn: không lượng tử hóa / Cơ sở dữ liệu: chỉ giữ mã PQ” lặp định nghĩa; ý dẫn tới bảng tra chưa có.

### Q09 — Bảng tra khoảng cách

- **Sửa 2026-10-14:** quyết định `tách`: 10 dòng; giữ định nghĩa bảng và ví dụ, bảng chi phí sang Q11. Âm tiết mặt trang 44 → 20. Thời lượng mới: 2 phút.

- **Phần:** 4. **Vai trò:** thuật toán và chi phí. **Thời lượng:** 3 phút.
- **Mục đích:** lập bảng tra cho một truy vấn, chấm mã bằng tra và cộng, so chi phí với tính trực tiếp.
- **Câu chốt:** lập bảng một lần $\Theta(k^*D)$, sau đó mỗi mã chỉ cần $m$ lần tra.
- **Đầu vào:** công thức ADC (Q08), ví dụ hai đoạn (Q05–Q06; dữ kiện ghi trong ghi chú, các ô của bảng hiện trên trang). **Thể hiện:** dòng định nghĩa $T$; bảng HTML 2×2 với hai ô viền đậm cho mã $(0,1)$ (không chỉ bằng màu); dòng chấm hai mã; bảng chi phí.
- **Kết nối vào–ra:** hiện thực Q08; chi phí chấm một mã giao cho Q10 (quét $N$ mã) và I03.
- **Ghi chú diễn giả:** dữ kiện; một ô mẫu; phép đếm $k^*D$; khi nào đáng lập bảng; 512 lần tra so với 3072 tọa độ.
- **Nguồn:** PQ paper mục III-A tr.4; Princeton lớp 8 tr.27, 31–32.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình cũ `pq-lut.svg` chữ rất nhỏ, không có số; chi phí chỉ ở một dòng ký hiệu. Bảng tra dựng bằng HTML theo quy định bảng không dùng ảnh.

### Q10 — Giới hạn của PQ quét đầy đủ

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Chi phí: …"; Kết luận có nhãn; ngoại lệ trần 80 (bảng so sánh). Âm tiết mặt trang 59 → 61. Tiêu đề hiện hành: “Chi phí: PQ quét đầy đủ”. Thời lượng mới: 3 phút.

- **Phần:** 4 (kết phần). **Vai trò:** chi phí, giới hạn, kiểm tra, câu nối. **Thời lượng:** 3 phút.
- **Mục đích:** tính dữ liệu đọc và số lần tra khi quét mã PQ; so với quét véc-tơ gốc; chỉ ra thừa số còn lại.
- **Câu chốt:** PQ giảm chi phí mỗi phép đo, không giảm số véc-tơ được chấm.
- **Đầu vào:** kích thước mã (Q07), chi phí chấm một mã (Q09), số liệu kho (nhắc lại bằng số). **Thể hiện:** dòng dữ kiện; bảng hai cột; hộp câu hỏi; câu chốt.
- **Kết nối vào–ra:** đóng phần 4; nối A03 (hai thừa số) sang phần 5: chỉ mở một phần kho.
- **Kiểm tra:** $5{,}12$ giây với $10^{12}$ lần tra/giây (giả định), so với 30,7 giây ở P01.
- **Nguồn:** PQ paper tr.2, mục IV tr.6; Princeton lớp 8 tr.20–22.
- **Quyết định:** sửa. Tiêu đề cũ là câu; chi phí chỉ ký hiệu, không so được với lượt quét gốc; “tầng định tuyến” xuất hiện đột ngột.

### I00 — Tệp đảo (IVF)

- **Sửa 2026-10-14:** quyết định `sửa`: Nhu cầu; "tệp đảo (inverted file, IVF)" bằng "là"; bảng bốn danh sách bỏ (hình đã có); Ví dụ.. Âm tiết mặt trang 54 → 46. Thời lượng mới: 2,5 phút.

- **Phần:** 5, IVF-PQ (thuật toán). **Vai trò:** mở phần, trực giác, ví dụ. **Thời lượng:** 3 phút.
- **Mục đích:** mô tả tệp đảo, xác định danh sách được mở với $nprobe$ cho trước trên ví dụ.
- **Câu chốt:** IVF giảm số véc-tơ được chấm; mã PQ trong mỗi danh sách giảm chi phí mỗi lần chấm.
- **Đầu vào:** giới hạn PQ quét đầy đủ (Q10), VQ (Q00–Q02). **Thể hiện:** dòng định nghĩa; hình `tep-dao.svg` (bốn ô, hai ô mở tô màu và viền liền, nhãn “(mở)”; nhãn $y_3$, $y_8$); bảng HTML bốn danh sách; dòng 8/16.
- **Kết nối vào–ra:** nhận thừa số “số véc-tơ được chấm” từ Q10; ví dụ dùng tiếp ở I01–I04.
- **Ghi chú diễn giả:** tên đầy đủ; IVF là VQ thô; tọa độ ví dụ; tương ứng ký hiệu $k'$, $w$ của bài báo và `nlist`, `nprobe` của Faiss.
- **Nguồn:** Princeton lớp 8 tr.21–22; PQ paper mục IV tr.6–7. Ví dụ do học phần dựng.
- **Quyết định:** viết lại. Bản cũ (tiêu đề câu “IVF-PQ định tuyến rồi chấm mã nén”) chỉ có hai thẻ chữ, không hình; dùng “định tuyến”, “véc-tơ dư” chưa giải thích.

### I01 — Chọn danh sách cần mở

- **Sửa 2026-10-14:** quyết định `sửa`: "Đáp án" thành "Lời giải" trong ghi chú. Âm tiết mặt trang 13 → 13. Thời lượng mới: 3 phút.

- **Phần:** 5. **Vai trò:** hình thức hóa phép gán, ví dụ, kiểm tra. **Thời lượng:** 3 phút.
- **Mục đích:** gán véc-tơ vào danh sách, chọn $nprobe$ danh sách cho một truy vấn; thấy giới hạn khi hàng xóm nằm ở ô bên cạnh.
- **Câu chốt:** mở danh sách theo khoảng cách từ $q$ tới tâm thô; hàng xóm thật gần ranh giới có thể nằm ở danh sách chưa mở.
- **Đầu vào:** ví dụ bốn ô (I00), nhắc lại bằng hình `tep-dao-o.svg` (không đánh dấu danh sách mở để khớp câu hỏi). **Thể hiện:** công thức $a(y)$, $L_i$; hình; bảng bốn tâm và thứ tự; hộp câu hỏi.
- **Kết nối vào–ra:** cụ thể hóa I00; hiện tượng bỏ sót dẫn tới tham số $nprobe$ trong chi phí I03.
- **Kiểm tra:** $y_3$ không được chấm với $nprobe=1$ (9,49 < 15,49 nên $y_3\in L_0$), dù là hàng xóm gần thứ hai ($2{,}34$).
- **Nguồn:** Princeton lớp 8 tr.21–22; PQ paper mục IV-A, IV-C tr.6–7.
- **Quyết định:** sửa. Tiêu đề cũ là câu; ví dụ cũ hai tâm $\mu_0=(0,0)$, $\mu_1=(8,0)$ rời rạc với các ví dụ khác và không cho thấy tác dụng của $nprobe$; ký tự “<” thô từng làm hỏng công thức (đã sửa ở bước chuẩn bị).

### I02 — Mã hóa phần dư

- **Sửa 2026-10-14:** quyết định `sửa`: thêm Nhu cầu; Ví dụ.. Âm tiết mặt trang 27 → 31. Thời lượng mới: 3 phút.

- **Phần:** 5. **Vai trò:** cơ chế và lập luận đúng. **Thời lượng:** 3 phút.
- **Mục đích:** tính phần dư và truy vấn dư; giải thích vì sao mỗi danh sách mở cần một bảng tra riêng.
- **Câu chốt:** $\|q-y\|=\|\widetilde q_i-r(y)\|$ với $y\in L_i$, nên quét $L_i$ bằng ADC với truy vấn dư $\widetilde q_i$.
- **Đầu vào:** ví dụ bốn ô (I00–I01), nhắc lại bằng hình phóng to hai ô dưới `tep-dao-du.svg`; ADC (Q06–Q09). **Thể hiện:** hai công thức; hình; hai gạch đầu dòng; dòng số liệu ví dụ.
- **Kết nối vào–ra:** cụ thể hóa cách chấm trong danh sách; số bảng tra $nprobe$ giao cho chi phí I03 và thuật toán I04.
- **Ghi chú diễn giả:** vì sao phần dư mã hóa tốt hơn; đẳng thức; kiểm tra 1,25; dùng nhầm bảng cho 31,25; một PQ chung cho mọi ô.
- **Nguồn:** PQ paper mục IV-A, IV-B tr.6, pt.31.
- **Quyết định:** sửa. Tiêu đề cũ là câu; không có lý do cho truy vấn dư riêng; dẫn chiếu “ví dụ ngay trước” bằng lời.

### I03 — Chi phí truy vấn IVF-PQ (chuyển sau I04)

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Chi phí: …"; Mô hình, Giả thiết; bảng về khuôn chung bốn cột. Âm tiết mặt trang 43 → 55. Tiêu đề hiện hành: “Chi phí: truy vấn IVF-PQ”. Thời lượng mới: 3 phút.

- **Phần:** 5. **Vai trò:** chi phí và ứng dụng vào tình huống mở đầu. **Thời lượng:** 3 phút.
- **Mục đích:** đếm chi phí truy vấn theo từng bước của thuật toán, thay số cho kho $10^{10}$ véc-tơ.
- **Câu chốt:** với $k_c=10^5$, $nprobe=64$, một truy vấn cần khoảng $3{,}6\cdot10^9$ thao tác, ít hơn khoảng 1400 lần so với quét đủ mã PQ.
- **Đầu vào:** thuật toán I04, chi phí lập bảng và chấm mã (Q09), số liệu kho (nhắc lại bằng số). **Thể hiện:** dòng giả định; bảng bước × số lần × chi phí × thay số; câu chốt so với Q10.
- **Kết nối vào–ra:** đếm theo các bước của I04; giao số liệu cho bảng so sánh C00.
- **Ghi chú diễn giả:** mô hình đếm; bỏ qua top-$K$; giả thiết cân bằng; phép tính; 3,6 ms; giả định minh họa; tác động của $nprobe$.
- **Nguồn:** PQ paper mục IV-C tr.7; Princeton lớp 8 tr.22, lớp 9 tr.5.
- **Quyết định:** sửa và chuyển vị trí. Tiêu đề cũ là câu; chưa theo mạch đếm bước × số lần × chi phí; không thay số nên không thấy IVF-PQ đáp ứng bài toán; giả thiết cân bằng chỉ ở ghi chú; đứng trước trang thuật toán.

### I04 — Thuật toán truy vấn IVF-PQ

- **Sửa 2026-10-14:** quyết định `tách`: Đầu vào/Đầu ra trước giả mã; vết đối chiếu sang I05 cùng tiêu đề. Âm tiết mặt trang 32 → 32. Tiêu đề hiện hành: “Thuật toán: truy vấn IVF-PQ”. Thời lượng mới: 2,5 phút.

- **Phần:** 5. **Vai trò:** thuật toán, ví dụ, kiểm tra. **Thời lượng:** 4 phút.
- **Mục đích:** đọc giả mã truy vấn IVF-PQ, chạy trên ví dụ, tính độ thu hồi khi đổi $nprobe$.
- **Câu chốt:** chỉ phần tử của $nprobe$ danh sách được chấm; hàng xóm ở danh sách chưa mở bị bỏ sót.
- **Đầu vào:** chọn danh sách (I01), phần dư và bảng tra riêng (I02), độ thu hồi (A01). **Thể hiện:** giả mã 8 dòng bên trái; bảng khoảng cách hai danh sách (tự chứa dữ kiện, ghi “ADC giả sử đúng”) và dòng kết quả bên phải; hộp câu hỏi.
- **Kết nối vào–ra:** tổng hợp I01–I02; các bước giả mã là cơ sở đếm chi phí I03.
- **Ghi chú diễn giả:** đặc tả đầu vào/đầu ra; trường hợp ít hơn $K$; dừng; trả mã định danh; giả định ADC đúng; đáp án $2/3$.
- **Nguồn:** PQ paper mục IV-C tr.7; Princeton lớp 8 tr.21.
- **Quyết định:** sửa. Tiêu đề cũ là câu; hình `ivfpq-flow.svg` chữ rất nhỏ; danh sách bốn bước thiếu khởi tạo, vòng lặp, cấu trúc giữ $K$ kết quả; không có vết chạy hay kiểm tra.

### C00 — So sánh bốn cấu trúc

- **Sửa 2026-10-14:** quyết định `sửa`: đổi sang khuôn Thuật toán | Đầu vào | Bảo đảm | Chi phí (quyết định 3); câu kết 31 âm tiết sang C04. Âm tiết mặt trang 99 → 67. Tiêu đề hiện hành: “Thuật toán, bảo đảm và chi phí”. Thời lượng mới: 3 phút.

- **Phần:** 6, tổng kết. **Vai trò:** đối chiếu, thu hồi tình huống. **Thời lượng:** 5 phút.
- **Mục đích:** so sánh bốn cấu trúc trên cùng bảng và trả lời bài toán mở đầu bằng số liệu bộ nhớ, chi phí truy vấn.
- **Câu chốt:** với kho mở đầu, HNSW cần khoảng 125 TB; IVF-PQ khoảng 5,2 TB và $3{,}6\cdot10^9$ thao tác mỗi truy vấn, đổi lại độ thu hồi phụ thuộc $nprobe$ và sai số mã hóa.
- **Đầu vào:** hai thừa số (A03), bốn trục (A02), số liệu H13, Q07, Q10, I03 (ghi lại bằng số trên trang). **Thể hiện:** dòng giả định; bảng năm cột; câu chốt.
- **Kết nối vào–ra:** thu hồi P01; chuyển sang câu hỏi tự kiểm C01.
- **Ghi chú diễn giả:** không xếp hạng phổ quát; chất lượng phải đo; khi nào HNSW phù hợp; kết hợp hai hướng; phép tính; LSH không thay số.
- **Nguồn:** tổng hợp; MMDS Ch.3; Princeton lớp 8 tr.2–5, lớp 9 tr.2–7; hai bài báo.
- **Quyết định:** sửa. Tiêu đề cũ “Bốn cơ chế trên cùng bốn trục”; bảng chỉ có ký hiệu; câu “Trả lời bài toán mở đầu” là lời khuyên chung, không thu hồi tình huống bằng số.

### C01, C02 — Tự kiểm tra (trang mới)

- **Phần:** 6, tổng kết. **Vai trò:** kiểm tra cuối bài. **Thời lượng:** 5 phút.
- **Mục đích:** tự kiểm ba mục tiêu của P02 bằng sáu câu ngắn có dữ kiện mới.
- **Câu chốt:** mỗi câu dùng lại một phép tính hoặc thuật toán của bài trên dữ kiện chưa xuất hiện.
- **Thể hiện:** nhãn “Câu hỏi:” và danh sách đánh số ba câu mỗi trang; đáp án và mục tiêu được kiểm trong ghi chú diễn giả.
- **Kết nối vào–ra:** sau C00; mở phần thực hành R00.
- **Kiểm tra (tính lại bằng chương trình):** C01: $1/2$; $ef=2$ không tới $z$, $ef=3$ tới $z$; 77,7 GB > 64 GB. C02: 8 byte, 245 760 số; 3,6; 500 000 mã, $4\cdot10^6$ lần tra.
- **Nguồn:** dữ kiện học phần dựng; $D=960$ là số chiều GIST trong bài báo PQ; $k_c=32\,000$ cho $N=10^9$ theo Princeton lớp 9 tr.5.
- **Sửa 2026-10-14:** tiêu đề "Câu hỏi tự kiểm tra" cho cả hai trang; dòng "Câu hỏi: trả lời và nêu kết quả đã dùng"; ghi chú nêu kết quả đã dùng và lời giải, ánh xạ câu → mục tiêu chuyển lên mục "Ánh xạ câu tự kiểm tra → mục tiêu". Hai dòng "Thể hiện" và "Kết nối vào–ra" ở trên là bản cũ. Kết nối hiện hành: C04 → C01 (câu 1–3: độ thu hồi, SEARCH-LAYER, bộ nhớ HNSW) → C02 (câu 4–6: kích thước mã PQ, ADC, số mã IVF-PQ) → C05 → RT.
- **Quyết định:** thêm. Phần kết cũ chỉ có C00, thiếu 4–6 nhiệm vụ tự kiểm theo tiêu chuẩn mục 2; P02 đã cam kết “So sánh và tự kiểm tra” (việc mở từ lượt rà phần 1–2).

### R00 — Sổ thực hành và dữ liệu

- **Sửa 2026-10-14:** quyết định `sửa`: nhãn Thực hành (quyết định 7). Âm tiết mặt trang 45 → 47. Thời lượng mới: 0 phút.

- **Phần:** 7, bài tập. **Vai trò:** mở phần thực hành. **Thời lượng:** 0 phút (đọc trước).
- **Mục đích:** biết dữ liệu dùng trong ba nhiệm vụ và ô nguồn của từng nhiệm vụ.
- **Câu chốt:** `xb` là kho $N=10^4$ véc-tơ 64 chiều, `gt` là tập đúng 10 hàng xóm từ quét đầy đủ.
- **Thể hiện:** dòng tên sổ và ô chuẩn bị; bảng bốn mảng; bảng ba nhiệm vụ.
- **Kết nối vào–ra:** sau phần tự kiểm; mở R01–R08. Ánh xạ `M`, `nbits` của Faiss sang $m$, $b$.
- **Ghi chú diễn giả:** tham số `SyntheticDataset`; `gt` từ `faiss.knn`; ký hiệu Faiss; hướng dẫn chuẩn bị máy; thời gian chạy máy không tính vào thời lượng tại lớp.
- **Nguồn:** sổ Princeton lớp 8, ô 0–4, 17, 21–24.
- **Quyết định:** sửa. Bản cũ không nói dữ liệu gồm gì, đặt đường dẫn nội bộ `sources/…` trên mặt trang và dòng chỉ dẫn điều phối “Thời gian máy được báo riêng”.

### R01 — Nhiệm vụ 1: mã và tái dựng PQ

- **Sửa 2026-10-14:** quyết định `sửa`: tiêu đề "Bài tập: … (a)"; "Sản phẩm:" thành Câu hỏi; dòng Nguồn; ghi chú có năng lực kiểm và Gợi ý. Âm tiết mặt trang 34 → 44. Tiêu đề hiện hành: “Bài tập: mã và tái dựng PQ (a)”. Thời lượng mới: 5,5 phút.

- **Phần:** 7. **Vai trò:** bài tập vận dụng công thức kích thước PQ. **Thời lượng:** 6 phút.
- **Mục đích:** nối tham số Faiss với $D$, $m$, $b$, $k^*$; dự đoán kích thước mã và bộ mã rồi kiểm bằng số in ra.
- **Thể hiện:** dòng ô 83; bảng ba đại lượng với cột dự đoán và giá trị in ra; dòng sản phẩm.
- **Kết nối vào–ra:** dùng Q04, Q07; giao cấu trúc `pq_centroids`, `xb_codes` cho R02.
- **Ghi chú diễn giả:** đáp án; ý nghĩa ô 94; ô 88–89; hướng dẫn chấm.
- **Nguồn:** sổ thực hành ô 82–95 (đọc trực tiếp nội dung ô).
- **Quyết định:** sửa. Bản cũ yêu cầu “bảng kích thước” mà không nói điền gì; chưa nối tham số Faiss với ký hiệu bài giảng; dòng “Dữ kiện” liệt kê tên biến không giải thích.

### R02 — Tái dựng thủ công véc-tơ 123

- **Sửa 2026-10-14:** quyết định `sửa`: "Gợi ý:" thành "Nhắc lại:"; "Yêu cầu:" thành Câu hỏi; dòng Nguồn. Âm tiết mặt trang 26 → 37. Tiêu đề hiện hành: “Bài tập: mã và tái dựng PQ (b)”. Thời lượng mới: 9 phút.

- **Phần:** 7. **Vai trò:** bài tập lập trình nối công thức với mảng. **Thời lượng:** 9 phút.
- **Mục đích:** viết biểu thức tái dựng PQ từ mã và bộ mã con.
- **Thể hiện:** dòng gợi ý công thức; khối mã chép đúng ô 96–97 (`language-python`, `data-trim`); dòng yêu cầu.
- **Kết nối vào–ra:** dùng cấu trúc mảng của R01 và công thức Q04; R03 yêu cầu giải thích điều kiện khớp.
- **Ghi chú diễn giả:** lời giải; vì sao so sánh chính xác đúng; hướng dẫn chấm.
- **Nguồn:** sổ thực hành ô 96–97.
- **Quyết định:** sửa. Bản cũ ghi `assert np.all(...)` khác ô 97 của nguồn; không nhắc công thức tái dựng; tiêu đề “Hoàn thiện ô tái dựng còn trống” mô tả thao tác thay vì nội dung.

### R03 — Điều kiện để tái dựng khớp

- **Sửa 2026-10-14:** quyết định `sửa`: tách dòng 22; "Sản phẩm:" vào Câu hỏi; dòng Nguồn. Âm tiết mặt trang 69 → 72. Tiêu đề hiện hành: “Bài tập: mã và tái dựng PQ (c)”. Thời lượng mới: 5 phút.

- **Phần:** 7. **Vai trò:** giải thích, lập luận. **Thời lượng:** 5 phút.
- **Mục đích:** giải thích vì sao biểu thức tái dựng bằng kết quả `decode` qua ba điều kiện.
- **Thể hiện:** dòng nhiệm vụ; bảng ba điều kiện với cột “Nếu vi phạm thì”; dòng sản phẩm.
- **Kết nối vào–ra:** hoàn tất nhiệm vụ 1 (R01–R02); mở nhiệm vụ 2 (R04).
- **Ghi chú diễn giả:** đáp án mẫu; rubric 10 điểm của nhiệm vụ 1.
- **Nguồn:** sổ thực hành ô 96–97; Princeton lớp 8 tr.30–31.
- **Quyết định:** sửa. Bản cũ chỉ có cột “Giải thích của nhóm” để trống, không nói phải lập luận gì; ghi chú thiếu đáp án mẫu; tiêu đề “Giải thích điều kiện khớp” chưa nói khớp với gì.

### R04 — Nhiệm vụ 2: cùng ngân sách 6 byte

- **Sửa 2026-10-14:** quyết định `sửa`: MSE giải nghĩa; Câu hỏi; dòng Nguồn. Âm tiết mặt trang 37 → 48. Tiêu đề hiện hành: “Bài tập: cùng ngân sách 6 byte (a)”. Thời lượng mới: 10 phút.

- **Phần:** 7. **Vai trò:** thực nghiệm có dự đoán. **Thời lượng:** 10 phút.
- **Mục đích:** áp dụng $D/m$, $k^*=2^b$ cho ba cấu hình cùng độ dài mã; thu số đo MSE và thời gian.
- **Thể hiện:** dòng mô tả ô 99 với ánh xạ `M`, `nbits`; bảng sáu cột ($m$, $b$ cho sẵn; bốn cột để điền); dòng hướng dẫn.
- **Kết nối vào–ra:** dùng Q04, Q07; số liệu dùng ở phân tích R05.
- **Ghi chú diễn giả:** đáp án dự đoán; không có số đo cố định; thời gian trong ô 99 không gồm huấn luyện; chạy trước nếu máy chậm.
- **Nguồn:** sổ thực hành ô 98–99.
- **Quyết định:** sửa. Bản cũ điền sẵn `dsub`, `ksub` (phần sinh viên nên tự suy ra), không có cột cho MSE và thời gian; ký hiệu $M_{PQ}$ mới, khác $m$ của bài. Ghi chú tự học cũ gọi thời gian là “huấn luyện/mã hóa”, sai so với ô 99 (chỉ đo mã hóa và giải mã).

### R05 — Phân tích đánh đổi cùng ngân sách

- **Sửa 2026-10-14:** quyết định `sửa`: "Yêu cầu" và "Sản phẩm:" thành Câu hỏi; dòng Nguồn; trần 80. Âm tiết mặt trang 63 → 66. Tiêu đề hiện hành: “Bài tập: cùng ngân sách 6 byte (b)”. Thời lượng mới: 10 phút.

- **Phần:** 7. **Vai trò:** phân tích số đo bằng mô hình chi phí của bài. **Thời lượng:** 10 phút.
- **Mục đích:** giải thích khác biệt MSE và thời gian của ba cấu hình bằng $D/m$, $k^*$, $k^*D$.
- **Thể hiện:** ba yêu cầu đánh số; dòng sản phẩm.
- **Kết nối vào–ra:** dùng bảng R04 và chi phí mã hóa Q02, Q04; khép nhiệm vụ 2, mở nhiệm vụ 3 (R06).
- **Ghi chú diễn giả:** nhận định của nguồn; $262\,144$, $4\,096$, $512$; giải mã ít phụ thuộc $k^*$; rubric.
- **Nguồn:** sổ thực hành ô 98–99; Princeton lớp 8 tr.32–33.
- **Quyết định:** sửa. Bản cũ có bốn yêu cầu chung, chưa đưa công cụ của bài ($k^*D$) và nhận định của nguồn để đối chiếu với số đo; tiêu đề “Đọc đánh đổi…” không học thuật.

### R06 — Nhiệm vụ 3: chỉ mục IVF-PQ

- **Sửa 2026-10-14:** quyết định `sửa`: "Sản phẩm:" thành Câu hỏi; dòng Nguồn. Âm tiết mặt trang 33 → 38. Tiêu đề hiện hành: “Bài tập: chỉ mục IVF-PQ (a)”. Thời lượng mới: 6 phút.

- **Phần:** 7. **Vai trò:** bài tập nối cấu hình thư viện với ký hiệu bài giảng. **Thời lượng:** 6 phút.
- **Mục đích:** đọc chuỗi cấu hình Faiss thành $k_c$, $m$, $b$; tính byte mã và kích thước danh sách trung bình; nêu vai trò huấn luyện và thêm dữ liệu.
- **Thể hiện:** khối mã ô 149–151 (`language-python`); dòng nhiệm vụ; bảng năm ô trống; dòng sản phẩm.
- **Kết nối vào–ra:** dùng I00–I02 và Q07; chỉ mục dùng cho truy vấn R07.
- **Ghi chú diễn giả:** đáp án; ý nghĩa `np`; ô 150, 151 làm gì; chạy trước nếu máy chậm.
- **Nguồn:** sổ thực hành ô 148–151; tài liệu Faiss “The index factory”.
- **Quyết định:** sửa. Bản cũ yêu cầu “giải thích chuỗi cấu hình” mà không nói giải thích thành phần nào; không nối với ký hiệu của bài.

### R07 — Độ thu hồi và thời gian theo số danh sách mở

- **Sửa 2026-10-14:** quyết định `sửa`: thêm Câu hỏi có ô nguồn (không thêm dòng Nguồn riêng vì trang chật). Âm tiết mặt trang 33 → 42. Tiêu đề hiện hành: “Bài tập: chỉ mục IVF-PQ (b)”. Thời lượng mới: 9 phút.

- **Phần:** 7. **Vai trò:** thực nghiệm, đọc đúng đại lượng đo. **Thời lượng:** 9 phút.
- **Mục đích:** chạy vòng đo của nguồn và diễn giải từng đại lượng bằng khái niệm của bài.
- **Câu chốt:** $nok/100$ là $\operatorname{recall@1}$ trung bình; thời gian in ra là tổng của $5000$ truy vấn; mở $nprobe$ danh sách chấm khoảng $50\,nprobe$ mã.
- **Thể hiện:** khối mã ô 155 (`language-python`); bảng ba đại lượng.
- **Kết nối vào–ra:** dùng A01 (độ thu hồi), I03 (số mã được chấm), R06 ($N/k_c=50$); số liệu ghi vào R08.
- **Ghi chú diễn giả:** vì sao là recall@1 và không phải recall@10; thời gian mỗi truy vấn; không đổi số lần lặp, kích thước lô.
- **Nguồn:** sổ thực hành ô 152–155; Princeton lớp 8 tr.4 (trục “1-recall@1”).
- **Quyết định:** sửa. Bản cũ không có ô 155; định nghĩa $nok/|xq|$ không nối với độ thu hồi của bài (và ghi chú cũ tránh gọi nó là độ thu hồi, trong khi với $K=1$ đó chính là $\operatorname{recall@1}$); tiêu đề chứa ký hiệu bị viết hoa thành “NPROBE”.

### R08 — Phiếu báo cáo nhiệm vụ 3

- **Sửa 2026-10-14:** quyết định `sửa`: tách dòng 30; "Yêu cầu:" thành Câu hỏi; dòng Nguồn. Âm tiết mặt trang 44 → 52. Tiêu đề hiện hành: “Bài tập: chỉ mục IVF-PQ (c)”. Thời lượng mới: 5 phút.

- **Phần:** 7. **Vai trò:** tổng hợp số đo, giải thích bằng cơ chế. **Thời lượng:** 5 phút.
- **Mục đích:** ghi kết quả vòng đo, vẽ đường độ thu hồi–thời gian và giải thích bằng số mã được chấm.
- **Thể hiện:** bảng năm hàng, cột $nprobe$ cho sẵn, bốn cột để điền; dòng yêu cầu.
- **Kết nối vào–ra:** dùng R07 và I03; khép phần thực hành và bài.
- **Ghi chú diễn giả:** số mã được chấm 100–2500; cách tính ms mỗi truy vấn; xu hướng thường thấy nhưng chỉ kết luận theo số đo; rubric 10 điểm.
- **Nguồn:** sổ thực hành ô 149–155.
- **Quyết định:** sửa. Bản cũ chỉ có một hàng trống cho năm giá trị; thiếu cột thời gian mỗi truy vấn và số mã được chấm; tiêu đề “Báo cáo phép quét của nguồn” khó hiểu.

### Ghi chú điều phối phần bài tập (không đưa lên trang hay ghi chú diễn giả)

- Sinh viên cài Python, NumPy, Matplotlib, Faiss CPU và chạy các ô nền 0–4, 17, 21–24 trước buổi học trên chính kernel sẽ dùng.
- Thời gian chạy máy (ô 85, 99, 150, 155) không tính vào 60 phút làm bài; nếu máy chậm, chạy trước ô 99 và 150 trên cùng kernel.
- R02 là TODO của chính sổ nguồn; R08 chỉ là phiếu ghi kết quả của vòng đo trong nguồn, không thêm mục tiêu vận hành hay giá trị $nprobe$ mới.

### H03, H03B — Tìm kiếm chùm và vết (tách sau lượt duyệt góc nhìn sinh viên)

- **H03 (2 phút):** quy tắc trên mặt trang: $C$, $W$; mở đỉnh gần $q$ nhất trong $C$; lân cận chưa thấy vào $C$, $W$ nếu $|W|<ef$ hoặc gần hơn phần tử xa nhất, thừa thì bỏ phần tử xa nhất; dừng khi $C$ rỗng hoặc đỉnh sắp mở xa hơn phần tử xa nhất. Hình `do-thi-vi-du.svg`. Câu chốt: $ef=1$ trùng tham lam.
- **H03B (2 phút):** vết $ef=3$ với hình `do-thi-chum.svg`, bảng gộp ba lần mở cuối thành một hàng; câu hỏi $ef=2$; đáp án và giải thích các lần mở $t$, $u$, $z$ trong ghi chú.
- **Quyết định:** tách. Lượt duyệt góc nhìn sinh viên (nghiêm trọng): quy tắc thêm/bỏ và điều kiện dừng chỉ ở ghi chú nên không tự tái tạo được vết hay trả lời câu hỏi; đưa quy tắc lên cùng trang với bảng thì tràn khung (đáy 774/720).


## Lượt sửa sau ba báo cáo rà (2026-10-14)

Căn cứ: quyết định hợp nhất của điều phối viên (`fix-d07.md`) từ ba báo cáo rà toán, mạch truyện và sinh viên. Quyết định cho từng phát hiện và phép tính các con số nằm trong `review-log.md`, mục cùng tên. Số trang, thứ tự, thời lượng 120 + 60 phút không đổi.

| Mã | Thay đổi | Lý do | Kết nối vào → ra |
|---|---|---|---|
| P05 | Nhu cầu có 122,88 TB và ≈30,7 giây; dòng cuối có ngân sách giả định 6 TB, 10 ms; dòng HNSW "giữ véc-tơ gốc"; `ul` | vấn đề trung tâm phải có giới hạn tài nguyên bằng số (`AGENTS.md`); dòng 3 khớp giới hạn mạch 3 giao mạch 4 | P04 → P05 → P01; trả lời ở C04 |
| P01 | Câu hỏi "quét toàn kho gấp bao nhiêu lần 10 ms" | P05 đã nêu 30,7 giây; câu hỏi cũ lộ đáp án | P05 → P01 → AT |
| C04 | Trả lời bằng TB, giây, ms; dòng cuối nêu cả hai điều kiện | câu trả lời phải dùng đơn vị của vấn đề; sửa kết luận sai trong ghi chú | C00 → C04 → C01 |
| P03 | Dòng LSH: "chỉ xác minh ứng viên cùng thùng với $q$; hàng xóm gần có thể bị bỏ sót (Bài 06)" | khớp kết quả Bài 06; tên đầy đủ của LSH trong ghi chú P00, P03 vì dòng có tên đầy đủ dài 22 âm tiết | Bài 06 → P03 → A03, C00 |
| A00 | "tối đa $K$ điểm"; sai số do đo một phần kho hoặc đo xấp xỉ | đặc tả phủ cả hai nguồn sai số (HNSW, PQ) | P01 → A00 → A01, A03, Q10 |
| A03, Q11 | A03 "đo bằng mã PQ"; Q11 dòng Mô hình "chấm một mã là phép đo xấp xỉ qua bảng tra" | thống nhất "được đo"/"được chấm" | A03 → Q11 → Q10 → I03 |
| I03 | Mô hình nêu 8 + 512 byte mỗi phần tử; Kết luận có 5,2 TB; cột Đóng góp ba chữ số; $n_c\approx nprobe\,N/k_c$ | bộ nhớ IVF-PQ tính trong mạch 5 trước C00, C04; tổng cột khớp 3,63·10⁹ | I05 → I03 → CT, C00, C04 |
| H10 | Tiêu đề "Ví dụ: chèn một điểm vào đồ thị ba tầng"; $x=2{,}6$ lên dòng dữ kiện | chữ hoa của tiêu đề biến $x$ thành $X$ | H09, H08 → H10 → H10B |
| Q00, Q05, I05 | Ba tâm, bốn tâm con, tập đúng $N_3(q)$ lên mặt trang | câu hỏi phải làm được từ mặt trang | không đổi |
| H14 | Giả thiết giải nghĩa đồ thị Delaunay ("tham lam luôn tới điểm gần $q$ nhất") | lần đầu dùng thuật ngữ; C03 dùng lại không giải nghĩa | H13 → H14 → QT |
| CT, H12, R08 | Từ khóa 19 âm tiết; hộp câu hỏi 17; R08 gộp hai dòng thành một Câu hỏi | trần 20 âm tiết mỗi dòng, trần 8 dòng trang bảng | không đổi |
| I01 | Câu hỏi đổi sang "Với $nprobe=3$, danh sách nào được mở, danh sách nào không?" | I01 và I05 cùng kiểm việc bỏ lỡ $y_3$; giữ I05 vì có recall | I00 → I01 → I02 |
| C00 | Hàng LSH: bảo đảm $\ge1-(1-p_1^r)^b$ cho điểm có $d(q,y)\le d_1$, chi phí "số ứng viên × $D$; $12\,288+8b$ byte mỗi véc-tơ"; HNSW "$\approx12\,553$ byte mỗi véc-tơ"; IVF-PQ $3{,}63\cdot10^9$ | cùng mô hình chi phí cho bốn hàng; đơn vị "mỗi véc-tơ" | C03 → C00 → C04 |
| C05 | Trang của hai bài báo, năm 2018; dòng MMDS ấn bản 3 (2020), Chương 3 | `AGENTS.md`: tác giả, năm, chương, mục, trang | C02 → C05 → RT |
| Q04, Q05 | Giữ thứ tự định nghĩa trước ví dụ | Q05 dùng ký hiệu đoạn $x^{(j)}$ và $k^*$ do Q04 định nghĩa; cặp ADC đặt ví dụ trước (Q06 → Q08) vì công thức ADC đọc được ngay từ ví dụ | không đổi |
| RT | Không thêm nhãn Thực hành | trang tiêu đề mạch có khuôn riêng (`strand-title`), không có ô nhãn; R00–R08 đều có nhãn | không đổi |

Ghi chú diễn giả sửa ở P00, P01, P03, P05, A00, A01, A03, HT, H00, H03, H05, H13, H14, QT, Q00, Q05, Q07, Q11, I01, I02, I03, I04, IT, CT, C00, C04, R08 (chi tiết trong `review-log.md`).

### Sửa nhỏ cuối sau rà lại (2026-10-14)

- **C00:** dòng dữ kiện bỏ "$b=8$", ghi "mã PQ 512 byte"; ô Đầu vào IVF-PQ "$k_c$, $nprobe$, mã PQ"; $b$ trên trang chỉ còn là số dải của LSH như Bài 06. Ô PQ "mã, bảng tra"; ô Bảo đảm HNSW "đúng trên đỉnh đã thấy" (tầng 0 đã nêu ở H09). Âm tiết 79/80.
- **P05:** dòng cuối "Chọn chỉ mục đủ độ thu hồi với $10^{12}$ lượt/giây, 6 TB, dưới 10 ms (giả định)."; dòng 2 rút thành "Trả tối đa $K$ điểm; đo độ thu hồi." Âm tiết 59/60.
- **H14:** ngoặc định nghĩa đồ thị Delaunay "(nối điểm có ô Voronoi kề nhau)"; tính chất tham lam tới điểm gần nhất ở ghi chú. Dòng 20 âm tiết, trang 60/60.

## Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)

Căn cứ: đặc tả sửa của điều phối viên (`spec-revise-07.md`, Phương án A) dựa trên hai báo cáo rà chỉ đọc (mạch và chủ đề mạch; phong cách MAT1101 và phản biện học thuật). Mục tiêu: mỗi mạch có một chủ đề, mọi trang phục vụ chủ đề đó, mặt trang theo lối MAT1101 (mệnh đề ngắn, mỗi trang một ý, "Muốn …"/"Nhu cầu:" nêu đích, câu kết là con số hoặc kết luận có điều kiện). Mục này là bản hiện hành; các mục trên là lịch sử. Deck 65 → 63 trang: 54 trang giảng (120 phút) và 9 trang bài tập (60 phút); bảy mạch 11/8/10/12/7/6/9.

### Bản đồ mạch

| N | Tên (khớp P04 và trang tiêu đề) | Loại | Chức năng | Đầu vào | Đầu ra | Trang tiêu đề mạch | Trang | Phút |
|---:|---|---|---|---|---|---|---|---:|
| 1 | Bài toán hàng xóm gần đúng | giới thiệu + khái niệm/mô hình | nêu kho $10^{10}$ véc-tơ, đặc tả tìm đúng và tìm gần đúng, độ thu hồi, bốn trục, mô hình hai thừa số | Bài 06: LSH chỉ xác minh ứng viên cùng thùng | $N_K(q)$, $\widehat N_K(q)$, recall@K, "chi phí ≈ số véc-tơ được đo × chi phí một phép đo", cột "Lưu véc-tơ gốc" | P00 (bìa) | P00, P03, P02, P04, P05, P01, A00, A00B, A01, A02, A03 | 20,5 |
| 2 | Tìm kiếm trên đồ thị lân cận | thuật toán | giảm thừa số thứ nhất trên một đồ thị: tham lam, chùm, SEARCH-LAYER, bất biến | mô hình hai thừa số; $N=10^{10}$ | SEARCH-LAYER đúng trên tập đỉnh đã thấy $V$; số bước còn tăng theo khoảng cách | `HT`, `id="mach-2"` | HT, H00, H01, H03, H03B, H04, H05, H06 | 19 |
| 3 | Đồ thị thế giới nhỏ phân tầng (HNSW) | thuật toán + chi phí | cạnh dài, tầng, truy vấn, phân phối tầng, chèn, tham số, chi phí | SEARCH-LAYER và bất biến; vết tham lam 6 bước | số phép đo tăng theo $\log N$ dưới giả thiết Delaunay; bộ nhớ ≈125,5 TB, ≈98% là véc-tơ gốc | `NT` (mới), `id="mach-3"` | NT, H06B, H07, H09, H08, H10, H10B, H12, H14, H13 | 23 |
| 4 | Lượng tử hóa tích (PQ) | khái niệm + thuật toán + chi phí | thay véc-tơ bằng mã ngắn, khoảng cách qua bảng tra | véc-tơ gốc chiếm 98% bộ nhớ HNSW | mã 512 byte (5,12 TB); ADC; quét đủ vẫn chấm $10^{10}$ mã | `QT`, `id="mach-4"` | QT, Q00, Q02, Q03, Q04, Q05, Q07, Q06, Q08, Q09, Q11, Q10 | 28 |
| 5 | Tệp đảo kết hợp PQ (IVF-PQ) | thuật toán + chi phí | chỉ chấm mã trong vài danh sách gần $q$ | PQ quét đủ chấm mọi mã | $\approx3{,}63\cdot10^9$ thao tác (≈3,6 ms), $8+512$ byte mỗi phần tử | `IT`, `id="mach-5"` | IT, I00, I01, I02, I04, I05, I03 | 17 |
| 6 | Tổng kết và tự kiểm tra | tổng kết | đối chiếu giả thiết, bảo đảm, chi phí; trả lời vấn đề trung tâm | bốn cấu trúc, cùng mô hình đếm | IVF-PQ khả thi có điều kiện (6 TB, 10 ms giả định) | `CT`, `id="mach-6"` | CT, C03, C00, C04, C01, C05 | 12,5 |
| 7 | Bài tập thực hành | thực hành | đo lại công thức PQ, IVF-PQ trên sổ Princeton lớp 8 | công thức PQ, ADC, chi phí IVF-PQ | ba phiếu đo đối chiếu dự đoán | `RT`, `id="mach-7"` | RT, R00, R01, R02, R04–R08 | 60 |

Tổng phần giảng 20,5 + 19 + 23 + 28 + 17 + 12,5 = 120 phút; bài tập 60 phút. Mạch 1 không có trang tiêu đề riêng; bìa là trang tiêu đề của mạch mở đầu (`AGENTS.md` §"Trang tiêu đề mạch"). `span.strand-number` của HT…RT là 2…7, khớp `#/2`…`#/7` (kiểm bằng trình duyệt: NT hiện "3 . 1").

### Trang tiêu đề mạch

| Mã | Tên | Vị trí | Dòng dẫn (âm tiết) | Ghi chú: kế thừa → nhiệm vụ → giao | Phút | Quyết định |
|---|---|---|---|---|---:|---|
| AT | (Bài toán hàng xóm gần đúng) | — | — | — | — | `bỏ`: A00–A03 là phần "bài toán" mà Bài 03, Bài 06 đặt trong mạch mở đầu; dòng dẫn cũ hứa "tránh quét" mà mạch không tránh phép quét nào |
| HT | Tìm kiếm trên đồ thị lân cận | điểm vào mạch 2, trước H00 | "Muốn đo ít véc-tơ mà vẫn tới điểm gần $q$, phải đi trên đồ thị lân cận và giữ nhiều hướng." (20) | mô hình hai thừa số, quét đủ đo $10^{10}$ véc-tơ → tham lam, chùm, SEARCH-LAYER, bất biến → "đúng trên tập đỉnh đã thấy, số bước còn tăng theo khoảng cách", giới hạn dẫn tới cạnh dài (92 âm tiết) | 0,5 | `sửa`: tên, dòng dẫn, từ khóa, `id="mach-2"`; ghi chú bỏ "chọn lân cận đa dạng" và cụm "chi phí hoàn tất cấu trúc" |
| NT | Đồ thị thế giới nhỏ phân tầng (HNSW) | điểm vào mạch 3, trước H06B | "Muốn tới vùng gần $q$ sau ít bước, phải đặt các tầng thưa có cạnh dài phía trên đồ thị chứa mọi điểm." (22) | SEARCH-LAYER và bất biến; số bước tăng theo khoảng cách → cạnh dài, tầng, truy vấn, rút tầng, chèn, đếm → "≈125,5 TB, ≈98% là véc-tơ gốc, nên véc-tơ cần được nén" (93 âm tiết; khớp H13: $12\,288/12\,553\approx0{,}979$) | 0,5 | `thêm`: tách mạch HNSW cũ (hai câu hỏi trung tâm trong 17 trang). Mã `NT` theo đặc tả; tên khác tiêu đề H06B. Ngoài chu trình khái niệm |
| CT | Tổng kết và tự kiểm tra | điểm vào mạch 6 | giữ | ghi chú nêu bất biến SEARCH-LAYER và số phép đo đồ thị nhiều tầng thay "phân phối tầng" (88 âm tiết) | 0,5 | `sửa` (ghi chú) |
| QT, IT, RT | giữ | giữ | giữ | giữ | 0,5 mỗi trang | `giữ` |

### Từng trang

Âm tiết đếm bằng `density07.py` trong scratchpad của điều phối viên (token tách theo khoảng trắng; bỏ tiêu đề, KaTeX, `pre`, `figure`, ghi chú, token thuần số trong ô bảng). Cột "Dòng" đếm `p`, `li`, hộp Câu hỏi và hàng `tbody`, không tính hàng tiêu đề bảng. Cột "Trần" là trần âm tiết áp dụng sau đợt sửa.

| # | Mã | Tiêu đề | Mạch | Quyết định | Âm tiết trước → sau | Trần | Dòng | Phút | Lý do và kết nối |
|---:|---|---|---:|---|---|---:|---:|---:|---|
| 1 | P00 | Chỉ mục hàng xóm gần đúng | 1 | `sửa` | 51 → 50 | bìa | 4 | 0,5 | luận đề không dùng viết tắt HNSW trước khai triển: "Đồ thị nhiều tầng bớt số phép đo, mã ngắn bớt chi phí mỗi phép đo; đổi lại, có thể sót hàng xóm thật." (24 token, trần 25) |
| 2 | P03 | Tiên quyết và quy ước | 1 | `sửa` | 61 → 45 | 60 | 4 | 1,5 | bỏ dòng "Ký hiệu: HNSW là …" (khai triển một viết tắt, không phải ký hiệu); dòng Nhắc lại khai triển LSH; "có thể bỏ sót" sang ghi chú; ghi chú bỏ câu lấy tài liệu làm chủ ngữ |
| 3 | P02 | Mục tiêu học tập | 1 | `sửa` | 50 → 49 | 80 | 3 | 1 | mục tiêu 2 "tìm kiếm trên đồ thị" (không dùng HNSW trước H07); ghi chú đánh số lại câu tự kiểm |
| 4 | P04 | Nội dung | 1 | `sửa` | 53 → 57 | 80 | 8 | 0,5 | bảy mạch mới; ghi chú một câu mỗi mạch |
| 5 | P05 | Vấn đề trung tâm | 1 | `sửa` | 61 → 54 | 60 | 5 | 1,5 | Nhu cầu nêu đích và ngân sách, không lặp số quét đủ của P01; bốn dòng trả lời mạch 2–5; dòng "đầu ra gần đúng" bỏ vì trang lên 63 (đặc tả cho phép bỏ khi vượt) |
| 6 | P01 | Ví dụ: truy hồi ngữ nghĩa trên mười tỷ véc-tơ | 1 | `giữ` | 37 → 37 | 60 | 4 | 3 | câu hỏi 30,7 giây giữ vì P05 không còn in số này |
| 7 | A00 | Bài toán $K$ hàng xóm gần nhất | 1 | `tách` | 60 → 37 | 60 | 3 | 3,5 | một đặc tả mỗi trang; Nhu cầu nêu đích ($3{,}07\cdot10^{13}$ lượt tọa độ); ghi chú nêu phép đếm $\Theta(ND)$ và phá hòa |
| 8 | A00B | Tìm hàng xóm gần đúng | 1 | `thêm` (tách từ A00) | — → 41 | 60 | 3 | 2 | Định nghĩa. ANN, câu cơ chế, Lưu ý thiếu điểm; ghi chú hai nguồn sai số và chữ "tối đa". Tên khác tên mạch 1 trên P04 |
| 9 | A01 | Độ thu hồi tại $K$ | 1 | `sửa` | 34 → 36 | 60 | 4 | 3 | "Định nghĩa. … là tỷ lệ …:" đứng trước công thức |
| 10 | A02 | Bốn trục đánh giá chỉ mục | 1 | `sửa` | 79 → 50 | 60 | 5 | 2 | câu hỏi A/B làm nhu cầu, đặt đầu trang, ≤ 20 âm tiết ("Nêu điều kiện để chọn B."); cột "Giữ cố định khi so sánh" sang ghi chú; bỏ ngoại lệ trần 80 |
| 11 | A03 | Hai cách giảm chi phí truy vấn | 1 | `sửa` | 57 → 43 | 60 | 5 | 2 | cột "Cách giảm" (lặp P05) thành "Lưu véc-tơ gốc" có/có/không/không; hàng "HNSW" thành "Đồ thị lân cận" (chưa khai triển HNSW); ghi chú bỏ câu chung "Cả ba đều đổi …", thêm $4ND$ byte = 122,88 TB. Trang cuối mạch 1 |
| 12 | HT | 2. Tìm kiếm trên đồ thị lân cận | 2 | `sửa` | 33 → 34 | dẫn ≤ 25 | 2 | 0,5 | xem bảng trang tiêu đề mạch |
| 13 | H00 | Đồ thị lân cận | 2 | `sửa` | 48 → 51 | 60 | 3 | 1 | Nhu cầu có số và giới hạn của quét đủ ($N=10^{10}$) |
| 14 | H01 | Tìm kiếm tham lam | 2 | `sửa` | 40 → 46 | 60 | 6 | 4 | Kết luận giải nghĩa "cực tiểu cục bộ (không lân cận nào gần $q$ hơn)" |
| 15 | H03 | Tìm kiếm chùm | 2 | `sửa` | 53 → 48 | 60 | 3 | 2 | "Muốn tới $z{:}1$ … phải giữ nhánh $s$ chưa đi."; "mở" giải nghĩa trên mặt trang; dòng "Dừng khi …" sang ghi chú (giả mã H05 có); ghi chú 174 → 141 |
| 16 | H03B | Ví dụ: tìm kiếm chùm trên đồ thị bảy đỉnh | 2 | `sửa` | 35 → 28 | 60 | 7 | 2 | bỏ câu tả bố cục bảng (sang ghi chú); không thêm "Diễn giải:" vì trang đã 8 dòng kể cả hàng tiêu đề |
| 17 | H04 | Thuật toán: SEARCH-LAYER | 2 | `sửa` | 43 → 41 | 60 | 4 | 2 | "Ký hiệu: $V$ là tập đỉnh đã thấy; $C,W\subseteq V$." không lặp định nghĩa $C$, $W$ |
| 18 | H05 | Thuật toán: SEARCH-LAYER | 2 | `giữ` | 8 → 8 | 60 | 1 | 4 | +0,5 phút đọc giả mã |
| 19 | H06 | Tính đúng: SEARCH-LAYER | 2 | `sửa` | 54 → 41 | 60 | 5 | 3,5 | bỏ dòng "Điều kiện dừng" (phương án mật độ thấp hơn: −13 so với −5 nếu bỏ dòng Ví dụ.); tính kết thúc vẫn ở ghi chú H05, H06; dòng Ví dụ. $ef=2$ giữ vì đọc hình `do-thi-ef2.svg` và dẫn sang NT ($z\notin V$). Trang cuối mạch 2; +0,5 phút |
| 20 | NT | 3. Đồ thị thế giới nhỏ phân tầng (HNSW) | 3 | `thêm` | — → 32 | dẫn ≤ 25 | 2 | 0,5 | điểm vào mạch 3; xem bảng trang tiêu đề mạch |
| 21 | H06B | Ví dụ: cạnh dài trên mười hai điểm thẳng hàng | 3 | `sửa` | 37 → 33 | 60 | 3 | 2 | "Nhu cầu: đi tới $q$ sau ít bước tham lam khi $q$ xa điểm vào."; vế "chỉ có cạnh ngắn …" sang ghi chú (phương án mật độ thấp hơn); ghi chú bỏ "zoom-out/zoom-in" |
| 22 | H07 | Đồ thị nhiều tầng | 3 | `sửa` | 47 → 47 | 60 | 4 | 2,5 | khai triển HNSW ở lần dùng đầu trong nội dung: "Đồ thị thế giới nhỏ phân tầng (Hierarchical Navigable Small World, HNSW) gồm nhiều tầng lồng nhau."; ghi chú bỏ đoạn lặp vết của H09 (178 → 150) |
| 23 | H09 | Thuật toán: truy vấn HNSW | 3 | `giữ` | 28 → 28 | 60 | 3 | 3 | — |
| 24 | H08 | Phân phối tầng của điểm mới | 3 | `sửa` | 54 → 57 | 60 | 6 | 3 | tiêu đề gọi tên kết quả; dòng công thức có động từ "Đặt …, với …" |
| 25 | H10 | Ví dụ: chèn một điểm vào đồ thị ba tầng | 3 | `sửa` | 37 → 36 | 60 | 5 | 3 | dữ kiện + "Xác định lân cận của $x$ ở tầng 1 và tầng 0."; Kết luận nêu kết quả đọc từ bảng: $p2,p4$ ở tầng 1, $p3,p2$ ở tầng 0; ghi chú 174 → 145 |
| 26 | H10B | Thuật toán: chèn HNSW | 3 | `sửa` | 15 → 29 | 60 | 3 | 4 | câu dẫn "Chèn là truy vấn với $x$, rồi nối …" chuyển từ H10; ghi chú bỏ câu cấu hình và câu nhắc ví dụ, giữ tham chiếu Thuật toán 4 và chỉ sang ghi chú bài giảng (188 → 130); +1 phút |
| — | H11 | Chọn lân cận đa dạng | 3 | `bỏ` | 36 → — | — | — | −2,5 | phần tùy chọn của thuật toán (`AGENTS.md`: đặt trong ghi chú bài giảng); không mục tiêu nào đòi; không trang sau nào dùng. Nội dung giữ ở ghi chú bài giảng §5 cùng `img/lec-07/lan-can-da-dang.svg` (không xóa tệp) |
| 27 | H12 | Ba tham số của HNSW | 3 | `sửa` | 65 → 56 | 60 | 4 | 2 | cột cuối rút thành cụm ngắn, giải thích chuyển vào ghi chú; bỏ ngoại lệ trần 80 |
| 28 | H14 | Chi phí: truy vấn HNSW | 3 | `sửa` | 60 → 56 | 60 | 4 | 1,5 | đặt trước H13; "Mệnh đề. Với giả thiết trên, số phép đo trung bình tăng theo $\log N$."; "Lưu ý: … trường hợp xấu thăm cả tầng."; bỏ dòng Kết luận (vế bộ nhớ thuộc H13); nguồn Malkov–Yashunin chỉ trong ghi chú; ghi chú bỏ câu trỏ mặt trang |
| 29 | H13 | Chi phí: bộ nhớ HNSW | 3 | `giữ` (đổi chỗ) | 53 → 53 | 80 | 5 | 1,5 | trang cuối mạch 3, kết "véc-tơ gốc chiếm khoảng 98% bộ nhớ" đúng câu Q00 nhận vào |
| 30 | QT | 4. Lượng tử hóa tích (PQ) | 4 | `giữ` | 39 → 39 | dẫn ≤ 25 | 2 | 0,5 | — |
| 31 | Q00 | Lượng tử hóa véc-tơ | 4 | `sửa` | 47 → 52 | 60 | 6 | 3,5 | "Nhu cầu: lưu mỗi véc-tơ bằng ít byte hơn; véc-tơ gốc chiếm 98% bộ nhớ HNSW." (bỏ 122,88 TB để giữ mật độ) |
| 32 | Q02 | Thuật toán: mã hóa VQ | 4 | `giữ` | 36 → 36 | 60 | 4 | 2 | — |
| 33 | Q03 | Chi phí: một bộ mã lớn | 4 | `sửa` | 69 → 62 | 80 | 6 | 2 | dòng Mô hình chỉ còn mô hình (dữ kiện ví dụ đã ở tiêu đề cột và ghi chú); Kết luận có số: "với $D=128$, mã 64 bit … cần $2^{64}$ tâm, khoảng $9{,}4\cdot10^{21}$ byte" ($2^{64}\cdot128\cdot4\approx9{,}44\cdot10^{21}$); bỏ "khổng lồ" |
| 34 | Q04 | Mã PQ và tái dựng | 4 | `sửa` | 42 → 46 | 60 | 4 | 3 | "Định nghĩa. Lượng tử hóa tích (PQ) là VQ riêng trên từng đoạn …" trong `p`; gạch "Tương tự VQ, nhưng …" thành "Mỗi đoạn $j$ có bộ mã con riêng …" vì định nghĩa đã chứa phép so với VQ |
| 35 | Q05 | Ví dụ: mã hóa PQ hai đoạn | 4 | `giữ` | 25 → 25 | 60 | 5 | 3 | — |
| 36 | Q07 | Chi phí: kích thước mã và bộ mã PQ | 4 | `sửa` | 46 → 43 | 80 | 5 | 3 | Kết luận một ý: "cùng $2^{64}$ mã, bộ mã PQ nhỏ hơn bộ mã VQ $2^{56}$ lần" ($2^{64}\cdot128/(2^8\cdot128)$); cấu hình kho mở đầu chuyển sang Q10 |
| 37 | Q06 | Ví dụ: khoảng cách bất đối xứng của mã $(0,1)$ | 4 | `sửa` | 22 → 27 | 60 | 5 | 3 | thêm "Nhu cầu: kho chỉ còn mã; cần ước lượng $d(q,x)$ mà không dùng $x$."; gộp dữ kiện $q$ vào dòng yêu cầu để giữ 6 dòng |
| 38 | Q08 | Khoảng cách bất đối xứng (ADC) | 4 | `sửa` | 51 → 44 | 60 | 4 | 2 | bỏ gạch lặp Q06; gạch còn lại thành `p` |
| 39 | Q09 | Bảng tra khoảng cách | 4 | `giữ` | 22 → 22 | 60 | 5 | 2 | — |
| 40 | Q11 | Chi phí: bảng tra và chấm mã | 4 | `giữ` | 57 → 57 | 80 | 5 | 1 | — |
| 41 | Q10 | Chi phí: PQ quét đầy đủ | 4 | `sửa` | 61 → 57 | 80 | 5 | 3 | dòng đầu "Mô hình:" kèm cấu hình ($m=512$ đoạn 6 chiều, $b=8$); một yếu tố chốt: giữ Kết luận giới hạn (I00 nhận vào), câu hỏi 5,12 giây chuyển thành phép tính trong ghi chú |
| 42 | IT | 5. Tệp đảo kết hợp PQ (IVF-PQ) | 5 | `giữ` | 36 → 36 | dẫn ≤ 25 | 2 | 0,5 | — |
| 43 | I00 | Tệp đảo (IVF) | 5 | `sửa` | 50 → 51 | 60 | 4 | 2,5 | "Nhu cầu: chấm ít hơn $10^{10}$ mã mỗi truy vấn; PQ quét đủ chấm mọi mã."; dòng Ví dụ. rút |
| 44 | I01 | Chọn danh sách cần mở | 5 | `sửa` | 15 → 28 | 60 | 7 | 3 | câu dẫn trước công thức gán ô |
| 45 | I02 | Mã hóa phần dư | 5 | `sửa` | 37 → 43 | 60 | 5 | 3 | "Phần dư có bình phương chuẩn trung bình nhỏ hơn của $y$" khớp ghi chú; ghi chú 156 → 147 |
| 46 | I04 | Thuật toán: truy vấn IVF-PQ | 5 | `giữ` | 32 → 32 | 60 | 2 | 3 | +0,5 phút |
| 47 | I05 | Ví dụ: truy vấn IVF-PQ | 5 | `giữ` | 26 → 26 | 60 | 5 | 2 | +0,5 phút |
| 48 | I03 | Chi phí: truy vấn IVF-PQ | 5 | `sửa` | 67 → 56 | 80 | 7 | 3 | Mô hình 17 âm tiết; Kết luận một ý (≈1400 lần); 5,2 TB giữ ở C00, C04 và ghi chú |
| 49 | CT | 6. Tổng kết và tự kiểm tra | 6 | `sửa` | 41 → 41 | dẫn ≤ 25 | 2 | 0,5 | ghi chú nhắc hai mạch đồ thị |
| 50 | C03 | Kết quả và giả thiết không được bỏ | 6 | `sửa` | 80 → 75 | 80 | 6 | 2 | bỏ hàng "Phân phối tầng" (kết quả phụ, còn ở H08 và ghi chú bài giảng) |
| 51 | C00 | Thuật toán, bảo đảm và chi phí | 6 | `sửa` | 78 → 78 | 80 | 5 | 3 | ghi chú mở bằng nội dung bảng, không mở bằng câu phủ định (172 → 146) |
| 52 | C04 | Câu trả lời cho vấn đề trung tâm | 6 | `sửa` | 72 → 57 | 80 | 5 | 2,5 | bỏ gạch nhắc đặc tả; ba dòng HNSW, PQ, IVF-PQ khớp P05 (dòng HNSW trả lời chung cho hai mạch đồ thị); +0,5 phút |
| 53 | C01 | Câu hỏi tự kiểm tra | 6 | `gộp` (nhận C02) | 54 → 53 | 60 | 4 | 4 | ba câu: $ef$ và bất biến (câu 2 cũ), bộ nhớ HNSW so 64 GB (câu 3 cũ, viết lại ≤ 20 âm tiết), số mã IVF-PQ với giả thiết cân bằng (câu 6 cũ); câu PQ $D=960$ không vừa trần 60 (61–63 âm tiết) nên chỉ còn ở ghi chú bài giảng; lời giải trùng ghi chú bài giảng §12 |
| — | C02 | Câu hỏi tự kiểm tra | 6 | `bỏ` (gộp vào C01) | 57 → — | — | — | −3,5 | câu 4 trùng Q07 và R01, câu 5 trùng thao tác Q09; câu 6 chuyển sang C01 |
| 54 | C05 | Nguồn và tài liệu đọc | 6 | `sửa` | 79 → 69 | 80 | 5 | 0,5 | dòng nguồn HNSW rút còn 12 âm tiết (tên đầy đủ của bài báo chuyển vào ghi chú); ngoại lệ: trần 80 của trang tổng kết, xem dưới |
| 55 | RT | 7. Bài tập thực hành | 7 | `giữ` | 41 → 41 | dẫn ≤ 25 | 2 | 0,5 | — |
| 56 | R00 | Sổ thực hành và dữ liệu | 7 | `giữ` | 49 → 49 | 80 | 8 | 0 | — |
| 57 | R01 | Bài tập: mã và tái dựng PQ (a) | 7 | `sửa` | 49 → 48 | 80 | 6 | 5,5 | "Câu hỏi:" ngay dưới nhãn Thực hành, trước dữ kiện |
| 58 | R02 | Bài tập: mã và tái dựng PQ (b) | 7 | `gộp` (nhận R03) | 39 → 39 | 80 | 3 | 14 | "Câu hỏi:" lên đầu; ba điều kiện khớp của R03 thành phần giải thích trong ghi chú; chấm nhiệm vụ 1: bảng 3 điểm (R01), biểu thức và `True` 7 điểm, vi phạm một điều kiện 4 điểm |
| — | R03 | Bài tập: mã và tái dựng PQ (c) | 7 | `bỏ` (gộp vào R02) | 73 → — | — | — | −5 | nhiệm vụ giải thích không có trong sổ nguồn ô 96–97 và không phải số đo |
| 59 | R04 | Bài tập: cùng ngân sách 6 byte (a) | 7 | `sửa` | 49 → 49 | 80 | 6 | 10 | "Câu hỏi:" lên đầu |
| 60 | R05 | Bài tập: cùng ngân sách 6 byte (b) | 7 | `sửa` | 66 → 66 | 80 | 5 | 10 | "Câu hỏi: từ số đo MSE và thời gian đã ghi, trả lời ba ý sau." (bỏ "trang (a)", "của mình") |
| 61 | R06 | Bài tập: chỉ mục IVF-PQ (a) | 7 | `sửa` | 41 → 37 | 80 | 3 | 6 | "Câu hỏi:" lên đầu, gộp câu "Chạy ô 149–151 …" |
| 62 | R07 | Bài tập: chỉ mục IVF-PQ (b) | 7 | `sửa` | 33 → 33 | 80 | 3 | 9 | "Câu hỏi:" lên trước mã |
| 63 | R08 | Bài tập: chỉ mục IVF-PQ (c) | 7 | `sửa` | 42 → 42 | 80 | 7 | 5 | "Câu hỏi:" lên trước bảng |

Phút: phần giảng 120 (AT −0,5, H11 −2,5, C02 −3,5; NT +0,5, A00B +2, H05 +0,5, H06 +0,5, H10B +1, I04 +0,5, I05 +0,5, C04 +0,5, C01 +0,5); bài tập 0,5 + 0 + 5,5 + 14 + 10 + 10 + 6 + 9 + 5 = 60.

### Lựa chọn khi đặc tả cho hai phương án

- **H06:** bỏ dòng "Điều kiện dừng" thay vì dòng "Ví dụ." (mật độ thấp hơn: 54 → 41 thay vì 49).
- **H06B:** vế "chỉ có cạnh ngắn …" sang ghi chú thay vì thành dòng giới hạn có số.
- **A02:** đưa câu hỏi A/B lên làm nhu cầu ở đầu trang thay vì thêm dòng "Muốn so sánh …" (thêm dòng làm trang 66 âm tiết, 7 dòng).
- **Q03:** không thêm dòng "Ví dụ." riêng; dữ kiện $D=128$, $k=2^{64}$ đã ở tiêu đề cột bảng.
- **Q10:** giữ Kết luận giới hạn, chuyển câu hỏi thời gian vào ghi chú (−17 âm tiết).
- **P05:** bỏ dòng "đầu ra gần đúng" vì trang lên 63.
- **C04:** bỏ hẳn gạch đặc tả thay vì rút.
- **C05:** rút dòng nguồn HNSW thay vì giữ tên bài báo trên mặt trang.
- **C01:** ba câu thay vì bốn (câu PQ làm trang vượt 60).

### Mật độ và ngoại lệ còn lại

Không trang trần 60 nào vượt 60 (cao nhất H08 57, Q00 52, H00 51, I00 51). Trang trên 60 đều thuộc nhóm trần 80: Q03 62 (chi phí), C03 75, C00 78 (tổng kết), R05 66 (đề recitation) và C05 69. **Ngoại lệ C05:** trang "Nguồn và tài liệu đọc" thuộc mạch tổng kết; ba dòng nguồn giữ tên tài liệu tiếng Anh (PQ, MMDS) và tên lớp học, mỗi dòng ≤ 20 âm tiết; trần áp dụng 80, trang 69. Hai trang trước đây dựa vào ngoại lệ "bảng so sánh" nay dưới 60: A02 50, H12 56. Không dòng chữ nào vượt 20 âm tiết, trừ câu luận đề bìa (24, trần 25) và dòng dẫn trang tiêu đề mạch (18–23, trần 25).

**Ngoại lệ dòng** (trần 6; bảng vết, bảng tính và bảng chi phí tới 8, đếm không tính hàng tiêu đề): P04 8 (bảy mạch và Đọc trước), R00 8 (hai bảng dữ kiện sổ thực hành), H03B 7 (vết 5 hàng), I01 7 (câu dẫn, công thức, bảng xếp tâm 4 hàng, câu hỏi), I03 7 (chi phí), R08 7 (phiếu 5 hàng). Ghi chú diễn giả trên 150 âm tiết chỉ ở trang chứng minh, tính đúng, đọc giả mã hoặc lời giải (H05 175, H06 156, H08 156, I01 154, C01 170, R02 196, R05 168, R07 158, R08 152, P01 163), cùng P03 171, Q10 152 (mức `nhẹ`).

### Kiểm tra theo mạch và câu tự kiểm

- Mạch 1: câu hỏi ở P01, A01, A02. Mạch 2: H03B. Mạch 3: H12. Mạch 4: Q00 (câu hỏi Q10 chuyển thành phép tính trong ghi chú). Mạch 5: I01, I05. Mạch 6: C01, lời giải trong ghi chú. Mạch 7: tám trang bài tập theo sổ Princeton COS 597A lớp 8.
- **Ánh xạ câu tự kiểm tra → mục tiêu (thay bản 2026-10-14):** câu 1 ($ef$, bất biến SEARCH-LAYER) → mục tiêu 2; câu 2 (bộ nhớ HNSW so 64 GB) → mục tiêu 3; câu 3 (số mã IVF-PQ, giả thiết cân bằng) → mục tiêu 3. Mục tiêu 1 được kiểm bằng câu hỏi A01 và câu hỏi recall@3 ở I05 (ghi chú P02 đã sửa theo).

### Thuật ngữ và viết tắt ở lần đầu trên mặt trang

LSH khai triển ở P03; PQ ở mục tiêu 2 (P02); IVF-PQ ở P04 ("Tệp đảo kết hợp PQ (IVF-PQ)"); HNSW khai triển ở H07. Trước H07, mặt trang chỉ dùng "HNSW" trong tên mạch 3 (P04, NT, từ khóa "Chi phí HNSW"), vì tên mạch do đặc tả chốt; P00, P02, P05, A03 đã thay "HNSW" bằng "đồ thị nhiều tầng", "đồ thị lân cận" hoặc "tìm kiếm trên đồ thị". Ghi chú P00 khai triển HNSW.

## Lượt sửa 2 sau rà lại (2026-10-16)

Căn cứ: danh sách sửa của điều phối viên sau ba báo cáo rà lại (độ chính xác, mạch, sinh viên và mật độ); không có phát hiện chặn hay nghiêm trọng. Mục này thay các ô tương ứng của mục "Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)"; số trang, thứ tự và thời lượng 120 + 60 phút không đổi.

**Đổi tên mạch 3:** "Đồ thị thế giới nhỏ phân tầng (HNSW)" trên P04, `h2` của NT và `aria-label` của section ngoài (cùng mẫu tên mạch 4, 5). H07 giữ khai triển có tiếng Anh. Trước P04, "HNSW" chỉ còn trong ghi chú P00 (đã khai triển) và ghi chú P02.

**I05** đổi tiêu đề thành "Ví dụ: truy vấn IVF-PQ" (trang vết chạy, không phải trang đặc tả).

### Mục storyboard đầy đủ cho trang mới

| Trường | A00B — Tìm hàng xóm gần đúng | NT — 3. Đồ thị thế giới nhỏ phân tầng (HNSW) |
|---|---|---|
| Mạch, vị trí | mạch 1, sau A00, trước A01 | mạch 3, **điểm vào mạch 3**, sau H06, trước H06B; `id="mach-3"` |
| Mục đích | hình thức hóa bài toán gần đúng tách khỏi bài toán tìm đúng; nêu hai nguồn thiếu điểm | nêu nhu cầu của mạch: ít bước khi $q$ xa điểm vào; báo các khối của mạch |
| Hành động sinh viên | đối chiếu đầu ra $\widehat N_K(q)$ với $N_K(q)$ của A00; nêu vì sao chỉ mục có thể thiếu điểm | đọc dòng dẫn và từ khóa; nối giới hạn của SEARCH-LAYER (H06) với ý tưởng tầng thưa |
| Đối tượng trung tâm | $\widehat N_K(q)\subseteq Y$, tối đa $K$ điểm | tầng thưa có cạnh dài phía trên đồ thị chứa mọi điểm (tầng 0) |
| Dữ kiện, ký hiệu kế thừa | $Y$, $q$, $K$, $d$ (P03, A00); $N_K(q)$ và quy tắc phá hòa theo chỉ số (A00) | SEARCH-LAYER, bất biến "đúng trên $V$" (H04–H06); vết $ef=2$ không tới $z$ |
| Kiến thức đầu vào | đặc tả đầu vào/đầu ra; tập con | tìm kiếm tham lam và tìm kiếm chùm trên một đồ thị |
| Sản phẩm học tập | phát biểu được đặc tả tìm gần đúng và hai nguồn sai số (đo một phần kho, đo xấp xỉ) | nêu được mạch 3 giải quyết giới hạn nào của mạch 2 |
| Bằng chứng kiểm | câu hỏi A01 (recall@5 $=2/5$) dùng $\widehat N_K$, $N_K$; Lưu ý trên mặt trang dẫn sang độ thu hồi | H06B (6 → 3 bước), câu hỏi H12, mệnh đề H14, bộ nhớ H13 |
| Ghi chú | 119 âm tiết: hai nguồn thiếu điểm, chữ "tối đa", dẫn sang phép đo chất lượng | 98 âm tiết: kế thừa → nhiệm vụ (hai câu: đặt tầng và truy vấn; rút tầng, chèn, đếm số phép đo rồi bộ nhớ) → giao "≈125,5 TB, ≈98% véc-tơ gốc" |
| Phút; quyết định | 2; `thêm` (tách từ A00) | 0,5; `thêm` |

### Quyết định lượt 2

Âm tiết đếm bằng `density07.py`; "trước" là bản sau lượt 1.

| Mã | Quyết định | Âm tiết trước → sau | Trần | Thay đổi và lý do |
|---|---|---|---:|---|
| H03 | `sửa` | 48 → 51 | 60 | $C$ "chứa các đỉnh từng vào $W$ nhưng chưa mở", khớp giả mã H05 (đỉnh bị loại khỏi phép thử $W$ không vào $C$; ví dụ $w{:}9$ ở câu tự kiểm 1); $ef$ gọi tên "bề rộng chùm" ở lần dùng đầu; ghi chú thêm "đỉnh bị đẩy khỏi $W$ vẫn ở lại $C$" |
| H03B | `sửa` | 28 → 42 | 60 | hộp câu hỏi gộp thành một câu (13 âm tiết) và thêm "Gợi ý:" quy tắc dừng (15 âm tiết), đủ để giải câu hỏi $ef=2$ trên mặt trang. Chọn hộp H03B thay vì thêm dòng dừng vào H03 vì H03 sẽ lên khoảng 64. Hộp gồm hai câu, mỗi câu ≤ 20 âm tiết; bộ đếm tính cả hộp là một dòng 28 âm tiết |
| H10 | `sửa` | 36 → 51 | 60 | dòng đầu nêu ý tưởng chèn trước ví dụ; $efConstruction$ giải nghĩa "bề rộng chùm khi chèn"; 6 dòng (bảng vết 3 hàng) |
| H10B | `sửa` | 29 → 15 | 60 | bỏ câu dẫn (đã ở H10; Đầu vào/Đầu ra đủ); giả mã: $ep$ luôn là tập (`ep ← {điểm vào}`, pha 1 `ep ← {…}`), biến `e ∈ R` đổi thành `y ∈ R`; ghi chú nêu kiểu $ep$ và "giữ $M_{max}(\ell_c)$ lân cận gần nhất" (151 âm tiết) |
| NT | `sửa` | 32 → 35 | dẫn ≤ 25 | tên mạch đầy đủ; dòng dẫn một nghĩa "… đặt các tầng thưa có cạnh dài phía trên tầng 0." (18); từ khóa "Tham số và chi phí"; ghi chú tách hai câu, thứ tự số phép đo rồi bộ nhớ |
| P04 | `sửa` | 57 → 60 | 80 | tên mạch 3 đầy đủ |
| H06B | `sửa` | 33 → 39 | 60 | Nhu cầu nêu kết quả kế thừa và giới hạn: "SEARCH-LAYER đúng trên đỉnh đã thấy, nhưng với cạnh ngắn, số bước tăng theo khoảng cách tới $q$." (19); dữ kiện "$p1,\ldots,p11$ ở $1,\ldots,11$" (cùng ký hiệu p4 của SVG) |
| HT | `sửa` | 34 → 34 | dẫn ≤ 25 | từ khóa `SEARCH&#8209;LAYER` (không ngắt dòng); ghi chú bỏ câu trừu tượng về "đồ thị bảy đỉnh giảm thừa số" và chỉ giao kết quả mạch 2 thật sự tạo ra (đúng trên $V$, vùng chưa thấy có thể chứa đỉnh gần hơn) (80 âm tiết) |
| H14 | `sửa` | 56 → 55 | 60 | "số phép đo trung bình là $O(\log N)$" (bài báo cho cận trên); ghi chú cùng cách nói |
| C03 | `sửa` | 75 → 76 | 80 | hàng HNSW: "Delaunay chính xác", "số phép đo trung bình $O(\log N)$"; hàng độ thu hồi "phá hòa theo chỉ số" |
| Q00 | `sửa` | 52 → 53 | 60 | "khoảng 98%" ($12\,288/12\,553\approx0{,}979$) |
| P05 | `sửa` | 54 → 56 | 60 | "trong kho $10^{10}$ véc-tơ" |
| A00 | `sửa` | 37 → 41 | 60 | Nhu cầu khớp bài toán tìm đúng: "một tập đúng để so mọi chỉ mục; quét đủ tạo nó bằng $3{,}07\cdot10^{13}$ lượt tọa độ"; phá hòa "chỉ số $i$ nhỏ đứng trước" (P03 đã có $y_1,\ldots,y_N$) |
| A00B | `sửa` | 41 → 48 | 60 | Lưu ý nối "…; mức thiếu đo bằng độ thu hồi." dẫn sang A01 |
| A03 | `sửa` | 43 → 45 | 60 | "Mô hình: chi phí truy vấn ≈ …" |
| H08 | `sửa` | 57 → 59 | 60 | Nhu cầu "khi chèn, mỗi điểm cần một tầng tối đa …" |
| Q03 | `sửa` | 62 → 63 | 80 | Kết luận có điều kiện, không lặp ô bảng: "với $D=128$, mã 64 bit không lấy được từ một bộ mã duy nhất"; con số $9{,}4\cdot10^{21}$ byte ở bảng và ghi chú |
| I02 | `sửa` | 43 → 38 | 60 | "Trung bình $\|r(y)\|^2$ nhỏ hơn trung bình $\|y\|^2$" thay câu cụt; thêm $y_8=(6{,}5;\ 2{,}5)$ trên mặt trang; ghi chú nêu điều kiện (tâm thô là trọng tâm ô, k-means hội tụ, trên tập huấn luyện) |
| I05 | `sửa` | 26 → 26 | 60 | tiêu đề "Ví dụ: truy vấn IVF-PQ" |
| C00 | `sửa` | 78 → 79 | 80 | ô LSH ghi "($b$ dải)" để tách khỏi $b$ bit của PQ |
| Ghi chú | `sửa` | — | — | P03 giải nghĩa họ $(d_1,d_2,p_1,p_2)$-nhạy cảm, $b$ dải, $r$ hàm (181 âm tiết); P00 khai triển PQ và IVF-PQ (151); H00 dùng $N\cdot(4D+4g)$ thay $s$ (trùng tên đỉnh $s$); A00 phá hòa theo chỉ số; I03 nêu khoảng 3,3 GB đọc mỗi truy vấn và giả định băng thông cỡ 1 TB/s cho con số 3,6 ms (166) |

Ghi chú trên 150 âm tiết mới phát sinh ở lượt này (mức `nhẹ`): P03 181, I02 168, I03 166, H03 154, P00 151, H10B 151; phần thêm là điều kiện hoặc giải nghĩa ký hiệu mà rà lại yêu cầu.

### Không sửa (đã quyết)

- **Chân trang ẩn ở mạch mở đầu (P00–A03):** do quy tắc CSS dùng chung `.reveal section:first-of-type.present~.footer`, cùng hành vi với mạch mở đầu của Bài 03, Bài 06; sửa CSS dùng chung nằm ngoài phạm vi.
- **P01 sát đáy khung:** không tràn (còn khoảng 12 px).
- **A03 dùng "Đồ thị lân cận"** trước H00: vai trò bản đồ xem trước của mô hình hai thừa số.
- **H04 tham số $\ell_c$:** giữ "(một đồ thị: $\ell_c=0$)"; mạch 3 dùng nhiều tầng.
- **P05 không có dòng cho mạch 1:** bỏ để giữ ≤ 60 âm tiết (bản có dòng này 63).
- **P00 luận đề:** giữ bản lượt 1.

Thời lượng không đổi: 20,5 / 19 / 23 / 28 / 17 / 12,5 = 120 phút; bài tập 60 phút.

## Lượt sửa 3 (2026-10-16)

Căn cứ: danh sách của điều phối viên sau rà lại lần 2. Tên mạch 3, dòng dẫn NT và tiêu đề I05 đã sửa tại chỗ trong các bảng hiện hành của mục "Rà chủ đề mạch…" (outline và storyboard). Số trang, thứ tự, thời lượng không đổi.

| Mã | Âm tiết trước → sau | Dòng | Thay đổi |
|---|---|---:|---|
| H03 | 51 → 56 | 4 | "$W$ gồm tối đa $ef$ (bề rộng chùm) đỉnh đã thấy gần $q$ nhất" thành gạch riêng để giữ ≤ 20 âm tiết mỗi dòng; gạch "tương tự tham lam, nhưng giữ nhiều đỉnh trong $W$" giữ phép so sánh |
| H09 | 28 → 28 | 3 | giả mã: `ep ← {điểm vào}`, `SEARCH-LAYER(q, ep, …)`, `ep ← W`; dòng Ví dụ. "$\{p8\}$, $\{p6\}$"; ghi chú: $ep$ là tập một phần tử khi xuống tầng dưới |
| H10 | 51 → 47 | 7 | ô "$ep=\{p4\}$"; dòng dữ kiện rút thành "Xác định lân cận ở tầng 1, 0." để không xuống dòng (trang sát chân); câu ý tưởng tách hai dòng: "Tầng $>\ell$: tìm $x$ với $ef=1$, không thêm cạnh." và "Tầng $\le\ell$: tìm với bề rộng chùm $efConstruction$, rồi nối $x$ với $M$ đỉnh gần nó." (7 dòng: bảng vết, trần 8) |
| H10B | 15 → 15 | 2 | ghi chú tách câu về $ep$; pha 2 chạy ở tầng $\min(\ell,L),\ldots,0$; cắt lân cận giữ $M_{max}(\ell_c)$ lân cận gần $y$ nhất ($y\in R$ của giả mã) |
| H06B | 39 → 47 | 4 | dòng kết quả kế thừa và giới hạn đứng riêng; "Nhu cầu: ít bước khi $q$ xa điểm vào." nêu đích; ghi chú mở bằng vết 6 bước, khác câu mở của ghi chú NT |
| NT | 35 → 38 | 2 | dòng dẫn "… phía trên đồ thị chứa mọi điểm." (22 âm tiết) thay "tầng 0", vì tầng 0 chỉ được định nghĩa ở H07 |
| I02 | 38 → 44 | 5 | thêm "(tâm thô là trọng tâm ô)" lên mặt trang; dòng 17 âm tiết |
| H03B | 42 → 42 | 7 | ghi chú lời giải: dừng ở lần lấy thứ tư từ $C$ ($s{:}8$ lấy ra nhưng không mở), trả $W=\{b,a\}$ (155 âm tiết, lời giải) |
| Ghi chú | — | — | HT: "tìm kiếm chùm với $ef=3$ giữ nhánh $s$ và tới được $z$"; A00B bỏ câu cuối lặp Lưu ý (119 → 100); H00: mã định danh 4 byte khi $N<2^{32}$, 8 byte với kho $10^{10}$; I03: "≈3,3 GB mã PQ và mã định danh" |

Ghi chú H10B (sửa cuối): cắt lân cận giữ $M_{max}(\ell_c)$ đỉnh gần nhất chỉ với cách chọn đơn giản (Thuật toán 3); quy tắc chọn đa dạng (Thuật toán 4) có thể giữ tập khác. Mặt trang không đổi.

C01 lời giải, ghi chú H10 và H04 không coi $ep$ là một đỉnh (đã kiểm). Glyph U+2011 ở từ khóa HT giữ nguyên (điều phối viên đã kiểm hiển thị).

## Lượt biên tập theo bản đánh giá giảng dạy (2026-10-27)

Căn cứ: bản đánh giá giảng dạy của người dùng (chép gọn trong scratchpad của điều phối viên, `guide-07.md`) và kế hoạch đã duyệt (`plan-guide-07.md`), cùng quyết định của điều phối viên: A03 viết mô hình bằng lời và gọi tên $n_c$, không đặt ký hiệu $t_d$; ghi chú bài giảng chưa sửa trong lượt này (ví dụ năm điểm và A01B sẽ đồng bộ sau mạch 7); không dùng "HNSW" trước H07, không dùng ký hiệu đoạn $x^{(j)}$ ở P03, không dùng "GPU". Mục này thay các ô tương ứng của mục "Rà chủ đề mạch và phong cách MAT1101 (2026-10-16)" và hai lượt sửa sau đó. Âm tiết, dòng và độ dài ghi chú đếm bằng `check07.py` của điều phối viên (cùng quy tắc `density07.py`).

### Mạch 1

**Thứ tự và thời lượng hiện hành:** P00, P03, P02, P04, P05, P01, A00, A00B, A01, **A01B**, A02, A03 (12 trang). Phút: P00 0,5; P03 1,5; P02 1; P04 0,5; P05 1; P01 2,5; A00 2,5; A00B 2; A01 2; A01B 2; A02 1,5; A03 2,5; tổng 19,5 (trước 20,5). Một phút bớt ra chuyển sang mạch 2 (19 → 21) theo kế hoạch §9; cho tới khi mạch 2 được sửa, tổng phần giảng tạm là 119,5 phút. Chỉ số `#/1/v` của A02, A03 dịch xuống một (A02 `#/1/11`, A03 `#/1/12`); `#/2`…`#/7` không đổi.

**Mục đầy đủ cho trang mới A01B — Độ thu hồi trung bình**

| Trường | Nội dung |
|---|---|
| Mạch, vị trí | mạch 1, sau A01, trước A02 (`#/1/10`) |
| Mục đích | mở rộng độ thu hồi từ một truy vấn sang tập truy vấn; tách hai cách hiểu dễ nhầm của con số 0,9; nêu rằng độ thu hồi không xét thứ tự |
| Hoạt động sinh viên | tính trung bình cho hai tập mười truy vấn (ví dụ trên trang và câu hỏi), so hai kiểu lỗi có cùng trung bình |
| Đối tượng trung tâm | $\overline{\operatorname{recall@K}}=\frac1{\lvert Q\rvert}\sum_{q\in Q}\operatorname{recall@K}(q)$ |
| Dữ kiện, ký hiệu kế thừa | $\operatorname{recall@K}(q)$, $N_K(q)$, $\widehat N_K(q)$ (A00, A00B, A01); ký hiệu mới $Q$ (tập truy vấn) |
| Kiến thức đầu vào | độ thu hồi của một truy vấn; trung bình cộng |
| Sản phẩm học tập | phát biểu được độ thu hồi trung bình; giải thích vì sao trung bình 0,9 không cho biết tỷ lệ truy vấn đúng hoàn toàn |
| Bằng chứng kiểm | câu hỏi trên trang (chín truy vấn đạt 1, một đạt 0: trung bình 0,9 như ví dụ); hàng "Chất lượng" của A02; $nok/100$ ở R07 là $\operatorname{recall@1}$ trung bình |
| Ghi chú | 153 âm tiết (có lời giải): lời giải, hai kiểu lỗi, tỷ lệ đúng hoàn toàn phải đếm riêng, độ thu hồi so hai tập nên bỏ qua thứ tự, liên hệ $nok/100$; nguồn Malkov và Yashunin tr.1, sổ Princeton lớp 8 ô 155 |
| Mặt trang | 58 âm tiết, 5 dòng, dòng dài nhất 17, 1 công thức hiển thị |
| Phút; quyết định | 2; `thêm`: phản ví dụ số cho cách hiểu sai "0,9 là 90% truy vấn đúng" (bản đánh giá, trang độ thu hồi); A01 không còn chỗ (36 âm tiết, hình chiếm nửa trang) |

**Các trang sửa**

| Mã | Quyết định | Âm tiết trước → sau | Dòng | Ghi chú (âm tiết) trước → sau | Phút | Thay đổi và lý do |
|---|---|---|---:|---|---:|---|
| P00 | `giữ` | 51 → 51 | 4 | 151 → 151 | 0,5 | luận đề đã nêu "bớt số phép đo … bớt chi phí mỗi phép đo … có thể sót"; ẩn dụ mục lục sách không đưa lên trang hay ghi chú |
| P03 | `sửa` | 43 → 58 | 5 | 187 → 184 | 1,5 | thêm dòng "Hàng xóm không cùng thùng với $q$ ở dải nào bị bỏ sót." (nguồn gốc của độ thu hồi < 1); dòng Nhắc lại thứ hai "… bằng tổng theo các nhóm tọa độ rời nhau" (chuẩn bị Q08, I02, không dùng $x^{(j)}$). Ghi chú: bỏ câu lặp mặt trang về xác minh ứng viên; giải nghĩa cận $1-(1-p_1^r)^b$ qua hai bước (trùng khóa ở một dải $\ge p_1^r$; các dải độc lập nên bỏ sót ở cả $b$ dải $\le(1-p_1^r)^b$). Công thức ở lại ghi chú (đưa lên làm trang vượt 60) |
| P02 | `sửa` | 48 → 48 | 3 | 135 → 135 | 1 | mục tiêu 3 gắn quyết định cụ thể: "Tính bộ nhớ, chi phí truy vấn; chọn chỉ mục cho kho $10^{10}$ véc-tơ với 6 TB, 10 ms." Ghi chú (ánh xạ câu tự kiểm) chưa đổi, để mạch 6 |
| P04 | `giữ` (ghi chú `sửa`) | 52 → 52 | 8 | 141 → 157 | 0,5 | ghi chú thêm: mỗi mạch xử lý giới hạn mà mạch trước để lại, một hệ thống cụ thể chỉ dùng cấu trúc hợp ngân sách; rút câu về tổng kết. 157 âm tiết (mức `nhẹ`) |
| P05 | `giữ` | 51 → 51 | 5 | 149 → 149 | 1 | ba đại lượng (độ trễ, bộ nhớ, độ thu hồi) nằm ở A02; "(giả định)" đã có. −0,5 phút |
| P01 | `sửa` | 35 → 36 | 4 | 168 → 202 | 2,5 | hộp câu hỏi một câu tính cho hai tốc độ "$10^{12}$ và $10^{13}$ lượt tọa độ mỗi giây" (bản có câu thứ hai "Tính lại với phần cứng nhanh gấp 10 lần." làm hộp xuống dòng và tràn đáy khung 1600×900, đã thử và bỏ). Ghi chú lời giải: 3,07 giây, vẫn gấp khoảng 307 lần ngân sách; thời gian đọc 122,88 TB không giảm khi chỉ tăng tốc độ tính. 202 âm tiết, có lời giải |
| A00 | `sửa` | 41 → 48 | 5 | 136 → 142 | 2,5 | thêm "Ví dụ. Năm điểm với $d(q,y_i)$ trong bảng, $K=3$: $N_3(q)=\{y_4,y_2,y_5\}$." và bảng một hàng $d(q,y_i)$ = 2,5; 1,2; 3,0; 0,8; 1,7 (tự tính: thứ tự tăng $y_4,y_2,y_5,y_1,y_3$). Ghi chú: thứ tự tăng dần; mô hình chỉ đếm tọa độ, giữ $K$ điểm tốt nhất bằng hàng đợi ưu tiên thêm $O(N\log K)$ phép so sánh; bỏ hai câu lặp mặt trang |
| A00B | `sửa` | 48 → 50 | 4 | 105 → 146 | 2 | dòng cơ chế và Lưu ý thay bằng ví dụ chung với A00: "$\widehat N_3(q)=\{y_4,y_5,y_1\}$"; "Thiếu $y_2$ vì $y_2$ không được đo, hoặc khoảng cách xấp xỉ xếp $y_2$ sau $y_1$."; "Lưu ý: mức thiếu điểm đo bằng độ thu hồi." Ghi chú: hai nguồn thiếu điểm trên ví dụ, phân biệt hai nguồn cho biết nên mở rộng vùng tìm hay làm phép đo chính xác hơn. Tên cấu trúc theo từng nguồn chuyển sang cột mới của A03 |
| A01 | `sửa` (ghi chú) | 34 → 34 | 4 | 107 → 103 | 2 | ghi chú bỏ câu "trung bình trên tập truy vấn" (sang A01B), thêm $\operatorname{recall@3}=2/3$ cho ví dụ năm điểm. −1 phút |
| A02 | `sửa` | 39 → 54 | 6 | 143 → 134 | 1,5 | thêm "Lưu ý: chỉ so hai chỉ mục trên cùng dữ liệu, cùng $K$, cùng phần cứng." (điều kiện để câu hỏi A/B có nghĩa); ghi chú giữ chi tiết từng trục, bỏ câu lặp |
| A03 | `sửa` | 31 → 44 | 6 | 122 → 150 | 2,5 | Mô hình gọi tên $n_c$ ("số véc-tơ được đo $n_c$"; Q11, Q10, I03 dùng lại); dòng "Quét đủ có $n_c=N$, mỗi phép đo $\Theta(D)$."; bảng thêm cột "Thiếu điểm vì" (LSH, đồ thị lân cận: không được đo; PQ: đo xấp xỉ; IVF-PQ: cả hai), cột "Thừa số giảm" ghi $n_c$. Ghi chú: giải thích cột mới, $4ND$ byte, một lần tra bảng và một lượt tọa độ không nhất thiết cùng thời gian. Không đặt $t_d$ (quyết định điều phối viên) |

Kiểm `check07.py` sau lượt: mạch 1 không trang nào vượt 60 âm tiết, 6 dòng hay 20 âm tiết mỗi dòng (trừ dòng luận đề bìa P00, 24 token, đã duyệt từ lượt 2026-10-16); không tràn khung 1600×900, không lỗi KaTeX, console hay yêu cầu mạng ngoài. Ghi chú trên 150 âm tiết: P03 184 và P04 157 (mức `nhẹ`), P01 202 và A01B 153 (có lời giải).

**Lệch tạm thời có chủ đích:** ví dụ năm điểm (A00, A00B, A01) và trang A01B chưa có trong `materials/lec-07/lecture-note.md`; đồng bộ ghi chú bài giảng sau mạch 7.

### Rà lại mạch 1 (2026-10-28)

Căn cứ: hai báo cáo rà lại (độ chính xác; mạch, văn phong, sinh viên) và danh sách sửa của điều phối viên. Bảng này thay các ô tương ứng của hai bảng "Mạch 1" phía trên (kể cả mục A01B); thứ tự 12 trang, chỉ số `#/1/v` và thời lượng 19,5 phút không đổi. "Trước" là bản sau lượt biên tập 2026-10-27.

| Mã | Âm tiết trước → sau | Dòng | Ghi chú trước → sau | Thay đổi và lý do |
|---|---|---:|---|---|
| P03 | 58 → 56 | 5 | 184 → 150 | dòng hệ quả LSH mở bằng "Suy ra" ("(Bài 06)" chỉ giữ ở dòng Nhắc lại đầu, bỏ lần lặp); dòng Nhắc lại thứ hai viết công thức $\|x-y\|_2^2=\sum_{j=1}^{m}\sum_{i\in G_j}(x_i-y_i)^2$ với $G_1,\ldots,G_m$ là phân hoạch của $\{1,\ldots,D\}$ (nhóm rời nhau và phủ hết, điều kiện cho tính cộng). Ghi chú: "mọi hàm chọn độc lập từ họ" (cận $p_1^r$ cần $r$ hàm trong một dải độc lập); bỏ giải nghĩa hàng đợi ưu tiên, k-means và "1 GB" để về 150 |
| P04 | 52 → 52 | 8 | 157 → 150 | ghi chú: "Mỗi cấu trúc khắc phục một giới hạn của cấu trúc trước; một hệ thống chỉ dùng cấu trúc hợp ngân sách." (bỏ chủ ngữ "Mỗi mạch"); rút câu tổng kết |
| A00B | 50 → 59 | 4 | 146 → 150 | thêm dòng "Chỉ mục (index) là cấu trúc dựng sẵn trên $Y$, quyết định véc-tơ nào được đo và đo thế nào." ngay sau Định nghĩa (thuật ngữ trung tâm chưa được định nghĩa); dòng Lưu ý chuyển vào ghi chú (cũng bỏ nghĩa thứ hai của "đo"). Ghi chú: phép suy đúng chiều "$y_1$ vào kết quả còn $y_2$ thì không, nên khoảng cách xấp xỉ của $y_2$ lớn hơn của $y_1$"; "ngoài tập đỉnh đã đo trên đồ thị"; "bỏ sót" thay "bỏ lỡ" |
| A01 | 34 → 43 | 5 | 103 → 105 | Ví dụ. "$\operatorname{recall@5}=3/5$; năm điểm: $\operatorname{recall@3}=2/3$" (ví dụ xuyên suốt có kết quả trên mặt trang); thêm "Lưu ý: độ thu hồi không xét thứ tự trong $K$ kết quả." (chuyển từ A01B; vừa khung, đã xem ảnh 1600 và 390). Ghi chú: "Bài báo PQ, mục V-A, tr.7" |
| A01B | 58 → 58 | 5 | 153 → 123 | "Độ thu hồi trung bình (mean recall)" ở lần dùng đầu; Ví dụ. "$K=10$, $\lvert Q\rvert=10$, mỗi truy vấn tìm lại 9 hàng xóm thật: trung bình $0{,}9$."; "Lưu ý: trung bình $0{,}9$ không cho biết tỷ lệ truy vấn đúng hoàn toàn." (kết luận lên mặt trang); Câu hỏi: "Chín truy vấn đạt 1, một đạt 0. Tính trung bình và tỷ lệ truy vấn đúng hoàn toàn." Ghi chú: lời giải 0,9 và tỷ lệ đúng hoàn toàn $9/10$ so với $0$ ở ví dụ; "$nok$ là số truy vấn …; $nok/100$ là $\operatorname{recall@1}$ trung bình". Sản phẩm học tập và bằng chứng kiểm của mục A01B giữ; dòng dài nhất 14 |
| A03 | 44 → 47 | 6 | 150 → 149 | dòng quét đủ nối kho mở bài: "Quét đủ có $n_c=N=10^{10}$, mỗi phép đo $D=3072$ lượt tọa độ." Ghi chú: mô hình bỏ qua chi phí cố định mỗi truy vấn; lập bảng tra và chọn tâm thô được đếm ở trang chi phí PQ, IVF-PQ, còn chi phí băm $q$ của LSH không tính trong bài; mã PQ "từ vài byte đến vài trăm byte" |

Thuật ngữ thống nhất trong mạch 1: "bỏ sót" cho điểm không được đo; "thiếu" khi so hai tập. Không sửa (ghi nhận): hộp Câu hỏi P01 ở 1600×900 chạm mũi tên điều khiển dọc (đã có trước lượt này, hộp vẫn một dòng; sửa cần đổi CSS dùng chung hoặc bỏ nội dung). Để sau: Q11 "Nhắc lại: $n_c$" (mạch 4); mục tiêu "giải thích" ở P02 (mạch 6).

Sửa nhẹ cuối (2026-10-28): A01 giữ dòng Ví dụ không có "Hình:"/"năm điểm trên" vì bản phân biệt nguồn xuống dòng ở 1600×900 (đã xem ảnh). Câu "PQ lấy $G_j$ là $m$ đoạn liên tiếp" không thêm vào ghi chú P03 vì ghi chú lên 160 âm tiết.

### Mạch 2

Căn cứ: `plan-guide-07.md` mục 2 và quyết định của điều phối viên (H04 giữ hình $ef=3$, không khẳng định $C\not\subseteq W$ ở trạng thái này; trường hợp $C\not\subseteq W$ đặt ở ghi chú H03C với $ef=2$; H01B có SVG mới; H00 nối $n_c$ của A03). Âm tiết, dòng, ghi chú đếm bằng `check07.py`; "trước" đo trên bản đã commit sau mạch 1 (5b13a8e).

**Thứ tự và thời lượng hiện hành:** HT, H00, H01, **H01B**, H03, H03B, **H03C**, H04, H05, H06 (10 trang). Phút: HT 0,5; H00 1; H01 2,5; H01B 2; H03 2; H03B 2,5; H03C 2,5; H04 1,5; H05 3; H06 3,5; tổng 21 (trước 19). Tổng phần giảng tạm là $19{,}5+21+23+28+17+12{,}5=121$ phút cho tới khi mạch 3 (23 → 21), mạch 4 (28 → 27) và mạch 5 (17 → 19) được sửa theo kế hoạch §9; sau đó về 120. Chỉ số: H01B `#/2/4`, H03 `#/2/5`, H03B `#/2/6`, H03C `#/2/7`, H04 `#/2/8`, H05 `#/2/9`, H06 `#/2/10`; HT vẫn `#/2/1`, số "2.".

**Mục đầy đủ cho hai trang mới**

| Trường | H01B — Cực tiểu cục bộ | H03C — Ví dụ: tìm kiếm chùm trên đồ thị bảy đỉnh, bước cuối |
|---|---|---|
| Mạch, vị trí | mạch 2, sau H01, trước H03 (`#/2/4`) | mạch 2, sau H03B, trước H04 (`#/2/7`) |
| Mục đích | định nghĩa cực tiểu cục bộ; phân biệt với đỉnh gần $q$ nhất trong cả đồ thị; chỉ ra bước làm tham lam thất bại | hoàn tất vết $ef=3$ tới $z$; giao câu hỏi $ef=2$ để thấy bề rộng chùm đổi vùng khám phá |
| Hoạt động sinh viên | đọc hình, xác định cực tiểu cục bộ và đỉnh gần nhất; giải thích vì sao nhánh $s$ bị loại | điền ba hàng còn lại của vết theo cùng khuôn H03B; chạy lại với $ef=2$ và chỉ ra bước dừng |
| Đối tượng trung tâm | đỉnh $b{:}5$ (cực tiểu cục bộ), $z{:}1$ (gần $q$ nhất), cạnh $e$–$s$ bị loại | ba lần mở $t$, $u$, $z$; phép so $d(c,q)\le d(f,q)$; điều kiện dừng $C$ rỗng |
| Dữ kiện, ký hiệu kế thừa | đồ thị bảy đỉnh và vết tham lam (H00, H01); ký hiệu $e{:}9$ | $W=\{t{:}4,b{:}5,a{:}7\}$, $C=\{t{:}4\}$ sau khi mở $s$ (H03B); $f$, $C$, $W$, $ef$ (H03) |
| Kiến thức đầu vào | lân cận trong đồ thị; quy tắc tham lam | tìm kiếm chùm, hàng đợi ưu tiên |
| Sản phẩm học tập | phát biểu được định nghĩa và vì sao điều kiện dừng của tham lam chỉ bảo đảm cực tiểu cục bộ | vết đầy đủ đối chiếu được với giả mã H05; lời giải $ef=2$ trả $\{b,a\}$ |
| Bằng chứng kiểm | dòng Nhận xét trên trang; câu tự kiểm về tham lam ở mạch 6 | hộp Câu hỏi (lời giải trong ghi chú: dừng ở lần lấy thứ tư, $s{:}8>a{:}7$); H06 dùng lại lần chạy $ef=2$ |
| Hình | `cuc-tieu-cuc-bo.svg` (mới, chế độ `'local'` của `generate_svg.py`): $b$ viền kép có nhãn "cực tiểu cục bộ", $z$ có nhãn "gần q nhất", cạnh $e$–$s$ nét đứt có nhãn "bị loại ở bước đầu"; tín hiệu bằng chữ và nét, không chỉ bằng màu | dùng lại `do-thi-chum.svg` |
| Mặt trang | 46 âm tiết, 3 dòng, dòng dài nhất 18 | 38 âm tiết, 6 dòng (bảng vết 3 hàng), dòng dài nhất 13 |
| Ghi chú | 126 âm tiết: điều kiện dừng chỉ kiểm lân cận trực tiếp; phải giữ $s$ sau khi sang $a$; 4 phép đo của vết tham lam; đỉnh gần nhất cũng là một cực tiểu cục bộ; nguồn Princeton lớp 9 tr.8 | 118 âm tiết: lời giải $ef=2$; trạng thái sau khi mở $a$ với $ef=2$ ($V=\{e,a,s,b\}$, $C=\{s,b\}$, $W=\{b,a\}$) cho thấy $C\subseteq W$ không phải lúc nào cũng đúng; $ef$ đổi vùng khám phá, không đổi đồ thị |
| Phút; quyết định | 2; `thêm` (tách khỏi H01: thêm vào H01 làm trang 68 âm tiết, 7 dòng) | 2,5; `thêm` (tách vết khỏi H03B thay vì gộp $t,u,z$ thành một hàng) |

**Các trang sửa**

| Mã | Quyết định | Âm tiết trước → sau | Dòng | Ghi chú trước → sau | Phút | Thay đổi và lý do |
|---|---|---|---:|---|---:|---|
| HT | `giữ` | 34 → 34 | 2 | 82 → 82 | 0,5 | trang tiêu đề không nhận định nghĩa; ẩn dụ tìm đường không đưa lên |
| H00 | `sửa` | 50 → 45 | 3 | 148 → 137 | 1 | Nhu cầu nối mô hình A03: "quét đủ có $n_c=N=10^{10}$; cần $n_c\ll N$ mà vẫn tới điểm gần $q$." Ghi chú: "chỉ các đỉnh trên đường đi và lân cận của chúng được đo" (trước: "chỉ các đỉnh trên đường đi được đo", hẹp hơn tập đã đo); bỏ câu về hàm khoảng cách (A00B đã định nghĩa chỉ mục) |
| H01 | `sửa` | 42 → 43 | 6 | 157 → 138 | 2,5 | Ký hiệu: "$e{:}9$ nghĩa là $d(e,q)=9$, chỉ được tính khi gặp $e$." (thuật toán không biết trước khoảng cách); Kết luận: "tham lam dừng ở $b{:}5$, trong khi $z{:}1$ gần $q$ hơn." Định nghĩa cực tiểu cục bộ chuyển sang H01B. Ghi chú: số trên hình chỉ để chạy tay; khoảng cách tính khi đỉnh xuất hiện trong danh sách lân cận. −1,5 phút |
| H03 | `giữ` | 56 → 56 | 4 | 169 → 169 | 2 | trang sát 60; ghi chú đã có câu $ef=1$ cho lại tham lam |
| H03B | `sửa` | 40 → 30 | 6 | 168 → 135 | 2,5 | bảng 4 hàng $e,a,b,s$ thêm cột "$d(c,q)$, $d(f,q)$" ($9\le9$, $7\le9$, $5\le8$, $8\le8$; $f$ lấy trước khi mở $c$) để quy tắc dừng thấy được trước giả mã; dòng đầu định nghĩa $f$; thêm "Nhận xét. Mở $a$ đẩy $e{:}9$ khỏi $W$ nhưng giữ $s{:}8$; sau khi mở $b$, nhánh $s$ còn trong $C$."; hộp câu hỏi $ef=2$ và lời giải chuyển sang H03C. +0,5 phút |
| H04 | `sửa` | 40 → 47 | 4 | 114 → 147 | 1,5 | chú thích hình đọc đúng trạng thái $ef=3$: "Sau khi mở $b$, $ef=3$: $e$ đã mở, bị đẩy khỏi $W$; $s$ chưa mở, thuộc $C$ và $W$." (không khẳng định $C\not\subseteq W$, sai ở trạng thái này); Ký hiệu: "$V$ là tập đỉnh đã thấy, tức đã tính $d(\cdot,q)$". Ghi chú phân biệt thấy và mở. −0,5 phút |
| H05 | `sửa` | 8 → 8 | 1 | 186 → 186 | 3 | chú thích cuối dòng trong giả mã: đã thấy/chờ mở/kết quả; ngưỡng; ứng viên tốt nhất xa hơn ngưỡng; mở $c$; mỗi đỉnh chỉ đo một lần; $W$ có thể vừa đổi (giữ đủ sáu chú thích vì không tràn ngang ở 1600×900, đã xem ảnh). −1 phút |
| H06 | `sửa` | 38 → 45 | 6 | 172 → 198 | 3,5 | bảng 4 hàng: khởi tạo; duy trì khi $\lvert W\rvert<ef$; duy trì khi $\lvert W\rvert=ef$ ("$y$ thay $f$ nếu gần $q$ hơn; nếu không, $W$ vẫn là $ef$ đỉnh gần nhất"); khi dừng ("$W$ đúng trên $V$; đỉnh ngoài $V$ không được xét"). Ví dụ "đỉnh gần nhất $z{:}1\notin V$". Ghi chú chứng minh: bất biến chỉ đổi khi một đỉnh mới vào $V$, lấy $c$ khỏi $C$ không đổi $W$; hai nhánh duy trì. Ghi chú 198 âm tiết (chứng minh, ≤ 250) |

**Vết tự chạy lại theo giả mã H05** ($f$ lấy ở dòng 4, trước khi mở $c$). $ef=3$: mở $e$ ($9\le9$) → $C=\{a,s\}$, $W=\{a7,s8,e9\}$; mở $a$ ($7\le9$) → $C=\{b,s\}$, $W=\{b5,a7,s8\}$; mở $b$ ($5\le8$) → $C=\{s\}$; mở $s$ ($8\le8$) → $C=\{t\}$, $W=\{t4,b5,a7\}$; mở $t$ ($4\le7$) → $C=\{u\}$, $W=\{u2,t4,b5\}$; mở $u$ ($2\le5$) → $C=\{z\}$, $W=\{z1,u2,t4\}$; mở $z$ ($1\le4$) → $C$ rỗng, dừng. $ef=2$: mở $e$ ($9\le9$) → $W=\{a7,s8\}$; mở $a$ ($7\le8$) → $C=\{s,b\}$, $W=\{b5,a7\}$, $V=\{e,a,s,b\}$; mở $b$ ($5\le7$) → $C=\{s\}$; lấy $s$: $8>7$, dừng, trả $\{b,a\}$. Với $ef=3$, $C\subseteq W$ sau mọi lần mở.

**Hình:** `generate_svg.py` thêm chế độ `'local'` của `do_thi_vi_du` và lệnh sinh `cuc-tieu-cuc-bo.svg`. Chạy lại tệp sinh không đổi SVG nào khác (kiểm `git status` và `git diff --stat` trên `img/lec-07/`: chỉ `generate_svg.py` đổi và một tệp mới).

**Lệch tạm thời có chủ đích:** H01B, H03C và cột so sánh của vết chưa có trong `materials/lec-07/lecture-note.md`; đồng bộ cùng lượt ghi chú sau mạch 7.

#### Rà lại mạch 2 (2026-10-28)

Căn cứ: hai báo cáo rà lại mạch 2 và danh sách sửa của điều phối viên. Bảng này thay các ô tương ứng của tiểu mục "Mạch 2"; thứ tự, chỉ số và thời lượng không đổi. "Trước" là bản sau lượt sửa mạch 2 lần đầu.

| Mã | Âm tiết trước → sau | Dòng | Ghi chú trước → sau | Thay đổi và lý do |
|---|---|---:|---|---|
| H01 | 43 → 43 | 6 | 138 → 111 | ô bảng viết $e{:}9$, $a{:}7,\ s{:}8$, … như dòng Ký hiệu; ghi chú bỏ câu "4 phép đo" (giữ ở H01B, nơi câu này phục vụ lập luận "$s$ đã đo nhưng bị bỏ") |
| H03 | 56 → 58 | 4 | 169 → 169 | "đỉnh đã thấy (đã đo $d(\cdot,q)$)" ở lần dùng đầu trên mặt trang, trước định nghĩa $V$ ở H04 |
| H03B | 30 → 34 | 7 | 135 → 135 | quy tắc mở và dừng nêu trước bảng: "Mở $c$ khi $d(c,q)\le d(f,q)$, với $f$ là đỉnh xa $q$ nhất của $W$; ngược lại dừng." (dòng riêng; 7 dòng, trần bảng vết 8); cột so sánh của bảng nay có lý do trên mặt trang |
| H03C | 38 → 32 | 6 | 118 → 125 | bỏ "Gợi ý:" khỏi hộp câu hỏi (quy tắc dừng đã ở H03B); gợi ý chuyển vào ghi chú, trước lời giải |
| H04 | 47 → 48 | 4 | 147 → 147 | Đầu vào: "(một đồ thị thì $\ell_c=0$)" để dòng không ngắt giữa công thức |
| H05 | 8 → 8 | 1 | 186 → 186 | sáu chú thích `//` cùng bắt đầu ở cột 40 (tính theo ký tự hiển thị); không tràn ngang ở 1600×900, đã xem ảnh 1600 và 390 |
| H06 | 45 → 45 | 6 | 198 → 202 | ghi chú: trường hợp xấu thăm mọi đỉnh và cạnh đến được từ $ep$ trong tầng (Thuật toán 2 chỉ mở lân cận của đỉnh đã vào $C$) |
