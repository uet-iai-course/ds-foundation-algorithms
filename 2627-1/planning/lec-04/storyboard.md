# Bảng phân cảnh — Bài 04: PageRank theo chủ đề, liên kết rác và HITS

> **Trạng thái:** đặc tả đã triển khai ngày 24/09/2026 thành 51 slide, 51 ghi chú diễn giả và tài liệu tự học. Các quyết định bố cục dưới đây cùng mục điều chỉnh triển khai là căn cứ của bản phát hành; kết quả kiểm định xem review-log.md.

## Trạng thái kế hoạch

- **Quy mô đã chốt:** 7 phần; 48 slide giảng / 120 phút + 3 slide bài tập / 60 phút = 51 slide, mã `lec04-sXX-YY`.
- **Bảng tổng thời gian:**

| Phần | Nội dung | Slide | Phút | Thời lượng từng slide (phút) | Slide kiểm tra |
|---|---|---|---|---|---|
| S01 | Giới thiệu bài học | 6 | 10 | 1, 1, 2, 2, 2, 2 | s01-06 |
| S02 | PageRank theo chủ đề | 10 | 25 | 2, 2, 2, 3, 2, 3, 3, 3, 3, 2 | s02-10 |
| S03 | Cụm thao túng liên kết | 8 | 22 | 2, 3, 2, 3, 4, 3, 3, 2 | s03-08 |
| S04 | TrustRank và khối lượng rác | 8 | 21 | 2, 3, 3, 2, 3, 3, 3, 2 | s04-08 |
| S05 | Hai vai trò của HITS | 11 | 30 | 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2 | s05-11 |
| S06 | Tổng kết và kiểm tra | 5 | 12 | 2, 2, 2, 5, 1 | s06-04 |
| S07 | Bài tập trên lớp | 3 | 60 | 18, 22, 20 | s07-03 (kiểm tra riêng phần 7; slide 01, 02 cũng là hoạt động bài tập) |
| **Tổng** | | **51** | **180** | | |

- **Kiểm tra riêng theo phần:** s01-06 (tiên quyết, hỗ trợ MT1), s02-10 (MT1), s03-08 (MT2), s04-08 (MT3), s05-11 (MT4), s06-04 (MT5), s07-03 (MT4 trên G4, đến hội tụ). Không cộng thêm thời gian ngoài bảng.
- **Ký hiệu cần nhắc ở mở bài:** $S$ ở Bài 03 là ma trận sửa nút cụt; ở Bài 04, $S$ là **tập đỉnh** chủ đề. Cầu nối $P := S_{\text{Bài03}}$ (cùng cột nguồn, cột cụt thay bằng $u=\mathbf{1}/n$); G4 không nút cụt nên $P=M_0$. Trong phần cụm thao túng, $q$ là **số** trang hỗ trợ, khác $q_S$ là **vector** có chỉ số.
- **Nhắc về khối lượng:** $\beta P r$ có tổng $\beta$, phần dịch chuyển $(1-\beta)q_S$ có tổng $1-\beta$; chỉ vector $r$ và $q_S$ mới có tổng 1. Không nói "betaPr có tổng 1".

## Bản đồ hành trình các cụm

### Cụm 1 — PageRank theo chủ đề (S02)

1. **Bước ánh xạ ID:** tình huống/vấn đề jaguar ở s01-03 → so chi phí hai hướng ở s01-04 → s02-01 (trực giác nhảy về tập đại diện) → s02-02 (G4, $S=\{B,D\}$, $q_S$) → s02-03 ($\beta P r_0$ theo cạnh) → s02-04 (cộng dịch chuyển → $r_1$) → s02-05 ($r_2$ và $r^*$) → s02-06 (đặc tả tổng quát) → s02-07 (giả mã thưa) → s02-08 (bất biến + co $L_1$) → s02-09 (k chủ đề, chi phí) → s02-10 (kiểm tra).
2. **Kiến thức đầu vào:** ma trận $P:=S_{\text{Bài03}}$ từ Bài 03 (s01-05 nhắc lại), G4 và $\beta=4/5$ từ VD5.10, khái niệm vector phân bố.
3. **Sản phẩm:** đặc tả $r'=\beta Pr+(1-\beta)q_S$ (HT1), giả mã biểu diễn thưa với bù nút cụt đều, tính tuyến tính k chủ đề (HT3), chi phí $O(kI(n+m_G))$.
4. **Tình huống dữ liệu/quy mô:** đồ thị Web lớn, thưa; ví dụ tính tay trên G4 ($n=4$, $m_G=8$); quy mô ký hiệu $n, m_G, k, I$ — không bịa số Web thực.
5. **Tiên quyết/đầu ra:** tiên quyết là đóng góp theo cạnh $\beta r_j/d_j$ và $\beta$ (kiểm ở s01-06); đầu ra là nền cho TrustRank (S04 dùng lại bất biến/co) và cho MT5 (so mô hình ở S06).
6. **Kết nối:** nhận từ s01-03/s01-04 (vấn đề chủ đề và chi phí hai hướng) và s01-06 (mỗi cạnh đóng góp $\beta r_j/d_j$); sau kiểm tra s02-10, chuyển sang s03-01 (tín hiệu liên kết vẫn có thể bị thao túng) và s04-03 (quy tắc trust cùng dạng).
7. **Dữ kiện từ ví dụ sang đặc tả/giả mã/chứng minh:** dãy $r_0\to r_1\to r_2\to r^*$ của VD1 (s02-02..05) cung cấp dữ kiện cho đặc tả HT1 (s02-06); giả mã s02-07 khái quát đúng phép tính đã chạy tay; chứng minh s02-08 dùng chính cấu trúc $\beta Pr + (1-\beta)q_S$ vừa thấy.
8. **Bước gộp/không áp dụng:** không có bước gộp; S01 là phần mở bài/tiên quyết (nhắc trước qua s01-06), không phải cụm thuật toán mới — chu trình 8 bước không áp dụng toàn bộ cho S01; không dựng hình mới — G4 vẽ lại theo Hình 5.1 khi dựng.

### Cụm 2 — Cụm thao túng liên kết / cụm thao túng (S03)

1. **Bước ánh xạ ID:** s03-01 (giới hạn tín hiệu) → s03-02 (Hình 5.16 ba vùng) → s03-03 ($N,q,x,y$) → s03-04 ($z$ mỗi trang hỗ trợ) → s03-05 (ba thành phần về đích) → s03-06 (nghiệm chính xác + xấp xỉ) → s03-07 ($\beta=.85$, hệ số, giới hạn, chi phí) → s03-08 (kiểm tra gán hạng).
2. **Kiến thức đầu vào:** PageRank cơ sở và vai trò phần dịch chuyển (từ S02), ký hiệu $N,q,x,y,z$ của bản 5.11.
3. **Sản phẩm:** phương trình cụm thao túng và nghiệm chính xác $y=\dfrac{x}{1-\beta^2}+\dfrac{\beta q+1}{N(1+\beta)}$, xấp xỉ sách bỏ $(1-\beta)/N$, sai khác $\dfrac{1}{N(1+\beta)}$ (HT4).
4. **Tình huống dữ liệu/quy mô:** mô hình ba vùng (không thể tác động / có thể tác động / các trang sở hữu; đích và $q$ trang hỗ trợ cùng nằm trong vùng sở hữu, mỗi trang hỗ trợ chỉ trỏ đích, không trỏ chéo); không chọn $N,q,x$ tự bịa — dùng hệ số nguyên bản 5.11; tại $\beta=17/20$: hệ số ngoài $400/111\approx3.6036$, hệ số nhân $q/N$ là $\beta/(1+\beta)=17/37\approx.4595$.
5. **Tiên quyết/đầu ra:** tiên quyết là hiểu dòng chảy theo cạnh và phần dịch chuyển; đầu ra là động lực cho TrustRank (S04) và hạng số cho câu hỏi s03-08, s06-04.
6. **Kết nối:** nhận từ s02-10 (kiểm tra cuối phần 2); nhả sang s04-01 (phòng vệ sau khi hiểu tấn công).
7. **Dữ kiện từ ví dụ sang đặc tả/chứng minh:** ba thành phần trở về đích (s03-05) là dữ kiện; s03-06 giải phương trình từng bước thành HT4; s03-07 chuyển nghiệm thành hệ số và giới hạn diễn giải.
8. **Bước gộp/không áp dụng:** cụm này **phân tích mô hình, không có giả mã thao túng** — không áp dụng bước thuật toán; chi phí chỉ là đánh giá biểu thức $O(1)$ khi đã biết $x$; bản đồ S03 phản ánh ba vùng đúng của Hình 5.16 (đích và $q$ trang hỗ trợ cùng trong vùng sở hữu, mỗi trang hỗ trợ chỉ trỏ đích, không trỏ chéo) — minh họa lấy SVG hiện có `hinh-5-16-cum-thao-tung.svg` đúng nguồn.

### Cụm 3 — TrustRank và khối lượng rác (S04)

1. **Bước ánh xạ ID:** s04-01 (giả thiết cô lập gần đúng) → s04-02 (chọn $T$, cân bằng chất lượng/độ phủ) → s04-03 (quy tắc từ TSP) → s04-04 (lỗi hạt giống + thiên lệch, gộp một slide) → s04-05 (định nghĩa mass — tỷ số phụ trợ dùng lại dữ kiện đã tính, không thuộc chu trình trọng tâm của TrustRank) → s04-06 (bảng 5.17, cảnh báo hai thiết lập) → s04-07 (tính A và B) → s04-08 (kiểm tra mass âm).
2. **Kiến thức đầu vào:** toàn bộ máy TSP từ S02 (bất biến, co, chi phí — dùng lại, không chứng minh trùng), G4 và $\beta=4/5$.
3. **Sản phẩm:** quy tắc $t'=\beta Pt+(1-\beta)q_T$, $q_T=e_T/|T|$; spam mass $s_p=(r_p-t_p)/r_p$ là **tỷ số phụ trợ dùng lại dữ kiện $r_p$, $t_p$ đã tính**, đứng ngoài chu trình trọng tâm của TrustRank (chu trình chỉ là phép lặp của $t$), với giới hạn âm/$\le1$/không xác suất (HT5).
4. **Tình huống dữ liệu/quy mô:** tập tin cậy $T$ là đầu vào được thẩm định; VD5.12 với **cảnh báo hai thiết lập** (PageRank nền không hệ số suy giảm, trust có $\beta=.8$).
5. **Tiên quyết/đầu ra:** tiên quyết là TSP và ý nghĩa cụm thao túng; đầu ra là công cụ phòng vệ, nền so sánh cho phần kế tiếp S05 (HITS — mô hình khác PageRank) và dữ kiện cho câu hỏi s04-08, s06-04.
6. **Kết nối:** nhận trực tiếp từ s02-08 (cùng bất biến) và s03-01 (nhu cầu phòng vệ); nhả sang s05-01 (HITS làm phần kế tiếp, khác PageRank toàn Web) rồi s06-01 (bảng 4 mô hình).
7. **Dữ kiện từ ví dụ sang đặc tả/chứng minh:** bảng 5.17 và phép tỷ số tại A, B (s04-06..07) là dữ kiện; s04-05 phân tích tỷ số thành phát biểu về dấu và giới hạn; bất biến/co **không chứng minh lại** — ghi rõ dùng lại HT2.
8. **Bước gộp:** lỗi hạt giống và thiên lệch gộp chung s04-04 vì cùng một trực giác "sai số nguồn lan theo liên kết"; không áp dụng bước giả mã riêng (thuật toán trùng TSP); S04 dùng lại **G4/S={B,D} đã tính ở S02** (VD1, s02-02..05) cho VD3 — đừng tính lại: chu trình 8 bước không áp dụng toàn bộ cho S04 vì phần lớn nội dung là dùng lại máy TSP, phần mới chỉ là chọn $T$, quy tắc trust và tỷ số mass phụ trợ.

### Cụm 4 — HITS hai vai trò (S05)

1. **Bước ánh xạ ID:** s05-01 (phạm vi đồ thị con) → s05-02 (VD 5.13, định nghĩa $h,a$) → s05-03 (G5, Hình 5.18, tổng theo cạnh) → s05-04 (raw $a$, $a_1$) → s05-05 (raw $h$, $h_1$) → s05-06 ($L$, hàng nguồn — hàng $i$ của $L^T$ liệt kê nguồn $j\to i$) → s05-07 (vòng 2) → s05-08 (giả mã, biên, dừng) → s05-09 (vector riêng, điều kiện đủ) → s05-10 (chi phí) → s05-11 (kiểm tra).
2. **Kiến thức đầu vào:** đồ thị có hướng, nhân ma trận–vector, ý tưởng phương pháp lũy thừa (đối chiếu NG5 slide 10).
3. **Sản phẩm:** quy tắc luân phiên $a_{raw}=L^Th_{old}\to$ chuẩn hóa theo phần tử lớn nhất $\to a_{new}$; $h_{raw}=La_{new}\to$ chuẩn hóa theo phần tử lớn nhất $\to h_{new}$ (HT6); điều kiện đủ hội tụ (HT7); chi phí $\Theta(n_H+m_H)$/vòng (HT8).
4. **Tình huống dữ liệu/quy mô:** đồ thị con đã chọn theo truy vấn; ví dụ G5 ($n_H=5$, $m_H=8$); cách chọn graph nằm ngoài tuyến chính — không khẳng định HITS chỉ chạy được trên đồ thị nhỏ.
5. **Tiên quyết/đầu ra:** tiên quyết là nhân ma trận và trực giác hai vai trò; đầu ra là nửa còn lại của bảng so sánh ở S06 và bài tập R3 (s07-03).
6. **Kết nối:** nhận từ s05-01 (khác PageRank toàn Web); nhả hai vector chuẩn hóa theo phần tử lớn nhất 1 cho s06-01 và s07-03.
7. **Dữ kiện từ ví dụ sang đặc tả/chứng minh:** hai vòng raw/scale của VD4 (s05-04..07) là dữ kiện; s05-08 khái quát thành thuật toán với check max 0 và cờ dừng; s05-09 nêu điều kiện đủ (hướng trội duy nhất $\lambda_1>\lambda_2\ge0$, khởi có hình chiếu khác 0) — ghi chú chứng minh, không giả thiết sinh viên biết Perron–Frobenius.
8. **Bước gộp/không áp dụng:** không dựng $LL^T$/$L^TL$ (có thể đặc); không dùng chuẩn hóa L2 của slide 55 NG3 — chọn chuẩn hóa theo max và cập nhật luân phiên của sách; không suy hội tụ từ vài vòng; S05 là cụm thuật toán mới duy nhất trong bài — chu trình 8 bước áp dụng trọn vẹn ở đây.

---

#### lec04-s01-01 — Trang tiêu đề bài 04

- **Vai trò và mục tiêu:** mở bài; định vị bài trong chuỗi: Bài 03 đã cho PageRank cơ sở, bài này trả lời ba hạn chế của nó. Hỗ trợ CLO2, mở đường MT1–MT5.
- **Luận điểm trung tâm:** một tín hiệu liên kết duy nhất chưa đủ — cần xếp hạng theo chủ đề, hiểu thao túng, và phân vai hub/authority.
- **Nội dung cụ thể:** tiêu đề theo mẫu gồm tên môn, học kỳ và tên bài "Bài 04 — PageRank theo chủ đề, liên kết rác và HITS"; dòng phụ: MMDS Ch.5 §5.3–5.5; ba từ khóa: xếp hạng theo chủ đề, cụm thao túng liên kết, hai vai trò HITS.
- **Bố cục đã chọn:** Dải trên 25% đặt tên học phần “Giải thuật nền tảng của Khoa học dữ liệu” và “Học kỳ 1, 2026–2027” theo lớp tên môn/học kỳ của mẫu; vùng giữa 60% đặt tên Bài 04 và ba từ khóa, căn giữa; dải dưới 15% đặt nguồn MMDS. Không hình.
- **Trọng tâm và thứ tự đọc:** tiêu đề trước, rồi ba từ khóa, cuối cùng dòng nguồn.
- **Lý do phù hợp sinh viên năm 3:** sinh viên vừa xong Bài 03 với ma trận sửa nút cụt; nêu ngay ba từ khóa giúp họ gắn bài mới vào cái đã biết thay vì cảm thấy bắt đầu lại.
- **Giới hạn bố cục:** Mặt slide gồm tên môn, học kỳ, tên bài, ba từ khóa và nguồn; chưa dùng ký hiệu toán. Phần giải thích ba hạn chế để các trang động lực.
- **Ví dụ và số liệu:** không áp dụng — slide định vị, không có phép tính.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận bối cảnh từ Bài 03; nhả ba từ khóa cho s01-02 (mục lục) và s01-03 (truy vấn jaguar).
- **Nguồn:** NG0 sources/source.md (Bài 4 đề xuất); NG1 trang đầu chương 5.
- **Thời lượng:** 1 phút (chào, đọc tiêu đề, nêu một câu "hôm nay trả lời ba hạn chế").
- **Ghi chú soạn:** nói chậm ba từ khóa; không giải thuật toán nào ở đây; nhắc sẽ đổi ký hiệu $S$ so với Bài 03 để tránh sốc ở s01-05.

#### lec04-s01-02 — Mục lục 7 phần

- **Vai trò và mục tiêu:** Định vị bảy phần; khi giảng, nêu bằng lời rằng mỗi phần có kiểm tra và cuối bài có bài tập. Mã và ánh xạ mục tiêu chỉ dùng trong tệp kế hoạch.
- **Luận điểm trung tâm:** ba mô hình xếp hạng, mỗi mô hình một câu trả lời cho một hạn chế, khép lại bằng so sánh và bài tập.
- **Nội dung cụ thể:** 7 tên phần, không số phút, không ID slide, không mã kiểm tra, không nhãn quy trình: 1 Giới thiệu; 2 PageRank theo chủ đề; 3 Cụm thao túng liên kết; 4 TrustRank và khối lượng rác; 5 Hai vai trò của HITS; 6 Tổng kết và kiểm tra; 7 Bài tập trên lớp.
- **Bố cục đã chọn:** hai cột tên phần (4 + 3) chiếm 70% giữa, mỗi dòng: số thứ tự — tên phần; không tạo hộp tra ID; thời lượng và mã slide kiểm tra (s01-06, s02-10, s03-08, s04-08, s05-11, s06-04, s07-03) giữ ở tệp kế hoạch, không lên mặt.
- **Trọng tâm và thứ tự đọc:** Đọc cột trái từ phần 1 đến 4, rồi cột phải từ phần 5 đến 7; các số thứ tự giữ hướng đọc nhất quán.
- **Lý do phù hợp sinh viên năm 3:** Hai cột 4+3 tên ngắn giúp sinh viên đã biết PageRank nhận ra ba bước mở rộng: chủ đề, thao túng–phòng vệ, hai vai trò; phần bài tập ở cuối tách rõ bước vận dụng.
- **Giới hạn bố cục:** Mặt slide chỉ bảy tên phần; không hiển thị mã slide, mã mục tiêu hoặc số phút. Các mã chỉ ở tệp kế hoạch; thời lượng điều phối giữ ở trường Thời lượng và ghi chú dành cho giảng viên.
- **Ví dụ và số liệu:** không áp dụng — chỉ tổng thời gian 120' + 60' đã chốt.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận ba từ khóa từ s01-01; mỗi dòng mục lục trỏ đúng phần tương ứng, dòng 2 mở s02-01.
- **Nguồn:** NG0 sources/source.md (thứ tự đề xuất Bài 4); bảng 7 phần đã duyệt trong đặc tả.
- **Thời lượng:** 1 phút (đọc lướt 7 dòng, nhấn "mỗi phần có một slide kiểm tra").
- **Ghi chú soạn:** không đọc từng dòng; chỉ chỉ 3 trụ: phần 2 (thuật toán), phần 3–4 (tấn công–phòng vệ), phần 5 (mô hình khác). Nhắc phần 7 là làm bài, mang máy tính.

#### lec04-s01-03 — Truy vấn jaguar: một từ, hai chủ đề

- **Vai trò và mục tiêu:** tạo nhu cầu cho PageRank theo chủ đề; MT1 được đặt lên nền động lực này.
- **Luận điểm trung tâm:** PageRank cơ sở cho mỗi trang một điểm duy nhất, không biết trang nói về con vật hay chiếc xe.
- **Nội dung cụ thể:** truy vấn *jaguar*; hai thẻ chủ đề của sách: "động vật" (mèo lớn châu Mỹ) và "ô tô"; PageRank cơ sở xếp theo liên kết, không theo chủ đề truy vấn; vấn đề xếp hạng cần thể hiện chủ đề. Hoạt động: **Câu hỏi:** *jaguar* gợi ý nghĩa nào — phân loại hai ý nghĩa vào hai thẻ chủ đề. (Không liệt kê dòng mô tả trang web tự tạo — chỉ dùng hai thẻ chủ đề của sách.)
- **Bố cục đã chọn:** trái 45%: hộp truy vấn chữ *jaguar* lớn; phải 55%: hai thẻ chủ đề "động vật" và "ô tô" của sách (mỗi thẻ chỉ nhãn tên chủ đề, không liệt kê dòng mô tả trang web tự tạo); dưới cùng dải 1 dòng: "PageRank cơ sở: một điểm/trang, không phân chủ đề". Nhãn chữ hai thẻ, không chỉ màu.
- **Trọng tâm và thứ tự đọc:** hộp truy vấn trước, rồi hai thẻ chủ đề song song, cuối dòng kết luận.
- **Lý do phù hợp sinh viên năm 3:** ví dụ lịch sử quen thuộc (NG1 p195) giúp sinh viên thấy ngay giới hạn của công cụ mình vừa học ở Bài 03; chỗ dễ nhầm là tưởng cần đổi thuật toán hoàn toàn — bài này sẽ chỉ cần đổi vector dịch chuyển.
- **Giới hạn bố cục:** mặt slide chỉ nêu vấn đề; lịch sử thuật ngữ và chi tiết công cụ tìm kiếm thời 2000s để ghi chú.
- **Ví dụ và số liệu:** không áp dụng số — ví dụ định tính từ NG1 p195 (ví dụ lịch sử).
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận "một điểm/trang" từ Bài 03; nhả vấn đề "xếp hạng cần thể hiện chủ đề" cho s01-04 (bộ nhớ vector) và s02-01.
- **Nguồn:** NG1 §5.3, p195/PDF21 (ví dụ jaguar, ví dụ lịch sử).
- **Thời lượng:** 2 phút (hoạt động "Câu hỏi:" phân loại hai ý nghĩa của *jaguar* vào hai thẻ chủ đề, thu 2–3 câu trả lời, chốt hai thẻ).
- **Ghi chú soạn:** bước nói: hỏi trước — cho sinh viên phân loại — mới chỉ hai thẻ chủ đề; sai lầm cần chặn: "đổi từ khóa truy vấn là xong" — vấn đề nằm ở điểm số của trang, không phải câu hỏi.

#### lec04-s01-04 — Bộ nhớ: một vector riêng mỗi người hay k vector chủ đề

