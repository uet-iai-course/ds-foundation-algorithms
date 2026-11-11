# Bài tập Bài 06 — Tìm cặp tương đồng bằng LSH

Các bài tập củng cố 06.15–06.30 dưới đây đi kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 06.k là của [ghi chú Bài 06](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-tim-cap-tuong-dong-bang-lsh.html), nơi Bài tập 06.1–06.14 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bảy bài 06.20–06.25 và 06.28 lấy từ phần bài tập của Leskovec, Rajaraman và Ullman, *Mining of Massive Datasets* (MMDS), ấn bản 3, Chương 3, và là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 06](lecture-06-tim-cap-tuong-dong-bang-lsh.html); Bài tập 06.26 là phần (d) của Bài 3.7.5, dành cho tự học. Ba điểm của Bài 3.7.5 được ký hiệu $z_1,z_2,z_3$ (MMDS viết $p_1,p_2,p_3$, trùng với hai cận của họ nhạy cảm); vector $z$ không chỉ số trong Bài 3.7.2 giữ tên của đề sách. Tên vector trong Bài tập 06.23 viết chữ đứng $\mathrm A,\mathrm B,\mathrm C,\mathrm D$ để không trùng số tài liệu $C$ và số chiều $D$. Máy tính được dùng cho lũy thừa và $\arccos$; không có yêu cầu viết chương trình. Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Phân dải, khử lặp, xác minh; ứng viên giả và cặp bỏ sót (Mục 1, Mục 2.1–2.2) | 06.1, 06.2 | 06.17, 06.30 |
| 2. Xác suất thành ứng viên, chọn $b$, $r$, đếm công việc (Mục 2.3–2.5) | 06.3, 06.4 | 06.16, 06.18, 06.20, 06.21, 06.29 |
| 3. Năm độ đo khoảng cách, họ nhạy cảm, phép ghép AND và OR (Mục 3) | 06.5, 06.6, 06.7 | 06.15, 06.19, 06.22 |
| 4. Họ chọn tọa độ, họ siêu phẳng, họ chiếu có dịch và chi phí chữ ký (Mục 4) | 06.8–06.11 | 06.23–06.27 |
| 5. Đối sánh thực thể, đối sánh vân tay, bản tin gần trùng (Mục 5, Tình huống 06.1–06.4) | 06.12–06.14 | 06.28 |

## Mức nhận biết

::: exercise Bài tập 06.15
Dữ kiện: họ MinHash trên các tập hữu hạn, không rỗng với khoảng cách Jaccard (Hệ quả 06.23).

Viết bộ tham số của họ MinHash với $d_1=0{,}2$, $d_2=0{,}5$, rồi bộ tham số của họ sau phép ghép đồng thời bậc 2.
:::

::: hint
Hệ quả 06.23 cho $p_i=1-d_i$; phép ghép đồng thời giữ $d_1$, $d_2$ và bình phương hai mức xác suất.
:::

::: solution
Họ MinHash là $(0{,}2;\ 0{,}5;\ 0{,}8;\ 0{,}5)$-nhạy cảm. Với hai hàm độc lập, phép ghép đồng thời bậc 2 cho $(0{,}2;\ 0{,}5;\ 0{,}64;\ 0{,}25)$.

**Kiểm tra lại.** Hai ngưỡng khoảng cách không đổi khi ghép; $0{,}8^2=0{,}64$ và $0{,}5^2=0{,}25$.
:::

::: exercise Bài tập 06.16
Dữ kiện: phân dải với $b$ dải, $r$ hàng mỗi dải, $P_{b,r}(s)=1-(1-s^r)^b$ (Định lý 06.7).

Giữ $r$ và tăng $b$. Xác định ảnh hưởng tới số cặp bỏ sót và tới $K$.
:::

::: hint
Xét chiều biến thiên của $(1-s^r)^b$ theo $b$ với $s$ cố định trong $(0,1)$.
:::

