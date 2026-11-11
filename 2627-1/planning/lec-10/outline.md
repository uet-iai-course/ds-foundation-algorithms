# Bài 10: Nén dữ liệu không mất thông tin

> Ghi chú phạm vi (2026-11-08): các mục từ "Mục tiêu và phạm vi" tới "Tên mạch và trang tiêu đề mạch" là dàn ý của **bộ trang chiếu mới** (bảy mạch, viết lại từ ghi chú `materials/lec-10/lecture-note.md` và `exercises.md`, commit `51cb9ad`), thay toàn bộ dàn ý của deck cũ. Mục "Ghi chú bài giảng (bản 2026-11-08)" cuối tệp giữ nguyên.

## Mục tiêu và phạm vi

Đối tượng: sinh viên năm 2 (lập trình, toán rời rạc, xác suất cơ bản, cây và hàng đợi ưu tiên). 120 phút giảng và 60 phút bài tập vận dụng trong cùng tệp HTML.

Mục tiêu học tập trên deck (P02), mỗi mục một sản phẩm kiểm được:

1. Đặc tả nén; chứng minh không mã nào rút ngắn mọi thông điệp; tách mô hình, bộ mã. Kiểm: T05 câu 1 (đếm chuỗi), P07; tách mô hình khỏi bộ mã kiểm cùng T05 câu 2.
2. Kiểm mã tiền tố, tổng Kraft; tính entropy, chứng minh hai cận. Kiểm: K21 (trường hợp dấu bằng), X01 (Kraft bằng cách đếm lá).
3. Chạy Huffman tĩnh; chứng minh tối ưu; đếm chi phí. Kiểm: H17, X02, T05 câu 2.
4. Chạy Huffman thích nghi; chứng minh tăng–đổi giữ tính chất anh em. Kiểm: A20, X03.
5. Mã hóa, giải mã bằng khoảng; chuỗi bit dài dưới $I(x)+2$. Kiểm: X04, T05 câu 3.
6. Chạy mã số học 16 bit với bit chờ; giải thích $N\le2^{R-2}$; chọn cặp mô hình–bộ mã. Kiểm: G06 (Câu hỏi về bit chờ), G15, T05 câu 4; phần chọn cặp: T03, T04.

Sáu mục tiêu của deck gộp mục tiêu 2–3 và 6–7 của ghi chú. Ngoài phạm vi mặt trang (chỉ ở ghi chú bài giảng hoặc ghi chú diễn giả): chứng minh McMillan, mã khối $j$ ký hiệu, Mệnh đề 10.33 (chứng minh và phát biểu ở ghi chú diễn giả), chứng minh Mệnh đề 10.27 và Bổ đề 10.24 (ghi chú diễn giả), mã số học thích nghi (NG Chương 6), cách lan truyền nhớ của EE398A-3, `scale_counts`, cận Fibonacci tổng quát, chứng minh đầy đủ Mệnh đề 10.41.

## Nguồn và quyết định chọn nguồn

- Trục nội dung: ghi chú bài giảng Bài 10 (mọi định nghĩa, kết quả, ví dụ và số trên mặt trang lấy từ ghi chú hoặc `exercises.md`; K3).
- Nguồn của ghi chú, ghi ở ghi chú diễn giả và trang "Nguồn và tài liệu đọc": Nelson và Gailly, *The Data Compression Book*, ấn bản 2 (NG), Chương 2–5, trang PDF; Blelloch, CMU 15-499 *Data Compression* phần 1–2 và Assignment 1a (CMU, CMU-A1); Girod, Stanford EE398A *Entropy and Lossless Coding*, *Arithmetic Coding* (EE398A-1, EE398A-3); Stanford CS106B *Huffman Coding*.
- MMDS không có chương nén, nên không có ghi công `mmds.org` (Q1, K3).
- Nhịp theo nguồn: mô hình–bộ mã theo NG Hình 2.1 và CMU tc.8; mã tiền tố theo nhịp CS106B (thất bại → định nghĩa → giải mã trên cây) với dữ liệu CMU tc.22 và NG; Kraft qua khoảng mã (CMU tc.45–47, EE398A-1 tc.15–16), cách đếm lá để dành recitation; Huffman theo dữ liệu NG, bảng vết kiểu CS106B, hình kiểu CMU tc.34; tối ưu theo khung CMU tc.31, 36; Huffman thích nghi theo NG Chương 4, mỗi trạng thái một hình; mã số học theo NG (BILL GATES), hình khoảng lồng kiểu EE398A-3 tc.3–4, hình thức hóa CMU tc.45–51; thanh ghi theo NG và CMU tc.55. Thứ tự mã tiền tố → Kraft → entropy theo ghi chú (Q2), khác CMU, EE398A, NG; con số "eeeee" ở P04 (ghi chú diễn giả) giữ trực giác thông tin sớm.
- "Đọc trước:" NG Chương 2–5 (D6).

