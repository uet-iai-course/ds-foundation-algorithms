# Storyboard Bài 06: Tìm cặp tương đồng bằng LSH

Bản viết mới ngày 28-09-2026, đã được gate độc lập PASS và điều phối viên chấp nhận trước triển khai. Chỉ dùng sườn MMDS 3e §§3.4–3.8 và các quyết định đã duyệt trong `outline.md`. Các mã trang và chủ đề chỉ phục vụ quy trình, không hiển thị trên mặt slide hoặc trong ghi chú diễn giả. Các đoạn “Nội dung công khai” là dự kiến mặt trang; đoạn “Diễn giải học thuật” định hướng nội dung notes, không chứa hướng dẫn giảng viên. Bố cục và phút là thông tin nội bộ.

## Bản đồ hành trình và chu trình cụm

Cập nhật 2026-10-14 (căn chỉnh văn phong). Bảng dưới thay bảng cụm A–R ngày 28-09; bảng cũ được giữ trong lịch sử Git. Mạch 1 mở bằng trang bìa; mạch 2–7 mở bằng trang tiêu đề mạch `lec06-s0N-00`.

| Mạch, loại và chức năng | Trang tiêu đề mạch; vai trò chu trình | Tình huống, đầu vào → sản phẩm | Các bước và mã trang | Phút |
|---|---|---|---|---:|
| 1. Bài toán tìm cặp tương đồng; giới thiệu | Trang bìa `lec06-s01-01` (câu luận đề) | Kho một triệu tài liệu; chữ ký Bài 05 → bài toán tìm cặp, nhu cầu và năm dòng trả lời có điều kiện | Bìa s01-01; tiên quyết s01-06; mục tiêu s01-02; nội dung s01-07; vấn đề trung tâm s01-08; tình huống s01-03; đặc tả s01-04; kiểm tra s01-05 | 10 |
| 2. Phân dải chữ ký MinHash; thuật toán và chi phí | `lec06-s02-00`; bước `vấn đề` của cụm phân dải | Bốn tập đặc trưng, $b=2$, $r=1$, $t=2/3$ → $\mathcal C$, $P_{b,r}(s)$, $Q$, $K$ | Vấn đề s02-00, s02-01; trực giác và ví dụ s02-06; vết chạy s02-02–05; đặc tả s02-07; giả mã s02-08; tính đúng s02-09, s02-15; xác suất s02-10–12; chi phí s02-13, s02-16; kiểm tra s02-14 | 30 |
| 3. Khoảng cách và họ nhạy cảm; khái niệm và mô hình | `lec06-s03-00`; bước `vấn đề` của cụm độ đo | Hai điểm, năm độ đo của sách → họ $(d_1,d_2,p_1,p_2)$, AND, OR | Vấn đề và ví dụ s03-00, s03-01; định nghĩa s03-02; độ đo s03-03–06 (chu trình rút gọn); họ s03-07–08; phép ghép s03-09–10; vận dụng s03-11; cơ chế s03-12; kiểm tra s03-13 | 28 |
| 4. Các họ băm theo độ đo; thuật toán | `lec06-s04-00`; ngoài chu trình khái niệm | Vector bit, ba pháp tuyến, ba điểm → ba họ cơ sở và chi phí chữ ký | Thuật toán tổng quát s04-14; Hamming s04-01–02; góc s04-03, s04-05, s04-04, s04-12; Euclid s04-06, s04-07, s04-08, s04-13, s04-09; chi phí s04-10; kiểm tra s04-11 | 25,5 |
| 5. Ứng dụng tìm cặp tương đồng; thực hành vận dụng | `lec06-s05-00`; ngoài chu trình khái niệm | Hai nguồn hồ sơ, mô hình vân tay $0{,}2$/$0{,}8$, Ví dụ 3.24 → đổi biểu diễn hoặc họ hàm | Thực thể s05-01; vân tay s05-02–04; bản tin s05-05, s05-07; kiểm tra s05-06, s05-08 | 15,5 |
| 6. Tổng kết và tự kiểm tra; tổng kết | `lec06-s06-00`; ngoài chu trình khái niệm | Toàn bài → bảng kết quả, bảng thuật toán, sáu kết luận có điều kiện, câu hỏi, nguồn | s06-05, s06-02, s06-01, s06-03, s06-04, s06-08 | 11 |
| 7. Bài tập vận dụng; recitation | `lec06-s07-00`; ngoài chu trình khái niệm | Bảy bài MMDS → bảng, biểu thức, chữ ký, thùng, xác suất | s07-01–07 (Bài 3.4.1, 3.4.2, 3.6.1, 3.7.1, 3.7.2, 3.7.5(a–c), 3.8.2) | 60 |

Tổng: 70 trang giảng, 120 phút; 8 trang bài tập, 60 phút; 78 trang. Trang tiêu đề mạch của mạch 7 lấy 0,5 phút từ Bài 3.4.1 (12 → 11,5 phút). Lượt sửa deck sau năm báo cáo (2026-10-14) thêm `lec06-s04-14` (thuật toán tìm cặp với họ nhạy cảm, 1,5 phút) ngay sau trang tiêu đề mạch 4; 1,5 phút lấy từ s04-01, s04-04, s04-06 (mỗi trang 2 → 1,5 phút); mạch 4 giữ 25,5 phút với 15 trang.

## Phân bổ thời gian khi phần giảng vượt 60 trang

Phần giảng có 70 trang cho 120 phút (69 trang trước lượt sửa deck sau năm báo cáo), trung bình khoảng 1,71 phút mỗi trang. Mười tám trang tăng thêm, gồm trang `lec06-s04-14` thêm sau năm báo cáo và mười bảy trang gồm 6 trang tiêu đề mạch (2,5 phút giảng và 0,5 phút recitation), 4 trang mở đầu hoặc kết luận mới (s01-06, s01-08, s06-05, s06-08) và 7 trang tách (s01-07, s02-15, s02-16, s04-12, s04-13, s05-07, s05-08), phút của trang tách chia lại từ trang gốc. Không phần nào chuyển sang đọc thêm; không bỏ ví dụ hay chứng minh cốt lõi.

| Mạch | Trang trước → sau | Phút trước → sau | Bù trừ |
|---|---|---|---|
| 1 | 5 → 8 | 8 → 10 | +2 cho tiên quyết, nội dung, vấn đề trung tâm |
| 2 | 14 → 17 | 32 → 30 | −2: rút ví dụ dải và trang đặc tả |
| 3 | 13 → 14 | 30 → 28 | −2: bỏ hai bảng nhỏ AND, OR |
| 4 | 11 → 14 → 15 | 26 → 25,5 | −0,5; s04-14 thêm sau năm báo cáo, 1,5 phút lấy từ ba trang ví dụ của mạch |
| 5 | 6 → 9 | 16 → 15,5 | −0,5 |
| 6 | 4 → 7 | 8 → 11 | +3 cho bảng kết quả và trang nguồn |
| 7 | 7 → 8 | 60 → 60 | 0,5 phút trang tiêu đề lấy từ Bài 3.4.1 |

## Ngoại lệ mật độ và bố cục

- `lec06-s01-07` (Nội dung): 8 dòng, vì trang phải liệt kê đủ bảy mạch và dòng Đọc trước; danh sách chia hai cột trong `agenda-slide` để vừa khung, không thu nhỏ chữ.
- `lec06-s01-01` (bìa): câu luận đề 24 âm tiết, trong trần 25 của bìa, vì viết đầy đủ "Băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH)" và "thùng (bucket)" ở lần đầu.
- Trang tiêu đề mạch 3–7: dòng dẫn 21–23 âm tiết, trong trần 25 âm tiết của dòng dẫn.
- `lec06-s02-08`: giả mã 12 dòng đứng riêng, kèm một thẻ trạng thái nhỏ, đúng quy định giả mã dài hơn tám dòng.
- Trang trần 80 âm tiết: `lec06-s01-02` (mục tiêu, 76), `lec06-s06-01` (tổng kết, 78), `lec06-s06-05` (bảng kết quả, 63), `lec06-s06-02` (bảng thuật toán, 53), `lec06-s04-10` (bảng chi phí, 69), `lec06-s07-07` (đề recitation, 71). Không trang nội dung nào vượt 60 âm tiết.
- Lượt sửa deck sau năm báo cáo (2026-10-14), đếm bằng `density.py` của vai sinh viên (token có chữ hoặc chữ số, ô chỉ có số bị bỏ): trang trần 80 là `lec06-s01-02` (79), `lec06-s01-07` (56), `lec06-s02-13` (67), `lec06-s02-16` (41; 40 sau lượt sửa cuối), `lec06-s04-10` (76), `lec06-s06-05` (78), `lec06-s06-02` (74; 76 sau lượt sửa cuối), `lec06-s06-01` (73; 76 sau lượt sửa cuối), `lec06-s06-08` (65, trang nguồn, ngoại lệ mới: trang tổng kết liệt kê nguồn và móc nối Bài 07) và bảy trang đề recitation (29–77). Mọi trang trần 60 có ≤ 60 âm tiết, mọi dòng ≤ 20 âm tiết.
- Trang có bảng dữ liệu (s02-02, s02-04, s02-05, s02-14, s03-06, s04-01, s04-04, s04-06, s07-02) đếm 7 dòng vì hàng tiêu đề và mỗi hàng bảng là một dòng; bảng chi phí và bảng so sánh (s02-13, s04-10, s06-05) theo trần 8 hàng. Bảng `lec06-s06-05` có đúng 8 hàng gồm hàng tiêu đề.
- Trang đề recitation giữ một dòng ngắn "Nguồn: MMDS, Bài …, tr.…" (lớp `ex-note`) theo quyết định của điều phối viên; từ lượt sửa deck sau năm báo cáo, tên đầy đủ của sách và chữ viết tắt MMDS đã có ở trang Nội dung.

## Quy tắc thể hiện và giới hạn chung

Dùng hệ lớp của `lecture-style.css`: trang tiêu đề/mục lục như Lecture 02, `example-slide`, `ex-grid2`, `ex-card`, `ex-equation`, `ex-table`, `ex-code`, `ex-note`, `ex-source`, và `cost-slide`. Tỷ lệ các vùng dưới đây là quyết định bố cục, không là chỉ dẫn giảm cỡ chữ. Bảng là HTML, công thức là KaTeX, giả mã là `pre/code` có `data-trim`; sơ đồ và hình học dùng SVG vẽ lại. Không dùng `fragment`.

Mỗi phiếu chỉ định một trọng tâm và thứ tự đọc. Dữ kiện/giả thiết quyết định kết luận hiện trên mặt trang. Ghi chú mở rộng chứng minh, biên, lỗi và nguồn. Nếu nội dung vượt khung ở pha 2, tách trang và quay lại gate cho phạm vi thay đổi cùng hai trang lân cận; không giảm thang chữ. Những dữ kiện dùng chung viện dẫn V01–V12 trong outline; phiếu vẫn nêu giá trị cần quan sát. Không dùng màu làm dấu phân biệt duy nhất.

## Phiếu từng trang

Cập nhật 2026-10-14: phiếu được xếp theo thứ tự trang của deck sau căn chỉnh văn phong (77 trang, bảy mạch; 78 trang từ lượt sửa deck sau năm báo cáo). Mỗi phiếu cũ giữ nội dung lập kế hoạch ban đầu và thêm dòng **Căn chỉnh 2026-10-14** ghi quyết định, lý do, số âm tiết mặt trang trước → sau (đếm bằng `dens.py`, không tính tiêu đề, công thức, giả mã, ô số và ghi chú diễn giả), tiêu đề cũ nếu đổi và loại bài tập. Dòng **Ánh xạ ghi chú** đổi từ mã N sang `note-topic-id` và số hiệu của ghi chú bài giảng. Phiếu mới (6 trang tiêu đề mạch, 4 trang thêm, 7 trang tách) có đủ các trường: mạch, mục đích, thao tác của sinh viên, đối tượng trung tâm, dữ kiện kế thừa, kiến thức đầu vào, sản phẩm, bằng chứng, kết nối, nguồn, quyết định và thời lượng. Nội dung mặt trang hiện hành là tệp HTML; trường "Nội dung công khai dự kiến" của phiếu cũ là bản kế hoạch trước căn chỉnh.

### Mạch 1. Bài toán tìm cặp tương đồng

#### lec06-s01-01 — Tìm cặp tương đồng bằng LSH

