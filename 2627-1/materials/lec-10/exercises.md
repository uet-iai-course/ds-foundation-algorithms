# Bài tập Bài 10 — Nén dữ liệu không mất thông tin

Các bài tập củng cố 10.9–10.21 dưới đây có gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 10.k là của [ghi chú Bài 10](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-nen-du-lieu-khong-mat-thong-tin.html), nơi Bài tập 10.1–10.8 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bốn bài sách 10.11, 10.12, 10.14 và 10.15 là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 10](lecture-10-nen-du-lieu-khong-mat-thong-tin.html).

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả nén không mất thông tin, mô hình và bộ mã (Mục 1) | 10.1, 10.8 | 10.21 |
| 2. Mã tiền tố, cây mã, bất đẳng thức Kraft (Mục 2) | 10.2 | 10.9, 10.10, 10.12, 10.13 |
| 3. Tự thông tin, entropy, hai cận cho mã tiền tố (Mục 2) | 10.3 | 10.18 |
| 4. Huffman tĩnh: chạy, tối ưu, chi phí, đầu mục (Mục 3) | 10.4 | 10.11, 10.19, 10.21 |
| 5. Huffman thích nghi theo NG (Mục 4) | 10.5 | 10.14, 10.16 |
| 6. Mã số học với số thực (Mục 5) | 10.6 | 10.15, 10.20 |
| 7. Mã số học với thanh ghi, chọn cặp mô hình–bộ mã (Mục 6, Mục 7) | 10.7, 10.8 | 10.17 |

## Mức nhận biết

::: exercise Bài tập 10.9 (Một dòng bit, ba cách đọc; CMU, trang chiếu 22)
Cho mã a = `1`, b = `01`, c = `101`, d = `011`. Liệt kê mọi cách tách dòng `10111` thành từ mã. Tính tổng Kraft của mã. Xác định mã có giải mã duy nhất không, và cho một mã tiền tố có cùng bộ độ dài.
:::

::: hint
Thử từ mã đầu là `1` rồi là `101`.
:::

::: solution
Ba cách tách: `1`·`01`·`1`·`1` = abaa, `101`·`1`·`1` = caa, `1`·`011`·`1` = ada. Tổng Kraft là $\tfrac12+\tfrac14+\tfrac18+\tfrac18=1$, nhưng mã không giải mã duy nhất, vì Định lý 10.9 nói về độ dài chứ không về một bộ từ mã. Bộ độ dài $(1,2,3,3)$ có mã tiền tố a = `0`, b = `10`, c = `110`, d = `111`, dựng theo Bước 2 của chứng minh Định lý 10.9.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 10.10 (Giải mã duy nhất nhưng không tiền tố; CMU-A1, bài 2, tr.1)
Trên bảng chữ cái $\{\varsigma_0,\varsigma_1,\ldots,\varsigma_{k-1}\}$, đặt $c(\varsigma_i)=1\,0^i$, tức `1`, `10`, `100`, … Chứng tỏ $c$ không là mã tiền tố nhưng giải mã duy nhất. Xét xem bộ giải mã có nhận ra ký hiệu ngay khi đọc bit cuối của từ mã hay không.
:::

::: hint
Mọi từ mã bắt đầu bằng bit 1 và không chứa bit 1 nào khác.
:::

::: solution
`1` là tiền tố của `10`, nên $c$ không là mã tiền tố. Trong $c^*(x)$, các bit 1 đánh dấu đúng đầu các từ mã, nên $x$ được khôi phục duy nhất: ký hiệu thứ $t$ là $\varsigma_i$ với $i$ là số bit 0 giữa bit 1 thứ $t$ và bit 1 thứ $t+1$, hoặc cuối dòng (lời giải CMU-A1, tr.1). Sau khi đọc `1`, bộ giải mã chưa biết đó là $\varsigma_0$ hay đầu của $\varsigma_1$; nó phải đọc thêm một bit, nên mã không giải mã tức thời như mã tiền tố (Mệnh đề 10.6(c)).
:::

::: exercise Bài tập 10.11 (Huffman A–E với quy tắc gán bit khác; NG, Chương 3, tr.32–37)
Thông điệp có số đếm A: 15, B: 7, C: 6, D: 6, E: 5. Chạy Thuật toán 10.14 với quy tắc phá hòa của NG (chọn D trước C) và quy tắc gán bit 0 cho nút lấy ra trước trong mỗi lượt. Ghi bốn lượt ghép, bảng mã và tổng số bit. So với mã của Ví dụ 10.8, với 89 bit của Shannon–Fano và $85{,}25$ bit tự thông tin.
:::

