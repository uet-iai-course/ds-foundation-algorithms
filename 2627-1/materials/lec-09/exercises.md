# Bài tập Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Các bài tập củng cố 09.10–09.19 dưới đây có gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 09.k là của [ghi chú Bài 09](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-dong-du-lieu-dem-momen-va-cua-so.html), nơi Bài tập 09.1–09.9 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Năm bài sách 09.10, 09.11, 09.12, 09.15 và 09.16, tức các bài 4.5.1, 4.4.1, 4.5.3, 4.6.1, 4.6.3 của MMDS, là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 09](lecture-09-dong-du-lieu-dem-momen-va-cua-so.html).

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả các đại lượng trên dòng và chọn phác thảo theo đại lượng, bảo đảm và chi phí (Mục 1, Mục 7) | 09.1, 09.9 | 09.10, 09.18 |
| 2. Chạy Flajolet–Martin; cận hai phía của $2^R$ và cận thất bại của trung vị (Mục 2) | 09.2, 09.3 | 09.11, 09.17 |
| 3. Chạy biến Alon–Matias–Szegedy; $\mathbb E[X]=F_2$, dạng tổng quát cho $F_p$, lấy mẫu hồ chứa (Mục 3) | 09.4, 09.5 | 09.12, 09.13, 09.14 |
| 4. Cập nhật và truy vấn Count-Min Sketch; chọn số ô và số hàng theo $\varepsilon$, $\delta$, $\kappa$ (Mục 4) | 09.6 | — |
| 5. Duy trì và truy vấn biểu diễn DGIM; bộ nhớ $O(\log^2N)$ bit và cận sai số tương đối 50% (Mục 5) | 09.7 | 09.15, 09.16 |
| 6. Cập nhật cửa sổ suy giảm mũ và tìm phần tử phổ biến với ít hơn $1/(c\theta)$ điểm (Mục 6) | 09.8 | 09.19 |

## Mức nhận biết

::: exercise Bài tập 09.10 (Số bất ngờ; Bài 4.5.1, MMDS §4.5.6, tr.149)
Tính số bất ngờ (mômen bậc hai) của dòng $3,1,4,1,3,4,2,1,2$. Mômen bậc ba của dòng này bằng bao nhiêu?
:::

::: hint
Lập bảng tần suất rồi áp Định nghĩa 09.1.
:::

::: solution
Tần suất: $f_1=3$ (vị trí 2, 4, 8), $f_2=2$ (7, 9), $f_3=2$ (1, 5), $f_4=2$ (3, 6). Do đó $F_2=9+4+4+4=21$ và $F_3=27+8+8+8=51$.

**Kiểm tra lại.** $3+2+2+2=9$, bằng độ dài dòng.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 09.11 (Ba hàm băm; Bài 4.4.1, MMDS §4.4.5, tr.145)
Dòng gồm các số nguyên $3,1,4,1,5,9,2,6,5$. Các hàm băm có dạng $h(x)=\alpha x+\beta\bmod32$, kết quả coi như số nhị phân 5 bit. Xác định độ dài đuôi của mỗi phần tử và ước lượng số phần tử phân biệt khi hàm băm là (a) $h(x)=2x+1\bmod32$; (b) $h(x)=3x+7\bmod32$; (c) $h(x)=4x\bmod32$.
:::

::: hint
Tính $h(x)$, viết 5 bit, đếm số bit 0 ở cuối; $R$ là số lớn nhất; ước lượng $2^R$ (Thuật toán 09.6).
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

(a) $R=0$, ước lượng $1$. (b) $R=4$, ước lượng $16$. (c) $R=4$, ước lượng $16$. Dòng có 7 phần tử phân biệt $\{1,2,3,4,5,6,9\}$, nên cả ba ước lượng đều sai xa. Ở (c), $h(9)=36\bmod32=4=h(1)$, nên hàm không đơn ánh.

**Kiểm tra lại.** $3\cdot3+7=16=10000_2$; $4\cdot4=16$.
:::

::: exercise Bài tập 09.12 (Giá trị các biến AMS; Bài 4.5.3, MMDS §4.5.6, tr.150)
Áp thuật toán AMS cho dòng $3,1,4,1,3,4,2,1,2$ của Bài tập 09.10 để ước lượng số bất ngờ. Với mỗi vị trí $i$, biến AMS bắt đầu ở vị trí $i$ có bộ đếm bằng bao nhiêu khi dòng kết thúc, và cho ước lượng nào?
:::

::: hint
Bộ đếm của biến bắt đầu ở $i$ là $v_i$ của Định nghĩa 09.19.
:::

