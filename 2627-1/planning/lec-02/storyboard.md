# Storyboard Bài 2: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Hành trình khái niệm

Chuỗi chính giữ một tình huống xuyên suốt: đếm từ trong kho tài liệu lớn. Kho không vừa một máy, nên hệ tệp chia khối và đặt tác vụ gần dữ liệu. Từ đầu ra theo từ, bài chọn khóa trung gian, chạy tay Word Count, hình thức hóa ba giai đoạn, chứng minh tính đúng, rồi phân tích dữ liệu trung gian, lệch tải, lỗi và chi phí. Phần cuối đặt MapReduce vào ngăn xếp và giới hạn phạm vi áp dụng.

Mạch này dùng giáo trình và bộ trang chiếu chính thức MMDS Chương 2 cho phần cốt lõi: trang chiếu 2–11 mở động cơ và hệ tệp; 12–20 xây Word Count; 21–26 trình bày thực thi và lỗi; 27–32 trình bày độ hạt, bộ kết hợp và phân vùng; 38–40 định nghĩa chi phí I/O. Phần E so sánh hai nguồn và chọn Stanford CS246 trang 50–60, 66 cho DAG, Spark và giới hạn xử lý theo lô; MMDS 3e mục 2.4 dùng để kiểm chứng. Bài 2.2.1 và 2.3.1 tạo phần bài tập.

Theo rà dàn ý của quy trình Quill, các phụ thuộc khái niệm là:

$$
\text{giới hạn mạng}\rightarrow\text{chia khối}\rightarrow\text{khóa trung gian}\rightarrow\text{nhóm theo khóa}\rightarrow\text{tính đúng}\rightarrow\text{bộ kết hợp}\rightarrow\text{chi phí}\rightarrow\text{lựa chọn mô hình}.
$$

Không tạo `quill.json` vì đây không phải dự án sách.

Bản hiện hành có 42 trang với 42 `data-slide-id` duy nhất, đặt trong 7 mạch ngoài: mở đầu, tình huống dữ liệu lớn, luồng khóa–giá trị, giảm dữ liệu trung gian, thực thi chịu lỗi, ngăn xếp và kết luận, bài tập recitation.

## Bản đồ chu trình học tập trọng tâm

| Bước | Mã trang | Kiến thức đầu vào | Sản phẩm và dữ kiện truyền tiếp |
|---|---|---|---|
| Tình huống dữ liệu lớn | A00–A01 | Bài 1: dữ liệu không vừa bộ nhớ | Kho tài liệu phân tán; cần số lần xuất hiện theo từ; giới hạn là mạng, bộ nhớ và lỗi máy |
| Vấn đề | A02–A03 | Hệ tệp phân tán | Đầu vào là tài liệu; đầu ra $c(w)$; khóa phải gom đóng góp theo từ |
| Trực giác | B00 | Ánh xạ khóa–giá trị | map phát đóng góp, hệ thống nhóm, reduce tổng hợp |
| Ví dụ chạy tay | B01 | Hai tài liệu nhỏ | Truyền nguyên dữ kiện “dữ liệu lớn”, “lớn lớn” sang map, danh sách nhóm và tổng |
| Hình thức hóa | B05, B02 | Vết chạy B01 | Kiểu khóa, kiểu giá trị, bảo đảm nhóm, điều kiện trước và sau |
| Thuật toán và tính đúng | B04, B06 | Đặc tả B05 | Giả mã reduce, bất biến tổng tiền tố, dừng và kết luận |
| Ứng dụng và chi phí | C00–D04 | Tính đúng của phép cộng | Bộ kết hợp, phân vùng, lệch tải, $I,M,O$ và khôi phục |
| Kiểm tra | B07, C05–C06, D05, E04 | Toàn bộ chuỗi | Vết chạy mới, trạng thái trung bình, lỗi và lựa chọn tác vụ |

Không có bước `không áp dụng`. B01 dùng trường hợp nhỏ để chạy tay nhưng giữ lại đúng cấu trúc đầu ra của tình huống A00–A03. A00 dùng số liệu lịch sử của bộ trang chiếu MMDS (hơn 20 tỷ trang, 20 KB/trang, hơn 400 TB, quét 4–5 tháng) và ghi rõ không phải quy mô Web hiện tại.

