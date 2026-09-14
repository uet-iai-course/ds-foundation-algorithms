# Storyboard Bài 02: MapReduce và ngăn xếp xử lý dữ liệu lớn

## Bản sửa theo tiêu chuẩn biên soạn — 2026-09-14

Áp dụng [slide_authoring_standard.md](../../../slide_authoring_standard.md) và [AGENTS.md](../../../AGENTS.md). Sinh viên năm 2 đã biết lập trình, tổng hữu hạn và nhân ma trận cơ bản; không mặc định đã học hệ phân tán, đại số quan hệ hoặc Spark. Nguồn chính [ch2n.pdf](../../../sources/textbooks/ch2n.pdf), MMDS Chương 2, 60 trang PDF, trang in 20–79. Trang PDF = trang in −19. Phạm vi theo Bài 2 của sources/source.md; PageRank thuộc Bài 3.

Bản này thay storyboard trước tiêu chuẩn. Mỗi section ngoài sau mở đầu tương ứng một mục 2.1–2.8 của PDF theo yêu cầu trực tiếp của người dùng: 9 section là ngoại lệ có căn cứ đối với quy định 5–7. Có **52 trang giảng, 9 trang bài tập; 120 phút giảng và 60 phút recitation**. Thời lượng là dự kiến, chưa được diễn tập với lớp thật.

Bài tập giữ nguyên dữ kiện/yêu cầu nguồn, chỉ dịch và tách ý: 2.2.1(a–c), trang 30/PDF 11 (15 phút); 2.3.1(a–d), trang 40/PDF 21 (20 phút); 2.5.1(a,c), trang 59/PDF 40 (25 phút). Bài tập đặt cuối section nguồn, dùng liên kết từ tổng kết/tài liệu tham khảo để học sau phần giảng. Đây là ngoại lệ vị trí recitation nhằm giữ ánh xạ section–PDF. Khi giảng, phím phải chuyển sang section tiếp theo trước cụm bài tập; phần luyện tập đi theo liên kết cuối mỗi cụm. Mọi bài có sản phẩm yêu cầu và lời giải trong ghi chú.

## Hành trình và phân bổ

| Mục | Kiến thức đầu vào | Mạch viết và sản phẩm chuyển tiếp | Phút giảng |
|---|---|---|---:|
| Mở đầu | Giới hạn một máy | Tiêu đề → mục lục → bốn mục tiêu | 5 |
| 2.1 | Dữ liệu lớn | Cụm và mạng → lỗi → khối và bản sao → đầu vào cho tác vụ | 10 |
| 2.2 | Dữ liệu đã chia | Đếm từ → phát, nhóm, cộng → giả mã → bất biến → gộp, lệch tải, chạy lại | 18 |
| 2.3 | Khóa và cộng tổng | Tích theo hàng → chia dải; bảng tập hợp → chọn, chiếu → vết nối → giả mã và tính đúng → tổng hợp | 30 |
| 2.4 | Một công việc | Đồ thị hàm → RDD → Map, Flatmap, Filter → tính lại → mạng tác vụ cần đánh giá | 12 |
| 2.5 | Thuật toán và nơi nhận | Mô hình → bảng đếm → nối hai bảng → lưới → thuật toán và tính đúng → chi phí → so sánh và khả thi | 27 |
| 2.6 | Chi phí và tải mỗi nơi | Đặc tả ảnh → q và rho → từng cặp → từng nhóm → bao phủ đúng → bộ nhớ | 12 |
| 2.7 | Các kết quả đã xây | Liên hệ các lớp → sản phẩm tự kiểm tra và bài tập | 5 |
| 2.8 | Hướng ôn tập | Nguồn gốc, học liệu, ghi chú và bắt đầu recitation | 1 |

## Chu trình các cụm trọng tâm

Các mã rút gọn dưới đây đều có tiền tố `lec02-`. Thời lượng từng cụm được tính từ các trang trong mục kế tiếp.

| Cụm | Thứ tự suy luận và mã trang | Dữ kiện, giả thiết truyền tiếp | Kiểm tra và chi phí |
|---|---|---|---|
| Đếm từ | s02-01: nhu cầu, đặc tả → 02/03: trực giác, vết → 04: giả mã → 04a: đúng → 05–07: ứng dụng, giới hạn | D1 “dữ liệu lớn”, D2 “lớn lớn”; tách khoảng trắng; giữ đủ năm lần xuất hiện | Câu hỏi ở 02, 06; s05-03 dùng lại 5 → 4 cặp; ex221 |
| Ma trận–vector | s03-01: nhu cầu, đặc tả gắn tiên quyết → 02: vết ký hiệu → 02a: giả mã, đúng → 03: chia dải | Ma trận $n\times n$; $p_j=m_{ij}v_j$; mỗi vị trí lưu một lần, số 0 không lưu; vector hoặc dải vector vừa bộ nhớ | Bất biến tổng, hàng không phát; ex251a tính đọc dải lặp |
| Chọn, chiếu | s03-04: khôi phục quan hệ → 05/06: ví dụ và mã cùng trang | Bốn hàng Links từ Hình 2.5; ngữ nghĩa tập hợp | Chu trình rút gọn vì là ứng dụng trực tiếp của lọc và nhóm khóa; tính đúng trên trang, dừng và chi phí trong ghi chú |
| Nối | s03-07a: nhu cầu, trực giác, cặp ví dụ → 08: vết đầy đủ → 07: đặc tả, mã → 07b: đúng, biên, chi phí | Hai bản sao cùng bốn hàng Links; U2 tương ứng B; nhãn L1/L2 tương ứng R/S | Câu hỏi nhóm url3; s05-04 thay $r=s=4$; chi phí phát $xy$ kết quả tách khỏi chi phí truyền |
| Tổng hợp | s03-09: áp dụng đếm từ lên Links; Friends là liên hệ nguồn trong ghi chú | Mỗi hàng đóng góp một số 1; tổng bằng j sau j đóng góp | Rút gọn do đã chứng minh bộ đếm ở s02-04a; ex251c và ex231b/d |
| Nối ba bảng | s05-05: nhu cầu, vết lưới → 05a: quy tắc Map → 05b: Reduce, đúng → 06: đếm → 07/08: so sánh → 09: kiểm tra | Ví dụ 2.15: lưới 4×4, ô (2,1); R gửi c bản, S một bản, T b bản; so sánh B,C thật | Bảng số hạng; Ví dụ 2.16 dùng ước tính 30r; k chính phương; ít hơn khi k<961, bằng khi k=961; kiểm tra bộ nhớ riêng |
| Các cặp ảnh | s06-00: nhu cầu → 01: hai đại lượng → 02: quy tắc từng cặp và đếm → 03: nhóm và đếm → 03a: đúng → 04: khả thi | Một triệu ảnh, một triệu byte/ảnh, 1000 nhóm đều; độ tương tự đối xứng; chỉ phát cặp vượt ngưỡng tau | Cặp chéo và nội bộ được bao phủ đúng; trung gian $N\rho B$, tổng cần cộng thêm $NB$; số so sánh không giảm |

