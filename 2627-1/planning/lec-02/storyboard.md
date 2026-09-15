# Storyboard Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Phạm vi hiện hành — 2026-09-15, bổ sung tổ chức thực thi và phục hồi

Áp dụng [slide_authoring_standard.md](../../../slide_authoring_standard.md) và [AGENTS.md](../../../AGENTS.md). Sinh viên năm 2 đã học lập trình và nhân ma trận–vector, chưa học CSDL. Nguồn chính: [MMDS Chương 2](../../../sources/textbooks/ch2n.pdf), trang in 20–79; trang PDF bằng trang in trừ 19. Giữ 9 section: mở đầu và mỗi mục 2.1–2.8 một section theo yêu cầu người dùng, ngoại lệ quy tắc 5–7 section.

Bản hiện hành có **50 trang giảng và 8 trang bài tập**, thiết kế **120 phút giảng + 60 phút recitation**. Phân bổ dự kiến, chưa diễn tập với lớp thật. Bỏ quan hệ, chọn, chiếu, nối, tổng hợp và liên hệ nhân hai ma trận (2.3.3–2.3.10), các ví dụ chi phí nối của 2.5.3 và bài 2.5.1(c) theo chỉ dẫn mới về tiên quyết. Không giữ phép nối ngầm trong bài tập hoặc phần kết. Thời gian chuyển sang giải thích hai hàm, vết chạy và đếm chi phí; không thêm số liệu ngoài nguồn.

Recitation: 2.2.1(a–c), trang 30/PDF 11: 15 phút; 2.3.1(a–d), trang 40/PDF 21: 20 phút; 2.5.1(a), trang 59/PDF 40: 25 phút. Giữ nguyên đề nguồn, chỉ dịch và tách ý. Bỏ bài 2.5.1(c), dành trọn 25 phút cho lập bảng, trình bày và đối chiếu điều kiện của ý (a); không thêm bài mới. Bài tập nằm cuối section nguồn, ngoại lệ để giữ ánh xạ PDF; liên kết từ tổng kết dẫn vào recitation sau phần giảng.

## Hành trình khái niệm

| Mục | Mạch viết và sản phẩm chuyển tiếp | Phút giảng |
|---|---|---:|
| Mở đầu | Giới hạn một máy → mục tiêu và nội dung. | 5 |
| 2.1 | Cụm máy → lỗi → khối và bản sao → đầu vào tác vụ. | 8 |
| 2.2 | Lợi ích → đếm từ → hai hàm → giả mã/đúng → tạo tác vụ → phân khóa → gán máy → dữ liệu còn lại → phục hồi lỗi. | 38 |
| 2.3 | Đổi khóa từ từ sang hàng → vết các tích → giả mã → chia dải vector. | 20 |
| 2.4 | Một công việc → đồ thị phụ thuộc → Spark/tính lại → nhiều tác vụ cần đánh giá. | 10 |
| 2.5 | Mô hình/đơn vị → đếm từ → đọc dải vector → tổng và tải lớn nhất. | 15 |
| 2.6 | Giới hạn tác vụ → đặc tả ảnh → từng cặp → nhóm ảnh → đúng và bộ nhớ. | 18 |
| 2.7 | Thu hồi các lớp lập luận → bốn sản phẩm tự kiểm tra. | 5 |
| 2.8 | Nguồn/hướng đọc → bài tập từ giáo trình. | 1 |

## Chu trình và nguồn

- Đếm từ: s02-01 đặt vấn đề; 02/03 chạy vết; 03a hình thức hóa; 03b nối hai hàm bằng sơ đồ; 04 giả mã; 03c đặc tả đầu ra; 04a tính đúng; 04b đếm thao tác; 05 gộp; 06–06c tạo và phân công tác vụ; 07–07b lưu trữ và phục hồi. D1 “dữ liệu lớn”, D2 “lớn lớn” là ví dụ Việt hóa đã có, minh họa Ví dụ 2.1–2.2, trang 25–27. Số 1 biểu diễn từng lần xuất hiện; không loại lặp. Hình dựa Hình 2.2, không đồng nhất mỗi hàm với một máy. Kiểm tra ở 02/06 và tổng kết; chi phí dùng lại cùng 5 cặp ở s05-03.
- Ma trận–vector: s03-01 đặc tả từ tiên quyết; 02 vết ký hiệu; 02a giả mã, giả thiết và đúng; 03 chia dải (Hình 2.4); 03a đánh giá phép tính và bộ nhớ. Không tự đặt ma trận số ngoài nguồn. 2.5 quay lại dữ liệu này: mỗi phần tử đọc một lần, mỗi tác vụ đọc dải vector cần dùng. s05-03a định nghĩa đơn vị/kích thước và đếm; 03b cộng rồi xét trường hợp. Bài 2.5.1(a) yêu cầu giải thích mỗi số hạng và điều kiện. Số học chính xác; hàng không lưu hiểu bằng 0.
- Cặp ảnh: s06-00 đặc tả theo 2.6.2; 01 định nghĩa q/rho; 02 từng cặp; 03 từng nhóm; 03a bao phủ cặp chéo/nội bộ; 03b đếm so sánh; 04 kiểm tra bộ nhớ. Giữ dữ kiện nguồn một triệu ảnh, một triệu byte mỗi ảnh và 1000 nhóm đều; không giảm số so sánh. Không cần phép nối quan hệ để theo dõi phân công ảnh.
- Hệ thống và Spark dùng hình cơ chế/phụ thuộc; không tạo chứng minh hay giả mã ngoài nguồn. MMDS và Stanford đã được kiểm kê; sách quyết định mạch, ví dụ và chi phí. Giữ cách thể hiện một bước suy luận mỗi trang, ví dụ trước ký hiệu đã tham khảo math-4-AI 01–03.
- 13 SVG được dùng, gồm năm hình mới về tạo Map, phân khóa, phân bổ máy, phục hồi Map và phục hồi Reduce. Hình khóa–tác vụ cũ không còn nhúng; các tài sản cũ giữ để truy nguyên. Mỗi hình mới có script tái sinh, mô tả và mũi tên; không dùng màu làm tín hiệu duy nhất.

Các ID giữ ổn định từ bản trước; thứ tự trình bày do DOM quyết định, không sắp xếp ID. Khoảng trống ID là các slide đã bỏ, không phải bài tập bị thiếu.


