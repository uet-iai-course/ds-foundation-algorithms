# Bài 04 — PageRank theo chủ đề, liên kết rác và HITS

Tài liệu này dựa trên chương 5 của *Mining of Massive Datasets* (Leskovec, Rajaraman, Ullman), các mục §5.3–5.5; bộ slide chính thức tại [www.mmds.org](http://www.mmds.org). Bản trình chiếu của bài nằm ở [Bộ trang chiếu](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html). Bài thực hành kèm mã Python nằm ở [Bài thực hành](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html).

**Mục tiêu đọc.** Sau bài này người học có thể:

1. Tính PageRank theo chủ đề: lập $q_S$, chạy vòng lặp thưa và giải hệ để lấy $r^*$ trên đồ thị nhỏ;
2. Giải phương trình cân bằng của cụm thao túng liên kết, phân biệt nghiệm chính xác và xấp xỉ, rồi tính TrustRank và khối lượng rác $s_p$;
3. Chạy hai vòng HITS bằng tay với chuẩn hóa max và phát biểu điều kiện hội tụ theo hướng;
4. Chọn mô hình phù hợp và kiểm tra điều kiện áp dụng trước khi tính.

**Đường học.** §1 khôi phục ký hiệu từ Bài 03 → §2 PageRank theo chủ đề (nền cho §4) → §3–4 cụm thao túng, TrustRank, khối lượng rác → §5 HITS (đọc độc lập, chỉ cần §1) → §6 so sánh → §7 ba bài tập → §8 chọn mô hình. Sau mỗi mục có tự kiểm; phần tính tay đối chiếu với bài thực hành.

## Bảng ký hiệu tra nhanh

| Ký hiệu | Nghĩa | Ghi chú |
|---|---|---|
| $P$ | Ma trận chuyển **cột nguồn** ($P:=S_{\text{Bài03}}$), cột tổng 1 | Nút cụt đã bù đều |
| $L$ | Ma trận kề **hàng nguồn** của HITS, $L_{ij}=1$ nếu $i\to j$ | Chỉ dùng trong §5 |
| $S$ | **Tập đỉnh** chủ đề (không phải ma trận) | Khác $S_{\text{Bài03}}$ |
| $q_S$ | Phân bố dịch chuyển trên tập $S$, thường đều $e_S/\lvert S\rvert$ | Vector, khác $q$ ở §3 là **số** trang hỗ trợ |
| $\beta$ | Hệ số theo liên kết: $4/5$ trong ví dụ G4 và TrustRank; $0.85$ trong Ví dụ 5.11 | Mỗi chỗ ghi rõ giá trị |
| $\tau$ | Ngưỡng dừng lặp, đo chênh giữa hai vòng liên tiếp | Không phải sai số tới nghiệm |
| $K_{\max}$ | Ngân sách số vòng lặp, nguyên $\ge1$ | Hết ngân sách trả trạng thái CHƯA ĐẠT |

Riêng giá trị $\beta=1$ xuất hiện trong đề 5.4.2 chỉ là **quy ước riêng của PageRank nền** trong đề nguồn MMDS (không suy giảm theo liên kết); nó nằm ngoài miền $(0,1)$ mà thuật toán ở §2 đòi hỏi, và không được gọi là phép co.

## 1. Cầu nối từ Bài 03

Bài 03 đã xây dựng ma trận sửa nút cụt $S$ với cột nguồn là các cạnh ra và cột nút cụt được bù đều bằng $u=\mathbf{1}/n$. Trong bài này ta đặt $P := S_{\text{Bài03}}$ và dùng $P$ làm ma trận chuyển. Lưu ý đổi ký hiệu: chữ $S$ ở Bài 04 **không** còn là ma trận mà là **tập đỉnh** chủ đề — tập các trang đại diện cho một chủ đề, phân bố dịch chuyển trên đó gọi là $q_S$.

PageRank cơ sở có ba giới hạn dẫn đến hướng mới của bài này:

1. Điểm xếp hạng không phụ thuộc chủ đề truy vấn (riêng tín hiệu PageRank cơ sở không đổi giữa hai nghĩa động vật và ô tô của *jaguar*);
2. Dễ bị đẩy điểm bằng cụm trang hỗ trợ (cụm thao túng liên kết);
3. Không phân biệt hai vai trò trang dẫn (hub) và trang được dẫn (authority).

Ba mô hình trả lời lần lượt: PageRank theo chủ đề (§2), phân tích cụm thao túng cùng TrustRank/khối lượng rác (§3–4), và HITS (§5). Giả thiết người đọc đã quen đồ thị có hướng, phép nhân ma trận–vector và xác suất cơ bản. Tên đầy đủ của HITS lần đầu gặp là *tìm kiếm theo chủ đề dựa trên siêu liên kết (HITS)* (Hyperlink-Induced Topic Search).

## 2. PageRank theo chủ đề (topic-sensitive PageRank)

### 2.1 Nhu cầu

PageRank cơ sở cho mỗi trang một điểm độc lập với truy vấn. Khi truy vấn mang tính chủ đề, thứ hạng nên thiên về các trang thuộc chủ đề đó. Ý tưởng: chạy nhiều bộ PageRank, mỗi bộ ứng với một chủ đề, và phần dịch chuyển chỉ nhảy về tập đại diện của chủ đề ấy.

### 2.2 Đặc tả

Cho đồ thị với $n\ge1$ đỉnh, ma trận chuyển cột nguồn $P$ (cột tổng 1, không âm; nút cụt đã được bù đều trong $P$). Cho $S\ne\emptyset$ là tập đỉnh chủ đề và $\beta\in(0,1)$. Vector dịch chuyển $q_S$ là một phân bố trên $S$: $q_S\ge0$, $\sum_i(q_S)_i=1$, và $(q_S)_i=0$ với mọi $i\notin S$ (giá của $q_S$ nằm trong $S$). Trường hợp dùng xuyên suốt bài này là $q_S$ **đều trên $S$**: $q_S=e_S/|S|$, với $e_S$ là vector chỉ thị của $S$.

PageRank theo chủ đề là nghiệm của phương trình bất động

$$r = \beta P r + (1-\beta)\, q_S,$$

Phần $(1-\beta)q_S$ là **phần dịch chuyển**: mỗi vòng, một khối lượng $(1-\beta)$ được phân bố lại trên tập $S$ thay vì trên toàn bộ đồ thị.

### 2.3 Ví dụ G4

Dùng G4 ($n=4$, $m_G=8$; A→B,C,D; B→A,D; C→A; D→B,C), không nút cụt nên $P=M_0$:

$$P=\begin{bmatrix}0&\tfrac12&1&0\\ \tfrac13&0&0&\tfrac12\\ \tfrac13&0&0&\tfrac12\\ \tfrac13&\tfrac12&0&0\end{bmatrix}$$

**Vế theo cạnh:** $\beta P r$ — khối lượng đi theo cạnh, bị co hệ số $\beta$. **Vế dịch chuyển:** $(1-\beta)q_S$ — khối lượng nhảy về tập chủ đề.

Với $S=\{B,D\}$, $\beta=4/5$, $q_S=(0,\tfrac12,0,\tfrac12)$, khởi $r_0=q_S$:

| Vòng | $r_A$ | $r_B$ | $r_C$ | $r_D$ | Trạng thái |
|---|---|---|---|---|---|
| $r_0=q_S$ | $0$ | $\tfrac12$ | $0$ | $\tfrac12$ | khởi |
| $r_1$ | $\tfrac15$ | $\tfrac3{10}$ | $\tfrac15$ | $\tfrac3{10}$ | 1 vòng |
| $r_2$ | $\tfrac{42}{150}$ | $\tfrac{41}{150}$ | $\tfrac{26}{150}$ | $\tfrac{41}{150}$ | 2 vòng |
| $r_3$ | $\tfrac{62}{250}$ | $\tfrac{71}{250}$ | $\tfrac{46}{250}$ | $\tfrac{71}{250}$ | 3 vòng |
| $r^*$ | $\tfrac{54}{210}$ | $\tfrac{59}{210}$ | $\tfrac{38}{210}$ | $\tfrac{59}{210}$ | nghiệm chính xác (giải hệ) |

Ví dụ vòng 1: $\beta P r_0 = (\tfrac15,\tfrac15,\tfrac15,\tfrac15)$ và $(1-\beta)q_S=(0,\tfrac1{10},0,\tfrac1{10})$, cộng lại được $r_1$. Chú ý $r^*$ là nghiệm giải hệ, không phải kết quả vòng 3.

Một phương trình mẫu theo tọa độ của $r=(\tfrac45)Pr+(\tfrac15)q_S$ (với $S=\{B,D\}$):

$$r_B=\frac45\left(\frac{r_A}{3}+\frac{r_D}{2}\right)+\frac1{10}.$$

Giải bốn phương trình tọa độ như vậy cho $r^*$ ở bảng trên; tổng bằng 1 là một phép kiểm nghiệm.

### 2.4 Trực giác và bất biến

Mỗi vòng, khối lượng chia làm hai dòng: phần $\beta$ đi theo cạnh, phần $1-\beta$ quay về tập $S$. Vì $P$ cột tổng 1 và $q_S$ là phân bố, ánh xạ $F(r)=\beta Pr+(1-\beta)q_S$ bảo toàn bất biến xác suất: nếu $r\ge0$, $\sum r_i=1$ thì $r_{\text{mới}}\ge0$ và $\sum (r_{\text{mới}})_i = \beta + (1-\beta) = 1$. Phép co theo chuẩn L1:

$$\|F(r)-F(s)\|_1 = \beta\,\|P(r-s)\|_1 \le \beta\,\|r-s\|_1,$$

vì $\|Pv\|_1\le\|v\|_1$ khi $P$ cột tổng 1. Với $\beta<1$, ánh xạ co trên tập các phân phối xác suất nên $r^*$ tồn tại duy nhất và lặp hội tụ. Điểm có thể bằng 0 ở những trang không được $q_S$ hỗ trợ gián tiếp — không tuyên bố dương mọi trang.

**Bất đẳng thức tam giác theo từng phần tử.** Với vector bất kỳ $v$,

$$\begin{aligned}
\|Pv\|_1
&=\sum_i\Big|\sum_j P_{ij}v_j\Big|\\
&\le\sum_i\sum_j P_{ij}|v_j|\\
&=\sum_j|v_j|\sum_iP_{ij}\\
&=\|v\|_1.
\end{aligned}$$

dùng bất đẳng thức tam giác cho từng thành phần và giả thiết cột tổng 1 của $P$. Đây là suy diễn trực tiếp từ phương trình MMDS §5.3.2.

::: proof
**Tồn tại, duy nhất, co và chặn lỗi.** Vì $0<\beta<1$, chuỗi hình học

$$r^*=(1-\beta)\sum_{k\ge0}\beta^k P^k q_S$$

có tổng khối lượng $(1-\beta)\sum_{k\ge0}\beta^k=1$ (mỗi $P^kq_S$ là phân bố vì $P$ cột tổng 1), nên chuỗi hội tụ và tổng của nó là một phân bố. Thay vào phương trình bất động:

$$\begin{aligned}
\beta Pr^*+(1-\beta)q_S
&=(1-\beta)\sum_{k\ge1}\beta^kP^kq_S+(1-\beta)q_S\\
&=(1-\beta)\sum_{k\ge0}\beta^kP^kq_S\\
&=r^*,
\end{aligned}$$

nên $r^*$ là điểm bất động. Tính duy nhất: nếu $r,r'$ đều bất động thì

$$\|r-r'\|_1=\beta\|P(r-r')\|_1\le\beta\|r-r'\|_1,$$