- **Mục đích và vai trò:** Định vị bài trong mạch biểu diễn và tìm cặp.
- **Thông điệp:** Bài học xây cơ chế chọn cặp sau khi đã có chữ ký.
- **Nội dung công khai dự kiến:** Tên bài; tên học phần; học kỳ 1, năm học 2026–2027; “Băm nhạy cảm theo tính cục bộ (LSH)”.
- **Đầu vào và giả thiết:** Bài 05 đã cung cấp chữ ký MinHash.
- **Dữ kiện, hình thức hóa và vết chạy:** Không có ví dụ số; tên và số bài theo source.md.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Tiêu đề lớn ở giữa trên; học phần và học kỳ phía dưới theo title-slide. Một cụm tên giúp sinh viên năm 2 nhận nhiệm vụ mới; không thêm công thức hay mục tiêu dài.
- **Kết nối vào–ra:** Nhận kết quả Bài 05; trang nội dung xác định những thành phần của quy trình cần xây.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chữ ký là đầu vào của bước chọn cặp. Việc biểu diễn từng tài liệu đã được giải quyết ở Bài 05; bài này xét việc tổ chức phép so giữa nhiều tài liệu.
- **Nguồn:** sources/source.md, bảng Thứ tự đề xuất, dòng 6; B §3.4 tr.91–92/PDF 20–21.
- **Ánh xạ ghi chú:** `lec-06-topic-01` (mã cũ `N01`); số hiệu: mở chương. **Thời lượng:** 0,5 phút (trước 0.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: câu luận đề lên bìa và viết đầy đủ LSH; nguồn chuyển vào ghi chú diễn giả. Âm tiết mặt trang 32 → 49.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: viết đầy đủ "locality-sensitive hashing" và "(bucket)" trong câu luận đề (24 âm tiết, trần 25 của bìa); ghi chú bỏ mẫu dấu hai chấm báo kịch tính. Âm tiết mặt trang 51 → 51.

#### lec06-s01-06 — Tiên quyết và quy ước

- **Mạch và mục đích:** Mạch 1, giới thiệu. Nêu lại ba kết quả Bài 05 và quy ước ký hiệu trước khi dùng.
- **Thao tác của sinh viên:** Đọc ba dòng Nhắc lại và hai dòng Ký hiệu; đối chiếu $s$ với $\widehat s$.
- **Đối tượng trung tâm:** Định lý MinHash $\Pr[h_\pi(A)=h_\pi(B)]=\mathrm{SIM}(A,B)$ và ma trận $\mathrm{SIG}\in V^{n\times C}$.
- **Dữ kiện và ký hiệu kế thừa:** Jaccard, MinHash, chữ ký từ ghi chú Bài 05, Mục 2, 6, 7.
- **Kiến thức đầu vào:** Xác suất cơ bản, tập hợp.
- **Sản phẩm học tập:** Danh sách ký hiệu dùng trong bài.
- **Bằng chứng kiểm tra:** Câu 3–4 của trang câu hỏi s01-05 (phân biệt $s$ với $\widehat s$).
- **Kết nối vào–ra:** Vào: bìa. Ra: mục tiêu học tập và nội dung dùng các ký hiệu này.
- **Nguồn:** Ghi chú Bài 05; MMDS §3.3.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: mạch mở đầu bắt buộc có trang Nhắc lại/Ký hiệu. Âm tiết mặt trang — → 58.
- **Ánh xạ ghi chú:** `lec-06-topic-18`; số hiệu: Kiến thức tiên quyết; Nhận xét 06.2. **Thời lượng:** 1,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (sinh viên): bỏ $V$ chưa định nghĩa, viết "$\mathrm{SIG}$ cỡ $n\times C$". Âm tiết mặt trang 58 → 59.

#### lec06-s01-02 — Mục tiêu học tập

- **Mục đích và vai trò:** Nhận diện thứ tự bảy phần và ba năng lực quan sát được của bài học.
- **Thông điệp:** Tạo và xác minh tập ứng viên, tính xác suất để chọn tham số, và chọn họ băm theo độ đo là ba đầu ra học tập.
- **Nội dung công khai dự kiến:** Bài toán tìm cặp tương đồng Phân dải chữ ký MinHash Khoảng cách và họ nhạy cảm Các họ băm theo độ đo Ứng dụng tìm cặp tương đồng Tổng kết và tự kiểm tra Bài tập vận dụng Mục tiêu học tập Tạo và xác minh tập cặp ứng viên bằng phân dải chữ ký. Tính xác suất một cặp thành ứng viên; chọn số dải, số hàng và cách ghép AND/OR. Chọn họ băm theo độ đo và áp dụng cho thực thể, vân tay, bản tin.
- **Đầu vào và giả thiết:** Tên bài và chữ ký.
- **Dữ kiện, hình thức hóa và vết chạy:** Không áp dụng ví dụ số.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai vùng: danh mục bảy phần 60% bên trái; ba mục tiêu 40% bên phải. Tiêu đề và mục lục giữ cỡ chữ agenda-slide; mục tiêu dùng cỡ chữ nội dung của example-slide. CSS chỉ chia lưới, không đổi font. Đọc mục tiêu rồi liên hệ từng phần; ba mục tiêu gộp MT1–MT6, được kiểm ở phần kết.
- **Kết nối vào–ra:** Chữ ký Bài 05 → ba sản phẩm học tập; số cặp của kho triệu tài liệu tạo nhu cầu đầu tiên. Kết bài s06-03/04 kiểm lại ba năng lực.
- **Diễn giải học thuật, lời giải và tiêu chí:** Phần 1 đặt bài toán: sau khi có chữ ký, số cặp vẫn tăng bậc hai. Phần 2 chia chữ ký thành dải để sinh cặp ứng viên, xác minh chúng, rồi tính xác suất và chi phí. Phần 3 và 4 mở rộng cách làm từ Jaccard sang các độ đo khác qua khái niệm họ băm nhạy cảm. Phần 5 áp dụng vào ba bài toán của sách. Ba mục tiêu được kiểm ở các trang câu hỏi cuối mỗi phần và ở phần tổng kết; mục tiêu 2 bao gồm phép ghép AND/OR của phần 3, mục tiêu 3 bao gồm ba ứng dụng của phần 5.
- **Nguồn:** B § §3.4–3.8 tr.91–122; outline mục 5.
- **Ánh xạ ghi chú:** `lec-06-topic-01` (mã cũ `N01`); số hiệu: Mục tiêu học tập. **Thời lượng:** 1 phút (trước 1 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: trang gộp mục lục và mục tiêu 89 âm tiết vượt trần 80; tách thành Mục tiêu và Nội dung. Âm tiết mặt trang 89 → 76. Tiêu đề cũ: “Nội dung và mục tiêu”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B2, B6, B11: mục tiêu viết bằng lời thay $P_{b,r}(s)$ và $(d_1,d_2,p_1,p_2)$; "dải (band)"; ghi chú nêu thao tác mỗi mục tiêu đòi, bỏ bảng ánh xạ điều phối. Âm tiết mặt trang 76 → 79.

#### lec06-s01-07 — Nội dung

- **Mạch và mục đích:** Mạch 1, giới thiệu. Liệt kê bảy mạch với số và tên trùng trang tiêu đề mạch; dòng Đọc trước.
- **Thao tác của sinh viên:** Đọc thứ tự mạch; mở giáo trình đúng mục.
- **Đối tượng trung tâm:** Danh sách bảy mạch.
- **Dữ kiện và ký hiệu kế thừa:** Mục tiêu học tập ở trang trước.
- **Kiến thức đầu vào:** Không.
- **Sản phẩm học tập:** Lộ trình bài học.
- **Bằng chứng kiểm tra:** Số mạch trên trang khớp `#/N` (kiểm bằng trình duyệt).
- **Kết nối vào–ra:** Vào: mục tiêu. Ra: vấn đề trung tâm trả lời theo cùng số mạch.
- **Nguồn:** MMDS §§3.4–3.8, tr.91–122.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: phần mục lục tách từ trang gộp; ol 1–7 khớp tên trang tiêu đề mạch, thêm Đọc trước. Âm tiết mặt trang — → 45.
- **Ánh xạ ghi chú:** `lec-06-topic-01`; số hiệu: —. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: viết đầy đủ tác giả, tên sách và "MMDS, ấn bản 3"; ghi chú bỏ nhãn "Mạch N", nêu mạch 4 và 5 là hai nhánh song song. Âm tiết mặt trang 47 → 56.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): ghi chú nêu đúng phạm vi song song, phần ứng dụng dùng lại thuật toán tổng quát. Âm tiết mặt trang 56 → 56.

#### lec06-s01-08 — Vấn đề trung tâm

- **Mạch và mục đích:** Mạch 1, giới thiệu. Nêu bài toán dữ liệu lớn trong một dòng và câu trả lời có điều kiện của mạch 2–6.
- **Thao tác của sinh viên:** Đọc nhu cầu; đối chiếu năm dòng với sáu dòng trả lời của s06-01 (bốn dòng đầu tương ứng dòng 1–4, dòng cuối và nhu cầu tương ứng dòng 5–6); mạch 7 là bài tập nên không có dòng riêng.
- **Đối tượng trung tâm:** Kho $10^6$ tài liệu, khoảng $5\cdot10^{11}$ cặp.
- **Dữ kiện và ký hiệu kế thừa:** Ví dụ 3.10 (số tài liệu, số cặp).
- **Kiến thức đầu vào:** Tổ hợp chập hai.
- **Sản phẩm học tập:** Năm dòng trả lời có điều kiện, thu hồi bằng sáu dòng có số ở s06-01.
- **Bằng chứng kiểm tra:** Trang s06-01 trả lời theo cùng thứ tự các dòng.
- **Kết nối vào–ra:** Vào: nội dung. Ra: ví dụ kho một triệu tài liệu cho số liệu chi tiết.
- **Nguồn:** MMDS Ví dụ 3.10, tr.92.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: mạch mở đầu bắt buộc có trang vấn đề trung tâm; mỗi dòng 2–6 là câu trả lời có điều kiện của mạch cùng số. Âm tiết mặt trang — → 59.
- **Ánh xạ ghi chú:** `lec-06-topic-01`; số hiệu: Hệ quả 06.8 (dòng 2). **Thời lượng:** 1,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A1, B1: năm dòng viết bằng lời, không ký hiệu chưa định nghĩa; dòng AND/OR nêu đúng cơ chế AND rồi OR với hàm độc lập; dòng cuối là giới hạn chung; bỏ số $5\cdot10^{11}$ trước khi được tính; danh sách không đánh số theo mạch; ghi chú bỏ câu chỉ đường. Âm tiết mặt trang 59 → 59.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ (rà lại mạch): dòng cuối thành kết luận có điều kiện "Chưa giả thiết phân bố tương đồng: xấu nhất xét mọi cặp"; rút dòng 1–2 để giữ trần 60. Âm tiết mặt trang 59 → 60.

#### lec06-s01-03 — Ví dụ: kho một triệu tài liệu

- **Mục đích và vai trò:** Tính riêng dung lượng chữ ký và số phép so cặp.
- **Thông điệp:** Dung lượng chữ ký tuyến tính không làm số cặp mất bậc hai.
- **Nội dung công khai dự kiến:** $C=10^6$ tài liệu, chữ ký $n=250$ thành phần, 4 byte/thành phần. Dung lượng chữ ký $10^6\cdot250\cdot4=10^9$ byte Số cặp cần so $\binom{10^6}{2}=499\,999\,500\,000$ Giả sử mỗi cặp mất $1\,\mu s$: tổng thời gian khoảng $5{,}79$ ngày. Chữ ký giảm chi phí mỗi cặp; số cặp vẫn tăng bậc hai.
- **Đầu vào và giả thiết:** Tổ hợp chập 2; byte và đơn vị thời gian.
- **Dữ kiện, hình thức hóa và vết chạy:** V01; $10^6\cdot250\cdot4$; $499999500000\cdot10^{-6}/86400=5{,}78703125$. Giả định thời gian, không phép đo.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 45% là phép tính dung lượng; phải 55% là số cặp và thời gian. Đọc cùng $C$ trên hai nhánh. Năm 2 cần tách hai đại lượng có đơn vị khác; diễn giải thời gian chi tiết vào notes.
- **Kết nối vào–ra:** Bản đồ mục 1→giới hạn số cặp; giới hạn dẫn tới đặc tả chỉ tìm cặp đạt ngưỡng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Ví dụ 3.10 là phép tính minh họa của sách. Nếu bài toán yêu cầu xuất độ tương đồng của mọi cặp thì kích thước đầu ra đã là bậc hai. Nhu cầu ở đây chỉ gồm những cặp đủ tương đồng.
- **Nguồn:** B Ex 3.10 tr.92/PDF 21; M PDF 24; S3 PDF 10–14.
- **Ánh xạ ghi chú:** `lec-06-topic-01` (mã cũ `N01`); số hiệu: Ví dụ 06.1. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: đổi sang khuôn trang ví dụ (dữ kiện, yêu cầu, bước, Kết luận); bỏ dòng nguồn. Âm tiết mặt trang 46 → 51. Tiêu đề cũ: “Chi phí so sánh mọi cặp chữ ký”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ: thêm bước $499\,999{,}5$ giây; kết luận nêu chữ ký $10^9$ byte; ghi chú bỏ "bản soạn", mở bằng việc tính số của vấn đề trung tâm. Âm tiết mặt trang 52 → 52.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ (rà lại toán): đơn vị $1\,\mu\mathrm{s}$. Âm tiết mặt trang 52 → 52.

#### lec06-s01-04 — Bài toán tìm cặp tương đồng

- **Mục đích và vai trò:** Nêu dữ liệu đã có và tiêu chuẩn chấp nhận cặp.
- **Thông điệp:** Bài toán nhận các tập, chữ ký và ngưỡng, trả mọi cặp đạt ngưỡng; cách làm là chỉ xác minh cặp ứng viên, chấp nhận khả năng bỏ sót.
- **Nội dung công khai dự kiến:** Đầu vào: các tập $S_1,\ldots,S_C$ hữu hạn, không rỗng; ma trận chữ ký $\mathrm{SIG}$ cỡ $n\times C$; ngưỡng $t\in[0,1]$. Đầu ra: mọi cặp $c<d$ có $\mathrm{SIM}(S_c,S_d)\ge t$. [Hình: Chữ ký tạo khóa dải, sinh cặp ứng viên duy nhất rồi xác minh trên tập gốc.] Chỉ xác minh các cặp ứng viên; đổi lại, cặp đạt ngưỡng có thể bị bỏ sót.
- **Đầu vào và giả thiết:** Jaccard, MinHash Bài 05; cùng phép thử theo hàng.
- **Dữ kiện, hình thức hóa và vết chạy:** Ký hiệu $C,n,\mathrm{SIG},s,\widehat s$ giữ Bài 05. Chưa dùng $b,r$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai dòng “Đầu vào”, “Đầu ra” ở trên; sơ đồ quy trình rộng ở giữa; câu chốt về cách làm và khả năng bỏ sót ở cuối. Ký hiệu phụ ($V$, $s$, $\widehat s$, tính chất MinHash) nằm trong ghi chú để mặt trang chỉ còn bài toán.
- **Kết nối vào–ra:** Số cặp quá lớn→cặp cần tìm; kiểm tra mở đầu xác nhận phần chi phí còn thiếu.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đặt $s=\mathrm{SIM}(S_c,S_d)$, tính trên hai tập gốc; $\widehat s$ là tỷ lệ thành phần trùng của hai cột chữ ký, phụ thuộc các phép thử đã lấy. $V$ là miền giá trị của một thành phần chữ ký. Bài 05 cho $\Pr[h(S_c)=h(S_d)]=s$ với MinHash lý tưởng: cặp càng tương đồng thì càng dễ trùng thành phần chữ ký, và đó là cơ sở để chọn ứng viên. Xác minh Jaccard cho một cặp là quyết định xác định; việc cặp ấy có được đưa vào tập ứng viên hay không phụ thuộc các phép thử. Hình là sơ đồ của cả quy trình; cách tạo khóa dải từ chữ ký được xây dựng ở phần 2.
- **Nguồn:** B §3.4 tr.91–92, §3.4.3 tr.95–96; P5, commit 5530bd6, đoạn ký hiệu.
- **Ánh xạ ghi chú:** `lec-06-topic-01` (mã cũ `N01`); số hiệu: Định nghĩa 06.1. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: nhãn Đầu vào/Đầu ra in đậm; câu luận đề đã lên bìa nên câu cuối đổi thành Lưu ý. Âm tiết mặt trang 40 → 28.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: "cặp bỏ sót (false negative)" trong dòng Lưu ý. Âm tiết mặt trang 28 → 35.

#### lec06-s01-05 — Câu hỏi về bài toán tìm cặp

- **Mục đích và vai trò:** Phân biệt giảm kích thước từng đối tượng với giảm số cặp.
- **Thông điệp:** Số cặp tăng bậc hai theo số tài liệu; tập ứng viên giảm số phép xác minh; quyết định cuối dựa trên Jaccard gốc, không dựa trên tỷ lệ trùng chữ ký.
- **Nội dung công khai dự kiến:** Câu hỏi: Với $C=10^5$ tài liệu và $1\,\mu s$ mỗi cặp, tính số cặp và tổng thời gian. So với $C=10^6$, số cặp giảm bao nhiêu lần? Trong kho $10^6$ tài liệu, bộ tạo ứng viên trả $10^6$ cặp. Số phép xác minh giảm bao nhiêu lần so với xét mọi cặp? Cặp $S_1,S_4$ của Bài 05 có $\widehat s=1$ trên hai thành phần chữ ký và $s=2/3$. Đại lượng nào quyết định cặp có đạt ngưỡng $t$?
- **Đầu vào và giả thiết:** V01 và hợp đồng s01-04.
- **Dữ kiện, hình thức hóa và vết chạy:** Câu 1 dùng dữ kiện luyện tập $C=10^5$; câu 2 dùng cặp $S_1,S_4$ được nhắc lại trên mặt trang; đáp án $4\,999\,950\,000$ cặp, gần 1,4 giờ, giảm khoảng 100 lần; $\widehat s=1$, $s=2/3$, quyết định theo $s$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Nhãn “Câu hỏi:” và ba câu đánh số toàn chiều rộng; dòng nguồn ghi dữ kiện luyện tập. Không câu nào có đáp án trên mặt s01-03, s01-04.
- **Kết nối vào–ra:** Hợp đồng→tự kiểm; nhu cầu tập ứng viên dẫn vào phân dải.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: $\binom{10^5}{2}=4\,999\,950\,000$ cặp, khoảng $5\,000$ giây, tức gần 1,4 giờ; giảm số tài liệu 10 lần làm số cặp giảm khoảng 100 lần vì số cặp tăng bậc hai. Câu 2: hai hàng chữ ký trùng nên $\widehat s=1$, còn $s=|\{a,d\}|/|\{a,c,d\}|=2/3$; quyết định dựa trên $s$, tính ở bước xác minh. Tiêu chí: thấy tăng bậc hai, phân biệt tương đồng thật với ước lượng. Câu về $10^6$ cặp ứng viên không còn trên trang này.
- **Nguồn:** B Ex 3.10/ §3.4 tr.91–92; câu kiểm tra trực tiếp dữ kiện nguồn.
- **Ánh xạ ghi chú:** `lec-06-topic-01` (mã cũ `N01`); số hiệu: Bài tập 06.1; Nhận xét 06.2. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tách câu dài; câu 2 cũ (bộ tạo trả $10^6$ cặp) chuyển sang trang trả lời vấn đề trung tâm làm con số thu hồi. Âm tiết mặt trang 80 → 42. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: trung bình (sư phạm), nhẹ (sinh viên): thêm "Nhắc lại:" bốn tập và chữ ký trước khi dùng; gộp thành hai câu hỏi có nhiệm vụ. Âm tiết mặt trang 42 → 43.

### Mạch 2. Phân dải chữ ký MinHash

#### lec06-s02-00 — 2. Phân dải chữ ký MinHash

- **Mạch và vị trí:** điểm vào mạch 2; trang tiêu đề mạch `section.strand-title`, `id="mach-2"`, mở tại `#/2`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 2 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Ma trận chữ ký, định lý MinHash, ngưỡng $t$; kho một triệu tài liệu.
- **Sản phẩm giao cho mạch sau:** tập ứng viên $\mathcal C$, $P_{b,r}(s)$, $Q$, $K$.
- **Vai trò chu trình:** bước `vấn đề` của cụm phân dải: dòng dẫn nêu đúng nhu cầu gom cột giống nhau vào cùng thùng.
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/2` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 32 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-02`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: ghi chú bỏ "Mạch này", "giao cho mạch sau". Âm tiết mặt trang 32 → 32.

#### lec06-s02-01 — Dải, khóa dải và cặp ứng viên

- **Mục đích và vai trò:** Mô tả quy tắc đưa hai cột vào cùng nhóm.
- **Thông điệp:** Chia chữ ký thành dải; cặp trùng toàn bộ ít nhất một dải là ứng viên, và cột càng tương đồng càng dễ thành ứng viên.
- **Nội dung công khai dự kiến:** [Hình: Chữ ký được chia thành b dải, mỗi dải r hàng; mỗi dải tạo khóa riêng.] Chia $n=br$ hàng thành $b$ dải. Phần của một cột trong dải là bộ $r$ giá trị có thứ tự (tuple); hai cột trùng dải khi hai tuple bằng nhau. Chung ít nhất một dải → cặp ứng viên. Hai cột càng tương đồng càng dễ trùng ở ít nhất một dải. Cặp dưới ngưỡng vẫn thành ứng viên gọi là ứng viên giả. Mỗi dải dùng một bảng thùng riêng; cùng bộ giá trị ở hai dải khác nhau không vào cùng thùng.
- **Đầu vào và giả thiết:** SIG và nhu cầu ứng viên.
- **Dữ kiện, hình thức hóa và vết chạy:** HT1 trực giác; chưa áp công thức xác suất.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** SVG chữ ký với ngoặc dải ở trái 60%, hai câu quy tắc ở phải 40%. Năm 2 thấy AND trong dải và OR giữa dải bằng quan hệ nhóm; ký hiệu đặt cạnh ngoặc.
- **Kết nối vào–ra:** Ứng viên cần được tạo→nhóm các đoạn bằng nhau; SIG nhỏ cho phép chạy từng bước.
- **Diễn giải học thuật, lời giải và tiêu chí:** Theo §3.4.1, cách tiếp cận chung là băm mỗi đối tượng nhiều lần sao cho đối tượng tương đồng dễ vào cùng thùng hơn; cặp vào cùng thùng ở ít nhất một lần băm là cặp ứng viên. Với chữ ký MinHash, mỗi dải là một lần băm: phần $r$ giá trị của một cột trong dải tạo thành một bộ có thứ tự (tuple). Cột càng giống nhau thì từng thành phần càng dễ trùng, nên càng dễ trùng toàn bộ một dải. Cặp không tương đồng mà vẫn thành ứng viên là ứng viên giả; cặp tương đồng không thành ứng viên là cặp bị bỏ sót. So hai tuple rẻ hơn nhiều so với đọc hai tập gốc.
- **Nguồn:** B §3.4.1 tr.92–93/PDF 21–22; M PDF 44–46.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Định nghĩa 06.3. **Thời lượng:** 1 phút (trước 1 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu; bỏ chuỗi mũi tên; tách ex-note sang ghi chú; định nghĩa cặp ứng viên bằng "gọi là". Âm tiết mặt trang 84 → 59. Tiêu đề cũ: “Ý tưởng phân dải chữ ký”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12, B11: thêm dòng ví dụ dẫn nhập (cột 2 và 4 cùng $(0,2,1)$), đổi "Ý nghĩa" thành "Trực quan." đặt trước định nghĩa; "cặp ứng viên (candidate pair)". Âm tiết mặt trang 59 → 59.

#### lec06-s02-06 — Ví dụ: năm cột, dải ba hàng

- **Mục đích và vai trò:** Phân biệt trùng một thành phần với trùng tuple nhiều hàng.
- **Thông điệp:** Trùng dải đòi trùng cả r thành phần; trùng một hàng chưa đủ. Cột cùng thùng khi và chỉ khi tuple bằng nhau.
- **Nội dung công khai dự kiến:** Chữ ký có $n=12$ hàng, chia $b=4$ dải, mỗi dải $r=3$ hàng. Dải đầu Cột 1 Cột 2 Cột 3 Cột 4 Cột 5 Hàng 1 1 0 0 0 2 Hàng 2 3 2 1 2 2 Hàng 3 0 1 3 1 1 Tuple ở dải đầu: cột 2 và cột 4 cùng là $(0,2,1)$; cột 3 là $(0,1,3)$. Cột 2 và 4 thành ứng viên; cột 2 và 3 chỉ trùng một hàng nên chưa trùng dải. Chỉ dải đầu được cho trong Hình 3.7; chín hàng còn lại chưa có dữ kiện.
- **Đầu vào và giả thiết:** V02 đã có $r=1$; nay thay dữ kiện sang V03.
- **Dữ kiện, hình thức hóa và vết chạy:** V03; cặp 2,3 trùng hàng đầu nhưng khác tuple; cặp 2,4 là ứng viên bất kể dải còn lại.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ma trận 3 × 5 chiếm 60% trên; hai tuple so sánh ở dưới. Phần 9 hàng thiếu chỉ ghi “các dải khác chưa có dữ kiện”. Năm 2 thấy điều kiện AND thất bại tại hàng 2; không dựng tổng ứng viên từ dữ liệu thiếu.
- **Kết nối vào–ra:** Nhận định nghĩa dải từ s02-01; vết chạy s02-02–05 áp dụng phân dải trên chữ ký của Bài 05.
- **Diễn giải học thuật, lời giải và tiêu chí:** Ví dụ 3.11: cột 2 và 4 có cùng tuple $(0,2,1)$ ở dải đầu nên chắc chắn vào cùng thùng của dải này và thành cặp ứng viên, bất kể ba dải còn lại. Sách giả định có rất nhiều thùng, nên hai tuple khác nhau như $(1,3,0)$ và $(0,2,1)$ gần như không va chạm; từ đây xem hai cột cùng thùng khi và chỉ khi tuple bằng nhau. Cột 2 và 3 chỉ trùng hàng đầu nên chưa trùng dải đầu, nhưng vẫn có thể thành ứng viên nếu trùng một trong ba dải chưa được cho.
- **Nguồn:** B Ex 3.11/Hình 3.7 tr.92–93/PDF 21–22; M 45–46.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Ví dụ 06.2. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: khuôn trang ví dụ; còn một câu Kết luận; ex-note chuyển sang ghi chú. Âm tiết mặt trang 67 → 43. Tiêu đề cũ: “Ví dụ trùng dải với ba hàng”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (sư phạm): một câu kết luận, dùng cặp 2–5 trùng hai hàng làm phản ví dụ. Âm tiết mặt trang 55 → 48.

#### lec06-s02-02 — Ví dụ: bốn tập đặc trưng

- **Mục đích và vai trò:** Đọc đúng hàng, cột và tham số của vết chạy.
- **Thông điệp:** Cùng dữ kiện tập gốc và chữ ký cho phép kiểm kết quả sau phân dải.
- **Nội dung công khai dự kiến:** $S_1=\{a,d\},\quad S_2=\{c\}$ $S_3=\{b,d,e\},\quad S_4=\{a,c,d\}$ Dữ kiện Ví dụ 3.8, MMDS; giữ chữ ký từ Bài 05. Hàng $S_1$ $S_2$ $S_3$ $S_4$ 1 1 3 0 1 2 0 2 0 0 $b=2,\quad r=1,\quad t=2/3$ Với $r=1$, mỗi hàng là một dải. Khóa của cột $c$ ở dải $j$ là cặp $(j,\text{tuple})$.
- **Đầu vào và giả thiết:** Ký hiệu từ s01-04 và quy tắc dải.
- **Dữ kiện, hình thức hóa và vết chạy:** V02; các số 1,3,0,1 là giá trị chữ ký, cột 1–4 là mã tài liệu. Phân dải là phép áp dụng mới đã duyệt.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng tập gốc ở trái 45%; ma trận có nhãn cột/hàng/dải ở phải 55%. Giữ vị trí ma trận ở hai trang sau. Năm 2 đọc đồng thời đối tượng và biểu diễn; không lặp cách tính MinHash.
- **Kết nối vào–ra:** Quy tắc nhóm→đầu vào cụ thể; dải 1 là bước cập nhật đầu tiên.
- **Diễn giải học thuật, lời giải và tiêu chí:** Các chữ ký thuộc Ví dụ 3.8 của sách. Hai hàm cố định chỉ dùng chạy thuật toán; định lý xác suất ở phần sau xét mô hình hoán vị đều độc lập. Với một hàng mỗi dải, tuple có một thành phần.
- **Nguồn:** B Ex 3.8 tr.85–86/PDF 14–15; áp dụng §3.4.1 tr.92–93; P5, commit 5530bd6.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Ví dụ 06.3. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: ví dụ xuyên suốt gọi bằng tên; thêm yêu cầu; nguồn sang ghi chú. Âm tiết mặt trang 32 → 22. Tiêu đề cũ: “Phân dải chữ ký của bốn tập”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (mạch): ghi chú nêu lý do $r=1$ và nơi kiểm điều kiện cả tuple. Âm tiết mặt trang 22 → 22.

#### lec06-s02-03 — Ví dụ: bốn tập đặc trưng, thùng của dải 1

- **Mục đích và vai trò:** Chèn bốn mã tài liệu theo khóa dải đầu.
- **Thông điệp:** Khóa đầy đủ giữ đúng nhóm trong một dải.
- **Nội dung công khai dự kiến:** Tài liệu Giá trị dải 1 1 1 2 3 3 0 4 1 Khóa (dải, tuple) Danh sách mã $(1,(1))$ 1, 4 $(1,(3))$ 2 $(1,(0))$ 3 Cặp phát ở dải 1: $(1,4)$. Lần chèn tài liệu 4 tạo thùng có hai phần tử; thùng đơn không phát cặp.
- **Đầu vào và giả thiết:** V02, tuple một thành phần.
- **Dữ kiện, hình thức hóa và vết chạy:** Bốn lượt chèn ở dải 1: tài liệu 1 và 4 cùng khóa $(1,(1))$; tài liệu 2, 3 ở thùng đơn; cặp phát $(1,4)$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng giá trị dải 1 bên trái; bảng khóa (dải, tuple) và danh sách mã bên phải; dòng cặp phát và câu chốt ở dưới.
- **Kết nối vào–ra:** Đầu vào→nhóm dải 1; dải 2 dùng cùng phép chèn nhưng không chung miền khóa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Sau bốn lượt chèn, mỗi tài liệu xuất hiện đúng một lần trong thùng của nó ở dải 1. Chỉ một thùng có hai phần tử nên chỉ phát cặp (1,4). Mã dải là một thành phần của khóa, khác giá trị chữ ký 1.
- **Nguồn:** B §3.4.1 tr.92–93 trên dữ kiện Ex 3.8; V02.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Ví dụ 06.3. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: gộp hai bảng thành một bảng bốn hàng để không quá sáu dòng. Âm tiết mặt trang 38 → 29. Tiêu đề cũ: “Thùng của dải 1”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B18: bảng cùng khuôn "Khóa dải | Tài liệu | Cặp phát" với s02-04. Âm tiết mặt trang 33 → 37.

#### lec06-s02-04 — Ví dụ: bốn tập đặc trưng, hợp qua hai dải

- **Mục đích và vai trò:** Phát cặp dải 2 và khử lặp qua các dải.
- **Thông điệp:** Tổng lượt phát cặp có thể lớn hơn số ứng viên duy nhất.
- **Nội dung công khai dự kiến:** Khóa dải 2 Mã Cặp phát $(2,(0))$ 1, 3, 4 (1,3), (1,4), (3,4) $(2,(2))$ 2 ∅ Dải 1 đã phát $(1,4)$. Số lượt phát trước khử lặp: $Q=1+3=4$. Tập ứng viên sau khử lặp: $\mathcal C=\{(1,3),(1,4),(3,4)\}$ Số cặp phân biệt: $K=|\mathcal C|=3$. Cặp (1,4) phát hai lần nhưng chỉ được xác minh một lần.
- **Đầu vào và giả thiết:** Thùng dải 1; mọi cặp không thứ tự trong danh sách.
- **Dữ kiện, hình thức hóa và vết chạy:** V02;$\binom32=3$; cặp 14 được phát ở cả hai dải.8 lượt chèn cho toàn vết chạy.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ma trận trái 45% giữ nguyên; bảng dải 2 và dòng hợp cặp phải 55%. Cặp 14 lặp có nhãn “đã có”. Năm 2 phân biệt lượt xử lý và phần tử của tập; không chỉ dùng màu.
- **Kết nối vào–ra:** Nhóm dải 1→nhiều dải; tập đã khử lặp là đầu vào xác minh.
- **Diễn giải học thuật, lời giải và tiêu chí:** $Q$ đếm lượt trước khử lặp; $K$ đếm cặp phân biệt. Một cặp được sinh nhiều lần vẫn chỉ xác minh một lần khi lưu trong tập. Khóa có số dải nên giá trị 0 ở dải 1 không tự ghép với 0 ở dải 2.
- **Nguồn:** B §3.4.1, 3.4.3 tr.92–96; áp dụng V02.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Ví dụ 06.3. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bỏ lưới hai cột; định nghĩa $Q$, $K$ bằng "là". Âm tiết mặt trang 39 → 34. Tiêu đề cũ: “Hợp các cặp qua hai dải”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B18: cột "Mã" đổi thành "Tài liệu". Âm tiết mặt trang 36 → 37.

#### lec06-s02-05 — Ví dụ: bốn tập đặc trưng, xác minh

- **Mục đích và vai trò:** Tính Jaccard cho ba ứng viên và chọn kết quả.
- **Thông điệp:** Xác minh loại cặp dưới ngưỡng trong tập ứng viên.
- **Nội dung công khai dự kiến:** Giữ cặp có Jaccard gốc ít nhất $t=2/3$. Cặp Giao Hợp Jaccard Kết quả (1,3) {d} {a,b,d,e} $1/4$ Loại (1,4) {a,d} {a,c,d} $2/3$ Giữ (3,4) {d} {a,b,c,d,e} $1/5$ Loại Kết quả là $\{(1,4)\}$; hai cặp $(1,3)$ và $(3,4)$ là ứng viên giả. Xác minh chỉ loại ứng viên giả; nó không khôi phục cặp đạt ngưỡng chưa được sinh.
- **Đầu vào và giả thiết:** Tập V02 và $\mathcal C$ ở trang trước.
- **Dữ kiện, hình thức hóa và vết chạy:** V02 giữ $t$; $\widehat s_{14}=1$ nhưng $s_{14}=2/3$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 3 hàng cặp/giao-hợp/Jaccard/kết quả ở giữa, ngưỡng trên bảng. Năm 2 tính lại tử và mẫu trước quyết định; notes giữ danh sách hợp đầy đủ.
- **Kết nối vào–ra:** Nhận $\mathcal C$ từ s02-04; trang đặc tả s02-07 hình thức hóa ứng viên và đầu ra đã chạy tay.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hợp của $S_1$ và $S_3$ là $\{a,b,d,e\}$; hợp của $S_1$ và $S_4$ là $\{a,c,d\}$; hợp của $S_3$ và $S_4$ là $\{a,b,c,d,e\}$. Cặp $(1,3)$ và $(3,4)$ là ứng viên giả ở tầng tạo cặp. Xác minh không thể khôi phục một cặp đạt ngưỡng đã bị bỏ sót bởi phân dải.
- **Nguồn:** B §3.4.3 tr.95–96; Ex 3.8; dữ kiện; V02.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Ví dụ 06.3. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: định nghĩa ứng viên giả trên trang; ex-note "không khôi phục cặp chưa sinh" chuyển sang s02-15. Âm tiết mặt trang 53 → 38. Tiêu đề cũ: “Xác minh bằng Jaccard gốc”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: "ứng viên giả (false positive)". Âm tiết mặt trang 38 → 40.

#### lec06-s02-07 — Thuật toán: phân dải và xác minh

- **Mục đích và vai trò:** Viết điều kiện trước và sau của phân dải.
- **Thông điệp:** Đầu ra là các cặp ứng viên — cùng khóa ở ít nhất một dải — có Jaccard gốc đạt ngưỡng.
- **Nội dung công khai dự kiến:** Đầu vào: $\mathrm{SIG}\in V^{n\times C}$; $b,r$ nguyên dương, $n=br$; các tập $S_1,\ldots,S_C$; ngưỡng $t\in[0,1]$. Khóa dải $k_{j,c}=\bigl(j,\mathrm{SIG}_{(j-1)r+1:jr,c}\bigr)$ Tập ứng viên: $\mathcal C=\{(c,d):c<d,\ \exists j:\ k_{j,c}=k_{j,d}\}$. Đầu ra: $\{(c,d)\in\mathcal C:\ \mathrm{SIM}(S_c,S_d)\ge t\}$.
- **Đầu vào và giả thiết:** Ví dụ tuple và cùng dải.
- **Dữ kiện, hình thức hóa và vết chạy:** HT1; $j=1,\ldots,b$;$c=1,\ldots,C$; V02 khóa $(2,(0))$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba dòng vào/khóa/ra toàn chiều ngang; khóa ở khung giữa. Năm 2 ánh xạ (j, tuple) của vết chạy sang ký hiệu lát ma trận; diễn giải chỉ số ở notes, không thêm chứng minh trên cùng trang.
- **Kết nối vào–ra:** Tuple đã thấy→hợp đồng; giả mã thực hiện đúng hợp đồng này.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hàm băm bảng chỉ định nơi tra cứu; phép bằng vẫn so cả số dải và tuple. Điều kiện tồn tại một dải giải thích phép hợp ứng viên. Đầu ra dùng thứ tự $c<d$ để hai cách gọi một cặp có cùng biểu diễn. Các tập $S_c$ hữu hạn, không rỗng để Jaccard xác định. Đặc tả chưa nói mọi cặp đạt ngưỡng đều nằm trong $\mathcal C$; khả năng bỏ sót được phân tích ở các trang xác suất.
- **Nguồn:** B §3.4.1, 3.4.3 tr.92–96; diễn đạt đặc tả đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Định nghĩa 06.3; Thuật toán 06.4. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Thuật toán:, nhãn Đầu vào/Đầu ra in đậm. Âm tiết mặt trang 18 → 15. Tiêu đề cũ: “Đặc tả phân dải và xác minh”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (toán, sinh viên): Đầu vào ghi tập "hữu hạn, không rỗng"; bỏ $V$; ghi chú giải thích ký hiệu cắt lát. Âm tiết mặt trang 13 → 18.

#### lec06-s02-08 — Thuật toán: phân dải và xác minh

- **Mục đích và vai trò:** Theo dõi khởi tạo, vòng lặp, phát cặp và kết quả trả về.
- **Thông điệp:** Dựng thùng trước khi phát cặp giúp tránh xét mọi cặp của kho.
- **Nội dung công khai dự kiến:** B ← từ điển rỗng; CAND ← tập rỗng với j = 1,…,b và c = 1,…,C: z ← bản sao SIG[(j−1)r+1 : jr, c] k ← (j, z) nếu k chưa có trong B: B[k] ← [] B[k].append(c) với mỗi danh sách L trong B: với mỗi c < d thuộc L: CAND.add((c,d)) OUT ← tập rỗng với mỗi (c,d) trong CAND: nếu SIM(S_c,S_d) ≥ t: OUT.add((c,d)) trả OUT` Vết chạy $b=2,r=1$ $bC=8$ lượt chèn $Q=4$ lượt phát cặp $K=3$ lần kiểm Jaccard 1 cặp kết quả
- **Đầu vào và giả thiết:** HT1; đọc từ điển, danh sách và tập; các tập gốc hữu hạn không rỗng sẵn có; $t\in[0,1]$.
- **Dữ kiện, hình thức hóa và vết chạy:** V02 nối vào dòng chèn 8 lần, phát 4 lần, kiểm 3 lần; không có vòng trên mọi cặp kho.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khối giả mã lớn trái 70%; phải 30% ba trạng thái “thùng→cặp duy nhất→kết quả” kèm 8/4/3. Năm 2 đã biết vòng lặp, cần thấy dữ liệu truyền giữa pha; notes mô tả chi tiết so khóa và Jaccard.
- **Kết nối vào–ra:** Hợp đồng→thủ tục; bất biến chứng minh việc dựng nhóm và phát cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Khóa được sao chép để phân tích bộ nhớ thống nhất. Khi khóa chưa có trong từ điển, thuật toán tạo danh sách rỗng rồi mới nối mã tài liệu; khi khóa đã có, thuật toán nối vào danh sách hiện tại. Các vòng lặp đều trên tập hữu hạn. Tập CAND khử lặp sau mỗi lần phát. Jaccard gốc được tính trực tiếp cho mỗi cặp duy nhất; bỏ kiểm chữ ký ở bước 6 của sách và bắt buộc kiểm gốc trên mọi ứng viên. Trong sách, bước 7 kiểm gốc mới được ghi là tùy chọn.
- **Nguồn:** B §3.4.1 tr.92–93, §3.4.3 tr.95–96; giả mã diễn đạt và lựa chọn baseline đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Thuật toán 06.4. **Thời lượng:** 3 phút (trước 3.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: đổi tiêu đề; ghi chú diễn giả thành đoạn đọc giả mã. Âm tiết mặt trang 17 → 13. Tiêu đề cũ: “Thuật toán phân dải và xác minh”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: kiểm trình duyệt: thẻ trạng thái tách "$b=2$, $r=1$" khỏi tiêu đề để công thức không ngắt dòng. Âm tiết mặt trang 12 → 12.

#### lec06-s02-09 — Tính đúng: phân dải và xác minh

- **Mục đích và vai trò:** Giải thích vì sao thuật toán trả đúng kết quả theo tập ứng viên.
- **Thông điệp:** Tính đúng của dựng thùng không bảo đảm thu đủ mọi cặp tương đồng.
- **Nội dung công khai dự kiến:** Bất biến: ở dải đang xét, mỗi mã đã xử lý thuộc đúng nhóm khóa của nó. Bước Lập luận Khởi tạo Trước dải đầu, $B$ rỗng. Đầu dải $j$, chưa có khóa mang $j$; giữ các dải trước. Duy trì Tạo danh sách nếu khóa mới, rồi nối mã vào đúng nhóm. Kết thúc Hai mã cùng nhóm khi và chỉ khi cùng khóa; phát cặp trong mọi nhóm rồi hợp cho đúng $\mathcal C$. Đầu ra gồm đúng các cặp trong $\mathcal C$ có $s\ge t$; cặp ngoài $\mathcal C$ không được xét. Các vòng lặp hữu hạn; $C<2$ hoặc thùng có dưới hai phần tử không phát cặp.
- **Đầu vào và giả thiết:** Giả mã và đầu ra HT1.
- **Dữ kiện, hình thức hóa và vết chạy:** B rỗng trước dải đầu. Trước dải j chưa có khóa mang j; các dải trước giữ nguyên. Mỗi lượt chèn tạo đúng danh sách nếu cần rồi thêm đúng một mã, không di chuyển mã khác.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba bước khởi tạo/duy trì/kết thúc xếp dọc với một kết luận dưới. Năm 2 nối bất biến với dòng chèn đã thấy; proof đầy đủ và tập rỗng vào notes.
- **Kết nối vào–ra:** Thủ tục→bảo đảm có điều kiện; xác suất bước tới mô tả việc một cặp được sinh.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chứng minh theo số lượt chèn ở từng dải. Trước dải đầu tiên, từ điển $B$ rỗng. Ở đầu mỗi dải $j$, chưa có khóa mang chỉ số $j$, còn các nhóm của những dải trước được giữ nguyên. Vì chưa xử lý mã nào ở dải $j$, bất biến của dải này đúng. Nếu khóa mới, danh sách rỗng được tạo trước khi nối mã; nếu khóa đã có, các mã trước đó được giữ nguyên. Mỗi lượt bổ sung đúng một mã vào nhóm khóa của nó và không chuyển mã khác. Khi dựng thùng kết thúc, phát mọi cặp trong từng thùng cho đúng quan hệ tồn tại dải; phép hợp khử lặp. Kiểm Jaccard gốc xác định đầu ra trong tập ứng viên. Đầu vào của đặc tả là các tập hữu hạn không rỗng; tập rỗng nằm ngoài miền phân tích này.
- **Nguồn:** B §3.4.1, 3.4.3; chứng minh suy từ thủ tục nguồn, đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-02` (mã cũ `N02`); số hiệu: Mệnh đề 06.5. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 103 âm tiết, vượt 1,5 lần trần; giữ mệnh đề, bất biến và bảng khởi tạo–duy trì–kết thúc. Âm tiết mặt trang 103 → 59. Tiêu đề cũ: “Tính đúng của phân dải”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B13: bất biến hai chiều "danh sách khóa $(j,z)$ bằng tập cột đã chèn có tuple $z$"; bảng dùng "cột" thay "mã". Âm tiết mặt trang 59 → 60.

#### lec06-s02-15 — Tính đúng: phân dải và xác minh

- **Mạch và mục đích:** Mạch 2, thuật toán. Hoàn tất lập luận tính đúng: phát cặp, xác minh, dừng, trường hợp biên.
- **Thao tác của sinh viên:** Nối bất biến của s02-09 với hai vòng cuối của giả mã.
- **Đối tượng trung tâm:** Đẳng thức $\mathrm{CAND}=\mathcal C$ và đầu ra $\{(c,d)\in\mathcal C:s\ge t\}$.
- **Dữ kiện và ký hiệu kế thừa:** Bất biến và giả mã s02-08, s02-09; vết chạy bốn tập đặc trưng.
- **Kiến thức đầu vào:** Tập hợp, khử lặp.
- **Sản phẩm học tập:** Phát biểu đầy đủ của Mệnh đề 06.5 kèm điều kiện dừng và biên.
- **Bằng chứng kiểm tra:** Câu 1 của s02-14; Bài tập 06.2.
- **Kết nối vào–ra:** Vào: bất biến s02-09. Ra: giới hạn "cặp ngoài $\mathcal C$ không được xét" dẫn tới xác suất s02-10.
- **Nguồn:** MMDS §§3.4.1, 3.4.3, tr.92–96; CLRS §2.1 cho khuôn bất biến.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: phần thứ hai tách từ s02-09: phát cặp, xác minh, dừng, biên, lưu ý. Âm tiết mặt trang — → 59.
- **Ánh xạ ghi chú:** `lec-06-topic-02`; số hiệu: Mệnh đề 06.5; Nhận xét 06.6. **Thời lượng:** 1 phút.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: "mã tài liệu" trong ghi chú. Âm tiết mặt trang 60 → 60.

#### lec06-s02-10 — Xác suất trùng một dải

- **Mục đích và vai trò:** Suy xác suất AND từ các hàng độc lập.
- **Thông điệp:** Một dải $r$ hàng trùng với xác suất $s^r$.
- **Nội dung công khai dự kiến:** Tính đúng chỉ xét cặp trong $\mathcal C$; cần biết cặp tương đồng vào $\mathcal C$ với xác suất bao nhiêu. Cặp tập không rỗng cố định có Jaccard $s$; các MinHash lý tưởng được chọn đều, độc lập. Gọi $E_i$ là biến cố hai cột trùng ở hàng $i$ của dải: $\Pr(E_i)=s$. $\Pr(E_1\cap\cdots\cap E_r)=s^r$ Trùng dải $s^r$ Không trùng dải $1-s^r$ Với $s=0{,}8$ và $r=5$: $0{,}8^5=0{,}32768$ và $1-0{,}32768=0{,}67232$.
- **Đầu vào và giả thiết:** Định lý MinHash Bài 05 và độc lập; phép trùng tuple V03.
- **Dữ kiện, hình thức hóa và vết chạy:** HT3; V04 $s=0{,}8,r=5$ cho $s^r=0{,}32768$; thất bại dải=0,67232.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bên trái 55% ghi các sự kiện theo hàng; phải 45% công thức và thế số. Năm 2 ghép nghĩa “tất cả” với phép nhân; giả thiết hiện phía trên, còn khác mô hình V02 ở notes.
- **Kết nối vào–ra:** Tính đúng theo ứng viên→khả năng một dải nhận cặp; nhiều dải dùng biến cố bù.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tính độc lập thuộc các lần chọn hàm, chưa thuộc các cặp dữ liệu. Hai hàm cố định trong ví dụ đã cho không được dùng để suy công thức này. Giá trị $s=0{,}8$ là tương đồng thật, không là tỷ lệ trùng của một chữ ký quan sát.
- **Nguồn:** B §3.4.2 tr.93–94/PDF 22–23; Ex 3.12 tr.94.
- **Ánh xạ ghi chú:** `lec-06-topic-03` (mã cũ `N03`); số hiệu: Ví dụ 06.4. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: Nhu cầu và Giả thiết thành dòng có nhãn; bỏ hai thẻ, số đưa vào dòng Ví dụ. Âm tiết mặt trang 57 → 49.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (sư phạm): dòng ví dụ số đặt trước công thức $s^r$. Âm tiết mặt trang 49 → 52.

#### lec06-s02-11 — Xác suất thành ứng viên

- **Mục đích và vai trò:** Dùng biến cố bù để suy xác suất ít nhất một dải trùng.
- **Thông điệp:** Cặp có Jaccard s thành ứng viên với xác suất 1−(1−s^r)^b; với 20 dải 5 hàng, cặp có s=0,8 hiếm khi bị bỏ sót.
- **Nội dung công khai dự kiến:** Các dải dùng những phép thử độc lập; cặp thành ứng viên khi ít nhất một dải trùng. Không dải nào trùng với xác suất $(1-s^r)^b$. Lấy biến cố bù: $P_{b,r}(s)=1-(1-s^r)^b$ Với $b=20$, $r=5$, $s=0{,}8$: $P_{20,5}(0{,}8)\approx0{,}999644$ Chỉ khoảng 1 trên 3 000 cặp có Jaccard $0{,}8$ bị bỏ sót.
- **Đầu vào và giả thiết:** Sự kiện dải ở trang trước; các nhóm hàm độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** V04, HT3; $0{,}67232^{20}=0{,}000356058$; cả hai xác suất theo một cặp $s=0{,}8$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai hàng sự kiện→công thức trên; thế số dưới. Năm 2 thấy phép bù sau phép nhân theo dải; chưa đưa đồ thị trước khi biết trục tung.
- **Kết nối vào–ra:** Một dải→hợp nhiều dải; đồ thị dùng công thức để chọn tham số.
- **Diễn giải học thuật, lời giải và tiêu chí:** Xác suất bỏ sót tại một cặp đạt ngưỡng là $1-P(s)$. Tại $s=0{,}8$, giá trị này là $(0{,}67232)^{20}\approx0{,}000356$, khoảng 1 trên 2 800; sách làm tròn thành khoảng 1 trên 3 000. Các nhóm hàng độc lập vì toàn bộ các MinHash thành phần độc lập. Cặp dữ liệu được giữ cố định suốt phép suy. Với $r=1$, đường xác suất lõm và không có đầy đủ dạng chữ S.
- **Nguồn:** B §3.4.2 tr.93–95; M PDF 54; S3 PDF 49.
- **Ánh xạ ghi chú:** `lec-06-topic-03` (mã cũ `N03`); số hiệu: Định lý 06.7; Hệ quả 06.8. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: khuôn trang kết quả: Định lý, Chứng minh một dòng, Ý nghĩa có số. Âm tiết mặt trang 43 → 46.

#### lec06-s02-12 — Đường cong S và chọn số dải

- **Mục đích và vai trò:** Phân biệt ba đại lượng ngưỡng và so cấu hình cùng $n$.
- **Thông điệp:** Đường xác suất ứng viên tăng dốc quanh (1/b)^{1/r}; chọn b, r để vùng dốc nằm thấp hơn t khi cần ít bỏ sót, cao hơn t khi cần ít ứng viên giả.
- **Nội dung công khai dự kiến:** [Hình: Xác suất ứng viên theo Jaccard thật của cấu hình 20 dải 5 hàng và 10 dải 10 hàng, cùng 100 hàng.] $b=20$, $r=5$: $P(s)=1/2$ tại $s\approx0{,}509$; xấp xỉ $(1/b)^{1/r}\approx0{,}549$. Tại ngưỡng $t=0{,}8$: cấu hình $b=20$, $r=5$ bỏ sót khoảng $0{,}036\%$, cấu hình $b=r=10$ khoảng $32\%$. Chọn $b,r$ với $(1/b)^{1/r}\approx t$; thấp hơn $t$ để ít bỏ sót, cao hơn $t$ để ít ứng viên giả.
- **Đầu vào và giả thiết:** HT3; ngưỡng $t$ từ đặc tả.
- **Dữ kiện, hình thức hóa và vết chạy:** V04, HT4; $s_{1/2}=(1-2^{-1/b})^{1/r}\approx0{,}509$ và $(1/b)^{1/r}\approx0{,}549$ cho $(20,5)$; bỏ sót tại $t=0{,}8$: $0{,}036\%$ và $32\%$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Đồ thị lớn toàn chiều rộng; hai dòng ngắn (điểm $P=1/2$ so với xấp xỉ; bỏ sót tại $t$) và câu chốt nêu quy tắc §3.4.3. Công thức nghiệm nằm trong ghi chú.
- **Kết nối vào–ra:** Xác suất→quyết định tham số; số ứng viên và lượt phát quyết định chi phí thực tế.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đường $P_{b,r}(s)$ có dạng chữ S khi $r>1$: thấp ở Jaccard nhỏ, tăng dốc quanh một ngưỡng rồi gần 1. Phương trình $P(s)=1/2$ cho $s^r=1-2^{-1/b}$, nên điểm xác suất một nửa là $(1-2^{-1/b})^{1/r}$; giá trị $(1/b)^{1/r}$ chỉ xấp xỉ vùng dốc, không bằng nghiệm này và không phải ngưỡng chấp nhận $t$. Hai cấu hình trong hình cùng dùng 100 hàng. Tại $s=0{,}8$, xác suất bỏ sót của cấu hình $b=20$, $r=5$ là $(1-0{,}8^5)^{20}\approx0{,}000356$, của cấu hình $b=r=10$ là $(1-0{,}8^{10})^{10}\approx0{,}321$. Đây là xác suất theo từng cặp có Jaccard cho trước, không phải tỷ lệ lỗi của một kho chưa biết phân bố tương đồng. Quy tắc chọn tham số lấy từ bước 4 của §3.4.3.
- **Nguồn:** B Ex 3.12 tr.94–95, Bài 3.4.2 tr.96; S4 PDF 34/trang in 37; so $n$ cố định.
- **Ánh xạ ghi chú:** `lec-06-topic-03` (mã cũ `N03`); số hiệu: Ví dụ 06.5; Mệnh đề 06.9; Nhận xét 06.10. **Thời lượng:** 2,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `giữ`: chỉ đổi câu cuối thành Kết luận và bỏ dòng nguồn. Âm tiết mặt trang 35 → 31.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B6, B7, B11, B20: "nghiệm một nửa $s_{1/2}$", "(S-curve)"; ghi chú: chữ S cần $b\ge2$ và $r\ge2$, bỏ câu biên soạn về dấu chấm thập phân của hình (ngoại lệ hình giữ như cũ). Âm tiết mặt trang 32 → 37.

#### lec06-s02-13 — Chi phí: phân dải và xác minh

- **Mục đích và vai trò:** Gắn từng số hạng chi phí với pha thuật toán.
- **Thông điệp:** Chi phí là O(nC+Q+ΣT_J) thời gian và O(nC+K) bộ nhớ phụ; Q và K phụ thuộc dữ liệu, xấu nhất vẫn bậc hai.
- **Nội dung công khai dự kiến:** Mô hình: SIG đã có; mỗi mã một từ máy; xử lý tuple dài $r$ tốn $O(r)$, thao tác bảng băm kỳ vọng $O(1)$. $u_{j,z}$: số mã trong thùng $(j,z)$; $T_J(c,d)$: thời gian tính Jaccard của cặp $(c,d)$. Pha Công việc Chi phí kỳ vọng Dựng thùng $bC$ tuple, mỗi tuple dài $r$ $O(nC)$ Phát và khử lặp $Q=\sum_{j,z}\binom{u_{j,z}}2$ $O(Q)$ Kiểm tập gốc $K=|\mathcal C|$ cặp duy nhất $\sum_{(c,d)\in\mathcal C}T_J(c,d)$ Thời gian $O(nC+Q+\sum T_J)$; bộ nhớ phụ $O(nC+K)$, ngoài SIG đầu vào. Xấu nhất mọi cột chung thùng: $K=\binom C2$; phân dải không giảm bậc hai vô điều kiện.
- **Đầu vào và giả thiết:** Giả mã, khử lặp;$u_{j,z}$ là kích thước thùng;$K=|\mathcal C|$.
- **Dữ kiện, hình thức hóa và vết chạy:** V02:8 chèn,4 phát,3 kiểm; V01 không tự có tỷ lệ giảm. SIG $nC$ từ là đầu vào riêng. $T_J$ không giả định hằng.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Mô hình một dòng trên; bảng 3 hàng trọng tâm; công thức tổng và xấu nhất dưới. Năm 2 truy chi phí về thao tác đã chạy. Notes chứa biểu diễn tập sắp xếp và phân rã bộ nhớ chi tiết.
- **Kết nối vào–ra:** Tham số→lượng công việc; kiểm tra phần yêu cầu phối hợp thuật toán, xác suất và giới hạn.
- **Diễn giải học thuật, lời giải và tiêu chí:** Dựng thùng xử lý $bC$ tuple, mỗi tuple dài $r$, nên tốn $O(brC)=O(nC)$. Phát cặp tốn một thao tác cho mỗi trong $Q$ lượt, kể cả lượt phát lại. Nếu các tập được lưu theo thứ tự tăng, phép trộn hai dãy cho $T_J(c,d)=O(|S_c|+|S_d|)$. Khóa sao chép chiếm tối đa $nC$ từ, danh sách thùng $bC$ mã, tập cặp $K$ phần tử. Nếu mọi cột chung mỗi thùng thì $Q=b\binom C2$ và $K=\binom C2$. Trong mô hình MinHash độc lập, với $s_{cd}=\mathrm{SIM}(S_c,S_d)$, $\mathbb E[K]=\sum_{c<d}P_{b,r}(s_{cd})$: lượng công việc phụ thuộc phân bố tương đồng của kho.
- **Nguồn:** B §3.4.1, 3.4.3; phân tích suy từ giả mã đã duyệt, N04; U PDF 14; đối chiếu quan hệ ứng viên–công việc.
- **Ánh xạ ghi chú:** `lec-06-topic-04` (mã cũ `N04`); số hiệu: Mệnh đề 06.11. **Thời lượng:** 2,5 phút (trước 3.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 90 âm tiết; bảng đổi về cột Bước, Số lần, Chi phí mỗi lần, Đóng góp; bộ nhớ và xấu nhất sang s02-16. Âm tiết mặt trang 90 → 53. Tiêu đề cũ: “Chi phí phân dải và xác minh”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A5, B12, B18: mô hình ghi tập gốc đã sắp xếp trong bộ nhớ chính; cột đóng góp ghi biểu thức đếm trước ký hiệu tiệm cận; "mã tài liệu"; ghi chú: trường hợp đĩa ($2K$ lần đọc ngẫu nhiên) và bước 6 của §3.4.3. Âm tiết mặt trang 54 → 67.

#### lec06-s02-16 — Chi phí: bộ nhớ và trường hợp xấu nhất

- **Mạch và mục đích:** Mạch 2, chi phí. Bộ nhớ, thay số trên bốn tập đặc trưng và trường hợp xấu nhất.
- **Thao tác của sinh viên:** Thay $bC=8$, $Q=4$, $K=3$; tính $Q$, $K$ khi mọi cột chung thùng.
- **Đối tượng trung tâm:** $Q=b\binom C2$, $K=\binom C2$.
- **Dữ kiện và ký hiệu kế thừa:** Bảng chi phí s02-13; vết chạy bốn tập.
- **Kiến thức đầu vào:** Tổ hợp chập hai.
- **Sản phẩm học tập:** Kết luận phân dải không giảm bậc hai vô điều kiện.
- **Bằng chứng kiểm tra:** Câu 1 của s06-03; Bài tập 06.4, 06.17.
- **Kết nối vào–ra:** Vào: bảng chi phí. Ra: câu hỏi s02-14; mạch 3 khái quát sang độ đo khác.
- **Nguồn:** Phân tích chi phí từ thủ tục MMDS §3.4.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: phần thứ hai tách từ s02-13. Âm tiết mặt trang — → 38.
- **Ánh xạ ghi chú:** `lec-06-topic-04`; số hiệu: Ví dụ 06.6; Nhận xét 06.12; Mệnh đề 06.13. **Thời lượng:** 1,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A5, B18: bộ nhớ phụ ghi "ngoài SIG và tập gốc". Âm tiết mặt trang 38 → 41.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): công thức $\mathbb E[K]$, $\mathbb E[Q]$ (Mệnh đề 06.13) lên mặt trang thay dòng bộ số bốn tập, bộ số chuyển vào ghi chú. Âm tiết mặt trang 41 → 40.

#### lec06-s02-14 — Câu hỏi về phân dải

- **Mục đích và vai trò:** Giải thích vai trò khử lặp, xác minh và độc lập.
- **Thông điệp:** Đổi cấu hình dải trên cùng chữ ký đổi tập ứng viên; công thức xác suất cho thấy đánh đổi giữa ứng viên giả và bỏ sót.
- **Nội dung công khai dự kiến:** Câu hỏi: $S_1=\{a,d\},\quad S_2=\{c\}$ $S_3=\{b,d,e\},\quad S_4=\{a,c,d\}$ Hàng $S_1$ $S_2$ $S_3$ $S_4$ 1 1 3 0 1 2 0 2 0 0 Với cùng chữ ký, $b=1$, $r=2$ và $t=2/3$: tính $Q$, $K$ và tập kết quả. Viết $P_{2,1}(s)$ và $P_{1,2}(s)$; tính tại $s=1/4$ và $s=2/3$. Vì sao vết chạy với hai hàm cố định không chứng minh được các công thức xác suất ấy?
- **Đầu vào và giả thiết:** V02 hiển thị lại SIG và ba Jaccard cần dùng; các công thức phần 2.
- **Dữ kiện, hình thức hóa và vết chạy:** Đáp án: $b=1,r=2$ cho $Q=K=1$, kết quả $\{(1,4)\}$; $P_{2,1}(s)=1-(1-s)^2$, $P_{1,2}(s)=s^2$, tại $s=1/4$: $7/16$, $1/16$; tại $s=2/3$: $8/9$, $4/9$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Tập gốc bên trái, ma trận chữ ký bên phải; ba câu đánh số bên dưới. Câu 1 đổi cấu hình để không lặp vết chạy đã hiện.
- **Kết nối vào–ra:** Chi phí→kiểm phần; Jaccard là một độ đo nền, phần 3 xây các cách đo gần khác.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: một dải hai hàng cho các tuple $(1,0)$, $(3,2)$, $(0,0)$, $(1,0)$; chỉ cột 1 và 4 chung thùng, nên $Q=K=1$ và $(1,4)$ đạt ngưỡng $2/3$. So với $b=2,r=1$ ($K=3$), đòi trùng cả hai hàng đã loại hai ứng viên giả. Câu 2: $P_{2,1}(s)=1-(1-s)^2$, $P_{1,2}(s)=s^2$; tại $s=1/4$ là $7/16$ và $1/16$; tại $s=2/3$ là $8/9$ và $4/9$. Cấu hình một dải hai hàng nhận ít cặp xa hơn nhưng cũng bỏ sót cặp gần nhiều hơn. Câu 3: công thức là xác suất trên cách chọn ngẫu nhiên các MinHash; một bộ hàm cố định chỉ cho một kết quả xác định trên dữ liệu đã cho. Tiêu chí: tính đúng tuple hai hàng, phân biệt $Q$ và $K$, thấy đánh đổi giữa hai cấu hình, nêu đúng nguồn ngẫu nhiên.
- **Nguồn:** B Ex 3.8/ §3.4; câu kiểm tra áp dụng nguyên dữ kiện nguồn, tham số đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-02, lec-06-topic-03` (mã cũ `N02,N03,N04`); số hiệu: Bài tập 06.2, 06.3. **Thời lượng:** 3 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: câu 3 viết "Giải thích vì sao"; tập và bảng gộp để không quá sáu dòng. Âm tiết mặt trang 42 → 32. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.

### Mạch 3. Khoảng cách và họ nhạy cảm

#### lec06-s03-00 — 3. Khoảng cách và họ nhạy cảm

- **Mạch và vị trí:** điểm vào mạch 3; trang tiêu đề mạch `section.strand-title`, `id="mach-3"`, mở tại `#/3`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 3 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Phân dải chỉ phục vụ Jaccard; xác suất trùng một hàng bằng $s$.
- **Sản phẩm giao cho mạch sau:** định nghĩa họ nhạy cảm, công thức ghép, phân dải là AND rồi OR.
- **Vai trò chu trình:** bước `vấn đề` của cụm độ đo khoảng cách.
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/3` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 38 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-05`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (mạch, sư phạm): dòng dẫn nêu cả độ đo, họ băm và phép ghép; từ khóa "Bốn độ đo"; ghi chú bỏ nhãn quy trình. Âm tiết mặt trang 38 → 36.

#### lec06-s03-01 — Độ đo khoảng cách

- **Mục đích và vai trò:** Tính ba cách đo trên cùng hai điểm.
- **Thông điệp:** Cách định nghĩa khoảng cách quyết định ý nghĩa của gần nhau.
- **Nội dung công khai dự kiến:** Phân dải dùng MinHash nên chỉ phục vụ Jaccard trên tập. Với vector hay chuỗi, cần một độ đo khác và một phép băm hợp với độ đo ấy. [Hình: Hai điểm (2,7) và (6,4), chênh lệch tọa độ 4 và 3; đoạn thẳng nối hai điểm dài L₂ = 5.] $x=(2,7),\quad y=(6,4)$ $L_1=4+3=7$ $L_2=\sqrt{4^2+3^2}=5$ $L_\infty=\max(4,3)=4$ Cùng hai điểm, ba độ đo cho ba giá trị; ngưỡng “gần” chỉ có nghĩa khi đã chọn độ đo.
- **Đầu vào và giả thiết:** Tọa độ, hình học phẳng; Jaccard đã đo hai tập.
- **Dữ kiện, hình thức hóa và vết chạy:** V05:$\sqrt{4^2+3^2}=5$, $4+3=7$, $\max(4,3)=4$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình tọa độ trái 60% giữ tỷ lệ, trục $x_1,x_2$; phải 40% ba phép tính cùng thứ tự. Năm 2 đã có hình học, cần thấy cùng dữ liệu cho ba quy tắc; định nghĩa tổng quát sang trang sau.
- **Kết nối vào–ra:** Phân dải mới có xác suất gắn Jaccard trên tập; vector và chuỗi cần độ đo riêng. Ba cách đo của cùng cặp điểm dẫn sang miền và tiên đề metric.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đoạn thẳng nối hai điểm cho khoảng cách Euclid. Đường đi theo hai trục có tổng độ dài 7. Độ lệch lớn nhất bằng 4. Các giá trị mô tả ba cách đo, không phải ba ước lượng của cùng một đại lượng.
- **Nguồn:** B §3.5.2/Ex 3.13 tr.97–98/PDF 26–27.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Ví dụ 06.7. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu; tách câu dài; Kết luận một câu. Âm tiết mặt trang 55 → 32. Tiêu đề cũ: “Khoảng cách giữa hai điểm”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (sư phạm): ví dụ viết "tổng độ lệch", "độ dài đoạn thẳng", "độ lệch lớn nhất" thay $L_1,L_2,L_\infty$ chưa định nghĩa. Âm tiết mặt trang 34 → 45.

#### lec06-s03-02 — Độ đo khoảng cách và chuẩn vector

- **Mục đích và vai trò:** Nêu miền và bốn tiên đề trước khi dùng độ đo.
- **Thông điệp:** Độ đo mô tả gần–xa bằng một hàm có điều kiện xác định.
- **Nội dung công khai dự kiến:** Khoảng cách trên miền X $d(x,y)\ge0$. $d(x,y)=0\iff x=y$. $d(x,y)=d(y,x)$. $d(x,z)\le d(x,y)+d(y,z)$. Chuẩn trên vector $x,y\in\mathbb R^D,\ q\ge1$ $\|x-y\|_q=\left(\sum_{i=1}^D|x_i-y_i|^q\right)^{1/q}$ $\|x-y\|_\infty=\max_i|x_i-y_i|$ Với $q\ge1$, $\|x-y\|_q$ thỏa bốn tiên đề; $L_1$, $L_2$, $L_\infty$ ở trang trước là ba trường hợp.
- **Đầu vào và giả thiết:** V05, kiểu hàm và bất đẳng thức.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5; không áp định nghĩa chuẩn $q<1$; $D$ số chiều, không là khoảng cách.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khung định nghĩa ở trên 60%; dòng họ chuẩn và V05 nhãn 5/7/4 ở dưới 40%. Năm 2 chuyển số cụ thể sang miền và ký hiệu; chứng minh Minkowski không nằm tuyến chính.
- **Kết nối vào–ra:** Ba phép đo cụ thể→tiên đề; Jaccard có khoảng cách tương ứng cho tập.
- **Diễn giải học thuật, lời giải và tiêu chí:** $d$ nhận giá trị không âm; điều kiện bằng 0 tách điểm; đối xứng không phụ thuộc thứ tự cặp; bất đẳng thức tam giác chặn đường trực tiếp bằng đường qua điểm thứ ba. Với $q\ge1$, bất đẳng thức tam giác của $\|\cdot\|_q$ là bất đẳng thức Minkowski. Tuyến bài dùng $q=1,2,\infty$.
- **Nguồn:** B §3.5.1–2 tr.97–98; bổ sung $q\ge1$ để sửa phát biểu quá rộng của nguồn.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Định nghĩa 06.14. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: định nghĩa bằng "là", bốn dòng tiên đề gộp còn hai; một khối công thức. Âm tiết mặt trang 24 → 25.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: "Ý nghĩa" đổi thành "Nhận xét."; "$L_2$ (Euclid)". Âm tiết mặt trang 25 → 26.

#### lec06-s03-03 — Khoảng cách Jaccard

- **Mục đích và vai trò:** Chuyển tương đồng tập sang khoảng cách và đọc bước chứng minh tam giác.
- **Thông điệp:** MinHash biểu diễn khoảng cách Jaccard bằng xác suất khác nhau.
- **Nội dung công khai dự kiến:** $d_J(A,B)=1-\mathrm{SIM}(A,B)=\Pr[h(A)\ne h(B)]$ Các tập hữu hạn, không rỗng. Ví dụ: $d_J(S_1,S_4)=1-2/3=1/3$. Bất đẳng thức tam giác, dùng cùng một MinHash lý tưởng $h$ cho ba tập: $\{h(A)\ne h(C)\}\subseteq\{h(A)\ne h(B)\}\cup\{h(B)\ne h(C)\}$ $d_J(A,C)\le d_J(A,B)+d_J(B,C)$ Nếu $h(A)=h(B)$ và $h(B)=h(C)$ thì $h(A)=h(C)$; lấy xác suất và chặn hợp, không cần độc lập.
- **Đầu vào và giả thiết:** Tiên đề metric; định lý MinHash Bài 05 và chặn hợp.
- **Dữ kiện, hình thức hóa và vết chạy:** Cặp S1,S4 có SIM=2/3 → d_J=1/3; d_J(A,B)=Pr[h(A)≠h(B)] bằng lấy bù định lý MinHash; cùng h cho ba tập → bao hàm sự kiện → chặn hợp → tam giác.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Một chuỗi suy luận toàn chiều rộng: ví dụ cặp đã học, nhận diện khoảng cách với xác suất khác băm, bao hàm sự kiện, rồi cận tam giác. Giữ miền không rỗng và cùng h; không thêm hình trang trí.
- **Kết nối vào–ra:** Khái niệm metric→mô hình tập đã biết; khoảng cách góc mở miền vector theo hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Nếu $h(A)\ne h(C)$ thì không thể đồng thời $h(A)=h(B)$ và $h(B)=h(C)$. Định lý MinHash cho $\Pr[h(A)=h(B)]=\mathrm{SIM}(A,B)$; lấy bù được $\Pr[h(A)\ne h(B)]=d_J(A,B)$. Cặp $S_1,S_4$ có Jaccard $2/3$ nên khoảng cách $1/3$. Lấy xác suất của bao hàm sự kiện và chặn hợp cho $d_J(A,C)\le d_J(A,B)+d_J(B,C)$. Các tiên đề còn lại theo định nghĩa giao, hợp trên tập không rỗng.
- **Nguồn:** B §3.5.3 tr.98–99/PDF 27–28; P5; miền tập không rỗng.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Mệnh đề 06.15. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: định nghĩa bằng "là"; Chứng minh một dòng; đổi tên tập thứ ba thành $W$ để không trùng $C$. Âm tiết mặt trang 39 → 33.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B14: thêm "Mệnh đề. $d_J$ là khoảng cách…" trước chứng minh. Âm tiết mặt trang 34 → 46.

#### lec06-s03-04 — Khoảng cách góc

- **Mục đích và vai trò:** Tính góc và nêu miền mà góc là metric.
- **Thông điệp:** Khoảng cách góc phân biệt các hướng, độc lập với độ dài vector.
- **Nội dung công khai dự kiến:** Với $x,y\ne0$: $\theta(x,y)=\arccos\dfrac{x\cdot y}{\|x\|_2\|y\|_2}\in[0,\pi]$. Ví dụ $x=(1,2,-1)$, $y=(2,1,1)$. Tích và chuẩn $x\cdot y=3$ $\|x\|_2=\|y\|_2=\sqrt6$ Góc $\cos\theta=\frac{3}{6}=\frac12$ $\theta=\pi/3=60^\circ$ Góc là khoảng cách trên các hướng, hoặc các vector đơn vị. $x$ và $2x$ cùng hướng; vector 0 không có hướng. Khoảng cách góc ở ví dụ là $\pi/3$, không là $1-\cos\theta=1/2$.
- **Đầu vào và giả thiết:** Tích vô hướng, chuẩn Euclid, và điều kiện d=0.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5, V06; góc radian $\theta=\arccos((x\cdot y)/(\|x\|\|y\|))$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 50% hai vector chuẩn hóa thành hướng; phải 50% tích/chuẩn/góc ba dòng. Năm 2 phân biệt cosin và góc bằng đơn vị; nhận xét $1-\cos\theta$ ở notes.
- **Kết nối vào–ra:** Jaccard đo tập→góc đo hướng; chuỗi dùng phép thay đổi rời rạc.
- **Diễn giải học thuật, lời giải và tiêu chí:** Cosin là độ tương đồng bằng $1/2$ trong ví dụ; khoảng cách góc bằng $\pi/3$. Hai bội dương có góc 0 nên chỉ xem góc là metric sau đồng nhất hướng hoặc chuẩn hóa. Hai vector đối hướng có góc $\pi$. Bất đẳng thức tam giác: trên mặt cầu đơn vị, góc là độ dài cung lớn ngắn nhất nối hai hướng, và đường đi qua hướng thứ ba không ngắn hơn cung ấy. Phép băm dấu phần 4 sử dụng đúng góc này.
- **Nguồn:** B §3.5.4/Ex 3.14 tr.99/PDF 28; S4 PDF 45/trang in 48; đối chiếu thuật ngữ.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Định nghĩa 06.16; Ví dụ 06.8; Nhận xét 06.17. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bốn khối công thức thành bảng hai hàng; Lưu ý thay ex-note. Âm tiết mặt trang 41 → 27.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B9, B11: định nghĩa ghi "trên các hướng (vector đơn vị)"; "độ tương đồng cosin (cosine similarity)"; công thức bọc ngoặc để không ngắt dòng. Âm tiết mặt trang 27 → 38.

#### lec06-s03-05 — Khoảng cách chỉnh sửa

- **Mục đích và vai trò:** Theo dõi phép chèn/xóa và tính khoảng cách theo LCS.
- **Thông điệp:** Khoảng cách chỉnh sửa trong bài đếm phép chèn và xóa.
- **Nội dung công khai dự kiến:** Khoảng cách chỉnh sửa là số thao tác ít nhất để biến chuỗi này thành chuỗi kia; mỗi bước chèn hoặc xóa một ký tự. Biến $x=$ `abcde` thành $y=$ `acfdeg`: Thao tác Chuỗi sau thao tác Xóa b `acde` Chèn f `acfde` Chèn g `acfdeg` $L$ là độ dài dãy con chung dài nhất (không cần liên tiếp); ở đây là `acde`, $L=4$. $d_{\rm edit}(x,y)=|x|+|y|-2L=5+6-2\cdot4=3$
- **Đầu vào và giả thiết:** Chuỗi, dãy con, độ dài; chỉ chèn/xóa.
- **Dữ kiện, hình thức hóa và vết chạy:** HT5, V07; $5+6-8=3$; dãy con $acde$. Không có phép thay thế một bước.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Vết bốn trạng thái trên 70% ngang, mỗi mũi tên ghi thao tác; công thức dưới 30%. Năm 2 thấy dữ liệu còn lại trước công thức; proof hai cận và định nghĩa LCS đầy đủ trong notes.
- **Kết nối vào–ra:** Góc đo thay hướng→chuỗi đo thao tác sửa; Hamming sẽ giữ cố định độ dài/vị trí.
- **Diễn giải học thuật, lời giải và tiêu chí:** Một phương án tối ưu giữ một dãy con chung và xóa/chèn các ký tự khác. Giữ $L$ ký tự cần $|x|-L$ lần xóa và $|y|-L$ lần chèn. Ngược lại, các ký tự không bị xóa tạo thành dãy con chung nên không giữ quá $L$. Đây là lập luận giá trị tối ưu, không cung cấp thuật toán quy hoạch động tính dãy con chung dài nhất (longest common subsequence, LCS). Chương 3 của MMDS không xây họ LSH riêng cho khoảng cách chỉnh sửa; bài này dùng nó để so với Hamming và minh họa tiên đề metric.
- **Nguồn:** B §3.5.5/Ex 3.15–16 tr.100/PDF 29.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Ví dụ 06.9; Định nghĩa 06.18; Mệnh đề 06.19. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bảng ba thao tác thay bằng một dòng vết; định nghĩa bằng "là". Âm tiết mặt trang 66 → 40. Tiêu đề cũ: “Khoảng cách chỉnh sửa chuỗi”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11, nhẹ: "(edit distance)", "(longest common subsequence)"; công thức $|x|+|y|-2L$ thành dòng "Mệnh đề."; ghi chú phân biệt Levenshtein. Âm tiết mặt trang 40 → 58.

#### lec06-s03-06 — Khoảng cách Hamming

- **Mục đích và vai trò:** Đếm tọa độ khác nhau trên vector cùng độ dài.
- **Thông điệp:** Hamming giữ vị trí và đếm số bất đồng.
- **Nội dung công khai dự kiến:** Chỉ số 1 2 3 4 5 x 1 0 1 0 1 y 1 1 1 1 0 So sánh Trùng Khác Trùng Khác Khác $d_H(x,y)=\sum_{i=1}^D\mathbf1[x_i\ne y_i]=3$ $\mathbf1[E]=1$ nếu $E$ đúng, bằng 0 nếu $E$ sai. Hamming đếm vị trí khác trên hai vector cùng chiều.
- **Đầu vào và giả thiết:** Vector rời rạc cùng chiều; khác với phép chèn/xóa.
- **Dữ kiện, hình thức hóa và vết chạy:** V08, HT5; hai vị trí trùng 1,3 dùng lại trong s04-01/02.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai hàng bit thẳng cột, nhãn “trùng/khác” dưới từng vị trí; công thức dưới. Năm 2 đếm trực tiếp trước dùng mẫu số $D$; notes chứng minh tam giác theo tọa độ.
- **Kết nối vào–ra:** Chuỗi có thể đổi chiều→vector cố định chiều; các độ đo đã đủ để diễn đạt họ gần–xa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Nếu $x_i\ne z_i$ thì ít nhất một trong $x_i\ne y_i$ hoặc $y_i\ne z_i$ đúng. Cộng theo tọa độ cho bất đẳng thức tam giác.
- **Nguồn:** B §3.5.6/Ex 3.17 tr.101/PDF 30.
- **Ánh xạ ghi chú:** `lec-06-topic-05` (mã cũ `N05`); số hiệu: Ví dụ 06.10; Định nghĩa 06.20; Nhận xét 06.21. **Thời lượng:** 1,5 phút (trước 1.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `giữ`: thêm câu định nghĩa bằng "là" và dòng Ký hiệu; bỏ câu kết luận thừa. Âm tiết mặt trang 32 → 31.

#### lec06-s03-07 — Họ băm nhạy cảm theo tính cục bộ

- **Mục đích và vai trò:** Diễn giải đầy đủ bốn tham số và nguồn xác suất.
- **Thông điệp:** Họ LSH khái quát MinHash: với hàm chọn ngẫu nhiên, cặp gần trùng với xác suất ít nhất p1, cặp xa không quá p2.
- **Nội dung công khai dự kiến:** Khái quát MinHash: chọn ngẫu nhiên một hàm $h$ từ họ $\mathcal H$; cặp gần dễ trùng, cặp xa khó trùng. Với $0\le d_1<d_2$ và $0\le p_2<p_1\le1$, họ $\mathcal H$ là $(d_1,d_2,p_1,p_2)$-nhạy cảm nếu với mọi cặp $x,y$, xác suất trùng $P=\Pr[h(x)=h(y)]$ thỏa: $d(x,y)\le d_1\ \Rightarrow\ P\ge p_1$ $d(x,y)\ge d_2\ \Rightarrow\ P\le p_2$ [Hình: Cặp gần có xác suất trùng ít nhất p1, cặp xa có xác suất trùng không quá p2, miền giữa không được bảo đảm.] Xác suất lấy theo cách chọn $h$, cùng $h$ cho hai đối tượng; miền giữa không được bảo đảm.
- **Đầu vào và giả thiết:** Metric, sự kiện va chạm MinHash đã biết.
- **Dữ kiện, hình thức hóa và vết chạy:** HT6; cùng hàm $h$ áp cho hai đối tượng; không lấy xác suất trên “mỗi hàm cố định”.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trục khoảng cách chia gần/giữa/xa chiếm 45% trên; hai bất đẳng thức lớn dưới. Năm 2 cần liên kết hướng≤với≥xác suất; không vẽ đường cong cụ thể cho mọi họ.
- **Kết nối vào–ra:** Các độ đo→mô hình xác suất chung; MinHash kiểm định định nghĩa bằng một ví dụ đã quen.
- **Diễn giải học thuật, lời giải và tiêu chí:** Độ đo xác định cặp gần và xa; một họ băm phải có phân phối lấy mẫu và hai cận xác suất tương ứng. Nguồn ngẫu nhiên là phép lấy $h$ từ họ có phân phối. Với dữ liệu và $h$ đã cố định, kết quả trùng là xác định. Định nghĩa chỉ đòi hai cận; không đòi đẳng thức giữa xác suất va chạm và một độ tương đồng.
- **Nguồn:** B §3.6.1 tr.103–104/PDF 32–33; S4 PDF 19/trang in 22 và PDF 20/trang in 23.
- **Ánh xạ ghi chú:** `lec-06-topic-06` (mã cũ `N06`); số hiệu: Định nghĩa 06.22. **Thời lượng:** 3 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: Nhu cầu và Định nghĩa có nhãn; giữ điều kiện trên mặt trang. Âm tiết mặt trang 53 → 40.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12, B15, B11: Nhu cầu có số của MinHash trước định nghĩa; hai công thức hiển thị hết chiều ngang, hình chuyển xuống; "(locality-sensitive family)". Âm tiết mặt trang 41 → 52.

#### lec06-s03-08 — Ví dụ: họ MinHash theo Jaccard

- **Mục đích và vai trò:** Chuyển cận khoảng cách thành cận va chạm.
- **Thông điệp:** MinHash cho một trường hợp cụ thể của họ nhạy cảm.
- **Nội dung công khai dự kiến:** Định lý MinHash: $\Pr[h(A)=h(B)]=\mathrm{SIM}(A,B)=1-d_J(A,B)$. Cặp gần $d_J\le0{,}3$ thì xác suất trùng $\ge0{,}7$. Cặp xa $d_J\ge0{,}6$ thì xác suất trùng $\le0{,}4$. Vậy họ MinHash là $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$-nhạy cảm. Tổng quát: họ MinHash là $(d_1,d_2,1-d_1,1-d_2)$-nhạy cảm với mọi $0\le d_1<d_2\le1$.
- **Đầu vào và giả thiết:** HT6; tập hữu hạn không rỗng, MinHash lý tưởng.
- **Dữ kiện, hình thức hóa và vết chạy:** B Ex 3.18; phân biệt bộ tham số này với V09(.2, .6, .8, .4) sẽ dùng cho ghép.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng 2 hàng miền khoảng cách/phép trừ/cận xác suất; dòng bộ 4 dưới. Năm 2 thực hiện $1-d$ để thấy đảo hướng bất đẳng thức; không thêm đồ thị trùng chức năng.
- **Kết nối vào–ra:** Định nghĩa→một họ có thật; phép ghép sẽ thay cận xác suất của họ cơ sở.
- **Diễn giải học thuật, lời giải và tiêu chí:** Từ tính đơn điệu giảm của $1-d$, miền gần cho cận dưới còn miền xa cho cận trên. Hai ngưỡng không quyết định hành vi trong miền giữa. Bộ tham số suy trực tiếp từ định lý MinHash.
- **Nguồn:** B §3.6.2/Ex 3.18 tr.104–105/PDF 33–34.
- **Ánh xạ ghi chú:** `lec-06-topic-06` (mã cũ `N06`); số hiệu: Hệ quả 06.23; Ví dụ 06.11. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Ví dụ:; hai thẻ chứa câu thành hai dòng. Âm tiết mặt trang 36 → 35. Tiêu đề cũ: “Họ MinHash theo Jaccard”.

#### lec06-s03-09 — Phép ghép đồng thời

- **Mục đích và vai trò:** Suy biến đổi xác suất AND và các cận của họ.
- **Thông điệp:** Ghép đồng thời r hàm độc lập biến họ (d1,d2,p1,p2) thành (d1,d2,p1^r,p2^r): giảm mạnh xác suất của cặp xa nhưng cũng giảm cặp gần.
- **Nội dung công khai dự kiến:** Một phép thử chỉ tách $p_1$ và $p_2$ một độ chênh nhỏ; phép ghép khuếch đại độ chênh này. Trùng một dải tương ứng với ghép đồng thời $r$ MinHash. Phép ghép đồng thời (AND): chọn $r$ hàm độc lập từ họ; nhận cặp khi cả $r$ hàm trùng. Với $p=\Pr[h(x)=h(y)]$ của một cặp cố định: $g(x)=(h_1(x),\ldots,h_r(x)),\qquad\Pr[g(x)=g(y)]=p^r$ Họ mới là $(d_1,d_2,p_1^r,p_2^r)$-nhạy cảm. $p$ $p^4$ 0,8 0,4096 0,4 0,0256 Cặp xa hiếm trùng hơn nhiều, nhưng cặp gần cũng giảm từ 0,8 xuống khoảng 0,41.
- **Đầu vào và giả thiết:** Dải nhiều hàng V03, họ 4 tham số, độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7; $p$ va chạm cặp cố định;$r=4,p=.8$ cho.4096;$p=.4$ cho.0256.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Nhóm $r$ phép thử trái 55%, ngoặc tuple; phải 45% phép nhân và cận. Năm 2 đối chiếu đúng cấu trúc một dải trước khái quát; chi tiết tính đơn điệu ở notes.
- **Kết nối vào–ra:** Họ cơ sở→AND; OR bổ sung cơ hội trùng để giảm bỏ sót.
- **Diễn giải học thuật, lời giải và tiêu chí:** Cặp dữ liệu được giữ cố định; mỗi phép thử cơ sở trùng với xác suất $p$. Sự kiện bằng tuple là giao của $r$ sự kiện trùng. Độc lập cho tích $p^r$. Hàm $p\mapsto p^r$ tăng trên [0,1], nên bảo toàn hướng hai cận gần/xa. Khi $r>1$, xác suất trong (0,1) giảm; nhiều cặp gần cũng khó được chọn hơn.
- **Nguồn:** B §3.6.3 tr.105–106/PDF 34–35; S4 PDF 25/trang in 28.
- **Ánh xạ ghi chú:** `lec-06-topic-07` (mã cũ `N07`); số hiệu: Định nghĩa 06.25; Mệnh đề 06.26. **Thời lượng:** 2,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tách câu dài; bảng nhỏ thành dòng Ví dụ. Âm tiết mặt trang 73 → 45.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A1, B5, B12: Nhu cầu "cần hạ $p_2$ về gần 0"; dòng ví dụ nêu họ $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$ của Ví dụ 3.19 và đứng trước công thức; ghi chú nêu AND tăng tỷ số, không tăng hiệu. Âm tiết mặt trang 45 → 53.

#### lec06-s03-10 — Phép ghép ít nhất một

- **Mục đích và vai trò:** Suy biến đổi xác suất OR bằng biến cố bù.
- **Thông điệp:** Ghép ít nhất một b hàm biến họ (d1,d2,p1,p2) thành (d1,d2,1−(1−p1)^b,1−(1−p2)^b): tăng cả hai xác suất; đặt sau AND để kéo cặp gần lên.
- **Nội dung công khai dự kiến:** AND làm giảm cả hai xác suất. Phép ghép ít nhất một (OR) chọn $b$ hàm độc lập và nhận cặp khi ít nhất một hàm trùng; hợp các dải tương ứng với OR. Không hàm nào trùng với xác suất $(1-p)^b$; lấy biến cố bù, cặp được nhận với xác suất $1-(1-p)^b$ Họ mới là $(d_1,d_2,1-(1-p_1)^b,1-(1-p_2)^b)$-nhạy cảm. $p$ $1-(1-p)^4$ 0,8 0,9984 0,4 0,8704 OR tăng cả hai xác suất; đặt sau AND, nó tăng lại cận gần.
- **Đầu vào và giả thiết:** AND và phép bù; hợp dải V02.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7;$b=4,p=.8$ cho.9984;$p=.4$ cho.8704.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** $b$ bảng trái 55% mũi tên vào phép hợp; phải 45% sự kiện không trùng và bù. Năm 2 gắn OR với hợp ứng viên đã chạy; không diễn đạt OR thành bằng một tuple.
- **Kết nối vào–ra:** AND lọc chặt→OR bù cơ hội; hai thứ tự ghép cho hành vi khác nhau.
- **Diễn giải học thuật, lời giải và tiêu chí:** Độc lập là điều kiện để nhân $b$ xác suất $1-p$. Biểu thức $1-(1-p)^b$ tăng theo $p$ nên biến đổi được hai cận của họ. Với $p=0{,}4$, OR 4 cho $1-0{,}6^4=0{,}8704$: cặp xa cũng dễ được nhận hơn, nên OR thường đặt sau AND. Quan hệ “trùng ở ít nhất một bảng” có thể không bắc cầu, nên nói chung không thay được bằng phép bằng của một mã đơn.
- **Nguồn:** B §3.6.3 tr.106–107; S4 PDF 27/trang in 30.
- **Ánh xạ ghi chú:** `lec-06-topic-07` (mã cũ `N07`); số hiệu: Định nghĩa 06.25; Mệnh đề 06.26. **Thời lượng:** 2,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tách câu dài; bảng nhỏ thành dòng Ví dụ. Âm tiết mặt trang 73 → 53.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12: Nhu cầu có số, ví dụ trước định nghĩa; ghi chú: từng phép ghép riêng không tăng độ chênh; số hiệu 06.25 → 06.26. Âm tiết mặt trang 54 → 57.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: dấu câu trong ghi chú. Âm tiết mặt trang 57 → 57.

#### lec06-s03-11 — Ví dụ: hai thứ tự ghép trên 16 phép thử

- **Mục đích và vai trò:** So sánh AND–OR với OR–AND trên cùng 16 phép thử.
- **Thông điệp:** Cùng số hàm cơ sở không cho cùng đánh đổi.
- **Nội dung công khai dự kiến:** Họ $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$-nhạy cảm, cùng 16 phép thử cơ sở độc lập. Thứ tự Biến đổi xác suất Cận gần Cận xa AND 4 → OR 4 $F(p)=1-(1-p^4)^4$ 0,878497 0,098535 OR 4 → AND 4 $G(p)=[1-(1-p)^4]^4$ 0,993615 0,573952 AND rồi OR đưa hai cận $0{,}8$ và $0{,}4$ thành $0{,}88$ và $0{,}10$, độ chênh tăng; OR rồi AND giữ cặp gần tốt hơn nhưng nhận cặp xa tới $0{,}57$. Các số là cận biến đổi từ $p_1,p_2$, không là xác suất chính xác của mọi cặp.
- **Đầu vào và giả thiết:** HT7 và phép thế xác suất.
- **Dữ kiện, hình thức hóa và vết chạy:** V09; trung gian $p^4$=.4096/.0256; OR 4=.9984/.8704; dùng số chưa làm tròn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai cột 50/50 cùng hàng: cấu trúc→công thức→cận gần/xa. Năm 2 so cùng tiêu chí và giữ 16 hàm; proof đã có nên mặt trang chỉ so phép ghép và giá trị.
- **Kết nối vào–ra:** Hai quy tắc→lựa chọn cấu trúc; cấu trúc cần được hiện thực qua bảng và có chi phí.
- **Diễn giải học thuật, lời giải và tiêu chí:** AND–OR cho cận xa nhỏ hơn nhưng cận gần cũng nhỏ hơn. OR–AND giữ cặp gần nhiều hơn đồng thời nhận cặp xa nhiều hơn. Hai kết luận cùng được đọc từ bảng; không có thứ tự tốt hơn vô điều kiện theo cả hai loại lỗi. Vì $F$ và $G$ tăng trên $[0,1]$, chúng biến cận dưới của cặp gần thành cận dưới và cận trên của cặp xa thành cận trên; chỉ một cặp có xác suất cơ sở đúng bằng $p$ mới có xác suất ghép đúng bằng $F(p)$ hoặc $G(p)$.
- **Nguồn:** B Ex 3.19–20 tr.106–108/PDF 35–37.
- **Ánh xạ ghi chú:** `lec-06-topic-07` (mã cũ `N07`); số hiệu: Ví dụ 06.12. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Ví dụ:; Lưu ý đứng trước Kết luận. Âm tiết mặt trang 71 → 52. Tiêu đề cũ: “So sánh hai thứ tự ghép”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: dòng dữ kiện thêm nhiệm vụ "tính cận theo hai thứ tự ghép". Âm tiết mặt trang 57 → 60.

#### lec06-s03-12 — Phân dải như phép ghép AND rồi OR

- **Mục đích và vai trò:** Nối biểu thức logic với lưu trữ và số phép thử.
- **Thông điệp:** Với AND rồi OR, mỗi nhóm AND tạo khóa tuple và bước OR hợp các tập cặp.
- **Nội dung công khai dự kiến:** [Hình: Mười sáu phép thử chia bốn nhóm AND; phép OR hợp cặp của bốn nhóm.] AND $r$ rồi OR $b$ tương ứng với phân dải: tính $br$ giá trị → tạo $b$ tuple → tra $b$ bảng → hợp cặp. Với họ MinHash, $p=s$ nên $F(s)=1-(1-s^4)^4=P_{4,4}(s)$, đường cong S với $b=r=4$. Số phép thử đo chi phí tính hàm; kích thước thùng quyết định số lượt phát cặp.
- **Đầu vào và giả thiết:** Giả mã phân dải và hai phép ghép.
- **Dữ kiện, hình thức hóa và vết chạy:** HT7; sơ đồ thực hiện AND_r rồi OR_b. Với V09, đây là AND 4 rồi OR 4. Hai thứ tự đều dùng 16 giá trị, nhưng OR rồi AND phải hợp cặp trong từng nhóm OR rồi giao các tập cặp của những nhóm OR; chi phí phát và kiểm cặp vẫn phụ thuộc Q, K.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ 4 bước ngang trên; bảng nhỏ thao tác/số lượng dưới. Năm 2 chuyển ký hiệu xác suất thành thao tác lập trình quen; không tạo bảo đảm tốc độ từ số hàm.
- **Kết nối vào–ra:** Xác suất ghép→cơ chế và chi phí; kiểm tra phần nối miền metric với điều kiện họ.
- **Diễn giải học thuật, lời giải và tiêu chí:** Trong cấu trúc AND rồi OR, mỗi nhóm AND lưu trực tiếp một tuple; bước OR hợp các tập cặp qua nhiều bảng. Với thứ tự OR rồi AND, mỗi nhóm OR hợp các cặp từ các bảng cơ sở của nhóm, rồi bước AND lấy giao các tập cặp của những nhóm ấy. Quan hệ OR không được thay bằng phép bằng nhau của một tuple. Dù việc tính hàm băm ít tốn kém, thùng lớn vẫn phát nhiều cặp. Giá trị $br$ chỉ đo số phép thử cơ sở, mỗi phép có chi phí tùy họ.
- **Nguồn:** B §3.6.3 tr.105–108; liên hệ thuật toán §3.4.1 đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-07` (mã cũ `N07`); số hiệu: Nhận xét 06.27. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bỏ chuỗi mũi tên; ex-note thành dòng thường. Âm tiết mặt trang 46 → 33. Tiêu đề cũ: “Thực hiện AND rồi OR bằng phân dải”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: số hiệu Nhận xét 06.26 → 06.27. Âm tiết mặt trang 34 → 34.

#### lec06-s03-13 — Câu hỏi về độ đo và phép ghép

- **Mục đích và vai trò:** Đọc cận họ, phân biệt miền và tính ghép.
- **Thông điệp:** Vận dụng phép ghép để mở rộng khoảng cách hai cận, và tính hai độ đo mới trên dữ kiện nhỏ.
- **Nội dung công khai dự kiến:** Câu hỏi: Áp dụng AND 2 rồi OR 2 cho họ MinHash $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$. Tính hai cận mới và so độ chênh $p_1-p_2$ trước và sau. Tính khoảng cách chỉnh sửa (chèn, xóa) giữa `abc` và `bca`. Tính góc giữa $(1,1,0)$ và $(1,0,0)$.
- **Đầu vào và giả thiết:** HT5–HT7; bộ tham số Ex 3.18.
- **Dữ kiện, hình thức hóa và vết chạy:** Đáp án: $(0{,}3;\ 0{,}6;\ 0{,}7399;\ 0{,}2944)$; khoảng cách chỉnh sửa 2; góc $45^\circ$. Câu cũ trùng s03-07/08, s03-04 và Bài 3.6.1(a) đã thay.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Một khối gồm 3 nhiệm vụ độc lập, mỗi yêu cầu tối đa 2 dòng. Năm 2 kiểm cùng ba điều kiện vừa xây; lời giải và tiêu chí trong notes, không thêm ví dụ ngoài nguồn.
- **Kết nối vào–ra:** Cơ chế ghép→tự kiểm; các họ Hamming/góc/Euclid cung cấp phép thử cơ sở cụ thể.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: AND 2 cho $0{,}49$ và $0{,}16$; OR 2 cho $1-0{,}51^2=0{,}7399$ và $1-0{,}84^2=0{,}2944$. Họ mới là $(0{,}3;\ 0{,}6;\ 0{,}7399;\ 0{,}2944)$-nhạy cảm; độ chênh $p_1-p_2$ tăng từ $0{,}3$ lên $0{,}4455$, với điều kiện các hàm độc lập. Câu 2: dãy con chung dài nhất là `bc`, $L=2$, nên khoảng cách là $3+3-2\cdot2=2$ (xóa `a` đầu, chèn `a` cuối). Câu 3: tích vô hướng 1, hai chuẩn $\sqrt2$ và 1, nên $\cos\theta=1/\sqrt2$ và $\theta=\pi/4=45^\circ$. Tiêu chí: ghép đúng thứ tự và nêu độc lập, xác định đúng dãy con chung, tính đúng chuẩn.
- **Nguồn:** B Ex 3.18 tr.105, Bài 3.6.1(a) tr.108, §3.5.4 tr.99; kiểm tra trực tiếp định nghĩa.
- **Ánh xạ ghi chú:** `lec-06-topic-05, lec-06-topic-07` (mã cũ `N05,N06,N07`); số hiệu: Bài tập 06.5, 06.7. **Thời lượng:** 3 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `giữ`: chỉ bỏ dòng nguồn. Âm tiết mặt trang 48 → 36. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B17: câu 1 (21 âm tiết) tách thành hai câu. Âm tiết mặt trang 38 → 39.

### Mạch 4. Các họ băm theo độ đo

#### lec06-s04-00 — 4. Các họ băm theo độ đo

- **Mạch và vị trí:** điểm vào mạch 4; trang tiêu đề mạch `section.strand-title`, `id="mach-4"`, mở tại `#/4`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 4 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Định nghĩa họ nhạy cảm, phép ghép.
- **Sản phẩm giao cho mạch sau:** thuật toán tìm cặp với họ nhạy cảm (s04-14), dùng lại ở vân tay; ba họ cơ sở và giả thiết của bảo đảm, dùng ở tổng kết.
- **Vai trò chu trình:** ngoài chu trình khái niệm (dòng dẫn nêu nhu cầu chung của ba họ; s04-01 có Nhu cầu riêng).
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/4` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 40 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-08`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B4, C: từ khóa thêm "Thuật toán chung", rút còn bốn cụm; ghi chú nêu mạch 4 và 5 là hai nhánh song song, bỏ "giao cho mạch sau". Âm tiết mặt trang 40 → 32.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): ghi chú sửa phạm vi "song song". Âm tiết mặt trang 32 → 32.

#### lec06-s04-14 — Thuật toán: tìm cặp với họ nhạy cảm

- **Mạch và mục đích:** Mạch 4, thuật toán. Phát biểu thuật toán tìm cặp với một họ $(d_1,d_2,p_1,p_2)$-nhạy cảm bất kỳ, để ba họ cơ sở của mạch có chỗ dùng chung và Bài 07 có chế độ truy vấn để dẫn lại.
- **Thao tác của sinh viên:** Đọc Đầu vào, Đầu ra; so giả mã với giả mã phân dải s02-08 và chỉ ra hai dòng khác (tạo khóa, xác minh); đọc bảo đảm theo cặp.
- **Đối tượng trung tâm:** Khóa $(j,g_j(x))$ với $g_j=(h_{j1},\ldots,h_{jr})$, $h_{ji}$ lấy độc lập từ $\mathcal H$; xác minh bằng $d(x_c,x_e)\le d_1$.
- **Dữ kiện và ký hiệu kế thừa:** Định nghĩa họ nhạy cảm (s03-07), AND $r$ rồi OR $b$ (s03-09, s03-10, s03-12), giả mã và bất biến của phân dải (s02-08, s02-09).
- **Kiến thức đầu vào:** Phép ghép, tập ứng viên $\mathcal C$.
- **Sản phẩm học tập:** Bảo đảm: cặp có $d\le d_1$ thành ứng viên với xác suất $\ge1-(1-p_1^r)^b$, cặp có $d\ge d_2$ với xác suất $\le1-(1-p_2^r)^b$.
- **Bằng chứng kiểm tra:** Câu hỏi kho ảnh 128 chiều (s06-04, câu 6) và hàng "Tìm cặp với họ nhạy cảm" của bảng s06-02.
- **Kết nối vào–ra:** Vào: trang tiêu đề mạch 4. Ra: họ chọn tọa độ s04-01 cung cấp $\mathcal H$ đầu tiên. Ghi chú diễn giả nêu biến thể truy vấn cho Bài 07.
- **Nguồn:** MMDS §3.4.1, tr.92–93; §3.6.3, tr.105–108.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `thêm` theo A4 của điều phối viên (phát hiện nghiêm trọng của vai chuyên gia: mạch 4 thiếu trang đặc tả và giả mã cho thuật toán tổng quát). Âm tiết mặt trang — → 39; giả mã 7 dòng; mạch 4 thành 15 trang, trang Nội dung không đổi.
- **Ánh xạ ghi chú:** `lec-06-topic-07`; ghi chú không có khối riêng, gần nhất là Thuật toán 06.4 và Mệnh đề 06.26. **Thời lượng:** 1,5 phút (lấy từ s04-01, s04-04, s04-06).
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: ghi chú giải thích chỉ số $e$. Âm tiết mặt trang 39 → 39.

#### lec06-s04-01 — Họ băm chọn tọa độ

- **Mục đích và vai trò:** Mở phần 4: định nghĩa họ băm chọn tọa độ cho Hamming và chạy trên cặp $x,y$ của định nghĩa $d_H$.
- **Thông điệp:** Có đúng $D-d_H(x,y)$ chỉ số cho hai vector cùng giá trị băm.
- **Nội dung công khai dự kiến:** Họ LSH cho khoảng cách Hamming trên vector $D$ chiều, $D>0$: $h_I(x)=x_I,\qquad I\in\{1,\ldots,D\}$ Chỉ số $I$ 1 2 3 4 5 $h_I(x)$ 1 0 1 0 1 $h_I(y)$ 1 1 1 1 0 Cùng giá trị băm Có Không Có Không Không Một lần chọn $I$ cho một hàm; cùng hàm đó băm mọi vector của kho. Có $D-d_H(x,y)=5-3=2$ chỉ số cho $x,y$ cùng giá trị băm.
- **Đầu vào và giả thiết:** Hamming và khung họ; phép đọc phần tử mảng.
- **Dữ kiện, hình thức hóa và vết chạy:** V08; $D=5,d_H=3$; cùng $I$ cho cả hai vector.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn và công thức hàm ở trên; bảng giá trị băm theo từng chỉ số; dòng phụ về một hàm chung; câu chốt đếm chỉ số thuận lợi. Năm 2 thấy hàm và đầu ra trước công thức xác suất.
- **Kết nối vào–ra:** Định nghĩa metric chưa tự cung cấp họ LSH. Bắt đầu xây và kiểm riêng phép thử tọa độ cho Hamming; số vị trí trùng dẫn tới chứng minh đếm ở s04-02.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tính metric chưa bảo đảm có họ LSH; với mỗi độ đo cần chỉ ra nguồn ngẫu nhiên và chứng minh xác suất va chạm riêng. Hamming cho họ đơn giản nhất: hàm chỉ đọc một tọa độ. Cặp $x,y$ là cặp đã dùng khi định nghĩa $d_H$. Nếu mỗi vector dùng một chỉ số riêng thì không còn một hàm chung, và việc hai giá trị băm bằng nhau không nói gì về khoảng cách. Mỗi lần tính chỉ đọc một tọa độ, tốn $O(1)$ khi truy cập mảng mất thời gian hằng.
- **Nguồn:** B §3.7.1 tr.109/PDF 38; dữ kiện Ex 3.17 tr.101.
- **Ánh xạ ghi chú:** `lec-06-topic-08` (mã cũ `N08`); số hiệu: Ví dụ 06.13; Định nghĩa 06.28. **Thời lượng:** 1,5 phút (trước 2 phút; lượt sửa deck chuyển 0,5 phút cho s04-14).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu có dữ kiện; ex-note sang ghi chú. Âm tiết mặt trang 46 → 32.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B7, nhẹ: "vector có $D$ thành phần rời rạc"; hàm định nghĩa bằng câu "là"; thời lượng 2 → 1,5 phút cho s04-14. Âm tiết mặt trang 32 → 41.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): ghi chú mở bằng câu nối với thuật toán tìm cặp với họ nhạy cảm. Âm tiết mặt trang 41 → 41.

#### lec06-s04-02 — Tính nhạy cảm của họ chọn tọa độ

- **Mục đích và vai trò:** Chứng minh bằng đếm xác suất va chạm của họ chọn tọa độ và nêu bộ tham số nhạy cảm theo định nghĩa ở phần 3.
- **Thông điệp:** Họ chọn tọa độ là $(d_1,d_2,1-d_1/D,1-d_2/D)$-nhạy cảm; ghép cần chỉ số độc lập.
- **Nội dung công khai dự kiến:** Chọn $I$ đều trong $D$ chỉ số; có đúng $D-d_H(x,y)$ chỉ số thuận lợi. $\Pr[h_I(x)=h_I(y)]=\frac{D-d_H(x,y)}D=1-\frac{d_H(x,y)}D$ $D=5,\quad d_H(x,y)=3\quad\Rightarrow\quad \Pr=2/5$ Với $d_1<d_2$, họ chọn tọa độ là $(d_1,d_2,1-d_1/D,1-d_2/D)$-nhạy cảm. Ghép AND hoặc OR cần các chỉ số độc lập, lấy có hoàn lại.
- **Đầu vào và giả thiết:** Số chỉ số trùng ở s04-01, phân phối đều.
- **Dữ kiện, hình thức hóa và vết chạy:** HT8; V08 trùng 2 trên 5. Họ hữu hạn không giới hạn số lần lấy mẫu độc lập.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu phép đếm; hai dòng công thức (tổng quát, ví dụ); dòng bộ tham số nhạy cảm; câu chốt về ghép. Năm 2 dùng xác suất hữu hạn để chứng minh; không đưa thêm đường cong.
- **Kết nối vào–ra:** Phép thử→bảo đảm; dữ liệu theo hướng cần một phép thử dùng tích vô hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Mỗi chỉ số có xác suất $1/D$, nên cộng trên $D-d_H$ chỉ số thuận lợi cho công thức; phép đếm cho giá trị chính xác. Xác suất giảm tuyến tính theo $d_H$, nên $d_H\le d_1$ cho xác suất ít nhất $1-d_1/D$ và $d_H\ge d_2$ cho xác suất nhiều nhất $1-d_2/D$; đó là hai điều kiện của định nghĩa họ nhạy cảm. Họ chỉ có $D$ hàm phân biệt, nhưng điều đó không giới hạn số phép thử: lấy có hoàn lại thì các chỉ số độc lập và công thức $p^r$ của phép AND áp dụng được. Chọn $r$ chỉ số khác nhau không cho công thức $p^r$.
- **Nguồn:** B §3.7.1 tr.109; sửa diễn giải giới hạn số hàm độc lập của nguồn.
- **Ánh xạ ghi chú:** `lec-06-topic-08` (mã cũ `N08`); số hiệu: Mệnh đề 06.29; Nhận xét 06.30. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: thêm dòng Giả thiết; Lưu ý thay câu kết luận. Âm tiết mặt trang 37 → 39.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (toán): miền $0\le d_1<d_2\le D$; ghi chú nêu giới hạn $D$ hàm của MMDS và lấy có hoàn lại; số hiệu 06.28 → 06.29. Âm tiết mặt trang 40 → 40.

#### lec06-s04-03 — Hàm băm dấu theo siêu phẳng

- **Mục đích và vai trò:** Định nghĩa hàm băm dấu theo siêu phẳng qua gốc cho khoảng cách góc và chạy một pháp tuyến trên dữ kiện Ví dụ 3.22.
- **Thông điệp:** Giá trị băm là phía của siêu phẳng chứa vector; chỉ phụ thuộc hướng.
- **Nội dung công khai dự kiến:** Pháp tuyến $v\ne0$ xác định siêu phẳng qua gốc $\{x: v\cdot x=0\}$; hàm băm ghi phía chứa vector: $h_v(x)=\operatorname{sign}(v\cdot x),\qquad \operatorname{sign}(0)=+1$ [Hình: Pháp tuyến vuông góc mặt phân chia, hướng vào nửa không gian có dấu dương.] $x=(3,4,5,6),\ y=(4,3,2,1)$ $v_1=(1,-1,1,1)$ $v_1\cdot x=3-4+5+6=10$ $v_1\cdot y=4-3+2+1=4$ $h_{v_1}(x)=h_{v_1}(y)=+1$: cùng phía siêu phẳng. Giá trị băm chỉ phụ thuộc hướng của $x$, phù hợp khoảng cách góc.
- **Đầu vào và giả thiết:** Tích vô hướng, vector V10 hiển thị đầy đủ; x=(3,4,5,6), y=(4,3,2,1).
- **Dữ kiện, hình thức hóa và vết chạy:** V10, HT9 cơ chế; pháp tuyến vuông góc siêu phẳng, khác đường chia trong hình hai chiều.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn và định nghĩa ở trên; hình pháp tuyến bên trái; phép tính $v_1\cdot x$, $v_1\cdot y$ bên phải; câu chốt về hướng. Năm 2 đã có tích vô hướng từ đại số tuyến tính.
- **Kết nối vào–ra:** Tọa độ đơn→phép thử theo hướng; nhiều pháp tuyến tạo chữ ký dấu.
- **Diễn giải học thuật, lời giải và tiêu chí:** Khoảng cách góc không đổi khi nhân vector với một số dương, nên phép thử phù hợp phải chỉ phụ thuộc hướng. Dấu của $v\cdot x$ có tính chất này: nhân $x$ với $c>0$ không đổi dấu. Pháp tuyến vuông góc với mặt phân chia. Một pháp tuyến $v$ được giữ cố định khi băm mọi vector; quy tắc dấu tại 0 làm hàm xác định. Pháp tuyến $v_1$ lấy từ Ví dụ 3.22 chỉ minh họa phép tính; phân phối của pháp tuyến ngẫu nhiên được nêu cùng chứng minh xác suất.
- **Nguồn:** B §3.7.2–3/Ex 3.22 tr.109–111; S4 PDF 48/trang in 51; hình pháp tuyến.
- **Ánh xạ ghi chú:** `lec-06-topic-09` (mã cũ `N09`); số hiệu: Ví dụ 06.14; Định nghĩa 06.31. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `giữ`: tách khối công thức dài; câu cuối thành Ý nghĩa. Âm tiết mặt trang 38 → 29.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12, B11: thêm Nhu cầu ($\theta(x,2x)=0$), "Ý nghĩa" thành "Trực quan."; "(hyperplane)"; hàm định nghĩa bằng câu "là"; hình thu nhỏ để vừa khung. Âm tiết mặt trang 29 → 45.

#### lec06-s04-05 — Tính nhạy cảm của họ siêu phẳng

- **Mục đích và vai trò:** Chứng minh xác suất cùng dấu $1-\theta/\pi$ dưới pháp tuyến đẳng hướng và nêu bộ tham số nhạy cảm; đặt trước chữ ký dấu vì s04-04 dùng kết quả này.
- **Thông điệp:** Họ siêu phẳng là $(d_1,d_2,1-d_1/\pi,1-d_2/\pi)$-nhạy cảm.
- **Nội dung công khai dự kiến:** $x,y\ne0$ tạo góc $\theta\in[0,\pi]$ (radian); pháp tuyến $v$ đẳng hướng, tức mọi hướng đồng khả năng. [Hình: Hai miền pháp tuyến tách hai vector, tổng góc 2 theta trên vòng tròn 2 pi.] Hai cung hướng tách $x$ và $y$, mỗi cung rộng $\theta$: $\Pr[h_v(x)\ne h_v(y)]=\frac{2\theta}{2\pi}=\frac\theta\pi$ $\Pr[h_v(x)=h_v(y)]=1-\frac\theta\pi$ $\theta=\pi/3\Rightarrow\Pr[h_v(x)=h_v(y)]=2/3$. Với $0\le d_1<d_2\le\pi$, họ siêu phẳng là $(d_1,d_2,1-d_1/\pi,1-d_2/\pi)$-nhạy cảm.
- **Đầu vào và giả thiết:** Khoảng cách góc N05; dấu, pháp tuyến và siêu phẳng.
- **Dữ kiện, hình thức hóa và vết chạy:** HT9; V06 đổi 60° thành $\pi/3$; V10 là phân phối khác được ghi rõ.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu giả thiết; hình hai cung tách bên trái; hai đẳng thức xác suất và ví dụ $\pi/3$ bên phải; câu chốt bộ tham số. Năm 2 thấy tỷ phần góc trước công thức; chứng minh chiếu về mặt phẳng ở ghi chú.
- **Kết nối vào–ra:** Hàm băm dấu ở s04-03 → xác suất va chạm và bộ tham số; quan hệ $p_{\ne}=\theta/\pi$ cho quy tắc ước lượng góc ở s04-04.
- **Diễn giải học thuật, lời giải và tiêu chí:** Khi $0<\theta<\pi$, hai vector sinh một mặt phẳng và dấu của $v\cdot x$, $v\cdot y$ chỉ phụ thuộc hình chiếu của $v$ lên mặt phẳng đó. Tính đẳng hướng làm hướng của hình chiếu phân phối đều trên vòng tròn; hình chiếu bằng 0 có xác suất 0. Hai dấu khác nhau đúng khi hướng chiếu rơi vào một trong hai cung rộng $\theta$. Hai trường hợp biên khớp công thức: $\theta=0$ cho cùng dấu với xác suất 1, $\theta=\pi$ cho khác dấu với xác suất 1 vì tích vô hướng bằng 0 có xác suất 0. Góc phải đo bằng radian; thay số độ vào $1-\theta/\pi$ cho kết quả sai. MMDS viết cùng bộ tham số theo độ: $(180-d)/180$.
- **Nguồn:** B §3.7.2/Hình 3.13 tr.109–110; S4 PDF 49/trang in 52.
- **Ánh xạ ghi chú:** `lec-06-topic-09` (mã cũ `N09`); số hiệu: Định lý 06.32. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `giữ`: thêm nhãn Giả thiết và số hiệu. Âm tiết mặt trang 32 → 28.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11, nhẹ: "(isotropic)"; ví dụ nêu cặp $(1,2,-1)$, $(2,1,1)$; số hiệu 06.31 → 06.32. Âm tiết mặt trang 29 → 32.

#### lec06-s04-04 — Ví dụ: chữ ký dấu của hai vector, ba pháp tuyến

- **Mục đích và vai trò:** Ghép $m$ hàm dấu thành chữ ký và áp quy tắc $\widehat\theta=\pi\widehat p_{\ne}$ trên Ví dụ 3.22; phân biệt sai lệch do mẫu nhỏ và do pháp tuyến không đẳng hướng.
- **Thông điệp:** Quy tắc ước lượng chỉ có bảo đảm khi pháp tuyến đẳng hướng và đủ nhiều; ba pháp tuyến dấu $\pm1$ cho $120^\circ$ so với góc thật $38{,}05^\circ$.
- **Nội dung công khai dự kiến:** $m$ pháp tuyến cho chữ ký $m$ bit; xác suất khác dấu là $p_{\ne}=\Pr[h_v(x)\ne h_v(y)]=\theta/\pi$. Quy tắc ước lượng: $\widehat\theta=\pi\widehat p_{\ne}$, với $\widehat p_{\ne}$ là tỷ lệ bit khác. Pháp tuyến $v_i\cdot x$ $v_i\cdot y$ Dấu của $x$, $y$ $v_1=(1,-1,1,1)$ 10 4 +, + $v_2=(-1,1,-1,1)$ 2 −2 +, − $v_3=(1,1,-1,-1)$ −4 4 −, + $\widehat p_{\ne}=\frac23,\qquad\widehat\theta=\pi\cdot\frac23=120^\circ,\qquad\theta\approx38{,}05^\circ$ Ba pháp tuyến dấu $\pm1$ cố định chỉ minh họa phép tính; chúng không có phân phối đẳng hướng. Ước lượng lệch xa góc thật vì chỉ có ba bit và pháp tuyến không đẳng hướng.
- **Đầu vào và giả thiết:** Hàm dấu (s04-03) và quan hệ $p_{\ne}=\theta/\pi$ dưới pháp tuyến đẳng hướng (s04-05). Ba pháp tuyến dấu trong bảng là dữ kiện cố định của Ví dụ 3.22.
- **Dữ kiện, hình thức hóa và vết chạy:** V10; $x\cdot y=40$, chuẩn bình phương 86 và 30. Ba pháp tuyến là mẫu cố định dấu ±1.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu chữ ký và quy tắc ước lượng; bảng ba pháp tuyến với hai tích và hai dấu; dòng công thức ước lượng và góc thật; dòng phụ và câu chốt về hai nguồn sai lệch. Góc thật bằng arccos và trường hợp 16 pháp tuyến vào ghi chú.
- **Kết nối vào–ra:** Quan hệ $p_{\ne}=\theta/\pi$ đã chứng minh ở s04-05 → quy tắc ước lượng; giới hạn của ví dụ dẫn sang họ cho khoảng cách Euclid ở s04-06.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chữ ký dấu thay xác suất khác dấu bằng tỷ lệ bit khác quan sát được trên $m$ pháp tuyến độc lập. Góc thật: $x\cdot y=40$, $\|x\|_2^2=86$, $\|y\|_2^2=30$, nên $\theta=\arccos(40/\sqrt{2580})\approx38{,}047579^\circ$. Có hai nguồn sai lệch tách biệt. Mẫu ba bit có phương sai lớn. Ngay cả khi dùng đủ 16 vector dấu $\pm1$ trong bốn chiều với quy tắc dấu tại 0 đã nêu, chỉ 4 vector cho hai dấu khác nhau, nên ước lượng là $45^\circ$, vẫn khác góc thật; đó là sai lệch do phân phối không đẳng hướng.
- **Nguồn:** B §3.7.3/Ex 3.22 tr.111/PDF 40.
- **Ánh xạ ghi chú:** `lec-06-topic-09` (mã cũ `N09`); số hiệu: Ví dụ 06.15. **Thời lượng:** 1,5 phút (trước 2 phút; lượt sửa deck chuyển 0,5 phút cho s04-14).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 66 âm tiết; ví dụ giữ ở trang này, quy tắc ước lượng sang s04-12. Âm tiết mặt trang 66 → 31. Tiêu đề cũ: “Chữ ký dấu và ước lượng góc”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: nửa câu định nghĩa "chữ ký dấu (sketch)" trước khi dùng; thời lượng 2 → 1,5 phút. Âm tiết mặt trang 31 → 41.

#### lec06-s04-12 — Ước lượng góc từ chữ ký dấu

- **Mạch và mục đích:** Mạch 4, thuật toán. Quy tắc ước lượng góc từ chữ ký dấu và đối chiếu với ví dụ.
- **Thao tác của sinh viên:** Đổi tỷ lệ bit khác $2/3$ thành $\widehat\theta=120^\circ$, so với $38{,}05^\circ$.
- **Đối tượng trung tâm:** $\widehat\theta=\pi\widehat p_{\ne}$.
- **Dữ kiện và ký hiệu kế thừa:** Định lý 06.32 (s04-05); chữ ký dấu của ví dụ s04-04.
- **Kiến thức đầu vào:** Tỷ lệ, góc radian.
- **Sản phẩm học tập:** Quy tắc ước lượng và hai nguồn sai lệch (ít bit, phân phối không đẳng hướng).
- **Bằng chứng kiểm tra:** Bài 3.7.2 (s07-05); Bài tập 06.24.
- **Kết nối vào–ra:** Vào: ví dụ ba pháp tuyến. Ra: độ lớn bị bỏ qua dẫn tới họ chiếu s04-06.
- **Nguồn:** MMDS §3.7.3, Ví dụ 3.22, tr.110–111.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: phần thứ hai tách từ s04-04; nhãn "Quy tắc:" đổi thành "Thuật toán." theo quyết định điều phối viên. Âm tiết mặt trang — → 42.
- **Ánh xạ ghi chú:** `lec-06-topic-09`; số hiệu: Thuật toán 06.33. **Thời lượng:** 1 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (toán, chuyên gia): nhãn "Quy tắc ước lượng."; "$2\pi/3$, tức $120^\circ$"; ghi chú thêm độ lệch chuẩn $\pi\sqrt{p(1-p)/m}$ (khoảng $42^\circ$ với $m=3$) và quan hệ $m$ với $n$; số hiệu 06.32 → 06.33. Âm tiết mặt trang 43 → 46.

#### lec06-s04-06 — Ví dụ: ba điểm trên trục thứ nhất

- **Mục đích và vai trò:** Mở cụm Euclid: nêu vì sao cần giữ độ lớn tọa độ chiếu và chạy phép chia khoảng trên trục cố định của Bài 3.7.5.
- **Thông điệp:** Mã là chỉ số khoảng rộng $a$ chứa tọa độ chiếu; trục cố định có biên cố định có thể tách cặp gần.
- **Nội dung công khai dự kiến:** Khoảng cách Euclid phụ thuộc độ lớn, nên phép băm giữ tọa độ chiếu thay vì chỉ giữ dấu: chia trục thành các khoảng rộng $a$ và trả chỉ số khoảng. $z_1=(1,2,3),\ z_2=(0,2,4),\ z_3=(4,3,2)$; trục thứ nhất, $a=1$; mã là phần nguyên của tọa độ thứ nhất chia cho $a$. Điểm Tọa độ chiếu Khoảng chứa Mã $z_1$ 1 $[1,2)$ 1 $z_2$ 0 $[0,1)$ 0 $z_3$ 4 $[4,5)$ 4 Ba mã khác nhau nên trục này chưa tạo cặp; khoảng đóng bên trái, mở bên phải.
- **Đầu vào và giả thiết:** Chuẩn Euclid, phép chiếu và hàm sàn.
- **Dữ kiện, hình thức hóa và vết chạy:** Bài 3.7.5 giữ dữ kiện; chỉ minh họa một trục, a=1. Chưa giải hai trục khác/a=2.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu nhu cầu giữ độ lớn; dòng dữ kiện; bảng điểm/tọa độ chiếu/khoảng/mã; câu chốt. Năm 2 thấy điểm đúng biên thuộc khoảng nào; ghi chú phân biệt trục cố định với hướng ngẫu nhiên.
- **Kết nối vào–ra:** Góc bỏ độ dài→lượng tử hóa hình chiếu; biên khoảng đòi đặc tả dịch ngẫu nhiên.
- **Diễn giải học thuật, lời giải và tiêu chí:** Hàm dấu chỉ giữ phía của siêu phẳng nên mất thông tin độ lớn; hai điểm cùng hướng nhưng cách xa vẫn cùng dấu. Chiếu lên một trục rồi chia khoảng giữ được độ lớn của hiệu hình chiếu. Bài 3.7.5 ký hiệu ba điểm là $p_1,p_2,p_3$; tài liệu đổi thành $z_1,z_2,z_3$ để không trùng với hai cận xác suất $p_1,p_2$ của họ nhạy cảm. Đây là thực thi trên trục cố định của bài tập nguồn, không là bảo đảm xác suất của họ hướng ngẫu nhiên. Với trục cố định, hai điểm rất gần nhưng nằm hai phía một biên luôn bị tách; điều này dẫn tới phép dịch ngẫu nhiên.
- **Nguồn:** B §3.7.4 tr.111–113; Bài 3.7.5(a) tr.114/PDF 43, phần minh họa đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-10` (mã cũ `N10`); số hiệu: Ví dụ 06.16. **Thời lượng:** 1,5 phút (trước 2 phút; lượt sửa deck chuyển 0,5 phút cho s04-14).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu; tách câu dài. Âm tiết mặt trang 78 → 38. Tiêu đề cũ: “Chia trục chiếu thành khoảng”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B7, B18: "mã thùng"; ghi chú: hàm cùng dạng trong $\mathbb R^3$, $u=e_1$, $\delta=0$; thời lượng 2 → 1,5 phút. Âm tiết mặt trang 38 → 48.

#### lec06-s04-07 — Họ chiếu có dịch ngẫu nhiên

- **Mục đích và vai trò:** Định nghĩa họ chiếu có dịch ngẫu nhiên cho khoảng cách Euclid trong mặt phẳng, xuất phát từ hạn chế của biên cố định ở s04-06.
- **Thông điệp:** Dịch đều của biên khoảng cho xác suất theo khoảng cách hình chiếu.
- **Nội dung công khai dự kiến:** Biên cố định luôn tách hai điểm gần nằm hai phía biên; họ chiếu chọn ngẫu nhiên cả hướng chiếu và vị trí biên. [Hình: Trục hình chiếu chia khoảng độ rộng a, biên ka trừ delta; hai hình chiếu có khoảng cách ell.] Trong $\mathbb R^2$: $u$ là hướng đơn vị chọn đều; $a>0$. $\delta$ chọn đều trên $[0,a)$, độc lập với $u$. $h_{u,\delta}(x)=\left\lfloor\frac{u\cdot x+\delta}{a}\right\rfloor$ Mã $k$ ứng với khoảng $[ka-\delta,(k+1)a-\delta)$ trên trục $u$; cùng $(u,\delta)$ cho mọi điểm.
- **Đầu vào và giả thiết:** Phép chiếu chia khoảng, hàm sàn; nguồn ngẫu nhiên của họ.
- **Dữ kiện, hình thức hóa và vết chạy:** HT10; u, hướng; δ, dịch; a, độ rộng; D=2. Không dùng t cho dịch.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hình trục chiếu với biên dịch ở trên 60%; công thức và ba tham số dưới 40%. Năm 2 phân biệt đổi hướng với dời lưới; phần attribution Datar ở notes, không đưa p-stable.
- **Kết nối vào–ra:** Thực thi một trục→họ ngẫu nhiên; cố định hướng để tính xác suất theo dịch.
- **Diễn giải học thuật, lời giải và tiêu chí:** Trục cố định ở trang trước là trường hợp $u$ bằng một vector cơ sở và $\delta=0$. Hàm chiếu áp dụng được ở mọi số chiều; chỉ phần chứng minh cận dùng hai chiều. Chọn $\delta$ đều làm vị trí biên trên trục không ưu tiên điểm nào, nên một cặp gần chỉ bị tách với xác suất nhỏ. Hàm vẫn dùng chung một cặp $(u,\delta)$ cho mọi điểm; nếu mỗi điểm có phép dịch riêng thì so mã không còn ý nghĩa. Công thức lượng tử hóa với dịch đều đối chiếu Datar §3.2; hướng đơn vị đều trong mặt phẳng và cận hai chiều theo mô hình MMDS.
- **Nguồn:** B §3.7.4 tr.111–113; D §3.2PDF 3; bổ sung đã được điều phối viên duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-10` (mã cũ `N10`); số hiệu: Định nghĩa 06.34. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: câu mở thành Nhu cầu; câu cuối thành Lưu ý. Âm tiết mặt trang 57 → 37.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B7, trung bình (sư phạm): định nghĩa trên $\mathbb R^D$ với $u$ đều trên mặt cầu đơn vị; Nhu cầu có ví dụ cực đoan $0{,}99$ và $1{,}01$; ghi chú: cận chỉ cho $D=2$, MMDS không có độ dịch. Âm tiết mặt trang 37 → 46.

#### lec06-s04-08 — Xác suất chung thùng khi cố định hướng

- **Mục đích và vai trò:** Tính xác suất theo dịch bằng độ dài phần biên chia cặp.
- **Thông điệp:** Khoảng cách hình chiếu quyết định phần dịch làm hai điểm khác thùng.
- **Nội dung công khai dự kiến:** Cố định $u$; đặt $\ell=|u\cdot(x-y)|$ là khoảng cách giữa hai hình chiếu. Chỉ $\delta$ còn ngẫu nhiên. $0\le\ell<a$ Trong một chu kỳ dài $a$, các vị trí biên nằm giữa hai hình chiếu chiếm độ dài $\ell$; khi đó hai điểm khác thùng. $\ell\ge a$ Hai hình chiếu không thể cùng nằm trong một khoảng nửa mở rộng $a$. $\Pr_\delta[h(x)=h(y)\mid u]=\max(0,\,1-\ell/a)$ Hình chiếu càng gần, xác suất chung thùng càng lớn; còn phải lấy trung bình theo $u$.
- **Đầu vào và giả thiết:** HT10, phân phối đều của $\delta$, độ dài chu kỳ.
- **Dữ kiện, hình thức hóa và vết chạy:** Trường hợp $\ell=0$ cho 1; $\ell\ge a$ cho 0; chiều dài không âm. Không tự thêm dữ kiện thực nghiệm.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn cố định $u$ và định nghĩa $\ell$; hai thẻ cho hai trường hợp $\ell<a$ và $\ell\ge a$; công thức chung $\max(0,1-\ell/a)$; câu chốt nối sang bước lấy trung bình theo $u$.
- **Kết nối vào–ra:** Đặc tả ngẫu nhiên→xác suất có điều kiện; cận chiếu nối tới khoảng cách Euclid.
- **Diễn giải học thuật, lời giải và tiêu chí:** Vì $\delta$ đều trên $[0,a)$, vị trí biên modulo $a$ đều trên một chu kỳ. Khi $0<\ell<a$, hai điểm khác thùng đúng khi một biên rơi giữa hai hình chiếu, với xác suất $\ell/a$; điểm biên có xác suất 0. Khi $\ell=0$, hai hình chiếu trùng nhau nên luôn chung thùng, khớp công thức. Khi $\ell\ge a$, xác suất bằng 0. Kết quả mới có điều kiện theo $u$. Bước tiếp theo dùng quan hệ $\ell\le\|x-y\|_2$ và phân phối của hướng để chuyển sang cận theo khoảng cách Euclid.
- **Nguồn:** B §3.7.4; điều kiện dịch từ D §3.2; chứng minh hình học của bản soạn, đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-10` (mã cũ `N10`); số hiệu: Bổ đề 06.35. **Thời lượng:** 1 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 77 âm tiết; phát biểu bổ đề ở trang này, chứng minh hai trường hợp sang s04-13. Âm tiết mặt trang 77 → 28.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: số hiệu Bổ đề 06.34 → 06.35. Âm tiết mặt trang 29 → 29.

#### lec06-s04-13 — Chứng minh: xác suất chung thùng khi cố định hướng

- **Mạch và mục đích:** Mạch 4, kết quả. Chứng minh hai trường hợp của Bổ đề 06.35.
- **Thao tác của sinh viên:** Tính độ dài đoạn biên làm hai điểm khác thùng; gộp hai trường hợp.
- **Đối tượng trung tâm:** $\max(0,1-\ell/a)$.
- **Dữ kiện và ký hiệu kế thừa:** Định nghĩa họ chiếu có dịch s04-07; phát biểu bổ đề s04-08.
- **Kiến thức đầu vào:** Phân phối đều trên một đoạn.
- **Sản phẩm học tập:** Chứng minh có hai trường hợp, nêu bước dùng dịch đều.
- **Bằng chứng kiểm tra:** Câu 3 của s04-11; Bài tập 06.10(a,b).
- **Kết nối vào–ra:** Vào: s04-08. Ra: định lý họ chiếu hai chiều s04-09 lấy trung bình theo $u$.
- **Nguồn:** MMDS §3.7.4, tr.112; Datar và cộng sự §3.2.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: phần chứng minh tách từ s04-08. Âm tiết mặt trang — → 44.
- **Ánh xạ ghi chú:** `lec-06-topic-10`; số hiệu: Bổ đề 06.35. **Thời lượng:** 2 phút.

#### lec06-s04-09 — Tính nhạy cảm của họ chiếu hai chiều

- **Mục đích và vai trò:** Suy hai cận với đúng miền hai chiều.
- **Thông điệp:** Họ chiếu trong $\mathbb R^2$ là $(a/2,2a,1/2,1/3)$-nhạy cảm; hằng số $1/3$ chỉ đúng cho hai chiều.
- **Nội dung công khai dự kiến:** $\rho=\|x-y\|_2$; $P=\Pr[h(x)=h(y)]$ là trung bình theo $u$ của $\max(0,1-\ell/a)$. [Hình: Đoạn nối hai điểm dài rho tạo góc nhọn phi với trục u; hình chiếu dài ell bằng rho nhân trị tuyệt đối cos phi.] Cặp gần, $\rho\le a/2$ $\ell\le\rho\ \Rightarrow\ P\ge1-\rho/a\ge1/2$ Cặp xa, $\rho\ge2a$ $\phi$: góc nhọn giữa $x-y$ và trục chiếu. Chung thùng cần $\ell=\rho|\cos\phi|<a$: $|\cos\phi|<a/\rho\le\tfrac12\ \Rightarrow\ \phi>\tfrac\pi3$ $u$ đều trong $\mathbb R^2$ nên $\phi$ đều trên $[0,\pi/2]$: $P\le\frac{\pi/2-\pi/3}{\pi/2}=1/3$ Họ chiếu trong $\mathbb R^2$ là $(a/2,\,2a,\,1/2,\,1/3)$-nhạy cảm.
- **Đầu vào và giả thiết:** Công thức va chạm theo độ dài chiếu ell ở s04-08; u đều trong mặt phẳng và delta đều độc lập. Quan hệ ell=rho|cos phi| được thiết lập trực tiếp trên trang này.
- **Dữ kiện, hình thức hóa và vết chạy:** Hình tam giác nối rho, ell và phi. Gần dùng ell≤rho. Xa cần ell<a; rho≥2a suy |cos phi|<1/2 và phi>pi/3, rồi chặn bằng tỷ lệ miền góc đều. Không dùng điều kiện cần như điều kiện đủ.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Hai cột: trái là SVG hinh-chieu-euclid.svg và cận gần; phải là chuỗi cận xa. Hình ghi rho, ell, phi, trục u, đường vuông góc nét đứt; không ấn định tỷ lệ rho với độ rộng a. Nhãn font 32–38 trong viewBox 610×335; giữ thang chữ chung.
- **Kết nối vào–ra:** Xác suất theo $\ell$→bảo đảm theo $\rho$; cùng khung họ cho phép so chi phí ba phép thử.
- **Diễn giải học thuật, lời giải và tiêu chí:** Cận gần đúng với mọi hướng nên vẫn đúng sau khi lấy trung bình theo $u$. Với cặp xa, điều kiện $\phi>\pi/3$ là cần nhưng chưa đủ để chung thùng, nên kết quả là cận trên. Hình tam giác chỉ biểu diễn quan hệ chiếu; nó không đặt tỷ lệ cố định giữa $\rho$ và $a$. Tính đều của góc nhọn dùng đúng hai chiều; trong số chiều lớn hơn, hướng ngẫu nhiên tập trung gần vuông góc với $x-y$, nên hằng số $1/3$ không chuyển sang mọi chiều. Giống các họ trước, độ chênh giữa $1/2$ và $1/3$ được khuếch đại bằng AND và OR.
- **Nguồn:** B §3.7.4 tr.112–113/Hình 3.14; S4 PDF 57–58; giả thiết và proof bổ sung đã duyệt.
- **Ánh xạ ghi chú:** `lec-06-topic-10` (mã cũ `N10`); số hiệu: Định lý 06.36; Nhận xét 06.37. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bố cục còn sáu dòng, một khối công thức; thêm số hiệu. Âm tiết mặt trang 37 → 38.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12, B15, nhẹ: "Định lý." lên đầu trang, chứng minh theo thứ tự cặp gần → cặp xa; công thức nội dòng bọc ngoặc; "tức" → "nên"; ghi chú: cận xa không cần dịch đều, nhận xét định tính §3.7.5; số hiệu 06.35 → 06.36. Âm tiết mặt trang 39 → 43.

#### lec06-s04-10 — Chi phí: chữ ký theo ba họ

- **Mục đích và vai trò:** Đếm phép tính và tham số lưu của một hàm trong ba họ trước khi viết tiệm cận; tách chi phí tính chữ ký khỏi chi phí phân dải đã có ở phần 2.
- **Thông điệp:** Chi phí mỗi phép thử phụ thuộc lượng tọa độ được đọc.
- **Nội dung công khai dự kiến:** Mô hình: vector đặc $D$ chiều, mỗi số một từ máy, mỗi phép đọc, nhân, cộng tốn thời gian hằng. Họ Phép tính của một hàm Thời gian Tham số lưu Chọn tọa độ 1 lần đọc $O(1)$ 1 chỉ số Siêu phẳng $D$ nhân, $D-1$ cộng, 1 so sánh $O(D)$ $D$ từ Chiếu có dịch $D$ nhân, $D$ cộng, 1 chia, 1 lấy sàn $O(D)$ $D+1$ từ Chữ ký $m$ hàm cho $C$ vector: $C\cdot m$ lần tính, tức $O(Cm)$ với họ chọn tọa độ và $O(CmD)$ với hai họ còn lại. Đây là chi phí tính chữ ký; dựng thùng, phát $Q$ cặp và xác minh $K$ cặp tính như ở phần 2.
- **Đầu vào và giả thiết:** Các hàm cơ sở và mô hình chi phí N04.
- **Dữ kiện, hình thức hóa và vết chạy:** Suy đếm trực tiếp từ $h_I$, $h_u$, $h_{u,\delta}$; vector đặc là điều kiện. Không gán $O(1)$ cho tích vô hướng $D$ chiều.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu mô hình chi phí; bảng 4 cột (họ, phép tính của một hàm, thời gian, tham số lưu) cho ba họ; dòng tổng $C\cdot m$ lần tính; câu chốt nối với $Q$, $K$ của phần 2.
- **Kết nối vào–ra:** Các bảo đảm→chi phí thực hiện; kiểm tra phần yêu cầu giữ đúng giả thiết.
- **Diễn giải học thuật, lời giải và tiêu chí:** Các số trong bảng là phép đếm từ định nghĩa hàm, không phải số đo. Bộ nhớ gồm hai phần: tham số của $m$ hàm, là $m$ chỉ số hoặc $O(mD)$ từ, dùng chung cho cả kho; và chữ ký, $m$ giá trị cho mỗi vector. Chữ ký dấu chỉ cần $m$ bit cho mỗi vector, chữ ký chiếu cần $m$ số nguyên. Với vector thưa có $\mathrm{nnz}(x)$ thành phần khác 0, tích vô hướng chỉ cần duyệt $\mathrm{nnz}(x)$ thành phần, nên $D$ trong bảng được thay bằng $\mathrm{nnz}(x)$. Sau khi có chữ ký, phân dải dùng lại đúng thuật toán của phần 2 với $n=br$ hàm.
- **Nguồn:** B §3.7.1–4 tr.109–113; suy chi phí từ công thức nguồn.
- **Ánh xạ ghi chú:** `lec-06-topic-17` (mã cũ `N08,N09,N10`); số hiệu: Mệnh đề 06.38. **Thời lượng:** 1,5 phút (trước 1.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: 102 âm tiết; bảng đổi về khuôn Bước, Số lần, Chi phí mỗi lần, Đóng góp; chi tiết phép tính sang ghi chú. Âm tiết mặt trang 102 → 69. Tiêu đề cũ: “Chi phí tính chữ ký theo họ băm”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B12, C: cột "Phép tính mỗi lần" ghi số phép tính trước $O(\cdot)$; dòng tổng; ghi chú nêu $m$ đóng vai $n$; số hiệu 06.37 → 06.38. Âm tiết mặt trang 70 → 76.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình, nhẹ (rà lại mạch): kết luận dẫn thuật toán tổng quát và nêu $m=br$. Âm tiết mặt trang 76 → 76.

#### lec06-s04-11 — Câu hỏi về các họ theo độ đo

- **Mục đích và vai trò:** Kiểm tra phần 4 bằng dữ kiện mới: họ chọn tọa độ kèm AND 2, góc $3\pi/4$ cho họ siêu phẳng, xác suất có điều kiện và cận hai chiều của họ chiếu.
- **Thông điệp:** Mỗi công thức va chạm gắn với một phép lấy mẫu cụ thể.
- **Nội dung công khai dự kiến:** Câu hỏi: Với $x=11001$ và $y=10011$, tính xác suất trùng của một hàm chọn tọa độ và của AND 2 với chỉ số độc lập. Tính xác suất cùng dấu của $x=(1,0)$ và $y=(-1,1)$ dưới pháp tuyến đẳng hướng. Với $a=2$ và $u$ cố định, hai hình chiếu cách nhau $\ell=0{,}5$: tính xác suất chung thùng theo $\delta$. Xác định cận xác suất của cặp có $\|x-y\|_2=5$ trong $\mathbb R^2$.
- **Đầu vào và giả thiết:** Bộ tham số của ba họ (s04-02, s04-05, s04-09) và xác suất có điều kiện của họ chiếu (s04-08); dữ kiện luyện tập mới, không trùng các ví dụ đã giải.
- **Dữ kiện, hình thức hóa và vết chạy:** Đáp án 2/5;60°=π/3→2/3; u đều hai chiều, δ đều độc lập. Không giải thêm V11 các trục còn lại.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba nhiệm vụ một cột, rộng 90%; dữ kiện tách dòng công thức. Năm 2 kiểm không chỉ phép thế mà cả điều kiện; đáp án giữ ở notes.
- **Kết nối vào–ra:** Chi phí/họ→kiểm tra; ứng dụng sẽ chọn lại biểu diễn và quy tắc sinh cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: hai vector khác tại vị trí 2 và 4, nên $d_H=2$, xác suất trùng $1-2/5=3/5$; AND 2 cho $(3/5)^2=9/25=0{,}36$ khi hai chỉ số lấy độc lập, có hoàn lại. Câu 2: $x\cdot y=-1$, $\|x\|_2=1$, $\|y\|_2=\sqrt2$, nên $\cos\theta=-1/\sqrt2$, $\theta=3\pi/4$; xác suất cùng dấu $1-3/4=1/4$. Câu 3: $1-0{,}5/2=0{,}75$; vì $5\ge2a=4$ nên cặp là cặp xa và xác suất chung thùng không quá $1/3$, với $u$ đều trong mặt phẳng và $\delta$ đều độc lập. Tiêu chí: đếm đúng $d_H$ và nêu điều kiện độc lập; đổi góc sang radian trước khi dùng $1-\theta/\pi$; phân biệt xác suất có điều kiện theo $u$ với cận sau khi lấy trung bình theo $u$.
- **Nguồn:** B Ex 3.17, Ex 3.14, §3.7.1–4; kiểm trực tiếp dữ kiện/giả thiết đã học.
- **Ánh xạ ghi chú:** `lec-06-topic-08, lec-06-topic-09, lec-06-topic-10` (mã cũ `N08,N09,N10`); số hiệu: Bài tập 06.8–06.10. **Thời lượng:** 2,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tách câu 3 thành hai câu ngắn. Âm tiết mặt trang 68 → 50. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B16, B7: câu 4 ghi $a=2$ và $u$ đều; ghi chú: cận xa đúng với mọi $\delta$. Âm tiết mặt trang 51 → 58.

### Mạch 5. Ứng dụng tìm cặp tương đồng

#### lec06-s05-00 — 5. Ứng dụng tìm cặp tương đồng

- **Mạch và vị trí:** điểm vào mạch 5; trang tiêu đề mạch `section.strand-title`, `id="mach-5"`, mở tại `#/5`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 5 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Khung biểu diễn, họ, ghép, thùng, xác minh.
- **Sản phẩm giao cho mạch sau:** xác suất mô hình vân tay; giới hạn của hàm khóa cố định.
- **Vai trò chu trình:** ngoài chu trình khái niệm (ba ứng dụng có Nhu cầu riêng).
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/5` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 36 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-11`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B4, C: ghi chú mở bằng quan hệ với các họ theo độ đo, bỏ "giao cho mạch sau"; 95 âm tiết. Âm tiết mặt trang 36 → 36.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): ghi chú nêu OR 1024 là thuật toán tổng quát với họ hàm ba ô, $r=1$, $b=1024$. Âm tiết mặt trang 36 → 36.

