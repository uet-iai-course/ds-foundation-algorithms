# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

Một kho nhật ký web lưu địa chỉ trang, kích thước và ngày thu thập. Cần tính tổng byte theo từng máy chủ, nhưng kho không vừa bộ nhớ chính. Phép tính chỉ là cộng; khó khăn nằm ở cách đọc dữ liệu và trạng thái phải giữ.

Kho web còn phục vụ xếp hạng, tìm tài liệu gần trùng và truy hồi theo véc-tơ. Dòng truy vấn cần được lấy mẫu hoặc thống kê ngay khi đến. Dữ liệu đã lưu cần nén, sắp xếp và lập chỉ mục. Các ứng dụng dưới đây lấy từ Bài 02–15; mỗi ứng dụng xác định một đầu ra và một giới hạn cần giải thuật xử lý. Sau đó, ta phân tích trọn thuật toán tổng byte, dùng các tiêu chí ấy để đọc chương trình học và chuẩn bị kiến thức.

[Bộ trang chiếu Bài 01](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html) dùng cùng dữ kiện và ký hiệu. Ghi chú giải thích thêm đặc tả, chứng minh, điều kiện chi phí và lời giải bài tập.

## Tổng hợp và tìm kiếm trên kho web

### Tổng kích thước theo máy chủ

Đầu vào là các bản ghi về trang web; đầu ra là tổng kích thước của những trang thuộc mỗi máy chủ. Gọi $D$ là số byte đầu vào và $M$ là dung lượng bộ nhớ chính khả dụng, cũng tính bằng byte. Khi $D>M$, cách tải cả kho vào bộ nhớ không đáp ứng giới hạn.

Có thể đọc tuần tự và chỉ giữ tổng đang chạy theo máy chủ. Tuy nhiên, số máy chủ phân biệt cũng quyết định dung lượng của bảng tổng; đầu vào không vừa bộ nhớ không có nghĩa bảng tổng chắc chắn vừa. Stanford CS246 nêu tình huống này ở trang chiếu 62 của bài mở đầu; MMDS mục 1.3.3, trang 13 và BHK trang PDF 10 cung cấp bối cảnh truy cập ngoài bộ nhớ.

![Kho nhật ký đi qua một lượt quét; bộ nhớ chỉ giữ bảng tổng theo máy chủ, sau đó xuất tổng byte của từng máy chủ](img/lec-01/kho-nhat-ky-bo-nho.svg)

Ví dụ này được phân tích đầy đủ ở phần thuật toán quét–cộng dồn. Các ứng dụng tiếp theo cho thấy ngoài bộ nhớ còn có những giới hạn khác.

### Tổng hợp kho tài liệu phân tán

Một kho tài liệu nằm trên nhiều máy. Với mỗi từ, cần tổng số lần xuất hiện trong toàn kho. Đầu ra là bảng từ–số lần, không phải bản sao của mọi tài liệu trên một máy.

Gom toàn bộ kho về một máy phải truyền cả dữ liệu và tập trung công việc vào máy đó. Một hướng xử lý là tính đóng góp tại nơi lưu dữ liệu rồi gom theo từ. Hình thể hiện luồng đóng góp, chưa phải vết chạy một chương trình cụ thể. Khi tác vụ lỗi được chạy lại, môi trường thực thi phải bảo đảm kết quả cuối không bỏ sót hoặc tính trùng đóng góp. Lượng dữ liệu trung gian, phân bố tải và khôi phục tác vụ đều cần được xét. Nguồn: MMDS mục 2.1–2.2.6; slide Chương 2, trang 8–12 và 20; Bài 02.

![Các phần kho ở ba máy tạo đóng góp theo từ, truyền qua mạng và gom thành tổng; tác vụ lỗi cần được chạy lại](img/lec-01/ung-dung-tong-hop-phan-tan.svg)

### Xếp hạng trang web

Đồ thị web có hướng: mỗi đỉnh là một trang, mỗi cạnh là một liên kết. Bài toán xếp hạng cần một điểm cho mỗi trang theo mô hình đã chọn. Đồ thị minh họa có ba đỉnh $y,a,m$: $y$ trỏ tới $y,a$; $a$ trỏ tới $y,m$; $m$ trỏ tới $a$. Hình giữ nguyên các cạnh của nguồn, không gán điểm xếp hạng mới.

![Đồ thị có ba đỉnh y, a, m; y có một khuyên, y và a liên kết hai chiều, a và m liên kết hai chiều](img/lec-01/ung-dung-xep-hang-web.svg)

Biểu diễn một ma trận đặc cho mọi cặp trang có thể lãng phí bộ nhớ khi đồ thị thưa. Phương pháp tính lặp còn phải trả chi phí đọc cạnh và cập nhật điểm qua nhiều vòng. Điều kiện hội tụ, tiêu chuẩn dừng và chi phí mỗi vòng là ba việc khác nhau cần phân tích ở Bài 03. Nguồn: MMDS mục 5.1.2 và 5.2; slide Link Analysis 1, trang 18–21, 48 và 53.

### Xếp hạng theo chủ đề

Truy vấn “jaguar” có thể chỉ loài báo, ô tô, hệ điều hành hoặc máy chơi trò chơi. Dữ liệu liên kết có thể như nhau nhưng đầu ra phù hợp còn phụ thuộc chủ đề truy vấn. Đặc tả vì thế phải nêu điểm hạng phục vụ mục tiêu nào; một điểm chung cho mỗi trang chưa phân biệt các nghĩa này.

![Truy vấn jaguar nối tới bốn cách hiểu: loài báo, ô tô, hệ điều hành và máy chơi trò chơi](img/lec-01/ung-dung-truy-van-theo-chu-de.svg)

Bài 04 xem cách đưa chủ đề vào xếp hạng. Điều này không tạo ra bảo đảm rằng thuật toán biết đúng ý định của từng người dùng. Nguồn: MMDS mục 5.3.1, trang 195–196.

### Liên kết bị thao túng

Nếu một nhóm trang được tạo để hỗ trợ trang đích, liên kết không còn mang cùng ý nghĩa như trong giả thiết xếp hạng ban đầu. Hình phân biệt trang ngoài tầm tác động, trang có thể tác động và trang sở hữu. Các trang có thể tác động trỏ đến đích $t$; $t$ trỏ đến từng trang hỗ trợ, và mỗi trang hỗ trợ trỏ lại $t$.

![Cụm liên kết theo Hình 5.16: liên kết ngoài đi vào t; t và các trang hỗ trợ sở hữu liên kết qua lại](img/lec-01/ung-dung-lien-ket-thao-tung.svg)

