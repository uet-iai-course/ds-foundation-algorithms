# Dàn ý Bài 8

## Phạm vi và mục tiêu

- Bài 8 theo thứ tự đề xuất trong `sources/source.md`: **Dòng dữ liệu: mô hình, lấy mẫu và lọc**.
- Đối tượng: sinh viên năm hai, đã học lập trình, toán rời rạc, đại số tuyến tính, xác suất cơ bản và Bài 01–07 (băm, bất biến vòng lặp).
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Sản phẩm học tập (mục tiêu trên deck, cập nhật 2026-10-28): (1) đặc tả thuật toán dòng một lượt và chọn khóa lấy mẫu cho một thống kê theo nhóm; (2) lập vết hồ chứa và chứng minh bằng quy nạp mỗi phần tử đã đọc còn trong mẫu với xác suất $s/r$ khi $r\ge s$; (3) xây dựng và truy vấn Bloom filter, tính xác suất nhận nhầm khóa ngoài $S$ và số hàm băm tối ưu.
- Ngoài phạm vi: Rejection Sampling, Flajolet–Martin, moment, DGIM, cửa sổ trượt và suy giảm theo thời gian.

## Luận đề và vấn đề trung tâm (2026-10-28)

- Câu luận đề (P00): «Băm khóa giữ trọn nhóm, hồ chứa giữ mẫu cỡ cố định, mảng bit loại hầu hết khóa ngoài tập.»
- Vấn đề trung tâm (P01). Nhu cầu: lấy mẫu, lọc dòng chưa biết độ dài, không lưu cả dòng. Câu trả lời có điều kiện:
  1. Mạch 2: đọc một lần nên chỉ trả lời từ trạng thái giữ lại.
  2. Mạch 3: hàm băm đều giữ trọn mỗi người dùng với xác suất $1/10$; mẫu có $\approx r/10$ bộ, tức tăng theo dòng.
  3. Mạch 4: với số ngẫu nhiên đều, độc lập, hồ chứa giữ mỗi phần tử đã đọc với xác suất $s/r$ khi $r\ge s$.
  4. Mạch 5: Bloom filter $8\cdot10^9$ bit, sáu hàm băm đều, độc lập, không loại khóa nào của $10^9$ khóa, nhận nhầm $\approx2\%$ (xấp xỉ mũ $(1-e^{-6/8})^6\approx0{,}0216$; số 6 do học phần chọn).
- Số liệu: MMDS §4.2.1 tr.136; §4.3.1 tr.139.

## Nguồn

| Vai trò | Tệp | Phạm vi dùng |
|---|---|---|
| Giáo trình, nguồn chuẩn | `sources/textbooks/mmds/ch4-mining-data-streams.pdf` | mục 4.1–4.3; bài tập 4.2.1 và 4.3.1–4.3.3 |
| Slide chính | `sources/reference-slides/mmds/ch04-streams1.pdf` | mô hình dòng, lấy mẫu theo khóa, hồ chứa |
| Slide chính | `sources/reference-slides/mmds/ch04-streams2.pdf` | Bloom filter và phân tích |
| Đối chiếu | `sources/reference-slides/stanford-cs246/16-streams.pdf` | bản CS246 ngày 26/02/2026; phép đếm K01 và đường cong B11 (tr.31–32) |
| Đối chiếu | `sources/reference-slides/stanford-cs246-2017/streams-2.pdf` | bản Jeffrey D. Ullman tạo ngày 01/03/2017; ví dụ Bloom 11 bit B05 |

MMDS được ưu tiên ở mọi cụm. Stanford được dùng tại K01 vì phép đếm số truy vấn phân biệt rõ hơn, tại B05 vì có trọn vết 11 bit và tại B11 để đối chiếu hình dạng đường cong. Mọi công thức được kiểm chứng bằng sách; ví dụ B05 giữ nguyên dữ kiện nguồn. Ghi công: <http://www.mmds.org>.

## Mạch phần giảng

