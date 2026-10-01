# Storyboard Bài 06: Tìm cặp tương đồng bằng LSH

Bản viết mới ngày 28-09-2026, đã được gate độc lập PASS và điều phối viên chấp nhận trước triển khai. Chỉ dùng sườn MMDS 3e §§3.4–3.8 và các quyết định đã duyệt trong `outline.md`. Các mã trang và chủ đề chỉ phục vụ quy trình, không hiển thị trên mặt slide hoặc trong ghi chú diễn giả. Các đoạn “Nội dung công khai” là dự kiến mặt trang; đoạn “Diễn giải học thuật” định hướng nội dung notes, không chứa hướng dẫn giảng viên. Bố cục và phút là thông tin nội bộ.

## Bản đồ hành trình và chu trình cụm

| Cụm, phần và chức năng | Tình huống, đầu vào, sản phẩm | Tám bước và mã trang | Câu nối, bước gộp và giới hạn | Phút |
|---|---|---|---|---:|
| A, phần 1: thiết lập bài toán | Triệu tài liệu; SIG 250 thành phần,1 GB; gần $5\cdot10^{11}$ cặp. Tiên quyết MinHash → nhu cầu tạo ứng viên | Tình huống/vấn đề s01-03; nhắc kết quả và đặc tả nhu cầu s01-04; kiểm tra s01-05 | Chữ ký giảm chi phí mỗi cặp; số cặp cần một cơ chế khác. Không có thuật toán mới ở phần mở. Quy mô được thu hồi s02-13 và s06-01/02 | 8 |
| B, phần 2: phân dải | V02 giữ cùng SIG, tập và $t=2/3$; V03 làm rõ AND nhiều hàng. Đầu ra là $\mathcal C$, kết quả sau kiểm và mô hình sai số/chi phí | Tình huống kế thừa A; vấn đề/trực giác s02-01; vết chạy s02-02–06; đặc tả s02-07; thuật toán s02-08; đúng/biên s02-09; xác suất s02-10–12; chi phí/ứng dụng s02-13; kiểm tra s02-14 | V02 truyền tuple, khóa, cặp 14 lặp vào giả mã, bất biến,$Q,K$. V03 chỉ bổ sung trực giác $r=3$, không thay dữ kiện V02. Công thức sau thao tác; kiểm gốc chỉ xét ứng viên | 32 |
| C, phần 3: độ đo và họ | Kết quả LSH cho tập chưa xác định “gần” ở vector/chuỗi. V05–08 → miền/độ đo → họ tổng quát | Nhu cầu/trực giác/ví dụ chuẩn s03-01; hình thức chuẩn/metric s03-02; ví dụ và tính chất các độ đo s03-03–06; họ s03-07–08; AND/OR với chứng minh s03-09–10; vận dụng s03-11; cơ chế/chi phí s03-12; kiểm tra s03-13 | Độ đo phụ dùng chu trình rút gọn định nghĩa–tính–giới hạn, không giả mã riêng. Chứng minh Jaccard dùng bao hàm sự kiện trên slide, đầy đủ trong notes. Phép ghép dùng lại dải thay vì thêm miền ví dụ | 30 |
| D 1, phần 4: Hamming | V08, vector cùng chiều; chọn tọa độ rẻ → phép thử gần–xa | Vấn đề/trực giác/ví dụ s04-01; định nghĩa/chứng minh s04-02; ứng dụng/chi phí s04-10; kiểm tra s04-11 | Một phép thử đọc 1 tọa độ. Phép ghép độc lập lấy chỉ số đều có hoàn lại; không giới hạn số mẫu bằng số hàm phân biệt | 4 |
| D 2, phần 4: góc | V10, tích vô hướng; cần dùng hướng thay độ dài → bit dấu và xác suất | Trực giác/vết chạy s04-03–04; hình thức/lập luận góc s04-05; thuật toán lấy nhiều dấu hiện trong s04-04; chi phí s04-10; kiểm s04-11 | Đổi từ 3 pháp tuyến dấu cố định sang mô hình đẳng hướng phải nêu rõ. Góc thật và ước lượng khác nhau do mẫu và phân phối. Dấu 0 quy ước cố định | 8 |
| D 3, phần 4: Euclid | Điểm gần về độ dài, phép chiếu có thể qua biên; V11 trục 1, a=1 → mã khoảng | Vấn đề/trực giác/vết chạy s04-06; đặc tả s04-07; va chạm theo dịch s04-08; cận/đúng s04-09; ứng dụng/chi phí s04-10; kiểm s04-11 | Hướng đơn vị và dịch đều là ngẫu nhiên của họ; trục cố định V11 chỉ minh họa thao tác. Cận số chỉ hai chiều; chi tiết lượng tử hóa tiếp nhận Datar, proof bản soạn | 14 |
| E 1, phần 5: thực thể | Hai bảng mỗi bảng 1 triệu hồ sơ, tên/địa chỉ/điện thoại → hợp cặp rồi chấm điểm | Tình huống, vấn đề, trực giác, quy tắc/xác minh và giới hạn s05-01; kiểm s05-06 | Không có mô hình phân phối để gán họ 4 tham số. Không có dữ liệu hồ sơ cụ thể để tự tạo vết số; dùng đúng trường và quy mô nguồn. Phép hợp dùng lại thuật toán đã học | 3 |
| E 2, phần 5: vân tay | Ảnh đã chuẩn hóa thành tập ô; V12 → mô hình va chạm và ghép | Vấn đề/trực giác/đặc tả s05-02; ví dụ và phép tính cơ sở s05-03; ghép, chi phí/sai số s05-04; kiểm s05-06 và R6 | Định nghĩa thùng chung và singleton trước xác suất. Dữ kiện 0.2/0.8 là mô hình; giữ giả thiết độc lập. Thuật toán ghép và proof đã có ở C, không lặp đầy đủ | 8.5 |
| E 3, phần 5: bản tin | Cùng bài báo có phần bao quanh khác; token Ex 3.24 → shingle theo từ dừng | Tình huống, vấn đề, trực giác, vết token, quy tắc và giới hạn s05-05; kiểm s05-06 | Dùng tập đặc trưng mới với quy trình N02; không làm định lý hiệu năng. Cơ chế shingle đã học Bài 05; không lặp thuật toán MinHash | 4.5 |
| F, phần 6: thu hồi | Đầu ra toàn bài → quyết định biểu diễn, họ, tham số, xác minh và giới hạn | Tình huống/ứng dụng s06-01; tổng chi phí/sai số s06-02;6 nhiệm vụ s06-03/04 | Không đưa khái niệm mới. Câu nối Bài 07 chỉ nêu so sánh chỉ mục theo chất lượng/thời gian/bộ nhớ | 8 |
| R, phần 7: vận dụng nguồn | Sáu cụm bài đã học → bảng, biểu thức, chữ ký, thùng, sai số | s07-01–07; Bài 3.8.2 là kiểm tra tổng hợp | R1 chia 2 trang, thời gian tính một lần 18 phút. Các bước ngắn chỉ phân chia đề gốc, không đổi yêu cầu | 60 |

Các phút D 1+D 2+D 3=26 và E 1+E 2+E 3=16 bao gồm phần chia sẻ chi phí/kiểm tra; chúng không cộng thêm ngoài bảng phần. Mọi thuật toán cơ sở dừng sau số tọa độ/phép thử hữu hạn. Phép băm cơ sở khác nhau nhưng cùng dùng khung ghép, thùng, ứng viên và xác minh.

## Quy tắc thể hiện và giới hạn chung

Dùng hệ lớp của `lecture-style.css`: trang tiêu đề/mục lục như Lecture 02, `example-slide`, `ex-grid2`, `ex-card`, `ex-equation`, `ex-table`, `ex-code`, `ex-note`, `ex-source`, và `cost-slide`. Tỷ lệ các vùng dưới đây là quyết định bố cục, không là chỉ dẫn giảm cỡ chữ. Bảng là HTML, công thức là KaTeX, giả mã là `pre/code` có `data-trim`; sơ đồ và hình học dùng SVG vẽ lại. Không dùng `fragment`.

Mỗi phiếu chỉ định một trọng tâm và thứ tự đọc. Dữ kiện/giả thiết quyết định kết luận hiện trên mặt trang. Ghi chú mở rộng chứng minh, biên, lỗi và nguồn. Nếu nội dung vượt khung ở pha 2, tách trang và quay lại gate cho phạm vi thay đổi cùng hai trang lân cận; không giảm thang chữ. Những dữ kiện dùng chung viện dẫn V01–V12 trong outline; phiếu vẫn nêu giá trị cần quan sát. Không dùng màu làm dấu phân biệt duy nhất.

## Phiếu từng trang

### Phần 1. Bài toán tìm cặp tương đồng

#### lec06-s01-01 — Tìm cặp tương đồng bằng LSH

- **Mục đích và vai trò:** Định vị bài trong mạch biểu diễn và tìm cặp.
- **Thông điệp:** Bài học xây cơ chế chọn cặp sau khi đã có chữ ký.
- **Nội dung công khai dự kiến:** Tên bài; tên học phần; học kỳ 1, năm học 2026–2027; “Băm nhạy cảm theo tính cục bộ (LSH)”.
- **Đầu vào và giả thiết:** Bài 05 đã cung cấp chữ ký MinHash.
- **Dữ kiện, hình thức hóa và vết chạy:** Không có ví dụ số; tên và số bài theo source.md.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Tiêu đề lớn ở giữa trên; học phần và học kỳ phía dưới theo title-slide. Một cụm tên giúp sinh viên năm 2 nhận nhiệm vụ mới; không thêm công thức hay mục tiêu dài.
- **Kết nối vào–ra:** Nhận kết quả Bài 05; trang nội dung xác định những thành phần của quy trình cần xây.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chữ ký là đầu vào của bước chọn cặp. Việc biểu diễn từng tài liệu đã được giải quyết ở Bài 05; bài này xét việc tổ chức phép so giữa nhiều tài liệu.
- **Nguồn:** sources/source.md, bảng Thứ tự đề xuất, dòng 6; B §3.4 tr.91–92/PDF 20–21.
- **Ánh xạ ghi chú:** `N01`. **Thời lượng:** 0.5 phút.

#### lec06-s01-02 — Nội dung và mục tiêu

- **Mục đích và vai trò:** Nhận diện thứ tự bảy phần và ba năng lực quan sát được của bài học.
- **Thông điệp:** Tạo và xác minh tập ứng viên, tính xác suất để chọn tham số, và chọn họ băm theo độ đo là ba đầu ra học tập.
- **Nội dung công khai dự kiến:** Bài toán tìm cặp tương đồng Phân dải chữ ký MinHash Khoảng cách và họ nhạy cảm Các họ băm theo độ đo Ứng dụng tìm cặp tương đồng Tổng kết và tự kiểm tra Bài tập vận dụng Mục tiêu học tập Tạo và xác minh tập cặp ứng viên bằng phân dải chữ ký. Tính xác suất một cặp thành ứng viên; chọn số dải và số hàng. Chọn họ băm phù hợp với độ đo khoảng cách.
- **Đầu vào và giả thiết:** Tên bài và chữ ký.
- **Dữ kiện, hình thức hóa và vết chạy:** Không áp dụng ví dụ số.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai vùng: danh mục bảy phần 60% bên trái; ba mục tiêu 40% bên phải. Tiêu đề và mục lục giữ cỡ chữ agenda-slide; mục tiêu dùng cỡ chữ nội dung của example-slide. CSS chỉ chia lưới, không đổi font. Đọc mục tiêu rồi liên hệ từng phần; ba mục tiêu gộp MT1–MT6, được kiểm ở phần kết.
- **Kết nối vào–ra:** Chữ ký Bài 05 → ba sản phẩm học tập; số cặp của kho triệu tài liệu tạo nhu cầu đầu tiên. Kết bài s06-03/04 kiểm lại ba năng lực.
- **Diễn giải học thuật, lời giải và tiêu chí:** Phần 1 đặt bài toán: sau khi có chữ ký, số cặp vẫn tăng bậc hai. Phần 2 chia chữ ký thành dải để sinh cặp ứng viên, xác minh chúng, rồi tính xác suất và chi phí. Phần 3 và 4 mở rộng cách làm từ Jaccard sang các độ đo khác qua khái niệm họ băm nhạy cảm. Phần 5 áp dụng vào ba bài toán của sách. Ba mục tiêu được kiểm ở các trang câu hỏi cuối mỗi phần và ở phần tổng kết.
- **Nguồn:** B § §3.4–3.8 tr.91–122; outline mục 5.
- **Ánh xạ ghi chú:** `N01`. **Thời lượng:** 1 phút.

#### lec06-s01-03 — Số cặp sau khi tạo chữ ký

- **Mục đích và vai trò:** Tính riêng dung lượng chữ ký và số phép so cặp.
- **Thông điệp:** Dung lượng chữ ký tuyến tính không làm số cặp mất bậc hai.
- **Nội dung công khai dự kiến:** $C=10^6$, $n=250$,4 byte/thành phần: dung lượng $10^9$ byte. Số cặp $\binom C2=499999500000$. Với giả định $1\,\mu s$/cặp: khoảng 5.79 ngày.
- **Đầu vào và giả thiết:** Tổ hợp chập 2; byte và đơn vị thời gian.
- **Dữ kiện, hình thức hóa và vết chạy:** V01; $10^6\cdot250\cdot4$; $499999500000\cdot10^{-6}/86400=5.78703125$. Giả định thời gian, không phép đo.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 45% là phép tính dung lượng; phải 55% là số cặp và thời gian. Đọc cùng $C$ trên hai nhánh. Năm 2 cần tách hai đại lượng có đơn vị khác; diễn giải thời gian chi tiết vào notes.
- **Kết nối vào–ra:** Bản đồ mục 1→giới hạn số cặp; giới hạn dẫn tới đặc tả chỉ tìm cặp đạt ngưỡng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Ví dụ 3.10 là phép tính minh họa của sách. Nếu bài toán yêu cầu xuất độ tương đồng của mọi cặp thì kích thước đầu ra đã là bậc hai. Nhu cầu ở đây chỉ gồm những cặp đủ tương đồng.
- **Nguồn:** B Ex 3.10 tr.92/PDF 21; M PDF 24; S3 PDF 10–14.
- **Ánh xạ ghi chú:** `N01`. **Thời lượng:** 2 phút.

#### lec06-s01-04 — Đầu vào và cặp cần tìm

- **Mục đích và vai trò:** Nêu dữ liệu đã có và tiêu chuẩn chấp nhận cặp.
- **Thông điệp:** Bộ tạo ứng viên giảm phạm vi xác minh nhưng có thể bỏ sót cặp đạt ngưỡng.
- **Nội dung công khai dự kiến:** $S_1,\ldots,S_C$ là các tập đặc trưng hữu hạn không rỗng; $\mathrm{SIG}\in V^{n\times C}$; $s=\mathrm{SIM}(S_c,S_d)$, ngưỡng $t\in[0,1]$. Đích: các cặp $c<d$ có $s\ge t$. Sơ đồ SIG→ứng viên→Jaccard gốc. Nhắc $\Pr[h(S_c)=h(S_d)]=s$ với tập không rỗng và hoán vị đều.
- **Đầu vào và giả thiết:** Jaccard, MinHash Bài 05; cùng phép thử theo hàng.
- **Dữ kiện, hình thức hóa và vết chạy:** Ký hiệu $C,n,\mathrm{SIG},s,\widehat s$ giữ Bài 05. Chưa dùng $b,r$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ lớn ngang phía trên 60%; hợp đồng đầu vào và ngưỡng ở dưới 40%. Năm 2 theo đối tượng đi qua từng bước trước xác suất; không nhét chứng minh MinHash vào mặt trang.
- **Kết nối vào–ra:** Số cặp quá lớn→cặp cần tìm; kiểm tra mở đầu xác nhận phần chi phí còn thiếu.
- **Diễn giải học thuật, lời giải và tiêu chí:** $s$ được tính trên tập gốc; $\widehat s$ là tỷ lệ trùng của một chữ ký đã lấy. Hai đại lượng khác nhau. Xác minh Jaccard cho một cặp là quyết định xác định, còn việc cặp ấy được đưa vào tập ứng viên phụ thuộc các phép thử.
- **Nguồn:** B §3.4 tr.91–92, §3.4.3 tr.95–96; P5, commit 5530bd6, đoạn ký hiệu.
- **Ánh xạ ghi chú:** `N01`. **Thời lượng:** 2.5 phút.

#### lec06-s01-05 — Kiểm tra bài toán tìm cặp

- **Mục đích và vai trò:** Phân biệt giảm kích thước từng đối tượng với giảm số cặp.
- **Thông điệp:** Cần chọn cặp trước bước xác minh chính xác.
- **Nội dung công khai dự kiến:** Câu hỏi: Với $10^6$ tài liệu và chữ ký 250 thành phần, 4 byte/thành phần, tính dung lượng chữ ký. Tính số cặp không thứ tự. Chữ ký ngắn đã loại được giới hạn này chưa? Phân biệt Jaccard thật $s$ và tỷ lệ trùng chữ ký $\widehat s$.
- **Đầu vào và giả thiết:** V01 và hợp đồng s01-04.
- **Dữ kiện, hình thức hóa và vết chạy:** Dữ kiện nguồn giữ nguyên; không yêu cầu công thức LSH chưa học.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Một khối nhiệm vụ với ba yêu cầu đánh số: dung lượng, số cặp, phân biệt s và tỷ lệ chữ ký. Giữ dữ kiện triệu tài liệu; đáp án trong notes. Ba yêu cầu xác nhận tiên quyết trước phân dải.
- **Kết nối vào–ra:** Hợp đồng→tự kiểm; nhu cầu tập ứng viên dẫn vào phân dải.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: dung lượng chữ ký là $10^6\cdot250\cdot4=10^9$ byte. Số cặp vẫn là $\binom{10^6}{2}=499999500000$; chữ ký ngắn giảm dữ liệu mỗi cặp nhưng chưa giảm số cặp. $s$ là Jaccard tính trên tập gốc; $\widehat s$ là tỷ lệ thành phần trùng của chữ ký quan sát được, nên phụ thuộc các phép thử đã lấy. Tiêu chí: phân biệt dung lượng với số cặp và phân biệt tương đồng thật với ước lượng.
- **Nguồn:** B Ex 3.10/ §3.4 tr.91–92; câu kiểm tra trực tiếp dữ kiện nguồn.
- **Ánh xạ ghi chú:** `N01`. **Thời lượng:** 2 phút.

### Phần 2. Phân dải chữ ký MinHash

#### lec06-s02-01 — Phân dải chữ ký

- **Mục đích và vai trò:** Mô tả quy tắc đưa hai cột vào cùng nhóm.
- **Thông điệp:** Trùng toàn bộ một dải đủ để tạo một cặp ứng viên.
- **Nội dung công khai dự kiến:** Chia $n=br$ hàng thành $b$ dải. Hai cột trùng một dải khi cả $r$ thành phần của dải đều trùng. Chung ít nhất một dải → cặp ứng viên. Mỗi dải cho một bộ $r$ giá trị có thứ tự (tuple); so trong cùng dải, rồi hợp cặp.
- **Đầu vào và giả thiết:** SIG và nhu cầu ứng viên.
- **Dữ kiện, hình thức hóa và vết chạy:** HT1 trực giác; chưa áp công thức xác suất.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** SVG chữ ký với ngoặc dải ở trái 60%, hai câu quy tắc ở phải 40%. Năm 2 thấy AND trong dải và OR giữa dải bằng quan hệ nhóm; ký hiệu đặt cạnh ngoặc.
- **Kết nối vào–ra:** Ứng viên cần được tạo→nhóm các đoạn bằng nhau; SIG nhỏ cho phép chạy từng bước.
- **Diễn giải học thuật, lời giải và tiêu chí:** Mỗi dải là một phép thử khác. Cùng tuple ở hai vị trí dải khác nhau không phải cùng khóa. So bằng tuple là phép kiểm rẻ hơn việc đọc hai tập gốc lớn.
- **Nguồn:** B §3.4.1 tr.92–93/PDF 21–22; M PDF 44–46.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 1 phút.

#### lec06-s02-02 — Chữ ký của bốn tập

- **Mục đích và vai trò:** Đọc đúng hàng, cột và tham số của vết chạy.
- **Thông điệp:** Cùng dữ kiện tập gốc và chữ ký cho phép kiểm kết quả sau phân dải.
- **Nội dung công khai dự kiến:** Dữ kiện: $S_1=\{a,d\},S_2=\{c\},S_3=\{b,d,e\},S_4=\{a,c,d\}$. SIG hai hàng $(1,3,0,1)$,$(0,2,0,0)$. $b=2,r=1,t=2/3$.
- **Đầu vào và giả thiết:** Ký hiệu từ s01-04 và quy tắc dải.
- **Dữ kiện, hình thức hóa và vết chạy:** V02; các số 1,3,0,1 là giá trị chữ ký, cột 1–4 là mã tài liệu. Phân dải là phép áp dụng mới đã duyệt.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng tập gốc ở trái 45%; ma trận có nhãn cột/hàng/dải ở phải 55%. Giữ vị trí ma trận ở hai trang sau. Năm 2 đọc đồng thời đối tượng và biểu diễn; không lặp cách tính MinHash.
- **Kết nối vào–ra:** Quy tắc nhóm→đầu vào cụ thể; dải 1 là bước cập nhật đầu tiên.
- **Diễn giải học thuật, lời giải và tiêu chí:** Các chữ ký thuộc Ví dụ 3.8 của sách. Hai hàm cố định chỉ dùng chạy thuật toán; định lý xác suất ở phần sau xét mô hình hoán vị đều độc lập. Với một hàng mỗi dải, tuple có một thành phần.
- **Nguồn:** B Ex 3.8 tr.85–86/PDF 14–15; áp dụng §3.4.1 tr.92–93; P5, commit 5530bd6.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-03 — Thùng của dải thứ nhất