## Bản đồ trang phần giảng

| Mã | Luận điểm trung tâm | Nguồn | Nối tiếp | Phút |
|---|---|---|---|---:|
| P00 | Dữ liệu và trạng thái vượt một máy dẫn đến mô hình phân tán | `source.md`; MMDS Ch.2 | Nối từ Bài 1 sang mục tiêu | 2 |
| P01 | Bốn sản phẩm học tập có thể kiểm tra | `source.md`, Bài 2 | Sang tình huống kho tài liệu | 3 |
| A00 | Kho Web hơn 400 TB làm một lượt đọc trên một máy mất khoảng 4–5 tháng | MMDS slides 4, 8, 12; MMDS 2.1, 2.2.1 | Cần lưu trữ phân tán | 2 |
| A01 | Bản sao cho phép đặt tác vụ gần dữ liệu | MMDS slides 9–11; MMDS 2.1, 2.2.5 | Cần chia trách nhiệm | 5 |
| A02 | Môi trường thực thi che chia việc, lỗi và di chuyển | MMDS slide 20; MMDS 2.2.1–2.2.6 | Người dùng chỉ định phép biến đổi | 4 |
| A03 | Đầu ra theo từ quyết định khóa trung gian | MMDS slides 12–14; MMDS 2.2.1 | Chạy tay ba giai đoạn | 4 |
| B00 | Map, nhóm khóa, reduce có ba trách nhiệm khác nhau | MMDS slides 14–16; MMDS 2.2 | Sang ví dụ | 2 |
| B01 | Vết chạy giữ nguyên đóng góp từ tài liệu đến tổng | MMDS slides 18–19; MMDS Ví dụ 2.1–2.2 | Hình thức hóa map | 5 |
| B05 | Điều kiện trước, sau và biên tách khỏi cài đặt | MMDS 2.2.1–2.2.3 | Hình thức hóa map | 4 |
| B02 | Map phát 0, 1 hoặc nhiều cặp; khóa không duy nhất | MMDS slides 17, 19; MMDS 2.2.1 | Hệ thống gom cặp | 4 |
| B03 | Nhóm theo khóa bảo đảm một khóa về một reducer | MMDS slides 16, 21, 23, 32; MMDS 2.2.2 | Reduce nhận danh sách | 4 |
| B04 | Reduce tổng hợp một khóa và dừng sau danh sách | MMDS slides 17, 19; MMDS 2.2.3 | Chốt đặc tả | 4 |
| B06 | Tính đúng theo song ánh đóng góp và bất biến tổng; mệnh đề và giả thiết trên mặt trang | Suy ra trực tiếp từ MMDS Ví dụ 2.1–2.2 | Kiểm tra vết chạy | 5 |
| B07 | Người học tự tạo toàn bộ luồng trên ví dụ mới | MMDS 2.2 | Sang chi phí dữ liệu trung gian | 3 |
| C00 | Đầu ra map là phần phải truyền | MMDS slides 30–31; MMDS 2.2.4 | Dùng bộ kết hợp | 2 |
| C01 | Bộ kết hợp thay nhiều đóng góp cục bộ bằng một tổng | MMDS slides 30–31; MMDS 2.2.4 | Điều kiện an toàn | 5 |
| C02 | Phép gộp cần kết hợp, giao hoán, đóng và giữ cùng ngữ nghĩa | MMDS slide 30; MMDS 2.2.4 | Sang phân vùng | 5 |
| C03 | $h$, $r$ và $p(k)$ xác định Reduce task nhận khóa | MMDS slides 25, 27, 32; MMDS 2.2.2, 2.2.5 | Độ dài danh sách gây lệch | 4 |
| C04 | Reducer, Reduce task và máy công nhân là ba cấp khác nhau | MMDS khung trang in 28 | Sang hai cơ chế phân tải | 5 |
| C05 | Gộp reducer trong task khác với lập lịch task lên máy; câu hỏi phân biệt hai cơ chế | MMDS trang in 28–29 | Kiểm tra hai cơ chế | 3 |
| C06 | Người học tự tìm trạng thái cho phép tính trung bình; notes chỉ gợi ý tiêu chí | MMDS 2.2.4; liên hệ Bài 2.3.1(b) | Sang thực thi chịu lỗi | 3 |
| D00 | Chạy lại tác vụ cần kết quả phụ thuộc đầu vào; ví dụ hiệu ứng ngoài làm chạy lại sai | MMDS 2.2.5–2.2.6 | Theo dõi trạng thái | 2 |
| D01 | Bộ điều phối theo dõi và cấp lại tác vụ | MMDS slides 23–25; MMDS 2.2.5 | Phân biệt lỗi map/reduce | 5 |
| D02 | Tệp trung gian cục bộ làm lỗi map khác lỗi reduce | MMDS slides 24–26; MMDS 2.2.6 | Chi phí của dữ liệu truyền | 4 |
| D03 | Hai quy ước đo hai đại lượng khác nhau: $I+M$ và $I+2M+O$ | MMDS slides 38–40; MMDS 2.5.1 | Xác định tác động của bộ kết hợp | 5 |
| D04 | Bộ kết hợp có thể giảm kích thước dữ liệu trung gian $M$ | MMDS 2.2.4, 2.5.1 | Kiểm tra với lỗi | 4 |
| D05 | Thực thi lại làm phát sinh I/O ngoài mô hình lý tưởng; cầu nối sang ngăn xếp | MMDS 2.2.6 | Sang ngăn xếp | 3 |
| E00 | MapReduce là một tầng thực thi | MMDS 2.4; Stanford 50–53 | Mở các tầng ngăn xếp | 2 |
| E01 | HDFS, Hadoop MapReduce và Spark giữ các vai trò cụ thể; sơ đồ là tổng hợp MMDS + Stanford | MMDS 2.4; Stanford 51–59 | Chọn phạm vi phù hợp | 5 |
| E02 | MapReduce phù hợp quét tuần tự theo lô; vòng lặp phải ghi/đọc trung gian | MMDS slides 9, 12–14; MMDS 30–31; Stanford 50, 66 | Đúc thành khuôn đặc tả | 4 |
| E03 | Năm bước đặc tả nối tính đúng với chi phí; bước 5 yêu cầu nêu quy ước chi phí | Tổng hợp nguồn đã dùng | Kiểm tra lựa chọn | 4 |
| E04 | Kết luận thu hồi A00, tóm tuyến và chỉ khi chuyển sang DAG/Spark | MMDS slides 12, 34–35; Stanford 50, 66 | Kết phần giảng, nối recitation | 4 |
| **Tổng** |  |  |  | **120** |

