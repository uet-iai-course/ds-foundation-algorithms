# Dàn ý Bài 05 — Biểu diễn tương đồng: Shingling và MinHash

Bản viết mới ngày 28-09-2026. Ba tệp quy trình được thay toàn bộ theo yêu cầu của người dùng; dàn ý cũ không được dùng làm khuôn. Trạng thái: cửa kiểm kế hoạch đã PASS và được điều phối viên chấp nhận; bản nháp HTML, ghi chú và SVG đã được triển khai để kiểm định độc lập. Chưa xác nhận bản dựng đạt cửa kiểm cuối.

## 1. Bài toán giảng dạy

**Vấn đề trung tâm:** với một kho tài liệu có các phiên bản gần trùng, cần chọn biểu diễn tương đồng văn bản và tạo chữ ký nhỏ để ước lượng độ tương đồng của một cặp. Hai giới hạn được tách rõ: tập đặc trưng tốn bộ nhớ; việc xét mọi cặp có số phép so sánh bậc hai. Bài 05 giải quyết biểu diễn và chi phí so sánh mỗi cặp; bước tạo tập ứng viên thuộc Bài 06.

Bài 05 theo bảng thứ tự đề xuất trong `sources/source.md`, ánh xạ từ buổi gốc 3 và một phần buổi 12. Trục là MMDS 3e Chương 3, §§3.1–3.3. Người học là sinh viên năm 2; đã học lập trình, tập hợp, vector, băm và xác suất cơ bản. Mặc định năm 3 của skill outline được thay bằng đối tượng năm 2 theo chỉ dẫn học phần. Không giả định kiến thức về cơ sở dữ liệu, hệ phân tán, LSH hoặc mô hình nhúng.

| Mục tiêu | Sản phẩm học tập | Kiểm tra trực tiếp |
|---|---|---|
| MT1 | Tính Jaccard và xác định đối tượng được biểu diễn bằng tập | 09, 51, 53, 57 |
| MT2 | Tạo tập shingle, phân biệt độ dài shingle với kích thước mã băm | 18, 49, 52 |
| MT3 | Lập ma trận đặc trưng, chạy MinHash và chứng minh xác suất trùng bằng Jaccard | 27, 49, 50, 53, 54, 56, 57 |
| MT4 | Tính tỷ lệ tọa độ trùng; phân biệt một ước lượng với kỳ vọng và phương sai | 34, 46, 50, 57 |
| MT5 | Truy vết thuật toán quét hàng, giải thích bất biến, đếm thời gian và bộ nhớ | 46, 50, 55, 56, 57 |

48 trang phần giảng gồm cả mở đầu và kiểm tra, tổng 120 phút (từ 01/10/2026; trước đó 50 trang, trang 17 gộp vào 19 và trang 21 gộp vào 20); 7 trang bài tập cho 5 bài nguồn, tổng 60 phút; deck có 55 trang. Số trang cho phép giữ ví dụ, chứng minh và vết cập nhật ở cỡ chữ chung, không dùng trang trang trí. Không có phần cài môi trường hoặc notebook vì phạm vi nguồn không yêu cầu. Tăng tốc ở §§3.3.6–3.3.7 chỉ thuộc ghi chú đọc thêm, ngoài 120 phút.

**Cập nhật 2026-10-14 (sửa toàn diện theo chuẩn trình bày).** Deck có 65 trang: 57 trang giảng (120 phút) và 8 trang bài tập (60 phút). Câu luận đề trên trang bìa: "Với hoán vị chọn đều, hai tập trùng MinHash với xác suất bằng Jaccard; chữ ký ngắn nhờ đó ước lượng được Jaccard." Trang "Mục tiêu học tập" (`lec05-s01-03`) hiển thị năm mục tiêu quan sát được, ánh xạ vào bảng trên như sau; mã MT chỉ dùng trong hồ sơ, không trên mặt trang hay trong ghi chú diễn giả.

| Mục tiêu hiển thị | MT | Kiểm tra trực tiếp (mã trang) |
|---|---|---|
| 1. Tạo tập shingle của một chuỗi và tính Jaccard của hai tập | MT1, MT2 | `lec05-s01-09`, `lec05-s02-09`, `lec05-s07-01`, `lec05-s07-02` |
| 2. Chứng minh hai tập trùng MinHash với xác suất bằng Jaccard | MT3 | `lec05-s03-09`, `lec05-s07-03`, `lec05-s07-04` |
| 3. Ước lượng Jaccard từ chữ ký; tính kỳ vọng và phương sai của ước lượng | MT4 | `lec05-s04-07`, `lec05-s06-03`, `lec05-s06-04`, `lec05-s07-07` |
| 4. Chạy phép quét hàng, nêu bất biến, đếm thời gian và bộ nhớ | MT5 | `lec05-s05-12`, `lec05-s07-05`, `lec05-s07-06` |
| 5. Xác định thừa số chi phí chữ ký giảm được và thừa số còn bậc hai | MT5 (thu hồi) | `lec05-s06-04` câu 6 |

## 2. Phân tích học liệu và kiểm kê nguồn

Quy ước trích dẫn: `B` là sách; số trang là trang in, trang PDF bằng trang in trừ 71. `MM`, `ST03`, `ST04`, `CM`, `UM` dùng số trang PDF. Các tệp tạm phục vụ kiểm chứng không phải học liệu phát hành.