## Dàn ý và thời lượng

| Mạch | Trang | Phút | Nội dung |
|---|---:|---:|---|
| 1 Mở đầu | 12 | 13 | bìa, tiên quyết, mục tiêu, nội dung, vấn đề trung tâm (hai trang), A–E với mã cố định, đặc tả, Mệnh đề 10.2, chữ u, mô hình–bộ mã, bốn thành phần |
| 2 Mã tiền tố, bất đẳng thức Kraft và entropy | 15 | 20 | 1011 ba cách đọc, mã tiền tố, cây mã và giải mã, Mệnh đề 10.6, khoảng mã, bốn tổng Kraft và dựng mã (một trang), Định lý 10.9 và chứng minh, tự thông tin và entropy, độ dài trung bình và ví dụ A–E, cận dưới và chứng minh, độ dài Shannon kèm ví dụ 102 bit, Câu hỏi dấu bằng |
| 3 Mã Huffman tĩnh | 16 | 21,5 | số bit tối thiểu, Shannon–Fano, dựng từ lá, bốn lượt ghép, cây và bảng mã, giả mã, phép đổi chỗ, Bổ đề 10.16 và chứng minh, Định lý 10.18 và chứng minh, Hệ quả 10.19, chi phí, đầu mục, Câu hỏi năm ký hiệu lệch |
| 4 Mã Huffman thích nghi | 18 | 24 | một lượt không đầu mục, danh sách nút, tính chất anh em, Định lý 10.22, tăng A từ 1 lên 3 (hai trang), UPDATE, Định lý 10.25 và hai trang tính đúng (Bổ đề 10.24 ở hàng "Hợp lệ"), chi phí, ESCAPE/EOS, thêm E, bộ nén–giải nén kèm điều kiện đồng bộ, chống tràn, dựng lại, Câu hỏi bộ giải mã bỏ phép đổi |
| 5 Mã số học | 25 | 34 | giới hạn 1 bit, thu hẹp B, I, L, khoảng chuỗi, mã hóa BILL GATES, Mệnh đề 10.31, thuật toán số thực, giải mã, bảy chữ A, Định lý 10.34 và chứng minh, Hệ quả 10.35; thanh ghi, năm chữ số thập phân, tràn dưới, ba trường hợp, ENCODE-SYMBOL, vết cbb (hai trang), Bổ đề 10.38, 10.39, giải mã hai ký hiệu đầu, DECODE, chi phí, Câu hỏi bảng số đếm tích lũy |
| 6 Tổng kết và tự kiểm tra | 7 | 7,5 | A–E qua các bộ mã, kết quả và giả thiết, cặp mô hình–bộ mã, trả lời có điều kiện, câu hỏi tự kiểm tra, nguồn |
| **Giảng** | **93** | **120** | |
| 7 Bài tập vận dụng | 12 | 60 | Kraft bằng đếm lá (13), Huffman A–E quy tắc gán bit khác (10), ba lần tăng A (20), giải mã số học bốn chữ (17) |

## Chức năng của bảy mạch