Hệ thống lưu trữ và Spark dùng trạng thái, phụ thuộc và điều kiện khôi phục để giải thích cơ chế; không tạo giả mã hoặc chứng minh khi không áp dụng. Nhân hai ma trận, phép tập hợp, TensorFlow, đệ quy, đồng bộ và chứng minh cận dưới được định vị là đọc thêm. Tám bước học tập không bắt buộc thành tám trang. Thuật toán mới có vết trước giả mã; riêng công thức nhân hàng đã là tiên quyết, nên dùng nó để nhắc đặc tả trước vết đóng góp.

## Nguồn và cách thể hiện

- MMDS và Stanford CS246 đã được đối chiếu: dùng MMDS cho hệ tệp phân tán, đếm từ và nhóm khóa; tham khảo Stanford cho cách giải thích Spark và đồ thị phụ thuộc. Sách được chỉ định quyết định thứ tự, thuật toán, ví dụ và mô hình chi phí. Không thay mô hình đầu vào tác vụ của sách bằng mô hình cộng cả đầu ra trong slide tham khảo.
- Giữ cách dạy đã tham khảo ở ../math-4-AI lecture 01–03: một bước suy luận mỗi trang, dữ kiện trước khái quát, ví dụ xuyên suốt, hình và bảng trước công thức kết luận. Không sao chép nội dung, CSS hoặc hình môn toán.
- D1/D2 cụ thể hóa cơ chế đếm từ bằng tiếng Việt. Chọn From=url1, chiếu From và COUNT trên Links là áp dụng thuật toán nguồn lên Hình 2.5; không ghi là ví dụ số nguyên văn. Không tạo ma trận số hoặc danh sách 300 bạn cho Sally.
- Mười SVG gồm bốn hình bổ sung (mạng tủ máy, khóa–tác vụ–máy, đường đi hai cạnh, cặp nhóm ảnh) và sáu hình ban đầu: khối và bản sao (sơ đồ khái niệm hai bản sao), năm dải ma trận (Hình 2.4), luồng công việc (Hình 2.6 đủ sáu cung), chuỗi Spark (Ví dụ 2.7–2.10), mô hình chi phí (2.5.1) và lưới 4×4 (Hình 2.8). Hình có mô tả thay thế và nhãn, không dùng màu làm tín hiệu duy nhất. Vết số, công thức và giả mã dùng bảng HTML, KaTeX và khối mã.
- Hiệu chỉnh nguồn: lưới dùng chỉ số 0–3; ít chi phí hơn khi k<961; rho thay r cho sao chép, tau thay t cho ngưỡng. Số liệu người dùng và bạn bè là ví dụ lịch sử; 30r là ước tính của ví dụ.

## Đặc tả từng trang

Mã dưới đây là nội bộ, không hiện trên mặt slide hay ghi chú diễn giả. “Đầu ra nối tiếp” nêu kết quả cần mang sang trang kế tiếp; nếu trang kế là bài tập, phần giảng chuyển theo section như hướng dẫn ở đầu tài liệu. Hình thức kiểm tra không có câu hỏi riêng được thực hiện bằng việc chạy lại bảng hoặc giải thích đúng sản phẩm ghi ở mục đích; câu hỏi hiện trên slide có đáp án trong notes.

### `lec02-s00-01` · MapReduce và ngăn xếp xử lý dữ liệu lớn

- **Mục đích:** Xác định bài toán phân chia tính toán của bài 2.
- **Câu chốt:** Chọn khóa và phân chia dữ liệu là cơ sở thiết kế phép tính trên nhiều máy.
- **Kiến thức đầu vào:** Giới hạn một máy ở bài 1.
- **Vai trò và cách thể hiện:** Tiêu đề và thông tin học phần.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: theo dõi thứ tự tám mục nguồn của bài.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, Phần dẫn chương, trang in 21–22; sources/source.md, Bài 2.
- **Thời lượng:** 1 phút giảng.

### `lec02-s00-02` · Nội dung bài giảng

- **Mục đích:** Theo dõi thứ tự tám mục nguồn của bài.
- **Câu chốt:** Mạch bài đi từ lưu trữ và thực thi đến thuật toán, chi phí và đánh đổi bộ nhớ.
- **Kiến thức đầu vào:** Tên bài.
- **Vai trò và cách thể hiện:** Mục lục hai cột theo mục 2.1–2.8.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: nêu bốn sản phẩm học tập cần đạt.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, các mục 2.1–2.8.
- **Thời lượng:** 2 phút giảng.

### `lec02-s00-03` · Mục tiêu học tập

- **Mục đích:** Nêu bốn sản phẩm học tập cần đạt.
- **Câu chốt:** Kết quả học tập gồm vết chạy, giả mã, bảng chi phí và giải thích đánh đổi.
- **Kiến thức đầu vào:** Mục lục bài.
- **Vai trò và cách thể hiện:** Bốn mục tiêu bằng động từ kiểm tra được.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt máy, tủ máy và mạng giữa các tủ.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s00-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, sources/source.md, Bài 2; Chương 2.
- **Thời lượng:** 2 phút giảng.

### `lec02-s01-01` · 2.1 · Cụm máy và mạng kết nối

- **Mục đích:** Phân biệt máy, tủ máy và mạng giữa các tủ.
- **Câu chốt:** Dữ liệu giữa hai tủ phải đi qua mạng liên tủ.
- **Kiến thức đầu vào:** Dữ liệu vượt một máy.
- **Vai trò và cách thể hiện:** Sơ đồ mạng nội tủ và liên tủ; phân biệt phạm vi kết nối để đọc phần lỗi máy tiếp theo.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt hậu quả lỗi máy và lỗi cả tủ.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Thời lượng:** 3 phút giảng.

### `lec02-s01-02` · Lỗi máy và lỗi kết nối

- **Mục đích:** Phân biệt hậu quả lỗi máy và lỗi cả tủ.
- **Câu chốt:** Lỗi máy và lỗi mạng cả tủ có phạm vi ảnh hưởng khác nhau.
- **Kiến thức đầu vào:** Cấu trúc cụm máy.
- **Vai trò và cách thể hiện:** Hai trường hợp lỗi dẫn đến bản sao và tác vụ.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: xác định bản sao còn đọc được khi máy hỏng.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Thời lượng:** 3 phút giảng.

### `lec02-s01-03` · Chia khối, lưu bản sao và đọc gần dữ liệu

- **Mục đích:** Xác định bản sao còn đọc được khi máy hỏng.
- **Câu chốt:** Bản sao chỉ giúp phục hồi khi còn ít nhất một bản sao truy cập được.
- **Kiến thức đầu vào:** Lỗi máy và tủ.
- **Vai trò và cách thể hiện:** SVG khối/bản sao; điều kiện đặt khác tủ hiện trên trang.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đặc tả đầu vào và đầu ra của đếm từ.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s01-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.1, trang in 22–24.
- **Thời lượng:** 4 phút giảng.

### `lec02-s02-01` · 2.2 · Mô hình MapReduce

