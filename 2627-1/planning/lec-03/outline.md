# Bài 3: PageRank — mô hình và tính toán

## Phạm vi và sản phẩm học tập

- Vị trí: Bài 3 theo thứ tự đề xuất trong `sources/source.md`, tách phần PageRank của buổi gốc 4 sau Bài 2 về MapReduce.
- Đối tượng: sinh viên đã học đồ thị có hướng, phép nhân ma trận–vector, phân phối xác suất và mô hình khóa–giá trị.
- Phạm vi nguồn: MMDS 3e, Chương 5, mục 5.1–5.2. Topic-Sensitive PageRank, link spam, TrustRank và HITS thuộc Bài 4.
- Sản phẩm: lập phương trình PageRank; sửa nút cụt và bẫy nhện; chạy phép lặp; nêu đúng điều kiện hội tụ; dùng cận hậu nghiệm; biểu diễn đồ thị thưa; mô tả một vòng PageRank bằng các pha MapReduce.
- Thời lượng: 120 phút giảng và 60 phút bài tập trực tiếp từ MMDS.

## Mạch nội dung

Bảy mạch: mở đầu (gộp P/A), B, C, D, E, kết luận K và recitation R.

1. Mở đầu (P/A): xếp hạng trên đồ thị liên kết lớn, đầu vào thưa, đầu ra xác suất và trực giác người lướt ngẫu nhiên.
2. B: đóng góp trên cạnh trước ma trận — chạy tay đồ thị $y,a,m$, rồi mới dựng ma trận cột và phép lặp.
3. C: nút cụt và bẫy nhện — hai biến thể MMDS của cùng đồ thị, theo vết mất hoặc kẹt khối lượng, sửa cột nút cụt và thêm hệ số giảm.
4. D: tính đúng và hội tụ — bất biến xác suất, tính dương, ánh xạ co theo chuẩn $L_1$, cận hậu nghiệm và giới hạn vòng lặp.
5. E: tính toán quy mô lớn — bản ghi cấu trúc, đóng góp map, nhóm và reduce, tổng nút cụt, phần dư toàn cục, số pha đồng bộ và chi phí mỗi vòng.
6. K: kết luận — thu hồi bài toán A00, ba khối đã xây và nối sang Bài 4.
7. R: bài tập MMDS — 5.1.1, 5.1.2, 5.2.1 và 5.2.2.

Tổng cộng 39 slide: 120 phút giảng và 60 phút bài tập trực tiếp từ MMDS; K00 là trang kết luận.

## Chu trình học tập

| Cụm | Tình huống và vấn đề | Trực giác | Ví dụ chạy tay | Hình thức hóa | Thuật toán và lập luận | Ứng dụng, chi phí và kiểm tra |
|---|---|---|---|---|---|---|
| PageRank cơ sở | A00–A01 | A02–A03 | B01–B02 | B03 | B04–B06 | D05, R02–R03 |
| Nút cụt và bẫy nhện | C00–C02, C04 | C03, C05 | C02–C03, C04–C06 | C03, C05 | C07, D00–D03 | E04, R05 |
| PageRank phân tán | E00 | E01 | E02 | E03–E04 | E04 | E05, R04–R05 |

Dữ liệu $y,a,m$ được giữ từ B01 đến B05. C01 tạo hai biến thể nguồn bằng cách đổi riêng cạnh ra của $m$. C02–C06 truyền các trạng thái số sang công thức sửa và hệ số giảm. E01–E05 dùng lại bản ghi của $a$ và quy ước nút cụt để nối phép tính đại số với MapReduce. E00–E01 chỉ được tính một lần, thuộc chu trình phân tán; trong chu trình PageRank cơ sở, E00 chỉ thu hồi giới hạn ma trận đặc mà không tính lại thời lượng.

## Ký hiệu thống nhất

