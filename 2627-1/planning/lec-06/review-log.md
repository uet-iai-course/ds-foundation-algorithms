# Nhật ký rà soát Bài 06: Tìm cặp tương đồng bằng LSH

## Trạng thái và phạm vi ngày 28-09-2026

Đây là nhật ký mới của lượt viết lại toàn bộ Bài 06 đã được người dùng xác nhận. Không kế thừa tuyên bố hoàn tất của bản cũ. Pha 1 thay `outline.md`, `storyboard.md` và tệp này từ đầu. Pha 1 chỉ sửa ba kế hoạch. Sau gate PASS và chấp nhận của điều phối viên, pha 2 đã có bản nháp HTML, ghi chú, SVG và cập nhật mục Bài 06 trong index. Chưa commit hoặc push. Đã nhận đủ năm báo cáo độc lập và hoàn tất lượt editor riêng; tái rà toán/mạch/học thuật cùng QA cuối vẫn còn.

Phạm vi bài là MMDS 3e §§3.4–3.8, tr.91–122, theo thứ tự đề xuất trong `sources/source.md`; Bài 06 nhận một phần buổi gốc 12. Sách là sườn. Người học năm 2, 120 phút giảng và 60 phút bài tập. Bài 05 tại commit `5530bd6` chỉ được dùng cho ký hiệu và Ví dụ 3.8. Không đọc lại hay lấy kế hoạch, HTML, ghi chú Bài 06 cũ làm khuôn.

## Phân công và chứng cứ quy trình

| Tác tử/vai trò | Đầu vào và việc được giao | Đầu ra, quyết định tiếp nhận | Cấu hình mô hình được chỉ định |
|---|---|---|---|
| Điều phối viên `/root` | Tiếp nhận yêu cầu; xác định phạm vi; hợp nhất ba đề xuất độc lập; khóa miền và ký hiệu | Chấp nhận sườn sách, cấu trúc 7 phần, 120+60, bản đồ N01–N15, chi phí và dịch Euclid; chấp nhận dự toán 53+7 trang; kiểm định tiếp sau writer | Cơ chế native của phiên; không dùng lời tự khai làm bằng chứng model thực chạy |
| `lec06_plan`, lập kế hoạch chỉ đọc | Source map, nguồn chi tiết, tiêu chuẩn, UI; không đọc học liệu cũ Bài 06 | Hồ sơ đề xuất mục tiêu, mạch, chủ đề, bố cục và 51 trang dự toán; root chọn cấu trúc 7 phần và thời lượng của hồ sơ này | GPT-6-Astra, reasoning xhigh theo cấu hình được điều phối viên chỉ định; chưa có metadata runtime độc lập trong hồ sơ writer |
| `lec06_sources`, phân tích nguồn và toán chỉ đọc | Sách đầy đủ §§3.4–3.8, ba PDF slide, ký hiệu và dữ kiện Bài 05 | Kiểm kê nguồn, vết chạy, bài tập, mô hình Q/K, sửa sai giả thiết; root chấp nhận có hiệu chỉnh ghi bên dưới | GPT-6-Astra, reasoning xhigh theo cấu hình được điều phối viên chỉ định; không coi tự khai là bằng chứng runtime |
| `lec06_external`, đối chiếu và bản đồ chủ đề độc lập, chỉ đọc | MMDS/Stanford, nguồn UMass, Datar; cùng phạm vi | Đối chiếu ba bộ slide đại học ở hai trường, đề xuất nguồn dịch biên, bản đồ chủ đề; root hợp nhất trước writer | GPT-6-Astra, reasoning xhigh theo cấu hình được điều phối viên chỉ định; không có bằng chứng runtime bổ sung trong hồ sơ writer |
| `lec06_writer`, tác tử soạn duy nhất pha 1 | Các quyết định đã được root chấp nhận và nguồn gốc; chỉ được ghi ba tệp quy trình | Outline mới, 60 phiếu trang, kiến trúc notes N01–N16, lời giải recitation, log; dừng trước pha 2 | GPT-6-Astra, reasoning xhigh được chỉ định trong giao việc; không suy model runtime từ lời tự khai |
| `lec06_gate`, kiểm định storyboard chỉ đọc | Ba tệp pha 1, nguồn và chín phát hiện của điều phối viên | Lượt kiểm đầu CHƯA ĐẠT; lượt tái kiểm PASS, còn bốn điểm nhẹ E01–E04 đã được writer sửa và root xác nhận | GPT-6-Astra, reasoning xhigh qua cơ chế native theo giao việc; không suy model thực chạy từ lời tự khai |

Các hồ sơ nguồn ban đầu ở thư mục tạm là chứng cứ tiếp nhận, không phải nơi duy nhất giữ quyết định. Danh mục nguồn, so sánh theo cụm, ví dụ, số đã kiểm, sai khác, bản đồ chủ đề và lời giải đã được chuyển vào ba tệp quy trình bền vững. Không gọi OpenRouter, API/CLI mô hình, không đọc `.env` hoặc bí mật. Không có tác tử viết song song. Script tính số và sinh tài liệu chỉ là xử lý cục bộ xác định, không là tác tử hoặc lời gọi mô hình.

## Nguồn, mức độ kiểm kê và giới hạn truy cập

| Phạm vi | Bằng chứng đọc/quan sát trong hồ sơ độc lập và writer | Kết luận, giới hạn |
|---|---|---|
| Bài và tiên quyết | `sources/source.md`: dòng 6 mục tiêu/học liệu/thứ tự, quan hệ 05→06→07; dòng 6 `reference-slides/README.md` | Khớp bài 06, dùng Bài 05 rồi bổ sung độ đo trước họ; nguồn cục bộ đầy đủ |
| Sách B | 63 trang PDF; toàn văn §§3.4–3.8 tr.91–122/PDF 20–51 đã được tác tử nguồn đọc; ảnh PDF 22,39,41,43,50 đối chiếu hình/bài tập. Writer mở lại §§3.4 và các trang đề 3.4.1–2,3.6.1,3.7.1–5,3.8.2/Ex 3.24 | Trang in=PDF+71; nguồn cho toàn sườn và bài tập. Không chỉ dùng slide để xác nhận định lý |
| MMDS M | 59 trang đã kiểm kê toàn văn; ảnh 45–46,54–57; writer mở lại 44–47 | Bản cục bộ dùng cho phân dải; trang MMDS HTTP/HTTPS timeout và `/slides.html` không mở được trong lượt đối chiếu. Vẫn ghi công `http://www.mmds.org` |
| Stanford S3/S4 | 54/60 trang đã kiểm kê toàn văn; ảnh được liệt kê trong outline; writer mở lại S3 PDF 39–40, S4 PDF 19–20 và trực tiếp ảnh PDF 19 | Chọn Stanford cho pháp tuyến/vùng góc vì quan hệ rõ hơn. Ảnh PDF 19 có ≤/≥; OCR đọc thành </> bị bác |
| UMass U | COMPSCI 514 Lecture 9 Fall 2021,16 trang; đọc toàn bộ và xem PDF 3,5,10–14 | Đủ đối chiếu trường thứ hai. Học cách gắn xác suất với số ứng viên; không lấy ví dụ âm thanh hay bố cục PDF 13 sát mép |
| Datar D | SoCG 2004, §3.2, PDF 3 đã đọc và xem ảnh trong hồ sơ đối chiếu, root xác nhận phạm vi | Chỉ lấy dịch đều và lượng tử hóa; chứng minh cận hai chiều của bản soạn không gán cho bài báo p-stable |
| Kho giao diện tham khảo | Template, CSS, Lecture 02, index được đọc. Hồ sơ điều phối ghi checkout `uet-iai-course/machine-learning` không có cục bộ | Không tuyên bố đã xem checkout thiếu. Dùng nguyên tắc đã có trong tiêu chuẩn: một luận điểm, hình/công thức lớn, nhịp cơ chế–ví dụ–kiểm tra; không sao chép CSS/assets khác |
| Render | Điều phối viên chuẩn bị kiểm local Chromium/Reveal và phương án Codex Slides nhập ảnh/notes xác định | Pha 1 chưa render học liệu mới. Nếu Codex Slides gặp giới hạn, ghi đúng fallback cục bộ; không tuyên bố đã rà Codex Slides trước bằng chứng |

Mục tiêu đối chiếu của skill đạt bằng S3, S4, U tại Stanford và UMass, cộng MMDS bắt buộc. Datar là bài báo gốc bổ sung giả thiết, không tính thành bộ slide đại học. Các raster/PDF tải để đọc nguồn chỉ nằm tạm, không là tài sản phát hành.

## Quyết định hợp nhất chủ đề và sai khác cấu trúc

| Vấn đề hoặc đề xuất độc lập | Quyết định trước khi soạn | Lý do và tác động |
|---|---|---|
| Planner đề xuất 7 phần với 6 phần giảng riêng; source/external đề xuất gộp ứng dụng và kết luận | Giữ cấu trúc planner:8+32+30+26+16+8=120, recitation 60 | Mở đầu và kết luận có chức năng rõ; độ đo+họ được gộp hợp lý trong phần 3; vẫn đúng thứ tự sách |
| Dự toán khoảng 51 trang | Tách thành 53 trang giảng, 7 trang bài tập | Dải 1/dải 2/xác minh tách trạng thái; các độ đo giữ trang riêng; định nghĩa/chứng minh/xác suất không chen cùng trang. Root chấp nhận 53+7; không dùng mốc 45–55 như quota |
| N02 thiếu hợp đồng đầu ra và khử lặp trong slide tham khảo | Thêm đặc tả, bất biến, biên và kiểm gốc trực tiếp | Khép khoảng trống giữa thủ tục nhóm và kết luận đầu ra. Đây là diễn đạt/suy luận từ §3.4, không thuật toán ngoài nguồn |
| N04 mô hình Q/K | Thêm đã duyệt | Nguồn không biểu thức hóa đủ chi phí đầu ra; chống kết luận tuyến tính vô điều kiện. Sao chép tuple để bộ nhớ khớp giả mã |
| Các bản đồ chủ đề dùng tên/mã khác nhau | Hợp nhất N01–N15 theo planner; thêm N16 riêng cho đề/lời giải | Nguồn ngẫu nhiên của external gộp vào N06; dịch đều gộp vào N10; bất biến nguồn gộp vào N02. Không phát triển thêm nội dung chỉ để bao danh mục |
| Cận Euclid thiếu dịch | Thêm giả thiết có nguồn và chứng minh sơ cấp | Datar cho cơ chế dịch; MMDS cho hướng hai chiều; cận giữ trong hai chiều. Không mở rộng sang p-stable |
| N15 nhiều đề xuất | Chọn triển khai gọn Bài 3.7.5(d) và mô hình ngày §3.8.3; các mục khác chỉ là chỉ dẫn nguồn | Không làm tiên quyết cho bài tập bắt buộc; tránh kéo dài notes. Ghép 256, MapReduce, đạo hàm, mở rộng Euclid chỉ chỉ dẫn đọc |
| Các hồ sơ đề xuất recitation khác nhau | Chọn đúng R1–R6 của root:18+10+6+10+8+8=60 | Giữ 3.4.1–2 đầy đủ; giữ 3.6.1(a–d); thêm cả 3.7.1 và 3.7.2; giữ 3.7.5(a–c); dùng 3.8.2 thay 3.8.1 |
| Bài 3.7.5 trùng ví dụ giảng | Giảng chỉ trục 1, a=1; recitation vẫn đủ ba trục, a=1,2 | Không giải sẵn toàn bộ bài trước recitation; phần (d) chuyển đọc thêm có lý do |
| §3.9, HNSW, PQ, RAG, notebook | Chuyển khỏi phạm vi Bài 06 | Theo source.md và yêu cầu sách làm sườn; không có mã trình diễn bắt buộc |

## Sai khác nguồn và sửa toán học đã khóa

| Vị trí nguồn/vấn đề | Bằng chứng hoặc phép kiểm | Quyết định và vị trí thực hiện |
|---|---|---|
| B 3.6.1 “for every f” | Hàm cố định cho kết quả xác định, còn xác suất trên lấy hàm | Cặp $x,y$ cố định;$h\sim\mathcal H$ theo phân phối. HT6, N06, s03-07 |
| S4 PDF 19 OCR</> | Ảnh có ≤/≥, writer xem trực tiếp | Bác ghi chú OCR trong source-dossier; dùng ≤/≥ như sách, giữ miền giữa không ràng buộc |
| Miền MinHash/góc | Xác suất phải trong [0,1] | Tổng quát MinHash chỉ $0\le d_1<d_2\le1$; họ góc radian chỉ $0\le d_1<d_2\le\pi$. Ghi chú N06, N09 |
| “Trùng thùng” và trùng tuple | Va chạm băm khóa khác tuple có thể sinh thêm cặp | Khóa đầy đủ $(j,tuple)$, giải va chạm bằng so khóa. Không ghép cùng tuple ở dải khác. HT1 |
| B 3.4.3 bước 6 kiểm chữ ký; bước 7 kiểm gốc được ghi tùy chọn | Lọc $\widehat s$ trước Jaccard có thể thêm bỏ sót | Biến thể đã duyệt bỏ bước 6, bắt buộc kiểm gốc trực tiếp trên mọi ứng viên duy nhất. Sửa xuất xứ theo MF07; không nhận tìm đủ cặp thật |
| Đường xác suất và ngưỡng | Với $r=1$ đường lõm;$b=1$ đường lồi; nghiệm $P=1/2$ khác $b^{-1/r}$ | Gọi đường xác suất; chốt $t,s_{1/2},b^{-1/r}$ riêng; không trộn điểm bất động. N03 |
| M 50 ghi 0.3% | Công thức dùng $s=.3=30\%$ | Không chép. Các đồ thị dùng công thức/số sách |
| Vùng tô M 57/S4 PDF 33 | Không có phân bố tương đồng của kho để tính mẫu số lỗi toàn kho | Chỉ xác suất có điều kiện theo cặp và $P(s)$; không dùng diện tích như tỷ lệ lỗi |
| B 3.5.2 “any constant r” | Chuẩn chỉ $q\ge1$; nhiều mệnh đề sai với $q<1$ | Dùng $q\ge1$; tuyến chính $L_1,L_2,L_\infty$ |
| B 3.5.3 và lời nguồn về rỗng | Root đối chiếu Bài 05: SIM (∅, ∅) chưa định nghĩa; cột $+\infty$ chỉ kỹ thuật | Bác câu hồ sơ nguồn gán $J(\varnothing,\varnothing)=1$ cho Bài 05. Chốt mọi tập Jaccard/MinHash đều hữu hạn không rỗng; không thêm quy ước mới. HT1, HT5, N01–N06 |
| B 3.5.4 góc trên vector | $x$ và $2x$ khác nhau nhưng góc 0 | Góc là metric trên hướng/bội dương hoặc vector đơn vị, không trên toàn vector khác 0. $1-\cos\theta$ khác góc; $\theta$ đo radian, độ có quy đổi |
| Chỉnh sửa chuỗi | Ex 3.15 chỉ xóa/chèn; LCS cho 3 | Không thêm phép thay thế chi phí 1 hoặc DP. N05 |
| Bài 3.5.3 “greater than” | Các chuẩn có thể bằng nhau | Nếu dẫn chỉ viết ≥; bài này không soạn thêm chứng minh bài 3.5.3 |
| B 3.7.1 họ Hamming hữu hạn | Lấy mẫu có hoàn lại cho các lần chọn chỉ số độc lập | Không suy giới hạn số phép khuếch đại bằng $D$; nêu $D>0$. HT8 |
| OR như equality | Quan hệ chung ít nhất một bảng nói chung không bắc cầu | Dùng quyết định cặp/hợp nhiều bảng. AND mới có phép bằng tuple trực tiếp. N07 |
| Hai giá trị sau ghép | Công thức F/G đúng bằng giá trị khi xác suất cơ sở của cặp bằng $p$; họ chỉ có cận | Gọi cận gần/xa sau ghép, dùng tính đơn điệu. Ex 3.19–20, s03-11, N07 |
| B 3.7.3/S4 PDF 51 pháp tuyến ±1 | V10 góc thật 38.047579°, toàn 16 pháp tuyến cho 45° | Đẳng thức $1-\theta/\pi$ chỉ với đẳng hướng. Ví dụ dấu là phép tính hữu hạn; phân biệt mẫu và phân phối. sign (0)=+1 cố định |
| B 3.7.4 thiếu dịch biên | Cặp gần có thể luôn ở hai phía biên cố định; Datar §3.2 cho dịch đều | Chốt $u$ đều đơn vị hai chiều,$\delta\sim U[0,a)$ độc lập; xác suất theo $\delta$ là $\max(0,1-\ell/a)$. Cận gần≥1/2, cận xa≤1/3 chỉ hai chiều |
| B 3.7.5 “d 1<4 d 2” | Ví dụ trước có $d_2=4d_1$, câu nguồn không diễn đạt ràng buộc ấy | Không chép; nhánh mở rộng định tính chỉ $d_1<d_2$, không tái dùng hằng số hai chiều |
| Bài 3.7.5 trục cố định | Chỉ thực thi phép gán thùng | Không áp bảo đảm của hướng ngẫu nhiên cho ba trục cố định; khóa tách theo trục |
| Vân tay: thùng không đạt | Nếu mọi ảnh thiếu ô vào một thùng chung, va chạm không còn $q_F,q_T$ nguồn | Chỉ ảnh có đủ 3 ô vào thùng chung; ảnh khác nhận thùng đơn riêng. N12, s05-02 |
| Vân tay: nguồn chọn 3 ô từ lưới | Nếu điều kiện hóa ảnh truy vấn đã có 3 ô, xác suất sẽ khác | Chọn ba ô trước khi xét ảnh;$q_T=(.2\cdot.8)^3$,$q_F=.2^6$ là cả hai ảnh có đủ 3 ô. Nêu rõ mô hình độc lập, chưa phải thực nghiệm |
| Vân tay: làm tròn | Sách lấy.063²=.00397; từ tham số chưa làm tròn=.004024207 | Giữ tham số gốc cho tính tiếp; ghi sai khác do làm tròn, không coi là sai công thức |
| Ghép thực thể | Ba trường không có mô hình độc lập hoặc $p_1,p_2$ | Thuật toán sinh ứng viên và chấm điểm; không tự gán họ bốn tham số. Mô hình ngày cần giả thiết đại diện, chỉ notes đọc thêm |
| Bản tin, Ex 3.24 | Từ dừng tiếng Anh; token kế tiếp $x$ chưa cho;75%/25% là giả định | Giữ token tiếng Anh nguồn và giải thích tiếng Việt; không bịa token sau laundry, không xem dự báo là thực nghiệm |
| Các khẩu hiệu tốc độ trong slide | “MAGIC”, O (N), O (1) không đủ mô hình và không xử lý đầu ra bậc hai | Bỏ lời quảng bá; dùng Q, K và cận xấu nhất; không đổi thành khẳng định hiệu năng mới |

## Tự kiểm số và tính đúng trên kế hoạch

| Đối tượng | Phép tính hoặc bằng chứng | Kết quả hiện tại |
|---|---|---|
| V01 | $\binom{10^6}{2}=499999500000$; giây/ngày chia 86400 | 5.78703125 ngày; dung lượng $10^9$ byte. Giữ vai trò giả định |
| V02 | Dải 1 phát 14; dải 2 phát 13,14,34; Jaccard 13=1/4,14=2/3,34=1/5 | $Q=4,K=3$,8 lượt chèn, chỉ 14 đạt $t=2/3$. Phải giữ cặp có ngoặc khi chuyển công khai |
| V03 | 3 × 5 số từ ảnh Hình 3.7; tuple 2=tuple 4=(0,2,1) | Chỉ kết luận dải đầu; không tạo 9 hàng thiếu |
| V04 | $P(.3)=.047494259$;$P(.8)=.999643942$; ngưỡng chính xác.508695962 | Phân biệt xấp xỉ.549280272 và $t=.8$; so 10 × 10 cùng $n=100$ |
| V05–08 | 4,3→7,5,4; cos 1/2→π/3; LCS4→3 phép sửa; Hamming 3/5 | Khớp từng ví dụ nguồn, đơn vị và miền |
| V09 | AND 4→OR 4 và đảo thứ tự tại p=.8, .4 | (.878497449, .098534519) so (.993615344, .573951942); cận sau ghép |
| V10 | Tích (10,2, -4)/(4, -2,4); góc thật arccos $40/\sqrt{2580}$ | 120° ước lượng,38.047579° thật; khác phân phối được nêu |
| R1 | Tính 27 lũy thừa và 3 nghiệm $P=1/2$ | Bảng đủ 9 × 3, ngưỡng.406088134, .569353387, .424394480; đáp án lưu trong storyboard |
| R2 | Các phép biến đổi A (p)=p², B (p)=1−(1−p)²/³ | Bốn chuỗi đúng nguồn, trạng thái trung gian cho (d) |
| R3 | So 6 cặp theo 6 tọa độ | AB{3,4}, AC{1,3,5}, AD{1,5,6}, BC{2,3,6}, BD{2}, CD{1,2,4,5} |
| R4 | 12 tích vô hướng, chuẩn bình phương 54, tích 14, -14, -54 | Dấu++++, -+-+, +-+-; góc thật 74.973886°,105.026114°,180° |
| R5 | Hàm sàn mỗi trục với $a=1,2$ | $a=1$ chỉ 12; $a=2$ cả 3 cặp; biên trái đóng/phải mở đúng |
| V12/R6 | $q_F=.000064,q_T=.004096$; ghép dùng số chưa làm tròn | OR 2048: (.122849062, .000223559); AND 2 OR 1024: (.004024207, .029680224) |
| Thuật toán | I/O, tuple đầy đủ, khử lặp, kiểm gốc; khởi tạo–duy trì–kết thúc | Tính đúng theo tập ứng viên, không hứa đầy đủ mọi cặp đạt ngưỡng |
| Chi phí | Sao chép $bC$ tuple dài $r$; phát Q; kiểm K | $O(nC+Q+\sum T_J)$ kỳ vọng, bộ nhớ phụ $O(nC+K)$ ngoài SIG; khớp giả mã |

Các phép số đã được tác tử nguồn kiểm bằng Python thuần và bàn giao bảng kết quả; writer đối chiếu lại với công thức và bảng trong kế hoạch. Điều phối viên có thể chạy lại script tính số tạm. Đây là kiểm kế hoạch, chưa là kiểm trạng thái HTML hoặc SVG mới.

## Rà Quill và no-ai-slop

Đã đọc skill lập dàn bài cục bộ và hai references; áp dụng đủ tám phần phân tích trong outline. Mặc định năm 3 của skill được thay bằng năm 2 theo chỉ dẫn học phần; lý do mỗi bố cục gắn với thao tác cụ thể, không chỉ ghi “trực quan”. Quill được dùng theo nguyên tắc Outline/Revise: kiểm thứ tự, thuật ngữ, ký hiệu, đầu vào/đầu ra giữa chủ đề; không khởi tạo `quill.json` hoặc dự án sách.

Kết quả Quill: SIG của Bài 05 được dùng ngay ở N02;$s$ đổi sang $d=1-s$ trước định nghĩa họ; năm loại độ đo xuất hiện trước họ tương ứng; AND/OR nhận ví dụ phân dải đã có; N12 nhắc xác suất có điều kiện trước nhân 0.2 × 0.8; kết luận thu hồi P, Q, K và kho triệu tài liệu. N15 không cấp tiên quyết bắt buộc. Ghi chú đặt định nghĩa trước ví dụ; trang chiếu đặt thao tác/trực giác trước hình thức ở cụm trọng tâm. Hai chu trình được phân biệt có chủ ý.

Phạm vi no-ai-slop: các tác tử chỉ đọc dùng Detect cho lời nguồn; writer dùng Edit cho tiêu đề, thông điệp, nội dung công khai dự kiến và diễn giải notes ở 60 phiếu, cùng kiến trúc notes. Các phát hiện nguồn có trích đoạn gồm “MAGIC”, “the magic happens”, “best S-curve”, “computation is not an issue”; quyết định thay bằng tên thao tác, xác suất và điều kiện chi phí. Không dùng điểm phát hiện AI, không suy đoán tác giả.

| Nhóm eval.md | Bằng chứng biên tập và kết quả tự kiểm |
|---|---|
| Bảo toàn ý/giả thiết/dữ kiện | Giữ đủ r, b, s, miền không rỗng, độc lập, cận Euclid hai chiều, cả 6 cụm bài nguyên nguồn; không làm văn phong ngắn bằng bỏ điều kiện |
| Câu cụ thể và trực tiếp | Tiêu đề gọi khái niệm hoặc thao tác; loại câu hỏi tu từ, câu “từ…đến…”, lời nhấn mạnh chung; giữ câu hỏi đánh giá có nhiệm vụ |
| Không lời điều phối trong học liệu dự kiến | Các yêu cầu bố cục/cách tách nằm trường nội bộ; câu lời giải viết bằng phép tính và kết luận. Mã V/N/HT, ID không thuộc mặt trang hoặc notes công khai |
| Khoảng trắng và ký hiệu | Lượt Edit trước còn sót các từ dính được gate ghi ở G04. Lượt sửa gate thay từng chuỗi đã nhận diện trong ba kế hoạch và các phiếu tạm, giữ nguyên đường dẫn; kết quả chờ tác tử độc lập kiểm lại. Không dùng kết quả quét từ để chứng nhận sạch tuyệt đối |
| Tránh lặp máy móc | Mỗi trang có thao tác riêng: đọc ma trận, chèn, phát, hợp, kiểm, suy sự kiện hoặc chọn tham số; các trang không chỉ đổi tên cùng một ý |
| Cấu trúc và mức học thuật | Giữ định nghĩa/chứng minh/câu tự kiểm có chức năng; không áp gợi ý khẩu ngữ hoặc câu rời của skill vào học liệu |
| Đọc cuối và bản bàn giao | Toàn văn sửa nằm ba tệp mới; phần “Thay đổi trong lượt này” bên dưới nêu phạm vi. Chưa tuyên bố đạt render hoặc thay cho 5 reviewer độc lập |

## Đối chiếu tiêu chuẩn slide ở mức kế hoạch

| Nhóm tiêu chuẩn | Vị trí/bằng chứng | Tình trạng và việc còn lại |
|---|---|---|
| Đối tượng/ngôn ngữ | Outline 1,4; từng phiếu có đầu vào và lý do năm 2 | Đã đặc tả; gate rà lại mật độ của s02-12, s03-02, s04-09, s07-05/07 |
| Mục đích/mạch | 7 phần, 53 trang giảng; bản đồ chu trình và câu nối từng trang | Tự kiểm khớp; chờ gate độc lập. 6 nhiệm vụ kết bài phủ MT1–MT6 |
| Thuật toán | s02-01–09; N02; hàm Hamming/dấu/chiếu | I/O, bất biến, dừng, biên, chi phí có vị trí; chưa render giả mã để kiểm khả năng đọc |
| Ví dụ | V01–12, R1–6; vết chạy/bảng vai trò trong outline/storyboard | Số đã đối chiếu; SVG/HTML phải dùng lại cùng dữ kiện khi dựng |
| Chi phí | s02-13, s03-12, s04-10, s06-02; N04 | Mô hình trước công thức; Q/K tách; giá trị vừa từ máy/sao chép tuple đã chốt |
| Trực quan | Bố cục từng trang và danh sách SVG; ngưỡng chữ theo CSS chung | Chỉ đặc tả; chưa xác nhận hình/chữ/công thức ở khung 1280 × 720 hoặc màn hẹp |

Điều kiện pha 1 đã tự kiểm: 60 mã trang duy nhất; số phần 7; phút theo phần 8,32,30,26,16,8,60; giảng 120 và bài tập 60; mỗi phần có trang kiểm tra; bài tập có đề, sản phẩm, lời giải, tiêu chí và nguồn. Danh sách ID/tiêu đề/phút được xuất thêm ra thư mục tạm cho điều phối viên đối chiếu, không tạo tệp quy trình thứ tư trong repo.

Kiểm cấu trúc trước khi bàn giao pha 1: 60 ID đều duy nhất và đúng thứ tự với manifest tạm; thời lượng theo phần khớp 8,32,30,26,16,8,60. Không có mã V/N/HT/R, lời viện dẫn phiếu nội bộ hoặc thời gian điều phối trong mặt trang và notes phần giảng. Dấu phân cách công thức Markdown cân bằng, không có ký tự điều khiển do escape. Thư viện KaTeX cục bộ đã phân tích 863 biểu thức trong ba tệp với `throwOnError: true`, không báo lỗi cú pháp; đây là kiểm công thức nguồn, không thay kiểm render. Các đường dẫn nguồn trong liên kết được giữ nguyên, không qua bước giãn khoảng trắng.

## Thay đổi trong lượt này và các cổng còn lại

Thay toàn bộ ba kế hoạch cũ bằng bản đồ nguồn/chủ đề mới, 53 phiếu giảng, 7 phiếu bài tập, kiến trúc 16 chủ đề notes và lời giải đầy đủ. Các sửa nguồn, miền không rỗng, chi phí Q/K, dịch Euclid, phân phối pháp tuyến và mô hình vân tay đã được ghi thành quyết định bền vững.

Đã xử lý chín phát hiện của lượt đọc điều phối trước gate: khai báo đủ vector bốn chiều; trường kiểm chứng không tham gia tính điểm; giới hạn quy tắc từ dừng với quảng cáo; bỏ thời gian điều phối khỏi notes phần giảng; lời giải kiểm tra tự đủ; miền nguyên dương của b/r; ký hiệu hàm trục; khoảng trắng và tên tệp; trường hợp góc 0 và pi. Lượt sửa giữ nguyên 60 trang, thời lượng và mạch. Các trang lân cận đã được writer đối chiếu; gate độc lập vẫn cần kiểm.

## Xử lý cổng storyboard G01–G05

Điều phối viên đã chấp nhận cả năm đề xuất sửa của gate. Các sửa dưới đây chỉ tác động ba tệp kế hoạch và hai tệp phiếu/manifest tạm; không thay số trang, thứ tự, tiêu đề, thời lượng, dữ kiện nguồn hoặc phạm vi bài. Tên tác tử lập kế hoạch được sửa thành `lec06_plan` theo bằng chứng giao việc.

| Mã và mức độ | Sửa đã thực hiện | Phạm vi kiểm lại của writer và cổng tiếp theo |
|---|---|---|
| G01 — nghiêm trọng | Sau khi sao chép tuple, đặt $k\leftarrow(j,z)$; nếu khóa chưa có thì tạo $B[k]\leftarrow[]$, sau đó thực hiện `B[k].append(c)`. Outline, s02-08, bất biến s02-09 và N02 cùng mô tả hai trường hợp khóa mới/đã có | Rà s02-06–10, N02, HT1 và chi phí s02-13/N04. Vết chạy vẫn có 8 lượt chèn, $Q=4$, $K=3$; chi phí kỳ vọng vẫn $O(nC+Q+\sum T_J)$ và bộ nhớ phụ $O(nC+K)$. Tạo tối đa $bC$ danh sách không làm đổi cận |
| G02 — trung bình | s03-12 ghi rõ cơ chế AND_r rồi OR_b: tuple trong nhóm, hợp cặp giữa nhóm. Diễn giải và N07 nêu thứ tự OR rồi AND: hợp cặp trong mỗi nhóm OR, rồi giao các tập cặp của những nhóm OR | Rà s03-10–13 và N07. Hai thứ tự vẫn dùng 16 hàm trong Ví dụ 3.19–20; các cận gần/xa và bảng số giữ nguyên. OR không được đồng nhất với phép bằng tuple |
| G03 — trung bình | Nhiệm vụ 2 và đáp án s06-03 thêm điều kiện Jaccard $s\ge t$. N03/N14 xác định bỏ sót theo cùng điều kiện; s06-02 cũng ghi rõ cặp đạt ngưỡng chưa được sinh | Rà s06-01–04 và N03/N14. $(1-s^r)^b$ là xác suất không được chọn; tên “bỏ sót” áp dụng cho cặp đạt ngưỡng. Không đổi phép tính hoặc phút |
| G04 — trung bình | Sửa có mục tiêu các từ dính ở s04-03–11, s06-04, kiến trúc ghi chú và toàn bộ nhật ký; chuẩn hóa các mã HT1, MT1, S3/S4 và tên tệp `eval.md` | Rà toàn văn thay đổi, ưu tiên mặt trang và diễn giải học thuật; đối chiếu hai trang lân cận mỗi phía tại các điểm sửa. Các phép thay hữu hạn không giãn đường dẫn, tên tệp hoặc công thức bằng regex. Lượt Edit trước có sai sót; không lấy lời tự kiểm trước làm bằng chứng đạt |
| G05 — nhẹ | Khai báo $t\in[0,1]$ tại s01-04, bảng ký hiệu, HT1, N01/N02 và đầu vào xác minh s02-07/08 | Rà s01-04–05 và s02-07–09. Bộ tạo ứng viên vẫn nhận SIG và phân dải; ngưỡng thuộc bước chấp nhận sau xác minh. Ví dụ $t=2/3$ và $t=.8$ giữ nguyên |

Writer đã đọc lại các đoạn và phạm vi lân cận được liệt kê, áp dụng no-ai-slop Edit cùng kiểm liên tục Quill. Các kết quả này là bàn giao sửa, chưa phải PASS độc lập của gate. Manifest tạm vẫn gồm 60 ID theo thứ tự cũ, 53 trang giảng và 7 trang bài tập; phút theo phần vẫn 8, 32, 30, 26, 16, 8, 60.