mà $\beta<1$ nên $\|r-r'\|_1=0$. Chặn lỗi theo vòng: đặt $e_\ell=r_\ell-r^*$ với $\ell$ là chỉ số vòng lặp, thì

$$\|e_{\ell+1}\|_1=\beta\|Pe_\ell\|_1\le\beta\|e_\ell\|_1,$$

suy ra

$$\|r_\ell-r^*\|_1\le\beta^\ell\|r_0-r^*\|_1.$$
:::

### 2.5 Giả mã thưa

Không lưu $P$ đặc; mỗi vòng chỉ quét cạnh của đồ thị thô và **tính lại** phần bù nút cụt. Ở đây $M_0$ là ma trận cột nguồn chuẩn hóa của đồ thị thô (cột của nút cụt là cột 0):

```text
r ← q_S                      # khởi tạo từ q_S
với vòng = 1 .. K_max:
    δ ← Σ r_j trên các đỉnh cụt      # tính lại mỗi vòng
    r_mới ← β M0 r + β δ u + (1−β) q_S
    nếu ‖r_mới − r‖₁ ≤ τ:  trả r_mới, trạng thái ĐẠT
    r ← r_mới
hết K_max:  trả r, trạng thái CHƯA ĐẠT
```

với $u=\mathbf{1}/n$, $n\ge1$, $K_{max}$ nguyên $\ge1$, $\tau>0$. Hai trạng thái kết thúc: đạt ngưỡng (trả vector mới) hoặc hết ngân sách vòng (trả vector và trạng thái cuối). Lưu ý $\tau$ chỉ là **điều kiện dừng tính toán**: nó đo độ thay đổi giữa hai vòng liên tiếp, không phải sai số tới nghiệm $r^*$. Không được dùng chính $\tau$ làm chặn sai số tới nghiệm. Chặn theo số vòng $\ell$ đã được chứng minh ở §2.4.

