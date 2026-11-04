# Storyboard Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Viết lại toàn bộ ngày 2026-11-04 cùng bộ trang chiếu mới, theo đặc tả đã duyệt K1–K9 của điều phối viên, `plan-deck.md` và `source-deck.md`; nguồn nội dung có thẩm quyền là ghi chú `materials/lec-09/lecture-note.md` (commit `0c13fdc`). Các mục storyboard cũ (deck 53 trang) bị thay; mục hành trình chủ đề của ghi chú ở cuối tệp được giữ. Âm tiết đếm bằng script kiểm deck (khoảng trắng, bỏ tiêu đề, KaTeX, giả mã, hình, số trong bảng, ghi chú); "dòng" là dòng nhìn thấy (các khối cạnh nhau trong lưới tính một dòng); "max" là âm tiết của dòng dài nhất.

Tổng: **109 trang** = 96 trang giảng (120 phút) + 13 trang recitation (60 phút); lượt biên tập 1 sau năm rà soát tách C03 và E08 (C03B, E11). So với đích ≈ 90 + 13 của K2: đã áp các phép gộp 1–7, 9, 11 của `plan-deck.md` §3 (không áp 8, 10); thêm bốn trang do tách: P04B (hình vấn đề trung tâm cần cỡ đủ đọc), D07B, D17B (mật độ), E07B (bảng vết 9 hàng tách được nên tách, theo K8).

## Bản đồ mạch

| Mạch (tên trùng trang Nội dung) | Tiền tố | Loại | Chức năng | Vào | Ra | Đóng góp | Trang tiêu đề mạch |
|---|---|---|---|---|---|---|---|
| 1. Mở đầu | P | giới thiệu và động lực | Đặt năm câu hỏi thành đại lượng có định nghĩa ($f_u$, $F_p$, cửa sổ trượt) và đếm chi phí lời giải chính xác | Bài 08: Định nghĩa 08.1, Định lý 08.17, 08.25; Ví dụ 08.17 để ngỏ | $F_0=d$, $f_u$, $F_2$; 512 MiB mỗi trang, 125 MB mỗi URL; dòng mười lăm phần tử | Đặt vấn đề trung tâm có hình và câu trả lời có điều kiện của mạch 2–5 | P00 (trang bìa) |
| 2. Đếm phần tử phân biệt bằng Flajolet–Martin | F | thuật toán và ví dụ vận dụng, kèm cụm chi phí | Ước lượng $F_0$ bằng độ dài đuôi lớn nhất; ngưỡng hai phía; gộp trung bình nhóm rồi trung vị | $F_0=d$, 512 MiB, dòng mười lăm phần tử | Phép gộp (dùng lại ở AMS); giới hạn: $F_0$ không phân biệt hai dòng lệch khác nhau | Một số nhỏ mỗi hàm băm, 368 byte so với 512 MiB | FT, `id="mach-2"`, `#/2` |
| 3. Mômen bậc hai và ước lượng AMS | M | thuật toán và ví dụ vận dụng | Ước lượng $F_2$ không chệch; $F_p$; hồ chứa vị trí | $F_2$; Ví dụ 09.2; Định lý 08.17; phép gộp mạch 2 | Giới hạn: $F_2$ không chỉ ra phần tử nặng | Bảo đảm kỳ vọng, một cặp mỗi biến | MT, `id="mach-3"`, `#/3` |
| 4. Ước lượng tần suất bằng Count-Min Sketch | C | thuật toán và ví dụ vận dụng (cụm cầu nối: họ băm phổ dụng, Markov) | Ước lượng $f_u$ một phía; cận xác suất; định cỡ $m$, $t$ | $f_u$; cận hợp; Định lý 06.7; Bloom filter | Giới hạn: mọi đại lượng tính trên toàn dòng | 74 000 bộ đếm cho mọi phần tử | CT, `id="mach-4"`, `#/4` |
| 5. Cửa sổ trượt và cửa sổ suy giảm mũ | D, E | thuật toán và ví dụ vận dụng: cụm DGIM rồi cụm suy giảm | DGIM: cận dưới $N$ bit, sáu quy tắc, $O(\log^2N)$ bit, cận 50%, cập nhật đúng, khấu hao; cửa sổ suy giảm: truy hồi, tổng $<1/c$, phần tử phổ biến $<1/(c\theta)$ điểm | Cửa sổ trượt (P06), câu 4–5 của P05; Count-Min toàn dòng | Năm phác thảo, ba loại bảo đảm và năm bộ giả thiết | 266 byte so với 125 MB; $<2/c$ điểm | DT, `id="mach-5"`, `#/5` |
| 6. Tổng kết và tự kiểm tra | T | tổng kết và bài tập (phần tổng kết); không khái niệm mới | Hai bảng đối chiếu, trả lời có điều kiện năm yêu cầu bằng số, tự kiểm tra, nguồn, nối Bài 10 | Mọi kết quả 09.1–09.57 | Kiến thức cho recitation; nối Bài 10 | Thu hồi tình huống mở bài bằng số | TT, `id="mach-6"`, `#/6` |
| 7. Bài tập vận dụng | X | tổng kết và bài tập (phần bài tập, dọc riêng 60 phút) | Năm bài MMDS chạy tay FM, AMS, DGIM | Thuật toán 09.6, Định nghĩa 09.1, 09.19, Thuật toán 09.45, 09.47 | Sản phẩm nộp: bảng đuôi băm, $F_2$/$F_3$, bảng $v_i$, hai ước lượng DGIM, trạng thái thùng | Kiểm mục tiêu 2, 3, 5 | XT, `id="mach-7"`, `#/7` |

Bảy section ngoài (mở đầu, bốn mạch giảng, tổng kết, bài tập), trong khoảng 5–7, như Bài 08. DGIM và cửa sổ suy giảm cùng mạch 5 vì MMDS đặt §4.6 và §4.7 kề nhau, ghi chú nhóm Mục 5–6 dưới nhãn "gần đây", và cụm suy giảm mở từ giới hạn của cửa sổ trượt (E01 mở bằng "Nhắc lại:"). Không gộp cửa sổ suy giảm vào kết luận vì cụm có khái niệm mới (`AGENTS.md` dòng 141). Trang tiêu đề mạch FT, MT, CT, DT có dòng dẫn nêu đúng nhu cầu của thuật toán đầu mạch, nên được ghi là bước `vấn đề`; TT, XT nằm ngoài chu trình khái niệm.

## Bản đồ chu trình theo cụm

| Cụm | Tình huống, vấn đề | Trực giác | Ví dụ chạy tay | Hình thức hóa | Thuật toán | Lập luận đúng | Ứng dụng, chi phí | Kiểm tra |
|---|---|---|---|---|---|---|---|---|
| Flajolet–Martin | FT, F01 | F03 (so với Bloom filter) | F03, F05 | F04, F09 | F06 | F07, F10–F11 | F12, F18 | F19 |
| Gộp ước lượng (cụm con) | F13 | F13 | F14 | F16 | F15 | F17 | F18 | F19 |
| AMS | MT, M01 | M03 (so với hồ chứa cỡ 1) | M03 | M04, M06 | M05 | M07, M08 | M09 | M15 |
| AMS dòng chưa biết độ dài (biến thể) | M10 | M10 | M11 | M13 | M12 | M13 | M14 | M15 |
| Count-Min | CT, C01, C02 | C04 (so với Bloom filter) | C04, C06–C07 | C03, C03B, C04 | C08 | C09–C12 | C13 | C14 |
| DGIM | DT, D01, D03–D04 | D06, D15 (phép nhớ) | D06, D10, D15 | D07, D07B | D11, D16 | D09, D13, D17–D17B | D08, D18 | D19 |
| Cửa sổ suy giảm | E01 | E01 (ghi chú diễn giả), E03 | E02, E06 | E03, E04 | — | E05 | E04 (dòng mưa) | — |
| Phần tử phổ biến (cụm con) | E07 dòng đầu (giới hạn $d$ số) | E07 dòng đầu (tổng điểm $<1/c$) | E07–E07B | E09 | E08 | E10 | E11, E09 | E12 |
| Tổng kết | T01 | — | — | — | — | — | T05 | T06 |

Chu trình rút gọn có lý do: mômen bậc $p$ (M09) dùng cùng chứng minh với $F_2$; bài toán phần tử nặng (C02) là đặc tả; họ băm phổ dụng và Markov (C03) là công cụ cầu nối. Trực giác của cửa sổ suy giảm (trọng số nhân $1-c$ mỗi phần tử mới) nằm trong hình E01, E03 và ghi chú diễn giả E01.

## Từng trang

Quy ước cột Quyết định: `giữ` nghĩa là giữ đúng trang của `plan-deck.md` (mục đích, khối ghi chú, hình) sau khi soạn; mọi thay đổi khác ghi rõ `sửa`, `gộp`, `tách`, `thêm` kèm lý do. Cột "Kiến thức đầu vào" ghi kết quả hay kỹ năng cần biết trước; cột "Dữ kiện, ký hiệu kế thừa" ghi dữ liệu và ký hiệu lấy từ trang trước.