### Cụm thực thi và phục hồi mở rộng

Từ hai hàm đã học, 06 khôi phục các cấp thực thi; 06a chia dữ liệu cho Map; 06b dùng cùng h phân khóa cho Reduce; 06c bộ điều phối gán các tác vụ cho tiến trình trên máy. Sau đó 07 xác định nơi lưu ba loại dữ liệu; 07a theo dõi lỗi máy Map; 07b theo dõi lỗi máy Reduce và giới hạn máy bộ điều phối. Đây là cơ chế hệ thống, không tạo thuật toán hay chứng minh ngoài nguồn. Các câu hỏi ở 07a/07b kiểm tra đúng phạm vi phải tính lại; bài 2.2.1 dùng lại khái niệm khóa/tác vụ/máy để giải thích lệch tải.

D1 thuộc phần 0, D2 thuộc phần 1 chỉ là minh họa. Map 0/1 ban đầu ở A/B; R0/R1 ở C/D. h(dữ)=h(liệu)=0, h(lớn)=1; hai Map tạo bốn tệp, một rỗng. Tình huống lỗi độc lập: A hỏng → E chạy lại Map 0, báo tệp thay thế; D hỏng khi R1 đang chạy → F chạy lại R1, R0 đã xong giữ nguyên. Không khẳng định hình phân công là trạng thái đồng thời. Không đồng nhất hàm băm với bộ lập lịch; không dùng số máy minh họa làm quy mô hệ thống.

## Đặc tả từng trang

### `lec02-s00-01` · MapReduce và ngăn xếp xử lý dữ liệu lớn

- **Kiến thức đầu vào:** Giới hạn một máy ở bài 1.
- **Mục đích:** Xác định bài toán phân chia tính toán của bài 2.
- **Câu chốt:** Chọn khóa và phân chia dữ liệu là cơ sở thiết kế phép tính trên nhiều máy.
- **Kết nối vào–ra:** từ “Giới hạn một máy ở Bài 1”; chuẩn bị “Nội dung bài giảng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Phần dẫn chương, trang in 21–22; sources/source.md, Bài 2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s00-02` · Nội dung bài giảng

- **Kiến thức đầu vào:** Tên bài.
- **Mục đích:** Theo dõi thứ tự tám mục nguồn của bài.
- **Câu chốt:** Mạch bài đi từ lưu trữ và thực thi đến thuật toán, chi phí và đánh đổi bộ nhớ.
- **Kết nối vào–ra:** từ “MapReduce và ngăn xếp xử lý dữ liệu lớn”; chuẩn bị “Mục tiêu học tập”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, các mục 2.1–2.8.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s00-03` · Mục tiêu học tập

- **Kiến thức đầu vào:** Mục lục bài.
- **Mục đích:** Nêu bốn sản phẩm học tập cần đạt.
- **Câu chốt:** Kết quả học tập gồm vết chạy, giả mã, bảng chi phí và giải thích đánh đổi.
- **Kết nối vào–ra:** từ “Nội dung bài giảng”; chuẩn bị “2.1 · Cụm máy và mạng kết nối”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, sources/source.md, Bài 2; Chương 2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-03).
- **Thời lượng:** 1 phút giảng.

### `lec02-s01-01` · 2.1 · Cụm máy và mạng kết nối

- **Kiến thức đầu vào:** Dữ liệu vượt một máy.
- **Mục đích:** Phân biệt máy, tủ máy và mạng giữa các tủ.
- **Câu chốt:** Dữ liệu giữa hai tủ phải đi qua mạng liên tủ.
- **Kết nối vào–ra:** từ “Mục tiêu học tập”; chuẩn bị “Lỗi máy và lỗi kết nối”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-01).
- **Thời lượng:** 3 phút giảng.

### `lec02-s01-02` · Lỗi máy và lỗi kết nối

- **Kiến thức đầu vào:** Cấu trúc cụm máy.
- **Mục đích:** Phân biệt hậu quả lỗi máy và lỗi cả tủ.
- **Câu chốt:** Lỗi máy và lỗi mạng cả tủ có phạm vi ảnh hưởng khác nhau.
- **Kết nối vào–ra:** từ “2.1 · Cụm máy và mạng kết nối”; chuẩn bị “Chia khối, lưu bản sao và đọc gần dữ liệu”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s01-03` · Chia khối, lưu bản sao và đọc gần dữ liệu

- **Kiến thức đầu vào:** Lỗi máy và tủ.
- **Mục đích:** Xác định bản sao còn đọc được khi máy hỏng.
- **Câu chốt:** Bản sao chỉ giúp phục hồi khi còn ít nhất một bản sao truy cập được.
- **Kết nối vào–ra:** từ “Lỗi máy và lỗi kết nối”; chuẩn bị “2.2 · Mô hình MapReduce”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-03).
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-01` · 2.2 · Mô hình MapReduce

- **Kiến thức đầu vào:** Dữ liệu đã chia thành khối.
- **Mục đích:** Đặc tả đầu vào và đầu ra của đếm từ.
- **Câu chốt:** Map phát đóng góp; hệ thống nhóm theo khóa; reduce tổng hợp từng nhóm.
- **Kết nối vào–ra:** từ “Chia khối, lưu bản sao và đọc gần dữ liệu”; chuẩn bị “Lợi ích của MapReduce”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, Ví dụ 2.1–2.2, trang in 25–27.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-01).
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-01a` · Lợi ích của MapReduce

- **Kiến thức đầu vào:** Giới hạn một máy, cụm máy và hai hàm vừa được giới thiệu.
- **Mục đích:** Ghép năm lợi ích với cơ chế hệ thống tạo ra chúng.
- **Câu chốt:** Lập trình viên mô tả phép tính; hệ thống tổ chức việc thực thi.
- **Kết nối vào–ra:** từ kho tài liệu lớn ở s02-01; tạo động lực theo dõi D1/D2 ở s02-02 và các cơ chế phân công, phục hồi phía sau.
- **Cách thể hiện:** Một bảng năm hàng, hai cột lợi ích/cơ chế; không thêm sơ đồ trang trí. Các giới hạn và câu nối nằm trong notes.
- **Nguồn:** MMDS Chương 2, trang 21–22, 25–30; slide MMDS trang 24–25. Dean và Ghemawat (2004), tóm tắt và mục 3.4, dùng để đối chiếu. Năm ý do người dùng cung cấp; năm video YouTube không truy cập được nên không trích lời hoặc coi là đã xem.
- **Ghi chú:** [Giải thích điều kiện và nối mạch](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-01a).
- **Thời lượng:** 1 phút giảng.

### `lec02-s02-02` · Mỗi lần xuất hiện tạo một đóng góp

- **Kiến thức đầu vào:** Đặc tả đếm từ; tách theo khoảng trắng.
- **Mục đích:** Phát đủ năm đóng góp từ hai tài liệu.
- **Câu chốt:** Năm lần xuất hiện tạo năm cặp, kể cả các cặp trùng nhau.
- **Kết nối vào–ra:** từ “Lợi ích của MapReduce”; chuẩn bị “Nhóm theo khóa rồi cộng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.1, trang in 26; dữ liệu minh họa tiếng Việt được ghi trong storyboard.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-02).
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-03` · Nhóm theo khóa rồi cộng

