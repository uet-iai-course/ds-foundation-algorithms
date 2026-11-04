# Storyboard Bài 9

## Hành trình khái niệm

- **Flajolet–Martin:** tình huống F00 → trực giác và ví dụ F01 → đặc tả F02 → hình thức hóa F03 → giới hạn F04 → thuật toán gộp đúng F05 → chi phí và kiểm tra F06.
- **Count-Min Sketch:** tình huống C00 → trực giác và ví dụ số C01 → đặc tả cùng giả thiết C02 → nhiễu kỳ vọng, Markov và khuếch đại C03 → chi phí, giới hạn và kiểm tra C04.
- **AMS:** tình huống M00 → đại lượng M01 → trực giác và vết hậu tố M02 → hình thức hóa M03 → thuật toán M04 → cầu nối chứng minh M05 → tính đúng M06 → duy trì trên dòng tăng và chi phí M07.
- **DGIM:** tình huống và cận bộ nhớ D00 → định nghĩa bucket D01 → ví dụ trạng thái D02 → đọc bất biến từ ví dụ D03 → cập nhật D04–D05 → truy vấn bằng mốc phải D06–D07 → tính đúng D08 → chi phí và kiểm tra D09.
- **Cửa sổ suy giảm:** tình huống, trực giác và giới hạn tổng hữu hạn E00 → định nghĩa, cập nhật, chi phí và kiểm tra suy diễn E01. Đây là khái niệm phụ nên dùng chu trình rút gọn; không áp dụng bước ví dụ chạy tay vì nguồn không cho một bộ dữ kiện số riêng trong phạm vi đã chọn.

Tình huống xuyên suốt là dòng sự kiện có khóa và thời gian đến, với bộ nhớ nhỏ hơn lịch sử. Dữ liệu và đầu ra cụ thể được lấy lại theo cụm: lượt đăng nhập và số người dùng phân biệt ở FM; yêu cầu mạng và tần suất khóa ở Count-Min; phân phối tần suất ở AMS; vé phim mã hóa bit và số sự kiện gần đây ở DGIM/cửa sổ suy giảm.

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch"; yêu cầu người dùng 2026-10-14. Mỗi section ngoài trừ mạch mở đầu mở bằng một trang `class="strand-title"`, `id="mach-N"`. Mã theo quy ước của bài: mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch, nên trang tiêu đề mạch dùng `<tiền tố>T`. Trang tiêu đề mạch nằm ngoài chu trình khái niệm; thời lượng 0,5 phút mỗi trang lấy từ trang đầu mạch (cột "Trang đầu mạch"), tổng thời lượng bài không đổi. Deck 46 → 53 trang.

Bản đồ mạch (tên trùng từng chữ với trang Nội dung): 1. Mở đầu (mở bằng trang bìa P00); 2. Đếm khóa phân biệt bằng Flajolet–Martin (`FT`); 3. Ước lượng tần suất bằng Count-Min Sketch (`CT`); 4. Mômen và ước lượng AMS (`MT`); 5. Đếm bit 1 trong cửa sổ bằng DGIM (`DT`); 6. Cửa sổ suy giảm và tổng kết (`ET`); 7. Bài tập vận dụng (`XT`).

