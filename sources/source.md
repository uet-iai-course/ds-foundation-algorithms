# Nguồn học phần UET.DSE2053

## Phạm vi và nguyên tắc sử dụng

Tệp này chuyển nội dung từ đề cương chi tiết của học phần sang Markdown để làm nguồn chung khi chuẩn bị từng bài giảng. Phần A là bản trích xuất có cấu trúc; phần B là đề xuất biên tập chương trình. Các đề xuất ở phần B không thay thế đề cương đã ban hành.

- Tệp nguồn: `UET_Đề cương học phần_UET.DSE2053_Giải thuật nền tảng cho Khoa học dữ liệu_7460108.01.24.2506.docx`.
- Quy mô nguồn: 11 bảng, 214 hàng và 824 ô.
- Nguồn có 5 ảnh PNG dùng làm dấu đầu dòng; không có hình nội dung cần chuyển sang bài giảng.
- Nội dung và số liệu dưới đây được giữ theo DOCX. Các điểm nghi ngờ được gắn nhãn **[CẦN XÁC MINH]**, không tự sửa.

---

# Phần A. Trích xuất từ đề cương

## I. Thông tin chung

| Trường | Nội dung trong nguồn |
|---|---|
| Tên học phần | Giải thuật nền tảng cho Khoa học dữ liệu (Foundational Algorithms in Data Science) |
| Mã học phần | UET.DSE2053 |
| Số tín chỉ (LT/ThH/BT/TH) | 3 (30/30/0/90) |
| Học phần tiên quyết | UET.CS1058 – Cấu trúc dữ liệu và giải thuật |
| Đơn vị phụ trách | Viện Trí tuệ nhân tạo |

### Mục tiêu học phần

Học phần giúp sinh viên nắm vững và vận dụng được các nguyên lý, mô hình và thuật toán nền tảng trong Khoa học Dữ liệu, tập trung vào các kỹ thuật xử lý dữ liệu quy mô lớn, dữ liệu đồ thị, dòng dữ liệu và dữ liệu nén. Qua đó, sinh viên phát triển năng lực phân tích, đánh giá và triển khai các giải pháp kỹ thuật hiệu quả, có khả năng thích ứng với các thách thức trong môi trường dữ liệu lớn và nhận thức rõ trách nhiệm khi xử lý thông tin trong thực tế.

### Giảng viên

- PGS. TS. Nguyễn Phương Thái, `thainp@vnu.edu.vn`.
- TS. Trần Quốc Long, `tqlong@vnu.edu.vn`.
- TS. Nguyễn Thị Ngọc Diệp, `ngocdiep@vnu.edu.vn`.
- TS. Trần Hồng Việt, `thviet@vnu.edu.vn`.
- ThS. Ngô Minh Hương, `nmhuong@vnu.edu.vn`.

### Học liệu bắt buộc

1. Avrim Blum, John Hopcroft và Ravindran Kannan, *Foundations of Data Science*, Cambridge University Press, 2020.
2. Abraham Silberschatz, Henry Francis Korth và S. Sudarshan, *Database System Concepts*, ấn bản thứ 7, McGraw-Hill Education, 2019.
3. Jure Leskovec, Anand Rajaraman và Jeffrey D. Ullman, *Mining of Massive Datasets*, Cambridge University Press, 2014.
4. Mark Nelson và Jean-loup Gailly, *The Data Compression Book*, ấn bản thứ 2, Wiley, 1995.
5. Giảng viên Trường Đại học Công nghệ, bài giảng của học phần.

### Học liệu tham khảo

1. Mark Nelson và Jean-loup Gailly, *The Data Compression Book*, ấn bản thứ 2, Wiley, 1995.

### Hình thức tổ chức trong nguồn

| Hình thức | Số buổi | Số tiết mỗi buổi | Tuần | Cách tổ chức |
|---|---:|---:|---|---|
| Lý thuyết | 15 | 2 | 1–15 | Học trực tiếp |
| Thực hành | 15 | 2 | 1–15 | Học trực tiếp |
| Tự học | 105 | 7 | 1–15 | Tự đọc tài liệu |

**[CẦN XÁC MINH – thời lượng]** Dòng tín chỉ ghi `3 (30/30/0/90)`, nhưng bảng hình thức tổ chức ghi 105 buổi tự học, mỗi buổi 7 tiết. Cần xác định `105` là số tiết hay số buổi, đồng thời đối chiếu với thành phần tự học `90` trong dòng tín chỉ.

### Yêu cầu của học phần

- Sinh viên cần có kiến thức nền tảng về cấu trúc dữ liệu và giải thuật, cơ sở dữ liệu và xác suất – thống kê.
- Biết lập trình thành thạo một ngôn ngữ như Python hoặc C++.
- Có khả năng đọc hiểu tài liệu chuyên ngành bằng tiếng Anh.
- Có tinh thần tự học, làm việc nhóm và tư duy phản biện trong việc áp dụng giải thuật vào bài toán dữ liệu thực tế.

## II. Chuẩn đầu ra

### Chuẩn đầu ra học phần

Kết thúc học phần, sinh viên có khả năng:

| Mã | Nội dung chuẩn đầu ra |
|---|---|
| CLO1 | Diễn giải (2) được các nguyên lý và thuật toán cơ bản thường được sử dụng trong khoa học dữ liệu, vai trò và ứng dụng của các thuật toán này trong việc giải quyết các bài toán thực tiễn liên quan đến các loại dữ liệu phức tạp. |
| CLO2 | Phân tích (4) được đặc điểm của bài toán dữ liệu quy mô lớn trong các miền như đồ thị web, dữ liệu dòng và tìm kiếm tương đồng, để lựa chọn kỹ thuật hoặc thuật toán phù hợp. |
| CLO3 | Thiết kế và triển khai (4) được giải pháp xử lý dữ liệu hiệu quả bằng cách áp dụng các thuật toán đã học, bảo đảm hiệu suất và độ chính xác trên dữ liệu thực tế. |
| CLO4 | Thể hiện (3) tinh thần học tập nghiêm túc, chủ động tìm hiểu công nghệ mới, có trách nhiệm trong thu thập, xử lý và chia sẻ dữ liệu một cách minh bạch và đúng đạo đức, đặc biệt trong các bài toán liên quan đến dữ liệu lớn và cá nhân. |

### Liên kết CLO–PI/PLO