Yêu cầu ở đây là đánh giá độ tin cậy của tín hiệu và giới hạn diễn giải điểm hạng. Sơ đồ không chứng minh ý định hoặc danh tính của một người. Nguồn: MMDS mục 5.4, Hình 5.16; Bài 04.

### Tìm tài liệu gần trùng

Đầu vào là một tập tài liệu; đầu ra là các cặp có độ tương đồng vượt mức đã chốt. Trước khi tối ưu, cần xác định biểu diễn và độ đo: “gần trùng” trên tập đoạn ký tự là một đặc tả cụ thể, khác với đánh giá hai tài liệu nói về cùng một chủ đề.

Với $N$ tài liệu, số cặp không thứ tự là $\binom N2=N(N-1)/2$. Khi $N=10^6$:

$$
\binom{10^6}{2}=499\,999\,500\,000\approx5\times10^{11}.
$$

Đây là phép đếm, không phải kết quả đo thời gian. Biểu diễn gọn giúp giảm chi phí mỗi lần so sánh; chọn ứng viên giúp giảm số cặp phải đối chiếu. Hai tác dụng này khác nhau.

![Tập đoạn ký tự tạo chữ ký gọn; chữ ký tạo cặp ứng viên; ứng viên được đối chiếu trên dữ liệu gốc](img/lec-01/ung-dung-tai-lieu-gan-trung.svg)

Đối chiếu dữ liệu gốc có thể loại ứng viên không đủ tương đồng, nhưng không khôi phục cặp đã bị bước chọn ứng viên bỏ sót. Bài 05–06 phân tích các xác suất liên quan. Nguồn: MMDS mục 3.1–3.4; slide Chương 3, trang 15–16 và 24; Stanford CS246 03-lsh, trang 14.

### Truy hồi theo véc-tơ

Kho dữ liệu được biểu diễn bằng các véc-tơ cùng số chiều. Cho một véc-tơ truy vấn và một độ đo khoảng cách đã chọn, cần trả các mục gần truy vấn. Nếu yêu cầu $k$ hàng xóm, lời giải chính xác trả $k$ mục gần nhất theo quy ước xử lý hòa đã chốt. Lời giải gần đúng được đánh giá bằng chất lượng truy hồi và tài nguyên sử dụng.

Độ thu hồi tại $k$ là tỷ lệ hàng xóm gần thật xuất hiện trong $k$ kết quả trả về, khi tập chuẩn và quy ước hòa đã cố định. Bên cạnh độ thu hồi, cần đo độ trễ truy vấn, bộ nhớ và chi phí xây chỉ mục. Quét toàn bộ kho cho mỗi truy vấn tránh xây cấu trúc phức tạp nhưng phải tính khoảng cách tới mọi véc-tơ.

![Véc-tơ truy vấn qua chỉ mục để lấy các mục gần; bốn tiêu chí là độ thu hồi, độ trễ, bộ nhớ và xây dựng](img/lec-01/ung-dung-truy-hoi-vec-to.svg)

BIODS 271, trang PDF 17–18 dùng tình huống 10 tỷ véc-tơ, 3072 chiều, mỗi thành phần 32 bit để làm rõ nhu cầu quy mô. Hình ở đây chỉ mô tả luồng truy hồi, không dùng hình hai chiều làm bằng chứng cho không gian 3072 chiều. Bài 07 học các chỉ mục và mã gọn; nguồn bổ sung là Princeton lớp 8, trang 2–5.

Tự kiểm tra: tìm mọi cặp gần trùng và tìm $k$ mục gần một truy vấn khác nhau về đầu ra và số đối tượng phải xét như thế nào?

## Dòng dữ liệu, khôi phục và truy vấn

Kho tĩnh sinh truy vấn liên tục, còn dữ liệu lưu trữ phải được tổ chức để đọc lại. Các tình huống này bổ sung yêu cầu về cập nhật, thời gian phục vụ và khôi phục.

### Lấy mẫu và lọc dòng truy vấn

Dữ liệu đến theo thứ tự, có thể chưa biết độ dài cuối cùng. Một nhiệm vụ là giữ một mẫu phục vụ phân tích; nhiệm vụ khác là kiểm tra nhanh trước một phép tra cứu đắt. Cả hai đều dùng trạng thái nhỏ, nhưng đầu ra và điều kiện đúng khác nhau.

![Dòng truy vấn có hai nhánh: giữ trạng thái mẫu để xuất mẫu; dùng bộ lọc để chuyển trường hợp có thể có tới tra cứu chính xác](img/lec-01/ung-dung-dong-truy-van.svg)

Mẫu phải có phân phối phù hợp với đơn vị lấy mẫu: bản ghi và khóa không luôn cho cùng ý nghĩa thống kê. Bộ lọc Bloom chuẩn với thao tác chỉ chèn có thể báo “có thể có” cho phần tử chưa chèn. Nếu băm nhất quán và trạng thái không bị xóa hoặc hỏng, nó không báo vắng cho phần tử đã chèn. Vì vậy, kết quả “có thể có” vẫn cần kiểm tra chính xác khi ứng dụng đòi đáp án chắc chắn. Nguồn: MMDS mục 4.1–4.3, trang 133–142; Streams 1, trang 6; Bài 08.

### Thống kê trên dòng và cửa sổ

Đầu ra có thể là số khóa khác nhau, tần suất một khóa, một mômen của phân phối tần suất hoặc số sự kiện trong cửa sổ gần đây. Với tần suất $f_j$ của khóa $j$, mômen thứ hai là $\sum_j f_j^2$; đại lượng này khác tổng số sự kiện $\sum_j f_j$.

![Một dòng phục vụ bốn loại thống kê; mốc cửa sổ tách phần gần đây khỏi quá khứ](img/lec-01/ung-dung-thong-ke-cua-so.svg)

Truy vấn toàn dòng giữ ảnh hưởng của quá khứ, còn truy vấn cửa sổ phải loại ảnh hưởng trước mốc. Từ đó, đại lượng cần ước lượng và phạm vi thời gian quyết định trạng thái. Các cấu trúc sẽ học có loại sai số khác nhau: một số dùng ngẫu nhiên, còn DGIM có cận xác định. Nguồn: MMDS mục 4.4–4.7, trang 142–159, Hình 4.2–4.4; UMass CS514 Lecture 10 cho Count-Min; Bài 09.

### Văn bản cần khôi phục nguyên vẹn

Với nén không mất thông tin, đầu ra của bộ giải mã phải bằng đúng đầu vào bộ mã hóa. Chuỗi `aabaacabcabcb` có các mẫu lặp; nguồn dùng nó để minh họa nén từ điển. Trong Bài 01, chỉ theo dõi yêu cầu khôi phục, chưa xây mã.

