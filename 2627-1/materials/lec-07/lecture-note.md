# Bài 07 — Chỉ mục hàng xóm gần đúng

Xem bộ trang chiếu tại [Bài 07 — Chỉ mục hàng xóm gần đúng](lecture-07-chi-muc-hang-xom-gan-dung.html).

Bài 06 tìm các cặp tương đồng bên trong một tập. Bài này xét bài toán truy vấn: cho một véc-tơ mới $q$, tìm $K$ véc-tơ gần $q$ nhất trong một kho rất lớn. Ba cấu trúc được trình bày: đồ thị HNSW giảm số véc-tơ phải đo, lượng tử hóa tích (PQ) thay mỗi véc-tơ bằng một mã ngắn, và tệp đảo IVF-PQ chỉ mở một phần kho rồi chấm điểm bằng mã ngắn.

## Mục tiêu và kiến thức tiên quyết

Sau bài này, người học có thể:

- đặc tả bài toán tìm $K$ hàng xóm gần đúng và tính độ thu hồi tại $K$;
- chạy tìm kiếm tham lam, tìm kiếm chùm và `SEARCH-LAYER` trên đồ thị;
- giải thích cách HNSW tổ chức tầng, truy vấn, chèn và cắt cạnh;
- mã hóa véc-tơ bằng lượng tử hóa tích (PQ) và tính khoảng cách bất đối xứng (ADC);
- mô tả IVF-PQ, phân tích chi phí và nhận ra trường hợp thiếu ứng viên;
- so sánh LSH, HNSW, PQ quét đầy đủ và IVF-PQ theo bốn trục chi phí–chất lượng.

Kiến thức tiên quyết gồm khoảng cách Euclid, đồ thị có hướng, hàng đợi ưu tiên, xác suất và $k$-means cơ bản. Bài 05–06 đã trình bày LSH và phân dải; bài này chỉ dùng lại vai trò lọc ứng viên của LSH.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $Y=\{y_1,\dots,y_N\}\subset\mathbb R^D$ | cơ sở dữ liệu véc-tơ |
| $q$ | véc-tơ truy vấn |
| $K$ | số hàng xóm cần trả về, $1\le K\le N$ |
| $N_K(q),\widehat N_K(q)$ | tập đúng và tập gần đúng gồm $K$ hàng xóm |
| $ef$ | giới hạn kích thước tập kết quả động của `SEARCH-LAYER` |
| $M$ | tham số số liên kết của HNSW |
| $m$ | số lượng tử hóa con của PQ; Faiss gọi tham số này là `M` |
| $k^*=2^b$ | số tâm trong mỗi bộ mã con |
| $k_c$ | số tâm thô của IVF |
| $nprobe$ | số danh sách đảo được mở khi truy vấn |

## 1. Truy hồi ngữ nghĩa và bài toán hàng xóm gần nhất

Trong truy hồi ngữ nghĩa, kho văn bản được chia thành các đoạn. Một mô hình nhúng biến mỗi đoạn thành một véc-tơ số thực sao cho hai đoạn có nội dung gần nhau cho hai véc-tơ gần nhau theo một độ đo như tích vô hướng, cosin hoặc khoảng cách Euclid. Câu truy vấn đi qua cùng mô hình để thành véc-tơ $q$. Tìm đoạn liên quan khi đó là tìm các véc-tơ gần $q$ nhất trong kho.

![Mười tỷ đoạn văn bản và câu truy vấn đi qua cùng một mô hình nhúng thành véc-tơ 3072 chiều; kết quả là K đoạn có véc-tơ gần véc-tơ truy vấn q nhất.](img/lec-07/truy-hoi-ngu-nghia.svg)

Nguồn BIODS 271 xét $N=10^{10}$ véc-tơ, mỗi véc-tơ có $D=3072$ tọa độ là số thực 32 bit. Theo hệ thập phân, kho chiếm

$$
N D\cdot4=10^{10}\cdot3072\cdot4\ \text{byte}=122{,}88\ \text{TB},
$$

chưa kể mã định danh. Quét toàn kho cho một truy vấn phải xử lý $ND\approx3{,}07\cdot10^{13}$ tọa độ. Giả sử một máy xử lý $10^{12}$ tọa độ mỗi giây, một truy vấn mất khoảng 30,7 giây, chưa tính thời gian đọc 122,88 TB từ bộ nhớ. Bài này xây các chỉ mục để tránh lượt quét đó.

**Bài toán $K$ hàng xóm gần nhất.** Cho kho $Y=\{y_1,\dots,y_N\}\subset\mathbb R^D$, truy vấn $q\in\mathbb R^D$, hàm khoảng cách $d$ và số nguyên $1\le K\le N$. Tìm đúng trả tập $N_K(q)$ gồm $K$ điểm có $d(q,y)$ nhỏ nhất. Khi hai điểm cách $q$ bằng nhau, điểm có mã định danh nhỏ hơn đứng trước, tức thứ tự xét theo cặp $(d(q,y),\operatorname{id}(y))$; nhờ đó $N_K(q)$ xác định duy nhất.

Quét đầy đủ tính $N$ khoảng cách. Một khoảng cách Euclid xử lý $D$ cặp tọa độ, nên tổng chi phí là $\Theta(ND)$ phép toán trên tọa độ; với $N=10^{10}$ và $D=3072$ là $3{,}07\cdot10^{13}$. Chi phí tuyến tính theo $N$ làm cách này không dùng được cho kho rất lớn.

**Tìm hàng xóm gần đúng (Approximate Nearest Neighbor, ANN)** nới điều kiện của tìm đúng: chỉ mục trả một tập $\widehat N_K(q)$ gồm $K$ điểm, có thể thiếu một số điểm của $N_K(q)$, đổi lại chỉ phải đo một phần kho.

Chất lượng của $\widehat N_K(q)$ được đo bằng độ thu hồi tại $K$:

$$
\operatorname{recall@K}(q)=\frac{|\widehat N_K(q)\cap N_K(q)|}{K}.
$$

Đây là tỷ lệ hàng xóm thật mà chỉ mục tìm lại được. Vì hai tập đều có $K$ phần tử, độ thu hồi bằng 1 khi và chỉ khi chỉ mục trả đúng tập hàng xóm thật. Trên một tập truy vấn, độ thu hồi được lấy trung bình.

::: example Độ thu hồi tại 5
Tập đúng là $\{a,b,c,d,e\}$, chỉ mục trả $\{c,d,e,f,g\}$. Giao có ba phần tử nên $\operatorname{recall@5}=3/5$.
:::

![Tập đúng gồm a, b, c, d, e; tập chỉ mục trả về gồm c, d, e, f, g; phần giao gồm c, d, e.](img/lec-07/do-thu-hoi.svg)

::: exercise Tự kiểm
Với cùng tập đúng, chỉ mục trả $\{a,c,f,g,h\}$. Tính $\operatorname{recall@5}$.
:::

::: solution
Giao là $\{a,c\}$, nên $\operatorname{recall@5}=2/5$.
:::

Các chỉ mục gần đúng đánh đổi chất lượng lấy thời gian và bộ nhớ, nên một con số đơn lẻ không xếp hạng được hai chỉ mục. Phép so sánh đo đồng thời bốn trục và giữ cố định các điều kiện đo.

| Trục | Đại lượng đo | Giữ cố định khi so sánh |
|---|---|---|
| Chất lượng | $\operatorname{recall@K}$ trung bình | tập truy vấn, $K$, tập đúng |
| Truy vấn | độ trễ, số khoảng cách | phần cứng, số luồng |
| Xây dựng | thời gian, dữ liệu huấn luyện | tham số chỉ mục |
| Bộ nhớ | byte mỗi véc-tơ, kể cả cấu trúc chỉ mục | có lưu véc-tơ gốc hay không |

