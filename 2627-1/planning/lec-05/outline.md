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

50 trang phần giảng gồm cả mở đầu và kiểm tra, tổng 120 phút; 7 trang bài tập cho 5 bài nguồn, tổng 60 phút. Số trang cho phép giữ ví dụ, chứng minh và vết cập nhật ở cỡ chữ chung, không dùng trang trang trí. Không có phần cài môi trường hoặc notebook vì phạm vi nguồn không yêu cầu. Tăng tốc ở §§3.3.6–3.3.7 chỉ thuộc ghi chú đọc thêm, ngoài 120 phút.

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
| Bài toán gần trùng, phép đếm cặp | B tr. 73–76 | Giữ, 04–05; thu hồi tại 33,47–48 |
| Jaccard, Hình 3.1 | B §3.1.1 tr. 74–75 | Giữ và vẽ lại SVG, 06–09 |
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

## 5. Mạch giảng và bản đồ bảy phần

| Phần | Loại, sản phẩm và kết nối | Trang | Phút | Kiểm tra |
|---|---|---|---:|---|
| 1. Giới thiệu và tương đồng tập hợp | Giới thiệu + khái niệm; kho gần trùng → Jaccard cần một biểu diễn tập | 01–09 | 18 | 09 |
| 2. Shingling văn bản | Khái niệm + thuật toán; chuỗi → tập phần tử để nén | 10–18 | 22 | 18 |
| 3. MinHash theo hoán vị | Khái niệm + chứng minh; tập → một phép thử có xác suất trùng bằng Jaccard | 19–27 | 22 | 27 |
| 4. Chữ ký MinHash | Ước lượng; một phép thử → tỷ lệ nhiều phép thử và tác dụng của $n$ | 28–34 | 17 | 34 |
| 5. Tính chữ ký và giới hạn | Thuật toán + chi phí; băm hàng → chữ ký tính được, bất biến và giới hạn | 35–46 | 31 | 46 |
| 6. Tổng kết | Thu hồi tình huống; kết nối biểu diễn, bảo đảm và giới hạn số cặp | 47–50 | 10 | 49–50 |
| 7. Bài tập vận dụng | 5 bài nguồn, riêng sau phần giảng | 51–57 | 60 | 56–57, Bài 3.3.3 |

Mỗi phần tương ứng một `section` ngoài. Phần bài tập có 7 trang nhưng chỉ 5 bài; việc tách Bài 3.3.1 và 3.3.3 không nhân thời lượng. Không có phần đọc thêm trên mặt deck; ghi chú tự học đánh dấu nhánh đọc thêm riêng.

| Cụm trọng tâm | Tám bước học tập và trang thực hiện | Dữ liệu được truyền và quyết định gộp |
|---|---|---|
| Jaccard | Tình huống 04; vấn đề 05; trực giác/ví dụ 06; hình thức 07; ứng dụng 08; kiểm tra 09 | Giao 3, hợp 8 truyền từ hình sang công thức. Không có thuật toán riêng vì phép đếm tập là tiên quyết; chi phí mọi cặp đặt ở 05 |
| Shingling | Tình huống/vấn đề/trực giác 10; ví dụ 11; hình thức 12; thuật toán và đúng 13; ứng dụng/chi phí 14–17; kiểm tra 18 | `abcdabd`, $k=2$, sáu cửa sổ, năm phần tử giữ nguyên. 13 gộp bất biến ngắn; chứng minh đầy đủ vào ghi chú |
| MinHash | Tình huống/vấn đề 19; biểu diễn 20–21; trực giác 22; ví dụ 23; hình thức 24; lập luận đúng 25–26; kiểm tra 27 | Cùng bốn tập Hình 3.2; thứ tự `b, e, a, d, c`. Chi phí lưu hoán vị chuyển 35 vì chỉ khi đó cần triển khai; 19 đã đặt giới hạn bộ nhớ |
| Chữ ký | Nhu cầu nhiều phép thử sau 27; ví dụ 28; hình thức 29–30; chứng minh kỳ vọng/phương sai 31–32; chi phí 33; kiểm tra 34 | Hai thứ tự suy từ Ví dụ 3.8 dùng trước định nghĩa, quyết định riêng của root. Thuật toán tích lũy chữ ký thực hiện ở cụm kế; không bỏ ngầm |
| Quét hàng | Tình huống/vấn đề/trực giác 35; đặc tả 36; ví dụ 37–40; thuật toán 41; đúng 42; chi phí 43–44; giới hạn 45; kiểm tra 46 | Đổi công khai a–e sang 0–4; giữ toàn bộ dữ kiện và vết min Hình 3.4. Đặc tả trước vết chạy đầy đủ vì MinHash và cực tiểu đã có trực giác tại 22–24 và 35 |

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