![Chuỗi aabaacabcabcb được mã hóa rồi giải mã thành đúng chuỗi ban đầu, không gán tỷ lệ nén](img/lec-01/ung-dung-nen-van-ban.svg)

Dung lượng phải tính cả dòng mã và thông tin phụ trợ cần giải mã, chẳng hạn mô hình hoặc từ điển. Bộ mã hóa và bộ giải mã phải dùng quy ước tương thích. Nguồn: Nelson–Gailly Chương 3 và 9; CMU LZ, trang logic 11–14; Bài 10–11.

### Ảnh cho phép khôi phục gần đúng

Với tuyến nén ảnh có lượng tử hóa, đặc tả khôi phục khác với văn bản: ảnh tái tạo có thể khác ảnh đầu vào. Phải chốt cách đo sai số hoặc chất lượng phù hợp ứng dụng trước khi so sánh phương pháp.

![Khối ảnh đi qua biến đổi, lượng tử hóa và mã hóa; sau giải mã và tái tạo, ảnh có thể khác đầu vào](img/lec-01/ung-dung-nen-anh.svg)

Hình đánh dấu lượng tử hóa là bước mất thông tin; không đồng nhất nó với phép biến đổi. Không có ảnh trước/sau hay số chất lượng thực nghiệm được tự thêm. Bài 11 học tuyến nén JPEG tương ứng. Nguồn: Nelson–Gailly Chương 11; CMU lossy, trang logic 2–16.

### Sắp xếp tệp vượt bộ nhớ

Đầu vào là tệp bản ghi lớn hơn bộ nhớ; đầu ra phải giữ cùng các bản ghi, kể cả bản ghi có khóa lặp, theo thứ tự khóa yêu cầu. Sắp như một mảng nằm trọn trong bộ nhớ không đáp ứng điều kiện.

![Tệp lớn được chia thành các dãy đã sắp, rồi đọc qua bộ đệm trộn để tạo tệp có thứ tự](img/lec-01/ung-dung-sap-xep-ngoai.svg)

Có thể tạo các dãy có thứ tự từ những phần vừa bộ nhớ, sau đó trộn qua bộ đệm. Số phép so sánh chưa mô tả đủ chi phí; cần tính các lượt đọc và ghi theo khối. Nguồn: Database System Concepts, ấn bản 7 (viết tắt DSC), Chương 15, trang chiếu 17–23; Bài 12.

### Tra khóa và khoảng giá trị

Truy vấn điểm tìm bản ghi có khóa bằng giá trị đã cho; truy vấn khoảng tìm bản ghi có khóa trong khoảng. Cần xác định cả quy ước biên của khoảng và cách trả các khóa lặp nếu có.

![Yêu cầu tra điểm hoặc khoảng đi qua chỉ mục để chọn khối cần đọc; cập nhật dữ liệu phải duy trì chỉ mục](img/lec-01/ung-dung-tra-cuu-khoa.svg)

Quét bảng mỗi lần có thể đọc nhiều khối không cần thiết. Chỉ mục giảm truy cập cho lớp truy vấn phù hợp nhưng có chi phí xây dựng, dung lượng và cập nhật. Cây có thứ tự và băm không có cùng khả năng phục vụ khoảng giá trị. Nguồn: DSC Chương 14, trang chiếu 3–16; Bài 13.

### Tìm tài liệu chứa từ khóa

Đầu vào là kho tài liệu và điều kiện từ khóa; đầu ra là tập mã tài liệu thỏa điều kiện. Hướng ánh xạ từ từ khóa đến danh sách tài liệu chứa từ tránh phải đọc toàn bộ kho cho mỗi yêu cầu.

![Từ khóa được tra trong từ điển để lấy danh sách mã tài liệu, sau đó kết hợp thành tập kết quả](img/lec-01/ung-dung-tim-tu-khoa.svg)

Điều kiện chứa đồng thời các từ dùng giao tập tài liệu; điều kiện chứa ít nhất một từ dùng hợp. Tìm tập tài liệu thỏa điều kiện và xếp hạng chúng là hai bước có đặc tả khác nhau. Nguồn: DSC Chương 31, trang 13–16 và trang chiếu 14–16; Bài 14.

### Tìm đối tượng trong một vùng

Đầu vào gồm các đối tượng không gian và vùng truy vấn $Q$; đầu ra ở đây là những đối tượng giao $Q$. Chỉ mục có thể dùng hộp bao để chọn ứng viên, rồi kiểm quan hệ hình học trên đối tượng thật.

![Vùng Q giao cả hai hộp bao A và B trong sơ đồ của Bài14; cần xét ứng viên từ cả hai nhánh rồi kiểm đối tượng thật](img/lec-01/ung-dung-truy-van-khong-gian.svg)

Hình giữ vị trí tương đối của hai hộp bao và $Q$ từ Bài 14. Đi theo chỉ một nhánh sẽ bỏ phần ứng viên cần xét. Ngược lại, hộp bao giao vùng không đủ để kết luận đối tượng thật giao vùng. Nguồn: DSC Chương 24, trang chiếu 17, 21–24; Auburn, trang PDF 10–13.

### Kết nối hai bảng theo mã sinh viên

Bảng `student` có 5000 bản ghi trong 100 khối; bảng `takes` có 10.000 bản ghi trong 400 khối. Đầu ra của phép nối theo `ID` gồm **mọi cặp** bản ghi có mã bằng nhau. Khi một mã xuất hiện nhiều lần, chỉ trả một cặp cho mã đó là sai.

![Hai bảng student và takes được đọc vào bộ nhớ hữu hạn để ghép theo ID và trả mọi cặp có ID bằng nhau](img/lec-01/ung-dung-noi-bang.svg)

Dùng ngân sách $M_{\rm khối}=20$ khối như kịch bản giảng dạy ở Bài 15. Số 20 không phải số đo hay hằng số của giáo trình; các quy mô hai bảng lấy từ DSC Chương 15, trang chiếu 28. Không bảng nào vừa ngân sách này. Lặp qua từng bản ghi của một bảng và quét lại bảng kia có thể đọc nhiều lần cùng dữ liệu; cần xét cách tái sử dụng khối, chỉ mục, thứ tự hoặc phân hoạch. Nguồn thêm: DSC Chương 15, trang chiếu 24 và 40.

Tự kiểm tra: trong các ứng dụng trên, yêu cầu nào cần khôi phục đúng dữ liệu, yêu cầu nào cần lọc ứng viên, và yêu cầu nào phải trả đủ cặp khóa lặp?

## Thuật toán quét–cộng dồn

