# Storyboard Bài 9

## Hành trình khái niệm

- **Flajolet–Martin:** tình huống F00 → trực giác và ví dụ F01 → đặc tả F02 → hình thức hóa F03 → giới hạn F04 → thuật toán gộp đúng F05 → chi phí và kiểm tra F06.
- **Count-Min Sketch:** tình huống C00 → trực giác và ví dụ số C01 → đặc tả cùng giả thiết C02 → nhiễu kỳ vọng, Markov và khuếch đại C03 → chi phí, giới hạn và kiểm tra C04.
- **AMS:** tình huống M00 → đại lượng M01 → trực giác và vết hậu tố M02 → hình thức hóa M03 → thuật toán M04 → cầu nối chứng minh M05 → tính đúng M06 → duy trì trên dòng tăng và chi phí M07.
- **DGIM:** tình huống và cận bộ nhớ D00 → định nghĩa bucket D01 → ví dụ trạng thái D02 → đọc bất biến từ ví dụ D03 → cập nhật D04–D05 → truy vấn bằng mốc phải D06–D07 → tính đúng D08 → chi phí và kiểm tra D09.
- **Cửa sổ suy giảm:** tình huống, trực giác và giới hạn tổng hữu hạn E00 → định nghĩa, cập nhật, chi phí và kiểm tra suy diễn E01. Đây là khái niệm phụ nên dùng chu trình rút gọn; không áp dụng bước ví dụ chạy tay vì nguồn không cho một bộ dữ kiện số riêng trong phạm vi đã chọn.

Tình huống xuyên suốt là dòng sự kiện có khóa và thời gian đến, với bộ nhớ nhỏ hơn lịch sử. Dữ liệu và đầu ra cụ thể được lấy lại theo cụm: lượt đăng nhập và số người dùng phân biệt ở FM; yêu cầu mạng và tần suất khóa ở Count-Min; phân phối tần suất ở AMS; vé phim mã hóa bit và số sự kiện gần đây ở DGIM/cửa sổ suy giảm.

## Bản đồ chu trình và thời lượng

| Cụm | Mã thực hiện chu trình | Đầu vào → sản phẩm | Dữ kiện truyền | Bước gộp hoặc rút gọn | Câu nối | Phút |
|---|---|---|---|---|---|---:|
| Bản đồ quyết định | P01; A00–A02 | dòng khóa và mốc đến → chọn đúng loại trạng thái | bốn câu hỏi ở P01; phạm vi toàn dòng/gần đây ở A00 truyền sang A01 | tình huống, vấn đề và hình thức gộp vì chưa có thuật toán | Đại lượng và phạm vi thời gian quyết định phác thảo. | 8 |
| FM | F00–F06 | khóa và băm $L$ bit → $\widehat F_0$ | $\rho,R,2^R$ từ F01–F03 sang gộp F05 | trực giác và ví dụ gộp F01; tính đúng là lập luận ngưỡng dưới băm lý tưởng, không tuyên bố không chệch | Một đuôi hiếm báo quy mô, nhưng cần $q$ ước lượng để ổn định. | 22 |
| Count-Min | C00–C04 | cập nhật không âm → $\widehat f_x$ | $f_x=6$ và nhiễu $3,1,5$ ở C01 sang phép min C02; $Y_j$ sang Markov và khuếch đại C03 | ứng dụng, chi phí và kiểm tra gộp C04 vì cụm rút gọn 14 phút | Từ số khóa phân biệt chuyển sang số lần của một khóa cụ thể. | 14 |
| AMS | M00–M07 | vị trí đều, bộ đếm hậu tố → $\widehat F_2$ | dòng 15 phần tử và $c_I$ ở M02 truyền sang hình thức M03, thuật toán và chứng minh | kiểm tra gộp vào nhánh hồ chứa M07; chi phí lượng hóa theo $q$ | Mômen đo độ lệch mà một truy vấn tần suất riêng lẻ không thể hiện. | 25 |
| DGIM | D00–D09 | dòng bit, cửa sổ $N$, hậu tố $k$ → $\widehat c(k)$ | Hình 4.2 ở D02 truyền sang bất biến D03, truy vấn D07 và cận D08 | ví dụ đứng trước bất biến; truy vấn chỉ dùng mốc phải, không giả định biết đầu trái | Từ toàn dòng chuyển sang câu hỏi chỉ về dữ liệu gần đây. | 36 |
| Suy giảm | E00–E01 | dòng số và $c$ → tổng có trọng số | đường trọng số và tổng hữu hạn E00 truyền sang truy hồi E01 | rút gọn vì là khái niệm phụ; kiểm tra suy diễn ở E01; không dạy duy trì nhiều khóa | Bỏ biên cứng bằng cách giảm dần trọng số. | 7 |
| Tổng hợp | T00–T01 | bốn hợp đồng → lựa chọn có điều kiện | bảo đảm từ F04, C03, M06, D08 | không có thuật toán mới | Bài tập kiểm tra trực tiếp từng bảo đảm. | 8 |

