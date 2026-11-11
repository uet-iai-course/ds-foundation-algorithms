# Bài tập Bài 10 — Nén dữ liệu không mất thông tin

Các bài tập củng cố 10.9–10.15 dưới đây lấy từ bài tập 1 của học phần CMU 15-499 *Algorithms in the Real World* (viết tắt CMU-A1) và từ hai ví dụ của sách *The Data Compression Book* của Nelson và Gailly (viết tắt NG) dùng làm bài trên lớp, kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 10.k là của [ghi chú Bài 10](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-nen-du-lieu-khong-mat-thong-tin.html), nơi Bài tập 10.1–10.8 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bốn bài 10.11, 10.12, 10.14 và 10.15 là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 10](lecture-10-nen-du-lieu-khong-mat-thong-tin.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả nén không mất thông tin, mô hình và bộ mã (Mục 1) | 10.1, 10.8 | 10.10 |
| 2. Mã tiền tố, cây mã, bất đẳng thức Kraft (Mục 2) | 10.2 | 10.10, 10.12, 10.13 |
| 3. Tự thông tin, entropy, hai cận cho mã tiền tố (Mục 2) | 10.3 | 10.9, 10.15 |
| 4. Huffman tĩnh: chạy, tối ưu, chi phí, đầu mục (Mục 3) | 10.4 | 10.11 |
| 5. Huffman thích nghi (Mục 4) | 10.5 | 10.14 |
| 6. Mã số học với số thực (Mục 5) | 10.6 | 10.15 |
| 7. Mã số học với thanh ghi, chọn cặp mô hình–bộ mã (Mục 6, Mục 7) | 10.7, 10.8 | — |

## Mức nhận biết

::: exercise Bài tập 10.14 (Ba lần tăng A; NG, Chương 4, Hình 4.2–4.4, tr.69–72)
Cây có trọng số với danh sách vị trí $\#1$–$\#9$: A2, B2, C2, D2, $(\mathrm A,\mathrm B)4$, $(\mathrm C,\mathrm D)4$, $(\#5,\#6)8$, E10, gốc 18. Chạy Thuật toán 10.23 ba lần liên tiếp với $s=\mathrm A$. Sau mỗi lần, ghi các phép đổi, danh sách vị trí và độ dài từ mã của năm ký hiệu.

- (a) Lần tăng thứ nhất, A từ 2 lên 3.
- (b) Lần tăng thứ hai, A từ 3 lên 4.
- (c) Lần tăng thứ ba, A từ 4 lên 5.
:::

::: hint
Ở mỗi nút trên đường đi, tìm nút cuối của khối cùng trọng số trước khi tăng.
:::

::: solution
**Câu (a).** Đổi A ở $\#1$ với D ở $\#4$; phép đổi và danh sách vị trí như lần tăng thứ hai của Ví dụ 10.12. Độ dài: A, B, C, D 3 bit, E 1 bit.

**Câu (b).** Phép tăng và danh sách vị trí như lần tăng thứ ba của Ví dụ 10.13, không có phép đổi. Độ dài không đổi.

**Câu (c).** Đổi A với nút $(\mathrm D,\mathrm B)$ ở $\#5$, rồi đổi $\#7$ với E ở $\#8$; hai phép đổi và danh sách vị trí như lần tăng thứ tư của Ví dụ 10.13. Độ dài: E 1, A 2, C 3, B và D 4 bit.

**Kiểm tra lại.** Tổng Kraft sau Câu (a) và (b) là $\tfrac12+4\cdot\tfrac18=1$, sau Câu (c) là $\tfrac12+\tfrac14+\tfrac18+2\cdot\tfrac1{16}=1$. Trọng số gốc tăng đúng 1 mỗi lần, thành 19, 20, 21; mỗi danh sách không giảm và có bốn cặp anh em ở các vị trí $(\#1,\#2)$, …, $(\#7,\#8)$, như Định lý 10.25.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 10.10 (Mã giải mã duy nhất không là mã tiền tố; CMU-A1, bài 2, tr.1)
Dựng một mã giải mã duy nhất nhưng không là mã tiền tố, và chứng minh hai tính chất đó.
:::

::: hint
Tìm một mã mà điểm bắt đầu của mỗi từ mã nhận ra được bằng một bit.
:::

::: solution
Trên bảng chữ cái $\{\varsigma_1,\ldots,\varsigma_k\}$, đặt $c(\varsigma_i)=1\,0^{i-1}$, tức `1`, `10`, `100`, …

**Không là mã tiền tố.** `1` là tiền tố của `10`, nên $c$ vi phạm điều kiện của Định nghĩa 10.5.

**Giải mã duy nhất.** Mỗi từ mã có đúng một bit 1, ở đầu. Trong $c^*(x)$, các bit 1 vì thế đánh dấu đúng đầu các từ mã, và ký hiệu thứ $t$ là $\varsigma_i$ với $i-1$ là số bit 0 giữa bit 1 thứ $t$ và bit 1 thứ $t+1$, hoặc cuối dòng. Hai thông điệp khác nhau cho hai dãy số bit 0 khác nhau, nên $c^*$ là đơn ánh (Định nghĩa 10.1).

**Kiểm tra lại.** Dòng `110100` có bit 1 ở các vị trí 1, 2, 4, nên tách thành `1`, `10`, `100` với 0, 1, 2 bit 0, tức $\varsigma_1\varsigma_2\varsigma_3$. Tổng Kraft là $\sum_{i=1}^{k}2^{-i}=1-2^{-k}\le1$, khớp Nhận xét 10.10.
:::

::: exercise Bài tập 10.11 (Huffman A–E với quy tắc gán bit khác; NG, Chương 3, tr.32–37)
Thông điệp có số đếm A: 15, B: 7, C: 6, D: 6, E: 5. Chạy Thuật toán 10.14 với quy tắc phá hòa chọn D trước C (NG, tr.35) và quy tắc gán bit 0 cho nút lấy ra trước trong mỗi lượt (NG, tr.62–63).

- (a) Bốn lượt ghép như Ví dụ 10.8; ghi bit gán cho mỗi nút theo quy tắc.
- (b) Lập bảng mã và tính tổng số bit.
- (c) So với mã của Ví dụ 10.8, với 89 bit của Shannon–Fano (Ví dụ 10.7) và với $I(x)\approx85{,}25$ bit.
:::

::: hint
Lượt 1 lấy E5 rồi D6, nên E nhận bit 0 ở lượt đó.
:::

::: solution
**Câu (a).** Lượt 1: E bit 0, D bit 1. Lượt 2: C bit 0, B bit 1. Lượt 3: DE11 bit 0, BC13 bit 1. Lượt 4: A bit 0, nút 24 bit 1.

**Câu (b).** A = `0`, E = `100`, D = `101`, C = `110`, B = `111`. Số bit là $15\cdot1+(7+6+6+5)\cdot3=87$.

**Câu (c).** Cây cùng hình dạng với cây của Ví dụ 10.8, nên cùng 87 bit, nhưng từ mã khác: quy tắc gán bit thuộc giao thức như quy tắc phá hòa (Giả thiết của Thuật toán 10.14). 87 bit ít hơn 89 bit của Shannon–Fano và nằm trong $[I(x);\,I(x)+39)$, đúng Hệ quả 10.19.

**Kiểm tra lại.** Tổng Kraft $\tfrac12+4\cdot\tfrac18=1$; trọng số gốc $39=N$.
:::

::: exercise Bài tập 10.12 (Bất đẳng thức Kraft bằng cách đếm lá; CMU-A1, bài 4A, tr.1)
Cho mã tiền tố $c$ với độ dài $\ell_s$ và $\ell_{\max}=\max_s\ell_s$. Chứng minh $\sum_s2^{-\ell_s}\le1$ bằng cách đếm các lá của cây nhị phân hoàn hảo (perfect binary tree) độ sâu $\ell_{\max}$, tức cây mà mọi nút trong có đúng hai con và mọi lá ở độ sâu $\ell_{\max}$.
:::

::: hint
Đếm số lá ở độ sâu $\ell_{\max}$ nhận một từ mã độ dài $\ell$ làm tổ tiên.
:::

::: solution
**Tập lá của một từ mã.** Cây nhị phân hoàn hảo độ sâu $\ell_{\max}$ có $2^{\ell_{\max}}$ lá, là mọi chuỗi $\ell_{\max}$ bit. Từ mã $c(s)$ là tiền tố của đúng $2^{\ell_{\max}-\ell_s}$ lá, vì $\ell_{\max}-\ell_s$ bit cuối tùy ý; khi $\ell_s=\ell_{\max}$, đó là chính lá $c(s)$.

**Các tập lá rời nhau.** Nếu một lá có hai tiền tố $c(s)$ và $c(s')$ với $s\ne s'$, thì từ mã ngắn hơn là tiền tố của từ mã dài hơn, trái với điều kiện tiền tố.

**Đếm lá.** Tổng số lá được đếm không vượt số lá của cây:
$$
\sum_s2^{\ell_{\max}-\ell_s}\le2^{\ell_{\max}},
$$
và chia hai vế cho $2^{\ell_{\max}}$ được $\sum_s2^{-\ell_s}\le1$. $\square$

**Kiểm tra lại.** Với mã `0`, `10`, `110`, `111` của Bài tập 10.3, $\ell_{\max}=3$ và các tập lá có $4+2+1+1=8=2^3$ phần tử.
:::

::: exercise Bài tập 10.13 (Một từ mã ngắn buộc hai từ mã dài; CMU-A1, bài 4B, tr.1)
Một mã tiền tố có $2^\gamma$ từ mã, $\gamma\ge1$, trong đó có một từ mã ngắn hơn $\gamma$ bit. Chứng minh có ít nhất hai từ mã dài hơn $\gamma$ bit.
:::

::: hint
Phản chứng và dùng Định lý 10.9(a).
:::

::: solution
Giả sử có nhiều nhất một từ mã dài hơn $\gamma$ bit. Từ mã ngắn $u$ có $\lvert u\rvert\le\gamma-1$, nên góp ít nhất $2^{1-\gamma}$ vào tổng Kraft; mỗi từ mã dài không quá $\gamma$ bit góp ít nhất $2^{-\gamma}$. Có hai trường hợp:

- không từ mã nào dài hơn $\gamma$: tổng ít nhất $2^{1-\gamma}+(2^\gamma-1)2^{-\gamma}=1+2^{-\gamma}>1$;
- đúng một từ mã $u'$ dài hơn $\gamma$: tổng ít nhất $2^{1-\gamma}+(2^\gamma-2)2^{-\gamma}+2^{-\lvert u'\rvert}=1+2^{-\lvert u'\rvert}>1$.

Cả hai trường hợp trái với Định lý 10.9(a). $\square$

**Kiểm tra lại.** Mã `0`, `10`, `110`, `111` của Bài tập 10.3 có $4=2^2$ từ mã, nên $\gamma=2$; từ mã `0` ngắn hơn 2 bit, và đúng hai từ mã `110`, `111` dài hơn 2 bit, với tổng Kraft $\tfrac12+\tfrac14+\tfrac18+\tfrac18=1$. Do đó cận "ít nhất hai" là chặt.
:::

## Mức vận dụng

::: exercise Bài tập 10.9 (Entropy có điều kiện của xích Markov hai trạng thái; CMU-A1, bài 1, tr.1)
Một dòng điểm ảnh $X_1X_2\cdots$ nhận giá trị trắng ($\mathrm w$) hoặc đen ($\mathrm b$) và là xích Markov với xác suất chuyển

- $\Pr[X_{t+1}=\mathrm w\mid X_t=\mathrm w]=0{,}9$, $\Pr[X_{t+1}=\mathrm b\mid X_t=\mathrm w]=0{,}1$;
- $\Pr[X_{t+1}=\mathrm w\mid X_t=\mathrm b]=0{,}2$, $\Pr[X_{t+1}=\mathrm b\mid X_t=\mathrm b]=0{,}8$.

Xích này là một mô hình bậc 1 (Định nghĩa 10.3), như các điểm ảnh fax đi thành loạt ở Tình huống 10.2. Entropy có điều kiện (conditional entropy) là
$$
H(X_{t+1}\mid X_t)=\sum_{x}\Pr[X_t=x]\,H(X_{t+1}\mid X_t=x),
$$
trong đó $H(X_{t+1}\mid X_t=x)$ là entropy của phân phối của $X_{t+1}$ khi biết $X_t=x$ (trang chiếu 15 của bài giảng *Data Compression*, học phần CMU 15-499).

- (a) Tìm phân phối dừng $(\pi_{\mathrm w},\pi_{\mathrm b})$, tức phân phối của $X_t$ không đổi theo $t$.
- (b) Tính $H(X_{t+1}\mid X_t)$ khi $X_t$ có phân phối dừng.
- (c) Tính entropy không điều kiện $H(X_t)$ theo phân phối dừng, và tỷ số $H(X_t)/H(X_{t+1}\mid X_t)$.
:::

::: hint
Phân phối dừng thỏa $\pi_{\mathrm w}=0{,}9\,\pi_{\mathrm w}+0{,}2\,\pi_{\mathrm b}$ và $\pi_{\mathrm w}+\pi_{\mathrm b}=1$.
:::

::: solution
**Câu (a).** Từ $\pi_{\mathrm w}=0{,}9\,\pi_{\mathrm w}+0{,}2\,\pi_{\mathrm b}$ suy ra $0{,}1\,\pi_{\mathrm w}=0{,}2\,\pi_{\mathrm b}$, tức $\pi_{\mathrm w}=2\pi_{\mathrm b}$; cùng với $\pi_{\mathrm w}+\pi_{\mathrm b}=1$ được $\pi_{\mathrm w}=2/3$, $\pi_{\mathrm b}=1/3$.

**Câu (b).** Hai entropy theo trạng thái trước là

- $H(X_{t+1}\mid X_t=\mathrm w)=-0{,}9\log_20{,}9-0{,}1\log_20{,}1\approx0{,}469$ bit;
- $H(X_{t+1}\mid X_t=\mathrm b)=-0{,}2\log_20{,}2-0{,}8\log_20{,}8\approx0{,}722$ bit.

Do đó $H(X_{t+1}\mid X_t)\approx\tfrac23\cdot0{,}469+\tfrac13\cdot0{,}722\approx0{,}553$ bit.

**Câu (c).** $H(X_t)=\tfrac23\log_2\tfrac32+\tfrac13\log_23\approx0{,}918$ bit, nên tỷ số là $0{,}918/0{,}553\approx1{,}66$.

**Kiểm tra lại.** $0{,}1\cdot\tfrac23=0{,}2\cdot\tfrac13=\tfrac1{15}$, đúng phương trình dừng.
:::

::: exercise Bài tập 10.15 (Giải mã số học bốn chữ; CMU-A1, bài 3, tr.1)
Mô hình $p(\mathrm a)=0{,}1$, $p(\mathrm b)=0{,}2$, $p(\mathrm c)=0{,}7$ với $F(\mathrm a)=0$, $F(\mathrm b)=0{,}1$, $F(\mathrm c)=0{,}3$; entropy của mô hình là $H\approx1{,}157$ bit mỗi chữ.

- (a) Giải mã dòng `01001110110`, biết thông điệp có bốn chữ.
- (b) Giải thích vì sao dòng này dài hơn mã độ dài cố định 2 bit mỗi chữ.
:::

::: hint
$0{,}01001110110_2=630/2048$, rồi chạy bộ giải mã của Thuật toán 10.32 bốn bước.
:::

::: solution
**Câu (a).** $z=630/2048=0{,}3076171875$. Bắt đầu với $\zeta=z$, mỗi dòng tìm khoảng chứa $\zeta$ rồi tính $\zeta\gets(\zeta-F(s))/p_s$:

| $\zeta$ | khoảng | chữ | $\zeta$ mới |
|---|---|---|---|
| $0{,}3076171875$ | $[0{,}3;\,1)$ | c | $\approx0{,}01088$ |
| $0{,}01088$ | $[0;\,0{,}1)$ | a | $0{,}1088$ |
| $0{,}1088$ | $[0{,}1;\,0{,}3)$ | b | $0{,}0441$ |
| $0{,}0441$ | $[0;\,0{,}1)$ | a | — |

Thông điệp là caba, với khoảng chuỗi $[0{,}307;\,0{,}3084)$, rộng $0{,}7\cdot0{,}1\cdot0{,}2\cdot0{,}1=0{,}0014$.

**Câu (b).** $I(\mathrm{caba})=-\log_20{,}0014\approx9{,}48$ bit, lớn hơn 8 bit của mã cố định, vì caba chứa hai chữ a và một chữ b, ba chữ có xác suất nhỏ theo mô hình. Theo Định lý 10.34, $\lambda=\lceil9{,}48\rceil+1=11$; trung điểm $0{,}3077$ nhân $2^{11}$ được $630{,}17$, nên chuỗi bit là đúng `01001110110` của đề. Tự thông tin kỳ vọng của một thông điệp bốn chữ là $4H\approx4{,}63$ bit, và theo Hệ quả 10.35 số bit kỳ vọng nằm trong $[4{,}63;\,6{,}63)$; thông điệp caba có tự thông tin $9{,}48$ bit, khoảng gấp đôi $4H\approx4{,}63$.

**Kiểm tra lại.** $630/2048\approx0{,}30762\in[0{,}307;\,0{,}3084)$, và $\lambda=11<I(x)+2\approx11{,}48$.
:::
