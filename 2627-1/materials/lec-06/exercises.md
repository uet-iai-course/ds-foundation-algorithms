# Bài tập Bài 06 — Tìm cặp tương đồng bằng LSH

Các bài tập củng cố 06.15–06.30 dưới đây đi kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 06.k là của [ghi chú Bài 06](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-tim-cap-tuong-dong-bang-lsh.html), nơi Bài tập 06.1–06.14 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Mọi bài lấy từ phần bài tập của Leskovec, Rajaraman và Ullman, *Mining of Massive Datasets* (MMDS), ấn bản 3, Chương 3; bảy bài 06.20–06.25 và 06.28 là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 06](lecture-06-tim-cap-tuong-dong-bang-lsh.html); các bài còn lại dành cho tự học. Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Phân dải, khử lặp, xác minh; ứng viên giả và cặp bỏ sót (Mục 1, Mục 2.1–2.2) | 06.1, 06.2 | — |
| 2. Xác suất thành ứng viên, chọn $b$, $r$, đếm công việc (Mục 2.3–2.5) | 06.3, 06.4 | 06.20, 06.21 |
| 3. Năm độ đo khoảng cách, họ nhạy cảm, phép ghép AND và OR (Mục 3) | 06.5, 06.6, 06.7 | 06.15–06.19, 06.22 |
| 4. Họ chọn tọa độ, họ siêu phẳng, họ chiếu có dịch và chi phí chữ ký (Mục 4) | 06.8–06.11 | 06.23–06.26, 06.29 |
| 5. Đối sánh thực thể, đối sánh vân tay, bản tin gần trùng (Mục 5, Tình huống 06.1–06.4) | 06.12–06.14 | 06.27, 06.28, 06.30 |

## Mức nhận biết

::: exercise Bài tập 06.15 (Khoảng cách Jaccard của hai cặp tập; MMDS Bài 3.5.4, §3.5.7, tr.102)
Dữ kiện: hai cặp tập hữu hạn, không rỗng.

- (a) $\{1,2,3,4\}$ và $\{2,3,4,5\}$.
- (b) $\{1,2,3\}$ và $\{4,5,6\}$.

Tính khoảng cách Jaccard của từng cặp.
:::

::: hint
Tính độ tương đồng Jaccard từ cỡ của giao và hợp, rồi dùng $d_J=1-\mathrm{SIM}$ (Mệnh đề 06.15).
:::

::: solution
**Câu (a).** Giao là $\{2,3,4\}$, có $3$ phần tử; hợp là $\{1,2,3,4,5\}$, có $5$ phần tử. Do đó $\mathrm{SIM}=3/5$ và $d_J=1-3/5=2/5$.

**Câu (b).** Giao rỗng, hợp có $6$ phần tử, nên $\mathrm{SIM}=0$ và $d_J=1$.

**Kiểm tra lại.** Cả hai giá trị nằm trong $[0,1]$, như Mệnh đề 06.15; hai tập rời nhau cho giá trị lớn nhất $1$.
:::

::: exercise Bài tập 06.16 (Khoảng cách $L_1$ và $L_2$; MMDS Bài 3.5.2, §3.5.7, tr.102)
Dữ kiện: hai điểm $x=(5,6,7)$ và $y=(8,2,4)$ trong $\mathbb R^3$.

Tính khoảng cách $L_1$ và khoảng cách $L_2$ giữa $x$ và $y$.
:::

::: hint
Tính độ lệch tuyệt đối theo từng tọa độ trước, rồi thế vào công thức $\lVert x-y\rVert_q$ của Định nghĩa 06.14 với $q=1$ và $q=2$.
:::

::: solution
Độ lệch theo ba tọa độ là $\lvert5-8\rvert=3$, $\lvert6-2\rvert=4$, $\lvert7-4\rvert=3$. Do đó

$$
\lVert x-y\rVert_1=3+4+3=10,\qquad \lVert x-y\rVert_2=\sqrt{9+16+9}=\sqrt{34}\approx5{,}831.
$$

