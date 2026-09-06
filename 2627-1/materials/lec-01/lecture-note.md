# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

## Nội dung và kết quả buổi học

Bài học khảo sát các bài toán dữ liệu của Bài 02–15, từ đó xác định giới hạn tài nguyên và yêu cầu đối với thuật toán. Bài toán tìm cặp tài liệu gần trùng được phân tích qua biểu diễn, đặc tả, thuật toán xét mọi cặp và các tiêu chí đánh giá. Phần cuối giới thiệu nội dung học phần, sự chuẩn bị cần có và các giả thiết khi suy luận từ dữ liệu.

Sau buổi học, sinh viên có thể:

1. Nêu đầu vào, đầu ra và trở ngại của một bài toán dữ liệu.
2. Giải thích tính đúng của thuật toán xét mọi cặp và phân biệt các khía cạnh đánh giá lời giải.
3. Phân biệt kết quả tính toán với kết luận rút ra về dữ liệu; tính kỳ vọng trùng dưới các giả thiết đã cho.

[Bộ trang chiếu Bài 01](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html) dùng cùng dữ kiện và ký hiệu. Ghi chú mở rộng đặc tả, chứng minh, điều kiện chi phí và lời giải bài tập.

## Tổng hợp và tìm kiếm trên kho web

### Tính tổng kích thước trang web theo máy chủ

Kho thu thập web lưu các bản ghi gồm địa chỉ trang, kích thước và ngày thu thập. Máy chủ được xác định từ địa chỉ trang. Bài toán yêu cầu cộng kích thước các trang có trong kho thuộc cùng máy chủ, rồi trả một tổng cho mỗi máy chủ. Tổng này không phải lưu lượng truy cập hoặc dung lượng toàn bộ máy chủ.

Bốn bản ghi minh họa đầu ra có dạng rút gọn:

| Máy chủ | Kích thước trang (byte) |
|---|---:|
| a.vn | 40 |
| b.vn | 25 |
| a.vn | 15 |
| c.vn | 0 |

Kết quả là a.vn có $40+15=55$ byte, b.vn có 25 byte và c.vn có 0 byte. Đây là ví dụ nhỏ để kiểm tra phép tính; nó không mô tả quy mô thật của một kho web.

Gọi $D$ là số byte của tệp bản ghi và $M$ là dung lượng bộ nhớ chính khả dụng. Khi $D>M$, cách nạp trọn tệp để xử lý không khả thi. $D$ đo dung lượng tệp đầu vào, không đồng nhất với tổng kích thước nội dung các trang được ghi trong tệp.

![Tệp bản ghi lớn trên đĩa không thể nạp trọn vào bộ nhớ chính hữu hạn](img/lec-01/kho-nhat-ky-bo-nho.svg)

Một hướng xử lý là đọc tuần tự và chỉ giữ tổng đang chạy theo máy chủ. Bảng tổng cũng phải vừa bộ nhớ; số máy chủ phân biệt quyết định kích thước bảng này. Phần phân tích thuật toán sẽ dùng lại bốn bản ghi trên để kiểm tra cách cập nhật và chứng minh tính đúng. Nguồn bài toán: Stanford CS246 01-intro, trang chiếu 62; bối cảnh truy cập ngoài bộ nhớ: MMDS 1.3.4, tr. 13 và BHK trang PDF 10.

### Đếm số lần xuất hiện của từng từ

Khi kho tài liệu được chia trên nhiều máy, thống kê toàn kho cần kết hợp dữ liệu ở nhiều nơi. Bài toán đếm từ nhận các tài liệu và trả một bảng từ–số lần xuất hiện. Nếu một từ xuất hiện nhiều lần trong một tài liệu, phải tính đủ các lần đó; đầu ra khác với số tài liệu chứa từ.

![Cùng từ w nằm ở hai phần kho; gom mọi tài liệu qua mạng về một máy làm tập trung đường truyền và công việc](img/lec-01/ung-dung-tong-hop-phan-tan.svg)

Hình lấy một từ $w$ để biểu diễn một khóa có mặt ở nhiều phần kho, không gán số đếm cụ thể. Gom toàn bộ tài liệu về một máy phải truyền cả dữ liệu và dồn việc vào máy nhận. Nếu máy hoặc tác vụ lỗi, chạy lại phải tránh bỏ sót và đếm trùng.

Tính đóng góp tại nơi lưu dữ liệu rồi gom theo từ là hướng xử lý của Bài 02. Lượng dữ liệu trung gian, phân bố tải và cơ chế xử lý kết quả tác vụ chạy lại đều ảnh hưởng đến lời giải. Nguồn: MMDS 2.1–2.2.6; slide Chương 2, trang 8–13 và 20.

### Tính điểm quan trọng của trang web

Thống kê từ mô tả nội dung kho. Khi một truy vấn khớp nhiều trang, hệ thống tìm kiếm còn phải sắp xếp các kết quả. Bài toán ở đây dùng cấu trúc liên kết để tính một điểm quan trọng cho mỗi trang, làm một tín hiệu hỗ trợ việc sắp xếp.

Đầu vào là đồ thị có hướng: đỉnh biểu diễn trang, cạnh biểu diễn liên kết. Đồ thị trong hình có ba đỉnh $y,a,m$: $y$ trỏ tới $y,a$; $a$ trỏ tới $y,m$; $m$ trỏ tới $a$. Khuyên tại $y$ biểu diễn liên kết từ trang đó về chính nó.

![Ba trang liên kết có hướng; việc đọc liên kết và cập nhật điểm được lặp lại để tính điểm hỗ trợ sắp kết quả](img/lec-01/ung-dung-xep-hang-web.svg)

Trong PageRank, điểm của một trang phụ thuộc điểm của các trang trỏ tới nó. Mỗi vòng cập nhật vì thế phải đọc liên kết và tính đóng góp cho nhiều trang. Một ma trận đặc cho mọi cặp trang còn có thể lãng phí bộ nhớ khi đồ thị thưa. Bài 03 phân tích biểu diễn, chi phí mỗi vòng, hội tụ và điều kiện dừng.

Điểm quan trọng theo liên kết không đo đầy đủ độ liên quan với một truy vấn. Hình chỉ nêu đầu ra cần tính, không gán trước các điểm hay thứ hạng. Nguồn: MMDS 5.1–5.2; Link Analysis 1, trang 18–21, 48 và 53.

### Ưu tiên kết quả tìm kiếm theo chủ đề

Một điểm quan trọng dùng chung cho mỗi trang chưa phân biệt các chủ đề của truy vấn. “Jaguar” có thể chỉ loài báo, ô tô, hệ điều hành hoặc máy chơi trò chơi. Với chủ đề đã xác định là ô tô, yêu cầu là ưu tiên các trang về xe trong kết quả tìm kiếm.

![Truy vấn jaguar có bốn nghĩa; chủ đề ô tô đã biết xác định mục tiêu ưu tiên trang về xe](img/lec-01/ung-dung-truy-van-theo-chu-de.svg)

