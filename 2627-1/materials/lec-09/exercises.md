# Bài tập Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Các bài tập củng cố 09.10–09.22 dưới đây lấy từ bài tập của hai giáo trình *Mining of Massive Datasets* của Leskovec, Rajaraman và Ullman (viết tắt MMDS) và *Foundations of Data Science* của Blum, Hopcroft và Kannan (viết tắt BHK), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 09.k là của [ghi chú Bài 09](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-dong-du-lieu-dem-momen-va-cua-so.html), nơi Bài tập 09.1–09.9 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Năm bài 09.10, 09.11, 09.12, 09.15 và 09.16 (MMDS Bài 4.5.1, 4.4.1, 4.5.3, 4.6.1, 4.6.3) là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 09](lecture-09-dong-du-lieu-dem-momen-va-cua-so.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả các đại lượng trên dòng và chọn phác thảo theo đại lượng, bảo đảm và chi phí (Mục 1, Mục 7) | 09.1, 09.9 | 09.10, 09.18 |
| 2. Chạy Flajolet–Martin; cận hai phía của $2^R$ và cận thất bại của trung vị (Mục 2) | 09.2, 09.3 | 09.11, 09.17, 09.21 |
| 3. Chạy biến Alon–Matias–Szegedy; $\mathbb E[X]=F_2$, dạng tổng quát cho $F_p$, lấy mẫu hồ chứa (Mục 3) | 09.4, 09.5 | 09.12, 09.13, 09.14, 09.22 |
| 4. Cập nhật và truy vấn Count-Min Sketch; chọn số ô và số hàng theo $\varepsilon$, $\delta$, $\kappa$ (Mục 4) | 09.6 | 09.20 |
| 5. Duy trì và truy vấn biểu diễn DGIM; bộ nhớ $O(\log^2N)$ bit và cận sai số tương đối 50% (Mục 5) | 09.7 | 09.15, 09.16, 09.19 |
| 6. Cập nhật cửa sổ suy giảm mũ và tìm phần tử phổ biến với ít hơn $1/(c\theta)$ điểm (Mục 6) | 09.8 | — |

## Mức nhận biết

::: exercise Bài tập 09.10 (Số bất ngờ và mômen bậc ba; Bài 4.5.1, MMDS §4.5.6, tr.149)
Cho dòng $3,1,4,1,3,4,2,1,2$.

- (a) Tính số bất ngờ $F_2$ của dòng.
- (b) Tính mômen bậc ba $F_3$ của dòng.
:::

::: hint
Lập bảng tần suất rồi áp Định nghĩa 09.1.
:::

::: solution
**Câu (a).** Tần suất là $f_1=3$ (vị trí 2, 4, 8), $f_2=2$ (vị trí 7, 9), $f_3=2$ (vị trí 1, 5), $f_4=2$ (vị trí 3, 6). Do đó $F_2=9+4+4+4=21$.

**Câu (b).** $F_3=27+8+8+8=51$.

**Kiểm tra lại.** $f_1+f_2+f_3+f_4=3+2+2+2=9$, bằng độ dài dòng; $F_2=21$ bằng trung bình các ước lượng AMS của Bài tập 09.12.
:::

::: exercise Bài tập 09.14 (Ước lượng mômen bậc bốn; Bài 4.5.6, MMDS §4.5.6, tr.150)
Một biến AMS có bộ đếm $v$ khi dòng độ dài $r$ kết thúc. Xác định cách đổi $v$ thành ước lượng không chệch của mômen bậc bốn $F_4$.
:::

::: hint
Viết $2v-1=v^2-(v-1)^2$ rồi thay bậc 2 bằng bậc 4.
:::

::: solution
Theo Hệ quả 09.23 với $p=4$, ước lượng là
$$
X_4=r\bigl(v^4-(v-1)^4\bigr)=r(4v^3-6v^2+4v-1),
$$
và $\mathbb E[X_4]=F_4$.

