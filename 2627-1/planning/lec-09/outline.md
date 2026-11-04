# Dàn ý Bài 9

## Phạm vi và mục tiêu

- Bài 9 theo thứ tự đề xuất: **Dòng dữ liệu: đếm, mômen và cửa sổ**.
- Phần giảng 120 phút; phần bài tập củng cố 60 phút.
- Đầu vào kiến thức: mô hình dòng, hàm băm, xác suất cơ bản, kỳ vọng và lấy mẫu hồ chứa từ Bài 8.
- Sản phẩm: chọn phác thảo theo đại lượng cần ước lượng; chạy và giải thích Flajolet–Martin, Count-Min Sketch, AMS và DGIM; nêu bảo đảm cùng điều kiện áp dụng; cập nhật một tổng suy giảm mũ.
- Ngoài phạm vi: cơ chế HyperLogLog chuẩn, biến thể DGIM sai số tùy ý, Count-Min cho dòng có cập nhật âm và thuật toán tự sinh danh sách khóa nặng.

## Nguồn và quyết định chọn

| Cụm | Khớp chuẩn đầu ra | Độ chính xác và tính hiện thời | Ví dụ hoặc hình | Khả năng Việt hóa | Nguồn được chọn và lý do |
|---|---|---|---|---|---|
| Đếm phân biệt | MMDS và Stanford đều khớp $F_0$. | Sách MMDS và Stanford 2017 cho đúng thứ tự gộp; MMDS Streams 2 tr.25 và Stanford 2026 tr.44 đảo thứ tự. | MMDS có vết băm và bài tập trực tiếp. | Ký hiệu ngắn, dễ vẽ lại. | Sách MMDS tr.142–145 làm chuẩn; Stanford 2017 Streams 2 kiểm tra thứ tự trung bình trong nhóm rồi trung vị giữa nhóm. |
| Count-Min Sketch | Không có trong MMDS Chương 4 hoặc các slide Stanford được ánh xạ. | UMass nêu đầy đủ miền băm, khuếch đại xác suất và tham số khóa nặng. | Có cơ chế va chạm và lập luận Markov. | Có thể Việt hóa mà giữ tên thuật toán. | Chỉ dùng UMass CS514 Lecture 10 với $m=\lceil2k/\varepsilon\rceil$, $t=\lceil\log_2(1/\delta)\rceil$; không trộn dạng tham số khác. |
| Mômen và AMS | Cả hai nguồn khớp $F_2$ và tính không chệch. | Sách MMDS nêu đầy đủ biến hậu tố và chứng minh. | MMDS có ví dụ 910/8110 và vết ba vị trí. | Thuận lợi, ký hiệu nhất quán với sách. | MMDS tr.146–150 làm trục; Stanford 2017 chỉ đối chiếu. |
| DGIM | Cả hai nguồn khớp đếm bit 1 trong hậu tố. | Sách MMDS xác định sáu bất biến và cận 50%; Stanford diễn đạt cập nhật dễ theo dõi. | Hình 4.2 và 4.3 của MMDS nối trực tiếp với bài tập. | Phải vẽ lại mốc phải và phần trái chưa xác định. | MMDS tr.151–157 làm trục; Stanford 2017 Streams 1 tr.13–24 dùng để kiểm tra diễn đạt cập nhật/truy vấn. |
| Cửa sổ suy giảm | Cả hai nguồn khớp ý giảm trọng số theo tuổi. | Sách MMDS cho định nghĩa, tổng hữu hạn và truy hồi. | Hình 4.4 đủ cho so sánh với cửa sổ cứng. | Dễ Việt hóa. | MMDS tr.157–159 làm chuẩn; Stanford 2017 Streams 1 tr.27–29 đối chiếu. |

MMDS được ưu tiên khi hai nguồn tương đương. Slide Stanford 2017 được dùng để kiểm tra thứ tự gộp FM và cách diễn đạt DGIM; không sao chép giao diện hoặc tài sản. Ghi công: <http://www.mmds.org>.