::: exercise Tự kiểm
Chỉ mục A đạt $\operatorname{recall@10}=0{,}9$ với độ trễ 5 ms; B đạt $0{,}7$ với 2 ms. Có thể kết luận B tốt hơn không?
:::

::: solution
Không. B nhanh hơn nhưng tìm lại ít hàng xóm thật hơn. Chỉ chọn được khi biết yêu cầu: với yêu cầu độ thu hồi ít nhất $0{,}85$ thì chọn A; với yêu cầu độ trễ dưới 3 ms thì chọn B.
:::

## 2. Hai cách giảm chi phí truy vấn

Chi phí của một truy vấn xấp xỉ bằng tích hai thừa số:

$$
\text{chi phí}\approx(\text{số véc-tơ được đo})\times(\text{chi phí một phép đo}).
$$

Quét đầy đủ có thừa số thứ nhất bằng $N$ và thừa số thứ hai bằng $\Theta(D)$. Các chỉ mục trong bài giảm một hoặc cả hai thừa số.

- **Giảm số véc-tơ được đo.** LSH (Bài 06) băm $q$ bằng cùng các hàm và chỉ kiểm các véc-tơ cùng thùng. Đồ thị HNSW đi theo cạnh tới vùng gần $q$ và chỉ đo các đỉnh trên đường đi.
- **Giảm chi phí một phép đo và bộ nhớ.** PQ thay mỗi véc-tơ $D$ số thực bằng một mã ngắn vài chục đến vài trăm byte; khoảng cách được tính bằng tra bảng.

Hai hướng không loại trừ nhau. Đồ thị và LSH thường vẫn lưu véc-tơ gốc; PQ dùng một mình vẫn chấm điểm cả $N$ mã. IVF-PQ giảm cả hai thừa số: chỉ mở một phần kho rồi chấm điểm bằng mã PQ. Mọi cấu trúc trên đều đổi một phần độ chính xác lấy thời gian hoặc bộ nhớ.

## 3. Đồ thị lân cận và tìm kiếm tham lam

**Đồ thị lân cận** biểu diễn mỗi véc-tơ bằng một đỉnh; mỗi đỉnh có cạnh có hướng tới một số đỉnh gần nó. Chỉ mục lưu các véc-tơ, danh sách lân cận của mỗi đỉnh và một điểm vào cố định. Khi mỗi mã định danh chiếm 4 byte, bộ nhớ khoảng $N\cdot(\text{kích thước véc-tơ}+4\ \text{byte}\times\text{bậc})$. Đồ thị không thay đổi hàm khoảng cách; nó chỉ quyết định véc-tơ nào được đo. Tìm kiếm bắt đầu từ điểm vào, đo khoảng cách từ $q$ tới các lân cận rồi đi tới đỉnh gần $q$ hơn, nên chỉ các đỉnh trên đường đi được đo.

Ví dụ dưới đây dùng một đồ thị bảy đỉnh do học phần dựng để chạy tay. Vị trí các đỉnh giữ đúng tỷ lệ khoảng cách tới $q$; mỗi đoạn thẳng là hai cạnh có hướng ngược nhau.

![Đồ thị bảy đỉnh e, a, b, s, t, u, z có khoảng cách tới q lần lượt 9, 7, 5, 8, 4, 2, 1; cạnh e–a, a–b, e–s, s–t, t–u, u–z; điểm vào là e.](img/lec-07/do-thi-vi-du.svg)

**Tìm kiếm tham lam.** Ở mỗi bước, thuật toán đo các lân cận của đỉnh hiện tại và sang lân cận gần $q$ nhất nếu lân cận đó gần $q$ hơn đỉnh hiện tại; nếu không, thuật toán dừng. Ký hiệu $e:9$ nghĩa là $d(e,q)=9$.

| Đỉnh hiện tại | Lân cận | Quyết định |
|---|---|---|
| $e:9$ | $a:7,\ s:8$ | sang $a$ |
| $a:7$ | $e:9,\ b:5$ | sang $b$ |
| $b:5$ | $a:7$ | dừng |

![Tìm kiếm tham lam đi từ e qua a tới b có khoảng cách 5 rồi dừng; z có khoảng cách 1 nằm trên nhánh e, s, t, u.](img/lec-07/do-thi-tham-lam.svg)

Đỉnh không có lân cận nào gần $q$ hơn chính nó gọi là **cực tiểu cục bộ**. Điều kiện dừng chỉ kiểm các lân cận trực tiếp, nên tham lam bảo đảm kết quả là cực tiểu cục bộ, không bảo đảm là đỉnh gần $q$ nhất. Ở ví dụ, $b:5$ là cực tiểu cục bộ trong khi $d(z,q)=1$. Nhánh $e\to s$ bị bỏ ngay ở bước đầu vì $s:8$ xa hơn $a:7$, dù chính nhánh này dẫn tới $t:4$, $u:2$, $z:1$.

Thuật toán dừng vì khoảng cách giảm nghiêm ngặt sau mỗi bước và đồ thị hữu hạn. Nếu khoảng cách đã đo được ghi nhớ, ví dụ cần 4 phép đo ($e$; $a$ và $s$; $b$) và không đo $t,u,z$. Đồ thị và khoảng cách do học phần dựng từ cơ chế trong slide Princeton lớp 9, tr.8.

::: exercise Tự kiểm
Điều kiện dừng ở $b$ chứng minh được kết luận nào?
:::

::: solution
$b$ là cực tiểu cục bộ đối với các cạnh đã cho. Điều kiện này không loại trừ một đỉnh tốt hơn ở vùng chưa khám phá.
:::

## 4. Tìm kiếm chùm và `SEARCH-LAYER`

**Tìm kiếm chùm** giữ nhiều hướng thay vì một. Thuật toán duy trì hai tập: $C$ gồm các đỉnh đã thấy nhưng chưa mở, và $W$ gồm tối đa $ef$ đỉnh gần $q$ nhất đã thấy. Mỗi bước mở đỉnh gần $q$ nhất trong $C$. Một lân cận chưa thấy được thêm vào $C$ và $W$ khi $W$ chưa đủ $ef$ phần tử hoặc lân cận đó gần $q$ hơn phần tử xa nhất của $W$; nếu $W$ vượt $ef$ thì bỏ phần tử xa nhất. Thuật toán dừng khi $C$ rỗng hoặc đỉnh sắp mở xa $q$ hơn phần tử xa nhất của $W$.

Trên đồ thị ví dụ với điểm vào $e$ và $ef=3$:

| Mở | $C$ sau bước | $W$ sau bước |
|---|---|---|
| $e$ | $a{:}7,\ s{:}8$ | $a{:}7,\ s{:}8,\ e{:}9$ |
| $a$ | $b{:}5,\ s{:}8$ | $b{:}5,\ a{:}7,\ s{:}8$ |
| $b$ | $s{:}8$ | $b{:}5,\ a{:}7,\ s{:}8$ |
| $s$ | $t{:}4$ | $t{:}4,\ b{:}5,\ a{:}7$ |
| $t$ | $u{:}2$ | $u{:}2,\ t{:}4,\ b{:}5$ |
| $u$ | $z{:}1$ | $z{:}1,\ u{:}2,\ t{:}4$ |
| $z$ | rỗng | $z{:}1,\ u{:}2,\ t{:}4$ |

![Tìm kiếm chùm với ef bằng 3 giữ s trong hàng đợi; khi b không còn lân cận mới, thuật toán mở s rồi đi qua t, u tới z có khoảng cách 1.](img/lec-07/do-thi-chum.svg)

