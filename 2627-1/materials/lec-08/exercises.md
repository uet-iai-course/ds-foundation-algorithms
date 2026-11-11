# Bài tập Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc

Các bài tập củng cố 08.6–08.14 dưới đây đi kèm [ghi chú Bài 08](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html), nơi Bài tập 08.1–08.5 đứng ngay sau các mục, mỗi bài kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 08.k là của ghi chú đó, và ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bốn bài 08.10–08.13 là các bài 4.3.1–4.3.3 và 4.2.1 của MMDS và là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 08](lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html). Bài tập xếp theo ba mức: nhận biết (08.6–08.9), tính toán hoặc chứng minh (08.10–08.12) và vận dụng (08.13, 08.14).

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả thuật toán dòng một lượt và mẫu theo khóa cho một thống kê theo nhóm (Mục 1, Mục 2) | 08.1, 08.2, 08.3 | 08.6, 08.13 |
| 2. Chứng minh xác suất có mặt $s/r$ của lấy mẫu hồ chứa (Mục 3) | 08.4 | 08.7, 08.14 |
| 3. Xây và truy vấn Bloom filter, chứng minh không có âm giả, tính xác suất dương giả và số hàm băm tối ưu (Mục 4) | 08.5 | 08.8–08.12 |

## Mức nhận biết

::: exercise Bài tập 08.6 (Ngưỡng 5% và mẫu từng bộ)
Hàm $h$ nhận giá trị trong $\{0,\ldots,99\}$. Muốn giữ $5\%$ người dùng của dòng truy vấn tìm kiếm, điều kiện giữ bộ $t$ là gì? Vì sao không lấy $5\%$ từng bộ? Nêu kết quả đã dùng.
:::

::: hint
Đếm số giá trị được nhận; với mẫu từng bộ, dùng công thức tỷ lệ giữ $\eta$ ở Nhận xét 08.7.
:::

::: solution
Giữ $t$ khi $h(K(t))<5$, với $K(t)$ là người dùng: đúng 5 trong 100 giá trị, nên mỗi người được giữ với xác suất $5/100$ khi $h$ đều theo từng khóa (Mệnh đề 08.10(b)), và mọi bộ của một người nhận cùng quyết định (Mệnh đề 08.10(a)). Lấy từng bộ với xác suất $\eta=0{,}05$ cho tỷ số $\frac{d\eta}{u+(2-\eta)d}=\frac{0{,}05d}{u+1{,}95d}=\frac{d}{20u+39d}$ thay vì $\frac{d}{u+d}$ (Nhận xét 08.7, Mệnh đề 08.6). Với $u=d=1$, đó là $1/59$ thay vì $1/2$.
:::

::: exercise Bài tập 08.7 (Xác suất có mặt trong hồ chứa)
Hồ chứa có $s=50$ ô, dòng đã có $r=1\,000$ bộ. Bộ thứ 7 và bộ thứ 999 còn trong hồ với xác suất bao nhiêu? Cần giả thiết gì?
:::

::: hint
Kiểm $r\ge s$ rồi dùng Định lý 08.17.
:::

::: solution
Vì $r=1\,000\ge s=50$, Định lý 08.17 cho $\Pr[x_7\in W]=\Pr[x_{999}\in W]=s/r=50/1\,000=0{,}05$. Cần mỗi số $j$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước. Xác suất $s/r$ không phụ thuộc vị trí $i$: bộ đến rất sớm và bộ vừa đến có cùng xác suất.
:::

::: exercise Bài tập 08.8 (Âm giả sau khi thêm khóa)
Bloom filter có thể trả "chắc chắn không thuộc" cho một khóa đã được thêm vào $S$ không? Nêu giả thiết của câu trả lời.
:::

::: hint
Xem bốn điều kiện của Định lý 08.25 và điều gì xảy ra khi bỏ điều kiện 1.
:::

::: solution
Không, khi bốn điều kiện của Định lý 08.25 được giữ: không bit nào bị xóa, truy vấn dùng đúng hàm băm và mảng đã xây, hàm băm tất định, mọi phép ghi đã xong. Nếu gỡ một khóa bằng cách đặt bit về 0, khóa khác dùng chung bit có thể bị loại: trong mảng 11 bit của Ví dụ 08.11, gỡ 585 làm 159 nhận "chắc chắn không thuộc".
:::

::: exercise Bài tập 08.9 (Gấp đôi số bit)
Giữ $m$, gấp đôi $n$. Số hàm băm tối ưu $k^*$ và giá trị $p(k^*)$ thay đổi thế nào? Tính cho $n/m$ từ 8 lên 16.
:::

