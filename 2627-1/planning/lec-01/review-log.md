# Nhật ký rà soát Bài 1

## Sửa sau recheck (2026-10-14)

Theo `recheck-d01.md` và giao việc của điều phối viên; tác tử soạn `fork`, Opus 5.5, effort `high`; không commit.

| Mức độ | Trang chiếu | Phát hiện | Quyết định |
|---|---|---|---|
| nhẹ | ghi chú D01 | câu "Bốn dòng cụ thể hóa…" sai sau khi bảng còn hai dòng; câu đầu lấy bảng làm chủ ngữ | sửa: bỏ câu; câu đầu "Hai năng lực giải thích và lựa chọn ứng với CLO1–CLO2; …" |
| nhẹ | F04 dòng 1 | "tránh đọc lại" quá mạnh | sửa: "sắp hoặc băm theo khóa (Bài 12, 15) giảm đọc lại" |
| nhẹ | G01 | hàng chi phí đọc ghi thiếu giả thiết đếm $F$, đứng lệch thứ tự P04 | sửa: giả thiết "khối chưa có trong bộ đệm"; hàng chuyển lên đầu bảng, khớp thứ tự P04 (79/80 âm tiết) |
| nhẹ | review-log | quy ước đếm âm tiết chưa ghi | sửa: ghi dưới đây |
| nhẹ | ghi chú G03 | *Foundations of Data Science* thiếu mục, trang | sửa: "đọc trọn Chương 1–2" |

**Quy ước đếm mật độ.** `scratchpad/w01/cap01.py` đếm token có chữ cái (tách theo khoảng trắng, token phải chứa ít nhất một chữ cái), bỏ tiêu đề trang, công thức KaTeX, khối mã `pre`, SVG nội dòng và ghi chú diễn giả; mỗi `p`, `li`, hàng bảng là một dòng khi xét trần 20 âm tiết. Số liệu "trước" của kế hoạch theo cùng quy ước.

Kiểm: `cap01.py` D01 36, F04 78, G01 79 (trần 80), không dòng vượt 20 âm tiết; Playwright cổng 8771 toàn deck ở 1600×900 và 390×844: 0 lỗi, 0 cảnh báo KaTeX, 0 `.katex-error`, không tràn; đã xem ảnh D01, F04, G01; `git diff --check` sạch.


## Lượt sửa sau rà ba vai (2026-10-14)

**Giao việc.** Điều phối viên giao tác tử soạn (`fork`, Opus 5.5, effort `high`) sửa theo `fix-d01.md`, hợp nhất ba báo cáo rà chỉ đọc (`review-d01-math.md`, `review-d01-storyline.md`, `review-d01-student.md`; ba tác tử rà `fork` Opus 5.5 theo lệnh gọi của điều phối viên; không có phát hiện chặn bàn giao hay nghiêm trọng). Phạm vi ghi mở rộng: ghi chú `lec02-s01-07` và review-log 02; ghi chú deck 05 và review-log 05. Không sửa CSS. Không commit.

**Quyết định cho từng phát hiện.** Mã: T = rà toán, M = mạch viết, S = sinh viên.

| Mã | Mức độ | Trang chiếu | Quyết định |
|---|---|---|---|
| T1, M3, S2 | trung bình | P04, F04 | sửa: danh sách không đánh số; dòng cuối "Lưu trú độc lập: kỳ vọng khoảng $249\,750$ biến cố trùng…" (dùng "biến cố" như F03, không "cặp", vì kỳ vọng đếm biến cố cặp người – cặp ngày); F04 dòng khối đọc ghi: "quét lại tốn khối đọc ghi; sắp hoặc băm theo khóa (Bài 12, 15) tránh đọc lại", ghi chú nối về kho tài liệu trên đĩa |
| T6, S1 | nhẹ, trung bình | P03, P04 ($R$ trước định nghĩa) | sửa: dòng Ký hiệu P02 thêm "$R$ là tập cặp đạt ngưỡng"; tên học phần tiên quyết vào ghi chú (P02 58/60) |
| M1, T2 | trung bình | G01 | sửa: thêm hàng "Chi phí đọc ghi \| dữ liệu vượt bộ nhớ \| một lượt $F$ khối; đọc và ghi $2F$"; ghi chú "hai tập cùng rỗng làm hợp rỗng"; câu quyết định thiết kế thay bằng câu về mô hình chi phí; rút ô để giữ 78/80 |
| T3, S nhẹ, M10 | trung bình, nhẹ | G02, F03, F05 | sửa: câu 2 thay bằng câu dựa trên hàng chi phí đọc ghi của G01 (ba lượt, đáp $6F$); lời giải câu 3 nêu độc lập giữa hai người khi lấy $1/H$; F03 "$X$ là tổng các chỉ báo trùng…"; ghi chú F05 "nhờ hai người chọn độc lập và đều". Câu đếm từ chạy lại (cầu nối Bài 02) bỏ khỏi G02; dòng chuẩn bị Bài 02 vẫn ở G03 |
| T4, S | nhẹ, trung bình | C07 | sửa: "Kiểm một cặp (trộn hai danh sách) \| $N(N-1)/2$ \| $\le2L$ phép so sánh \| $\le N(N-1)L$, tức $O(N^2L)$"; ghi chú nêu vì sao $\le2L$ |
| T5, M, S | nhẹ | C18, C06 | sửa: Duy trì "cặp mới chưa từng xét…"; tiêu đề C06 "Tính đúng: bất biến của xét mọi cặp", C18 "Tính đúng: khởi tạo, duy trì, kết thúc" |
| M4 | trung bình | A01; storyboard | sửa: thêm dòng Đầu ra (kèm số 55, 25, 0); câu kết nêu giới hạn tệp vượt bộ nhớ; storyboard ghi một mô tả (khuôn tình huống cộng bảng dữ kiện), 8 dòng kể cả bảng |
| M7 | trung bình | D01 ↔ E02, E03 | sửa: D01 còn hai năng lực (CLO1–CLO2), hai năng lực còn lại do E02, E03 cụ thể hóa; phút D01 1 → 0,5, E02 1,5 → 2 |
| M8, S | trung bình | G03, P01 | sửa: G03 ghi MMDS ấn bản 3 (2020) §1.2 tr.6–8, §1.3.4 tr.13, §3.1 tr.73–75; DSC Chương 14–15; Nelson–Gailly ấn bản 2; Blum, Hopcroft, Kannan (2020), *Foundations of Data Science*, Chương 1–2; P01 thêm tên sách BHK. G03 7 dòng (ngoại lệ trang nguồn) |
| M6, S | trung bình, nhẹ | C02 | sửa: "đoạn ký tự (shingle)"; Kết luận "$J(S,T)\ge\tau$ khi và chỉ khi $\tau\le3/8$" (không dùng quy tắc chọn cặp trước C03) |
| S | nhẹ | P00 | sửa: "Yêu cầu dữ liệu lớn chỉ thành bài toán thuật toán khi đã chốt đầu ra, biểu diễn, giới hạn tài nguyên, mức chính xác." (25; câu của `fix-d01.md` có "và" thành 26, nên bỏ "và") |
| M9, S | trung bình, nhẹ | storyboard | sửa: mỗi trang mới một phiếu đủ chín trường; P04↔F04 đối ứng trong phiếu P04; ngoại lệ 8 dòng P01; A01 một mô tả |
| M5 (T5 của vai mạch viết) | trung bình | deck 02 ghi chú `lec02-s01-07` | sửa: tên trang dẫn thành "Các tiêu chí đánh giá", "Tính đúng: khởi tạo, duy trì, kết thúc" và "Nguồn và tài liệu đọc"; G03 thêm "tính kết hợp và giao hoán"; ghi review-log 02 |
| M19 | nhẹ | deck 05 ghi chú trang Tiên quyết | sửa: "Thuật toán: xét mọi cặp"; ghi review-log 05 |
| M11 | nhẹ | ghi chú P04 | sửa: dòng giảm cặp lấy điều kiện đủ ở câu hỏi hậu kiểm và đặt vào Bài 05–06 |
| M12 | nhẹ | E01, ghi chú D02, D11 | sửa: tên năm nhóm theo bản đồ (hình D02); lệch với `sources/source.md` ghi mở |
| M13 | nhẹ | D08 | sửa: "phần còn lại phân theo bước nhảy ngẫu nhiên" |
| M14 | nhẹ | ghi chú B02, D03 (câu nối) | sửa: câu nối chuyển về cuối; B09, E03, D07: giữ (câu nối nằm ở trang cuối nội dung trước trang câu hỏi, trang câu hỏi có lời giải thay câu nối) |
| M15 | nhẹ | C05 | sửa: ghi chú nêu thứ tự trình bày các trang |
| M16 | nhẹ | ghi chú CT | sửa: phạm vi đúng (đếm phép tính trên bài toán mẫu; tiêu chí khác minh họa bằng ví dụ đã gặp) |
| M17 | nhẹ | ghi chú GT, G01, F04 | sửa: bỏ "Không có khái niệm mới."; G01 câu thiết kế thay; F04 bỏ câu ba vế và câu lặp |
| M18, S | nhẹ | ghi chú A02, F02, F03, B09, R02 | sửa: bỏ câu lặp A02; F02 dòng Nguồn về cuối, câu 100 chỗ viết lại; số theo dấu phẩy và khoảng trắng nhóm nghìn |
| T7, S | nhẹ | B12 câu 2 | sửa: câu hỏi "vì sao quét lại tốn khối"; lời giải thêm phép đếm $5000\cdot400+100=2\,000\,100$ lần chuyển khối (DSC Chương 15, trang chiếu 24), ghi là số đếm theo mô hình |
| S | nhẹ | R01, R02, R04 | sửa: "kỳ vọng số biến cố trùng (sách: số cặp nghi vấn)"; "từng phần"; R04 "có nên cho rằng…" |
| S | nhẹ | E06 | sửa: bỏ hình lặp C15, thay dòng "Nhắc lại: recall@5 $=3/5$" |
| S | nhẹ | P01 8 dòng | ghi ngoại lệ trang Nội dung trong storyboard |
| S | nhẹ | nhãn SVG ≈ 0,73 cỡ thân (D08, C15, E06) | giữ: trên ngưỡng 0,65 cho nhãn ngắn; SVG không đổi; mở |
| S | nhẹ | phông đơn cách lệch dấu (C04, mọi deck) | mở: CSS chung, ngoài phạm vi |
| S | nhẹ | mẫu "Hình … không phải …" trong khoảng 10 ghi chú | mở: giữ những câu chặn cách hiểu sai cụ thể; rút ở đợt ghi chú sau |

**Kiểm tra.** `cap01.py`: không trang trần 60 vượt 60 (P02 58, P04 59, C07 59, C18 60); P03 80, G01 78, E03 79, F04 78, G03 70 (trần 80); không dòng nào vượt 20 âm tiết; luận đề 25. Thẻ HTML cân bằng (dựng lại bằng bộ dựng). Chromium Playwright cổng 8771, toàn deck 01 ở 1600×900 và 390×844 (ảnh riêng P00, P02, P04, P01, A01, C02, C07, C18, D01, F04, G01, G02, G03, E06, B12, F03): 0 lỗi, 0 cảnh báo KaTeX, 0 `.katex-error`, không tràn; P01 đáy 818/864; deck 02 (trang s01-07 và toàn deck) sạch ở hai cỡ. Đã tự xem ảnh các trang đổi. `git diff --check` sạch.

**Tác động.** Deck 02 và deck 05: chỉ ghi chú diễn giả (tên trang dẫn). Ghi chú bài giảng 01: G02 câu 2 đổi (nay về chi phí đọc ghi), cần đồng bộ ở đợt ghi chú; các điểm đã ghi trước (hai con trỏ, LSH, số mục tiêu) vẫn mở.


## Sửa toàn diện theo chuẩn 2026-10-14

**Giao việc.** Điều phối viên giao tác tử soạn (một tác tử ghi tệp; loại `fork`, Claude Opus 5.5, effort `high`, theo lệnh gọi Agent của điều phối viên). Phạm vi ghi: deck Bài 01, ba tệp `planning/lec-01/` và `lecture-style.css` chỉ để thêm tối đa 5 quy tắc giới hạn bởi `.lecture-bigdata`. Căn cứ: `AGENTS.md`, `slide_authoring_standard.md`, deck mẫu Bài 06, `plan-lec01.md`, mục "Bài 01" và "Chung cho mọi bài" của `decisions-decks.md`. Skill `no-ai-slop` nạp ở chế độ Edit. Không commit. Deck dựng lại bằng bộ dựng `scratchpad/w01/build.py` với đặc tả `spec/s0…s9.py`.

**Quyết định đã áp dụng.**

| # | Quyết định | Thực hiện |
|---:|---|---|
| 1 | Gộp D+E thành mạch 4; F thành mạch 5; mạch 6 tổng kết mới; mạch 7 bài tập; giữ 7 section | `id="mach-4"` DT "Năm nhóm thuật toán và cách học", `mach-5` FT, `mach-6` GT mới, `mach-7` RT; `aria-label` bằng tên mạch; trang Nội dung khớp từng chữ |
| 2 | Luận đề bốn thành phần, ≤ 25 âm tiết | "Một yêu cầu dữ liệu lớn thành bài toán thuật toán khi chốt đầu ra, biểu diễn, giới hạn tài nguyên, mức chính xác." (24) |
| 3 | Bỏ D00, E00, E05, F00; gộp E04 | nội dung chuyển vào ghi chú DT, D01, FT, dòng Nhu cầu F01, G02 câu 1–2, G03 |
| 4 | Thêm A10, B12, D11 (phương án 83 trang); mục phân bổ thời gian | 83 trang (75 giảng, 8 bài tập); storyboard có mục phân bổ |
| 5 | A01 giữ bảng, ngoại lệ 7 dòng | ghi trong storyboard |
| 6 | `.course-deck` với lớp dùng chung; tối đa 5 quy tắc `.lecture-bigdata` | bỏ khối `<style>` 29 quy tắc; gốc `reveal course-deck lecture-bigdata`; thêm 4 quy tắc (chiều cao hình) cạnh khối `.lecture-lsh` |
| 7 | Chấp nhận tiêu đề in hoa | theo `.course-deck` |
| 8 | Bỏ dòng nguồn ở R00 | bỏ; trang đề bài R01–R05 và bước R06 giữ dòng "Nguồn: MMDS, Bài …, tr.8" lớp `ex-note` |
| 9 | LSH theo Bài 06; "véc-tơ/vector" ngoài đợt | "băm nhạy cảm theo tính cục bộ (LSH)" ở D04, ghi chú C16; "véc-tơ" giữ, lệch với Bài 02–06 ghi ở đây |
| 10 | MMDS "ấn bản 3 (2020)" | ghi ở P01, G03; `sources/source.md` dòng 42 ghi bản 2014: lệch nguồn, chưa sửa (ngoài phạm vi) |
| 11 | Rà rút gọn ba vai | chưa chạy; điều phối viên giao |

**Hai điểm ngoài phạm vi đã ghi ở Bài 05.** (1) Ghi chú C04, C07 hứa "Bài 05 phân tích hai con trỏ": bỏ; ghi chú C04 nói hai con trỏ là phép trộn hai danh sách đã sắp của học phần tiên quyết, nguồn C07 bỏ "Bài 05 thuật toán hai con trỏ". (2) Lộ trình "Bài 05–06 giảm số cặp": A06 (ghi chú), D04 (mặt trang và ghi chú), F04 (mặt trang dòng 4 và ghi chú), D11 (lời giải) nay nói Bài 05 biểu diễn bằng tập đoạn ký tự và chữ ký MinHash, Bài 06 phân dải LSH để chọn cặp ứng viên.

**CSS chung.** Thêm vào `lecture-style.css` ngay sau khối Bài 06 (`.lecture-lsh`):
`.reveal.course-deck.lecture-bigdata .l01-figure { margin: 10px 0; }`, `.l01-figure img { display:block; width:100%; max-height:320px; margin:0 auto; object-fit:contain; }`, `.l01-short img { max-height:245px; }`, `.l01-map img { max-height:470px; }`. Phạm vi ảnh hưởng: mọi selector giới hạn bởi `.lecture-bigdata`, chỉ deck 01 mang lớp này; không sửa quy tắc có sẵn. Kiểm hồi quy bằng Chromium Playwright cổng 8771 trên toàn bộ trang của Bài 02 (93), Bài 03 (72) và Bài 06 ở 1600×900 và 390×844: 0 lỗi console, 0 cảnh báo KaTeX, 0 `.katex-error`, không tràn khung, không cuộn ngang.

**Mặt trang.** Mọi trang nội dung dùng `example-slide` (C07 `cost-slide`, P01 `agenda-slide`, P00 `title-slide`); `.card` → `.ex-card`, `.grid2` → `.ex-grid2`, `.trace` → `.ex-table` (`th scope="col"`), `.formula` → `p.ex-equation`, `.check` → dòng "Câu hỏi:" hoặc `p.ex-takeaway`, `img.figure` → `figure.l01-figure`; không `style`, `fragment`, `.dense`. Hai công thức có chữ Việt trong `\text{}` (C15, F06) viết lại: chữ ra ngoài KaTeX. Nhãn ngoài danh sách bỏ ("Khó khăn:", "Sau buổi học:", "Sản phẩm:", "Gợi ý:" trên mặt trang).

**Ghi chú diễn giả.** Mọi ghi chú bọc `<p>`, có câu "Nguồn:" tách đoạn; bỏ câu lấy tài liệu làm chủ ngữ ("Trước hết…", "Phần tiếp theo…", "Các ví dụ tiếp theo…", "phần tiếp theo…", "buổi này"); "slide" → "trang chiếu"; "Gợi ý chấm" → "Hướng dẫn chấm"; chuẩn hóa khoảng trắng dính ("Bài07", "student100khối", "lớp8–9"…); nguồn "source.md" thay bằng đề cương. Ghi chú A03, A06, A07 rút về ≤ 150 âm tiết. Ký tự "<" trong công thức ghi chú được thoát.

**Mật độ (trước → sau).** Đếm bằng `scratchpad/w01/cap01.py`; số trước theo `plan-lec01.md` §0.1.

| Chỉ số | Trước (77 trang) | Sau (83 trang) |
|---|---:|---:|
| Trung vị trang nội dung | 52 | 46 |
| Trang nội dung > 60 âm tiết | 25 | 16 (đều thuộc nhóm trần 80) |
| Trang vượt trần | 17 | 0 |
| Trang > 80 âm tiết | 11 | 0 |
| Mặt trang dài nhất | 124 (E01) | 80 |
| Dòng > 20 âm tiết (ngoài dòng dẫn mạch) | 12 trang | 0 |
| Ghi chú > 150 âm tiết | 8 | 1 (R05, lời giải, 210 ≤ 250) |

**Kiểm tra.** `git diff --check` sạch (deck, CSS, ba tệp kế hoạch). Thẻ HTML cân bằng; 83 `data-slide-id` duy nhất, không `id` trùng; 7 section ngoài có `aria-label`. Chromium Playwright cổng 8771, cả 83 trang ở 1600×900: 0 lỗi console, 0 cảnh báo KaTeX, 0 `.katex-error`, 0 yêu cầu mạng ngoài, không cuộn ngang, không phần tử vượt khung; đáy thấp nhất D04 796/864 px (chân trang 845); cỡ chữ nhỏ nhất 24 px (dòng nguồn `ex-note`), 25 px (ô bảng). 390×844: 0 lỗi, không tràn phải. Đã tự xem ảnh 1600×900 của cả 83 trang (10 ảnh ghép) và ảnh hẹp D09.

**Vấn đề mở.**

| Mức độ | Trang chiếu | Vấn đề | Đề xuất | Trạng thái |
|---|---|---|---|---|
| nhẹ | mạch 1 | chân trang ẩn khi section đầu hiện (CSS chung) | xem ở đợt CSS chung | mở |
| nhẹ | toàn bài | "véc-tơ" khác "véc tơ"/"vector" của Bài 02–06 | thống nhất ở đợt thuật ngữ | mở |
| nhẹ | `sources/source.md` dòng 42 | MMDS ghi bản 2014, deck ghi ấn bản 3 (2020) | sửa nguồn ở đợt sau | mở |
| nhẹ | `img/lec-01/` | hai SVG mồ côi có từ trước (`giao-thoa-khai-pha-du-lieu.svg`, `the-tich-gan-bien.svg`) | dọn ở đợt hình | mở |
| — | toàn bài | rà ba vai (sinh viên kèm mật độ; độ chính xác toán; kết nối và mạch viết) | điều phối viên giao | chờ |

**Tác động tới ghi chú bài giảng `materials/lec-01/lecture-note.md`** (không sửa đợt này): ký hiệu, ví dụ, con số và kết luận không đổi. Cần sửa ở đợt ghi chú: dòng 246 còn câu "Bài 05 phân tích thao tác đó" (hai con trỏ); dòng 399, 427 viết "Băm nhạy cảm cục bộ (LSH)" thay vì "băm nhạy cảm theo tính cục bộ"; ghi chú có 3 mục tiêu, deck 5; chưa có mục tổng kết riêng. `index.html` không đổi.


## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 1 gồm Bài 01–05; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | L01-BT | Dòng dữ liệu, nén và truy vấn trên đĩa | Muốn tiếp nhận, lưu và khai thác dữ liệu lớn, phải tính đến bộ nhớ hữu hạn và chi phí đọc đĩa. |
| 3 | L01-CT | Đặc tả và đánh giá thuật toán | Muốn chọn lời giải cho bài toán tìm cặp gần trùng, phải đặc tả đầu ra rồi xét tính đúng và chi phí. |
| 4 | L01-DT | Năm nhóm thuật toán của học phần | Muốn biết mỗi bài sau giải nhu cầu nào, phải đối chiếu phương pháp với các bài toán đã gặp. |
| 5 | L01-ET | Chuẩn bị và cách học | Muốn học các nhóm thuật toán, phải biết phần kiến thức nền cần ôn và sản phẩm chứng tỏ đã hiểu. |
| 6 | L01-FT | Mẫu trùng ngẫu nhiên và suy luận | Muốn dùng mẫu trùng tìm được làm căn cứ, phải ước lượng số trùng ngẫu nhiên theo mô hình nền. |
| 7 | L01-RT | Bài tập vận dụng | Muốn kiểm mô hình lưu trú, phải đổi quy mô, tiêu chuẩn trùng và đơn vị đếm rồi tính lại kỳ vọng. |

Mã `-00` không dùng được vì L01-B00 … L01-R00 đã là các trang mở phần có nội dung (thẻ, bảng); các trang này không phải trang một dòng "A. Tên phần" nên được giữ nguyên và đứng thứ hai trong mạch. Mã mới viết `L01-<chữ>T` theo cách viết liền của bài. Dòng dẫn 20–23 âm tiết; từ khóa đúng năm cụm; ghi chú diễn giả 71–87 âm tiết, nêu kết quả kế thừa, nhiệm vụ và kết quả giao, viết từ nội dung các trang trong mạch. Số trang: 71 → 77.

Trang Nội dung: L01-P01 "Nội dung buổi học" đã có nhưng là ba thẻ nhóm không khớp các mạch; ba thẻ được thay bằng danh sách đánh số 1–7 (hai cột `ol`, `ol start="5"`), tên trùng từng chữ với tên mạch, mạch 1 là "Tổng hợp và tìm kiếm dữ liệu web". Trang gộp mục tiêu và nội dung, mặt trang khoảng 95 âm tiết, vượt trần 80; theo phạm vi đợt này chỉ đánh số danh sách, chưa tách. Notes viết lại thành một câu cho mỗi mạch, nêu quan hệ suy luận. Không đổi tiêu đề trang.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (trang Tiên quyết và quy ước, trang Vấn đề trung tâm, câu luận đề trên trang bìa); tách trang L01-P01 về trần 80 âm tiết; chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Bài 01 còn khối `<style>` riêng và không mang lớp `.course-deck`; đây là sai lệch có từ trước, ngoài phạm vi đợt này. Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 84/84; 77 `data-slide-id` và 6 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/7` mở đúng trang tiêu đề mạch 2–7 (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 716 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; danh sách trang Nội dung đọc ra đúng bảy tên mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang tiêu đề mạch và trang Nội dung được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.


### Sửa sau rà lại đợt 1

Sau rà lại độc lập (báo cáo đọc lại đợt 1, không có phát hiện chặn bàn giao hoặc nghiêm trọng), sửa hai điểm. (1) Mức trung bình: từ khóa của L01-DT là "MapReduce · PageRank · MinHash và LSH · Dòng dữ liệu · Nén và đọc ghi", năm cụm dưới tên "Năm nhóm thuật toán của học phần" nhưng không khớp năm nhóm. Đổi thành "Phân tán và xếp hạng · Tương đồng và tìm gần · Dòng và cửa sổ · Nén và khôi phục · Lưu trữ và truy vấn", đúng từng chữ với năm nhãn nhóm trên hình của L01-D02 (`ban-do-hoc-phan.svg`). Notes của L01-D02 dùng tên ngắn hơn (tương đồng; dòng dữ liệu; nén); chọn tên trên mặt hình vì đó là chữ sinh viên thấy trên trang. (2) Mức nhẹ: ghi ngoại lệ tạm thời về mật độ của L01-P01 (89–95 âm tiết, trần 80) vào storyboard, cả mục bổ sung và hàng L01-P01; tách trang ở đợt sau. Kiểm lại: `#/4` vẫn mở `mach-4`, khối tiêu đề không tràn khung ở 1600×900; `git diff --check` sạch.


### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 6 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## ER-004 — R, bài tập về phép đếm và suy luận

ER-004 hoàn tất. Bốn commit nội dung đã push riêng và xác nhận bằng git ls-remote: D `9ca7a455a9738a170a28906a8216a4d36458ed04`, E `b2ab434932e073702fdc7a4981aff3a07d5dc19a`, F `ea364a09a64718cdbdd309eb88111d9495c4719a`, R `7cb48d523e3d22b0e70769c51edd9668ddc3aa23`. Lượt Chromium cuối sau bổ sung nguồn trong Markdown vẫn đạt toàn bộ 71 trang và viewer; sáu khối bài tập giữ nguyên. Checklist chỉ được tick sau xác nhận push. Bản cập nhật trạng thái không thay học liệu đã kiểm định.

Phần R có 7 trang, 60 phút: mở phần → dựng mô hình gốc → thay quy mô → trùng ba ngày → bài mua hàng → đơn vị đếm → lời giải có điều kiện. Thêm R06 và hai SVG; phân lại thời lượng trong phần, không thêm bài tập. Toàn bài có 71 trang, 7 phần ngoài; 64 trang giảng/120 phút và 7 trang bài tập/60 phút. HTML A–F giữ nguyên so với commit trước phần R.

Nguồn là MMDS mục 1.2.3–1.2.4, trang 7–8, Bài 1.2.1(a–c), Bài 1.2.2 và chú thích 3. Sáu khối đề, gợi ý, lời giải trong Markdown giữ nguyên từng ký tự so với HEAD trước phần R; phần giải thích, bảng và hình được thêm bên ngoài. Không tạo số liệu hay đổi giả thuyết nguồn. Chú thích trong nguồn yêu cầu chấp nhận giả thuyết của bài mua hàng để làm bài, không coi đó là kết luận về dữ liệu thực.

| Vai / phiên | Kết quả và quyết định |
|---|---|
| Writer ban đầu 79767 | Soạn mở phần sau lượt 95599 lỗi; giữ hai bài và bốn thành phần lời giải, cắt lời chào và lời nhấn rỗng |
| Storyboard 9258 | Xác nhận 60 phút; nhận sửa nguồn R02 riêng (a,b), R03 riêng (c). Bác số cơ sở khoảng 249875 do reviewer tự nêu: giá trị thật là 249749,99975025 |
| Sinh viên 88995 | Nhận sửa khoảng trắng trong alt và nói rõ MMDS/năm quan sát. Không sắp lại theo mã nội bộ hoặc đưa đáp án lên mặt slide bài tập |
| Giải thuật/nguồn 78020 | Nhận nguồn từng hàng cần chính xác. Bác cách hiểu phải ở một khách sạn cố định suốt ba ngày: trang 7 của mô hình 1.2.3 nói rõ khách sạn có thể khác giữa các ngày; trang 8 tiếp tục mô hình này |
| Toán 42115 | Xác nhận bốn giá trị kỳ vọng và bài mua hàng đúng; nhận thống nhất dấu thập phân trong notes và làm rõ cận xác suất bằng chỉ báo |
| Sư phạm 83491 | Nhận sửa khoảng trắng và nguồn; R06 là chia bước của cùng bài. Giữ cột nối theo nghĩa dẫn sang trang kế tiếp, không đổi thành nội dung lặp trong trang |
| Mạch 1745 | Không lỗi nghiêm trọng; F→R và R04→R06→R05 nối được. Làm rõ sản phẩm riêng của từng trang trong storyboard; R01 lập mô hình, R02 giải nên mức gợi ý khác nhau có chủ đích |
| Writer chỉnh sửa 7401 | Chạy sau đủ năm báo cáo, soạn hai câu về tập không thứ tự và chỉ báo không lớn hơn số đếm; tích hợp vào notes, giữ phân biệt xác suất nền và xác suất có điều kiện |

Lượt writer 95599 kết thúc với lỗi `model returned an empty or incomplete answer after all retries`; đã báo người dùng và dừng tích hợp, chạy lại cùng mô hình/provider với giới hạn đầu ra phù hợp. Các lượt hoàn tất trên có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter, xác nhận từ JSON runtime. Không đổi kênh hoặc gửi tệp bí mật.

Rà lại toán/nguồn 83837 đã đọc cả trang 7–8, xác nhận cách hiểu khách sạn có thể khác giữa các ngày, các kết quả kỳ vọng và cận chỉ báo. Báo cáo tự viết một dấu bằng sai khi thay tổ hợp bằng số làm tròn ở bước trung gian (b), không nằm trong học liệu; điều phối giữ phép tính tổ hợp chính xác đã tự kiểm. Rà mạch 57987 đọc đủ 135 dòng, xác nhận F04→E04→R00 và chuỗi bài tập liền mạch. Cả hai báo cáo hiểu cột cuối của bản trích thiếu header là từ khóa của trang hiện tại: bác đề xuất đổi cột vì bảng thật ghi rõ “Nối sang trang sau” ở dòng tiêu đề. R02 nối sang tiêu chuẩn ba ngày, R03 sang cặp lượt mua là đúng. Không còn lỗi nội dung hoặc hiển thị bắt buộc đã được xác minh. Runtime của hai lượt vẫn đúng model/provider nêu trên.

Điều phối kiểm độc lập bằng tổ hợp chính xác: cơ sở 249749,99975025; (a) 999499,9990005; (b) 249749,999875125; (c) 0,0830834999169165; bài mua hàng 0,00018981846904990663. Y đếm cặp lượt; chỉ báo của Y≥1 không lớn hơn Y nên Pr(Y≥1)≤E[Y] trong mô hình nền. Cận này không cho xác suất một cặp có ý định gì khi đã quan sát trùng.

Quill dùng rà thứ tự khái niệm, đơn vị đếm và các cầu F04/E04→R00, R03→R04→R06→R05. No-ai-slop dùng biên tập mặt trang, alt, notes và đoạn ghi chú mới; tự kiểm trực tiếp eval.md: giữ dữ kiện, giọng học thuật và giả thiết, cắt chỉ dẫn sản xuất, lời mở rỗng và diễn đạt lặp. Không cắt hướng dẫn học tập hoặc lời giải cần cho người học. Không tạo quill.json.

Kiểm Chromium trên bản 71 trang: rộng 1280×720 và hẹp 390×844; 7 phần, 70 notes (trang tên bài không cần notes), 120+60 phút. Không lỗi KaTeX/JavaScript/HTTP, ảnh hỏng hoặc yêu cầu mạng ngoài. SVG không chồng nhãn/vượt khung; đã xem toàn bộ R và phóng R04 sau sửa cuối. Cảnh báo hộp KaTeX A06 là cảnh báo đo đã có, ảnh không bị cắt. Viewer có 41 lượt nhúng hình, 54 mục lục, không tràn ngang; sáu khối gợi ý/lời giải gập khi đọc, bàn phím mở được và mở khi in. PDF slide có 71 trang. Liên kết chỉ mục/viewer và từ chối đường dẫn/số bài sai đạt. Index không đổi vì mô tả và liên kết vẫn đúng.

Codex Slides vẫn là nháp cũ 0 trang, không có Browser phù hợp; đã báo và kiểm trực tiếp RevealJS cục bộ theo ngoại lệ của kho. Không tuyên bố đã đồng bộ hoặc kiểm trên Codex Slides. Ảnh/PDF/gói rà soát ở /tmp/er004.8MWOn4, không đưa vào Git. Chỉ stage đầu ra Bài 01; giữ các thay đổi người dùng ngoài phạm vi.

## ER-004 — F, phản biện và kiểm định

Rà mạch cuối2520 đã đọc trọn798dòng, xác nhận đúng70slide và các nhómouter, F06trướcF03, câu nốiF04thu hồi gần trùng, E→F→Rliền mạch; không còn lỗi nghiêm trọng/chặn. Runtime requested/observed z-ai/glm-5.3-flash, provider OpenRouter. Fđủ điều kiện commit/push.