Khi mở $b$, lân cận duy nhất $a$ đã thấy, nhưng $s{:}8$ vẫn nằm trong $C$; đó là nhánh dự phòng mà tham lam đã bỏ. Với $ef=1$, quy tắc trùng tìm kiếm tham lam và dừng ở $b$.

::: exercise Tự kiểm
Chạy lại tìm kiếm chùm trên đồ thị ví dụ với $ef=2$. Thuật toán dừng ở bước nào và trả $W$ nào?
:::

::: solution
Sau khi mở $e$, $W=\{a{:}7,s{:}8\}$ ($e$ bị bỏ vì xa nhất). Mở $a$ thêm $b{:}5$ và bỏ $s$, nên $W=\{b{:}5,a{:}7\}$. Mở $b$ không thêm gì. Đỉnh kế tiếp trong $C$ là $s{:}8$, xa hơn phần tử xa nhất $a{:}7$ của $W$, nên thuật toán dừng và trả $\{b,a\}$. Chùm phải đủ rộng để giữ $s$ trong $W$ thì mới đi tiếp qua nhánh $s$.
:::

**Đặc tả `SEARCH-LAYER`.** Tìm kiếm chùm trên đồ thị ví dụ là trường hợp $ep=\{e\}$, $ef=3$ của thủ tục `SEARCH-LAYER(q, ep, ef, ℓc)` trong bài báo HNSW.

- Đầu vào: truy vấn $q$; bề rộng $ef\ge1$; tập điểm vào $ep$ với $1\le|ep|\le ef$, mọi phần tử thuộc tầng $\ell_c$; tầng $\ell_c$ của đồ thị. Khi chỉ có một đồ thị, $\ell_c=0$; đồ thị nhiều tầng được xét ở mục 5.
- Đầu ra: $W$, tối đa $ef$ đỉnh gần $q$ nhất trong các đỉnh đã thấy.
- Trạng thái: $V$ gồm các đỉnh đã thấy; $C\subseteq V$ gồm các đỉnh chưa mở; $W\subseteq V$.

Điều kiện $1\le|ep|\le ef$ làm phép khởi tạo $W\leftarrow ep$ hợp lệ: $W$ không rỗng nên luôn có phần tử xa nhất, và không vượt $ef$. Đầu ra chỉ nói về các đỉnh đã thấy; vùng chưa phát hiện có thể chứa đỉnh gần $q$ hơn.

![Trạng thái sau khi mở b với ef bằng 3: V gồm e, a, b, s; C gồm s; W gồm b, a, s; C và W là tập con của V.](img/lec-07/search-layer-trang-thai.svg)

```text
SEARCH-LAYER(q, ep, ef, ℓc)
V ← ep;  C ← ep;  W ← ep
while C khác rỗng:
    c ← lấy ra đỉnh gần q nhất trong C
    f ← đỉnh xa q nhất trong W
    if d(c,q) > d(f,q): break
    for y in lân cận của c ở tầng ℓc:
        if y ∉ V:
            thêm y vào V
            f ← đỉnh xa q nhất trong W
            if |W| < ef or d(y,q) < d(f,q):
                thêm y vào C và W
                if |W| > ef: bỏ đỉnh xa q nhất khỏi W
return W
```

Phần tử xa nhất $f$ của $W$ là ngưỡng chấp nhận. Khi $|W|<ef$, đỉnh mới luôn được thêm; khi $W$ đã đủ, chỉ đỉnh gần $q$ hơn $f$ mới được giữ. Ngưỡng phải tính lại trong vòng lặp lân cận vì $W$ có thể đổi sau mỗi lần thêm và bỏ. Ở ví dụ $ef=3$, khi mở $s$ với $W=\{b,a,s\}$: $f=s{:}8$; $t{:}4$ được thêm, $s$ bị bỏ và ngưỡng mới là $f=a{:}7$.

Lệnh `break` chạy khi đỉnh gần nhất còn trong $C$ đã xa $q$ hơn $f$. Khi đó mọi đỉnh của $W$ đều đã được mở, vì một đỉnh của $W$ còn trong $C$ sẽ gần $q$ hơn $c$, trái với cách chọn $c$. Mở tiếp các ứng viên xa hơn vẫn có thể gặp đỉnh tốt hơn; dừng ở đây là đánh đổi để giới hạn số phép đo, nên kết quả là gần đúng. Thuật toán kết thúc vì mỗi đỉnh vào $V$ và $C$ nhiều nhất một lần và tầng hữu hạn.

**Bất biến.** Sau mỗi lần một đỉnh mới vào $V$, $W$ là một tập gồm $\min(ef,|V|)$ đỉnh của $V$ gần $q$ nhất.

- *Khởi tạo:* $V=W=ep$ và $|ep|\le ef$.
- *Duy trì:* khi $|W|<ef$, mọi đỉnh mới đều vào $W$, nên $W=V$. Khi $|W|=ef$, đỉnh mới $y$ hoặc gần $q$ hơn đỉnh xa nhất $f$ của $W$, khi đó $y$ thay $f$ và $W$ là $ef$ đỉnh gần nhất của $V\cup\{y\}$; hoặc không gần hơn, khi đó $y$ không thuộc $ef$ đỉnh gần nhất và $W$ giữ nguyên. Chữ “một tập” xử lý trường hợp hòa khoảng cách.
- *Khi dừng:* $W$ đúng trên $V$, nhưng đỉnh ngoài $V$ không được xét.

Ở lần chạy $ef=2$, thuật toán dừng với $V=\{e,a,s,b\}$ và $W=\{b{:}5,a{:}7\}$, đúng là hai đỉnh gần nhất trong bốn đỉnh đã thấy; $z{:}1$ chưa bao giờ được thấy vì $s$ không được mở.

![Với ef bằng 2 và điểm vào e, thuật toán dừng khi đã thấy e, a, s, b; W gồm b và a; t, u, z chưa được thấy.](img/lec-07/do-thi-ef2.svg)

Bất biến vì vậy không bảo đảm tìm được hàng xóm toàn cục: vùng tốt có thể không nối với phần đã thấy bằng một đường mà thuật toán chọn mở. Trường hợp xấu, thuật toán thăm mọi đỉnh và cạnh của tầng.

::: exercise Tự kiểm
Vì sao tăng $ef$ thường làm tăng độ thu hồi nhưng làm truy vấn tốn hơn?
:::

::: solution
$W$ lớn hơn giữ được nhiều hướng, giảm khả năng cắt sớm một nhánh hữu ích. Đổi lại, thuật toán mở thêm đỉnh và duy trì hàng đợi lớn hơn.
:::

## 5. HNSW: tầng, truy vấn và chèn

**Cạnh dài và cạnh ngắn.** Số phép đo của một lần tìm kiếm xấp xỉ bằng số bước nhân với bậc trung bình của các đỉnh trên đường đi. Trên $N$ điểm của một đường thẳng, nếu chỉ có cạnh giữa hai điểm liền kề thì tham lam từ đầu dãy có thể cần khoảng $N$ bước. Ở ví dụ dưới đây, $q$ nằm giữa $p6$ và $p7$, gần $p6$ hơn: chỉ với cạnh ngắn, tham lam từ $s$ cần 6 bước; thêm cạnh dài $s$–$p4$, $p4$–$p8$, $p8$–$p11$ thì chỉ cần 3 bước $s\to p4\to p5\to p6$. Cạnh dài phải đặt đúng chỗ: nếu chỉ có $p4$–$p8$, tham lam từ $s$ vẫn cần 6 bước.

