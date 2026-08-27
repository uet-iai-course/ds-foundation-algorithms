# Slide tham khảo cho 15 buổi đề xuất

## Phạm vi và cách dùng

Thư mục này chứa slide tham khảo cho **15 buổi trong bảng “Thứ tự đề xuất” của `sources/source.md`**. Các tệp đủ để lập outline, storyboard và bản nháp nội dung cho cả 15 buổi. Chúng không tự động thay thế giáo trình, chương sách hoặc bài báo gốc khi cần kiểm chứng định lý, bảo đảm xác suất, chứng minh tính đúng hay phân tích độ phức tạp.

Các PDF/PPTX trong bảng chỉ lưu cục bộ và không được theo dõi bởi Git. Tên tệp xác định vị trí cần đặt sau khi tải từ nguồn chính thức ở mục “Nguồn theo khóa học”. Kho từ xa chỉ phát hành bảng ánh xạ và liên kết, không phát hành lại slide của bên thứ ba.

Khi soạn một bài:

1. Đọc mục tương ứng trong `sources/source.md`.
2. Đọc các tệp được ánh xạ trong bảng dưới đây.
3. Kiểm tra lại mệnh đề kỹ thuật bằng giáo trình hoặc nguồn gốc được nêu cho bài.
4. Ghi nguồn đến trang hoặc số slide cụ thể trong outline, storyboard và ghi chú diễn giả.
5. Vẽ lại sơ đồ thành SVG và dựng lại công thức, bảng, giả mã bằng HTML hoặc KaTeX. Không sao chép giao diện, CSS hoặc nguyên trang từ slide tham khảo.

## Đánh giá mức độ đầy đủ

| Buổi đề xuất | Slide cục bộ cần đọc | Phạm vi được hỗ trợ | Kết luận |
|---:|---|---|---|
| 1 | `stanford-cs246/01-intro.pdf` | Bài toán dữ liệu lớn, mô hình chi phí, hệ tệp phân tán và bối cảnh khai phá dữ liệu | Đủ cho bản nháp; dùng MMDS Chương 1 để chốt thuật ngữ và phạm vi |
| 2 | `stanford-cs246/01-intro.pdf` | MapReduce, luồng khóa–giá trị, ví dụ và chi phí truyền thông | Đủ cho bản nháp; dùng MMDS Chương 2 để kiểm chứng mô hình |
| 3 | `stanford-cs246/03-lsh.pdf`; `stanford-cs246/04-lsh_theory.pdf` | Shingling, Jaccard, MinHash và quan hệ xác suất | Đủ cho bản nháp và ví dụ chạy tay; kiểm chứng chứng minh bằng MMDS Chương 3 |
| 4 | `stanford-cs246/03-lsh.pdf`; `stanford-cs246/04-lsh_theory.pdf` | LSH, banding, đường cong ngưỡng và ứng viên giả/bỏ sót | Đủ cho bản nháp và phân tích xác suất ở mức học phần |
| 5 | `stanford-cs246/16-streams.pdf`; `stanford-cs246-2017/streams-2.pdf` | Mô hình dòng, Reservoir Sampling và Bloom Filter | **Đủ có điều kiện:** chưa có nguồn slide phù hợp cho Rejection Sampling; chỉ dạy nội dung này khi bổ sung nguồn, nếu không chuyển thành phần tùy chọn |
| 6 | `stanford-cs246-2017/streams-1.pdf`; `stanford-cs246-2017/streams-2.pdf`; `umass-cs514/lecture8-hyperloglog.pdf`; `umass-cs514/lecture10-count-min.pdf` | Phần tử phân biệt, moment, Flajolet–Martin, HyperLogLog, Count-Min Sketch, cửa sổ và DGIM | Đủ cho bản nháp; phải giảm số thuật toán triển khai đầy đủ nếu storyboard vượt 120 phút |
| 7 | `stanford-cs246/09-pagerank.pdf` | Mô hình PageRank, nút cụt, bẫy nhện, phép lặp và tính toán quy mô lớn | Đủ cho bản nháp và ví dụ chạy tay; dùng MMDS Chương 5 để kiểm chứng ký hiệu |
| 8 | `stanford-cs246/10-spam.pdf` | Topic-Sensitive PageRank, link spam, TrustRank và HITS | Đủ cho bản nháp; giữ thống nhất ký hiệu với buổi 7 |
| 9 | `cmu-15-499/compression1-2.pdf`; `cmu-15-499/compression3.pdf` | Mã tiền tố, Huffman, Arithmetic Coding và giới thiệu Adaptive Huffman | **Đủ có điều kiện:** phần Adaptive Huffman mới ở mức khái quát; cần chương sách hoặc slide chuyên biệt nếu dạy giả mã và lập luận đúng đầy đủ |
| 10 | `mit-15-564/lec3-compression.pdf`; `cmu-15-499/compression3-lz.pdf`; `cmu-15-499/compression4-lossy.pdf` | LZ77, LZ78, LZW, nguyên tắc nén mất dữ liệu và JPEG | Đủ cho bản nháp; dùng *The Data Compression Book* để chốt biến thể thuật toán và đặc tả khôi phục |
| 11 | `db-book-7e/ch12.pptx`; `db-book-7e/ch13.pptx`; `db-book-7e/ch15.pptx`; `wisconsin-cs764/L2-external-sort-replacement-selection.pdf` | Lưu trữ khối, bộ đệm, External Merge Sort, Replacement Selection và mô hình I/O | Đủ cho bản nháp và phân tích lượt I/O |
| 12 | `db-book-7e/ch14.pptx`; `db-book-7e/ch24.pptx` | B-Tree, B+-Tree, băm tĩnh và Bitmap Index | Đủ cho bản nháp; chọn một cấu trúc làm thuật toán trọng tâm để tránh quá tải |
| 13 | `db-book-7e/ch24.pptx`; `db-book-7e/ch31.pptx`; `cornell-cs5780/lecture15-kd-ball-trees.pdf`; `auburn-comp7120/lecture02-spatial-indexing.pdf` | Inverted Index, kd-tree, ball tree, chỉ mục không gian và ánh xạ theo đường cong lấp đầy không gian | Đủ cho bản nháp; phải ghi rõ loại truy vấn và giả thiết hình học của từng cấu trúc |
| 14 | `stanford-biods271/L12-approximate-nearest-neighbor.pdf`; `stanford-cs246/03-lsh.pdf`; `stanford-cs246/04-lsh_theory.pdf` | Tổng quan ANN, LSH, HNSW, Product Quantization, IVF-PQ và FAISS | **Đủ có điều kiện:** đủ cho bài so sánh/tổng quan; cần bài báo gốc HNSW và PQ nếu trình bày bảo đảm, giả mã hoặc phân tích độ phức tạp chi tiết |
| 15 | `db-book-7e/ch15.pptx` | Nested-Loop Join, Sort-Merge Join, Hash Join và Grace Hash Join | Đủ cho bản nháp, ví dụ và mô hình chi phí I/O |

