# Bài 07 — Chỉ mục hàng xóm gần đúng

Xem bộ trang chiếu tại [Bài 07 — Chỉ mục hàng xóm gần đúng](../../lecture-07-chi-muc-hang-xom-gan-dung.html).

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

## 1. Từ quy mô dữ liệu đến đặc tả ANN

Nguồn BIODS 271 xét $N=10^{10}$ véc-tơ, mỗi véc-tơ có $D=3072$ số thực 32 bit. Dữ liệu thô chiếm

$$
N D\cdot4=10^{10}\cdot3072\cdot4=122{,}88\ \text{TB}.
$$

Nếu mỗi đoạn có 6 chiều thì có $m=3072/6=512$ đoạn. Vì mỗi đoạn có $k^*=256$ tâm nên chỉ số tâm cần $P_c=8$ bit; mã PQ dài 512 byte. Toàn bộ mã chiếm

$$
N\frac{mb}{8}=10^{10}\cdot512=5{,}12\ \text{TB}.
$$

Đây là phép suy ra từ cấu hình nguồn, chưa tính định danh, bộ mã, chỉ mục hoặc véc-tơ gốc. Nén giảm mạnh bộ nhớ, nhưng quét đủ vẫn phải chấm điểm $N$ mã.

![Kho mười tỷ véc-tơ 3072 chiều: dữ liệu số thực cần 122,88 TB, còn mã PQ gồm 512 đoạn 8 bit cần 5,12 TB.](img/lec-07/quy-mo-vector.svg)

Đầu vào bài toán là $Y$, truy vấn $q$, hàm khoảng cách $d$ và số nguyên $K$. Đầu ra gồm $K$ mã định danh phân biệt. Khi hai điểm cách $q$ bằng nhau, ta phá hòa theo $(d(q,y),\operatorname{id}(y))$. Nhờ đó tập đúng $N_K(q)$ được xác định duy nhất.

Quét đầy đủ tính khoảng cách từ $q$ đến mọi điểm. Với khoảng cách Euclid tốn $\Theta(D)$ cho mỗi điểm, tổng chi phí là $\Theta(ND)$.

Chỉ mục gần đúng trả về $\widehat N_K(q)$, không nhất thiết trùng với $N_K(q)$. Độ thu hồi tại $K$ là

$$
\operatorname{recall@K}(q)=\frac{|\widehat N_K(q)\cap N_K(q)|}{K}.
$$

Nếu hai tập có năm phần tử và ba phần tử chung thì $\operatorname{recall@5}=3/5$.

![Hai tập năm phần tử có ba phần tử chung nên độ thu hồi tại năm bằng ba phần năm.](img/lec-07/ann-recall.svg)

Một phép so sánh chỉ mục cần giữ cố định tập truy vấn, chuẩn đúng, phần cứng, số luồng và chính sách lưu véc-tơ gốc, rồi đo ít nhất bốn trục.

| Trục | Đại lượng tiêu biểu |
|---|---|
| Chất lượng | recall@K |
| Truy vấn | độ trễ, số phép tính khoảng cách |
| Xây dựng | thời gian và dữ liệu huấn luyện |
| Bộ nhớ | byte mỗi véc-tơ và phụ phí chỉ mục |

::: exercise Tự kiểm
Chỉ mục A đạt recall@10 bằng 0,9 với độ trễ 5 ms; B đạt 0,7 với độ trễ 2 ms. Có thể kết luận B tốt hơn không?
:::

::: solution
Không. B nhanh hơn nhưng thu hồi thấp hơn. Chưa thể xếp hạng khi chưa nêu yêu cầu chất lượng và điều kiện đo.
:::

## 2. Ba cách cắt chi phí

LSH, đồ thị lân cận và lượng tử hóa tác động vào ba phần khác nhau của phép tìm kiếm.

