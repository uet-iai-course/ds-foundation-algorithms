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
2. AT → A05 → A00 → A02 → A06 (cập nhật 2026-10-28): ví dụ ba truy vấn trên dòng cảm biến (MMDS Hình 4.1, Ví dụ 4.1; quy mô §4.1.2); định nghĩa thuật toán dòng và mô hình hệ thống; chi phí ba truy vấn theo từng phần tử (mô hình từ máy); bài tập trạng thái của phương sai (câu hỏi của học phần). Bỏ A01 (gộp vào A00) và A03; A04 chuyển sang mạch 3 thành K01B.
3. K00, K01, K01B, K02–K08: lấy mẫu nhất quán theo khóa; K01B là bảng giữ/bỏ theo người dùng (MMDS §4.2.2), chuyển từ mạch 2 ngày 2026-10-28.
4. R00, R01, R03, R02, R04–R08: vấn đề → phân biệt → chạy tay → đặc tả → thuật toán và chứng minh hồ chứa.
5. B00, B02, B05, B01, B03–B12: tình huống → vị trí hệ thống → ví dụ → đặc tả → thuật toán, bảo đảm và xác suất dương giả.
6. C00–C02: chọn cấu trúc theo câu hỏi, nguồn và phạm vi.
7. X00–X05: bốn bài tập trực tiếp từ MMDS (Ex.4.2.1 tr.138; Ex.4.3.1–4.3.2 tr.141; Ex.4.3.3 tr.142).

## Thuật ngữ và ký hiệu

Các dòng $x_i$, $W$, $r$, $S$, $m$, $k$ cập nhật theo quyết định ký hiệu 2026-10-28; trang Tiên quyết và quy ước (P04) đặt các ký hiệu này. Các dòng còn lại cập nhật khi duyệt mạch dùng chúng.

| Ký hiệu | Nghĩa |
|---|---|
| $x_1,x_2,\ldots$ | phần tử của dòng; không dùng $x$ cho nghĩa khác |
| $t$, $K(t)$ | một bộ trên dòng và khóa của bộ |
| $a/b$ | tỷ lệ khóa cần lấy mẫu |
| $h(K)<a$ | điều kiện chọn khi $h$ có miền $0,\ldots,b-1$; $h$ phải phân bố đều trên toàn miền để tỷ lệ $a/b$ được bảo đảm |
| $s$ | sức chứa hồ chứa, $s\ge1$ |
| $W$ | mảng hồ chứa $W[1..s]$ (thay $S$ cũ, từ 2026-10-28) |
| $r$ | số phần tử đã đọc, tính cả phần tử vừa đến; dùng chung cho mô hình dòng và hồ chứa |
| $S$ | tập khóa của Bloom filter |
| $n$ | số bit của mảng Bloom |
| $m$ | số khóa được đưa vào Bloom filter, $m=\lvert S\rvert$ |
| $k$ | số hàm băm của Bloom filter; khác khóa $K$ |
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
| lấy mẫu hồ chứa | reservoir sampling |
| Bloom filter (còn gọi là bộ lọc Bloom) | Bloom filter |
| dương giả | false positive |
| âm giả | false negative |

## Kiểm kê nội dung và hình

