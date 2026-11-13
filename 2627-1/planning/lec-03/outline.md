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

## Ghi chú theo chuẩn giáo trình (2026-11-11)

Mục này thay mục "Ghi chú tự học đã phát hành" ở trên (bảy chủ đề `lec03-note-01`…`07` không còn dùng). Cập nhật theo vòng sửa 1 (hàng đợi `lec03-queue.md`, 2026-11-11).

**Goal.** `materials/lec-03/lecture-note.md` là một chương giáo trình tự chứa theo `materials/_templates/lecture-note.md`, kế hoạch `lec03-plan.md`, quyết định Q1–Q10 và vòng sửa 1 (B1–B4) của điều phối viên; bộ trang chiếu giữ nguyên. Bài tập cuối mục trong ghi chú: 03.1 (MMDS 5.1.5, cuối 2.1), 03.2 (tự dựng theo B1, cuối 2.5), 03.3 (MMDS 5.2.3, cuối 3.3), 03.4 (MMDS 5.2.4, cuối 4.4), 03.5 (MMDS 5.1.6, phần đọc thêm), 03.6 (thực hành theo B1, cuối Mục 5). Bài tập củng cố 03.7–03.12 ở `materials/lec-03/exercises.md`: 03.7 (5.2.2), 03.8 (5.1.1), 03.9 (5.1.2), 03.10 (5.2.1), 03.11 (5.1.3), 03.12 (5.1.7); 03.7–03.10 là recitation của deck.

**Vấn đề trung tâm.** Xếp hạng $10^9$ trang (trang chiếu MMDS tr.48) theo cấu trúc liên kết; ma trận đặc cần $8\cdot10^{18}$ byte (Ví dụ 03.1). Hình cấu trúc chương: `img/lec-03/note-cau-truc-chuong-03.svg`, mỗi cột ghi câu hỏi và khái niệm, không ghi kết quả (B4).

### Bản đồ chủ đề bốn nhóm