Phần F có9trang/16phút (8mãF và E04): mở phần, bài toán lưu trú, mô hình, xác suất, đơn vị đếm, kỳ vọng, giới hạn suy luận, thu hồi khung toàn bài và chuẩn bịMapReduce. Thêm2SVG, cập nhật N07/N08 và kế hoạch. Toàn bài70trang,7phần,120+60phút. D/Eđã push; HTML A–E vàR giữ nguyên trong commitF.

Writer50859soạn mở phần: giữ ba bước, sửa cách gọi mức trùng bình thường thành kỳ vọng dưới mô hình. Rà nguồn MMDS1.2.1–1.2.4tr.6–8, giữ P=10^9,T=1000,H=10^5,q=.01 và khách sạn có thể khác giữa ngày; không dựng hồ sơ quan sát giả.

| Vai / tiến trình | Báo cáo và quyết định |
|---|---|
| Storyboard62988 | Đúng16phút/cầu nối; sửa nguồn từng hàng, không gánMMDS2.2cho mọiF. Bác đề xuất chuyển hình sau công thức: hình trực giác chuẩn bị cho phép nhân. Bảng thật cóheader, gói trích không có |
| Sinh viên37273 | Nhận bổ sung thay số q²=10^-4và công thức kỳ vọng; đưa khác khách sạn giữa ngày lên hình. Không bịa thêm hồ sơ ngày1/ngày5/kháchsạnX; hình ký hiệu là mẫu cụ thể trong mô hình nguồn |
| Giải thuật54297 | Nhận tách sai khác đơn vị đếm khỏi sai khác do xấp xỉ tổ hợp; thêm theo mô hình nền ở mở phần. Giữ khoảng249750vì đây là giá trị làm tròn và đã định nghĩa kỳ vọng |
| Toán33146 | Kết luận mô hình đúng nhưng báo cáo tự viết sai số trung gian C(10^9,2), thiếu3số0; điều phối bác số đó, không có trong học liệu. Kiểm số nguyên độc lập rồi giao rà lại91515 |
| Sư phạm5127 | Nhận diễn đạt tuyến tính kỳ vọng bằng lời. Bác nhận địnhF06sauF03: thứ tựHTMLvàstoryboard đã làF06→F03. Giữ tênBonferroni trongnotes cùng mô tả, không dạy hiệu chỉnh kiểm định |
| Mạch27025 | Nhận tăng cầu nối F07→F04 bằng mẫu lưu trú rồi gần trùng. Bác đếm68trang/F8: Bcó12trang, E04thuộcF; HTMLthật70trang/F9. Không đổi dữ kiệnE05vì đây là vận dụng ví dụ đã học |
| Writer sửa97458/26234 | Lượt97458ghi draft nhưng lỗi tool-call limit; đã báo và dừng tích hợp. Lượt26234cùng mô hình hoàn tất; tích hợp thay số, tuyến tính và câu nối, bỏ câu dành cho người soạn |
| Toán rà lại91515 | Xác nhận đủ các số tổ hợp/tích/kỳ vọng, giả thiết độc lập và đơn vị đếm; không lỗi |

Lỗi OpenRouter đã báo nguyên văn: `model exceeded the tool-call limit (3)` ở writer97458; `model exceeded the tool-call limit (2)` ở reviewer mạch18567. Không đổi kênh/mô hình; chạy lại phạm vi hẹp và cho đọc toàn gói một lượt. Mọi lượt hoàn tất có requested_model=observed_model=z-ai/glm-5.3-flash, providerOpenRouter từJSONruntime.

Điều phối kiểm số nguyên: C(10^9,2)=499999999500000000; C(1000,2)=499500; tích249749999750250000000000, nhân10^-18cho249749.99975025. Xác suất1ngày10^-9và2ngày10^-18; tính tuyến tính không cần mọi phép thử độc lập. Không đồng nhất biến cố với cặp người và không suy xác suất phối hợp từ kỳ vọng.

Chromium rộng/hẹp toàn70trang,7phần,120+60phút; công thức, SVG, bàn phím, viewer và PDF70trang đạt, không tài nguyên hỏng/mạngngoài. Đã xem toànF và phóngF01/F03sau sửa; một cảnh báo đo hộp KaTeX A06đã có từ trước, ảnh không bị cắt. Quill rà toànmạch vì Fthu hồi/kếtluận thay đổi; no-ai-slop bỏ lời soạn thảo, làm rõ phép tính và giữ giả thiết. Codex Slides vẫn nháp0trang; kiểm trên RevealJS cục bộ.

## ER-004 — E, kết quả rà soát

Phần E sửa3trang thành6trang, có E00mở phần, E05vận dụng tập hợp, E06báo cáo thực nghiệm; thêm hoc-tap-san-pham.svg, dùng lại hình Jaccard và độ thu hồi. N06 trong ghi chú viết lại cùng mạch. Writer8112 soạn mở phần; giữ ba nhánh và bỏ chỉ dẫn người trình bày khỏi draft. Toàn bài66trang/7phần/120+60phút, E9phút. HTML ngoài E không đổi.

| Vai / tiến trình | Kết quả, quyết định |
|---|---|
| Storyboard82224 | Đúng thứ tự và9phút; thay mô tả sản phẩm lặp bằng sản phẩm riêng cho từng trang. Giữ IDổn định; E04thuộc phầnF |
| Sinh viên99447 | Xác nhận hai ví dụ tách rõ; các góp ý về dấu đóng/Markdown xen HTML là do gói ghép, không phải học liệu. Con số1/2trong bảng là phút, không phải thứ tự |
| Giải thuật75567 | Nhận ca J=τ được chọn và giải thích mẫu số độ thu hồi. Bác nhận định cao về F02: q²/H là một ngày, hai ngày là bình phương; công thức nằm F03ngoài trích, không sửa F ở commit E |
| Toán77999 | Không lỗi toán; nhận sửa khoảng trắng số/ký hiệu trong notes |
| Sư phạm71707 | Nhận làm rõ sản phẩm E05; giữ tự kiểm hậu kiểm vì C16/D04đã giải thích; không lặp lại toàn cơ chế |
| Mạch83039 | Xác nhận D→E→F và9phút; bác đảo thứ tự ghi chú vì gói ghép hai sản phẩm, ghi chú thật N06nằm trước N07 |
| Writer sửa88117 | Viết hai câu ca biên và mẫu số, đã tích hợp vào notes và ghi chú |
| Rà lại4835 | Xác nhận J=τ, Jaccard3/8 và recall3/5 đúng, mạch theo thứ tự hợp lệ. E04không nằm trong đoạn trích nhưng tồn tại trong outerF của HTML đầy đủ |

Mọi lượt hoàn tất có requested_model=observed_model=z-ai/glm-5.3-flash, provider OpenRouter. Lượt gọi reviewer đầu bị bộ duyệt quyền từ chối vì chưa nhận quyền gửi học liệu; điều phối báo nguyên nhân, đọc xác minh AGENTS.md dòng393, rồi gọi lại cùng kênh với điều khoản cho phép rõ. Được chấp thuận; không đổi kênh, không đọc/gửi .env hoặc bí mật.

Kiểm trực quan phát hiện E05sát chân trang; bỏ khoảng đệm công thức khối, giữ cỡ chữ. Chromium rộng/hẹp toàn66trang, SVG/KaTeX/ảnh/liên kết/bàn phím/viewer/PDF66trang đã kiểm; E05sau sửa không tràn. Quill giữ tuyến kiến thức→vận dụng→sản phẩm→báo cáo→trách nhiệm; no-ai-slop bỏ chỉ dẫn tác giả, sửa câu dính số và thay nhật ký bằng cặp gần trùng. Codex Slides vẫn nháp0trang, kiểm RevealJS cục bộ. Index không đổi vì thông tin và liên kết vẫn đúng.

### D — kết quả phản biện và kiểm định

| Vai / tiến trình | Kết quả và quyết định của điều phối |
|---|---|
| Storyboard57755 | Đúng17phút và mạch. Bác lỗi thiếu đóng section: gói gửi là trích đoạn kết thúc ở E02; HTML thật đã kiểm7outer. Giữ IDổn định, không đánh số nội dung hiển thị theo mã |
| Sinh viên88450 | Nhận góp ý giải thích phân phối dịch chuyển và nhánh Bloom cần xác minh; gọi rõ ví dụ Jaccard. Bác thiếu hình recall: SVG C15 đã hiển thị hai tập; không sửa C |
| Giải thuật99069 | Không lỗi nghiêm trọng; giữ điều kiện Bloom và phân biệt giảm bộ nhớ/giảm ứng viên. Không thêm cận Count-Min khi chỉ giới thiệu vai trò |
| Toán97046 | Không lỗi; xác nhận3/8,3/5,MinHash,Bloom,PageRank và logic hậu kiểm |
| Sư phạm66710 | Bác “mâu thuẫn3/8và3/5”: là hai bộ dữ kiện và hai độ đo khác nhau, được gọi rõ. Nhận góp ý quá tải notes: rút D06/D07/D10, giữ chi tiết ở N05. Không xóa ý tưởng cơ chế vì người dùng yêu cầu lý giải |
| Mạch94303 | Không lỗi nghiêm trọng; C→D và D→E liền mạch. Thống nhất cách gọi truy vấn véc-tơ trong N05 |
| Writer sửa8702 | Soạn lại hai đoạn; điều phối rút câu định nghĩa điểm nền lặp, giữ dữ kiện100/400/20khối và câu nối E |
| Rà mạch lại59613 | Xác nhận điểm nền và các cầu D08/D07 đúng; không lỗi nghiêm trọng. Bác đưa ví dụ3/8sang “Bài05”: ví dụ đã nằm ở C02 của chính bài này |

Mọi lượt hoàn tất có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter, xác nhận từ JSON runtime. Không đổi mô hình. Writer sửa phản hồi chậm nhưng hoàn tất, không có lỗi OpenRouter.

Điều phối kiểm rộng1280×720/hẹp390×844 toàn63trang,7phần,120+60phút; SVG mới/được dùng ở D không tràn nhãn/chồng chữ, không ảnh hỏng/KaTeX lỗi/JavaScript lỗi/yêu cầu mạng ngoài. Xem ảnh toàn D, phóng D04/D08; rút dòng cuối D04 để tách khỏi chân trang. Viewer có34hình, mục lục, công thức, khối gập/bàn phím/bản in đạt; PDF63trang. Các cảnh báo hộp công thức A06/F03 đã kiểm bằng ảnh, không bị cắt.

Quill dùng kiểm mạch và N04→N05→N06; no-ai-slop dùng bỏ mô tả chung sai từ draft, rút danh sách trong lời giảng, định nghĩa thuật ngữ bằng câu trực tiếp. Tự kiểm eval.md đạt cho phần sửa; học liệu nằm trong tệp sản phẩm, không lộ chỉ dẫn người soạn. Codex Slides vẫn nháp cũ0trang; đã dùng RevealJS cục bộ và không tuyên bố kiểm bằng Codex Slides. Index không đổi vì mô tả/liên kết/bản đồ vẫn đúng và đã kiểm. Chỉ thay D trong HTML; E/F/R chờ các commit kế tiếp.


## ER-004 — D, nguồn và kế hoạch

Đã duyệt kế hoạch reader82151 và nguồn67108 (requested/observed z-ai/glm-5.3-flash, provider OpenRouter). Writer77070 soạn mở phần trong gói tạm; giữ tiêu đề rõ nội dung, bác phần đánh đồng mọi phương pháp với biểu diễn nhỏ hơn và đổi đếm tất cả từ thành tìm từ phổ biến. Đếm từ MapReduce phải giữ mọi đóng góp; nối bảng không bắt buộc dùng chỉ mục. Điều phối triển khai11trang D,4SVG và mở rộng N05 theo nguồn đã đối chiếu; A–C/E/F/R giữ nguyên HTML. Chu trình khảo sát có ý tưởng/ví dụ nhưng không giảng trước chứng minh bài sau. Rà storyboard và năm góc nhìn độc lập trước bước writer chỉnh sửa.


Trạng thái mới nhất: ER-004, cập nhật lần lượt D/E/F/R. Các mục ER-003 trở về trước được giữ làm lịch sử.

## ER-003 — đặc tả và đánh giá thuật toán, 2026-09-07

Phần C thay8trang bằng17trang C00–C16: mở đúng tên người dùng; ví dụ cặp tài liệu gần trùng; tổng quan10tiêu chí và trang riêng có khái niệm, ví dụ, SVG. Thêm11SVG; đồng bộ ghi chú, outline/storyboard/index và các câu nhắc ví dụ cũ ngoài C. Không sửa CSS/thư viện hoặc bài tập nguồn. 60trang,7phần,120+60phút. Mục này là trạng thái hiện hành; các mục trước là lịch sử.

### Nguồn và quyết định kế hoạch

Đọc nguồn cấp học phần và ánh xạ Bài01; giữ mục tiêu phân biệt đặc tả/biểu diễn/thuật toán/mô hìnhchi phí. Bổ sung của người dùng bác ví dụ cộng dồn làm trọng tâm. Hai reader độc lập8482(lập kế hoạch) và92226(nguồn) hoàn tất; kế hoạch cộng dồn trước đó bị thay, không dùng làm cơ sở triển khai.

Đối chiếu trực tiếp MMDS3eCh3 tr73–75/§3.1.1–3.1.2 và3.2.1, Ví dụ3.1/Hình3.1 giao3/hợp8; MMDSslidesCh3:15–17 và Stanford03-lsh:14–18. Hai slide nguồn tương đương về nhu cầu/biểu diễn/ứng viên; ưu tiên MMDS, Stanford kiểm quy mô1triệu. Không dùng số ngày làm tròn như số đo. Xét mọi cặp và chứng minh là hình thức hóa trực tiếp phép duyệt trong nguồn; không giảng trước cơ chế LSH. Lấy DSC15:24 cho bảng100/400khối; M20 từ Bài15; DSC15:17–23 cho sắp ngoài; DSC14:4,10–11 cho cập nhật lương; MMDS2.2.4–2.2.6/2.5 và Stanford01-intro67–69 cho đếm từ/mạng; Bài07 cho recall5=3/5 và xây/truy vấn; Nelson–Gailly/CMU cho yêu cầu lưu mã và khôi phục. Không thêm benchmark, tỷ lệ nén hoặc ngưỡng số.

Planner đề xuất chia bảy nhóm bên trong C và giảng sâu shingling/băm: bác vì C chỉ một phần ngoài và mục tiêu Bài01 là phân tích. Source reader nêu khoảng trống cập nhật ANN: dùng DSC14thay vì suy diễn. Chấp nhận dùng ví dụ khác nhau cho các chi phí, không buộc một phép cộng đại diện mọi khía cạnh.

### Điều phối và lỗi công cụ

AGENTS.md cho phép gửi nội dung workspace không bí mật tới OpenRouter, ngoại trừ .env. Lượt đầu bị từ chối ở bước cấp quyền; điều phối đã kiểm điều khoản này và chạy lại với căn cứ rõ, được chấp thuận. Không đọc/in/gửi .env hay bí mật.

Writer33938 dừng với lỗi đã báo nguyên văn: “RuntimeError: OpenRouter request exceeded 300s wall timeout”; chưa tạo draft. Writer76452 thử lại cùng mô hình hoàn tất một trang mở phần. Điều phối giữ cấu trúc hai thẻ, bỏ tiếng Anh thừa và mệnh đề “giải chính xác là bất khả thi”, sửa aside thành notes; triển khai phần còn lại từ đặc tả đã duyệt.

Sáu reviewer là các tiến trình riêng chạy song song. Coherence45411 và18802 lỗi “model returned an empty or incomplete answer after all retries”; đã báo nguyên văn, dừng bước phụ thuộc, tăng giới hạn đầu ra cùng mô hình. Coherence4072 hoàn tất trên bản trích nội dung hiển thị toàn bộ60trang.

Runtime được đọc từ JSON cầu nối cho mọi lượt hoàn tất nêu trên và sáu báo cáo: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Không dùng lời tự khai trong báo cáo. Writer chỉnh sửa riêng được chạy sau đủ năm góc nhìn; các writer không chạy đồng thời.

### Báo cáo độc lập và quyết định

| Vai / phiên | Mức độ, vị trí, vấn đề và bằng chứng | Đề xuất / quyết định |
|---|---|---|
| Storyboard52024 | Nhẹ: cho rằng E9/F16 lệch vì cộng theo tiền tố ID; tùy chọn C16chỉ1phút | Bác kết luận lệch: E04thuộc outerF, thời lượng theo section làE9/F16. Nêu rõ quy ước. C16tăng2phút, C15giảm3→2; Cgiữ31phút |
| Sinh viên83074 | Trung bình C02: “chọn đúng khi” mơ hồ; C11cho rằng véc-tơ chưa định nghĩa; C05nguy cơ chật | Đổi C02thành điều kiện chọn rõ. Bác tiên quyết thiếu: A07đã định nghĩa véc-tơ. C05kiểm ảnh1280×720không tràn, giữ chữ hiện hành. Không đổi hình C07chỉ vì tái dùng V06 |
| Giải thuật32491 | Không lỗi thuật toán/phạm vi; nhẹ nguồn MMDS4.1 trong mục cập nhật; tùy chọn tự kiểm lặp | Tách nguồn DSC14cho chỉ mục và MMDS4.1cho tốc độ dòng, không gán nguồn dòng cho chỉ mục. Giữ kiểm tra thu hồi sau giải thích để đo hiểu điều kiện |
| Toán99182 | Không lỗi thực; xác nhận tập khôngrỗng,3/8,chỉ số,biên,chứng minh,O(N²L),3/5,A∩R | Giữ giả thiết trong notes và ghi chú. Điều phối tự chạy số cặp/Jaccard/recall và1200trường hợp hữu hạn. Bổ sung chạy tay tượng trưng tại C04sẽ được rà lại |
| Sư phạm50426 | Trung bình C00đòiSVG; C03–C07thiếu gắn đầu ra với cặp3/8 | C00hai thẻ đã trực quan hóa hai nhánh; người dùng không yêu cầu SVGtrangtrí nên không thêm. Nhận góp ý chạy tay: N2,C1=S,C2=T, xuất(1,2)nếuτ≤3/8, ngược lại rỗng; không tự tạo ngưỡng số |
| Mạch4072 | Dùng mức “Cao” cho C01lặp A06; trung bình C08lặp B09; E04thiếu cầu hiển thị sau F04 | C01đổi vai trò từ nhắc quy mô sang phân biệt giống hệt/gầntrùng, nối vào từ C00 và ra độ đo C02. C08giữ dữ kiện nhưng hình/luậnđiểm mới: ngân sách đồng thời+bộđệm, nối C07tính→C09đọc lại; yêu cầu cho phép dùng lại ứng dụng. E04thêm câu gom đủ/không tínhtrùng trên nhiều máy, nối yêu cầu đúngđủ F04→chuẩn bịMapReduce→R dùng mô hình lưu trú |

Điều phối phát hiện thêm E01và đoạn ghi chú tiên quyết còn hỏi bảng tổng bước3 sau khi bỏ ví dụ C: thay bằng giao3/hợp8. C16mở lại ngữ cảnh cặp tài liệu sau ví dụ truy vấn véc-tơ. Hình xây chỉ mục sửa chiều truy vấn→chỉ mục để không ngụ ý chỉ mục tạo ra truy vấn. Các ánh xạ N03/N04và tiêu chí đếm trang trong storyboard được đồng bộ, giữ mục lịch sử có nhãn riêng.


Writer chỉnh sửa72050 hoàn tất trên cùng runtime; soạn bốn đoạnC01/C04/C16/E04. Điều phối giữ hai nhánh theo ngưỡng, sửa chiều định nghĩa ứng viên và bỏ cách hiểu sai “so sánh từng ký tự” thành “kiểm bằng nhau từng ký tự”. Không nhận nguyên văn câu gọi mọi cặp tài liệu là ứng viên. Bản cuối đang được reviewer toán58919và mạch73106rà lại; chưa đánh dấu yêu cầu hoàn tất trước khi push.

### Rà lại và kiểm định cuối

Reviewer toán58919 xác nhận hai nhánh chạy tay, đặc tả, giả mã, bất biến và trường hợp biên không có lỗi. Reviewer mạch73106 đã đọc trọn bản hiển thị 60 trang; C01→C02, C04, C16→D, E01 và E04 đạt, không còn lỗi nghiêm trọng/chặn. Gợi ý dấu cách chỉ thuộc dòng metadata của gói tạm, không nằm trong học liệu. Requested/observed model của cả hai là z-ai/glm-5.3-flash, provider OpenRouter.

Điều phối chạy lại kiểm định sau chỉnh sửa:

- 60 mã trang duy nhất khớp thứ tự storyboard; 7 section ngoài; 54 trang giảng và 6 trang bài tập. C31 phút, toàn giảng120 phút, bài tập60 phút; E04 được tính trong F.
- So sánh HTML với HEAD d39fea7: ngoài C chỉ các sửa có chủ ý tại A01, B09, E01, F03, F04, E04; các phần khác giữ nguyên. Không sửa CSS, thư viện hoặc đề/lời giải bài tập.
- Tính lại số cặp499999500000, Jaccard3/8, độ thu hồi3/5 và sáu cặp theo thứ tự; chạy1200trường hợp hữu hạn gồm N0/N1/ngưỡng0/ngưỡng1, đầu ra khớp đặc tả và không lặp.
- Chromium1280×720 và390×844 duyệt toàn bộ60trang; không tràn khung, không lỗi JavaScript/KaTeX, ảnh hỏng hoặc yêu cầu mạng ngoài. Kiểm từng nhãn SVG phần C: không ra ngoài viewBox hoặc chồng nhãn.
- Đã xem toàn bộ ảnh trang, phóng riêng C03/C04/C15/E01, ảnh sau sửa C01/C12/E04, hai trang lân cận các phía và các câu thu hồi. Hai cảnh báo scrollHeight của KaTeX ở A06/F03 là đo hộp công thức, ảnh không bị cắt.
- Viewer: 31 lượt nhúng hình, không hình hỏng/công thức lỗi/tràn ngang ở rộng và hẹp; sáu khối gợi ý/lời giải gập mặc định, bàn phím mở được và mở khi in; từ chối đường dẫn thoát thư mục và số bài lệch.
- PDF slide60trang; ghi chú A4 tạo được, hình/công thức và mục lục hiển thị. Chỉ mục rộng/hẹp và liên kết kiểm đạt.
- Quill rà thứ tự khái niệm, ký hiệu và cầu nối; không tạo dự án sách. No-ai-slop biên tập mặt trang/notes/Markdown rồi tự kiểm đủ các mục eval.md: giữ dữ kiện và giọng học thuật, không khẩu hiệu/câu hỏi tu từ/chỉ dẫn người viết; phần đối lập còn lại là phân biệt toán học cần thiết. Không còn cách gọi bị người dùng phản đối trong HTML hoặc ghi chú công khai.
- git diff --check đạt. Tệp .gitignore, AGENTS.md và hạ tầng .codex/OpenRouter của người dùng được giữ ngoài commit.

Codex Slides: dự án20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj vẫn draft/0slide của bản cũ, không có mặt Browser phù hợp để xác minh deck hiện hành. Đã thông báo và dùng kiểm RevealJS cục bộ theo ngoại lệ AGENTS.md; không tuyên bố đã rà hoặc đồng bộ qua Codex Slides. Bằng chứng ảnh/PDF/JSON ở thư mục tạm /tmp/er003.9rFlP5/verification, không đưa vào Git.

Trạng thái: hoàn tất. Commit nội dung `5661db9e23f2e75565b27107c85e6a842b940faa` đã push bằng `git push origin main`; `git ls-remote origin refs/heads/main` trả đúng hash. ER-003 được tick sau xác nhận này. Không có thay đổi nội dung học liệu sau lượt kiểm cuối.

## ER-002 — tổ chức lại phần dòng dữ liệu, lưu trữ và truy vấn, 2026-09-06

Đã triển khai, kiểm định và push commit nội dung `961a5d2b94cdd8b4fb2953b3c9f2ea62f44798f9`; git ls-remote xác nhận đúng hash trên origin/main. Sửa 12 trang B và chín SVG, đồng bộ phần ghi chú tương ứng, outline/storyboard/index. Giữ nguyên HTML phần A và từ C01 đến cuối bằng so sánh với HEAD cde84ce. Không sửa CSS, thư viện, bài tập hoặc các bài khác. Các thay đổi AGENTS.md, .gitignore và hạ tầng OpenRouter của người dùng không thuộc commit.

### Nguồn, kế hoạch và triển khai

Đã đọc source.md và bảng ánh xạ nguồn Bài08–15, đối chiếu ví dụ MMDS4.2 tr136–138 (mẫu theo người dùng),4.3 tr139 (thư/danh sách cho phép),4.1.3/4.4–4.7 (thống kê). MMDS Streams1:3–9 và Stanford CS246 16-streams:4–9 tương đương về mục tiêu, độ chính xác và khả năng Việt hóa; chọn MMDS, dùng sách để cụ thể hóa tình huống. CMU LZ trang logic13–14 giữ chuỗi aabaacabcabcb; CMU lossy trang3 cho sơ đồ gộp mức sáng, đối chiếu cả hình khi trích xuất chữ lỗi phông. DSC14:4/6/10–16 cho mã/lương;15:17–24/28/40 cho sắp/nối;24:17/21–24 cho vùng;31:14 và sách tr13–16 cho hai từ cùng xuất hiện. Sửa dẫn quy mô hai bảng từ slide28 về24; giữ M20 theo kịch bản Bài15. Ghi nhận lỗi dấu giao ở công thức OR trong PPTX31; nội dung dùng phép hợp đúng, không chép lỗi.

Planner36150 và source-reader71280 độc lập; điều phối duyệt kế hoạch ba cụm, giữ12trang/26phút. Source-reader53143 lỗi `model exceeded the tool-call limit (3)`; đã báo nguyên văn và chạy lại đúng hai đoạn tệp. Writer90571 lỗi `model exceeded the tool-call limit (4)`; giữ bản nháp ở /tmp và chạy lại writer21374. Runtime các lượt hoàn tất: requested_model=`z-ai/glm-5.3-flash`, observed_model=`z-ai/glm-5.3-flash`, provider=`OpenRouter`.

Writer tạo ý ba nhóm và hai hàng bài toán; điều phối không nhập nguyên văn bản nháp thiếu B02, bỏ nhầm mã/notes hoặc nhãn chật. Khôi phục đầy đủ cấu trúc mẫu và soạn bản tích hợp theo đặc tả. Sau đủ năm báo cáo, writer chỉnh sửa55416 tạo lời giảng rút gọn; giữ ý phân biệt người/lượt và giải thích báo có nhầm, bác các câu “tức thì”, “chỉ con số lớn mới cần xấp xỉ” và gọi mọi bài toán là cấu trúc dòng. Không có hai writer chạy đồng thời.

### Các báo cáo độc lập và quyết định

Mọi reviewer dưới đây là tiến trình riêng, chạy song song trên toàn B cùng A06/A07 và C01/C02. Cùng runtime requested_model/observed_model=`z-ai/glm-5.3-flash`, provider=`OpenRouter`; không suy danh tính mô hình từ lời tự khai. Reviewer chỉ đọc nội dung và alt; điều phối kiểm SVG và trình duyệt riêng.

| Vai / phiên | Mức độ, vị trí, vấn đề và bằng chứng | Đề xuất và quyết định |
|---|---|---|
| Storyboard42934 | Nhẹ, B10/B09: cân nhắc nhắc nhóm lưu trữ; số quy mô lặp ở notes. Xác nhận B00→dòng→nén→đĩa có tiến triển, không thiếu cầu nối | Giữ B10 vì đã nêu lưu để đọc lại; số ở notes cần nguồn/giả thiết nên giữ. Đếm toàn bài bằng script thay vì suy từ packet |
| Sinh viên95675 | Reviewer dùng mức “Cao” cho B01/B02: Bloom, DGIM và “có thể có” trong lời giảng chưa rõ; trung bình B07 “xếp hạng liên quan” | Rút tên chuyên biệt khỏi lời giảng nhập môn, giữ điều kiện đúng và nguồn trong ghi chú tự học; giải thích báo có dù địa chỉ ngoài danh sách. B07 đổi “chưa sắp thứ tự ưu tiên”. Không còn vấn đề bắt buộc |
| Giải thuật53189 | Không lỗi bắt buộc về phạm vi/kết luận; phân biệt đếm cặp, đếm người/lượt, nén/truy cập, giao/hợp đúng | Giữ chiều sâu khảo sát, không đưa thuật toán chuyên biệt vào phần giới thiệu |
| Chính xác31136 | Không phát hiện lỗi kết luận; kiểm số cặp499999500000, vết40+15=55,100/400khối và M20, mọi cặp trùngID | Điều phối tự kiểm lại dữ kiện nguồn và quan hệ hình. Bảo đảm bộ lọc giữ đủ điều kiện, không nhận lời diễn giải “âm giả” sai trong báo cáo |
| Sư phạm71192 | Trung bình B01/B02: tên Bloom/DGIM gây tải; nhẹ B06: cây/băm chưa học. Không có lỗi trình tự bắt buộc | Rút tên khỏi B01/B02; ghi chú B06 chỉ nêu giới hạn cấu trúc, mặt trang không có tên thuật toán. Không thêm lời dẫn dư vào A hoặc B00 |
| Mạch viết30677 | Trung bình B09→C01: đề nghị thu giới hạn trước trở lại kho nhật ký; nhẹ B00: thứ tự câu ví dụ | B09 sửa rõ “phần tiếp theo phân loại chi phí rồi phân tích tổng byte”. Giữ B00 giới thiệu ba nhóm trước hai ví dụ vì đúng vai trò mở phần |

Nhiều reviewer suy grid2 chứa bốn thẻ là lỗi. Bác: CSS định nghĩa hai cột và tự tạo hai hàng; trình duyệt xác nhận C01 đúng. Không tạo grid4 hay sửa CSS. Góp ý A06/A07 thiếu nối/giải thích bị bác vì nội dung đã có và nằm ngoài phạm vi; không thêm chỉ dẫn nội bộ lên mặt trang.

Rà mạch lại4674 sau chỉnh sửa: toàn B cùng hai trang mỗi phía; xác nhận không còn lỗi bắt buộc. B00 định vị ba nhóm; B10 nối số đếm với nhu cầu khôi phục; B11 định nghĩa khối trước các bài toán đĩa; B09→C01 phân loại chi phí→C02 vết tổng byte. Không đổi mở/kết toàn bài hoặc luận điểm trung tâm nên phạm vi rà lại này phù hợp.

### Biên tập và kiểm định cuối

Quill kiểm thứ tự khái niệm và đầu vào–đầu ra giữa ba cụm, không tạo quill.json. No-ai-slop áp dụng cho mặt trang, lời giảng và ghi chú; tự kiểm trực tiếp eval.md: giữ ý/nguồn/điều kiện, mở bằng bài toán, bỏ khẩu hiệu và lời hướng dẫn người viết, tránh thuật ngữ chưa giải thích và tiêu đề kể tiến trình. Các nhóm Editing principles, Words to cut, Patterns to cut, Final read đạt trong phạm vi chỉnh sửa; bản đầy đủ là HTML/Markdown đã sửa, phần “thay đổi” được bàn giao ngắn gọn. Không thêm số đo, tỷ lệ nén hoặc dữ liệu thực nghiệm giả.

Chín SVG có role/img và title/desc; hình vùng giữ Q giao cả A/B, không gán đối tượng kết quả. Nhãn B01/B02 quá dài được phát hiện bằng getBBox và ảnh chụp, đã rút. Dải mức sáng là minh họa định tính của lượng tử hóa; thứ tự các vạch sắp xếp giữ cùng đa tập và khóa lặp. Không raster, không tài sản lõi ngoài mạng.

Chromium chạy lại bản cuối tại cổng8765: 51slide/7phần, 50notes (trang bìa không cần),120phút giảng+60recitation. Đối chiếu đủ51mã với storyboard; rộng1280×720 và hẹp390×844, duyệt toàn bộ, chụp102ảnh. Không trang ra ngoài khung, không lỗi JavaScript/KaTeX/HTTP hoặc tài nguyên ngoài mạng; chín SVG không nhãn vượt viewBox/chồng nhau. Điều phối xem trực tiếp12trang B; cảnh báo scrollHeight ở A06/C03/F03 do hộp KaTeX, ảnh không cắt và nội dung ngoài phạm vi không đổi. Bàn phím xuống P01, phải B00 đúng. PDF đủ51trang.

Viewer: 19hình,42mục lục, không ảnh hỏng/công thức lỗi/tràn ngang ở cả rộng và hẹp; bốn khối đáp án gập mặc định, Enter mở, bản in mở tất cả; chặn đường dẫn vượt materials và doc/deck lệch số bài. Index rộng/hẹp và liên kết hợp lệ. Bằng chứng cục bộ: /tmp/er002.MGNeaE/verification/results.json, ảnh từng trang, slides.pdf và lecture-note.pdf. git diff --check đạt.

