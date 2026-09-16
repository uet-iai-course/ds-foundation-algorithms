# Storyboard Bài 02

## Section 1 — Giới thiệu bài học

### `lec02-s01-01` — Tiêu đề bài học

- **Mục đích:** Xác định tên bài, môn học và học kỳ.
- **Tiêu đề:** Mô hình tính toán Map-Reduce.
- **Môn học:** Giải thuật nền tảng của Khoa học dữ liệu.
- **Học kỳ:** Học kỳ 1 · Năm học 2026–2027.
- **Cách thể hiện:** Tiêu đề lớn ở giữa, tên môn và học kỳ bên dưới.
- **Nguồn nội dung:** Chỉ dẫn trực tiếp của người dùng; thông tin học phần hiện có.

### `lec02-s01-02` — Nội dung

- **Mục đích:** Giới thiệu các phần của bài học sau slide tiêu đề.
- **Hiện trạng:** Bốn mục “Giới thiệu”, “Mô hình tính toán Map-Reduce”, “Các ví dụ Map-Reduce”, “Chi phí và lợi ích của song song hóa”.
- **Quy tắc cập nhật:** Khi thêm section mới, thêm tên phần tương ứng vào slide “Nội dung”.
- **Nguồn:** Chỉ dẫn trực tiếp của người dùng.

### `lec02-s01-03` — Dữ liệu lớn trên nhiều máy

- **Mục đích:** Nhận ra nhu cầu xử lý kho dữ liệu lớn trên các máy phổ thông qua ví dụ Google.
- **Kết nối:** Sau tiêu đề/mục lục; tạo bối cảnh cho các yêu cầu của mô hình tính toán.
- **Cách thể hiện:** Hình chia dữ liệu thành khối A/B/C; máy 1 chứa A/B, máy 2 chứa B/C, máy 3 chứa C/A. Mỗi khối có hai bản sao minh họa trên hai máy khác nhau; ba bài toán với đầu ra rõ: chỉ mục từ, số lượt truy cập theo địa chỉ, liên kết đến trang.
- **Câu chốt:** Dữ liệu nằm ở nhiều nơi; cần tổ chức các máy cùng xử lý.
- **Nguồn:** Dean–Ghemawat, OSDI 2004, mục 1, 2.3, 3, trang 1–3; MMDS Chương 2, trang 21–23. Ba máy là hình minh họa, không phải thống kê Google.

### `lec02-s01-04` — Các yêu cầu của mô hình tính toán

- **Mục đích:** Giải thích bốn nhu cầu do người dùng chỉ định và ý nghĩa “trong suốt” đối với lập trình viên.
- **Mạch:** Dữ liệu phân tán → cần xử lý song song → ưu tiên nơi lưu dữ liệu → hệ thống đảm nhiệm phân chia, lập lịch, chống lỗi và phục hồi.
- **Cách thể hiện:** Bốn ý đánh số, mỗi ý có giải thích trực tiếp; chưa giới thiệu chữ ký hai hàm hoặc công thức.
- **Kết nối:** Thu hồi bối cảnh Google; chuẩn bị cho nội dung mô hình sẽ được người dùng chỉ định tiếp.
- **Nguồn:** Chỉ dẫn người dùng; Dean–Ghemawat, mục 1, 3.1, 3.3, 3.4, trang 1, 3–5. Lập lịch là chọn nơi/lúc chạy; trong suốt không miễn trách nhiệm viết đúng phép tính; chống lỗi không bảo đảm máy luôn hoạt động.

### `lec02-s01-05` — Ví dụ: Cộng dãy số (song song hoá và cục bộ hoá)

- **Mục đích:** Giải thích vì sao cộng cục bộ và gộp các tổng cho cùng kết quả; mở rộng sang toán tử giao hoán, kết hợp.
- **Kết nối vào:** Sau bốn yêu cầu, dùng phép cộng quen thuộc để thể hiện tính toán gần dữ liệu và song song hóa.
- **Ví dụ:** Tính tổng n số; minh họa n=6. Máy1 nhận a1,a4; máy2 nhận a2,a5; máy3 nhận a3,a6. Mỗi số góp đúng một lần.
- **Cách thể hiện:** Ba ô máy chứa phép cộng HTML/KaTeX, ba mũi tên tới tổng chung; hai tính chất kèm ý nghĩa; thay mọi dấu cộng bằng toán tử mới ở cả hai tầng.
- **Giả thiết:** Phép toán chính xác; miền đóng, dãy hữu hạn, các nhóm không rỗng. Bản sao lưu trữ không được cộng lặp. Trường hợp rỗng và số dấu phẩy động giải thích trong notes.
- **Nguồn:** Yêu cầu người dùng; MMDS2.2.4 trang27–29. Không thêm thuật ngữ hệ thống hoặc công thức chi phí.
- **Kết nối ra:** Chuẩn bị cách biểu diễn phép tính cục bộ và gộp; chưa thêm section mới, mục lục vẫn Giới thiệu.

### `lec02-s01-06` — Cụm máy và lưu trữ phân tán HDFS

- Mục đích: chỉ ra đường truyền trong máy, trong rack và giữa các rack; giải thích vì sao đặt tính toán gần khối dữ liệu và đặt bản sao ở khác rack.
- Nối vào: ví dụ cộng cục bộ vừa cho thấy mỗi máy xử lý phần dữ liệu của mình. Slide này làm rõ “gần dữ liệu” trên một cụm máy thực tế.
- Trung tâm: sơ đồ hai tủ rack, mỗi tủ có bộ chuyển mạch nối hai máy; hai bộ chuyển mạch nối qua mạng liên rack. Một tệp gồm khối A và B, mỗi khối có ba bản sao: A ở máy 1/3/4, B ở máy 1/2/3.
- Chạy tay trong lời giảng: mất máy 1 vẫn còn A/B; mất cả rack 1 hoặc rack 2 vẫn còn A/B ở rack kia. Các bản sao không phải dữ liệu mới cần cộng thêm.
- Câu chốt: vị trí khối quyết định đường truyền khi tính toán; bản sao khác rack giúp dữ liệu còn đọc được khi một rack hỏng.
- Giới hạn: chỉ minh họa mạng và máy lưu khối, không phải toàn bộ kiến trúc HDFS; quản lý siêu dữ liệu và điều phối tính toán để trong ghi chú. Không khẳng định hệ thống chịu được mọi tổ hợp lỗi. Ba bản sao là cấu hình minh họa.
- Nguồn: MMDS Chương 2, mục 2.1.1–2.1.2; Apache HDFS Architecture, các mục Moving Computation, Data Replication, Replica Placement, Robustness: https://hadoop.apache.org/docs/current3/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html.
- Theo yêu cầu thêm đúng một slide, giữ section Giới thiệu và mục lục một dòng; chưa lập thời lượng cả bài.

### Bổ sung quy mô cho `lec02-s01-03`

Theo yêu cầu người dùng, mỗi bài toán có số liệu và năm công bố: chỉ mục Google hơn 8 tỷ trang (10/11/2004, Official Google Blog); mẫu 450 GB nhật ký truy vấn đã nén (Pike và cộng sự, Sawzall 2005, trang 26–27); kho thu thập 24 triệu trang với hơn 259 triệu liên kết (Brin–Page 1998, mục 2.2). Không coi ba mốc là cùng thời điểm. Đổi ví dụ đếm lượt truy cập URL thành đếm truy vấn chứa từ khóa theo ngày để đúng bài toán thực nghiệm có số liệu. Quy mô liên kết là quy mô kho web, không phải đo lường tác vụ MapReduce 1998; hơn 8 tỷ trang là quy mô chỉ mục, không phải một lần chạy. Giữ hình khối/bản sao và đầu ra của hai bài toán còn lại.