- **Vai trò và mục tiêu:** nêu cái giá của hai hướng giải quyết; đặt $n, U, k$ làm quy mô ký hiệu. Hỗ trợ MT5 (so chi phí) từ sớm.
- **Luận điểm trung tâm:** lưu vector riêng cho từng người dùng tốn $O(Un)$; lưu theo chủ đề chỉ tốn $O(kn)$ với $k$ nhỏ.
- **Nội dung cụ thể:** hai ô so sánh: (a) cá nhân hóa theo người: $U$ người × vector dài $n$ → $O(Un)$; (b) theo chủ đề: $k$ chủ đề × vector dài $n$ → $O(kn)$, cộng $O(Uk)$ nếu lưu trọng số người trên chủ đề. Ký hiệu: $n$ số trang, $U$ số người, $k$ số chủ đề — chỉ ký hiệu quy mô, không bịa số thực.
- **Bố cục đã chọn:** hai ô ngang bằng nhau mỗi ô 48% chiều rộng, giữa chừa 4%; ô trái "theo người", ô phải "theo chủ đề"; mỗi ô 3 dòng: ý tưởng, bộ nhớ, hệ quả; dòng dưới cùng: chú thích ký hiệu $n, U, k$.
- **Trọng tâm và thứ tự đọc:** ô trái trước (cái đắt), ô phải sau (cái rẻ), chú thích ký hiệu cuối.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 đã quen đếm bộ nhớ theo biến; đặt $O(Un)$ cạnh $O(kn)$ ngay từ đầu giúp họ hiểu vì sao bài chọn hướng chủ đề, không phải vì thuật toán "hay hơn".
- **Giới hạn bố cục:** mặt slide chỉ hai ô và dòng ký hiệu; phân tích $O(kI(n+m_G))$ đầy đủ để cho s02-09.
- **Ví dụ và số liệu:** không áp dụng số cụ thể — dùng ký hiệu quy mô theo đặc tả, không bịa $n/U/k$ số thực.
- **Hình thức hóa:** không áp dụng định lý; chỉ biểu thức bộ nhớ quy mô $O(Un)$ vs $O(kn+Uk)$.
- **Kết nối vào–ra cụ thể:** nhận câu hỏi chủ đề từ s01-03; nhả ký hiệu $k$ cho s02-09 (k chủ đề) và s06-02 (so chi phí).
- **Nguồn:** NG1 §5.3 (so sánh lưu k vector chủ đề); đặc tả đã duyệt mục chi phí.
- **Thời lượng:** 2 phút (đọc ô trái 1', ô phải 1').
- **Ghi chú soạn:** nhấn "lưu k vector O(kn) ngoài graph"; sai lầm dễ mắc: tưởng $k$ phải bằng $U$ — giải thích $k$ là số chủ đề chọn trước, nhỏ.

#### lec04-s01-05 — Mục tiêu, tiên quyết và cầu nối ký hiệu

- **Vai trò và mục tiêu:** chốt MT1–MT5 ngắn gọn; xử lý cầu nối $P:=S_{\text{Bài03}}$ và đổi ký hiệu $S$.
- **Luận điểm trung tâm:** từ PageRank cơ sở sang PageRank theo chủ đề chỉ đổi một chi tiết — vector dịch chuyển; các phần sau (HITS) đổi mô hình sâu hơn.
- **Nội dung cụ thể:** (1) Mục tiêu: tính PageRank theo chủ đề, giải phương trình cụm thao túng, tính TrustRank và khối lượng rác, chạy HITS và nêu điều kiện hội tụ, chọn mô hình cho tình huống. (2) Tiên quyết: đồ thị có hướng, ma trận–vector, xác suất cơ bản và ma trận sửa nút cụt của Bài 03. (3) Cầu nối: $P:=S_{\text{Bài03}}$ giữ cột nguồn và bù đều $u=\mathbf{1}/n$; $S$ ở Bài 04 là tập đỉnh chủ đề. G4 không có nút cụt nên $P=M_0$.
- **Bố cục đã chọn:** Trái 40%: năm câu mục tiêu ngắn, không kèm nhãn MT; phải 60%: ô tiên quyết ở trên và ô cầu nối ký hiệu ở dưới. Ô cầu nối đặt $P:=S_{\text{Bài03}}$ cạnh dòng “$S$ ở bài này là tập đỉnh chủ đề”; nhấn bằng nhãn chữ, không chỉ màu.
- **Trọng tâm và thứ tự đọc:** hộp phải trước (cầu nối ký hiệu là chỗ vấp), danh sách MT sau.
- **Lý do phù hợp sinh viên năm 3:** kế hoạch cũ nói "P đã học" là sai — sinh viên chỉ biết $S$ ma trận của Bài 03; ghi rõ hai nghĩa của $S$ ngay từ đầu tránh nhầm khi thấy $S=\{B,D\}$ ở phần 2.
- **Giới hạn bố cục:** mặt slide mỗi MT một dòng ngắn; phát biểu đầy đủ MT ở ghi chú; không đưa công thức TSP lên đây.
- **Ví dụ và số liệu:** không áp dụng — slide định tuyến.
- **Hình thức hóa:** không áp dụng; chỉ nêu quy ước ký hiệu.
- **Kết nối vào–ra cụ thể:** nhận ma trận sửa nút cụt từ Bài 03 (NG6); nhả $P$ và cảnh báo ký hiệu cho s02-02 và toàn bộ S02–S05.
- **Nguồn:** NG6 Lecture03 note §2–3 (ma trận thô $M_0$, ma trận sửa $S$); NG1 §5.3 p195.
- **Thời lượng:** 2 phút (1' cầu nối, 1' đọc 5 MT).
- **Ghi chú soạn:** nói rõ: "trong bài này khi thấy $S=\{B,D\}$ thì đó là tập đỉnh"; nhắc $q_S$ sẽ là vector, $q$ ở phần 3 là số — sẽ nhắc lại khi gặp.

#### lec04-s01-06 — Kiểm tra tiên quyết: đóng góp mỗi cạnh

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 1; đo năng lực tính đóng góp theo cạnh — nền của MT1.
- **Luận điểm trung tâm:** cạnh $j\to i$ đóng góp vào đích số $\beta r_j/d_j$ (khai thác trọng số chuyển $\beta/d_j$ nhân điểm nguồn $r_j$ — hai đại lượng khác nhau); tổng điểm có $\beta$ lẫn dịch chuyển bằng 1.
- **Nội dung cụ thể (đề trên mặt slide):** cho G4 (vẽ sẵn bên trái), trang B có điểm $r_B=\tfrac12\ge0$, bậc ra 2, $\beta=\tfrac45$, và giả thiết dữ kiện: $r\ge0$, tổng $r$ bằng 1, đồ thị không có nút cụt ($P$ đã là ma trận sửa nút cụt). Câu hỏi: (i) mỗi cạnh B→đích đóng góp bao nhiêu vào đích (theo $\beta r_B/d_B$)? (ii) vì sao tổng điểm của cả hệ vẫn bằng 1 khi có cả phần theo $\beta$ lẫn phần dịch chuyển (dựa trên dữ kiện đã cho, không tự suy từ riêng $r_B=\tfrac12$)?
- **Bố cục đã chọn:** trái 40%: đồ thị G4 với nhãn A, B, C, D và 8 cạnh; phải 60%: hộp câu hỏi 2 dòng (i), (ii) và dòng dữ kiện "r ≥ 0, tổng r = 1, đồ thị không nút cụt; điểm B = 1/2, bậc ra 2, β = 4/5"; không có đáp án trên mặt.
- **Trọng tâm và thứ tự đọc:** đọc dữ kiện trước (dòng dưới hộp), rồi hai câu hỏi; đồ thị chỉ để tra bậc ra.
- **Lý do phù hợp sinh viên năm 3:** thao tác "nhân điểm nguồn $r_j$ với trọng số chuyển $\beta/d_j$" là kỹ năng Bài 03; nếu quên điểm nguồn, các phép nhân $P r$ tiếp theo sẽ sai; câu (ii) chuẩn bị trực giác cho hai khối lượng $\beta$ và $1-\beta$; cần phân biệt rõ đóng góp $\beta r_j/d_j$ với trọng số chuyển $\beta/d_j$.
- **Giới hạn bố cục:** mặt slide chỉ đề và G4; lời giải đầy đủ và bảng đóng góp từng đỉnh để ghi chú.
- **Ví dụ và số liệu:** dùng G4 (NG1 Hình 5.1, PDF4); giá trị: điểm B $=\tfrac12$, bậc ra của B là 2, $\beta=\tfrac45$; không dùng $q_S$.
- **Hình thức hóa:** không áp dụng định lý; công thức đóng góp $\beta r_j/d_j$ (phân biệt với trọng số chuyển $\beta/d_j$).
- **Kết nối vào–ra cụ thể:** nhận quy tắc đóng góp theo cạnh $\beta r_j/d_j$ (trọng số chuyển $\beta/d_j$ nhân điểm nguồn) từ Bài 03; nhả trực giác "tổng = $\beta\cdot(\text{theo cạnh}) + (1-\beta)\cdot(\text{dịch chuyển})$" cho s02-04.
- **Nguồn:** NG1 Hình 5.1 p178/PDF4 (G4); NG6 Lecture03 (quy tắc ma trận chuyển).
- **Câu hỏi đủ dữ kiện:** có — điểm B, bậc ra B, $\beta$ đều cho trên mặt slide; G4 vẽ sẵn.
- **Đáp án (trong ghi chú):** (i) mỗi cạnh từ B đóng góp $\beta r_B/d_B=\tfrac45\cdot\tfrac12\cdot\tfrac12=\tfrac15$ (hai cạnh B→A, B→D; khai thác dữ kiện $r\ge0$, tổng 1, không nút cụt đã cho). (ii) phần theo cạnh có tổng $\beta=\tfrac45$, phần dịch chuyển có tổng $1-\beta=\tfrac15$; hai khối lượng cộng lại đúng 1 — nhấn rằng $\beta Pr$ có tổng $\beta$, không phải 1.
- **Tiêu chí đánh giá:** đúng $\tfrac15$ mỗi cạnh theo công thức $\beta r_B/d_B$; giải thích được hai khối lượng bổ sung dựa trên dữ kiện đã cho; lỗi cho thấy hiểu sai: quên nhân điểm nguồn $r_B$ (chỉ dùng trọng số $\beta/d_B$), hoặc nói "betaPr có tổng 1".
- **Thời gian hoạt động:** trong 2 phút: 1' suy nghĩ cá nhân, 30" trả lời nhanh (giơ bảng/đọc), 30" chữa.
- **Thời lượng:** 2 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** nếu nhiều sinh viên sai (ii), dừng 30 giây vẽ hai cột khối lượng $\tfrac45$ và $\tfrac15$ trước khi sang phần 2; không giới thiệu $q_S$ sớm.

#### lec04-s02-01 — Trực giác: người đọc chủ đề nhảy về tập đại diện

- **Vai trò và mục tiêu:** mở phần 2; chuyển từ nhu cầu "xếp hạng cần thể hiện chủ đề" (s01-03/s01-04) sang cơ chế "dịch chuyển về tập đại diện". Hỗ trợ MT1.
- **Luận điểm trung tâm:** thay vì nhảy ngẫu nhiên khắp Web, người đọc quan tâm một chủ đề chỉ nhảy về các trang đại diện chủ đề đó.
- **Nội dung cụ thể:** mô tả người đọc ngẫu nhiên: với xác suất $\beta$ đi theo liên kết, với xác suất $1-\beta$ "nhảy" — nhưng nhảy về đâu? Trả lời: về tập đại diện chủ đề $S$. Câu chốt: điểm số của trang giờ phụ thuộc chủ đề.
- **Bố cục đã chọn:** giữa 55%: sơ đồ 3 lớp — hàng trên "người đọc chủ đề", hàng giữa "Web (các mũi tên theo cạnh)", hàng dưới hộp "tập đại diện $S$" với mũi tên nhảy từ người đọc xuống; phải 45%: 3 dòng trực giác: đi theo cạnh / nhảy về $S$ / điểm theo chủ đề.
- **Trọng tâm và thứ tự đọc:** sơ đồ trước (thấy mũi tên nhảy), 3 dòng phải sau.
- **Lý do phù hợp sinh viên năm 3:** sinh viên đã biết phép đi ngẫu nhiên của Bài 03; chỉ cần đổi **nơi nhảy** — trực giác này tránh cảm giác học thuật toán mới hoàn toàn; chỗ dễ nhầm: tưởng nhảy về một trang duy nhất.
- **Giới hạn bố cục:** mặt slide chỉ trực giác; công thức $r'=\beta Pr+(1-\beta)q_S$ để cho s02-06.
- **Ví dụ và số liệu:** không áp dụng số — slide trực giác; ví dụ số bắt đầu s02-02.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận vấn đề "xếp hạng cần thể hiện chủ đề" từ s01-03/s01-04; nhả khái niệm tập đại diện $S$ cho s02-02.
- **Nguồn:** NG1 §5.3 p195–196/PDF21–22; NG3 slide 7–11 (trực giác chủ đề).
- **Thời lượng:** 2 phút (kể tình huống người đọc 1', chốt 3 dòng 1').
- **Ghi chú soạn:** dùng ví dụ jaguar: người đọc chủ đề "ô tô" nhảy về các trang ô tô uy tín; sai lầm cần chặn: "nhảy về trang điểm cao nhất" — nhảy về tập đại diện do người soạn chủ đề chọn.

#### lec04-s02-02 — G4, tập chủ đề S={B,D} và vector q_S

- **Vai trò và mục tiêu:** thiết lập toàn bộ dữ kiện số của phần 2; định nghĩa $q_S$. Nền MT1.
- **Luận điểm trung tâm:** $q_S$ là phân bố đều trên tập $S$; ở ví dụ này chọn luôn $r_0=q_S$ làm khởi tạo.
- **Nội dung cụ thể:** G4: A→B,C,D; B→A,D; C→A; D→B,C; $n=4$, $m_G=8$; $P=M_0$ (không nút cụt). $S=\{B,D\}$; $q_S=(0,\tfrac12,0,\tfrac12)$, tổng 1 (vector xác suất); $\beta=\tfrac45$ (VD5.10); $r_0=q_S$.
- **Bố cục đã chọn:** trái 45%: đồ thị G4 với 4 đỉnh nhãn A–D, 8 cạnh, hai đỉnh B, D có khung viền nhãn chữ "S"; phải 55%: bảng 3 dòng: $S=\{B,D\}$; $q_S=(0,\tfrac12,0,\tfrac12)$ tổng 1; $r_0=q_S$, $\beta=\tfrac45$. Dòng chú thích: "$\tfrac12$ ở đây là xác suất khởi trên tập $S$".
- **Trọng tâm và thứ tự đọc:** đồ thị trước (nhìn B, D được khoanh), bảng sau; đọc $q_S$ theo thứ tự đỉnh A, B, C, D cố định.
- **Lý do phù hợp sinh viên năm 3:** đây là lần đầu $S$ xuất hiện dạng tập — sinh viên dễ lẫn với ma trận $S$ Bài 03; khoanh viền trên đồ thị + nhãn chữ giúp gắn "tập đỉnh" với hình; thứ tự đỉnh cố định tránh lẫn vị trí phần tử $q_S$.
- **Giới hạn bố cục:** mặt slide chỉ dữ kiện và $q_S$; phép tính $\beta Pr_0$ để cho s02-03; không hiện $r_1$ sớm.
- **Ví dụ và số liệu:** VD1 (NG1 VD5.10, p197–199/PDF23–25): G4, $S=\{B,D\}$, $q_S=(0,\tfrac12,0,\tfrac12)$, $\beta=\tfrac45$, $r_0=q_S$.
- **Hình thức hóa:** không áp dụng định lý; nêu điều kiện $q_S\ge0$, $\sum q_S=1$, $S\ne\emptyset$ (một phần của HT1, đầy đủ ở s02-06).
- **Kết nối vào–ra cụ thể:** nhận $P=M_0$ và cảnh báo ký hiệu từ s01-05; nhả $r_0, \beta, P$ cho s02-03.
- **Nguồn:** NG1 VD5.10, §5.3, p197–199/PDF23–25; Hình 5.1 p178/PDF4.
- **Thời lượng:** 2 phút (đọc đồ thị 1', đọc $q_S$ và nhấn tổng 1 1').
- **Ghi chú soạn:** bước nói: chỉ đỉnh B, D thuộc chủ đề → mỗi đỉnh được $\tfrac12$; sai lầm dễ mắc: viết $q_S=(\tfrac12,\tfrac12,0,0)$ theo thứ tự B, D — nhắc thứ tự đỉnh A, B, C, D luôn cố định.

#### lec04-s02-03 — Tính βPr₀ theo từng cạnh

- **Vai trò và mục tiêu:** chạy tay phần theo cạnh của vòng 1; thao tác nhân ma trận–vector cụ thể. Nền MT1.
- **Luận điểm trung tâm:** mỗi đỉnh nhận tổng các đóng góp $\beta\cdot r_{0,u}/d_u$ từ các cạnh đi vào.
- **Nội dung cụ thể:** với $r_0=q_S=(0,\tfrac12,0,\tfrac12)$, mỗi đỉnh nhận tổng các đóng góp $\beta r_j/d_j$ từ các cạnh đi vào (G4 không có cạnh D→A):

  | Đích | Cạnh vào | Đóng góp $\beta r_j/d_j$ | Kết quả |
  |---|---|---|---|
  | A | B→A, C→A | $\beta\cdot\tfrac12\cdot\tfrac12 + \beta\cdot\tfrac{0}{1} = \tfrac15 + 0$ | $\tfrac15$ |
  | B | A→B, D→B | $\beta\cdot\tfrac{0}{3} + \beta\cdot\tfrac12\cdot\tfrac12 = 0 + \tfrac15$ | $\tfrac15$ |
  | C | A→C, D→C | $\beta\cdot\tfrac{0}{3} + \beta\cdot\tfrac12\cdot\tfrac12 = 0 + \tfrac15$ | $\tfrac15$ |
  | D | A→D, B→D | $\beta\cdot\tfrac{0}{3} + \beta\cdot\tfrac12\cdot\tfrac12 = 0 + \tfrac15$ | $\tfrac15$ |

  Vậy $\beta Pr_0=(\tfrac15,\tfrac15,\tfrac15,\tfrac15)$; tổng phần này $=\beta=\tfrac45$ (khối lượng, không phải phân bố).
- **Bố cục đã chọn:** trái 45%: G4 giữ nguyên vị trí như s02-02, cạnh đi vào mỗi đỉnh được đánh số thứ tự đóng góp (nhãn ①②…, không dùng màu); phải 55%: bảng 4 hàng (A, B, C, D) × cột "cạnh vào", "đóng góp $\beta r_j/d_j$" và "kết quả", mỗi kết quả $\tfrac15$; dòng dưới: "tổng = 4/5 = β".
- **Trọng tâm và thứ tự đọc:** bảng phải là trọng tâm; đồ thị trái để tra cạnh; đọc theo hàng A→D.
- **Lý do phù hợp sinh viên năm 3:** sinh viên hay nhân nhầm $P^T$; bảng "các đóng góp" theo đích giúp thấy mỗi hàng là tổng theo cạnh đi vào, đúng chiều $P$ (cột nguồn); dòng tổng $=\beta$ chuẩn bị cho s02-04.
- **Giới hạn bố cục:** mặt slide chỉ vòng 1 phần theo cạnh; phép nhân ma trận đầy đủ $P$ hiện cả ma trận trong ghi chú, không dồn lên mặt.
- **Ví dụ và số liệu:** VD1: $\beta Pr_0=(\tfrac15,\tfrac15,\tfrac15,\tfrac15)$, tổng $\tfrac45$ (NG1 VD5.10).
- **Hình thức hóa:** công thức $\beta Pr$; lưu ý $\|\beta Pr\|_1=\beta$ khi $\|r\|_1=1$ (dẫn tới HT2).
- **Kết nối vào–ra cụ thể:** nhận $r_0,\beta,P$ từ s02-02; nhả vector $(\tfrac15,\tfrac15,\tfrac15,\tfrac15)$ cho s02-04 cộng dịch chuyển.
- **Nguồn:** NG1 VD5.10, p197–199/PDF23–25.
- **Thời lượng:** 2 phút (tính đỉnh A cùng lớp 1', các đỉnh còn lại nhanh 1').
- **Ghi chú soạn (thử lỗi để kiểm phân biệt số):** chọn đỉnh A, liệt kê cạnh đi vào (B→A, C→A); nếu lớp nhân $P^T$ thay $P$ với $r_0=(0,\tfrac12,0,\tfrac12)$, $\beta=\tfrac45$ thì kết quả sai là $r_{1\text{sai}}=(\tfrac4{15},\tfrac3{10},0,\tfrac3{10})$, tổng $\tfrac{13}{15}$ (đã cộng phần dịch chuyển, chỉ sai chiều nhân ma trận); nếu dùng đúng $P$ nhưng bỏ dịch chuyển, tổng là $4/5$ — dùng để phân biệt hai lỗi; đúng vẫn là $\tfrac15$ cho A.

#### lec04-s02-04 — Cộng phần dịch chuyển: r₁