### Mạch 1. Mở đầu

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| P00 | Dòng dữ liệu: đếm, mômen và cửa sổ | ngoài chu trình | Nhận diện bài, luận đề và nguồn | Đọc luận đề, nêu năm câu hỏi của bài | Câu luận đề | — | Bài 08 (Ví dụ 08.17 để ngỏ) | Nêu được đổi chác bộ nhớ–sai số; kiểm ở T05 | phần mở đầu ghi chú | — | thêm: trang bìa theo mẫu | 45 (4, 20) | 140 | 0,5 |
| P01 | Tiên quyết và quy ước | cầu nối | Nhắc lại kết quả dùng lại, đặt ký hiệu cả bài | Đối chiếu ba dòng Nhắc lại với Bài 08 | Định nghĩa 08.1, Định lý 08.17, 08.25; cận hợp, tuyến tính kỳ vọng, $1-z\le e^{-z}$; $x_i,r,\mathcal U$ | Bài 08; xác suất cơ bản | Bài 08 | Dùng ký hiệu không cần định nghĩa lại ở mạch 2–5 | Tiên quyết, Bảng ký hiệu | lec-09-topic-01 | thêm: trang bắt buộc; cấp số nhân và Markov nhắc tại chỗ dùng (D09, E05, C03); thêm quy ước "vị trí đánh số từ 1" (G17), 59 → 60 âm tiết | 60 (4, 19) | 145 | 1,5 |
| P02 | Mục tiêu học tập | ngoài chu trình | Biết sáu sản phẩm kiểm được | Đọc sáu mục tiêu | Sáu mục tiêu | P01 (ký hiệu) | — | Mỗi mục tiêu ứng với câu hỏi cuối cụm và bài recitation | Mục tiêu học tập | — | thêm: trang bắt buộc của mạch mở đầu (AGENTS "Mẫu RevealJS bắt buộc") | 66 (6, 13) | 103 | 1 |
| P03 | Nội dung | ngoài chu trình | Thấy thứ tự bảy mạch, khớp `#/N` | Định vị mạch; ghi mục đọc trước | Danh sách 1–7, Đọc trước | tên mạch (trang tiêu đề mạch) | — | Số mạch khớp `#/2`…`#/7` (script) | Bản đồ chủ đề | — | thêm: trang bắt buộc của mạch mở đầu (AGENTS "Mẫu RevealJS bắt buộc") | 50 (5, 14) | 123 | 0,5 |
| P04 | Vấn đề trung tâm | tình huống, vấn đề | Nêu bài toán dữ liệu lớn: năm câu hỏi, bộ nhớ không tỷ lệ $d$ hay $N$ | Đọc hình năm câu hỏi → năm đại lượng → năm phác thảo | Hình `cau-truc-bai-09.svg` | mô hình dòng (Bài 08) | Dòng lượt nhấp Yahoo! (MMDS §4.1.2) | Gọi tên đại lượng của từng câu hỏi | Mục 1 mở, hình cấu trúc chương | lec-09-topic-02 | thêm: trang bài toán có hình của mạch mở đầu (K5, biến thể nhãn số mạch) | 35 (2, 18) | 121 | 0,5 |
| P04B | Vấn đề trung tâm, câu trả lời có điều kiện | vấn đề (câu trả lời có điều kiện) | Nêu câu trả lời có điều kiện của mạch 2–5 | Nối mỗi dòng với giả thiết và mạch chứng minh | Năm dòng có điều kiện | P04 | P04 | Nhắc lại bằng số ở T05 | Tóm tắt chương, bảng Mục 7.1 | lec-09-topic-25 | sửa (merge D, nghiêm trọng): dòng Count-Min tách kết luận tất định khỏi điều kiện hàng độc lập; năm điều kiện viết bằng lời thường; ngoại lệ K8 (≤ 80): 57 → 73 âm tiết | 73 (5, 18) | 138 | 1 |
| P05 | Ví dụ: năm câu hỏi trên dòng mười lăm phần tử | ví dụ dẫn nhập | Tính tay năm câu trả lời trên dòng mười lăm phần tử | Lập bảng vị trí, tính 4; 5; 59; 3 | Bảng vị trí 4 hàng + danh sách năm câu trả lời | đếm, tổng bình phương | MMDS Ví dụ 4.7 | Năm số; dòng dùng lại ở mọi mạch | Ví dụ 09.1 | lec-09-topic-02 | giữ; câu 1–2 gộp một mục để trang còn 6 dòng | 33 (6, 9) | 104 | 2,5 |
| P06 | Tần suất, mômen và cửa sổ trượt | hình thức hóa | Định nghĩa $f_u$, $F_p$, cửa sổ trượt; đặt câu 1–4 vào định nghĩa | Đọc $F_0=4$, $f_{\mathrm a}=5$, $F_2=59$ | Định nghĩa 09.1, 09.2 | P05 | P05 | Phân biệt $F_0$/$F_1$, $F_2$/$F_1^2$ (câu hỏi trong ghi chú diễn giả) | Định nghĩa 09.1, 09.2 | lec-09-topic-02 | sửa: thêm Định nghĩa 09.2 (kế hoạch đặt ở P07) để P07 giữ ≤ 8 dòng; trước: ước lượng kế hoạch 40, sau: 59 âm tiết | 59 (4, 18) | 131 | 1,5 |
| P07 | Chi phí: lời giải chính xác | chi phí | Đọc bộ nhớ lời giải chính xác của năm câu hỏi | So năm hàng, đều tỷ lệ với $d$ hoặc $N$ | Bảng 5 hàng; 512 MiB, 125 MB | P06; bit, byte | P06 | Số 512 MiB, 125 MB dùng lại ở F01, D01, T05 | Nhận xét 09.3 | lec-09-topic-02 | giữ; dòng Mô hình nêu đơn vị; hàng câu 5 sửa thành $D_r(u)$ với mọi $u$, $d$ số, theo Nhận xét 09.3 đã sửa (commit `b1d1c77`) | 79 (8, 15) | 119 | 1 |

### Mạch 2. Flajolet–Martin

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| FT | 2.Đếm phần tử phân biệt bằng Flajolet–Martin | điểm vào mạch 2 (vấn đề) | Dòng dẫn nêu nhu cầu đếm phân biệt bằng vài bit | — | Dòng dẫn | P06–P07 | $F_0=d$, 512 MiB | — | — | lec-09-topic-03 | thêm: trang tiêu đề mạch (AGENTS "Trang tiêu đề mạch") | 36 (0, 0) | 93 | 0,5 |
| F01 | Người dùng phân biệt của một trang | tình huống, vấn đề | Nêu động lực (IP mỗi trang), giới hạn Bài 08, khó khăn $\lvert\mathcal U\rvert$ bit | Đọc hình: vector $2^{32}$ bit so với bộ nhớ cần đạt | Hình `fm-bai-toan.svg` | Bloom filter, hồ chứa (Bài 08) | Ví dụ 08.17; P07 | Nêu vì sao cần ngẫu nhiên hoặc sai số | §2 mở, Nhận xét 09.3, 09.4 | lec-09-topic-03 | thêm: trang bài toán có hình (quy ước 2026-10-29) | 46 (3, 17) | 146 | 2 |
| F03 | Ví dụ: đuôi băm của bốn phần tử | trực giác, ví dụ chạy tay | Thấy vì sao đuôi dài báo cỡ $d$; chạy một hàm băm | Đếm bit 0 cuối, lập vết $R$: 1,1,2,2 | Bảng $h_1$; so với Bloom filter | nhị phân; Bloom filter | dòng mười lăm phần tử | $2^R=4$ | §2.2, Ví dụ 09.3 | lec-09-topic-04 | gộp: F02 vào đầu F03 (phép gộp 1); dòng trực giác nối xác suất $2^{-\ell}$ với cỡ $2^\ell$ (merge D) | 57 (6, 19) | 146 | 2 |
| F04 | Độ dài đuôi và ước lượng Flajolet–Martin | hình thức hóa | Định nghĩa $\rho$, $R$, ước lượng $2^R$ | Tính $\rho(01100)$ | Định nghĩa 09.5 | F03 | F03 | $R=2$ trên dòng ví dụ | Định nghĩa 09.5 | lec-09-topic-04 | giữ | 43 (4, 17) | 101 | 1 |
| F05 | Ví dụ: ba hàm băm khác trên cùng dòng | ví dụ | Thấy ước lượng dao động 2, 8, 16 với cùng $d$ | Đọc $R$ từ ba hàng | Bảng $h_3,h_4,h_5$ | F04 | F03–F04 | Nhu cầu mô hình xác suất và phép gộp | Ví dụ 09.4 | lec-09-topic-04 | giữ | 31 (6, 16) | 103 | 1 |
| F06 | Thuật toán: Flajolet–Martin | thuật toán | Đọc giả mã, phép quyết định, khung để ngỏ | Chạy với $h_4$ (ghi chú diễn giả) | Đầu vào/Đầu ra + giả mã 6 dòng | F04 | F04 | Chi phí một câu; $R$ chỉ giữ một số | Thuật toán 09.6 | lec-09-topic-04 | giữ | 47 (4, 18) | 112 | 1,5 |
| F07 | Tính đúng: Flajolet–Martin | lập luận đúng | Chứng minh bất biến của $R$ bằng quy nạp; hệ quả hợp nhất | Theo khởi tạo–duy trì–kết luận | Mệnh đề 09.7 | quy nạp; hàm băm tất định | F06 | Phần tử lặp góp một giá trị; dùng ở F19 | Mệnh đề 09.7 | lec-09-topic-04 | giữ; tiêu đề đổi thành “Tính đúng: Flajolet–Martin” (không đặt ký hiệu trong tiêu đề viết hoa) | 42 (5, 15) | 152 | 1,5 |
| F09 | Ngưỡng hai phía của ước lượng | hình thức hóa (kết quả) | Phát biểu ngưỡng hai phía với mô hình băm lý tưởng | Đọc vai trò từng giả thiết | Định nghĩa 09.8 (dòng Giả thiết) + Định lý 09.10 | độc lập; F07 | F07 | Cận $1/\lambda$, $e^{-\lambda/2}$ | Định nghĩa 09.8, Định lý 09.10 | lec-09-topic-05 | gộp: F08 vào F09 (phép gộp 2) | 41 (4, 17) | 125 | 1,5 |
| F10 | Chứng minh: ngưỡng hai phía, phía trên | chứng minh | Chứng minh (a), (b) bằng Bổ đề 09.9 và cận hợp | Theo Bổ đề, Bước 1–3 | 2 khối công thức | cận hợp | F09 | Phía trên không cần độc lập | Bổ đề 09.9, chứng minh Định lý 09.10 Bước 1–3 | lec-09-topic-05 | giữ; Bổ đề 09.9 thành dòng đầu (phép gộp 2) | 38 (6, 12) | 119 | 2 |
| F11 | Chứng minh: ngưỡng hai phía, phía dưới | chứng minh | Chứng minh (c) bằng độc lập và $1-z\le e^{-z}$ | Theo Bước 4–6 | 1 khối công thức | $1-z\le e^{-z}$; độc lập | F10 | Phản ví dụ ba giả thiết (ghi chú diễn giả) | chứng minh Định lý 09.10 Bước 4–6 | lec-09-topic-05 | giữ | 41 (5, 16) | 93 | 2 |
| F12 | Ví dụ: một nghìn phần tử phân biệt | ví dụ, ứng dụng | Thay số $d=1\,000$, $\lambda=4$: cận so với chính xác | Đọc hình, so 0,25/0,217 và 0,135/0,020 | Hình `fm-nguong-hai-phia-trang-chieu.svg` | F09 | F09–F11 | Xác suất 0,763: một hàm chỉ cho cỡ | Ví dụ 09.5 | lec-09-topic-05 | sửa: dùng bản trang chiếu của hình ghi chú (nhãn ≥ 18 px) | 14 (2, 8) | 110 | 0,5 |
| F13 | Trung bình và trung vị của các ước lượng | vấn đề (gộp) | So trung bình và trung vị: phân phối phân phối đuôi nặng, lũy thừa của 2 | Đọc bảng so sánh | Bảng 2 cột × 3 hàng | kỳ vọng; trung vị | F12; sáu ước lượng | Nhu cầu phép gộp hai bước | §2.4 mở, Mệnh đề 09.11, Nhận xét 09.12 | lec-09-topic-06 | giữ; ô trung vị có phép tính 256, 512, 112; ghi chú nêu 33 và cận 17 (merge D, N6) | 58 (6, 14) | 129 | 1,5 |
| F14 | Ví dụ: gộp sáu ước lượng | ví dụ chạy tay | Gộp sáu ước lượng: trung bình nhóm rồi trung vị | Tính 4, 5, 10 → 5 | Bảng $Y_j$ (ngang) | F13 | F13 | $\widehat d=5$ | Ví dụ 09.6 | lec-09-topic-06 | sửa: bảng ngang (6 hàng dọc của kế hoạch cho 9 dòng); bản nháp đầu đã ngang: 41 âm tiết, 6 dòng | 40 (6, 20) | 161 | 1,5 |
| F15 | Thuật toán: gộp trung bình rồi trung vị | thuật toán | Đọc phép gộp; $g$ lẻ chia hết $q$; biên | Đặt $g=q$, $g=1$ | Đầu vào/Đầu ra + giả mã | F14 | F14 | Bước cuối là trung vị | Thuật toán 09.13 | lec-09-topic-06 | sửa: giả mã viết từ bốn bước của ghi chú; thêm dòng phép quyết định và chi phí (G8) | 46 (4, 16) | 124 | 1 |
| F16 | Mẹo trung vị | kết quả | Phát biểu mẹo trung vị; thay số $q=21$ | Kiểm $\eta\le0{,}144$ | Bổ đề 09.14 + Hệ quả 09.15 | độc lập; cận hợp | F15 | ≤ 0,0029; bước trung bình nhóm chưa có cận | Bổ đề 09.14, Hệ quả 09.15 | lec-09-topic-06 | giữ | 55 (5, 20) | 104 | 1,5 |
| F17 | Chứng minh: mẹo trung vị | chứng minh | Chứng minh mẹo trung vị | Theo Bước 1–4 | 1 khối công thức | tổ hợp; cận hợp | F16 | Phản ví dụ bỏ độc lập, bỏ khoảng (ghi chú diễn giả) | chứng minh Bổ đề 09.14 | lec-09-topic-06 | giữ | 43 (4, 18) | 150 | 2 |
| F18 | Chi phí: Flajolet–Martin | chi phí | Lập bảng chi phí; thay số $q=420$ | Tính 2 941 bit ≈ 368 byte | Mô hình + bảng 3 hàng | bit của bộ đếm (Bài 08) | F15–F16 | 368 byte so với 512 MiB, dùng ở T05 | Mệnh đề 09.16, Nhận xét 09.17 | lec-09-topic-07 | giữ | 64 (7, 20) | 153 | 1 |
| F19 | Bài tập: phần tử lặp và ngưỡng hai phía | kiểm tra | Câu hỏi: phần tử lặp, ngưỡng hai phía với $d=2\,000$ | Giải (a), (b) | Câu hỏi | F07, F09 | F07, F09 | Lời giải trong ghi chú diễn giả | Bài tập 09.2 | lec-09-topic-07 | giữ | 27 (2, 18) | 156 | 1 |