- **Mục đích và vai trò:** Chèn bốn mã tài liệu theo khóa dải đầu.
- **Thông điệp:** Khóa đầy đủ giữ đúng nhóm trong một dải.
- **Nội dung công khai dự kiến:** Dải 1 có $(1,3,0,1)$. Bảng:$(1,(1))\mapsto[1,4]$;$(1,(3))\mapsto[2]$;$(1,(0))\mapsto[3]$. Cặp phát:$(1,4)$.
- **Đầu vào và giả thiết:** V02, tuple một thành phần.
- **Dữ kiện, hình thức hóa và vết chạy:** Khởi tạo thùng rỗng; chèn 1→thùng 1: [1]; chèn 4→thùng 1: [1,4]; thùng đơn không phát cặp.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ma trận cố định trái 45%; bảng khóa/danh sách/cặp phải 55%. Mũi tên nhãn “chèn 4” nối ô 1 với danh sách[1,4]. Năm 2 theo được một thao tác và phần giữ nguyên; lịch chèn đủ ở notes.
- **Kết nối vào–ra:** Đầu vào→nhóm dải 1; dải 2 dùng cùng phép chèn nhưng không chung miền khóa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Sau bốn lượt chèn, mỗi tài liệu xuất hiện đúng một lần trong thùng của nó ở dải 1. Chỉ một thùng có hai phần tử nên chỉ phát cặp (1,4). Mã dải là một thành phần của khóa, khác giá trị chữ ký 1.
- **Nguồn:** B §3.4.1 tr.92–93 trên dữ kiện Ex 3.8; V02.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-04 — Hợp các cặp qua hai dải

- **Mục đích và vai trò:** Phát cặp dải 2 và khử lặp qua các dải.
- **Thông điệp:** Tổng lượt phát cặp có thể lớn hơn số ứng viên duy nhất.
- **Nội dung công khai dự kiến:** Dải 2:$(2,(0))\mapsto[1,3,4]$;$(2,(2))\mapsto[2]$. Phát $(1,3),(1,4),(3,4)$. Hợp với dải 1:$\mathcal C=\{(1,3),(1,4),(3,4)\}$;$Q=4,K=3$.
- **Đầu vào và giả thiết:** Thùng dải 1; mọi cặp không thứ tự trong danh sách.
- **Dữ kiện, hình thức hóa và vết chạy:** V02;$\binom32=3$; cặp 14 được phát ở cả hai dải.8 lượt chèn cho toàn vết chạy.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ma trận trái 45% giữ nguyên; bảng dải 2 và dòng hợp cặp phải 55%. Cặp 14 lặp có nhãn “đã có”. Năm 2 phân biệt lượt xử lý và phần tử của tập; không chỉ dùng màu.
- **Kết nối vào–ra:** Nhóm dải 1→nhiều dải; tập đã khử lặp là đầu vào xác minh.
- **Diễn giải học thuật, lời giải và tiêu chí:** $Q$ đếm lượt trước khử lặp; $K$ đếm cặp phân biệt. Một cặp được sinh nhiều lần vẫn chỉ xác minh một lần khi lưu trong tập. Khóa có số dải nên giá trị 0 ở dải 1 không tự ghép với 0 ở dải 2.
- **Nguồn:** B §3.4.1, 3.4.3 tr.92–96; áp dụng V02.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-05 — Xác minh bằng Jaccard gốc

- **Mục đích và vai trò:** Tính Jaccard cho ba ứng viên và chọn kết quả.
- **Thông điệp:** Xác minh loại cặp dưới ngưỡng trong tập ứng viên.
- **Nội dung công khai dự kiến:** $t=2/3$. Bảng: cặp $(1,3)$ có giao $\{d\}$, hợp 4 phần tử, $s=1/4$; cặp $(1,4)$ có giao $\{a,d\}$, hợp 3 phần tử, $s=2/3$; cặp $(3,4)$ có giao $\{d\}$, hợp 5 phần tử, $s=1/5$. Kết quả $\{(1,4)\}$.
- **Đầu vào và giả thiết:** Tập V02 và $\mathcal C$ ở trang trước.
- **Dữ kiện, hình thức hóa và vết chạy:** V02 giữ $t$; $\widehat s_{14}=1$ nhưng $s_{14}=2/3$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 3 hàng cặp/giao-hợp/Jaccard/kết quả ở giữa, ngưỡng trên bảng. Năm 2 tính lại tử và mẫu trước quyết định; notes giữ danh sách hợp đầy đủ.
- **Kết nối vào–ra:** Ứng viên→kết quả trong ví dụ; dải nhiều hàng sẽ thay điều kiện trùng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hợp của $S_1$ và $S_3$ là $\{a,b,d,e\}$; hợp của $S_1$ và $S_4$ là $\{a,c,d\}$; hợp của $S_3$ và $S_4$ là $\{a,b,c,d,e\}$. Cặp $(1,3)$ và $(3,4)$ là ứng viên giả ở tầng tạo cặp. Xác minh không thể khôi phục một cặp đạt ngưỡng đã bị bỏ sót bởi phân dải.
- **Nguồn:** B §3.4.3 tr.95–96; Ex 3.8; dữ kiện; V02.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-06 — Điều kiện trùng một dải

- **Mục đích và vai trò:** Phân biệt trùng một thành phần với trùng tuple nhiều hàng.
- **Thông điệp:** Một dải $r=3$ đòi cả ba thành phần trùng.
- **Nội dung công khai dự kiến:** Dải đầu Hình 3.7: hàng $(1,0,0,0,2),(3,2,1,2,2),(0,1,3,1,1)$. Cột 2 và 4 đều $(0,2,1)$; cột 3 là $(0,1,3)$. Chữ ký nguồn có 12 hàng nhưng chỉ dải đầu được cho.
- **Đầu vào và giả thiết:** V02 đã có $r=1$; nay thay dữ kiện sang V03.
- **Dữ kiện, hình thức hóa và vết chạy:** V03; cặp 2,3 trùng hàng đầu nhưng khác tuple; cặp 2,4 là ứng viên bất kể dải còn lại.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ma trận 3 × 5 chiếm 60% trên; hai tuple so sánh ở dưới. Phần 9 hàng thiếu chỉ ghi “các dải khác chưa có dữ kiện”. Năm 2 thấy điều kiện AND thất bại tại hàng 2; không dựng tổng ứng viên từ dữ liệu thiếu.
- **Kết nối vào–ra:** Vết một hàng→điều kiện tổng quát; ký hiệu tuple đủ để viết đặc tả.
- **Diễn giải học thuật, lời giải và tiêu chí:** Kết luận được giới hạn ở dải đầu. Cột 2 và 3 vẫn có thể thành ứng viên nếu trùng một dải khác chưa được cho. Việc khác thùng ở một dải chưa kết luận Jaccard thấp.
- **Nguồn:** B Ex 3.11/Hình 3.7 tr.92–93/PDF 21–22; M 45–46.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-07 — Đặc tả bộ tạo ứng viên

- **Mục đích và vai trò:** Viết điều kiện trước và sau của phân dải.
- **Thông điệp:** Tập ứng viên là hợp của các cặp trùng khóa dải đầy đủ.
- **Nội dung công khai dự kiến:** Các tập nguồn hữu hạn không rỗng. Vào:$\mathrm{SIG}\in V^{n\times C}$,$n=br$,$b,r\in\mathbb N_{>0}$. Khóa $k_{j,c}=(j,\mathrm{SIG}_{(j-1)r+1:jr,c})$. Ra:$\mathcal C=\{(c,d):c<d,\exists j:k_{j,c}=k_{j,d}\}$. Bảng băm so khóa đầy đủ để giải va chạm.
- **Đầu vào và giả thiết:** Ví dụ tuple và cùng dải.
- **Dữ kiện, hình thức hóa và vết chạy:** HT1; $j=1,\ldots,b$;$c=1,\ldots,C$; V02 khóa $(2,(0))$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba dòng vào/khóa/ra toàn chiều ngang; khóa ở khung giữa. Năm 2 ánh xạ (j, tuple) của vết chạy sang ký hiệu lát ma trận; diễn giải chỉ số ở notes, không thêm chứng minh trên cùng trang.
- **Kết nối vào–ra:** Tuple đã thấy→hợp đồng; giả mã thực hiện đúng hợp đồng này.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hàm băm bảng chỉ định nơi tra cứu; phép bằng vẫn so cả số dải và tuple. Điều kiện tồn tại một dải giải thích phép hợp ứng viên. Đầu ra dùng thứ tự $c<d$ để hai cách gọi một cặp có cùng biểu diễn. Bước xác minh tiếp theo nhận ngưỡng Jaccard $t\in[0,1]$.
- **Nguồn:** B §3.4.1, 3.4.3 tr.92–96; diễn đạt đặc tả đã duyệt.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-08 — Thuật toán tạo và kiểm cặp

- **Mục đích và vai trò:** Theo dõi khởi tạo, vòng lặp, phát cặp và kết quả trả về.
- **Thông điệp:** Dựng thùng trước khi phát cặp giúp tránh xét mọi cặp của kho.
- **Nội dung công khai dự kiến:** B ← từ điển rỗng; CAND ← tập rỗng với j = 1,…,b và c = 1,…,C: z ← bản sao SIG[(j−1)r+1 : jr, c] k ← (j, z) nếu k chưa có trong B: B[k] ← [] B[k].append(c) với mỗi danh sách L trong B: với mỗi c < d thuộc L: CAND.add((c,d)) OUT ← tập rỗng với mỗi (c,d) trong CAND: nếu SIM(S_c,S_d) ≥ t: OUT.add((c,d)) trả OUT Vết chạy8 lượt chèn tài liệu 4 lượt phát cặp 3 lần kiểm Jaccard 1 cặp kết quả
- **Đầu vào và giả thiết:** HT1; đọc từ điển, danh sách và tập; các tập gốc hữu hạn không rỗng sẵn có; $t\in[0,1]$.
- **Dữ kiện, hình thức hóa và vết chạy:** V02 nối vào dòng chèn 8 lần, phát 4 lần, kiểm 3 lần; không có vòng trên mọi cặp kho.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khối giả mã lớn trái 70%; phải 30% ba trạng thái “thùng→cặp duy nhất→kết quả” kèm 8/4/3. Năm 2 đã biết vòng lặp, cần thấy dữ liệu truyền giữa pha; notes mô tả chi tiết so khóa và Jaccard.
- **Kết nối vào–ra:** Hợp đồng→thủ tục; bất biến chứng minh việc dựng nhóm và phát cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Khóa được sao chép để phân tích bộ nhớ thống nhất. Khi khóa chưa có trong từ điển, thuật toán tạo danh sách rỗng rồi mới nối mã tài liệu; khi khóa đã có, thuật toán nối vào danh sách hiện tại. Các vòng lặp đều trên tập hữu hạn. Tập CAND khử lặp sau mỗi lần phát. Jaccard gốc được tính trực tiếp cho mỗi cặp duy nhất; bỏ kiểm chữ ký ở bước 6 của sách và bắt buộc kiểm gốc trên mọi ứng viên. Trong sách, bước 7 kiểm gốc mới được ghi là tùy chọn.
- **Nguồn:** B §3.4.1 tr.92–93, §3.4.3 tr.95–96; giả mã diễn đạt và lựa chọn baseline đã duyệt.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 3.5 phút.

#### lec06-s02-09 — Bất biến và phạm vi tính đúng

- **Mục đích và vai trò:** Giải thích vì sao thuật toán trả đúng kết quả theo tập ứng viên.
- **Thông điệp:** Tính đúng của dựng thùng không bảo đảm thu đủ mọi cặp tương đồng.
- **Nội dung công khai dự kiến:** Bất biến: ở dải đang xét, mỗi mã đã xử lý thuộc đúng nhóm khóa của nó. BướcLập luận Khởi tạoTrước dải đầu, $B$ rỗng. Đầu dải $j$, chưa có khóa mang $j$; giữ các dải trước. Duy trìTạo danh sách nếu khóa mới, rồi nối mã vào đúng nhóm. Kết thúcPhát mọi cặp chung nhóm; hợp khử lặp; kiểm Jaccard gốc. Đầu ra gồm đúng các cặp trong $\mathcal C$ có $s\ge t$. Các vòng lặp hữu hạn; $C<2$ hoặc thùng có dưới hai phần tử không phát cặp.
- **Đầu vào và giả thiết:** Giả mã và đầu ra HT1.
- **Dữ kiện, hình thức hóa và vết chạy:** B rỗng trước dải đầu. Trước dải j chưa có khóa mang j; các dải trước giữ nguyên. Mỗi lượt chèn tạo đúng danh sách nếu cần rồi thêm đúng một mã, không di chuyển mã khác.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba bước khởi tạo/duy trì/kết thúc xếp dọc với một kết luận dưới. Năm 2 nối bất biến với dòng chèn đã thấy; proof đầy đủ và tập rỗng vào notes.
- **Kết nối vào–ra:** Thủ tục→bảo đảm có điều kiện; xác suất bước tới mô tả việc một cặp được sinh.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chứng minh theo số lượt chèn ở từng dải. Trước dải đầu tiên, từ điển $B$ rỗng. Ở đầu mỗi dải $j$, chưa có khóa mang chỉ số $j$, còn các nhóm của những dải trước được giữ nguyên. Vì chưa xử lý mã nào ở dải $j$, bất biến của dải này đúng. Nếu khóa mới, danh sách rỗng được tạo trước khi nối mã; nếu khóa đã có, các mã trước đó được giữ nguyên. Mỗi lượt bổ sung đúng một mã vào nhóm khóa của nó và không chuyển mã khác. Khi dựng thùng kết thúc, phát mọi cặp trong từng thùng cho đúng quan hệ tồn tại dải; phép hợp khử lặp. Kiểm Jaccard gốc xác định đầu ra trong tập ứng viên. Đầu vào của đặc tả là các tập hữu hạn không rỗng; tập rỗng nằm ngoài miền phân tích này.
- **Nguồn:** B §3.4.1, 3.4.3; chứng minh suy từ thủ tục nguồn, đã duyệt.
- **Ánh xạ ghi chú:** `N02`. **Thời lượng:** 2 phút.

#### lec06-s02-10 — Xác suất trùng trong một dải

- **Mục đích và vai trò:** Suy xác suất AND từ các hàng độc lập.
- **Thông điệp:** Một dải $r$ hàng trùng với xác suất $s^r$.
- **Nội dung công khai dự kiến:** Cặp tập không rỗng cố định có Jaccard $s$. Mỗi MinHash lý tưởng chọn đều, độc lập. Đặt $E_i=$“hai chữ ký trùng ở hàng $i$”. $\Pr(E_i)=s$, $\Pr(\cap_{i=1}^rE_i)=s^r$. Không trùng dải:$1-s^r$.
- **Đầu vào và giả thiết:** Định lý MinHash Bài 05 và độc lập; phép trùng tuple V03.
- **Dữ kiện, hình thức hóa và vết chạy:** HT3; V04 $s=.8,r=5$ cho $s^r=.32768$; thất bại dải=.67232.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bên trái 55% ghi các sự kiện theo hàng; phải 45% công thức và thế số. Năm 2 ghép nghĩa “tất cả” với phép nhân; giả thiết hiện phía trên, còn khác mô hình V02 ở notes.
- **Kết nối vào–ra:** Tính đúng theo ứng viên→khả năng một dải nhận cặp; nhiều dải dùng biến cố bù.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tính độc lập thuộc các lần chọn hàm, chưa thuộc các cặp dữ liệu. Hai hàm cố định trong ví dụ đã cho không được dùng để suy công thức này. Giá trị $s=.8$ là tương đồng thật, không là tỷ lệ trùng của một chữ ký quan sát.
- **Nguồn:** B §3.4.2 tr.93–94/PDF 22–23; Ex 3.12 tr.94.
- **Ánh xạ ghi chú:** `N03`. **Thời lượng:** 2.5 phút.

#### lec06-s02-11 — Xác suất tạo ứng viên

- **Mục đích và vai trò:** Dùng biến cố bù để suy xác suất ít nhất một dải trùng.
- **Thông điệp:** Các dải độc lập cho $P_{b,r}(s)=1-(1-s^r)^b$.
- **Nội dung công khai dự kiến:** Không dải nào trùng:$(1-s^r)^b$. Ít nhất một dải trùng:$P_{b,r}(s)=1-(1-s^r)^b$. Với $b=20,r=5,s=.8$: bỏ sót $.000356058$, được chọn $.999643942$.
- **Đầu vào và giả thiết:** Sự kiện dải ở trang trước; các nhóm hàm độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** V04, HT3; $.67232^{20}=.000356058$; cả hai xác suất theo một cặp $s=.8$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai hàng sự kiện→công thức trên; thế số dưới. Năm 2 thấy phép bù sau phép nhân theo dải; chưa đưa đồ thị trước khi biết trục tung.
- **Kết nối vào–ra:** Một dải→hợp nhiều dải; đồ thị dùng công thức để chọn tham số.
- **Diễn giải học thuật, lời giải và tiêu chí:** Xác suất bỏ sót tại một cặp đạt ngưỡng là $1-P(s)$. Các nhóm hàng độc lập vì toàn bộ các MinHash thành phần độc lập. Cặp dữ liệu được giữ cố định suốt phép suy. Với $r=1$, đường xác suất lõm và không có đầy đủ dạng chữ S.
- **Nguồn:** B §3.4.2 tr.93–95; M PDF 54; S3 PDF 49.
- **Ánh xạ ghi chú:** `N03`. **Thời lượng:** 2 phút.

#### lec06-s02-12 — Ngưỡng và lựa chọn số dải

- **Mục đích và vai trò:** Phân biệt ba đại lượng ngưỡng và so cấu hình cùng $n$.
- **Thông điệp:** Ngưỡng chấp nhận do bài toán đặt; đường xác suất do $b,r$ quyết định.
- **Nội dung công khai dự kiến:** Ngưỡng chấp nhận $t=.8$; xét $(b,r)=(20,5)$. Điểm xác suất một nửa: $P(s_{1/2})=1/2$, $s_{1/2}\approx.508696$. Xấp xỉ điểm chuyển tiếp: $b^{-1/r}\approx.549280$.
- **Đầu vào và giả thiết:** HT3; ngưỡng $t$ từ đặc tả.
- **Dữ kiện, hình thức hóa và vết chạy:** V04, HT4; $s_{1/2}=(1-2^{-1/b})^{1/r}$ để notes/suy đại số; điểm xấp xỉ có $P=.641514$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Đồ thị lớn toàn chiều rộng; ba dòng ngắn bên dưới phân biệt t, điểm P(s_half)=1/2 và xấp xỉ vùng chuyển tiếp. Công thức đóng và phép biến đổi nằm trong notes, không thu nhỏ chữ để giữ cả công thức dài.
- **Kết nối vào–ra:** Xác suất→quyết định tham số; số ứng viên và lượt phát quyết định chi phí thực tế.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tại $s=.8$, cấu hình 20 × 5 bỏ sót khoảng .035606%; 10 × 10 khoảng 32.114003%. Đây là xác suất có điều kiện theo $s$, không là tỷ lệ lỗi của một kho chưa biết phân bố tương đồng. Phương trình $P(s)=1/2$ cho $s^r=1-2^{-1/b}$, nên $s_{1/2}=(1-2^{-1/b})^{1/r}$. Giá trị $b^{-1/r}$ xấp xỉ vùng chuyển tiếp; nó không bằng nghiệm xác suất một nửa hoặc ngưỡng chấp nhận $t$.
- **Nguồn:** B Ex 3.12 tr.94–95, Bài 3.4.2 tr.96; S4 PDF 34/trang in 37; so $n$ cố định.
- **Ánh xạ ghi chú:** `N03`. **Thời lượng:** 2.5 phút.

#### lec06-s02-13 — Chi phí tạo và xác minh ứng viên