Các tình huống vừa khảo sát chỉ định vị nhu cầu; thuật toán chuyên biệt thuộc các bài sau. Với tổng byte, ta có thể đi hết từ đặc tả đến chứng minh ngay trong Bài 01.

### Đặc tả và biểu diễn

Cho dãy $L=((u_i,s_i))_{i=1}^{n}$. Ở đây $n$ là số bản ghi hữu hạn, $u_i$ là tên máy chủ, $s_i\in\mathbb N_0$ là kích thước tính bằng byte.

- Đầu ra: bảng $S$ có đúng tập máy chủ xuất hiện trong $L$, với $S[u]=\sum_{i:u_i=u}s_i$.
- Điều kiện trước: bản ghi hợp lệ; kiểu dùng cho tổng không tràn.
- Điều kiện sau: đúng tập khóa và đúng giá trị tổng tại mỗi khóa.
- Ràng buộc lời giải đang xét: đọc tuần tự một lượt; chỉ giữ trạng thái cần thiết, không giữ toàn bộ dãy.

Giới hạn $D>M$ không tự bắt buộc mọi thuật toán chỉ được đọc một lượt; ở đây ta chọn và phân tích lời giải một lượt. Đặc tả bài toán không bắt buộc bảng băm: đó là một lựa chọn biểu diễn và cài đặt bảng $S$. Nguồn tình huống là Stanford CS246 trang chiếu 62; đặc tả và lập luận dưới đây được dựng cho ví dụ học phần.

### Ví dụ và trực giác trạng thái

::: example
Dùng bốn bản ghi đã có của học phần. Đây là dữ liệu chạy tay từ lược đồ nguồn, không phải dữ liệu thực nghiệm.

| Bước | Bản ghi (máy chủ, byte) | Trạng thái $S$ sau bước |
|---:|---|---|
| 0 | Chưa đọc | Bảng rỗng |
| 1 | (a.vn, 40) | a.vn: 40 |
| 2 | (b.vn, 25) | a.vn: 40; b.vn: 25 |
| 3 | (a.vn, 15) | a.vn: 55; b.vn: 25 |
| 4 | (c.vn, 0) | a.vn: 55; b.vn: 25; c.vn: 0 |

Sau bước 3, hai bản ghi của a.vn có tổng $40+15=55$. Sau bước 4, c.vn phải xuất hiện dù tổng bằng 0.
:::

Bảng tổng giữ đủ thông tin về tiền tố để xử lý phần còn lại: khi gặp một bản ghi của $u$, chỉ cần tổng cũ của $u$ và số byte mới. Các bản ghi trước có thể bỏ sau khi cộng. Đây là trực giác tóm tắt trạng thái; tính đúng được chứng minh bằng bất biến, không chỉ bằng một vết chạy.

### Mệnh đề và giả mã

Mệnh đề: với điều kiện trước đã nêu, thuật toán sau dừng và trả đúng bảng $S$ của đặc tả.

```text
S ← bảng rỗng
với i từ 1 đến n:
    (u, s) ← bản ghi tiếp theo
    nếu u chưa có trong S:
        S[u] ← 0
    S[u] ← S[u] + s
trả về S
```

Thuật toán chỉ cần phép kiểm khóa, khởi tạo, đọc và cập nhật giá trị. Mỗi vòng tiêu thụ thêm một bản ghi; số bản ghi chưa xử lý giảm từ $n$ xuống $0$, nên thuật toán dừng sau $n$ vòng.

### Chứng minh bằng bất biến tiền tố

::: proof
Sau $k$ bản ghi, với $0\le k\le n$, bất biến gồm hai vế:

1. Tập khóa của $S$ đúng bằng các máy chủ trong tiền tố dài $k$.
2. Với mỗi khóa $u$ trong bảng, $S[u]=\sum_{i\le k,\;u_i=u}s_i$.

**Khởi tạo.** Với $k=0$, tiền tố rỗng và bảng rỗng có cùng tập khóa. Không có khóa cần kiểm giá trị.

**Duy trì.** Giả sử bất biến đúng sau $k<n$ bản ghi. Bản ghi tiếp theo là $(u_{k+1},s_{k+1})$. Nếu khóa mới, thuật toán thêm khóa với 0 rồi cộng $s_{k+1}$; đó là toàn bộ tổng của khóa trong tiền tố mới. Nếu khóa đã có, tổng cũ đúng theo giả thiết quy nạp; cộng $s_{k+1}$ cho tổng đúng trên tiền tố dài hơn. Các khóa khác không đổi. Tập khóa chỉ thêm đúng khóa mới nếu cần. Giả thiết tổng không tràn bảo đảm phép cộng cài đặt vẫn là phép cộng trong đặc tả.

**Kết thúc.** Thuật toán dừng ở $k=n$. Vế thứ nhất cho đúng tập máy chủ trong toàn dãy; vế thứ hai cho đúng tổng của từng máy chủ. Hai vế chính là điều kiện sau, nên thuật toán đúng.
:::

### Trường hợp biên, chi phí và tính khả thi

Dãy rỗng trả bảng rỗng. Khóa lặp được cộng dồn. Bản ghi kích thước 0 vẫn tạo khóa; bỏ bước ấy sẽ làm sai tập khóa. Kích thước âm hoặc bản ghi hỏng nằm ngoài miền đầu vào đã chốt, không được ngầm bỏ qua.

Đặt $h$ là số máy chủ phân biệt, $D$ là số byte đầu vào, $M$ là số byte bộ nhớ khả dụng, $v$ là tốc độ đọc tính bằng byte/giây.

| Thành phần | Kết quả và điều kiện |
|---|---|
| Thời gian tính | $O(n)$ kỳ vọng nếu thao tác bảng băm có thời gian kỳ vọng $O(1)$ |
| Trạng thái | $O(h)$ mục trong bảng; không đồng nhất $h$ mục với $h$ byte |
| Truy cập đầu vào | Một lượt quét tuần tự |
| Thời gian truyền | $T_{\rm quét}\ge D/v$; chưa tính xử lý bản ghi hoặc các chi phí khác |
| Kết quả | Tổng chính xác và đúng tập khóa theo đặc tả |

Mô hình thao tác đơn vị giả định kích thước khóa và tổng được xử lý trong chi phí đã nêu. Nếu tên máy chủ hoặc số nguyên dài tùy ý, phải tính thêm chi phí biểu diễn và thao tác theo độ dài. Dung lượng thực gồm khóa, tổng và phần phụ trợ của bảng.