**Kiểm tra lại.** $9+16+9=34$, và $5{,}831^2\approx34{,}0$. Độ lệch lớn nhất là $L_\infty=4$, và $4\le5{,}831\le10$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 06.17 (Cosin và góc của bốn cặp véc-tơ (vector); MMDS Bài 3.5.5, §3.5.7, tr.102)
Dữ kiện: bốn cặp véc-tơ khác $0$.

- (a) $(3,-1,2)$ và $(-2,3,1)$.
- (b) $(1,2,3)$ và $(2,4,6)$.
- (c) $(5,0,-4)$ và $(-1,-6,2)$.
- (d) $(0,1,1,0,1,1)$ và $(0,0,1,0,0,0)$.

Với từng cặp, tính cosin của góc giữa hai véc-tơ và góc $\theta$ (Định nghĩa 06.16).
:::

::: hint
Tính tích vô hướng và bình phương hai chuẩn trước; $\cos\theta=x\cdot y/(\lVert x\rVert_2\lVert y\rVert_2)$, rồi lấy $\arccos$.
:::

::: solution
| Câu | $x\cdot y$ | $\lVert x\rVert_2^2$; $\lVert y\rVert_2^2$ | $\cos\theta$ | $\theta$ |
|---|---:|---|---:|---|
| (a) | $-7$ | $14$; $14$ | $-1/2$ | $2\pi/3=120^\circ$ |
| (b) | $28$ | $14$; $56$ | $1$ | $0$ |
| (c) | $-13$ | $41$; $41$ | $-13/41\approx-0{,}3171$ | $\approx108{,}486^\circ$ |
| (d) | $1$ | $4$; $1$ | $1/2$ | $\pi/3=60^\circ$ |

**Câu (a).** $x\cdot y=-6-3+2=-7$ và $\sqrt{14\cdot14}=14$, nên $\cos\theta=-1/2$.

**Câu (b).** $\sqrt{14\cdot56}=\sqrt{784}=28$, nên $\cos\theta=28/28=1$ và $\theta=0$.

**Câu (c).** $x\cdot y=-5+0-8=-13$ và $\sqrt{41\cdot41}=41$.

**Câu (d).** Chỉ tọa độ thứ ba cho tích khác $0$, nên $x\cdot y=1$; $\sqrt{4\cdot1}=2$, nên $\cos\theta=1/2$.

**Kiểm tra lại.** Ở (b), véc-tơ thứ hai bằng $2$ lần véc-tơ thứ nhất, nên hai véc-tơ cùng hướng và góc bằng $0$, khớp với $\cos\theta=1$. Ở (c), $\cos108{,}486^\circ\approx-0{,}3171\approx-13/41$.
:::

::: exercise Bài tập 06.18 (Khoảng cách chỉnh sửa của ba cặp chuỗi; MMDS Bài 3.5.7, §3.5.7, tr.102)
Dữ kiện: ba cặp chuỗi; chỉ dùng thao tác chèn hoặc xóa một ký tự (Định nghĩa 06.18).

- (a) $abcdef$ và $bdaefc$.
- (b) $abccdabc$ và $acbdcab$.
- (c) $abcdef$ và $baedfc$.

Tính khoảng cách chỉnh sửa của từng cặp.
:::

::: hint
Tìm một dãy con chung dài nhất, rồi dùng $d(x,y)=\lvert x\rvert+\lvert y\rvert-2L$ (Mệnh đề 06.19).
:::

::: solution
**Câu (a).** Dãy con chung dài nhất là $bdef$, $L=4$, nên $d=6+6-2\cdot4=4$.

**Câu (b).** Dãy con chung dài nhất là $abcab$, $L=5$, nên $d=8+7-2\cdot5=5$.

**Câu (c).** Dãy con chung dài nhất là $bdf$, $L=3$, nên $d=6+6-2\cdot3=6$.

**Kiểm tra lại.** Mỗi câu có một vết sửa đúng số thao tác:

- (a) xóa $a$, $c$ được $bdef$; chèn $a$ sau $d$ và chèn $c$ ở cuối được $bdaefc$: $4$ thao tác.
- (b) xóa chữ $c$ thứ hai, chữ $d$ và chữ $c$ cuối được $abcab$; chèn $c$ sau chữ $a$ đầu và chèn $d$ sau chữ $b$ được $acbdcab$: $5$ thao tác.
- (c) xóa $a$, $c$, $e$ được $bdf$; chèn $a$, $e$ sau $b$ và chèn $c$ ở cuối được $baedfc$: $6$ thao tác.
:::

::: exercise Bài tập 06.19 (Ba hàm trên số nguyên không âm; MMDS Bài 3.5.1, §3.5.7, tr.101–102)
Dữ kiện: miền là tập số nguyên không âm; ba hàm

- (a) $\max(x,y)$;
- (b) $\lvert x-y\rvert$;
- (c) $x+y$.

Xác định hàm nào là độ đo khoảng cách theo Định nghĩa 06.14. Chứng minh ba tiên đề cho hàm là độ đo; với hàm không là độ đo, chỉ ra tiên đề bị vi phạm bằng một phản ví dụ.
:::

::: hint
Kiểm tiên đề 1 tại một cặp $x=y>0$ trước.
:::

::: solution
**Câu (a).** Không là độ đo: $\max(1,1)=1\ne0$, nên tiên đề 1 bị vi phạm.

**Câu (b).** Là độ đo. Hàm nhận giá trị không âm. Tiên đề 1: $\lvert x-y\rvert=0$ khi và chỉ khi $x=y$. Tiên đề 2: $\lvert x-y\rvert=\lvert y-x\rvert$. Tiên đề 3: với mọi $x,y,w$,

$$
\lvert x-w\rvert=\lvert(x-y)+(y-w)\rvert\le\lvert x-y\rvert+\lvert y-w\rvert
$$

theo bất đẳng thức tam giác của giá trị tuyệt đối. $\square$

**Câu (c).** Không là độ đo: $1+1=2\ne0$, nên tiên đề 1 bị vi phạm.

**Kiểm tra lại.** Tại $x=y=0$ cả ba hàm bằng $0$, nên phản ví dụ ở (a) và (c) phải dùng $x=y>0$.
:::