Các ô có giá trị trong ma trận nguồn:

| CLO | PI liên kết | Mức trong ma trận |
|---|---|---:|
| CLO1 | PI1.3; PI1.4 | 3; 3 |
| CLO2 | PI4.3 | 3 |
| CLO3 | PI4.3 | 3 |
| CLO4 | PI6.3; PI7.2 | 3; 3 |

Mức đóng góp của học phần: PI1.3 và PI1.4 ở mức `I`; PI4.3, PI6.3 và PI7.2 ở mức `R`.

- `I` (Introduced) – Giới thiệu: học phần hỗ trợ ở mức cơ bản, giúp người học bước đầu tiếp cận nội dung liên quan đến PLO/PI.
- `R` (Reinforced) – Củng cố: học phần hỗ trợ ở mức trung bình, người học có nhiều cơ hội được thực hành, thí nghiệm hoặc áp dụng trong thực tiễn.
- `M` (Mastered) – Thành thạo: học phần đóng vai trò then chốt, giúp người học đạt mức thành thạo về một PI quan trọng của PLO, hoặc đạt toàn bộ PLO.

## III. Nội dung giảng dạy theo đề cương

### Danh mục 15 buổi gốc

| Buổi | Chủ đề |
|---:|---|
| 1 | Giới thiệu giải thuật trong khoa học dữ liệu |
| 2 | Thuật toán phác thảo (Sketching) |
| 3 | Thuật toán lấy mẫu (Sampling) |
| 4 | Giải thuật xử lý đồ thị: PageRank và MapReduce |
| 5 | Các biến thể nâng cao của PageRank |
| 6 | Thuật toán xử lý dòng dữ liệu (phần 1) |
| 7 | Thuật toán xử lý dòng dữ liệu (phần 2) |
| 8 | Nén dữ liệu không mất thông tin |
| 9 | Nén dữ liệu bằng từ điển và nén mất dữ liệu |
| 10 | Chỉ mục truyền thống và băm tĩnh |
| 11 | Chỉ mục văn bản và chỉ mục không gian |
| 12 | Băm và ánh xạ gần đúng |
| 13 | Chỉ mục gần đúng hiệu suất cao |
| 14 | Sắp xếp ngoài bộ nhớ |
| 15 | Thuật toán kết nối dữ liệu (Join) |

### Buổi 1. Giới thiệu giải thuật trong khoa học dữ liệu

- **Mô tả:** Vai trò của giải thuật trong khoa học dữ liệu; các bài toán có dữ liệu lớn, đa dạng và không ngừng thay đổi.
- **LLO1:** Nhận biết vai trò của giải thuật trong xử lý dữ liệu quy mô lớn. Phương pháp đánh giá: Quizz. Liên quan CLO1.
- **Đọc trước:** Blum, Hopcroft và Kannan, Chương 1, 2.
- **Bài giảng:** Bài giảng buổi 1.
- **Thảo luận:** Vì sao dữ liệu lớn đòi hỏi các giải thuật và cấu trúc dữ liệu khác với truyền thống?
- **Hoạt động:** Khảo sát một tập dữ liệu thực tế có kích thước lớn; phân tích các vấn đề khi xử lý bằng công cụ thông thường.
- **Đánh giá:** Quiz cuối buổi.
- **Nhắc nhở:** Tìm hiểu trước thuật toán phác thảo.

### Buổi 2. Thuật toán phác thảo (Sketching)

- **Mô tả:** Các thuật toán phác thảo dữ liệu để ước lượng tần suất và phân phối, gồm Count-Min Sketch, Bloom Filter và HyperLogLog.
- **LLO1:** Mô tả nguyên lý và so sánh các kỹ thuật phác thảo dữ liệu. Phương pháp đánh giá: Quizz. Liên quan CLO1.
- **Đọc trước:** Blum, Hopcroft và Kannan, Chương 6.
- **Bài giảng:** Bài giảng buổi 2.
- **Thảo luận:** Tại sao Count-Min Sketch chấp nhận xấp xỉ và được dùng trong các hệ thống thực tế?
- **Hoạt động:** Cài đặt Count-Min Sketch và kiểm tra sai số khi đếm tần suất từ một luồng dữ liệu văn bản lớn.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước thuật toán lấy mẫu.

### Buổi 3. Thuật toán lấy mẫu (Sampling)

- **Mô tả:** Reservoir Sampling, MinHash và Rejection Sampling.
- **LLO1:** Phân tích ưu, nhược điểm của các kỹ thuật lấy mẫu và ứng dụng phù hợp. Phương pháp đánh giá: Quizz. Liên quan CLO2.
- **Đọc trước:** Blum, Hopcroft và Kannan, Chương 6.
- **Bài giảng:** Bài giảng buổi 3.
- **Thảo luận:** MinHash có thể giúp gì trong so sánh tài liệu và phát hiện trùng lặp?
- **Hoạt động:** Cài đặt MinHash để phát hiện tương đồng giữa các tài liệu văn bản.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước PageRank và MapReduce.

### Buổi 4. PageRank và MapReduce

- **Mô tả:** Bài toán đồ thị web, thuật toán PageRank và cách triển khai bằng MapReduce.
- **LLO1:** Trình bày cách hoạt động của PageRank và lập trình xử lý đồ thị lớn. Phương pháp đánh giá: Quizz. Liên quan CLO1, CLO3.
- **Đọc trước:** Leskovec, Rajaraman và Ullman, Chương 5.
- **Bài giảng:** Bài giảng buổi 4.
- **Thảo luận:** Tại sao PageRank cần nhiều vòng lặp? MapReduce hỗ trợ thế nào khi dữ liệu quá lớn?
- **Hoạt động:** Mô phỏng PageRank trên một tập dữ liệu đồ thị web đơn giản.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước các biến thể nâng cao của PageRank.

### Buổi 5. Các biến thể nâng cao của PageRank

- **Mô tả:** Topic-Sensitive PageRank, TrustRank, Spam Mass và HITS.
- **LLO1:** So sánh các thuật toán xếp hạng nút trong đồ thị và phân tích ứng dụng. Phương pháp đánh giá: Quizz. Liên quan CLO2.
- **Đọc trước:** Leskovec, Rajaraman và Ullman, Chương 5.
- **Bài giảng:** Bài giảng buổi 5.
- **Thảo luận:** HITS và PageRank khác nhau thế nào về cách đánh giá độ quan trọng?
- **Hoạt động:** Cài đặt HITS và áp dụng cho một mạng trích dẫn khoa học nhỏ.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước thuật toán xử lý dòng dữ liệu, phần 1.