Kiểm kỹ thuật sau sửa gate: 60 phiếu trong JSON khớp các trường tương ứng trong storyboard; ID, tiêu đề và phút khớp manifest trước sửa. Các URL và đường dẫn nguồn được đối chiếu với bản trước sửa, không thay đổi. `git diff --check` không báo lỗi khoảng trắng. KaTeX cục bộ phân tích 930 biểu thức với `throwOnError: true`, không báo lỗi cú pháp. Việc quét ID nội bộ và phút ở mặt trang/diễn giải phần giảng không phát hiện chuỗi vi phạm. Đây là kiểm văn bản nguồn; khả năng đọc của HTML và hình vẫn thuộc pha 2.

Gate đã tái kiểm PASS G01–G05; root đã xác nhận bốn sửa nhẹ E01–E04 và cho phép dựng HTML, notes, SVG cùng mục index Bài 06. Sau bản nháp cần đủ năm báo cáo độc lập trước editor riêng; rà lại toán/mạch khi có sửa tương ứng. Kiểm cuối phải dựa trên Reveal/viewer thật, offline, notes diễn giả, bàn phím, màn rộng/hẹp, bản in, KaTeX/SVG/liên kết. Nếu sửa CSS chung, kiểm ít nhất Bài 02/03 và các deck ảnh hưởng. Codex Slides chỉ dùng nhập ảnh/notes và thay đổi trạng thái xác định, không gọi mô hình. Commit/push thuộc điều phối sau mọi PASS; không gộp thay đổi của người dùng.

## Cổng triển khai pha 2

Điều phối viên thông báo gate tái rà PASS, không còn lỗi chặn hoặc nghiêm trọng, và cho phép dựng pha 2. Writer đã sửa bốn điểm nhẹ trước dựng: khôi phục chữ “Pha 1” ở outline và cuối storyboard; bỏ từ “hình” lặp; giới hạn bất biến theo dải đang xét; gọi đúng các nhóm OR ở bước lấy giao của cấu trúc OR rồi AND. Các phiếu tạm được đồng bộ, giữ 60 ID, tiêu đề và phút. Writer đã đọc báo cáo tái rà; root đã đối chiếu đủ bốn sửa E01–E04 trong repo và các phiếu tạm, xác nhận đạt và không yêu cầu mở lại gate.

## Bản nháp đầy đủ pha 2

Writer viết mới HTML Bài 06 từ các phiếu đã duyệt: 60 trang, 60 ghi chú diễn giả, bảy phần ngoài với phân bố 5/14/13/11/6/4/7. Tiêu đề, thứ tự và ID giữ manifest; thời lượng kế hoạch vẫn 120+60 phút. Mặt trang là nội dung học thuật và nhiệm vụ cụ thể, không sao các mô tả bố cục của phiếu. Ghi chú tự học được viết độc lập, khoảng 8.000 từ, gồm định nghĩa trước ví dụ, thuật toán, tám khối chứng minh, tám khối bài tập/đáp án và sáu gợi ý; tám bài tập gồm sáu cụm nguồn cùng hai mục tự kiểm. Không thêm bài lập trình.

Tài sản mới gồm 11 SVG: `quy-trinh-cap.svg`, `phan-dai-chu-ky.svg`, `xac-suat-phan-dai.svg`, `mien-gan-xa.svg`, `ghep-and-or.svg`, `chuan-vector.svg`, `phap-tuyen-dau.svg`, `goc-tach-sieu-phang.svg`, `chia-khoang-dich.svg`, `khoa-thuc-the.svg`, `phep-thu-van-tay.svg`. `2627-1/img/lec-06/generate_svg.py` tái tạo chúng bằng thư viện chuẩn Python, không cần mạng. Mỗi SVG có title, desc, role và alt tại nơi dùng. Mười SVG cũ được xóa sau khi HTML và ghi chú mới không còn tham chiếu chúng. Không đọc nội dung hình cũ để làm khung.

CSS chỉ thêm các selector `.reveal.course-deck.lecture-lsh`, điều chỉnh lưới, kích thước hình và khoảng đệm 28px hai bên; giữ thang chữ chung. Index chỉ đổi mô tả mục Bài 06, giữ liên kết deck/viewer hợp lệ. Bài 05 không được sửa; chỉ kế thừa đoạn cấu hình Reveal/Notes đã kiểm: main dùng chỉ số hash từ 1, receiver từ 0, nạp CSS KaTeX cục bộ và sao FontFace sau handshake cùng origin. Không có khối style riêng, kiểu chữ nội dòng, fragment hoặc tài sản lõi phụ thuộc mạng.

### Phản hồi QA sớm của điều phối viên và sửa tương ứng

| Phát hiện trước bản nháp đầy đủ | Sửa của writer | Trạng thái tại handoff |
|---|---|---|
| Hình chuẩn dùng tỷ lệ hai trục khác nhau, nhãn trục bị cắt | Hai trục cùng 50 đơn vị ảnh trên một đơn vị tọa độ; chừa nhãn trong viewBox, tăng chữ để đọc khi ghép slide | Generator đã chạy lại; root cần kiểm snapshot cuối |
| Chú giải hình góc chạm vòng tròn và che mũi tên | Tách vùng hình và chú giải, thêm cung góc giữa hai hướng và nhãn góc của hai miền tách | Giữ đúng hai miền góc; không đổi xác suất |
| Nhãn khóa dải chạm cạnh hộp | Dùng khóa ngắn `(j, tuple)` trong hộp, số dải vẫn hiện ở cột trái | Không đổi định nghĩa khóa |
| Nút điều hướng chạm nội dung ở mép; ba hình toàn chiều rộng có chữ nhỏ | Thêm khoảng đệm hai bên có phạm vi Bài 06; bỏ lớp hình ngắn ở s03-07, s03-12, s05-01 | Giữ font chung và số trang; cần root render lại |
| Thiếu nhãn nhiệm vụ và đáp án chưa tự đủ | Thêm “Câu hỏi:” ở mọi trang kiểm/recitation; bổ sung lời giải s01-05, s05-06; gọi rõ các tập/cặp ở s02-05 | Notes và phiếu kế hoạch đã đồng bộ |
| Ký hiệu chưa định nghĩa ở lần dùng | Khai triển LSH ở phần mở; giải nghĩa $V$, $u_{j,z}$, $p$ và góc nhọn $\phi$ trong nội dung/notes liên quan | Không thêm ký hiệu hoặc mệnh đề ngoài kế hoạch |

Root đã báo QA sơ bộ trên bản đầu: chụp 120 ảnh wide/narrow, không lỗi tràn khung/ngang/footer, KaTeX, hình, đường dẫn hoặc yêu cầu mạng lõi; kiểm Notes thật đủ 60 trang, đồng bộ hai chiều và mở lại đạt. Root cũng đã báo viewer bản đầu đạt với 519 công thức, 14 khối gập, bàn phím, in/afterprint, 38 mục lục, màn 1440/390, kiểm đường dẫn không hợp lệ và liên kết deck. Đây là kết quả của snapshot trước các sửa cuối, không được dùng thay kiểm cuối hoặc năm reviewer. Root đã đọc lại ba tệp planning qua Codex DesignFiles và giao diện ở pha 1; bản planning cuối pha 2 còn cần đồng bộ lại.

### Tự kiểm trước handoff

Writer áp dụng no-ai-slop Edit cho tiêu đề, mặt trang, diễn giải, ghi chú và lời giải; rà theo eval để loại lời điều phối, câu dẫn rỗng, quảng bá và lối gọi cặp không rõ. Quill kiểm chuỗi ký hiệu SIG→dải→cặp→xác suất/chi phí→độ đo→họ→ghép→ứng dụng, đồng thời giữ định nghĩa trước ví dụ trong ghi chú. Các giới hạn đẳng hướng, hai chiều, tập không rỗng, độc lập và chọn ô trước ảnh được giữ rõ. Không dùng điểm phát hiện AI hoặc tự khai runtime làm chứng cứ.

Kiểm tĩnh cục bộ đạt: 60 ID/title đúng thứ tự, 60 notes, bảy phần, không style nội dòng/fragment, mọi src cục bộ hợp lệ, 11 SVG đủ metadata, Markdown đúng heading đầu và dấu toán, hình/liên kết index hợp lệ. Các khối tự học không lồng. Kiểm số trực tiếp đối chiếu 27 ô của Bài 3.4.1 với công thức; hàng $s=.7$ bị chép lặp trong lượt nháp đã được sửa trước bàn giao. `git diff --check` không báo lỗi. Generator đã chạy lại và không dùng mạng. Các kiểm này không chứng nhận khả năng đọc của snapshot cuối.

KaTeX cục bộ kiểm 413 biểu thức trong văn bản HTML gồm mặt trang và notes, cùng 524 biểu thức Markdown: không có lỗi cú pháp. Có thông báo thiếu dữ liệu kích thước cho một số ký tự tiếng Việt trong `text` của công thức; đây không phải lỗi phân tích cú pháp, nhưng các dòng công thức chứa nhãn tiếng Việt vẫn cần đối chiếu render cuối. Không dùng kết quả phân tích công thức thay kiểm hình thức hiển thị.

Bản nháp đầy đủ chờ năm báo cáo độc lập và tác tử chỉnh sửa riêng theo quy trình. Root thực hiện render cuối, hồi quy CSS Bài 02/03, viewer, Notes và Codex Slides; writer chưa commit hoặc phát hành. Các trang mật độ cao tiếp tục ưu tiên s02-08/12/13, s03-02/03, s04-05/09 và s07-05/07. Nếu cần tách trang, phải quay lại điều phối để giữ kiểm soát manifest và thời lượng.

## Năm lượt rà độc lập trên bản nháp đầy đủ

Điều phối viên đã nhận, đọc và chấp nhận đủ năm báo cáo trước khi giao editor riêng. Các reviewer không đọc báo cáo của nhau và không sửa sản phẩm. Bản nháp được rà có SHA-256 HTML `fe2489327cfc6a893e4585cd9968a71fced913d66e6a55438b9bff7dfb075b91`, Markdown `8f1255f765cfc19122ce89d3033dab9c7d933fca291e7171d62773deb2e81aec`, gồm 60 trang và 11 SVG. Các kết luận dưới đây thuộc snapshot đó, chưa phải kết luận sau chỉnh sửa.

| Tác tử và vai | Kết luận, phát hiện | Kiểm đạt và bằng chứng chính | Giới hạn |
|---|---|---|---|
| `/root/lec06_math_review`, toán và thuật toán | PASS; M01, M02, E01 đều nhẹ; không lỗi chặn/nghiêm trọng/trung bình | Đọc toàn deck/notes/plans/SVG; đối chiếu trực tiếp sách §§3.4–3.8, Ví dụ 3.8, ba slide PDF và Datar §3.2. Kiểm độc lập toàn bảng 27 xác suất, sáu cụm bài tập, 16 pháp tuyến dấu, vết $Q=4,K=3$, cận/miền/độc lập và đường SVG. Khóa đầy đủ, bất biến, dừng, chi phí, xác minh, định lý góc và Euclid đúng theo giả thiết | Xem riêng ba ảnh s04-03/05/07 để kiểm quan hệ toán; không nhận đã kiểm toàn bộ render/viewer/bàn phím/in. M01 đổi ký hiệu hình; M02 làm rõ cơ sở theo dải; E01 là lời biên soạn |
| `/root/lec06_expert_review`, chuyên gia giải thuật và khoa học dữ liệu | CONDITIONAL; EX-01–03 trung bình, EX-04–05 nhẹ; không lỗi chặn/nghiêm trọng | Đủ năm loại độ đo, ba họ, ba ứng dụng, thuật toán–đúng–chi phí, phạm vi và sáu cụm recitation. Đối chiếu trực tiếp sách, ba PDF và dịch đều trong Datar; tính độc lập phân dải/ghép/vân tay. Xác nhận 53+7 trang, 120+60 phút thiết kế | Chỉ đọc, không xem render. Thiếu tự kiểm địa phương, định nghĩa từ dừng, nối truy hồi vân tay; lời biên soạn và phiếu s01-05 chưa khớp |
| `/root/lec06_flow_review`, mạch và nguồn | CONDITIONAL; MF01–04 trung bình, MF05–07 nhẹ; không lỗi chặn/nghiêm trọng | Rà từng trang và bảy ranh giới phần, N01–N16; đối chiếu trực tiếp sách và ba PDF. Giữ được sườn SIG→dải→xác suất/chi phí→độ đo→họ→ghép→ứng dụng; tổng kết thu hồi triệu tài liệu, $P,Q,K$ và bỏ sót. Đề recitation khớp nguồn | Không xem render hoặc mở lại web/Datar; không dùng OCR phủ định ảnh nguồn đã xác minh. Cần mục tiêu công khai, cầu nối mở rộng độ đo, tiên quyết từ dừng, định nghĩa độ trễ; thu hồi chỉnh sửa, loại lời biên soạn, sửa xuất xứ bước 6/7 |
| `/root/lec06_student_review`, góc nhìn sinh viên năm 2 | CONDITIONAL; S01–03 trung bình, S04–05 nhẹ; không lỗi chặn/nghiêm trọng | Đọc toàn deck/notes/plans, đối chiếu sách và ba PDF; tính lại các ví dụ/bài chính. Xem đủ 10 contact sheet/60 trang, mở riêng 13 ảnh rộng và bốn ảnh hẹp; hai ảnh đầu viewer thuộc snapshot trước. Giả mã, bảng, nhãn hình đọc được trong các ảnh đã mở; ký hiệu/mạch nhìn chung liên tục | Chưa kiểm toàn viewer hiện hành, bàn phím/in. Màn 390px thu nhỏ cả khung trình chiếu, không là bản đọc thân bài tốt. Thiếu định nghĩa $s_{1/2}$, bước chiếu Euclid, sự kiện điều kiện .8; tuple/chỉ báo cần giải nghĩa; lời biên soạn cần bỏ |
| `/root/lec06_academic_review`, học thuật và giảng dạy | CONDITIONAL; AH01–05, AH08 trung bình, AH06–07 nhẹ; không lỗi chặn/nghiêm trọng | Đọc toàn nội dung công khai/plans, sách và ba PDF. Xem đủ 10 contact sheet, năm ảnh rộng s03-03/s04-04/07/09/s05-05. Xác nhận vết phân dải, pháp tuyến dấu và ghép vân tay. Giữ các phân biệt toán học cần thiết và hai chu trình deck/notes | Không kiểm tương tác/viewer/in/mạng; không tính lại toàn bảng 27 ô. Cần khép Jaccard→xác suất, tỷ lệ dấu→góc, hình học chiếu, định nghĩa đặc trưng; sửa metadiscourse, từ “ít nhất”, tuple và tự kiểm chi phí |

Theo xác nhận của điều phối viên từ lời gọi công cụ, cả năm reviewer và `/root/lec06_editor` đều được tạo với `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none`. Đây là cấu hình được chỉ định, không là chứng cứ độc lập về runtime hoặc tuyến xác thực. Editor là tác tử riêng sau writer, chỉ một editor ghi kho; không tạo tác tử con, không dùng OpenRouter, API/CLI mô hình, `.env` hoặc bí mật.

## Quyết định hợp nhất và sửa sau năm báo cáo

Mọi phát hiện dưới đây đều được điều phối viên nhận. Điểm trùng được gộp để sửa một lần trên HTML, ghi chú, hình/generator và kế hoạch liên quan. Không có phát hiện nào bị bác mà không xử lý. Bốn phát hiện bổ sung của điều phối viên được ký hiệu ĐP01–04 trong bảng này; chúng không thay các mã của năm reviewer.

| Mã, mức độ | Vị trí → vấn đề và bằng chứng | Quyết định, thay đổi và phạm vi cần kiểm lại |
|---|---|---|
| M01 nhẹ | s04-03/N09: công thức dùng $v$ nhưng hình ghi $u$; ảnh rộng cho thấy hai ký hiệu | Nhận. Generator và SVG pháp tuyến dùng $v$ ở nhãn/mô tả; outline HT9 và bảng ký hiệu cùng dùng $v$. Giữ $u$ cho hướng chiếu. Rà s04-01–05 và N09 |
| M02 nhẹ; ĐP04 nhẹ | s02-09/N02: “ban đầu từ điển rỗng” ngay trong quy nạp theo dải có thể hiểu sai khi $j>1$ | Gộp. Khẳng định $B$ rỗng trước dải đầu; đầu mỗi dải $j$ chưa có khóa mang $j$, còn các dải trước được giữ. Giả mã/vết chạy/chi phí không đổi. Rà toán s02-07–11, N02 |
| E01 của vai toán nhẹ; EX-04 nhẹ; MF06 nhẹ; S05 nhẹ; AH05 trung bình; ĐP01 trung bình | s01-02/s05-05 và N05/N13 có “Phân dải được xây trước…”, “Không có căn cứ để tự tạo token…”, lý do dịch token, cảnh báo 75%/25% chưa có đầu vào | Gộp. Chuyển lý do biên soạn sang log; công khai chỉ còn quan hệ AND/OR, danh sách từ dừng, token kế tiếp chưa biết và giới hạn quy tắc. Bỏ lời về việc không triển khai chứng minh Minkowski/DP; giữ điều kiện $q\ge1$ và việc chi phí tính LCS cần một thuật toán. Rà học thuật/no-ai-slop toàn vùng |
| EX-01 trung bình; AH08 trung bình; ĐP03 trung bình | Notes N01–N13 thiếu nhiều nhiệm vụ cuối chủ đề đã duyệt, đặc biệt N04 phân biệt $Q,K$ | Gộp. Thêm 12 khối tự kiểm/solution để cùng N03 sẵn có phủ đủ N01–N13; N07/08/09/12 có liên kết rõ đến đề/lời giải nguồn. N04 dùng đúng vết $Q=4,K=3$, giải thích phát lặp vẫn tốn công. N14 và sáu cụm N16 giữ nguyên; N15 vẫn đọc thêm. Storyboard có bảng vị trí thực hiện. Không tạo recitation mới |
| EX-02 trung bình; MF03 trung bình; phần bản tin của AH04 trung bình | s05-05/N13 dùng từ dừng và “danh sách đang xét” trước định nghĩa/danh sách; sách tr.120 nêu trực tiếp năm token | Gộp. Định nghĩa từ dừng, liệt kê I, that, you, for, your trước vết; nêu bước that + you + buy và mật độ từ dừng trong văn xuôi của tình huống nguồn. Giữ bốn shingle xác định, $x$ chưa biết và quảng cáo dài. Tự kiểm N13 dùng nhiệm vụ s05-06 và đối tượng đầu ra; bỏ nhiệm vụ về thao tác dịch khỏi công khai. Rà s05-03–06/s06-01–02 và N12–N14 |
| EX-03 trung bình; phần vân tay của AH04 trung bình | s05-02/04, N12 thiếu định nghĩa đặc trưng và nối cấu trúc ghép với truy hồi; sách tr.117–120 mô tả cả hai | Gộp. Đặc trưng là nơi đường vân kết thúc/nhập vào nhau. Notes mô tả truy vấn một ảnh: hợp mã trong nhóm 1, hợp trong nhóm 2, giao, so ảnh; tìm mọi cặp dùng các tập cặp từ thùng. Chi phí xử lý mã và xác minh tách rõ. Không điều kiện hóa lại ảnh truy vấn; $q_T,q_F$ giữ nguyên. Rà toàn phần 5 và N12 |
| EX-05 nhẹ | Phiếu s01-05 còn nhiệm vụ cũ, HTML đã có ba câu dung lượng/số cặp/$s,\widehat s$ | Nhận phương án đồng bộ planning theo HTML. Giữ ba câu hiện hành và lời giải; cập nhật trường nội dung/bố cục, phiếu JSON. Tự kiểm N01 giữ nhiệm vụ tập ứng viên theo kiến trúc notes. Không đổi phút |
| MF01 trung bình | Phần mở chỉ có mục lục, thiếu năng lực quan sát được | Nhận. s01-02 đổi thành “Nội dung và mục tiêu”, giữ bảy mục và thêm ba năng lực gộp MT1–MT6. Bố cục hai vùng; danh mục/tiêu đề giữ font agenda, mục tiêu dùng font nội dung chuẩn. CSS chỉ chia lưới trong `.reveal.course-deck.lecture-lsh`; không giảm font. Đồng bộ tiêu đề/phiếu/manifest. Vì mở bài đổi, cần tái rà mạch toàn tuyến |
| MF02 trung bình | Ranh giới 2→3 và 3→4 chưa nói vì sao cần độ đo/họ khác; lý do chỉ có trong storyboard | Nhận. s03-01/N05 nối MinHash–Jaccard với vector/chuỗi; diễn giải s03-07/N06 tách độ đo khỏi bảo đảm tạo ứng viên; s04-01 và đầu “Ba họ…” nêu tính metric chưa bảo đảm tồn tại LSH. Không đảo ví dụ và định nghĩa. Rà mạch toàn tuyến, ưu tiên s02-12–s03-03 và s03-11–s04-02 |
| MF04 trung bình | N15 dùng trung bình ngày trước định nghĩa đại lượng và giả thiết cho 45 | Nhận. Độ trễ = ngày tạo B − ngày tạo A; giới hạn 0–90 ngày. Nêu giả thiết đủ là độ trễ ngẫu nhiên đều để có trung bình 45; không suy từ giới hạn đơn thuần. Nhóm điểm tối đa 300 được giả định khớp đúng, có trung bình 10. Giữ $x=10f+45(1-f)$ và điều kiện đại diện. Rà toán N11/N15 và các tiểu mục lân cận |
| MF05 nhẹ | Khái niệm chỉnh sửa chưa được thu hồi trong xác minh thực thể; sách tr.116 dùng nó cho điểm phạt | Nhận. s05-01 notes/N11 nêu khoảng cách chỉnh sửa trong phạt sai khác theo trường và hiệu chỉnh bảng tên tương đương. Không gán quy tắc điểm thành metric hoặc họ bốn tham số. Rà s03-03–07, s04-10–s05-03 và N05/N11 |
| MF07 nhẹ | Log/notes gọi bước 6 lọc chữ ký của sách là tùy chọn, nhưng chữ “Optionally” gắn bước 7 kiểm gốc | Nhận. Ghi chính xác biến thể đã duyệt: bỏ kiểm chữ ký bước 6, bắt buộc kiểm gốc trên mọi ứng viên. Sách chỉ gọi bước 7 tùy chọn. Sửa mô tả nguồn trong cả ba planning, notes và diễn giải s02-08; không đổi thuật toán hoặc cận |
| S01 trung bình | s02-12 chỉ có ký hiệu $s_{1/2}$ và hai số, thiếu định nghĩa ngay mặt slide | Nhận. Hiển thị $P(s_{1/2})=1/2$, tên điểm xác suất một nửa; gọi $b^{-1/r}$ là xấp xỉ vùng chuyển tiếp. Công thức đóng chuyển vào notes; giữ đồ thị lớn và phông. Rà s02-10–14/N03, R1 |
| S02 trung bình; AH03 trung bình | s04-09 thiếu $\ell=\rho|\cos\phi|$ và bước $\phi>\pi/3$; hình cũ chỉ có trục sau chiếu | Gộp. Thêm SVG `hinh-chieu-euclid.svg` qua generator, dùng chung notes; hình đoạn nối/hình chiếu/góc nhọn có đường vuông góc nét đứt. Hiển thị quan hệ độ dài, điều kiện cần và miền góc. Giữ hình dịch một chiều ở s04-07. Hình mới không ấn định quan hệ $a$ với $\rho$ để tránh áp hình minh họa cho cả hai miền cận. Rà toán/học thuật s04-05–11/N10 và render |
| S03 trung bình | s05-03 dùng “xác suất có điều kiện .8” trước tên sự kiện | Nhận. Mặt slide nói ảnh thứ hai có đặc trưng tại ô đã có ở ảnh thứ nhất; notes ghi $E_1,E_2$, $\Pr(E_2\mid E_1)=.8$. Giữ .16, .004096, .000064 và việc chọn ô trước ảnh. Rà s05-01–05/N12/R6 |
| S04 nhẹ; AH07 nhẹ | Tuple, $\Sigma$, chỉ báo chưa được giải nghĩa; notes dùng tiêu đề “Metric…” | Gộp. Lần đầu giải thích bộ $r$ giá trị có thứ tự, tập ký hiệu, chỉ báo nhận 1/0; slide Hamming cũng giải nghĩa chỉ báo. Đổi tiêu đề notes thành “Độ đo khoảng cách và chuẩn vector”. Cập nhật bảng thuật ngữ. Không thay khóa hoặc ký pháp trong giả mã |
| AH01 trung bình | s03-03 đi từ định nghĩa tập hợp sang bao hàm sự kiện, thiếu quan hệ khoảng cách–xác suất | Nhận. Thu hồi cặp (1,4): $1-2/3=1/3$; ghi $d_J(A,B)=\Pr[h(A)\ne h(B)]$ trước bao hàm, giữ cùng MinHash và không cần độc lập. Rà toán/học thuật s03-01–05/N05 |
| AH02 trung bình | s04-04/N09 đổi tỷ lệ khác bit thành góc trước căn cứ/định nghĩa quy tắc | Nhận phương án giữ thứ tự. Trước áp dụng, nêu xác suất khác dấu $p_{\ne}=\theta/\pi$ trong mô hình đẳng hướng và quy tắc $\widehat\theta=\pi\widehat p_{\ne}$. Notes định nghĩa tỷ lệ qua chỉ báo và nêu hai miền góc làm căn cứ; chứng minh đầy đủ vẫn sau vết dấu. Pháp tuyến dấu cố định không được nhận bảo đảm đẳng hướng. Rà toán/học thuật s04-01–07/N09/R4 |
| AH06 nhẹ | Định nghĩa chỉnh sửa ở s03-05 nêu thao tác nhưng thiếu tính tối thiểu | Nhận. Thêm “số thao tác ít nhất”, giữ chỉ chèn/xóa một ký tự. Rà s03-03–07 và phiếu |
| ĐP02 nhẹ | Giả mã thiếu `data-trim` | Nhận. Thêm thuộc tính trên code plaintext; không thay mã, thụt dòng hoặc cỡ chữ |

Các lý do biên soạn được giữ ở đây: token tiếng Anh được bảo toàn vì danh sách từ dừng của Ví dụ 3.24 là tiếng Anh; dịch token rồi áp danh sách cũ sẽ đổi dữ kiện. Không có token sau “laundry” nên chỉ bốn shingle đầy đủ được xác định. Phân tích giả định 75%/25% của sách không được triển khai trong bài, vì vậy cảnh báo riêng về hai tỷ lệ ấy cũng bỏ khỏi notes. Không bổ sung chứng minh Minkowski hoặc thuật toán quy hoạch động vì phạm vi chỉ cần metric/giá trị tối ưu chỉnh sửa; các điều kiện và phân biệt chi phí vẫn còn. Đặt vết dấu trước chứng minh hình học tạo trực giác thao tác, nhưng quy tắc ước lượng nay được định nghĩa trước phép sử dụng. Đây là các quyết định nội bộ, không phải lời hướng dẫn công khai.

## Tự kiểm của editor và bàn giao tái rà

Editor đã đọc hợp đồng sửa, đủ năm báo cáo cùng phát hiện của điều phối viên; đọc source map trước nguồn chi tiết, dòng ánh xạ Bài 06, AGENTS, tiêu chuẩn, template/CSS/index và toàn văn HTML/ghi chú hiện hành. Editor tự trích bốn PDF cục bộ và đối chiếu trực tiếp các đoạn được sửa: bước 6/7 ở tr.95–96; MinHash–Jaccard tr.98–99; quy tắc dấu/siêu phẳng tr.109–111; hình chiếu tr.112; điểm phạt/ngày tr.116; đặc trưng, truy hồi vân tay và từ dừng tr.117–121. Không nhận việc trích văn bản là kiểm ảnh toàn bộ nguồn, không dùng dossier thay cho những đoạn sách này.

No-ai-slop **Edit** áp dụng cho các tiêu đề, mặt trang, ghi chú diễn giả và ghi chú tự học được sửa; tự đối chiếu `eval.md` trước bàn giao. Quill Outline/Revise áp dụng cho đầu vào–đầu ra, thuật ngữ và ký hiệu N01–N16; không tạo `quill.json`. Kết quả tự kiểm:

| Nhóm eval/tiêu chuẩn | Bằng chứng và kết quả |
|---|---|
| Bảo toàn nội dung | Đạt tự kiểm: không đổi dữ kiện/vết số/đề recitation, giữ miền không rỗng, nguồn ngẫu nhiên, độc lập, cùng phép băm, dấu 0, hai chiều và chọn ô trước ảnh. Cầu nối/giả thiết thêm có nguồn và quyết định của điều phối |
| Văn phong học thuật, câu cụ thể | Đạt tự kiểm: chuyển các lời về thứ tự biên soạn/token/chứng minh sang log; giữ câu hỏi có nhiệm vụ, định nghĩa, lập luận, giới hạn mô hình và tổng kết có chức năng. Không dùng khẩu ngữ, ca tụng, điểm phát hiện AI hoặc suy đoán tác giả |
| Mạch Quill | Đạt tự kiểm với giới hạn cần tái rà: thêm mục tiêu và câu nối; Jaccard có phép lấy bù; góc có quy tắc trước tính; Euclid có hình chiếu trước cận; thực thể dùng lại chỉnh sửa; hai ứng dụng còn lại có dữ liệu/thuật toán truy hồi. Ký hiệu $v$ pháp tuyến tách $u$ hướng chiếu |
| Vai trò/đầu ra | 60 phiếu và manifest khớp từng trường; tiêu đề s01-02 thay đổi để thêm mục tiêu, s04-09 được rút gọn sau QA để tránh nút điều hướng. N01–N13 đều có tự kiểm tại chỗ hoặc liên kết rõ, N14 tổng hợp và N16 recitation giữ chức năng riêng |
| Thuật toán/chi phí | Chỉ làm rõ cơ sở bất biến và xuất xứ biến thể, không đổi giả mã ngoài `data-trim`. Tự kiểm $Q/K$ nối phép đếm với phát lặp. Cần reviewer toán tái nhận các đoạn lập luận bổ sung |
| Cấu trúc và kỹ thuật nguồn | Kiểm tĩnh PASS: 60 ID/60 notes, bảy section phân bố 5/14/13/11/6/4/7; phút 8/32/30/26/16/8/60. Không inline style/fragment/raster; src và alt hợp lệ; index không đổi trong lượt editor |
| Markdown và liên kết | 20 exercise, 20 solution, 8 proof, 5 example, 6 hint; không lồng khối, heading đầu H1. Bốn liên kết đến Bài 3.6.1, 3.7.1, 3.7.2, 3.8.2 khớp quy tắc slug viewer. Cần QA viewer thực để xác nhận gập/bàn phím/in |
| Công thức và SVG | KaTeX cục bộ phân tích 456 biểu thức HTML và 577 Markdown, không lỗi cú pháp. Có cảnh báo dữ liệu kích thước vài ký tự tiếng Việt trong công thức như bản nháp, cần xem render. Cả 12 SVG tái tạo byte-identical trong thư mục tạm; phép đo tam giác xác nhận độ chiếu bằng độ dài gốc nhân cos góc |
| Ảnh editor | Chụp 120 ảnh rộng/hẹp trên snapshot sau sửa nội dung: không lỗi bounds/horizontal/footer, không lỗi trang hoặc tải tài nguyên. Đã mở riêng ảnh rộng s01-02, s02-09/12, s03-03, s04-04/09, s05-02/03/05 và ảnh hẹp s04-09. Sau đó chỉ ngắt dòng bất đẳng thức ở s04-09 và tách câu biểu diễn ảnh khỏi gạch đầu dòng s05-02; QA cuối phải dùng snapshot sau hai sửa này |
| CSS | Chỉ thêm lưới `.lsh-orientation` trong phạm vi `.reveal.course-deck.lecture-lsh`; giữ font, line-height và spacing của các vai chữ. Không xác nhận hồi quy bằng đọc CSS; root kiểm Bài 02/03 và các deck ảnh hưởng |

Tự kiểm số mới xác nhận $P_{20,5}(s_{1/2})=1/2$ tới sai số số thực, phép chiếu của SVG, trung bình đều $(0+90)/2=45$ và hai biên của công thức hỗn hợp. Các bảng số không đổi đã có kiểm độc lập của năm reviewer; editor không dùng việc tính lại vài số để thay lượt rà toán.

Phạm vi ghi của editor gồm HTML Bài 06, Markdown ghi chú, ba planning, generator, SVG pháp tuyến và SVG chiếu mới; CSS chỉ lưới nói trên. Phiếu `storyboard-cards.json`, `storyboard-manifest.json` và `draft-content.json` tạm được đồng bộ. Không sửa Bài 05, hạ tầng viewer, index, AGENTS, tiêu chuẩn, `.gitignore`, user dirt; không commit hoặc push.

Bàn giao cần ba lượt tái rà độc lập: **toán** cho s02-09/N02, s03-03/N05, s04-04/N09, s04-09/N10/SVG mới, s05-03/N12 và mô hình ngày N15; **mạch** cho toàn tuyến vì mục tiêu mở đầu đổi, kể cả các ranh giới phần và tự kiểm N01–N13; **học thuật** cho các cầu nối Jaccard/góc/chiếu và định nghĩa ứng dụng. Mỗi vùng đọc thêm hai trang lân cận mỗi phía theo hợp đồng. Root còn QA Reveal/viewer/Notes/offline/bàn phím/in, hồi quy CSS và Codex Slides trên snapshot cuối. Kết quả editor là hoàn tất lượt sửa được giao, chưa phải PASS cuối hoặc phát hành.


### Sửa sau QA cuối của điều phối viên

Ba phát hiện sau đây xuất hiện sau tự kiểm editor và đã được sửa trước snapshot bàn giao. Các kết quả kiểm cú pháp/toàn trang ở trên không phát hiện đủ các lỗi này; không dùng chúng để thay QA DOM, nút điều hướng và bản in.