- **Mục đích và vai trò:** Gắn từng số hạng chi phí với pha thuật toán.
- **Thông điệp:** Thời gian phụ thuộc lượt phát cặp, không chỉ số tài liệu.
- **Nội dung công khai dự kiến:** Chữ ký đã có; từ máy; sao chép tuple; bảng băm kỳ vọng. Bảng: đọc $bC$ tuple×$r$→$nC$; phát/khử lặp→$Q=\sum_{j,z}\binom{u_{j,z}}2$; kiểm→$K$ cặp. Tổng $O(nC+Q+\sum T_J)$; bộ nhớ phụ $O(nC+K)$. Xấu nhất $Q=b\binom C2$.
- **Đầu vào và giả thiết:** Giả mã, khử lặp;$u_{j,z}$ là kích thước thùng;$K=|\mathcal C|$.
- **Dữ kiện, hình thức hóa và vết chạy:** V02:8 chèn,4 phát,3 kiểm; V01 không tự có tỷ lệ giảm. SIG $nC$ từ là đầu vào riêng. $T_J$ không giả định hằng.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Mô hình một dòng trên; bảng 3 hàng trọng tâm; công thức tổng và xấu nhất dưới. Năm 2 truy chi phí về thao tác đã chạy. Notes chứa biểu diễn tập sắp xếp và phân rã bộ nhớ chi tiết.
- **Kết nối vào–ra:** Tham số→lượng công việc; kiểm tra phần yêu cầu phối hợp thuật toán, xác suất và giới hạn.
- **Diễn giải học thuật, lời giải và tiêu chí:** $u_{j,z}$ là số mã tài liệu trong thùng $(j,z)$. Xử lý mỗi khóa dài $r$ tốn $O(r)$; kỳ vọng bảng băm được tính sau xử lý khóa. Các tập đã sắp xếp cho $T_J(c,d)=O(|S_c|+|S_d|)$. Khóa sao chép tối đa $nC$ từ, danh sách $bC$ mã, tập cặp $K$ phần tử. Nếu mọi cột chung mỗi thùng thì $K=\binom C2$.
- **Nguồn:** B §3.4.1, 3.4.3; phân tích suy từ giả mã đã duyệt, N04; U PDF 14; đối chiếu quan hệ ứng viên–công việc.
- **Ánh xạ ghi chú:** `N04`. **Thời lượng:** 3.5 phút.

#### lec06-s02-14 — Kiểm tra phân dải và xác minh

- **Mục đích và vai trò:** Giải thích vai trò khử lặp, xác minh và độc lập.
- **Thông điệp:** Ba bước xử lý có ba hợp đồng khác nhau.
- **Nội dung công khai dự kiến:** Câu hỏi: Dùng ma trận và các tập đã cho với $b=2,r=1,t=2/3$: xác định $Q,K$ và kết quả sau kiểm gốc. Với mô hình MinHash lý tưởng độc lập, viết xác suất được chọn của cặp có Jaccard $s$. Nêu giả thiết dùng để nhân xác suất.
- **Đầu vào và giả thiết:** V02 hiển thị lại SIG và ba Jaccard cần dùng; các công thức phần 2.
- **Dữ kiện, hình thức hóa và vết chạy:** Đáp án $Q=4,K=3$, tập kết quả chỉ gồm (1,4);$P(s)=1-(1-s)^2$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 45% ma trận 2 × 4 và tập gốc gọn; phải 55% ba nhiệm vụ. Năm 2 vận dụng lại dữ kiện đã theo dõi, cần phân biệt kết quả xác định với mô hình xác suất. Không hiện đáp án.
- **Kết nối vào–ra:** Chi phí→kiểm phần; Jaccard là một độ đo nền, phần 3 xây các cách đo gần khác.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: cặp $(1,4)$ được phát hai lần; tập ứng viên là $\{(1,3),(1,4),(3,4)\}$; chỉ cặp $(1,4)$ đạt ngưỡng. Do đó $Q=4,K=3$. Trong mô hình hai thành phần MinHash lý tưởng độc lập, xác suất được chọn của cặp có Jaccard $s$ là $1-(1-s)^2$. Tiêu chí: phân biệt lượt phát và cặp duy nhất, kiểm Jaccard trên tập gốc và nêu đúng nguồn ngẫu nhiên.
- **Nguồn:** B Ex 3.8/ §3.4; câu kiểm tra áp dụng nguyên dữ kiện nguồn, tham số đã duyệt.
- **Ánh xạ ghi chú:** `N02,N03,N04`. **Thời lượng:** 3 phút.

### Phần 3. Khoảng cách và họ nhạy cảm

#### lec06-s03-01 — Khoảng cách giữa hai điểm

- **Mục đích và vai trò:** Tính ba cách đo trên cùng hai điểm.
- **Thông điệp:** Cách định nghĩa khoảng cách quyết định ý nghĩa của gần nhau.
- **Nội dung công khai dự kiến:** MinHash gắn với Jaccard; tìm cặp vector hoặc chuỗi cần xác định độ đo phù hợp. $x=(2,7),\quad y=(6,4)$ $L_1=4+3=7$ $L_2=\sqrt{4^2+3^2}=5$ $L_\infty=\max(4,3)=4$
- **Đầu vào và giả thiết:** Tọa độ, hình học phẳng; Jaccard đã đo hai tập.
- **Dữ kiện, hình thức hóa và vết chạy:** V05:$\sqrt{4^2+3^2}=5$, $4+3=7$, $\max(4,3)=4$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình tọa độ trái 60% giữ tỷ lệ, trục $x_1,x_2$; phải 40% ba phép tính cùng thứ tự. Năm 2 đã có hình học, cần thấy cùng dữ liệu cho ba quy tắc; định nghĩa tổng quát sang trang sau.
- **Kết nối vào–ra:** Phân dải mới có xác suất gắn Jaccard trên tập; vector và chuỗi cần độ đo riêng. Ba cách đo của cùng cặp điểm dẫn sang miền và tiên đề metric.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đoạn thẳng nối hai điểm cho khoảng cách Euclid. Đường đi theo hai trục có tổng độ dài 7. Độ lệch lớn nhất bằng 4. Các giá trị mô tả ba cách đo, không phải ba ước lượng của cùng một đại lượng.
- **Nguồn:** B §3.5.2/Ex 3.13 tr.97–98/PDF 26–27.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 2 phút.

#### lec06-s03-02 — Độ đo khoảng cách

- **Mục đích và vai trò:** Nêu miền và bốn tiên đề trước khi dùng độ đo.
- **Thông điệp:** Độ đo mô tả gần–xa bằng một hàm có điều kiện xác định.
- **Nội dung công khai dự kiến:** $d:X\times X\to\mathbb R_{\ge0}$; $d(x,y)=0\Leftrightarrow x=y$; đối xứng; $d(x,z)\le d(x,y)+d(y,z)$. Với $x,y\in\mathbb R^D$, $d_q(x,y)=(\sum_i|x_i-y_i|^q)^{1/q}$,$q\ge1$; $d_\infty=\max_i|x_i-y_i|$.
- **Đầu vào và giả thiết:** V05, kiểu hàm và bất đẳng thức.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5; không áp định nghĩa chuẩn $q<1$; $D$ số chiều, không là khoảng cách.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khung định nghĩa ở trên 60%; dòng họ chuẩn và V05 nhãn 5/7/4 ở dưới 40%. Năm 2 chuyển số cụ thể sang miền và ký hiệu; chứng minh Minkowski không nằm tuyến chính.
- **Kết nối vào–ra:** Ba phép đo cụ thể→tiên đề; Jaccard có khoảng cách tương ứng cho tập.
- **Diễn giải học thuật, lời giải và tiêu chí:** Không âm là miền giá trị của $d$; điều kiện bằng 0 tách điểm; đối xứng không phụ thuộc thứ tự cặp; bất đẳng thức tam giác chặn đường trực tiếp bằng đường qua điểm thứ ba. Tuyến bài dùng $q=1,2,\infty$.
- **Nguồn:** B §3.5.1–2 tr.97–98; bổ sung $q\ge1$ để sửa phát biểu quá rộng của nguồn.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 2 phút.

#### lec06-s03-03 — Khoảng cách Jaccard

- **Mục đích và vai trò:** Chuyển tương đồng tập sang khoảng cách và đọc bước chứng minh tam giác.
- **Thông điệp:** MinHash biểu diễn khoảng cách Jaccard bằng xác suất khác nhau.
- **Nội dung công khai dự kiến:** Các tập hữu hạn không rỗng; cặp đã có: $d_J(S_1,S_4)=1-2/3=1/3$. $d_J(A,B)=1-\frac{|A\cap B|}{|A\cup B|}=\Pr[h(A)\ne h(B)]$ Dùng cùng một MinHash lý tưởng $h$ cho cả ba tập: $\{h(A)\ne h(C)\}\subseteq\{h(A)\ne h(B)\}\cup\{h(B)\ne h(C)\}$ $d_J(A,C)\le d_J(A,B)+d_J(B,C)$ Lấy xác suất rồi chặn hợp; không cần độc lập giữa hai biến cố.
- **Đầu vào và giả thiết:** Tiên đề metric; định lý MinHash Bài 05 và chặn hợp.
- **Dữ kiện, hình thức hóa và vết chạy:** Cặp S1,S4 có SIM=2/3 → d_J=1/3; d_J(A,B)=Pr[h(A)≠h(B)] bằng lấy bù định lý MinHash; cùng h cho ba tập → bao hàm sự kiện → chặn hợp → tam giác.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Một chuỗi suy luận toàn chiều rộng: ví dụ cặp đã học, nhận diện khoảng cách với xác suất khác băm, bao hàm sự kiện, rồi cận tam giác. Giữ miền không rỗng và cùng h; không thêm hình trang trí.
- **Kết nối vào–ra:** Khái niệm metric→mô hình tập đã biết; khoảng cách góc mở miền vector theo hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Nếu $h(A)\ne h(C)$ thì không thể đồng thời $h(A)=h(B)$ và $h(B)=h(C)$. Định lý MinHash cho $\Pr[h(A)=h(B)]=\mathrm{SIM}(A,B)$; lấy bù được $\Pr[h(A)\ne h(B)]=d_J(A,B)$. Cặp $S_1,S_4$ có Jaccard $2/3$ nên khoảng cách $1/3$. Lấy xác suất của bao hàm sự kiện và chặn hợp cho $d_J(A,C)\le d_J(A,B)+d_J(B,C)$. Không cần ba sự kiện độc lập. Các tiên đề còn lại theo định nghĩa giao, hợp trên tập không rỗng.
- **Nguồn:** B §3.5.3 tr.98–99/PDF 27–28; P5; miền tập không rỗng.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 2.5 phút.

#### lec06-s03-04 — Khoảng cách góc

- **Mục đích và vai trò:** Tính góc và nêu miền mà góc là metric.
- **Thông điệp:** Khoảng cách góc phân biệt các hướng, độc lập với độ dài vector.
- **Nội dung công khai dự kiến:** Dữ kiện: $x=(1,2,-1),y=(2,1,1)$; $x\cdot y=3$, $\|x\|=\|y\|=\sqrt6$; $\cos\theta=1/2$, $\theta=\pi/3=60^\circ$. Miền: vector đơn vị hoặc hướng, bội dương được đồng nhất; vector 0 không có hướng.
- **Đầu vào và giả thiết:** Tích vô hướng, chuẩn Euclid, và điều kiện d=0.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5, V06; góc radian $\theta=\arccos((x\cdot y)/(\|x\|\|y\|))$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 50% hai vector chuẩn hóa thành hướng; phải 50% tích/chuẩn/góc ba dòng. Năm 2 phân biệt cosin và góc bằng đơn vị; nhận xét $1-\cos\theta$ ở notes.
- **Kết nối vào–ra:** Jaccard đo tập→góc đo hướng; chuỗi dùng phép thay đổi rời rạc.
- **Diễn giải học thuật, lời giải và tiêu chí:** Cosin là độ tương đồng bằng $1/2$ trong ví dụ; khoảng cách góc bằng $\pi/3$. Hai bội dương có góc 0 nên chỉ xem góc là metric sau đồng nhất hướng hoặc chuẩn hóa. Hai vector đối hướng có góc $\pi$. Phép băm dấu phần 4 sử dụng đúng góc này.
- **Nguồn:** B §3.5.4/Ex 3.14 tr.99/PDF 28; S4 PDF 45/trang in 48; đối chiếu thuật ngữ.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 2 phút.

#### lec06-s03-05 — Khoảng cách chỉnh sửa chuỗi

- **Mục đích và vai trò:** Theo dõi phép chèn/xóa và tính khoảng cách theo LCS.
- **Thông điệp:** Khoảng cách chỉnh sửa trong bài đếm phép chèn và xóa.
- **Nội dung công khai dự kiến:** Khoảng cách chỉnh sửa là số thao tác ít nhất để biến chuỗi này thành chuỗi kia; mỗi bước chèn hoặc xóa một ký tự. $abcde\to acde\to acfde\to acfdeg$ Thao tácChuỗi sau thao tác Xóa bacde Chèn facfde Chèn gacfdeg $d_{\rm edit}(x,y)=|x|+|y|-2L=5+6-2\cdot4=3$ Dãy con chung dài nhất là acde, dài L=4; dãy con không cần liên tiếp.
- **Đầu vào và giả thiết:** Chuỗi, dãy con, độ dài; chỉ chèn/xóa.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5, V07; $5+6-8=3$; dãy con $acde$. Không có phép thay thế một bước.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Vết bốn trạng thái trên 70% ngang, mỗi mũi tên ghi thao tác; công thức dưới 30%. Năm 2 thấy dữ liệu còn lại trước công thức; proof hai cận và định nghĩa LCS đầy đủ trong notes.
- **Kết nối vào–ra:** Góc đo thay hướng→chuỗi đo thao tác sửa; Hamming sẽ giữ cố định độ dài/vị trí.
- **Diễn giải học thuật, lời giải và tiêu chí:** Một phương án tối ưu giữ một dãy con chung và xóa/chèn các ký tự khác. Giữ $L$ ký tự cần $|x|-L$ lần xóa và $|y|-L$ lần chèn. Ngược lại, các ký tự không bị xóa tạo thành dãy con chung nên không giữ quá $L$. Đây là lập luận giá trị tối ưu, không cung cấp thuật toán quy hoạch động tính LCS.
- **Nguồn:** B §3.5.5/Ex 3.15–16 tr.100/PDF 29.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 2 phút.

#### lec06-s03-06 — Khoảng cách Hamming

- **Mục đích và vai trò:** Đếm tọa độ khác nhau trên vector cùng độ dài.
- **Thông điệp:** Hamming giữ vị trí và đếm số bất đồng.
- **Nội dung công khai dự kiến:** Chỉ số12345 x10101 y11110 So sánhTrùngKhácTrùngKhácKhác $d_H(x,y)=\sum_{i=1}^D\mathbf1[x_i\ne y_i]=3$ $\mathbf1[E]=1$ nếu $E$ đúng, bằng 0 nếu $E$ sai. Hamming đếm vị trí khác trên hai vector cùng chiều.
- **Đầu vào và giả thiết:** Vector rời rạc cùng chiều; khác với phép chèn/xóa.
- **Dữ kiện, hình thức hóa và vết chạy:** V08, HT5; hai vị trí trùng 1,3 dùng lại trong s04-01/02.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai hàng bit thẳng cột, nhãn “trùng/khác” dưới từng vị trí; công thức dưới. Năm 2 đếm trực tiếp trước dùng mẫu số $D$; notes chứng minh tam giác theo tọa độ.
- **Kết nối vào–ra:** Chuỗi có thể đổi chiều→vector cố định chiều; các độ đo đã đủ để diễn đạt họ gần–xa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Nếu $x_i\ne z_i$ thì ít nhất một trong $x_i\ne y_i$ hoặc $y_i\ne z_i$ đúng. Cộng theo tọa độ cho bất đẳng thức tam giác. Khi xây họ chọn tọa độ, giả thiết $D>0$ cần để có phân phối đều.
- **Nguồn:** B §3.5.6/Ex 3.17 tr.101/PDF 30.
- **Ánh xạ ghi chú:** `N05`. **Thời lượng:** 1.5 phút.

#### lec06-s03-07 — Họ băm nhạy cảm

- **Mục đích và vai trò:** Diễn giải đầy đủ bốn tham số và nguồn xác suất.
- **Thông điệp:** Họ nhạy cảm chặn xác suất trùng ở hai miền khoảng cách.
- **Nội dung công khai dự kiến:** $0\le d_1<d_2,\quad0\le p_2<p_1\le1$; $\mathcal H$ là họ hàm kèm phân phối. Cặp $x,y$ cố định; xác suất theo $h\sim\mathcal H$, cùng $h$ băm hai đối tượng. Họ (d₁,d₂,p₁,p₂)-nhạy cảm được xác định bởi hai cận.
- **Đầu vào và giả thiết:** Metric, sự kiện va chạm MinHash đã biết.
- **Dữ kiện, hình thức hóa và vết chạy:** HT6; cùng hàm $h$ áp cho hai đối tượng; không lấy xác suất trên “mỗi hàm cố định”.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trục khoảng cách chia gần/giữa/xa chiếm 45% trên; hai bất đẳng thức lớn dưới. Năm 2 cần liên kết hướng≤với≥xác suất; không vẽ đường cong cụ thể cho mọi họ.
- **Kết nối vào–ra:** Các độ đo→mô hình xác suất chung; MinHash kiểm định định nghĩa bằng một ví dụ đã quen.
- **Diễn giải học thuật, lời giải và tiêu chí:** Độ đo xác định cặp gần và xa; một họ băm phải có phân phối lấy mẫu và hai cận xác suất tương ứng. Nguồn ngẫu nhiên là phép lấy $h$ từ họ có phân phối. Với dữ liệu và $h$ đã cố định, kết quả trùng là xác định. Định nghĩa chỉ đòi hai cận; không đòi đẳng thức giữa xác suất va chạm và một độ tương đồng.
- **Nguồn:** B §3.6.1 tr.103–104/PDF 32–33; S4 PDF 19/trang in 22 và PDF 20/trang in 23.
- **Ánh xạ ghi chú:** `N06`. **Thời lượng:** 3 phút.

#### lec06-s03-08 — Họ MinHash theo Jaccard

- **Mục đích và vai trò:** Chuyển cận khoảng cách thành cận va chạm.
- **Thông điệp:** MinHash cho một trường hợp cụ thể của họ nhạy cảm.
- **Nội dung công khai dự kiến:** $d_J=1-s$; $\Pr[h(A)=h(B)]=1-d_J(A,B)$. Gần:$d_J\le.3\Rightarrow P\ge.7$; xa:$d_J\ge.6\Rightarrow P\le.4$. Họ $(.3,.6,.7,.4)$.
- **Đầu vào và giả thiết:** HT6; tập hữu hạn không rỗng, MinHash lý tưởng.
- **Dữ kiện, hình thức hóa và vết chạy:** B Ex 3.18; phân biệt bộ tham số này với V09(.2, .6, .8, .4) sẽ dùng cho ghép.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 2 hàng miền khoảng cách/phép trừ/cận xác suất; dòng bộ 4 dưới. Năm 2 thực hiện $1-d$ để thấy đảo hướng bất đẳng thức; không thêm đồ thị trùng chức năng.
- **Kết nối vào–ra:** Định nghĩa→một họ có thật; phép ghép sẽ thay cận xác suất của họ cơ sở.
- **Diễn giải học thuật, lời giải và tiêu chí:** Từ tính đơn điệu giảm của $1-d$, miền gần cho cận dưới còn miền xa cho cận trên. Hai ngưỡng không quyết định hành vi trong miền giữa. Họ này sử dụng kết quả MinHash, không phải một chứng minh mới của định lý MinHash.
- **Nguồn:** B §3.6.2/Ex 3.18 tr.104–105/PDF 33–34.
- **Ánh xạ ghi chú:** `N06`. **Thời lượng:** 2 phút.

#### lec06-s03-09 — Phép ghép đồng thời

- **Mục đích và vai trò:** Suy biến đổi xác suất AND và các cận của họ.
- **Thông điệp:** Ghép AND làm giảm cả xác suất trùng của cặp gần lẫn cặp xa.
- **Nội dung công khai dự kiến:** Phép ghép đồng thời (AND). Chọn $h_1,\ldots,h_r$ độc lập; cùng các hàm cho mọi đối tượng. Tuple $g(x)=(h_1(x),\ldots,h_r(x))$. $\Pr[g(x)=g(y)]=p^r$. Họ mới $(d_1,d_2,p_1^r,p_2^r)$.
- **Đầu vào và giả thiết:** Dải nhiều hàng V03, họ 4 tham số, độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7; $p$ va chạm cặp cố định;$r=4,p=.8$ cho.4096;$p=.4$ cho.0256.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Nhóm $r$ phép thử trái 55%, ngoặc tuple; phải 45% phép nhân và cận. Năm 2 đối chiếu đúng cấu trúc một dải trước khái quát; chi tiết tính đơn điệu ở notes.
- **Kết nối vào–ra:** Họ cơ sở→AND; OR bổ sung cơ hội trùng để giảm bỏ sót.
- **Diễn giải học thuật, lời giải và tiêu chí:** Cặp dữ liệu được giữ cố định; mỗi phép thử cơ sở trùng với xác suất $p$. Sự kiện bằng tuple là giao của $r$ sự kiện trùng. Độc lập cho tích $p^r$. Hàm $p\mapsto p^r$ tăng trên [0,1], nên bảo toàn hướng hai cận gần/xa. Khi $r>1$, xác suất trong (0,1) giảm; nhiều cặp gần cũng khó được chọn hơn.
- **Nguồn:** B §3.6.3 tr.105–106/PDF 34–35; S4 PDF 25/trang in 28.
- **Ánh xạ ghi chú:** `N07`. **Thời lượng:** 2.5 phút.