| note-topic-id | Mục ghi chú | Chủ đề và khối số hiệu | Nhãn | Nguồn | Chu trình |
|---|---|---|---|---|---|
| `lec-03-topic-01` | Mục 1 mở, 1.1 | Thư rác theo từ, trại thư rác; Ví dụ 03.1; Định nghĩa 03.1; Ví dụ 03.2–03.3 | cốt lõi | MMDS §5.1.1 tr.176–177, hộp tr.177, §5.1.6; trang chiếu MMDS tr.16–17, 48 | rút gọn: đặc tả bài toán, không có định lý |
| `lec-03-topic-02` | 1.2 | Ví dụ 03.4; Định nghĩa 03.2; hai nhầm lẫn | cốt lõi | MMDS §5.1.2 | rút gọn: một định nghĩa, ví dụ trước và sau |
| `lec-03-topic-03` | Mục 2 mở, 2.1 | Người lướt ngẫu nhiên; Định nghĩa 03.3; Ví dụ 03.5; Mệnh đề 03.4; Định nghĩa 03.5 (phép lặp lũy thừa, phép lặp thô); Ví dụ 03.6; Bài tập 03.1 | cốt lõi | MMDS §5.1.2 tr.177–180, Ví dụ 5.1–5.2, hộp tr.180; trang chiếu MMDS tr.31–32 | đủ |
| `lec-03-topic-04` | 2.2 | Cấu trúc nơ thắt (`note-no-that-web.svg`); Định nghĩa 03.6, 03.7; Ví dụ 03.7, 03.8 | cốt lõi; nơ thắt là cầu nối | MMDS §5.1.3 tr.181–182, §5.1.4 tr.182–183, §5.1.5 tr.185–186, Ví dụ 5.3, 5.5 | rút gọn: hai khái niệm phụ, không định lý |
| `lec-03-topic-05` | 2.3 | Bước nhảy, phần bù; Định nghĩa 03.8; Ví dụ 03.9–03.11; Mệnh đề 03.9; câu tổng $1-\beta\delta$ của công thức không bù | cốt lõi; Mệnh đề 03.9 là cầu nối | MMDS §5.1.5 tr.186–187, Ví dụ 5.6; trang chiếu MMDS tr.42, 49, 52; CS246 tr.45, 54 | đủ |
| `lec-03-topic-06` | 2.4 | Thuật toán 03.10; Ví dụ 03.12; Mệnh đề 03.11; Nhận xét 03.12 | cốt lõi | MMDS §5.1.2 tr.179, §5.2 tr.189; CLRS §2.1 | đủ |
| `lec-03-topic-07` | 2.5 | Mệnh đề 03.13; Bổ đề 03.14; Định lý 03.15; Hệ quả 03.16; Mệnh đề 03.17 (công thức không bù và chuẩn hóa lại, chuyển từ Nhận xét 03.10 cũ theo A7, đặt sau Ví dụ 03.13 theo vòng sửa 2); Ví dụ 03.13; Nhận xét 03.18; Bài tập 03.2 | cốt lõi; Mệnh đề 03.17 là cầu nối (Q8); Hệ quả 03.16 là bổ sung (dùng ở Bài 04; Hệ quả 03.17 ở bản vòng sửa 1) | MMDS §5.1.5; trang chiếu MMDS tr.51; chứng minh của chương (Q1) | đủ |
| `lec-03-topic-08` | Mục 3 mở, 3.1 | Định nghĩa 03.19; Ví dụ 03.14 | cốt lõi | MMDS §5.2.1 tr.190, §5.2.2 tr.191, Ví dụ 5.7, Hình 5.11 | rút gọn: biểu diễn dữ liệu |
| `lec-03-topic-09` | 3.2 | Ví dụ 03.15 (bỏ hình `model-collect.svg`, vòng sửa 2); Nhận xét 03.20 | cầu nối (Bài 02 → khối) | MMDS §5.2.2–5.2.3 tr.191; Thuật toán 02.18, Mệnh đề 02.15, Nhận xét 02.20, Tình huống 02.3 | rút gọn |
| `lec-03-topic-10` | 3.3 | Định nghĩa 03.21; Ví dụ 03.16–03.18 (03.18 tính trang B, B3); Thuật toán 03.22 (có bảng chi phí); Mệnh đề 03.23; Nhận xét 03.24; Bài tập 03.3 | cốt lõi | MMDS §5.2.3–5.2.4 tr.191–194, Ví dụ 5.8, Hình 5.12–5.14 | đủ |
| `lec-03-topic-11` | Mục 4 mở, 4.1 | Định nghĩa 03.25; Mệnh đề 03.26; Ví dụ 03.19 | cốt lõi | MMDS §5.2.1, §5.2.4 | đủ |
| `lec-03-topic-12` | 4.2, 4.3 | Mệnh đề 03.27, 03.28; Ví dụ 03.20, 03.21 ($H$ tính cả cặp khởi tạo: 144/132) | cốt lõi | MMDS §5.2.3, §5.2.5 tr.193–194; Định nghĩa 02.33, Mệnh đề 02.38 | đủ |
| `lec-03-topic-13` | 4.4 | Mệnh đề 03.29; Nhận xét 03.30; Ví dụ 03.22; Bài tập 03.4 | cốt lõi | Định nghĩa 02.30, 02.39 | đủ |
| `lec-03-topic-14` | Đọc thêm (thu gọn) | Thuật toán 03.31 (có bảng chi phí); Ví dụ 03.23; Nhận xét 03.32; Bài tập 03.5 | đọc thêm (Q4; không có §5.2.5) | MMDS §5.1.4 tr.183–185, Ví dụ 5.4, Hình 5.4–5.5, chú thích 4 | rút gọn |
| `lec-03-topic-15` | Mục 5 | `pagerank.py`; Nhận xét 03.33; Ví dụ 03.24; Bài tập 03.6 | cốt lõi (thực hành) | `materials/lec-03/code/` | rút gọn: không có bài sách (Q10), bài cuối mục theo B1 |
| `lec-03-topic-16` | Tình huống và ứng dụng | Tình huống 03.1 (một tỷ trang), 03.2 (nơ thắt, giả thiết bị vi phạm); ứng dụng Bài 04, Bài 14 | bổ sung | trang chiếu MMDS tr.48; MMDS §5.1.1, §5.1.3, §5.1.6, §5.2.1 | không áp dụng |
| `lec-03-topic-17` | Tóm tắt chương | Đoạn 8 câu (có câu trả lời ở quy mô $10^9$), kết quả theo mục, công thức, giả thiết hay bỏ quên | tổng kết | toàn chương | không áp dụng |