| Phát hiện và bằng chứng QA | Sửa, phạm vi và kiểm lại |
|---|---|
| Chặn diễn giải: các dấu nhỏ hơn chưa escape trong notes s04-09 khiến HTML parser hiểu phần bắt đầu bằng chữ a là thẻ; văn bản DOM mất đoạn suy luận. Điều phối viên xác định đây cũng là nguyên nhân timeout font của cửa sổ Notes tại trang này | Escape ba span toán trong notes thành thực thể HTML; quét mọi span toán có cặp dấu trong HTML để bảo đảm không còn góc nhọn raw. Parser độc lập giữ đủ ba bất đẳng thức trong chuỗi suy. Đồng bộ lại diễn giải s04-09 trong storyboard, phiếu và bản nội dung tạm vì lần đồng bộ trước cũng đã mất đoạn. Không sửa hạ tầng Notes hoặc CSS. Root kiểm lại Notes thật |
| Vừa: tiêu đề s04-09 chạm nút lên khi nội dung cao | Rút thành “Cận xác suất trong mặt phẳng”; đồng bộ tiêu đề trong outline, storyboard, phiếu và manifest. Không đổi font, thứ tự, ID, thời lượng hoặc phát biểu. Root kiểm lại nút điều hướng |
| Vừa: bản in ghi chú trang 36 cắt công thức bỏ sót khi hai xác suất ở cùng một hàng trong lời giải Bài 3.8.2 | Tách mỗi xác suất thành một khối công thức riêng, áp dụng cho OR 2048 và AND hai nhóm OR 1024. Không đổi biểu thức hoặc số. Root kiểm lại PDF/bản in |

Sau ba sửa, tự kiểm kỹ thuật đạt: 60 ID/60 notes, bảy phần; 60 phiếu khớp storyboard/manifest và tổng phút 120+60; 12 SVG tái tạo đúng từng byte; không còn tiêu đề cũ hoặc diễn giải bị nuốt. KaTeX phân tích 456 biểu thức HTML và 579 biểu thức Markdown, không lỗi cú pháp. Kiểm HTML parser xác nhận đủ các bất đẳng thức ở s04-09; đây là kiểm bổ sung tách khỏi kiểm cú pháp KaTeX. Hai công thức khối được tách làm số biểu thức Markdown tăng hai. No-ai-slop Edit/eval và Quill kiểm lại tiêu đề rút gọn cùng các đoạn liên quan; thuật ngữ và mạch suy luận giữ nguyên.

Editor dừng ghi sản phẩm công khai sau ba sửa, hoàn tất log và lưu danh sách SHA-256 tại `/tmp/lec06-rebuild/editor-final-snapshot.json`. Bản snapshot này dành cho tái rà và QA cuối của root, không xác nhận PASS của các lượt độc lập chưa nhận. Không commit/push.

## Tái rà độc lập và kết luận của điều phối viên

Ngày 28-09-2026, điều phối viên đã đọc đầy đủ ba báo cáo tái rà trên bản cuối. HTML có SHA-256 `4c1a97bbb8a52137a6feeb1fb5a7d2d5ea4b1b1382d7720823546746db91b20a`; ghi chú có SHA-256 `63bb796770e87ea072f90bc9dec4198085219a954df3f0d22ec4d834ede9ff63`. Các hash này không đổi trong kiểm định và đồng bộ cuối.

| Vai tái rà | Kết luận và phạm vi | Quyết định cuối |
|---|---|---|
| Toán và thuật toán — `/root/lec06_math_review` | PASS; đóng M01/M02/E01. Kiểm các bổ sung Jaccard–xác suất, ước lượng góc, bất biến theo dải, cận chiếu hai chiều, mô hình ngày, 13 tự kiểm và lời giải. Kiểm qua HTML parser chuỗi bất đẳng thức s04-09; bốn công thức Bài 3.8.2 chỉ đổi ngắt dòng | Nhận; không còn sửa toán hoặc thuật toán tồn đọng |
| Mạch và nguồn — `/root/lec06_flow_review` | PASS; đóng MF01–MF07. Đọc đủ 60 mặt trang/60 notes, toàn tuyến bảy phần, sáu ranh giới, các vùng sửa cùng hai trang lân cận mỗi phía và N01–N16. Xác nhận mục tiêu–đầu ra, sườn sách, 120+60 phút, nguồn bài tập và đồng bộ tiêu đề/phiếu | Nhận; không đổi thứ tự hoặc phạm vi thêm |
| Học thuật và giảng dạy — `/root/lec06_academic_review` | PASS; đóng AH01–AH08. Đọc diff và vùng phụ thuộc; đọc lại các đoạn sách; xem ảnh cuối về Jaccard, góc, hình chiếu, đặc trưng vân tay và từ dừng. Không còn lời biên soạn trong nội dung công khai được rà | Nhận; các phát hiện trùng của vai chuyên gia/sinh viên cũng đã được editor xử lý và root đối chiếu |

Ba báo cáo đầy đủ nằm trong thư mục QA tạm: `recheck-math.md`, `recheck-flow.md`, `recheck-academic.md`. Bảng này lưu kết luận, phạm vi và quyết định bền vững; không phụ thuộc việc các tệp tạm còn tồn tại. Điều phối viên đã đối chiếu phần văn bản đổi, hình mới và ba sửa QA cuối. Không dùng kết quả tự kiểm của editor thay các lượt độc lập.

### Phiếu kiểm sáu nhóm của tiêu chuẩn

| Nhóm | Bằng chứng bản cuối | Kết luận |
|---|---|---|
| Đối tượng | Giải nghĩa tuple, chỉ báo, tập ký hiệu, đặc trưng và từ dừng tại nơi dùng; không giả định cơ sở dữ liệu hoặc hệ phân tán. Bài lập trình không được thêm ngoài nguồn | Đạt cho tiên quyết năm 2 đã ghi |
| Mục đích và mạch | Ba mục tiêu công khai; 60 phiếu có chức năng/đầu vào/đầu ra; mạch sách §§3.4–3.8; tổng kết thu hồi kho triệu tài liệu và phân biệt xác suất–công việc–kết quả. N01–N13 có tự kiểm địa phương | Đạt; tái rà toàn tuyến PASS |
| Thuật toán | Đặc tả, khóa đầy đủ, khởi tạo thùng, phát cặp, hợp tập, xác minh gốc, bất biến và dừng nhất quán. Phân biệt tính đúng trong tập ứng viên với bỏ sót do xác suất | Đạt; biến thể so với bước 6/7 của sách đã ghi rõ |
| Ví dụ | Cùng dữ kiện truyền từ chữ ký đến thùng, $Q=4,K=3$, Jaccard và xác minh; pháp tuyến dấu cố định phân biệt với mô hình đẳng hướng; bài tập giữ dữ kiện và yêu cầu nguồn | Đạt; lời giải và bảng số được rà độc lập |
| Chi phí | Phép đếm $Q$, số cặp duy nhất $K$, giá trị băm/khóa và xác minh được tách; có trường hợp xấu nhất, mô hình bộ nhớ và điều kiện kỳ vọng. Tự kiểm giải thích vì sao không thay $Q$ bằng $K$ | Đạt; không nhận LSH luôn tuyến tính |
| Trực quan | 12 SVG có mô tả, nhãn và quan hệ nguồn; công thức/bảng/giả mã vẫn là nội dung văn bản. Hình chiếu mới thể hiện độ dài và chân vuông góc; glyph, khung và nhãn đã kiểm trên trình duyệt | Đạt trong các kích thước kiểm dưới đây |

### Kiểm định cuối trên trình duyệt

Kiểm trên máy chủ kho tại `http://[::1]:8765/`, dùng Chromium cục bộ vì phiên này không cung cấp công cụ Browser trong trình biên tập. Các yêu cầu mạng ngoài máy chủ bị chặn trong kiểm Reveal/viewer; tài sản lõi vẫn tải đủ. Không coi liên kết tham khảo ngoài kho là phụ thuộc chạy bài.

| Kiểm | Kết quả và giới hạn |
|---|---|
| RevealJS | 60 trang × hai kích thước rộng/hẹp = 120 ảnh cuối. Không tràn khung/ngang/footer, lỗi KaTeX, hình hỏng, HTTP lỗi hoặc lỗi JavaScript. Kiểm bàn phím/hash và nút điều hướng đạt; s04-09 không còn chạm tiêu đề. Root đã xem toàn bộ 60 mặt trang ở lượt đầy đủ, xem lại các vùng sửa và ảnh s04-09 cuối |
| Notes diễn giả thật | Mở bằng phím S từ HTML kho, đối chiếu đủ 60 notes với slide hiện hành; công thức, font, MathML ẩn, đồng bộ hai chiều và đóng/mở lại đều đạt. Root xem lại s04-09: đủ chuỗi bất đẳng thức, không còn thẻ HTML phát sinh ngoài ý muốn |
| Ghi chú tự học | 579 công thức, không lỗi KaTeX; màn rộng 1440px và hẹp 390px không tràn trang/hỏng hình/thiếu alt. 38 mục lục và bốn liên kết tự kiểm đều có đích; 26 khối gập đóng mặc định, mở/đóng bằng bàn phím, mở khi in và phục hồi sau in. Đường dẫn sai bài và đi ngoài materials bị từ chối |
| Bản in | PDF QA 37 trang. Root đã xem tất cả trang ở lượt kiểm đầy đủ; sau tách công thức chỉ vùng cuối thay đổi, đã in lại và xem trang 36–37. Cả bốn xác suất Bài 3.8.2 hiện trọn vẹn. Ngắt trang tự động còn có khoảng trắng và tiêu đề tài liệu tham khảo ở cuối trang 36; không mất nội dung |
| SVG | 12 tệp có metadata và không có nhãn vượt viewBox. Root chạy generator lần cuối, SHA-256 trước/sau giống nhau cho cả 12 tệp. Hình chiếu mới có chữ nhỏ nhất khoảng 22,9px trong khung 1280×720; một số nhãn ngắn của hình dịch khoảng khoảng 19,6px đã được vai sinh viên xem và chấp nhận |
| CSS và phạm vi ảnh hưởng | Mọi selector thêm giới hạn ở `.reveal.course-deck.lecture-lsh`; không đổi thang chữ chung. Hồi quy Bài 02/03: 144 trang, 288 ảnh rộng/hẹp không lỗi hình học/tải; đối chiếu cuối font, độ đậm, line-height, margin/padding của từng thành phần khớp baseline. Hash HTML Bài 02–05 và hạ tầng viewer giữ nguyên |
| Kiểm tĩnh | 60 ID duy nhất/60 notes/bảy phần; thứ tự và phiếu khớp. Không thêm raster, thư viện, phông mạng hoặc CSS riêng trong HTML. Liên kết deck/viewer của mục Bài 06 hợp lệ. `git diff --check` đạt |

Màn 390px thu nhỏ khung trình chiếu 1280×720, nên không dùng kết quả không tràn để khẳng định đọc tốt chữ thân bài trên điện thoại. Ghi chú qua viewer là bản đọc có bố cục thích ứng. Thời lượng 120+60 phút là thiết kế trong storyboard/notes, chưa là kết quả giảng thử có bấm giờ.

### Đồng bộ và rà Codex Slides

Dự án `20260827182308-b-i-6-t-m-c-p-t-ng-ng-b-ng-lsh-bmts` được cập nhật bằng 60 ảnh PNG từ bản Reveal đã kiểm và 60 ghi chú trích từ HTML. Ảnh PNG chỉ nằm trong kho dữ liệu cục bộ của công cụ và thư mục QA tạm, không đưa vào Git. Mọi thao tác là nhập nội dung tường minh; không dùng chức năng sinh ảnh, sinh deck, sinh notes, nghiên cứu hoặc mô hình qua API. Không dùng OpenRouter hoặc đọc tệp bí mật.

Kiểm giao diện Codex Slides bằng Chromium ở chế độ chỉ đọc: mở lần lượt đủ 60 trang, SHA-256 ảnh phục vụ từ ứng dụng khớp ảnh nguồn, 60 trường ghi chú khớp manifest và không lỗi JavaScript. Root xem các ảnh giao diện được chọn, gồm mục tiêu mở đầu, cận Euclid và panel notes bài vân tay. Trạng thái dự án là `deck`, 60/60 trang có ảnh. Các yêu cầu tự lưu chat từ giao diện bị chặn có chủ đích; lịch sử chat/chi phí cũ của dự án không là kết quả chạy mới. Trường notes của Codex Slides giữ TeX dạng văn bản; khả năng render công thức được xác minh ở cửa sổ Reveal Notes thật. Ba Design Files cuối được đồng bộ từ outline, storyboard và nhật ký trong kho, rồi kiểm đọc lại.

Kết luận kiểm định nội dung và kỹ thuật: **PASS**, không còn phát hiện chặn, nghiêm trọng hoặc trung bình chưa xử lý. Phạm vi phát hành chỉ gồm sản phẩm Bài 06, mô tả index và CSS đã giới hạn; các thay đổi riêng của người dùng được giữ ngoài commit. Commit/push do điều phối viên thực hiện sau đồng bộ Design Files; mã commit và kết quả đối chiếu `origin/main` được báo trong bàn giao.

## Duyệt từng trang ngày 02/10/2026

Yêu cầu của người dùng: duyệt lần lượt từng trang, xác định trang muốn nói gì, đề xuất rồi sửa để tiêu đề ngắn gọn, học thuật; lập luận chặt; khái niệm không xuất hiện đột ngột. Sau mỗi trang, sửa phần tương ứng của `lecture-note.md`, commit và push.

Cách làm như lượt Bài 05 (01/10/2026): điều phối viên (phiên Claude Code, Opus 5.5, effort `high`) biên tập từng trang, tự kiểm theo `no-ai-slop`/`eval.md`, tính lại phép tính bằng chương trình; sau mỗi phần, một tác tử rà chỉ đọc (`subagent_type: "fork"`, kế thừa Opus 5.5) kiểm độ chính xác và mạch. Kiểm hiển thị bằng Playwright Chromium ở 1600 × 900 và 390 × 844 (khổ hẹp kiểm bằng cuộn tới trang vì chế độ cuộn của Reveal), ghi chú ở 1440 × 900, 390 × 844 và in; máy chủ chạy ở cổng 8775 từ gốc kho. Quy ước số thập phân: trang nào được sửa thì đổi dấu chấm thập phân sang dấu phẩy (`0{,}8`) theo cách viết tiếng Việt đã dùng ở Bài 04–05.

| Trang | Trang muốn nói | Quyết định | Thay đổi deck và storyboard | Ghi chú tự học |
|---|---|---|---|---|
| lec06-s01-01 | Tên bài; LSH được diễn giải ở dòng phụ; nối từ chữ ký Bài 05. | giữ | Tiêu đề, dòng phụ và ghi chú đạt. | Không đổi. |
| lec06-s01-02 | Bảy phần và ba mục tiêu học tập. | sửa | Ba mục tiêu viết lại theo sản phẩm cụ thể: tạo và xác minh tập ứng viên bằng phân dải; tính xác suất một cặp thành ứng viên và chọn số dải, số hàng; chọn họ băm theo độ đo (trước: “Suy xác suất…”, “Chọn phép thử…” chưa nói đối tượng). Ghi chú bỏ thuật ngữ AND/OR (định nghĩa ở phần 3), thay bằng chuỗi quan hệ giữa các phần. Storyboard đồng bộ. | Không đổi; phần mở đầu ghi chú nêu cùng phạm vi. |
| lec06-s01-03 | Ví dụ 3.10: chữ ký một triệu tài liệu chỉ $10^9$ byte nhưng còn khoảng $5\cdot10^{11}$ cặp, gần 6 ngày với 1 µs mỗi cặp. | sửa nhẹ | Tiêu đề “Số cặp sau khi tạo chữ ký” (kể tiến trình) → “Chi phí so sánh mọi cặp chữ ký”. Số viết theo quy ước tiếng Việt: $499\,999\,500\,000$, $5{,}79$ ngày. | Mục 1: cùng cách viết số ($499\,999\,500\,000$, $499\,999{,}5$ giây, $5{,}787$ ngày). |
| lec06-s01-04 | Phát biểu bài toán: đầu vào tập, chữ ký, ngưỡng $t$; đầu ra mọi cặp có $\mathrm{SIM}\ge t$; cách làm chỉ xác minh ứng viên. | sửa | Tiêu đề “Đầu vào và cặp cần tìm” → “Bài toán tìm cặp tương đồng”. Sáu dòng ký hiệu rời thay bằng hai dòng có nhãn “Đầu vào”, “Đầu ra”; ký hiệu $V$, $s$, $\widehat s$ và tính chất MinHash chuyển vào ghi chú. Câu chốt nêu cách làm và cái giá: chỉ xác minh ứng viên, có thể bỏ sót (trước đó nói “bộ tạo ứng viên” khi chưa giới thiệu ý tưởng). | Không đổi; mục 1 đã phát biểu bài toán, ký hiệu và khả năng bỏ sót. |
| lec06-s01-05 | Kiểm tra: số cặp tăng bậc hai, tác dụng của tập ứng viên, phân biệt $s$ với $\widehat s$. | sửa | Tiêu đề “Kiểm tra bài toán tìm cặp” → “Câu hỏi về bài toán tìm cặp”. Câu 1–2 cũ có đáp án nguyên văn trên s01-03; thay bằng: số cặp và thời gian với $C=10^5$ ($4\,999\,950\,000$ cặp, gần 1,4 giờ); mức giảm số phép xác minh khi chỉ có $10^6$ ứng viên (khoảng $5\cdot10^5$ lần); câu 3 dùng cặp $S_1,S_4$ của Bài 05 ($\widehat s=1$, $s=2/3$). Dòng nguồn ghi dữ kiện luyện tập. | Mục 1: bài tự kiểm thêm ý (b) với $C=10^5$, có lời giải; số viết theo quy ước tiếng Việt. |
| lec06-s02-01 | Ý tưởng phân dải: chia $n=br$ hàng thành $b$ dải; trùng toàn bộ ít nhất một dải là ứng viên; cột càng tương đồng càng dễ thành ứng viên. | sửa | Tiêu đề “Phân dải chữ ký” → “Ý tưởng phân dải chữ ký”. Câu chốt kỹ thuật về tuple thay bằng trực giác của MMDS §3.4.1 (cột càng tương đồng càng dễ trùng ít nhất một dải); dòng phụ nêu mỗi dải có bảng thùng riêng; gạch thứ hai định nghĩa tuple (nhãn của hình). Ghi chú nêu cách tiếp cận chung của LSH, ứng viên giả và bỏ sót. | Mục 2: đoạn mở thêm cách tiếp cận chung của LSH, ứng viên giả, bỏ sót và trực giác phân dải. |
| lec06-s02-06 | Ví dụ 3.11 (Hình 3.7, $r=3$): trùng dải đòi trùng cả ba thành phần; cột 2 và 4 thành ứng viên, cột 2 và 3 chưa. | sửa, chuyển vị trí | Chuyển lên ngay sau s02-01 theo thứ tự MMDS §3.4.1: vết chạy s02-02…05 dùng $r=1$ nên không minh họa được điều kiện “trùng cả $r$ thành phần”. Tiêu đề “Điều kiện trùng một dải” → “Ví dụ trùng dải với ba hàng”. Dòng $z_2=z_4=(0,2,1)$ dùng ký hiệu chưa định nghĩa; viết lại bằng lời. Câu chốt nêu cả hai kết luận. Ghi chú thêm giả định của sách: cùng thùng khi và chỉ khi tuple bằng nhau. Phiếu storyboard chuyển cùng vị trí. | Mục 2: đoạn Hình 3.7 chuyển lên trước vết chạy, thêm giả định về thùng. |
| lec06-s02-02 | Dữ kiện vết chạy: chữ ký hai hàng của $S_1..S_4$ (Ví dụ 3.8), $b=2$, $r=1$, $t=2/3$. | sửa nhẹ | Tiêu đề “Chữ ký của bốn tập” → “Phân dải chữ ký của bốn tập”. Câu chốt định nghĩa khóa của cột ở dải $j$ là cặp $(j,\text{tuple})$ (trước đó “khóa” xuất hiện chưa định nghĩa). | Mục 2: câu mở vết chạy nêu khóa gồm số dải và tuple. |
| lec06-s02-03 | Dải 1: bốn lượt chèn tạo ba thùng; chỉ thùng $(1,(1))$ có hai mã và phát cặp $(1,4)$. | sửa nhẹ | Tiêu đề “Thùng của dải thứ nhất” → “Thùng của dải 1”. Cột “Khóa đầy đủ” → “Khóa (dải, tuple)”; ô “1 → 1, 4” khó đọc → “1, 4”; công thức $(1,4)$ đứng riêng → “Cặp phát ở dải 1: $(1,4)$”. | Không đổi; bảng vết chạy mục 2 đã có cùng thùng và cặp. |
| lec06-s02-04 | Dải 2 phát ba cặp; hợp với dải 1 cho $Q=4$ lượt phát, $\mathcal C$ có $K=3$ cặp phân biệt; $(1,4)$ phát hai lần nhưng xác minh một lần. | sửa nhẹ | Giữ tiêu đề. $Q$ và $K$ được gọi tên trên mặt trang (“số lượt phát trước khử lặp”, “số cặp phân biệt”); trước đó chỉ định nghĩa trong ghi chú, trong khi s02-13 dùng lại hai đại lượng này. | Mục 2: câu vết chạy nêu $Q=4$ đếm cả lần phát lại và $K=3$. |
| lec06-s02-05 | Xác minh ba ứng viên bằng Jaccard gốc ($1/4$, $2/3$, $1/5$); kết quả $\{(1,4)\}$. | sửa nhẹ | Giữ tiêu đề và bảng. Câu chốt gọi tên khái niệm trên ví dụ: $(1,3)$, $(3,4)$ là ứng viên giả; ý “xác minh không khôi phục cặp chưa được sinh” chuyển thành dòng phụ. | Không đổi; mục 2 đã định nghĩa ứng viên giả và có cùng ba giá trị Jaccard. |
| lec06-s02-07 | Đặc tả: đầu vào SIG, $b,r$, các tập, $t$; khóa dải; tập ứng viên $\mathcal C$; đầu ra là phần tử của $\mathcal C$ đạt ngưỡng. | sửa | Tiêu đề “Đặc tả bộ tạo ứng viên” → “Đặc tả phân dải và xác minh”. Thêm dòng “Đầu ra” (trước chỉ có đầu vào); các tập và $t$ đưa vào dòng đầu vào thay vì dòng chú thích; câu về bảng băm (chi tiết cài đặt) chuyển vào ghi chú. Ghi chú nêu đặc tả chưa bảo đảm không bỏ sót. | Mục 2: thêm công thức đầu ra sau xác minh. |
| lec06-s02-08 | Giả mã: dựng thùng theo khóa dải, phát và khử lặp cặp, xác minh Jaccard gốc. | sửa nhẹ | Tiêu đề “Thuật toán tạo và kiểm cặp” → “Thuật toán phân dải và xác minh” (khớp trang đặc tả). Thẻ vết chạy nối số đếm với ký hiệu dùng ở trang chi phí: $bC=8$, $Q=4$, $K=3$. Giả mã giữ nguyên. | Không đổi; mục 2 có cùng giả mã. |
| lec06-s02-09 | Bất biến dựng thùng; kết thúc cho đúng $\mathcal C$; xác minh cho đúng đầu ra trong $\mathcal C$. | sửa nhẹ | Tiêu đề “Bất biến và phạm vi tính đúng” → “Tính đúng của phân dải”. Hàng “Kết thúc” nêu bước suy luận quyết định (cùng nhóm khi và chỉ khi cùng khóa, nên hợp cho đúng $\mathcal C$) thay cho danh sách thao tác. Câu chốt thêm “cặp ngoài $\mathcal C$ không được xét”. | Không đổi; mục 2 có chứng minh đầy đủ. |
| lec06-s02-10 | Xác suất trùng một dải bằng $s^r$ dưới MinHash đều, độc lập. | sửa | Tiêu đề “Xác suất trùng trong một dải” → “Xác suất trùng một dải”. Thêm câu nối từ s02-09 (tính đúng chỉ xét cặp trong $\mathcal C$, cần xác suất vào $\mathcal C$). Định nghĩa $E_i$ viết bằng câu văn thay chữ tiếng Việt trong KaTeX. Số thập phân dùng dấu phẩy ($0{,}8^5=0{,}32768$). | Mục 3, tiểu mục “Mô hình xác suất”: đổi số thập phân sang dấu phẩy. |
| lec06-s02-11 | $P_{b,r}(s)=1-(1-s^r)^b$ qua biến cố bù; $P_{20,5}(0{,}8)\approx0{,}999644$. | sửa | Tiêu đề “Xác suất tạo ứng viên” → “Xác suất thành ứng viên”. Biến cố “không dải nào trùng” viết bằng câu văn thay chữ tiếng Việt trong KaTeX. Câu chốt kỹ thuật (“lấy biến cố bù…”) thay bằng cách đọc con số theo MMDS Ví dụ 3.12: khoảng 1 trên 3 000 cặp có Jaccard $0{,}8$ bị bỏ sót (tính lại: $1/0{,}000356\approx2\,808$, ghi ở ghi chú). Số thập phân dùng dấu phẩy. | Không đổi; ví dụ $s=0{,}8$ ở mục 3 đã đổi số ở commit trước. |
| lec06-s02-12 | Đường xác suất ứng viên dạng chữ S; điểm $P=1/2$ khác xấp xỉ $(1/b)^{1/r}$ và khác ngưỡng $t$; quy tắc chọn $b,r$. | viết lại | Tiêu đề “Ngưỡng và lựa chọn số dải” → “Đường cong S và chọn số dải”. Giữ hình; hai dòng nêu $s_{1/2}\approx0{,}509$ so với $(1/b)^{1/r}\approx0{,}549$ và bỏ sót tại $t=0{,}8$ của hai cấu hình ($0{,}036\%$ và $32\%$, trước chỉ có trong ghi chú; tính lại). Câu chốt là quy tắc bước 4 MMDS §3.4.3 (thấp hơn $t$ để ít bỏ sót, cao hơn để ít ứng viên giả) — trước đó trang không nêu cách chọn tham số. Số thập phân dùng dấu phẩy. | Mục 3, tiểu mục ngưỡng: đổi số thập phân, thêm quy tắc chọn $b,r$ theo §3.4.3. |
| lec06-s02-13 | Chi phí: dựng thùng $O(nC)$, phát cặp $O(Q)$, xác minh $\sum T_J$; bộ nhớ phụ $O(nC+K)$; xấu nhất $K=\binom C2$. | sửa | Tiêu đề “Chi phí tạo và xác minh ứng viên” → “Chi phí phân dải và xác minh”. Mô hình chi phí đưa lên đầu trang (tiêu chuẩn mục 5); định nghĩa $T_J$ trên mặt trang (trước chưa định nghĩa). Dòng tổng “bộ nhớ phụ” viết ngoài KaTeX. Câu chốt đưa kết luận trường hợp xấu (trước nằm ở dòng chú thích). Ghi chú thêm $\mathbb E[K]$ theo phân bố tương đồng. | Không đổi; mục 4 có cùng mô hình, bảng, trường hợp xấu và $\mathbb E[K]$. |
| lec06-s02-14 | Kiểm tra phân dải: đổi cấu hình trên cùng chữ ký, đánh đổi xác suất, nguồn ngẫu nhiên. | sửa | Tiêu đề “Kiểm tra phân dải và xác minh” → “Câu hỏi về phân dải”. Câu 1 cũ ($b=2,r=1$) trùng vết chạy s02-02…05 đã hiện đáp án; thay bằng $b=1,r=2$ ($Q=K=1$, loại hai ứng viên giả). Câu 2 tính $P_{2,1}$, $P_{1,2}$ tại $s=1/4$ ($7/16$, $1/16$) và $s=2/3$ ($8/9$, $4/9$), tính lại bằng phân số. Câu 3 giữ ý nguồn ngẫu nhiên. | Mục 2: bài tự kiểm thêm ý (b) với $b=1,r=2$. |
| lec06-s03-01 | Mở phần 3: phân dải chỉ phục vụ Jaccard; ví dụ $L_1=7$, $L_2=5$, $L_\infty=4$ cho cùng hai điểm. | sửa nhẹ | Giữ tiêu đề và ví dụ. Câu dẫn nêu rõ kết quả kế thừa và giới hạn (phân dải dùng MinHash nên chỉ phục vụ Jaccard; vector, chuỗi cần độ đo và phép băm khác). Thêm câu chốt rút từ ví dụ: “gần” phụ thuộc độ đo. | Mục 5: câu nối thêm nhu cầu phép băm riêng cho mỗi độ đo; sau ví dụ thêm nhận xét ngưỡng “gần” phụ thuộc độ đo. |
| lec06-s03-02 | Bốn tiên đề metric; chuẩn $L_q$ với $q\ge1$. | sửa nhẹ | Tiêu đề “Độ đo khoảng cách” → “Độ đo khoảng cách và chuẩn vector” (trang có hai thẻ). Câu chốt chung chung (“Miền và điều kiện tham số là một phần của định nghĩa”) thay bằng kết luận nối với ví dụ trước: $L_q$ thỏa bốn tiên đề khi $q\ge1$, $L_1,L_2,L_\infty$ là ba trường hợp. | Không đổi; mục 5 đã có định nghĩa và điều kiện $q\ge1$. |