#### lec06-s03-10 — Phép ghép ít nhất một

- **Mục đích và vai trò:** Suy biến đổi xác suất OR bằng biến cố bù.
- **Thông điệp:** Ghép OR tăng cơ hội nhận cặp và số ứng viên có thể phải kiểm.
- **Nội dung công khai dự kiến:** Phép ghép ít nhất một (OR). Chọn $b$ phép thử độc lập. Cặp được nhận nếu ít nhất một phép thử trùng. Xác suất $1-(1-p)^b$; cận mới $1-(1-p_1)^b$,$1-(1-p_2)^b$. OR là quyết định cặp qua nhiều bảng.
- **Đầu vào và giả thiết:** AND và phép bù; hợp dải V02.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7;$b=4,p=.8$ cho.9984;$p=.4$ cho.8704.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** $b$ bảng trái 55% mũi tên vào phép hợp; phải 45% sự kiện không trùng và bù. Năm 2 gắn OR với hợp ứng viên đã chạy; không diễn đạt OR thành bằng một tuple.
- **Kết nối vào–ra:** AND lọc chặt→OR bù cơ hội; hai thứ tự ghép cho hành vi khác nhau.
- **Diễn giải học thuật, lời giải và tiêu chí:** Không có phép thử trùng có xác suất $(1-p)^b$. Lấy bù cho OR; biểu thức tăng theo $p$ nên chuyển hai cận được. Quan hệ “trùng ở ít nhất một bảng” có thể không bắc cầu; nói chung nó không là phép bằng của một mã đơn.
- **Nguồn:** B §3.6.3 tr.106–107; S4 PDF 27/trang in 30.
- **Ánh xạ ghi chú:** `N07`. **Thời lượng:** 2.5 phút.

#### lec06-s03-11 — Thứ tự ghép và xác suất

- **Mục đích và vai trò:** So sánh AND–OR với OR–AND trên cùng 16 phép thử.
- **Thông điệp:** Cùng số hàm cơ sở không cho cùng đánh đổi.
- **Nội dung công khai dự kiến:** Dữ kiện: họ $(.2,.6,.8,.4)$,16 phép thử. AND 4→OR 4:$F(p)=1-(1-p^4)^4$; cận (.878497, .098535). OR 4→AND 4:$G(p)=[1-(1-p)^4]^4$; cận (.993615, .573952).
- **Đầu vào và giả thiết:** HT7 và phép thế xác suất.
- **Dữ kiện, hình thức hóa và vết chạy:** V09; trung gian $p^4$=.4096/.0256; OR 4=.9984/.8704; dùng số chưa làm tròn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai cột 50/50 cùng hàng: cấu trúc→công thức→cận gần/xa. Năm 2 so cùng tiêu chí và giữ 16 hàm; proof đã có nên mặt trang chỉ so phép ghép và giá trị.
- **Kết nối vào–ra:** Hai quy tắc→lựa chọn cấu trúc; cấu trúc cần được hiện thực qua bảng và có chi phí.
- **Diễn giải học thuật, lời giải và tiêu chí:** AND–OR cho cận xa nhỏ hơn nhưng cận gần cũng nhỏ hơn. OR–AND giữ cặp gần nhiều hơn đồng thời nhận cặp xa nhiều hơn. Hai kết luận cùng được đọc từ bảng; không có thứ tự tốt hơn vô điều kiện theo cả hai loại lỗi. Các số trong bảng là cận dưới gần và cận trên xa được biến đổi từ $p_1,p_2$; chỉ một cặp có xác suất cơ sở đúng bằng $p$ mới có xác suất ghép đúng bằng $F(p)$ hoặc $G(p)$.
- **Nguồn:** B Ex 3.19–20 tr.106–108/PDF 35–37.
- **Ánh xạ ghi chú:** `N07`. **Thời lượng:** 3 phút.

#### lec06-s03-12 — Cơ chế thực hiện phép ghép

- **Mục đích và vai trò:** Nối biểu thức logic với lưu trữ và số phép thử.
- **Thông điệp:** Với AND rồi OR, mỗi nhóm AND tạo khóa tuple và bước OR hợp các tập cặp.
- **Nội dung công khai dự kiến:** Trường hợp AND rồi OR: ghép đồng thời $r$ phép thử trong mỗi nhóm, rồi nhận khi ít nhất một trong $b$ nhóm trùng. Tính $br$ giá trị cơ sở; tạo $b$ tuple; tra $b$ bảng; hợp cặp và xác minh. Ngân sách tính và lưu tăng theo số phép thử; số ứng viên vẫn phụ thuộc kích thước thùng.
- **Đầu vào và giả thiết:** Giả mã phân dải và hai phép ghép.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7; sơ đồ thực hiện AND_r rồi OR_b. Với V09, đây là AND 4 rồi OR 4. Hai thứ tự đều dùng 16 giá trị, nhưng OR rồi AND phải hợp cặp trong từng nhóm OR rồi giao các tập cặp của những nhóm OR; chi phí phát và kiểm cặp vẫn phụ thuộc Q, K.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ 4 bước ngang trên; bảng nhỏ thao tác/số lượng dưới. Năm 2 chuyển ký hiệu xác suất thành thao tác lập trình quen; không tạo bảo đảm tốc độ từ số hàm.
- **Kết nối vào–ra:** Xác suất ghép→cơ chế và chi phí; kiểm tra phần nối miền metric với điều kiện họ.
- **Diễn giải học thuật, lời giải và tiêu chí:** Trong cấu trúc AND rồi OR, mỗi nhóm AND lưu trực tiếp một tuple; bước OR hợp các tập cặp qua nhiều bảng. Với thứ tự OR rồi AND, mỗi nhóm OR hợp các cặp từ các bảng cơ sở của nhóm, rồi bước AND lấy giao các tập cặp của những nhóm ấy. Quan hệ OR không được thay bằng phép bằng nhau của một tuple. Dù việc tính hàm băm ít tốn kém, thùng lớn vẫn phát nhiều cặp. Giá trị $br$ chỉ đo số phép thử cơ sở, mỗi phép có chi phí tùy họ.
- **Nguồn:** B §3.6.3 tr.105–108; liên hệ thuật toán §3.4.1 đã duyệt.
- **Ánh xạ ghi chú:** `N07`. **Thời lượng:** 2 phút.

#### lec06-s03-13 — Kiểm tra độ đo và phép ghép

- **Mục đích và vai trò:** Đọc cận họ, phân biệt miền và tính ghép.
- **Thông điệp:** Miền dữ liệu và giả thiết độc lập quyết định kết luận.
- **Nội dung công khai dự kiến:** Câu hỏi: Với họ $(.3,.6,.7,.4)$, nêu bảo đảm tại $d=.2$,$d=.8$ và điều có thể kết luận tại $d=.5$. Viết xác suất AND 2→OR 3 của cặp có xác suất cơ sở $p$. Hai vector $x$,$2x$ khác 0 có khoảng cách góc bằng bao nhiêu; miền metric phải hiểu thế nào?
- **Đầu vào và giả thiết:** HT5–HT7; bộ tham số Ex 3.18.
- **Dữ kiện, hình thức hóa và vết chạy:** Tại.2: P≥.7; .8: P≤.4; .5 không có cận từ định nghĩa. $1-(1-p^2)^3$; góc 0 trên cùng hướng.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Một khối gồm 3 nhiệm vụ độc lập, mỗi yêu cầu tối đa 2 dòng. Năm 2 kiểm cùng ba điều kiện vừa xây; lời giải và tiêu chí trong notes, không thêm ví dụ ngoài nguồn.
- **Kết nối vào–ra:** Cơ chế ghép→tự kiểm; các họ Hamming/góc/Euclid cung cấp phép thử cơ sở cụ thể.
- **Diễn giải học thuật, lời giải và tiêu chí:** Với $d=.2$, xác suất trùng ít nhất .7; với $d=.8$, xác suất trùng không quá .4. Tại $d=.5$, định nghĩa họ không đưa ra bảo đảm chung. AND 2 rồi OR 3 cho $1-(1-p^2)^3$ khi các phép thử độc lập. Hai vector $x,2x$ có góc 0; chúng biểu diễn cùng một hướng. Góc là metric trên các hướng hoặc trên vector đơn vị. Tiêu chí: giữ đúng hai cận và miền giữa, nêu độc lập, xác định đúng miền metric.
- **Nguồn:** B Ex 3.18 tr.105, Bài 3.6.1(a) tr.108, §3.5.4 tr.99; kiểm tra trực tiếp định nghĩa.
- **Ánh xạ ghi chú:** `N05,N06,N07`. **Thời lượng:** 3 phút.

### Phần 4. Các họ băm theo độ đo

#### lec06-s04-01 — Băm bằng một tọa độ

- **Mục đích và vai trò:** Chạy một hàm tọa độ trên vector cùng chiều.
- **Thông điệp:** Tọa độ được chọn quyết định hai vector có trùng giá trị băm.
- **Nội dung công khai dự kiến:** Tính metric chưa bảo đảm có họ LSH; mỗi độ đo cần một phép thử và chứng minh riêng. Chỉ số I12345 x10101 y11110 Trùng?CóKhôngCóKhôngKhông $h_I(x)=x_I$ I = 1Hai giá trị 1 và 1: trùng. I = 2Hai giá trị 0 và 1: khác. Cùng một chỉ số được dùng để băm mọi vector.
- **Đầu vào và giả thiết:** Hamming và khung họ; phép đọc phần tử mảng.
- **Dữ kiện, hình thức hóa và vết chạy:** V08; $D=5,d_H=3$; cùng $I$ cho cả hai vector.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai hàng bit trên 65% khung; các ô I=1, I=2 được đóng khung kèm chữ; dưới là hàm đọc tọa độ. Năm 2 thấy đầu vào/hàm/đầu ra trước công thức xác suất.
- **Kết nối vào–ra:** Định nghĩa metric chưa tự cung cấp họ LSH. Bắt đầu xây và kiểm riêng phép thử tọa độ cho Hamming; số vị trí trùng dẫn tới chứng minh đếm ở s04-02.
- **Diễn giải học thuật, lời giải và tiêu chí:** Một lần chọn $I$ định nghĩa một hàm cho toàn bộ dữ liệu. Mỗi lần tính chỉ đọc một tọa độ nếu truy cập mảng mất thời gian hằng. Chọn chỉ số riêng cho từng vector sẽ không tạo cùng một phép thử.
- **Nguồn:** B §3.7.1 tr.109/PDF 38; dữ kiện Ex 3.17 tr.101.
- **Ánh xạ ghi chú:** `N08`. **Thời lượng:** 2 phút.

#### lec06-s04-02 — Xác suất va chạm Hamming

- **Mục đích và vai trò:** Chứng minh xác suất bằng đếm tọa độ.
- **Thông điệp:** Tọa độ đều cho xác suất $1-d_H/D$.
- **Nội dung công khai dự kiến:** $D>0$;$I$ đều trong $\{1,\ldots,D\}$. Có $D-d_H(x,y)$ chỉ số trùng nên $\Pr[h_I(x)=h_I(y)]=(D-d_H)/D$. Dữ kiện: $2/5$. Nhiều phép thử lấy $I$ độc lập, có hoàn lại.
- **Đầu vào và giả thiết:** Số chỉ số trùng ở s04-01, phân phối đều.
- **Dữ kiện, hình thức hóa và vết chạy:** HT8; V08 trùng 2 trên 5. Họ hữu hạn không giới hạn số lần lấy mẫu độc lập.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng đếm tổng/khác/trùng bên trái 45%; phân số và giả thiết bên phải 55%. Năm 2 dùng xác suất hữu hạn để chứng minh; tránh đưa thêm đường cong.
- **Kết nối vào–ra:** Phép thử→bảo đảm; dữ liệu theo hướng cần một phép thử dùng tích vô hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Mỗi chỉ số có xác suất $1/D$, nên cộng trên $D-d_H$ chỉ số cho kết quả. Khi ghép, lấy có hoàn lại giúp các chỉ số độc lập. Chọn các chỉ số khác nhau không tự cho công thức $p^r$.
- **Nguồn:** B §3.7.1 tr.109; sửa diễn giải giới hạn số hàm độc lập của nguồn.
- **Ánh xạ ghi chú:** `N08`. **Thời lượng:** 2 phút.

#### lec06-s04-03 — Dấu của tích vô hướng

- **Mục đích và vai trò:** Tạo một bit bằng một pháp tuyến cố định.
- **Thông điệp:** Siêu phẳng qua gốc phân đối tượng theo dấu tích vô hướng.
- **Nội dung công khai dự kiến:** $x=(3,4,5,6)$ và $y=(4,3,2,1)$. $h_v(x)=\operatorname{sign}(v\cdot x)$, với $\operatorname{sign}(0)=+1$. Cho $v_1=(1,-1,1,1)$: $v_1\cdot x=3-4+5+6=10$, $v_1\cdot y=4-3+2+1=4$; hai vector cùng dấu $+$.
- **Đầu vào và giả thiết:** Tích vô hướng, vector V10 hiển thị đầy đủ; x=(3,4,5,6), y=(4,3,2,1).
- **Dữ kiện, hình thức hóa và vết chạy:** V10, HT9 cơ chế; pháp tuyến vuông góc siêu phẳng, khác đường chia trong hình hai chiều.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 55% hình siêu phẳng/pháp tuyến và hai miền dấu; phải 45% hai phép tính. Hình là lát hai chiều khái niệm, không gán tọa độ bốn chiều cho ảnh. Năm 2 tách đường chia với pháp tuyến; định lý ngẫu nhiên chờ s04-05.
- **Kết nối vào–ra:** Tọa độ đơn→phép thử theo hướng; nhiều pháp tuyến tạo chữ ký dấu.
- **Diễn giải học thuật, lời giải và tiêu chí:** Một pháp tuyến $v$ phải được giữ cố định khi băm mọi vector. Dấu bằng 0 có quy tắc thống nhất để hàm xác định. Vết số dùng pháp tuyến dấu của sách và chỉ minh họa phép tính, chưa thể hiện phân phối đẳng hướng.
- **Nguồn:** B §3.7.2–3/Ex 3.22 tr.109–111; S4 PDF 48/trang in 51; hình pháp tuyến.
- **Ánh xạ ghi chú:** `N09`. **Thời lượng:** 2.5 phút.

#### lec06-s04-04 — Chữ ký dấu và góc ước lượng

- **Mục đích và vai trò:** Tính chữ ký nhiều bit và đối chiếu góc thật.
- **Thông điệp:** Chữ ký ngắn có thể cho góc ước lượng khác xa góc thật.
- **Nội dung công khai dự kiến:** $x=(3,4,5,6),\quad y=(4,3,2,1)$ Pháp tuyếnTích với xTích với yHai dấu $v_1=(1,-1,1,1)$104+, + $v_2=(-1,1,-1,1)$2-2+, − $v_3=(1,1,-1,-1)$-44−, + Đẳng hướng cho $p_{\ne}=\theta/\pi$; quy tắc ước lượng là $\widehat\theta=\pi\widehat p_{\ne}$, với $\widehat p_{\ne}$ là tỷ lệ bit khác. $\widehat\theta=\pi\cdot\frac23=120^\circ,\qquad\theta\approx38.05^\circ$ Ba pháp tuyến dấu cố định minh họa phép tính; chúng không có phân phối đẳng hướng.
- **Đầu vào và giả thiết:** Hàm dấu và tích vô hướng đã có. Nêu quan hệ p_khác=theta/pi dưới pháp tuyến đẳng hướng và quy tắc theta_hat=pi nhân tỷ lệ bit khác trước phép đổi 2/3 thành 120 độ. Các pháp tuyến dấu trong bảng vẫn là dữ kiện cố định.
- **Dữ kiện, hình thức hóa và vết chạy:** V10; $x\cdot y=40$, chuẩn bình phương 86 và 30. Ba pháp tuyến là mẫu cố định dấu ±1.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 3 hàng pháp tuyến/tích x/tích y/dấu trùng ở giữa; so hai góc dưới. Năm 2 theo đủ trung gian rồi đối chiếu; góc thật bằng arccos và toàn 16 pháp tuyến vào notes.
- **Kết nối vào–ra:** Vết một dấu → ba dấu và quy tắc ước lượng có phạm vi xác định → chứng minh hình học của mô hình đẳng hướng ở s04-05. Giữ thứ tự trang.
- **Diễn giải học thuật, lời giải và tiêu chí:** Với pháp tuyến đẳng hướng, xác suất khác dấu $p_{\ne}=\theta/\pi$. Thay xác suất bằng tỷ lệ bit khác quan sát được cho quy tắc $\widehat\theta=\pi\widehat p_{\ne}$. Ba pháp tuyến dấu ở bảng là dữ kiện cố định; áp quy tắc này chỉ tạo một giá trị ước lượng, không nhận bảo đảm của mô hình đẳng hướng. Quan hệ xác suất được chứng minh bằng hình học ở phần siêu phẳng. $\theta=\arccos(40/\sqrt{86\cdot30})\approx38.047579^\circ$. Có hai nguồn khác biệt: mẫu hữu hạn và pháp tuyến dấu ±1 không đẳng hướng. Nếu xét đủ 16 vector dấu với sign (0)=+1, có 4 trường hợp trái dấu nên góc ước lượng 45°, vẫn khác góc thật.
- **Nguồn:** B §3.7.3/Ex 3.22 tr.111/PDF 40.
- **Ánh xạ ghi chú:** `N09`. **Thời lượng:** 2.5 phút.

#### lec06-s04-05 — Xác suất cùng phía siêu phẳng

- **Mục đích và vai trò:** Nêu điều kiện và bước hình học của xác suất góc.
- **Thông điệp:** Pháp tuyến đẳng hướng cho xác suất cùng dấu $1-\theta/\pi$.
- **Nội dung công khai dự kiến:** $x,y\ne0$; hướng pháp tuyến ngẫu nhiên đẳng hướng; cùng $h$ cho mọi vector. Góc $\theta\in[0,\pi]$ đo radian. Hai miền pháp tuyến làm khác dấu có tổng góc $2\theta$ trên $2\pi$. $\Pr[h(x)=h(y)]=1-\theta/\pi$. Với $\theta=\pi/3$:2/3.
- **Đầu vào và giả thiết:** Khoảng cách góc N05; dấu, pháp tuyến và siêu phẳng.
- **Dữ kiện, hình thức hóa và vết chạy:** HT9; V06 đổi 60° thành $\pi/3$; V10 là phân phối khác được ghi rõ.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình lớn 70% trên: hai vector cố định, hai vùng tách dùng nét gạch và nhãn; công thức/giả thiết dưới 30%. Năm 2 thấy tỷ phần góc trước xác suất; proof chiếu về mặt phẳng trong notes.
- **Kết nối vào–ra:** Chữ ký dấu hữu hạn→mô hình bảo đảm; Euclid cần thêm thông tin độ dài.
- **Diễn giải học thuật, lời giải và tiêu chí:** Nếu $\theta=0$, hai vector cùng hướng và cùng dấu với xác suất 1. Nếu $\theta=\pi$, chúng đối hướng và khác dấu với xác suất 1, nên xác suất trùng bằng 0; trường hợp tích vô hướng bằng 0 có xác suất 0 dưới phân phối liên tục đẳng hướng. Khi $0<\theta<\pi$, hai vector không cùng phương và sinh một mặt phẳng. Tính đẳng hướng làm hướng pháp tuyến chiếu vào mặt phẳng này có phân phối đều. Các hướng tách hai vector chiếm tỷ lệ $\theta/\pi$; lấy bù được xác suất cùng dấu. Quy tắc dấu tại 0 vẫn được cố định để hàm xác định.
- **Nguồn:** B §3.7.2/Hình 3.13 tr.109–110; S4 PDF 49/trang in 52.
- **Ánh xạ ghi chú:** `N09`. **Thời lượng:** 3 phút.

#### lec06-s04-06 — Chiếu điểm vào các khoảng

- **Mục đích và vai trò:** Gán thùng theo một trục cố định bằng hàm sàn.
- **Thông điệp:** Phép chiếu biến vector thành một tọa độ để chia khoảng.
- **Nội dung công khai dự kiến:** Dữ kiện: $p_1=(1,2,3),p_2=(0,2,4),p_3=(4,3,2)$. Chỉ xét trục thứ nhất và $a=1$: các tọa độ 1,0,4; thùng [1,2), [0,1), [4,5); mã 1,0,4. Biên trái đóng, phải mở.
- **Đầu vào và giả thiết:** Chuẩn Euclid, phép chiếu và hàm sàn.
- **Dữ kiện, hình thức hóa và vết chạy:** Bài 3.7.5 giữ dữ kiện; chỉ minh họa một trục, a=1. Chưa giải hai trục khác/a=2.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Đường số có khoảng rộng 1 chiếm 60% trên, bảng điểm/tọa độ/mã dưới. Năm 2 thấy điểm đúng biên thuộc khoảng nào; notes phân biệt trục cố định với hướng ngẫu nhiên.
- **Kết nối vào–ra:** Góc bỏ độ dài→lượng tử hóa hình chiếu; biên khoảng đòi đặc tả dịch ngẫu nhiên.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hàm theo trục thứ nhất là $h_1(x)=\lfloor x_1/a\rfloor$. Với ba điểm đã cho và $a=1$, các mã ở trục thứ nhất là 1,0,4 nên chưa tạo cặp. Đây là thực thi trên trục cố định của bài tập nguồn, không là phép kiểm bảo đảm xác suất của họ hướng ngẫu nhiên.
- **Nguồn:** B §3.7.4 tr.111–113; Bài 3.7.5(a) tr.114/PDF 43, phần minh họa đã duyệt.
- **Ánh xạ ghi chú:** `N10`. **Thời lượng:** 2 phút.