- **Kiến thức đầu vào:** Năm cặp đã phát.
- **Mục đích:** Tính tổng cho từng khóa và giữ các lần xuất hiện trùng.
- **Câu chốt:** Ba đóng góp của từ “lớn” về cùng khóa và được cộng thành 3.
- **Kết nối vào–ra:** từ “Mỗi lần xuất hiện tạo một đóng góp”; chuẩn bị “Hai hàm của MapReduce”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.2–2.2.3, Ví dụ 2.2, trang in 26–27.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03).
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-03a` · Hai hàm của MapReduce

- **Kiến thức đầu vào:** Khóa–giá trị, vết đếm từ và ký hiệu hàm.
- **Mục đích:** Đọc miền vào–ra của Map và Reduce, phân biệt ba tầng kiểu dữ liệu.
- **Câu chốt:** Map và Reduce được nối bằng bước hệ thống nhóm theo khóa.
- **Kết nối vào–ra:** Từ “Nhóm theo khóa rồi cộng”; cung cấp kết quả cho “Từ Map đến Reduce”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS 2.2.1–2.2.3, tr. 25–27. Trong ví dụ, K_1 là mã tài liệu, V_1 là nội dung; Map bỏ mã tài liệu. K_2 và K_3 là từ; V_2 và V_3 là số nguyên. Cách viết map(tài_liệu) ở trang sau lược khóa đầu vào như sách. Chữ ký mô tả kiểu dữ liệu; luật xử lý cụ thể nằm trong giả mã.
    Reduce được gọi đúng một lần cho mỗi khóa có mặt ở dữ liệu trung gian.
    Không dựa vào thứ tự tài liệu ban đầu khi cộng các giá trị; phép cộng trong ví dụ không phụ thuộc thứ tự. Khóa đầu ra K_3 có thể khác K_2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-03b` · Từ Map đến Reduce

- **Kiến thức đầu vào:** Chữ ký hai hàm, năm cặp D1/D2 và ba khóa.
- **Mục đích:** Theo dõi đủ năm đóng góp từ hai tài liệu tới ba kết quả.
- **Câu chốt:** Nhóm theo khóa giữ đủ mọi lần xuất hiện trước khi Reduce cộng.
- **Kết nối vào–ra:** Từ “Hai hàm của MapReduce”; cung cấp kết quả cho “Đặc tả bài toán đếm từ”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** Figure 2.2 (MMDS), áp dụng cho D1, D2 đã có. D1 = "dữ liệu lớn" phát
    (dữ,1), (liệu,1), (lớn,1); D2 = "lớn lớn" phát hai cặp (lớn,1). Ba nhóm:
    dữ [1], liệu [1], lớn [1,1,1]. Nhãn vai trò: Người viết: Map/Reduce;
    Hệ thống: nhóm khóa.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03b).
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-03c` · Đặc tả bài toán đếm từ

- **Kiến thức đầu vào:** Vết D1/D2 và giao diện hai hàm.
- **Mục đích:** Phân biệt đếm lần xuất hiện với đếm tài liệu.
- **Câu chốt:** Mỗi từ xuất hiện có đúng một cặp kết quả với số đếm của nó.
- **Kết nối vào–ra:** Từ “Từ Map đến Reduce”; cung cấp kết quả cho “Thuật toán đếm từ”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Ba hàng đầu vào, đầu ra, điều kiện; đối chiếu T=5 và f(lớn)=3.
- **Nguồn:** MMDS Chương 2, 2.2.1–2.2.3, trang 25–27.
- **Ghi chú:** [Giả thiết, phân tích và giới hạn](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03c).
- **Thời lượng:** 2 phút giảng.


### `lec02-s02-04` · Thuật toán đếm từ

- **Kiến thức đầu vào:** Vết nhóm theo khóa.
- **Mục đích:** Viết lại hai hàm đếm từ với giả thiết rõ.
- **Câu chốt:** Map phát một số 1 mỗi lần xuất hiện; reduce cộng mọi giá trị của từ.
- **Kết nối vào–ra:** Từ “Đặc tả bài toán đếm từ”; cung cấp kết quả cho “Bộ đếm trả đúng số lần xuất hiện”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, trang in 25–27; lập luận đúng từ Ví dụ 2.1–2.2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-04).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-04a` · Bộ đếm trả đúng số lần xuất hiện

- **Kiến thức đầu vào:** Giả mã và trạng thái s.
- **Mục đích:** Chứng minh bộ đếm đúng bằng bất biến cộng tổng.
- **Câu chốt:** Sau mỗi lần cộng, bộ đếm bằng tổng các giá trị đã đọc.
- **Kết nối vào–ra:** Từ “Thuật toán đếm từ”; cung cấp kết quả cho “Đếm thao tác của thuật toán đếm từ”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, trang in 25–27; diễn giải tính đúng của Ví dụ 2.1–2.2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-04a).
- **Thời lượng:** 1 phút giảng.

### `lec02-s02-04b` · Đếm thao tác của thuật toán đếm từ

- **Kiến thức đầu vào:** Giả mã cộng từ 0 và chứng minh đếm từ.
- **Mục đích:** Đếm số cặp phát và phép cộng từ vòng lặp.
- **Câu chốt:** T lần xuất hiện tạo T cặp và T phép cộng khi chưa gộp.
- **Kết nối vào–ra:** Từ “Bộ đếm trả đúng số lần xuất hiện”; cung cấp kết quả cho “Gộp cục bộ trước khi truyền”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng bước–số lượng, dùng lại 5 cặp; một biến tổng ngoài vùng hệ thống.
- **Nguồn:** MMDS Chương 2, 2.2.1–2.2.3, trang 25–27; phép đếm suy ra từ giả mã.
- **Ghi chú:** [Giả thiết, phân tích và giới hạn](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-04b).
- **Thời lượng:** 2 phút giảng.