**Rà lại phần 1–2 (tác tử chỉ đọc, `subagent_type: "fork"`, kế thừa Opus 5.5).** Độ chính xác đạt: 5,787 ngày; $4\,999\,950\,000$ cặp, 1,39 giờ; $P_{20,5}(0{,}8)\approx0{,}999644$; $1/0{,}000356\approx2\,808$ (khớp “roughly one in 3000”); $s_{1/2}=0{,}50870$, $20^{-1/5}=0{,}54928$; quy tắc bước 4 §3.4.3; câu hỏi s02-14. Không câu hỏi nào có đáp án trên mặt trang trước; việc chuyển s02-06 không tạo khoảng trống. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Trang | Phát hiện rà lại | Quyết định | Thay đổi |
|---|---|---|---|
| storyboard s01-04, s01-05, s02-03, s02-05, s02-12, s02-14 | (trung bình) Trường Dữ kiện, Bố cục, Kết nối còn mô tả bản cũ. | sửa | Viết lại theo HTML hiện tại. |
| storyboard s01-03, s02-10, s02-11, s02-12 | (nhẹ) Trường Dữ kiện còn dấu chấm thập phân. | sửa | Đổi sang dấu phẩy. |
| lec06-s02-01 → s02-05 | (nhẹ) “Ứng viên giả” dùng trên mặt s02-05 nhưng chỉ định nghĩa trong ghi chú. | sửa | Dòng phụ s02-01: “Cặp dưới ngưỡng vẫn thành ứng viên gọi là ứng viên giả.” |
| lec06-s01-04 | (nhẹ) “Cặp ứng viên” trước định nghĩa ở s02-01. | giữ | Dùng theo nghĩa thông thường như cầu nối; ghi chú đã nói cách tạo ứng viên được xây ở phần 2. |
| lec06-s02-12 | (nhẹ) Dòng nguồn ghi chú khác mặt trang. | sửa | Thống nhất “Ví dụ 3.12; §3.4.3”. |
| lec06-s02-12 (SVG) | (nhẹ) Nhãn trục `xac-suat-phan-dai.svg` dùng dấu chấm thập phân. | giữ, ghi ngoại lệ | Hình sinh bằng `generate_svg.py` dùng chung cho nhiều SVG; không sửa hình trong lượt duyệt văn bản này. Nêu để xử lý trong một lượt sửa hình riêng. |
| lec06-s02-13 | (nhẹ) $s_{cd}$ chưa định nghĩa trong ghi chú. | sửa | Thêm “với $s_{cd}=\mathrm{SIM}(S_c,S_d)$”. |
| lec06-s03-03 | $d_J=1-\mathrm{SIM}=\Pr[h(A)\ne h(B)]$; bất đẳng thức tam giác qua bao hàm biến cố và chặn hợp. | sửa nhẹ | Giữ tiêu đề. Sắp lại thứ tự định nghĩa → ví dụ $d_J(S_1,S_4)=1/3$ → chứng minh (trước đó ví dụ đứng trước định nghĩa). Câu chốt nêu lý do của phép bao hàm (trước chỉ trong ghi chú). | Không đổi; mục 5 có cùng lập luận. |
| lec06-s03-04 | Khoảng cách góc $\theta=\arccos(x\cdot y/\|x\|\|y\|)$; Ví dụ 3.14 cho $60^\circ$; góc là metric trên hướng. | sửa nhẹ | Giữ tiêu đề. Thêm dòng định nghĩa tổng quát với điều kiện $x,y\ne0$ và miền $[0,\pi]$ trước dữ kiện (trước đó khái niệm chỉ hiện qua ví dụ). | Không đổi; mục 5 đã có định nghĩa. |
| lec06-s03-05 | Khoảng cách chỉnh sửa (chèn, xóa) $=|x|+|y|-2L$; ví dụ `abcde` → `acfdeg` bằng 3. | sửa nhẹ | Giữ tiêu đề. Bỏ dòng công thức lặp dãy biến đổi đã có trong bảng (chuỗi bị in nghiêng như biến); chuỗi ghi dạng mã. Định nghĩa $L$ (dãy con chung dài nhất) đặt trước công thức thay vì ở dòng chú thích sau. | Không đổi; mục 5 có cùng định nghĩa và ví dụ. |
| lec06-s03-06 | Hamming đếm vị trí khác của hai vector cùng chiều; Ví dụ 3.17 cho $d_H=3$. | giữ | Tiêu đề, bảng so từng vị trí, công thức và ký hiệu chỉ báo đạt. | Không đổi. |
| lec06-s03-07 | Định nghĩa họ $(d_1,d_2,p_1,p_2)$-nhạy cảm: cặp gần trùng với xác suất $\ge p_1$, cặp xa $\le p_2$, xác suất theo cách chọn $h$. | sửa | Tiêu đề “Họ băm nhạy cảm” → “Họ băm nhạy cảm theo tính cục bộ”. Thêm câu dẫn khái quát từ MinHash (trước đó trang mở thẳng bằng ràng buộc tham số). Định nghĩa phát biểu thành câu có điều kiện trước hình. Câu chốt (trước chỉ nhắc tên họ bằng chữ thường) nêu nguồn ngẫu nhiên và miền giữa. | Mục 6: câu mở thêm MinHash là ví dụ đầu tiên và định nghĩa giữ lại tính chất ấy. |
| lec06-s03-08 | Định lý MinHash cho xác suất trùng $1-d_J$, nên MinHash là họ $(d_1,d_2,1-d_1,1-d_2)$-nhạy cảm; Ví dụ 3.18. | sửa | Giữ tiêu đề. Dòng đầu nêu căn cứ (định lý MinHash). Hai thẻ viết bằng câu văn thay “P(trùng)” là chữ tiếng Việt trong KaTeX. Số thập phân dùng dấu phẩy; bộ tham số dùng dấu chấm phẩy làm phân cách $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$ để không lẫn với dấu phẩy thập phân. Câu chốt là phát biểu tổng quát. | Mục 6, tiểu mục hai bảo đảm: đổi số thập phân, bộ tham số dùng dấu chấm phẩy; bài tự kiểm tách ba giá trị $d$. |
| lec06-s03-09 | Phép ghép AND: $r$ hàm độc lập, xác suất $p^r$, họ $(d_1,d_2,p_1^r,p_2^r)$; trùng một dải là AND $r$ MinHash. | sửa | Giữ tiêu đề. Thêm câu dẫn nêu nhu cầu khuếch đại khoảng cách $p_1$–$p_2$ và nối với phân dải (MMDS §3.6.3); nêu họ mới trên mặt trang. Bảng bỏ cột “r=4” thừa, còn $p$ và $p^4$; số thập phân dấu phẩy. Câu chốt đọc ra đánh đổi (cặp gần cũng giảm xuống khoảng 0,41) thay cho “tính đơn điệu chuyển cận của họ”. | Mục 6, tiểu mục phép ghép: đổi số thập phân; thêm câu “phân dải là AND rồi OR trên họ MinHash”. |
| lec06-s03-10 | Phép ghép OR: xác suất $1-(1-p)^b$, họ biến đổi tương ứng; OR tăng cả hai xác suất; hợp các dải là OR. | sửa | Giữ tiêu đề. Hai công thức có chữ tiếng Việt trong KaTeX viết lại bằng câu văn. Thêm câu nối với AND và phân dải, họ mới trên mặt trang, bảng $p$ và $1-(1-p)^4$ ($0{,}9984$; $0{,}8704$, tính lại) đối xứng với trang AND. Câu chốt nêu vai trò của OR sau AND; ý “không bắc cầu” chuyển vào ghi chú. | Không đổi thêm; mục 6 đã có chứng minh OR và câu nối phân dải (commit trước). |
| lec06-s03-11 | Hai thứ tự ghép trên họ $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$: AND 4 → OR 4 cho $0{,}878$ và $0{,}099$; OR 4 → AND 4 cho $0{,}994$ và $0{,}574$. | sửa | Tiêu đề “Thứ tự ghép và xác suất” → “So sánh hai thứ tự ghép”. Số thập phân dấu phẩy, bộ tham số dùng dấu chấm phẩy. Câu chốt nêu kết luận so sánh (AND–OR mở rộng khoảng cách hai cận; OR–AND nhận cặp xa tới $0{,}57$), tính lại. Ghi chú phụ viết $p_1,p_2$ bằng KaTeX. | Không đổi; mục 6 đã đổi số ở commit s03-09. |
| lec06-s03-12 | AND 4 rồi OR 4 thực hiện bằng 4 tuple, 4 bảng và hợp cặp; chính là phân dải với $b=r=4$. | sửa nhẹ | Tiêu đề “Cơ chế thực hiện phép ghép” → “Thực hiện AND rồi OR bằng phân dải”. Dòng các bước nêu kết luận nối hai phần: AND rồi OR chính là phân dải. Hình, câu chốt và ghi chú giữ. | Không đổi; mục 6 có câu “phân dải là AND rồi OR trên họ MinHash” (commit s03-09). |
| lec06-s03-13 | Kiểm tra phần 3: phép ghép trên họ MinHash, khoảng cách chỉnh sửa, góc. | sửa | Tiêu đề “Kiểm tra độ đo và phép ghép” → “Câu hỏi về độ đo và phép ghép”. Câu 1 cũ có đáp án trên s03-07/08; câu 2 cũ trùng Bài 3.6.1(a) của phần bài tập; câu 3 cũ có đáp án ở dòng phụ s03-04. Thay bằng: AND 2 rồi OR 2 trên $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$ ($0{,}7399$; $0{,}2944$); khoảng cách chỉnh sửa `abc`–`bca` (2); góc giữa $(1,1,0)$ và $(1,0,0)$ ($45^\circ$). Tính lại bằng chương trình. | Mục 6: bài tự kiểm thêm ý (b) AND 2 rồi OR 2, có lời giải. |
| lec06-s04-01 | Mở phần 4: họ băm chọn tọa độ $h_I(x)=x_I$ cho Hamming; trên $x,y$ của s03-06 có $D-d_H=2$ chỉ số cùng giá trị băm. | sửa | Tiêu đề “Băm bằng một tọa độ” → “Họ băm chọn tọa độ”. Câu dẫn cũ (tính metric chưa bảo đảm họ LSH) chuyển vào ghi chú làm câu nối với phần 3; câu dẫn mới nêu họ cho Hamming và giả thiết $D>0$. Công thức hàm đặt trước bảng; hàng bảng ghi $h_I(x)$, $h_I(y)$, “Cùng giá trị băm”. Bỏ hai thẻ $I=1$, $I=2$ lặp lại bảng. Câu chốt đếm $D-d_H(x,y)=2$, dẫn trực tiếp tới xác suất ở s04-02. | Ghi chú bài giảng mục “Chọn tọa độ cho Hamming” đã có cùng thứ tự và ví dụ; không đổi. |
| lec06-s04-02 | Xác suất va chạm $1-d_H/D$ chứng minh bằng đếm chỉ số thuận lợi; họ chọn tọa độ là $(d_1,d_2,1-d_1/D,1-d_2/D)$-nhạy cảm. | sửa | Tiêu đề “Xác suất va chạm Hamming” → “Tính nhạy cảm của họ chọn tọa độ”. Câu dẫn nêu lý lẽ đếm thay cho dòng giả thiết rời. Thêm bộ tham số nhạy cảm (MMDS §3.7.1) để nối trực tiếp với định nghĩa s03-07; trước đó trang chỉ có xác suất mà không kết luận họ thuộc loại nào. Ghi chú bổ sung vì sao xác suất giảm theo $d_H$ cho hai điều kiện. | Ghi chú bài giảng mục “Chọn tọa độ cho Hamming” thêm câu về bộ tham số nhạy cảm. |
| lec06-s04-03 | Hàm băm dấu $h_v(x)=\operatorname{sign}(v\cdot x)$: phía của siêu phẳng qua gốc chứa $x$; ví dụ $v_1$ cho $x,y$ cùng dấu. | sửa | Tiêu đề “Dấu của tích vô hướng” → “Hàm băm dấu theo siêu phẳng”. Định nghĩa từ cuối trang lên đầu, kèm câu dẫn về siêu phẳng qua gốc và pháp tuyến. Kết luận ví dụ viết bằng giá trị băm. Thêm câu chốt: giá trị băm chỉ phụ thuộc hướng, phù hợp khoảng cách góc; lý do (nhân với $c>0$) ở ghi chú. Nguồn bổ sung §3.7.2. Phát hiện thứ tự: s04-04 dùng $p_{\ne}=\theta/\pi$ trước khi s04-05 chứng minh; xử lý ở hai trang sau. | Ghi chú bài giảng mục “Siêu phẳng, chữ ký dấu và góc” thêm câu về tính chỉ phụ thuộc hướng. |

### Rà lại phần 3

Tác tử rà chỉ đọc: vai trò chính xác toán–thuật toán, mạch lập luận và tiếng Việt học thuật; kiểu `fork` của công cụ Agent, mô hình Claude Opus 5.5, effort `high`; phạm vi s03-01…13, hai trang biên s02-14 và s04-01, hai mục ghi chú tương ứng, phiếu storyboard. Tác tử tính lại mọi số (L₁/L₂/L∞, $d_J(S_1,S_4)$, góc $\pi/3$, khoảng cách chỉnh sửa, $p^4$, $1-(1-p)^4$, $F$, $G$, ba đáp án s03-13), tất cả đúng, và không có đáp án câu hỏi nào lộ trên trang trước. Một lần chạy đầu dừng mà không có báo cáo; một lần chạy lại bị dừng vì trùng việc với tác tử đã trả báo cáo đầy đủ.

| Mức độ | Trang chiếu | Vấn đề | Quyết định |
|---|---|---|---|
| nghiêm trọng | s03-07 | Hai điều kiện của định nghĩa chỉ có trong SVG; nhãn hình “P(trùng)” lệch ký hiệu. | Đã sửa: thêm hai phép kéo theo bằng KaTeX với $P=\Pr[h(x)=h(y)]$, đặt cạnh hình; nhãn SVG (và `generate_svg.py`) đổi thành “Pr[h(x)=h(y)]”. |
| trung bình | s03-09, s03-11, s03-13; ghi chú (b) | “Khoảng cách” vừa chỉ độ đo $d$, vừa chỉ hiệu $p_1-p_2$. | Đã sửa: dùng “độ chênh $p_1-p_2$”; bỏ “khoảng 0,88”; đáp án ghi $0{,}4455$. |
| trung bình | s03-11/12 ↔ s02-14 | Không nối $F(p)$ với đường cong S $P_{b,r}(s)$. | Đã sửa: dòng phụ s03-12 “Với họ MinHash, $p=s$ nên $F(s)=P_{4,4}(s)$”. |
| trung bình | s03-12 (SVG) | Nhãn “Mỗi hàng tạo một tuple” gọi dải là hàng. | Đã sửa: “Mỗi dải tạo một tuple” (SVG và bộ sinh). |
| trung bình | ghi chú “Ghép đồng thời…” | Bộ tham số thập phân phân tách bằng dấu phẩy. | Đã sửa: $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$. |
| nhẹ | s03-04 | “$1-\cos\theta$ khác $\theta$” trơ; ghi chú thiếu bất đẳng thức tam giác. | Đã sửa: dòng phụ nêu $\pi/3$ so với $1/2$; ghi chú thêm lập luận cung trên mặt cầu. |
| nhẹ | s03-09 | $p$ chưa định nghĩa trên mặt trang. | Đã sửa: “Với $p=\Pr[h(x)=h(y)]$ của một cặp cố định”. |
| nhẹ | s03-03, s03-10, s03-11 | Ghi chú lặp mặt trang. | Đã sửa: bỏ câu lặp; s03-10 nêu vai trò độc lập; s03-11 nêu lý do $F$, $G$ tăng bảo toàn hướng cận. |
| nhẹ | s03-05 | LCS chưa viết đầy đủ tiếng Việt. | Đã sửa trong ghi chú. |
| nhẹ | s03-06 | Ghi chú nhắc họ chọn tọa độ trước định nghĩa họ. | Đã sửa: bỏ câu; giả thiết $D>0$ đã có trên mặt trang s04-01. |
| nhẹ | s03-02 | Câu vụng; thiếu căn cứ tam giác cho $q\ge1$. | Đã sửa: “$d$ nhận giá trị không âm”; thêm bất đẳng thức Minkowski. |
| nhẹ | s03-01 | Alt nói hình có ba khoảng cách; câu chốt dạng dấu hai chấm. | Đã sửa alt theo hình (chỉ ghi $L_2=5$) và câu chốt. |
| nhẹ | s03-08/09/10/12 | “chính là” lặp, “kéo… lên lại”, câu tương phản. | Đã sửa: “tương ứng với”, “tăng lại cận gần”; ghi chú s03-08 viết lại. |

Kiểm hiển thị lại s03-01, 04, 07, 09, 11, 12 ở 1600×900 và 390×844: không lỗi KaTeX, không tràn khung 16:9, không lỗi console, không yêu cầu mạng ngoài. Ghi chú bài giảng kiểm ở 1440 màn hình, 390 và in.
| lec06-s04-05 | Chứng minh $\Pr[h_v(x)=h_v(y)]=1-\theta/\pi$ dưới pháp tuyến đẳng hướng; họ siêu phẳng $(d_1,d_2,1-d_1/\pi,1-d_2/\pi)$-nhạy cảm. | tách thứ tự, sửa | Dời lên trước s04-04 (thứ tự trình chiếu 4.4) vì s04-04 cũ dùng $p_{\ne}=\theta/\pi$ trước khi trang này chứng minh; thứ tự mới khớp MMDS (§3.7.2 rồi §3.7.3). Tiêu đề “Xác suất cùng phía siêu phẳng” → “Tính nhạy cảm của họ siêu phẳng”. Bỏ chữ Việt trong KaTeX (“khác dấu”, “cùng dấu”) bằng $\Pr[h_v(x)\ne h_v(y)]$. Định nghĩa “đẳng hướng” trên mặt trang. Thêm bộ tham số nhạy cảm làm câu chốt (MMDS viết theo độ). | Ghi chú mục “Siêu phẳng, chữ ký dấu và góc” sắp lại: định nghĩa → mệnh đề và chứng minh → bộ tham số → chữ ký và quy tắc ước lượng → Ví dụ 3.22 → chi phí; câu hỏi tự kiểm bỏ chữ Việt trong KaTeX; $38{,}047579^\circ$. |
| lec06-s04-04 | Chữ ký dấu $m$ bit và quy tắc $\widehat\theta=\pi\widehat p_{\ne}$ trên Ví dụ 3.22: $120^\circ$ so với góc thật $38{,}05^\circ$. | sửa | Tiêu đề “Chữ ký dấu và góc ước lượng” → “Chữ ký dấu và ước lượng góc”. Câu dẫn dựa vào quan hệ đã chứng minh ở trang trước. Đầu cột bảng ghi $v_i\cdot x$, $v_i\cdot y$; dấu trừ thống nhất “−”. Số thập phân dấu phẩy. Thêm câu chốt tách hai nguồn sai lệch (mẫu nhỏ, pháp tuyến không đẳng hướng); ghi chú đưa phép tính góc thật và trường hợp 16 pháp tuyến. Nguồn ghi §3.7.3. | Như trên. |
| lec06-s04-06 | Mở cụm Euclid: giữ độ lớn tọa độ chiếu bằng cách chia trục thành khoảng rộng $a$; trục thứ nhất của Bài 3.7.5 cho ba mã khác nhau. | sửa | Tiêu đề “Chiếu điểm vào các khoảng” → “Chia trục chiếu thành khoảng”. Thêm câu dẫn nêu nhu cầu (hàm dấu bỏ độ lớn, khoảng cách Euclid cần độ lớn). Ba điểm đổi tên $p_1,p_2,p_3$ → $z_1,z_2,z_3$ vì trùng ký hiệu hai cận $p_1,p_2$ của họ nhạy cảm; dữ kiện và yêu cầu bài không đổi, tên gốc của sách ghi trong ghi chú s04-06, s07-06, ghi chú bài giảng và outline (V11). Khoảng chứa viết bằng KaTeX. Ghi chú nêu biên cố định tách cặp gần, dẫn sang phép dịch ở s04-07. | Ghi chú bài giảng: ví dụ mục “Phép chiếu Euclid…” và Bài 3.7.5(a–c) đổi tên điểm, ghi tên gốc. |
| lec06-s04-07 | Định nghĩa họ $h_{u,\delta}(x)=\lfloor(u\cdot x+\delta)/a\rfloor$: hướng $u$ đều, dịch $\delta$ đều trên $[0,a)$ độc lập. | sửa | Tiêu đề “Họ chiếu với dịch ngẫu nhiên” → “Họ chiếu có dịch ngẫu nhiên”. Thêm câu dẫn nêu nhu cầu (biên cố định tách cặp gần) để phép dịch không xuất hiện đột ngột. Diễn đạt “$u$ đều hướng đơn vị” → “$u$ là hướng đơn vị chọn đều”. Câu chốt nêu khoảng của mã $k$ và yêu cầu dùng chung $(u,\delta)$. Hình `chia-khoang-dich.svg`: nhãn “u · y” đè lên biên, dời nhãn và thu cỡ chữ (sửa cả `generate_svg.py`). Ghi chú nêu trục cố định là trường hợp riêng $\delta=0$. | Ghi chú bài giảng đã có cùng định nghĩa, khoảng của mã $k$ và lý do dịch; không đổi. |
| lec06-s04-08 | Cố định $u$: $\Pr_\delta[h(x)=h(y)\mid u]=\max(0,1-\ell/a)$ với $\ell$ là khoảng cách hai hình chiếu. | sửa | Tiêu đề “Xác suất chung khoảng chiếu” → “Xác suất chung thùng khi cố định hướng”. Bỏ chữ Việt trong KaTeX (“khác thùng”, “chung thùng”): lập luận của hai trường hợp viết bằng câu văn, kết luận chung viết bằng một công thức. Tiêu đề thẻ viết bằng KaTeX. Câu dẫn nói rõ chỉ $\delta$ còn ngẫu nhiên. Thêm câu chốt nối sang bước lấy trung bình theo $u$ ở s04-09. Ghi chú xét thêm trường hợp $\ell=0$. Nguồn ghi tr.112. | Ghi chú bài giảng đã có chứng minh ba trường hợp; không đổi. |
| lec06-s04-09 | Lấy trung bình theo $u$: cặp gần $\rho\le a/2$ có $P\ge1/2$, cặp xa $\rho\ge2a$ có $P\le1/3$; họ chiếu hai chiều $(a/2,2a,1/2,1/3)$-nhạy cảm. | sửa | Tiêu đề “Cận xác suất trong mặt phẳng” → “Tính nhạy cảm của họ chiếu hai chiều” (song song s04-02, s04-05). Câu dẫn bỏ giả thiết lặp s04-07, thay bằng định nghĩa $\rho$, $P$ và phép lấy trung bình kết quả s04-08. Tiêu đề hai cột và bộ tham số viết bằng KaTeX, có hậu tố “-nhạy cảm”. Chuỗi suy luận cặp xa gộp thành một dòng; nêu căn cứ “$u$ đều trong $\mathbb R^2$ nên $\phi$ đều”. Ghi chú bỏ câu lặp mặt trang, thêm lý do hằng số $1/3$ không chuyển sang chiều cao và nối với phép ghép AND/OR (dùng “độ chênh”). | Ghi chú bài giảng đã có hai chứng minh và giới hạn số chiều; không đổi. |
| lec06-s04-10 | Chi phí tính chữ ký của ba họ: đếm phép tính một hàm, thời gian, tham số lưu; $C\cdot m$ lần tính. | sửa | Tiêu đề “Chi phí các phép băm cơ sở” → “Chi phí tính chữ ký theo họ băm”. Theo quy định chi phí, bảng đếm phép tính của một hàm ($D$ nhân, $D-1$ cộng…) trước cột tiệm cận và tách cột tham số lưu; mô hình chi phí nêu ở câu dẫn; nguồn ghi rõ là số đếm từ định nghĩa. Dòng tổng $C\cdot m$ viết bằng câu văn, không dùng chữ Việt trong KaTeX. Câu chốt nối với $Q$, $K$ của phần 2. Ghi chú tách bộ nhớ tham số và bộ nhớ chữ ký, thêm trường hợp vector thưa. | Ghi chú bài giảng thêm mục “Chi phí tính chữ ký của ba họ” với cùng bảng và một bài tự kiểm. |
| lec06-s04-11 | Kiểm tra phần 4 bằng dữ kiện mới. | sửa | Tiêu đề “Kiểm tra các họ theo độ đo” → “Câu hỏi về các họ theo độ đo”. Ba câu cũ có đáp án trên mặt trang trước ($10101/11110\to2/5$ ở s04-01/02; $\pi/3\to2/3$ ở s04-05; điều kiện cận Euclid ở s04-07/09). Thay bằng: $11001/10011$ cho $3/5$ và AND 2 cho $0{,}36$; $(1,0),(-1,1)$ có $\theta=3\pi/4$, xác suất cùng dấu $1/4$; $a=2$, $\ell=0{,}5$ cho $0{,}75$ và cặp $\rho=5\ge2a$ có cận trên $1/3$ (đã tính lại). Câu cuối viết dạng yêu cầu “Xác định”. | Như s04-10. |
| lec06-s05-01 | Đối sánh thực thể: ba hàm khóa trùng hoàn toàn, OR tạo ứng viên, rồi chấm điểm; cặp không trùng khóa nào bị bỏ sót. | sửa | Giữ tiêu đề. Câu dẫn nêu đầu ra (cặp hồ sơ cùng một người) và chi phí $10^{12}$ bằng KaTeX. Thêm dòng nối với phần 3–4: ba khóa là ba hàm, ứng viên là OR (ghi chú: phân dải $b=3$, $r=1$; sách dùng ba lần sắp xếp thay bảng băm). Câu chốt nêu hệ quả bỏ sót (MMDS §3.8.2). Dòng phụ “trường phụ không tham gia tính điểm” xuất hiện đột ngột trên mặt trang, chuyển vào ghi chú cùng tên trường cụ thể (ngày tạo hồ sơ) và chỉ dẫn mục Đọc thêm. Ghi chú nêu quy tắc chấm điểm 100 mỗi trường, phạt theo bình phương khoảng cách chỉnh sửa. | Ghi chú bài giảng mục “Đối sánh thực thể” thêm câu về phép OR, phân dải $b=3,r=1$ và bỏ sót; câu hỏi tự kiểm viết dạng yêu cầu. |
| lec06-s05-02 | Họ băm ba ô: ảnh có điểm đặc trưng ở đủ ba ô vào thùng chung, ảnh khác vào thùng đơn. | sửa | Tiêu đề “Biểu diễn và thùng vân tay” → “Họ băm ba ô cho vân tay” (gọi đúng là một họ LSH như MMDS §3.8.5). Câu dẫn định nghĩa “điểm đặc trưng” trước khi dùng (trước đây ở gạch đầu dòng sau hình). Gạch đầu dòng nêu hàm $f$ ứng với ba ô ngẫu nhiên. Ghi chú thêm lý do không dùng MinHash (lưới khoảng 1000 ô) và hai dạng bài toán một–nhiều, nhiều–nhiều. | Ghi chú bài giảng mục “Đối sánh vân tay” thêm hai câu tương ứng. |

### Rà lại phần 4

Tác tử rà chỉ đọc: vai trò chính xác toán–thuật toán, mạch lập luận và tiếng Việt học thuật; kiểu `fork` của công cụ Agent, mô hình Claude Opus 5.5, effort `high`; phạm vi phần 4 theo thứ tự trình chiếu (s04-05 trước s04-04), hai trang biên s03-13 và s05-01, mục ghi chú “Ba họ băm theo độ đo”, Bài 3.7.5(a–c), phiếu storyboard. Tác tử tính lại mọi số (Hamming $2/5$, $3/5$, $9/25$; sáu tích vô hướng; $120^\circ$ và $38{,}047579^\circ$; liệt kê 16 vector dấu cho $45^\circ$; $3\pi/4\to1/4$; $0{,}75$; cận $1/2$, $1/3$; phép đếm chi phí), tất cả đúng. Không còn kết quả dùng trước khi chứng minh; không còn chữ Việt trong KaTeX; đáp án s04-11 không lộ trên trang trước.

| Mức độ | Trang chiếu | Vấn đề | Quyết định |
|---|---|---|---|
| nghiêm trọng | s04-07 (ghi chú) | Mã trang chiếu trong ghi chú diễn giả. | Đã sửa: “Trục cố định ở trang trước…”; quét lại mọi ghi chú, không còn mã trang. |
| trung bình | storyboard s04-08, s04-10, s04-11 | Trường Bố cục/Đầu vào không khớp trang hiện tại. | Đã sửa ba trường. |
| trung bình | ghi chú, “Chi phí tính chữ ký của ba họ” | Bài tự kiểm hỏi xác suất, không hỏi chi phí. | Đã sửa: bài đếm phép nhân, từ lưu pháp tuyến và bit chữ ký với $C=10^6$, $D=1000$, $m=200$ ($2\cdot10^{11}$; $2\cdot10^5$; $2\cdot10^8$). |
| nhẹ | s04-03, s04-10; ghi chú | $z$ mang nhiều nghĩa. | Đã sửa: siêu phẳng viết $\{x: v\cdot x=0\}$ (khớp nhãn hình); $\operatorname{sign}(t)$ trong ghi chú; số thành phần khác 0 viết $\mathrm{nnz}(x)$. |
| nhẹ | s04-06 | Mã viết $\lfloor x_1/a\rfloor$ khi điểm tên $z_i$. | Đã sửa bằng câu văn. |
| nhẹ | s04-04 | $p_{\ne}$ chưa định nghĩa. | Đã sửa: $p_{\ne}=\Pr[h_v(x)\ne h_v(y)]=\theta/\pi$; câu dẫn tách hai dòng. |
| nhẹ | s04-07 (ghi chú) | Ví dụ ba chiều, họ định nghĩa hai chiều. | Đã sửa: hàm chiếu áp dụng mọi số chiều, chỉ chứng minh cận dùng hai chiều. |
| nhẹ | s04-04 | Câu chốt dạng dấu hai chấm. | Đã sửa: “…vì chỉ có ba bit…”. |
| nhẹ | ghi chú s04-02, s04-03, s04-07 | Câu tương phản, câu nói về tài liệu. | Đã sửa. |
| nhẹ | s04-05 (hình) | Nhãn nói hướng pháp tuyến đều, thực tế là hướng hình chiếu. | Đã sửa SVG và bộ sinh. |
| nhẹ | s04-07 (hình) | Dấu trừ “-” trong nhãn $k$. | Đã sửa thành “−” trong SVG và bộ sinh. |
| nhẹ | ghi chú, mục Hamming | $\Sigma$ chưa định nghĩa. | Đã sửa. |

Kiểm hiển thị lại s04-03…07 ở 1600×900 và 390×844: không lỗi KaTeX, không tràn khung, không lỗi console, không yêu cầu mạng ngoài. Ghi chú bài giảng kiểm ở 1440, 390 và in.
| lec06-s05-03 | Xác suất cùng có đủ ba ô: $q_F=0{,}000064$, $q_T=0{,}004096$; một hàm chưa đủ, cần ghép. | sửa | Tiêu đề “Xác suất cơ sở của mô hình vân tay” → “Xác suất va chạm của hàm ba ô”. Số thập phân chuyển sang dấu phẩy ($0{,}2$; $0{,}8$; $0{,}04$; $0{,}16$). Giả thiết độc lập của các ô đưa lên câu dẫn. Câu chốt mới nêu $q_T\approx1/244$ và nhu cầu ghép, nối với s05-04; dòng phụ cũ về chọn ô trước khi xét ảnh chuyển vào ghi chú (đã có ở s05-02). Ghi chú thêm tỷ số $q_T/q_F=64$ và chỉnh “khoảng một phần 200” của MMDS thành $1/244{,}14$. Nguồn ghi §3.8.5. | Ghi chú bài giảng mục “Đối sánh vân tay”: toàn bộ số thập phân chuyển sang dấu phẩy; thêm câu về $1/244$ và tỷ số 64. |
| lec06-s05-04 | OR 1024 và AND hai nhóm OR 1024: $0{,}0634/0{,}0150$ so với $0{,}00402/0{,}0297$. | sửa | Giữ tiêu đề. Thêm câu dẫn nêu vai trò của từng phép ghép (nối từ $q_T$ nhỏ ở s05-03). Cột bảng đổi tên “Ứng viên giả”, “Bỏ sót” thành “Nhận cặp khác ngón”, “Bỏ sót cặp cùng ngón” để khớp mô hình hai loại cặp; số thập phân dấu phẩy, làm tròn ba chữ số có nghĩa trên mặt trang, giá trị đầy đủ ở ghi chú (đã tính lại). Hai công thức gộp một dòng. Câu chốt định lượng: giảm khoảng 16 lần, bỏ sót gấp đôi. Ghi chú thêm tỷ lệ kho phải so trong bài toán một–nhiều ($6{,}3\%$, khoảng $1/250$). | Ghi chú bài giảng thêm câu định lượng và tỷ lệ kho phải so. |
| lec06-s05-05 | Shingle gồm từ dừng và hai từ kế tiếp; tập trung ở văn xuôi nên Jaccard phản ánh phần bản tin. | sửa | Tiêu đề “Shingle cho bản tin gần trùng” → “Shingle theo từ dừng cho bản tin”. Câu dẫn mới nêu bài toán (bản tin đăng lại kèm quảng cáo khác, cần cùng văn bản gốc) trước khi định nghĩa từ dừng; trước đây trang mở bằng định nghĩa từ dừng mà chưa có nhu cầu. Câu chốt nêu hệ quả cho Jaccard; ghi chú thêm so sánh $0{,}75$ / $0{,}25$ / $1/3$ của MMDS với shingle 10 ký tự. Dòng phụ “your laundry x” và câu “câu dài cũng có thể là quảng cáo” chuyển vào ghi chú (câu sau là đáp án của s05-06 cũ). | Ghi chú bài giảng mục “Bản tin gần trùng” thêm đoạn so sánh Jaccard; câu hỏi tự kiểm viết dạng yêu cầu. |
| lec06-s05-06 | Kiểm tra phần 5: khóa địa chỉ tạo ứng viên, chấm điểm quyết định; OR 512 cho $0{,}0322$ và bỏ sót $0{,}1223$; ba shingle từ dừng. | sửa | Tiêu đề “Kiểm tra điều kiện của ứng dụng” → “Câu hỏi về các ứng dụng”. Ba câu cũ dạng “Vì sao…”, câu 3 có đáp án trên mặt trang s05-05 cũ và câu 1 trùng bài tự kiểm của ghi chú. Thay bằng ba yêu cầu tính/xác định: cặp tên MMDS §3.8.1 (“Bob S. Jomes”/“Robert Jones Jr.”) cùng địa chỉ; OR 512 với $q_F,q_T$ (tính lại: $0{,}0322$, $0{,}1223$); câu mới cho shingle từ dừng. | Ghi chú bài giảng không có mục tương ứng; không đổi. |
| lec06-s06-01 | Ba bước của quy trình gắn với kết quả từng phần; ba ứng dụng chỉ thay bước 1 hoặc 2. | sửa | Giữ tiêu đề. Ba bước viết lại để nêu kết quả kế thừa (các độ đo của phần 3; họ $(d_1,d_2,p_1,p_2)$ và AND–OR là phân dải; $Q$, $K$ và xác minh của phần 2). Câu chốt cũ về “kho triệu tài liệu” lặp ý s06-02 nên thay bằng nhận xét tổng hợp phần 5: ứng dụng nào đổi bước nào. Ghi chú nêu vai trò của từng bước. | Ghi chú bài giảng mục “Tổng hợp và tự kiểm” thêm câu về ba ứng dụng. |
| lec06-s06-02 | $P_{b,r}(s)$, $Q$, $K$ và hệ quả; xác minh loại ứng viên giả nhưng không lấy lại cặp bỏ sót. | sửa | Tiêu đề “Giới hạn chi phí và sai số” → “Chi phí và hai loại sai số”. Bảng thêm cột “Hệ quả”; $P(s)$ viết đúng ký hiệu $P_{b,r}(s)$ của phần 2 và nêu xác suất bỏ sót $1-P_{b,r}(s)$. Trường hợp xấu nhất nêu hệ quả “không nhanh hơn so mọi cặp”. Câu chốt cũ chỉ là lời báo trước Bài 07, thay bằng kết luận về hai loại sai số; nội dung nối sang Bài 07 chuyển vào ghi chú cùng lý do (bảo đảm theo cặp, chi phí theo phân bố thùng). | Ghi chú bài giảng mục “Tổng hợp và tự kiểm” thêm câu về hai loại sai số và trường hợp xấu nhất. |

### Rà lại phần 5

Tác tử rà chỉ đọc: vai trò chính xác toán–thuật toán, mạch lập luận và tiếng Việt học thuật; kiểu `fork` của công cụ Agent, mô hình Claude Opus 5.5, effort `high`; phạm vi s05-01…06, hai trang biên s04-11 và s06-01, mục ghi chú “Ba ứng dụng tìm cặp”, phiếu storyboard. Tác tử tính lại mọi số ($q_F$, $q_T$, $1/244{,}14$, tỷ số 64; OR 1024; AND hai nhóm; $15{,}76$ lần và $1{,}985$ lần; $1/248{,}5$; OR 512; $0{,}75$/$0{,}25$/$1/3$; các danh sách shingle), tất cả đúng; không có chữ Việt trong KaTeX, mã trang hay thời lượng trong ghi chú; đáp án s05-06 không lộ trước.