- **Vai trò và mục tiêu:** hoàn tất vòng 1; cho thấy vai trò của $(1-\beta)q_S$. Trọng tâm MT1.
- **Luận điểm trung tâm:** $r_1=\beta Pr_0+(1-\beta)q_S$ — phần dịch chuyển bù đúng lượng còn thiếu để tổng về 1.
- **Nội dung cụ thể:** $(1-\beta)q_S=\tfrac15\cdot(0,\tfrac12,0,\tfrac12)=(0,\tfrac1{10},0,\tfrac1{10})$, tổng $\tfrac15$ (vector khối lượng); cộng: $r_1=(\tfrac15,\tfrac3{10},\tfrac15,\tfrac3{10})$, tổng 1 (vector xác suất). Nhãn: $\tfrac12$ trong $q_S$ là xác suất khởi; $\tfrac1{10}$ là phần bổ sung dịch chuyển $(1-\beta)\cdot\tfrac12$ — hai giá trị khác ý nghĩa.
- **Bố cục đã chọn:** ba cột ngang: cột trái 30% lặp lại $\beta Pr_0=(\tfrac15,\tfrac15,\tfrac15,\tfrac15)$ nhãn "theo cạnh"; cột giữa 30% $(0,\tfrac1{10},0,\tfrac1{10})$ nhãn "dịch chuyển"; cột phải 40% $r_1$ nhãn "tổng", mỗi phần tử viết $\tfrac15+\tfrac1{10}=\tfrac3{10}$ kiểu; dòng dưới: hai khối lượng $\tfrac45+\tfrac15=1$.
- **Trọng tâm và thứ tự đọc:** cột trái → giữa → phải; dòng tổng cuối cùng chốt.
- **Lý do phù hợp sinh viên năm 3:** phép cộng theo thành phần là thao tác quen; bố cục ba cột tách rõ hai khối lượng giúp tránh lỗi "quên dịch chuyển → tổng 0.8" đã liệt kê trong kiểm số; nhãn riêng cho $\tfrac12$ và $\tfrac1{10}$ chống trộn.
- **Giới hạn bố cục:** mặt slide chỉ vòng 1; dãy $r_2, r_3$ để cho s02-05; không hiện công thức tổng quát.
- **Ví dụ và số liệu:** VD1: $(1-\beta)q_S=(0,\tfrac1{10},0,\tfrac1{10})$ (khối lượng, tổng $\tfrac15$); $r_1=(\tfrac15,\tfrac3{10},\tfrac15,\tfrac3{10})$ (xác suất, tổng 1) (NG1 VD5.10).
- **Hình thức hóa:** công thức $r'=\beta Pr+(1-\beta)q_S$ xuất hiện lần đầu ở dạng cụ thể; đặc tả đầy đủ ở s02-06.
- **Kết nối vào–ra cụ thể:** nhận $\beta Pr_0$ từ s02-03; nhả $r_1$ cho s02-05 và là đáp án slide kiểm tra s02-10.
- **Nguồn:** NG1 VD5.10, p197–199/PDF23–25.
- **Thời lượng:** 3 phút (1' tính $(1-\beta)q_S$, 1' cộng theo thành phần, 1' kiểm tổng và phân biệt hai nhãn).
- **Ghi chú soạn:** sai lầm cần chặn: lấy $\tfrac12$ trong $q_S$ trộn với $\tfrac1{10}$; hỏi lớp "tổng của phần dịch chuyển là bao nhiêu?" — phải là $\tfrac15$, không phải 1.

#### lec04-s02-05 — Vòng 2 và nghiệm giới hạn r*

- **Vai trò và mục tiêu:** cho thấy lặp hội tụ và phân biệt nghiệm giải hệ với kết quả vòng lặp. Hoàn thành MT1 về mặt số.
- **Luận điểm trung tâm:** lặp đủ nhiều vòng hội tụ về $r^*$; $r^*$ là nghiệm giải hệ, không phải "vòng 3".
- **Nội dung cụ thể:** $r_2=(\tfrac{42}{150},\tfrac{41}{150},\tfrac{26}{150},\tfrac{41}{150})$; $r_3=(\tfrac{62}{250},\tfrac{71}{250},\tfrac{46}{250},\tfrac{71}{250})$; nghiệm $r^*=(\tfrac{54}{210},\tfrac{59}{210},\tfrac{38}{210},\tfrac{59}{210})$ — nhãn "giới hạn (giải hệ)", không gán là vòng 3. Giữ phân số nguồn, mẫu 150/250/210 khác nhau có lý do; $r_B=r_D=\tfrac{59}{210}$ do $r_{B,0}=r_{D,0}$ và cùng phần dịch chuyển — quan hệ được phép lặp bảo toàn.
- **Bố cục đã chọn:** bảng 5 hàng ($r_0, r_1, r_2, r_3, r^*$) × 4 cột đỉnh A–D + cột "trạng thái" (khởi / 1 vòng / 2 vòng / 3 vòng / giới hạn); bảng chiếm 70% giữa; hàng $r^*$ có khung nhãn "giải hệ"; phải 30%: G4 thu nhỏ giữ vị trí như các slide trước.
- **Trọng tâm và thứ tự đọc:** đọc bảng theo hàng từ $r_0$; dừng ở hàng $r^*$ và đọc nhãn "giới hạn"; không so mẫu số giữa các hàng.
- **Lý do phù hợp sinh viên năm 3:** sinh viên hay gán nghiệm cho vòng cuối mình thấy; nhãn "giải hệ" tách rời hai khái niệm "lặp gần đúng" và "nghiệm chính xác"; giữ phân số nguồn tránh sai số làm tròn khi đối chiếu bài tập.
- **Giới hạn bố cục:** mặt slide chỉ bảng và nhãn; cách giải hệ để ghi chú; không nói "hội tụ sau 3 vòng".
- **Ví dụ và số liệu:** VD1: $r_2, r_3, r^*$ như trên (NG1 VD5.10; nghiệm giải hệ bằng Fraction).
- **Hình thức hóa:** không áp dụng định lý; nêu $r^*$ thỏa $r^*=\beta Pr^*+(1-\beta)q_S$ (dẫn tới HT1, HT2).
- **Kết nối vào–ra cụ thể:** nhận $r_1$ từ s02-04; nhả $r^*$ cho s02-08 (bất biến) và $t$ của VD3 ở s04-06.
- **Nguồn:** NG1 VD5.10, p197–199/PDF23–25.
- **Thời lượng:** 2 phút (1' đọc $r_2, r_3$, 1' nhấn nhãn $r^*$).
- **Ghi chú soạn:** nói: "$r_3$ chưa phải nghiệm; $r^*$ đến từ giải hệ"; sai lầm: quy đồng ép cùng mẫu rồi so sánh nhầm; nhắc $r_B=r_D=\tfrac{59}{210}$ do $r_{B,0}=r_{D,0}$ và cùng phần dịch chuyển — quan hệ được phép lặp bảo toàn, không gán cho đối xứng đồ thị chưa chứng minh.

#### lec04-s02-06 — Đặc tả tổng quát TSP

- **Vai trò và mục tiêu:** hình thức hóa từ dữ kiện vừa tính; phát biểu đầy đủ điều kiện. HT1.
- **Luận điểm trung tâm:** mọi phép tính vừa chạy là trường hợp riêng của $r'=\beta Pr+(1-\beta)q_S$ với điều kiện chặt.
- **Nội dung cụ thể:** đặc tả: $r'=\beta Pr+(1-\beta)q_S$ với $q_S\ge0$, $\sum q_S=1$, $S\ne\emptyset$, $\beta\in(0,1)$, $n\ge1$; $P$ không âm, cột tổng 1. Đối chiếu từng điều kiện với ví dụ: $q_S=(0,\tfrac12,0,\tfrac12)$ thỏa; $\beta=\tfrac45\in(0,1)$. Nhắc khối lượng: $\beta Pr$ tổng $\beta$, $(1-\beta)q_S$ tổng $1-\beta$; chỉ $r$ và $q_S$ tổng 1.
- **Bố cục đã chọn:** trên 45%: khối công thức $$r'=\beta Pr+(1-\beta)q_S$$ và dòng điều kiện; dưới 55%: bảng 2 cột "điều kiện" ↔ "giá trị ở ví dụ" 5 hàng ($q_S$, $S$, $\beta$, $n$, $P$).
- **Trọng tâm và thứ tự đọc:** công thức trước, bảng đối chiếu sau; đọc bảng theo hàng để thấy mỗi điều kiện đều có hiện thân.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 cần thấy điều kiện không phải trang trí — mỗi điều kiện dùng ở bước sau ($\beta<1$ cho phép co, $S\ne\emptyset$ để $q_S$ tồn tại); bảng đối chiếu giúp chuyển từ "nhớ công thức" sang "kiểm điều kiện".
- **Giới hạn bố cục:** mặt slide chỉ đặc tả và bảng đối chiếu; chứng minh bất biến để s02-08; không đưa giả mã lên đây.
- **Ví dụ và số liệu:** VD1 dùng làm cột đối chiếu; không thêm số mới.
- **Hình thức hóa:** HT1 — đặc tả TSP (NG1 §5.3).
- **Kết nối vào–ra cụ thể:** nhận dữ kiện từ s02-02..05; nhả đặc tả cho s02-07 (giả mã) và s04-03 (TrustRank cùng dạng).
- **Nguồn:** NG1 §5.3, p196–199/PDF22–25.
- **Thời lượng:** 3 phút (1' đọc công thức, 2' bảng đối chiếu).
- **Ghi chú soạn:** hỏi nhanh lớp: "vì sao cần $S\ne\emptyset$?" — vì $q_S$ phải là phân bố; sai lầm: nói "$\beta Pr$ có tổng 1" — sửa ngay bằng hai khối lượng.

#### lec04-s02-07 — Giả mã: biểu diễn thưa, bù nút cụt, dừng

- **Vai trò và mục tiêu:** chuyển đặc tả thành thuật toán chạy được; chuẩn bị cho CLO3. HT1 áp dụng.
- **Luận điểm trung tâm:** một vòng lặp = nhân thưa + bù nút cụt đều + cộng dịch chuyển; dừng theo ngưỡng hoặc số vòng.
- **Nội dung cụ thể (giả mã 9 dòng):**
  1. Nhận đồ thị $G$ có $n\ge1$ đỉnh, $q_S$, $\beta\in(0,1)$, $\tau>0$, $K_{max}\ge1$ nguyên; $q_S$ là phân bố xác suất.
  2. Đặt $r\leftarrow q_S$, tính bậc ra $d_j$; $u=\mathbf{1}/n$.
  3. Với $k=1,\ldots,K_{max}$, thực hiện các dòng 4–8:
  4. $\delta\leftarrow\sum_{j:d_j=0}r_j$.
  5. $r_{new}\leftarrow\beta M_0r+\beta\delta u+(1-\beta)q_S$.
  6. $\epsilon\leftarrow\|r_{new}-r\|_1$.
  7. Nếu $\epsilon\le\tau$, trả $(r_{new},\text{đạt ngưỡng})$.
  8. Gán $r\leftarrow r_{new}$ để bắt đầu vòng tiếp theo.
  9. Sau vòng lặp, trả $(r,\text{chưa đạt ngưỡng})$.
- **Bố cục đã chọn:** Khối giả mã chiếm toàn chiều rộng và 80% vùng nội dung; thụt dòng 4–8 dưới vòng lặp. Dải dưới 20% có ba nhãn ngắn: “tính lại khối lượng nút cụt”, “ngưỡng chênh hai vòng”, “trả vector và trạng thái”. Giữ thang chữ của mẫu; giải thích dài ở ghi chú.
- **Trọng tâm và thứ tự đọc:** Đọc từ đầu vào đến vòng lặp; theo phần thụt dòng để nhận ra khối lượng nút cụt được tính lại, rồi đọc hai lối trả kết quả.
- **Lý do phù hợp sinh viên năm 3:** Sinh viên đã biết vòng lặp PageRank; khối thụt dòng làm rõ trạng thái nào được tính lại. Hai lối trả kết quả phân biệt đạt ngưỡng với hết số vòng, tránh gọi mọi lần dừng là hội tụ.
- **Giới hạn bố cục:** mặt slide giữ khối 9 dòng; chứng minh $\|Pv\|_1\le\|v\|_1$ và phân tích chi phí để s02-08, s02-09; không code thật.
- **Ví dụ và số liệu:** không chạy số mới — giả mã khái quát đúng phép tính VD1 đã chạy tay (s02-03..05).
- **Hình thức hóa:** HT1 dạng thuật toán; điều kiện dừng $\|r_{new}-r\|_1\le\tau$ hoặc $K_{max}$.
- **Kết nối vào–ra cụ thể:** nhận đặc tả HT1 từ s02-06; nhả cấu trúc vòng lặp cho s04-03 (TrustRank chỉ đổi $q_S\to q_T$) và s05-08 (so với HITS).
- **Nguồn:** NG1 §5.3, p198–199/PDF24–25 (phép lặp, bù nút cụt); NG6 Lecture03 (bù nút cụt đều).
- **Thời lượng:** 3 phút (1' dòng 1–3, 1' dòng 4–6, 1' dòng 7–9 và hai cờ).
- **Ghi chú soạn:** Giải thích dòng 5 bằng ba phần đã học: nhân thưa $M_0r$, bù đều $\delta u$ và dịch chuyển theo $q_S$. Khối lượng $\delta$ lấy từ $r$ hiện tại; không đặt ngoài vòng lặp. $\tau$ đo chênh hai vòng, không phải sai số tuyệt đối tới nghiệm. Khi hết $K_{max}$, vector $r$ đã nhận lần cập nhật cuối.

#### lec04-s02-08 — Bất biến xác suất và phép co L₁

- **Vai trò và mục tiêu:** chứng minh ngắn hai tính chất bảo đảm lặp có nghiệm và hội tụ. HT2.
- **Luận điểm trung tâm:** tổng khối lượng được giữ nguyên và phép ánh xạ $F$ co khoảng cách giữa hai điểm theo $\beta<1$, ép dãy lặp về một điểm giới hạn.
- **Nội dung cụ thể:** (1) Bất biến: $\mathbf{1}^T(\beta Pr)=\beta\,\mathbf{1}^Tr=\beta$ (vì cột $P$ tổng 1) và $\mathbf{1}^T((1-\beta)q_S)=1-\beta$; cộng lại tổng 1; các thành phần đều không âm vì $P,r,q_S\ge0$. (2) Co $L_1$ qua hiệu hai ảnh: với $F(r)=\beta Pr+(1-\beta)q_S$, $$\|F(r)-F(s)\|_1=\beta\|P(r-s)\|_1\le\beta\|r-s\|_1,$$ trong đó $\|Pv\|_1\le\|v\|_1$ vì $\|Pv\|_1=\sum_i|\sum_jP_{ij}v_j|\le\sum_j|v_j|\sum_iP_{ij}=\|v\|_1$ (dùng $P\ge0$, cột tổng 1). Hai điểm bất kỳ cách nhau co với hệ số không quá $\beta$ mỗi vòng (phần dịch chuyển triệt tiêu khi lấy hiệu) → dãy lặp là Cauchy, $r^*$ tồn tại và duy nhất. **Giả thiết dùng:** $P\ge0$, cột $P$ tổng 1, $\beta\in(0,1)$, $q_S$ phân bố; **bất biến bảo toàn:** không âm và tổng 1. Lưu ý: $r^*$ có thể có phần tử 0 khi $q_S$ hỗ trợ con — không tuyên bố dương mọi trang.
- **Bố cục đã chọn:** hai khối dọc: khối trên 45% "bất biến" với 2 dòng phép tính; khối dưới 55% "co L₁ qua F(r)−F(s)" với 3 dòng: chuỗi đẳng thức $\|F(r)-F(s)\|_1\le\beta\|r-s\|_1$, hệ quả co theo $\beta$, kết luận $r^*$ duy nhất; dòng cuối nhỏ: "phần tử 0 có thể xảy ra".
- **Trọng tâm và thứ tự đọc:** khối trên trước (dễ), khối dưới sau; đọc dòng kết luận "duy nhất" cuối cùng.
- **Lý do phù hợp sinh viên năm 3:** hai chuỗi đẳng thức–bất đẳng thức ngắn vừa sức; Bài 03 đã dạy phép co nên đây là dùng lại dạng hiệu $F(r)-F(s)$, không phải lần đầu gặp khái niệm; chỗ dễ nhầm: tưởng co nghĩa là mọi phần tử giảm — co là khoảng cách giữa hai trạng thái.
- **Giới hạn bố cục:** mặt slide 2 khối ngắn; chi tiết dãy Cauchy và chứng minh đầy đủ để ghi chú mở rộng; không đưa định lý cố định điểm.
- **Ví dụ và số liệu:** đối chiếu VD1: tổng $r_1=\tfrac45+\tfrac15=1$ — dữ kiện đã thấy ở s02-04 dùng làm kiểm chứng khối trên.
- **Hình thức hóa:** HT2 — bất biến xác suất và co $L_1$; dùng lại cho TrustRank (s04-03) không chứng minh trùng.
- **Kết nối vào–ra cụ thể:** Nhận đặc tả và phép lặp từ s02-06–07; giải thích tính đúng của phép lặp, chuyển sang chi phí ở s02-09. TrustRank ở s04-03 dùng lại kết quả này.
- **Nguồn:** NG1 §5.3, p198/PDF24 (phép lặp); NG6 Bài 03, ghi chú §2–3 (bất biến và phép co), áp dụng cho phân bố dịch chuyển đã cố định.
- **Thời lượng:** 3 phút (1' bất biến, 2' co và duy nhất).
- **Ghi chú soạn:** bước nói: viết $\mathbf{1}^TP$ = vector hàng chứa tổng từng cột → nhân với $r$ cho $\mathbf{1}^Tr$; sai lầm: chứng minh "$\|Pv\|_1=\|v\|_1$" — chỉ có $\le$; giả thiết cần nêu đủ: $P\ge0$, cột $P$ tổng 1, $\beta\in(0,1)$, $q_S$ phân bố; ý Cauchy dùng cận cấp số nhân theo chênh hai vòng liên tiếp; tính duy nhất nhờ $\beta<1$.

#### lec04-s02-09 — k chủ đề: tính tuyến tính, phối hợp và chi phí

- **Vai trò và mục tiêu:** mở rộng từ 1 chủ đề sang k; cầu nối sang MT5. HT3, HT8 (phần TSP).
- **Luận điểm trung tâm:** tính trước k vector, lúc truy vấn chỉ phối hợp tuyến tính với trọng số cho trước, theo chi phí đã ghi ở bảng.
- **Nội dung cụ thể:** chạy TSP cho $k$ chủ đề với cùng $P$, cùng $\beta$: được $r_1^{(l)},\dots$; vì phương trình tuyến tính theo $q$, $r^*=\sum_l\alpha_l r^{(l)*}$ với $\alpha_l\ge0$, $\sum\alpha_l=1$ là nghiệm cho $q=\sum\alpha_l q_l$ (tính tuyến tính của vector, giải thích ngắn). Chi phí: 1 vòng $\Theta(n+m_G)$; $k$ chủ đề $I$ vòng $O(kI(n+m_G))$; lưu $O(kn)$ ngoài graph; phối hợp khi truy vấn: mỗi trang $O(k)$, toàn vector $O(kn)$ — so với cá nhân hóa $O(Un)$: $O(kn+Uk)$ nếu lưu trọng số người.
- **Bố cục đã chọn:** trên 50%: công thức phối hợp $$r^*=\sum_{l=1}^{k}\alpha_l\, r^{(l)*},\quad \alpha_l\ge0,\ \sum_l\alpha_l=1$$ kèm dòng "cùng $P$, cùng $\beta$"; dưới 50%: bảng 3 hàng chi phí: 1 vòng / k chủ đề / so cá nhân hóa, cột "phép toán" và "độ phức tạp".
- **Trọng tâm và thứ tự đọc:** công thức trước (ý chính), bảng chi phí sau; đọc hàng "k chủ đề" làm mốc.
- **Lý do phù hợp sinh viên năm 3:** sinh viên đã thấy $O(Un)$ ở s01-04; bảng này khép vòng: hướng chủ đề tính trước k vector và cho phép trộn chủ đề lúc truy vấn với chi phí $O(k)$ mỗi trang; chỗ dễ nhầm: tưởng phải chạy lại lặp cho từng người dùng.
- **Giới hạn bố cục:** mặt slide chỉ công thức và bảng; giải thích "suy ra tuyến tính" ngắn trong ghi chú, không định lý phô trương.
- **Ví dụ và số liệu:** không chạy số — dùng ký hiệu quy mô $n, m_G, k, I, U$; DMOZ16 chỉ là ví dụ lịch sử trong sách nếu cần nhắc, không khẳng định hệ đang hoạt động.
- **Hình thức hóa:** HT3 — phối hợp tuyến tính; HT8 (phần TSP).
- **Kết nối vào–ra cụ thể:** nhận giả mã từ s02-07; nhả chi phí cho s06-02 (so 4 mô hình) và ý "trộn chủ đề" cho s06-03.
- **Nguồn:** NG1 §5.3, p199/PDF25; đặc tả đã duyệt mục chi phí.
- **Thời lượng:** 3 phút (1' công thức phối hợp, 1' bảng chi phí, 1' so với s01-04).
- **Ghi chú soạn:** nói: "k vector tính trước, offline; lúc truy vấn chỉ cộng có trọng số"; sai lầm: quên điều kiện cùng $P$, cùng $\beta$ — nếu đổi $\beta$ giữa các chủ đề thì phối hợp không còn nghiệm đúng.

#### lec04-s02-10 — Kiểm tra phần 2: tính r₁ₐ và r₁ᵦ

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 2; đo MT1 — phân biệt phần theo cạnh và phần dịch chuyển.
- **Luận điểm trung tâm:** hai đỉnh nhận cùng khối lượng liên kết trong vòng này vẫn cho điểm khác nhau — vì phần dịch chuyển chỉ tới thành viên $S$.
- **Nội dung cụ thể (đề trên mặt slide):** Câu hỏi: cho G4, $S=\{B,D\}$, $\beta=\tfrac45$, $r_0=q_S=(0,\tfrac12,0,\tfrac12)$. Tính $r_{1,A}$ và $r_{1,B}$; giải thích nguyên nhân hai điểm này khác nhau.
- **Bố cục đã chọn:** Trái 40%: G4 với cùng vị trí và nhãn đỉnh; phải 60%: dữ kiện và hai yêu cầu tính, giải thích. Mặt slide không có gợi ý hay đáp án; nếu người học bế tắc, giảng viên gợi ý bằng lời việc tách phần liên kết và phần dịch chuyển.
- **Trọng tâm và thứ tự đọc:** dữ kiện trước, câu hỏi sau, gợi ý cuối cùng chỉ đọc khi bế tắc.
- **Lý do phù hợp sinh viên năm 3:** đúng thao tác vừa luyện ở s02-03..04; chỗ dễ nhầm: A không thuộc $S$ nên phần dịch chuyển của A bằng 0 — sinh viên hay cộng nhầm $\tfrac1{10}$ cho mọi đỉnh.
- **Giới hạn bố cục:** mặt slide chỉ đề; lời giải từng bước để ghi chú.
- **Ví dụ và số liệu:** VD1: $r_{1,A}=\tfrac15$, $r_{1,B}=\tfrac3{10}$ (NG1 VD5.10).
- **Hình thức hóa:** áp dụng HT1.
- **Kết nối vào–ra cụ thể:** nhận quy trình từ s02-04; nhả năng lực phân biệt hai khối lượng cho s04-03 (TrustRank) và s06-04.
- **Nguồn:** NG1 VD5.10, p197–199/PDF23–25.
- **Câu hỏi đủ dữ kiện:** có — G4, $S$, $\beta$, $r_0$ đều cho; không cần dữ kiện ngoài.
- **Đáp án (trong ghi chú):** $r_{1,A}=\beta\cdot\tfrac12\cdot\tfrac12+\beta\cdot\tfrac0{1}+0=\tfrac15$ (A nhận B→A và C→A; phần dịch chuyển 0 vì A ∉ S). $r_{1,B}=\beta\cdot\tfrac0{3}+\beta\cdot\tfrac12\cdot\tfrac12+\tfrac15\cdot\tfrac12=\tfrac15+\tfrac1{10}=\tfrac3{10}$ (B nhận A→B và D→B). Hai đỉnh nhận cùng khối lượng liên kết $\tfrac15$; khác nhau **do phần dịch chuyển trong vòng này** (B ∈ S, A ∉ S), không do cấu trúc cạnh vào khác — hai đỉnh nhận khối lượng liên kết giống nhau.
- **Tiêu chí đánh giá:** đúng hai giá trị ($\tfrac15$, $\tfrac3{10}$); giải thích được A ∉ S nên thiếu phần dịch chuyển trong khi khối lượng liên kết vào giống nhau; lỗi hiểu sai: cộng $\tfrac1{10}$ cho A, hoặc nhân $P^T$.
- **Thời gian hoạt động:** trong 2 phút: 1' suy nghĩ, 30" trả lời, 30" chữa.
- **Thời lượng:** 2 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** khi chữa, viết hai cột khối lượng cho A và B cạnh nhau; nếu lớp nhầm rộng, quay lại s02-04 30 giây; không mở rộng sang $r_2$.

#### lec04-s03-01 — Giới hạn của tín hiệu liên kết

- **Vai trò và mục tiêu:** mở phần 3; chuyển từ "thuật toán chạy đúng" sang "kẻ xấu biết thuật toán". Đặt nền MT2.
- **Luận điểm trung tâm:** PageRank đoán trước được — ai hiểu công thức đủ sâu có thể dựng cấu trúc liên kết để đẩy điểm trang mình.
- **Nội dung cụ thể:** ba ý: (1) PageRank là hàm cố định của cấu trúc liên kết; (2) chủ trang web kiểm soát được liên kết ra từ trang của mình; (3) câu hỏi phần này: một cấu trúc nhỏ giá rẻ có đẩy điểm lên bao nhiêu? — trả lời bằng phương trình, không bằng phỏng đoán.
- **Bố cục đã chọn:** giữa 60%: sơ đồ nhỏ — trang đích và cụm trang hỗ trợ nối vào, nhãn chữ "đích" / "hỗ trợ"; phải 40%: 3 dòng luận điểm đánh số; dòng dưới: "phần này phân tích mô hình, không dạy tạo spam".
- **Trọng tâm và thứ tự đọc:** sơ đồ trước (thấy quan hệ đích↔hỗ trợ), 3 dòng sau; dòng cảnh báo đọc cuối.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 cần ranh giới đạo đức rõ: hiểu tấn công để phòng vệ; ghi dòng cảnh báo ngay trên mặt slide tránh hiểu sai mục đích bài học; chỗ dễ nhầm: tưởng bài dạy cách làm spam.
- **Giới hạn bố cục:** mặt slide chỉ động cơ và cảnh báo; mô hình ba vùng để s03-02; không nêu tên công cụ spam thực tế.
- **Ví dụ và số liệu:** không áp dụng — slide đặt vấn đề.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** Nhận từ s02-10 ở cuối phần 2: đã phân biệt phần liên kết và phần dịch chuyển. Tín hiệu liên kết vẫn có thể bị thao túng; chuyển sang cấu trúc ba vùng ở s03-02.
- **Nguồn:** NG1 §5.4, p199–200/PDF25–26; NG3 slide 29–35 (động lực, giữ theo sách).
- **Thời lượng:** 2 phút (nêu vấn đề 1', đọc cảnh báo 1').
- **Ghi chú soạn:** nhấn: mục tiêu là phân tích và phòng vệ (phần 4 sẽ dùng); sai lầm cần chặn: "chỉ cần nhiều liên kết là điểm cao tùy ý" — sẽ chứng minh bằng phương trình rằng điểm có chặn.

#### lec04-s03-02 — Hình 5.16: ba vùng của cụm thao túng

- **Vai trò và mục tiêu:** thiết lập hình học mô hình; chuẩn bị ký hiệu. Nền MT2.
- **Luận điểm trung tâm:** cụm thao túng nằm trong vùng các trang sở hữu: đích và $q$ trang hỗ trợ cùng một vùng, trang hỗ trợ chỉ trỏ đích, đích trỏ mọi trang hỗ trợ.
- **Nội dung cụ thể:** Hình 5.16 (vẽ lại SVG `hinh-5-16-cum-thao-tung.svg` từ nguồn, giữ ba vùng và cạnh; sửa các mũi tên chồng nhau): ba vùng — **không thể tác động** (phần Web còn lại), **có thể tác động** (trang không sở hữu nhưng có thể đặt liên kết trên đó), **các trang sở hữu** (chứa cả trang đích và $q$ trang hỗ trợ); cấu trúc trong vùng sở hữu: mỗi trang hỗ trợ **chỉ trỏ đích**, đích trỏ mọi trang hỗ trợ, **không trỏ chéo giữa các trang hỗ trợ**; dòng chảy điểm: từ vùng có thể tác động vào trang đích trong vùng sở hữu, trong vùng sở hữu đi vòng đích↔hỗ trợ.
- **Bố cục đã chọn:** giữa 65%: SVG `hinh-5-16-cum-thao-tung.svg` ba vùng — vùng không thể tác động trái, vùng có thể tác động giữa, vùng sở hữu phải (chứa cả đích và $q$ trang hỗ trợ); mũi tên có nhãn dòng chảy; phải 35%: 3 dòng chú giải vùng, mỗi dòng một nhãn.
- **Trọng tâm và thứ tự đọc:** vùng sở hữu trước (nơi đặt đích và hỗ trợ), vùng có thể tác động sau, vùng không thể tác động cuối; theo dõi mũi tên hai chiều đích↔hỗ trợ trong vùng sở hữu.
- **Lý do phù hợp sinh viên năm 3:** sơ đồ vùng giúp sinh viên không lạc trong đồ thị đầy đủ; chỗ dễ nhầm: tưởng trang hỗ trợ trỏ chéo nhau — trong Hình 5.16 mỗi trang hỗ trợ chỉ trỏ đích, đích trỏ mọi trang hỗ trợ; cấu trúc này mới làm phương trình $z$, $y$ đứng vững.
- **Giới hạn bố cục:** mặt slide chỉ sơ đồ và chú giải; ký hiệu $N,q,x,y$ để s03-03; không vẽ số trang cụ thể.
- **Ví dụ và số liệu:** không áp dụng số — hình cấu trúc từ NG1 Hình 5.16 p200/PDF26.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận động cơ từ s03-01; nhả ba vùng cho s03-03 gán ký hiệu.
- **Nguồn:** NG1 Hình 5.16, p200/PDF26 (đọc lại nguồn; minh họa lấy SVG hiện có `hinh-5-16-cum-thao-tung.svg` đúng nguồn); NG3 slide 29–35.
- **Thời lượng:** 3 phút (chỉ ba vùng 1', theo dòng chảy 1', kiểm mũi tên hai chiều đích↔hỗ trợ 1').
- **Ghi chú soạn:** nói: "vùng sở hữu là các trang do người thao túng kiểm soát, trong đó đích và $q$ trang hỗ trợ cùng nằm"; sai lầm: vẽ trỏ chéo giữa các trang hỗ trợ — trong mô hình mỗi trang hỗ trợ chỉ trỏ đích; sai lầm khác: vẽ mũi tên từ vùng sở hữu ra ngoài — hỗ trợ không tương tác ra ngoài vùng.

#### lec04-s03-03 — Ý nghĩa N, q, x, y

- **Vai trò và mục tiêu:** chốt ký hiệu của bản 5.11; tránh trộn với $q_S$. Nền MT2.
- **Luận điểm trung tâm:** bốn đại lượng đủ để viết phương trình điểm đích.
- **Nội dung cụ thể:** $N$ = tổng số trang ($N\ge q+1$); $q$ = **số** trang hỗ trợ, $q\ge1$ (khác $q_S$ là vector); $x$ = đóng góp vào đích từ **ngoài** cụm, đã gồm hệ số $\beta$; $y$ = điểm đích cần đánh giá. Bảng 4 hàng ký hiệu — ý nghĩa — điều kiện.
- **Bố cục đã chọn:** trái 55%: bảng 4 hàng ($N, q, x, y$) × 3 cột (ký hiệu, ý nghĩa, điều kiện); phải 45%: thu nhỏ sơ đồ ba vùng từ s03-02 giữ nguyên vị trí vùng, gắn nhãn $N$ phủ toàn bộ, $q$ trên vùng hỗ trợ, $x$ trên mũi tên vào, $y$ trên đích.
- **Trọng tâm và thứ tự đọc:** sơ đồ phải trước (gắn nhãn lên hình), bảng trái sau để chốt định nghĩa.
- **Lý do phù hợp sinh viên năm 3:** gắn ký hiệu trực tiếp lên sơ đồ giúp nhớ vai trò từng đại lượng; chỗ dễ nhầm số một: $q$ (số đếm) với $q_S$ (vector) — nhắc lại cảnh báo từ s01-05.
- **Giới hạn bố cục:** mặt slide chỉ 4 ký hiệu; $z$ để s03-04; không chọn số $N, q, x$ cụ thể — giữ hệ số nguyên bản 5.11.
- **Ví dụ và số liệu:** không áp dụng số cụ thể — ký hiệu theo NG1 bản 5.11, không tự bịa.
- **Hình thức hóa:** không áp dụng; quy ước ký hiệu.
- **Kết nối vào–ra cụ thể:** nhận ba vùng từ s03-02; nhả $N,q,x,y$ cho s03-04 (thêm $z$) và s03-06.
- **Nguồn:** NG1 VD5.11, §5.4, p200–204/PDF26–30.
- **Thời lượng:** 2 phút (1' bảng, 1' gắn nhãn lên sơ đồ).
- **Ghi chú soạn:** hỏi lớp: "$q$ ở đây là gì?" — phải trả lời "số trang hỗ trợ", phân biệt $q_S$; sai lầm: tưởng $x$ gồm cả dòng từ hỗ trợ — $x$ chỉ là đóng góp ngoài.

#### lec04-s03-04 — Điểm mỗi trang hỗ trợ: z

- **Vai trò và mục tiêu:** viết phương trình cho $z$; bước trung gian của hệ. Nền MT2.
- **Luận điểm trung tâm:** mỗi trang hỗ trợ nhận đều phần $\beta$ của đích, cộng phần dịch chuyển đều.
- **Nội dung cụ thể:** mỗi trang hỗ trợ nhận $\beta y/q$ (đích chia đều cho $q$ trang hỗ trợ qua các cạnh về) cộng $(1-\beta)/N$ (dịch chuyển đều trên $N$ trang): $$z=\beta\frac{y}{q}+\frac{1-\beta}{N}.$$ Giải thích từng số hạng: $\beta y/q$ — phần theo cạnh từ đích; $(1-\beta)/N$ — phần nhảy ngẫu nhiên.
- **Bố cục đã chọn:** trên 40%: công thức $z$ lớn giữa màn; dưới 60%: sơ đồ thu nhỏ đích↔một trang hỗ trợ với hai mũi tên nhãn $\beta y/q$ và $(1-\beta)/N$; chú thích "$q$ trang hỗ trợ, mỗi trang nhận như nhau".
- **Trọng tâm và thứ tự đọc:** công thức trước, sơ đồ sau để giải thích hai số hạng.
- **Lý do phù hợp sinh viên năm 3:** phương trình một ẩn vừa sức; tách hai số hạng giúp sinh viên thấy $z$ phụ thuộc $y$ — nền của việc giải hệ ở s03-06; chỗ dễ nhầm: quên chia $q$ hoặc quên nhân $\beta$.
- **Giới hạn bố cục:** mặt slide chỉ phương trình $z$; phương trình $y$ để s03-05; không giải ở đây.
- **Ví dụ và số liệu:** không áp dụng số — ký hiệu theo bản 5.11.
- **Hình thức hóa:** một phần của HT4; phương trình đầy đủ ở s03-05..06.
- **Kết nối vào–ra cụ thể:** nhận ký hiệu từ s03-03; nhả $z$ cho s03-05 thay vào phương trình đích.
- **Nguồn:** NG1 VD5.11, p200–204/PDF26–30.
- **Thời lượng:** 3 phút (1' hai số hạng, 1' nhấn chia đều $q$, 1' hỏi lớp kiểm tra thiếu /q).
- **Ghi chú soạn:** sai lầm: viết $z=\beta y+(1-\beta)/N$ (quên /q) — hỏi lớp "đích trỏ tới mấy trang hỗ trợ?"; nhắc $(1-\beta)/N$ chia đều mọi trang, không chỉ vùng hỗ trợ.

#### lec04-s03-05 — Ba thành phần trở về đích

- **Vai trò và mục tiêu:** viết phương trình đích; hoàn thành hệ hai phương trình. Nền MT2.
- **Luận điểm trung tâm:** điểm đích = dòng từ ngoài + dòng vòng từ hỗ trợ + phần dịch chuyển trực tiếp.
- **Nội dung cụ thể:** $$y=x+\beta q z+\frac{1-\beta}{N}.$$ Ba thành phần: $x$ — đóng góp ngoài (đã gồm $\beta$); $\beta q z$ — mỗi trong $q$ trang hỗ trợ trỏ về đích với khối lượng $z$, nhân $\beta$; $(1-\beta)/N$ — dịch chuyển trực tiếp về đích. Hệ hai ẩn $(y,z)$ hai phương trình.
- **Bố cục đã chọn:** giữa 50%: công thức $y$ lớn, ba số hạng được đóng khung riêng với nhãn ①②③; trái 25%: sơ đồ ba mũi tên vào đích tương ứng ba nhãn; phải 25%: dòng "hệ 2 phương trình, 2 ẩn (y, z)".
- **Trọng tâm và thứ tự đọc:** sơ đồ trái trước (thấy ba dòng), công thức giữa sau, đối chiếu nhãn ①②③ với mũi tên.
- **Lý do phù hợp sinh viên năm 3:** tách ba số hạng thành ba mũi tên giúp sinh viên không cộng trộn; chỗ dễ nhầm: tưởng $x$ chưa gồm $\beta$ rồi nhân thêm lần nữa — nhãn "đã gồm β" chặn lỗi này.
- **Giới hạn bố cục:** mặt slide chỉ phương trình và sơ đồ; phép thế và giải để s03-06; không hiện nghiệm sớm.
- **Ví dụ và số liệu:** không áp dụng số — cấu trúc phương trình theo bản 5.11.
- **Hình thức hóa:** hệ phương trình cụm thao túng (một phần HT4).
- **Kết nối vào–ra cụ thể:** nhận $z$ từ s03-04; nhả hệ hai phương trình cho s03-06 giải.
- **Nguồn:** NG1 VD5.11, p200–204/PDF26–30.
- **Thời lượng:** 4 phút (1' sơ đồ, 2' đối chiếu ba số hạng, 1' chốt hệ 2 phương trình 2 ẩn).
- **Ghi chú soạn:** hỏi lớp: "vì sao $\beta q z$ chứ không phải $qz$?" — vì dòng từ hỗ trợ về đích cũng bị co $\beta$; sai lầm: gộp $(1-\beta)/N$ vào $x$ — $x$ là dòng theo cạnh từ ngoài, dịch chuyển là dòng riêng.

#### lec04-s03-06 — Giải chính xác và xấp xỉ của sách

- **Vai trò và mục tiêu:** giải hệ từng bước; tách rõ nghiệm chính xác và xấp xỉ. HT4.
- **Luận điểm trung tâm:** thay $z$ vào phương trình đích, giải ra nghiệm chính xác; sách bỏ một hạng để được xấp xỉ.
- **Nội dung cụ thể:** thay $z=\beta y/q+(1-\beta)/N$ vào $y=x+\beta qz+(1-\beta)/N$: $$y=x+\beta^2 y+\frac{\beta q(1-\beta)}{N}+\frac{1-\beta}{N}$$ $$\Rightarrow\quad y_{\text{chính xác}}=\frac{x}{1-\beta^2}+\frac{\beta q+1}{N(1+\beta)}.$$ Xấp xỉ sách bỏ phần dịch chuyển trực tiếp $(1-\beta)/N$: $$y_{\text{xấp xỉ}}=\frac{x}{1-\beta^2}+\frac{\beta q}{N(1+\beta)}.$$ Sai khác: $\dfrac{1}{N(1+\beta)}$ — tác động sau khi giải của hạng bị bỏ, không bằng chính hạng đó; cả hai nghiệm đều chia cho $1-\beta^2$.
- **Bố cục đã chọn:** trái 55%: 4 dòng giải từng bước (thay → gom → chia $1-\beta^2$ → nghiệm chính xác); phải 45%: hai khối: "xấp xỉ: bỏ $(1-\beta)/N$" và "sai khác $=1/[N(1+\beta)]$"; dòng dưới: hai công thức nghiệm xếp chồng có nhãn "chính xác" / "xấp xỉ".
- **Trọng tâm và thứ tự đọc:** dòng giải trái theo thứ tự; so hai nghiệm phải để thấy khác nhau đúng một hạng trong tử.
- **Lý do phù hợp sinh viên năm 3:** đại số một ẩn vừa sức; chỗ dễ nhầm số một: tưởng sai khác là chính hạng bị bỏ $(1-\beta)/N$ — thực tế sau khi chia $1-\beta^2=(1-\beta)(1+\beta)$ nó thành $1/[N(1+\beta)]$; nhãn "chính xác/xấp xỉ" chống gộp hai công thức.
- **Giới hạn bố cục:** mặt slide 4 dòng giải và 2 nghiệm; kiểm tra đại số từng bước để ghi chú; không thay số cụ thể.
- **Ví dụ và số liệu:** không áp dụng số — nghiệm theo ký hiệu bản 5.11; hệ số số cụ thể ở s03-07.
- **Hình thức hóa:** HT4 — nghiệm chính xác và xấp xỉ, sai khác $1/[N(1+\beta)]$.
- **Kết nối vào–ra cụ thể:** nhận hệ từ s03-05; nhả hai nghiệm cho s03-07 (hệ số) và s03-08 (gán hạng).
- **Nguồn:** NG1 VD5.11, §5.4, p200–204/PDF26–30.
- **Thời lượng:** 3 phút (1' giải từng bước, 1' xấp xỉ, 1' sai khác).
- **Ghi chú soạn:** bước nói: gom hai hạng chứa $y$ bên trái → $y(1-\beta^2)$; sai lầm: nói "xấp xỉ sai khác $(1-\beta)/N$" — sửa: sau khi chia, sai khác là $1/[N(1+\beta)]$; không nói "tăng trang hỗ trợ khiến PageRank lớn tùy ý".

#### lec04-s03-07 — $\beta=0.85$: hệ số, giới hạn diễn giải và chi phí

- **Vai trò và mục tiêu:** gắn số vào nghiệm; nêu cách nói đúng và chi phí. Hoàn thành MT2 về diễn giải.
- **Luận điểm trung tâm:** tại $\beta=.85$, dòng ngoài được khuếch đại khoảng 3.6 lần; nhóm $q$ trang hỗ trợ đóng góp theo số hạng $(17/37)(q/N)$.
- **Nội dung cụ thể:** $\beta=.85=17/20$: hệ số ngoài $1/(1-\beta^2)=400/111\approx3.6036$ — nói "gấp khoảng 3.6 lần", không nói "tăng thêm 360%"; số hạng hỗ trợ có hệ số $\beta/(1+\beta)=17/37\approx0.4595$ nhân $q/N$: $y_{\text{xấp xỉ}}$ chứa $(17/37)\cdot(q/N)$, không viết thành đẳng thức "q/N = 17/37". Chi phí: đánh giá biểu thức khi đã biết $x$ là $O(1)$; tìm PageRank nền vẫn cần lặp trên đồ thị; số trang hỗ trợ không là chi phí xử lý toàn Web.
- **Bố cục đã chọn:** trên 45%: hai hộp hệ số cạnh nhau: "ngoài: $400/111\approx3.6036$" và "hỗ trợ: hệ số $17/37\approx0.4595$, số hạng $(17/37)(q/N)$"; dưới 55%: 3 dòng diễn giải: cách nói đúng / cách nói sai (gạch đầu dòng có nhãn "đúng"/"tránh") / chi phí 2 dòng.
- **Trọng tâm và thứ tự đọc:** hai hộp hệ số trước, dòng diễn giải sau; dừng ở dòng "tránh" để đọc kỹ.
- **Lý do phù hợp sinh viên năm 3:** Đặt hệ số cạnh số hạng đầy đủ giúp phân biệt “gấp 3,6 lần” với “tăng thêm 360%” và phân biệt hệ số $17/37$ với $q/N$. Phần chi phí tách việc đánh giá biểu thức khi biết $x$ khỏi việc tính PageRank trên toàn đồ thị.
- **Giới hạn bố cục:** mặt slide chỉ hệ số và diễn giải; phạm vi mô hình (chỉ phân tích/phòng vệ) đã ghi ở s03-01, nhắc một dòng.
- **Ví dụ và số liệu:** VD2: $\beta=17/20$, $400/111\approx3.6036$, $17/37\approx.4595$ (NG1 VD5.11; tính từ phép lặp đã kiểm).
- **Hình thức hóa:** HT4 áp dụng số; HT8 (phần cụm thao túng: $O(1)$ khi biết $x$).
- **Kết nối vào–ra cụ thể:** Nhận nghiệm từ s03-06; chuyển việc diễn giải các số hạng sang kiểm tra s03-08. Kết quả phân tích tạo nhu cầu phòng vệ bằng nguồn tin cậy ở s04-01.
- **Nguồn:** NG1 VD5.11, p200–204/PDF26–30.
- **Thời lượng:** 3 phút (1' hệ số, 1' đúng/tránh, 1' chi phí).
- **Ghi chú soạn:** sai lầm cần chặn: "tăng thêm 360%", "PageRank lớn tùy ý" và viết đẳng thức sai "$q/N=17/37$" (17/37 là hệ số nhân $q/N$, từ $\beta/(1+\beta)$); nhắc $q$ là số trang hỗ trợ, không phải vector.

#### lec04-s03-08 — Kiểm tra phần 3: gán hạng bốn số hạng

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 3; đo MT2 — gán đúng nguồn và hạng bị bỏ.
- **Luận điểm trung tâm:** bốn số hạng của phương trình mở rộng mỗi số hạng có một nguồn dòng chảy riêng.
- **Nội dung cụ thể (đề trên mặt slide):** Câu hỏi: trong phương trình $y=x+\beta^2y+\dfrac{\beta q(1-\beta)}{N}+\dfrac{1-\beta}{N}$: (i) mỗi số hạng đến từ nguồn nào? (ii) sách bỏ hạng nào để được xấp xỉ?
- **Bố cục đã chọn:** giữa 60%: phương trình 4 số hạng, mỗi số hạng một khung trống nhãn "nguồn?"; dưới 30%: hai câu hỏi (i), (ii). Không lộ đáp án; đáp án để trong ghi chú giảng viên, không dán nhãn quy trình lên mặt.
- **Trọng tâm và thứ tự đọc:** phương trình trước, hai câu hỏi sau.
- **Lý do phù hợp sinh viên năm 3:** gán nguồn từng số hạng là thao tác vừa luyện ở s03-05..06; chỗ dễ nhầm: chọn nhầm $\beta q(1-\beta)/N$ làm hạng bị bỏ — hạng bị bỏ là phần dịch chuyển trực tiếp $(1-\beta)/N$.
- **Giới hạn bố cục:** mặt slide chỉ đề; bảng nguồn đầy đủ để ghi chú.
- **Ví dụ và số liệu:** VD2: bốn số hạng như trên; không cần số cụ thể $N,q,x$.
- **Hình thức hóa:** HT4.
- **Kết nối vào–ra cụ thể:** nhận nghiệm từ s03-06; nhả năng lực gán hạng cho s06-04 (câu hỏi tích hợp "hạng nào sách bỏ").
- **Nguồn:** NG1 VD5.11, p200–204/PDF26–30.
- **Câu hỏi đủ dữ kiện:** có — phương trình cho đầy đủ trên mặt slide.
- **Đáp án (trong ghi chú):** $x$ — đóng góp ngoài cụm (đã gồm $\beta$); $\beta^2y$ — vòng đích→hỗ trợ→đích; $\beta q(1-\beta)/N$ — dịch chuyển đến các trang hỗ trợ rồi vòng về đích; $(1-\beta)/N$ — dịch chuyển trực tiếp về đích. Xấp xỉ bỏ đúng $(1-\beta)/N$; sai khác sau giải là $1/[N(1+\beta)]$.
- **Tiêu chí đánh giá:** gán đúng 4 nguồn; chỉ ra đúng hạng bị bỏ; lỗi hiểu sai: bỏ $\beta q(1-\beta)/N$, hoặc nói sai khác bằng chính hạng bị bỏ.
- **Thời gian hoạt động:** trong 2 phút: 1' suy nghĩ, 30" trả lời, 30" chữa.
- **Thời lượng:** 2 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** chữa bằng cách chỉ từng số hạng trên công thức s03-06; nếu lớp nhầm hạng bị bỏ, viết lại hai nghiệm xếp chồng 30 giây.

#### lec04-s04-01 — Giả thiết cô lập gần đúng

- **Vai trò và mục tiêu:** mở phần 4; nêu rõ đây là giả thiết, không bảo đảm. Nền MT3.
- **Luận điểm trung tâm:** "trang tốt ít trỏ tới trang rác" — nếu đúng, điểm tin cậy lan từ nguồn tốt sẽ ít chạm trang rác.
- **Nội dung cụ thể:** phát biểu giả thiết: các trang tốt (được con người đánh giá) ít liên kết tới trang rác; hệ quả mong muốn: chạy PageRank với dịch chuyển về tập tin cậy cho điểm thấp ở vùng rác. Ghi rõ: **giả thiết, không bảo đảm** — có trang tốt bị chiếm quyền, có trang rác trỏ lẫn nhau.
- **Bố cục đã chọn:** giữa 50%: khối phát biểu giả thiết trong khung nhãn "GIẢ THIẾT"; dưới 50%: hai cột "kỳ vọng" (điểm trust thấp ở rác) và "rủi ro" (giả thiết sai → sai lệch), mỗi cột 2 dòng.
- **Trọng tâm và thứ tự đọc:** khung giả thiết trước, hai cột sau; nhãn "GIẢ THIẾT" đọc đầu tiên.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 cần phân biệt phát biểu định lý với giả thiết làm việc; đây là chỗ dễ nhầm số một của phần này — nhiều tài liệu trình bày như sự thật; khung nhãn giúp tách mức phát biểu.
- **Giới hạn bố cục:** mặt slide chỉ giả thiết và hệ quả; cách chọn $T$ để s04-02; không nêu hậu tố .edu/.gov như bảo đảm sạch.
- **Ví dụ và số liệu:** không áp dụng — slide phát biểu giả thiết.
- **Hình thức hóa:** không áp dụng định lý; ghi nhận mức "giả thiết" trong danh mục hình thức hóa.
- **Kết nối vào–ra cụ thể:** nhận nhu cầu phòng vệ từ s03-01; nhả giả thiết cho s04-02 (chọn $T$) và s04-04 (hệ quả khi giả thiết sai).
- **Nguồn:** NG1 §5.4, p201–202/PDF27–28.
- **Thời lượng:** 2 phút (đọc giả thiết 1', hai cột 1').
- **Ghi chú soạn:** nói rõ: "đây là giả thiết làm việc, phần cuối bài sẽ khép lại giới hạn này"; sai lầm cần chặn: "trang .edu/.gov chắc chắn sạch" — không bảo đảm, chỉ là ứng viên.

#### lec04-s04-02 — Chọn tập tin cậy T: cân bằng thẩm định và độ phủ

- **Vai trò và mục tiêu:** chỉ ra $T$ là đầu vào được thẩm định; nêu hai cách nguồn. Nền MT3.
- **Luận điểm trung tâm:** chất lượng của TrustRank phụ thuộc chất lượng $T$ — cân bằng giữa chất lượng tập $T$ và độ phủ.
- **Nội dung cụ thể:** hai cách chọn nguồn: (a) chọn ứng viên từ các trang PageRank cao rồi thẩm định; (b) miền có giám quản (do tổ chức quản lý). Cân bằng giữa chất lượng tập $T$ và độ phủ; $T\ne\emptyset$.
- **Bố cục đã chọn:** hai cột bằng nhau 48% mỗi cột: trái "chọn ứng viên PageRank cao rồi thẩm định", phải "miền có giám quản"; mỗi cột 2 dòng: cách làm / phạm vi phủ; dải dưới: dòng "cân bằng: chất lượng tập $T$ ↔ độ phủ".
- **Trọng tâm và thứ tự đọc:** hai cột song song, trái trước; dải đánh đổi cuối cùng chốt.
- **Lý do phù hợp sinh viên năm 3:** sinh viên đã biết PageRank cao ≠ tin cậy (từ phần 3); hai cách nguồn cho họ thấy quyết định kỹ thuật gắn với chất lượng dữ liệu đầu vào; chỗ dễ nhầm: tưởng có bộ $T$ "chuẩn" duy nhất.
- **Giới hạn bố cục:** mặt slide chỉ hai cách và cân bằng chất lượng/độ phủ; quy tắc tính trust để s04-03; không liệt kê danh sách tên miền cụ thể.
- **Ví dụ và số liệu:** không áp dụng số — phân loại phương pháp.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận giả thiết từ s04-01; nhả khái niệm $T\ne\emptyset$ cho s04-03 (định nghĩa $q_T$).
- **Nguồn:** NG1 §5.4, p202/PDF28; NG3 slide 37–45.
- **Thời lượng:** 3 phút (1' cột trái, 1' cột phải, 1' đánh đổi).
- **Ghi chú soạn:** hỏi lớp: "chọn cách nào để tập $T$ vừa chất lượng vừa đủ phủ?" — không có đáp án duy nhất, mục đích là thấy cân bằng; sai lầm: coi $T$ lớn luôn tốt hơn — mở rộng $T$ có thể tăng độ phủ, nhưng cần thẩm định chất lượng các trang mới.

#### lec04-s04-03 — Quy tắc tính trust: dùng lại máy TSP

- **Vai trò và mục tiêu:** định nghĩa TrustRank bằng chính phương trình TSP; dùng lại bất biến/co không chứng minh trùng. HT5 (phần quy tắc).
- **Luận điểm trung tâm:** TrustRank là TSP với vector dịch chuyển phân bố đều trên tập tin cậy.
- **Nội dung cụ thể:** $q_T=e_T/|T|$ (phân bố đều trên $T$, $|T|$ phần tử), $t_0=q_T$, $$t'=\beta Pt+(1-\beta)q_T.$$ Giống TSP mọi mặt: cùng $P$, cùng $\beta$, cùng vòng lặp, cùng bù nút cụt; bất biến xác suất và co $L_1$ dùng lại từ PageRank theo chủ đề — không chứng minh lại; chi phí như TSP: $\Theta(n+m_G)$/vòng.
- **Bố cục đã chọn:** trên 45%: công thức $t'$ lớn, bên cạnh công thức TSP $r'=\beta Pr+(1-\beta)q_S$ xếp chồng để đối chiếu, hai nhãn "trust" / "TSP"; dưới 55%: bảng 3 hàng "giống" (P, β, vòng lặp) và 1 hàng "khác" (chỉ $q_S\to q_T$); dòng cuối: "bất biến và co: dùng lại HT2".
- **Trọng tâm và thứ tự đọc:** hai công thức xếp chồng trước (thấy chỉ khác vector dịch chuyển), bảng sau.
- **Lý do phù hợp sinh viên năm 3:** sinh viên vừa chứng minh HT2; thấy máy dùng lại giúp tiết kiệm tải nhận thức và củng cố kỹ năng; chỗ dễ nhầm: tưởng TrustRank cần thuật toán mới — chỉ đổi đầu vào.
- **Giới hạn bố cục:** mặt slide chỉ quy tắc và bảng đối chiếu; lỗi hạt giống để s04-04; không chứng minh lại bất biến.
- **Ví dụ và số liệu:** không chạy số ở đây — số ở s04-06..07 (VD3).
- **Hình thức hóa:** HT5 (quy tắc); HT2 dùng lại.
- **Kết nối vào–ra cụ thể:** nhận HT1, HT2 từ s02-06..08 và $T$ từ s04-02; nhả quy tắc cho s04-06 (bảng 5.17) và bài tập R2 (s07-02).
- **Nguồn:** NG1 §5.4, p202–203/PDF28–29.
- **Thời lượng:** 3 phút (1' đối chiếu công thức, 1' bảng, 1' nhấn dùng lại).
- **Ghi chú soạn:** hỏi lớp: "điều kiện nào của HT1 vẫn giữ?" — $q_T\ge0$, tổng 1, $T\ne\emptyset$, $\beta\in(0,1)$; sai lầm: tưởng cần chứng minh hội tụ mới — cùng phép co, cùng kết luận.

#### lec04-s04-04 — Lỗi hạt giống và thiếu độ phủ

- **Vai trò và mục tiêu:** chỉ ra hai điểm yếu của TrustRank; gộp một slide vì cùng trực giác. Hoàn thành góc nhìn phê phán MT3.
- **Luận điểm trung tâm:** Chất lượng hạt giống và độ phủ của tập tin cậy ảnh hưởng tới điểm thu được qua liên kết; thuật toán không tự khắc phục hai giới hạn đầu vào này.
- **Nội dung cụ thể:** (a) Lỗi hạt giống: một trang xấu lọt vào $T$ sẽ truyền trust cho vùng nó trỏ tới — sai số nguồn lan theo liên kết. (b) Thiếu độ phủ: điểm trust của một trang phụ thuộc toàn bộ đường đi và trọng số từ $T$ tới nó, không đơn điệu theo khoảng cách — trang ở xa $T$ vẫn có thể nhận điểm cao nếu đường đi qua các nguồn tốt, và trang gần $T$ không bảo đảm điểm cao. Hai hiện tượng cùng một gốc: trust lan theo cấu trúc liên kết từ $T$.
- **Bố cục đã chọn:** hai thẻ ngang bằng nhau: thẻ trên "lỗi hạt giống" — mô tả bằng chữ tác động: sai số nguồn lan theo liên kết tới vùng đích; thẻ dưới "thiếu độ phủ" — mô tả bằng chữ giới hạn: điểm phụ thuộc toàn bộ đường đi và trọng số, không đơn điệu theo khoảng cách; dòng cuối: "hai hiện tượng: cùng gốc — trust lan theo liên kết".
- **Trọng tâm và thứ tự đọc:** thẻ trên trước (lỗi rõ ràng hơn), thẻ dưới sau; dòng cuối gộp hai hiện tượng.
- **Lý do phù hợp sinh viên năm 3:** sinh viên hay tin đầu ra thuật toán là khách quan; hai thẻ cho thấy đầu ra phụ thuộc đầu vào được thẩm định và phụ thuộc toàn bộ cấu trúc liên kết — bài học về giới hạn mô hình; gộp hai hiện tượng tránh lặp trực giác hai lần.
- **Giới hạn bố cục:** mặt slide hai thẻ ngắn, mô tả bằng chữ; ví dụ số về mass để s04-05..07; không đưa giải pháp nâng cao (truyền trust riêng đã bỏ theo spec).
- **Ví dụ và số liệu:** không áp dụng số — phân tích định tính.
- **Hình thức hóa:** không áp dụng định lý; ghi nhận hai giới hạn.
- **Kết nối vào–ra cụ thể:** nhận quy tắc từ s04-03; nhả động cơ "cần thước đo bổ sung" cho s04-05 (spam mass).
- **Nguồn:** NG1 §5.4, p202–203/PDF28–29.
- **Thời lượng:** 2 phút (1' mỗi khối).
- **Ghi chú soạn:** Dùng lại tình huống một trang xấu lọt vào tập tin cậy: phần dịch chuyển tới trang đó tiếp tục lan theo các liên kết. Nhắc rằng khoảng cách ngắn tới tập tin cậy không tự bảo đảm điểm cao; cần xét toàn bộ đường đi và trọng số.

#### lec04-s04-05 — Spam mass: định nghĩa và giới hạn

- **Vai trò và mục tiêu:** định nghĩa thước đo thứ hai; nêu rõ dấu, giới hạn, không phải xác suất. HT5.
- **Luận điểm trung tâm:** mass đo phần điểm PageRank "vượt" so với điểm trust — tỷ số so sánh, không phải xác suất.
- **Nội dung cụ thể:** $$s_p=\frac{r_p-t_p}{r_p},\qquad r_p>0.$$ Phân tích: có thể âm (khi $t_p>r_p$); $\le1$ khi $t\ge0$ (vì $r_p-t_p\le r_p$); **không phải xác suất**, không có ngưỡng chắc chắn "trên ngưỡng là rác"; điều kiện dùng: $r_p>0$ để chia được.
- **Bố cục đã chọn:** trên 40%: công thức mass lớn; dưới 60%: bảng 3 hàng "khi nào dương / khi nào âm / chặn trên" × cột "điều kiện" và "ý nghĩa"; dòng cuối nhỏ: "không phải xác suất, không ngưỡng chắc chắn".
- **Trọng tâm và thứ tự đọc:** công thức trước, bảng sau; dòng cuối đọc kỹ hai lần.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 quen tỷ số nhưng hay gán nhãn xác suất cho mọi tỷ số trong [0,1]; bảng điều kiện giúp họ diễn giải dấu đúng; chỗ dễ nhầm: mass âm = "trang tốt chắc chắn" — chỉ là $t_p>r_p$ trong thiết lập đang dùng.
- **Giới hạn bố cục:** mặt slide chỉ định nghĩa và bảng; bảng 5.17 với cảnh báo hai thiết lập để s04-06.
- **Ví dụ và số liệu:** không chạy số ở đây — số ở s04-06..07.
- **Hình thức hóa:** HT5 — mass có thể âm, $\le1$ khi $t\ge0$, không xác suất.
- **Kết nối vào–ra cụ thể:** nhận nhu cầu từ s04-04; nhả định nghĩa cho s04-06 (bảng) và s04-08 (kiểm tra).
- **Nguồn:** NG1 §5.4, p203/PDF29.
- **Thời lượng:** 3 phút (1' công thức, 2' bảng điều kiện).
- **Ghi chú soạn:** hỏi lớp: "mass có thể vượt 1 không?" — không, khi $t\ge0$ thì $r_p-t_p\le r_p$; sai lầm: gọi mass là "xác suất trang là rác" — sửa ngay; nhắc cần $r_p>0$.

#### lec04-s04-06 — Bảng 5.17 với cảnh báo hai thiết lập

- **Vai trò và mục tiêu:** trình bày dữ kiện VD5.12; cảnh báo rõ hai thiết lập khác nhau. Nền MT3.
- **Luận điểm trung tâm:** bảng 5.17 minh họa phép tỷ số, không cô lập riêng tác động của $T$.
- **Nội dung cụ thể:** VD5.12 trên G4: PageRank nền $r=(\tfrac13,\tfrac29,\tfrac29,\tfrac29)$ lấy từ PageRank **không hệ số suy giảm** (bài 5.2); TrustRank $t=(\tfrac{54}{210},\tfrac{59}{210},\tfrac{38}{210},\tfrac{59}{210})$ với $\beta=.8$, $T=\{B,D\}$ — **có** hệ số suy giảm. Hai thiết lập khác nhau: bảng chỉ minh họa phép tỷ số. Mass: $s=(\tfrac8{35},-\tfrac{37}{140},\tfrac{13}{70},-\tfrac{37}{140})$.
- **Bố cục đã chọn:** giữa 55%: bảng 4 hàng (A, B, C, D) × 3 cột ($r_p$, $t_p$, $s_p$), thứ tự cột cố định; trên bảng 1 dòng cảnh báo trong khung: "hai thiết lập khác nhau — chỉ minh họa phép tỷ số"; phải 40%: 3 dòng ghi chú nguồn từng cột.
- **Trọng tâm và thứ tự đọc:** dòng cảnh báo trước (bắt buộc), bảng sau theo hàng A→D, cột $r_p\to t_p\to s_p$.
- **Lý do phù hợp sinh viên năm 3:** sinh viên dễ so sánh hai cột như cùng thiết lập rồi rút kết luận sai về $T$; cảnh báo đặt trên bảng, trước cả bảng, để đọc đầu tiên; giữ phân số nguồn tránh sai số.
- **Giới hạn bố cục:** mặt slide chỉ bảng và cảnh báo; tính chi tiết A, B để s04-07; không đổi điểm nền để "đẹp ví dụ".
- **Ví dụ và số liệu:** VD3 (NG1 VD5.12, p203–204/PDF29–30): $r$, $t$, $s$ như trên; giữ nguyên số nguồn.
- **Hình thức hóa:** HT5 áp dụng; cảnh báo hai thiết lập là phần bắt buộc của phát biểu.
- **Kết nối vào–ra cụ thể:** nhận $r^*$ từ s02-05 (chú ý: nguồn dùng $r$ không hệ số suy giảm — khác thiết lập, ghi rõ); nhả bảng cho s04-07.
- **Nguồn:** NG1 VD5.12, §5.4, p203–204/PDF29–30.
- **Thời lượng:** 3 phút (1' cảnh báo, 2' đọc bảng).
- **Ghi chú soạn:** nói rõ: "$r$ ở đây không phải $r^*$ của VD1 — nguồn dùng PageRank không hệ số suy giảm"; sai lầm: so $r$ và $t$ như cùng thiết lập rồi kết luận về $T$; ứng dụng so kiểm soát cần cùng $\beta$, cùng xử lý nút cụt.

#### lec04-s04-07 — Tính mass tại A và B: dấu và giới hạn

- **Vai trò và mục tiêu:** chạy tay phép tỷ số; thấy mass âm xuất hiện thế nào. Hoàn thành MT3 về phép tính.
- **Luận điểm trung tâm:** cùng một công thức cho mass dương ở A và âm ở B — dấu phản ánh quan hệ $t_p$ với $r_p$.
- **Nội dung cụ thể:** A: $s_A=(\tfrac13-\tfrac{54}{210})/\tfrac13=\tfrac8{35}$ (dương, $r_A>t_A$); B: $s_B=(\tfrac29-\tfrac{59}{210})/\tfrac29=-\tfrac{37}{140}$ (âm, $t_B>r_B$). Giới hạn: mass $\le1$ khi $t\ge0$; giá trị âm không phải "xác suất rác âm" — chỉ nói $t_B>r_B$ trong thiết lập đang dùng.
- **Bố cục đã chọn:** hai khối ngang: khối trên "đỉnh A" với 3 dòng: $r_A$, $t_A$, phép chia và kết quả $\tfrac8{35}$; khối dưới "đỉnh B" tương tự, kết quả $-\tfrac{37}{140}$ có khung nhãn "âm: $t_B>r_B$"; dòng cuối: "dấu = quan hệ giữa $t_p$ và $r_p$, không phải nhãn rác/sạch".
- **Trọng tâm và thứ tự đọc:** khối A trước (dương, quen), khối B sau (âm, mới); dòng kết luận cuối.
- **Lý do phù hợp sinh viên năm 3:** phép chia phân số vừa sức; chỗ dễ nhầm: thấy âm liền kết luận "trang tốt" hoặc "số liệu sai" — cả hai đều sai; khung nhãn "âm: $t_B>r_B$" giữ diễn giải trong phạm vi dữ kiện.
- **Giới hạn bố cục:** mặt slide chỉ hai phép tính; diễn giải sâu và câu hỏi để s04-08; không tính C, D trên mặt (giữ trong ghi chú).
- **Ví dụ và số liệu:** VD3: $s_A=\tfrac8{35}$, $s_B=-\tfrac{37}{140}$ (NG1 VD5.12); C: $\tfrac{13}{70}$, D: $-\tfrac{37}{140}$ (ghi chú).
- **Hình thức hóa:** HT5 áp dụng.
- **Kết nối vào–ra cụ thể:** nhận bảng từ s04-06; nhả hai giá trị cho s04-08 (câu hỏi mass âm) và s06-04.
- **Nguồn:** NG1 VD5.12, p203–204/PDF29–30.
- **Thời lượng:** 3 phút (1' khối A, 1' khối B, 1' kết luận dấu).
- **Ghi chú soạn:** bước nói: trừ trước, chia sau; kiểm nhanh $t_B=\tfrac{59}{210}\approx.281$ và $r_B=\tfrac29\approx.222$ để thấy $t_B>r_B$; sai lầm: đổi mẫu số tùy ý — giữ phân số nguồn.

#### lec04-s04-08 — Kiểm tra phần 4: mass âm nghĩa gì

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 4; đo MT3 — diễn giải mass đúng, không coi là xác suất.
- **Luận điểm trung tâm:** dấu của mass cho biết quan hệ giữa hai điểm số, không phải nhãn nhị phân rác/sạch.
- **Nội dung cụ thể (đề trên mặt slide):** Câu hỏi: cho $t_B=\tfrac{59}{210}$ và $r_B=\tfrac29$ (hai giá trị ghi sẵn trên mặt). (i) tính $s_B$; (ii) mass âm nghĩa gì? (iii) có được kết luận "xác suất trang B là rác" không? Vì sao?
- **Bố cục đã chọn:** trái 40%: hai ô giá trị $t_B$, $r_B$ xếp chồng; phải 60%: hộp 3 câu hỏi (i)–(iii); dòng dưới: công thức $s_p=(r_p-t_p)/r_p$ để tra. Không có đáp án trên mặt.
- **Trọng tâm và thứ tự đọc:** hai giá trị trước, công thức giữa, ba câu hỏi sau.
- **Lý do phù hợp sinh viên năm 3:** đúng thao tác s04-07 nhưng đổi đỉnh; chỗ dễ nhầm: câu (iii) — sinh viên hay trả lời "được, vì mass trong [0,1]"; kiểm tra này nhắm thẳng vào hiểu sai phổ biến nhất của phần.
- **Giới hạn bố cục:** mặt slide chỉ đề và công thức; đáp án đầy đủ để ghi chú.
- **Ví dụ và số liệu:** VD3: $s_B=-\tfrac{37}{140}$ (NG1 VD5.12).
- **Hình thức hóa:** HT5.
- **Kết nối vào–ra cụ thể:** nhận định nghĩa từ s04-05 và dữ kiện từ s04-06; nhả năng lực diễn giải cho s06-04 (câu hỏi "mass âm được không").
- **Nguồn:** NG1 VD5.12, p203–204/PDF29–30.
- **Câu hỏi đủ dữ kiện:** có — $t_B$, $r_B$, công thức đều trên mặt slide.
- **Đáp án (trong ghi chú):** (i) $s_B=(\tfrac29-\tfrac{59}{210})/\tfrac29=-\tfrac{37}{140}$. (ii) mass âm nghĩa là $t_B>r_B$: điểm trust của B cao hơn PageRank nền trong thiết lập đang dùng — không suy thêm "được đánh giá tin cậy hơn" vì hai cột có thiết lập khác nhau. (iii) Không — mass không phải xác suất, không có ngưỡng chắc chắn; chỉ là tỷ số so sánh.
- **Tiêu chí đánh giá:** đúng $-\tfrac{37}{140}$; diễn giải trong phạm vi "$t_B>r_B$"; từ chối đúng câu (iii) với lý do "không phải xác suất"; lỗi hiểu sai: gọi mass là xác suất, hoặc kết luận "B chắc chắn sạch".
- **Thời gian hoạt động:** trong 2 phút: 45" suy nghĩ, 45" trả lời, 30" chữa.
- **Thời lượng:** 2 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** khi chữa, nhấn lại cảnh báo hai thiết lập của s04-06; nếu lớp hỏi "vì sao chọn $r$ không hệ số suy giảm", trả lời: đó là thiết lập nguồn VD5.12, không đổi để đẹp ví dụ.

#### lec04-s05-01 — Phạm vi: đồ thị con đã chọn, hai đầu ra

- **Vai trò và mục tiêu:** mở phần 5; đặt HITS vào bối cảnh khác PageRank: chạy trên đồ thị con theo truy vấn, cho hai điểm số. Nền MT4.
- **Luận điểm trung tâm:** HITS nhận một đồ thị con đã chọn và trả về hai điểm cho mỗi trang: trung tâm và thẩm quyền.
- **Nội dung cụ thể:** quy trình: truy vấn → chọn đồ thị con (cách chọn nằm ngoài tuyến chính) → chạy HITS trên đồ thị cố định đó → hai vector đầu ra $h$ (hub) và $a$ (authority). Nhấn: HITS chạy trên đồ thị đã chọn cố định; không khẳng định HITS chỉ chạy được trên đồ thị nhỏ.
- **Bố cục đã chọn:** dải ngang 4 bước: "truy vấn" → "chọn đồ thị con" → "chạy HITS" → "h, a"; dưới dải: 2 dòng: "đầu vào: graph đã chọn, cố định trong lúc chạy"; "đầu ra: hai vector, mỗi đỉnh hai điểm".
- **Trọng tâm và thứ tự đọc:** dải 4 bước trái→phải; hai dòng dưới chốt phạm vi.
- **Lý do phù hợp sinh viên năm 3:** sinh viên vừa xong ba mô hình toàn Web; khác biệt phạm vi (đồ thị con) là điểm cần nêu trước để không so sánh lệch; chỗ dễ nhầm: tưởng HITS thay thế PageRank — nó trả lời câu hỏi khác.
- **Giới hạn bố cục:** mặt slide chỉ quy trình và phạm vi; định nghĩa $h, a$ để s05-02; không thêm root/base algorithm.
- **Ví dụ và số liệu:** không áp dụng — slide định phạm vi.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận bối cảnh từ S04; nhả khung "hai đầu ra" cho s05-02.
- **Nguồn:** NG1 §5.5, p204–205/PDF30–31; NG5 slide 27–29 (phạm vi, đối chiếu, ≤200 từ tổng cho cả cụm Cornell).
- **Thời lượng:** 2 phút (1' dải bước, 1' phạm vi).
- **Ghi chú soạn:** nói: "cách chọn graph theo truy vấn là bài toán riêng, không học hôm nay"; sai lầm: khẳng định "HITS chỉ chạy được trên đồ thị nhỏ" — không có căn cứ, không nói.

#### lec04-s05-02 — Ví dụ 5.13: định nghĩa hub và authority

- **Vai trò và mục tiêu:** định nghĩa hai vai trò qua ví dụ khoa học; gắn từ Việt đầy đủ. Nền MT4.
- **Luận điểm trung tâm:** hub tốt trỏ tới nhiều authority tốt; authority tốt được nhiều hub tốt trỏ tới — hai vai trò nâng nhau.
- **Nội dung cụ thể:** VD 5.13: trang danh mục môn học của khoa (trỏ tới trang từng môn) = hub; trang từng môn học (được trang danh mục trỏ tới) = authority. Thuật ngữ: điểm trung tâm (hub), điểm thẩm quyền (authority); tên đầy đủ lần đầu: HITS — "tìm kiếm theo chủ đề dựa trên siêu liên kết" (Hyperlink-Induced Topic Search).
- **Bố cục đã chọn:** trái 50%: sơ đồ 1 trung tâm — ô "trang danh mục môn học của khoa (hub)" ở trên, mũi tên xuống các ô "trang từng môn học (authority)" ở dưới; phải 50%: 2 hộp định nghĩa: "hub: điểm trung tâm — trỏ tới authority tốt" và "authority: điểm thẩm quyền — được hub tốt trỏ tới"; dòng dưới: tên đầy đủ HITS.
- **Trọng tâm và thứ tự đọc:** sơ đồ trước (thấy trung tâm và các đích), hai hộp định nghĩa sau; đọc theo vòng "hub→authority→hub".
- **Lý do phù hợp sinh viên năm 3:** ví dụ danh mục môn học/trang từng môn gần trải nghiệm sinh viên; chỗ dễ nhầm: một trang chỉ có thể là hub hoặc authority — thực tế mỗi trang có cả hai điểm.
- **Giới hạn bố cục:** mặt slide chỉ định nghĩa; ma trận $L$ để s05-03; không đưa công thức cập nhật sớm.
- **Ví dụ và số liệu:** không áp dụng số — định nghĩa khái niệm (NG1 VD 5.13).
- **Hình thức hóa:** không áp dụng; định nghĩa khái niệm.
- **Kết nối vào–ra cụ thể:** nhận phạm vi từ s05-01; nhả hai vai trò cho s05-03 (G5).
- **Nguồn:** NG1 §5.5, VD 5.13, p205/PDF31.
- **Thời lượng:** 2 phút (1' sơ đồ, 1' hai định nghĩa).
- **Ghi chú soạn:** hỏi lớp: "trang danh mục môn học là hub hay authority?" — có thể cả hai; sai lầm: dùng "Selection" từ slide tham khảo — không dùng.

#### lec04-s05-03 — G5 và quy tắc tổng theo cạnh

- **Vai trò và mục tiêu:** thiết lập đồ thị ví dụ G5 và quy tắc đếm tổng theo cạnh. Nền MT4.
- **Luận điểm trung tâm:** điểm mới của mỗi đỉnh là tổng điểm các đỉnh nối với nó theo cạnh — trước khi viết ma trận.
- **Nội dung cụ thể:** G5: A→B,C,D; B→A,D; C→E; D→B,C; E không có cạnh ra; $n_H=5$, $m_H=8$. Khác G4: thay C→A bằng C→E. Quy tắc: $a_u$ mới = tổng $h_v$ cũ với $v\to u$; $h_v$ mới = tổng $a_u$ mới với $v\to u$.
- **Bố cục đã chọn:** trái 50%: đồ thị G5 với 5 đỉnh nhãn A–E, 8 cạnh; đỉnh E có nhãn "không cạnh ra"; phải 50%: 2 dòng quy tắc tổng theo cạnh (một cho $a$, một cho $h$) + dòng "khác G4: C→A đổi thành C→E".
- **Trọng tâm và thứ tự đọc:** đồ thị trước (đếm cạnh từng đỉnh), quy tắc sau; dừng ở đỉnh E để thấy "không cạnh ra".
- **Lý do phù hợp sinh viên năm 3:** quy tắc tổng theo cạnh là bước trước ma trận — Cornell (NG5 slide 20–24) cũng nối theo hướng này; chỗ dễ nhầm: nhầm G5 với G4 (bài tập R3 dùng G4) — nhãn khác nhau ghi ngay.
- **Giới hạn bố cục:** mặt slide chỉ đồ thị và quy tắc; ma trận $L$ để s05-06; không tính số ở đây.
- **Ví dụ và số liệu:** VD4: G5, $n_H=5$, $m_H=8$ (NG1 Hình 5.18, p206/PDF32).
- **Hình thức hóa:** không áp dụng; quy tắc đếm.
- **Kết nối vào–ra cụ thể:** nhận hai vai trò từ s05-02; nhả G5 và quy tắc cho s05-04 (vòng 1).
- **Nguồn:** NG1 Hình 5.18, §5.5, p206/PDF32.
- **Thời lượng:** 3 phút (2' đọc đồ thị và đếm cạnh, 1' quy tắc).
- **Ghi chú soạn:** cho lớp đếm: E có 0 cạnh ra, 1 cạnh vào (từ C); sai lầm: dùng G4 thay G5 — nhắc bài tập sẽ dùng G4 riêng.

#### lec04-s05-04 — Vòng 1: raw a và a₁

- **Vai trò và mục tiêu:** chạy nửa đầu vòng 1 (authority trước); thiết lập thói quen trước chuẩn hóa → chuẩn hóa. Nền MT4.
- **Luận điểm trung tâm:** authority mới = tổng hub cũ theo cạnh đi vào; rồi chuẩn hóa theo phần tử lớn nhất.
- **Nội dung cụ thể:** khởi $h_0=\mathbf{1}$, $a_0=\mathbf{0}$ ($a_0$ chỉ để đo chênh). $a_{raw,i}=\sum_{j\to i}h_{old,j}$, nên $a_{raw}=(1,2,2,2,1)$ (tổng hub của các đỉnh trỏ tới); chuẩn hóa theo phần tử lớn nhất 2: $a_1=(\tfrac12,1,1,1,\tfrac12)$.
- **Bố cục đã chọn:** trái 45%: G5 giữ nguyên vị trí; phải 55%: 2 khối xếp dọc: khối "trước chuẩn hóa" với vector $(1,2,2,2,1)$ và chú thích "tổng theo cạnh đi vào"; khối "chuẩn hóa" với phép chia $\div 2$ và $a_1$; dòng dưới: "$h_0=\mathbf{1}$, $a_0=\mathbf{0}$ (đo chênh)".
- **Trọng tâm và thứ tự đọc:** khối trước chuẩn hóa trước (thấy tổng), khối chuẩn hóa sau; nhãn max "2" đọc rõ.
- **Lý do phù hợp sinh viên năm 3:** tách trước chuẩn hóa/chuẩn hóa thành hai khối giúp thao tác thành hai bước nhỏ; chỗ dễ nhầm: quên khởi $a_0=\mathbf{0}$ và tưởng $a$ tham gia vòng 1 — vòng 1 chỉ dùng $h_0$.
- **Giới hạn bố cục:** mặt slide chỉ nửa authority của vòng 1; nửa hub để s05-05; không hiện ma trận $L$.
- **Ví dụ và số liệu:** VD4 vòng 1: $a_{raw}=(1,2,2,2,1)$, $a_1=(\tfrac12,1,1,1,\tfrac12)$ (NG1; numbers.json HITS_5_18).
- **Hình thức hóa:** một phần HT6.
- **Kết nối vào–ra cụ thể:** nhận quy tắc từ s05-03; nhả $a_1$ cho s05-05.
- **Nguồn:** NG1 §5.5, Hình 5.19–5.20, p206–207/PDF32–33.
- **Thời lượng:** 3 phút (1' khởi tạo, 2' raw và scale).
- **Ghi chú soạn:** bước nói: đỉnh B nhận trỏ từ A và D, mỗi đỉnh $h_0=1$ → $a_{raw,B}=2$; sai lầm: dùng $a_0$ để tính — $a_0$ chỉ đo chênh.

#### lec04-s05-05 — Vòng 1: raw h và h₁

- **Vai trò và mục tiêu:** hoàn tất vòng 1 với nửa hub; thấy $h_E=0$ lần đầu. Nền MT4.
- **Luận điểm trung tâm:** hub mới = tổng authority mới theo cạnh đi ra; đỉnh không có cạnh ra cho 0.
- **Nội dung cụ thể:** $h_{raw,i}=\sum_{i\to j}a_{new,j}$, nên $h_{raw}=(3,\tfrac32,\tfrac12,2,0)$ (tổng $a_1$ của các đỉnh mà đỉnh đó trỏ tới); chuẩn hóa theo phần tử lớn nhất 3: $h_1=(1,\tfrac12,\tfrac16,\tfrac23,0)$. $h_E=0$ vì E không có cạnh ra.
- **Bố cục đã chọn:** trái 45%: G5 giữ nguyên; phải 55%: 2 khối "trước chuẩn hóa" và "chuẩn hóa" như s05-04, nhãn max "3"; khung nhỏ dưới: "$h_E=0$: E không cạnh ra" với mũi tên chỉ đỉnh E trên đồ thị.
- **Trọng tâm và thứ tự đọc:** khối trước chuẩn hóa trước, khối chuẩn hóa sau; khung $h_E=0$ đọc cuối — là dữ kiện cho câu hỏi s05-11.
- **Lý do phù hợp sinh viên năm 3:** sinh viên hay trộn hai chiều cập nhật; khối này đối lập với s05-04 (đi vào vs đi ra) giúp phân biệt; chỗ dễ nhầm: tưởng E "vô dụng" — authority của E vẫn sẽ dương.
- **Giới hạn bố cục:** mặt slide chỉ nửa hub vòng 1; ma trận $L$ và đối chiếu $P$ để s05-06.
- **Ví dụ và số liệu:** VD4 vòng 1: $h_{raw}=(3,\tfrac32,\tfrac12,2,0)$, $h_1=(1,\tfrac12,\tfrac16,\tfrac23,0)$ (NG1; numbers.json).
- **Hình thức hóa:** một phần HT6.
- **Kết nối vào–ra cụ thể:** nhận $a_1$ từ s05-04; nhả $h_1$ cho s05-07 (vòng 2).
- **Nguồn:** NG1 §5.5, Hình 5.19–5.20, p206–207/PDF32–33.
- **Thời lượng:** 3 phút (1' raw, 1' scale, 1' $h_E=0$).
- **Ghi chú soạn:** bước nói: A trỏ tới B, C, D → $h_{raw,A}=a_B+a_C+a_D=1+1+1=3$; sai lầm: tính $h$ từ $L^T$ — sai hướng; nhắc lần chuẩn hóa mỗi vòng khác nhau (2 rồi 3).

#### lec04-s05-06 — Ma trận L hàng nguồn, đối chiếu với P

- **Vai trò và mục tiêu:** hình thức hóa hai quy tắc tổng thành ma trận; phân biệt $L$ với $P$. HT6 (phần ma trận).
- **Luận điểm trung tâm:** $L$ có hàng là nguồn — khác $P$ có cột là nguồn; hai phép nhân $L^Th$ và $La$ tương ứng hai quy tắc.
- **Nội dung cụ thể:** $$L=\begin{bmatrix}0&1&1&1&0\\1&0&0&1&0\\0&0&0&0&1\\0&1&1&0&0\\0&0&0&0&0\end{bmatrix}$$ hàng = đỉnh nguồn. Hàng $i$ của $L^T$ (tức cột $i$ của $L$) liệt kê các nguồn $j\to i$: $a_{raw,i}=\sum_j L_{ji}\,h_{old,j}$; hàng $i$ của $L$ liệt kê các đích $i\to j$: $h_{raw,i}=\sum_j L_{ij}\,a_{new,j}$. Nhắc: $P$ của PageRank có cột nguồn, $L$ có hàng nguồn — hai quy ước khác nhau.
- **Bố cục đã chọn:** trái 50%: ma trận $L$ 5×5 với nhãn hàng/cột A–E, chú thích "hàng = nguồn"; phải 50%: 2 dòng công thức $a_{raw,i}=\sum_j L_{ji}h_{old,j}$, $h_{raw,i}=\sum_j L_{ij}a_{new,j}$, dưới là 1 dòng đối chiếu "P: cột nguồn ↔ L: hàng nguồn".
- **Trọng tâm và thứ tự đọc:** ma trận trước (kiểm hàng A có 1 ở B, C, D), công thức sau, dòng đối chiếu cuối.
- **Lý do phù hợp sinh viên năm 3:** sinh viên vừa quen $P$ cột nguồn ở Bài 03; đặt hai quy ước cạnh nhau ngăn lỗi nhân nhầm chiều — lỗi đã liệt kê trong kiểm số VD4; hàng 5 toàn 0 nhìn thấy ngay E không cạnh ra.
- **Giới hạn bố cục:** mặt slide chỉ $L$ và hai công thức; vòng 2 để s05-07; không dựng $LL^T$.
- **Ví dụ và số liệu:** VD4: $L$ như trên (NG1 Hình 5.19, p206/PDF32).
- **Hình thức hóa:** HT6 (phần ma trận).
- **Kết nối vào–ra cụ thể:** nhận hai quy tắc từ s05-04..05; nhả ký hiệu $L^Th$, $La$ cho s05-07..08.
- **Nguồn:** NG1 Hình 5.19, §5.5, p206/PDF32.
- **Thời lượng:** 3 phút (1' đọc ma trận, 2' đối chiếu hai phép nhân).
- **Ghi chú soạn:** hỏi lớp: "hàng nào toàn 0? vì sao?" — hàng E; sai lầm: viết $L$ cột nguồn như $P$ — cho kết quả sai; không dựng $LL^T$/$L^TL$ vì có thể đặc.

#### lec04-s05-07 — Vòng 2: raw và scale đủ hai vai trò

- **Vai trò và mục tiêu:** chạy vòng 2 đầy đủ; thấy các đỉnh phân hóa. Hoàn thành dữ kiện VD4.
- **Luận điểm trung tâm:** vòng 2 dùng trạng thái mới của vòng 1 — cập nhật luân phiên từ trạng thái cũ.
- **Nội dung cụ thể:** $a_{raw}=L^Th_1=(\tfrac12,\tfrac53,\tfrac53,\tfrac32,\tfrac16)$; chuẩn hóa theo phần tử lớn nhất $\tfrac53$: $a_2=(\tfrac3{10},1,1,\tfrac9{10},\tfrac1{10})$. $h_{raw}=L\,a_2=(\tfrac{29}{10},\tfrac65,\tfrac1{10},2,0)$; chuẩn hóa theo phần tử lớn nhất $\tfrac{29}{10}$: $h_2=(1,\tfrac{12}{29},\tfrac1{29},\tfrac{20}{29},0)$. Nhãn giữa cột 1–2: "chia $\tfrac53$", giữa cột 3–4: "chia $\tfrac{29}{10}$" — bốn số chia trong hai vòng của ví dụ này khác nhau; giữ nguyên từng số chia; vòng 1 (max $2, 3$) chỉ đối chiếu trong ghi chú.
- **Bố cục đã chọn:** bảng 5 hàng (A–E) × 4 cột ($a_{raw}$, $a_2$, $h_{raw}$, $h_2$) chiếm toàn chiều rộng; nhãn "chia $\tfrac53$" giữa cột 1–2, "chia $\tfrac{29}{10}$" giữa cột 3–4; dòng dưới: "cập nhật luân phiên: $a$ từ $h_{old}$, $h$ từ $a_{new}$".
- **Trọng tâm và thứ tự đọc:** bảng theo hàng A→E, trong hàng đọc $a_{raw}\to a_2\to h_{raw}\to h_2$; nhãn chia giữa cột để tra lần chuẩn hóa.
- **Lý do phù hợp sinh viên năm 3:** bảng một vòng giúp thấy phân hóa các đỉnh và các lần chuẩn hóa khác nhau; chỗ dễ nhầm: dùng $a_1$ cũ khi tính $h$ — phải dùng $a_2$ mới; giữ phân số nguồn tránh trộn lần chuẩn hóa.
- **Giới hạn bố cục:** mặt slide chỉ bảng vòng 2; vòng 1 chỉ đối chiếu trong ghi chú; giới hạn và thuật toán đầy đủ để s05-08..09; không hiện giá trị thập phân.
- **Ví dụ và số liệu:** VD4 vòng 2: các giá trị trên (NG1; numbers.json HITS_5_18).
- **Hình thức hóa:** HT6 (bảng vòng).
- **Kết nối vào–ra cụ thể:** nhận $h_1$ từ s05-05 và $L$ từ s05-06; nhả hai vòng cho s05-08 (thuật toán) và s05-11 (kiểm tra).
- **Nguồn:** NG1 Hình 5.20, §5.5, p207/PDF33.
- **Thời lượng:** 3 phút (1' phần a, 1' phần h, 1' nhãn chia).
- **Ghi chú soạn:** kiểm nhanh: $a_{raw,E}=h_{1,C}=\tfrac16$ → $a_{2,E}=\tfrac1{10}$ sau chia $\tfrac53$; vòng 1 chỉ đối chiếu trong ghi chú; sai lầm: quy đồng các lần chuẩn hóa — giữ nhãn $\tfrac53, \tfrac{29}{10}$.

#### lec04-s05-08 — Giả mã HITS: điều kiện biên và ba trạng thái kết thúc

- **Vai trò và mục tiêu:** khái quát hai vòng thành thuật toán với trường hợp biên và điều kiện dừng. HT6.
- **Luận điểm trung tâm:** mỗi vòng là 2 quét cạnh + 2 quét max; dừng theo ngưỡng chênh, hết số vòng, hoặc suy biến.
- **Nội dung cụ thể (giả mã 13 dòng):**
  1. Nhận danh sách cạnh của đồ thị $n_H\ge1$ đỉnh, $\tau>0$, $K_{max}\ge1$ nguyên; $L\in\{0,1\}^{n_H\times n_H}$ là ma trận kề tương ứng.
  2. Đặt $h_{old}\leftarrow\mathbf{1}$, $a_{old}\leftarrow\mathbf{0}$.
  3. Với $k=1,\ldots,K_{max}$, thực hiện các dòng 4–12:
  4. $a_{raw}\leftarrow L^Th_{old}$; $c_a\leftarrow\max_i a_{raw,i}$.
  5. Nếu $c_a=0$, trả $(\mathbf{0},\mathbf{0},\text{suy biến})$.
  6. $a_{new}\leftarrow a_{raw}/c_a$.
  7. $h_{raw}\leftarrow La_{new}$; $c_h\leftarrow\max_i h_{raw,i}$.
  8. Nếu $c_h=0$, trả $(\mathbf{0},\mathbf{0},\text{suy biến})$.
  9. $h_{new}\leftarrow h_{raw}/c_h$.
  10. $\epsilon\leftarrow\max(\|h_{new}-h_{old}\|_\infty,\|a_{new}-a_{old}\|_\infty)$.
  11. Nếu $\epsilon\le\tau$, trả $(h_{new},a_{new},\text{đạt ngưỡng})$.
  12. Gán $(h_{old},a_{old})\leftarrow(h_{new},a_{new})$.
  13. Sau vòng lặp, trả $(h_{old},a_{old},\text{chưa đạt})$.
- **Bố cục đã chọn:** Giả mã chiếm toàn chiều rộng và 85% vùng nội dung, mỗi dòng là một bước ngắn; thụt dòng 4–12 dưới vòng lặp. Dải dưới 15% có ba nhãn trạng thái: “suy biến”, “đạt ngưỡng”, “chưa đạt”. Không đặt thêm cột chú giải làm hẹp công thức; giữ thang chữ của mẫu.
- **Trọng tâm và thứ tự đọc:** Theo số dòng từ trên xuống; nhìn cặp tính–kiểm–chia cho thẩm quyền rồi cho trung tâm. Đọc điều kiện dừng và giá trị trả về sau cả hai cập nhật.
- **Lý do phù hợp sinh viên năm 3:** Hai số chia $c_a,c_h$ có nhãn riêng để không dùng nhầm hệ số chuẩn hóa. Cấu trúc lặp giống PageRank đã học; cặp trạng thái cũ–mới và ba lối kết thúc làm rõ phần mới của HITS.
- **Giới hạn bố cục:** Mặt slide chỉ giả mã 13 dòng ngắn và ba trạng thái; phép nhân ma trận được thực hiện bằng quét cạnh, không dựng ma trận đặc. Giải thích điều kiện hội tụ để s05-09.
- **Ví dụ và số liệu:** không chạy số mới — giả mã khái quát đúng hai vòng VD4 đã chạy tay.
- **Hình thức hóa:** HT6 dạng thuật toán.
- **Kết nối vào–ra cụ thể:** nhận hai vòng từ s05-07; nhả thuật toán cho bài tập R3 (s07-03) và so sánh với s02-07 ở s06-02.
- **Nguồn:** NG1 §5.5, p206–207/PDF32–33.
- **Thời lượng:** 3 phút (1' dòng 1–3, 1' dòng 4–7, 1' dòng 8 và cờ).
- **Ghi chú soạn:** $a_{old}=\mathbf{0}$ chỉ là mốc đo chênh ở vòng đầu; $a_{new}$ được tính từ $h_{old}$. Kiểm cả $c_a,c_h$ trước khi chia. Đồ thị không có cạnh trả hai vector 0 và cờ suy biến. Nhánh đạt trả cặp mới; hết số vòng trả cặp đã cập nhật cuối cùng và cờ chưa đạt. $\tau$ là ngưỡng thay đổi, không phải chứng nhận sai số tới nghiệm.

#### lec04-s05-09 — Vì sao hội tụ: vector riêng với điều kiện đủ

- **Vai trò và mục tiêu:** nêu cơ sở lý thuyết của lặp luân phiên; mức ghi chú chứng minh. HT7.
- **Luận điểm trung tâm:** điểm giới hạn là vector riêng của $L^TL$ và $LL^T$; hội tụ về hướng trội khi hướng trội duy nhất.
- **Nội dung cụ thể:** với $u\ge0$: $h_{u+1}\propto LL^Th_u$; $a_{u+1}\propto L^TL\,a_u$ chỉ với $u\ge1$ ($a_0=\mathbf{0}$ chỉ để đo chênh, không phải điểm khởi cho $a$) — lặp là phương pháp lũy thừa. **Các điều kiện sau đủ bảo đảm hội tụ về hướng trội (không phải điều kiện cần):** $L\ne0$; hướng trội duy nhất $\lambda_1>\lambda_2\ge0$ của $LL^T$ và $L^TL$; $h_0$ có hình chiếu khác 0 lên hướng trội của $LL^T$. Phác ý: sai số giảm như $(\lambda_2/\lambda_1)^u$ — không suy hội tụ từ vài vòng quan sát.
- **Bố cục đã chọn:** trên 40%: hai dòng suy ra $LL^Th_u$, $L^TLa_u$ (chỉ $u\ge1$) với nhãn "phương pháp lũy thừa"; giữa 40%: khung 3 điều kiện đủ đánh số; dưới 20%: dòng "phác ý: sai số ~ $(\lambda_2/\lambda_1)^u$; không suy hội tụ từ vài vòng".
- **Trọng tâm và thứ tự đọc:** hai dòng suy ra trước (thấy cấu trúc vector riêng), khung điều kiện sau, dòng phác ý cuối.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 chưa học Perron–Frobenius; nêu điều kiện đủ như "hộp kiểm" thay vì định lý trừu tượng; ý tưởng lũy thừa có khoảng cách phổ (NG5 slide 10) giúp họ tin cơ chế mà không cần chứng minh đầy đủ.
- **Giới hạn bố cục:** mặt slide 3 khối ngắn; chứng minh đầy đủ để ghi chú mở rộng; không tuyên bố hội tụ đơn nhất không điều kiện (claim slide 56 NG3 đã loại).
- **Ví dụ và số liệu:** đối chiếu VD4: các vòng cho thấy $h,a$ ổn định dần theo hướng; giới hạn $h\approx(1,.3583,0,.7165,0)$, $a\approx(.2087,1,1,.7913,0)$ (32 vòng để chênh hai vòng dưới $10^{-12}$) — ghi chú.
- **Hình thức hóa:** HT7 — điều kiện đủ hội tụ, mức ghi chú chứng minh.
- **Kết nối vào–ra cụ thể:** nhận thuật toán từ s05-08; nhả bảo đảm lý thuyết cho s05-10 (chi phí) và s06-01.
- **Nguồn:** NG1 §5.5, p207–208/PDF33–34; NG5 slide 10 (ý tưởng phương pháp lũy thừa, đối chiếu).
- **Thời lượng:** 3 phút (1' hai dòng suy ra, 1' ba điều kiện, 1' phác ý).
- **Ghi chú soạn:** Nhấn đây là điều kiện đủ, không phải điều kiện cần. $a_1$ là kết quả chuẩn hóa $L^Th_0$; $a_0=\mathbf{0}$ chỉ đo chênh, không dùng làm điểm khởi cho truy hồi theo $L^TL$. Giải thích phương pháp lũy thừa bằng phân rã theo các vector riêng của ma trận đối xứng: thành phần ngoài hướng trội giảm tương đối theo $(\lambda_2/\lambda_1)^u$. Không kết luận hội tụ chỉ từ vài vòng và không dựng các tích ma trận để tính trên đồ thị lớn.

#### lec04-s05-10 — Chi phí HITS: hai quét cạnh mỗi vòng

- **Vai trò và mục tiêu:** đếm phép toán; hoàn thành HT8 phần HITS. Nền MT5.
- **Luận điểm trung tâm:** mỗi vòng chỉ quét danh sách cạnh hai lần và tìm max hai lần — không cần ma trận đầy đủ.
- **Nội dung cụ thể:** 1 vòng: $a_{raw}$ quét cạnh (mỗi cạnh 1 phép cộng), $h_{raw}$ quét cạnh lần 2, cộng 2 lần tìm max → $\Theta(n_H+m_H)$/vòng và bộ nhớ $O(n_H+m_H)$. Không dựng $LL^T$/$L^TL$ vì có thể đặc ($O(n_H^2)$). Đối chiếu TSP: $\Theta(n+m_G)$/vòng — cùng bậc, khác cấu trúc cập nhật.
- **Bố cục đã chọn:** trên 45%: bảng 2 hàng (HITS / TSP) × 3 cột (1 vòng / bộ nhớ / cấu trúc); dưới 55%: sơ đồ 4 bước một vòng HITS: quét cạnh (a) → quét max → quét cạnh (h) → quét max, mỗi ô nhãn phép toán.
- **Trọng tâm và thứ tự đọc:** sơ đồ 4 bước trước (đếm theo bước), bảng đối chiếu sau.
- **Lý do phù hợp sinh viên năm 3:** sinh viên đã đếm chi phí TSP ở s02-09; bảng đối chiếu giúp thấy hai thuật toán cùng bậc chi phí nhưng HITS cho hai vector; chỗ dễ nhầm: tưởng cần nhân ma trận 5×5 đầy đủ.
- **Giới hạn bố cục:** mặt slide chỉ bảng và sơ đồ; so sánh 4 mô hình đầy đủ để s06-02.
- **Ví dụ và số liệu:** VD4: $n_H=5$, $m_H=8$ — mỗi vòng 2×8 phép cộng cạnh + 2×5 phép so max; không bịa quy mô lớn.
- **Hình thức hóa:** HT8 (phần HITS).
- **Kết nối vào–ra cụ thể:** nhận thuật toán từ s05-08; nhả chi phí cho s06-02.
- **Nguồn:** NG1 §5.5, p208/PDF34; đặc tả đã duyệt mục chi phí.
- **Thời lượng:** 3 phút (1' sơ đồ, 1' bảng, 1' đối chiếu TSP).
- **Ghi chú soạn:** sai lầm: dựng $LL^T$ — ma trận có thể đặc, tốn $O(n_H^2)$; nhắc HITS trên đồ thị đã chọn cố định, cách chọn graph ngoài tuyến chính.

#### lec04-s05-11 — Kiểm tra phần 5: h_E và a_E

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 5; đo MT4 — hiểu hướng cập nhật luân phiên và scale.
- **Luận điểm trung tâm:** hai vai trò cập nhật theo hai chiều khác nhau — đỉnh có thể có một điểm bằng 0 và điểm kia dương.
- **Nội dung cụ thể (đề trên mặt slide):** Câu hỏi: trên G5: (i) vì sao $h_E=0$ ngay vòng 1? (ii) vì sao $a_E=\tfrac12>0$ ở vòng 1? (iii) vì sao $a_E$ vòng 2 $=\tfrac1{10}$? Chỉ giải thích các thành phần tại E, không tính lại toàn bộ vòng.
- **Bố cục đã chọn:** trái 40%: G5 giữ nguyên vị trí, đỉnh E được khoanh; phải 60%: hộp 3 câu hỏi (i)–(iii); dòng dưới: nhắc "cập nhật luân phiên, chuẩn hóa theo phần tử lớn nhất". Không có đáp án trên mặt.
- **Trọng tâm và thứ tự đọc:** đỉnh E trên đồ thị trước, ba câu hỏi sau.
- **Lý do phù hợp sinh viên năm 3:** ba câu bám đúng ba thao tác: đếm cạnh ra (i), đếm cạnh vào (ii), scale theo max (iii); chỗ dễ nhầm: tưởng E "bị bỏ" vì $h_E=0$ — authority của E vẫn dương vì có C→E.
- **Giới hạn bố cục:** mặt slide chỉ đề; lời giải từng bước để ghi chú.
- **Ví dụ và số liệu:** VD4: $h_E=0$; $a_{raw,E}$ vòng 1 $=1$ → $a_E=\tfrac12$; vòng 2: $a_{raw,E}=h_{1,C}=\tfrac16$, max $\tfrac53$ → $a_E=\tfrac1{10}$ (NG1; numbers.json).
- **Hình thức hóa:** HT6 áp dụng.
- **Kết nối vào–ra cụ thể:** nhận hai vòng từ s05-07; nhả hiểu biết hướng cập nhật cho s06-04 và bài tập R3.
- **Nguồn:** NG1 Hình 5.18–5.20, §5.5, p206–207/PDF32–33.
- **Câu hỏi đủ dữ kiện:** có — G5 vẽ sẵn, hai vòng đã học; không cần dữ kiện ngoài.
- **Đáp án (trong ghi chú):** (i) E không có cạnh ra → tổng authority các đỉnh E trỏ tới rỗng → $h_{raw,E}=0$. (ii) E có cạnh vào từ C, và $h_{0,C}=1$ → $a_{raw,E}=1$, chuẩn hóa theo phần tử lớn nhất 2 → $\tfrac12$. (iii) vòng 2: $a_{raw,E}=h_{1,C}=\tfrac16$; max $a_{raw}$ vòng 2 là $\tfrac53$ → $\tfrac16\div\tfrac53=\tfrac1{10}$.
- **Tiêu chí đánh giá:** đúng cả ba lý do; phân biệt cạnh ra/cạnh vào; lỗi hiểu sai: dùng $a_0$ để tính vòng 1, hoặc quên đổi max giữa các vòng.
- **Thời gian hoạt động:** trong 2 phút: 1' suy nghĩ, 30" trả lời, 30" chữa — tập trung giải thích, không tính toàn vòng.
- **Thời lượng:** 2 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** chữa bằng cách chỉ đỉnh E và lần lượt hai chiều mũi tên; nếu lớp nhầm (iii), viết lại phép chia $\tfrac16/\tfrac53$ 30 giây; không mở rộng sang giới hạn.

#### lec04-s06-01 — Bảng bốn mô hình

- **Vai trò và mục tiêu:** mở phần 6; gom bốn mô hình vào một bảng để so sánh. Hỗ trợ MT5.
- **Luận điểm trung tâm:** bốn mô hình khác nhau ở đầu vào, đầu ra và câu hỏi mà chúng trả lời — không phải "tốt hơn" tuyệt đối.
- **Nội dung cụ thể:** Bảng bốn hàng với các cột mô hình, đầu vào, đầu ra, cách dùng: PageRank cơ sở — đồ thị và $\beta$ — vector $r$ — xếp hạng chung; PageRank theo chủ đề — thêm tập $S$ — vector $r_S$ — xếp hạng theo chủ đề; TrustRank — thêm tập tin cậy $T$ — vector $t$ — đánh giá tín hiệu tin cậy; HITS — đồ thị con đã chọn — cặp $h,a$ — phân biệt hai vai trò. Ghi chú dưới bảng: khối lượng rác được tính thêm từ cả $r$ và $t$, không phải đầu ra riêng của TrustRank.
- **Bố cục đã chọn:** bảng 4 hàng × 4 cột (mô hình / đầu vào thêm / đầu ra / câu hỏi trả lời) chiếm 75% giữa; cột "đầu vào thêm" được nhấn bằng khung; dòng dưới: "cùng nền: đồ thị có hướng, ma trận–vector".
- **Trọng tâm và thứ tự đọc:** đọc theo hàng, cột "đầu vào thêm" trước để thấy mỗi mô hình thêm gì.
- **Lý do phù hợp sinh viên năm 3:** sau ba phần thuật toán, sinh viên cần gộp lại thành bản đồ chọn mô hình; chỗ dễ nhầm: tưởng TSP thay thế PR cơ sở — bảng cho thấy TSP là PR cơ sở cộng một đầu vào.
- **Giới hạn bố cục:** mặt slide chỉ bảng; so chi phí để s06-02; không thêm hàng RWR/SimRank/Pixie (đã bỏ).
- **Ví dụ và số liệu:** không áp dụng số — bảng tổng hợp; các giá trị ví dụ đã thấy ở các phần.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận ba mô hình từ S02–S05; nhả bảng cho s06-02 (chi phí) và s06-04 (kiểm tra).
- **Nguồn:** NG1 §5.3–5.5 tổng hợp; NG5 slide 34 (so PR/HITS, đối chiếu).
- **Thời lượng:** 2 phút (đọc bảng theo hàng).
- **Ghi chú soạn:** hỏi nhanh: "mô hình nào cần đầu vào do con người thẩm định?" — TrustRank ($T$); sai lầm: gộp $q_S$ và $T$ thành một loại — $q_S$ là chủ đề, $T$ là tập tin cậy; nhấn: TrustRank chỉ trả vector $t$, spam mass phải tính thêm từ vector PageRank $r$.

#### lec04-s06-02 — So sánh chi phí trong cùng tham số

- **Vai trò và mục tiêu:** so chi phí bốn mô hình trên cùng tham số; hoàn thành HT8. Hỗ trợ MT5.
- **Luận điểm trung tâm:** so chi phí chỉ có nghĩa trong cùng mô hình và cùng tham số — không kết luận "nhanh hơn" ngoài mô hình.
- **Nội dung cụ thể:** TSP: 1 vòng $\Theta(n+m_G)$; $k$ chủ đề $O(kI(n+m_G))$, lưu $O(kn)$. TrustRank: như TSP (dùng lại). HITS: $\Theta(n_H+m_H)$/vòng trên đồ thị con. Farm: đánh giá biểu thức $O(1)$ khi đã biết $x$; tìm PageRank nền vẫn cần lặp. Ghi dòng: "so sánh trong cùng tham số; không kết luận nhanh hơn ngoài mô hình".
- **Bố cục đã chọn:** bảng 4 hàng (TSP / Trust / HITS / cụm thao túng) × 3 cột (chi phí chính / bộ nhớ / điều kiện áp dụng); bảng 70% giữa; dòng cảnh báo dưới cùng trong khung.
- **Trọng tâm và thứ tự đọc:** bảng theo hàng; cột "điều kiện áp dụng" đọc kỹ — nơi chứa giới hạn.
- **Lý do phù hợp sinh viên năm 3:** sinh viên đã thấy từng con số ở s02-09, s05-10, s03-07; bảng gộp giúp trả lời câu hỏi thi dạng "chọn mô hình cho tình huống"; chỗ dễ nhầm: so HITS (đồ thị con nhỏ) với PR (toàn Web) rồi kết luận HITS rẻ hơn.
- **Giới hạn bố cục:** mặt slide chỉ bảng; các dẫn chiếu chi tiết để ghi chú; không bịa quy mô Web thực.
- **Ví dụ và số liệu:** không chạy số mới — tổng hợp các độ phức tạp đã duyệt (HT8).
- **Hình thức hóa:** HT8.
- **Kết nối vào–ra cụ thể:** nhận các độ phức tạp từ s02-09, s03-07, s05-10; nhả bảng cho s06-04.
- **Nguồn:** NG1 §5.3–5.5; đặc tả đã duyệt mục chi phí.
- **Thời lượng:** 2 phút (đọc bảng, nhấn dòng cảnh báo).
- **Ghi chú soạn:** sai lầm cần chặn: "HITS nhanh hơn vì graph nhỏ" — đồ thị con nhỏ là lựa chọn đầu vào, không phải tính chất thuật toán; nhắc farm $O(1)$ chỉ khi đã biết $x$.

#### lec04-s06-03 — Thu hồi jaguar, cụm thao túng và hai vai trò

- **Vai trò và mục tiêu:** khép lại câu hỏi mở đầu; cho sinh viên biết chọn đầu vào/đầu ra nào cho từng nhu cầu. Hoàn thành MT5 về mặt nhận thức.
- **Luận điểm trung tâm:** mỗi hạn chế nêu đầu bài giờ có một công cụ và một giới hạn tương ứng.
- **Nội dung cụ thể:** (1) jaguar → TSP: đổi $q_S$ theo chủ đề, phối hợp $\sum\alpha_l r_l$. (2) cụm thao túng → hiểu bằng phương trình farm, phòng vệ bằng TrustRank/mass — với giới hạn giả thiết. (3) hai vai trò → HITS trên đồ thị con. Mỗi dòng kèm "đầu vào cần chuẩn bị" và "đầu ra nhận được".
- **Bố cục đã chọn:** 3 hàng ngang, mỗi hàng 3 ô: nhu cầu (trái 30%) / công cụ (giữa 40%) / giới hạn (phải 30%); hàng 1 jaguar, hàng 2 farm–trust, hàng 3 hai vai trò.
- **Trọng tâm và thứ tự đọc:** theo hàng; cột "giới hạn" đọc sau cùng mỗi hàng — nhắc bài không hứa quá.
- **Lý do phù hợp sinh viên năm 3:** sinh viên cần câu trả lời "học xong dùng khi nào"; bố cục 3 ô/hàng ép ghép nhu cầu–công cụ–giới hạn thành một câu hoàn chỉnh; chỗ dễ nhầm: quên giới hạn của giả thiết trust.
- **Giới hạn bố cục:** mặt slide 3 hàng ngắn; khép 3 giới hạn đầy đủ để s06-05.
- **Ví dụ và số liệu:** không áp dụng số — tổng hợp; nhắc lại $r^*=(\tfrac{54}{210},\tfrac{59}{210},\tfrac{38}{210},\tfrac{59}{210})$ nếu cần đối chiếu.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận bảng mô hình từ s06-01; nhả ba cặp nhu cầu–công cụ cho s06-04.
- **Nguồn:** NG1 §5.3–5.5 tổng hợp.
- **Thời lượng:** 2 phút (30" mỗi hàng, 30" chốt).
- **Ghi chú soạn:** hỏi lớp trước khi hiện cột giới hạn: "công cụ này hứa được gì?"; sai lầm: nói "TrustRank loại bỏ rác" — chỉ giảm tin vào trang rác theo giả thiết.

#### lec04-s06-04 — Kiểm tra tích hợp: bốn nhiệm vụ

- **Vai trò và mục tiêu:** slide kiểm tra riêng phần 6; đo MT5 — chọn và vận dụng đúng mô hình cho từng tình huống.
- **Luận điểm trung tâm:** mỗi mô hình có một "núm vặn" riêng — biết núm nào ở đâu là biết dùng mô hình.
- **Nội dung cụ thể (đề trên mặt slide):** bốn câu hỏi trên các ví dụ đã học, mỗi ô nhãn **Câu hỏi:**: (1) muốn trang ô tô lên cao cho người đọc chủ đề ô tô — chọn mô hình rồi chỉ chỗ thay $q_S$ trong công thức; (2) trong phương trình farm, hạng nào bị bỏ TRONG PHƯƠNG TRÌNH trước khi giải? (3) spam mass âm — được không, nghĩa gì? (4) cần hai vai trò trung tâm/thẩm quyền — chọn mô hình rồi chỉ chiều nhân ma trận.
- **Bố cục đã chọn:** 4 ô câu hỏi xếp lưới 2×2, mỗi ô nhãn Câu hỏi số; không lộ đáp án.
- **Trọng tâm và thứ tự đọc:** theo số 1→4; mỗi ô tự chứa đủ dữ kiện từ ví dụ đã học.
- **Lý do phù hợp sinh viên năm 3:** bốn câu bám đúng bốn hiểu sai đã chặn trong bài: quên chỗ thay $q_S$, nhầm hạng bị bỏ, coi mass là xác suất, nhân nhầm chiều ma trận; dạng tích hợp giúp sinh viên tự thấy mô hình nào mình còn lơ mơ.
- **Giới hạn bố cục:** mặt slide chỉ 4 câu; đáp án và lỗi hiểu sai để ghi chú; không thêm câu mới.
- **Ví dụ và số liệu:** dùng lại VD1 (TSP), VD2 (cụm thao túng), VD3 (mass), VD4 (HITS) — không số mới.
- **Hình thức hóa:** HT1, HT4, HT5, HT6 áp dụng.
- **Kết nối vào–ra cụ thể:** nhận toàn bộ bài; củng cố kiến thức đã học; nối sang bài tập S07.
- **Nguồn:** NG1 §5.3–5.5 (các ví dụ đã dẫn).
- **Câu hỏi đủ dữ kiện:** có — mỗi câu dựa trên ví dụ đã học trong bài, dữ kiện đã trình bày.
- **Đáp án (trong ghi chú):** (1) thay $q_S$ trong hạng dịch chuyển $(1-\beta)q_S$ của $r'=\beta Pr+(1-\beta)q_S$ — chọn $q_S$ phân bố trên tập trang ô tô; lỗi hiểu sai: đổi $\beta$ hoặc $P$. (2) hạng $(1-\beta)/N$ — phần dịch chuyển trực tiếp; lỗi: chọn $\beta q(1-\beta)/N$. (3) được — mass có thể âm, nghĩa là $t_p>r_p$ trong thiết lập đang dùng; không phải xác suất; lỗi: gọi là xác suất rác. (4) $L^T$ nhân với $h$ cũ: $a_{raw}=L^Th_{old}$; lỗi: nhân $L$ hoặc $L^TL$.
- **Tiêu chí đánh giá:** đo lựa chọn mô hình và lý do kèm theo, không chỉ nhớ công thức; mỗi câu rút được lỗi hiểu sai tương ứng; sai ≥2 câu cho thấy cần ôn phần đó.
- **Thời gian hoạt động:** trong 5 phút: 4×1' suy nghĩ–trả lời từng nhiệm vụ, 1' chữa tổng.
- **Thời lượng:** 5 phút (toàn bộ là hoạt động kiểm tra).
- **Ghi chú soạn:** giữ nhịp 1 phút mỗi câu; nếu câu nào lớp sai rộng, ghi lại để mở bài tập tương ứng; không chữa dài quá 1 phút.

#### lec04-s06-05 — Khép ba giới hạn và nối tiếp

- **Vai trò và mục tiêu:** khép bài bằng ba giới hạn; nối bài tập và đọc thêm. Không có kiểm tra riêng.
- **Luận điểm trung tâm:** ba mô hình đều có giới hạn rõ — biết giới hạn là một phần của năng lực.
- **Nội dung cụ thể:** (1) TSP: cần tập đại diện chủ đề do người chọn; $r^*$ có thể có phần tử 0 khi $q_S$ hỗ trợ con. (2) Trust: dựa trên giả thiết "trang tốt ít trỏ rác" — không bảo đảm; mass không phải xác suất. (3) HITS: hội tụ theo điều kiện đủ; cách chọn đồ thị con ngoài tuyến chính. Nối: bài tập 3 bài (5.3.1, 5.4.2, 5.5.1); đọc thêm MMDS §5.3–5.5; Bài 05 so sánh tài liệu gần trùng — không dạy Jaccard hôm nay.
- **Bố cục đã chọn:** trái 55%: 3 dòng giới hạn đánh số, mỗi dòng một câu; phải 45%: hộp "tiếp theo": 3 dòng (bài tập trên lớp / đọc §5.3–5.5 / Bài 05).
- **Trọng tâm và thứ tự đọc:** giới hạn trước, hộp tiếp theo sau.
- **Lý do phù hợp sinh viên năm 3:** sinh viên năm 3 cần biết "thuật toán này không dùng được khi nào" trước khi làm bài tập; ba dòng khớp ba phần chính giúp ôn nhanh; hộp tiếp theo cho hành động cụ thể sau buổi học.
- **Giới hạn bố cục:** mặt slide 3 dòng + hộp; chi tiết giới hạn đã có ở các phần, không lặp.
- **Ví dụ và số liệu:** không áp dụng — slide khép.
- **Hình thức hóa:** không áp dụng.
- **Kết nối vào–ra cụ thể:** nhận tổng kết từ s06-03..04; nối sang s07-01 và tự học §5.3–5.5.
- **Nguồn:** NG1 §5.3–5.5 (giới hạn từng mô hình); NG0 (nối Bài 05).
- **Thời lượng:** 1 phút (đọc nhanh 3 dòng, giao bài tập).
- **Ghi chú soạn:** không mở chủ đề mới; nhắc mang máy tính/bảng tính cho phần 7; sai lầm: tuyên bố "đã kiểm render" — bài chỉ mới ở kế hoạch dàn bài.

#### lec04-s07-01 — Bài tập 5.3.1: TSP với hai tập $S$

- **Vai trò và mục tiêu:** hoạt động bài tập 1; vận dụng MT1 trên hai tập $S$ mới (Bài 5.3.1).
- **Luận điểm trung tâm:** đổi tập $S$ là đổi vector dịch chuyển — nghiệm thay đổi theo, nhưng quy trình giữ nguyên.
- **Nội dung cụ thể (đề đầy đủ trên mặt slide):** Câu hỏi: trên G4, dùng $\beta=0.8$ theo quy ước của Ví dụ 5.10. Tính PageRank theo chủ đề khi (a) $S=\{A\}$ và (b) $S=\{A,C\}$. Mỗi câu trình bày $q_S$, phương trình, nghiệm và phép kiểm tổng các thành phần bằng 1.
- **Bố cục đã chọn:** trái 35%: G4 cố định ở vị trí quen; giữa 40%: đề bài 2 câu (a), (b) và dòng quy ước "$\beta=.8$ kế thừa VD5.10"; phải 25%: bảng kết quả phải trống 2 hàng (tập $S$ / $q$ / $r^*$ / tổng) để điền khi chữa. Đáp án chỉ trong ghi chú.
- **Trọng tâm và thứ tự đọc:** đề giữa trước, quy ước ngay dưới, G4 trái để tra bậc ra; bảng phải chỉ điền khi chữa.
- **Lý do phù hợp sinh viên năm 3:** đúng quy trình s02-07 nhưng đổi đầu vào; hai tập $S$ cho hai vector $q$ khác nhau — nhãn tập $S$ trên từng cột chống trộn nghiệm; chỗ dễ nhầm: quên kiểm tổng 1.
- **Giới hạn bố cục:** mặt slide chỉ đề và bảng trống; lời giải từng bước để ghi chú; không tạo sổ tay mã/chương trình.
- **Ví dụ và số liệu:** NG1 Bài 5.3.1, p199/PDF25: đáp án (a) $S=\{A\}$: $q_S=(1,0,0,0)$, $r^*=(\tfrac37,\tfrac4{21},\tfrac4{21},\tfrac4{21})$; (b) $S=\{A,C\}$: $q_S=(\tfrac12,0,\tfrac12,0)$, $r^*=(\tfrac{27}{70},\tfrac6{35},\tfrac{19}{70},\tfrac6{35})$ — chỉ trong ghi chú.
- **Hình thức hóa:** HT1 áp dụng.
- **Kết nối vào–ra cụ thể:** nhận quy trình từ s02-07; củng cố s06-04 câu 1; nối s07-02.
- **Nguồn:** NG1 Bài 5.3.1, p199/PDF25.
- **Thời lượng:** 18 phút: 6' đọc đề và dựng $q$ + phương trình, 8' tính nghiệm (giải hệ hoặc lặp), 4' chữa và kiểm tổng 1.
- **Ghi chú soạn:** nhắc quy ước $\beta=.8$ trước khi bắt đầu; sai lầm: trộn nghiệm hai tập $S$ — nhãn cột theo tập $S$; nếu nhóm lặp chậm, gợi ý giải hệ trực tiếp. Tiêu chí: đúng $q_S$, phương trình/giải hệ hoặc lặp, nghiệm, tổng 1.

#### lec04-s07-02 — Bài tập 5.4.2: TrustRank và spam mass với $T=\\{B\\}$

- **Vai trò và mục tiêu:** hoạt động bài tập 2; vận dụng MT3 trọn quy trình: trust rồi mass (Bài 5.4.2).
- **Luận điểm trung tâm:** đổi $T$ thay đổi cả hai đầu ra — trust vector và mass — nhưng quy tắc tính không đổi.
- **Nội dung cụ thể (đề đầy đủ trên mặt slide):** cho G4, chỉ B tin cậy ($T=\{B\}$), TrustRank dùng $\beta=4/5$ (quy ước kế thừa VD5.10). PageRank nền $r=(\tfrac13,\tfrac29,\tfrac29,\tfrac29)$ — nguồn dùng không hệ số suy giảm ($\beta=1$), quy ước thừa kế; ghi cảnh báo hai thiết lập trên mặt bài. (a) Tính TrustRank từng trang. (b) Tính spam mass từng trang.
- **Bố cục đã chọn:** trái 35%: G4 cố định; giữa 40%: đề 2 câu + dòng dữ kiện $r_{base}$ + khung cảnh báo "hai thiết lập khác nhau"; phải 25%: bảng kết quả phải trống 2 khối (t / mass) × 4 đỉnh. Đáp án chỉ trong ghi chú.
- **Trọng tâm và thứ tự đọc:** dữ kiện $r_{base}$ trước (cần cho câu b), đề (a) rồi (b), cảnh báo đọc trước khi tính.
- **Lý do phù hợp sinh viên năm 3:** quy trình hai bước (trust → mass) đúng như s04-03..05; chỗ dễ nhầm: dùng $r^*$ của VD1 (có hệ số suy giảm) làm điểm nền — đề cố tình in $r_{base}$ trên mặt để tránh; mass âm tại B sẽ xuất hiện lại như VD3.
- **Giới hạn bố cục:** mặt slide chỉ đề, dữ kiện và bảng trống; đáp án để ghi chú; không đổi điểm nền.
- **Ví dụ và số liệu:** NG1 Bài 5.4.2, p204/PDF30: đáp án $t=(\tfrac{198}{735},\tfrac{263}{735},\tfrac{116}{735},\tfrac{158}{735})$; mass $=(\tfrac{47}{245},-\tfrac{299}{490},\tfrac{71}{245},\tfrac8{245})$ — chỉ trong ghi chú.
- **Hình thức hóa:** HT5, HT2 (dùng lại) áp dụng.
- **Kết nối vào–ra cụ thể:** nhận quy tắc từ s04-03; củng cố s06-04 câu 3; nối s07-03.
- **Nguồn:** NG1 Bài 5.4.2, p204/PDF30.
- **Thời lượng:** 22 phút: 3' đọc dữ kiện và cảnh báo, 10' tính trust, 6' tính mass, 3' chữa.
- **Ghi chú soạn:** nhấn: $r$ nền không hệ số suy giảm là quy ước nguồn, không phải lỗi đề; sai lầm: quên cảnh báo hai thiết lập rồi kết luận sai về $T$; mass âm tại B ($-\tfrac{299}{490}$) — cùng diễn giải VD3, không phải xác suất; không nhầm $r$ nền với $r^*$ của VD1. Tiêu chí: đúng $t$, đúng tỷ số, diễn giải âm, không nhầm $r$ nền với $r^*$ VD1.

#### lec04-s07-03 — Bài tập 5.5.1: HITS trên G4 đến hội tụ

- **Vai trò và mục tiêu:** hoạt động bài tập 3; vận dụng MT4 trọn quy trình HITS đến hội tụ (Bài 5.5.1).
- **Luận điểm trung tâm:** hai vòng đầu tính tay được, nhưng đề yêu cầu đến hội tụ — phải hiểu điều kiện dừng, không dừng ở 2 vòng.
- **Nội dung cụ thể (đề đầy đủ trên mặt slide):** Câu hỏi: trên G4 của Hình 5.1, tính điểm trung tâm $h$ và điểm thẩm quyền $a$ của HITS. Dùng $L_4=\begin{bmatrix}0&1&1&1\\1&0&0&1\\1&0&0&0\\0&1&1&0\end{bmatrix}$ theo hàng nguồn; có thể dùng máy tính hoặc bảng tính. Nếu dùng phép lặp đã học, gợi ý ngưỡng thay đổi $\tau=0.001$. Sản phẩm: hai vector chuẩn hóa theo phần tử lớn nhất bằng 1 và cách tính; nếu lặp, kèm vết lặp cùng điều kiện dừng.
- **Bố cục đã chọn:** trái 35%: G4 cố định ở vị trí quen (nhãn "G4 — Hình 5.1"); giữa 40%: đề + ma trận $L_4$ + dòng "$\tau=.001$ gợi ý gần đúng"; phải 25%: bảng kết quả phải trống (hàng $h$, $a$ × 4 đỉnh). Đáp án chỉ trong ghi chú.
- **Trọng tâm và thứ tự đọc:** nhãn đồ thị trước (chốt G4, không G5), đề giữa, ma trận $L_4$ để tra; bảng phải điền khi nộp.
- **Lý do phù hợp sinh viên năm 3:** đây là bài duy nhất yêu cầu chạy đến hội tụ — kiểm đúng thao tác giả mã s05-08 (kiểm số chia, ba trạng thái kết thúc và điều kiện dừng); chỗ dễ nhầm số một: dùng G5 của ví dụ thay G4; nhầm $L_4$ với $L$ của G5.
- **Giới hạn bố cục:** mặt slide chỉ đề, $L_4$ và bảng trống; hai vòng bảng trợ giúp để ghi chú; đề cuối phải là hội tụ, không thay đề bằng 2 vòng.
- **Ví dụ và số liệu:** NG1 Bài 5.5.1, p208/PDF34: hai vòng đầu $a_1=(1,1,1,1)$, $h_1=(1,\tfrac23,\tfrac13,\tfrac23)$; $a_2=(\tfrac35,1,1,1)$, $h_2=(1,\tfrac8{15},\tfrac15,\tfrac23)$; với $\tau=.001$ đạt ngưỡng thay đổi sau 11 vòng, $\epsilon\approx0.0007450739557$, $h\approx(1,.392369,.103046,.710676)$, $a\approx(.289993,1,1,.814221)$; 43 vòng chỉ khi dùng ngưỡng $10^{-12}$; nghiệm giới hạn làm tròn 4 số: $h\approx(1,.3919,.1028,.7108)$, $a\approx(.2892,1,1,.8136)$ — chỉ trong ghi chú, không gán số giới hạn cho chính vòng 11.
- **Hình thức hóa:** HT6, HT7, HT8 áp dụng.
- **Kết nối vào–ra cụ thể:** nhận thuật toán từ s05-08; khép bài, nối Bài 05.
- **Nguồn:** NG1 Bài 5.5.1, p208/PDF34.
- **Câu hỏi đủ dữ kiện:** có — G4, $L_4$, quy tắc lặp, $\tau$ đều trên mặt slide.
- **Đáp án (trong ghi chú):** hai vòng đầu như bảng trợ giúp; với $\tau=.001$: 11 vòng, $\epsilon\approx0.0007450739557$, $h\approx(1,.392369,.103046,.710676)$, $a\approx(.289993,1,1,.814221)$; 43 vòng chỉ khi ngưỡng $10^{-12}$; nghiệm giới hạn làm tròn 4 số $h\approx(1,.3919,.1028,.7108)$, $a\approx(.2892,1,1,.8136)$; cách lặp: $a_{raw}=L_4^Th_{old}$ → chuẩn hóa theo phần tử lớn nhất → $h_{raw}=L_4a_{new}$ → chuẩn hóa theo phần tử lớn nhất; ba trạng thái kết thúc: đạt ngưỡng chênh, chưa đạt khi hết số vòng cho phép, hoặc suy biến khi số chia bằng 0.
- **Tiêu chí đánh giá:** Chấp nhận nghiệm giới hạn làm tròn bốn chữ số hoặc trạng thái vòng 11 kèm báo cáo ngưỡng thay đổi $0.001$; không coi số chữ số in ra là bảo đảm sai số tới nghiệm. Hai vector được chuẩn hóa theo phần tử lớn nhất bằng 1; trình bày được cách tính. Với phép lặp, cần đúng hướng cập nhật, dùng trạng thái mới và kiểm cả hai chênh; không dừng tùy ý sau hai vòng. Chấp nhận cách giải ma trận đúng trên đồ thị bốn đỉnh, kể cả dùng $L_4^TL_4$. Dùng nhầm G5 là sai dữ kiện.
- **Thời gian hoạt động:** trong 20 phút: 4' dựng $L_4$ và kiểm, 10' tính lặp (máy tính/bảng tính), 3' kiểm điều kiện dừng, 3' chữa.
- **Thời lượng:** 20 phút (toàn bộ là hoạt động bài tập/kiểm tra; không cộng thêm thời gian).
- **Ghi chú soạn:** nhắc lại: G4 riêng, $L_4$ khác $L$ của G5 (C→A giữ nguyên, không có E); $\tau=.001$ là gợi ý gần đúng, không thay đề; nếu sinh viên hỏi "bao nhiêu vòng là đủ", trả lời: đến khi hai chênh $\le\tau$ — 11 vòng với $\tau=.001$, khoảng 43 vòng chỉ với ngưỡng $10^{-12}$; đề cuối là tính đến hội tụ, không chỉ 2 vòng.

---

## Ánh xạ cụm mới → mã deck cũ và note-topic-id

> Kế hoạch mới dùng mã `lec04-sXX-YY`; mã deck cũ P/T/S/K/H/Z/R chỉ để tra cứu, chưa dựng lại. Ánh xạ ở **cấp cụm/section** (không 1–1 từng slide); note-topic-id giữ nguyên bản đồ L04-N01…N07 đã có, không tạo note mới.

| Cụm mới | Mã deck cũ | note-topic-id | Chức năng | Kết nối vào–ra | Tiên quyết | Đầu ra | Thời lượng |
|---|---|---|---|---|---|---|---|
| S01 Giới thiệu (s01-01…06) | P00, P01, T00 | L04-N01 | Mở bài, mục lục, động lực jaguar, quy mô $n,U,k$, mục tiêu MT1–MT5, cầu nối ký hiệu $P:=S_{\text{Bài03}}$, kiểm tra tiên quyết | Vào: Bài 03 (ma trận sửa nút cụt); Ra: s02-01, s02-02 | Đồ thị có hướng, ma trận–vector, xác suất cơ bản | Mục lục và động lực bài | 10' / 6 slide |
| S02 PageRank theo chủ đề (s02-01…10) | T00–T07 | L04-N02 | Trực giác nhảy về tập đại diện, VD1 (G4, $S=\{B,D\}$), đặc tả HT1, giả mã thưa, HT2, k chủ đề HT3 | Vào: s01-06; Ra: s03-01, s04-03, s06-01 | Đóng góp theo cạnh, $\beta$ (kiểm ở s01-06) | Quy trình TSP và HT1–HT3 | 25' / 10 slide |
| S03 Cụm thao túng liên kết (s03-01…08) | S00–S05 | L04-N03 | Giới hạn tín hiệu, Hình 5.16 ba vùng, ký hiệu $N,q,x,y,z$, hệ phương trình, nghiệm chính xác/xấp xỉ HT4, hệ số $\beta=.85$ | Vào: s02-10; Ra: s04-01, s03-08→s06-04 | Dòng chảy theo cạnh, phần dịch chuyển | Nghiệm farm và HT4 | 22' / 8 slide |
| S04 TrustRank và khối lượng rác (s04-01…08) | K00–K05 | L04-N04 | Giả thiết cô lập, chọn $T$, quy tắc trust (dùng lại HT1/HT2), lỗi hạt giống/thiên lệch, mass HT5, VD3 bảng 5.17 | Vào: s02-08, s03-01; Ra: s06-01 | TSP (HT1, HT2), ý nghĩa cụm thao túng | Quy trình trust→mass và HT5 | 21' / 8 slide |
| S05 Hai vai trò của HITS (s05-01…11) | H00–H09 | L04-N05 | Phạm vi đồ thị con, VD 5.13, G5, hai vòng raw/scale, ma trận $L$ hàng nguồn HT6, giả mã, HT7, chi phí HT8 | Vào: S04; Ra: s06-01, s07-03 | Nhân ma trận–vector, trực giác hai vai trò | Thuật toán HITS và HT6–HT8 | 30' / 11 slide |
| S06 Tổng kết và kiểm tra (s06-01…05) | Z00–Z03 | L04-N06 | Bảng 4 mô hình, so chi phí cùng tham số, thu hồi jaguar/farm/hai vai trò, kiểm tra tích hợp MT5, khép 3 giới hạn | Vào: S02–S05 (củng cố kiến thức đã học); Ra: s07-01, Bài 05 | Toàn bộ chủ đề cốt lõi | Tổng hợp chọn mô hình | 12' / 5 slide |
| S07 Bài tập trên lớp (s07-01…03) | R00–R04 | L04-N07 | Bài 5.3.1 TSP hai tập $S$ (18'), Bài 5.4.2 TrustRank+mass với $T=\{B\}$ (22'), Bài 5.5.1 HITS trên G4 đến hội tụ (20') | Vào: s02-07, s04-03, s05-08; Ra: khép Bài 04, nối Bài 05 | Quy trình TSP, HT5, HT6–HT8 | Sản phẩm bài tập | 60' / 3 slide |

**Căn cứ khác biệt so với deck cũ (đã ghi trong phiếu, không lặp ở đây):** tách bước trực giác/đặc tả (T01–T02 cũ → s02-01/02/06), tách nghiệm chính xác khỏi xấp xỉ farm (S04–S05 cũ → s03-06), 7 kiểm tra riêng theo phần (s01-06, s02-10, s03-08, s04-08, s05-11, s06-04, s07-03) thay vì chỉ MT, bố cục cụ thể từng slide (bảng đóng góp, hai khối lượng, bảng hai vòng HITS), mở bài có cầu nối ký hiệu $P:=S_{\text{Bài03}}$ và đổi nghĩa $S$ (kế hoạch cũ nói "P đã học" là sai). Giữ nguồn và thứ tự MMDS §5.3–5.5; tổng 48 slide giảng/120' + 3 bài tập/60' = 51 slide, 7 phần chuẩn.

**Tác động khi triển khai HTML/notes (chưa sửa các tệp đó ở lượt này):** mỗi phiếu cần một trang HTML theo mã `lec04-sXX-YY`; slide kiểm tra cần đáp án/rubric trong ghi chú diễn giả; bảng tổng và ánh xạ trên là căn cứ dựng; chưa chạy kiểm render — mọi kết quả kiểm bản render cũ không gán cho kế hoạch này.


## Điều chỉnh khi triển khai và kiểm ảnh ngày 24/09/2026

Giữ nguyên 51 ID, thứ tự, mục tiêu, thời lượng và dữ kiện nguồn. Các quyết định dưới đây thay phần mô tả bố cục tương ứng khi có khác biệt, để khớp bản HTML đã kiểm định. Lý do chung là làm rõ quan hệ và giảm nội dung lặp, không giảm thang chữ của học phần.

| Slide | Bố cục triển khai cụ thể | Lý do phù hợp sinh viên năm 3 |
|---|---|---|
| s02-02 | Đồ thị 45%, bảng 55% | Đọc cùng vị trí đỉnh trước khi đối chiếu vector; sửa tổng tỷ lệ 105% trong phiếu cũ. |
| s02-03 | G4 chung bên trái, bảng cạnh vào bên phải; không thêm số lên cạnh | Bảng đã ghi tên cạnh nên tránh thêm một lớp mã số cạnh dễ lẫn với đóng góp. |
| s02-04 | Ba cột 30/30/40; các vector viết dọc, nhãn theo cạnh/dịch chuyển/tổng | Giữ thứ tự A–D và cho thấy hai dòng khối lượng mà không ép vector ngang dài. |
| s02-08 | Hai thẻ dọc bất biến/phép co; giả thiết ngắn ở trên, khai triển chứng minh trong notes | Giữ bước suy luận chính trên mặt; người học đối chiếu được giả thiết mà không phải đọc cả chứng minh cùng lúc. |
| s02-09 | Công thức phối hợp ở trên; bảng thời gian và bộ nhớ ở dưới | Phân biệt chi phí tính với chi phí lưu; thống nhất nghiệm chủ đề là $r^{(l)*}$. |
| s03-01 | Sơ đồ ba vùng 60%, ba luận điểm 40%; bỏ câu cảnh báo quy trình | Mở đúng mô hình sẽ dùng tiếp và không đưa vào sơ đồ giản lược sai cạnh. |
| s03-03 | Bảng đại lượng 55%, hình 45%; ý nghĩa ký hiệu ở chú thích cạnh hình | Không khẳng định hình có nhãn mà thực tế chỉ xuất hiện trong bảng. |
| s03-04 | Công thức trên, SVG dòng tổng hợp giữa, chú thích dưới | Nhìn đồng thời luồng từ ngoài, vòng đích–hỗ trợ và dịch chuyển đều; công thức vẫn đặt trong KaTeX. |
| s03-05 | Sơ đồ ba luồng 45%, công thức và chú giải 55% | Ghép ba luồng với ba số hạng, giữ hình trong chiều cao vùng nội dung. |
| s03-08 | Công thức trên; bốn ô gán nguồn 2×2; yêu cầu tìm hạng bỏ ở dưới | Có vùng trả lời thực thay vì lời chỉ dẫn tạo ô trống. |
| s04-01…04 | Giả thiết/so sánh bằng thẻ chữ thân bài; s04-03 có hai công thức xếp chồng | Dùng đúng thang chữ chung, nêu rõ TrustRank kế thừa PageRank theo chủ đề. |
| s04-06…07 | Bảng và định nghĩa cột; sau đó hai dải A/B với phép tỷ số | Bỏ vector lặp, giữ cảnh báo hai hệ số và phân biệt dấu bằng quan hệ giữa hai điểm. |
| s05-07 | Bảng 7 cột; hai số chia dùng ô gộp 5 hàng | Giữ rõ bốn trạng thái thô/chuẩn hóa và hai số chia riêng; không đổi các số bằng nhau của nguồn. |
| s05-09…10 | Hai phép truy hồi cạnh nhau; điều kiện đủ trong một thẻ; chi phí tách quét cạnh và quét đỉnh | Không coi quan sát số là chứng minh; không đếm thiếu chuẩn hóa và đo chênh. |
| s06-03 | Ba hàng nhu cầu–công cụ–giới hạn; khoảng cách gọn | Thu hồi ba vấn đề mở bài mà không gán ngữ nghĩa ô tô cho G4. |
| s07-01…03 | Đồ thị trái 35%, đề và bảng trả lời phải 65%; ma trận $L_4$ nằm trong notes | Đồ thị đủ dữ kiện để tự dựng ma trận, tránh quá tải đề; giữ nguyên yêu cầu và bài tập MMDS. |

Hình G4/G5 được vẽ lại một lần và dùng chung, giữ ổn định vị trí đỉnh và đúng tám cạnh. Hình 5.16 vẫn có ba vùng; không tự thêm cạnh từ vùng không thể tác động sang vùng giữa. Bảng 5.17 và bài tập 5.4.2 tiếp tục giữ hai thiết lập của nguồn ($r$ với $\beta=1$, $t$ với $\beta=4/5$). Các phân số bằng nhau do cấu trúc được giữ nguyên và phân biệt bằng nhãn, không đổi dữ kiện nguồn.


## Ghi chú và bài thực hành — 24/09/2026

Giai đoạn này dùng nguyên 51 mã trang chiếu ở trên; không thêm slide. Các mã chủ đề dưới đây áp dụng cho tài liệu tự học và thực hành. Thứ tự định nghĩa trước ví dụ là chu trình của ghi chú, không phải thay đổi chu trình trực giác trước hình thức hóa của slide.

| `note-topic-id` | Vị trí và vai trò | Kiến thức vào → sản phẩm ra | Thành phần áp dụng và kết nối |
|---|---|---|---|
| `lec04-note-01` | Mở đầu, bảng ký hiệu, §1; định hướng | PageRank Bài03 → phân biệt $P,L,S,q_S,q$ | Mục tiêu, tình huống và cầu nối; không áp dụng định lý/thuật toán riêng. Dẫn vào §2; bảng tra giúp sinh viên năm3 nhận biết ký hiệu cũ đổi vai trò. |
| `lec04-note-02` | §2; mô hình theo chủ đề | Phân phối, đồ thị → đặc tả và cài TSP | Nhu cầu→đặc tả→G4→dòng khối lượng→bất biến/co→giả mã thưa→chứng minh→chi phí→tự kiểm. Chuỗi hình học giải thích tồn tại mà không cần tiên quyết Banach. Chuyển công cụ sang §3 và §4. |
| `lec04-note-03` | §3; giải thích thao túng | Cân bằng PageRank → nghiệm chính xác và xấp xỉ | Mô hình→SVG5.16→phương trình $z,y$→suy diễn→giới hạn→tự kiểm; không có thuật toán lặp mới. Đầu ra là động lực dùng hạt giống tin cậy ở §4. |
| `lec04-note-04` | §4; tín hiệu tin cậy | Công cụ §2 và nguy cơ §3 → $t,s$ | Đặc tả→chọn hạt giống→tỷ số→Ví dụ5.12→giới hạn→tự kiểm. Dẫn lại bất biến/co §2; nhãn hai $\beta$ đứng ngay cạnh dữ kiện. Chuyển sang giới hạn của một điểm và hai vai trò HITS. |
| `lec04-note-05` | §5; hai vai trò | Ma trận kề và cộng theo cạnh → cài HITS | Vai trò→đặc tả cộng→G5 hai vòng→giả mã→điều kiện đủ/phác thảo→chi phí→tự kiểm. Giữ bảng/vết gần phép tính; chuyển sang so sánh §6. |
| `lec04-note-06` | §6 và §8; chọn mô hình | Các kết quả §2–5 → lựa chọn có điều kiện | Hai bảng ngắn và kết luận ứng dụng; không tạo chứng minh mới. Đầu ra của §6 dùng giải bài §7; §8 thu hồi ba giới hạn mở đầu và dẫn thực hành. |
| `lec04-note-07` | §7 và `exercises.md`; luyện tập | Đặc tả và vết → sản phẩm Python/giải thích | Ba đề nguồn, gợi ý và lời giải gập; phần thực hành tách đề gốc với hướng dẫn của môn, cung cấp lệnh và tiêu chí. G4 dùng xuyên ba nhiệm vụ; G5 chỉ là kiểm ví dụ HITS, không đổi đề5.5.1. |

### Bản đồ thực hành 60 phút

| Thời lượng | Nguồn / dữ kiện | Hoạt động và sản phẩm | Bố trí tài liệu và lý do |
|---|---|---|---|
| 5 phút | G4, MMDS Hình5.1/5.15 | Chuẩn bị Python3, lưu các tệp chung thư mục, đọc danh sách cạnh | Danh sách tệp→lệnh→dữ kiện; tránh để sinh viên tự đoán môi trường hoặc đường dẫn. |
| 15 phút | Bài5.3.1 tr.199/PDF25: $S=\{A\}$ và $S=\{A,C\}$, $\beta=4/5$ theo ví dụ | Chạy TSP, kiểm tổng1, đối chiếu hai nghiệm, giải thích dịch chuyển | Đề→lệnh→sản phẩm→khối gợi ý/đối chiếu gập. Hai tập được đặt nhãn riêng, giữ mọi phân số nguồn. |
| 15 phút | Bài5.4.2 tr.204/PDF30: $T=\{B\}$; baseline $\beta=1$, Trust $4/5$ | Dùng lại bộ lặp; tính/diễn giải mass âm | Bảng hai cấu hình ngay trước lệnh; tránh lẫn PageRank nền với TrustRank. Sản phẩm $t,s$ và giải thích $s_B<0$. |
| 20 phút | Bài5.5.1 tr.208/PDF34, G4 | Tự cài `hits_step`, kiểm hai vòng, chạy HITS và đối chiếu trạng thái dừng | Khung hàm→hai phép cộng→kiểm tự chạy→kết quả. Tách HITS khỏi vector xác suất; kiểm G5 được ghi rõ là kiểm chương trình theo Ví dụ5.14. |
| 5 phút | Tổng hợp ba bài | Nộp mã HITS và báo cáo ngắn, đọc tiêu chí kiểm | Checklist sản phẩm cụ thể; không dùng tốc độ trên G4 để kết luận khả năng mở rộng. |

Tổng 60 phút là hình thức thực hành của ba bài nguồn đã có, không bổ sung một recitation 60 phút nữa vào deck. Đề gốc không đổi dữ kiện hoặc yêu cầu toán học; lệnh, mã, khung hàm, dung sai và bảng sản phẩm là cách tổ chức thực hành do môn biên soạn. Chi phí dùng cùng mô hình thưa $\Theta(n+m)$ mỗi vòng; không lập ma trận tích HITS trong mã thực hành.