- **Mục đích:** Đặc tả đầu vào và đầu ra của đếm từ.
- **Câu chốt:** Map phát đóng góp; hệ thống nhóm theo khóa; reduce tổng hợp từng nhóm.
- **Kiến thức đầu vào:** Dữ liệu đã chia thành khối.
- **Vai trò và cách thể hiện:** Hai thẻ đầu vào–đầu ra và ba bước Map–nhóm–Reduce.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phát đủ năm đóng góp từ hai tài liệu.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, Ví dụ 2.1–2.2, trang in 25–27.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-02` · Mỗi lần xuất hiện tạo một đóng góp

- **Mục đích:** Phát đủ năm đóng góp từ hai tài liệu.
- **Câu chốt:** Năm lần xuất hiện tạo năm cặp, kể cả các cặp trùng nhau.
- **Kiến thức đầu vào:** Đặc tả đếm từ; tách theo khoảng trắng.
- **Vai trò và cách thể hiện:** Bảng hai chuỗi tiếng Việt và từng cặp phát.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tính tổng cho từng khóa và giữ các lần xuất hiện trùng.
- **Kiểm tra:** Từ “lớn” tạo bao nhiêu cặp trước khi nhóm? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.1, trang in 26; dữ liệu minh họa tiếng Việt được ghi trong storyboard.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-03` · Nhóm theo khóa rồi cộng

- **Mục đích:** Tính tổng cho từng khóa và giữ các lần xuất hiện trùng.
- **Câu chốt:** Ba đóng góp của từ “lớn” về cùng khóa và được cộng thành 3.
- **Kiến thức đầu vào:** Năm cặp đã phát.
- **Vai trò và cách thể hiện:** Bảng khóa–danh sách–kết quả.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: viết lại hai hàm đếm từ với giả thiết rõ.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.2–2.2.3, Ví dụ 2.2, trang in 26–27.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-04` · Thuật toán đếm từ

- **Mục đích:** Viết lại hai hàm đếm từ với giả thiết rõ.
- **Câu chốt:** Map phát một số 1 mỗi lần xuất hiện; reduce cộng mọi giá trị của từ.
- **Kiến thức đầu vào:** Vết nhóm theo khóa.
- **Vai trò và cách thể hiện:** Giả mã Map/Reduce cạnh nhau; giả thiết trước mã.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chứng minh bộ đếm đúng bằng bất biến cộng tổng.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-04) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, trang in 25–27; lập luận đúng từ Ví dụ 2.1–2.2.
- **Thời lượng:** 3 phút giảng.

### `lec02-s02-04a` · Bộ đếm trả đúng số lần xuất hiện

- **Mục đích:** Chứng minh bộ đếm đúng bằng bất biến cộng tổng.
- **Câu chốt:** Sau mỗi lần cộng, bộ đếm bằng tổng các giá trị đã đọc.
- **Kiến thức đầu vào:** Giả mã và trạng thái s.
- **Vai trò và cách thể hiện:** Bảng khởi tạo–duy trì–kết luận; biên kho rỗng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giải thích gộp cục bộ giữ nguyên tổng.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-04a) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.1–2.2.3, trang in 25–27; diễn giải tính đúng của Ví dụ 2.1–2.2.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-05` · Gộp cục bộ trước khi truyền

- **Mục đích:** Giải thích gộp cục bộ giữ nguyên tổng.
- **Câu chốt:** Gộp cục bộ giảm số cặp gửi mà giữ nguyên ý nghĩa tổng đếm.
- **Kiến thức đầu vào:** Bất biến bộ đếm.
- **Vai trò và cách thể hiện:** Trước–sau D2; 5 cặp thành 4; điều kiện phép cộng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt reducer theo khóa, tác vụ và máy.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-05) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.4, trang in 27–28.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-06` · Khóa, tác vụ và máy

- **Mục đích:** Phân biệt reducer theo khóa, tác vụ và máy.
- **Câu chốt:** Một tác vụ có thể xử lý nhiều khóa; một máy có thể chạy nhiều tác vụ.
- **Kiến thức đầu vào:** Nhóm khóa và bộ kết hợp.
- **Vai trò và cách thể hiện:** SVG vùng máy–tác vụ–nhóm khóa lồng nhau; phân công ba khóa của D1/D2 chỉ để minh họa.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: xác định phần phải chạy lại theo nơi lưu dữ liệu.
- **Kiểm tra:** Một khóa có danh sách rất dài có tự được chia nhỏ khi tăng số tác vụ? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Khung reducer/tác vụ/máy, trang in 28; 2.2.5.
- **Thời lượng:** 2 phút giảng.

### `lec02-s02-07` · Lưu trữ quyết định phần cần chạy lại

- **Mục đích:** Xác định phần phải chạy lại theo nơi lưu dữ liệu.
- **Câu chốt:** Mất trung gian cục bộ có thể buộc chạy lại cả tác vụ Map đã hoàn thành.
- **Kiến thức đầu vào:** Bản sao và đơn vị tác vụ.
- **Vai trò và cách thể hiện:** Bảng lỗi Map/Reduce và trung gian cục bộ.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giải thích lệch tải khi danh sách từ có độ dài khác nhau.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s02-07) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.2.5–2.2.6, trang in 28–30.
- **Thời lượng:** 3 phút giảng.

### `lec02-ex221a` · Bài tập 2.2.1(a) · Lệch tải khi chưa gộp

- **Mục đích:** Giải thích lệch tải khi danh sách từ có độ dài khác nhau.
- **Câu chốt:** Tần suất từ khác nhau làm độ dài danh sách của các reducer khác nhau.
- **Kiến thức đầu vào:** Reducer theo khóa.
- **Vai trò và cách thể hiện:** Đề gốc 100 Map, không bộ kết hợp; sản phẩm giải thích.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: so sánh gom reducer vào 10 và 10000 tác vụ.
- **Kiểm tra:** Không dùng bộ kết hợp. Thời gian xử lý danh sách của các reducer có lệch đáng kể không? Giải thích. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(a), trang in 30 / PDF 11.
- **Thời lượng:** 5 phút recitation.

### `lec02-ex221b` · Bài tập 2.2.1(b) · Gom reducer vào tác vụ

- **Mục đích:** So sánh gom reducer vào 10 và 10000 tác vụ.
- **Câu chốt:** Gom nhiều khóa vào một tác vụ có thể làm tải giữa các tác vụ đều hơn.
- **Kiến thức đầu vào:** Phân biệt reducer và task.
- **Vai trò và cách thể hiện:** Đề gốc gán ngẫu nhiên; giữ nguyên dữ kiện.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: lập luận tác động của gộp cục bộ lên lệch tải.
- **Kiểm tra:** Gán ngẫu nhiên các reducer vào 10 tác vụ Reduce. So sánh mức lệch với cách gán vào 10000 tác vụ Reduce. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(b), trang in 30 / PDF 11.
- **Thời lượng:** 5 phút recitation.

### `lec02-ex221c` · Bài tập 2.2.1(c) · Tác động của bộ kết hợp

- **Mục đích:** Lập luận tác động của gộp cục bộ lên lệch tải.
- **Câu chốt:** Gộp đầy đủ ở mỗi Map giới hạn số giá trị mỗi từ gửi về reducer theo số tác vụ Map.
- **Kiến thức đầu vào:** Bộ kết hợp và 100 Map.
- **Vai trò và cách thể hiện:** Đề gốc; đáp án nêu điều kiện gộp toàn bộ mỗi task.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đặc tả tích ma trận–vector trong biểu diễn thưa.
- **Kiểm tra:** Dùng bộ kết hợp tại cả 100 tác vụ Map. Mức lệch có còn đáng kể không? Giải thích. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.2.1(c), trang in 30 / PDF 11.
- **Thời lượng:** 5 phút recitation.

### `lec02-s03-01` · 2.3 · Nhân ma trận–vector

- **Mục đích:** Đặc tả tích ma trận–vector trong biểu diễn thưa.
- **Câu chốt:** Mỗi thành phần của tích ma trận–vector là tổng đóng góp của một hàng.
- **Kiến thức đầu vào:** Nhân hàng với vector; lưu phân tán.
- **Vai trò và cách thể hiện:** Nhu cầu ma trận Web lớn; miền chỉ số và công thức.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tái tạo tổng hàng từ các đóng góp theo cột.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-02` · Khóa hàng gom đúng các tích