### `lec02-s02-05` · Gộp cục bộ trước khi truyền

- **Kiến thức đầu vào:** Bất biến bộ đếm.
- **Mục đích:** Giải thích gộp cục bộ giữ nguyên tổng.
- **Câu chốt:** Gộp cục bộ giảm số cặp gửi mà giữ nguyên ý nghĩa tổng đếm.
- **Kết nối vào–ra:** Từ “Đếm thao tác của thuật toán đếm từ”; cung cấp kết quả cho “Khóa, tác vụ và máy”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.4, trang in 27–28.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-05).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-06` · Khóa, tác vụ và máy

- **Kiến thức đầu vào:** Khóa–giá trị, hai hàm Map/Reduce.
- **Mục đích:** Phân biệt hàm, lần gọi theo khóa, tác vụ, tiến trình và máy.
- **Câu chốt:** Tác vụ là phần công việc; Worker và máy là nơi thực hiện.
- **Kết nối vào–ra:** Từ “Gộp cục bộ trước khi truyền”; cung cấp kết quả cho “Tạo tác vụ Map từ dữ liệu đầu vào”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng bốn vai trò, phân biệt số khóa với số tác vụ.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-06).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-06a` · Tạo tác vụ Map từ dữ liệu đầu vào

- **Kiến thức đầu vào:** Phần dữ liệu và các cấp thực thi.
- **Mục đích:** Giải thích cùng hàm Map chạy trên các phần đầu vào khác nhau.
- **Câu chốt:** Một phần đầu vào có thể chứa nhiều phần tử; một tác vụ gọi Map nhiều lần.
- **Kết nối vào–ra:** từ “Khóa, tác vụ và máy”; chuẩn bị “Phân chia khóa cho các tác vụ Reduce”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Sơ đồ hai phần D1/D2 tới Map 0/1, chưa gán máy.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-06a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-06b` · Phân chia khóa cho các tác vụ Reduce

- **Kiến thức đầu vào:** Hai Map và ba khóa của D1/D2.
- **Mục đích:** Theo dõi tệp trung gian từ mọi Map tới đúng tác vụ Reduce.
- **Câu chốt:** Hàm h chọn tác vụ, không chọn máy; một tác vụ nhận nhiều khóa.
- **Kết nối vào–ra:** từ “Tạo tác vụ Map từ dữ liệu đầu vào”; chuẩn bị “Bộ điều phối phân bổ tác vụ lên máy”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG hai Map trên A/B, bốn tệp (một rỗng), hai đích R0/R1.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-06b).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-06c` · Bộ điều phối phân bổ tác vụ lên máy

- **Kiến thức đầu vào:** Tác vụ đã được tạo và khóa đã phân chia.
- **Mục đích:** Giải thích bộ điều phối giao tác vụ cho Worker rảnh và theo dõi trạng thái.
- **Câu chốt:** Nhiều tác vụ có thể lần lượt chạy trên cùng máy.
- **Kết nối vào–ra:** từ “Phân chia khóa cho các tác vụ Reduce”; chuẩn bị “Lưu trữ quyết định phần cần chạy lại”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Sơ đồ Hình 2.3 vẽ lại: bộ điều phối, Worker trên A–D; mũi tên phân công, không phải dữ liệu.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-06c).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-07` · Lưu trữ quyết định phần cần chạy lại

- **Kiến thức đầu vào:** Phân công tác vụ, tệp cục bộ và hệ tệp phân tán.
- **Mục đích:** Xác định dữ liệu còn lại sau lỗi để suy ra phần phải chạy lại.
- **Câu chốt:** Nơi lưu dữ liệu quyết định tính lại phần nào.
- **Kết nối vào–ra:** từ “Bộ điều phối phân bổ tác vụ lên máy”; chuẩn bị “Phục hồi khi máy Map hỏng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng ba loại dữ liệu/nơi lưu; kiểm tra Worker định kỳ.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-07).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-07a` · Phục hồi khi máy Map hỏng