### 2.6 Chi phí và phối hợp

Mỗi vòng tốn $\Theta(n+m_G)$ phép nhân–cộng với $m_G$ là số cạnh của đồ thị thô (không lưu $P$ đặc sau bù cụt); tổng bộ nhớ $O(n+m_G)$ cho vector và danh sách cạnh. Với $k$ chủ đề, gọi $I$ là số vòng lặp: $O(kI(n+m_G))$ phép tính, bộ nhớ $O(kn+m_G)$ — chỉ cần lưu $k$ vector ngoài đồ thị. Phối hợp lúc truy vấn: với trọng số $\alpha_l\ge0$, $\sum\alpha_l=1$, dùng chung $P$ và $\beta$, trong đó $r^{(l)*}$ là nghiệm của mỗi chủ đề $l$,

$$r^* = \sum_{l=1}^{k} \alpha_l\, r^{(l)*},$$

tức điểm hỗn hợp ứng với dịch chuyển hỗn hợp $q=\sum_l\alpha_l q_l$; tính tuyến tính theo các vector chủ đề.

::: example
Kiểm tra nhanh trên G4: A nhận theo cạnh từ B và C. Vì $r_{0,B}=1/2$, $r_{0,C}=0$ và $(q_S)_A=0$,

$$r_{1,A}=\frac45\left(\frac12\cdot\frac12+1\cdot0\right)+\frac15\cdot0=\frac15.$$

Tại B, cạnh D→B đóng góp $1/5$ và phần dịch chuyển đóng góp $1/10$:

$$r_{1,B}=\frac45\left(\frac13\cdot0+\frac12\cdot\frac12\right)+\frac1{10}=\frac3{10}.$$

Hai thành phần theo cạnh và dịch chuyển có nguồn khác nhau.
:::

Tự kiểm: $S=V$ (toàn bộ đỉnh) với $q_S=\mathbf{1}/n$ phải cho lại đúng PageRank cơ sở của Bài 03. Giới hạn: đặc tả đòi $S\ne\emptyset$; nếu $S$ rỗng thì $q_S$ không phải phân bố và mô hình không xác định.

## 3. Cụm thao túng liên kết — MMDS §5.4.1–5.4.2

### 3.1 Vai trò

Một người thao túng có thể dựng mạng liên kết nhân tạo để nâng PageRank của trang đích. Tập trang hỗ trợ được tạo cho mục đích này gọi là **cụm thao túng liên kết** (spam farm). Mô hình dưới đây tính phần hạng mà cấu trúc ấy dồn vào trang đích $t$.

### 3.2 Mô hình và đặc tả

Chia toàn bộ web thành ba vùng theo mức độ truy cập của người vận hành spam farm:

1. **Trang không tiếp cận được**: người thao túng không thể thay đổi liên kết.
2. **Trang có thể tác động**: người thao túng có thể chèn liên kết tới trang đích.
3. **Trang sở hữu**: người vận hành kiểm soát toàn bộ, gồm cả trang đích $t$.

Các biến:

- $N$: tổng số trang web, với $N\ge q+1$ (cần ít nhất trang đích ngoài $q$ trang hỗ trợ).
- $q$: số trang hỗ trợ trong spam farm, nguyên $\ge1$.
- $x$: tổng đóng góp từ ngoài vào đích $t$, đã gồm nhân $\beta$.
- $y$: PageRank của đích $t$.

Cả $q$ và $N$ đều có thể thay đổi khi tăng $q$ (thêm trang hỗ trợ cũng tăng $N$, có thể thay cả $x$), nên cần thận trọng khi diễn dịch. Sách MMDS dùng ký hiệu $m,n$ cho hai đại lượng này; ở đây đổi tên thành $q,N$ để phân biệt với số đỉnh/cạnh của đồ thị ví dụ. Mô hình dùng $0<\beta<1$ như §2.

Cấu trúc đồ thị trong Hình 5.16: mỗi trang hỗ trợ chỉ trỏ tới $t$; $t$ trỏ tới cả $q$ trang hỗ trợ.

![Hình 5.16 — Cụm thao túng liên kết với ba vùng: vùng không thể tác động, vùng có thể tác động, và vùng các trang sở hữu; trang đích t và q trang hỗ trợ cùng nằm trong vùng sở hữu, dòng chảy từ vùng giữa vào t](img/lec-04/hinh-5-16-cum-thao-tung.svg)