## Nguồn theo khóa học

- **Stanford CS246 — Mining Massive Data Sets:** dùng *Mining of Massive Datasets* làm giáo trình và công bố slide cho MapReduce, LSH, dòng dữ liệu và PageRank. Trang khóa học: <https://web.stanford.edu/class/cs246/>. Bản năm 2017 và học liệu: <https://snap.stanford.edu/class/cs246-2017/handouts.html>.
- **UMass CS514 — Algorithms for Data Science:** dùng các chương của MMDS và có slide riêng về HyperLogLog, Count-Min Sketch. Lịch và học liệu: <https://people.cs.umass.edu/~cmusco/CS514F21/schedule.html>.
- **Database System Concepts, ấn bản 7:** slide chính thức cho các chương lưu trữ, chỉ mục, xử lý truy vấn, chỉ mục nâng cao và truy hồi thông tin. Trang slide: <https://www.db-book.com/slides-dir/index.html>.
- **MIT 15.564 — Information Technology I:** slide tổng quan nén dữ liệu, dùng *The Data Compression Book* làm tài liệu đọc thêm. Tệp nguồn: <https://ocw.mit.edu/courses/15-564-information-technology-i-spring-2003/02e1f182fa2c82b01b4d74e51ceef7d4_lec3.pdf>.
- **CMU 15-499 — Introduction to Data Compression:** slide về mã Huffman, Arithmetic Coding, họ Lempel–Ziv và nén mất dữ liệu. Trang học liệu: <https://www.cs.cmu.edu/afs/cs/project/pscico-guyb/realworld/www/slidesS03.html>.
- **Stanford BIODS 271:** slide tổng quan tìm hàng xóm gần đúng. Tệp nguồn: <https://web.stanford.edu/class/biods271/assets/lectures/L12.pdf>.
- **Wisconsin CS764:** slide về sắp xếp ngoài bộ nhớ và Replacement Selection. Tệp nguồn: <https://pages.cs.wisc.edu/~yxy/cs764-f22/slides/L2-notes.pdf>.
- **Cornell CS5780:** ghi chú về kd-tree và ball tree. Tệp nguồn: <https://www.cs.cornell.edu/courses/cs5780/2024sp/lectures/pdfs/lecturenote15.pdf>.
- **Auburn COMP7120:** slide về chỉ mục không gian và đường cong lấp đầy không gian. Tệp nguồn: <https://www.eng.auburn.edu/~weishinn/Comp7120/Lecture%202.pdf>.

## Giới hạn sử dụng

Các tệp giữ nguyên quyền tác giả và điều kiện sử dụng của nguồn. Slide chính thức của *Database System Concepts* cho phép giảng viên dùng trong học phần có kê giáo trình với yêu cầu ghi công theo trang nguồn. Với mọi bộ slide, chỉ trích phần cần thiết, ghi nguồn cụ thể và không phát hành lại bản dẫn xuất ngoài phạm vi được phép.

Kết luận hiện tại: nguồn cục bộ **đủ để lập dàn ý và bản nháp cho 15 buổi đề xuất**. Trước khi hoàn tất deck, buổi 5 phải xử lý khoảng trống Rejection Sampling; buổi 9 phải bổ sung nguồn nếu dạy Adaptive Huffman đầy đủ; buổi 14 phải dùng bài báo gốc nếu đưa ra bảo đảm hoặc phân tích chi tiết về HNSW và Product Quantization.