| Mạch | Loại | Chức năng | Đầu vào | Đầu ra |
|---|---|---|---|---|
| 1 | giới thiệu và động lực; khái niệm | đặt bài toán khôi phục từng bit, đặc tả, giới hạn, mô hình–bộ mã | Bài 08, Bài 09 | A–E, Định nghĩa 10.1, 10.3 |
| 2 | khái niệm hoặc mô hình | điều kiện tiền tố, Kraft, entropy, cận hai phía | đặc tả | cây mã, khoảng mã, $[H;\,H+1)$; chưa có cách dựng mã tối ưu |
| 3 | thuật toán và ví dụ vận dụng | Huffman tĩnh, tối ưu, chi phí, đầu mục | cây mã, hai cận | mã tối ưu; giới hạn hai lượt, đầu mục |
| 4 | thuật toán và ví dụ vận dụng | Huffman thích nghi một lượt | thứ tự lấy ra, tối ưu | cây Huffman sau mỗi ký hiệu; giới hạn 1 bit mỗi ký hiệu |
| 5 | thuật toán và ví dụ vận dụng | mã số học số thực và thanh ghi | giới hạn 1 bit, khoảng mã | cận $<I(x)+2$, bộ mã 16 bit đúng khi $N\le2^{R-2}$ |
| 6 | tổng kết | thu hồi và so sánh | mọi kết quả | chọn cặp mô hình–bộ mã; nối Bài 11 |
| 7 | bài tập vận dụng | bốn bài sách | mạch 2–5 | sản phẩm nộp |

## Bản đồ chu trình học tập

Các mã dưới đây liệt kê theo cột chu trình, không theo thứ tự trang. Xem `storyboard.md`, mục "Chu trình học tập theo cụm". Cụm thuật toán theo khuôn của `CLAUDE.md`: Huffman tĩnh (H02 giới hạn 89 bit → H03 "tương tự … nhưng khác ở …" và nhận xét cấu trúc → H04 chạy tay → H06 Đầu vào/Đầu ra, giả mã, phép quyết định → H07–H12 tính đúng → H15 chi phí); tăng–đổi (A01 → A07 → A06 → A10 → A12, A13, A13B → A14); mã số học số thực (S01 → S02 → S04 → S06 → S05, S06 → S06 ghi chú diễn giả); thanh ghi (G01 → G02, G04 → G06 → G05 → G08, G09 → G13), giải mã nguyên (G10 → G11). Chu trình rút gọn có lý do: mô hình–bộ mã (phân loại và giao thức), entropy (đại lượng đo, kết quả ở topic-07), Shannon–Fano (phương pháp trước làm giới hạn, Q3), chi phí và đầu mục (phân tích thuật toán đã có), chống tràn và dựng lại (biến thể phụ của chương trình).

## Thuật ngữ và ký hiệu

Bảng Việt–Anh và bảng ký hiệu của ghi chú ở cuối tệp áp dụng cho deck. Tên tiếng Anh nêu ở lần đầu trên mặt trang: mã ký hiệu (symbol code), từ mã (codeword), giải mã duy nhất (uniquely decodable code) ở P06; cây mã (code tree) ở K04; độ dài trung bình (average length), mã tiền tố tối ưu (optimal prefix code) ở K16; mô hình xác suất (statistical model), tĩnh (static), thích nghi (adaptive), bậc (order), bộ mã (coder) ở P09; quy tắc phá hòa (tie-breaking rule), `EOS` (end of stream) ở P10; tiền tố (prefix), mã tiền tố (prefix code), mã tức thời (instantaneous code) ở K02; khoảng mã (code interval), tổng Kraft (Kraft sum) ở K08; tự thông tin (self-information), entropy ở K15; đầu mục (header) ở H16; cây có trọng số (weighted tree), tính chất anh em (sibling property) ở A03; xác suất tích lũy (cumulative probability), khoảng ký hiệu (symbol interval), khoảng chuỗi (sequence interval) ở S03; thanh ghi (register) ở G01; tràn dưới (underflow) ở G03; chuẩn hóa (renormalization), bit chờ (pending bits) ở G04; cây nhị phân hoàn hảo (perfect binary tree) ở X01. Mặt trang dùng "mã số học", "mô hình thích nghi", "số đếm", "Lời giải".

## Tài sản trực quan