#### lec06-s04-07 — Họ chiếu với dịch ngẫu nhiên

- **Mục đích và vai trò:** Đặc tả nguồn ngẫu nhiên và mã thùng Euclid.
- **Thông điệp:** Dịch đều của biên khoảng cho xác suất theo khoảng cách hình chiếu.
- **Nội dung công khai dự kiến:** Trong $\mathbb R^2$:$u$ đều hướng đơn vị;$a>0$;$\delta\sim\operatorname{Unif}[0,a)$ độc lập. $h_{u,\delta}(x)=\lfloor(u\cdot x+\delta)/a\rfloor$. Cùng $(u,\delta)$ cho mọi điểm. Biên trên trục hình chiếu:$ka-\delta$.
- **Đầu vào và giả thiết:** Phép chiếu chia khoảng, hàm sàn; nguồn ngẫu nhiên của họ.
- **Dữ kiện, hình thức hóa và vết chạy:** HT10; u, hướng; δ, dịch; a, độ rộng; D=2. Không dùng t cho dịch.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình trục chiếu với biên dịch ở trên 60%; công thức và ba tham số dưới 40%. Năm 2 phân biệt đổi hướng với dời lưới; phần attribution Datar ở notes, không đưa p-stable.
- **Kết nối vào–ra:** Thực thi một trục→họ ngẫu nhiên; cố định hướng để tính xác suất theo dịch.
- **Diễn giải học thuật, lời giải và tiêu chí:** Phép dịch tránh việc một biên cố định luôn tách một cặp gần nằm hai phía biên ấy. Công thức lượng tử hóa với dịch đều được đối chiếu Datar §3.2; hướng đơn vị đều trong mặt phẳng và cận hai chiều là mô hình MMDS được hoàn thiện giả thiết.
- **Nguồn:** B §3.7.4 tr.111–113; D §3.2PDF 3; bổ sung đã được điều phối viên duyệt.
- **Ánh xạ ghi chú:** `N10`. **Thời lượng:** 2.5 phút.

#### lec06-s04-08 — Xác suất chung khoảng chiếu

- **Mục đích và vai trò:** Tính xác suất theo dịch bằng độ dài phần biên chia cặp.
- **Thông điệp:** Khoảng cách hình chiếu quyết định phần dịch làm hai điểm khác thùng.
- **Nội dung công khai dự kiến:** Cố định $u$, đặt $\ell=|u\cdot(x-y)|$. Nếu $0\le\ell<a$, biên tách hai hình chiếu chiếm độ dài $\ell$ trong chu kỳ $a$. $\Pr_\delta[h(x)=h(y)\mid u]=\max(0,1-\ell/a)$.
- **Đầu vào và giả thiết:** HT10, phân phối đều của $\delta$, độ dài chu kỳ.
- **Dữ kiện, hình thức hóa và vết chạy:** Trường hợp $\ell=0$ cho 1; $\ell\ge a$ cho 0; chiều dài không âm. Không tự thêm dữ kiện thực nghiệm.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình một chu kỳ $a$, chỉ đoạn $\ell$ có biên tách ở trên 65%; công thức dưới 35%. Năm 2 chuyển độ dài sang xác suất bằng chia $a$; proof và trường biên trong notes.
- **Kết nối vào–ra:** Đặc tả ngẫu nhiên→xác suất có điều kiện; cận chiếu nối tới khoảng cách Euclid.
- **Diễn giải học thuật, lời giải và tiêu chí:** Khi $\ell<a$, vị trí biên modulo $a$ đều trên một chu kỳ; hai điểm khác thùng đúng khi biên rơi giữa chúng, trừ điểm biên xác suất 0. Khi $\ell\ge a$, hai điểm không thể chung một khoảng nửa mở rộng $a$. Công thức thống nhất cả hai trường hợp.
- **Nguồn:** B §3.7.4; điều kiện dịch từ D §3.2; chứng minh hình học của bản soạn, đã duyệt.
- **Ánh xạ ghi chú:** `N10`. **Thời lượng:** 2.5 phút.

#### lec06-s04-09 — Cận xác suất trong mặt phẳng

- **Mục đích và vai trò:** Suy hai cận với đúng miền hai chiều.
- **Thông điệp:** Họ chiếu hai chiều có bộ tham số $(a/2,2a,1/2,1/3)$.
- **Nội dung công khai dự kiến:** Trong $\mathbb R^2$, $u$ đều hướng; $\delta$ đều trên $[0,a)$, độc lập với $u$. Cặp gần: $\rho=\|x-y\|_2\le a/2$, $\ell\le\rho$. $P\ge1-\rho/a\ge1/2$ Cặp xa: ρ ≥ 2a$\phi\in[0,\pi/2]$ là góc nhọn với trục chiếu. $\ell=\rho|\cos\phi|$ Chung thùng cần $\ell<a$, nên $|\cos\phi|<a/\rho\le1/2$. Do đó $\phi>\pi/3$; $\phi$ đều trên $[0,\pi/2]$. $P\le\frac{\pi/2-\pi/3}{\pi/2}=1/3$ Họ chiếu hai chiều: (a/2, 2a, 1/2, 1/3).
- **Đầu vào và giả thiết:** Công thức va chạm theo độ dài chiếu ell ở s04-08; u đều trong mặt phẳng và delta đều độc lập. Quan hệ ell=rho|cos phi| được thiết lập trực tiếp trên trang này.
- **Dữ kiện, hình thức hóa và vết chạy:** Hình tam giác nối rho, ell và phi. Gần dùng ell≤rho. Xa cần ell<a; rho≥2a suy |cos phi|<1/2 và phi>pi/3, rồi chặn bằng tỷ lệ miền góc đều. Không dùng điều kiện cần như điều kiện đủ.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai cột: trái là SVG hinh-chieu-euclid.svg và cận gần; phải là chuỗi cận xa. Hình ghi rho, ell, phi, trục u, đường vuông góc nét đứt; không ấn định tỷ lệ rho với độ rộng a. Nhãn font 32–38 trong viewBox 610×335; giữ thang chữ chung.
- **Kết nối vào–ra:** Xác suất theo $\ell$→bảo đảm theo $\rho$; cùng khung họ cho phép so chi phí ba phép thử.
- **Diễn giải học thuật, lời giải và tiêu chí:** Với cặp xa $\rho\ge2a>0$, $\phi\in[0,\pi/2]$ là góc nhọn giữa trục chiếu $u$ và đường thẳng theo $x-y$. Cận gần đúng với mọi hướng nên cũng đúng khi lấy trung bình theo $u$. Với cặp xa, hình chiếu có độ dài $\ell=\rho|\cos\phi|$. Chung thùng cần $\ell<a$, nên $|\cos\phi|<a/\rho\le1/2$, tức $\phi>\pi/3$. Điều kiện góc là cần, chưa đủ cho chung thùng, vì vậy kết quả là cận trên. Hình tam giác chỉ biểu diễn quan hệ chiếu; nó không đặt một tỷ lệ cố định giữa $\rho$ và $a$. Tính đều của góc nhọn dùng đúng hai chiều; không chuyển hằng số 1/3 sang mọi chiều.
- **Nguồn:** B §3.7.4 tr.112–113/Hình 3.14; S4 PDF 57–58; giả thiết và proof bổ sung đã duyệt.
- **Ánh xạ ghi chú:** `N10`. **Thời lượng:** 3 phút.

#### lec06-s04-10 — Chi phí các phép băm cơ sở

- **Mục đích và vai trò:** So công việc trên cùng mô hình vector đã có.
- **Thông điệp:** Chi phí mỗi phép thử phụ thuộc lượng tọa độ được đọc.
- **Nội dung công khai dự kiến:** Vector $D$ chiều, mỗi tọa độ một từ, truy cập ngẫu nhiên $O(1)$. Tọa độ Hamming: đọc 1 giá trị,$O(1)$. Dấu/chiếu với vector đặc: đọc $D$ giá trị, tích vô hướng $O(D)$. Với $m$ phép thử, lưu $m$ giá trị/đối tượng; thùng và kiểm ứng viên tính riêng.
- **Đầu vào và giả thiết:** Các hàm cơ sở và mô hình chi phí N04.
- **Dữ kiện, hình thức hóa và vết chạy:** Suy đếm trực tiếp từ $h_I$, $h_u$, $h_{u,\delta}$; vector đặc là điều kiện. Không gán $O(1)$ cho tích vô hướng $D$ chiều.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 3 hàng phép thử/đọc/chi phí; dòng $m$ phía dưới. Năm 2 so cùng biểu diễn và phạm vi, không nhầm chi phí băm với toàn thuật toán; chi tiết bộ nhớ pháp tuyến ở notes.
- **Kết nối vào–ra:** Các bảo đảm→chi phí thực hiện; kiểm tra phần yêu cầu giữ đúng giả thiết.
- **Diễn giải học thuật, lời giải và tiêu chí:** Lưu $m$ pháp tuyến đặc cần $O(mD)$ từ; các hàm tọa độ chỉ cần $m$ chỉ số. Tính chữ ký cho $C$ vector có chi phí $O(Cm)$ với Hamming hoặc $O(CmD)$ với dấu/chiếu đặc. Đây là phép đếm từ đặc tả hàm, còn phát cặp vẫn phụ thuộc $Q,K$.
- **Nguồn:** B §3.7.1–4 tr.109–113; suy chi phí từ công thức nguồn.
- **Ánh xạ ghi chú:** `N08,N09,N10`. **Thời lượng:** 1.5 phút.

#### lec06-s04-11 — Kiểm tra các họ theo độ đo

- **Mục đích và vai trò:** Tính một xác suất và xác định điều kiện của hai bảo đảm hình học.
- **Thông điệp:** Mỗi công thức va chạm gắn với một phép lấy mẫu cụ thể.
- **Nội dung công khai dự kiến:** Câu hỏi: Với 10101 và 11110, tính xác suất trùng của tọa độ đều. Với góc $60^\circ$, tính xác suất cùng dấu dưới pháp tuyến đẳng hướng. Một phép chiếu theo trục cố định có đủ để dùng cận $(a/2,2a,1/2,1/3)$ hay không; nêu hai nguồn ngẫu nhiên cần có.
- **Đầu vào và giả thiết:** V08, V06, HT8–HT10.
- **Dữ kiện, hình thức hóa và vết chạy:** Đáp án 2/5;60°=π/3→2/3; u đều hai chiều, δ đều độc lập. Không giải thêm V11 các trục còn lại.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba nhiệm vụ một cột, rộng 90%; dữ kiện tách dòng công thức. Năm 2 kiểm không chỉ phép thế mà cả điều kiện; đáp án giữ ở notes.
- **Kết nối vào–ra:** Chi phí/họ→kiểm tra; ứng dụng sẽ chọn lại biểu diễn và quy tắc sinh cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hai vector Hamming khác tại vị trí 2,4,5 nên có hai vị trí trùng trong năm vị trí; xác suất bằng $2/5$. Góc $60^\circ=\pi/3$ cho xác suất cùng dấu $1-(\pi/3)/\pi=2/3$ khi pháp tuyến đẳng hướng. Cận Euclid đang xét cần hướng đơn vị đều trong mặt phẳng và dịch đều trên $[0,a)$ độc lập với hướng; một trục cố định không đủ. Tiêu chí: tính đúng xác suất và đơn vị góc, nêu đủ hai nguồn ngẫu nhiên cùng miền hai chiều.
- **Nguồn:** B Ex 3.17, Ex 3.14, §3.7.1–4; kiểm trực tiếp dữ kiện/giả thiết đã học.
- **Ánh xạ ghi chú:** `N08,N09,N10`. **Thời lượng:** 2.5 phút.

### Phần 5. Ứng dụng tìm cặp tương đồng

#### lec06-s05-01 — Đối sánh thực thể

- **Mục đích và vai trò:** Tách tạo ứng viên theo trường với quyết định cùng thực thể.
- **Thông điệp:** Khớp một trường tạo cặp cần xét, chưa xác nhận cùng người.
- **Nội dung công khai dự kiến:** Hai nguồn, mỗi nguồn một triệu hồ sơ; đối chiếu trực tiếp cần 10¹² cặp. Khớp ít nhất một trường tạo ứng viên; điểm tổng hợp quyết định tập kết quả. Trường phụ không tham gia tính điểm có thể dùng kiểm chứng chất lượng kết quả.
- **Đầu vào và giả thiết:** OR, khử lặp, xác minh; không giả định ba trường độc lập xác suất.
- **Dữ kiện, hình thức hóa và vết chạy:** B §3.8: quy mô và tên trường nguồn; không tự tạo hồ sơ người. Mô hình điểm/ngày chỉ đọc thêm.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ hai nguồn→ba nhánh khóa→hợp ứng viên→chấm điểm chiếm 75%; câu giới hạn dưới. Năm 2 nhận cấu trúc OR đã biết trong miền mới; không đưa bảng hồ sơ tự đặt.
- **Kết nối vào–ra:** Họ cơ sở→ứng dụng có quy tắc khớp riêng; vân tay cung cấp mô hình xác suất cụ thể.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tên hoặc địa chỉ có thể trùng ở các người khác nhau. Ví dụ sách dùng khoảng cách chỉnh sửa để tính điểm phạt sai khác ở từng trường, rồi hiệu chỉnh theo các bảng tên tương đương. Như vậy, khóa khớp hoàn toàn tạo ứng viên; độ sai khác giữa chuỗi tham gia chấm điểm để xác minh. Một trường phụ không tham gia điểm có thể được dùng kiểm chất lượng tập cặp theo mô hình phù hợp; nó không xác nhận từng cặp. Chưa có phân phối các hồ sơ nên chưa gán bốn tham số LSH cho ba trường.
- **Nguồn:** B §3.8.1–3 tr.114–117/PDF 43–46.
- **Ánh xạ ghi chú:** `N11`. **Thời lượng:** 3 phút.

#### lec06-s05-02 — Biểu diễn và thùng vân tay

- **Mục đích và vai trò:** Nêu quy tắc băm bằng ba ô đã chọn.
- **Thông điệp:** Chỉ ảnh chứa đặc trưng ở cả ba ô mới vào thùng chung.
- **Nội dung công khai dự kiến:** Ảnh đã chuẩn hóa được biểu diễn bằng tập ô có đặc trưng. Đặc trưng: nơi đường vân kết thúc hoặc các đường vân nhập vào nhau. Chọn ba ô từ lưới trước khi xét ảnh. Ảnh có đủ ba ô vào thùng chung. Mỗi ảnh thiếu ô nhận thùng đơn riêng. Một cặp trùng phép thử khi cả hai ảnh cùng chứa đủ ba ô.
- **Đầu vào và giả thiết:** Đặc trưng vân tay là nơi đường vân kết thúc hoặc nhập vào nhau; chuẩn hóa kích thước và hướng trước biểu diễn bằng tập ô. Không giả định sinh viên biết xử lý ảnh.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; lưới chỉ là sơ đồ khái niệm, không là dữ liệu ảnh thực. Singleton cho ảnh thiếu ô bảo đảm không va chạm với nhau.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Lưới ba ô đánh dấu bằng số/viền trái 50%; quy tắc hai nhánh thùng chung/thùng đơn phải 50%. Năm 2 tránh nhầm “không đạt” là một thùng 0 chung; không dùng ảnh raster.
- **Kết nối vào–ra:** Ứng dụng thực thể thiếu mô hình→họ vân tay cụ thể; các giả thiết 0.2/0.8 cho xác suất cơ sở.
- **Diễn giải học thuật, lời giải và tiêu chí:** Một đặc trưng vân tay là vị trí đường vân kết thúc hoặc các đường vân nhập vào nhau. Chuẩn hóa kích thước và hướng khiến cùng ô có ý nghĩa so sánh giữa ảnh. Phép băm của sách gom những ảnh chứa cả ba đặc trưng; các ảnh khác được tách thành các thùng đơn. Nếu gộp tất cả ảnh thiếu ô vào cùng thùng, xác suất va chạm sẽ khác mô hình được tính sau đó.
- **Nguồn:** B §3.8.4–5 tr.117–118/PDF 46–47.
- **Ánh xạ ghi chú:** `N12`. **Thời lượng:** 2.5 phút.

#### lec06-s05-03 — Xác suất cơ sở của mô hình vân tay

- **Mục đích và vai trò:** Tính xác suất một phép thử nhận hai loại cặp.
- **Thông điệp:** Mô hình xác suất cho hai xác suất cơ sở khác nhau.
- **Nội dung công khai dự kiến:** Mô hình: mỗi ô có đặc trưng với xác suất 0.2. Với hai ảnh cùng ngón, xác suất ảnh thứ hai có đặc trưng tại ô đã có ở ảnh thứ nhất là 0.8. Cặp ảnhCùng có một ôCùng có đủ ba ô Khác ngón$.2^2=.04$$q_F=.04^3=.000064$ Cùng ngón$.2\cdot.8=.16$$q_T=.16^3=.004096$ Các ô và phép thử độc lập theo mô hình; đây không phải số đo thực nghiệm. Ba ô được chọn từ lưới trước khi xét ảnh; không điều kiện hóa ảnh truy vấn đã có ba ô.
- **Đầu vào và giả thiết:** Xác suất có điều kiện, ba ô cùng đạt; quy tắc thùng s05-02.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; một ô cùng ngón=.16, khác ngón=.04; rồi lũy thừa 3. Không đổi 0.8 thành xác suất vô điều kiện.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng hai hàng loại cặp/xác suất một ô/xác suất ba ô. Giả thiết trên bảng. Năm 2 theo hai tầng nhân, phân biệt điều kiện 0.8 và xác suất chung 0.16; notes ghi phạm vi mô hình.
- **Kết nối vào–ra:** Quy tắc thùng→xác suất cơ sở; xác suất nhỏ cần ghép nhiều phép thử để giảm bỏ sót.
- **Diễn giải học thuật, lời giải và tiêu chí:** Gọi $E_1,E_2$ là sự kiện ảnh thứ nhất, thứ hai có đặc trưng tại ô đang xét. Với hai ảnh cùng ngón, Ví dụ 3.23 giả định $\Pr(E_1)=.2$ và $\Pr(E_2\mid E_1)=.8$, nên $\Pr(E_1\cap E_2)=.16$. Phép nhân ba ô và phép ghép nhiều thử tiếp theo dựa trên mô hình độc lập của sách. Dùng chung ảnh hoặc chọn các bộ ba khác nhau không tự chứng minh độc lập trong dữ liệu thực. Ba ô được chọn từ lưới trước khi xét ảnh; không điều kiện hóa rằng ảnh truy vấn đã chứa cả ba ô ấy. Xác suất $q_T,q_F$ là xác suất cả hai ảnh cùng chứa đủ ba ô được chọn.
- **Nguồn:** B Ex 3.23/ §3.8.5 tr.118–120/PDF 47–49.
- **Ánh xạ ghi chú:** `N12`. **Thời lượng:** 3 phút.

#### lec06-s05-04 — Phép ghép trong đối sánh vân tay

- **Mục đích và vai trò:** Tính và so sai số của OR 1024 với AND hai nhóm.
- **Thông điệp:** Tăng tính chọn lọc bằng AND làm tăng bỏ sót theo mô hình.
- **Nội dung công khai dự kiến:** Cấu trúcPhép thửỨng viên giảBỏ sót OR 10241024.063436634.014951892 AND hai nhóm OR 10242048.004024207.029680224 $P_F=[1-(1-q_F)^{1024}]^2$ $P_{\rm miss}=1-[1-(1-q_T)^{1024}]^2$ Phép AND giảm ứng viên giả nhưng tăng bỏ sót; hai hàng có ngân sách khác nhau.
- **Đầu vào và giả thiết:** q_F, q_T ở trang trước, AND/OR độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; phép ghép dùng số chưa làm tròn; hai nhóm tổng 2048 phép thử, khác ngân sách OR 1024.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai cột cấu trúc/bảng xác suất; mỗi cột ghi rõ số hàm cơ sở. Năm 2 so đánh đổi nhưng thấy ngân sách khác nhau; chi tiết 1−(1−FN)^2 ở notes.
- **Kết nối vào–ra:** Xác suất ba ô → khuếch đại; ứng dụng khung OR–AND qua hợp mã ảnh trong từng nhóm, giao hai hợp rồi xác minh. Với tìm mọi cặp, hợp/giao trên tập cặp phát từ thùng. Sau đó bản tin thay biểu diễn thay vì thay phép ghép.
- **Diễn giải học thuật, lời giải và tiêu chí:** Với một ảnh truy vấn, hợp các mã ảnh trong những thùng phù hợp của nhóm OR thứ nhất; làm tương tự ở nhóm thứ hai; lấy giao hai hợp rồi so ảnh với các ứng viên còn lại. Các phép hợp và giao xử lý mã ảnh, còn xác minh vân tay có chi phí riêng. Khi tìm mọi cặp trong kho, phát cặp từ các thùng, hợp trong từng nhóm OR rồi giao hai tập cặp. Các xác suất ở đây vẫn xét cả hai ảnh trước khi biết chúng chứa những ô nào. AND hai nhóm giữ xác suất nhận cùng ngón là $[1-(1-q_T)^{1024}]^2$, nên bỏ sót là một trừ giá trị đó. Xác suất ứng viên giả là bình phương của $1-(1-q_F)^{1024}$. Sách dùng 0.063 đã làm tròn nên cho 0.00397; tính từ tham số gốc cho 0.004024207. Đây là xác suất theo mô hình hai loại cặp, không là đo hiệu năng một hệ nhận dạng.
- **Nguồn:** B §3.8.5/Ex 3.23 tr.118–120/PDF 47–49.
- **Ánh xạ ghi chú:** `N12`. **Thời lượng:** 3 phút.