::: hint
Dùng $k^*=(n/m)\ln2$ và $p(k^*)=2^{-k^*}$ của Định lý 08.28.
:::

::: solution
$k^*=(n/m)\ln2$ gấp đôi, và $p(k^*)=2^{-k^*}$ nên giá trị mới là bình phương giá trị cũ (Định lý 08.28). Với $n/m=8$: $k^*\approx5{,}545$, $p(k^*)\approx0{,}0214$. Với $n/m=16$: $k^*\approx11{,}09$, $p(k^*)\approx0{,}0214^2\approx4{,}6\cdot10^{-4}$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 08.10 (Ba và bốn hàm băm; Bài 4.3.1, MMDS §4.3.4, tr.141)
Với tình huống lọc thư, $n=8\cdot10^9$ bit và tập $S$ gồm $m=10^9$ khóa, tính xác suất dương giả khi dùng ba hàm băm, và khi dùng bốn hàm băm.
:::

::: hint
Dùng dạng mũ $p(k)=(1-e^{-km/n})^k$ với $km/n=k/8$.
:::

::: solution
$p(3)=(1-e^{-3/8})^3\approx0{,}030579$ và $p(4)=(1-e^{-1/2})^4\approx0{,}023969$. Bốn hàm băm tốt hơn ba vì $4<k^*\approx5{,}545$, trên đoạn $p$ còn giảm (Định lý 08.28). Theo Mệnh đề 08.27, đây là dạng mũ, một cận dưới của $p_{FP}$ dưới mô hình băm đều, độc lập; với $n=8\cdot10^9$, các mức xấp xỉ trùng nhau tới nhiều chữ số. Không suy ra rằng càng nhiều hàm băm càng tốt: với $k>k^*$, $p$ tăng.

**Kiểm tra lại.** Hai số nằm giữa $p(2)\approx0{,}0489$ và $p(6)\approx0{,}0216$ của Ví dụ 08.14 và 08.16, đúng chiều giảm của $p$ trên $(0,k^*]$.
:::

::: exercise Bài tập 08.11 (Chia mảng bit; Bài 4.3.2, MMDS §4.3.4, tr.141)
Có $n$ bit bộ nhớ và tập $S$ gồm $m$ khóa. Thay vì $k$ hàm băm vào một mảng, chia $n$ bit thành $k$ mảng và băm một lần vào mỗi mảng. Theo $n$, $m$, $k$, xác suất dương giả là bao nhiêu? So với $k$ hàm băm vào một mảng chung. Quy ước của học phần, sách không nêu: $k$ chia hết $n$; các hàm băm đều và độc lập.

![Trái: một mảng 64 bit, chỉ số 0 đến 63, khóa v được băm bằng bốn hàm h1 đến h4 vào bất kỳ vị trí nào của cả mảng, ở đây h2 và h3 rơi vào cùng một bit. Phải: 64 bit chia thành bốn mảng, mỗi mảng 16 bit; h1 chỉ băm vào mảng 1, h2 vào mảng 2, h3 vào mảng 3, h4 vào mảng 4; bit bị trúng có nền đậm.](img/lec-08/chia-mang-bit.svg)

Hình dựng bài toán với $n=64$, $k=4$: bên trái, bốn hàm băm của mảng chung có thể trúng cùng một bit; bên phải, mỗi hàm chỉ băm vào mảng con riêng của nó, nên bốn vị trí luôn khác nhau.
:::

::: hint
Một mảng con có $n/k$ bit và nhận $m$ phi tiêu, mỗi khóa của $S$ một phi tiêu. Để so sánh, dùng bất đẳng thức Bernoulli ở phần tiên quyết.
:::

::: solution
**Mảng chia.** Một bit cố định của một mảng con bằng 0 khi không khóa nào của $S$ băm vào nó; mỗi khóa trượt bit đó với xác suất $1-k/n$, nên xác suất là $(1-k/n)^m$. Với khóa $y\notin S$ cố định, $h_i(y)$ rơi đều trong mảng con thứ $i$, độc lập với các phi tiêu của $S$, nên bit đó bằng 1 với xác suất $1-(1-k/n)^m$. Các mảng con dùng các hàm băm khác nhau, chọn độc lập, nên $k$ phép kiểm độc lập, và tích

$$
p_{\text{chia}}=\bigl[1-(1-k/n)^m\bigr]^k,
$$

đúng chính xác dưới mô hình này.

**Mảng chung.** Ở mảng chung, $k$ phép kiểm cùng đọc một mảng có số bit 1 ngẫu nhiên $X$, nên theo Mệnh đề 08.27 giá trị chính xác là $p_{FP}=\mathbb E[(X/n)^k]$, còn $q^k=[1-(1-1/n)^{km}]^k$ chỉ là xấp xỉ, một cận dưới.

