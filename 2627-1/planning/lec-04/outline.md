# Bài 04: PageRank theo chủ đề, liên kết rác và HITS

## Phạm vi của bản dàn bài mới

Ngày lập: 27/09/2026. Bản này thay thế toàn bộ dàn bài cũ theo yêu cầu của người dùng. Nội dung được xây lại từ đề cương và nguồn chi tiết; cấu trúc HTML, dàn ý, storyboard và báo cáo đạt của bản cũ không được dùng làm căn cứ thiết kế hoặc kiểm định bản mới.

Sản phẩm của yêu cầu này là ba tệp `outline.md`, `storyboard.md`, `review-log.md` trong thư mục hiện tại. Đây là kế hoạch nội dung, chưa phải bộ slide đã triển khai. HTML, SVG, ghi chú bài giảng, mã thực hành và mục tài nguyên hiện có không thuộc bước viết lại này. Quan hệ của chúng với kế hoạch mới được ghi trong nhật ký.

**Nguồn nền theo chỉ dẫn bổ sung của người dùng:** sách MMDS quyết định mạch bài, khái niệm, thứ tự lập luận, ví dụ và bài tập. Theo §5.3 → §5.4 → §5.5; slide của tác giả và các trường chỉ dùng để đối chiếu cách minh họa, không dùng làm khung thay cho sách.

Áp dụng kỹ năng `build-slide-deck-outline` tại `.agents/skills/build-slide-deck-outline/`, `no-ai-slop` và `quill`. Không khởi tạo dự án sách. Chỉ dùng tác tử gốc GPT-6-Astra, mức suy luận `xhigh`; không dùng OpenRouter.

- Số bài: 04 theo **Thứ tự đề xuất** của `sources/source.md`; ánh xạ buổi gốc 5.
- Chuẩn đầu ra trực tiếp: so sánh các thuật toán xếp hạng nút và phân tích ứng dụng, thuộc CLO2.
- Đối tượng: sinh viên năm 2, theo `AGENTS.md` và `slide_authoring_standard.md`; thay mặc định năm 3 của skill bằng căn cứ cụ thể này.
- Tiên quyết: Bài 03, đồ thị có hướng, nhân ma trận–vector, phân phối xác suất và phân tích chi phí. Không giả định đã học Jaccard, phân loại văn bản, hệ tìm kiếm chuyên dụng hoặc lý thuyết phổ nâng cao.
- Thiết kế: 48 slide giảng, 120 phút; 3 slide bài tập, 60 phút. Có 7 phần dọc; mỗi phần có một slide kiểm tra riêng.
- Nội dung trên slide và ghi chú dự kiến dùng tiếng Việt trang trọng, học thuật. Các quyết định bố cục, thời lượng, mã slide và lý do sư phạm chỉ thuộc hồ sơ nội bộ.

## Bài toán trung tâm và mục tiêu

Một đồ thị liên kết có thể cần phục vụ các nhu cầu khác nhau: xếp hạng theo chủ đề truy vấn, giảm tác động của liên kết thao túng, hoặc phân biệt trang cung cấp thông tin với trang dẫn tới nguồn thông tin. Một điểm PageRank toàn cục không biểu diễn đầy đủ ba nhu cầu này. Việc lưu một vector trên toàn bộ web cho từng người dùng còn đặt ra giới hạn bộ nhớ (MMDS §5.3.1, tr.195–196).

| Mã | Kết quả quan sát được | Bằng chứng đánh giá |
|---|---|---|
| MT1 | Lập phân phối dịch chuyển và tính PageRank theo chủ đề; phân biệt thay phân phối với thay đồ thị | S02-12; Bài 5.3.1 |
| MT2 | Truy nguyên từng đóng góp và giải phương trình điểm trang đích trong cụm thao túng | S03-08; Bài 5.4.1(a,c) |
| MT3 | Tính TrustRank, Spam Mass trên cùng mô hình và nêu giới hạn diễn giải | S04-07; S06-04 |
| MT4 | Lập ma trận HITS, cập nhật hai vector đúng chiều và đúng thứ tự; giải thích chuẩn hóa | S05-11; Bài 5.5.2 |
| MT5 | Chọn phương pháp theo đầu ra, giả thiết và chi phí trên đồ thị thưa | S06-03, S06-04; bảng so sánh cuối bài |

Các mã rút gọn Sxx-yy trong outline tương ứng `lec04-sxx-yy` trong storyboard. Chúng không thuộc nội dung hiển thị hay ghi chú diễn giả.

Ngoài phạm vi: SimRank, Pinterest/Pixie, hệ gợi ý Twitter, chi tiết phân loại chủ đề bằng Jaccard, triển khai công cụ tìm kiếm, mã thực hành mới và chứng minh phổ tổng quát. Bài 05 sẽ thiết lập Jaccard; không đưa tiên quyết ấy vào Bài 04. Nội dung HITS về danh sách học phần là tình huống của sách, không phải yêu cầu xây ứng dụng mới.

## Nguồn và vị trí kiểm chứng

Mọi số trang PDF trong bảng bắt đầu từ 1. Không phát hành lại PDF/PPTX hoặc hình raster của nguồn.

