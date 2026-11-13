# Dàn ý Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Phần deck viết lại ngày 2026-11-04 cùng bộ trang chiếu mới (109 trang sau lượt biên tập 1; 111 trang sau đợt sửa theo bảng phát hiện 2026-11-13), theo đặc tả K1–K9 của điều phối viên; các mục ghi chú (bảng thuật ngữ, bản đồ chủ đề, ghi chú bài giảng 2026-11-04) giữ nguyên.

## Phạm vi và mục tiêu

- Bài 09 theo thứ tự đề xuất của `sources/source.md`: **Dòng dữ liệu: đếm, mômen và cửa sổ**. Phần giảng 120 phút (96 trang), phần bài tập vận dụng 60 phút (15 trang từ 2026-11-13, phần dọc riêng).
- Đầu vào: Bài 08 (thuật toán dòng một lượt, hồ chứa, Bloom filter, hàm băm tất định), Bài 06 (Định lý 06.7), xác suất cơ bản (cận hợp, tuyến tính kỳ vọng, $1-z\le e^{-z}$).
- Sáu mục tiêu như ghi chú: đặc tả đại lượng và chọn phác thảo; Flajolet–Martin với ngưỡng hai phía và mẹo trung vị; biến AMS, $F_p$, hồ chứa vị trí; Count-Min và định cỡ $m$, $t$; DGIM với cận dưới $N$ bit, bộ nhớ $O(\log^2N)$, cận 50%, gộp dây chuyền; cửa sổ suy giảm và phần tử phổ biến. Sửa 2026-11-13: trang P02 viết lại theo động từ và đối tượng của sáu mục tiêu ghi chú (thêm $y_k$, $D_r$, phạm vi toàn dòng hay cửa sổ, dạng $F_p$, tính không chệch với hồ chứa, Markov và hàng độc lập, cận dưới $N$ bit, phép gộp đúng, ít hơn $1/(c\theta)$ điểm), 79 âm tiết.
- Ngoài phạm vi deck (chỉ ở ghi chú hoặc đọc thêm): HyperLogLog, giảm sai số DGIM và tổng số nguyên (Nhận xét 09.50), tình huống cỡ lân cận trong mạng xã hội (Tình huống 09.1), Count-Min cho dòng có cập nhật âm, cơ chế liệt kê phần tử nặng của UMass.

## Mạch của bộ trang chiếu

| N (`#/N`) | Tên mạch (trang Nội dung) | Trang tiêu đề mạch | Trang bài toán có hình | Mục ghi chú | Trang | Phút |
|---:|---|---|---|---|---:|---:|
| 1 | Mở đầu | P00 (trang bìa) | P04 `cau-truc-bai-09.svg` | Mục tiêu, Tiên quyết, Bảng ký hiệu, Mục 1 | 9 | 10 |
| 2 | Đếm phần tử phân biệt bằng Flajolet–Martin | FT, `id="mach-2"` | F01 `fm-bai-toan.svg` | Mục 2 | 18 | 25 |
| 3 | Mômen bậc hai và ước lượng AMS | MT, `id="mach-3"` | M01 `ams-hai-phan-bo.svg` | Mục 3 | 15 | 20 |
| 4 | Ước lượng tần suất bằng Count-Min Sketch | CT, `id="mach-4"` | C01 `cm-phan-tu-nang.svg` | Mục 4 | 15 | 18 |
| 5 | Cửa sổ trượt và cửa sổ suy giảm mũ | DT, `id="mach-5"` | D01 `dgim-bai-toan.svg`; cụm suy giảm E01 `suy-giam-hai-phim.svg` | Mục 5, Mục 6 | 32 | 39 |
| 6 | Tổng kết và tự kiểm tra | TT, `id="mach-6"` | T01 `nam-yeu-cau.svg` | Mục 7, Tình huống, Tóm tắt, Tham khảo | 7 | 8 |
| 7 | Bài tập vận dụng | XT, `id="mach-7"` | X01 `bai-4-4-1-dong.svg` | Bài tập 09.10, 09.11, 09.12, 09.20, 09.15, 09.16 | 15 | 60 |