## Section 2 — Mô hình tính toán Map-Reduce

Người dùng duyệt phần Giới thiệu và yêu cầu mở section mới với đúng hai slide ban đầu. Bài toán đếm từ là ví dụ xuyên suốt section này, không là một phần độc lập. Mạch dự kiến: khả năng của mô hình → đặc tả đếm từ → dùng chính bài toán này giải thích Map, nhóm theo khóa và Reduce ở các slide sẽ soạn sau theo chỉ dẫn. Hiện chưa thêm các slide giải thuật hoặc phân tích chi phí. Ngoại lệ: bài đang xây từng bước, mới có hai section, chưa áp dụng số phần/thời lượng của deck hoàn chỉnh.

### `lec02-s02-01` — 2 · Mô hình tính toán Map-Reduce

- Mục đích: nêu khả năng Map-Reduce đáp ứng các nhu cầu ở phần Giới thiệu; theo điều chỉnh trực tiếp của người dùng, không mô tả cách làm ở đây.
- Nối vào: nhu cầu xử lý trên cụm máy, tính toán gần dữ liệu và chịu lỗi ở phần trước.
- Cách thể hiện: bốn ô có icon SVG nội dòng tương ứng (cụm máy nối mạng; ba tác vụ đồng thời; phép tính cạnh nơi lưu dữ liệu; chuyển tác vụ từ máy lỗi sang máy khác). Mỗi icon có mô tả truy cập, giữ nhãn chữ. Bốn năng lực — dữ liệu phân tán; tính toán song song và tăng năng lực bằng nhiều máy; ưu tiên tính gần dữ liệu; điều phối và phục hồi tự động.
- Câu chốt: mô hình giúp thực hiện phép tính trên cụm máy và giao việc tổ chức thực thi cho hệ thống.
- Giới hạn: không hứa tăng tốc tuyến tính, không bảo đảm mọi bài toán hay tổ hợp lỗi. Không đưa khóa/giá trị hoặc sơ đồ Map → Reduce lên slide này.
- Nối ra: dùng đếm từ làm ví dụ cụ thể để tìm hiểu cơ chế trong các bước sau.
- Nguồn: MMDS 2.2 mở đầu, trang 25 và 2.2.5; Dean–Ghemawat 2004, tóm tắt, mục 3.1, 3.3, 3.4.

### `lec02-s02-02` — Ví dụ: Đếm tần suất xuất hiện từ

- Mục đích: nêu chính xác đầu vào, đầu ra và đại lượng cần đếm trước khi giải bằng Map-Reduce.
- Đầu vào: $n\geq1$ văn bản $d_1,\ldots,d_n$, đã tách từ theo quy tắc thống nhất; $V$ là tập từ xuất hiện.
- Đầu ra: mỗi $w\in V$ có một cặp $(w,c(w))$; $c_i(w)$ là số lần $w$ xuất hiện trong $d_i$, và $c(w)=\sum_{i=1}^{n}c_i(w)$.
- Khó khăn: đầu vào nằm trên nhiều máy và có thể vượt bộ nhớ một máy; cùng từ xuất hiện ở nhiều nơi nên cần gộp số đếm, hạn chế chuyển toàn bộ văn bản.
- Cách thể hiện: nội dung đặc tả ở cột trái khoảng 70%, gồm đầu vào/đầu ra, một công thức chính và hai khó khăn ngắn. Cột phải khoảng 30% minh họa các tờ văn bản riêng mang nhãn $d_1$, $d_2$, …, $d_n$ → bảng từ/số lần, dùng đúng ký hiệu của đặc tả; không thêm dữ kiện số hoặc các bước thuật toán. Công thức và bảng dựng bằng HTML/KaTeX, mũi tên SVG. Chi tiết chỉ số vị trí và văn bản rỗng ở notes.
- Nguồn: MMDS 2.2.1–2.2.3, ví dụ 2.1–2.2, trang 25–27. Ký hiệu đặc tả được viết lại để gần phép cộng phần trước, không thêm dữ kiện số.
- Giới hạn: tần suất ở đây là số lần xuất hiện, không là tần suất tương đối hoặc số văn bản chứa từ. Tách từ ngoài phạm vi; tập đầu ra rỗng nếu mọi văn bản rỗng. Không đếm lặp bản sao vật lý.
- Nối ra: giữ nguyên $w$ và $c(w)$ khi xây Map/Reduce sau này. Chỉ đặc tả bài toán trong lần sửa này, chưa viết lời giải.

### `lec02-s02-03` — Map và Reduce cho bài toán đếm từ

- Mục đích: mô tả hai hàm giải đúng bài toán vừa đặc tả; từ $w$ là khóa, giá trị 1 biểu thị một lần xuất hiện.
- Mạch: đặc tả $c(w)$ → phát một đơn vị cho mỗi lần gặp từ → hệ thống nhóm theo từ, giữ các phần tử lặp → cộng danh sách số đếm.
- Cách thể hiện: hai khối Map/Reduce, giả mã ngắn; dải nối nêu trách nhiệm nhóm của hệ thống. Chưa gộp cục bộ trong Map, tránh lẫn với bộ gộp tối ưu hóa.
- Đúng: mỗi lần xuất hiện tạo đúng một đơn vị và được cộng đúng một lần cho cùng từ, nên đầu ra đúng $c(w)=\sum_i c_i(w)$. Tính hữu hạn, văn bản rỗng và chi phí duyệt/cộng ở notes.
- Nguồn: MMDS 2.2.1–2.2.3, ví dụ 2.1–2.2, trang 25–27; Dean–Ghemawat 2004, mục 2.1.
- Nối ra: hai hàm chưa nói máy nào chạy; slide sau giải thích tác vụ và điều phối.

### `lec02-s02-04` — Hệ thống phối hợp và phân phối tác vụ

- Mục đích: phân biệt hàm, tác vụ và máy; theo được phân chia đầu vào, giao việc và chuyển dữ liệu theo từ.
- Hình: ví dụ ba tác vụ Map ở ba máy; hai tác vụ Reduce ở máy 1 và máy 3. Đây là sơ đồ bố trí minh họa, không số liệu hiệu năng hay quy định số máy.
- Bộ điều phối giao tác vụ cho máy rảnh, ưu tiên dữ liệu gần; một tác vụ Map xử lý nhiều bản ghi trong phần đầu vào; một tác vụ Reduce xử lý nhiều khóa và gọi hàm Reduce cho từng khóa.
- Một máy có thể chạy nhiều tác vụ; một tác vụ logic có thể có nhiều lượt thực thi trên các máy khác nhau để dự phòng. Hệ thống không cộng lặp kết quả của các lượt thực thi. Phân biệt dư thừa tính toán với nhân bản khối HDFS (Dean–Ghemawat 2004, mục 3.3, 3.6).
- Mọi cặp cùng từ đi tới cùng một tác vụ Reduce. Các máy truyền dữ liệu trung gian trực tiếp, không chuyển toàn bộ qua bộ điều phối. Máy có thể nhận nhiều tác vụ theo lịch.
- Nguồn: MMDS 2.2, trang 25–28; Dean–Ghemawat 2004, mục 3.1. Chi tiết lập lịch, truyền có thể chồng lấp với Map và phục hồi ở notes.
- Nối ra: chạy tay dữ liệu nhỏ để kiểm tra đường đi từ văn bản đến kết quả.

