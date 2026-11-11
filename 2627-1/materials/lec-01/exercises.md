# Bài tập Bài 01 — Bài toán dữ liệu lớn và mô hình thuật toán

Các bài tập củng cố 01.10–01.11 dưới đây lấy từ mục bài tập §1.2.4 của sách *Mining of Massive Datasets* (ấn bản 3) của Leskovec, Rajaraman và Ullman (viết tắt MMDS), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 01.k là của [ghi chú Bài 01](material-viewer.html?doc=materials/lec-01/lecture-note.md&deck=lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html), nơi Bài tập 01.1–01.9 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Hai bài 01.10 và 01.11 là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 01](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html).

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đầu vào, đầu ra, tài nguyên; số khối và lần truyền khối (Mục 1, Mục 2) | 01.1, 01.2, 01.3, 01.4 | — |
| 2. Đặc tả cặp gần trùng; tính đúng của xét mọi cặp (Mục 3.1–3.3) | 01.5, 01.6 | — |
| 3. Chi phí của xét mọi cặp; xác minh ứng viên (Mục 3.4–3.5) | 01.2, 01.7 | — |
| 4. Giới hạn, nhóm bài và kiến thức nền (Mục 4) | 01.8 | — |
| 5. Kỳ vọng số biến cố trùng, độc lập và tuyến tính, Markov, giới hạn kết luận (Mục 5) | 01.9 | 01.10, 01.11 |

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 01.10 (Thay đổi quy mô quan sát; MMDS, Bài 1.2.1, §1.2.4, tr.8)
Dùng mô hình lưu trú không phối hợp của Định nghĩa 01.18 với $P=10^9$ người, $T=1000$ ngày, $H=10^5$ khách sạn và $q=0{,}01$, trong đó Ví dụ 01.13 cho $\mathbb E[X]=249\,749{,}99975025$. Tính kỳ vọng số biến cố trùng nếu áp dụng **từng thay đổi riêng** dưới đây, các số khác giữ nguyên.

- (a) Số ngày quan sát tăng lên $2000$.
- (b) Số người được quan sát tăng lên $2\cdot10^9$, và vì vậy có $2\cdot10^5$ khách sạn.
- (c) Chỉ báo một cặp người khi họ ở cùng một khách sạn trong ba ngày khác nhau; khách sạn có thể khác nhau giữa các ngày, điều kiện trùng xét trong từng ngày.

Với mỗi câu, ghi số phép thử, xác suất của một phép thử, kỳ vọng, và điều Hệ quả 01.22 cho biết.
:::

::: hint
Khi điều kiện là trùng trong $\kappa$ ngày khác nhau, một phép thử là một cặp người cùng một bộ $\kappa$ ngày, và lập luận của Mệnh đề 01.20 cho kỳ vọng $\binom P2\binom T\kappa(q^2/H)^\kappa$. Dùng $\kappa=2$ cho Câu (a), (b) và $\kappa=3$ cho Câu (c).
:::

::: solution
**Câu (a).** Số phép thử $\binom{10^9}{2}\binom{2000}{2}=499\,999\,999\,500\,000\,000\cdot1\,999\,000$; xác suất mỗi phép thử vẫn là $p^2=10^{-18}$. Theo Mệnh đề 01.20,
$$
\begin{aligned}
\mathbb E[X_a]&=\binom{10^9}{2}\binom{2000}{2}10^{-18}\\
&=999\,499{,}9990005\\
&\approx999\,500 .
\end{aligned}
$$
So với Ví dụ 01.13, kỳ vọng nhân với $\binom{2000}{2}/\binom{1000}{2}=1\,999\,000/499\,500=3998/999\approx4{,}002$, lớn hơn 4 một chút vì $999\cdot4=3996<3998$. Xấp xỉ $\binom T2\approx T^2/2$ của MMDS cho khoảng $1\,000\,000$.

**Câu (b).** Xác suất trùng trong một ngày đổi thành $p=q^2/H=10^{-4}/(2\cdot10^5)=5\cdot10^{-10}$, nên $p^2=2{,}5\cdot10^{-19}$. Số cặp người là $\binom{2\cdot10^9}{2}$, số cặp ngày vẫn $\binom{1000}{2}=499\,500$. Theo Mệnh đề 01.20,
$$
\begin{aligned}
\mathbb E[X_b]&=\binom{2\cdot10^9}{2}\binom{1000}{2}\\
&\quad\cdot\left(5\cdot10^{-10}\right)^2\\
&=249\,749{,}999875125\\
&\approx249\,750 .
\end{aligned}
$$
Số cặp người tăng $\binom{2\cdot10^9}{2}/\binom{10^9}{2}=3\,999\,999\,998/999\,999\,999\approx4{,}000000002$ lần, lớn hơn 4 một chút, còn xác suất mỗi phép thử giảm đúng 4 lần, nên kỳ vọng tăng thêm khoảng $5\times10^{-10}$ lần giá trị cũ, gần như không đổi. Xấp xỉ của MMDS cho khoảng $250\,000$.

**Câu (c).** Một phép thử là một cặp người cùng một bộ ba ngày khác nhau; có $\binom{10^9}{2}\binom{1000}{3}$ phép thử, với $\binom{1000}{3}=166\,167\,000$. Theo độc lập giữa ngày, xác suất trùng trong cả ba ngày là $p^3=10^{-27}$. Tuyến tính của kỳ vọng cho
$$
\begin{aligned}
\mathbb E[X_c]&=\binom{10^9}{2}\binom{1000}{3}10^{-27}\\
&=0{,}0830834999169165\\
&\approx0{,}0831 .
\end{aligned}
$$
Xấp xỉ $\binom T3\approx T^3/6$ cho khoảng $0{,}0833$.