1. P00 → P04 → P02 → P03 → P01 (cập nhật 2026-10-28): bìa có câu luận đề; tiên quyết và quy ước; mục tiêu học tập; nội dung và đọc trước; vấn đề trung tâm với câu trả lời có điều kiện của mạch 2–5 (số liệu MMDS tr.133, 136, 139).
2. AT → A08 → A05 → A00 → A07 → A02 → A06 (cập nhật 2026-10-29: A08 «Truy vấn trên dòng cảm biến» là trang bài toán đầu mạch, hình `bai-toan-cam-bien.svg`; A05 đổi tiêu đề thành «Ví dụ: trạng thái của ba truy vấn»; cập nhật 2026-10-28; A07 thêm ở lượt biên tập theo bản đánh giá giảng dạy): ví dụ ba truy vấn trên dòng cảm biến (MMDS Hình 4.1, Ví dụ 4.1; quy mô §4.1.2); định nghĩa thuật toán dòng và mô hình hệ thống; định nghĩa trạng thái, phép cập nhật, phép trả lời và vết cửa sổ 4 số trên $1,5,2,7,4$ (hình `trang-thai-cap-nhat.svg`); chi phí ba truy vấn theo từng phần tử (mô hình từ máy); bài tập trạng thái của phương sai (câu hỏi của học phần). Bỏ A01 (gộp vào A00) và A03; A04 chuyển sang mạch 3 thành K01B.
3. KT → K15 → K10 → K01 → K11 → K09 → K01B → K02 → K12 → K13 → K04 → K14 → K05 → K06 → K07 → K08 (động lực và khó khăn, 2026-10-29: thêm K15 «Mẫu cho truy vấn tức thời» (hình `mau-truy-van-tuc-thoi.svg`; truy vấn thường trực như giá trị lớn nhất, phương sai có trạng thái riêng cỡ hằng; nghiên cứu người dùng điển hình bằng truy vấn tức thời, chưa biết khi bộ đến; không dựng được trạng thái riêng, không lưu được cả dòng, nên cần mẫu $1/10$ đại diện cho cả dòng; hình có ba câu hỏi: tỷ lệ lặp của người dùng điển hình, số truy vấn của mỗi người trong tháng, câu hỏi chưa biết trước; MMDS §4.1.3, tr.134 và §4.2.1, tr.136); K10 nêu khó khăn chính trên mặt trang (hai bản “đồ thị” ở $r=1$ và $r=4$, bộ $r=1$ phải được quyết định khi đến vì giữ tạm mọi bộ là lưu cả dòng; hình `bai-toan-ty-le-lap.svg` thay hai thanh ngân sách bằng vị trí $r$, ngoặc nối hai bản và khối ràng buộc); K02 mở bằng «Nhu cầu:» mọi bộ của một người nhận cùng quyết định, không lưu nhãn theo người, rồi giới hạn của bảng nhãn ($10^8$ người, 1,6 GB); câu nhắc Bài 02 chuyển vào ghi chú GV; KT đổi lời dẫn và cụm khóa. Trước đó, sửa theo phản hồi người dùng 2026-10-29, lượt mạch 3: thêm K11 «Ví dụ: tỷ lệ lặp trên mẫu từng bộ» (100 người như An, $1/29$), K12 «Ví dụ: chọn hàm băm trước dòng» (họ $h_\omega(\text{tên})=(\text{mã}+\omega)\bmod10$, mã An 7, Bình 4, Chi 1, $\omega=3$), K13 «Khóa, ngăn và ngưỡng» (hình `ngan-va-nguong.svg`, $a=1$ và $a=3$), K14 vết thuật toán với $a=5$ trên năm bộ, cùng tiêu đề K04; đại lượng ước lượng là tỷ lệ lặp của người dùng điển hình (MMDS §4.2.1); truy vấn mẫu "băm" đổi thành "đệ quy"; K07 bỏ câu hạ ngưỡng khỏi mặt trang. Cập nhật 2026-10-29 trước đó: K10 «Tỷ lệ truy vấn lặp trên mẫu» là trang bài toán đầu mạch, hình `bai-toan-ty-le-lap.svg`; K01 mở bằng phương án giữ từng bộ; cập nhật 2026-10-28): ví dụ ba bộ của An (cây xác suất hai bộ “đồ thị”, hình `cay-hai-bo-do-thi.svg`, thêm ở lượt biên tập theo bản đánh giá giảng dạy); sai lệch tổng quát $d/(10u+19d)$; bảng giữ/bỏ theo người dùng (MMDS §4.2.2); hàm băm thay bảng; thuật toán với đặc tả; tính đúng; chọn khóa (MMDS §4.2.3); chi phí và hạ ngưỡng (MMDS §4.2.4); câu hỏi ngưỡng. Tỷ lệ $1/10$ ($b=10$, $a=1$) xuyên mạch. Bỏ K00, gộp K03 vào K04.
4. RT → R00 → R10 → R01 → R03 → R04 → R05 → R06 → R07 → R08 → R09 (cập nhật 2026-10-29): mẫu cỡ cố định (giới hạn có số, hai ứng dụng có nguồn); ba cách trực tiếp và khó khăn chính (R10, bảng so sánh); ý tưởng so với mẫu theo khóa; vết hai ô; thuật toán với đặc tả, mảng $W$; tính đúng và hai nửa bước quy nạp; chi phí; so sánh với mẫu theo khóa và câu hỏi kiểm. Gộp R02 vào R04.
5. BT → B00 → B02 → B05 → B05A → B05B → B01 → B03 → B04 → B06 → B07 → B08 → B09 → B10 → B11 → B12 (cập nhật 2026-10-28; B05A, trang câu hỏi kiểm tra 118 và 29, thêm ở lượt biên tập theo bản đánh giá giảng dạy): giới hạn lưu $S$; ý tưởng và nhận xét bit 0; ví dụ 11 bit thêm ba khóa và kiểm tra hai khóa (một dương giả); đặc tả và định nghĩa dương giả/âm giả; giả mã; không có âm giả; xác suất một bit bằng 1 và xác suất dương giả; ảnh hưởng của $k$; $k^*$; ví dụ tám bit mỗi khóa; chi phí.
6. CT → C06 → C00 → C03 → C01 → C04 → C05 → C02 (cập nhật 2026-10-29: C06 «Hai dòng và ba câu hỏi» là trang bài toán đầu mạch, hình `hai-dong-ba-cau-hoi.svg`; C01 bỏ dòng mở trùng; cập nhật 2026-10-28): kết quả và giả thiết không được bỏ; thuật toán, bảo đảm và chi phí; câu trả lời cho vấn đề trung tâm có số; câu hỏi tự kiểm tra (hai trang, phủ ba mục tiêu); nguồn và tài liệu đọc, liên kết ghi chú bài giảng và Bài 09.