| Mức độ | Trang chiếu | Vấn đề | Quyết định |
|---|---|---|---|
| trung bình | s05-04 ↔ ghi chú | Thuật ngữ lệch: deck “nhận cặp khác ngón”, ghi chú “ứng viên giả”. | Đã sửa: ghi chú dùng “xác suất nhận cặp khác ngón (ứng viên giả)” và “bỏ sót cặp cùng ngón”. |
| trung bình | storyboard s05-04, s05-05, s05-06 | Trường Bố cục/Dữ kiện không khớp trang. | Đã sửa ba trường. |
| nhẹ | s05-01 | “OR của ba hàm” có thể gợi áp công thức $1-(1-p)^b$ cho ba hàm cố định. | Đã sửa: “cấu trúc của phép OR”; ghi chú (deck và bài giảng) nêu ba hàm cố định nên không áp công thức. |
| nhẹ | s05-04 | Công thức không nhãn, chỉ ứng với hàng AND. | Đã sửa: “Với AND 2 nhóm: …”. |
| nhẹ | s05-05 | Không báo shingle thứ năm. | Đã sửa: thêm “your laundry …”. |
| nhẹ | s05-05 | Phần chèn giữa câu vụng. | Đã sửa bằng ngoặc đơn. |
| nhẹ | s05-03, s05-04 (ghi chú) | Câu lặp mặt trang. | Đã bỏ. |
| nhẹ | ghi chú “Đối sánh thực thể”, “Bản tin gần trùng” | Đáp án bài tự kiểm nằm ngay trong đoạn trước. | Đã sửa: hai bài tự kiểm dùng dữ kiện mới (cặp tên MMDS §3.8.1; câu “The report said…”) kèm lời giải. |
| nhẹ | ghi chú “Đối sánh thực thể” | Một ý nói ba lần. | Đã gộp. |
| nhẹ | storyboard s05-02, s05-03 | Số thập phân dấu chấm. | Đã sửa. |

Phát hiện ngoài phạm vi về ghi chú s06-01 đã được xử lý trong commit s06-01. Kiểm hiển thị lại s05-01, 03, 04, 05 ở 1600×900 và 390×844; ghi chú bài giảng ở 1440, 390 và in.
| lec06-s06-03 | Kiểm tra tổng hợp MT1–MT3 bằng dữ kiện mới. | sửa | Tiêu đề “Tự kiểm tra thuật toán và mô hình” → “Câu hỏi tổng hợp về phân dải”. Ba câu cũ có đáp án trên mặt trang trước (vết chạy $Q=4$, $K=3$ ở s02-08; công thức bỏ sót ở s02-11/12; họ $(0{,}3;0{,}6;0{,}7;0{,}4)$ ở s03-08) và dùng số thập phân dấu chấm. Thay bằng: SIG $(2,1,2,0)$/$(1,1,1,1)$ cho $Q=7$, $K=6$, cặp $(1,3)$ phát lặp; $b=10$, $r=4$ cho ngưỡng $0{,}562$, $P(0{,}8)=0{,}9949$, $P(0{,}3)=0{,}0781$; họ MinHash $(0{,}2;0{,}5;0{,}8;0{,}5)$ và sau AND 2 $(0{,}2;0{,}5;0{,}64;0{,}25)$ (đã tính lại bằng chương trình). | Ghi chú bài giảng mục “Tổng hợp và tự kiểm”: sáu câu và lời giải thay bằng sáu câu mới của s06-03/04; bỏ “$(.3,.6,.7,.4)$”. |
| lec06-s06-04 | Kiểm tra tổng hợp MT4–MT6 bằng dữ kiện mới. | sửa | Tiêu đề “Tự kiểm tra phép ghép và ứng dụng” → “Câu hỏi tổng hợp về họ băm và ứng dụng”. Ba câu cũ có đáp án trên s03-11, s04-05 và ghi chú s06-01. Thay bằng: họ siêu phẳng $\pi/6$/$\pi/2$ với AND 2 rồi OR 2 ($0{,}9066$; $0{,}4375$); chọn họ và chi phí cho kho ảnh 128 chiều; ảnh hưởng của tăng $b$ tới bỏ sót và $K$. | Như trên. |
| lec06-s07-01 | Bài 3.4.1: bảng $P(s)$ cho ba cấu hình $(r,b)$, $s=0{,}1;\ldots;0{,}9$. | sửa | Tiêu đề “Bảng xác suất tạo ứng viên” → “Bảng giá trị đường cong S” (khớp thuật ngữ của nguồn và s02-12). Bảng giữ chỗ “9 giá trị” thay bằng bảng ba cấu hình $r$, $b$; dữ kiện và yêu cầu giữ nguyên Bài 3.4.1. Số thập phân dấu phẩy, danh sách phân tách bằng dấu chấm phẩy. Ghi chú bỏ dòng thời lượng (quy định cấm thời lượng trong ghi chú), làm tròn đáp án sáu chữ số (đã tính lại bằng chương trình). | Ghi chú bài giảng mục “Xác suất phân dải — Bài 3.4.1–2”: toàn bộ số thập phân chuyển sang dấu phẩy. |
| lec06-s07-02 | Bài 3.4.2: nghiệm $P(s)=1/2$ so với $(1/b)^{1/r}$. | sửa | Tiêu đề “Điểm xác suất một nửa” → “Ngưỡng của đường cong S”. Xấp xỉ viết $(1/b)^{1/r}$ như nguồn và s02-12; tiêu đề cột bằng KaTeX; ô “…” thay bằng ô trống. Ghi chú bỏ thời lượng, số dấu phẩy, thêm ý nghĩa chiều sai lệch (xấp xỉ ước lượng ngưỡng hơi cao). | Như trên. |
| lec06-s07-03 | Bài 3.6.1(a–d): bốn biểu thức xác suất qua nhiều tầng ghép. | sửa | Tiêu đề “Xác suất sau nhiều phép ghép” → “Xác suất qua nhiều tầng ghép”. $p$ viết bằng KaTeX; câu dẫn nêu rõ xuất phát từ họ MinHash như nguồn. Ghi chú bỏ thời lượng, thêm quy tắc biến đổi theo tầng. Dữ kiện và yêu cầu giữ nguyên. | Ghi chú bài giảng mục Bài 3.6.1 không có số thập phân; không đổi. |
| lec06-s07-04 | Bài 3.7.1: hàm chọn tọa độ nhận từng cặp của bốn vector. | sửa | Tiêu đề “Các hàm tọa độ tạo ứng viên” → “Hàm chọn tọa độ trên bốn vector” (khớp tên họ ở s04-01). Ghi chú bỏ thời lượng; đáp án viết tập chỉ số bằng KaTeX; thêm quan hệ số hàm $=6-d_H$ và ghi tên gốc dạng chuỗi bit. Đáp án đã kiểm lại từng vị trí. Dữ kiện giữ nguyên. | Ghi chú bài giảng Bài 3.7.1 không có số thập phân; không đổi. |
| lec06-s07-05 | Bài 3.7.2: chữ ký dấu của ba vector và góc ước lượng/góc thật. | sửa nhẹ | Giữ tiêu đề và mặt trang. Ghi chú bỏ thời lượng; danh sách góc phân tách bằng dấu chấm phẩy; góc thật $74{,}97^\circ$; $105{,}03^\circ$ (đã tính lại: $\cos\theta=\pm14/54$). | Ghi chú bài giảng Bài 3.7.2: số thập phân dấu phẩy. |
| lec06-s07-06 | Bài 3.7.5(a–c): thùng chiếu trên ba trục. | sửa nhẹ | Ghi chú bỏ thời lượng. Tên điểm đã đổi $z_1,z_2,z_3$ ở commit s04-06. | Không đổi thêm. |
| lec06-s07-07 | Bài 3.8.2(a,b): OR 2048 so với AND hai nhóm OR 1024. | sửa | Tiêu đề “So sánh hai phép ghép vân tay” → “So sánh hai cấu trúc ghép cho vân tay”. Số thập phân dấu phẩy trên mặt trang; “ứng viên giả và bỏ sót” viết theo thuật ngữ s05-04 (“nhận cặp khác ngón”, “bỏ sót cặp cùng ngón”). Ghi chú bỏ thời lượng, số dấu phẩy, thêm nhận xét định lượng cùng ngân sách (khoảng 30 lần; $12\%$ so với $3\%$, đã tính lại). Dữ kiện và yêu cầu giữ nguyên. | Ghi chú bài giảng Bài 3.8.2: số thập phân dấu phẩy, thống nhất thuật ngữ. |

### Rà lại phần 6–7 và mạch toàn deck

Tác tử rà chỉ đọc: vai trò chính xác toán–thuật toán (phần 6–7) và mạch lập luận toàn deck (60 trang theo thứ tự trình chiếu); kiểu `fork` của công cụ Agent, mô hình Claude Opus 5.5, effort `high`. Tác tử tính lại mọi đáp án của s06-03/04 và sáu cụm bài tập (27 giá trị Bài 3.4.1, ba ngưỡng Bài 3.4.2, bốn biểu thức Bài 3.6.1, sáu tập chỉ số Bài 3.7.1, chữ ký và góc Bài 3.7.2, mã thùng Bài 3.7.5, xác suất Bài 3.8.2) và đối chiếu thêm s02-12; tất cả đúng. Dữ kiện bài tập giữ nguyên; không còn thời lượng hay mã trang trong ghi chú diễn giả; không còn số thập phân dấu chấm trên deck và ghi chú; tiêu đề phiếu khớp h2 cả 60 trang. Các ranh giới phần 1→2, 2→3, 3→4, 4→5, 5→6 được đánh giá liên kết đủ.

| Mức độ | Trang chiếu | Vấn đề | Quyết định |
|---|---|---|---|
| trung bình | s01-02 | Mục tiêu không nói tới AND/OR và ba ứng dụng, nên không đối chiếu được với câu hỏi tổng hợp. | Đã sửa: mục 2 thêm “cách ghép AND/OR”, mục 3 thêm “áp dụng cho thực thể, vân tay, bản tin”; ghi chú nêu ánh xạ. |
| trung bình | s02-12 ↔ s07-01/02 | $(20,5)$ nghĩa $(b,r)$ ngược với $(r,b)$ của bài tập. | Đã sửa: s02-12 ghi “$b=20$, $r=5$”, “$b=r=10$” trên mặt trang và ghi chú. Bảng ghi chú bài giảng có tiêu đề cột $(b,r)$ nên giữ. |
| nhẹ | s07-01 (ghi chú) | $(3;10)$ khác $(6,20)$. | Đã sửa thành $(3,10)$. |
| nhẹ | s07-06, s07-07 (ghi chú) | Dòng nguồn lặp. | Đã bỏ câu nguồn trong đoạn đầu. |
| nhẹ | s05-02 (ghi chú) | Câu điều hướng “ở trang sau”. | Đã sửa: “khác mô hình $q_T$, $q_F$”. |
| nhẹ | s06-04 (ghi chú) | Hằng số trong ký hiệu $O$. | Đã sửa: $O(CmD)$ với $D=128$. |
| nhẹ | ghi chú Bài 3.4.1–2, mục ngưỡng | $b^{-1/r}$ khác $(1/b)^{1/r}$ của deck. | Đã thống nhất $(1/b)^{1/r}$ trong toàn bộ ghi chú. |
| nhẹ | ghi chú “Tổng hợp và tự kiểm” | $P(s)$ thiếu chỉ số. | Đã sửa thành $P_{b,r}(s)$. |
| nhẹ | ghi chú, gợi ý Bài 3.7.5 | $x_i$ không khớp tên điểm $z_j$. | Đã sửa bằng câu văn. |
| nhẹ | s07-05 | “Sản phẩm” nằm trong `ex-note`. | Đã tách: quy ước dấu ở `ex-note`, sản phẩm ở `ex-takeaway`. |
| nhẹ | storyboard s06-01 | Trường Dữ kiện mô tả bản cũ. | Đã sửa. |
| nhẹ | s03-05 | Khoảng cách chỉnh sửa không có họ LSH, khái niệm treo. | Đã sửa: ghi chú nêu MMDS chương 3 không xây họ riêng cho độ đo này và vai trò của nó trong bài (so với Hamming, minh họa tiên đề). |
| nhẹ | s06-02 ↔ s01-03 | Kết bài chưa khép con số $C=10^6$. | Đã sửa: ghi chú s06-02 nêu $K\approx5\cdot10^{11}$ trong trường hợp xấu nhất. |
| nhẹ | s06-04 → s07-01 | Phần bài tập vào thẳng câu hỏi. | Giữ: phần 7 là phần thực hành tách riêng, có nhãn phần và tiêu đề bài nguồn trên từng trang. |
| nhẹ | storyboard phần 2–3 | Số thập phân dấu chấm trong phiếu. | Giữ: tài liệu lập kế hoạch nội bộ, sinh viên không thấy; ghi nhận là giới hạn. |

Thêm: bốn câu hỏi tự kiểm trong ghi chú bài giảng dạng “…không?”/“Vì sao…?” viết lại dạng yêu cầu (“Giải thích…”, “Xác định…”, “nêu…”).

### Kiểm định cuối lượt duyệt từng trang, 02/10/2026

| Hạng mục | Kết quả |
|---|---|
| Cấu trúc | 60 trang (53 giảng, 7 bài tập), bảy phần 5/14/13/11/6/4/7; mục lục s01-02 khớp; 60 `data-slide-id` duy nhất, 60 ghi chú; không `fragment`, không `<style>`, không style nội dòng; không mã trang hay thời lượng trong ghi chú diễn giả. Một khối mã có `data-trim` và `language-plaintext`. Không ảnh raster. Điều hướng phím (Space) đi qua đủ 60 trang theo thứ tự. |
| Hiển thị deck | Playwright Chromium, 1600 × 900 và 390 × 844, đủ 60 trang (120 ảnh): không lỗi KaTeX, console hay trang; không tải tài nguyên ngoài máy cục bộ; không cuộn ngang; cỡ chữ nhỏ nhất 18 px; không tràn khung ở 1600 × 900. Điều phối viên xem ảnh nguyên cỡ của mọi trang đã sửa. Ảnh lưu ngoài kho. |
| Khổ hẹp | Như Bài 03–05: ở chiều rộng ≤ 435 px Reveal chuyển sang chế độ cuộn; kiểm bằng cuộn tới từng trang, 60/60 trang nằm trọn trong khung, nội dung thu nhỏ theo khung 16:9 (giới hạn runtime dùng chung, không sửa). |
| Ghi chú tự học | Viewer 1440 × 900, 390 × 844 và chế độ in: 705 công thức KaTeX, không lỗi, không cuộn ngang, không lỗi console (bỏ qua thông báo CSP do máy chủ reload chèn script). Mọi mục cập nhật theo deck; thêm mục “Chi phí tính chữ ký của ba họ”. Không còn số thập phân dấu chấm, không còn câu hỏi tự kiểm dạng câu hỏi. |
| Đồng bộ planning | 60/60 tiêu đề phiếu storyboard khớp HTML; thứ tự phiếu khớp thứ tự deck (s02-06 sau s02-01, s04-05 trước s04-04); outline thêm mục tóm tắt lượt duyệt và cập nhật V11. |
| Rà lại | Năm lượt rà chỉ đọc có báo cáo (phần 1–2, phần 3, phần 4, phần 5, phần 6–7 kèm mạch toàn deck); một lần chạy đầu của lượt phần 3 dừng không báo cáo và một lần chạy lại bị dừng vì trùng việc (đã ghi ở mục phần 3). Không có phát hiện chặn bàn giao; hai phát hiện nghiêm trọng (s03-07 điều kiện chỉ trong hình; mã trang trong ghi chú s04-07) đã sửa; mọi phát hiện trung bình đã xử lý; hai phát hiện nhẹ giữ có lý do. Phép tính kiểm lại bằng chương trình. |
| no-ai-slop | Mỗi trang sửa được tự kiểm theo `eval.md` (Edit mode); các lượt rà dùng Detect mode. |
| Phạm vi tệp | HTML Bài 06, `lecture-note.md`, ba tệp planning, bốn SVG (`mien-gan-xa.svg`, `ghep-and-or.svg`, `chia-khoang-dich.svg`, `goc-tach-sieu-phang.svg`) và `generate_svg.py` cho nhãn hình. CSS, index và viewer không đổi. Thay đổi sẵn có của người dùng (`.gitignore`, `AGENTS.md`, `slide_authoring_standard.md`, các tệp chưa theo dõi) không được stage. |
| Giới hạn | Điều phối viên trực tiếp biên tập theo tiền lệ Bài 04–05, bù bằng các lượt rà độc lập theo phần; không chạy lại đủ năm vai rà độc lập cho toàn deck. Cổng 8765 bị máy chủ của dự án khác chiếm nên kiểm trên cổng 8775. Nhãn trục của `xac-suat-phan-dai.svg` vẫn dùng dấu chấm thập phân (ngoại lệ đã ghi ở phần 2). Phiếu storyboard phần 2–3 còn số thập phân dấu chấm trong một số trường nội bộ. Các commit s07-01…03 và s07-04…07 gộp theo cụm vì cùng loại sửa. |

#### Phiếu kiểm tra trước khi duyệt (`slide_authoring_standard.md`)

| Mục | Kết quả |
|---|---|
| Tiêu đề ngắn, gọi đúng khái niệm/kết quả | Đạt: 43/59 tiêu đề `h2` đổi; không câu hỏi, không câu kể tiến trình. |
| Văn phong học thuật, no-ai-slop | Đạt: Edit mode khi sửa, Detect mode ở năm lượt rà. |
| Không văn nói, chỉ dẫn biên soạn | Đạt: đã gỡ câu điều hướng “ở trang sau”, mã trang và thời lượng trong ghi chú. |
| Mỗi slide một mục đích, vai trò ghi ở storyboard | Đạt: 60 phiếu có “Mục đích và vai trò”, cập nhật cho mọi trang đã sửa. |
| Mỗi phần mở nhu cầu, nối kết quả | Đạt: lượt rà mạch đánh giá đủ ở mọi ranh giới phần. |
| Phần kết thu hồi tình huống, có tự kiểm | Đạt: s06-01 nối ba bước với các phần; s06-02 khép $C=10^6$; s06-03/04 dữ kiện mới. Thời lượng giảng và bài tập tính riêng trong storyboard. |
| Một trọng tâm mỗi slide | Đạt: không trang nào tràn; nội dung phụ chuyển vào ghi chú. |
| Tiên quyết và ký hiệu đặt trước nơi dùng | Đạt: đổi thứ tự s04-04/05; định nghĩa ứng viên giả, $p_{\ne}$, điểm đặc trưng, từ dừng trước khi dùng. |
| Thuật toán đủ đặc tả, đúng, dừng, chi phí | Đạt: phân dải (s02-07…13) giữ đặc tả, giả mã, tính đúng, chi phí. |
| Ví dụ tính lại được | Đạt: mọi số trên các trang đã sửa được tính lại bằng chương trình. |
| Mô hình chi phí trước phép tính | Đạt: s02-13, s04-10 nêu mô hình trước bảng. |
| Số hạng chi phí truy về bước | Đạt: s04-10 đếm phép tính của một hàm trước tiệm cận. |
| Cùng dữ kiện, chỉ số, thuật ngữ | Đạt: thống nhất $z_i$, “độ chênh”, “nhận cặp khác ngón”, $(1/b)^{1/r}$, $P_{b,r}(s)$. |
| Câu hỏi đo đúng mục tiêu, có đáp án | Đạt: mục tiêu s01-02 cập nhật; đáp án và tiêu chí trong ghi chú. |
| Render đọc được, liên kết hoạt động | Đạt: xem hàng “Hiển thị deck”. |
| Khối mã `data-trim`, công thức render, không `fragment` | Đạt. |
| Sai khác nguồn có lý do | Đạt: đổi tên điểm Bài 3.7.5, chỉnh “một phần 200” thành $1/244{,}14$, giá trị $0{,}004024$ thay $0{,}00397$ đều ghi trong nhật ký. |

## Căn chỉnh văn phong 2026-10-14

### Lý do, căn cứ và phạm vi giai đoạn 1

- **Lý do.** Yêu cầu người dùng ngày 2026-10-14: đưa Bài 06 về chuẩn mới của `AGENTS.md` (bản đang sửa, chưa commit), gồm "Tiêu chuẩn giáo trình cho ghi chú bài giảng" (ghi chú là một chương tự chứa có số hiệu, giọng kể "chúng ta/ta", mẫu tám bước, tình huống áp dụng), "Trang tiêu đề mạch" và "Văn phong và mật độ mặt trang chiếu", cùng `slide_authoring_standard.md`. Mẫu tham chiếu: ghi chú Bài 05 của `../rl-plan` (cấu trúc và giọng, không lấy nội dung).
- **Kế hoạch.** `/tmp/claude-1000/-data-tqlong-ds-foundation-algorithms/120f1262-3ea0-45af-8c12-2dcf2a1526d1/scratchpad/plan-lec06.md` (tác tử lập kế hoạch chỉ đọc, lập ngày 2026-10-14), được điều phối viên duyệt. Giai đoạn 1 thực hiện mục E (ghi chú), phần F1 liên quan mục 5 của outline và phần F2 liên quan kiến trúc ghi chú của storyboard.
- **Phân công.** Tác tử soạn giai đoạn 1, vai trò writer, là tác tử duy nhất được ghi tệp trong lượt này, theo giao việc của điều phối viên. Loại tác tử, mô hình và effort được điều phối viên ghi theo bằng chứng tool call; mục này không dùng lời tự khai làm bằng chứng.
- **Tệp đã sửa.** `materials/lec-06/lecture-note.md` (viết lại toàn bộ); `planning/lec-06/outline.md` (thuật ngữ Việt–Anh, bảng `note-topic-id` ↔ mục ghi chú, mục 5 thành bảng mạch mới); `planning/lec-06/storyboard.md` (chỉ phần "Kiến trúc ghi chú bài giảng tự học"); tệp này. Không sửa deck HTML, SVG, CSS, viewer, index. Không commit.

### Quyết định của điều phối viên cho các điểm mở (G5 của kế hoạch)

1. Tên mạch 1 giữ "Bài toán tìm cặp tương đồng"; ghi chú `## 1. Bài toán tìm cặp tương đồng`.
2. Thu hồi kho một triệu tài liệu bằng $\binom{10^6}{2}=499\,999\,500\,000$ và câu "nếu bộ tạo ứng viên trả $10^6$ cặp (giả định luyện tập) thì số phép xác minh giảm khoảng $5\cdot10^5$ lần"; ghi rõ là giả định, không ghép $n=250$ với $(b,r)=(20,5)$. Đã thực hiện ở đoạn mở của "Tóm tắt chương".
3. (deck) Giữ số bài sách trên trang recitation.
4. Hình cấu trúc chương ở Mục 1 dùng lại `img/lec-06/quy-trinh-cap.svg` kèm đoạn đọc hình nối tới Mục 2–5. Đã thực hiện; không tạo hình mới.
5. Đánh số `## 1.`–`## 5.`; "Tình huống áp dụng và ứng dụng", "Tóm tắt chương", "Bài tập củng cố", "Hướng dẫn đọc thêm và tài liệu tham khảo" không đánh số. Đã thực hiện.
6. Giữ cả bốn tình huống, kể cả Tình huống 06.4 (pháp tuyến $\pm1$ cố định), chỉ dùng số đã có. Đã thực hiện.
7. (deck) Nhãn "Quy tắc:" thay bằng "Thuật toán.".
8. Rà đủ năm vai sau khi deck xong; ghi chú được rà toán và rà mạch viết ngay sau giai đoạn này.

### Cấu trúc ghi chú mới và số hiệu cuối cùng

Thứ tự: tiêu đề, một đoạn giới thiệu, dòng liên kết deck, Mục tiêu học tập (5), Kiến thức tiên quyết (`lec-06-topic-18`), Bảng ký hiệu (23 dòng), Bản đồ chủ đề (19 chủ đề), `## 1.`–`## 5.`, Tình huống áp dụng và ứng dụng (`-19`), Tóm tắt chương (`-14`), Bài tập củng cố (`-16`, ba tiểu mục mức), Hướng dẫn đọc thêm và tài liệu tham khảo (`-15`). Ánh xạ N01–N16 sang `lec-06-topic-k` nằm ở outline mục 4 và storyboard phần kiến trúc ghi chú. Bỏ 18 dòng "Nguồn:" cuối mục, nhãn "Câu hỏi:" đầu khối bài tập, mục "Tổng hợp và tự kiểm" và "Đọc thêm có giới hạn" (tách ba nơi), bốn liên kết neo cũ tới bài sách.

**Bộ đếm chung (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán).**

- Mục 1: Định nghĩa 06.1 (Bài toán tìm cặp tương đồng); Nhận xét 06.2 (Hai đại lượng $s$ và $\widehat s$).
- Mục 2: Định nghĩa 06.3 (Dải, khóa dải và tập ứng viên); Thuật toán 06.4 (Phân dải và xác minh); Mệnh đề 06.5 (Tính đúng của phân dải và xác minh); Nhận xét 06.6 (Trường hợp biên và bước lọc theo $\widehat s$); Định lý 06.7 (Xác suất thành ứng viên); Hệ quả 06.8 (Xác suất bỏ sót); Mệnh đề 06.9 (Nghiệm một nửa); Nhận xét 06.10 (Ba đại lượng ngưỡng và quy tắc chọn $b$, $r$); Mệnh đề 06.11 (Chi phí của Thuật toán 06.4); Nhận xét 06.12 (Trường hợp xấu nhất); Mệnh đề 06.13 (Kỳ vọng của $K$ và $Q$).
- Mục 3: Định nghĩa 06.14 (Độ đo khoảng cách; chuẩn $L_q$); Mệnh đề 06.15 (Khoảng cách Jaccard); Định nghĩa 06.16 (Khoảng cách góc); Nhận xét 06.17 (Góc và cosin); Định nghĩa 06.18 (Khoảng cách chỉnh sửa; dãy con chung dài nhất); Mệnh đề 06.19 (Khoảng cách chỉnh sửa qua dãy con chung); Định nghĩa 06.20 (Khoảng cách Hamming); Nhận xét 06.21 (Hamming là độ đo; chi phí tính độ đo); Định nghĩa 06.22 (Họ nhạy cảm theo tính cục bộ); Hệ quả 06.23 (Họ MinHash); Định nghĩa 06.24 (Phép ghép AND và OR); Mệnh đề 06.25 (Xác suất sau phép ghép); Nhận xét 06.26 (Phân dải là AND rồi OR).
- Mục 4: Định nghĩa 06.27 (Họ chọn tọa độ); Mệnh đề 06.28 (Xác suất trùng của họ chọn tọa độ); Nhận xét 06.29 (Ghép nhiều hàm chọn tọa độ); Định nghĩa 06.30 (Hàm băm dấu và họ siêu phẳng); Định lý 06.31 (Xác suất cùng dấu); Thuật toán 06.32 (Chữ ký dấu và ước lượng góc); Định nghĩa 06.33 (Họ chiếu có dịch trong mặt phẳng); Bổ đề 06.34 (Xác suất chung thùng khi cố định hướng); Định lý 06.35 (Họ chiếu có dịch trong hai chiều); Nhận xét 06.36 (Trục cố định, số chiều và chi phí); Mệnh đề 06.37 (Chi phí tính chữ ký của ba họ).
- Mục 5: Định nghĩa 06.38 (Hàm khóa và quy tắc ứng viên theo trường); Nhận xét 06.39 (Hàm khóa cố định không cho cận xác suất); Định nghĩa 06.40 (Hàm ba ô cho vân tay); Mệnh đề 06.41 (Xác suất va chạm của hàm ba ô); Định nghĩa 06.42 (Từ dừng và shingle theo từ dừng).

Số hiệu khớp danh sách tạm tính E2 của kế hoạch ở mọi vị trí.

**Ví dụ.** 06.1 Kho một triệu tài liệu (Ví dụ 3.10); 06.2 Năm cột, dải ba hàng (Ví dụ 3.11, Hình 3.7); 06.3 Bốn tập đặc trưng (Ví dụ 3.8, $b=2$, $r=1$, $t=2/3$); 06.4 Cặp $s=0{,}8$ qua 20 dải năm hàng (Ví dụ 3.12); 06.5 Hai cấu hình cùng 100 hàng; 06.6 Công việc trên bốn tập đặc trưng; 06.7 Ba độ đo trên hai điểm (Ví dụ 3.13); 06.8 Góc giữa hai vector (Ví dụ 3.14); 06.9 Sửa abcde thành acfdeg (Ví dụ 3.15–3.16); 06.10 Hai vector bit (Ví dụ 3.17); 06.11 Họ MinHash với hai ngưỡng $0{,}3$ và $0{,}6$ (Ví dụ 3.18); 06.12 Hai thứ tự ghép trên 16 phép thử (Ví dụ 3.19–3.20); 06.13 Hai vector bit theo từng chỉ số; 06.14 Dấu theo hai pháp tuyến (Ví dụ 3.22); 06.15 Chữ ký dấu với ba pháp tuyến cố định (Ví dụ 3.22); 06.16 Ba điểm trên trục thứ nhất (Bài 3.7.5); 06.17 Hai cấu trúc ghép cho vân tay (Ví dụ 3.23); 06.18 Shingle theo từ dừng trên hai câu (Ví dụ 3.24).

**Tình huống.** 06.1 Đối sánh hồ sơ hai nguồn và kiểm bằng trường ngày (giả thiết không thỏa: hàm khóa cố định); 06.2 Truy vấn vân tay một–nhiều; 06.3 Bản tin gần trùng; 06.4 Ước lượng góc bằng pháp tuyến có tọa độ $\pm1$ (giả thiết đẳng hướng không thỏa).

**Bài tập.** Trong các mục: 06.1 (Mục 1), 06.2 (2.2), 06.3 (2.4), 06.4 (2.5), 06.5 (3.5), 06.6 (3.6), 06.7 (3.7), 06.8 (4.1), 06.9 (4.2), 06.10 (4.3), 06.11 (4.4), 06.12 (5.1), 06.13 (5.2), 06.14 (5.3). Bài tập củng cố: mức nhận biết 06.15 (họ MinHash $d_1=0{,}2$, $d_2=0{,}5$, AND 2), 06.16 (giữ $r$, tăng $b$); mức tính toán hoặc chứng minh 06.17 ($Q$, $K$ trên SIG hai hàng), 06.18 ($b=10$, $r=4$), 06.19 (họ siêu phẳng, AND 2 rồi OR 2), 06.20 (Bài 3.4.1), 06.21 (Bài 3.4.2), 06.22 (Bài 3.6.1(a–d)), 06.23 (Bài 3.7.1), 06.24 (Bài 3.7.2), 06.25 (Bài 3.7.5(a–c)), 06.26 (Bài 3.7.5(d)); mức vận dụng 06.27 (kho ảnh 128 chiều), 06.28 (Bài 3.8.2(a,b)). Số hiệu bài tập khác danh sách tạm tính E2 vì bộ đếm theo thứ tự xuất hiện; các trang recitation s07-01…s07-07 ứng với Bài tập 06.20, 06.21, 06.22, 06.23, 06.24, 06.25, 06.28. Sáu nhiệm vụ tự kiểm cũ là Bài tập 06.15–06.19 và 06.27; các câu hỏi trên trang s02-14, s03-13, s04-11, s05-06 (đã có lời giải kiểm bằng chương trình trong ghi chú diễn giả) được dùng làm dữ kiện cho Bài tập 06.3(b,c), 06.5(c,d), 06.8, 06.9, 06.10(a,c), 06.13.

**Mục tiêu ↔ bài tập.** Mục tiêu 1: 06.2, 06.4, 06.17; mục tiêu 2: 06.3, 06.16, 06.18, 06.20, 06.21; mục tiêu 3: 06.6, 06.7, 06.15, 06.19, 06.22; mục tiêu 4: 06.8–06.11, 06.23–06.26; mục tiêu 5: 06.12–06.14, 06.27, 06.28.

### Giáo trình và mục đã tham khảo cho từng mục chương