#### lec06-s05-05 — Shingle cho bản tin gần trùng

- **Mục đích và vai trò:** Áp dụng quy tắc từ dừng để chọn đặc trưng văn bản chính.
- **Thông điệp:** Biểu diễn phải phù hợp với tiêu chuẩn cùng văn bản.
- **Nội dung công khai dự kiến:** Từ dừng là từ xuất hiện rất thường xuyên. Ví dụ dùng: I, that, you, for, your. Mỗi shingle gồm một từ dừng và hai token tiếp theo. Buy Sudzo.Không có token từ dừng → không có shingle. I recommend that you buy Sudzo for your laundry.“I recommend that” · “that you buy” “you buy Sudzo” · “for your laundry” Quy tắc ưu tiên văn xuôi; câu dài cũng có thể là quảng cáo. “your laundry x” còn phụ thuộc token tiếp theo x chưa được cho. Mục tiêu là cùng văn bản, không chỉ cùng chủ đề.
- **Đầu vào và giả thiết:** Từ dừng là từ rất thường gặp; danh sách ví dụ I, that, you, for, your. Shingle lấy từ dừng và hai token kế tiếp. Token sau laundry chưa được cho.
- **Dữ kiện, hình thức hóa và vết chạy:** that + you + buy → that you buy. Buy Sudzo không có từ dừng trong danh sách. Câu dài có bốn shingle xác định và your laundry x chưa xác định x. Mật độ từ dừng cao hơn trong văn xuôi của tình huống nguồn giải thích mục đích biểu diễn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trên là hai đoạn nguồn, dưới là bảng vị trí từ dừng/shingle; phân biệt quảng cáo 0 shingle và câu văn bằng nhãn. Năm 2 chạy đúng quy tắc trên token; không dịch dữ kiện rồi dùng danh sách từ dừng tiếng Anh.
- **Kết nối vào–ra:** Ứng dụng phép ghép→lựa chọn đặc trưng; kiểm tra phần nối biểu diễn với ý nghĩa kết quả.
- **Diễn giải học thuật, lời giải và tiêu chí:** Danh sách từ dừng của ví dụ gồm I, that, you, for, your. Từ “that” và hai token theo sau tạo shingle “that you buy”. Câu ngắn “Buy Sudzo.” không có từ dừng trong danh sách này nên không tạo shingle. Câu dài “I recommend that you buy Sudzo for your laundry.” cũng có thể dùng làm lời quảng cáo và vẫn tạo các shingle đã liệt kê. Trong tình huống nguồn, văn xuôi có mật độ từ dừng cao hơn quảng cáo hoặc tiêu đề, nên đóng góp nhiều shingle hơn. Quy tắc không bảo đảm loại mọi quảng cáo. Các tập shingle ở đây chỉ thuộc những đoạn minh họa được cho. Sách còn ghi “your laundry x”, trong đó $x$ là từ theo sau câu, chưa được cung cấp.
- **Nguồn:** B §3.8.6/Ex 3.24 tr.120–121/PDF 49–50.
- **Ánh xạ ghi chú:** `N13`. **Thời lượng:** 2.5 phút.

#### lec06-s05-06 — Kiểm tra điều kiện của ứng dụng

- **Mục đích và vai trò:** Phát hiện điều kiện thiếu trong việc diễn giải ứng viên.
- **Thông điệp:** Biểu diễn và bước kiểm cuối xác định ý nghĩa của kết quả.
- **Nội dung công khai dự kiến:** Câu hỏi: Nêu bước còn thiếu sau khi hai hồ sơ khớp số điện thoại. Với phép thử ba ô vân tay, các ảnh thiếu ô được gán thùng thế nào. Quy tắc shingle theo từ dừng ở ví dụ bản tin nhằm tìm cùng văn bản hay mọi bài về cùng sự kiện?
- **Đầu vào và giả thiết:** Ba cơ chế s05-01–05.
- **Dữ kiện, hình thức hóa và vết chạy:** Không thêm dữ kiện; đối chiếu quy tắc nguyên nguồn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba nhiệm vụ trong một khối; mỗi nhiệm vụ ghi tên miền để tránh đổi ngữ cảnh ngầm. Năm 2 phân biệt đối tượng/ứng viên/kết quả, đáp án ở notes.
- **Kết nối vào–ra:** Ba ứng dụng→kiểm tra; tổng kết thu hồi toàn quy trình chọn và kiểm cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: một số điện thoại có thể được nhiều người dùng chung, nên khớp điện thoại chỉ tạo ứng viên và cần chấm điểm hoặc xác minh hồ sơ. Nếu gom mọi ảnh thiếu ô vào một thùng, các ảnh ấy cũng va chạm dù không cùng có đủ ba ô, trái với sự kiện đang được tính xác suất. Quảng cáo dài vẫn có thể chứa từ dừng và tạo shingle; câu “I recommend that you buy Sudzo for your laundry.” là một ví dụ. Tiêu chí: phân biệt khớp khóa với cùng thực thể, giữ đúng mô hình thùng và không coi từ dừng là bộ lọc mọi quảng cáo.
- **Nguồn:** B §3.8.1–6 tr.114–121; kiểm quy tắc nguồn.
- **Ánh xạ ghi chú:** `N11,N12,N13`. **Thời lượng:** 2 phút.

### Phần 6. Tổng kết và tự kiểm tra

#### lec06-s06-01 — Quy trình tìm cặp tương đồng

- **Mục đích và vai trò:** Ghép các thành phần thành một quy trình có điều kiện.
- **Thông điệp:** Biểu diễn, phép thử và xác minh phải cùng thực hiện một đặc tả.
- **Nội dung công khai dự kiến:** Sơ đồ: đối tượng→biểu diễn và độ đo→họ cơ sở→phép ghép→thùng→cặp duy nhất→xác minh. Kho triệu tài liệu nhận lại SIG ở đầu bước chọn cặp. Đầu ra được kiểm theo ngưỡng trên biểu diễn gốc.
- **Đầu vào và giả thiết:** N01–N13; không có khái niệm mới.
- **Dữ kiện, hình thức hóa và vết chạy:** V01 gợi lại C=10^6; không đưa con số K cho kho chưa có phân bố.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ một hàng hai tầng để nhãn đọc được; mỗi bước một danh từ/thao tác. Năm 2 cần nhận ra các quyết định nối nhau; ví dụ chi tiết không lặp trên mặt trang.
- **Kết nối vào–ra:** Ứng dụng→mẫu chung; chi phí và sai số quyết định tính phù hợp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Minh họa tài liệu dùng tập shingle, MinHash và phân dải; vân tay thay phép thử cơ sở; bản tin điều chỉnh biểu diễn. Cùng một khung ứng viên không khiến các bài toán có cùng tiêu chuẩn đúng.
- **Nguồn:** B §3.4.3 và §3.8, tr.95–96, 114–121.
- **Ánh xạ ghi chú:** `N14`. **Thời lượng:** 2 phút.

#### lec06-s06-02 — Giới hạn chi phí và sai số

- **Mục đích và vai trò:** Thu hồi hai điều kiện làm quy trình có ích.
- **Thông điệp:** Số cặp sinh và xác suất bỏ sót phải được đánh giá cùng nhau.
- **Nội dung công khai dự kiến:** $P(s)$ mô tả khả năng sinh một cặp; $Q$ đếm lượt phát; $K$ đếm cặp xác minh. Xấu nhất $K=\binom C2$. Kiểm gốc loại ứng viên dưới ngưỡng, còn cặp đạt ngưỡng chưa sinh vẫn bị bỏ sót. Bài 07 so chỉ mục theo chất lượng, thời gian và bộ nhớ.
- **Đầu vào và giả thiết:** HT2, HT3, mô hình chi phí N04.
- **Dữ kiện, hình thức hóa và vết chạy:** V01 và V02 giữ vai trò; không tự tuyên bố giảm cặp tuyến tính.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba ô P/Q/K cùng kích thước ở trên; giới hạn xấu nhất và xác minh dưới. Năm 2 phân biệt đại lượng xác suất với số đếm, không thêm công thức mới.
- **Kết nối vào–ra:** Quy trình→điều kiện sử dụng; sáu nhiệm vụ sau đo lại từng mục tiêu.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chi phí băm nhỏ chưa đủ nếu một số thùng chứa quá nhiều đối tượng. Thay tham số có thể giảm số cặp xa được nhận nhưng làm mất thêm cặp gần. Bài tiếp theo xét cách tổ chức chỉ mục với các tiêu chí đánh giá này.
- **Nguồn:** B §3.4.2–3, §3.6.3; sources/source.md, Bài 07.
- **Ánh xạ ghi chú:** `N14`. **Thời lượng:** 1.5 phút.

#### lec06-s06-03 — Tự kiểm tra thuật toán và mô hình

- **Mục đích và vai trò:** Phối hợp MT1–MT3 trên dữ kiện đã học.
- **Thông điệp:** Hợp đồng đầu ra và mô hình xác suất cần được phân biệt.
- **Nội dung công khai dự kiến:** Câu hỏi: (1) Với SIG hai hàng $(1,3,0,1)$,$(0,2,0,0)$ và $b=2,r=1$, nêu cặp phát lặp và $K$. (2) Viết xác suất bỏ sót của một cặp có Jaccard $s\ge t$ trong mô hình MinHash độc lập. (3) Với họ $(.3,.6,.7,.4)$, nêu cận được bảo đảm khi $d\ge.6$.
- **Đầu vào và giả thiết:** V02, HT3, HT6; toàn dữ kiện hiện trên trang.
- **Dữ kiện, hình thức hóa và vết chạy:** Nhiệm vụ 1→MT1;2→MT2;3→MT3.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba yêu cầu một cột, ma trận nhỏ kề yêu cầu 1. Năm 2 gọi lại thao tác trước công thức và cận; không để đáp án gợi ngay dưới câu hỏi.
- **Kết nối vào–ra:** Giới hạn→tự kiểm nửa đầu; trang sau kiểm phép ghép/họ/ứng dụng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: cặp $(1,4)$ phát hai lần, $K=3$. Với cặp đạt ngưỡng $s\ge t$, xác suất bỏ sót là $(1-s^r)^b$. Khi $d\ge0.6$, xác suất trùng không quá $0.4$. Tiêu chí: đếm cặp duy nhất, giữ giả thiết độc lập và điều kiện đạt ngưỡng, giữ chiều cận xa.
- **Nguồn:** B Ex 3.8, §3.4.2, Ex 3.18 tr.105; tổng hợp mục tiêu MT1–MT3.
- **Ánh xạ ghi chú:** `N14`. **Thời lượng:** 2.5 phút.

#### lec06-s06-04 — Tự kiểm tra phép ghép và ứng dụng

- **Mục đích và vai trò:** Phối hợp MT4–MT6 và nhận diện giới hạn của kết luận.
- **Thông điệp:** Kết quả số chỉ có ý nghĩa trong mô hình đã nêu.
- **Nội dung công khai dự kiến:** Câu hỏi: (4) Nêu sự khác nhau giữa $1-(1-p^4)^4$ và $[1-(1-p)^4]^4$. (5) Nêu điều kiện để xác suất cùng dấu bằng $1-\theta/\pi$. (6) Giải thích vì sao chung thùng ở phép thử vân tay vẫn cần xác minh.
- **Đầu vào và giả thiết:** V09, HT9, HT11.
- **Dữ kiện, hình thức hóa và vết chạy:** Nhiệm vụ 4→MT4;5→MT5;6→MT6. Sáu nhiệm vụ cuối bài phủ đủ mục tiêu.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba yêu cầu một cột; hai công thức đặt cùng dòng nếu đọc được, nếu không hai dòng cùng cỡ chữ. Năm 2 nối cấu trúc, phép lấy mẫu và ứng dụng; giữ lời giải ở notes.
- **Kết nối vào–ra:** Tự kiểm nửa đầu→nửa sau; bài tập nguồn cung cấp vết chạy đầy đủ hơn.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: công thức thứ nhất AND 4 rồi OR 4, công thức thứ hai đảo thứ tự; các phép thử độc lập. Công thức góc cần vector khác 0, pháp tuyến đẳng hướng, cùng hàm và $\theta$ đo bằng radian. Cặp khác ngón vẫn có xác suất chung thùng theo mô hình nên cần so ảnh. Tiêu chí: nêu đủ cấu trúc/giả thiết và tầng quyết định.
- **Nguồn:** B Ex 3.19–20, §3.7.2, §3.8.5; tổng hợp MT4–MT6.
- **Ánh xạ ghi chú:** `N14`. **Thời lượng:** 2 phút.

### Phần 7. Bài tập vận dụng

#### lec06-s07-01 — Bảng xác suất tạo ứng viên

- **Mục đích và vai trò:** Tính đủ bảng xác suất của Bài 3.4.1.
- **Thông điệp:** Tham số dải quyết định đường xác suất cho từng giá trị tương đồng.
- **Nội dung công khai dự kiến:** Câu hỏi: Với $s=0.1,0.2,\ldots,0.9$, tính $P(s)=1-(1-s^r)^b$ cho ba cấu hình $(r,b)=(3,10),(6,20),(5,50)$. Sản phẩm: bảng 9 hàng × 3 cột xác suất. Có thể dùng máy tính cho lũy thừa.
- **Đầu vào và giả thiết:** HT3; giữ nguyên cả ba cấu hình và chín giá trị $s$.
- **Dữ kiện, hình thức hóa và vết chạy:** R1 phần đầu; đáp án 27 giá trị ở bảng lời giải phía sau trong storyboard; không đổi thứ tự (r, b).
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trên là công thức/dữ kiện; dưới bảng trống 9 hàng × 3 cột chỉ chứa nhãn để làm bài. Năm 2 tính có hệ thống, không cần chép số nguồn dài; đáp án trong notes/ghi chú.
- **Kết nối vào–ra:** Tự kiểm→tính đường xác suất; bảng dẫn tới điểm xác suất một nửa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 12 phút. Với $s=0.1,\ldots,0.9$, cấu hình $(r,b)=(3,10)$ cho $0.009955120,0.077180588,0.239448893,0.483870732,0.736924424,0.912267475,0.985015105,0.999234054,0.999997864$. Cấu hình $(6,20)$ cho $0.000020000,0.001279222,0.014479467,0.078809323,0.270187144,0.615414636,0.918185997,0.997712125,0.999999740$. Cấu hình $(5,50)$ cho $0.000499878,0.015875200,0.114539882,0.402283952,0.795550630,0.982533828,0.999898996,0.999999998$ và xấp xỉ 1. Kết quả cuối được làm tròn, không bằng 1 chính xác. Tiêu chí: giữ đúng $r,b$, tính đủ 27 giá trị và chỉ làm tròn sau lũy thừa. Nguồn: Bài 3.4.1, MMDS 3e, §3.4.4, tr.96.
- **Nguồn:** B Bài 3.4.1, §3.4.4, tr.96/PDF 25; dịch nguyên yêu cầu, không lược cấu hình.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 12 phút.

#### lec06-s07-02 — Điểm xác suất một nửa

- **Mục đích và vai trò:** Giải ngưỡng chính xác và so xấp xỉ cho ba cấu hình nguồn.
- **Thông điệp:** Nghiệm $P(s)=1/2$ khác xấp xỉ $b^{-1/r}$.
- **Nội dung công khai dự kiến:** Câu hỏi: Với từng cấu hình $(r,b)=(3,10),(6,20),(5,50)$ của bài trước, tìm $s$ để xác suất tạo ứng viên bằng 1/2. So với xấp xỉ $b^{-1/r}$. Sản phẩm: phép biến đổi và bảng ba cặp giá trị.
- **Đầu vào và giả thiết:** Bảng xác suất, biến đổi lũy thừa; không thêm điểm bất động.
- **Dữ kiện, hình thức hóa và vết chạy:** R1 phần hai; nghiệm (.406088134, .569353387, .424394480); xấp xỉ (.464158883, .606962231, .457305052).
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khối đề trên; bảng trống 3 hàng cấu hình/chính xác/xấp xỉ dưới. Năm 2 thực hiện đại số thay vì đọc đồ thị; hai giá trị đặt cạnh để không đồng nhất.
- **Kết nối vào–ra:** Bảng P →ngưỡng; phép ghép tổng quát tiếp tục thao tác xác suất.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 6 phút. Từ $(1-s^r)^b=1/2$ suy $s=(1-2^{-1/b})^{1/r}$. Với $(r,b)=(3,10),(6,20),(5,50)$, nghiệm chính xác lần lượt là $0.406088134,0.569353387,0.424394480$; xấp xỉ $b^{-1/r}$ là $0.464158883,0.606962231,0.457305052$. Tiêu chí: có bước biến đổi, tính đủ ba cấu hình và nhận ra cả ba xấp xỉ lớn hơn nghiệm chính xác. Nguồn: Bài 3.4.2, tr.96.
- **Nguồn:** B Bài 3.4.2, §3.4.4, tr.96/PDF 25; giữ yêu cầu và toàn cấu hình bài 3.4.1.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 6 phút.

#### lec06-s07-03 — Xác suất sau nhiều phép ghép

- **Mục đích và vai trò:** Viết xác suất cho bốn chuỗi AND/OR của Bài 3.6.1.
- **Thông điệp:** Thứ tự phép ghép được giữ trong từng trạng thái trung gian.
- **Nội dung công khai dự kiến:** Câu hỏi: Gọi $p$ là xác suất trùng của một MinHash cơ sở. Biểu diễn xác suất sau các phép ghép: (a) AND 2 rồi OR 3; (b) OR 3 rồi AND 2; (c) AND 2, rồi OR 2, rồi AND 2; (d) OR 2, rồi AND 2, rồi OR 2, rồi AND 2. Sản phẩm: bốn biểu thức; các phép thử độc lập.
- **Đầu vào và giả thiết:** HT7; các cấu hình nguyên nguồn.
- **Dữ kiện, hình thức hóa và vết chạy:** R2; lời giải các trạng tháiq 1, q 2, q 3 ở mục đáp án. Không thêm yêu cầu mã.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bốn hàng chuỗi thao tác, mỗi hàng mũi tên bằng chữ; cột kết quả để trống. Năm 2 theo thứ tự từ trái sang phải trước mở ngoặc lồng; notes ghi từng trạng thái.
- **Kết nối vào–ra:** Ngưỡng→hợp phép biến đổi; họ Hamming cho vết chạy cụ thể của hàm cơ sở.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 10 phút. Đáp án: (a) $1-(1-p^2)^3$; (b) $[1-(1-p)^3]^2$; (c) $[1-(1-p^2)^2]^2$; (d) đặt $q_1=1-(1-p)^2,q_2=q_1^2,q_3=1-(1-q_2)^2$, kết quả $q_3^2$. Tiêu chí: bảo toàn thứ tự, bù đúng ở OR, nhân đúng ở AND. Nguồn Bài 3.6.1(a–d), tr.108.
- **Nguồn:** B Bài 3.6.1(a–d), §3.6.4, tr.108/PDF 37.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 10 phút.

#### lec06-s07-04 — Các hàm tọa độ tạo ứng viên

- **Mục đích và vai trò:** Liệt kê hàm Hamming nhận từng cặp của bốn vector.
- **Thông điệp:** Mỗi cặp được nhận bởi đúng các tọa độ mà nó trùng.
- **Nội dung công khai dự kiến:** Câu hỏi: Họ gồm sáu hàm $h_i(x)=x_i$ cho vector độ dài 6. Với bốn vector $A=000000,B=110011,C=010101,D=011100$, xác định những hàm làm từng cặp trở thành ứng viên. Sản phẩm: sáu tập chỉ số.
- **Đầu vào và giả thiết:** HT8; chỉ số 1–6; cùng $i$ ở hai vector.
- **Dữ kiện, hình thức hóa và vết chạy:** R3; giữ 4 vector nguồn, đổi tên nhãn A–D để phân biệt mã đối tượng và giá trị.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 45% bảng 4 × 6 bit; phải 55% danh sách 6 cặp có chỗ ghi tập chỉ số. Năm 2 đối chiếu thẳng cột, tránh chỉ đếm Hamming mà thiếu tên hàm.
- **Kết nối vào–ra:** Biểu thức ghép→phép thử hữu hạn; chữ ký dấu thay phép đọc tọa độ bằng tích vô hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 6 phút. Đáp án: AB={3,4}; AC={1,3,5}; AD={1,5,6}; BC={2,3,6}; BD={2}; CD={1,2,4,5}. Tiêu chí: đủ sáu cặp, đúng chỉ số từ 1 và so cùng vị trí. Nguồn Bài 3.7.1, tr.113.
- **Nguồn:** B Bài 3.7.1, §3.7.6, tr.113/PDF 42; nhãn A–D chỉ thay cách gọi.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 6 phút.