**Điều Hệ quả 01.22 cho biết.** Ở Câu (a) và (b), kỳ vọng lớn hơn 1 nên cận $\Pr(X\ge1)\le\mathbb E[X]$ không cho thông tin. Ở Câu (c), xác suất có ít nhất một biến cố trùng ba ngày trong mô hình không phối hợp không quá $0{,}0831$. Kết luận này nói về dữ liệu sinh theo mô hình; nó không xác định danh tính hay ý định của một cặp người cụ thể trong đầu ra.

**Kiểm tra lại.** Câu (a): $249\,749{,}99975025\cdot3998/999=999\,499{,}9990005$. Câu (c): $499\,999\,999\,500\,000\,000\cdot166\,167\,000\cdot10^{-27}=0{,}0830834999169165$.
:::

## Mức vận dụng

::: exercise Bài tập 01.11 (Trùng tập mặt hàng; MMDS, Bài 1.2.2, §1.2.4, tr.8)
Có thông tin mua sắm của $10^8$ người. Mỗi người đi siêu thị $100$ lần trong một năm và mỗi lần mua $10$ trong $1000$ mặt hàng mà siêu thị bán. Giả thuyết làm việc là một cặp khủng bố sẽ mua đúng cùng một tập $10$ mặt hàng vào một lần nào đó trong năm. Nếu tìm các cặp người đã mua cùng một tập mặt hàng, có thể kỳ vọng những người tìm được thực sự là khủng bố không?

Lập mô hình nền, xác định một phép thử, tính kỳ vọng số biến cố trùng, rồi trả lời và nêu giả thiết mà kết luận cần.
:::

::: hint
Trong mô hình nền, mỗi lần mua chọn đều một tập 10 phần tử trong 1000 mặt hàng, độc lập với các lần mua khác. Với hai người khác nhau, một phép thử chọn một lần mua của người thứ nhất và một lần mua của người thứ hai; hai lần đó không cần có cùng số thứ tự.
:::

::: solution
**Mô hình nền.** Theo cách của Định nghĩa 01.18: mỗi lần mua chọn đều một trong $\binom{1000}{10}$ tập 10 mặt hàng, các lần mua của mọi người độc lập. Một giỏ là một tập: đổi thứ tự mua không tạo tập mới.

**Phép thử.** Một cặp người không thứ tự và một cặp gồm một lần mua của mỗi người. Có $\binom{10^8}{2}=4\,999\,999\,950\,000\,000$ cặp người và $100\cdot100=10^4$ cặp lần mua cho mỗi cặp người. Gọi $Y$ là số phép thử có hai tập mặt hàng bằng nhau.

**Xác suất một phép thử.** Cố định tập của lần mua thứ nhất; lần mua thứ hai chọn đúng tập đó với xác suất $1/\binom{1000}{10}$, với $\binom{1000}{10}=263\,409\,560\,461\,970\,212\,832\,400\approx2{,}634\times10^{23}$.

**Kỳ vọng.** Theo tuyến tính của kỳ vọng, như Bước 4 của chứng minh Mệnh đề 01.20,
$$
\begin{aligned}
\mathbb E[Y]&=\frac{\binom{10^8}{2}\cdot10^4}{\binom{1000}{10}}\\
&\approx0{,}000189818469\\
&\approx1{,}90\times10^{-4}.
\end{aligned}
$$

**Xác suất có ít nhất một trùng ngẫu nhiên.** $Y$ nhận giá trị nguyên không âm, nên theo Hệ quả 01.22, $\Pr(Y\ge1)\le\mathbb E[Y]\approx1{,}90\times10^{-4}$.

**Trả lời và giả thiết cần.** MMDS (§1.2.2, tr.7) khuyên chỉ tìm những sự kiện hiếm đến mức khó xảy ra trong dữ liệu ngẫu nhiên ("events so rare that they are unlikely to occur in random data"), và trùng tập mặt hàng thuộc loại này: kỳ vọng số trùng ngẫu nhiên chỉ khoảng $1{,}90\times10^{-4}$, so với $249\,750$ biến cố ở hồ sơ lưu trú (Nhận xét 01.23). Vì vậy, nếu có ít nhất một cặp khủng bố thật mua đúng như giả thuyết làm việc, một cặp tìm được khó là trùng ngẫu nhiên trong mô hình nền. Để nói xác suất một cặp tìm được thật sự là khủng bố, cần thêm tỷ lệ nền và mô hình mua hàng của nhóm cần tìm; $\mathbb E[Y]$ không cho hai thông tin đó. Lần mua thực cũng không nhất thiết chọn đều và độc lập, nên giả thiết của mô hình nền phải được kiểm trước khi áp dụng kết luận cho dữ liệu thật.

**Kiểm tra lại.** $4{,}99999995\times10^{15}\cdot10^4/(2{,}634\times10^{23})\approx1{,}898\times10^{-4}$, khớp $0{,}000189818469$. Chỉ so các lần mua cùng số thứ tự giữa hai người sẽ cho $100$ thay vì $10^4$ cặp lần mua, và kỳ vọng nhỏ hơn 100 lần.
:::