- **Kiến thức đầu vào:** Tệp Map cục bộ có thể mất khi máy hỏng.
- **Mục đích:** Mô phỏng phát hiện, đưa về chờ, giao lại Map và báo vị trí tệp mới.
- **Câu chốt:** Map đã xong vẫn phải tính lại nếu đầu ra cục bộ mất.
- **Kết nối vào–ra:** từ “Lưu trữ quyết định phần cần chạy lại”; chuẩn bị “Phục hồi khi máy Reduce hỏng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG bốn bước: máy A mất phản hồi → Map 0 chờ → E đọc D1 → tệp mới cho Reduce; B giữ Map 1.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-07a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-07b` · Phục hồi khi máy Reduce hỏng

- **Kiến thức đầu vào:** Trung gian Map còn, kết quả Reduce hoàn thành nằm trên hệ tệp phân tán.
- **Mục đích:** Mô phỏng chạy lại Reduce đang thực hiện, giữ kết quả đã hoàn tất.
- **Câu chốt:** Reduce đang chạy được giao lại; Reduce đã xong không cần tính lại trong tình huống này.
- **Kết nối vào–ra:** từ “Phục hồi khi máy Map hỏng”; chuẩn bị “2.3 · Nhân ma trận–vector”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG D hỏng → Reduce 1 chờ → F đọc lại Map → ghi kết quả; Reduce 0 giữ nguyên. Máy bộ điều phối hỏng: khởi động lại toàn bộ công việc theo mô hình MMDS.
- **Nguồn:** MMDS 2.2.1–2.2.6, trang 25–30; khung trang 28, Hình 2.3. Các tên máy và phân công D1/D2 là minh họa cơ chế, không là dữ kiện nguyên văn sách.
- **Ghi chú:** [Cơ chế, giả thiết, đáp án và nguồn chi tiết](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-07b).
- **Thời lượng:** 2 phút giảng.

### `lec02-ex221a` · Bài tập 2.2.1(a) · Lệch tải khi chưa gộp

- **Kiến thức đầu vào:** Reducer theo khóa.
- **Mục đích:** Giải thích lệch tải khi danh sách từ có độ dài khác nhau.
- **Câu chốt:** Tần suất từ khác nhau làm độ dài danh sách của các reducer khác nhau.
- **Kết nối vào–ra:** từ “Lưu trữ quyết định phần cần chạy lại”; tạo cơ sở cho “Bài tập 2.2.1(b) · Gom reducer vào tác vụ”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(a), trang in 30 / PDF 11.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex221a).
- **Thời lượng:** 5 phút recitation.

### `lec02-ex221b` · Bài tập 2.2.1(b) · Gom reducer vào tác vụ

- **Kiến thức đầu vào:** Phân biệt reducer và task.
- **Mục đích:** So sánh gom reducer vào 10 và 10000 tác vụ.
- **Câu chốt:** Gom nhiều khóa vào một tác vụ có thể làm tải giữa các tác vụ đều hơn.
- **Kết nối vào–ra:** từ “Bài tập 2.2.1(a) · Lệch tải khi chưa gộp”; tạo cơ sở cho “Bài tập 2.2.1(c) · Tác động của bộ kết hợp”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(b), trang in 30 / PDF 11.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex221b).
- **Thời lượng:** 5 phút recitation.

### `lec02-ex221c` · Bài tập 2.2.1(c) · Tác động của bộ kết hợp

- **Kiến thức đầu vào:** Bộ kết hợp và 100 Map.
- **Mục đích:** Lập luận tác động của gộp cục bộ lên lệch tải.
- **Câu chốt:** Gộp đầy đủ ở mỗi Map giới hạn số giá trị mỗi từ gửi về reducer theo số tác vụ Map.
- **Kết nối vào–ra:** từ “Bài tập 2.2.1(b) · Gom reducer vào tác vụ”; tạo cơ sở cho “2.3 · Nhân ma trận–vector”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(c), trang in 30 / PDF 11.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex221c).
- **Thời lượng:** 5 phút recitation.

### `lec02-s03-01` · 2.3 · Nhân ma trận–vector

- **Kiến thức đầu vào:** Nhân hàng với vector; lưu phân tán.
- **Mục đích:** Đặc tả tích ma trận–vector trong biểu diễn thưa.
- **Câu chốt:** Mỗi thành phần của tích ma trận–vector là tổng đóng góp của một hàng.
- **Kết nối vào–ra:** từ “Phục hồi khi máy Reduce hỏng”; chuẩn bị “Khóa hàng gom đúng các tích”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-01).
- **Thời lượng:** 5 phút giảng.

### `lec02-s03-02` · Khóa hàng gom đúng các tích

- **Kiến thức đầu vào:** Đặc tả M,v,x.
- **Mục đích:** Tái tạo tổng hàng từ các đóng góp theo cột.
- **Câu chốt:** Khóa hàng đưa các tích của cùng một thành phần về cùng nhóm.
- **Kết nối vào–ra:** từ “2.3 · Nhân ma trận–vector”; chuẩn bị “Giả mã nhân ma trận–vector”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-02).
- **Thời lượng:** 4 phút giảng.

### `lec02-s03-02a` · Giả mã nhân ma trận–vector

- **Kiến thức đầu vào:** Vết tổng hàng và bất biến đếm từ.
- **Mục đích:** Giải thích giả mã gom tích trả đúng mỗi thành phần.
- **Câu chốt:** Khi vector vừa bộ nhớ, Map tính từng tích rồi reduce cộng theo hàng.
- **Kết nối vào–ra:** Từ “Khóa hàng gom đúng các tích”; cung cấp kết quả cho “Chia dải khi vector không vừa bộ nhớ”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-02a).
- **Thời lượng:** 4 phút giảng.

### `lec02-s03-03` · Chia dải khi vector không vừa bộ nhớ

- **Kiến thức đầu vào:** Vector phải vừa bộ nhớ.
- **Mục đích:** Giữ đủ tích khi chia vector thành các dải.
- **Câu chốt:** Chia dải giữ mỗi phần vector vừa bộ nhớ và vẫn gom đủ tích theo hàng.
- **Kết nối vào–ra:** Từ “Giả mã nhân ma trận–vector”; cung cấp kết quả cho “Công việc và bộ nhớ khi nhân ma trận–vector”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.3.2, Hình 2.4, trang in 32.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-03).
- **Thời lượng:** 4 phút giảng.

### `lec02-s03-03a` · Công việc và bộ nhớ khi nhân ma trận–vector

- **Kiến thức đầu vào:** Giả mã, chia dải vector và z phần tử được lưu.
- **Mục đích:** Tách số phép tính khỏi lượng vector cần giữ.
- **Câu chốt:** Chia dải giảm vùng vector cần giữ, vẫn có z phép nhân và z phép cộng.
- **Kết nối vào–ra:** Từ “Chia dải khi vector không vừa bộ nhớ”; cung cấp kết quả cho “Bài tập 2.3.1(a) · Số nguyên lớn nhất”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng thao tác và số phần tử vector n hoặc L; dẫn chi phí đọc lặp sang 2.5.
- **Nguồn:** MMDS Chương 2, 2.3.1–2.3.2, trang 31–32; phân tích từ giả mã.
- **Ghi chú:** [Giả thiết, phân tích và giới hạn](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-03a).
- **Thời lượng:** 3 phút giảng.


### `lec02-ex231a` · Bài tập 2.3.1(a) · Số nguyên lớn nhất

- **Kiến thức đầu vào:** Cách chọn khóa và tổng hợp.
- **Mục đích:** Thiết kế MapReduce tìm số nguyên lớn nhất.
- **Câu chốt:** Lấy cực đại phải khởi tạo hoặc xử lý đầu vào sao cho đúng cả với số âm.
- **Kết nối vào–ra:** Từ “Công việc và bộ nhớ khi nhân ma trận–vector”; cung cấp kết quả cho “Bài tập 2.3.1(b) · Trung bình các số nguyên”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(a), trang in 40 / PDF 21.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex231a).
- **Thời lượng:** 5 phút recitation.

### `lec02-ex231b` · Bài tập 2.3.1(b) · Trung bình các số nguyên

- **Kiến thức đầu vào:** Bộ kết hợp và cặp trạng thái.
- **Mục đích:** Giữ tổng và số lượng để tính trung bình đúng.
- **Câu chốt:** Trung bình cần tổng và số lượng; chia sau khi gộp hai đại lượng đó.
- **Kết nối vào–ra:** Từ “Bài tập 2.3.1(a) · Số nguyên lớn nhất”; cung cấp kết quả cho “Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(b), trang in 40 / PDF 21.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex231b).
- **Thời lượng:** 5 phút recitation.

### `lec02-ex231c` · Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần

- **Kiến thức đầu vào:** Phép chiếu loại trùng.
- **Mục đích:** Dùng khóa để mỗi số nguyên chỉ xuất hiện một lần.
- **Câu chốt:** Dùng giá trị làm khóa để mỗi số nguyên phân biệt chỉ được phát một lần.
- **Kết nối vào–ra:** từ “Bài tập 2.3.1(b) · Trung bình các số nguyên”; tạo cơ sở cho “Bài tập 2.3.1(d) · Số lượng giá trị khác nhau”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(c), trang in 40 / PDF 21.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex231c).
- **Thời lượng:** 5 phút recitation.

### `lec02-ex231d` · Bài tập 2.3.1(d) · Số lượng giá trị khác nhau

- **Kiến thức đầu vào:** Đếm và loại trùng.
- **Mục đích:** Tổng hợp số khóa phân biệt thành một số đếm.
- **Câu chốt:** Có thể loại trùng theo khóa rồi cộng số khóa để đếm giá trị phân biệt.
- **Kết nối vào–ra:** từ “Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần”; tạo cơ sở cho “2.4 · Luồng công việc nhiều hàm”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(d), trang in 40 / PDF 21.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex231d).
- **Thời lượng:** 5 phút recitation.

### `lec02-s04-01` · 2.4 · Luồng công việc nhiều hàm

- **Kiến thức đầu vào:** Hai tầng MapReduce và chịu lỗi.
- **Mục đích:** Đọc phụ thuộc dữ liệu giữa nhiều hàm.
- **Câu chốt:** Cung trong luồng công việc thể hiện đầu ra hàm trước cung cấp đầu vào hàm sau.
- **Kết nối vào–ra:** từ “Chia dải khi vector không vừa bộ nhớ”; chuẩn bị “Spark: Map và Flatmap”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.4.1, Hình 2.6 và Ví dụ 2.6, trang in 42–43.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-02` · Spark: Map và Flatmap