### Mạch 3. AMS

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| MT | 3.Mômen bậc hai và ước lượng AMS | điểm vào mạch 3 (vấn đề) | Dòng dẫn nêu nhu cầu đo độ lệch | — | Dòng dẫn | $F_2$ (P06) | $F_2$; phép gộp mạch 2 | — | — | lec-09-topic-08 | thêm: trang tiêu đề mạch (AGENTS "Trang tiêu đề mạch") | 41 (0, 0) | 93 | 0,5 |
| M01 | Độ lệch của phân bố tần suất | tình huống, vấn đề | Động lực đo độ lệch; giới hạn FM ($F_0=11$ cả hai); khó khăn $d$ bộ đếm | Đọc hai biểu đồ, so 910 và 8 110 | Hình `ams-hai-phan-bo.svg` | $F_0$, $F_2$ | Ví dụ 09.2 | Nhu cầu ước lượng $F_2$ | §3 mở, Ví dụ 09.2 | lec-09-topic-08 | thêm: trang bài toán có hình; dòng Nhu cầu gọi tên dòng lượt truy cập theo IP (G18); không dùng câu "hàng tỷ bộ đếm" (K3) | 46 (3, 19) | 123 | 2 |
| M03 | Ví dụ: ba biến trên dòng mười lăm phần tử | trực giác, ví dụ chạy tay | Đếm hậu tố từ ba vị trí; so với hồ chứa cỡ 1 | Đọc 3, 2, 2 → 75, 45, 45 | Hình `ams-ba-bien-trang-chieu.svg` | hồ chứa cỡ 1 (Định lý 08.17) | dòng mười lăm phần tử; Định lý 08.17 | Trung bình 55 so với 59 | §3.1, Ví dụ 09.7 | lec-09-topic-08 | gộp: M02 vào M03 (phép gộp 3); thêm dòng Trực quan (merge D); hình bản trang chiếu | 35 (2, 19) | 132 | 2 |
| M04 | Số lần xuất hiện ở hậu tố và biến AMS | hình thức hóa | Định nghĩa $v_i$, $X=r(2v_I-1)$ | Phân biệt $v_6=4$ với $f_{\mathrm a}=5$ | Định nghĩa 09.19 | M03 | M03 | $v_I$ của ba biến | Định nghĩa 09.19 | lec-09-topic-08 | giữ | 49 (4, 15) | 101 | 1 |
| M05 | Thuật toán: AMS khi biết độ dài dòng | thuật toán | Đọc giả mã, bất biến bộ đếm | Đọc bất biến bộ đếm, chạy một biến trên vị trí 6 | Đầu vào/Đầu ra + giả mã + Bất biến | M04 | M04 | Bộ đếm $v_6=4$; chỗ để ngỏ "vì sao $2v-1$" dẫn tới M06 | Thuật toán 09.20 | lec-09-topic-08 | giữ; thêm dòng phép quyết định và chỗ để ngỏ (G8) | 59 (5, 18) | 117 | 1 |
| M06 | Biến AMS không chệch | kết quả | Phát biểu không chệch; ý nghĩa $f_u/r\cdot f_u$ | Nêu giả thiết $I$ đều | Định lý 09.22 | kỳ vọng | M05 | Kỳ vọng, không phải từng biến | Định lý 09.22 | lec-09-topic-09 | giữ | 45 (4, 17) | 119 | 1 |
| M07 | Chứng minh: biến AMS không chệch | chứng minh | Chứng minh không chệch qua tổng các số lẻ | Theo Bổ đề, Bước 1–4 | 1 khối công thức | quy nạp; M06 | M06 | Phản ví dụ 93, 103 (ghi chú diễn giả) | Bổ đề 09.21, chứng minh Định lý 09.22 | lec-09-topic-09 | giữ | 33 (5, 13) | 113 | 2 |
| M08 | Ví dụ: bộ đếm hậu tố ở mọi vị trí | ví dụ kiểm | Kiểm trên mọi vị trí; phương sai | Tính bảng $v_i$, tổng 59; Var 1 304 | Bảng 3 hàng × 15 cột | phương sai | M07 | Độ lệch chuẩn ≈ 36, 61% của $F_2$ | Ví dụ 09.8 | lec-09-topic-09 | giữ | 22 (7, 11) | 102 | 1,5 |
| M09 | Ước lượng mômen bậc cao | ứng dụng (biến thể, chu trình rút gọn) | Đổi phép trả lời cho $F_p$ | Tính $F_3=243$, ba biến cho 165 | Hệ quả 09.23 | M07 | M07 | Bài tập 09.13–09.14 | Hệ quả 09.23, Ví dụ 09.9 | lec-09-topic-10 | giữ; chu trình rút gọn vì dùng cùng chứng minh | 29 (4, 10) | 87 | 1 |
| M10 | Vị trí của biến trên dòng chưa biết độ dài | vấn đề (biến thể) | Nêu khó khăn khi không biết $r$: kỳ vọng 93 | Nối với hồ chứa | Nhu cầu + Nhắc lại Định lý 08.17 | Định lý 08.17 | M06 | Ý tưởng hồ chứa vị trí | §3.4 mở, Tình huống 09.3 | lec-09-topic-11 | giữ | 54 (4, 18) | 132 | 1 |
| M11 | Ví dụ: hai biến trên năm phần tử đầu | ví dụ chạy tay | Lập vết $s=2$ | Theo bảng 5 hàng | Bảng vết | M10 | M10 | 10 so với $F_2=7$ | Ví dụ 09.10 | lec-09-topic-11 | giữ; dòng dữ kiện gộp làm một (8 dòng, trần bảng vết), quy ước "tăng bộ đếm trước" chuyển vào ghi chú diễn giả | 34 (8, 10) | 115 | 2 |
| M12 | Thuật toán: AMS trên dòng chưa biết độ dài | thuật toán | Đọc giả mã AMS hồ chứa | Đối chiếu giả mã với vết M11 ở bước $r=4$ | Đầu vào/Đầu ra + giả mã 8 dòng | Thuật toán 08.16 | M11 | Phép quyết định $\xi\le s$ | Thuật toán 09.24 | lec-09-topic-11 | sửa: giả mã viết từ năm bước của ghi chú; thêm câu chi phí (G8) | 51 (4, 18) | 120 | 1 |
| M13 | Tính đúng: AMS trên dòng chưa biết độ dài | lập luận đúng | Chứng minh vị trí đều, bộ đếm đúng, trung bình không chệch | Theo Bước 1–3 | Mệnh đề 09.25, Hệ quả 09.26 | tuyến tính kỳ vọng; quy nạp | M12 | Chỉ trung bình $s$ biến có kỳ vọng $F_2$ | Mệnh đề 09.25, Hệ quả 09.26 | lec-09-topic-11 | sửa (merge D): mặt trang gồm Hệ quả $\mathbb E[\bar X]=F_2$ và định nghĩa $v_i^{(r)}$, $\bar X$; chứng minh gộp một dòng: 59 → 42 âm tiết | 45 (5, 14) | 133 | 2 |
| M14 | Chi phí: AMS | chi phí | Bảng chi phí; độc lập khi gộp | Đọc bảng 4 hàng | Mô hình + bảng + Lưu ý | mô hình chi phí | M12–M13 | Khoảng 100 biến (CS246) | bảng chi phí Thuật toán 09.24, Nhận xét 09.27–09.28 | lec-09-topic-11 | giữ (K2); dòng Lưu ý thay bằng phép gộp trung bình–trung vị với $s$ hồ chứa cỡ 1 (merge D) | 66 (8, 17) | 139 | 1 |
| M15 | Bài tập: đếm ở tiền tố | kiểm tra | Câu hỏi: đếm ở tiền tố | Chứng minh, kiểm 59 | Câu hỏi | M07 | M07 | Lời giải trong ghi chú diễn giả | Bài tập 09.4 | lec-09-topic-11 | giữ | 27 (3, 12) | 147 | 1 |

