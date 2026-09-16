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
- **Hiện trạng:** Một dòng “Giới thiệu”.
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
