# Dàn ý Bài 02: Mô hình tính toán Map-Reduce

## 1. Giới thiệu bài học

- Slide 1: tiêu đề bài, tên môn học và học kỳ theo yêu cầu người dùng.

- Slide 2: Nội dung gồm “Giới thiệu”, “Mô hình tính toán Map-Reduce”, “Các ví dụ Map-Reduce” và “Chi phí và lợi ích của song song hóa”. Khi thêm section mới, bổ sung mục tương ứng vào slide này.

- Slide 3: Bối cảnh Google, các máy phổ thông và ba bài toán có quy mô lịch sử: chỉ mục hơn 8 tỷ trang (2004), mẫu nhật ký truy vấn nén 450 GB (2005), kho 24 triệu trang với hơn 259 triệu liên kết (1998).
- Slide 4: Dữ liệu phân tán, song song hóa, tính toán gần dữ liệu, điều phối/chống lỗi/phục hồi trong suốt.

- Slide 5: Cộng n số tại các máy rồi gộp; khái quát bằng toán tử giao hoán và kết hợp.

- Slide 6: Mạng các rack và HDFS; tính toán gần khối dữ liệu, nhân bản qua rack để chịu lỗi.

## 2. Mô hình tính toán Map-Reduce

- Khả năng của mô hình: xử lý dữ liệu phân tán, song song hóa, tính toán gần dữ liệu, điều phối và phục hồi tự động. Chưa mô tả cách làm theo yêu cầu người dùng.
- Ví dụ xuyên suốt: đếm tần suất xuất hiện từ trong n văn bản. Bước đầu đặc tả đầu vào, đầu ra, số đếm và khó khăn khi dữ liệu lớn.
- Hai hàm cho ví dụ đếm từ: Map phát (từ,1), hệ thống nhóm, Reduce cộng số đếm.
- Hệ thống phân chia/giao tác vụ và chuyển dữ liệu theo từ; phân biệt tác vụ với máy.
- Chạy tay hai văn bản “mèo chó mèo” và “chó chim” qua Map, nhóm, Reduce.
- Hình thức hóa chữ ký Map và Reduce, đối chiếu ví dụ đếm từ.
- Quy tắc nhóm/phân phối khóa; các pha logic của một công việc.
- Giả mã mô hình tổng quát, giữ phần tử lặp, phân biệt tác vụ logic và lượt thực thi.


## Động lực và yêu cầu mô hình

Duyệt một slide động lực trong section Giới thiệu, sau Nội dung. Giữ ba bài toán của Google từ bài báo2004, hình máy phổ thông và phần dữ liệu. Theo câu hỏi tiếp theo của người dùng, câu chốt phải làm rõ tính chất chung: xử lý tương tự trên từng phần/bản ghi, rồi gộp kết quả cục bộ. Không đưa chữ ký Map/Reduce, khóa hoặc cơ chế chuyển dữ liệu lên mặt slide này. Notes giải thích ba ví dụ và nhu cầu phối hợp máy; đây là động lực mô hình lập trình, không tuyên bố mọi bài toán dữ liệu lớn đều phù hợp. Hình ba máy minh họa, không số đo Google. Không thêm section mới, mục lục vẫn chỉ Giới thiệu. Không phục hồi deck/ghi chú đã xóa; không commit/push.

Theo các chỉ dẫn tiếp theo của người dùng, tách phần dẫn dắt thành slide 3 về Google và slide 4 về bốn yêu cầu: dữ liệu trên nhiều máy; tính toán song song; tính toán gần dữ liệu; phân chia, lập lịch, chống lỗi và phục hồi trong suốt đối với lập trình viên. Người dùng chỉ đạo từng slide nên chưa lập lại cả bài hoặc tài liệu tự học.

## Bổ sung Combine theo yêu cầu

Thêm sau đặc tả mô hình cơ bản: gộp cục bộ bằng Combine, dùng lại ví dụ đếm từ, giảm 5 xuống 4 cặp truyền. Nguồn MMDS 2.2.4, trang 27–28. Giữ khóa và kiểu trung gian; phép gộp kết hợp, giao hoán và tương thích với Reduce. Đây là điều kiện đủ cho cách gộp trình bày, không phải đặc tính bắt buộc của mọi Reduce. Một slide cùng section 2; không thêm mục lục.

## Chốt cấu trúc tiếp theo theo yêu cầu giảng viên

