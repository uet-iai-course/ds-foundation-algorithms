# Ghi chú Bài 03 — PageRank: mô hình và tính toán

Bài giảng tương ứng: [PageRank — mô hình và tính toán](lecture-03-pagerank-mo-hinh-va-tinh-toan.html). Ghi chú dựa trên Chương 5 của giáo trình [Mining of Massive Datasets](http://www.mmds.org) (MMDS). Các bổ sung về phép co và cận dừng được chứng minh trực tiếp từ đặc tả PageRank.

## 1. Động lực: xếp hạng theo đồ thị liên kết

Kho metadata của các trang Web không vừa bộ nhớ của một máy. Cần tính trước một thứ hạng dựa trên cấu trúc liên kết và cập nhật nó mà không dựng ma trận đặc. Bài 02 đã cung cấp mô hình MapReduce cho dữ liệu vượt bộ nhớ; bài này dùng lại mô hình đó để thực hiện phép lặp PageRank trên đồ thị thưa.

## 2. Đặc tả đồ thị và người lướt ngẫu nhiên

Cho đồ thị có hướng $G=(V,E)$, với $n=|V|$ trang và $m=|E|$ cạnh. Cạnh $j\to i$ nghĩa là trang $j$ trỏ tới trang $i$. Ký hiệu $N^+(j)=\{i:(j,i)\in E\}$ là tập đích của $j$, $d^+(j)=|N^+(j)|$ là bậc ra, và $N^-(i)=\{j:(j,i)\in E\}$ là tập nguồn trỏ tới $i$. Các liên kết lặp giữa cùng hai trang được gộp thành một; vòng tự nối được phép.

Một **người lướt ngẫu nhiên** bắt đầu ở một trang bất kỳ và lặp lại bước: tại trang $j$, chọn đều một trong $d^+(j)$ liên kết đi. Do đó $j$ đóng góp khối lượng $r_j/d^+(j)$ cho mỗi đích. Khi các điều kiện hội tụ ở Mục 5 được thỏa, phân phối vị trí tiến tới vector **PageRank** $r$.

Phân phối ổn định thỏa phương trình cân bằng, cho mọi trang $i$:

$$r_i=\sum_{j\in N^-(i)}\frac{r_j}{d^+(j)},$$

kèm điều kiện chuẩn hóa $\sum_i r_i=1$. Đặt ma trận chuyển theo cột $P$ với $P_{ij}=1/d^+(j)$ nếu $j\to i$, và $P_{ij}=0$ nếu không. Khi đó $r=Pr$. Cập nhật $r^{(t+1)}=P\,r^{(t)}$ là **phép lặp lũy thừa** (power iteration).

### Ví dụ cơ sở ba nút $y,a,m$

Xét đồ thị ba nút $y,a,m$ (gợi nhớ Yahoo, Amazon, Microsoft) với các cạnh $y\to y$, $y\to a$, $a\to y$, $a\to m$, $m\to a$. Bậc ra là $d^+(y)=2$, $d^+(a)=2$, $d^+(m)=1$. Ma trận chuyển cột và nghiệm của biến thể cơ sở là:

$$P=\begin{bmatrix}1/2&1/2&0\\1/2&0&1\\0&1/2&0\end{bmatrix},\qquad
r^*=\begin{bmatrix}2/5&2/5&1/5\end{bmatrix}^{T}.$$

::: derivation
Cột $y$ nhận $1/2$ tại $y$ và $1/2$ tại $a$ (vì $y$ trỏ $y,a$); cột $a$ nhận $1/2$ tại $y$ và $1/2$ tại $m$ (vì $a$ trỏ $y,m$); cột $m$ nhận $1$ tại $a$ (vì $m$ chỉ trỏ $a$). Phương trình cân bằng:

$$r_y=\frac12 r_y+\frac12 r_a,\qquad r_a=\frac12 r_y+r_m,\qquad r_m=\frac12 r_a.$$

Từ phương trình thứ ba có $r_a=2r_m$. Thay vào phương trình đầu được $r_y=r_a$, thay vào phương trình thứ hai cũng được $r_y=r_a$ (nhất quán). Dùng tổng $r_y+r_a+r_m=2r_m+2r_m+r_m=5r_m=1$, ta có $r_m=1/5$, $r_a=2/5$, $r_y=2/5$, khớp với $r^*$.
:::

Đồ thị ba nút được dùng dưới ba dạng: cơ sở, nút cụt ở Mục 3 và bẫy nhện ở Mục 4. Mỗi dạng có một ma trận và nghiệm riêng.

**Tự kiểm.** Từ $r^{(0)}=(1/3,1/3,1/3)^T$, hãy tính $r^{(1)}$ theo hai cách: cộng đóng góp trên cạnh và nhân $P r^{(0)}$.

## 3. Biến thể nút cụt và sửa lại cột

Một trang không có liên kết đi, gọi là **nút cụt** (dead end), nhận khối lượng nhưng không phân phối nó ở bước sau. Tổng xác suất vì thế giảm dưới $1$ và không còn là một phân phối. Xét biến thể nút cụt của đồ thị ba nút: bỏ cạnh $m\to a$, khi đó $d^+(m)=0$ và cột $m$ của ma trận chuyển bằng toàn không.

::: derivation
Bắt đầu từ vector đều $r^{(0)}=(1/3,1/3,1/3)^T$ với cột $m$ bằng $0$, bước đầu là

$$r^{(1)}=P\,r^{(0)}=\begin{bmatrix}1/2&1/2&0\\1/2&0&0\\0&1/2&0\end{bmatrix}\begin{bmatrix}1/3\\1/3\\1/3\end{bmatrix}=\begin{bmatrix}1/3\\1/6\\1/6\end{bmatrix},$$

có tổng $1/3+1/6+1/6=2/3$. Khối lượng $1/3$ của nút cụt $m$ bị mất ở mỗi bước.
:::

Cách sửa được dùng trong ghi chú là thay cột của mỗi nút cụt bằng phân phối đều $1/n$. Ma trận $\bar P$ thu được là **ngẫu nhiên theo cột**: mỗi cột có tổng bằng $1$. Gọi $P_0$ là toán tử chỉ chứa cạnh thật, $d_j=1$ nếu $j$ là nút cụt và $0$ nếu không, còn $e$ là vector toàn số $1$. Khi đó

$$\bar P=P_0+\frac{e\,d^T}{n}.$$

::: proof
Xét cột $j$ của $\bar P$. Nếu $j$ không là nút cụt thì $d_j=0$, cột của $ed^T/n$ bằng $0$, và cột chính là cột $j$ của $P_0$, có tổng bằng $1$. Nếu $j$ là nút cụt thì $d_j=1$, cột của $ed^T/n$ bằng $(1/n,\dots,1/n)^T$, còn cột $j$ của $P_0$ bằng $0$. Vậy mọi cột của $\bar P$ có tổng bằng $1$, nên phép nhân $\bar P r$ bảo toàn tổng xác suất.
:::

::: derivation
Trên biến thể nút cụt, $P_0$ có cột $m$ bằng $0$ và $d_m=1$. Với vector đều $r^{(0)}=(1/3,1/3,1/3)^T$, khối lượng nút cụt là $d^T r=r_m=1/3$, được phân phối đều $\tfrac13\cdot\tfrac1n=\tfrac19$ cho mỗi nút. Bước sửa kiểm được:

$$\bar P\,r^{(0)}=P_0\,r^{(0)}+\frac{e\,d^T}{n}\,r^{(0)}=\begin{bmatrix}1/3\\1/6\\1/6\end{bmatrix}+\begin{bmatrix}1/9\\1/9\\1/9\end{bmatrix}=\begin{bmatrix}4/9\\5/18\\5/18\end{bmatrix},$$

với $4/9+5/18+5/18=(8+5+5)/18=1$. Khối lượng nút cụt được phân phối lại đúng một lần và tổng không bị mất.
:::

**Tự kiểm.** Nếu hai nút cụt mang tổng hạng $0{,}3$, phép sửa thêm bao nhiêu vào mỗi thành phần khi $n=5$?

## 4. Biến thể bẫy nhện và hệ số giảm $\beta$

Kể cả khi không có nút cụt, một nhóm trang không có cạnh đi ra ngoài, gọi là **bẫy nhện**, có thể giữ toàn bộ khối lượng. Xét biến thể bẫy nhện của đồ thị ba nút: thay $m\to a$ bằng vòng tự nối $m\to m$. Mọi nút đều có bậc ra, nhưng một khi người lướt vào $m$ thì không thể rời nó.

Cách khắc phục là dùng **hệ số giảm** và **dịch chuyển ngẫu nhiên**. Định nghĩa $U=ee^T/n$, ma trận có mọi phần tử bằng $1/n$, và toán tử

$$A_\beta=\beta P+(1-\beta)U,$$

với $0<\beta<1$. Người lướt theo liên kết với xác suất $\beta$; với xác suất $1-\beta$, họ chuyển đều sang một trang bất kỳ. Vì vậy bẫy nhện một nút không thể giữ toàn bộ xác suất.

::: derivation
Với $\beta=0{,}8$ trên biến thể bẫy nhện của đồ thị ba nút, ta có

$$A_{0,8}=\begin{bmatrix}7/15&7/15&1/15\\7/15&1/15&1/15\\1/15&7/15&13/15\end{bmatrix},\qquad
r^*=\begin{bmatrix}7/33&5/33&21/33\end{bmatrix}^{T}.$$

Với ma trận $P$ của biến thể bẫy nhện, hàng thứ ba là $(0,1/2,1)$ và $P_{33}=1$. Do đó $A_{31}=1/15$, $A_{32}=0{,}8\cdot1/2+1/15=7/15$ và $A_{33}=0{,}8\cdot1+1/15=13/15$. Với hàng thứ ba của $A_{0,8}$,

$$\frac1{15}\frac7{33}+\frac7{15}\frac5{33}+\frac{13}{15}\frac{21}{33}=\frac{315}{495}=\frac{21}{33},$$

đúng bằng thành phần thứ ba của $r^*$. Hai hàng còn lại được kiểm tương tự; $7+5+21=33$ nên tổng các thành phần bằng $1$.
:::

::: example
Biến thể cơ sở, với $m\to a$, áp dụng cùng $\beta=0{,}8$ có nghiệm $(35/93,\;37/93,\;21/93)^T$. Biến thể bẫy nhện đổi cạnh ra của $m$, nên không dùng chung ma trận hoặc nghiệm với đồ thị cơ sở.
:::

**Tự kiểm.** Chỉ ra đúng cột thay đổi khi chuyển từ đồ thị cơ sở sang biến thể bẫy nhện, rồi giải thích vì sao hai nghiệm ở trên không thể dùng thay nhau.

## 5. Hội tụ và cận dừng

Ký hiệu đơn hình (simplex) là tập

$$\mathcal S=\{x\in\mathbb R^n:x_i\ge0,\ \sum_i x_i=1\}.$$

Đơn hình này là một tập đóng trong $\mathbb R^n$, vì vậy đầy đủ dưới chuẩn $L_1$. Ta xét hai trường hợp.

### Trường hợp $\beta=1$

Khi $\beta=1$, toán tử là $A_1=P$. Nếu $P$ là **bất khả quy** — từ mọi nút đi tới được mọi nút — và **không chu kỳ**, thì phép lặp lũy thừa hội tụ từ mọi phân phối đầu về nghiệm duy nhất.

::: proof
Xét đồ thị hai nút $c\leftrightarrow d$ và $\beta=1$. Ma trận chuyển là $\begin{bmatrix}0&1\\1&0\end{bmatrix}$, có chu kỳ $2$. Từ $(1,0)^T$, phép lặp đi tới $(0,1)^T$ rồi quay lại $(1,0)^T$. Dãy không hội tụ dù $(1/2,1/2)^T$ là điểm bất động. Vì vậy không thể bỏ điều kiện không chu kỳ khỏi bảo đảm hội tụ từ mọi phân phối đầu.
:::

### Trường hợp $0<\beta<1$

Với $0<\beta<1$, trong biến thể không có nút cụt, cả $P$ và $U$ đều ngẫu nhiên theo cột. Nếu đồ thị có nút cụt thì thay $P$ bằng $\bar P$ đã sửa ở Mục 3. Trong cả hai trường hợp, $A_\beta$ là ma trận ngẫu nhiên theo cột. Với $x,y\in\mathcal S$, vector $z=x-y$ có tổng bằng $0$, nên

$$U(x-y)=\frac{ee^T}{n}(x-y)=\frac{e}{n}\,e^T(x-y)=0,$$

vì $e^T z$ là tổng các thành phần của $z$. Hạng phụ thuộc $1-\beta$ biến mất.

::: proof
Với $x,y\in\mathcal S$, hiệu của toán tử tại hai điểm:

$$A_\beta x-A_\beta y=\beta P(x-y)+(1-\beta)U(x-y)=\beta P(x-y).$$

Lấy chuẩn $L_1$ và dùng việc $P$ ngẫu nhiên theo cột nên $\|Pz\|_1\le\|z\|_1$ với mọi $z$:

$$\|A_\beta x-A_\beta y\|_1=\beta\|P(x-y)\|_1\le\beta\|x-y\|_1.$$

Vậy $A_\beta$ là phép co hệ số $\beta$ trên không gian đầy đủ $\mathcal S$. Theo định lý điểm bất động Banach, tồn tại **duy nhất** điểm bất động $r^*=A_\beta r^*$, và dãy $r^{(t+1)}=A_\beta r^{(t)}$ hội tụ tới $r^*$ từ mọi điểm khởi đầu trong $\mathcal S$.
:::

### Cận dừng hậu nghiệm

Đặt sai lệch liên tiếp tại vòng $t$ là

$$\Delta_t=\|r^{(t)}-r^{(t-1)}\|_1.$$

Từ tính co hệ số $\beta$ ta dựng cận hậu nghiệm (a posteriori):

$$\|r^*-r^{(t)}\|_1\le\frac{\beta}{1-\beta}\,\Delta_t.$$

::: derivation
Với $t\ge2$, tính co cho

$$\Delta_{t+1}=\|A_\beta r^{(t)}-A_\beta r^{(t-1)}\|_1\le\beta\,\Delta_t,$$

nên quy nạp $\Delta_{t+k}\le\beta^k\Delta_t$ với mọi $k\ge0$. Vì $r^{(t+k)}=A_\beta^k r^{(t)}\to r^*$ khi $k\to\infty$, tổng chuỗi hình học cho

$$\|r^*-r^{(t)}\|_1\le\sum_{k\ge1}\Delta_{t+k}\le\Delta_t\sum_{k\ge1}\beta^k=\frac{\beta\Delta_t}{1-\beta}.$$

Hệ số $\beta/(1-\beta)$ tăng nhanh khi $\beta$ tiến tới $1$, phản ánh bảo đảm hội tụ yếu đi. Khi $\beta$ tiến tới $0$, cận tiến tới $0$: phép dịch chuyển đều chi phối và nghiệm đạt được ngay.
:::

Cụ thể, muốn sai số không quá $\varepsilon$ chỉ cần dừng khi

$$\Delta_t\le\tau,\qquad \tau=\frac{(1-\beta)\,\varepsilon}{\beta}.$$

::: proof
Nếu $\Delta_t\le\tau$ thì theo cận trên $\|r^*-r^{(t)}\|_1\le\frac{\beta}{1-\beta}\Delta_t\le\frac{\beta}{1-\beta}\cdot\frac{(1-\beta)\varepsilon}{\beta}=\varepsilon$, đúng điều kiện mong muốn.
:::

**Tự kiểm.** Với $\beta=0{,}8$ và sai số đích $\varepsilon=10^{-4}$, hãy tính ngưỡng phần dư $\tau$.

## 6. Thuật toán PageRank có hệ số giảm

- **Đầu vào.** Tập $V$ gồm $n$ nút, danh sách cạnh $j\to i$ của $E$, hệ số $\beta\in(0,1)$, ngưỡng $\varepsilon>0$. Chọn $K_{\max}\in\mathbb N$ với $K_{\max}\ge1$ là cận số vòng tối đa.
- **Đầu ra.** Vector xấp xỉ $r$ với sai lệch liên tiếp $\|r^{(t)}-r^{(t-1)}\|_1\le\tau$, hoặc thông báo không hội tụ trong hạn ngân sách.
- **Điều kiện trước.** Đồ thị hữu hạn; mỗi $d^+(j)$ được tính sau khi gộp liên kết lặp; $n\ge1$; $\beta\in(0,1)$; $\varepsilon>0$; $K_{\max}\ge1$.
- **Điều kiện sau.** Nếu trả về `đã hội tụ` thì $\|r^{(t)}-r^{(t-1)}\|_1\le\tau$ (kéo theo $\|r^*-r^{(t)}\|_1\le\varepsilon$) và $r$ là một phân phối (tổng $1$). Nếu trả về `hết ngân sách vòng` thì $r$ là xấp xỉ tốt nhất đạt được trước khi hết $K_{\max}$ vòng.
- **Dừng.** Khi $\Delta_t\le\tau$ (trả `đã hội tụ`) hoặc khi đạt vòng $t=K_{\max}$ (trả `hết ngân sách vòng`).
- **Biên.** Với $\beta=1$, nút cụt làm rò khối lượng, còn chu kỳ hoặc bẫy nhện có thể làm phép lặp không hội tụ tới phân phối mong muốn. Bảo đảm của thuật toán này dùng $0<\beta<1$.

**Giả mã.**

```text
r ← (1/n, ..., 1/n)
tau ← (1-beta)*epsilon/beta
cho t từ 1 đến K_max:
    delta_dangling ← 0
    cho mỗi nút j:
        nếu d_plus(j) = 0:
            delta_dangling ← delta_dangling + r[j]
    dong_gop ← (0, ..., 0)
    cho mỗi cạnh j → i:
        dong_gop[i] ← dong_gop[i] + r[j]/d_plus(j)
    cho mỗi nút i:
        r_new[i] ← beta*(dong_gop[i] + delta_dangling/n) + (1-beta)/n
    residual ← ||r_new-r||_1
    nếu residual ≤ tau:
        trả về ("đã hội tụ", r_new)
    r ← r_new
trả về ("hết ngân sách vòng", r)
```

Trong giả mã, `d_plus(j)` biểu diễn $d^+(j)$, `delta_dangling` biểu diễn $\delta=d^T r$, còn `residual` biểu diễn $\Delta_t$.

**Chi phí.** Mỗi vòng duyệt mọi cạnh trong $\Theta(m)$ và thực hiện số lượt tuyến tính trên các nút trong $\Theta(n)$, tổng $\Theta(n+m)$. Cạnh cần $\Theta(m)$ bộ nhớ; vector hạng và bản ghi cấu trúc cần $\Theta(n)$, nên tổng là $\Theta(n+m)$. Số vòng không nằm trong cận chi phí mỗi vòng này.

**Triển khai thưa không cộng đôi khối lượng nút cụt.** Ta biết tập $V$ và giữ **đúng một bản ghi cấu trúc** $S_i$ cho mỗi nút, kể cả danh sách rỗng. Tác vụ thứ nhất gom $\delta=d^T r$ từ các nút cụt. Tác vụ cập nhật tiếp theo phát bản ghi cấu trúc và các đóng góp cạnh của $P_0$; reduce tính

$$\beta\left(P_0\,r+\delta\frac{e}{n}\right)+(1-\beta)\frac{e}{n},$$

và gom $\Delta_{t+1}=\|r^{(t+1)}-r^{(t)}\|_1$. Không cần dựng cột đặc hoặc ma trận $U$. Khối lượng $\delta$ chỉ được thêm qua $\delta e/n$; nếu vừa phát nó theo cạnh vừa cộng hạng này thì nút cụt bị đếm hai lần. Tổng sau cập nhật là $\beta(1-\delta)+\beta\delta+(1-\beta)=1$.

**Vòng thuật toán và tác vụ MapReduce.** Một vòng PageRank là một lần cập nhật vector. Nếu hệ thống cần hoàn tất phép gom $\delta$ trước khi cập nhật, vòng đó dùng hai tác vụ MapReduce và hai điểm đồng bộ: một tác vụ tính $\delta$, một tác vụ truyền cấu trúc, cộng đóng góp và tính $\Delta_{t+1}$. Số tác vụ trong một vòng khác với số vòng cần để hội tụ.

**Tự kiểm.** Giải thích vì sao một nút có danh sách kề rỗng vẫn cần bản ghi cấu trúc đi qua reduce.

## 7. Bài tập cuối (theo MMDS)

Bốn bài dưới đây giữ nguyên dữ kiện và yêu cầu của MMDS 5.1.1, 5.1.2, 5.2.1 và 5.2.2.

### Bài MMDS 5.1.1 — PageRank không dùng hệ số giảm cho Hình 5.7

::: exercise
Tính PageRank của từng trang trong Hình 5.7, không dùng hệ số giảm.

![Đồ thị Hình 5.7 gồm ba nút a, b, c và bảy cạnh có hướng](img/lec-03/do-thi-bai-tap-5-7.svg)
:::

Hình 5.7 có $a\to a,b,c$; $b\to a,c$; $c\to b,c$, nên $d^+(a)=3$, $d^+(b)=2$, $d^+(c)=2$.

::: hint
Viết ba phương trình cân bằng theo tập nguồn $N^-(i)$. Cạnh tự nối $a\to a$ đóng góp $r_a/3$ vào $r_a$.
:::

::: solution
Cân bằng:

$$r_a=\frac{r_a}{3}+\frac{r_b}{2},\qquad
r_b=\frac{r_a}{3}+\frac{r_c}{2},\qquad
r_c=\frac{r_a}{3}+\frac{r_b}{2}+\frac{r_c}{2}.$$

Từ phương trình đầu, $r_b=4r_a/3$. Thay vào phương trình thứ hai được $r_c=2r_b-2r_a/3=2r_a$. Chuẩn hóa cho $r_a+4r_a/3+2r_a=13r_a/3=1$, nên

$$r_a=\frac3{13},\qquad r_b=\frac4{13},\qquad r_c=\frac6{13}.$$

Kiểm phương trình đầu: $r_a/3+r_b/2=1/13+2/13=3/13=r_a$. Phương trình thứ hai cho $1/13+3/13=4/13=r_b$; tổng ba thành phần bằng $1$.
:::

### Bài MMDS 5.1.2 — PageRank với $\beta=0{,}8$ cho Hình 5.7

::: exercise
Tính PageRank của từng trang trong Hình 5.7 với $\beta=0{,}8$.

![Đồ thị Hình 5.7 gồm ba nút a, b, c và bảy cạnh có hướng](img/lec-03/do-thi-bai-tap-5-7.svg)
:::

::: hint
Áp dụng $A_\beta=\beta P+(1-\beta)U$. Mỗi phương trình nhận hạng dịch chuyển $(1-\beta)/n=1/15$. Nút $c$ có vòng tự nối còn $b$ không, nên không giả định hai hạng bằng nhau.
:::

::: solution
Ma trận chuyển cột của Hình 5.7: cột $a$ (bậc 3) là $(1/3,1/3,1/3)$, cột $b$ (bậc 2) là $(1/2,0,1/2)$, cột $c$ (bậc 2) là $(0,1/2,1/2)$. Với $A_{0,8}=0{,}8P+0{,}2U$ và mỗi phần tử của $0{,}2U$ bằng $1/15$:

$$A_{0,8}=\begin{bmatrix}5/15&7/15&1/15\\5/15&1/15&7/15\\5/15&7/15&7/15\end{bmatrix},$$

với phần tử $(1,1)=0{,}8/3+1/15=4/15+1/15=5/15=1/3$. Vậy hệ là

$$r_a=\tfrac13 r_a+\tfrac7{15}r_b+\tfrac1{15}r_c,\qquad
r_b=\tfrac13 r_a+\tfrac1{15}r_b+\tfrac7{15}r_c,\qquad
r_c=\tfrac13 r_a+\tfrac7{15}r_b+\tfrac7{15}r_c.$$

Rút gọn (nhân 15):

$$10r_a=7r_b+r_c,\qquad 14r_b=5r_a+7r_c,\qquad 8r_c=5r_a+7r_b.$$

Từ phương trình đầu: $r_c=10r_a-7r_b$. Thay vào phương trình thứ hai: $14r_b=5r_a+7(10r_a-7r_b)=75r_a-49r_b$, tức $63r_b=75r_a$, vậy $r_b=\tfrac{25}{21}r_a$. Kéo theo $r_c=10r_a-7\cdot\tfrac{25}{21}r_a=\tfrac{35}{21}r_a=\tfrac53 r_a$. Phương trình thứ ba có hai vế cùng bằng $\tfrac{40}{3}r_a$, nên thỏa. Chuẩn hóa $r_a(1+\tfrac{25}{21}+\tfrac53)=r_a\cdot\tfrac{81}{21}=1$, nên $r_a=\tfrac{7}{27}$ và

$$r_a=\frac{7}{27},\qquad r_b=\frac{25}{81},\qquad r_c=\frac{35}{81},$$

với tổng $1$. Phương trình đầu cho $10r_a=70/27$ và $7r_b+r_c=210/81=70/27$, nên thỏa. So với Bài 5.1.1, dịch chuyển ngẫu nhiên làm chênh lệch nhỏ hơn; $c$ vẫn có hạng cao nhất.
:::

### Bài MMDS 5.2.1 — mật độ làm biểu diễn thưa tiết kiệm

::: exercise
Cho ma trận Boolean $n\times n$ với $n\ge2$ biểu diễn một đồ thị. So sánh lưu trữ dưới dạng ma trận đầy đủ ($n^2$ bit) với cách liệt kê vị trí các số $1$ dưới dạng các cặp số nguyên, mỗi số nguyên cần $\lceil\log_2 n\rceil$ bit. Tìm mật độ các số $1$ (tỉ lệ số $1$ trên tổng số ô) để biểu diễn thưa tiết kiệm hơn.
:::

::: hint
Mỗi ô bằng $1$ được mã hóa bằng hai số nguyên (chỉ số hàng và chỉ số cột), mỗi số tốn $\lceil\log_2n\rceil$ bit, nên mỗi số $1$ tốn đúng $2\lceil\log_2n\rceil$ bit. Nếu có $q$ ô mang giá trị $1$, so sánh $2q\lceil\log_2n\rceil$ với $n^2$.
:::

::: solution
Với $q$ ô mang giá trị $1$, liệt kê cần $2q\lceil\log_2n\rceil$ bit; ma trận đầy cần $n^2$ bit. Biểu diễn thưa tiết kiệm hơn khi và chỉ khi

$$2q\lceil\log_2 n\rceil<n^2,\qquad\text{hay}\qquad \frac{q}{n^2}<\frac{1}{2\lceil\log_2 n\rceil}.$$

Vậy mật độ ngưỡng là $1/(2\lceil\log_2 n\rceil)$: nếu tỉ lệ ô $1$ thấp hơn ngưỡng này thì liệt kê rẻ hơn, ngược lại ma trận đầy rẻ hơn. Ví dụ $n=2^{20}$: $\lceil\log_2 n\rceil=20$, nên ngưỡng là $1/40=2{,}5\%$. Với trường hợp biên $n=2$, ngưỡng là $1/2$.
:::

### Bài MMDS 5.2.2 — biểu diễn ma trận chuyển bằng §5.2.1

::: exercise
Dùng đúng phương pháp của §5.2.1 để biểu diễn ma trận chuyển của (a) Hình 5.4 và (b) Hình 5.7. Biểu diễn mỗi cột nguồn bằng `nguồn | bậc ra | danh sách đích`; nút cụt có bậc $0$ và danh sách rỗng.
:::

Hình 5.4 có: $A\to B,C,D$; $B\to A,D$; $C\to E$; $D\to B,C$; $E$ không có cạnh ra. Hình 5.7 có: $a\to a,b,c$; $b\to a,c$; $c\to b,c$.

![Đồ thị Hình 5.4 gồm năm nút A đến E, trong đó E là nút cụt](img/lec-03/do-thi-bai-tap-5-4.svg)

![Đồ thị Hình 5.7 gồm ba nút a, b, c và bảy cạnh có hướng](img/lec-03/do-thi-bai-tap-5-7.svg)

::: hint
Với mỗi nguồn, đếm bậc ra bằng số đích sau khi gộp lặp, và liệt kê danh sách đích. Nút cụt $E$ (không cạnh ra) có bậc $0$ và danh sách rỗng. Ghi đúng một bản ghi cho mỗi nút, kể cả nút cụt.
:::

::: solution
(a) Hình 5.4:

| Nguồn | Bậc ra | Danh sách đích |
|---|---|---|
| A | 3 | B, C, D |
| B | 2 | A, D |
| C | 1 | E |
| D | 2 | B, C |
| E | 0 | (rỗng) |

(b) Hình 5.7:

| Nguồn | Bậc ra | Danh sách đích |
|---|---|---|
| a | 3 | a, b, c |
| b | 2 | a, c |
| c | 2 | b, c |

Kiểm tra tổng: Hình 5.4 có $3+2+1+2=8$ đúng bằng số cạnh; Hình 5.7 có $3+2+2=7$ cạnh. Mỗi dòng ứng với đúng một nút, kể cả nút cụt $E$.
:::

## 8. Thu hồi động lực và ranh giới chủ đề

Kho metadata Web không vừa một máy, nhưng ma trận chuyển lại thưa. Hệ số giảm tạo một ánh xạ co; cận hậu nghiệm cho biết khi nào có thể dừng; biểu diễn thưa đưa chi phí mỗi vòng về $\Theta(n+m)$. PageRank vì thế là ví dụ điển hình cho vai trò của giải thuật trong Khoa học dữ liệu: mô hình đúng, bảo đảm đúng và mô hình truy cập dữ liệu phải được thiết kế cùng nhau.

MMDS nhắc đến công trình của Brin và Page như một mốc lịch sử, không phải nguồn cho số đo Web hiện tại. Bài 04 tiếp tục với PageRank theo chủ đề, spam liên kết, TrustRank và HITS; các nội dung đó không thuộc phạm vi ghi chú này.