17 SVG mới trong `img/lec-10/`, sinh bởi `../tools/courses/ds-foundation-algorithms/2627-1/img/lec-10/generate_deck_svg.py` (danh sách và trang dùng ở `storyboard.md`, mục "Hình"). Rộng 1 200 đơn vị, cao theo khung hiển thị của lớp `.stream-figure` (360 px), `.stream-short` (270 px), `.stream-mini` (150 px), `.stream-tall` (520 px), chữ nhỏ nhất 20 đơn vị, nên nhãn khi chiếu ở 1280×720 khoảng 18–24 px. Lớp gốc của deck là `reveal course-deck lecture-compression`; `lecture-course.css` chỉ thêm `.lecture-compression` vào các selector của khối Bài 08 (D5).

## Tên mạch và trang tiêu đề mạch

| N | Mã | `id` | Tên mạch | Dòng dẫn (âm tiết) | Từ khóa |
|---:|---|---|---|---|---|
| 2 | KT | `mach-2` | Mã tiền tố, bất đẳng thức Kraft và entropy | Muốn chọn độ dài từ mã ngắn mà vẫn giải mã được, phải có điều kiện tiền tố, tổng Kraft và mức đích entropy. (24) | Mã tiền tố · Cây mã · Tổng Kraft · Entropy · Cận hai phía |
| 3 | HT | `mach-3` | Mã Huffman tĩnh | Muốn có mã tiền tố tối ưu cho một bảng số đếm, phải ghép hai nút nhẹ nhất từ lá lên gốc. (22) | Shannon–Fano · Hàng đợi ưu tiên · Phép đổi chỗ · Tính tối ưu · Đầu mục |
| 4 | AT | `mach-4` | Mã Huffman thích nghi | Muốn nén một lượt mà không gửi bảng số đếm, phải cập nhật cây Huffman cục bộ sau mỗi ký hiệu. (22) | Tính chất anh em · Nút cuối khối · ESCAPE và EOS · Đồng bộ hai phía · Dựng lại cây |
| 5 | ST | `mach-5` | Mã số học | Muốn dùng dưới một bit cho ký hiệu xác suất lớn, phải mã cả thông điệp bằng một khoảng số. (20) | Khoảng chuỗi · Ký hiệu kết thúc · Cận độ dài · Thanh ghi 16 bit · Bit chờ |
| 6 | TT | `mach-6` | Tổng kết và tự kiểm tra | Muốn chọn bộ nén cho một tệp, phải đặt giả thiết, bảo đảm và chi phí của ba bộ mã cạnh nhau. (22) | — |
| 7 | XT | `mach-7` | Bài tập vận dụng | Muốn vận dụng Kraft, hai mã Huffman và mã số học, phải chạy tay và chứng minh trên bài của sách và CMU 15-499. (23) | Đếm lá · Lượt ghép · Nút cuối khối · Giải mã khoảng |

Tên mạch khác tiêu đề trang nội dung đầu mạch (K01, H01, A01, S01, T01, X01). Câu luận đề trang bìa: "Mã Huffman cách entropy dưới một bit mỗi ký hiệu; mã số học lý tưởng cách tự thông tin của thông điệp dưới hai bit." (25 âm tiết, D7).

## Ghi chú bài giảng (bản 2026-11-08)

Tệp: `materials/lec-10/lecture-note.md`. Căn cứ: `decisions.md` (Q1–Q20, M1–M15) và bản đồ chủ đề cuối của điều phối viên. Trục nguồn Nelson–Gailly 2e (NG) Chương 2–5; đối chiếu CMU 15-499 (CMU, CMU-A1), Stanford EE398A (EE398A-1, EE398A-3), Stanford CS106B. MMDS không có chương nén (Q1). Trang NG là trang PDF (Q9). Ghi chú không có mục "Bản đồ chủ đề" (M15); bảng dưới là bản đồ chủ đề, và chú thích `note-topic-id` nằm trong thân ghi chú.

### Mục tiêu học tập của ghi chú

1. Đặc tả nén không mất thông tin, tách mô hình khỏi bộ mã, chứng minh không mã nào rút ngắn mọi thông điệp (Mục 1).
2. Mã tiền tố, giải mã bằng cây, bất đẳng thức Kraft hai chiều và dựng mã từ bộ độ dài (Mục 2).
3. Tự thông tin, entropy, độ dài trung bình; $H\le\bar\ell<H+1$ cho mã tiền tố tối ưu (Mục 2).
4. Huffman tĩnh: chạy, tối ưu, chi phí, đầu mục (Mục 3).
5. Huffman thích nghi theo NG: `ESCAPE`, `EOS`, lá trọng số 0, tăng–đổi, dựng lại; bất biến và đồng bộ (Mục 4).
6. Mã số học với số thực: khoảng nửa mở, giải mã, dừng, cận $\lambda<I(x)+2$ (Mục 5).
7. Mã số học 16 bit: phát tiền tố chung, bit chờ, ràng buộc $N\le2^{R-2}$; chọn cặp mô hình–bộ mã (Mục 6, Mục 7).