### Mạch 4. Count-Min

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| CT | 4.Ước lượng tần suất bằng Count-Min Sketch | điểm vào mạch 4 (vấn đề) | Dòng dẫn nêu nhu cầu tần suất với bảng không phụ thuộc $d$ | — | Dòng dẫn | $f_u$ (P06) | $F_2$ không chỉ phần tử nặng | — | — | lec-09-topic-12 | thêm: trang tiêu đề mạch; dòng dẫn rút từ 26 xuống 23 âm tiết (G1) | 41 (0, 0) | 93 | 0,5 |
| C01 | Địa chỉ gửi nhiều yêu cầu | tình huống, vấn đề | Động lực IP gửi nhiều yêu cầu; khó khăn $r/\kappa$ so với $r/\kappa-1$ | Đọc hình ngưỡng 5 | Hình `cm-phan-tu-nang.svg` | $f_u$, $F_2$ | dòng mười lăm phần tử | Nhu cầu nới lỏng | §4 mở, §4.1 | lec-09-topic-12 | thêm: trang bài toán có hình; dòng giới hạn có số $F_2=59$ (G9) | 44 (3, 16) | 160 | 2 |
| C02 | Bài toán phần tử nặng | hình thức hóa (đặc tả, chu trình rút gọn) | Định nghĩa bài toán $(\varepsilon,\kappa)$; ví dụ $\kappa=3$, $\varepsilon=1/4$ | Xếp a, b, c, d | Định nghĩa 09.30 | C01 | C01 | Yêu cầu với ước lượng | Định nghĩa 09.30 | lec-09-topic-12 | giữ; chu trình rút gọn vì là đặc tả | 46 (5, 18) | 115 | 1 |
| C03 | Họ băm phổ dụng | cầu nối | Định nghĩa họ băm phổ dụng; phản ví dụ hàm hằng | Áp định nghĩa cho họ một hàm hằng và họ độc lập từng cặp | Định nghĩa 09.31 | kỳ vọng | cận hợp | Nêu vì sao hàm hằng không phổ dụng | Định nghĩa 09.31 | lec-09-topic-13 | tách (merge D, thay quyết định cũ): C03 họ băm phổ dụng, C03B bất đẳng thức Markov | 54 (4, 18) | 132 | 1 |
| C03B | Bất đẳng thức Markov | cầu nối | Bất đẳng thức Markov và vai trò của $Z\ge0$ | Nêu phản ví dụ $Z=\pm10$ | Bổ đề 09.32 | kỳ vọng | kỳ vọng | Áp cho nhiễu $Z_j$ ở C10 | Bổ đề 09.32 | lec-09-topic-13 | thêm (tách từ C03, merge D) | 27 (4, 11) | 100 | 0,5 |
| C04 | Bộ đếm dùng chung và phép lấy cực tiểu | trực giác, ví dụ, hình thức hóa | Ô dùng chung, cực tiểu 104/78/90; định nghĩa Count-Min; so với Bloom | Lấy min | Hình `cm-ba-o.svg` + Định nghĩa 09.33 | Bloom filter | C03; Bloom filter | $\widehat f_u=78$ | §4.3, Ví dụ 09.11, Định nghĩa 09.33 | lec-09-topic-14 | gộp: C05 vào C04 (phép gộp 4) | 45 (3, 19) | 140 | 1,5 |
| C06 | Ví dụ: bảng hai hàng ba ô, năm bước đầu | ví dụ chạy tay | Cập nhật bảng $2\times3$ năm bước đầu | Theo bảng vết | Hình `cm-bang-2x3.svg` + bảng vết | C04 | C04 | Bảng sau 5 bước | Ví dụ 09.12 (năm bước đầu) | lec-09-topic-14 | giữ | 17 (7, 17) | 103 | 2 |
| C07 | Ví dụ: bảng hai hàng ba ô, cuối dòng | ví dụ | Cuối dòng: 8, 4, 3, 3; va chạm của a | Đọc bảng | Bảng 4 hàng | C06 | C06 | Nhu cầu chứng minh một phía và cận xác suất | Ví dụ 09.12 (cuối dòng) | lec-09-topic-14 | giữ | 22 (7, 16) | 111 | 1,5 |
| C08 | Thuật toán: cập nhật và truy vấn Count-Min | thuật toán | Đọc giả mã; cực tiểu; biên $f_u=0$ | Chạy truy vấn của $\mathrm d$ trên bảng C07 | Đầu vào/Đầu ra + giả mã 5 dòng | C04 | C07 | Chi phí một câu | Thuật toán 09.34 | lec-09-topic-14 | giữ | 53 (4, 19) | 124 | 1 |
| C09 | Tính đúng: Count-Min, ô không nhỏ hơn tần suất | lập luận đúng | Ô không nhỏ hơn tần suất, quy nạp | Theo khởi tạo–duy trì–kết luận | Bổ đề 09.35 | quy nạp | C08 | $Z_j\ge0$ | Bổ đề 09.35 | lec-09-topic-15 | giữ | 46 (5, 14) | 124 | 1 |
| C10 | Nhiễu của một hàng | kết quả + chứng minh | Nhiễu kỳ vọng $\le r/m$, Markov 1/2 | Thay số $10/3$, 10, 3 | Bổ đề 09.36 | C03, C09 | C03, C09 | Cần khuếch đại theo hàng | Bổ đề 09.36 | lec-09-topic-15 | giữ; ví dụ tách nhiễu quan sát $Z_1=Z_2=3$ với cận kỳ vọng $10/3\le5$ (merge D, N3) | 43 (6, 13) | 145 | 1,5 |
| C11 | Bảo đảm của Count-Min | kết quả | Bảo đảm Count-Min với $m$, $t$ | Đọc ý nghĩa $\delta=0{,}01$ | Định lý 09.37 | C10; độc lập | C10 | Sai số $\varepsilon r/\kappa$, xác suất $\delta$ | Định lý 09.37 | lec-09-topic-15 | giữ | 40 (4, 17) | 121 | 1 |
| C12 | Chứng minh: bảo đảm của Count-Min | chứng minh | Bước 1–3: cận dưới, đổi về nhiễu, tích theo hàng | Theo bước | 1 khối `aligned` | Định lý 06.7 | C11; Định lý 06.7 | Phản ví dụ ba giả thiết (ghi chú diễn giả) | chứng minh Định lý 09.37 | lec-09-topic-15 | giữ | 35 (4, 15) | 133 | 1,5 |
| C13 | Chi phí: Count-Min | chi phí | Bảng chi phí; 14 000 và 74 000 bộ đếm | Thay số | Mô hình + bảng 3 hàng + 2 dòng | logarit cơ số 2 | C11; Hệ quả 09.38 | 74 000 bộ đếm, dùng ở T05 | bảng chi phí Thuật toán 09.34, Hệ quả 09.38, Bài tập 09.6 | lec-09-topic-15 | giữ; dòng kết đóng bài toán $(\varepsilon,\kappa)$ trên các phần tử đã xuất hiện, theo Hệ quả 09.38(b) | 51 (7, 14) | 144 | 1 |
| C14 | Bài tập: hai hàng cùng một hàm băm | kiểm tra | Câu hỏi: hai hàng cùng hàm; vì sao cực tiểu | Tính 8,4,3,8 | Câu hỏi | C07, C12 | C07, C12 | Lời giải trong ghi chú diễn giả | phản ví dụ Định lý 09.37, Nhận xét 09.39 | lec-09-topic-15 | giữ | 45 (3, 16) | 168 | 1 |