Thứ tự trong mạch theo ghi chú: FM (đuôi băm → định nghĩa → thuật toán → bất biến → ngưỡng hai phía → phân phối đuôi nặng → gộp → mẹo trung vị → chi phí); AMS (biến → không chệch → $F_p$ → dòng chưa biết độ dài → chi phí); Count-Min (bài toán phần tử nặng → họ băm phổ dụng, Markov → bảng và cực tiểu → bảo đảm → chi phí); DGIM (cận dưới → thùng, sáu quy tắc, bộ nhớ → truy vấn, cận 50% → cập nhật, tính đúng, khấu hao); cửa sổ suy giảm (định nghĩa, truy hồi → phần tử phổ biến, số điểm). Chi tiết từng trang ở `storyboard.md`.

Dòng dẫn trang tiêu đề mạch: FT "Muốn đếm phần tử phân biệt bằng vài bit cho mỗi hàm băm, phải đọc cỡ của tập từ đuôi băm dài nhất."; MT "Muốn đo độ lệch của phân bố mà không giữ bộ đếm cho mọi phần tử, phải ước lượng từ một vị trí ngẫu nhiên."; CT "Muốn ước lượng tần suất bằng một bảng nhỏ, phải chấp nhận ước lượng thừa và chặn phần thừa theo xác suất."; DT "Muốn trả lời về phần gần đây của dòng, phải tóm tắt cửa sổ bằng thùng hoặc bằng trọng số giảm theo tuổi."; TT "Muốn chọn đúng phác thảo cho một câu hỏi, phải đối chiếu đại lượng, giả thiết và chi phí."; XT "Muốn vận dụng Flajolet–Martin, AMS, Count-Min và DGIM, phải chạy và kiểm giả thiết của chúng trên ví dụ của giáo trình." (sửa 2026-11-13)

## Nguồn và quyết định chọn theo cụm

| Cụm | Trục | Đối chiếu | Quyết định |
|---|---|---|---|
| Mở đầu | Ghi chú Mục 1; MMDS §4.1.2, §4.4.1, §4.5.1, Ví dụ 4.6–4.7 | Stanford CS246 2017, Streams 1, tr.13 | Quy mô URL $N=10^9$ theo Stanford (MMDS không có số cho URL) |
| Flajolet–Martin | MMDS §4.4, tr.142–145; trang chiếu MMDS phần 2, tr.17–25 | CS246 2017 Streams 2, tr.23–30; CS246 2026 tr.35–44 | Trình tự MMDS; thứ tự gộp trung bình nhóm rồi trung vị theo Stanford 2017 Streams 2, tr.30, vì trang chiếu MMDS tr.25 và CS246 2026 tr.44 đảo thứ tự; mẹo trung vị theo UMass bài 8 bằng phép đếm của ghi chú |
| AMS | MMDS §4.5, tr.145–150; phần 2, tr.27–36 | CS246 2017 Streams 2, tr.40–49 | Trình tự MMDS; "khoảng 100 biến" theo Stanford Streams 2, tr.49 (MMDS không nêu số) |
| Count-Min | UMass CS514 bài 10, trang chiếu 8–19 | BHK §6.2.1, Định lý 2.1 | Hình và ví dụ 104/78/90 theo UMass trang chiếu 16; thứ tự khối theo ghi chú (công cụ trước bảng); không dùng dòng `5,12,3,…` của UMass |
| DGIM | MMDS §4.6, tr.150–157; phần 1, tr.23–45 | CS246 2017 Streams 1, tr.11–25 | Trình tự MMDS, truy vấn trước cập nhật như ghi chú; theo Stanford: thùng là đoạn liên tục kết thúc ở bit 1 (tr.16–17), cận 50% có số hạng "+1" (tr.23, vì MMDS phần 1 tr.42 bỏ sót), trang số thùng (tr.24, MMDS không có); ví dụ dùng Hình 4.2/4.3 của sách, không dùng chuỗi của trang chiếu |
| Cửa sổ suy giảm | MMDS §4.7, tr.157–159; phần 2, tr.38–43 | CS246 2017 Streams 1, tr.27–32 | Trình tự MMDS; ví dụ dòng mưa $c=0{,}1$ theo Stanford Streams 1, tr.28 (MMDS không có ví dụ số) |
| Tổng kết | Ghi chú Mục 7, Ví dụ 09.20 | Stanford Streams 2, tr.32–38 (chỉ trong ghi chú diễn giả T07) | Không thêm khái niệm mới; tình huống cỡ lân cận trong đồ thị chỉ ở ghi chú |