**Hình 5.16** — Ba vùng của cụm thao túng: vùng không thể tác động, vùng có thể tác động, và vùng các trang sở hữu. Trang đích $t$ và $q$ trang hỗ trợ cùng thuộc vùng sở hữu; mỗi trang hỗ trợ chỉ trỏ về đích, đích trỏ tới mọi trang hỗ trợ. Dòng đóng góp $x$ đi từ vùng giữa vào $t$.

### 3.3 Hạng của mỗi trang hỗ trợ

Gọi $z$ là hạng của mỗi trang trong $q$ trang hỗ trợ. Do cấu trúc đối xứng, mọi trang hỗ trợ có cùng $z$.

Mỗi trang hỗ trợ nhận đóng góp từ $t$ qua phần $\beta P r$, rồi cộng phần dịch chuyển đều $(1-\beta)/N$. Vì $t$ trỏ tới cả $q$ trang hỗ trợ và hạng của $t$ là $y$, mỗi trang hỗ trợ nhận $y/q$ qua cạnh rồi nhân $\beta$:

$$z=\beta\frac{y}{q}+\frac{1-\beta}{N}.$$

![Luồng hạng từ trang ngoài vào trang đích t, rồi tuần hoàn giữa t và q trang hỗ trợ.](img/lec-04/luong-hang-trong-cum.svg)

::: derivation
Trang đích $t$ có điểm $y$ và chia phần theo cạnh đều cho $q$ trang hỗ trợ. Mỗi trang nhận $\beta y/q$. Phần dịch chuyển đều thêm $(1-\beta)/N$, tạo phương trình cân bằng của $z$ ở trên.
:::

### 3.4 Phương trình chính xác cho $y$

Phương trình chính xác cho đích $t$ có ba số hạng: đóng góp ngoài $x$ (đã gồm $\beta$), đóng góp qua $q$ trang hỗ trợ mỗi trang đóng $\beta z$, và phần dịch chuyển trực tiếp $(1-\beta)/N$:

$$y=x+\beta qz+\frac{1-\beta}{N}.$$

Thay $z=\beta y/q+(1-\beta)/N$:

$$\begin{aligned}
y&=x+\beta q\left(\beta\frac{y}{q}+\frac{1-\beta}{N}\right)+\frac{1-\beta}{N}\\
&=x+\beta^2y+\frac{\beta q(1-\beta)}{N}+\frac{1-\beta}{N}.
\end{aligned}$$

Chuyển $\beta^2y$ sang trái:

$$y(1-\beta^2)=x+\frac{(1-\beta)(\beta q+1)}{N}.$$

Vì $1-\beta^2=(1-\beta)(1+\beta)$, ta có:

$$y=\frac{x}{1-\beta^2}+\frac{\beta q+1}{N(1+\beta)}.$$

Sách (MMDS §5.4.2) đưa ra một biểu thức đơn giản hơn bằng cách bỏ số hạng phần dịch chuyển trực tiếp vào trang đích $t$ — tức bỏ $(1-\beta)/N$ **trong phương trình cân bằng của $y$ tại trang đích $t$** — trước khi giải; số hạng này **không bị bỏ** trong phương trình cân bằng của $z$ ở §3.3:

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\cdot\frac{q}{N}.$$

**Phân biệt hai đại lượng dễ nhầm.** Số hạng bị bỏ là $(1-\beta)/N$ — một thành phần của phương trình cân bằng tại vế phải. Hệ quả của việc bỏ nó, sau khi đã giải và chia cho $1-\beta^2$, là hai nghiệm chênh nhau $\dfrac{1}{N(1+\beta)}$:

$$y_{\text{chính xác}}=\frac{x}{1-\beta^2}+\frac{\beta q+1}{N(1+\beta)}, \qquad y_{\text{xấp xỉ}}=\frac{x}{1-\beta^2}+\frac{\beta q}{N(1+\beta)}.$$

Vậy $(1-\beta)/N$ và $\dfrac{1}{N(1+\beta)}$ là hai đại lượng **khác nhau**: một là số hạng bị bỏ trong phương trình, kia là sai khác giữa hai nghiệm sau khi đã chia cho $1-\beta^2$. Không được gọi hai đại lượng ấy là một.

::: example
**Ví dụ 5.11.**

Với $\beta=0.85$,

$$\frac{1}{1-\beta^2}=\frac{1}{0.2775}\approx3.6036,
\qquad \frac{\beta}{1+\beta}=\frac{0.85}{1.85}\approx0.4595.$$

Dạng xấp xỉ của sách là $y\approx3.6036x+0.4595q/N$.
:::

### 3.5 Giới hạn của mô hình

Mô hình giả sử mỗi trang hỗ trợ chỉ trỏ tới $t$, còn $t$ trỏ đều tới cả $q$ trang hỗ trợ. Công thức không mô tả mọi cấu trúc thao túng. Hơn nữa, $q<N$ và việc thêm trang hỗ trợ làm đổi $N$, có thể đổi cả đóng góp ngoài $x$. MMDS §5.4.3 dùng sự thích nghi qua lại giữa người thao túng và bộ máy tìm kiếm để dẫn sang cách tiếp cận dựa trên tập trang tin cậy.

**Tự kiểm.** Gán tên nguồn hạng cho bốn số hạng trong phương trình trước khi gom $y$: $x$, $\beta^2y$, $\beta q(1-\beta)/N$ và $(1-\beta)/N$.

## 4. TrustRank và khối lượng rác — MMDS §5.4.3–5.4.5

### 4.1 Vai trò

Liên kết có thể bị thao túng, nên TrustRank thay tập trang theo chủ đề bằng tập trang đã được thẩm định. Khối lượng rác sau đó đo độ chênh tương đối giữa PageRank và TrustRank của từng trang.

Từ phần này, $t$ là vector điểm tin cậy; ở mô hình cụm thao túng trước đó, chữ $t$ chỉ trang đích. TrustRank chạy trên toàn đồ thị, dùng tín hiệu $q_T$ và trả một điểm tin cậy cho mỗi trang.

### 4.2 Đặc tả

Cho $T\subseteq V$ khác rỗng, đặt $q_T=e_T/|T|$ và:

$$t^{(0)}=q_T,\qquad t^{(u+1)}=\beta P t^{(u)}+(1-\beta)q_T.$$