- LSH tạo ngăn ứng viên bằng hàm băm nhạy cảm cục bộ, sau đó hậu kiểm.
- HNSW tạo đường đi trên đồ thị để tránh thăm phần lớn đỉnh.
- PQ thay véc-tơ cơ sở dữ liệu bằng dãy chỉ số tâm để giảm bộ nhớ và chi phí chấm điểm.

Ba cơ chế đều đánh đổi độ chính xác lấy tài nguyên, nhưng không thay thế nhau theo một thứ tự cố định. IVF-PQ còn ghép lọc ứng viên với mã nén.

## 3. Tìm kiếm tham lam và cực tiểu cục bộ

Đồ thị lân cận giữ nguyên hàm khoảng cách; nó chỉ thay cách chọn véc-tơ cần đo. Mỗi đỉnh là một véc-tơ và cạnh dẫn đến các đỉnh lân cận hữu ích.

Xét khoảng cách đến $q$. Từ $e:9$, hai lân cận là $a:7$ và $s:8$. Thuật toán tham lam luôn đi đến lân cận gần $q$ nhất nếu lân cận đó tốt hơn đỉnh hiện tại.

| Bước | Đỉnh hiện tại | Lân cận | Quyết định |
|---|---|---|---|
| 0 | $e:9$ | $a:7, s:8$ | sang $a$ |
| 1 | $a:7$ | $b:5$ | sang $b$ |
| 2 | $b:5$ | $a:7$ | dừng |

Điều kiện dừng chỉ nói không có lân cận trực tiếp nào tốt hơn $b$. Nó không chứng minh $b$ gần $q$ nhất toàn cục. Nhánh qua $s$ có thể dẫn đến $t:4$, $u:2$ rồi $z:1$, nhưng tìm kiếm tham lam không mở nhánh đó. Ví dụ này được dựng lại từ cơ chế trong slide Princeton lớp 9.

![Tìm kiếm tham lam đi từ e qua a đến b và bỏ lỡ nhánh s, t, u dẫn đến z gần truy vấn hơn.](img/lec-07/greedy-beam.svg)

::: exercise Tự kiểm
Điều kiện dừng ở $b$ chứng minh được kết luận nào?
:::

::: solution
$b$ là cực tiểu cục bộ đối với các cạnh đã cho. Điều kiện này không loại trừ một đỉnh tốt hơn ở vùng chưa khám phá.
:::

## 4. Tìm kiếm chùm và `SEARCH-LAYER`

Tìm kiếm chùm giữ nhiều hướng có triển vọng. Với ví dụ trên và $ef=3$, tập làm việc có thể lần lượt chứa $\{e\}$, $\{a,s\}$, rồi $\{t:4,b:5,a:7\}$ sau khi mở $a$ và $s$. Nhờ giữ nhánh $s$, thuật toán còn đường đến $u$ và $z$.

`SEARCH-LAYER(q,ep,ef,ℓ)` dùng ba tập: $C$ là hàng đợi ứng viên chưa mở; $W$ giữ tối đa $ef$ đỉnh tốt nhất đã gặp; $V$ giữ các đỉnh đã thăm.

```text
SEARCH-LAYER(q, ep, ef, tầng ℓ)
    V ← {ep}; C ← {ep}; W ← {ep}
    while C không rỗng
        c ← đỉnh gần q nhất trong C; bỏ c khỏi C
        f ← đỉnh xa q nhất trong W
        if d(c,q) > d(f,q): break
        for mỗi e thuộc lân cận của c ở tầng ℓ
            if e chưa thuộc V
                thêm e vào V
                f ← đỉnh xa q nhất trong W
                if |W| < ef hoặc d(e,q) < d(f,q)
                    thêm e vào C và W
                    nếu |W| > ef, bỏ đỉnh xa q nhất khỏi W
    return W
```

Khi $|W|<ef$, đỉnh mới luôn được thêm. Khi $W$ đã đầy, chỉ đỉnh tốt hơn phần tử xa nhất mới được giữ.