### `lec02-s02-05` — Ví dụ: Chạy Map-Reduce để đếm từ

- Mục đích: tự theo dõi các cặp được phát, nhóm và cộng; phân biệt số lần xuất hiện với số văn bản chứa từ.
- Theo yêu cầu ví dụ cụ thể, chọn dữ kiện minh họa: $d_1$ = “mèo chó mèo”, $d_2$ = “chó chim”; tách theo khoảng trắng. Đây là dữ liệu do người soạn chọn theo yêu cầu, không trích nguyên văn giáo trình.
- Map văn bản 1 phát (mèo,1), (chó,1), (mèo,1); Map văn bản 2 phát (chó,1), (chim,1).
- Nhóm: mèo → [1,1], chó → [1,1], chim → [1]. Reduce: (mèo,2), (chó,2), (chim,1). Kiểm tra tổng số đếm là 5, bằng tổng số lần xuất hiện.
- Cách thể hiện: ba cột có nhãn vai trò; các nhóm không được gọi là máy hoặc tác vụ riêng. Giữ mọi phần tử lặp; thứ tự hàng đầu ra không là yêu cầu bài toán.
- Nguồn cơ chế: MMDS 2.2.1–2.2.3. Không mở thêm section; mục lục vẫn hai mục.

### Cụm hình thức hóa mô hình tổng quát

Theo yêu cầu, nối từ ví dụ đếm từ sang chữ ký hai hàm, nhóm/phân phối, các pha và thuật toán hình thức. Giữ trong section 2, mục lục không thêm mục. Dùng quy ước đầu ra là cặp theo MMDS; bài báo Dean–Ghemawat dùng chữ ký Reduce hẹp hơn nên không coi hai cách ký hiệu là đồng nhất. Phân biệt một công việc với chuỗi nhiều công việc. Ký hiệu $A^*$ chỉ các dãy hữu hạn phần tử thuộc $A$, gồm dãy rỗng; giữ số lần lặp, không dùng phép hợp tập hợp làm mất số đếm.

### `lec02-s02-06` — Hình thức hóa hàm Map

- Mục đích: đọc được $\mathrm{Map}:K_1\times V_1\to(K_2\times V_2)^*$ và hiểu mỗi lần gọi có thể phát không, một hoặc nhiều cặp.
- Đầu vào: một cặp mã/nội dung; đầu ra: dãy cặp trung gian. $K_1,V_1$ và $K_2,V_2$ là các miền khóa/giá trị.
- Hình: một cặp → Map → dãy cặp; đối chiếu $(i,d_i)$ và các cặp (từ,1) của ví dụ. Một văn bản giữ một nhãn; không vẽ hàm như một máy.
- Nguồn: MMDS 2.2.1 trang25–26; Dean–Ghemawat 2004, mục2.2.

### `lec02-s02-07` — Hình thức hóa hàm Reduce

- Mục đích: đọc $\mathrm{Reduce}:K_2\times V_2^*\to(K_3\times V_3)^*$, nhận một khóa và các giá trị cùng khóa, phát không hoặc nhiều cặp đầu ra.
- Hình: $(k,L_k)$ → Reduce → dãy cặp kết quả; liên hệ mèo,[1,1] → (mèo,2).
- Giới hạn: $K_3,V_3$ có thể khác miền trung gian; Reduce tổng quát không bắt buộc là phép cộng hoặc một phép toán hai ngôi giao hoán/kết hợp. Nếu muốn kết quả không phụ thuộc thứ tự giá trị, hàm trên danh sách phải bất biến với hoán vị hoặc quy định thêm thứ tự.
- Nguồn: MMDS 2.2.3 trang27. Trong công việc chỉ gọi Reduce cho khóa thực sự xuất hiện nên nhóm không rỗng.

### `lec02-s02-08` — Phân phối và nhóm theo khóa

- Mục đích: từ dãy cặp trung gian $I$, xác định danh sách $L_k$ và tác vụ nhận nó mà không làm mất phần tử lặp.
- $r\geq1$ là số tác vụ Reduce; $p:K_2\to\{0,\ldots,r-1\}$ phân công khóa. Các cặp cùng khóa đến cùng tác vụ; hai khóa khác nhau có thể đến cùng tác vụ nhưng không gộp thành một nhóm.
- Hình: các cặp → hai nhóm riêng → một tác vụ Reduce có thể nhận cả hai. Ví dụ minh họa mèo/chó có thể cùng được $p$ gán vào tác vụ0; không tuyên bố đây là giá trị của một hàm băm cụ thể.
- Nguồn: MMDS 2.2.2 trang26–27 và chú thích về hàm phân phối. Hệ thống không bảo đảm thứ tự giá trị trong nhóm; bộ điều phối không phải điểm tập trung toàn bộ dữ liệu trung gian.

### `lec02-s02-09` — Các pha của một công việc Map-Reduce

- Mục đích: theo dõi kiểu dữ liệu qua chia đầu vào → Map → phân phối/nhóm → Reduce.
- Hình: bốn khối theo chiều đọc; ghi người viết hai hàm, hệ thống chia và tổ chức dữ liệu. $X$ là đầu vào; $B_1,\ldots,B_m$ là các phần theo vị trí bản ghi; $I$ là toàn bộ dữ liệu trung gian phân tán; $Y$ là kết quả.
- Phân biệt: một pha gồm nhiều tác vụ; một tác vụ có thể gọi hàm nhiều lần; đây là pha logic, truyền dữ liệu có thể chồng lấp thực thi Map.
- Nguồn: MMDS2.2 hình2.2; Dean–Ghemawat2004 mục3.1. Chia thành bốn pha để làm rõ việc phân chia đầu vào; không thêm công việc lặp mới.

### `lec02-s02-10` — Mô hình Map-Reduce: mô tả hình thức

- Mục đích: đọc thuật toán tổng quát có đầu vào, tham số, khởi tạo, các vòng lặp song song, nhóm và đầu ra.
- Đầu vào: dãy hữu hạn $X$, Map, Reduce, $m,r\geq1$, hàm phân phối $p$. Khởi tạo các dãy kết quả $O_t$ rỗng; chia $X$ theo vị trí để bản ghi giống nhau vẫn được xử lý đủ lần.
- Trọng tâm: giả mã; “gom giữ lặp” nối các dãy mà giữ mọi phần tử, không cam kết thứ tự kết quả toàn cục. Không dùng hình trang trí bên cạnh giả mã.
- Notes: đặc tả logic, không yêu cầu hiện thực quét lại $I$ cho mỗi khóa hoặc dồn $I$ về một máy. Giả thiết các lần gọi hữu hạn/kết thúc, ổn định theo thứ tự đã quy định; chạy lại/dự phòng không tăng số đóng góp logic. $X$ rỗng hoặc Map không phát gì cho đầu ra rỗng. Chứng minh bảo toàn đóng góp và nhóm theo khóa, không khẳng định hai hàm bất kỳ tự giải đúng bài toán mong muốn.
- Nguồn: hình thức hóa từ MMDS2.2.1–2.2.3 và Dean–Ghemawat2004 mục3.1. Không nêu độ phức tạp hoặc tăng tốc chung khi chưa chọn hàm và mô hình chi phí.

