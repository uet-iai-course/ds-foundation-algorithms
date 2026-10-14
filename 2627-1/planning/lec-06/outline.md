# Bài 06: Tìm cặp tương đồng bằng LSH

Bản kế hoạch viết lại ngày 28-09-2026. Phạm vi đã được người dùng xác nhận là toàn bộ kế hoạch, bộ trang chiếu và ghi chú Bài 06. Pha 1 đã được gate độc lập PASS và điều phối viên cho phép triển khai. Pha 2 đã có bản nháp HTML, ghi chú tự học và SVG; đã nhận đủ năm báo cáo độc lập và đang hoàn tất lượt editor; tái rà cùng QA cuối vẫn còn. Không dùng kế hoạch, HTML hoặc ghi chú Bài 06 cũ làm khung. Bài 05 tại commit `5530bd6` chỉ cung cấp tiên quyết, ký hiệu và dữ kiện Ví dụ 3.8.

## 1. Bài toán giảng dạy

Theo `sources/source.md`, đây là bài thứ 6 trong thứ tự đề xuất, nhận một phần buổi gốc 12. Mục tiêu cấp bài là dùng băm nhạy cảm theo tính cục bộ (LSH) để tạo tập ứng viên và phân tích đánh đổi giữa bỏ sót với ứng viên giả. Nguồn trục là *Mining of Massive Datasets*, ấn bản 3 (MMDS), Chương 3, §§3.4–3.8, tr.91–122. Giữ thứ tự khái niệm của sách; slide đối chiếu chỉ hỗ trợ việc thể hiện và kiểm chứng.

Người học là sinh viên năm 2 đã học lập trình, tập hợp, xác suất cơ bản và đại số tuyến tính. Bài 05 đã thiết lập shingle, Jaccard, chữ ký MinHash và định lý xác suất trùng của một MinHash lý tưởng. Nhắc lại nguồn ngẫu nhiên và phép nhân độc lập tại nơi sử dụng. Khoảng cách được xây trong bài trước định nghĩa họ LSH. Không giả định kiến thức cơ sở dữ liệu, hệ phân tán hoặc framework.

Vấn đề trung tâm: chữ ký đã vừa bộ nhớ nhưng số cặp vẫn là $\binom C2$. Cần tổ chức các phép thử để chỉ xác minh một tập cặp, đồng thời mô tả những cặp có thể bị bỏ sót và công việc vẫn phải thực hiện.

| Mã | Mục tiêu quan sát được | Bằng chứng học tập |
|---|---|---|
| MT1 | Lập khóa dải, dựng thùng, sinh và khử lặp cặp rồi kiểm Jaccard gốc | Vết chạy có $Q=4$, $K=3$ và kết quả $(1,4)$; câu hỏi phần 2 |
| MT2 | Suy ra xác suất tạo ứng viên; phân biệt ngưỡng, xác suất lỗi theo cặp và chi phí | Chuỗi biến cố, chọn cấu hình tại $s=0.3,0.8$; Bài 3.4.1–2 |
| MT3 | Xác định miền độ đo và đọc định nghĩa họ nhạy cảm bốn tham số | Phân biệt hướng với vector; diễn giải miền gần, giữa và xa |
| MT4 | Suy xác suất AND/OR và so thứ tự ghép trong cùng ngân sách hàm cơ sở | Ví dụ 3.19–20; Bài 3.6.1(a–d) |
| MT5 | Chạy băm tọa độ, băm dấu và phép chiếu chia khoảng; nêu điều kiện bảo đảm | Bài 3.7.1, 3.7.2, 3.7.5(a–c) |
| MT6 | Chọn biểu diễn và bước xác minh cho thực thể, vân tay, bản tin | Tính mô hình vân tay; phân biệt cùng văn bản với cùng chủ đề; Bài 3.8.2 |

Phần giảng gồm 53 trang dự kiến, 120 phút (cập nhật 2026-10-14: 69 trang giảng và 8 trang bài tập sau căn chỉnh văn phong; 70 trang giảng sau lượt sửa deck theo năm báo cáo, xem mục 5). Số trang xuất phát từ việc tách trạng thái, định nghĩa, chứng minh và kiểm tra; không phải chỉ tiêu số lượng. Recitation có 7 trang thuộc 6 cụm bài sách, 60 phút. Không có phần viết mã vì mục tiêu và nguồn không yêu cầu một chương trình trình diễn. Không tạo notebook. §3.9, HNSW, PQ và RAG nằm ngoài Bài 06; Bài 07 tiếp nhận độ đo, xác suất ứng viên và đánh đổi chi phí.

## 2. Học liệu, kiểm kê và ánh xạ nguồn

Mọi số trang PDF dưới đây đếm từ 1. Với PDF chương sách, trang in bằng trang PDF cộng 71 trong vùng được dùng. Các hồ sơ nguồn độc lập đã đọc toàn bộ văn bản §§3.4–3.8 và toàn bộ văn bản của ba bộ slide bắt buộc; phạm vi xem ảnh được ghi riêng, không suy chất lượng bố cục từ OCR.