#### lec06-s05-01 — Đối sánh thực thể

- **Mục đích và vai trò:** Mở phần 5: nhận ra phép OR của ba hàm khóa (phân dải $b=3$, $r=1$) trong bài toán đối sánh thực thể và hệ quả bỏ sót.
- **Thông điệp:** Khớp một trường tạo cặp cần xét, chưa xác nhận cùng người.
- **Nội dung công khai dự kiến:** Tìm cặp hồ sơ cùng một người giữa hai nguồn, mỗi nguồn $10^6$ hồ sơ: chấm điểm mọi cặp cần $10^{12}$ lần. [Hình: Khớp tên, địa chỉ hoặc điện thoại sinh ứng viên; hợp cặp trước khi chấm điểm và xác minh.] Ba hàm khóa: tên, địa chỉ, điện thoại trùng hoàn toàn. Cặp thành ứng viên khi trùng ít nhất một khóa, tức OR của ba hàm. Chỉ ứng viên được chấm điểm; cặp không trùng hoàn toàn khóa nào bị bỏ sót.
- **Đầu vào và giả thiết:** OR, khử lặp, xác minh; không giả định ba trường độc lập xác suất.
- **Dữ kiện, hình thức hóa và vết chạy:** B §3.8: quy mô và tên trường nguồn; không tự tạo hồ sơ người. Mô hình điểm/ngày chỉ đọc thêm.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ hai nguồn→ba nhánh khóa→hợp ứng viên→chấm điểm chiếm 75%; câu giới hạn dưới. Năm 2 nhận cấu trúc OR đã biết trong miền mới; không đưa bảng hồ sơ tự đặt.
- **Kết nối vào–ra:** Họ cơ sở→ứng dụng có quy tắc khớp riêng; vân tay cung cấp mô hình xác suất cụ thể.
- **Diễn giải học thuật, lời giải và tiêu chí:** Ba hàm khóa đóng vai trò ba dải, mỗi dải một hàm: phân dải với $b=3$, $r=1$. Trong ví dụ của sách, thay cho bảng băm, hồ sơ được sắp lần lượt theo tên, địa chỉ, điện thoại và chỉ các hồ sơ liền nhau có cùng khóa được chấm điểm; kết quả như dùng bảng băm. Điểm của một cặp là 100 cho mỗi trường, trừ điểm phạt tăng theo bình phương khoảng cách chỉnh sửa, có hiệu chỉnh bằng bảng tên tương đương như Bill và William. Khớp một khóa chưa đủ kết luận cùng người, vì nhiều người có thể chung địa chỉ hoặc điện thoại. Ngưỡng điểm được kiểm bằng trường ngày tạo hồ sơ, không tham gia điểm; cách kiểm này ở mục Đọc thêm. Chưa có phân phối của các trường nên chưa gán được bốn tham số của họ nhạy cảm.
- **Nguồn:** B §3.8.1–3 tr.114–117/PDF 43–46.
- **Ánh xạ ghi chú:** `lec-06-topic-11` (mã cũ `N11`); số hiệu: Định nghĩa 06.39; Nhận xét 06.40; Tình huống 06.1. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu; tách câu dài; Kết luận một câu. Âm tiết mặt trang 69 → 52.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B10, B11: OR trên ba hàm cố định, không áp được $1-(1-p)^b$; "(entity resolution)"; ghi chú ghi chu trình rút gọn. Âm tiết mặt trang 52 → 60.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: dấu chấm thừa trong ghi chú. Âm tiết mặt trang 60 → 60.