#### lec06-s07-05 — Chữ ký dấu và góc giữa ba vector

- **Mục đích và vai trò:** Tính đủ chữ ký và đối chiếu góc thật cho Bài 3.7.2.
- **Thông điệp:** Bốn phép thử cố định cho một ước lượng góc có thể sai lệch.
- **Nội dung công khai dự kiến:** Câu hỏi: $v_1=(1,1,1,-1),v_2=(1,1,-1,1),v_3=(1,-1,1,1),v_4=(-1,1,1,1)$. Với $x=(2,3,4,5),y=(-2,3,-4,5),z=(2,-3,4,-5)$, tính chữ ký dấu. Với từng cặp, tính góc ước lượng từ chữ ký và góc thật. Sản phẩm: bảng tích/dấu và bảng ba cặp góc.
- **Đầu vào và giả thiết:** Cơ chế chữ ký dấu; quy tắc dấu tại 0 là +1; máy tính hỗ trợ arccos.
- **Dữ kiện, hình thức hóa và vết chạy:** R4 giữ nguyên ba vector và bốn pháp tuyến. Đây là mẫu dấu cố định, không được gán phân phối đẳng hướng.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Dữ kiện bốn pháp tuyến ở trên theo nhóm 2 × 2; ba vector ở giữa; nhiệm vụ ở đáy. Sinh viên năm 2 cần đủ dữ kiện trên một trang; các bảng kết quả thuộc notes để giữ khả năng đọc.
- **Kết nối vào–ra:** Băm tọa độ cung cấp chữ ký rời rạc; tích vô hướng cung cấp chữ ký dấu; bài kế tiếp dùng phép chiếu để gán thùng Euclid.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 10 phút. Tích của $x$ là $(4,6,8,10)$, của $y$ là $(-8,10,-4,6)$, của $z$ là $(8,-10,4,-6)$. Chữ ký lần lượt là $(+,+,+,+)$, $(-,+,-,+)$ và $(+,-,+,-)$. Góc ước lượng của các cặp $xy,xz,yz$ là $90^\circ,90^\circ,180^\circ$; góc thật xấp xỉ $74.973886^\circ,105.026114^\circ,180^\circ$. Tiêu chí: tính đúng tích và dấu, dùng cùng bốn pháp tuyến, chuẩn bình phương bằng 54 và đổi radian sang độ rõ ràng. Nguồn: Bài 3.7.2, tr.113–114.
- **Nguồn:** B Bài 3.7.2(a–c) và câu hỏi chung, §3.7.6, tr.113–114/PDF 42–43.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 10 phút.

#### lec06-s07-06 — Thùng chiếu trên ba trục

- **Mục đích và vai trò:** Gán thùng ở hai độ rộng và hợp đúng theo cùng trục.
- **Thông điệp:** Độ rộng khoảng thay tập cặp ứng viên ngay cả với trục cố định.
- **Nội dung công khai dự kiến:** Câu hỏi: $p_1=(1,2,3),p_2=(0,2,4),p_3=(4,3,2)$. Ba hàm là phép chiếu trên ba trục tọa độ; các khoảng $[ja,(j+1)a)$,$j\in\mathbb Z$. (a) Gán thùng khi $a=1$; (b) lặp lại với $a=2$; (c) tìm cặp ứng viên cho mỗi trường hợp. Sản phẩm: hai bảng mã thùng và hai tập cặp.
- **Đầu vào và giả thiết:** Phần giảng chỉ minh họa trục thứ nhất với a=1; hàm sàn và thùng tách theo trục đã được định nghĩa.
- **Dữ kiện, hình thức hóa và vết chạy:** R5 giữ nguyên (a–c); phần (d) chuyển sang N15. Các biên khoảng giữ nguyên sách.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba điểm và quy ước biên ở trên; hai bảng trống có cùng cột trục 1,2,3 ở dưới. Sinh viên năm 2 so hai độ rộng trên cùng dữ kiện; đáp án tập cặp thuộc notes.
- **Kết nối vào–ra:** Phép băm dấu dùng hướng; phép chiếu chia khoảng dùng tọa độ và độ rộng. Bài vân tay kế tiếp dùng lại phép ghép để so sai số.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 8 phút. Với $a=1$, mã của ba điểm lần lượt là $(1,2,3),(0,2,4),(4,3,2)$, chỉ có cặp $(1,2)$. Với $a=2$, các mã là $(0,1,1),(0,1,2),(2,1,1)$, cả ba cặp đều là ứng viên. Tiêu chí: dùng hàm sàn đúng tại biên, chỉ so trong cùng trục, hợp và khử lặp đúng. Ba trục cố định không tự cho bảo đảm xác suất của họ hướng ngẫu nhiên. Nguồn: Bài 3.7.5(a–c), tr.114.
- **Nguồn:** B Bài 3.7.5(a–c), §3.7.6, tr.114/PDF 43; chuyển (d) sang đọc thêm.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 8 phút.

#### lec06-s07-07 — So sánh hai phép ghép vân tay

- **Mục đích và vai trò:** Tính hai loại lỗi với cùng 2048 hàm cơ sở.
- **Thông điệp:** Cùng ngân sách hàm có thể ưu tiên giảm bỏ sót hoặc giảm ứng viên giả.
- **Nội dung công khai dự kiến:** Câu hỏi: Mỗi ô có đặc trưng với xác suất 0.2. Với hai bản cùng ngón, ảnh thứ hai có đặc trưng tại ô đã có của ảnh thứ nhất với xác suất 0.8. Mỗi phép thử chọn ba ô từ lưới; các phép thử độc lập theo mô hình. $F_1$ là OR 1024, $F_2$ là OR 2048. (a) Tính xác suất ứng viên giả và bỏ sót của $F_2$. (b) So với AND hai nhóm OR 1024 độc lập. Sản phẩm: bảng hai xác suất cho hai cấu trúc.
- **Đầu vào và giả thiết:** Mô hình vân tay, xác suất cơ sở và AND/OR đã học; không dùng tiên quyết từ phần đọc thêm.
- **Dữ kiện, hình thức hóa và vết chạy:** R6 giữ nguyên Bài 3.8.2(a, b). Hai cấu trúc cùng 2048 phép thử; đây là trang kiểm tra tổng hợp của phần 7.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Giả thiết mô hình ở trên; hai sơ đồ nhóm ở giữa; hai nhiệm vụ dưới. Sinh viên năm 2 cần suy xác suất cơ sở rồi áp dụng phép ghép; không dùng giá trị đã làm tròn làm đầu vào.
- **Kết nối vào–ra:** Các phép băm cơ sở dẫn đến việc chọn cách khuếch đại; bài kết thúc bằng đánh đổi có điều kiện giữa hai loại lỗi.
- **Diễn giải học thuật, lời giải và tiêu chí:** Thời lượng học tập dự kiến 8 phút. $q_F=0.000064,q_T=0.004096$. OR 2048 cho xác suất ứng viên giả $0.122849062$ và bỏ sót $0.000223559$. AND hai nhóm OR 1024 cho xác suất ứng viên giả $0.004024207$ và bỏ sót $0.029680224$. Tiêu chí: suy đúng hai xác suất cơ sở, nêu độc lập, ghép đúng thứ tự, dùng giá trị chưa làm tròn và so cùng 2048 hàm. Nguồn: Bài 3.8.2(a, b), tr.121.
- **Nguồn:** B Bài 3.8.2(a, b), §3.8.7, tr.121/PDF 50; kiểm tra tổng hợp.
- **Ánh xạ ghi chú:** `N16`. **Thời lượng:** 8 phút.

## Kiến trúc ghi chú bài giảng tự học

Ghi chú là tài liệu độc lập, bắt đầu H1 và liên kết về bộ trang chiếu. Ký hiệu được định nghĩa trước lần dùng. Mỗi chủ đề mở bằng nhu cầu và kết nối vào; sau đó định nghĩa/đặc tả trước ví dụ, dùng ví dụ để giải thích trực quan, rồi mới phát biểu kết quả, thuật toán và chứng minh. Cuối chủ đề có giới hạn, nhiệm vụ tự kiểm và kết nối ra. Các phiếu dưới đây xác định nội dung cần có; không dùng mặt slide hoặc notes diễn giả làm bản sao cho ghi chú.

### N01. Bài toán ứng viên

Nguồn B §3.4, tr.91–92. Nhận chữ ký từ Bài 05; sản phẩm là đặc tả tìm cặp đạt ngưỡng và phân biệt bộ nhớ với số cặp. Định nghĩa các tập hữu hạn không rỗng $S_1,\ldots,S_C$, Jaccard $s$, ma trận SIG và ngưỡng $t\in[0,1]$ trước khi tính Ví dụ 3.10. Tính đủ $10^9$ byte, số cặp, giây và ngày; nêu giả định một microgiây. Trực quan là hai nhánh chi phí số cặp và chi phí mỗi cặp. Không có định lý hay thuật toán mới; không tạo đề mục chứng minh rỗng. Tự kiểm yêu cầu xác định giới hạn còn lại khi chữ ký đã vừa bộ nhớ. Đầu ra tạo nhu cầu N02.

### N02. Phân dải, khử lặp và xác minh

Nguồn B §§3.4.1,3.4.3, tr.92–96; dữ kiện Ví dụ 3.8, tr.85–86. Trước ví dụ, đặc tả rõ SIG $n\times C$, $b,r\in\mathbb N_{>0}$, $n=br$, khóa $(j,\text{tuple})$, ngưỡng $t\in[0,1]$, tập cặp chuẩn hóa $c<d$ và đầu ra sau xác minh. Miền các tập nguồn hữu hạn không rỗng. Khóa bảng băm được so đầy đủ; hàm băm lưu trữ không thay phép bằng toán học.

Ví dụ tự học gồm đủ các tập gốc, SIG, khởi tạo, hai bảng thùng, bốn lượt phát và hợp ba cặp, ba phép Jaccard. Dùng Hình 3.7 như ví dụ thứ hai chỉ cho điều kiện $r=3$; không điền dữ kiện chưa có. Trực quan giải thích AND trong dải và OR qua dải. Giả mã khởi tạo từ điển rỗng và tập cặp rỗng. Trong hai vòng dựng thùng, sao chép tuple thành $z$, đặt $k\leftarrow(j,z)$; nếu khóa chưa có thì tạo $B[k]\leftarrow[]$, rồi thực hiện `B[k].append(c)`. Sau đó phát cặp trong từng thùng, khử lặp, kiểm gốc và trả kết quả; không duyệt trước mọi cặp kho.

Mệnh đề tính đúng: với SIG cố định, thuật toán trả đúng những cặp đạt $t$ trong tập có một dải trùng. Chứng minh đầy đủ theo bất biến: từ điển rỗng trước dải đầu; đầu dải j chưa có khóa mang j, các dải trước được giữ; nếu khóa mới thì tạo danh sách rỗng, nếu khóa đã có thì giữ các mã trước đó, rồi mỗi lượt chèn thêm đúng mã vào khóa của nó; khi dừng, cùng thùng tương đương cùng tuple trong cùng dải; phát và hợp tạo đúng tập ứng viên; phép kiểm giữ đúng điều kiện Jaccard. Các vòng hữu hạn; $C<2$ hay thùng dưới hai phần tử không phát cặp. Tập rỗng nằm ngoài miền, không bổ sung quy ước Jaccard rỗng. Tự kiểm: giải thích cặp 14 phát hai lần nhưng chỉ kiểm một lần. Chi phí được đặt thành N04 sau khi N03 giải thích xác suất; liên kết không bỏ bước mà tránh ngắt cơ chế xác suất của sách.

### N03. Xác suất ứng viên, ngưỡng và hai loại lỗi

Nguồn B §3.4.2–3, tr.93–96 và Bài 3.4.2. Định nghĩa mô hình: cặp tập không rỗng cố định, các MinHash thành phần đều độc lập, so khóa chính xác. Định nghĩa ứng viên giả ở tầng sinh cặp; bỏ sót là sự kiện một cặp có Jaccard $s\ge t$ không được chọn. Sau đó chạy Ví dụ 3.12 tại $s=.8$: $.8^5=.32768$, thất bại một dải $.67232$, thất bại 20 dải $.000356058$, được chọn $.999643942$. Trực quan nối sự kiện với phép AND/OR trước hình đường xác suất.

Chứng minh đủ bốn bước $s^r$, $1-s^r$, $(1-s^r)^b$, lấy bù. Chỉ rõ nơi dùng độc lập trong dải và giữa dải; không cần độc lập giữa các cặp dữ liệu. Suy đại số $s_{1/2}=(1-2^{-1/b})^{1/r}$, so $t$ và $b^{-1/r}$; với 20 × 5 có .508695962 và .549280272. So cấu hình 20 × 5 với 10 × 10 cùng $n=100$ tại $s=.3,.8$. Giải thích sai số theo cặp, không gán diện tích đồ thị thành tỷ lệ kho. Bộ lọc theo $\widehat s$ là lựa chọn khác có thể thêm bỏ sót, không thuộc baseline. Tự kiểm yêu cầu chọn giữa hai cấu hình nếu ưu tiên giảm bỏ sót ở .8 hoặc giảm ứng viên ở .3; đầu ra nối N04 đếm công việc.

### N04. Mô hình chi phí

Chủ đề bổ sung đã duyệt, suy trực tiếp từ giả mã B §3.4. Định nghĩa $u_{j,z},Q,K,T_J$ và mô hình từ máy/bảng băm kỳ vọng/sao chép tuple trước phép đếm. Vết V02 cho 8 chèn,4 phát,3 kiểm; hình hoặc bảng nối từng dòng giả mã với từng số hạng. Suy $Q=\sum\binom{u_{j,z}}2$, $K\le Q$, thời gian kỳ vọng $O(nC+Q+\sum T_J)$ và bộ nhớ phụ $O(nC+K)$ ngoài SIG đầu vào. Chứng minh bằng đếm $bC$ tuple dài $r$, $Q$ lượt chèn cặp, $K$ lần kiểm; với tập đã sắp xếp, mô tả phép trộn và $T_J=O(|S_c|+|S_d|)$.

Trường hợp xấu mọi cột cùng thùng mỗi dải cho $Q=b\binom C2$, $K=\binom C2$. Một đoạn tùy chọn suy $\mathbb E[K]=\sum P(s_{cd})$ và $\mathbb E[Q]=b\sum s_{cd}^r$ bằng biến chỉ báo; nhấn tuyến tính kỳ vọng không cần độc lập cặp. Tự kiểm yêu cầu giải thích vì sao chỉ thay $Q$ bằng $K$ trong chi phí phát cặp là sai. Kết nối ra: quy trình hiện dùng Jaccard; N05 xác định các miền khoảng cách khác.

### N05. Miền dữ liệu và các độ đo

Nguồn B §3.5, tr.96–103. Trước các ví dụ, định nghĩa metric với miền/hàm/tiên đề; chuẩn vector $L_q$ chỉ $q\ge1$, nêu $L_1,L_2,L_\infty$. Với mỗi loại, định nghĩa trước rồi chạy đúng ví dụ nguồn: V05 tính 7,5,4; Jaccard trên tập hữu hạn không rỗng dùng cặp 14; góc trên hướng hoặc vector đơn vị dùng V06; chỉnh sửa chỉ chèn/xóa dùng V07; Hamming trên $\Sigma^D$ dùng V08. Định nghĩa dãy con và dãy con chung dài nhất trước công thức LCS. Giữ $\theta$ radian, ghi phép đổi 60°=π/3.

Chứng minh đầy đủ tam giác Jaccard bằng cùng MinHash: bao hàm sự kiện rồi chặn hợp; không cần độc lập. Chứng minh công thức chỉnh sửa bằng hai cận: dựng phép xóa/chèn theo LCS; mọi kịch bản sửa giữ một dãy con chung nên không thể giữ quá $L$. Từ phép nối kịch bản sửa suy tam giác; đảo kịch bản cho đối xứng. Hamming chứng minh theo tọa độ rồi cộng. Góc có phác thảo hình học đường trên mặt cầu đơn vị, ghi đúng mức phác thảo; không nhận nó là metric trên toàn vector khác 0. Tính metric của chuẩn được phát biểu theo nguồn, không thêm chứng minh Minkowski ngoài tiên quyết.

Không có thuật toán mới cho từng định nghĩa, vì vậy không tạo giả mã DP. Có thể đếm $O(D)$ để tính chuẩn/Hamming/góc trên vector đặc, $O(|A|+|B|)$ với tập sắp xếp; không tự gán chi phí tính LCS khi chưa trình bày thuật toán. Tự kiểm phân biệt cosin với góc và chỉnh sửa chèn/xóa với Hamming. N05 cấp miền/đơn vị cho N06.

### N06. Họ nhạy cảm theo khoảng cách

Nguồn B §3.6.1–2, tr.103–105. Nêu nhu cầu diễn đạt một phép thử cho nhiều miền dữ liệu. Định nghĩa $\mathcal H$ kèm phân phối, cặp cố định, cùng $h$, miền tham số và hai cận trước Ví dụ 3.18. Với Jaccard, $0\le d_1<d_2\le1$ cho họ $(d_1,d_2,1-d_1,1-d_2)$; Ví dụ 3.18 cho (.3, .6, .7, .4). Đồ thị ba miền không áp một dạng đường cụ thể cho mọi họ.

Lập luận ví dụ chỉ dùng $P=1-d_J$ và tính đơn điệu; không gọi đó là bằng chứng mọi họ có equality. Không có thuật toán mới; việc lấy mẫu một hàm được nêu là hợp đồng xác suất. Tự kiểm dùng d=.2, .5, .8 và giải thích vùng giữa không ràng buộc. Đầu ra là bộ cận để N07 biến đổi.

### N07. Phép ghép AND và OR

Nguồn B §3.6.3, tr.105–108. Định nghĩa cặp được nhận, các phép thử độc lập và phép ghép trước Ví dụ 3.19–20. AND lưu tuple và nhận khi tất cả trùng; OR nhận khi ít nhất một bảng trùng. Chạy trung gian $p^4$ hoặc $1-(1-p)^4$ rồi lớp ghép thứ hai cho $p=.8,.4$; giữ cận .878497449/.098534519 so .993615344/.573951942.

Chứng minh hai công thức đầy đủ bằng giao độc lập và bù; chuyển cận theo tính đơn điệu. Phân biệt xác suất đúng bằng $p$ của một cặp với các cận gần/xa của họ. Diễn đạt OR như quan hệ cặp vì quan hệ này nói chung không bắc cầu; không biến OR thành equality của một hashvalue. Giả mã ngắn cho AND_r rồi OR_b thể hiện tính hàm, nhóm tuple, tra bảng và hợp cặp, dẫn lại N02 thay lặp toàn thuật toán. Với OR rồi AND, mỗi nhóm OR hợp cặp qua các bảng cơ sở, sau đó lấy giao các tập cặp của những nhóm OR. Quan hệ OR không được mã hóa bằng phép bằng nhau của tuple. Chi phí số hàm bằng tích các kích thước nhóm; chi phí phát cặp vẫn phụ thuộc $Q$. Tự kiểm dùng bốn chuỗi Bài 3.6.1 và giải thích hai thứ tự có cùng 16 hàm nhưng khác đánh đổi. N08–N10 thay họ cơ sở mà giữ phép ghép.

### N08. Họ Hamming

Nguồn B §3.7.1, tr.109. Định nghĩa vector cùng chiều $D>0$, $I$ đều và $h_I(x)=x_I$ trước V08. Ví dụ liệt kê vị trí 1,3 trùng và 2,4,5 khác; hình hai hàng bit cho xác suất 2/5. Mệnh đề $P=1-d_H/D$ được chứng minh bằng đếm số chỉ số thuận lợi. Nêu lựa chọn chỉ số có hoàn lại cho nhiều thử độc lập. Thuật toán lấy $I$, đọc một tọa độ, trả giá trị; dừng sau một lần đọc. Chi phí $O(1)$ mỗi thử với mảng, trữ một chỉ số; $m$ thử cần $m$ chỉ số và $m$ giá trị mỗi đối tượng. Tự kiểm Bài 3.7.1 có lời giải trong N16. Nối sang N09 khi tọa độ rời rạc được thay bởi hướng.

### N09. Siêu phẳng và chữ ký dấu