![Mười hai điểm s, p1 đến p11 trên một đường thẳng, q nằm giữa p6 và p7 gần p6 hơn; chỉ có cạnh ngắn thì tham lam từ s cần 6 bước, thêm cạnh dài s–p4, p4–p8, p8–p11 thì cần 3 bước.](img/lec-07/canh-dai-mot-chieu.svg)

Cạnh dài đưa tìm kiếm tới gần $q$ nhanh; cạnh ngắn tinh chỉnh quanh $q$. Đây là ý tưởng của danh sách nhảy (skip list). HNSW tách cạnh theo thang độ dài vào các tầng khác nhau. Ví dụ một chiều được dựng lại theo slide Princeton lớp 9, tr.11–13.

**Đồ thị nhiều tầng.** Hierarchical Navigable Small World (HNSW) chồng nhiều đồ thị lân cận lên nhau. Tầng 0 chứa mọi điểm với cạnh ngắn; mỗi tầng trên chứa một tập con thưa hơn với cạnh dài hơn. Một điểm có tầng tối đa $\ell$ thì xuất hiện ở mọi tầng $0,\ldots,\ell$. Truy vấn tìm với $ef=1$, tức tìm kiếm tham lam, từ tầng cao nhất; điểm dừng ở mỗi tầng là điểm vào của tầng ngay dưới; ở tầng 0, chùm rộng $efSearch$ được dùng để có nhiều ứng viên tốt.

Trên mười hai điểm của ví dụ một chiều, lấy tầng 1 gồm $s,p2,p4,p6,p8,p10$ và tầng 2 gồm $s,p4,p8$ (do học phần chọn để minh họa). Tầng 2 đi $s\to p4\to p8$; tầng 1 bắt đầu từ $p8$ và sang $p6$; tầng 0 bắt đầu từ $p6$. Tổng cộng 3 bước di chuyển, so với 6 bước khi chỉ có tầng 0.

![Tầng 0 chứa mười hai điểm s, p1 đến p11; tầng 1 chứa s, p2, p4, p6, p8, p10; tầng 2 chứa s, p4, p8. Truy vấn ở tầng 2 đi s, p4, p8; xuống tầng 1 đi từ p8 sang p6; xuống tầng 0 tìm quanh p6.](img/lec-07/do-thi-nhieu-tang.svg)

**Truy vấn HNSW.** Đầu vào gồm $q$, $K$ và bề rộng $efSearch\ge K$; đầu ra là tối đa $K$ đỉnh gần $q$ nhất trong các đỉnh đã thấy ở tầng 0. Điểm vào nằm ở tầng cao nhất $L$.

```text
ep ← điểm vào;  L ← tầng của ep
for ℓc = L, L−1, …, 1:
    W ← SEARCH-LAYER(q, {ep}, 1, ℓc)
    ep ← đỉnh duy nhất của W
W ← SEARCH-LAYER(q, {ep}, efSearch, 0)
return K đỉnh gần q nhất trong W
```

Ở tầng trên, $ef=1$ biến `SEARCH-LAYER` thành tìm kiếm tham lam và $W$ có đúng một đỉnh. Trong ví dụ ba tầng, $ep$ lần lượt là $p8$ (sau tầng 2) và $p6$ (sau tầng 1); tầng 0 tìm quanh $p6$. Điều kiện $efSearch\ge K$ để $W$ có chỗ cho $K$ kết quả; nếu phần đồ thị tới được có ít hơn $K$ đỉnh thì thuật toán trả ít hơn $K$. Thuật toán kết thúc vì có hữu hạn tầng và mỗi lời gọi `SEARCH-LAYER` kết thúc; theo bất biến của `SEARCH-LAYER`, kết quả đúng trên các đỉnh đã thấy ở tầng 0.

**Rút ngẫu nhiên tầng.** Khi chèn một điểm, HNSW lấy $U\sim\mathrm{Uniform}(0,1]$ và gán tầng tối đa

$$
\ell=\left\lfloor-\ln(U)\,m_L\right\rfloor,\qquad m_L>0.
$$

Với số nguyên $k\ge0$, $\ell\ge k$ khi và chỉ khi $U\le e^{-k/m_L}$, nên

$$
\Pr[\ell\ge k]=e^{-k/m_L}=\rho^k,\qquad \rho=e^{-1/m_L}.
$$

Đây là phân phối hình học như trong danh sách nhảy: mỗi tầng giữ khoảng tỷ lệ $\rho$ số điểm của tầng ngay dưới. Kỳ vọng số điểm có $\ell\ge k$ là $N\rho^k$, bằng 1 khi $k=\log_{1/\rho}N$, nên tầng cao nhất xấp xỉ $\log_{1/\rho}N$. Ký hiệu $\rho$ thay cho $p$ của bài báo để khỏi trùng tên điểm $p1,\ldots,p11$. Miền $(0,1]$ tránh $\ln 0$; mọi điểm thuộc tầng 0 vì $\ell\ge0$.

::: example Tầng với $m_L=1/\ln 16$
Khi đó $\rho=1/16$: tầng 1 chứa khoảng $1/16$ số điểm, tầng 2 khoảng $1/256$. Với $N=10^{10}$, tầng cao nhất xấp xỉ $\log_{16}10^{10}\approx8{,}3$.
:::

Bài báo chọn $m_L=1/\ln M$, với $M$ là số lân cận được nối cho mỗi điểm mới (định nghĩa ở thao tác chèn); khi đó $\rho=1/M$. Đây là lựa chọn thực nghiệm, không phải điều kiện để thuật toán đúng.

**Chèn một điểm.** Chèn điểm mới $x$ là truy vấn chính $x$, rồi nối $x$ với các đỉnh gần nó ở từng tầng mà $x$ thuộc về. Ví dụ: chèn $x$ ở tọa độ $2{,}6$ vào đồ thị ba tầng ở trên, với tầng rút được $\ell=1$, nối $M=2$ lân cận và bề rộng chùm khi chèn `efConstruction` bằng 3. Khoảng cách tới $x$: $p3$ 0,4; $p2$ 0,6; $p4$ 1,4; $p1$ 1,6; $s$ 2,6.

| Tầng | Tìm từ | Kết quả |
|---|---|---|
| 2 | $s$, $ef=1$ | $ep=p4$; không thêm cạnh |
| 1 | $p4$, $ef=3$ | $W=\{p2,p4,s\}$; nối $x$ với $p2,p4$ |
| 0 | $p2,p4,s$, $ef=3$ | $W=\{p3,p2,p4\}$; nối $x$ với $p3,p2$ |

![Điểm mới x ở tọa độ 2,6 có tầng 1, M bằng 2; pha 1 ở tầng 2 đi từ s tới p4; pha 2 nối x với p2 và p4 ở tầng 1, với p3 và p2 ở tầng 0.](img/lec-07/chen-vi-du.svg)

Giả mã chèn theo Thuật toán 1 của bài báo:

```text
ℓ ← ⌊−ln(U)·mL⌋;  ep ← điểm vào;  L ← tầng của ep
for ℓc = L, L−1, …, ℓ+1:                      // pha 1
    ep ← đỉnh gần x nhất trong SEARCH-LAYER(x, {ep}, 1, ℓc)
for ℓc = min(L,ℓ), …, 0:                      // pha 2
    W ← SEARCH-LAYER(x, ep, efConstruction, ℓc)
    R ← chọn M lân cận cho x từ W
    nối x với mỗi đỉnh của R theo hai chiều ở tầng ℓc
    với mỗi e ∈ R có bậc vượt Mmax(ℓc): cắt lân cận của e
    ep ← W
if ℓ > L: đặt x làm điểm vào
```