- **Mục đích:** Tái tạo tổng hàng từ các đóng góp theo cột.
- **Câu chốt:** Khóa hàng đưa các tích của cùng một thành phần về cùng nhóm.
- **Kiến thức đầu vào:** Đặc tả M,v,x.
- **Vai trò và cách thể hiện:** Bảng 0→p1→p1+p2→tổng; chỉ rõ thứ tự minh họa.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giải thích giả mã gom tích trả đúng mỗi thành phần.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-02a` · Giả mã nhân ma trận–vector

- **Mục đích:** Giải thích giả mã gom tích trả đúng mỗi thành phần.
- **Câu chốt:** Khi vector vừa bộ nhớ, Map tính từng tích rồi reduce cộng theo hàng.
- **Kiến thức đầu vào:** Vết tổng hàng và bất biến đếm từ.
- **Vai trò và cách thể hiện:** Giả mã, điều kiện vector vừa RAM, số học và hàng không phát.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giữ đủ tích khi chia vector thành các dải.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-02a) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.1, trang in 31–32.
- **Thời lượng:** 3 phút giảng.

### `lec02-s03-03` · Chia dải khi vector không vừa bộ nhớ

- **Mục đích:** Giữ đủ tích khi chia vector thành các dải.
- **Câu chốt:** Chia dải giữ mỗi phần vector vừa bộ nhớ và vẫn gom đủ tích theo hàng.
- **Kiến thức đầu vào:** Vector phải vừa bộ nhớ.
- **Vai trò và cách thể hiện:** SVG năm dải; phủ hết miền cột, cùng khóa hàng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đọc bộ, thuộc tính và lược đồ của quan hệ tập hợp.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.2, Hình 2.4, trang in 32.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-04` · Một quan hệ là một bảng dữ liệu

- **Mục đích:** Đọc bộ, thuộc tính và lược đồ của quan hệ tập hợp.
- **Câu chốt:** Quan hệ trong bài dùng ngữ nghĩa tập hợp: không có hai bộ giống nhau.
- **Kiến thức đầu vào:** Bảng dữ liệu và cạnh có hướng.
- **Vai trò và cách thể hiện:** Bốn hàng Links từ Hình 2.5; quy ước không lặp bộ.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chọn đúng hai hàng thỏa from=url1.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-04) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.3, Hình 2.5, Ví dụ 2.3, trang in 33–34.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-05` · Phép chọn giữ các hàng thỏa điều kiện

- **Mục đích:** Chọn đúng hai hàng thỏa From=url1.
- **Câu chốt:** Phép chọn kiểm tra điều kiện trên từng hàng và giữ hàng thỏa điều kiện.
- **Kiến thức đầu vào:** Bốn hàng Links; điều kiện C(t).
- **Vai trò và cách thể hiện:** Bảng đầy đủ giữ hai/bỏ hai cạnh giả mã và hai chiều tính đúng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chiếu cột from và loại bản trùng bằng khóa.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-05) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.4, trang in 35; phần trích Hình 2.5.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-06` · Phép chiếu giữ cột và loại bản sao

- **Mục đích:** Chiếu cột From và loại bản trùng bằng khóa.
- **Câu chốt:** Phép chiếu gom các bộ chiếu giống nhau theo khóa để chỉ phát một bản.
- **Kiến thức đầu vào:** Quan hệ tập hợp, Links.
- **Vai trò và cách thể hiện:** Bảng bốn hàng→hai giá trị; giả mã và giải thích loại trùng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chọn đỉnh giữa làm khóa của đường đi hai cạnh.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-06) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.5, trang in 35–36; phần trích Hình 2.5.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-07a` · Bài toán nối: đường đi hai cạnh

- **Mục đích:** Chọn đỉnh giữa làm khóa của đường đi hai cạnh.
- **Câu chốt:** Hai cạnh nối được khi chung đỉnh giữa; trên Links, hai đường đều qua url2.
- **Kiến thức đầu vào:** Hai cạnh có hướng trong Links.
- **Vai trò và cách thể hiện:** Đồ thị bốn cạnh Links; hai đường đi hai cạnh qua url2 dẫn sang bảng vết đầy đủ.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chạy phép nối trên toàn bộ phần trích links.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-07a) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.7 và Ví dụ 2.4, trang in 35,37; phần trích Hình 2.5.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-08` · Vết nối trên bốn hàng Links

- **Mục đích:** Chạy phép nối trên toàn bộ phần trích Links.
- **Câu chốt:** Chỉ khóa url2 có dữ liệu ở cả hai phía nên phát đúng hai đường đi.
- **Kiến thức đầu vào:** Khóa giữa, nhãn L1/L2.
- **Vai trò và cách thể hiện:** Bảng bốn khóa; hai kết quả; câu kiểm tra nhóm url3.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: khái quát vết links thành thuật toán nối r và s.
- **Kiểm tra:** Giải thích vì sao nhóm url3 không phát đường đi. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Hình 2.5, Ví dụ 2.4 và 2.3.7, trang in 33,35,37.
- **Thời lượng:** 3 phút giảng.

### `lec02-s03-07` · Thuật toán nối hai quan hệ

- **Mục đích:** Khái quát vết Links thành thuật toán nối R và S.
- **Câu chốt:** Nối tự nhiên gom hai phía theo thuộc tính chung rồi ghép mọi cặp phù hợp.
- **Kiến thức đầu vào:** Vết nối, lược đồ, nhãn nguồn.
- **Vai trò và cách thể hiện:** Đặc tả, bảng Map, giả mã Reduce duyệt tích hai nhóm.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chứng minh nối đầy đủ và tính chi phí phát kết quả.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-07) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.7 và Ví dụ 2.4, trang in 35,37.
- **Thời lượng:** 3 phút giảng.

### `lec02-s03-07b` · Nối: tính đúng, biên và chi phí

- **Mục đích:** Chứng minh nối đầy đủ và tính chi phí phát kết quả.
- **Câu chốt:** Nhóm có x phần tử bên trái và y phần tử bên phải phát xy kết quả.
- **Kiến thức đầu vào:** Giả mã nối và nhóm cùng b.
- **Vai trò và cách thể hiện:** Bảng hai chiều tính đúng, biên; x,y và xy kết quả.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: áp dụng count bằng đóng góp một số 1 mỗi hàng.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-07b) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.7, trang in 37.
- **Thời lượng:** 2 phút giảng.

### `lec02-s03-09` · Đếm số hàng theo khóa