Đầu vào bổ sung là chủ đề cần ưu tiên; đầu ra là điểm và thứ tự có xét chủ đề đó. Xác định chủ đề từ truy vấn hoặc ngữ cảnh là công việc riêng. Hình biểu diễn yêu cầu, không phải thứ hạng đã tính.

Lưu một bộ điểm cho toàn bộ trang web riêng với từng người dùng sẽ tốn quá nhiều bộ nhớ ở quy mô web. MMDS đề xuất dùng một số bộ điểm theo chủ đề thay vì một bộ đầy đủ cho mỗi người. Bài 04 học cách đưa chủ đề vào xếp hạng; phương pháp không bảo đảm suy đoán đúng ý định của mọi người dùng. Nguồn: MMDS 5.3.1, tr. 195–196.

### Hạn chế liên kết rác trong xếp hạng

Điểm dựa trên liên kết còn có thể bị đẩy lên bởi một bên cố ý tạo nhiều trang hỗ trợ. Bài toán là hạn chế ảnh hưởng của các liên kết rác lên điểm hạng và kết quả tìm kiếm.

![Ba nhóm trang theo Hình 5.16; cụm cùng bên kiểm soát chứa đích t và các trang hỗ trợ liên kết qua lại](img/lec-01/ung-dung-lien-ket-thao-tung.svg)

Hình phân biệt trang ngoài tầm tác động, trang cho phép bên tạo rác đặt liên kết, và trang do bên đó sở hữu. Các trang có thể tác động trỏ đến đích $t$; $t$ trỏ đến từng trang hỗ trợ và mỗi trang hỗ trợ trỏ lại $t$. Đích và các trang hỗ trợ nằm trong cùng cụm kiểm soát.

Nhiều liên kết không nhất thiết đến từ nhiều nguồn độc lập. Chỉ xét số liên kết hoặc điểm truyền tới một trang chưa đủ để đánh giá độ tin cậy. Một hướng là dùng tập trang tin cậy ban đầu để điều chỉnh điểm, như TrustRank. Việc chọn tập tin cậy là yêu cầu riêng; phương pháp không bảo đảm loại hết liên kết rác. Sơ đồ cũng không đủ chứng minh danh tính hoặc ý định của một người ngoài đời. Nguồn: MMDS 5.4.1–5.4.4, Hình 5.16; Bài 04.

### Tìm các cặp tài liệu gần trùng

Ngay cả khi đã xử lý điểm hạng, kết quả tìm kiếm vẫn có thể chứa các bản sao chỉ khác một phần văn bản. Đầu vào của bài toán gần trùng là một kho tài liệu; đầu ra là các cặp có độ tương đồng đạt ngưỡng đã chọn.

“Gần trùng” ở đây xét phần văn bản chung, không chỉ việc hai tài liệu nói về cùng chủ đề. Biểu diễn tài liệu, độ đo tương đồng và ngưỡng phải được xác định trước khi đánh giá kết quả.

![Hai tài liệu giữ chung nhiều đoạn và sửa một phần; trong kho, so sánh trực tiếp phải xét mọi cặp tài liệu](img/lec-01/ung-dung-tai-lieu-gan-trung.svg)

Nét trong hai trang chỉ minh họa phần chung và phần sửa, không biểu diễn một số đo. Với $N$ tài liệu, so sánh tất cả cần xét $N(N-1)/2$ cặp không thứ tự. Khi $N=10^6$:

$$
\binom{10^6}{2}=499\,999\,500\,000\approx5\times10^{11}.
$$

Gần 500 tỷ là số cặp, không phải kết quả đo thời gian. Biểu diễn gọn giúp giảm chi phí mỗi lần so sánh; chọn ứng viên giúp giảm số cặp phải đối chiếu. Kiểm tra lại dữ liệu gốc có thể loại ứng viên sai, nhưng không khôi phục cặp đã bị bỏ sót. Bài 05–06 phân tích các phương pháp và xác suất này. Nguồn: MMDS 3.1–3.4; Stanford CS246 03-lsh, trang chiếu 14.

### Tìm đoạn tài liệu bằng véc-tơ truy vấn

Tìm mọi cặp gần trùng xét cả kho. Một nhu cầu khác là cho một truy vấn rồi tìm các đoạn tài liệu gần truy vấn ấy. Mỗi đoạn tài liệu và truy vấn được mã hóa thành một dãy số, gọi là véc-tơ. Cùng một phép mã hóa được dùng cho cả đoạn và truy vấn, tạo các véc-tơ cùng số chiều.

Cho một quy tắc tính khoảng cách và số lượng $k$, đầu ra chính xác gồm $k$ đoạn có véc-tơ gần truy vấn nhất. Điều kiện là $1\le k\le N$, với $N$ là số đoạn; cần chốt cách xử lý khi nhiều đoạn bằng khoảng cách. Độ gần theo véc-tơ không tự bảo đảm đúng về ngữ nghĩa.

![Một truy vấn dạng véc-tơ được đối chiếu với các đoạn tài liệu đã mã hóa để trả k đoạn gần nhất](img/lec-01/ung-dung-truy-hoi-vec-to.svg)

BIODS 271 dùng tình huống 10 tỷ véc-tơ, 3072 chiều, mỗi thành phần 32 bit. Quét hết kho cho mỗi truy vấn cần tính 10 tỷ khoảng cách; mỗi khoảng cách còn sử dụng nhiều thành phần. Truy vấn mới phải thực hiện lại công việc này. Quy mô trên lấy từ nguồn, không phải số đo của học phần.

Bài 07 học tổ chức và nén véc-tơ để giảm chi phí truy vấn. Khi cho phép gần đúng, phải đánh giá chất lượng: độ thu hồi tại $k$ là tỷ lệ hàng xóm gần thật xuất hiện trong $k$ kết quả trả về, với tập chuẩn và quy ước hòa đã chốt. Các chi phí khác gồm độ trễ, bộ nhớ, xây dựng và cập nhật chỉ mục. Nguồn: BIODS 271 L12, trang PDF 16 cho bài toán truy hồi đoạn tài liệu, 17–18 cho quy mô; Princeton lớp 8, trang 2–5.

Tự kiểm tra: tìm mọi cặp gần trùng và tìm $k$ mục gần một truy vấn khác nhau về đầu ra và số đối tượng phải xét như thế nào?

## Xử lý dòng dữ liệu, lưu trữ và truy vấn

Các yêu cầu tìm kiếm tạo ra nhật ký cần phân tích. Nội dung văn bản và ảnh cần được lưu để đọc lại. Dữ liệu nằm trên đĩa còn phải được sắp xếp, tra cứu hoặc ghép từ nhiều bảng. Ba nhóm công việc này có đầu ra khác nhau: mẫu và thống kê; dữ liệu khôi phục; kết quả truy vấn. Chúng không nhất thiết là các bước nối tiếp của cùng một hệ thống.

### Giữ mẫu truy vấn và lọc thư đến