Sau mỗi phần, trang đầu phần kế tiếp nhắc đúng sản phẩm vừa tạo: A03 truyền khóa sang B00; B05 truyền điều kiện trước và sau sang B02; B06 truyền điều kiện đúng sang C00; C01–C06 truyền $M$ sang D03; D03 truyền mô hình chi phí sang E02; D05 truyền giới hạn chuỗi job sang E00; E03 truyền mẫu đặc tả sang E04 và recitation R05–R08.

## Bản đồ trang phần bài tập

| Mã | Nội dung và điều chỉnh | Nguồn | Lời giải trong ghi chú | Phút |
|---|---|---|---|---:|
| R00 | Trang chuyển phần; không thêm yêu cầu | MMDS 2.2.1, 2.3.1 | Có hướng dẫn tổ chức | 0 |
| R01 | Dịch sát phần dẫn Bài 2.2.1, không thêm yêu cầu; giao việc ba ý | Bài 2.2.1, trang in 30, PDF 11 | Hướng dẫn tổ chức trong ghi chú | 4 |
| R02 | Dịch sát ý (a), không thêm sản phẩm | Bài 2.2.1(a), trang in 30, PDF 11 | Có đáp án và thang 4 điểm | 8 |
| R03 | Dịch sát ý (b), giữ 10 và 10.000 task | Bài 2.2.1(b), trang in 30, PDF 11 | Có đáp án và thang 6 điểm | 11 |
| R04 | Dịch sát ý (c), giữ 100 Map task | Bài 2.2.1(c), trang in 30, PDF 11 | Có đáp án và thang 5 điểm | 9 |
| R05 | Dịch sát phần dẫn Bài 2.3.1, không thêm định dạng sản phẩm | Bài 2.3.1, trang in 40, PDF 21 | Chuyển bài | 0 |
| lec02-r06a | Dịch sát ý (a), không thêm yêu cầu bộ kết hợp | Bài 2.3.1(a), trang in 40, PDF 21 | Có đáp án và thang 3 điểm; biên tệp rỗng trong ghi chú | 6 |
| lec02-r06b | Dịch sát ý (b), không thêm yêu cầu bộ kết hợp | Bài 2.3.1(b), trang in 40, PDF 21 | Có đáp án và thang 4 điểm; biên tệp rỗng trong ghi chú | 8 |
| R07 | Dịch sát ý (c), không thêm sản phẩm | Bài 2.3.1(c), trang in 40, PDF 21 | Có đáp án và thang 4 điểm; ghi rõ reducer nhận $x$ từ khóa; đầu ra $(khóa\ không\ dùng,x)$ | 6 |
| R08 | Dịch sát ý (d), không thêm sản phẩm | Bài 2.3.1(d), trang in 40, PDF 21 | Có đáp án và thang 5 điểm | 8 |
| **Tổng** |  |  |  | **60** |