| Mã | Tài liệu và đường dẫn | Phần đã đọc; vai trò |
|---|---|---|
| NG0 | `sources/source.md`; `sources/reference-slides/README.md` | Bài đề xuất 4, buổi gốc 5, dòng ánh xạ 4; phạm vi và tiên quyết |
| NG1 | Leskovec, Rajaraman, Ullman, *Mining of Massive Datasets*, Chương 5; `sources/textbooks/mmds-3e-ch05-link-analysis.pdf` | §5.3–5.5, tr.195–208/PDF21–34; Hình5.1 tr.178/PDF4, Hình5.9 tr.189/PDF15. Nguồn chính cho định nghĩa, ví dụ và bài tập |
| NG2 | Slide MMDS phần 1; `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` | Đã kiểm kê toàn bộ 60 trang; kế thừa PageRank, biểu diễn thưa và bù nút cụt; không dạy lại phần Bài03 |
| NG3 | Slide MMDS phần 2; `sources/reference-slides/mmds/ch05-linkanalysis2.pdf` | Đã kiểm kê toàn bộ 60 trang; chủ đề 7–11, cụm thao túng 31–35, độ tin cậy 38–45, HITS47–60 |
| NG4 | Stanford CS246, Jure Leskovec và Charilaos Kanatsoulis, 05/02/2026; `sources/reference-slides/stanford-cs246/10-spam.pdf` | Đã kiểm kê toàn bộ 72 trang; chủ đề 5–14, cụm thao túng 51–55, TrustRank58–62, Spam Mass64–65; không có triển khai HITS |
| NG5 | Bài03, `2627-1/lecture-03-pagerank-mo-hinh-va-tinh-toan.html` | Đối chiếu các công thức $M_0$, $r^t$, $\beta$, $u$, $\delta^t$ và cách bù nút cụt; chỉ dùng để giữ tính liên tục |
| NG6 | Simone Teufel, Cambridge, *Information Retrieval, Handout Second Part*, Lent2012; [PDF chính thức](https://www.cl.cam.ac.uk/teaching/1112/InfoRtrv/lecture_slides2.pdf) | Đọc tr.65–85, xem trực tiếp tr.79–85 (PDF và số in trùng); chỉ đối chiếu cách dẫn nhập/cập nhật HITS, không thay mạch sách |

Nguồn trực tuyến: [MMDS](http://www.mmds.org/), [Stanford CS246](https://web.stanford.edu/class/cs246/), [slide Stanford được ánh xạ](https://web.stanford.edu/class/cs246/slides/10-spam.pdf). Trang MMDS bị hết thời gian chờ khi mở ngày 27/09/2026; ba PDF MMDS/Stanford cục bộ và chương sách đều đọc được. Tuyên bố ghi công MMDS đã kiểm trực tiếp ở trang đầu của PDF: bản triển khai phải có liên kết `http://www.mmds.org` khi sử dụng phần đáng kể.

## So sánh nguồn theo cụm và quyết định

| Cụm | Quan sát từ nguồn | Quyết định và lý do |
|---|---|---|
| Động lực | NG1 tr.195–196 dùng truy vấn “jaguar” đa nghĩa và giới hạn vector riêng từng người; NG4 tr.5–9 dùng “Trojan” | Chọn NG1 để nối ngữ cảnh với bộ nhớ; chỉ dùng nghĩa động vật và ô tô, không dựa vào sản phẩm phần mềm lịch sử |
| PageRank theo chủ đề | NG3 tr.7–11 và NG4 tr.9–14 có cùng cơ chế thay bước nhảy; hình NG3 tr.10 chứa đồng thời nhiều tập và nhiều giá trị $\beta$ | Ưu tiên MMDS. Chọn Hình5.15/VD5.10 của NG1 để giữ đồ thị A–D của Bài03; tách vết chạy và kết luận thay vì chép mật độ hình nguồn |
| Cụm thao túng | NG3 tr.33–35 và NG4 tr.53–55 cùng ba vùng trang, một đích và các trang hỗ trợ | Ưu tiên MMDS; tách kiến trúc, đóng góp và phương trình. NG1 tr.201 quyết định số hạng nào bị lược |
| TrustRank | NG3 tr.38–43 và NG4 tr.58–62 dùng hạt giống tin cậy và giảm ảnh hưởng theo đường đi | Chọn NG1 §5.4.4 làm đặc tả PageRank thiên lệch; không trộn công thức lan truyền một lần với phương trình lặp chuẩn hóa |
| Spam Mass | NG1 Hình5.17 ghép PageRank không dịch chuyển với TrustRank $\beta=0.8$; slide chỉ nêu công thức | Tính lại cặp cùng $\beta=4/5$, cùng đồ thị và cùng tổng1. Giữ công thức nguồn, ghi rõ bảng số dẫn xuất khác Hình5.17 |
| HITS | NG3 tr.50–58 cho trực giác hai chiều nhưng dùng nhiều cách chuẩn hóa; NG1 tr.205–207 có vết chạy hai vòng; NG4 không có cụm HITS | Ưu tiên MMDS, thống nhất chuẩn max của sách. Tách hình–vết chạy–ma trận–giả mã–chi phí; không sao khẳng định điểm giới hạn duy nhất vô điều kiện trên slide56 |

Cambridge NG6 tr.80–82 nối truy vấn với hai vai trò và tập trang cần xếp hạng; tr.83–84 tách công thức khỏi giả mã; tr.85 là bảng kết quả lịch sử dày. Chỉ học cách tách khối công thức–thuật toán. Không thêm tập gốc/tập cơ sở thành chủ đề mới vì sách mô tả HITS trực tiếp trên đồ thị đã chọn. Các trang đã xem chưa có vết số liên tục bằng VD5.15 của sách. Ký hiệu xác suất nhảy $\alpha$ ở Cambridge tr.71 không chuyển sang bài; giữ $\beta$ đi theo cạnh. Không dùng các kết quả lịch sử của tr.85 làm bằng chứng hiện hành.

Đánh giá độ phù hợp sư phạm trong cột quyết định là nhận định của người lập kế hoạch, không phải kết luận thực nghiệm của nguồn. Các nhận định lịch sử về DMOZ, tên miền hay công cụ tìm kiếm không được chuyển thành khẳng định về hệ thống hiện hành.

## Bản đồ chủ đề và quyết định hợp nhất

Tác tử lập kế hoạch và tác tử phân tích nguồn đề xuất độc lập trước bước soạn. Điều phối viên chấp nhận các mục dưới đây; không thêm chủ đề để tăng độ dài tài liệu.

| Chủ đề | Nhãn | Khoảng trống, đầu vào và vai trò | Quyết định; vị trí và đầu ra |
|---|---|---|---|
| Phân phối PageRank và chiều cạnh | Cầu nối | Cần kiểm lại tiên quyết Bài03 trước khi đổi bước nhảy | Giữ ngắn; S01 → S02 |
| PageRank theo chủ đề | Cốt lõi | Phân phối, đồ thị → điểm theo ngữ cảnh | Giữ NG1§5.3; S02 → TrustRank |
| Vector dịch chuyển tổng quát và bù nút cụt | Cầu nối | Công thức nguồn trên ví dụ không nút cụt chưa xác định cách bù của Bài03 | Thêm đặc tả tường minh giữ bù đều; S02-05 |
| Bảo toàn tổng, tính co và cận dừng | Bổ sung | Điều kiện dừng phải gắn với điểm cố định; phép tính vài vòng chưa chứng minh tính đúng | Thêm suy luận từ ma trận cột có tổng1 và $0<\beta<1$, dựa trên NG1§5.1.5,§5.3.2 và tiên quyết đại số; S02-07–08 |
| Cụm thao túng liên kết | Cốt lõi | Luồng điểm PageRank → cơ chế tăng điểm không do chất lượng | Giữ NG1§5.4.1–2; S03 → S04 |
| TrustRank và Spam Mass | Cốt lõi | Điểm theo tập hạt giống và mô hình tấn công → chỉ số để rà soát | Giữ NG1§5.4.3–5; S04 → so sánh |
| So sánh cùng mô hình | Bổ sung | Sai khác $\beta$ trong VD5.12 gây nhầm nguyên nhân thay đổi | Sửa bảng số bằng tính lại; S04-04–05 |
| Hai vai trò HITS | Cốt lõi | Tổng đóng góp theo cạnh → điểm trung tâm và điểm uy tín | Giữ NG1§5.5; S05 → MT4, MT5 |
| $M_0$ và $L^\mathsf T$; chuẩn hóa max | Cầu nối | HITS đổi hướng chỉ số và không chia bậc ra; tổng vector không là1 | Tách đối chiếu cụ thể NG1tr.205; S05-06–07 |
| Quan hệ vector riêng | Cốt lõi ở mức giới hạn | Giải thích điểm ổn định của phép lặp | Giữ phác thảo có điều kiện; không chứng minh lý thuyết phổ tổng quát; S05-09 |
| Chi phí theo cạnh | Bổ sung | Cần đối chiếu cùng mô hình, tránh tạo tích ma trận làm mất tính thưa | Phép đếm trực tiếp từ giả mã; S02-10, S05-10 |
| Jaccard và phân loại văn bản | Đọc thêm/chuyển bài | Phân loại không phải mục tiêu MT1; Jaccard chưa học | Chuyển cơ chế sang Bài05; chỉ giữ đầu vào chủ đề đã xác định |
| SimRank, Pixie, Twitter | Đọc thêm | Không khép khoảng trống của mục tiêu Bài04 | Bỏ khỏi tuyến120 phút; không có slide phụ ngầm |
| Lập trình HITS | Ngoài yêu cầu hiện tại | Hoạt động buổi gốc có cài đặt; yêu cầu hiện tại chỉ dàn bài | Không tạo mã hoặc một phần thực hành mới; giả mã và bài tập đủ kiểm cơ chế, hoạt động lập trình cần yêu cầu triển khai riêng |

Đồ thị tiên quyết: Bài03 → phân phối dịch chuyển → PageRank theo chủ đề → TrustRank → Spam Mass; luồng điểm Bài03 → cụm thao túng → nhu cầu đánh giá độ tin cậy; tổng theo cạnh → hai vai trò HITS → ma trận $L$ → cập nhật luân phiên → chuẩn hóa → quan hệ vector riêng và chi phí. Các nhánh gặp nhau ở lựa chọn phương pháp. Mở S03 chỉ rõ trở lại dịch chuyển đều trước khi đổi cạnh. Mở S05 xác định đồ thị đầu vào đã chọn và giới hạn tính hai vector trên đồ thị lớn; S05-10 thu hồi bằng hai lượt cạnh và tránh tạo tích ma trận có thể đặc hơn.

Giữ thứ tự §5.3 → §5.4 → §5.5. Đặt HITS ngay sau PageRank sẽ ngắt quan hệ bước nhảy theo chủ đề–TrustRank; đặt TrustRank trước cụm thao túng sẽ làm thiếu vấn đề cần giải quyết. Cơ chế Jaccard được lược cục bộ để không tạo tiên quyết ngược với Bài05.

## Bảy phần và phân bổ thời lượng

| Phần | Loại chính; mục tiêu | Đầu vào → kết quả chuyển tiếp | Slide | Phút | Kiểm tra riêng |
|---|---|---|---:|---:|---|
| S01. Bài toán xếp hạng liên kết | Giới thiệu và động lực; MT1, MT5 | PageRank Bài03 → nhu cầu theo chủ đề/độ tin cậy/vai trò | 6 | 12 | S01-06 |
| S02. PageRank theo chủ đề | Khái niệm, thuật toán, chi phí; MT1 | Ngữ cảnh truy vấn → vector bước nhảy và điểm ổn định | 12 | 30 | S02-12 |
| S03. Cơ chế liên kết rác | Mô hình và phân tích; MT2 | Quy tắc truyền điểm → phương trình khuếch đại | 8 | 20 | S03-08 |
| S04. TrustRank và Spam Mass | Thuật toán và diễn giải; MT3 | Hạt giống và cơ chế thao túng → chỉ số có giới hạn | 7 | 18 | S04-07 |
| S05. HITS | Thuật toán, ví dụ, chi phí; MT4 | Vai trò liên kết → hai vector và quy tắc cập nhật | 11 | 30 | S05-11 |
| S06. So sánh các phương pháp xếp hạng | Tổng hợp và kết luận; MT5 | Các phương pháp → lựa chọn theo đầu ra và giả thiết | 4 | 10 | S06-04 |
| S07. Bài tập | Luyện tập từ giáo trình; MT1, MT2, MT4 | Ba mô hình đã học → bài giải có thể kiểm chứng | 3 | 60 | S07-03 |

Tổng phần giảng: 48 slide/120 phút. Recitation: 3 slide/60 phút, gồm cả trình bày và đối chiếu lời giải. S07 đặt sau phần giảng trong cùng HTML ở bước triển khai. Một bài dài20 phút dùng một slide dữ kiện và yêu cầu, lời giải thuộc ghi chú; thời lượng không xuất hiện trên slide. Mốc48 nằm trong khoảng45–55 của tiêu chuẩn, không thêm slide để đạt chỉ tiêu.

## Thuật ngữ và ký hiệu thống nhất

| Ký hiệu/thuật ngữ | Nghĩa, miền và quy ước |
|---|---|
| $G=(V,E)$; $n=|V|$, $\ell=|E|$ | Đồ thị có hướng; đỉnh theo thứ tự đã nêu, cạnh không trọng số; khuyên chỉ khi nguồn có |
| $d_j$; $M_0$ | Bậc ra; $(M_0)_{ij}=1/d_j$ nếu $j\to i$, bằng0 nếu không; cột nút cụt bằng0. Cột là nguồn như Bài03 |
| $u$; $\delta^t$ | $u_i=1/n$; $\delta^t=\sum_{j:d_j=0}r_j^t$ |
| $\beta$ | Xác suất đi theo liên kết, $0<\beta<1$; ví dụ G4 dùng $4/5$, mô hình spam dùng $0.85$ theo nguồn |
| $S$, $v$ | Tập dịch chuyển không rỗng; $v_i=1/|S|$ khi $i\in S$, bằng0 nếu không. Tổng quát $v\ge0$, $\sum_i v_i=1$ |
| $r^t,r^*$ | Vector điểm cột ở vòng $t$ và điểm cố định; tổng1 |
| $\rho$; $T$ | Vector TrustRank; tập hạt giống tin cậy. Dùng $\rho$ để không nhầm $t$ là vòng lặp hoặc trang đích |
| $s_i$ | Spam Mass, $s_i=(r_i-\rho_i)/r_i$, chỉ định nghĩa khi $r_i>0$ |
| $L$ | Ma trận kề HITS, $L_{ij}=1$ khi $i\to j$; hàng là nguồn; không chia bậc ra |
| $h,a$ | Điểm trung tâm (hub) và điểm uy tín (authority); hai vector không âm, chuẩn hóa phần tử lớn nhất bằng1 |
| $\tau,K$ | Ngưỡng thay đổi giữa hai vòng và số vòng tối đa; dừng do hết $K$ không đồng nghĩa đã đạt ngưỡng |
| $k$; $K_j$ | Số chủ đề; số vòng thực chạy của phép tính vector chủ đề $j$, phân biệt với giới hạn vòng $K$ |
| $m,x,y$ | Số trang hỗ trợ, đóng góp từ ngoài đã nhân $\beta$, điểm trang đích; chỉ dùng trong mô hình cụm thao túng |

HITS được giới thiệu là thuật toán tìm kiếm theo chủ đề dựa trên siêu liên kết (HITS); giữ tên thuật toán ở các tiêu đề. “Uy tín” trong HITS là vai trò cấu trúc liên kết, không đồng nghĩa chứng nhận tin cậy của TrustRank.

## Đặc tả và mức hình thức hóa

### HT1. PageRank theo phân phối dịch chuyển

Đầu vào: danh sách cạnh $G$, $v$, $\beta$, $\tau>0$, $K\ge1$. Giữ quy ước bù đều của Bài03, độc lập với chủ đề:

$$r^{t+1}=\beta M_0r^t+\beta\delta^tu+(1-\beta)v.$$

Với đồ thị không nút cụt, $\delta^t=0$. Trên đồ thị tổng quát, đặt $z_j=\mathbf1[d_j=0]$ và $\bar M=M_0+u z^\mathsf T$. Vector $z$ chỉ báo nút cụt; $d_j$ vẫn chỉ bậc ra như Bài03. Khi đó $\bar M$ có tổng mỗi cột bằng1.

Thuật toán: khởi tạo $r^0=v$; đặt vector đóng góp bằng0; với mỗi cạnh $j\to i$ cộng $\beta r_j^t/d_j$; cộng $\beta\delta^tu+(1-\beta)v$; tính $\Delta=\|r^{t+1}-r^t\|_1$ rồi thay đồng thời vector cũ. Trả điểm hiện tại cùng trạng thái đạt ngưỡng nếu $\Delta\le\tau$, hoặc hết số vòng nếu đạt $K$. Đồ thị và $v$ cố định suốt phép lặp. Không dùng giá trị vừa cập nhật của một đỉnh để tính đỉnh khác trong cùng vòng.

### HT2. Bảo toàn và tính co

$\bar M$ không âm, mỗi cột tổng1. Nếu $r^t$ là phân phối, $r^{t+1}$ không âm và tổng $\beta+(1-\beta)=1$. Với $F(r)=\beta\bar Mr+(1-\beta)v$:

$$\|F(p)-F(q)\|_1\le\beta\|p-q\|_1.$$

Mặt S02-08 nhắc tính co trong một dòng và tập trung vào cận dừng từ tổng đuôi cấp số nhân. Chứng minh bằng bất đẳng thức tam giác và tổng cột nằm trong ghi chú. Các sai khác liên tiếp bị chặn bởi cấp số nhân; vì $\beta<1$, tổng đuôi tiến về $0$, dãy hội tụ và giới hạn thỏa phương trình. Nếu hai điểm cố định khác nhau, bất đẳng thức trên cho $D\le\beta D$, suy ra $D=0$. Đây là chứng minh ngắn, không viện dẫn tính liên thông mạnh hoặc giả thiết $v_i>0$ cho mọi đỉnh.

$$\|r^{t+1}-r^*\|_1\le\frac{\beta}{1-\beta}\|r^{t+1}-r^t\|_1.$$

Cận này là tổng phần đuôi cấp số nhân; không được đồng nhất thay đổi giữa hai vòng với sai số tới nghiệm. Các bước lập luận này là diễn giải toán học bổ sung từ phương trình nguồn, đã được điều phối viên chọn để hoàn thiện điều kiện dừng.

### HT3. Kết hợp chủ đề và chi phí

Với cùng $\bar M,\beta$, các trọng số $w_j\ge0$, $\sum_{j=1}^k w_j=1$ cho $v=\sum_jw_jv^{(j)}$ thì $r^*=\sum_jw_jr^{(j)}$. Chứng minh bằng thế tổng vào phương trình cố định và dùng HT2. Nếu thay ma trận hay $\beta$, kết luận tuyến tính này không được suy ra.

Mô hình: phép toán vô hướng chi phí đơn vị; đồ thị lưu danh sách cạnh. Một vector cần $\Theta(n+\ell)$ phép toán mỗi vòng: đọc $\ell$ cạnh, xử lý bù, dịch chuyển và kiểm tra trên $n$ đỉnh. Chạy đủ $K$ vòng cho một vector cần $\Theta(K(n+\ell))$; bộ nhớ đầu vào $\Theta(n+\ell)$, phụ $\Theta(n)$.

Tiền tính độc lập $k$ vector với số vòng thực chạy $K_j$ của chủ đề $j$ cần $\Theta((\sum_{j=1}^kK_j)(n+\ell))$ phép toán. Mỗi vector bị giới hạn $K$ vòng cho cận $O(kK(n+\ell))$. Nếu mọi vector đều chạy đủ $K$ vòng thì chi phí là $\Theta(kK(n+\ell))$. Tính tuần tự giảm trạng thái lặp cần giữ, không loại các phép lặp của từng chủ đề. Lưu $k$ kết quả cần $\Theta(kn)$ số; ghép điểm cho $c$ ứng viên cần $\Theta(kc)$ phép nhân–cộng. Đây là phép đếm từ giả mã, không phải số đo thời gian hoặc toàn bộ chi phí hệ tìm kiếm.

S02-11 thu hồi §5.3.3 theo bốn bước: chọn chủ đề → chọn tập dịch chuyển → xác định chủ đề truy vấn → sử dụng điểm. Trong phạm vi bài, chủ đề hoặc trọng số do người dùng cung cấp; không đưa Jaccard thành tiên quyết.

### HT4. Cụm thao túng

Giả thiết: toàn đồ thị không có nút cụt và dùng PageRank toàn cục với dịch chuyển đều. Trang đích chỉ trỏ tới $m\ge1$ trang hỗ trợ; mỗi hỗ trợ chỉ trỏ lại đích và chỉ nhận cạnh từ đích. Mọi cạnh ngoài vào cụm đều tới đích. Đại lượng $x$ là tổng đóng góp ngoài đã nhân $\beta$ và chia bậc ra tại từng nguồn. Đặt $b=(1-\beta)/n$. Điểm mỗi trang hỗ trợ $p=\beta y/m+b$. Phương trình chính xác:

$$y=x+\beta mp+b=x+\beta^2y+\beta mb+b.$$

Suy ra $y=[x+\beta mb+b]/(1-\beta^2)$. Khi bỏ riêng bước nhảy trực tiếp $b$ tới đích như NG1 tr.201:

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\frac mn.$$

Với $\beta=0.85$, hai hệ số lần lượt xấp xỉ $3.6036$ và $0.45946$. Hệ số đầu là nhân $3.6036$ lần, tương đương tăng khoảng $260.36\%$ so với $x$, không phải tăng $360\%$. Không kết luận mọi cấu trúc có nhiều liên kết là spam. Đây là phân tích mô hình, không phải một thuật toán cần giả mã riêng.

### HT5. TrustRank và Spam Mass

TrustRank dùng HT1 với $v$ tập trung trên $T$, các trang được xác định tin cậy từ thông tin ngoài cấu trúc đồ thị. Giả định vận hành: trang tin cậy ít trỏ tới trang rác; không là định lý hoặc bảo đảm phân loại.

Tính $r$ bằng bước nhảy đều, $\rho$ bằng bước nhảy trên $T$, cùng $G$, cách bù và $\beta$; chuẩn hóa tổng1. $s_i=1-\rho_i/r_i$ khi $r_i>0$. Giá trị có thể âm; không có cận dưới0 và không phải xác suất. Điểm gần1 gợi ý cần rà soát theo mô hình, không đủ kết luận một trang là rác. Hai phép lặp và phép chia theo đỉnh có cùng bậc chi phí với HT1, thêm chi phí chọn/kiểm hạt giống không được mô hình phép toán đồ thị bao phủ.

### HT6. HITS

Đầu vào: đồ thị có ít nhất một cạnh, $L$, $\tau>0$, $K\ge1$. Khởi tạo $h^0=a^0=\mathbf1$. Mỗi vòng tính $\tilde a=L^\mathsf Th^t$, $a^{t+1}=\tilde a/\max_i\tilde a_i$, rồi $\tilde h=La^{t+1}$, $h^{t+1}=\tilde h/\max_i\tilde h_i$. Dừng khi cả hai thay đổi theo chuẩn vô cùng không quá $\tau$; trả hai vector và trạng thái đạt ngưỡng/hết vòng. Nếu đồ thị không cạnh, mọi điểm thô bằng0, không được chia0; trả trạng thái không xác định theo quy ước chuẩn max.

Tính đúng của một vòng: với cạnh $i\to j$, điểm trung tâm $h_i$ được cộng vào uy tín $a_j$, rồi uy tín mới $a_j$ được cộng về trung tâm $h_i$. Hai vector không âm và max bằng1 sau chuẩn hóa; chuẩn hóa không đổi tỷ lệ hay thứ hạng trong từng vector. Hai điểm không phải xác suất và không phải hai loại đỉnh rời nhau.

Ở giới hạn, $h\propto LL^\mathsf Th$, $a\propto L^\mathsf TLa$. Một trị riêng lớn nhất đơn và khởi tạo có thành phần khác0 theo vector riêng tương ứng là điều kiện đủ cho hướng giới hạn duy nhất của phép lặp lũy thừa. Mặt S05-09 giữ các quan hệ tỷ lệ; điều kiện trị riêng được giải nghĩa trong ghi chú ở mức phác thảo và không trở thành đầu ra đánh giá chưa chuẩn bị. Không khẳng định mọi đồ thị đều có cùng điểm duy nhất độc lập khởi tạo. Bài tập chuỗi minh họa trực tiếp sự chi phối của thành phần lớn nhất mà không giải đa thức tổng quát.

Mỗi vòng quét cạnh hai lần, chuẩn hóa và so sánh các vector trên đỉnh: $\Theta(n+\ell)$ thời gian, $\Theta(n)$ bộ nhớ phụ, $\Theta(n+\ell)$ kể cả đầu vào. Không lập các tích $LL^\mathsf T,L^\mathsf TL$ để chạy: chúng có thể đặc hơn $L$. Nguồn: NG1 tr.205–208, NG3 tr.50–59; điều kiện phổ được ghi để giới hạn mệnh đề, không mở phần lý thuyết phổ mới.

## Phiếu ví dụ và kiểm chứng số

### VD1. PageRank theo chủ đề trên đồ thị G4

Nguồn: NG1 Hình5.15/VD5.10 tr.196–197, PDF22–23. Giữ nguyên dữ kiện. Thứ tự A,B,C,D; cạnh A→B,C,D; B→A,D; C→A; D→B,C. Không có khuyên, không có nút cụt; $n=4$, $\ell=8$.

| Đại lượng | Ký hiệu | Giá trị | Kiểu/đơn vị; vai trò |
|---|---|---|---|
| Đỉnh | A,B,C,D | Bốn nhãn chữ | Nhãn; tách khỏi giá trị điểm và số vòng |
| Bậc ra | $(d_A,d_B,d_C,d_D)$ | $(3,2,1,2)$ | Số cạnh; số2 lặp có chủ ý ở B,D |
| Đi theo cạnh | $\beta$ | $4/5$ | Xác suất |
| Tập dịch chuyển | $S$ | $\{B,D\}$ | Tập đỉnh |
| Phân phối dịch chuyển, khởi tạo | $v=r^0$ | $(0,1/2,0,1/2)^\mathsf T$ | Vector tổng1 |
| Bước nhảy được thêm | $(1-\beta)v$ | $(0,1/10,0,1/10)^\mathsf T$ | Điểm mỗi vòng |

$$M_0=\begin{pmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{pmatrix}.$$

Vết đầy đủ dùng trên các slide:

| Vòng | A | B | C | D | Tổng |
|---:|---:|---:|---:|---:|---:|
| 0 | $0$ | $1/2$ | $0$ | $1/2$ | $1$ |
| 1 | $1/5$ | $3/10$ | $1/5$ | $3/10$ | $1$ |
| 2 | $7/25$ | $41/150$ | $13/75$ | $41/150$ | $1$ |
| 3 | $31/125$ | $71/250$ | $23/125$ | $71/250$ | $1$ |
| Cố định | $9/35$ | $59/210$ | $19/105$ | $59/210$ | $1$ |

Vòng1: $M_0r^0=(1/4,1/4,1/4,1/4)^\mathsf T$; nhân $4/5$ rồi thêm vector bước nhảy. Vòng2 tại A: $(4/5)[(1/2)(3/10)+1(1/5)]=7/25$. Kiểm lỗi: dùng nhầm bước nhảy đều tạo $(1/4,1/4,1/4,1/4)$ ngay vòng1, khác kết quả đúng; bỏ hệ số1/2 của cạnh B→A làm A nhận $2/5$ thay vì $1/5$. Các giá trị bằng nhau ở B,D là hệ quả cấu trúc, không phải lỗi chọn số. Giữ số và bổ sung nhãn hàng/vòng cố định, không sửa đồ thị để làm các điểm khác nhau.

Ứng dụng lại: S02, S04 và Bài5.3.1; không đổi vị trí đỉnh qua các hình.

### VD2. Phân tích cụm thao túng

Nguồn: NG1 Hình5.16 và VD5.11 tr.200–201/PDF26–27, NG3 tr.33–35. Giữ đầy đủ giả thiết HT4: toàn đồ thị không nút cụt, dịch chuyển đều; đích chỉ trỏ các hỗ trợ, hỗ trợ chỉ nhận cạnh từ đích và chỉ trỏ lại đích; mọi cạnh ngoài vào cụm tới đích. Giữ mô hình ký hiệu, không tự đặt kích thước web hoặc số trang hỗ trợ.

| Đại lượng | Ký hiệu | Giá trị/miền | Kiểu và vai trò |
|---|---|---|---|
| Trang web tổng cộng | $n$ | $n\ge m+1$ | Số trang, mẫu số bước nhảy |
| Trang hỗ trợ | $m$ | $m\ge1$ | Số trang, mẫu số phần chia từ đích |
| Đóng góp ngoài | $x$ | Do các cạnh ngoài xác định | Điểm đã nhân $\beta$ |
| Điểm đích | $y$ | Ẩn của phương trình | Điểm, không là số trang |
| Điểm hỗ trợ | $p$ | $\beta y/m+(1-\beta)/n$ | Điểm của mỗi trang hỗ trợ |
| Tham số nguồn | $\beta$ | $0.85=17/20$ | Xác suất |
| Hai hệ số | $1/(1-\beta^2)$; $\beta/(1+\beta)$ | $400/111$; $17/37$ | Không thứ nguyên; xấp xỉ $3.6036$, $0.45946$ |

Vết: $y\to\beta y/m\to p\to\beta mp\to y$. Lỗi dễ mắc: đếm thêm $\beta x$ làm giảm đóng góp ngoài hai lần; bỏ số lượng $m$ khi cộng các hỗ trợ; dùng dấu bằng khi đã bỏ bước nhảy trực tiếp. Dữ liệu ký hiệu giúp theo dấu từng hệ số, không cần đặt số mới. Quyết định: giữ số nguồn và phân biệt vai trò bằng tên đại lượng.

### VD3. TrustRank và Spam Mass trên G4

Nguồn cơ chế NG1§5.4.4–5; phép áp dụng tính lại có chủ ý trên G4/VD1. Giữ $\beta=4/5$, $T=\{B,D\}$, tổng của hai vector bằng1. Bảng này **không phải bản chép Hình5.17**.

| Đỉnh | PageRank đều $r_i$ | TrustRank $\rho_i$ | Spam Mass $s_i$ |
|---|---:|---:|---:|
| A | $9/28$ | $9/35$ | $1/5$ |
| B | $19/84$ | $59/210$ | $-23/95$ |
| C | $19/84$ | $19/105$ | $1/5$ |
| D | $19/84$ | $59/210$ | $-23/95$ |

Vết tại A: $r_A-\rho_A=9/140$; $(9/140)/(9/28)=1/5$. Tại B: $r_B-\rho_B=-23/420$; chia hiệu này cho $19/84$ được $-23/95$. Lỗi đổi dấu cho $-1/5$ tại A; ép giá trị âm thành0 làm mất so sánh thực tế. Quyết định: giữ dữ kiện nguồn G4, tính lại cặp đồng nhất tham số; thêm nhãn vector để không nhầm số điểm với chỉ số.

### VD4. HITS trên G5

Nguồn: NG1 Hình5.18–5.20/VD5.14–5.15, tr.205–208/PDF31–34. Giữ nguyên đồ thị A–E: A→B,C,D; B→A,D; C→E; D→B,C; E không có cạnh ra. Đây là đồ thị khác G4: C→A được thay bằng C→E và có thêm E; không suy HITS bằng cách dùng lại ma trận PageRank G4.

| Đại lượng | Ký hiệu | Giá trị | Kiểu/vai trò |
|---|---|---|---|
| Số đỉnh/cạnh | $n,\ell$ | $5,8$ | Số lượng; tách khỏi điểm |
| Khởi tạo | $h^0$ | $(1,1,1,1,1)$ | Điểm trung tâm ban đầu, không tổng1 |
| Uy tín thô lần1 | $L^\mathsf Th^0$ | $(1,2,2,2,1)$ | Tổng theo cạnh vào |
| Uy tín lần1 | $a^1$ | $(1/2,1,1,1,1/2)$ | Chia max bằng2 |
| Trung tâm thô lần1 | $La^1$ | $(3,3/2,1/2,2,0)$ | Tổng uy tín mới theo cạnh ra |
| Trung tâm lần1 | $h^1$ | $(1,1/2,1/6,2/3,0)$ | Chia max bằng3 |
| Uy tín lần2 | $a^2$ | $(3/10,1,1,9/10,1/10)$ | Từ vector thô $(1/2,5/3,5/3,3/2,1/6)$ |
| Trung tâm lần2 | $h^2$ | $(1,12/29,1/29,20/29,0)$ | Từ vector thô $(29/10,6/5,1/10,2,0)$ |

Giới hạn kiểm số: $h\approx(1,0.3583,0,0.7165,0)$, $a\approx(0.2087,1,1,0.7913,0)$. Độ chính xác4 chữ số là cách hiển thị của nguồn, không là ngưỡng dừng của thuật toán. Lỗi dùng $M_0$ thay $L^\mathsf T$ sẽ cho vector thô $(1/2,5/6,5/6,5/6,1)$ ở lượt uy tín đầu, khác $(1,2,2,2,1)$; dùng $a^0$ thay $a^1$ để tính trung tâm làm vết chạy khác thuật toán đã đặc tả. Giữ số, thêm nhãn “thô/chuẩn hóa”, cùng thứ tự A–E. Các giá trị0,1 và B=C là nội dung cơ chế cần giữ.

## Đối chiếu cách tổ chức bố cục

Đã đọc [SLIDE_STYLE_GUIDE.md của uet-iai-course/machine-learning](https://github.com/uet-iai-course/machine-learning/blob/main/SLIDE_STYLE_GUIDE.md). Chỉ kế thừa một thành phần trung tâm trên mỗi trang, hình đủ lớn và chú thích nêu kết luận từ hình. Không kế thừa khuyến nghị viết như đang giảng; văn phong học thuật của yêu cầu hiện tại được ưu tiên. Không sao CSS, phông chữ hoặc tài sản từ kho tham khảo.

## Đặc tả hình và bố cục dùng chung

Chưa tạo SVG ở bước này. Mọi hình triển khai phải có `role="img"`, mô tả thay thế và tín hiệu ngoài màu. Chỉ tái sử dụng tài sản cũ sau khi đối chiếu lại từng cạnh và nhãn với đặc tả mới.

| Hình dự kiến | Đối tượng, nhãn và quan hệ | Slide dùng; kết luận thị giác |
|---|---|---|
| Truy vấn theo ngữ cảnh | Cùng từ “jaguar”, hai nhóm trang động vật/ô tô; không gán điểm giả | S01-03, S06-02; từ khóa không tự quyết định chủ đề |
| G4 và tập dịch chuyển | A trên trái, B trên phải, C dưới trái, D dưới phải; tám cạnh VD1; B,D có viền đôi và nhãn thuộc $S$ | S02-02–04, S04; giữ đồ thị, đổi bước nhảy |
| Ba vùng trang | Vùng không tác động được, tác động được, sở hữu; cạnh từ vùng tác động được tới đích; cặp cạnh đích–hỗ trợ | S03-02–05; phân biệt nguồn ngoài với tuần hoàn nội bộ |
| Đóng góp ở đích | Ba nhánh có nhãn $x$, $\beta mp$, $b$ | S03-04–05; phương trình có ba nguồn điểm |
| Danh sách và trang học phần | Một trang danh sách trỏ tới các trang học phần, theo VD5.13; không thêm số điểm | S05-01; trung tâm và uy tín là hai vai trò |
| G5 và vết HITS | Đồ thị nguyên Hình5.18; E dưới trái của C, C→E; bảng A–E giữ hàng qua hai lượt | S05-02–07; tổng đi vào khác tổng đi ra |
| Chuỗi Hình5.9 | Đỉnh1 có khuyên; cạnh1→2→…→n, đầu/cuối có nhãn | S07-03; khuyên thay đổi thành phần chi phối |

Bố cục kế thừa mẫu kỹ thuật và thành phần chung đã đọc ở Lecture02: `.title-slide`, `.agenda-slide`, `.example-slide`, `.ex-grid2`, `.ex-table`, `.ex-code`, `.math-large`, `.question-box`, `.cost-slide`. Khung1280×720; cỡ chữ theo CSS chung. Không sao khối `<style>` cũ trong template để ghi đè thang chữ; không dùng CSS riêng đã gắn với dàn bài04 cũ làm lý do giữ cấu trúc. Phiếu từng slide phải chỉ rõ vùng, tỷ lệ, thứ tự đọc, giới hạn nội dung và lý do phù hợp năm2.

## Bài tập nguồn và sản phẩm phải hoàn thành

### BT1. MMDS 5.3.1(a,b), tr.199/PDF25 — 20 phút

Đề dịch: Tính PageRank theo chủ đề của đồ thị Hình5.15 khi tập dịch chuyển là (a) chỉ A; (b) A và C. Giữ toàn bộ G4; dùng $\beta=0.8$ của VD5.10 ngay trước bài, nêu rõ tham số kế thừa vì câu đề không lặp lại. Được chia việc thành lập $v$, viết hệ và kiểm nghiệm; không thay tập đỉnh hoặc cạnh.

Sản phẩm: hai vector xác suất, hệ phương trình và phép kiểm tổng1/điểm cố định. Đáp án: (a) $(3/7,4/21,4/21,4/21)$; (b) $(27/70,6/35,19/70,6/35)$. Phân bổ: thiết lập3, tính12, đối chiếu5 phút. Tiêu chí: đúng tập bước nhảy, đúng chiều ma trận, nghiệm thỏa phương trình; không chỉ chấm tổng1.

### BT2. MMDS 5.4.1(a,c), tr.203–204/PDF29–30 — 20 phút

Đề dịch: Lặp lại phân tích cụm thao túng Hình5.16 khi (a) mỗi trang hỗ trợ chỉ trỏ tới chính nó thay vì trang đích; (c) mỗi trang hỗ trợ trỏ tới cả chính nó và trang đích. Giữ các cạnh ra của trang đích, điều kiện toàn đồ thị không có nút cụt, không có cạnh từ ngoài cụm vào các hỗ trợ và ký hiệu nguồn. Các hỗ trợ được nhận thêm cạnh từ chính nó theo khuyên của mỗi biến thể; không giữ điều kiện chỉ nhận cạnh từ đích của mô hình gốc. Lược ý(b) về trang hỗ trợ không có liên kết ra để không mở thêm một bài về quy ước bù nút cụt; điều chỉnh phạm vi, không đổi dữ kiện hai ý giữ lại.

Sản phẩm: phương trình điểm hỗ trợ và điểm đích, biểu thức theo $x,m,n,\beta$, nêu chính xác hay xấp xỉ. Theo cách bỏ bước nhảy trực tiếp tới đích của §5.4.2:

- (a) $p=\beta y/m+\beta p+b$; không còn dòng hỗ trợ về đích, $y\approx x$.
- (c) $p=\beta y/m+\beta p/2+b$, $y\approx x+\beta mp/2$; suy ra $y\approx(2-\beta)x/[(1-\beta)(2+\beta)]+\beta m/[(2+\beta)n]$.

Nếu giữ bước nhảy trực tiếp: (a) $y=x+b$; (c) $y=[(2-\beta)(x+b)+\beta mb]/[(1-\beta)(2+\beta)]$. Hai cách được chấp nhận khi ghi nhất quán giả thiết. Phân bổ: mô hình4, biến đổi11, đối chiếu5 phút. Tiêu chí: đúng số cạnh ra của trang hỗ trợ, không nhân $\beta$ hai lần vào $x$, phân biệt mô hình xấp xỉ.

### BT3. MMDS 5.5.2, tr.208/PDF34; Hình5.9 tr.189/PDF15 — 20 phút

Đề dịch: Với chuỗi $n$ đỉnh như Hình5.9, tính các vector trung tâm và uy tín theo $n$. **Hình nguồn có khuyên tại đỉnh đầu**: $1\to1$ cùng chuỗi $1\to2\to\cdots\to n$. Không được thay bằng chuỗi không khuyên. Dùng khởi tạo toàn1 và chuẩn max đã học.

Với $n\ge2$, $LL^\mathsf T=\operatorname{diag}(2,1,\ldots,1,0)$. Sau $t\ge1$ vòng, $h^t=(1,2^{-t},\ldots,2^{-t},0)$; vì thế $h^*=(1,0,\ldots,0)$, $a^*=(1,1,0,\ldots,0)$. Khi $n=2$, phần giữa rỗng và giới hạn đạt ngay. Khi $n=1$, chỉ còn khuyên, $h=a=(1)$. Sản phẩm: hai vector theo $n$, chứng minh từ hai cập nhật hoặc ma trận đường chéo và xử lý biên. Phân bổ: lập ma trận4, suy luận11, đối chiếu5 phút. Tiêu chí: giữ khuyên; đúng hướng cạnh; giải thích chuẩn max; phân biệt biên1 và2. Đây là slide kiểm tra riêng của S07, thời lượng tính đúng một lần.

Chọn BT3 thay 5.5.1 vì nghiệm HITS trên G4 cần lặp số hoặc giải đa thức bậc ba; bài chuỗi cho lời giải đầy đủ bằng tay trong20 phút. Không biến bài “tính vector” thành chỉ tính hai vòng rồi coi đã xong.

## Mạch cụm và các bước được gộp

| Cụm | Tình huống → trực giác → ví dụ → hình thức → thuật toán/lập luận → chi phí → kiểm tra |
|---|---|
| PageRank theo chủ đề | S01-03–04 → S02-01 → S02-02–04 → S02-05 → S02-06–08 → S02-09–11 → S02-12 |
| Cụm thao túng | S03-01 trở lại PageRank toàn cục với dịch chuyển đều, chỉ thay cạnh → S03-02 → S03-03–04 → S03-05 → S03-06–07 → S03-08; không có thuật toán thực thi riêng, phương trình cân bằng và giới hạn mô hình thay bước giả mã |
| TrustRank/Spam Mass | S03-08 → S04-01–02 → S04-03–05 → HT5 được gắn vào S04-02,05 → tái dùng HT1, không lặp giả mã → S04-06 → S04-07 |
| HITS | S05-01 xác định đồ thị đầu vào đã chọn, hai vector và nhu cầu lặp theo cạnh trên đồ thị lớn → S05-02 → S05-03–05 → S05-06–07 → S05-08–09 → S05-10 → S05-11 |

Bản đồ này cho phép ví dụ xuất hiện trước ma trận tổng quát trong slide. Phiếu bố cục, nội dung hiển thị, diễn giải học thuật và đáp án cụ thể nằm trong `storyboard.md`. Báo cáo nguồn, các quyết định sửa lỗi và bằng chứng kiểm định nằm trong `review-log.md`.

## Trạng thái triển khai bản nháp ngày 28/09/2026

Bản triển khai giữ nguyên 51 phiếu và bảy phần đã duyệt, phân bố 6/12/8/7/11/4/3. Đã dựng lại HTML, 51 ghi chú diễn giả và 20 SVG qua `img/lec-04/scripts/render_figures.py`. Ghi chú tự học đã được đồng bộ trong `materials/lec-04/lecture-note.md`; thẻ Bài 4 chỉ liên kết deck và ghi chú. Các tệp thực hành cũ được giữ nguyên nhưng không còn được thẻ Bài 4 hoặc ghi chú mới giới thiệu là tài nguyên đã kiểm định của bản này.

Mục tiêu của ghi chú là cho phép người học tự lập đặc tả, tái tạo các vết số và hoàn thành lập luận từ mô hình tới kết quả. Vấn đề trung tâm giữ nguyên: thay thông tin ưu tiên hoặc ý nghĩa điểm để đáp ứng ba yêu cầu xếp hạng. Các chủ đề tự học được ánh xạ bằng `note-topic-id` ở phụ lục triển khai của storyboard; không thêm nhánh ngoài bản đồ chủ đề đã duyệt.

| Chủ đề đã duyệt | Vị trí ghi chú | Quyết định triển khai |
|---|---|---|
| Tiên quyết PageRank, chiều cạnh, nhu cầu chủ đề | §1–2.1 | Giữ; định nghĩa trước ví dụ cho tài liệu tự học |
| PageRank theo chủ đề, bù nút cụt, bảo toàn, co và dừng | §2.2–2.4 | Giữ và triển khai đầy đủ các bổ sung đã duyệt |
| Kết hợp vector và chi phí theo cạnh | §2.5 | Giữ; phân biệt số vòng thực $K_j$ với giới hạn $K$ |
| Cụm thao túng, chính xác và xấp xỉ | §3 | Giữ; đủ giả thiết trước phương trình, không tạo thuật toán giả cho mô hình đại số |
| TrustRank, cùng mô hình và Spam Mass | §4 | Giữ; cùng $\beta=4/5$, giữ giá trị âm và giới hạn diễn giải |
| Hai vai trò, ma trận, chuẩn hóa và HITS | §5.1–5.4 | Giữ; định nghĩa phép cập nhật trước vết chạy của tài liệu tự học |
| Quan hệ vector riêng, chi phí | §5.5–5.6 | Giữ phác thảo có điều kiện và phép đếm hai lượt cạnh |
| Lựa chọn và ba bài tập nguồn | §6–7 | Giữ; thay các bài cũ bằng bộ ba đã duyệt, lời giải đọc độc lập |

Ký hiệu và đồ thị tiên quyết dùng bảng thống nhất hiện có. Chứng minh trong ghi chú mở rộng các bước quyết định, không thêm chứng minh phổ tổng quát. Các đoạn kết nối chỉ nêu kết quả được kế thừa, giả thiết đổi và giới hạn; không chứa chỉ dẫn điều phối lớp. Đây là trạng thái có bản nháp để rà, chưa xác nhận hoàn thành năm lượt rà độc lập hoặc phát hành.

## Chỉnh sửa cục bộ sau năm lượt rà bản triển khai ngày 28/09/2026

Điều phối viên đã hợp nhất năm báo cáo độc lập về bản HTML, SVG, notes và ghi chú tự học trước khi giao editor riêng. Giữ nguyên 51 trang, bảy phần, thời lượng 120 + 60 phút, 13 chủ đề tự học và tuyến MMDS §5.3 → §5.4 → §5.5.

| Phạm vi | Quyết định và căn cứ | Ảnh hưởng tới mạch |
|---|---|---|
| S01-04; `lec04-note-01` | Giữ tình huống lưu trữ; khôi phục quy mô minh họa có sẵn tại MMDS §5.3.1, tr.195–196: khoảng một tỷ người dùng, mỗi vector có nhiều tỷ thành phần. Không dùng như số đo hiện hành. | Làm rõ giới hạn bộ nhớ trước phương án lưu vector chủ đề; chi phí theo số chủ đề vẫn ở S02-10. |
| S02-01; S03-02; `lec04-note-05` | Sửa mô tả đích của nhánh liên kết; hình kiến trúc dùng “Đóng góp từ ngoài”, còn $x$ được định nghĩa tại S03-04. | Khôi phục đúng chiều nguồn–đích và tránh ký hiệu xuất hiện trước định nghĩa; giữ mọi cạnh. |
| S04-02/03; S05-02/06 | Dẫn định nghĩa TrustRank về §5.4.4; G5/Hình 5.18 về §5.5.2, Ví dụ 5.14; ma trận/Hình 5.19 về §5.5.2. | Chỉ sửa đường tra nguồn, không đổi nội dung hoặc thứ tự. |
| S05-05/07/08; `lec04-note-09` | Văn xuôi dùng “giá trị lớn nhất” và “chuẩn hóa bằng giá trị lớn nhất”; giữ toán tử trong công thức/giả mã. | Giữ quy ước chuẩn hóa và trạng thái đồ thị không cạnh. |

Hai sửa viewer được duyệt riêng gồm giới hạn phần tử định vị trong bảng cuộn và cho mọi hình của học phần co vừa giấy khi in. Không thay mô hình, thuật toán, dữ kiện, bài tập hoặc nội dung ngoài Bài 04. Nhật ký ghi đầy đủ từng báo cáo, quyết định và giới hạn kiểm định còn lại.