#### lec06-s05-02 — Họ băm ba ô cho vân tay

- **Mục đích và vai trò:** Định nghĩa biểu diễn vân tay bằng tập ô và họ băm ba ô; nêu vì sao MMDS không dùng MinHash ở đây.
- **Thông điệp:** Chỉ ảnh chứa đặc trưng ở cả ba ô mới vào thùng chung.
- **Nội dung công khai dự kiến:** Ảnh vân tay đã chuẩn hóa kích thước và hướng được biểu diễn bằng tập ô lưới chứa điểm đặc trưng, tức nơi đường vân kết thúc hoặc nhập vào nhau. [Hình: Ba ô được chọn trước khi xét ảnh; ảnh có đủ ba ô vào thùng chung, mỗi ảnh thiếu ô có thùng riêng.] Mỗi hàm $f$ ứng với ba ô chọn ngẫu nhiên trước khi xét ảnh. Ảnh có điểm đặc trưng ở cả ba ô vào thùng chung của $f$. Mỗi ảnh còn lại vào một thùng đơn riêng. Hai ảnh va chạm theo $f$ khi cả hai có điểm đặc trưng ở đủ ba ô.
- **Đầu vào và giả thiết:** Đặc trưng vân tay là nơi đường vân kết thúc hoặc nhập vào nhau; chuẩn hóa kích thước và hướng trước biểu diễn bằng tập ô. Không giả định sinh viên biết xử lý ảnh.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; lưới chỉ là sơ đồ khái niệm, không là dữ liệu ảnh thực. Singleton cho ảnh thiếu ô bảo đảm không va chạm với nhau.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Lưới ba ô đánh dấu bằng số/viền trái 50%; quy tắc hai nhánh thùng chung/thùng đơn phải 50%. Năm 2 tránh nhầm “không đạt” là một thùng 0 chung; không dùng ảnh raster.
- **Kết nối vào–ra:** Ứng dụng thực thể thiếu mô hình xác suất → họ vân tay có mô hình cụ thể; các giả thiết $0{,}2$ và $0{,}8$ cho xác suất va chạm ở s05-03.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tập ô có thể so bằng Jaccard, nhưng lưới chỉ khoảng 1000 ô nên tập đã nhỏ; MMDS dùng một họ khác thay vì rút gọn bằng MinHash. Chuẩn hóa kích thước và hướng làm cùng một ô có ý nghĩa so sánh giữa các ảnh. Có hai bài toán: một–nhiều, so một ảnh truy vấn với cả kho; nhiều–nhiều, tìm mọi cặp trong kho. Với bài toán thứ nhất, các thùng của nhiều hàm được dựng trước và ảnh truy vấn chỉ được so với ảnh trong các thùng chứa nó. Nếu gom mọi ảnh thiếu ô vào cùng một thùng, chúng sẽ va chạm với nhau và xác suất va chạm khác mô hình $q_T$, $q_F$.
- **Nguồn:** B §3.8.4–5 tr.117–118/PDF 46–47.
- **Ánh xạ ghi chú:** `lec-06-topic-12` (mã cũ `N12`); số hiệu: Định nghĩa 06.41. **Thời lượng:** 2 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng Nhu cầu; câu 31 âm tiết chuyển sang ghi chú. Âm tiết mặt trang 86 → 59.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ: "(minutia)". Âm tiết mặt trang 59 → 60.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ (rà lại mạch): ghi chú nêu hàm ba ô chọn ngẫu nhiên, khác ba hàm khóa cố định. Âm tiết mặt trang 60 → 60.