| Mã | Tài liệu và vị trí | Phạm vi đọc, vai trò, trạng thái |
|---|---|---|
| B | Leskovec–Rajaraman–Ullman, MMDS 3e, `sources/textbooks/mmds-3e-ch03-finding-similar-items.pdf` | 63 trang PDF; §§3.4–3.8, tr.91–122/PDF 20–51; nguồn cho mọi định nghĩa, thuật toán, ví dụ và bài tập chính. Thêm Ví dụ 3.8, tr.85–86 cho dữ kiện nối Bài 05 |
| M | Slide MMDS, `sources/reference-slides/mmds/ch03-lsh.pdf`; [trang tác giả](http://www.mmds.org/) | 59 trang; đọc toàn bộ văn bản, đối chiếu kỹ PDF 14–17,24,40–59; xem ảnh PDF 45–46,54–57. Metadata tạo 11-08-2014; không coi đây là năm của sách |
| S3 | Jure Leskovec, Stanford CS246, LSH I, 13-01-2026, `sources/reference-slides/stanford-cs246/03-lsh.pdf`; [PDF chính thức](https://web.stanford.edu/class/cs246/slides/03-lsh.pdf) | 54 trang; toàn bộ văn bản, cụm PDF 34–54; ảnh PDF 39/40/48/49 ứng với số in 41/42/50/51. Nguồn đối chiếu phân dải |
| S4 | Jure Leskovec, Stanford CS246, LSH II, 15-01-2026, `sources/reference-slides/stanford-cs246/04-lsh_theory.pdf`; [PDF chính thức](https://web.stanford.edu/class/cs246/slides/04-lsh_theory.pdf) | 60 trang; toàn bộ văn bản; ảnh PDF 19,20,25,27,33,34,45,48,49,53,57,58. Số in không liên tục: PDF 19→22,48→51,49→52,57→60,58→61 |
| U | Cameron Musco, UMass Amherst COMPSCI 514, Lecture 9, Fall 2021; [PDF chính thức](https://people.cs.umass.edu/~cmusco/CS514F21/slides/lecture9/lecture9Compressed.pdf) | Đọc 16 trang; xem ảnh PDF 3,5,10–14, số in=PDF−1. Đối chiếu trường thứ hai, không là nguồn bài tập |
| D | Datar–Immorlica–Indyk–Mirrokni, SoCG 2004, *Locality-Sensitive Hashing Scheme Based on p-Stable Distributions*; [PDF tác giả](https://people.csail.mit.edu/nickle/pubs/pstable.pdf) | §3.2, PDF 3 đã đọc và xem ảnh. Chỉ nhận cơ chế dịch đều của biên lượng tử hóa; không dạy phân phối ổn định |
| P5 | Học liệu Bài 05 tại commit `5530bd6` | Chỉ đọc các đoạn ký hiệu và Ví dụ 3.8. Giữ $C,n,\mathrm{SIG},S_c,s,\widehat s$; không mượn cấu trúc |
| UI | `2627-1/lecture-template.html`, `lecture-style.css`, Lecture 02, `index.html` | Chỉ kế thừa cấu trúc, cấu hình, thành phần dùng chung; không kế thừa nội dung, metadata hoặc chỉ dẫn mẫu trong notes |

Dòng 6 của `sources/reference-slides/README.md` ánh xạ đầy đủ M, S3, S4 và yêu cầu so sánh theo cụm. Bốn PDF cốt lõi đều có cục bộ. Trang MMDS HTTP/HTTPS bị timeout trong lượt đối chiếu; `/slides.html` cũng không mở được. Bản cục bộ được dùng với giới hạn này. S3/S4 và lịch CS246 đã được đối chiếu nguồn chính thức. U là slide thật từ UMass, không phải ghi chú bài giảng. Các ảnh đọc nguồn chỉ lưu tạm, không đưa vào sản phẩm Git.

| Cụm sách | Định nghĩa, thuật toán, ví dụ, hình và bài tập đã kiểm kê | Quyết định và vị trí đích |
|---|---|---|
| §3.4, tr.91–96/PDF 20–25 | Ví dụ 3.10; phân dải; Hình 3.7/Ví dụ 3.11; bốn xác suất; Hình 3.8–3.9/Ví dụ 3.12; quy trình bảy bước; Bài 3.4.1–4 | Giữ sườn; tách vết chạy và chứng minh; kiểm gốc trực tiếp. Phần 1–2; R1. 3.4.3–4 là nhánh đọc thêm |
| §3.5, tr.96–103/PDF 25–32 | Tiên đề metric; $L_1,L_2,L_\infty$; Jaccard và chứng minh tam giác; góc; chỉnh sửa chèn/xóa và dãy con chung dài nhất; Hamming; Ví dụ 3.13–17; Bài 3.5.1–10 | Giữ đủ năm loại độ đo; không thêm thuật toán quy hoạch động. Phần 3, N05; các bài nguồn không được chọn chỉ là danh mục tự học |
| §3.6, tr.103–108/PDF 32–37 | Họ bốn tham số, MinHash, AND/OR, Ví dụ 3.18–21, Hình 3.10–12, Bài 3.6.1–4 | Giữ định nghĩa và hai chứng minh ghép; sửa nguồn xác suất. Phần 3, R2; Ví dụ 3.21 và Bài 3.6.2–4 đọc thêm |
| §3.7, tr.108–114/PDF 37–43 | Hamming; siêu phẳng; chữ ký dấu/Ví dụ 3.22; chiếu Euclid/Hình 3.13–14; mở rộng định tính; Bài 3.7.1–5 | Giữ ba họ; bổ sung dịch đều có nguồn, cận số chỉ hai chiều. Phần 4, R3–R5; 3.7.5(d) đọc thêm |
| §3.8, tr.114–122/PDF 43–51 | Thực thể, kiểm bằng trường phụ; vân tay/Ví dụ 3.23; bản tin/Ví dụ 3.24; Bài 3.8.1–5 | Giữ cơ chế cả ba ứng dụng. Phần 5, R6; mô hình ngày và Bài 3.8.1 chỉ đọc thêm |

Nguồn không cung cấp chương trình cài đặt cho các cụm được chọn. Giả mã phân dải là diễn đạt thủ tục §§3.4.1, 3.4.3; bất biến và biểu thức chi phí là suy luận của bản soạn đã được điều phối viên duyệt.

## 3. Đối chiếu slide đại học và lựa chọn

| Cụm | Quan sát có nguồn | Quyết định, lý do và giới hạn |
|---|---|---|
| Nhu cầu | B Ví dụ 3.10 tr.92; M 24; S3 PDF 10–14 nêu số cặp và các tuyên bố tốc độ; U PDF 3 phân biệt một–nhiều với mọi cặp | Dùng triệu tài liệu của sách. Tách bộ nhớ và số phép so; bỏ khẳng định tuyến tính/hằng số không có giả thiết |
| Phân dải | M 45–46 và S3 PDF 39–40 đều có ma trận dưới, thùng trên, nhiều mũi tên; hai nguồn tương đương về cơ chế nhưng không cho vết số đầy đủ | Ưu tiên MMDS. Vẽ lại dữ kiện B Hình 3.7 và chạy SIG Ví dụ 3.8; bảng thùng ghi khóa và mã tài liệu để tự tính được |
| Xác suất | M 54–56 và S3 PDF 48–49 đi theo một dải→không dải→biến cố bù; S4 PDF 34 so cấu hình cùng độ dài chữ ký | Giữ chuỗi sách; biểu đồ sau phép suy; dùng $n=100$ cho $(b,r)=(20,5),(10,10)$. Không xem diện tích tô là tỷ lệ lỗi toàn kho |
| Họ bốn tham số | S4 PDF 19/20 đặt điều kiện và miền gần–xa; ảnh PDF 19 xác nhận dấu $\le,\ge$ dù OCR đọc sai | Vẽ ba miền trên trục khoảng cách; vùng giữa để trống bảo đảm. Không áp đường chữ S cho mọi họ |
| AND/OR | S4 PDF 25/27 ghép định nghĩa, chứng minh ngắn và đánh đổi trên cùng trang; B tr.105–108 có hai thứ tự 16 phép thử | Tách sự kiện AND và OR; so hai thứ tự trên cùng bảng số. Sinh viên năm 2 dùng nhân độc lập và bù trước khi thay cận |
| Góc | S4 PDF 48/49 phân biệt pháp tuyến, siêu phẳng, hai miền góc tách; B Hình 3.13 ngắn hơn | Dùng cách tổ chức hình của Stanford, vẽ lại và thêm nét/nhãn. Chốt đẳng hướng và quy tắc dấu trước phát biểu xác suất |
| Euclid | S4 PDF 57 đặt hình chiếu dưới tam giác; PDF 58 và B tr.112 thiếu rõ điều kiện dịch biên | Giữ hình chiếu và bổ sung $\delta$ độc lập đều theo D §3.2; chứng minh cận hai chiều là suy luận bản soạn |
| Chi phí | U PDF 10–12 nối lặp/ghép với công việc; PDF 14 cộng lượng đối tượng cần xét. PDF 13 có nội dung sát/cắt mép | Học cách gắn xác suất với số ứng viên. Không lấy dữ kiện âm thanh, bố cục quá sát mép hoặc bảo đảm truy vấn ngoài phạm vi |
| Ứng dụng | M/S3/S4 không thay thế đủ ba trường hợp §3.8; S3 có RAG/tìm ảnh ở mở bài | Dùng sách cho thực thể, vân tay và bản tin. Không mở rộng bài bằng các tình huống ngoài sườn |

Mục tiêu đối chiếu gồm ba bộ slide đại học của Stanford và UMass cùng bộ MMDS bắt buộc. Uy tín nguồn không thay thế kiểm chứng mệnh đề. Phần đáng kể của MMDS được sử dụng phải ghi công bằng liên kết `http://www.mmds.org` trong tài liệu công khai. Không sao chép CSS, font, raster hoặc PDF nguồn vào đầu ra.

## 4. Bản đồ chủ đề hợp nhất và đồ thị tiên quyết

Ba đề xuất độc lập đã được điều phối viên hợp nhất trước khi soạn. Cột quyết định ghi rõ nội dung được giữ, gộp, thêm hoặc chuyển sang đọc thêm. Các mục được thêm chỉ khép khoảng trống đặc tả và chứng minh; không mở mục tiêu cấp bài.

| note-topic-id | Chủ đề; phân loại; nguồn | Vai trò, khoảng trống; đầu vào → sản phẩm | Vị trí và quan hệ; quyết định, phạm vi |
|---|---|---|---|
| N01 | Bài toán ứng viên; cốt lõi; B 3.4 tr.91–92 | SIG còn số cặp bậc hai; chữ ký → đặc tả cặp vượt ngưỡng | Mở trước N02; giữ. Gộp cầu nối MinHash của hồ sơ nguồn |
| N02 | Phân dải và thuật toán; cốt lõi; B 3.4.1,3.4.3 tr.92–96; Ex 3.8 | Khóa, thùng, khử lặp, xác minh; ma trận → tập cặp chính xác trong tập ứng viên | Sau N01, trước N03; giữ và bổ sung bất biến/biên từ thủ tục nguồn; đã duyệt |
| N03 | Xác suất, ngưỡng, sai sót; cốt lõi; B 3.4.2–3, Bài 3.4.2 | Độc lập → $P(s)$; phân biệt $t,s_{1/2},b^{-1/r}$ | Sau N02, trước N04; gộp hai mục xác suất/ngưỡng của hồ sơ đối chiếu |
| N04 | Chi phí tạo và kiểm cặp; bổ sung; suy từ B 3.4 | Nguồn chưa đếm $Q,K$; giả mã → đếm công việc/bộ nhớ và xấu nhất | Khép phân dải; thêm đã duyệt. Dùng sao chép tuple, không giả định xác minh $O(1)$ |
| N05 | Miền và độ đo; cốt lõi; B 3.5 tr.96–103 | Tập/vector/chuỗi → định nghĩa và tính năm loại; cơ sở gần–xa | Trước N06; giữ thứ tự chuẩn→Jaccard→góc→chỉnh sửa→Hamming; không thêm DP |
| N06 | Họ nhạy cảm; cốt lõi, có cầu nối; B 3.6.1–2 tr.103–105 | Khoảng cách → hai bảo đảm theo phân phối chọn hàm | Sau N05, trước N07; gộp mục nguồn ngẫu nhiên của external; sửa lượng từ |
| N07 | Phép ghép AND/OR; cốt lõi; B 3.6.3 tr.105–108 | Họ cơ sở → xác suất ghép và chi phí số hàm | Trước N08–N10, dùng lại phân dải; giữ Ex 3.19–20; OR là quyết định cặp |
| N08 | Băm tọa độ Hamming; cốt lõi; B 3.7.1 tr.109 | Tọa độ → $1-d_H/D$; lấy mẫu đều có hoàn lại | Đầu phần họ khác; giữ; cấp phép thử rời rạc đơn giản cho N09 |
| N09 | Siêu phẳng và chữ ký dấu; cốt lõi; B 3.7.2–3 tr.109–111 | Tích vô hướng/góc → dấu và xác suất; phân biệt hai phân phối pháp tuyến | Sau N08, trước N10; giữ Ex 3.22, quy tắc $\operatorname{sign}(0)=+1$ |
| N10 | Chiếu Euclid; cốt lõi và bổ sung; B 3.7.4–5 tr.111–113; D 3.2 | Chiếu/chia khoảng → va chạm; thiếu dịch biên cho cận gần | Sau N09; gộp dịch đều đã duyệt; chứng minh số chỉ hai chiều, không dạy p-stable |
| N11 | Đối sánh thực thể; cốt lõi; B 3.8.1–3 tr.114–117 | Khớp trường → ứng viên → chấm điểm và kiểm chứng | Đầu ứng dụng; giữ cơ chế, chuyển chi tiết mô hình ngày sang N15 |
| N12 | Đối sánh vân tay; cốt lõi; B 3.8.4–5 tr.117–120 | Tập ô, xác suất có điều kiện → quy tắc cơ sở và OR/AND | Sau N11; giữ mô hình 0.2/0.8, nguồn ngẫu nhiên và độc lập nêu rõ |
| N13 | Bản tin gần trùng; cốt lõi; B 3.8.6 tr.120–121 | Shingle → biểu diễn tập trung văn bản chính; phân biệt cùng chủ đề | Khép ứng dụng, trước N14; giữ token tiếng Anh nguyên nguồn, không tạo quy tắc từ dừng Việt |
| N14 | Tổng hợp và tự kiểm; cốt lõi; B 3.4–3.8 | Quy trình đã xây → lựa chọn có điều kiện, thu hồi $Q,K$ và sai số | Kết tuyến chính; giữ 6 nhiệm vụ phủ MT1–MT6 |
| N15 | Nhánh tự học; đọc thêm; B 3.4.4,3.6.2–4,3.7.5,3.8.3 | Kiến thức chính → MapReduce, phép ghép 256, phân biệt điểm bất động, mở rộng Euclid và kiểm thực thể | Sau N14; chọn giải Bài 3.7.5(d) và mô hình kiểm ngày; các mục khác chỉ là chỉ dẫn nguồn, không làm tiên quyết. Bài 3.7.5(d) có lời giải bổ sung |
| N16 | Bài tập và lời giải; cốt lõi; sáu cụm nguyên nguồn | MT1–MT6 → bảng số, biểu thức, chữ ký, thùng, so sánh lỗi | Sau tuyến chính; tách khỏi N14 để truy nguyên bài sách; 60 phút |

Đồ thị tiên quyết: Bài 05 → N01 → N02 → N03 → N04; N04 → N05 → N06 → N07; N05+N07 → N08 → N09 → N10; N02+N07 → N11 → N12 → N13 → N14; N08–N13 → N16. N15 là nhánh sau nội dung chính, không có cạnh ngược thành tiên quyết. Trong N05, góc được định nghĩa trước N09; trong N12, xác suất có điều kiện được nhắc trước phép nhân $0.2\cdot0.8$.

| Ký hiệu/thuật ngữ | Miền, ý nghĩa và quy ước |
|---|---|
| $C,n,\mathrm{SIG},V$ | Số tài liệu, độ dài chữ ký, ma trận $n\times C$; $V$ là miền giá trị thành phần chữ ký; không gọi SIG là $M$ |
| $S_c,s,\widehat s$ | Tập đặc trưng; Jaccard thật của một cặp; tỷ lệ thành phần chữ ký trùng |
| $b,r,j,i$ | Số dải, số hàng mỗi dải, chỉ số dải, chỉ số thành phần; $b,r\in\mathbb N_{>0}$, $n=br$. $r$ tại đây không là mã hàng đặc trưng của Bài 05 |
| $t,s_{1/2}$ | Ngưỡng chấp nhận Jaccard $t\in[0,1]$; nghiệm $P(s)=1/2$. $b^{-1/r}$ là xấp xỉ, không mặc nhiên bằng hai số trên |
| $\mathcal C,K,Q,u_{j,z}$ | Tập cặp ứng viên; số cặp duy nhất; tổng lượt phát cặp trước khử lặp; số phần tử trong thùng khóa $z$ của dải $j$ |
| $D,d,d_H,d_J$ | Số chiều; khoảng cách tổng quát; khoảng cách Hamming; khoảng cách Jaccard |
| $\mathcal H,h$ | Họ hàm kèm phân phối và một hàm được chọn; cùng $h$ áp dụng cho mọi đối tượng |
| $v$ | Pháp tuyến của siêu phẳng và hàm dấu; dùng cùng ký hiệu trong SVG, deck và notes |
| Tuple, $\Sigma$, $\mathbf1[E]$ | Bộ giá trị có thứ tự; tập ký hiệu; chỉ báo nhận 1 nếu E đúng, 0 nếu E sai |
| $u,\delta,a$ | Vector đơn vị đều trên mặt cầu đơn vị của $\mathbb R^D$ (Định nghĩa 06.34; Định lý 06.36 chỉ cho $D=2$), dịch biên độc lập đều trên $[0,a)$, độ rộng khoảng $a>0$ |
| $\theta$ | Góc đo radian trong $1-\theta/\pi$; $60^\circ=\pi/3$, $120^\circ=2\pi/3$; giá trị độ chỉ dùng khi ghi rõ quy đổi |
| Ứng viên giả / bỏ sót | Cặp dưới ngưỡng được sinh / cặp đạt ngưỡng không được sinh; luôn chỉ rõ tầng tạo ứng viên và mẫu số nếu dùng tỷ lệ |
| AND / OR | Phép ghép đồng thời (AND) / ít nhất một (OR); tên tiếng Việt đi trước lần đầu; OR là quan hệ cặp qua nhiều bảng |
| Khoảng cách góc | Góc trên các hướng, hay vector đơn vị; khác độ tương đồng cosin $\cos\theta$ và khác $1-\cos\theta$ |
| Băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH) | Tên chung của các bộ tạo ứng viên dùng hàm băm sao cho cặp càng giống càng dễ chung thùng; viết đầy đủ ở lần đầu mỗi tài liệu, sau đó dùng LSH. Bổ sung 2026-10-14; outline Bài 07 đang viết "băm nhạy cảm cục bộ (LSH)", cần thống nhất khi rà Bài 07 |
| Họ nhạy cảm theo tính cục bộ (locality-sensitive family) | Họ $(d_1,d_2,p_1,p_2)$-nhạy cảm, Định nghĩa 06.22 của ghi chú |
| Cặp ứng viên (candidate pair); ứng viên giả (false positive); cặp bỏ sót (false negative) | Định nghĩa 06.1 của ghi chú; thuật ngữ tiếng Anh chỉ ghi ở lần đầu |
| Độ đo khoảng cách (metric) | Hàm thỏa ba tiên đề, Định nghĩa 06.14 |
| Khoảng cách chỉnh sửa (edit distance); dãy con chung dài nhất (longest common subsequence) | Chỉ chèn và xóa; Định nghĩa 06.18, Mệnh đề 06.19 |
| Phép ghép đồng thời (AND-construction); phép ghép ít nhất một (OR-construction) | Định nghĩa 06.25; sau lần đầu được gọi tắt AND, OR |
| Pháp tuyến (normal vector); chữ ký dấu (sketch) | Định nghĩa 06.31; chữ ký dấu là dãy $m$ bit dấu, Thuật toán 06.33 |
| Điểm đặc trưng vân tay (minutia) | Vị trí đường vân kết thúc hoặc hai đường vân nhập vào nhau, MMDS §3.8.4; Mục 5.2 |
| Từ dừng (stop word) | Danh sách cho trước; Định nghĩa 06.43 |
| Phân dải (banding); dải (band); thùng (bucket); bảng băm (hash table) | Định nghĩa 06.3, Thuật toán 06.4; thuật ngữ tiếng Anh ghi ở lần đầu trong ghi chú (bổ sung 2026-10-14) |
| Siêu phẳng (hyperplane); đẳng hướng (isotropic) | Định nghĩa 06.31; thuật ngữ tiếng Anh ghi ở lần đầu (bổ sung 2026-10-14) |
| Đường chữ S (S-curve); độ tương đồng cosin (cosine similarity) | Mục 2.4 (cần $b\ge2$, $r\ge2$); Mục 3.3 (bổ sung 2026-10-14) |
| Giả thiết độc lập thêm của MMDS (vân tay) | Ví dụ 06.18, Tình huống 06.2: các biến cố va chạm qua nhiều hàm và giữa hai nhóm AND được coi là độc lập; không suy ra từ Mệnh đề 06.26; số bỏ sót của sách là cận dưới theo Jensen (bổ sung 2026-10-14) |

### Ánh xạ `note-topic-id` sang mục ghi chú (căn chỉnh 2026-10-14)

Ghi chú bài giảng được viết lại theo cấu trúc chương của `AGENTS.md`. Mỗi chủ đề mang một chú thích `<!-- note-topic-id: lec-06-topic-k -->` ngay trước tiêu đề mục tương ứng; $k$ giữ số thứ tự của mã N cũ để truy nguyên, ba chủ đề 17–19 được thêm. Số hiệu là số đã chốt trong ghi chú.

| `note-topic-id` | Mã cũ | Chủ đề; nhóm | Mục ghi chú | Số hiệu chính | Mạch deck |
|---|---|---|---|---|---|
| `lec-06-topic-18` | — | Kiến thức tiên quyết; cầu nối | Kiến thức tiên quyết | Dẫn ghi chú Bài 05, Mục 2–3, 5–7, 9, 11 | 1 (trang Tiên quyết và quy ước) |
| `lec-06-topic-01` | N01 | Bài toán tìm cặp; cốt lõi | 1 | Ví dụ 06.1; Định nghĩa 06.1; Nhận xét 06.2; Bài tập 06.1 | 1 |
| `lec-06-topic-02` | N02 | Phân dải, khử lặp, xác minh; cốt lõi | 2.1–2.2 | Ví dụ 06.2–06.3; Định nghĩa 06.3; Thuật toán 06.4; Mệnh đề 06.5; Nhận xét 06.6; Bài tập 06.2 | 2 |
| `lec-06-topic-03` | N03 | Xác suất, ngưỡng, hai loại sai số; cốt lõi | 2.3–2.4 | Ví dụ 06.4–06.5; Định lý 06.7; Hệ quả 06.8; Mệnh đề 06.9; Nhận xét 06.10; Bài tập 06.3 | 2 |
| `lec-06-topic-04` | N04 | Chi phí tạo và kiểm cặp; bổ sung | 2.5 | Ví dụ 06.6; Mệnh đề 06.11, 06.13; Nhận xét 06.12; Bài tập 06.4 | 2 |
| `lec-06-topic-05` | N05 | Độ đo khoảng cách; cốt lõi, chu trình rút gọn | 3.1–3.5 | Ví dụ 06.7–06.10; Định nghĩa 06.14, 06.16, 06.18, 06.20; Mệnh đề 06.15, 06.19; Nhận xét 06.17, 06.21; Bài tập 06.5 | 3 |
| `lec-06-topic-06` | N06 | Họ nhạy cảm theo tính cục bộ; cốt lõi | 3.6 | Định nghĩa 06.22; Hệ quả 06.23; Ví dụ 06.11; Nhận xét 06.24; Bài tập 06.6 | 3 |
| `lec-06-topic-07` | N07 | Phép ghép AND, OR; cốt lõi | 3.7 | Định nghĩa 06.25; Mệnh đề 06.26; Ví dụ 06.12; Nhận xét 06.27; Bài tập 06.7 | 3 |
| `lec-06-topic-08` | N08 | Họ chọn tọa độ; cốt lõi | 4.1 | Ví dụ 06.13; Định nghĩa 06.28; Mệnh đề 06.29; Nhận xét 06.30; Bài tập 06.8 | 4 |
| `lec-06-topic-09` | N09 | Siêu phẳng, chữ ký dấu; cốt lõi | 4.2 | Ví dụ 06.14–06.15; Định nghĩa 06.31; Định lý 06.32; Thuật toán 06.33; Bài tập 06.9 | 4 |
| `lec-06-topic-10` | N10 | Chiếu có dịch ngẫu nhiên; cốt lõi, dịch đều là bổ sung | 4.3 | Ví dụ 06.16; Định nghĩa 06.34; Bổ đề 06.35; Định lý 06.36; Nhận xét 06.37; Bài tập 06.10 | 4 |
| `lec-06-topic-17` | thêm 02/10 | Chi phí tính chữ ký ba họ; bổ sung | 4.4 | Mệnh đề 06.38; Bài tập 06.11 | 4 |
| `lec-06-topic-11` | N11 | Đối sánh thực thể; cốt lõi | 5.1 | Định nghĩa 06.39; Nhận xét 06.40; Ví dụ 06.17; Bài tập 06.12 | 5 |
| `lec-06-topic-12` | N12 | Đối sánh vân tay; cốt lõi | 5.2 | Định nghĩa 06.41; Mệnh đề 06.42; Ví dụ 06.18; Bài tập 06.13 | 5 |
| `lec-06-topic-13` | N13 | Bản tin gần trùng; cốt lõi | 5.3 | Định nghĩa 06.43; Ví dụ 06.19; Bài tập 06.14 | 5 |
| `lec-06-topic-19` | — | Tình huống áp dụng; cốt lõi | Tình huống áp dụng và ứng dụng | Tình huống 06.1–06.4 (06.1 và 06.4 giả thiết không thỏa) | 5, 6 |
| `lec-06-topic-14` | N14 | Tóm tắt chương; cốt lõi | Tóm tắt chương | Thu hồi kho một triệu tài liệu | 6 |
| `lec-06-topic-16` | N16 | Bài tập củng cố; cốt lõi | Bài tập củng cố | Bài tập 06.15–06.30; bài sách 06.20–06.26, 06.28 | 6 (06.15–06.19, 06.27), 7 (bài sách); 06.29–06.30 chỉ ở ghi chú |
| `lec-06-topic-15` | N15 | Đọc thêm; đọc thêm | Hướng dẫn đọc thêm và tài liệu tham khảo | Bài 3.7.5(d) chuyển thành Bài tập 06.26; mô hình trường ngày chuyển thành Tình huống 06.1; các chỉ dẫn đọc tiếp ở mục tham khảo | 6 (trang Nguồn và tài liệu đọc) |

## 5. Mạch giảng và chu trình theo cụm

Bảng mạch dưới đây thay bảng bảy phần cũ (5/14/13/11/6/4/7 trang, 53 + 7 trang) theo kế hoạch căn chỉnh văn phong 2026-10-14. Mạch 1 mở bằng trang bìa; mạch 2–7 mở bằng trang tiêu đề mạch `section.strand-title` theo `lecture-template.html`, mã `lec06-s0N-00`, `id="mach-N"`, nên mạch N mở tại `#/N` khi `hashOneBasedIndex: true`. Tên bảy mạch trùng từng chữ với trang "Nội dung" `lec06-s01-07`. Số trang và phút trong bảng đã được thực hiện ở giai đoạn 2 (deck sửa ngày 2026-10-14); storyboard có mục phân bổ thời gian vì phần giảng vượt 60 trang, và mục ngoại lệ mật độ. Có 34 trong 60 trang cũ đổi tiêu đề, chủ yếu thêm tiền tố "Ví dụ:", "Thuật toán:", "Tính đúng:", "Chi phí:", "Bài tập:" hoặc gọi tên theo khái niệm trung tâm; tiêu đề hiện hành của mọi `data-slide-id` nằm ở bảng ánh xạ cuối `storyboard.md`.

| Mạch | Trang mở mạch | Tên mạch | Dòng dẫn của trang tiêu đề mạch | Vai trò; kết nối vào → đầu ra | Mục ghi chú | Trang | Phút | Kiểm tra riêng |
|---|---|---|---|---|---|---:|---:|---|
| 1 | Trang bìa `lec06-s01-01` | Bài toán tìm cặp tương đồng | Không có trang tiêu đề mạch; bìa mang câu luận đề | Mở đầu: chữ ký Bài 05 → bài toán tìm cặp, vấn đề trung tâm, kho một triệu tài liệu | 1 | 8 | 10 | lec06-s01-05 |
| 2 | `lec06-s02-00` | Phân dải chữ ký MinHash | Muốn chỉ xác minh một phần nhỏ các cặp, phải gom các cột giống nhau vào cùng thùng. | Thuật toán, xác suất và chi phí: SIG → khóa dải → $\mathcal C$ → $P_{b,r}(s)$, $Q$, $K$ | 2 | 17 | 30 | lec06-s02-14 |
| 3 | `lec06-s03-00` | Khoảng cách và họ nhạy cảm | Muốn dùng phân dải ngoài Jaccard, phải có độ đo, họ băm hợp với độ đo và phép ghép tách cặp gần, cặp xa. | Mô hình: Jaccard → năm độ đo → họ $(d_1,d_2,p_1,p_2)$ → AND, OR | 3 | 14 | 28 | lec06-s03-13 |
| 4 | `lec06-s04-00` | Các họ băm theo độ đo | Muốn tìm cặp gần theo Hamming, góc hoặc Euclid, phải có họ băm mà xác suất trùng giảm theo khoảng cách. | Ba họ cơ sở, giả thiết của từng bảo đảm, chi phí chữ ký → khung của mạch 2 dùng lại | 4 | 15 | 25,5 | lec06-s04-11 |
| 5 | `lec06-s05-00` | Ứng dụng tìm cặp tương đồng | Muốn áp dụng khung tìm cặp cho hồ sơ, vân tay và bản tin, phải chọn lại biểu diễn hoặc họ hàm. | Vận dụng: đổi biểu diễn hoặc họ hàm, giữ thùng và xác minh | 5; Tình huống 06.1–06.3 | 9 | 15,5 | lec06-s05-06, lec06-s05-08 |
| 6 | `lec06-s06-00` | Tổng kết và tự kiểm tra | Muốn trả lời bài toán kho một triệu tài liệu, phải nêu giả thiết, bảo đảm và chi phí của từng kết quả. | Bảng kết quả–giả thiết, bảng thuật toán–bảo đảm–chi phí, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn | Tóm tắt chương; Tình huống 06.4 | 7 | 11 | lec06-s06-03, lec06-s06-04 |
| 7 | `lec06-s07-00` | Bài tập vận dụng | Nhu cầu: áp dụng phân dải, phép ghép, ba họ băm và mô hình vân tay vào bảy bài của MMDS Chương 3. | Bài sách, sản phẩm và lời giải | Bài tập 06.20–06.25, 06.28 | 8 | 60 | lec06-s07-07 |

Tổng 7 mạch, 70 trang giảng/120 phút và 8 trang bài tập/60 phút, 78 trang (lượt sửa deck sau năm báo cáo thêm `lec06-s04-14`, thuật toán tìm cặp với họ nhạy cảm, mạch 4 thành 15 trang, 25,5 phút). Gộp §§3.5–3.6 trong mạch 3 vì độ đo là đầu vào của họ; cụm con vẫn giữ thứ tự sách. Cụm thuật toán phân dải có đầy đủ tình huống, vấn đề, trực giác, vết chạy, hình thức hóa, giả mã/bất biến, ứng dụng/chi phí, kiểm tra. Các độ đo là khái niệm phụ nên rút gọn thuật toán/chi phí khi không có thuật toán mới; không tạo giả mã cho định nghĩa metric. Ghi chú bài giảng đánh số `## 1.`–`## 5.` ứng với mạch 1–5; mạch 6 ứng với "Tóm tắt chương" (cùng Tình huống 06.4), mạch 7 ứng với các bài sách trong "Bài tập củng cố". Chi tiết tám bước của từng cụm và câu nối nằm trong storyboard.

## 6. Ví dụ, dữ kiện và hình trực quan

Các số nguồn được giữ. Ký hiệu, nhãn đối tượng và đơn vị dùng để phân biệt vai trò; không thay số bài tập nhằm tạo khác biệt. Giá trị xác suất hiển thị thường làm tròn 6 chữ số, nhưng phép ghép tiếp dùng giá trị chưa làm tròn. Các bảng lời giải có thể giữ 9 chữ số.

| Mã | Đại lượng → ký hiệu → giá trị → kiểu/đơn vị → vai trò → nguồn | Vết chạy, thử lỗi và quyết định |
|---|---|---|
| V01 | Tài liệu $C=10^6$; chữ ký $n=250$; 4 byte/thành phần; thời gian giả định $1\,\mu s$/cặp; B Ex 3.10 tr.92 | $10^9$ byte, $499999500000$ cặp, $499999.5$ giây, $5.78703125$ ngày. Giữ số và đơn vị; phân biệt dung lượng với số cặp, không coi là benchmark |
| V02 | $S_1=\{a,d\},S_2=\{c\},S_3=\{b,d,e\},S_4=\{a,c,d\}$; $\mathrm{SIG}$ có hàng $(1,3,0,1)$ và $(0,2,0,0)$; $C=4,n=2$; B Ex 3.8 tr.85–86. Áp dụng mới $b=2,r=1,t=2/3$ theo §3.4 | Dải 1: thùng 1→1,4; thùng 3→2; thùng 0→3. Dải 2: thùng 0→1,3,4; thùng 2→2. Phát 14;13,14,34, nên $Q=4,K=3$. Jaccard 13=$1/4$,14=$2/3$,34=$1/5$; giữ 14. Giữ số, thêm nhãn dải. Lỗi không khử lặp cho 4 lần kiểm; lỗi dùng $\widehat s$ cho 14 cho 1 thay vì $2/3$ |
| V03 | $n=12,b=4,r=3$; dải đầu gồm hàng $(1,0,0,0,2),(3,2,1,2,2),(0,1,3,1,1)$; B Ex 3.11/Hình 3.7 tr.93 | Tuple cột 2=cột 4=$(0,2,1)$; cột 3=$(0,1,3)$. Giữ nguyên 3 × 5, không điền 9 hàng thiếu. Lỗi xét một hàng sẽ nhận cặp 2,3; xét đủ tuple loại cặp ấy ở dải này |
| V04 | $n=100,b=20,r=5$; $s=.3,.4,.5,.6,.8$ là Jaccard thật; B Ex 3.12 tr.94–95 | $P=.047494259,.186049552,.470050715,.801902454,.999643942$. $s_{1/2}=.508695962$, xấp xỉ=.549280272, $P$ tại xấp xỉ=.641514078. Giữ số; ghi riêng $t=.8$. Với $(b,r)=(10,10)$: $P(.3)=.000059047$, $P(.8)=.678859974$. Không hoán đổi $b,r$ |
| V05 | Điểm $x=(2,7),y=(6,4)$; độ lệch tọa độ 4 và 3; B Ex 3.13 tr.98 | $L_1=7,L_2=5,L_\infty=4$. Giữ số; 4 là độ lệch/trị cực đại có ý nghĩa toán học, phân biệt với tọa độ $y_2=4$ bằng nhãn |
| V06 | $x=(1,2,-1),y=(2,1,1)$; B Ex 3.14 tr.99 | $x\cdot y=3$, hai chuẩn $\sqrt6$, cos=$1/2$, $\theta=\pi/3=60^\circ$. Hai chuẩn bằng nhau được giữ; $1-\cos\theta=1/2$ khác góc |
| V07 | Chuỗi $abcde,acfdeg$; B Ex 3.15–16 tr.100 | $abcde\to acde\to acfde\to acfdeg$: xóa b, chèn f, g. Dãy con chung dài nhất $acde$ dài 4; $5+6-2\cdot4=3$. Giữ số; không cho phép thay thế một bước |
| V08 | Vector 10101,11110; $D=5$; B Ex 3.17 tr.101 | Khác vị trí 2,4,5; $d_H=3$; trùng 1,3 nên xác suất tọa độ=$2/5$. Giữ dữ kiện; lỗi đếm số bit 1 không cho đúng khoảng cách |
| V09 | Họ $(.2,.6,.8,.4)$, 16 phép thử, $r=b=4$; B Ex 3.19–20 tr.106–108 | AND 4→OR 4: $(.878497449,.098534519)$; OR 4→AND 4: $(.993615344,.573951942)$. Giữ số 4 lặp vì cùng ngân sách; nhãn thứ tự phân biệt cấu trúc |
| V10 | $v_1=(1,-1,1,1),v_2=(-1,1,-1,1),v_3=(1,1,-1,-1)$; $x=(3,4,5,6),y=(4,3,2,1)$; B Ex 3.22 tr.111 | Tích $x=(10,2,-4)$, $y=(4,-2,4)$; dấu $(+,+,-)$ và $(+,-,+)$; khác $2/3$, góc ước lượng $2\pi/3=120^\circ$, thật $\arccos(40/\sqrt{2580})\approx38.047579^\circ$. Giữ số; tách sai số mẫu và phân phối dấu không đẳng hướng |
| V11 | $z_1=(1,2,3),z_2=(0,2,4),z_3=(4,3,2)$ (sách: $p_1,p_2,p_3$); ba trục, $a=1,2$; B Bài 3.7.5 tr.114 | $a=1$: khóa $(1,2,3),(0,2,4),(4,3,2)$; chỉ cặp 12. $a=2$: $(0,1,1),(0,1,2),(2,1,1)$; cả 3 cặp. Giữ số; chỉ chạy trục thứ nhất với $a=1$ trên tuyến giảng để recitation chưa bị giải sẵn |
| V12 | Mô hình vân tay: ô có đặc trưng 0.2, điều kiện cùng ngón 0.8, 3 ô,1024 phép thử; B Ex 3.23 tr.118–120 | $q_F=.2^6=.000064$, $q_T=(.2\cdot.8)^3=.004096$. OR 1024: xác suất ứng viên giả=.063436634, bỏ sót=.014951892. AND hai nhóm: .004024207 và .029680224. Giữ xác suất nguồn, dùng số chưa làm tròn; không suy độc lập từ việc chọn bộ ba khác nhau |

V02 là phép áp dụng được duyệt của thuật toán lên dữ kiện sách, không phải ví dụ phân dải có sẵn trong sách. Hai hàm MinHash cố định ở V02 chỉ minh họa thực thi; phân tích V04 chuyển sang mô hình MinHash lý tưởng chọn đều độc lập. Với $r=1$, không gọi đường xác suất là chữ S.

Đặc tả hình: dùng SVG cho luồng ứng viên, hai dải và thùng, dải ba hàng, đồ thị xác suất, miền gần–giữa–xa, nhóm AND/OR, hình chuẩn vector, siêu phẳng, chiếu Euclid, khóa thực thể và lưới vân tay khái niệm. Bảng, công thức và giả mã vẫn là HTML/KaTeX. Các hình có nhãn, quan hệ, trục/đơn vị khi cần, `role="img"` và mô tả thay thế cụ thể; không dùng màu làm tín hiệu duy nhất. Với hình sinh bằng mã, lưu script tái tạo cùng tài sản pha 2. Không có ngoại lệ raster.

## 7. Mức hình thức hóa, giả mã và chi phí

| Mã | Phát biểu và giả thiết | Mức slide / ghi chú; nguồn |
|---|---|---|
| HT1 | Các tập nguồn hữu hạn không rỗng; ngưỡng $t\in[0,1]$; khóa dải đầy đủ $(j,\mathrm{SIG}_{(j-1)r+1:jr,c})$, $n=br$; cặp chuẩn hóa $c<d$ | I/O và giả mã đầy đủ; notes chứng minh khởi tạo–duy trì–kết thúc. B 3.4.1,3.4.3 |
| HT2 | Sau xác minh, đầu ra gồm đúng các cặp trong $\mathcal C$ có $\mathrm{SIM}\ge t$ | Bất biến và giới hạn trên slide; proof đầy đủ trong notes. Không bảo đảm mọi cặp thật đều vào $\mathcal C$ |
| HT3 | Với tập không rỗng, MinHash lý tưởng đều độc lập và so tuple chính xác, $P_{b,r}(s)=1-(1-s^r)^b$ | Chứng minh đầy đủ bằng độc lập và bù; B 3.4.2. $s$ thật, không thay bằng $\widehat s$ |
| HT4 | $s_{1/2}=(1-2^{-1/b})^{1/r}$ | Biến đổi đại số trên slide/notes; B Bài 3.4.2. Không đồng nhất điểm bất động |
| HT5 | Jaccard trên các tập hữu hạn không rỗng; bốn tiên đề metric; $L_q$ với $q\ge1$; $d_J=1-\mathrm{SIM}$; góc trên hướng; chỉnh sửa chèn/xóa; Hamming cùng chiều | Phát biểu/tính; notes chứng minh Jaccard, chỉnh sửa, Hamming đầy đủ; phác thảo hình học cho góc, không dạy Minkowski. B 3.5 |
| HT6 | $0\le d_1<d_2$, $0\le p_2<p_1\le1$; với cặp $x,y$ cố định, $d\le d_1\Rightarrow\Pr_{h\sim\mathcal H}[h(x)=h(y)]\ge p_1$, $d\ge d_2\Rightarrow\Pr\le p_2$ | Định nghĩa đầy đủ, vùng giữa không ràng buộc; khi tổng quát MinHash dùng $0\le d_1<d_2\le1$, họ góc dùng $0\le d_1<d_2\le\pi$; B 3.6.1, S4 PDF 19 xác minh dấu |
| HT7 | Ghép các phép thử độc lập: AND $r$ cho $p^r$; OR $b$ cho $1-(1-p)^b$ | Hai chứng minh đầy đủ ngắn; ánh xạ cận bởi tính đơn điệu; OR là quyết định cặp. B 3.6.3 |
| HT8 | Chọn chỉ số $I$ đều trong $\{1,\ldots,D\}$, $D>0$: $h_I(x)=x_I$, $\Pr[h_I(x)=h_I(y)]=1-d_H/D$ | Chứng minh đếm tọa độ; lấy có hoàn lại khi ghép; B 3.7.1 |
| HT9 | $x,y\ne0$, pháp tuyến đẳng hướng, cùng $h$, $h_v(x)=\operatorname{sign}(v\cdot x)$: xác suất $1-\theta/\pi$ | Phác thảo góc tách trên slide, proof hình học trong notes; B 3.7.2. Dấu±1 của Ex 3.22 chỉ là vết chạy khác phân phối |
| HT10 | $u$ đều hướng đơn vị hai chiều, $\delta\sim U[0,a)$ độc lập; $h=\lfloor(u\cdot x+\delta)/a\rfloor$ | Theo $u$, xác suất theo $\delta$ là $\max(0,1-\lvert u\cdot(x-y)\rvert/a)$. Cận $(a/2,2a,1/2,1/3)$ chỉ hai chiều. B 3.7.4 + cơ chế dịch D 3.2; proof là suy luận bản soạn |
| HT11 | Mô hình vân tay 0.2/0.8, chuẩn hóa và độc lập theo nguồn; chỉ ảnh chứa cả 3 ô vào thùng chung, ảnh khác nhận thùng đơn riêng | Tính cơ sở và ghép đầy đủ; B 3.8.4–5. Không là số đo thực nghiệm |

Thuật toán HT1: đã có SIG và các tập nguồn; khởi tạo từ điển thùng $B$ và tập cặp rỗng. Với từng dải $j$ và tài liệu $c$, sao chép tuple thành $z$, đặt khóa đầy đủ $k\leftarrow(j,z)$. Nếu $k$ chưa có trong $B$, tạo $B[k]\leftarrow[]$; sau đó thực hiện `B[k].append(c)`. Thao tác này tạo danh sách trước lần chèn đầu tiên và giữ nguyên danh sách khi khóa đã có. Với từng danh sách, phát mọi cặp $c<d$ vào $\mathcal C$. Với từng cặp duy nhất, tính Jaccard gốc và giữ nếu đạt $t$. Dừng sau hữu hạn dải, cột, thùng, cặp. Băm bảng phải giải va chạm bằng so khóa đầy đủ. Không duyệt mọi cặp của kho để tìm khóa trùng. Với $C<2$ hoặc thùng dưới hai phần tử, không phát cặp. Đặc tả nhận các tập hữu hạn không rỗng. Tập rỗng nằm ngoài miền của thuật toán và phân tích xác suất đang trình bày; không thêm quy ước Jaccard cho hai tập rỗng. Biến thể đang dạy bỏ bước 6 kiểm chữ ký của §3.4.3 và bắt buộc kiểm Jaccard gốc trên mọi ứng viên. Trong sách, bước 7 kiểm gốc mới được ghi là tùy chọn. Lọc theo $\widehat s$ có thể thêm bỏ sót.

Mô hình chi phí đã duyệt: chữ ký đã có; mỗi mã/tọa độ vừa một từ máy; đọc, tính và so tuple dài $r$ tốn $O(r)$; bảng băm kỳ vọng $O(1)$ sau xử lý khóa. Sao chép tuple để thống nhất hợp đồng bộ nhớ.

$$
Q=\sum_{j,z}\binom{u_{j,z}}2,\qquad K=|\mathcal C|\le Q.
$$

| Bước giả mã | Phép đếm | Chi phí và bộ nhớ |
|---|---|---|
| Đọc, tạo khóa, dựng thùng | $bC$ tuple, mỗi tuple $r$ thành phần | $O(nC)$ kỳ vọng; khóa sao chép tối đa $nC$ từ, danh sách $bC$ mã |
| Phát cặp, khử lặp | $Q$ lượt chèn cặp hai mã | $O(Q)$ kỳ vọng; lưu $K$ cặp |
| Kiểm Jaccard gốc | $K$ cặp duy nhất | $\sum_{(c,d)\in\mathcal C}T_J(c,d)$; với tập đã sắp xếp, $T_J=O(\lvert S_c\rvert+\lvert S_d\rvert)$ |
| Tổng | V02:8 lượt chèn,4 lượt phát,3 lần kiểm | $O(nC+Q+\sum T_J)$ kỳ vọng; bộ nhớ phụ $O(nC+K)$, ngoài SIG đầu vào $nC$ từ |

Xấu nhất $Q=b\binom C2$, $K=\binom C2$; không có bảo đảm dưới bậc hai vô điều kiện. Trong notes có thể suy $\mathbb E[K]=\sum_{c<d}P(s_{cd})$, $\mathbb E[Q]=b\sum_{c<d}s_{cd}^r$ bằng tuyến tính kỳ vọng; không cần độc lập giữa các cặp. Phần giảng không tăng thêm công thức kỳ vọng nếu làm loãng mô hình đếm thực tế.

## 8. Tổng hợp dàn bài, bài tập và điều kiện triển khai

Phiếu từng trang, ánh xạ note-topic, chu trình cụm, nội dung công khai dự kiến, lời giải, bố cục và phút nằm trong `storyboard.md`. Ghi chú được soạn độc lập theo thứ tự vai trò → định nghĩa → ví dụ → trực quan → mệnh đề/thuật toán/chứng minh → ứng dụng/lỗi/tự kiểm. Không sao chép mặt slide hay notes diễn giả thành tài liệu tự học.

| Cụm recitation | Bài sách nguyên nguồn | Phạm vi và sản phẩm | Phút |
|---|---|---|---:|
| R1 | 3.4.1 và 3.4.2, tr.96/PDF 25 | Ba cấu hình, chín $s$; bảng 27 xác suất,3 ngưỡng chính xác và 3 xấp xỉ | 18 |
| R2 | 3.6.1(a–d), tr.108/PDF 37 | Giữ bốn chuỗi; biểu thức xác suất và trạng thái trung gian | 10 |
| R3 | 3.7.1, tr.113/PDF 42 | Bốn vector, sáu hàm tọa độ; hàm tạo ứng viên cho từng cặp | 6 |
| R4 | 3.7.2, tr.113–114/PDF 42–43 | Ba vector, bốn pháp tuyến; chữ ký, góc ước lượng và góc thật | 10 |
| R5 | 3.7.5(a–c), tr.114/PDF 43 | Ba điểm, ba trục, rộng 1 và 2; bảng thùng/cặp. Chuyển (d) sang đọc thêm | 8 |
| R6 | 3.8.2(a, b), tr.121/PDF 50 | OR 2048 so AND hai nhóm OR 1024; hai xác suất lỗi | 8 |

Cập nhật 2026-10-14: phần bài tập có 8 trang, gồm trang tiêu đề mạch `lec06-s07-00` và bảy trang đề `lec06-s07-01`…`07` mang tiêu đề "Bài tập: …"; mỗi trang đề giữ một dòng nguồn số bài sách; lời giải là Bài tập 06.20–06.25 và 06.28 của ghi chú. Máy tính chỉ hỗ trợ lũy thừa/arccos. Dịch đề, chia R1 thành hai trang, lược 3.7.5(d) khỏi recitation; không đổi dữ kiện hoặc yêu cầu toán học. Phút thuộc storyboard và ghi chú học tập theo yêu cầu recitation, không hiển thị trên mặt trang. Lời giải không chứa hướng dẫn giảng viên hay mã nội bộ.

Pha 2 dùng `.reveal.course-deck.lecture-lsh`, CSS chung, mẫu trang tiêu đề/mục lục/`example-slide`/`cost-slide`; không sao chép khối style mẫu. Giữ `lang="vi"`, 1280 × 720, controls ở mép, slideNumber, hashOneBasedIndex và hash; thư viện Reveal, notes, highlight, KaTeX cục bộ. Không có `fragment`. Mọi hình kỹ thuật vẽ SVG, đường dẫn tương đối. Ghi chú bắt đầu H1, dùng `$...$`/`$$...$$`, khối tự học không lồng, hint/solution gập mặc định và mở khi in.

Quill được áp dụng ở mức Outline/Revise để kiểm thứ tự và liên tục; không khởi tạo `quill.json`. No-ai-slop Edit được áp dụng cho tiêu đề, câu chốt, nội dung dự kiến và diễn giải notes; tự kiểm theo `eval.md`. Kết quả và sai khác nguồn được ghi bền vững trong `review-log.md`. Pha 1 chưa xác nhận hiển thị, đủ năm reviewer, kiểm viewer, commit hoặc phát hành.

## 9. Hoàn thiện sau năm lượt rà độc lập

Điều phối viên nhận toàn bộ phát hiện của năm vai; editor gộp điểm trùng và sửa cục bộ, giữ 60 trang/7 phần/120+60 phút. Trang s01-02 “Nội dung và mục tiêu” hiển thị ba năng lực: lập và xác minh ứng viên (MT1/MT6); suy xác suất, phân tích chi phí và tham số (MT2/MT4); chọn phép thử theo độ đo và giả thiết (MT3/MT5). Sáu nhiệm vụ kết bài kiểm lại các năng lực này.

- Giữ trật tự ví dụ trước hình thức trên deck. Thêm quan hệ d_J=Pr[khác MinHash] và ví dụ cặp (1,4) trước chứng minh tam giác. Với góc, nêu quy tắc ước lượng và căn cứ mô hình đẳng hướng trước phép đổi tỷ lệ; chứng minh hình học vẫn ở trang sau.
- Bổ sung hình chiếu hai chiều có rho, ell, phi và chuỗi điều kiện cần cho cận xa. Hình mới hinh-chieu-euclid.svg do generator tạo; tổng tài sản SVG hiện tại là 12.
- Khôi phục kết nối Jaccard → độ đo trên vector/chuỗi → họ có phân phối và hai cận. Tính metric không tự bảo đảm tồn tại một họ LSH.
- Thu hồi chỉnh sửa chuỗi ở điểm phạt thực thể; giải nghĩa đặc trưng vân tay; mô tả truy hồi hợp–hợp–giao–xác minh; định nghĩa từ dừng và danh sách năm từ nguồn trước vết shingle.
- Tự kiểm N01–N13 được thực hiện tại chủ đề bằng khối gập hoặc liên kết rõ đến bài nguồn. Giữ tự kiểm N14, phạm vi đọc thêm N15 và sáu cụm recitation N16; không thêm dữ kiện recitation.
- N15: độ trễ là ngày tạo B trừ ngày tạo A, lọc 0–90 ngày. Trung bình ngẫu nhiên 45 dùng giả thiết đủ là độ trễ đều; đây là phần làm rõ mô hình đã được điều phối duyệt. Nhóm điểm tối đa 300 được giả định khớp đúng và có trung bình 10 ngày. Công thức hỗn hợp giữ nguyên.

Mục tiêu mở đầu thay đổi đòi tái rà mạch toàn tuyến. Bất biến, nhận diện khoảng cách–xác suất, quy tắc góc, hình học Euclid và giả thiết mô hình ngày cần tái rà toán. Cầu nối hình thức hóa cần tái rà học thuật. Không coi tự kiểm editor hoặc snapshot render trước sửa là PASS cuối.

## Duyệt từng trang ngày 02/10/2026

Lượt duyệt theo yêu cầu người dùng: với mỗi trang, xác định trang muốn nói gì, đề xuất rồi sửa để tiêu đề ngắn gọn, học thuật, lập luận chặt và khái niệm không xuất hiện đột ngột; sau mỗi trang sửa mục tương ứng của ghi chú tự học, commit và push. Chi tiết từng trang và các lượt rà lại theo phần nằm trong `review-log.md`, mục cùng tên.

- **Cấu trúc.** Deck giữ 60 trang (53 giảng, 7 bài tập), bảy phần 5/14/13/11/6/4/7. Hai thay đổi thứ tự: s02-06 (ví dụ trùng dải) đặt ngay sau s02-01 để trực giác có ví dụ trước đặc tả; s04-05 (xác suất cùng phía siêu phẳng) đặt trước s04-04 (chữ ký dấu) vì quy tắc ước lượng góc dùng kết quả $p_{\ne}=\theta/\pi$, khớp thứ tự MMDS §3.7.2 rồi §3.7.3. Thời lượng không đổi.
- **Câu nối mới.** Bài toán tìm cặp có đầu vào/đầu ra (s01-04); định nghĩa ứng viên giả trước khi đếm (s02-01, s02-05); quy tắc chọn ngưỡng §3.4.3 (s02-12); nhu cầu khuếch đại độ chênh $p_1-p_2$ (s03-09); $F(s)=P_{4,4}(s)$ nối phép ghép với đường cong S (s03-12); bộ tham số nhạy cảm của cả ba họ theo độ đo (s04-02, s04-05, s04-09); lý do cần độ lớn và phép dịch (s04-06, s04-07); OR của ba khóa trong đối sánh thực thể (s05-01); lý do không dùng MinHash cho vân tay (s05-02); bài toán bản tin trước định nghĩa từ dừng (s05-05); ba bước quy trình gắn với kết quả từng phần và hai loại sai số (s06-01, s06-02).
- **Câu hỏi kiểm tra.** Các trang s01-05, s02-14, s03-13, s04-11, s05-06, s06-03, s06-04 thay câu có đáp án trên mặt trang trước bằng câu vận dụng với dữ kiện mới; đáp án đã tính lại bằng chương trình.
- **Ký hiệu.** Số thập phân dùng dấu phẩy trên deck và ghi chú, bộ tham số thập phân dùng dấu chấm phẩy; không còn chữ Việt trong `\text` của KaTeX; ba điểm của Bài 3.7.5 đổi $p_i\to z_i$ để không trùng hai cận $p_1,p_2$ (dữ kiện V11 ở bảng trên đã cập nhật); “khoảng cách” chỉ dùng cho độ đo, hiệu hai cận gọi là “độ chênh”.
- **Tiêu đề.** 43 trong 59 tiêu đề `h2` đổi theo khái niệm hoặc kết quả trung tâm.
- **Bài tập.** Dữ kiện và yêu cầu của sáu cụm recitation giữ nguyên; ghi chú diễn giả bỏ dòng thời lượng (thời lượng chỉ còn trong storyboard).
- **Ghi chú tự học.** Mọi mục được cập nhật theo các câu nối mới; thêm mục “Chi phí tính chữ ký của ba họ”; mục siêu phẳng sắp lại theo thứ tự định nghĩa → xác suất → chữ ký → ví dụ; các bài tự kiểm có đáp án trong đoạn ngay trước được thay bằng dữ kiện mới.