### Buổi 6. Thuật toán xử lý dòng dữ liệu, phần 1

- **Mô tả:** Bài toán dữ liệu dòng; Flajolet-Martin, AMS và DGIM.
- **LLO1:** Diễn giải các kỹ thuật xử lý dòng dữ liệu và ứng dụng. Phương pháp đánh giá: Quizz. Liên quan CLO1.
- **Đọc trước:** Leskovec, Rajaraman và Ullman, Chương 4.
- **Bài giảng:** Bài giảng buổi 6.
- **Thảo luận:** Dữ liệu dòng khác gì với dữ liệu truyền thống? Tại sao phải chấp nhận sai số?
- **Hoạt động:** Triển khai DGIM để đếm số bit 1 trong cửa sổ trượt.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước thuật toán xử lý dòng dữ liệu, phần 2.

### Buổi 7. Thuật toán xử lý dòng dữ liệu, phần 2

- **Mô tả:** Thuật toán cửa sổ trượt và “kỹ thuật làm cũ”.
- **LLO1:** Thiết kế chiến lược lưu giữ thông tin hiệu quả trong dữ liệu dòng. Phương pháp đánh giá: Quizz. Liên quan CLO3.
- **Đọc trước:** Leskovec, Rajaraman và Ullman, Chương 4.
- **Bài giảng:** Bài giảng buổi 7.
- **Thảo luận:** Có nên lưu toàn bộ dữ liệu? Làm sao để không bị tràn bộ nhớ?
- **Hoạt động:** Lập trình hệ thống đếm từ xuất hiện gần nhất bằng kỹ thuật cửa sổ trượt.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước nén dữ liệu không mất thông tin.

**[CẦN XÁC MINH – thuật ngữ]** Nguồn dùng cụm “kỹ thuật làm cũ”. Cần đối chiếu bản bài giảng hoặc học liệu để xác định thuật ngữ gốc và nghĩa dự kiến trước khi soạn trang chiếu.

### Buổi 8. Nén dữ liệu không mất thông tin

- **Mô tả:** Huffman, Adaptive Huffman và Arithmetic Coding.
- **LLO1:** Phân tích cách các thuật toán nén làm giảm kích thước dữ liệu mà không mất thông tin. Phương pháp đánh giá: Quizz. Liên quan CLO1.
- **Đọc trước:** Nelson và Gailly, Chương 3, 4, 5.
- **Bài giảng:** Bài giảng buổi 8.
- **Thảo luận:** Tại sao Huffman hiệu quả với dữ liệu có phân phối lệch?
- **Hoạt động:** Cài đặt Huffman cho dữ liệu văn bản đầu vào.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước nén bằng từ điển và nén mất dữ liệu.

### Buổi 9. Nén bằng từ điển và nén mất dữ liệu

- **Mô tả:** LZ77, LZ78, LZW và nén mất dữ liệu như JPEG.
- **LLO1:** So sánh kỹ thuật nén từ điển và nén mất dữ liệu; lựa chọn ứng dụng phù hợp. Phương pháp đánh giá: Quizz. Liên quan CLO2.
- **Đọc trước:** Nelson và Gailly, Chương 8, 9, 10, 11.
- **Bài giảng:** Bài giảng buổi 9.
- **Thảo luận:** Khi nào nên dùng nén mất dữ liệu? Có an toàn cho ảnh y tế không?
- **Hoạt động:** Áp dụng LZW cho văn bản và thử nén ảnh bằng mã hóa JPEG.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước chỉ mục truyền thống và băm tĩnh.

### Buổi 10. Chỉ mục truyền thống và băm tĩnh

- **Mô tả:** B+-Tree, B-Tree, băm tĩnh và Bitmap Index.
- **LLO1:** Trình bày nguyên lý và ứng dụng của các cấu trúc chỉ mục. Phương pháp đánh giá: Quizz. Liên quan CLO1.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 14; Leskovec, Rajaraman và Ullman, Chương 3.
- **Bài giảng:** Bài giảng buổi 10.
- **Thảo luận:** B+-Tree có lợi gì khi dùng với ổ đĩa? Khi nào dùng Bitmap Index?
- **Hoạt động:** Mô phỏng tìm kiếm và chèn trong cây B+-Tree.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước chỉ mục văn bản và chỉ mục không gian.

### Buổi 11. Chỉ mục văn bản và chỉ mục không gian

- **Mô tả:** Inverted Index, Full-Text Search, kd-tree và ball tree.
- **LLO1:** Hiểu cấu trúc và cách xây dựng các loại chỉ mục chuyên biệt. Phương pháp đánh giá: Quizz. Liên quan CLO1, CLO3.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 14; Leskovec, Rajaraman và Ullman, Chương 3.
- **Bài giảng:** Bài giảng buổi 11.
- **Thảo luận:** Inverted Index hỗ trợ tìm kiếm thế nào? Khi nào dùng kd-tree?
- **Hoạt động:** Xây dựng chỉ mục đảo cho một tập văn bản và tìm kiếm từ khóa.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước băm và ánh xạ gần đúng.

### Buổi 12. Băm và ánh xạ gần đúng

- **Mô tả:** Shingling, Minhashing, Locality-Sensitive Hashing (LSH), Z-order Curve và Space-Filling Curve.
- **LLO1:** Giải thích cơ chế ánh xạ dữ liệu để tìm tương đồng hiệu quả. Phương pháp đánh giá: Quizz. Liên quan CLO2.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 14; Leskovec, Rajaraman và Ullman, Chương 3.
- **Bài giảng:** Bài giảng buổi 12.
- **Thảo luận:** LSH giúp tiết kiệm thời gian tìm kiếm thế nào?
- **Hoạt động:** So sánh tìm cặp tài liệu giống nhau bằng duyệt tuyến tính và Minhash + LSH.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước chỉ mục gần đúng hiệu suất cao.

**[CẦN XÁC MINH – nội dung trùng]** MinHash xuất hiện ở cả buổi 3 và buổi 12. Cần phân định mức giới thiệu ở buổi 3 và mức hình thức hóa cùng Shingling/LSH ở buổi 12, hoặc chuyển toàn bộ MinHash về một cụm.

