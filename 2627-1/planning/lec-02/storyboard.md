# Storyboard Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Phạm vi hiện hành — 2026-09-15, bổ sung tổ chức thực thi và phục hồi

Áp dụng [slide_authoring_standard.md](../../../slide_authoring_standard.md) và [AGENTS.md](../../../AGENTS.md). Sinh viên năm 2 đã học lập trình và nhân ma trận–vector, chưa học CSDL. Nguồn chính: [MMDS Chương 2](../../../sources/textbooks/ch2n.pdf), trang in 20–79; trang PDF bằng trang in trừ 19. Giữ 9 section: mở đầu và mỗi mục 2.1–2.8 một section theo yêu cầu người dùng, ngoại lệ quy tắc 5–7 section.

Bản hiện hành có **60 trang giảng và 8 trang bài tập**, thiết kế **120 phút giảng + 60 phút recitation**. Phân bổ dự kiến, chưa diễn tập với lớp thật. Bỏ quan hệ, chọn, chiếu, nối, tổng hợp và liên hệ nhân hai ma trận (2.3.3–2.3.10), các ví dụ chi phí nối của 2.5.3 và bài 2.5.1(c) theo chỉ dẫn mới về tiên quyết. Không giữ phép nối ngầm trong bài tập hoặc phần kết. Thời gian chuyển sang giải thích hai hàm, vết chạy và đếm chi phí; không thêm số liệu ngoài nguồn.

Recitation: 2.2.1(a–c), trang 30/PDF 11: 15 phút; 2.3.1(a–d), trang 40/PDF 21: 20 phút; 2.5.1(a), trang 59/PDF 40: 25 phút. Giữ nguyên đề nguồn, chỉ dịch và tách ý. Bỏ bài 2.5.1(c), dành trọn 25 phút cho lập bảng, trình bày và đối chiếu điều kiện của ý (a); không thêm bài mới. Bài tập nằm cuối section nguồn, ngoại lệ để giữ ánh xạ PDF; liên kết từ tổng kết dẫn vào recitation sau phần giảng.

## Hành trình khái niệm

| Mục | Mạch viết và sản phẩm chuyển tiếp | Phút giảng |
|---|---|---:|
| Mở đầu | Giới hạn một máy → mục tiêu và nội dung. | 5 |
| 2.1 | Cụm máy → lỗi → khối và bản sao → đầu vào tác vụ. | 7 |
| 2.2 | Lợi ích → đếm từ → hai hàm → giả mã/đúng → tạo tác vụ → phân khóa → gán máy → dữ liệu còn lại → phục hồi lỗi. | 31 |
| 2.3 | Đổi khóa từ từ sang hàng → vết các tích → giả mã → chia dải vector. | 16 |
| 2.4 | Văn bản → tách/lọc/đếm → Hadoop → Spark → dùng lại/khôi phục → chi phí. | 17 |
| 2.5 | Hai nơi nhận → đếm/cộng chi phí → tổng công việc → thời gian tuần tự/song song → chia đều và giới hạn. | 19 |
| 2.6 | Bài toán ảnh → bốn ảnh chạy tay → byte → q/rho → nhóm ảnh → đếm lại → bao phủ → so sánh và đánh đổi. | 19 |
| 2.7 | Thu hồi các lớp lập luận → bốn sản phẩm tự kiểm tra. | 5 |
| 2.8 | Nguồn/hướng đọc → bài tập từ giáo trình. | 1 |

## Chu trình và nguồn