Công thức co $L_1$ tương tự PageRank chủ đề, xác định duy nhất điểm bất động.

Chọn hạt giống: chọn ứng viên có PageRank cao rồi thẩm định thủ công, hoặc chọn các miền có cơ chế thành viên. Không coi hậu tố miền là chứng nhận tuyệt đối. Kết quả TrustRank phụ thuộc độ phủ của hạt giống và sai số chọn hạt giống.

### 4.3 Khối lượng rác (spam mass)

Cho mỗi trang $p$ với PageRank $r_p>0$ và TrustRank $t_p$, định nghĩa:

$$s_p=\frac{r_p-t_p}{r_p}.$$

::: example
Nếu $r_p>t_p$ thì $s_p>0$; nếu $r_p<t_p$ thì $s_p<0$; và nếu hai điểm bằng nhau thì $s_p=0$. Khi $r_p=0$, tỷ số không xác định.
:::

$s_p$ có thể âm, không bị kẹp về $0$ và không phải xác suất. MMDS không đưa ra một ngưỡng bảo đảm để phân loại trang rác từ tỷ số này.

Vì vậy chỉ tính $s_p$ khi $r_p>0$, giữ nguyên giá trị âm và không diễn giải $s_p$ như xác suất.

### 4.4 Ví dụ 5.12 và Hình 5.17 — hai quy ước khác nhau

Hình 5.17 minh họa một điểm về quy ước tính. Trên cùng một cấu trúc liên kết, hình cố ý dùng hai quy ước khác nhau:

- PageRank **không suy giảm ($\beta=1$)**: $r=(3/9,2/9,2/9,2/9)^T$.
- TrustRank với $\beta=0.8$, $T=\{B,D\}$: $t=(54,59,38,59)^T/210$.

Khối lượng rác tương ứng là $(8/35,-37/140,13/70,-37/140)^T$. Chẳng hạn, tại $A$:

$$s_A=\frac{3/9-54/210}{3/9}=\frac{8}{35}\approx0.229.$$

Hai vector trong hình dùng hai quy ước khác nhau, nên ví dụ chỉ minh họa phép tính tỷ số. Khi dùng khối lượng rác để so sánh trong ứng dụng, phải tính PageRank và TrustRank với cùng $\beta$ và cùng quy ước xử lý nút cụt.

**Tự kiểm.** Tính lại $s_B$ và giải thích vì sao kết quả âm không phải lỗi. Bài 7.2 thay tập tin cậy bằng $T=\{B\}$.

## 5. HITS — MMDS §5.5.1–5.5.2

PageRank theo chủ đề và TrustRank vẫn gán cho mỗi trang **một** điểm duy nhất; HITS tách hai vai trò trang dẫn và trang được dẫn thành hai điểm riêng.

### 5.1 Vai trò

HITS (Hyperlink-Induced Topic Search) xếp hạng trong một đồ thị con cố định lấy từ kết quả truy vấn. MMDS Ví dụ 5.13 mô tả danh sách học phần như một trang trung tâm và trang của từng học phần như trang thẩm quyền. Mỗi trang vẫn có cả hai điểm:

- **Điểm thẩm quyền** (authority) $a_i$: cao khi được các trang trung tâm có điểm cao trỏ tới.
- **Điểm trung tâm** (hub) $h_i$: cao khi trỏ tới các trang thẩm quyền có điểm cao.

Trang danh mục minh họa vai trò dẫn đường; trang học phần minh họa vai trò cung cấp nội dung. Điểm của hai vai trò phụ thuộc lẫn nhau qua liên kết.

![Trực quan hai vai trò HITS: trang trung tâm trỏ tới các trang thẩm quyền; mỗi trang có cả hai loại điểm.](img/lec-04/cap-vai-tro-hits.svg)

### 5.2 Hai phép cập nhật luân phiên

Cho đồ thị con $G_H$ với $n_H$ đỉnh và $m_H$ cạnh. Khác với PageRank (dùng ma trận **cột nguồn**), HITS dùng ma trận kề $L\in\{0,1\}^{n_H\times n_H}$ với **hàng là nguồn**: $L_{ij}=1$ nếu $i\to j$.

HITS thực hiện hai bước luân phiên:

- **Thẩm quyền thô**: $a_{\text{thô}}=L^Th$. Thành phần $i$ bằng tổng $h_j$ của mọi trang $j$ trỏ tới $i$.
- **Trung tâm thô**: $h_{\text{thô}}=La$. Thành phần $i$ bằng tổng $a_j$ của mọi trang $j$ mà $i$ trỏ tới.

Sau mỗi phép nhân, chia cho phần tử lớn nhất (chuẩn max).

::: derivation
Phần tử $(L^Th)_i=\sum_jL_{ji}h_j$. Vì $L_{ji}=1$ khi $j\to i$, đây là tổng điểm trung tâm của các trang trỏ tới $i$. Tương tự, $(La)_i=\sum_jL_{ij}a_j$ là tổng điểm thẩm quyền của các trang mà $i$ trỏ tới.
:::

::: derivation
Về đại số, $a\propto L^TLa$ và $h\propto LL^Th$. Trong tính toán, không dựng $L^TL$ hay $LL^T$ vì tích có thể đặc. Ta giữ hai phép nhân thưa nối tiếp, mỗi vòng có chi phí $\Theta(n_H+m_H)$.
:::

### 5.3 Ví dụ 5.14–5.15 — Hình 5.18–5.20

Xét đồ thị Hình 5.18 với thứ tự $(A,B,C,D,E)$:

- $A\to B,C,D$;
- $B\to A,D$;
- $C\to E$;
- $D\to B,C$;
- $E$ không trỏ ra.

Ma trận liên kết trong Hình 5.19 là

$$L=\begin{bmatrix}0&1&1&1&0\\1&0&0&1&0\\0&0&0&0&1\\0&1&1&0&0\\0&0&0&0&0\end{bmatrix}.$$

Khởi đầu $h^{(0)}=e=(1,1,1,1,1)^T$.