### Buổi 13. Chỉ mục gần đúng hiệu suất cao

- **Mô tả:** Approximate Nearest Neighbor (ANN), Hierarchical Navigable Small World (HNSW) và Product Quantization (PQ).
- **LLO1:** Đánh giá các kỹ thuật tìm hàng xóm gần đúng trong dữ liệu lớn. Phương pháp đánh giá: Quizz. Liên quan CLO1, CLO3.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 14; Leskovec, Rajaraman và Ullman, Chương 3.
- **Bài giảng:** Bài giảng buổi 13.
- **Thảo luận:** Tại sao không thể dùng duyệt tuyến tính để tìm tương đồng với dữ liệu lớn?
- **Hoạt động:** Dùng FAISS để tìm ảnh tương tự trong một tập ảnh.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước sắp xếp ngoài bộ nhớ.

**[CẦN XÁC MINH – học liệu]** Cần kiểm tra Chương 14 của *Database System Concepts* và Chương 3 của *Mining of Massive Datasets* có bao phủ ANN, HNSW, PQ và FAISS ở mức mà buổi học yêu cầu hay không. Nếu không, đề cương cần chỉ rõ học liệu bổ sung.

### Buổi 14. Sắp xếp ngoài bộ nhớ

- **Mô tả:** External Merge Sort và Replacement Selection cho dữ liệu không vừa bộ nhớ.
- **LLO1:** Trình bày và áp dụng thuật toán sắp xếp ngoài bộ nhớ hiệu quả. Phương pháp đánh giá: Quizz. Liên quan CLO1, CLO3.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 15.
- **Bài giảng:** Bài giảng buổi 14.
- **Thảo luận:** Vì sao phải chia nhỏ dữ liệu để sắp xếp? Có bao nhiêu lần đọc/ghi đĩa là tối ưu?
- **Hoạt động:** Triển khai External Merge Sort cho tập dữ liệu lớn hơn RAM.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Tìm hiểu trước thuật toán kết nối dữ liệu.

### Buổi 15. Thuật toán kết nối dữ liệu (Join)

- **Mô tả:** Nested-Loop Join, Sort-Merge Join, Hash Join và Grace Hash Join.
- **LLO1:** So sánh các thuật toán kết nối và phân tích hiệu quả trên dữ liệu lớn. Phương pháp đánh giá: Quizz. Liên quan CLO2, CLO3.
- **Đọc trước:** Silberschatz, Korth và Sudarshan, Chương 15.
- **Bài giảng:** Bài giảng buổi 15.
- **Thảo luận:** Khi nào dùng Grace Hash Join thay vì Sort-Merge Join?
- **Hoạt động:** Kết nối hai bảng lớn bằng các thuật toán đã học, so sánh hiệu suất và ôn tập thi cuối kỳ.
- **Đánh giá:** Quiz đầu buổi.
- **Nhắc nhở:** Ôn tập thi cuối kỳ.

## IV. Tổ chức giảng dạy và đánh giá

### Tổ chức giảng dạy và hình thức cuối kỳ

| Thành phần | Số giờ mỗi buổi | Số buổi | Tuần học | Ghi nhận trong nguồn |
|---|---:|---:|---|---|
| Lý thuyết | 2 | 15 | 1–15 | Có |
| Bài tập chia lớp | Không ghi | Không ghi | Không ghi | Để trống |
| Thực hành chia lớp | 2 | 15 | 1–15 | Có |
| Đánh giá cuối kỳ | — | — | — | Đánh dấu `x` tại cột `TL` |

**[CẦN XÁC MINH – viết tắt]** Dấu `x` nằm tại cột `TL`, nhưng đề cương không giải thích chữ viết tắt này. Cần xác nhận cách diễn giải chính thức.

### Kế hoạch đánh giá

| Hình thức | Phương pháp | Thời điểm | Thang điểm | Trọng số học phần | Phân bổ CLO trong nguồn | Công cụ |
|---|---|---|---:|---:|---|---|
| Kiểm tra đánh giá thường xuyên: sự chuyên cần, tinh thần học tập | Quizz | Tại mỗi buổi học | 10 | 20% | CLO1: 50%; CLO4: 50% | Rubric đánh giá chuyên cần |
| Đánh giá bài tập nhóm | Bài tập nhóm | Tại một vài buổi học | 10 | 20% | CLO3: 90%; CLO4: 10% | Rubric đánh giá bài tập nhóm |
| Thi cuối kỳ | Bài kiểm tra cuối kì | Cuối kỳ | 10 | 60% | CLO1: 50%; CLO2: 30%; CLO3: 20%; CLO4: 20% | Rubric đánh giá cuối kỳ |

**[CẦN XÁC MINH – trọng số]** Phân bổ CLO của thi cuối kỳ trong bảng kế hoạch cộng thành 120%. Rubric cuối kỳ lại ghi CLO4 có trọng số 0%. Hai phần chưa khớp nhau.

### Rubric đánh giá chuyên cần

| Tiêu chí | CLO | Trọng số | Điểm tối đa | Đạt quá yêu cầu | Đạt | Gần đạt | Không đạt |
|---|---|---:|---:|---|---|---|---|
| Mức độ tham gia theo thời khóa biểu và trung thực trong học tập | CLO4 | 50% | 5 | 10,0 → 8,4; tham dự 80–90% buổi học | 8,4 → 7,0; tham dự 80–90% buổi học | 7,0 → 4,0; tham dự khoảng 70% buổi học | 4,0 → 0; tham dự dưới 70% buổi học |
| Mức độ hiểu kiến thức | CLO1 | 50% | 5 | 10,0 → 8,4 | 8,4 → 7,0 | 7,0 → 4,0 | 4,0 → 0 |

**[CẦN XÁC MINH – rubric]** Hai mức “Đạt quá yêu cầu” và “Đạt” của tiêu chí tham gia cùng ghi “tham dự 80–90% buổi học”. Các khoảng điểm cũng dùng chung mốc 8,4 và 7,0 ở hai mức liền nhau.

### Rubric đánh giá bài tập nhóm