### Bản đồ chủ đề (bốn nhóm)

| `note-topic-id` | Chủ đề | Nhóm | Mục | Nguồn chính | Khối chính |
|---|---|---|---|---|---|
| `lec-10-topic-01` | Kiến thức tiên quyết | cầu nối | Tiên quyết | Định nghĩa 08.1, 08.3; Định lý 09.37; Bài 05 Mục 10; CS106B tr.130–132 | danh sách phát biểu lại |
| `lec-10-topic-02` | Đặc tả nén không mất thông tin | cốt lõi; chứng minh Mệnh đề 10.2 là bổ sung | 1.1 | NG tr.18–20, 32–33; CMU tc.7, 22; CS106B tr.182 | Ví dụ 10.1; Định nghĩa 10.1; Mệnh đề 10.2 |
| `lec-10-topic-03` | Mô hình xác suất, bộ mã và giao thức | cốt lõi, chu trình rút gọn | 1.2 | NG tr.19–21, 24, 52, 99; CMU tc.8; EE398A-1 tc.23 | Ví dụ 10.2; Định nghĩa 10.3; Nhận xét 10.4; Bài tập 10.1 |
| `lec-10-topic-04` | Mã tiền tố và cây mã | cốt lõi; chứng minh Mệnh đề 10.6 là bổ sung | 2.1 | CMU tc.20–24; EE398A-1 tc.3–4, 11–15; NG tr.31, 36 | Định nghĩa 10.5; Ví dụ 10.3; Mệnh đề 10.6 |
| `lec-10-topic-05` | Khoảng mã và bất đẳng thức Kraft | cốt lõi; chiều đủ (b), Định nghĩa 10.7, Bổ đề 10.8 là bổ sung; McMillan là đọc thêm | 2.2 | CMU tc.28, 45–47; EE398A-1 tc.12–16; CMU-A1 bài 4A | Định nghĩa 10.7; Bổ đề 10.8; Ví dụ 10.4; Định lý 10.9; Nhận xét 10.10; Bài tập 10.2 |
| `lec-10-topic-06` | Tự thông tin và entropy | cốt lõi, chu trình rút gọn | 2.3 | CMU tc.13–14, 26; EE398A-1 tc.6–8; NG tr.20, 33 | Định nghĩa 10.11; Ví dụ 10.5 |
| `lec-10-topic-07` | Cận entropy cho mã tiền tố | cốt lõi; chứng minh cận dưới là bổ sung | 2.4 | CMU tc.27, 29–30; EE398A-1 tc.10, 12, 17, 20 | Định lý 10.12, 10.13; Ví dụ 10.6; Bài tập 10.3 |
| `lec-10-topic-08` | Shannon–Fano | cầu nối, chu trình rút gọn | 3.1 | NG tr.31–34, 37 | Ví dụ 10.7 |
| `lec-10-topic-09` | Thuật toán Huffman tĩnh | cốt lõi | 3.2 | NG tr.23, 34–36, 51–56; CMU tc.33–35; CS106B tr.130–132 | Ví dụ 10.8; Thuật toán 10.14; Bài tập 10.4 |
| `lec-10-topic-10` | Tính tối ưu của Huffman | cốt lõi; Bổ đề 10.15, 10.17 là bổ sung | 3.3 | CMU tc.26, 31, 36, 56; NG tr.35, 37 | Ví dụ 10.9, 10.10; Bổ đề 10.15–10.17; Định lý 10.18; Hệ quả 10.19 |
| `lec-10-topic-11` | Chi phí và đầu mục của Huffman tĩnh | cốt lõi, chu trình rút gọn | 3.4 | NG tr.24, 52–54, 62, 66–67 | Nhận xét 10.20 |
| `lec-10-topic-12` | Tính chất anh em | cốt lõi; chứng minh Định lý 10.22 là bổ sung | 4.1 | NG tr.67–69, 81, 92 | Ví dụ 10.11; Định nghĩa 10.21; Định lý 10.22 |
| `lec-10-topic-13` | Tăng trọng số và đổi nút | cốt lõi; Bổ đề 10.24 và Định lý 10.25 là bổ sung | 4.2 | NG tr.69–72, 83–84 | Ví dụ 10.12, 10.13; Thuật toán 10.23; Bổ đề 10.24; Định lý 10.25 |
| `lec-10-topic-14` | `ESCAPE`, `EOS`, lá trọng số 0 và đồng bộ | cốt lõi; Mệnh đề 10.27 là bổ sung | 4.3 | NG tr.73–74, 79–83, 87, 90 | Ví dụ 10.14; Thuật toán 10.26; Mệnh đề 10.27 |
| `lec-10-topic-15` | Chống tràn và dựng lại cây | cốt lõi; quan hệ Fibonacci chu trình rút gọn, chứng minh ngoài phạm vi | 4.4 | NG tr.74–77, 84–88, 91 | Ví dụ 10.15, 10.16; Nhận xét 10.28; Thuật toán 10.29; Bài tập 10.5 |
| `lec-10-topic-16` | Khoảng của chuỗi; mã hóa và giải mã với số thực | cốt lõi; chứng minh Mệnh đề 10.31 là bổ sung | 5.1–5.2 | NG tr.96–99; CMU tc.37–44; EE398A-3 tc.2–7 | Định nghĩa 10.30; Ví dụ 10.17, 10.18; Mệnh đề 10.31; Thuật toán 10.32 |
| `lec-10-topic-17` | Cách dừng, khoảng mã và cận độ dài | cốt lõi; Mệnh đề 10.33, phần (a) và cận dưới (c) của Định lý 10.34, Hệ quả 10.35 là bổ sung | 5.3–5.4 | NG tr.99, 104; CMU tc.38, 45–51; EE398A-3 tc.5 | Mệnh đề 10.33; Ví dụ 10.19; Định lý 10.34; Hệ quả 10.35; Bài tập 10.6 |
| `lec-10-topic-18` | Thanh ghi hữu hạn và phát tiền tố chung | cốt lõi, chu trình gộp với topic-19 | 6.1 | NG tr.100–102, 105–107, 111 | Định nghĩa 10.36; Ví dụ 10.20 |
| `lec-10-topic-19` | Tràn dưới, bit chờ và ràng buộc số đếm | cốt lõi; Bổ đề 10.38, 10.39 là bổ sung | 6.2 | NG tr.102–103, 107–112; CMU tc.53–55 | Thuật toán 10.37; Ví dụ 10.21 (vết cbb); Bổ đề 10.38, 10.39; Bài tập 10.7, 10.17 |
| `lec-10-topic-20` | Giải mã nguyên và kết thúc dòng | cốt lõi; chứng minh đầy đủ Mệnh đề 10.41 ngoài phạm vi | 6.3 | NG tr.103, 105–106, 113–114, 385 | Thuật toán 10.40; Mệnh đề 10.41; bảng chi phí mã số học |
| `lec-10-topic-21` | Chọn cặp mô hình–bộ mã | cốt lõi, chu trình rút gọn | 7 | NG tr.23–24, 66–67; tổng hợp Mục 1–6 | bảng so sánh; Bài tập 10.8 |
| `lec-10-topic-22` | Tình huống áp dụng và ứng dụng | cốt lõi | Tình huống | NG tr.22, 24, 37, 67, 96, 104; CMU tc.2–3 | Tình huống 10.1–10.3 |
| `lec-10-topic-23` | Tóm tắt chương | cốt lõi | Tóm tắt | — | đoạn tóm tắt, danh mục kết quả, công thức, giả thiết |
| `lec-10-topic-24` | Bài tập củng cố | cốt lõi | Bài tập | CMU-A1 bài 1–4; NG tr.32–37, 35, 62–63, 69–72 | đoạn dẫn và liên kết trong ghi chú; Bài tập 10.9–10.15 với gợi ý và lời giải nằm ở `materials/lec-10/exercises.md` (tách vì ghi chú vượt 32 000 âm tiết, quyết định của điều phối viên 2026-11-08; recitation: 10.11, 10.12, 10.14, 10.15) |
| `lec-10-topic-25` | Hướng dẫn đọc thêm và tài liệu tham khảo | đọc thêm | Tham khảo | NG; CMU; EE398A; CS106B | danh mục nguồn có trang; chứng minh ngoài phạm vi học phần ghi nguồn trong tài liệu tham khảo |