![SEARCH-LAYER duy trì tập ứng viên C, tập kết quả động W và tập đã thăm V.](img/lec-07/search-layer.svg)

Trong vòng lặp, $W$ chứa không quá $ef$ đỉnh tốt nhất trong số các đỉnh được chấp nhận vào vùng khám phá. Mỗi đỉnh vào $V$ nhiều nhất một lần. Thuật toán dừng khi $C$ rỗng hoặc ứng viên tốt nhất chưa mở xa hơn phần tử xa nhất trong $W$.

Bất biến này không bảo đảm tìm được hàng xóm toàn cục: vùng tốt có thể không nối với phần đã khám phá bằng một đường đủ hấp dẫn. Trường hợp xấu vẫn có thể phải thăm tuyến tính theo số đỉnh và cạnh của tầng.

::: exercise Tự kiểm
Vì sao tăng $ef$ thường giúp recall nhưng làm truy vấn tốn hơn?
:::

::: solution
$W$ lớn hơn giữ được nhiều hướng, giảm khả năng cắt sớm một nhánh hữu ích. Đổi lại, thuật toán mở thêm đỉnh và duy trì hàng đợi lớn hơn.
:::

## 5. HNSW: tầng, truy vấn và chèn

Hierarchical Navigable Small World (HNSW) chồng nhiều đồ thị lân cận. Tầng cao thưa để đi xa; tầng 0 dày hơn để tinh chỉnh quanh truy vấn.

Khi chèn một đỉnh, lấy $U\sim\mathrm{Uniform}(0,1]$ và gán mức cao nhất

$$
\ell=\left\lfloor-\ln(U)\,m_L\right\rfloor,\qquad m_L>0.
$$

Đỉnh xuất hiện ở mọi tầng từ 0 đến $\ell$. Xác suất đạt tầng cao giảm theo hàm mũ. Lựa chọn thực nghiệm $m_L=1/\ln M$ chỉ có nghĩa khi $M>1$; đây không phải điều kiện bắt buộc để thuật toán đúng.

![HNSW có ít đỉnh ở tầng cao và nhiều đỉnh ở tầng thấp; truy vấn đi từ lối vào trên xuống tầng 0.](img/lec-07/hnsw-layers.svg)

Giả sử điểm vào nằm ở tầng cao nhất $L$. Từ tầng $L$ xuống tầng 1, truy vấn gọi `SEARCH-LAYER` với $ef=1$; kết quả trở thành điểm vào cho tầng kế tiếp. Ở tầng 0, thuật toán gọi với `efSearch` và trả $K$ phần tử gần nhất. Cần `efSearch` $\ge K$ để tập động có đủ chỗ, nhưng đồ thị được tiếp cận vẫn có thể chứa ít hơn $K$ đỉnh.

Nếu chỉ mục rỗng, đỉnh mới trở thành điểm vào và tạo các tầng $0,\dots,\ell$. Nếu không rỗng, việc chèn gồm hai pha.

1. Từ $L$ xuống $\ell+1$, định tuyến với $ef=1$.
2. Từ $\min(L,\ell)$ xuống 0, tìm ứng viên với `efConstruction`, chọn không quá $M$ lân cận, nối hai chiều rồi cắt danh sách ở mỗi đầu nếu vượt giới hạn.

Tầng 0 dùng $M_{\max,0}$; các tầng trên dùng $M_{\max}$. Nếu $\ell>L$, đỉnh mới trở thành điểm vào ở các tầng mới.

![Khi chèn, HNSW định tuyến ở tầng cao rồi tìm ứng viên, nối và cắt cạnh ở từng tầng thấp hơn.](img/lec-07/hnsw-insert.svg)

Chọn đúng $M$ điểm gần nhất có thể tạo một cụm cạnh cùng hướng. Heuristic đa dạng chỉ nhận ứng viên $e$ khi