Bảy chỗ chọn Stanford, có lý do ở cột cuối: (1) thứ tự gộp FM; (2) khoảng 100 biến AMS; (3) quy mô URL $N=10^9$; (4) thùng là đoạn liên tục; (5) cận 50% có "+1"; (6) trang số thùng; (7) ví dụ dòng mưa. Mọi hình vẽ lại bằng SVG; không chép CSS, phông, ảnh hay bảng màu của slide nguồn. Ghi công `http://www.mmds.org` ở trang bìa (ghi chú diễn giả) và trang Nguồn (T07).

## Bài tập vận dụng (recitation)

| Thứ tự | Bài sách | Bài tập | Trang | Phút |
|---:|---|---|---|---:|
| 1 | MMDS 4.4.1, §4.4.5, tr.145 | Bài tập 09.11 | X01 (đề, hình `bai-4-4-1-dong.svg`), X01B, X01C | 13 |
| 2 | MMDS 4.5.1, §4.5.6, tr.149 | Bài tập 09.10 | X02, X02B | 7 |
| 3 | MMDS 4.5.3, §4.5.6, tr.150 | Bài tập 09.12 | X03, X03B | 10 |
| 4 | BHK 6.7, §6.6, tr.204 | Bài tập 09.20 | X06, X06B (thêm 2026-11-13 cho mục tiêu 4) | 6 |
| 5 | MMDS 4.6.1, §4.6.8, tr.157 | Bài tập 09.15 | X04 (hình `dgim-bai-4-6-1.svg`), X04B | 11 |
| 6 | MMDS 4.6.3, §4.6.8, tr.157 | Bài tập 09.16 | X05 (hình `dgim-bai-4-6-3.svg`), X05B, X05C | 13 |

Đề giữ dữ kiện và yêu cầu của sách. Sửa 2026-11-13: đề X03 và X05 theo cấu trúc (a), (b) của `exercises.md` (Bài tập 09.12, 09.16); thêm Bài tập 09.20 vì mục tiêu 4 chưa có bài recitation. Mỗi trang đề ghi số bài, mục, trang; trang "Lời giải:" cùng tiêu đề; ghi chú diễn giả có gợi ý, lỗi thường gặp và hướng dẫn chấm 10 điểm theo bước của lời giải.

## Thuật ngữ và ký hiệu