Máy tìm kiếm muốn nghiên cứu mức lặp truy vấn của người dùng. Mỗi bản ghi gồm người dùng, truy vấn và thời điểm. Nếu không thể lưu hết nhật ký, hệ thống cần chọn một mẫu vẫn cho phép nghiên cứu hành vi ấy. Lấy mẫu từng bản ghi riêng lẻ có thể làm mất những lần lặp cần đo; chọn người dùng rồi giữ lịch sử truy vấn của họ là đơn vị lấy mẫu phù hợp với ví dụ này.

Bài toán lọc thư có đầu vào khác: một dòng thư kèm địa chỉ gửi và danh sách địa chỉ cho phép. Đầu ra phải nhận thư từ địa chỉ trong danh sách, bỏ thư ngoài danh sách. Nếu danh sách vượt bộ nhớ, mỗi thư có thể cần một lần tra cứu trên đĩa.

![Nhật ký truy vấn tạo mẫu theo người dùng; thư đến được kiểm địa chỉ theo danh sách cho phép](img/lec-01/ung-dung-dong-truy-van.svg)

Giữ một tỷ lệ người dùng cố định không bảo đảm mẫu luôn vừa bộ nhớ khi lịch sử tăng. MMDS mục 4.2.4 xét điều chỉnh tỷ lệ để đáp ứng ngân sách. Với lọc thư, bộ lọc Bloom có thể loại nhanh địa chỉ chắc chắn không có trong danh sách; trường hợp “có thể có” vẫn phải tra danh sách chính xác nếu yêu cầu chỉ nhận thành viên. Bảo đảm không loại nhầm phần tử đã chèn áp dụng cho bộ lọc chuẩn chỉ chèn và tra cứu, không xóa, với băm và trạng thái nhất quán. Thuộc danh sách cho phép không phải bằng chứng rằng mọi thư đều không phải thư rác. Nguồn: MMDS mục 4.2–4.3, trang 136–142; Bài 08.

### Đếm người dùng và lượt truy cập gần đây

Nhật ký truy cập gồm mã người dùng và thời điểm của mỗi lượt. Hai đầu ra thường gặp là số người dùng khác nhau trong phạm vi đã chọn và số lượt truy cập trong một khoảng thời gian gần nhất. Một người quay lại tạo thêm lượt, nhưng không tạo thêm người dùng khác nhau.

![Mốc thời gian tách lượt quá cũ khỏi cửa sổ gần đây; đếm người khác nhau khác với đếm lượt](img/lec-01/ung-dung-thong-ke-cua-so.svg)

Lưu mọi mã đã gặp có thể vượt bộ nhớ khi số người dùng tăng. Truy vấn cửa sổ còn phải loại ảnh hưởng của bản ghi hết hạn. Chỉ lưu tổng số lượt từ đầu là chưa đủ để trả số lượt gần đây. Tuy nhiên, đếm tổng lượt từ đầu chỉ cần một bộ đếm; không phải mọi thống kê trên dòng đều cần thuật toán xấp xỉ.

Bài 09 còn xét tần suất $f_j$ của khóa $j$ và mômen thứ hai $\sum_j f_j^2$, khác tổng số sự kiện $\sum_j f_j$. Đại lượng cần ước lượng và phạm vi thời gian quyết định trạng thái cần giữ. Các phương pháp có bảo đảm sai số khác nhau; DGIM có cận xác định. Nguồn: MMDS mục 4.1.3, 4.4–4.7, trang 134–135, 142–159; UMass CS514 Lecture 10 cho Count-Min.

### Lưu văn bản với ít dung lượng hơn

Một số đếm không đủ để tái tạo nhật ký. Nén văn bản đặt bài toán lưu một biểu diễn có thể giải mã thành đúng chuỗi đầu vào. Trong nén không mất thông tin, mọi ký hiệu và thứ tự đều phải được bảo toàn.

Chuỗi `aabaacabcabcb` trong ví dụ LZ của CMU có các cụm lặp như `ab` và `abc`. Sự lặp lại có thể được khai thác khi mã hóa, nhưng không được tùy ý bỏ phần lặp nếu bộ giải mã không biết phải khôi phục nó ở đâu.

![Dữ liệu mã cùng thông tin giải mã phải khôi phục đúng chuỗi aabaacabcabcb](img/lec-01/ung-dung-nen-van-ban.svg)

Dung lượng phải tính cả dữ liệu mã và thông tin phụ trợ cần giải mã. Không thể hứa mọi chuỗi đều ngắn hơn sau nén. Hình chỉ nêu yêu cầu khôi phục, không cho tỷ lệ nén hoặc bộ mã cụ thể. Nguồn: Nelson–Gailly Chương 3 và 9; CMU LZ, trang logic 11–14; Bài 10–11.

### Giảm dung lượng ảnh với sai số cho phép

Đầu vào là ảnh cần lưu hoặc truyền. Với nén có mất thông tin, đầu ra sau giải mã được phép khác ảnh gốc nhưng phải đáp ứng tiêu chí chất lượng của ứng dụng. Các ứng dụng cần khôi phục nguyên vẹn ảnh phải dùng đặc tả khác.

![Minh họa định tính: nhiều mức sáng gần nhau được gộp thành ít mức đại diện hơn, làm mất phân biệt giữa các mức ban đầu](img/lec-01/ung-dung-nen-anh.svg)

Thay các mức sáng gần nhau bằng một mức đại diện làm mất thông tin. Đây là lượng tử hóa, một bước khác với phép biến đổi trong tuyến nén JPEG. Không thể suy ra tỷ lệ nén hoặc chất lượng từ hình định tính; cần đo dung lượng và đánh giá ảnh khôi phục bằng tiêu chí đã chọn. Nguồn: Nelson–Gailly Chương 11; CMU lossy, trang logic 2–16, đặc biệt trang 3; Bài 11.

### Sắp xếp tệp lớn theo khóa

Đĩa trao đổi dữ liệu với bộ nhớ theo khối; mỗi khối có thể chứa nhiều bản ghi. Nén giảm dung lượng nhưng chưa xác định các khối cần đọc để xử lý. Các bài toán tiếp theo áp dụng cho tệp trên đĩa, không đòi tệp nhất thiết đã nén.

Sắp xếp nhận một tệp bản ghi chưa có thứ tự và tạo tệp chứa đủ các bản ghi ấy theo khóa tăng dần. Khóa là thuộc tính xác định thứ tự. Phải giữ cả những bản ghi có khóa lặp; sắp xếp không đồng nghĩa với loại trùng.

![Các vạch biểu diễn thứ tự tương đối của khóa trước và sau sắp xếp; bộ nhớ chỉ giữ một phần tệp](img/lec-01/ung-dung-sap-xep-ngoai.svg)