- Đếm từ: s02-01 đặt vấn đề; 02/03 chạy vết; 03a hình thức hóa; 03b nối hai hàm bằng sơ đồ; 04 giả mã; 03c đặc tả đầu ra; 04a tính đúng; 04b đếm thao tác; 05 gộp; 06–06c tạo và phân công tác vụ; 07–07b lưu trữ và phục hồi. D1 “dữ liệu lớn”, D2 “lớn lớn” là ví dụ Việt hóa đã có, minh họa Ví dụ 2.1–2.2, trang 25–27. Số 1 biểu diễn từng lần xuất hiện; không loại lặp. Hình dựa Hình 2.2, không đồng nhất mỗi hàm với một máy. Kiểm tra ở 02/06 và tổng kết; chi phí dùng lại cùng 5 cặp ở s05-03.
- Ma trận–vector: s03-01 đặc tả từ tiên quyết; 02 vết ký hiệu; 02a giả mã, giả thiết và đúng; 03 chia dải (Hình 2.4); 03a đánh giá phép tính và bộ nhớ. Không tự đặt ma trận số ngoài nguồn. 2.5 quay lại dữ liệu này: mỗi phần tử đọc một lần, mỗi tác vụ đọc dải vector cần dùng. s05-03a đếm bộ ma trận và cặp tích; 03c đếm dải vector đọc lặp; 03b cộng ba khoản rồi xét trường hợp trong notes. Bài 2.5.1(a) yêu cầu giải thích mỗi số hạng và điều kiện. Số học chính xác; hàng không lưu hiểu bằng 0.
- Cặp ảnh: s06-00 đặt bài toán; 02 chạy tay bốn ảnh; 02a đếm byte; 01 đặt tên q/rho sau ví dụ; 03/03c/03d gom nhóm và đếm lại; 03a chứng minh bao phủ; 03b đếm số so sánh; 04 kiểm tra đánh đổi. Giữ dữ kiện một triệu ảnh, một triệu byte mỗi ảnh và 1000 nhóm đều.
- Hệ thống và Spark dùng hình cơ chế/phụ thuộc; không tạo chứng minh hay giả mã ngoài nguồn. MMDS và Stanford đã được kiểm kê; sách quyết định mạch, ví dụ và chi phí. Giữ cách thể hiện một bước suy luận mỗi trang, ví dụ trước ký hiệu đã tham khảo math-4-AI 01–03.
- 30 SVG được dùng; các hình mới ở 2.5–2.6 diễn giải từng phép đếm; phần2.4 thay hai hình cũ bằng bốn hình về chuỗi văn bản, Hadoop, lưu đệm và phục hồi Spark. Các hình thực thi/phục hồi MapReduce ở2.2 được giữ. Hình khóa–tác vụ cũ không còn nhúng; các tài sản cũ giữ để truy nguyên. Mỗi hình mới có script tái sinh, mô tả và mũi tên; không dùng màu làm tín hiệu duy nhất.

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
- **Thời lượng:** 2 phút giảng.

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
- **Thời lượng:** 1 phút giảng.

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
- **Thời lượng:** 1 phút giảng.

### `lec02-s02-03` · Nhóm theo khóa rồi cộng

- **Kiến thức đầu vào:** Năm cặp đã phát.
- **Mục đích:** Tính tổng cho từng khóa và giữ các lần xuất hiện trùng.
- **Câu chốt:** Ba đóng góp của từ “lớn” về cùng khóa và được cộng thành 3.
- **Kết nối vào–ra:** từ “Mỗi lần xuất hiện tạo một đóng góp”; chuẩn bị “Hai hàm của MapReduce”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.2.2–2.2.3, Ví dụ 2.2, trang in 26–27.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03).
- **Thời lượng:** 1 phút giảng.

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
- **Thời lượng:** 2 phút giảng.

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
- **Thời lượng:** 3 phút giảng.

### `lec02-s03-02` · Khóa hàng gom đúng các tích

- **Kiến thức đầu vào:** Đặc tả M,v,x.
- **Mục đích:** Tái tạo tổng hàng từ các đóng góp theo cột.
- **Câu chốt:** Khóa hàng đưa các tích của cùng một thành phần về cùng nhóm.
- **Kết nối vào–ra:** từ “2.3 · Nhân ma trận–vector”; chuẩn bị “Giả mã nhân ma trận–vector”. Mạch giảng bỏ qua recitation tới cuối buổi.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-02).
- **Thời lượng:** 2 phút giảng.

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
- **Kết nối vào–ra:** từ “Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần”; tạo cơ sở cho “2.4 · Từ văn bản đến chuỗi xử lý dữ liệu”. Bài tập dùng sau phần giảng qua liên kết.
- **Cách thể hiện:** Bảng, giả mã hoặc công thức theo từng bước; diễn giải và đáp án trong notes.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(d), trang in 40 / PDF 21.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-ex231d).
- **Thời lượng:** 5 phút recitation.