#### lec06-s05-03 — Ví dụ: xác suất va chạm của hàm ba ô

- **Mục đích và vai trò:** Tính $q_F$, $q_T$ của một hàm ba ô theo mô hình MMDS và cho thấy một hàm chưa đủ, dẫn tới phép ghép ở trang sau.
- **Thông điệp:** Mô hình xác suất cho hai xác suất cơ sở khác nhau.
- **Nội dung công khai dự kiến:** Mô hình: một ô có điểm đặc trưng với xác suất $0{,}2$; với hai ảnh cùng ngón, nếu ảnh thứ nhất có đặc trưng ở một ô thì ảnh thứ hai có đặc trưng ở ô đó với xác suất $0{,}8$. Các ô độc lập. Cặp ảnh Cùng có đặc trưng ở một ô Cùng có đủ ba ô Khác ngón $0{,}2^2=0{,}04$ $q_F=0{,}04^3=0{,}000064$ Cùng ngón $0{,}2\cdot0{,}8=0{,}16$ $q_T=0{,}16^3=0{,}004096$ Một hàm nhận cặp cùng ngón với xác suất chỉ khoảng $1/244$; cần ghép nhiều hàm. Các số là xác suất theo mô hình của sách, không phải số đo trên dữ liệu vân tay.
- **Đầu vào và giả thiết:** Xác suất có điều kiện, ba ô cùng đạt; quy tắc thùng s05-02.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; một ô: cùng ngón $0{,}16$, khác ngón $0{,}04$; rồi lũy thừa 3. Không đổi $0{,}8$ thành xác suất vô điều kiện.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu mô hình và giả thiết độc lập; bảng hai hàng loại cặp/xác suất một ô/xác suất ba ô; câu chốt về $q_T\approx1/244$. Năm 2 theo hai tầng nhân, phân biệt xác suất điều kiện $0{,}8$ và xác suất chung $0{,}16$.
- **Kết nối vào–ra:** Quy tắc thùng→xác suất cơ sở; xác suất nhỏ cần ghép nhiều phép thử để giảm bỏ sót.
- **Diễn giải học thuật, lời giải và tiêu chí:** Gọi $E_1,E_2$ là sự kiện ảnh thứ nhất, thứ hai có đặc trưng tại ô đang xét. Với hai ảnh cùng ngón, $\Pr(E_1\cap E_2)=\Pr(E_1)\Pr(E_2\mid E_1)=0{,}2\cdot0{,}8=0{,}16$; với hai ảnh khác ngón, hai ảnh độc lập nên được $0{,}2^2$. $q_T$ và $q_F$ là xác suất cả hai ảnh cùng có đủ ba ô được chọn; ba ô chọn trước khi xét ảnh, nên không điều kiện hóa rằng ảnh truy vấn đã chứa cả ba ô. Tỷ số $q_T/q_F=64$ cho thấy một hàm đã phân biệt hai loại cặp, nhưng $q_T$ quá nhỏ để dùng một mình. MMDS viết “khoảng một phần 200”; giá trị đúng là $1/244{,}14$.
- **Nguồn:** B Ex 3.23/ §3.8.5 tr.118–120/PDF 47–49.
- **Ánh xạ ghi chú:** `lec-06-topic-12` (mã cũ `N12`); số hiệu: Mệnh đề 06.42. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: 99 âm tiết; hai dòng Giả thiết, bảng hai hàng, một Kết luận; ex-note sang ghi chú. Âm tiết mặt trang 99 → 55. Tiêu đề cũ: “Xác suất va chạm của hàm ba ô”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: số hiệu Mệnh đề 06.41 → 06.42. Âm tiết mặt trang 56 → 56.

#### lec06-s05-04 — Phép ghép trong đối sánh vân tay

- **Mục đích và vai trò:** Tính và so sai số của OR 1024 với AND hai nhóm.
- **Thông điệp:** Tăng tính chọn lọc bằng AND làm tăng bỏ sót theo mô hình.
- **Nội dung công khai dự kiến:** OR 1024 hàm nâng xác suất nhận cặp cùng ngón; AND hai nhóm OR 1024 hạ xác suất nhận cặp khác ngón. Cấu trúc Số hàm Nhận cặp khác ngón Bỏ sót cặp cùng ngón OR 1024 1024 $0{,}0634$ $0{,}0150$ AND 2 nhóm OR 1024 2048 $0{,}00402$ $0{,}0297$ Với AND 2 nhóm: $P_F=\left[1-(1-q_F)^{1024}\right]^2$, $P_{\rm miss}=1-\left[1-(1-q_T)^{1024}\right]^2$. AND giảm cặp khác ngón khoảng 16 lần, đổi lại bỏ sót tăng gấp đôi; hai cấu trúc dùng số hàm khác nhau.
- **Đầu vào và giả thiết:** q_F, q_T ở trang trước, AND/OR độc lập.
- **Dữ kiện, hình thức hóa và vết chạy:** V12; phép ghép dùng số chưa làm tròn; hai nhóm tổng 2048 phép thử, khác ngân sách OR 1024.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu vai trò của OR và AND; bảng hai cấu trúc (số hàm, nhận cặp khác ngón, bỏ sót cặp cùng ngón); dòng công thức cho cấu trúc AND; câu chốt định lượng. Giá trị chưa làm tròn và quy trình truy vấn ở ghi chú.
- **Kết nối vào–ra:** Xác suất ba ô → khuếch đại; ứng dụng khung OR–AND qua hợp mã ảnh trong từng nhóm, giao hai hợp rồi xác minh. Với tìm mọi cặp, hợp/giao trên tập cặp phát từ thùng. Sau đó bản tin thay biểu diễn thay vì thay phép ghép.
- **Diễn giải học thuật, lời giải và tiêu chí:** Giá trị chưa làm tròn: OR 1024 cho $1-(1-q_F)^{1024}=0{,}063436634$ và $(1-q_T)^{1024}=0{,}014951892$; AND hai nhóm cho $0{,}004024207$ và $0{,}029680224$. Sách lấy $0{,}063^2$ nên được $0{,}00397$, lệch do làm tròn trung gian. Với bài toán một–nhiều, xác suất nhận cặp khác ngón cũng là tỷ lệ kho phải so với ảnh truy vấn: khoảng $6{,}3\%$ với OR, khoảng $1/250$ với AND. Thực hiện với một ảnh truy vấn: hợp các ảnh trong những thùng chứa nó ở nhóm thứ nhất, làm tương tự ở nhóm thứ hai, lấy giao hai hợp rồi so ảnh truy vấn với các ảnh còn lại. Hợp và giao chỉ xử lý mã ảnh; phép so vân tay mới là phần tốn kém.
- **Nguồn:** B §3.8.5/Ex 3.23 tr.118–120/PDF 47–49.
- **Ánh xạ ghi chú:** `lec-06-topic-12` (mã cũ `N12`); số hiệu: Ví dụ 06.18; Tình huống 06.2. **Thời lượng:** 2,5 phút (trước 3 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: một dòng dẫn, bảng hai hàng, một khối công thức. Âm tiết mặt trang 69 → 54.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A2, B17: dòng Giả thiết độc lập (giả định MMDS) thay dòng 21 âm tiết; $P_{\rm miss}$ đổi thành $1-P_T$; ghi chú: chỉ độc lập có điều kiện, $0{,}0150$ là cận dưới theo Jensen. Âm tiết mặt trang 60 → 57.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch): ghi chú nêu OR 1024 là thuật toán tổng quát, AND hai nhóm OR lấy giao hai tập cặp. Âm tiết mặt trang 57 → 57.

#### lec06-s05-05 — Bản tin gần trùng

- **Mục đích và vai trò:** Nêu bài toán bản tin gần trùng, quy tắc shingle theo từ dừng (Ví dụ 3.24) và hệ quả: Jaccard phản ánh phần văn xuôi, khác shingle ký tự.
- **Thông điệp:** Biểu diễn phải phù hợp với tiêu chuẩn cùng văn bản.
- **Nội dung công khai dự kiến:** Một bản tin được nhiều báo đăng lại kèm quảng cáo khác nhau; cần cặp trang cùng văn bản gốc. Văn xuôi có nhiều từ dừng (từ rất thường gặp) hơn quảng cáo. Shingle: một từ dừng và hai từ tiếp theo. Từ dừng của ví dụ: I, that, you, for, your. Buy Sudzo. Không có từ dừng nên không có shingle. I recommend that you buy Sudzo for your laundry. “I recommend that” · “that you buy” “you buy Sudzo” · “for your laundry” · “your laundry …” Shingle tập trung ở văn xuôi, nên Jaccard phản ánh phần bản tin hơn phần quảng cáo.
- **Đầu vào và giả thiết:** Từ dừng là từ rất thường gặp; danh sách ví dụ I, that, you, for, your. Shingle lấy từ dừng và hai token kế tiếp. Token sau laundry chưa được cho.
- **Dữ kiện, hình thức hóa và vết chạy:** that + you + buy → that you buy. Buy Sudzo không có từ dừng trong danh sách. Câu dài có bốn shingle xác định và your laundry x chưa xác định x. Mật độ từ dừng cao hơn trong văn xuôi của tình huống nguồn giải thích mục đích biểu diễn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Câu dẫn nêu bài toán; dòng quy tắc shingle; hai thẻ cho câu quảng cáo và câu văn xuôi; câu chốt về Jaccard. So sánh $0{,}75$/$0{,}25$/$1/3$ ở ghi chú.
- **Kết nối vào–ra:** Ứng dụng phép ghép→lựa chọn đặc trưng; kiểm tra phần nối biểu diễn với ý nghĩa kết quả.
- **Diễn giải học thuật, lời giải và tiêu chí:** Shingle thứ năm “your laundry x” có $x$ là từ đứng sau câu, chưa được cho. MMDS so sánh hai trang, mỗi trang nửa bản tin, nửa quảng cáo: nếu chung bản tin mà khác quảng cáo, Jaccard theo shingle từ dừng có thể khoảng $0{,}75$; nếu chung quảng cáo mà khác bản tin, khoảng $0{,}25$. Với shingle 10 ký tự liên tiếp, hai trường hợp đều cho khoảng $1/3$, nên không phân biệt được. Quy tắc chỉ ưu tiên văn xuôi; một câu quảng cáo viết dạng văn xuôi vẫn tạo shingle. Mục tiêu là cùng văn bản, không phải cùng chủ đề; bài toán cùng chủ đề cần kỹ thuật khác. Sau khi có tập shingle mới, MinHash, phân dải và xác minh Jaccard được dùng lại nguyên vẹn.
- **Nguồn:** B §3.8.6/Ex 3.24 tr.120–121/PDF 49–50.
- **Ánh xạ ghi chú:** `lec-06-topic-13` (mã cũ `N13`); số hiệu: Định nghĩa 06.43; Tình huống 06.3. **Thời lượng:** 1,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 108 âm tiết; nhu cầu và định nghĩa ở trang này, ví dụ Sudzo sang s05-07. Âm tiết mặt trang 108 → 58. Tiêu đề cũ: “Shingle theo từ dừng cho bản tin”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: "từ dừng (stop word)". Âm tiết mặt trang 58 → 56.