::: solution
| $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $x_i$ | 3 | 1 | 4 | 1 | 3 | 4 | 2 | 1 | 2 |
| $v_i$ | 2 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 1 |
| $9(2v_i-1)$ | 27 | 45 | 27 | 27 | 9 | 9 | 27 | 9 | 9 |

**Kiểm tra lại.** Tổng các ước lượng là 189, trung bình $189/9=21=F_2$, đúng Định lý 09.22.
:::

::: exercise Bài tập 09.13 (Mômen bậc ba; Bài 4.5.4, MMDS §4.5.6, tr.150)
Lặp lại Bài tập 09.12 khi các biến dùng để ước lượng mômen bậc ba. Giá trị mỗi biến khi dòng kết thúc là bao nhiêu? Mỗi biến cho ước lượng nào? Trung bình các ước lượng so với mômen bậc ba thật thế nào?
:::

::: hint
Giá trị biến không đổi; chỉ phép trả lời đổi thành $r(3v^2-3v+1)$ (Hệ quả 09.23).
:::

::: solution
Giá trị các biến vẫn là $2,3,2,2,1,1,2,1,1$. Với $r=9$: $v=1\mapsto9$, $v=2\mapsto9\cdot7=63$, $v=3\mapsto9\cdot19=171$. Các ước lượng theo vị trí: $63,171,63,63,9,9,63,9,9$, tổng 459, trung bình $51$, đúng bằng $F_3=51$ của Bài tập 09.10, vì trung bình trên mọi vị trí là kỳ vọng với $I$ đều.
:::

::: exercise Bài tập 09.14 (Tổng các số lẻ và mômen bậc bốn; Bài 4.5.5 và 4.5.6, MMDS §4.5.6, tr.150)
- (a) Chứng minh bằng quy nạp theo $f$ rằng $1+3+5+\cdots+(2f-1)=f^2$.
- (b) Muốn ước lượng mômen bậc bốn, phải đổi giá trị biến thành ước lượng như thế nào?
:::

::: hint
(a) Bổ đề 09.21. (b) Hệ quả 09.23 với $p=4$.
:::

::: solution
(a) Cơ sở $f=1$: $1=1^2$. Nếu tổng đến $2f-1$ bằng $f^2$, thì cộng thêm $2(f+1)-1=2f+1$ được $f^2+2f+1=(f+1)^2$.

(b) Với bộ đếm $v$, ước lượng là $r\bigl(v^4-(v-1)^4\bigr)=r(4v^3-6v^2+4v-1)$; nó không chệch vì $\sum_{v=1}^{f}\bigl(v^4-(v-1)^4\bigr)=f^4$ (tổng lồng nhau).
:::

::: exercise Bài tập 09.15 (Truy vấn trên Hình 4.2; Bài 4.6.1, MMDS §4.6.8, tr.157)
Cửa sổ như MMDS Hình 4.2, tức trạng thái của Ví dụ 09.14: các thùng (kích thước, mốc phải) $(1,r-1)$, $(1,r-2)$, $(2,r-4)$, $(4,r-8)$, $(4,r-14)$, $(8,r-22)$; hai mươi lăm bit cuối $1011011000101110110010110$. Ước lượng số bit 1 trong $k$ vị trí cuối với (a) $k=5$, (b) $k=15$. Mỗi ước lượng lệch bao nhiêu so với giá trị đúng?
:::

::: hint
Tìm $b^*$, thùng cũ nhất có mốc phải $\ge r-k+1$ (Thuật toán 09.45).
:::

::: solution
(a) $k=5$: các vị trí $r-4,\ldots,r$ là $10110$, có 3 bit 1. $b^*=(2,r-4)$; $T=1+1=2$; $\widehat y_5=2+2/2=3$. Đúng, sai lệch 0.

(b) $k=15$: các vị trí $r-14,\ldots,r$ là $101110110010110$, có 9 bit 1 ở $r-14$, $r-12$, $r-11$, $r-10$, $r-8$, $r-7$, $r-4$, $r-2$, $r-1$. $b^*=(4,r-14)$, chỉ mốc phải của nó trong hậu tố; $T=1+1+2+4=8$; $\widehat y_{15}=8+4/2=10$. Thừa 1, sai số tương đối $1/9\approx11\%$.

**Kiểm tra lại.** Cả hai sai số nằm trong cận 50% của Định lý 09.46; (b) là trường hợp ước lượng cao với $\pi=1$.
:::

