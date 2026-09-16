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
- **Hiện trạng:** Hai mục “Giới thiệu” và “Mô hình tính toán Map-Reduce”.
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