### `lec02-s04-01` · 2.4 · Từ văn bản đến chuỗi xử lý dữ liệu

- **Kiến thức đầu vào:** Giả mã MapReduce và mô hình tác vụ đã học.
- **Mục đích:** Đặc tả và chạy tay ví dụ lọc rồi đếm từ.
- **Câu chốt:** Lọc đúng từ dừng rồi đếm mọi lần xuất hiện còn lại.
- **Kết nối vào–ra:** Từ “Giả mã MapReduce và mô hình tác vụ đã học”; cung cấp cơ chế và dữ liệu cho “Đầu ra một bước là đầu vào bước sau”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-02` · Đầu ra một bước là đầu vào bước sau

- **Kiến thức đầu vào:** 2.4 · Từ văn bản đến chuỗi xử lý dữ liệu.
- **Mục đích:** Theo dõi dữ liệu qua chuỗi bước và hai nhánh dùng lại.
- **Câu chốt:** Các bước phụ thuộc qua dữ liệu, và một kết quả có thể dùng cho nhiều nhánh.
- **Kết nối vào–ra:** Từ “2.4 · Từ văn bản đến chuỗi xử lý dữ liệu”; cung cấp cơ chế và dữ liệu cho “Hadoop: lưu dữ liệu và chạy MapReduce”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-03` · Hadoop: lưu dữ liệu và chạy MapReduce

- **Kiến thức đầu vào:** Đầu ra một bước là đầu vào bước sau.
- **Mục đích:** Phân biệt vai trò HDFS và Hadoop MapReduce.
- **Câu chốt:** HDFS lưu tệp; Hadoop MapReduce tổ chức tính toán.
- **Kết nối vào–ra:** Từ “Đầu ra một bước là đầu vào bước sau”; cung cấp cơ chế và dữ liệu cho “Ví dụ văn bản trong Hadoop MapReduce”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-04` · Ví dụ văn bản trong Hadoop MapReduce

- **Kiến thức đầu vào:** Hadoop: lưu dữ liệu và chạy MapReduce.
- **Mục đích:** Ánh xạ tách/lọc/đếm vào một công việc MapReduce.
- **Câu chốt:** Tách và lọc có thể nằm trong cùng hàm Map của một công việc.
- **Kết nối vào–ra:** Từ “Hadoop: lưu dữ liệu và chạy MapReduce”; cung cấp cơ chế và dữ liệu cho “Spark: biến đổi các phần dữ liệu”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-04).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-05` · Spark: biến đổi các phần dữ liệu

- **Kiến thức đầu vào:** Ví dụ văn bản trong Hadoop MapReduce.
- **Mục đích:** Phân biệt map, flatMap và filter trên cùng tài liệu.
- **Câu chốt:** map tạo một đối tượng, flatMap tạo từng phần tử, filter giữ phần tử đạt điều kiện.
- **Kết nối vào–ra:** Từ “Ví dụ văn bản trong Hadoop MapReduce”; cung cấp cơ chế và dữ liệu cho “Spark: từ chuỗi biến đổi đến kết quả”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-05).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-06` · Spark: từ chuỗi biến đổi đến kết quả

- **Kiến thức đầu vào:** Spark: biến đổi các phần dữ liệu.
- **Mục đích:** Đọc chuỗi biến đổi Spark và xác định hành động tạo kết quả.
- **Câu chốt:** reduceByKey tạo số đếm theo từ; hành động lưu yêu cầu tính và ghi kết quả.
- **Kết nối vào–ra:** Từ “Spark: biến đổi các phần dữ liệu”; cung cấp cơ chế và dữ liệu cho “Tính khi cần và dùng lại kết quả”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-06).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-07` · Tính khi cần và dùng lại kết quả