Thời lượng phần giảng (2026-10-29, sau lượt động lực và khó khăn của mạch 4): mạch 4 giữ 24 phút (R10 2 mới; R01 2,5 → 2; R03 3 → 2,5; R04 3,5 → 3; R06 2,5 → 2); các mạch khác không đổi; tổng 120 phút; phần bài tập 60 phút. Trước đó, thời lượng phần giảng (2026-10-29, sau lượt động lực và khó khăn của mạch 3): mạch 3 giữ 27 phút (K15 1,5 mới; K01B 2 → 1,5; K09 1,5 → 1; K05 2 → 1,5); các mạch khác không đổi; tổng 120 phút; phần bài tập 60 phút. Trước đó, thời lượng phần giảng (2026-10-29, sau lượt sửa mạch 3): mạch 1 6,5; mạch 2 13; mạch 3 27; mạch 4 24 (R01 2,5); mạch 5 37,5 (B04 2; B09 2; B11 2); mạch 6 12 (C03 2); tổng 120 phút; phần bài tập 60 phút. Trước lượt này: Thời lượng phần giảng (2026-10-29, sau khi thêm trang bài toán đầu mạch): mạch 1 6,5; mạch 2 13 (A08 1,5; A05 1,5; A00 2,5); mạch 3 24,5 (K10 1,5; K01 2,5; K01B 2); mạch 4 24,5 (R09 2,5); mạch 5 39 (B03 2); mạch 6 12,5 (C06 1; C01 1,5); tổng 120 phút. Phần bài tập 60 phút (không đổi). Trước đó (2026-10-28): mạch 1 6,5; mạch 2 13; mạch 3 24; mạch 4 25; mạch 5 39,5 (thêm B05A 2 phút; B05B bớt 1,5, B10 và B12 bớt mỗi trang 0,5); mạch 6 12.
7. XT → X01 → X01B → X02 → X02B → X03 → X03B → X04 → X04B → X04C (cập nhật 2026-10-28, lượt biên tập theo bản đánh giá giảng dạy): bốn bài tập trực tiếp từ MMDS (Ex.4.2.1 tr.138; Ex.4.3.1–4.3.2 tr.141; Ex.4.3.3 tr.142), tiêu đề "Bài tập: <chủ đề>"; mỗi đề có trang lời giải kế tiếp cùng tiêu đề, nhãn "Lời giải:" (X01B, X02B, X03B); lời giải Ex.4.3.3 tách hai trang ", điểm dừng" (X04B) và ", xét dấu" (X04C); hình `chia-mang-bit.svg` dựng đề Ex.4.3.2. Phần bài tập 60 phút: XT 0,5; X01 12; X01B 2,5; X02 8; X02B 2; X03 12; X03B 3; X04 11; X04B 4,5; X04C 4,5.