::: exercise Bài tập 09.16 (Ba bit 1 nữa trên Hình 4.3; Bài 4.6.3, MMDS §4.6.8, tr.157)
Mô tả điều xảy ra với các thùng nếu ba bit 1 nữa đi vào cửa sổ biểu diễn ở MMDS Hình 4.3, tức các thùng (kích thước, mốc phải) từ cũ sang mới $(8,r-23)$, $(4,r-15)$, $(4,r-9)$, $(2,r-5)$, $(2,r-2)$, $(1,r)$. Có thể giả sử không bit 1 nào trong hình rời cửa sổ.
:::

::: hint
Trạng thái của Hình 4.3 là kết quả của Ví dụ 09.16. Áp Thuật toán 09.47 ba lần.
:::

::: solution
Đặt $r$ là vị trí bit mới nhất của Hình 4.3. Trạng thái đầu (kích thước, mốc phải), từ cũ sang mới: $(8,r-23)$, $(4,r-15)$, $(4,r-9)$, $(2,r-5)$, $(2,r-2)$, $(1,r)$. Giả sử ba bit 1 đến ở $r+1$, $r+2$, $r+3$; nếu xen bit 0, chỉ các mốc đổi.

1. **Bit ở $r+1$.** Tạo $(1,r+1)$; hai thùng cỡ 1, không gộp. Kích thước: $8,4,4,2,2,1,1$.
2. **Bit ở $r+2$.** Tạo $(1,r+2)$; ba thùng cỡ 1 nên gộp $(1,r)$ và $(1,r+1)$ thành $(2,r+1)$. Ba thùng cỡ 2 ($r-5$, $r-2$, $r+1$) nên gộp hai thùng cũ nhất thành $(4,r-2)$. Ba thùng cỡ 4 ($r-15$, $r-9$, $r-2$) nên gộp hai thùng cũ nhất thành $(8,r-9)$. Nay có hai thùng cỡ 8, mốc $r-23$ và $r-9$. Kích thước: $8,8,4,2,1$.
3. **Bit ở $r+3$.** Tạo $(1,r+3)$; hai thùng cỡ 1, không gộp. Trạng thái cuối: $(8,r-23)$, $(8,r-9)$, $(4,r-2)$, $(2,r+1)$, $(1,r+2)$, $(1,r+3)$.

Nhánh điều kiện: Hình 4.3 ghi "có ít nhất một thùng cỡ 8". Nếu phần không vẽ đã có thêm một thùng cỡ 8, thì ở bước 2 có ba thùng cỡ 8, hai thùng cũ nhất được gộp thành một thùng cỡ 16, và dây chuyền có thể lan tiếp tới các kích thước lớn hơn.

**Kiểm tra lại.** Phần nhìn thấy ngoài thùng cỡ 8 cũ có $4+4+2+2+1=13$ bit 1; thêm 3 thành $16=8+4+2+1+1$.
:::

## Mức vận dụng

::: exercise Bài tập 09.17 (Chọn hàm băm dạng $\alpha x+\beta\bmod2^L$; Bài 4.4.2, MMDS §4.4.5, tr.145)
Các hàm băm ở Bài tập 09.11 có vấn đề gì? Lời khuyên nào cho người định dùng hàm băm dạng $h(x)=\alpha x+\beta\bmod2^L$ (MMDS viết $ax+b\bmod2^k$)?
:::

::: hint
Xét bit thấp của $\alpha x$ khi $\alpha$ chẵn, rồi khi $\alpha$ lẻ, và so với giả thiết của Định lý 09.10.
:::

::: solution
**$\alpha$ chẵn.** Nếu $\alpha=2^{\sigma}\alpha'$ với $\alpha'$ lẻ và $\sigma\ge1$, thì $\sigma$ bit thấp của $h(x)$ bằng $\sigma$ bit thấp của $\beta$ với mọi $x$. Nếu $2^\sigma\nmid\beta$, mọi phần tử có cùng độ dài đuôi nhỏ hơn $\sigma$: câu (a) có $\sigma=1$, $\beta=1$, ước lượng luôn là 1. Nếu $2^\sigma\mid\beta$, mọi đuôi ít nhất $\sigma$: câu (c) có $\sigma=2$, $\beta=0$, ước lượng ít nhất 4 với mọi dòng. Cả hai vi phạm $\Pr[\rho\ge\ell]=2^{-\ell}$ của Bổ đề 09.9.

