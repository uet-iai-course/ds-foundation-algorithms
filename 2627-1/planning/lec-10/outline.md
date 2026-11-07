# Bài 10: Nén dữ liệu không mất thông tin

> Ghi chú phạm vi (2026-11-08): các mục "Mục tiêu và phạm vi", "Nguồn và quyết định chọn nguồn", "Dàn ý và thời lượng", "Chức năng của sáu mạch", "Bản đồ chu trình học tập", "Thuật ngữ và ký hiệu", "Tài sản trực quan" và "Tên mạch và trang tiêu đề mạch" dưới đây là của **deck cũ** (sáu mạch, ký hiệu $[L,H)$, $C_s$, $D_s$), giữ nguyên chờ làm lại deck. Phần ghi chú bài giảng viết lại ngày 2026-11-08 nằm ở mục "Ghi chú bài giảng (bản 2026-11-08)" cuối tệp và thay cho bản đồ `L10-N01…N10` cũ (bảng ánh xạ ở cùng mục).

## Mục tiêu và phạm vi

Sau phần giảng, sinh viên có thể:

1. đặc tả bài toán nén không mất thông tin, phân biệt trục mô hình tĩnh/cập nhật với trục bộ mã Huffman/số học;
2. dựng, dùng và giải thích tính tối ưu của mã Huffman tĩnh;
3. mô phỏng `ESCAPE`, `EOS` và phép đổi của Huffman thích nghi theo biến thể Nelson–Gailly; giải thích điều kiện và mục đích dựng lại khi đạt ngưỡng;
4. mã hóa, giải mã một thông điệp bằng khoảng nửa mở của mã hóa số học;
5. dùng tự thông tin và entropy để giải thích độ dài của một chuỗi cụ thể;
6. nêu điều kiện đồng bộ, kết thúc dòng, chi phí và giới hạn của ba cặp mô hình–bộ mã được học.

Phần giảng dài 120 phút. Phần bài tập dài 60 phút và nằm sau phần giảng trong cùng tệp HTML.

## Nguồn và quyết định chọn nguồn

| Cụm | Nguồn trục | Nguồn đối chiếu | Quyết định |
|---|---|---|---|
| Mã tiền tố và Huffman | Nelson–Gailly, Ch.3, PDF tr.31–37 | Stanford EE398A, *Entropy and Lossless Coding*; Stanford CS106B, *Huffman Coding*; CMU `compression1-2.pdf` | Giữ dữ liệu A–E và mã của sách; dùng Stanford cho nhịp trực quan cây và hàng đợi; dùng CMU cho Kraft. Viết lại chứng minh trao đổi với mệnh đề, phép đổi và cấu trúc con tối ưu. |
| Huffman thích nghi | Nelson–Gailly, Ch.4: tính chất và Hình 4.2–4.3 ở PDF tr.67–71; `ESCAPE` ở tr.73–74; cập nhật, chống tràn và dựng lại ở tr.75–85; lá mới trọng số 0 ở tr.82–83 | CMU `compression3.pdf` | Chỉ dùng biến thể trong sách: `ESCAPE`, `EOS`, tính chất anh em, đổi nút và dựng lại. Vết ký hiệu mới gồm `ESCAPE`, tám bit thô, lá trọng số 0 và cập nhật. Không dùng tên NYT, FGK hay Vitter. Không dùng Hình 4.1 vì hình và lời mô tả lệch nhau. |
| Mã hóa số học | Nelson–Gailly, Ch.2 và Ch.5, PDF tr.96–104 | Stanford EE398A, *Arithmetic Coding*, trang chiếu 10–12 và 16; CMU `compression1-2.pdf` | Giữ ví dụ “BILL GATES”, khoảng nửa mở, phát tiền tố chung và underflow theo sách. Dùng Stanford để đối chiếu số học hữu hạn và phép dịch; nhãn E1/E2/E3 là nhãn theo dõi của deck, không quy cho Stanford. Erratum bảng giải mã chỉ ghi trong ghi chú và nhật ký. |
| Bài tập | Nelson–Gailly, các ví dụ Ch.3–4; CMU Assignment 1a, Problem 3 | CMU solution | Người dùng đã phê duyệt ngoại lệ nguồn ngày 2026-08-28: X01–X02 chuyển ví dụ Nelson–Gailly thành bài luyện; X03 dùng CMU Assignment 1a, Problem 3. |

MMDS không bao phủ mô-đun nén này, nên không có cụm tương đương để ưu tiên hoặc Việt hóa.

## Dàn ý và thời lượng