::: exercise Bài tập 06.20 (Đường cong S của ba cấu hình; MMDS Bài 3.4.1, §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$ (Định lý 06.7); ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$, viết theo thứ tự $(r,b)$ của đề sách.

Lập bảng 27 giá trị $P(s)$ cho $s=0{,}1;\ 0{,}2;\ \ldots;\ 0{,}9$ với cả ba cấu hình.
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
| 0,9 | 0,999997864 | 0,999999740 | $1-0{,}40951^{50}\approx1-4{,}1\cdot10^{-20}$ |

**Kiểm tra lại.** Tại $s=0{,}1$, $r=3$, $b=10$: $1-(1-0{,}001)^{10}\approx0{,}009955$.
:::

::: exercise Bài tập 06.21 (Nghiệm một nửa so với xấp xỉ; MMDS Bài 3.4.2, §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$; ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$ của Bài tập 06.20.

Với từng cấu hình, giải $P(s)=1/2$ và lập bảng so nghiệm với xấp xỉ $(1/b)^{1/r}$.
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

Cả ba xấp xỉ lớn hơn nghiệm một nửa. Nghiệm của $P(s)=1/2$ chỉ phụ thuộc $(r,b)$; ngưỡng $t$ do bài toán đặt (Nhận xét 06.10).

**Kiểm tra lại.** Với $(3,10)$: $0{,}406088134^3\approx0{,}066967$, và $(1-0{,}066967)^{10}\approx0{,}5$.
:::

::: exercise Bài tập 06.22 (Bốn chuỗi ghép; MMDS Bài 3.6.1(a–d), §3.6.4, tr.108)
Dữ kiện: $p$ là xác suất trùng của một MinHash cơ sở; mọi phép ghép dùng các bản thử độc lập (Mệnh đề 06.26).

Viết xác suất nhận cặp sau các chuỗi ghép, theo thứ tự từ trái sang phải, kèm xác suất trung gian sau từng tầng:

- (a) AND 2 rồi OR 3.
- (b) OR 3 rồi AND 2.
- (c) AND 2, OR 2, AND 2.
- (d) OR 2, AND 2, OR 2, AND 2.
:::

::: hint
Mỗi tầng AND $k$ thay xác suất $q$ bằng $q^k$; mỗi tầng OR $k$ thay $q$ bằng $1-(1-q)^k$.
:::

::: solution
**Câu (a).** $p\to p^2\to1-(1-p^2)^3$.

**Câu (b).** $p\to1-(1-p)^3\to\bigl[1-(1-p)^3\bigr]^2$.

**Câu (c).** $p\to p^2\to1-(1-p^2)^2\to\bigl[1-(1-p^2)^2\bigr]^2$.

**Câu (d).** Đặt $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$; kết quả là $q_3^2$.

Tại $p=1/2$, (a) cho $37/64\approx0{,}578$, (b) cho $49/64\approx0{,}766$, nên đảo thứ tự AND và OR làm đổi xác suất nhận cặp.

**Kiểm tra lại.** Tại $p=1$ cả bốn biểu thức bằng $1$; tại $p=0$ cả bốn bằng $0$.
:::

::: exercise Bài tập 06.23 (Họ chọn tọa độ trên sáu bit; MMDS Bài 3.7.1, §3.7.6, tr.113)
Dữ kiện: họ gồm sáu hàm $h_i(x)=x_i$, $i=1,\ldots,6$ (Định nghĩa 06.28); bốn véc-tơ $\mathrm A=000000$, $\mathrm B=110011$, $\mathrm C=010101$, $\mathrm D=011100$.

Với mỗi cặp AB, AC, AD, BC, BD, CD, xác định tập chỉ số của các hàm làm cặp đó thành ứng viên.
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

**Kiểm tra lại.** Tổng số lần nhận qua sáu cặp là $2+3+3+3+1+4=16$. Đếm theo hàm, $h_1,\ldots,h_6$ nhận lần lượt $3$, $3$, $3$, $2$, $3$, $2$ cặp, cũng có tổng $16$, và $16=6\cdot6-20$ với $20$ là tổng khoảng cách Hamming của sáu cặp.
:::

::: exercise Bài tập 06.24 (Chữ ký dấu với bốn pháp tuyến; MMDS Bài 3.7.2, §3.7.6, tr.113–114)
Dữ kiện: bốn pháp tuyến

$$
v_1=(1,1,1,-1),\quad v_2=(1,1,-1,1),\quad v_3=(1,-1,1,1),\quad v_4=(-1,1,1,1);
$$

ba véc-tơ $x=(2,3,4,5)$, $y=(-2,3,-4,5)$, $z=(2,-3,4,-5)$; quy ước $\operatorname{sign}(0)=+1$.

Lập bảng tích vô hướng và chữ ký dấu của ba véc-tơ. Với mỗi cặp, tính góc ước lượng từ chữ ký (Thuật toán 06.33) và góc thật.
:::

::: hint
Tính bốn tích vô hướng trước khi lấy dấu. Góc ước lượng bằng $\pi$ nhân tỷ lệ bit khác; góc thật tính từ tích vô hướng của hai véc-tơ gốc.
:::

::: solution
| Véc-tơ | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký |
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

Bốn pháp tuyến cố định, trái với giả thiết pháp tuyến đẳng hướng của Định lý 06.32, nên ví dụ nằm ngoài bảo đảm của định lý (Tình huống 06.4).

**Kiểm tra lại.** $14/54=7/27$; $y=-z$ nên góc giữa $y$ và $z$ bằng $\pi$.
:::

::: exercise Bài tập 06.25 (Chiếu lên trục với $a=1$, $a=2$; MMDS Bài 3.7.5(a–c), §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$. Ba hàm là phép chiếu lên ba trục tọa độ; các khoảng có dạng $[ka,(k+1)a)$ với $k\in\mathbb Z$, không dịch biên. Một cặp là ứng viên khi hai điểm cùng mã ở ít nhất một trục (mỗi trục là một dải với $r=1$).

- (a) Gán thùng với $a=1$.
- (b) Lặp lại với $a=2$.
- (c) Tìm các cặp ứng viên trong mỗi trường hợp.
:::

::: hint
Mã của một điểm ở trục $i$ là $\lfloor x_i/a\rfloor$. Chỉ so mã trong cùng trục; số trục là một phần của khóa, như số dải ở Định nghĩa 06.3.
:::

::: solution
**Câu (a) và Câu (b).** Mã theo ba trục:

| $a$ | Mã của $z_1$ theo ba trục | Mã của $z_2$ | Mã của $z_3$ |
|---:|---|---|---|
| $1$ (trục 1 như Ví dụ 06.16) | $(1,2,3)$ | $(0,2,4)$ | $(4,3,2)$ |
| 2 | $(0,1,1)$ | $(0,1,2)$ | $(2,1,1)$ |

**Câu (c).** Với $a=1$, chỉ $z_1$, $z_2$ trùng mã ở trục 2, nên tập cặp là $\{(1,2)\}$. Với $a=2$, cặp $(1,2)$ trùng ở trục 1 và trục 2; cặp $(1,3)$ trùng ở trục 2 và trục 3; cặp $(2,3)$ trùng ở trục 2. Hợp các cặp theo trục và khử lặp cho $\{(1,2),(1,3),(2,3)\}$.

**Kiểm tra lại.** Một tọa độ bằng $a$ thuộc $[a,2a)$, không thuộc $[0,a)$: tọa độ $2$ với $a=2$ có mã $1$.
:::

::: exercise Bài tập 06.26 (Mọi độ rộng $a$ cho từng cặp; MMDS Bài 3.7.5(d), §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ và ba phép chiếu lên ba trục tọa độ như Bài tập 06.25; độ rộng $a>0$ tùy ý, khoảng nửa mở $[ka,(k+1)a)$, $k\in\mathbb Z$, không dịch biên. Một cặp là ứng viên khi hai điểm cùng mã ở ít nhất một trục (mỗi trục là một dải với $r=1$).

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

**Các trục còn lại.** Ở trục 1, cặp $(1,3)$ có tọa độ $1$ và $4$, cặp $(2,3)$ có $0$ và $4$; ở trục 3, cặp $(2,3)$ có $4$ và $2$. Mã chung bằng $0$ khi $a>4$. Mã chung bằng $k\ge1$ cần $4/(k+1)<a\le1/k$ với hai tọa độ $1$, $4$, hoặc $4/(k+1)<a\le2/k$ với hai tọa độ $2$, $4$; hai khoảng này rỗng với mọi $k\ge1$, vì $4k<k+1$ và $4k<2(k+1)$ đều sai. Hai tọa độ $0$, $4$ chỉ có mã chung $0$. Vậy các trục này chỉ cho ứng viên khi $a>4$, đã nằm trong $(3,\infty)$. Ở trục 3, cặp $(1,3)$ có tọa độ $3$ và $2$, lặp lại điều kiện của trục 2.

**Kết luận.** Mỗi cặp $(1,3)$, $(2,3)$ là ứng viên đúng khi

$$
a\in(3/2,2]\cup(3,\infty).
$$

**Kiểm tra lại.** Tại $a=3/2$, $\lfloor3/1{,}5\rfloor=2\ne\lfloor2/1{,}5\rfloor=1$; tại $a=3$, $\lfloor3/3\rfloor=1\ne\lfloor2/3\rfloor=0$; tại $a=2$, hai tọa độ $2$ và $3$ cùng mã $1$. Quy tắc nửa mở quyết định các dấu đóng, mở này.
:::

## Mức vận dụng

::: exercise Bài tập 06.27 (Kiểm đối sánh tài liệu tham khảo bằng năm xuất bản; MMDS Bài 3.8.1, §3.8.7, tr.121)
Dữ kiện: đối sánh thực thể trên các tài liệu tham khảo; mỗi cặp được chấm điểm theo độ tương đồng của tiêu đề, danh sách tác giả và nơi xuất bản. Mọi tài liệu có năm xuất bản, và năm này đồng khả năng là một trong mười năm gần nhất. Trong các cặp đạt điểm tối đa, độ lệch năm xuất bản trung bình là $0{,}1$. Các cặp ở một mức điểm cố định có độ lệch năm trung bình là $2$.

- (a) Tính chính xác độ lệch năm trung bình của một cặp hai tài liệu chọn ngẫu nhiên.
- (b) Tính tỷ phần các cặp ở mức điểm đó thực sự cùng một tài liệu.
:::

::: hint
Với hai năm độc lập, mỗi năm đều trên mười giá trị, độ lệch $\lvert\Delta\rvert$ bằng $k\in\{1,\ldots,9\}$ với xác suất $2(10-k)/100$. Câu (b) dùng mô hình hỗn hợp hai thành phần của Tình huống 06.1.
:::

::: solution
**Câu (a).** Hai năm của một cặp ngẫu nhiên độc lập và đều trên mười giá trị. Có $2(10-k)$ cặp năm có thứ tự với $\lvert\Delta\rvert=k$, nên

$$
\mathbb E\lvert\Delta\rvert=\sum_{k=1}^{9}k\cdot\frac{2(10-k)}{100}=\frac{330}{100}=3{,}3.
$$

**Câu (b).** Như Tình huống 06.1, coi nhóm cặp ở mức điểm này là hỗn hợp: tỷ phần $\eta$ cùng một tài liệu, có độ lệch trung bình $0{,}1$ như các cặp điểm tối đa, và tỷ phần $1-\eta$ ghép ngẫu nhiên, có độ lệch trung bình $3{,}3$. Khi đó

$$
2=0{,}1\eta+3{,}3(1-\eta),\qquad \eta=\frac{3{,}3-2}{3{,}2}=\frac{13}{32}\approx0{,}406.
$$

**Kiểm tra lại.** $\sum_{k=1}^9k(10-k)=10\cdot45-285=165$, nên tổng ở Câu (a) là $330/100$. Thế ngược: $0{,}1\cdot13/32+3{,}3\cdot19/32=64/32=2$.
:::

::: exercise Bài tập 06.28 (OR 2048 so với AND hai nhóm OR 1024; MMDS Bài 3.8.2(a,b), §3.8.7, tr.121)
Dữ kiện: mỗi ô có điểm đặc trưng với xác suất $0{,}2$; với hai ảnh cùng ngón, ảnh thứ hai có điểm đặc trưng tại một ô đã có ở ảnh thứ nhất với xác suất $0{,}8$; mỗi hàm chọn ba ô từ lưới trước khi xét ảnh (Mệnh đề 06.42); các hàm chọn độc lập, và dùng giả thiết độc lập thêm của Ví dụ 06.18. Gọi $F_1$ là OR 1024 hàm và $F_2$ là OR 2048 hàm.

- (a) Tính xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón của $F_2$.
- (b) Lập bảng so hai xác suất đó với cấu trúc AND hai nhóm $F_1$ độc lập; hai cấu trúc cùng dùng 2048 hàm.
:::

::: hint
Tính $q_F$ và $q_T$ từ mô hình một ô rồi ba ô. Với cặp cùng ngón, bỏ sót là biến cố bù của được nhận. Không dùng các giá trị đã làm tròn như $0{,}063$ làm đầu vào ghép tiếp.
:::

::: solution
Xác suất cơ sở là $q_F=0{,}2^6=0{,}000064$ và $q_T=(0{,}2\cdot0{,}8)^3=0{,}004096$.

**Câu (a).** $F_2$ nhận cặp khác ngón với xác suất $1-(1-q_F)^{2048}\approx0{,}122849062$ và bỏ sót cặp cùng ngón với xác suất $(1-q_T)^{2048}\approx0{,}000223559$.

**Câu (b).**

| Cấu trúc | Nhận cặp khác ngón | Bỏ sót cặp cùng ngón |
|---|---:|---:|
| $F_2$: OR 2048 | $1-(1-q_F)^{2048}\approx0{,}122849062$ | $(1-q_T)^{2048}\approx0{,}000223559$ |
| AND hai nhóm $F_1$ (Ví dụ 06.18) | $\bigl[1-(1-q_F)^{1024}\bigr]^2\approx0{,}004024207$ | $1-\bigl[1-(1-q_T)^{1024}\bigr]^2\approx0{,}029680224$ |

Cùng 2048 hàm, OR 2048 nhận cặp khác ngón nhiều gấp khoảng 30 lần ($0{,}1228$ so với $0{,}0040$) và bỏ sót ít hơn khoảng 130 lần ($0{,}00022$ so với $0{,}0297$). $q_F$, $q_T$ là xác suất cả hai ảnh có đủ ba ô (Mệnh đề 06.42). Số bỏ sót $0{,}000223559$ của $F_2$, tính theo giả thiết độc lập thêm, là cận dưới của xác suất bỏ sót thật, vì hàm $\xi\mapsto(1-\xi)^{2048}$ lồi (Tình huống 06.2).

**Kiểm tra lại.** $(1-q_T)^{2048}$ là bình phương của $(1-q_T)^{1024}\approx0{,}014951892$, và $0{,}014951892^2\approx0{,}000223559$.
:::

::: exercise Bài tập 06.29 (Chữ ký dấu với 16 pháp tuyến $\pm1$; MMDS Bài 3.7.3, §3.7.6, tr.114)
Dữ kiện: ba véc-tơ $x=(2,3,4,5)$, $y=(-2,3,-4,5)$, $z=(2,-3,4,-5)$ của Bài tập 06.24; pháp tuyến là cả 16 véc-tơ của $\mathbb R^4$ có tọa độ $\pm1$; quy ước $\operatorname{sign}(0)=+1$.

- (a) Tính chữ ký dấu 16 bit của ba véc-tơ.
- (b) Với mỗi cặp, tính góc ước lượng $\widehat\theta=\pi\widehat p_{\ne}$ của Thuật toán 06.33 và so với góc thật.
:::

::: hint
Tính 16 tích vô hướng cho mỗi véc-tơ, chú ý các tích bằng $0$. Góc thật của ba cặp đã có ở lời giải Bài tập 06.24.
:::

::: solution
**Câu (a).**

| Pháp tuyến $v$ | $v\cdot x$ | $v\cdot y$ | $v\cdot z$ | Dấu $x$, $y$, $z$ |
|---|---:|---:|---:|---|
| $(1,1,1,1)$ | 14 | 2 | −2 | $+,+,-$ |
| $(1,1,1,-1)$ | 4 | −8 | 8 | $+,-,+$ |
| $(1,1,-1,1)$ | 6 | 10 | −10 | $+,+,-$ |
| $(1,1,-1,-1)$ | −4 | 0 | 0 | $-,+,+$ |
| $(1,-1,1,1)$ | 8 | −4 | 4 | $+,-,+$ |
| $(1,-1,1,-1)$ | −2 | −14 | 14 | $-,-,+$ |
| $(1,-1,-1,1)$ | 0 | 4 | −4 | $+,+,-$ |
| $(1,-1,-1,-1)$ | −10 | −6 | 6 | $-,-,+$ |
| $(-1,1,1,1)$ | 10 | 6 | −6 | $+,+,-$ |
| $(-1,1,1,-1)$ | 0 | −4 | 4 | $+,-,+$ |
| $(-1,1,-1,1)$ | 2 | 14 | −14 | $+,+,-$ |
| $(-1,1,-1,-1)$ | −8 | 4 | −4 | $-,+,-$ |
| $(-1,-1,1,1)$ | 4 | 0 | 0 | $+,+,+$ |
| $(-1,-1,1,-1)$ | −6 | −10 | 10 | $-,-,+$ |
| $(-1,-1,-1,1)$ | −4 | 8 | −8 | $-,+,-$ |
| $(-1,-1,-1,-1)$ | −14 | −2 | 2 | $-,-,+$ |

Chữ ký dấu của mỗi véc-tơ là cột dấu tương ứng, theo thứ tự các hàng. Tích bằng $0$ xảy ra với $x$ tại $\pm(1,-1,-1,1)$, và với $y$, $z$ tại $\pm(1,1,-1,-1)$; theo quy ước, các bit đó là $+$.

**Câu (b).**

| Cặp | Số bit khác | Góc ước lượng | Góc thật |
|---|---:|---|---|
| $x,y$ | 6 | $\pi\cdot6/16=67{,}5^\circ$ | $\approx74{,}974^\circ$ |
| $x,z$ | 10 | $\pi\cdot10/16=112{,}5^\circ$ | $\approx105{,}026^\circ$ |
| $y,z$ | 14 | $\pi\cdot14/16=157{,}5^\circ$ | $180^\circ$ |

Với bốn pháp tuyến của Bài tập 06.24, ba góc ước lượng là $90^\circ$, $90^\circ$, $180^\circ$. Mười sáu pháp tuyến đưa hai cặp đầu lại gần góc thật hơn, sai số giảm từ khoảng $15^\circ$ xuống khoảng $7{,}5^\circ$, nhưng cặp $y,z$ sai $22{,}5^\circ$: tại hai pháp tuyến vuông góc với $y$, cả $y$ và $z=-y$ nhận bit $+$. Phân phối đều trên 16 véc-tơ $\pm1$ không đẳng hướng, nên Định lý 06.32 không bảo đảm các ước lượng này (Tình huống 06.4).

**Kiểm tra lại.** Vì $z=-y$, ở 14 pháp tuyến có $v\cdot y\ne0$, bit của $z$ ngược bit của $y$, nên $y$, $z$ khác nhau ở đúng 14 bit, và ở mỗi pháp tuyến đó $x$ khác đúng một trong hai véc-tơ. Ở hai pháp tuyến còn lại, $y$ và $z$ cùng bit $+$, còn $x$ có một bit $+$ và một bit $-$. Do đó $6+10=14+2=16$.
:::

::: exercise Bài tập 06.30 (Số hàm tối ưu của phép ghép OR cho vân tay; MMDS Bài 3.8.5, §3.8.7, tr.122)
Dữ kiện: họ hàm ba ô của Bài tập 06.28, với $q_F=0{,}000064$ và $q_T=0{,}004096$ (Mệnh đề 06.42); $F_3$ là phép ghép OR bậc $n$ của các hàm chọn độc lập từ họ này; dùng giả thiết độc lập thêm của Ví dụ 06.18.

Tìm $n$ để tổng của xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón dưới $F_3$ nhỏ nhất.
:::

::: hint
Viết tổng thành một hàm $g(n)$ rồi xét dấu của $g(n+1)-g(n)$.
:::

::: solution
Theo phép ghép ít nhất một (Mệnh đề 06.26) và giả thiết độc lập thêm,

$$
g(n)=1-(1-q_F)^n+(1-q_T)^n.
$$

Hiệu hai giá trị liên tiếp là $g(n+1)-g(n)=q_F(1-q_F)^n-q_T(1-q_T)^n$, nên

$$
g(n+1)\ge g(n)\iff\Bigl(\frac{1-q_F}{1-q_T}\Bigr)^n\ge\frac{q_T}{q_F}=64\iff n\ge\frac{\ln64}{\ln\frac{1-q_F}{1-q_T}}\approx1029{,}32.
$$

Vì $(1-q_F)/(1-q_T)>1$, vế trái tăng theo $n$: $g(n+1)<g(n)$ khi $n\le1029$ và $g(n+1)\ge g(n)$ khi $n\ge1030$. Giá trị nhỏ nhất đạt tại $n=1030$, với $g(1030)\approx0{,}07838439$, gồm xác suất nhận cặp khác ngón $\approx0{,}063796$ và xác suất bỏ sót $\approx0{,}014588$.

**Kiểm tra lại.** $g(1029)\approx0{,}07838447$, $g(1030)\approx0{,}07838439$ và $g(1031)\approx0{,}07838456$. Cấu trúc OR 1024 của Ví dụ 06.18 cho $g(1024)\approx0{,}07838853$, lớn hơn $g(1030)$ chưa tới $5\cdot10^{-6}$.
:::