Giới hạn Codex Slides: get_project trả dự án 20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj ở trạng thái draft/0 slide. Không có bề mặt Browser tương ứng để xác minh bản RevealJS. Đã báo người dùng và dùng kiểm định cục bộ theo ngoại lệ AGENTS; không tuyên bố đã rà bản sửa bằng Codex Slides.

## Vòng rà 2026-08-30

Kế hoạch: hợp nhất các sửa đã duyệt vào HTML, SVG bản đồ, outline, storyboard và nhật ký này; giữ 7 section ngoài và tổng thời lượng 120+60.

Phân tích nguồn: đọc `AGENTS.md`, bản đồ nguồn, bản HTML và planning cùng bản trích xuất MMDS, Stanford, BHK; các sửa lấy từ quyết định của điều phối viên, không thêm số liệu, nguồn hay ví dụ mới.

Kiểm định storyboard: đếm lại 41 trang, 7 section ngoài, tổng thời lượng phần giảng 120 phút và phần bài tập 60 phút; các mạch A–D giữ chức năng, kết nối vào/ra và đóng góp mục tiêu; bản đồ chu trình rút gọn cho B–E đã ghi bước gộp, bước không áp dụng và lý do.

Năm vai độc lập (mỗi vai một lượt rà riêng):

| mức độ | trang | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| nghiêm trọng | toàn bộ aside | Thời lượng lặp giữa HTML và storyboard | Cụm “Thời lượng dự kiến: … phút.” xuất hiện ở mọi ghi chú | Xóa khỏi mọi aside; chỉ giữ trong storyboard/outline |
| trung bình | A06 | pre quá nhỏ | font-size .66em | Nâng lên .75em |
| trung bình | A07 | Chưa nêu rõ điều kiện dừng | Ghi chú nói “dừng sau n bước” nhưng mặt trang không nêu | Thêm “mỗi bước xử lý một bản ghi” vào bước kết thúc |
| trung bình | B06 | Ký hiệu e, w chưa định nghĩa | Công thức điểm(e) dùng e, w ngay trên mặt trang | Định nghĩa e là thư, w là từ trên mặt trang |
| trung bình | B07 | Câu hỏi lặp câu B04 | Câu hỏi bảng tổng đã có ở B04 | Đổi sang phân loại “phân phối ước lượng từ mẫu”; notes đáp mô hình thống kê |
| trung bình | C05 | Câu hỏi lặp câu A08 | Câu hỏi trường hợp thất bại đã có ở A08 | Đổi sang phép đánh đổi khi O(h) không vừa bộ nhớ; notes nêu đổi đặc tả, tóm tắt xấp xỉ hoặc thu hẹp truy vấn, phải nêu rõ |
| trung bình | D01 | Giả thiết độc lập chưa hiện trên mặt trang | Chỉ có trong notes D02 | Viết rõ mỗi người mỗi ngày xác suất q=0,01, độc lập giữa người/ngày |
| trung bình | D03 | Tiêu đề gán sai thuật ngữ | “Nguyên lý Bonferroni đếm biến cố trùng kỳ vọng” | Đổi thành “Đếm biến cố trùng bằng kỳ vọng”; notes phân định MMDS gọi đây là Bonferroni phi hình thức, công thức dùng tính tuyến tính của kỳ vọng, không dùng union bound |
| nhẹ | D04 | Tiêu đề dài, chữ số bằng chữ | “Kỳ vọng có khoảng hai trăm năm mươi nghìn…” | Đổi thành “Kỳ vọng khoảng 250.000 biến cố trùng” |
| trung bình | D05 | Ba thẻ hé chiều tác động | Thẻ cũ ghi sẵn “số cặp ngày gần gấp bốn” | Ba thẻ chỉ nêu dữ kiện; câu hỏi yêu cầu xác định số phép thử và xác suất thay đổi thế nào |
| trung bình | E02 | Độ dày 1/d chỉ có trong notes | Câu hỏi O(1/d) xuất hiện trước khi nêu dữ kiện | Giới thiệu trên mặt trang trước câu hỏi rằng vành ngoài dày cỡ 1/d lần bán kính |
| trung bình | E03 | Từ “mạch” không phù hợp cho bản đồ học phần | Tiêu đề, alt, SVG title/desc/footer dùng “mạch” | Đổi thành “Bản đồ 15 bài theo năm nhóm”; Bài 1 là nền chung; giữ nguyên nội dung năm nhóm và quan hệ |
| trung bình | E04 | Notes chưa thu hồi mở đầu rõ | Ghi chú chỉ liệt kê bốn câu kiểm tra | Notes thu hồi: kho nhật ký không vừa bộ nhớ dẫn tới đặc tả, chi phí, bảo đảm; nhiều phép thử và số chiều buộc nêu mô hình/giả thiết; đây là kết luận phần giảng |
| trung bình | R01 | Gộp sai hai thay đổi độc lập và hé sản phẩm | “nên có 200.000 khách sạn”; sản phẩm “ba công thức và ba giá trị” | Tách thành hai thay đổi độc lập (người, khách sạn); sản phẩm chỉ ba công thức; tham chiếu dữ kiện tới trang D01 thay vì chỉ Mục 1.2.3 |
| nghiêm trọng | R05 | Đáp số và kết luận hiện trên mặt trang | Fragment chứa công thức và kết luận trong khi hoạt động 15 phút | Chuyển toàn bộ công thức, đáp số 1,898·10^-4, C(1000,10), cận xác suất, rubric và hai giới hạn vào notes; mặt trang chỉ giữ yêu cầu và sản phẩm; thêm câu kết nối thu hồi khung Bài 1; không đổi dữ kiện 10^8 |

Hai phát hiện bị bác:

- (a) “A00–A08 cộng sai thời lượng” — bác. A00–A08 cộng đúng 32 phút (2+5+4+2+4+4+4+4+3).
- (b) “R05 đáp số sai bậc 10” — bác. R05 đúng 1,898·10^-4 vì C(10^8,2)≈5·10^15, không phải 5·10^17.

Quyết định khác: không đổi tên học phần “của” trong tiêu đề vì đây là quy ước toàn bộ kho theo AGENTS, không sửa cục bộ một deck.

Runtime: reader, reviewer và writer đều có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter.

### Tái kiểm sau chỉnh sửa

- Vai độ chính xác rà lại A07, B06–B07, C05, D01–D05, E02–E04 và R01–R05: mọi giả thiết, ký hiệu, ba biến thể, kết quả số và cận xác suất đều đúng; đáp án chỉ còn trong ghi chú. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Vai kết nối và mạch viết rà lại toàn bài rồi rà hẹp D04–E04 và R05 sau lần sửa cuối: D05→E00, E02→E03, E04→R00 và kết luận R05 đều có câu nối; E04 thu hồi bốn mục tiêu P01; đủ 7 section ngoài. Không còn lỗi bắt buộc.
- Tự kiểm `no-ai-slop/eval.md`: giữ nguyên mệnh đề và số liệu nguồn; không có từ cấm, lời dẫn rỗng, câu hỏi tu từ trong tiêu đề, kết luận lặp hoặc nhịp câu quảng bá. Câu chữ hiển thị và ghi chú dùng động từ trực tiếp, thuật ngữ nhất quán.
- Rà mạch theo Quill Outline Workflow mà không tạo `quill.json`: tuyến kho nhật ký → thuật toán → tầng lời giải → chi phí → tín hiệu giả → kết luận → bài tập tiến triển liên tục; bảng ký hiệu và thuật ngữ nội bộ được đồng bộ.

### Kiểm định kỹ thuật và giới hạn công cụ

- Bộ phân tích HTML xác nhận 7 section ngoài, 41 `data-slide-id` duy nhất, 41 ghi chú, không thiếu đường dẫn cục bộ; cả 5 SVG phân tích XML thành công; `git diff --check` đạt.
- `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Cổng 8765 đang do một tiến trình cũ phục vụ `/tmp/lec03-webroot.wGW4jP` chiếm; không dừng tiến trình ngoài phạm vi.
- Máy chủ thay thế chỉ gắn `127.0.0.1`, chỉ phục vụ `2627-1/` tại cổng 8766. HTML, RevealJS, Notes, Highlight, Math, ba tài nguyên KaTeX và SVG E03 đều trả HTTP 200; máy chủ được dừng sau kiểm tra.
- Codex Slides đọc lại thành công dự án `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj`: nguồn và yêu cầu vẫn còn, nhưng dự án ở checkpoint `clarify` và có 0 trang. Phiên này không có Codex in-editor Browser hay trình duyệt Chromium/Firefox để rà canvas. Không tải bản HTML mới tới Codex Slides vì quyền gửi tệp đã cấp cho OpenRouter, không bao gồm đích Codex Slides. Vì vậy không tuyên bố đã rà trực quan bản sửa mới bằng Codex Slides; kiểm định hiển thị trước vòng này vẫn là mốc tham khảo, còn vòng mới dựa trên cấu trúc, HTTP và rà bố cục từ DOM/CSS.

## Trạng thái sau chỉnh sửa

- Tệp trang chiếu: `2627-1/lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html`.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Bài tập lấy trực tiếp MMDS Bài 1.2.1 và 1.2.2, trang 8; đáp án chỉ ở ghi chú diễn giả.
- Tài sản trực quan: 5 SVG; không dùng ảnh raster.
- `2627-1/index.html` đã có thẻ Bài 1 và liên kết đúng tới tệp HTML; vòng này không cần sửa chỉ mục.

## Báo cáo kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | A04, A05, B00–B07, C00–C03 | Ví dụ chạy tay đứng sau đặc tả, giả mã và một phần khảo sát | Khoảng 39 phút sau thuật toán mới quay lại vết chạy | Chuyển vết chạy lên trước đặc tả và hoàn tất chu trình trước phần B |
| nghiêm trọng | D01–D04 | Công thức Bonferroni xuất hiện trước tình huống | D01 nêu nguyên lý, D02 mới nêu hồ sơ lưu trú | Đặt tình huống trước, rồi giả thiết, đếm phép thử và kỳ vọng |
| nghiêm trọng | R04–R05 | Đáp án hiện trước khi hoạt động kết thúc | R05 hiện công thức dù được tính 15 phút | Giữ câu hỏi trước; chỉ hiện lời giải khi chữa |
| nghiêm trọng | P01 | Mục tiêu hiển thị không khớp outline | Bốn mục tiêu trên slide, sáu mục tiêu trong outline | Đồng bộ phạm vi; cao chiều chỉ định tuyến |
| trung bình | B02–B06 | Nhiều ví dụ rời làm đứt tình huống xuyên suốt | Giao thoa, học máy, PageRank và lọc thư nối tiếp | Dùng lại kho nhật ký; thu gọn khảo sát |
| trung bình | E01–E02 | Thiếu cầu nối và nhập hai hiện tượng | Công thức khoảng cách dẫn thẳng sang hình thể tích | Phân biệt rõ hai hiện tượng và thêm câu kiểm tra |
| trung bình | D05, R01–R03 | Phần giảng tiết lộ bài tập | Ghi chú D05 cho đáp số phần c | Bỏ đáp số khỏi phần giảng |
| nhẹ | A05, B01 | Tiêu đề chưa nêu luận điểm | “Điểm nghẽn nằm ở đâu”; phủ định “không được nhập” | Dùng tiêu đề khẳng định trực tiếp |

## Báo cáo góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | A04, A05, B00–B07, C00–C03 | Ví dụ chạy tay xuất hiện sau hình thức hóa, giả mã và chứng minh | Khoảng cách khoảng 39 phút | Đưa vết chạy trước đặc tả và hoàn tất chu trình trước B |
| nghiêm trọng | E03 | Bản đồ 15 bài có chữ quá nhỏ | SVG 1200×640 dùng chữ 17 px, khi co chỉ còn khoảng 11–12 px | Tách hai trang hoặc gộp thành năm mạch chữ lớn |
| nghiêm trọng | R04–R05 | Trang chữa lộ công thức và đáp số | R05 hiện toàn bộ đáp án nhưng vẫn tính 15 phút | Dùng ghi chú hoặc fragment và thêm sản phẩm R04 |
| trung bình | A05 | Một trang gánh giả mã, bất biến, dừng, biên và chi phí | Thời lượng bốn phút | Tách thuật toán, chứng minh và chi phí |
| trung bình | P01, E00–E02 | Mục tiêu không báo trước chứng minh hoặc phần cao chiều | Mặt slide có bốn mục tiêu, outline có sáu | Đồng bộ; lược cao chiều khỏi đánh giá nếu chỉ định tuyến |
| trung bình | B02–B06 | Tải chuyển ngữ cảnh cao | Nhiều lĩnh vực và ví dụ mới trong vài phút | Gộp nội dung và dùng lại kho nhật ký |
| trung bình | E01–E02 | Thiếu ví dụ hoặc câu kiểm tra | Hai trang chỉ trình bày công thức và hình | Thêm phép tính hoặc câu kiểm tra có căn cứ từ BHK |
| nhẹ | B07 | Câu hỏi quá rộng cho hai phút | Yêu cầu xét mỗi sản phẩm và dữ liệu phải giữ | Chọn một sản phẩm, có đáp án mẫu trong ghi chú |

## Báo cáo chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | A04, A05, C03 | Chu trình thuật toán sai thứ tự | Vết chạy sau đặc tả và thuật toán | Chuyển vết chạy trước đặc tả |
| nghiêm trọng | D02–D04, R01–R03 | “Cùng khách sạn” mơ hồ | Nguồn cho phép khách sạn khác giữa các ngày | Ghi rõ cùng một khách sạn trong từng ngày, có thể khác qua ngày |
| nghiêm trọng | R04–R05 | Thiếu giả thiết và câu hỏi gốc của Bài 1.2.2 | Không có giả thuyết cặp thật chắc chắn mua cùng tập 10 món | Khôi phục bằng ngôn ngữ trung tính và hỏi so trùng thật với trùng ngẫu nhiên |
| nghiêm trọng | E01–E02 | Nhập khoảng cách với thể tích gần biên | Hình thể tích mang tiêu đề khoảng cách | Đổi tiêu đề và thêm cầu nối |
| trung bình | B04–B07 | “Mô hình tính toán” dễ nhầm computational model | Thuật ngữ có nghĩa khác trong lý thuyết tính toán | Dùng “mô hình dữ liệu theo truy vấn” |
| trung bình | C02, C05, E04 | Sai số bị gọi là nguồn chi phí | C02 liệt kê bốn nguồn chi phí | Dùng “Ba chi phí và một bảo đảm” |
| trung bình | D03–D05, R01–R03 | Phần giảng lặp và tiết lộ bài tập | D05 cho biết biến thể giảm dưới 1 | Bỏ đáp số và điều chỉnh hoạt động |
| trung bình | R05 | Biểu thức đếm cặp lượt mua, không chính xác cặp người | Một cặp người có thể trùng nhiều lần | Định nghĩa $X$ là số cặp lượt hoặc dùng xác suất đúng/xấp xỉ |
| trung bình | C00, C02 | Nguồn Stanford 67–70 mâu thuẫn quyết định phạm vi | Ghi chú vẫn dẫn các trang này | Bỏ mọi dẫn nguồn này |
| nhẹ | A05 | Tiêu đề sai trọng tâm | “Điểm nghẽn nằm ở đâu” trên trang giả mã | Đổi tiêu đề theo luận điểm |
| nhẹ | E03 | Dùng “moment” trong hình | Chưa thuần Việt | Dùng “mômen” |

## Báo cáo độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | E02 | Hình chỉ nói thể tích gần biên, không chứng minh khoảng cách tập trung | Hình BHK 2.2 là mặt cắt thể tích | Đổi tiêu đề và câu nối |
| trung bình | D04, R01–R03 | Tổ hợp đếm biến cố, không nhất thiết là số cặp người phân biệt | Một cặp người có thể góp nhiều cặp ngày | Gọi kỳ vọng số biến cố trùng; chỉ xấp xỉ cặp người khi biến cố hiếm |
| trung bình | R04–R05 | Công thức chính xác cho cặp lượt mua | Tử số là $\binom P2 100^2$ | Định nghĩa $X$ tương ứng; có thể dùng $\Pr(X\ge1)\le E[X]$ |
| trung bình | D02–D04, R01–R03 | Thiếu giả thiết độc lập và chọn đều | Công thức $(q^2/H)^k$ cần các giả thiết này | Ghi rõ độc lập giữa người/ngày và chọn đều có điều kiện |
| trung bình | A05 | Bất biến thiếu tập khóa | Chỉ phát biểu đúng giá trị cho khóa đã có | Thêm tập khóa đúng bằng máy chủ trong tiền tố |
| nhẹ | A04 | Miền $s_i$ và ràng buộc truy cập chưa chính xác | $s_i\ge0$; “đọc một lần” đặt trong điều kiện đầu vào | Dùng $s_i\in\mathbb{N}_0$; tách ràng buộc truy cập |
| nhẹ | C02 | $O(n)$ kỳ vọng thiếu giả thiết | Chi phí phụ thuộc bảng băm | Nêu mỗi cập nhật bảng băm kỳ vọng $O(1)$ |

Đối chiếu số học của phản biện: 249749,99975025; 999499,9990005; 249749,999875125; 0,0830834999; $\binom{1000}{10}=263409560461970212832400$; $1,8981846905\cdot10^{-4}$.

## Báo cáo phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | A03–A05, B00–B07, C00–C03 | Phần khảo sát B chen giữa thuật toán và ví dụ/chi phí, phá mạch suy luận | Khoảng 39 phút mới quay lại vết chạy | Đưa ví dụ trước đặc tả, hoàn tất chu trình và chi phí trước phần khảo sát |
| nghiêm trọng | D00–D04 | Công thức Bonferroni xuất hiện trước tình huống | D01 trước D02 | Đặt hồ sơ lưu trú trước, rồi đếm phép thử, hình thức hóa và tính kỳ vọng |
| nghiêm trọng | R04–R05 | Đáp án hiện ngay khi hoạt động chưa kết thúc | R05 hiện công thức và số nhưng tính 15 phút | Giữ câu hỏi trước, chỉ tiết lộ khi chữa hoặc trong ghi chú |
| nghiêm trọng | P01 | Mục tiêu hiển thị không khớp outline | Bốn mục tiêu so với sáu | Đồng bộ hoặc thu gọn phạm vi |
| trung bình | B02–B06 | Nhiều ví dụ rời làm đứt tình huống xuyên suốt | Giao thoa, học máy, PageRank, lọc thư | Gộp và dùng lại kho nhật ký |
| trung bình | E01–E02 | Thiếu cầu nối và nhập hai hiện tượng | Công thức khoảng cách rồi hình thể tích | Phân biệt rõ và thêm câu kiểm tra |
| trung bình | D05, R01–R03 | Giảng tiết lộ bài tập | Ghi chú cho đáp số phần c | Bỏ đáp số khỏi phần giảng |
| nhẹ | A05, B01 | Tiêu đề không nêu luận điểm | “Điểm nghẽn…” và tiêu đề phủ định | Đổi tiêu đề trực tiếp |

## Quyết định chỉnh sửa

Tất cả đề xuất `chặn bàn giao` và `nghiêm trọng` đã áp dụng. Các đề xuất `trung bình` và `nhẹ` cũng đã áp dụng, với hai lựa chọn cụ thể:

- E03 dùng phương án gộp thành năm mạch thay vì tách hai trang; cách này giữ một luận điểm trung tâm và không tăng thời lượng.
- E01 dùng câu kiểm tra về kỳ vọng theo $d$ thay cho một ví dụ số dài; câu hỏi dựa trực tiếp vào công thức đang hiển thị và giữ cụm cao chiều ở mức định tuyến.

Không có đề xuất nào bị bác bỏ. Sau khi đổi thứ tự và số trang, đã rà lại toàn bộ cụm A, B, C, D, E và hai trang lân cận quanh mỗi điểm nối.

## Sai khác có chủ ý so với nguồn

| Mục | Quyết định | Lý do |
|---|---|---|
| Stanford trang chiếu 32–61 và 63–70 | Bỏ | Nội dung hệ phân tán thuộc Bài 2; trang 62 là ngoại lệ duy nhất để lấy lược đồ kho web |
| Ví dụ bốn bản ghi A04 | Tự dựng từ lược đồ nguồn | Cần vết chạy nhỏ; ghi rõ không phải dữ liệu thực nghiệm |
| MMDS Hình 1.1 về John Snow | Bỏ | Không cần cho mạch đặc tả, chi phí và nhiều phép thử |
| MMDS nguyên lý Bonferroni | Giữ ở mức phi hình thức | Nguồn không trình bày phép hiệu chỉnh thống kê đầy đủ tại đây |
| MMDS Bài 1.2.1 | Chia R01–R03 | Giữ nguyên dữ kiện và yêu cầu; thêm mốc hoạt động |
| MMDS Bài 1.2.2 | Chia R04–R05 | Giữ nguyên giả thuyết toán học; đáp án chỉ hiện khi chữa |
| Nhãn con người trong Bài 1.2.2 | Dùng “nhóm cần phát hiện” | Ngôn ngữ trung tính, không đổi cấu trúc toán học hoặc câu hỏi |
| BHK Chương 2 | Chỉ định tuyến | Định lý chi tiết vượt phạm vi Bài 1 |
| Bản đồ 15 bài | Gộp thành năm mạch | Chữ 17 px không đọc được khi chiếu; số bài được giữ theo mạch |

## Hình vẽ lại và tiếp cận

- `kho-nhat-ky-bo-nho.svg`: nhãn $D,M,b$, mũi tên và hoa văn bộ nhớ.
- `giao-thoa-khai-pha-du-lieu.svg`: ba hoa văn được dùng thật, cùng ba kiểu viền.
- `phep-thu-va-duong-tinh-gia.svg`: ba khối có nhãn và kiểu viền; đại lượng được gọi là biến cố trùng kỳ vọng.
- `the-tich-gan-bien.svg`: vành ngoài dùng hoa văn chấm; mô tả đúng hiện tượng thể tích.
- `ban-do-hoc-phan.svg`: năm mạch, chữ nhỏ nhất 22 px, biểu tượng và kiểu viền riêng.

Mỗi SVG có `role="img"`, `title`, `desc`; không dùng màu làm tín hiệu duy nhất.

## Tự kiểm biên tập

Đã dùng `no-ai-slop` và tự kiểm trực tiếp theo `no-ai-slop/eval.md`: giữ nguyên mệnh đề và số liệu nguồn; bỏ lời dẫn rỗng, câu hỏi tu từ, nhấn mạnh phô trương, nhịp câu máy móc và kết luận lặp. Tiêu đề dùng tiếng Việt, chỉ giữ tên riêng, tên thuật toán và ký hiệu chuẩn.

Đã dùng Quill ở mức Outline Workflow để rà mục tiêu, thứ tự khái niệm, thuật ngữ, ký hiệu và câu nối. Chuỗi $(u_i,s_i)$ đi liên tục từ vết chạy sang đặc tả, giả mã và bất biến; $P,T,H,q$ chỉ dùng trong cụm Bonferroni và bài tập. Không tạo `quill.json`.

## Kiểm tra tính đúng khi chỉnh sửa

- Bất biến gồm cả tập khóa và giá trị; chứng minh nêu mệnh đề, khởi tạo, duy trì, kết thúc và điều kiện dừng.
- Thời gian kỳ vọng $O(n)$ chỉ dưới giả thiết mỗi thao tác bảng băm kỳ vọng $O(1)$.
- Trong mô hình lưu trú, các quyết định độc lập giữa người/ngày; có điều kiện đã đi, khách sạn được chọn đều. Khách sạn có thể khác giữa các ngày.
- $X$ ở D03 là số biến cố trùng theo cặp người và cặp ngày. $X$ ở R05 là số cặp lượt mua trùng của hai người khác nhau.
- Công thức R05 cho kỳ vọng số cặp lượt mua; $\Pr(X\ge1)\le\mathbb{E}[X]$ theo bất đẳng thức Markov.

## Việc còn lại cho điều phối viên

- Không còn việc nội dung hoặc kỹ thuật phải xử lý trước bàn giao.
- Sau khi commit, điều phối viên đẩy lên `origin` và kiểm tra URL GitHub Pages.

## Kiểm tra tĩnh sau chỉnh sửa

- 41 `data-slide-id`, tất cả duy nhất; 41 trang đều có ghi chú.
- Storyboard có đúng 41 dòng ánh xạ; không thiếu hoặc thừa mã.
- Tổng thời lượng lấy từ ghi chú: phần giảng 120 phút, phần bài tập 60 phút.
- Số thẻ mở/đóng `<section>` là 48/48; số thẻ mở/đóng ghi chú là 41/41.
- Năm SVG đều phân tích XML thành công, có `role="img"`, `title` và `desc`.
- HTML không tham chiếu ảnh raster, URL ngoài hoặc tài nguyên cốt lõi trên mạng.
- Ba tệp Markdown chỉ dùng dấu đô la cho công thức nội dòng và công thức khối.
- `git diff --check` không báo lỗi khoảng trắng.

## Kiểm định cuối của điều phối viên

- Chạy máy chủ tại thư mục gốc bằng `python3 -m reloadserver 8765`. Môi trường không cài mô-đun toàn cục nên dùng bản tạm trong `/tmp` qua `PYTHONPATH`; máy chủ phục vụ đúng ở cổng 8765.
- Tải thử HTML, RevealJS, CSS, plugin, ba tài nguyên KaTeX thực tế và năm SVG qua HTTP; tất cả trả mã 200.
- Dùng Chromium qua Playwright duyệt tuần tự đủ 41 trang ở khung 1280×720 và 800×600. Hai lượt kiểm thử đạt; không có lỗi JavaScript, yêu cầu mạng thất bại hoặc phần tử vượt khung trang đang trình chiếu.
- Chụp 41 ảnh ở khung 1280×720 và kiểm tra bản ghép toàn bộ. Các trang có giả mã, bảng vết chạy, công thức Bonferroni, năm mạch học phần và bài tập đều đọc được; fragment R05 ẩn đáp án trước bước chữa.

## Cập nhật mạch học tập

- **Mức độ:** nghiêm trọng. **Trang chiếu:** E03. **Vấn đề:** số bài trên bản đồ phản ánh các nhóm chủ đề nhưng không phản ánh thứ tự học liền mạch. **Bằng chứng:** hình cũ ghi `2, 7, 8`, `3, 4, 14`, `5, 6`, `9, 10`, `11–13, 15`; `sources/source.md` đã sắp lại năm mạch thành các khoảng liên tiếp. **Quyết định:** sửa SVG và trang E03 thành `2–4`, `5–7`, `8–9`, `10–11`, `12–15`; đổi tiêu đề từ “tuyến” sang “mạch”.
- E02 được sửa tham chiếu từ Bài 14 cũ sang Bài 7 mới. Đã rà lại E01–E04 theo quy tắc hai trang lân cận; không đổi thời lượng, công thức hoặc mạch lập luận của cụm số chiều lớn.
- Vòng rà lại E01–E04 đã mở rộng văn bản thay thế của E03 để nêu đủ tên năm mạch. Ghi chú E02 cũng được sửa: với vành dày $O(1/d)$, chỉ kết luận một tỷ lệ lớn thể tích nằm gần biên và tỷ lệ phụ thuộc hằng số ẩn; không còn tuyên bố giới hạn bằng 1.
- Kiểm tra lại bằng Chromium ở 1280 × 720 và 800 × 600: đủ 41 trang, không lỗi JavaScript hoặc tài nguyên, không tràn khung. E03 hiển thị đúng năm khoảng bài liên tiếp và đủ tên mạch.
- Kiểm tra bàn phím bằng API điều hướng RevealJS trong cùng chuỗi trang; cấu hình vẫn giữ `controlsLayout: "edges"`, `slideNumber`, `hashOneBasedIndex` và `hash`.
- `2627-1/index.html` đã có đúng một liên kết đến bài hoàn thành và không liên kết tới tệp quy trình.

### Giới hạn Codex Slides

Dự án bền vững có mã `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj`. Trạng thái chuẩn được đọc lại thành công, nhưng dự án vẫn ở bước làm rõ và có 0 trang nội bộ. Tải các tệp cuối vào Design Files trả lỗi HTTP 500; tải HTML làm material thành công nhưng lượt chat không gắn được material vào ngữ cảnh. Giao diện Browser trong trình soạn thảo không khả dụng ở phiên này. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; kiểm định trực quan cuối dựa trên RevealJS cục bộ và Chromium.

## Vòng xây dựng ghi chú bài giảng 2026-09-01

### Phạm vi và quyết định chủ đề

- Chỉ xây dựng ghi chú bài giảng; không viết lại bộ trang chiếu. HTML chỉ được sửa hai điểm dùng chung: thống nhất thuật ngữ “quét–cộng dồn” và sửa nguồn BHK Hình 2.2 thành PDF trang 17.
- Bản đồ N01–N10 gồm bảy chủ đề `cốt lõi` và ba chủ đề `cầu nối` là N02, N09, N10. Không có chủ đề `bổ sung`. BHK PDF trang 18–21 giữ ở mức `đọc thêm`; bất đẳng thức Markov là cầu nối ngắn trong N08.
- Ghi chú dùng lại năm SVG đã có của Bài 01. Không tạo ảnh raster, không thêm dữ liệu, ví dụ thực nghiệm hoặc mệnh đề ngoài nguồn.
- Viewer kế thừa cục bộ cấu trúc phát hành an toàn từ kho `math-4-AI`, đổi toàn bộ nhận diện học phần và dùng Marked, DOMPurify, KaTeX cục bộ. Không gửi mã ngoài workspace đó tới OpenRouter.

### Worker OpenRouter và cổng duyệt

Các lượt được chấp nhận đều báo `requested_model=observed_model=z-ai/glm-5.3-flash` và `provider=OpenRouter` tại runtime.

| Giai đoạn | Vai | Kết quả dùng để triển khai |
|---|---|---|
| Lập kế hoạch | reader | Chốt goal, phạm vi, tiêu chí và rủi ro |
| Phân tích nguồn | reader | Kiểm kê MMDS, Stanford, BHK và ánh xạ nguồn |
| Bản đồ chủ đề | reviewer | Hợp nhất N01–N10; không đề xuất chủ đề bổ sung |
| Soạn và sửa | writer | Tạo bản nháp trong thư mục tạm, rồi sửa theo các báo cáo đã duyệt |
| Góc nhìn sinh viên | reviewer | Yêu cầu giải thích kỳ vọng biến cố, điều kiện $1/H$, ký hiệu và câu tự kiểm tra |
| Phản biện giảng dạy | reviewer | Yêu cầu chuyển hình ba miền, nối Markov vào bài tập và bổ sung kiểm tra |
| Chuyên gia giải thuật và khoa học dữ liệu | reviewer | Phát hiện nguồn BHK lệch, thuật ngữ chưa thống nhất và mục từ không dùng |
| Độ chính xác toán học và thuật toán | reviewer | Xác nhận số học; yêu cầu thống nhất nguồn BHK và bỏ dẫn Stanford lặp |
| Kết nối và mạch viết | reviewer | Yêu cầu cắt siêu bình luận, giải thích $249\,750$ so với $250\,000$ và chỉnh R01 |

Một số lượt reviewer ban đầu chạm giới hạn vòng công cụ và không được dùng làm báo cáo. Điều phối viên dừng phần phụ thuộc, thu hẹp phạm vi rồi chạy lại đúng vai; năm báo cáo trong bảng trên đều hoàn tất và độc lập.

### Sửa sau rà soát và tái kiểm

- Mọi lỗi `nghiêm trọng` đã sửa, đặc biệt là vị trí BHK Hình 2.2. Các điểm trung bình và nhẹ về kỳ vọng chính xác, xác suất có điều kiện, ký hiệu $y,z$, Markov, câu nối, câu tự kiểm tra và nguồn A03 cũng đã xử lý.
- Worker độ chính xác tái kiểm công thức tổ hợp, kỳ vọng, Markov, bất biến, chi phí và giả thiết độc lập: không còn lỗi chặn bàn giao hoặc nghiêm trọng. Xấp xỉ R03 được chuẩn hóa thành $0{,}083$ (xấp xỉ $1/12$).
- Worker mạch viết tái kiểm N01–N10. Sau khi thêm câu tự kiểm tra cho N03, N06, N07, N09 và đổi đầu ra N10 thành áp dụng khung trong các bài sau, lượt xác nhận cuối báo không còn lỗi chặn bàn giao, nghiêm trọng hoặc trung bình.

### Biên tập bản cuối

- Codex chính đọc toàn bộ `lecture-note.md`, dùng `$no-ai-slop` để bỏ lời dẫn rỗng, câu mô tả quy trình, nhịp câu máy móc và đoạn kết tóm tắt lặp. Không đổi mệnh đề, dữ kiện, giả thiết, ký hiệu, kết quả hoặc nguồn.
- Tự kiểm trực tiếp theo `no-ai-slop/eval.md`: đạt các tiêu chí về độ trung thành với nguồn, giọng tự nhiên, câu trực tiếp, không quảng bá, không siêu bình luận và không lặp kết luận.
- Rà mạch theo Quill Outline Workflow: N01–N10 nối liên tục; thuật ngữ, ký hiệu và sản phẩm học tập khớp outline và storyboard. Không tạo `quill.json`.

### Kiểm định viewer và index

- Kiểm tra tĩnh đạt: Markdown bắt đầu bằng H1; ba bảng có hàng tiêu đề; sáu khối directive cân bằng, không lồng; khối mã có ngôn ngữ; năm SVG tồn tại, có `role="img"`, `title`, `desc`; năm mã SRI khớp tệp cục bộ; JavaScript qua `node --check`; không có tài nguyên lõi từ mạng.
- Chromium/Playwright ở 1280×720 và 390×844: 23 mục lục, 178 công thức KaTeX, không lỗi công thức; năm SVG tải đủ; không tràn trang; không lỗi JavaScript, lỗi trang hoặc yêu cầu mạng; gợi ý và lời giải gập mặc định, mở được bằng bàn phím; liên kết bỏ qua điều hướng hoạt động.
- Viewer từ chối đường dẫn ngoài `materials/lec-NN/` và từ chối số bài của `doc`/`deck` không khớp. Bản in A4 gồm 15 trang, tự mở mọi khối gập và ẩn mục lục cùng thanh điều hướng.
- Sau khi viewer đạt, `index.html` mới được cập nhật. Kiểm tra index ở hai khung cho đủ 15 thẻ, đúng một liên kết ghi chú Bài 01, hai tài nguyên Bài giảng/Ghi chú, không tràn trang hoặc lỗi JavaScript.

## Vòng đồng bộ deck với ghi chú bài giảng 2026-09-02

### Điều phối và worker OpenRouter

- Reader kế hoạch `45938` và reader nguồn `19318` dùng `z-ai/glm-5.3-flash` qua OpenRouter; cả hai kết luận không cần thêm, gộp, tách hoặc bỏ trang.
- Writer hợp lệ `15607` dùng `deepseek/deepseek-v4-flash-0731` qua OpenRouter trên bản sao tạm. Phiên `67191` bị dừng ngay vì dùng nhầm model; phiên DeepSeek `42928` hết thời gian trước khi ghi tệp nên không được tính.
- Năm báo cáo reviewer hợp lệ: nguồn–ghi chú `43467`, toán–giải thuật `83574`, sư phạm `26158`, no-ai + mạch Quill `64311`, kỹ thuật tĩnh `3556`. Tất cả reviewer hợp lệ báo `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.
- Hai phiên kỹ thuật `74396` và `53521` chạm giới hạn lượt công cụ, không dùng làm báo cáo. Reviewer kỹ thuật được chạy lại với phạm vi hẹp và hoàn tất ở phiên `3556`.
- Không gửi `.env`, bí mật hoặc thông tin xác thực tới worker. Codex chính chỉ áp dụng các sửa nằm trong phạm vi đã duyệt.