## Thuật ngữ và ký hiệu

Các dòng $x_i$, $W$, $r$, $S$, $m$, $k$ cập nhật theo quyết định ký hiệu 2026-10-28; trang Tiên quyết và quy ước (P04) đặt các ký hiệu này. Các dòng còn lại cập nhật khi duyệt mạch dùng chúng.

| Ký hiệu | Nghĩa |
|---|---|
| $x_1,x_2,\ldots$ | phần tử của dòng; không dùng $x$ cho nghĩa khác |
| $t$, $K(t)$ | một bộ trên dòng và khóa của bộ |
| $u$, $d$ | số truy vấn tìm kiếm xuất hiện một lần, hai lần trong phép đếm sai lệch (MMDS viết $s$ cho $u$) |
| $\tau$ | ngưỡng khi hạ tỷ lệ để giữ ngân sách (chỉ trong ghi chú; MMDS §4.2.4 viết $t$) |
| $a/b$ | tỷ lệ khóa cần lấy mẫu |
| $h(K)<a$ | điều kiện chọn khi $h$ có miền $0,\ldots,b-1$; $h$ phải phân bố đều trên toàn miền để tỷ lệ $a/b$ được bảo đảm |
| $b$, $a$ | số ngăn (giá trị của $h$, ngăn không chứa dữ liệu) và ngưỡng: giữ khi $h(K)<a$ |
| $\omega$ | tham số chọn hàm trong họ ví dụ $h_\omega(\text{tên})=(\text{mã}+\omega)\bmod10$, rút đều một lần trước dòng (vai hạt giống); không dùng $c$ vì $c$ là giá trị băm và chỉ số bit |
| $s$ | sức chứa hồ chứa, $s\ge1$ |
| $W$ | mảng hồ chứa $W[1..s]$ (thay $S$ cũ, từ 2026-10-28) |
| $j$ | số nguyên rút đều trong $\{1,\ldots,r\}$, độc lập với lịch sử |
| $r$ | số phần tử đã đọc, tính cả phần tử vừa đến; dùng chung cho mô hình dòng và hồ chứa |
| $S$ | tập khóa của Bloom filter |
| $n$ | số bit của mảng Bloom |
| $m$ | số khóa được đưa vào Bloom filter, $m=\lvert S\rvert$ |
| $k$ | số hàm băm của Bloom filter; khác khóa $K$ |
| $y$ | khóa truy vấn của Bloom filter; $v$ là khóa của $S$ trong giả mã xây |
| $p(k)$ | dạng mũ $(1-e^{-km/n})^k$, xấp xỉ của $p_{FP}$ |
| $k^*$ | $(n/m)\ln2$ |
| $q$ | mật độ bit 1 chính xác dưới mô hình $km$ phép băm iid: $q=1-(1-1/n)^{km}$ |
| $p_{FP}$ | xác suất dương giả; $q^k$ là xấp xỉ chuẩn và dạng mũ $(1-e^{-km/n})^k$ là xấp xỉ khi $n$ lớn |

### Thuật ngữ Việt–Anh

| Thuật ngữ | Tiếng Anh |
|---|---|
| dòng dữ liệu | data stream |
| trạng thái (dữ liệu giữ lại giữa hai lần đọc) | state |
| truy vấn thường trực | standing query |
| truy vấn tức thời | ad-hoc query |
| bộ nhớ làm việc | working store |
| kho lưu trữ | archival store |
| bộ đệm vòng | ring buffer |
| từ máy | machine word |
| lấy mẫu theo khóa | sampling by key (MMDS §4.2.3, "key") |
| ngăn (giá trị của hàm băm, không chứa dữ liệu) | bucket (MMDS §4.2.2) |
| ngưỡng | threshold |
| người dùng điển hình | typical user (MMDS §4.2.1) |
| lấy mẫu hồ chứa | reservoir sampling |
| Bloom filter (còn gọi là bộ lọc Bloom) | Bloom filter |
| dương giả | false positive |
| âm giả | false negative |