- **Kiến thức đầu vào:** D2, cặp từ–số đếm.
- **Mục đích:** Phân biệt một danh sách với nhiều phần tử RDD.
- **Câu chốt:** Map trả một đối tượng cho mỗi đầu vào; Flatmap có thể trả nhiều phần tử.
- **Kết nối vào–ra:** từ “2.4 · Luồng công việc nhiều hàm”; chuẩn bị “Nối Flatmap với Filter”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.4.2, Ví dụ 2.7, trang in 44–45.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-03` · Nối Flatmap với Filter

- **Kiến thức đầu vào:** RDD và Flatmap.
- **Mục đích:** Theo dõi lọc từng phần tử sau Flatmap.
- **Câu chốt:** Filter quyết định giữ hay bỏ từng phần tử mà Flatmap đã tạo.
- **Kết nối vào–ra:** từ “Spark: Map và Flatmap”; chuẩn bị “Đánh giá lười và dòng dõi”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.4.2, Ví dụ 2.8, trang in 45–46.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-04` · Đánh giá lười và dòng dõi

- **Kiến thức đầu vào:** Chuỗi Flatmap rồi Filter.
- **Mục đích:** Nêu thứ tự tính lại R2 từ lịch sử biến đổi.
- **Câu chốt:** Dòng dõi lưu cách tạo dữ liệu để tính lại phần bị mất khi còn đầu vào cần thiết.
- **Kết nối vào–ra:** từ “Nối Flatmap với Filter”; chuẩn bị “Vai trò lưu trữ và thực thi”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.4.3, Ví dụ 2.9–2.10, trang in 46–47.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-04).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-05` · Vai trò lưu trữ và thực thi

- **Kiến thức đầu vào:** DFS, MapReduce, Spark.
- **Mục đích:** Phân biệt trách nhiệm lưu trữ với thực thi.
- **Câu chốt:** Lưu trữ phân tán và hệ thực thi giải quyết hai trách nhiệm khác nhau.
- **Kết nối vào–ra:** từ “Đánh giá lười và dòng dõi”; chuẩn bị “2.5 · Quy ước tính chi phí”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.4.1–2.4.3, trang in 41–48; 2.4.4–2.4.6, trang in 48–53 là đọc thêm.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-05).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-02` · 2.5 · Quy ước tính chi phí

- **Kiến thức đầu vào:** Mạng tác vụ và nơi lưu dữ liệu.
- **Mục đích:** Chọn đơn vị, phạm vi và quy tắc đếm chi phí.
- **Câu chốt:** Phải chốt đơn vị, phạm vi và quy tắc đếm trước khi cộng chi phí.
- **Kết nối vào–ra:** từ “Vai trò lưu trữ và thực thi”; chuẩn bị “Cộng dữ liệu mà mỗi tầng nhận”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.5.1–2.5.2, trang in 53–56.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-02).
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-01` · Cộng dữ liệu mà mỗi tầng nhận

- **Kiến thức đầu vào:** Quy tắc chi phí đầu vào tác vụ.
- **Mục đích:** Lập tổng I+M từ hai tầng nhận dữ liệu.
- **Câu chốt:** Chi phí theo mô hình sách là tổng kích thước đầu vào của các tác vụ.
- **Kết nối vào–ra:** từ “2.5 · Quy ước tính chi phí”; chuẩn bị “Đếm từ: theo dữ liệu qua hai tầng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.5.1, trang in 53–55.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03` · Đếm từ: theo dữ liệu qua hai tầng