**Kiểm tra lại.** Trên dòng $3,1,4,1,3,4,2,1,2$ của Bài tập 09.10, với $r=9$ và các bộ đếm của Bài tập 09.12: $v=1$ cho $9$, $v=2$ cho $9\cdot15=135$, $v=3$ cho $9\cdot65=585$. Các ước lượng là $135,585,135,135,9,9,135,9,9$, tổng $1\,161$, trung bình $129=3^4+3\cdot2^4=F_4$.
:::

::: exercise Bài tập 09.20 (Họ băm đều nhưng không độc lập từng cặp; Bài 6.7, BHK §6.6, tr.204)
Cho tập vũ trụ $\mathcal U$ có ít nhất hai phần tử và số nguyên $m\ge2$ (BHK viết $M$). Xây dựng một họ $\mathcal H$ các hàm $\mathcal U\to\{0,\ldots,m-1\}$ sao cho với mọi $x\in\mathcal U$, khi $h$ chọn đều từ $\mathcal H$, $h(x)$ nhận mỗi giá trị trong $\{0,\ldots,m-1\}$ với cùng xác suất ($\mathcal H$ là 1-universal), nhưng $\mathcal H$ không là họ độc lập từng cặp (2-universal) của Định nghĩa 09.31.
:::

::: hint
Tính đều chỉ ràng buộc từng giá trị $h(x)$ riêng lẻ; tìm một họ làm $h(x)$, $h(y)$ phụ thuộc nhau.
:::

::: solution
Lấy $\mathcal H=\{h_0,\ldots,h_{m-1}\}$ với $h_k(x)=k$ cho mọi $x\in\mathcal U$.

**Tính đều.** Với mọi $x$ và $w$, $h(x)=w$ khi và chỉ khi $h=h_w$, nên $\Pr[h(x)=w]=1/m$.

**Không độc lập từng cặp.** Với $x\ne y$, $\Pr[h(x)=w,\,h(y)=z]$ bằng $1/m$ khi $w=z$ và bằng 0 khi $w\ne z$, khác $1/m^2$ vì $m\ge2$. Hơn nữa $\Pr[h(x)=h(y)]=1>1/m$, nên $\mathcal H$ cũng không là họ băm phổ dụng theo Định nghĩa 09.31. Dùng họ này cho các hàng Count-Min là phản ví dụ "Bỏ họ băm phổ dụng" nêu sau Định lý 09.37.

**Kiểm tra lại.** Với $m=3$, cặp $(h(x),h(y))$ nhận $(0,0)$, $(1,1)$, $(2,2)$, mỗi cặp với xác suất $1/3$, tổng bằng 1; họ độc lập từng cặp phải cho mỗi cặp trong 9 cặp xác suất $1/9$.
:::

::: exercise Bài tập 09.22 (Chọn một phần tử đều trên dòng; Bài 6.1, câu 1, BHK §6.6, tr.204)
Cho dòng $x_1,\ldots,x_r$, mỗi phần tử là một số nguyên trong $\{1,\ldots,\lvert\mathcal U\rvert\}$ (BHK viết $a_1,\ldots,a_n$ và $m$), với $r$ chưa biết trước.

- (a) Xây dựng một thuật toán dòng một lượt chọn một phần tử của dòng đều ngẫu nhiên, tức mỗi vị trí $i\le r$ được chọn với xác suất $1/r$.
- (b) Xác định bộ nhớ thuật toán cần.
:::

::: hint
(a) Giữ một phần tử và thay nó bằng phần tử thứ $i$ với một xác suất phụ thuộc $i$.
:::

::: solution
**Câu (a).** Giữ $x_1$ và bộ đếm $i=1$. Khi $x_i$ đến với $i\ge2$, rút $\xi$ đều trên $\{1,\ldots,i\}$; nếu $\xi=1$ thì thay phần tử đang giữ bằng $x_i$. Đây là Thuật toán 08.16 với hồ chứa cỡ $s=1$, cũng là bước 4 của Thuật toán 09.24 với $s=1$. Theo Định lý 08.17 với $s=1$, sau $r$ phần tử mỗi vị trí đã đọc có mặt trong hồ với xác suất $1/r$.