- Định nghĩa: mô hình dòng, mẫu theo khóa, mẫu hồ chứa, Bloom filter.
- Thuật toán: `LẤY-MẪU-THEO-KHÓA`, `HỒ-CHỨA`, `XÂY-BLOOM`, `KIỂM-TRA-BLOOM`.
- Chứng minh: tính nhất quán theo khóa; quy nạp xác suất $s/r$; điều kiện không âm giả.
- Phân tích: $\Theta(s)$ bộ nhớ hồ chứa; $\Theta(km)$ xây và $\Theta(k)$ truy vấn Bloom; mật độ bit hữu hạn $q$ chính xác dưới băm iid, FPR $q^k$ là xấp xỉ chuẩn và dạng mũ là xấp xỉ khi $n$ lớn.
- Bài tập: X01 dùng giả thiết lược đồ `Grades` với định danh university duy nhất toàn cục; đáp án và rubric là lời giải giảng viên suy ra từ đề, không in trong sách.
- SVG tự vẽ: mô hình dòng (`mo-hinh-dong.svg`, thay `stream-model.svg` trên deck từ 2026-10-28; bản cũ còn trong ghi chú), bảng giữ/bỏ theo người dùng (`bang-theo-nguoi-dung.svg`), mẫu theo khóa, vết hồ chứa, ví dụ Bloom 11 bit, luồng kiểm tra Bloom, đường cong FPR.
- Không dùng ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.

## Bản đồ chủ đề cho ghi chú tự học

Cập nhật 2026-10-28 theo báo cáo rà ghi chú và quyết định ký hiệu cùng ngày: mã `L08-N01`…`L08-N11` không hợp lệ với viewer (`TOPIC_ID_PATTERN` chỉ nhận chữ thường) nên thay bằng `lec-08-topic-01`…`lec-08-topic-17`. Ghi chú được viết lại thành chương giáo trình theo từng mạch; bảng dưới là bản đồ đích, đã đặt trong phần đầu chương của `lecture-note.md`. Mục ghi chú: 1 Mô hình dòng một lượt; 2 Lấy mẫu theo khóa; 3 Lấy mẫu hồ chứa; 4 Lọc thành viên bằng Bloom filter; 5 Chọn cấu trúc theo đầu ra; rồi Tình huống, Tóm tắt, Bài tập củng cố, Tham khảo.

| `note-topic-id` | Nhãn | Mục ghi chú | Chủ đề | Sản phẩm | Mã cũ |
|---|---|---|---|---|---|
| `lec-08-topic-01` | cầu nối | Tiên quyết | Kiến thức tiên quyết | Hai bài toán dòng của ghi chú Bài 01; hàm băm tất định (ghi chú Bài 05, Mục 9, 11; hàm phân phối Bài 02); cách phân tích Định lý 06.7; công cụ xác suất, Jensen; $(1-1/c)^c\to e^{-1}$, $1-z\le e^{-z}$, Bernoulli, hàm lõm, cực trị; quy nạp và bất biến (ghi chú Bài 05, Mục 10; Mệnh đề 06.5) | — |
| `lec-08-topic-02` | cốt lõi | 1 | Mô hình dòng một lượt | đặc tả chung và bốn trục chi phí | N01 |
| `lec-08-topic-03` | cốt lõi | 2.1 | Sai lệch của lấy mẫu từng bộ | tỷ số $d/(10u+19d)$ so với $d/(u+d)$ | N02 |
| `lec-08-topic-04` | cốt lõi; kích thước mẫu kỳ vọng là bổ sung | 2.2 | Mẫu nhất quán theo khóa | quy tắc $h(K(t))<a$, thuật toán, tính nhất quán, xác suất $a/b$ | N03 |
| `lec-08-topic-05` | cốt lõi | 2.3 | Chọn khóa theo đơn vị thống kê | quy trình ba bước; dẫn tới Bài tập 4.2.1 | N03 (tách) |
| `lec-08-topic-06` | cầu nối | 2.4 | Ngưỡng băm khi ngân sách cố định | hạ $\tau$ mà không lưu quyết định cũ; bất biến của mẫu | N04 |
| `lec-08-topic-07` | cốt lõi | 3.1–3.3 | Đặc tả và thuật toán hồ chứa | vết $s=2$, giả mã trên $W$ | N05 |
| `lec-08-topic-08` | cốt lõi; số lần ghi kỳ vọng là bổ sung | 3.4–3.5 | Xác suất $s/r$ và chi phí hồ chứa | chứng minh quy nạp, chi phí | N05 (tách) |
| `lec-08-topic-09` | cốt lõi | 4.1–4.3 | Cơ chế Bloom filter | xây, truy vấn, ví dụ 11 bit | N06 |
| `lec-08-topic-10` | cốt lõi | 4.4 | Không âm giả | bốn điều kiện và phản ví dụ | N07 |
| `lec-08-topic-11` | cốt lõi; cận dưới $q^k\le p_{FP}$ là bổ sung | 4.5 | Mật độ bit và xác suất dương giả | phân biệt chính xác với xấp xỉ | N08 |
| `lec-08-topic-12` | cốt lõi; định cỡ cho 1% là bổ sung | 4.6 | Số hàm băm tối ưu | dẫn xuất và làm tròn $k^*$ | N09 |
| `lec-08-topic-13` | cốt lõi | 5 | Chọn cấu trúc theo đầu ra | ánh xạ đầu ra sang trạng thái | N10 |
| `lec-08-topic-14` | cốt lõi | Tình huống | Tình huống áp dụng | bài toán giải trọn, một tình huống vi phạm giả thiết | — |
| `lec-08-topic-15` | cốt lõi | Tóm tắt | Tóm tắt chương | chuỗi kết quả, giả thiết hay bị bỏ quên, sang Bài 09 | — |
| `lec-08-topic-16` | cốt lõi | Bài tập | Bài tập củng cố | ba mức, gồm bốn bài MMDS của mạch 7 | N11 |
| `lec-08-topic-17` | đọc thêm | Tham khảo | Đọc thêm và tài liệu | ánh xạ mục ↔ nguồn; lấy mẫu có trọng số (Blum–Hopcroft–Kannan §6.1) | — |