Khi tệp vượt bộ nhớ, không thể sắp nó như một mảng nằm trọn trong bộ nhớ. Có thể sắp từng phần vừa bộ nhớ, rồi trộn các dãy đã có thứ tự. Chi phí cần tính cả đọc và ghi khối, không chỉ số so sánh. Nguồn: Database System Concepts, ấn bản 7 (viết tắt DSC), Chương 15, trang chiếu 17–23; Bài 12.

### Tìm hồ sơ giảng viên theo mã hoặc lương

Với bảng hồ sơ giảng viên `instructor`, truy vấn theo mã `ID` trả hồ sơ đúng mã. Truy vấn theo khoảng lương `salary` trả tất cả hồ sơ có lương trong khoảng. Phải xác định có lấy hai đầu mút hay không; hình dùng đoạn kín và không gán mức lương cụ thể.

![Tra một mã trả hồ sơ tương ứng; tra đoạn lương kín trả đủ hồ sơ có lương trong đoạn](img/lec-01/ung-dung-tra-cuu-khoa.svg)

Quét cả bảng cho mỗi yêu cầu đọc nhiều dữ liệu không thuộc kết quả. Chỉ mục phù hợp giúp chọn khối cần đọc nhưng phải được xây dựng và cập nhật khi dữ liệu thay đổi. Nếu nhiều hồ sơ cùng mức lương thỏa điều kiện, phải trả đủ. Băm và cây có thứ tự không có cùng khả năng hỗ trợ truy vấn khoảng. Nguồn: DSC Chương 14, trang chiếu 4, 6, 10–16; Bài 13.

### Tìm tài liệu chứa đồng thời hai từ khóa

Đầu vào là kho tài liệu và hai từ khóa; đầu ra là tập tài liệu chứa cả hai từ. Một tài liệu chỉ chứa một từ không thỏa điều kiện. Bài toán này chọn tập tài liệu, chưa sắp xếp theo độ liên quan.

![Hai từ khóa phải cùng xuất hiện trong mỗi tài liệu kết quả](img/lec-01/ung-dung-tim-tu-khoa.svg)

Đọc lại toàn bộ kho cho mỗi yêu cầu tốn công. Chỉ mục đảo lưu ánh xạ từ mỗi từ khóa đến danh sách tài liệu chứa nó. Giao hai danh sách cho điều kiện chứa cả hai từ; hợp cho điều kiện chứa ít nhất một từ. Nguồn: DSC Chương 31, trang 13–16 và trang chiếu 14; Bài 14.

### Tìm đối tượng giao vùng trên bản đồ

Đầu vào gồm các đối tượng hình học và vùng truy vấn $Q$. Đầu ra là các đối tượng có phần giao với $Q$, kể cả nằm hoàn toàn trong $Q$. Kiểm trực tiếp mọi hình trên bản đồ có thể tốn nhiều công.

![Q giao hộp bao A và B của hai nhóm đối tượng; cả hai nhóm cần được kiểm tiếp](img/lec-01/ung-dung-truy-van-khong-gian.svg)

Hộp bao là hình chữ nhật chứa các đối tượng của một nhóm. Trong sơ đồ, $A$ và $B$ là hộp bao, không phải các đối tượng kết quả. Vì $Q$ giao cả hai, chỉ đi một nhánh có thể bỏ sót ứng viên. Ngược lại, hộp bao giao $Q$ chưa chứng minh đối tượng thật giao $Q$. Hình không vẽ đối tượng thật nên chưa thể liệt kê kết quả cuối cùng. Nguồn: DSC Chương 24, trang chiếu 17, 21–24; Auburn, trang PDF 10–13; Bài 14.

### Ghép sinh viên với các môn đã đăng ký

Bảng `student` lưu thông tin sinh viên, còn `takes` lưu các lượt đăng ký học. Ghép theo mã sinh viên `ID` tạo thông tin sinh viên kèm từng môn đã đăng ký. Đầu ra phải gồm mọi cặp bản ghi trùng mã; một sinh viên đăng ký nhiều môn có thể tạo nhiều kết quả.

![Hồ sơ sinh viên ghép với từng lượt đăng ký cùng mã để trả sinh viên kèm môn đã đăng ký](img/lec-01/ung-dung-noi-bang.svg)

Trong nguồn, `student` có 5000 bản ghi trong 100 khối và `takes` có 10.000 bản ghi trong 400 khối. Ví dụ ở Bài 15 dùng bộ nhớ $M_{\rm khối}=20$ khối; cả hai bảng đều vượt bộ nhớ. Quét bảng đăng ký lại cho từng sinh viên sẽ đọc nhiều lần cùng dữ liệu. Các phương pháp nối cần tái sử dụng khối mà vẫn trả đủ các cặp. Nguồn: DSC Chương 15, trang chiếu 24 cho quy mô, 28 cho nối theo khối và 40 cho ví dụ bộ nhớ; kịch bản bộ nhớ của Bài 15.

Tự kiểm tra: phân biệt điều phải giữ khi lấy mẫu theo người dùng, khôi phục văn bản, lọc ứng viên vùng và trả các cặp trùng mã. Mỗi đầu ra đặt một điều kiện đúng khác nhau.

## Phân tích thuật toán xử lý dữ liệu lớn

Các bài toán trên đĩa cho thấy hai yêu cầu khác nhau: trả đúng kết quả và thực hiện được trong ngân sách tài nguyên. Tìm cặp tài liệu gần trùng còn buộc ta phân biệt một cặp được tìm thấy với toàn bộ các cặp cần tìm.

### Bài toán và cách biểu diễn

Các bản sao của một trang web thường giữ nội dung chính nhưng thay tên máy chủ hoặc liên kết. So sánh bằng nhau từng ký tự không nhận ra đủ những cặp này. Bài toán tìm gần trùng xét phần văn bản được chia sẻ; nó không kết luận hai tài liệu cùng ý nghĩa hay có hành vi sao chép trái phép.

Mỗi tài liệu được biểu diễn bằng tập các đoạn ký tự liên tiếp cùng độ dài. Cả kho dùng cùng quy tắc chuẩn hóa. Một đoạn chỉ xuất hiện một lần trong tập dù lặp nhiều lần trong văn bản. Trong phần này, các tập đã được tạo và đều không rỗng; Bài 05 phân tích cách tạo chúng.

Độ tương đồng Jaccard của hai tập hữu hạn có hợp không rỗng là

$$J(S,T)=\frac{|S\cap T|}{|S\cup T|}.$$

Tỷ lệ nằm trong $[0,1]$. Nó bằng $1$ khi hai tập không rỗng bằng nhau, bằng $0$ khi chúng rời nhau.

::: example MMDS Ví dụ 3.1
Hình 3.1 cho hai phần tử chỉ thuộc $S$, ba phần tử chung và ba phần tử chỉ thuộc $T$. Do đó

$$J(S,T)=\frac{3}{2+3+3}=\frac38.$$

Với ngưỡng $\tau$ đã cho, cặp này đạt yêu cầu khi và chỉ khi $\tau\le3/8$. Không chọn ngưỡng bằng cách nhìn riêng cặp ví dụ này.
:::