| Tiêu chí | CLO | Trọng số | Điểm tối đa | Đạt quá yêu cầu | Đạt | Gần đạt | Không đạt |
|---|---|---:|---:|---|---|---|---|
| Xây dựng một bài toán khoa học dữ liệu đơn giản, áp dụng một số nội dung kiến thức hoặc thuật toán đã học | CLO3 | 90% | 9 | 10,0 → 8,0 | 8,0 → 6,0 | 6,0 → 4,0 | 4,0 → 0 |
| Trung thực trong học tập | CLO4 | 10% | 1 | 10,0 → 8,0 | 8,0 → 6,0 | 6,0 → 4,0 | 4,0 → 0 |

### Rubric đánh giá cuối kỳ

| Tiêu chí | CLO | Trọng số | Điểm tối đa | Đạt quá yêu cầu | Đạt | Gần đạt | Không đạt |
|---|---|---:|---:|---|---|---|---|
| Diễn giải được kiến thức lý thuyết | CLO1 | 50% | 5 | 10,0 → 8,0 | 8,0 → 6,0 | 6,0 → 4,0 | 4,0 → 0 |
| Phân loại được bài toán, chỉ ra thuật toán, mô hình phù hợp | CLO2 | 30% | 3 | 10,0 → 8,0 | 8,0 → 6,0 | 6,0 → 4,0 | 4,0 → 0 |
| Thiết kế được giải pháp sơ bộ cho một ứng dụng đơn giản | CLO3 | 20% | 2 | 10,0 → 8,0 | 8,0 → 6,0 | 6,0 → 4,0 | 4,0 → 0 |
| Không gian lận trong thi cử | CLO4 | 0% | 0 | Mức 1 – Đạt quá yêu cầu (>70%) | Mức 2 – Đạt (≈70%) | Mức 3 – Gần đạt (>40%) | Mức 4 – Không đạt (<40%) |

**[CẦN XÁC MINH – liên kết CLO4]** CLO4 không xuất hiện trong LLO của 15 buổi, dù được đánh giá qua chuyên cần, bài tập nhóm và bảng kế hoạch thi cuối kỳ. Cần xác định LLO hoặc hoạt động nào cung cấp bằng chứng trực tiếp cho trách nhiệm, minh bạch và đạo đức dữ liệu.

---

# Phần B. Biên tập đề xuất cho chuỗi bài giảng

## Giáo trình trục và sách bổ trợ

Đề xuất này giữ 15 buổi và phạm vi của đề cương, nhưng sắp lại quan hệ tiên quyết. Năm chương đầu của *Mining of Massive Datasets*, ấn bản thứ 3 (MMDS 3e), tạo trục cho phần dữ liệu lớn:

1. Chương 1: Data Mining.
2. Chương 2: MapReduce and the New Software Stack.
3. Chương 3: Finding Similar Items, gồm Shingling, MinHash, Locality-Sensitive Hashing (LSH) và độ đo khoảng cách.
4. Chương 4: Mining Data Streams, gồm mô hình dòng, lấy mẫu, lọc, đếm phần tử phân biệt, mômen, cửa sổ và suy giảm.
5. Chương 5: Link Analysis, gồm PageRank, tính PageRank hiệu quả, Topic-Sensitive PageRank, link spam và HITS.