**Câu (b).** Một phần tử cần $\lceil\log_2\lvert\mathcal U\rvert\rceil$ bit và bộ đếm vị trí cần $\lceil\log_2(r+1)\rceil$ bit, tức $O(\log\lvert\mathcal U\rvert+\log r)$ bit, cộng phần cần để rút $\xi$.

**Kiểm tra lại.** Với $r=3$: $x_1$ được giữ với xác suất $1\cdot\frac12\cdot\frac23=\frac13$, $x_2$ với xác suất $\frac12\cdot\frac23=\frac13$, $x_3$ với xác suất $\frac13$.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 09.11 (Độ dài đuôi dưới ba hàm băm; Bài 4.4.1, MMDS §4.4.5, tr.145)
Dòng gồm các số nguyên $3,1,4,1,5,9,2,6,5$. Các hàm băm có dạng $h(x)=\alpha x+\beta\bmod32$, kết quả coi như số nhị phân 5 bit. Xác định độ dài đuôi của mỗi phần tử và ước lượng $2^R$ của số phần tử phân biệt khi hàm băm là

- (a) $h(x)=2x+1\bmod32$;
- (b) $h(x)=3x+7\bmod32$;
- (c) $h(x)=4x\bmod32$.
:::

::: hint
Tính $h(x)$, viết 5 bit, đếm số bit 0 ở cuối; $R$ là số lớn nhất; ước lượng là $2^R$ (Thuật toán 09.6).
:::

::: solution
| $x$ | 3 | 1 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| (a) $2x+1$ | $00111$ | $00011$ | $01001$ | $00011$ | $01011$ | $10011$ | $00101$ | $01101$ | $01011$ |
| đuôi (a) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| (b) $3x+7$ | $10000$ | $01010$ | $10011$ | $01010$ | $10110$ | $00010$ | $01101$ | $11001$ | $10110$ |
| đuôi (b) | 4 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| (c) $4x$ | $01100$ | $00100$ | $10000$ | $00100$ | $10100$ | $00100$ | $01000$ | $11000$ | $10100$ |
| đuôi (c) | 2 | 2 | 4 | 2 | 2 | 2 | 3 | 3 | 2 |

Dòng có 7 phần tử phân biệt $\{1,2,3,4,5,6,9\}$.

**Câu (a).** $R=0$, ước lượng $2^0=1$.

**Câu (b).** $R=4$ (phần tử 3), ước lượng $2^4=16$.

**Câu (c).** $R=4$ (phần tử 4), ước lượng $16$.

**Kiểm tra lại.** Ở (a), $2x+1$ luôn lẻ nên mọi đuôi bằng 0. Ở (b), (c), $3\cdot3+7=16=10000_2$ và $4\cdot4=16$, nên đuôi dài nhất bằng 4.
:::

::: exercise Bài tập 09.12 (Giá trị các biến AMS; Bài 4.5.3, MMDS §4.5.6, tr.150)
Thuật toán AMS ước lượng số bất ngờ của dòng $3,1,4,1,3,4,2,1,2$, độ dài $r=9$, với một biến bắt đầu ở mỗi vị trí $i=1,\ldots,9$.

- (a) Xác định bộ đếm của biến bắt đầu ở mỗi vị trí $i$ khi dòng kết thúc.
- (b) Tính ước lượng $9(2v_i-1)$ của từng biến và trung bình của chín ước lượng.
:::

::: hint
(a) Bộ đếm của biến bắt đầu ở $i$ là $v_i$ của Định nghĩa 09.19.
:::

::: solution
**Câu (a).** Bộ đếm $v_i$ là số lần $x_i$ xuất hiện trong $x_i,\ldots,x_9$.

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $x_i$ | 3 | 1 | 4 | 1 | 3 | 4 | 2 | 1 | 2 |
| $v_i$ | 2 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 1 |

**Câu (b).** Các ước lượng $9(2v_i-1)$ theo vị trí là $27,45,27,27,9,9,27,9,9$. Tổng là 189, trung bình $189/9=21$.