## Kiểm kê nội dung và hình

- Định nghĩa: mô hình dòng, mẫu theo khóa, mẫu hồ chứa, Bloom filter.
- Thuật toán: `LẤY-MẪU-THEO-KHÓA`, `HỒ-CHỨA`, `XÂY-BLOOM`, `KIỂM-TRA-BLOOM`.
- Chứng minh: tính nhất quán theo khóa; quy nạp xác suất $s/r$; điều kiện không âm giả.
- Phân tích: $\Theta(s)$ bộ nhớ hồ chứa; $\Theta(km)$ xây và $\Theta(k)$ truy vấn Bloom; mật độ bit hữu hạn $q$ chính xác dưới băm iid, FPR $q^k$ là xấp xỉ chuẩn và dạng mũ là xấp xỉ khi $n$ lớn.
- Bài tập: X01 dùng giả thiết lược đồ `Grades` với định danh university duy nhất toàn cục; lời giải và tiêu chí đối chiếu do học phần suy ra từ đề, ghi trong speaker notes; sách không in lời giải.
- SVG tự vẽ trong `img/lec-08/` (24 tệp, cập nhật 2026-10-29, thêm `ngan-va-nguong.svg` và `mau-truy-van-tuc-thoi.svg`; `stream-model.svg`, `key-sampling.svg`, `bloom-11bit.svg` đã xóa, không trang nào dùng): cấu trúc chương (`cau-truc-chuong.svg`, chỉ ghi chú); trang bài toán đầu mạch (2026-10-29, hiện chỉ deck): ba truy vấn trên dòng cảm biến và bộ nhớ (`bai-toan-cam-bien.svg`, A08), dòng năm bộ có vị trí $r$, tỷ lệ lặp của An, ngoặc nối hai bản “đồ thị” và khối ràng buộc giữ hoặc bỏ khi bộ đến (`bai-toan-ty-le-lap.svg`, K10 và ghi chú §2); chọn mẫu lúc dòng chạy, hỏi mẫu bằng truy vấn tức thời về sau (`mau-truy-van-tuc-thoi.svg`, K15 và ghi chú §2), mẫu cỡ cố định trên dòng a, x, c, y, z, k, c (`bai-toan-mau-co-dinh.svg`, R00), $S$ so với bộ nhớ chính và phép tra đĩa (`bai-toan-loc-thu.svg`, B00), hai dòng và ba câu hỏi (`hai-dong-ba-cau-hoi.svg`, C06), mã chỉ duy nhất trong một trường (`grades-hai-truong.svg`, X01); mô hình dòng (`mo-hinh-dong.svg`, deck A00 và ghi chú); trạng thái và phép cập nhật, cửa sổ 4 số (`trang-thai-cap-nhat.svg`, deck A07 và ghi chú); cây xác suất hai bộ “đồ thị” (`cay-hai-bo-do-thi.svg`, deck K01 và ghi chú); bảng giữ/bỏ theo người dùng (`bang-theo-nguoi-dung.svg`, K01B); hàm băm thay bảng (`bam-theo-nguoi-dung.svg`, K02); vết hồ chứa (`reservoir-trace.svg`, R03), vết hồ chứa thu nhỏ (`reservoir-mini.svg`, chỉ deck R04), một bước của hồ chứa (`reservoir-step.svg`, R06); luồng kiểm tra Bloom (`bloom-pipeline.svg`, B02); Bloom 11 bit thêm ba khóa (`bloom-11bit-them.svg`, B05), mảng trơn cho câu hỏi (`bloom-11bit-mang.svg`, chỉ deck B05A), mảng đánh dấu bit của 118 và 29 (`bloom-11bit-mini.svg`, B05B); bốn phi tiêu vào tám bia (`phi-tieu-8-bia.svg`, B07); đường cong xác suất dương giả có vạch $k^*$ và nhãn hai vùng (`fpr-curve.svg`, B11); một mảng chung và bốn mảng chia (`chia-mang-bit.svg`, X03). Hình có trong cả deck và ghi chú trừ khi ghi "chỉ deck" hoặc "chỉ ghi chú".
- Không dùng ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.

