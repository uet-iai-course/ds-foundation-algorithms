# Bài 04 — PageRank theo chủ đề, liên kết rác và HITS

> **Trạng thái:** đã triển khai kế hoạch thành HTML, SVG và ghi chú bài giảng ngày 24/09/2026. Giữ 51 ID mới và 7 phần theo storyboard; bằng chứng kiểm định bản này được ghi riêng trong review-log.md, không dùng kết quả của các deck cũ.

## Phạm vi, đối tượng, tiên quyết

- **Phạm vi:** theo `sources/source.md` thứ tự đề xuất — PageRank theo chủ đề (topic-sensitive PageRank), cụm thao túng liên kết (link farm) và TrustRank/spam mass, HITS hai vai trò hub/authority; ánh xạ buổi gốc 5; hỗ trợ CLO1 (diễn giải) và CLO3 (chạy thuật toán), trọng tâm CLO2. Nguồn chính MMDS Ch.5 §5.3–5.5.
- **Đối tượng:** sinh viên năm 3, theo yêu cầu bản skill của phiên này (ngoại lệ rõ so với mặc định năm 2). Không nâng giả định ngoài những gì đã có ở Bài 03: đồ thị có hướng, ma trận–vector, xác suất cơ bản.
- **Tiên quyết:** Bài 03 đã dạy ma trận sửa nút cụt, ký hiệu $S$ (ma trận). Ở Bài 04, $S$ chủ đề là **tập đỉnh** — phải ghi rõ đổi ký hiệu này ở mở bài; đồng thời cầu nối $P := S_{\text{Bài03}}$ (cùng cột nguồn, cột cụt thay bằng $u = \mathbf{1}/n$); đồ thị ví dụ G4 không nút cụt nên $P = M_0$. Kế hoạch 04 cũ nói "P đã học" là sai, đã bác.
- **Quy mô:** 7 phần, 48 slide giảng / 120 phút + 3 slide bài tập / 60 phút = 51 slide. Bảng thời gian planner cũ (tổng 125 phút) đã bị bác.

## Vấn đề trung tâm

Tín hiệu liên kết tĩnh (PageRank cơ sở) không phân biệt chủ đề truy vấn (ví dụ truy vấn *jaguar* về động vật hay ô tô), dễ bị thao túng bằng cụm trang hỗ trợ, và không cho hai vai trò hub/authority. Bài này trả lời bằng ba mô hình: PageRank theo chủ đề với **vector dịch chuyển** $q_S$ (khởi tạo không xác định mô hình, phân bố trên tập đại diện chủ đề), phân tích cụm thao túng để hiểu và phòng vệ (TrustRank, spam mass), và HITS với **điểm trung tâm (hub) và điểm thẩm quyền (authority)** trên đồ thị con đã chọn (G5 thay cạnh C→A của G4 bằng C→E, tách rõ hai vai trò).

## Mục tiêu học tập (đo được)

- **MT1:** Sinh viên tính một bước và nghiệm giới hạn của PageRank theo chủ đề trên G4 với $S=\{B,D\}$, $\beta=4/5$, $r_0=q_S$, nêu được vai trò của phần dịch chuyển $(1-\beta)q_S$.
- **MT2:** Sinh viên giải phương trình cụm thao túng cho điểm đích $y$ theo $x,q,N,\beta$, phân biệt nghiệm chính xác và xấp xỉ của sách, và gán hạng cho bốn số hạng của **phương trình cân bằng** (không gọi là hạng trong nghiệm).
- **MT3:** Sinh viên tính TrustRank từng trang và spam mass từng trang trên G4, diễn giải được ý nghĩa giá trị mass âm và giới hạn của tỷ số (không phải xác suất).
- **MT4:** Sinh viên chạy hai vòng lặp luân phiên HITS trên G5, giữ chuẩn hóa max, và nêu điều kiện đủ hội tụ (hướng trội duy nhất $\lambda_1>\lambda_2\ge 0$, khởi có hình chiếu khác 0).
- **MT5:** Sinh viên so sánh bốn mô hình (PageRank cơ sở, PageRank theo chủ đề — viết tắt TSP, TrustRank, HITS) về đầu vào/đầu ra/chi phí và chọn đúng mô hình cho một tình huống cho trước.

## Bảng 7 phần

| Phần | Loại sư phạm | Nội dung | Slide | Phút | Đầu vào | Đầu ra | MT | ID kiểm tra | Kiểm tra |
|---|---|---|---|---|---|---|---|---|---|
| S01 | Mở bài + kiểm tiên quyết | Giới thiệu bài học | 6 | 10 | Tiên quyết Bài03, truy vấn jaguar | Bản đồ 7 phần, cầu nối $P:=S$, ký hiệu $S$ tập đỉnh | hỗ trợ MT1 | `lec04-s01-06` | Câu hỏi tiên quyết: nguồn B điểm 1/2, bậc ra 2, $\beta=4/5$ → mỗi cạnh đóng góp 1/5; tổng có $\beta$ lẫn dịch chuyển = 1 (G4, không hỏi $q_S$) |
| S02 | Khái niệm + hình thức hóa + thuật toán | PageRank theo chủ đề | 10 | 25 | G4, $S=\{B,D\}$, $q_S$, $\beta=4/5$ | Đặc tả PageRank theo chủ đề (TSP), giả mã biểu diễn thưa, tính tuyến tính k chủ đề, chi phí | MT1 | `lec04-s02-10` | Câu hỏi: tính $r_{1,A}$ và $r_{1,B}$, vì sao 1/5 khác 3/10 |
| S03 | Phân tích mô hình | Cụm thao túng liên kết | 8 | 22 | Hình 5.16 ba vùng, ký hiệu $N,q,x,y$ | Phương trình cụm thao túng chính xác + xấp xỉ, hệ số tại $\beta=.85$, giới hạn/chi phí | MT2 | `lec04-s03-08` | Câu hỏi gán 4 hạng $x,\ \beta^2 y,\ \beta q(1-\beta)/N,\ (1-\beta)/N$ → nguồn nào, bỏ hạng nào ra xấp xỉ |
| S04 | Mô hình phòng vệ + ví dụ số | TrustRank và khối lượng rác | 8 | 21 | Giả thiết cô lập gần đúng, tập $T$ | $t'=\beta P t+(1-\beta)q_T$, spam mass $s_p=(r_p-t_p)/r_p$, bảng 5.17 có cảnh báo 2 thiết lập | MT3 | `lec04-s04-08` | Câu hỏi: $t_B=59/210$, $r_B=2/9$ → mass âm $-37/140$ nghĩa gì, có phải xác suất rác không |
| S05 | Thuật toán + chứng minh có điều kiện | Hai vai trò của HITS | 11 | 30 | G5, Hình 5.18, định nghĩa $h,a$ | Vòng luân phiên chuẩn hóa theo phần tử lớn nhất, điều kiện dừng và trường hợp biên (điểm không bắt buộc giảm đơn điệu), vector riêng có điều kiện, chi phí 2 quét cạnh | MT4 | `lec04-s05-11` | Câu hỏi: vì sao $h_E=0$ ngay vòng 1 trong khi $a_E=1/2>0$, và $a_E$ vòng 2 $=1/10$ |
| S06 | Tổng kết + kiểm tra tích hợp | Tổng kết và kiểm tra | 5 | 12 | Bảng 4 mô hình, so chi phí | Thu hồi jaguar/cụm thao túng/2 vai trò, khép 3 giới hạn, nối bài tập và §5.3–5.5 | MT5 | `lec04-s06-04` | Câu hỏi tích hợp 4 nhiệm vụ (thay $q_S$ chỗ nào; hạng nào sách bỏ; mass âm được không; HITS nhân ma trận nào); có lựa chọn mô hình cho ô tô và hai vai trò HITS trước công thức |
| S07 | Bài tập thực hành | Bài tập trên lớp | 3 | 60 | R1, R2, R3 (NG1) | Đáp án TSP hai tập S; TrustRank + mass; HITS G4 đến hội tụ | MT4 (G4 riêng), hỗ trợ MT1, MT3 | `lec04-s07-03` | Slide 03 là kiểm tra riêng phần 7 (riêng MT4); slide 01, 02 cũng là hoạt động bài tập |

Tổng: 48 slide giảng / 120 phút + 3 slide / 60 phút = 51 slide.

## Danh mục nguồn NG0–NG7