**Bài tập theo mục tiêu.** Mục tiêu 3 (bảo toàn, hội tụ, ngưỡng dừng) và mục tiêu 6 (`pagerank.py`) không có bài giáo trình trong MMDS §5.1–5.2; theo `AGENTS.md` mục 10 và B1, chúng dựa vào Bài tập 03.2 và 03.6 cuối mục trong ghi chú, dựng trên dữ kiện đã có của ghi chú.

**Bỏ.** Bài 5.1.4 (!!) (Q3); cập nhật theo dải trên một máy §5.2.5 và trang chiếu MMDS tr.54–59 (Q4); ba nhiệm vụ thực hành của `practice-README.md` không thành bài tập trong `exercises.md` (Q10, C1); chuỗi Neumann (A8; chỉ giữ một câu cách chứng minh Cauchy).

### Thuật ngữ Việt–Anh của ghi chú

| Tiếng Việt | Tiếng Anh | Lần đầu trong ghi chú |
|---|---|---|
| thư rác theo từ; trại thư rác | term spam; spam farm | Mục 1 |
| bầu bằng chân | vote with their feet | Mục 1.1 |
| khuyên; bậc ra | self-loop; out-degree | Định nghĩa 03.1 |
| người lướt ngẫu nhiên | random surfer | Mục 2.1 |
| ma trận liên kết | transition matrix | Định nghĩa 03.3 |
| phép lặp lũy thừa; phép lặp thô | power iteration; trường hợp $A=M_0$, $r^0=u$ | Định nghĩa 03.5 |
| cấu trúc nơ thắt; thành phần liên thông mạnh; thành phần vào, ra; tua; ống; thành phần rời | bowtie; strongly connected component (SCC); in-, out-component; tendrils; tubes; isolated components | Mục 2.2 |
| nút cụt | dead end | Định nghĩa 03.6 |
| dưới ngẫu nhiên; ngẫu nhiên theo cột | substochastic; column stochastic | Định nghĩa 03.6 |
| bẫy liên kết | spider trap | Định nghĩa 03.7 |
| đánh thuế; bước nhảy (còn gọi là dịch chuyển); phân phối nhảy | taxation; teleport; (Bài 04: phân phối dịch chuyển) | Mục 2.3 |
| danh sách liên kết ra | (biểu diễn theo bậc ra và danh sách đích, MMDS §5.2.1) | Định nghĩa 03.19 |
| dải; khối | stripe; block | Định nghĩa 03.21 |
| đọc ghi lặp | thrashing | Nhận xét 03.20 |
| pha chuyển dữ liệu trung gian | shuffle | Bảng ký hiệu |
| nhóm trang liên kết đôi một | clique | Bài tập 03.11 |
| chỉ mục ngược | inverted index | mục Ứng dụng |

### Khác biệt với bộ trang chiếu