| Ký hiệu | Nghĩa |
|---|---|
| $G=(V,E)$ | Đồ thị có hướng đơn sau khi gộp liên kết lặp; cho phép vòng tự nối |
| $n=|V|$, $m=|E|$ | Số nút và số cạnh sau khi gộp |
| $j\to i$ | Cạnh từ nút nguồn $j$ đến nút đích $i$ |
| $d^+(j)$, $N^+(j)$ | Bậc ra và tập đích của $j$ |
| $N^-(i)$ | Tập tiền nhiệm có cạnh đi vào nút $i$ |
| $P_0$ | Toán tử chuyển thưa chỉ chứa cạnh thật; cột của nút cụt bằng 0 |
| $d$ | Vector chỉ báo nút cụt: $d_j=1$ khi $d^+(j)=0$, ngược lại bằng 0 |
| $\bar P=P_0+ed^T/n$ | Ma trận chuyển cột ngẫu nhiên sau khi sửa nút cụt |
| $P$ | Ký hiệu gọn cho $\bar P$ trong phần phép lặp tập trung C03–D04 |
| $e$ | Vector toàn số 1, độ dài $n$ |
| $U=ee^T/n$ | Ma trận chuyển đều |
| $A_\beta=\beta P+(1-\beta)U$ | Ma trận chuyển có hệ số giảm và dịch chuyển ngẫu nhiên |
| $r^{(t)}$ | Vector PageRank ở vòng $t$ |
| $\tau$ | Ngưỡng phần dư giữa hai vòng |
| $\varepsilon$ | Sai số $L_1$ đích đến nghiệm |
| $K_{\max}$ | Số vòng tối đa |
| $\delta^{(t)}=d^Tr^{(t)}$ | Tổng hạng tại các nút cụt |
| $\Delta_{t+1}$ | Tổng thay đổi $L_1$ sau vòng cập nhật |

## Ánh xạ nguồn

| Cụm | Nguồn chính | Quyết định |
|---|---|---|
| Động cơ, luồng hạng, ma trận, đồ thị $y,a,m$ | MMDS official slides Ch5 part 1, slide 18–27; MMDS 3e §5.1.2 | Giữ dữ kiện; thêm bước chạy tay đóng góp trước ma trận |
| Người lướt ngẫu nhiên | Stanford CS246 `09-pagerank.pdf`, slide 17–18 | Dùng bổ trợ vì cầu nối hành vi–phương trình ngắn hơn; sách MMDS kiểm chứng |
| Nút cụt, bẫy nhện, hệ số giảm | MMDS official slides, slide 38–46; MMDS 3e §5.1.4–5.1.5 | Dùng đúng hai biến thể $y,a,m$; chọn quy ước chuẩn hóa cột nút cụt bằng $e/n$ |
| Điều kiện hội tụ | MMDS 3e §5.1.2; lý thuyết chuỗi Markov hữu hạn | Không lặp mệnh đề thiếu giả thiết; nêu bất khả quy là điều kiện đủ cho duy nhất, thêm không chu kỳ cho hội tụ khi $\beta=1$; chứng minh trường hợp $0<\beta<1$ bằng ánh xạ co |
| Cận dừng | Suy ra từ ánh xạ co | Dùng cận hậu nghiệm $\beta\Delta_t/(1-\beta)$; tách $\tau$ khỏi $\varepsilon$ |
| Biểu diễn thưa và MapReduce | MMDS 3e §5.2.1–5.2.2; MMDS slides 48, 52–55 | Giữ đúng một bản ghi cho mỗi nút; dùng $P_0$ cho cạnh thật và $\delta e/n$ để hiện thực $\bar P$; làm rõ $\Delta$, hai pha đồng bộ và chi phí $\Theta(n+m)$ |
| Bài tập | MMDS 3e, Bài 5.1.1–5.1.2, trang in 187–188; Bài 5.2.1–5.2.2, trang in 195 | Dịch trực tiếp; vẽ lại đủ Hình 5.4 và 5.7; không đổi dữ kiện |

## Kiểm tra số

Đồ thị cơ sở, thứ tự $(y,a,m)$:

$$
P=\begin{bmatrix}1/2&1/2&0\\1/2&0&1\\0&1/2&0\end{bmatrix},
\qquad
r^*=\begin{bmatrix}2/5&2/5&1/5\end{bmatrix}^{T}.
$$