Đồ thị tiên quyết: `topic-01→topic-02`; nhánh khóa `02→03→04→05→06`; nhánh hồ chứa `02→07→08` (08 so với 04); nhánh Bloom `02→09→10→11→12`; ba nhánh hội tụ ở `13`, rồi `14→15`; `16` dùng mọi chủ đề trước; `17` cuối chương. Chu trình rút gọn: `05` (quy trình), `06` (cầu nối, một mệnh đề bất biến), `13` (tổng hợp). Các nhãn "bổ sung" trong cột Nhãn chờ điều phối viên duyệt khi viết mục tương ứng.

Ký hiệu của ghi chú theo quyết định ký hiệu của điều phối viên ngày 2026-10-28 và bảng "Thuật ngữ và ký hiệu" ở trên, thêm: $\mathcal K$ (miền khóa), $b$ thường cho số giá trị của $h$ (kể cả ở ngưỡng §4.2.4, thay $B$ của MMDS), $\tau$, $u$, $d$, $j$, $B[0..n-1]$, $y$, $X$ (số bit 1), $p(k)$, $k^*$. Biến phụ của chứng minh $k^*$ chưa chốt: đề xuất cũ $u=e^{-z}$ trùng $u$ (truy vấn đơn) nên phải chọn chữ khác khi viết Mục 4.6.

## Tên mạch và trang tiêu đề mạch (2026-10-14)

Mỗi mạch trừ mạch mở đầu mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên trùng từng chữ với trang Nội dung. Deck 55 trang; 56 trang sau khi thêm P04 ngày 2026-10-28.

| N | Tên mạch | Trang tiêu đề mạch | Trang nội dung đầu mạch |
|---:|---|---|---|
| 1 | Mở đầu | P00 (trang bìa) | P04 (Tiên quyết và quy ước), rồi P02, P03, P01 |
| 2 | Mô hình tính toán trên dòng | AT | A00 |
| 3 | Lấy mẫu theo khóa | KT | K00 |
| 4 | Lấy mẫu hồ chứa | RT | R00 |
| 5 | Lọc thành viên bằng Bloom filter | BT | B00 |
| 6 | Tổng kết và chuyển tiếp | CT | C00 |
| 7 | Bài tập vận dụng | XT | X00 |