![Hai tập có ba phần tử chung trong tám phần tử của hợp.](img/lec-01/danh-gia-jaccard.svg)

Nguồn: MMDS §3.1.1–3.1.2, tr. 74–75 và §3.2.1. MMDS slide Chương 3, trang 15–17 và Stanford CS246 03-lsh, trang 14–18 thống nhất về nhu cầu biểu diễn và giảm số cặp.

### Đặc tả đầu vào và đầu ra

Đầu vào gồm số nguyên $N\ge0$, các tập hữu hạn không rỗng $C_1,\ldots,C_N$ và ngưỡng $\tau\in[0,1]$. Tập $C_i$ biểu diễn tài liệu thứ $i$. Đầu ra phải là

$$R=\{(i,j):1\le i<j\le N,\ J(C_i,C_j)\ge\tau\},$$

với mỗi cặp xuất hiện đúng một lần. Điều kiện $i<j$ loại so sánh một tài liệu với chính nó và tránh trả cả hai thứ tự của cùng cặp. Khi $N<2$, kết quả rỗng.

Chỉ trả các cặp đạt ngưỡng là chưa đủ nếu còn bỏ sót cặp khác cũng đạt ngưỡng. Nếu cho phép gần đúng, phải nêu sai lệch nào được chấp nhận. Tập rỗng nằm ngoài miền đầu vào đang xét; không tự gán giá trị cho $0/0$.

| Thành phần | Nội dung trong bài toán |
|---|---|
| Đặc tả | Trả đúng tập $R$ theo Jaccard và ngưỡng đã cho |
| Biểu diễn | Tập đoạn ký tự; có thể lưu thành danh sách đã sắp, không lặp |
| Thuật toán | Duyệt các cặp, kiểm tương đồng, xuất cặp đạt ngưỡng |
| Cài đặt | Kiểu phần tử, phép so sánh, cách đọc tệp, cách kiểm ngưỡng |
| Kết quả thực nghiệm | Các cặp cụ thể và số đo trong thiết lập chạy đã công bố |

Một lần chạy đúng không chứng minh mọi đầu vào, và một lần chạy nhanh không chứng minh một cận tiệm cận.

### Thuật toán xét mọi cặp và tính đúng

Giả sử phép kiểm Jaccard cho kết quả chính xác. Có thể duyệt hai danh sách đã sắp để đếm giao và hợp bằng hai con trỏ; Bài 05 phân tích thao tác đó.

~~~text
nếu N < 2:
    kết thúc với kết quả rỗng
cho i = 1,...,N−1:
    cho j = i+1,...,N:
        tính chính xác J(Cᵢ, Cⱼ)
        nếu J(Cᵢ, Cⱼ) ≥ τ:
            xuất cặp (i, j)
~~~

Với $N=2$, $C_1=S$, $C_2=T$ trong ví dụ, hai vòng chỉ xét $(1,2)$. Phép kiểm cho $J(C_1,C_2)=3/8$. Nếu $\tau\le3/8$, thuật toán xuất $(1,2)$ rồi dừng; nếu $\tau>3/8$, nó kết thúc với kết quả rỗng. Như vậy đầu ra là $\{(1,2)\}$ hoặc $\varnothing$ theo yêu cầu ngưỡng.

Kết quả được xuất dần, không bắt buộc lưu mọi cặp đã xét hoặc toàn bộ đầu ra trong bộ nhớ. Chi phí ghi đầu ra vẫn tồn tại.

::: proof Tính đúng và điều kiện dừng
Mệnh đề: với đầu vào hợp lệ và phép kiểm tương đồng chính xác, thuật toán xuất đúng $R$, mỗi cặp một lần.

Bất biến: sau mỗi bước, các cặp đã xuất gồm đúng các cặp đạt ngưỡng trong phần đã xét.

Ban đầu chưa xét và chưa xuất cặp nào nên bất biến đúng. Giả sử nó đúng trước một bước. Cặp mới chưa được xét trước đó. Nếu đạt ngưỡng, thuật toán xuất cặp ấy; nếu không, nó không xuất. Kết quả trước giữ nguyên nên bất biến tiếp tục đúng và không có cặp trùng lặp.

Hai vòng xét mỗi cặp $i<j$ đúng một lần rồi dừng sau $N(N-1)/2$ cặp. Khi kết thúc, phần đã xét là toàn bộ miền cặp; bất biến cho kết quả bằng $R$. Với $N<2$, miền cặp và kết quả đều rỗng.
:::

![Ba trong sáu cặp đã xét; kết quả đang có đúng với phần đã xét.](img/lec-01/danh-gia-tinh-dung.svg)

Chứng minh giả định phép kiểm ngưỡng chính xác. Cài đặt dấu phẩy động phải được kiểm tra ở gần ngưỡng; không suy từ giả mã rằng mọi cách tính số đều giữ nguyên quyết định.

::: exercise Tự kiểm đặc tả
Nếu vòng trong bắt đầu từ $j=1$ thay vì $j=i+1$, thuật toán vi phạm phần nào của đặc tả?
:::

::: solution
Nó có thể trả cặp tự so sánh $(i,i)$ và cả hai thứ tự $(i,j),(j,i)$ khi đạt ngưỡng. Chúng không thỏa điều kiện $i<j$.
:::

Nguồn bài toán và cách xét mọi cặp: MMDS Chương 3, tr. 73. Giả mã và chứng minh là cách hình thức hóa trực tiếp phép duyệt hữu hạn đó.

## Đánh giá lời giải theo từng khía cạnh

Tính đúng đã được chứng minh cho thuật toán xét mọi cặp. Tính khả thi còn phụ thuộc tài nguyên và cách phục vụ công việc.

| Nhóm | Tiêu chí | Đại lượng hoặc điều kiện |
|---|---|---|
| Kết quả | Tính đúng | Đáp ứng đặc tả trên mọi đầu vào hợp lệ |
| Kết quả | Chất lượng gần đúng | Thước đo sai lệch và điều kiện bảo đảm |
| Tài nguyên | Khối lượng tính toán | Số thao tác theo kích thước đầu vào |
| Tài nguyên | Bộ nhớ làm việc | Dung lượng lớn nhất cần giữ đồng thời |
| Tài nguyên | Đọc ghi và lượt quét | Khối chuyển giữa đĩa–bộ nhớ, số lần đọc toàn dữ liệu |
| Tài nguyên | Dữ liệu mạng | Lượng dữ liệu trao đổi giữa máy |
| Tài nguyên | Dung lượng lưu trữ | Dữ liệu đã lưu cùng phần phụ trợ |
| Vận hành | Độ trễ truy vấn | Thời gian từ nhận đến trả kết quả |
| Vận hành | Xây dựng | Thời gian, bộ nhớ để tạo cấu trúc trước truy vấn |
| Vận hành | Cập nhật | Công việc phản ánh một thay đổi dữ liệu |