### Mạch 5. Cửa sổ trượt và cửa sổ suy giảm mũ — cụm DGIM

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| DT | 5.Cửa sổ trượt và cửa sổ suy giảm mũ | điểm vào mạch 5 (vấn đề) | Dòng dẫn nêu nhu cầu tóm tắt cửa sổ | — | Dòng dẫn | cửa sổ trượt (P06) | Count-Min tính trên toàn dòng | — | — | lec-09-topic-16 | thêm: trang tiêu đề mạch (AGENTS "Trang tiêu đề mạch") | 42 (0, 0) | 89 | 0,5 |
| D01 | Lượt truy cập trong cửa sổ gần đây | tình huống, vấn đề | Câu 4 thành dòng bit; URL $N=10^9$; khó khăn 125 MB | Đọc hình cửa sổ 8 bit | Hình `dgim-bai-toan.svg` | P05 câu 4 | P05, P07 | Nhu cầu mọi $k\le N$ | §5 mở, Nhận xét 09.3 | lec-09-topic-16 | thêm: trang bài toán có hình; dòng Ký hiệu định nghĩa $x_i$, $y_k$ (merge D); 125 MB chỉ ở mặt trang | 57 (4, 18) | 129 | 2 |
| D03 | Cận dưới cho đếm chính xác trong cửa sổ | kết quả | Cận dưới $N$ bit cho đáp số chính xác | Đọc (a), (b) | Mệnh đề 09.41 | thuật toán dòng (Định nghĩa 08.1) | D01 | Mọi cách tiết kiệm phải chấp nhận sai số | Mệnh đề 09.41 | lec-09-topic-16 | giữ | 56 (4, 19) | 120 | 1 |
| D04 | Chứng minh: cận dưới cho đếm chính xác | chứng minh + ví dụ | Chứng minh qua Dirichlet; minh họa $1001/0101$ | Theo Bước 1–3 | 3 bước + ví dụ | nguyên lý Dirichlet | D03 | Nêu lại cặp cửa sổ $1001/0101$ và bước đọc thêm $N-k$ bit | chứng minh Mệnh đề 09.41, Ví dụ 09.13 | lec-09-topic-16 | gộp: D02 vào D04 (phép gộp 5) | 59 (4, 20) | 174 | 1,5 |
| D06 | Ví dụ: sáu đoạn trên hai mươi lăm bit | trực giác, ví dụ | Đọc trạng thái Hình 4.2; ý tưởng số bit 1 lũy thừa của 2 | Đọc sáu đoạn 1,1,2,4,4,8 | Hình `dgim-trang-thai-nen.svg` | lũy thừa của 2 | MMDS Hình 4.2 | Trạng thái dùng ở D10, D15, X04 | §5.2, Ví dụ 09.14 | lec-09-topic-17 | gộp: D05 vào D06; viết lại ý tưởng theo ghi chú, không dùng "thùng", "mốc phải" trước D07 (merge D, nghiêm trọng); tiêu đề gọi theo đối tượng | 49 (3, 18) | 160 | 1,5 |
| D07 | Thùng của biểu diễn DGIM | hình thức hóa | Định nghĩa thùng, mốc phải, kích thước, cách lưu | Đọc thùng cỡ 2 phủ $1001$ | Định nghĩa 09.42 (thùng) | D06 | D06 | Đọc thùng $(4,r-8)$: năm vị trí, bốn bit 1 | Định nghĩa 09.42 | lec-09-topic-17 | tách: D07 bản nháp 99 âm tiết tách thành D07 (52) và D07B (56); ví dụ dùng thùng $(4,r-8)$ để không trùng D06 (G15) | 58 (4, 20) | 127 | 1 |
| D07B | Sáu quy tắc của biểu diễn DGIM | hình thức hóa | Sáu quy tắc của biểu diễn DGIM | Kiểm sáu quy tắc trên Hình 4.2 | Danh sách 1–6 | D07 | D07 | Số hiệu quy tắc dùng trong mọi chứng minh | Định nghĩa 09.42, Nhận xét 09.43 | lec-09-topic-17 | thêm (tách từ D07, lý do mật độ) | 56 (5, 14) | 143 | 1 |
| D08 | Số thùng và bộ nhớ | kết quả, chi phí bộ nhớ | Số thùng $O(\log N)$, bộ nhớ $O(\log^2N)$; thay số $N=10^9$ | Tính 60 × 35 + 30 | Mệnh đề 09.44 | logarit; D07B | D07B | 266 byte so với 125 MB | Mệnh đề 09.44 | lec-09-topic-17 | giữ | 40 (4, 13) | 102 | 1 |
| D09 | Chứng minh: số thùng và bộ nhớ | chứng minh | Chứng minh số thùng | Theo Bước 1–4 | 4 bước | tổng cấp số nhân | D08 | Nêu bước dùng quy tắc 4, 6 và vì sao $2^J\le N$ | chứng minh Mệnh đề 09.44 | lec-09-topic-17 | giữ | 59 (5, 19) | 122 | 1,5 |
| D10 | Ví dụ: mười vị trí cuối trên hai mươi lăm bit | ví dụ chạy tay (truy vấn) | Truy vấn $k=10$: 6 so với 5 | Tìm $b^*$, $T$ | Hình `dgim-truy-van-10.svg` | D06 | D06 | Trường hợp $\pi=1$ | Ví dụ 09.15 | lec-09-topic-18 | giữ; hình mới theo generator | 20 (2, 11) | 114 | 1,5 |
| D11 | Thuật toán: truy vấn DGIM | thuật toán | Đọc giả mã truy vấn; biên $k=N$ | Chạy truy vấn với $k=10$ trên D10 | Đầu vào/Đầu ra + giả mã 5 dòng | D10 | D10 | $O(\log N)$ | Thuật toán 09.45 | lec-09-topic-18 | sửa: giả mã viết từ ba bước | 37 (4, 14) | 109 | 1 |
| D12 | Cận sai số 50% | kết quả | Cận 50%; ý nghĩa $2/3$ đến 2 lần | Đổi cận về "giữa $2/3$ và 2 lần" số trả về | Định lý 09.46 | D11 | D11 | Bảo đảm tất định | Định lý 09.46 | lec-09-topic-18 | giữ | 29 (3, 18) | 132 | 1 |
| D13 | Chứng minh: cận sai số 50% | chứng minh | Chứng minh cận 50% (Bước 1–5) | Theo bước | 1 khối công thức | tổng cấp số nhân; quy tắc 4, 6 | D12 | Phản ví dụ quy tắc 4, quy tắc 1 (ghi chú diễn giả) | chứng minh Định lý 09.46 | lec-09-topic-18 | gộp: D13 + D14 (phép gộp 7) | 46 (5, 18) | 181 | 2 |
| D15 | Ví dụ: một bit 1 mới trên hai mươi lăm bit | trực giác, ví dụ chạy tay (cập nhật) | Thêm một bit 1: gộp hai thùng cỡ 1 cũ nhất | Đọc hai dải trước–sau | Hình `dgim-cap-nhat-trang-chieu.svg` | phép cộng nhị phân | D06 | Trạng thái Hình 4.3, dùng ở X05 | Ví dụ 09.16 | lec-09-topic-19 | giữ; thêm dòng Nhu cầu nối với cận 50% (merge D) | 49 (3, 20) | 177 | 2 |
| D16 | Thuật toán: cập nhật DGIM | thuật toán | Đọc giả mã cập nhật; gộp hai thùng cũ nhất | So với gộp hai thùng mới nhất | Đầu vào/Đầu ra + giả mã 8 dòng | D15 | D15 | Gộp trên $2,2,2,1$ và nêu quy tắc 6 bị phá | Thuật toán 09.47 | lec-09-topic-19 | giữ; thêm câu chi phí (G8) | 38 (3, 17) | 123 | 1 |
| D17 | Tính đúng: cập nhật DGIM, hết hạn và bit mới | lập luận đúng | Hết hạn, bit 0, khởi tạo vòng gộp | Theo Bước 1–3 | Định lý 09.48 | D07B; bất biến vòng lặp | D16 | Nêu vì sao chỉ thùng cũ nhất hết hạn | Định lý 09.48, Bước 1–3 | lec-09-topic-19 | tách: bản nháp 84 âm tiết tách thành D17 (58) và D17B (49) | 58 (4, 18) | 170 | 1,5 |
| D17B | Tính đúng: cập nhật DGIM, vòng gộp | lập luận đúng | Bất biến vòng gộp: khởi tạo–duy trì–kết thúc | Theo bảng | Bảng bất biến $\mathcal I_\chi$ | D17 | D17 | Nêu khởi tạo, duy trì, kết thúc của $\mathcal I_\chi$ | Định lý 09.48, Bước 4–5 | lec-09-topic-19 | thêm (tách từ D17); bất biến thêm vế các cỡ lớn hơn (merge D) | 59 (5, 17) | 180 | 1,5 |
| D18 | Chi phí: cập nhật DGIM | chi phí | Xấu nhất $O(\log N)$; khấu hao một lượt gộp mỗi bit 1 | Đếm số thùng | Mô hình + bảng 3 hàng + 2 dòng | phân tích khấu hao | D16–D17B | Đếm số thùng để chặn tổng lượt gộp | Mệnh đề 09.49 | lec-09-topic-19 | giữ; gộp hai dòng khấu hao thành một (G12): 71 → 58 âm tiết, 8 → 7 dòng | 60 (7, 20) | 147 | 1,5 |
| D19 | Bài tập: hai bit 1 liên tiếp | kiểm tra | Câu hỏi: hai bit 1 liên tiếp | Ghi trạng thái, kiểm quy tắc | Câu hỏi | D16 | D16 | Lời giải trong ghi chú diễn giả | Bài tập 09.7 | lec-09-topic-20 | giữ | 48 (3, 19) | 153 | 1 |