- **Mục đích:** Áp dụng COUNT bằng đóng góp một số 1 mỗi hàng.
- **Câu chốt:** COUNT theo khóa là cộng một đóng góp cho mỗi hàng thuộc nhóm.
- **Kiến thức đầu vào:** Đếm từ, nhóm khóa, Links.
- **Vai trò và cách thể hiện:** Bảng hai nhóm với tổng 0→1→2 rồi giả mã; SUM/AVG là liên hệ.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: nhận ra phép nhân hai ma trận gồm nối rồi tổng hợp.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-09) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.8 và Ví dụ 2.5, trang in 35,38; vết COUNT áp dụng lên Hình 2.5.
- **Thời lượng:** 3 phút giảng.

### `lec02-s03-10` · Nhân ma trận là nối rồi cộng

- **Mục đích:** Nhận ra phép nhân hai ma trận gồm nối rồi tổng hợp.
- **Câu chốt:** Nhân hai ma trận có thể tổ chức thành nối theo chỉ số chung rồi cộng các tích.
- **Kiến thức đầu vào:** Nhân ma trận–vector, nối và tổng.
- **Vai trò và cách thể hiện:** Công thức có điều kiện tương thích và bảng hai công việc; chi tiết đọc thêm.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: thiết kế mapreduce tìm số nguyên lớn nhất.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s03-10) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.3.9–2.3.10, trang in 38–40.
- **Thời lượng:** 2 phút giảng.

### `lec02-ex231a` · Bài tập 2.3.1(a) · Số nguyên lớn nhất

- **Mục đích:** Thiết kế MapReduce tìm số nguyên lớn nhất.
- **Câu chốt:** Lấy cực đại phải khởi tạo hoặc xử lý đầu vào sao cho đúng cả với số âm.
- **Kiến thức đầu vào:** Cách chọn khóa và tổng hợp.
- **Vai trò và cách thể hiện:** Đề 2.3.1(a); yêu cầu mã, trạng thái và tính đúng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giữ tổng và số lượng để tính trung bình đúng.
- **Kiểm tra:** Thiết kế MapReduce để trả số nguyên lớn nhất. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(a), trang in 40 / PDF 21.
- **Thời lượng:** 4 phút recitation.

### `lec02-ex231b` · Bài tập 2.3.1(b) · Trung bình các số nguyên

- **Mục đích:** Giữ tổng và số lượng để tính trung bình đúng.
- **Câu chốt:** Trung bình cần tổng và số lượng; chia sau khi gộp hai đại lượng đó.
- **Kiến thức đầu vào:** Bộ kết hợp và cặp trạng thái.
- **Vai trò và cách thể hiện:** Đề 2.3.1(b); không lấy trung bình không trọng số của các trung bình.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: dùng khóa để mỗi số nguyên chỉ xuất hiện một lần.
- **Kiểm tra:** Thiết kế MapReduce để trả trung bình các số nguyên. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(b), trang in 40 / PDF 21.
- **Thời lượng:** 6 phút recitation.

### `lec02-ex231c` · Bài tập 2.3.1(c) · Mỗi số chỉ xuất hiện một lần

- **Mục đích:** Dùng khóa để mỗi số nguyên chỉ xuất hiện một lần.
- **Câu chốt:** Dùng giá trị làm khóa để mỗi số nguyên phân biệt chỉ được phát một lần.
- **Kiến thức đầu vào:** Phép chiếu loại trùng.
- **Vai trò và cách thể hiện:** Đề 2.3.1(c); khóa là giá trị số nguyên.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tổng hợp số khóa phân biệt thành một số đếm.
- **Kiểm tra:** Thiết kế MapReduce để trả mỗi số chỉ xuất hiện một lần. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(c), trang in 40 / PDF 21.
- **Thời lượng:** 4 phút recitation.

### `lec02-ex231d` · Bài tập 2.3.1(d) · Số lượng giá trị khác nhau

- **Mục đích:** Tổng hợp số khóa phân biệt thành một số đếm.
- **Câu chốt:** Có thể loại trùng theo khóa rồi cộng số khóa để đếm giá trị phân biệt.
- **Kiến thức đầu vào:** Đếm và loại trùng.
- **Vai trò và cách thể hiện:** Đề 2.3.1(d); hướng dẫn hai công việc, không tuyên bố bắt buộc.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đọc phụ thuộc dữ liệu giữa nhiều hàm.
- **Kiểm tra:** Thiết kế MapReduce để trả số lượng giá trị khác nhau. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.3.1(d), trang in 40 / PDF 21.
- **Thời lượng:** 6 phút recitation.

### `lec02-s04-01` · 2.4 · Luồng công việc nhiều hàm

- **Mục đích:** Đọc phụ thuộc dữ liệu giữa nhiều hàm.
- **Câu chốt:** Cung trong luồng công việc thể hiện đầu ra hàm trước cung cấp đầu vào hàm sau.
- **Kiến thức đầu vào:** Hai tầng MapReduce và chịu lỗi.
- **Vai trò và cách thể hiện:** SVG Hình 2.6 đủ sáu cung; điều kiện chặn.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt một danh sách với nhiều phần tử rdd.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.4.1, Hình 2.6 và Ví dụ 2.6, trang in 42–43.
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-02` · Spark: Map và Flatmap

- **Mục đích:** Phân biệt một danh sách với nhiều phần tử RDD.
- **Câu chốt:** Map trả một đối tượng cho mỗi đầu vào; Flatmap có thể trả nhiều phần tử.
- **Kiến thức đầu vào:** D2, cặp từ–số đếm.
- **Vai trò và cách thể hiện:** Bảng Map/Flatmap cùng D2; giữ hai lần xuất hiện.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: theo dõi lọc từng phần tử sau flatmap.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.4.2, Ví dụ 2.7, trang in 44–45.
- **Thời lượng:** 3 phút giảng.

### `lec02-s04-03` · Nối Flatmap với Filter

- **Mục đích:** Theo dõi lọc từng phần tử sau Flatmap.
- **Câu chốt:** Filter quyết định giữ hay bỏ từng phần tử mà Flatmap đã tạo.
- **Kiến thức đầu vào:** RDD và Flatmap.
- **Vai trò và cách thể hiện:** SVG R0→R1→R2; câu kiểm tra từ dừng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: nêu thứ tự tính lại r2 từ lịch sử biến đổi.
- **Kiểm tra:** Một từ dừng xuất hiện ba lần; R₂ còn bao nhiêu cặp của từ đó? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, 2.4.2, Ví dụ 2.8, trang in 45–46.
- **Thời lượng:** 2 phút giảng.

### `lec02-s04-04` · Đánh giá lười và dòng dõi

- **Mục đích:** Nêu thứ tự tính lại R2 từ lịch sử biến đổi.
- **Câu chốt:** Dòng dõi lưu cách tạo dữ liệu để tính lại phần bị mất khi còn đầu vào cần thiết.
- **Kiến thức đầu vào:** Chuỗi Flatmap rồi Filter.
- **Vai trò và cách thể hiện:** Ba cơ chế đánh giá lười/lưu đệm/dòng dõi và câu kiểm tra.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt trách nhiệm lưu trữ với thực thi.
- **Kiểm tra:** R₂ bị mất; hãy nêu thứ tự áp dụng phép biến đổi từ tệp tài liệu. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, 2.4.3, Ví dụ 2.9–2.10, trang in 46–47.
- **Thời lượng:** 3 phút giảng.

### `lec02-s04-05` · Vai trò lưu trữ và thực thi

- **Mục đích:** Phân biệt trách nhiệm lưu trữ với thực thi.
- **Câu chốt:** Lưu trữ phân tán và hệ thực thi giải quyết hai trách nhiệm khác nhau.
- **Kiến thức đầu vào:** DFS, MapReduce, Spark.
- **Vai trò và cách thể hiện:** Bảng hai lớp và phân biệt Reduce; định vị đọc thêm.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chọn đơn vị, phạm vi và quy tắc đếm chi phí.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s04-05) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.4.1–2.4.3, trang in 41–48; 2.4.4–2.4.6, trang in 48–53 là đọc thêm.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-02` · 2.5 · Quy ước tính chi phí