- **Kiến thức đầu vào:** Spark: từ chuỗi biến đổi đến kết quả.
- **Mục đích:** Giải thích thời điểm tính và điều kiện dùng lại dữ liệu.
- **Câu chốt:** Lưu lại dữ liệu đã tính giúp hành động sau dùng lại các phần còn giữ.
- **Kết nối vào–ra:** Từ “Spark: từ chuỗi biến đổi đến kết quả”; cung cấp cơ chế và dữ liệu cho “Tính lại phần dữ liệu bị mất”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-07).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-08` · Tính lại phần dữ liệu bị mất

- **Kiến thức đầu vào:** Tính khi cần và dùng lại kết quả.
- **Mục đích:** Chỉ ra phần cần đọc và tính lại khi mất dữ liệu.
- **Câu chốt:** Lịch sử biến đổi chỉ ra cách tái tạo phần cần dùng từ nguồn còn tồn tại.
- **Kết nối vào–ra:** Từ “Tính khi cần và dùng lại kết quả”; cung cấp cơ chế và dữ liệu cho “Hadoop MapReduce và Spark”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-08).
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-09` · Hadoop MapReduce và Spark

- **Kiến thức đầu vào:** Tính lại phần dữ liệu bị mất.
- **Mục đích:** Phân biệt hệ tính toán với lưu trữ và nhận ra bước cần nhóm dữ liệu.
- **Câu chốt:** Spark có thể dùng HDFS; cả hai hệ tính toán đều cần được đánh giá theo dữ liệu thực nhận.
- **Kết nối vào–ra:** Từ “Tính lại phần dữ liệu bị mất”; cung cấp cơ chế và dữ liệu cho “2.5 · Quy ước tính chi phí”.
- **Cách thể hiện:** Ví dụ A/B đi xuyên suốt; sơ đồ dữ liệu ở 02/04/07/08, bảng vai trò hoặc phép biến đổi ở 03/05/09, giả mã ở 06. Mỗi trang chỉ tập trung bước nêu trong tiêu đề.
- **Nguồn:** MMDS 2.4.1–2.4.3, trang 41–48, Ví dụ 2.7–2.10; Apache Hadoop và Spark RDD Guide cho tên thành phần/API, theo outline. Ví dụ A/B là chuyển ngữ cơ chế nguồn, không thay D1/D2.
- **Ghi chú:** [Lập luận, giả thiết và câu chuyển](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-09).
- **Thời lượng:** 1 phút giảng.

### `lec02-s05-02` · 2.5 · Đếm dữ liệu mỗi tác vụ nhận

- **Kiến thức đầu vào:** So sánh Hadoop và Spark.
- **Mục đích / câu chốt:** Hai tài liệu vào Map; năm cặp vào Reduce. Bộ đếm ở đầu vào mỗi tầng.
- **Kết nối vào–ra:** từ “So sánh Hadoop và Spark”; chuẩn bị “Từ hai bộ đếm đến tổng chi phí”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.5.1–2.5.2, trang 53–56; Ví dụ 2.1 và 2.2.4.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-01` · Từ hai bộ đếm đến tổng chi phí

- **Kiến thức đầu vào:** 2.5 · Đếm dữ liệu mỗi tác vụ nhận.
- **Mục đích / câu chốt:** I là đầu vào Map, M là trung gian đến Reduce; C = I + M.
- **Kết nối vào–ra:** từ “2.5 · Đếm dữ liệu mỗi tác vụ nhận”; chuẩn bị “Năm cặp trung gian tạo 5B byte”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.5.1–2.5.2, trang 53–56; Ví dụ 2.1 và 2.2.4.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03` · Năm cặp trung gian tạo 5B byte