- Kết section 2 “Mô hình tính toán Map-Reduce” bằng slide “Câu hỏi kiểm tra” (`lec02-s02-12`); chỉ kiểm tra kiến thức vừa học.
- Sau section ví dụ, section chính dự kiến: **Hệ thống Map-Reduce**. Dự kiến mạch: chia đầu vào và giao tác vụ → hàm phân phối khóa → chuyển và nhóm dữ liệu → theo dõi tác vụ → phát hiện lỗi và phục hồi Map/Reduce → phân biệt chạy lại và thực thi dự phòng. Làm rõ dữ liệu nào được lưu bền vững, dữ liệu trung gian nào cần tạo lại; nguồn MMDS 2.2.2, 2.2.5 và Dean–Ghemawat 3.1–3.6.
- Section chính riêng: **Chi phí và lợi ích của song song hóa**. Dự kiến mạch: quy ước mô hình chi phí → tổng công việc và thời gian hoàn thành → ví dụ tính tuần tự/song song với giả thiết rõ → chi phí truyền dữ liệu và Combine → giới hạn do lệch tải, tác vụ chậm và chi phí điều phối. Đối chiếu MMDS 2.5–2.6 trước khi soạn chi tiết.
- Theo yêu cầu tiếp theo của giảng viên, triển khai Chi phí ngay sau Các ví dụ; Hệ thống vẫn ở mức kế hoạch. Những cơ chế đã có ở section 2 đủ làm tiên quyết; các giả thiết về lịch chạy và đường truyền được nêu tại từng slide chi phí. Chưa dựng slide trống hoặc thêm Hệ thống vào mục lục.

## 3. Các ví dụ Map-Reduce

Theo yêu cầu mới, triển khai section ví dụ trước hai section Hệ thống và Chi phí đã dự kiến. Section có một slide mở, mỗi bài năm slide cốt lõi và một slide ứng dụng, cùng một slide Câu hỏi kiểm tra cuối: tổng 20 slide sau khi thêm một slide ứng dụng cho mỗi bài.

| Cụm | Slide | Đặc tả và nguồn | Vai trò |
|---|---|---|---|
| Mở phần | lec02-s03-01 | Chọn khóa và giá trị từ mô hình ở section 2 | Cầu nối |
| Nhân ma trận–véc tơ | lec02-s03-02 đến 06 | MMDS 2.3.1 tr.31–32; 2.2.4 tr.27–28 | Cốt lõi |
| Số từ phân biệt | lec02-s03-07 đến 11 | MMDS bài 2.3.1(d), tr.40, đổi số nguyên thành từ theo yêu cầu; cơ chế nhóm và loại trùng | Cốt lõi |
| Trung bình cộng | lec02-s03-12 đến 16 | MMDS bài 2.3.1(b), tr.40; mở miền số nguyên sang số thực với giả thiết số học chính xác | Cốt lõi |
| Câu hỏi kiểm tra | lec02-s03-17 | Dùng lại ba ví dụ và các giả thiết đã xây | Kiểm tra |

Mỗi cụm: bài toán hình thức → ứng dụng → đặc điểm/ý tưởng → đặc tả Map, Reduce, Combine → ví dụ → chứng minh. Thứ tự này là chỉ dẫn cụ thể của người dùng, ưu tiên hơn chu trình mặc định ưu tiên ví dụ trước hình thức. Chi phí chi tiết sẽ ở section riêng.

Quyết định nguồn: dùng sách MMDS cho thuật toán ma trận và đề bài trung bình/đếm phân biệt; slide MMDS và Stanford xác nhận cơ chế Combine nhưng không cung cấp đủ cả ba cụm theo khuôn yêu cầu. Các lời giải và ví dụ chạy tay được diễn giải từ nguồn và tự kiểm, không gán số liệu minh họa cho sách. Không đưa đại số quan hệ/CSDL vào bài.

Ký hiệu: $p$ là số hàng, $q$ là số cột của ma trận, $A=(a_{ij})$, $v$ đầu vào, $y=Av$ đầu ra; $n$ là số văn bản hoặc số phần tử theo từng bài; $W_i$ tập từ văn bản $d_i$; $D$ số từ phân biệt; $g$ khóa chung cố định; $(s,c)$ là tổng và số lượng; $L$ danh sách giá trị cùng khóa; $\mu$ là trung bình.

Giả thiết: ma trận có đủ bản ghi tọa độ kể cả 0, mỗi tọa độ một lần; $v$ vừa RAM mỗi tác vụ Map. Trung bình có $n\geq1$, số học chính xác trong chứng minh. Đếm phân biệt dùng hai công việc, chương trình điều phối trả 0 khi không có từ. Combine đếm phân biệt ở công việc 1 giữ sự hiện diện, không cộng tần suất; công việc 2 cộng các số 1. Đây là một thiết kế, không khẳng định hai công việc là cận dưới.