Nguồn B §§3.7.2–3, tr.109–111; hình đối chiếu S4 PDF 48–49. Định nghĩa siêu phẳng qua gốc, pháp tuyến, hàm dấu với sign (0)=+1 và góc $\theta\in[0,\pi]$ trước V10. Trước ví dụ, nêu xác suất khác dấu bằng theta/pi trong mô hình đẳng hướng và định nghĩa quy tắc ước lượng bằng pi nhân tỷ lệ bit khác; nêu căn cứ hai miền góc tách. Sau đó dùng 3 pháp tuyến dấu cố định để chạy đủ sáu tích, tạo chữ ký và góc 120°; tính góc thật 38.047579°. Trực quan phân biệt pháp tuyến với đường phân chia.

Sau ví dụ, trở lại mô hình pháp tuyến đẳng hướng đã nêu để chứng minh mệnh đề $P=1-\theta/\pi$. Xử lý riêng $\theta=0$ cho xác suất trùng 1 và $\theta=\pi$ cho xác suất trùng 0. Khi $0<\theta<\pi$, hai vector không cùng phương; chứng minh chiếu về mặt phẳng sinh bởi chúng, đếm tổng góc tách $2\theta$ trên $2\pi$, rồi lấy bù. Họ góc chỉ dùng $0\le d_1<d_2\le\pi$. Thuật toán $m$ bit dùng cùng $m$ pháp tuyến cho mọi đối tượng; vector đặc cho $O(mD)$ phép tính và $m$ bit/đối tượng, pháp tuyến dùng $O(mD)$ từ. Phân phối dấu ±1 không đẳng hướng; toàn 16 vector dấu của Ex 3.22 cho 45° với quy tắc 0 đã chốt, tách nguồn sai số phân phối với mẫu. Tự kiểm tính dấu Bài 3.7.2 và nêu giả thiết của định lý. N10 giữ thao tác tích vô hướng nhưng dùng độ lớn hình chiếu.

### N10. Chiếu Euclid và chia khoảng

Nguồn B §§3.7.4–5, tr.111–113; Datar §3.2 PDF 3 chỉ cho cơ chế dịch. Định nghĩa trong mặt phẳng:$a>0$, $u$ đều hướng đơn vị,$\delta$ độc lập đều trên $[0,a)$,$h=\lfloor(u\cdot x+\delta)/a\rfloor$. Sau định nghĩa, tách ví dụ thực thi xác định của Bài 3.7.5: ba điểm/ba trục với $a=1,2$; có thể dẫn bài tập trước rồi cung cấp lời giải gập ở N16 để tài liệu tự học đọc độc lập. Không áp bảo đảm ngẫu nhiên cho ba trục cố định.

Hình chiếu có biên $ka-\delta$, khoảng nửa mở và độ dài $\ell$. Chứng minh xác suất theo $\delta$ bằng độ dài khoảng biên tách; xét $\ell=0$, $0<\ell<a$, $\ell\ge a$. Chứng minh cận gần bằng $\ell\le\rho\le a/2$; cận xa bằng điều kiện cần $\rho|\cos\phi|<a$ và góc nhọn đều hai chiều. Phát biểu $(a/2,2a,1/2,1/3)$ chỉ hai chiều. Đây là suy luận bản soạn bổ sung giả thiết MMDS, không gán cận cho bài báo p-stable. Thuật toán tính tích vô hướng, cộng $\delta$, chia $a$, lấy sàn rồi dùng khung N02/N07; dừng hữu hạn, chi phí vector đặc $O(D)$ mỗi thử. Tự kiểm phân biệt gần về hình chiếu với chung thùng và điều kiện theo số chiều. N11 bắt đầu vận dụng chọn biểu diễn/quy tắc.

### N11. Đối sánh thực thể

Nguồn B §§3.8.1–3, tr.114–117. Định nghĩa hai nguồn hồ sơ, đối tượng thực thể và ứng viên trước ví dụ hai tập một triệu bản ghi. Các trường tên/địa chỉ/điện thoại giữ nguyên nguồn. Mô tả ba bảng khóa, hợp cặp, khử lặp, chấm điểm đầy đủ; không tự tạo bảng hồ sơ nhân khẩu. Trực quan là luồng ba khóa chảy vào hợp cặp. Chứng minh theo cơ chế chỉ bảo đảm mọi cặp khớp ít nhất một trường được đưa vào ứng viên; không suy đồng nhất thực thể. Không có phân phối đủ để phát biểu họ bốn tham số; không giả định các trường độc lập.

Chi phí đối chiếu toàn bộ hai nguồn là $10^{12}$ cặp; phương án nhóm vẫn phụ thuộc tổng kích thước thùng và chi phí chấm điểm. Nêu trường phụ không dùng chấm điểm có thể kiểm chất lượng tập kết quả, còn công thức ngày được chuyển N15. Tự kiểm giải thích khớp điện thoại chưa đủ xác nhận cùng người. N12 cung cấp ví dụ có mô hình xác suất rõ.

### N12. Đối sánh vân tay

Nguồn B §§3.8.4–5/Ex 3.23, tr.117–120. Định nghĩa ảnh chuẩn hóa, tập ô có đặc trưng và phép thử chọn ba ô từ lưới trước khi xét ảnh. Thùng chung chỉ dành cho ảnh chứa cả ba ô; ảnh thiếu ô nhận thùng đơn riêng. Nêu khác nhau của truy vấn một ảnh với kho và tìm cặp trong kho; không thêm quy trình nhận dạng ảnh.

Ví dụ mô hình 0.2/0.8 nêu rõ độc lập. Tính xác suất cả hai ảnh có đủ ba ô:$q_F=.2^6$,$q_T=(.2\cdot.8)^3$; không điều kiện hóa rằng ảnh truy vấn đã chứa ba ô. Trực quan tách tầng một ô, ba ô, nhiều thử. Suy OR 1024 và AND hai nhóm bằng công thức đã chứng minh; giữ số chưa làm tròn. Thuật toán cơ sở và khung ghép từ N07 được áp dụng; xác minh vân tay nằm sau ứng viên và có chi phí riêng, không gán $O(1)$. Tự kiểm Bài 3.8.2 so hai phương án cùng 2048 hàm. N13 đổi biểu diễn văn bản để kiểm ý nghĩa tương đồng.

### N13. Bản tin gần trùng

Nguồn B §3.8.6/Ex 3.24, tr.120–121. Định nghĩa bài toán nhóm trang xuất phát từ cùng văn bản với phần bao quanh khác; phân biệt cùng chủ đề. Định nghĩa từ dừng là từ rất thường gặp, nêu danh sách I, that, you, for, your. Đặc tả shingle là một token từ dừng và hai token tiếp theo; mật độ từ dừng cao trong văn xuôi giải thích lựa chọn đặc trưng. Câu ngắn “Buy Sudzo.” có 0 shingle; câu dài có bốn shingle xác định và một shingle phụ thuộc token kế tiếp $x$ chưa được cho. Câu dài cũng có thể là lời quảng cáo; quy tắc ưu tiên văn xuôi, không bảo đảm loại mọi quảng cáo. Không tạo token sau laundry.

Hình đối chiếu văn bản chính và phần bao quanh chỉ là quan hệ khái niệm. Mệnh đề học thuật ở mức quy tắc biểu diễn, không là định lý về mọi trang web; không biến dự đoán 75%/25% thành thực nghiệm. Dùng lại thuật toán shingle/MinHash/LSH, kèm chi phí phụ thuộc số token và $Q,K$, không phân tích mô hình chưa có. Tự kiểm xác định đối tượng đầu ra và giải thích vì sao câu quảng cáo dài của nguồn vẫn tạo shingle. Thay nhiệm vụ bình luận thao tác dịch bằng nhiệm vụ ứng dụng s05-06 đã có; lý do giữ token thuộc review-log. N14 thu hồi toàn quy trình.

### N14. Tổng hợp và tự kiểm

Nguồn §§3.4–3.8. Mở bằng đầu ra đã có và sơ đồ lựa chọn biểu diễn→độ đo→họ→ghép→ứng viên→xác minh. Thu hồi triệu tài liệu, không tự ước lượng số cặp được giảm. Liên hệ $P,Q,K,T_J$, bảo đảm trong tập ứng viên và khả năng bỏ sót cặp có Jaccard $s\ge t$. Không có định nghĩa, thuật toán hoặc chứng minh mới; ghi rõ “không áp dụng” trong kế hoạch này vì đây là tổng hợp. Sáu nhiệm vụ s06-03/04 có lời giải gập, đo đủ MT1–MT6. Kết nối Bài 07 theo tiêu chí chất lượng/thời gian/bộ nhớ, không dạy HNSW/PQ.

### N15. Đọc thêm có giới hạn

Chọn hai mục triển khai ngắn; chúng không cấp tiên quyết cho recitation. Mục thứ nhất giải Bài 3.7.5(d), tr.114: cặp 12 luôn chung ở trục 2 nên ứng viên với mọi $a>0$; cặp 13 và 23 thành ứng viên khi $a\in(3/2,2]\cup(3,\infty)$. Lời giải xét điều kiện hàm sàn trên các cặp tọa độ và hợp các khoảng; kiểm riêng các biên 3/2,2,3. Mục thứ hai giải thích mô hình kiểm thực thể bằng ngày của §3.8.3, tr.116–117: độ trễ là ngày tạo hồ sơ B trừ ngày tạo hồ sơ A, lọc 0–90 ngày; giả thiết độ trễ ngẫu nhiên đều làm rõ trung bình 45 ngày. Nhóm đạt điểm tối đa 300 được giả định khớp đúng và có trung bình 10 ngày; nhóm cùng mức điểm được xét có trung bình $x$; mô hình hỗn hợp $x=10f+45(1-f)$ cho $f=(45-x)/35$. Nêu giả thiết đại diện của hai nhóm và không dùng để kết luận từng cặp.

MapReduce Bài 3.4.4, tr.96; ghép 256 Ví dụ 3.21, tr.108; điểm bất động/đạo hàm Bài 3.6.2–4, tr.108; mở rộng Euclid §3.7.5, tr.113 chỉ nằm danh mục đọc tiếp kèm mục đích, không soạn thêm chương hoặc chứng minh. Không thêm nội dung §3.9, HNSW, PQ, RAG. Phạm vi chọn gọn tránh làm tài liệu tự học tăng độ dài mà không tạo đầu ra cần thiết.

### N16. Bài tập và lời giải

Sáu cụm nguồn, R1–R6, giữ toàn dữ kiện/yêu cầu và tổng 60 phút như phiếu s07-01–07. Mỗi bài có khối exercise, hint, solution không lồng nhau; hint/solution gập mặc định, dùng bàn phím và mở khi in. Dữ kiện đề xuất hiện đầy đủ để người đọc không phải mở slide. Các lời giải dưới đây chuyển vào tài liệu, không chỉ tham chiếu storyboard. Tiêu chí đánh giá nêu bước toán học và lỗi cụ thể, không chứa lời điều phối lớp. Việc chia bài 3.4.1–2 thành hai trang và chuyển 3.7.5(d) sang đọc thêm là hai điều chỉnh, được ghi trong log.

## Lời giải recitation cần triển khai đầy đủ

### R1. Bài 3.4.1–2, tr.96, 18 phút

| $s$ | $r=3,b=10$ | $r=6,b=20$ | $r=5,b=50$ |
|---:|---:|---:|---:|
|0.1|0.009955120|0.000020000|0.000499878|
|0.2|0.077180588|0.001279222|0.015875200|
|0.3|0.239448893|0.014479467|0.114539882|
|0.4|0.483870732|0.078809323|0.402283952|
|0.5|0.736924424|0.270187144|0.795550630|
|0.6|0.912267475|0.615414636|0.982533828|
|0.7|0.985015105|0.918185997|0.999898996|
|0.8|0.999234054|0.997712125|0.999999998|
|0.9|0.999997864|0.999999740|xấp xỉ 1|

Từ $1-(1-s^r)^b=1/2$ suy $(1-s^r)^b=1/2$, $s^r=1-2^{-1/b}$ và $s=(1-2^{-1/b})^{1/r}$. Theo ba cấu hình: nghiệm chính xác $.406088134,.569353387,.424394480$; xấp xỉ $.464158883,.606962231,.457305052$. Cả ba xấp xỉ đều lớn hơn nghiệm. Điểm cuối bảng làm tròn về 1, không phát biểu xác suất bằng 1 chính xác. Tiêu chí: đúng công thức, đủ 27 ô, đủ 3 cặp ngưỡng, phân biệt $r,b$; không biến $t$ do người dùng chọn thành nghiệm $P=1/2$.

### R2. Bài 3.6.1(a–d), tr.108, 10 phút

(a) $p\to p^2\to1-(1-p^2)^3$. (b) $p\to1-(1-p)^3\to[1-(1-p)^3]^2$. (c) $p\to p^2\to1-(1-p^2)^2\to[1-(1-p^2)^2]^2$. (d) $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$, kết quả $q_3^2$. Mỗi tầng lấy các bản thử độc lập. Các số hàm 6,6,8,16 chỉ là phép kiểm phụ của người soạn, không bổ sung yêu cầu ngoài đề nguồn.

### R3. Bài 3.7.1, tr.113, 6 phút

| Cặp | Chỉ số hàm tạo ứng viên | Số tọa độ khác để đối chiếu |
|---|---|---:|
|A, B|3,4|4|
|A, C|1,3,5|3|
|A, D|1,5,6|3|
|B, C|2,3,6|3|
|B, D|2|5|
|C, D|1,2,4,5|2|

Sản phẩm phải liệt kê hàm, chứ chỉ báo khoảng cách chưa trả lời đủ đề. Nhãn A–D chỉ thay cách gọi bốn vector, không đổi bit.

### R4. Bài 3.7.2, tr.113–114, 10 phút

| Vector | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký dấu |
|---|---|---|
|$x=(2,3,4,5)$|$(4,6,8,10)$|$(+,+,+,+)$|
|$y=(-2,3,-4,5)$|$(-8,10,-4,6)$|$(-,+,-,+)$|
|$z=(2,-3,4,-5)$|$(8,-10,4,-6)$|$(+,-,+,-)$|

Bình phương chuẩn đều 54; tích $xy=14,xz=-14,yz=-54$. Góc thật là $\arccos(7/27)\approx74.973886^\circ$, $\arccos(-7/27)\approx105.026114^\circ$ và $\pi=180^\circ$. Góc ước lượng là $\pi(2/4)=\pi/2=90^\circ$ cho hai cặp đầu và $\pi(4/4)=\pi$ cho cặp cuối. Đây là vết tính bốn pháp tuyến cố định, không bảo đảm ước lượng chính xác cho mọi vector.

### R5. Bài 3.7.5(a–c), tr.114, 8 phút

| $a$ | Mã $p_1$ theo ba trục | Mã $p_2$ | Mã $p_3$ | Cặp ứng viên |
|---:|---|---|---|---|
|1|$(1,2,3)$|$(0,2,4)$|$(4,3,2)$|$(1,2)$|
|2|$(0,1,1)$|$(0,1,2)$|$(2,1,1)$|$(1,2),(1,3),(2,3)$|

Mỗi mã là $\lfloor x_i/a\rfloor$. Chỉ so cùng trục; mã 2 ở trục 2 không phải cùng khóa với mã 2 ở trục 3. Giá trị $a$ thuộc $[a,2a)$, không thuộc $[0,a)$. Phần (d) chuyển N15; phần giảng chỉ minh họa trục 1 với $a=1$ nên không giải sẵn cả bài.

### R6. Bài 3.8.2(a, b), tr.121, 8 phút

$q_F=(.2^2)^3=.000064$ và $q_T=(.2\cdot.8)^3=.004096$. Với OR 2048:

$$
P_F=1-(1-q_F)^{2048}\approx.122849062,\qquad
P_{\rm miss}=(1-q_T)^{2048}\approx.000223559.
$$

Với hai nhóm OR 1024 độc lập ghép AND:

$$
P_F=[1-(1-q_F)^{1024}]^2\approx.004024207,\qquad
P_{\rm miss}=1-[1-(1-q_T)^{1024}]^2\approx.029680224.
$$

OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn; cấu trúc AND giảm ứng viên giả và tăng bỏ sót. Các xác suất thuộc mô hình nguồn với ba ô được chọn từ lưới trước khi xét ảnh. Hai phương án cùng 2048 phép thử. Không tính từ .063 hoặc .985 đã làm tròn.

## Đặc tả tài sản và kiểm định pha sau

Hình dự kiến thuộc `2627-1/img/lec-06/`: luồng biểu diễn–ứng viên; dải/thùng; dải 3 hàng; đồ thị xác suất; miền gần–giữa–xa; cấu trúc AND/OR; chuẩn vector; siêu phẳng; chiếu Euclid; khóa thực thể; lưới vân tay khái niệm. Được gộp hình theo chức năng nếu vẫn truy được quan hệ. Các bảng giá trị dùng HTML/Markdown, không vẽ chữ nhỏ trong SVG. Mỗi SVG có role=img, title/description và alt cụ thể; tọa độ/trọng số/nhãn khớp nguồn. Nếu dùng script sinh SVG, lưu mã tái tạo cùng tài sản.

Pha 1 chỉ kiểm được đặc tả và dữ kiện. Gate đã đối chiếu từng phiếu, trình tự, thời lượng, giả thiết, mặt trang dự kiến và note-topic; bốn sửa nhẹ sau PASS đã được điều phối viên xác nhận. Pha 2 cần kiểm Reveal thực, KaTeX, SVG, notes, đường dẫn, offline, khung rộng/hẹp, bàn phím, in, viewer và hồi quy CSS 02/03 nếu thay CSS chung. Năm reviewer độc lập và editor riêng là bước sau bản nháp. Không đánh dấu render hoặc phát hành đạt tại pha 1.

## Đồng bộ sau năm báo cáo độc lập

Lượt editor giữ 60 trang và thứ tự cũ, bảy phần, 120 phút giảng + 60 phút recitation. Chỉ s01-02 đổi tiêu đề thành “Nội dung và mục tiêu”; ba năng lực gộp MT1–MT6. Mục tiêu mở đầu thay đổi nên cần tái rà mạch toàn tuyến. Các phần thêm là định nghĩa/cầu nối và nhiệm vụ đã duyệt, không mở chủ đề hoặc bài tập nguồn mới.

| Chủ đề | Tự kiểm được thực hiện trong ghi chú | Vị trí đáp án |
|---|---|---|
| N01 | Giới hạn số cặp và tập trung gian trước Jaccard | Khối solution cuối mục bài toán |
| N02 | Cặp (1,4) phát hai lần nhưng kiểm một lần | Khối solution cuối mục phân dải |
| N03 | Chọn cấu hình tại s=.8 và s=.3 | Giữ khối exercise/solution đã có |
| N04 | Phân biệt Q=4 với K=3 khi đếm chi phí phát | Khối solution cuối mục chi phí |
| N05 | Cosin/góc; căn chỉnh Hamming/chỉnh sửa | Khối solution cuối mục độ đo |
| N06 | Đọc cận họ tại d=.2,.5,.8 | Khối solution ngay trước phép ghép |
| N07 | Bốn chuỗi Bài 3.6.1; so hai thứ tự cùng 16 phép thử | Liên kết đến bài nguồn và lời giải gập; giải thích cục bộ |
| N08 | Tập chỉ số của Bài 3.7.1 | Liên kết rõ đến đề/lời giải gập cuối tài liệu |
| N09 | Bài 3.7.2 và giả thiết xác suất góc | Liên kết bài nguồn; solution cục bộ về giả thiết |
| N10 | ell<a chưa bảo đảm chung thùng; nguồn ngẫu nhiên/số chiều | Khối solution cuối mục Euclid |
| N11 | Khớp điện thoại chưa xác nhận cùng người | Khối solution cuối mục thực thể |
| N12 | Hai cấu trúc cùng 2048 phép thử, Bài 3.8.2 | Liên kết rõ đến đề/lời giải gập cuối tài liệu |
| N13 | Cùng văn bản/cùng chủ đề; quảng cáo dài có từ dừng | Khối solution cuối mục bản tin |
| N14 | Sáu nhiệm vụ tổng hợp | Giữ khối solution hiện có |
| N15 | Hai nhánh đọc thêm đã có lời giải/giới hạn | Không thêm bài bắt buộc; không tính vào 60 phút recitation |
| N16 | Sáu cụm bài nguồn | Giữ nguyên dữ kiện, nhiệm vụ, lời giải và phút |

N02 và ghi chú s02-08 mô tả đúng biến thể: bỏ bước 6 kiểm chữ ký của sách, kiểm gốc bắt buộc cho mọi ứng viên; sách chỉ gắn “tùy chọn” cho bước 7 kiểm gốc. N09 định nghĩa quy tắc ước lượng trước áp dụng, nhưng vẫn dùng vết dấu trước chứng minh hình học; không đổi thứ tự trang. N10 thêm SVG tam giác và chuỗi ell=rho|cos phi| → điều kiện cần phi>pi/3; không ấn định tỷ lệ với a. N11 thu hồi khoảng cách chỉnh sửa trong điểm phạt theo trường. N12 định nghĩa đặc trưng đường vân và truy hồi hợp–hợp–giao–xác minh; không đổi điều kiện hóa của q_T,q_F. N15 giữ công thức hỗn hợp và tách rõ giả thiết đều khỏi riêng ràng buộc 0–90.
