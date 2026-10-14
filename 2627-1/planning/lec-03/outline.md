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
| 2 | Bài toán xếp hạng trang web | Phát biểu bài toán, ví dụ và trực giác | 18 phút |
| 3 | Mô hình và thuật toán PageRank | Hoàn thiện mô hình, thuật toán và tính đúng | 28 phút |
| 4 | Tính PageRank trên đồ thị lớn | Biểu diễn và thuật toán phân tán | 22 phút |
| 5 | Chi phí và lợi ích của cách tính | Đánh giá chi phí | 15 phút |
| 6 | Thực hành tính PageRank | Thực hành | 20 phút |
| 7 | Tổng kết và bài tập vận dụng | Tổng kết, kiểm tra, recitation | 7 phút + 60 phút bài tập |

Tổng giảng chính 120 phút; recitation 60 phút. Bản triển khai có 63 slide, phân bổ theo bảy phần: 6, 8, 16, 10, 9, 7, 7. Phần 6 có nhãn **Thực hành**; phần chứng minh nâng cao hoặc tối ưu ngoài mạch chính, nếu giữ, có nhãn **Đọc thêm**, ghi thời gian riêng. Không chuyển điều kiện đúng hoặc bước cần để code sang đọc thêm.

Từ 2026-10-14, mỗi phần 2–7 mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên mạch trùng từng chữ với cột "Tên trên mục lục"; mạch 1 mở bằng trang bìa. Deck 69 slide.

| N | Trang tiêu đề mạch | Trang mở phần cũ, tiêu đề mới |
|---:|---|---|
| 2 | lec03-s02-00 | lec03-s02-01: Điểm và thứ tự cho mỗi trang |
| 3 | lec03-s03-00 | lec03-s03-01: Chia điểm và bước đi ngẫu nhiên |
| 4 | lec03-s04-00 | lec03-s04-01: Ma trận đặc và danh sách liên kết |
| 5 | lec03-s05-00 | lec03-s05-01: Bốn đại lượng chi phí |
| 6 | lec03-s06-00 | lec03-s06-01: Sản phẩm và môi trường thực hành |
| 7 | lec03-s07-00 | lec03-s07-01: Chuỗi kết quả và giới hạn của PageRank |

Chi tiết mạch, cách thể hiện, đầu ra học tập, nguồn và bài tập: [storyboard.md](storyboard.md).

## Ghi chú tự học đã phát hành

- Bảy chủ đề `lec03-note-01` đến `lec03-note-07` khớp bảy phần slide; bản đồ chi tiết ở cuối storyboard.
- Chủ đề 01–07 là cốt lõi. Giữ cầu nối từ phép chia điểm sang ma trận và từ nhân ma trận sang chia khối; bổ sung các bước chứng minh và lời giải để đọc độc lập. Cận sai số hậu nghiệm chỉ đọc thêm.
- Thay toàn bộ ví dụ cũ y/a/m bằng đồ thị A–D và các biến thể đã dùng trên slide. Giữ bốn bài nguồn và hình 5.4, 5.7; không thêm HITS, TrustRank hoặc nội dung Bài 04.
- Tài liệu tại `materials/lec-03/lecture-note.md`, mã thực hành tại `materials/lec-03/code/`; liên kết trên trang danh mục dùng trình đọc Markdown cục bộ.


## Điều chỉnh cách thể hiện ngày 2026-09-17

Giữ mục tiêu, bảy phần, đồ thị A–D, thuật toán, bài tập và thời lượng. Bổ sung [phân tích trực quan](visual-revision.md) cùng bảng 21 slide được điều chỉnh trong storyboard. Ưu tiên liên hệ đối tượng–thao tác–kết quả: cạnh/cột ma trận, ba nguồn điểm, vết Map/Combine, bảng đếm byte và trạng thái của mã. Kiểm định và trạng thái phát hành ghi tại review-log.md.

## Sửa toàn diện theo chuẩn 2026-10-14

Câu luận đề trên trang bìa (quyết định 3 của điều phối viên, bản 25 token): "Mỗi vòng PageRank là một phép nhân ma trận thưa với véc tơ; bước nhảy và bù nút cụt bảo đảm phép lặp hội tụ."

Phương án A: gộp mạch 1 "Giới thiệu bài học" với mạch 2 "Bài toán xếp hạng trang web"; tách tổng kết và bài tập thành hai section ngoài. Bảng "Bảy phần của bài giảng" phía trên là bản trước đợt sửa.