**$\alpha$ lẻ.** Khi đó $x\mapsto\alpha x+\beta\bmod2^L$ là song ánh, nên các phần tử phân biệt có giá trị băm phân biệt; nhưng điều đó chưa đủ. Vì $\alpha$ khả nghịch modulo $2^L$, $\alpha x+\beta\equiv\alpha(x+\tilde\beta)$ với $\tilde\beta=\alpha^{-1}\beta$, và nhân với số lẻ không đổi số bit 0 ở cuối, nên $\rho(h(x))=\rho((x+\tilde\beta)\bmod2^L)$. Hai phần tử cùng số dư theo $2^j$ có cùng độ dài đuôi khi độ dài này nhỏ hơn $j$, nên giả thiết độc lập của Định lý 09.10 không thỏa trên dữ liệu có cấu trúc: ví dụ, nếu mọi phần tử của dòng là bội của $1\,024$, mọi giá trị băm có cùng 10 bit thấp, nên với xác suất $1-2^{-10}$ theo phép chọn $\beta$, mọi phần tử có cùng độ dài đuôi nhỏ hơn 10 và ước lượng không vượt $2^9=512$ dù $d$ lớn.

**Lời khuyên.** Chọn $\alpha$ lẻ và $2^L$ vượt cỡ tập vũ trụ (MMDS tr.143); dù vậy, họ này chỉ xấp xỉ mô hình băm lý tưởng khi dữ liệu không có cấu trúc theo các bit thấp.
:::

::: exercise Bài tập 09.18 (Số bất ngờ nhỏ nhất và lớn nhất; Bài 4.5.2, MMDS §4.5.6, tr.150)
Một dòng có $r$ phần tử, trong đó $d$ phần tử phân biệt. Số bất ngờ nhỏ nhất và lớn nhất có thể là bao nhiêu, theo $d$ và $r$? Kiểm với Ví dụ 09.2 và với dòng mười lăm phần tử.
:::

::: hint
Mỗi phần tử phân biệt xuất hiện ít nhất một lần. So $F_2$ trước và sau khi chuyển một lần xuất hiện từ phần tử này sang phần tử khác.
:::

::: solution
**Phép chuyển.** Chuyển một lần xuất hiện từ phần tử có tần suất $\phi$ sang phần tử có tần suất $\psi$ đổi $F_2$ một lượng $(\phi-1)^2+(\psi+1)^2-\phi^2-\psi^2=2(\psi-\phi)+2$.

**Lớn nhất.** Nếu $\psi\ge\phi\ge2$, phép chuyển làm $F_2$ tăng, và vẫn giữ $d$ phần tử phân biệt. Lặp lại tới khi mọi phần tử trừ một có tần suất 1: $F_2^{\max}=(r-d+1)^2+(d-1)$.

**Nhỏ nhất.** Nếu $\phi\ge\psi+2$, phép chuyển làm $F_2$ giảm $2(\phi-\psi-1)>0$. Do đó ở cực tiểu, mọi tần suất hơn kém nhau nhiều nhất 1. Viết $r=Qd+Q'$ với $0\le Q'<d$: $Q'$ phần tử xuất hiện $Q+1$ lần, $d-Q'$ phần tử $Q$ lần, và $F_2^{\min}=Q'(Q+1)^2+(d-Q')Q^2$.

**Kiểm tra lại.** $r=100$, $d=11$: $Q=9$, $Q'=1$, $F_2^{\min}=100+10\cdot81=910$, $F_2^{\max}=90^2+10=8\,110$, khớp Ví dụ 09.2. $r=15$, $d=4$: $Q=3$, $Q'=3$, $F_2^{\min}=3\cdot16+9=57$, $F_2^{\max}=12^2+3=147$, và $57\le59\le147$.
:::

::: exercise Bài tập 09.19 (Vì sao ngưỡng không bằng 1 hay 2)
Trong Thuật toán 09.55, vì sao không chọn ngưỡng $\theta=1$ hay $\theta=2$? Với $c=1/2$, chạy năm phần tử đầu $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d$ với $\theta=1$ và cho biết phần tử nào còn được theo dõi sau bước 5.
:::

::: hint
Điểm của phần tử vừa tạo bằng 1; xem Bước 4 của chứng minh Định lý 09.56.
:::

::: solution
Với $\theta=2$, phần tử mới bị xóa ngay. Với $\theta=1$, nó bị xóa ở bước kế tiếp, khi điểm thành $1-c<1$, trừ khi xuất hiện lại ngay. Trên năm phần tử với $c=1/2$: bước 1 giữ $\mathrm a:1$; bước 2 xóa $\mathrm a$ ($1/2$), giữ $\mathrm b:1$; bước 3 xóa $\mathrm b$, giữ $\mathrm c:1$; bước 4 xóa $\mathrm c$, tạo lại $\mathrm b:1$; bước 5 xóa $\mathrm b$, giữ $\mathrm d:1$. Sau bước 5 chỉ còn $\mathrm d$, phần tử vừa đến: thuật toán chỉ nhớ phần tử cuối cùng.
:::