Nếu bảng $h$ khóa không vừa $M$, chứng minh toán học vẫn đúng nhưng cài đặt giữ toàn bộ bảng trong bộ nhớ không khả thi. Cần thay cách tổ chức ngoài bộ nhớ hoặc phân tán và phân tích lại chi phí. Chỉ được đổi sang kết quả xấp xỉ khi đặc tả cho phép. Nguồn bối cảnh chi phí: MMDS mục 1.3.3, trang 13; BHK trang PDF 10. Không dùng tốc độ thiết bị lịch sử trong sách như tốc độ phần cứng hiện tại.

Tự kiểm tra: nêu cả hai vế bất biến sau ba bản ghi. Nếu xóa khóa có tổng 0 để tiết kiệm chỗ, mệnh đề nào không còn đúng?

## Khung đánh giá một lời giải

Ví dụ tổng byte phân biệt năm tầng cần thống nhất với nhau:

| Tầng | Nội dung trong ví dụ |
|---|---|
| Bài toán | Tổng byte theo từng máy chủ |
| Biểu diễn | Dãy cặp máy chủ–kích thước và bảng tổng |
| Thuật toán | Quét, khởi tạo khóa mới, cộng dồn |
| Cài đặt | Ngôn ngữ, bảng băm, kiểu tổng, cách đọc tệp |
| Kết quả | Bảng tổng cụ thể; nếu đo thời gian, phải ghi thiết lập đo |

Chứng minh thuật toán, cận chi phí và kết quả đo thực nghiệm là những bằng chứng khác nhau. Một lần chạy đúng không chứng minh mọi đầu vào; một lần chạy nhanh không chứng minh cận tiệm cận.

### Tài nguyên và thời gian phục vụ

| Mặt cần xét | Ứng dụng dẫn đến yêu cầu |
|---|---|
| Khối lượng tính toán | Gần trùng có số cặp tăng bậc hai; đồ thị cần tính lặp |
| Bộ nhớ | Bảng tổng theo khóa, trạng thái dòng, véc-tơ và chỉ mục |
| Đọc/ghi và lượt quét | Sắp ngoài, tra cứu và kết nối bảng |
| Truyền thông, phối hợp | Kho phân tán, dữ liệu trung gian, chạy lại tác vụ |
| Độ trễ truy vấn | Truy hồi véc-tơ, tra khóa, từ khóa và vùng |
| Cập nhật | Bản ghi dòng mới đến; chỉ mục phải theo dữ liệu mới |
| Dung lượng lưu trữ | Dòng mã cùng mô hình hoặc từ điển để giải mã |

Độ trễ một truy vấn khác tổng thời gian xử lý cả kho; cả hai khác thời gian xây chỉ mục. Ngân sách bộ nhớ, thời gian và sai số có đơn vị khác nhau, nên không cộng trực tiếp thành một đại lượng tối ưu khi chưa định nghĩa mục tiêu.

### Bảo đảm phải gắn với đặc tả

Văn bản nén không mất thông tin phải giải mã đúng; ảnh có lượng tử hóa cần tiêu chí sai số tái tạo. Chọn cặp ứng viên cần xét cả ứng viên giả và bỏ sót. Truy hồi gần đúng cần đo độ thu hồi cùng tài nguyên. Bộ lọc Bloom chuẩn và lọc hộp bao có điều kiện không bỏ nghiệm, nhưng dựa trên hai cơ chế khác nhau.

Phải phân biệt bảo đảm xác suất dưới giả thiết ngẫu nhiên, cận xác định và chất lượng đo trên tập truy vấn. Không hứa một phương pháp đồng thời nhanh nhất, nhỏ nhất và chính xác tuyệt đối cho mọi dữ liệu.

Tự kiểm tra: bước kiểm tra lại giải quyết loại lỗi nào trong chọn ứng viên? Chi phí xây chỉ mục có thể được bỏ khỏi báo cáo chỉ vì một truy vấn chạy nhanh không?

## Nội dung học phần và phương pháp sẽ học

Học phần **Giải thuật nền tảng của Khoa học dữ liệu**, mã **UET.DSE2053**, có **3 tín chỉ**. Đề cương quy định bốn chuẩn đầu ra học phần (CLO): giải thích nguyên lý và giải thuật; phân tích để lựa chọn; thiết kế, triển khai và đánh giá; tự học và xử lý dữ liệu có trách nhiệm.

Riêng Bài 01, sinh viên cần tạo được ba sản phẩm:

1. Đặc tả và giải thích bất biến của tổng byte: giữ đúng tập khóa và đúng tổng, kể cả khóa có tổng 0; nêu điều kiện của cận chi phí.
2. Phân tích một ứng dụng đã khảo sát: xác định đầu ra, giới hạn tài nguyên và bảo đảm có điều kiện; phân biệt bảo đảm với kết quả đo.
3. Tính kỳ vọng trùng trong bài tập: dùng đúng đơn vị đếm và giả thiết; nêu giới hạn khi suy luận về dữ liệu.

Các câu tự kiểm về bảng tổng, ứng viên và hai bài tập MMDS kiểm những sản phẩm này. Việc triển khai thuật toán chuyên biệt thuộc các bài sau.

![Bài01 là nền chung cho năm nhóm bài liền nhau: phân tán và xếp hạng; tương đồng và tìm gần; dòng và cửa sổ; nén; lưu trữ và truy vấn](img/lec-01/ban-do-hoc-phan.svg)

Bảng dưới đây là danh mục của học phần, theo thứ tự đề xuất của đề cương. Bài 01 chỉ định vị vai trò và thuộc tính cần đánh giá; cơ chế, chứng minh và cài đặt thuộc bài tương ứng.