Tệp `umass-cs514/lecture8-hyperloglog.pdf` chỉ đủ cho FM/LogLog, không mô tả đầy đủ HyperLogLog chuẩn. Deck chỉ nêu HyperLogLog là hướng mở rộng.

## Mạch phần giảng

1. P00–A02: mở bài, tình huống dòng sự kiện và bản đồ chọn cấu trúc, 8 phút.
2. F00–F06: Flajolet–Martin, 22 phút.
3. C00–C04: Count-Min Sketch rút gọn, 14 phút.
4. M00–M07: mômen bậc hai và AMS, 25 phút.
5. D00–D09: cửa sổ bit và DGIM, 36 phút.
6. E00–T01: cửa sổ suy giảm mũ rồi kết luận bằng bảng tổng hợp bảo đảm và giới hạn, 15 phút.

Tổng phần giảng: **120 phút**.
Sáu mạch giảng và một mạch bài tập tạo đúng bảy `<section>` ngoài.

## Bài tập củng cố

| Bài | Nguồn | Phút |
|---|---|---:|
| X01 | MMDS Ex.4.4.1, tr.145 | 12 |
| X02 | MMDS Ex.4.5.1, tr.150 | 8 |
| X03 | MMDS Ex.4.5.3, tr.150 | 12 |
| X04 | MMDS Ex.4.6.1, tr.157 | 12 |
| X05 | MMDS Ex.4.6.3, tr.157 | 16 |

Tổng phần bài tập: **60 phút**. X00 chỉ mở phần, không tính thời lượng.

## Thuật ngữ và ký hiệu