- Thêm so với deck: cấu trúc nơ thắt (§5.1.3); vết đầy đủ MMDS Ví dụ 5.2, 5.3, 5.5, 5.6; Mệnh đề 03.9 (ba dạng, gồm thuật toán trả phần rò rỉ của trang chiếu MMDS tr.52); Mệnh đề 03.17 (công thức không bù và chuẩn hóa lại, Q8); Định lý 03.15 dạng khối bốn phần (Giả thiết, Kết luận gồm (a)–(c), Điều kiện áp dụng, Phạm vi), chứng minh tồn tại–duy nhất qua tính khả nghịch của $\mathrm I_n-\beta\bar M$ (deck s03-14 chỉ phát biểu tính co, chứng minh Cauchy trong ghi chú diễn giả; ghi chú nêu cách Cauchy thành một câu); Hệ quả 03.16 trong mạch chính (deck s03-12 chỉ nói "chặn sai số"); vai trò giả thiết "Bỏ …" có số cho Mệnh đề 03.11, 03.13, Định lý 03.15, Mệnh đề 03.23, 03.26–03.29; bảng chi phí cho Thuật toán 03.22, 03.31; phần đọc thêm loại nút cụt đệ quy; Bài 5.1.3, 5.1.5–5.1.7, 5.2.3, 5.2.4 và Bài tập 03.2, 03.6 (deck không có); công thức $\Delta_t=\tfrac15(2/5)^t$ giải thích 20 vòng của `base` (Ví dụ 03.24).
- Số liệu lệch deck: deck s05-05 ghi $H=96\to84$, $C=248\to236$; ghi chú tính cả 4 cặp khởi tạo theo Định nghĩa 02.33 nên $H=144\to132$, $C=296\to284$, Combine giảm $1/12$ của $H$, $\approx4{,}1\%$ của $C$ (A2). $Q=84$ của deck s05-07 giữ trong ghi chú với giả thiết các cặp khởi tạo được tạo trên máy chạy Reduce. Ghi chú nêu $Q$ một nghĩa: byte Map→Reduce qua mạng (A3).
- Thứ tự: s03-15 (cộng đóng góp về A) là Ví dụ 03.15 ở Mục 3.2, như deck sau lượt sửa 2026-10-14.
- Đề recitation: deck s07-04…s07-07 ghi lời giải ở "ghi chú bài giảng, mục 7, Bài 1–4" và có hướng dẫn chấm; nay lời giải nằm ở `exercises.md`: s07-04 ↔ Bài tập 03.8 (5.1.1), s07-05 ↔ 03.9 (5.1.2), s07-06 ↔ 03.10 (5.2.1), s07-07 ↔ 03.7 (5.2.2); dẫn chiếu của deck lỗi thời (ghi lệch, không sửa deck).
- Giả mã tiếng Việt (deck s03-11 trộn "Delta", "new"); "véc-tơ" (deck "véc tơ").
- Nguồn quy mô $10^9$: ghi chú dẫn trang chiếu MMDS tr.48 (deck dẫn CS246 tr.51, cùng số). CS246 09 ghi hai tác giả Leskovec và Kanatsoulis.
- `desc` của hai SVG dùng chung với deck không khớp hình (không sửa ở lượt này, theo phạm vi ghi): `model-spider-trap.svg` nói có "nhãn C tới C đặt trên vòng lặp" nhưng hình không có nhãn; `visual-contraction.svg` nhắc "Công thức trên slide". Văn bản thay thế trong ghi chú mô tả đúng hình.

### Tương ứng ký hiệu deck ↔ ghi chú