**So sánh.** Theo bất đẳng thức Bernoulli, $(1-1/n)^k\ge1-k/n$, nên $(1-1/n)^{km}\ge(1-k/n)^m$. Mảng chia có ít bit 0 hơn theo kỳ vọng, nên $p_{\text{chia}}\ge q^k$. Khi $n$ lớn, cả hai về $(1-e^{-km/n})^k$.

**Ví dụ số.** Với $n=64$, $m=8$, $k=4$: $p_{\text{chia}}\approx0{,}026450$; $q^k\approx0{,}024556$; giá trị chính xác của mảng chung $\mathbb E[(X/64)^4]\approx0{,}025354$, tính từ phân phối số bit 1 sau 32 phi tiêu. Với $n=8\cdot10^9$, $m=10^9$, $k=4$, hai công thức trùng tới chín chữ số có nghĩa, $0{,}023968650\ldots$

**Kiểm tra lại.** Chiều $p_{\text{chia}}\ge q^k$ được chứng minh; trong ví dụ, mảng chia còn lớn hơn giá trị chính xác của mảng chung, nhưng chương không chứng minh chiều này cho mọi $n$, $m$, $k$.
:::

::: exercise Bài tập 08.12 (Số hàm băm tối ưu; Bài 4.3.3, MMDS §4.3.4, tr.142)
Theo $n$ là số bit và $m$ là số khóa của $S$, số hàm băm nào làm nhỏ nhất xác suất dương giả? Dùng dạng mũ $p(k)=(1-e^{-km/n})^k$ với $k$ thực, rồi chọn $k$ nguyên.
:::

::: hint
Đặt $\rho=m/n$, $z=k\rho$, $\theta=e^{-z}$ và xét $\lambda(k)=\ln p(k)$. Tìm điểm làm đạo hàm bằng 0, rồi xét dấu đạo hàm ở hai phía.
:::

::: solution
Đây là Định lý 08.28 và Hệ quả 08.29. Với các biến của gợi ý, $\lambda(k)=k\ln(1-e^{-k\rho})$, và theo quy tắc tích

$$
\lambda'(k)=\ln(1-e^{-k\rho})+\frac{k\rho\,e^{-k\rho}}{1-e^{-k\rho}}=\ln(1-\theta)+\frac{z\theta}{1-\theta}=\frac{\phi(\theta)}{1-\theta},
$$

với $\phi(\theta)=(1-\theta)\ln(1-\theta)-\theta\ln\theta$; bước cuối thay $z=-\ln\theta$. Vì $1-\theta>0$, dấu của $\lambda'(k)$ là dấu của $\phi(\theta)$. Ta có $\phi(1/2)=0$, nên $\theta=1/2$, tức $k^*=(n/m)\ln2$, là một điểm dừng; điểm dừng chưa đủ để kết luận cực tiểu toàn cục, nên cần xét dấu $\phi$ ở hai phía. Hàm $\phi$ dương trên $(0,1/2)$, nhờ tính lõm chặt và $\phi(0^+)=\phi(1/2)=0$, và âm trên $(1/2,1)$, nhờ $\phi(1-\theta)=-\phi(\theta)$. Vì $\theta>1/2$ khi và chỉ khi $k<(n/m)\ln2$, $p$ giảm rồi tăng và nhỏ nhất tại $k^*=(n/m)\ln2$, với $p(k^*)=2^{-k^*}$. Với $k$ nguyên, so $p$ tại $\lfloor k^*\rfloor$ và $\lceil k^*\rceil$, và lấy $k=1$ nếu $k^*<1$. Các bước đầy đủ nằm trong chứng minh Định lý 08.28.

**Kiểm tra lại.** Với $n/m=8$: $k^*\approx5{,}545$; $p(5)\approx0{,}021679>p(6)\approx0{,}021577$, nên chọn $k=6$.
:::

## Mức vận dụng

::: exercise Bài tập 08.13 (Chọn khóa lấy mẫu; Bài 4.2.1, MMDS §4.2.5, tr.138)
Dòng có lược đồ `Grades(university, courseID, studentID, grade)`. Mã trường là duy nhất; mã học phần và mã sinh viên chỉ duy nhất trong một trường.

![Hai khối trường U1 và trường U2; mỗi khối có hộp học phần CS101 và hộp sinh viên 123; đường nối hai hộp CS101 ghi cùng mã CS101, hai học phần khác nhau; đường nối hai hộp 123 ghi cùng mã 123, hai sinh viên khác nhau.](img/lec-08/grades-hai-truong.svg)