- **Mục đích:** Chọn đơn vị, phạm vi và quy tắc đếm chi phí.
- **Câu chốt:** Phải chốt đơn vị, phạm vi và quy tắc đếm trước khi cộng chi phí.
- **Kiến thức đầu vào:** Mạng tác vụ và nơi lưu dữ liệu.
- **Vai trò và cách thể hiện:** Bảng mô hình trước công thức, gồm đọc cục bộ/đầu ra cuối.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: lập tổng i+m từ hai tầng nhận dữ liệu.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.1–2.5.2, trang in 53–56.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-01` · Cộng dữ liệu mà mỗi tầng nhận

- **Mục đích:** Lập tổng I+M từ hai tầng nhận dữ liệu.
- **Câu chốt:** Chi phí theo mô hình sách là tổng kích thước đầu vào của các tác vụ.
- **Kiến thức đầu vào:** Quy tắc chi phí đầu vào tác vụ.
- **Vai trò và cách thể hiện:** SVG I→Map→M→Reduce; định nghĩa I,M cùng đơn vị.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tính chi phí đếm từ trước và sau gộp.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.1, trang in 53–55.
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-03` · Đếm từ: theo dữ liệu qua hai tầng

- **Mục đích:** Tính chi phí đếm từ trước và sau gộp.
- **Câu chốt:** Gộp D2 giảm trung gian từ năm xuống bốn cặp trong cùng ví dụ đếm từ.
- **Kiến thức đầu vào:** Năm cặp, bốn cặp; I và B byte.
- **Vai trò và cách thể hiện:** Bảng I+5B và I+4B với giả thiết trước bảng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đếm map và reduce cho phép nối hai bảng.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.1, 2.2.4 và mô hình 2.5.1; phần trích minh họa được ghi trong storyboard.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-04` · Nối hai bảng: một lần phát cho mỗi bộ

- **Mục đích:** Đếm Map và Reduce cho phép nối hai bảng.
- **Câu chốt:** Mỗi bộ được đọc ở Map và ở Reduce nên nối hai bảng có chi phí chuẩn hóa 2(r+s).
- **Kiến thức đầu vào:** Thuật toán nối, đơn vị chuẩn hóa.
- **Vai trò và cách thể hiện:** Bảng căn cứ từng tầng và thay r=s=4 được 16.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giải thích ba bộ gặp tại ô (2,1).
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-04) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.14, trang in 55; phần Links Hình 2.5.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-05` · Nối ba bảng: gửi tới một lưới

- **Mục đích:** Giải thích ba bộ gặp tại ô (2,1).
- **Câu chốt:** Bộ R theo hàng, bộ T theo cột và bộ S tại ô giao đưa ba bộ phù hợp đến cùng ô.
- **Kiến thức đầu vào:** Nối hai quan hệ, giá trị thuộc tính chung.
- **Vai trò và cách thể hiện:** SVG lưới 4×4 từ Ví dụ 2.15; R bốn bản, S một bản, T bốn bản.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: viết quy tắc gửi bộ tới mọi ô cần nó.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-05) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.3 và Ví dụ 2.15, trang in 56–58.
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-05a` · Gửi bộ tới các ô cần nhận

- **Mục đích:** Viết quy tắc gửi bộ tới mọi ô cần nó.
- **Câu chốt:** Số bản gửi phụ thuộc số cột với R, số hàng với T và bằng một với S.
- **Kiến thức đầu vào:** Vết ô(2,1); hàm băm và lưới.
- **Vai trò và cách thể hiện:** Bảng giả mã Map theo R/S/T; miền b,c và nhãn nguồn.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: giải thích nối ba bảng đúng dù băm va chạm.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-05a) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.3, Ví dụ 2.15, trang in 56–58.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-05b` · Ghép tại ô chung và kiểm tra tính đúng

- **Mục đích:** Giải thích nối ba bảng đúng dù băm va chạm.
- **Câu chốt:** Trùng ô băm chỉ tạo ứng viên; reducer vẫn kiểm tra giá trị B và C thật.
- **Kiến thức đầu vào:** Quy tắc gửi và thuộc tính thật.
- **Vai trò và cách thể hiện:** Giả mã Reduce, hai chiều tính đúng, ô duy nhất và biên.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: truy từng số hạng c3 về số bản được nhận.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-05b) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.3 và khung Computation Cost of the 3-Way Join, trang in 57–58.
- **Thời lượng:** 2 phút giảng.

### `lec02-s05-06` · Chi phí của phép nối ba bảng

- **Mục đích:** Truy từng số hạng C3 về số bản được nhận.
- **Câu chốt:** Mỗi số hạng chi phí nối ba bảng bắt nguồn từ một tầng đọc hoặc một lần sao chép.
- **Kiến thức đầu vào:** R gửi c, S gửi một bản, T gửi b.
- **Vai trò và cách thể hiện:** Bảng bốn cột, tổng hai tầng rồi thay b=c=4.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tính chi phí hai công việc nối tiếp từ kích thước trung gian.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-06) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.5.3, trang in 56–58.
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-07` · Nối tuần tự có thể tạo bảng trung gian lớn

- **Mục đích:** Tính chi phí hai công việc nối tiếp từ kích thước trung gian.
- **Câu chốt:** Bảng trung gian lớn được đọc lại ở công việc sau làm tăng tổng chi phí.
- **Kiến thức đầu vào:** Nối hai bảng và mô hình đầu vào.
- **Vai trò và cách thể hiện:** Giả thiết lịch sử30r; bảng bốnr+62r=66r.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: so sánh chi phí có xét điểm bằng và miền nguyên.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-07) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.16, trang in 58–59.
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-08` · So sánh hai cách dưới cùng giả thiết

- **Mục đích:** So sánh chi phí có xét điểm bằng và miền nguyên.
- **Câu chốt:** Dưới giả thiết ví dụ và lưới vuông, hai cách bằng chi phí ở k=961.
- **Kiến thức đầu vào:** C3, r=s=t, trung gian30r.
- **Vai trò và cách thể hiện:** Bảng k16/k961 và ba bước bất đẳng thức.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: phân biệt tổng chi phí với thời gian hoàn thành.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s05-08) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, Ví dụ 2.15–2.16, trang in 57–59; hiệu chỉnh biên đẳng thức.
- **Thời lượng:** 3 phút giảng.

### `lec02-s05-09` · Tổng chi phí và tải lớn nhất