| Deck | Ghi chú | Lý do |
|---|---|---|
| $T_{\max}$ (s03-11, s06-02) | $K$ | khớp Bài 04 (Q5) |
| $L$ số vòng (s05-08) | $t_{\text{dừng}}$ | $L_i$ là danh sách giá trị của Bài 02 (Q5) |
| $p$ số máy (s05-01) | $P$ | ký hiệu Bài 02 (Q5) |
| chỉ số máy (Bài 02 $u$) | $\nu$, $t_\nu$ | $u$ là phân phối đều (A5) |
| $b_{\text{eff}}$ | $b_{\text{eff}}$ (giữ), định nghĩa là băng thông của đường nối dùng chung mà mọi byte của $Q$ đi qua | Bài 02 viết $B$, nhưng deck dùng $B$ cho bộ nhớ (Q5); điều kiện của Mệnh đề 02.38 (A3) |
| $c_e$ | $c_e$ (giữ) | Bài 02 viết $\tau$ cho thời gian một phép cộng, trùng ngưỡng $\tau$ (Q5) |
| $B$ bộ nhớ một tác vụ (s05-01) | $B_{\text{task}}$ | luôn có chỉ số |
| $S_4=8/3$ (s05-06, nói "tăng tốc") | "mức tăng tốc $8/3$", không dùng chữ $S$ | $S$ là dung lượng (A5) |
| $\bar M=M_0+uz^{\mathsf T}$ (ghi chú diễn giả s03-14) | $\bar M=M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$ | $z=M_0r$ ở Mục 3 (Q6) |
| $I$ ma trận đơn vị (không có ở deck) | $\mathrm I_n$ | $I$ là đầu vào Map (A5) |
| $S$ trong thuật toán trả phần rò rỉ (nguồn) | $s$ | $S$ là dung lượng |
| tên trang A, B (nghiêng hoặc thường) | $\mathrm A$, $\mathrm B$ chữ đứng; Hình 5.7 $\mathrm a,\mathrm b,\mathrm c$, điểm $r_{\mathrm a}$ | không lẫn $B_{\text{task}}$, $C=I+H$ (Q5, A5) |
| (không có) | $\mathcal D$, $n_+$, $R$, $q$, $W$, $w_{\max}$, $\varepsilon$, $\sigma$ (tổng điểm của công thức không bù) | thêm cho các mệnh đề |

### Lệch thuật ngữ với Bài 04 (sửa ở đợt B4, không sửa ở lượt này)

Bài 04 viết $\ell$ cho số cạnh (Bài 03: $m$), $\bar M=M_0+uz^{\mathsf T}$ (Bài 03: $\mathbf 1_{\mathcal D}$), "vector" (Bài 03: "véc-tơ"), "cụm thao túng liên kết" (Bài 03: "trại thư rác"), "phân phối dịch chuyển" (Bài 03: "phân phối nhảy", có ghi chú tên của Bài 04); câu "Bài 03 viết $T_{\max}$" ở deck Bài 04 lỗi thời; `planning/lec-04/outline.md` còn ghi "$\bar M$ là ma trận $S$ của Bài 03".

## Sửa deck theo bảng phát hiện 2026-11-13

Deck sửa theo bảng phát hiện 2026-11-13 trong `review-log.md` và quyết định G1–G18, D03 của điều phối viên; ghi chú bài giảng là chuẩn nội dung. Deck 72 → 82 trang (73 trang giảng, 120 phút; 9 trang bài tập, 60 phút). Chi tiết từng trang: `storyboard.md`, mục cùng tên. Mục này thay các điểm sau của các mục trên: "véc tơ" (quyết định 7 cũ) thành "véc-tơ" (quyết định người dùng 2026-11-13); "Cận sai số hậu nghiệm chỉ đọc thêm" thành nội dung chính (Hệ quả 03.16); danh sách "Khác biệt với bộ trang chiếu" và bảng "Tương ứng ký hiệu deck ↔ ghi chú" đã được xử lý trên deck.

**Mục tiêu học tập trên deck** (theo sáu mục tiêu chính của ghi chú, note:11–16; mục tiêu đọc thêm không lên deck):