| Mã | Nguồn và đường dẫn | Phạm vi đã kiểm tra và vai trò |
|---|---|---|
| B | Leskovec, Rajaraman, Ullman, *Mining of Massive Datasets*, ấn bản 3; `sources/textbooks/mmds-3e-ch03-finding-similar-items.pdf` | Tr.73–91, §§3.1–3.3; nguồn trục, dữ liệu, hình và bài tập |
| MM | Slide chính thức MMDS, `sources/reference-slides/mmds/ch03-lsh.pdf`; [trang tác giả](http://www.mmds.org) | Kiểm kê cả 59 trang; cụm 14–39 đối chiếu Bài 05, 40–59 thuộc Bài 06 |
| ST03 | Stanford CS246, Jure Leskovec, 13-01-2026, `sources/reference-slides/stanford-cs246/03-lsh.pdf`; [bản chính thức](https://web.stanford.edu/class/cs246/slides/03-lsh.pdf) | Kiểm kê 54 trang; trọng tâm 14–33; phân biệt giá trị hàng với hạng ở tr. 28 |
| ST04 | Stanford CS246, Jure Leskovec, 15-01-2026, `sources/reference-slides/stanford-cs246/04-lsh_theory.pdf`; [bản chính thức](https://web.stanford.edu/class/cs246/slides/04-lsh_theory.pdf) | Kiểm kê 60 trang; 3–7 ôn Bài 05, 8–60 là ranh giới bài sau |
| CM | CMU 15-853, Spring 2013, *Algorithms in the Real World*, 31 trang; [PDF chính thức](https://www.cs.cmu.edu/afs/cs/project/pscico-guyb/realworld/www/slidesS13/minhash.pdf) | Đối chiếu tr. 9–20; xem trực tiếp 14, 16, 19, 20; không đưa ví dụ ngoài sách vào tuyến chính |
| UM | Cameron Musco, UMass Amherst COMPSCI 514, Fall 2021, Lecture 9; [PDF chính thức](https://people.cs.umass.edu/~cmusco/CS514F21/slides/lecture9/lecture9Compressed.pdf) | Đối chiếu toàn bộ 16 trang; xem trực tiếp 6–8; học quan hệ phần tử cực tiểu với giao |

Ba PDF cục bộ trong dòng Bài 05 của `sources/reference-slides/README.md` đã được tác tử nguồn mở và kiểm kê toàn bộ. Các báo cáo độc lập `/tmp/lec05-rebuild/source-dossier.md`, `external-dossier.md`, `planner.md` đã được điều phối viên chấp nhận trước khi soạn. Bản thân writer đọc các hồ sơ này và các trang sách liên quan; không nhận thay việc xem ảnh của tác tử khác. Trang chủ MMDS bị timeout trong lượt kiểm tra trực tuyến; PDF chính thức cục bộ đủ để đối chiếu. Ghi công MMDS bằng liên kết trên vẫn là yêu cầu khi phát hành.

| Thành phần học thuật | Nguồn | Quyết định và vị trí |
|---|---|---|
| Bài toán gần trùng, phép đếm cặp | B tr. 73–76; Ví dụ 3.10 tr. 92 (giả định một micro giây mỗi cặp, chữ ký 1.000 byte, 1 GB) | Giữ, 04–05; thu hồi tại 33, 47–48; hai bản tin ở 04 là ví dụ dựng |
| Jaccard, Hình 3.1 | B §3.1.1 tr. 74–75 | Giữ và vẽ lại SVG, 07–09 (06 gộp vào 07 ngày 07/10/2026) |
| Shingle, Ví dụ 3.3–3.4 | B §3.2.1 tr. 78 | Giữ chuỗi nguồn, 10–15; thuật toán hóa định nghĩa có ghi rõ |
| Chọn độ dài và mã hóa shingle | B §§3.2.2–3.2.3 tr. 79–80 | Giữ mức quy tắc kinh nghiệm, 14,16–18 |
| Ma trận và hoán vị, Hình 3.2–3.3 | B §§3.3.1–3.3.2 tr. 81–83 | Giữ cùng 5 hàng, 4 tập; 20–24 |
| Chứng minh xác suất | B §3.3.3 tr. 83 | Chứng minh đầy đủ, 25–27; không thay bằng kiểm thử hữu hạn |
| Chữ ký, kỳ vọng | B §3.3.4 tr. 83–84 | Giữ, sửa đơn vị kỳ vọng; 28–34 |
| Phương sai ước lượng | Suy ra từ B §§3.3.3–3.3.4 và xác suất tiên quyết | Thêm đã duyệt; 32, ghi chú n05-08 |
| Quét hàng, Hình 3.4 | B §3.3.5 tr. 84–86; Hình 3.4 tr. 85; Ví dụ 3.8 tr. 85–86 | Giữ đầy đủ, 35–46; bổ sung bất biến và đếm chi phí |
| Đa tập; shingle theo từ dừng | B §3.1.3, §3.2.4 | Đọc thêm trong ghi chú; không là tiên quyết của tuyến chính |
| Tăng tốc, Hình 3.5 | B §§3.3.6–3.3.7 tr. 86–90 | Đọc thêm có điều kiện ngẫu nhiên và xử lý giá trị thiếu |
| Bài tập | B 3.1.1, 3.2.3, 3.3.1(a, b), 3.3.2(a, b), 3.3.3(a, b, c) | Giữ đề và dữ kiện; dịch, chuẩn hóa ký hiệu, tách 7 trang |
| LSH, khoảng cách và ANN | B §3.4 trở đi; MM40–59; ST03 34–54; ST04 8–60 | Chuyển Bài 06–07, chỉ nêu nhu cầu tạo ứng viên ở kết luận |

Không có mã nguồn cần chuyển. Giả mã tạo shingle được suy ra từ định nghĩa, không phải mã trích giáo trình; giả mã quét chữ ký là đặc tả lại §3.3.5. Hình kỹ thuật được vẽ SVG; bảng ma trận, công thức và giả mã dựng bằng HTML/KaTeX. Không mang ảnh raster, CSS, phông chữ hoặc PDF của các nguồn vào đầu ra Git.

## 3. Đối chiếu slide đại học

| Cụm | Bằng chứng đối chiếu | Quyết định đã duyệt |
|---|---|---|
| Động lực | MM15, 24; ST03 14; CM 9 | Giữ tình huống sách/MMDS; số cặp và kích thước mỗi biểu diễn là hai đại lượng riêng |
| Shingling | MM19–23; ST03 18–20 | Hai slide tương đương; ưu tiên MMDS, dùng chuỗi `abcdabd` của sách để liên tục nguồn |
| Jaccard, ma trận | MM14, 22,26–27; ST03 20–21; CM 12–14 | Giữ Hình 3.1–3.2 sách; không trộn ma trận 7 hàng ở slide tham khảo |
| Hoán vị | MM32–33; ST03 26–28 | Giữ sách; dùng cảnh báo ST03 28 để tách định danh, hạng và giá trị băm |
| Chứng minh | MM34–35; ST03 29–30; UM 6–8 | Giữ phân loại X/Y/Z của sách, nối với phần tử đầu trong hợp; không lặp hai chứng minh độc lập |
| Chữ ký | MM36–38; ST03 31–32 | Bảng tỷ lệ trùng đặt sau ví dụ cụ thể; loại lời khẳng định bảo toàn chính xác ở từng lần chạy |
| Quét hàng | MM39; ST03 33; CM 19–20 | Đặc tả lấy từ sách; giữ dữ liệu và trạng thái đồng thời như CMU, tách vết chạy khỏi giả mã |
| Trình tự khác | UM 3–5 đặt LSH trước MinHash | Không dùng vì khác tiên quyết của học phần; giữ Jaccard → shingle → MinHash |

Các nhận xét bố cục dựa trên ảnh đã xem trong hồ sơ đối chiếu: ST03 27, 28, 32, 33; CM 14, 16, 19, 20; UM 6, 7, 8; MM35. Các kết luận sư phạm là quyết định biên tập, không phải mệnh đề của nguồn. Học nguyên tắc một luận điểm, hình đủ lớn, chú thích nêu kết quả từ kho tham khảo `uet-iai-course/machine-learning`; không sao chép nội dung hay giao diện.

## 4. Khái niệm, thuật ngữ và tiên quyết

| Khái niệm | Vai trò | Đầu vào → đầu ra | Điểm dễ nhầm |
|---|---|---|---|
| Tương đồng tập hợp | Trọng tâm | Giao/hợp → đại lượng cần ước lượng | Mẫu số là hợp, không phải tổng kích thước |
| Shingling | Trọng tâm | Chuỗi → tập đoạn con liên tiếp | Số cửa sổ khác số phần tử phân biệt |
| Ma trận đặc trưng | Cầu nối | Tập → cấu trúc hàng/cột | Hàng là phần tử, cột là tập |
| MinHash một thành phần | Trọng tâm | Tập và thứ tự chung → định danh phần tử đầu | định danh khác vị trí và khác giá trị băm |
| Định lý MinHash | Trọng tâm | Hoán vị đều → xác suất trùng | Một ví dụ trùng không chứng minh xác suất |
| Chữ ký và ước lượng | Trọng tâm | Nhiều phép thử → tỷ lệ tọa độ trùng | Không lấy Jaccard giữa tập các giá trị chữ ký |
| Băm hàng và phép min | Trọng tâm | Ma trận, hàm băm → chữ ký tính được | Băm hữu hạn không tự thỏa mô hình hoán vị đều |
| Bất biến và chi phí | Bổ sung cần thiết | Vòng lặp → tính đúng và phép đếm | Không bỏ khởi tạo; phép min không đồng nghĩa ô giảm |

Đồ thị tiên quyết: tập hợp → Jaccard → shingle → ma trận đặc trưng → thứ tự chung → MinHash → định lý → chữ ký → kỳ vọng/phương sai → quét hàng → chi phí/giới hạn. Băm shingle xuất hiện sau độ dài shingle; băm hàng chỉ xuất hiện sau định lý lý tưởng. Định nghĩa tập rỗng được xử lý ngay khi tạo shingle; định lý chính luôn giới hạn tập không rỗng.

| Ký hiệu | Nghĩa, miền và quy ước |
|---|---|
| $D,\ell$ | Chuỗi tài liệu và độ dài; ghi rõ ký tự hoặc byte theo dữ kiện nguồn |
| $k, S_k(D)$ | $k\ge1$ là độ dài shingle; tập các đoạn con liên tiếp dài $k$ |
| $U, R$ | Vũ trụ hữu hạn; $R=\lvert U\rvert$ là số hàng |
| $C, S_c$ | $C$ tập/tài liệu; $1\le c\le C$ |
| $M(r, c)$ | Ma trận đặc trưng $R\times C$; bằng 1 khi phần tử hàng $r$ thuộc $S_c$ |
| $\pi,\operatorname{rank}_\pi(u)$ | Thứ tự trên $U$ và vị trí $1,\ldots, R$ của phần tử $u$ |
| $h_\pi(S)$ | định danh phần tử đầu tiên của tập không rỗng $S$ trong thứ tự $\pi$ |
| $n,\sigma(S)$ | Độ dài chữ ký và vector gồm $n$ giá trị MinHash |
| $\mathrm{SIM}(S, T), s$ | Jaccard thật; $s$ rút gọn cho một cặp cố định |
| $X_i,\widehat{\mathrm{SIM}}$ | Biến chỉ báo trùng ở tọa độ $i$ và tỷ lệ tọa độ trùng |
| $f_i,\mathrm{SIG}(i,c)$ | $i=1,\ldots,n$; $f_i:\{0,\ldots,R-1\}\to V$, với $V$ hữu hạn có thứ tự toàn phần. Chữ ký là cực tiểu trên giá trị của cột hợp với $\{+\infty\}$; cột rỗng trả $+\infty$ |
| $B_1,B_2,m_{B_j}(u)$ | Hai đa tập hữu hạn và số bội; chỉ ở n05-12, tổng số bội của hai đa tập dương |
| $L=\operatorname{nnz}(M)$ | Tổng số ô 1; dùng trong phép đếm chi phí |

Quy ước các hàng $a, b, c, d, e$ tương ứng mã $0,1,2,3,4$ được khai báo ở trang 37. Đây là đổi nhãn đã công khai; không viết ngầm $a=1$. Chữ ký lý tưởng lưu định danh; chữ ký thực hành lưu giá trị băm. Khi một hàm là song ánh, hai cách lưu cho cùng quan hệ bằng nhau nhưng không cùng giá trị số.

**Thuật ngữ Việt–Anh (bổ sung 2026-10-14, thống nhất với Bài 06).** Thuật ngữ tiếng Anh đặt trong ngoặc ở lần xuất hiện đầu trên mặt trang.

| Thuật ngữ | Tiếng Anh | Lần đầu trên mặt trang |
|---|---|---|
| độ tương đồng Jaccard | Jaccard similarity (tên riêng, giữ "Jaccard") | `lec05-s01-07` |
| shingle | shingle (giữ tiếng Anh, chưa có bản dịch ổn định) | `lec05-s02-01` |
| va chạm | collision | `lec05-s02-07` |
| ma trận đặc trưng | characteristic matrix | `lec05-s03-02` |
| hoán vị | permutation | `lec05-s03-04` |
| chữ ký MinHash | MinHash signature | `lec05-s04-02` |
| ma trận chữ ký | signature matrix | `lec05-s05-02` |
| băm nhạy cảm theo tính cục bộ | locality-sensitive hashing, LSH | `lec05-s06-07` |
| từ dừng | stop word | chỉ trong ghi chú bài giảng |

Bảng ký hiệu trên không đổi trong đợt sửa 2026-10-14.

## 5. Mạch giảng và bản đồ bảy phần

| Phần | Loại, sản phẩm và kết nối | Trang | Phút | Kiểm tra |
|---|---|---|---:|---|
| 1. Tài liệu gần trùng và độ tương đồng Jaccard | Giới thiệu + khái niệm; kho gần trùng → Jaccard cần một biểu diễn tập | 01–09 | 18 | 09 |
| 2. Shingling văn bản | Khái niệm + thuật toán; chuỗi → tập phần tử để nén | 10–16, 18 | 21 | 18 |
| 3. MinHash theo hoán vị | Khái niệm + chứng minh; tập → một phép thử có xác suất trùng bằng Jaccard | 19–20, 22–27 | 23 | 27 |
| 4. Chữ ký MinHash | Ước lượng; một phép thử → tỷ lệ nhiều phép thử và tác dụng của $n$ | 28–34 | 17 | 34 |
| 5. Tính chữ ký bằng hàm băm | Thuật toán + chi phí; băm hàng → chữ ký tính được, bất biến và giới hạn | 35–46 | 31 | 46 |
| 6. Tổng kết và tự kiểm tra | Thu hồi tình huống; kết nối biểu diễn, bảo đảm và giới hạn số cặp | 47–50 | 10 | 49–50 |
| 7. Bài tập vận dụng | 5 bài nguồn, riêng sau phần giảng | 51–57 | 60 | 56–57, Bài 3.3.3 |

Mỗi phần tương ứng một `section` ngoài. Từ 14/10/2026, phần 2–7 mở bằng trang tiêu đề mạch `lec05-s02-00` … `lec05-s07-00` (`class="strand-title"`, `id="mach-N"`), tên trùng từng chữ với cột Phần; phần 6 đổi tên từ "Tổng kết" thành "Tổng kết và tự kiểm tra" theo `AGENTS.md`. Cột Trang giữ số phiếu cũ; deck 60 trang. Phần bài tập có 7 trang nhưng chỉ 5 bài; việc tách Bài 3.3.1 và 3.3.3 không nhân thời lượng. Không có phần đọc thêm trên mặt deck; ghi chú tự học đánh dấu nhánh đọc thêm riêng.

| Cụm trọng tâm | Tám bước học tập và trang thực hiện | Dữ liệu được truyền và quyết định gộp |
|---|---|---|
| Jaccard | Tình huống 04; vấn đề 05; trực giác/ví dụ 06; hình thức 07; ứng dụng 08; kiểm tra 09 | Giao 3, hợp 8 truyền từ hình sang công thức. Không có thuật toán riêng vì phép đếm tập là tiên quyết; chi phí mọi cặp đặt ở 05 |
| Shingling | Tình huống/vấn đề/trực giác 10; ví dụ 11; hình thức 12; thuật toán và đúng 13; ứng dụng/chi phí 14–16 (17 gộp vào 19); kiểm tra 18 | `abcdabd`, $k=2$, sáu cửa sổ, năm phần tử giữ nguyên. 13 gộp bất biến ngắn; chứng minh đầy đủ vào ghi chú |
| MinHash | Tình huống/vấn đề 19; biểu diễn 20 (21 gộp vào 20); trực giác 22; ví dụ 23; hình thức 24; lập luận đúng 25–26; kiểm tra 27 | Cùng bốn tập Hình 3.2; thứ tự `b, e, a, d, c`. Chi phí lưu hoán vị chuyển 35 vì chỉ khi đó cần triển khai; 19 đã đặt giới hạn bộ nhớ |
| Chữ ký | Nhu cầu nhiều phép thử sau 27; ví dụ 28; hình thức 29–30; chứng minh kỳ vọng/phương sai 31–32; chi phí 33; kiểm tra 34 | Hai thứ tự suy từ Ví dụ 3.8 dùng trước định nghĩa, quyết định riêng của root. Thuật toán tích lũy chữ ký thực hiện ở cụm kế; không bỏ ngầm |
| Quét hàng | Tình huống/vấn đề/trực giác 35; đặc tả 36; ví dụ 37–40; thuật toán 41; đúng 42; chi phí 43–44; giới hạn 45; kiểm tra 46 | Đổi công khai a–e sang 0–4; giữ toàn bộ dữ kiện và vết min Hình 3.4. Đặc tả trước vết chạy đầy đủ vì MinHash và cực tiểu đã có trực giác tại 22–24 và 35 |

**Bản đồ mạch sau sửa 2026-10-14.** Bảng trên giữ số phiếu cũ; bảng dưới là trạng thái hiện hành theo mã trang (thứ tự trang và phút từng trang ở `storyboard.md`, mục "Bản đồ mạch và quyết định sửa toàn diện 2026-10-14").

| Mạch | Tên | Trang | Số trang | Phút |
|---|---|---|---:|---:|
| 1 | Tài liệu gần trùng và độ tương đồng Jaccard | s01-01, s01-10, s01-03, s01-02, s01-11, s01-04, s01-05, s01-07, s01-08, s01-09 | 10 | 19 |
| 2 | Shingling văn bản | s02-00 … s02-07, s02-09 | 9 | 20 |
| 3 | MinHash theo hoán vị | s03-00 … s03-02, s03-04 … s03-09 | 9 | 22 |
| 4 | Chữ ký MinHash | s04-00 … s04-07 | 8 | 16,5 |
| 5 | Tính chữ ký bằng hàm băm | s05-00 … s05-09, s05-13, s05-10 … s05-12 | 14 | 30,5 |
| 6 | Tổng kết và tự kiểm tra | s06-00, s06-05, s06-06, s06-02, s06-03, s06-04, s06-07 | 7 | 12 |
| 7 | Bài tập vận dụng | s07-00 … s07-07 | 8 | 60 |

Ví dụ xuyên suốt được gọi bằng tên: "kho một triệu tài liệu" (mở ở s01-05, thu hồi ở s06-02; cùng tên với ví dụ mở đầu Bài 06) và "bốn tập đặc trưng" (Hình 3.2; s03-02 → s05-13, s07-05).

Câu nối chính: Jaccard cần phần tử của tập; shingling tạo phần tử nhưng biểu diễn có thể lớn; MinHash cho một biến cố xác suất; nhiều thành phần tạo ước lượng; tính cực tiểu hiện thực hóa chữ ký; số cặp vẫn cần cơ chế ứng viên của Bài 06.

## 6. Ví dụ, dữ kiện và kiểm tra vai trò số

Các dữ kiện dưới đây cố định theo sách. Quyết định chung là **giữ số và bổ sung nhãn**, không điều chỉnh dữ liệu để tạo kết quả thuận lợi. Màu chỉ hỗ trợ; mọi khác biệt còn có nhãn hàng, cột, vị trí hoặc loại X/Y/Z.

| Mã ví dụ | Đại lượng → ký hiệu → giá trị → kiểu/vai trò → nguồn | Vết chạy và thử lỗi dễ mắc |
|---|---|---|
| VD 1 | Số tài liệu $C=10^6$, số cặp $C(C-1)/2=499\,999\,500\,000$; số đếm; B tr. 73 | Không dùng $C^2$ như số cặp chính xác; không gán tốc độ phần cứng |
| VD 2 | Giao 3, hợp 8, $\mathrm{SIM}=3/8$; số phần tử và tỷ số; Hình 3.1 | 3 không phải số hàng chữ ký; không dùng $\lvert S\rvert+\lvert T\rvert$ làm mẫu số |
| VD 3 | $D=\texttt{abcdabd}$, $\ell=7$, $k=2$; chuỗi/độ dài; VD 3.3 | Cửa sổ `ab, bc, cd, da, ab, bd`; tập có 5 phần tử. Giữ lặp `ab` để phân biệt lần xuất hiện và phần tử |
| VD 4 | `touch down` dài 10, `touchdown` dài 9, $k=9$; VD 3.4 | Hai cửa sổ `touch dow`,`ouch down` khác cửa sổ `touchdown`; không dịch chuỗi rồi giữ đáp án |
| VD 5 | $R=5, C=4, L=9$; Hình 3.2 | Ma trận dưới đây; tổng kích thước $2+1+3+3=9$, 20 ô. Không đồng nhất 9 phần tử hiện diện với 5 hàng |
| VD 6 | $\pi=(b, e, a, d, c)$; định danh kết quả $(a, c, b, a)$, hạng $(3,5,1,3)$; Hình 3.3 | Cặp 1–4 trùng một lần, Jaccard $2/3$; dùng cùng thứ tự cho mọi cột |
| VD 7 | $n=2$, $\pi_1=(e, a, b, c, d)$, $\pi_2=(d, a, c, e, b)$; suy trực tiếp VD 3.8 | Hàng định danh $(a, c, e, a)$ và $(d, c, d, d)$; tỷ lệ trùng cặp 1–4 bằng 1. Đây là hai thứ tự cố định, không phải bằng chứng chọn đều |
| VD 8 | Mã hàng 0–4; $f_1(r)=(r+1)\bmod5$, $f_2(r)=(3r+1)\bmod5$; VD 3.8 | Giá trị và trạng thái trong storyboard; $f_2(3)=0$ là giá trị, khác chỉ số hàng 3; phép min có thể giữ nguyên |
| VD 9 | $s=2/3, n=100$; áp dụng Hình 3.2 và độ dài minh họa §3.3.4 | Kỳ vọng số lần trùng $200/3$, tỷ lệ $2/3$, phương sai $1/450$; kỳ vọng số đếm có thể không nguyên |

| Phần tử | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| a | 1 | 0 | 0 | 1 |
| b | 0 | 0 | 1 | 0 |
| c | 0 | 1 | 0 | 1 |
| d | 1 | 0 | 1 | 1 |
| e | 0 | 0 | 1 | 0 |

$S_1=\{a, d\}$, $S_2=\{c\}$, $S_3=\{b, d, e\}$, $S_4=\{a, c, d\}$. Sáu Jaccard theo thứ tự 12, 13, 14, 23, 24, 34 là $0,1/4,2/3,0,1/3,1/5$. Vét cạn 120 hoán vị cho số trùng $0, 30, 80,0, 40,24$; phép kiểm hỗ trợ đối chiếu số, không thay chứng minh.

Nguồn quy mô bộ nhớ: B tr. 81, tài liệu 50.000 byte, tập mã khoảng 200.000 byte, chữ ký 1.000 byte dưới mô hình lưu mã 4 byte. Các số là minh họa của nguồn, không phải số đo mới hoặc bảo đảm sai số. Không suy ít byte hơn từ riêng $n<R$: ma trận bit và chữ ký từ máy có đơn vị khác nhau.

## 7. Mức hình thức hóa và điều kiện đúng

| Mã | Phát biểu, giả thiết và kết luận | Mức, vai trò và vị trí |
|---|---|---|
| HT1 | Hai tập hữu hạn, $S\cup T\ne\varnothing$: $\mathrm{SIM}(S, T)=\lvert S\cap T\rvert/\lvert S\cup T\rvert$ | Định nghĩa; áp dụng Hình 3.1, trang 07 |
| HT2 | $k\ge1$, $D$ dài $\ell$: $S_k(D)=\{D[i:i+k]:0\le i\le\ell-k\}$; rỗng nếu $\ell<k$ | Định nghĩa và bất biến tập cửa sổ; 12–13 |
| HT3 | $S\ne\varnothing$: $h_\pi(S)=\arg\min_{u\in S}\operatorname{rank}_\pi(u)$ | Định nghĩa trả định danh; 24, sau ví dụ |
| HT4 | $S, T\ne\varnothing$, $\pi$ đều trên $R!$ hoán vị, dùng chung: $\Pr[h_\pi(S)=h_\pi(T)]=\mathrm{SIM}(S, T)$ | Chứng minh đầy đủ: phần tử đầu của hợp phân bố đều và trùng khi, chỉ khi thuộc giao; 25–26 |
| HT5 | $X_i=\mathbf1\{h_{\pi_i}(S)=h_{\pi_i}(T)\}$; $\widehat{\mathrm{SIM}}=n^{-1}\sum_iX_i$ | Định nghĩa ước lượng; so sánh cùng tọa độ; 29–30 |
| HT6 | Mỗi hoán vị đều: $\mathbb E[X_i]=s$, $\mathbb E[\sum_iX_i]=ns$, $\mathbb E[\widehat{\mathrm{SIM}}]=s$ | Suy ra tuyến tính kỳ vọng; độc lập không cần ở bước này; 31 |
| HT7 | Thêm độc lập: $\operatorname{Var}(\widehat{\mathrm{SIM}})=s(1-s)/n$ | Suy ra Bernoulli, đầy đủ trong ghi chú; không thêm bất đẳng thức tập trung; 32 |
| HT8 | $f_i:\{0,\ldots,R-1\}\to V$, $V$ hữu hạn có thứ tự toàn phần; $+\infty$ lớn hơn mọi phần tử của $V$. Sau tập hàng $A$, $\mathrm{SIG}(i,c)=\min(\{f_i(r):r\in A,M(r,c)=1\}\cup\{+\infty\})$. Khi quét xong, $A=\{0,\ldots,R-1\}$, kể cả cột rỗng trả $+\infty$ | Đặc tả toàn miền ở 36, bất biến và khởi tạo/duy trì/dừng ở 42; tính cực tiểu không tự chứng minh họ băm lý tưởng |
| HT9 | Mô hình từ máy, đầu vào đã có: đặc $\Theta(nC+nR+RC+nL)$; danh sách hàng $\Theta(nC+nR+nL)$ | Phép đếm từ giả mã; chữ ký $\Theta(nC)$ từ, đệm $\Theta(n)$; 43–44 |

Hai hàm modulo 5 của ví dụ là hoán vị vì hệ số 1 và 3 khả nghịch modulo 5. Một hàm affine modulo $R$ là hoán vị khi hệ số góc nguyên tố cùng nhau với $R$; không cần $R$ nguyên tố. Bảng giá trị trong Bài 3.3.3 là chứng cứ trực tiếp ở modulo 6. Song ánh không kéo theo phân phối đều trên mọi hoán vị; không gán định lý chính xác cho một họ băm hữu hạn tùy ý.

## 8. Tổng hợp quyết định và bản đồ ghi chú

Điều phối viên chấp nhận kế hoạch độc lập và hồ sơ nguồn trước writer. Phương sai, bất biến và chi phí được thêm để lấp ba khoảng trống: tác dụng định lượng của độ dài chữ ký; căn cứ đúng của phép quét; khả năng đối chiếu lợi ích bộ nhớ với giới hạn số cặp. Không thêm thuật toán hai con trỏ, rolling hash, chuỗi de Bruijn, Hoeffding, họ băm nâng cao hoặc banding.

| `note-topic-id` | Nhãn, quyết định, nguồn | Vai trò; đầu vào → sản phẩm; vị trí trước–sau | Thành phần trình bày và slide |
|---|---|---|---|
| n05-01 | cốt lõi, giữ; B73–76 | Kho văn bản → đặc tả và hai giới hạn; mở toàn bài, dẫn n05-02 | Vai trò, ví dụ nguồn, đếm cặp, lỗi; 04–05,47–48; không có định lý/thuật toán riêng |
| n05-02 | cốt lõi, giữ; §3.1.1 | Giao/hợp → Jaccard; sau bài toán, trước shingle | Định nghĩa trước VD 3.1, hình giao/hợp, biên và kiểm tra; 06–09 |
| n05-03 | cốt lõi, giữ; §§3.2.1–3.2.3 | Chuỗi và băm → tập shingle; nhận đại lượng Jaccard, chuyển tập cho n05-04 | Đặc tả, VD 3.3–4, trực quan, giả mã, bất biến, chi phí trực tiếp, lỗi; 10–18 |
| n05-04 | cầu nối, thêm tường minh; §3.3.1 và BT 3.3.8 | Tập → ma trận, miền không rỗng; nối biểu diễn tới MinHash | Định nghĩa, Hình 3.2, thưa, trường hợp $\ell<k$; 19–21; không có định lý độc lập |
| n05-05 | cốt lõi, giữ; §3.3.2 | Thứ tự và ma trận → định danh phần tử thắng; trước xác suất | Định nghĩa trước VD 3.7, hình, quy ước định danh/hạng, kiểm tra; 22–24 |
| n05-06 | cốt lõi, giữ; §3.3.3 | Giao/hợp và hoán vị đều → chứng minh xác suất; tạo căn cứ n05-07 | Ví dụ X/Y/Z, định lý đủ giả thiết, chứng minh hai chiều, biên; 25–27 |
| n05-07 | cốt lõi, giữ/sửa; §3.3.4 | Một phép thử → chữ ký và ước lượng; chuẩn bị phương sai | Định nghĩa, VD 7, ma trận, kỳ vọng số đếm/tỷ lệ, chi phí cặp; 28–31,33–34 |
| n05-08 | bổ sung, thêm đã duyệt; hệ quả §§3.3.3–4 | Bernoulli độc lập → phương sai; lấp căn cứ của tác dụng $n$ | Mệnh đề, chứng minh, áp dụng và giới hạn; 32, 34; không có thuật toán riêng |
| n05-09 | cốt lõi, giữ; §3.3.5 | Băm hàng và min → chữ ký thực hành; nhận lý tưởng, chuyển vết chạy cho n05-10 | Đặc tả, VD 3.8 đầy đủ, trực quan, giả mã; 35–41 |
| n05-10 | bổ sung, thêm đã duyệt; suy từ §3.3.5 | Vòng lặp → bất biến, dừng, phép đếm; thu hồi nhu cầu bộ nhớ | Chứng minh đầy đủ, bảng thao tác, đặc/thưa, từ máy, kiểm tra; 42–44, 46 |
| n05-11 | cầu nối, giữ; §3.3.5, BT 3.3.3/3.3.8 | Lý tưởng và thực hành → điều kiện bảo đảm, giá trị thiếu; trước tổng hợp | Biên tập rỗng, va chạm, song ánh/phân bố, lỗi; 45–48; không có cơ chế mới |
| n05-12 | đọc thêm, gộp; §3.1.3, §3.2.4 | Biểu diễn đã học → đa tập/từ dừng; nhánh sau tuyến chính | Giữ quy ước hợp cộng của sách nếu trình bày; không áp định lý tập hợp; không có slide bắt buộc |
| n05-13 | đọc thêm, chuyển; §§3.3.6–3.3.7 | Chữ ký đầy đủ → cắt hàng/phân nhóm; nhánh sau giới hạn | Hoán vị đều của $U$, $m$ nguyên với $1\le m<R$, $+\infty$, VD 3.9 và giới hạn; không có slide bắt buộc |
| n05-14 | cốt lõi, giữ; năm bài nguồn | Các kết quả chính → lời giải độc lập, không phụ thuộc đọc thêm | Đề, hướng giải, lời giải gập và tiêu chí; 49–57 |

Chu trình ghi chú: vai trò → định nghĩa/đặc tả → ví dụ → trực quan → phát biểu → thuật toán khi có → chứng minh → ứng dụng/lỗi/kiểm tra. Chu trình này khác chủ ý với slide, nơi trực giác và ví dụ thường đi trước hình thức hóa. Ghi chú không sao chép nguyên văn các notes. Các mục không áp dụng được nêu trong bảng, không tạo đề mục rỗng.

Tài sản dự kiến: hình giao–hợp, cửa sổ shingle, hoán vị chung, phần tử đầu trong hợp, quy trình tài liệu–tập–chữ ký. Ma trận và vết chạy là bảng HTML để đọc giá trị chính xác. Mọi SVG có mô tả thay thế cụ thể và giữ dữ liệu nguồn. Kế hoạch chưa xác nhận các tài sản đã được vẽ.

## Tự kiểm trước khi dựng

Đã đối chiếu 7 phần, 50 trang giảng, 7 trang bài tập, 120+60 phút; mỗi phần có trang kiểm tra. Trang 28 đã đổi thành ví dụ cụ thể trước trang 29 hình thức hóa; lấy lại dữ liệu Ví dụ 3.8 có ghi nguồn và bản chất cố định. Đã chuẩn hóa $\ell, k, R, C, n, L$, $h_\pi, f_i$, $\mathrm{SIM},\widehat{\mathrm{SIM}}$. Bài tập giữ số, chỉ đổi ký hiệu độ dài tài liệu và tên hàm băm.

No-ai-slop Edit/eval áp dụng cho tiêu đề, câu chốt, nội dung dự kiến và notes trong storyboard; giữ nguyên giả thiết và kết luận. Quill Outline/Revise áp dụng cho quan hệ tiên quyết, đầu vào/đầu ra và tính liên tục, không tạo `quill.json`. Những kiểm tra hiển thị, năm báo cáo độc lập, QA viewer và phát hành vẫn chưa thực hiện tại thời điểm này; ghi riêng trong `review-log.md`.


## Hiệu chỉnh theo cửa kiểm G01–G06

Bản đồ mục tiêu đã được giới hạn theo nhiệm vụ thực sự được đo ở trang 49–57. Trang 17 nói rõ giả thiết không va chạm khi suy từ 5 shingle sang 5 mã phân biệt. Trang 28 liệt kê đủ bốn tập và chốt bảng hai thứ tự cố định trên cùng mặt trang. Đặc tả trang 36 định nghĩa đủ miền chỉ số $i$, miền $V$ hữu hạn có thứ tự toàn phần và kết quả $+\infty$ cho cột rỗng, thống nhất HT8 và trang 42. Trang 43 giải nghĩa $L$ là tổng số ô 1 trước phép đếm $nL$. Chỉ dẫn giữ nguyên phạm vi bài tập nằm ở trường nội bộ, không trong notes học thuật; Hình 3.4 được dẫn đúng tr. 85, còn Ví dụ 3.8 trải tr. 85–86.

Các hiệu chỉnh không thay sườn sách, 57 trang hoặc thời lượng 120+60 phút. Trạng thái: writer đã sửa theo báo cáo, chờ tác tử cửa kiểm tái kiểm; chưa xác nhận đạt để triển khai HTML.


## Quyết định biên tập sau bản nháp công khai

Điều phối viên đã hợp nhất đủ năm báo cáo độc lập và gate bản thực trước khi giao editor riêng. Giữ toàn bộ bản đồ chủ đề, 57 trang, bảy phần và thời lượng 120 + 60 phút. Những sửa sau chỉ khép khoảng trống đã có, không mở chủ đề mới:

| Chủ đề | Quyết định | Khoảng trống, nội dung bổ sung và quan hệ trước–sau |
|---|---|---|
| n05-01 | giữ, làm rõ | Định nghĩa $C$ trên slide đếm cặp trước công thức; không đổi bài toán mở đầu. |
| n05-03 | giữ, làm rõ | Trang 13 có mô hình $O(k)$ kỳ vọng cho tạo/băm/chèn khóa; tổng $O(1+wk)$ kể khởi tạo, đồng bộ ghi chú. |
| n05-05/06 | giữ, phục hồi | Argmin trả phần tử, ví dụ định danh $a$ và hạng 3; hình X/Y/Z đặt điều kiện phần tử đầu hợp; đầu vào cho chứng minh không đổi. |
| n05-07/08 | giữ, phục hồi | Bảng hai tọa độ chữ ký ở 30 tạo căn cứ cho hai chỉ báo; chuỗi phương sai ở 32 chỉ chỗ dùng độc lập. |
| n05-09/10 | giữ, phục hồi | Bảng 37 có đủ mã/phần tử, incidence và giá trị băm; 39/40 giữ trạng thái vào và đánh dấu thành phần giảm. Dữ kiện là Ví dụ 3.8, chuẩn bị vòng lặp, bất biến và phép đếm $nL$. |
| n05-09/11 | cầu nối, làm rõ | Với $a\leftrightarrow0$, $d\leftrightarrow3$, cặp $S_1,S_4$ đổi $(a,d)^{\mathsf T}$ thành $(f_1(0),f_2(3))^{\mathsf T}=(1,0)^{\mathsf T}$; không va chạm bảo toàn so bằng, không suy ngẫu nhiên đều từ song ánh. |
| n05-12 | đọc thêm, giữ | Đổi tên đa tập thành $B_1,B_2$ để giữ $C$ cho số tài liệu; nêu hữu hạn và tổng bội dương. Ví dụ từ dừng phục hồi đúng chín vị trí theo PDF tr. 80, không lấy danh sách ngoài. |
| n05-13 | đọc thêm, làm rõ | Chọn đều hoán vị và lấy $m$ hàng đầu với $m$ nguyên, $1\le m<R$. Không thêm công thức phương sai cho mẫu số hữu ích ngẫu nhiên. |
| n05-14 | giữ, ghi mức chứng minh | Bài 3.2.3 giữ byte và giả thiết ít nhất $\ell$ chuỗi độ dài $k$. Quy ước tính mỗi ký tự một byte; đáp số $\max(0,\ell-k+1)$ kèm chứng minh cận trên. Không chứng minh phần đạt cận, không thêm de Bruijn hay giả thiết $\ell$ ký tự khác nhau. |

No-ai-slop Edit/eval giữ nguyên phát biểu có điều kiện, nguồn và phân biệt toán học; chỉ sửa câu/nhãn liên quan phát hiện. Quill áp dụng cho tính liên tục theo bảng này, không tạo `quill.json`. Năm báo cáo và quyết định từng phát hiện được lưu bền vững trong review-log; kết luận kiểm định cuối vẫn thuộc điều phối viên sau tái kiểm.


## Duyệt từng trang ngày 01/10/2026

Lượt duyệt theo yêu cầu người dùng: với mỗi trang, xác định trang muốn nói gì, đề xuất rồi sửa để tiêu đề ngắn gọn, học thuật, lập luận chặt và khái niệm không xuất hiện đột ngột; sau mỗi trang sửa mục tương ứng của ghi chú tự học, commit và push. Chi tiết từng trang và các lượt rà lại theo phần nằm trong `review-log.md`, mục cùng tên.

- **Cấu trúc.** Deck còn 55 trang (48 giảng, 7 bài tập), bảy phần 9/8/8/7/12/4/7. Trang 17 (dung lượng tập shingle) gộp vào trang 19 vì cùng luận điểm; trang 21 (biểu diễn thưa) gộp vào trang 20 vì ghi chú phải nhắc giá trị băm trước khi giới thiệu và danh sách cột theo hàng đã xuất hiện đúng lúc ở trang 37, 43. Thời lượng chuyển sang trang 19 và 22; phần 2 còn 21 phút, phần 3 có 23 phút.
- **Câu nối mới.** Tài liệu → tập (trang 06); trực giác “một thay đổi ảnh hưởng nhiều nhất $k$ cửa sổ” (trang 10); tiêu chí chọn $k$ (14); so sánh 4-shingle với mã 9-shingle (16); nhu cầu một đại diện (22); một phép thử chỉ cho 0/1 (28); nhu cầu mô phỏng hoán vị (35); thu hồi hai thừa số của trang 05 ở trang 48.
- **Câu hỏi kiểm tra.** Các trang 09, 18, 27, 34, 46, 49, 50 thay câu có đáp án trên mặt trang trước bằng câu vận dụng; dữ kiện biến thể ghi rõ ở dòng nguồn.
- **Tiêu đề.** 40 trong 54 tiêu đề `h2` đổi theo khái niệm hoặc kết quả trung tâm; không đặt ký hiệu trong tiêu đề viết hoa.
- **Ghi chú tự học.** Mục 1–11 và 14 cập nhật theo các câu nối và câu hỏi mới; thứ tự khái niệm của ghi chú giữ nguyên.

## Duyệt từng trang lần hai ngày 07/10/2026

Lượt duyệt theo yêu cầu người dùng: với mỗi trang, xác định trang muốn nói gì, vấn đề còn lại và cách thể hiện tốt hơn; xong thì commit và push. Chi tiết từng trang nằm trong `review-log.md`, mục cùng tên.

- **Cấu trúc.** Deck còn 54 trang (47 giảng, 7 bài tập), bảy phần 8/8/8/7/12/4/7. Trang 06 (đếm giao, hợp) gộp vào trang 07 vì hai trang dùng cùng Hình 3.1 cho một luận điểm; thời lượng 2 phút chuyển sang trang 07. Tổng 120 + 60 phút giữ nguyên.
- **Hình.** Thêm `ban-tin-dang-lai.svg` (trang 04, ví dụ dựng hai bản tin) và `bam-thay-hoan-vi.svg` (trang 35, $f_1$ tạo thứ tự $(e,a,b,c,d)$). Xóa `tai-lieu-gan-trung.svg` và `quy-mo-so-sanh-cap.svg`. `quet-ma-tran-thua.svg` chỉ còn dùng trong ghi chú tự học. Bộ hình hiện có tám SVG.
- **Số liệu thu hồi.** Ví dụ 3.10 (tr. 92) cung cấp giả định một micro giây mỗi cặp và quy mô 1 GB cho $10^6$ chữ ký 1.000 byte; trang 05 dùng thời gian gần 6 ngày, trang 48 thu hồi bộ nhớ, độ lệch chuẩn và thời gian.
- **Dữ kiện trên mặt trang.** Trang 10 (bảng cửa sổ `abcdabd`/`abcxabd`), 12, 20, 30 (hai tập và hai thứ tự), 44 ($n=250$) đưa dữ kiện lên trang thay cho dẫn chiếu bằng lời.

## Sửa toàn diện theo chuẩn 2026-10-14

Căn cứ: `AGENTS.md` ("Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch", "Văn phong và mật độ mặt trang chiếu", "Tiêu chuẩn trang chiếu và ghi chú diễn giả"), `slide_authoring_standard.md`, deck mẫu Bài 06. Tóm tắt quyết định (chi tiết ở `storyboard.md` và `review-log.md`, mục cùng tên):

- **Mạch mở đầu** (8 → 10 trang): bìa có câu luận đề và dòng đơn vị; thêm "Tiên quyết và quy ước" (`lec05-s01-10`) và "Vấn đề trung tâm" (`lec05-s01-11`); "Mục tiêu học tập" đứng trước "Nội dung"; "Nội dung" có dòng "Đọc trước:"; s01-05 thành "Ví dụ: kho một triệu tài liệu".
- **Mạch kết luận** (5 → 7 trang): thêm "Kết quả và giả thiết không được bỏ" (`lec05-s06-05`), "Thuật toán, bảo đảm và chi phí" (`lec05-s06-06`), "Nguồn và tài liệu đọc" (`lec05-s06-07`); s06-02 thành "Câu trả lời cho vấn đề trung tâm"; bỏ s06-01 "Quy trình biểu diễn tài liệu" (hình vẫn dùng trong ghi chú bài giảng); hai trang câu hỏi thành "Câu hỏi tự kiểm tra".
- **Mạch 5** (13 → 14 trang): s05-09 tách bảng thay số sang `lec05-s05-13`.
- **Mặt trang**: bỏ 52 dòng `p.ex-source` (ghi công mmds.org chuyển sang trang nguồn); bảy trang đề recitation giữ một dòng "Nguồn: MMDS, Bài …"; mỗi trang nhiều nhất một câu kết luận có nhãn; nhãn chỉ trong danh sách cho phép; tiêu đề có tiền tố "Ví dụ:", "Thuật toán:", "Tính đúng:", "Chi phí:", "Bài tập:" theo `AGENTS.md`.
- **Ghi chú diễn giả**: bỏ bảy câu thời lượng của mạch 7; trang đề recitation có năng lực kiểm, "Gợi ý:", "Lời giải:"; bỏ câu lấy tài liệu làm chủ ngữ và dẫn chiếu "phần sau/Phần 2".
- **Ký hiệu, dữ kiện, kết luận toán học**: không đổi. Hai số mới là tổng thay số ở s05-13: $8+10+20+18=56$ và $8+10+18=36$.

### Lượt sửa sau ba báo cáo rà (2026-10-14)

- Bảng kết quả–giả thiết (s06-05): hàng "Tập mã shingle" nêu kết quả "SIM trên tập mã bằng SIM trên tập shingle" dưới giả thiết cùng quy ước khoảng trắng, mã không va chạm; cận \(|S_k(D)|\le w\) thuộc bảo đảm của thuật toán tạo tập shingle (s06-06).
- Quy ước: hạng trong hoán vị đếm từ 1, vị trí ký tự và mã hàng đếm từ 0 (ghi tại s03-05, s03-06 và ghi chú s01-10). Ký hiệu Bài 01 \(J\), \(N\), \(C_i\) ứng với \(\mathrm{SIM}\), \(C\), \(S_i\) của bài này, nêu trên trang Tiên quyết và quy ước.
- Trang vấn đề trung tâm và trang câu trả lời dùng danh sách không đánh số, sáu dòng theo thứ tự mạch, như Bài 06.

## Ghi chú theo chuẩn giáo trình (2026-11-11)

Mục này thay bản đồ ghi chú ở §8 (`n05-01`… chỉ còn là lịch sử). Ghi chú `materials/lec-05/lecture-note.md` viết lại theo kế hoạch `lec05-plan.md` và quyết định Q1–Q14 của điều phối viên; bộ trang chiếu giữ nguyên.

**Goal.** Ghi chú là một chương giáo trình tự chứa theo `materials/_templates/lecture-note.md`: mục tiêu (7), tiên quyết dẫn số hiệu Bài 01, bảng ký hiệu ba cột, năm mục nội dung ứng với năm mạch nội dung của deck, một phần đọc thêm thu gọn sau Mục 5 gồm hai tiểu mục, ba tình huống, tóm tắt. Bài tập cuối mục 05.1–05.14 trong ghi chú; bài tập củng cố 05.15–05.28 ở `materials/lec-05/exercises.md`, chỉ bài MMDS §3.1–3.3; recitation của deck là 05.15, 05.19, 05.20, 05.21, 05.22. Jaccard không được định nghĩa lại (Định nghĩa 01.9 phát biểu lại ở tiên quyết, Q4); ví dụ Hình 3.1 và `jaccard-ba-vung.svg` không còn trong ghi chú. "Trong thực hành" là đoạn văn có nhãn in đậm (Q14).

**Vấn đề trung tâm.** Kho $10^6$ tài liệu: $499\,999\,500\,000$ cặp; tập mã shingle khoảng $200\,000$ byte mỗi tài liệu (Ví dụ 05.1; MMDS tr.81). Hình cấu trúc chương: `img/lec-05/note-cau-truc-chuong-05.svg`, sinh bởi `../tools/courses/ds-foundation-algorithms/2627-1/img/lec-05/generate_note_svg.py`.

### Bản đồ chủ đề bốn nhóm

| note-topic-id | Mục ghi chú | Chủ đề và khối số hiệu | Nhãn | Nguồn | Chu trình |
|---|---|---|---|---|---|
| `lec-05-topic-01` | Mục 1 mở, 1.1 | Ba tình huống gần trùng; hình cấu trúc chương; Ví dụ 05.1 | cầu nối | MMDS tr.73, §3.1.2 tr.75–76, Ví dụ 3.10 tr.92; Bài 01 (Mệnh đề 01.12, Bổ đề 01.14, Mệnh đề 01.15, Ví dụ 01.8) | rút gọn: mục giới thiệu, không định nghĩa |
| `lec-05-topic-02` | 1.2 | Nhắc Định nghĩa 01.9; Nhận xét 05.1 (ngưỡng $t$); Bài tập 05.1, 05.2 | cầu nối | §3.1.1–3.1.3 tr.74–76 | rút gọn: khái niệm đã định nghĩa ở Bài 01 |
| `lec-05-topic-03` | Mục 2 | Ví dụ 05.2, 05.3, 05.4; Định nghĩa 05.2; Thuật toán 05.3; Mệnh đề 05.4, 05.6; Nhận xét 05.5; Bài tập 05.3, 05.4 | cốt lõi | §3.2.1–3.2.3 tr.78–80, Ví dụ 3.3, 3.4 | đủ (ví dụ trước định nghĩa, thuật toán, tính đúng, chi phí, giả thiết bị bỏ, trong thực hành) |
| `lec-05-topic-04` | Mục 3 mở, 3.1 | Ví dụ 05.5; Định nghĩa 05.7 | cầu nối | §3.3.1 tr.81–82, Ví dụ 3.6, Hình 3.2 | rút gọn: biểu diễn, không có định lý riêng |
| `lec-05-topic-05` | 3.2 | Ví dụ 05.6; Định nghĩa 05.8 | cốt lõi | §3.3.2 tr.82–83, Ví dụ 3.7, Hình 3.3 | đủ |
| `lec-05-topic-06` | 3.3 | Ví dụ 05.7, 05.8; Bổ đề 05.9; Định lý 05.10 (bốn phần, ba "Bỏ …"); Bài tập 05.5, 05.6 | cốt lõi | §3.3.3 tr.83; §3.3.5 tr.84 (trong thực hành) | đủ |
| `lec-05-topic-07` | Mục 4 mở, 4.1–4.3 | Ví dụ 05.9; Định nghĩa 05.11; Mệnh đề 05.12, 05.13 | cốt lõi | §3.3.4 tr.83–84 | đủ |
| `lec-05-topic-08` | 4.4 | Mệnh đề 05.14; Hệ quả 05.15; Ví dụ 05.10; Nhận xét 05.16; Bài tập 05.7, 05.8, 05.9 | bổ sung (đã duyệt, HT7) | suy từ §3.3.4; tr.81, tr.83 (trong thực hành) | đủ |
| `lec-05-topic-09` | Mục 5 mở, 5.1–5.2 | Ví dụ 05.11, 05.12; Định nghĩa 05.17; Thuật toán 05.18 | cốt lõi | §3.3.5 tr.84–86, Ví dụ 3.8, Hình 3.4 | đủ (vết chạy trước giả mã) |
| `lec-05-topic-10` | 5.3–5.4 | Mệnh đề 05.19, 05.21; Hệ quả 05.20; Ví dụ 05.13 | bổ sung (đã duyệt) | suy từ §3.3.5; tr.81, Ví dụ 3.10 (trong thực hành) | đủ |
| `lec-05-topic-11` | 5.5 | Mệnh đề 05.22; Nhận xét 05.23; Bài tập 05.10, 05.11, 05.12 | cầu nối | §3.3.5; CS246 03-lsh trang chiếu 33 | rút gọn: điều kiện và giới hạn của cơ chế đã có |
| `lec-05-topic-12` | Đọc thêm (thu gọn), tiểu mục 1 | Định nghĩa 05.24, 05.25; Ví dụ 05.14, 05.15; Bài tập 05.13 | đọc thêm | §3.1.3 tr.77, §3.2.4 tr.80 | rút gọn |
| `lec-05-topic-13` | Đọc thêm (thu gọn), tiểu mục 2 | Nhận xét 05.26; Ví dụ 05.16; Bài tập 05.14 | đọc thêm | §3.3.6–3.3.7 tr.86–90, Ví dụ 3.9, Hình 3.5 | rút gọn |
| `lec-05-topic-14` | Tình huống và ứng dụng | Tình huống 05.1 (kho $10^6$, $n=250$), 05.2 (tài liệu ngắn hơn $k$, giả thiết không rỗng bị vi phạm), 05.3 (bộ hàm cố định của Ví dụ 3.8); ứng dụng Bài 06, 08, 09, 10 | cốt lõi (áp dụng) | tr.81, Ví dụ 3.8, 3.10 | không áp dụng |
| `lec-05-topic-15` | Tóm tắt chương | Đoạn 7 câu, kết quả theo mục, công thức, giả thiết hay bỏ quên; hình `quy-trinh-bieu-dien.svg` | tổng kết | toàn chương | không áp dụng |
| `lec-05-topic-16` | Bài tập củng cố | Liên kết tới `exercises.md` (05.15–05.28) | tổng kết | MMDS Bài 3.1.1–3.3.9 | không áp dụng |

Phần đọc thêm là một mục `##` thu gọn ("Đọc thêm: Biến thể của biểu diễn và của phép quét") chứa hai tiểu mục, thay cho hai mục `##` thu gọn liền nhau của kế hoạch: `material-viewer.js` chuyển dấu `note-collapsed` thứ hai vào thân mục thu gọn thứ nhất và báo lỗi "Dấu note-collapsed phải đứng ngay trước một tiêu đề cấp hai".

**Bài tập theo mục tiêu (bảy mục tiêu).** Mục tiêu 1 ↔ 05.1, 05.2 / 05.15; mục tiêu 2 ↔ 05.3, 05.4 / 05.16, 05.19; mục tiêu 3 ↔ 05.5, 05.6 / 05.20, 05.23, 05.26, 05.27; mục tiêu 4 ↔ 05.7(a)(b), 05.9 / 05.22(c); mục tiêu 5 ↔ 05.7(c), 05.8 / không có; mục tiêu 6 ↔ 05.10, 05.11 / 05.21, 05.22(a), 05.25; mục tiêu 7 ↔ 05.12 / 05.22(b), 05.24; đọc thêm ↔ 05.13, 05.14 / 05.17, 05.18, 05.28. Mục tiêu 5 không có bài MMDS riêng cho phương sai; theo `AGENTS.md` mục 10 nó dựa vào bài cuối mục.

### Thuật ngữ Việt–Anh của ghi chú

| Tiếng Việt | Tiếng Anh | Lần đầu trong ghi chú |
|---|---|---|
| độ tương đồng Jaccard | Jaccard similarity | Kiến thức tiên quyết (Định nghĩa 01.9) |
| shingle, $k$-shingle | shingle, $k$-gram | Giới thiệu chương; Định nghĩa 05.2 |
| cửa sổ | (window) | Định nghĩa 05.2 |
| va chạm | collision | Mục 2.4 |
| ma trận đặc trưng; biểu diễn theo hàng | characteristic matrix | Mục tiêu 3; Định nghĩa 05.7 |
| hoán vị; hạng | permutation; (rank) | Mục tiêu 3; Định nghĩa 05.8 |
| chữ ký MinHash; ma trận chữ ký | MinHash signature; signature matrix | Mục tiêu 4; Định nghĩa 05.11 |
| ước lượng không chệch | unbiased (estimator) | Mục tiêu 4 |
| hàm băm; lượt quét; bất biến vòng lặp; biến chỉ báo | hash function; pass; loop invariant; indicator variable | Kiến thức tiên quyết |
| giá trị canh | sentinel | Bảng ký hiệu |
| đa tập; bội | bag, multiset; (multiplicity) | Đọc thêm |
| từ dừng | stop word | Đọc thêm |

### Khác biệt với bộ trang chiếu

- Thứ tự Mục 4: ghi chú đặt chi phí so sánh (4.3, Mệnh đề 05.13) trước phương sai (4.4, Mệnh đề 05.14); deck đặt `s04-05` (phương sai) trước `s04-06` (chi phí). Nội dung không đổi.
- Ký hiệu: tên phần tử chữ đứng $\mathrm a,\ldots,\mathrm e$ (deck chữ nghiêng); hệ số hàm affine $\alpha,\beta$ (deck `s05-11` viết $a,b$, trùng tên phần tử a, b); chỉ báo $\mathbf 1[E]$ như Bài 06 (deck $\mathbf 1\{E\}$); bí danh $\widehat s=\widehat{\mathrm{SIM}}$; loại hàng $\mathrm X,\mathrm Y,\mathrm Z$ chữ đứng; hàm mã shingle $g$ (deck không đặt tên); số lớn nhóm bằng khoảng trắng hẹp (deck `s01-11`, `s05-10`, `s06-02` viết "50.000", "200.000", "1.000"); "véc-tơ" (deck "vector").
- Deck `s01-10` ghi "Bài 01 viết $J(S,T)$"; ghi chú Bài 01 hiện viết $\mathrm{SIM}$ (lệch có từ trước).
- Mục tiêu: deck `s01-03` có năm mục; ghi chú tách mục 6 (hàm affine, giả thiết bị vi phạm).
- Nội dung thêm so với deck: Bổ đề 05.9 tách riêng; Mệnh đề 05.6 có chứng minh; danh sách "Bỏ …" sau Mệnh đề 05.4, 05.6, 05.12, 05.19 và Định lý 05.10; Hệ quả 05.20; Ví dụ 05.3 ($3/7$); Nhận xét 05.16; Nhận xét 05.23 với họ 20 hàm affine modulo 5 ($13/20$, $7/20$); ví dụ $R=4$ ở đoạn đọc Mệnh đề 05.22 (deck `s05-11` dùng hệ số 5 modulo 6 của Bài 3.3.3; ghi chú tránh lộ lời giải Bài tập 05.22(b)); Tình huống 05.2, 05.3.
- Câu hỏi tự kiểm `s06-03`, `s06-04` ↔ Bài tập 05.3(c), 05.4(c), 05.7(b)(c), 05.12(a), 05.9 của ghi chú; recitation `s07-01` ↔ 05.15, `s07-02` ↔ 05.19, `s07-03`/`s07-04` ↔ 05.20, `s07-05` ↔ 05.21, `s07-06`/`s07-07` ↔ 05.22.

### Tương ứng ký hiệu deck ↔ ghi chú

| Deck | Ghi chú | Lý do |
|---|---|---|
| $a,b,c,d,e$ (chữ nghiêng) | $\mathrm a,\ldots,\mathrm e$ | quy ước tên phần tử chữ đứng (Bài 01, 04); Ví dụ 06.3 của Bài 06 viết chữ nghiêng |
| $(ar+b)\bmod R$ | $(\alpha r+\beta)\bmod R$ | $a$, $b$ trùng tên phần tử (Q6); Bài 06 viết $\alpha,\beta$ |
| $\mathbf1\{E\}$ | $\mathbf 1[E]$ | như Bài 06 |
| $\widehat{\mathrm{SIM}}$ | $\widehat s=\widehat{\mathrm{SIM}}(S,T)$ | như Bài 06 |
| $X$, $Y$, $Z$ (loại hàng); $X_i$ (chỉ báo) | $\mathrm X$, $\mathrm Y$, $\mathrm Z$; $I_i$ | chữ X đã dùng cho loại hàng $\mathrm X$ và số đếm $x$, nên chỉ báo viết $I_i$ (vòng sửa 1) |
| (không có) | $g$ (mã shingle), $\mu_B(u)$ (bội), $P$ (nhóm hàng), $m$ (số hàng xét), $A$ (hàng đã quét, trong chứng minh) | thêm cho các mệnh đề và phần đọc thêm |
| MMDS: $n$ (độ dài tài liệu), $h_i$, $k$ (số hàng ở §3.3.6–3.3.7), $T$ (nhóm hàng) | $\ell$, $f_i$, $R$, $P$ | $n$ là độ dài chữ ký, $h_\pi$ là MinHash, $k$ là độ dài shingle, $T$ là tập của cặp |

### Vòng sửa 1 (2026-11-11): thay đổi so với bản nháp 1

Theo hàng đợi `lec05-queue.md` (A1–A14, B1–B3) và năm báo cáo rà. Số hiệu khối, ví dụ, tình huống và bài tập không đổi; `note-topic-id` không đổi.

- **Mục tiêu học tập:** bảy mục (mục tiêu 4 cũ tách thành 4: chữ ký, không chệch, chi phí so, Mục 4.1–4.3; và 5: phương sai, độ dài chữ ký, Mục 4.4). Bài tập theo mục tiêu: 1 ↔ 05.1, 05.2 / 05.15; 2 ↔ 05.3, 05.4 / 05.16, 05.19; 3 ↔ 05.5, 05.6 / 05.20, 05.23, 05.26, 05.27; 4 ↔ 05.7(a)(b), 05.9 / 05.22(c); 5 ↔ 05.7(c), 05.8 / không có bài MMDS; 6 ↔ 05.10, 05.11 / 05.21, 05.22(a), 05.25; 7 ↔ 05.12 / 05.22(b), 05.24.
- **Bài tập cuối mục đổi dữ kiện** (không hỏi lại kết quả đã in): 05.3(a) $k=3$ trên `abcdabd`/`abcxabd` ($1/4$); 05.4(a) $k$ nhỏ nhất với $20^k>2^{32}$ ($k=8$), (b) thư $2\,000$ ký tự, $k=5$ ($1\,996$ mã, $7\,984$ byte), (c) va chạm chéo cho $1/3$; 05.5(a) thêm phần tử f ($L=11$, $RC=24$, Jaccard $0\to1/5$), (b) $\pi=(\mathrm c,\mathrm e,\mathrm b,\mathrm a,\mathrm d)$; 05.8(b) $n=625$ khi chưa biết $s$; 05.9 tập mã so với chữ ký trên kho $10^4$ thư (tỷ số $19{,}96$); 05.10 hàng chữ ký thứ ba với $f_3=(4r+2)\bmod5$ (hàng $(2,0,1,0)$, 4 phép min không giảm); 05.11(a) $n=3$ (74 và 54 thao tác); 05.12(b) hàm $(4r+1)\bmod6$ trên hai tập rời ($\widehat s=1$); 05.13 ba cách đo $\{\mathrm a,\mathrm a,\mathrm b\}$, $\{\mathrm a,\mathrm b,\mathrm b\}$ ($1/3$, $1/2$, 1); 05.14 chia chẵn–lẻ và chia $\{0,1,2,7\}$/$\{3,4,5,6\}$ trên Hình 3.5. Mọi số kiểm bằng `scratchpad/l05w/verify_r1.py`.
- **Ví dụ 05.1** so chi phí một cặp trên tập mã ($\le100\,000$ phép so sánh, Bổ đề 01.14) với trên chữ ký (250), tỷ số 400; số cặp chỉ còn nêu ở tiên quyết và Ví dụ 05.1.
- **Ký hiệu:** vị trí cửa sổ $j$ (chỉ số hàm $i$); chỉ báo $I_i$ (loại hàng $\mathrm X,\mathrm Y,\mathrm Z$ giữ nguyên); $W_i$ trong Bước 2 chứng minh Mệnh đề 05.14; tập hàng đã quét $H$ (chứng minh Mệnh đề 05.19); bảng ký hiệu thêm $A$, $u$, $\Pr$, $\mathbb E$, $\operatorname{Var}$; quy ước thêm $L$, $R$, $M$ của Bài 01; "phân phối đều", "hoán vị (còn gọi là thứ tự liệt kê)"; tệp bài tập: $K=\lvert S\cap T\rvert$ ở 05.27, $x+y$ ở 05.20.
- **Mã hàng:** $U$ là tập các mã shingle xuất hiện trong kho, mã hàng là thứ tự tăng dần trong $U$, $R\le2^{32}$ (sau Định nghĩa 05.7); Tình huống 05.1 giả sử biểu diễn theo hàng đã có và thay số $nR\le1{,}07\cdot10^{12}$.
- **Nguồn:** giữ rào đón "có thể đã đủ bất thường" của MMDS ở Nhận xét 05.1; bỏ cụm "sai lệch tuyệt đối trên thang Jaccard"; tên $k$-gram dẫn trang chiếu MMDS tr.20, CS246 trang chiếu 18; quy ước bội lớn hơn ở tr.77, chú thích 2; họ hàm CS246 viết $((\alpha r+\beta)\bmod p)\bmod R$ kèm lý do không chọn đều.
- **Bài tập 05.19 (Q9):** cận $\max(0,\ell-k+1)$; giả thiết của đề bảo đảm đủ $\ell-k+1$ chuỗi khác nhau; phép dựng tường minh khi bảng chữ cái có ít nhất $\ell-k+1$ ký tự; `00010111` là ví dụ với bảng chữ cái nhỏ.
- **Ghi chú khác:** Bài 04 (Ứng dụng, Tóm tắt) nêu Jaccard là Định nghĩa 01.9 và Bài 05 ước lượng nó bằng chữ ký MinHash; Bài 06 bỏ Định nghĩa 05.25 khỏi tiên quyết và tham khảo, phát biểu lại đúng Mệnh đề 05.12, thêm "(Ví dụ 05.12)" và dòng tham khảo Bài 01; Bài 08 dẫn "Định nghĩa 05.17; Nhận xét 05.23"; Bài 09 dẫn "Bước 2 trong chứng minh Mệnh đề 05.14".
- **Không đổi:** hình `ban-tin-dang-lai.svg` (deck dùng chung, A14); deck 06, 09 vẫn dẫn số mục cũ trong ghi chú diễn giả (B3, ghi `review-log.md`).

### Vòng sửa 2 (2026-11-11)

Mục 1 mở bằng Thuật toán 01.11, Mệnh đề 01.12, Bổ đề 01.14, Mệnh đề 01.15 (không số liệu), đoạn giới thiệu chương bỏ câu về Bài 01; năm danh sách phản ví dụ (sau Mệnh đề 05.4, 05.6, 05.12, 05.19 và Định lý 05.10) trở lại câu mở chuẩn của `AGENTS.md`, phản ví dụ độc lập của Mệnh đề 05.14 gộp vào câu; Mục 5 mở bằng thiếu hụt của Ví dụ 05.9 ($R$ số mỗi hoán vị, MMDS §3.3.5); bảng chi phí Thuật toán 05.18 bỏ dòng bước 3, tổng ghi "cộng $O(1)$ cho bước 3" để khớp 56 thao tác của Ví dụ 05.13; Bài tập 05.24 không phụ thuộc phần đọc thêm; Bài tập 05.19 kết luận chỉ nêu điều kiện đạt cận tường minh. Số hiệu không đổi.

## Sửa deck theo bảng phát hiện (2026-11-13)

Deck sửa theo bảng phát hiện 2026-11-13 trong `review-log.md`, nguyên tắc deck mới và ghi chú (bản 2026-11-11, không sửa). Mục này thay các mục "Khác biệt với bộ trang chiếu" và "Tương ứng ký hiệu deck ↔ ghi chú" ở trên, vốn mô tả deck 2026-10-14; bảng mục tiêu MT1–MT5 và bảng "Mục tiêu hiển thị" ở Mục 1 cũng được thay bằng bảng dưới đây.

**Quy mô.** 81 trang: 66 trang giảng (120 phút), 15 trang bài tập vận dụng (60 phút); bảy mạch 10/13/10/10/15/8/15 (sau lượt sửa sau kiểm lại: thêm s02-13, bảng vết chèn của Ví dụ 05.2). Chi tiết từng trang, thời gian, ngoại lệ mật độ ở `storyboard.md`.

**Mục tiêu học tập trên deck (`lec05-s01-03`)** khớp bảy mục tiêu của ghi chú, cùng thứ tự; 80 âm tiết (đếm tay).

| Mục tiêu (ghi chú) | Trang phục vụ | Kiểm tra |
|---|---|---|
| 1. Số cặp nhân chi phí một cặp; Jaccard theo phần tử (Mục 1) | s01-04, s01-05, s01-07, s01-08 | s01-09; s07-01/s07-11 (Bài tập 05.15) |
| 2. Tập $k$-shingle, Thuật toán 05.3, mã giữ Jaccard (Mục 2) | s02-01 … s02-07, s02-10 … s02-13 | s02-09; s07-02/s07-12 (05.19) |
| 3. Ma trận đặc trưng, MinHash, Định lý 05.10 (Mục 3) | s03-01 … s03-08, s03-10 | s03-09; s07-03, s07-04 và lời giải (05.20) |
| 4. Chữ ký, không chệch, chi phí so (Mục 4.1–4.3) | s04-08, s04-01 … s04-04, s04-06 | s04-07 câu 1; s06-03 câu 3; s07-07/s07-17 (05.22(c)) |
| 5. Phương sai, độ dài chữ ký (Mục 4.4) | s04-05, s04-09 | s04-07 câu 2, 3 (Bài tập 05.8); s06-04 câu 4 |
| 6. Quét hàng, bất biến, thời gian, bộ nhớ (Mục 5.1–5.4) | s05-01 … s05-10, s05-13 | s05-12; s07-05/s07-15 (05.21), s07-06/s07-16 (05.22(a)) |
| 7. Hàm affine là hoán vị; giả thiết bị vi phạm (Mục 5.5, Tình huống 05.2, 05.3) | s05-11, s05-14 | s06-04 câu 5; s07-06/s07-16 (05.22(b)) |

**Mạch.** Mạch 2–5 ứng với Mục 2–5 của ghi chú, mỗi mạch mở bằng trang bài toán có hình (s02-01, s03-01, s04-08, s05-01); mạch tổng kết mở bằng s06-08 (hình quy trình của ghi chú). Thứ tự Mục 4 theo ghi chú: kỳ vọng (s04-04) → chi phí so (s04-06) → phương sai (s04-05) → cận độ lệch chuẩn (s04-09). Trong mạch 2, khoảng trắng (s02-06) đứng trước chọn $k$ (s02-05).

**Ký hiệu.** Deck dùng bảng ký hiệu của ghi chú: chỉ số cửa sổ $j$; số vòng $q$ trong bất biến tạo tập shingle; tập hàng đã quét $H$; chỉ báo $I_i$ và $\mathbf 1[E]$; ước lượng $\widehat s=\widehat{\mathrm{SIM}}(S,T)$; loại hàng $\mathrm X,\mathrm Y,\mathrm Z$; tên phần tử chữ đứng $\mathrm a,\ldots,\mathrm e$; hệ số hàm affine $\alpha,\beta$; hàm mã shingle $g$; $L=\operatorname{nnz}(M)$ và "biểu diễn theo hàng"; số lớn nhóm bằng khoảng trắng hẹp; "véc-tơ". Jaccard của Bài 01 là $\mathrm{SIM}$ (Định nghĩa 01.9). Trong ghi chú diễn giả, kết quả dẫn bằng số khối của ghi chú (Định nghĩa 05.2 … Nhận xét 05.23, Ví dụ 05.1 … 05.13, Tình huống 05.1–05.3, Bài tập 05.2 … 05.22).

**Nội dung thêm so với deck 2026-10-14** (đều từ ghi chú): Mệnh đề 05.6 (s02-10), Mệnh đề 05.4 tách tính đúng và chi phí (s02-11, s02-12), Bổ đề 05.9 (s03-10), Hệ quả 05.15 và Ví dụ 05.10 (s04-09), Mệnh đề 05.22 có chứng minh và ví dụ modulo 4 (s05-11), Nhận xét 05.23 và Tình huống 05.2 (s05-14), bảng hai biểu diễn của Ví dụ 05.1 (s01-05), trang "Lời giải:" cho bảy trang đề recitation.

**Thuật ngữ Anh thêm ở lần dùng đầu trên mặt trang:** near-duplicate (s01-04), indicator variable (s01-10), window (s02-01), $k$-gram (s02-03), loop invariant (s02-11), permutation (s03-04), rank (s03-06), unbiased (s04-04), signature matrix (s04-02).