| Mã trang | Tiêu đề (tên mạch) | Mục đích | Vị trí | Kiến thức đầu vào | Đầu ra | Ghi chú | Phút | Quyết định |
|---|---|---|---|---|---|---|---:|---|
| P03 | Nội dung | Liệt kê đánh số mọi mạch, tên trùng trang tiêu đề mạch; notes một câu mỗi mạch | mạch mở đầu, sau P00 | Tên bài | Thứ tự và quan hệ các mạch | trang `agenda-slide` | 0,5 (từ trang bìa) | thêm |
| FT | Đếm khóa phân biệt bằng Flajolet–Martin | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 2, `id="mach-2"`, trước F00 | Bốn hợp đồng trên một dòng (A00–A02) | Flajolet–Martin, gộp trung bình rồi trung vị | ngoài chu trình khái niệm; tên khác tiêu đề F00 | 0,5 (từ F00) | thêm |
| CT | Ước lượng tần suất bằng Count-Min Sketch | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 3, `id="mach-3"`, trước C00 | Số khóa phân biệt; dòng chỉ tăng | Count-Min Sketch và bảo đảm một phía | ngoài chu trình khái niệm; tên khác tiêu đề C00 | 0,5 (từ C00) | thêm |
| MT | Mômen và ước lượng AMS | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 4, `id="mach-4"`, trước M00 | Tần suất từng khóa | Biến AMS không chệch cho $F_2$ | ngoài chu trình khái niệm; tên khác tiêu đề M00 | 0,5 (từ M00) | thêm |
| DT | Đếm bit 1 trong cửa sổ bằng DGIM | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 5, `id="mach-5"`, trước D00 | Các phác thảo trên toàn dòng | DGIM, sáu bất biến, cận sai số | ngoài chu trình khái niệm; tên khác tiêu đề D00 | 0,5 (từ D00) | thêm |
| ET | Cửa sổ suy giảm và tổng kết | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 6, `id="mach-6"`, trước E00 | Cửa sổ biên cứng của DGIM | Cửa sổ suy giảm, bảng chọn cấu trúc, năm giới hạn | ngoài chu trình khái niệm; tên khác tiêu đề E00 | 0,5 (từ E00) | thêm |
| XT | Bài tập vận dụng | Dòng dẫn nêu nhu cầu của mạch; notes nối kết quả kế thừa, nhiệm vụ, kết quả giao | điểm vào mạch 7, `id="mach-7"`, trước X00 | FM, AMS, DGIM | Năm bài MMDS 4.4.1, 4.5.1, 4.5.3, 4.6.1, 4.6.3 | ngoài chu trình khái niệm; tên khác tiêu đề X00 | 0,5 (từ X01; X00 không có phút riêng nên X01 giảm 0,5 phút) | thêm |

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–7) ngay sau trang bìa P00, tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 43 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Mạch 6 gộp cửa sổ suy giảm (E00–E01) với bảng tổng kết (T00–T01) như cấu trúc hiện có; tên mạch "Cửa sổ suy giảm và tổng kết" nêu cả hai.

## Bản đồ chu trình và thời lượng

| Cụm | Mã thực hiện chu trình | Đầu vào → sản phẩm | Dữ kiện truyền | Bước gộp hoặc rút gọn | Câu nối | Phút |
|---|---|---|---|---|---|---:|
| Bản đồ quyết định | P01; A00–A02 | dòng khóa và mốc đến → chọn đúng loại trạng thái | bốn câu hỏi ở P01; phạm vi toàn dòng/gần đây ở A00 truyền sang A01 | tình huống, vấn đề và hình thức gộp vì chưa có thuật toán | Đại lượng và phạm vi thời gian quyết định phác thảo. | 8 |
| FM | F00–F06 | khóa và băm $L$ bit → $\widehat F_0$ | $\rho,R,2^R$ từ F01–F03 sang gộp F05 | trực giác và ví dụ gộp F01; tính đúng là lập luận ngưỡng dưới băm lý tưởng, không tuyên bố không chệch | Một đuôi hiếm báo quy mô, nhưng cần $q$ ước lượng để ổn định. | 22 |
| Count-Min | C00–C04 | cập nhật không âm → $\widehat f_x$ | $f_x=6$ và nhiễu $3,1,5$ ở C01 sang phép min C02; $Y_j$ sang Markov và khuếch đại C03 | ứng dụng, chi phí và kiểm tra gộp C04 vì cụm rút gọn 14 phút | Từ số khóa phân biệt chuyển sang số lần của một khóa cụ thể. | 14 |
| AMS | M00–M07 | vị trí đều, bộ đếm hậu tố → $\widehat F_2$ | dòng 15 phần tử và $c_I$ ở M02 truyền sang hình thức M03, thuật toán và chứng minh | kiểm tra gộp vào nhánh hồ chứa M07; chi phí lượng hóa theo $q$ | Mômen đo độ lệch mà một truy vấn tần suất riêng lẻ không thể hiện. | 25 |
| DGIM | D00–D09 | dòng bit, cửa sổ $N$, hậu tố $k$ → $\widehat c(k)$ | Hình 4.2 ở D02 truyền sang bất biến D03, truy vấn D07 và cận D08 | ví dụ đứng trước bất biến; truy vấn chỉ dùng mốc phải, không giả định biết đầu trái | Từ toàn dòng chuyển sang câu hỏi chỉ về dữ liệu gần đây. | 36 |
| Suy giảm | E00–E01 | dòng số và $c$ → tổng có trọng số | đường trọng số và tổng hữu hạn E00 truyền sang truy hồi E01 | rút gọn vì là khái niệm phụ; kiểm tra suy diễn ở E01; không dạy duy trì nhiều khóa | Bỏ biên cứng bằng cách giảm dần trọng số. | 7 |
| Tổng hợp | T00–T01 | năm hợp đồng → lựa chọn có điều kiện | bảo đảm từ F04, C03, M06, D08 và E01 | không có thuật toán mới | Bài tập kiểm tra trực tiếp từng bảo đảm. | 8 |