- **Kiến thức đầu vào:** Từ hai bộ đếm đến tổng chi phí.
- **Mục đích / câu chốt:** D1 phát ba cặp dữ một, liệu một, lớn một; D2 phát hai cặp lớn một, mỗi cặp dài B byte.
- **Kết nối vào–ra:** từ “Từ hai bộ đếm đến tổng chi phí”; chuẩn bị “Gộp trong D2 bớt một cặp”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.5.1–2.5.2, trang 53–56; Ví dụ 2.1 và 2.2.4.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-04` · Gộp trong D2 bớt một cặp

- **Kiến thức đầu vào:** Năm cặp trung gian tạo 5B byte.
- **Mục đích / câu chốt:** Hai cặp (lớn,1) gộp thành (lớn,2): 4 cặp đến Reduce thay vì 5.
- **Kết nối vào–ra:** từ “Năm cặp trung gian tạo 5B byte”; chuẩn bị “Ma trận: một lần đọc, một lần nhận tích”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.5.1–2.5.2, trang 53–56; Ví dụ 2.1 và 2.2.4.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-04).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03a` · Ma trận: một lần đọc, một lần nhận tích

- **Kiến thức đầu vào:** Gộp trong D2 bớt một cặp.
- **Mục đích / câu chốt:** z phần tử ma trận vào Map; mỗi phần tử tạo một cặp tích, z cặp vào Reduce.
- **Kết nối vào–ra:** từ “Gộp trong D2 bớt một cặp”; chuẩn bị “Một dải vector có thể được đọc nhiều lần”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.3.2, 2.5.1 và Bài 2.5.1(a), trang 32, 54–55, 59; phép đếm suy ra từ nguồn.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03c` · Một dải vector có thể được đọc nhiều lần

- **Kiến thức đầu vào:** Ma trận: một lần đọc, một lần nhận tích.
- **Mục đích / câu chốt:** Dải L_j được 2 tác vụ Map đọc: tổng 2L_j; tổng quát a_j tác vụ đọc a_j L_j.
- **Kết nối vào–ra:** từ “Ma trận: một lần đọc, một lần nhận tích”; chuẩn bị “Ghép ba khoản chi phí”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.3.2, 2.5.1 và Bài 2.5.1(a), trang 32, 54–55, 59; phép đếm suy ra từ nguồn.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03c).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-03b` · Ghép ba khoản chi phí

- **Kiến thức đầu vào:** Một dải vector có thể được đọc nhiều lần.
- **Mục đích / câu chốt:** Ba khoản: ma trận z, vector Σ a_j L_j, tích z; tổng C = 2z + Σ a_j L_j.
- **Kết nối vào–ra:** từ “Một dải vector có thể được đọc nhiều lần”; chuẩn bị “Tổng dữ liệu và nơi nhận nhiều nhất”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.3.2, 2.5.1 và Bài 2.5.1(a), trang 32, 54–55, 59; phép đếm suy ra từ nguồn.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03b).
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-09` · Song song hóa giảm thời gian hoàn thành

- **Kiến thức đầu vào:** Ghép ba khoản chi phí; vết Reduce R0/R1 đã có.
- **Mục đích / câu chốt:** Cùng R0=2,R1=3 chưa gộp: một máy5c,hai máy3c; tổng5giátrị và5B không đổi, thời gian hoàn thành giảm.
- **Kết nối vào–ra:** từ “Ghép ba khoản chi phí”; chuẩn bị “Thêm máy cần đủ việc và chia đều”.
- **Cách thể hiện:** Trục thời gian cùng tỉ lệ hoặc bảng 1/2/3 máy; giả thiết c và phạm vi tầng Reduce ghi trước kết luận.
- **Nguồn:** MMDS 2.5.2, trang55–56; liên hệ2.6, trang64; phép tính suy ra từ mô hình giả định, không số đo thực tế.
- **Ghi chú:** [Lập luận và điều kiện](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-09).
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-10` · Thêm máy cần đủ việc và chia đều