- **Kiến thức đầu vào:** Năm cặp, bốn cặp; I và B byte.
- **Mục đích:** Tính chi phí đếm từ trước và sau gộp.
- **Câu chốt:** Gộp D2 giảm trung gian từ năm xuống bốn cặp trong cùng ví dụ đếm từ.
- **Kết nối vào–ra:** từ “Cộng dữ liệu mà mỗi tầng nhận”; chuẩn bị “Ma trận–vector: đếm đầu vào từng tầng”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.1, 2.2.4 và mô hình 2.5.1; phần trích minh họa được ghi trong storyboard.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03a` · Ma trận–vector: đếm đầu vào từng tầng

- **Kiến thức đầu vào:** Cách chia dải vector và mô hình tổng đầu vào tác vụ.
- **Mục đích:** Đếm ma trận, vector và tích trung gian ở đúng nơi nhận.
- **Câu chốt:** Mỗi dải vector bị đọc lại theo số tác vụ cần nó.
- **Kết nối vào–ra:** từ “Đếm từ: theo dữ liệu qua hai tầng”; chuẩn bị “Chi phí đọc lặp dải vector”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, 2.3.2, 2.5.1 và Bài tập 2.5.1(a), trang in 32,54–55,59.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03a).
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-03b` · Chi phí đọc lặp dải vector

- **Kiến thức đầu vào:** Bảng ba lượng dữ liệu ở trang trước, tổng hữu hạn.
- **Mục đích:** Cộng ba số hạng và suy ra hai trường hợp phân công.
- **Câu chốt:** Nhiều tác vụ có thể tăng tổng dữ liệu đọc.
- **Kết nối vào–ra:** từ “Ma trận–vector: đếm đầu vào từng tầng”; chuẩn bị “Tổng chi phí và tải lớn nhất”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, 2.3.2, 2.5.1 và Bài tập 2.5.1(a), trang in 32,54–55,59.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03b).
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-09` · Tổng chi phí và tải lớn nhất

- **Kiến thức đầu vào:** Chi phí đọc dải vector và mô hình tổng đầu vào.
- **Mục đích:** Phân biệt tổng chi phí với thời gian hoàn thành.
- **Câu chốt:** Tổng đầu vào không đủ quyết định thời gian và bộ nhớ tác vụ nặng nhất.
- **Kết nối vào–ra:** từ “Chi phí đọc lặp dải vector”; chuẩn bị “2.6 · Tìm các cặp ảnh tương tự”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.5.2 và chuyển sang 2.6, trang in 55–56,61.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-09).
- **Thời lượng:** 2 phút giảng.

### `lec02-ex251a` · Bài tập 2.5.1(a) · Nhân ma trận–vector

- **Kiến thức đầu vào:** Chia dải và mô hình đầu vào.
- **Mục đích:** Đếm chi phí nhân ma trận–vector có đọc lặp dải.
- **Câu chốt:** Chi phí chia dải phải tính cả số lần mỗi dải vector được các tác vụ đọc.
- **Kết nối vào–ra:** từ “Tổng chi phí và tải lớn nhất”; tạo cơ sở cho “2.6 · Tìm các cặp ảnh tương tự”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.5.1(a), trang in 59 / PDF 40; 2.3.2.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex251a).
- **Thời lượng:** 25 phút recitation.

### `lec02-s06-00` · 2.6 · Tìm các cặp ảnh tương tự

- **Kiến thức đầu vào:** Đánh đổi bộ nhớ và truyền dữ liệu.
- **Mục đích:** Đặc tả đầu ra cặp ảnh vượt ngưỡng tương tự.
- **Câu chốt:** Cần kiểm tra mọi cặp ảnh nhưng chỉ trả các cặp vượt ngưỡng tương tự.
- **Kết nối vào–ra:** từ “Tổng chi phí và tải lớn nhất”; chuẩn bị “Đầu vào mỗi reducer và số lần sao chép”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 62–63.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-00).
- **Thời lượng:** 3 phút giảng.

### `lec02-s06-01` · Đầu vào mỗi reducer và số lần sao chép

- **Kiến thức đầu vào:** Nhu cầu chia ảnh cho reducer.
- **Mục đích:** Đọc q và rho như hai đại lượng khác nhau.
- **Câu chốt:** q giới hạn đầu vào mỗi reducer; rho đếm số cặp phát trung bình trên một đầu vào.
- **Kết nối vào–ra:** từ “2.6 · Tìm các cặp ảnh tương tự”; chuẩn bị “Mỗi reducer xử lý một cặp ảnh”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.6.1, trang in 61.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-01).
- **Thời lượng:** 3 phút giảng.

### `lec02-s06-02` · Mỗi reducer xử lý một cặp ảnh

- **Kiến thức đầu vào:** q,rho; cặp không thứ tự.
- **Mục đích:** Đếm số bản sao khi mỗi reducer nhận hai ảnh.
- **Câu chốt:** Mỗi reducer nhận hai ảnh nhưng mỗi ảnh phải gửi tới N−1 nơi.
- **Kết nối vào–ra:** từ “Đầu vào mỗi reducer và số lần sao chép”; chuẩn bị “Gom nhóm để dùng lại mỗi ảnh”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 62–63.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-02).
- **Thời lượng:** 3 phút giảng.

### `lec02-s06-03` · Gom nhóm để dùng lại mỗi ảnh

- **Kiến thức đầu vào:** Phương án từng cặp, chia đều1000 nhóm.
- **Mục đích:** Tính q,rho khi mỗi reducer nhận hai nhóm.
- **Câu chốt:** Gom nhóm tăng dữ liệu mỗi reducer để dùng lại ảnh đã nhận cho nhiều phép so sánh.
- **Kết nối vào–ra:** Từ “Mỗi reducer xử lý một cặp ảnh”; cung cấp kết quả cho “Bao phủ mọi cặp, mỗi cặp đúng một nơi”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.6.2, Ví dụ 2.18, trang in 63–64.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03a` · Bao phủ mọi cặp, mỗi cặp đúng một nơi