### Mạch 5 — cụm cửa sổ suy giảm

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| E01 | Phim phổ biến hiện thời | tình huống, vấn đề | Nhắc lại giới hạn cửa sổ trượt; phim phổ biến; DGIM mỗi phần tử quá tốn | Đọc hình hai phim | Hình `suy-giam-hai-phim.svg` | cửa sổ trượt | D19; Ví dụ 09.17 | Nhu cầu trọng số theo tuổi | §6 mở, §5 đoạn cuối | lec-09-topic-21 | thêm: trang bài toán có hình mở cụm; Nhắc lại chỉ chứa giới hạn của DGIM (merge D) | 51 (3, 20) | 138 | 1,5 |
| E02 | Ví dụ: mười tuần so với một tuần | ví dụ dẫn nhập | $c=0{,}1$: 6,51 so với 2 | Tính tổng cấp số nhân | 1 khối công thức | tổng cấp số nhân | E01 | A trên B | Ví dụ 09.17 | lec-09-topic-21 | giữ | 36 (3, 20) | 74 | 1 |
| E03 | Cửa sổ suy giảm mũ | hình thức hóa | Định nghĩa $D_r$, $D_r(u)$; so cửa sổ $1/c$ | Đọc hình trọng số | Định nghĩa 09.52 + hình `cua-so-suy-giam-trang-chieu.svg` | E02 | E02 | Đọc trọng số tuổi 10: 0,35 | Định nghĩa 09.52, Nhận xét 09.54 | lec-09-topic-21 | sửa: hình bản trang chiếu (nhãn ≥ 18 px) | 25 (2, 17) | 133 | 1 |
| E04 | Truy hồi và tổng trọng số | kết quả | Truy hồi, tổng $<1/c$; dòng mưa | Tính $D_1,D_2,D_3$ | Mệnh đề 09.53 | E03 | E03 | Tổng điểm $<1/c$ cho E10 | Mệnh đề 09.53 | lec-09-topic-21 | giữ | 22 (5, 9) | 104 | 0,5 |
| E05 | Chứng minh: truy hồi và tổng trọng số | chứng minh | Chứng minh truy hồi và tổng | Theo Bước 1–3 | 1 khối công thức | tổng cấp số nhân | E04 | Nêu bước dùng tổng cấp số nhân | chứng minh Mệnh đề 09.53 | lec-09-topic-21 | giữ (K2 không gộp E05) | 28 (4, 11) | 85 | 1 |
| E06 | Ví dụ: điểm của bốn phần tử | ví dụ | Điểm bốn phần tử, $c=1/2$: b trên a | Đọc bảng | Bảng 4 hàng | E04 | E04; P05 câu 5 | Trả lời câu 5 | Ví dụ 09.18 | lec-09-topic-21 | giữ | 15 (6, 13) | 109 | 1 |
| E07 | Ví dụ: vết chạy với hằng số suy giảm và ngưỡng một nửa, bước 1–5 | vấn đề, trực giác, ví dụ chạy tay | Giới hạn $d$ số và ý tưởng tổng $<1/c$; vết bước 1–5 | Theo bảng vết | Bảng vết 6 hàng | E04(c) | E06 | Trạng thái sau bước 5: $\mathrm b:5/8$, $\mathrm d:1$ | Ví dụ 09.19 | lec-09-topic-22 | sửa (G5): mở bằng giới hạn và ý tưởng của ghi chú §6.2; bảng vết 9 hàng tách thành E07 (bước 1–5) và E07B (bước 6–15) vì tách được (K8) | 41 (8, 19) | 100 | 1,5 |
| E07B | Ví dụ: vết chạy với hằng số suy giảm và ngưỡng một nửa, bước 6–15 | ví dụ chạy tay | Vết bước 6–15; ≤ 2 điểm; cận dưới điểm thật | Theo bảng vết | Bảng vết 3 hàng + Diễn giải | E07 | E07 | $\mathrm b:1$, $\mathrm a:3/4$ | Ví dụ 09.19 | lec-09-topic-22 | thêm (tách từ E07) | 48 (7, 17) | 103 | 1,5 |
| E08 | Thuật toán: phần tử phổ biến trong cửa sổ suy giảm | thuật toán + chi phí | Đọc giả mã; định nghĩa điểm được duy trì | Đối chiếu bước xóa với vết E07 | Đầu vào/Đầu ra + giả mã | E07B; bảng băm | E07B | $O(1/(c\theta))$ mỗi phần tử | Thuật toán 09.55, bảng chi phí, Nhận xét 09.57 | lec-09-topic-22 | tách (merge D): bảng chi phí chuyển sang E11, đặt sau chứng minh số điểm | 52 (4, 18) | 122 | 1 |
| E09 | Số điểm được duy trì | kết quả | Số điểm $<1/(c\theta)$; $c=10^{-9}$ | Thay $c=10^{-9}$, $\theta=1/2$ | Định lý 09.56 | E04(c) | E08 | < $2\cdot10^9$ điểm, không quá $d$ | Định lý 09.56 | lec-09-topic-22 | giữ | 41 (4, 15) | 155 | 1 |
| E10 | Chứng minh: số điểm được duy trì | chứng minh | Bước 1–3: quy nạp, tổng, đếm | Theo bước | 1 khối công thức | quy nạp | E09, E04 | Nêu bước dùng tổng $<1/c$ | chứng minh Định lý 09.56 | lec-09-topic-22 | giữ | 28 (4, 12) | 115 | 1,5 |
| E11 | Chi phí: phần tử phổ biến | chi phí | Bảng chi phí theo số điểm $\Lambda$, sau khi đã chặn $\Lambda$ | Thay $\Lambda<1/(c\theta)$ | Mô hình + bảng 3 hàng | E09 | E08, E09 | $O(1/(c\theta))$ mỗi phần tử | bảng chi phí Thuật toán 09.55, Nhận xét 09.57 | lec-09-topic-22 | thêm (tách từ E08, merge D): Mô hình đứng đầu, đặt sau chứng minh | 45 (6, 18) | 118 | 0,5 |
| E12 | Bài tập: ngưỡng một phần tư | kiểm tra | Câu hỏi: ngưỡng $1/4$ | Chặn, chạy năm bước | Câu hỏi | E09 | E08–E09 | Lời giải trong ghi chú diễn giả | Bài tập 09.8 | lec-09-topic-22 | giữ | 25 (3, 11) | 138 | 1 |

### Mạch 6. Tổng kết và tự kiểm tra

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| TT | 6.Tổng kết và tự kiểm tra | điểm vào mạch 6 | Dòng dẫn nêu việc đối chiếu | — | Dòng dẫn | mạch 2–5 | Mạch 2–5 | — | — | lec-09-topic-23 | thêm: trang tiêu đề mạch (AGENTS "Trang tiêu đề mạch") | 31 (0, 0) | 97 | 0,5 |
| T01 | Năm yêu cầu trên dòng lượt truy cập | vấn đề (thu hồi tình huống) | Năm yêu cầu của một trang web, chưa lộ lời giải | Chọn phác thảo cho từng yêu cầu | Hình `nam-yeu-cau.svg` + Câu hỏi | mạch 2–5 | P04 | Câu trả lời ở T05 | Mục 7 mở, Ví dụ 09.20 (dữ kiện) | lec-09-topic-23 | thêm: trang bài toán có hình | 16 (1, 16) | 112 | 1 |
| T02 | Kết quả và giả thiết không được bỏ | tổng kết | Bảng kết quả–giả thiết–công thức, 7 hàng | Gọi phản ví dụ của từng giả thiết | Bảng 7 hàng | mạch 2–5 | mạch 2–5 | Gọi một phản ví dụ cho mỗi giả thiết | bảng đầu Mục 7.1 | lec-09-topic-23 | gộp: T02 + T03 (phép gộp 9) | 70 (8, 14) | 149 | 1,5 |
| T04 | Thuật toán, bảo đảm và chi phí | tổng kết | Bảng thuật toán–đầu vào–bảo đảm–chi phí | So bộ nhớ | Mô hình + bảng 5 hàng | mạch 2–5 | mạch 2–5 | So bộ nhớ của năm thuật toán với lời giải chính xác | bảng thứ hai Mục 7.1 | lec-09-topic-23 | giữ | 61 (7, 16) | 132 | 1,5 |
| T05 | Câu trả lời cho vấn đề trung tâm | ứng dụng | Trả lời có điều kiện năm yêu cầu bằng số | Đọc năm dòng | Năm dòng | T02, T04 | T01; F18, C13, D08, E09 | 368 byte, 74 000 bộ đếm, 266 byte, $<2/c$ | Ví dụ 09.20 | lec-09-topic-23 | giữ; 57 âm tiết, không cần ngoại lệ K8 | 61 (5, 19) | 162 | 1,5 |
| T06 | Câu hỏi tự kiểm tra | kiểm tra | Bốn câu tự kiểm tra, mỗi mạch giảng một câu (FM, AMS, DGIM, Count-Min) | Trả lời, nêu kết quả | Câu hỏi + 4 câu | mạch 2–5 | mạch 2–5 | Lời giải trong ghi chú diễn giả | Mệnh đề 09.11, Nhận xét 09.29, 09.51, Bài tập 09.19 | lec-09-topic-25 | sửa (merge D): câu 3 hỏi bộ nhớ DGIM (Nhận xét 09.51), câu 4 hỏi Count-Min (Ví dụ 09.12) | 57 (5, 14) | 155 | 1,5 |
| T07 | Nguồn và tài liệu đọc | ngoài chu trình | Nguồn, ghi công MMDS, liên kết ghi chú, nối Bài 10 | Ghi mục đọc thêm; mở ghi chú bài giảng | Danh sách nguồn | nguồn của mạch 1–5 | — | Liên kết viewer và Bài 10 hoạt động | Tài liệu tham khảo | lec-09-topic-27 | giữ | 60 (6, 16) | 185 | 0,5 |

### Mạch 7. Bài tập vận dụng (phần dọc riêng)