#### lec06-s05-07 — Ví dụ: shingle theo từ dừng

- **Mạch và mục đích:** Mạch 5, ví dụ. Chạy quy tắc shingle theo từ dừng trên Ví dụ 3.24.
- **Thao tác của sinh viên:** Liệt kê shingle của hai câu; nhận ra shingle còn thiếu từ.
- **Đối tượng trung tâm:** Bốn shingle xác định của câu văn xuôi.
- **Dữ kiện và ký hiệu kế thừa:** Định nghĩa shingle theo từ dừng s05-05.
- **Kiến thức đầu vào:** Shingle Bài 05.
- **Sản phẩm học tập:** Danh sách shingle và giải thích câu quảng cáo không có shingle.
- **Bằng chứng kiểm tra:** Câu hỏi s05-08; Bài tập 06.14.
- **Kết nối vào–ra:** Vào: s05-05. Ra: câu hỏi ứng dụng s05-06, s05-08.
- **Nguồn:** MMDS §3.8.6, Ví dụ 3.24, tr.120–121.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: ví dụ tách từ s05-05. Âm tiết mặt trang — → 57.
- **Ánh xạ ghi chú:** `lec-06-topic-13`; số hiệu: Ví dụ 06.19. **Thời lượng:** 1,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: dòng dữ kiện thêm nhiệm vụ "liệt kê shingle". Âm tiết mặt trang 57 → 60.

#### lec06-s05-06 — Câu hỏi về đối sánh thực thể và vân tay

- **Mục đích và vai trò:** Kiểm tra phần 5 bằng dữ kiện mới: tạo ứng viên và xác minh trong đối sánh thực thể, OR 512 cho vân tay, shingle từ dừng trên câu mới.
- **Thông điệp:** Biểu diễn và bước kiểm cuối xác định ý nghĩa của kết quả.
- **Nội dung công khai dự kiến:** Câu hỏi: Hai hồ sơ có tên “Bob S. Jomes” và “Robert Jones Jr.”, cùng địa chỉ, khác điện thoại. Xác định cặp có thành ứng viên không, qua hàm khóa nào, và bước nào quyết định hai hồ sơ cùng người. Dùng OR 512 thay cho OR 1024 với $q_F,q_T$ đã có. Tính xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón. Với từ dừng I, that, you, for, your, liệt kê các shingle có đủ hai từ theo sau trong câu “The report said that you should wait for your turn.”
- **Đầu vào và giả thiết:** Ba cơ chế s05-01–05.
- **Dữ kiện, hình thức hóa và vết chạy:** Câu 1 dùng cặp tên của MMDS §3.8.1; câu 2 (OR 512) và câu 3 (câu “The report said…”) là dữ kiện luyện tập mới, dùng $q_F$, $q_T$ và danh sách từ dừng của nguồn.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba nhiệm vụ trong một khối; mỗi nhiệm vụ ghi tên miền để tránh đổi ngữ cảnh ngầm. Năm 2 phân biệt đối tượng/ứng viên/kết quả, đáp án ở notes.
- **Kết nối vào–ra:** Ba ứng dụng→kiểm tra; tổng kết thu hồi toàn quy trình chọn và kiểm cặp.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: tên không trùng hoàn toàn, điện thoại khác, địa chỉ trùng, nên cặp thành ứng viên qua khóa địa chỉ. Bước chấm điểm theo ba trường và ngưỡng điểm quyết định hai hồ sơ cùng người; trùng địa chỉ không đủ. Câu 2: $1-(1-0{,}000064)^{512}\approx0{,}0322$ và $(1-0{,}004096)^{512}\approx0{,}1223$; so với OR 1024, cặp khác ngón giảm khoảng một nửa nhưng bỏ sót tăng khoảng tám lần. Câu 3: “that you should”, “you should wait”, “for your turn”; shingle bắt đầu bằng “your” chỉ có một từ theo sau trong câu. Tiêu chí: phân biệt tạo ứng viên với xác minh; dùng giá trị $q_F,q_T$ chưa làm tròn và đúng chiều của bỏ sót; chỉ bắt đầu shingle tại từ dừng.
- **Nguồn:** B §3.8.1–6 tr.114–121; kiểm quy tắc nguồn.
- **Ánh xạ ghi chú:** `lec-06-topic-11, lec-06-topic-12` (mã cũ `N11,N12,N13`); số hiệu: Bài tập 06.12, 06.13. **Thời lượng:** 1,5 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `tách`: 107 âm tiết; câu shingle sang s05-08. Âm tiết mặt trang 107 → 50. Tiêu đề cũ: “Câu hỏi về các ứng dụng”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A2, nhẹ: dữ kiện hồ sơ lên dòng "Câu hỏi:"; câu vân tay nêu giả định độc lập của MMDS. Âm tiết mặt trang 51 → 58.

#### lec06-s05-08 — Câu hỏi về shingle theo từ dừng

- **Mạch và mục đích:** Mạch 5, kiểm tra. Câu hỏi về shingle theo từ dừng, tách từ s05-06.
- **Thao tác của sinh viên:** Liệt kê shingle có đủ hai từ theo sau.
- **Đối tượng trung tâm:** Câu luyện tập "The report said that you should wait for your turn."
- **Dữ kiện và ký hiệu kế thừa:** Danh sách năm từ dừng của Ví dụ 3.24.
- **Kiến thức đầu vào:** Định nghĩa 06.43.
- **Sản phẩm học tập:** Ba shingle và một shingle chưa xác định.
- **Bằng chứng kiểm tra:** Lời giải trong ghi chú diễn giả; Bài tập 06.14.
- **Kết nối vào–ra:** Vào: s05-07. Ra: mạch tổng kết.
- **Nguồn:** MMDS §3.8.6; câu luyện tập do bản soạn đặt.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: câu hỏi tách từ s05-06. Âm tiết mặt trang — → 30. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Ánh xạ ghi chú:** `lec-06-topic-13`; số hiệu: Bài tập 06.14. **Thời lượng:** 1 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: ghi chú bỏ "bản soạn". Âm tiết mặt trang 30 → 30.

### Mạch 6. Tổng kết và tự kiểm tra

#### lec06-s06-00 — 6. Tổng kết và tự kiểm tra

- **Mạch và vị trí:** điểm vào mạch 6; trang tiêu đề mạch `section.strand-title`, `id="mach-6"`, mở tại `#/6`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 6 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Kết quả của mạch 2–5.
- **Sản phẩm giao cho mạch sau:** bảng kết quả, bảng thuật toán, trả lời vấn đề trung tâm; nối Bài 07.
- **Vai trò chu trình:** ngoài chu trình khái niệm.
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/6` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 39 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-14`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B4, C: dòng dẫn "Muốn trả lời bài toán kho một triệu tài liệu…"; ghi chú 92 âm tiết, bỏ câu "Mạch này không đưa khái niệm mới". Âm tiết mặt trang 39 → 39.

#### lec06-s06-05 — Kết quả và giả thiết không được bỏ

- **Mạch và mục đích:** Mạch 6, tổng kết. Bảng bảy kết quả của mạch 2–5 với giả thiết không được bỏ.
- **Thao tác của sinh viên:** Nêu giả thiết của từng kết quả và hậu quả khi bỏ.
- **Đối tượng trung tâm:** Bảng Kết quả, Giả thiết không được bỏ, Công thức hoặc thuật toán.
- **Dữ kiện và ký hiệu kế thừa:** Mệnh đề 06.5, Định lý 06.7, Định nghĩa 06.22, Mệnh đề 06.26.
- **Kiến thức đầu vào:** Mạch 2–4.
- **Sản phẩm học tập:** Danh sách giả thiết có phản ví dụ trong ghi chú diễn giả.
- **Bằng chứng kiểm tra:** Câu 4–5 của s06-04.
- **Kết nối vào–ra:** Vào: trang tiêu đề mạch 6. Ra: bảng thuật toán s06-02.
- **Nguồn:** Tổng hợp MMDS §§3.4–3.7.
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: mạch kết luận bắt buộc có bảng Kết quả, Giả thiết không được bỏ, Công thức hoặc thuật toán. Âm tiết mặt trang — → 63.
- **Ánh xạ ghi chú:** `lec-06-topic-14`; số hiệu: Mệnh đề 06.5; Định lý 06.7; Định nghĩa 06.22; Mệnh đề 06.26. **Thời lượng:** 2 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B3: thêm hàng ba họ cơ sở, vân tay (giả định độc lập), khóa thực thể; $P$ đổi thành $\Pr[h(x)=h(y)]$; 8 hàng bảng (trần 8). Âm tiết mặt trang 63 → 78.

#### lec06-s06-02 — Thuật toán, bảo đảm và chi phí