Hai ý 2.3.1(a–b) được tách thành hai trang dọc lec02-r06a và lec02-r06b vì mỗi ý là một bài toán thiết kế độc lập; lời giải vẫn tách rõ theo ý. Các nhãn "Sản phẩm" đã được bỏ khỏi R01–R08 để mặt trang chỉ giữ nguyên yêu cầu toán học của MMDS. Hướng dẫn chấm chỉ nằm trong ghi chú diễn giả.

## Sai khác có chủ ý so với nguồn

- Tách MapReduce khỏi PageRank theo `sources/source.md`; bỏ toàn bộ PageRank, phép nối và nhân ma trận–vector.
- Gộp sơ đồ hệ tệp và vị trí dữ liệu thành SVG A01; khối khoảng 64 MB và ba bản sao chỉ nêu trong ghi chú A01 theo số liệu lịch sử MMDS, không đưa lên mặt trang.
- Đổi thứ tự phần B thành B00, B01, B05, B02, B03, B04, B06, B07: đặc tả điều kiện trước và sau đi trước để B02 hình thức hóa phía map trên nền đặc tả; `data-slide-id` giữ ổn định.
- B06 viết mệnh đề và chứng minh từ cơ chế Word Count trong MMDS Ví dụ 2.1–2.2 để đáp ứng chuẩn lập luận đúng; đây là phần hình thức hóa do người soạn triển khai, không phải định lý mới của nguồn.
- D00 bổ sung điều kiện đầu ra chỉ phụ thuộc đầu vào và không tạo hiệu ứng ngoài không kiểm soát để giải thích khi nào chạy lại tác vụ là an toàn; nguồn MMDS cung cấp cơ chế lập lịch lại.
- E03 là khuôn đặc tả tổng hợp từ các bước đã dùng trong bài, không phải thuật toán hoặc API mới của nguồn.
- Dùng hai tài liệu nhỏ ở B01 để chạy tay đúng cơ chế Ví dụ 2.1–2.2; chuỗi tiếng Việt chỉ là dữ liệu minh họa, không phải số liệu thực nghiệm.
- Đặt MMDS 2.5.1 cạnh bộ trang chiếu chính thức MMDS 38–40 để chỉ rõ hai quy ước, thay vì chọn một và làm mất truy nguyên.
- Phần Spark chỉ định vị trong ngăn xếp; không dạy RDD, DataFrame hoặc API.
- Phần recitation chỉ dùng Bài 2.2.1 và 2.3.1; không dùng Bài 2.5.1.