**Kiểm tra lại.** Trung bình 21 bằng $F_2$ của Bài tập 09.10, đúng Định lý 09.22, vì trung bình trên mọi vị trí là kỳ vọng với $I$ đều.
:::

::: exercise Bài tập 09.13 (Mômen bậc ba từ các biến AMS; Bài 4.5.4, MMDS §4.5.6, tr.150)
Cho dòng $3,1,4,1,3,4,2,1,2$, độ dài $r=9$, với một biến AMS bắt đầu ở mỗi vị trí và các bộ đếm $v_1,\ldots,v_9=2,3,2,2,1,1,2,1,1$ của Bài tập 09.12. Các biến được dùng để ước lượng mômen bậc ba.

- (a) Tính ước lượng mômen bậc ba của từng biến.
- (b) So trung bình các ước lượng với $F_3$ của dòng.
:::

::: hint
(a) Bộ đếm không đổi; chỉ phép trả lời đổi thành $r(3v^2-3v+1)$ (Hệ quả 09.23).
:::

::: solution
**Câu (a).** Theo Hệ quả 09.23, ước lượng là $9(3v^2-3v+1)$: $v=1$ cho $9$, $v=2$ cho $9\cdot7=63$, $v=3$ cho $9\cdot19=171$. Các ước lượng theo vị trí là $63,171,63,63,9,9,63,9,9$.

**Câu (b).** Tổng là 459, trung bình $459/9=51$, bằng $F_3=51$ của Bài tập 09.10.

**Kiểm tra lại.** Phần tử 1 ở vị trí 2, 4, 8 có $v=3,2,1$ và góp $171+63+9=243=9\cdot3^3=r\,f_1^3$.
:::

::: exercise Bài tập 09.15 (Hai truy vấn trên MMDS Hình 4.2; Bài 4.6.1, MMDS §4.6.8, tr.157)
Cửa sổ như MMDS Hình 4.2, tức trạng thái của Ví dụ 09.14: các thùng (kích thước, mốc phải) từ cũ sang mới $(8,r-22)$, $(4,r-14)$, $(4,r-8)$, $(2,r-4)$, $(1,r-2)$, $(1,r-1)$; hai mươi lăm bit cuối, từ vị trí $r-24$ tới $r$, là $1011011000101110110010110$.

- (a) Ước lượng số bit 1 trong $k=5$ vị trí cuối.
- (b) Ước lượng số bit 1 trong $k=15$ vị trí cuối.

Tính sai lệch của mỗi ước lượng so với giá trị đúng.
:::

::: hint
Tìm $b^*$, thùng cũ nhất có mốc phải $\ge r-k+1$ (Thuật toán 09.45).
:::

::: solution
**Câu (a).** Các vị trí $r-4,\ldots,r$ là $10110$, có 3 bit 1. $b^*=(2,r-4)$; $T=1+1=2$; $\widehat y_5=2+2/2=3$. Ước lượng đúng, sai lệch 0.

**Câu (b).** Các vị trí $r-14,\ldots,r$ là $101110110010110$, có 9 bit 1, ở $r-14$, $r-12$, $r-11$, $r-10$, $r-8$, $r-7$, $r-4$, $r-2$, $r-1$. $b^*=(4,r-14)$, chỉ mốc phải của nó nằm trong hậu tố; $T=1+1+2+4=8$; $\widehat y_{15}=8+4/2=10$. Ước lượng thừa 1, sai số tương đối $1/9\approx11\%$.

**Kiểm tra lại.** Theo Bước 1 của chứng minh Định lý 09.46, $y_k=T+\pi$: (a) $2+1=3$, (b) $8+1=9$, khớp số đếm trực tiếp; với $\pi=1$ và $\lvert b^*\rvert=2^\mu$, sai lệch $2^{\mu-1}-1$ bằng 0 ở (a), bằng 1 ở (b).
:::