Bảng theo bảng ký hiệu của ghi chú bài giảng (2026-11-04); mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu hoặc thuật ngữ | Nghĩa | Tiếng Anh |
|---|---|---|
| $x_i$; $r$ | phần tử ở vị trí (mốc thời gian) $i$; số phần tử đã đọc | timestamp |
| $\mathcal U$; $u$ | tập vũ trụ; một phần tử | universal set |
| $f_u$; $F_p$; $d=F_0$ | tần suất của $u$; mômen bậc $p$; số phần tử phân biệt | moment of order $p$; number of distinct elements |
| $F_2$ | số bất ngờ | surprise number |
| phác thảo | cấu trúc nhỏ cho ước lượng có bảo đảm | sketch |
| $h$; $L$; $\rho(y)$; $R$ | hàm băm Flajolet–Martin; số bit giá trị băm; độ dài đuôi; độ dài đuôi lớn nhất | tail length, number of trailing zeros |
| $q$; $g$; $Y_j$; $\widehat d$ | số hàm băm; số nhóm ($g$ lẻ, chia hết $q$); ước lượng $2^{R_j}$; ước lượng gộp | median trick |
| $s$; $I$; $v_i$; $X=r(2v_I-1)$ | số biến AMS và sức chứa hồ chứa vị trí; vị trí được chọn; số lần $x_i$ xuất hiện trong $x_i,\ldots,x_r$; biến AMS | AMS variable |
| phần tử nặng; $\kappa$; $\varepsilon$; $\delta$ | phần tử có $f_u\ge r/\kappa$; tham số sai số; xác suất thất bại | heavy hitter, frequent item |
| họ băm phổ dụng | $\Pr[h(u)=h(u')]\le1/m$ với $u\ne u'$ | universal hash family |
| $m$; $t$; $h_j$; $A_j$; $\widehat f_u$; $Z_j$ | số ô mỗi hàng; số hàng; hàm băm và mảng của hàng $j$; ước lượng Count-Min; nhiễu va chạm | Count-Min Sketch |
| cửa sổ trượt; $N$; $k$ | $N$ phần tử cuối; độ dài cửa sổ; độ dài hậu tố được hỏi | sliding window |
| thùng $b$; $\lvert b\rvert$; $\tau_b$ | đoạn vị trí liên tục của DGIM; số bit 1 trong thùng; mốc phải | bucket |
| $b^*$; $y_k$; $\widehat y_k$ | thùng cũ nhất có mốc phải trong $k$ vị trí cuối; số bit 1 thật; ước lượng DGIM | |
| $c$; $D_r$; $D_r(u)$; $\theta$ | hằng số suy giảm; giá trị cửa sổ suy giảm; điểm phổ biến của $u$; ngưỡng điểm | decay constant, exponentially decaying window, most popular elements |
| chi phí khấu hao; phương pháp thế năng | chi phí trung bình trên dãy thao tác; phân tích theo hàm thế | amortized cost; potential method |

## Kiểm kê hình và nội dung

- Chín SVG tự vẽ: bản đồ quyết định; vết FM; bảng Count-Min; vết AMS; trạng thái DGIM nền; truy vấn DGIM $k=10$; bài tập DGIM $k=5,15$; trạng thái đầu cho chuỗi gộp; so sánh trọng số cửa sổ.
- Thuật toán: FM, Count-Min, AMS và cập nhật/truy vấn DGIM; truy hồi cửa sổ suy giảm.
- Lập luận: ngưỡng FM dưới mô hình băm lý tưởng; cảnh báo đuôi nặng; nhiễu kỳ vọng, Markov và khuếch đại Count-Min; tính không chệch AMS; bất biến, chi phí và cận sai số DGIM.
- Không có ảnh raster, mã trình diễn hoặc tài nguyên mạng cốt lõi.

## Bản đồ chủ đề ghi chú bài giảng

Theo bản đồ chủ đề của ghi chú (2026-11-04); thay bảng `L09-N01…N10` cũ.

| `note-topic-id` | Chủ đề | Nhãn | Mục | Nguồn | Sản phẩm |
|---|---|---|---|---|---|
| `lec-09-topic-01` | Kiến thức tiên quyết | cầu nối | Tiên quyết | Ghi chú Bài 08, 06, 05; BHK §12 | Phát biểu lại kết quả được dẫn |
| `lec-09-topic-02` | Năm câu hỏi, tần suất và mômen | cốt lõi | 1 | MMDS §4.5.1, Ví dụ 4.6–4.7; CS246 Streams 1 tr.13 | $f_u$, $F_p$, cửa sổ trượt, chi phí lời giải chính xác |
| `lec-09-topic-03` | Đếm chính xác và giới hạn bộ nhớ | cốt lõi; cận dưới tất định là bổ sung | 2.1 | MMDS §4.4.1; BHK §6.2.1 tr.183 | Nhu cầu ước lượng $F_0$ |
| `lec-09-topic-04` | Đuôi băm và ước lượng $2^R$ | cốt lõi | 2.2 | MMDS §4.4.2 | Chạy Flajolet–Martin; bất biến $R$ |
| `lec-09-topic-05` | Ngưỡng hai phía | cốt lõi; dạng bất đẳng thức là bổ sung | 2.3 | MMDS §4.4.2 tr.143 | Cận $1/\lambda$ và $e^{-\lambda/2}$ |
| `lec-09-topic-06` | Đuôi nặng và gộp ước lượng | cốt lõi; cận kỳ vọng và mẹo trung vị là bổ sung | 2.4 | MMDS §4.4.3; UMass bài 8 tr.3–5 | Trung bình trong nhóm rồi trung vị; cận $(4\eta)^{q/2}$ |
| `lec-09-topic-07` | Chi phí, hợp nhất, thực hành | cốt lõi | 2.5 | MMDS §4.4.4; UMass bài 8 tr.8 | Bộ nhớ theo bit; ghép phác thảo bằng max |
| `lec-09-topic-08` | Biến AMS | cốt lõi | 3.1 | MMDS §4.5.2, Ví dụ 4.8 | Chạy biến AMS |
| `lec-09-topic-09` | Tính không chệch | cốt lõi; tổng các số lẻ là cầu nối | 3.2 | MMDS §4.5.3, Bài tập 4.5.5 | $\mathbb E[X]=F_2$ |
| `lec-09-topic-10` | Mômen bậc cao | cốt lõi, chu trình rút gọn | 3.3 | MMDS §4.5.4 | Ước lượng $F_p$ |
| `lec-09-topic-11` | AMS trên dòng chưa biết độ dài | cốt lõi; bất biến và hệ quả trung bình là bổ sung | 3.4–3.5 | MMDS §4.5.5; Định lý 08.17 | Hồ chứa vị trí; trung bình không chệch |
| `lec-09-topic-12` | Bài toán phần tử nặng | cốt lõi, chu trình rút gọn | 4.1 | UMass bài 10 tr.8–11 | Bài toán $(\varepsilon,\kappa)$ |
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
| `lec-09-topic-26` | Bài tập củng cố | cốt lõi | Bài tập | MMDS Bài 4.4.1, 4.4.2, 4.5.1–4.5.6, 4.6.1, 4.6.3 | Ba mức, năm bài vận dụng trên lớp |
| `lec-09-topic-27` | Đọc thêm và tài liệu | đọc thêm | Tham khảo | UMass bài 8; BHK §6.2; trang chiếu MMDS | HyperLogLog, thuật toán Frequent |

Quan hệ tiên quyết: Mục 1 là đầu vào của mọi mục; Mục 3 dùng phép gộp của Mục 2.4 và Định lý 08.17; Mục 4 dùng cận hợp và bất đẳng thức Markov; Mục 5 chỉ cần Mục 1 và mô hình dòng của Bài 08; Mục 6 mở từ giới hạn của cửa sổ trượt; mọi nhánh gặp nhau ở Mục 7.

## Ghi chú bài giảng 2026-11-04

- Các mục về deck (mạch phần giảng, bài tập theo mã trang, tên mạch, kiểm kê hình của deck) phản ánh deck cũ cho tới khi deck được làm lại.
- Thứ tự mục của ghi chú: năm câu hỏi (Mục 1) → Flajolet–Martin → AMS → Count-Min → DGIM → cửa sổ suy giảm → chọn phác thảo. AMS đứng trước Count-Min vì $F_2$ không chỉ ra phần tử nặng, nên Count-Min nhận nhu cầu từ giới hạn của AMS; deck cũ đặt Count-Min trước AMS.
- Nguồn: MMDS là trục cho Flajolet–Martin, AMS, DGIM và cửa sổ suy giảm; Count-Min theo UMass CS514 bài 10, vì MMDS không trình bày; BHK §6.2.1 cho cận dưới đếm chính xác và họ độc lập từng cặp; Stanford CS246 2017 cho bài toán URL, ví dụ dòng mưa và Tình huống 09.1.
- Bỏ Count-Min cho cập nhật âm và các ví dụ tự dựng cũ của deck; dữ liệu tính tay của ghi chú được ghi ở quy ước nguồn trong bảng ký hiệu.
- Ghi chú có 57 khối đánh số chung, 20 ví dụ, 3 tình huống, 19 bài tập (năm bài MMDS dùng cho phần vận dụng trên lớp) và sáu SVG trong `img/lec-09/`.

## Tên mạch và trang tiêu đề mạch (2026-10-14)

Mỗi mạch trừ mạch mở đầu mở bằng trang tiêu đề mạch (`class="strand-title"`, `id="mach-N"`); tên trùng từng chữ với trang Nội dung. Deck 53 trang.

| N | Tên mạch | Trang tiêu đề mạch | Trang nội dung đầu mạch |
|---:|---|---|---|
| 1 | Mở đầu | P00 (trang bìa) | — |
| 2 | Đếm khóa phân biệt bằng Flajolet–Martin | FT | F00 |
| 3 | Ước lượng tần suất bằng Count-Min Sketch | CT | C00 |
| 4 | Mômen và ước lượng AMS | MT | M00 |
| 5 | Đếm bit 1 trong cửa sổ bằng DGIM | DT | D00 |
| 6 | Cửa sổ suy giảm và tổng kết | ET | E00 |
| 7 | Bài tập vận dụng | XT | X00 |