### `lec02-s02-11` — Gộp cục bộ trước khi Reduce: hàm Combine

- Vị trí: sau mô hình hình thức cơ bản, giữ trong section 2. Điểm vào: danh sách cùng khóa có thể dài; phép cộng đã được giới thiệu là kết hợp và giao hoán.
- Mục đích: giải thích gộp cục bộ trước khi truyền và điều kiện bảo toàn kết quả.
- Ví dụ giữ nguyên hai văn bản: Map1 gộp hai cặp (mèo,1) thành (mèo,2); Map2 giữ (chó,1), (chim,1). Năm cặp giảm còn bốn; Reduce cuối vẫn cho mèo2, chó2, chim1. Sơ đồ hai hàng, phân biệt dữ liệu trước/sau Combine.
- Điều kiện đủ của phép gộp đang trình bày: kết hợp, giao hoán, giữ khóa, đóng trên kiểu trung gian và tương thích với phép gộp của Reduce. Không áp đặt điều kiện này lên Reduce tổng quát.
- Combine là tùy chọn; không dùng hoặc gộp lặp nhiều tầng vẫn đúng. Không bảo đảm danh sách luôn ngắn hoặc toàn bộ dữ liệu vừa RAM.
- Notes: chứng minh bảo toàn tổng từng khóa; trung bình cần trạng thái (tổng,số lượng), không lấy trung bình của các trung bình. Kiểm tra miệng: giải thích vì sao hai cặp chó vẫn phải gặp nhau ở Reduce.
- Chi phí: chỉ đếm số cặp truyền 5→4, không suy ra số byte giảm 20% hoặc tăng tốc 20%; thêm chi phí gộp tại Map.
- Nguồn: MMDS mục 2.2.4, trang 27–28; Dean–Ghemawat 2004 mục 4.3. Chu trình rút gọn trong một slide vì là tối ưu bổ sung cho mô hình vừa học. Dự kiến 4 phút trong bài đang xây từng phần, chưa chốt tổng thời lượng.

### `lec02-s02-12` — Câu hỏi kiểm tra

- Vị trí: cuối section 2, sau Combine. Mục đích: kiểm tra khả năng theo dõi dữ liệu và phân biệt khóa, tác vụ, máy.
- Dữ kiện giữ nguyên $d_1$ = “mèo chó mèo”, $d_2$ = “chó chim”, mỗi văn bản giao một tác vụ Map; Map phát (từ,1), Combine và Reduce cộng.
- Ba câu: xác định cặp sau Combine; danh sách và đầu ra Reduce cho chó; giải thích hai khóa chung tác vụ và nhiều tác vụ trên một máy.
- Đáp án trong notes: Map1 (mèo,2),(chó,1); Map2 (chó,1),(chim,1); chó nhận [1,1], trả (chó,2); khóa khác nhau có thể cùng tác vụ nhưng nhóm riêng, một máy có thể chạy nhiều tác vụ.
- Không thêm hình vì sản phẩm học tập là sinh viên tự mô phỏng từ dữ kiện ngắn. Dự kiến 3 phút, kiểm tra trên lớp theo yêu cầu người dùng; không là bài tập recitation trích nguồn. Cơ sở: mô hình và ví dụ đã đối chiếu MMDS 2.2.1–2.2.4.
- Kết section mô hình tại đây. Hệ thống và Chi phí được tách thành hai section chính riêng trong outline; chưa triển khai trong lần sửa này.

## Section 3 — Các ví dụ Map-Reduce

Chức năng: vận dụng mô hình đã học để chọn khóa, giá trị trung gian và phép gộp; chứng minh bảo toàn đóng góp và kết quả. Điểm vào: Map/Reduce/Combine ở section 2; điểm ra: ba thuật toán để dùng tiếp khi học hệ thống và chi phí. Không thêm hai section đó trong lần này.

Theo chỉ dẫn cụ thể, mỗi bài giữ đúng thứ tự: bài toán hình thức → ứng dụng → đặc điểm và ý tưởng → các hàm → ví dụ → chứng minh. Đây là ngoại lệ có chủ đích so với chu trình mặc định. Ví dụ số tự chọn theo yêu cầu, không phải số liệu thực nghiệm hoặc bài recitation nguyên văn. Thời lượng dự kiến 49 phút cho section (gồm ba slide ứng dụng mới); bài vẫn đang được xây từng phần, chưa chốt tổng 120+60 phút.

### `lec02-s03-01` — Mở phần: Các ví dụ Map-Reduce

- Mục đích: Chọn khóa và giá trị theo đầu ra cần tính.
- Câu chốt và kết nối: Mô hình chung → ba kiểu gộp: tổng theo hàng, hiện diện theo từ, tổng và số lượng.
- Nội dung, cách thể hiện: Ba hàng giới thiệu, chưa thêm đặc tả.
- Nguồn: MMDS 2.3.1; bài 2.3.1(b,d), tr.40.
- Thời lượng dự kiến: 1 phút.

### `lec02-s03-02` — Bài toán nhân ma trận–véc tơ

- Mục đích: Phát biểu đúng đầu vào, đầu ra và giả thiết.
- Câu chốt và kết nối: Ma trận A kích thước p×q, véc tơ v có q phần tử → y=Av có p phần tử; mỗi tọa độ góp đúng một lần.
- Nội dung, cách thể hiện: Công thức trung tâm; p,q>=1, đủ pq tọa độ cả 0, v vừa RAM mỗi Map, số học chính xác.
- Nguồn: MMDS 2.3.1, tr.31–32 và bài 2.3.2, tr.40.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-06a` — Ứng dụng: Tương đồng trang web và truy vấn

- Vị trí: ngay sau lec02-s03-02 (phát biểu bài toán), trước lec02-s03-03 (đặc điểm và ý tưởng).
- Mục đích: Ánh xạ trang web và truy vấn vào bài toán nhân ma trận–véc tơ.
- Câu chốt và dữ kiện: A: trang×từ; v: truy vấn; y: điểm cosine. Các hàng A và v khác 0 trước chuẩn hóa, có độ dài Euclid1.
- Cách thể hiện và notes: Hai thẻ biểu diễn, công thức y=Av và sơ đồ nhân. Notes phân biệt điểm số với bước xếp hạng; ví dụ9,8,9,11 ở slide ví dụ sau chưa chuẩn hóa.
- Nguồn: Introduction to Information Retrieval, 6.3.1–6.3.2; MMDS 2.3.1.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-03` — Nhân ma trận–véc tơ: đặc điểm và ý tưởng

- Mục đích: Giải thích chọn khóa hàng i.
- Câu chốt và kết nối: Các tích nằm phân tán → nhóm đúng các tích của một hàng.
- Nội dung, cách thể hiện: Icon cạnh đặc điểm và hình ba máy: máy1 chứa B1/B2, máy2 B2/B3, máy3 B3/B1. Ba khối logic, mỗi khối hai bản sao minh họa. Mỗi bản ghi logic chỉ góp một lần; khối không bắt buộc tương ứng một hàng.
- Nguồn: MMDS 2.3.1–2.3.2, tr.31–32.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-04` — Nhân ma trận–véc tơ: các hàm

- Mục đích: Đọc được Map và phép gộp dùng chung.
- Câu chốt và kết nối: Map(B) duyệt mọi bản ghi (i,j,a_ij) trong khối và yield(i,a_ij*v[j]); Combine và Reduce yield tổng cùng khóa hàng.
- Nội dung, cách thể hiện: Giả mã ngắn, danh sách L được định nghĩa; Combine tùy chọn.
- Nguồn: MMDS 2.3.1; 2.2.4.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-05` — Nhân ma trận–véc tơ: Ví dụ

