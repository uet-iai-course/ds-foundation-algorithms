# Bài tập Bài 04 — PageRank theo chủ đề, liên kết rác và HITS

Các bài tập củng cố 04.8–04.14 dưới đây lấy từ bài tập Chương 5 của sách *Mining of Massive Datasets*, ấn bản 3 (viết tắt MMDS), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 04.k là của [ghi chú Bài 04](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html), nơi Bài tập 04.1–04.7 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Ba bài 04.9, 04.10 và 04.13, tức MMDS Bài 5.3.1, 5.4.1(a, c) và 5.5.2, là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 04](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Phân phối dịch chuyển, hai vòng PageRank theo chủ đề, điểm cố định (Mục 2.1, 2.2) | 04.2, 04.3 | 04.9 |
| 2. Bảo toàn, hội tụ, cận sai số, ghép chủ đề, chi phí (Mục 2.3–2.5) | 04.2, 04.3, 04.7 | 04.9, 04.11 (phần kiểm tra dùng Mệnh đề 04.6) |
| 3. Cụm thao túng liên kết, điểm trang đích, hệ số khuếch đại (Mục 3) | 04.4 | 04.10, 04.14 |
| 4. TrustRank và khối lượng rác (Mục 4) | 04.5 | 04.11 |
| 5. Ma trận kề $L$, phép lặp HITS, giới hạn qua véc-tơ riêng (Mục 5) | 04.6 | 04.8, 04.12, 04.13 |
| 6. Chọn phương pháp theo đầu ra, giả thiết, chi phí (Mục 6) | 04.7 | — |

## Mức nhận biết

::: exercise Bài tập 04.8 (Hai vòng HITS trên Hình 5.1; MMDS Bài 5.5.1, phần hai vòng đầu, §5.5.3, tr.208)
Đồ thị MMDS Hình 5.1 (tr.178) có bốn trang và các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$. Lập ma trận kề $L$ (Định nghĩa 04.17) và $L^{\mathsf T}$, rồi chạy hai vòng của phép cập nhật HITS từ $h^0=(1,1,1,1)$, chuẩn hóa theo giá trị lớn nhất sau mỗi phép nhân. Ghi các véc-tơ thô và véc-tơ chuẩn hóa của từng bước.
:::

![Đồ thị G4 của MMDS Hình 5.1 với bốn trang A, B, C, D và tám cạnh: A tới B, C, D; B tới A, D; C tới A; D tới B, C; các cạnh ngược chiều vẽ bằng hai đường riêng.](img/lec-04/hinh-5-1-trung-tinh.svg)

::: hint
Hàng $i$ của $L$ có số 1 ở cột của các trang mà $i$ trỏ tới. Ở mỗi vòng, tính $L^{\mathsf T}h$ trước, chuẩn hóa để được $a$, rồi mới tính $La$ bằng $a$ vừa có.
:::

::: solution
**Ma trận kề.** Theo thứ tự A, B, C, D,
$$
\begin{gathered}
L=\begin{pmatrix}0&1&1&1\\1&0&0&1\\1&0&0&0\\0&1&1&0\end{pmatrix},\\
L^{\mathsf T}=\begin{pmatrix}0&1&1&0\\1&0&0&1\\1&0&0&1\\1&1&0&0\end{pmatrix}.
\end{gathered}
$$

**Vòng một.** Mỗi trang của G4 có đúng hai cạnh vào, nên $\tilde a^1=L^{\mathsf T}\mathbf 1=(2,2,2,2)$ và $a^1=(1,1,1,1)$. Trung tâm thô là số cạnh ra của mỗi trang: $\tilde h^1=La^1=(3,2,1,2)$; chia cho 3 được $h^1=(1,2/3,1/3,2/3)$.

**Vòng hai.**

| Trang | Trang trỏ tới | $\tilde a^2$ | $a^2$ | Trang được trỏ tới | $\tilde h^2$ | $h^2$ |
|---|---|---:|---:|---|---:|---:|
| A | B, C | $2/3+1/3=1$ | $3/5$ | B, C, D | $3$ | $1$ |
| B | A, D | $1+2/3=5/3$ | $1$ | A, D | $3/5+1=8/5$ | $8/15$ |
| C | A, D | $5/3$ | $1$ | A | $3/5$ | $1/5$ |
| D | A, B | $1+2/3=5/3$ | $1$ | B, C | $2$ | $2/3$ |

Uy tín thô chia cho $5/3$; trung tâm thô chia cho $3$. Vậy $a^2=(3/5,1,1,1)$ và $h^2=(1,8/15,1/5,2/3)$.

**Kiểm tra lại.** Theo Bổ đề 04.21, $h^2=N\big((LL^{\mathsf T})^2\mathbf 1\big)$. Với
$$
LL^{\mathsf T}=\begin{pmatrix}3&1&0&2\\1&2&1&0\\0&1&1&0\\2&0&0&2\end{pmatrix},
$$
ta có $LL^{\mathsf T}\mathbf 1=(6,4,2,4)$ và $LL^{\mathsf T}(6,4,2,4)=(30,16,6,20)$; chia cho 30 được $(1,8/15,1/5,2/3)$, đúng $h^2$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 04.9 (PageRank với hai tập dịch chuyển; MMDS Bài 5.3.1, §5.3.5, tr.199)
Trên đồ thị MMDS Hình 5.15 (tr.197), tức G4 với các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$, tính PageRank theo chủ đề khi tập dịch chuyển là

- (a) chỉ A;
- (b) A và C.

Dùng $\beta=0{,}8$ như MMDS Ví dụ 5.10. Trình bày phân phối dịch chuyển, hệ phương trình và véc-tơ theo thứ tự A, B, C, D.
:::

![Đồ thị G4 của MMDS Hình 5.1 với bốn trang A, B, C, D và tám cạnh: A tới B, C, D; B tới A, D; C tới A; D tới B, C; không đánh dấu sẵn tập dịch chuyển.](img/lec-04/hinh-5-1-trung-tinh.svg)

::: hint
Giữ $M_0$ của G4 và chỉ đổi $v$. Trừ phương trình hàng D khỏi phương trình hàng B để tìm quan hệ giữa $r_{\mathrm B}$ và $r_{\mathrm D}$ trước khi giải cả hệ.
:::

::: solution
**Câu (a).** Với $v=(1,0,0,0)$ và $\beta=4/5$, Định nghĩa 04.1 cho hệ
$$
\begin{aligned}
r_{\mathrm A}&=\tfrac25r_{\mathrm B}+\tfrac45r_{\mathrm C}+\tfrac15,\\
r_{\mathrm B}&=\tfrac4{15}r_{\mathrm A}+\tfrac25r_{\mathrm D},\\
r_{\mathrm C}&=\tfrac4{15}r_{\mathrm A}+\tfrac25r_{\mathrm D},\\
r_{\mathrm D}&=\tfrac4{15}r_{\mathrm A}+\tfrac25r_{\mathrm B}.
\end{aligned}
$$
Trừ hàng D khỏi hàng B: $r_{\mathrm B}-r_{\mathrm D}=\tfrac25(r_{\mathrm D}-r_{\mathrm B})$, nên $r_{\mathrm B}=r_{\mathrm D}$. Hàng B và hàng C có cùng vế phải, nên $r_{\mathrm C}=r_{\mathrm B}$. Gọi giá trị chung là $\sigma$; hàng B cho $\sigma=\tfrac4{15}r_{\mathrm A}+\tfrac25\sigma$, tức $\sigma=\tfrac49r_{\mathrm A}$. Điều kiện tổng $r_{\mathrm A}+3\sigma=1$ cho $\tfrac73r_{\mathrm A}=1$, nên
$$
r^*=\Big(\frac37,\frac4{21},\frac4{21},\frac4{21}\Big).
$$

**Câu (b).** Với $v=(1/2,0,1/2,0)$, phần dịch chuyển là $\tfrac1{10}$ tại A và tại C, bằng 0 tại B và D. Hàng B và hàng D không đổi so với (a), nên $r_{\mathrm B}=r_{\mathrm D}=\sigma=\tfrac49r_{\mathrm A}$. Hàng C cộng thêm $\tfrac1{10}$: $r_{\mathrm C}=\sigma+\tfrac1{10}$. Điều kiện tổng $r_{\mathrm A}+3\sigma+\tfrac1{10}=1$ cho $\tfrac73r_{\mathrm A}=\tfrac9{10}$, nên
$$
r^*=\Big(\frac{27}{70},\frac6{35},\frac{19}{70},\frac6{35}\Big).
$$
Trong (b), hàng A có phần dịch chuyển $\tfrac1{10}$, bằng một nửa phần $\tfrac15$ của (a).

**Kiểm tra lại.** Hàng A của (b): $\tfrac25\cdot\tfrac6{35}+\tfrac45\cdot\tfrac{19}{70}+\tfrac1{10}=\tfrac{12}{175}+\tfrac{38}{175}+\tfrac1{10}=\tfrac27+\tfrac1{10}=\tfrac{27}{70}$. Theo Mệnh đề 04.6, vì $u=\tfrac12v_{\{\mathrm B,\mathrm D\}}+\tfrac12v_{\{\mathrm A,\mathrm C\}}$, ta có $r^*_{\{\mathrm A,\mathrm C\}}=2r^*_u-r^*_{\{\mathrm B,\mathrm D\}}$; với $r^*_u=(9/28,19/84,19/84,19/84)$ và $r^*_{\{\mathrm B,\mathrm D\}}=(9/35,59/210,19/105,59/210)$, thành phần A là $\tfrac9{14}-\tfrac9{35}=\tfrac{27}{70}$ và thành phần C là $\tfrac{19}{42}-\tfrac{19}{105}=\tfrac{19}{70}$, đúng kết quả (b).
:::

::: exercise Bài tập 04.10 (Hai biến thể của cụm thao túng; MMDS Bài 5.4.1(a, c), §5.4.6, tr.203–204)
Lặp lại phân tích cụm thao túng của MMDS §5.4.2 (Mệnh đề 04.10) cho một cụm trong đó mỗi trang hỗ trợ

- (a) chỉ trỏ tới chính nó, thay cho trỏ tới trang đích;
- (c) trỏ tới cả chính nó và trang đích.

Ý (b) của MMDS Bài 5.4.1 là Bài tập 04.14.

Giữ các giả thiết còn lại: đồ thị không có nút cụt, dịch chuyển đều, $0<\beta<1$, $m\ge1$; trang đích trỏ tới đúng $m$ trang hỗ trợ; trang hỗ trợ không nhận cạnh từ ngoài cụm, nên mọi cạnh từ ngoài vào cụm kết thúc ở trang đích; $x$ đã nhân $\beta$ và chia bậc ra tại nguồn; $b=(1-\beta)/n$. Viết phương trình của $p$ và $y$, biểu thức của $y$ theo $x$, $m$, $n$, $\beta$, và phân biệt nghiệm chính xác với xấp xỉ bỏ phần dịch chuyển trực tiếp vào trang đích.
:::

![Biến thể a: trang Đích trỏ tới m trang hỗ trợ; trang hỗ trợ H có một khuyên H tới H và không có cạnh quay về Đích.](img/lec-04/ho-tro-tu-khuyen.svg)

![Biến thể c: trang Đích trỏ tới m trang hỗ trợ; trang hỗ trợ có một khuyên và một cạnh quay về Đích.](img/lec-04/ho-tro-khuyen-va-dich.svg)

::: hint
Lập phương trình của trang hỗ trợ trước, chia điểm theo bậc ra của trang hỗ trợ: trong (a) bậc ra là 1 và cạnh duy nhất là khuyên; trong (c) bậc ra là 2.
:::

::: solution
**Câu (a).** Mỗi trang hỗ trợ nhận $\beta y/m$ từ trang đích, $\beta p$ từ khuyên của chính nó, và $b$; trang đích không còn nhận gì từ các trang hỗ trợ:
$$
\begin{gathered}
p=\frac{\beta y}m+\beta p+b,\\
y=x+b .
\end{gathered}
$$
Do đó $p=(\beta y/m+b)/(1-\beta)$, và nghiệm chính xác là $y=x+b$; bỏ phần dịch chuyển trực tiếp $b$ được $y\approx x$. Cụm không khuếch đại gì: điểm bị giữ lại ở các trang hỗ trợ.

**Câu (c).** Mỗi trang hỗ trợ có hai cạnh ra, nên mỗi cạnh mang $\beta p/2$:
$$
\begin{gathered}
p=\frac{\beta y}m+\frac\beta2p+b,\\
y=x+\frac{\beta m}2p+b .
\end{gathered}
$$
Từ phương trình thứ nhất, $(2-\beta)p=2\beta y/m+2b$. Nhân phương trình thứ hai với $2-\beta$ và thế vào:
$$
\begin{aligned}
(2-\beta)y&=(2-\beta)(x+b)\\
&\quad+\beta^2y+\beta mb .
\end{aligned}
$$
Vì $2-\beta-\beta^2=(1-\beta)(2+\beta)>0$, nghiệm chính xác là
$$
y=\frac{(2-\beta)(x+b)+\beta mb}{(1-\beta)(2+\beta)} .
$$
Bỏ phần dịch chuyển trực tiếp vào trang đích, tức số hạng $(2-\beta)b$ ở tử số, và thay $b=(1-\beta)/n$ trong số hạng $\beta mb$:
$$
\begin{aligned}
y&\approx\frac{2-\beta}{(1-\beta)(2+\beta)}\,x\\
&\quad+\frac{\beta}{2+\beta}\cdot\frac mn .
\end{aligned}
$$
Phần dịch chuyển vào các trang hỗ trợ được giữ, vì tổng $m$ phần đó tạo số hạng tỷ lệ với $m/n$.

**So sánh.** Với $\beta=0{,}85$, hệ số của $x$ trong (c) là $\tfrac{1{,}15}{0{,}15\cdot2{,}85}\approx2{,}69$, nhỏ hơn $3{,}60$ của cụm gốc (Hệ quả 04.11): khuyên giữ lại một nửa phần điểm ở trang hỗ trợ thay cho trả về trang đích.

**Kiểm tra lại.** Gắn hai biến thể vào đồ thị bảy trang của Ví dụ 04.6, $n=7$, $m=2$, $\beta=4/5$; phần G4 không đổi nên $x=\tfrac{38}{1015}$ và $b=\tfrac1{35}$. Giải đủ bảy phương trình cho $y=\tfrac{67}{1015}=x+b$ ở biến thể (a) và $y=\tfrac{317}{1421}\approx0{,}223$ ở biến thể (c), đúng hai công thức chính xác; cụm gốc có $y=\tfrac9{29}\approx0{,}310$.
:::

::: exercise Bài tập 04.11 (TrustRank với một trang tin cậy; MMDS Bài 5.4.2, §5.4.6, tr.204)
Trên đồ thị MMDS Hình 5.1 (G4: $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$), giả sử chỉ B là trang tin cậy. Dùng $\beta=4/5$.

- (a) Tính TrustRank của mỗi trang.
- (b) Tính khối lượng rác của mỗi trang.
:::

::: hint
TrustRank là PageRank theo chủ đề với $v_T=(0,1,0,0)$. Hàng C và hàng B có cùng phần theo liên kết. Với (b), dùng PageRank nền cùng $\beta=4/5$ theo Định nghĩa 04.14.
:::

::: solution
**Câu (a).** Với $v_T=(0,1,0,0)$, hệ $\rho=\tfrac45M_0\rho+\tfrac15v_T$ là
$$
\begin{aligned}
\rho_{\mathrm A}&=\tfrac45\big(\tfrac12\rho_{\mathrm B}+\rho_{\mathrm C}\big),\\
\rho_{\mathrm B}&=\tfrac45\big(\tfrac13\rho_{\mathrm A}+\tfrac12\rho_{\mathrm D}\big)+\tfrac15,\\
\rho_{\mathrm C}&=\tfrac45\big(\tfrac13\rho_{\mathrm A}+\tfrac12\rho_{\mathrm D}\big),\\
\rho_{\mathrm D}&=\tfrac45\big(\tfrac13\rho_{\mathrm A}+\tfrac12\rho_{\mathrm B}\big).
\end{aligned}
$$
Hàng C bằng hàng B trừ $\tfrac15$, nên $\rho_{\mathrm C}=\rho_{\mathrm B}-\tfrac15$. Đặt $\sigma=\rho_{\mathrm B}$. Hàng D cho $\rho_{\mathrm D}=\tfrac4{15}\rho_{\mathrm A}+\tfrac25\sigma$; thế vào hàng B: $\sigma=\tfrac4{15}\rho_{\mathrm A}+\tfrac25\big(\tfrac4{15}\rho_{\mathrm A}+\tfrac25\sigma\big)+\tfrac15$, tức $\tfrac{21}{25}\sigma=\tfrac{28}{75}\rho_{\mathrm A}+\tfrac15$ và $\sigma=\tfrac49\rho_{\mathrm A}+\tfrac5{21}$. Hàng A cho $\rho_{\mathrm A}=\tfrac45\big(\tfrac32\sigma-\tfrac15\big)=\tfrac65\sigma-\tfrac4{25}$; thế $\sigma$ vào: $\tfrac7{15}\rho_{\mathrm A}=\tfrac27-\tfrac4{25}=\tfrac{22}{175}$. Do đó
$$
\begin{aligned}
\rho&=\Big(\frac{66}{245},\frac{263}{735},\frac{116}{735},\frac{158}{735}\Big)\\
&=\frac1{735}(198,263,116,158).
\end{aligned}
$$

**Câu (b).** Với PageRank nền $r=(9/28,19/84,19/84,19/84)$ cùng $\beta=4/5$ (Ví dụ 03.13) và $s_i=1-\rho_i/r_i$:

| Trang | $r_i$ | $\rho_i$ | $s_i$ |
|---|---:|---:|---:|
| A | $9/28$ | $66/245$ | $17/105\approx0{,}162$ |
| B | $19/84$ | $263/735$ | $-387/665\approx-0{,}582$ |
| C | $19/84$ | $116/735$ | $201/665\approx0{,}302$ |
| D | $19/84$ | $158/735$ | $33/665\approx0{,}050$ |

B, trang tin cậy, có khối lượng rác âm. C có khối lượng rác lớn nhất vì chỉ nhận điểm từ A và D, còn B không trỏ tới C. Theo cách đọc của MMDS, cả bốn giá trị gần 0 hơn gần 1.

**Kiểm tra lại.** $\rho$ có tổng $\tfrac{198+263+116+158}{735}=1$. Với $T=\{\mathrm D\}$, TrustRank là $(12/49,10/49,10/49,17/49)$, và theo Mệnh đề 04.6, $\tfrac12(\rho_{\{\mathrm B\}}+\rho_{\{\mathrm D\}})$ phải bằng TrustRank với $T=\{\mathrm B,\mathrm D\}$ của Ví dụ 04.8: thành phần A là $\tfrac12\big(\tfrac{66}{245}+\tfrac{60}{245}\big)=\tfrac{63}{245}=\tfrac9{35}$, đúng. Ngoài ra $\sum_ir_is_i=\tfrac9{28}\cdot\tfrac{17}{105}+\tfrac{19}{84}\cdot\tfrac{-387+201+33}{665}=\tfrac{153}{2940}-\tfrac{153}{2940}=0$.
:::

::: exercise Bài tập 04.12 (Giới hạn HITS trên Hình 5.1; MMDS Bài 5.5.1, phần giới hạn, §5.5.3, tr.208)
Tính điểm trung tâm và điểm uy tín của mỗi trang trên đồ thị MMDS Hình 5.1 (G4: $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$), tức giới hạn của phép lặp HITS từ $h^0=(1,1,1,1)$ với chuẩn hóa theo giá trị lớn nhất. Giải bằng hệ phương trình $LL^{\mathsf T}h=\nu h$ như MMDS Ví dụ 5.15, ghi kết quả bốn chữ số thập phân, và kiểm giả thiết của Định lý 04.22.
:::

::: hint
$LL^{\mathsf T}$ có phần tử $(i,k)$ bằng số trang mà cả $i$ và $k$ cùng trỏ tới. Từ các hàng B, C, D, biểu diễn $h_{\mathrm B}$, $h_{\mathrm C}$, $h_{\mathrm D}$ theo $h_{\mathrm A}$ và $\nu$, rồi thế vào hàng A. Phương trình bậc ba thu được không có nghiệm hữu tỷ dương; giải số, chẳng hạn bằng chia đôi trên $[4,5]$, nơi đa thức đổi dấu.
:::

::: solution
**Hệ phương trình.** Với $L$ của Bài tập 04.8,
$$
LL^{\mathsf T}=\begin{pmatrix}3&1&0&2\\1&2&1&0\\0&1&1&0\\2&0&0&2\end{pmatrix}.
$$
Ví dụ, phần tử (A, D) bằng 2 vì A và D cùng trỏ tới B và C. Hệ $LL^{\mathsf T}h=\nu h$:

- $\nu h_{\mathrm A}=3h_{\mathrm A}+h_{\mathrm B}+2h_{\mathrm D}$;
- $\nu h_{\mathrm B}=h_{\mathrm A}+2h_{\mathrm B}+h_{\mathrm C}$;
- $\nu h_{\mathrm C}=h_{\mathrm B}+h_{\mathrm C}$, nên $h_{\mathrm C}=h_{\mathrm B}/(\nu-1)$;
- $\nu h_{\mathrm D}=2h_{\mathrm A}+2h_{\mathrm D}$, nên $h_{\mathrm D}=2h_{\mathrm A}/(\nu-2)$.

Thế $h_{\mathrm C}$ vào hàng B: $h_{\mathrm B}\big(\nu-2-\tfrac1{\nu-1}\big)=h_{\mathrm A}$, nên $h_{\mathrm B}=h_{\mathrm A}(\nu-1)/(\nu^2-3\nu+1)$.

**Trị riêng lớn nhất.** Thế vào hàng A và chia cho $h_{\mathrm A}\ne0$:
$$
\nu-3=\frac{\nu-1}{\nu^2-3\nu+1}+\frac4{\nu-2}.
$$
Nhân hai vế với $(\nu^2-3\nu+1)(\nu-2)$: vế trái thành $\nu^4-8\nu^3+22\nu^2-23\nu+6$, vế phải thành $5\nu^2-15\nu+6$. Hiệu là $\nu(\nu^3-8\nu^2+17\nu-8)$, đúng đa thức đặc trưng của $LL^{\mathsf T}$. Đa thức $f(\nu)=\nu^3-8\nu^2+17\nu-8$ có $f(4)=-4<0$ và $f(5)=2>0$; chia đôi trên $[4,5]$ cho nghiệm lớn nhất $\lambda_1\approx4{,}8136$; hai nghiệm còn lại xấp xỉ $2{,}5293$ và $0{,}6571$, cùng nghiệm $\nu=0$. Trị riêng lớn nhất là đơn và $h^0$ có mọi thành phần dương, nên Định lý 04.22 áp dụng được.

**Giới hạn.** Đặt $h_{\mathrm A}=1$ với $\nu=\lambda_1$: $h_{\mathrm D}=2/(\lambda_1-2)\approx0{,}7108$; $\lambda_1^2-3\lambda_1+1\approx9{,}7299$ nên $h_{\mathrm B}\approx3{,}8136/9{,}7299\approx0{,}3919$; $h_{\mathrm C}=h_{\mathrm B}/(\lambda_1-1)\approx0{,}1028$. Điểm trung tâm là
$$
\begin{aligned}
h^*\approx(&1;\,0{,}3919;\\
&0{,}1028;\,0{,}7108).
\end{aligned}
$$
Điểm uy tín là $N(L^{\mathsf T}h^*)$: A nhận từ B, C, $0{,}4947$; B và C nhận từ A, D, $1{,}7108$; D nhận từ A, B, $1{,}3919$. Chia cho $1{,}7108$:
$$
a^*\approx(0{,}2892;\,1;\,1;\,0{,}8136).
$$
A là trang trung tâm lớn nhất vì trỏ tới ba trang; B và C là hai trang uy tín lớn nhất vì được A và D, hai trang trung tâm lớn nhất, trỏ tới.

**Kiểm tra lại.** Hàng A: $3+0{,}3919+2\cdot0{,}7108=4{,}8135\approx\lambda_1$. Vòng thứ ba của phép lặp cho $h^3=(1,34/73,11/73,50/73)\approx(1;\,0{,}466;\,0{,}151;\,0{,}685)$, còn cách $h^*$ khoảng $0{,}07$ ở thành phần B; theo Bước 4 của chứng minh Định lý 04.22, phần sai lệch giảm theo $(\lambda_2/\lambda_1)^t$ với $\lambda_2/\lambda_1\approx2{,}5293/4{,}8136\approx0{,}53$.
:::

## Mức vận dụng

::: exercise Bài tập 04.13 (HITS trên chuỗi có khuyên; MMDS Bài 5.5.2, bài khó của MMDS, §5.5.3, tr.208; Hình 5.9, tr.189)
Đồ thị là một chuỗi $n$ trang như MMDS Hình 5.9: $n\ge1$, cạnh $1\to1$ và các cạnh $i\to i+1$ với $1\le i<n$. Tính các véc-tơ trung tâm và uy tín theo $n$: chạy phép lặp HITS từ $h^0=a^0=\mathbf 1$, chuẩn hóa theo giá trị lớn nhất sau mỗi phép nhân, và tìm hai véc-tơ giới hạn, kể cả hai trường hợp $n=1$ và $n=2$.
:::

![Chuỗi có khuyên tại trang 1: cạnh 1 tới 1 và các cạnh i tới i cộng 1; dấu chấm lửng thay các trang giữa; trang n không có cạnh ra.](img/lec-04/chuoi-co-khuyen.svg)

::: hint
Với $n\ge2$, hàng 1 của $L$ có số 1 ở cột 1 và cột 2; mỗi hàng giữa có một số 1; hàng cuối toàn 0. Các hàng khác nhau có số 1 ở các cột khác nhau, nên $LL^{\mathsf T}$ là ma trận đường chéo.
:::

::: solution
**Ma trận $LL^{\mathsf T}$.** Với $n\ge2$, hai hàng khác nhau của $L$ không có cột chung nào chứa số 1, nên
$$
LL^{\mathsf T}=\mathrm{diag}(2,\underbrace{1,\ldots,1}_{n-2},0).
$$

**Phép lặp.** Từ $h^0=\mathbf 1$, mỗi trang nhận đúng một cạnh vào (trang 1 từ khuyên, trang $i+1$ từ trang $i$), nên $\tilde a^1=\mathbf 1$ và $a^1=\mathbf 1$. Trung tâm thô là số cạnh ra: $(2,1,\ldots,1,0)$; chia cho 2 được $h^1=(1,1/2,\ldots,1/2,0)$.

Quy nạp: giả sử $h^t=(1,2^{-t},\ldots,2^{-t},0)$ với $t\ge1$. Trang 1 và trang 2 cùng nhận từ trang 1, nên hai thành phần đầu của $\tilde a^{t+1}$ bằng 1; trang $i\ge3$ nhận từ trang $i-1$ với điểm $2^{-t}$. Giá trị lớn nhất là 1, nên $a^{t+1}=(1,1,2^{-t},\ldots,2^{-t})$. Trung tâm thô tiếp theo là $(1+1,2^{-t},\ldots,2^{-t},0)$: trang 1 cộng uy tín của trang 1 và trang 2, trang $i$ giữa cộng uy tín của trang $i+1$, trang $n$ không có cạnh ra. Chia cho 2 được $h^{t+1}=(1,2^{-(t+1)},\ldots,2^{-(t+1)},0)$. Vậy với $t\ge1$,
$$
\begin{aligned}
h^t&=(1,\underbrace{2^{-t},\ldots,2^{-t}}_{n-2},0),\\
a^t&=(1,1,\underbrace{2^{-(t-1)},\ldots,2^{-(t-1)}}_{n-2}).
\end{aligned}
$$

**Giới hạn.** Lấy giới hạn khi $t\to\infty$:
$$
\begin{gathered}
h^*=(1,0,\ldots,0),\\
a^*=(1,1,0,\ldots,0).
\end{gathered}
$$
Với $n=2$, các phần giữa rỗng: $h^t=(1,0)$ và $a^t=(1,1)$ từ vòng đầu. Với $n=1$, khuyên $1\to1$ vẫn còn, $L=[1]$ và $h^t=a^t=(1)$ ở mọi vòng; không có phép chia cho 0.

**Kiểm tra lại.** Với $n=4$, ba vòng đầu cho $h=(1,1/2,1/2,0)$, $(1,1/4,1/4,0)$, $(1,1/8,1/8,0)$ và $a=(1,1,1,1)$, $(1,1,1/2,1/2)$, $(1,1,1/4,1/4)$, đúng công thức với $t=1,2,3$. Kết quả cũng khớp Định lý 04.22: với $n\ge2$, trị riêng lớn nhất của $LL^{\mathsf T}$ là $\lambda_1=2$, đơn, với véc-tơ riêng là véc-tơ đơn vị của trang 1, nên $h^*=N(\psi_1)=(1,0,\ldots,0)$; $L^{\mathsf T}\psi_1$ có số 1 ở trang 1 và trang 2, nên $a^*=(1,1,0,\ldots,0)$. Khi $n\ge3$, $\lambda_2=1$, và các thành phần giữa của $h^t$ bằng $(\lambda_2/\lambda_1)^t=2^{-t}$, đúng số hạng của Bước 4 trong chứng minh định lý.
:::

::: exercise Bài tập 04.14 (Trang hỗ trợ không có cạnh ra; MMDS Bài 5.4.1(b), §5.4.6, tr.203–204)
Lặp lại phân tích cụm thao túng của MMDS §5.4.2 (Mệnh đề 04.10) cho một cụm trong đó mỗi trang hỗ trợ không trỏ tới trang nào. Giữ các giả thiết còn lại: ngoài các trang hỗ trợ, đồ thị không có nút cụt; dịch chuyển đều; phần điểm của nút cụt được bù đều cho $n$ trang như Định nghĩa 03.8; $0<\beta<1$; trang đích trỏ tới đúng $m$ trang hỗ trợ; trang hỗ trợ không nhận cạnh từ ngoài cụm, nên mọi cạnh từ ngoài vào cụm kết thúc ở trang đích; $b=(1-\beta)/n$. Viết phương trình của $p$ và $y$, nghiệm chính xác của $y$, và xấp xỉ khi $n$ lớn; so với cụm gốc.
:::

![Biến thể b: một mũi tên nhãn x vào trang Đích; Đích trỏ tới các trang hỗ trợ H1, H2, …, Hm; các trang hỗ trợ có viền nét đứt và nhãn không có cạnh ra.](img/lec-04/note-ho-tro-nut-cut.svg)

::: hint
Các trang hỗ trợ là nút cụt, nên tổng điểm nút cụt là $\delta=mp$, và mỗi trang, kể cả trang đích và trang hỗ trợ, nhận thêm phần bù $\beta mp/n$.
:::

::: solution
**Phương trình.** Mỗi trang hỗ trợ nhận $\beta y/m$ từ trang đích, phần dịch chuyển $b$ và phần bù $\beta\delta/n=\beta mp/n$; trang đích nhận $x$, $b$ và phần bù, nhưng không nhận gì theo liên kết từ trang hỗ trợ:
$$
\begin{gathered}
p=\frac{\beta y}m+b+\frac{\beta mp}n,\\
y=x+b+\frac{\beta mp}n .
\end{gathered}
$$

**Nghiệm chính xác.** Từ phương trình thứ nhất, $p\,(n-\beta m)/n=\beta y/m+b$, nên $\dfrac{\beta mp}n=\dfrac{\beta^2y+\beta mb}{n-\beta m}$, với $n-\beta m>0$ vì $m<n$. Thế vào phương trình thứ hai và nhân với $n-\beta m$:
$$
\begin{aligned}
&y\,(n-\beta m-\beta^2)\\
&\quad=(x+b)(n-\beta m)+\beta mb .
\end{aligned}
$$
Vì $n\ge m+1$ và $\beta<1$, $n-\beta m-\beta^2>0$, nên
$$
y=\frac{(x+b)(n-\beta m)+\beta mb}{n-\beta m-\beta^2} .
$$

**Xấp xỉ khi $n$ lớn.** Khi $n$ lớn, $b=(1-\beta)/n$ và phần bù $\beta mp/n$ đều nhỏ, nên $y\approx x$: cụm không khuếch đại đóng góp từ ngoài. Phần điểm trang đích gửi tới các trang hỗ trợ dừng ở đó, rồi được chia đều cho cả $n$ trang, nên trang đích chỉ nhận lại phần $1/n$ của nó. So với cụm gốc, với hệ số $1/(1-\beta^2)\approx3{,}6$ khi $\beta=0{,}85$, biến thể này mất toàn bộ tác dụng; nó cũng kém biến thể (c) của Bài tập 04.10.

**Kiểm tra lại.** Gắn biến thể vào đồ thị bảy trang của Ví dụ 04.6: $n=7$, $m=2$, $\beta=4/5$, $b=\tfrac1{35}$. Giải đủ bảy phương trình có bù nút cụt cho $r^*_{\mathrm C}=\tfrac{475}{2843}$, nên $x=\tfrac45\cdot\tfrac12\cdot\tfrac{475}{2843}=\tfrac{190}{2843}$, và $y=\tfrac{335}{2843}\approx0{,}118$, $p=\tfrac{279}{2843}$. Công thức nghiệm chính xác với $n-\beta m=\tfrac{27}5$ và $n-\beta m-\beta^2=\tfrac{119}{25}$ cho cùng $y=\tfrac{335}{2843}$; cụm gốc trên cùng đồ thị có $y=\tfrac9{29}\approx0{,}310$.
:::
