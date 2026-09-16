# Bài 03 — Dàn ý triển khai

Trạng thái: Hoàn tất bảy phần, 63 slide (59 slide giảng trong 120 phút và bốn bài tập trong 60 phút), ghi chú tự học và mã Python đã kiểm định. Bản mới thay cấu trúc deck cũ theo yêu cầu.


- Tên bài: **PageRank: mô hình và tính toán**, Bài 03 theo thứ tự đề xuất trong `sources/source.md`; tiếp nối phép nhân ma trận–véc tơ và MapReduce của Bài 02.
- Nguồn chính: MMDS 3e Chương 5, mục 5.1–5.2. Đối chiếu `sources/reference-slides/mmds/ch05-linkanalysis1.pdf` và `sources/reference-slides/stanford-cs246/09-pagerank.pdf`.
- Sinh viên năm 2: biết đồ thị có hướng, xác suất cơ bản và đại số tuyến tính; không giả định đã học chuỗi Markov hoặc cơ sở dữ liệu.
- Đầu ra: giải thích ý nghĩa điểm; lập phép cập nhật; xử lý nút cụt và bẫy liên kết; chạy lặp, kiểm kết quả; mô tả phép tính theo khối/MapReduce; tính chi phí cơ bản và chuyển thuật toán thành Python.
- Để Bài 04 xử lý PageRank theo chủ đề, liên kết rác, TrustRank và HITS. Không mở thêm phần hệ thống Hadoop; dùng lại Bài 02 khi cần.

## Bảy phần của bài giảng

| Phần | Tên trên mục lục | Loại phần | Thời lượng chính dự kiến |
|---|---|---|---:|
| 1 | Giới thiệu bài học | Giới thiệu và động lực | 10 phút |
| 2 | Bài toán Xếp hạng trang web | Phát biểu bài toán, ví dụ và trực giác | 18 phút |
| 3 | Mô hình và thuật toán PageRank | Hoàn thiện mô hình, thuật toán và tính đúng | 28 phút |
| 4 | Tính PageRank trên đồ thị lớn | Biểu diễn và thuật toán phân tán | 22 phút |
| 5 | Chi phí và lợi ích của cách tính | Đánh giá chi phí | 15 phút |
| 6 | Thực hành tính PageRank | Thực hành | 20 phút |
| 7 | Tổng kết và bài tập vận dụng | Tổng kết, kiểm tra, recitation | 7 phút + 60 phút bài tập |

Tổng giảng chính 120 phút; recitation 60 phút. Bản triển khai có 63 slide, phân bổ theo bảy phần: 6, 8, 16, 10, 9, 7, 7. Phần 6 có nhãn **Thực hành**; phần chứng minh nâng cao hoặc tối ưu ngoài mạch chính, nếu giữ, có nhãn **Đọc thêm**, ghi thời gian riêng. Không chuyển điều kiện đúng hoặc bước cần để code sang đọc thêm.


Chi tiết mạch, cách thể hiện, đầu ra học tập, nguồn và bài tập: [storyboard.md](storyboard.md).

## Ghi chú tự học đã phát hành

- Bảy chủ đề `lec03-note-01` đến `lec03-note-07` khớp bảy phần slide; bản đồ chi tiết ở cuối storyboard.
- Chủ đề 01–07 là cốt lõi. Giữ cầu nối từ phép chia điểm sang ma trận và từ nhân ma trận sang chia khối; bổ sung các bước chứng minh và lời giải để đọc độc lập. Cận sai số hậu nghiệm chỉ đọc thêm.
- Thay toàn bộ ví dụ cũ y/a/m bằng đồ thị A–D và các biến thể đã dùng trên slide. Giữ bốn bài nguồn và hình 5.4, 5.7; không thêm HITS, TrustRank hoặc nội dung Bài 04.
- Tài liệu tại `materials/lec-03/lecture-note.md`, mã thực hành tại `materials/lec-03/code/`; liên kết trên trang danh mục dùng trình đọc Markdown cục bộ.