| Bài | Phương pháp và cấu trúc sẽ học | Ứng dụng và thuộc tính cần đánh giá |
|---:|---|---|
| 02 | MapReduce; ánh xạ, nhóm, rút gọn; bộ kết hợp và phân vùng | Tổng hợp kho phân tán; bảo toàn đóng góp, truyền thông và phối hợp khôi phục tác vụ |
| 03 | PageRank; phép lặp, xử lý nút cụt và bẫy nhện | Xếp hạng web; điều kiện hội tụ, tiêu chuẩn dừng và chi phí mỗi vòng |
| 04 | PageRank theo chủ đề, TrustRank, khối lượng rác, HITS | Chủ đề và liên kết thao túng; giả thiết tín hiệu, phạm vi đồ thị, giới hạn diễn giải |
| 05 | Shingling, độ đo Jaccard, MinHash | Gần trùng; dưới hoán vị đều, xác suất trùng MinHash bằng độ tương đồng Jaccard |
| 06 | Băm nhạy cảm cục bộ (LSH), phân dải và khuếch đại | Tạo ứng viên; xác suất ứng viên, bỏ sót và chi phí đối chiếu |
| 07 | HNSW; lượng tử hóa tích (PQ); IVF-PQ | Truy hồi véc-tơ; độ thu hồi, độ trễ, bộ nhớ, xây dựng; phân biệt phép đo với bảo đảm lý thuyết |
| 08 | Lấy mẫu theo khóa, lấy mẫu hồ chứa, bộ lọc Bloom | Dòng truy vấn; đơn vị và phân phối mẫu, cập nhật, sai số một phía có điều kiện |
| 09 | Flajolet–Martin, phác thảo Count-Min, AMS, DGIM, suy giảm mũ | Thống kê dòng; đại lượng, cửa sổ, loại sai số và trạng thái; DGIM có cận xác định |
| 10 | Huffman tĩnh, Huffman thích nghi, mã hóa số học | Nén không mất thông tin; độ dài mã, dữ liệu phụ trợ, khôi phục đúng |
| 11 | LZ77, LZ78, LZW; JPEG dựa trên biến đổi cô-sin rời rạc (DCT) | Mẫu lặp và ảnh; đồng bộ từ điển, trạng thái; phân biệt LZ không mất thông tin với lượng tử hóa ảnh |
| 12 | Sắp xếp trộn ngoài bộ nhớ, chọn thay thế | Sắp tệp lớn; dãy có thứ tự, số lượt đọc/ghi và bộ đệm |
| 13 | B-Tree, B+-Tree, băm tĩnh, chỉ mục bitmap | Tra khóa/khoảng; loại truy vấn, dung lượng, xây dựng và cập nhật |
| 14 | Chỉ mục đảo, R-tree, kd-tree, ball tree, Z-order | Từ khóa và không gian; cắt nhánh, độ đầy đủ của lọc và tinh lọc |
| 15 | Nối vòng lặp theo bản ghi/khối/chỉ mục; nối sắp xếp–trộn; nối băm và Grace Hash | Kết nối bảng; đúng mọi cặp khớp, ngân sách bộ nhớ, lệch phân hoạch, đọc/ghi |

MapReduce là mô hình xử lý; Jaccard là độ đo; chỉ mục là cấu trúc dữ liệu. Spark và Faiss là phần mềm hỗ trợ khi bài tương ứng sử dụng, không được gộp tất cả các tên thành “thuật toán”. HNSW, HITS, AMS và DGIM được giữ như tên phương pháp; IVF-PQ kết hợp chỉ mục phân vùng với mã lượng tử hóa tích.

Năm nhóm theo thứ tự học là Bài 02–04, 05–07, 08–09, 10–11 và 12–15. Tiên quyết có các nhánh: Bài 01 đến 02–03–04; đến 05–06–07; đến 08–09; đến 10–11; đến 12–13–14. Bài 12–13 hỗ trợ Bài 15; Bài 02 hỗ trợ cách tính phân tán khi cần. Nhóm sau không mặc nhiên cần toàn bộ nhóm trước.

## Kiến thức, kỹ năng và cách học

### Kiến thức đầu vào và phần cần ôn

Tiên quyết chính thức là UET.CS1058. Sinh viên cần lập trình, đọc giả mã, dùng cấu trúc dữ liệu và phân tích độ phức tạp. Nền cơ sở dữ liệu, xác suất, toán rời rạc và đại số tuyến tính được dùng theo mạch.

| Mạch | Phần nền cần huy động |
|---|---|
| Phân tán và xếp hạng | Khóa–giá trị, tính kết hợp; đồ thị, ma trận, xác suất |
| Tương đồng và hàng xóm gần | Tập hợp, băm, véc-tơ, khoảng cách, xác suất |
| Dòng và cửa sổ | Biến ngẫu nhiên, kỳ vọng, xác suất, trạng thái cập nhật |
| Nén | Phân phối ký hiệu, cây, chuỗi, từ điển; biến đổi cho ảnh |
| Lưu trữ và truy vấn | Bản ghi, khối, cây chỉ mục và phép nối quan hệ |

Không yêu cầu biết sẵn MapReduce, PageRank hoặc HNSW. Để tự đối chiếu nền chung, hãy chạy bước thứ ba của bảng tổng và giải thích phép nhân xác suất của hai biến cố độc lập. Nếu chưa giải thích được, ôn phần vòng lặp/bảng ánh xạ hoặc xác suất trước mạch liên quan.

### Kỹ năng cần tạo thành sản phẩm

Giải thích một phương pháp phải nêu được đặc tả, cơ chế và giả thiết. Phân tích lựa chọn phải chỉ ra tài nguyên trội và bảo đảm cần giữ. Khi thiết kế và triển khai, cần có vết chạy nhỏ, luận điểm chứng minh, trường hợp biên và bảng chi phí.

Nền thực hành gồm Python hoặc C++, đọc tài liệu chuyên ngành tiếng Anh và làm việc với giả mã. Báo cáo thử nghiệm cần ghi dữ liệu, tham số, môi trường, kết quả hiệu suất và chất lượng đầu ra để người khác kiểm tra lại. Các yêu cầu này cụ thể hóa CLO1–CLO3; không biến một kết quả đo thành định lý.

### Thái độ thể hiện trong cách làm việc

Đọc trước và ghi lại điểm chưa hiểu để tự học có mục tiêu. Khi phản biện, chỉ rõ giả thiết hoặc bước suy luận cần kiểm. Khi làm nhóm, ghi nguồn và đóng góp của từng thành viên. Báo cáo cả sai số, hạn chế và kết quả không như dự kiến.

Trách nhiệm dữ liệu gồm cách thu thập, xử lý, sử dụng và chia sẻ phù hợp quy định áp dụng. Tránh gán ý định cho con người từ một mẫu trùng trong dữ liệu. Đây là hành vi học tập theo CLO4, không phải một chính sách đánh giá mới.

### Chuẩn bị Bài 02

Đọc MMDS Chương 2 theo tài liệu Bài 02. Ôn ánh xạ khóa–giá trị, phép nhóm và tính kết hợp, giao hoán của phép cộng. Với tổng số nguyên không tràn, thay cách nhóm hoặc thứ tự cộng giữ nguyên tổng nếu mỗi đóng góp được tính đúng một lần. Bất biến giúp kiểm tra điều kiện ấy.

Bài 01 không đặt thêm bài lập trình hoặc phần mềm bắt buộc. Phần thực hành theo đúng bài và tài liệu đã chỉ định. Một chương trình tính đúng theo mô hình vẫn cần được kiểm tra về ý nghĩa suy luận từ dữ liệu; phần sau dùng mẫu trùng để làm rõ giới hạn đó.