Không cộng trực tiếp số phép toán, dung lượng và sai số thành một giá trị nếu chưa định nghĩa mục tiêu tối ưu.

### Khối lượng tính toán

Với $N\ge2$ tài liệu, số lần kiểm là $\binom N2=N(N-1)/2$. Với $N=10^6$, có $499\,999\,500\,000$ cặp. Đây là phép đếm, không phải số đo tốc độ. Khi số tài liệu tăng gấp đôi, số cặp tăng gần bốn lần.

Giả sử mỗi tập được lưu thành danh sách tăng dần không lặp, có không quá $L$ phần tử, và so sánh hai phần tử có chi phí đơn vị. Hai con trỏ duyệt một cặp trong $O(|C_i|+|C_j|)\subseteq O(L)$. Phần xét toàn kho có cận trên trường hợp xấu $O(N^2L)$, chưa tính tạo và sắp các tập.

![Bốn tài liệu tạo sáu cặp; số cặp tăng theo bình phương số tài liệu.](img/lec-01/ung-dung-tai-lieu-gan-trung.svg)

Coi một lần kiểm là hằng số che mất tác động của độ dài tài liệu. Giảm số cặp kiểm cũng chưa xác định toàn bộ chi phí: còn tạo ứng viên và xuất kết quả. Nếu $R$ chứa bậc hai cặp, riêng xuất đầy đủ từng cặp đã cần bậc hai thao tác. Nguồn: MMDS Chương 3, tr. 73; Stanford 03-lsh, trang 14; Bài 05.

### Bộ nhớ làm việc

Bộ nhớ làm việc là dung lượng lớn nhất phải giữ đồng thời, gồm trạng thái, dữ liệu đang dùng và bộ đệm. Nó khác kích thước toàn bộ đầu vào và đầu ra đã ghi.

Để ghép hồ sơ sinh viên với lượt đăng ký theo mã sinh viên, hai bảng chiếm 100 và 400 khối, còn ngân sách ví dụ chỉ có 20 khối bộ nhớ. Không bảng nào nạp trọn được. Xử lý từng phần phải chừa chỗ cho các bộ đệm và đầu ra.

![Hai bảng 100 và 400 khối vượt ngân sách 20 khối bộ nhớ.](img/lec-01/danh-gia-bo-nho.svg)

Nguồn quy mô: DSC Chương 15, trang chiếu 24; ngân sách 20 khối từ Bài 15. Chia phần không đổi yêu cầu trả mọi cặp trùng mã, nhưng có thể làm tăng số lần đọc lại.

### Đọc ghi và số lượt quét

Chi phí đọc ghi đếm khối chuyển giữa đĩa và bộ nhớ. Một lượt quét đọc hết dữ liệu một lần. Với tệp $F$ khối chưa có trong bộ đệm, một lượt đọc cần $F$ lần chuyển khối. Nếu cũng ghi ra $F$ khối, phần chuyển dữ liệu của lượt đó là $2F$.

Sắp ngoài tạo các dãy đã sắp rồi trộn. Các lượt trộn đọc ghi lại cùng dữ liệu; số bộ đệm giới hạn số dãy trộn đồng thời.

![Sắp ngoài đọc tệp, xử lý trong bộ đệm, ghi dãy và tiếp tục đọc ghi ở lượt trộn sau.](img/lec-01/danh-gia-doc-ghi.svg)

Hai phương pháp có số so sánh gần nhau vẫn có thể khác số khối đọc ghi. Truy cập tuần tự và ngẫu nhiên cũng có chi phí thực khác nhau; số khối chưa phải số giây. Nguồn: DSC Chương 15, trang chiếu 17–23; MMDS §1.3.4.

### Dữ liệu truyền qua mạng

Chi phí mạng ở đây đo lượng dữ liệu trao đổi giữa máy. Với đếm từ, mỗi máy đếm tại nơi giữ phần kho rồi gửi số đếm theo từ để cộng lại. Khi từ lặp nhiều, cách này có thể gửi ít dữ liệu hơn chuyển toàn bộ văn bản.

![Hai máy đếm từ w tại chỗ rồi gửi số đếm để tổng hợp toàn kho.](img/lec-01/danh-gia-truyen-mang.svg)

Đếm đúng đòi hỏi mỗi đóng góp được tính đúng một lần, kể cả khi tác vụ chạy lại. Tổng lượng truyền không tự quyết định thời gian hoàn thành: lệch tải, máy chậm và các vòng đồng bộ còn gây chờ. Lượng dữ liệu mạng chỉ đếm chuyển giữa máy, còn chi phí truyền thông trong MMDS §2.5 có thể tính cả dữ liệu vào ra của tác vụ. Nguồn: MMDS §2.2.4–2.2.6, §2.5; Stanford 01-intro, trang 67–69.

### Độ trễ truy vấn

Độ trễ là khoảng từ lúc nhận truy vấn đến lúc trả kết quả, gồm chờ, truy cập, tính toán và trả lời. Với tìm $k$ đoạn tài liệu gần véc-tơ truy vấn, chỉ đếm phép tính khoảng cách chưa mô tả đủ thời gian chờ.

![Độ trễ trải từ nhận truy vấn qua các công đoạn đến trả kết quả.](img/lec-01/danh-gia-do-tre.svg)

Thông lượng là số truy vấn hoàn tất trong một đơn vị thời gian, không phải độ trễ từng truy vấn. Khi đo cần công bố tập truy vấn, phần cứng, số luồng, tải và chất lượng. Độ rộng các công đoạn trong hình không biểu diễn số đo. Nguồn: Bài 07, mục 1; BIODS 271 và Princeton lớp 8–9.

### Chi phí xây dựng chỉ mục

Xây chỉ mục tổ chức kho thành cấu trúc phục vụ các truy vấn về sau. Cần tính thời gian và bộ nhớ lớn nhất lúc xây, không chỉ dung lượng chỉ mục hoàn tất.

![Kho véc-tơ đi qua bước xây chỉ mục; nhiều truy vấn dùng lại chỉ mục.](img/lec-01/danh-gia-xay-dung.svg)

Với tìm véc-tơ, phương pháp có thể cần tạo đồ thị hoặc học bộ mã. Báo cáo phải nói công việc nào được tính. Trả truy vấn nhanh vẫn có thể tốn nhiều thời gian chuẩn bị; lợi ích còn phụ thuộc cách dùng lại. Nguồn: Bài 07, mục 1; các trục đánh giá từ Princeton lớp 8–9.

### Chi phí cập nhật

Chi phí cập nhật gồm sửa dữ liệu và cấu trúc phụ thuộc. Khi lương của giảng viên thay đổi, phải sửa bản ghi gốc lẫn mục chỉ dẫn theo lương để truy vấn khoảng dùng giá trị mới.

![Thay đổi lương tác động tới bản ghi và chỉ mục; tra cứu cần hai cấu trúc nhất quán.](img/lec-01/danh-gia-cap-nhat.svg)