| Phần | Mã trang | Thời lượng |
|---|---|---:|
| Đặt bài toán và mô hình chung | P00–P02 | 9 phút |
| Mã tiền tố và Huffman tĩnh | H00–H13 | 38 phút |
| Huffman thích nghi | A00–A10 | 30 phút |
| Mã hóa số học | R00–R13 | 36 phút |
| Chọn bộ mã hóa và tổng hợp | S00–S01 | 7 phút |
| Bài tập recitation | X00–X03 | 60 phút |

Tổng phần giảng: 120 phút. Phần recitation đủ 60 phút theo ngoại lệ nguồn được người dùng phê duyệt ngày 2026-08-28; không còn lỗi chặn hoặc nghiêm trọng.

## Chức năng của sáu mạch

| Mạch | Chức năng | Kết nối vào | Đầu ra cho mạch sau | Đóng góp vào mục tiêu |
|---|---|---|---|---|
| Đặt bài toán và mô hình chung | Tách mô hình xác suất khỏi bộ mã hóa, đặt yêu cầu khôi phục chính xác. | Kiến thức tiên quyết về xác suất, cây và hàng đợi ưu tiên. | Ma trận lựa chọn và tiêu chí giao thức. | Mục tiêu 1 và 6. |
| Mã tiền tố và Huffman tĩnh | Đi từ miền độ dài khả thi đến thuật toán tham lam và lập luận tối ưu. | Ma trận có ô tĩnh + Huffman. | Chi phí đếm trước và truyền cây làm động cơ cho cập nhật trực tuyến. | Mục tiêu 2. |
| Huffman thích nghi | Xây cây đồng bộ khi chưa biết thống kê, gồm ký hiệu mới, đổi nút và dựng lại. | Nhược điểm đầu mục của mô hình tĩnh. | Phân biệt chi phí mô hình với giới hạn độ dài nguyên bit. | Mục tiêu 3 và 6. |
| Mã hóa số học | Mã cả chuỗi bằng khoảng, thêm cách dừng và chuẩn hóa hữu hạn. | Giới hạn một từ mã nguyên bit cho mỗi ký hiệu. | Quan hệ độ rộng khoảng, tự thông tin và chi phí triển khai. | Mục tiêu 4 và 5. |
| Chọn bộ mã hóa và tổng hợp | Thu hồi hai trục và liệt kê thông tin giao thức cần để giải mã đúng. | Ba cặp đã phân tích. | Tiêu chí lựa chọn và yêu cầu giải trình cho bài tập. | Mục tiêu 1 và 6. |
| Bài tập recitation | Buộc sinh viên tạo cây, vết cập nhật và vết khoảng có thể chấm. | Thuật toán, bất biến và quy ước của năm mạch giảng. | Ba sản phẩm luyện tập kèm hướng dẫn chấm. | Kiểm tra toàn bộ sáu mục tiêu. |

## Bản đồ chu trình học tập

| Cụm | Tình huống | Vấn đề | Trực giác | Chạy tay | Hình thức | Thuật toán và tính đúng | Chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| Huffman tĩnh | H00 | H01 | H02–H03 | H04–H08 | H02, H09 | H09–H11 | H12 | H13 |
| Huffman thích nghi | A00 | A01–A02 | A03 | A02, A04–A06 | A03, A07 | A07–A08 | A09 | A10 |
| Mã hóa số học | R00 | R01 | R02 | R03–R04 | R05, R08 | R06–R07, R09–R11 | R12 | R13 |

## Thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Cách dùng |
|---|---|
| mã tiền tố | Không từ mã nào là tiền tố của từ mã khác. |
| $f_s$, $p_s$ | Tần suất và xác suất của ký hiệu $s$. |
| $\ell_s$ | Độ dài từ mã của $s$. |
| $L,H$ | Cận dưới và cận trên của khoảng nửa mở $[L,H)$. |
| $C_s,D_s$ | Cận tích lũy dưới và trên của ký hiệu $s$. |
| $I(x)$ | Tự thông tin của một chuỗi cụ thể, bằng $-\log_2 p(x)$. |
| $H(P)$ | Entropy, tức tự thông tin trung bình theo phân phối $P$. |
| `ESCAPE` | Lá báo ký hiệu chưa có trong cây; theo sau bởi biểu diễn thô của ký hiệu. |
| `EOS` | Ký hiệu kết thúc dòng. |
| tính chất anh em | Có thể liệt kê nút theo trọng số không giảm sao cho hai nút anh em đứng kề nhau. |

## Tài sản trực quan

Tất cả hình được vẽ lại bằng SVG trong `2627-1/img/lec-10/`: cây tiền tố và tám miền Kraft; chuỗi ghép Huffman A–E; cây mã/giải mã; các mức phóng đại khoảng “BILL GATES”; chuẩn hóa giải mã; E1/E2/E3 theo khoảng nửa mở; tăng trọng số; đổi nút; hai đường ống `ESCAPE`/`EOS`.

## Tên mạch và trang tiêu đề mạch (2026-10-14)