::: solution
Với $0<s<1$, $0<1-s^r<1$ nên $(1-s^r)^b$ giảm khi $b$ tăng, và $P_{b,r}(s)$ tăng với mọi $s$. Mỗi cặp đạt ngưỡng có xác suất bỏ sót nhỏ hơn, nên kỳ vọng của số cặp bỏ sót giảm; mỗi cặp xa cũng có xác suất thành ứng viên lớn hơn, nên kỳ vọng của $K$ và của thời gian xác minh tăng; kỳ vọng của $Q$ cũng tăng vì có thêm dải (Mệnh đề 06.13). Độ dài chữ ký $n=br$ và chi phí lập chữ ký cũng tăng.

**Kiểm tra lại.** Tại $s=0{,}8$, $r=5$: $b=20$ cho xác suất bỏ sót $0{,}67232^{20}\approx0{,}000356$, nhỏ hơn $0{,}67232$ của $b=1$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 06.17
Dữ kiện: ma trận chữ ký có hai hàng $(2,1,2,0)$ và $(1,1,1,1)$ cho bốn tài liệu; $b=2$, $r=1$.

Tính $Q$, $K$ và nêu cặp được phát lặp.
:::

::: hint
Lập các thùng của từng dải; một thùng cỡ $u$ phát $\binom u2$ cặp.
:::

::: solution
Dải 1 có các thùng $\{1,3\}$ (giá trị 2), $\{2\}$, $\{4\}$; dải 2 có một thùng $\{1,2,3,4\}$ (giá trị 1). Do đó $Q=\binom22+\binom42=1+6=7$. Dải 2 đã phát đủ sáu cặp, nên $K=6$, và cặp $(1,3)$ được phát hai lần.

**Kiểm tra lại.** $Q-K=1$, đúng một lượt phát lặp.
:::

::: exercise Bài tập 06.18
Dữ kiện: phân dải với $b=10$, $r=4$ (Định lý 06.7, Nhận xét 06.10).

Tính ngưỡng xấp xỉ $(1/b)^{1/r}$ và xác suất thành ứng viên của cặp có $s=0{,}8$ và $s=0{,}3$.
:::

::: hint
Tính $s^4$ trước, rồi thế vào (2.1); làm tròn ở bước cuối.
:::

::: solution
$(1/10)^{1/4}=0{,}1^{1/4}\approx0{,}562$. Với $s=0{,}8$: $0{,}8^4=0{,}4096$ và $P=1-(1-0{,}4096)^{10}\approx0{,}9949$. Với $s=0{,}3$: $0{,}3^4=0{,}0081$ và $P=1-(1-0{,}0081)^{10}\approx0{,}0781$.

**Kiểm tra lại.** $0{,}562^4\approx0{,}0998$, gần $1/b=0{,}1$.
:::

::: exercise Bài tập 06.19
Dữ kiện: họ siêu phẳng với pháp tuyến đẳng hướng (Định lý 06.32); cặp gần là cặp có $\theta\le\pi/6$, cặp xa là cặp có $\theta\ge\pi/2$.

Tính $p_1$, $p_2$ và hai cận sau phép ghép AND 2 rồi OR 2.
:::

::: hint
Định lý 06.32 cho $p_i=1-d_i/\pi$; cấu trúc AND 2 rồi OR 2 là $F(p)=1-(1-p^2)^2$.
:::

::: solution
$p_1=1-1/6=5/6$ và $p_2=1-1/2=1/2$. Với $F(p)=1-(1-p^2)^2$: $F(5/6)\approx0{,}9066$ và $F(1/2)=1-(3/4)^2=0{,}4375$.

**Kiểm tra lại.** $(5/6)^2=25/36$, $1-25/36=11/36$, $(11/36)^2\approx0{,}0934$, nên $F(5/6)\approx0{,}9066$.
:::