::: hint
Lượt 1 lấy E5 rồi D6, nên E nhận bit 0 ở lượt đó.
:::

::: solution
**Bốn lượt.** E5 (bit 0) và D6 (bit 1) thành 11; C6 (bit 0) và B7 (bit 1) thành 13; 11 (bit 0) và 13 (bit 1) thành 24; A15 (bit 0) và 24 (bit 1) thành 39.

**Bảng mã.** A = `0`, E = `100`, D = `101`, C = `110`, B = `111`. Số bit là $15\cdot1+(7+6+6+5)\cdot3=87$.

**So sánh.** Cây cùng hình dạng với cây của Ví dụ 10.8, nên cùng 87 bit, nhưng từ mã khác nhau: quy tắc gán bit thuộc giao thức như quy tắc phá hòa (Nhận xét 10.4). 87 bit ít hơn 89 bit của Shannon–Fano và nằm trong $[I(x);\,I(x)+39)$ với $I(x)\approx85{,}25$, đúng Hệ quả 10.19.
:::

::: exercise Bài tập 10.12 (Bất đẳng thức Kraft bằng cách đếm lá; CMU-A1, bài 4A, tr.1)
Cho mã tiền tố $c$ với độ dài $\ell_s$ và $\ell_{\max}=\max_s\ell_s$. Chứng minh $\sum_s2^{-\ell_s}\le1$ bằng cách đếm các lá của cây nhị phân hoàn hảo (perfect binary tree) độ sâu $\ell_{\max}$, tức mọi nút trong có đúng hai con và mọi lá ở độ sâu $\ell_{\max}$.
:::

::: hint
Đếm số lá ở độ sâu $\ell_{\max}$ nhận một từ mã độ dài $\ell$ làm tổ tiên.
:::

::: solution
**Bước 1 (tập lá của một từ mã).** Cây nhị phân hoàn hảo độ sâu $\ell_{\max}$ có $2^{\ell_{\max}}$ lá, là mọi chuỗi $\ell_{\max}$ bit. Từ mã $c(s)$ là tổ tiên của đúng các lá có tiền tố $c(s)$, gồm $2^{\ell_{\max}-\ell_s}$ lá, vì $\ell_{\max}-\ell_s$ bit cuối tùy ý.

