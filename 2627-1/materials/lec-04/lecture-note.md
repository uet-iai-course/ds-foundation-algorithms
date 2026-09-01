# Bài 04 — PageRank theo chủ đề, liên kết rác và HITS

Tài liệu bám theo **MMDS §5.3–5.5** (Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman, *Mining of Massive Datasets*). Nguồn trục: [http://www.mmds.org](http://www.mmds.org). Bài học liên kết tới slide [`lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html`](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html).

## 1. Cầu nối từ Bài 03

Bài 03 đã xây PageRank cổ điển trên toàn đồ thị $G=(V,E)$, với $n=|V|$, $m_G=|E|$. Ma trận chuyển $P$ là ma trận cột ngẫu nhiên đã xử lý nút cụt. Vòng lặp cập nhật

$$r^{(u+1)}=\beta P r^{(u)}+(1-\beta)v$$

với $0<\beta<1$ và $v$ là phân phối dịch chuyển. Số hạng $(1-\beta)v$ đưa khối lượng ra khỏi các bẫy liên kết. Phương trình điểm bất động $r=\beta Pr+(1-\beta)v$ có nghiệm duy nhất vì toán tử là phép co trong chuẩn $L_1$.

Bài 04 xử lý ba giới hạn của điểm xếp hạng toàn cục:

1. PageRank theo chủ đề thay phân phối dịch chuyển để ưu tiên một chủ đề.
2. Phân tích cụm thao túng liên kết giải thích cách cấu trúc nhân tạo dồn hạng; TrustRank và khối lượng rác cung cấp tín hiệu chống thao túng.
3. HITS tách điểm trang trung tâm và trang thẩm quyền trên một đồ thị con truy vấn.

Trong bài này, HITS dùng một ma trận khác với $P$: dùng $L\in\{0,1\}^{n\times n}$ với $L_{ij}=1$ khi $i\to j$. Vậy hàng của $L$ là nguồn của cạnh, cột là đích. Không đồng nhất $L$ với $P$; $P$ là ma trận xác suất chuyển (dựa trên cột), còn $L$ chỉ là cấu trúc liên kết thô.

## 2. PageRank theo chủ đề — MMDS §5.3.1–5.3.3

### 2.1 Vai trò

PageRank cổ điển cho một thứ hạng toàn cục, còn truy vấn có thể cần ưu tiên một chủ đề. Chọn tập khác rỗng $S\subseteq V$ làm tập trang mẫu. PageRank theo chủ đề thay phân phối dịch chuyển đều bằng phân phối chỉ đặt khối lượng lên $S$; liên kết sau đó truyền tín hiệu này sang các trang lân cận.

### 2.2 Đặc tả

Chọn một chủ đề hẹp $S\subseteq V$ khác rỗng, đặt tín hiệu

$$q_S=\frac{e_S}{|S|}$$

trong đó $(e_S)_i=1$ nếu $i\in S$ và $0$ nếu không, tức $q_S$ là phân phối đều trên các phần tử của $S$. Vòng lặp:

$$r^{(u+1)}=\beta P r^{(u)}+(1-\beta)q_S.$$

Khi $S=V$ ta thu được PageRank cổ điển vì $q_V$ là phân phối đều. Với tập $S$ nhỏ hơn, $q_S$ neo khối lượng dịch chuyển vào các phần tử của $S$ trước khi liên kết truyền khối lượng sang phần còn lại của đồ thị.

Tính chất hội tụ. Định nghĩa toán tử $F_S(x)=\beta Px+(1-\beta)q_S$. Với hai vector $x,y$ bất kỳ:

$$\|F_S(x)-F_S(y)\|_1\le\beta\|x-y\|_1.$$

Đây là phép co chuẩn $L_1$ với hệ số $\beta<1$. Vì vậy vòng lặp hội tụ tới một điểm bất động duy nhất, độc lập với phân phối khởi tạo.

### 2.3 Ví dụ chạy tay — Hình 5.15

Xét đồ thị trên Hình 5.15 với thứ tự $(A,B,C,D)$ và cạnh:

- $A\to B,C,D$;
- $B\to A,D$;
- $C\to A$;
- $D\to B,C$.

Ma trận chuyển cột tương ứng:

$$P=\begin{bmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{bmatrix}.$$

Kiểm tra: cột B ứng với $B\to A,D$ nên $P_{B}=(1/2,0,0,1/2)$, cột C ứng với $C\to A$ nên $P_C=(1,0,0,0)$, cột D ứng với $D\to B,C$ nên $P_D=(0,1/2,1/2,0)$.

Chọn $S=\{B,D\}$, $\beta=0{,}8$. Khởi đầu $r^{(0)}=q_S=(0,1/2,0,1/2)^T$. Tính vòng 1:

$$\beta P r^{(0)}=(0{,}8)\,P\,(0,1/2,0,1/2)^T.$$

Cột B (trọng $1/2$) cộng cột D (trọng $1/2$):

$$P r^{(0)}=\frac12\begin{bmatrix}1/2\\0\\0\\1/2\end{bmatrix}+\frac12\begin{bmatrix}0\\1/2\\1/2\\0\end{bmatrix}=\begin{bmatrix}1/4\\1/4\\1/4\\1/4\end{bmatrix}.$$

Nhân với $\beta=0{,}8$:

$$\beta P r^{(0)}=\left(\frac{2}{10},\frac{2}{10},\frac{2}{10},\frac{2}{10}\right)^T.$$

Phần dịch chuyển: $(1-\beta)q_S=0{,}2\cdot(0,1/2,0,1/2)^T=(0,1/10,0,1/10)^T$. Vậy:

$$r^{(1)}=\left(\frac{2}{10},\frac{3}{10},\frac{2}{10},\frac{3}{10}\right)^T.$$

So với $q_S$, khối lượng đã được phân tán từ B và D ra các trang chúng trỏ tới (A, D, B, C); chính B và D vẫn giữ giá trị cao nhất nhờ phần dịch chuyển trực tiếp. Điều này chỉ ra vai trò của $q_S$: giữ tín hiệu chủ đề qua các vòng.

::: example
Trong Ví dụ 5.10, phần theo cạnh phân đều khối lượng lên bốn trang, còn phần dịch chuyển chỉ thêm $1/10$ vào $B$ và $D$. Vì vậy $B,D$ có hạng $3/10$, cao hơn $A,C$ với hạng $2/10$ sau vòng đầu.
:::

### 2.4 Chi phí và giới hạn

Nếu lưu $k$ chủ đề, mỗi chủ đề cần một vector riêng kích thước $n$, tổng bộ nhớ $\Theta(kn)$. Cho một vòng cập nhật đầy đủ cả $k$ chủ đề, ta nhân $P$ (có $m_G$ cạnh khác không) với mỗi vector rồi cộng phần dịch chuyển, tổng công việc $\Theta(k(n+m_G))$.

Có thể phối hợp nhiều chủ đề qua tổ hợp lồi. Cho trọng số $\alpha_1,\dots,\alpha_k\ge0$ với $\sum_\ell\alpha_\ell=1$. Đặt

$$r=\sum_\ell\alpha_\ell r^{(S_\ell)}.$$

Vì mỗi $r^{(S_\ell)}$ là một phân phối (tổng bằng $1$ và không âm), tổ hợp lồi $r$ cũng là một phân phối. Đó là điểm quan trọng khi muốn kết hợp nhiều chủ đề.

::: example
Giả sử $r^{(S_1)}$ và $r^{(S_2)}$ là hai phân phối đã tính. Với $\alpha_1=0{,}6$ và $\alpha_2=0{,}4$, vector $0{,}6r^{(S_1)}+0{,}4r^{(S_2)}$ vẫn không âm và có tổng bằng $1$.
:::

MMDS dùng danh mục DMOZ gồm 16 chủ đề trong Ví dụ 5.9 để minh họa việc chuẩn bị một số ít vector. Đây là bối cảnh của ví dụ, không phải mô tả một hệ thống hiện thời. Trong bài này, tập $S$ là dữ liệu đầu vào.

**Tự kiểm.** Thay $S$ bằng $V$ trong công thức cập nhật và chỉ ra vì sao ta thu lại PageRank với dịch chuyển đều. Bài 7.1 kiểm tra việc thay $S$ trên cùng một đồ thị.

## 3. Cụm thao túng liên kết — MMDS §5.4.1–5.4.2

### 3.1 Vai trò

Một người thao túng có thể dựng mạng liên kết nhân tạo để nâng PageRank của trang đích. Tập trang hỗ trợ được tạo cho mục đích này gọi là **cụm thao túng liên kết** (spam farm). Mô hình dưới đây tính phần hạng mà cấu trúc ấy dồn vào trang đích $t$.

### 3.2 Mô hình và đặc tả

Chia toàn bộ web thành ba vùng theo mức độ truy cập của người vận hành spam farm:

1. **Trang không tiếp cận được**: người thao túng không thể thay đổi liên kết.
2. **Trang có thể tác động**: người thao túng có thể chèn liên kết tới trang đích.
3. **Trang sở hữu**: người vận hành kiểm soát toàn bộ, gồm cả trang đích $t$.

Các biến:

- $N$: tổng số trang web.
- $q$: số trang hỗ trợ trong spam farm.
- $x$: tổng đóng góp từ ngoài vào đích $t$, đã gồm nhân $\beta$.
- $y$: PageRank của đích $t$.

Cả $q$ và $N$ đều có thể thay đổi khi tăng $q$ (thêm trang hỗ trợ cũng tăng $N$, có thể thay cả $x$), nên cần thận trọng khi diễn dịch.

Cấu trúc đồ thị trong Hình 5.16: mỗi trang hỗ trợ chỉ trỏ tới $t$; $t$ trỏ tới cả $q$ trang hỗ trợ.

![Sơ đồ hai cụm spam farm: mỗi trang hỗ trợ (dưới) trỏ tới một trang đích t (trên), và t trỏ lại tất cả q trang hỗ trợ.](img/lec-04/hinh-5-16-cum-thao-tung.svg)

### 3.3 Hạng của mỗi trang hỗ trợ

Gọi $z$ là hạng của mỗi một trong $q$ trang hỗ trợ. Do cấu trúc đối xứng, mọi trang hỗ trợ có cùng $z$.

Mỗi trang hỗ trợ nhận đóng góp từ $t$ qua phần $\beta P r$, rồi cộng phần dịch chuyển đều $(1-\beta)/N$. Vì $t$ trỏ tới cả $q$ trang hỗ trợ và hạng của $t$ là $y$, mỗi trang hỗ trợ nhận $y/q$ qua cạnh rồi nhân $\beta$:

$$z=\beta\frac{y}{q}+\frac{1-\beta}{N}.$$

![Luồng hạng từ trang ngoài vào đích t, rồi tuần hoàn giữa t và q trang hỗ trợ.](img/lec-04/luong-hang-trong-cum.svg)

Công thức dựa trên phép co: trang hỗ trợ không nhận gì từ các trang hỗ trợ khác (chúng chỉ trỏ tới $t$), vậy nguồn vào duy nhất là $t$ và phần dịch chuyển.

::: derivation
Tại một trang hỗ trợ, đóng góp từ $t$ qua một trong $q$ cạnh là $\beta y/q$. Cộng phần dịch chuyển đều $(1-\beta)/N$ cho $z=\beta y/q+(1-\beta)/N$.
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

::: derivation
Từ $y=x+\beta qz+(1-\beta)/N$, thay biểu thức của $z$ rồi gom $y$ về một vế:

$$y(1-\beta^2)=x+\frac{(1-\beta)(\beta q+1)}{N}.$$

Chia cho $(1-\beta^2)=(1-\beta)(1+\beta)$ thu được công thức chính xác ở trên.
:::

Sách (MMDS §5.4.2) đưa ra một biểu thức đơn giản hơn bằng cách bỏ số hạng phần dịch chuyển trực tiếp vào $t$ trước khi giải:

Theo dạng xấp xỉ trong sách,

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\cdot\frac{q}{N}.$$

Sai số so với biểu thức chính xác:

$$\frac{1}{N(1+\beta)}.$$

Đây là phần dịch chuyển trực tiếp vào $t$ đã bị bỏ. Xấp xỉ hợp lý khi $1/[N(1+\beta)]$ nhỏ so với các số hạng được giữ. Không được suy luận rằng có thể tăng $q$ tùy ý trong khi giữ mọi đại lượng khác cố định: thêm trang hỗ trợ làm đổi $N$ và có thể đổi cả $x$.

::: example
**Ví dụ 5.11.**

Với $\beta=0{,}85$,

$$\frac{1}{1-\beta^2}=\frac{1}{0{,}2775}\approx3{,}6036,
\qquad \frac{\beta}{1+\beta}=\frac{0{,}85}{1{,}85}\approx0{,}4595.$$

Dạng xấp xỉ của sách là $y\approx3{,}6036x+0{,}4595q/N$.
:::

### 3.5 Giới hạn của mô hình

Mô hình giả sử mỗi trang hỗ trợ chỉ trỏ tới $t$, còn $t$ trỏ đều tới cả $q$ trang hỗ trợ. Công thức không mô tả mọi cấu trúc thao túng. Hơn nữa, $q<N$ và việc thêm trang hỗ trợ làm đổi $N$, có thể đổi cả đóng góp ngoài $x$. MMDS §5.4.3 dùng sự thích nghi qua lại giữa người thao túng và bộ máy tìm kiếm để dẫn sang cách tiếp cận dựa trên tập trang tin cậy.

**Tự kiểm.** Gán tên nguồn hạng cho bốn số hạng trong phương trình trước khi gom $y$: $x$, $\beta^2y$, $\beta q(1-\beta)/N$ và $(1-\beta)/N$.

## 4. TrustRank và khối lượng rác — MMDS §5.4.3–5.4.5

### 4.1 Vai trò

Liên kết có thể bị thao túng, nên TrustRank thay tập trang theo chủ đề bằng tập trang đã được thẩm định. Khối lượng rác sau đó đo độ chênh tương đối giữa PageRank và TrustRank của từng trang.

TrustRank chạy trên toàn đồ thị, dùng tín hiệu $q_T$ và trả một điểm tin cậy cho mỗi trang.

### 4.2 Đặc tả

Cho $T\subseteq V$ khác rỗng, đặt $q_T=e_T/|T|$ và:

$$t^{(0)}=q_T,\qquad t^{(u+1)}=\beta P t^{(u)}+(1-\beta)q_T.$$

Công thức co $L_1$ tương tự PageRank chủ đề, xác định duy nhất điểm bất động.

Chọn seed: chọn ứng viên có PageRank cao rồi thẩm định thủ công, hoặc chọn các miền có cơ chế thành viên. Không coi hậu tố miền là chứng nhận tuyệt đối. Kết quả TrustRank phụ thuộc độ phủ của seed và sai số chọn seed.

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

- PageRank **không hệ số giảm**: $r=(3/9,2/9,2/9,2/9)^T$.
- TrustRank với $\beta=0{,}8$, $T=\{B,D\}$: $t=(54,59,38,59)^T/210$.

Khối lượng rác tương ứng là $(8/35,-37/140,13/70,-37/140)^T$. Chẳng hạn, tại $A$:

$$s_A=\frac{3/9-54/210}{3/9}=\frac{8}{35}\approx0{,}229.$$

Hai vector trong hình dùng hai quy ước khác nhau, nên ví dụ chỉ minh họa phép tính tỷ số. Khi dùng khối lượng rác để so sánh trong ứng dụng, phải tính PageRank và TrustRank với cùng $\beta$ và cùng quy ước xử lý nút cụt.

**Tự kiểm.** Tính lại $s_B$ và giải thích vì sao kết quả âm không phải lỗi. Bài 7.2 thay tập tin cậy bằng $T=\{B\}$.

## 5. HITS — MMDS §5.5.1–5.5.2

### 5.1 Vai trò

HITS (Hyperlink-Induced Topic Search) xếp hạng trong một đồ thị con cố định lấy từ kết quả truy vấn. MMDS Ví dụ 5.13 mô tả danh sách học phần như một trang trung tâm và trang của từng học phần như trang thẩm quyền. Mỗi trang vẫn có cả hai điểm:

- **Điểm thẩm quyền** (authority) $a_i$: cao khi được các trang trung tâm có điểm cao trỏ tới.
- **Điểm trung tâm** (hub) $h_i$: cao khi trỏ tới các trang thẩm quyền có điểm cao.

Trực quan: hub là "trang tìm đường", authority là "trang nội dung". Hai vai trò củng cố lẫn nhau: một hub tốt trỏ tới những authority tốt, và một authority tốt được những hub tốt trỏ tới.

![Trực quan hai vai trò HITS: hub hướng tới các authority; các authority được đánh giá qua các hub trỏ tới nó.](img/lec-04/cap-vai-tro-hits.svg)

### 5.2 Hai phép cập nhật luân phiên

Cho đồ thị con với ma trận $L\in\{0,1\}^{n\times n}$ hàng nguồn: $L_{ij}=1$ nếu $i\to j$.

HITS thực hiện hai bước luân phiên:

- **Thẩm quyền thô**: $a_{\text{thô}}=L^Th$. Thành phần $i$ bằng tổng $h_j$ của mọi trang $j$ trỏ tới $i$.
- **Trung tâm thô**: $h_{\text{thô}}=La$. Thành phần $i$ bằng tổng $a_j$ của mọi trang $j$ mà $i$ trỏ tới.

Sau mỗi phép nhân, chia cho chuẩn vô cùng.

::: derivation
Phần tử $(L^Th)_i=\sum_jL_{ji}h_j$. Vì $L_{ji}=1$ khi $j\to i$, đây là tổng điểm hub của các trang trỏ tới $i$. Tương tự, $(La)_i=\sum_jL_{ij}a_j$ là tổng điểm authority của các trang mà $i$ trỏ tới.
:::

::: derivation
Về đại số, $a\propto L^TLa$ và $h\propto LL^Th$. Trong tính toán, không dựng $L^TL$ hay $LL^T$ vì tích có thể đặc. Ta giữ hai phép nhân thưa nối tiếp, mỗi vòng có chi phí $\Theta(n+m_G)$.
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

$A$ có điểm hub lớn nhất sau hai vòng; $B$ và $C$ có điểm authority lớn nhất.

![Ma trận L hàng nguồn của Hình 5.18 dùng để tính hai vòng đầu HITS.](img/lec-04/hinh-5-18.svg)

### 5.4 Đặc tả làm chặt của học phần

Để minh họa tính chất hội tụ, học phần áp dụng một đặc tả bổ sung. Cho $K_{\max}\ge1$, $0<\tau<1$, khởi đầu $h=e$, $a=0$. Tại mỗi vòng:

1. Tính $a_{\text{thô}}=L^Th$. Nếu $\|a_{\text{thô}}\|_\infty=0$, trả $(0_n,0_n)$ kèm cờ suy biến; nếu không, chuẩn hóa thành $a_{\text{mới}}$.
2. Tính $h_{\text{thô}}=La_{\text{mới}}$. Nếu $\|h_{\text{thô}}\|_\infty=0$, trả kết quả suy biến; nếu không, chuẩn hóa thành $h_{\text{mới}}$.
3. Nếu $\max(\|a_{\text{mới}}-a\|_\infty,\|h_{\text{mới}}-h\|_\infty)\le\tau$, trả cờ hội tụ.
4. Hết $K_{\max}$ mà chưa đạt ngưỡng thì trả cờ hết ngân sách.

Chuẩn vô cùng, ngưỡng $\tau$, cờ suy biến và cờ hết ngân sách là phần đặc tả bổ sung của học phần.

Nếu một vector thô có chuẩn vô cùng bằng $0$, thuật toán trả hai vector $0_n$ và bật cờ suy biến thay vì thực hiện phép chia cho $0$.

```text
h ← e; a ← 0_n
cho u từ 1 đến K_max:
    a_thô ← L^T h
    nếu ||a_thô||_∞ = 0: trả (0_n, 0_n, sai, đúng, u)
    a_mới ← a_thô / ||a_thô||_∞
    h_thô ← L a_mới
    nếu ||h_thô||_∞ = 0: trả (0_n, 0_n, sai, đúng, u)
    h_mới ← h_thô / ||h_thô||_∞
    nếu max(||a_mới-a||_∞, ||h_mới-h||_∞) ≤ tau:
        trả (h_mới, a_mới, đúng, sai, u)
    (h, a) ← (h_mới, a_mới)
trả (h, a, sai, sai, K_max)
```

Qua hai phép cập nhật, ta có $a\propto L^TLa$ và $h\propto LL^Th$. Vì vậy $a$ và $h$ lần lượt tiến theo các hướng riêng trội của $L^TL$ và $LL^T$ khi các điều kiện phổ bên dưới được thỏa.

::: proof
Đây là phác thảo có điều kiện. Phân rã vector khởi đầu theo các hướng riêng của $L^TL$ hoặc $LL^T$. Nếu trị riêng trội theo trị tuyệt đối là duy nhất và thành phần của khởi đầu trên hướng đó khác $0$, lũy thừa của toán tử khuếch đại thành phần trội nhanh hơn các thành phần còn lại. Chuẩn hóa sau mỗi vòng loại hệ số độ lớn, nên hướng của dãy tiến tới hướng riêng trội.
:::

MMDS chỉ phát biểu hội tụ dưới các giả thiết phù hợp. Hướng giới hạn là duy nhất khi hướng riêng trội phù hợp tồn tại và khởi đầu $h=e$ có thành phần khác $0$ trên hướng đó.

### 5.5 Chi phí và giới hạn

Mỗi vòng gồm hai phép nhân (thưa) và hai lần lấy cực đại (chuẩn hóa):

- Công việc: $\Theta(n+m_G)$ mỗi vòng.
- Bộ nhớ: $\Theta(n+m_G)$ trên đồ thị con.

HITS chạy trên đồ thị con cố định, nên kết quả phụ thuộc cách chọn đồ thị con. Nếu hướng riêng trội không duy nhất hoặc khởi tạo không có thành phần trên hướng đó, bảo đảm hội tụ về một hướng duy nhất không áp dụng.

**Tự kiểm.** Với Hình 5.18, giải thích vì sao $E$ có điểm hub bằng $0$ sau vòng đầu nhưng vẫn có điểm authority dương. Bài 7.3 kiểm tra HITS trên Hình 5.1.

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
| Chi phí | $\Theta(n)$ | $\Theta(n+m_G)$ mỗi vòng |

- PageRank theo chủ đề và TrustRank dùng cùng mô hình vòng lặp co $L_1$, chi phí mỗi vòng giống nhau; khác nhau ở đối tượng $q$ (chủ đề so với tin cậy).
- Khối lượng rác không chạy vòng lặp mới: chỉ tính $s_p=(r_p-t_p)/r_p$ trên mỗi trang, với chi phí $\Theta(n)$ và điều kiện $r_p>0$.
- HITS chạy trên đồ thị con, $\Theta(n+m_G)$ mỗi vòng với hai phép nhân thưa.

## 7. Ba bài tập MMDS

### 7.1 MMDS 5.3.1 — PageRank theo chủ đề trên Hình 5.15

::: exercise
Trên đồ thị Hình 5.15, giữ $\beta=0{,}8$ như Ví dụ 5.10. Tính PageRank theo chủ đề khi: (a) $S=\{A\}$; (b) $S=\{A,C\}$. Sản phẩm gồm hai vector điểm bất động theo thứ tự $(A,B,C,D)$ và phép kiểm tổng bằng $1$.
:::

::: hint
Với $S=\{A\}$, dùng $q_S=(1,0,0,0)^T$. Với $S=\{A,C\}$, dùng $q_S=(1/2,0,1/2,0)^T$. Trong từng trường hợp, giải $r=0{,}8Pr+0{,}2q_S$ cùng điều kiện $e^Tr=1$.
:::

::: solution
Với $S=\{A\}$, nghiệm là

$$r=\left(\frac37,\frac4{21},\frac4{21},\frac4{21}\right)^T.$$

Tổng các thành phần bằng $3/7+3(4/21)=1$. Với $S=\{A,C\}$, nghiệm là

$$r=\left(\frac{27}{70},\frac6{35},\frac{19}{70},\frac6{35}\right)^T.$$

Tổng bằng $(27+12+19+12)/70=1$. Trong cả hai trường hợp, thay vector vào $r-0{,}8Pr=0{,}2q_S$ cho đúng phần dư dịch chuyển.
:::

![Đồ thị Hình 5.15, cùng cấu trúc với Hình 5.1, gồm bốn trang A, B, C, D và không đánh dấu tập dịch chuyển.](img/lec-04/hinh-5-1-trung-tinh.svg)

Nguồn: MMDS Bài 5.3.1, trang in 199, PDF trang 25.

### 7.2 MMDS 5.4.2 — TrustRank và khối lượng rác

::: exercise
Trên đồ thị Hình 5.1 theo thứ tự $(A,B,C,D)$, giả sử chỉ $B$ là trang tin cậy và $\beta=0{,}8$. PageRank cơ sở không hệ số giảm là

$$P=\begin{bmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{bmatrix},
\qquad r=\left(\frac13,\frac29,\frac29,\frac29\right)^T.$$

Tính TrustRank của mỗi trang, rồi tính khối lượng rác. Sản phẩm gồm vector $t$, vector $s$ và phép kiểm tổng của $t$.
:::

::: hint
$q_T=(0,1,0,0)^T$ vì $T=\{B\}$. Giải $t=0{,}8Pt+0{,}2q_T$. Sau đó dùng $s_p=(r_p-t_p)/r_p$; giữ nguyên mọi giá trị âm.
:::

::: solution
Nghiệm của $t=0{,}8Pt+0{,}2q_T$ là

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

Giá trị $s_B<0$ phản ánh TrustRank của hạt giống $B$ lớn hơn PageRank cơ sở; không kẹp giá trị này về $0$.
:::

Nguồn: MMDS Bài 5.4.2, trang in 204, PDF trang 30.

### 7.3 MMDS 5.5.1 — HITS trên Hình 5.1

::: exercise
Tính điểm hub và điểm authority của các trang trong Hình 5.1. Với thứ tự $(A,B,C,D)$, ma trận liên kết hàng nguồn là

$$L=\begin{bmatrix}0&1&1&1\\1&0&0&1\\1&0&0&0\\0&1&1&0\end{bmatrix}.$$

Khởi tạo $h^{(0)}=e$, chuẩn hóa theo chuẩn vô cùng sau mỗi phép nhân. Báo hai vòng đầu và hai vector khi sai khác lớn nhất giữa hai vòng liên tiếp không quá $10^{-3}$.
:::

::: hint
Mỗi vòng tính $a_{\text{thô}}=L^Th$, chuẩn hóa thành $a_{\text{mới}}$, rồi tính $h_{\text{thô}}=La_{\text{mới}}$ và chuẩn hóa. Giữ phân số trong hai vòng đầu để kiểm phép nhân.
:::

::: solution
Vòng đầu cho

$$a^{(1)}=(1,1,1,1)^T,\qquad
h^{(1)}=\left(1,\frac23,\frac13,\frac23\right)^T.$$

Ở vòng hai, $L^Th^{(1)}$ tỷ lệ với $(3,5,5,5)^T$, nên

$$a^{(2)}=\left(\frac35,1,1,1\right)^T.$$

Tiếp theo, $La^{(2)}$ tỷ lệ với $(15,8,3,10)^T$, nên

$$h^{(2)}=\left(1,\frac8{15},\frac15,\frac23\right)^T.$$

Lặp tiếp cho hai hướng gần đúng

$$h=(1;\ 0{,}391944;\ 0{,}102775;\ 0{,}710831),$$

$$a=(0{,}289169;\ 1;\ 1;\ 0{,}813607).$$

Vì vậy $A$ có điểm hub lớn nhất, còn $B$ và $C$ có điểm authority lớn nhất.
:::

Nguồn: MMDS Bài 5.5.1, trang in 208, PDF trang 34.

## 8. Chọn mô hình

Dùng PageRank theo chủ đề khi cần một điểm xếp hạng theo tập trang mẫu. Dùng TrustRank và khối lượng rác khi có tập hạt giống đã thẩm định và cần một tín hiệu chẩn đoán liên kết rác. Dùng HITS khi cần tách vai trò trang trung tâm khỏi trang thẩm quyền trên một đồ thị con truy vấn. Không phương pháp nào tự nó chứng minh chất lượng nội dung của một trang.

Nguồn chính: [Mining of Massive Datasets](http://www.mmds.org), Chương 5, §5.3–5.5.