- **Mục đích:** Phân biệt tổng chi phí với thời gian hoàn thành.
- **Câu chốt:** Tổng dữ liệu và tải lớn nhất là hai đại lượng khác nhau; chưa trực tiếp là thời gian chạy.
- **Kiến thức đầu vào:** So sánh chi phí nối.
- **Vai trò và cách thể hiện:** Hai thẻ tổng/tải lớn nhất; câu kiểm tra tính khả thi.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đếm chi phí nhân ma trận–vector có đọc lặp dải.
- **Kiểm tra:** Tổng chi phí giảm có đủ để kết luận bài toán chạy nhanh hơn không? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, 2.5.2 và chuyển sang 2.6, trang in 55–56,61.
- **Thời lượng:** 2 phút giảng.

### `lec02-ex251a` · Bài tập 2.5.1(a) · Nhân ma trận–vector

- **Mục đích:** Đếm chi phí nhân ma trận–vector có đọc lặp dải.
- **Câu chốt:** Chi phí chia dải phải tính cả số lần mỗi dải vector được các tác vụ đọc.
- **Kiến thức đầu vào:** Chia dải và mô hình đầu vào.
- **Vai trò và cách thể hiện:** Đề 2.5.1(a); sản phẩm bảng theo z,Lj,aj.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tính chi phí tổng hợp theo số hàng quan hệ.
- **Kiểm tra:** Biểu diễn chi phí truyền thông theo kích thước ma trận và vector. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.5.1(a), trang in 59 / PDF 40; 2.3.2.
- **Thời lượng:** 13 phút recitation.

### `lec02-ex251c` · Bài tập 2.5.1(c) · Nhóm và tổng hợp

- **Mục đích:** Tính chi phí tổng hợp theo số hàng quan hệ.
- **Câu chốt:** Mỗi hàng được đọc một lần ở Map và một lần ở Reduce trong mô hình chuẩn hóa.
- **Kiến thức đầu vào:** Thuật toán nhóm, mô hình đầu vào.
- **Vai trò và cách thể hiện:** Đề 2.5.1(c); đơn vị chuẩn hóa hoặc byte.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đặc tả đầu ra cặp ảnh vượt ngưỡng tương tự.
- **Kiểm tra:** Biểu diễn chi phí truyền thông theo kích thước quan hệ. Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, Bài tập 2.5.1(c), trang in 59 / PDF 40; 2.3.8.
- **Thời lượng:** 12 phút recitation.

### `lec02-s06-00` · 2.6 · Tìm các cặp ảnh tương tự

- **Mục đích:** Đặc tả đầu ra cặp ảnh vượt ngưỡng tương tự.
- **Câu chốt:** Cần kiểm tra mọi cặp ảnh nhưng chỉ trả các cặp vượt ngưỡng tương tự.
- **Kiến thức đầu vào:** Đánh đổi bộ nhớ và truyền dữ liệu.
- **Vai trò và cách thể hiện:** Dữ kiệnmột triệu ảnh,1 MB/ảnh; đối xứng và ngưỡng tau.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đọc q và rho như hai đại lượng khác nhau.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-00) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 62–63.
- **Thời lượng:** 1 phút giảng.

### `lec02-s06-01` · Đầu vào mỗi reducer và số lần sao chép

- **Mục đích:** Đọc q và rho như hai đại lượng khác nhau.
- **Câu chốt:** q giới hạn đầu vào mỗi reducer; rho đếm số cặp phát trung bình trên một đầu vào.
- **Kiến thức đầu vào:** Nhu cầu chia ảnh cho reducer.
- **Vai trò và cách thể hiện:** Bảng định nghĩa và tỷ số số cặp/số đầu vào.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: đếm số bản sao khi mỗi reducer nhận hai ảnh.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.6.1, trang in 61.
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-02` · Mỗi reducer xử lý một cặp ảnh

- **Mục đích:** Đếm số bản sao khi mỗi reducer nhận hai ảnh.
- **Câu chốt:** Mỗi reducer nhận hai ảnh nhưng mỗi ảnh phải gửi tới N−1 nơi.
- **Kiến thức đầu vào:** q,rho; cặp không thứ tự.
- **Vai trò và cách thể hiện:** Quy tắc gửi/so sánh/phát và bảng q=2, rho=N−1,byte.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tính q,rho khi mỗi reducer nhận hai nhóm.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 62–63.
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03` · Gom nhóm để dùng lại mỗi ảnh

- **Mục đích:** Tính q,rho khi mỗi reducer nhận hai nhóm.
- **Câu chốt:** Gom nhóm tăng dữ liệu mỗi reducer để dùng lại ảnh đã nhận cho nhiều phép so sánh.
- **Kiến thức đầu vào:** Phương án từng cặp, chia đều1000 nhóm.
- **Vai trò và cách thể hiện:** Quy tắc Map theo cặp nhóm và bảng tính từng đại lượng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chứng minh mọi cặp ảnh được xét đúng một nơi.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s06-03) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.6.2, Ví dụ 2.18, trang in 63–64.
- **Thời lượng:** 2 phút giảng.

### `lec02-s06-03a` · Bao phủ mọi cặp, mỗi cặp đúng một nơi

- **Mục đích:** Chứng minh mọi cặp ảnh được xét đúng một nơi.
- **Câu chốt:** Mọi cặp chéo và cặp nội bộ đều được giao đúng một nơi, không giảm số cặp phải so sánh.
- **Kiến thức đầu vào:** Cặp nhóm và phép modulo.
- **Vai trò và cách thể hiện:** SVG tách cặp chéo và cặp nội bộ được giao riêng trong trường hợp hai nhóm kề nhau; câu hỏi xét hậu quả bỏ quy tắc giao riêng.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: kiểm tra bộ nhớ thực tế ngoài kích thước ảnh.
- **Kiểm tra:** Nếu mọi reducer chứa nhóm $u$ đều so sánh nội bộ nhóm đó, một cặp bị xét mấy lần? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, 2.6.2, trang in 63–64.
- **Thời lượng:** 3 phút giảng.

### `lec02-s06-04` · Đánh đổi cần kiểm tra trước khi triển khai

- **Mục đích:** Kiểm tra bộ nhớ thực tế ngoài kích thước ảnh.
- **Câu chốt:** Dung lượng ảnh chưa bao gồm bộ nhớ phụ nên chưa đủ kết luận reducer chạy được.
- **Kiến thức đầu vào:** q2000,1 MB/ảnh; đầy đủ các cặp.
- **Vai trò và cách thể hiện:** Bảng hai phương án và câu kiểm tra 2 GB.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: nối cách chọn khóa với lưu trữ và đánh giá.
- **Kiểm tra:** Với cách gom nhóm, 2 GB dữ liệu ảnh đã đủ để kết luận reducer chạy được chưa? Đáp án hoặc hướng giải nằm trong ghi chú diễn giả của trang.
- **Nguồn:** MMDS, Chương 2, 2.6.2–2.6.7, trang in 61–74.
- **Thời lượng:** 2 phút giảng.

### `lec02-s07-01` · 2.7 · Từ lưu trữ đến đánh giá thuật toán

- **Mục đích:** Nối cách chọn khóa với lưu trữ và đánh giá.
- **Câu chốt:** Cách chọn khóa quyết định nơi dữ liệu gặp nhau và ảnh hưởng cả chi phí lẫn bộ nhớ.
- **Kiến thức đầu vào:** Các kết quả từ2.1–2.6.
- **Vai trò và cách thể hiện:** Bảng thu hồi năm lớp lập luận.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: chọn bài tập để tự kiểm tra từng mục tiêu.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s07-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.7, trang in 74–77.
- **Thời lượng:** 3 phút giảng.