Bảng theo bảng ký hiệu của ghi chú bài giảng (2026-11-04); mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu hoặc thuật ngữ | Nghĩa | Tiếng Anh |
|---|---|---|
| $x_i$; $r$ | phần tử ở vị trí (mốc thời gian) $i$; số phần tử đã đọc | timestamp |
| $\mathcal U$; $u$ | tập vũ trụ; một phần tử | universal set |
| $f_u$; $F_p$; $d=F_0$ | tần suất của $u$; mômen bậc $p$; số phần tử phân biệt | moment of order $p$; number of distinct elements |
| $F_2$ | số bất ngờ | surprise number |
| phác thảo | cấu trúc nhỏ cho ước lượng có bảo đảm | sketch |
| $h$; $L$; $\rho(\mathbf s)$; $R$ | hàm băm Flajolet–Martin; số bit giá trị băm; độ dài đuôi; độ dài đuôi lớn nhất | tail length, number of trailing zeros |
| $q$; $g$; $Y_j$; $\widehat d$ | số hàm băm; số nhóm ($g$ lẻ, chia hết $q$); ước lượng $2^{R_j}$; ước lượng gộp | median trick |
| $\xi$ | số ngẫu nhiên đều trên $\{1,\ldots,r\}$ của hồ chứa vị trí | |
| $s$; $I$; $v_i$; $X=r(2v_I-1)$ | số biến AMS và sức chứa hồ chứa vị trí; vị trí được chọn; số lần $x_i$ xuất hiện trong $x_i,\ldots,x_r$; biến AMS | AMS variable |
| phần tử nặng; $\kappa$; $\varepsilon$; $\delta$ | phần tử có $f_u\ge r/\kappa$; tham số sai số; xác suất thất bại | heavy hitter, frequent item |
| họ băm phổ dụng | $\Pr[h(u)=h(u')]\le1/m$ với $u\ne u'$ | universal hash family |
| $m$; $t$; $h_j$; $A_j$; $\widehat f_u$; $Z_j$ | số ô mỗi hàng; số hàng; hàm băm và mảng của hàng $j$; ước lượng Count-Min; nhiễu va chạm | Count-Min Sketch |
| cửa sổ trượt; $N$; $k$ | $N$ phần tử cuối; độ dài cửa sổ; độ dài hậu tố được hỏi | sliding window |
| thùng $b$; $\lvert b\rvert$; $\tau_b$ | đoạn vị trí liên tục của DGIM; số bit 1 trong thùng; mốc phải | bucket |
| $b^*$; $y_k$; $\widehat y_k$ | thùng cũ nhất có mốc phải trong $k$ vị trí cuối; số bit 1 thật; ước lượng DGIM | |
| $c$; $D_r$; $D_r(u)$; $\theta$ | hằng số suy giảm; giá trị cửa sổ suy giảm; điểm phổ biến của $u$; ngưỡng điểm | decay constant, exponentially decaying window, most popular elements |
| chi phí khấu hao; phương pháp thế năng | chi phí trung bình trên dãy thao tác; phân tích theo hàm thế | amortized cost; potential method |

## Kiểm kê hình của bộ trang chiếu

Mọi SVG sinh bằng `tools/courses/ds-foundation-algorithms/2627-1/img/lec-09/generate_deck_svg.py` (dùng lại hàm vẽ của `generate_svg.py`; không sửa sáu SVG của ghi chú). Mỗi tệp có `role="img"`, `<title>`, `<desc>`; trên trang có `alt` cụ thể; màu luôn kèm kiểu nét hoặc nhãn.

| Tệp | Trang | Nội dung, số liệu (từ ghi chú) |
|---|---|---|
| `cau-truc-bai-09.svg` | P04 | Biến thể của `cau-truc-chuong-09.svg` với số mạch 2–6 thay "Mục k" |
| `fm-bai-toan.svg` | F01 | Dòng IP của một trang → véc-tơ $2^{32}$ bit = 512 MiB; chiều cao không theo tỷ lệ (sinh lại 2026-11-13) |
| `fm-nguong-hai-phia-trang-chieu.svg` | F12 | Bản trang chiếu của `fm-nguong-hai-phia.svg` (Ví dụ 09.5), $\ell=0..16$, chữ lớn hơn |
| `ams-hai-phan-bo.svg` | M01 | Ví dụ 09.2: 910 và 8 110, cùng $F_0=11$ |
| `ams-ba-bien-trang-chieu.svg` | M03 | Bản trang chiếu của `ams-ba-bien.svg` (Ví dụ 09.7), nhãn vị trí lớn hơn |
| `cm-phan-tu-nang.svg` | C01 | §4.1: tần suất 5, 4, 3, 3; ngưỡng $r/\kappa=5$; b ở $r/\kappa-1$ |
| `cm-ba-o.svg` | C04 | Ví dụ 09.11 (UMass trang chiếu 16): 104, 78, 90 → 78 |
| `cm-bang-2x3.svg` | C06 | Ví dụ 09.12: phần tử băm vào mỗi ô theo $h_1$, $h_2$ |
| `dgim-bai-toan.svg` | D01 | Dòng bit $\mathbf 1[x_i=\mathrm a]$, cửa sổ 8 bit có 3 bit 1; 125 MB mỗi URL |
| `dgim-trang-thai-nen.svg` | D06 | Hình 4.2 (Ví dụ 09.14), không có đường truy vấn |
| `dgim-truy-van-10.svg` | D10 | Hình 4.2, đường $k=10$, $b^*=(4,r-8)$ viền đậm (Ví dụ 09.15) |
| `dgim-cap-nhat-trang-chieu.svg` | D15 | Bản trang chiếu của `dgim-cap-nhat.svg` (Ví dụ 09.16) |
| `suy-giam-hai-phim.svg` | E01 | Ví dụ 09.17: phim A 1 × 10 tuần, phim B 2 ở tuần hiện nay |
| `cua-so-suy-giam-trang-chieu.svg` | E03 | Bản trang chiếu của `cua-so-suy-giam.svg` (Định nghĩa 09.52, Nhận xét 09.54) |
| `nam-yeu-cau.svg` | T01 | Ví dụ 09.20, phần dữ kiện; cột phác thảo để dấu hỏi |
| `bai-4-4-1-dong.svg` | X01 | Bài tập 09.11: chín số → $h(x)=\alpha x+\beta\bmod32$ → chín ô 5 bit |
| `dgim-bai-4-6-1.svg` | X04 | Hình 4.2 với hai ranh giới $k=5$, $k=15$, không ghi đáp số |
| `dgim-bai-4-6-3.svg` | X05 | Hình 4.3 có mốc $r-25..r$, chú thích "có ít nhất một thùng cỡ 8" |

SVG cũ của deck 53 trang đã `git rm` (không còn tệp nào dẫn tới): `ams-trace.svg`, `count-min.svg`, `dgim-buckets.svg`, `dgim-query-10.svg`, `dgim-exercise.svg`, `dgim-cascade-exercise.svg`, `fm-trace.svg`, `window-weights.svg`. `decision-map.svg` chưa xóa: `planning/lec-01/storyboard.md` (dòng 229) còn ghi tên tệp này làm nguồn cho hình của Bài 01. Sáu SVG của ghi chú giữ nguyên; `cau-truc-chuong-09.svg`, `fm-nguong-hai-phia.svg`, `ams-ba-bien.svg`, `dgim-trang-thai.svg`, `dgim-cap-nhat.svg`, `cua-so-suy-giam.svg` chỉ ghi chú dùng.

Không có ảnh raster, mã trình diễn hay tài nguyên mạng cốt lõi.

## Bản đồ chủ đề ghi chú bài giảng

Theo bản đồ chủ đề của ghi chú (2026-11-04); thay bảng `L09-N01…N10` cũ.

| `note-topic-id` | Chủ đề | Nhãn | Mục | Nguồn | Sản phẩm |
|---|---|---|---|---|---|
| `lec-09-topic-01` | Kiến thức tiên quyết | cầu nối | Tiên quyết | Ghi chú Bài 08, 06, 05; BHK §12 | Phát biểu lại kết quả được dẫn |
| `lec-09-topic-02` | Năm câu hỏi, tần suất và mômen | cốt lõi | 1 | MMDS §4.5.1, Ví dụ 4.6–4.7; CS246 Streams 1 tr.13 | $f_u$, $F_p$, cửa sổ trượt, chi phí lời giải chính xác |
| `lec-09-topic-03` | Đếm chính xác và giới hạn bộ nhớ | cốt lõi; cận dưới tất định là bổ sung | 2.1 | MMDS §4.4.1; BHK §6.2.1 tr.183 | Nhu cầu ước lượng $F_0$ |
| `lec-09-topic-04` | Đuôi băm và ước lượng $2^R$ | cốt lõi | 2.2 | MMDS §4.4.2 | Chạy Flajolet–Martin; bất biến $R$ |
| `lec-09-topic-05` | Ngưỡng hai phía | cốt lõi; dạng bất đẳng thức là bổ sung | 2.3 | MMDS §4.4.2 tr.143 | Cận $1/\lambda$ và $e^{-\lambda/2}$ |
| `lec-09-topic-06` | Phân phối đuôi nặng và gộp nhiều hàm băm | cốt lõi; cận kỳ vọng và mẹo trung vị là bổ sung | 2.4 | MMDS §4.4.3; UMass bài 8 tr.3–5 | Trung bình trong nhóm rồi trung vị; cận $(4\eta)^{q/2}$ |
| `lec-09-topic-07` | Chi phí, hợp nhất, thực hành | cốt lõi | 2.5 | MMDS §4.4.4; UMass bài 8 tr.8 | Bộ nhớ theo bit; ghép phác thảo bằng max |
| `lec-09-topic-08` | Biến AMS | cốt lõi | 3.1 | MMDS §4.5.2, Ví dụ 4.8 | Chạy biến AMS |
| `lec-09-topic-09` | Tính không chệch | cốt lõi; tổng các số lẻ là cầu nối | 3.2 | MMDS §4.5.3, Bài tập 4.5.5 | $\mathbb E[X]=F_2$ |
| `lec-09-topic-10` | Mômen bậc cao | cốt lõi, chu trình rút gọn vì cùng chứng minh với Định lý 09.22 | 3.3 | MMDS §4.5.4 | Ước lượng $F_p$ |
| `lec-09-topic-11` | AMS trên dòng chưa biết độ dài | cốt lõi; bất biến và hệ quả trung bình là bổ sung | 3.4–3.5 | MMDS §4.5.5; Định lý 08.17 | Hồ chứa vị trí; trung bình không chệch |
| `lec-09-topic-12` | Bài toán phần tử nặng | cốt lõi, chu trình rút gọn vì là đặc tả | 4.1 | UMass bài 10 tr.8–11 | Bài toán $(\varepsilon,\kappa)$ |
| `lec-09-topic-13` | Họ băm phổ dụng, bất đẳng thức Markov | cầu nối | 4.2 | UMass bài 10 tr.14; BHK §6.2.1 tr.184–185 | Cận va chạm, Markov |
| `lec-09-topic-14` | Bảng Count-Min | cốt lõi | 4.3 | UMass bài 10 tr.12–16 | Cập nhật, truy vấn cực tiểu |
| `lec-09-topic-15` | Bảo đảm Count-Min | cốt lõi; cận hợp cho mọi phần tử là bổ sung | 4.4 | UMass bài 10 tr.17–19 | Sai số $\varepsilon r/\kappa$ với xác suất $\delta$; chọn $m$, $t$ |
| `lec-09-topic-16` | Cận dưới $N$ bit | cốt lõi | 5.1 | MMDS §4.6.1 | Lời giải chính xác cần $N$ bit |
| `lec-09-topic-17` | Thùng, sáu quy tắc, bộ nhớ | cốt lõi; chứng minh số thùng là bổ sung | 5.2 | MMDS §4.6.2–4.6.3, Hình 4.2 | $O(\log^2N)$ bit |
| `lec-09-topic-18` | Truy vấn và cận 50% | cốt lõi | 5.3 | MMDS §4.6.3–4.6.4; CS246 Streams 1 tr.23 | $\tfrac12y_k\le\widehat y_k\le\tfrac32y_k$ |
| `lec-09-topic-19` | Cập nhật DGIM | cốt lõi; tính đúng và khấu hao là bổ sung | 5.4 | MMDS §4.6.5, Hình 4.3; CLRS 4e Ch.16 | Gộp dây chuyền; khấu hao một lượt gộp mỗi bit 1 |
| `lec-09-topic-20` | Mở rộng DGIM | đọc thêm | 5.5 | MMDS §4.6.6–4.6.7 | Giảm sai số; tổng số nguyên |
| `lec-09-topic-21` | Cửa sổ suy giảm | cốt lõi; tổng hữu hạn là cầu nối | 6.1 | MMDS §4.7.1–4.7.2; CS246 Streams 1 tr.28 | Truy hồi $D_r$; tổng $<1/c$ |
| `lec-09-topic-22` | Phần tử phổ biến hiện thời | cốt lõi; chứng minh cận là bổ sung | 6.2 | MMDS §4.7.3 | Ít hơn $1/(c\theta)$ điểm |
| `lec-09-topic-23` | Chọn phác thảo theo câu hỏi | cốt lõi | 7 | Tổng hợp Mục 2–6 | Hai bảng đối chiếu; Ví dụ 09.20 |
| `lec-09-topic-24` | Tình huống áp dụng và ứng dụng | cốt lõi | Tình huống | CS246 2017 Streams 2 tr.32–38; Streams 1 tr.13; MMDS §4.5.5 | Ba tình huống, một vi phạm giả thiết |
| `lec-09-topic-25` | Tóm tắt chương | cốt lõi | Tóm tắt | — | Chuỗi kết quả; nối Bài 10 |
| `lec-09-topic-26` | Bài tập củng cố | cốt lõi | Bài tập | MMDS Bài 4.4.1, 4.4.2, 4.5.1–4.5.6, 4.6.1, 4.6.3; BHK Bài 6.7 | Ba mức, sáu bài vận dụng trên lớp (từ 2026-11-13) |
| `lec-09-topic-27` | Đọc thêm và tài liệu | đọc thêm | Tham khảo | UMass bài 8; BHK §6.2; trang chiếu MMDS | HyperLogLog, thuật toán Frequent |

Quan hệ tiên quyết: Mục 1 là đầu vào của mọi mục; Mục 3 dùng phép gộp của Mục 2.4 và Định lý 08.17; Mục 4 dùng cận hợp và bất đẳng thức Markov; Mục 5 chỉ cần Mục 1 và mô hình dòng của Bài 08; Mục 6 mở từ giới hạn của cửa sổ trượt ở Mục 5; mọi nhánh gặp nhau ở Mục 7.

## Ghi chú bài giảng 2026-11-04

- Các mục về deck ở đầu tệp đã được viết lại theo bộ trang chiếu mới (2026-11-04); deck là bản tóm lược của ghi chú, cùng thứ tự, ký hiệu, ví dụ và số hiệu kết quả.
- Thứ tự mục của ghi chú: năm câu hỏi (Mục 1) → Flajolet–Martin → AMS → Count-Min → DGIM → cửa sổ suy giảm → chọn phác thảo. AMS đứng trước Count-Min vì $F_2$ không chỉ ra phần tử nặng, nên Count-Min nhận nhu cầu từ giới hạn của AMS; deck cũ đặt Count-Min trước AMS.
- Nguồn: MMDS là trục cho Flajolet–Martin, AMS, DGIM và cửa sổ suy giảm; Count-Min theo UMass CS514 bài 10, vì MMDS không trình bày; BHK §6.2.1 cho cận dưới đếm chính xác và họ độc lập từng cặp; Stanford CS246 2017 cho bài toán URL, ví dụ dòng mưa và Tình huống 09.1.
- Bỏ Count-Min cho cập nhật âm và các ví dụ tự dựng cũ của deck; dữ liệu tính tay của ghi chú được ghi ở quy ước nguồn trong bảng ký hiệu.
- Ghi chú có 57 khối đánh số chung, 20 ví dụ, 3 tình huống, 9 bài tập cuối mục (09.1–09.9) và sáu SVG trong `img/lec-09/`; 10 bài tập củng cố 09.10–09.19 (năm bài MMDS dùng cho phần vận dụng trên lớp) nằm trong `materials/lec-09/exercises.md`.