**Bước 2 (rời nhau).** Nếu một lá có hai tiền tố $c(s)$ và $c(s')$ với $s\ne s'$, thì từ mã ngắn hơn là tiền tố của từ mã dài hơn, trái với điều kiện tiền tố. Vậy các tập lá đôi một rời nhau.

**Bước 3 (đếm).**
$$
\begin{aligned}
\sum_s2^{\ell_{\max}-\ell_s}&\le2^{\ell_{\max}},\\
\sum_s2^{-\ell_s}&\le1. \qquad\square
\end{aligned}
$$
Lời giải CMU-A1 (tr.3) in bất đẳng thức của Bước 3 theo chiều ngược lại; chiều đúng là tổng số lá được đếm không vượt $2^{\ell_{\max}}$.
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
:::

::: exercise Bài tập 10.14 (Ba lần tăng A, một lần tăng D; NG, Chương 4, Hình 4.2–4.4, tr.69–72)
Cây có trọng số với danh sách vị trí $\#1$–$\#9$: A2, B2, C2, D2, $(\mathrm A,\mathrm B)4$, $(\mathrm C,\mathrm D)4$, $(\#5,\#6)8$, E10, gốc 18. Chạy Thuật toán 10.23 ba lần với $s=\mathrm A$, rồi (d) một lần với $s=\mathrm D$ từ cây cuối. Sau mỗi lần, ghi các phép đổi, danh sách vị trí và độ dài từ mã của năm ký hiệu.
:::

::: hint
Ở mỗi nút trên đường đi, tìm nút cuối của khối cùng trọng số trước khi tăng.
:::

::: solution
**Lần 1 (A 2→3).** Đổi A với D, nút cuối khối trọng số 2. Danh sách D2, B2, C2, A3, $(\mathrm D,\mathrm B)4$, $(\mathrm C,\mathrm A)5$, 9, E10, 19. Độ dài: A–D 3 bit, E 1 bit.

**Lần 2 (A 3→4).** Không đổi. Danh sách D2, B2, C2, A4, $(\mathrm D,\mathrm B)4$, $(\mathrm C,\mathrm A)6$, 10, E10, 20. Độ dài không đổi.

**Lần 3 (A 4→5).** Đổi A với nút $(\mathrm D,\mathrm B)$ ở $\#5$, rồi đổi nút $\#7$ trọng số 10 với E. Danh sách D2, B2, C2, $(\mathrm D,\mathrm B)4$, A5, $(\mathrm C,\#4)6$, E10, $(\mathrm A,\#6)11$, 21. Độ dài: E 1, A 2, C 3, B và D 4 bit, như NG (tr.71).

**(d) D 2→3.** Khối trọng số 2 gồm D, B, C ở $\#1$–$\#3$; đổi D với C, rồi tăng D, nút $\#6$, $\#8$, gốc thành 3, 7, 12, 22. Danh sách C2, B2, D3, $(\mathrm C,\mathrm B)4$, A5, $(\mathrm D,\#4)7$, E10, $(\mathrm A,\#6)12$, 22. Độ dài: E 1, A 2, D 3, B và C 4 bit.

**Kiểm tra lại.** Trọng số gốc tăng đúng 1 mỗi lần; mỗi danh sách không giảm và có bốn cặp anh em ở các vị trí $(\#1,\#2)$, …, $(\#7,\#8)$, như Định lý 10.25.
:::

::: exercise Bài tập 10.15 (Giải mã số học bốn chữ; CMU-A1, bài 3, tr.1)
Mô hình $p(\mathrm a)=0{,}1$, $p(\mathrm b)=0{,}2$, $p(\mathrm c)=0{,}7$ với $F(\mathrm a)=0$, $F(\mathrm b)=0{,}1$, $F(\mathrm c)=0{,}3$. Giải mã dòng `01001110110`, biết thông điệp có bốn chữ. Giải thích vì sao dòng này dài hơn mã độ dài cố định 2 bit mỗi chữ, dù entropy của mô hình chỉ hơn 1 bit một chút.
:::

::: hint
$0{,}01001110110_2=630/2048$.
:::

::: solution
**Giải mã.** $z=630/2048=0{,}3076171875$. Đặt $\zeta=z$; lần lượt: $\zeta\in[0{,}3;\,1)$ cho c, $\zeta\gets(\zeta-0{,}3)/0{,}7\approx0{,}01088$; $\zeta\in[0;\,0{,}1)$ cho a, $\zeta\gets0{,}1088$; $\zeta\in[0{,}1;\,0{,}3)$ cho b, $\zeta\gets0{,}0441$; $\zeta\in[0;\,0{,}1)$ cho a. Thông điệp là caba, như lời giải CMU-A1 (tr.2). Khoảng chuỗi là $[0{,}307;\,0{,}3084)$, rộng $0{,}0014$.

**Độ dài.** $I(\mathrm{caba})=-\log_20{,}0014\approx9{,}48$ bit, lớn hơn 8 bit của mã cố định, vì caba chứa hai chữ a và một chữ b ít xảy ra theo mô hình. Theo Định lý 10.34, $\lambda=\lceil9{,}48\rceil+1=11$; trung điểm $0{,}3077$ nhân $2^{11}$ được $630{,}17$, nên chuỗi bit đúng là `01001110110` của đề. Entropy $H\approx1{,}157$ bit nói về độ dài kỳ vọng $4H\approx4{,}63$ bit của một thông điệp bốn chữ ngẫu nhiên, không về thông điệp caba cụ thể.
:::

::: exercise Bài tập 10.16 (Ký hiệu mới qua `ESCAPE`)
Mã hóa thông điệp AB bằng Thuật toán 10.26, bắt đầu từ cây khởi tạo, với mã ASCII A $=65=01000001_2$ và B $=66=01000010_2$. Ghi từ mã phát ra cho mỗi ký hiệu và cho `EOS`, danh sách vị trí sau mỗi lần thêm lá và cập nhật, và tổng số bit; so với 16 bit ASCII.
:::

::: hint
Trên cây khởi tạo, `ESCAPE` ở $\#1$ có từ mã `1`; lá mới luôn được thêm dưới vị trí $\#1$.
:::

::: solution
**Ký hiệu A.** Phát `1` rồi `01000001`, 9 bit. Thêm lá: A0, `ESCAPE`1, (A, `ESCAPE`)1, `EOS`1, gốc 2. Cập nhật: A thành 1; nút $\#3$ có nút cuối khối là `EOS` ở $\#4$, nên đổi hai nút rồi tăng thành 2; gốc thành 3. Danh sách A1, `ESCAPE`1, `EOS`1, (A, `ESCAPE`)2, gốc 3; từ mã `EOS` = `1`, `ESCAPE` = `00`, A = `01`.

**Ký hiệu B.** Phát `00` rồi `01000010`, 10 bit. Thêm lá dưới A ở $\#1$: B0, A1, (A, B)1, `ESCAPE`1, `EOS`1, $(\#3,\mathtt{ESCAPE})2$, gốc 3. Cập nhật: B thành 1; nút $\#3$ có nút cuối khối là `EOS` ở $\#5$, nên đổi rồi tăng thành 2; gốc thành 4. Danh sách B1, A1, `EOS`1, `ESCAPE`1, (A, B)2, (`ESCAPE`, `EOS`)2, gốc 4; từ mã `ESCAPE` = `00`, `EOS` = `01`, A = `10`, B = `11`.

**Kết thúc.** Phát `EOS` = `01`. Dòng bit `101000001000100001001` dài 21 bit, hơn 16 bit ASCII, vì mỗi ký hiệu mới tốn từ mã `ESCAPE` cộng 8 bit thô.
:::

::: exercise Bài tập 10.17 (Bit chờ với thanh ghi 8 bit)
Chạy Thuật toán 10.37 với $R=8$, tức $Q=64$, trên mô hình $f_{\mathrm a}=1$, $f_{\mathrm b}=2$, $f_{\mathrm c}=7$, $G(\mathrm a)=0$, $G(\mathrm b)=1$, $G(\mathrm c)=3$, $N=10$, cho thông điệp bc, rồi kết thúc theo quy tắc của NG. Ghi `low`, `high`, $m$ và các bit phát sau mỗi thao tác; kiểm dòng bit nằm trong khoảng thực của bc.
:::

::: hint
Ở trạng thái khởi tạo, $\texttt{low}=0$, $\texttt{high}=255$, $\texttt{range}=256$; ngưỡng là $Q=64$, $2Q=128$, $3Q=192$.
:::

::: solution
**Ký hiệu b.** $\texttt{high}=0+\lfloor256\cdot3/10\rfloor-1=75$, $\texttt{low}=\lfloor256\cdot1/10\rfloor=25$. Vì $75<128$, nửa dưới: phát `0`, $\texttt{low}=50$, $\texttt{high}=151$. Dừng, vì $50<64$ và $151\ge128$.

**Ký hiệu c.** $\texttt{range}=102$, $\texttt{high}=50+\lfloor102\cdot10/10\rfloor-1=151$, $\texttt{low}=50+\lfloor102\cdot3/10\rfloor=80$. Vì $64\le80$ và $151<192$, khoảng giữa: $m=1$, $\texttt{low}=2(80-64)=32$, $\texttt{high}=2(151-64)+1=175$. Dừng, vì $32<64$ và $175\ge128$.

**Kết thúc.** Bit thứ hai của $\texttt{low}=32$ (`00100000`) là 0, nên phát `0` rồi $m+1=2$ bit `1`. Bỏ qua các bit 0 đệm, dòng bit là `0011`, biểu diễn $0{,}1875$.

**Kiểm tra lại.** Khoảng thực: b cho $[0{,}1;\,0{,}3)$, c cho $[0{,}16;\,0{,}3)$, và $0{,}16\le0{,}1875<0{,}3$.
:::

::: exercise Bài tập 10.18 (Mã tối ưu cho xác suất lũy thừa của 2)
Cho phân phối $P$ trên $\Sigma$ với mọi $p_s=2^{-\ell_s}$, $\ell_s$ nguyên dương. Chứng minh có mã tiền tố $c$ với $\lvert c(s)\rvert=\ell_s$ cho mọi $s$, rằng $\bar\ell(c)=H(P)$, và rằng $c$ là mã tiền tố tối ưu cho $P$.
:::

::: hint
Tính tổng Kraft của bộ độ dài, rồi dùng Định lý 10.9(b) và Định lý 10.12.
:::

::: solution
**Bước 1 (tồn tại).** $\sum_s2^{-\ell_s}=\sum_sp_s=1$, nên theo Định lý 10.9(b) có mã tiền tố $c$ với $\lvert c(s)\rvert=\ell_s$.

**Bước 2 (độ dài trung bình).** $\ell_s=\log_2(1/p_s)=I(s)$, nên
$$
\begin{aligned}
\bar\ell(c)&=\sum_sp_s\ell_s\\
&=\sum_sp_s\log_2\frac1{p_s}=H(P).
\end{aligned}
$$

**Bước 3 (tối ưu).** Theo Định lý 10.12, mọi mã tiền tố $c'$ có $\bar\ell(c')\ge H(P)=\bar\ell(c)$, nên không mã tiền tố nào có độ dài trung bình nhỏ hơn. $\square$
:::

::: exercise Bài tập 10.19 (Ký hiệu nặng hơn không nằm sâu hơn)
Cho $T$ là một cây tối ưu cho số đếm $f$, và $d_s$ là độ sâu của lá $s$ trong $T$. Chứng minh rằng nếu $f_s>f_{s'}$ thì $d_s\le d_{s'}$.
:::

::: hint
Phản chứng: giả sử $d_s>d_{s'}$, đổi chỗ hai lá và dùng công thức $\Delta$ của Ví dụ 10.9.
:::

::: solution
Giả sử $d_s>d_{s'}$. Đổi chỗ hai lá $s$ và $s'$ cho một cây $T'$ có cùng các lá, và theo Ví dụ 10.9,
$$
\begin{aligned}
&\operatorname{cost}(T')-\operatorname{cost}(T)\\
&\quad=(f_s-f_{s'})(d_{s'}-d_s).
\end{aligned}
$$
Thừa số thứ nhất dương, thừa số thứ hai âm, nên $\operatorname{cost}(T')<\operatorname{cost}(T)$, trái với tính tối ưu của $T$. Vậy $d_s\le d_{s'}$. $\square$
:::

## Mức vận dụng

::: exercise Bài tập 10.20 (Quy tắc trung điểm có luôn ngắn nhất; CMU, trang chiếu 49)
Một khoảng chuỗi là $[0;\,0{,}33)$. Tính chuỗi bit do quy tắc của Định lý 10.34 cho, rồi tìm chuỗi bit ngắn nhất có khoảng mã nằm trong khoảng này.
:::

::: hint
Thử các chuỗi 2 bit.
:::

::: solution
$-\log_20{,}33\approx1{,}60$, nên $\lambda=3$; trung điểm $0{,}165$ nhân 8 được $1{,}32$, nên chuỗi là `001`, khoảng mã $[0{,}125;\,0{,}25)$. Chuỗi `00` có khoảng mã $[0;\,0{,}25)\subseteq[0;\,0{,}33)$ và ngắn hơn 1 bit; chuỗi `0` có khoảng $[0;\,0{,}5)$ thì không. Quy tắc bảo đảm tính chứa và cận $\lambda<I(x)+2$ của Định lý 10.34, nhưng không luôn cho chuỗi ngắn nhất.
:::

::: exercise Bài tập 10.21 (Bảng mã dùng chung hay bảng riêng)
Bảng mã Huffman mẫu của NG (tr.22) cho Q và Z từ mã 11 bit. Một tệp gồm $n$ ký tự, chỉ là Q và Z. So ba cách lưu: ASCII; mã theo bảng mẫu dùng chung; mã Huffman tĩnh dựng từ chính tệp, gửi kèm bảng số đếm khoảng 256 byte (NG, tr.24), bỏ qua `EOS`. Tìm $n$ nhỏ nhất để cách thứ ba ngắn hơn từng cách còn lại, và chỉ ra giả thiết của Định lý 10.18 mà cách thứ hai vi phạm.
:::

::: hint
Với hai ký hiệu, mã Huffman dùng 1 bit mỗi ký tự; 256 byte là 2 048 bit.
:::

::: solution
Ba cách tốn $8n$, $11n$ và $n+2\,048$ bit. Cách thứ ba ngắn hơn cách thứ hai khi $n+2\,048<11n$, tức $n>204{,}8$, nên $n\ge205$; ngắn hơn ASCII khi $n+2\,048<8n$, tức $n>292{,}6$, nên $n\ge293$.

Bảng mẫu được dựng từ số đếm của văn bản khác, nên cây không tối ưu cho tệp này: Định lý 10.18 chỉ bảo đảm tối ưu cho số đếm đã đưa vào thuật toán (Tình huống 10.3(a)).
:::