Nếu chỉ sửa bản ghi, truy vấn có thể bỏ sót mục đã chuyển vào khoảng hoặc lấy mục đã chuyển ra. Sơ đồ mô tả trạng thái sau cập nhật hoàn tất, không quy định giao thức giao dịch. Có thể đo thao tác, khối đọc ghi hay thời gian cho mỗi cập nhật; với dòng còn xét khả năng theo kịp tốc độ đến. Nguồn duy trì chỉ mục: DSC Chương 14, trang chiếu 4, 10–11 và các mục chèn/xóa. Nguồn yêu cầu theo kịp dòng: MMDS §4.1.

### Dung lượng lưu trữ

Dung lượng lưu trữ gồm dữ liệu đã lưu và phần phụ trợ. Với văn bản nén không mất thông tin, phải tính dòng mã và mọi thông tin giải mã thực sự cần lưu. Bản khôi phục phải bằng nguyên văn bản ban đầu.

![Bản lưu gồm mã và thông tin giải mã cần thiết để khôi phục đúng văn bản.](img/lec-01/danh-gia-luu-tru.svg)

Thông tin phụ tùy phương pháp: có từ điển được tái dựng, không cần lưu toàn bộ cạnh mã. Nếu có chỉ mục truy cập, phải tính cả nó. Dung lượng bản lưu khác bộ nhớ làm việc khi nén/giải nén; không phải mọi đầu vào đều nén ngắn hơn. Với ảnh cho phép mất thông tin, báo dung lượng cùng sai số tái tạo. Nguồn: Nelson–Gailly Chương 3, 8–9, 11; CMU về nén LZ; Bài 10–11.

### Chất lượng kết quả gần đúng

Với véc-tơ truy vấn $q$, gọi $N_k(q)$ là tập $k$ hàng xóm gần nhất theo khoảng cách đã chọn và quy tắc phá hòa cố định. Giả sử $1\le k\le N$ và kết quả $\widehat N_k(q)$ cũng gồm $k$ định danh phân biệt. Độ thu hồi tại $k$ là

$$\operatorname{recall@}k(q)=\frac{|\widehat N_k(q)\cap N_k(q)|}{k}.$$

::: example Ba trong năm hàng xóm thật
Tập đúng $\{a,b,c,d,e\}$ và tập trả về $\{c,d,e,f,g\}$ có ba phần tử chung. Độ thu hồi tại năm là $3/5$; hai mục $f,g$ không bù được hai hàng xóm thật $a,b$ bị thiếu.
:::

![Hai tập năm phần tử có ba phần tử chung; a,b bị thiếu, f,g nằm ngoài tập đúng.](img/lec-01/danh-gia-do-thu-hoi.svg)

Đây là ví dụ chạy tay từ Bài 07, không phải đo hiệu năng. Chất lượng đo trên tập truy vấn không tự là bảo đảm xác suất cho mọi đầu vào. Các bài toán dùng sai số khác nhau: độ thu hồi, sai số tái tạo, cận xác định hoặc cận xác suất với giả thiết tương ứng. Nguồn: Bài 07, mục 1 và hình độ thu hồi; Princeton lớp 8–9.

### Giảm ứng viên và nguy cơ bỏ sót

Một hướng giảm đối chiếu là chọn cặp ứng viên rồi tính Jaccard chính xác chỉ trên các cặp ấy. Gọi $A$ là tập ứng viên, $R$ là tập cặp đúng theo đặc tả. Sau hậu kiểm chính xác, đầu ra là

$$\widehat R=A\cap R.$$

Suy ra $\widehat R\subseteq R$: mọi cặp trả ra đều đạt ngưỡng. Muốn có $\widehat R=R$, còn cần $R\subseteq A$, tức không bỏ sót cặp đúng khi chọn ứng viên.

![Cặp được chọn đi qua kiểm tra chính xác; cặp không được chọn không xuất hiện lại ở hậu kiểm.](img/lec-01/danh-gia-ung-vien.svg)

Băm nhạy cảm cục bộ (LSH) ở Bài 06 xây cơ chế chọn ứng viên với bảo đảm xác suất dưới giả thiết cụ thể. Không gọi hậu kiểm là đầy đủ chỉ vì các phép kiểm đã thực hiện đều chính xác. Chi phí tạo ứng viên và kích thước đầu ra cũng phải được tính. Nguồn: MMDS Chương 3, tr. 73 và §3.4.

::: exercise Tự kiểm đánh giá
Bộ lọc chưa bảo đảm không bỏ sót, nhưng bước sau kiểm Jaccard chính xác cho mọi ứng viên. Có thể cam kết trả đúng tập $R$ không?
:::

::: solution
Chưa thể. Hậu kiểm loại ứng viên không đạt ngưỡng nhưng không xét cặp ngoài $A$. Cần bảo đảm $R\subseteq A$ để giữ đặc tả chính xác, hoặc công bố yêu cầu chất lượng gần đúng được chấp nhận.
:::

Các nhóm phương pháp của học phần xử lý những giới hạn này. Mỗi phương pháp phải gắn với đầu ra, điều kiện áp dụng và mô hình chi phí cụ thể.

## Nội dung học phần và phương pháp sẽ học

Các yêu cầu vừa phân tích dẫn tới năm nhóm phương pháp: xử lý phân tán, tìm tương đồng, duy trì trạng thái dòng, nén dữ liệu, tổ chức lưu trữ và truy vấn.

Học phần Giải thuật nền tảng của Khoa học dữ liệu, mã UET.DSE2053, có 3 tín chỉ. Đề cương quy định bốn chuẩn đầu ra học phần (CLO): giải thích nguyên lý và giải thuật; phân tích để lựa chọn; thiết kế, triển khai và đánh giá; tự học và xử lý dữ liệu có trách nhiệm.

![Bài 01 là nền chung cho năm nhóm bài liền nhau: phân tán và xếp hạng; tương đồng và tìm gần; dòng và cửa sổ; nén; lưu trữ và truy vấn](img/lec-01/ban-do-hoc-phan.svg)

Năm nhóm được học liền nhau theo thứ tự dưới đây. Mỗi bài gắn phương pháp với một đầu ra và các thuộc tính cần đánh giá.

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

MapReduce là mô hình xử lý; Jaccard là độ đo; chỉ mục là cấu trúc dữ liệu. Spark và Faiss là phần mềm hỗ trợ khi bài tương ứng sử dụng, có vai trò khác với các thuật toán và cấu trúc dữ liệu. IVF-PQ kết hợp chỉ mục phân vùng với mã lượng tử hóa tích.

Năm nhóm theo thứ tự học là Bài 02–04, 05–07, 08–09, 10–11 và 12–15. Tiên quyết có các nhánh: Bài 01 đến 02–03–04; đến 05–06–07; đến 08–09; đến 10–11; đến 12–13–14. Bài 12–13 hỗ trợ Bài 15; Bài 02 hỗ trợ cách tính phân tán khi cần. Nhóm sau không mặc nhiên cần toàn bộ nhóm trước.