## Bản đồ chủ đề cho ghi chú tự học

Cập nhật 2026-10-28 theo báo cáo rà ghi chú và quyết định ký hiệu cùng ngày: mã `L08-N01`…`L08-N11` không hợp lệ với viewer (`TOPIC_ID_PATTERN` chỉ nhận chữ thường) nên thay bằng `lec-08-topic-01`…`lec-08-topic-17`. Ghi chú được viết lại thành chương giáo trình theo từng mạch; bảng dưới là bản đồ đích, đã đặt trong phần đầu chương của `lecture-note.md`. Mục ghi chú: 1 Mô hình dòng một lượt; 2 Lấy mẫu theo khóa; 3 Lấy mẫu hồ chứa; 4 Lọc thành viên bằng Bloom filter; 5 Chọn cấu trúc theo câu hỏi; rồi Tình huống áp dụng và ứng dụng, Tóm tắt chương, Bài tập củng cố, Hướng dẫn đọc thêm và tài liệu tham khảo. Toàn chương đã viết ngày 2026-10-28.

| `note-topic-id` | Nhãn | Mục ghi chú | Chủ đề | Sản phẩm | Mã cũ |
|---|---|---|---|---|---|
| `lec-08-topic-01` | cầu nối | Tiên quyết | Kiến thức tiên quyết | Hai bài toán dòng của ghi chú Bài 01; hàm băm tất định (ghi chú Bài 05, Mục 9, 11; hàm phân phối Bài 02); cách phân tích Định lý 06.7; công cụ xác suất, Jensen; $(1-1/c)^c\to e^{-1}$, $1-z\le e^{-z}$, Bernoulli, hàm lõm, cực trị; quy nạp và bất biến (ghi chú Bài 05, Mục 10; Mệnh đề 06.5) | — |
| `lec-08-topic-02` | cốt lõi | 1 | Mô hình dòng một lượt | đặc tả chung và bốn trục chi phí | N01 |
| `lec-08-topic-03` | cốt lõi | 2.1 | Sai lệch của lấy mẫu từng bộ | tỷ số $d/(10u+19d)$ so với $d/(u+d)$ | N02 |
| `lec-08-topic-04` | cốt lõi; kích thước mẫu kỳ vọng là bổ sung | 2.2, 2.4 | Mẫu nhất quán theo khóa | quy tắc $h(K(t))<a$, thuật toán, tính nhất quán, xác suất $a/b$ | N03 |
| `lec-08-topic-05` | cốt lõi | 2.3 | Chọn khóa theo đơn vị thống kê | quy trình ba bước; dẫn tới Bài tập 4.2.1 | N03 (tách) |
| `lec-08-topic-06` | cầu nối | 2.5 | Ngưỡng băm khi ngân sách cố định | hạ $\tau$ mà không lưu quyết định cũ; bất biến của mẫu | N04 |
| `lec-08-topic-07` | cốt lõi | 3.1–3.2 | Đặc tả và thuật toán hồ chứa | vết $s=2$, giả mã trên $W$ | N05 |
| `lec-08-topic-08` | cốt lõi; mọi tập con đồng khả năng (Mệnh đề 08.18) và số lần ghi kỳ vọng là bổ sung | 3.3–3.5 | Xác suất $s/r$ và chi phí hồ chứa | chứng minh quy nạp, chi phí | N05 (tách) |
| `lec-08-topic-09` | cốt lõi | 4.1–4.3 | Cơ chế Bloom filter | xây, truy vấn, ví dụ 11 bit | N06 |
| `lec-08-topic-10` | cốt lõi | 4.4 | Không âm giả | bốn điều kiện và phản ví dụ | N07 |
| `lec-08-topic-11` | cốt lõi; cận dưới $q^k\le p_{FP}$ là bổ sung | 4.5 | Mật độ bit và xác suất dương giả | phân biệt chính xác với xấp xỉ | N08 |
| `lec-08-topic-12` | cốt lõi | 4.6–4.7 | Số hàm băm tối ưu | dẫn xuất và làm tròn $k^*$ | N09 |
| `lec-08-topic-13` | cốt lõi | 5.1–5.2 | Chọn cấu trúc theo câu hỏi | hai bảng đối chiếu, quy trình ba bước, trả lời vấn đề trung tâm | N10 |
| `lec-08-topic-14` | cốt lõi | Tình huống | Tình huống áp dụng và ứng dụng | ba tình huống, Tình huống 08.3 vi phạm giả thiết; ứng dụng ở Bài 09 | — |
| `lec-08-topic-15` | cốt lõi | Tóm tắt | Tóm tắt chương | chuỗi kết quả, giả thiết hay bị bỏ quên, sang Bài 09 | — |
| `lec-08-topic-16` | cốt lõi | Bài tập | Bài tập củng cố | ba mức: nhận biết 08.6–08.9 (câu tự kiểm C04–C05), tính toán hoặc chứng minh 08.10–08.12 (MMDS 4.3.1–4.3.3), vận dụng 08.13 (MMDS 4.2.1) và 08.14 (hồ chứa cho từng khóa, MMDS tr.150) | N11 |
| `lec-08-topic-17` | đọc thêm | Tham khảo | Hướng dẫn đọc thêm và tài liệu tham khảo | ánh xạ mục ↔ nguồn (MMDS §4.1–4.3, §4.5.5, slide Streams 1–2, CS246 2026, Ullman 2017, CLRS §2.1); ghi công http://www.mmds.org; đọc tiếp Bài 09, Blum–Hopcroft–Kannan §6.1 | — |