| Mục ghi chú | Nguồn và mục đã đối chiếu trong lượt này | Điều lấy làm cách diễn giải |
|---|---|---|
| Kiến thức tiên quyết | Ghi chú Bài 05 của học phần, danh sách mục 1–14 (đọc tiêu đề và Mục 11) | Dẫn theo mục vì Bài 05 chưa đánh số; nhắc lại "hai tầng va chạm", "hoán vị affine" |
| 1 | MMDS §3.4, Ví dụ 3.10, tr.91–92 (qua ghi chú cũ đã rà và bảng V01 của outline) | Mở bằng số cặp còn lại sau chữ ký; tách bộ nhớ khỏi số cặp |
| 2.1–2.2 | MMDS §3.4.1 và §3.4.3 (đọc lại văn bản bảy bước, bước 4, 6, 7, tr.95–96); Ví dụ 3.11/Hình 3.7; Cormen và cộng sự (2022) §2.1 cho khuôn bất biến khởi tạo–duy trì–kết thúc (dẫn theo khuôn chuẩn của sách, không mở bản sách trong lượt này) | Ví dụ Hình 3.7 trước định nghĩa; bất biến chia bước; bước lọc theo $\widehat s$ của sách được nêu và bỏ có lý do |
| 2.3–2.4 | MMDS §3.4.2–3.4.3, Ví dụ 3.12 ("khoảng 1 trên 3000"), Bài 3.4.2 | Chuỗi một dải → không dải → bù; quy tắc chọn $(1/b)^{1/r}$ thấp hơn hoặc cao hơn $t$ theo bước 4 của sách |
| 2.5 | Suy từ thủ tục §3.4 (chủ đề bổ sung đã duyệt); khuôn bảng đếm của học phần | Bảng Bước–Số lần–Chi phí mỗi lần–Đóng góp |
| 3.1–3.5 | MMDS §3.5, Ví dụ 3.13–3.17 (qua ghi chú cũ và bảng V05–V08) | Giữ thứ tự chuẩn, Jaccard, góc, chỉnh sửa, Hamming; ví dụ đặt trước định nghĩa |
| 3.6–3.7 | MMDS §3.6.1–3.6.3, Ví dụ 3.18–3.20; Stanford CS246 LSH II (qua outline mục 3) | Hai bảo đảm và miền giữa; hai thứ tự ghép cùng 16 hàm |
| 4.1 | MMDS §3.7.1 (đọc lại văn bản trong lượt này) | Họ $\{f_1,\ldots,f_d\}$ và bộ $(d_1,d_2,1-d_1/d,1-d_2/d)$; khác MinHash ở số hàm hữu hạn |
| 4.2 | MMDS §3.7.2–3.7.3 (đọc lại §3.7.3 về vector $\pm1$ và quy ước số 0), Ví dụ 3.22 | Sách coi vector $\pm1$ "đủ ngẫu nhiên"; ghi chú nêu đây là vi phạm giả thiết đẳng hướng (Tình huống 06.4), đúng như ghi chú cũ đã rà |
| 4.3 | MMDS §3.7.4–3.7.5; Datar và cộng sự (2004) §3.2 (qua outline mục 2–3) | Dịch đều là chủ đề bổ sung; cận chỉ hai chiều |
| 4.4 | Đếm từ định nghĩa hàm (chủ đề bổ sung ngày 02/10) | Bảng đếm phép tính |
| 5.1, Tình huống 06.1 | MMDS §3.8.1–3.8.3 (đọc lại văn bản §3.8.2–3.8.3 trong lượt này: 100 điểm mỗi trường, tổng 300, ba lần sắp xếp, trễ 0–90 ngày, trung bình 45 và 10, $f=(45-x)/35$) | Giữ đúng số của sách; nêu hàm khóa cố định là giả thiết không thỏa |
| 5.2, Tình huống 06.2 | MMDS §3.8.4–3.8.5, Ví dụ 3.23 (đọc lại định nghĩa điểm đặc trưng, lưới khoảng 1000 ô, thùng chung và thùng đơn) | Mô hình $0{,}2$, $0{,}8$ là giả định; truy vấn một–nhiều |
| 5.3, Tình huống 06.3 | MMDS §3.8.6, Ví dụ 3.24 (đọc lại các giá trị 75%, 25%, 1/3 và năm shingle) | Đổi biểu diễn, giữ MinHash và phân dải |
| Giọng kể, "Trong thực hành", tình huống | Ghi chú Bài 05 của `../rl-plan` (mẫu đã áp chuẩn từ giáo trình *Học máy thống kê*); không mở `../SML-textbook-main.zip` trong lượt này | Giọng "chúng ta/ta", đoạn kết mục văn xuôi, danh sách "Bỏ <giả thiết>", khối tình huống có "Dẫn ngược lý thuyết" |

Không có đoạn dịch hoặc chép từ giáo trình; các số của sách được dẫn kèm số ví dụ, mục và trang.

### Lập luận mới cần tác tử rà toán kiểm

Các đoạn sau là lập luận mới so với ghi chú đã rà ngày 02/10; mọi số khác giữ nguyên giá trị đã kiểm.

- Mệnh đề 06.5, ba phản ví dụ: hai khóa $(1,(1))$, $(1,(3))$ chung ô làm phát cặp $(1,2)$ và $\mathrm{CAND}\ne\mathcal C$, với $t=0$ cặp vào đầu ra; khóa không chứa số dải với hai cột $(1,2)$, $(2,1)$; tập rỗng cho $0/0$.
- Định lý 06.7, năm phản ví dụ: thứ tự cố định đặt $a$ đầu cho xác suất $1$ với $S_1$, $S_4$; cùng hoán vị trong dải cho $s$ ($0{,}8$ thay $0{,}32768$); cùng $r$ hoán vị cho mọi dải cho $s^r$ ($0{,}32768$ thay $0{,}999643942$); va chạm ô làm (2.1) thành $\ge$ với cặp $(1,2)$, $s=0$; hai tập rỗng có cột toàn $+\infty$.
- Định lý 06.7, "Trong thực hành": số cặp bỏ sót kỳ vọng bằng $\sum(1-s_{cd}^r)^b$ trên các cặp đạt ngưỡng (tuyến tính kỳ vọng).
- Mệnh đề 06.9: chứng minh tồn tại và duy nhất nghiệm bằng tính tăng chặt và liên tục.
- Mệnh đề 06.11: hai hàng $O(bC)$ thêm vào bảng đếm (tạo danh sách, duyệt danh sách).
- Mệnh đề 06.13, "Trong thực hành": phát biểu định tính về nhóm bản sao làm $Q$ tăng theo bình phương cỡ nhóm.
- Định nghĩa 06.14: phản ví dụ $q=1/2$ với $(0,0)$, $(1,0)$, $(1,1)$ cho $4>1+1$.
- Mệnh đề 06.25, hai phản ví dụ: dùng lại một hàm bốn lần cho $0{,}8$ thay $0{,}4096$ và thay $0{,}9984$; băm hai đối tượng bằng hai hàm khác nhau.
- Mệnh đề 06.28, hai phản ví dụ: $I\equiv1$ cho xác suất $1$ thay $2/5$; chỉ số riêng cho $x=y=10101$ với cặp chỉ số $(1,2)$.
- Định lý 06.31: chứng minh Bước 1–3 viết lại chi tiết hơn ($y=\pm\lambda x$; phân tích $v=v_\Pi+v_\perp$); bốn phản ví dụ: 16 vector $\pm1$ cho $4/16$ khác dấu, ứng với $45^\circ$ (đã có trong ghi chú cũ, nay thành phản ví dụ); $\theta=60$ độ cho số âm; $x=0$; hai pháp tuyến độc lập cho $x=y$ trùng với xác suất $1/2$.
- Thuật toán 06.32: $\mathbb E[\widehat p_{\ne}]=\theta/\pi$ theo tuyến tính kỳ vọng.
- Bổ đề 06.34: phản ví dụ $\delta=0$, hình chiếu $1\pm\varepsilon$ với $a=1$.
- Định lý 06.35: chứng minh cận gần dùng Cauchy–Schwarz $\ell\le\rho$; hai phản ví dụ: $\delta=0$ với hai điểm $(\pm\varepsilon,0)$, $0<\varepsilon\le a/4$, xác suất $0$; $u$ luôn vuông góc với $x-y$ cho xác suất $1$. Giới hạn hai chiều được nêu là chưa có phản ví dụ trong chương, không khẳng định cận thay thế.
- Mệnh đề 06.37: ví dụ đếm $2\cdot3\cdot4=24$ phép nhân cho Ví dụ 06.15. Bài tập 06.11 thêm dòng kiểm $2\cdot10^8$ bit $=2{,}5\cdot10^7$ byte.
- Mệnh đề 06.41, hai phản ví dụ: ba ô luôn cùng có hoặc cùng không cho $0{,}04$; chọn ô theo ảnh truy vấn cho $0{,}8^3=0{,}512$.
- Tình huống 06.2: tỷ phần kỳ vọng ảnh khác ngón phải so bằng $P_F$ theo tuyến tính kỳ vọng. Tình huống 06.4: hàm $\pm1$ tốn khoảng $D-1$ phép cộng, trừ.
- Các dòng "Kiểm tra lại" mới: Ví dụ 06.5 ($0{,}8^{10}\approx0{,}107374$), Bài tập 06.13 ($0{,}1223^2\approx0{,}0150$), Bài tập 06.16 ($0{,}67232^{20}\approx0{,}000356$), Bài tập 06.18 ($0{,}562^4\approx0{,}0998$), Bài tập 06.19 ($(11/36)^2\approx0{,}0934$), Bài tập 06.20 (tại $s=0{,}1$, $r=3$, $b=10$), Bài tập 06.21 ($0{,}406088134^3\approx0{,}066967$), Bài tập 06.26 (các biên $3/2$, $2$, $3$).

Tác tử soạn đã tính lại bằng chương trình: $0{,}67232^{20}=0{,}000356058$, $(1-0{,}8^{10})^{10}=0{,}321140026$, $P_{20,5}(0{,}549280272)=0{,}641514078$, 16 vector $\pm1$ cho 4 vector khác dấu ($45^\circ$), $\arccos(40/\sqrt{2580})=38{,}047579^\circ$.

Không phát hiện mâu thuẫn số liệu giữa ghi chú cũ và bảng V01–V12, HT1–HT11 của outline.

### Kiểm tra đã chạy

- **Script kiểm cấu trúc** (`python3 -I` trong scratchpad của tác tử soạn): 27 451 từ theo cách đếm khoảng trắng, 25 740 từ khi bỏ công thức khối và mã; 164 khối `:::`, 164 dòng đóng, không lồng; bộ đếm chung 06.1–06.42, Ví dụ 06.1–06.18, Tình huống 06.1–06.4, Bài tập 06.1–06.28, đều liên tục và không trùng; mọi `proof` đi ngay sau kết quả, có tiêu đề cùng số hiệu và kết thúc bằng $\square$; mọi `exercise` có `hint` và `solution`; mọi định lý, mệnh đề, bổ đề, hệ quả có đủ bốn phần; 19 `note-topic-id` duy nhất, đúng dạng `lec-06-topic-NN`, mỗi mã ngay trước một tiêu đề; không còn "Mục này", "Tài liệu này", "xem trang chiếu", "dễ thấy", "Đáp án", "Câu hỏi:", dòng mở bằng "Nguồn:" hay "hãy"; 12 SVG được dùng; số lượng `$$` chẵn; không có số thập phân dấu chấm trong công thức; mọi tham chiếu "Định nghĩa/Định lý/…/Bài tập 06.k" trỏ đúng loại khối.
- **Viewer** (Playwright Chromium, máy chủ của kho tại cổng 8771, `wait_until="load"`), 1440 × 900 và 390 × 844: 164 `.material-block` khớp số khối Markdown; 2 123 công thức KaTeX, 0 `.katex-error`; mục lục 35 liên kết; không cuộn ngang; 12 ảnh tải được; không lỗi console ngoài thông báo CSP về script nội dòng của reloadserver; 8 cảnh báo KaTeX chế độ strict do chữ Việt trong `\text{…}` của các dòng căn cứ (cảnh báo, không phải lỗi). Chế độ in: 72/72 khối `proof`, `hint`, `solution` mở. Ảnh chụp: `/tmp/claude-1000/-data-tqlong-ds-foundation-algorithms/120f1262-3ea0-45af-8c12-2dcf2a1526d1/scratchpad/shots/note06new-*.png`, đã xem trực tiếp.
- **`git diff --check`**: không lỗi.

### Tự kiểm `no-ai-slop` (chế độ Edit, theo `eval.md`)

| Nhóm kiểm | Kết quả |
|---|---|
| Giữ ý, không thêm khẳng định, ví dụ, số liệu, nguồn | Đạt có ghi chú: các lập luận mới chỉ nằm ở danh sách phản ví dụ và đoạn "Trong thực hành", liệt kê ở mục trên để rà toán; mọi số khác lấy từ ghi chú cũ, outline hoặc lời giải đã kiểm trong ghi chú diễn giả. |
| Giọng và mức trang trọng | Đạt: giữ văn phong học thuật của học phần; "chúng ta" cho kế hoạch và lựa chọn, "ta" trong tính toán, câu khách quan trong khối hình thức; tài liệu không làm chủ ngữ. |
| Từ cấm, trạng từ rỗng, cụm rỗng | Đạt: đã bỏ "thực sự", "chính là", "đáng kể", "một cách hiển nhiên"; không có từ quảng bá. |
| Tương phản nhị phân, câu hỏi tu từ, mở đầu rỗng | Đạt có ghi chú: các cặp "X, không phải Y" còn lại là phân biệt toán học bắt buộc ($\widehat s$ với $s$, xác suất theo cặp với tỷ lệ kho, mô hình với số đo); câu hỏi trong văn bản là câu hỏi nghiên cứu được trả lời ngay (đầu Mục 2.3, trước Mệnh đề 06.5). |
| Siêu bình luận, câu kết sáo, tóm lược thừa | Đạt: không có "điểm mấu chốt", "cần lưu ý"; đoạn kết mục là yêu cầu của chuẩn và dẫn số hiệu. |
| Định dạng | Đạt: danh sách chỉ dùng cho mục song song (giả thiết, trường hợp, bước); in đậm chỉ ở nhãn bước, nhãn phần; một gạch ngang dài duy nhất ở tiêu đề theo mẫu. |
| Nhịp câu | Đạt có ghi chú: các khối lặp cùng khuôn (Dữ kiện, Tính, Kiểm tra lại; bốn phần của định lý) do chuẩn quy định; văn xuôi giữa các khối đổi độ dài câu. |

### Sai lệch, giới hạn và việc còn lại

- **Độ dài vượt đích.** Đích của giao việc là 11 000–16 000 từ; bản hiện tại 27 451 từ theo cách đếm khoảng trắng (25 740 khi bỏ công thức khối và mã), vượt cả khoảng thường gặp 8 000–20 000 của `AGENTS.md`. Nguyên nhân: tám bước cho mười hai khái niệm và thuật toán trọng tâm, bốn tình huống, 28 bài tập có gợi ý và lời giải (riêng các bài sách khoảng 2 000 từ), bảng ký hiệu và bản đồ chủ đề, danh sách "Bỏ giả thiết"; tiếng Việt đếm theo âm tiết. Ghi chú mẫu Bài 05 của `../rl-plan` theo cùng chuẩn có 26 226 từ theo cùng cách đếm. Cần điều phối viên quyết định có rút gọn hay không; các chỗ có thể rút mà không bỏ yêu cầu: bảng chi phí lặp trong Thuật toán 06.4 (đã có ở Mệnh đề 06.11), Ví dụ 06.14 (trùng một phần Ví dụ 06.15), đoạn mở Mục 3.7 (trùng số của Ví dụ 06.12), câu (a) của Bài tập 06.1.
- **Cảnh báo KaTeX.** 8 cảnh báo strict do chữ Việt trong `\text{…}` của cột căn cứ, theo đúng dạng `&&\text{(...)}` mà `AGENTS.md` yêu cầu; hiển thị đúng.
- **Định nghĩa MinHash.** Ghi chú giữ cách viết của ghi chú cũ, $h_\pi(A)=\min_{a\in A}\pi(a)$ là thứ hạng; outline Bài 05 viết $h_\pi$ là định danh phần tử đầu. Hai cách cho cùng biến cố trùng vì $\pi$ là song ánh; cần thống nhất khi rà mạch liên bài.
- **Thuật ngữ liên bài.** Outline Bài 07 viết "băm nhạy cảm cục bộ (LSH)"; Bài 06 dùng "băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH)" như `AGENTS.md`.
- **Storyboard.** Bảng N01–N16 ở mục "Đồng bộ sau năm báo cáo độc lập" và các phiếu trang deck là bản lịch sử; ánh xạ hiện hành nằm ở phần "Kiến trúc ghi chú bài giảng tự học" và outline mục 4. Phiếu trang, bảng `data-slide-id` ↔ `note-topic-id`, mục phân bổ thời gian thuộc giai đoạn 2.
- **Deck.** Chưa sửa. Số hiệu trên deck phải lấy từ danh sách cuối ở trên; kế hoạch mục D có các số bài tập tạm tính khác (06.21–06.28 cho recitation), cần thay bằng 06.20–06.25 và 06.28.
- **Rà soát.** Ghi chú chờ tác tử rà toán (tính lại mọi số, kiểm các phản ví dụ mục trên) và tác tử rà mạch viết (tám bước, đoạn kết mục, giọng kể, tính tự chứa). Chưa có phát hiện nào trong lượt này.

### Giai đoạn 2: bộ trang chiếu (2026-10-14)

**Phạm vi.** Giai đoạn 1 được điều phối viên chấp nhận, kể cả ngoại lệ độ dài của ghi chú. Giai đoạn 2 do tác tử soạn thực hiện, vẫn là tác tử duy nhất được ghi tệp; hai tác tử rà toán và rà mạch viết rà ghi chú song song, chỉ đọc. Tệp đã sửa: `lecture-06-tim-cap-tuong-dong-bang-lsh.html` (viết lại theo kế hoạch mục A–D), `outline.md` (mục 1, 5, 8), `storyboard.md` (bản đồ hành trình, phân bổ thời gian, ngoại lệ mật độ, 77 phiếu trang, bảng ánh xạ `data-slide-id` ↔ `note-topic-id`) và tệp này. `lecture-note.md`, CSS, SVG, viewer, index không đổi. Không commit.

**Quyết định cấu trúc.**

- Giữ 7 `<section>` ngoài, lớp gốc `.reveal.course-deck.lecture-lsh`, `lang="vi"`, 1280 × 720, cấu hình Reveal và chân trang cũ; không `<style>`, không style nội dòng, không `.dense`, không `fragment`.
- 77 trang (69 giảng, 8 bài tập), phân bố 8/17/14/14/9/7/8. Thêm 6 trang tiêu đề mạch `lec06-s0N-00` với `id="mach-N"` (N = 2…7), 4 trang mới (s01-06 Tiên quyết và quy ước, s01-08 Vấn đề trung tâm, s06-05 Kết quả và giả thiết không được bỏ, s06-08 Nguồn và tài liệu đọc), 7 trang tách (s01-07 từ s01-02; s02-15 từ s02-09; s02-16 từ s02-13; s04-12 từ s04-04; s04-13 từ s04-08; s05-07 từ s05-05; s05-08 từ s05-06). Các trang cũ giữ mã; `id` của trang cũ không đổi.
- Mạch mở đầu theo đúng thứ tự: bìa (câu luận đề ở `p.supporting-text`) → Tiên quyết và quy ước → Mục tiêu học tập → Nội dung (ol 1–7 + "Đọc trước:") → Vấn đề trung tâm → Ví dụ: kho một triệu tài liệu → Bài toán tìm cặp tương đồng → Câu hỏi.
- Mạch kết luận: tiêu đề mạch → bảng kết quả–giả thiết → bảng thuật toán–bảo đảm–chi phí (s06-02 đổi vai trò) → Trả lời vấn đề trung tâm (gộp nội dung s06-01 và s06-02 cũ; bỏ hình `quy-trinh-cap.svg` khỏi trang này) → hai trang Câu hỏi tự kiểm tra → Nguồn và tài liệu đọc (ghi công `http://www.mmds.org`, liên kết viewer, nối Bài 07).
- Thu hồi kho một triệu tài liệu theo quyết định 2 của điều phối viên: dòng cuối s06-01 nêu $\binom{10^6}{2}=499\,999\,500\,000$ và giả định luyện tập $10^6$ cặp ứng viên, số phép xác minh giảm khoảng $5\cdot10^5$ lần; lời giải câu 2 cũ của s01-05 chuyển vào ghi chú diễn giả của s06-01.
- Bỏ toàn bộ 58 dòng `p.ex-source`; nguồn giữ trong ghi chú diễn giả. Bảy trang đề recitation giữ một dòng "Nguồn: MMDS 3e, Bài …, tr.…" dùng lớp `ex-note` (quyết định 3).
- Nhãn "Quy tắc:" ở trang ước lượng góc đổi thành "Thuật toán." (quyết định 7). Mọi nhãn trên mặt trang thuộc danh sách của `AGENTS.md` (kiểm bằng grep: Nhu cầu, Nhắc lại, Ký hiệu, Giả thiết, Định nghĩa., Định lý., Mệnh đề., Bổ đề., Chứng minh., Thuật toán., Ví dụ., Đầu vào, Đầu ra, Bất biến, Điều kiện dừng, Trường hợp biên, Mô hình, Ý nghĩa, Kết luận, Lưu ý, Quy ước, Câu hỏi, Đọc trước, Nguồn).
- Mỗi trang có nhiều nhất một câu kết luận cuối trang; mọi `ex-note` chứa câu văn được chuyển thành dòng có nhãn hoặc vào ghi chú diễn giả. Trang ví dụ, thuật toán, tính đúng, chứng minh, chi phí, bài tập mang tiền tố tương ứng.
- Trang Nội dung dùng `agenda-slide` với danh sách chia hai cột (`ex-grid2`, lớp dùng chung) vì bảy mục ở cỡ chữ 42 px tràn khung; không thu nhỏ chữ. Trang bài tập 3.6.1 và 3.8.2 dùng các dòng "(a)…(d)" thay `ol type="a"` vì CSS chung hiển thị số.
- CSS: không sửa. Lớp `.lsh-orientation` không còn được dùng trong deck. Deck phụ thuộc các lớp `strand-title`, `strand-title-body`, `strand-number`, `strand-lead`, `strand-keys` hiện nằm trong thay đổi chưa commit của `lecture-style.css`; cần commit CSS chung trước hoặc cùng deck (điểm G5.9 của kế hoạch).

**Số hiệu ghi chú trên mặt trang** (tối đa một lần mỗi trang): s02-11 Định lý 06.7; s02-12 Mệnh đề 06.9; s02-13 Mệnh đề 06.11; s02-15 Mệnh đề 06.5; s03-03 Mệnh đề 06.15; s03-07 Định nghĩa 06.22; s03-08 Hệ quả 06.23; s03-10 Mệnh đề 06.25; s03-12 Nhận xét 06.26; s04-02 Mệnh đề 06.28; s04-05 Định lý 06.31; s04-08 Bổ đề 06.34; s04-09 Định lý 06.35; s04-10 Mệnh đề 06.37; s04-12 Thuật toán 06.32; s05-03 Mệnh đề 06.41. Ghi chú diễn giả của các trang câu hỏi, recitation và tổng kết dẫn số Bài tập 06.k tương ứng (06.1–06.3, 06.5, 06.7–06.10, 06.12–06.28).

**Mật độ trước → sau.** Script cũ `tools/density.py` (bỏ sót trang đầu mỗi section): trước 53 trang, trung vị 53, lớn nhất 108, 23 trang > 60, 35 trang > 40; sau 70 trang, trung vị 39,5, lớn nhất 78, 5 trang > 60, 33 trang > 40. Script sửa `w06/dens.py` trong scratchpad (tính mọi trang, đếm âm tiết có chữ cái, bỏ tiêu đề, công thức, giả mã và ghi chú; đếm dòng `p`, `li`, hàng `tbody`, `h3`; đếm khối `ex-equation` và `$$`): trước 60 trang, trung vị 53, lớn nhất 108, 26 trang > 60, 11 trang > 80; sau 77 trang, trang nội dung trung vị 40, lớn nhất 78, 34 trang > 40, 5 trang > 60, 0 trang > 80. Năm trang > 60 đều thuộc loại trần 80: s01-02 mục tiêu (76), s06-01 tổng kết (78), s06-05 bảng kết quả (63), s04-10 bảng chi phí (69), s07-07 đề recitation (71). Không trang nội dung nào vượt trần 60; không trang nào vượt 1,5 lần trần. Trang > 6 dòng: chỉ s01-07 (8 dòng, ngoại lệ ghi trong storyboard). Dòng > 20 âm tiết: chỉ câu luận đề của bìa (25) và dòng dẫn trang tiêu đề mạch 3–7 (21–23, trong trần 25 của dòng dẫn). Không trang nào quá 3 khối công thức hay quá một câu kết luận. Ghi chú diễn giả mọi trang trong khoảng 59–142 âm tiết; trang tiêu đề mạch 70–102.

Bảng mật độ từng trang (cột "Trần": 60 cho trang nội dung, 80 cho mục tiêu, nội dung, tổng kết, bảng, chi phí, đề recitation; "—" cho bìa và trang tiêu đề mạch):

| `data-slide-id` | Tiêu đề | Quyết định | Âm tiết trước → sau | Trần | Dòng | Dòng dài nhất | Khối công thức | Âm tiết ghi chú |
|---|---|---|---|---:|---:|---:|---:|---:|
| `lec06-s01-01` | Tìm cặp tương đồng bằng LSH | `sửa` | 32 → 49 | — | 4 | 25 | 0 | 83 |
| `lec06-s01-06` | Tiên quyết và quy ước | `thêm` | — → 58 | 60 | 5 | 13 | 0 | 91 |
| `lec06-s01-02` | Mục tiêu học tập | `tách` | 89 → 76 | 80 | 5 | 20 | 0 | 82 |
| `lec06-s01-07` | Nội dung | `thêm` | — → 45 | 80 | 8 | 6 | 0 | 97 |
| `lec06-s01-08` | Vấn đề trung tâm | `thêm` | — → 59 | 60 | 6 | 13 | 0 | 107 |
| `lec06-s01-03` | Ví dụ: kho một triệu tài liệu | `sửa` | 46 → 51 | 60 | 6 | 15 | 2 | 89 |
| `lec06-s01-04` | Bài toán tìm cặp tương đồng | `sửa` | 40 → 28 | 60 | 3 | 13 | 0 | 96 |
| `lec06-s01-05` | Câu hỏi về bài toán tìm cặp | `sửa` | 80 → 42 | 60 | 5 | 13 | 0 | 85 |
| `lec06-s02-00` | 2. Phân dải chữ ký MinHash | `thêm` | — → 32 | — | 2 | 18 | 0 | 86 |
| `lec06-s02-01` | Dải, khóa dải và cặp ứng viên | `sửa` | 84 → 59 | 60 | 5 | 14 | 0 | 119 |
| `lec06-s02-06` | Ví dụ: năm cột, dải ba hàng | `sửa` | 67 → 43 | 60 | 6 | 13 | 0 | 103 |
| `lec06-s02-02` | Ví dụ: bốn tập đặc trưng | `sửa` | 32 → 22 | 60 | 6 | 11 | 1 | 87 |
| `lec06-s02-03` | Ví dụ: bốn tập đặc trưng, thùng của dải 1 | `sửa` | 38 → 29 | 60 | 6 | 12 | 0 | 70 |
| `lec06-s02-04` | Ví dụ: bốn tập đặc trưng, hợp qua hai dải | `sửa` | 39 → 34 | 60 | 6 | 12 | 1 | 59 |
| `lec06-s02-05` | Ví dụ: bốn tập đặc trưng, xác minh | `sửa` | 53 → 38 | 60 | 6 | 12 | 0 | 64 |
| `lec06-s02-07` | Thuật toán: phân dải và xác minh | `sửa` | 18 → 15 | 60 | 5 | 7 | 1 | 86 |
| `lec06-s02-08` | Thuật toán: phân dải và xác minh | `sửa` | 17 → 13 | 60 | 5 | 3 | 0 | 127 |
| `lec06-s02-09` | Tính đúng: phân dải và xác minh | `tách` | 103 → 59 | 60 | 5 | 13 | 0 | 134 |
| `lec06-s02-15` | Tính đúng: phân dải và xác minh | `thêm` | — → 59 | 60 | 5 | 14 | 0 | 99 |
| `lec06-s02-10` | Xác suất trùng một dải | `sửa` | 57 → 49 | 60 | 5 | 16 | 1 | 89 |
| `lec06-s02-11` | Xác suất thành ứng viên | `sửa` | 43 → 46 | 60 | 4 | 20 | 1 | 72 |
| `lec06-s02-12` | Đường cong S và chọn số dải | `giữ` | 35 → 31 | 60 | 3 | 17 | 0 | 109 |
| `lec06-s02-13` | Chi phí: phân dải và xác minh | `tách` | 90 → 53 | 80 | 6 | 16 | 0 | 91 |
| `lec06-s02-16` | Chi phí: bộ nhớ và trường hợp xấu nhất | `thêm` | — → 38 | 80 | 5 | 17 | 1 | 87 |
| `lec06-s02-14` | Câu hỏi về phân dải | `sửa` | 42 → 32 | 60 | 6 | 19 | 0 | 117 |
| `lec06-s03-00` | 3. Khoảng cách và họ nhạy cảm | `thêm` | — → 38 | — | 2 | 22 | 0 | 79 |
| `lec06-s03-01` | Độ đo khoảng cách | `sửa` | 55 → 32 | 60 | 6 | 13 | 3 | 90 |
| `lec06-s03-02` | Độ đo khoảng cách và chuẩn vector | `sửa` | 24 → 25 | 60 | 6 | 11 | 1 | 74 |
| `lec06-s03-03` | Khoảng cách Jaccard | `sửa` | 39 → 33 | 60 | 5 | 15 | 2 | 97 |
| `lec06-s03-04` | Khoảng cách góc | `sửa` | 41 → 27 | 60 | 5 | 8 | 0 | 101 |
| `lec06-s03-05` | Khoảng cách chỉnh sửa | `sửa` | 66 → 40 | 60 | 4 | 19 | 1 | 117 |
| `lec06-s03-06` | Khoảng cách Hamming | `giữ` | 32 → 31 | 60 | 6 | 14 | 1 | 80 |
| `lec06-s03-07` | Họ băm nhạy cảm theo tính cục bộ | `sửa` | 53 → 40 | 60 | 5 | 19 | 2 | 93 |
| `lec06-s03-08` | Ví dụ: họ MinHash theo Jaccard | `sửa` | 36 → 35 | 60 | 5 | 11 | 0 | 83 |
| `lec06-s03-09` | Phép ghép đồng thời | `sửa` | 73 → 45 | 60 | 5 | 17 | 1 | 87 |
| `lec06-s03-10` | Phép ghép ít nhất một | `sửa` | 73 → 53 | 60 | 6 | 20 | 1 | 87 |
| `lec06-s03-11` | Ví dụ: hai thứ tự ghép trên 16 phép thử | `sửa` | 71 → 52 | 60 | 5 | 15 | 0 | 95 |
| `lec06-s03-12` | Phân dải như phép ghép AND rồi OR | `sửa` | 46 → 33 | 60 | 3 | 15 | 0 | 113 |
| `lec06-s03-13` | Câu hỏi về độ đo và phép ghép | `giữ` | 48 → 36 | 60 | 4 | 19 | 0 | 93 |
| `lec06-s04-00` | 4. Các họ băm theo độ đo | `thêm` | — → 40 | — | 2 | 21 | 0 | 100 |
| `lec06-s04-01` | Họ băm chọn tọa độ | `sửa` | 46 → 32 | 60 | 6 | 11 | 1 | 97 |
| `lec06-s04-02` | Tính nhạy cảm của họ chọn tọa độ | `sửa` | 37 → 39 | 60 | 6 | 15 | 2 | 89 |
| `lec06-s04-03` | Hàm băm dấu theo siêu phẳng | `giữ` | 38 → 29 | 60 | 6 | 15 | 2 | 114 |
| `lec06-s04-05` | Tính nhạy cảm của họ siêu phẳng | `giữ` | 32 → 28 | 60 | 6 | 11 | 2 | 103 |
| `lec06-s04-04` | Ví dụ: chữ ký dấu của hai vector, ba pháp tuyến | `tách` | 66 → 31 | 60 | 6 | 13 | 0 | 73 |
| `lec06-s04-12` | Ước lượng góc từ chữ ký dấu | `thêm` | — → 42 | 60 | 4 | 15 | 0 | 114 |
| `lec06-s04-06` | Ví dụ: ba điểm trên trục thứ nhất | `sửa` | 78 → 38 | 60 | 6 | 15 | 0 | 120 |
| `lec06-s04-07` | Họ chiếu có dịch ngẫu nhiên | `sửa` | 57 → 37 | 60 | 5 | 14 | 1 | 115 |
| `lec06-s04-08` | Xác suất chung thùng khi cố định hướng | `tách` | 77 → 28 | 60 | 3 | 18 | 1 | 90 |
| `lec06-s04-13` | Chứng minh: xác suất chung thùng khi cố định hướng | `thêm` | — → 44 | 60 | 4 | 16 | 0 | 116 |
| `lec06-s04-09` | Tính nhạy cảm của họ chiếu hai chiều | `sửa` | 37 → 38 | 60 | 6 | 13 | 1 | 95 |
| `lec06-s04-10` | Chi phí: chữ ký theo ba họ | `sửa` | 102 → 69 | 80 | 6 | 17 | 0 | 110 |
| `lec06-s04-11` | Câu hỏi về các họ theo độ đo | `sửa` | 68 → 50 | 60 | 5 | 18 | 0 | 103 |
| `lec06-s05-00` | 5. Ứng dụng tìm cặp tương đồng | `thêm` | — → 36 | — | 2 | 22 | 0 | 93 |
| `lec06-s05-01` | Đối sánh thực thể | `sửa` | 69 → 52 | 60 | 4 | 15 | 0 | 142 |
| `lec06-s05-02` | Họ băm ba ô cho vân tay | `sửa` | 86 → 59 | 60 | 5 | 16 | 0 | 116 |
| `lec06-s05-03` | Ví dụ: xác suất va chạm của hàm ba ô | `sửa` | 99 → 55 | 60 | 5 | 17 | 0 | 117 |
| `lec06-s05-04` | Phép ghép trong đối sánh vân tay | `sửa` | 69 → 54 | 60 | 5 | 19 | 1 | 110 |
| `lec06-s05-05` | Bản tin gần trùng | `tách` | 108 → 58 | 60 | 5 | 15 | 0 | 126 |
| `lec06-s05-07` | Ví dụ: shingle theo từ dừng | `thêm` | — → 57 | 60 | 5 | 16 | 0 | 66 |
| `lec06-s05-06` | Câu hỏi về đối sánh thực thể và vân tay | `tách` | 107 → 50 | 60 | 4 | 18 | 0 | 106 |
| `lec06-s05-08` | Câu hỏi về shingle theo từ dừng | `thêm` | — → 30 | 60 | 2 | 20 | 0 | 79 |
| `lec06-s06-00` | 6. Tổng kết và tự kiểm tra | `thêm` | — → 39 | — | 2 | 23 | 0 | 102 |
| `lec06-s06-05` | Kết quả và giả thiết không được bỏ | `thêm` | — → 63 | 80 | 4 | 15 | 0 | 94 |
| `lec06-s06-02` | Thuật toán, bảo đảm và chi phí | `sửa` | 82 → 53 | 80 | 4 | 14 | 0 | 109 |
| `lec06-s06-01` | Trả lời vấn đề trung tâm | `sửa` | 64 → 78 | 80 | 6 | 19 | 0 | 122 |
| `lec06-s06-03` | Câu hỏi tự kiểm tra | `sửa` | 52 → 34 | 60 | 4 | 13 | 0 | 92 |
| `lec06-s06-04` | Câu hỏi tự kiểm tra | `sửa` | 69 → 51 | 60 | 4 | 20 | 0 | 93 |
| `lec06-s06-08` | Nguồn và tài liệu đọc | `thêm` | — → 56 | 60 | 5 | 18 | 0 | 81 |
| `lec06-s07-00` | 7. Bài tập vận dụng | `thêm` | — → 40 | — | 2 | 23 | 0 | 70 |
| `lec06-s07-01` | Bài tập: bảng giá trị đường cong S | `sửa` | 37 → 34 | 80 | 5 | 14 | 1 | 68 |
| `lec06-s07-02` | Bài tập: ngưỡng của đường cong S | `sửa` | 36 → 30 | 80 | 6 | 15 | 0 | 82 |
| `lec06-s07-03` | Bài tập: xác suất qua nhiều tầng ghép | `sửa` | 64 → 43 | 80 | 6 | 20 | 0 | 73 |
| `lec06-s07-04` | Bài tập: hàm chọn tọa độ trên bốn vector | `sửa` | 38 → 32 | 80 | 5 | 16 | 1 | 77 |
| `lec06-s07-05` | Bài tập: chữ ký dấu của ba vector | `sửa` | 39 → 29 | 80 | 6 | 13 | 0 | 91 |
| `lec06-s07-06` | Bài tập: thùng chiếu trên ba trục | `sửa` | 41 → 30 | 80 | 5 | 9 | 0 | 97 |
| `lec06-s07-07` | Bài tập: hai cấu trúc ghép cho vân tay | `sửa` | 98 → 73 | 80 | 6 | 17 | 0 | 109 |