- Mục đích: Tái tạo đủ các tích và kết quả.
- Câu chốt và kết nối: A=[[1,2,0,1],[0,1,2,0],[2,0,1,1],[1,1,0,2]], v=[1,2,3,4] → y=[9,8,9,11].
- Nội dung, cách thể hiện: Bốn khối2×2 B11,B12,B21,B22; đường chia hàng/cột trong ma trận. Map mỗi khối yield4cặp; Combine mỗi khối tạo2tổng theo hàng. Bảng hiển thị đủ16cặp. Reduce nhận [5,4],[2,6],[2,7],[3,8].
- Nguồn: Ví dụ tự chọn từ thuật toán MMDS 2.3.1.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-06` — Nhân ma trận–véc tơ: tính đúng

- Mục đích: Chứng minh kết quả cho hàng i bất kỳ.
- Câu chốt và kết nối: Đủ và không lặp các tích của hàng i; gộp giữ tổng → y_i đúng.
- Nội dung, cách thể hiện: Ba bước suy luận; notes hàng toàn 0 và giới hạn số dấu phẩy động.
- Nguồn: Suy diễn từ đặc tả MMDS 2.3.1.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-07` — Đếm từ phân biệt: bài toán

- Mục đích: Phân biệt số loại từ với số lần xuất hiện.
- Câu chốt và kết nối: W_i là tập từ trong d_i; D là kích thước hợp các W_i.
- Nội dung, cách thể hiện: Công thức và giả thiết tách từ nhất quán; tất cả rỗng trả 0.
- Nguồn: Bài MMDS 2.3.1(d), tr.40, đổi miền theo user.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-11a` — Ứng dụng: Kích thước từ vựng

- Vị trí: ngay sau lec02-s03-07 (phát biểu bài toán), trước lec02-s03-08 (đặc điểm và ý tưởng).
- Mục đích: Dùng số từ phân biệt để biết số chiều biểu diễn theo toàn bộ từ vựng.
- Câu chốt và dữ kiện: D=3 với mèo,chó,chim; q=D khi không chọn lọc thêm từ.
- Cách thể hiện và notes: Sơ đồ kho → từ duy nhất → kích thước. Đếm D không tự gán chỉ số cột.
- Nguồn: Ứng dụng bài MMDS2.3.1(d), tr.40; IR6.3.2.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-08` — Từ phân biệt: đặc điểm và ý tưởng

- Mục đích: Giải thích cần loại trùng toàn cục trước khi cộng.
- Câu chốt và kết nối: Trùng trong/giữa văn bản → công việc1 loại trùng → công việc2 đếm.
- Nội dung, cách thể hiện: Icon cạnh đặc điểm và sơ đồ hai công việc; g là khóa chung cố định.
- Nguồn: MMDS 2.2; 2.3.5; bài 2.3.1(d).
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-09` — Từ phân biệt: các hàm

- Mục đích: Theo dõi đầu ra công việc1 trở thành đầu vào công việc2.
- Câu chốt và kết nối: Công việc1 mỗi từ phát1 đại diện; công việc2 đưa mỗi đại diện về g để cộng.
- Nội dung, cách thể hiện: Bảng/khối hai công việc, Map/Combine/Reduce mỗi công việc; rỗng do chương trình điều phối trả 0.
- Nguồn: Lời giải diễn giải bài MMDS 2.3.1(d).
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-10` — Từ phân biệt: chạy tay

- Mục đích: Tính số loại từ qua hai công việc.
- Câu chốt và kết nối: mèo chó mèo / chó chim → mèo,chó,chim → D=3.
- Nội dung, cách thể hiện: Hiển thị cặp Map, Combine, nhóm và kết quả; 5 lần xuất hiện, 3 loại từ; cộng cục bộ 2+2 sai.
- Nguồn: Dùng lại ví dụ section2, thuật toán từ nguồn.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-11` — Từ phân biệt: tính đúng

- Mục đích: Chứng minh không thiếu và không đếm lặp từ.
- Câu chốt và kết nối: Từ xuất hiện ↔ đúng1 cặp công việc1; công việc2 cộng1 mỗi cặp.
- Nội dung, cách thể hiện: Lập luận hai chiều, Combine giữ hiện diện; trường hợp rỗng.
- Nguồn: Suy diễn từ đặc tả hai công việc.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-12` — Trung bình cộng: bài toán

- Mục đích: Nêu miền n>=1 và đầu ra trung bình.
- Câu chốt và kết nối: Dãy a_1..a_n → tổng chia n; giữ các vị trí dù giá trị trùng.
- Nội dung, cách thể hiện: Công thức trung tâm, số học chính xác; n=0 không xác định.
- Nguồn: MMDS bài 2.3.1(b), tr.40; mở miền sang thực.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-16a` — Ứng dụng: Số từ trung bình mỗi trang

- Vị trí: ngay sau lec02-s03-12 (phát biểu bài toán), trước lec02-s03-13 (đặc điểm và ý tưởng).
- Mục đích: Diễn giải trung bình như thống kê độ dài trang.
- Câu chốt và dữ kiện: Hai trang có3và2từ; trạng thái(3,1),(2,1) → tổng5,sốtrang2 →2,5từ/trang.
- Cách thể hiện và notes: Sơ đồ tổng–số lượng và công thức; đếm trang rỗng trong mẫu số, không có trang thì không xác định.
- Nguồn: Ứng dụng bài MMDS2.3.1(b), tr.40.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-13` — Trung bình cộng: đặc điểm và ý tưởng

- Mục đích: Nhận ra vì sao phải giữ tổng cùng số lượng.
- Câu chốt và kết nối: [2,4] và [9] có kích thước khác nhau; trung bình các trung bình 6 sai, kết quả đúng 5.
- Nội dung, cách thể hiện: Icon các phần không đều, số lượng, phép gộp; sơ đồ trạng thái (s,c).
- Nguồn: Diễn giải bài 2.3.1(b) bằng cơ chế Combine 2.2.4.
- Thời lượng dự kiến: 2 phút.

### `lec02-s03-14` — Trung bình cộng: các hàm

- Mục đích: Phân biệt kiểu đầu ra Combine với Reduce.
- Câu chốt và kết nối: Map phát (a_i,1); Combine cộng tổng/đếm; Reduce chia sau khi gộp toàn bộ.
- Nội dung, cách thể hiện: Giả mã/bảng hàm ngắn, g là khóa chung, L là danh sách trạng thái.
- Nguồn: Lời giải bài MMDS 2.3.1(b).
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-15` — Trung bình cộng: chạy tay

- Mục đích: Tính được trạng thái qua từng bước.
- Câu chốt và kết nối: [2,4]|[9] → (6,2),(9,1) → (15,3) → 5.
- Nội dung, cách thể hiện: Bảng cặp Map và Combine; Reduce nhận đủ trạng thái, chia một lần.
- Nguồn: Ví dụ tự chọn theo yêu cầu.
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-16` — Trung bình cộng: tính đúng