Tham số: $M$ là số lân cận nối cho $x$; `efConstruction` là bề rộng chùm khi chèn, chọn $\ge M$; $M_{\max}$ ở các tầng trên và $M_{\max,0}$ ở tầng 0 là bậc tối đa, cả hai ít nhất bằng $M$; bài báo đề xuất $M_{\max,0}=2M$. Nếu chỉ mục rỗng, $x$ được tạo ở các tầng $0,\ldots,\ell$ và trở thành điểm vào. Pha 1 chạy ở các tầng cao hơn $\ell$, nơi $x$ không xuất hiện, nên chỉ tìm điểm vào. Ở pha 2, $ep$ là một tập: kết quả $W$ của tầng trên làm tập điểm vào của tầng dưới. Mỗi đầu mút tự cắt danh sách của mình, nên quan hệ kề có thể không còn đối xứng dù bước nối là hai chiều. Ở ví dụ, sau khi nối, $p2,p4$ ở tầng 1 và $p3,p2$ ở tầng 0 đều có bậc 3, nên với $M_{\max}=3$, $M_{\max,0}=4$ không có cắt.

**Chọn lân cận đa dạng.** Chọn đúng $M$ đỉnh gần $x$ nhất có thể tạo nhiều cạnh cùng một hướng. Quy tắc đa dạng của bài báo (Thuật toán 4) xét ứng viên $y$ theo $d(y,x)$ tăng dần và chỉ nhận $y$ khi

$$
d(y,x)<d(y,r)\qquad\text{với mọi lân cận }r\text{ đã chọn}.
$$

::: example Chọn hai lân cận cho $x$
Ví dụ hai chiều: $x=(0;0)$, $c1=(2;0{,}3)$, $c2=(2{,}6;0{,}9)$, $c3=(2{,}4;-0{,}6)$, $c4=(-3;0{,}5)$, $M=2$. Trên ví dụ một chiều, hai cách chọn cho cùng kết quả nên ví dụ được đổi sang hai chiều. Theo thứ tự $d(\cdot,x)$: $c1$ 2,0; $c3$ 2,5; $c2$ 2,8; $c4$ 3,0. Quy tắc nhận $c1$; loại $c3$ vì $d(c3,c1)\approx1{,}0<2{,}5$; loại $c2$ vì $d(c2,c1)\approx0{,}8<2{,}8$; nhận $c4$ vì $d(c4,c1)\approx5{,}0>3{,}0$. Kết quả $\{c1,c4\}$ ở hai phía của $x$, trong khi chọn hai đỉnh gần nhất cho $\{c1,c3\}$ cùng một phía.
:::

![Điểm mới x có bốn ứng viên: c1, c2, c3 cùng một phía, c4 ở phía đối diện; chọn hai đỉnh gần nhất cho c1 và c3, quy tắc đa dạng cho c1 và c4.](img/lec-07/lan-can-da-dang.svg)

Một ứng viên gần một lân cận đã chọn hơn gần $x$ thì cạnh tới nó không mở hướng mới. Quy tắc giữ cạnh tới nhiều hướng, giúp đồ thị liên thông giữa các cụm. Đây là tiêu chí cục bộ, không phải tối ưu toàn cục. Quy tắc thay cho dòng “chọn $M$ lân cận” trong giả mã chèn và cũng được dùng khi cắt bậc. Hai tùy chọn của Thuật toán 4 (mở rộng ứng viên bằng lân cận của chúng; bổ sung ứng viên bị loại khi chưa đủ $M$) nằm ngoài phạm vi bài này.

## 6. Tham số, bộ nhớ và giới hạn HNSW

| Tham số | Dùng khi | Tăng tham số thì |
|---|---|---|
| $M$ | chèn | nhiều cạnh hơn: tốn bộ nhớ, mỗi lần mở đỉnh đo nhiều lân cận hơn; điều hướng thường tốt hơn |
| `efConstruction` | chèn | xây chậm hơn; lân cận được chọn từ nhiều ứng viên hơn |
| `efSearch` | truy vấn | độ trễ tăng; độ thu hồi thường tăng |

$M$ và `efConstruction` quyết định đồ thị khi xây, nên đổi chúng phải xây lại chỉ mục; `efSearch` đổi được cho từng truy vấn. Các xu hướng trong bảng là quan sát thực nghiệm của bài báo HNSW (mục 4.1), không phải bảo đảm đơn điệu cho mọi dữ liệu. Bài báo cho biết $M$ gần tối ưu thường nằm trong khoảng 6–48.

**Bộ nhớ.** Mỗi điểm lưu véc-tơ $D$ số thực 4 byte và danh sách lân cận ở mỗi tầng nó thuộc về: tối đa $M_{\max,0}$ lân cận ở tầng 0 và $M_{\max}$ ở mỗi tầng trên. Theo phân phối tầng, kỳ vọng số tầng trên của một điểm là $\sum_{k\ge1}\rho^k=\rho/(1-\rho)$. Bài báo HNSW ước lượng phần cạnh bằng $(M_{\max,0}+m_L M_{\max})$ nhân số byte mỗi liên kết; hai cách cho cùng cỡ vài trăm byte mỗi điểm.

::: example Bộ nhớ cho mười tỷ véc-tơ
Giả định $N=10^{10}$, $D=3072$, $M=16$, $M_{\max,0}=32$, $M_{\max}=16$, $\rho=1/16$. Vì $10^{10}>2^{32}$, mã định danh cần 8 byte. Véc-tơ gốc: $4\cdot3072=12\,288$ byte mỗi điểm, $122{,}88$ TB toàn kho. Cạnh: kỳ vọng tối đa $32+16\cdot\tfrac{1/16}{15/16}\approx33{,}1$ liên kết, khoảng 265 byte mỗi điểm, $2{,}65$ TB toàn kho. Véc-tơ gốc chiếm khoảng 98% bộ nhớ.
:::

**Truy vấn và xây dựng.** Số phép đo của một truy vấn xấp xỉ số bước nhân bậc trung bình trên đường đi. Bài báo chứng minh số phép đo tăng theo $\log N$ dưới giả thiết mỗi tầng là đồ thị Delaunay chính xác và bậc trung bình bị chặn bởi hằng số (mục 4.2.1); điều này đúng với dữ liệu Euclid ngẫu nhiên số chiều thấp, còn bậc của đồ thị Delaunay tăng nhanh theo số chiều. Đồ thị thực tế chỉ xấp xỉ, nên kết luận không là cận cho mọi dữ liệu. Đồ thị kém, tham số nhỏ hoặc dữ liệu bất lợi có thể làm tìm kiếm thăm cả tầng. Xây chỉ mục gồm $N$ lần chèn, mỗi lần một lượt tìm với bề rộng `efConstruction`.

HNSW giảm số phép đo nhưng vẫn giữ toàn bộ véc-tơ gốc. Giảm bộ nhớ đòi hỏi biểu diễn véc-tơ gọn hơn; đó là nội dung của lượng tử hóa ở mục sau.

::: exercise Tự kiểm
Muốn giảm độ trễ mà không xây lại chỉ mục, nên điều chỉnh tham số nào? Rủi ro là gì?
:::

::: solution
Giảm `efSearch`. Truy vấn mở ít đỉnh hơn nhưng có thể bỏ lỡ hàng xóm đúng, làm độ thu hồi giảm.
:::

## 7. Lượng tử hóa véc-tơ và lượng tử hóa tích

**Lượng tử hóa véc-tơ (VQ)** thay mỗi véc-tơ bằng chỉ số của tâm gần nó nhất trong một bộ mã $C=\{c_0,\dots,c_{k-1}\}\subset\mathbb R^D$; mã dài $\lceil\log_2 k\rceil$ bit. Khi cần, véc-tơ được tái dựng bằng tâm tương ứng:

$$
i(x)=\arg\min_{0\le i<k}\|x-c_i\|^2,\qquad \widehat x=c_{i(x)}.
$$

Đây là nén mất dữ liệu: sai số tái dựng $\|x-\widehat x\|^2$ đo mức mất thông tin, và không đồng nhất với độ thu hồi của truy vấn. Các điểm cùng mã tạo thành một ô của không gian.

::: example Ba tâm trong mặt phẳng
$C=\{(0;0),(2;0),(0;2)\}$, $x=(1{,}7;\ 0{,}4)$. Bình phương khoảng cách tới ba tâm là $3{,}05$; $0{,}25$; $5{,}45$, nên mã là 1 (2 bit), $\widehat x=c_1=(2;0)$ và sai số $0{,}25$. Ranh giới các ô là các đường “tọa độ thứ nhất bằng 1”, “tọa độ thứ hai bằng 1” và “hai tọa độ bằng nhau”.
:::

![Ba tâm c0 tại (0, 0), c1 tại (2, 0), c2 tại (0, 2) chia mặt phẳng thành ba ô; điểm x tại (1,7; 0,4) nằm trong ô của c1.](img/lec-07/luong-tu-hoa-vec-to.svg)

::: exercise Tự kiểm
Với cùng bộ mã, tính mã và sai số tái dựng của $y=(0{,}6;\ 1{,}5)$.
:::

::: solution
Bình phương khoảng cách: $2{,}61$; $4{,}21$; $0{,}61$. Mã 2, $\widehat y=c_2=(0;2)$, sai số $0{,}61$.
:::

**Đặc tả và chi phí.** Đầu vào là $x\in\mathbb R^D$ và bộ mã $C$ đã học; khi hòa, chọn chỉ số nhỏ hơn. Đầu ra là mã $i(x)$ dài $\lceil\log_2 k\rceil$ bit, với điều kiện sau: không tâm nào gần $x$ hơn $c_{i(x)}$. Bộ mã thường được học bằng k-means trên một tập huấn luyện: xen kẽ gán mỗi điểm cho tâm gần nhất và dời mỗi tâm về trọng tâm các điểm được gán. Hai điều kiện Lloyd này là cần, không đủ, nên k-means chỉ cho cực tiểu cục bộ của sai số bình phương trung bình. Mã hóa một véc-tơ cần $k$ khoảng cách, tức $\Theta(kD)$ phép toán; lưu bộ mã cần $kD$ số. Cả hai tỷ lệ với $k$.

**Giới hạn của một bộ mã lớn.** Sai số tái dựng giảm khi tăng số tâm $k$, nên véc-tơ nhiều chiều cần mã dài. Bài báo PQ xét véc-tơ SIFT $D=128$ chiều với mã 64 bit, tức chỉ 0,5 bit mỗi tọa độ: một bộ mã duy nhất cần $k=2^{64}\approx1{,}8\cdot10^{19}$ tâm. Lưu bộ mã cần $kD\cdot4\approx9{,}4\cdot10^{21}$ byte, mã hóa một véc-tơ cần khoảng $2{,}4\cdot10^{21}$ phép toán, và k-means cần nhiều hơn $k$ điểm huấn luyện. Thêm 1 bit mã làm $k$ gấp đôi, nên mã dài với một bộ mã duy nhất là không khả thi; cần cách tạo mã dài từ các bộ mã nhỏ.

**Lượng tử hóa tích (Product Quantization, PQ)** tạo mã dài từ $m$ bộ mã nhỏ. Véc-tơ $x\in\mathbb R^D$ được chia thành $m$ đoạn $x^{(1)},\ldots,x^{(m)}$ bằng nhau, mỗi đoạn $D/m$ chiều, nên cần $m\mid D$. Đoạn $j$ có bộ mã con riêng gồm $k^*=2^b$ tâm, học bằng k-means trên đoạn tương ứng của tập huấn luyện. Mã PQ là $(i_1,\ldots,i_m)$, dài $mb$ bit; véc-tơ tái dựng ghép các tâm con:

$$
\widehat x=\big(c^{(1)}_{i_1},\ldots,c^{(m)}_{i_m}\big).
$$

Mã hóa là $m$ phép gán tâm độc lập, mỗi phép $\Theta(k^*D/m)$, tổng $\Theta(k^*D)$. Ví dụ $D=8$, $m=4$, $k^*=256$: mỗi chỉ số 8 bit, mã 32 bit. Bài báo dùng $m$ cho số đoạn; Faiss gọi tham số này là `M`, khác $M$ của HNSW.

![Véc-tơ tám chiều chia thành bốn đoạn hai chiều; mỗi đoạn được mã hóa bằng bộ mã con 256 tâm thành một chỉ số 8 bit; mã PQ là bộ bốn chỉ số, dài 32 bit.](img/lec-07/pq-tach-doan.svg)

::: example Mã hóa PQ với hai đoạn
$D=4$, $m=2$, $k^*=2$. Bộ mã đoạn 1 gồm tâm 0 $=(0;2)$ và tâm 1 $=(2;0)$; bộ mã đoạn 2 gồm tâm 0 $=(0;0)$ và tâm 1 $=(3;0)$. Với $x=(0{,}2;\ 1{,}8\mid 2{,}7;\ 0{,}1)$, bình phương khoảng cách ở đoạn 1 là $0{,}08$ và $6{,}48$, ở đoạn 2 là $7{,}30$ và $0{,}10$. Mã là $(0,1)$, dài 2 bit; $\widehat x=(0;\ 2\mid 3;\ 0)$ và sai số tái dựng $0{,}08+0{,}10=0{,}18$, vì bình phương khoảng cách cộng theo đoạn.
:::

![Đoạn 1 có tâm 0 tại (0; 2) và tâm 1 tại (2; 0), x gần tâm 0; đoạn 2 có tâm 0 tại (0; 0) và tâm 1 tại (3; 0), x gần tâm 1; mã của x là (0, 1).](img/lec-07/pq-vi-du.svg)

**Kích thước mã và bộ mã.** Mã PQ dài $mb$ bit, tức $\lceil mb/8\rceil$ byte. Số véc-tơ tái dựng khác nhau là $(k^*)^m$, nhưng $m$ bộ mã con chỉ chứa $m\cdot k^*\cdot D/m=k^*D$ số. So với VQ cùng độ dài mã 64 bit và $D=128$:

| | VQ, $k=2^{64}$ | PQ, $m=8$, $k^*=256$ |
|---|---|---|
| Số mã khác nhau | $2^{64}$ | $256^8=2^{64}$ |
| Bộ mã | $2^{64}\cdot128$ số | $256\cdot128=32\,768$ số |
| Mã hóa một véc-tơ | $\Theta(2^{64}\cdot128)$ | $\Theta(32\,768)$ |

PQ đạt cùng số mã với bộ mã nhỏ hơn rất nhiều lần, vì không gian mã là tích của $m$ không gian nhỏ. Cơ sở dữ liệu $N$ mã cần $N\lceil mb/8\rceil$ byte.

::: example Kho mười tỷ véc-tơ
Cấu hình của nguồn BIODS: $D=3072$, đoạn 6 chiều nên $m=512$; $k^*=256$ nên $b=8$. Mỗi mã dài $512\cdot8$ bit $=512$ byte và $10^{10}$ mã chiếm $5{,}12$ TB, nhỏ hơn 24 lần so với $122{,}88$ TB dữ liệu gốc. Chưa tính mã định danh, bộ mã ($256\cdot3072$ số) và cấu trúc chỉ mục.
:::