### Quyết định sau năm báo cáo

- Chấp nhận sửa goal/prompt từ sáu thành bảy mạch; HTML và storyboard vốn đã có đúng bảy mạch, hợp chuẩn 5–7.
- Chấp nhận bỏ mã nội bộ `D01` khỏi R01, bỏ cụm “mốc hoạt động”, các nhãn câu nối và tên tệp nội bộ khỏi lời giảng.
- Chấp nhận thống nhất ký hiệu E01 với ghi chú, bổ sung giả thiết phương sai hữu hạn, làm rõ kết quả tổ hợp ở D03–D04/R02 và bán kính trong ở E02.
- Xác minh trực tiếp `mmds-3e-ch01-data-mining.pdf`, trang 7–8: ví dụ nằm ở Mục 1.2.3 và Bài 1.2.1 dùng dữ kiện của mục này.
- Bác đề xuất đổi cấu trúc index ngoài Bài 01 vì thuộc phạm vi đồng bộ toàn học phần, không phải lỗi của deck này. Giữ giả mã A06 không gắn lớp ngôn ngữ vì đây là giả mã, không có ngôn ngữ lập trình xác định. Giữ nhãn hiển thị “Bài 1” theo quy ước giao diện hiện có; `01` vẫn được dùng trong tên tệp và đường dẫn.

### Biên tập bản cuối

- Dùng `$no-ai-slop` trên toàn bộ nội dung hiển thị và ghi chú diễn giả. Kiểm tra theo `no-ai-slop/eval.md` không còn lời dẫn rỗng, nhãn quy trình, câu tổng kết lặp, quảng bá hoặc nhịp câu máy móc.
- Rà theo Quill Revise Workflow: chuỗi kho nhật ký → đặc tả → thuật toán → bất biến → chi phí và chuỗi mô hình ngẫu nhiên → kỳ vọng → bài tập giữ nguyên dữ kiện, ký hiệu và đầu ra. Không tạo `quill.json`.
- Ghi chú bài giảng chỉ đổi một công thức để thống nhất ký hiệu véc-tơ $\mathbf{y},\mathbf{z}$ và chỉ số $j$; đã rà lại E01 của deck và N09 của ghi chú.

### Kiểm định kỹ thuật và trực quan

- 41 `data-slide-id` duy nhất, 41 ghi chú diễn giả, 48 thẻ `<section>` mở/đóng cân bằng và bảy section ngoài.
- Năm SVG phân tích XML thành công, có `role="img"`, `title` và `desc`; không có ảnh raster hoặc tài nguyên lõi từ mạng.
- Chromium duyệt đủ 41 trang ở 1280×720, 800×600 và 720×900: không tràn khung, không lỗi JavaScript, KaTeX, trang hoặc yêu cầu tài nguyên.
- Điều hướng bàn phím đi đúng từ P00 xuống P01 và sang A00. Bản in A4 có 41 trang; 41 ghi chú tồn tại; không có phần tử `.katex-error`.
- Ảnh render D03, D04, E01, E02, E03, R01 và R02 được xem trực tiếp; công thức, nhãn SVG và phần bài tập đều đọc được.
- `index.html` đã có đúng liên kết Bài giảng và Ghi chú của Bài 01; không cần đổi URL hoặc tài nguyên.
- Dự án Codex Slides chuẩn `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj` đọc được nhưng vẫn ở bước làm rõ với 0 trang nội bộ. Browser Codex Slides không khả dụng trong phiên; vì vậy bằng chứng trực quan dùng RevealJS cục bộ và Chromium, không tuyên bố đã xem deck trong Codex Slides.

### Tái kiểm

- Toán–giải thuật: phiên `50263`, GLM/OpenRouter, PASS; tính lại D04, R02, R03, R05 và xác nhận bất biến, chi phí, giả thiết cùng hai SVG.
- Mạch/no-ai: phiên `29457`, GLM/OpenRouter, PASS; xác nhận E01, E03, R01, năm SVG, bảy mạch và việc dọn nhãn quy trình đều đạt.

## Lập lại kế hoạch theo ứng dụng — 2026-09-06

### Phạm vi bàn giao

Yêu cầu mới là lập lại kế hoạch Bài 01 từ thông tin Bài 02–15: ứng dụng → nhu cầu nhiều mặt → giới thiệu học phần/thuật toán/thuộc tính → kiến thức, kỹ năng và thái độ; lập kế hoạch hình cho mọi ví dụ. Ba tệp planning được cập nhật. Chưa triển khai HTML, ghi chú công khai, SVG hoặc index; chưa commit/push bản công khai mới. Các báo cáo kiểm định và công bố ở những mục ngày trước chỉ áp dụng cho phiên bản cũ.

Kế hoạch mới có 39 trang giảng, 120 phút, và sáu trang bài tập, 60 phút; bảy phần ngoài. A/B dành 45 phút cho 16 tình huống; C phân tích nhu cầu và một ví dụ giải thuật; D/E giới thiệu chương trình và sự chuẩn bị; F kiểm tra giả thiết, kết luận; R giữ hai bài MMDS. Danh mục hình bao phủ 18 ví dụ, thêm một bản đồ học phần. Tất cả hình mới đều có trạng thái dự kiến.

### Kiểm kê và căn cứ