Đồ thị tiên quyết: `topic-01→topic-02`; nhánh khóa `02→03→04→05→06`; nhánh hồ chứa `02→07→08` (08 so với 04); nhánh Bloom `02→09→10→11→12`; ba nhánh hội tụ ở `13`, rồi `14→15`; `16` dùng mọi chủ đề trước; `17` cuối chương. Chu trình rút gọn: `05` (quy trình), `06` (cầu nối, một mệnh đề bất biến), `13` (tổng hợp). Các nhãn "bổ sung" trong cột Nhãn chờ điều phối viên duyệt khi viết mục tương ứng.

Ký hiệu của ghi chú theo quyết định ký hiệu của điều phối viên ngày 2026-10-28 và bảng "Thuật ngữ và ký hiệu" ở trên, thêm: $\mathcal K$ (miền khóa), $b$ thường cho số giá trị của $h$ (kể cả ở ngưỡng §4.2.4, thay $B$ của MMDS), $\tau$, $u$, $d$, $j$, $B[0..n-1]$, $y$, $X$ (số bit 1), $p(k)$, $k^*$. Biến phụ của chứng minh $k^*$ chưa chốt: đề xuất cũ $u=e^{-z}$ trùng $u$ (truy vấn đơn) nên phải chọn chữ khác khi viết Mục 4.6.

## Tên mạch và trang tiêu đề mạch (2026-10-14)

Mỗi mạch trừ mạch mở đầu mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên trùng từng chữ với trang Nội dung. Deck 58 trang sau lượt duyệt từng mạch; 59 trang sau khi thêm A07, 60 trang sau khi thêm B05A, 64 trang sau khi thêm X01B, X02B, X03B, X04C (lượt biên tập theo bản đánh giá giảng dạy, 2026-10-28); 67 trang sau khi thêm A08, K10, C06 (trang bài toán đầu mạch, 2026-10-29); 71 trang sau khi thêm K11, K12, K13, K14; 72 trang sau khi thêm K15 (động lực của mạch 3, 2026-10-29); 73 trang sau khi thêm R10 (động lực và khó khăn của mạch 4, 2026-10-29).

| N | Tên mạch | Trang tiêu đề mạch | Trang nội dung đầu mạch |
|---:|---|---|---|
| 1 | Mở đầu | P00 (trang bìa) | P04 (Tiên quyết và quy ước), rồi P02, P03, P01 |
| 2 | Mô hình tính toán trên dòng | AT | A08 |
| 3 | Lấy mẫu theo khóa | KT | K15 (động lực), rồi K10 (bài toán) |
| 4 | Lấy mẫu hồ chứa | RT | R00 |
| 5 | Lọc thành viên bằng Bloom filter | BT | B00 |
| 6 | Tổng kết và chuyển tiếp | CT | C06 |
| 7 | Bài tập vận dụng | XT | X01 |