- **Kiến thức đầu vào:** Song song hóa giảm thời gian hoàn thành; vết Reduce R0/R1 đã có.
- **Mục đích / câu chốt:** Thêm máy chỉ có ích khi có đủ tác vụ và chia đều; tác vụ nặng nhất và chi phí phụ giới hạn tăng tốc.
- **Kết nối vào–ra:** từ “Song song hóa giảm thời gian hoàn thành”; chuẩn bị “Phân chia ảnh để giảm số bản gửi”.
- **Cách thể hiện:** Trục thời gian cùng tỉ lệ hoặc bảng 1/2/3 máy; giả thiết c và phạm vi tầng Reduce ghi trước kết luận.
- **Nguồn:** MMDS 2.5.2, trang55–56; liên hệ2.6, trang64; phép tính suy ra từ mô hình giả định, không số đo thực tế.
- **Ghi chú:** [Lập luận và điều kiện](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-10).
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


### `lec02-s06-00` · 2.6 · Phân chia ảnh để giảm số bản gửi

- **Kiến thức đầu vào:** Tổng dữ liệu và nơi nhận nhiều nhất.
- **Mục đích / câu chốt:** Hai ảnh được hàm độ tương tự s đánh giá; giữ cặp nếu vượt ngưỡng tau.
- **Kết nối vào–ra:** từ “Tổng dữ liệu và nơi nhận nhiều nhất”; chuẩn bị “Một ảnh phải đến nhiều cặp”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-00).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-02` · Một ảnh phải đến nhiều cặp

- **Kiến thức đầu vào:** 2.6 · Phân chia ảnh để giảm số bản gửi.
- **Mục đích / câu chốt:** Bốn ảnh và sáu khóa cặp: mỗi ảnh đến ba khóa, mỗi khóa nhận hai ảnh.
- **Kết nối vào–ra:** từ “2.6 · Phân chia ảnh để giảm số bản gửi”; chuẩn bị “Từ số bản gửi đến số byte”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-02).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-02a` · Từ số bản gửi đến số byte

- **Kiến thức đầu vào:** Một ảnh phải đến nhiều cặp.
- **Mục đích / câu chốt:** Ba yếu tố nhân: N ảnh × (N−1) nơi nhận mỗi ảnh × B byte mỗi ảnh.
- **Kết nối vào–ra:** từ “Một ảnh phải đến nhiều cặp”; chuẩn bị “Đặt tên hai đại lượng vừa đếm”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-02a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-01` · Đặt tên hai đại lượng vừa đếm

- **Kiến thức đầu vào:** Từ số bản gửi đến số byte.
- **Mục đích / câu chốt:** Nhắc lại: P1 đến 3 nơi; mỗi nơi nhận 2 ảnh — hai con số là q và ρ.
- **Kết nối vào–ra:** từ “Từ số bản gửi đến số byte”; chuẩn bị “Gom nhóm để dùng lại ảnh”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-01).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03` · Gom nhóm để dùng lại ảnh

- **Kiến thức đầu vào:** Đặt tên hai đại lượng vừa đếm.
- **Mục đích / câu chốt:** N ảnh chia g nhóm đều; một reducer nhận 2 nhóm và so sánh nhiều cặp bằng ảnh đã nhận.
- **Kết nối vào–ra:** từ “Đặt tên hai đại lượng vừa đếm”; chuẩn bị “Đếm lại nơi nhận và số ảnh”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03c` · Đếm lại nơi nhận và số ảnh

- **Kiến thức đầu vào:** Gom nhóm để dùng lại ảnh.
- **Mục đích / câu chốt:** Nhóm u ghép g−1 cặp nhóm; mỗi nơi nhận 2 nhóm, mỗi nhóm N/g ảnh.
- **Kết nối vào–ra:** từ “Gom nhóm để dùng lại ảnh”; chuẩn bị “Gom nhóm giảm số byte trung gian”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03c).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03d` · Gom nhóm giảm số byte trung gian