$$
d(e,q)<d(e,r)\qquad\text{với mọi lân cận }r\text{ đã chọn}.
$$

Đây là tiêu chí cục bộ nhằm giữ các hướng khác nhau, không phải chứng minh tối ưu toàn cục. Sau khi mỗi đầu mút tự cắt danh sách, quan hệ kề có thể không còn đối xứng dù bước nối ban đầu là hai chiều. Phần mở rộng ứng viên của bài báo HNSW nằm ngoài phạm vi bài này.

## 6. Tham số, bộ nhớ và giới hạn HNSW

| Tham số | Khi tăng tham số |
|---|---|
| $M$ | nhiều cạnh hơn; bộ nhớ và thời gian xây dựng tăng; khả năng điều hướng thường tốt hơn |
| `efConstruction` | xét nhiều ứng viên khi chèn; xây dựng chậm hơn và đồ thị thường tốt hơn |
| `efSearch` | mở rộng truy vấn; độ trễ tăng và recall thường tăng |

Nếu lưu véc-tơ gốc, dữ liệu cần $O(ND)$ số. Nếu bậc trung bình được chặn bởi một hằng số tỷ lệ với $M$, số liên kết kỳ vọng là $O(NM)$. Đây là suy luận dưới giả thiết về bậc, không phải cận cho mọi trạng thái hay mọi cài đặt.

HNSW không bảo đảm phổ quát rằng mọi truy vấn đều mất thời gian logarit. Đồ thị kém, tham số nhỏ hoặc dữ liệu bất lợi có thể làm tìm kiếm thăm nhiều đỉnh, đến mức tuyến tính trong trường hợp xấu.

::: exercise Tự kiểm
Muốn giảm độ trễ mà không xây lại chỉ mục, nên điều chỉnh tham số nào? Rủi ro là gì?
:::

::: solution
Giảm `efSearch`. Truy vấn mở ít đỉnh hơn nhưng có thể bỏ lỡ hàng xóm đúng, làm recall giảm.
:::

## 7. Từ lượng tử hóa véc-tơ đến lượng tử hóa tích

Lượng tử hóa véc-tơ (VQ) học bộ mã $C=\{c_1,\dots,c_{k^*}\}\subset\mathbb R^D$. Mỗi $y$ nhận chỉ số tâm gần nhất và được tái dựng bằng tâm đó:

$$
i(y)=\arg\min_{1\le i\le k^*}\|y-c_i\|^2,\qquad \widehat y=c_{i(y)}.
$$

Ví dụ một chiều: với các tâm 0 và 4, điểm $y=3$ nhận mã 2, tái dựng thành 4 và có sai số bình phương 1. Một bộ mã cho toàn không gian cần lưu $k^*D$ số; muốn biểu diễn rất nhiều mã thì số tâm tăng quá nhanh.

PQ chia $D$ chiều thành $m$ đoạn bằng nhau, nên cần $m\mid D$. Mỗi đoạn dùng một bộ mã con gồm $k^*=2^b$ tâm. Mã của $y$ là $(i_1(y),\dots,i_m(y))$; véc-tơ tái dựng là phép ghép các tâm con tương ứng.

Số tổ hợp mã là $(k^*)^m$, nhưng các bộ mã chỉ lưu $mk^*(D/m)=k^*D$ số. Cơ sở dữ liệu mã cần

$$
N\left\lceil\frac{mb}{8}\right\rceil\ \text{byte}.
$$

![PQ chia véc-tơ thành các đoạn và thay mỗi đoạn bằng chỉ số của một tâm con.](img/lec-07/pq-split.svg)

PQ giảm bộ nhớ nhưng tạo sai số tái dựng $\|y-\widehat y\|^2$. Tăng $m$ hoặc $b$ thường giảm sai số, đồng thời làm mã, bảng tra hoặc thời gian huấn luyện lớn hơn.

