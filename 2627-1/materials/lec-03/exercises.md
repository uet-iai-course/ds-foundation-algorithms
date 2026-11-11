# Bài tập Bài 03 — PageRank: mô hình và tính toán

Các bài tập củng cố 03.7–03.12 dưới đây lấy từ bài tập Chương 5 của sách *Mining of Massive Datasets*, ấn bản 3 (viết tắt MMDS), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 03.k là của [ghi chú Bài 03](material-viewer.html?doc=materials/lec-03/lecture-note.md&deck=lecture-03-pagerank-mo-hinh-va-tinh-toan.html), nơi Bài tập 03.1–03.6 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bốn bài 03.7–03.10, tức MMDS Bài 5.2.2, 5.1.1, 5.1.2 và 5.2.1, là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 03](lecture-03-pagerank-mo-hinh-va-tinh-toan.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Ma trận liên kết, một vòng chia điểm, hệ $r=M_0r$ (Mục 1, Mục 2.1) | 03.1 | 03.8 |
| 2. Nút cụt, bẫy liên kết, quy tắc cập nhật đầy đủ, hệ có bước nhảy (Mục 2.2, 2.3) | — | 03.9, 03.11 |
| 3. Bảo toàn tổng, hội tụ, ngưỡng dừng (Mục 2.4, 2.5) | 03.2 | — |
| 4. Danh sách liên kết ra, biểu diễn khối, Map, Combine, Reduce (Mục 3) | 03.3, 03.4 | 03.7 |
| 5. Dung lượng, bộ nhớ, đầu vào Map và Reduce, thời gian (Mục 4) | 03.4 | 03.10 |
| 6. Chạy `pagerank.py` và đối chiếu (Mục 5) | 03.6 | — |
| 7. (Đọc thêm) Loại nút cụt đệ quy và khôi phục điểm | 03.5 | 03.12 |

## Mức nhận biết

::: exercise Bài tập 03.7 (Biểu diễn hai đồ thị theo liên kết ra; MMDS Bài 5.2.2, §5.2.6, tr.195)
Dùng Định nghĩa 03.19, lập bảng nguồn, bậc ra và danh sách đích cho ma trận liên kết của hai đồ thị:

- (a) đồ thị của MMDS Hình 5.4 (tr.184): $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm E$; $\mathrm D\to\mathrm B,\mathrm C$; E không có liên kết ra;
- (b) đồ thị của MMDS Hình 5.7 (tr.188): $\mathrm a\to\mathrm a,\mathrm b,\mathrm c$; $\mathrm b\to\mathrm a,\mathrm c$; $\mathrm c\to\mathrm b,\mathrm c$.
:::

![Đồ thị Hình 5.4: năm nút A, B, C, D, E; A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới E; D trỏ tới B, C; E không có mũi tên đi ra.](img/lec-03/ex-fig-54.svg)

![Đồ thị Hình 5.7: ba nút a, b, c; a trỏ tới a, b, c; b trỏ tới a, c; c trỏ tới b, c; bảy cạnh, gồm hai khuyên ở a và ở c.](img/lec-03/ex-fig-57.svg)

::: hint
Mỗi nguồn ghi bậc ra trên toàn đồ thị rồi toàn bộ danh sách đích; nguồn không có liên kết ra vẫn có bản ghi với bậc 0. Một khuyên là một cạnh và được tính vào bậc ra.
:::

::: solution
**Câu (a).** Hình 5.4 có tám cạnh:

| Nguồn | Bậc ra | Đích |
|---|---|---|
| A | 3 | B, C, D |
| B | 2 | A, D |
| C | 1 | E |
| D | 2 | B, C |
| E | 0 | (rỗng) |

**Câu (b).** Hình 5.7 có bảy cạnh, gồm hai khuyên:

| Nguồn | Bậc ra | Đích |
|---|---|---|
| a | 3 | a, b, c |
| b | 2 | a, c |
| c | 2 | b, c |

**Kiểm tra lại.** Tổng bậc ra là $3+2+1+2+0=8$ và $3+2+2=7$, bằng số cạnh của hai hình. Bản ghi $(\mathrm E,0,[\,])$ không ứng với phần tử khác 0 nào của ma trận, nhưng cần cho phép tính $\delta$ của Định nghĩa 03.8. Từ bản ghi của $\mathrm a$, cột $\mathrm a$ của ma trận có $1/3$ ở cả ba hàng, kể cả hàng $\mathrm a$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 03.8 (PageRank của ba trang không có bước nhảy; MMDS Bài 5.1.1, §5.1.7, tr.187–188)
Đồ thị của MMDS Hình 5.7 có ba trang và các cạnh $\mathrm a\to\mathrm a,\mathrm b,\mathrm c$; $\mathrm b\to\mathrm a,\mathrm c$; $\mathrm c\to\mathrm b,\mathrm c$. Tính PageRank của từng trang khi không có bước nhảy, tức điểm cố định $r^*$ của Định nghĩa 03.5.
:::

::: hint
Viết ma trận liên kết theo cột nguồn, lập hệ $r=M_0r$ cùng điều kiện tổng bằng 1, rồi biểu diễn $r_{\mathrm b}$ và $r_{\mathrm c}$ theo $r_{\mathrm a}$.
:::

::: solution
**Lập hệ.** Theo Định nghĩa 03.3, cột $\mathrm a$ là $(1/3,1/3,1/3)^{\mathsf T}$, cột $\mathrm b$ là $(1/2,0,1/2)^{\mathsf T}$, cột $\mathrm c$ là $(0,1/2,1/2)^{\mathsf T}$. Đồ thị không có nút cụt. Hệ $r=M_0r$ cùng điều kiện tổng là
$$
\begin{aligned}
r_{\mathrm a}&=\frac{r_{\mathrm a}}3+\frac{r_{\mathrm b}}2,\\
r_{\mathrm b}&=\frac{r_{\mathrm a}}3+\frac{r_{\mathrm c}}2,\\
r_{\mathrm c}&=\frac{r_{\mathrm a}}3+\frac{r_{\mathrm b}}2+\frac{r_{\mathrm c}}2,\\
1&=r_{\mathrm a}+r_{\mathrm b}+r_{\mathrm c} .
\end{aligned}
$$

**Giải.** Phương trình thứ nhất cho $r_{\mathrm b}/2=2r_{\mathrm a}/3$, tức $r_{\mathrm b}=4r_{\mathrm a}/3$. Phương trình thứ hai cho $r_{\mathrm c}/2=r_{\mathrm b}-r_{\mathrm a}/3=r_{\mathrm a}$, tức $r_{\mathrm c}=2r_{\mathrm a}$. Điều kiện tổng cho $13r_{\mathrm a}/3=1$, nên
$$
r_{\mathrm a}=\frac3{13},\quad r_{\mathrm b}=\frac4{13},\quad r_{\mathrm c}=\frac6{13}.
$$

**Kiểm tra lại.** Phương trình thứ ba: $\tfrac1{13}+\tfrac2{13}+\tfrac3{13}=\tfrac6{13}=r_{\mathrm c}$; tổng $(3+4+6)/13=1$. Mỗi cột của $M_0$ có tổng 1, nên cộng ba phương trình của hệ $r=M_0r$ được đồng nhất thức $r_{\mathrm a}+r_{\mathrm b}+r_{\mathrm c}=r_{\mathrm a}+r_{\mathrm b}+r_{\mathrm c}$; một phương trình là hệ quả của hai phương trình kia, và điều kiện tổng chọn ra một nghiệm.
:::

::: exercise Bài tập 03.9 (PageRank của ba trang với $\beta=0{,}8$; MMDS Bài 5.1.2, §5.1.7, tr.188)
Với đồ thị Hình 5.7 của Bài tập 03.8, tính PageRank của từng trang theo Định nghĩa 03.8 với $\beta=0{,}8$, tức điểm cố định $r^*=F(r^*)$ của Định lý 03.15. So với kết quả của Bài tập 03.8.
:::

::: hint
Đồ thị không có nút cụt nên $\delta=0$ và phần chung là $(1-\beta)/3=1/15$ (Mệnh đề 03.9(c)). Thay $r_{\mathrm c}=1-r_{\mathrm a}-r_{\mathrm b}$ để còn hai ẩn.
:::

::: solution
**Lập hệ.** Theo Mệnh đề 03.9(c), $r=\tfrac45M_0r+\tfrac1{15}\mathbf 1$. Hai phương trình đầu là
$$
\begin{aligned}
r_{\mathrm a}&=\frac45\Big(\frac{r_{\mathrm a}}3+\frac{r_{\mathrm b}}2\Big)+\frac1{15},\\
r_{\mathrm b}&=\frac45\Big(\frac{r_{\mathrm a}}3+\frac{r_{\mathrm c}}2\Big)+\frac1{15}.
\end{aligned}
$$
Nhân 15: $15r_{\mathrm a}=4r_{\mathrm a}+6r_{\mathrm b}+1$, tức $11r_{\mathrm a}-6r_{\mathrm b}=1$; và $15r_{\mathrm b}=4r_{\mathrm a}+6r_{\mathrm c}+1$.

**Giải.** Thay $r_{\mathrm c}=1-r_{\mathrm a}-r_{\mathrm b}$ vào phương trình thứ hai: $15r_{\mathrm b}=4r_{\mathrm a}+6-6r_{\mathrm a}-6r_{\mathrm b}+1$, tức $2r_{\mathrm a}+21r_{\mathrm b}=7$. Nhân phương trình thứ nhất với 7, phương trình thứ hai với 2 rồi cộng: $81r_{\mathrm a}=21$, nên $r_{\mathrm a}=21/81=7/27$. Khi đó $r_{\mathrm b}=(11r_{\mathrm a}-1)/6=(231/81-81/81)/6=25/81$ và $r_{\mathrm c}=1-r_{\mathrm a}-r_{\mathrm b}=35/81$.

**Kiểm tra lại.** Phương trình của $r_{\mathrm c}$: $\tfrac45\big(\tfrac{7}{81}+\tfrac{25}{162}+\tfrac{35}{162}\big)+\tfrac1{15}=\tfrac45\cdot\tfrac{74}{162}+\tfrac1{15}=\tfrac{148}{405}+\tfrac{27}{405}=\tfrac{175}{405}=\tfrac{35}{81}$; tổng $(21+25+35)/81=1$. So với Bài tập 03.8, bước nhảy kéo các điểm về gần $1/3$: $r_{\mathrm c}$ giảm từ $6/13\approx0{,}462$ xuống $35/81\approx0{,}432$, còn $r_{\mathrm a}$ tăng từ $3/13\approx0{,}231$ lên $21/81\approx0{,}259$.
:::

::: exercise Bài tập 03.10 (Ngưỡng lưu ma trận thưa; MMDS Bài 5.2.1, §5.2.6, tr.195)
Cần lưu một ma trận Boolean $n\times n$, tức mọi phần tử là 0 hoặc 1, với $n\ge2$. Có hai cách lưu: lưu chính các bit, hoặc liệt kê vị trí các phần tử 1 thành cặp số nguyên, mỗi số nguyên cần $\lceil\log_2n\rceil$ bit. Cách thứ nhất hợp với ma trận đặc, cách thứ hai hợp với ma trận thưa. Xác định ngưỡng của tỷ lệ phần tử 1 để cách thứ hai tốn ít bit hơn.
:::

::: hint
Gọi $m$ là số phần tử 1 và $\rho=m/n^2$ là tỷ lệ của chúng. Viết số bit của hai cách theo $n$ và $m$ rồi lập bất đẳng thức ngặt.
:::

::: solution
**Hai dung lượng.** Lưu bit tốn $n^2$ bit. Liệt kê tốn $m$ cặp, mỗi cặp hai số nguyên $\lceil\log_2n\rceil$ bit, tổng $2m\lceil\log_2n\rceil$ bit.

**Ngưỡng.** Cách liệt kê tốn ít bit hơn khi và chỉ khi
$$
\begin{aligned}
&2m\lceil\log_2n\rceil<n^2\\
&\iff\rho=\frac m{n^2}<\frac1{2\lceil\log_2n\rceil}.
\end{aligned}
$$

**Kiểm tra lại.** Với $n=4$, $\lceil\log_24\rceil=2$ và ngưỡng là $\rho<1/4$, tức ít hơn 4 phần tử 1 trong 16: với $m=3$, liệt kê tốn $3\cdot2\cdot2=12<16$ bit; với $m=4$, tốn đúng 16 bit. Với $n=10^9$ của Tình huống 03.1, $\lceil\log_2n\rceil=30$ và ngưỡng là $1/60$, trong khi đồ thị web có khoảng $10^{10}$ cạnh trên $10^{18}$ ô, $\rho\approx10^{-8}$.
:::

## Mức vận dụng

::: exercise Bài tập 03.11 (Nhóm trang liên kết đôi một và một trang đích chung; MMDS Bài 5.1.3, §5.1.7, tr.188)
Đồ thị web gồm một *nhóm trang liên kết đôi một* (clique) có $N\ge2$ trang, tức mọi cặp trang khác nhau của nhóm có cạnh theo cả hai chiều, và thêm một trang $X$ là đích của mọi trang trong nhóm; $X$ không có liên kết ra. Ở bài này $N$ là số trang của nhóm, nên đồ thị có $N+1$ trang. MMDS Hình 5.8 vẽ trường hợp $N=4$. Xác định PageRank của từng trang theo Định nghĩa 03.8, dưới dạng hàm của $N$ và $\beta$.
:::

![Bốn trang của một nhóm liên kết đôi một, mỗi cặp nối bằng hai mũi tên ngược chiều; mỗi trang của nhóm có thêm một mũi tên tới trang X ở dưới; X không có mũi tên đi ra.](img/lec-03/note-hinh-5-8.svg)

::: hint
Theo tính đối xứng, mọi trang của nhóm có cùng điểm $p$; gọi điểm của $X$ là $x$. Mỗi trang của nhóm có bậc ra $N$; $X$ là nút cụt, nên $\delta=x$. Trừ phương trình của $X$ cho phương trình của một trang trong nhóm.
:::

::: solution
**Mô hình.** Mỗi trang của nhóm trỏ tới $N-1$ trang còn lại của nhóm và tới $X$, nên có bậc ra $N$; $\mathcal D=\{X\}$. Định lý 03.15 cho một điểm cố định duy nhất. Hoán vị các trang của nhóm không đổi đồ thị, nên ảnh của điểm cố định qua hoán vị đó vẫn là điểm cố định, và theo tính duy nhất, mọi trang của nhóm có cùng điểm $p$. Gọi $x$ là điểm của $X$ và $c=\big((1-\beta)+\beta x\big)/(N+1)$ là phần chung.

**Hai phương trình.** Một trang của nhóm nhận từ $N-1$ trang khác của nhóm, mỗi trang gửi $p/N$; $X$ nhận từ cả $N$ trang của nhóm:
$$
\begin{gathered}
p=\beta\frac{(N-1)p}{N}+c,\\
x=\beta p+c .
\end{gathered}
$$

**Giải.** Trừ hai phương trình: $x-p=\beta p-\beta(N-1)p/N=\beta p/N$, nên $x=p(N+\beta)/N$. Điều kiện tổng $Np+x=1$ cho $p\big(N+(N+\beta)/N\big)=1$, tức
$$
\begin{gathered}
p=\frac{N}{N^2+N+\beta},\\
x=\frac{N+\beta}{N^2+N+\beta}.
\end{gathered}
$$

**So với công thức đánh thuế không bù.** Công thức $v'=\beta Mv+(1-\beta)e/(N+1)$ của MMDS (§5.1.5, tr.186) không có phần bù, nên phần chung là $(1-\beta)/(N+1)$ thay cho $c$. Giải như trên được $p=\dfrac{N(1-\beta)}{(N+1)\big(N(1-\beta)+\beta\big)}$ và $x=\beta p+\dfrac{1-\beta}{N+1}$, với tổng nhỏ hơn 1. Theo Mệnh đề 03.17, chia hai điểm này cho tổng của chúng được đúng $p$, $x$ ở trên.

**Kiểm tra lại.** Với $N=4$, $\beta=4/5$: $N^2+N+\beta=104/5$, nên $p=20/104=5/26$ và $x=(24/5)\cdot(5/104)=3/13$, tổng $4\cdot5/26+3/13=1$. Thế vào: $c=(1/5+\tfrac45\cdot\tfrac3{13})/5=\tfrac{5}{65}=\tfrac1{13}$, và $\tfrac45\cdot\tfrac34\cdot\tfrac5{26}+\tfrac1{13}=\tfrac3{26}+\tfrac2{26}=\tfrac5{26}=p$. Công thức không bù cho $p=1/10$, $x=3/25$, tổng $13/25$; $\tfrac{1/10}{13/25}=\tfrac5{26}$. $X$ có điểm lớn nhất vì mọi trang của nhóm trỏ tới nó, và $x-p=\beta p/N$ giảm khi $N$ tăng.
:::

::: exercise Bài tập 03.12 (Cây nút cụt, phần đọc thêm; MMDS Bài 5.1.7, §5.1.7, tr.189)
Đồ thị gồm một trang gốc có khuyên, đồng thời là gốc của một cây nhị phân đầy đủ có $N\ge1$ mức như MMDS Hình 5.10: mức 0 là gốc, mỗi trang ở mức $h\le N-2$ trỏ tới hai con ở mức $h+1$, và các trang ở mức $N-1$ không có liên kết ra; khi $N=1$, đồ thị chỉ có gốc với khuyên. Ở bài này $N$ là số mức, không phải số trang. Áp Thuật toán 03.31 của phần đọc thêm: loại nút cụt đệ quy, tính PageRank của đồ thị còn lại, rồi khôi phục điểm của các trang đã xóa. Xác định điểm của mỗi trang.
:::

![Trang gốc ở trên có khuyên về chính nó và hai mũi tên xuống hai con; mỗi trang ở mức dưới có hai mũi tên xuống hai con; các lá ở mức cuối không có mũi tên đi ra; dấu ba chấm chỉ các mức tiếp theo.](img/lec-03/note-hinh-5-10.svg)

::: hint
Lá bị xóa trước, rồi tới các trang ở mức trên; chỉ gốc còn lại. Khi khôi phục, mỗi trang có đúng một nguồn là cha của nó; bậc ra của gốc trên toàn đồ thị là 3 khi $N\ge2$.
:::

::: solution
**Xóa.** Khi $N\ge2$, các lá ở mức $N-1$ là nút cụt; xóa chúng làm các trang ở mức $N-2$ thành nút cụt, và cứ thế lên tới mức 1. Gốc có khuyên nên không bị xóa; đồ thị còn lại là một trang với khuyên, có PageRank $\hat r_{\text{gốc}}=1$.

**Bậc ra trên toàn đồ thị.** Gốc trỏ tới chính nó và hai con, nên $d_{\text{gốc}}=3$; mỗi trang ở mức $1\le h\le N-2$ có $d=2$.

**Khôi phục.** Duyệt ngược thứ tự xóa, tức từ mức 1 xuống. Mỗi trang ở mức 1 có nguồn duy nhất là gốc, nên có điểm $1/3$. Một trang ở mức $h\ge2$ có nguồn duy nhất là cha ở mức $h-1$ với bậc 2, nên có điểm bằng nửa điểm của cha. Quy nạp theo $h$, mọi trang $v$ ở mức $h$, với $1\le h\le N-1$, có
$$
\hat r_v=\frac1{3\cdot2^{h-1}}.
$$

**Kiểm tra lại.** Mức $h$ có $2^h$ trang, nên tổng điểm của mức $h$ là $2^h/(3\cdot2^{h-1})=2/3$ với mọi $h\ge1$, và tổng toàn đồ thị là $1+\tfrac23(N-1)$: bằng 1 khi $N=1$, lớn hơn 1 khi $N\ge2$, như Nhận xét 03.32. Với $N=3$: gốc 1, hai trang mức 1 mỗi trang $1/3$, bốn lá mỗi lá $1/6$, tổng $1+2/3+2/3=7/3$.
:::