| ID | Nguồn | Vị trí / ghi chú |
|---|---|---|
| NG0 | [sources/source.md](../../../sources/source.md) | Bài 4 đề xuất (bảng mục tiêu, thứ tự), buổi gốc 5; bảng reference-slides Bài 4. Không thiếu nguồn bắt buộc. |
| NG1 | [mmds-3e-ch05-link-analysis.pdf](../../../sources/textbooks/mmds-3e-ch05-link-analysis.pdf) | 38 trang; **Leskovec, Rajaraman, Ullman**; trang in = PDF + 174. §5.3: 195–199/PDF21–25; §5.4: 199–204/PDF25–30; §5.5: 204–208/PDF30–34. Hình 5.1:178/PDF4, 5.15:197/PDF23, 5.16:200/PDF26, 5.17:203/PDF29, 5.18–19:206/PDF32, 5.20:207/PDF33. Bài 5.3.1:199/PDF25; 5.4.2:204/PDF30; 5.5.1:208/PDF34. |
| NG2 | [ch05-linkanalysis1.pdf](../../../sources/reference-slides/mmds/ch05-linkanalysis1.pdf) | 60 slide, kiểm kê toàn bộ; PageRank cơ sở, 60 cầu nối chủ đề; nội dung 8–60 thuộc Bài 03, chỉ nhắc lại cần thiết. Link công bằng: [www.mmds.org](http://www.mmds.org). |
| NG3 | [ch05-linkanalysis2.pdf](../../../sources/reference-slides/mmds/ch05-linkanalysis2.pdf) | 60 slide; 1–5 nhắc PageRank; 7–11 chủ đề; 12–20 RWR/SimRank bỏ; 29–35 cụm thao túng giữ; 37–45 TrustRank/spam giữ theo sách; 47–60 HITS giữ trực giác, đổi chuẩn hóa/cập nhật theo sách. Không sao chép giao diện/hình raster. |
| NG4 | [10-spam.pdf](../../../sources/reference-slides/stanford-cs246/10-spam.pdf) | 72 slide, CS246 Stanford, ngày 5 tháng 2 năm 2026 (ghi Mỹ: 2/5); Leskovec/Rajaraman/Ullman theo trang đầu; [bản gốc mở được](https://web.stanford.edu/class/cs246/slides/10-spam.pdf). Dùng đối chiếu; Pixie (20–41, 67–71) và truyền trust riêng (72) bỏ. |
| NG5 | [Cornell INFO4300/CS4300, Ginsparg, 27/10/2009, 40 slide](https://courses.cit.cornell.edu/info4300_2009fa/slides/16.pdf) | Đã đọc text trang 1, 10, 20–34; screenshot 26/30 thất bại — không tuyên bố đã xem bố cục hình. Chỉ đối chiếu ĐH thứ 2; tóm tắt ≤200 từ, dẫn link gần bảng nhận định. |
| NG6 | Lecture03 [note](../../materials/lec-03/lecture-note.md) §2–3 và [HTML hiện hành](../../lecture-03-pagerank-mo-hinh-va-tinh-toan.html) | Ma trận thô $M_0$, ma trận sửa nút cụt $S$ ở chứng minh; cầu nối $P:=S_{\text{Bài03}}$. |
| NG7 | [template](../../lecture-template.html) / [CSS](../../lecture-style.css) / [index](../../index.html) / [Lecture02](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) | Dùng lại lớp CSS có sẵn (.course-deck, .lecture-title, .agenda-slide, .motivation-grid, .source-note, .question-box hoặc tương đương); 1280×720, body ≥ .75em, không fragment, không màu đơn độc; SVG kỹ thuật vẽ lại khi dựng. |

Ghi chú truy cập: [www.mmds.org](http://www.mmds.org) (http/https) trả web 502 ở lượt kiểm hiện tại; bản PDF chính thức cục bộ đủ, không coi là thiếu nguồn. Đã mở [guide chính thức](https://raw.githubusercontent.com/uet-iai-course/machine-learning/main/SLIDE_STYLE_GUIDE.md).

## So sánh ngắn MMDS – Stanford – Cornell (có căn cứ)

- **MMDS (NG1, NG3):** nguồn chính. Sách cung cấp số chạy tay nhất quán (VD5.10, 5.11, 5.12; Hình 5.1, 5.15–5.20); HITS theo chuẩn hóa max và cập nhật luân phiên. Slide 55 của NG3 chuẩn hóa L2 khác sách — chọn sách thống nhất.
- **Stanford CS246 (NG4):** tương đương nội dung tại các cụm: chủ đề MMDS 7–11 ↔ Stanford 9–14; cụm thao túng MMDS 29–35 ↔ Stanford 49–55; TrustRank MMDS 37–45 ↔ Stanford 57–65. Không chọn Stanford làm nguồn chính chỉ vì pdftotext rõ hơn; slide 35/55 có nhận định "as large as we want" — loại nhận định.
- **Cornell (NG5):** đối chiếu ĐH thứ 2 cho HITS. Tóm tắt (≤200 từ): slide 20–24 trình bày ví dụ hai vai trò hub/authority và cách nối tổng theo cạnh thành ma trận; slide 27–29 nói về tập gốc và tập mở rộng, cho biết phạm vi áp dụng của HITS trên đồ thị con; slide 31–32 mô tả cập nhật và chuẩn hóa; slide 33 nêu hiện tượng lệch chủ đề; slide 34 so sánh PageRank và HITS. Slide 26 khẳng định $A^TA$ có hàng tổng 1 — điều này không đúng nói chung, không dùng; slide 10 gợi ý phương pháp lũy thừa với khoảng cách phổ, dùng để kiểm điều kiện hội tụ HITS. Không thêm root/base algorithm vào tuyến chính. Nguồn: [Cornell INFO4300/CS4300, Ginsparg, 27/10/2009](https://courses.cit.cornell.edu/info4300_2009fa/slides/16.pdf).

Điều phối viên đã xem ảnh render trực tiếp: NG1 PDF 23, 26, 27, 29, 32, 33; NG3 slide 10, 35, 55, 56; NG4 slide 13, 55, 65. Hình nguồn chính đã kiểm hướng cạnh theo công thức, không cần tạo ảnh mới.

## Bản đồ khái niệm và đồ thị tiên quyết

**Đồ thị tiên quyết (DAG phụ thuộc toán học, tách khỏi đồ thị dữ liệu G4/G5 và khỏi mạch trình bày):**

```
PageRank Bài 03 (ma trận sửa nút cụt, phép co) ──► P := S_Bài03 ──► vector dịch chuyển q_S ──► TSP ──► TrustRank
PageRank Bài 03 ──► mô hình cụm thao túng ──► nhu cầu phòng vệ ──► TrustRank
Đồ thị có hướng + nhân ma trận–vector ──► hai vai trò HITS ──► lặp luân phiên và điều kiện hội tụ
TSP, cụm thao túng, TrustRank, HITS ──► so sánh / chọn mô hình
```

Lưu ý: thứ tự giảng S02→S03→S04→S05 là **tuyến sư phạm**, không phải mọi mũi tên trong mạch giảng là tiên quyết toán học; đặc biệt TrustRank/spam mass **không** là tiên quyết của HITS. Các nhánh trên chỉ ra kiến thức cần có trước; thứ tự trình bày được ghi riêng trong bảng bảy phần. G4 và G5 là đồ thị dữ liệu dùng cho ví dụ số.

| Khái niệm | Loại | Tiên quyết | Ghi chú |
|---|---|---|---|
| Vector dịch chuyển $q_S$ | Cốt lõi | Tập $S$ (đỉnh), phân bố xác suất | Đổi từ "vector khởi động"; khởi tạo không xác định mô hình |
| TSP: $r'=\beta P r+(1-\beta)q_S$ | Cốt lõi | $P:=S_{\text{Bài03}}$, G4 | Tính tuyến tính theo $q$ |
| Cụm thao túng (link farm) | Cốt lõi | PageRank cơ sở | Phân tích mô hình, không dạy tạo spam |
| TrustRank / spam mass | Cốt lõi | TSP, giả thiết cô lập gần đúng | Mass có thể âm, không phải xác suất |
| HITS hai vai trò $h,a$ | Cốt lõi | Đồ thị con, ma trận $L$ hàng nguồn | Chuẩn hóa max, cập nhật luân phiên |
| $P:=S_{\text{Bài03}}$; $S$ tập đỉnh | Cầu nối | Bài 03 | Ghi rõ đổi ký hiệu ở mở bài |
| Đồ thị G4, G5; $M_0$ | Cầu nối | Bài 03 | G4 không nút cụt nên $P=M_0$ |
| RWR/SimRank, Pixie, root/base | Bỏ | — | Ngoài tuyến chính (NG3 12–20; NG4 20–41, 67–71, 72) |
| DMOZ16 | Đọc thêm | — | Ví dụ lịch sử trong sách; lược khỏi tuyến chính vì không lấp khoảng trống; không khẳng định hệ đang hoạt động |
| Perron–Frobenius đầy đủ | Đọc thêm | — | Chỉ nêu điều kiện đủ, không chứng minh |

**Quyết định hợp nhất:** giữ toàn bộ khái niệm cốt lõi và cầu nối; gộp "lỗi hạt giống" và "thiên lệch" vào một slide S04-04 (cùng một trực giác); bỏ RWR/SimRank/Pixie vì spec đã duyệt; thêm slide giải thích tính tuyến tính k chủ đề (S02-09) vì là cầu nối sang MT5.

## Phiếu ngắn 4 khái niệm trọng tâm

Mỗi phiếu theo mạch: nhu cầu → trực giác → ví dụ → hình thức → thuật toán/đúng → ứng dụng/chi phí → kiểm tra.

**1. PageRank theo chủ đề (TSP — topic-sensitive PageRank)** — ID `lec04-s02-*`
- *Nhu cầu:* truy vấn jaguar cần xếp hạng theo chủ đề. *Trực giác:* người đọc chủ đề chỉ nhảy về tập đại diện $S$. *Ví dụ:* G4, $S=\{B,D\}$, $\beta=4/5$, $r_0=q_S=(0,\tfrac12,0,\tfrac12)$.
- *Hình thức:* $r'=\beta P r+(1-\beta)q_S$, $q_S\ge 0$, $\sum q_S=1$, $S\ne\emptyset$, $\beta\in(0,1)$.
- *Thuật toán/đúng:* biểu diễn thưa, bù nút cụt đều với $u=\mathbf{1}/n$; mỗi vòng **tính lại** $\delta=\sum r_j$ trên các đỉnh cụt; cập nhật $r_{new}=\beta M_0 r+\beta\delta\, u+(1-\beta)q_S$; dừng khi $\|r_{new}-r\|_1\le\tau$ với $\tau>0$, hoặc hết $K_{max}$ (nguyên $\ge1$); đạt → trả $r_{new}$ + trạng thái đạt, hết $K_{max}$ → trả trạng thái cuối + chưa đạt; bất biến xác suất; co L1 vì $\|Pv\|_1\le\|v\|_1$, $\beta<1$; $r^*$ duy nhất, có thể có phần tử 0 khi $q_S$ hỗ trợ con — không tuyên bố dương mọi trang.
- *Ứng dụng/chi phí:* k chủ đề, $O(kI(n+m_G))$, lưu $O(kn)$ ngoài đồ thị; phối hợp $r^*=\sum\alpha_l r_l$.
- *Kiểm tra:* `lec04-s02-10` — tính $r_{1,A}=\tfrac15$, $r_{1,B}=\tfrac3{10}$, vì sao khác.

**2. Cụm thao túng (link farm)** — ID `lec04-s03-*`
- *Nhu cầu:* hiểu vì sao PageRank bị đẩy lên. *Trực giác:* trang đích nhận về cả ba dòng: từ $x$, từ các trang hỗ trợ, và phần dịch chuyển. *Ví dụ:* Hình 5.16 ba vùng, $N$ tổng trang, $q\ge1$ hỗ trợ, $x$ đóng góp ngoài (đã gồm $\beta$), $y$ đích.
- *Hình thức:* $z=\beta y/q+(1-\beta)/N$; $y=x+\beta q z+(1-\beta)/N$; nghiệm chính xác $y=\dfrac{x}{1-\beta^2}+\dfrac{\beta q+1}{N(1+\beta)}$; xấp xỉ sách bỏ phần dịch chuyển trực tiếp, sai khác $\tfrac{1}{N(1+\beta)}$.
- *Thuật toán/đúng:* tại $\beta=.85=17/20$: hệ số ngoài $400/111\approx3.6036$ — nói "gấp khoảng 3.6 lần", không nói "tăng thêm 360%"; hệ số $17/37\approx.4595$ **nhân** $q/N$. Không nói "tăng trang hỗ trợ khiến PageRank lớn tùy ý".
- *Chi phí:* đánh giá biểu thức khi đã biết $x$ là $O(1)$; tìm PageRank nền vẫn cần lặp trên đồ thị.
- *Kiểm tra:* `lec04-s03-08` — gán 4 hạng, nguồn nào bỏ khi xấp xỉ.

**3. TrustRank và khối lượng rác (Trust/mass)** — ID `lec04-s04-*`
- *Nhu cầu:* phòng vệ sau khi hiểu cụm thao túng. *Trực giác:* trang tốt ít trỏ rác — **giả thiết**, không bảo đảm. *Ví dụ:* VD5.12 với cảnh báo hai thiết lập (PageRank nền không hệ số suy giảm).
- *Hình thức:* $q_T=e_T/|T|$, $t_0=q_T$, $t'=\beta P t+(1-\beta)q_T$; mass $s_p=(r_p-t_p)/r_p$, $r_p>0$; có thể âm, $\le1$ khi $t\ge0$, không phải xác suất, không ngưỡng chắc chắn.
- *Thuật toán/đúng:* bất biến/co/chi phí dùng lại từ TSP, không chứng minh trùng; hai cách chọn $T$ (thẩm định ứng viên PageRank cao hoặc tên miền có kiểm soát), cân bằng chi phí thẩm định/độ phủ; không nói hậu tố .edu/.gov bảo đảm sạch.
- *Kiểm tra:* `lec04-s04-08` — mass âm $-37/140$ nghĩa gì.

**4. HITS** — ID `lec04-s05-*`
- *Nhu cầu:* hai vai trò trên đồ thị con theo truy vấn. *Trực giác:* hub tốt trỏ tới authority tốt và ngược lại. *Ví dụ:* G5 ($n_H=5,m_H=8$), Hình 5.18; vòng 1: $a_1=(\tfrac12,1,1,1,\tfrac12)$, $h_1=(1,\tfrac12,\tfrac16,\tfrac23,0)$.
- *Hình thức:* $L$ hàng nguồn (khác $P$ cột nguồn); $a_{raw}=L^T h_{old}$, $h_{raw}=L\,a_{new}$, chuẩn hóa theo phần tử lớn nhất mỗi vòng.
- *Thuật toán/đúng:* ba trạng thái kết thúc: (suy biến — $L=0$), (đạt ngưỡng $\tau$), (chưa đạt khi hết $K_{max}$); kiểm $\max=0$ **trước** khi chia (đồ thị không cạnh → trả $h=a=0$, cờ suy biến); đạt ngưỡng → trả cặp $(h,a)$ MỚI; hết $K_{max}$ → trả cặp cuối + chưa đạt; dừng $\max|h_{new}-h_{old}|,\max|a_{new}-a_{old}|\le\tau$; **các điều kiện sau đủ bảo đảm hội tụ về hướng trội** (KHÔNG là điều kiện cần): hướng trội duy nhất $\lambda_1>\lambda_2\ge0$ của $L^TL$ và $LL^T$, $L\ne0$, và khởi có hình chiếu khác 0 trên hướng trội; phác ý sai số giảm $(\lambda_2/\lambda_1)^u$ — không suy từ vài vòng.
- *Chi phí:* $O(n_H+m_H)$/vòng, 2 quét cạnh + 2 quét max; không dựng $LL^T$ (có thể đặc).
- *Kiểm tra:* `lec04-s05-11` — vì sao $h_E=0$ ngay vòng 1.

**Vì sao chọn mạch này:** nhu cầu trước trực giác trước ký hiệu (theo hướng dẫn); chỉ TrustRank dùng lại bất biến xác suất và phép co của TSP (không chứng minh trùng), còn cụm thao túng giải đại số riêng và HITS phân tích riêng; kiểm tra đặt cuối mỗi phiếu để nối thẳng vào bảng 7 phần.

## Danh mục hình thức hóa (ID HT1–HT8)

| ID | Phát biểu / giả thiết | Mức chứng minh | Nguồn | Slide |
|---|---|---|---|---|
| HT1 | Đặc tả TSP: $r'=\beta Pr+(1-\beta)q_S$ với $P\ge0$, cột tổng 1, $q_S\ge0$, $\sum q_S=1$, $S\ne\emptyset$, $\beta\in(0,1)$, $n\ge1$ | Đặc tả + kiểm bất biến | NG1 §5.3 | s02-06 |
| HT2 | Bất biến xác suất và phép co L1 của TSP trên simplex: giả thiết $P\ge0$ cột tổng 1, $\beta\in(0,1)$, $q_S$ là phân bố (tổng 1, không âm); kết luận bất biến gồm cả không âm và tổng 1; $\|F(r)-F(s)\|_1=\beta\|P(r-s)\|_1\le\beta\|r-s\|_1$ (dùng lại cho TrustRank) | Chứng minh ngắn (2 bất đẳng thức) | NG1 §5.3 | s02-08 |
| HT3 | Phối hợp $r^*=\sum\alpha_l r_l$ với $\alpha\ge0$, $\sum\alpha_l=1$, $\beta$ chung, $P$ chung | Suy ra tuyến tính, giải thích ngắn | NG1 §5.3 | s02-09 |
| HT4 | Cụm thao túng: nghiệm chính xác $y$ và xấp xỉ sách, sai khác $\tfrac{1}{N(1+\beta)}$ | Giải phương trình từng bước | NG1 §5.4, VD5.11 | s03-06 |
| HT5 | TrustRank $t'=\beta Pt+(1-\beta)q_T$ với $T\ne\emptyset$, $q_T=e_T/\lvert T\rvert$; spam mass $s_p=(r_p-t_p)/r_p$ chỉ xác định khi $r_p>0$; có thể âm, $\le1$ khi $t\ge0$, không xác suất | Phân tích tỷ số | NG1 §5.4 | s04-05 |
| HT6 | Quy tắc HITS: $a_{raw}=L^Th_{old}$, $h_{raw}=La_{new}$, chuẩn hóa theo phần tử lớn nhất, cập nhật luân phiên | Đặc tả + bảng vòng | NG1 §5.5, Hình 5.19–5.20 | s05-04..07 |
| HT7 | Các điều kiện đủ bảo đảm hội tụ HITS về hướng trội (không phải điều kiện cần): hướng trội duy nhất $\lambda_1>\lambda_2\ge0$ của $LL^T$ và $L^TL$, $L\ne0$, và khởi có hình chiếu khác 0 lên hướng trội của $LL^T$ (không phải của $L^TL$; tham chiếu $h_0$) | Ghi chú chứng minh, không giả thiết SV biết Perron | NG1 §5.5; NG5 slide 10 | s05-09 |
| HT8 | Chi phí: HITS $\Theta(n_H+m_H)$/vòng, 2 quét cạnh + 2 quét max; TSP $\Theta(n+m_G)$/vòng; cụm thao túng $O(1)$ khi đã biết $x$ | Đếm phép toán | NG1 §5.3–5.5 | s03-07, s05-10, s06-02 |

## Thuật ngữ và ký hiệu

| Ký hiệu | Ý nghĩa | Lưu ý |
|---|---|---|
| $P$ | Ma trận sửa nút cụt đều, $P:=S_{\text{Bài03}}$ | G4 không nút cụt nên $P=M_0$ |
| $S$ | **Tập đỉnh** chủ đề (Bài 04) | Đổi từ ma trận $S$ của Bài 03 — ghi rõ ở mở bài |
| $q_S$ | Vector dịch chuyển trên tập $S$ | Khác $q$ = **số** trang hỗ trợ trong cụm thao túng |
| $q$ | Số trang hỗ trợ cụm thao túng ($q\ge1$, $N\ge q+1$) | Ký hiệu khác $q_S$, giữ nguyên bản 5.11 |
| $N,x,y,z$ | Tổng trang / đóng góp ngoài / đích / mỗi trang hỗ trợ | Khác G4 |
| $\beta$ | Hệ số theo liên kết | $4/5$ (TSP, trust), $17/20$ (cụm thao túng) |
| $h,a$ | Điểm trung tâm / thẩm quyền HITS | HITS đầy đủ: "tìm kiếm theo chủ đề dựa trên siêu liên kết" (Hyperlink-Induced Topic Search) lần đầu |
| $T,q_T,t$ | Tập tin cậy, vector tin cậy | $T$ nonempty, $q_T=e_T/\lvert T\rvert$ |
| $s_p$ | Spam mass | $(r_p-t_p)/r_p$ |
| $L$ | Ma trận kề HITS, hàng nguồn | Khác $P$ cột nguồn |


## Bảng hình dự kiến và ý cần thấy

| Hình | Nguồn | Ý cần thấy |
|---|---|---|
| Đồ thị G4 | NG1 Hình 5.1 (PDF4) | 4 đỉnh, 8 cạnh; nền cho TSP/trust/bài tập R1–R2 |
| Ba vùng cụm thao túng | NG1 Hình 5.16 (PDF26) | Ba vùng nguyên bản: không thể tác động / có thể tác động / các trang sở hữu; đích và $q$ trang hỗ trợ cùng nằm trong vùng sở hữu; mỗi trang hỗ trợ **chỉ** trỏ đích, đích trỏ mọi trang hỗ trợ, không có trỏ chéo giữa các trang hỗ trợ; dòng chảy $x$, $\beta q z$, phần dịch chuyển |
| Bảng 5.17 mass | NG1 Hình 5.17 (PDF29) | Cảnh báo hai thiết lập; mass âm tại B |
| Đồ thị G5 | NG1 Hình 5.18 (PDF32) | 5 đỉnh 8 cạnh; E không cạnh ra → $h_E=0$ |
| Ma trận $L, L^T$ | NG1 Hình 5.19 (p206/PDF32) | Hàng nguồn khác $P$ cột nguồn; đối chiếu $L^Th$ / $La$ |
| Bảng lặp HITS | NG1 Hình 5.20 (p207/PDF33) | Nhãn chuẩn hóa theo phần tử lớn nhất, trạng thái cũ/mới; không gán cho so sánh PageRank/HITS |

## Ghi chú kỹ thuật đã cam kết

- TSP: bất biến xác suất, co L1 — đã nêu ở phiếu 1; cụm thao túng: nghiệm chính xác + xấp xỉ và giới hạn (không ép đủ định lý ở cụm thao túng); HITS: chuẩn max, cập nhật luân phiên, hội tụ có điều kiện đủ; chỉ TrustRank dùng lại bất biến/co của TSP, cụm thao túng và HITS phân tích riêng.
- Phiếu số chi tiết VD1–VD5 (TSP, cụm thao túng, mass, HITS, recitation) đã nối đầy đủ dưới đây.
- Bảng 7 phần: mỗi ô kiểm tra có ID riêng với tiền tố `lec04-`: s01-06, s02-10, s03-08, s04-08, s05-11, s06-04, s07-03; gắn với mục tiêu MT: s01-06 (kiểm tiên quyết hỗ trợ MT1, không tạo MT0), s02-10 (MT1), s03-08 (MT2), s04-08 (MT3), s05-11 (MT4), s06-04 (MT5), s07-03 (MT4). Không đổi slide/timing.

## Phiếu số ví dụ — phần 1: PageRank theo chủ đề và cụm thao túng (VD1–VD2)

### VD1 — TSP trên G4, $S=\{B,D\}$, $\beta=4/5$ (NG1 VD5.10, §5.3, p197–199/PDF23–25)

**Nguồn và quyền điều chỉnh:** số liệu từ NG1 VD5.10 và dãy vòng đã kiểm bằng Fraction + giải hệ Gaussian (phương pháp Fraction/giải hệ, thuật toán kiểm để truy ngược). Không tự làm tròn, không đổi số nguồn; chỉ bổ sung nhãn khi các giá trị bằng nhau có ý nghĩa khác nhau.

**Đối tượng / đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn:**

| Đối tượng/đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị | Vai trò | Nguồn |
|---|---|---|---|---|---|
| Đồ thị ví dụ | G4 | $n=4$, $m_G=8$; thứ tự A,B,C,D: A→B,C,D; B→A,D; C→A; D→B,C | đồ thị có hướng | nền mọi phép tính | NG1 Hình 5.1 (PDF4) |
| Ma trận chuyển | $P$ | $\begin{bmatrix}0&\tfrac12&1&0\\ \tfrac13&0&0&\tfrac12\\ \tfrac13&0&0&\tfrac12\\ \tfrac13&\tfrac12&0&0\end{bmatrix}$ | ma trận 4×4, cột tổng 1, không âm | nhân bên trái vector | NG1 §5.3; G4 không nút cụt nên $P=M_0$ |
| Hệ số theo liên kết | $\beta$ | $4/5$ | số thực vô đơn vị | co mỗi vòng | NG1 VD5.10 |
| Tập chủ đề | $S$ | $\{B,D\}$ | tập đỉnh | đại diện chủ đề | NG1 VD5.10 |
| Vector dịch chuyển | $q_S$ | $(0,\tfrac12,0,\tfrac12)$ | vector xác suất, tổng 1 | phân bố dịch chuyển; ở ví dụ cũng chọn làm khởi tạo | NG1 VD5.10 |
| Khởi | $r_0$ | $=q_S$ | vector xác suất | điểm bắt đầu lặp | NG1 VD5.10 |
| Liên kết | $\beta P r_0$ | $(\tfrac15,\tfrac15,\tfrac15,\tfrac15)$ | vector khối lượng, tổng $4/5$ | dòng theo cạnh | Tính từ phép lặp NG1, VD5.10 |
| Dịch chuyển | $(1-\beta)q_S$ | $(0,\tfrac1{10},0,\tfrac1{10})$ | vector khối lượng, tổng $1/5$ | phần bổ sung dịch chuyển | Tính từ phép lặp NG1, VD5.10 |
| Vòng 1 | $r_1$ | $(\tfrac15,\tfrac3{10},\tfrac15,\tfrac3{10})$ | vector xác suất | kết quả 1 vòng | Tính từ phép lặp NG1, VD5.10 |
| Vòng 2 | $r_2$ | $(\tfrac{42}{150},\tfrac{41}{150},\tfrac{26}{150},\tfrac{41}{150})$ | vector xác suất | kết quả 2 vòng | Tính từ phép lặp NG1, VD5.10 |
| Vòng 3 | $r_3$ | $(\tfrac{62}{250},\tfrac{71}{250},\tfrac{46}{250},\tfrac{71}{250})$ | vector xác suất | kết quả 3 vòng | Tính từ phép lặp NG1, VD5.10 |
| Nghiệm | $r^*$ | $(\tfrac{54}{210},\tfrac{59}{210},\tfrac{38}{210},\tfrac{59}{210})$ | vector xác suất, tổng 1 | nghiệm chính xác | Tính từ phép lặp NG1, VD5.10 (giải hệ) |

**Vết chạy chính xác (bảng vai trò gộp, giữ nhãn đỉnh và cột trạng thái):**

| Vòng | $r_A$ | $r_B$ | $r_C$ | $r_D$ | Trạng thái |
|---|---|---|---|---|---|
| $r_0=q_S$ | $0$ | $\tfrac12$ | $0$ | $\tfrac12$ | khởi |
| $r_1$ | $\tfrac15$ | $\tfrac3{10}$ | $\tfrac15$ | $\tfrac3{10}$ | 1 vòng |
| $r_2$ | $\tfrac{42}{150}$ | $\tfrac{41}{150}$ | $\tfrac{26}{150}$ | $\tfrac{41}{150}$ | 2 vòng |
| $r_3$ | $\tfrac{62}{250}$ | $\tfrac{71}{250}$ | $\tfrac{46}{250}$ | $\tfrac{71}{250}$ | 3 vòng |
| $r^*$ | $\tfrac{54}{210}$ | $\tfrac{59}{210}$ | $\tfrac{38}{210}$ | $\tfrac{59}{210}$ | nghiệm chính xác (giải hệ), **không gán là vòng 3** |

**Lỗi dễ mắc, nhầm số, quyết định giữ số + bổ sung nhãn:**
- Nhiều phân số bằng nhau nhưng ý nghĩa khác nhau: $\tfrac12$ trong $q_S$ là **xác suất khởi trên tập $S$**, còn $\tfrac1{10}$ là **phần bổ sung dịch chuyển** $(1-\beta)\cdot\tfrac12$ — giữ cả hai, nhãn rõ để không lẫn.
- $r_2$ và $r_3$ có mẫu khác nhau (150, 250) — giữ phân số nguồn, không quy đồng ép cùng mẫu; các dạng tương đương trong numbers.json (ví dụ $42/150=7/25$) là cùng giá trị, không phải lỗi số.
- Sai nhân $P^T$ thay $P$ với $r_0=(0,\tfrac12,0,\tfrac12)$, $\beta=4/5$ cho $r_{1,sai}=(\tfrac4{15},\tfrac3{10},0,\tfrac3{10})$, tổng $\tfrac{13}{15}\ne1$ — kết quả sai cụ thể giúp phân biệt số; sai bỏ phần dịch chuyển → tổng $4/5\ne1$.
- $r^*$ là nghiệm giải hệ, không phải kết quả vòng 3; ghi nhãn "giới hạn" thay vì gán vòng.

**Slide dùng lại:** `lec04-s02-02..05` (dữ kiện), `lec04-s02-10` (kiểm tra $r_{1,A}=\tfrac15$, $r_{1,B}=\tfrac3{10}$), `lec04-s01-06` (tiên quyết: nguồn B điểm $\tfrac12$, bậc ra 2, mỗi cạnh đóng góp $\tfrac15$).

### VD2 — Cụm thao túng liên kết (link farm), $\beta=.85$ (NG1 VD5.11, §5.4, p200–204/PDF26–30)

**Nguồn và quyền điều chỉnh:** ký hiệu và hệ số nguyên giữ nguyên bản 5.11; không tự chọn $N,q,x$ bịa. Hệ số tại $\beta=.85=17/20$ tính từ phép lặp NG1, VD5.11.

**Đối tượng / đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn:**

| Đối tượng/đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị | Vai trò | Nguồn |
|---|---|---|---|---|---|
| Tổng số trang | $N$ | nguyên dương, $N\ge q+1$ | số đếm | quy mô đồ thị | NG1 bản 5.11 |
| Số trang hỗ trợ | $q$ | nguyên, $q\ge1$ | số đếm (**khác** vector $q_S$) | vùng hỗ trợ | NG1 bản 5.11 |
| Đóng góp ngoài | $x$ | đã gồm $\beta$ | số thực vô đơn vị | dòng vào đích từ ngoài cụm | NG1 bản 5.11 |
| Điểm đích | $y$ | nghiệm công thức | số thực vô đơn vị | đại lượng cần đánh giá | NG1 bản 5.11 |
| Điểm mỗi trang hỗ trợ | $z$ | $z=\beta y/q+(1-\beta)/N$ | số thực vô đơn vị | trung gian | NG1 bản 5.11 |
| Hệ số ngoài | $1/(1-\beta^2)$ | $400/111\approx3.6036$ tại $\beta=17/20$ | số thực vô đơn vị | mức khuếch đại | Tính từ phép lặp NG1, VD5.11 |
| Hệ số hỗ trợ | $\beta/(1+\beta)$ | $17/37\approx.4595$ tại $\beta=17/20$ | số thực vô đơn vị | đóng góp mỗi hỗ trợ | Tính từ phép lặp NG1, VD5.11 |

**Công thức chính xác và xấp xỉ:**
$$z=\beta\frac{y}{q}+\frac{1-\beta}{N},\qquad y=x+\beta q z+\frac{1-\beta}{N}$$
$$y_{\text{chính xác}}=\frac{x}{1-\beta^2}+\frac{\beta q+1}{N(1+\beta)},\qquad y_{\text{xấp xỉ}}=\frac{x}{1-\beta^2}+\frac{\beta q}{N(1+\beta)}$$
Sai khác giữa hai nghiệm: $\tfrac{1}{N(1+\beta)}$ — đây là tác động sau khi giải phương trình của hạng bị bỏ $(1-\beta)/N$, KHÔNG bằng chính hạng đó; hai nghiệm đều chia cho $1-\beta^2$.

**Lỗi dễ mắc, nhầm số, quyết định giữ số + bổ sung nhãn:**
- Nói "gấp khoảng 3.6 lần" (từ $400/111$), **không** nói "tăng thêm 360%".
- **Không** nói "tăng trang hỗ trợ khiến PageRank lớn tùy ý" — claim đã loại.
- $q$ là **số** trang hỗ trợ, $q_S$ là **vector** có chỉ số — nhãn khác nhau, không trộn.
- Xấp xỉ bỏ đúng hạng $(1-\beta)/N$ (phần dịch chuyển trực tiếp), không bỏ hạng $\beta q(1-\beta)/N$.

**Slide dùng lại:** `lec04-s03-03..07` (ý nghĩa $N,q,x,y,z$; ba thành phần trở về đích; giải chính xác/xấp xỉ; hệ số $\beta=.85$), `lec04-s03-08` (gán 4 hạng $x,\ \beta^2 y,\ \beta q(1-\beta)/N,\ (1-\beta)/N$ → nguồn nào, bỏ hạng nào ra xấp xỉ).

## Phiếu số ví dụ — phần 2: TrustRank/spam mass và HITS (VD3–VD4)

### VD3 — Spam mass trên G4, $\beta=.8$, $T=\{B,D\}$ (NG1 VD5.12, §5.4, p203–204/PDF29–30)

**Nguồn và quyền điều chỉnh:** giữ nguyên số nguồn VD5.12; **CẢNH BÁO hai thiết lập**: PageRank nền $r$ lấy từ PageRank **không hệ số suy giảm** (bài 5.2), còn $t$ lấy từ TrustRank **có hệ số suy giảm** $\beta=.8$ — bảng chỉ minh họa phép tỷ số, không cô lập riêng tác động của $T$. Không đổi PageRank nền để đẹp ví dụ.

**Đối tượng / đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn:**

| Đối tượng/đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị | Vai trò | Nguồn |
|---|---|---|---|---|---|
| PageRank nền | $r$ | $(\tfrac13,\tfrac29,\tfrac29,\tfrac29)$ | vector xác suất | mẫu so sánh | NG1 VD5.12 (PageRank không hệ số suy giảm, mục 5.2) |
| TrustRank | $t$ | $(\tfrac{54}{210},\tfrac{59}{210},\tfrac{38}{210},\tfrac{59}{210})$ | vector xác suất | mẫu so sánh | NG1 VD5.12, $\beta=.8$, $T=\{B,D\}$ |
| Spam mass | $s_p$ | $(\tfrac8{35},-\tfrac{37}{140},\tfrac{13}{70},-\tfrac{37}{140})$ | tỷ số vô đơn vị, có thể âm | kết quả | Tính từ phép lặp NG1, VD5.12 |

**Vết chạy chính xác (bảng vai trò gộp):**

| Đỉnh | $r_p$ | $t_p$ | $s_p=(r_p-t_p)/r_p$ | Trạng thái |
|---|---|---|---|---|
| A | $\tfrac13$ | $\tfrac{54}{210}$ | $\tfrac8{35}$ | dương |
| B | $\tfrac29$ | $\tfrac{59}{210}$ | $-\tfrac{37}{140}$ | **âm** ($t_B>r_B$) |
| C | $\tfrac29$ | $\tfrac{38}{210}$ | $\tfrac{13}{70}$ | dương |
| D | $\tfrac29$ | $\tfrac{59}{210}$ | $-\tfrac{37}{140}$ | **âm** ($t_D>r_D$) |

**Lỗi dễ mắc, nhầm số, quyết định giữ số + bổ sung nhãn:**
- Mass âm tại B và D nghĩa là $t_p>r_p$: chỉ nói được điều này trong bảng — không suy diễn "được đánh giá tin cậy hơn điểm nền" vì hai điểm có ý nghĩa/thiết lập khác nhau; không phải "trang chắc chắn rác".
- Mass **không phải xác suất**, không có ngưỡng chắc chắn; có thể âm, $\le1$ khi $t\ge0$.
- Hai thiết lập khác nhau (PageRank nền không hệ số suy giảm vs trust có hệ số suy giảm) — ghi cảnh báo trên slide, không trộn.
- Ứng dụng so kiểm soát cần **cùng $\beta$, cùng xử lý nút cụt** giữa điểm nền và trust.

**Slide dùng lại:** `lec04-s04-06..08` (bảng 5.17 với cảnh báo; tính A và B; câu hỏi mass âm $-37/140$ nghĩa gì).

### VD4 — HITS trên G5, khác G4 thay C→A bằng C→E (ví dụ nội bộ của dàn bài; nguồn sách NG1 Hình 5.18–5.20, §5.5, p204–208/PDF30–34)

**Nguồn và quyền điều chỉnh:** số vòng và giới hạn tính từ phép lặp theo MMDS §5.5, Hình 5.18–5.20 (phép tính kiểm nội bộ của dàn bài, không phải ví dụ số 4 của sách); giới hạn 32 vòng để chênh hai vòng của cả $h,a$ dưới $10^{-12}$ theo phép tính kiểm. Không làm tròn khác.

**Đối tượng / đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn:**

| Đối tượng/đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị | Vai trò | Nguồn |
|---|---|---|---|---|---|
| Đồ thị ví dụ | G5 | $n_H=5$, $m_H=8$; A→B,C,D; B→A,D; C→E; D→B,C; E không có cạnh ra | đồ thị có hướng | khác G4: thay C→A bằng C→E | NG1 Hình 5.18 (PDF32) |
| Ma trận kề | $L$ | $\begin{bmatrix}0&1&1&1&0\\ 1&0&0&1&0\\ 0&0&0&0&1\\ 0&1&1&0&0\\ 0&0&0&0&0\end{bmatrix}$ | ma trận 5×5, **hàng nguồn** (khác $P$ cột nguồn) | nhân $L^Th$, $La$ | NG1 Hình 5.19 (p206/PDF32) |
| Khởi | $h_0,a_0$ | $h_0=\mathbf{1}$, $a_0=\mathbf{0}$ | vector 5 chiều | $a_0$ chỉ đo chênh | NG1 §5.5 |
| Vòng 1 raw | $a_{raw},h_{raw}$ | $a_{raw}=(1,2,2,2,1)$; $h_{raw}=(3,\tfrac32,\tfrac12,2,0)$ | vector | trước chuẩn hóa | Tính từ phép lặp theo MMDS §5.5 (kiểm nội bộ VD4) |
| Vòng 1 scale | $a_1,h_1$ | $a_1=(\tfrac12,1,1,1,\tfrac12)$; $h_1=(1,\tfrac12,\tfrac16,\tfrac23,0)$ | vector, max 1 | sau chuẩn hóa | Tính từ phép lặp theo MMDS §5.5 (kiểm nội bộ VD4) |
| Vòng 2 raw | $a_{raw},h_{raw}$ | $a_{raw}=(\tfrac12,\tfrac53,\tfrac53,\tfrac32,\tfrac16)$; $h_{raw}=(\tfrac{29}{10},\tfrac65,\tfrac1{10},2,0)$ | vector | trước chuẩn hóa | Tính từ phép lặp theo MMDS §5.5 (kiểm nội bộ VD4) |
| Vòng 2 scale | $a_2,h_2$ | $a_2=(\tfrac3{10},1,1,\tfrac9{10},\tfrac1{10})$; $h_2=(1,\tfrac{12}{29},\tfrac1{29},\tfrac{20}{29},0)$ | vector, max 1 | sau chuẩn hóa | Tính từ phép lặp theo MMDS §5.5 (kiểm nội bộ VD4) |
| Giới hạn | $h^*,a^*$ | $h\approx(1,.3583,0,.7165,0)$; $a\approx(.2087,1,1,.7913,0)$ | vector, max 1 | hội tụ | Tính từ phép lặp theo MMDS §5.5 (kiểm nội bộ VD4; làm tròn 4 chữ số) |

**Vết chạy chính xác (bảng vai trò gộp, nhãn chuẩn hóa theo phần tử lớn nhất, trạng thái cũ/mới):**

| Vòng | $a_{raw}$ | $a$ (chuẩn hóa max) | $h_{raw}$ | $h$ (chuẩn hóa max) | Trạng thái |
|---|---|---|---|---|---|
| 1 | $(1,2,2,2,1)$ | $(\tfrac12,1,1,1,\tfrac12)$ | $(3,\tfrac32,\tfrac12,2,0)$ | $(1,\tfrac12,\tfrac16,\tfrac23,0)$ | cũ→mới |
| 2 | $(\tfrac12,\tfrac53,\tfrac53,\tfrac32,\tfrac16)$ | $(\tfrac3{10},1,1,\tfrac9{10},\tfrac1{10})$ | $(\tfrac{29}{10},\tfrac65,\tfrac1{10},2,0)$ | $(1,\tfrac{12}{29},\tfrac1{29},\tfrac{20}{29},0)$ | cũ→mới |
| giới hạn | — | $(.2087,1,1,.7913,0)$ | — | $(1,.3583,0,.7165,0)$ | hội tụ (≈ làm tròn 4 chữ số) |

**Lỗi dễ mắc, nhầm số, quyết định giữ số + bổ sung nhãn:**
- $h_E=0$ ngay vòng 1 vì E không có cạnh ra; nhưng $a_E=\tfrac12>0$ vì có C→E; $a_E$ vòng 2 $=\tfrac1{10}$ vì chuẩn $a_{raw}$ max $\tfrac53$.
- Giữ nhãn lần chuẩn hóa theo đúng thứ tự: $2,\ 3,\ \tfrac53,\ \tfrac{29}{10}$ — mỗi vòng max khác nhau, không quy đồng; không dùng $\tfrac12,\tfrac13$ rồi trộn với $\tfrac53$.
- Sai nhầm hướng cập nhật: nếu dùng $Lh_0$ thay $L^Th_0$ để tính $a$ sẽ cho $(1,\tfrac23,\tfrac13,\tfrac23,0)$ sau chuẩn hóa theo phần tử lớn nhất — $a_E=0$ sai dù C→E; đúng là $a_1=(\tfrac12,1,1,1,\tfrac12)$. $a$ từ $L^Th_{old}$ (không phải $Lh$), $h$ từ $La_{new}$.
- Không dựng $LL^T$/$L^TL$ vì có thể đặc; không nhầm G4 (bài tập) với G5 (ví dụ).

**Slide dùng lại:** `lec04-s05-03..07` (G5, tổng theo cạnh, raw/chuẩn hóa vòng 1 và 2, $L$ hàng nguồn), `lec04-s05-10` (giới hạn $\Theta(n_H+m_H)$/vòng, 2 quét cạnh + 2 quét max), `lec04-s05-11` (câu hỏi $h_E=0$, $a_E$ vòng 2).

## Phiếu số ví dụ — phần 3: bài tập trên lớp (VD5) và giới hạn

### VD5 — Recitation 3 bài (NG1 Bài 5.3.1, 5.4.2, 5.5.1), tổng 60 phút

**Nguồn và quyền điều chỉnh:** cả 3 bài từ NG1; đáp án tính bằng Fraction/giải hệ theo thuật toán kiểm NG1 (R1, R2, R3). Quy ước kế thừa được **nói rõ trên đề**: $\beta=.8$ kế thừa VD5.10 liền trước (R1), và $r_{base}$ không hệ số suy giảm như VD5.12 (R2) — đề không in lại, ghi quy ước minh bạch. Không tự tạo notebook/code.

**Đối tượng / đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn (chung):**

| Đối tượng/đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị | Vai trò | Nguồn |
|---|---|---|---|---|---|
| Đồ thị | G4 | như VD1, $n=4$, $m_G=8$ | đồ thị | nền cả 3 bài | NG1 Hình 5.1 |
| Hệ số | $\beta$ | $.8=4/5$ (R1, R2) | số thực vô đơn vị | kế thừa VD5.10 | NG1 Bài 5.3.1, 5.4.2 |
| Ma trận HITS | $L_4$ | $\begin{bmatrix}0&1&1&1\\ 1&0&0&1\\ 1&0&0&0\\ 0&1&1&0\end{bmatrix}$ | ma trận 4×4, hàng nguồn | R3 | NG1 Bài 5.5.1 |

**R1 — Bài 5.3.1 (p199/PDF25), 18 phút [6+8+4]:** tính TSP trên G4 khi $S=\{A\}$ và khi $S=\{A,C\}$, $\beta=.8$ (quy ước kế thừa VD5.10, đề không in lại). Sản phẩm: vector $q$, phương trình, nghiệm và tổng 1.

| Tập $S$ | $q$ | Nghiệm $r^*$ | Trạng thái |
|---|---|---|---|
| $\{A\}$ | $(1,0,0,0)$ | $(\tfrac37,\tfrac4{21},\tfrac4{21},\tfrac4{21})$ | tổng 1 |
| $\{A,C\}$ | $(\tfrac12,0,\tfrac12,0)$ | $(\tfrac{27}{70},\tfrac6{35},\tfrac{19}{70},\tfrac6{35})$ | tổng 1 |

**R2 — Bài 5.4.2 (p204/PDF30), 22 phút [3+10+6+3]:** G4, chỉ B tin cậy ($T=\{B\}$), $\beta=.8$; $r_{base}$ không hệ số suy giảm như VD5.12 là quy ước thừa kế, không giả đề ghi. (a) TrustRank từng trang; (b) spam mass từng trang. Dữ kiện cần $r_{base}$ trên mặt bài; lưu cảnh báo hai thiết lập.

| Đại lượng | Giá trị | Trạng thái |
|---|---|---|
| $t$ | $(\tfrac{198}{735},\tfrac{263}{735},\tfrac{116}{735},\tfrac{158}{735})$ | tổng 1 |
| $s_p$ | $(\tfrac{47}{245},-\tfrac{299}{490},\tfrac{71}{245},\tfrac8{245})$ | mass âm tại B |

**R3 — Bài 5.5.1 (p208/PDF34), 20 phút [4+10+3+3]:** tính $h$ và $a$ cho **G4 Hình 5.1, KHÔNG G5**. Hai vòng bảng trợ giúp trong ghi chú diễn giả nhưng đề cuối phải tính đến hội tụ: $h\approx(1,.3919,.1028,.7108)$, $a\approx(.2892,1,1,.8136)$; $\tau=.001$ là gợi ý tính gần đúng, không thay đề bằng 2 vòng; nguồn giữ nguyên; dùng máy tính/bảng tính nếu cần, không tự tạo notebook/code. Sản phẩm: hai vector chuẩn hóa theo phần tử lớn nhất (max 1) và cách lặp. Đây là slide kiểm tra riêng phần 7 (`lec04-s07-03`), không cộng thêm thời gian.

**Vết chạy R3 (bảng vai trò gộp, tính từ phép lặp NG1, R3):**

| Vòng | $a_{raw}$ | $a$ | $h_{raw}$ | $h$ | Trạng thái |
|---|---|---|---|---|---|
| 1 | $(2,2,2,2)$ | $(1,1,1,1)$ | $(3,2,1,2)$ | $(1,\tfrac23,\tfrac13,\tfrac23)$ | cũ→mới |
| 2 | $(1,\tfrac53,\tfrac53,\tfrac53)$ | $(\tfrac35,1,1,1)$ | $(3,\tfrac85,\tfrac35,2)$ | $(1,\tfrac8{15},\tfrac15,\tfrac23)$ | cũ→mới |
| hội tụ | — | $(.2892,1,1,.8136)$ | — | $(1,.3919,.1028,.7108)$ | 43 vòng để chênh hai vòng dưới $10^{-12}$ (≈ làm tròn 4 chữ số) |

**Lỗi dễ mắc, nhầm số, quyết định giữ số + bổ sung nhãn:**
- R1: hai tập $S$ cho hai vector $q$ khác nhau — nhãn tập $S$ trên từng cột, không trộn nghiệm.
- R2: mass âm tại B ($-\tfrac{299}{490}$) — cùng cảnh báo VD3, không coi là xác suất.
- R3: **G4 riêng**, không nhầm với G5 của VD4; $L_4$ khác $L$ của G5 (C→A giữ nguyên, không có E).
- Các số bài/slide không dùng làm tên đỉnh.

**Slide dùng lại:** `lec04-s07-01` (R1), `lec04-s07-02` (R2), `lec04-s07-03` (R3, kiểm tra riêng phần 7).

## Giới hạn của kế hoạch này

- Đây là **kế hoạch dàn bài**, chưa dựng HTML/SVG/CSS/note; mọi kết quả kiểm render cũ không gán cho bản này. Trạng thái chỉ là kế hoạch — không tuyên bố review đã chạy hay đã đạt.
- Khi triển khai cần rà lại: tác động note L04-N01…N07 (không tạo note mới), ánh xạ 51 mã kế hoạch với mã deck cũ, và các vùng CSS dùng lại (NG7) — những điểm này cần rà khi dựng thực tế.
- Số liệu đã đối chiếu với đặc tả; không tự làm tròn khác. Nếu khi dựng phát hiện va chạm số, quay lại phiếu này trước khi sửa slide.

## Kiểm mục tiêu → slide kiểm tra

| Mục tiêu | Slide kiểm tra | Năng lực được kiểm tra |
|---|---|---|
| Tiên quyết (hỗ trợ MT1) | `lec04-s01-06` | tính đúng đóng góp mỗi cạnh theo $\beta$ |
| MT1 | `lec04-s02-10` | phân biệt phần theo cạnh và phần dịch chuyển |
| MT2 | `lec04-s03-08` | gán ý nghĩa cho bốn số hạng của phương trình cân bằng cụm thao túng |
| MT3 | `lec04-s04-08` | diễn giải spam mass đúng, không coi là xác suất |
| MT4 | `lec04-s05-11` | nêu đúng hướng cập nhật luân phiên HITS |
| MT5 | `lec04-s06-04` | chọn đúng mô hình cho tình huống tích hợp |
| MT4 (HITS G4 riêng) | `lec04-s07-03` | chạy lặp HITS đến hội tụ trên G4 |


## Giai đoạn ghi chú và thực hành ngày 24/09/2026

### 1. Goal
Hoàn thiện ghi chú tự học và xây dựng bài thực hành Python cho Lecture 04, giúp sinh viên năm 3 tính, kiểm chứng và so sánh PageRank theo chủ đề, TrustRank/khối lượng rác và HITS.

### 2. Vấn đề trung tâm
Đồ thị liên kết thưa cần xếp hạng theo ngữ cảnh, giảm tác động của liên kết rác và phân biệt hai vai trò trang. Người học chuyển đặc tả thành phép quét cạnh, đối chiếu vết chạy tay và diễn giải đúng kết quả; đồ thị nhỏ dùng kiểm chứng công thức, không đo hiệu năng web.

### 3. Bằng chứng hoàn thành
- Ghi chú đủ nhu cầu, đặc tả, ví dụ, lập luận đúng, chi phí, giới hạn và tự kiểm trong phạm vi MMDS §5.3–5.5; đọc độc lập với slide.
- Ba bài nguồn giữ đúng dữ kiện và yêu cầu; hướng dẫn lập trình, thời lượng, ngưỡng dừng và mã ghi rõ do môn biên soạn.
- Python thư viện chuẩn tái lập các nghiệm phân số, hai vòng HITS và trạng thái dừng; có khung HITS cho sinh viên và kiểm tra tự chạy.
- Bài thực hành có dữ kiện, lệnh, sản phẩm, tiêu chí đối chiếu và hướng dẫn gập mặc định; tổng 60 phút.
- Năm báo cáo độc lập, quyết định xử lý và kiểm định số bằng oracle độc lập được lưu trong nhật ký.
- Viewer trên màn hình rộng/hẹp, công thức, hình, liên kết, bàn phím, in và index đạt; commit được đẩy lên origin/main.

### 4. Đầu ra
`materials/lec-04/lecture-note.md`, `materials/lec-04/exercises.md`; `materials/lec-04/code/link_analysis.py`, `hits_student.py`, `check_practice.py`, `practice-README.md`; ba tệp quy trình và tài nguyên thực hành ở `2627-1/index.html`. Dùng lại SVG Lecture 04 đã kiểm định; không cần SVG mới. Không sửa deck, CSS hay viewer nếu không phát hiện lỗi dùng chung liên quan.

### 5. Đối tượng và tiên quyết
Sinh viên năm 3 theo yêu cầu cụ thể đã áp dụng cho Lecture 04; biết Python, đồ thị có hướng, ma trận–vector, xác suất và Bài 03. Khôi phục ký hiệu $P:=S_{\text{Bài03}}$, tập $S$, hướng ma trận, chuẩn $L_1$ và chuẩn max. Không giả định biết định lý điểm bất động Banach, hệ phân tán hoặc thư viện xử lý đồ thị.

### 6. Phạm vi nguồn
| Nguồn | Phần | Vai trò |
|---|---|---|
| `sources/source.md` | Bài đề xuất 4, buổi gốc 5 | Phạm vi, mục tiêu, hoạt động cài HITS |
| MMDS 3e chương 5 | §5.3–5.5; Hình 5.1/5.15/5.18 | Đặc tả, dữ kiện, ví dụ, bài tập |
| MMDS bài tập | 5.3.1 tr.199/PDF25; 5.4.2 tr.204/PDF30; 5.5.1 tr.208/PDF34 | Ba đề gốc |
| MMDS slide linkanalysis1/2 | Các cụm đã ánh xạ và đối chiếu ở giai đoạn deck | Trực giác, cách biểu diễn; sách chốt chuẩn max |
| Stanford CS246 `10-spam.pdf` | Topic-sensitive PageRank, link spam, TrustRank | Đối chiếu cơ chế và giới hạn lựa chọn hạt giống |
| Cornell INFO4300, Ginsparg, 27/10/2009 | Slide 10, phương pháp lũy thừa | Căn cứ đối chiếu cho phác thảo hội tụ HITS đã có |

### 7. Bản đồ chủ đề
| ID | Chủ đề / nhãn | Mục tiêu và đầu vào | Đầu ra / phần sau | Nguồn, quyết định |
|---|---|---|---|---|
| `lec04-note-01` | Mục tiêu, đường học, ký hiệu / cầu nối | PageRank Bài03 | Phân biệt $P,L,S,q_S$; vào TSP | Bài03, MMDS5.3; giữ và thêm bảng tra |
| `lec04-note-02` | PageRank theo chủ đề / cốt lõi | Phân phối và đồ thị thưa | Tính $r$, bất biến, co, phối hợp; nền TrustRank | MMDS5.3; giữ, giải thích rõ chứng minh co |
| `lec04-note-03` | Cụm thao túng / cốt lõi | Cân bằng PageRank | Giải $y$, phân biệt chính xác/xấp xỉ; nhu cầu hạt giống | MMDS5.4.1–2; giữ |
| `lec04-note-04` | TrustRank và khối lượng rác / cốt lõi | TSP và mô hình thao túng | Tính $t,s$, phân biệt tín hiệu với kết luận phân loại | MMDS5.4.3–5; giữ |
| `lec04-note-05` | HITS / cốt lõi | Đồ thị và ma trận Boolean | Hai vector, vết, hội tụ theo hướng, chi phí | MMDS5.5, Cornell slide10; giữ |
| `lec04-note-06` | So sánh và chọn mô hình / cầu nối | Kết quả bốn cụm trên | Chọn mô hình và kiểm điều kiện áp dụng | Tổng hợp từ MMDS5.3–5.5; giữ hai bảng dễ đọc |
| `lec04-note-07` | Ba bài tập và triển khai / cốt lõi | Đặc tả và vết chạy tay | Sản phẩm lập trình kiểm chứng đúng đề nguồn | MMDS5.3.1,5.4.2,5.5.1; thêm thực hành riêng |

Đồ thị tiên quyết: 01→02→03→04; 01→05; (02,03,04,05)→06→07. Trong thực hành, đề 5.3.1→5.4.2 dùng lại bộ lặp; đề 5.5.1 thay cả hướng cộng và chuẩn hóa.

### 8. Chủ đề bổ sung đề xuất
- Đưa vào: mục tiêu/đường học/bảng ký hiệu để người học tự định hướng, nhãn phân biệt hai ma trận và các số trùng từ nguồn; vị trí sau mở đầu.
- Đưa vào: bước bất đẳng thức tam giác theo từng phần tử và biểu diễn chuỗi hình học của nghiệm TSP, là suy diễn từ phương trình MMDS §5.3.2 với $P$ cột tổng 1 và $0<\beta<1$, để không phải giả định đã biết định lý Banach; vị trí §2.4.
- Đưa vào: hướng dẫn lập trình và khung HITS trên ba bài nguồn; lấp khoảng trống từ giả mã đến mã thực thi trong yêu cầu mới.
- Loại khỏi đợt này: thêm Jaccard suy luận chủ đề, mở rộng TrustRank, Perron–Frobenius đầy đủ, dữ liệu trích dẫn mới; không cần để đạt mục tiêu đã chốt. Không thêm mục đọc thêm chỉ để dài tài liệu.

### 9. Khuôn trình bày
02/04/05: nhu cầu→đặc tả→ví dụ→trực quan→phát biểu bảo đảm→thuật toán→chứng minh→chi phí/giới hạn→kiểm tra. 04 dẫn lại chứng minh 02, không lặp. 03: nhu cầu→mô hình→hình→suy diễn→giới hạn→kiểm tra; thuật toán lặp riêng không áp dụng vì đây là giải phương trình cân bằng. 01/06/07 là định hướng/tổng hợp/luyện tập nên không tạo định lý và chứng minh rỗng.

### 10. Ngoài phạm vi
Không viết lại slide, không tạo notebook, không dùng thư viện ngoài Python chuẩn, không lấy dữ liệu web mới, không đo hiệu năng và không thay dữ kiện MMDS. Không khởi tạo `quill.json`. Không sửa tài liệu bài khác, `.env` hoặc các thay đổi người dùng đang có.

### 11. Rủi ro và điểm cần duyệt
Giữ các giá trị bằng nhau có ý nghĩa trong nguồn và gắn nhãn vai trò. Đề 5.4.2 dùng PageRank nền $\beta=1$ còn TrustRank $\beta=4/5$; không âm thầm dùng baseline khác. HITS có ba trạng thái và chuẩn max; $\tau$ chỉ đo độ thay đổi. Bài thực hành 60 phút là cách triển khai ba bài nguồn, không cộng thêm 60 phút vào deck 120+60 đã có. Mọi quyết định trong phạm vi được điều phối viên chấp nhận; không còn thiếu nguồn cần hỏi người dùng.

### 12. Kế hoạch tác tử
Reader `plan` và `source` chạy song song, reader `topic` riêng; đều `z-ai/glm-5.3-flash`, OpenRouter, chế độ JSON. Điều phối viên hợp nhất trước writer. Writer note rồi writer code/thực hành chạy tuần tự trong thư mục tạm. Năm reviewer độc lập chạy song song; editor sau hợp nhất; rà lại toán và mạch nếu sửa tương ứng. Điều phối viên kiểm số/CLI/viewer, áp dụng tệp đã đạt, thêm index, commit/push.

### 13. Trạng thái
Sẵn sàng soạn: nguồn và phạm vi đã đủ; điều phối viên duyệt ngày 24/09/2026. Đây là cổng soạn, chưa phải kết luận kiểm định hay bàn giao.