Hình: sơ đồ chọn khóa, hai công việc loại trùng–đếm, trạng thái tổng–số lượng; slide đặc điểm có icon SVG kèm nhãn. Bảng chạy tay và công thức dựng bằng HTML/KaTeX. Chứng minh ưu tiên các bước suy luận, không ép thêm hình.

Lưu trữ ma trận: các bản ghi tọa độ được chia thành khối và nhân bản trên nhiều máy; phân biệt dữ liệu logic với bản sao vật lý. Hình dùng ba khối, hai bản sao mỗi khối chỉ để minh họa. Nguồn MMDS 2.1.2 và 2.3.1.

Trong ví dụ ma trận, Map nhận một khối B và duyệt các bản ghi (i,j,a_ij), yield(i,a_ij*v[j]); Combine và Reduce cũng dùng yield. Đây là điều chỉnh giao diện theo người dùng so với Map nhận một phần tử trong MMDS; tập cặp trung gian không đổi.

## Ứng dụng của ba ví dụ

Theo yêu cầu, đặt một slide ứng dụng ngay sau phát biểu bài toán của từng bài:
- lec02-s03-06a: chấm điểm tương đồng các trang web với một truy vấn. A có p hàng trang web và q cột từ; v là véc tơ truy vấn cùng trục. Chuẩn hóa mỗi hàng A và v về độ dài Euclid1 để y=Av cho điểm cosine; bước chọn trang điểm cao tách khỏi phép nhân.
- lec02-s03-11a: số từ phân biệt cho kích thước từ vựng, bằng số cột khi dùng nguyên bộ từ.
- lec02-s03-16a: dùng số lần xuất hiện từ của từng trang làm dãy đầu vào để tính số từ trung bình mỗi trang; trang rỗng vẫn góp vào số trang.