- **Mục đích và vai trò:** So năm thuật toán của bài theo đầu vào, bảo đảm và chi phí trong cùng mô hình từ máy.
- **Thông điệp:** Bảo đảm là xác suất theo cặp và có giả thiết; chi phí chữ ký cộng với chi phí phân dải và xác minh.
- **Nội dung công khai dự kiến:** Đại lượng Ý nghĩa Hệ quả $P_{b,r}(s)$ Xác suất cặp Jaccard $s$ thành ứng viên Cặp đạt ngưỡng bị bỏ sót với xác suất $1-P_{b,r}(s)$ $Q$ Lượt phát cặp trước khử lặp Thời gian phát cặp $O(Q)$ $K$ Cặp duy nhất phải xác minh Ứng viên giả bị loại, nhưng tốn thời gian xác minh Trường hợp xấu nhất, mọi đối tượng chung thùng: $K=\tbinom C2$, không nhanh hơn so mọi cặp. Xác minh loại được ứng viên giả nhưng không lấy lại cặp bị bỏ sót.
- **Đầu vào và giả thiết:** HT2, HT3, mô hình chi phí N04.
- **Dữ kiện, hình thức hóa và vết chạy:** V01 và V02 giữ vai trò; không tự tuyên bố giảm cặp tuyến tính.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bảng bốn cột Thuật toán | Đầu vào | Bảo đảm | Chi phí, năm hàng: phân dải và xác minh, tìm cặp với họ nhạy cảm, chữ ký chọn tọa độ, chữ ký dấu, chữ ký chiếu có dịch. Nội dung công khai dự kiến ở trên là bản kế hoạch cũ.
- **Kết nối vào–ra:** Vào: s06-05 (giả thiết). Ra: s06-01 dùng hàng phân dải để chặn $K$.
- **Diễn giải học thuật, lời giải và tiêu chí:** Chi phí ba họ cơ sở chỉ là chi phí lấy chữ ký; thuật toán tổng quát lấy chữ ký bằng $br$ hàm rồi chạy phân dải và xác minh bằng $d$. Ứng viên giả làm tăng $K$; bước xác minh không khôi phục được cặp bỏ sót. Đổi $b$, $r$ dịch vùng chuyển tiếp, nên giảm một loại sai số thường làm tăng loại kia.
- **Nguồn:** B §3.4.2–3, §3.6.3; sources/source.md, Bài 07.
- **Ánh xạ ghi chú:** `lec-06-topic-14` (mã cũ `N14`); số hiệu: Thuật toán 06.4, 06.33; Mệnh đề 06.11, 06.38. **Thời lượng:** 1,5 phút (trước 1.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: đổi vai trò thành bảng Thuật toán, Đầu vào, Bảo đảm, Chi phí; nội dung cũ chuyển sang s06-01 và ghi chú diễn giả. Âm tiết mặt trang 82 → 53. Tiêu đề cũ: “Chi phí và hai loại sai số”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B7, A4: thêm hàng thuật toán tìm cặp với họ nhạy cảm; đầu vào chiếu "$\mathbb R^D$", bảo đảm "khi $D=2$"; bỏ $\Sigma^D$; ghi chú bỏ cặp câu khẩu hiệu. Âm tiết mặt trang 54 → 74.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: "$Cbr$ lần tính hàm, cộng phân dải". Âm tiết mặt trang 74 → 76.

#### lec06-s06-01 — Câu trả lời cho vấn đề trung tâm

- **Mục đích và vai trò:** Trả lời vấn đề trung tâm s01-08 bằng các kết luận có điều kiện, theo thứ tự các dòng của s01-08; thu hồi bài toán kho một triệu tài liệu bằng một chặn kỳ vọng cho $K$ dưới giả định về phân bố tương đồng.
- **Thông điệp:** Mỗi bảo đảm có giả thiết riêng; số cặp phải xác minh chỉ nhỏ khi dữ liệu có ít cặp tương đồng, và tuyến tính kỳ vọng cho phép tính chặn đó.
- **Nội dung công khai dự kiến:** [Hình: Chữ ký tạo khóa, hợp cặp ứng viên rồi kiểm tập gốc.] Biểu diễn và độ đo: Jaccard trên tập, góc, Euclid, Hamming. Họ $(d_1,d_2,p_1,p_2)$-nhạy cảm và cấu trúc ghép: AND $r$ rồi OR $b$ là phân dải. Dựng thùng, khử lặp $Q$ lượt phát thành $K$ cặp, xác minh trên dữ liệu gốc. Ba ứng dụng chỉ thay bước 1 hoặc 2: bản tin đổi biểu diễn, vân tay và thực thể đổi họ hàm; bước 3 giữ nguyên.
- **Đầu vào và giả thiết:** N01–N13; không có khái niệm mới.
- **Dữ kiện, hình thức hóa và vết chạy:** Ba bước gắn với kết quả từng phần (độ đo của phần 3; họ và AND–OR của phần 3–4; $Q$, $K$ và xác minh của phần 2); câu chốt nêu ứng dụng nào đổi bước nào.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Sơ đồ một hàng hai tầng để nhãn đọc được; mỗi bước một danh từ/thao tác. Năm 2 cần nhận ra các quyết định nối nhau; ví dụ chi tiết không lặp trên mặt trang.
- **Kết nối vào–ra:** Vào: s06-02 (bảng thuật toán, chi phí $O(nC+Q+\sum T_J)$), s02-16 (ghi chú: $\mathbb E[K]=\sum P_{b,r}(s_{cd})$), s05-04 (số vân tay). Ra: câu hỏi tự kiểm tra s06-03, s06-04 và Bài 07.
- **Diễn giải học thuật, lời giải và tiêu chí:** Sáu dòng: phân dải $b=20$, $r=5$ bỏ sót cặp $s=0{,}8$ với xác suất $\approx0{,}00036$; AND 4 rồi OR 4 đưa $(0{,}8;0{,}4)$ thành $(0{,}88;0{,}10)$; chi phí chữ ký $O(Cm)$ hoặc $O(CmD)$ kèm giả thiết của từng họ; vân tay OR 1024 cho $0{,}0634$ và $0{,}0150$ dưới giả định độc lập; giả định $s\le0{,}1$ cho mọi cặp ngoài $N$ cặp gần cho $\mathbb E[K]\le N+10^8$ vì $P_{20,5}(0{,}1)=1{,}9998\cdot10^{-4}$; khi $N\ll10^8$ xác minh khoảng 100 giây thay cho $5{,}79$ ngày. Số $10^6$ cặp ứng viên cũ giữ trong ghi chú như số liệu luyện tập. Nội dung công khai dự kiến ở trên là bản kế hoạch cũ.
- **Nguồn:** B §3.4.3 và §3.8, tr.95–96, 114–121.
- **Ánh xạ ghi chú:** `lec-06-topic-14` (mã cũ `N14`); số hiệu: Tóm tắt chương. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: gộp s06-01 và s06-02 cũ thành năm kết luận có điều kiện theo thứ tự trang vấn đề trung tâm; thu hồi kho một triệu tài liệu bằng số cặp và giả định luyện tập; bỏ hình (đã ở s01-04). Âm tiết mặt trang 64 → 78. Tiêu đề cũ: “Quy trình tìm cặp tương đồng”.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A3, C: tiêu đề "Câu trả lời cho vấn đề trung tâm"; bỏ dòng giả định $10^6$ cặp; thêm giả định $s\le0{,}1$ cho cặp nền, $\mathbb E[K]\le N+10^8$ và khoảng 100 giây; dòng 3–4 có số và giả thiết; số $10^6$ cặp giữ trong ghi chú như số liệu luyện tập. Âm tiết mặt trang 80 → 73.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: trung bình (rà lại mạch, toán): dòng 3 nêu bảo đảm và giả thiết của ba họ, chi phí tách khỏi giả thiết; dòng 6 "thời gian xác minh kỳ vọng không quá khoảng 100 giây", $1\,\mu\mathrm{s}$; ghi chú dẫn Mệnh đề 06.13, không cần các cặp độc lập, $\mathbb E[Q]\le20N+10^8$, cùng giả định $1\,\mu\mathrm{s}$ với s01-03. Âm tiết mặt trang 73 → 76.

#### lec06-s06-03 — Câu hỏi tự kiểm tra

- **Mục đích và vai trò:** Kiểm tra tổng hợp MT1–MT3 bằng dữ kiện mới: đếm $Q$, $K$; ngưỡng và xác suất với $b=10$, $r=4$; bộ tham số MinHash và AND 2.
- **Thông điệp:** Hợp đồng đầu ra và mô hình xác suất cần được phân biệt.
- **Nội dung công khai dự kiến:** Câu hỏi: SIG có hai hàng $(2,1,2,0)$ và $(1,1,1,1)$; $b=2$, $r=1$. Tính $Q$, $K$ và nêu cặp được phát lặp. Với $b=10$, $r=4$, tính ngưỡng xấp xỉ $(1/b)^{1/r}$ và xác suất thành ứng viên của cặp có $s=0{,}8$ và $s=0{,}3$. Viết bộ tham số của họ MinHash với $d_1=0{,}2$, $d_2=0{,}5$, rồi của họ sau AND 2.
- **Đầu vào và giả thiết:** Thuật toán phân dải, $P_{b,r}(s)$, định nghĩa họ nhạy cảm và phép AND; dữ kiện luyện tập không trùng các vết chạy đã giải.
- **Dữ kiện, hình thức hóa và vết chạy:** Câu 1→MT1; câu 2→MT2; câu 3→MT3. Đáp án đã tính lại: $Q=7$, $K=6$; $0{,}562$, $0{,}9949$, $0{,}0781$; $(0{,}2;\ 0{,}5;\ 0{,}64;\ 0{,}25)$.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba yêu cầu một cột; đáp án và tiêu chí chỉ ở ghi chú.
- **Kết nối vào–ra:** Giới hạn→tự kiểm nửa đầu; trang sau kiểm phép ghép/họ/ứng dụng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: dải 1 cho thùng $\{1,3\}$, dải 2 cho thùng $\{1,2,3,4\}$; $Q=1+6=7$, $K=6$, cặp $(1,3)$ phát hai lần. Câu 2: ngưỡng $0{,}1^{1/4}\approx0{,}562$; $P(0{,}8)=1-(1-0{,}4096)^{10}\approx0{,}9949$, $P(0{,}3)=1-(1-0{,}0081)^{10}\approx0{,}0781$. Câu 3: $(0{,}2;\ 0{,}5;\ 0{,}8;\ 0{,}5)$, sau AND 2 là $(0{,}2;\ 0{,}5;\ 0{,}64;\ 0{,}25)$ với hai hàm độc lập. Tiêu chí: đếm cả lượt phát lặp trong $Q$ và chỉ đếm một lần trong $K$; dùng đúng thứ tự AND trong dải rồi OR giữa các dải; giữ nguyên $d_1$, $d_2$ khi ghép.
- **Nguồn:** B Ex 3.8, §3.4.2, Ex 3.18 tr.105; tổng hợp mục tiêu MT1–MT3.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N14`); số hiệu: Bài tập 06.16–06.18. **Thời lượng:** 2,5 phút (trước 2.5 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng."; câu MinHash chuyển sang s06-04, câu "giữ r, tăng b" chuyển vào đây. Âm tiết mặt trang 52 → 34. Tiêu đề cũ: “Câu hỏi tổng hợp về phân dải”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ (toán): ghi chú gọi $0{,}1^{1/4}$ là xấp xỉ, thêm nghiệm một nửa $\approx0{,}509$; "kỳ vọng của $K$". Âm tiết mặt trang 34 → 34.

#### lec06-s06-04 — Câu hỏi tự kiểm tra

- **Mục đích và vai trò:** Kiểm tra tổng hợp MT4–MT6: AND–OR trên họ siêu phẳng, chọn họ và chi phí cho một ứng dụng mới, đánh đổi hai loại sai số khi tăng $b$.
- **Thông điệp:** Kết quả số chỉ có ý nghĩa trong mô hình đã nêu.
- **Nội dung công khai dự kiến:** Câu hỏi: Họ siêu phẳng với cặp gần $\theta\le\pi/6$, cặp xa $\theta\ge\pi/2$. Tính $p_1$, $p_2$ và hai cận sau AND 2 rồi OR 2. Kho $C$ ảnh, mỗi ảnh một vector đặc trưng thực 128 chiều; cặp cần tìm có góc nhỏ. Chọn họ cơ sở và nêu chi phí tính chữ ký $m$ bit. Giữ $r$, tăng $b$: xác định ảnh hưởng tới số cặp bỏ sót và tới $K$.
- **Đầu vào và giả thiết:** Họ siêu phẳng, công thức AND/OR, bảng chi phí ba họ, $P_{b,r}(s)$ và hai loại sai số.
- **Dữ kiện, hình thức hóa và vết chạy:** Câu 1→MT4; câu 2→MT5–MT6; câu 3→MT2, MT6. Đáp án đã tính lại: $5/6$, $1/2$, $0{,}9066$, $0{,}4375$; $128\,Cm$ phép nhân.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba yêu cầu một cột; đáp án và tiêu chí chỉ ở ghi chú.
- **Kết nối vào–ra:** Tự kiểm nửa đầu→nửa sau; bài tập nguồn cung cấp vết chạy đầy đủ hơn.
- **Diễn giải học thuật, lời giải và tiêu chí:** Câu 1: $p_1=1-1/6=5/6$, $p_2=1/2$; $F(p)=1-(1-p^2)^2$ cho $F(5/6)\approx0{,}9066$ và $F(1/2)=0{,}4375$. Câu 2: họ siêu phẳng, vì góc chỉ phụ thuộc hướng; tính chữ ký cần $C\cdot m\cdot128$ phép nhân, tức $O(CmD)$ với $D=128$, và lưu $m$ bit mỗi ảnh cùng $128m$ số cho các pháp tuyến. Câu 3: $P_{b,r}(s)$ tăng với mọi $s$, nên ít cặp bỏ sót hơn nhưng nhiều cặp xa thành ứng viên hơn, $K$ và thời gian xác minh tăng. Tiêu chí: đổi góc sang radian trước khi dùng $1-\theta/\pi$; tách chi phí tính chữ ký khỏi chi phí phân dải; nêu đủ hai chiều của đánh đổi.
- **Nguồn:** B Ex 3.19–20, §3.7.2, §3.8.5; tổng hợp MT4–MT6.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N14`); số hiệu: Bài tập 06.15, 06.19, 06.27. **Thời lượng:** 2 phút (trước 2 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng."; đánh số tiếp 4–6. Âm tiết mặt trang 69 → 51. Tiêu đề cũ: “Câu hỏi tổng hợp về họ băm và ứng dụng”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B17: câu 6 rút còn 18 âm tiết. Âm tiết mặt trang 55 → 52.

#### lec06-s06-08 — Nguồn và tài liệu đọc

- **Mạch và mục đích:** Mạch 6, tổng kết. Nguồn, ghi công mmds.org, liên kết ghi chú bài giảng, nối sang Bài 07.
- **Thao tác của sinh viên:** Mở ghi chú bài giảng; xác định mục sách tương ứng từng mạch.
- **Đối tượng trung tâm:** Danh mục nguồn.
- **Dữ kiện và ký hiệu kế thừa:** Toàn bài.
- **Kiến thức đầu vào:** Không.
- **Sản phẩm học tập:** Danh mục đọc và liên kết viewer.
- **Bằng chứng kiểm tra:** Liên kết viewer mở được (kiểm bằng trình duyệt).
- **Kết nối vào–ra:** Vào: câu hỏi tự kiểm tra. Ra: mạch bài tập; Bài 07 (căn cứ `sources/source.md`, dòng Bài 7).
- **Nguồn:** MMDS 3e Chương 3; Stanford CS246 LSH I–II; Datar và cộng sự (2004).
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: mạch kết luận bắt buộc có trang nguồn, ghi công mmds.org và liên kết ghi chú. Âm tiết mặt trang — → 56.
- **Ánh xạ ghi chú:** `lec-06-topic-15`; số hiệu: Hướng dẫn đọc thêm và tài liệu tham khảo. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11, B17: HNSW, PQ viết đầy đủ trong ghi chú, mặt trang "chỉ mục đồ thị HNSW và lượng tử hóa tích (PQ)"; tên đầy đủ Datar và cộng sự; nhãn "Đối chiếu:" thành "Nguồn:"; trang nguồn theo trần 80 (ngoại lệ). Âm tiết mặt trang 64 → 65.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ (rà lại toán): ghi chú tách bài về nhà (06.15–06.19, 06.26, 06.27, 06.29, 06.30) khỏi bài giải trên lớp. Âm tiết mặt trang 65 → 65.

### Mạch 7. Bài tập vận dụng

#### lec06-s07-00 — 7. Bài tập vận dụng

- **Mạch và vị trí:** điểm vào mạch 7; trang tiêu đề mạch `section.strand-title`, `id="mach-7"`, mở tại `#/7`.
- **Mục đích:** nêu nhiệm vụ của mạch bằng một dòng dẫn và tối đa năm cụm từ khóa; không định nghĩa, công thức, hình hay bài tập.
- **Thao tác của sinh viên:** đọc dòng dẫn, nhận ra kết quả kế thừa và nhiệm vụ mới.
- **Đối tượng trung tâm:** tên mạch, trùng từng chữ với dòng 7 của trang Nội dung `lec06-s01-07`.
- **Dữ kiện và ký hiệu kế thừa:** Toàn bộ kết quả của bài.
- **Sản phẩm giao cho mạch sau:** lời giải bảy trang đề, Bài tập 06.20–06.25, 06.28.
- **Vai trò chu trình:** ngoài chu trình khái niệm.
- **Bằng chứng:** trang kiểm tra cuối mạch; số mạch khớp `#/7` khi duyệt bằng trình duyệt.
- **Nguồn:** kế hoạch căn chỉnh 2026-10-14, mục A; `AGENTS.md`, "Trang tiêu đề mạch".
- **Căn chỉnh 2026-10-14:** quyết định `thêm`: trang tiêu đề mạch bắt buộc. Âm tiết mặt trang — → 40 (dòng dẫn ≤ 25 âm tiết theo quy tắc trang tiêu đề mạch).
- **Ánh xạ ghi chú:** `lec-06-topic-16`. **Thời lượng:** 0,5 phút.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: C: nhãn "Nhu cầu:" in đậm; "bảy bài"; từ khóa rút gọn; ghi chú: Bài 3.4.4 là đọc thêm. Âm tiết mặt trang 41 → 36.

#### lec06-s07-01 — Bài tập: bảng giá trị đường cong S

- **Mục đích và vai trò:** Tính đủ bảng xác suất của Bài 3.4.1.
- **Thông điệp:** Tham số dải quyết định đường xác suất cho từng giá trị tương đồng.
- **Nội dung công khai dự kiến:** Câu hỏi: Tính $P(s)=1-(1-s^r)^b$ với $s=0{,}1;\ 0{,}2;\ \ldots;\ 0{,}9$ cho ba cấu hình: Cấu hình $r$ $b$ 1 3 10 2 6 20 3 5 50 Sản phẩm: bảng 9 hàng × 3 cột xác suất. Có thể dùng máy tính cho lũy thừa; chỉ làm tròn kết quả cuối.
- **Đầu vào và giả thiết:** HT3; giữ nguyên cả ba cấu hình và chín giá trị $s$.
- **Dữ kiện, hình thức hóa và vết chạy:** R1 phần đầu; đáp án 27 giá trị ở bảng lời giải phía sau trong storyboard; không đổi thứ tự (r, b).
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trên là công thức/dữ kiện; dưới bảng trống 9 hàng × 3 cột chỉ chứa nhãn để làm bài. Năm 2 tính có hệ thống, không cần chép số nguồn dài; đáp án trong notes/ghi chú.
- **Kết nối vào–ra:** Tự kiểm→tính đường xác suất; bảng dẫn tới điểm xác suất một nửa.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án theo $s=0{,}1;\ldots;0{,}9$. Cấu hình $(r,b)=(3,10)$: $0{,}009955$; $0{,}077181$; $0{,}239449$; $0{,}483871$; $0{,}736924$; $0{,}912267$; $0{,}985015$; $0{,}999234$; $0{,}999998$. Cấu hình $(6,20)$: $0{,}000020$; $0{,}001279$; $0{,}014479$; $0{,}078809$; $0{,}270187$; $0{,}615415$; $0{,}918186$; $0{,}997712$; $0{,}9999997$. Cấu hình $(5,50)$: $0{,}000500$; $0{,}015875$; $0{,}114540$; $0{,}402284$; $0{,}795551$; $0{,}982534$; $0{,}999899$; $0{,}999999998$; giá trị cuối làm tròn thành 1 nhưng không bằng 1 chính xác. Tiêu chí: giữ đúng $r$ và $b$, tính đủ 27 giá trị, chỉ làm tròn sau lũy thừa.
- **Nguồn:** B Bài 3.4.1, §3.4.4, tr.96/PDF 25; dịch nguyên yêu cầu, không lược cấu hình.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.20. **Thời lượng:** 11,5 phút (trước 12 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Bài tập:; bảng cấu hình thành một dòng công thức; giữ dòng nguồn số bài sách. Âm tiết mặt trang 37 → 34. Tiêu đề cũ: “Bảng giá trị đường cong S”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B8: ghi chú thêm giá trị $s=0{,}9$ của $(5,50)$: $1-4{,}1\cdot10^{-20}$. Âm tiết mặt trang 37 → 36.

#### lec06-s07-02 — Bài tập: nghiệm một nửa của đường cong S

- **Mục đích và vai trò:** Giải ngưỡng chính xác và so xấp xỉ cho ba cấu hình nguồn.
- **Thông điệp:** Nghiệm $P(s)=1/2$ khác xấp xỉ $b^{-1/r}$.
- **Nội dung công khai dự kiến:** Câu hỏi: Với ba cấu hình của bài trước, tìm $s$ sao cho $P(s)=1/2$ và so với xấp xỉ $(1/b)^{1/r}$. $(r,b)$ Nghiệm của $P(s)=1/2$ $(1/b)^{1/r}$ $(3,10)$ $(6,20)$ $(5,50)$ Sản phẩm: phép biến đổi giải $s$ và bảng ba cặp giá trị.
- **Đầu vào và giả thiết:** Bảng xác suất, biến đổi lũy thừa; không thêm điểm bất động.
- **Dữ kiện, hình thức hóa và vết chạy:** R1 phần hai; nghiệm (.406088134, .569353387, .424394480); xấp xỉ (.464158883, .606962231, .457305052).
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Khối đề trên; bảng trống 3 hàng cấu hình/chính xác/xấp xỉ dưới. Năm 2 thực hiện đại số thay vì đọc đồ thị; hai giá trị đặt cạnh để không đồng nhất.
- **Kết nối vào–ra:** Bảng P →ngưỡng; phép ghép tổng quát tiếp tục thao tác xác suất.
- **Diễn giải học thuật, lời giải và tiêu chí:** Từ $(1-s^r)^b=1/2$ suy ra $s=(1-2^{-1/b})^{1/r}$. Nghiệm chính xác: $0{,}406088$; $0{,}569353$; $0{,}424394$. Xấp xỉ $(1/b)^{1/r}$: $0{,}464159$; $0{,}606962$; $0{,}457305$. Cả ba xấp xỉ đều lớn hơn nghiệm chính xác, nên dùng xấp xỉ sẽ ước lượng ngưỡng hơi cao. Tiêu chí: có bước biến đổi, tính đủ ba cấu hình và nêu chiều sai lệch của xấp xỉ.
- **Nguồn:** B Bài 3.4.2, §3.4.4, tr.96/PDF 25; giữ yêu cầu và toàn cấu hình bài 3.4.1.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.21. **Thời lượng:** 6 phút (trước 6 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Bài tập:; đề tự chứa bằng bảng cấu hình. Âm tiết mặt trang 36 → 30. Tiêu đề cũ: “Ngưỡng của đường cong S”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B6: tiêu đề "Bài tập: nghiệm một nửa của đường cong S"; ghi chú dùng "nghiệm một nửa $s_{1/2}$". Âm tiết mặt trang 31 → 30.

#### lec06-s07-03 — Bài tập: xác suất qua nhiều tầng ghép

- **Mục đích và vai trò:** Viết xác suất cho bốn chuỗi AND/OR của Bài 3.6.1.
- **Thông điệp:** Thứ tự phép ghép được giữ trong từng trạng thái trung gian.
- **Nội dung công khai dự kiến:** Câu hỏi: Bắt đầu từ họ MinHash với xác suất trùng $p$ của một hàm; các hàm độc lập. Viết xác suất trùng sau mỗi chuỗi ghép: Ý Thứ tự ghép (a) AND 2 → OR 3 (b) OR 3 → AND 2 (c) AND 2 → OR 2 → AND 2 (d) OR 2 → AND 2 → OR 2 → AND 2 Sản phẩm: bốn biểu thức xác suất, ghi rõ từng tầng trung gian.
- **Đầu vào và giả thiết:** HT7; các cấu hình nguyên nguồn.
- **Dữ kiện, hình thức hóa và vết chạy:** R2; lời giải các trạng tháiq 1, q 2, q 3 ở mục đáp án. Không thêm yêu cầu mã.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Bốn hàng chuỗi thao tác, mỗi hàng mũi tên bằng chữ; cột kết quả để trống. Năm 2 theo thứ tự từ trái sang phải trước mở ngoặc lồng; notes ghi từng trạng thái.
- **Kết nối vào–ra:** Ngưỡng→hợp phép biến đổi; họ Hamming cho vết chạy cụ thể của hàm cơ sở.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: (a) $1-(1-p^2)^3$; (b) $[1-(1-p)^3]^2$; (c) $[1-(1-p^2)^2]^2$; (d) đặt $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$, kết quả là $q_3^2$. Mỗi tầng AND nâng xác suất của tầng trước lên lũy thừa, mỗi tầng OR lấy bù của tích các bù. Tiêu chí: giữ đúng thứ tự ghép, lấy bù đúng ở OR, nhân đúng ở AND.
- **Nguồn:** B Bài 3.6.1(a–d), §3.6.4, tr.108/PDF 37.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.22. **Thời lượng:** 10 phút (trước 10 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Bài tập:; bảng bốn ý thành bốn dòng (a)–(d). Âm tiết mặt trang 64 → 43. Tiêu đề cũ: “Xác suất qua nhiều tầng ghép”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: nguồn "MMDS" thay "MMDS 3e". Âm tiết mặt trang 54 → 53.

#### lec06-s07-04 — Bài tập: hàm chọn tọa độ trên bốn vector

- **Mục đích và vai trò:** Liệt kê hàm Hamming nhận từng cặp của bốn vector.
- **Thông điệp:** Mỗi cặp được nhận bởi đúng các tọa độ mà nó trùng.
- **Nội dung công khai dự kiến:** Câu hỏi: Họ gồm sáu hàm $h_i(x)=x_i$, $i=1,\ldots,6$. Vector 1 2 3 4 5 6 A 0 0 0 0 0 0 B 1 1 0 0 1 1 C 0 1 0 1 0 1 D 0 1 1 1 0 0 Xác định các hàm làm từng cặp thành ứng viên: AB, AC, AD, BC, BD, CD. Sản phẩm: sáu tập chỉ số.
- **Đầu vào và giả thiết:** HT8; chỉ số 1–6; cùng $i$ ở hai vector.
- **Dữ kiện, hình thức hóa và vết chạy:** R3; giữ 4 vector nguồn, đổi tên nhãn A–D để phân biệt mã đối tượng và giá trị.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Trái 45% bảng 4 × 6 bit; phải 55% danh sách 6 cặp có chỗ ghi tập chỉ số. Năm 2 đối chiếu thẳng cột, tránh chỉ đếm Hamming mà thiếu tên hàm.
- **Kết nối vào–ra:** Biểu thức ghép→phép thử hữu hạn; chữ ký dấu thay phép đọc tọa độ bằng tích vô hướng.
- **Diễn giải học thuật, lời giải và tiêu chí:** Đáp án: AB: $\{3,4\}$; AC: $\{1,3,5\}$; AD: $\{1,5,6\}$; BC: $\{2,3,6\}$; BD: $\{2\}$; CD: $\{1,2,4,5\}$. Hàm $h_i$ làm một cặp thành ứng viên khi hai vector trùng ở vị trí $i$; số hàm của mỗi cặp bằng $6-d_H$. Sách cho bốn vector dạng chuỗi 000000, 110011, 010101, 011100; tên A–D chỉ để gọi cặp. Tiêu chí: đủ sáu cặp, đánh chỉ số từ 1 và so cùng vị trí.
- **Nguồn:** B Bài 3.7.1, §3.7.6, tr.113/PDF 42; nhãn A–D chỉ thay cách gọi.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.23. **Thời lượng:** 6 phút (trước 6 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: bảng 4 × 6 thành một dòng KaTeX với tên vector chữ đứng. Âm tiết mặt trang 38 → 32. Tiêu đề cũ: “Hàm chọn tọa độ trên bốn vector”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: nguồn "MMDS" thay "MMDS 3e"; tên vector A–D giữ theo sách. Âm tiết mặt trang 33 → 32.

#### lec06-s07-05 — Bài tập: chữ ký dấu của ba vector

- **Mục đích và vai trò:** Tính đủ chữ ký và đối chiếu góc thật cho Bài 3.7.2.
- **Thông điệp:** Bốn phép thử cố định cho một ước lượng góc có thể sai lệch.
- **Nội dung công khai dự kiến:** Câu hỏi: $v_1=(1,1,1,-1)$ $v_2=(1,1,-1,1)$ $v_3=(1,-1,1,1)$ $v_4=(-1,1,1,1)$ $x=(2,3,4,5),\ y=(-2,3,-4,5),\ z=(2,-3,4,-5)$ Tính chữ ký dấu của cả ba vector. Với mỗi cặp, tính góc ước lượng từ chữ ký và góc thật. Quy ước $\operatorname{sign}(0)=+1$. Sản phẩm: bảng tích/dấu và bảng ba cặp góc.
- **Đầu vào và giả thiết:** Cơ chế chữ ký dấu; quy tắc dấu tại 0 là +1; máy tính hỗ trợ arccos.
- **Dữ kiện, hình thức hóa và vết chạy:** R4 giữ nguyên ba vector và bốn pháp tuyến. Đây là mẫu dấu cố định, không được gán phân phối đẳng hướng.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Dữ kiện bốn pháp tuyến ở trên theo nhóm 2 × 2; ba vector ở giữa; nhiệm vụ ở đáy. Sinh viên năm 2 cần đủ dữ kiện trên một trang; các bảng kết quả thuộc notes để giữ khả năng đọc.
- **Kết nối vào–ra:** Băm tọa độ cung cấp chữ ký rời rạc; tích vô hướng cung cấp chữ ký dấu; bài kế tiếp dùng phép chiếu để gán thùng Euclid.
- **Diễn giải học thuật, lời giải và tiêu chí:** Tích với $v_1,\ldots,v_4$: $x$ cho $(4,6,8,10)$, $y$ cho $(-8,10,-4,6)$, $z$ cho $(8,-10,4,-6)$. Chữ ký lần lượt là $(+,+,+,+)$, $(-,+,-,+)$ và $(+,-,+,-)$. Góc ước lượng của các cặp $xy$, $xz$, $yz$: $90^\circ$; $90^\circ$; $180^\circ$. Góc thật: $\cos\theta=14/54$, $-14/54$, $-1$, tức xấp xỉ $74{,}97^\circ$; $105{,}03^\circ$; $180^\circ$. Tiêu chí: tính đúng tích và dấu, dùng cùng bốn pháp tuyến, chuẩn bình phương bằng 54 và đổi radian sang độ rõ ràng.
- **Nguồn:** B Bài 3.7.2(a–c) và câu hỏi chung, §3.7.6, tr.113–114/PDF 42–43.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.24. **Thời lượng:** 10 phút (trước 10 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Bài tập:; ex-note quy ước dấu thành dòng Quy ước. Âm tiết mặt trang 39 → 29. Tiêu đề cũ: “Chữ ký dấu và góc giữa ba vector”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: B11: nguồn "MMDS" thay "MMDS 3e". Âm tiết mặt trang 30 → 29.

#### lec06-s07-06 — Bài tập: thùng chiếu trên ba trục

- **Mục đích và vai trò:** Gán thùng ở hai độ rộng và hợp đúng theo cùng trục.
- **Thông điệp:** Độ rộng khoảng thay tập cặp ứng viên ngay cả với trục cố định.
- **Nội dung công khai dự kiến:** Câu hỏi: $z_1=(1,2,3),\ z_2=(0,2,4),\ z_3=(4,3,2)$ Ba hàm chiếu trên ba trục; khoảng $[ja,(j+1)a)$, $j\in\mathbb Z$. Gán thùng khi $a=1$. Lặp lại khi $a=2$. Tìm các cặp ứng viên trong mỗi trường hợp. Sản phẩm: hai bảng mã theo trục và hai tập cặp.
- **Đầu vào và giả thiết:** Phần giảng chỉ minh họa trục thứ nhất với a=1; hàm sàn và thùng tách theo trục đã được định nghĩa.
- **Dữ kiện, hình thức hóa và vết chạy:** R5 giữ nguyên (a–c); phần (d) chuyển sang N15. Các biên khoảng giữ nguyên sách.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Ba điểm và quy ước biên ở trên; hai bảng trống có cùng cột trục 1,2,3 ở dưới. Sinh viên năm 2 so hai độ rộng trên cùng dữ kiện; đáp án tập cặp thuộc notes.
- **Kết nối vào–ra:** Phép băm dấu dùng hướng; phép chiếu chia khoảng dùng tọa độ và độ rộng. Bài vân tay kế tiếp dùng lại phép ghép để so sai số.
- **Diễn giải học thuật, lời giải và tiêu chí:** Với $a=1$, mã của ba điểm lần lượt là $(1,2,3),(0,2,4),(4,3,2)$, chỉ có cặp $(1,2)$. Với $a=2$, các mã là $(0,1,1),(0,1,2),(2,1,1)$, cả ba cặp đều là ứng viên. Tiêu chí: dùng hàm sàn đúng tại biên, chỉ so trong cùng trục, hợp và khử lặp đúng. Ba trục cố định không tự cho bảo đảm xác suất của họ hướng ngẫu nhiên. Sách ký hiệu ba điểm là $p_1,p_2,p_3$.
- **Nguồn:** B Bài 3.7.5(a–c), §3.7.6, tr.114/PDF 43; chuyển (d) sang đọc thêm.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.25. **Thời lượng:** 8 phút (trước 8 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: tiền tố Bài tập:. Âm tiết mặt trang 41 → 30. Tiêu đề cũ: “Thùng chiếu trên ba trục”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: nhẹ: khoảng $[ka,(k+1)a)$, $k\in\mathbb Z$, bọc ngoặc để không ngắt dòng; ghi chú nêu sách viết $j$. Âm tiết mặt trang 30 → 29.
- **Lượt sửa cuối 2026-10-14 (sau hai lượt rà lại):** quyết định `sửa`: nhẹ: "mã thùng" trong ghi chú. Âm tiết mặt trang 29 → 29.

#### lec06-s07-07 — Bài tập: hai cấu trúc ghép cho vân tay

- **Mục đích và vai trò:** Tính hai loại lỗi với cùng 2048 hàm cơ sở.
- **Thông điệp:** Cùng ngân sách hàm có thể ưu tiên giảm bỏ sót hoặc giảm ứng viên giả.
- **Nội dung công khai dự kiến:** Câu hỏi: Mỗi ô có điểm đặc trưng với xác suất $0{,}2$. Với hai ảnh cùng ngón, xác suất ảnh thứ hai có đặc trưng tại ô đã có của ảnh thứ nhất là $0{,}8$. Mỗi phép thử chọn ba ô từ lưới trước khi xét ảnh; các phép thử độc lập theo mô hình. Tính xác suất nhận cặp khác ngón (ứng viên giả) và bỏ sót cặp cùng ngón của OR 2048. So với AND hai nhóm OR 1024 độc lập. Sản phẩm: bảng hai xác suất cho hai cấu trúc cùng 2048 phép thử.
- **Đầu vào và giả thiết:** Mô hình vân tay, xác suất cơ sở và AND/OR đã học; không dùng tiên quyết từ phần đọc thêm.
- **Dữ kiện, hình thức hóa và vết chạy:** R6 giữ nguyên Bài 3.8.2(a, b). Hai cấu trúc cùng 2048 phép thử; đây là trang kiểm tra tổng hợp của phần 7.
- **Bố cục, thứ tự đọc, lý do phù hợp năm 2 và giới hạn:** Giả thiết mô hình ở trên; hai sơ đồ nhóm ở giữa; hai nhiệm vụ dưới. Sinh viên năm 2 cần suy xác suất cơ sở rồi áp dụng phép ghép; không dùng giá trị đã làm tròn làm đầu vào.
- **Kết nối vào–ra:** Các phép băm cơ sở dẫn đến việc chọn cách khuếch đại; bài kết thúc bằng đánh đổi có điều kiện giữa hai loại lỗi.
- **Diễn giải học thuật, lời giải và tiêu chí:** $q_F=0{,}000064$, $q_T=0{,}004096$. OR 2048 cho xác suất nhận cặp khác ngón $1-(1-q_F)^{2048}\approx0{,}122849$ và bỏ sót $(1-q_T)^{2048}\approx0{,}000224$. AND hai nhóm OR 1024 cho $0{,}004024$ và $0{,}029680$. Cùng 2048 hàm, OR 2048 gần như không bỏ sót nhưng nhận khoảng $12\%$ cặp khác ngón; AND hai nhóm nhận khoảng 30 lần ít hơn, đổi lại bỏ sót khoảng $3\%$. Tiêu chí: suy đúng hai xác suất cơ sở, nêu độc lập, ghép đúng thứ tự, dùng giá trị chưa làm tròn và so cùng 2048 hàm.
- **Nguồn:** B Bài 3.8.2(a, b), §3.8.7, tr.121/PDF 50; kiểm tra tổng hợp.
- **Ánh xạ ghi chú:** `lec-06-topic-16` (mã cũ `N16`); số hiệu: Bài tập 06.28. **Thời lượng:** 8 phút (trước 8 phút).
- **Căn chỉnh 2026-10-14:** quyết định `sửa`: 98 âm tiết; tách giả thiết thành dòng có nhãn. Âm tiết mặt trang 98 → 73. Tiêu đề cũ: “So sánh hai cấu trúc ghép cho vân tay”. Loại bài tập: trang câu hỏi, lời giải trong ghi chú diễn giả.
- **Lượt sửa deck 2026-10-14 (năm báo cáo):** quyết định `sửa`: A2: dòng giả định độc lập của MMDS; ghi chú: không suy từ việc chọn hàm độc lập, $(1-q_T)^{2048}$ là cận dưới. Âm tiết mặt trang 75 → 77.

## Kiến trúc ghi chú bài giảng tự học

**Cập nhật 2026-10-14 (căn chỉnh văn phong, giai đoạn 1).** Ghi chú được viết lại thành một chương theo "Cấu trúc bắt buộc của một chương" trong `AGENTS.md`: tiêu đề `# Bài 06 — Tìm cặp tương đồng bằng LSH`, một đoạn giới thiệu, dòng liên kết bộ trang chiếu, Mục tiêu học tập (năm mục tiêu như trang `lec06-s01-02` dự kiến), Kiến thức tiên quyết, Bảng ký hiệu (23 dòng), Bản đồ chủ đề, các mục `## 1.`–`## 5.` ứng với mạch 1–5, Tình huống áp dụng và ứng dụng, Tóm tắt chương, Bài tập củng cố (ba mức) và Hướng dẫn đọc thêm và tài liệu tham khảo. Mỗi chủ đề có chú thích `note-topic-id` duy nhất ngay trước tiêu đề mục; số $k$ của `lec-06-topic-k` giữ số của mã N cũ, ba chủ đề 17–19 được thêm. Môi trường đánh số dùng một bộ đếm chung cho Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán (06.1–06.42) và bộ đếm riêng cho Ví dụ (06.1–06.18), Tình huống (06.1–06.4), Bài tập (06.1–06.28). Nội dung học thuật của các phiếu N dưới đây được giữ; mỗi tiêu đề phiếu ghi thêm mã chủ đề và vị trí mới. Phiếu trang deck (`data-slide-id` ↔ `note-topic-id`) được cập nhật ở giai đoạn 2.

| Mã cũ | `note-topic-id` | Mục ghi chú mới | Số hiệu trong ghi chú | Thay đổi so với phiếu cũ |
|---|---|---|---|---|
| — | `lec-06-topic-18` | Kiến thức tiên quyết | — | Thêm: Jaccard, shingle, MinHash, chữ ký, hàm băm thay hoán vị (dẫn ghi chú Bài 05 theo mục vì Bài 05 chưa đánh số), công cụ xác suất, tích vô hướng |
| N01 | `lec-06-topic-01` | 1 | Ví dụ 06.1; Định nghĩa 06.1; Nhận xét 06.2; Bài tập 06.1 | Mục 1 mở bằng kết quả Bài 05, Ví dụ 06.1, trực giác, định nghĩa; hình `quy-trinh-cap.svg` làm hình cấu trúc chương có đoạn đọc hình |
| N02 | `lec-06-topic-02` | 2.1–2.2 | Ví dụ 06.2–06.3; Định nghĩa 06.3; Thuật toán 06.4; Mệnh đề 06.5; Nhận xét 06.6; Bài tập 06.2 | Ví dụ Hình 3.7 đứng trước định nghĩa; vết chạy đứng trước giả mã; chứng minh chia năm bước; thêm "Bỏ giả thiết" và "Trong thực hành" |
| N03 | `lec-06-topic-03` | 2.3–2.4 | Ví dụ 06.4–06.5; Định lý 06.7; Hệ quả 06.8; Mệnh đề 06.9; Nhận xét 06.10; Bài tập 06.3 | Ví dụ 3.12 đứng trước định lý; định lý bốn phần; năm phản ví dụ "Bỏ giả thiết"; Bài tập 06.3 thêm câu $P_{2,1}$, $P_{1,2}$ từ trang `lec06-s02-14` |
| N04 | `lec-06-topic-04` | 2.5 | Ví dụ 06.6; Mệnh đề 06.11, 06.13; Nhận xét 06.12; Bài tập 06.4 | Bảng đếm theo cột Bước, Số lần, Chi phí mỗi lần, Đóng góp; kỳ vọng $K$, $Q$ thành mệnh đề có chứng minh |
| N05 | `lec-06-topic-05` | 3.1–3.5 | Ví dụ 06.7–06.10; Định nghĩa 06.14, 06.16, 06.18, 06.20; Mệnh đề 06.15, 06.19; Nhận xét 06.17, 06.21; Bài tập 06.5 | Chu trình rút gọn (khái niệm phụ); ví dụ trước định nghĩa; Bài tập 06.5 thêm hai câu của trang `lec06-s03-13` |
| N06 | `lec-06-topic-06` | 3.6 | Định nghĩa 06.22; Hệ quả 06.23; Ví dụ 06.11; Nhận xét 06.24; Bài tập 06.6 | Họ MinHash thành hệ quả của Mệnh đề 06.15 |
| N07 | `lec-06-topic-07` | 3.7 | Định nghĩa 06.25; Mệnh đề 06.26; Ví dụ 06.12; Nhận xét 06.27; Bài tập 06.7 | Bài tập 06.7 bỏ phần (a) trùng Bài tập 06.22, giữ AND 2 rồi OR 2 |
| N08 | `lec-06-topic-08` | 4.1 | Ví dụ 06.13; Định nghĩa 06.28; Mệnh đề 06.29; Nhận xét 06.30; Bài tập 06.8 | Bài tập 06.8 dùng dữ kiện trang `lec06-s04-11` ($x=11001$, $y=10011$), không trỏ tới bài sách |
| N09 | `lec-06-topic-09` | 4.2 | Ví dụ 06.14–06.15; Định nghĩa 06.31; Định lý 06.32; Thuật toán 06.33; Bài tập 06.9 | Ví dụ một pháp tuyến trước định nghĩa; ví dụ ba pháp tuyến trước thuật toán ước lượng góc; Bài tập 06.9 dùng dữ kiện trang `lec06-s04-11` |
| N10 | `lec-06-topic-10` | 4.3 | Ví dụ 06.16; Định nghĩa 06.34; Bổ đề 06.35; Định lý 06.36; Nhận xét 06.37; Bài tập 06.10 | Bổ đề và định lý tách khối; Bài tập 06.10 gộp câu cũ và câu $a=2$ của trang `lec06-s04-11` |
| thêm 02/10 | `lec-06-topic-17` | 4.4 | Mệnh đề 06.38; Bài tập 06.11 | Bảng đếm thành chứng minh của mệnh đề |
| N11 | `lec-06-topic-11` | 5.1 | Định nghĩa 06.39; Nhận xét 06.40; Ví dụ 06.17; Bài tập 06.12 | Mô hình trường ngày chuyển sang Tình huống 06.1 |
| N12 | `lec-06-topic-12` | 5.2 | Định nghĩa 06.41; Mệnh đề 06.42; Ví dụ 06.18; Bài tập 06.13 | Bài tập 06.13 dùng câu OR 512 của trang `lec06-s05-06`; truy vấn một–nhiều chuyển sang Tình huống 06.2 |
| N13 | `lec-06-topic-13` | 5.3 | Định nghĩa 06.43; Ví dụ 06.19; Bài tập 06.14 | Hệ quả Jaccard $0{,}75$, $0{,}25$, $1/3$ chuyển sang Tình huống 06.3 |
| — | `lec-06-topic-19` | Tình huống áp dụng và ứng dụng | Tình huống 06.1–06.4 | Thêm; Tình huống 06.1 (hàm khóa cố định) và 06.4 (pháp tuyến $\pm1$) là hai tình huống giả thiết không thỏa |
| N14 | `lec-06-topic-14` | Tóm tắt chương | — | Sáu nhiệm vụ tự kiểm chuyển thành Bài tập 06.15–06.19 và 06.27; thu hồi kho một triệu tài liệu bằng $\binom{10^6}{2}$ và giả định luyện tập $10^6$ cặp |
| N15 | `lec-06-topic-15` | Hướng dẫn đọc thêm và tài liệu tham khảo | — | Tách ba nơi: Bài 3.7.5(d) thành Bài tập 06.26; mô hình trường ngày thành Tình huống 06.1; các chỉ dẫn đọc tiếp ở mục tham khảo |
| N16 | `lec-06-topic-16` | Bài tập củng cố | Bài tập 06.15–06.30 | R1 tách thành Bài tập 06.20 (Bài 3.4.1) và 06.21 (Bài 3.4.2); R2–R6 là Bài tập 06.22–06.25 và 06.28 |

### N01 → `lec-06-topic-01`. Bài toán ứng viên (Mục 1)

Nguồn B §3.4, tr.91–92. Nhận chữ ký từ Bài 05; sản phẩm là đặc tả tìm cặp đạt ngưỡng và phân biệt bộ nhớ với số cặp. Định nghĩa các tập hữu hạn không rỗng $S_1,\ldots,S_C$, Jaccard $s$, ma trận SIG và ngưỡng $t\in[0,1]$ trước khi tính Ví dụ 3.10. Tính đủ $10^9$ byte, số cặp, giây và ngày; nêu giả định một microgiây. Trực quan là hai nhánh chi phí số cặp và chi phí mỗi cặp. Không có định lý hay thuật toán mới; không tạo đề mục chứng minh rỗng. Tự kiểm yêu cầu xác định giới hạn còn lại khi chữ ký đã vừa bộ nhớ. Đầu ra tạo nhu cầu N02.

### N02 → `lec-06-topic-02`. Phân dải, khử lặp và xác minh (Mục 2.1–2.2)

Nguồn B §§3.4.1,3.4.3, tr.92–96; dữ kiện Ví dụ 3.8, tr.85–86. Trước ví dụ, đặc tả rõ SIG $n\times C$, $b,r\in\mathbb N_{>0}$, $n=br$, khóa $(j,\text{tuple})$, ngưỡng $t\in[0,1]$, tập cặp chuẩn hóa $c<d$ và đầu ra sau xác minh. Miền các tập nguồn hữu hạn không rỗng. Khóa bảng băm được so đầy đủ; hàm băm lưu trữ không thay phép bằng toán học.

Ví dụ tự học gồm đủ các tập gốc, SIG, khởi tạo, hai bảng thùng, bốn lượt phát và hợp ba cặp, ba phép Jaccard. Dùng Hình 3.7 như ví dụ thứ hai chỉ cho điều kiện $r=3$; không điền dữ kiện chưa có. Trực quan giải thích AND trong dải và OR qua dải. Giả mã khởi tạo từ điển rỗng và tập cặp rỗng. Trong hai vòng dựng thùng, sao chép tuple thành $z$, đặt $k\leftarrow(j,z)$; nếu khóa chưa có thì tạo $B[k]\leftarrow[]$, rồi thực hiện `B[k].append(c)`. Sau đó phát cặp trong từng thùng, khử lặp, kiểm gốc và trả kết quả; không duyệt trước mọi cặp kho.

Mệnh đề tính đúng: với SIG cố định, thuật toán trả đúng những cặp đạt $t$ trong tập có một dải trùng. Chứng minh đầy đủ theo bất biến: từ điển rỗng trước dải đầu; đầu dải j chưa có khóa mang j, các dải trước được giữ; nếu khóa mới thì tạo danh sách rỗng, nếu khóa đã có thì giữ các mã trước đó, rồi mỗi lượt chèn thêm đúng mã vào khóa của nó; khi dừng, cùng thùng tương đương cùng tuple trong cùng dải; phát và hợp tạo đúng tập ứng viên; phép kiểm giữ đúng điều kiện Jaccard. Các vòng hữu hạn; $C<2$ hay thùng dưới hai phần tử không phát cặp. Tập rỗng nằm ngoài miền, không bổ sung quy ước Jaccard rỗng. Tự kiểm: giải thích cặp 14 phát hai lần nhưng chỉ kiểm một lần. Chi phí được đặt thành N04 sau khi N03 giải thích xác suất; liên kết không bỏ bước mà tránh ngắt cơ chế xác suất của sách.

### N03 → `lec-06-topic-03`. Xác suất ứng viên, ngưỡng và hai loại lỗi (Mục 2.3–2.4)

Nguồn B §3.4.2–3, tr.93–96 và Bài 3.4.2. Định nghĩa mô hình: cặp tập không rỗng cố định, các MinHash thành phần đều độc lập, so khóa chính xác. Định nghĩa ứng viên giả ở tầng sinh cặp; bỏ sót là sự kiện một cặp có Jaccard $s\ge t$ không được chọn. Sau đó chạy Ví dụ 3.12 tại $s=.8$: $.8^5=.32768$, thất bại một dải $.67232$, thất bại 20 dải $.000356058$, được chọn $.999643942$. Trực quan nối sự kiện với phép AND/OR trước hình đường xác suất.

Chứng minh đủ bốn bước $s^r$, $1-s^r$, $(1-s^r)^b$, lấy bù. Chỉ rõ nơi dùng độc lập trong dải và giữa dải; không cần độc lập giữa các cặp dữ liệu. Suy đại số $s_{1/2}=(1-2^{-1/b})^{1/r}$, so $t$ và $b^{-1/r}$; với 20 × 5 có .508695962 và .549280272. So cấu hình 20 × 5 với 10 × 10 cùng $n=100$ tại $s=.3,.8$. Giải thích sai số theo cặp, không gán diện tích đồ thị thành tỷ lệ kho. Bộ lọc theo $\widehat s$ là lựa chọn khác có thể thêm bỏ sót, không thuộc baseline. Tự kiểm yêu cầu chọn giữa hai cấu hình nếu ưu tiên giảm bỏ sót ở .8 hoặc giảm ứng viên ở .3; đầu ra nối N04 đếm công việc.

### N04 → `lec-06-topic-04`. Mô hình chi phí (Mục 2.5)

Chủ đề bổ sung đã duyệt, suy trực tiếp từ giả mã B §3.4. Định nghĩa $u_{j,z},Q,K,T_J$ và mô hình từ máy/bảng băm kỳ vọng/sao chép tuple trước phép đếm. Vết V02 cho 8 chèn,4 phát,3 kiểm; hình hoặc bảng nối từng dòng giả mã với từng số hạng. Suy $Q=\sum\binom{u_{j,z}}2$, $K\le Q$, thời gian kỳ vọng $O(nC+Q+\sum T_J)$ và bộ nhớ phụ $O(nC+K)$ ngoài SIG đầu vào. Chứng minh bằng đếm $bC$ tuple dài $r$, $Q$ lượt chèn cặp, $K$ lần kiểm; với tập đã sắp xếp, mô tả phép trộn và $T_J=O(|S_c|+|S_d|)$.

Trường hợp xấu mọi cột cùng thùng mỗi dải cho $Q=b\binom C2$, $K=\binom C2$. Một đoạn tùy chọn suy $\mathbb E[K]=\sum P(s_{cd})$ và $\mathbb E[Q]=b\sum s_{cd}^r$ bằng biến chỉ báo; nhấn tuyến tính kỳ vọng không cần độc lập cặp. Tự kiểm yêu cầu giải thích vì sao chỉ thay $Q$ bằng $K$ trong chi phí phát cặp là sai. Kết nối ra: quy trình hiện dùng Jaccard; N05 xác định các miền khoảng cách khác.

### N05 → `lec-06-topic-05`. Miền dữ liệu và các độ đo (Mục 3.1–3.5)

Nguồn B §3.5, tr.96–103. Trước các ví dụ, định nghĩa metric với miền/hàm/tiên đề; chuẩn vector $L_q$ chỉ $q\ge1$, nêu $L_1,L_2,L_\infty$. Với mỗi loại, định nghĩa trước rồi chạy đúng ví dụ nguồn: V05 tính 7,5,4; Jaccard trên tập hữu hạn không rỗng dùng cặp 14; góc trên hướng hoặc vector đơn vị dùng V06; chỉnh sửa chỉ chèn/xóa dùng V07; Hamming trên $\Sigma^D$ dùng V08. Định nghĩa dãy con và dãy con chung dài nhất trước công thức LCS. Giữ $\theta$ radian, ghi phép đổi 60°=π/3.

Chứng minh đầy đủ tam giác Jaccard bằng cùng MinHash: bao hàm sự kiện rồi chặn hợp; không cần độc lập. Chứng minh công thức chỉnh sửa bằng hai cận: dựng phép xóa/chèn theo LCS; mọi kịch bản sửa giữ một dãy con chung nên không thể giữ quá $L$. Từ phép nối kịch bản sửa suy tam giác; đảo kịch bản cho đối xứng. Hamming chứng minh theo tọa độ rồi cộng. Góc có phác thảo hình học đường trên mặt cầu đơn vị, ghi đúng mức phác thảo; không nhận nó là metric trên toàn vector khác 0. Tính metric của chuẩn được phát biểu theo nguồn, không thêm chứng minh Minkowski ngoài tiên quyết.

Không có thuật toán mới cho từng định nghĩa, vì vậy không tạo giả mã DP. Có thể đếm $O(D)$ để tính chuẩn/Hamming/góc trên vector đặc, $O(|A|+|B|)$ với tập sắp xếp; không tự gán chi phí tính LCS khi chưa trình bày thuật toán. Tự kiểm phân biệt cosin với góc và chỉnh sửa chèn/xóa với Hamming. N05 cấp miền/đơn vị cho N06.

### N06 → `lec-06-topic-06`. Họ nhạy cảm theo khoảng cách (Mục 3.6)

Cập nhật 2026-10-14: thêm Nhận xét 06.24 (bộ tham số là cận, không là xác suất của từng cặp) sau Ví dụ 06.11; các số hiệu dùng chung từ 06.24 trở đi tăng một.

Nguồn B §3.6.1–2, tr.103–105. Nêu nhu cầu diễn đạt một phép thử cho nhiều miền dữ liệu. Định nghĩa $\mathcal H$ kèm phân phối, cặp cố định, cùng $h$, miền tham số và hai cận trước Ví dụ 3.18. Với Jaccard, $0\le d_1<d_2\le1$ cho họ $(d_1,d_2,1-d_1,1-d_2)$; Ví dụ 3.18 cho (.3, .6, .7, .4). Đồ thị ba miền không áp một dạng đường cụ thể cho mọi họ.

Lập luận ví dụ chỉ dùng $P=1-d_J$ và tính đơn điệu; không gọi đó là bằng chứng mọi họ có equality. Không có thuật toán mới; việc lấy mẫu một hàm được nêu là hợp đồng xác suất. Tự kiểm dùng d=.2, .5, .8 và giải thích vùng giữa không ràng buộc. Đầu ra là bộ cận để N07 biến đổi.

### N07 → `lec-06-topic-07`. Phép ghép AND và OR (Mục 3.7)

Nguồn B §3.6.3, tr.105–108. Định nghĩa cặp được nhận, các phép thử độc lập và phép ghép trước Ví dụ 3.19–20. AND lưu tuple và nhận khi tất cả trùng; OR nhận khi ít nhất một bảng trùng. Chạy trung gian $p^4$ hoặc $1-(1-p)^4$ rồi lớp ghép thứ hai cho $p=.8,.4$; giữ cận .878497449/.098534519 so .993615344/.573951942.

Chứng minh hai công thức đầy đủ bằng giao độc lập và bù; chuyển cận theo tính đơn điệu. Phân biệt xác suất đúng bằng $p$ của một cặp với các cận gần/xa của họ. Diễn đạt OR như quan hệ cặp vì quan hệ này nói chung không bắc cầu; không biến OR thành equality của một hashvalue. Giả mã ngắn cho AND_r rồi OR_b thể hiện tính hàm, nhóm tuple, tra bảng và hợp cặp, dẫn lại N02 thay lặp toàn thuật toán. Với OR rồi AND, mỗi nhóm OR hợp cặp qua các bảng cơ sở, sau đó lấy giao các tập cặp của những nhóm OR. Quan hệ OR không được mã hóa bằng phép bằng nhau của tuple. Chi phí số hàm bằng tích các kích thước nhóm; chi phí phát cặp vẫn phụ thuộc $Q$. Tự kiểm dùng bốn chuỗi Bài 3.6.1 và giải thích hai thứ tự có cùng 16 hàm nhưng khác đánh đổi. N08–N10 thay họ cơ sở mà giữ phép ghép.

### N08 → `lec-06-topic-08`. Họ Hamming (Mục 4.1)

Nguồn B §3.7.1, tr.109. Định nghĩa vector cùng chiều $D>0$, $I$ đều và $h_I(x)=x_I$ trước V08. Ví dụ liệt kê vị trí 1,3 trùng và 2,4,5 khác; hình hai hàng bit cho xác suất 2/5. Mệnh đề $P=1-d_H/D$ được chứng minh bằng đếm số chỉ số thuận lợi. Nêu lựa chọn chỉ số có hoàn lại cho nhiều thử độc lập. Thuật toán lấy $I$, đọc một tọa độ, trả giá trị; dừng sau một lần đọc. Chi phí $O(1)$ mỗi thử với mảng, trữ một chỉ số; $m$ thử cần $m$ chỉ số và $m$ giá trị mỗi đối tượng. Tự kiểm Bài 3.7.1 có lời giải trong N16. Nối sang N09 khi tọa độ rời rạc được thay bởi hướng.

### N09 → `lec-06-topic-09`. Siêu phẳng và chữ ký dấu (Mục 4.2)

Nguồn B §§3.7.2–3, tr.109–111; hình đối chiếu S4 PDF 48–49. Định nghĩa siêu phẳng qua gốc, pháp tuyến, hàm dấu với sign (0)=+1 và góc $\theta\in[0,\pi]$ trước V10. Trước ví dụ, nêu xác suất khác dấu bằng theta/pi trong mô hình đẳng hướng và định nghĩa quy tắc ước lượng bằng pi nhân tỷ lệ bit khác; nêu căn cứ hai miền góc tách. Sau đó dùng 3 pháp tuyến dấu cố định để chạy đủ sáu tích, tạo chữ ký và góc 120°; tính góc thật 38.047579°. Trực quan phân biệt pháp tuyến với đường phân chia.

Sau ví dụ, trở lại mô hình pháp tuyến đẳng hướng đã nêu để chứng minh mệnh đề $P=1-\theta/\pi$. Xử lý riêng $\theta=0$ cho xác suất trùng 1 và $\theta=\pi$ cho xác suất trùng 0. Khi $0<\theta<\pi$, hai vector không cùng phương; chứng minh chiếu về mặt phẳng sinh bởi chúng, đếm tổng góc tách $2\theta$ trên $2\pi$, rồi lấy bù. Họ góc chỉ dùng $0\le d_1<d_2\le\pi$. Thuật toán $m$ bit dùng cùng $m$ pháp tuyến cho mọi đối tượng; vector đặc cho $O(mD)$ phép tính và $m$ bit/đối tượng, pháp tuyến dùng $O(mD)$ từ. Phân phối dấu ±1 không đẳng hướng; toàn 16 vector dấu của Ex 3.22 cho 45° với quy tắc 0 đã chốt, tách nguồn sai số phân phối với mẫu. Tự kiểm tính dấu Bài 3.7.2 và nêu giả thiết của định lý. N10 giữ thao tác tích vô hướng nhưng dùng độ lớn hình chiếu.

### N10 → `lec-06-topic-10`. Chiếu Euclid và chia khoảng (Mục 4.3)

Nguồn B §§3.7.4–5, tr.111–113; Datar §3.2 PDF 3 chỉ cho cơ chế dịch. Định nghĩa trong mặt phẳng:$a>0$, $u$ đều hướng đơn vị,$\delta$ độc lập đều trên $[0,a)$,$h=\lfloor(u\cdot x+\delta)/a\rfloor$. Sau định nghĩa, tách ví dụ thực thi xác định của Bài 3.7.5: ba điểm/ba trục với $a=1,2$; có thể dẫn bài tập trước rồi cung cấp lời giải gập ở N16 để tài liệu tự học đọc độc lập. Không áp bảo đảm ngẫu nhiên cho ba trục cố định.

Hình chiếu có biên $ka-\delta$, khoảng nửa mở và độ dài $\ell$. Chứng minh xác suất theo $\delta$ bằng độ dài khoảng biên tách; xét $\ell=0$, $0<\ell<a$, $\ell\ge a$. Chứng minh cận gần bằng $\ell\le\rho\le a/2$; cận xa bằng điều kiện cần $\rho|\cos\phi|<a$ và góc nhọn đều hai chiều. Phát biểu $(a/2,2a,1/2,1/3)$ chỉ hai chiều. Đây là suy luận bản soạn bổ sung giả thiết MMDS, không gán cận cho bài báo p-stable. Thuật toán tính tích vô hướng, cộng $\delta$, chia $a$, lấy sàn rồi dùng khung N02/N07; dừng hữu hạn, chi phí vector đặc $O(D)$ mỗi thử. Tự kiểm phân biệt gần về hình chiếu với chung thùng và điều kiện theo số chiều. N11 bắt đầu vận dụng chọn biểu diễn/quy tắc.

### N11 → `lec-06-topic-11`. Đối sánh thực thể (Mục 5.1)

Cập nhật 2026-10-14: thêm Ví dụ 06.17 (thang điểm 300 của §3.8.2, tr.115–116; khoảng cách chỉnh sửa Bill/William bằng 5) sau Nhận xét 06.40; Tình huống 06.1 thêm kết luận theo khung tr.117 (185 điểm: $f\approx1$; 115 điểm: $f>0$).

Nguồn B §§3.8.1–3, tr.114–117. Định nghĩa hai nguồn hồ sơ, đối tượng thực thể và ứng viên trước ví dụ hai tập một triệu bản ghi. Các trường tên/địa chỉ/điện thoại giữ nguyên nguồn. Mô tả ba bảng khóa, hợp cặp, khử lặp, chấm điểm đầy đủ; không tự tạo bảng hồ sơ nhân khẩu. Trực quan là luồng ba khóa chảy vào hợp cặp. Chứng minh theo cơ chế chỉ bảo đảm mọi cặp khớp ít nhất một trường được đưa vào ứng viên; không suy đồng nhất thực thể. Không có phân phối đủ để phát biểu họ bốn tham số; không giả định các trường độc lập.

Chi phí đối chiếu toàn bộ hai nguồn là $10^{12}$ cặp; phương án nhóm vẫn phụ thuộc tổng kích thước thùng và chi phí chấm điểm. Nêu trường phụ không dùng chấm điểm có thể kiểm chất lượng tập kết quả, còn công thức ngày được chuyển N15. Tự kiểm giải thích khớp điện thoại chưa đủ xác nhận cùng người. N12 cung cấp ví dụ có mô hình xác suất rõ.

### N12 → `lec-06-topic-12`. Đối sánh vân tay (Mục 5.2)

Nguồn B §§3.8.4–5/Ex 3.23, tr.117–120. Định nghĩa ảnh chuẩn hóa, tập ô có đặc trưng và phép thử chọn ba ô từ lưới trước khi xét ảnh. Thùng chung chỉ dành cho ảnh chứa cả ba ô; ảnh thiếu ô nhận thùng đơn riêng. Nêu khác nhau của truy vấn một ảnh với kho và tìm cặp trong kho; không thêm quy trình nhận dạng ảnh.

Ví dụ mô hình 0.2/0.8 nêu rõ độc lập. Tính xác suất cả hai ảnh có đủ ba ô:$q_F=.2^6$,$q_T=(.2\cdot.8)^3$; không điều kiện hóa rằng ảnh truy vấn đã chứa ba ô. Trực quan tách tầng một ô, ba ô, nhiều thử. Suy OR 1024 và AND hai nhóm bằng công thức đã chứng minh; giữ số chưa làm tròn. Thuật toán cơ sở và khung ghép từ N07 được áp dụng; xác minh vân tay nằm sau ứng viên và có chi phí riêng, không gán $O(1)$. Tự kiểm Bài 3.8.2 so hai phương án cùng 2048 hàm. N13 đổi biểu diễn văn bản để kiểm ý nghĩa tương đồng.

### N13 → `lec-06-topic-13`. Bản tin gần trùng (Mục 5.3)

Nguồn B §3.8.6/Ex 3.24, tr.120–121. Định nghĩa bài toán nhóm trang xuất phát từ cùng văn bản với phần bao quanh khác; phân biệt cùng chủ đề. Định nghĩa từ dừng là từ rất thường gặp, nêu danh sách I, that, you, for, your. Đặc tả shingle là một token từ dừng và hai token tiếp theo; mật độ từ dừng cao trong văn xuôi giải thích lựa chọn đặc trưng. Câu ngắn “Buy Sudzo.” có 0 shingle; câu dài có bốn shingle xác định và một shingle phụ thuộc token kế tiếp $x$ chưa được cho. Câu dài cũng có thể là lời quảng cáo; quy tắc ưu tiên văn xuôi, không bảo đảm loại mọi quảng cáo. Không tạo token sau laundry.

Hình đối chiếu văn bản chính và phần bao quanh chỉ là quan hệ khái niệm. Mệnh đề học thuật ở mức quy tắc biểu diễn, không là định lý về mọi trang web; không biến dự đoán 75%/25% thành thực nghiệm. Dùng lại thuật toán shingle/MinHash/LSH, kèm chi phí phụ thuộc số token và $Q,K$, không phân tích mô hình chưa có. Tự kiểm xác định đối tượng đầu ra và giải thích vì sao câu quảng cáo dài của nguồn vẫn tạo shingle. Thay nhiệm vụ bình luận thao tác dịch bằng nhiệm vụ ứng dụng s05-06 đã có; lý do giữ token thuộc review-log. N14 thu hồi toàn quy trình.

### N14 → `lec-06-topic-14`. Tổng hợp và tự kiểm (Tóm tắt chương)

Nguồn §§3.4–3.8. Mở bằng đầu ra đã có và sơ đồ lựa chọn biểu diễn→độ đo→họ→ghép→ứng viên→xác minh. Thu hồi triệu tài liệu, không tự ước lượng số cặp được giảm. Liên hệ $P,Q,K,T_J$, bảo đảm trong tập ứng viên và khả năng bỏ sót cặp có Jaccard $s\ge t$. Không có định nghĩa, thuật toán hoặc chứng minh mới; ghi rõ “không áp dụng” trong kế hoạch này vì đây là tổng hợp. Sáu nhiệm vụ s06-03/04 có lời giải gập, đo đủ MT1–MT6. Kết nối Bài 07 theo tiêu chí chất lượng/thời gian/bộ nhớ, không dạy HNSW/PQ.

### N15 → `lec-06-topic-15`. Đọc thêm có giới hạn (tách ba nơi, xem bảng trên)

Chọn hai mục triển khai ngắn; chúng không cấp tiên quyết cho recitation. Mục thứ nhất giải Bài 3.7.5(d), tr.114: cặp 12 luôn chung ở trục 2 nên ứng viên với mọi $a>0$; cặp 13 và 23 thành ứng viên khi $a\in(3/2,2]\cup(3,\infty)$. Lời giải xét điều kiện hàm sàn trên các cặp tọa độ và hợp các khoảng; kiểm riêng các biên 3/2,2,3. Mục thứ hai giải thích mô hình kiểm thực thể bằng ngày của §3.8.3, tr.116–117: độ trễ là ngày tạo hồ sơ B trừ ngày tạo hồ sơ A, lọc 0–90 ngày; giả thiết độ trễ ngẫu nhiên đều làm rõ trung bình 45 ngày. Nhóm đạt điểm tối đa 300 được giả định khớp đúng và có trung bình 10 ngày; nhóm cùng mức điểm được xét có trung bình $x$; mô hình hỗn hợp $x=10f+45(1-f)$ cho $f=(45-x)/35$. Nêu giả thiết đại diện của hai nhóm và không dùng để kết luận từng cặp.

MapReduce Bài 3.4.4, tr.96; ghép 256 Ví dụ 3.21, tr.108; điểm bất động/đạo hàm Bài 3.6.2–4, tr.108; mở rộng Euclid §3.7.5, tr.113 chỉ nằm danh mục đọc tiếp kèm mục đích, không soạn thêm chương hoặc chứng minh. Không thêm nội dung §3.9, HNSW, PQ, RAG. Phạm vi chọn gọn tránh làm tài liệu tự học tăng độ dài mà không tạo đầu ra cần thiết.

### N16 → `lec-06-topic-16`. Bài tập và lời giải (Bài tập củng cố)

Cập nhật 2026-10-14 (lượt sửa ghi chú theo hai báo cáo rà): thêm Bài tập 06.29 (chọn $(b,r)$ cho $t=0{,}6$ trong bốn cấu hình $br=100$, kiểm mục tiêu 2) và Bài tập 06.30 (chứng minh biến thể $b$ bảng cho $\mathrm{CAND}=\mathcal C$ và phản ví dụ một bảng không có số dải, kiểm mục tiêu 1) ở cuối Mức vận dụng; hai bài chỉ có trong ghi chú, không thêm trang chiếu.

Sáu cụm nguồn, R1–R6, giữ toàn dữ kiện/yêu cầu và tổng 60 phút như phiếu s07-01–07. Mỗi bài có khối exercise, hint, solution không lồng nhau; hint/solution gập mặc định, dùng bàn phím và mở khi in. Dữ kiện đề xuất hiện đầy đủ để người đọc không phải mở slide. Các lời giải dưới đây chuyển vào tài liệu, không chỉ tham chiếu storyboard. Tiêu chí đánh giá nêu bước toán học và lỗi cụ thể, không chứa lời điều phối lớp. Việc chia bài 3.4.1–2 thành hai trang và chuyển 3.7.5(d) sang đọc thêm là hai điều chỉnh, được ghi trong log.

### Thêm 02/10 → `lec-06-topic-17`. Chi phí tính chữ ký ba họ (Mục 4.4)

Chủ đề bổ sung đã thêm trong lượt duyệt ngày 02/10, nay mang mã riêng. Mô hình đếm: vector đặc $D$ chiều, mỗi số một từ máy. Mệnh đề 06.38 đếm phép tính của một hàm cho ba họ ($O(1)$, $O(D)$, $O(D)$), suy ra $O(Cm)$ hoặc $O(CmD)$ cho chữ ký và $O(m)$ hoặc $O(mD)$ từ cho tham số; vector thưa thay $D$ bằng $\mathrm{nnz}(x)$. Kết nối vào: ba họ của Mục 4.1–4.3; kết nối ra: chi phí phân dải của Mệnh đề 06.11 cộng thêm. Bài tập 06.11 giữ dữ kiện $C=10^6$, $D=1000$, $m=200$.

### Thêm 2026-10-14 → `lec-06-topic-18`. Kiến thức tiên quyết

Chủ đề cầu nối. Ghi chú Bài 05 chưa đánh số hiệu, nên mọi kết quả được dẫn theo mục ("ghi chú Bài 05, Mục k") và phát biểu lại trong một đến hai câu: Jaccard (Mục 2), shingle (Mục 3), MinHash và định lý xác suất trùng (Mục 5–6), chữ ký và ước lượng (Mục 7), hàm băm thay hoán vị (Mục 9, 11); công cụ xác suất (bù, độc lập, chặn hợp, tuyến tính kỳ vọng) và tích vô hướng, Cauchy–Schwarz. Sản phẩm: mọi kết quả nhắc lại ở các mục sau có chỗ dẫn.

### Thêm 2026-10-14 → `lec-06-topic-19`. Tình huống áp dụng và ứng dụng

Chủ đề cốt lõi theo yêu cầu "Tình huống áp dụng" của `AGENTS.md`. Bốn khối `application`, mỗi khối có bài toán và dữ liệu, mô hình hóa, kiểm giả thiết, áp dụng, chi phí, diễn giải, giới hạn và dẫn ngược số hiệu: Tình huống 06.1 (đối sánh hồ sơ và kiểm bằng trường ngày, §3.8.2–3.8.3; giả thiết không thỏa vì hàm khóa cố định), 06.2 (truy vấn vân tay một–nhiều, §3.8.5), 06.3 (bản tin gần trùng, §3.8.6), 06.4 (pháp tuyến $\pm1$, §3.7.3 và Ví dụ 3.22; giả thiết đẳng hướng không thỏa, $120^\circ$, $45^\circ$ so với $38{,}05^\circ$). Không có số liệu mới ngoài số đã kiểm. Danh mục ứng dụng dẫn Bài 07, Bài 02 (MapReduce qua Bài 3.4.4) và Bài 05.

## Lời giải recitation cần triển khai đầy đủ

### R1. Bài 3.4.1–2, tr.96, 18 phút

| $s$ | $r=3,b=10$ | $r=6,b=20$ | $r=5,b=50$ |
|---:|---:|---:|---:|
|0.1|0.009955120|0.000020000|0.000499878|
|0.2|0.077180588|0.001279222|0.015875200|
|0.3|0.239448893|0.014479467|0.114539882|
|0.4|0.483870732|0.078809323|0.402283952|
|0.5|0.736924424|0.270187144|0.795550630|
|0.6|0.912267475|0.615414636|0.982533828|
|0.7|0.985015105|0.918185997|0.999898996|
|0.8|0.999234054|0.997712125|0.999999998|
|0.9|0.999997864|0.999999740|xấp xỉ 1|

Từ $1-(1-s^r)^b=1/2$ suy $(1-s^r)^b=1/2$, $s^r=1-2^{-1/b}$ và $s=(1-2^{-1/b})^{1/r}$. Theo ba cấu hình: nghiệm chính xác $.406088134,.569353387,.424394480$; xấp xỉ $.464158883,.606962231,.457305052$. Cả ba xấp xỉ đều lớn hơn nghiệm. Điểm cuối bảng làm tròn về 1, không phát biểu xác suất bằng 1 chính xác. Tiêu chí: đúng công thức, đủ 27 ô, đủ 3 cặp ngưỡng, phân biệt $r,b$; không biến $t$ do người dùng chọn thành nghiệm $P=1/2$.

### R2. Bài 3.6.1(a–d), tr.108, 10 phút

(a) $p\to p^2\to1-(1-p^2)^3$. (b) $p\to1-(1-p)^3\to[1-(1-p)^3]^2$. (c) $p\to p^2\to1-(1-p^2)^2\to[1-(1-p^2)^2]^2$. (d) $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$, kết quả $q_3^2$. Mỗi tầng lấy các bản thử độc lập. Các số hàm 6,6,8,16 chỉ là phép kiểm phụ của người soạn, không bổ sung yêu cầu ngoài đề nguồn.

### R3. Bài 3.7.1, tr.113, 6 phút

| Cặp | Chỉ số hàm tạo ứng viên | Số tọa độ khác để đối chiếu |
|---|---|---:|
|A, B|3,4|4|
|A, C|1,3,5|3|
|A, D|1,5,6|3|
|B, C|2,3,6|3|
|B, D|2|5|
|C, D|1,2,4,5|2|

Sản phẩm phải liệt kê hàm, chứ chỉ báo khoảng cách chưa trả lời đủ đề. Nhãn A–D chỉ thay cách gọi bốn vector, không đổi bit.

### R4. Bài 3.7.2, tr.113–114, 10 phút

| Vector | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký dấu |
|---|---|---|
|$x=(2,3,4,5)$|$(4,6,8,10)$|$(+,+,+,+)$|
|$y=(-2,3,-4,5)$|$(-8,10,-4,6)$|$(-,+,-,+)$|
|$z=(2,-3,4,-5)$|$(8,-10,4,-6)$|$(+,-,+,-)$|

Bình phương chuẩn đều 54; tích $xy=14,xz=-14,yz=-54$. Góc thật là $\arccos(7/27)\approx74.973886^\circ$, $\arccos(-7/27)\approx105.026114^\circ$ và $\pi=180^\circ$. Góc ước lượng là $\pi(2/4)=\pi/2=90^\circ$ cho hai cặp đầu và $\pi(4/4)=\pi$ cho cặp cuối. Đây là vết tính bốn pháp tuyến cố định, không bảo đảm ước lượng chính xác cho mọi vector.

### R5. Bài 3.7.5(a–c), tr.114, 8 phút

| $a$ | Mã $p_1$ theo ba trục | Mã $p_2$ | Mã $p_3$ | Cặp ứng viên |
|---:|---|---|---|---|
|1|$(1,2,3)$|$(0,2,4)$|$(4,3,2)$|$(1,2)$|
|2|$(0,1,1)$|$(0,1,2)$|$(2,1,1)$|$(1,2),(1,3),(2,3)$|

Mỗi mã là $\lfloor x_i/a\rfloor$. Chỉ so cùng trục; mã 2 ở trục 2 không phải cùng khóa với mã 2 ở trục 3. Giá trị $a$ thuộc $[a,2a)$, không thuộc $[0,a)$. Phần (d) chuyển N15; phần giảng chỉ minh họa trục 1 với $a=1$ nên không giải sẵn cả bài.

### R6. Bài 3.8.2(a, b), tr.121, 8 phút

$q_F=(.2^2)^3=.000064$ và $q_T=(.2\cdot.8)^3=.004096$. Với OR 2048:

$$
P_F=1-(1-q_F)^{2048}\approx.122849062,\qquad
P_{\rm miss}=(1-q_T)^{2048}\approx.000223559.
$$

Với hai nhóm OR 1024 độc lập ghép AND:

$$
P_F=[1-(1-q_F)^{1024}]^2\approx.004024207,\qquad
P_{\rm miss}=1-[1-(1-q_T)^{1024}]^2\approx.029680224.
$$

OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn; cấu trúc AND giảm ứng viên giả và tăng bỏ sót. Các xác suất thuộc mô hình nguồn với ba ô được chọn từ lưới trước khi xét ảnh. Hai phương án cùng 2048 phép thử. Không tính từ .063 hoặc .985 đã làm tròn.

## Đặc tả tài sản và kiểm định pha sau

Hình dự kiến thuộc `2627-1/img/lec-06/`: luồng biểu diễn–ứng viên; dải/thùng; dải 3 hàng; đồ thị xác suất; miền gần–giữa–xa; cấu trúc AND/OR; chuẩn vector; siêu phẳng; chiếu Euclid; khóa thực thể; lưới vân tay khái niệm. Được gộp hình theo chức năng nếu vẫn truy được quan hệ. Các bảng giá trị dùng HTML/Markdown, không vẽ chữ nhỏ trong SVG. Mỗi SVG có role=img, title/description và alt cụ thể; tọa độ/trọng số/nhãn khớp nguồn. Nếu dùng script sinh SVG, lưu mã tái tạo cùng tài sản.

Pha 1 chỉ kiểm được đặc tả và dữ kiện. Gate đã đối chiếu từng phiếu, trình tự, thời lượng, giả thiết, mặt trang dự kiến và note-topic; bốn sửa nhẹ sau PASS đã được điều phối viên xác nhận. Pha 2 cần kiểm Reveal thực, KaTeX, SVG, notes, đường dẫn, offline, khung rộng/hẹp, bàn phím, in, viewer và hồi quy CSS 02/03 nếu thay CSS chung. Năm reviewer độc lập và editor riêng là bước sau bản nháp. Không đánh dấu render hoặc phát hành đạt tại pha 1.

## Đồng bộ sau năm báo cáo độc lập

Lượt editor giữ 60 trang và thứ tự cũ, bảy phần, 120 phút giảng + 60 phút recitation. Chỉ s01-02 đổi tiêu đề thành “Nội dung và mục tiêu”; ba năng lực gộp MT1–MT6. Mục tiêu mở đầu thay đổi nên cần tái rà mạch toàn tuyến. Các phần thêm là định nghĩa/cầu nối và nhiệm vụ đã duyệt, không mở chủ đề hoặc bài tập nguồn mới.

| Chủ đề | Tự kiểm được thực hiện trong ghi chú | Vị trí đáp án |
|---|---|---|
| N01 | Giới hạn số cặp và tập trung gian trước Jaccard | Khối solution cuối mục bài toán |
| N02 | Cặp (1,4) phát hai lần nhưng kiểm một lần | Khối solution cuối mục phân dải |
| N03 | Chọn cấu hình tại s=.8 và s=.3 | Giữ khối exercise/solution đã có |
| N04 | Phân biệt Q=4 với K=3 khi đếm chi phí phát | Khối solution cuối mục chi phí |
| N05 | Cosin/góc; căn chỉnh Hamming/chỉnh sửa | Khối solution cuối mục độ đo |
| N06 | Đọc cận họ tại d=.2,.5,.8 | Khối solution ngay trước phép ghép |
| N07 | Bốn chuỗi Bài 3.6.1; so hai thứ tự cùng 16 phép thử | Liên kết đến bài nguồn và lời giải gập; giải thích cục bộ |
| N08 | Tập chỉ số của Bài 3.7.1 | Liên kết rõ đến đề/lời giải gập cuối tài liệu |
| N09 | Bài 3.7.2 và giả thiết xác suất góc | Liên kết bài nguồn; solution cục bộ về giả thiết |
| N10 | ell<a chưa bảo đảm chung thùng; nguồn ngẫu nhiên/số chiều | Khối solution cuối mục Euclid |
| N11 | Khớp điện thoại chưa xác nhận cùng người | Khối solution cuối mục thực thể |
| N12 | Hai cấu trúc cùng 2048 phép thử, Bài 3.8.2 | Liên kết rõ đến đề/lời giải gập cuối tài liệu |
| N13 | Cùng văn bản/cùng chủ đề; quảng cáo dài có từ dừng | Khối solution cuối mục bản tin |
| N14 | Sáu nhiệm vụ tổng hợp | Giữ khối solution hiện có |
| N15 | Hai nhánh đọc thêm đã có lời giải/giới hạn | Không thêm bài bắt buộc; không tính vào 60 phút recitation |
| N16 | Sáu cụm bài nguồn | Giữ nguyên dữ kiện, nhiệm vụ, lời giải và phút |

N02 và ghi chú s02-08 mô tả đúng biến thể: bỏ bước 6 kiểm chữ ký của sách, kiểm gốc bắt buộc cho mọi ứng viên; sách chỉ gắn “tùy chọn” cho bước 7 kiểm gốc. N09 định nghĩa quy tắc ước lượng trước áp dụng, nhưng vẫn dùng vết dấu trước chứng minh hình học; không đổi thứ tự trang. N10 thêm SVG tam giác và chuỗi ell=rho|cos phi| → điều kiện cần phi>pi/3; không ấn định tỷ lệ với a. N11 thu hồi khoảng cách chỉnh sửa trong điểm phạt theo trường. N12 định nghĩa đặc trưng đường vân và truy hồi hợp–hợp–giao–xác minh; không đổi điều kiện hóa của q_T,q_F. N15 giữ công thức hỗn hợp và tách rõ giả thiết đều khỏi riêng ràng buộc 0–90.

## Ánh xạ `data-slide-id` ↔ `note-topic-id` (căn chỉnh 2026-10-14)

| `data-slide-id` | Tiêu đề trang | `note-topic-id` | Số hiệu trong ghi chú | Phút |
|---|---|---|---|---:|
| `lec06-s01-01` | Tìm cặp tương đồng bằng LSH | `lec-06-topic-01` | mở chương | 0,5 |
| `lec06-s01-06` | Tiên quyết và quy ước | `lec-06-topic-18` | Kiến thức tiên quyết; Nhận xét 06.2 | 1,5 |
| `lec06-s01-02` | Mục tiêu học tập | `lec-06-topic-01` | Mục tiêu học tập | 1 |
| `lec06-s01-07` | Nội dung | `lec-06-topic-01` | — | 0,5 |
| `lec06-s01-08` | Vấn đề trung tâm | `lec-06-topic-01` | Hệ quả 06.8 (dòng 2) | 1,5 |
| `lec06-s01-03` | Ví dụ: kho một triệu tài liệu | `lec-06-topic-01` | Ví dụ 06.1 | 1,5 |
| `lec06-s01-04` | Bài toán tìm cặp tương đồng | `lec-06-topic-01` | Định nghĩa 06.1 | 2 |
| `lec06-s01-05` | Câu hỏi về bài toán tìm cặp | `lec-06-topic-01` | Bài tập 06.1; Nhận xét 06.2 | 1,5 |
| `lec06-s02-00` | 2. Phân dải chữ ký MinHash | `lec-06-topic-02` | — | 0,5 |
| `lec06-s02-01` | Dải, khóa dải và cặp ứng viên | `lec-06-topic-02` | Định nghĩa 06.3 | 1 |
| `lec06-s02-06` | Ví dụ: năm cột, dải ba hàng | `lec-06-topic-02` | Ví dụ 06.2 | 1,5 |
| `lec06-s02-02` | Ví dụ: bốn tập đặc trưng | `lec-06-topic-02` | Ví dụ 06.3 | 1,5 |
| `lec06-s02-03` | Ví dụ: bốn tập đặc trưng, thùng của dải 1 | `lec-06-topic-02` | Ví dụ 06.3 | 1,5 |
| `lec06-s02-04` | Ví dụ: bốn tập đặc trưng, hợp qua hai dải | `lec-06-topic-02` | Ví dụ 06.3 | 1,5 |
| `lec06-s02-05` | Ví dụ: bốn tập đặc trưng, xác minh | `lec-06-topic-02` | Ví dụ 06.3 | 2 |
| `lec06-s02-07` | Thuật toán: phân dải và xác minh | `lec-06-topic-02` | Định nghĩa 06.3; Thuật toán 06.4 | 1,5 |
| `lec06-s02-08` | Thuật toán: phân dải và xác minh | `lec-06-topic-02` | Thuật toán 06.4 | 3 |
| `lec06-s02-09` | Tính đúng: phân dải và xác minh | `lec-06-topic-02` | Mệnh đề 06.5 | 1,5 |
| `lec06-s02-15` | Tính đúng: phân dải và xác minh | `lec-06-topic-02` | Mệnh đề 06.5; Nhận xét 06.6 | 1 |
| `lec06-s02-10` | Xác suất trùng một dải | `lec-06-topic-03` | Ví dụ 06.4 | 2 |
| `lec06-s02-11` | Xác suất thành ứng viên | `lec-06-topic-03` | Định lý 06.7; Hệ quả 06.8 | 2 |
| `lec06-s02-12` | Đường cong S và chọn số dải | `lec-06-topic-03` | Ví dụ 06.5; Mệnh đề 06.9; Nhận xét 06.10 | 2,5 |
| `lec06-s02-13` | Chi phí: phân dải và xác minh | `lec-06-topic-04` | Mệnh đề 06.11 | 2,5 |
| `lec06-s02-16` | Chi phí: bộ nhớ và trường hợp xấu nhất | `lec-06-topic-04` | Ví dụ 06.6; Nhận xét 06.12; Mệnh đề 06.13 | 1,5 |
| `lec06-s02-14` | Câu hỏi về phân dải | `lec-06-topic-02, lec-06-topic-03` | Bài tập 06.2, 06.3 | 3 |
| `lec06-s03-00` | 3. Khoảng cách và họ nhạy cảm | `lec-06-topic-05` | — | 0,5 |
| `lec06-s03-01` | Độ đo khoảng cách | `lec-06-topic-05` | Ví dụ 06.7 | 1,5 |
| `lec06-s03-02` | Độ đo khoảng cách và chuẩn vector | `lec-06-topic-05` | Định nghĩa 06.14 | 2 |
| `lec06-s03-03` | Khoảng cách Jaccard | `lec-06-topic-05` | Mệnh đề 06.15 | 2 |
| `lec06-s03-04` | Khoảng cách góc | `lec-06-topic-05` | Định nghĩa 06.16; Ví dụ 06.8; Nhận xét 06.17 | 2 |
| `lec06-s03-05` | Khoảng cách chỉnh sửa | `lec-06-topic-05` | Ví dụ 06.9; Định nghĩa 06.18; Mệnh đề 06.19 | 2 |
| `lec06-s03-06` | Khoảng cách Hamming | `lec-06-topic-05` | Ví dụ 06.10; Định nghĩa 06.20; Nhận xét 06.21 | 1,5 |
| `lec06-s03-07` | Họ băm nhạy cảm theo tính cục bộ | `lec-06-topic-06` | Định nghĩa 06.22 | 3 |
| `lec06-s03-08` | Ví dụ: họ MinHash theo Jaccard | `lec-06-topic-06` | Hệ quả 06.23; Ví dụ 06.11 | 1,5 |
| `lec06-s03-09` | Phép ghép đồng thời | `lec-06-topic-07` | Định nghĩa 06.25; Mệnh đề 06.26 | 2,5 |
| `lec06-s03-10` | Phép ghép ít nhất một | `lec-06-topic-07` | Định nghĩa 06.25; Mệnh đề 06.26 | 2,5 |
| `lec06-s03-11` | Ví dụ: hai thứ tự ghép trên 16 phép thử | `lec-06-topic-07` | Ví dụ 06.12 | 2,5 |
| `lec06-s03-12` | Phân dải như phép ghép AND rồi OR | `lec-06-topic-07` | Nhận xét 06.27 | 1,5 |
| `lec06-s03-13` | Câu hỏi về độ đo và phép ghép | `lec-06-topic-05, lec-06-topic-07` | Bài tập 06.5, 06.7 | 3 |
| `lec06-s04-00` | 4. Các họ băm theo độ đo | `lec-06-topic-08` | — | 0,5 |
| `lec06-s04-14` | Thuật toán: tìm cặp với họ nhạy cảm | `lec-06-topic-07` | Thuật toán 06.4; Mệnh đề 06.26 | 1,5 |
| `lec06-s04-01` | Họ băm chọn tọa độ | `lec-06-topic-08` | Ví dụ 06.13; Định nghĩa 06.28 | 1,5 |
| `lec06-s04-02` | Tính nhạy cảm của họ chọn tọa độ | `lec-06-topic-08` | Mệnh đề 06.29; Nhận xét 06.30 | 2 |
| `lec06-s04-03` | Hàm băm dấu theo siêu phẳng | `lec-06-topic-09` | Ví dụ 06.14; Định nghĩa 06.31 | 2 |
| `lec06-s04-05` | Tính nhạy cảm của họ siêu phẳng | `lec-06-topic-09` | Định lý 06.32 | 2,5 |
| `lec06-s04-04` | Ví dụ: chữ ký dấu của hai vector, ba pháp tuyến | `lec-06-topic-09` | Ví dụ 06.15 | 1,5 |
| `lec06-s04-12` | Ước lượng góc từ chữ ký dấu | `lec-06-topic-09` | Thuật toán 06.33 | 1 |
| `lec06-s04-06` | Ví dụ: ba điểm trên trục thứ nhất | `lec-06-topic-10` | Ví dụ 06.16 | 1,5 |
| `lec06-s04-07` | Họ chiếu có dịch ngẫu nhiên | `lec-06-topic-10` | Định nghĩa 06.34 | 2 |
| `lec06-s04-08` | Xác suất chung thùng khi cố định hướng | `lec-06-topic-10` | Bổ đề 06.35 | 1 |
| `lec06-s04-13` | Chứng minh: xác suất chung thùng khi cố định hướng | `lec-06-topic-10` | Bổ đề 06.35 | 2 |
| `lec06-s04-09` | Tính nhạy cảm của họ chiếu hai chiều | `lec-06-topic-10` | Định lý 06.36; Nhận xét 06.37 | 2,5 |
| `lec06-s04-10` | Chi phí: chữ ký theo ba họ | `lec-06-topic-17` | Mệnh đề 06.38 | 1,5 |
| `lec06-s04-11` | Câu hỏi về các họ theo độ đo | `lec-06-topic-08, lec-06-topic-09, lec-06-topic-10` | Bài tập 06.8–06.10 | 2,5 |
| `lec06-s05-00` | 5. Ứng dụng tìm cặp tương đồng | `lec-06-topic-11` | — | 0,5 |
| `lec06-s05-01` | Đối sánh thực thể | `lec-06-topic-11` | Định nghĩa 06.39; Nhận xét 06.40; Tình huống 06.1 | 2,5 |
| `lec06-s05-02` | Họ băm ba ô cho vân tay | `lec-06-topic-12` | Định nghĩa 06.41 | 2 |
| `lec06-s05-03` | Ví dụ: xác suất va chạm của hàm ba ô | `lec-06-topic-12` | Mệnh đề 06.42 | 2,5 |
| `lec06-s05-04` | Phép ghép trong đối sánh vân tay | `lec-06-topic-12` | Ví dụ 06.18; Tình huống 06.2 | 2,5 |
| `lec06-s05-05` | Bản tin gần trùng | `lec-06-topic-13` | Định nghĩa 06.43; Tình huống 06.3 | 1,5 |
| `lec06-s05-07` | Ví dụ: shingle theo từ dừng | `lec-06-topic-13` | Ví dụ 06.19 | 1,5 |
| `lec06-s05-06` | Câu hỏi về đối sánh thực thể và vân tay | `lec-06-topic-11, lec-06-topic-12` | Bài tập 06.12, 06.13 | 1,5 |
| `lec06-s05-08` | Câu hỏi về shingle theo từ dừng | `lec-06-topic-13` | Bài tập 06.14 | 1 |
| `lec06-s06-00` | 6. Tổng kết và tự kiểm tra | `lec-06-topic-14` | — | 0,5 |
| `lec06-s06-05` | Kết quả và giả thiết không được bỏ | `lec-06-topic-14` | Mệnh đề 06.5; Định lý 06.7; Định nghĩa 06.22; Mệnh đề 06.26, 06.29; Định lý 06.32, 06.36; Mệnh đề 06.42; Nhận xét 06.40 | 2 |
| `lec06-s06-02` | Thuật toán, bảo đảm và chi phí | `lec-06-topic-14` | Thuật toán 06.4, 06.33; Mệnh đề 06.11, 06.38 | 1,5 |
| `lec06-s06-01` | Câu trả lời cho vấn đề trung tâm | `lec-06-topic-14` | Tóm tắt chương; Mệnh đề 06.13 | 2 |
| `lec06-s06-03` | Câu hỏi tự kiểm tra | `lec-06-topic-16` | Bài tập 06.16–06.18 | 2,5 |
| `lec06-s06-04` | Câu hỏi tự kiểm tra | `lec-06-topic-16` | Bài tập 06.15, 06.19, 06.27 | 2 |
| `lec06-s06-08` | Nguồn và tài liệu đọc | `lec-06-topic-15` | Hướng dẫn đọc thêm và tài liệu tham khảo | 0,5 |
| `lec06-s07-00` | 7. Bài tập vận dụng | `lec-06-topic-16` | — | 0,5 |
| `lec06-s07-01` | Bài tập: bảng giá trị đường cong S | `lec-06-topic-16` | Bài tập 06.20 | 11,5 |
| `lec06-s07-02` | Bài tập: nghiệm một nửa của đường cong S | `lec-06-topic-16` | Bài tập 06.21 | 6 |
| `lec06-s07-03` | Bài tập: xác suất qua nhiều tầng ghép | `lec-06-topic-16` | Bài tập 06.22 | 10 |
| `lec06-s07-04` | Bài tập: hàm chọn tọa độ trên bốn vector | `lec-06-topic-16` | Bài tập 06.23 | 6 |
| `lec06-s07-05` | Bài tập: chữ ký dấu của ba vector | `lec-06-topic-16` | Bài tập 06.24 | 10 |
| `lec06-s07-06` | Bài tập: thùng chiếu trên ba trục | `lec-06-topic-16` | Bài tập 06.25 | 8 |
| `lec06-s07-07` | Bài tập: hai cấu trúc ghép cho vân tay | `lec-06-topic-16` | Bài tập 06.28 | 8 |