## Kiến thức, kỹ năng và cách học

Mỗi nhóm phương pháp sử dụng một phần kiến thức nền: đồ thị cho xếp hạng, xác suất cho lấy mẫu, cây và khối dữ liệu cho chỉ mục. Việc chuẩn bị theo từng nhóm giúp xác định phần cần ôn trước khi học.

### Kiến thức đầu vào và phần cần ôn

Tiên quyết chính thức là UET.CS1058. Sinh viên cần lập trình, đọc giả mã, dùng cấu trúc dữ liệu và phân tích độ phức tạp. Nền cơ sở dữ liệu, xác suất, toán rời rạc và đại số tuyến tính được dùng theo mạch.

| Mạch | Phần nền cần huy động |
|---|---|
| Phân tán và xếp hạng | Khóa–giá trị, tính kết hợp; đồ thị, ma trận, xác suất |
| Tương đồng và hàng xóm gần | Tập hợp, băm, véc-tơ, khoảng cách, xác suất |
| Dòng và cửa sổ | Biến ngẫu nhiên, kỳ vọng, xác suất, trạng thái cập nhật |
| Nén | Phân phối ký hiệu, cây, chuỗi, từ điển; biến đổi cho ảnh |
| Lưu trữ và truy vấn | Bản ghi, khối, cây chỉ mục và phép nối quan hệ |

Không yêu cầu biết sẵn MapReduce, PageRank hoặc HNSW. Để tự đối chiếu nền chung, tính Jaccard khi giao có ba phần tử và hợp có tám phần tử, rồi giải thích phép nhân xác suất của hai biến cố độc lập. Kết quả thứ nhất là $3/8$; với độc lập, xác suất đồng thời là tích hai xác suất. Nếu chưa giải thích được, ôn tập hợp hoặc xác suất trước mạch liên quan.

### Kỹ năng cần tạo thành sản phẩm

Giải thích một phương pháp phải nêu được đặc tả, cơ chế và giả thiết. Phân tích lựa chọn phải chỉ ra tài nguyên trội và bảo đảm cần giữ. Khi thiết kế và triển khai, cần có vết chạy nhỏ, luận điểm chứng minh, trường hợp biên và bảng chi phí.

Nền thực hành gồm Python hoặc C++, đọc tài liệu chuyên ngành tiếng Anh và làm việc với giả mã. Báo cáo thử nghiệm cần ghi dữ liệu, tham số, môi trường, kết quả hiệu suất và chất lượng đầu ra để người khác kiểm tra lại. Các yêu cầu này cụ thể hóa CLO1–CLO3; không biến một kết quả đo thành định lý.

### Thái độ thể hiện trong cách làm việc

Đọc trước và ghi lại điểm chưa hiểu để tự học có mục tiêu. Khi phản biện, chỉ rõ giả thiết hoặc bước suy luận cần kiểm. Khi làm nhóm, ghi nguồn và đóng góp của từng thành viên. Báo cáo cả sai số, hạn chế và kết quả không như dự kiến.

Trách nhiệm dữ liệu gồm cách thu thập, xử lý, sử dụng và chia sẻ phù hợp quy định áp dụng. Tránh gán ý định cho con người từ một mẫu trùng trong dữ liệu.

## Mô hình ngẫu nhiên và giới hạn suy luận

Trách nhiệm khi phân tích dữ liệu còn nằm ở cách diễn giải đầu ra. Liệt kê đúng mọi mẫu trùng chưa cho biết những trùng hợp ấy có bất thường hay có thể xuất hiện ngẫu nhiên. Hồ sơ lưu trú cho phép tính cụ thể mức trùng dưới một mô hình nền.

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

## Từ lời giải một máy đến Bài 02

Với đếm từ trên kho phân tán, kết quả phải chứa đúng số lần xuất hiện của mỗi từ trong toàn kho. Đếm tại từng máy rồi gom số đếm phải bảo toàn mọi đóng góp và tránh tính trùng, kể cả khi tác vụ chạy lại. Bài 02 học cách gom theo khóa cùng chi phí truyền dữ liệu; các bài lưu trữ xét cách tổ chức ngoài bộ nhớ.

Để chuẩn bị Bài 02, đọc MMDS Chương 2; ôn ánh xạ khóa–giá trị, phép nhóm và tính kết hợp, giao hoán của phép cộng. Với tổng số nguyên không tràn, đổi cách nhóm hoặc thứ tự cộng giữ nguyên tổng nếu mỗi đóng góp được tính đúng một lần. Bất biến giúp kiểm tra điều kiện ấy.

## Bài tập từ MMDS

Hai bài từ MMDS, mục 1.2.4, trang 8 dùng lại cách đếm cặp và tính kỳ vọng của hồ sơ lưu trú: thay quy mô quan sát, thay tiêu chuẩn trùng, rồi xét tập mặt hàng. Mỗi lời giải cần nêu đơn vị đếm, giả thiết và giới hạn kết luận.

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

Số cặp người gần gấp 4, còn xác suất trùng trong hai ngày giảm đúng 4 lần. Kỳ vọng gần như không đổi; xấp xỉ của sách cho khoảng $250\,000$. Giá trị dùng tổ hợp không hoàn toàn bằng cơ sở.

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

MMDS mục 1.1 phân biệt mô hình thống kê với bản tóm tắt phục vụ truy vấn. BHK Chương 1–2 trình bày nền tảng về dữ liệu cao chiều.

- **Đề cương học phần:** nguồn xác định mã UET.DSE2053, chuẩn đầu ra, tiên quyết và thứ tự 15 bài; xem [chỉ mục học phần](index.html).
- **Mining of Massive Datasets, ấn bản 3:** Chương 1 cho chi phí và hai bài tập; Chương 2, 5, 3, 4 cho phân tán, xếp hạng, tương đồng và dòng. Nội dung và các sơ đồ tương ứng được biên soạn lại theo sách cùng slide chính thức. Ghi công tác giả tại [MMDS](http://www.mmds.org).
- **Stanford CS246:** bài mở đầu trang chiếu 62 cho tổng kích thước; 03-lsh trang 14 cho quy mô so cặp.
- **Blum–Hopcroft–Kannan, Foundations of Data Science:** Chương 1–2, đặc biệt trang PDF 9–12, cho giới hạn mô hình bộ nhớ và định hướng đọc thêm.
- **BIODS 271 và Princeton COS 597A:** các trang đã dẫn trong ứng dụng véc-tơ; tài liệu và bài báo HNSW/PQ theo Bài 07 dùng để học cơ chế chi tiết.
- **Nelson–Gailly, The Data Compression Book:** Chương 3–5, 8–9, 11; slide CMU LZ và lossy theo Bài 10–11.
- **Database System Concepts, ấn bản 7:** slide Chương 14–15, 24 và nội dung Chương 31 theo Bài 12–15. UMass CS514 Lecture 10 bổ sung Count-Min trong Bài 09.

[Quay về bộ trang chiếu](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html).