::: exercise Bài tập 09.16 (Ba bit 1 nữa trên Hình 4.3; Bài 4.6.3, MMDS §4.6.8, tr.157)
Ba bit 1 nữa đi vào cửa sổ biểu diễn ở MMDS Hình 4.3, tức các thùng (kích thước, mốc phải) từ cũ sang mới $(8,r-23)$, $(4,r-15)$, $(4,r-9)$, $(2,r-5)$, $(2,r-2)$, $(1,r)$. Có thể giả sử không bit 1 nào trong hình rời cửa sổ.

- (a) Giả sử $(8,r-23)$ là thùng cũ nhất và là thùng cỡ 8 duy nhất. Mô tả điều xảy ra với các thùng.
- (b) Mô tả các thùng khi trước $(8,r-23)$ còn một thùng cỡ 8 và thùng này chưa hết hạn.
:::

::: hint
Trạng thái của Hình 4.3 là kết quả của Ví dụ 09.16. Áp Thuật toán 09.47 ba lần.
:::

::: solution
**Câu (a).** Đặt $r$ là vị trí bit mới nhất của Hình 4.3. Giả sử ba bit 1 đến ở $r+1$, $r+2$, $r+3$; nếu xen bit 0, chỉ các mốc đổi.

1. **Bit ở $r+1$.** Tạo $(1,r+1)$; hai thùng cỡ 1, không gộp. Kích thước: $8,4,4,2,2,1,1$.
2. **Bit ở $r+2$.** Tạo $(1,r+2)$; ba thùng cỡ 1 nên gộp $(1,r)$ và $(1,r+1)$ thành $(2,r+1)$. Ba thùng cỡ 2 ($r-5$, $r-2$, $r+1$) nên gộp hai thùng cũ nhất thành $(4,r-2)$. Ba thùng cỡ 4 ($r-15$, $r-9$, $r-2$) nên gộp hai thùng cũ nhất thành $(8,r-9)$. Nay có hai thùng cỡ 8, mốc $r-23$ và $r-9$. Kích thước: $8,8,4,2,1$.
3. **Bit ở $r+3$.** Tạo $(1,r+3)$; hai thùng cỡ 1, không gộp. Trạng thái cuối: $(8,r-23)$, $(8,r-9)$, $(4,r-2)$, $(2,r+1)$, $(1,r+2)$, $(1,r+3)$.

**Câu (b).** Bit ở $r+1$ và các lượt gộp ở cỡ 1, 2, 4 khi bit ở $r+2$ đến giống câu (a). Sau khi tạo $(8,r-9)$ có ba thùng cỡ 8, nên bước 4 của Thuật toán 09.47 gộp hai thùng cỡ 8 cũ nhất thành $(16,r-23)$, rồi áp tiếp bước 4 cho cỡ 16: nếu khi đó có ba thùng cỡ 16 thì gộp hai thùng cũ nhất, và cứ thế ở các cỡ lớn hơn. Bit ở $r+3$ giống câu (a). Phần nhìn thấy của trạng thái cuối là $(16,r-23)$, $(8,r-9)$, $(4,r-2)$, $(2,r+1)$, $(1,r+2)$, $(1,r+3)$.

**Kiểm tra lại.** Ở (a), phần nhìn thấy ngoài thùng cỡ 8 cũ có $4+4+2+2+1=13$ bit 1; thêm 3 thành $16=8+4+2+1+1$. Ở (b), thùng $(16,r-23)$ chứa 8 bit 1 của $(8,r-23)$ và 8 bit 1 của thùng cỡ 8 cũ hơn; phần còn lại vẫn là $8+4+2+1+1=16$.
:::

::: exercise Bài tập 09.19 (Các cách chia một dòng bit thành thùng; Bài 4.6.2, MMDS §4.6.8, tr.157)
Dòng bit $1001011011101$, đánh số vị trí từ 1 (cũ nhất, bên trái) tới 13 (mới nhất, bên phải), nằm trọn trong cửa sổ. Xác định mọi cách chia dòng này thành thùng thỏa sáu quy tắc của Định nghĩa 09.42.
:::

::: hint
Xác định trước kích thước các thùng từ số bit 1 và quy tắc 4–6, rồi xét các bit 0 nằm giữa hai thùng.
:::