## Mô hình ngẫu nhiên và giới hạn suy luận

### Mô hình hồ sơ lưu trú

MMDS mục 1.2.3, trang 7–8 xét việc tìm các cặp có hoạt động phối hợp từ hồ sơ khách sạn. Mô hình nền giả sử không có nhóm như vậy, với:

| Ký hiệu | Ý nghĩa | Giá trị |
|---|---|---:|
| $P$ | Số người | $10^9$ |
| $T$ | Số ngày quan sát | $1000$ |
| $H$ | Số khách sạn | $10^5$ |
| $q$ | Xác suất một người đi khách sạn mỗi ngày | $0{,}01$ |

Mỗi người quyết định độc lập giữa người và ngày; nếu đi thì chọn đều một trong $H$ khách sạn. Nguồn dùng 100 chỗ mỗi khách sạn để đặt quy mô $H$; phép tính ngẫu nhiên không áp thêm giới hạn sức chứa cứng làm các lựa chọn phụ thuộc.

Một phép thử gồm một cặp người và một cặp ngày khác nhau. Biến cố trùng xảy ra nếu hai người ở cùng khách sạn trong từng ngày được chọn; khách sạn có thể khác giữa hai ngày.

![Một cặp người và một cặp ngày được ghép thành phép thử cùng khách sạn trong từng ngày](img/lec-01/phep-thu-va-duong-tinh-gia.svg)

### Từ xác suất một phép thử đến kỳ vọng

::: derivation
Hai người cùng đi trong một ngày có xác suất $q^2$. Khi đã đi, xác suất chọn cùng khách sạn là $1/H$. Do đó:

$$
p=\frac{q^2}{H}=10^{-9}.
$$

Hai ngày độc lập cho xác suất trùng trong cả hai ngày là $p^2=10^{-18}$.

Với mỗi cặp người và cặp ngày, đặt biến chỉ báo bằng 1 nếu trùng, bằng 0 nếu không. Gọi $X$ là tổng các chỉ báo, tức số biến cố **cặp người–cặp ngày** trùng. Tính tuyến tính kỳ vọng cho:

$$
\mathbb E[X]=\binom P2\binom T2p^2
=\binom{10^9}{2}\binom{1000}{2}10^{-18}
=249\,749{,}99975025.
$$

Làm tròn được $249\,750$. MMDS dùng $\binom n2\approx n^2/2$ và được khoảng $250\,000$.
:::

Các phép thử có thể chia sẻ người hoặc ngày; tính tuyến tính kỳ vọng không đòi hỏi chúng độc lập. Giả thiết độc lập trong mô hình được dùng khi tính $q^2$ và $p^2$.

$X$ không phải số cặp người phân biệt: một cặp có thể trùng trên nhiều bộ ngày. Phép đếm chính xác ở đây là số biến cố; cách gọi cặp trong nguồn dựa trên xấp xỉ hiếm trùng nhiều lần. Không cần đồng nhất hai đại lượng để thấy quy mô trùng ngẫu nhiên.

### Diễn giải có điều kiện

MMDS gọi cảnh báo này là nguyên lý Bonferroni phi hình thức: cần ước lượng số mẫu trùng dưới dữ liệu ngẫu nhiên trước khi coi kết quả tìm được là bằng chứng. Phần này không trình bày định lý hiệu chỉnh kiểm định nhiều lần.

Một thuật toán liệt kê đúng các mẫu trùng chỉ đáp ứng đặc tả tìm kiếm. Kỳ vọng nền không tự cho xác suất một người thuộc nhóm cần tìm khi đã thấy trùng. Kết luận ấy còn phụ thuộc mô hình thay thế, tỷ lệ nền và tính phù hợp của giả thiết về dữ liệu.

Tự kiểm tra: giải thích nơi dùng độc lập và nơi chỉ dùng tuyến tính kỳ vọng. Nếu một cặp người trùng trên ba ngày, họ đóng góp bao nhiêu biến cố cặp ngày vào $X$?

## Bài tập từ MMDS

Hai bài sau lấy trực tiếp từ MMDS, mục 1.2.4, trang 8. Giữ dữ kiện và yêu cầu toán học, dịch và chia bước để dựng mô hình, tính, rồi diễn giải. Gợi ý và lời giải có thể mở riêng.

### Bài 1.2.1: thay đổi quy mô quan sát

::: exercise
Dùng mô hình hồ sơ lưu trú ở mục 1.2.3 của nguồn. Số cặp bị báo nghi vấn thay đổi thế nào nếu áp dụng **từng thay đổi riêng**, các số khác giữ nguyên?

(a) Tăng số ngày quan sát lên $2000$.

(b) Tăng số người được quan sát lên $2$ tỷ; do đó có $200\,000$ khách sạn.

(c) Chỉ báo một cặp nếu họ cùng ở một khách sạn vào cùng thời điểm trong ba ngày khác nhau. Khách sạn có thể khác giữa các ngày; điều kiện trùng được xét trong từng ngày.

Sản phẩm: với mỗi phần, ghi số phép thử, xác suất một phép thử, kỳ vọng và diễn giải theo mô hình.
:::

::: hint
Nếu cần trùng trong $k$ ngày khác nhau, đơn vị đếm gồm cặp người và **bộ $k$ ngày**. Kỳ vọng số biến cố là:

$$
\binom P2\binom Tk\left(\frac{q^2}{H}\right)^k.
$$

Dùng $k=2$ cho (a), (b); $k=3$ cho (c). Với (b), cả $P$ và $H$ đều thay đổi. Phân biệt giá trị dùng tổ hợp với xấp xỉ của sách.
:::

::: solution
Cơ sở là $249\,749{,}99975025$ biến cố; sách làm tròn bằng xấp xỉ lũy thừa thành khoảng $250\,000$.

**(a)** Chỉ thay $T=2000$:

$$
\mathbb E[X_a]=\binom{10^9}{2}\binom{2000}{2}10^{-18}
=999\,499{,}9990005\approx999\,500.
$$

Tỷ lệ so cơ sở là $\binom{2000}{2}/\binom{1000}{2}=3998/999$, gần 4 nhưng không đúng bằng 4. Xấp xỉ $\binom T2\approx T^2/2$ của sách cho khoảng $1\,000\,000$.

**(b)** Thay $P=2\times10^9$, $H=2\times10^5$:

$$
\mathbb E[X_b]=\binom{2\times10^9}{2}\binom{1000}{2}
\left(5\times10^{-10}\right)^2
=249\,749{,}999875125\approx249\,750.
$$

