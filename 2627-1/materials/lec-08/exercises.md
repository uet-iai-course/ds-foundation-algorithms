# Bài tập Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc

Các bài tập củng cố 08.6–08.13 dưới đây lấy từ bài tập của hai giáo trình *Mining of Massive Datasets* của Leskovec, Rajaraman và Ullman (viết tắt MMDS) và *Foundations of Data Science* của Blum, Hopcroft và Kannan (viết tắt BHK), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 08.k là của [ghi chú Bài 08](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html), nơi Bài tập 08.1–08.5 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bốn bài 08.10–08.13 (MMDS Bài 4.3.1–4.3.3 và 4.2.1) là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 08](lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả thuật toán dòng một lượt và mẫu theo khóa cho một thống kê theo nhóm (Mục 1, Mục 2) | 08.1, 08.2, 08.3 | 08.13 |
| 2. Chứng minh xác suất có mặt $s/r$ của lấy mẫu hồ chứa (Mục 3) | 08.4 | 08.6, 08.7, 08.8, 08.9 |
| 3. Xây và truy vấn Bloom filter, chứng minh không có âm giả, tính xác suất dương giả và số hàm băm tối ưu (Mục 4) | 08.5 | 08.10, 08.11, 08.12 |

## Mức nhận biết

::: exercise Bài tập 08.6 (Chọn hàng qua một phần tử; Bài 6.3, BHK §6.6, tr.204)
Mỗi phần tử ở hàng $i$, cột $j$ của một ma trận được chọn với xác suất $\pi_{ij}\ge0$, với $\sum_{i,j}\pi_{ij}=1$. Tính xác suất cách sau chọn hàng $i$, rồi so với $\sum_j\pi_{ij}$: chọn một phần tử theo xác suất của nó, rồi lấy hàng chứa phần tử đó.
:::

::: hint
Viết biến cố "chọn hàng $i$" thành hợp của các biến cố "chọn phần tử ở hàng $i$, cột $j$".
:::

::: solution
Mỗi lần chọn cho đúng một phần tử, nên các biến cố "chọn phần tử ở hàng $i$, cột $j$" với $j$ khác nhau rời nhau, và hàng $i$ được lấy khi và chỉ khi một trong các biến cố đó xảy ra. Do đó
$$\Pr[\text{chọn hàng }i]=\sum_j\pi_{ij},$$
đúng bằng xác suất cần có.

**Kiểm tra lại.** Với ma trận $\begin{pmatrix}0{,}1&0{,}2\\0{,}3&0{,}4\end{pmatrix}$, hàng 1 được chọn với xác suất $0{,}1+0{,}2=0{,}3$, hàng 2 với xác suất $0{,}3+0{,}4=0{,}7$, tổng bằng 1.
:::

::: exercise Bài tập 08.7 (Chọn một từ theo số lần xuất hiện; Bài 6.2, BHK §6.6, tr.204)
Một cuốn sách rất lớn được đọc một lượt, từ đầu đến cuối. Xây dựng cách chọn một từ sao cho xác suất chọn mỗi từ tỷ lệ với số lần từ đó xuất hiện trong sách, và nêu bộ nhớ cần dùng.
:::

::: hint
Coi mỗi lần xuất hiện của một từ là một phần tử của dòng.
:::

::: solution
Coi sách là dòng $x_1,\ldots,x_r$, mỗi phần tử là một lần xuất hiện của một từ, và chạy Thuật toán 08.16 với $s=1$. Theo Định lý 08.17 với $s=1$, sau $r$ phần tử, mỗi vị trí $i\le r$ là phần tử trong hồ với xác suất $1/r$. Nếu từ $w$ xuất hiện $f_w$ lần thì $w$ được chọn khi hồ chứa một trong $f_w$ vị trí của nó; các biến cố này rời nhau, nên $w$ được chọn với xác suất $f_w/r$, tỷ lệ với $f_w$. Bộ nhớ gồm một từ trong hồ và bộ đếm $r$, tức $\lceil\log_2(r+1)\rceil$ bit cho bộ đếm.

**Kiểm tra lại.** Với sách "a b a", $r=3$. Phần tử ở vị trí 1 còn trong hồ khi không bị thay ở bước 2 và bước 3, với xác suất $\frac12\cdot\frac23=\frac13$; vị trí 3 vào hồ với xác suất $\frac13$. Vậy $\Pr[\text{chọn a}]=\frac13+\frac13=\frac23=f_{\mathrm a}/r$ và $\Pr[\text{chọn b}]=\frac13$.
:::

::: exercise Bài tập 08.12 (Số hàm băm tối ưu; Bài 4.3.3, MMDS §4.3.4, tr.142)
Cho $n$ là số bit và $m$ là số khóa của $S$; xét dạng mũ $p(k)=(1-e^{-km/n})^k$.

- (a) Với $k$ thực dương, xác định số hàm băm làm $p$ nhỏ nhất theo $n$ và $m$.
- (b) Xác định số hàm băm nguyên tốt nhất.
:::

::: hint
Đặt $\rho=m/n$, $z=k\rho$, $\theta=e^{-z}$ và xét $\lambda(k)=\ln p(k)$. Tìm điểm làm đạo hàm bằng 0, rồi xét dấu đạo hàm ở hai phía.
:::

::: solution
**Câu (a).** Với các biến của gợi ý, dấu của $\lambda'(k)$ trùng dấu của $\phi(\theta)=(1-\theta)\ln(1-\theta)-\theta\ln\theta$, và $\phi$ dương trên $(0,1/2)$, âm trên $(1/2,1)$ (chứng minh Định lý 08.28, Bước 2–4). Vì $\theta>1/2$ khi và chỉ khi $k<(n/m)\ln2$, theo Định lý 08.28, $p$ giảm chặt trên $(0,k^*]$, tăng chặt trên $[k^*,\infty)$ và nhỏ nhất tại $k^*=(n/m)\ln2$, với $p(k^*)=2^{-k^*}$.

**Câu (b).** Theo Hệ quả 08.29, khi $k^*\ge1$, số nguyên tốt nhất là giá trị cho $p$ nhỏ hơn trong $\lfloor k^*\rfloor$ và $\lceil k^*\rceil$; khi $k^*<1$, đó là $k=1$.

**Kiểm tra lại.** Với $n/m=10$: $k^*=10\ln2\approx6{,}931$; $p(6)\approx0{,}008436>p(7)\approx0{,}008194$, nên chọn $k=7$; cả hai không nhỏ hơn $2^{-k^*}\approx0{,}008193$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 08.8 (Chọn vị trí theo bình phương giá trị; Bài 6.1, câu 2, BHK §6.6, tr.204)
Cho dòng $x_1,x_2,\ldots$, mỗi phần tử là một số nguyên trong $\{1,\ldots,Q\}$ (BHK viết $a_1,\ldots,a_n$ và $m$), với độ dài chưa biết trước. Xây dựng thuật toán một lượt sao cho sau $r$ phần tử, vị trí $i\le r$ được chọn với xác suất tỷ lệ với $x_i^2$. Chứng minh tính đúng và nêu bộ nhớ.
:::

::: hint
Làm như hồ chứa với $s=1$ (Thuật toán 08.16), nhưng xác suất thay ở bước $r$ phụ thuộc $x_r^2$ và tổng các bình phương đã đọc.
:::

::: solution
**Thuật toán.** Giữ $Y_r=\sum_{i\le r}x_i^2$ và một vị trí $I$ cùng giá trị $x_I$. Khi $x_r$ đến, đặt $Y_r\gets Y_{r-1}+x_r^2$, rút một số nguyên đều trong $\{1,\ldots,Y_r\}$, và đặt $I\gets r$ khi số rút không vượt $x_r^2$, tức với xác suất $x_r^2/Y_r$. Các số rút độc lập với nhau. Ở bước 1, $x_1^2/Y_1=1$, nên $I=1$.

**Tính đúng.** Vị trí $i$ là $I$ sau bước $r\ge i$ khi nó được nhận ở bước $i$ và không bị thay ở các bước $i+1,\ldots,r$. Ở bước $\ell>i$, xác suất không thay là $1-x_\ell^2/Y_\ell=Y_{\ell-1}/Y_\ell$. Do các số rút độc lập,
$$\Pr[I=i]=\frac{x_i^2}{Y_i}\prod_{\ell=i+1}^{r}\frac{Y_{\ell-1}}{Y_\ell}=\frac{x_i^2}{Y_i}\cdot\frac{Y_i}{Y_r}=\frac{x_i^2}{Y_r}.$$

**Bộ nhớ.** Thuật toán giữ $Y_r\le rQ^2$, vị trí $I\le r$ và giá trị $x_I\le Q$, tức $O(\log r+\log Q)$ bit.

**Kiểm tra lại.** Với dòng $1,2,2$: $Y_1,Y_2,Y_3=1,5,9$. Vị trí 1: $1\cdot\frac15\cdot\frac59=\frac19$; vị trí 2: $\frac45\cdot\frac59=\frac49$; vị trí 3: $\frac49$. Ba xác suất bằng $x_i^2/9$ và có tổng 1.
:::

::: exercise Bài tập 08.10 (Ba và bốn hàm băm; Bài 4.3.1, MMDS §4.3.4, tr.141)
Với tình huống lọc thư, $n=8\cdot10^9$ bit và tập $S$ gồm $m=10^9$ khóa, tính xác suất dương giả:

- (a) khi dùng ba hàm băm;
- (b) khi dùng bốn hàm băm.
:::

::: hint
Dùng dạng mũ $p(k)=(1-e^{-km/n})^k$ với $km/n=k/8$.
:::

::: solution
**Câu (a).** $p(3)=(1-e^{-3/8})^3\approx0{,}030579$.

**Câu (b).** $p(4)=(1-e^{-1/2})^4\approx0{,}023969$. Bốn hàm băm tốt hơn ba vì $4<k^*\approx5{,}545$, trên đoạn $p$ còn giảm (Định lý 08.28); với $k>k^*$, $p$ tăng. Theo Mệnh đề 08.27, hai số là dạng mũ, một cận dưới của $p_{FP}$ dưới mô hình băm đều, độc lập. Với $n=8\cdot10^9$, $q^k$ và $p(k)$ trùng nhau tới chín chữ số có nghĩa, ở cả $k=3$ và $k=4$.

**Kiểm tra lại.** Hai số nằm giữa $p(2)\approx0{,}0489$ và $p(5)\approx0{,}0217$ của Ví dụ 08.14 và 08.16, đúng chiều giảm của $p$ trên $(0,k^*]$.
:::

::: exercise Bài tập 08.11 (Chia mảng bit; Bài 4.3.2, MMDS §4.3.4, tr.141)
Có $n$ bit bộ nhớ và tập $S$ gồm $m$ khóa. Thay vì $k$ hàm băm vào một mảng, chia $n$ bit thành $k$ mảng và băm một lần vào mỗi mảng. Giả sử $k$ chia hết $n$ và các hàm băm đều, độc lập.

- (a) Tính xác suất dương giả theo $n$, $m$, $k$.
- (b) So sánh với $k$ hàm băm vào một mảng chung.

![Trái: một mảng 64 bit, chỉ số 0 đến 63, khóa v được băm bằng bốn hàm h1 đến h4 vào bất kỳ vị trí nào của cả mảng, ở đây h2 và h3 rơi vào cùng một bit. Phải: 64 bit chia thành bốn mảng, mỗi mảng 16 bit; h1 chỉ băm vào mảng 1, h2 vào mảng 2, h3 vào mảng 3, h4 vào mảng 4; bit bị trúng có nền đậm.](img/lec-08/chia-mang-bit.svg)

Hình dựng bài toán với $n=64$, $k=4$: bên trái, bốn hàm băm của mảng chung có thể trúng cùng một bit; bên phải, mỗi hàm chỉ băm vào mảng con riêng của nó, nên bốn vị trí luôn khác nhau.
:::

::: hint
Một mảng con có $n/k$ bit và nhận $m$ phi tiêu, mỗi khóa của $S$ một phi tiêu. Để so sánh, dùng bất đẳng thức Bernoulli ở phần tiên quyết.
:::

::: solution
**Câu (a).** Một bit cố định của một mảng con bằng 0 khi không khóa nào của $S$ băm vào nó; mỗi khóa trượt bit đó với xác suất $1-k/n$, nên xác suất là $(1-k/n)^m$. Với khóa $y\notin S$ cố định, $h_i(y)$ rơi đều trong mảng con thứ $i$, độc lập với các phi tiêu của $S$, nên bit đó bằng 1 với xác suất $1-(1-k/n)^m$. Các mảng con dùng các hàm băm khác nhau, chọn độc lập, nên $k$ phép kiểm độc lập, và
$$p_{\text{chia}}=\bigl[1-(1-k/n)^m\bigr]^k$$
đúng chính xác dưới mô hình này.

**Câu (b).** Ở mảng chung, $k$ phép kiểm cùng đọc một mảng có số bit 1 ngẫu nhiên $X$, nên theo Mệnh đề 08.27 giá trị chính xác là $p_{FP}=\mathbb E[(X/n)^k]$, còn $q^k=[1-(1-1/n)^{km}]^k$ là một cận dưới. Theo bất đẳng thức Bernoulli, $(1-1/n)^k\ge1-k/n$, nên $(1-1/n)^{km}\ge(1-k/n)^m$: mảng chia có ít bit 0 hơn theo kỳ vọng, và $p_{\text{chia}}\ge q^k$. Khi $n$ lớn và $m/n$ cố định, cả hai cách cho cùng $(1-e^{-km/n})^k$; trong ví dụ dưới đây, mảng chia cho xác suất dương giả lớn hơn cả giá trị chính xác của mảng chung.

**Kiểm tra lại.** Với $n=64$, $m=8$, $k=4$: $q^k\approx0{,}024556<\mathbb E[(X/64)^4]\approx0{,}025354<p_{\text{chia}}\approx0{,}026450$ (giá trị giữa tính bằng máy, từ phân phối số bit 1 sau 32 phi tiêu). Với $n=8\cdot10^9$, $m=10^9$, $k=4$, hai công thức trùng tới chín chữ số có nghĩa, $0{,}023968650\ldots$
:::

::: exercise Bài tập 08.9 (Nhiều mẫu độc lập theo trọng số; Bài 6.4, BHK §6.6, tr.204)
Cho dòng $x_1,x_2,\ldots$ các số nguyên dương, với độ dài chưa biết trước. Xây dựng thuật toán một lượt rút $L$ chỉ số độc lập $I_1,\ldots,I_L$, mỗi chỉ số bằng $i\le r$ với xác suất tỷ lệ với $x_i$; một chỉ số có thể được rút nhiều lần. Nêu bộ nhớ của thuật toán.
:::

::: hint
Làm như Bài tập 08.8 với trọng số $x_i$ thay cho $x_i^2$, rồi chạy $L$ bản sao với các số rút độc lập.
:::

::: solution
**Thuật toán.** Giữ tổng chạy $Y_r=\sum_{i\le r}x_i$, dùng chung cho mọi bản sao, và $L$ chỉ số $I_1,\ldots,I_L$. Khi $x_r$ đến, đặt $Y_r\gets Y_{r-1}+x_r$; với mỗi bản sao, rút một số nguyên đều trong $\{1,\ldots,Y_r\}$, độc lập với mọi lần rút khác, và đặt chỉ số của bản sao đó bằng $r$ khi số rút không vượt $x_r$.

**Tính đúng.** Mỗi bản sao là thuật toán của Bài tập 08.8 với trọng số $x_i$, nên cùng phép tính tích lồng nhau cho $\Pr[I_\ell=i]=x_i/Y_r$ với mọi $\ell$. Các bản sao dùng các số rút độc lập, nên $I_1,\ldots,I_L$ độc lập. Đây là rút có hoàn lại: hai bản sao có thể giữ cùng một chỉ số, khác hồ chứa cỡ $s$, nơi $s$ vị trí luôn khác nhau (Mệnh đề 08.18).

**Bộ nhớ.** $L$ chỉ số, mỗi chỉ số $\lceil\log_2(r+1)\rceil$ bit, cộng $\lceil\log_2(Y_r+1)\rceil$ bit cho tổng $Y_r$; mỗi phần tử tốn $L$ lần rút.

**Kiểm tra lại.** Với dòng $1,3$ và $L=2$: $Y_2=4$, mỗi bản sao chọn vị trí 2 với xác suất $3/4$, nên cả hai cùng chọn vị trí 2 với xác suất $(3/4)^2=9/16$. Hồ chứa $s=2$ trên cùng dòng luôn giữ cả hai vị trí.
:::

## Mức vận dụng

::: exercise Bài tập 08.13 (Chọn khóa lấy mẫu; Bài 4.2.1, MMDS §4.2.5, tr.138)
Dòng có lược đồ `Grades(university, courseID, studentID, grade)`. Mã trường là duy nhất; mã học phần và mã sinh viên chỉ duy nhất trong một trường.

![Hai khối trường U1 và trường U2; mỗi khối có hộp học phần CS101 và hộp sinh viên 123; đường nối hai hộp CS101 ghi cùng mã CS101, hai học phần khác nhau; đường nối hai hộp 123 ghi cùng mã 123, hai sinh viên khác nhau.](img/lec-08/grades-hai-truong.svg)

Hình minh họa giả thiết của đề: ở hai trường U1 và U2, cùng mã học phần CS101 là hai học phần khác nhau, và cùng mã sinh viên 123 là hai sinh viên khác nhau.

Với một mẫu $1/20$ của dữ liệu, chọn thuộc tính khóa để ước lượng:

- (a) với mỗi trường, số sinh viên trung bình của một học phần;
- (b) tỷ lệ sinh viên có điểm trung bình từ 3,5;
- (c) tỷ lệ học phần có ít nhất nửa số sinh viên đạt "A".
:::

::: hint
Với mỗi câu, xác định thống kê gộp các bộ theo đơn vị nào, rồi chọn thuộc tính nhận diện duy nhất đơn vị đó (quy trình ở Mục 2.3).
:::

::: solution
**Câu (a).** Đơn vị là học phần, khóa `(university, courseID)`. Mọi bộ của một học phần cùng vào mẫu hoặc cùng bị bỏ (Mệnh đề 08.10(a)), nên số sinh viên của học phần được giữ đếm đúng. Mẫu từng bản ghi chỉ giữ khoảng $1/20$ số sinh viên của mỗi học phần, nên số đếm nhỏ đi khoảng 20 lần.

**Câu (b).** Đơn vị là sinh viên, khóa `(university, studentID)`: điểm trung bình của một sinh viên cần mọi bộ của sinh viên đó.

**Câu (c).** Đơn vị là học phần, khóa `(university, courseID)`: tỷ lệ đạt "A" của một học phần cần mọi bộ của học phần.

Cả ba khóa phải có `university`, vì mã học phần và mã sinh viên chỉ duy nhất trong một trường; thiếu nó, hai học phần cùng mã ở hai trường bị gộp thành một đơn vị (bước 3 của quy trình ở Mục 2.3).

**Kiểm tra lại.** Với hình trên, khóa `(university, studentID)` cho hai sinh viên mã 123 hai khóa (U1, 123) và (U2, 123), còn khóa `studentID` gộp họ thành một khóa 123; mọi bộ của sinh viên (U1, 123) có cùng khóa (U1, 123), đúng bước 3 của quy trình.
:::