**Kiểm trình duyệt.** Playwright Chromium (`w06/deckcheck.py`), máy chủ của kho tại cổng 8771, `wait_until="load"`, tắt hiệu ứng chuyển trang bằng `Reveal.configure`, duyệt cả 77 trang bằng `Reveal.getIndices` và `Reveal.slide(h, v, 99)` ở 1600 × 900 và 390 × 844:

- không lỗi console, kể cả thông báo CSP; không phản hồi lỗi, không tài nguyên ngoài máy cục bộ; 0 `.katex-error`;
- ở 1600 × 900, không phần tử nào (trừ phần nội bộ của KaTeX) vượt khung `.slides`; mọi ảnh tải được; cỡ chữ đo được ở khung 1280 × 720: 28 px cho đoạn văn và danh sách, 25 px trong bảng, 24 px chỉ ở bảy dòng nguồn của trang recitation (`ex-note`, chú thích ngắn theo lớp dùng chung);
- `#/1`…`#/7` mở đúng `lec06-s01-01`, `lec06-s02-00`, …, `lec06-s07-00`; phím Space đi qua đủ 77 trang theo đúng thứ tự HTML;
- ở 390 × 844, Reveal thu nhỏ khung 16:9 như các bài trước (giới hạn runtime dùng chung đã ghi ở lượt 02/10), không lỗi;
- lượt đầu phát hiện trang Nội dung tràn khung với danh sách một cột và ảnh chụp giữa hiệu ứng chuyển trang; đã sửa bố cục hai cột và tắt hiệu ứng khi chụp; lượt sau sạch.
- Ảnh chụp: `/tmp/claude-1000/-data-tqlong-ds-foundation-algorithms/120f1262-3ea0-45af-8c12-2dcf2a1526d1/scratchpad/shots/deck06-*.png` (mạch mở đầu, mọi trang tiêu đề mạch, mạch kết luận, các trang tách và các trang có hình, ở cả hai cỡ) và các tấm ghép `sheet-deck06-*.png`; tác tử soạn đã xem toàn bộ tấm ghép.
- `git diff --check`: không lỗi. Kiểm cân bằng thẻ HTML bằng `html.parser`: không thẻ lệch hay thiếu đóng; 77 `data-slide-id` duy nhất, không trùng `id`.

**Tự kiểm `no-ai-slop` (Edit) cho mặt trang và ghi chú diễn giả.**

| Nhóm kiểm | Kết quả |
|---|---|
| Không thêm khẳng định, số liệu | Đạt: mọi số lấy từ deck cũ, ghi chú hoặc outline (G6 của kế hoạch); câu mới chỉ sắp lại hoặc rút gọn. |
| Văn phong mặt trang | Đạt: không "chúng ta", "ta thấy", "rõ ràng", câu hỏi tu từ hay lời chỉ đường; định nghĩa dùng "là", "gọi là"; không mã nội bộ trên mặt trang và trong ghi chú. |
| Ghi chú diễn giả | Đạt có ghi chú: không mở bằng "Trang này"; đã bỏ các cụm điều hướng "trang sau", "trang trước", "ví dụ trước", "bài trước" và "Đáp án"; ghi chú trang tiêu đề mạch còn nhắc "mạch" theo số, không phải mã nội bộ. |
| Lặp và câu rỗng | Đạt: câu kết luận cuối trang là con số hoặc kết luận có điều kiện; không khẩu hiệu, không chuỗi mũi tên. |
| Định dạng | Đạt: nhãn in đậm chỉ ở đầu dòng; không gạch ngang dài trên mặt trang. |

**Việc còn lại.** Rà đủ năm vai trên deck (quyết định 8 của điều phối viên); rà `quill` về thuật ngữ và liên tục giữa deck và ghi chú; phiếu kiểm `slide_authoring_standard.md` ở bước kiểm định cuối; đồng bộ phần "Đồng bộ sau năm báo cáo độc lập" của storyboard (bảng N01–N16 lịch sử) nếu điều phối viên muốn xóa dấu vết cũ; thứ tự commit với CSS chung.

### Lượt sửa ghi chú theo hai báo cáo rà (2026-10-14)

**Phạm vi.** Tác tử soạn thảo (fork, Opus 5.5, effort `high`, là tác tử ghi duy nhất) sửa `materials/lec-06/lecture-note.md` theo hai báo cáo rà độc lập chỉ đọc: `review-note06-math.md` (độ chính xác toán và thuật toán: 1 nghiêm trọng, 5 trung bình, 11 nhẹ) và `review-note06-storyline.md` (mạch và liên kết: T1–T16 trung bình, N1–N24 nhẹ), cùng 19 quyết định của điều phối viên. Deck không sửa trong lượt này. Chưa commit.

**Quyết định cho báo cáo toán.**

| Mức | Vị trí (số hiệu cũ) | Quyết định | Cách xử lý |
|---|---|---|---|
| nghiêm trọng | Ví dụ 06.17, Tình huống 06.2, Bài tập 06.13, 06.28: độc lập của 1024 phép thử gán cho Mệnh đề 06.25 | sửa | Nêu "giả thiết độc lập thêm của MMDS" (va chạm qua các hàm và giữa hai nhóm AND coi là độc lập), không suy từ mệnh đề phép ghép; giữ số của sách. Thêm vào Giới hạn của Tình huống 06.2 và lời giải 06.28: theo Jensen, xác suất bỏ sót thật $\mathbb E[(1-p)^{1024}]\ge(1-q_T)^{1024}$, số của sách là cận dưới; tương tự $0{,}0634$ là cận trên của xác suất nhận ảnh khác ngón dưới OR 1024. Thêm bất đẳng thức Jensen vào Kiến thức tiên quyết. Không dùng số mô phỏng. |
| trung bình | Tóm tắt và lời giải 06.10(c): cận $1/3$ "cần dịch đều" | sửa | Bước 2 của định lý chỉ dùng "chung thùng cần $\ell<a$", đúng với mọi $\delta$; ghi rõ ở Điều kiện áp dụng, cuối Bước 2, đoạn vai trò giả thiết, Tóm tắt và 06.10(c). |
| trung bình | Nhận xét 06.36: "ghép nhiều hàm để phân biệt hai khoảng cách gần nhau" | sửa | Thay bằng lập luận định tính của MMDS §3.7.5 (tr.113): $d_1<d_2\Rightarrow p_1>p_2$ rồi khuếch đại; nói rõ sách không tính $p_1,p_2$, không chứng minh đơn điệu, không có độ dịch. Sửa "Trong thực hành" của Mục 4.3 tương ứng. |
| trung bình | $L_q$ là độ đo khi $q\ge1$ | sửa (lượt trước trong cùng vòng) | Ghi MMDS §3.5.2 (tr.97–98) định nghĩa $L_r$ cho mọi $r$; điều kiện $q\ge1$ là Minkowski, dùng không chứng minh. |
| trung bình | Tiên quyết MinHash gán định nghĩa thứ hạng cho Bài 05 | sửa | Phát biểu lại theo ghi chú Bài 05 Mục 5 (phần tử đầu tiên theo hoán vị); phản ví dụ của Định lý 06.7 dùng "bằng $a$". |
| trung bình | Tóm tắt gạch 4 dẫn sai kỳ vọng của Mệnh đề 06.11 | sửa | Kỳ vọng của $K$, $Q$ ở Mệnh đề 06.13 theo hoán vị; Nhận xét 06.12 cho $K=\binom C2$; kỳ vọng ở 06.11 chỉ theo hàm băm của bảng. |
| nhẹ | Phản ví dụ tập rỗng (quy ước $+\infty$) | sửa | "theo quy ước đầu ra của thuật toán quét (ghi chú Bài 05, Mục 9 và 11)". |
| nhẹ | Va chạm ô "thêm cặp vào $\mathcal C$" | sửa | Đổi thành $\mathrm{CAND}\supseteq\mathcal C$, $\Pr[(c,d)\in\mathrm{CAND}]\ge P_{b,r}(s)$. |
| nhẹ | Mệnh đề 06.25: gạch "bỏ cùng hàm" thiếu phản ví dụ | sửa | Phản ví dụ $S_1$ với hai hoán vị độc lập cho xác suất $1/2$ thay cho $1$. |
| nhẹ | Bước 2 chứng minh 06.15 "ba tiên đề đầu" | sửa | Đổi tên bước theo Định nghĩa 06.14. |
| nhẹ | Dạng chữ S chỉ cần $r\ge2$ | sửa | Cần $b\ge2$ và $r\ge2$ (Mục 2.4 và Nhận xét 06.10). |
| nhẹ | Tóm tắt gạch 1 trộn hai mức dùng lại hàm | sửa | Trong dải: $s$ thay $s^r$; giữa các dải: $s^r$ thay $P_{b,r}(s)$. |
| nhẹ | Mục 3.7 gán cách nhìn "quyết định trên từng cặp" cho Ví dụ 3.20 | sửa | Dẫn §3.6.1 cho cách nhìn này. |
| nhẹ | Mục 4.3 "ý tưởng chiếu có dịch" ở §3.7.5 | sửa | "phép chiếu lên đường thẳng ngẫu nhiên và chia khoảng". |
| nhẹ | Lời giải 06.16 viết như khẳng định xác định | sửa | Nói về kỳ vọng của số cặp bỏ sót, $K$, $Q$ (Mệnh đề 06.13). |
| nhẹ | Định lý 06.31 "mọi $D\ge2$" | sửa | "Mọi $D\ge1$", với $D=1$ thuộc Bước 1. |
| nhẹ | "1 trên 3 000"; trang Ví dụ 3.11, 3.24 | sửa | Khoảng 1 trên 2 800 (sách làm tròn 3 000); Ví dụ 3.11 tr.92–93; Ví dụ 3.24 tr.120–121. |

**Quyết định cho báo cáo mạch.**

| Mã | Quyết định | Cách xử lý |
|---|---|---|
| T1 | sửa | Kế hoạch mục sau chỉ nêu ở đoạn kết mục trước; đoạn mở Mục 2–5 viết lại thành nhu cầu và dữ kiện kế thừa. |
| T2 | sửa | Bài 07 dùng LSH làm bộ lọc ứng viên cho truy vấn và so với đồ thị thế giới nhỏ phân tầng (HNSW), lượng tử hóa tích (PQ), viết đủ tên; sửa ở "Ứng dụng trong các bài sau" và câu cuối Tóm tắt. |
| T3 | sửa | Mục 5.3 dẫn "ghi chú Bài 05, Mục 12" (MMDS §3.2.4, tr.80) trước Định nghĩa 06.43 và nói định nghĩa được nhắc lại; "shingle ký tự như Bài 05" thành "$k$-shingle ký tự (ghi chú Bài 05, Mục 3)"; bỏ gạch trỏ ngược trong danh sách ứng dụng. |
| T4 | sửa | Như mục "dạng chữ S" của báo cáo toán. |
| T5 | sửa | Định nghĩa 06.34 (cũ 06.33) trên $\mathbb R^D$, $u$ đều trên mặt cầu đơn vị, không nêu cách sinh; tiêu đề "Họ chiếu có dịch"; Ví dụ 06.16 là hàm cùng dạng trên $\mathbb R^3$ với $u=e_1$, $\delta=0$; Bổ đề 06.35 đúng mọi $D$; Định lý 06.36 phát biểu và chứng minh cho $D=2$, dẫn MMDS §3.7.4 (tr.111–113). |
| T6 | sửa | Như mục Tóm tắt gạch 4 của báo cáo toán. |
| T7 | sửa | Thêm Bài tập 06.29 (chọn $(b,r)$ cho $t=0{,}6$, kiểm mục tiêu 2) và 06.30 (chứng minh biến thể $b$ bảng cho $\mathrm{CAND}=\mathcal C$, phản ví dụ một bảng thiếu số dải, kiểm mục tiêu 1) ở cuối Mức vận dụng để không đánh số lại bài tập; câu ánh xạ mục tiêu và số bài "mười sáu" cập nhật. |
| T8 | sửa | 06.3 chép bốn tập và hai hàng chữ ký; 06.21 nhắc lại $P(s)$; 06.26 chép ba điểm. |
| T9 | sửa | Bước 1 Thuật toán 06.33 (cũ 06.32): pháp tuyến độc lập, đẳng hướng, ví dụ tọa độ chuẩn tắc độc lập, chứng minh đẳng hướng ngoài phạm vi; vector $\pm1$ không đẳng hướng. |
| T10 | sửa | Thuật ngữ gốc ở lần đầu: banding, band, bucket, hash table, hyperplane, isotropic, S-curve, cosine similarity; thêm vào bảng thuật ngữ của `outline.md`. |
| T11 | sửa | Thêm $q_F$, $q_T$, $\ell$ vào bảng ký hiệu; quy ước cho $d$, $\pi$, $L$, $k$; Bài tập 06.25–06.26 dùng $[ka,(k+1)a)$, ghi sách viết $j$. |
| T12 | sửa | "Trong thực hành" sau Mệnh đề 06.29, Thuật toán 06.33, Mệnh đề 06.38; đoạn so kết quả với kết quả sau 06.29 và 06.32; Nhận xét 06.24 mới ở Mục 3.6; Ví dụ 06.17 mới ở Mục 5.1 (thang 300 điểm, Bill/William có khoảng cách chỉnh sửa $5=4+7-2\cdot3$). |
| T13 | sửa | Tách các đoạn dài ở Mục 1, 2.2–2.5, 3.1, 3.5, 3.7, Nhận xét 06.37, Tình huống 06.3, Tóm tắt; không còn dòng văn xuôi quá khoảng bốn câu ở các vị trí báo cáo nêu. |
| T14 | sửa | Tình huống 06.1 thêm kết luận theo khung tr.117 (185 điểm: $x\approx10$, $f\approx1$; 115 điểm: $x<45$, $f>0$, không xác định giá trị). Tình huống 06.3 chọn $(b,r)=(20,5)$, $s_{1/2}\approx0{,}509$; theo đơn điệu: $P(0{,}25)\le P(0{,}3)=0{,}047494259$, $P(0{,}75)\ge P(0{,}6)=0{,}801902454$; shingle 10 ký tự cho cả hai loại cặp cùng xác suất trong $[P(0{,}3),P(0{,}4)]=[0{,}047494259;\ 0{,}186049552]$. Câu mở phần tình huống sửa: 06.2 cần giả thiết độc lập thêm, 06.3 cần mô hình MinHash lý tưởng. |
| T15 | sửa | Bỏ giọng người chấm ở lời giải 06.20, 06.21, 06.23, 06.28, thay bằng nhận xét toán học (ví dụ đổi chỗ $(r,b)=(10,3)$ cho $P(0{,}5)\approx0{,}002927$). |
| T16 | sửa | Ví dụ 06.3 đặt tên $B$, CAND, OUT. |
| N1–N5, N7 | sửa | Hình 3.7 của sách; tiêu đề Nhận xét 06.6; bỏ số bước của quy trình §3.4.3; tách "bước thuật toán" và "Bước chứng minh"; 1 trên 2 800; tên bước của 06.15. |
| N6 | sửa | Trang cho $L_q$ (tr.97–98) và Nhận xét 06.17 (MMDS §3.5.4, tr.99). |
| N8 | sửa | Nhận xét 06.21 viết đủ hai tiên đề. |
| N9 | sửa | Định lý 06.32 Bước 2: lập luận phép quay trong $\Pi$; Định lý 06.36 Bước 2: $\gamma=(\alpha-\beta)\bmod\pi$ đều, $\phi=\min(\gamma,\pi-\gamma)$ có $\Pr[\phi\le\psi]=2\psi/\pi$. |
| N10 | sửa | "chữ ký dấu" in đậm tại câu định nghĩa, ngay trước Ví dụ 06.15; đầu ra của Thuật toán 06.33 dùng cùng tên. |
| N11 | sửa | Câu đếm $6$ tích vô hướng × $4$ phép nhân $=24=CmD$; Bài tập 06.11 so số bit với số bit ($64$ bit mỗi từ, gấp 320 lần). |
| N12–N14 | sửa | Vai cặp ảnh theo Định nghĩa 06.1; Kiểm tra lại của Ví dụ 06.18 bằng $0{,}063436634^2$; tuyến tính kỳ vọng dẫn Kiến thức tiên quyết. |
| N15 | sửa | Bỏ lặp "dự đoán của mô hình" ở "Trong thực hành" sau Ví dụ 06.18 và ở Giới hạn của Tình huống 06.2; giữ ở Phạm vi của Mệnh đề 06.42 và một lần ở Tóm tắt. |
| N16 | sửa | Bỏ tài liệu làm chủ ngữ ("Bản soạn", "ghi chú dùng"). |
| N17 | sửa một phần | Câu 5 Tóm tắt có chủ ngữ; giữ giả định $10^6$ cặp vì đã ghi rõ là giả định luyện tập, không là số đo. |
| N18 | sửa | Một câu nhắc lại mô hình khóa–giá trị của Bài 02 cho Bài 3.4.4. |
| N19 | sửa | Ví dụ 3.19 (tr.106). |
| N20 | bác bỏ trong lượt này | Chính tả "vector"/"véc-tơ" là quyết định cấp học phần, ngoài phạm vi chỉ sửa ghi chú 06; chuyển cho điều phối viên. |
| N21 | sửa | Đoạn trực quan Mục 3.6 nêu vì sao chỉ cần hai cận và liên hệ đường xác suất. |
| N22 | sửa | Giải thích bảng tên tương đương (Bill là tên gọi tắt của William) và mô hình hỗn hợp hai thành phần (tỷ phần $f$ trễ 10 ngày, $1-f$ trễ 45 ngày). |
| N23 | bác bỏ | Bài tập 06.2, 06.3, 06.5 đặt ở cuối cụm 2.1–2.3 và 3.1–3.4 theo Bản đồ chủ đề; Bài tập 06.29 mới có thêm phép tính $P_{b,r}$ tại một điểm. |
| N24 | sửa | Định lý 06.36 dẫn MMDS §3.7.4 (tr.111–113); mục tài liệu tham khảo nói rõ bộ tham số và lập luận góc theo MMDS, dịch đều theo Datar và cộng sự. Báo cáo ghi tr.112–113; mục 3.7.4 bắt đầu ở tr.111 theo bản pdftotext. |

**Đánh số lại.** Nhận xét mới chèn sau Hệ quả 06.23 nên dãy số dùng chung từ 06.24 tăng một: Nhận xét 06.24 (mới); Định nghĩa 06.24→06.25, Mệnh đề 06.25→06.26, Nhận xét 06.26→06.27, Định nghĩa 06.27→06.28, Mệnh đề 06.28→06.29, Nhận xét 06.29→06.30, Định nghĩa 06.30→06.31, Định lý 06.31→06.32, Thuật toán 06.32→06.33, Định nghĩa 06.33→06.34, Bổ đề 06.34→06.35, Định lý 06.35→06.36, Nhận xét 06.36→06.37, Mệnh đề 06.37→06.38, Định nghĩa 06.38→06.39, Nhận xét 06.39→06.40, Định nghĩa 06.40→06.41, Mệnh đề 06.41→06.42, Định nghĩa 06.42→06.43. Ví dụ mới chèn sau Ví dụ 06.16: Ví dụ 06.17 (mới), Ví dụ 06.17→06.18, 06.18→06.19. Bài tập 06.1–06.28 và Tình huống 06.1–06.4 giữ số; thêm Bài tập 06.29–06.30. Danh sách số hiệu ở mục "Cấu trúc ghi chú mới và số hiệu cuối cùng" phía trên giữ nguyên như lịch sử và được thay bằng danh sách này. `outline.md` (bảng thuật ngữ, bảng `note-topic-id`) và `storyboard.md` (dòng "Ánh xạ ghi chú", bảng kiến trúc ghi chú, bảng ánh xạ trang–chủ đề) đã đổi theo. Deck chưa đổi; mười tham chiếu số hiệu ghi chú trong deck cần đổi ở lượt sửa deck: `lec06-s03-10` Mệnh đề 06.25→06.26; `lec06-s03-12` Nhận xét 06.26→06.27; `lec06-s04-02` Mệnh đề 06.28→06.29; `lec06-s04-05` Định lý 06.31→06.32; `lec06-s04-12` Thuật toán 06.32→06.33; `lec06-s04-08` Bổ đề 06.34→06.35; `lec06-s04-09` Định lý 06.35→06.36; `lec06-s04-10` Mệnh đề 06.37→06.38; `lec06-s05-03` Mệnh đề 06.41→06.42; `lec06-s06-05` Mệnh đề 06.25→06.26.

**Lập luận mới cần tác tử rà toán kiểm lại.** (1) Phương sai $(\theta/\pi)(1-\theta/\pi)/m$ của $\widehat p_{\ne}$ (sau Thuật toán 06.33). (2) Lập luận phép quay trong $\Pi$ cho Bước 2 của Định lý 06.32. (3) Phản ví dụ $S_1$ với hai hoán vị độc lập cho xác suất $1/2$ (Mệnh đề 06.26). (4) Cận Jensen cho xác suất bỏ sót và xác suất nhận cặp khác ngón (Tình huống 06.2, Bài tập 06.28). (5) Cận đơn điệu trong Tình huống 06.3. (6) Khoảng cách chỉnh sửa Bill/William bằng 5 và tỷ lệ 25 dưới giả định mức trừ $c\,d^2$ (Ví dụ 06.17). (7) Bước 2 Định lý 06.36: $\phi$ đều và cận xa không cần dịch đều. (8) Bài tập 06.29: $s_{1/2}$, $(1/b)^{1/r}$, $P_{b,r}(0{,}3)$ cho bốn cấu hình, bỏ sót $0{,}025219456$ tại $s=0{,}7$. (9) Bài tập 06.30: chứng minh biến thể $b$ bảng và phản ví dụ ba cột. (10) Bài tập 06.11: $6{,}4\cdot10^{10}/(2\cdot10^8)=320$. Mọi số mới được tính lại bằng Python trong phiên.

**Kiểm tra đã chạy.**

- `w06/check.py`: 172 khối mở và đóng khớp, không lồng; dãy số dùng chung 06.1–06.43, ví dụ 06.1–06.19, tình huống 06.1–06.4, bài tập 06.1–06.30 liên tục; 30 bài tập đều có `hint` và `solution`; 19 `note-topic-id` duy nhất; 12 ảnh; số `$$` chẵn; không chuỗi cấm.
- `w06/xref.py`: mọi tham chiếu "loại + số" trỏ đúng một khối cùng loại (0 lỗi trên 96 khối có số).
- Trình xem (`w06/viewer.py`, Playwright Chromium, cổng 8771): 1440 × 900 và 390 × 844 đều render 172 `.material-block`, 0 `.katex-error`, 12 ảnh tải được, không tràn ngang, không yêu cầu mạng ngoài; chế độ in mở 76/76 khối gập. Một lỗi CSP về script nội tuyến của `material-viewer.html` và cảnh báo KaTeX về chữ Việt trong `\text{}` ở hai công thức Mục 2.3–2.4 có từ trước lượt này. Ảnh chụp Mục 4.3, Ví dụ 06.17, Bài tập 06.30 và Tình huống 06.2 ở cả hai cỡ đã xem trực tiếp.
- `git diff --check`: không lỗi.
- Tự kiểm `no-ai-slop` (Edit, theo `eval.md`) cho đoạn mới: không thêm số ngoài nguồn và phép tính kiểm lại; không câu hỏi tu từ, không lời chỉ dẫn người chấm; đoạn mới mở bằng dữ kiện hoặc kết quả.

### Lượt sửa deck theo năm báo cáo rà độc lập (2026-10-14)

**Phạm vi và vai trò.** Tác tử soạn thảo (fork, Opus 5.5, effort `high`, tác tử ghi duy nhất) sửa `lecture-06-tim-cap-tuong-dong-bang-lsh.html`, `storyboard.md`, `outline.md` và tệp này theo danh sách hợp nhất của điều phối viên (`deck06-edit-list.md`, mục A bắt buộc, B sửa, C sửa khi tiện, D bác bỏ) và năm báo cáo chỉ đọc: vai sinh viên, chuyên gia giải thuật và khoa học dữ liệu, độ chính xác toán và thuật toán, phản biện học thuật–sư phạm, kết nối và mạch viết. Ghi chú bài giảng không sửa trong lượt này. Không commit. Tự kiểm `no-ai-slop` (Edit) theo `eval.md` cho mọi câu mới trên mặt trang và trong ghi chú diễn giả: không câu hỏi tu từ, không "chúng ta", không lời chỉ đường hay nhãn quy trình, không thêm số ngoài nguồn và phép tính kiểm lại; mẫu "…, không phải …" chỉ giữ ở chỗ phân biệt hai đối tượng dễ nhầm.

**Quyết định của điều phối viên bị thay.** Quyết định 2 của "Căn chỉnh văn phong 2026-10-14" (thu hồi kho một triệu tài liệu bằng giả định bộ tạo trả $10^6$ cặp) được thay theo A3: trang `lec06-s06-01` dùng giả định trên dữ liệu (mọi cặp ngoài $N$ cặp gần có $s\le0{,}1$), $P_{20,5}(0{,}1)=1-(1-10^{-5})^{20}=1{,}9998\cdot10^{-4}$, $\mathbb E[K]\le N+10^8$, và khoảng 100 giây xác minh thay cho $5{,}79$ ngày. Số $10^6$ cặp cũ giữ trong ghi chú diễn giả như số liệu luyện tập.

**Kết quả chính.** Deck có 78 trang (70 giảng, 8 bài tập); trang mới `lec06-s04-14` "Thuật toán: tìm cặp với họ nhạy cảm" đứng sau trang tiêu đề mạch 4 (A4), 1,5 phút lấy từ s04-01, s04-04, s04-06. Tiêu đề đổi: s06-01 "Câu trả lời cho vấn đề trung tâm"; s07-02 "Bài tập: nghiệm một nửa của đường cong S". Mười số hiệu ghi chú trên deck đã cập nhật theo ghi chú mới: s03-10 Mệnh đề 06.26; s03-12 Nhận xét 06.27; s04-02 Mệnh đề 06.29; s04-05 Định lý 06.32; s04-12 Thuật toán 06.33; s04-08 Bổ đề 06.35; s04-09 Định lý 06.36; s04-10 Mệnh đề 06.38; s05-03 Mệnh đề 06.42; s06-05 Mệnh đề 06.26 (cùng danh sách số hiệu mới trong ghi chú diễn giả). Deck không dẫn Ví dụ 06.17–06.19 hay Tình huống nào khác Tình huống 06.1, nên không có số Ví dụ hay Tình huống cần đổi.

**Quyết định cho từng phát hiện.** Mã: M = toán, E = chuyên gia, P = sư phạm, S = sinh viên, L = mạch. "sửa (A1)" nghĩa là sửa theo mục A1 của danh sách hợp nhất.