::: exercise Bài tập 06.20 (Bài 3.4.1, MMDS §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$ (Định lý 06.7); ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$, viết theo thứ tự $(r,b)$ của đề sách.

Tính $P(s)$ cho $s=0{,}1;\ 0{,}2;\ \ldots;\ 0{,}9$ với cả ba cấu hình. Sản phẩm là bảng 27 xác suất.
:::

::: hint
Giữ thứ tự $(r,b)$ của đề. Tính $s^r$ trước, rồi $(1-s^r)^b$, và chỉ làm tròn kết quả cuối.
:::

::: solution
| $s$ | $r=3,b=10$ | $r=6,b=20$ | $r=5,b=50$ |
|---:|---:|---:|---:|
| 0,1 | 0,009955120 | 0,000020000 | 0,000499878 |
| 0,2 | 0,077180588 | 0,001279222 | 0,015875200 |
| 0,3 | 0,239448893 | 0,014479467 | 0,114539882 |
| 0,4 | 0,483870732 | 0,078809323 | 0,402283952 |
| 0,5 | 0,736924424 | 0,270187144 | 0,795550630 |
| 0,6 | 0,912267475 | 0,615414636 | 0,982533828 |
| 0,7 | 0,985015105 | 0,918185997 | 0,999898996 |
| 0,8 | 0,999234054 | 0,997712125 | 0,999999998 |
| 0,9 | 0,999997864 | 0,999999740 | xấp xỉ 1 |

Giá trị cuối bảng chỉ làm tròn về $1$, không bằng $1$ chính xác. Đổi chỗ $r$ và $b$ cho một hàm khác: chẳng hạn $(r,b)=(10,3)$ cho $P(0{,}5)=1-(1-2^{-10})^3\approx0{,}002927$, khác $0{,}736924424$ của $(3,10)$.

**Kiểm tra lại.** Tại $s=0{,}1$, $r=3$, $b=10$: $1-(1-0{,}001)^{10}\approx0{,}009955$.
:::

::: exercise Bài tập 06.21 (Bài 3.4.2, MMDS §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$; ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$ của Bài tập 06.20.

Với từng cấu hình, tìm $s$ để $P(s)=1/2$ và so với xấp xỉ $(1/b)^{1/r}$. Sản phẩm là phép biến đổi và bảng ba cặp ngưỡng.
:::

::: hint
Cô lập $(1-s^r)^b$ trước, rồi lấy căn bậc $b$ và căn bậc $r$ (Mệnh đề 06.9).
:::

::: solution
Biến đổi $1-(1-s^r)^b=1/2$ cho $s=(1-2^{-1/b})^{1/r}$.

| $(r,b)$ | Nghiệm chính xác | Xấp xỉ $(1/b)^{1/r}$ |
|---|---:|---:|
| $(3,10)$ | 0,406088134 | 0,464158883 |
| $(6,20)$ | 0,569353387 | 0,606962231 |
| $(5,50)$ | 0,424394480 | 0,457305052 |

Cả ba xấp xỉ lớn hơn nghiệm một nửa. Các nghiệm này là tính chất của cấu hình, không phải ngưỡng $t$ do bài toán đặt (Nhận xét 06.10).

**Kiểm tra lại.** Với $(3,10)$: $0{,}406088134^3\approx0{,}066967$, và $(1-0{,}066967)^{10}\approx0{,}5$.
:::

::: exercise Bài tập 06.22 (Bài 3.6.1(a–d), MMDS §3.6.4, tr.108)
Dữ kiện: $p$ là xác suất trùng của một MinHash cơ sở; mọi phép ghép dùng các bản thử độc lập (Mệnh đề 06.26).

Viết xác suất nhận cặp sau các chuỗi ghép, theo thứ tự từ trái sang phải:

- (a) AND 2 rồi OR 3.
- (b) OR 3 rồi AND 2.
- (c) AND 2, OR 2, AND 2.
- (d) OR 2, AND 2, OR 2, AND 2.

Sản phẩm là bốn biểu thức, có trạng thái trung gian cho từng tầng.
:::

::: hint
Mỗi tầng AND $k$ thay xác suất $q$ bằng $q^k$; mỗi tầng OR $k$ thay $q$ bằng $1-(1-q)^k$.
:::

::: solution
(a) $p\to p^2\to1-(1-p^2)^3$.

(b) $p\to1-(1-p)^3\to\bigl[1-(1-p)^3\bigr]^2$.

(c) $p\to p^2\to1-(1-p^2)^2\to\bigl[1-(1-p^2)^2\bigr]^2$.

(d) Đặt $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$; kết quả là $q_3^2$.

Mỗi tầng dùng các bản thử độc lập của tầng trước. Đảo thứ tự AND và OR nói chung làm đổi biểu thức, như (a) so với (b).

**Kiểm tra lại.** Tại $p=1$ cả bốn biểu thức bằng $1$; tại $p=0$ cả bốn bằng $0$.
:::

::: exercise Bài tập 06.23 (Bài 3.7.1, MMDS §3.7.6, tr.113)
Dữ kiện: họ gồm sáu hàm $h_i(x)=x_i$, $i=1,\ldots,6$ (Định nghĩa 06.28); bốn vector $\mathrm A=000000$, $\mathrm B=110011$, $\mathrm C=010101$, $\mathrm D=011100$.

Với mỗi cặp vector, xác định các hàm làm cặp đó thành ứng viên. Sản phẩm là sáu tập chỉ số cho các cặp AB, AC, AD, BC, BD, CD.
:::

::: hint
Đánh chỉ số từ 1. Hàm $h_i$ nhận cặp khi hai bit ở vị trí $i$ bằng nhau.
:::

::: solution
| Cặp | Chỉ số hàm nhận cặp | Hamming để đối chiếu |
|---|---|---:|
| AB | 3, 4 | 4 |
| AC | 1, 3, 5 | 3 |
| AD | 1, 5, 6 | 3 |
| BC | 2, 3, 6 | 3 |
| BD | 2 | 5 |
| CD | 1, 2, 4, 5 | 2 |

Số hàm nhận một cặp bằng $6$ trừ khoảng cách Hamming, nên cặp CD gần nhất được nhiều hàm nhận nhất, cặp BD xa nhất chỉ được một hàm nhận.

**Kiểm tra lại.** Ở mỗi hàng, số chỉ số cộng khoảng cách Hamming bằng $6$.
:::

::: exercise Bài tập 06.24 (Bài 3.7.2, MMDS §3.7.6, tr.113–114)
Dữ kiện: bốn pháp tuyến

$$
v_1=(1,1,1,-1),\quad v_2=(1,1,-1,1),\quad v_3=(1,-1,1,1),\quad v_4=(-1,1,1,1);
$$

ba vector $x=(2,3,4,5)$, $y=(-2,3,-4,5)$, $z=(2,-3,4,-5)$; quy ước $\operatorname{sign}(0)=+1$.

Tính chữ ký dấu của ba vector. Với mỗi cặp, tính góc ước lượng từ chữ ký (Thuật toán 06.33) và góc thật. Sản phẩm là bảng tích và dấu, và bảng ba cặp góc.
:::

::: hint
Tính bốn tích vô hướng trước khi lấy dấu. Góc ước lượng bằng $\pi$ nhân tỷ lệ bit khác; góc thật tính từ tích vô hướng của hai vector gốc.
:::

::: solution
| Vector | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký |
|---|---|---|
| $x$ | $(4,6,8,10)$ | $(+,+,+,+)$ |
| $y$ | $(-8,10,-4,6)$ | $(-,+,-,+)$ |
| $z$ | $(8,-10,4,-6)$ | $(+,-,+,-)$ |

Bình phương ba chuẩn đều bằng $54$; $x\cdot y=14$, $x\cdot z=-14$, $y\cdot z=-54$.

| Cặp | Tỷ lệ khác dấu | Góc ước lượng | Góc thật |
|---|---:|---|---|
| $x,y$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(7/27)\approx74{,}973886^\circ$ |
| $x,z$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(-7/27)\approx105{,}026114^\circ$ |
| $y,z$ | $4/4$ | $\pi=180^\circ$ | $\pi=180^\circ$ |

Bốn pháp tuyến là dữ kiện cố định, không phải mẫu đẳng hướng, nên vết tính không bảo đảm góc ước lượng bằng góc thật (Tình huống 06.4).

**Kiểm tra lại.** $14/54=7/27$; $y=-z$ nên góc giữa $y$ và $z$ bằng $\pi$.
:::

::: exercise Bài tập 06.25 (Bài 3.7.5(a–c), MMDS §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ (sách ký hiệu $p_1,p_2,p_3$). Ba hàm là phép chiếu lên ba trục tọa độ; các khoảng có dạng $[ka,(k+1)a)$ với $k\in\mathbb Z$ (sách viết chỉ số là $j$; chương này dành $j$ cho số dải), không dịch biên.

- (a) Gán thùng với $a=1$.
- (b) Lặp lại với $a=2$.
- (c) Tìm các cặp ứng viên trong mỗi trường hợp.

Sản phẩm là hai bảng mã theo trục và hai tập cặp.
:::

::: hint
Mã của một điểm ở trục $i$ là $\lfloor x_i/a\rfloor$. Chỉ so mã trong cùng trục; số trục là một phần của khóa, như số dải ở Định nghĩa 06.3.
:::

::: solution
| $a$ | Mã của $z_1$ theo ba trục | Mã của $z_2$ | Mã của $z_3$ | Tập cặp |
|---:|---|---|---|---|
| 1 | $(1,2,3)$ | $(0,2,4)$ | $(4,3,2)$ | $\{(1,2)\}$ |
| 2 | $(0,1,1)$ | $(0,1,2)$ | $(2,1,1)$ | $\{(1,2),(1,3),(2,3)\}$ |

Với $a=1$, chỉ $z_1$, $z_2$ trùng ở trục 2. Với $a=2$, cặp $(1,2)$ trùng ở trục 1 và trục 2; cặp $(1,3)$ trùng ở trục 2 và trục 3; cặp $(2,3)$ trùng ở trục 2. Hợp các cặp theo trục và khử lặp cho tập kết quả.

**Kiểm tra lại.** Một tọa độ bằng $a$ thuộc $[a,2a)$, không thuộc $[0,a)$: tọa độ $2$ với $a=2$ có mã $1$.
:::

::: exercise Bài tập 06.26 (Bài 3.7.5(d), MMDS §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ và ba phép chiếu lên ba trục tọa độ như Bài tập 06.25; độ rộng $a>0$ tùy ý, khoảng nửa mở $[ka,(k+1)a)$, $k\in\mathbb Z$, không dịch biên.

Với mỗi cặp điểm, tìm mọi giá trị $a$ làm cặp đó thành ứng viên.
:::

::: hint
Hai số $\alpha<\beta$ không âm cùng mã khi $\lfloor\alpha/a\rfloor=\lfloor\beta/a\rfloor$. Xét riêng giá trị mã chung bằng $0$ và bằng một số nguyên $k\ge1$.
:::

::: solution
**Cặp $(1,2)$.** Hai điểm có cùng tọa độ thứ hai, bằng $2$, nên luôn chung thùng ở trục 2: ứng viên với mọi $a>0$.

**Cặp $(1,3)$ và $(2,3)$ ở trục 2.** Hai tọa độ là $2$ và $3$. Mã chung bằng $0$ khi $a>3$. Mã chung bằng một số nguyên $k\ge1$ khi đồng thời $ka\le2$ và $3<(k+1)a$, tức

$$
\frac3{k+1}<a\le\frac2k .
$$

Khoảng này khác rỗng chỉ khi $3k<2(k+1)$, tức $k<2$, nên chỉ $k=1$ và $a\in(3/2,2]$.

**Các trục còn lại.** Ở trục 1, cặp $(1,3)$ có tọa độ $1$ và $4$, cặp $(2,3)$ có $0$ và $4$; ở trục 3, cặp $(2,3)$ có $4$ và $2$. Mỗi trường hợp chỉ trùng mã khi $a>4$, đã nằm trong $(3,\infty)$. Ở trục 3, cặp $(1,3)$ có tọa độ $3$ và $2$, lặp lại điều kiện của trục 2.

**Kết luận.** Mỗi cặp $(1,3)$, $(2,3)$ là ứng viên đúng khi

$$
a\in(3/2,2]\cup(3,\infty).
$$

**Kiểm tra lại.** Tại $a=3/2$, $\lfloor3/1{,}5\rfloor=2\ne\lfloor2/1{,}5\rfloor=1$; tại $a=3$, $\lfloor3/3\rfloor=1\ne\lfloor2/3\rfloor=0$; tại $a=2$, hai tọa độ $2$ và $3$ cùng mã $1$. Quy tắc nửa mở quyết định các dấu đóng, mở này.
:::

## Mức vận dụng

::: exercise Bài tập 06.27
Dữ kiện: kho $C$ ảnh, mỗi ảnh một vector đặc trưng thực 128 chiều; cần tìm các cặp ảnh có góc nhỏ.

Chọn họ cơ sở trong Mục 4 và nêu chi phí tính chữ ký $m$ bit.
:::

::: hint
Xác định độ đo của bài toán trước, rồi dùng Mệnh đề 06.38.
:::

::: solution
Dùng họ siêu phẳng (Định lý 06.32), vì độ đo là góc và chỉ phụ thuộc hướng. Theo Mệnh đề 06.38 với $D=128$, tính chữ ký cần $C\cdot m\cdot128$ phép nhân, tức $O(CmD)$; mỗi ảnh lưu $m$ bit, và các pháp tuyến cần $128m$ số. Dựng thùng, phát cặp và xác minh được tính thêm theo Mệnh đề 06.11.

**Kiểm tra lại.** Họ chọn tọa độ dùng cho Hamming trên vector rời rạc, còn họ chiếu có dịch đo khoảng cách Euclid, phụ thuộc cả độ dài; cả hai không đo đúng góc.
:::

::: exercise Bài tập 06.28 (Bài 3.8.2(a,b), MMDS §3.8.7, tr.121)
Dữ kiện: mỗi ô có điểm đặc trưng với xác suất $0{,}2$; với hai ảnh cùng ngón, ảnh thứ hai có điểm đặc trưng tại một ô đã có ở ảnh thứ nhất với xác suất $0{,}8$; mỗi hàm chọn ba ô từ lưới trước khi xét ảnh; các hàm độc lập theo mô hình (Mệnh đề 06.42). Gọi $F_1$ là OR 1024 hàm và $F_2$ là OR 2048 hàm.

- (a) Tính xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón của $F_2$.
- (b) So với cấu trúc AND hai nhóm $F_1$ độc lập.

Sản phẩm là bảng hai xác suất cho hai cấu trúc cùng 2048 hàm.
:::

::: hint
Tính $q_F$ và $q_T$ từ mô hình một ô rồi ba ô. Với cặp cùng ngón, bỏ sót là biến cố bù của được nhận. Không dùng các giá trị đã làm tròn như $0{,}063$ làm đầu vào ghép tiếp.
:::

::: solution
Xác suất cơ sở là $q_F=0{,}2^6=0{,}000064$ và $q_T=(0{,}2\cdot0{,}8)^3=0{,}004096$.

| Cấu trúc | Nhận cặp khác ngón | Bỏ sót cặp cùng ngón |
|---|---:|---:|
| $F_2$: OR 2048 | $1-(1-q_F)^{2048}\approx0{,}122849062$ | $(1-q_T)^{2048}\approx0{,}000223559$ |
| AND hai nhóm $F_1$ | $\bigl[1-(1-q_F)^{1024}\bigr]^2\approx0{,}004024207$ | $1-\bigl[1-(1-q_T)^{1024}\bigr]^2\approx0{,}029680224$ |

OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn. AND hai nhóm OR 1024 giảm ứng viên giả và tăng bỏ sót. Hai phương án cùng ngân sách 2048 hàm, nên khác biệt đến từ cấu trúc ghép. Các xác suất trên là xác suất cả hai ảnh có đủ ba ô, không phải xác suất có điều kiện khi ảnh truy vấn đã có ba ô (Mệnh đề 06.42).

Các phép nhân qua 1024 hoặc 2048 hàm dùng giả thiết độc lập thêm của MMDS (Ví dụ 06.18), không suy ra từ Mệnh đề 06.26. Với $p$ là xác suất va chạm của một cặp ảnh cùng ngón cố định theo cách chọn ba ô, $q_T=\mathbb E[p]$ và xác suất bỏ sót thật của $F_2$ là $\mathbb E[(1-p)^{2048}]$. Hàm $t\mapsto(1-t)^{2048}$ lồi, nên theo bất đẳng thức Jensen xác suất này ít nhất $(1-q_T)^{2048}\approx0{,}000223559$: số bỏ sót của $F_2$ trong bảng là cận dưới. Với AND hai nhóm $F_1$, hàm $t\mapsto1-[1-(1-t)^{1024}]^2$ không lồi cũng không lõm, nên số $0{,}029680224$ dựa trên giả định độc lập và không có bất đẳng thức một chiều.

**Kiểm tra lại.** $(1-q_T)^{2048}$ là bình phương của $(1-q_T)^{1024}\approx0{,}014951892$, và $0{,}014951892^2\approx0{,}000223559$.
:::

::: exercise Bài tập 06.29
Dữ kiện: chữ ký dài $n=100$; bốn cấu hình $(b,r)\in\{(50,2),(25,4),(20,5),(10,10)\}$, đều có $br=100$; ngưỡng $t=0{,}6$; bài toán ưu tiên tránh bỏ sót các cặp đạt ngưỡng.

(a) Tính $s_{1/2}$ theo (2.2) và xấp xỉ $(1/b)^{1/r}$ cho bốn cấu hình.

(b) Theo quy tắc của Nhận xét 06.10, giữ các cấu hình có $(1/b)^{1/r}<t$; trong số đó chọn cấu hình có $P_{b,r}(0{,}3)$ nhỏ nhất, với $s=0{,}3$ là cặp xa đại diện như Ví dụ 06.5.

(c) Với cấu hình được chọn, tính xác suất bỏ sót một cặp có $s=0{,}7$.
:::

::: hint
Câu (b) cần $P_{b,r}(0{,}3)=1-(1-0{,}3^r)^b$ cho các cấu hình còn lại sau bước lọc. Câu (c) dùng Hệ quả 06.8.
:::

::: solution
(a)

| $(b,r)$ | $s_{1/2}$ | $(1/b)^{1/r}$ | $P_{b,r}(0{,}3)$ |
|---|---:|---:|---:|
| $(50,2)$ | 0,117334119 | 0,141421356 | 0,991044917 |
| $(25,4)$ | 0,406648983 | 0,447213595 | 0,183986664 |
| $(20,5)$ | 0,508695962 | 0,549280272 | 0,047494259 |
| $(10,10)$ | 0,763108147 | 0,794328235 | 0,000059047 |

(b) Ba cấu hình đầu có $(1/b)^{1/r}<0{,}6$; cấu hình $(10,10)$ bị loại vì vùng chuyển tiếp nằm trên $t$. Trong ba cấu hình còn lại, $(20,5)$ có $P_{b,r}(0{,}3)$ nhỏ nhất, nên được chọn.

(c) Theo Hệ quả 06.8, xác suất bỏ sót là $(1-0{,}7^5)^{20}=(1-0{,}16807)^{20}=0{,}83193^{20}\approx0{,}025219456$.

**Kiểm tra lại.** Cấu hình bị loại $(10,10)$ bỏ sót cặp $s=0{,}7$ với xác suất $(1-0{,}7^{10})^{10}\approx0{,}750855826$, lớn hơn nhiều so với $0{,}025$; điều này khớp với việc nó đặt vùng chuyển tiếp trên $t$.
:::

::: exercise Bài tập 06.30
Dữ kiện: một biến thể của Thuật toán 06.4 dùng $b$ bảng băm $B_1,\ldots,B_b$ so khóa đầy đủ. Ở bước 2, cột $c$ của dải $j$ được nối vào danh sách $B_j[z_{j,c}]$, với khóa chỉ là tuple; bước 3 duyệt mọi danh sách của mọi bảng. Ma trận chữ ký có $n=4$, $b=2$, $r=2$ và ba cột, mỗi cột viết từ hàng 1 đến hàng 4: cột 1 là $(1,2,3,4)$, cột 2 là $(3,4,1,2)$, cột 3 là $(1,2,5,6)$.

(a) Chứng minh tập $\mathrm{CAND}$ của biến thể bằng tập ứng viên $\mathcal C$ của Định nghĩa 06.3.

(b) Tính $\mathcal C$, tập $\mathrm{CAND}$ của biến thể, và tập $\mathrm{CAND}$ khi dùng một bảng duy nhất với khóa chỉ là tuple.
:::

::: hint
Câu (a) lặp lại bất biến của chứng minh Mệnh đề 06.5 cho từng bảng $B_j$; số dải nằm ở việc chọn bảng thay vì nằm trong khóa. Câu (b) viết hai tuple của mỗi cột trước khi dựng thùng.
:::

::: solution
(a) Bảng $B_j$ chỉ nhận các lượt chèn của dải $j$. Áp dụng bất biến của Bước 1 và Bước 2 trong chứng minh Mệnh đề 06.5 cho riêng $B_j$: khi bước 2 kết thúc, danh sách $B_j[z]$ là đúng tập $\{c:\ z_{j,c}=z\}$. Do đó $c$, $d$ chung một danh sách của $B_j$ khi và chỉ khi $z_{j,c}=z_{j,d}$, tức $k_{j,c}=k_{j,d}$. Bước 3 thêm $(c,d)$ vào $\mathrm{CAND}$ khi và chỉ khi tồn tại $j$ để $c$, $d$ chung một danh sách của $B_j$, tức tồn tại $j$ với $k_{j,c}=k_{j,d}$. Theo Định nghĩa 06.3, $\mathrm{CAND}=\mathcal C$. $\square$

(b) Tuple ở dải 1 là $(1,2)$, $(3,4)$, $(1,2)$ cho ba cột; ở dải 2 là $(3,4)$, $(1,2)$, $(5,6)$. Chỉ cột 1 và cột 3 trùng một dải, nên $\mathcal C=\{(1,3)\}$.

| Cách tổ chức | Danh sách có ít nhất hai cột | $\mathrm{CAND}$ |
|---|---|---|
| $b$ bảng | $B_1[(1,2)]=[1,3]$ | $\{(1,3)\}$ |
| Một bảng, khóa chỉ là tuple | $[(1,2)]=[1,3,2]$; $[(3,4)]=[2,1]$ | $\{(1,2),(1,3),(2,3)\}$ |

Với một bảng có khóa chỉ là tuple, tuple $(1,2)$ của cột 2 ở dải 2 rơi vào danh sách của cột 1 và cột 3 ở dải 1, và tuple $(3,4)$ của cột 1 ở dải 2 rơi vào danh sách của cột 2 ở dải 1. Hai cặp $(1,2)$ và $(2,3)$ được phát dù không trùng dải nào: $\mathrm{CAND}\ne\mathcal C$.

**Kiểm tra lại.** Cặp $(1,2)$ so dải 1: $(1,2)\ne(3,4)$; dải 2: $(3,4)\ne(1,2)$. Cặp $(2,3)$ so dải 1: $(3,4)\ne(1,2)$; dải 2: $(1,2)\ne(5,6)$. Cả hai không thuộc $\mathcal C$.
:::