Tổng phần giảng: **120 phút**.

Ánh xạ RevealJS: sáu mạch giảng là P00–A02, F00–F06, C00–C04, M00–M07, D00–D09 và E00–T01; mạch bài tập X00–X05 đứng cuối. Tổng cộng đúng bảy `<section>` ngoài. Trong mạch kết luận E00–T01, suy giảm mũ mở rộng khái niệm dữ liệu gần đây rồi T00–T01 đối chiếu năm cấu trúc và thu hồi bản đồ quyết định mở bài.

## Bản đồ từng trang phần giảng

| ID | Bước tiến | Nguồn |
|---|---|---|
| P00 | Định vị bài sau Bài 8. | `sources/source.md`; MMDS Ch.4 |
| P01 | Nêu dòng, giới hạn và bốn đầu ra. | MMDS tr.142–159 |
| P02 | Nêu sản phẩm học tập quan sát được. | `sources/source.md` |
| A00 | Phân biệt truy vấn toàn dòng với truy vấn gần đây; không lặp bản đồ P01. | tổng hợp nguồn |
| A01 | Đặc tả bốn dạng đầu ra và bảo đảm. | MMDS 4.4–4.6; UMass Count-Min |
| A02 | Kiểm tra giới hạn của bảng đếm chính xác. | MMDS tr.142, 146 |
| F00 | Mở tình huống sử dụng người dùng duy nhất và nhiều dòng song song. | MMDS tr.142–143 |
| F01 | Minh họa đuôi băm hiếm. | MMDS tr.143; Streams 2 tr.17–20 |
| F02 | Đặc tả trạng thái, cập nhật, dòng rỗng và $\rho(0)$ cho băm $L$ bit. | MMDS tr.143; quy ước biên do deck đặt |
| F03 | Lập luận xác suất ngưỡng quanh $2^r$ dưới mô hình băm đều, độc lập. | MMDS tr.143–144 |
| F04 | Phân biệt trung bình/trung vị và cảnh báo đuôi nặng. | MMDS tr.144 |
| F05 | Nêu đúng thứ tự trung bình trong nhóm rồi trung vị. | MMDS tr.144; Stanford 2017 Streams 2 |
| F06 | Lượng hóa chi phí theo $q$, nêu giới hạn và kiểm tra phần tử lặp. | MMDS tr.144–145 |
| C00 | Mở tình huống sử dụng tần suất khóa trong dòng chỉ tăng. | UMass CS514 Lecture 10 |
| C01 | Chạy ví dụ $f_x=6$ với nhiễu va chạm $3,1,5$. | UMass CS514 Lecture 10 |
| C02 | Đặc tả $n,k,\varepsilon,\delta$, khởi tạo bảng, $m=\lceil2k/\varepsilon\rceil$, $t=\lceil\log_2(1/\delta)\rceil$; nêu miền, độc lập đôi một trong hàng và độc lập giữa hàng. | UMass CS514 Lecture 10 |
| C03 | Nối kỳ vọng nhiễu → Markov → hàng độc lập và phép min; kết luận sai số $\varepsilon n/k$. | UMass CS514 Lecture 10 |
| C04 | Lượng hóa $O(t)$, $O(mt)$; nêu giới hạn ứng viên và cập nhật âm. | UMass CS514 Lecture 10 |
| M00 | Đặt hai phân phối cùng độ dài, khác $F_2$. | MMDS tr.146 |
| M01 | Định nghĩa $F_k$, diễn giải $F_0,F_1,F_2$. | MMDS tr.146 |
| M02 | Chạy vết hậu tố để hình thành trực giác về bộ đếm $c_I$. | MMDS Ví dụ 4.7–4.8, tr.146–147 |
| M03 | Định nghĩa rõ $I,c_I,X$ sau ví dụ. | MMDS tr.146–147 |
| M04 | Giả mã một biến AMS. | MMDS tr.146–147 |
| M05 | Nhóm hạng theo cùng khóa để chuẩn bị chứng minh. | MMDS tr.147–148 |
| M06 | Chứng minh $\mathbb E[X]=F_2$. | MMDS tr.148 |
| M07 | Duy trì $q$ vị trí đều trên dòng tăng, đủ ba nhánh cập nhật và chi phí. | MMDS tr.148–149 |
| D00 | Mở tình huống sử dụng vé phim và cận $N$ bit cho lời giải chính xác. | MMDS tr.151, 157–159 |
| D01 | Định nghĩa bucket và mốc phải. | MMDS tr.152 |
| D02 | Vẽ lại đúng Hình 4.2, gồm phần trái chưa xác định và các mốc phải ở bit 1. | MMDS Hình 4.2, tr.152 |
| D03 | Đọc sáu bất biến từ trạng thái vừa thấy. | MMDS tr.152–153 |
| D04 | Nêu cập nhật, hết hạn và cascade. | MMDS tr.154–155 |
| D05 | Chạy tay chuỗi gộp cục bộ. | MMDS tr.155–156 |
| D06 | Đặc tả truy vấn chỉ bằng mốc phải của bucket cũ nhất còn trong hậu tố. | MMDS tr.153–154 |
| D07 | Chạy truy vấn $k=10$ với ranh giới trước vị trí 16. | MMDS Ví dụ 4.12, tr.153–154 |
| D08 | Chứng minh cận 50% cho $c>0$ bằng $A\ge \lvert b^*\rvert-1$, xét cả ước lượng thấp và cao; tách trường hợp $c=0$. | MMDS tr.154 |
| D09 | Phân tích bộ nhớ, cập nhật, truy vấn. | MMDS tr.153–155 |
| E00 | Mở tình huống độ phổ biến gần đây; so sánh phân bố và sửa tổng hữu hạn. | MMDS Hình 4.4, tr.157–158 |
| E01 | Dẫn truy hồi, chi phí $O(1)$ và kiểm tra bằng đổi chỉ số. | MMDS tr.158–159 |
| T00 | Đối chiếu năm cấu trúc theo đầu ra, cập nhật và trạng thái. | tổng hợp nguồn |
| T01 | Khóa năm điều kiện bảo đảm, ghi công nguồn. | tổng hợp nguồn |