::: solution
**Kích thước các thùng.** Dòng có 8 bit 1, ở các vị trí 1, 4, 6, 7, 9, 10, 11, 13. Theo quy tắc 4 và 5, nếu kích thước lớn nhất là $2^J$ thì mỗi kích thước $2^j$, $0\le j\le J$, có $n_j\in\{1,2\}$ thùng, và $\sum_jn_j2^j=8$. Với $J\le1$, tổng không quá $2+4=6$; với $J\ge3$, tổng ít nhất $1+2+4+8=15$. Với $J=2$, phương trình $n_0+2n_1+4n_2=8$ chỉ có nghiệm $n_0=2$, $n_1=n_2=1$. Theo quy tắc 6 và Nhận xét 09.43, đi từ mới về cũ các thùng có kích thước $1,1,2,4$ và lần lượt chứa các bit 1 ở vị trí $\{13\}$, $\{11\}$, $\{9,10\}$, $\{1,4,6,7\}$.

**Các đoạn.** Mỗi thùng là một đoạn liên tục kết thúc ở bit 1 (quy tắc 1) và không chứa bit 1 của thùng khác (quy tắc 3). Do đó thùng cỡ 4 là đoạn $[1,7]$, chứa cả các bit 0 ở vị trí 2, 3, 5; thùng $\{11\}$ là đoạn $[11,11]$. Bit 0 ở vị trí 8 có thể thuộc thùng $\{9,10\}$ hoặc không thuộc thùng nào; bit 0 ở vị trí 12 có thể thuộc thùng $\{13\}$ hoặc không thuộc thùng nào. Vậy có $2\cdot2=4$ cách chia, viết từ cũ sang mới, mỗi ngoặc là một thùng và bit 0 ngoài ngoặc không thuộc thùng nào:

- $(1001011)\,0\,(11)\,(1)\,0\,(1)$;
- $(1001011)\,0\,(11)\,(1)\,(01)$;
- $(1001011)\,(011)\,(1)\,0\,(1)$;
- $(1001011)\,(011)\,(1)\,(01)$.

Cả bốn cách có cùng các mốc phải 7, 10, 11, 13 và cùng kích thước, nên cho cùng một biểu diễn DGIM.

**Kiểm tra lại.** $4+2+1+1=8$, bằng số bit 1 của dòng.
:::

## Mức vận dụng

::: exercise Bài tập 09.17 (Chọn hàm băm $\alpha x+\beta\bmod2^L$; Bài 4.4.2, MMDS §4.4.5, tr.145)
Dòng $3,1,4,1,5,9,2,6,5$ được băm bằng ba hàm $h(x)=2x+1\bmod32$, $h(x)=3x+7\bmod32$ và $h(x)=4x\bmod32$ của họ $h(x)=\alpha x+\beta\bmod2^L$ với $L=5$ (MMDS viết $ax+b\bmod2^k$); độ dài đuôi và ước lượng $2^R$ của ba hàm có ở Bài tập 09.11.

- (a) Chỉ ra vấn đề của ba hàm, khi $\alpha$ chẵn và khi $\alpha$ lẻ.
- (b) Nêu lời khuyên cho người định dùng hàm băm của họ này.
:::

::: hint
(a) Xét bit thấp của $\alpha x$ khi $\alpha$ chẵn, rồi khi $\alpha$ lẻ, và so với giả thiết của Định lý 09.10.
:::

::: solution
**Câu (a).** *Khi $\alpha$ chẵn.* Nếu $\alpha=2^{\sigma}\alpha'$ với $\alpha'$ lẻ và $\sigma\ge1$, thì $\sigma$ bit thấp của $h(x)$ bằng $\sigma$ bit thấp của $\beta$ với mọi $x$. Nếu $2^\sigma\nmid\beta$, mọi phần tử có cùng độ dài đuôi nhỏ hơn $\sigma$: hàm $2x+1$ có $\sigma=1$, $\beta=1$, nên ước lượng luôn là 1. Nếu $2^\sigma\mid\beta$, mọi đuôi ít nhất $\sigma$: hàm $4x$ có $\sigma=2$, $\beta=0$, nên ước lượng ít nhất 4 với mọi dòng; hàm này còn không đơn ánh, vì $h(9)=36\bmod32=4=h(1)$. Cả hai không thỏa giả thiết $h(u)$ đều của Bổ đề 09.9.