Nguồn kiểm tra cấu trúc: [Mining of Massive Datasets](https://www.mmds.org/) và [mục lục do Cambridge University Press công bố](https://assets.cambridge.org/97811084/76348/toc/9781108476348_toc.pdf).

Các mô-đun sau không thuộc trục năm chương trên và cần sách bổ trợ:

- Nén dữ liệu: Nelson và Gailly, *The Data Compression Book*, theo các chương đã ghi trong đề cương.
- Lưu trữ, sắp xếp ngoài bộ nhớ, chỉ mục và Join: Silberschatz, Korth và Sudarshan, *Database System Concepts*, ấn bản thứ 7. Cấu trúc sách chính thức gồm Chương 12 về lưu trữ vật lý, Chương 13 về cấu trúc lưu trữ, Chương 14 về chỉ mục, Chương 15 về xử lý truy vấn, Chương 24 về chỉ mục nâng cao và Chương 31 về truy hồi thông tin. Nguồn: [Database System Concepts](https://www.db-book.com/).
- Count-Min Sketch có slide bổ trợ từ UMass CS514. Tệp UMass mang tên HyperLogLog chỉ đủ đối chiếu trực giác FM/LogLog, chưa đủ để dạy cơ chế HyperLogLog chuẩn. Bài 7 dùng Stanford BIODS 271 để đặt bối cảnh, giáo trình Princeton COS 597A cho cơ chế và bài tập, cùng bài báo gốc HNSW/PQ để kiểm chứng giả mã, giả thiết và kết luận. Rejection Sampling chưa có nguồn slide phù hợp và chỉ nên giữ khi bổ sung được nguồn đã kiểm chứng.

Slide bổ trợ đã tải và bảng ánh xạ theo từng buổi nằm tại [`reference-slides/README.md`](reference-slides/README.md). Bảng này cho biết phần nào đủ cho bản nháp và phần nào vẫn cần giáo trình hoặc bài báo gốc trước khi hoàn tất deck.

## Nguyên tắc điều chỉnh

1. Mỗi thuật toán trọng tâm bắt đầu bằng một tình huống sử dụng trên dữ liệu lớn. Tình huống phải nêu loại dữ liệu, giới hạn khiến cách xử lý trực tiếp không phù hợp và đầu ra cần tính. Chỉ dùng quy mô định lượng khi tài liệu có nguồn; không bịa số liệu để tạo kịch tính.
2. Dùng năm chương đầu của MMDS 3e làm trục nội dung; sắp theo mạch Chương 1→2→5→3→4 để các bài phân tán–xếp hạng và tương đồng–hàng xóm gần không bị ngắt quãng.
3. Tách MapReduce khỏi PageRank: dạy mô hình xử lý phân tán trước, rồi dùng lại khi tính PageRank.
4. Đặt MinHash cạnh Shingling và LSH; không dạy lặp trong bài lấy mẫu.
5. Nêu mô hình dòng trước lấy mẫu, lọc và phác thảo; gom DGIM với cửa sổ trượt.
6. Đặt Z-order Curve và Space-Filling Curve cạnh chỉ mục không gian.
7. Giới thiệu mô hình chi phí I/O và sắp xếp ngoài bộ nhớ trước B+-Tree, Sort-Merge Join và Grace Hash Join.
8. Giữ hai buổi nén liền nhau; không thay đổi tổng số buổi.

## Năm mạch học tập

Bài 1 là nền chung. Mười bốn bài còn lại được xếp liền nhau theo năm mạch; không xen một bài thuộc mạch khác vào giữa mạch:

1. **Xử lý phân tán và xếp hạng:** Bài 2–4.
2. **Tương đồng và hàng xóm gần:** Bài 5–7.
3. **Dòng dữ liệu và cửa sổ:** Bài 8–9.
4. **Nén dữ liệu và từ điển:** Bài 10–11.
5. **Lưu trữ, chỉ mục và kết nối:** Bài 12–15.

Bài hàng xóm gần được đặt ngay sau LSH; vì vậy phải giới thiệu đủ biểu diễn vector, độ đo khoảng cách và đồ thị lân cận trong chính mạch Bài 5–7, không phụ thuộc vào mạch chỉ mục lưu trữ. Bảng “Ánh xạ thứ tự gốc sang đề xuất” bên dưới chỉ ánh xạ từ 15 buổi trong đề cương gốc sang thứ tự mới.

## Tình huống dữ liệu lớn mở đầu mỗi buổi đề xuất

Các tình huống dưới đây định hướng phần mở bài ở cấp buổi. Chúng không thay cho tình huống riêng của từng thuật toán trọng tâm. Khi tạo trang chiếu, phải đối chiếu với tài liệu chi tiết và thay bằng trường hợp có dữ liệu, giả thiết hoặc bằng chứng cụ thể hơn nếu nguồn cung cấp.

| Buổi | Tình huống mở bài | Giới hạn tạo nhu cầu thuật toán |
|---:|---|---|
| 1 | Phân tích một kho nhật ký hoặc tập dữ liệu không vừa bộ nhớ của một máy | Không thể giả định truy cập ngẫu nhiên nhanh hoặc quét lặp lại tùy ý |
| 2 | Xây dựng chỉ mục hoặc tổng hợp thống kê từ dữ liệu phân tán trên nhiều máy | Chi phí truyền dữ liệu và đồng bộ có thể lớn hơn chi phí tính cục bộ |
| 3 | Xếp hạng các trang trong đồ thị liên kết web lớn | Ma trận liên kết thưa nhưng quá lớn để xử lý như ma trận đặc trên một máy |
| 4 | Xếp hạng theo chủ đề và giảm tác động của liên kết rác | Một điểm PageRank toàn cục không phản ánh mọi ngữ cảnh truy vấn và có thể bị thao túng |
| 5 | Phát hiện tài liệu hoặc trang web gần trùng trong một kho văn bản lớn | So sánh từng cặp tạo số phép so sánh bậc hai |
| 6 | Tìm nhanh các cặp tài liệu có khả năng tương đồng cao | Không thể tính độ tương đồng chính xác cho mọi cặp ứng viên |
| 7 | Tìm hàng xóm gần cho vector biểu diễn trong một kho lớn | Duyệt tuyến tính cho mỗi truy vấn không đáp ứng yêu cầu thời gian; cần đánh đổi độ chính xác, bộ nhớ và độ trễ |
| 8 | Lấy mẫu và loại nhanh phần tử không liên quan từ dòng sự kiện đến liên tục | Không biết trước độ dài dòng và không thể lưu toàn bộ dữ liệu |
| 9 | Đếm phần tử phân biệt, tần suất, mômen và sự kiện gần đây trong dòng dữ liệu | Bộ nhớ hữu hạn và yêu cầu xử lý một lượt buộc phải chấp nhận xấp xỉ có kiểm soát |
| 10 | Lưu trữ hoặc truyền một kho văn bản và nhật ký lớn mà phải khôi phục đúng từng bit | Dung lượng và băng thông hạn chế nhưng không cho phép mất thông tin |
| 11 | Nén kho văn bản lặp mẫu và kho ảnh lớn có yêu cầu chất lượng khác nhau | Một mô hình nén duy nhất không phù hợp đồng thời với dữ liệu ký hiệu và dữ liệu cảm nhận |
| 12 | Sắp xếp một tệp dữ liệu lớn hơn bộ nhớ chính | Thuật toán sắp xếp trong RAM không áp dụng; số lượt đọc và ghi khối chi phối chi phí |
| 13 | Tra cứu khóa trong một bảng lớn lưu trên thiết bị khối | Quét toàn bộ bảng cho mỗi truy vấn gây quá nhiều thao tác I/O |
| 14 | Tìm từ khóa hoặc đối tượng gần một vị trí trong kho văn bản và dữ liệu không gian lớn | Cùng một thứ tự tuyến tính không hỗ trợ hiệu quả cả truy vấn văn bản và truy vấn lân cận |
| 15 | Kết nối bảng sự kiện với bảng thực thể khi cả hai không vừa bộ nhớ | Nested-Loop Join trực tiếp gây quá nhiều lượt I/O; cần khai thác sắp xếp, băm hoặc chỉ mục |

## Mục tiêu, tiên quyết và học liệu của từng bài đề xuất

Bảng này là đặc tả biên tập, không phải nội dung nguyên văn của đề cương. Mỗi lần soạn bài phải đọc cả phần trích xuất của các buổi gốc được ánh xạ và phần học liệu dưới đây.

| Bài | Sản phẩm học tập chính | Kiến thức đầu vào | Học liệu phải kiểm tra |
|---:|---|---|---|
| 1 | Phân biệt đặc tả bài toán, biểu diễn dữ liệu, thuật toán và mô hình chi phí trong bối cảnh dữ liệu lớn | Cấu trúc dữ liệu, phân tích độ phức tạp và xác suất cơ bản | MMDS 3e, Chương 1; Blum, Hopcroft và Kannan, Chương 1–2 |
| 2 | Mô tả mô hình MapReduce, thiết kế các bước map/reduce và phân tích chi phí truyền thông ở mức nguồn yêu cầu | Bài 1; ánh xạ khóa–giá trị và phép nhóm | MMDS 3e, Chương 2 |
| 3 | Lập phương trình PageRank, xử lý nút cụt và tính lặp PageRank trên đồ thị nhỏ trước khi mở rộng | Bài 2; đồ thị có hướng, đại số tuyến tính và phân phối xác suất | MMDS 3e, Chương 5, mục 5.1–5.2 |
| 4 | So sánh Topic-Sensitive PageRank, cơ chế xử lý link spam và HITS theo mục tiêu xếp hạng | Bài 3 và ký hiệu PageRank đã thống nhất | MMDS 3e, Chương 5, mục 5.3–5.5 |
| 5 | Tạo shingle, tính độ tương đồng Jaccard và giải thích vì sao chữ ký MinHash bảo toàn xác suất tương đồng | Băm, tập hợp, vector và xác suất cơ bản | MMDS 3e, Chương 3, mục 3.1–3.3 |
| 6 | Dùng Locality-Sensitive Hashing để tạo tập ứng viên và phân tích đánh đổi giữa bỏ sót với ứng viên giả | Bài 5; xác suất của nhiều hàm băm và độ đo khoảng cách | MMDS 3e, Chương 3, mục 3.4–3.8 |
| 7 | So sánh LSH, HNSW và PQ theo chất lượng kết quả, thời gian truy vấn, thời gian xây dựng và bộ nhớ | Bài 5–6; vector, độ đo khoảng cách và đồ thị cơ bản | MMDS 3e, Chương 3; slide Stanford BIODS 271 trong `reference-slides/`; bài báo gốc nếu dạy bảo đảm hoặc phân tích chi tiết |
| 8 | Đặc tả mô hình dòng, thực hiện lấy mẫu theo khóa và lấy mẫu hồ chứa, giải thích cơ chế lọc xác suất | Bài 1; xác suất, băm và bất biến vòng lặp | MMDS Chương 4, mục 4.1–4.3; slide MMDS/Stanford trong `reference-slides/`; bài tập trực tiếp 4.2.1 và 4.3.1–4.3.3; loại Rejection Sampling vì chưa có nguồn |
| 9 | Chọn cấu trúc tóm tắt theo đại lượng cần ước lượng; nêu sai số, bộ nhớ và phạm vi truy vấn cửa sổ | Bài 8; biến ngẫu nhiên, kỳ vọng và xác suất va chạm băm | Bản cục bộ MMDS Chương 4, mục 4.4–4.7; slide MMDS/Stanford và UMass Count-Min trong `reference-slides/`; bài tập trực tiếp 4.4.1, 4.5.1, 4.5.3, 4.6.1 và 4.6.3; không dạy HyperLogLog chi tiết vì nguồn hiện có không chứa cơ chế chuẩn |
| 10 | Dựng mã tiền tố, chạy Huffman tĩnh, Huffman thích nghi và mã hóa số học; phân tích điều kiện khôi phục đúng | Cây, hàng đợi ưu tiên và xác suất ký hiệu | Nelson và Gailly, Chương 3–5 làm trục; slide Stanford EE398A, Stanford CS106B và CMU 15-499 trong `reference-slides/` để đối chiếu cách trình bày |
| 11 | So sánh nén từ điển với nén mất dữ liệu theo đặc tả khôi phục, tỷ lệ nén và miền ứng dụng | Bài 10; chuỗi, từ điển và biểu diễn ảnh cơ bản | Nelson và Gailly, Chương 8–11 làm trục; CMU 15-499 logic 5, 6, 13, 16 và lossy 11 dùng trực tiếp cho recitation theo ngoại lệ được phê duyệt ngày 2026-08-28 |
| 12 | Chạy External Merge Sort và phân tích số lượt đọc/ghi theo kích thước bộ nhớ và khối | Merge Sort, tệp, bộ đệm và mô hình I/O | *Database System Concepts* 7e, Chương 12–13 và phần sắp xếp ngoài bộ nhớ của Chương 15; bài tập trực tiếp 15.1, 15.9 và 13.5; Wisconsin CS764 chỉ bổ sung Replacement Selection |
| 13 | So sánh B-Tree, B+-Tree, băm tĩnh và Bitmap Index theo loại truy vấn và chi phí I/O | Bài 12; cây cân bằng và băm | *Database System Concepts* 7e, Chương 14 |
| 14 | Chọn biểu diễn chỉ mục cho truy vấn văn bản hoặc không gian và giải thích giới hạn của từng cấu trúc | Bài 13; vector, khoảng cách và truy vấn phạm vi | *Database System Concepts* 7e, Chương 24 và 31; slide Cornell CS5780 và Auburn COMP7120 trong `reference-slides/`; Chương 31 trực tuyến tại `textbooks/db-book-7e-ch31-information-retrieval.pdf`; lời giải chính thức Bài 25.2–25.3 của ấn bản 6 tại `exercises/db-book-6e/ch25-practice-solutions.pdf` |
| 15 | Chạy và so sánh Nested-Loop Join, Sort-Merge Join, Hash Join và Grace Hash Join theo mô hình I/O | Bài 12–13; quan hệ, băm và sắp xếp ngoài bộ nhớ | *Database System Concepts* 7e, Chương 15 |

## Thứ tự đề xuất

| Buổi đề xuất | Chủ đề đề xuất | Nguồn từ buổi gốc | Điều chỉnh và lý do |
|---:|---|---|---|
| 1 | Bài toán dữ liệu lớn và mô hình thuật toán | 1 | Neo theo MMDS Chương 1; làm rõ kích thước dữ liệu, hạn chế bộ nhớ, chi phí truyền dữ liệu và yêu cầu xấp xỉ. |
| 2 | MapReduce và ngăn xếp xử lý dữ liệu lớn | phần MapReduce của 4 | Neo theo MMDS Chương 2; tách nền tảng tính toán phân tán khỏi PageRank để dùng lại ở các bài sau. |
| 3 | PageRank: mô hình và tính toán | phần PageRank của 4 | Neo theo đầu MMDS Chương 5; dùng lại MapReduce từ buổi 2 khi bàn về tính PageRank trên đồ thị lớn. |
| 4 | Topic-Sensitive PageRank, link spam và HITS | 5 | Neo theo phần còn lại của MMDS Chương 5; giữ ngay sau PageRank cơ sở để dùng lại ký hiệu. |
| 5 | Biểu diễn tương đồng: Shingling và MinHash | 3, một phần 12 | Neo theo nửa đầu MMDS Chương 3; chuyển MinHash khỏi bài lấy mẫu và đặt sau Shingling. |
| 6 | Tìm cặp tương đồng bằng LSH | một phần 12 | Neo theo nửa sau MMDS Chương 3; dùng chữ ký MinHash của buổi 5 và bổ sung độ đo khoảng cách theo phạm vi sách. |
| 7 | Chỉ mục hàng xóm gần đúng | 13 | Nối trực tiếp từ LSH; so sánh LSH, HNSW và PQ. Biểu diễn vector, khoảng cách và đồ thị lân cận phải được cung cấp trong Bài 5–7; không phụ thuộc Bài 14. |
| 8 | Dòng dữ liệu: mô hình, lấy mẫu và lọc | 3, 2, 6 | Neo theo đầu MMDS Chương 4; dạy Reservoir Sampling và Bloom Filter trong mô hình một lượt. |
| 9 | Dòng dữ liệu: đếm, mômen và cửa sổ | 2, 6, 7 | Neo theo phần còn lại của MMDS Chương 4; tổ chức các phác thảo theo đại lượng cần ước lượng. |
| 10 | Nén dữ liệu không mất thông tin | 8 | Mô-đun bổ trợ từ *The Data Compression Book*; giữ Huffman, Adaptive Huffman và Arithmetic Coding. |
| 11 | Nén bằng từ điển và nén mất dữ liệu | 9 | Giữ LZ77, LZ78, LZW và JPEG, nhưng tách rõ hai đặc tả khôi phục dữ liệu. |
| 12 | Mô hình I/O và sắp xếp ngoài bộ nhớ | 14 | Thiết lập khối, lượt đọc/ghi, run và phép trộn cho toàn mạch lưu trữ. |
| 13 | Chỉ mục truyền thống và băm tĩnh | 10 | Dùng mô hình I/O của buổi 12 để phân tích B-Tree, B+-Tree, băm tĩnh và Bitmap Index. |
| 14 | Chỉ mục văn bản và chỉ mục không gian | 11, một phần 12 | Đặt Inverted Index, kd-tree, ball tree, Z-order Curve và Space-Filling Curve trong cùng cụm biểu diễn và truy vấn. |
| 15 | Thuật toán kết nối dữ liệu | 15 | Dùng sắp xếp ngoài bộ nhớ, chỉ mục và băm để phân tích Nested-Loop Join, Sort-Merge Join, Hash Join và Grace Hash Join. |

## Ánh xạ thứ tự gốc sang đề xuất

| Buổi gốc | Vị trí hoặc phạm vi đề xuất | Quyết định |
|---:|---|---|
| 1 | Buổi 1 | Giữ |
| 2 | Buổi 8 và 9 | Tách Bloom Filter sang buổi 8; các cấu trúc ước lượng sang buổi 9 |
| 3 | Buổi 5 và 8 | Tách MinHash sang buổi 5; Reservoir/Rejection Sampling sang buổi 8 |
| 4 | Buổi 2 và 3 | Tách MapReduce sang buổi 2; PageRank sang buổi 3 |
| 5 | Buổi 4 | Giữ liền sau PageRank cơ sở |
| 6 | Buổi 8 và 9 | Tách mô hình dòng sang buổi 8; các thuật toán đếm và cửa sổ sang buổi 9 |
| 7 | Buổi 9 | Gộp với cụm cửa sổ và decay |
| 8 | Buổi 10 | Giữ nội dung và quan hệ trước–sau |
| 9 | Buổi 11 | Giữ nội dung và quan hệ trước–sau |
| 10 | Buổi 13 | Đặt sau mô hình I/O và sắp xếp ngoài bộ nhớ |
| 11 | Buổi 14 | Giữ; nhận thêm Z-order và Space-Filling Curve |
| 12 | Buổi 5, 6 và 14 | Tách theo ba vai trò: chữ ký MinHash, truy hồi bằng LSH, ánh xạ không gian |
| 13 | Buổi 7 | Đặt ngay sau LSH trong mạch tương đồng và hàng xóm gần |
| 14 | Buổi 12 | Mở mạch lưu trữ, chỉ mục và kết nối |
| 15 | Buổi 15 | Giữ; hưởng lợi từ các tiên quyết đã sắp lại |

## Quan hệ tiên quyết sau điều chỉnh

- Buổi 1 → buổi 2: bài toán dữ liệu lớn → mô hình xử lý phân tán.
- Buổi 2 → buổi 3 → buổi 4: MapReduce → PageRank cơ sở → các biến thể xếp hạng.
- Buổi 5 → buổi 6 → buổi 7: Shingling và MinHash → LSH → HNSW/PQ và tìm hàng xóm gần đúng.
- Buổi 8 → buổi 9: mô hình dòng, lấy mẫu và lọc → ước lượng mômen và cửa sổ trượt.
- Buổi 10 → buổi 11: mã dựa trên xác suất → từ điển và nén mất dữ liệu.
- Buổi 12 → buổi 13 → buổi 14: mô hình I/O và sắp xếp ngoài → chỉ mục trên đĩa → chỉ mục chuyên biệt.
- Buổi 12–13 → buổi 15: mô hình I/O, sắp xếp ngoài và băm → Join.

## Việc cần xác minh trước khi tạo từng bộ trang chiếu

1. Xác nhận số tiết tự học: `90` hay `105`, và đơn vị của `105`.
2. Xác nhận cách diễn giải chữ viết tắt `TL` của hình thức thi cuối kỳ.
3. Sửa hoặc xác nhận phân bổ CLO của thi cuối kỳ đang cộng thành 120%.
4. Phân biệt hai mức tham dự cùng ghi 80–90% trong rubric chuyên cần.
5. Xác định thuật ngữ gốc của “kỹ thuật làm cũ”.
6. Chỉ rõ cách CLO4 được dạy và thu thập minh chứng trong các LLO/hoạt động của 15 buổi.
7. Với buổi 7, bổ sung bài báo gốc HNSW và PQ nếu deck trình bày giả mã, bảo đảm hoặc phân tích độ phức tạp chi tiết.
8. Khi lập kế hoạch chi tiết, kiểm tra tải nội dung của buổi 9 sau khi gom các thuật toán đếm và cửa sổ. Nếu vượt thời lượng, giảm số thuật toán triển khai đầy đủ; không thu nhỏ phần đặc tả, sai số và ví dụ chạy tay.
9. Xác nhận việc tách MapReduce khỏi bài PageRank có phù hợp với phân công giảng dạy và lịch thực hành hiện hành.