| ID | Tiêu đề | Bước chu trình | Mục đích (sinh viên làm được) | Hành động của sinh viên | Đối tượng trung tâm | Kiến thức đầu vào | Dữ kiện, ký hiệu kế thừa | Sản phẩm, bằng chứng | Khối ghi chú | `note-topic-id` | Quyết định và lý do | ÂT (dòng, max) | Ghi chú ÂT | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|---:|
| XT | 7.Bài tập vận dụng | điểm vào mạch 7 | Dòng dẫn nêu việc tính tay trên dòng giáo trình | — | Dòng dẫn | mạch 2, 3, 5 | mạch 2, 3, 5 | — | — | lec-09-topic-26 | thêm: trang tiêu đề mạch của phần recitation | 34 (0, 0) | 86 | 0 |
| X01 | Bài tập: đuôi băm của ba hàm băm | kiểm tra (đề) | Đề Bài 4.4.1 với hình dòng chín số | Tính giá trị băm | Hình `bai-4-4-1-dong.svg` + Câu hỏi | F06 | F06 | Bảng chín giá trị băm (đối chiếu X01B) | Bài tập 09.11 | lec-09-topic-26 | thêm: trang bài toán có hình sau XT | 42 (4, 20) | 103 | 4 |
| X01B | Bài tập: đuôi băm của ba hàm băm | lời giải | Lời giải (a), (b) | Đối chiếu bảng | Bảng 5 hàng | X01 | X01 | Hướng dẫn chấm 10 điểm (ghi chú diễn giả) | Bài tập 09.11 | lec-09-topic-26 | giữ | 19 (7, 14) | 111 | 5 |
| X01C | Bài tập: đuôi băm của ba hàm băm | lời giải | Lời giải (c), nhận xét không đơn ánh | Đối chiếu | Bảng 2 hàng | X01B | X01B | Nêu hàm không đơn ánh và 7 phần tử phân biệt | Bài tập 09.11 | lec-09-topic-26 | giữ | 27 (6, 17) | 126 | 5 |
| X02 | Bài tập: số bất ngờ | kiểm tra (đề) | Đề Bài 4.5.1 | Lập bảng tần suất | Câu hỏi | P06 | P06 | Bảng tần suất (đối chiếu X02B) | Bài tập 09.10 | lec-09-topic-26 | giữ | 26 (4, 11) | 69 | 3 |
| X02B | Bài tập: số bất ngờ | lời giải | $F_2=21$, $F_3=51$ | Đối chiếu | Bảng tần suất | X02 | X02 | Kiểm tổng tần suất bằng 9 | Bài tập 09.10 | lec-09-topic-26 | giữ | 20 (6, 10) | 97 | 5 |
| X03 | Bài tập: giá trị các biến AMS | kiểm tra (đề) | Đề Bài 4.5.3 (giữ câu hỏi của sách) | Tính $v_i$ | Câu hỏi | M04 | M04 | Chín giá trị $v_i$ (đối chiếu X03B) | Bài tập 09.12 | lec-09-topic-26 | giữ | 39 (3, 19) | 88 | 4 |
| X03B | Bài tập: giá trị các biến AMS | lời giải | $v_i$, ước lượng, trung bình 21 | Đối chiếu | Bảng 3 hàng × 9 cột | X03 | X03 | Kiểm Định lý 09.22 | Bài tập 09.12 | lec-09-topic-26 | giữ | 20 (6, 10) | 139 | 8 |
| X04 | Bài tập: hai truy vấn trên hai mươi lăm bit | kiểm tra (đề) | Đề Bài 4.6.1 với hình hai ranh giới | Tìm $b^*$ | Hình `dgim-bai-4-6-1.svg` + Câu hỏi | D11 | D10–D11 | Hai ước lượng và sai lệch (đối chiếu X04B) | Bài tập 09.15 | lec-09-topic-26 | sửa: hình vẽ lại bằng generator (thay `dgim-exercise.svg`) | 39 (4, 14) | 82 | 4 |
| X04B | Bài tập: hai truy vấn trên hai mươi lăm bit | lời giải | Bảng hai truy vấn: 3 đúng, 10 so với 9 | Đối chiếu | Bảng 2 hàng | X04 | X04 | Kiểm cận 50% | Bài tập 09.15 | lec-09-topic-26 | giữ | 34 (5, 17) | 131 | 8 |
| X05 | Bài tập: ba bit 1 nữa sau một bit 1 mới | kiểm tra (đề) | Đề Bài 4.6.3 với hình Hình 4.3 | Áp cập nhật ba lần | Hình `dgim-bai-4-6-3.svg` + Câu hỏi | D16 | D15–D16 | Ba trạng thái thùng (đối chiếu X05B, X05C) | Bài tập 09.16 | lec-09-topic-26 | sửa: hình vẽ lại bằng generator (thay `dgim-cascade-exercise.svg`) | 48 (4, 19) | 108 | 4 |
| X05B | Bài tập: ba bit 1 nữa sau một bit 1 mới | lời giải | Bit $r+1$, $r+2$: dây chuyền ba mức | Đối chiếu bảng | Bảng 4 hàng | X05 | X05 | Ba lượt gộp đúng mốc | Bài tập 09.16 | lec-09-topic-26 | giữ | 37 (7, 12) | 158 | 6 |
| X05C | Bài tập: ba bit 1 nữa sau một bit 1 mới | lời giải | Bit $r+3$, trạng thái cuối, nhánh cỡ 16, kiểm tổng | Đối chiếu | 4 dòng | X05B | X05B | Kiểm $13+3=16$ và sáu quy tắc | Bài tập 09.16 | lec-09-topic-26 | giữ | 39 (4, 20) | 122 | 4 |

## Bảng thời gian

| Mạch | Trang | Phút |
|---|---:|---:|
| 1 Mở đầu | 9 | 10,0 |
| 2 Flajolet–Martin | 18 | 25,0 |
| 3 AMS | 15 | 20,0 |
| 4 Count-Min | 15 | 18,0 |
| 5 Cửa sổ (DGIM) | 19 | 25,0 |
| 5 Cửa sổ (suy giảm) | 13 | 14,0 |
| 6 Tổng kết | 7 | 8,0 |
| **Phần giảng** | **96** | **120,0** |
| 7 Bài tập vận dụng | 13 | 60 |
| **Tổng** | **109** | **180** |

Phần giảng vượt 60 trang: bài có năm thuật toán trọng tâm, mỗi thuật toán đủ chu trình, trang bài toán có hình sau mỗi trang tiêu đề mạch và chứng minh tách trang theo quy ước tác giả 2026-10-28/29; trung bình khoảng 1,3 phút mỗi trang, mặt trang mỏng (57 trang trên 40 âm tiết, không trang nào vượt trần ngoài các loại trang được trần 80). Đọc thêm, không lên mặt trang: Nhận xét 09.50 (giảm sai số DGIM, tổng số nguyên; nhắc trong ghi chú diễn giả D18), Tình huống 09.1 (cỡ lân cận trong mạng xã hội; nhắc ở ghi chú diễn giả T07), HyperLogLog. Recitation: 4.4.1 = 14, 4.5.1 = 8, 4.5.3 = 12, 4.6.1 = 12, 4.6.3 = 14 phút.

## Ánh xạ `data-slide-id` ↔ `note-topic-id`

| `note-topic-id` | `data-slide-id` |
|---|---|
| lec-09-topic-01 | P01 |
| lec-09-topic-02 | P04, P05, P06, P07 |
| lec-09-topic-03 | FT, F01 |
| lec-09-topic-04 | F03, F04, F05, F06, F07 |
| lec-09-topic-05 | F09, F10, F11, F12 |
| lec-09-topic-06 | F13, F14, F15, F16, F17 |
| lec-09-topic-07 | F18, F19 |
| lec-09-topic-08 | MT, M01, M03, M04, M05 |
| lec-09-topic-09 | M06, M07, M08 |
| lec-09-topic-10 | M09 |
| lec-09-topic-11 | M10, M11, M12, M13, M14, M15 |
| lec-09-topic-12 | CT, C01, C02 |
| lec-09-topic-13 | C03, C03B |
| lec-09-topic-14 | C04, C06, C07, C08 |
| lec-09-topic-15 | C09, C10, C11, C12, C13, C14 |
| lec-09-topic-16 | DT, D01, D03, D04 |
| lec-09-topic-17 | D06, D07, D07B, D08, D09 |
| lec-09-topic-18 | D10, D11, D12, D13 |
| lec-09-topic-19 | D15, D16, D17, D17B, D18 |
| lec-09-topic-20 | D19 |
| lec-09-topic-21 | E01, E02, E03, E04, E05, E06 |
| lec-09-topic-22 | E07, E07B, E08, E09, E10, E11, E12 |
| lec-09-topic-23 | TT, T01, T02, T04, T05 |
| lec-09-topic-25 | P04B, T06 |
| lec-09-topic-26 | XT, X01, X01B, X01C, X02, X02B, X03, X03B, X04, X04B, X05, X05B, X05C |
| lec-09-topic-27 | T07 |
| lec-09-topic-24 | không có trang riêng; Tình huống 09.1 và 09.3 chỉ nhắc trong ghi chú diễn giả T07, M10; Tình huống 09.2 cho số liệu URL ở D01, D08 |

P00, P02, P03 không gắn chủ đề (phần đầu chương không mang mã, như Bài 08). Câu hỏi cuối cụm dùng bài tập của ghi chú: F19 (09.2), M15 (09.4), C14 (phản ví dụ của Định lý 09.37, Nhận xét 09.39), D19 (09.7, thuộc topic-20 theo vị trí trong ghi chú), E12 (09.8); T06 dùng Mệnh đề 09.11, Nhận xét 09.29, 09.51 và Bài tập 09.19.

## Danh sách mật độ và ngoại lệ

Trang trên 60 âm tiết, đều thuộc loại được trần 80: P02 (66), P04B (73), P07 (79), F18 (64), M14 (66), T02 (70), T04 (61), T05 (61). Loại: P02 mục tiêu; P07, F18, M14 bảng chi phí; T02 bảng tổng kết; T04 bảng so sánh và chi phí; P04B, T05 trả lời có điều kiện (K8). P03 (danh sách 7 mạch, hai cột) và D07B (6 quy tắc, hai cột) có trên 6 mục lá nhưng 5 dòng nhìn thấy.

Trang trên 6 dòng nhìn thấy (trần 8 cho bảng vết, bảng chi phí): P07 (8), F18 (7), M08 (7), M11 (8), M14 (8), C06 (7), C07 (7), C13 (7), D18 (7), E07 (8), E07B (7), T04 (7), X01B (7), X05B (7). Loại: M08, M11, C06, C07 (bảng vết và bảng kết quả cuối vết của cùng ví dụ), E07, E07B, X01B, X05B bảng vết; P07, F18, M14, D18, E11 bảng chi phí; T04 bảng so sánh và chi phí.

**Ngoại lệ T02** (bảng tổng kết 7 hàng + tiêu đề cột = 8 dòng, 70 âm tiết): phép gộp 9 của kế hoạch đặt bảy kết quả vào một bảng như ghi chú Mục 7.1; trần âm tiết 80 của bảng tổng kết được giữ; số dòng 8 bằng trần của bảng vết/chi phí. Trước (kế hoạch, hai trang T02/T03): 70 và 55 ước lượng; sau: 70 (8, 14). Không tách lại vì bảng tổng kết phải đọc được cùng lúc.

**Ngoại lệ P04B** (K8, trần 80): câu trả lời có điều kiện viết bằng lời thường cho cả năm mạch (rà soát vòng 1); trước 57, sau 73 âm tiết (5 dòng). T05 (61) thuộc cùng loại trang trả lời có điều kiện; bảng vết E07 tách thành E07/E07B (bước 1–5 và 6–15). Dòng dài nhất mọi trang nội dung ≤ 20 âm tiết; ≤ 3 công thức hiển thị mỗi trang; giả mã dài nhất 8 dòng (M12, D16), có Đầu vào/Đầu ra ngay trước.

Ghi chú diễn giả trên 150 âm tiết (giới hạn khoảng 250 cho chứng minh và lời giải): F07 (152), F14 (161), F18 (153), F19 (156), C01 (160), C14 (168), D04 (174), D06 (160), D13 (181), D15 (177), D17 (170), D17B (180), D19 (153), E09 (155), T05 (162), T06 (155), T07 (185), X05B (158).