Hai vòng dưới đây dựng lại bảng vết Hình 5.20.

**Vòng 1.** $a_{\text{thô}}=L^Th^{(0)}$: cộng theo cột của $L$:

$$a_{\text{thô}}=(1,2,2,2,1)^T.$$

Chuẩn vô cùng (giá trị lớn nhất là $2$):

$$a^{(1)}=\left(\frac{1}{2},1,1,1,\frac{1}{2}\right)^T.$$

$h_{\text{thô}}=La^{(1)}$: cộng theo hàng:

- Hàng A: $a_B+a_C+a_D=1+1+1=3$;
- Hàng B: $a_A+a_D=1/2+1=3/2$;
- Hàng C: $a_E=1/2$;
- Hàng D: $a_B+a_C=1+1=2$;
- Hàng E: $0$.

$$h_{\text{thô}}=(3,3/2,1/2,2,0)^T.$$

Chuẩn (giá trị lớn nhất là $3$):

$$h^{(1)}=\left(1,\frac{1}{2},\frac{1}{6},\frac{2}{3},0\right)^T.$$

**Vòng 2.** $L^Th^{(1)}$: cộng theo cột:

- Cột A: $h_B=1/2$;
- Cột B: $h_A+h_D=5/3$;
- Cột C: $h_A+h_D=5/3$;
- Cột D: $h_A+h_B=3/2$;
- Cột E: $h_C=1/6$.

$$a_{\text{thô}}=(1/2,5/3,5/3,3/2,1/6)^T.$$

Chuẩn (lớn nhất là $5/3$):

$$a^{(2)}=\left(\frac{3}{10},1,1,\frac{9}{10},\frac{1}{10}\right)^T.$$

$La^{(2)}$: cộng theo hàng:

- A: $a_B+a_C+a_D=29/10$;
- B: $a_A+a_D=6/5$;
- C: $a_E=1/10$;
- D: $a_B+a_C=2$;
- E: $0$.

$$h_{\text{thô}}=(29/10,6/5,1/10,2,0)^T.$$

Chuẩn (lớn nhất là $29/10$):

$$h^{(2)}=\left(1,\frac{12}{29},\frac{1}{29},\frac{20}{29},0\right)^T.$$

$A$ có điểm trung tâm lớn nhất sau hai vòng; $B$ và $C$ có điểm thẩm quyền lớn nhất.

![Đồ thị Hình 5.18 gồm năm nút A, B, C, D, E và các cạnh dùng để tính HITS.](img/lec-04/hinh-5-18.svg)

### 5.4 Đặc tả hình thức HITS

Trên đồ thị con $G_H$ với $n_H$ đỉnh và $m_H$ cạnh, dựng ma trận kề $L$ kích thước $n_H\times n_H$ với **hàng là nguồn**: $L_{ij}=1$ nếu có cạnh $i\to j$, ngược lại $0$ (Boolean). Khởi tạo $h_0=\mathbf{1}$ (vector toàn 1) và $a_0=\mathbf{0}$; $a_0$ chỉ dùng làm mốc đo chênh ở vòng đầu, không tham gia sinh $a_1$ theo công thức truy hồi của $a$.

Quy tắc cập nhật luân phiên, chuẩn hóa theo **phần tử lớn nhất** (chuẩn max của sách, khác chuẩn L2 trong một số slide):

$$a_{\text{thô}} = L^T h_{\text{cũ}}, \qquad h_{\text{thô}} = L\, a_{\text{mới}},$$

chia mỗi vector cho phần tử lớn nhất của chính nó sau mỗi bước.

Đầu vào yêu cầu $n_H\ge1$, $\tau>0$, $K_{\max}$ nguyên và ít nhất 1. Giả mã (chuẩn hóa bằng phần tử lớn nhất, cập nhật luân phiên):

```text
h ← 1 (vector toàn 1);  a ← 0
với u = 1 .. K_max:
    a_thô ← Lᵀ h;   nếu max(a_thô) = 0: trả h = 0, a = 0, cờ SUY BIẾN; dừng
    a_mới ← a_thô / max(a_thô)
    h_thô ← L a_mới; nếu max(h_thô) = 0: trả h = 0, a = 0, cờ SUY BIẾN; dừng
    h_mới ← h_thô / max(h_thô)
    nếu max|a_mới − a| ≤ τ và max|h_mới − h| ≤ τ:
        trả (h_mới, a_mới), cờ ĐẠT NGƯỠNG; dừng
    h ← h_mới;  a ← a_mới
hết K_max: trả (h, a), cờ CHƯA ĐẠT
```

Ba cờ trạng thái: suy biến ($L=0$, đồ thị không cạnh — cả hai nhánh đều trả cặp vector 0), đạt ngưỡng $\tau$, chưa đạt khi hết ngân sách vòng. Khi đạt ngưỡng trả cặp **mới** $(h_{\text{mới}},a_{\text{mới}})$; khi hết ngân sách trả cặp cuối. Ngưỡng $\tau$ chỉ là tiêu chí dừng tính toán, đo độ chênh giữa hai vòng liên tiếp — nó không cho biết khoảng cách tới nghiệm thật.

Truy hồi: $h_{u+1}\propto LL^T h_u$ với $u\ge0$, và $a_{u+1}\propto L^T L\, a_u$ với $u\ge1$. Riêng $a_1$ sinh từ $h_0$ qua $a_1\propto L^T h_0$; không truy hồi $a_0=\mathbf{0}$ (nếu làm vậy sẽ dừng ngay ở vector 0).

### 5.5 Điều kiện hội tụ và chi phí

Các điều kiện sau là **đủ** bảo đảm hội tụ về hướng trội (không phải điều kiện cần):

- $L\ne 0$;
- giá trị riêng trội duy nhất: $\lambda_1 > \lambda_2 \ge 0$ cho cả $LL^T$ và $L^TL$;
- khởi tạo có hình chiếu khác 0 lên hướng trội của $LL^T$ (điều kiện đặt trên $h_0$).