## Phần bài tập củng cố

| ID | Phút | Dữ kiện, yêu cầu và sản phẩm | Hướng dẫn chấm trong ghi chú | Nguồn trực tiếp |
|---|---:|---|---|---|
| X00 | 0 | Mở phần và nêu hình thức nộp. | Nêu năm bài trực tiếp từ sách. | MMDS 4.4–4.6 |
| X01 | 12 | Tính đuôi băm, $R$ và ba ước lượng cho dòng đã cho. | Bảng chín giá trị mỗi hàm và kết quả $1,16,16$. | Ex.4.4.1, tr.145 |
| X02 | 8 | Lập bảng tần suất, tính $F_2,F_3$. | $F_2=21,F_3=51$. | Ex.4.5.1, tr.150 |
| X03 | 12 | Tính rõ mọi bộ đếm hậu tố $c_i$, không nhập nhằng với $X_i$. | Một hàng chín giá trị; $X_i$ và trung bình 21 chỉ dùng tự kiểm trong ghi chú. | Ex.4.5.3, tr.150 |
| X04 | 12 | Truy vấn Hình 4.2 với $k=5,15$ trên hình không lộ đáp án; SVG bài tập khớp bit-by-bit trạng thái DGIM nền. | $3$ đúng tuyệt đối; $10$ so với $9$, lệch $1/9$. | Ex.4.6.1, tr.157 |
| X05 | 16 | Từ trạng thái Hình 4.3 tự chứa, thêm ba bit 1 và ghi cascade qua mọi mức. | Ba trạng thái; nhánh điều kiện nếu phía trái đã có hai bucket 8, và tiếp tục cao hơn khi cần. | Ex.4.6.3, tr.157 |