Biến thể nút cụt có cột $m$ bằng 0 cho $r^{(1)}=(1/3,1/6,1/6)^T$ từ vector đều; tổng giảm còn $2/3$. Sau khi thay cột $m$ bằng $e/3$, $r^{(1)}=(4/9,5/18,5/18)^T$ và tổng bằng 1.

Biến thể bẫy nhện $m\to m$, với $\beta=0{,}8$:

$$
A_{0,8}=\begin{bmatrix}7/15&7/15&1/15\\7/15&1/15&1/15\\1/15&7/15&13/15\end{bmatrix},
\qquad
r^*=\begin{bmatrix}7/33&5/33&21/33\end{bmatrix}^{T}.
$$

Đồ thị cơ sở với $\beta=0{,}8$ có nghiệm $r^*=(35/93,37/93,21/93)^T$. Hai nghiệm có hệ số giảm thuộc hai đồ thị khác nhau và không được dùng thay nhau.

## Bản đồ chủ đề của ghi chú bài giảng

| `note-topic-id` | Chủ đề | Nhãn | Sản phẩm học tập | Nguồn và quyết định |
|---|---|---|---|---|
| `note-topic-03-web-graph` | Đồ thị Web có hướng và tính thưa | cốt lõi | Đặc tả đúng đầu vào, cạnh và tham số kích thước | MMDS §5.1.2, §5.2.1; giữ |
| `note-topic-03-random-surfer` | Người lướt ngẫu nhiên và phân phối hạng | cầu nối | Nối hành vi truy cập với phân phối xác suất | MMDS §5.1.2; Stanford bổ trợ trực giác |
| `note-topic-03-flow-matrix` | Đóng góp theo cạnh, ma trận cột và vết chạy $y,a,m$ | cốt lõi | Dựng $P$ và kiểm tra phương trình cố định | MMDS slide 16–27; giữ |
| `note-topic-03-dead-end` | Nút cụt và sửa cột | cốt lõi | Tính khối lượng mất và chứng minh phép sửa bảo toàn tổng | MMDS §5.1.4, slide 38, 41–43; giữ |
| `note-topic-03-spider-trap` | Bẫy nhện và hệ số giảm | cốt lõi | Phân biệt bẫy với nút cụt, dựng $A_\beta$ | MMDS §5.1.5, slide 39, 44–46; giữ |
| `note-topic-03-convergence` | Ánh xạ co trên simplex | bổ sung | Chứng minh nghiệm duy nhất và hội tụ khi $0<\beta<1$ | Suy trực tiếp từ đặc tả; không gán cho MMDS |
| `note-topic-03-stopping` | Thuật toán lặp và cận dừng hậu nghiệm | bổ sung | Chọn $\tau$ từ sai số đích $\varepsilon$ và đọc hai trạng thái trả về | Tiêu chí phần dư từ slide; cận suy bằng chuỗi hình học |
| `note-topic-03-sparse-mapreduce` | Một vòng PageRank thưa bằng MapReduce | cốt lõi | Mô tả bản ghi, hai pha, $\delta$, $\Delta$ và chi phí | MMDS §5.2.1–5.2.2; giữ |
| `note-topic-03-exercises` | Bốn bài tập MMDS | cốt lõi luyện tập | Tự tính PageRank và biểu diễn ma trận thưa | MMDS 5.1.1–5.2.2; giữ nguyên dữ kiện |
| `note-topic-03-boundary` | Ranh giới sang Bài 04 | đọc thêm | Xác định phần chưa học | Chỉ liên kết ra; không soạn PageRank theo chủ đề, spam hoặc HITS |

Đồ thị tiên quyết của ghi chú là `web-graph → random-surfer → flow-matrix → {dead-end, spider-trap} → convergence → stopping → sparse-mapreduce → exercises`. Hai chủ đề bổ sung chỉ lấp khoảng trống về bảo đảm hội tụ và điều kiện dừng; không mở rộng phạm vi sang lý thuyết chuỗi Markov tổng quát.