| Mã | Mức | Trang | Phát hiện | Quyết định và cách xử lý |
|---|---|---|---|---|
| M1 | nghiêm trọng | s01-08 | "AND, OR tăng $p_1-p_2$" sai với từng phép ghép riêng | sửa (A1): dòng viết bằng lời "AND rồi OR, hàm độc lập: cặp gần trùng xác suất gần 1, cặp xa gần 0"; ghi chú nêu từng phép ghép riêng không làm được |
| M2 | nghiêm trọng | s05-04, s05-06, s07-07 | độc lập của các phép thử vân tay là giả định riêng | sửa (A2): dòng Giả thiết trên s05-04, nhắc ở s05-06, s07-07; ghi chú: chỉ độc lập có điều kiện, số bỏ sót là cận dưới theo Jensen. Bác bỏ phần đề xuất đưa số mô phỏng $\approx2{,}2\%$: điều phối viên không dùng số mô phỏng |
| M3 | trung bình | s02-12 | chữ S cần $b\ge2$, $r\ge2$ | sửa (B7) trong ghi chú |
| M4 | trung bình | s04-07, s04-06, s06-02 | họ định nghĩa trên $\mathbb R^2$, ví dụ trên $\mathbb R^3$ | sửa (B7): hàm trên $\mathbb R^D$, $u$ đều trên mặt cầu; cận chỉ cho $D=2$; ví dụ ba điểm là hàm cố định trong $\mathbb R^3$ |
| M5 | trung bình | s07-01 | thiếu giá trị $s=0{,}9$ của $(5,50)$ | sửa (B8): $1-4{,}1\cdot10^{-20}$, làm tròn thành 1 |
| M6 | nhẹ | s04-11 | cận $1/3$ gắn thừa điều kiện dịch đều | sửa trong ghi chú |
| M7 | nhẹ | s04-09 | "tức" chỉ là kéo theo | sửa: "nên" |
| M8 | nhẹ | s04-02 | thiếu miền $0\le d_1<d_2\le D$ | sửa |
| M9 | nhẹ | s06-03 | gọi $0{,}1^{1/4}$ là ngưỡng | sửa: "xấp xỉ", thêm nghiệm một nửa $\approx0{,}509$ |
| M10 | nhẹ | s01-08, s02-07, s03-09, s04-12 | thiếu giả thiết trên mặt trang; trộn radian và độ | sửa: điều kiện độc lập trong ghi chú s01-08 và trên s06-01; "hữu hạn, không rỗng"; "mỗi hàm trùng với xác suất $p$"; "$2\pi/3$, tức $120^\circ$" |
| E1 | nghiêm trọng | s01-08, s03-09 | như M1 | sửa (A1); s03-09 Nhu cầu "cần hạ $p_2$ về gần 0", ghi chú nêu AND tăng tỷ số $2\to16$, giảm hiệu $0{,}4\to0{,}384$ |
| E2 | nghiêm trọng | mạch 4 | thiếu trang đặc tả và giả mã cho thuật toán tổng quát | sửa (A4): trang `lec06-s04-14`, Đầu vào, Đầu ra, giả mã 7 dòng, bảo đảm theo cặp (Mệnh đề 06.26), ghi chú nêu biến thể truy vấn cho Bài 07; s04-12 đổi nhãn "Quy tắc ước lượng." |
| E3 | nghiêm trọng | s02-13, s02-16 | mô hình chi phí bỏ qua nơi lưu tập gốc và bước 6 | sửa (A5): "tập gốc đã sắp xếp nằm trong bộ nhớ chính"; ghi chú: $2K$ lần đọc ngẫu nhiên nếu trên đĩa, bước 6 lọc theo $\widehat s$ đổi lại thêm bỏ sót |
| E4 | trung bình | s03-04 | điều kiện "trên các hướng" chỉ còn trong ghi chú | sửa (B9) |
| E5 | trung bình | s05-04, s07-07 | giả thiết độc lập không có trên mặt trang | sửa (A2); bác bỏ số $0{,}0216$ (số mô phỏng) |
| E6 | trung bình | s05-01 | OR trên ba hàm không nói là hàm cố định | sửa (B10) |
| E7 | trung bình | toàn deck | thiếu thuật ngữ tiếng Anh ở lần đầu | sửa (B11): locality-sensitive hashing, bucket (s01-01); band (s01-02); false negative (s01-04); candidate pair (s02-01); false positive (s02-05); S-curve (s02-12); cosine similarity (s03-04); edit distance, longest common subsequence (s03-05); locality-sensitive family (s03-07); hyperplane (s04-03); sketch (s04-04); isotropic (s04-05); entity resolution (s05-01); minutia (s05-02); stop word (s05-05). Thuật ngữ đã có ở mục tiêu hoặc tiêu đề mạch được chú giải ở trang định nghĩa khi trần âm tiết không cho phép, chẳng hạn "cặp ứng viên" |
| E8 | trung bình | s04-09, s06-02, s06-05 | bỏ §3.7.5 về nhiều chiều | sửa một phần: ghi chú s04-09 nêu lập luận định tính của §3.7.5; s06-02 ghi $\mathbb R^D$, bảo đảm khi $D=2$. Không phát biểu tính đơn điệu trong nhiều chiều như một kết quả vì ghi chú bài giảng không chứng minh |
| E9 | trung bình | s06-01, s02-16 | câu trả lời dựa trên giả định đầu ra $10^6$ cặp | sửa (A3) |
| E10 | trung bình | s01-08 | ký hiệu trước khi định nghĩa | sửa (B1) |
| E11 | trung bình | storyboard, các trang câu hỏi | thời gian làm câu hỏi trên lớp không thực tế | bác bỏ trong lượt này: tổng 120 phút và số câu giữ theo storyboard đã duyệt; mỗi trang câu hỏi có lời giải và tiêu chí trong ghi chú diễn giả để giảng viên chọn câu; điều phối viên không đưa mục này vào danh sách sửa |
| E12 | nhẹ | s04-02 | lệch MMDS về giới hạn $D$ hàm; thiếu $d_2\le D$ | sửa: ghi chú nêu giới hạn của MMDS, lấy có hoàn lại cho $p^r$, không hoàn lại thì không; miền trên mặt trang |
| E13 | nhẹ | s06-02 | $\mathbb R^2$ với $O(CmD)$; $\Sigma^D$ chưa định nghĩa | sửa |
| E14 | nhẹ | s02-12 | khuyến nghị theo xấp xỉ; nhãn SVG dấu chấm | sửa câu kết luận ($s_{1/2}\approx(1/b)^{1/r}$); hình giữ ngoại lệ đã ghi (B20), `img/` ngoài phạm vi ghi của lượt này |
| E15 | nhẹ | s03-05 | không phân biệt Levenshtein | sửa trong ghi chú |
| E16 | nhẹ | s04-12 | thiếu độ lệch chuẩn | sửa trong ghi chú: $\pi\sqrt{p(1-p)/m}$, khoảng $42^\circ$ với $m=3$ và góc thật |
| E17 | nhẹ | s01-03 | lặp phép tính của Bài 05 | bác bỏ: trang tính số của vấn đề trung tâm của bài này; ghi chú nói rõ vai trò |
| E18 | nhẹ | Bài 05/06/07 | thuật ngữ liên bài (LSH, vector/véc-tơ) | bác bỏ trong lượt này: quyết định cấp học phần, chuyển điều phối viên |
| E19 | nhẹ | ghi chú s01-07, s02-00, s03-00, s04-00, s05-00, s06-08, s01-08 | ngôn ngữ lập kế hoạch, câu chỉ đường | sửa |
| E20 | nhẹ | s01-04 | $\mathrm{SIG}$ trong đầu vào của bài toán | bác bỏ: bài toán được đặt sau Bài 05, chữ ký là dữ liệu đã có; đặc tả thuật toán ở s02-07 tách riêng |
| E21 | nhẹ | mạch 7 | không có dự phòng; không có MapReduce | bác bỏ phần dự phòng (D); ghi chú s07-00 nêu Bài 3.4.4 là đọc thêm |
| P1 | nghiêm trọng | s01-08, s03-09 | như M1 | sửa (A1) |
| P2 | trung bình | s02-01 | thiếu ví dụ dẫn nhập; "Ý nghĩa" thay trực giác | sửa (B12) |
| P3 | trung bình | s03-07 | định nghĩa trước ví dụ có số | sửa (B12): Nhu cầu mang số của MinHash |
| P4 | trung bình | s03-09, s03-10 | công thức trước ví dụ | sửa (B12) |
| P5 | trung bình | s04-03 | thiếu Nhu cầu | sửa (B12) |
| P6 | trung bình | s04-06, s04-07 | thiếu ví dụ cực đoan cho biên cố định | sửa: Nhu cầu s04-07 "hình chiếu $0{,}99$ và $1{,}01$ có mã thùng 0 và 1" |
| P7 | trung bình | s04-09 | phát biểu sau chứng minh | sửa (B12): "Định lý." đầu trang; không tách trang vì trang vừa khung và giữ 78 trang |
| P8 | trung bình | s05-01 | không có ví dụ chạy tay | bác bỏ thêm trang (số trang cố định 78 theo điều phối viên); chu trình rút gọn được ghi trong ghi chú diễn giả và storyboard; cặp hồ sơ cụ thể ở s05-06 |
| P9 | trung bình | s02-13, s04-10 | ký hiệu tiệm cận không có biểu thức đếm | sửa (B12) |
| P10 | trung bình | s01-05 | dùng $S_1$, $S_4$ trước khi nêu | sửa (B12): "Nhắc lại:" |
| P11 | trung bình | s01-08 | như E10 | sửa (B1) |
| P12 | trung bình | s06-01 | thiếu giả thiết từng dòng | sửa (A3) |
| P13 | trung bình | s06-05 | thiếu hàng mạch 4–5 | sửa (B3): 8 hàng bảng, trần 80 |
| P14 | trung bình | s02-12 | nhãn SVG dấu chấm; câu biên soạn trong ghi chú | sửa phần ghi chú (B20); hình giữ ngoại lệ |
| P15 | trung bình | s07-01 | như M5 | sửa (B8) |
| P16 | trung bình | s01-07, s06-08, s07-0x | viết tắt chưa viết đầy đủ | sửa: s01-07 tên đầy đủ và "(MMDS), ấn bản 3"; nguồn trang bài tập "MMDS"; HNSW, PQ ở s06-08 |
| P17 | trung bình | toàn deck | thuật ngữ tiếng Anh | sửa (như E7) |
| P18 | nhẹ | s02-11 | "Ý nghĩa" chứa con số | sửa: "Ví dụ." |
| P19 | nhẹ | s03-02 | "Ý nghĩa" không đọc kết quả | sửa: "Nhận xét." |
| P20 | nhẹ | s03-01 | $L_q$ dùng trước định nghĩa | sửa: viết bằng lời |
| P21 | nhẹ | s03-05 | công thức không thành mệnh đề | sửa |
| P22 | nhẹ | s02-10 | ví dụ sau công thức | sửa |
| P23 | nhẹ | s04-05 | phát biểu ở dòng Kết luận | bác bỏ: dòng Giả thiết đứng đầu, kết luận đánh số đứng cuối như mẫu trang kết quả có chứng minh ngắn; trần 6 dòng không cho thêm dòng Định lý |
| P24 | nhẹ | s03-11, s05-03, s05-07 | thiếu động từ yêu cầu | sửa s03-11, s05-07; bác bỏ s05-03 vì trần 6 dòng, nhiệm vụ nằm ở tiêu đề và bảng |
| P25 | nhẹ | s02-04 | cột "Mã" | sửa (B18) |
| P26 | nhẹ | s02-06 | hai câu kết luận | sửa |
| P27 | nhẹ | s01-03 | thiếu bước trung gian; kết luận | sửa |
| P28 | nhẹ | s05-06 | mục 1 là dữ kiện | sửa |
| P29 | nhẹ | s05-02, s05-05 | Nhu cầu không có số | bác bỏ: hai trang ở 60 và 56 âm tiết, thêm dòng số vượt trần 60; số Jaccard và lý do bỏ MinHash ở ghi chú diễn giả |
| P30 | nhẹ | s04-12 | nhãn "Thuật toán." chỉ có công thức | sửa: "Quy tắc ước lượng." |
| P31 | nhẹ | s04-01, s04-03 | hàm chỉ định nghĩa bằng dấu bằng | sửa: câu "là" |
| P32 | nhẹ | s06-01 | tiêu đề là cụm động từ | sửa |
| P33 | nhẹ | s07-00, s03-00 | nhãn không in đậm; "sáu cụm"; từ khóa gộp | sửa |
| P34 | nhẹ | s06-00 | ghi chú 103 âm tiết | sửa: 92 |
| P35 | nhẹ | ghi chú s01-07, s07-00, s06-08 | mở bằng tài liệu hoặc mạch làm chủ ngữ | sửa |
| P36 | nhẹ | ghi chú s01-03, s05-08, s01-08 | "bản soạn", câu chỉ đường | sửa |
| P37 | nhẹ | s06-08 | trích dẫn thiếu thông tin | sửa Datar và cộng sự (bốn tác giả, SoCG 2004); bác bỏ số trang chiếu CS246 vì outline chưa ghi số trang đã đối chiếu |
| P38 | nhẹ | ghi chú s01-01, s06-02 và nhiều trang | dấu hai chấm báo kịch tính; cặp khẩu hiệu; lặp "…, không phải …" | sửa (1), (2); (3) giảm ở s03-04, s04-06, giữ ở chỗ phân biệt hai đối tượng |
| S1 | trung bình | s06-08 | 64 âm tiết, vượt trần 60 | sửa (B17): trang nguồn theo trần 80, ngoại lệ ghi storyboard; hiện 65 |
| S2 | trung bình | s03-13, s05-04, s06-04 | dòng 21 âm tiết | sửa (B17) |
| S3 | trung bình | s01-08, s01-02 | ký hiệu trước định nghĩa | sửa (B1, B2) |
| S4 | trung bình | s02-04, s02-13, s04-06, s04-07 | "mã" hai nghĩa | sửa (B18): "mã tài liệu", "mã thùng" |
| S5 | trung bình | s02-09 | bất biến thiếu một chiều | sửa (B13) |
| S6 | trung bình | s03-03 | không phát biểu mệnh đề | sửa (B14) |
| S7 | trung bình | s03-07 | công thức ngắt giữa biểu thức; nhãn SVG nhỏ | sửa phần công thức (B15); nhãn SVG giữ, `img/` ngoài phạm vi ghi của lượt này, câu bên hình nêu cùng nội dung |
| S8 | trung bình | s04-09 | thứ tự đọc, công thức ngắt dòng | sửa (B15) |
| S9 | trung bình | s04-11 | câu 4 thiếu $a$ | sửa (B16) |
| S10 | trung bình | s06-02 | $\Sigma^D$ | sửa (B7) |
| S11 | nhẹ | 25 trang | trên mức đích 40 | ghi nhận; mọi trang trần 60 ≤ 60 |
| S12 | nhẹ | trang có bảng dữ liệu | 7 dòng | sửa: storyboard ghi quy ước hàng bảng |
| S13 | nhẹ | s02-08 | công thức ngắt trong thẻ | sửa |
| S14 | nhẹ | s02-07 | ký hiệu cắt lát | sửa trong ghi chú |
| S15 | nhẹ | s02-01 | "thùng" chưa định nghĩa trên mặt trang | bác bỏ: trang ở 59 âm tiết; "thùng (bucket)" có chú giải ở bìa, bảng s02-03 nêu tài liệu theo khóa |
| S16 | nhẹ | s01-06 | $V$ chỉ trong ghi chú | sửa |
| S17 | nhẹ | s02-11 | nhãn "Ý nghĩa" | sửa |
| S18 | nhẹ | s03-05 | công thức không ghi mệnh đề | sửa |
| S19 | nhẹ | s04-05 | ví dụ không nêu cặp | sửa |
| S20 | nhẹ | s04-06 | ký hiệu $x_1$ lẫn $z_i$ | sửa: viết bằng lời |
| S21 | nhẹ | s07-04 | tên A–D trùng $C$, $D$ | bác bỏ: tên theo đề sách, chữ đứng; ghi chú bài giảng có quy ước |
| S22 | nhẹ | s05-04 | $P_{\rm miss}$ | sửa: $1-P_T$ |
| S23 | nhẹ | s06-08 | nhãn "Đối chiếu"; HNSW, PQ | sửa |
| S24 | nhẹ | s01-05 | mục 3 là dữ kiện | sửa |
| S25 | nhẹ | s01-02 | ghi chú chứa ánh xạ điều phối | sửa |
| S26 | nhẹ | mạch 1 | chân trang ẩn do CSS chung | bác bỏ trong lượt này (D) |
| S27 | nhẹ | s03-00, s04-00, s07-00, s03-01, s07-06 | từ khóa xuống dòng, ngắt dòng mồ côi | sửa |
| S28 | nhẹ | s02-12 | dấu chấm thập phân của hình | giữ ngoại lệ (B20) |
| S29 | nhẹ | s06-00 | ghi chú 103 âm tiết | sửa |
| L1 | nghiêm trọng | s06-01 | thu hồi bằng giả định đầu ra | sửa (A3) |
| L2 | trung bình | s01-08 | ký hiệu chưa định nghĩa | sửa (B1) |
| L3 | trung bình | s01-08 ↔ s03-09–11 | lời hứa AND, OR mâu thuẫn ví dụ | sửa (A1); ghi chú s03-10 nêu từng phép ghép riêng không tăng độ chênh |
| L4 | trung bình | s01-08, s06-01 | dòng 6 ép khớp mạch | sửa: danh sách không đánh số theo mạch, dòng cuối là giới hạn chung; mạch 7 là recitation nên không có dòng riêng |
| L5 | trung bình | s06-01 | dòng 4–5 thiếu số và giả thiết | sửa (A3) |
| L6 | trung bình | s06-05 | thiếu hàng mạch 4–5 | sửa (B3) |
| L7 | trung bình | s06-00 | dòng dẫn hứa việc không làm | sửa (B4) |
| L8 | trung bình | s04-00 → s05-00 | mạch 4 không giao cho mạch 5 | sửa (B4): ghi chú s04-00, s05-00 nêu hai nhánh song song |
| L9 | trung bình | s03-08 → s03-10 | đổi ví dụ không báo | sửa (B5) |
| L10 | trung bình | s02-12, s06-03, s07-02, s01-02 | "ngưỡng" ba nghĩa | sửa (B6) |
| L11 | trung bình | storyboard | phiếu s06-01, s06-02, s01-05 lỗi thời | sửa (B19) |
| L12 | nhẹ | s03-00 | dòng dẫn trùng chức năng s04-00 | sửa |
| L13 | nhẹ | s02-06 → s02-02 | đổi dữ kiện đột ngột | sửa trong ghi chú s02-02 |
| L14 | nhẹ | s04-04 → s04-12 | "chữ ký dấu" dùng trước định nghĩa | sửa |
| L15 | nhẹ | s05-06 | câu hỏi tách khỏi nội dung | bác bỏ: giữ kiểu câu hỏi cuối mạch |
| L16 | nhẹ | s02-16, mạch 6 | lặp bộ số | bác bỏ: lặp do khuôn, mỗi trang có chức năng riêng |
| L17 | nhẹ | s06-02 | đầu vào $\mathbb R^2$ | sửa |
| L18 | nhẹ | toàn deck | $P$ nhiều nghĩa; $n$ và $m$; họ/hàm ba ô; $L_2$ Euclid | sửa: $\Pr[h(x)=h(y)]$ ở s06-05, $1-P_T$ ở s05-04; ghi chú s04-10, s04-12 nêu $m$ đóng vai $n$; "$L_2$ (Euclid)" ở s03-02; "họ" chỉ họ, "hàm" chỉ một hàm, đã nhất quán |
| L19 | nhẹ | s01-03 | ghi chú không nói tính số của trang trước | sửa |

**Mật độ sau sửa** (`density.py` của vai sinh viên, token có chữ hoặc chữ số; công thức, tiêu đề, giả mã, ô chỉ có số bị bỏ). 78 trang; 71 trang nội dung, trung vị 46 âm tiết, lớn nhất 79 (s01-02, trần 80); 0 trang trần 60 vượt 60; dòng dài nhất 20 âm tiết; tối đa 2 khối công thức và 1 khung nhấn mỗi trang; ghi chú diễn giả 65–150 âm tiết; ghi chú trang tiêu đề mạch 86–96 âm tiết; dòng dẫn trang tiêu đề mạch ≤ 24 âm tiết. Trang trần 80: s01-02 (79), s01-07 (56), s02-13 (67), s02-16 (41), s04-10 (76), s06-05 (78), s06-02 (74), s06-01 (73), s06-08 (65, ngoại lệ trang nguồn), bảy trang đề (29–77). Số âm tiết trước → sau của từng trang sửa ghi trong phiếu storyboard, dòng "Lượt sửa deck 2026-10-14 (năm báo cáo)".

**Kiểm tra đã chạy.**

- `git diff --check`: không lỗi. Kiểm HTML bằng `html.parser`: không thẻ lệch hay thiếu đóng; 78 `data-slide-id` duy nhất; 78 `id` duy nhất; 0 thuộc tính `style`, 0 khối `<style>`, 0 lớp `dense`.
- Playwright Chromium (`w06/deckcheck2.py`, máy chủ cổng 8771, `wait_until="load"`, tắt hiệu ứng chuyển trang, nhảy bằng `Reveal.getIndices` và `Reveal.slide(h,v,99)`), duyệt cả 78 trang ở 1600 × 900 và 390 × 844: 0 lỗi console (kể cả CSP), 0 phản hồi lỗi, 0 yêu cầu ra ngoài máy cục bộ, 0 `.katex-error`, không phần tử nào vượt khung `.slides` ở 1600 × 900, không công thức nội dòng nào bị ngắt giữa biểu thức (kiểm `getClientRects` của mọi `.katex` nội dòng; lượt đầu phát hiện s02-08, s03-04, s04-03, s06-01 và tràn ngang ở s03-07, đã sửa bằng cách bọc công thức và tách hai công thức của s03-07). `#/1`…`#/7` mở đúng trang tiêu đề mạch; phím Space đi qua đủ 78 trang theo thứ tự HTML.
- Ảnh chụp các trang sửa: `scratchpad/shots/deck06r-<id>-{wide,narrow}.png`, ghép xem tại `scratchpad/mont/r-*.png`; đã xem toàn bộ ảnh rộng. Lượt xem đầu thấy s04-03, s04-09 và s02-12 sát mép trên, mép dưới; đã thu hình, chuyển phần chứng minh xa sang cột hình và rút dòng đầu của s02-12. Ở 390 × 844, Reveal thu khung 16:9 như các bài trước; ảnh hẹp chụp ngay sau chuyển mạch đôi khi còn hiện trang trước do chế độ cuộn, không phải lỗi deck.

**Chưa làm.** Sinh lại SVG (`xac-suat-phan-dai.svg` dấu chấm thập phân, nhãn nhỏ của `mien-gan-xa.svg`) vì `img/lec-06/` ngoài phạm vi ghi của lượt này; sửa CSS chung về chân trang (D); thống nhất thuật ngữ liên bài (cấp học phần). Cần rà lại: độ chính xác của s04-14, s06-01, s05-04, s02-13; mạch của s01-08, s06-00 → s06-08 và hai trang lân cận mỗi phía, và mạch toàn deck vì câu trả lời vấn đề trung tâm thay đổi.

### Sửa nhỏ ghi chú theo lượt rà lại toán (2026-10-14)

Tác tử soạn thảo (fork, Opus 5.5, effort `high`) sửa `materials/lec-06/lecture-note.md` theo `recheck-note06-math.md` và chỉ đạo của điều phối viên. Deck không đổi. Chưa commit.

| Phát hiện | Quyết định | Cách xử lý |
|---|---|---|
| Lập luận Jensen bị dùng cho cả cấu trúc AND hai nhóm | sửa | Tình huống 06.2 (Giới hạn), gạch cuối "Giả thiết hay bị bỏ quên" ở Tóm tắt và lời giải Bài tập 06.28: Jensen chỉ áp cho cấu trúc OR, nơi $0{,}0150$ (OR 1024) và $0{,}000223559$ ($F_2$, OR 2048) là cận dưới của bỏ sót. Với AND hai nhóm, $t\mapsto[1-(1-t)^{1024}]^2$ không lồi cũng không lõm trên $[0,1]$ (lồi gần $0$, lõm gần $1$), nên ghi chú chỉ nói số của sách dựa trên giả định độc lập và không có bất đẳng thức một chiều. Không dùng số mô phỏng |
| Ví dụ 06.17: "25 lần" ngầm đọc "khác một chữ cái" là $d=1$ | sửa | Nêu cả hai trường hợp trong câu điều kiện: đọc là $d=1$ thì giảm $25$ lần; theo Định nghĩa 06.18 (chỉ chèn, xóa) một phép thay là $d=2$, giảm $25/4$ lần |
| Bài tập 06.29(b): mốc $s=0{,}3$ chưa giải thích | sửa | Ghi $s=0{,}3$ là cặp xa đại diện như Ví dụ 06.5 |

Kiểm tra: `w06/check.py` (172 khối khớp, số hiệu liên tục, 30 bài tập có gợi ý và lời giải), `w06/xref.py` (0 lỗi), trình xem cổng 8771 ở 1440 × 900 và 390 × 844 (172 khối, 0 `.katex-error`, không tràn ngang, in mở 76/76 khối gập), `git diff --check` không lỗi.

### Lượt sửa cuối sau hai lượt rà lại deck (2026-10-14)

Tác tử soạn thảo (fork, Opus 5.5, effort `high`, tác tử ghi duy nhất) sửa deck, `lecture-note.md`, `storyboard.md` và tệp này theo `recheck-deck06-math.md`, `recheck-deck06-storyline.md` và chỉ đạo của điều phối viên. Chưa commit.

**Tác động deck ↔ ghi chú.** Lượt sửa deck trước đổi kết luận dùng chung của vấn đề trung tâm (s06-01, theo A3) nhưng ghi chú bài giảng vẫn giữ kết luận cũ "bộ tạo trả $10^6$ cặp, giảm $5\cdot10^5$ lần" ở Tóm tắt chương. Lượt này sửa ghi chú cho khớp: thêm hai đoạn ngay sau đoạn "Trong thực hành" của Mệnh đề 06.13 (giả định ngoài $N$ cặp gần mọi cặp có $s\le0{,}1$; $P_{20,5}(0{,}1)\approx1{,}9998\cdot10^{-4}$; $\mathbb E[K]\le N+10^8$, $\mathbb E[Q]\le20N+10^8$, không cần các cặp độc lập; thời gian xác minh kỳ vọng không quá khoảng 100 giây với $1\,\mu\mathrm{s}$ mỗi lần so cặp của Ví dụ 06.1 và $N\ll10^8$, so với khoảng $5{,}79$ ngày) và viết lại đoạn 4 của Tóm tắt chương theo cùng số. Không thêm khối Ví dụ mới, nên không đổi số hiệu nào. Số $10^6$ cặp chỉ còn trong ghi chú diễn giả s06-01 như số liệu luyện tập. Ghi chú cũng thống nhất đơn vị $1\,\mu\mathrm{s}$ và nêu "chỉ số khoảng, trên trang chiếu gọi là mã thùng".

**Quyết định cho từng phát hiện.**

| Báo cáo | Mức | Trang | Phát hiện | Quyết định và cách xử lý |
|---|---|---|---|---|
| Toán | nhẹ | s06-01, s01-03 | `$1\,\mu s$` hiển thị s nghiêng | sửa: `$1\,\mu\mathrm{s}$` trên deck và trong ghi chú bài giảng |
| Toán | nhẹ | s06-01 | 100 giây là cận của kỳ vọng; ghi chú thiếu "không cần độc lập"; 1 µs cùng giả định | sửa: "thời gian xác minh kỳ vọng không quá khoảng 100 giây"; ghi chú dẫn Mệnh đề 06.13 và nêu cùng giả định với trang kho một triệu tài liệu |
| Toán | nhẹ | s06-01 dòng 3 | chi phí đọc như phụ thuộc $D=2$ | sửa: dòng 3 nêu bảo đảm và giả thiết của ba họ, chi phí $O(Cm)$, $O(CmD)$ tách riêng |
| Toán | nhẹ | ghi chú s03-10 | "; Từng" | sửa |
| Toán | nhẹ | ghi chú s06-08 | bài về nhà chồng bài trên lớp | sửa: về nhà 06.15–06.19, 06.26, 06.27, 06.29, 06.30; trên lớp 06.20–06.25, 06.28 |
| Mạch | nghiêm trọng (ngoài deck) | ghi chú, Tóm tắt chương | kết luận cũ $10^6$ cặp | sửa như mục tác động ở trên |
| Mạch | trung bình | s02-16 → s06-01 | $\mathbb E[K]$ chỉ có trong ghi chú diễn giả | sửa: công thức $\mathbb E[K]$, $\mathbb E[Q]$ (Mệnh đề 06.13) lên mặt s02-16, thay dòng bộ số bốn tập (chuyển vào ghi chú) |
| Mạch | trung bình | s06-01 dòng 3 | không có bảo đảm, câu khó đọc | sửa (như dòng toán ở trên) |
| Mạch | trung bình | s04-14 → s04-01, s04-10; s05-00, s05-04 | thuật toán tổng quát không được dùng lại; "hai nhánh song song" sai phạm vi | sửa: ghi chú s04-01 mở bằng câu nối; kết luận s04-10 "thùng, $Q$, $K$ như thuật toán tổng quát, $m=br$"; ghi chú s05-00, s05-04 nêu OR 1024 là thuật toán tổng quát với họ hàm ba ô, $r=1$, $b=1024$, còn AND hai nhóm OR lấy giao hai tập cặp; ghi chú s01-07, s04-00 nêu ba họ cơ sở song song với ứng dụng, ứng dụng dùng lại thuật toán tổng quát |
| Mạch | trung bình | storyboard s01-08, s06-05, s04-00 | trường chức năng lỗi thời | sửa |
| Mạch | nhẹ | s06-01 dòng 5–6 | thiếu công việc phát cặp, dựng thùng | sửa trong ghi chú: $\mathbb E[Q]\le20N+10^8$, dựng thùng $nC=10^8$ thao tác với $n=100$. Bác bỏ thêm "$t=0{,}8$" vào dòng 1: trang đã ở 76 âm tiết, dòng 1 nêu cặp $s=0{,}8$ của Ví dụ 3.12 |
| Mạch | nhẹ | s01-08 dòng cuối | giới hạn, chưa là câu trả lời có điều kiện | sửa: "Chưa giả thiết phân bố tương đồng: xấu nhất xét mọi cặp"; dòng 1–2 rút để giữ 60 âm tiết |
| Mạch | nhẹ | s06-01 dòng 4 | chỉ có vân tay, thiếu khóa thực thể và bản tin | bác bỏ: trần âm tiết; khóa thực thể có ở s06-05, bản tin không có bảo đảm riêng |
| Mạch | nhẹ | s06-05 → s06-01 | lặp bảo đảm của ba họ | bác bỏ: mỗi trang có chức năng riêng (L16) |
| Mạch | nhẹ | s04-14, s04-10, s06-02 | chỉ số $e$; $m=br$; "$Cbr$ hàm cộng phân dải" | sửa: ghi chú s04-14 giải thích $e$; s04-10 nêu $m=br$; s06-02 "$Cbr$ lần tính hàm, cộng phân dải" |
| Mạch | nhẹ | s05-01 → s05-02 | thiếu câu nối về họ ngẫu nhiên | sửa trong ghi chú s05-02 |
| Mạch | nhẹ | ghi chú s02-15, s07-06; ghi chú bài giảng Mục 4.3 | "mã" trơn; "mã thùng" và "chỉ số khoảng" | sửa: "mã tài liệu", "mã thùng" trong ghi chú diễn giả; ghi chú bài giảng nêu hai tên cùng một đại lượng |
| Mạch | nhẹ | ghi chú s03-10, s05-01 | dấu câu | sửa |
| Mạch | nhẹ | storyboard đầu tệp, bảng ánh xạ | tổng cũ 69, 77 trang; "năm câu trả lời"; hàng s06-05 thiếu số hiệu | sửa |

**Mật độ và kiểm tra.** `density.py` của vai sinh viên: 78 trang, 0 trang trần 60 vượt 60 (s01-08 đúng 60), dòng dài nhất 20 âm tiết, ghi chú diễn giả ≤ 150 âm tiết, ghi chú trang tiêu đề mạch ≤ 96. HTML cân bằng, 78 `data-slide-id` và 78 `id` duy nhất, 0 thuộc tính `style`. Playwright cổng 8771 duyệt cả 78 trang ở 1600 × 900 và 390 × 844, chụp s01-03, s01-08, s02-16, s04-01, s04-10, s04-14, s05-00, s05-04, s06-01, s06-02, s06-08 (đã xem ảnh rộng s01-08, s02-16, s06-01): 0 lỗi console, 0 `.katex-error`, không tràn khung, không công thức nội dòng ngắt dòng, `#/1–7` đúng, phím Space đủ 78 trang. Ghi chú bài giảng: `w06/check.py` (172 khối, số hiệu liên tục), `w06/xref.py` 0 lỗi, trình xem 172 khối, 0 `.katex-error`, không tràn, in mở 76/76. `git diff --check` không lỗi.

## Ghi nhận của điều phối viên về đợt căn chỉnh 2026-10-14

**Mô hình và tác tử (bằng chứng từ lời gọi công cụ `Agent`, không phải lời tự khai).** Phiên điều phối chạy Claude Fable 5.1. Tác tử phân tích nguồn văn phong (MAT1101, giáo trình Học máy thống kê) là loại `fork`, kế thừa mô hình Fable 5.1 của điều phối viên; đây là tác tử duy nhất không chạy Opus 5.5, được giao trước khi quy ước mô hình của dự án được cập nhật và chỉ làm việc đọc nguồn ngoài kho. Mọi tác tử còn lại được tạo bằng `Agent` với `subagent_type: "general-purpose"`, `model: "opus"` (Claude Opus 5.5), `effort: "high"`: lập kế hoạch (chỉ đọc); soạn thảo (một tác tử, tiếp tục bằng `SendMessage` qua các lượt: ghi chú, deck, sửa ghi chú, sửa deck, sửa cuối); rà ghi chú (toán; mạch viết và chuẩn giáo trình kiêm góc nhìn sinh viên và no-ai-slop Detect); rà deck năm vai (sinh viên kèm đo mật độ; chuyên gia giải thuật và khoa học dữ liệu; độ chính xác toán học; phản biện học thuật kèm no-ai-slop Detect; kết nối và mạch viết); rà lại toán ghi chú; rà lại toán deck; rà lại mạch deck. Các mục trên trong tệp này ghi tác tử soạn là `fork` là ghi nhầm của chính tác tử; loại thực tế là `general-purpose` Opus 5.5 `high`.

**Quyết định của điều phối viên.** Chấp nhận kế hoạch `plan-lec06.md` với các quyết định đã ghi ở đầu mục "Căn chỉnh văn phong 2026-10-14"; quyết định 2 (thu hồi bằng giả định $10^6$ cặp) được thay sau lượt rà mạch deck bằng kết luận suy từ Mệnh đề 06.13 (giả định ngoài $N$ cặp gần mọi cặp có $s\le0{,}1$; $\mathbb E[K]\le N+10^8$; xác minh kỳ vọng không quá khoảng 100 giây), điều phối viên đã tính lại: $1-(1-10^{-5})^{20}=1{,}9998\cdot10^{-4}$, $5\cdot10^{11}\cdot2\cdot10^{-4}=10^8$, $20\cdot5\cdot10^{11}\cdot10^{-5}=10^8$. Chấp nhận ngoại lệ độ dài ghi chú: 30 799 từ theo khoảng trắng, vượt khoảng 8 000–20 000 của `AGENTS.md`; lý do: tiếng Việt đếm theo âm tiết, ghi chú mẫu Bài 05 của `../rl-plan` có 26 226 từ theo cùng cách đếm, phần Bài tập củng cố gồm 30 bài có lời giải (trong đó 7 bài sách của recitation) chiếm khoảng 2 500 từ. Mọi đầu ra của tác tử đều được điều phối viên đọc báo cáo, đối chiếu một phần với tệp và chấp nhận; các phát hiện bị bác bỏ có lý do trong các mục trên.

**Kiểm định cuối do điều phối viên tự chạy (máy chủ `python3 -m reloadserver 8771` tại gốc kho; cổng 8765 và 8766 đang do `../math-4-AI` và `../rl-plan` chiếm).** `git diff --check` sạch. Deck: 78 `data-slide-id` duy nhất; 7 `<section>` ngoài; 6 trang tiêu đề mạch `id="mach-2"`…`mach-7`; không `<style>`, `style=`, `.dense`, `fragment`; `density.py`: 71 trang nội dung, trung vị 45 âm tiết, lớn nhất 79, 7 trang trên 60 đều thuộc nhóm trần 80 có ngoại lệ trong storyboard (s01-02, s02-13, s04-10, s06-05, s06-02, s06-01, s07-07). Playwright Chromium 1600×900 và 390×844 trên s01-01, s01-08, s02-00, s02-16, s03-00, s04-00, s04-10, s04-14, s05-00, s06-00, s06-01, s06-05, s07-00: 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; đã xem ảnh s01-08, s02-16, s04-14, s06-01, s06-05 (hẹp), các trang tiêu đề mạch. Ghi chú trong viewer: 172 khối `.material-block` khớp 172 khối `:::`, 0 `.katex-error`, không tràn ngang ở hai cỡ, khối gập mở được bằng bàn phím (Enter trên `summary`), viewer mở khối khi in qua `beforeprint`. Bài 02 và 03 mở không lỗi console sau khi thêm `.strand-title` vào CSS chung. `index.html` đã có liên kết ghi chú Bài 06, không đổi.

**Phạm vi commit.** Hai commit: ghi chú (`lecture-note.md`, `material-viewer.js`, `material-viewer.css`, `materials/_templates/lecture-note.md`) và deck (deck HTML, `lecture-style.css`, `lecture-template.html`, ba tệp planning). `AGENTS.md`, `CLAUDE.md`, `slide_authoring_standard.md`, `.gitignore` không được commit trong đợt này vì quy ước chỉ commit tệp quy định khi người dùng yêu cầu và vì `AGENTS.md` còn chứa thay đổi chưa commit của người dùng từ trước phiên.

**Giới hạn còn lại.** Hai SVG (`xac-suat-phan-dai.svg` dấu chấm thập phân, `mien-gan-xa.svg` nhãn nhỏ) giữ ngoại lệ cũ; CSS chung ẩn chân trang ở các trang mạch 1 (ảnh hưởng mọi deck, cần đợt sửa riêng); thuật ngữ liên bài ("băm nhạy cảm cục bộ" ở Bài 05, "véc-tơ" ở Bài 07) chưa thống nhất.