"tc." là trang chiếu. Lý do chu trình rút gọn: topic-03 là phân loại và giao thức, không có định lý hay thuật toán riêng; topic-06 là đại lượng đo, các kết quả về nó nằm ở topic-07; topic-08 là phương pháp trước dùng làm giới hạn có số (Q3, dưới 500 âm tiết); topic-11 phân tích chi phí của thuật toán đã có; topic-15 phần Fibonacci là kết quả phụ chỉ có phát biểu trong nguồn; topic-18 gộp chu trình với topic-19 vì phát tiền tố chung và tràn dưới là hai nhánh của cùng một vòng chuẩn hóa; topic-21 là tổng hợp.

Đồ thị tiên quyết: 01 → mọi chủ đề; 02 → 03 → (04 → 05 → 07; 06 → 07); 07 → 08 → 09 → 10 → 11; 09–11 → 12 → 13 → 14 → 15; 06, 10 → 16 → 17 (05 → 17 qua Bổ đề 10.8); 17 → 18 → 19 → 20; 09–20 → 21 → 22 → 23; mọi chủ đề nội dung → 24.

### Ánh xạ mã cũ → mới

| Mã cũ (`outline.md` trước 2026-11-08) | `note-topic-id` mới |
|---|---|
| `L10-N01` | `lec-10-topic-02`, `-03` |
| `L10-N02` | `lec-10-topic-04`, `-05` |
| `L10-N03` | `lec-10-topic-08`, `-09`, `-10`, `-11` |
| `L10-N04` | `lec-10-topic-14` |
| `L10-N05` | `lec-10-topic-12`, `-13`, `-15` |
| `L10-N06` | `lec-10-topic-16`, `-17` |
| `L10-N07` | `lec-10-topic-18`, `-19`, `-20` |
| `L10-N08` | `lec-10-topic-06`, `-07` |
| `L10-N09` | `lec-10-topic-21` |
| `L10-N10` | `lec-10-topic-24` |