1. Lập ma trận liên kết, tính một vòng, giải $r=M_0r$ có tổng 1.
2. Nhận diện nút cụt, bẫy liên kết; tính một vòng đầy đủ; giải hệ có bước nhảy.
3. Chứng minh bảo toàn tổng, hội tụ; chọn ngưỡng dừng từ cận sai số.
4. Lưu liên kết ra, chia khối; đặc tả Map, Combine, Reduce; chứng minh tính đúng.
5. Tính dung lượng, bộ nhớ tác vụ, đầu vào Map, Reduce (có, không Combine), thời gian Map.
6. Chạy `pagerank.py`, đối chiếu tính tay.

**Mạch và thứ tự.**

| Mạch | Tên | Trang (thứ tự deck) | Số trang | Phút |
|---|---|---|---:|---:|
| 1 | Bài toán xếp hạng trang web | s01-01, s01-07, s01-03, s01-02, s01-06, s01-04, s01-05, s02-02, s02-03, s02-04, s02-05, s02-07, s02-08 | 13 | 21 |
| 2 | Mô hình và thuật toán PageRank | s03-00, s03-01, s03-02, s03-03, s03-17, s03-04…s03-12, s03-18, s03-19, s03-13, s03-14, s03-20, s03-21, s03-22, s03-16 | 22 | 39 |
| 3 | Tính PageRank trên đồ thị lớn | s04-00, s04-01, s04-02, s03-15, s04-03, s04-11, s04-04, s04-05, s04-06, s04-09, s04-07, s04-08, s04-12, s04-10 | 14 | 22 |
| 4 | Chi phí và lợi ích của cách tính | s05-00…s05-09 | 10 | 15 |
| 5 | Thực hành tính PageRank | s06-00…s06-07 | 8 | 13,5 |
| 6 | Tổng kết và tự kiểm tra | s07-00, s07-02, s07-08, s07-01, s07-03, s07-09 | 6 | 9,5 |
| 7 | Bài tập vận dụng | s07-T, s07-07, s07-10, s07-04, s07-11, s07-05, s07-12, s07-06, s07-13 | 9 | 60 |

Trang mới: s03-17 (cấu trúc nơ thắt), s03-18 (Tính đúng: PageRank lặp, Mệnh đề 03.11), s03-19 (Chi phí: một vòng PageRank lặp), s03-20 (Chứng minh: hội tụ, Định lý 03.15), s03-21 (Cận sai số khi dừng, Hệ quả 03.16), s03-22 (Ví dụ 03.13), s04-12 (Chi phí: một vòng theo khối), s07-10…s07-13 (bốn trang "Lời giải:"). Gộp: s02-06 vào s02-05. Tách: s03-14 thành s03-14 và s03-20. Trang bài toán có hình đầu mạch 3, 4, 5: s04-01, s05-01, s06-01.

**Ký hiệu và thuật ngữ trên deck (theo bảng ký hiệu của ghi chú).** $K$ số vòng tối đa; $t_{\text{dừng}}$ số vòng thực chạy; $P$ số máy; $B_{\text{task}}$, $B_{\text{buf}}$ bộ nhớ; $b_{\text{eff}}$ băng thông; $\mathbf 1_{\mathcal D}$ trong $\bar M=M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$ (ghi chú diễn giả); $\mathrm I_n$ ma trận đơn vị; tên trang chữ đứng ($r_{\mathrm A}$); "véc-tơ"; "dải tổng" $z_a$; "phần chung"; "người lướt ngẫu nhiên (random surfer)"; "bước nhảy (còn gọi là dịch chuyển, teleport)"; "đánh thuế (taxation)" trong ghi chú diễn giả; "cấu trúc nơ thắt (bowtie)", "thành phần liên thông mạnh (SCC)". Số liệu theo ghi chú: $H$ 144 → 132 byte, $C$ 296 → 284 byte; $m\approx10^{10}$, $4{,}4\cdot10^{10}$ byte, 86 vòng cho sai số $10^{-8}$; nguồn quy mô $10^9$ trang là trang chiếu MMDS tr.48.