- **Kiến thức đầu vào:** Đếm lại nơi nhận và số ảnh.
- **Mục đích / câu chốt:** Cùng ba yếu tố nhưng thay (N−1) bằng (g−1): N(g−1)B byte.
- **Kết nối vào–ra:** từ “Đếm lại nơi nhận và số ảnh”; chuẩn bị “Mỗi cặp được so sánh đúng một nơi”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03d).
- **Thời lượng:** 1 phút giảng.

### `lec02-s06-03a` · Mỗi cặp được so sánh đúng một nơi

- **Kiến thức đầu vào:** Gom nhóm giảm số byte trung gian.
- **Mục đích / câu chốt:** Reducer của hai nhóm: cặp chéo u,v → {u,v}; cặp nội bộ nhóm u chỉ giao cho nhóm kế tiếp; nhóm cuối quay về 0.
- **Kết nối vào–ra:** từ “Gom nhóm giảm số byte trung gian”; chuẩn bị “Số cặp phải xét vẫn giữ nguyên”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03a).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03b` · Số cặp phải xét vẫn giữ nguyên

- **Kiến thức đầu vào:** Mỗi cặp được so sánh đúng một nơi.
- **Mục đích / câu chốt:** Lưới 4×4 tô 6 ô phía trên đường chéo: N(N−1)/2 phép so sánh.
- **Kết nối vào–ra:** từ “Mỗi cặp được so sánh đúng một nơi”; chuẩn bị “Đánh đổi giữa bản gửi và dữ liệu mỗi nơi”.
- **Cách thể hiện:** SVG lớn theo phép đếm, công thức HTML/KaTeX và lời giải trong notes.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
- **Ghi chú:** [Giả thiết, lập luận và đáp án](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03b).
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-04` · Đánh đổi giữa bản gửi và dữ liệu mỗi nơi