::: proof
**Phác thảo hội tụ theo hướng.** Đặt $B=LL^T$. Ma trận $B$ đối xứng, nửa xác định dương nên có cơ sở vector riêng trực chuẩn $v_j$ với trị riêng $\lambda_j\ge0$. Viết $h_0=\sum_j c_jv_j$, trong đó $c_1\ne0$. Khi đó

$$\frac{B^u h_0}{\lambda_1^u}=c_1v_1+\sum_{j\ge2}c_j\left(\frac{\lambda_j}{\lambda_1}\right)^u v_j.$$

Do $\lambda_1>\lambda_2$, các thành phần không trội tiến về 0 tương đối so với thành phần trội. Chuẩn hóa theo phần tử lớn nhất không đổi hướng của vector. Vì $\lambda_1>0$, $L^Tv_1\ne0$, nên bước cập nhật thẩm quyền cũng tiến về hướng tương ứng. Đây là phác thảo dưới các điều kiện đủ đã nêu, không phải khẳng định cho mọi ma trận liên kết.
:::

Phương pháp lũy thừa được đối chiếu với [Cornell INFO4300, Ginsparg, 27/10/2009, slide 10](https://courses.cit.cornell.edu/info4300_2009fa/slides/16.pdf); quy tắc HITS theo MMDS §5.5.
Chi phí mỗi vòng: hai quét cạnh (nhân $L^Th$ và $La$) cộng số hữu hạn quét đỉnh (tìm max, chuẩn hóa, đo chênh), tổng $\Theta(n_H+m_H)$; tổng bộ nhớ $O(n_H+m_H)$ cho đồ thị thưa và các vector. Không dựng ma trận $LL^T$ hay $L^TL$ đặc trong triển khai thưa; chỉ với hệ ma trận nhỏ hợp lệ mới giải theo ma trận.

Tự kiểm: $E$ không có cạnh ra nên $h_E=0$ ngay từ vòng 1, nhưng $a_E=\tfrac12>0$ ở vòng đầu vì có cạnh C→E — hai vai trò không đồng nhất.

## 6. Bảng so sánh

| Tiêu chí | PageRank theo chủ đề | TrustRank |
|---|---|---|
| Phạm vi | Toàn đồ thị | Toàn đồ thị |
| Tín hiệu | $q_S$ từ tập chủ đề | $q_T$ từ tập tin cậy |
| Đầu ra | Phân phối $r^{(S)}$ | Phân phối tin cậy $t$ |
| Bảo đảm | Phép co $L_1$ với hệ số $\beta$ | Cùng phép co PageRank |
| Chi phí mỗi vòng | $\Theta(n+m_G)$ mỗi vector | $\Theta(n+m_G)$ |

| Tiêu chí | Khối lượng rác | HITS |
|---|---|---|
| Phạm vi | Hậu xử lý $r,t$ | Đồ thị con truy vấn |
| Tín hiệu | Chênh lệch tương đối | Cấu trúc liên kết Boolean |
| Đầu ra | Tỷ số $s_p$ cho từng trang | Hai điểm $a_i,h_i$ |
| Bảo đảm | Cần $r_p>0$; không phải xác suất | Hội tụ có điều kiện phổ |
| Chi phí | $\Theta(n)$ | $\Theta(n_H+m_H)$ mỗi vòng |

- PageRank theo chủ đề và TrustRank dùng cùng mô hình vòng lặp co $L_1$, chi phí mỗi vòng giống nhau; khác nhau ở đối tượng $q$ (chủ đề so với tin cậy).
- Khối lượng rác không chạy vòng lặp mới: chỉ tính $s_p=(r_p-t_p)/r_p$ trên mỗi trang, với chi phí $\Theta(n)$ và điều kiện $r_p>0$.
- HITS chạy trên đồ thị con, $\Theta(n_H+m_H)$ mỗi vòng với hai phép nhân thưa.

## 7. Ba bài tập MMDS

### 7.1 MMDS 5.3.1 — PageRank theo chủ đề trên Hình 5.15

::: exercise
Trên đồ thị Hình 5.15, giữ $\beta=0.8$ như Ví dụ 5.10. Tính PageRank theo chủ đề khi: (a) $S=\{A\}$; (b) $S=\{A,C\}$. Sản phẩm gồm hai vector điểm bất động theo thứ tự $(A,B,C,D)$ và phép kiểm tổng bằng $1$.
:::

::: hint
Với $S=\{A\}$, dùng $q_S=(1,0,0,0)^T$. Với $S=\{A,C\}$, dùng $q_S=(1/2,0,1/2,0)^T$. Trong từng trường hợp, giải $r=0.8Pr+0.2q_S$ cùng điều kiện $e^Tr=1$.
:::

::: solution
Với $S=\{A\}$, nghiệm là

$$r=\left(\frac37,\frac4{21},\frac4{21},\frac4{21}\right)^T.$$

Tổng các thành phần bằng $3/7+3(4/21)=1$. Với $S=\{A,C\}$, nghiệm là

$$r=\left(\frac{27}{70},\frac6{35},\frac{19}{70},\frac6{35}\right)^T.$$

Tổng bằng $(27+12+19+12)/70=1$. Trong cả hai trường hợp, thay vector vào $r-0.8Pr=0.2q_S$ cho đúng phần dư dịch chuyển.
:::

![Đồ thị Hình 5.15, cùng cấu trúc với Hình 5.1, gồm bốn trang A, B, C, D và không đánh dấu tập dịch chuyển.](img/lec-04/hinh-5-1-trung-tinh.svg)

Nguồn: [MMDS](http://www.mmds.org), Bài 5.3.1, trang in 199, PDF trang 25.

### 7.2 MMDS 5.4.2 — TrustRank và khối lượng rác

::: exercise
Trên đồ thị Hình 5.1 theo thứ tự $(A,B,C,D)$, giả sử chỉ $B$ là trang tin cậy và $\beta=0.8$. G4 không có nút cụt nên $P=M_0$. Ma trận chuyển và PageRank nền với $\beta=1$ là

$$P=\begin{bmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{bmatrix},
\qquad r=\left(\frac13,\frac29,\frac29,\frac29\right)^T.$$

Tính TrustRank của mỗi trang, rồi tính khối lượng rác. Sản phẩm gồm vector $t$, vector $s$ và phép kiểm tổng của $t$.
:::

::: hint
$q_T=(0,1,0,0)^T$ vì $T=\{B\}$. Giải $t=0.8Pt+0.2q_T$. Sau đó dùng $s_p=(r_p-t_p)/r_p$; giữ nguyên mọi giá trị âm.
:::

::: solution
Nghiệm của $t=0.8Pt+0.2q_T$ là

$$t=\left(\frac{66}{245},\frac{263}{735},\frac{116}{735},\frac{158}{735}\right)^T.$$

Vì $66/245=198/735$, tổng bốn thành phần là $(198+263+116+158)/735=1$. Tính từng tỷ số cho

$$\begin{aligned}
s_A&=\frac{1/3-66/245}{1/3}=\frac{47}{245}, &
s_B&=\frac{2/9-263/735}{2/9}=-\frac{299}{490},\\
s_C&=\frac{2/9-116/735}{2/9}=\frac{71}{245}, &
s_D&=\frac{2/9-158/735}{2/9}=\frac{8}{245}.
\end{aligned}$$

Do đó

$$s=\left(\frac{47}{245},-\frac{299}{490},\frac{71}{245},\frac{8}{245}\right)^T.$$

Lưu ý quy ước của đề: $P$ là ma trận chuyển và $r$ là PageRank **không suy giảm ($\beta=1$)**, trong khi $t$ được tính với $\beta=0.8$ — đúng theo nguồn MMDS. Hai đại lượng dùng quy ước khác nhau, nên tỷ số $s_p$ chỉ mang tính minh họa phép tính. Giá trị $s_B<0$ phản ánh TrustRank của hạt giống $B$ lớn hơn PageRank cơ sở ($t_B>r_B$); không kẹp giá trị này về $0$.
:::

Nguồn: [MMDS](http://www.mmds.org), Bài 5.4.2, trang in 204, PDF trang 30.

### 7.3 MMDS 5.5.1 — HITS trên Hình 5.1

**Đề (Bài 5.5.1, tr. 208/PDF 34):** tính điểm trung tâm $h$ và điểm thẩm quyền $a$ cho đồ thị **G4 (Hình 5.1)** — không phải G5 của ví dụ; cạnh C→A giữ nguyên, không có đỉnh E. Đồ thị G4: A→B,C,D; B→A,D; C→A; D→B,C.

Ma trận kề hàng nguồn:

$$L_4=\begin{bmatrix}0&1&1&1\\ 1&0&0&1\\ 1&0&0&0\\ 0&1&1&0\end{bmatrix}$$

**Sản phẩm:** hai vector $h,a$ chuẩn hóa theo phần tử lớn nhất (max 1) và cách tính (lặp hoặc giải ma trận). Gợi ý ngưỡng $\tau=.001$.

::: hint
Cập nhật luân phiên: $a_{\text{thô}}=L_4^T h_{\text{cũ}}$, chuẩn hóa max; rồi $h_{\text{thô}}=L_4 a_{\text{mới}}$, chuẩn hóa max. Khởi $h_0=\mathbf{1}$, $a_0=\mathbf{0}$. Dừng khi cả hai chênh $L_\infty$ giữa hai vòng liên tiếp $\le\tau$.
:::

::: solution
Hai vòng đầu:

| Vòng | $a_{\text{thô}}$ | $a$ | $h_{\text{thô}}$ | $h$ | Trạng thái |
|---|---|---|---|---|---|
| 1 | $(2,2,2,2)$ | $(1,1,1,1)$ | $(3,2,1,2)$ | $(1,\tfrac23,\tfrac13,\tfrac23)$ | cũ→mới |
| 2 | $(1,\tfrac53,\tfrac53,\tfrac53)$ | $(\tfrac35,1,1,1)$ | $(3,\tfrac85,\tfrac35,2)$ | $(1,\tfrac8{15},\tfrac15,\tfrac23)$ | cũ→mới |

Tiếp tục lặp, kết quả làm tròn 4 chữ số:

$$h \approx (1,\,.3919,\,.1028,\,.7108), \qquad a \approx (.2892,\,1,\,1,\,.8136).$$

Trạng thái lặp: với $\tau=.001$, thuật toán dừng sau 11 vòng (chênh cuối $\approx .0007450739557$), cho

$$h \approx (1,\,.392369,\,.103046,\,.710676), \qquad a \approx (.289993,\,1,\,1,\,.814221);$$

với $\tau=10^{-12}$, cần 43 vòng để tiến tới giới hạn nêu trên. Ngưỡng $\tau$ thay đổi điều kiện dừng và do đó số vòng lặp; giá trị sau 11 vòng chưa phải khẳng định về sai số tới nghiệm chính xác. Với hệ nhỏ như này, cách kiểm tra bằng giải hệ ma trận là hợp lệ.
:::

Nguồn: [MMDS](http://www.mmds.org), Bài 5.5.1, tr. 208/PDF 34.

## 8. Chọn mô hình

Dùng PageRank theo chủ đề khi cần một điểm xếp hạng theo tập trang mẫu. Dùng TrustRank và khối lượng rác khi có tập hạt giống đã thẩm định và cần một tín hiệu chẩn đoán liên kết rác. Dùng HITS khi cần tách vai trò trang trung tâm khỏi trang thẩm quyền trên một đồ thị con truy vấn. Không phương pháp nào tự nó chứng minh chất lượng nội dung của một trang.

**Thực hành.** Mã Python, lệnh chạy, khung cài HITS cho sinh viên và kiểm tra tự chạy nằm ở [Bài thực hành](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html). Dùng vết tính tay ở §7 để đối chiếu kết quả chương trình.

Nguồn chính: [Mining of Massive Datasets](http://www.mmds.org), Chương 5, §5.3–5.5; đối chiếu phương pháp lũy thừa: Cornell INFO4300 (Ginsparg, 27/10/2009), [slide 10](https://courses.cit.cornell.edu/info4300_2009fa/slides/16.pdf).