### `lec02-s07-02` · Kiểm tra bằng sản phẩm học tập

- **Mục đích:** Vận dụng bốn kết quả đã học để tự kiểm tra từng mục tiêu.
- **Câu chốt:** Vết chạy, giải thích nhóm khóa, bảng chi phí và điều kiện bộ nhớ cùng kiểm tra mục tiêu bài.
- **Kiến thức đầu vào:** Giả mã, tính đúng và mô hình chi phí.
- **Vai trò và cách thể hiện:** Bốn nhiệm vụ tự kiểm tra trên D2, Links, r=s=4 và nhóm ảnh; đáp án trong ghi chú diễn giả.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Chuẩn bị: tìm nguồn chính và ghi chú tự học.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s07-02) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.7 và bài tập 2.2.1,2.3.1,2.5.1.
- **Thời lượng:** 2 phút giảng.

### `lec02-s08-01` · 2.8 · Tài liệu tham khảo

- **Mục đích:** Tìm nguồn chính và ghi chú tự học.
- **Câu chốt:** Chương 2 là nguồn chính; ghi chú giúp tự học, các mục cận dưới được định vị đọc thêm.
- **Kiến thức đầu vào:** Toàn bộ phần giảng.
- **Vai trò và cách thể hiện:** Tài liệu nguồn, ghi công MMDS, liên kết ghi chú và bài tập.
- **Kết nối vào–ra:** dùng kiến thức đầu vào trên để đạt mục đích trang. Quay lại bài tập 2.2.1 qua liên kết, rồi tiếp 2.3.1 và 2.5.1.
- **Ghi chú:** [Giả thiết, lập luận và câu chuyển của trang](../../lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html#/lec02-s08-01) nằm trong phần ghi chú diễn giả.
- **Nguồn:** MMDS, Chương 2, 2.8, trang in 77–79.
- **Thời lượng:** 1 phút giảng.

## Ánh xạ ghi chú độc lập

Ghi chú giữ thứ tự mục 2.1–2.8. Trong từng chủ đề, đặc tả đứng trước ví dụ và thuật toán theo chu trình tài liệu tự học của AGENTS; vì vậy ví dụ có thể có vị trí khác slide. Mọi dữ kiện và giả thiết dùng chung phải khớp.

| note-topic-id | Đầu vào → sản phẩm học tập → dùng tiếp | Trang liên quan |
|---|---|---|
|lec02-note-01|Lỗi máy → bản sao còn đọc được → chạy lại tác vụ|s01-*|
|lec02-note-02|Khóa → vết đếm và bất biến → thiết kế theo khóa|s02-*;ex221*|
|lec02-note-03|Khóa/cộng tổng → đặc tả/ví dụ/mã/đúng của ma trận và quan hệ → bảng chi phí|s03-*;ex231*|
|lec02-note-04|MapReduce → RDD và dòng dõi → mạng tác vụ cần đếm|s04-*|
|lec02-note-05|Thuật toán → tổng đầu vào và số bản sao → so sánh khả thi|s05-*;ex251*|
|lec02-note-06|Lượng dữ liệu → q/rho và đầy đủ cặp → giới hạn bộ nhớ|s06-*|
|lec02-note-07|Các kết quả → lời giải bài tập → tự kiểm tra|s07-*;toàn bộ ex*|
|lec02-note-08|Phạm vi bài → nguồn đọc chính/đọc thêm → tự học|s08-*|

Lượt sửa này đã đồng bộ ví dụ COUNT/Map–Flatmap, thêm hình luồng công việc và sửa đặc tả đầu ra cặp ảnh vượt ngưỡng. Trạng thái kiểm định và các quyết định cuối nằm trong review-log.md; số trang, nguồn và thời lượng trên đây là đặc tả hiện hành.

## Quyết định rà cuối về thứ tự và ký hiệu

Mã trang là định danh ổn định, không phải số thứ tự phát. Giữ s03-07a → s03-08 → s03-07 → s03-07b để ví dụ đứng trước khái quát; giữ s05-02 → s05-01 để mô hình và đơn vị đứng trước công thức. Thứ tự thực tế là thứ tự các mục trong storyboard và các section trong HTML. Không đổi mã chỉ để làm thứ tự số tăng dần, tránh làm hỏng liên kết đã dùng.

Khóa của L₁ là cột thứ hai, khóa của L₂ là cột thứ nhất. Vì vậy L₂ có url2,url3 tại khóa url1; bảng hiện hành được giữ sau khi tự chạy lại. q là cận trên theo mục 2.6.1; hai ví dụ chia đều đạt đúng cận. B được định nghĩa riêng là byte/cặp ở đếm từ và byte/ảnh ở so sánh ảnh. Bài tập 2.5.1(a) yêu cầu người học chọn ký hiệu và lập mô hình; không đưa các ký hiệu chưa cần dùng lên đề để thay việc lập luận của sinh viên.


## Bổ sung trực quan theo tiêu chuẩn ngày 14-09-2026

Giữ 61 trang, 9 phần, 120 + 60 phút và toàn bộ dữ kiện bài tập. Bốn hình mới là sơ đồ khái niệm hoặc biểu diễn lại dữ kiện đã có; không bổ sung mệnh đề hay số liệu thực nghiệm. Hình không thay công thức, bảng vết chạy hoặc giả mã.

| Trang | Vai trò và cách thể hiện cập nhật | Nguồn và điều chỉnh |
|---|---|---|
| lec02-s01-01 | Sơ đồ mạng hai tủ, phân biệt kết nối nội tủ/liên tủ; nối sang phạm vi lỗi | Hình 2.1, trang in 23/PDF4; trích hai tủ, không giữ số máy hay thông số lịch sử |
| lec02-s02-06 | Các vùng máy–tác vụ–nhóm khóa lồng nhau; nối sang lập lịch và khôi phục | Khung trang 28/PDF9, mục 2.2.5; áp dụng ba khóa D1/D2, phân công A/B minh họa |
| lec02-s03-07a | Đồ thị đủ bốn cạnh Links; hai đường qua url2 dẫn sang bảng vết và giả mã nối | Dữ kiện Hình 2.5 trang 33/PDF14 và mục 2.3.7; giữ cạnh trực tiếp url1→url3, không thêm cạnh |
| lec02-s06-03a | Hai nhóm ảnh và các cặp phải so sánh, xét v là nhóm kế tiếp u; nối quy tắc bao phủ với chi phí | Mục2.6.2, Ví dụ 2.18 trang 63–64/PDF44–45; ký hiệu ảnh đại diện, nhóm đánh số0..g−1 như slide |
| lec02-s07-02 | Bốn nhiệm vụ cụ thể trên D2, Links, r=s=4 và nhóm ảnh; đáp án trong notes | Áp dụng lại ví dụ đã giảng, giữ các liên kết bài tập nguồn; thời lượng hiện tại giữ nguyên |

Ưu tiên sách MMDS cho cả bốn hình; slide MMDS đối chiếu kiến trúc và thực thi, Stanford giữ vai trò hỗ trợ cụm Spark. Không gán hình nhóm ảnh cho slide tham khảo không chứa nội dung đó. Mỗi trang có câu chốt trong đặc tả; mọi khối giả mã thêm data-trim, giữ language-text.