Số cặp người gần gấp 4, còn xác suất trùng trong hai ngày giảm đúng 4 lần. Kỳ vọng gần như không đổi; xấp xỉ của sách cho khoảng $250\,000$. Không nói tổ hợp chính xác cho giá trị hoàn toàn bằng cơ sở.

**(c)** Giữ quy mô gốc, chọn bộ ba ngày:

$$
\mathbb E[X_c]=\binom{10^9}{2}\binom{1000}{3}10^{-27}
=0{,}0830834999169165\approx0{,}0831.
$$

Yêu cầu ba ngày làm kỳ vọng trùng ngẫu nhiên xuống dưới 1 trong mô hình. Điều đó không có nghĩa không thể xuất hiện trùng và không chứng minh danh tính của một cặp. Xấp xỉ $\binom T3\approx T^3/6$ cho khoảng $0{,}0833$.
:::

### Bài 1.2.2: trùng tập mặt hàng

::: exercise
Có thông tin mua sắm của $100$ triệu người. Mỗi người đi siêu thị $100$ lần trong một năm và mua $10$ trong $1000$ mặt hàng được bán.

Đề đặt giả thuyết rằng một cặp khủng bố sẽ mua đúng cùng một tập $10$ mặt hàng vào một thời điểm trong năm. Nếu tìm các cặp người đã mua cùng một tập mặt hàng, có thể kỳ vọng những người tìm được thực sự là khủng bố không?

Chú thích 3 của nguồn yêu cầu chấp nhận giả thuyết làm việc ấy, không bàn việc khủng bố có nhất thiết mua như vậy. Đây là giả thuyết của bài tập, không phải căn cứ gán nhãn người trong dữ liệu thực.

Sản phẩm: đơn vị đếm, mô hình nền, xác suất, kỳ vọng và câu trả lời có điều kiện.
:::

![Một lượt mua của người thứ nhất và một lượt mua của người thứ hai được so sánh theo tập mười mặt hàng](img/lec-01/ung-dung-trung-gio-hang.svg)

::: hint
Trong mô hình nền, mỗi lượt chọn đều một tập 10 phần tử trong 1000 mặt hàng, độc lập với các lượt khác. Với hai người khác nhau, có bao nhiêu cách chọn một lượt của người thứ nhất và một lượt của người thứ hai? Các mặt hàng trong một giỏ là một tập, không phải dãy có thứ tự.
:::

::: solution
Đặt $Y$ là số cặp lượt mua của hai người khác nhau có cùng tập mặt hàng. Có $\binom{10^8}{2}$ cặp người và $100^2$ cặp lượt cho mỗi cặp người. Không chỉ so lượt cùng số thứ tự giữa hai người.

Có $\binom{1000}{10}$ tập mặt hàng. Sau khi cố định tập của lượt thứ nhất, xác suất lượt thứ hai chọn đúng tập ấy là $1/\binom{1000}{10}$. Theo tuyến tính kỳ vọng:

$$
\mathbb E[Y]=\frac{\binom{10^8}{2}\,100^2}{\binom{1000}{10}}
\approx0{,}000189818469
\approx1{,}90\times10^{-4}.
$$

Kỳ vọng trùng ngẫu nhiên rất nhỏ dưới mô hình chọn đều, độc lập. Theo tiêu chí Bonferroni phi hình thức và giả thuyết làm việc của đề, việc tìm mẫu trùng này không bị ngập bởi các trùng ngẫu nhiên như ví dụ khách sạn.

Có thể làm rõ ý nghĩa “ít trùng” mà không suy danh tính: vì $Y$ là số nguyên không âm, chỉ báo $\mathbf1_{\{Y\ge1\}}\le Y$. Lấy kỳ vọng hai vế được $\Pr(Y\ge1)\le\mathbb E[Y]$. Xác suất xuất hiện ít nhất một trùng ngẫu nhiên trong mô hình vì thế không vượt khoảng $1{,}90\times10^{-4}$.

Tuy nhiên, xác suất có điều kiện một cặp là khủng bố sau khi quan sát trùng không được xác định chỉ từ $\mathbb E[Y]$ và giả thuyết nguồn. Còn cần tỷ lệ nền và mô hình cho nhóm cần tìm. Lượt mua thực cũng không nhất thiết độc lập hay chọn đều. Đó là giới hạn khi chuyển câu trả lời của bài tập sang kết luận thực tế.
:::

## Đọc thêm và tài liệu nguồn

Các chủ đề cao chiều và hai cách nhìn mô hình trong bản trước được chuyển khỏi tuyến chính. Đọc MMDS mục 1.1 để phân biệt mô hình thống kê với bản tóm tắt phục vụ truy vấn; đọc BHK Chương 1–2 để tìm hiểu dữ liệu cao chiều. Không dùng những chủ đề đọc thêm này làm điều kiện hoàn thành Bài 01.

- **Đề cương học phần:** nguồn xác định mã UET.DSE2053, chuẩn đầu ra, tiên quyết và thứ tự 15 bài; xem [chỉ mục học phần](index.html).
- **Mining of Massive Datasets, ấn bản 3:** Chương 1 cho chi phí và hai bài tập; Chương 2, 5, 3, 4 cho phân tán, xếp hạng, tương đồng và dòng. Nội dung và các sơ đồ tương ứng được biên soạn lại theo sách cùng slide chính thức. Ghi công tác giả tại [MMDS](http://www.mmds.org).
- **Stanford CS246:** bài mở đầu trang chiếu 62 cho tổng byte; 03-lsh trang 14 cho quy mô so cặp. Các phần MMDS tương đương được ưu tiên; tình huống tổng byte dùng Stanford vì đặc tả đầu ra trực tiếp phù hợp ví dụ xuyên suốt.
- **Blum–Hopcroft–Kannan, Foundations of Data Science:** Chương 1–2, đặc biệt trang PDF 9–12, cho giới hạn mô hình bộ nhớ và định hướng đọc thêm.
- **BIODS 271 và Princeton COS 597A:** các trang đã dẫn trong ứng dụng véc-tơ; tài liệu và bài báo HNSW/PQ theo Bài 07 dùng để học cơ chế chi tiết.
- **Nelson–Gailly, The Data Compression Book:** Chương 3–5, 8–9, 11; slide CMU LZ và lossy theo Bài 10–11.
- **Database System Concepts, ấn bản 7:** slide Chương 14–15, 24 và nội dung Chương 31 theo Bài 12–15. UMass CS514 Lecture 10 bổ sung Count-Min trong Bài 09.

Các dẫn trang trong từng ứng dụng cho biết phần nguồn được dùng; hình là sơ đồ được vẽ lại, không phải biểu đồ đo hiệu năng. [Quay về bộ trang chiếu](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html).