| Mạch | Tên | Trang (thứ tự deck, mã lịch sử) | Số trang | Phút |
|---|---|---|---:|---:|
| 1 | Bài toán xếp hạng trang web | s01-01, s01-07, s01-03, s01-02, s01-06, s01-04, s01-05, s02-02…s02-08 | 14 | 26,5 |
| 2 | Mô hình và thuật toán PageRank | s03-00…s03-14, s03-16 | 16 | 27 |
| 3 | Tính PageRank trên đồ thị lớn | s04-00, s04-01, s04-02, s03-15, s04-03, s04-11, s04-04…s04-10 | 13 | 23,5 |
| 4 | Chi phí và lợi ích của cách tính | s05-00…s05-09 | 10 | 15 |
| 5 | Thực hành tính PageRank | s06-00…s06-07 | 8 | 20 |
| 6 | Tổng kết và tự kiểm tra | s07-00, s07-02, s07-08, s07-01, s07-03, s07-09 | 6 | 8 |
| 7 | Bài tập vận dụng | s07-T, s07-04…s07-07 | 5 | 60 |

Deck 72 trang (67 giảng + 5 bài tập). Thêm s01-07 "Tiên quyết và quy ước", s04-11 (tách từ s04-03), s07-08 "Thuật toán, bảo đảm và chi phí", s07-09 "Nguồn và tài liệu đọc", s07-T (trang tiêu đề mạch 7); bỏ s02-00, s02-01; đổi vai trò s01-06 (Vấn đề trung tâm), s07-02 (Kết quả và giả thiết không được bỏ), s07-01 (Câu trả lời cho vấn đề trung tâm), s07-03 (Câu hỏi tự kiểm tra). Mười dòng nguồn trên mặt trang chuyển vào ghi chú diễn giả; đề recitation giữ dòng nguồn số bài.

- **Thuật ngữ (Việt – Anh, lần đầu trên mặt trang):** nút cụt (dead end), s03-04; bẫy liên kết (spider trap), s03-05; bước nhảy ngẫu nhiên (teleport), s03-06 (Bài 04 gọi "dịch chuyển"); ma trận liên kết $M_0$ (transition matrix trong ghi chú); bậc ra; danh sách liên kết ra; khối; Combine; băng thông hiệu quả; độ thay đổi $\Delta_t$; bộ nhớ chính (RAM). "véc tơ" thống nhất trong bài (quyết định 7); "MapReduce" theo `sources/source.md` và MMDS, khác "Map-Reduce" của Bài 02 (ghi lệch, không sửa Bài 02).
- **Quy ước:** véc tơ cột; chỉ số trên $t$ đếm vòng; dấu phẩy thập phân; dung lượng bằng byte (điểm 8 byte, mã trang và bậc ra 4 byte); $u_i=1/n$; $\delta^t$ tổng điểm cũ ở nút cụt; $c^t=(1-\beta)+\beta\delta^t$ chỉ dùng ở bảng tổng kết.
- **Trường hợp biên mới (s03-11):** mọi trang là nút cụt cho $\delta=1$, phần chung $1/n$, nên $r^1=u$ và $\Delta=0$; cần tác tử rà toán kiểm (quyết định 4).
- **Ký hiệu chữ $B$:** sau lượt sửa bỏ $B_{ab}$ (khối viết $M_{ab}$); $B$ nghiêng là bộ nhớ ($B$, $B_{\text{task}}$, $B_{\text{buf}}$), B đứng là trang, nêu một lần ở dòng "Ký hiệu:" của s05-01.
- **Ghi chú bài giảng:** không sửa trong đợt này; tác động ghi trong review-log.
- **Lượt sửa sau rà ba vai (2026-10-14).** $u$ (mọi thành phần $1/n$) và dạng véc tơ $r^{t+1}=\beta M_0r^t+((1-\beta)+\beta\delta^t)u$ đặt trên mặt trang s03-08; điểm bất động $r^*=M_0r^*$ (s03-03) và $r^*=F(r^*)$ (s03-14). Ma trận của chứng minh hội tụ là $\bar M$ ($M_0$ có cột nút cụt thay bằng $u$), khớp Bài 04; $S$ chỉ còn nghĩa dung lượng. Dải theo khối $r_b$, $z_a$ phân biệt với giá trị một trang $r_j$, $z_A$ bằng dòng "Ký hiệu:" ở s04-11 (trang đầu dùng dải). s03-15 chuyển sang mạch 3 làm bước trực giác sau s04-02. s07-09 có dòng nối Bài 04.