PQ tạo sai số tái dựng $\|x-\widehat x\|^2$. Tăng $m$ hoặc $b$ thường giảm sai số, đồng thời làm mã, bảng tra hoặc thời gian huấn luyện lớn hơn.

::: exercise Tự kiểm
Với $m=4$ và $b=8$, một mã dài bao nhiêu byte và biểu diễn bao nhiêu tổ hợp tâm?
:::

::: solution
Mã dài 4 byte và biểu diễn $(2^8)^4=2^{32}$ tổ hợp tâm.
:::

## 8. ADC, bảng tra và chi phí PQ

**Khoảng cách bất đối xứng (Asymmetric Distance Computation, ADC)** giữ truy vấn $q$ ở dạng đầy đủ, còn véc-tơ $y$ trong kho (ở ví dụ dưới đây là $x$) chỉ có mã $(i_1(y),\ldots,i_m(y))$. Khoảng cách được ước lượng bằng khoảng cách tới véc-tơ tái dựng:

$$
\widetilde d(q,y)^2=\|q-\widehat y\|^2=\sum_{j=1}^{m}\big\|q^{(j)}-c^{(j)}_{i_j(y)}\big\|^2.
$$

Đẳng thức thứ hai đúng vì bình phương khoảng cách Euclid là tổng theo tọa độ và các đoạn chia tọa độ thành các nhóm rời nhau. Số hạng đoạn $j$ chỉ phụ thuộc $q^{(j)}$ và chỉ số $i_j(y)\in\{0,\ldots,k^*-1\}$, nên với một truy vấn, mỗi đoạn chỉ có $k^*$ giá trị số hạng khác nhau.

::: example Khoảng cách bất đối xứng trên ví dụ PQ hai đoạn
Véc-tơ $x=(0{,}2;\ 1{,}8\mid 2{,}7;\ 0{,}1)$ chỉ còn mã $(0,1)$: tâm $(0;2)$ ở đoạn 1 và $(3;0)$ ở đoạn 2. Với $q=(0{,}1;\ 1{,}9\mid 2{,}5;\ 0{,}2)$, hai số hạng là $0{,}1^2+(-0{,}1)^2=0{,}02$ và $(-0{,}5)^2+0{,}2^2=0{,}29$, nên ước lượng là $0{,}31$. Giá trị đúng $\|q-x\|^2=0{,}02+0{,}05=0{,}07$: ADC đo khoảng cách tới véc-tơ tái dựng, nên sai lệch phụ thuộc sai số tái dựng của $x$. Phép tính chỉ cần mã của $x$ và các bộ mã con.
:::

![Hai mặt phẳng con của ví dụ PQ: x gần tâm 0 ở đoạn 1 và tâm 1 ở đoạn 2; truy vấn q ở (0,1; 1,9) và (2,5; 0,2).](img/lec-07/pq-vi-du-adc.svg)

**Bảng tra khoảng cách.** Vì mỗi đoạn chỉ có $k^*$ giá trị số hạng, với một truy vấn ta lập trước bảng $T[j,i]=\|q^{(j)}-c^{(j)}_i\|^2$ gồm $m\times k^*$ ô; chấm mã $(i_1,\ldots,i_m)$ bằng $\sum_j T[j,i_j]$. Trên ví dụ hai đoạn:

| $T$ | tâm 0 | tâm 1 |
|---|---|---|
| đoạn 1 | **0,02** | 7,22 |
| đoạn 2 | 6,29 | **0,29** |

Mã $(0,1)$ chọn hai ô in đậm, cho $0{,}02+0{,}29=0{,}31$; mã $(1,0)$ cho $7{,}22+6{,}29=13{,}51$.

| Việc | Chi phí |
|---|---|
| Lập bảng, mỗi truy vấn | $m\cdot k^*\cdot D/m=k^*D$ phép toán trên tọa độ; lưu $mk^*$ số |
| Chấm một mã | $m$ lần tra, $m-1$ phép cộng |
| Tính trực tiếp | $\Theta(D)$ mỗi véc-tơ |

Bảng được dùng lại cho mọi mã trong kho, nên đáng lập khi số mã cần chấm lớn hơn nhiều $k^*$. Với $D=3072$, $m=512$, chấm một mã cần 512 lần tra thay vì xử lý 3072 tọa độ. Quét đủ $N$ mã tốn $\Theta(Nm)$, chưa kể chọn $K$ kết quả tốt nhất.

Phép tính khoảng cách đối xứng (Symmetric Distance Computation, SDC) lượng tử hóa cả truy vấn rồi tra khoảng cách giữa hai tâm con, nên thêm sai số do lượng tử hóa truy vấn. Theo bài báo PQ, ưu điểm duy nhất của SDC là truy vấn cũng được lưu ở dạng mã; ADC có sai lệch khoảng cách thấp hơn với độ phức tạp tương tự. Bài này dùng ADC.

**Giới hạn của PQ quét đầy đủ.** Với kho mười tỷ véc-tơ và mã 512 đoạn, mỗi truy vấn vẫn chấm cả $10^{10}$ mã:

| Một truy vấn | Quét véc-tơ gốc | Quét mã PQ |
|---|---|---|
| Dữ liệu đọc | $122{,}88$ TB | $5{,}12$ TB |
| Phép toán | $ND\approx3{,}07\cdot10^{13}$ lượt tọa độ | $Nm=5{,}12\cdot10^{12}$ lần tra |
| Số véc-tơ được chấm | $10^{10}$ | $10^{10}$ |

Bảng bỏ qua chi phí lập bảng tra ($k^*D\approx7{,}9\cdot10^5$ phép toán) và việc giữ $K$ kết quả tốt nhất; các số là phép suy ra từ cấu hình, không phải số đo. PQ giảm chi phí mỗi phép đo, không giảm số véc-tơ được chấm.

::: exercise Tự kiểm
Với $10^{12}$ lần tra mỗi giây, quét mã PQ cho một truy vấn mất bao lâu? So với quét véc-tơ gốc ở cùng tốc độ.
:::

::: solution
$5{,}12\cdot10^{12}/10^{12}=5{,}12$ giây, so với khoảng 30,7 giây khi quét véc-tơ gốc. Vẫn quá chậm vì cả $10^{10}$ mã đều được chấm; cần chỉ mở một phần kho.
:::

## 9. Tệp đảo và IVF-PQ

**Tệp đảo (Inverted File, IVF)** là một lượng tử hóa thô với $k_c$ tâm $\mu_0,\ldots,\mu_{k_c-1}$ dùng để chia kho thành $k_c$ ô; danh sách đảo $L_i$ chứa mã định danh của các véc-tơ gần $\mu_i$ nhất. Truy vấn chỉ mở $nprobe$ danh sách có tâm gần $q$ nhất và chỉ chấm các phần tử trong đó. IVF giảm số véc-tơ được chấm; ghép với PQ thành IVF-PQ, trong đó mỗi phần tử của danh sách lưu mã định danh và một mã PQ ngắn, nên mỗi lần chấm cũng rẻ. Bài báo PQ gọi $k_c$ là $k'$ và $nprobe$ là $w$; Faiss dùng `nlist` và `nprobe`.

::: example Bốn danh sách đảo
Bốn tâm thô $\mu_0=(2;2)$, $\mu_1=(8;2)$, $\mu_2=(2;8)$, $\mu_3=(8;8)$ chia mười sáu điểm $y_1,\ldots,y_{16}$ thành bốn danh sách, mỗi danh sách bốn điểm: $L_0=\{y_1,\ldots,y_4\}$, $L_1=\{y_5,\ldots,y_8\}$, $L_2=\{y_9,\ldots,y_{12}\}$, $L_3=\{y_{13},\ldots,y_{16}\}$. Truy vấn $q=(6;3{,}5)$ gần $\mu_1$ nhất rồi đến $\mu_0$; với $nprobe=2$, chỉ 8 trên 16 phần tử được chấm.
:::