## Gộp và tách so với `plan-deck.md`

| Phép | Trang kế hoạch | Trang deck | Lý do |
|---|---|---|---|
| gộp 1 | F02 + F03 | F03 | phương án gọn được duyệt (K2) |
| gộp 2 | F08 + F09 (Bổ đề 09.9 vào F10) | F09, F10 | phương án gọn được duyệt (K2) |
| gộp 3 | M02 + M03 | M03 | phương án gọn được duyệt (K2) |
| gộp 4 | C04 + C05 | C04 | phương án gọn được duyệt (K2) |
| gộp 5 | D02 + D04 | D04 | phương án gọn được duyệt (K2) |
| gộp 6 | D05 + D06 | D06 | phương án gọn được duyệt (K2) |
| gộp 7 | D13 + D14 | D13 | phương án gọn được duyệt (K2) |
| gộp 9 | T02 + T03 | T02 | phương án gọn được duyệt (K2) |
| gộp 11 (đảo lại) | E08 + E11 | E08, E11 | phép gộp 11 của kế hoạch được đảo ở lượt biên tập 1: E11 là trang chi phí riêng |
| tách | P04 | P04, P04B | hình cấu trúc bài (K5) đủ lớn; mật độ |
| tách | D07 | D07, D07B | 99 âm tiết |
| tách | D17 | D17, D17B | kế hoạch §6 cho phép khi > 60 |
| tách | E07 | E07, E07B | bảng vết 9 hàng; K8 chỉ cho ngoại lệ khi không tách được |
| tách | C03 | C03, C03B | rà soát vòng 1: một luận điểm mỗi trang |
| tách | E08 | E08, E11 | rà soát vòng 1: Mô hình đứng đầu trang chi phí, bảng sau chứng minh |

Không áp phép gộp 8 (E05 giữ trang chứng minh) và 10 (M14 giữ trong mạch), theo K2. Mã trang của kế hoạch được giữ; các mã bị gộp (F02, F08, M02, C05, D02, D05, D14, T03) không còn trong deck; E11 có trong deck (trang chi phí phần tử phổ biến).

## Hành trình chủ đề của ghi chú bài giảng

Cập nhật 2026-11-04 theo `note-topic-id` của ghi chú; thay bảng `L09-N01…N10` cũ. Phần trang chiếu ở trên đã được viết lại theo deck mới (2026-11-04).

| `note-topic-id` | Vai trò và kết nối vào–ra | Kiến thức đầu vào → sản phẩm | Thành phần trình bày |
|---|---|---|---|
| `lec-09-topic-01` | Cầu nối vào chương; nhận Bài 08, 06, 05 và công cụ xác suất, cấp cho Mục 1–6. | Kết quả các bài trước → phát biểu lại đúng giả thiết. | Danh sách nhóm kết quả kèm số hiệu và phát biểu lại. |
| `lec-09-topic-02` | Mở từ yêu cầu Bài 08 để ngỏ; đặt năm đại lượng và chi phí lời giải chính xác, ra năm nhu cầu. | Mô hình dòng → $f_u$, $F_p$, cửa sổ trượt, Nhận xét 09.3. | Hình cấu trúc chương, Ví dụ 09.1–09.2, Định nghĩa 09.1–09.2, Bài tập 09.1, đoạn kết mục. |
| `lec-09-topic-03` | Nhận nhu cầu $F_0$; chứng tỏ đếm chính xác tốn 512 MiB, ra nhu cầu ước lượng. | Vector bit → cận dưới tất định (Nhận xét 09.4). | Đoạn bài toán, nhận xét có lập luận đếm. |
| `lec-09-topic-04` | Đưa ra ước lượng $2^R$; ra bất biến dùng cho phân tích. | Băm tất định → chạy Thuật toán 09.6, Mệnh đề 09.7. | Trực giác, Ví dụ 09.3–09.4, định nghĩa, thuật toán, chứng minh bất biến. |
| `lec-09-topic-05` | Nhận $R$; đặt mô hình băm lý tưởng và cận hai phía, ra nhu cầu gộp. | Độc lập, cận hợp, $1-z\le e^{-z}$ → Định lý 09.10. | Định nghĩa 09.8, Bổ đề 09.9, định lý bốn phần, chứng minh theo bước, phản ví dụ khi bỏ giả thiết, Ví dụ 09.5 với hình ngưỡng. |
| `lec-09-topic-06` | Nhận nhu cầu gộp; chỉ ra phân phối đuôi nặng và trung vị lũy thừa của 2, ra phép gộp hai bước. | Kỳ vọng, nhị thức → Mệnh đề 09.11, Bổ đề 09.14, Hệ quả 09.15. | Ví dụ 09.6, Thuật toán 09.13, bảng chi phí. |
| `lec-09-topic-07` | Đóng Mục 2 bằng chi phí và thực hành; ra mẫu cho Tình huống 09.1. | Số bit → Mệnh đề 09.16, Nhận xét 09.17–09.18. | Ví dụ 368 byte, nhầm lẫn, Bài tập 09.2–09.3, đoạn kết mục. |
| `lec-09-topic-08` | Nhận giới hạn của $F_0$; đặt biến AMS. | Hồ chứa cỡ 1 → $v_i$, $X$. | Trực giác, Ví dụ 09.7, hình ba biến, Định nghĩa 09.19, Thuật toán 09.20. |
| `lec-09-topic-09` | Chứng minh không chệch; ra kết quả cho Mục 3.3–3.4. | Tuyến tính kỳ vọng → Bổ đề 09.21, Định lý 09.22. | Chứng minh theo bước, phản ví dụ, Ví dụ 09.8 (phương sai). |
| `lec-09-topic-10` | Mở rộng sang $F_p$ bằng cùng chứng minh. | Tổng lồng nhau → Hệ quả 09.23. | Chu trình rút gọn: hệ quả, Ví dụ 09.9. |
| `lec-09-topic-11` | Bỏ giả thiết biết $r$; ra hồ chứa vị trí cho Tình huống 09.3. | Định lý 08.17 → Thuật toán 09.24, Mệnh đề 09.25, Hệ quả 09.26. | Ví dụ 09.10, nhận xét độc lập, Bài tập 09.4–09.5, đoạn kết mục. |
| `lec-09-topic-12` | Nhận giới hạn của $F_2$; đặt bài toán phần tử nặng. | Tần suất → bài toán $(\varepsilon,\kappa)$. | Đoạn bài toán, Định nghĩa 09.30, ví dụ ngưỡng. |
| `lec-09-topic-13` | Cấp hai công cụ cho Mục 4.4. | Xác suất → họ băm phổ dụng, Bổ đề 09.32. | Định nghĩa 09.31, ví dụ họ BHK, phản ví dụ hàm hằng. |
| `lec-09-topic-14` | Dựng bảng Count-Min. | Băm, mảng đếm → Định nghĩa 09.33, Thuật toán 09.34. | Trực giác, Ví dụ 09.11–09.12, bảng chi phí. |
| `lec-09-topic-15` | Chứng minh bảo đảm; ra nhu cầu dữ liệu gần đây. | Markov, độc lập các hàng → Định lý 09.37, Hệ quả 09.38. | Bổ đề 09.35–09.36, chứng minh, Bài tập 09.6, thực hành, đoạn kết mục. |
| `lec-09-topic-16` | Mở Mục 5 bằng dòng bit chỉ báo; ra nhu cầu xấp xỉ. | Đếm trạng thái → Mệnh đề 09.41. | Ví dụ 09.13, chứng minh theo bước. |
| `lec-09-topic-17` | Đặt biểu diễn DGIM. | Lũy thừa của 2 → Định nghĩa 09.42, Mệnh đề 09.44. | Ví dụ 09.14, hình trạng thái, Nhận xét 09.43. |
| `lec-09-topic-18` | Truy vấn và cận 50%. | Quy tắc 4 → Thuật toán 09.45, Định lý 09.46. | Ví dụ 09.15, chứng minh, phản ví dụ, thực hành. |
| `lec-09-topic-19` | Cập nhật giữ sáu quy tắc; ra chi phí khấu hao. | Bất biến vòng lặp, thế năng → Thuật toán 09.47, Định lý 09.48, Mệnh đề 09.49. | Ví dụ 09.16, hình cập nhật, bảng chi phí. |
| `lec-09-topic-20` | Đọc thêm và thực hành sau DGIM. | —→ giảm sai số, tổng số nguyên. | Nhận xét 09.50–09.51, Bài tập 09.7, đoạn kết mục. |
| `lec-09-topic-21` | Nhận giới hạn của cửa sổ trượt; đặt cửa sổ suy giảm. | Cấp số nhân → Định nghĩa 09.52, Mệnh đề 09.53. | Ví dụ 09.17–09.18, hình trọng số, Nhận xét 09.54. |
| `lec-09-topic-22` | Theo dõi phần tử phổ biến; ra bảo đảm thứ năm cho Mục 7. | Tổng $<1/c$ → Thuật toán 09.55, Định lý 09.56. | Ví dụ 09.19, chứng minh, Bài tập 09.8, đoạn kết mục. |
| `lec-09-topic-23` | Hội tụ Mục 2–6; chọn phác thảo cho năm yêu cầu. | Năm bảo đảm → hai bảng, quy trình chọn. | Bảng kết quả–giả thiết, bảng thuật toán, Ví dụ 09.20, Bài tập 09.9. |
| `lec-09-topic-24` | Dẫn lý thuyết ra ba bài toán, một bài vi phạm giả thiết. | Mục 2–6 → Tình huống 09.1–09.3. | Năm phần mỗi tình huống, dẫn ngược lý thuyết. |
| `lec-09-topic-25` | Kết chương, nối Bài 10. | Cả chương → chuỗi kết quả. | Đoạn kể 7 câu, kết quả theo mục, công thức, giả thiết hay bị bỏ quên. |
| `lec-09-topic-26` | Kiểm sáu mục tiêu. | Cả chương → lời giải kiểm được. | Ba mức, gợi ý, lời giải; năm bài MMDS vận dụng trên lớp. |
| `lec-09-topic-27` | Mở rộng không bắt buộc. | —→ hướng đọc tiếp. | Danh mục tài liệu, ghi công MMDS. |