*Khi $\alpha$ lẻ.* Khi đó $x\mapsto\alpha x+\beta\bmod2^L$ là song ánh, nên các phần tử phân biệt có giá trị băm phân biệt. Với $\alpha$ cố định, hiệu $h(x)-h(x')=\alpha(x-x')\bmod 2^L$ không phụ thuộc $\beta$, nên các giá trị băm không độc lập; mức sai của ước lượng phụ thuộc cấu trúc bit thấp của dữ liệu. Ví dụ, với $L=5$, nếu mọi phần tử của dòng là bội của 4 thì $\alpha x$ là bội của 4, nên mọi $h(x)$ có cùng 2 bit thấp, bằng 2 bit thấp của $\beta$; khi $\beta\bmod4\ne0$, mọi đuôi không quá 1 và ước lượng không vượt $2^1=2$.

**Câu (b).** Chọn $\alpha$ lẻ, vì $\alpha$ chẵn cố định các bit thấp (câu (a)), và chọn $L$ sao cho $2^L$ lớn hơn cỡ tập vũ trụ (MMDS §4.4.2, tr.143).

**Kiểm tra lại.** Với $\alpha=3$, $\beta=7$, bảy phần tử phân biệt $1,2,3,4,5,6,9$ có giá trị băm $10,13,16,19,22,25,2$, đôi một khác nhau, đúng tính song ánh khi $\alpha$ lẻ.
:::

::: exercise Bài tập 09.18 (Số bất ngờ nhỏ nhất và lớn nhất; Bài 4.5.2, MMDS §4.5.6, tr.150)
Một dòng có $r$ phần tử, trong đó $d$ phần tử phân biệt, $1\le d\le r$.

- (a) Xác định số bất ngờ $F_2$ lớn nhất theo $d$ và $r$.
- (b) Xác định số bất ngờ $F_2$ nhỏ nhất theo $d$ và $r$.
- (c) Kiểm hai công thức với $r=100$, $d=11$ và với $r=15$, $d=4$.
:::

::: hint
Mỗi phần tử phân biệt xuất hiện ít nhất một lần. So $F_2$ trước và sau khi chuyển một lần xuất hiện từ phần tử này sang phần tử khác.
:::

::: solution
Chuyển một lần xuất hiện từ phần tử có tần suất $\phi$ sang phần tử có tần suất $\psi$ đổi $F_2$ một lượng $(\phi-1)^2+(\psi+1)^2-\phi^2-\psi^2=2(\psi-\phi)+2$.

**Câu (a).** Nếu $\psi\ge\phi\ge2$, phép chuyển làm $F_2$ tăng và vẫn giữ $d$ phần tử phân biệt. Chọn $\psi$ là tần suất lớn nhất; tần suất này tăng mỗi lần và bị chặn bởi $r-d+1$, nên phép lặp dừng. Khi dừng, nhiều nhất một phần tử có tần suất lớn hơn 1, và tần suất đó bằng $r-(d-1)$. Do đó $F_2^{\max}=(r-d+1)^2+(d-1)$.