- **Kiến thức đầu vào:** Cặp nhóm và phép modulo.
- **Mục đích:** Chứng minh mọi cặp ảnh được xét đúng một nơi.
- **Câu chốt:** Mọi cặp chéo và cặp nội bộ đều được giao đúng một nơi, không giảm số cặp phải so sánh.
- **Kết nối vào–ra:** Từ “Gom nhóm để dùng lại mỗi ảnh”; cung cấp kết quả cho “Số phép so sánh khi gom nhóm ảnh”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** SVG có nhãn và chiều luồng.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 63–64.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03b` · Số phép so sánh khi gom nhóm ảnh

- **Kiến thức đầu vào:** Phân công mọi cặp đúng một nơi, N=10^6 và g=1000.
- **Mục đích:** Tính tổng số lần gọi hàm và tải lớn nhất một reducer.
- **Câu chốt:** Gom nhóm không giảm số cặp phải xét, nhưng dồn nhiều phép so sánh vào một reducer.
- **Kết nối vào–ra:** Từ “Bao phủ mọi cặp, mỗi cặp đúng một nơi”; cung cấp kết quả cho “Đánh đổi cần kiểm tra trước khi triển khai”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng hai cách chia; tổng 499999500000, tối đa 1 hoặc1499500; notes đếm cặp chéo/nội bộ.
- **Nguồn:** MMDS Chương 2, 2.6.2, trang 62–64; phép đếm từ quy tắc nguồn.
- **Ghi chú:** [Giả thiết, phân tích và giới hạn](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03b).
- **Thời lượng:** 3 phút giảng.


### `lec02-s06-04` · Đánh đổi cần kiểm tra trước khi triển khai

- **Kiến thức đầu vào:** q2000,1 MB/ảnh; đầy đủ các cặp.
- **Mục đích:** Kiểm tra bộ nhớ thực tế ngoài kích thước ảnh.
- **Câu chốt:** Dung lượng ảnh chưa bao gồm bộ nhớ phụ nên chưa đủ kết luận reducer chạy được.
- **Kết nối vào–ra:** Từ “Số phép so sánh khi gom nhóm ảnh”; cung cấp kết quả cho “2.7 · Từ lưu trữ đến đánh giá thuật toán”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.6.2–2.6.7, trang in 61–74.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-04).
- **Thời lượng:** 2 phút giảng.

### `lec02-s07-01` · 2.7 · Từ lưu trữ đến đánh giá thuật toán

- **Kiến thức đầu vào:** Các kết quả từ2.1–2.6.
- **Mục đích:** Nối cách chọn khóa với lưu trữ và đánh giá.
- **Câu chốt:** Cách chọn khóa quyết định nơi dữ liệu gặp nhau và ảnh hưởng cả chi phí lẫn bộ nhớ.
- **Kết nối vào–ra:** Từ “Đánh đổi cần kiểm tra trước khi triển khai”; cung cấp kết quả cho “Kiểm tra bằng sản phẩm học tập”. Bài tập được quay lại sau phần giảng.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.7, trang in 74–77.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s07-01).
- **Thời lượng:** 3 phút giảng.

### `lec02-s07-02` · Kiểm tra bằng sản phẩm học tập

- **Kiến thức đầu vào:** Giả mã đếm từ, giữ lặp, I+M và tải bộ nhớ ảnh.
- **Mục đích:** Tự kiểm tra giả mã, giữ lặp, chi phí đếm từ và bộ nhớ ảnh.
- **Câu chốt:** Vết chạy, chi phí và khả thi bộ nhớ là các yêu cầu riêng.
- **Kết nối vào–ra:** từ “2.7 · Từ lưu trữ đến đánh giá thuật toán”; chuẩn bị “2.8 · Tài liệu tham khảo”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.7 và bài tập 2.2.1,2.3.1,2.5.1.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s07-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s08-01` · 2.8 · Tài liệu tham khảo

- **Kiến thức đầu vào:** Toàn bộ phần giảng.
- **Mục đích:** Tìm nguồn chính và ghi chú tự học.
- **Câu chốt:** Chương 2 là nguồn chính; ghi chú giúp tự học, các mục cận dưới được định vị đọc thêm.
- **Kết nối vào–ra:** từ “Kiểm tra bằng sản phẩm học tập”; chuẩn bị “Bài 2.2.1 để bắt đầu recitation”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.8, trang in 77–79.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s08-01).
- **Thời lượng:** 1 phút giảng.

## Ánh xạ ghi chú độc lập

- `note-02-01` → mục 2.1 của lecture-note.md và các slide cùng mục. Vai trò: Cụm máy → lỗi → khối và bản sao → đầu vào tác vụ. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-02` → mục 2.2 của lecture-note.md và các slide cùng mục. Vai trò: Đếm từ → vết phát/nhóm/cộng → hai chữ ký → hình luồng → giả mã và đúng → thực thi. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-03` → mục 2.3 của lecture-note.md và các slide cùng mục. Vai trò: Đổi khóa từ từ sang hàng → vết các tích → giả mã → chia dải vector. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-04` → mục 2.4 của lecture-note.md và các slide cùng mục. Vai trò: Một công việc → đồ thị phụ thuộc → Spark/tính lại → nhiều tác vụ cần đánh giá. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-05` → mục 2.5 của lecture-note.md và các slide cùng mục. Vai trò: Mô hình/đơn vị → đếm từ → đọc dải vector → tổng và tải lớn nhất. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-06` → mục 2.6 của lecture-note.md và các slide cùng mục. Vai trò: Giới hạn tác vụ → đặc tả ảnh → từng cặp → nhóm ảnh → đúng và bộ nhớ. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-07` → mục 2.7 của lecture-note.md và các slide cùng mục. Vai trò: Thu hồi các lớp lập luận → bốn sản phẩm tự kiểm tra. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-08` → mục 2.8 của lecture-note.md và các slide cùng mục. Vai trò: Nguồn/hướng đọc → bài tập từ giáo trình. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.

## Các bổ sung trong bản hiện hành

Trang lợi ích s02-01a nằm sau mở mục 2.2, trước vết đếm từ; cơ chế chi tiết ở 06–07b. Bốn trang đặc tả/đánh giá mới là s02-03c, s02-04b, s03-03a và s06-03b. Tổng hiện hành 58 trang = 50 giảng + 8 bài tập; mục 2.2 có 38 phút, toàn bài 120+60 phút theo bảng và từng trang phía trên. Phân bổ của lần thêm lợi ích trước đây được lưu trong review-log, không dùng làm ngân sách hiện hành.

Đặc tả ma trận làm rõ tọa độ duy nhất và đầu ra hàng rỗng; đặc tả ảnh quy định mã 1..N và cặp i<j. Bộ kết hợp có phân tích số tổng cục bộ và bộ nhớ bảng trong ghi chú. Lời giải Bài 2.3.1 bổ sung bảng đặc tả/đánh giá, giữ nguyên đề. Các đại lượng bộ nhớ phụ không gồm vùng đầu vào và quản lý hệ thống. Không thêm SVG vì bốn trang mới dùng bảng HTML để đối chiếu các bước với phép đếm; giữ 13 hình hiện có.