- **Kiến thức đầu vào:** Số cặp phải xét vẫn giữ nguyên.
- **Mục đích / câu chốt:** Bảng so sánh hai phương án; tính 2000 ảnh × một triệu byte = 2 GB mỗi nơi rồi kiểm tra bộ nhớ phụ.
- **Kết nối vào–ra:** từ “Số cặp phải xét vẫn giữ nguyên”; chuẩn bị “Tổng kết”.
- **Cách thể hiện:** Bảng so sánh hai phương án; tính 2000 ảnh × một triệu byte = 2 GB mỗi nơi rồi kiểm tra bộ nhớ phụ.
- **Nguồn:** MMDS 2.6.1–2.6.2, trang 61–64; hình bốn ảnh từ Ví dụ 2.19/Hình 2.9, trang 64–65.
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
- `note-02-04` → mục 2.4 của lecture-note.md và các slide cùng mục. Vai trò: Văn bản → tách/lọc/đếm → Hadoop → Spark → dùng lại/khôi phục → chi phí. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-05` → mục 2.5 của lecture-note.md và các slide cùng mục. Vai trò: Mô hình/đơn vị → đếm từ → đọc dải vector → tổng và tải lớn nhất. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-06` → mục 2.6 của lecture-note.md và các slide cùng mục. Vai trò: Giới hạn tác vụ → đặc tả ảnh → từng cặp → nhóm ảnh → đúng và bộ nhớ. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-07` → mục 2.7 của lecture-note.md và các slide cùng mục. Vai trò: Thu hồi các lớp lập luận → bốn sản phẩm tự kiểm tra. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.
- `note-02-08` → mục 2.8 của lecture-note.md và các slide cùng mục. Vai trò: Nguồn/hướng đọc → bài tập từ giáo trình. Ghi chú định nghĩa trước ví dụ, mở rộng lập luận, cùng ký hiệu với slide.

## Các bổ sung trong bản hiện hành

Trang lợi ích s02-01a nằm sau mở mục 2.2, trước vết đếm từ; cơ chế chi tiết ở 06–07b. Bốn trang đặc tả/đánh giá mới là s02-03c, s02-04b, s03-03a và s06-03b. Tổng hiện hành 62 trang = 54 giảng + 8 bài tập; mục 2.2 có 34 phút, toàn bài 120+60 phút theo bảng và từng trang phía trên. Phân bổ của lần thêm lợi ích trước đây được lưu trong review-log, không dùng làm ngân sách hiện hành.

Đặc tả ma trận làm rõ tọa độ duy nhất và đầu ra hàng rỗng; đặc tả ảnh quy định mã 1..N và cặp i<j. Bộ kết hợp có phân tích số tổng cục bộ và bộ nhớ bảng trong ghi chú. Lời giải Bài 2.3.1 bổ sung bảng đặc tả/đánh giá, giữ nguyên đề. Các đại lượng bộ nhớ phụ không gồm vùng đầu vào và quản lý hệ thống. Không thêm SVG vì bốn trang mới dùng bảng HTML để đối chiếu các bước với phép đếm; giữ các hình đã có ở những phần khác; phần 2.4 dùng bốn hình mới.

## Quyết định viết lại 2.4 — 2026-09-16

Thay toàn bộ5trang cũ bằng9trang theo kế hoạch outline, giữ ID01–05 và thêm06–09. Hình f,g,h,i,j không còn dùng; hình chuỗi Spark cũ thay bằng ví dụ A/B. Phần2.4=18phút; ngân sách và từng trang phía trên là hiện hành. Bài tập60phút không đổi. Cơ chế hệ thống không tạo chứng minh mới; thuật toán lọc/đếm dùng lại chứng minh đếm từ. Các bước thực thi và đánh giá được phân bố qua ví dụ, giả mã, lưu đệm, khôi phục và nối sang2.5.

## Lần sửa 2.5–2.6: bản đồ chủ đề và ngoại lệ cục bộ

2.5 thực hiện mục tiêu đánh giá: biết thuật toán nhận dữ liệu ở đâu → chọn đơn vị → đếm từng khoản → cộng tổng → phân biệt tổng với tải lớn nhất. 2.6 thực hiện mục tiêu thiết kế: từ tải lớn nhất → đặc tả ảnh → gửi từng cặp → đếm bản gửi → đặt tên đại lượng → thay cách phân chia → kiểm tra tính đúng và đánh đổi. Không đưa q/rho lên trước ví dụ.

Các chủ đề cốt lõi gồm mô hình đầu vào, thuật toán từng cặp/nhóm và đánh giá. Cầu nối là hình bốn ảnh từ phần sau của sách, chuyển lên trước để khôi phục trực giác, không thêm lý thuyết đồ thị hai phía/cận dưới. Bổ sung là tách phép đọc lặp vector và ba yếu tố byte vốn bị gộp. Nội dung đọc thêm giữ 2.6.3–2.6.7. Không thêm bài tập hoặc dữ kiện thực nghiệm.

Ghi chú tự học ánh xạ: `note-cost-input` ↔ s05-02/01; `note-cost-word` ↔ s05-03/04; `note-cost-matrix` ↔ s05-03a/03c/03b; `note-cost-load` ↔ s05-09; `note-image-pair` ↔ s06-00/02/02a/01; `note-image-group` ↔ s06-03/03c/03d/03a; `note-image-work` ↔ s06-03b/04. Ghi chú mở bằng vai trò rồi định nghĩa; slide ưu tiên quan sát trước ký hiệu. Bước chứng minh không áp dụng cho quy ước đo; thuật toán ảnh có bao phủ, duy nhất và điều kiện dừng. Kiểm tra bằng giải thích khoản chi phí và đánh đổi bộ nhớ, bài2.5.1a giữ nguyên25phút.

Chủ đề cầu nối `note-parallel-time` ↔ s05-09/10: từ tổng chi phí sang thời gian nhận kết quả. Giữ cùng2/3giátrị; c là thời gian giả định mỗi giá trị, không phải ngưỡng tau. 2.6-04 thu hồi điều kiện đủ tác vụ trên số máy có sẵn. Tổng68trang,120+60; phần giảng60trang, không thêm recitation.