::: exercise Tự kiểm
Với $m=4$ và $b=8$, một mã dài bao nhiêu byte và biểu diễn bao nhiêu tổ hợp tâm?
:::

::: solution
Mã dài 4 byte và biểu diễn $(2^8)^4=2^{32}$ tổ hợp tâm.
:::

## 8. ADC, bảng tra và chi phí PQ

Trong tính khoảng cách bất đối xứng (ADC), truy vấn giữ nguyên độ chính xác còn véc-tơ cơ sở dữ liệu chỉ tồn tại dưới dạng mã PQ. Với $q=(q_1,\dots,q_m)$ và mã $(i_1,\dots,i_m)$,

$$
\widehat d_{\mathrm{ADC}}^2(q,y)=\sum_{j=1}^{m}\|q_j-c_{j,i_j}\|^2.
$$

Trước khi quét, lập bảng $T[j,i]=\|q_j-c_{j,i}\|^2$. Chấm điểm một mã chỉ cần $m$ lần tra bảng và cộng.

::: example Ví dụ ADC dựng lại
Cho $D=4$, $m=2$, $q=((0,0),(0,0))$. Một mã chọn $c_{1,2}=(0.1,0.1)$ và $c_{2,4}=(0.2,0.5)$. Khi đó

$$
T[1,2]=0.1^2+0.1^2=0.02,\qquad T[2,4]=0.2^2+0.5^2=0.29.
$$

Khoảng cách ADC bình phương là $0.02+0.29=0.31$. Các số minh họa đúng cơ chế bảng tra, không phải kết quả thực nghiệm từ nguồn.
:::

![ADC lập bảng khoảng cách từ từng đoạn truy vấn đến các tâm con rồi cộng các ô theo mã PQ.](img/lec-07/pq-lut.svg)

Lập bảng tốn $\Theta(k^*D)$ phép toán và lưu $\Theta(mk^*)$ số. Chấm một mã tốn $\Theta(m)$; quét đủ tốn $\Theta(Nm)$, chưa kể chọn top-$K$. Bộ mã chiếm $\Theta(k^*D)$ số và mã cơ sở dữ liệu chiếm $Nmb$ bit khi $mb$ chia hết cho 8.

Tính khoảng cách đối xứng (SDC) lượng tử hóa cả truy vấn lẫn dữ liệu rồi tra khoảng cách giữa hai tâm con. SDC có thể giảm tính toán nhưng thêm sai số do lượng tử hóa truy vấn. Bài này dùng ADC làm cơ chế chính.

## 9. IVF-PQ: lọc danh sách rồi chấm mã phần dư

PQ quét đầy đủ vẫn xét mọi mã. Inverted File with Product Quantization (IVF-PQ) thêm một lượng tử hóa thô để chỉ mở vài danh sách.

1. Học $k_c$ tâm thô $\mu_1,\dots,\mu_{k_c}$.
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

Làm các ô 98–99 với $M\in\{4,8,16\}$ và `nbits=48/M`. Ba cấu hình lần lượt là $4\times12$, $8\times6$ và $16\times4$ bit; tất cả đều dùng 48 bit, tức 6 byte mỗi véc-tơ. Báo cáo `dsub`, `ksub`, sai số tái dựng trung bình và thời gian huấn luyện/mã hóa. Không trộn phần này với cấu hình $4\times8$ bit ở nhiệm vụ 1.

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
- Princeton COS 597G, lớp 8, *Quantization*, và notebook thực hành đi kèm.
- Princeton COS 597G, lớp 9, *Graph Indexes*.
- Yu. A. Malkov và D. A. Yashunin, *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs*.
- H. Jégou, M. Douze và C. Schmid, *Product Quantization for Nearest Neighbor Search*.
- J. Leskovec, A. Rajaraman và J. D. Ullman, *Mining of Massive Datasets*, Chương 3.