Nguồn bổ sung theo yêu cầu ứng dụng: Manning, Raghavan, Schütze, Introduction to Information Retrieval, 6.3.1–6.3.2, [tích vô hướng](https://nlp.stanford.edu/IR-book/html/htmledition/dot-products-1.html) và [truy vấn như véc tơ](https://nlp.stanford.edu/IR-book/html/htmledition/queries-as-vectors-1.html). Điều phối đã đọc và duyệt trước khi soạn; không thêm học phần TF-IDF hoặc chỉ mục tìm kiếm vào phạm vi.

Ví dụ nhân ma trận đổi thành A4×4 chia bốn khối2×2 B11/B12/B21/B22, v=[1,2,3,4], y=[9,8,9,11]. Mỗi hàng trải trên hai khối; Combine tạo tổng bộ phận và Reduce cộng hai tổng. Đặc tả tổng quát vẫn p×q.


## 4. Chi phí và lợi ích của song song hóa

Phần mới theo yêu cầu giảng viên: mô hình chi phí tính toán, mô hình thời gian thực hiện và mô hình băng thông; dùng hình để đọc đại lượng trước khi thay số. Từ ba thuật toán ở section 3, chuyển sang đánh giá hiệu quả một cách tổ chức tác vụ. Dùng lại cộng dãy số ở phần giới thiệu và đếm từ ở section 2; không thêm thuật toán hoặc kiến thức CSDL.

| Slide | Sản phẩm học tập | Trọng tâm |
|---|---|---|
| lec02-s04-01 | Phân biệt công việc, thời gian và lượng truyền | Ba đại lượng $W$, $T_P$, $V$ cùng đơn vị |
| lec02-s04-02 | Đếm số phép cộng của toàn bộ các máy | $W_P=P(n/P-1)+(P-1)=n-1$ |
| lec02-s04-03 | Tính thời gian một pha từ lịch giao tác vụ | Lấy tải lớn nhất trong các máy, không lấy tác vụ dài nhất |
| lec02-s04-04 | So sánh thời gian tuần tự và song song | Cộng 16 số: $15\tau$ và $6\tau$; một máy gộp tuần tự |
| lec02-s04-05 | Tính chi phí theo quy ước sách MMDS | $C=I+H$, tổng kích thước đầu vào tác vụ |
| lec02-s04-06 | Đổi lượng truyền sang thời gian | $T_{\text{truyền}}\approx\lambda+V/B$ cho một thông điệp cô lập |
| lec02-s04-07 | Xác định giới hạn của đường nối dùng chung | $T\geq V/B$, 400 MB qua đường nối 100 MB/s cần ít nhất 4 giây |
| lec02-s04-08 | Tính tác động của Combine lên lượng truyền | Năm cặp thành bốn cặp: 80 byte thành 64 byte với mã hóa giả định |
| lec02-s04-09 | Ghép thời gian các pha không chồng lấp | Điều phối + Map + truyền và nhóm + Reduce |
| lec02-s04-10 | Tính mức tăng tốc trên cùng bài toán | $S_P=T_1/T_P$; $24/10=2{,}4$ |
| lec02-s04-11 | Vận dụng mô hình và đánh giá Combine | Lịch tải, lượng truyền, runtime, mức tăng tốc |

Nguồn chính: `sources/textbooks/ch2n.pdf`, mục 2.5.1–2.5.2, trang 53–56; Combine mục 2.2.4, trang 27–28; cấu trúc rack mục 2.1.1, trang 22–23. Đối chiếu `sources/reference-slides/mmds/ch02-mapreduce.pdf`, slide 38–40 và Stanford CS246 `01-intro.pdf`, slide 67–70. Hai bộ slide tương đương cho phân biệt tổng chi phí và thời gian; sách làm chuẩn cho quy tắc đếm đầu vào. Slide nguồn đếm tổng I/O, có $I+2H+O$; bài này không dùng quy ước đó cho $C$ và không coi $C$ là byte qua mạng thực tế.

Nguồn bổ sung được điều phối đọc và duyệt: Cornell CS5220, [Intro to Message Passing, mô hình độ trễ–băng thông](https://www.cs.cornell.edu/courses/cs5220/2020fa/lec/2020-10-06-intro.html) và [Performance basics, mức tăng tốc](https://www.cs.cornell.edu/courses/cs5220/2020fa/lec/2020-09-08-perf-basics.html). Chỉ dùng công thức cơ bản đáp ứng yêu cầu giảng viên, không mở sang MPI, LogP hoặc định luật Amdahl.

Ký hiệu trong phần này: $P$ số máy (phân biệt $p$ số hàng ma trận); $n$ số phần tử của dãy; $\tau$ thời gian một phép cộng; $t_m$ tổng thời gian các tác vụ giao máy $m$; $C$ tổng kích thước đầu vào tác vụ; $I$ tổng đầu vào Map; $H$ tổng đầu vào Reduce; $V$ byte đi qua đường truyền đang xét; $B$ băng thông hữu dụng; $\lambda$ độ trễ khởi đầu (không dùng $L$ đã chỉ danh sách Reduce); $S_P$ mức tăng tốc. Các ký hiệu được định nghĩa lại tại slide sử dụng.

Giả thiết áp dụng riêng cho từng mô hình: phép cộng đơn vị, số học chính xác, chia đều với $n\geq P\geq1$ và $n$ chia hết cho $P$; một máy gộp tuần tự; mỗi máy chạy một tác vụ tại một thời điểm, mọi tác vụ của pha sẵn sàng ở đầu pha, không có thời gian nghỉ giữa tác vụ trên máy; các pha nối tiếp, không lỗi/chạy lại. Giả thiết băng thông ổn định chỉ dùng cho đường truyền được chỉ rõ. Phân biệt giá trị trong mô hình với cận dưới do dung lượng đường nối.

Các con số 16 phần tử, kích thước byte, băng thông và số giây là dữ kiện minh họa để tính mô hình, không phải số đo hệ thống hay bài tập nguyên văn từ sách. Kiểm tra cuối phần là tương tác tại lớp theo yêu cầu, không thay phần recitation 60 phút. Phần mới dự kiến 27,5 phút; toàn bài tiếp tục được xây từng section nên chưa tuyên bố đủ 120+60 phút hoặc hoàn tất 5–7 mạch. Tách 11 slide thay vì 9 đề xuất ban đầu để quy ước $C$ và mức tăng tốc có slide riêng.

### Điều chỉnh cách trình bày chi phí

Giữ mạch và 11 trang của phần 4. Từ trang 05, lần lượt xây: tổng đầu vào tác vụ C (I + H) → lượng qua một đường truyền V và thời gian theo băng thông → giới hạn đường nối dùng chung → Combine giảm byte nhưng thêm xử lý → thời gian toàn công việc TP → mức tăng tốc SP → bài kiểm tra lợi ích ròng. Chỉ giới thiệu V ở trang băng thông; không dùng tên nguồn thay cho lời giải thích quy ước trên mặt slide. Các ký hiệu đều có ý nghĩa và đơn vị tại nơi dùng. Không thêm mô hình hiệu suất sử dụng máy trong lượt này.