Mỗi mạch trừ mạch mở đầu mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên trùng từng chữ với trang Nội dung. Deck 54 trang.

| N | Tên mạch | Trang tiêu đề mạch | Trang nội dung đầu mạch |
|---:|---|---|---|
| 1 | Mở đầu | P00 (trang bìa) | — |
| 2 | Mã Huffman tĩnh | HT | H00 |
| 3 | Huffman thích nghi | AT | A00 |
| 4 | Mã hóa số học | RT | R00 |
| 5 | Tổng kết và tự kiểm tra | ST | S00 |
| 6 | Bài tập vận dụng | XT | X00 |

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
| `lec-10-topic-14` | `ESCAPE`, `EOS`, lá trọng số 0 và đồng bộ | cốt lõi; Mệnh đề 10.27 là bổ sung | 4.3 | NG tr.73–74, 79–83, 87, 90 | Ví dụ 10.14; Thuật toán 10.26; Mệnh đề 10.27; Bài tập 10.16 |
| `lec-10-topic-15` | Chống tràn và dựng lại cây | cốt lõi; quan hệ Fibonacci chu trình rút gọn, chứng minh ngoài phạm vi | 4.4 | NG tr.74–77, 84–88, 91 | Ví dụ 10.15, 10.16; Nhận xét 10.28; Thuật toán 10.29; Bài tập 10.5 |
| `lec-10-topic-16` | Khoảng của chuỗi; mã hóa và giải mã với số thực | cốt lõi; chứng minh Mệnh đề 10.31 là bổ sung | 5.1–5.2 | NG tr.96–99; CMU tc.37–44; EE398A-3 tc.2–7 | Định nghĩa 10.30; Ví dụ 10.17, 10.18; Mệnh đề 10.31; Thuật toán 10.32 |
| `lec-10-topic-17` | Cách dừng, khoảng mã và cận độ dài | cốt lõi; Mệnh đề 10.33, phần (a) và cận dưới (c) của Định lý 10.34, Hệ quả 10.35 là bổ sung | 5.3–5.4 | NG tr.99, 104; CMU tc.38, 45–51; EE398A-3 tc.5 | Mệnh đề 10.33; Ví dụ 10.19; Định lý 10.34; Hệ quả 10.35; Bài tập 10.6 |
| `lec-10-topic-18` | Thanh ghi hữu hạn và phát tiền tố chung | cốt lõi, chu trình gộp với topic-19 | 6.1 | NG tr.100–102, 105–107, 111 | Định nghĩa 10.36; Ví dụ 10.20 |
| `lec-10-topic-19` | Tràn dưới, bit chờ và ràng buộc số đếm | cốt lõi; Bổ đề 10.38, 10.39 là bổ sung | 6.2 | NG tr.102–103, 107–112; CMU tc.53–55 | Thuật toán 10.37; Ví dụ 10.21 (vết cbb); Bổ đề 10.38, 10.39; Bài tập 10.7, 10.17 |
| `lec-10-topic-20` | Giải mã nguyên và kết thúc dòng | cốt lõi; chứng minh đầy đủ Mệnh đề 10.41 ngoài phạm vi | 6.3 | NG tr.103, 105–106, 113–114, 385 | Thuật toán 10.40; Mệnh đề 10.41; bảng chi phí mã số học |
| `lec-10-topic-21` | Chọn cặp mô hình–bộ mã | cốt lõi, chu trình rút gọn | 7 | NG tr.23–24, 66–67; tổng hợp Mục 1–6 | bảng so sánh; Bài tập 10.8 |
| `lec-10-topic-22` | Tình huống áp dụng và ứng dụng | cốt lõi | Tình huống | NG tr.22, 24, 37, 67, 96, 104; CMU tc.2–3 | Tình huống 10.1–10.3 |
| `lec-10-topic-23` | Tóm tắt chương | cốt lõi | Tóm tắt | — | đoạn tóm tắt, danh mục kết quả, công thức, giả thiết |
| `lec-10-topic-24` | Bài tập củng cố | cốt lõi | Bài tập | CMU tc.22, 49; CMU-A1 bài 2–4; NG tr.22, 24, 32–37, 69–72 | đoạn dẫn và liên kết trong ghi chú; Bài tập 10.9–10.21 với gợi ý và lời giải nằm ở `materials/lec-10/exercises.md` (tách vì ghi chú vượt 32 000 âm tiết, quyết định của điều phối viên 2026-11-08; recitation: 10.11, 10.12, 10.14, 10.15) |
| `lec-10-topic-25` | Hướng dẫn đọc thêm và tài liệu tham khảo | đọc thêm | Tham khảo | NG; CMU; EE398A; CS106B | danh mục nguồn có trang; bảng "Nguồn của các chứng minh" |

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