X00 không thêm yêu cầu toán học. Tổng phần bài tập: **60 phút**.

## Rà lại thứ tự sau chỉnh sửa

- A00 thay nội dung lặp với P01; đã rà P00–A02. P01 mở bốn quyết định, P02 đặt mục tiêu, A00 thêm trục toàn dòng/gần đây, A01 mới chốt hợp đồng.
- M02 và M03 đổi thứ tự; đã rà M00–M05. Tình huống và mômen đi trước, vết hậu tố đi trước ký hiệu $I,c_I,X$, rồi mới đến giả mã và chứng minh.
- D02 và D03 đổi thứ tự; đã rà D00–D05. Định nghĩa bucket đi trước trạng thái cụ thể, bất biến được đọc từ trạng thái, sau đó mới cập nhật.
- D07 và X04 dùng hình riêng để ranh giới truy vấn không lẫn với trạng thái nền hoặc đáp án bài tập.

## Hành trình chủ đề của ghi chú bài giảng

Cập nhật 2026-11-04 theo `note-topic-id` của ghi chú; thay bảng `L09-N01…N10` cũ. Phần trang chiếu ở trên phản ánh deck cũ cho tới khi deck được làm lại.

| `note-topic-id` | Vai trò và kết nối vào–ra | Kiến thức đầu vào → sản phẩm | Thành phần trình bày |
|---|---|---|---|
| `lec-09-topic-01` | Cầu nối vào chương; nhận Bài 08, 06, 05 và công cụ xác suất, cấp cho Mục 1–6. | Kết quả các bài trước → phát biểu lại đúng giả thiết. | Danh sách nhóm kết quả kèm số hiệu và phát biểu lại. |
| `lec-09-topic-02` | Mở từ yêu cầu Bài 08 để ngỏ; đặt năm đại lượng và chi phí lời giải chính xác, ra năm nhu cầu. | Mô hình dòng → $f_u$, $F_p$, cửa sổ trượt, Nhận xét 09.3. | Hình cấu trúc chương, Ví dụ 09.1–09.2, Định nghĩa 09.1–09.2, Bài tập 09.1, đoạn kết mục. |
| `lec-09-topic-03` | Nhận nhu cầu $F_0$; chứng tỏ đếm chính xác tốn 512 MiB, ra nhu cầu ước lượng. | Vector bit → cận dưới tất định (Nhận xét 09.4). | Đoạn bài toán, nhận xét có lập luận đếm. |
| `lec-09-topic-04` | Đưa ra ước lượng $2^R$; ra bất biến dùng cho phân tích. | Băm tất định → chạy Thuật toán 09.6, Mệnh đề 09.7. | Trực giác, Ví dụ 09.3–09.4, định nghĩa, thuật toán, chứng minh bất biến. |
| `lec-09-topic-05` | Nhận $R$; đặt mô hình băm lý tưởng và cận hai phía, ra nhu cầu gộp. | Độc lập, cận hợp, $1-z\le e^{-z}$ → Định lý 09.10. | Định nghĩa 09.8, Bổ đề 09.9, định lý bốn phần, chứng minh theo bước, phản ví dụ khi bỏ giả thiết, Ví dụ 09.5 với hình ngưỡng. |
| `lec-09-topic-06` | Nhận nhu cầu gộp; chỉ ra đuôi nặng và trung vị lũy thừa của 2, ra phép gộp hai bước. | Kỳ vọng, nhị thức → Mệnh đề 09.11, Bổ đề 09.14, Hệ quả 09.15. | Ví dụ 09.6, Thuật toán 09.13, bảng chi phí. |
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