![Bốn tâm thô μ0 đến μ3 chia mặt phẳng thành bốn ô ứng với bốn danh sách đảo; truy vấn q gần μ1 nhất rồi đến μ0; với nprobe bằng 2 chỉ L1 và L0 được mở.](img/lec-07/tep-dao.svg)

Quy trình IVF-PQ:

1. Học $k_c$ tâm thô $\mu_0,\dots,\mu_{k_c-1}$.
2. Gán $y$ vào tâm gần nhất $i(y)$ và lưu mã PQ của phần dư $r(y)=y-\mu_{i(y)}$ trong $L_{i(y)}$.
3. Với $q$, chọn tập $P$ gồm $nprobe$ tâm thô gần nhất.
4. Với mỗi $i\in P$, lập bảng ADC riêng cho $\widetilde q_i=q-\mu_i$, rồi chấm các mã trong $L_i$.
5. Gộp ứng viên và trả về tối đa $K$ phần tử có điểm nhỏ nhất.

![IVF-PQ chọn các tâm thô gần truy vấn, mở các danh sách tương ứng và chấm mã phần dư bằng ADC.](img/lec-07/ivfpq-flow.svg)

Số kết quả không thể vượt

$$
\min\left(K,\sum_{i\in P}|L_i|\right).
$$

Nếu danh sách được mở chứa ít hơn $K$ véc-tơ, thuật toán không thể trả đủ $K$ định danh phân biệt.

Chi phí truy vấn, chưa kể duy trì top-$K$, gồm

$$
\Theta(k_cD)+\Theta(nprobe\,k^*D)+\Theta\left(m\sum_{i\in P}|L_i|\right).
$$

Ba số hạng lần lượt là tìm tâm thô, lập bảng ADC và chấm mã. Chỉ khi các danh sách tương đối cân bằng mới có thể xấp xỉ

$$
\sum_{i\in P}|L_i|\approx nprobe\frac{N}{k_c}.
$$

Tăng $nprobe$ thường tăng recall và độ trễ. $nprobe$ là số danh sách, không phải số ứng viên.

::: exercise Tự kiểm
Một truy vấn mở hai danh sách có 3 và 4 phần tử, còn $K=10$. Số kết quả tối đa là bao nhiêu?
:::

::: solution
Tối đa $\min(10,3+4)=7$. Muốn có thể trả đủ 10, cần mở thêm danh sách hoặc xử lý trường hợp thiếu ứng viên.
:::

## 10. So sánh bốn cơ chế

Không có cấu trúc thắng trên mọi khối lượng công việc.

| Cơ chế | Nguồn ứng viên | Chi phí chính | Bộ nhớ nổi bật | Rủi ro chất lượng |
|---|---|---|---|---|
| LSH | ngăn băm | số bảng, ngăn và hậu kiểm | bảng băm, định danh | điểm gần không va chạm |
| HNSW | đường đi đồ thị | số đỉnh và cạnh được thăm | véc-tơ, liên kết | kẹt ở vùng đồ thị kém |
| PQ quét đủ | toàn bộ mã | $\Theta(Nm)$ | mã $Nmb$ bit, bộ mã | sai số lượng tử hóa |
| IVF-PQ | danh sách được mở | tâm thô, bảng ADC, mã ứng viên | danh sách và mã | bỏ sót danh sách đúng |

Khối lượng công việc ưu tiên recall có thể chấp nhận `efSearch` hoặc $nprobe$ lớn. Khi bộ nhớ bị giới hạn, PQ có thể phù hợp hơn, nhưng phải tính cả định danh, bộ mã và khả năng giữ véc-tơ gốc. Quyết định chỉ có ý nghĩa khi nêu rõ ngưỡng chất lượng và ngân sách.

## 11. Thực hành với runbook Princeton

Ba nhiệm vụ dưới đây dùng trực tiếp notebook `class-08-runbook-for-students.ipynb`. Không điền sẵn kết quả chạy vì số đo phụ thuộc môi trường.

### Chuẩn bị

Chạy các ô 0–4, 17 và 21–24 để tạo `d=64`, tập huấn luyện `xt`, cơ sở dữ liệu `xb`, truy vấn `xq` và chuẩn đúng `gt`. Ghi lại seed và môi trường.

### Nhiệm vụ 1: tái dựng PQ thủ công

Làm các ô 82–97 với bộ lượng tử hóa tích có $d=64$, $m=4$, $b=8$. Tại chỉ số 123, dùng bốn chỉ số mã để lấy bốn tâm con rồi ghép thành véc-tơ tái dựng; không gọi `decode`. Nộp mã, véc-tơ tái dựng, sai số bình phương và đoạn mã ghép.

### Nhiệm vụ 2: cùng ngân sách 6 byte

Làm các ô 98–99 với $M\in\{4,8,16\}$ và `nbits=48/M`. Ba cấu hình lần lượt là $4\times12$, $8\times6$ và $16\times3$ bit; tất cả đều dùng 48 bit, tức 6 byte mỗi véc-tơ. Báo cáo `dsub`, `ksub`, sai số tái dựng trung bình và thời gian huấn luyện/mã hóa. Không trộn phần này với cấu hình $4\times8$ bit ở nhiệm vụ 1.

### Nhiệm vụ 3: điều chỉnh IVF-PQ

Làm các ô 148–155 với chuỗi nguồn `IVF200,PQ16x8np` và thử $nprobe\in\{2,5,10,20,50\}$. Không diễn giải hậu tố `np` thành giá trị `nprobe`; notebook đặt `nprobe` riêng sau khi tạo chỉ mục.

Với mỗi giá trị, báo cáo `nok/|xq|` và tổng thời gian tìm kiếm theo mili giây. Trong notebook, `nok/|xq|` đo độ chính xác hạng 1: kết quả đầu tiên có trùng chuẩn đúng đầu tiên hay không. Nó không tự động bằng recall@K tổng quát. Không gọi tổng thời gian của cả lô là độ trễ mỗi truy vấn.

## 12. Tự kiểm cuối bài

1. Viết đặc tả ANN sao cho tập đúng vẫn xác định khi hòa khoảng cách.
2. Phân biệt điều kiện dừng tham lam với bảo đảm tối ưu toàn cục.
3. Nêu bất biến của `SEARCH-LAYER` và giới hạn của nó.
4. Giải thích vai trò riêng của $M$, `efConstruction` và `efSearch`.
5. Tính độ dài mã PQ khi biết $m$ và $b$; phân biệt mã với bộ mã.
6. Giải thích vì sao IVF-PQ cần bảng ADC riêng cho mỗi danh sách được mở.
7. Nêu điều kiện để dùng xấp xỉ $nprobe\,N/k_c$.
8. Lập bảng đo bốn trục để so sánh hai cấu hình trên cùng khối lượng công việc.

## Tài liệu tham khảo

- Stanford BIODS 271, bài 12, *Approximate Nearest Neighbor Search*.
- Princeton COS 597A, lớp 8, *Quantization*, và notebook thực hành đi kèm.
- Princeton COS 597A, lớp 9, *Graph Indexes*.
- Yu. A. Malkov và D. A. Yashunin, *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs*.
- H. Jégou, M. Douze và C. Schmid, *Product Quantization for Nearest Neighbor Search*.
- J. Leskovec, A. Rajaraman và J. D. Ullman, *Mining of Massive Datasets*, Chương 3.