- Mục đích: Dùng bất biến tổng và số lượng để chứng minh.
- Câu chốt và kết nối: Mỗi trạng thái tóm tắt một nhóm vị trí rời nhau; cộng bảo toàn → (tổng,n).
- Nội dung, cách thể hiện: Cơ sở một phần tử, bước gộp, kết luận n>0; notes kết thúc hữu hạn.
- Nguồn: Suy diễn từ đặc tả bài MMDS 2.3.1(b).
- Thời lượng dự kiến: 3 phút.

### `lec02-s03-17` — Câu hỏi kiểm tra

- Mục đích: Giải thích quyết định thiết kế trong cả ba bài.
- Câu chốt và kết nối: Khóa hàng; loại trùng trước khi đếm; giữ cặp tổng–số lượng.
- Nội dung, cách thể hiện: Ba câu hỏi, đáp án trong notes; dùng lại dữ kiện đã học.
- Nguồn: Kiểm tra ngắn theo yêu cầu, không recitation.
- Thời lượng dự kiến: 3 phút.


## Section 4 — Chi phí và lợi ích của song song hóa

Phần này nối từ các hàm và thuật toán đã đặc tả sang cách đánh giá một phương án chạy trên nhiều máy. Ba góc nhìn là công việc, thời gian hoàn thành và lượng truyền. Mô hình chi phí đầu vào của sách MMDS được giới thiệu riêng để không nhầm với lượng byte thực sự qua mạng. Các ví dụ cộng dãy số và đếm từ được dùng lại, không đưa thêm thuật toán hoặc kiến thức CSDL.

Chuỗi suy luận: phân biệt đơn vị → đếm công việc → đọc lịch chạy → tính thời gian cộng dãy số → đếm đầu vào tác vụ → thời gian một truyền → đường nối dùng chung → Combine → ghép các pha → tăng tốc → vận dụng. Với mỗi mô hình, hình chỉ ra nơi phát sinh chi phí, ví dụ cho phép tính lại và công thức khái quát có giả thiết. Không áp dụng bước giả mã/chứng minh thuật toán mới vì đây là phân tích các thuật toán đã học; thay bằng suy ra công thức từ quy tắc đếm và lịch chạy.