Tổng phần giảng: **120 phút**.

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
| F02 | Đặc tả trạng thái, cập nhật, dòng rỗng và $\rho(0)$ cho băm $L$ bit. | MMDS tr.143; làm rõ trường hợp biên hữu hạn |
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
| M01 | Định nghĩa $F_k$, diễn giải $F_0,F_1,F_2$. | MMDS tr.145–146 |
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
| T00 | Đối chiếu bốn cấu trúc theo đầu ra, cập nhật và trạng thái. | tổng hợp nguồn |
| T01 | Khóa bốn điều kiện bảo đảm, ghi công nguồn. | tổng hợp nguồn |

## Phần bài tập củng cố

| ID | Phút | Dữ kiện, yêu cầu và sản phẩm | Hướng dẫn chấm trong ghi chú | Nguồn trực tiếp |
|---|---:|---|---|---|
| X00 | 0 | Mở phần và nêu hình thức nộp. | Nêu năm bài trực tiếp từ sách. | MMDS 4.4–4.6 |
| X01 | 12 | Tính đuôi băm, $R$ và ba ước lượng cho dòng đã cho. | Bảng chín giá trị mỗi hàm và kết quả $1,16,16$. | Ex.4.4.1, tr.145 |
| X02 | 8 | Lập bảng tần suất, tính $F_2,F_3$. | $F_2=21,F_3=51$. | Ex.4.5.1, tr.149–150 |
| X03 | 12 | Tính rõ mọi bộ đếm hậu tố $c_i$, không nhập nhằng với $X_i$. | Một hàng chín giá trị; $X_i$ và trung bình 21 chỉ dùng tự kiểm trong ghi chú. | Ex.4.5.3, tr.150 |
| X04 | 12 | Truy vấn Hình 4.2 với $k=5,15$ trên hình không lộ đáp án. | $3$ đúng tuyệt đối; $10$ so với $9$, lệch $1/9$. | Ex.4.6.1, tr.157 |
| X05 | 16 | Từ trạng thái Hình 4.3 tự chứa, thêm ba bit 1 và ghi cascade qua mọi mức. | Ba trạng thái; nhánh điều kiện nếu phía trái đã có hai bucket 8, và tiếp tục cao hơn khi cần. | Ex.4.6.3, tr.157 |

X00 không thêm yêu cầu toán học. Tổng phần bài tập: **60 phút**.

## Rà lại thứ tự sau chỉnh sửa

- A00 thay nội dung lặp với P01; đã rà P00–A02. P01 mở bốn quyết định, P02 đặt mục tiêu, A00 thêm trục toàn dòng/gần đây, A01 mới chốt hợp đồng.
- M02 và M03 đổi thứ tự; đã rà M00–M05. Tình huống và mômen đi trước, vết hậu tố đi trước ký hiệu $I,c_I,X$, rồi mới đến giả mã và chứng minh.
- D02 và D03 đổi thứ tự; đã rà D00–D05. Định nghĩa bucket đi trước trạng thái cụ thể, bất biến được đọc từ trạng thái, sau đó mới cập nhật.
- D07 và X04 dùng hình riêng để ranh giới truy vấn không lẫn với trạng thái nền hoặc đáp án bài tập.