Hình minh họa giả thiết của đề: ở hai trường U1 và U2, cùng mã học phần CS101 là hai học phần khác nhau, và cùng mã sinh viên 123 là hai sinh viên khác nhau. U1, U2 là tên đặt chỗ, CS101 lấy từ đề MMDS, mã 123 do học phần đặt.

Với một mẫu $1/20$ của dữ liệu, chọn thuộc tính khóa để ước lượng:

(a) với mỗi trường, số sinh viên trung bình của một học phần;

(b) tỷ lệ sinh viên có điểm trung bình từ 3,5;

(c) tỷ lệ học phần có ít nhất nửa số sinh viên đạt "A".
:::

::: hint
Với mỗi câu, hỏi thống kê gộp các bộ theo đơn vị nào, rồi chọn thuộc tính nhận diện duy nhất đơn vị đó (quy trình ở Mục 2.3).
:::

::: solution
Với mỗi câu, xác định đơn vị mà thống kê gộp, rồi lấy khóa nhận diện đơn vị đó.

(a) Đơn vị là học phần, khóa `(university, courseID)`. Mọi bộ của một học phần cùng vào mẫu hoặc cùng bị bỏ (Mệnh đề 08.10(a)), nên số sinh viên của học phần được giữ đếm đúng, và mỗi trường còn, theo kỳ vọng, khoảng $1/20$ số học phần; trường có rất ít học phần có thể không còn học phần nào, và ước lượng cho trường đó không xác định. Đại lượng cần ước lượng là trung bình trên các học phần, không phải một tỷ lệ theo bản ghi điểm; mẫu từng bản ghi chỉ giữ khoảng $1/20$ số sinh viên của mỗi học phần, nên đếm sinh viên trên mẫu đó cho số quá nhỏ. Khóa chỉ gồm `university` sẽ bỏ hẳn khoảng $19/20$ số trường, trong khi câu hỏi cần mọi trường.

(b) Đơn vị là sinh viên, khóa `(university, studentID)`: điểm trung bình của một sinh viên cần mọi bộ của sinh viên đó.

(c) Đơn vị là học phần, khóa `(university, courseID)`: tỷ lệ đạt "A" của một học phần cần mọi bộ của học phần.

Cả ba khóa phải có `university`, vì mã học phần và mã sinh viên chỉ duy nhất trong một trường; thiếu nó, hai học phần cùng mã ở hai trường bị gộp thành một đơn vị (bước 3 của quy trình ở Mục 2.3). Chẳng hạn, nếu khóa chỉ là `studentID`, hai sinh viên khác trường cùng mã 123 bị gộp thành một người; mã 123 là ví dụ của học phần.
:::

::: exercise Bài tập 08.14 (Hồ chứa cho từng khóa)
MMDS (hộp "A General Stream-Sampling Problem", tr.150) đề xuất kết hợp hai cấu trúc: lấy mẫu theo khóa với tỷ lệ $a/b$, và với mỗi khóa được chọn, giữ các bộ của khóa đó trong một hồ chứa $s$ ô. Xét một khóa $K$ được chọn, đã có $r_K\ge s$ bộ.

(a) Một bộ cố định của $K$ nằm trong mẫu với xác suất bao nhiêu, theo các lần rút của hồ chứa của $K$?

(b) Mẫu có tối đa bao nhiêu bộ, nếu có $N_K$ khóa được chọn?

(c) Tỷ lệ truy vấn lặp của một người dùng $K$ có còn tính đúng trên mẫu không?
:::

::: hint
Áp Định lý 08.17 cho dòng con gồm các bộ của $K$; với (c), xem Nhận xét 08.20.
:::

::: solution
(a) Các bộ của $K$ tạo một dòng con, và hồ chứa của $K$ chạy Thuật toán 08.16 trên dòng con đó. Theo Định lý 08.17, với các số rút đều và độc lập với các lần rút trước, mỗi bộ của $K$ có mặt với xác suất $s/r_K$.

(b) Mỗi khóa được chọn giữ tối đa $s$ bộ, nên mẫu có tối đa $sN_K$ bộ, cộng một bộ đếm $r_K$ cho mỗi khóa. Một khóa nhiều bộ, như khóa $10^6$ bộ của Ví dụ 08.6, chỉ chiếm $s$ ô.

(c) Chỉ khi $r_K\le s$. Khi $r_K>s$, hồ chứa của $K$ chọn vị trí riêng lẻ, nên hai bộ của cùng một truy vấn có thể bị tách, và tỷ lệ lặp tính trên mẫu bị lệch xuống (Nhận xét 08.20). Cách kết hợp này đổi tính đúng của thống kê theo người dùng nặng lấy giới hạn bộ nhớ.
:::