Nguồn: sách MMDS `sources/textbooks/ch2n.pdf`, 2.5.1–2.5.2 trang 53–56; 2.2.4 trang 27–28; 2.1.1 trang 22–23. Đối chiếu slide MMDS 38–40 và Stanford CS246 67–70: hai bộ dùng tổng đọc/ghi, sách dùng kích thước đầu vào. Chọn sách cho $C$; giữ riêng $V$ cho đường truyền được xét. Bổ sung được duyệt: Cornell CS5220 [độ trễ–băng thông](https://www.cs.cornell.edu/courses/cs5220/2020fa/lec/2020-10-06-intro.html) và [mức tăng tốc](https://www.cs.cornell.edu/courses/cs5220/2020fa/lec/2020-09-08-perf-basics.html). Không dùng tốc độ mạng lịch sử của sách như thông số hiện tại.

Dữ kiện số là minh họa mô hình theo yêu cầu giảng viên, không phải phép đo hệ thống hay bài tập nguyên văn. Giới hạn quy mô được thể hiện bằng phần dữ liệu phải đi qua đường nối dùng chung và tải của máy bận nhất; con số nhỏ chỉ giúp tính tay, không mô tả quy mô Google. Đầu ra của phần là bộ công thức có điều kiện áp dụng để đánh giá và so sánh cách tổ chức các tác vụ. Nội dung hệ thống chi tiết vẫn ở mức kế hoạch.

Thời lượng: 27,5 phút cho 11 slide. Toàn deck hiện 49 slide, bốn section chính. Đây là ngoại lệ theo yêu cầu xây bài từng phần, chưa tuyên bố đủ toàn bài 120 phút và recitation 60 phút; câu hỏi cuối phần là tương tác tại lớp. Sáu SVG chính có mã tái tạo tại `img/lec-02/scripts/render-cost-figures.py`; hình nhỏ còn lại là SVG nội dòng.

### `lec02-s04-01` — Chi phí và lợi ích của song song hóa

- **Mục đích / sản phẩm:** Phân biệt đại lượng và đơn vị trước khi so sánh hai cách thực hiện.
- **Câu chốt:** $W$ đếm phép toán, $T_P$ đo thời gian, $V$ đếm byte qua mạng.
- **Vai trò:** Mở phần và xác lập mô hình
- **Kiến thức đầu vào:** Đặc tả Map/Reduce/Combine, ba ví dụ trước.
- **Cách thể hiện:** Ba ô có biểu tượng và nhãn; định nghĩa $P$ số máy, phân biệt $p$ số hàng ma trận.
- **Kết nối vào–ra:** Từ cách viết các hàm sang cách đánh giá; tạo ba góc nhìn cho các slide tiếp theo.
- **Kiểm tra và ghi chú:** Notes giải thích không cộng trực tiếp đại lượng khác đơn vị.
- **Nguồn:** MMDS 2.5, trang 53–56; cách chia ba góc nhìn theo yêu cầu.
- **Thời lượng:** 2 phút

### `lec02-s04-02` — Tổng công việc: cộng 16 số

- **Mục đích / sản phẩm:** Đếm công việc của mọi máy, kể cả các phép cộng chạy đồng thời.
- **Câu chốt:** $W_P=P(n/P-1)+(P-1)=n-1$ trong quy ước đang xét.
- **Vai trò:** Ví dụ và khái quát quy tắc đếm
- **Kiến thức đầu vào:** $W$ và $P$ từ slide mở; phép cộng tại máy rồi gộp.
- **Cách thể hiện:** Hai hình: 1 máy dùng 15 phép cộng; 4 máy dùng $4\times3+3=15$. Công thức dưới hình; $n$ và $W_P$ định nghĩa trước công thức.
- **Kết nối vào–ra:** Từ đơn vị phép toán tới tổng công việc; tạo dữ kiện giữ nguyên cho slide thời gian.
- **Kiểm tra và ghi chú:** Khởi tạo bằng phần tử đầu; số học chính xác, $n\geq P\geq1$, $n$ chia hết cho $P$. Bỏ chi phí khác; notes xét nhóm một phần tử.
- **Nguồn:** Suy ra từ cách cộng đã học; liên hệ MMDS 2.5; số 16/4 là minh họa.
- **Thời lượng:** 3 phút

### `lec02-s04-03` — Thời gian của một pha

- **Mục đích / sản phẩm:** Tính thời gian một pha từ tổng tải trên từng máy.
- **Câu chốt:** $T_{\mathrm{pha}}=\max_m t_m=\max(4,6,3)=6$ giây.
- **Vai trò:** Trực giác từ lịch chạy và hình thức hóa
- **Kiến thức đầu vào:** $T_P$, tác vụ và máy; phép cộng thời gian.
- **Cách thể hiện:** SVG cost-03: năm tác vụ trên ba hàng máy; cùng thang 150 px/giây, từ 0 đến 6. $t_m$ là tổng thời gian tác vụ giao máy $m$.
- **Kết nối vào–ra:** Sau tổng công việc, chuyển sang thời gian hoàn thành; dùng quy tắc lấy lớn nhất cho ví dụ cộng.
- **Kiểm tra và ghi chú:** Tất cả tác vụ sẵn sàng từ 0, mỗi máy chạy lần lượt không nghỉ và không lỗi. Phân biệt tác vụ dài nhất 3 giây với máy bận nhất 6 giây.
- **Nguồn:** MMDS 2.5.2, trang 55–56; lịch giả định.
- **Thời lượng:** 2,5 phút

### `lec02-s04-04` — Cộng 16 số trên 4 máy

- **Mục đích / sản phẩm:** Tính thời gian và đối chiếu với công việc đã đếm.
- **Câu chốt:** Tổng công việc vẫn 15 phép cộng; thời gian tính giảm từ $15\tau$ xuống $6\tau$.
- **Vai trò:** Áp dụng mô hình thời gian
- **Kiến thức đầu vào:** Hai slide trước; $\tau>0$ được định nghĩa là thời gian một phép cộng.
- **Cách thể hiện:** SVG cost-04: thanh tuần tự 15 đơn vị; bốn máy cùng cộng từ 0–3, máy 1 gộp từ 3–6; thang 60 px mỗi đơn vị. Hai dòng công thức $T_1,T_4$ và $T_P=(n/P-1)\tau+(P-1)\tau$.
- **Kết nối vào–ra:** Dùng lại 16 số/4 máy để phân biệt công việc và thời gian; chuẩn bị xét chi phí dữ liệu đã bỏ qua.
- **Kiểm tra và ghi chú:** Dữ liệu cục bộ; chia đều, $n$ chia hết $P$; một máy gộp tuần tự; bỏ đọc/ghi, truyền và điều phối. Notes nêu gộp theo cây là lịch khác, kiểm $P=1$ và $n=P$.
- **Nguồn:** Suy ra từ mô hình đã định nghĩa; MMDS 2.5.2.
- **Thời lượng:** 2,5 phút

### `lec02-s04-05` — Chi phí đầu vào tác vụ C

- **Mục đích / sản phẩm:** Tính tổng đầu vào các tác vụ và dùng đại lượng này để so sánh hai cách tổ chức cùng bài toán.
- **Câu chốt:** $C=I+H=100+40=140$ MB, gồm cả đọc cục bộ.
- **Vai trò:** Định nghĩa và ví dụ tính chi phí dữ liệu
- **Kiến thức đầu vào:** Luồng Map → Reduce; byte là đơn vị kích thước.
- **Cách thể hiện:** SVG cost-05 gồm đầu vào Map, Map, đầu vào Reduce, Reduce, đầu ra cuối. Định nghĩa $I,H$ trước công thức; đầu ra cuối ghi không tính vào $C$.
- **Kết nối vào–ra:** Từ số phép tính sang lượng dữ liệu phải đọc; C chưa cho thời gian hoàn thành. Slide sau mới giới thiệu V để chuyển sang thời gian truyền.
- **Kiểm tra và ghi chú:** Một công việc, không chạy lại; Combine nằm trong Map. Notes giải thích trung gian tính tại đầu vào Reduce, không cộng đầu ra lần nữa; nếu một dữ liệu vào nhiều tác vụ, tính mỗi lần.
- **Nguồn:** MMDS 2.5.1, trang 54–55. Notes đối chiếu quy ước tổng đọc/ghi ở hai bộ slide.
- **Thời lượng:** 2,5 phút

### `lec02-s04-06` — Băng thông và thời gian truyền

- **Mục đích / sản phẩm:** Tính thời gian một thông điệp từ dung lượng, băng thông và độ trễ.
- **Câu chốt:** $T_{\mathrm{truyền}}\approx\lambda+V/B=0{,}02+100/50=2{,}02$ giây.
- **Vai trò:** Mô hình băng thông và thay số
- **Kiến thức đầu vào:** Byte và giây; slide này mới định nghĩa $V$ trên một đường truyền, $B$ là số byte chuyển mỗi giây và $\lambda$ là độ trễ khởi đầu.
- **Cách thể hiện:** SVG nội dòng: thông điệp 100 MB → đường truyền 50 MB/s, độ trễ 0,02 giây → máy nhận.
- **Kết nối vào–ra:** Từ lượng dữ liệu sang thời gian; chuẩn bị xét giới hạn khi đường truyền dùng chung.
- **Kiểm tra và ghi chú:** Một thông điệp truyền riêng, $B$ ổn định, không tranh chấp; 1 MB bằng $10^6$ byte. Notes phân biệt MB/Mb và giới hạn dự đoán.
- **Nguồn:** Cornell CS5220, Intro to Message Passing, mô hình alpha–beta; đổi ký hiệu theo bài.
- **Thời lượng:** 2,5 phút

### `lec02-s04-07` — Băng thông dùng chung

- **Mục đích / sản phẩm:** Tính cận dưới thời gian khi nhiều máy cùng dùng một đường nối.
- **Câu chốt:** 400 MB qua đường nối 100 MB/s cần ít nhất 4 giây.
- **Vai trò:** Mở rộng mô hình sang tài nguyên dùng chung
- **Kiến thức đầu vào:** Rack đã học; $V/B$ của slide trước.
- **Cách thể hiện:** SVG cost-07: bốn máy gửi 100 MB mỗi máy qua cùng một đường nối giữa hai rack; $T\geq400/100=4$ giây.
- **Kết nối vào–ra:** Từ một truyền riêng tới tranh chấp đường nối; dẫn tới giảm lượng truyền bằng xử lý tại máy.
- **Kiểm tra và ghi chú:** Cận dưới do băng thông, chưa tính độ trễ. Không cấp riêng 100 MB/s cho từng máy. Tính cục bộ có thể giảm byte qua đường nối.
- **Nguồn:** MMDS 2.1.1, trang 22–23; cấu hình và phép tính minh họa.
- **Thời lượng:** 2 phút

### `lec02-s04-08` — Combine giảm lượng truyền

- **Mục đích / sản phẩm:** Đếm số cặp trung gian và quy đổi thành byte trước/sau Combine.
- **Câu chốt:** Năm cặp thành bốn cặp: 80 byte thành 64 byte; chưa đủ suy ra thời gian giảm 20%.
- **Vai trò:** So sánh hai cách tổ chức
- **Kiến thức đầu vào:** Combine của đếm từ; $C=I+H$ và $V$.
- **Cách thể hiện:** Bảng hai phương án dùng lại $d_1$: mèo chó mèo, $d_2$: chó chim; giữ ranh giới văn bản, số cặp tổng và phép nhân 16 byte/cặp.
- **Kết nối vào–ra:** Sau nút thắt đường truyền, chỉ ra một cách giảm byte; chuẩn bị đánh giá cả thời gian xử lý thêm.
- **Kiểm tra và ghi chú:** Mỗi văn bản một Map, cặp cố định 16 byte, qua đường xét một lần, không tính phần đầu gói. Notes: Combine thêm xử lý; $I$ giữ nguyên, $H$ giảm nên $C$ giảm.
- **Nguồn:** MMDS 2.2.4 trang 27–28, 2.5.1 trang 54; dữ kiện cũ và kích thước giả định.
- **Thời lượng:** 2,5 phút

### `lec02-s04-09` — Thời gian của cả công việc

- **Mục đích / sản phẩm:** Ghép đúng thời gian các pha trong mô hình nối tiếp.
- **Câu chốt:** $T_P=T_{\mathrm{điều\ phối}}+T_{\mathrm{Map}}+T_{\mathrm{truyền\ và\ nhóm}}+T_{\mathrm{Reduce}}=10$ giây.
- **Vai trò:** Tổng hợp mô hình
- **Kiến thức đầu vào:** Thời gian một pha và truyền dữ liệu.
- **Cách thể hiện:** SVG cost-09: 1 giây điều phối, 4 giây Map, 3 giây truyền và nhóm, 2 giây Reduce; trục 0/1/5/8/10, thang 100 px/giây. Công thức và thay số trên hai dòng.
- **Kết nối vào–ra:** Từ từng thành phần tới toàn công việc trên $P=4$ máy; đưa $T_4=10$ sang slide tăng tốc.
- **Kiểm tra và ghi chú:** Các pha không chồng lấp, không lỗi; đọc/ghi đã nằm trong các pha. Notes chỉ rõ nơi tính từng loại để không đếm lặp; 3 giây đã gồm truyền và nhóm.
- **Nguồn:** Mô hình đơn giản hóa từ MMDS 2.2.2 và 2.5.2; thời gian giả định.
- **Thời lượng:** 2,5 phút

### `lec02-s04-10` — Mức tăng tốc

- **Mục đích / sản phẩm:** Tính và diễn giải mức tăng tốc trên cùng bài toán.
- **Câu chốt:** $S_P=T_1/T_P$; $S_4=24/10=2{,}4$ lần.
- **Vai trò:** So sánh lợi ích
- **Kiến thức đầu vào:** $T_4=10$ giây từ lịch trước; thêm dữ kiện tuần tự 24 giây.
- **Cách thể hiện:** SVG cost-10: hai thanh cùng thang 38 px/giây, dài 24 và 10; công thức tỷ số dưới hình.
- **Kết nối vào–ra:** Từ runtime tổng sang quyết định có lợi; cung cấp công thức cho câu hỏi kiểm tra.
- **Kiểm tra và ghi chú:** Cùng dữ liệu, kết quả và phạm vi đo, $T_P>0$. Có lợi về thời gian khi $T_P<T_1$; notes giải thích chi phí truyền/gộp và lệch tải; bỏ hiệu suất vì chưa cần trong mạch này.
- **Nguồn:** Cornell CS5220, Performance basics; số giây giả định.
- **Thời lượng:** 2,5 phút

### `lec02-s04-11` — Câu hỏi kiểm tra

- **Mục đích / sản phẩm:** Vận dụng cả lịch chạy, lượng truyền, runtime và mức tăng tốc.
- **Câu chốt:** Tính lợi ích ròng: Combine bớt 2 giây truyền nhưng thêm 1 giây xử lý, tiết kiệm 1 giây.
- **Vai trò:** Kiểm tra vận dụng
- **Kiến thức đầu vào:** Các mô hình của phần này.
- **Cách thể hiện:** Bảng dữ kiện trái, ba nhiệm vụ phải: tải Map 2/3/5 giây, 120 MB qua 40 MB/s, điều phối 1 giây, Reduce 2 giây, tuần tự 22 giây; phương án Combine còn 40 MB và pha Map tăng 1 giây.
- **Kết nối vào–ra:** Thu hồi toàn bộ phần; kết quả giúp đánh giá một cách phân chia và giao tác vụ.
- **Kiểm tra và ghi chú:** Các pha nối tiếp; bỏ độ trễ/chi phí nhóm, đọc ghi đã trong Map/Reduce. Notes có lời giải: $T_{\mathrm{Map}}=5$, $T_{\mathrm{truyền}}=3$, $T_P=11$, $S_P=2$; sau Combine $T^{\prime}_P=10$, $S^{\prime}_P=2{,}2$.
- **Nguồn:** Dữ kiện giả định vận dụng mô hình đã nêu, theo yêu cầu kiểm tra tại lớp.
- **Thời lượng:** 3 phút

## Rà lại cách dẫn dắt phần chi phí theo góp ý giảng viên

Phạm vi: sửa các trang `lec02-s04-05` đến `lec02-s04-11`; giữ số trang, thứ tự, ví dụ và nguồn. Không mở rộng phần hệ thống hay bài tập recitation trong lượt sửa này.

| Trang | Câu hỏi học tập được giải quyết | Vai trò của đại lượng và kết nối |
|---|---|---|
| 05 | Các tác vụ phải đọc tổng cộng bao nhiêu dữ liệu? | Định nghĩa I, H trước C; C so sánh tổng đầu vào, gồm đọc cục bộ. Chưa đưa V vào đây. |
| 06 | Chuyển dữ liệu giữa máy mất bao lâu? | Giới thiệu V trên đường truyền, B byte/giây và độ trễ khởi đầu; thay số vào mô hình một thông điệp. |
| 07 | Nhiều máy gửi đồng thời có làm đường nối nhanh hơn? | B dùng chung; tổng V phải qua đường nối tạo thời gian tối thiểu. Dẫn tới giảm byte truyền. |
| 08 | Combine giảm phần chi phí nào? | Giảm số cặp gửi nhưng thêm xử lý cục bộ; phải đo thời gian toàn công việc mới biết lợi ích ròng. |
| 09 | Người dùng phải chờ bao lâu để có đủ kết quả? | TP cộng thời gian các pha nối tiếp; mỗi pha dùng thời gian hoàn tất, không cộng công việc các máy. |
| 10 | Dùng nhiều máy giúp nhanh hơn bao nhiêu lần? | T1 và TP cùng phạm vi; SP là tỷ số, giải thích 2,4 lần và điều kiện lợi về thời gian. |
| 11 | Có nên dùng Combine trong cấu hình đã cho? | Tính thời gian trước/sau từ dữ kiện, cân đối thời gian truyền giảm và thời gian Map tăng. |

Cách thể hiện: câu dẫn nêu nhu cầu đo, ký hiệu được giải nghĩa trước công thức, hình/bảng giữ vai trò trung tâm, câu cuối diễn giải kết quả cụ thể. Ghi chú diễn giả mở rộng giả thiết và câu nối. Giữ các ngoại lệ phạm vi và thời lượng của bản đang xây dựng từng phần.

## Thống nhất nhãn pha trong ví dụ cộng và làm rõ dữ kiện thời gian

- `lec02-s04-04`: gọi cộng cục bộ là Map và gộp bốn tổng là Reduce. Mỗi pha mất $3\tau$, nên $T_4=T_{\mathrm{Map}}+T_{\mathrm{Reduce}}=3\tau+3\tau=6\tau$. Giữ phép cộng tuần tự tại mỗi tác vụ và tổng khởi tạo bằng phần tử đầu; không đổi sang cây cộng. Nhãn hình khớp công thức. Công thức tổng quát giữ trong ghi chú để mặt slide tập trung vào ví dụ.
- `lec02-s04-09`: ghi trên mặt slide rằng thời gian 1/4/3/2 giây là dữ kiện cho trước của ví dụ giả định trên bốn máy. Không suy ra những số này từ ví dụ cộng 16 số; không phải số đo thực nghiệm. Mục đích là tập ghép thời gian các pha; bài tập phải cung cấp thời gian pha hoặc dữ kiện để tính chúng.
- Giữ thứ tự, số trang, các giả thiết và nguồn của phần chi phí. Hai trang dùng cùng ký hiệu pha nhưng hai bộ dữ kiện riêng.