**Câu (b).** Nếu $\phi\ge\psi+2$, phép chuyển làm $F_2$ giảm $2(\phi-\psi-1)>0$. Do đó ở cực tiểu, mọi tần suất hơn kém nhau nhiều nhất 1, tức thuộc $\{k,k+1\}$ với $k$ là tần suất nhỏ nhất và $j$ phần tử có tần suất $k+1$, $0\le j<d$. Khi đó $r=kd+j$, nên theo phép chia có dư $r=Qd+Q'$, $0\le Q'<d$, ta có $k=Q$ và $j=Q'$: $Q'$ phần tử xuất hiện $Q+1$ lần, $d-Q'$ phần tử xuất hiện $Q$ lần. Do đó $F_2^{\min}=Q'(Q+1)^2+(d-Q')Q^2$.

**Câu (c).** Với $r=100$, $d=11$: $Q=9$, $Q'=1$, $F_2^{\min}=100+10\cdot81=910$ và $F_2^{\max}=90^2+10=8\,110$, khớp Ví dụ 09.2. Với $r=15$, $d=4$: $Q=3$, $Q'=3$, $F_2^{\min}=3\cdot16+9=57$ và $F_2^{\max}=12^2+3=147$.

**Kiểm tra lại.** Dòng mười lăm phần tử của Ví dụ 09.1 có $r=15$, $d=4$ và $F_2=59$, nằm giữa 57 và 147. Ở hai trường hợp biên, hai công thức trùng nhau: với $d=1$ cả hai bằng $r^2$, với $d=r$ cả hai bằng $r$.
:::

::: exercise Bài tập 09.21 (Nâng xác suất của một ước lượng; Bài 6.6, BHK §6.6, tr.204)
Một thuật toán dùng một hàm băm ngẫu nhiên và cho ước lượng $\hat x$ của giá trị thật $x\ge0$. Với xác suất ít nhất $0{,}6$ theo phép chọn hàm băm, $x/4\le\hat x\le4x$.

- (a) Xây dựng từ nhiều lần chạy một ước lượng thỏa $x/4\le\hat x\le4x$ với xác suất ít nhất $0{,}8$.
- (b) Xác định số lần chạy lẻ nhỏ nhất mà phép phân tích ở câu (a) bảo đảm được xác suất $0{,}8$.
:::

::: hint
(a) Không biết phương sai của $\hat x$ nên lấy trung bình nhiều lần chạy có thể không giúp; cần một hàm khác của nhiều lần chạy.
:::

::: solution
**Câu (a).** Chạy thuật toán $q$ lần, $q$ lẻ, mỗi lần với một hàm băm chọn độc lập, cho $\hat x_1,\ldots,\hat x_q$, rồi trả trung vị $M$ của chúng. Đặt $G=[x/4,4x]$, một khoảng; mỗi $\hat x_\gamma$ nằm ngoài $G$ với xác suất $\eta\le0{,}4$, độc lập với nhau. Theo Bước 1 của chứng minh Bổ đề 09.14, nếu $M\notin G$ thì ít nhất $(q+1)/2$ giá trị nằm ngoài $G$. Cận $(4\eta)^{q/2}$ của bổ đề chỉ có nội dung khi $\eta<1/4$; ở đây $4\eta$ có thể bằng $1{,}6$, nên ta tính trực tiếp. Gọi $\eta_\gamma\le0{,}4$ là xác suất thất bại của lần chạy $\gamma$. Nâng $\eta_\gamma$ lên $0{,}4$ chỉ thêm kết cục thất bại cho lần chạy đó, nên biến cố "ít nhất $(q+1)/2$ lần thất bại" không thu hẹp; do đó
$$
\Pr[M\notin G]\le\sum_{k=(q+1)/2}^{q}\binom qk0{,}4^k\,0{,}6^{q-k}.
$$

**Câu (b).** Vế phải bằng $0{,}4$ khi $q=1$, khoảng $0{,}352$ khi $q=3$, $0{,}2131$ khi $q=15$ và $0{,}1989$ khi $q=17$. Với $q=17$, các số hạng $k=9,10,11,12$ lần lượt khoảng $0{,}1070$, $0{,}0571$, $0{,}0242$, $0{,}0081$, và các số hạng $k=13,\ldots,17$ có tổng khoảng $0{,}0025$. Vậy $q=17$ là số lẻ nhỏ nhất cho $\Pr[M\in G]\ge1-0{,}1989>0{,}8$.

**Kiểm tra lại.** Với $q=1$, xác suất thành công $0{,}6$ đúng bằng dữ kiện; với $q=15$, xác suất thành công khoảng $0{,}787<0{,}8$.
:::