- Đọc bản đồ cấp học phần và bảng slide tham khảo trước khi chọn ví dụ; giữ thứ tự đề xuất, Bài 01 từ buổi gốc 1. Đối chiếu mục tiêu, phạm vi, nguồn và các đoạn HTML liên quan của Bài 02–15.
- Đọc template, CSS và index để ràng buộc bố cục. Không đổi nhận diện hay thư viện. Ghi chú hiện có được kiểm tra về tình huống, ký hiệu và mạch; storyboard ghi phạm vi cần đồng bộ ở lần triển khai.
- Nguồn Bài 01 có trong kho: Stanford 01-intro, MMDS Chương 1, BHK. Đã trích đọc slide Stanford và kiểm trực tiếp trang 62; MMDS tr.7–8 cho đề và giả thuyết hai bài tập, tr.13 cho lưu trữ; BHK PDF 9–12 cho mô hình truy cập và dữ liệu nhiều chiều.
- Kiểm trực tiếp các trang nguồn được chọn để chốt ví dụ quy mô: MMDS Ch2 slide 4, 8–12; MMDS Ch3 slide 15–16, 24; Stanford 03-lsh slide 14; BIODS 271 PDF 17–18. Các nguồn DSC/nén/chỉ mục còn lại được truy nguyên qua outline và ghi chú của bài đã có; kế hoạch không tuyên bố đã kiểm lại toàn bộ PDF/PPTX của 14 bài trong lượt này.
- Đối chiếu [trang Stanford CS246](https://web.stanford.edu/class/cs246/) để xác nhận nơi công bố học liệu. Trang chính MMDS không tải được trong hai lần kiểm tra: “Failed to fetch https://www.mmds.org/: (400) Timeout fetching” và bản không www tương tự. Dùng các slide MMDS chính thức đã có cục bộ; giữ yêu cầu ghi công http://www.mmds.org khi triển khai.

### Tác tử và quyết định điều phối

Các phiên hợp lệ bên dưới đều có metadata runtime requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter; không dùng lời tự khai của worker làm bằng chứng. Không đọc hoặc đưa nội dung tệp .env vào prompt.

| Vai | Phiên | Kết quả và quyết định |
|---|---|---|
| Reader lập kế hoạch | 80347 | Nhận bản đồ năm mạch và danh mục phương pháp. Bác đề xuất giữ nguyên 41 trang và chỉ mở rộng bản đồ cuối bài vì trái yêu cầu mới. |
| Reader phân tích nguồn | 72326 | Lượt đầu finish_reason=length; phản hồi cuối chỉ còn phần rủi ro, không tính bảng bị cắt là đã nhận. Chấp nhận cảnh báo tải mạch B, hỗ trợ tiên quyết bài tập và phân biệt số liệu lịch sử/mô hình/đo. |
| Reader bổ sung bàn giao nguồn | 76038 | Đã đọc phạm vi đầu của 14 outline; nhận bảng liên hệ bài–ứng dụng–nhu cầu. Bỏ hàng Bài 01 dư; điều phối viên bổ sung nguồn đến trang và tách tình huống theo đầu ra. |
| Writer bản nháp có phạm vi | 50897 | Chỉ đọc hồ sơ đã duyệt trong thư mục tạm, trả nội dung qua output. Chấp nhận cấu trúc đầu vào/đầu ra và các quy tắc minh họa; biên tập trước khi áp dụng bằng apply_patch. |

Bác hai câu chuyển do writer đề xuất: “Mỗi cách xử lý ... đều quy về ... quét dữ liệu và cộng dồn trạng thái” và “Vì nhu cầu quét–cộng dồn lặp lại, học phần ... tổ chức thành năm nhóm”. Các thuật toán xếp hạng, chỉ mục, nén và hàng xóm gần không có cùng cơ chế đó. Storyboard thay bằng cầu nối dựa trên yêu cầu và mô hình chi phí. Chuyển thiết kế/triển khai/đánh giá về CLO3, hành vi học tập và trách nhiệm về CLO4.

Các đề xuất sai của reader cũng bị loại: dữ liệu lớn “không đổi độ khó”; bộ kết hợp MapReduce là xấp xỉ; HNSW thuộc nhóm phép lặp có bảo đảm hội tụ. Bảo đảm của từng phương pháp được mô tả riêng; không gán bảo đảm xác suất cho mọi cấu trúc dòng.

### Sự cố công cụ và xử lý

Lần chạy đầu gặp “Could not acquire lock ... Read-only file system (os error 30)” ở cache uv ngoài vùng ghi. Đổi cache sang thư mục tạm. Phiên 67954 trong sandbox báo “worker_failed ... api_transport_error”; không dùng kết quả phiên này.

Duyệt tự động từng từ chối reader vì cho rằng chưa có quyền gửi dữ liệu kho tới OpenRouter. Điều phối viên đọc lại điều khoản cho phép tại AGENTS.md mục “Điều phối mô hình trong dự án”, cung cấp bằng chứng và được chấp thuận chạy lại. Writer thư mục tạm từng bị từ chối vì gốc tạm bị xem là ngoài phạm vi; đọc lại bước 4 của quy trình OpenRouter về hồ sơ nguồn trong thư mục tạm, cung cấp bằng chứng, được chấp thuận. Không đổi nhà cung cấp hoặc lách quyết định từ chối.

### Sai khác có chủ ý và tác động

| Nội dung | Quyết định | Lý do và tác động |
|---|---|---|
| Mở bài và luận điểm | thay toàn bộ cấu trúc | Bắt đầu bằng ứng dụng và giới hạn; giới thiệu chương trình sau 70 phút đầu về ứng dụng/nhu cầu |
| Quét–cộng dồn | giữ, rút ngắn | Là ví dụ đầy đủ trong C, không chiếm một mạch 32 phút riêng |
| Tín hiệu giả | rút phần giảng; giữ bài tập | Có 12 phút F01–F03 và gợi ý dựng mô hình ở R01; bài tập giữ nguồn, dữ kiện và yêu cầu |
| Cao chiều và lọc thư | chuyển khỏi tuyến chính | V07 đủ định vị véc-tơ; không cần hình thể tích hoặc ví dụ lọc thư để hoàn thành mục tiêu mới |
| Bản đồ học phần | tách thành D02–D07 | Không đưa danh mục 14 bài lên một trang; giữ đúng năm mạch liền nhau |
| Năng lực sinh viên | thêm E01–E04 | Tách điều kiện đầu vào và chuẩn đầu ra; gắn thái độ với hành vi có thể quan sát |
| Hình minh họa | đặc tả H01–H19 | Giữ dữ liệu/quan hệ của nguồn, chỉ vẽ lại khi triển khai; không tạo ảnh đo giả |
| Băng thông | dự kiến đổi b thành v | Tránh lẫn số khối; phải đồng bộ HTML/ghi chú/hình trong lần triển khai |
| N01–N10 hiện có | lập ánh xạ tác động | Cần đổi thứ tự, mở/kết và câu nối khi triển khai; không sửa ghi chú trong yêu cầu chỉ lập kế hoạch |
| Hình bản đồ dùng ở index | giữ bản đang công khai | Sau khi sửa H19 phải rà cả index; lần này không công bố liên kết hay nội dung chưa kiểm định |

### Kiểm tra của điều phối viên

- Kiểm tra tự động: 45 mã trang duy nhất; thời lượng A/B/C/D/E/F/R lần lượt 22/23/25/20/15/15/60; đủ 14 hàng Bài 02–15; đủ 18 ví dụ có đặc tả hình.
- Tính lại số cặp với số nguyên: 499.999.500.000; kỳ vọng lưu trú là 249.749,99975025, làm tròn 249.750; kỳ vọng cặp lượt mua trùng khoảng 0,000189818469. Không gọi giá trị làm tròn là giá trị tổ hợp chính xác.
- Markdown dùng dấu dollar cho công thức; bảng có hàng tiêu đề; git diff --check không lỗi khoảng trắng.
- Áp dụng Quill Outline Workflow cho thứ tự, thuật ngữ, quan hệ trước–sau và tác động lên ghi chú; không tạo quill.json. Áp dụng no-ai-slop cho nội dung kế hoạch/lời chuyển, loại phát biểu phô trương và quy nạp quá mức của worker; tự rà theo eval.md.
- Kiểm định hiển thị, bàn phím, KaTeX của deck mới, SVG mới, viewer và Codex Slides thuộc bước triển khai; chưa thực hiện hoặc tuyên bố đạt. Không tạo dự án/deck Codex Slides mới trong phạm vi chỉ sửa kế hoạch cục bộ.


### Năm báo cáo độc lập và quyết định cuối

Các báo cáo dưới đây chỉ rà kế hoạch văn bản. Các phiên hoàn tất đều xác nhận requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter.

| Vai / phiên | Mức độ | Vị trí và bằng chứng | Quyết định |
|---|---|---|---|
| Sinh viên / 11311 | không chặn/nghiêm trọng; khuyến nghị nhẹ | 16 tình huống/45 phút, mỗi tình huống một đầu ra và giới hạn; hình V01–V18 đủ. Đề nghị rõ R00 không tính phút và sửa số dính chữ | Đã làm rõ R00 và chuẩn hóa khoảng trắng. Không nhận “sai số tổng phút” là lỗi vì chính báo cáo cộng đúng120/60; không nhận lỗi font không có bằng chứng trong tệp |
| Chuyên gia giải thuật / 51117 | không chặn/nghiêm trọng; khuyến nghị nhẹ | Đủ14bài, phân loại độ đo/mô hình/cấu trúc/phần mềm; đề nghị đồng nhất nguồn hình với nguồn ứng dụng | Giữ nguồn theo vai trò: MMDS Ch2 slide4 là quy mô, H02 dùng8–12/20 là sơ đồ. Spark/Faiss chỉ giải thích loại công cụ, không bổ sung mục tiêu hoặc trang; BHK đã có trong phần nguồn/khung mô hình |
| Toán–thuật toán / 45184 | không lỗi bắt buộc trong phạm vi đọc | Xác nhận số cặp, kỳ vọng lưu trú và cấu trúc công thức giỏ hàng; phạm vi outline được giao lệch xuống đoạn cuối nên chưa rà đủ giả thiết bảng băm | Điều phối viên tính lại số học và đọc đặc tả; giao bổ sung riêng phần giải thuật ở phiên22429. Không lấy câu xác nhận đơn vị/bảng băm ngoài đoạn đã đọc làm bằng chứng |
| Phản biện giảng dạy / 61897 | không chặn/nghiêm trọng; nhẹ | Chu trình quét đầy đủ và phân bổ120+60khớp. F02–F03 chỉ9phút mô hình xác suất; F01 là3phút trách nhiệm/giả thiết | Ghi rõ9phút mô hình +3phút giả thiết +3phút kết luận. Đây là chỉnh cách mô tả, không đổi thời lượng, thứ tự hay yêu cầu của người dùng |
| Kết nối và mạch viết / 95083 | không chặn/nghiêm trọng; nhẹ | Xác nhận tuyến A→B→C→D→E→F→R,45trang và18ví dụ; đề nghị làm rõ phạm vi sáu/bảy phần và tên takes | Đã rõ sáu phần giảng, tổng bảy với R; đổi B09 thành “Kết nối hai bảng theo mã sinh viên”. Giữ F04 quay về V01/V06 vì đúng ứng dụng mở đầu; F01 dùng V05 để vào giới hạn suy luận |

Lượt toán ban đầu72261 thất bại với lỗi nguyên văn “model returned an empty or incomplete answer after all retries”; lượt sư phạm86568 thất bại “model exceeded the tool-call limit (8)”. Dừng chốt phần phụ thuộc, thu hẹp nhiệm vụ và chạy lại đúng vai ở45184/61897; không chuyển nhà cung cấp. Không tính hai lượt lỗi là báo cáo hoàn tất.

Writer chỉnh sửa riêng38861 được giao ba đoạn ngắn sau khi đủ năm báo cáo. Chấp nhận cách tách9phút mô hình xác suất; bác lỗi đơn vị “R01–R05 tổng60trang” và thay bằng60phút; chọn tiêu đề tiếng Việt cụ thể theo phép nối. Điều phối viên áp dụng tuần tự bằng apply_patch và rà lại B07–C02, F01–R02; không đổi chức năng hoặc câu nối giữa các mạch.

Biên tập cuối theo no-ai-slop/eval.md: giữ yêu cầu của người dùng, nguồn và dữ kiện; bỏ câu tổng quát hóa không có căn cứ của worker; thống nhất thuật ngữ và số có khoảng trắng. Quill kiểm lại thứ tự ứng dụng→nhu cầu→khóa học→chuẩn bị→giới hạn suy luận; ánh xạ ảnh hưởng tới ghi chú được giữ rõ. Không phát sinh dự án sách.

Kiểm định Markdown bổ sung: 47 công thức trong outline/storyboard render thành công bằng KaTeX cục bộ; liên kết Markdown tương đối đều tồn tại. Các tên SVG tương lai là đặc tả, không phải liên kết công bố.

Phiên bổ sung toán–thuật toán 22429 hoàn tất, metadata GLM/OpenRouter khớp. Đã đọc đúng outline 116–126 và storyboard 51–59; xác nhận miền, đầu ra, bất biến, dừng/biên, chi phí kỳ vọng có điều kiện, đơn vị byte/khối và thứ tự vết trước đặc tả; không phát hiện lỗi. Phản hồi tự ghi nhầm số phiên 45184; nhật ký dùng ID phiên thực tế từ lệnh chạy, không dùng số tự khai đó.

Chốt phạm vi: ba tệp kế hoạch đã cập nhật và kiểm tra, không còn lỗi bắt buộc trong các báo cáo được chấp nhận. Không đưa thay đổi có sẵn của người dùng ở AGENTS.md, .gitignore hoặc công cụ OpenRouter vào công việc này. Việc xây dựng, kiểm định và công bố deck/ghi chú theo kế hoạch mới là bước triển khai tiếp theo.


## Triển khai slide và ghi chú ngày 2026-09-06

### Phạm vi và sao lưu

Theo yêu cầu tiếp theo của người dùng, triển khai kế hoạch đã duyệt thành HTML, ghi chú, SVG và tài nguyên chỉ mục; người dùng cho phép commit/push sau khi xong. Bản sao trước sửa nằm tại [thư mục sao lưu](../../backups/lec-01/2026-09-06-before-applications/README.md), gồm HTML, ghi chú, index, năm SVG và ba tệp kế hoạch. Không ghi đè các thay đổi ngoài Bài 01.

Bản mới có 45 trang: 39 giảng, sáu trang phần bài tập kể cả chuyển phần; bảy phần ngoài. Storyboard giữ 120+60 phút. Có 19 hình dùng cho 18 tình huống và bản đồ; thay ba SVG cũ, thêm 16 SVG. Hai SVG cũ không dùng trong tuyến mới vẫn được giữ. Ghi chú viết lại theo tám chủ đề, có đầy đủ đặc tả, vết, giả mã, chứng minh, biên và chi phí tổng byte; nguồn bài tập không đổi.

### Cổng lập kế hoạch và phân tích

- Reader lập kế hoạch phiên 33374: hoàn tất, requested_model=observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Chấp nhận trình tự sao lưu–hình–HTML–ghi chú–chỉ mục và kiểm 45 trang/7 mạch/120+60.
- Reader nguồn phiên 90386: hoàn tất, cùng model/provider. Chấp nhận kiểm kê đặc tả, bất biến, giới hạn và hai bài tập. Bác lỗi đọc số kỳ vọng thành 249749999750,25; điều phối tính trực tiếp được 249749,99975025. Nguồn gốc MMDS tr.7–8 được đọc lại để chốt đề và giả thuyết.
- Bản đồ chủ đề độc lập từ giai đoạn kế hoạch tiếp tục được dùng; quyết định giữ/thêm/đọc thêm trong outline không mở rộng sang cơ chế bài khác. Hồ sơ và đặc tả triển khai tạm được duyệt trước writer.

### Soạn và hợp nhất

Writer phiên 83610 hoàn tất qua OpenRouter, requested_model=observed_model=z-ai/glm-5.3-flash. Phần việc giới hạn là D03–E04 và bảng chương trình/chuẩn bị của ghi chú. Điều phối giữ ánh xạ phương pháp–thuộc tính, nhưng sửa bản nháp trước tích hợp: thêm data-slide-id, bỏ V và mã quy trình trên mặt trang/aside; đặt tên phương pháp đại diện lên slide; bỏ nhận định sai “nén là cấu trúc” và cam kết giữ chính xác độ tương đồng; không tự đặt lần thực hành bắt buộc. Điều phối tự triển khai các phần còn lại, SVG, đặc tả, chứng minh và lời giải bằng apply_patch.

Dùng quill để kiểm mạch ứng dụng → giới hạn → một lời giải đầy đủ → chương trình → chuẩn bị → suy luận; không tạo quill.json theo quy ước kho. Tóm tắt thay đổi liên tục: trước đây mở bằng giới thiệu và tập trung mô hình; nay mở ngay tổng byte và khảo sát Bài 02–15. Thuật ngữ, dữ kiện và nguồn các bài sau không đổi; không cần sửa Bài 02–15. Đồng bộ v thay b ở toàn bộ Bài 01; khung quét một lượt là lựa chọn lời giải, không suy từ D>M thành bắt buộc một lượt cho mọi thuật toán.

Dùng no-ai-slop cho mặt trang, aside và ghi chú; bỏ lời dẫn rỗng, mã quy trình, khẩu hiệu và các đoạn đọc thêm làm đứt tuyến. Các phân biệt toán học cần thiết được giữ, không cắt giả thiết để rút câu.

### Các báo cáo độc lập trên bản nháp

Sáu phiên reviewer riêng đọc cả HTML/aside, ghi chú và storyboard. Runtime của mỗi phiên có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Các báo cáo dưới đây là đầu ra nguyên văn; quyết định của điều phối ở sau, không mặc nhiên chấp nhận mọi nhận định.


#### Phiên 26601: storyboard

> # Báo cáo rà storyboard – HTML – lecture-note Bài 01
>
> **Phạm vi đã kiểm:** đọc toàn bộ 3 tệp (storyboard 185 dòng, HTML 309 dòng, ghi chú 503 dòng); đối chiếu số trang, thời lượng, dữ kiện số, chu trình quét–cộng dồn, thứ tự ứng dụng → thuật toán, nguồn bài tập, ánh xạ 8 chủ đề ghi chú. Không kiểm tra rendered RevealJS/SVG (nằm ngoài 3 tệp yêu cầu).
>
> **Kết quả kiểm tra chính (đạt):**
> - Số trang 39+6=45; mã duy nhất A01–A07, B01–B09, C01–C08, D01–D07, E01–E04, F01–F04, R00–R05 khớp HTML.
> - Thời lượng 22+23+25+20+15+15=120 và 10+15+10+10+15=60 khớp từng trang.
> - Thứ tự tuyến "ứng dụng trước, thuật toán sau" đúng: A/B khảo sát, C02–C06 mới có giả mã/bất biến; không có tên thuật toán chuyên biệt giới thiệu sớm.
> - Chu trình quét–cộng dồn đủ 8 bước: vết 4 bản ghi (40; 40/25; 55/25; 55/25/0 khớp C02/giả mã/bất biến/chi phí C06, cả khóa c.vn=0 và dãy rỗng đều được xử lý ở C05 và ghi chú).
> - Các phép tính suy ra trực tiếp đều đúng: cơ sở 249 749,99975025; (a) 999 500; (b) 249 750; (c) 0,0831; giỏ hàng ≈1,90×10⁻⁴; V06 499 999 500 000.
> - Nguồn bài tập MMDS 1.2.1(a–c), 1.2.2 và chú thích 3 được giữ đúng ở R01–R05 và ghi chú.
> - 8 chủ đề N01–N08 đều có mục tương ứng trong ghi chú (tổng hợp/tìm kiếm; dòng–khôi phục–truy vấn; quét–cộng dồn; khung đánh giá; nội dung học phần; kiến thức–kỹ năng; mô hình ngẫu nhiên; bài tập).
>
> **Không có lỗi chặn bàn giao hoặc nghiêm trọng.** Các điểm nhỏ:
>
> 1. **Nhỏ – HTML, ghi chú nhiều trang (vd. A07, B09, F02, R02, R03):** thiếu dấu cách sau số, như "tình huống10 tỷ véc-tơ3072 chiều,32 bit", "Ngân sách20 khối", "lập luận100 chỗ", "giảm4 lần", "là(q²/H)³". Đề xuất: rà chính tả dấu cách trước khi xuất bản.
> 2. **Nhỏ – HTML B09, thẻ "Dữ liệu":** chỉ ghi 100/400 khối, thiếu 5.000/10.000 bản ghi như storyboard dòng 51 (số nằm ở ghi chú). Đề xuất: thêm số bản ghi vào thẻ để mặt trang đủ dữ kiện.
> 3. **Nhỏ – ghi chú dòng 397:** ghi "mục 1.2.4" trong khi storyboard và phần còn lại dùng "1.2.1/1.2.3, tr. 8". Nên thống nhất cách gọi mục bài tập để tránh nhầm lẫn.
>
> **Kết luận:** không có lỗi bắt buộc phải sửa trước bàn giao; ba điểm nhỏ trên là biên tập.

#### Phiên 37741: student

> ## Báo cáo rà soát góc nhìn sinh viên — Bài 01
>
> **Phạm vi đã kiểm:** toàn văn 3 tệp (HTML 309 dòng, lecture-note.md 503 dòng, storyboard.md 185 dòng). Chưa kiểm hình ảnh render/SVG, KaTeX runtime, RevealJS — nêu riêng ở mục rủi ro thị giác.
>
> **Chặn bàn giao:** không phát hiện.
>
> **Nghiêm trọng:** không phát hiện. Các phép tính suy ra trực tiếp đều đúng khi kiểm lại: C(10⁶,2)=499.999.500.000 (A06, note dòng 57–61); E[X]=249.749,99975025 (F03, note dòng 375–380); (a) 999.499,999 ≈ 3998/999 × cơ sở (R02, note dòng 426–433); (b) gần 249.750 (P×4, xác suất÷4); (c) 0,0831 (R03, note dòng 447–450); E[Y]≈1,90×10⁻⁴ (R05, note dòng 478–482). Thời lượng storyboard 22+23+25+20+15+15=120 và 10+15+10+10+15=60, số trang 39+6=45 khớp đếm trực tiếp trên slide.
>
> **Nhỏ:**
> 1. HTML slide L01-C02 (dòng 135): bảng vết bắt đầu từ bước 1, thiếu bước 0 "Chưa đọc / Bảng rỗng" có trong ghi chú (dòng 181). Sinh viên đối chiếu hai nguồn sẽ thấy lệch đánh số. Đề xuất: thêm dòng bước 0 hoặc ghi chú hai bảng đánh số khác nhau.
> 2. Slide L01-E01 (dòng 216): câu hỏi "giải thích xác suất hai lựa chọn độc lập" hơi mơ hồ — chọn cái gì độc lập chưa nêu trên mặt slide; ghi chú (dòng 217) mới nói rõ. Đề xuất thêm "hai người đi khách sạn cùng ngày".
> 3. Ghi chú dòng 377 viết "249\,749\,99975025" chỉ bằng khoảng trắng ngăn nhóm, dễ đọc nhầm thành số nguyên ~2,5×10¹⁴; đề xuất dùng dấu thập phân rõ: 249 749,99975025 (slide L01-F03 ghi đúng hơn).
> 4. Storyboard dòng 7 "39 trang giảng" và dòng 166 "39+6=45" nhất quán, nhưng dòng 7 ghi "sáu trang bài tập kể cả trang chuyển phần" trong khi R00 không tính phút — nhất quán về số, không phải lỗi.
>
> **Độ dễ hiểu/theo dõi:** tốt. Định nghĩa trước ví dụ (A01–A06), giả mã–bất biến–chi phí nối mạch C rõ; bài tập có gợi ý/lời giải phân tầng. Ngôn ngữ nhất quán, thuật ngữ được định nghĩa khi xuất hiện.
>
> **Rủi ro thị giác (chưa kiểm render):** các slide dày như L01-B09, L01-D07, L01-C08 (bảng + thẻ + `.check`) và `.figure` max-height 320px trên khung 720px có nguy cơ tràn; cần kiểm thử 1280×720 theo đúng storyboard dòng 168 trước bàn giao. Alt-text đã cụ thể theo đặc tả hình storyboard.
>
> **Kết luận:** không có lỗi bắt buộc; 4 điểm nhỏ nên sửa trước bàn giao, kèm kiểm thử render hình học slide.

#### Phiên 77429: algorithms

> # Báo cáo rà soát Bài 01 (slide/aside, ghi chú, storyboard)
>
> **Phạm vi đã kiểm:** toàn văn 3 tệp (HTML 309 dòng, lecture-note.md 503 dòng, storyboard.md 185 dòng). Đã kiểm trực tiếp các phép tính: C(10⁶,2)=499 999 500 000; E[X]=249 749,99975025; biến thể (a) 999 499,9990005 (tỷ lệ 3998/999); (b) 249 749,999875125; (c) 0,08308…; E[Y]≈1,90×10⁻⁴ và cận Markov Pr(Y≥1)≤E[Y]. Tất cả đúng. Thời lượng 22+23+25+20+15+15=120 và 10+15+10+10+15=60 đúng; số trang 39+6=45 khớp số section trong HTML (39 giảng + R00–R05).
>
> **Không phát hiện lỗi chặn bàn giao hay lỗi nghiêm trọng.** Phân loại mô hình/cấu trúc/thuật toán được giữ nhất quán (MapReduce là mô hình xử lý, Jaccard là độ đo, chỉ mục là cấu trúc dữ liệu, HNSW/HITS/AMS/DGIM giữ như tên phương pháp); điều kiện các bảo đảm (Bloom chỉ dương tính giả dưới điều kiện băm/trạng thái, DGIM cận xác định, đối chiếu lại không cứu cặp bị bỏ sót, O(n) chỉ kỳ vọng) đều nêu đúng và đủ; không đòi dạy thuật toán bài sau trong mở đầu.
>
> **Lỗi nhỏ:**
>
> 1. **Vị trí:** lecture-note.md dòng 408 (đề bài 1.2.1(c)). **Vấn đề:** cách diễn đạt "cùng ở **một** khách sạn vào cùng thời điểm trong ba ngày khác nhau" dễ đọc thành cùng một khách sạn cả ba ngày (sẽ cho xác suất q²/H³, không phải (q²/H)³). **Bằng chứng:** lời giải dòng 448–449 và aside slide L01-R03 dùng (q²/H)³ với chú thích "khách sạn có thể khác". **Đề xuất:** sửa câu đề thành "cùng khách sạn trong từng ngày, khách sạn có thể khác giữa các ngày" cho khớp lời giải.
>
> 2. **Vị trí:** storyboard.md dòng 44 (L01-B02). **Vấn đề:** dùng "độ lệch" trong khi slide L01-B02 và ghi chú (dòng 95) nói "mômen thứ hai / mức tập trung của tần suất". **Đề xuất:** thống nhất thành "mômen tần suất".
>
> 3. **Vị trí:** HTML dòng 183 (alt của ban-do-hoc-phần.svg). **Vấn đề:** dấu hai chấm dính chữ "nhóm:2–4, 5–7…" thiếu khoảng trắng, ảnh hưởng văn bản đọc được (accessibility). **Đề xuất:** thêm khoảng trắng sau dấu ":".
>
> **Kết luận:** không có lỗi bắt buộc; khuyến nghị sửa 3 điểm nhỏ trước bàn giao.

#### Phiên 4384: math

> ## Báo cáo rà soát độ chính xác toán học — Bài 01
>
> **Phạm vi đã kiểm (đọc đủ cả 3 tệp):** đặc tả (C03), giả mã (C04), bất biến (C05), chi phí (C06), biên; hai ví dụ xác suất (F02–F03, 1.2.2) và toàn bộ lời giải bài tập (R02, R03, ghi chú mục 1.2.1–1.2.2); storyboard mục "Dữ kiện số".
>
> **Tự tính kiểm tổ hợp — kết quả khớp:**
> - $\binom{10^6}{2}=499\,999\,500\,000$ ✓.
> - Cơ sở: $E[X]=\binom{10^9}{2}\binom{1000}{2}10^{-18}=249\,749{,}99975025$ ✓ (slide F03, ghi chú dòng 377, storyboard dòng 130).
> - (a) $999\,499{,}9990005\approx999\,500$; tỷ lệ $\binom{2000}{2}/\binom{1000}{2}=3998/999$ ✓ (dòng 429–433, R02).
> - (b) $249\,749{,}999875125\approx249\,750$; H tăng gấp đôi nên $(q^2/H)^2$ giảm đúng 4 lần ✓ (dòng 438–443, R02).
> - (c) $\binom{10^9}{2}\binom{1000}{3}10^{-27}=0{,}0830834999169165$ ✓ (dòng 448–449, R03, storyboard); xấp xỉ $T^3/6\to0{,}0833$ ✓.
> - 1.2.2: $E[Y]=\binom{10^8}{2}100^2/\binom{1000}{10}\approx1{,}90\times10^{-4}$ ✓ (dòng 479–481); Markov $\Pr(Y\ge1)\le E[Y]$ suy ra đúng một bước ✓ (dòng 486).
> - Phân biệt kỳ vọng biến cố với số cặp người và với suy luận danh tính: nêu đúng và nhất quán ở F03, dòng 385, 488, 278, 288 ✓.
> - Bất biến tiền tố, xử lý dãy rỗng, khóa tổng 0, không tràn: đúng ✓.
>
> **Không phát hiện lỗi chặn bàn giao hay lỗi nghiêm trọng.**
>
> **Nhỏ (cosmetic, 1 mục):**
> - HTML, các aside (ví dụ dòng 250, 273, 278): thiếu dấu cách do nén ký tự — "làm tròn249750", "(q²/H)³=10⁻²⁷; có C(1000,3)bộ", "gần gấp4cơ sở". Ảnh hưởng hiển thị/chính tả ghi chú diễn giả, không sai số học. Đề xuất: thêm khoảng trắng khi biên tập lại aside.
>
> **Kết luận:** mọi con số tổ hợp, xác suất một phép thử, tuyến tính kỳ vọng và giới hạn suy luận đều được tự tính kiểm tra và khớp; phạm vi đã kiểm nêu trên, không có lỗi bắt buộc sửa ngoài lỗi trình bày nhỏ.

#### Phiên 19275: pedagogy

> ## Báo cáo phản biện Bài 01
>
> **Phạm vi đã kiểm:** toàn văn 3 tệp (HTML 309 dòng, ghi chú 503 dòng, storyboard 185 dòng) theo 5 tiêu chí yêu cầu. Không sửa tệp, không tra cứu ngoài.
>
> **Kiểm số học (trực tiếp, không đòi nguồn):** C(10⁶,2)=499.999.500.000 ✓; 249.749,99975 ✓; 3998/999≈4,002 ✓; E[Y]≈1,90×10⁻⁴ ✓; tổng phút A=22, B=23, C=25, D=20, E=15, F=15 → 120 ✓; R01–R05=10+15+10+10+15=60 ✓; 39 trang giảng + 6 trang bài tập = 45 ✓. Thứ tự slide A→F→R khớp chu trình ứng dụng→nhu cầu→học phần→chuẩn bị và câu nối storyboard, không bị áp nhầm. Hỗ trợ bài tập nguồn (MMDS 1.2.1, 1.2.2) có đề, gợi ý, lời giải, tiêu chí chấm ở cả HTML và ghi chú ✓.
>
> **Nghiêm trọng — thiếu mục tiêu đo được của bài học**
> - Vị trí: HTML L01-D01; storyboard dòng 60; ghi chú mục "Nội dung học phần".
> - Vấn đề: D01 chỉ liệt kê 4 CLO cấp học phần (giải thích, phân tích, thiết kế, tự học) — không thể đo ở mức một buổi. Không trang nào phát biểu "kết thúc bài này sinh viên làm được X" với sản phẩm kiểm tra được (ví dụ: đặc tả + chứng minh bất biến + bảng chi phí của ví dụ tổng byte, hay giải 1.2.1a với đúng đơn vị đếm). E02 liệt kê sản phẩm nhưng gắn với toàn học phần. Storyboard dòng 136 thừa nhận recitation "không đánh giá đủ mọi mục tiêu" nhưng không nêu mục tiêu thay thế đo được của Bài 01.
> - Đề xuất: thêm 2–3 mục tiêu đo được cấp bài (động từ hành vi + sản phẩm + tiêu chí đạt) vào D01 và ánh xạ sang C06/C08/F04/R01–R05.
>
> **Nhỏ**
> 1. HTML L01-A01 không mang tên bài trên mặt trang như storyboard dòng 7 cam kết ("A01 đồng thời mang tên bài"); chỉ có dòng identity nhỏ. Đề xuất thêm tiêu đề bài hoặc nêu rõ là fixed header chung.
> 2. L01-F04: storyboard dòng 74 cho phép "V01 hoặc V06", mặt slide chỉ dùng V01; ghi chú cũng vậy. Nhất quán nhưng nên ghi rõ lựa chọn đã chốt trong storyboard.
> 3. Ghi chú dòng 397 ghi "mục 1.2.4, trang 8" trong khi slide R00 ghi "Mục 1.2 · Bài 1.2.1"; nên thống nhất cách dẫn mục.
>
> **Kết luận:** không có lỗi chặn bàn giao; một lỗi nghiêm trọng về mục tiêu đo được cần xử lý trước khi dùng chính thức.

#### Phiên 23373: coherence

> ## Báo cáo rà soát Bài 01 (HTML, lecture-note.md, storyboard.md)
>
> **Phạm vi đã kiểm:** đọc toàn văn ba tệp (309/503/185 dòng, trong giới hạn 650); đối chiếu thứ tự tuyến, số trang, tổng thời lượng, tính nhất quán thuật ngữ/ký hiệu/số liệu, nguồn truy nguyên, lời mở–nối–kết. Không kiểm render RevealJS, SVG, KaTeX (ngoài phạm vi đọc tệp), không đòi nguồn ngoài.
>
> **Kết quả cấu trúc — đạt:**
> - Thứ tự ứng dụng (A01–B09) → phân tích một lời giải (C) → học phần (D) → chuẩn bị (E) → giới hạn suy luận (F) → bài tập (R) khớp storyboard và ghi chú.
> - Số trang 7+9+8+7+4+4+6 = 45 = 39+6; thời lượng 22+23+25+20+15+15 = 120 và R = 60 phút, đều khớp storyboard (dòng 166).
> - Câu nối giữa các mạch có ở ghi chú diễn giả từng trang khớp storyboard dòng 23–28 (A→B: slide A07/B01; B→C: B09; D→E: D07/E01; E→F: E03/F01; F→R: F04/R00).
> - Số liệu bảo toàn đúng: $\binom{10^6}{2}=499\,999\,500\,000$; kỳ vọng $249\,749{,}99975025 \to 249\,750$ (không nối dấu "=" với 250 000); các đáp số R02(a,b), R03, R05 được suy trực tiếp từ công thức, không thấy lỗi tính.
>
> **Nhỏ (không chặn):**
> 1. HTML dòng 262 ghi "Mục 1.2 · Bài 1.2.1 và 1.2.2", ghi chú dòng 397 ghi "mục 1.2.4, trang 8" — hai nhãn mục nguồn không đồng nhất; đề xuất thống nhất (ví dụ "MMDS mục 1.2.4").
> 2. HTML dòng 70 "Stanford03-lsh" thiếu khoảng cách (nơi khác viết "Stanford CS246 03-lsh"); lỗi trình bày.
> 3. Ghi chú dòng 397 nói "Gợi ý và lời giải có thể mở riêng" nhưng hiện tại gợi ý/lời giải nằm ngay trong tệp (::: hint, ::: solution) — nên sửa thành "có sẵn dưới dạng gợi ý/lời giải ẩn" hoặc bỏ câu.
>
> **Không phát hiện lỗi chặn bàn giao hay nghiêm trọng.** Các nguồn (MMDS, CS246, DSC, BHK, BIODS, Nelson–Gailly) được truy nguyên nhất quán ở cả ghi chú diễn giả và ghi chú bài giảng; các số minh họa (20 khối, 4 bản ghi) được ghi rõ là kịch bản giảng dạy, không gán cho nguồn — đúng nguyên tắc no-ai-slop.


### Quyết định sau phản biện

- Chấp nhận yêu cầu giảng dạy về mục tiêu riêng Bài 01: D01 và ghi chú thêm ba sản phẩm với tiêu chí đúng tập khóa/tổng/cận; đầu ra/giới hạn/bảo đảm; đơn vị đếm/giả thiết/giới hạn suy luận. Kiểm qua C06, C08, F04, R01–R05, không tuyên bố recitation đo đủ mọi mục tiêu của cả học phần.
- Chấp nhận sửa dấu cách ở aside, alt bản đồ; thêm bước 0 của vết để đối chiếu ghi chú; làm rõ câu tự chẩn đoán E01; thêm số bản ghi của student/takes lên B09. Mục 1.2.4 là đúng theo sách, nên giữ và thống nhất R00, không thay bằng số bài tập.
- Chấp nhận làm rõ khách sạn có thể khác giữa các ngày trong đề 1.2.1(c). Không chấp nhận công thức phụ do reviewer algorithms tự nêu về “cùng một khách sạn cả ba ngày”; không dùng nó vào bài. Lời giải chính giữ đúng $(q^2/H)^3$ và $\binom T3$.
- Bác cảnh báo của reviewer student về thiếu dấu thập phân: bản thật đã viết $249\,749{,}99975025$, reviewer math xác nhận đúng. Không sửa công thức đang đúng.
- A01 đã có tên bài trên dòng nhận diện, phù hợp quyết định mở thẳng ứng dụng. F04 chốt dùng lại V01. Gợi ý/lời giải Markdown được viewer chuyển thành khối gập; “mở riêng” không phải liên kết sang tệp khác.
- Bổ sung giả thuyết làm việc của bài 1.2.2 ngay trên R04; aside giữ diễn giải và chú thích 3. Kỳ vọng nền không xác định xác suất danh tính khi đã quan sát trùng.
- Bố cục hình ứng dụng đổi thành hình trên và ba thẻ dưới để giữ chữ; D02 dùng giới hạn chiều cao riêng, các hình lưu trú/giỏ hàng giảm khoảng trống dọc để nhãn lớn hơn. Không đổi quan hệ, số liệu hoặc thêm kết quả thực nghiệm.
- Hai chủ đề cao chiều và cách nhìn mô hình chỉ còn chỉ dẫn đọc thêm. Không giữ nguyên các phát biểu thiếu giả thiết trong ghi chú cũ. Lập luận chỉ báo $\mathbf1_{\{Y\ge1\}}\le Y$ giữ lại để giải thích cận xác suất, không thêm chủ đề ngoài bài.

### Lượt sửa riêng

Writer sửa phiên 88945 dừng với lỗi nguyên văn: `model exceeded the tool-call limit (10)`. Chưa áp bản sửa nào; điều phối thông báo và thu hẹp nhiệm vụ, không đổi provider/model.

Writer chạy lại phiên 21321 hoàn tất, requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Chấp nhận bố cục hai mức mục tiêu và ba sản phẩm. Điều phối biên tập trước áp dụng: không gọi tổng byte là “bài toán đếm”, dùng “tính kỳ vọng” thay “phát biểu kỳ vọng”, bỏ mã trang mà writer vẫn để trong aside, rút chữ để tránh quá tải. Các sửa định nghĩa/công thức không phát sinh; chỉ làm rõ diễn đạt đề ba ngày và tiêu chí mục tiêu. Reviewer giảng dạy/mạch viết rà lại phần thay đổi sau áp dụng.

### Giới hạn Codex Slides

Đọc trạng thái bền vững của dự án `20260827112432-b-i-1-b-i-to-n-d-li-u-l-n-v-m-h-nh-thu-t-8tlj`: vẫn là draft/clarify, 0 trang. Đã mở đúng dự án bằng liên kết trả về; phiên công cụ không có Browser trong trình soạn thảo để điều khiển trực quan. Không tạo một deck raster khác hoặc tuyên bố dự án đó khớp HTML. Theo quy tắc dự phòng của kho, đầu ra chính được kiểm trực tiếp bằng Chromium trên RevealJS/viewer tại cổng 8765. Skill xử lý lỗi Codex Slides được dùng để phân loại trạng thái cũ và giữ đúng project id; không khởi tạo lại dự án.

### Kiểm định kỹ thuật đang tổng hợp

Lượt đầu chờ networkidle bị timeout vì reloadserver duy trì kết nối theo dõi; đổi sang tín hiệu Reveal sẵn sàng, ảnh tải xong và phông chữ sẵn sàng. Lượt sau dùng sai selector h1 trong thân viewer; viewer hợp lệ chuyển h1 sang thanh tiêu đề, nên kiểm theo h2 và material-title. Đây là lỗi kịch bản kiểm thử, không sửa viewer để phù hợp một giả định kiểm thử sai. Rà ảnh phát hiện D02 quá cao do độ ưu tiên CSS; tăng độ ưu tiên selector của hình và giới hạn riêng bản đồ rồi chạy lại tất cả trang.

### Kết quả kiểm định cuối

Reviewer rà lại phiên 83779 bị lỗi `OpenRouter request exceeded 120s wall timeout`. Điều phối báo lỗi và chạy lại cùng vai trò trên ba đoạn ngắn, không chuyển model/provider. Phiên 61748 hoàn tất với requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter: xác nhận D01 và ghi chú đã có ba sản phẩm đo được, không còn lỗi bắt buộc về mục tiêu/mạch viết. Đoạn đọc cuối của reviewer là R05, không phải toàn R04; điều phối kiểm trực tiếp mặt R04 và aside để xác nhận giả thuyết nguồn đã hiển thị đủ.

| Kiểm tra | Bằng chứng và kết quả |
|---|---|
| Cấu trúc | 45 mã duy nhất, đúng thứ tự storyboard; 7 phần ngoài; 45 aside; 39 trang giảng và 6 trang bài tập |
| Thời lượng thiết kế | A22+B23+C25+D20+E15+F15=120; R01–R05=10+15+10+10+15=60 phút; chưa tuyên bố đây là thời gian diễn tập thực tế |
| Nội dung và số học | Năm vai phản biện độc lập cùng lượt storyboard; quét, tập khóa0, dãy rỗng, điều kiện kỳ vọng và toàn bộ phép tính tổ hợp đã kiểm; lỗi nghiêm trọng về mục tiêu đã sửa và rà lại |
| RevealJS | Đúng1280×720, edges, slideNumber/hashOneBasedIndex/hash; từng trang ở1280×720 và390×844 đều nằm trong khung; điều phối xem ảnh tổng hợp cả45trang và ảnh chi tiết các trang đổi hoặc có cảnh báo |
| Công thức/tài nguyên | Không lỗi KaTeX ở slide hoặc ghi chú; không ảnh hỏng, không lỗi trang hay phản hồiHTTP≥400; không yêu cầu mạng ngoài cho tải nội dung cốt lõi |
| Cảnh báo hình học | Bộ dò scrollHeight báo B09/C03/F03 do hộp chữ KaTeX cao hơn dòng văn bản; ảnh chi tiết cho thấy toàn công thức nằm trong thẻ và khung, không bị cắt. Không thu nhỏ công thức để làm mất cảnh báo giả |
| Hình | 19 SVG đang dùng có role và title/desc, alt cụ thể; XML hợp lệ; mọi nhãn nằm trong viewBox; các mũi tên/quan hệ đối chiếu lại nguồn; không raster |
| Viewer | 19hình, 41mục lục; công thức và bảng hiển thị; không tràn ngang toàn trang ở1280/390px; hình lớn cuộn ngang đúng thiết kế hiện có |
| Bàn phím | Mũi tên xuống A01→A02, phải→B01; Enter mở gợi ý; vùng hình hẹp nhận focus và ArrowRight làm scrollLeft tăng40px |
| Liên kết/an toàn | Từ index mở đúng note; từ viewer quay lại đúng deck; đường dẫn ngoài mẫu và doc/deck khác số bị từ chối. Thử trong bộ nhớ: script và liên kết javascript bị loại, không chạy mã |
| In slide | PDF đúng45trang; sửa viền phần recitation gây lệch6px và một trang trắng. Chỉ thay quy tắc print của HTML bài này |
| In ghi chú | PDF A4 có25trang, cả4khối gợi ý/lời giải mở khi in; bảng danh mục tiếp trang có tiêu đề. Sửa min-width hình900px chỉ khi in SVG lec-01; kiểm cả19hình không vượt cha và xem lại trang in có hình/công thức/bảng |
| Chỉ mục | Mô tả Bài01 theo tuyến mới; bản đồ chung và liên kết hoạt động ở rộng/hẹp; không đưa liên kết kế hoạch ra công khai |
| Sao lưu | 9tệp sản phẩm/giao diện sao lưu khớp từng byte với HEAD trước sửa; 3tệp kế hoạch lưu trạng thái đã replanning ngay trước triển khai, không so nhầm với HEAD cũ |
| Biên tập | Tự kiểm no-ai-slop/eval.md đạt: giữ dữ kiện/giả thiết, không thêm ví dụ hoặc số đo, cắt lời dẫn rỗng/mã nội bộ, tiêu đề Việt, câu tương tác có nhãn; quill xác nhận thứ tự/thuật ngữ/ký hiệu và tác động chỉ trong Bài01 |
| Git | Kiểm diff/whitespace và phạm vi tệp trước commit; chỉ đưa sản phẩm, kế hoạch, sao lưu và sửa in riêng lec-01 vào commit. Không đưa AGENTS.md, .gitignore, .codex hay openrouter-mcp của người dùng vào commit |

Các ảnh/PDF và kịch bản kiểm tra tạo trong thư mục tạm của phiên, không thêm tệp nhị phân vào Git. Ngoại lệ còn lại duy nhất về công cụ là Codex Slides không có bản dựng tương ứng và Browser trong trình soạn thảo không khả dụng; bản RevealJS đã được kiểm trực quan bằng Chromium cục bộ. Không còn lỗi chặn bàn giao hoặc nghiêm trọng ở sản phẩm.

### Trạng thái bàn giao

Slide, ghi chú, 19 hình, chỉ mục và ba tệp quy trình đã đồng bộ theo kế hoạch. Cần đọc học liệu từ MMDS, Stanford, BHK, Nelson–Gailly và DSC theo ánh xạ nguồn; không phát sinh nội dung thuật toán chuyên biệt ngoài phạm vi. Phiên bản được nhận diện bằng commit của lần triển khai này và lịch sử Git; push lên origin/main là bước xuất bản cuối theo quyền người dùng đã cấp.

## Lần sửa mở bài và kết nối — 2026-09-06

### Yêu cầu và phạm vi đã duyệt

Người dùng yêu cầu lập kế hoạch, bổ sung trang mở bài và trang kết nối vì các ví dụ xuất hiện đột ngột; sau đó dùng no-ai-slop để loại bỏ chỉ dẫn dành cho người viết. Phiên bản trước nằm trong commit `0c810116ea55894ab4b9d210b6316dd53fb70e4b`; giữ nguyên các bản sao lưu đã có. Lần này sửa HTML, ghi chú, chỉ mục và ba tệp quy trình; không đổi CSS, thuật toán, bài tập hay 19 SVG.

- Thêm P00/P01 để giới thiệu học phần, tình huống nhật ký vượt bộ nhớ, hành trình và sản phẩm học tập của buổi.
- Thêm A08/A09 nối tổng hợp → xếp hạng → tìm tương đồng; B00/B10/B11 nối kho tìm kiếm → dòng truy vấn → khôi phục dữ liệu → truy cập khối; D00 nối yêu cầu tài nguyên với nhóm phương pháp.
- C01/C02 thu hồi các ứng dụng về lời giải tổng byte; D01 chỉ giữ năng lực toàn học phần, tránh lặp mục tiêu P01.
- Đặt E04 sau F04: kết thúc phần giảng bằng chuẩn bị MapReduce, rồi R00 chuyển rõ sang bài tập về mô hình ngẫu nhiên. Không đặt chuẩn bị bài sau vào cuối phần tiên quyết khi lập luận của buổi chưa kết thúc.
- Giữ 7 phần ngoài, 53 trang gồm 47 trang giảng và 6 trang bài tập. Thời lượng thiết kế A25+B26+C25+D18+E9+F17=120 phút; R01–R05=10+15+10+10+15=60 phút. Mã trang cũ ổn định; thứ tự thực nằm trong bảng storyboard.

### Điều phối và bằng chứng runtime

Các lượt hoàn tất dưới đây đều có metadata runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Reader/reviewer chỉ đọc; writer chỉ được ghi thư mục tạm, điều phối kiểm và áp dụng vào kho. Không cấp `.env` cho công cụ worker, không đổi mô hình khi lỗi.

| Vai trò | Phiên và kết quả | Quyết định |
|---|---|---|
| Lập kế hoạch | 49196 hoàn tất | Nhận chẩn đoán thiếu mở bài và chuyển ý hiển thị; bác phương án cộng thời lượng thành 123 phút, nhãn sản xuất và tiêu đề hỏi tu từ; duyệt cấu trúc 8 trang thêm trong outline trước soạn |
| Phân tích nguồn | 35130 lỗi `model exceeded the tool-call limit (4)`; 59769 đọc hồ sơ giới hạn và hoàn tất | Giữ các nguồn hiện có; không xóa giới hạn toán học, liên hệ Bài 02–15 hay xuất xứ tình huống 20 khối vì chúng không phải chỉ dẫn cho người soạn |
| Soạn | 38545 lỗi `model exceeded the tool-call limit (5)`; 6493 hoàn tất trong thư mục tạm | Kiểm và sửa tên học phần/học kỳ, diễn đạt kho nhật ký vượt bộ nhớ, nguồn I/O; bỏ “chào lớp”, lời chỉ đạo nối trang và kết luận mọi thuật toán đều phải xét mọi cặp |
| Rà storyboard | 57381 hoàn tất | Đồng bộ toàn bộ tiêu đề bảng với HTML, gồm R04 “Trùng tập mặt hàng”; cập nhật ánh xạ N05 thành D00–D07 |
| Mạch viết | 56218 hoàn tất | Xác nhận đủ mở–nối–kết và vị trí E04 trước recitation; số trang/thời lượng được kiểm thêm bằng mã, không dựa vào các số đếm nhầm trong văn bản phản biện |
| Giải thuật | 92472 hoàn tất | Làm rõ thao tác Bloom, nhãn cận truyền, độc lập người/ngày và hai yêu cầu tự kiểm E01; giữ nguyên công thức và điều kiện đúng |
| Toán học | 52985 lỗi `model returned an empty or incomplete answer after all retries`; 11046 hoàn tất trên trích đoạn toán đầy đủ | Tự tính lại mọi đáp số; bác đề nghị sửa sai giá trị phần (a) và cảnh báo dấu thập phân không có thật |
| Giảng dạy | 29147 cùng lỗi câu trả lời rỗng; 40104 hoàn tất trên đủ 53 trang và notes | Giữ E04 ở cuối 120 phút giảng, không chuyển ra sau 60 phút recitation; không thêm nhãn nội bộ lên mặt trang; không gọi số đã làm tròn là “chính xác” |
| Góc nhìn sinh viên | 55714 cùng lỗi câu trả lời rỗng; 12942 hoàn tất trên đủ 53 trang và notes | Ghi nhận mở bài và các cầu nối rõ; kiểm trực tiếp mục tiêu P01 và đáp án F04/E04 đã đo được. Không thêm chỉ dẫn “Người soạn rà lại” vào notes. Không gắn nhãn tiên quyết dày đặc vào các ví dụ giới thiệu |
| Sửa riêng sau năm phản biện | 71562 hoàn tất | Soạn bốn đoạn ngắn trong `final-copy.md`; áp dụng sau kiểm, bỏ câu giải thích cận dưới lặp, giữ công thức bằng KaTeX và nhãn “Câu hỏi:” |

Mỗi lỗi worker đã được thông báo trước khi chạy lại với đầu vào giới hạn hơn; không âm thầm chuyển sang tác tử mặc định. Một số phản biện có nhận xét tự mâu thuẫn hoặc vượt yêu cầu; chúng là đề xuất, không phải bằng chứng thay cho nguồn và kiểm tra trực tiếp.

### Quyết định nội dung và kiểm toán số học

- Bloom: dùng “chuẩn, với thao tác chèn và tra cứu, không xóa”; giữ điều kiện băm và trạng thái đúng cho bảo đảm không bỏ phần tử đã chèn. Không tiếp nhận câu khái quát vô điều kiện về sai số từ reviewer.
- Chi phí: phân biệt số phép tính kỳ vọng $O(n)$ với cận thời gian truyền $T_{\rm quét}\ge D/v$. Hai đại lượng không mâu thuẫn; nhãn mới làm rõ mô hình, không sửa một cận đang đúng.
- Lưu trú: viết rõ lựa chọn độc lập giữa mọi người và mọi ngày; giữ chọn đều khách sạn có điều kiện đã đi. Tính tuyến tính kỳ vọng không đòi các phép thử cặp người–cặp ngày độc lập nhau.
- Kiểm lại bằng phân số chính xác: $\binom{10^9}{2}=499999999500000000$, $\binom{2000}{2}=1999000$. Phần 1.2.1(a) bằng $999499{,}9990005$, không phải $999499{,}9995$ như reviewer đề xuất. Các giá trị còn lại: $249749{,}99975025$ (mô hình gốc), $249749{,}999875125$ (b), $0{,}0830834999169165$ (c); giỏ hàng xấp xỉ $0{,}00018981846904990663$. Không đổi công thức hoặc đáp số đã đúng.
- Tự kiểm mục tiêu: P01 có đặc tả/bất biến, giới hạn/bảo đảm và kỳ vọng/giới hạn suy luận; các câu hỏi C06, C08, F04 và lời giải notes cho tiêu chí đối chiếu. Không thêm một trang đánh giá mới chỉ vì reviewer bỏ qua đáp án trong notes.
- Nguồn lưu trữ thứ cấp sửa từ mục 1.3.3 thành MMDS mục 1.3.4, trang 13. Bài tập giữ sách MMDS ấn bản 3 và số bài/mục/trang đã truy nguyên. Lần mở website MMDS gặp HTTP 502; không dùng dữ kiện web mới thay nguồn cục bộ.

### Biên tập no-ai-slop và rà mạch bằng quill

Đã tự kiểm trực tiếp theo `no-ai-slop/eval.md`: 11 nguyên tắc biên tập, nhóm từ cần cắt, 9 nhóm mẫu câu và các mục đọc cuối áp dụng đều đạt. Giữ giọng học thuật tiếng Việt và từ chuyên môn; không thêm số liệu, bằng chứng hay ví dụ. Cắt lời chỉ đạo sản xuất, nhãn “bản trước”, lời dẫn rỗng và câu tổng kết lặp khỏi mặt trang, ghi chú diễn giả và tài liệu tự học. Không đánh đồng giả thiết phủ định, lời giải chấm bài hay hướng dẫn học tập với chỉ dẫn cho người viết. Bản đầy đủ là HTML và Markdown của bài, không tạo bản rút gọn thay tài liệu.

Quill được dùng để đối chiếu dàn ý, thứ tự và thuật ngữ giữa slide/notes: ứng dụng → một lời giải có tính đúng và chi phí → bản đồ học phần → nền học tập → giới hạn suy luận. Mỗi cầu nối có đầu vào và đầu ra trong storyboard; ghi chú tự học thêm đoạn chuyển tương ứng, chuyển phần chuẩn bị MapReduce về cuối phần giảng. Không tạo `quill.json` hoặc dự án sách.

### Giới hạn công cụ

Dự án Codex Slides cũ vẫn ở draft/clarify, 0 trang; không có Browser trong trình soạn thảo để kiểm bản HTML trên bề mặt đó. Theo đường dự phòng của kho, dùng Chromium cục bộ trên chính RevealJS và viewer; không tạo deck raster thay thế, không tuyên bố trạng thái Codex Slides đã đồng bộ. Kho giao diện tham khảo machine-learning không có ở vị trí cục bộ đã kiểm; tiếp tục dùng template và CSS hiện hành, không tự tạo hệ giao diện mới.

### Rà lại và kiểm định bản cuối

Reviewer mạch viết phiên 85273 hoàn tất, metadata runtime vẫn đúng model/provider nêu trên. Đọc toàn bộ bản trích 53 trang và notes; xác nhận thứ tự mở bài đến chuẩn bị MapReduce, bốn diễn đạt đã sửa và không còn chỉ dẫn người soạn. Bác cảnh báo “thiếu recitation” của lượt này: bản trích đã có “Bài tập củng cố”; HTML thực có phần ngoài thứ bảy chứa R00–R05, và storyboard cộng đúng 60 phút. Không thêm từ tiếng Anh hay thời lượng lên mặt trang để chiều một cảnh báo dựa vào việc không thấy chữ “recitation”. Reviewer cũng trích nhầm bài tập cuối khi xác nhận E01; điều phối kiểm trực tiếp E01 và ảnh chụp, thấy đúng hai yêu cầu đã duyệt.

| Kiểm tra sau sửa cuối | Kết quả |
|---|---|
| Cấu trúc và kế hoạch | 53 mã duy nhất khớp thứ tự và tiêu đề storyboard; 7 phần ngoài, 53 aside; tổng 120+60 phút |
| Hiển thị từng trang | Kiểm cả 53 trang ở 1280×720 và 390×844; không vượt khung. Xem toàn bộ ảnh tổng hợp và ảnh chi tiết trang mở, trang sửa cuối |
| Công thức và tài nguyên | 0 lỗi KaTeX, 0 ảnh hỏng, 0 lỗi JavaScript, 0 phản hồi HTTP lỗi, 0 yêu cầu mạng ngoài cho nội dung cốt lõi |
| Cảnh báo hình học | B09/C03/F03 vẫn có cảnh báo scrollHeight của KaTeX nội dòng; ảnh xác nhận không cắt công thức, không thu nhỏ chữ để che cảnh báo |
| SVG | Giữ nguyên 19 SVG; kiểm XML, role và mô tả; không thêm raster hay tài sản trang trí |
| Bàn phím | Mũi tên xuống P00→P01, phải→B00; Enter mở gợi ý của viewer |
| Ghi chú | 19 hình, 42 mục lục; không tràn ngang toàn trang ở rộng/hẹp; bốn khối gợi ý/lời giải gập khi đọc và mở khi in |
| Liên kết/an toàn | Đúng liên kết note/deck; viewer từ chối đường dẫn ngoài mẫu và cặp doc/deck khác số bài; chỉ mục tải đúng ở rộng/hẹp |
| In | PDF slide 53 trang, ghi chú 25 trang A4; kiểm ảnh trang in, hình và công thức; không thêm PDF/ảnh kiểm thử vào Git |
| Biên tập | Tìm các mẫu chỉ dẫn sản xuất không còn kết quả trong HTML/Markdown; no-ai-slop giữ nguồn, giả thiết, lời giải và câu hỏi học tập; quill đối chiếu thứ tự phần và ký hiệu |
| Phạm vi Git | Sáu tệp thuộc Bài 01 và mục chỉ mục; không đưa AGENTS.md, .gitignore, .codex, codex-orchestrator hay openrouter-mcp của người dùng vào commit |

Thời lượng là thiết kế học liệu, chưa phải kết quả diễn tập trên lớp. Hạn chế công cụ Codex Slides đã nêu không được coi là đã kiểm trên Browser của ứng dụng; bản RevealJS được kiểm trực tiếp. Không còn lỗi chặn về nội dung hoặc hiển thị đã xác nhận. Bước xuất bản là commit và push thường lên origin/main theo quyền đã cấp, không ghi đè lịch sử.

### Đối chiếu hoàn tất mục tiêu

Commit `1c49e6276ef0335b3e93585fadc6e373dfe88184` chứa sáu tệp của lần sửa và đã được xác nhận trực tiếp trên `refs/heads/main` của origin bằng `git ls-remote`. Đối chiếu lại yêu cầu với hiện trạng: outline/storyboard có kế hoạch mở–nối; HTML triển khai đủ tám trang thêm và chuyển E04; ghi chú có các đoạn nối tương ứng; no-ai-slop đã cắt chỉ dẫn biên soạn, giữ nguồn và lời giải. Các thay đổi ngoài phạm vi của người dùng vẫn nguyên trạng.

Lượt đối chiếu phát hiện hai lỗi tài liệu kế hoạch: khi bỏ thẻ xuống dòng của tiêu đề P00 đã làm mất một khoảng trắng, và đoạn mô tả bố cục còn nêu phương án hình bên cạnh thẻ. Sửa thành tên bài có khoảng trắng và hình trên, ba thẻ dưới, đúng HTML đã kiểm trực quan. Đây là đồng bộ tài liệu, không thay đổi trang chiếu, ghi chú, nguồn, số liệu hoặc hình.

Chạy lại toàn bộ kiểm định Chromium sau đối chiếu: 53 trang, 7 phần, 53 notes, 120+60 phút; không lỗi công thức/tài nguyên/trang, không tràn khung ở rộng/hẹp; viewer có 19 hình và 42 mục lục, bàn phím và in đạt. Ba cảnh báo hình học KaTeX vẫn là các hộp nội dòng B09/C03/F03 đã kiểm bằng ảnh, không cắt nội dung. Kết quả khớp lần kiểm trước; bản HTML/Markdown không thay đổi sau commit nội dung.

## ER-001 — bài toán và hình trong section giới thiệu

### Yêu cầu, nguồn và phạm vi

Yêu cầu mới đã ghi nguyên văn trong edit_request.md: người mới chưa hiểu các ví dụ; cần bài toán, khó khăn do quy mô/triển khai và hình minh họa. Sửa P00/P01/A01–A07, bảy SVG và phần đầu ghi chú; bỏ A08/A09; đồng bộ outline, storyboard, index. Giữ B–R, số liệu và bài tập. Bản đích có 51 trang, bảy phần, 120+60 phút; A giữ 25 phút.

Điều phối đọc bản đồ nguồn, ánh xạ slide và các phần nguồn liên quan. Ưu tiên MMDS cho các cụm tương đương Stanford. A01 dùng Stanford intro62 vì nêu đúng URL/size/host; MMDS1.3.4 tr13 cho giới hạn bộ nhớ. A02 dùng MMDS Ch2 slide8–13,20 và sách2.1–2.2.6. A03 giữ đồ thị y,a,m của Link Analysis1 và MMDS5.1–5.2. A04 giữ bốn nghĩa jaguar và vấn đề bộ điểm riêng từng người ở MMDS5.3.1 tr195–196. A05 giữ ba nhóm/cạnh Hình5.16 và giả thiết tập tin cậy ở5.4.4. A06 dùng MMDS3.1–3.4; Stanford03-lsh14 cho quy mô số cặp. A07 đối chiếu BIODS271 PDF16 (các đoạn tài liệu và truy vấn dùng cùng phép mã hóa), 17–18 (10 tỷ véc-tơ, 3072 chiều, 32 bit mỗi thành phần), cùng Princeton08:2–5. Không đưa nội dung mô hình mã hóa vào học phần, không thêm số đo hoặc ví dụ số mới.

### Điều phối và bằng chứng runtime

Tất cả lượt hoàn tất dưới đây có `requested_model` và `observed_model` cùng bằng `z-ai/glm-5.3-flash`, `provider` là `OpenRouter`, lấy từ kết quả JSON của cầu nối. Không dùng lời tự khai của worker làm bằng chứng. Các worker chỉ đọc nhận hồ sơ/bản trích; điều phối trực tiếp kiểm PDF và ảnh trình duyệt. Writer chỉ ghi thư mục tạm `/tmp/er001.vCaHMQ`, sau đó điều phối kiểm và áp dụng bằng patch.

| Vai trò | Phiên | Kết quả và quyết định |
|---|---|---|
| Lập kế hoạch | 41911 | Duyệt bỏ A08/A09 và nêu rõ bảy nhiệm vụ; bác giữ bắt buộc ba thẻ ngắn và ghi phút trong notes; tự phân bổ lại 25 phút |
| Phân tích nguồn độc lập | 54450 | Bảy cụm đủ nguồn ở mức khảo sát; giữ các điều kiện D/M, đếm lần xuất hiện, đồ thị, chủ đề đã biết, tập tin cậy, số cặp và khoảng cách |
| Soạn phạm vi nhỏ | 16127 | Nháp A02 HTML/SVG. Giữ ý gom dữ liệu gây nút thắt; sửa nhãn quá dài/chồng nhau, bỏ figcaption lặp và câu nối sai nghĩa “đếm từ dẫn tới sắp kết quả” |
| Storyboard | 47804 | Đếm đúng51/120+60; phát hiện còn A08/A09 ở tiêu chí cầu nối cuối tệp; đã sửa thành sáu trang mở/nối |
| Góc nhìn sinh viên | 99739 | Không lỗi dữ kiện; đề xuất giải thích khuyên/t và bộ điểm. Đổi alt sang liên kết về chính nó; t đã có nhãn Trang đích trong SVG; không thêm tên thuật toán lên mặt trang |
| Giải thuật và dữ liệu | 83257 | Sửa câu chạy lại tác vụ tránh đếm trùng và alt A03; không thêm trường ngày vào bảng vì không dùng trong phép cộng; giữ 10 tỷ phép tính khoảng cách với giải thích mỗi phép dùng nhiều thành phần trong notes |
| Toán học và thuật toán | 39083 | Tự tính55/25/0,499999500000,10tỷ khoảng cách; D/M,k/hòa,chiều và cạnh đúng. Áp dụng “từ bốn bản ghi”, “giữa các trang” và alt A06 đủ mạng cặp |
| Phản biện giảng dạy | 36956 | Lo thiếu bối cảnh A07 được xử lý bằng truy hồi đoạn tài liệu từ nguồn16. Bác đề xuất ghi “bảy slide khảo sát” trên P01 và bỏ chi phí lặp A03: P01 đã nêu khảo sát, còn khó khăn là yêu cầu trực tiếp của người dùng. Không chuyển nhận xét “Cao” ngoài thang chuẩn thành lỗi bắt buộc thiếu bằng chứng |
| Kết nối toàn bài | 93847 | Đọc đủ51slide; không lỗi bắt buộc. A07→B00/B01 và E04→R00 nối được; A01 dùng lại ở C02–C06; giữ các phần sau |
| Chỉnh sửa độc lập sau năm báo cáo | 78857 | Soạn A07 cụ thể hóa đoạn tài liệu. Chấp nhận tác vụ/câu điều kiện; không áp dụng HTML bọc/CSS mới, mã B00 trong notes, figcaption lặp hoặc chữ32bit thiếu “mỗi thành phần”; dùng giao diện hiện tại |

Một writer nháp của phạm vi trao đổi trước đó, phiên83971, kết thúc với lỗi `OpenRouter request exceeded 300s wall timeout`. Đã báo người dùng; không áp dụng nháp lỗi. Lượt16127 chạy lại cùng mô hình/provider với phạm vi nhỏ hơn và hoàn tất. Không đổi ngầm nhà cung cấp.

### Biên tập và hình

P00 chỉ giữ nhận diện học phần; P01 nói năng lực và nội dung khái quát. Bảy ví dụ có câu nêu nhiệm vụ, hình cụ thể và khó khăn. A01 đưa bảng bốn bản ghi lên mặt trang, hình bộ nhớ lớn hơn bản nháp, chuyển D/M về notes. A02 giới thiệu từ w ngay trong câu bài toán. A03 giữ điểm quan trọng như tín hiệu hỗ trợ, không đồng nhất với độ liên quan. A04 giữ chủ đề như đầu vào đã biết. A05 khoanh cụm cùng kiểm soát. A06 vẽ phần chung/phần thay đổi và sáu cặp giữa bốn tài liệu; không vẽ chữ ký chưa định nghĩa. A07 biểu diễn truy vấn/đoạn tài liệu cùng dạng véc-tơ; không gán khoảng cách hoặc thứ hạng giả.

Quill rà trật tự nhiệm vụ→đầu ra→khó khăn và các chỗ dùng lại ví dụ; không tạo quill.json. No-ai-slop biên tập mặt trang, alt, notes và phần ghi chú bị tác động; điều phối tự kiểm trực tiếp theo eval.md: các nguyên tắc giữ ý/giọng, cắt từ rỗng, mẫu câu máy móc và đọc cuối áp dụng đều đạt. Giữ giả thiết phủ định, nguồn, câu hỏi học tập và lời giải; bỏ lời dẫn thiếu ngữ cảnh, nhãn mơ hồ và chỉ dẫn sản xuất. Bản đầy đủ nằm trong HTML/Markdown, không tạo bản rút gọn thay thế.

### Giới hạn công cụ và kiểm định

Codex Slides get_project vẫn trả draft/clarify,0slides cho dự án cũ; không có Browser nội bộ để xác minh bản RevealJS hiện tại. Tiếp tục đường dự phòng được kho cho phép: Chromium trên máy chủ8765 đang chạy; không tạo deck raster thay thế, không tuyên bố đã đồng bộ Codex Slides.

Kiểm thử tạm dùng `/tmp/er001.vCaHMQ/verify.py`; ảnh/PDF không đưa vào Git. Lượt chẩn đoán so HTML từ HTTP với Git báo khác vì máy chủ chèn mã tải lại; đã đổi sang so hai bản nguồn trong kho, xác nhận phần từ B00 đến cuối tệp không đổi từng byte. Kiểm nhãn SVG bằng getBBox cho bảy hình không thấy vượt khung hoặc chồng chữ. Các cảnh báo scrollHeight ở A06/B09/C03/F03 là hộp KaTeX nội dòng; ảnh cho thấy công thức không bị cắt, không thu nhỏ chữ để giấu cảnh báo.

### Rà lại và kết quả cuối ER-001

Reviewer mạch phiên49476 đọc đủ51slide sau sửa A07, xác nhận bảy mạch, bốn bản ghi được dùng lại ở C02–C06 và các ranh giới A07→B00/B01, F04→E04→R00. Đồng ý không thêm chỉ dẫn sản xuất lên P01 và không bỏ khó khăn lặp ở A03. Đề xuất ghi lý do mã B10/B11 không tăng đều đã được đáp ứng trong outline: mã ổn định để truy nguyên, thứ tự theo storyboard. Reviewer toán phiên60870 xác nhận lại điều kiện A07, số liệu và nguồn. Câu báo cáo nói A03 “không còn trở ngại lặp” không đúng bản thật; điều phối bác câu này, giữ khó khăn đọc/cập nhật nhiều vòng như đã duyệt. Cả hai lượt có requested_model=observed_model=z-ai/glm-5.3-flash, provider=OpenRouter. Không còn lỗi chặn hoặc nghiêm trọng đã được xác minh.

| Kiểm tra bản cuối | Kết quả |
|---|---|
| Cấu trúc/kế hoạch | 51 mã duy nhất khớp thứ tự storyboard;7phần;50notes vì trang tên bài không cần notes;120+60phút |
| Phạm vi | HTML từ B00 đến cuối không đổi từng byte;ghi chú từ phần dòng dữ liệu trở đi giữ nguyên, trừ dòng nguồn chung nếu cần |
| Hiển thị | Duyệt51slide ở1280×720 và390×844;không vượt khung;xem chín slide đầu và các trang lân cận/thu hồi ví dụ;A01/A07 xem lại ảnh chi tiết sau sửa cuối |
| SVG | Bảy hình được vẽ lại;XML/role/title/desc hợp lệ;nhãn không chồng/vượt viewBox;không thêm raster/CSS/thư viện |
| Công thức/tài nguyên | Không lỗi KaTeX/JavaScript/HTTP;không ảnh hỏng;không yêu cầu mạng ngoài cho thành phần cốt lõi |
| Bàn phím | P00↓P01,→B00;Enter mở gợi ý viewer |
| Ghi chú/index |19hình,42mục lục;không tràn ngang toàn trang ở rộng/hẹp;liên kết đúng;viewer từ chối doc ngoài mẫu/doc–deck khác số bài;index không lộ planning |
| In |51trang slide,27trang A4 ghi chú;bốn khối gợi ý/lời giải mở khi in;đã xem sáu trang đầu bản in ghi chú |
| Git |Chỉ đầu ra Bài01 vàedit_request.md;giữ thay đổi người dùng ởAGENTS.md,.gitignore,.codex,codex-orchestrator,openrouter-mcp |

Thời lượng là thiết kế học liệu, không phải số đo diễn tập. Nội dung đã xuất bản bằng commit `627d69ee9a214830ee81543faa170b1b50e7e532`, push thường lên origin/main; `git ls-remote` xác nhận đúng mã commit từ xa. ER-001 được tick sau xác nhận này. Bản cập nhật checklist/nhật ký không đổi học liệu đã kiểm định.

## Viết lại ghi chú theo chuẩn 2026-11 (đợt B1, giai đoạn 1 và 2, 2026-11-11)

Căn cứ: `prompt_fix_lecture_notes.md` (đợt B1); `AGENTS.md` §"Cấu trúc bắt buộc" mục 5, 6, 10; mục "The author's voice" của `../CLAUDE.md`. Điều phối viên: Claude Opus 5.5, effort high, không soạn hay rà. Quyết định của tác giả (2026-11-11): Bài 01 là bài giới thiệu, không thêm bài tập; giữ Bài tập 01.1–01.9 (ghi chú) và 01.10–01.11 (MMDS Bài 1.2.1, 1.2.2, §1.2.4, tr.8; `exercises.md`) và hoàn thiện. Giai đoạn 2 vì vậy chỉ còn rà và hoàn thiện, gộp vào lượt này.

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Lập kế hoạch chương | general-purpose | opus | high | không |
| Soạn, sau đó biên tập ba vòng (SendMessage) | general-purpose | opus | high | ghi chú, `exercises.md`, `img/lec-01/note-cau-truc-chuong-01.svg` và bộ sinh trong `tools/`, `outline.md`, `storyboard.md`, các dòng dẫn tới Bài 01 trong ghi chú Bài 08, 09 |
| Rà vai sinh viên năm hai | general-purpose | opus | high | không |
| Rà chuyên gia miền | general-purpose | opus | high | không |
| Rà độ chính xác (ba lượt) | general-purpose | opus | high | không |
| Rà sư phạm, `no-ai-slop` Detect | general-purpose | opus | high | không |
| Rà mạch và liên kết (ba lượt) | general-purpose | opus | high | không |

### Phát hiện và quyết định

| mức độ | vị trí | vấn đề | quyết định |
|---|---|---|---|
| nghiêm trọng | `exercises.md`, Bài tập 01.10(a) | "$3998/999$ … nhỏ hơn 4"; thực ra $999\cdot4=3996<3998$ | chấp nhận: $\approx4{,}002$, lớn hơn 4 |
| nghiêm trọng | Mục 3–4 | "bộ nhớ 20 khối (Mục 2.4)" không có trong Mục 2.4 | chấp nhận: đặt $M=20$ ở Mục 2.4 (DSC Ch.15, trang chiếu 40) |
| trung bình | toàn chương | thuật ngữ lệch các bài sau | chấp nhận: "lần truyền khối" (Bài 12, 15); "xác minh" (Bài 06); "dương giả/âm giả" (Bài 08), "ứng viên giả/cặp bỏ sót" (Bài 06); bảng thuật ngữ trong `outline.md` |
| trung bình | ký hiệu | $J$, $d$ hai nghĩa, $b$, $c$, $s$, $h$, $e$, $u$ | chấp nhận: $\mathrm{SIM}$; $D$ số chiều, $d(\cdot,\cdot)$ khoảng cách; $\tau=a/c$; $\lambda$ ngưỡng Markov; $\kappa$, $x_0$ trong ký hiệu $O$; câu đối chiếu với Bài 05–07 |
| trung bình | Tình huống 01.2 | "mọi thuật toán nối tốn ít nhất 500 lần" | chấp nhận: thu hẹp về trường hợp không có chỉ mục |
| trung bình | Mục 2.1, Nhận xét 01.6 | số liệu đĩa viết như sự thật chung | chấp nhận: "MMDS giả sử"; thêm số liệu đĩa từ/SSD và $b\,t_T+S\,t_S$ (DSC trang chiếu 8) |
| trung bình | Tình huống 01.3 | "tập khóa hợp lý" ngược MMDS §1.3.2 | chấp nhận: tập khóa hợp lý nhưng chung ước 2 với $B$ |
| trung bình | Tình huống 01.1 | khẳng định Mệnh đề trên chữ ký xấp xỉ | chấp nhận: giả thiết phép kiểm chính xác bị vi phạm, mất cả $\widehat R\subseteq R$ |
| trung bình | Bài tập 01.8, Ví dụ 01.11 | "ba đại lượng khác nhau" | chấp nhận: đếm lại đại lượng chính |
| trung bình | Mục 3.5 | thứ tự: độ thu hồi trước ứng viên | chấp nhận: đổi thứ tự, đổi số hiệu (bảng dưới) |
| trung bình | đọc hình, câu hỏi 1 và 4, câu mở Mục 2, 3, 4, Tóm tắt | đọc hình sai; câu hỏi chưa áp vào bài toán trung tâm; câu mở lặp cuối mục trước | chấp nhận |
| trung bình | toàn chương | khoảng 16 câu chỉ đường, 13 câu bình luận nguồn, câu gần đính chính sách, cảnh báo "sao chép" và MMDS Ví dụ 3.10 lặp | chấp nhận: cắt; phép tính giữ |
| trung bình | Ví dụ 01.7 | chạy tay $N=2$ quá ngắn | chấp nhận: $N=3$, $C_3=C_1$ |
| nhẹ | khoảng 40 mục của năm báo cáo | trang nguồn (DSC 8–9, CMU 13–14, 17, 19), BHK bản 04/01/2018, CS246 trang chiếu 67–69, Markov, $8{,}31\%$, Spam Mass, BIODS 271, … | chấp nhận |
| — | cắt thêm bảng Mục 3.2, 4.1, danh mục tham khảo để đạt mục tiêu cắt 1 800 | bác bỏ: độ dài 19 128 đã trong khoảng 12 000–32 000 |
| — | gộp công thức đã ngắt dòng | bác bỏ: tràn khung ở 390 px |
| — | đổi câu mở "Các giả thiết … có vai trò riêng" | bác bỏ: dạng chuẩn của `AGENTS.md` |
| — | đổi nhãn $S,T$ của `img/lec-01/danh-gia-jaccard.svg` | bác bỏ: hình dùng chung với deck; ghi chú nêu $S=C_1$, $T=C_2$ |
| — | đổi $t_T$, $t_S$ | bác bỏ: ký hiệu của DSC và Bài 15 |
| — | thêm bài tập mức nhận biết | hủy theo quyết định tác giả |

Đổi số hiệu (Mục 3.5): Định nghĩa 01.16 → 01.17 (độ thu hồi); Mệnh đề 01.17 → 01.16 (xác minh ứng viên); Ví dụ 01.9 ↔ 01.10. Không nơi nào ngoài ghi chú dẫn các số cũ.

Dẫn chéo: ghi chú Bài 08 (các câu dẫn Bài 01 ở phần tiên quyết, Mục 1, Mục 4, tham khảo) đổi tên mục cũ thành Mục 2.2, Mục 5, Ví dụ 01.4, Mệnh đề 01.20; câu "Ghi chú Bài 01 … chưa đánh số hiệu" ở Bài 08 và Bài 09 sửa phần nói về Bài 01.

Sai khác với deck (không sửa deck trong đợt này): deck còn $J$, nhãn $S,T$, "khối đọc ghi" (P04, B00, C09), "hậu kiểm" (D04, G01), "bỏ sót" (C16, GT), "lần kiểm" (C07, F04); ghi trong `outline.md`.

Nguồn đã đối chiếu: MMDS §1.2–1.3, tr.6–13; Ch.3 tr.73–75, 92; §4.2–4.3, §5.3.1; DSC Ch.15 trang chiếu 8–9, 19–22, 24–28, 40; CS246 trang chiếu 32–33, 62, 67–69; BHK tr.10, 13; BIODS L12 tr.16–18; CMU 15-499 compression3-lz trang chiếu 13–14, 17, 19.

### Kết quả kiểm tra

- Độ dài: ghi chú 12 212 (bản cũ) → 19 173; `exercises.md` 1 297.
- Khối: bộ đếm chung 01.1–01.23 liên tục; Ví dụ 01.1–01.14; Bài tập 01.1–01.11; Tình huống 01.1–01.3; 51 dẫn "X 01.k" trong ghi chú, `exercises.md`, Bài 08, Bài 09 trỏ tới khối có thật.
- Grep: 0 "chưa phải", "Bản đồ chủ đề", "Mục này", "do học phần", "hậu kiểm", "chuyển khối", "Đáp"; `git diff --check` sạch.
- Trình duyệt (`http.server`, Playwright Chromium): ghi chú và `exercises.md` ở 1600×900, 390×844: 0 lỗi console, 0 request hỏng, 0 `.katex-error`, trang không cuộn ngang (13 hình rộng nằm trong khung cuộn riêng, như Bài 10), khối gập mở khi in.

### Mục 5 chuyển thành phần Đọc thêm thu gọn (2026-11-11)

Phản hồi của tác giả: "bài ghi chú 01, mục 5 không phù hợp với nội dung cả bài lắm"; lựa chọn "thu gọn thành đọc thêm, collapse". Mục 5 đổi thành `## Đọc thêm: Mẫu trùng ngẫu nhiên và suy luận`, giữ vị trí, khối và số hiệu (01.18–01.23, Ví dụ 01.12–01.14, Bài tập 01.9); dòng `<!-- note-collapsed -->` trước tiêu đề làm viewer thu gọn mục (tính năng mới của `material-viewer.js`, mở khi in và khi bấm liên kết trong mục lục). Mạch chính còn ba câu hỏi, sơ đồ ba cột, mục tiêu 5 thành dòng "Phần đọc thêm"; Tóm tắt giữ một câu về $\mathbb E[X]$; "Bài tập củng cố" nêu 01.10–01.11 dùng phần đọc thêm; Mục 4.2 giữ ý "$\mathrm{SIM}\ge\tau$ chưa đủ căn cứ kết luận sao chép". Ghi chú Bài 08 (dẫn "Mục 5") đổi thành "phần đọc thêm *Mẫu trùng ngẫu nhiên và suy luận*".

| Tác tử | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Biên tập (hai lượt, SendMessage) | general-purpose | opus | high | ghi chú, `exercises.md`, SVG, `outline.md`, `storyboard.md` |
| Rà mạch và liên kết | general-purpose | opus | high | không |

Rà mạch: 3 trung bình (văn bản làm chủ ngữ ở dòng 3 và Tóm tắt; Bài tập củng cố không nêu phụ thuộc phần đọc thêm; sai khác với deck chưa ghi), 4 nhẹ: chấp nhận, trừ đổi tên mục "Hướng dẫn đọc thêm và tài liệu tham khảo" (bác bỏ: tiêu đề của mẫu). Sai khác với deck: deck giữ bốn câu ở P04/F04 và mạch 5 trong phần giảng; không sửa deck trong đợt này. Độ dài sau sửa: 19 073 âm tiết.


## Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): kiểm tra các deck 01–10 xem deck nào chưa tuân thủ các nguyên tắc của deck mới và chưa khớp với ghi chú bài giảng, ghi bảng phát hiện đầy đủ vào `review-log.md` của từng bài, thời điểm phát hiện là ngày 2026-11-13. Đợt này chỉ đọc: deck, ghi chú và `exercises.md` không đổi (HEAD `45ddcf9`; md5 deck `e7d4c423`, ghi chú `deadf0ea`, `exercises.md` `4bb70c95`, trùng nhau lúc bắt đầu và lúc kết thúc lượt rà).

**Căn cứ.** `AGENTS.md` dòng 1–190 và 381–650; `slide_authoring_standard.md`; `CLAUDE.md` của học phần ("Course-specific rules", "Writing", "Deck structure and content"); `../CLAUDE.md` ("Writing course content", "The author's voice", gồm các luật 2026-11-04 và 2026-11-09); quy ước tác giả 2026-10-28/29 (`planning/lec-08/review-log.md` mục "Trang bài toán đầu mạch", `planning/lec-08/danh-gia-giang-day.md` "Định hướng chung"); quy ước của deck làm lại từ ghi chú (Bài 09 ngày 2026-11-04, Bài 10 ngày 2026-11-08): deck là bản tóm lược của ghi chú, ký hiệu theo bảng ký hiệu của ghi chú, mục tiêu khớp ghi chú, trang bài toán có hình sau mỗi trang tiêu đề mạch, chứng minh tách trang, mỗi bài recitation có trang "Lời giải:", dẫn chiếu khối ghi chú và bài tập trỏ đúng khối hiện tại.

**Tác tử (theo lời gọi công cụ).** Vai trò: rà soát chỉ đọc (quy tắc deck mới và đối chiếu ghi chú), một tác tử riêng cho Bài 01; loại `general-purpose`, mô hình `opus` (Opus 5.5), effort `high`; `no-ai-slop` chế độ Detect. Không ghi tệp trong kho, không commit. Mười tác tử của mười bài chạy song song (đều chỉ đọc). Điều phối viên: phiên Opus 5.5.

**Quét cơ học của điều phối viên** (Playwright, 1600×900 và 390×844, máy chủ tĩnh cục bộ): 83 trang, 7 section ngoài; trang tiêu đề mạch `mach-2…7` mở đúng `#/2…7`; 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 `fragment`; mã nguồn không có `<style>`, `style=""`, `.dense`; dẫn chiếu `01.k` của deck so với khối hiện có của ghi chú và `exercises.md` (đều tồn tại; loại khối và nội dung do tác tử kiểm). Các cờ quét được tác tử kiểm lại; cờ giả ghi ở mục "Đã kiểm" bên dưới.

**Điều phối viên kiểm lại trên tệp gốc:** ghi chú có mục "Đọc thêm: Mẫu trùng ngẫu nhiên và suy luận" (note:956) nhưng deck không có nhãn "Đọc thêm" nào; Mệnh đề 01.16 (note:714) không có trên deck (không có $R\subseteq A$, $A\cap R$); "hậu kiểm" xuất hiện 6 lần trên deck, 0 lần trong ghi chú; tên tệp `ann-recall.svg` có trong ghi chú diễn giả. Đúng như báo cáo.

**Quyết định của điều phối viên:** **chấp nhận** báo cáo làm bảng phát hiện của bài. Mọi phát hiện ở trạng thái **mở**; deck chưa được sửa. Cột "phát hiện" ghi thời điểm phát hiện.

**Kết luận:** cần sửa — mạch 5 vẫn là mạch giảng chính trong khi ghi chú đã chuyển nó thành phần Đọc thêm; ba khối cốt lõi của ghi chú (Định nghĩa 01.1, Mục 2.1 với Mệnh đề 01.5, Mệnh đề 01.16) không có trang phục vụ; mục tiêu, vấn đề trung tâm, ký hiệu và thuật ngữ còn theo bản ghi chú cũ.

**Số phát hiện:** chặn bàn giao 0 · nghiêm trọng 4 · trung bình 13 · nhẹ 13.

Quy ước dẫn dòng: `html:` = tệp deck, `note:` = `lecture-note.md`, `ex:` = `exercises.md`, `sb:` = `planning/lec-01/storyboard.md`, `ol:` = `outline.md`, `rl:` = `review-log.md`, `er:` = `../edit_request.md`.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | phát hiện |
|---|---|---|---|---|---|
| nghiêm trọng | L01-P01, P03, P04, FT, F01, F02, F05, F06, F03, F07, G01, F04, G02 | **Lệch ghi chú + Quy tắc (nhãn Đọc thêm, AGENTS.md:399, 468):** mạch 5 "Mẫu trùng ngẫu nhiên và suy luận" được dạy như mạch chính (14 phút), là dòng 4 của vấn đề trung tâm, mục tiêu 5, một hàng của bảng tổng kết và câu 3 của tự kiểm tra, trong khi ghi chú đã chuyển phần này thành **Đọc thêm thu gọn** theo quyết định tác giả 2026-11-11. Không trang nào mang nhãn **Đọc thêm**. Quyết định cũ "không sửa deck trong đợt này" (sb:450, sb:460, ol:318, rl:1122) chỉ hoãn việc sửa, không phải ngoại lệ. Mạch 7 (60 phút) lại dựa hoàn toàn trên mô hình này (ex:3, ex:13), nên thực hành phụ thuộc phần tùy chọn, trái AGENTS.md:468. | note:16 "Phần đọc thêm: tính kỳ vọng…"; note:955–956 `<!-- note-collapsed -->` "## Đọc thêm: Mẫu trùng ngẫu nhiên và suy luận"; rl:1135 "mục 5 không phù hợp với nội dung cả bài lắm… thu gọn thành đọc thêm"; html:42 mục tiêu 5 "Tính kỳ vọng số trùng ngẫu nhiên…"; html:59 "Lưu trú độc lập: kỳ vọng khoảng $249\,750$…"; html:656; html:646 hàng "Kỳ vọng trùng nền"; html:666 câu 3; html:48 mục 5 của Nội dung không có nhãn. | Cần tác giả xác nhận phương án. Đề xuất: (1) gắn nhãn **Đọc thêm** (lớp CSS loại phần của học phần) trên FT–F07 và mục 5 trang Nội dung; (2) P03 bỏ mục tiêu 5, thêm dòng "Đọc thêm: tính kỳ vọng số biến cố trùng ngẫu nhiên; chặn $\Pr(X\ge1)$ bằng bất đẳng thức Markov." như note:16; (3) P04/F04 còn ba dòng theo ba câu hỏi của note:85–89; (4) G01 ghi "(đọc thêm)" ở hàng kỳ vọng; G02 câu 3 thay bằng Bài tập 01.7 (bộ lọc và xác minh chính xác, note:812–828); (5) mở mạch 7 bằng một trang "Nhắc lại:" đủ để làm bài: mô hình $P,T,H,q$, $p=q^2/H$, $\mathbb E[X]=\binom P2\binom T2p^2$, Hệ quả 01.22 $\Pr(X\ge1)\le\mathbb E[X]$. | 2026-11-13 |
| nghiêm trọng | L01-C16 (thiếu trang trước C16) | **Lệch ghi chú (nội dung cốt lõi không có trang):** Mệnh đề 01.16 (xác minh ứng viên) với chứng minh, Ví dụ 01.9 và định nghĩa dương giả/âm giả là nửa sau của mục tiêu 3 của ghi chú, nhưng deck chỉ có một câu hỏi; không trang nào phát biểu $\widehat R=A\cap R$, $\widehat R\subseteq R$, $\widehat R=R\iff R\subseteq A$. | note:13 "chứng minh bước xác minh tập ứng viên $A$ trả đúng $R$ khi và chỉ khi $R\subseteq A$"; note:714–736; note:738–746 Ví dụ 01.9; note:748 FP/FN; html:416–418 C16 chỉ có định nghĩa cặp ứng viên bằng lời và "Câu hỏi: xác định hậu kiểm từng ứng viên có đủ bảo đảm…". | Thêm trang "Xác minh ứng viên": **Mệnh đề.** (a) $\widehat R=A\cap R$; (b) $\widehat R\subseteq R$; (c) $\widehat R=R\iff R\subseteq A$ (Mệnh đề 01.16), một dòng "Chứng minh." theo note:729–735. Thêm trang "Ví dụ: một cặp sai bị loại, một cặp đúng bị bỏ sót": $N=3$, $R=\{(1,2),(2,3)\}$, $A=\{(1,2),(1,3)\}$, "Tính $\widehat R$", kết quả $\{(1,2)\}$, độ thu hồi $1/2$; nêu dương giả (false positive, FP) = ứng viên giả $(1,3)$, âm giả (false negative, FN) = cặp bỏ sót $(2,3)$. Giữ C16 làm trang kiểm tra sau đó. | 2026-11-13 |
| nghiêm trọng | L01-B11, C09, G01, G02 (thiếu cụm trang ở mạch 2) | **Lệch ghi chú (nội dung cốt lõi không có trang) + Quy tắc (ký hiệu dùng trước khi định nghĩa):** Mục 2.1 của ghi chú (Định nghĩa 01.4 khối, lần truyền khối, lượt quét, mô hình chi phí đọc ghi; Ví dụ 01.3 tệp 1 TB; Mệnh đề 01.5 $F$, $2F$, $2mF$ có giả thiết và chứng minh) phục vụ mục tiêu 1 và câu hỏi 1 của chương, nhưng deck chỉ có hai câu bằng lời. $F$ chỉ được định nghĩa trong ghi chú diễn giả C09, rồi xuất hiện trên mặt trang G01, G02 như đã biết. | note:11 "tính số khối của một tệp và số lần truyền khối của các lượt quét"; note:239–282; note:248–257 ($F=15\,258\,790$; $10^4$ giây ≈ $2{,}78$ giờ; $152\,587{,}9$ giây ≈ $1{,}77$ ngày); html:194 "Khối là đơn vị đọc ghi giữa đĩa và bộ nhớ."; html:365–366; html:369 "Gọi F là số khối của tệp" (chỉ trong aside); html:641 "một lượt $F$ khối; đọc và ghi $2F$"; html:665. | Ở đầu mạch 2 (sau BT/B00) thêm: trang **Định nghĩa.** khối, lần truyền khối, lượt quét, mô hình chi phí đọc ghi (Định nghĩa 01.4); trang "Ví dụ: tệp 1 TB" với dòng "Tính $F$ và thời gian đọc", $F=\lceil10^{12}/65\,536\rceil=15\,258\,790$, đọc tuần tự $\approx2{,}78$ giờ, đọc từng khối riêng $\approx1{,}77$ ngày; trang **Mệnh đề.** (a) $F$, (b) $2F$, (c) $2mF$ với ba giả thiết (Mệnh đề 01.5), "Chứng minh." một dòng. Có thể thêm Bài tập 01.3 ($6F=91\,552\,740$) làm câu hỏi. C09 khi đó nhắc lại Mệnh đề 01.5 thay vì định nghĩa lại. | 2026-11-13 |
| nghiêm trọng | L01-C00 (và A01–A07) | **Lệch ghi chú (nội dung cốt lõi không có trang):** Định nghĩa 01.1 (bài toán dữ liệu: miền đầu vào $\mathcal I$, quan hệ đầu vào–đầu ra $\mathrm{Out}(I)$, ngân sách tài nguyên), động lực từ mô hình RAM và ba phản ví dụ không có trên deck, dù luận đề bìa dựa vào nó; Định nghĩa 01.2 ($k$ hàng xóm gần nhất chính xác với quy tắc phá hòa) chỉ nằm rải trong ghi chú diễn giả A07. Bìa nêu bốn thành phần "đầu ra, biểu diễn, giới hạn tài nguyên, mức chính xác", khác ba thành phần của Định nghĩa 01.1. | note:76 (mô hình RAM, BHK tr.10); note:122–136; note:160–164; html:20 luận đề; html:268 C00 "Xác định miền đầu vào, kết quả cần trả, mức chính xác yêu cầu."; html:120 "cần quy ước xử lý các khoảng cách bằng nhau" (chỉ aside). | Thêm sau A01 một trang **Định nghĩa.** bài toán dữ liệu = miền đầu vào, quan hệ đầu vào–đầu ra, ngân sách tài nguyên (Định nghĩa 01.1), đọc trên bốn bản ghi của A01 ($\mathrm{Out}(I)=\{(\text{a.vn},55),(\text{b.vn},25),(\text{c.vn},0)\}$); ba phản ví dụ đưa vào ghi chú diễn giả. Sau A07 thêm dòng **Định nghĩa.** $\mathcal N_k(\mathbf y)$ = $k$ chỉ số đầu theo cặp $(d(\mathbf x_i,\mathbf y),i)$ tăng dần (Định nghĩa 01.2) với ví dụ phá hòa $n=3$, $k=1$. Sửa luận đề bìa theo ba thành phần của note:3. | 2026-11-13 |
| trung bình | L01-C07 | **Lệch ghi chú (thiếu bổ đề, ví dụ và bảng đếm đầy đủ):** Bổ đề 01.14 (thủ tục trộn, $\le\|C\|+\|C'\|$ phép so sánh, $\gamma=\|C\cap C'\|$), số liệu MMDS Ví dụ 3.10 mở Mục 3.4 (chữ ký 1000 byte, $15\,259$ khối, $499\,999{,}5$ giây $\approx5{,}79$ ngày) mà Tóm tắt chương dùng ("gần sáu ngày"), Ví dụ 01.8 (gấp đôi kho → số vòng tăng $\approx4{,}000002$ lần) và phép so số nguyên $\gamma c\ge a(\|C_i\|+\|C_j\|-\gamma)$ không có trên deck; bảng đếm chỉ một hàng thay cho bốn hàng của ghi chú. | note:605–612; note:637–653; note:681–688 (bốn hàng: bước 1, trộn, so ngưỡng, xuất $\|R\|$); note:690–699; note:1245 "gần sáu ngày cho một triệu chữ ký"; html:350–352. | Tách C07 thành: trang mở với số liệu MMDS Ví dụ 3.10 (bộ nhớ đủ, đọc ghi một lượt, tính toán $\approx5{,}79$ ngày); trang **Bổ đề.** thủ tục trộn (Bổ đề 01.14) với một dòng chứng minh; trang "Chi phí: xét mọi cặp" có đủ bốn hàng của note:681–686 và dòng "Tính số vòng khi $N$ gấp đôi" ($\approx4{,}000002$). Nêu phép so số nguyên với $\tau=a/c$ trên C04 hoặc C06. | 2026-11-13 |
| trung bình | L01-P03 | **Lệch ghi chú (mục tiêu học tập):** mục tiêu 1 thiếu "tính số khối của một tệp và số lần truyền khối"; mục tiêu 3 của deck "phân biệt tính toán, bộ nhớ, đọc ghi, mạng" thay cho "chứng minh bước xác minh tập ứng viên $A$ trả đúng $R$ khi và chỉ khi $R\subseteq A$"; mục tiêu 5 là phần Đọc thêm. | note:11–16; html:38–42. | Viết lại bốn mục theo note:11–14 (rút còn ≤ 20 âm tiết mỗi dòng), ví dụ: "Nêu đầu vào, đầu ra, ngân sách; tính số khối và số lần truyền khối của lượt quét." / "Đặc tả cặp gần trùng bằng Jaccard; chứng minh xét mọi cặp trả đúng $R$." / "Đếm chi phí xét mọi cặp; chứng minh xác minh trả đúng $R$ khi và chỉ khi $R\subseteq A$." / "Gắn mỗi giới hạn với một nhóm Bài 02–15 và kiến thức nền." Thêm dòng Đọc thêm. Sửa ghi chú diễn giả P03 cho khớp. | 2026-11-13 |
| trung bình | L01-P04, F04 | **Lệch ghi chú (vấn đề trung tâm và câu trả lời):** ghi chú đặt ba câu hỏi (đơn vị chi phí khi dữ liệu trên đĩa; đúng là gì và xét mọi cặp tốn bao nhiêu; khi nào xét ít cặp hơn vẫn đủ) với câu trả lời $F,2F,2mF$ / $R$, $N(N-1)L$ / $\widehat R=A\cap R$, đủ khi $R\subseteq A$. Deck trả lời câu 1 bằng nối hai bảng 100/400 khối, có thêm dòng 4 thuộc Đọc thêm, và dòng 2 dùng "lần kiểm". | note:85–89; note:91 (hình cấu trúc chương, ba cột); html:56–59; html:61 "dòng về khối đọc ghi dựa trên hai bảng 100 và 400 khối với bộ nhớ 20 khối"; html:653–656. | P04: ba dòng, ví dụ "Dữ liệu trên đĩa: chi phí đo bằng lần truyền khối." / "Phép kiểm chính xác: xét mọi cặp trả đúng $R$ sau $\binom N2$ vòng." / "Xét ít cặp hơn qua tập ứng viên $A$: đủ khi $R\subseteq A$." F04 trả lời cùng thứ tự bằng số: "$F$, $2F$, $2mF$ lần truyền khối (Mệnh đề 01.5)"; "$499\,999\,500\,000$ vòng, $\le N(N-1)L$ phép so sánh, $\approx5{,}79$ ngày"; "$\widehat R=A\cap R$; MinHash, LSH (Bài 05–06) phải bảo đảm $R\subseteq A$ hoặc báo độ thu hồi". | 2026-11-13 |
| trung bình | L01-P02, C02, C03, C04, C06, C16, C17, C07, E02, G01, G02, D04, P04, B00, B12, C09, F04, R00, R04, R05, R06, C15 | **Lệch ghi chú (ký hiệu và thuật ngữ) + Quy tắc (một ký hiệu một nghĩa):** (1) deck viết Jaccard là $J$, ghi chú là $\mathrm{SIM}$; (2) deck dùng $S,T$ cho hai tập, ghi chú dùng $C_1,C_2$ (và $C,C'$ khi phát biểu chung); trong deck $T$ vừa là tập (C02) vừa là số ngày (F02); (3) "khối đọc ghi", "lần chuyển khối" thay cho "lần truyền khối"; (4) "hậu kiểm" thay cho "xác minh" (verification); (5) "lần kiểm" thay cho "vòng"; (6) "lượt mua", "lượt/người/năm", "số lượt" (truy cập) trái quy ước "lượt chỉ dùng cho lượt đọc hay lượt quét một tệp" (ghi chú, `exercises.md` viết "lần mua"); (7) tên đối tượng $a,b,f,g$ viết nghiêng, ghi chú viết chữ đứng $\mathrm a$. Quyết định "không sửa deck trong đợt này" (ol:318, rl:1122) là hoãn, nay trái nguyên tắc ký hiệu theo bảng ký hiệu của ghi chú. | note:36–39 (bảng ký hiệu), note:56 ($T$ số ngày), note:69–70 (chữ đứng; "lượt"), ol:320–330 (thuật ngữ thống nhất); html:30 "giao $S\cap T$"; html:285–288 "$J(S,T)$"; html:295; html:304; html:590 "$T$ … $1000$ ngày"; html:56 "số khối đọc ghi"; html:252 "lần chuyển khối"; html:665 "số lần chuyển khối"; html:470 "chỉ được hậu kiểm"; html:645 "Hậu kiểm ứng viên"; html:418; html:352 "lần kiểm"; html:654; html:731 "$100$ lượt/người/năm"; html:742; html:162 "số lượt"; html:411 "$f,g$ … $a,b$"; ex:71, ex:83 "lần mua". | Thay toàn deck: $J\to\mathrm{SIM}$; $S,T\to C_1,C_2$ (P02 dùng $C,C'$); "khối đọc ghi"/"lần chuyển khối" → "lần truyền khối"; "hậu kiểm" → "xác minh"; "lần kiểm" → "vòng"; "lượt mua" → "lần mua", "lượt truy cập" → "lần truy cập"; $a,\dots,g\to\mathrm a,\dots,\mathrm g$. Hình `danh-gia-jaccard.svg` dùng chung với ghi chú (rl:1114 bác đổi nhãn trong đợt ghi chú): nếu giữ $S,T$, mặt trang C02 phải nêu "$S=C_1$, $T=C_2$" như note:444; tốt hơn là vẽ lại với $C_1,C_2$ và cập nhật đoạn đọc hình của ghi chú. | 2026-11-13 |
| trung bình | L01-B00, C00, D01 (sau BT, CT, DT) | **Quy tắc (quy ước 2026-10-28/29: trang bài toán có hình ngay sau trang tiêu đề mạch; trang đầu mạch nêu động lực bằng số liệu có nguồn của ghi chú):** ba trang đầu mạch 2, 3, 4 là bảng hoặc thẻ chữ, không hình, không số; số liệu mở mục của ghi chú không xuất hiện. B00, C00, D01 là trang mở phần do người dùng yêu cầu (er:22, er:29, er:39), nên giữ trang và bổ sung chứ không thay. | `struct.txt`: L01-B00[-], L01-C00[-], L01-D01[-]; note:227 "tệp … 1 TB … bộ nhớ chính có 1 GB, tức một phần nghìn tệp"; note:426 "$N=10^6$"; note:835–839 ba giới hạn có số; html:145–148; html:267–271; html:434–438. | B00: thêm dòng số liệu "Tệp 1 TB, bộ nhớ 1 GB: đọc từng phần" và hình `kho-nhat-ky-bo-nho.svg` (hoặc chèn trang bài toán có hình ngay sau BT, giữ B00 thứ ba). C00: thêm dòng "Kho $N=10^6$ tài liệu: $499\,999\,500\,000$ cặp" và một hình nhỏ (có thể dùng lại `ung-dung-tai-lieu-gan-trung.svg`). Mạch 4: đặt trang ba giới hạn có số của note:835–839 cùng `ban-do-hoc-phan.svg` ngay sau DT, D01 lùi về trước E01 (khớp thứ tự Mục 4.1 → 4.2). | 2026-11-13 |
| trung bình | L01-B11, C09, C05, C06, C15, C16, D01, D02 | **Lệch ghi chú (thứ tự khái niệm):** (a) ghi chú mở Mục 2 bằng khối và lượt quét (2.1) rồi mới tới dòng, nén, đĩa; deck nêu khối ở B11 (giữa mạch 2) và định nghĩa chi phí đọc ghi ở C09 (mạch 3); (b) Định nghĩa 01.13 (mô hình chi phí) đứng sau tính đúng và sau số liệu MMDS Ví dụ 3.10; deck đặt bảng tiêu chí C05 trước C06; (c) Mục 3.5 đã đổi thứ tự thành ứng viên → xác minh → độ thu hồi (rl:1106); deck đặt C15 (độ thu hồi) trước C16 (ứng viên); (d) Mục 4.1 (bản đồ) đứng trước Mục 4.2 (CLO); deck đặt D01 trước D02. | note:229, 296, 328, 350; note:603–628; note:710–776; note:843–904; rl:1106 "thứ tự: độ thu hồi trước ứng viên → chấp nhận: đổi thứ tự"; html:192–201; html:363–369; html:320–336; html:406–419; html:432–444. | (a) xem dòng Mục 2.1 ở trên: cụm khối/lượt quét đứng đầu mạch 2, C09 nhắc lại; (b) chuyển C05 xuống sau C18, trước C07 hoặc ngay sau trang số liệu MMDS Ví dụ 3.10; (c) thứ tự C16 (ứng viên) → trang Mệnh đề 01.16 → ví dụ 01.9 → C15 (độ thu hồi tại $k$); (d) D02 → D03…D07 → D01 → E01…E03 → D11. Kiểm lại câu nối trong ghi chú diễn giả các trang lân cận. | 2026-11-13 |
| trung bình | L01-C17, E02 | **Lệch ghi chú (ví dụ chạy tay):** ghi chú đã thay vết chạy $N=2$ (bị đánh giá "quá ngắn", rl:1109) bằng Ví dụ 01.7: $N=3$, $C_3=C_1$, $\tau=1/2$, bảng bốn vòng, $R=\{(1,3)\}$; deck vẫn dùng $N=2$ với $S,T$. | note:496–520; rl:1109 "Ví dụ 01.7 \| chạy tay $N=2$ quá ngắn \| chấp nhận: $N=3$, $C_3=C_1$"; html:304 "Với $N=2$, $C_1=S$, $C_2=T$: chỉ xét $(1,2)$"; html:536. | C17 giữ phần (a) sáu cặp với $N=4$; thay phần (b) bằng bảng vết của note:510–515 (vòng 0–3, $\mathrm{SIM}$, so với $\tau=1/2$, kết quả $\varnothing,\varnothing,\{(1,3)\},\{(1,3)\}$), thêm dòng "Tính …". E02 hàng "Chạy tay": "vết $N=3$, $\tau=1/2$: $R=\{(1,3)\}$". Nếu bảng vượt trần, tách C17 thành hai trang cùng tiêu đề. | 2026-11-13 |
| trung bình | L01-B01, B10, B03, B04, B06 (và thiếu trang) | **Lệch ghi chú (khối có số hiệu của Mục 2.2–2.4 không có trên deck):** Ví dụ 01.4 (mẫu theo từng bản ghi cho tỷ số $\mu_2/(10\mu_1+19\mu_2)$, với $\mu_1=\mu_2=10$ được $1/29$ thay vì $1/2$); số liệu lọc thư ($10^9$ địa chỉ, ≥ 20 GB, bộ nhớ $8\cdot10^9$ bit); Định nghĩa 01.7 ($\mathrm{dec}(\mathrm{enc}(x))=x$); Định nghĩa 01.8 và Ví dụ 01.5 (chỉ mục băm, 800-555-1212 → thùng 17); Tình huống 01.3 ($h(x)=x\bmod10$ với khóa chẵn). Các trang tình huống của deck chỉ mô tả bằng lời. | note:300–318; note:320; note:332–338; note:368–384; note:1218–1230; html:153–156 (B01 không số); html:169–173; html:178–181; html:214–217. | B01: thêm dòng số "danh sách $10^9$ địa chỉ ≥ 20 GB, bộ nhớ $8\cdot10^9$ bit"; thêm trang "Ví dụ: mẫu theo từng bản ghi" với "Tính tỷ số trên mẫu", kết quả $\mu_2/(10\mu_1+19\mu_2)$, kiểm $1/29\ne1/2$. B10 hoặc B03: **Định nghĩa.** bộ nén $(\mathrm{enc},\mathrm{dec})$, không mất thông tin khi $\mathrm{dec}(\mathrm{enc}(x))=x$ (Định nghĩa 01.7). Sau B06: trang **Định nghĩa.** hàm băm, chỉ mục băm (Định nghĩa 01.8) với Ví dụ 01.5. | 2026-11-13 |
| trung bình | L01-R01–R06 | **Quy tắc (quy ước 2026-10-28/29 và CLAUDE.md "a worked exercise puts 'Lời giải:' on the next slide") + Lệch `exercises.md`:** không bài recitation nào có trang "Lời giải:" cùng tiêu đề; lời giải chỉ ở ghi chú diễn giả. Bài tập 01.10 yêu cầu với mỗi câu "điều Hệ quả 01.22 cho biết", nhưng R02, R03 không hỏi và không trả lời phần này; Hệ quả 01.22 (Markov) chưa có trên mặt trang nào, dù R05 dùng nó trong ghi chú diễn giả. | ex:24 "…kỳ vọng, và điều Hệ quả 01.22 cho biết"; ex:63; note:1125–1139; html:715 "Lời giải gồm số phép thử, xác suất mỗi phép thử, kỳ vọng và tỷ lệ so với cơ sở."; html:725; html:727 (không có cận $\Pr(X\ge1)\le0{,}0831$); html:754 "Pr(Y≥1)≤E[Y]". | Sau R02, R03, R05 thêm trang "Lời giải:" cùng tiêu đề, chép lời giải của ex:32–65 và ex:81–98 (số phép thử, xác suất, kỳ vọng $999\,499{,}9990005$; $249\,749{,}999875125$; $0{,}0830834999169165$; $1{,}90\times10^{-4}$). R02, R03 thêm yêu cầu "nêu điều Hệ quả 01.22 cho biết": (a), (b) cận không cho thông tin; (c) $\Pr(X\ge1)\le0{,}0831$. Hệ quả 01.22 đặt trên trang "Nhắc lại:" đầu mạch 7 (xem dòng mạch 5). Ghi chú diễn giả giữ hướng dẫn chấm. | 2026-11-13 |
| trung bình | L01-C10, C11, C12, C13, D04, D06, D08, D09, D10, B01, B03, A03, E02 | **Lệch ghi chú (nội dung trên deck không có trong ghi chú):** ví dụ, cơ chế và khẳng định ngoài ghi chú: dây chuyền độ trễ (C11), chi phí xây dựng chỉ mục véc-tơ (C12), ví dụ sửa lương và chỉ mục theo lương (C13), "định nghĩa chi phí truyền thông của MMDS 2.5" (C10; ghi chú dùng CS246 trang chiếu 67–68), hoán vị MinHash (D04), JPEG "biến đổi cô-sin rời rạc" (D06), bước nhảy ngẫu nhiên PageRank và HITS (D08), cơ chế HNSW/PQ (D09), cơ chế FM/Count-Min/DGIM (D10), tính chất Bloom (B01), "Không phải mọi chuỗi đều ngắn hơn sau nén" (B03), đồ thị y, a, m (A03), "Mã Python hoặc C++" (E02). Các trang này có từ ER-003, ER-004 theo yêu cầu người dùng, nên không bỏ trang. | er:29–38 (ER-003 "slide riêng có khái niệm, ví dụ cụ thể, hình minh hoạ"); er:39–45 (ER-004 "Mỗi khái niệm … cần lý giải, minh hoạ, ví dụ"); note:617–628 (bảng Định nghĩa 01.13 chỉ một dòng mỗi đại lượng); note:708; note:849–872; html:381–383; html:387–390; html:395–397; html:376; html:471; html:509; html:458, 460; html:477–479; html:494–499; html:157; html:182; html:86–88; html:540. | Theo luật "on conflict fix the note first": bổ sung vào ghi chú Mục 3.4 một ví dụ cho mỗi đại lượng của Định nghĩa 01.13 (dùng lại ví dụ của deck: nối bảng cho bộ nhớ, sắp ngoài cho đọc ghi, đếm từ cho dữ liệu mạng, truy vấn véc-tơ cho độ trễ và xây dựng, chỉ mục theo lương cho cập nhật) và vào Mục 4.1 một câu cơ chế cho mỗi phương pháp; hoặc rút các câu cơ chế khỏi mặt trang và ghi chú diễn giả về mức ghi chú. C10: thay "MMDS 2.5" bằng công thức chi phí truyền thông CS246 của note:708. | 2026-11-13 |
| trung bình | ghi chú diễn giả L01-P04, A01, A02, A04, A06, A07, B02, B03, B04, B05, B06, B07, B08, B12, C01, C02, C06, C07, C08, C11, C13, C14, C16, C17, D03, D08, E06, F01, F02, F06, R04 | **Quy tắc (luật tác giả: không câu xuất xứ số liệu, không rào đón vị thế của văn bản/hình, 2026-11-04; no-ai-slop Detect: negative listing):** khoảng 30 câu "không phải số đo", "Hình … không gán …", "chưa …" trong ghi chú diễn giả. | html:120 "lấy từ BIODS 271, không phải số đo của học phần"; html:252 "một số đếm chứ không phải số đo"; html:112 "Con số gần 500 tỷ là phép đếm, không phải kết quả đo tốc độ."; html:354 "Đây là phép đếm, không phải số giây đo được."; html:547 "Con số 3/5 chỉ mô tả chất lượng truy vấn đang xét, không phải kết quả đo một hệ thống thực."; html:190 "Hình minh họa định tính …, không phải ảnh thực nghiệm hoặc số đo chất lượng. Không suy ra tỷ lệ nén hay sai số từ kích thước các hình."; html:210 "…không phải dữ liệu số mới."; html:226 "Hình là đặc tả …, không đưa ra tập kết quả số."; html:234 "Sơ đồ không vẽ đối tượng thật nên không gán kết quả cuối cùng."; html:280 "Bốn tài liệu trong hình chỉ biểu diễn sáu cặp có thể xét, không gán điểm tương đồng."; html:306 "Ví dụ chỉ minh họa thứ tự xét, không gán cặp nào…"; html:335; html:361 "Sơ đồ kho dữ liệu không vẽ theo tỷ lệ diện tích"; html:383; html:404 "Hình không gán tỷ lệ nén"; html:460 "Hình không gán điểm hay thứ hạng mới."; html:96; html:80; html:586; html:592 "Đây là giả thiết của mô hình nền, không phải kết quả kiểm chứng từ hồ sơ thực."; html:608 "Đây là hệ quả phép đếm, không phải một bộ hồ sơ mới."; html:419 "bài này chưa phân tích cơ chế ấy". | Xóa các câu này. Khi giới hạn của ví dụ là nội dung, nêu nguyên nhân dạng khẳng định, ví dụ A07: "Quy mô $10^{10}$ véc-tơ, 3072 chiều, 4 byte mỗi thành phần cho kho $122{,}88$ TB." (thay câu "không phải số đo"); F02: "Mô hình nền mô tả dữ liệu khi không ai phối hợp; nó được so với dữ liệu quan sát." C16: thay "bài này chưa phân tích cơ chế ấy" bằng "Bài 06 phân tích xác suất thành ứng viên của LSH." Xuất xứ số liệu ghi vào `review-log.md`. | 2026-11-13 |
| trung bình | ghi chú diễn giả L01-B07, B08, B09, C13, C15, R04, R06 | **Quy tắc (không lời chú của người soạn, không chú thích đính chính nguồn, không tên tệp nội bộ trong ghi chú diễn giả):** | html:226 "Hai từ khóa được gọi là từ thứ nhất và từ thứ hai, không tự đặt thêm kho văn bản." và "công thức OR ở bản PPTX có lỗi dấu, dùng phép hợp đúng theo định nghĩa và sách"; html:234 "Vị trí tương đối giữ từ sơ đồ Bài 14"; html:242 "Kịch bản ở Bài 15 dùng ngân sách 20 khối" (ghi chú lấy từ DSC Ch.15 trang chiếu 40, note:360); html:397 "Không cần một mức lương giả để thấy quan hệ phụ thuộc"; html:412 "Nguồn: Bài 07 mục 1 và ann-recall.svg"; html:736 "Giữ giả thuyết ấy như điều kiện làm bài; chưa bàn tính đúng thực tế của giả thuyết theo chú thích nguồn."; html:747 "đây là bước chia nhỏ của cùng bài". | Xóa các câu và đoạn nguồn trên; B09 đổi thành "Bộ nhớ $M=20$ khối, như ví dụ nối băm của DSC (Ch.15, trang chiếu 40)"; C15 nguồn đổi thành "Princeton COS 597A, lớp 8–9" như note:1298; R04: "Giả thuyết làm việc của đề: một cặp khủng bố mua đúng cùng một tập 10 mặt hàng vào một lần trong năm." | 2026-11-13 |
| trung bình | L01-P02 | **Quy tắc (nhắc lại mọi kết quả trước lần dùng đầu; "Nhắc lại:" chỉ cho kết quả) + Lệch ghi chú (tiên quyết):** ghi chú nêu tiên quyết mô hình RAM và ký hiệu $O$, danh sách đã sắp, bất biến vòng lặp, bảng băm, biến chỉ báo; deck dùng bất biến (C06, C18), trộn danh sách đã sắp (C07), $O(N^2L)$ (C07) mà không nhắc lại. Dòng đầu "Nhắc lại: tiên quyết UET.CS1058." không phải một kết quả. Dòng Ký hiệu thiếu $F$, $M$, $L$. | note:20–28; html:28–32; html:349–354; html:339–342. | Dòng đầu đổi thành câu thường "Tiên quyết: UET.CS1058 (Cấu trúc dữ liệu và giải thuật)." Thay một dòng "Nhắc lại:" bằng "Nhắc lại: bất biến vòng lặp đúng khi khởi tạo, được duy trì, cho kết luận khi dừng; trộn hai danh sách đã sắp." Dòng Ký hiệu thêm "$F$, $M$ số khối của tệp và của bộ nhớ; $L$ cỡ tập lớn nhất". Giữ ≤ 6 dòng (gộp hai dòng nhắc lại tập và cặp). | 2026-11-13 |
| nhẹ | L01-G01 | **Lệch ghi chú (bảng tổng kết):** hàng "Hậu kiểm ứng viên" ghi công thức "kiểm chính xác" thay cho $\widehat R=A\cap R$, $\widehat R=R\iff R\subseteq A$; hàng "Chi phí đọc ghi" thiếu $2mF$; hàng xét mọi cặp ghi $O(N^2L)$ thay cho $\le N(N-1)L$. | note:1265–1272; note:1281; html:641, 644, 645. | Hàng 1: "$F$; $2F$; $m$ lượt $2mF$"; hàng 4: "$\le N(N-1)L$ phép so sánh"; hàng 5 đổi tên "Xác minh ứng viên", giả thiết "$R\subseteq A$, phép kiểm chính xác", công thức "$\widehat R=A\cap R$". Giữ ≤ 80 âm tiết. | 2026-11-13 |
| nhẹ | L01-C15 | **Lệch ghi chú (định nghĩa):** trang chỉ cho giá trị $\operatorname{recall@}5=3/5$, không có công thức Định nghĩa 01.17 và không có độ thu hồi cho bài toán cặp $\|\widehat R\cap R\|/\|R\|$. | note:750–760; html:408–410. | Thay dòng 1 bằng **Định nghĩa.** $\operatorname{recall@}k(\mathbf y)=\|\widehat{\mathcal N}_k(\mathbf y)\cap\mathcal N_k(\mathbf y)\|/k$ (Định nghĩa 01.17); giữ phép tính $3/5$. | 2026-11-13 |
| nhẹ | L01-C12 | **Lệch ghi chú (câu định nghĩa):** "thời gian và bộ nhớ lớn nhất khi tạo chỉ mục" đọc như "thời gian lớn nhất"; ghi chú: "thời gian và bộ nhớ để tạo một cấu trúc trước khi trả truy vấn". | note:625; html:387. | "Chi phí xây dựng là thời gian và bộ nhớ để tạo chỉ mục trước khi trả truy vấn." | 2026-11-13 |
| nhẹ | L01-CT, DT, FT, C05 | **Quy tắc (độ dài ghi chú diễn giả):** ghi chú trang tiêu đề mạch vượt 100 âm tiết: CT 113, DT 132, FT 120; C05 167 âm tiết (> 150) và có câu chỉ đường "Các trang sau trình bày theo thứ tự tính đúng, tính toán, …". | đếm token có chữ cái trong `aside.notes`; html:263, 430, 577, 328. | Rút mỗi ghi chú trang tiêu đề còn 3 câu (kết quả kế thừa, nhiệm vụ mạch, đầu ra giao tiếp); C05 bỏ câu chỉ đường và câu cuối. | 2026-11-13 |
| nhẹ | ghi chú diễn giả L01-P04, GT, F04, D01, E02, D10, G03, C02, C03 | **Quy tắc (không chỉ đường, author's voice "Navigation and forward pointers"):** | html:61 "Các dòng được trả lời theo đúng thứ tự ở phần tổng kết."; html:636 "Vấn đề trung tâm được trả lời theo đúng thứ tự các dòng đã nêu ở mở đầu."; html:658 "Mỗi dòng trả lời dòng cùng vị trí của trang vấn đề trung tâm."; html:439 "được cụ thể hóa ở hai trang sản phẩm phân tích và trách nhiệm dữ liệu cuối mạch"; html:540 "Bất biến … đã được lập ở phần phân tích."; html:499 "danh mục trong ghi chú còn giải thích AMS và suy giảm mũ"; html:678 "Ghi chú bài giảng có đủ lập luận và lời giải."; html:289 "Bài 05 xét đầy đủ quy tắc biểu diễn"; html:298 "quy ước hợp rỗng của Bài 05". | Xóa; nếu cần nội dung thì nêu trực tiếp (D10: "AMS ước lượng mômen bậc hai; suy giảm mũ đếm có trọng số giảm theo tuổi" nếu được thêm vào ghi chú). | 2026-11-13 |
| nhẹ | L01-C12, F03, F01, C10, C13; ghi chú diễn giả D02, D03, D04 | **Quy tắc (no-ai-slop Detect; luật tác giả cắt từ làm mềm, ưu tiên nghĩa khẳng định):** câu kết dạng châm ngôn; câu định nghĩa bằng phủ định; "có thể" không kèm số; đối lập nhị phân trong ghi chú diễn giả; gần mọi ghi chú diễn giả kết bằng một câu cầu nối cùng khuôn "Ngoài …, còn …" (nhịp máy móc). | html:389 "Độ trễ truy vấn thấp không xóa chi phí chuẩn bị." (fake-profound kicker); html:612 "Kỳ vọng là giá trị trung bình theo mô hình, không phải số đếm trên một kho cụ thể."; html:585 "Nhiều phép thử có thể tạo nhiều trùng ngẫu nhiên."; html:375 "…có thể giảm dữ liệu truyền"; html:444 "Đây là thứ tự học, không phải chuỗi tiên quyết…"; html:452 "MapReduce là mô hình xử lý; không tự biến lời giải thành xấp xỉ."; html:471 "Chữ ký không phải bản nén có thể khôi phục tài liệu."; html:104 "Kết quả tìm kiếm còn có thể chứa nhiều bản sao của cùng nội dung."; html:112 "Một nhu cầu khác là …". | C12: "Báo chi phí xây dựng cùng độ trễ truy vấn." F03: "Kỳ vọng là trung bình của $X$ qua các lần sinh dữ liệu theo mô hình." F01: "$\binom{10^9}{2}\approx5\times10^{17}$ cặp người: mẫu hiếm ở từng cặp vẫn xuất hiện nhiều lần." D02: thay câu phủ định bằng chuỗi tiên quyết của note:876–880. Câu cầu nối cuối ghi chú diễn giả chỉ giữ khi nêu kết quả kế thừa hoặc giới hạn tạo nhu cầu mới. | 2026-11-13 |
| nhẹ | L01-D03, D09 | **Quy tắc (nhãn in đậm chỉ thuộc danh sách cho phép; thuật ngữ mới in nghiêng):** | html:450 "<strong>Khóa</strong> là từ cần đếm"; html:477 "<strong>HNSW</strong> (đồ thị thế giới nhỏ phân tầng):"; html:478 "<strong>Lượng tử hóa tích (PQ):</strong>". | Đổi thành *khóa*, *HNSW*, *lượng tử hóa tích* (in nghiêng, không in đậm); HNSW kèm tên tiếng Anh (hierarchical navigable small world) trên mặt trang như note:856. | 2026-11-13 |
| nhẹ | L01-C17 | **Quy tắc (trang "Ví dụ: …" có dòng "Tính …"):** dòng đầu là "$N=4$: liệt kê các cặp…". | html:302. | "Tính thứ tự các cặp với $N=4$ và vết chạy với $N=3$, $\tau=1/2$." (gộp với sửa vết chạy ở trên). | 2026-11-13 |
| nhẹ | toàn deck (mọi `<section id="L01-…">`) | **Quy tắc (mã nội bộ không lộ):** mọi trang có thuộc tính `id="L01-…"`, nên khi `hash: true` thanh địa chỉ hiện `#/L01-A01`; deck mẫu 09, 10 chỉ đặt `id` cho `mach-2…7`. | html:18, 26, 35, 46, … (77 trang); lecture-09/10: 6 `<section id=` mỗi tệp. | Bỏ thuộc tính `id` của các trang nội dung, giữ `data-slide-id` và `id="mach-N"`. | 2026-11-13 |
| nhẹ | L01-A01 | **Quy tắc (một ký hiệu một nghĩa; ghi chú diễn giả không dùng ký hiệu không có trên trang):** ghi chú diễn giả dùng $D$ (dung lượng tệp) và $M$ (bộ nhớ, byte) không có trên mặt trang hay hình; trong ghi chú $D$ là số chiều, $M$ là số khối. | html:72 "D là dung lượng tệp bản ghi, còn M là bộ nhớ khả dụng"; note:48, 51; `kho-nhat-ky-bo-nho.svg` chỉ có nhãn chữ. | Viết bằng lời: "tệp bản ghi lớn hơn bộ nhớ chính"; hoặc dùng $F$, $M$ tính bằng khối như note:67. | 2026-11-13 |
| nhẹ | L01-D01, D02 | **Lệch ghi chú (Mục 4.2, 4.1):** D01 nêu hai năng lực "Giải thích", "Lựa chọn"; ghi chú nêu đủ CLO1–CLO4 bằng lời đề cương. D02 không nêu quan hệ tiên quyết theo năm nhánh. | note:899–904; note:874–882; html:435–438; html:444. | D01: bảng bốn hàng CLO1–CLO4 với ví dụ trên cặp gần trùng (giữ ≤ 80 âm tiết). D02 ghi chú diễn giả: năm chuỗi tiên quyết của note:876–880. | 2026-11-13 |
| nhẹ | L01-G03 | **Lệch ghi chú (tài liệu tham khảo):** BHK ghi "(2020)", ghi chú ghi "bản ngày 04/01/2018"; CLRS 4e (§1.1, §2.1, cơ sở của Định nghĩa 01.1 và chứng minh bất biến) không có trong danh mục. | note:1292, 1299; html:675. | Sửa năm BHK; thêm dòng CLRS 4e (§1.1, §2.1) vào ghi chú diễn giả hoặc mặt trang. | 2026-11-13 |
| nhẹ | toàn deck | **Quy tắc (deck mới, đặc tả 2026-11-04/08: số hiệu khối ghi chú được phép, tối đa một lần mỗi trang):** deck không dẫn số khối nào (refcheck 0), nên sinh viên không nối được trang với Định nghĩa/Mệnh đề và Bài tập 01.10–01.11 của `exercises.md`. | `refcheck.txt` "== 01: 0 đúng, 0 sai"; deck mẫu 09 dẫn 123 lần. | Thêm "(Định nghĩa 01.9)" ở C02, "(Định nghĩa 01.10)" ở C03, "(Thuật toán 01.11)" ở C04, "(Mệnh đề 01.12)" ở C06, "(Mệnh đề 01.15)" ở C07, "(Mệnh đề 01.16)" ở trang mới, "(Định nghĩa 01.17)" ở C15; R01, R04 ghi "Bài tập 01.10", "Bài tập 01.11" cạnh số bài MMDS. | 2026-11-13 |

### Đã kiểm, không lỗi / bác bỏ cờ quét

- **md5:** deck, ghi chú, `exercises.md` trùng nhau lúc bắt đầu và kết thúc (`e7d4c423`, `deadf0ea`, `4bb70c95`). Không sửa tệp nào trong kho.
- **Kỹ thuật (từ `scan/01/check.json`, đối chiếu lại):** 83 trang, 7 section ngoài, `mach-2…7` mở đúng `#/2…7`; 0 lỗi console, 0 request hỏng, 0 `.katex-error`, 0 `fragment`, không cuộn ngang ở 390 px; `style_blocks=1` là cờ giả (thẻ runtime). Mã nguồn không có `<style>`, `style=""`, `.dense`.
- **Ảnh chụp (`SP/shots-01/`):** G01, F04, E03, R06, C05, P03 ở 1600×900 và 390×844, 0 phần tử tràn khung. Ảnh G01 1280 đầu tiên bị cắt trái là ảnh chụp giữa hiệu ứng chuyển trang; chụp lại sau 1,5 s ở 1600×900 thì đủ.
- **Mật độ:** 16 trang > 60 âm tiết (P03 80, D07 77, E01 79, E02 77, E03 79, G01 79, F04 78, F07 71, R06 74, G03 70, P01 68, C05 68, R00 65, D06 64, D10 62, B00 61) đều ≤ 80, thuộc loại mục tiêu, nội dung, tổng kết, bảng hoặc đề recitation, và mỗi trang có trần 80 kèm số âm tiết trước → sau trong sb:360–442; không trang nào vượt 1,5 lần trần; không trang > 3 công thức hiển thị. Số dòng: ngoại lệ A01 (8), P01 (8), G03 (7), trang bảng ≤ 8 có trong sb:354. Mẫu dòng dài nhất (D11 mục 1, F04 dòng 1 và 4, C01 Đầu ra, B12 câu 2) đều ≤ 20 âm tiết.
- **Trang tiêu đề mạch:** dòng dẫn 22, 22, 22, 20, 21, 21 âm tiết, đúng khuôn "Muốn …, phải …"; mỗi trang 5 từ khóa; tên khác tiêu đề trang nội dung đầu; ghi chú BT 80, GT 62, RT 64 âm tiết đạt (CT, DT, FT vượt: đã ghi ở bảng).
- **Ghi chú diễn giả:** không trang nào < 40 âm tiết; R05 210 âm tiết là lời giải (≤ 250); không "Trang này", không thời lượng, không `data-slide-id` hay mã kế hoạch; không "chúng ta", "ta thấy", "rõ ràng" trên mặt trang.
- **Hình SVG:** nhãn nhỏ nhất khi chiếu 1280×720 (tính theo `object-fit: contain`): 20,4 px (D08), 20,8 px (C15), 21,8 px (D06); mọi hình ≥ 18 px; mọi `img` có `role="img"` và `alt` cụ thể.
- **Số đã tính lại, đúng:** $\binom{10^6}{2}=499\,999\,500\,000$; $5000\cdot400+100=2\,000\,100$ (B12); $p=10^{-4}/10^5=10^{-9}$, $p^2=10^{-18}$ (F05); $\mathbb E[X]=249\,749{,}99975025\approx249\,750$, xấp xỉ $250\,000$ (F03); $N(N-1)L$ (C07); $3/8$ và $\tau\le3/8$ (C02, G02); $6F$ (G02); $3/5$ (C15, E06); recitation: $999\,499{,}9990005$, $249\,749{,}999875125$, $0{,}0830834999169165$ ($\approx0{,}0833$ theo xấp xỉ), $\mathbb E[Y]\approx0{,}000189818469$, $100^2$ cặp lần mua — khớp ex:32–65, ex:81–100.
- **Câu hỏi và bài tập khớp ghi chú:** A10 ↔ Bài tập 01.1; B12 câu 1, 3 ↔ Bài tập 01.4(a), (b); C04 câu hỏi ↔ Bài tập 01.5; C16 ↔ Bài tập 01.7; D11 ↔ Ví dụ 01.11; G02 câu 1 ↔ 01.6, câu 2 ↔ 01.3, câu 3 ↔ 01.9(a, b); R01–R06 ↔ Bài tập 01.10(a–c), 01.11 (cùng đề MMDS 1.2.1, 1.2.2, tr.8, cùng giả thuyết làm việc); ghi chú diễn giả R02, R03, R05, R06 có hướng dẫn chấm.
- **Khớp ghi chú, đạt:** bảy bài toán A01–A07 cùng thứ tự và cùng số với bảng note:142–150 (A01 khớp Ví dụ 01.1); Định nghĩa 01.10 (C03) và giả mã Thuật toán 01.11 (C04) khớp note:465–550; tính đúng C06, C18 khớp bốn phần chứng minh của Mệnh đề 01.12; Mệnh đề 01.15 (C07) đúng cận; bảng kiến thức nền E01 khớp note:908–914; sản phẩm học tập E02/E06 và trách nhiệm E03 khớp note:918–928; mô hình F02, xác suất F05, phép thử F06, kỳ vọng F03 và bảng F07 khớp Định nghĩa 01.18–01.19, Ví dụ 01.12–01.14, Mệnh đề 01.20, Nhận xét 01.23; tên năm mạch nội dung khớp tên mục của ghi chú.
- **Mạch kết luận đủ thành phần:** trang tiêu đề GT; bảng "Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán" (bảng thuật toán thứ hai không áp dụng vì chỉ một thuật toán, lý do ở sb:350); trang trả lời có điều kiện F04 nhắc lại $N=10^6$ bằng số; G02 mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng." với 3 câu có lời giải; G03 ghi công `http://www.mmds.org`, liên kết viewer ghi chú và dòng nối Bài 02 khớp note:1245, 1301.
- **Dẫn chiếu:** `refcheck.txt` báo 0 dẫn chiếu `01.k`, nên không có dẫn chiếu sai khối (thiếu dẫn chiếu ghi ở bảng, mức nhẹ).
- **Cờ quét bác bỏ:** `style_blocks=1` (thẻ do runtime chèn); `overflow_1600` của deck 01 rỗng, không cần xác nhận.
- **Không đề nghị lật lại:** các trang mở phần B00, C00, D01–D07, E01–E06 và các trang tiêu chí C08–C15 do ER-002, ER-003, ER-004 yêu cầu (er:22–45) được giữ; đề xuất ở bảng chỉ bổ sung hình, số, thứ tự hoặc đồng bộ ghi chú. Quyết định "không sửa deck trong đợt này" (sb:450, 460; ol:318; rl:1122, 1142) là hoãn sửa, nay trái nguyên tắc deck khớp ghi chú, nên được nêu lại.

### Quyết định của người dùng (2026-11-13)

- Mạch 5 (mẫu trùng ngẫu nhiên và suy luận) được gắn nhãn **Đọc thêm**, khớp mục "Đọc thêm" của ghi chú (note:956). Mạch 7 mở bằng một trang "Nhắc lại:" nêu đủ mô hình và kết quả cần cho bài tập. Các phát hiện liên quan tới mạch 5, mạch 7, mục tiêu 5, vấn đề trung tâm (P04, F04), bảng G01 và câu 3 của G02 sửa theo hướng này.
- Thuật ngữ: dùng "véc-tơ". Deck 01 đã dùng "véc-tơ" (30 chỗ), không cần sửa.

## Sửa deck theo bảng phát hiện 2026-11-13

**Tác tử.** Một tác tử sửa (writer) do điều phối viên tạo; loại, mô hình và effort ghi theo lời gọi công cụ của điều phối viên. Căn cứ: bảng phát hiện ở mục trên, "Quyết định của người dùng (2026-11-13)", `edit-decisions.md` (G1–G18, D01); `no-ai-slop` chế độ Edit, tự kiểm theo `eval.md`. Không sửa ghi chú, `exercises.md`, CSS hay deck khác; không commit.

**Kết quả.** Deck 83 → 100 trang (80 giảng, 8 Đọc thêm, 12 bài tập); bảy section; 17 trang thêm, không bỏ trang. Hình: sửa nhãn bốn SVG (`danh-gia-bo-nho`, `ung-dung-noi-bang`, `ung-dung-thong-ke-cua-so`, `ung-dung-trung-gio-hang`) và thêm `danh-gia-jaccard-c.svg` bằng script `tools/courses/ds-foundation-algorithms/2627-1/img/lec-01/fix_deck_svg_2026_11_13.py`. Chi tiết từng trang ở `storyboard.md`, mục cùng tên.

**Xuất xứ dữ liệu tự dựng** (không ghi trên deck): bốn bản ghi a.vn, b.vn, c.vn của Ví dụ 01.1; vết chạy $N=3$, $C_3=C_1$, $\tau=1/2$ (Ví dụ 01.7(b)); $R$, $A$ của Ví dụ 01.9; năm hàng xóm a–g của Ví dụ 01.10; ví dụ phá hòa $n=3$, $k=1$ (Định nghĩa 01.2) đều do ghi chú dựng để tính tay, lấy nguyên từ ghi chú. Các số còn lại có nguồn ở dòng "Nguồn:" của ghi chú diễn giả.

| phát hiện | xử lý | trang | ghi chú |
|---|---|---|---|
| nghiêm trọng — mạch 5 dạy như mạch chính | sửa theo D01: nhãn Đọc thêm trên P01, dòng dẫn FT và mọi trang F; P03 bỏ mục tiêu 5, thêm dòng Đọc thêm; P04, F04 còn ba dòng; G01 bỏ hàng kỳ vọng; G02 câu 3 thay bằng Bài tập 01.7; thêm R07 "Nhắc lại:" đầu mạch 7 và F08 (Markov) | P01, P03, P04, FT, F01–F08, G01, F04, G02, R07 | mạch 5 không tính vào 120 phút |
| nghiêm trọng — Mệnh đề 01.16 không có trang | thêm trang mệnh đề có chứng minh và trang Ví dụ 01.9 với FP, FN, độ thu hồi $1/2$; C16 giữ làm trang nhu cầu và câu hỏi | C16, C23, C24 | |
| nghiêm trọng — Mục 2.1 không có trang, $F$ dùng trước định nghĩa | thêm Định nghĩa 01.4, Ví dụ 01.3, Mệnh đề 01.5 ở đầu mạch 2; C09 và B11 đổi thành "Nhắc lại:"; Bài tập 01.3 ($6F=91\,552\,740$) trong ghi chú diễn giả B16, C09 và G02 câu 2 | B14, B15, B16, B11, C09 | |
| nghiêm trọng — Định nghĩa 01.1, 01.2 không có trang; luận đề bìa bốn thành phần | thêm A11 (Định nghĩa 01.1 trên Ví dụ 01.1, ba phản ví dụ trong ghi chú diễn giả) và A12 (Định nghĩa 01.2, ví dụ phá hòa); luận đề theo ba thành phần | P00, A11, A12, A10 | A12 đặt sau A07 theo thứ tự note:154–164 |
| trung bình — C07 thiếu bổ đề, ví dụ, bảng bốn hàng | thêm C20 (MMDS Ví dụ 3.10: $15\,259$ khối, $5{,}79$ ngày), C21 (Bổ đề 01.14); C07 có Mệnh đề 01.15, bảng bốn hàng note:681–686 (có phép so số nguyên), dòng $N$ gấp đôi $\approx4{,}000002$ | C20, C21, C07 | phép so số nguyên đặt trong bảng C07 và ghi chú diễn giả C21 |
| trung bình — mục tiêu học tập | viết lại theo note:11–14; đếm tay 78 âm tiết | P03 | |
| trung bình — vấn đề trung tâm và câu trả lời | ba dòng theo note:85–89; F04 trả lời cùng thứ tự bằng số | P04, F04 | |
| trung bình — ký hiệu và thuật ngữ | $\mathrm{SIM}$, $C_1,C_2$, "lần truyền khối", "xác minh", "vòng", "lần mua", "lần truy cập", $\mathrm a,\ldots,\mathrm g$ trên toàn deck; hình deck `danh-gia-jaccard-c.svg` ghi $C_1,C_2$ | toàn deck; C02, C19, E02, G02, R04, R06, B02, B09 | không đổi nhãn hình ghi chú `danh-gia-jaccard.svg` (ghi chú vẫn đọc $S=C_1$, $T=C_2$); nhãn "lượt" trong bốn SVG đổi theo |
| trung bình — B00, C00, D01 không hình, không số | B00 thành trang bài toán có hình (1 TB, 1 GB); C00 thêm $N=10^6$ và hình (chuyển từ C01); D02 lên ngay sau DT với ba giới hạn có số và bản đồ; D01 lùi về trước E01 | B00, C00, C01, D02, D01 | giữ chức năng ER-002, ER-003, ER-004 |
| trung bình — thứ tự khái niệm | (a) Mục 2.1 đầu mạch 2; (b) C05 sau C20; (c) C16 → C23 → C24 → C15; (d) D02 → D03…D07 → D01 → E01…E03 → D11 | mạch 2, 3, 4 | câu nối trong ghi chú diễn giả các trang lân cận viết lại |
| trung bình — vết chạy $N=2$ | thay bằng Ví dụ 01.7(b), tách trang bảng vết; E02 dùng vết $N=3$ | C17, C19, E02 | |
| trung bình — khối Mục 2.2–2.4 thiếu | B01 thêm số liệu ($1/10$, $10^9$ địa chỉ, 20 GB); thêm B17 (Ví dụ 01.4) và B18 (Định nghĩa 01.8, Ví dụ 01.5); B10 thành Định nghĩa 01.7; Tình huống 01.3 trong ghi chú diễn giả B18 | B01, B17, B10, B18 | |
| trung bình — recitation thiếu trang "Lời giải:" | thêm R02B, R03B, R05B cùng tiêu đề, lời giải khớp `exercises.md`; R01–R03 hỏi "điều Hệ quả 01.22 cho biết"; Hệ quả 01.22 trên R07 và F08; hướng dẫn chấm theo bước trong ghi chú diễn giả | R01–R05B, R07, F08 | |
| trung bình — nội dung ngoài ghi chú | rút cơ chế ngoài ghi chú khỏi mặt trang và ghi chú diễn giả (dây chuyền độ trễ, hoán vị MinHash, DCT, bước nhảy ngẫu nhiên, HITS, HNSW/PQ, FM/CM/DGIM, tính chất Bloom, "Không phải mọi chuỗi…"); các trang D giữ chức năng ER-004 bằng bảng phương pháp và thuộc tính của note:849–864; C10 dùng công thức CS246 note:708; E02 bỏ "Python hoặc C++" | C10–C13, D03–D10, B01, B03, E02 | giữ hình và ví dụ ER-003 của C11–C13 (vector, lương), A03 (đồ thị y, a, m); đề nghị bổ sung ghi chú ở báo cáo của tác tử sửa |
| trung bình — khoảng 30 câu xuất xứ, rào đón | xóa; giới hạn nêu bằng nguyên nhân hoặc bằng số (A07: $122{,}88$ TB) | ghi chú diễn giả toàn deck | xuất xứ ghi ở đoạn trên |
| trung bình — lời chú người soạn, đính chính nguồn | xóa; B09 dẫn DSC trang chiếu 40; C15 nguồn Princeton COS 597A; R04 dùng "giả thuyết làm việc" | B07, B08, B09, C13, C15, R04, R06 | |
| trung bình — P02 "Nhắc lại" và ký hiệu | dòng tiên quyết thường; "Nhắc lại:" mô hình RAM, $O$, trộn, bất biến; Ký hiệu thêm $F$, $M$, $L$ | P02 | 6 dòng, 56 âm tiết |
| nhẹ — G01 bảng tổng kết | hàng $F$; $2F$; $2mF$, $\le N(N-1)L$, "Xác minh ứng viên" với $\widehat R=A\cap R$ | G01 | |
| nhẹ — C15 thiếu định nghĩa | Định nghĩa 01.17 dạng công thức; độ thu hồi cặp ở C24 | C15, C24 | |
| nhẹ — câu định nghĩa C12 | theo note:625 | C12 | |
| nhẹ — ghi chú diễn giả trang tiêu đề mạch dài | CT 97, DT 80, FT 89 âm tiết; C05 bỏ câu chỉ đường | CT, DT, FT, C05 | |
| nhẹ — câu chỉ đường | xóa ở P04, GT, F04, D01, E02, D10, G03, C02, C03 | các trang nêu | P04 giữ ánh xạ dòng → mạch vì là chức năng của trang vấn đề trung tâm |
| nhẹ — no-ai-slop Detect (câu kết châm ngôn, phủ định, "có thể") | C12 "Báo chi phí xây dựng cùng độ trễ truy vấn."; F03, F01 theo đề xuất; C10 bỏ "có thể giảm"; D02 nêu năm chuỗi tiên quyết; câu cầu nối khuôn "Ngoài …, còn …" bỏ | C12, F03, F01, C10, D02, D03, D04 | |
| nhẹ — nhãn in đậm D03, D09 | *khóa*, *HNSW*, *lượng tử hóa tích* in nghiêng, kèm tên tiếng Anh | D03, D09 | |
| nhẹ — C17 thiếu dòng "Tính …" | thêm | C17, C19 | |
| nhẹ — `id="L01-…"` lộ mã | bỏ thuộc tính `id` của mọi trang nội dung | toàn deck | giữ `id="mach-N"` |
| nhẹ — A01 dùng $D$, $M$ byte | ghi chú diễn giả viết bằng lời | A01 | |
| nhẹ — D01, D02 thiếu CLO, chuỗi tiên quyết | D01 bảng CLO1–CLO4; D02 ghi chú diễn giả năm chuỗi | D01, D02 | |
| nhẹ — G03 tài liệu | BHK bản 04/01/2018; thêm CLRS 4e; liên kết `exercises.md`; dòng Bài 02 | G03 | |
| nhẹ — không dẫn số khối | dẫn số khối ghi chú trên các trang kết quả (tối đa một lần mỗi trang) và Bài tập 01.10, 01.11 | toàn deck | `refcheck.py 01`: 175 đúng, 0 sai |

**Kiểm G17** (máy chủ 8796, Chromium, `check_deck.py`): 100 trang, 7 section, 0 lỗi console, 0 request hỏng, 0 `.katex-error`, 0 `fragment`, không trùng mã, mọi trang có ghi chú diễn giả (40–250 âm tiết), không trang > 3 công thức hiển thị, `overflow_1600` rỗng, `hash_strand` đúng `mach-2…7`, không cuộn ngang ở 390 px; trang > 60 âm tiết đều thuộc loại trần 80 và có trong ngoại lệ của `storyboard.md`. `refcheck.py 01`: 175 đúng, 0 sai. Ảnh chụp 1600×900 của 34 trang mới hoặc sửa nhiều và 390×844 của 4 trang đã xem. `git diff --check` sạch.

### Lượt sửa sau kiểm lại (2026-11-13)

Căn cứ: danh sách điều phối viên đã duyệt sau hai lượt kiểm lại (`merge-01.md`: 3 trung bình, 12 nhẹ) và hai quyết định: giữ một dòng cơ chế mỗi trang `D05`–`D10` (ngoại lệ ER-004, G12); mạch 6 không cần trang mở có hình. Cùng tác tử sửa; không commit.

| mục | xử lý | trang |
|---|---|---|
| 1 [TB] thủ tục trộn thiếu điều kiện lặp | thêm dòng "Lặp khi cả hai con trỏ chưa hết danh sách"; dòng "Chứng minh." chuyển xuống ghi chú diễn giả; 50 âm tiết | C21 |
| 2 [nhẹ] $X_c$ ở trang Markov | trường hợp ba ngày chuyển xuống ghi chú diễn giả, viết $\mathbb E[X_c]$, $\Pr(X_c\ge1)$ | F08 |
| 3 [nhẹ] giả thiết Ví dụ 01.4 | "$\mu_1$ truy vấn đúng một lần, $\mu_2$ đúng hai lần; giữ độc lập mỗi bản ghi với xác suất $1/10$"; 59 âm tiết | B17 |
| 4 [nhẹ] hình ứng viên còn "hậu kiểm" | `title` "Ứng viên và xác minh", nhãn "Xác minh chính xác", `desc` theo; qua script `fix_deck_svg_2026_11_13.py`; `alt` của C16 theo | C16, `danh-gia-ung-vien.svg` |
| 5 [nhẹ] P02 nhắc lại trộn | "Nhắc lại: mô hình RAM, ký hiệu $O$; danh sách đã sắp tăng ngặt" | P02 |
| 6 [nhẹ] giả thiết Mệnh đề 01.15, 01.5 | C07 dòng Mô hình thêm "mọi $C_i$ trong bộ nhớ"; B16 "đọc mỗi khối đúng một lần" | C07, B16 |
| 7 [TB] thứ tự mạch 3 | C20 → C05 → C08…C14 → C21 → C07 → C16; ghi chú diễn giả C21 mở bằng câu nối note:630–632; C16 dẫn Ví dụ 01.8 (kho gấp đôi, số vòng tăng gần bốn lần) ngay sau C07; storyboard và bảng thời gian cập nhật (tổng mạch 3 giữ 37,5 phút) | mạch 3 |
| 8 [TB] câu thừa ở G01 | xóa câu "Bài chỉ đặc tả một thuật toán…"; lý do giữ ở storyboard | G01 |
| 9 [nhẹ] R07 và F08 | R07: một nhãn "Nhắc lại:" cho danh sách bốn ý, ý ba "$X$ là tổng chỉ báo trên các phép thử; $\mathbb E[X]$ bằng số phép thử nhân xác suất một phép thử"; F08: dòng "Ba ngày" chuyển xuống ghi chú diễn giả | R07, F08 |
| 10 [nhẹ] mô tả lời giải | R00, R02 thêm "cận Hệ quả 01.22" | R00, R02 |
| 11 [nhẹ] ghi chú diễn giả trang tiêu đề mạch | DT: mạch 3 kết thúc ở $R\subseteq A$ và độ thu hồi; GT: "kết quả của mạch 2–3"; FT nêu kết quả kế thừa (trách nhiệm khi diễn giải kết quả tính toán); FT 95 âm tiết | DT, GT, FT |
| 12 [nhẹ] câu chỉ đường, câu tập $C_i$ | F04 xóa câu mở; C01 "Giả sử các tập $C_i$ đã có sẵn; Bài 05 tạo chúng." | F04, C01 |
| 13 [nhẹ] ý lặp | "$\mathrm{SIM}\ge\tau$ chưa đủ … sao chép" chỉ còn ở E03 (D01 ô CLO4 đổi thành "báo cáo cả cặp bỏ sót"; F07 bỏ câu); "chạy nhanh không chứng minh cận" chỉ còn ở C00 (E06 bỏ; C00 bỏ ý "chạy đúng", E02 giữ); C00 dòng 1 thành "Bài toán phân tích: tìm cặp tài liệu gần trùng trong kho $N=10^6$ tài liệu." | C00, D01, E06, F07 |
| 14 [nhẹ] D02 | thêm "Nhắc lại: ba giới hạn đã gặp." trước danh sách | D02 |
| 15 [nhẹ] storyboard | tiêu đề trong bảng lấy từ mã nguồn (KaTeX giữ dạng `$…$`); cột lý do trỏ "phát hiện k" theo dòng 1–30 của bảng phát hiện; ghi quyết định mạch 6 và ngoại lệ ER-004 | `storyboard.md` |
| ER-004 | một dòng cơ chế: D08 (Định nghĩa 03.8), D09 (HNSW tìm tham lam theo tầng; PQ, Định nghĩa 07.27), D05 (Bloom, Định nghĩa 08.22), D10 (Flajolet–Martin, Định nghĩa 09.5), D06 (Huffman, Thuật toán 10.14), D07 (note:872); giữ mật độ (D08 48, D09 60, D05 59, D10 58, D06 50, D07 79 âm tiết) | D05–D10 |

Làm khác danh sách: mục 9, R07 không ghi "(Mệnh đề 01.20)" trên mặt trang vì trang đã có "(Hệ quả 01.22)" mà đề bài cần (tối đa một số hiệu mỗi trang, G4); Mệnh đề 01.20 ở ghi chú diễn giả.

**Kiểm G17 sau lượt sửa.** `check_deck.py 8796`: 100 trang, 7 section, console 0, request hỏng 0, `.katex-error` 0, trùng mã 0, ghi chú diễn giả 40–250, `disp_gt3` rỗng, `overflow_1600` rỗng, `hash_strand` đúng `mach-2…7`, không cuộn ngang 390 px; mọi trang > 60 âm tiết thuộc loại trần 80 và có trong ngoại lệ storyboard. `refcheck.py 01`: 184 đúng, 0 sai. `git diff --check` sạch. Ảnh chụp 1600×900 của C21, C16, D05, D06, D08, D09, D10, R07, C07 và 390×844 của D09 đã xem.

### Kiểm lại và duyệt của điều phối viên (2026-11-13)

**Tác tử (theo lời gọi công cụ).** Sửa deck: `general-purpose`, `opus` (Opus 5.5), effort `high`, `no-ai-slop` chế độ Edit; lượt sửa sau kiểm lại do cùng tác tử (tiếp tục bằng `SendMessage`). Kiểm lại vai A (độ chính xác và khớp ghi chú) và vai B (mạch, cấu trúc, văn phong, `no-ai-slop` Detect): mỗi vai một tác tử `general-purpose`, `opus` (Opus 5.5), effort `high`, chỉ đọc.

| vai | kết luận | phát hiện (chặn/nghiêm trọng/trung bình/nhẹ) | quyết định |
|---|---|---|---|
| A | cần sửa | 0/0/1/5 | chấp nhận; điều kiện lặp của thủ tục trộn ở C21 (note:633). Sáu mục vào `merge-01.md` (mục 1–6) |
| B | cần sửa | 0/0/3/8 | chấp nhận; thứ tự mạch 3 (trang tổng C05 liền các trang tiêu chí, theo ER-003 và note:614→637), câu lời người soạn ở G01, xung đột ER-004/G12 ở D05–D10. Chín mục vào `merge-01.md` (mục 7–15) |

Quyết định của điều phối viên trong lượt này: (1) ER-004 là yêu cầu rõ của người dùng, nên mỗi trang D05–D10 giữ một dòng cơ chế, viết bằng thuật ngữ và số khối của ghi chú bài sau (Định nghĩa 03.8, 07.27, 08.22, 09.5, Thuật toán 10.14; D07 theo note:872); phần ghi chú 01 chưa có câu cơ chế là đề nghị sửa ghi chú cho người dùng. (2) Mạch 6 không thêm trang mở có hình: F04 nhắc lại $N=10^6$ bằng số, hình cấu trúc chương quá nhỏ khi chiếu.

Lượt sửa sau kiểm lại: 15/15 mục làm; R07 dẫn "(Hệ quả 01.22)" trên mặt trang, Mệnh đề 01.20 trong ghi chú diễn giả (một số hiệu mỗi trang) — chấp nhận. Deck 83 → 100 trang (80 giảng, 120 phút; mạch 5 tám trang Đọc thêm không tính giờ; mạch 7 mười hai trang, 60 phút). Hai SVG không còn deck nào dùng (`giao-thoa-khai-pha-du-lieu.svg`, `the-tich-gan-bien.svg`) được giữ vì bản lưu trong `backups/lec-01/` còn dẫn.

Đề nghị sửa ghi chú để lại cho người dùng (chi tiết trong báo cáo tác tử sửa): ví dụ cho các trang tiêu chí của ER-003; câu cơ chế cho từng nhóm phương pháp ở Mục 4.1; hình Jaccard nhãn $C_1$, $C_2$.

Kiểm của điều phối viên sau lượt sửa: `check_deck.py` (Playwright, 1600×900 và 390×844) 100 trang, ID không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, 0 `.katex-error`, không tràn khung, không cuộn ngang ở 390 px, `#/2…7` mở đúng `mach-2…7`; mười tám trang trên 60 âm tiết đều thuộc loại trần 80 có ngoại lệ trong storyboard. `refcheck.py`: 184 dẫn chiếu, 0 sai. `git diff --check` sạch. Điều phối viên tự xem ảnh FT (nhãn Đọc thêm) và R07 (trang "Nhắc lại:" mở mạch 7) ở 1600×900. Thuộc tính `id="L01-…"` của các trang nội dung đã bỏ; không tệp nào liên kết tới (đã grep); trang tiêu đề mạch giữ `id="mach-N"`.

Quyết định: **chấp nhận**; mọi phát hiện của bảng 2026-11-13 đã đóng.