### Thuật ngữ Việt–Anh của ghi chú

| Tiếng Việt | Tiếng Anh | Ghi chú |
|---|---|---|
| nén không mất thông tin; nén mất thông tin | lossless compression; lossy compression | nén mất thông tin chỉ nhắc làm mốc cho Bài 11 |
| bảng chữ cái; ký hiệu; thông điệp | alphabet; symbol; message | CMU gọi một ký hiệu là "message" |
| mã ký hiệu; từ mã; mở rộng | symbol code; codeword; extension | |
| mã giải mã duy nhất | uniquely decodable code | |
| mã tiền tố | prefix code, prefix-free code, instantaneous code | |
| cây mã | code tree | |
| khoảng mã | code interval | CMU tc.46 |
| tổng Kraft; bất đẳng thức Kraft; bất đẳng thức McMillan | Kraft sum; Kraft inequality; McMillan inequality (Kraft–McMillan) | |
| mô hình xác suất; bộ mã | statistical model; coder | |
| mô hình tĩnh; mô hình thích nghi; bậc | static model (forward adaptation); adaptive model (backward adaptation); order | thuật ngữ trong ngoặc theo EE398A-1 tc.23 |
| đầu mục | header, side information | |
| tự thông tin | self-information, information content | NG tr.20 gọi là "entropy" của ký hiệu |
| entropy; độ dài trung bình; mã tiền tố tối ưu | entropy; average length (expected code length); optimal prefix code | |
| mã Shannon–Fano; mã Huffman; hàng đợi ưu tiên; đống nhị phân | Shannon–Fano coding; Huffman coding; priority queue; binary heap | |
| cây nhị phân đầy đủ | full binary tree | |
| cây có trọng số; tính chất anh em; khối | weighted tree; sibling property; block | "khối" là đoạn liên tiếp cùng trọng số |
| ký hiệu thoát; ký hiệu kết thúc dòng | escape code (`ESCAPE`); end of stream (`EOS`, `END_OF_STREAM`) | Hình 4.5 của NG ghi "EOF" |
| co trọng số; dựng lại cây | rescaling; rebuilding | |
| mã số học; xác suất tích lũy; khoảng ký hiệu; khoảng chuỗi | arithmetic coding; cumulative probability; symbol interval; sequence interval | |
| thanh ghi; chuẩn hóa; nửa dưới, nửa trên, khoảng giữa | register; renormalization; lower half, upper half, middle half | CMU tc.55 gọi ba nhánh theo nửa khoảng; ghi chú không dùng nhãn E1/E2/E3 |
| tràn dưới; bit chờ; bit có nghĩa lớn nhất | underflow; pending bits (NG: underflow bits); most significant bit (MSB) | |
| mã độ dài loạt | run-length coding | chỉ ở phần Ứng dụng |

### Bảng ký hiệu của ghi chú

| Ký hiệu | Ý nghĩa |
|---|---|
| $\Sigma$, $s$, $k$ | bảng chữ cái, ký hiệu, cỡ bảng chữ cái |
| $x=x_1\cdots x_n$, $X$ | thông điệp, thông điệp ngẫu nhiên |
| $c$, $c(s)$, $c^*$, $\ell_s$, $\ell_{\max}$ | mã ký hiệu, từ mã, mở rộng, độ dài từ mã, độ dài lớn nhất |
| $f_s$, $N$ | số đếm, tổng số đếm |
| $p_s$, $P$, $\bar\ell(c)$ | xác suất theo mô hình, phân phối, độ dài trung bình |
| $I(s)$, $I(x)$, $H(P)$ | tự thông tin, entropy |
| $T$, $\operatorname{depth}_T$, $\operatorname{cost}(T)$ | cây mã, độ sâu lá, tổng số bit |
| $v$, $\operatorname{wt}(v)$, $W_{\max}$ | nút, trọng số nút, ngưỡng dựng lại |
| $F(s)$, $[a_t;\,a_t+w_t)$ | xác suất tích lũy trước $s$, khoảng sau $t$ ký hiệu |
| $z$, $\lambda$ | số được phát, số bit |
| $R$, $G(s)$, `low`, `high`, `range`, `code`, $m$ | số bit thanh ghi, số đếm tích lũy, các thanh ghi, số bit chờ |

Ký hiệu cục bộ: $K$ (tổng Kraft, cũng trong bảng ký hiệu của ghi chú), $J(u)$, $z_i$, $\varsigma_1,\ldots,\varsigma_k$ (Mục 2.2, Mục 5.1); $\xi$ (Mục 2.4); $\mathcal Q$ hàng đợi ưu tiên (Mục 3.2); $s_1,s_2,s_{12},T',T^*,\sigma,\sigma',d$ (Mục 3.3); $k'$ số lá, $q$ trọng số nút đang tăng, $\hat v$ nút cuối khối, $h$ số lượt, $\mu_r,\nu_r,\pi_r,\pi$, $\#i$ (Mục 4); $\omega$ trọng số lá khi co, $\mathrm{fib}(i)$ (Mục 4.4); $Q=2^{R-2}$ (trong bảng ký hiệu), $\eta$ điểm trên thang thực, $\mathcal I_0$, $\mathcal I_1$, $m'$, $\psi$ (Mục 6.2); $\gamma$ (Bài tập 10.13), $\delta$ (Bài tập 10.8), $\zeta$ biến chạy của bộ giải mã số thực (Mục 5.2). Chữ $m$ chỉ dùng cho số bit chờ; số lá của cây có trọng số viết $k'$; $\varphi$ chỉ là bộ nén ở Mục 1.

Ký hiệu đã bỏ so với deck cũ: $[L,H)$, $C_s$, $D_s$ (thay bằng $[a_t;\,a_t+w_t)$ và $F(s)$); $T_c$ (thay bằng $N$). Deck cũ còn dùng các ký hiệu đã bỏ; sửa khi làm lại deck.
