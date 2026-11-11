# Bài 07 — Chỉ mục hàng xóm gần đúng

Bài 06 tìm các cặp gần nhau bên trong một tập bằng băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH). Trong chương này, chúng ta xét bài toán truy vấn: cho một véc-tơ mới $q$, tìm $K$ véc-tơ gần $q$ nhất trong một kho rất lớn mà không đo khoảng cách từ $q$ tới mọi véc-tơ của kho. Ba cấu trúc được xây dựng là đồ thị thế giới nhỏ phân tầng (HNSW), lượng tử hóa tích (PQ) và tệp đảo kết hợp lượng tử hóa tích (IVF-PQ).

[Bộ trang chiếu Bài 07](lecture-07-chi-muc-hang-xom-gan-dung.html) trình bày cùng các ví dụ; [tệp bài tập Bài 07](material-viewer.html?doc=materials/lec-07/exercises.md&deck=lecture-07-chi-muc-hang-xom-gan-dung.html) chứa các bài tập củng cố và phần thực hành với sổ Faiss của Princeton.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đặc tả tìm đúng và tìm gần đúng $K$ hàng xóm, tính độ thu hồi, tách hai nguồn làm chỉ mục thiếu hàng xóm thật (Mục 1).
2. Chạy tay tìm kiếm tham lam và `SEARCH-LAYER`, chứng minh bất biến của `SEARCH-LAYER` (Mục 2).
3. Chạy truy vấn và phép chèn HNSW trên dữ kiện nhỏ, tính phân phối tầng và bộ nhớ, nêu ba giả thiết của cận $O(\log N)$ cho số phép đo (Mục 3).
4. Mã hóa và tái dựng véc-tơ bằng lượng tử hóa véc-tơ và lượng tử hóa tích, tính khoảng cách bất đối xứng bằng bảng tra và chặn sai số của nó (Mục 4).
5. Chạy truy vấn IVF-PQ trên phần dư, tính chi phí theo số tâm thô và số danh sách mở, nêu hậu quả khi danh sách lệch (Mục 5, Tình huống 07.2).
6. So sánh LSH, HNSW, PQ quét đủ và IVF-PQ theo bốn trục đánh giá, chọn chỉ mục theo ngân sách bộ nhớ, thời gian và ngưỡng độ thu hồi (Mục 6, Tình huống 07.1).

## Kiến thức tiên quyết

Số hiệu `01.k`, `06.k` chỉ ghi chú Bài 01, Bài 06; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Bài toán $k$ hàng xóm gần nhất chính xác** (Định nghĩa 01.2). Với kho $\mathbf x_1,\ldots,\mathbf x_n\in\mathbb R^D$, truy vấn $\mathbf y$ và $1\le k\le n$, tập $\mathcal N_k(\mathbf y)$ gồm $k$ chỉ số đứng đầu khi sắp theo cặp $(d(\mathbf x_i,\mathbf y),i)$ tăng dần.
- **Chỉ mục** (Định nghĩa 01.8). Chỉ mục trên một trường là cấu trúc dữ liệu trả mọi bản ghi có giá trị cho trước ở trường đó mà không đọc mọi bản ghi của tệp.
- **Xác minh ứng viên** (Mệnh đề 01.16). Kiểm chính xác trên một tập ứng viên $A$ trả đúng $A\cap R$, với $R$ là tập kết quả cần tìm; kết quả trả bằng $R$ khi và chỉ khi $R\subseteq A$ (phần (c)).
- **Độ thu hồi tại $k$** (Định nghĩa 01.17). Với tập $\widehat{\mathcal N}_k(\mathbf y)$ gồm $k$ chỉ số do một phương pháp trả về, $\operatorname{recall@}k(\mathbf y)=|\widehat{\mathcal N}_k(\mathbf y)\cap\mathcal N_k(\mathbf y)|/k$.
- **Độ đo khoảng cách** (Định nghĩa 06.14). Khoảng cách Euclid $\|x-y\|_2$ không âm, đối xứng, bằng $0$ đúng khi $x=y$, và thỏa bất đẳng thức tam giác $d(x,w)\le d(x,y)+d(y,w)$.
- **Họ nhạy cảm, phép ghép và LSH cho truy vấn** (Định nghĩa 06.22; Mệnh đề 06.26; Nhận xét 06.27; Định lý 06.36). Họ $\mathcal H$ là $(d_1,d_2,p_1,p_2)$-nhạy cảm nếu cặp có $d\le d_1$ trùng giá trị băm với xác suất ít nhất $p_1$ và cặp có $d\ge d_2$ trùng với xác suất nhiều nhất $p_2$. Ghép đồng thời $r$ hàm rồi ghép ít nhất một trên $b$ bảng nhận một cặp gần với xác suất ít nhất $1-(1-p_1^r)^b$; phân dải chữ ký là trường hợp riêng này. Theo Bài 06, khi LSH làm bộ lọc ứng viên cho truy vấn, véc-tơ truy vấn được băm bằng cùng các hàm và chỉ các véc-tơ cùng thùng được đo khoảng cách. Với khoảng cách Euclid, họ chiếu có dịch là $(a/2,2a,1/2,1/3)$-nhạy cảm, và bộ tham số này chỉ được chứng minh khi $D=2$.
- **Đồ thị, hàng đợi ưu tiên và đống nhị phân** (học phần Cấu trúc dữ liệu và giải thuật). Đồ thị có hướng gồm tập đỉnh và tập cạnh có thứ tự $(u,v)$. Đống nhị phân $n$ phần tử chèn hoặc lấy ra một phần tử trong $O(\log n)$ và đọc phần tử nhỏ nhất (đống cực tiểu) hoặc lớn nhất (đống cực đại) trong $O(1)$.
- **Xác suất** (học phần Xác suất thống kê). Tuyến tính kỳ vọng: kỳ vọng của một tổng bằng tổng các kỳ vọng, không cần độc lập; kỳ vọng của biến chỉ báo bằng xác suất của biến cố. Với biến ngẫu nhiên nhận giá trị nguyên không âm $X$, $\mathbb E[X]=\sum_{t\ge1}\Pr[X\ge t]$. Chặn hợp: $\Pr[\bigcup_iA_i]\le\sum_i\Pr[A_i]$, không cần độc lập. Chuỗi hình học: $\sum_{s\ge1}x^s=x/(1-x)$ khi $0\le x<1$.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một mục được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương, trừ các ngoại lệ nêu trong đoạn ngay sau bảng.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $Y=\{y_1,\ldots,y_N\}$; $N$; $D$ | kho véc-tơ; số véc-tơ; số chiều | $Y\subset\mathbb R^D$; số nguyên dương |
| $q$; $Q$ | véc-tơ truy vấn; tập truy vấn dùng để đo chất lượng | $\mathbb R^D$; tập hữu hạn |
| $d(\cdot,\cdot)$ | khoảng cách Euclid, $d(x,y)=\|x-y\|$; bình phương viết $\|x-y\|^2$ | $\mathbb R_{\ge0}$ |
| $K$ | số hàng xóm cần trả | $1\le K\le N$ |
| $\mathcal N_K(q)$; $\widehat{\mathcal N}_K(q)$ | tập $K$ hàng xóm đúng; tập do chỉ mục trả | tập chỉ số |
| $\operatorname{recall@}K(q)$; $\overline{\operatorname{recall@}K}$ | độ thu hồi tại $K$ của một truy vấn; trung bình trên $Q$ | $[0,1]$ |
| $S$; $n_c$ | tập véc-tơ được đo; số véc-tơ được đo, $n_c=|S|$ | $S\subseteq Y$; $0\le n_c\le N$ |
| $\widetilde d(q,y)$ | khoảng cách mà chỉ mục dùng để xếp hạng $y$ | $\mathbb R_{\ge0}$ |
| $V$; $C$; $W$ | đỉnh đã thấy; đỉnh chờ mở; kết quả tạm của `SEARCH-LAYER` | tập đỉnh, $C\subseteq V$, $W\subseteq V$ |
| $ef$; $f$; $ep$ | bề rộng chùm; phần tử xa $q$ nhất của $W$; tập điểm vào | $ef\ge1$; đỉnh; $1\le|ep|\le ef$ |
| $s$; $\mathcal L(y)$; $g$ | điểm vào của chỉ mục đồ thị; tập lân cận của đỉnh $y$; bậc ra trung bình | đỉnh; tập đỉnh; số thực dương |
| $u\prec v$; $u\preceq v$ | $(d(u,q),u)$ đứng trước $(d(v,q),v)$ theo thứ tự từ điển; $u\prec v$ hoặc $u=v$ | thứ tự toàn phần trên đỉnh |
| $\ell(y)$; $\ell_c$; $L$ | tầng tối đa của điểm $y$; tầng đang xét; tầng của điểm vào | số nguyên $\ge0$ |
| $Y_\ell$ | tập điểm có tầng tối đa ít nhất $\ell$ | $Y=Y_0\supseteq Y_1\supseteq\cdots$ |
| $m_L$; $\rho$; $U$ | hệ số rút tầng; $\rho=e^{-1/m_L}$; biến ngẫu nhiên đều | $m_L>0$; $(0,1)$; $(0,1]$ |
| $M$; $M_{\max}$; $M_{\max,0}$ | số lân cận nối cho điểm mới; bậc tối đa ở tầng trên; ở tầng 0 | số nguyên dương, $M\le M_{\max}\le M_{\max,0}$ |
| $\mathcal R$ | tập lân cận được chọn cho điểm mới ở một tầng | $\mathcal R\subseteq W$, $|\mathcal R|\le M$ |
| $\mathit{efConstruction}$; $\mathit{efSearch}$ | bề rộng chùm khi chèn; khi truy vấn ở tầng 0 | $\ge M$; $\ge K$ |
| $s_{id}$ | số byte của một mã định danh | 4 hoặc 8 |
| $\mathcal C$; $k$; $c_i$; $i(x)$; $\widehat x$ | bộ mã của lượng tử hóa véc-tơ; số tâm; tâm thứ $i$; mã của $x$; véc-tơ tái dựng | $\mathcal C\subset\mathbb R^D$; $0\le i<k$ |
| $m$; $G_j$; $x^{(j)}$ | số đoạn của lượng tử hóa tích; tập tọa độ của đoạn $j$; đoạn $j$ của $x$ | $m\mid D$; $G_1,\ldots,G_m$ phân hoạch $\{1,\ldots,D\}$; $\mathbb R^{D/m}$ |
| $k^*$; $\mathcal C^{(j)}$; $c^{(j)}_i$; $i_j(x)$ | số tâm mỗi bộ mã con; bộ mã con của đoạn $j$; tâm con $i$ của đoạn $j$; chỉ số tâm con của đoạn $j$ trong mã của $x$ | lũy thừa của 2, mỗi chỉ số dài $\log_2k^*$ bit; $0\le i<k^*$ |
| $\widehat d(q,y)$; $T[j,i]$ | khoảng cách đối xứng; phần tử của bảng tra khoảng cách | $\mathbb R_{\ge0}$; bảng $m\times k^*$ |
| $k_c$; $\mu_i$; $a(y)$; $L_i$ | số tâm thô; tâm thô thứ $i$; chỉ số tâm thô của $y$; danh sách đảo thứ $i$ | $0\le i<k_c$ |
| $\mathit{nprobe}$; $P$ | số danh sách mở; tập chỉ số các danh sách mở | $1\le \mathit{nprobe}\le k_c$; $|P|=\mathit{nprobe}$ |
| $r(y)$; $\widetilde q_i$ | phần dư $y-\mu_{a(y)}$; truy vấn dư $q-\mu_i$ | $\mathbb R^D$ |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy; tọa độ của một điểm cách nhau bằng dấu chấm phẩy, ví dụ $(1{,}7;\ 0{,}4)$; dấu $\mid$ ngăn hai đoạn của một véc-tơ, ví dụ $(0{,}2;\ 1{,}8\mid2{,}7;\ 0{,}1)$. 1 GB $=10^9$ byte và 1 TB $=10^{12}$ byte.
- Chỉ số véc-tơ $y_i$ và chỉ số đoạn $j$ đếm từ 1; chỉ số tâm, mã và danh sách đảo đếm từ 0.
- Tên đỉnh của đồ thị ví dụ viết thẳng ($\mathrm e,\mathrm a,\mathrm b,\mathrm s,\mathrm t,\mathrm u,\mathrm z$), kèm khoảng cách tới $q$ sau dấu hai chấm: $\mathrm e{:}9$ nghĩa là $d(\mathrm e,q)=9$. Chữ $e$ nghiêng trong $e^{-1/m_L}$ là cơ số của logarit tự nhiên.
- Chữ $L$ không chỉ số là tầng của điểm vào; $L_i$ có chỉ số là danh sách đảo. Chữ $C$ là hàng đợi đỉnh chờ mở, còn $\mathcal C$ là bộ mã.
- Hai ngoại lệ trong chương: chữ $k$ không chỉ số là số tâm của lượng tử hóa véc-tơ, nhưng là chỉ số tầng trong Mệnh đề 07.19, đoạn đọc sau mệnh đề này, Mệnh đề 07.21, Ví dụ 07.8, Bài tập 07.7 và công thức phân phối tầng của Tóm tắt; $p_1,\ldots,p_{11}$ là các điểm trên đường thẳng của Mục 3, còn $p_1$, $p_2$ của họ nhạy cảm chỉ xuất hiện ở phần tiên quyết, Mục 1.3 và Mục 6.
- So với Bài 06, các chữ $N$, $K$, $m$, $\rho$, $Q$, $C$, $\mathcal C$, $L$, $s$, $k$ đổi nghĩa; hai chữ $b$, $r$ giữ nghĩa số dải và số hàng mỗi dải của LSH.

Bảng sau nêu tương ứng ký hiệu một lần.

| Chương này | Bài báo HNSW | Bài báo PQ (Jégou và cộng sự) | Faiss và sổ thực hành |
|---|---|---|---|
| $N$, $y_i$, $q$, $K$ | $q$ là điểm được chèn | $n$, $y$, $x$ (truy vấn), $k$ | `nb`, `xb`, `xq`, `k` |
| $\rho$ | $p$ (§4.1) | — | — |
| $m$, $k^*$ | — | $m$, $k^*$ | `M`, $2^{\texttt{nbits}}$ |
| $k_c$, $\mathit{nprobe}$ | — | $k'$, $w$ | `nlist`, `nprobe` |

<!-- note-topic-id: lec-07-topic-01 -->
## 1. Bài toán hàng xóm gần đúng

Bài 01 đặt bài toán $k$ hàng xóm gần nhất chính xác (Định nghĩa 01.2): sắp mọi véc-tơ của kho theo khoảng cách tới truy vấn rồi lấy $k$ chỉ số đầu, nên mỗi truy vấn đo khoảng cách tới mọi véc-tơ. Bài 06 dùng LSH làm bộ lọc ứng viên: truy vấn được băm bằng cùng các hàm và chỉ các véc-tơ cùng thùng được đo; một véc-tơ gần thành ứng viên với xác suất ít nhất $1-(1-p_1^r)^b$ (Mệnh đề 06.26). Bộ lọc này có hai giới hạn: với khoảng cách Euclid, bộ tham số $(a/2,2a,1/2,1/3)$ chỉ được chứng minh khi $D=2$ (Định lý 06.36), và mọi véc-tơ gốc vẫn phải lưu để đo.

Bài toán trung tâm của chương có quy mô của BIODS 271 (bài 12, tr.17): kho $N=10^{10}$ véc-tơ, mỗi véc-tơ $D=3072$ thành phần là số thực 4 byte, tức $122{,}88$ TB. Giả sử máy chủ có 6 TB bộ nhớ trong, ứng dụng cho mỗi truy vấn 10 ms, và máy xử lý $10^{12}$ *thao tác* mỗi giây, với một thao tác là một lượt xử lý một tọa độ hoặc một lần tra bảng. Kho gốc vượt 6 TB hơn 20 lần. Quét toàn kho cho một truy vấn xử lý

$$
ND=10^{10}\cdot3072=3{,}072\cdot10^{13}
$$

lượt tọa độ, tức $30{,}72$ giây, gấp $3072$ lần ngân sách thời gian. Để trả lời trong cả hai ngân sách, chúng ta chấp nhận trả một tập gần đúng và xây ba cơ chế: đi theo cạnh của đồ thị để chỉ đo một phần kho, nén mỗi véc-tơ thành một mã ngắn để mỗi phép đo rẻ hơn, và ghép hai cách đó.

![Sơ đồ cấu trúc chương. Khối trên: kho mười mũ mười véc-tơ 3072 chiều, 122,88 TB, quét đủ 30,72 giây; chi phí bằng số véc-tơ được đo nhân chi phí một phép đo. Nhánh 1 giảm số véc-tơ được đo: khối nét đứt LSH của Bài 06, Mục 2 đồ thị lân cận, Mục 3 HNSW khoảng 125,5 TB. Nhánh 2 giảm chi phí một phép đo và bộ nhớ: Mục 4 lượng tử hóa tích, 5,12 TB, 5,12 giây. Hai nhánh hội tụ ở Mục 5 IVF-PQ, khoảng 5,2 TB và 3,6 ms, rồi Mục 6 chọn chỉ mục; mục tiêu 6 TB và 10 ms.](img/lec-07/note-cau-truc-chuong-07.svg)

Trên hình, khối trên cùng tách chi phí một truy vấn thành hai thừa số (Mệnh đề 07.7). Nhánh trái giảm thừa số thứ nhất: LSH của Bài 06 (khối nét đứt) giảm bằng thùng băm, Mục 2 và Mục 3 giảm bằng đường đi trên đồ thị. Nhánh phải giảm thừa số thứ hai và bộ nhớ bằng mã ngắn (Mục 4). Mục 5 ghép hai nhánh, và Mục 6 so bốn cấu trúc trên cùng kho mở đầu.

### 1.1 Tìm đúng, tìm gần đúng và chỉ mục

Trong *truy hồi ngữ nghĩa* (semantic retrieval), kho văn bản được chia thành các đoạn văn bản, và một *mô hình nhúng* (embedding model) biến mỗi đoạn văn bản thành một véc-tơ số thực; câu truy vấn đi qua cùng mô hình để thành véc-tơ $q$ (BIODS 271, tr.16). Hai đoạn văn bản có nội dung gần nhau cho hai véc-tơ gần nhau theo một độ đo như tích vô hướng, cosin hoặc khoảng cách Euclid. Tìm các đoạn văn bản liên quan tới câu hỏi khi đó là tìm các véc-tơ gần $q$ nhất trong kho. Trong toàn chương, $d$ là khoảng cách Euclid.

![Mười tỷ đoạn văn bản và câu truy vấn đi qua cùng một mô hình nhúng thành véc-tơ 3072 chiều; kết quả là K đoạn có véc-tơ gần véc-tơ truy vấn q nhất.](img/lec-07/truy-hoi-ngu-nghia.svg)

Kho đi qua mô hình nhúng một lần, khi xây chỉ mục, còn truy vấn đi qua mô hình mỗi lần hỏi. Để làm rõ đầu ra cần tạo, xem ví dụ sau.

::: example Ví dụ 07.1 (Năm điểm và ba hàng xóm)
**Dữ kiện.** Kho có $N=5$ véc-tơ $y_1,\ldots,y_5$; khoảng cách tới truy vấn $q$ đã tính là $d(q,y_1)=2{,}5$, $d(q,y_2)=1{,}2$, $d(q,y_3)=3{,}0$, $d(q,y_4)=0{,}8$, $d(q,y_5)=1{,}7$; cần $K=3$ hàng xóm.

**Thứ tự.** Sắp theo khoảng cách tăng dần: $y_4$ ($0{,}8$), $y_2$ ($1{,}2$), $y_5$ ($1{,}7$), $y_1$ ($2{,}5$), $y_3$ ($3{,}0$). Ba chỉ số đầu cho $\mathcal N_3(q)=\{4,2,5\}$.

**Quét với ba chỗ.** Đọc lần lượt $y_1,\ldots,y_5$ và chỉ giữ ba điểm gần nhất đã gặp, cùng điểm xa nhất trong ba điểm ấy:

| Đọc | Khoảng cách | Ba điểm đang giữ | Điểm xa nhất đang giữ |
|---|---|---|---|
| $y_1$ | $2{,}5$ | $y_1$ | $y_1{:}2{,}5$ |
| $y_2$ | $1{,}2$ | $y_1,y_2$ | $y_1{:}2{,}5$ |
| $y_3$ | $3{,}0$ | $y_1,y_2,y_3$ | $y_3{:}3{,}0$ |
| $y_4$ | $0{,}8$ | thay $y_3$: $y_1,y_2,y_4$ | $y_1{:}2{,}5$ |
| $y_5$ | $1{,}7$ | thay $y_1$: $y_2,y_4,y_5$ | $y_5{:}1{,}7$ |

**Kiểm tra lại.** Phép quét giữ đúng $\{y_2,y_4,y_5\}=\mathcal N_3(q)$ sau năm phép đo; điểm bị thay luôn là điểm xa nhất đang giữ, và chỉ bị thay khi điểm mới gần hơn nó.
:::

Ví dụ 07.1 giải bài toán bằng cách đo cả năm điểm. Với $N=10^{10}$, chúng ta muốn trả một tập gần với $\mathcal N_K(q)$ mà chỉ đo một phần kho hoặc dùng một khoảng cách rẻ hơn. Định nghĩa sau tách ba đối tượng: bài toán tìm đúng, bài toán tìm gần đúng và cấu trúc dựng sẵn để giải bài toán thứ hai.

::: definition Định nghĩa 07.1 (Tìm đúng, tìm gần đúng và chỉ mục hàng xóm)
Cho kho $Y=\{y_1,\ldots,y_N\}\subset\mathbb R^D$, truy vấn $q\in\mathbb R^D$, khoảng cách $d$ và số nguyên $K$ với $1\le K\le N$.

- Bài toán *tìm đúng $K$ hàng xóm* (exact $K$-nearest-neighbor search) trả tập $\mathcal N_K(q)$ gồm $K$ chỉ số đứng đầu khi sắp các chỉ số theo cặp $(d(q,y_i),i)$ tăng dần theo thứ tự từ điển.
- Bài toán *tìm gần đúng $K$ hàng xóm* (approximate nearest neighbor search, ANN) trả một tập $\widehat{\mathcal N}_K(q)$ gồm tối đa $K$ chỉ số phân biệt của $Y$, không đòi $\widehat{\mathcal N}_K(q)=\mathcal N_K(q)$.
- Một *chỉ mục hàng xóm* (vector index) là cấu trúc dữ liệu dựng trên $Y$ trước khi có truy vấn; với mỗi $q$, chỉ mục quyết định véc-tơ nào được đo và đo bằng khoảng cách nào, rồi trả $\widehat{\mathcal N}_K(q)$.
:::

Bài toán tìm đúng là bài toán của Định nghĩa 01.2 với $n\to N$, $\mathbf x_i\to y_i$, $\mathbf y\to q$, $k\to K$, kể cả quy tắc phá hòa theo chỉ số. Bài toán tìm gần đúng bỏ yêu cầu đầu ra bằng $\mathcal N_K(q)$. Chữ "tối đa" cho phép chỉ mục trả ít hơn $K$ chỉ số khi phần kho được đo chứa ít hơn $K$ véc-tơ.

Chỉ mục băm (Định nghĩa 01.8) tra bản ghi có khóa *bằng* một giá trị cho trước; chỉ mục hàng xóm tra các véc-tơ *gần* một véc-tơ cho trước và chấp nhận trả thiếu. Một nhầm lẫn thường gặp là coi chỉ mục hàng xóm như một cách tính $\mathcal N_K(q)$ nhanh hơn: không chỉ mục nào trong chương này bảo đảm $\widehat{\mathcal N}_K(q)=\mathcal N_K(q)$ cho mọi truy vấn.

Trước khi xây chỉ mục, chúng ta viết lại phép quét của Ví dụ 07.1 thành thuật toán, vì nó là mốc chi phí và là cách tính tập đúng để đo chất lượng. Ba điểm đang giữ được đặt trong một đống cực đại $H$ theo cặp $(d,i)$: gốc của đống là điểm xa nhất đang giữ, nên việc so và thay ở mỗi bước chỉ chạm gốc.

::: algorithm Thuật toán 07.2 (Quét đầy đủ với đống $K$ phần tử)
**Đầu vào.** Kho $Y=\{y_1,\ldots,y_N\}\subset\mathbb R^D$, truy vấn $q$, khoảng cách $d$, số nguyên $K$ với $1\le K\le N$.

**Đầu ra.** Danh sách $K$ chỉ số của $\mathcal N_K(q)$ theo thứ tự $(d(q,y_i),i)$ tăng dần.

**Giả thiết.** $H$ là đống cực đại theo thứ tự từ điển của cặp $(\delta,i)$; một khoảng cách Euclid trong $\mathbb R^D$ tốn $\Theta(D)$ phép toán.

1. Khởi tạo $H$ rỗng.
2. Với $t=1,\ldots,N$: tính $\delta_t=d(q,y_t)$. Nếu $|H|<K$, chèn $(\delta_t,t)$ vào $H$. Ngược lại, nếu $(\delta_t,t)$ nhỏ hơn gốc của $H$ theo thứ tự từ điển, lấy gốc ra rồi chèn $(\delta_t,t)$.
3. Lấy lần lượt các phần tử khỏi $H$ rồi đảo thứ tự; trả các chỉ số.

**Dừng.** Bước 2 có đúng $N$ lượt; bước 3 có $K$ lượt.

**Trường hợp biên.** Khi $\delta_t$ bằng khoảng cách ở gốc, cặp $(\delta_t,t)$ lớn hơn gốc vì $t$ lớn hơn mọi chỉ số đã đọc, nên điểm mới không thay điểm cũ, đúng quy tắc phá hòa theo chỉ số nhỏ.

**Chi phí.**

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2: tính khoảng cách | $N$ | $\Theta(D)$ | $\Theta(ND)$ |
| 2: so với gốc | $N$ | $O(1)$ | $O(N)$ |
| 2: lấy gốc và chèn | nhiều nhất $N$ | $O(\log K)$ | $O(N\log K)$ |
| 3: lấy hết phần tử | $K$ | $O(\log K)$ | $O(K\log K)$ |
:::

Thao tác quyết định của Thuật toán 07.2 là phép so với gốc ở bước 2: gốc là phần tử lớn nhất trong $K$ phần tử đang giữ, nên một điểm mới thuộc $K$ điểm gần nhất đã gặp khi và chỉ khi nó nhỏ hơn gốc. Mệnh đề sau phát biểu tính đúng và chi phí.

::: proposition Mệnh đề 07.3 (Tính đúng và chi phí của quét đầy đủ)
**Giả thiết.** $1\le K\le N$; mỗi $\delta_t=d(q,y_t)$ được tính chính xác; phép so dùng thứ tự từ điển trên cặp $(\delta,i)$.

**Kết luận.**

- (a) Thuật toán 07.2 trả đúng $\mathcal N_K(q)$, theo thứ tự $(d(q,y_i),i)$ tăng dần.
- (b) Thuật toán tính đúng $N$ khoảng cách và tốn $\Theta(ND)+O(N\log K)$ phép toán; ngoài kho, bộ nhớ phụ là $O(K)$.

**Điều kiện áp dụng.** Mọi hàm $d$ nhận giá trị thực; tính đúng không cần $d$ là độ đo khoảng cách.

**Phạm vi.** Chi phí tuyến tính theo $N$ cho mỗi truy vấn; thuật toán không dùng cấu trúc nào dựng trước.
:::

::: proof Chứng minh Mệnh đề 07.3
Ý tưởng: sau mỗi lượt của bước 2, đống chứa đúng các điểm gần nhất trong phần kho đã đọc. Gọi $I_t$ là mệnh đề "sau lượt $t$, $H$ chứa đúng $\min(K,t)$ cặp nhỏ nhất của $\{(\delta_1,1),\ldots,(\delta_t,t)\}$".

**Bước 1 (khởi tạo).** Trước lượt đầu, $t=0$ và $H$ rỗng, đúng là $\min(K,0)=0$ cặp nhỏ nhất của tập rỗng.

**Bước 2 (duy trì).** Giả sử $I_{t-1}$ đúng. Nếu $t-1<K$, thuật toán chèn $(\delta_t,t)$, nên $H$ chứa cả $t=\min(K,t)$ cặp. Nếu $t-1\ge K$, $H$ chứa $K$ cặp nhỏ nhất của $t-1$ cặp đầu với gốc $g$ lớn nhất trong chúng. Khi $(\delta_t,t)<g$, $K$ cặp nhỏ nhất của $t$ cặp đầu gồm cặp mới và $K-1$ cặp nhỏ nhất cũ, tức $H$ bỏ $g$ rồi thêm cặp mới. Khi $(\delta_t,t)>g$, có $K$ cặp cũ nhỏ hơn cặp mới, nên cặp mới không thuộc $K$ cặp nhỏ nhất và $H$ giữ nguyên. Hai cặp không thể bằng nhau vì chỉ số khác nhau. Vậy $I_t$ đúng.

**Bước 3 (kết thúc).** Sau lượt $N$, $I_N$ và $K\le N$ cho $H$ gồm $K$ cặp nhỏ nhất của mọi cặp, tức các chỉ số của $\mathcal N_K(q)$ [do Định nghĩa 07.1]. Bước 3 lấy các phần tử theo thứ tự giảm dần của đống cực đại, nên sau khi đảo, danh sách tăng dần. Điều này chứng minh (a).

**Bước 4 (chi phí).** Bước 2 tính $N$ khoảng cách, mỗi khoảng cách $\Theta(D)$; mỗi lượt có một phép so với gốc $O(1)$ và nhiều nhất một cặp lấy ra, chèn trên đống không quá $K$ phần tử, $O(\log K)$. Bước 3 tốn $O(K\log K)\subseteq O(N\log K)$. Đống giữ không quá $K$ cặp. Điều này chứng minh (b). $\square$
:::

Các giả thiết của Mệnh đề 07.3 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ phá hòa theo chỉ số, chỉ so khoảng cách bằng "$\le$": với $K=1$ và $\delta_1=\delta_2=1$, điểm $y_2$ thay $y_1$ và đầu ra là $\{2\}$, trong khi $\mathcal N_1(q)=\{1\}$.
- Bỏ $K\le N$: với $N=2$ và $K=3$, đống chỉ có hai phần tử và $\mathcal N_3(q)$ không xác định.
- Bỏ tính chính xác của $\delta_t$: nếu $\delta_5$ trong Ví dụ 07.1 được tính thành $2{,}6$, tập trả là $\{1,2,4\}\ne\mathcal N_3(q)$.

Bước 2 của chứng minh dùng phá hòa (hai cặp không bằng nhau) và tính chính xác của $\delta_t$; Bước 3 dùng $K\le N$.

**Trong thực hành.** Sổ thực hành đi kèm bài giảng 8 (class 8) của học phần Princeton COS 597A tính tập đúng `gt` gồm 10 hàng xóm cho mỗi truy vấn trong 100 truy vấn trên kho $10^4$ véc-tơ 64 chiều bằng hàm `faiss.knn`, một phép quét đầy đủ (ô mã 21). Tập đúng tốn $100\cdot10^4=10^6$ phép đo, được tính một lần rồi dùng để đo mọi chỉ mục gần đúng. Với kho mở đầu, cùng phép quét cần $30{,}72$ giây cho một truy vấn, nên tập đúng chỉ tính được trên một mẫu truy vấn nhỏ.

### 1.2 Độ thu hồi

Giả sử một chỉ mục trả $\{y_4,y_5,y_1\}$ cho truy vấn của Ví dụ 07.1. Hai trong ba điểm đúng là hàng xóm thật; $y_2$ bị thiếu và $y_1$ đứng vào chỗ của nó. Đại lượng sau đo phần hàng xóm thật được tìm lại, cho một truy vấn và cho một tập truy vấn.

::: definition Định nghĩa 07.4 (Độ thu hồi tại $K$; độ thu hồi trung bình)
Cho truy vấn $q$, tập đúng $\mathcal N_K(q)$ của Định nghĩa 07.1 và tập $\widehat{\mathcal N}_K(q)$ gồm tối đa $K$ chỉ số phân biệt do một chỉ mục trả. *Độ thu hồi tại $K$* (recall@K) là

$$
\begin{aligned}
&\operatorname{recall@}K(q)\\
&\quad=\frac{|\widehat{\mathcal N}_K(q)\cap\mathcal N_K(q)|}{K}.
\end{aligned}
$$

Với một tập truy vấn hữu hạn $Q$, *độ thu hồi trung bình* là

$$
\begin{aligned}
&\overline{\operatorname{recall@}K}\\
&\quad=\frac1{|Q|}\sum_{q\in Q}\operatorname{recall@}K(q).
\end{aligned}
$$
:::

Tử số đếm các hàng xóm thật mà chỉ mục trả; mẫu số là $K$ dù chỉ mục trả ít hơn $K$ chỉ số, nên trả thiếu bị tính là thiếu. Khi $|\widehat{\mathcal N}_K(q)|=K$, định nghĩa trùng Định nghĩa 01.17. Độ thu hồi tại $K$ bằng 1 khi và chỉ khi $\widehat{\mathcal N}_K(q)=\mathcal N_K(q)$: chiều thuận vì giao có $K$ phần tử thì chứa cả $\mathcal N_K(q)$, mà $\widehat{\mathcal N}_K(q)$ có tối đa $K$ phần tử.

Độ thu hồi trung bình là một con số cho cả tập $Q$ và che mất cách lỗi phân bố. Ví dụ: với 10 truy vấn, nếu mỗi truy vấn tìm lại 9 trong 10 hàng xóm thật thì $\overline{\operatorname{recall@}10}=0{,}9$ nhưng không truy vấn nào nhận đủ tập đúng. Ứng dụng cần mọi truy vấn đạt một mức tối thiểu phải đo thêm phân phối của $\operatorname{recall@}K(q)$, không chỉ trung bình.

::: example Ví dụ 07.2 (Chỉ mục trả $\{y_4,y_5,y_1\}$)
**Dữ kiện.** Như Ví dụ 07.1: $d(q,y_1)=2{,}5$, $d(q,y_2)=1{,}2$, $d(q,y_3)=3{,}0$, $d(q,y_4)=0{,}8$, $d(q,y_5)=1{,}7$, $K=3$, $\mathcal N_3(q)=\{4,2,5\}$. Chỉ mục trả $\widehat{\mathcal N}_3(q)=\{4,5,1\}$.

**Độ thu hồi.** Giao là $\{4,5\}$, nên $\operatorname{recall@}3(q)=2/3$.

**Hai cách $y_2$ bị thiếu.** Chỉ mục không đo $y_2$ và trả ba điểm tốt nhất trong $\{y_1,y_3,y_4,y_5\}$, đúng là $\{y_4,y_5,y_1\}$. Hoặc chỉ mục đo cả năm điểm nhưng xếp hạng bằng một khoảng cách xấp xỉ $\widetilde d$ với $\widetilde d(q,y_2)>\widetilde d(q,y_1)$, chẳng hạn $\widetilde d(q,y_2)=2{,}6$.

**Kiểm tra lại.** Trong cả hai cách, $y_3$ ($3{,}0$) không được trả, và đầu ra có đúng ba chỉ số.
:::

Ví dụ 07.2 là trường hợp $|\widehat{\mathcal N}_K(q)|=K$ của Định nghĩa 07.4. Hai cách thiếu $y_2$ cho cùng một con số $2/3$, nên độ thu hồi không cho biết lỗi đến từ đâu.

::: remark Nhận xét 07.5 (Độ thu hồi theo hạng của bài báo PQ và của Faiss)
Bài báo PQ của Jégou, Douze và Schmid (§V-A, tr.8) đo chất lượng bằng *recall@R*: tỷ lệ truy vấn có hàng xóm gần nhất nằm trong $R$ vị trí đầu của danh sách trả về; bài giảng 8 (tr.3, tr.5) và sổ thực hành dùng $R=1$ (1-recall@1). Khi $K=R=1$, đại lượng này bằng $\overline{\operatorname{recall@}1}$ của Định nghĩa 07.4. Khi $K>1$, chúng khác nhau: trên Ví dụ 07.2, hàng xóm gần nhất $y_4$ nằm trong ba vị trí đầu, nên recall@3 theo nghĩa của bài báo bằng 1, còn $\operatorname{recall@}3(q)=2/3$. Trong sổ thực hành (ô mã 155), `nok/100` là $\overline{\operatorname{recall@}1}$ trên 100 truy vấn, dù lời gọi `search` trả 10 kết quả.
:::

### 1.3 Bốn trục đánh giá và hai thừa số chi phí

Một chỉ mục gần đúng đổi chất lượng lấy thời gian hoặc bộ nhớ, nên độ thu hồi một mình không xếp hạng được hai chỉ mục. Bài giảng 8 (tr.2–5) vẽ ba trục độ chính xác, bộ nhớ và tốc độ; bài giảng 9 (class 9) cùng học phần (tr.2) nêu thêm thời gian xây chỉ mục chậm là nhược điểm của chỉ mục đồ thị.

::: remark Nhận xét 07.6 (Bốn trục đánh giá một chỉ mục)
| Trục | Đại lượng đo | Giữ cố định khi so |
|---|---|---|
| Chất lượng | $\overline{\operatorname{recall@}K}$ | tập truy vấn $Q$, $K$, tập đúng |
| Truy vấn | độ trễ, số khoảng cách mỗi truy vấn | phần cứng, số luồng, kích thước lô |
| Xây dựng | thời gian xây, lượng dữ liệu huấn luyện | tham số chỉ mục |
| Bộ nhớ | byte mỗi véc-tơ, kể cả cấu trúc chỉ mục | có lưu véc-tơ gốc hay không |

Hai chỉ mục chỉ so được trên một trục khi các trục còn lại được giữ cố định hoặc được nêu kèm. Ví dụ: bài giảng 8 (tr.5) so các họ chỉ mục ở cùng ngân sách 32 byte mỗi véc-tơ.
:::

Để biết một chỉ mục tiết kiệm ở đâu, chúng ta tách chi phí của một truy vấn. Mọi chỉ mục trong chương chọn một tập $S\subseteq Y$ các véc-tơ được đo, đo mỗi véc-tơ trong $S$ bằng một khoảng cách $\widetilde d$ (có thể khác $d$), rồi trả $K$ phần tử tốt nhất của $S$ theo $\widetilde d$. Quét đầy đủ có $S=Y$ và $\widetilde d=d$. Ví dụ 07.2 có hai cách: $S=Y\setminus\{y_2\}$ với $\widetilde d=d$, hoặc $S=Y$ với $\widetilde d\ne d$.

::: proposition Mệnh đề 07.7 (Hai thừa số chi phí và hai nguồn thiếu điểm)
**Giả thiết.** Với truy vấn $q$, chỉ mục chọn tập $S\subseteq Y$ với $n_c=|S|$ phần tử, tính $\widetilde d(q,y)$ cho mọi $y\in S$, rồi trả $\widehat{\mathcal N}_K(q)$ gồm $\min(K,n_c)$ phần tử đầu của $S$ theo cặp $(\widetilde d(q,y_i),i)$ tăng dần.

**Kết luận.**

- (a) Chi phí truy vấn bằng chi phí chọn $S$, cộng $n_c$ lần chi phí tính một giá trị $\widetilde d$, cộng $O(n_c\log K)$ cho việc giữ $K$ phần tử tốt nhất.
- (b) Mọi $y_i$ với $i\in\mathcal N_K(q)$ và $y_i\notin S$ đều thiếu trong $\widehat{\mathcal N}_K(q)$.
- (c) Nếu $\widetilde d=d$ trên $S$ thì $\operatorname{recall@}K(q)=1$ khi và chỉ khi $\{y_i: i\in\mathcal N_K(q)\}\subseteq S$.
- (d) Nếu $\widetilde d=d$ trên $S$ thì mọi $i\in\mathcal N_K(q)$ với $y_i\in S$ thuộc $\widehat{\mathcal N}_K(q)$, nên $\operatorname{recall@}K(q)=|\{i\in\mathcal N_K(q):y_i\in S\}|/K$.

**Điều kiện áp dụng.** Mọi cách chọn $S$, ngẫu nhiên hay xác định, và mọi $\widetilde d$.

**Phạm vi.** Mệnh đề không chặn xác suất $y\in S$ hay độ lệch $|\widetilde d-d|$.
:::

::: proof Chứng minh Mệnh đề 07.7
**Bước 1 (chi phí).** Truy vấn gồm ba việc: chọn $S$; tính $n_c$ giá trị $\widetilde d$; chạy bước 2 và bước 3 của Thuật toán 07.2 trên $n_c$ giá trị đã tính, tốn $O(n_c\log K)$ theo Mệnh đề 07.3(b). Cộng ba phần được (a).

**Bước 2 (điểm ngoài $S$).** Theo giả thiết, $\widehat{\mathcal N}_K(q)$ chỉ chứa phần tử của $S$, nên một hàng xóm thật nằm ngoài $S$ không thuộc đầu ra. Điều này chứng minh (b).

**Bước 3 (chứng minh (d)).** Giả sử $\widetilde d=d$ trên $S$. Một hàng xóm thật $y_i\in S$ có ít hơn $K$ phần tử của $Y$ đứng trước nó theo $(d,\text{chỉ số})$, nên có ít hơn $K$ phần tử của $S$ đứng trước nó; vì vậy $y_i$ nằm trong $\min(K,n_c)$ phần tử đầu của $S$ và thuộc $\widehat{\mathcal N}_K(q)$. Theo (b), không hàng xóm thật nào ngoài $S$ thuộc đầu ra, nên tử số của độ thu hồi là $|\{i\in\mathcal N_K(q):y_i\in S\}|$.

**Bước 4 (chứng minh (c)).** Theo (d), độ thu hồi bằng 1 khi và chỉ khi tử số bằng $K$, tức mọi hàng xóm thật thuộc $S$. $\square$
:::

Mệnh đề 07.7(c) là dạng hàng xóm của Mệnh đề 01.16(c): xác minh chính xác trên tập ứng viên trả đủ kết quả khi và chỉ khi tập ứng viên chứa mọi kết quả. Kết luận (a) tách chi phí thành hai thừa số, $n_c$ và chi phí một phép đo; (b), (c) và (d) tách hai nguồn thiếu điểm, điểm không được đo và điểm được đo nhưng bị xếp sai. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $\widetilde d=d$ trong (c), (d): trong Ví dụ 07.2 với $S=Y$ và $\widetilde d(q,y_2)=2{,}6$, mọi hàng xóm thật thuộc $S$ nhưng độ thu hồi là $2/3$.
- Bỏ quy tắc trả phần tử đầu của $S$ theo $\widetilde d$: một chỉ mục đo cả năm điểm của Ví dụ 07.1 bằng $d$ rồi trả ba điểm đầu theo chỉ số, $\{1,2,3\}$, có độ thu hồi $1/3$ dù $S=Y$.

Bước 2 chỉ dùng $\widehat{\mathcal N}_K(q)\subseteq S$; Bước 3 dùng cả $\widetilde d=d$ lẫn quy tắc trả phần tử đầu.

Trong bảng sau, dòng LSH dùng Mệnh đề 06.26: với cấu trúc ghép đồng thời $r$ hàm rồi ít nhất một trên $b$ bảng, một véc-tơ có $d(q,y)\le d_1$ thuộc $S$ với xác suất ít nhất $1-(1-p_1^r)^b$.

| Cấu trúc | Thừa số được giảm | Lưu véc-tơ gốc | Hàng xóm thật bị thiếu vì |
|---|---|---|---|
| LSH (Bài 06) | $n_c$: chỉ đo véc-tơ chung thùng với $q$ | có | không chung thùng, xác suất nhiều nhất $(1-p_1^r)^b$ khi $d\le d_1$ (Kết luận (b)) |
| Đồ thị lân cận, HNSW (Mục 2–3) | $n_c$: chỉ đo đỉnh gặp trên đường đi | có | không được thấy trên đường đi (Kết luận (b)) |
| PQ quét đủ (Mục 4) | chi phí một phép đo, bộ nhớ | không | $\widetilde d\ne d$ xếp sai thứ tự (giả thiết của (d) bị bỏ) |
| IVF-PQ (Mục 5) | cả hai | không | nằm trong danh sách không mở, hoặc bị xếp sai |

**Trong thực hành.** Khi kho còn véc-tơ gốc, nguồn thiếu thứ hai được giảm bằng cách *xếp hạng lại* (re-ranking): tính lại khoảng cách đúng $d$ cho một danh sách ngắn các ứng viên đầu theo $\widetilde d$ rồi chọn $K$ phần tử; theo Mệnh đề 07.7(d), bước này giữ đúng mọi hàng xóm thật có mặt trong danh sách ngắn. Nguồn thiếu thứ nhất chỉ giảm khi $S$ lớn hơn, tức trả thêm ở thừa số $n_c$.

::: exercise Bài tập 07.1 (Thời gian quét đầy đủ)
Kho có $N=10^{10}$ véc-tơ, $D=3072$; giả sử máy xử lý $10^{13}$ thao tác mỗi giây.

- (a) Tính thời gian quét đầy đủ một truy vấn và số lần thời gian này vượt ngân sách 10 ms.
- (b) Tính số véc-tơ $n_c$ lớn nhất mà một truy vấn đo được bằng khoảng cách đúng trong 10 ms.
:::

::: hint
Một khoảng cách đúng tốn $D$ lượt tọa độ; trong 10 ms máy làm được $10^{13}\cdot0{,}01$ thao tác.
:::

::: solution
**Câu (a).** $ND=3{,}072\cdot10^{13}$ lượt tọa độ, tức $3{,}072$ giây, gấp $3{,}072/0{,}01=307{,}2$ lần ngân sách.

**Câu (b).** $n_cD\le10^{11}$ cho $n_c\le10^{11}/3072\approx3{,}26\cdot10^7$, tức khoảng $0{,}33\%$ kho.

**Kiểm tra lại.** $3{,}26\cdot10^7\cdot3072\approx10^{11}$; muốn vào ngân sách, chỉ mục phải giảm $n_c$ khoảng 300 lần hoặc giảm chi phí một phép đo, như Mệnh đề 07.7(a).
:::

::: exercise Bài tập 07.2 (Độ thu hồi của một truy vấn và của một tập truy vấn)
(a) Tập đúng của một truy vấn là $\mathcal N_5(q)=\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$, chỉ mục trả $\{\mathrm a,\mathrm c,\mathrm f,\mathrm g,\mathrm h\}$. Tính $\operatorname{recall@}5(q)$.

(b) Trên 10 truy vấn với $K=10$, chín truy vấn có độ thu hồi 1 và một truy vấn có độ thu hồi 0. Tính $\overline{\operatorname{recall@}10}$ và tỷ lệ truy vấn nhận đủ tập đúng.
:::

::: hint
Ở câu (b), một truy vấn nhận đủ tập đúng khi và chỉ khi độ thu hồi của nó bằng 1.
:::

::: solution
**Câu (a).** Giao là $\{\mathrm a,\mathrm c\}$, nên $\operatorname{recall@}5(q)=2/5$.

**Câu (b).** $\overline{\operatorname{recall@}10}=(9\cdot1+0)/10=0{,}9$; tỷ lệ truy vấn nhận đủ tập đúng là $9/10$.

**Kiểm tra lại.** Nếu mỗi truy vấn tìm lại 9 trong 10 hàng xóm thật, trung bình cũng là $0{,}9$ nhưng tỷ lệ nhận đủ tập đúng là 0; độ thu hồi trung bình không phân biệt hai trường hợp.
:::

::: exercise Bài tập 07.3 (Chọn giữa hai chỉ mục)
Trên cùng tập truy vấn, cùng $K=10$ và cùng phần cứng, chỉ mục A đạt $\overline{\operatorname{recall@}10}=0{,}9$ với độ trễ 5 ms, chỉ mục B đạt $0{,}7$ với độ trễ 2 ms. Ứng dụng đặt ngưỡng độ thu hồi tối thiểu $\tau$ và ngân sách độ trễ $T_{\max}$ (ms).

- (a) Xác định điều kiện để mỗi chỉ mục dùng được.
- (b) Xác định, theo $\tau$ và $T_{\max}$, khi nào chỉ chọn được A, khi nào chỉ chọn được B, khi nào chọn được cả hai và khi nào không chọn được chỉ mục nào.
:::

::: hint
Một chỉ mục dùng được khi độ thu hồi của nó ít nhất $\tau$ và độ trễ của nó không quá $T_{\max}$.
:::

::: solution
**Câu (a).** A dùng được khi $\tau\le0{,}9$ và $T_{\max}\ge5$; B dùng được khi $\tau\le0{,}7$ và $T_{\max}\ge2$.

**Câu (b).** Chỉ A: $0{,}7<\tau\le0{,}9$ và $T_{\max}\ge5$. Chỉ B: $\tau\le0{,}7$ và $2\le T_{\max}<5$. Cả hai: $\tau\le0{,}7$ và $T_{\max}\ge5$; khi đó chọn theo trục còn lại, như bộ nhớ (Nhận xét 07.6). Không chỉ mục nào: $\tau>0{,}9$, hoặc $T_{\max}<2$, hoặc $0{,}7<\tau\le0{,}9$ và $T_{\max}<5$.

**Kiểm tra lại.** Bốn vùng phủ hết các cặp $(\tau,T_{\max})$ và không chồng nhau; câu "B tốt hơn" hay "A tốt hơn" chỉ có nghĩa sau khi biết $\tau$ và $T_{\max}$.
:::

Như vậy, chúng ta đã đặt bài toán tìm gần đúng (Định nghĩa 07.1), có mốc chi phí $\Theta(ND)$ của quét đầy đủ (Mệnh đề 07.3), có độ thu hồi để đo chất lượng (Định nghĩa 07.4) và có phép tách chi phí thành $n_c$ nhân chi phí một phép đo cùng hai nguồn thiếu điểm (Mệnh đề 07.7). Tuy nhiên, cách giảm $n_c$ duy nhất đã có là LSH, mà với khoảng cách Euclid, bộ tham số $(a/2,2a,1/2,1/3)$ chỉ được chứng minh khi $D=2$ (Định lý 06.36), trong khi kho mở đầu có $D=3072$. Trong Mục 2, chúng ta giảm $n_c$ bằng cách đi theo quan hệ gần giữa các véc-tơ trên một đồ thị.

<!-- note-topic-id: lec-07-topic-02 -->
## 2. Tìm kiếm trên đồ thị lân cận

Trên kho mở đầu, quét đầy đủ đo $n_c=10^{10}$ véc-tơ cho mỗi truy vấn, trong khi ngân sách 10 ms chỉ đủ cho khoảng $3{,}3\cdot10^6$ khoảng cách đúng ở $10^{12}$ thao tác mỗi giây. Nếu mỗi véc-tơ được nối với vài véc-tơ gần nó, một phép đi từ điểm xuất phát về phía $q$ chỉ đo các điểm gặp trên đường. Chúng ta cần biết phép đi dừng khi nào, dừng ở đâu và tốn bao nhiêu phép đo.

### 2.1 Đồ thị lân cận và tìm kiếm tham lam

Đồ thị bảy đỉnh trên hình dưới được dùng xuyên suốt mục này: mỗi đỉnh là một véc-tơ của kho, số ghi bên tên đỉnh là khoảng cách tới $q$, mỗi đoạn thẳng là hai cạnh có hướng ngược nhau, và điểm xuất phát là $\mathrm e$.

![Đồ thị bảy đỉnh e, a, b, s, t, u, z có khoảng cách tới q lần lượt 9, 7, 5, 8, 4, 2, 1; cạnh e–a, a–b, e–s, s–t, t–u, u–z; điểm vào là e.](img/lec-07/do-thi-vi-du.svg)

Vị trí các đỉnh trên hình giữ thứ tự khoảng cách tới $q$. Từ $\mathrm e$ có hai hướng: nhánh $\mathrm a,\mathrm b$ bắt đầu gần $q$ hơn ($\mathrm a{:}7<\mathrm s{:}8$) nhưng dừng ở $\mathrm b{:}5$; nhánh $\mathrm s,\mathrm t,\mathrm u,\mathrm z$ bắt đầu xa hơn nhưng dẫn tới đỉnh gần $q$ nhất.

::: definition Định nghĩa 07.8 (Đồ thị lân cận và chỉ mục đồ thị)
Một *đồ thị lân cận* (proximity graph) trên kho $Y$ là đồ thị có hướng $G=(Y,E)$ với mỗi đỉnh là một véc-tơ của kho; tập *lân cận* $\mathcal L(y)=\{v:(y,v)\in E\}$ của $y$ gồm vài véc-tơ gần $y$. Một *chỉ mục đồ thị* (graph index) lưu các véc-tơ, danh sách lân cận của mọi đỉnh và một *điểm vào* (entry point) cố định $s\in Y$. Với mã định danh $s_{id}$ byte và bậc ra trung bình $g$, chỉ mục chiếm

$$
N\cdot(4D+s_{id}\,g)\ \text{byte}
$$

khi mỗi tọa độ là số thực 4 byte (bài giảng 9, tr.7, với $s_{id}=4$).
:::

Chỉ mục đồ thị không đổi khoảng cách: mỗi véc-tơ được đo bằng đúng $d$, nên theo Mệnh đề 07.7, hàng xóm thật chỉ thiếu khi không được đo. Đồ thị lân cận khác *đồ thị $k$ hàng xóm* (k-nearest-neighbor graph): định nghĩa không đòi $\mathcal L(y)$ là đúng các điểm gần $y$ nhất, và quan hệ lân cận có thể không đối xứng.

Phép đi đơn giản nhất là *tìm kiếm tham lam* (greedy search; bài giảng 9, tr.8): bắt đầu ở điểm vào, ở mỗi bước đo các lân cận của đỉnh hiện tại và sang lân cận gần $q$ nhất nếu nó gần $q$ hơn đỉnh hiện tại; nếu không, dừng. Khoảng cách đã đo được ghi nhớ, nên mỗi đỉnh được đo nhiều nhất một lần.

Mỗi đỉnh mang chỉ số của véc-tơ tương ứng trong $Y$; tên chữ như $\mathrm b$ chỉ là nhãn. Ta viết $u\prec v$ khi $(d(u,q),u)$ đứng trước $(d(v,q),v)$ theo thứ tự từ điển, và $u\preceq v$ khi $u\prec v$ hoặc $u=v$; hai đỉnh cách $q$ bằng nhau thì đỉnh có chỉ số nhỏ đứng trước.

::: example Ví dụ 07.3 (Tham lam trên đồ thị bảy đỉnh)
**Dữ kiện.** Đồ thị bảy đỉnh với $\mathrm e{:}9$, $\mathrm a{:}7$, $\mathrm b{:}5$, $\mathrm s{:}8$, $\mathrm t{:}4$, $\mathrm u{:}2$, $\mathrm z{:}1$; cạnh hai chiều $\mathrm e$–$\mathrm a$, $\mathrm a$–$\mathrm b$, $\mathrm e$–$\mathrm s$, $\mathrm s$–$\mathrm t$, $\mathrm t$–$\mathrm u$, $\mathrm u$–$\mathrm z$; điểm vào $\mathrm e$.

**Vết chạy.**

| Đỉnh hiện tại | Lân cận và khoảng cách | Đỉnh đo mới | Quyết định |
|---|---|---|---|
| $\mathrm e{:}9$ | $\mathrm a{:}7$, $\mathrm s{:}8$ | $\mathrm a$, $\mathrm s$ | sang $\mathrm a$ vì $7<9$ |
| $\mathrm a{:}7$ | $\mathrm e{:}9$, $\mathrm b{:}5$ | $\mathrm b$ | sang $\mathrm b$ vì $5<7$ |
| $\mathrm b{:}5$ | $\mathrm a{:}7$ | không | dừng vì $7>5$ |

**Kết quả.** Tham lam trả $\mathrm b{:}5$ sau 4 phép đo ($\mathrm e$; $\mathrm a$, $\mathrm s$; $\mathrm b$), không đo $\mathrm t$, $\mathrm u$, $\mathrm z$.

**Kiểm tra lại.** Đỉnh gần $q$ nhất là $\mathrm z{:}1$; tham lam bỏ nhánh $\mathrm e\to\mathrm s$ ngay bước đầu vì $\mathrm s{:}8$ xa hơn $\mathrm a{:}7$.
:::

![Tìm kiếm tham lam đi từ e qua a tới b có khoảng cách 5 rồi dừng; z có khoảng cách 1 nằm trên nhánh e, s, t, u.](img/lec-07/do-thi-tham-lam.svg)

Trên hình, đường đi tham lam là $\mathrm e\to\mathrm a\to\mathrm b$, còn nhánh $\mathrm s,\mathrm t,\mathrm u,\mathrm z$ không được đi. Thuật toán sau viết lại các bước của Ví dụ 07.3.

::: algorithm Thuật toán 07.9 (Tìm kiếm tham lam trên đồ thị lân cận)
**Đầu vào.** Đồ thị lân cận $G$ với điểm vào $s$; truy vấn $q$.

**Đầu ra.** Một đỉnh $v$ của $G$; theo Mệnh đề 07.11(b), $v$ là một cực tiểu cục bộ.

**Giả thiết.** Quan hệ $\prec$ phá hòa theo chỉ số; khoảng cách đã đo được ghi nhớ.

1. Đặt $v\leftarrow s$ và đo $d(s,q)$.
2. Đo $d(w,q)$ cho mọi $w\in\mathcal L(v)$ chưa đo; gọi $w^*$ là lân cận nhỏ nhất của $v$ theo $\prec$.
3. Nếu $w^*\prec v$, đặt $v\leftarrow w^*$ và quay lại bước 2; ngược lại trả $v$.

**Dừng.** Sau nhiều nhất $N-1$ lần di chuyển (Mệnh đề 07.11(a)).

**Trường hợp biên.** Khi $\mathcal L(v)$ rỗng, thủ tục trả $v$.

**Chi phí.** Mỗi lượt bước 2 tốn nhiều nhất $|\mathcal L(v)|$ khoảng cách, mỗi khoảng cách $\Theta(D)$, và $|\mathcal L(v)|$ phép so.
:::

Đỉnh $\mathrm b$ mà Ví dụ 07.3 trả về không có lân cận nào gần $q$ hơn nó, dù đồ thị có đỉnh gần $q$ hơn nhiều. Định nghĩa sau gọi tên tình trạng này.

::: definition Định nghĩa 07.10 (Cực tiểu cục bộ)
Trong đồ thị lân cận $G$ với truy vấn $q$, đỉnh $v$ là một *cực tiểu cục bộ* (local minimum) nếu không lân cận nào của $v$ gần $q$ hơn $v$, tức $v\prec w$ với mọi $w\in\mathcal L(v)$.
:::

Đỉnh gần $q$ nhất của đồ thị luôn là một cực tiểu cục bộ, nhưng điều ngược lại sai: trong đồ thị bảy đỉnh, $\mathrm b{:}5$ và $\mathrm z{:}1$ đều là cực tiểu cục bộ, còn chỉ $\mathrm z$ gần $q$ nhất. Định nghĩa chỉ xét lân cận trực tiếp nên phụ thuộc vào cạnh của đồ thị: thêm cạnh $\mathrm b$–$\mathrm t$ làm $\mathrm b$ hết là cực tiểu cục bộ.

![Từ e, tham lam đi qua a tới b; b không có lân cận gần q hơn nên là cực tiểu cục bộ; z ở khoảng cách 1 là đỉnh gần q nhất, nằm trên nhánh s, t, u; cạnh e–s nét đứt bị loại ở bước đầu vì a gần q hơn s.](img/lec-07/cuc-tieu-cuc-bo.svg)

Trên hình, $\mathrm b$ là cực tiểu cục bộ, còn $\mathrm z$ là đỉnh gần $q$ nhất; cạnh nét đứt $\mathrm e$–$\mathrm s$ là chỗ tham lam rẽ sai. Mệnh đề sau nói tham lam luôn dừng, và dừng ở một cực tiểu cục bộ.

::: proposition Mệnh đề 07.11 (Tham lam dừng ở cực tiểu cục bộ)
**Giả thiết.** Đồ thị lân cận $G$ hữu hạn với $N$ đỉnh; điểm vào $s$; quan hệ $\prec$ phá hòa theo chỉ số; tìm kiếm tham lam theo Thuật toán 07.9.

**Kết luận.**

- (a) Tìm kiếm tham lam dừng sau nhiều nhất $N-1$ bước di chuyển.
- (b) Đỉnh trả về là một cực tiểu cục bộ.
- (c) Số phép đo nhiều nhất là $1+\sum_{v}|\mathcal L(v)|$, tổng lấy trên các đỉnh của đường đi.

**Điều kiện áp dụng.** Mọi đồ thị có hướng hữu hạn và mọi điểm vào.

**Phạm vi.** Mệnh đề không bảo đảm đỉnh trả về gần $q$ nhất, cũng không bảo đảm đỉnh đó thuộc $\mathcal N_K(q)$ với $K\ge1$.
:::

::: proof Chứng minh Mệnh đề 07.11
**Bước 1 (dừng).** Mỗi bước di chuyển sang một đỉnh đứng trước đỉnh hiện tại theo $\prec$, là một thứ tự toàn phần chặt trên $N$ đỉnh. Dãy đỉnh của đường đi vì thế giảm ngặt, không lặp đỉnh, nên có nhiều nhất $N$ đỉnh và nhiều nhất $N-1$ bước.

**Bước 2 (cực tiểu cục bộ).** Thủ tục dừng ở $v$ khi lân cận nhỏ nhất $w^*$ của $v$ theo $\prec$ không đứng trước $v$, tức $v\prec w^*$; vì $w^*$ nhỏ nhất, $v\prec w$ với mọi $w\in\mathcal L(v)$. Theo Định nghĩa 07.10, $v$ là cực tiểu cục bộ.

**Bước 3 (số phép đo).** Thủ tục đo điểm vào một lần, rồi ở mỗi đỉnh của đường đi đo các lân cận chưa đo, nhiều nhất $|\mathcal L(v)|$ phép. $\square$
:::

Ví dụ 07.3 là trường hợp đường đi $\mathrm e,\mathrm a,\mathrm b$: hai bước di chuyển, dừng ở cực tiểu cục bộ $\mathrm b$, và cận (c) cho $1+2+2+1=6$ phép đo, còn thực tế là 4 vì $\mathrm e$ và $\mathrm a$ đã đo trước khi được xét lại làm lân cận. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ phá hòa và cho phép sang lân cận không xa hơn: hai đỉnh $\mathrm a{:}5$, $\mathrm b{:}5$ nối nhau, tham lam đi $\mathrm a\to\mathrm b\to\mathrm a\to\cdots$ không dừng.
- Bỏ tính hữu hạn: trên dãy vô hạn đỉnh $v_1,v_2,\ldots$ với $d(v_n,q)=1+1/n$ và cạnh $v_n\to v_{n+1}$, mỗi bước đều gần hơn và tham lam không dừng.

Bước 1 dùng cả thứ tự chặt và tính hữu hạn; Bước 2 chỉ dùng điều kiện dừng.

### 2.2 Tìm kiếm chùm và `SEARCH-LAYER`

Tham lam chỉ giữ một hướng, nên một lựa chọn sai ở bước đầu là đủ để mất $\mathrm z$. Một cách trực quan, nếu giữ lại vài đỉnh tốt nhất đã thấy thay vì một, thì khi nhánh đang đi bị tắc, phép tìm còn quay lại được nhánh dự phòng. *Tìm kiếm chùm* (beam search) duy trì hai tập: $C$ gồm các đỉnh đã thấy nhưng chưa mở, và $W$ gồm tối đa $ef$ đỉnh gần $q$ nhất đã thấy; số nguyên $ef\ge1$ là *bề rộng chùm* (beam width). Mỗi bước mở đỉnh gần $q$ nhất trong $C$, tức đo các lân cận chưa thấy của nó. Một lân cận vào $C$ và $W$ khi $W$ chưa đủ $ef$ đỉnh hoặc khi nó gần $q$ hơn đỉnh xa nhất $f$ của $W$; nếu $W$ vượt $ef$ đỉnh thì bỏ đỉnh xa nhất. Phép tìm dừng khi $C$ rỗng hoặc khi đỉnh sắp mở xa $q$ hơn $f$ (bài giảng 9, tr.9). Để làm rõ quy tắc, xem ví dụ sau.

::: example Ví dụ 07.4 (Tìm kiếm chùm với $ef=3$)
**Dữ kiện.** Đồ thị bảy đỉnh của Ví dụ 07.3, với khoảng cách tới $q$ và cạnh như ở đó; khởi tạo $C=W=\{\mathrm e\}$; $ef=3$.

**Vết chạy.** Cột "Kiểm dừng" so đỉnh vừa lấy khỏi $C$ với đỉnh xa nhất $f$ của $W$ trước khi mở.

| Mở | Kiểm dừng | Lân cận mới | $C$ sau bước | $W$ sau bước | $f$ sau bước |
|---|---|---|---|---|---|
| $\mathrm e{:}9$ | $9\le9$ | $\mathrm a{:}7$, $\mathrm s{:}8$ | $\mathrm a,\mathrm s$ | $\mathrm a,\mathrm s,\mathrm e$ | $\mathrm e{:}9$ |
| $\mathrm a{:}7$ | $7\le9$ | $\mathrm b{:}5$; bỏ $\mathrm e$ khỏi $W$ | $\mathrm b,\mathrm s$ | $\mathrm b,\mathrm a,\mathrm s$ | $\mathrm s{:}8$ |
| $\mathrm b{:}5$ | $5\le8$ | không | $\mathrm s$ | $\mathrm b,\mathrm a,\mathrm s$ | $\mathrm s{:}8$ |
| $\mathrm s{:}8$ | $8\le8$ | $\mathrm t{:}4$; bỏ $\mathrm s$ khỏi $W$ | $\mathrm t$ | $\mathrm t,\mathrm b,\mathrm a$ | $\mathrm a{:}7$ |
| $\mathrm t{:}4$ | $4\le7$ | $\mathrm u{:}2$; bỏ $\mathrm a$ | $\mathrm u$ | $\mathrm u,\mathrm t,\mathrm b$ | $\mathrm b{:}5$ |
| $\mathrm u{:}2$ | $2\le5$ | $\mathrm z{:}1$; bỏ $\mathrm b$ | $\mathrm z$ | $\mathrm z,\mathrm u,\mathrm t$ | $\mathrm t{:}4$ |
| $\mathrm z{:}1$ | $1\le4$ | không | rỗng | $\mathrm z,\mathrm u,\mathrm t$ | $\mathrm t{:}4$ |

**Kết quả.** Phép tìm dừng vì $C$ rỗng và trả $W=\{\mathrm z,\mathrm u,\mathrm t\}$, đúng ba đỉnh gần $q$ nhất của đồ thị, sau 7 phép đo.

**Kiểm tra lại.** Khi mở $\mathrm b$, lân cận duy nhất $\mathrm a$ đã thấy, nhưng $\mathrm s{:}8$ còn trong $C$; đó là nhánh dự phòng mà tham lam đã bỏ ở Ví dụ 07.3.
:::

![Tìm kiếm chùm với ef bằng 3 giữ s trong hàng đợi; khi b không còn lân cận mới, thuật toán mở s rồi đi qua t, u tới z có khoảng cách 1.](img/lec-07/do-thi-chum.svg)

Trên hình, tìm kiếm chùm đi tiếp theo nhánh được tô $\mathrm e\to\mathrm s\to\mathrm t\to\mathrm u\to\mathrm z$ sau khi $\mathrm b$ hết lân cận mới. Ở dòng thứ tư của vết, phép kiểm dừng so $c=\mathrm s$ với $f$, mà lúc đó $f$ chính là $\mathrm s$, nên không dừng và $\mathrm s$ được mở dù nó xa hơn $\mathrm b$ và $\mathrm a$. Thuật toán sau viết quy tắc này theo Thuật toán 2 của bài báo HNSW (Malkov và Yashunin, tr.4) với tham số tầng $\ell_c$; khi chỉ có một đồ thị, $\ell_c=0$.

::: algorithm Thuật toán 07.12 (SEARCH-LAYER)
**Đầu vào.** Truy vấn $q$; tập điểm vào $ep$ gồm các đỉnh của tầng $\ell_c$; bề rộng chùm $ef$; đồ thị lân cận của tầng $\ell_c$.

**Đầu ra.** Tập $W$ gồm tối đa $ef$ đỉnh, là các đỉnh gần $q$ nhất theo $\prec$ trong tập $V$ các đỉnh đã thấy.

**Giả thiết.** $ef\ge1$ và $1\le|ep|\le ef$; tầng hữu hạn; quan hệ $\prec$ phá hòa theo chỉ số. $V$ là tập băm, $C$ là đống cực tiểu và $W$ là đống cực đại theo $\prec$.

1. Đặt $V\leftarrow ep$, $C\leftarrow ep$, $W\leftarrow ep$.
2. Khi $C$ khác rỗng: lấy $c$ là đỉnh nhỏ nhất theo $\prec$ ra khỏi $C$; đặt $f$ là đỉnh lớn nhất của $W$. Nếu $f\prec c$, dừng vòng lặp.
3. Với mỗi lân cận $y$ của $c$ ở tầng $\ell_c$ mà $y\notin V$: thêm $y$ vào $V$; đặt lại $f$ là đỉnh lớn nhất của $W$; nếu $|W|<ef$ hoặc $y\prec f$ thì thêm $y$ vào $C$ và $W$, và nếu $|W|>ef$ thì bỏ đỉnh lớn nhất khỏi $W$.
4. Trả $W$.

```text
SEARCH-LAYER(q, ep, ef, ℓc)
V ← ep;  C ← ep;  W ← ep
while C khác rỗng:
    c ← lấy ra đỉnh gần q nhất trong C
    f ← đỉnh xa q nhất trong W
    if f ≺ c: break
    for y in lân cận của c ở tầng ℓc:
        if y ∉ V:
            thêm y vào V
            f ← đỉnh xa q nhất trong W
            if |W| < ef or y ≺ f:
                thêm y vào C và W
                if |W| > ef: bỏ đỉnh xa q nhất khỏi W
return W
```

**Dừng.** Lệnh `break` ở bước 2, hoặc $C$ rỗng.

**Trường hợp biên.** Khi phần tầng đi tới được từ $ep$ có ít hơn $ef$ đỉnh, $W=V$ có ít hơn $ef$ đỉnh. Khi $ef=1$, thủ tục là tìm kiếm tham lam (Hệ quả 07.14).

**Chi phí.** Gọi $V$ là tập đã thấy khi dừng và $g_c=|\mathcal L(c)|$.

| Việc | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| tính $d(y,q)$ khi $y$ vào $V$ | $|V|$ | $\Theta(D)$ | $\Theta(|V|D)$ |
| lấy $c$ khỏi $C$ | nhiều nhất $|V|$ | $O(\log|V|)$ | $O(|V|\log|V|)$ |
| duyệt lân cận và tra $V$ | $\sum_{c\text{ được mở}}g_c$ | $O(1)$ kỳ vọng | $O\big(\sum g_c\big)$ |
| thêm vào $C$, $W$; bỏ khỏi $W$ | nhiều nhất $|V|$ | $O(\log|V|)$ | $O(|V|\log|V|)$ |
:::

Thao tác quyết định của Thuật toán 07.12 là phép so với $f$. Khi $|W|<ef$, đỉnh mới luôn được nhận; khi $W$ đã đủ, chỉ đỉnh gần $q$ hơn $f$ mới được nhận. Ngưỡng phải tính lại trong vòng lân cận vì $W$ đổi sau mỗi lần thêm và bỏ: ở dòng thứ tư của Ví dụ 07.4, khi mở $\mathrm s$, $f=\mathrm s{:}8$; sau khi $\mathrm t{:}4$ vào và $\mathrm s$ bị bỏ, ngưỡng mới là $\mathrm a{:}7$. Thủ tục phân biệt "thấy" (vào $V$, đã đo) với "mở" (lấy khỏi $C$ và duyệt lân cận); một đỉnh đã thấy mà không vào $C$ thì không bao giờ được mở.

![Trạng thái sau khi mở b với ef bằng 3: V gồm e, a, b, s; C gồm s; W gồm b, a, s; C và W là tập con của V; s thuộc cả C và W; e chỉ thuộc V.](img/lec-07/search-layer-trang-thai.svg)

Trạng thái trên hình là trạng thái sau dòng thứ ba của Ví dụ 07.4: $\mathrm e$ đã thấy và đã mở nhưng đã rời $W$; $\mathrm s$ thuộc cả $C$ và $W$ nên còn được mở. Mệnh đề sau nói $W$ đúng đến mức nào.

::: proposition Mệnh đề 07.13 (Tính đúng của SEARCH-LAYER)
**Giả thiết.** Như Thuật toán 07.12: tầng hữu hạn, $ef\ge1$, $1\le|ep|\le ef$, $\prec$ phá hòa theo chỉ số.

**Kết luận.**

- (a) Thuật toán 07.12 dừng; mỗi đỉnh vào $C$ nhiều nhất một lần.
- (b) Sau khởi tạo và sau mỗi lần một đỉnh vào $V$, $W$ là tập $\min(ef,|V|)$ đỉnh nhỏ nhất của $V$ theo $\prec$.
- (c) Khi thuật toán dừng, mọi đỉnh của $W$ đã được mở.

**Điều kiện áp dụng.** Mọi đồ thị có hướng hữu hạn, mọi tập điểm vào thỏa giả thiết.

**Phạm vi.** Kết luận (b) chỉ nói về $V$. Một đỉnh ngoài $V$ có thể gần $q$ hơn mọi đỉnh của $W$.
:::

::: proof Chứng minh Mệnh đề 07.13
**Bước 1 (dừng).** Một đỉnh chỉ vào $C$ ở khởi tạo hoặc ở bước 3, và bước 3 chỉ xét $y\notin V$ rồi thêm ngay $y$ vào $V$; vì đỉnh không rời $V$, mỗi đỉnh vào $C$ nhiều nhất một lần. Mỗi lượt của bước 2 lấy một đỉnh khỏi $C$, nên số lượt không vượt $|V|$, và $|V|$ không vượt số đỉnh của tầng. Điều này chứng minh (a).

**Bước 2 (khởi tạo của (b)).** Sau bước 1, $W=V=ep$ và $|ep|\le ef$, nên $W$ là toàn bộ $\min(ef,|V|)=|V|$ đỉnh của $V$.

**Bước 3 (duy trì của (b), trường hợp $|W|<ef$).** Theo bất biến, $|W|=\min(ef,|V|)<ef$ nên $W=V$. Đỉnh mới $y$ được thêm vào $W$, nên $W=V\cup\{y\}$ có $|V|+1\le ef$ đỉnh, đúng là $\min(ef,|V\cup\{y\}|)$ đỉnh nhỏ nhất.

**Bước 4 (duy trì của (b), trường hợp $|W|=ef$).** $W$ là $ef$ đỉnh nhỏ nhất của $V$, với đỉnh lớn nhất $f$. Nếu $y\prec f$, $ef$ đỉnh nhỏ nhất của $V\cup\{y\}$ gồm $y$ và $ef-1$ đỉnh nhỏ nhất của $V$, tức $W\setminus\{f\}$; thuật toán thêm $y$ rồi bỏ $f$, cho đúng tập đó. Nếu $f\prec y$, có $ef$ đỉnh của $V$ đứng trước $y$, nên $y$ không thuộc $ef$ đỉnh nhỏ nhất và $W$ giữ nguyên. Trường hợp $y=f$ không xảy ra vì $y\notin V$, và hai đỉnh khác nhau không hòa vì $\prec$ phá hòa. Các thao tác trên $C$ không đổi $V$, $W$, nên (b) được duy trì.

**Bước 5 (kết thúc, chứng minh (c)).** Mọi đỉnh của $W$ đã vào $C$ cùng lúc vào $W$. Nếu dừng vì $C$ rỗng, mọi đỉnh từng vào $C$ đã được lấy ra và mở. Nếu dừng bằng `break` ở đỉnh $c$, giả sử một $w\in W$ còn trong $C$; khi đó $w\preceq f\prec c$, trái với việc $c$ nhỏ nhất trong $C$. Vậy mọi đỉnh của $W$ đã rời $C$ trước $c$, ở những lượt không có `break`, tức đã được mở. $\square$
:::

Mệnh đề 07.13(b) là bất biến của Thuật toán 07.2 chuyển sang tập $V$ thay đổi: Thuật toán 07.2 giữ $K$ điểm tốt nhất của phần kho đã đọc, còn `SEARCH-LAYER` giữ $ef$ đỉnh tốt nhất của phần đồ thị đã thấy.

Kết luận (c) giải thích lệnh `break`: khi đỉnh gần nhất còn chờ đã xa hơn mọi đỉnh của $W$, mọi đỉnh của $W$ đã được mở. Mở tiếp các đỉnh xa hơn vẫn có thể gặp đỉnh tốt hơn, nên kết quả là gần đúng. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $|ep|\le ef$: với $ef=1$ và $ep=\{\mathrm e,\mathrm a\}$ trên đồ thị bảy đỉnh, khởi tạo cho $|W|=2>ef$, nên (b) sai ngay sau bước 1; mỗi lần thêm chỉ bỏ một đỉnh, nên thủ tục trả $W=\{\mathrm b,\mathrm a\}$ gồm hai đỉnh dù $ef=1$.
- Bỏ phép kiểm $y\notin V$: với $ef=8$ trên đồ thị bảy đỉnh, $|W|<ef$ luôn đúng, nên mở $\mathrm e$ thêm $\mathrm a$ vào $C$, mở $\mathrm a$ thêm lại $\mathrm e$, mở $\mathrm e$ thêm lại $\mathrm a$, và $C$ không bao giờ rỗng; thủ tục không dừng.
- Bỏ phá hòa: với $ef=1$, $ep=\{\mathrm a\}$ và hai lân cận $\mathrm b$, $\mathrm b'$ cùng cách $q$ là 5, đỉnh còn lại trong $W$ phụ thuộc thứ tự duyệt lân cận, nên "tập $ef$ đỉnh nhỏ nhất" ở (b) không xác định.

Bước 2 dùng $|ep|\le ef$; Bước 1 dùng phép kiểm $y\notin V$ và tính hữu hạn; Bước 4 dùng phá hòa.

::: corollary Hệ quả 07.14 (SEARCH-LAYER với $ef=1$ là tìm kiếm tham lam)
**Giả thiết.** Như Mệnh đề 07.13, với $ef=1$ và $ep=\{s\}$.

**Kết luận.** Các đỉnh được mở, theo thứ tự, là đường đi của Thuật toán 07.9 từ $s$; $W$ khi dừng chỉ gồm đỉnh Thuật toán 07.9 trả về; hai thủ tục đo cùng tập đỉnh.

**Điều kiện áp dụng.** Mọi đồ thị lân cận hữu hạn.

**Phạm vi.** Hệ quả so hai thủ tục trên cùng đồ thị; nó không nói đỉnh trả về gần $q$ nhất.
:::

::: proof Chứng minh Hệ quả 07.14
Gọi $u_1=s,u_2,\ldots$ là đường đi của Thuật toán 07.9. Ta chứng minh bằng quy nạp: lượt mở thứ $t$ mở $u_t$, và sau lượt đó $W=\{u_{t+1}\}$ nếu tham lam đi tiếp, $W=\{u_t\}$ nếu tham lam dừng.

**Bước 1 (một đỉnh trong $W$ là nhỏ nhất của $V$).** Với $ef=1$, Mệnh đề 07.13(b) cho $W=\{w\}$ với $w$ nhỏ nhất của $V$ theo $\prec$.

**Bước 2 (lượt mở $u_t$).** Trước lượt này $W=\{u_t\}$, nên mọi lân cận của $u_t$ đã thuộc $V$ đều đứng sau $u_t$. Sau khi xét các lân cận chưa thấy, $W$ chứa đỉnh nhỏ nhất của $\{u_t\}\cup\mathcal L(u_t)$, đúng là đỉnh mà tham lam sang, hoặc chính $u_t$ nếu tham lam dừng.

**Bước 3 (lượt kế tiếp).** Nếu $W=\{u_{t+1}\}$ với $u_{t+1}\ne u_t$, đỉnh này đã vào $C$ và là nhỏ nhất của $V\supseteq C$, nên lượt kế tiếp mở đúng $u_{t+1}$ mà không gặp `break`. Nếu $W=\{u_t\}$, mọi đỉnh còn trong $C$ thuộc $V\setminus\{u_t\}$ nên đứng sau $f=u_t$; lượt kế tiếp gặp `break` hoặc $C$ rỗng.

**Bước 4 (hai tập đo trùng nhau).** Cả hai thủ tục đo $s$ và các lân cận của những đỉnh được mở. Theo Bước 2 và Bước 3, hai tập đỉnh được mở trùng nhau, và lượt cuối của `SEARCH-LAYER` (`break` hoặc $C$ rỗng) không đo thêm, nên hai tập đo trùng nhau. $\square$
:::

::: example Ví dụ 07.5 (SEARCH-LAYER với $ef=2$ dừng sớm)
**Dữ kiện.** Đồ thị bảy đỉnh của Ví dụ 07.3 với khoảng cách và cạnh như ở đó; $ep=\{\mathrm e\}$; $ef=2$.

**Mở $\mathrm e$.** $\mathrm a{:}7$ vào vì $|W|=1<2$; $\mathrm s{:}8$ vào vì $8<9=f$, rồi $\mathrm e$ bị bỏ. $W=\{\mathrm a,\mathrm s\}$, $C=\{\mathrm a,\mathrm s\}$.

**Mở $\mathrm a$.** $\mathrm b{:}5$ vào vì $5<8$, rồi $\mathrm s$ bị bỏ khỏi $W$ nhưng còn trong $C$. $W=\{\mathrm b,\mathrm a\}$, $C=\{\mathrm b,\mathrm s\}$.

**Mở $\mathrm b$.** Không lân cận mới. $C=\{\mathrm s\}$.

**Dừng.** Lấy $\mathrm s{:}8$ khỏi $C$; $f=\mathrm a{:}7\prec\mathrm s$, nên `break`. Kết quả $W=\{\mathrm b,\mathrm a\}$, $V=\{\mathrm e,\mathrm a,\mathrm s,\mathrm b\}$.

**Kiểm tra lại.** $\mathrm b{:}5$ và $\mathrm a{:}7$ đúng là hai đỉnh nhỏ nhất của $V$, như Mệnh đề 07.13(b); $\mathrm z{:}1\notin V$ vì $\mathrm s$ không được mở.
:::

![Với ef bằng 2 và điểm vào e, thuật toán dừng khi đã thấy e, a, s, b; W gồm b và a; t, u, z chưa được thấy.](img/lec-07/do-thi-ef2.svg)

Bốn đỉnh đã thấy $\mathrm e,\mathrm a,\mathrm s,\mathrm b$ tách khỏi ba đỉnh chưa thấy $\mathrm t,\mathrm u,\mathrm z$. Ví dụ 07.5 là phản ví dụ cho việc đọc Mệnh đề 07.13 như một bảo đảm toàn cục: $W$ đúng trên bốn đỉnh đã thấy, còn ba đỉnh gần $q$ nhất nằm ngoài $V$.

::: remark Nhận xét 07.15 (Trong thực hành: bề rộng chùm và bộ nhớ)
Trong cài đặt, $V$ là mảng đánh dấu hoặc tập băm, $C$ và $W$ là hai đống nhị phân. Tăng $ef$ giữ nhiều hướng hơn trong $W$, đổi lại mở nhiều đỉnh hơn: Ví dụ 07.4 và 07.5 cho 7 và 4 phép đo. Trường hợp xấu, `SEARCH-LAYER` thấy mọi đỉnh của tầng và chi phí bằng một lần quét đầy đủ cộng chi phí hàng đợi. Bài giảng 9 (tr.9) ghi rằng tìm kiếm chùm cho độ thu hồi cao và độ trễ thấp khi cả dữ liệu lẫn đồ thị nằm trong bộ nhớ, và một máy chỉ chứa khoảng $10^8$ điểm.
:::

::: exercise Bài tập 07.4 (Điểm vào khác)
Trên đồ thị bảy đỉnh với $\mathrm e{:}9$, $\mathrm a{:}7$, $\mathrm b{:}5$, $\mathrm s{:}8$, $\mathrm t{:}4$, $\mathrm u{:}2$, $\mathrm z{:}1$ và cạnh hai chiều $\mathrm e$–$\mathrm a$, $\mathrm a$–$\mathrm b$, $\mathrm e$–$\mathrm s$, $\mathrm s$–$\mathrm t$, $\mathrm t$–$\mathrm u$, $\mathrm u$–$\mathrm z$, chạy Thuật toán 07.9 từ điểm vào $\mathrm s$.

- (a) Ghi vết chạy.
- (b) Ghi đường đi, đỉnh trả về và số phép đo; so với lượt chạy từ $\mathrm e$.
:::

::: hint
Lân cận của $\mathrm s$ là $\mathrm e$ và $\mathrm t$.
:::

::: solution
**Câu (a).** Từ $\mathrm s{:}8$ đo $\mathrm e{:}9$, $\mathrm t{:}4$, sang $\mathrm t$. Từ $\mathrm t$ đo $\mathrm u{:}2$, sang $\mathrm u$. Từ $\mathrm u$ đo $\mathrm z{:}1$, sang $\mathrm z$. Lân cận duy nhất của $\mathrm z$ là $\mathrm u{:}2>1$, nên dừng ở $\mathrm z$.

**Câu (b).** Đường đi $\mathrm s\to\mathrm t\to\mathrm u\to\mathrm z$, 5 phép đo ($\mathrm s$; $\mathrm e$, $\mathrm t$; $\mathrm u$; $\mathrm z$), trả đỉnh gần $q$ nhất. Từ $\mathrm e$, tham lam dừng ở $\mathrm b{:}5$ sau 4 phép đo.

**Kiểm tra lại.** Cả hai lượt dừng ở một cực tiểu cục bộ, như Mệnh đề 07.11(b); với cùng thủ tục tham lam, cực tiểu được trả phụ thuộc điểm vào. Ví dụ 07.4 cho thấy tìm kiếm chùm từ $\mathrm e$ tới được $\mathrm z$.
:::

::: exercise Bài tập 07.5 (Bề rộng chùm và một nhánh xa)
Đồ thị bốn đỉnh có $\mathrm u{:}8$, $\mathrm v{:}6$, $\mathrm w{:}9$, $\mathrm z{:}2$ (số là khoảng cách tới $q$) và cạnh hai chiều $\mathrm u$–$\mathrm v$, $\mathrm u$–$\mathrm w$, $\mathrm w$–$\mathrm z$; điểm vào $\mathrm u$. Chạy Thuật toán 07.12 và ghi $V$, $W$ khi dừng trong ba trường hợp:

- (a) $ef=2$, lân cận của $\mathrm u$ duyệt theo thứ tự $\mathrm v,\mathrm w$;
- (b) $ef=2$, thứ tự $\mathrm w,\mathrm v$;
- (c) $ef=3$.
:::

::: hint
Với $ef=2$, khi $\mathrm w$ được xét, so nó với đỉnh xa nhất của $W$ lúc đó.
:::

::: solution
**Câu (a), $ef=2$, thứ tự $\mathrm v,\mathrm w$.** Mở $\mathrm u$: $\mathrm v{:}6$ vào vì $|W|=1<2$, $W=\{\mathrm v,\mathrm u\}$; $\mathrm w{:}9$ vào $V$ nhưng không vào $C$ vì $9>8=f$. Mở $\mathrm v$: không lân cận mới; $C$ rỗng. Kết quả $W=\{\mathrm v,\mathrm u\}$, $V=\{\mathrm u,\mathrm v,\mathrm w\}$.

**Câu (b), $ef=2$, thứ tự $\mathrm w,\mathrm v$.** $\mathrm w$ vào vì $|W|=1<2$; $\mathrm v{:}6$ vào vì $6<9=f$, rồi $\mathrm w$ bị bỏ khỏi $W$ nhưng còn trong $C$. Mở $\mathrm v$: không lân cận mới. Lấy $\mathrm w{:}9$: $f=\mathrm u{:}8\prec\mathrm w$, `break`. Kết quả vẫn là $W=\{\mathrm v,\mathrm u\}$, $V=\{\mathrm u,\mathrm v,\mathrm w\}$.

**Câu (c), $ef=3$.** Mở $\mathrm u$: cả $\mathrm v$ và $\mathrm w$ vào vì $W$ chưa đủ. Mở $\mathrm v$: không gì mới. Mở $\mathrm w$ ($9\le9=f$): $\mathrm z{:}2$ vào vì $2<9$, bỏ $\mathrm w$. Mở $\mathrm z$: không gì mới. Kết quả $W=\{\mathrm z,\mathrm v,\mathrm u\}$, $V=\{\mathrm u,\mathrm v,\mathrm w,\mathrm z\}$.

**Kiểm tra lại.** Với $ef=2$, $\mathrm z$ không thuộc $V$ ở cả hai thứ tự, nên kết quả đúng trên $V$ nhưng thiếu đỉnh gần nhất; với $ef=3$, $W$ là ba đỉnh nhỏ nhất của $V$ như Mệnh đề 07.13(b).
:::

Như vậy, tìm kiếm tham lam dừng ở một cực tiểu cục bộ (Mệnh đề 07.11), và `SEARCH-LAYER` mở rộng nó thành tìm kiếm chùm với bất biến "$W$ là $ef$ đỉnh tốt nhất đã thấy" (Mệnh đề 07.13, Hệ quả 07.14). Hai kết quả chỉ nói về các đỉnh đã thấy, và số đỉnh phải mở phụ thuộc khoảng cách từ điểm vào tới vùng gần $q$. Trong Mục 3, chúng ta thêm cạnh dài theo nhiều tầng để rút ngắn đường đi.

<!-- note-topic-id: lec-07-topic-03 -->
## 3. Đồ thị thế giới nhỏ phân tầng (HNSW)

Số phép đo của `SEARCH-LAYER` xấp xỉ số đỉnh được mở nhân bậc trung bình của chúng. Trên $N$ điểm của một đường thẳng chỉ nối các điểm liền kề, tham lam từ một đầu tới điểm ở đầu kia cần $N-1$ bước. Chúng ta cần biết đặt cạnh dài ở đâu để số bước không tăng theo $N$ như vậy.

### 3.1 Cạnh dài và đồ thị nhiều tầng

::: example Ví dụ 07.6 (Mười hai điểm trên một đường thẳng)
**Dữ kiện.** Điểm vào $s$ ở tọa độ 0, điểm $p_i$ ở tọa độ $i$ với $i=1,\ldots,11$, truy vấn $q$ ở tọa độ $6{,}4$; đỉnh gần $q$ nhất là $p_6$ ($0{,}4$). Mọi cạnh là hai chiều; tìm kiếm tham lam từ $s$.

**Chỉ cạnh ngắn** $s$–$p_1$, $p_1$–$p_2$, …, $p_{10}$–$p_{11}$. Đường đi $s\to p_1\to\cdots\to p_6$ gồm 6 bước; ở $p_6$, hai lân cận $p_5$ ($1{,}4$) và $p_7$ ($0{,}6$) đều xa hơn.

**Thêm ba cạnh dài** $s$–$p_4$, $p_4$–$p_8$, $p_8$–$p_{11}$. Từ $s$, lân cận $p_4$ ($2{,}4$) tốt hơn $p_1$ ($5{,}4$); từ $p_4$, lân cận $p_5$ ($1{,}4$) tốt hơn $p_8$ ($1{,}6$); từ $p_5$ sang $p_6$. Đường đi $s\to p_4\to p_5\to p_6$ gồm 3 bước.

**Chỉ thêm cạnh** $p_4$–$p_8$. Từ $s$ chỉ có $p_1$, nên đường đi vẫn là $s\to p_1\to\cdots\to p_6$, 6 bước.

**Kiểm tra lại.** Cả ba lượt dừng ở $p_6$. Cạnh dài chỉ rút ngắn đường đi khi nó xuất phát từ một đỉnh sớm trên đường đi và dẫn tới đỉnh gần $q$ hơn lân cận ngắn; cạnh $p_4$–$p_8$ chỉ được xét sau 4 bước, và $p_8$ ($1{,}6$) thua $p_5$ ($1{,}4$).
:::

![Mười hai điểm s, p1 đến p11 trên một đường thẳng, q nằm giữa p6 và p7 gần p6 hơn; chỉ có cạnh ngắn thì tham lam từ s cần 6 bước, thêm cạnh dài s–p4, p4–p8, p8–p11 thì cần 3 bước.](img/lec-07/canh-dai-mot-chieu.svg)

Trên hình, ba cạnh dài vẽ phía trên trục; hai cạnh nét đứt $p_4$–$p_8$ và $p_8$–$p_{11}$ không nằm trên đường tham lam $s\to p_4\to p_5\to p_6$. Một cách trực quan, cạnh dài đưa phép tìm tới gần $q$ trong ít bước, còn cạnh ngắn cho phép dừng đúng chỗ (bài giảng 9, tr.11–13). *Danh sách nhảy* (skip list) dùng cùng ý tưởng cho khóa một chiều: mỗi tầng trên giữ một phần các phần tử của tầng dưới, nên các liên kết ở tầng trên dài hơn. HNSW áp dụng ý tưởng đó cho đồ thị lân cận.

::: definition Định nghĩa 07.16 (Đồ thị thế giới nhỏ phân tầng)
Mỗi điểm $y\in Y$ có một *tầng tối đa* (maximum layer) $\ell(y)\in\{0,1,2,\ldots\}$. Với mỗi $\ell\ge0$, đặt $Y_\ell=\{y\in Y:\ell(y)\ge\ell\}$, nên

$$
\begin{aligned}
&Y=Y_0\supseteq Y_1\supseteq\cdots\supseteq Y_L,\\
&L=\max_{y\in Y}\ell(y).
\end{aligned}
$$

Một *đồ thị thế giới nhỏ phân tầng* (Hierarchical Navigable Small World, HNSW) gồm, cho mỗi tầng $\ell=0,\ldots,L$, một đồ thị lân cận $G_\ell$ trên $Y_\ell$ (Định nghĩa 07.8), và một điểm vào thuộc $Y_L$. Tầng 0 chứa mọi điểm; tầng càng cao chứa càng ít điểm.
:::

Mỗi tầng là một đồ thị lân cận của Định nghĩa 07.8, nên `SEARCH-LAYER` chạy được trên từng tầng với $\ell_c$ là chỉ số tầng. Một điểm có $\ell(y)=2$ xuất hiện ở tầng 0, 1 và 2, mỗi tầng với một danh sách lân cận riêng. Vì tầng trên thưa hơn, cạnh ở tầng trên là cạnh dài; trên đường thẳng của Ví dụ 07.6, nếu tầng 2 chỉ gồm $s,p_4,p_8$ thì cạnh $p_4$–$p_8$ dài 4 đơn vị, còn mọi cạnh ở tầng 0 dài 1.

::: example Ví dụ 07.7 (Ba tầng trên đường thẳng)
**Dữ kiện.** Mười hai điểm của Ví dụ 07.6 ($s$ ở 0, $p_i$ ở $i$, $q$ ở $6{,}4$). $Y_1=\{s,p_2,p_4,p_6,p_8,p_{10}\}$, $Y_2=\{s,p_4,p_8\}$; mỗi tầng nối các điểm liền kề của tầng đó; điểm vào $s$.

**Tầng 2.** Tham lam từ $s$: $s\to p_4\to p_8$ ($6{,}4$; $2{,}4$; $1{,}6$); lân cận duy nhất của $p_8$ ở tầng này là $p_4$, nên dừng ở $p_8$.

**Tầng 1.** Từ $p_8$, lân cận $p_6$ ($0{,}4$) tốt hơn $p_{10}$ ($3{,}6$); từ $p_6$, hai lân cận $p_4$, $p_8$ đều xa hơn, nên dừng ở $p_6$.

**Tầng 0.** `SEARCH-LAYER` từ $\{p_6\}$ với $ef=3$ trả $W=\{p_6,p_7,p_5\}$ ($0{,}4$; $0{,}6$; $1{,}4$).

**Kiểm tra lại.** Tổng số bước di chuyển là $2+1+0=3$, so với 6 bước khi chỉ có tầng 0; $W$ đúng là ba điểm gần $q$ nhất của kho.
:::

![Tầng 0 chứa mười hai điểm s, p1 đến p11; tầng 1 chứa s, p2, p4, p6, p8, p10; tầng 2 chứa s, p4, p8. Truy vấn ở tầng 2 đi s, p4, p8; xuống tầng 1 đi từ p8 sang p6; xuống tầng 0 tìm quanh p6.](img/lec-07/do-thi-nhieu-tang.svg)

Điểm dừng ở một tầng là điểm vào của tầng ngay dưới. Thuật toán sau viết lại quy trình đó theo Thuật toán 5 của bài báo HNSW (Malkov và Yashunin, tr.5).

::: algorithm Thuật toán 07.17 (Truy vấn HNSW)
**Đầu vào.** Chỉ mục HNSW với điểm vào $s$ ở tầng $L$; truy vấn $q$; số nguyên $K\ge1$ và $\mathit{efSearch}\ge K$.

**Đầu ra.** Tối đa $K$ đỉnh, là các đỉnh gần $q$ nhất trong các đỉnh đã thấy ở tầng 0.

**Giả thiết.** Như Thuật toán 07.12 ở mọi tầng.

1. Đặt $ep\leftarrow\{s\}$.
2. Với $\ell_c=L,L-1,\ldots,1$: $W\leftarrow$ `SEARCH-LAYER`$(q,ep,1,\ell_c)$; $ep\leftarrow W$.
3. $W\leftarrow$ `SEARCH-LAYER`$(q,ep,\mathit{efSearch},0)$.
4. Trả $K$ đỉnh đầu của $W$ theo $\prec$.

**Dừng.** $L$ lời gọi ở bước 2 và một lời gọi ở bước 3, mỗi lời gọi dừng theo Mệnh đề 07.13(a).

**Trường hợp biên.** Khi $L=0$, bước 2 rỗng. Khi phần tầng 0 đi tới được có ít hơn $K$ đỉnh, thuật toán trả ít hơn $K$ đỉnh.

**Chi phí.** Tổng chi phí của $L+1$ lời gọi `SEARCH-LAYER` (bảng chi phí của Thuật toán 07.12), cộng $O(\mathit{efSearch}\log \mathit{efSearch})$ cho bước 4.
:::

Ở tầng trên, $ef=1$ biến `SEARCH-LAYER` thành tìm kiếm tham lam (Hệ quả 07.14), và $W$ có đúng một đỉnh. Điều kiện $\mathit{efSearch}\ge K$ dành đủ chỗ trong $W$ cho $K$ kết quả. Hệ quả sau suy trực tiếp từ Mệnh đề 07.13.

::: corollary Hệ quả 07.18 (Tính đúng của truy vấn HNSW)
**Giả thiết.** Như Thuật toán 07.17.

**Kết luận.** Thuật toán 07.17 dừng và trả $\min(K,|V_0|)$ đỉnh nhỏ nhất theo $\prec$ của tập $V_0$ các đỉnh đã thấy ở lời gọi tầng 0.

**Điều kiện áp dụng.** Mọi chỉ mục HNSW hữu hạn.

**Phạm vi.** Như Mệnh đề 07.13, kết luận chỉ nói về $V_0$; đỉnh ngoài $V_0$ có thể là hàng xóm thật.
:::

::: proof Chứng minh Hệ quả 07.18
Mỗi lời gọi dừng theo Mệnh đề 07.13(a). Ở lời gọi tầng 0, $1\le|ep|=1\le \mathit{efSearch}$, nên Mệnh đề 07.13(b) cho $W$ là $\min(\mathit{efSearch},|V_0|)$ đỉnh nhỏ nhất của $V_0$; vì $K\le \mathit{efSearch}$, $K$ đỉnh đầu của $W$ là $\min(K,|V_0|)$ đỉnh nhỏ nhất của $V_0$. $\square$
:::

### 3.2 Phân phối tầng

Trong Ví dụ 07.7, $Y_1$ và $Y_2$ cho trước, và mỗi tầng giữ khoảng một nửa tầng dưới. Khi các điểm được chèn lần lượt mà không biết trước toàn bộ kho, HNSW rút tầng tối đa ngẫu nhiên cho từng điểm mới (Thuật toán 1 của bài báo, tr.4): lấy $U$ đều trên $(0,1]$ và đặt

$$
\ell=\big\lfloor-\ln(U)\,m_L\big\rfloor,\qquad m_L>0.
$$

Số $-\ln U$ không âm, và $\ell\ge1$ khi và chỉ khi $-\ln U\ge1/m_L$; hệ số $m_L$ vì thế quyết định tỷ lệ điểm lên tầng trên. Đặt $\rho=e^{-1/m_L}\in(0,1)$.

::: proposition Mệnh đề 07.19 (Phân phối tầng)
**Giả thiết.** $U$ phân phối đều trên $(0,1]$; $m_L>0$; $\ell=\lfloor-\ln(U)m_L\rfloor$; các điểm của kho rút $U$ độc lập.

**Kết luận.**

- (a) Với mọi số nguyên $k\ge0$, $\Pr[\ell\ge k]=\rho^k$.
- (b) Kỳ vọng số điểm của kho có $\ell\ge k$ là $N\rho^k$.
- (c) Kỳ vọng số tầng trên tầng 0 mà một điểm thuộc về là $\mathbb E[\ell]=\rho/(1-\rho)$.

**Điều kiện áp dụng.** Mọi $m_L>0$.

**Phạm vi.** Mệnh đề không nói về cạnh hay chi phí truy vấn.
:::

::: proof Chứng minh Mệnh đề 07.19
**Bước 1 (biến cố $\ell\ge k$).** Với $k$ nguyên, $\lfloor z\rfloor\ge k$ khi và chỉ khi $z\ge k$. Do đó

$$
\begin{aligned}
\ell\ge k&\iff-\ln(U)\,m_L\ge k\\
&\iff\ln U\le-\frac k{m_L}\\
&\iff U\le e^{-k/m_L},
\end{aligned}
$$

trong đó bước thứ hai chia cho $m_L>0$ và bước thứ ba dùng tính tăng của hàm mũ.

**Bước 2 (xác suất).** Vì $e^{-k/m_L}\in(0,1]$ và $U$ đều trên $(0,1]$, $\Pr[U\le e^{-k/m_L}]=e^{-k/m_L}=\rho^k$. Điều này chứng minh (a).

**Bước 3 (số điểm).** Số điểm có $\ell\ge k$ là tổng $N$ biến chỉ báo, mỗi biến có kỳ vọng $\rho^k$ theo (a); tuyến tính kỳ vọng cho $N\rho^k$.

**Bước 4 (số tầng trên).** Điểm thuộc các tầng $1,\ldots,\ell$, tức $\ell$ tầng trên tầng 0. Vì $\ell$ nguyên không âm,

$$
\begin{aligned}
\mathbb E[\ell]&=\sum_{k\ge1}\Pr[\ell\ge k]\\
&=\sum_{k\ge1}\rho^k=\frac{\rho}{1-\rho}
\end{aligned}
$$

theo (a) và công thức chuỗi hình học với $0<\rho<1$. $\square$
:::

Mệnh đề 07.19(a) nói mỗi tầng giữ, theo kỳ vọng, tỷ lệ $\rho$ số điểm của tầng ngay dưới, vì $\Pr[\ell\ge k+1\mid\ell\ge k]=\rho^{k+1}/\rho^k=\rho$; đây là phân phối hình học của danh sách nhảy. Theo (b), số điểm kỳ vọng ở tầng $k$ bằng 1 khi $k=\log_{1/\rho}N$, nên tầng cao nhất xấp xỉ $\log_{1/\rho}N$. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ điều kiện $k$ nguyên: $\Pr[\ell\ge0{,}5]=\Pr[\ell\ge1]=\rho$, khác $\rho^{0{,}5}$.
- Bỏ $U>0$: nếu $U$ được rút trên $[0,1)$, giá trị $U=0$ làm $-\ln U$ không xác định; khi đó dùng $1-U$, có phân phối đều trên $(0,1]$.
- Bỏ $m_L>0$: với $m_L=0$, mọi điểm có $\ell=0$ và chỉ mục chỉ còn một tầng.

Bước 1 dùng $k$ nguyên và $m_L>0$; Bước 2 dùng $U$ đều trên $(0,1]$.

::: example Ví dụ 07.8 (Tầng của mười tỷ điểm với $m_L=1/\ln16$)
**Dữ kiện.** $N=10^{10}$, $m_L=1/\ln16$, nên $\rho=e^{-\ln16}=1/16=0{,}0625$.

**Tính.** Theo Mệnh đề 07.19(a), (b):

| $k$ | $\Pr[\ell\ge k]=\rho^k$ | $N\rho^k$ |
|---|---|---|
| 0 | 1 | $10^{10}$ |
| 1 | $0{,}0625$ | $6{,}25\cdot10^8$ |
| 2 | $3{,}9\cdot10^{-3}$ | $3{,}9\cdot10^7$ |
| 3 | $2{,}4\cdot10^{-4}$ | $2{,}4\cdot10^6$ |
| 8 | $2{,}3\cdot10^{-10}$ | $2{,}3$ |
| 9 | $1{,}5\cdot10^{-11}$ | $0{,}15$ |

**Diễn giải.** Tầng cao nhất xấp xỉ $\log_{16}10^{10}\approx8{,}3$. Theo (c), một điểm trung bình thuộc $\rho/(1-\rho)=1/15\approx0{,}067$ tầng trên tầng 0.

**Kiểm tra lại.** $16^8\approx4{,}3\cdot10^9<10^{10}<16^9$, khớp với cột cuối đổi từ trên 1 xuống dưới 1 giữa $k=8$ và $k=9$.
:::

Bài báo HNSW (§4.1, tr.5) chọn $m_L=1/\ln M$, với $M$ là số lân cận nối cho mỗi điểm mới (Thuật toán 07.20); lựa chọn này ứng với xác suất $p=1/M$ của danh sách nhảy, tức $\rho=1/M$, và Ví dụ 07.8 ứng với $M=16$. Thuật toán đúng với mọi $m_L>0$, vì Hệ quả 07.18 không dùng phân phối tầng.

### 3.3 Chèn một điểm

Chèn điểm mới $x$ là một truy vấn với chính $x$: phép tìm từ tầng cao nhất xuống cho biết những đỉnh nào đã gần $x$, và $x$ được nối với một số đỉnh đó ở mỗi tầng mà $x$ thuộc về. Để làm rõ các pha, xem ví dụ sau.

::: example Ví dụ 07.9 (Chèn $x=2{,}6$ vào đồ thị ba tầng)
**Dữ kiện.** Chỉ mục ba tầng của Ví dụ 07.7: tầng 0 nối các điểm liền kề của $s,p_1,\ldots,p_{11}$ ($s$ ở 0, $p_i$ ở $i$); tầng 1 nối các điểm liền kề của $s,p_2,p_4,p_6,p_8,p_{10}$; tầng 2 nối $s$–$p_4$, $p_4$–$p_8$; điểm vào $s$. Điểm mới $x$ ở tọa độ $2{,}6$ rút được $\ell=1$. Tham số: $M=2$, $\mathit{efConstruction}=3$, $M_{\max}=3$, $M_{\max,0}=4$. Khoảng cách tới $x$: $p_3$ $0{,}4$; $p_2$ $0{,}6$; $p_4$ $1{,}4$; $p_1$ $1{,}6$; $s$ $2{,}6$.

**Pha 1, tầng 2 (trên $\ell$).** Tham lam từ $s$ ($2{,}6$) sang $p_4$ ($1{,}4$); $p_8$ ($5{,}4$) xa hơn, dừng. $ep=\{p_4\}$; $x$ không thuộc tầng 2 nên không nối cạnh.

**Pha 2, tầng 1.** `SEARCH-LAYER`$(x,\{p_4\},3,1)$ trả $W=\{p_2{:}0{,}6,\ p_4{:}1{,}4,\ s{:}2{,}6\}$. Hai đỉnh gần nhất là $p_2$, $p_4$; nối $x$–$p_2$ và $x$–$p_4$ theo hai chiều.

**Pha 2, tầng 0.** `SEARCH-LAYER`$(x,\{p_2,p_4,s\},3,0)$ trả $W=\{p_3{:}0{,}4,\ p_2{:}0{,}6,\ p_4{:}1{,}4\}$. Nối $x$–$p_3$ và $x$–$p_2$.

**Kiểm tra lại.** Sau khi nối, $p_2$ và $p_4$ ở tầng 1 có bậc 3, $p_3$ và $p_2$ ở tầng 0 có bậc 3; không đỉnh nào vượt $M_{\max}=3$ hay $M_{\max,0}=4$, nên không có bước cắt.
:::

![Điểm mới x ở tọa độ 2,6 có tầng 1, M bằng 2; pha 1 ở tầng 2 đi từ s tới p4; pha 2 nối x với p2 và p4 ở tầng 1, với p3 và p2 ở tầng 0.](img/lec-07/chen-vi-du.svg)

Trên hình, $x$ có cạnh mới ở tầng 1 và tầng 0, còn ở tầng 2 chỉ có đường đi $s\to p_4$ của pha 1. Ở pha 2, tập $W$ của tầng trên làm tập điểm vào của tầng dưới; đó là lý do $ep$ của `SEARCH-LAYER` là một tập và giả thiết $|ep|\le ef$ cần $\mathit{efConstruction}\ge$ số phần tử của $W$ tầng trên. Thuật toán sau theo Thuật toán 1 của bài báo HNSW (tr.4), với bước chọn lân cận là chọn $M$ đỉnh gần nhất (Thuật toán 3 của bài báo, tr.5).

::: algorithm Thuật toán 07.20 (Chèn một điểm vào HNSW)
**Đầu vào.** Chỉ mục HNSW (có thể rỗng) với điểm vào $s$ ở tầng $L$; điểm mới $x$; tham số $M\ge1$, $\mathit{efConstruction}\ge M$, $M_{\max}\ge M$, $M_{\max,0}\ge M$, $m_L>0$.

**Đầu ra.** Chỉ mục có thêm $x$ ở các tầng $0,\ldots,\ell$.

**Giả thiết.** Như Thuật toán 07.12 ở mọi tầng; bậc tối đa ở tầng $\ell_c$ là $M_{\max,0}$ khi $\ell_c=0$ và $M_{\max}$ khi $\ell_c>0$.

1. Rút $\ell=\lfloor-\ln(U)m_L\rfloor$ (Mệnh đề 07.19).
2. Nếu chỉ mục rỗng: tạo $x$ ở các tầng $0,\ldots,\ell$ không có cạnh, đặt $x$ làm điểm vào với $L=\ell$, và dừng.
3. (Pha 1) $ep\leftarrow\{s\}$. Với $\ell_c=L,\ldots,\ell+1$: $ep\leftarrow$ `SEARCH-LAYER`$(x,ep,1,\ell_c)$.
4. (Pha 2) Với $\ell_c=\min(L,\ell),\ldots,0$: $W\leftarrow$ `SEARCH-LAYER`$(x,ep,\mathit{efConstruction},\ell_c)$; $\mathcal R\leftarrow M$ đỉnh gần $x$ nhất của $W$; thêm cạnh $(x,u)$ và $(u,x)$ ở tầng $\ell_c$ cho mọi $u\in\mathcal R$; với mỗi $u\in\mathcal R$ có bậc vượt bậc tối đa của tầng, chỉ giữ các lân cận gần $u$ nhất đủ bậc tối đa; $ep\leftarrow W$.
5. Nếu $\ell>L$: tạo $x$ ở các tầng $L+1,\ldots,\ell$, đặt $x$ làm điểm vào và $L\leftarrow\ell$.

**Dừng.** Hữu hạn lời gọi `SEARCH-LAYER`, mỗi lời gọi dừng theo Mệnh đề 07.13(a).

**Trường hợp biên.** Chỉ mục rỗng ở bước 2. Khi $\ell\ge L$, pha 1 rỗng. Khi $W$ có ít hơn $M$ đỉnh, $\mathcal R=W$.

**Chi phí.** Mỗi lời gọi `SEARCH-LAYER` tốn như bảng của Thuật toán 07.12.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 3: `SEARCH-LAYER` với $ef=1$ | $\max(0,L-\ell)$ | một lời gọi | $\max(0,L-\ell)$ lời gọi |
| 4: `SEARCH-LAYER` với $\mathit{efConstruction}$ | $\min(L,\ell)+1$, kỳ vọng nhiều nhất $1+\rho/(1-\rho)$ (Mệnh đề 07.19(c)) | một lời gọi | cùng số lời gọi |
| 4: chọn $\mathcal R$ | $\min(L,\ell)+1$ | $O(|W|\log|W|)$ | $O\big((\min(L,\ell)+1)\,|W|\log|W|\big)$ |
| 4: cắt bậc | nhiều nhất $M$ đỉnh mỗi tầng | $O(M_{\max,0}D+M_{\max,0}\log M_{\max,0})$ | $O\big(M(M_{\max,0}D+M_{\max,0}\log M_{\max,0})\big)$ mỗi tầng |
:::

Thuật toán 07.20 giữ ba tính chất của chỉ mục: $x$ thuộc mọi tầng $0,\ldots,\ell$; bước cắt giữ mọi bậc không vượt bậc tối đa của tầng, vì chỉ các đỉnh vừa nhận cạnh mới có thể vượt; bước 5 giữ điểm vào thuộc $Y_L$ như Định nghĩa 07.16.

Pha 1 chạy ở các tầng cao hơn $\ell$, nơi $x$ không xuất hiện, nên chỉ đi tìm điểm vào cho tầng $\ell$. Bước cắt bậc làm quan hệ kề có thể không đối xứng: mỗi đỉnh $u$ tự cắt danh sách của mình, nên $x$ có thể giữ cạnh $(x,u)$ trong khi $u$ đã bỏ $(u,x)$. Đó là lý do Định nghĩa 07.8 dùng đồ thị có hướng.

### 3.4 Chi phí và tham số

Ví dụ 07.7 cần 3 bước thay cho 6. Mệnh đề sau, theo lập luận của bài báo HNSW (§4.2.1, tr.7), cho số phép đo tăng theo $\log N$ dưới ba giả thiết; xác suất một điểm lên tầng trên là $\rho$ của Mệnh đề 07.19.

Giả thiết (ii) dùng hai khái niệm hình học. Với tập hữu hạn $Z\subset\mathbb R^D$, *ô Voronoi* (Voronoi cell) của $z\in Z$ là tập các điểm của $\mathbb R^D$ không xa $z$ hơn mọi điểm khác của $Z$; *đồ thị Delaunay* (Delaunay graph) của $Z$ nối hai điểm khi ô Voronoi của chúng có chung biên. Bài báo (§4.2.1, tr.7) dùng tính chất: trên đồ thị Delaunay, tìm kiếm tham lam luôn tới điểm gần $q$ nhất.

::: proposition Mệnh đề 07.21 (Số phép đo của truy vấn HNSW)
**Giả thiết.**

- (i) Tầng của các điểm rút theo Mệnh đề 07.19, độc lập với nhau và với vị trí của điểm.
- (ii) Mỗi đồ thị $G_\ell$ là đồ thị Delaunay của $Y_\ell$, nên tham lam trên $G_\ell$ luôn tới điểm của $Y_\ell$ gần $q$ nhất.
- (iii) Bậc trung bình của các đỉnh trên đường đi bị chặn bởi một hằng số $C_{\deg}$ không phụ thuộc $N$.

**Kết luận.**

- (a) Kỳ vọng của tầng cao nhất thỏa $\mathbb E[L]\le\lceil\log_{1/\rho}N\rceil+\rho/(1-\rho)$.
- (b) Kỳ vọng số bước tham lam ở mỗi tầng $\ell<L$ nhiều nhất $1/\rho$.
- (c) Kỳ vọng số phép đo của một truy vấn là $O\big(C_{\deg}\,\rho^{-1}\log_{1/\rho}N\big)$, tức $O(\log N)$ khi $\rho$ và $C_{\deg}$ cố định.

**Điều kiện áp dụng.** Theo bài báo (tr.7), giả thiết (iii) đúng với dữ liệu Euclid ngẫu nhiên khi kho rất lớn và có thể sai trong các không gian khác; $C_{\deg}$ phụ thuộc số chiều, vì bậc trung bình của đồ thị Delaunay tăng theo hàm mũ của số chiều.

**Phạm vi.** Đồ thị do Thuật toán 07.20 dựng chỉ xấp xỉ đồ thị Delaunay; với đồ thị thật, kết luận là mô hình giải thích, không là cận cho mọi dữ liệu.
:::

::: proof Phác thảo chứng minh Mệnh đề 07.21
**Bước 1 (chứng minh (a)).** Theo chặn hợp và Mệnh đề 07.19(a), $\Pr[L\ge k]\le N\rho^k$. Đặt $k_0=\lceil\log_{1/\rho}N\rceil$, nên $N\rho^{k_0}\le1$. Khi đó

$$
\begin{aligned}
\mathbb E[L]&=\sum_{k\ge1}\Pr[L\ge k]\\
&\le k_0+\sum_{j\ge1}N\rho^{k_0+j}\\
&\le k_0+\sum_{j\ge1}\rho^j\\
&=k_0+\frac{\rho}{1-\rho}.
\end{aligned}
$$

**Bước 2 (ý của (b)).** Xét tầng $\ell<L$. Theo (ii) cho tầng $\ell+1$, điểm vào $u$ của tầng $\ell$ là điểm của $Y_{\ell+1}$ gần $q$ nhất. Mỗi đỉnh sau $u$ trên đường đi tham lam ở tầng $\ell$ gần $q$ hơn đỉnh trước nó, nên gần $q$ hơn $u$ và không thuộc $Y_{\ell+1}$. Gọi $G$ là số điểm của $Y_\ell$ gần $q$ hơn điểm gần nhất của $Y_{\ell+1}$; số bước ở tầng $\ell$ không vượt $G$. Có điều kiện theo $Y_\ell$, mỗi điểm của $Y_\ell$ thuộc $Y_{\ell+1}$ độc lập với xác suất $\rho$ (giả thiết (i)), và $G\ge t$ khi và chỉ khi $t$ điểm của $Y_\ell$ gần $q$ nhất đều không thuộc $Y_{\ell+1}$. Do đó $\Pr[G\ge t]\le(1-\rho)^t$ và $\mathbb E[G]\le\sum_{t\ge1}(1-\rho)^t=(1-\rho)/\rho\le1/\rho$. Tầng $L$, nơi điểm vào $s$ tùy ý, không thuộc lập luận này.

**Bước 3 (ý của (c)).** Mỗi bước đo các lân cận của một đỉnh, theo (iii) trung bình nhiều nhất $C_{\deg}$ phép đo; nhân với (b) và với số tầng ở (a). Chứng minh đầy đủ, xử lý sự phụ thuộc giữa đường đi và tập điểm của từng tầng, nằm ngoài phạm vi học phần (Malkov và Yashunin, §4.2.1, tr.7). $\square$
:::

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ (i): nếu các tầng trên chỉ chứa các điểm bên trái, chẳng hạn $Y_1=\{s,p_1,p_2,p_3\}$ trên đường thẳng của Ví dụ 07.6, tầng 1 đi $s\to p_1\to p_2\to p_3$ (3 bước) rồi tầng 0 còn 3 bước tới $p_6$, tổng 6 bước như khi chỉ có một tầng.
- Bỏ (ii): trên đồ thị bảy đỉnh, tham lam dừng ở $\mathrm b{:}5$ thay cho $\mathrm z{:}1$ (Ví dụ 07.3), nên điểm vào của tầng dưới không còn là điểm gần nhất của tầng trên và Bước 2 không áp dụng.
- Bỏ (iii): trong mặt phẳng, một điểm ở tâm và $N-1$ điểm trên đường tròn quanh nó cho đồ thị Delaunay có đỉnh tâm bậc $N-1$; mở đỉnh này tốn $N-1$ phép đo. Với $D=128$, điều kiện (iii) chỉ đạt được trên kho cực lớn (bài báo, tr.7).

Bước 1 dùng phân phối tầng; Bước 2 dùng (i) và (ii); Bước 3 dùng (iii).

Bộ nhớ của HNSW gồm véc-tơ gốc và danh sách lân cận ở mỗi tầng mà điểm thuộc về. Mệnh đề sau tính kỳ vọng của phần thứ hai bằng Mệnh đề 07.19(c).

::: proposition Mệnh đề 07.22 (Bộ nhớ kỳ vọng của HNSW)
**Giả thiết.** Mỗi điểm lưu véc-tơ $D$ số thực 4 byte; ở tầng 0 mỗi điểm có nhiều nhất $M_{\max,0}$ lân cận, ở mỗi tầng trên nhiều nhất $M_{\max}$; mỗi liên kết là một mã định danh $s_{id}$ byte; tầng rút theo Mệnh đề 07.19.

**Kết luận.** Kỳ vọng số liên kết của một điểm nhiều nhất $B=M_{\max,0}+M_{\max}\,\rho/(1-\rho)$, và kỳ vọng bộ nhớ của chỉ mục nhiều nhất

$$
N\,(4D+s_{id}B)\ \text{byte}.
$$

**Điều kiện áp dụng.** $s_{id}=4$ khi $N\le2^{32}$; $s_{id}=8$ khi $N>2^{32}$.

**Phạm vi.** Không tính cấu trúc phụ (đánh dấu $V$, hàng đợi) và chi phí cấp phát bộ nhớ.
:::

::: proof Chứng minh Mệnh đề 07.22
Một điểm có tầng tối đa $\ell$ có nhiều nhất $M_{\max,0}+\ell M_{\max}$ liên kết [do giả thiết về bậc]. Lấy kỳ vọng và dùng $\mathbb E[\ell]=\rho/(1-\rho)$ (Mệnh đề 07.19(c)). Nhân với $s_{id}$, cộng $4D$ byte của véc-tơ, rồi cộng trên $N$ điểm theo tuyến tính kỳ vọng. $\square$
:::

Bước cắt bậc của Thuật toán 07.20 bảo đảm giả thiết về bậc. Bỏ bước này, một đỉnh có thể có nhiều hơn $M_{\max,0}$ liên kết: với điểm đầu tiên là gốc tọa độ, các điểm sau là các véc-tơ đơn vị $\mathbf u_1,\mathbf u_2,\ldots$ của $\mathbb R^D$ và $M=1$, mỗi $\mathbf u_i$ có gốc là điểm gần nhất (khoảng cách $1<\sqrt2$), nên gốc nhận một liên kết từ mỗi lần chèn.

::: example Ví dụ 07.10 (Bộ nhớ HNSW cho kho mười tỷ véc-tơ)
**Dữ kiện.** $N=10^{10}$, $D=3072$, $M=16$, $M_{\max,0}=32$, $M_{\max}=16$, $\rho=1/16$.

**Mã định danh.** $10^{10}>2^{32}\approx4{,}29\cdot10^9$, nên $s_{id}=8$.

**Tính.** Liên kết kỳ vọng mỗi điểm: $32+16\cdot\frac{1/16}{15/16}=32+\frac{16}{15}\approx33{,}07$, tức $\approx264{,}5$ byte. Véc-tơ: $4\cdot3072=12\,288$ byte. Mỗi điểm $\approx12\,552{,}5$ byte; toàn kho $\approx125{,}5$ TB, trong đó cạnh $\approx2{,}65$ TB.

**Kiểm tra lại.** Véc-tơ gốc chiếm $12\,288/12\,552{,}5\approx97{,}9\%$ bộ nhớ; bỏ hẳn cạnh, kho vẫn cần $122{,}88$ TB.
:::

::: remark Nhận xét 07.23 (Trong thực hành: ba tham số của HNSW)
| Tham số | Dùng khi | Tăng tham số thì |
|---|---|---|
| $M$ | chèn | thêm liên kết và bộ nhớ, mỗi lần mở đo nhiều lân cận hơn |
| $\mathit{efConstruction}$ | chèn | xây chậm hơn, lân cận chọn từ nhiều ứng viên hơn |
| $\mathit{efSearch}$ | truy vấn | mở nhiều đỉnh hơn ở tầng 0, độ trễ tăng |

$M$ và $\mathit{efConstruction}$ quyết định đồ thị khi xây, nên đổi chúng phải xây lại chỉ mục; $\mathit{efSearch}$ đổi được cho từng truy vấn, miễn $\mathit{efSearch}\ge K$. Bài báo (§4.2.3, tr.8) ghi rằng $M$ gần tối ưu thường nằm trong khoảng 6–48 và dùng mã định danh 4 byte khi kho dưới khoảng bốn tỷ điểm; với $M_{\max}=M$, $M_{\max,0}=2M$ và $\rho=1/M$, Mệnh đề 07.22 cho phần cạnh khoảng 53–388 byte mỗi điểm.
:::

::: exercise Bài tập 07.6 (Kho một trăm triệu véc-tơ trong 64 GB)
Kho có $N=10^8$ véc-tơ $D=128$ chiều, mỗi tọa độ 4 byte. HNSW dùng $m_L=1/\ln M$, $M_{\max}=M$, $M_{\max,0}=2M$.

- (a) Xác định số byte $s_{id}$ đủ cho mã định danh.
- (b) Với $M=16$, tính kỳ vọng bộ nhớ theo Mệnh đề 07.22 và so với 64 GB.
- (c) Với $M=12$, tính lại và so với 64 GB.
:::

::: hint
Khi $m_L=1/\ln M$ thì $\rho=1/M$.
:::

::: solution
**Câu (a).** $10^8<2^{32}\approx4{,}29\cdot10^9$, nên $s_{id}=4$.

**Câu (b).** $\rho=1/16$; liên kết kỳ vọng $32+16/15\approx33{,}07$, tức $\approx132{,}3$ byte. Mỗi điểm $512+132{,}3=644{,}3$ byte; toàn kho $\approx64{,}4$ GB, vượt 64 GB khoảng $0{,}4$ GB. Riêng véc-tơ gốc chiếm $51{,}2$ GB.

**Câu (c).** $\rho=1/12$; liên kết kỳ vọng $24+12\cdot\frac{1/12}{11/12}=24+12/11\approx25{,}09$, tức $\approx100{,}4$ byte. Mỗi điểm $\approx612{,}4$ byte; toàn kho $\approx61{,}2$ GB, vừa 64 GB.

**Kiểm tra lại.** Giảm $M$ chỉ đổi phần cạnh; véc-tơ gốc $51{,}2$ GB giữ nguyên, nên không giá trị $M$ nào đưa kho xuống dưới $51{,}2$ GB.
:::

::: exercise Bài tập 07.7 (Phân phối tầng với $m_L=1/\ln4$)
Kho có $N=10^6$ điểm, tầng rút theo Mệnh đề 07.19 với $m_L=1/\ln4$.

- (a) Tính $\rho$.
- (b) Tính kỳ vọng số điểm có $\ell\ge1$, $\ell\ge2$ và $\ell\ge5$.
- (c) Tìm số nguyên $k$ nhỏ nhất để kỳ vọng số điểm có $\ell\ge k$ nhỏ hơn 1, và so với $\log_4N$.
- (d) Tính kỳ vọng số tầng trên tầng 0 của một điểm.
:::

::: hint
$\rho=e^{-1/m_L}=e^{-\ln4}$.
:::

::: solution
**Câu (a).** $\rho=1/4$.

**Câu (b).** $N\rho=2{,}5\cdot10^5$; $N\rho^2=6{,}25\cdot10^4$; $N\rho^5=10^6/1024\approx976{,}6$.

**Câu (c).** $N\rho^9=10^6/262\,144\approx3{,}8$ và $N\rho^{10}\approx0{,}95$, nên $k=10$; $\log_410^6\approx9{,}97$.

**Câu (d).** $\rho/(1-\rho)=(1/4)/(3/4)=1/3$.

**Kiểm tra lại.** Mỗi dòng của (b) bằng dòng trước nhân $1/4$ cho mỗi tầng; (c) khớp nhận xét "tầng cao nhất xấp xỉ $\log_{1/\rho}N$" sau Mệnh đề 07.19.
:::

Như vậy, HNSW xếp các đồ thị lân cận thành tầng (Định nghĩa 07.16), truy vấn bằng `SEARCH-LAYER` từ trên xuống (Thuật toán 07.17, Hệ quả 07.18), rút tầng theo phân phối hình học (Mệnh đề 07.19) và chèn điểm bằng chính phép tìm đó (Thuật toán 07.20). Dưới ba giả thiết của Mệnh đề 07.21, số phép đo tăng theo $\log N$. Tuy nhiên, HNSW không giảm bộ nhớ của véc-tơ gốc và chi phí một phép đo. Trong Mục 4, chúng ta nén mỗi véc-tơ thành một mã ngắn để giảm cả bộ nhớ lẫn chi phí một phép đo.

<!-- note-topic-id: lec-07-topic-04 -->
## 4. Lượng tử hóa tích (PQ)

Với kho mở đầu, HNSW cần khoảng $125{,}5$ TB, trong đó véc-tơ gốc chiếm $97{,}9\%$ (Ví dụ 07.10), và mỗi phép đo xử lý $D=3072$ tọa độ. Thay mỗi véc-tơ bằng một mã ngắn thì mất một phần thông tin; chúng ta cần biết mã ngắn tới đâu thì còn tính được, và khoảng cách tính từ mã sai lệch bao nhiêu.

### 4.1 Lượng tử hóa véc-tơ

Cách nén đơn giản nhất chọn trước một tập nhỏ các véc-tơ đại diện và thay mỗi véc-tơ bằng số thứ tự của đại diện gần nó nhất. Để làm rõ, xem ví dụ sau.

::: example Ví dụ 07.11 (Ba tâm trong mặt phẳng)
**Dữ kiện.** Ba đại diện $c_0=(0;\ 0)$, $c_1=(2;\ 0)$, $c_2=(0;\ 2)$ và điểm $x=(1{,}7;\ 0{,}4)$.

**Tính.** $\|x-c_0\|^2=2{,}89+0{,}16=3{,}05$; $\|x-c_1\|^2=0{,}09+0{,}16=0{,}25$; $\|x-c_2\|^2=2{,}89+2{,}56=5{,}45$. Đại diện gần nhất là $c_1$.

**Kết quả.** Mã của $x$ là 1, dài $\lceil\log_23\rceil=2$ bit; véc-tơ tái dựng là $c_1=(2;\ 0)$ với sai số bình phương $0{,}25$.

**Kiểm tra lại.** Ranh giới giữa ô của $c_0$ và $c_1$ là đường $x_1=1$; $x$ có tọa độ thứ nhất $1{,}7>1$ và gần $c_1$ hơn $c_2$ vì $x_1>x_2$.
:::

![Ba tâm c0 tại (0; 0), c1 tại (2; 0), c2 tại (0; 2) chia mặt phẳng thành ba ô ngăn bởi các đường x1 bằng 1, x2 bằng 1 và x1 bằng x2; điểm x tại (1,7; 0,4) nằm trong ô của c1.](img/lec-07/luong-tu-hoa-vec-to.svg)

Mặt phẳng trên hình được chia thành ba ô, mỗi ô gồm các điểm có cùng đại diện gần nhất. Sai số tái dựng của một điểm là bình phương khoảng cách tới đại diện của ô chứa nó.

::: definition Định nghĩa 07.24 (Lượng tử hóa véc-tơ; Jégou và cộng sự, §II-A, tr.2)
Một *lượng tử hóa véc-tơ* (vector quantizer, VQ) gồm một *bộ mã* (codebook) $\mathcal C=\{c_0,\ldots,c_{k-1}\}\subset\mathbb R^D$ với $k$ *tâm* (centroid). Với $x\in\mathbb R^D$:

- *mã* của $x$ là $i(x)=\min\big\{i:\ \|x-c_i\|^2=\min_{0\le j<k}\|x-c_j\|^2\big\}$, dài $\lceil\log_2k\rceil$ bit;
- *véc-tơ tái dựng* (reconstruction) là $\widehat x=c_{i(x)}$, và *sai số tái dựng* là $\|x-\widehat x\|^2$;
- *ô* (cell) của tâm $c_i$ là $\{x\in\mathbb R^D: i(x)=i\}$;
- trên một tập hữu hạn $X$, *sai số bình phương trung bình* (mean squared error, MSE) là $\frac1{|X|}\sum_{x\in X}\|x-\widehat x\|^2$.
:::

Mã chọn tâm gần nhất, và khi hòa thì chọn chỉ số nhỏ, nên mỗi $x$ có đúng một mã; Ví dụ 07.11 là trường hợp $k=3$, $D=2$, $i(x)=1$. Ô của $c_i$ là ô Voronoi của $c_i$ trong $\mathcal C$, với hòa được gán cho chỉ số nhỏ; các ô phân hoạch $\mathbb R^D$, nên trên một tập điểm hữu hạn, lượng tử hóa véc-tơ là một phép phân cụm với các tâm làm đại diện (bài giảng 8, tr.8–9). Sai số tái dựng đo mức mất thông tin của một véc-tơ, không đo chất lượng truy vấn: một bộ mã có MSE nhỏ vẫn có thể xếp sai thứ tự hai véc-tơ gần $q$, và chất lượng truy vấn vẫn đo bằng độ thu hồi của Định nghĩa 07.4.

::: algorithm Thuật toán 07.25 (Mã hóa bằng lượng tử hóa véc-tơ)
**Đầu vào.** Véc-tơ $x\in\mathbb R^D$; bộ mã $\mathcal C$ gồm $k$ tâm.

**Đầu ra.** Mã $i(x)$ của Định nghĩa 07.24.

1. Với $i=0,\ldots,k-1$: tính $\|x-c_i\|^2$.
2. Trả chỉ số nhỏ nhất đạt giá trị nhỏ nhất.

**Dừng.** Sau $k$ lượt.

**Trường hợp biên.** Với $k=1$, mọi véc-tơ có mã 0 và mã dài 0 bit.

**Chi phí.** $k$ khoảng cách, mỗi khoảng cách $\Theta(D)$, tổng $\Theta(kD)$; bộ mã chiếm $kD$ số thực. Giải mã chỉ đọc $c_{i(x)}$, $\Theta(D)$.
:::

Thuật toán 07.25 là Thuật toán 07.2 với $K=1$, kho là bộ mã và truy vấn là $x$, nên tính đúng theo Mệnh đề 07.3. Chi phí mã hóa và bộ nhớ của bộ mã cùng tỷ lệ với $k$.

::: remark Nhận xét 07.26 (Học bộ mã bằng k-means)
Bộ mã được học trên một tập huấn luyện $X$ để MSE nhỏ. Hai *điều kiện tối ưu Lloyd* (Lloyd's optimality conditions) là điều kiện cần cho một bộ mã có MSE nhỏ nhất trên $X$ (bài giảng 8, tr.10; Jégou, §II-A, tr.2): mỗi véc-tơ được gán cho tâm gần nhất, và mỗi tâm là trọng tâm của các véc-tơ được gán cho nó. Vi phạm điều kiện nào thì sửa điều kiện đó làm giảm MSE. Thuật toán *k-means* (thuật toán Lloyd) lặp xen kẽ hai bước đó. Hai điều kiện là cần nhưng không đủ, nên k-means chỉ cho một cực tiểu cục bộ của MSE.
:::

Mã dài hơn đòi số tâm tăng theo lũy thừa của 2, như ví dụ sau.

::: example Ví dụ 07.12 (Một bộ mã cho mã 64 bit)
**Dữ kiện.** Véc-tơ SIFT $D=128$ chiều, mã 64 bit, tức $0{,}5$ bit mỗi tọa độ (Jégou, §II-B, tr.3).

**Tính.** Một bộ mã duy nhất cần $k=2^{64}\approx1{,}8\cdot10^{19}$ tâm. Lưu bộ mã cần $kD\cdot4\approx9{,}4\cdot10^{21}$ byte; mã hóa một véc-tơ theo Thuật toán 07.25 cần $kD\approx2{,}4\cdot10^{21}$ phép toán.

**Kiểm tra lại.** Bộ mã này lớn hơn kho mở đầu ($1{,}2288\cdot10^{14}$ byte) khoảng $7{,}7\cdot10^7$ lần.
:::

### 4.2 Lượng tử hóa tích

Một cách trực quan, nếu cắt véc-tơ thành vài đoạn và lượng tử hóa mỗi đoạn bằng một bộ mã nhỏ riêng, thì mã của cả véc-tơ là bộ các mã đoạn, và số véc-tơ tái dựng khác nhau là tích các số tâm. Hình dưới minh họa với $D=8$, bốn đoạn hai chiều và 256 tâm mỗi đoạn: mỗi đoạn cho một chỉ số 8 bit, cả véc-tơ cho mã 32 bit.

![Véc-tơ tám chiều chia thành bốn đoạn hai chiều; mỗi đoạn được mã hóa bằng bộ mã con 256 tâm thành một chỉ số 8 bit; mã PQ là bộ bốn chỉ số, dài 32 bit.](img/lec-07/pq-tach-doan.svg)

::: definition Định nghĩa 07.27 (Lượng tử hóa tích)
Cho số nguyên $m\mid D$ và phân hoạch $\{1,\ldots,D\}$ thành $m$ tập liên tiếp $G_1,\ldots,G_m$, mỗi tập $D/m$ tọa độ. *Đoạn* $j$ của $x\in\mathbb R^D$ là $x^{(j)}=(x_t)_{t\in G_j}\in\mathbb R^{D/m}$. Một *lượng tử hóa tích* (product quantizer, PQ) gồm $m$ *bộ mã con* (sub-quantizer codebook) $\mathcal C^{(j)}=\{c^{(j)}_0,\ldots,c^{(j)}_{k^*-1}\}\subset\mathbb R^{D/m}$, mỗi bộ $k^*$ tâm.

- Mã của $x$ là $(i_1(x),\ldots,i_m(x))$, với $i_j(x)$ là mã của $x^{(j)}$ theo lượng tử hóa véc-tơ với bộ mã $\mathcal C^{(j)}$ (Định nghĩa 07.24).
- Véc-tơ tái dựng là $\widehat x=\big(c^{(1)}_{i_1(x)}\mid\cdots\mid c^{(m)}_{i_m(x)}\big)$, ghép các tâm con theo thứ tự đoạn.
:::

Lượng tử hóa tích là $m$ lượng tử hóa véc-tơ chạy độc lập trên $m$ đoạn; với $m=1$ nó là lượng tử hóa véc-tơ trên cả véc-tơ (bài giảng 8, tr.33). Mỗi bộ mã con được học bằng k-means trên đoạn tương ứng của tập huấn luyện (Jégou, §II-B, tr.3). Tập các véc-tơ tái dựng là tích Descartes $\mathcal C^{(1)}\times\cdots\times\mathcal C^{(m)}$, từ đó có tên gọi.

::: example Ví dụ 07.13 (Mã hóa PQ với hai đoạn)
**Dữ kiện.** $D=4$, $m=2$, $k^*=2$. Bộ mã con đoạn 1: $c^{(1)}_0=(0;\ 2)$, $c^{(1)}_1=(2;\ 0)$; bộ mã con đoạn 2: $c^{(2)}_0=(0;\ 0)$, $c^{(2)}_1=(3;\ 0)$. Véc-tơ $x=(0{,}2;\ 1{,}8\mid2{,}7;\ 0{,}1)$.

**Đoạn 1.** $\|x^{(1)}-c^{(1)}_0\|^2=0{,}04+0{,}04=0{,}08$; $\|x^{(1)}-c^{(1)}_1\|^2=3{,}24+3{,}24=6{,}48$; $i_1=0$.

**Đoạn 2.** $\|x^{(2)}-c^{(2)}_0\|^2=7{,}29+0{,}01=7{,}30$; $\|x^{(2)}-c^{(2)}_1\|^2=0{,}09+0{,}01=0{,}10$; $i_2=1$.

**Kết quả.** Mã $(0,1)$, dài 2 bit; $\widehat x=(0;\ 2\mid3;\ 0)$; sai số tái dựng $\|x-\widehat x\|^2=0{,}04+0{,}04+0{,}09+0{,}01=0{,}18$.

**Kiểm tra lại.** $0{,}18=0{,}08+0{,}10$, tổng hai sai số đoạn; trong bốn véc-tơ tái dựng có thể, $\widehat x$ là véc-tơ gần $x$ nhất.
:::

![Đoạn 1 có tâm 0 tại (0; 2) và tâm 1 tại (2; 0), x gần tâm 0; đoạn 2 có tâm 0 tại (0; 0) và tâm 1 tại (3; 0), x gần tâm 1; mã của x là (0, 1).](img/lec-07/pq-vi-du.svg)

Trên hình, mỗi đoạn là một mặt phẳng con với hai tâm con; $x^{(1)}$ nằm gần tâm 0, $x^{(2)}$ nằm gần tâm 1. Mệnh đề sau chứng minh hai sự kiện của dòng kiểm tra trong trường hợp tổng quát.

::: proposition Mệnh đề 07.28 (Mã hóa theo đoạn và kích thước của PQ)
**Giả thiết.** $G_1,\ldots,G_m$ phân hoạch $\{1,\ldots,D\}$; mỗi bộ mã con có $k^*$ tâm; mã được tính theo Định nghĩa 07.27.

**Kết luận.**

- (a) Với mọi $c=(c^{(1)}\mid\cdots\mid c^{(m)})$ với $c^{(j)}\in\mathcal C^{(j)}$, $\|x-c\|^2=\sum_{j=1}^m\|x^{(j)}-c^{(j)}\|^2$.
- (b) $\widehat x$ là véc-tơ gần $x$ nhất trong tập tích $\mathcal C^{(1)}\times\cdots\times\mathcal C^{(m)}$, và $\|x-\widehat x\|^2=\sum_j\|x^{(j)}-c^{(j)}_{i_j(x)}\|^2$.
- (c) Mã dài $m\log_2k^*$ bit; có $(k^*)^m$ véc-tơ tái dựng; các bộ mã con chứa tổng cộng $k^*D$ số; mã hóa một véc-tơ tốn $\Theta(k^*D)$ phép toán.

**Điều kiện áp dụng.** Mọi $m$, $k^*$ với $k^*$ là lũy thừa của 2.

**Phạm vi.** Mệnh đề so $\widehat x$ với các véc-tơ của tập tích, không với một bộ mã bất kỳ có cùng số véc-tơ tái dựng.
:::

::: proof Chứng minh Mệnh đề 07.28
**Bước 1 (cộng theo đoạn).** $\|x-c\|^2=\sum_{t=1}^D(x_t-c_t)^2$. Vì $G_1,\ldots,G_m$ phân hoạch $\{1,\ldots,D\}$, mỗi chỉ số $t$ thuộc đúng một $G_j$, nên tổng tách thành $\sum_j\sum_{t\in G_j}(x_t-c_t)^2=\sum_j\|x^{(j)}-c^{(j)}\|^2$. Điều này chứng minh (a).

**Bước 2 (cực tiểu từng số hạng).** Theo (a), $\|x-c\|^2$ là tổng $m$ số hạng, số hạng $j$ chỉ phụ thuộc lựa chọn $c^{(j)}$. Tổng nhỏ nhất khi mỗi số hạng nhỏ nhất, tức $c^{(j)}=c^{(j)}_{i_j(x)}$ [do Định nghĩa 07.24]. Đây là $\widehat x$, chứng minh (b).

**Bước 3 (kích thước).** Mỗi chỉ số $i_j$ lấy $k^*$ giá trị, dài $\log_2k^*$ bit; $m$ chỉ số cho $m\log_2k^*$ bit và $(k^*)^m$ bộ mã khác nhau. Bộ mã con $j$ có $k^*$ tâm, mỗi tâm $|G_j|$ số, nên tổng là $k^*\sum_j|G_j|=k^*D$. Mã hóa chạy Thuật toán 07.25 trên mỗi đoạn, tốn $\Theta(k^*|G_j|)$, tổng $\Theta(k^*D)$. $\square$
:::

Các giả thiết của Mệnh đề 07.28 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ điều kiện phân hoạch, cho hai đoạn chồng nhau: với $D=2$, $G_1=\{1,2\}$, $G_2=\{2\}$, $x=(1;\ 1)$, $c=(0;\ 0)$, tổng theo đoạn là $2+1=3$ trong khi $\|x-c\|^2=2$, vì tọa độ thứ hai bị đếm hai lần.
- Bỏ phép mã hóa từng đoạn theo tâm gần nhất, chẳng hạn chọn $i_2=0$ trong Ví dụ 07.13: véc-tơ $(0;\ 2\mid0;\ 0)$ có sai số $0{,}08+7{,}30=7{,}38>0{,}18$.

Bước 1 dùng phân hoạch; Bước 2 dùng (a) và quy tắc tâm gần nhất. Bước 3 không dùng $m\mid D$; $k^*D$ đúng với mọi phân hoạch.

**Trong thực hành.** Với cùng độ dài mã $m\log_2k^*$ bit, bài giảng 8 (tr.33) ghi rằng $k^*$ lớn hơn và $m$ nhỏ hơn cho độ chính xác cao hơn nhưng bảng tâm lớn hơn và mã hóa chậm hơn, vì chi phí $\Theta(k^*D)$ của Mệnh đề 07.28(c) tăng theo $k^*$; hai đầu mút là $m=1$, k-means trên cả véc-tơ, và $k^*=2$, một bit mỗi đoạn.

::: example Ví dụ 07.14 (Hai cấu hình 64 bit và kho mười tỷ véc-tơ)
**Dữ kiện.** $D=128$, mã 64 bit: lượng tử hóa véc-tơ với $k=2^{64}$, hoặc lượng tử hóa tích với $m=8$, $k^*=256$ (Jégou, §II-B, tr.3).

**So sánh.**

| | Lượng tử hóa véc-tơ, $k=2^{64}$ | Lượng tử hóa tích, $m=8$, $k^*=256$ |
|---|---|---|
| số véc-tơ tái dựng | $2^{64}$ | $256^8=2^{64}$ |
| số thực trong bộ mã | $2^{64}\cdot128$ | $256\cdot128=32\,768$ |
| mã hóa một véc-tơ | $\Theta(2^{64}\cdot128)$ | $\Theta(32\,768)$ |

**Kho mở đầu.** BIODS 271 (tr.17) chọn đoạn 6 chiều và 256 tâm mỗi đoạn: $m=3072/6=512$, $\log_2k^*=8$, mã dài $512$ byte. $10^{10}$ mã chiếm $5{,}12$ TB, nhỏ hơn $122{,}88$ TB khoảng 24 lần; bộ mã con chứa $256\cdot3072$ số thực, khoảng $3{,}1$ MB.

**Kiểm tra lại.** Bộ mã của lượng tử hóa tích nhỏ hơn $2^{64}/2^8=2^{56}$ lần với cùng số véc-tơ tái dựng.
:::

### 4.3 Khoảng cách bất đối xứng và bảng tra

Kho giờ chỉ còn mã. Khi có truy vấn $q$, chúng ta giữ $q$ ở dạng đầy đủ và đo khoảng cách từ $q$ tới véc-tơ tái dựng của mỗi mã.

::: example Ví dụ 07.15 (Khoảng cách từ truy vấn tới một mã)
**Dữ kiện.** Bộ mã con của Ví dụ 07.13; véc-tơ $x=(0{,}2;\ 1{,}8\mid2{,}7;\ 0{,}1)$ chỉ còn mã $(0,1)$, tức $\widehat x=(0;\ 2\mid3;\ 0)$. Truy vấn $q=(0{,}1;\ 1{,}9\mid2{,}5;\ 0{,}2)$.

**Tính.** Đoạn 1: $\|q^{(1)}-(0;\ 2)\|^2=0{,}01+0{,}01=0{,}02$. Đoạn 2: $\|q^{(2)}-(3;\ 0)\|^2=0{,}25+0{,}04=0{,}29$. Ước lượng $\|q-\widehat x\|^2=0{,}31$.

**So với giá trị đúng.** $\|q-x\|^2=0{,}01+0{,}01+0{,}04+0{,}01=0{,}07$.

**Kiểm tra lại.** Phép tính chỉ dùng mã của $x$, các bộ mã con và $q$. Sai lệch $0{,}31-0{,}07=0{,}24$ gồm sai số tái dựng $0{,}18$ của $x$ và số hạng chéo $2(q-x)\cdot(x-\widehat x)=0{,}06$.
:::

![Hai mặt phẳng con của ví dụ PQ: đoạn 1 có tâm 0 tại (0; 2) và tâm 1 tại (2; 0), x ở (0,2; 1,8) gần tâm 0; đoạn 2 có tâm 0 tại (0; 0) và tâm 1 tại (3; 0), x ở (2,7; 0,1) gần tâm 1; truy vấn q ở (0,1; 1,9) và (2,5; 0,2).](img/lec-07/pq-vi-du-adc.svg)

Mỗi số hạng của $0{,}31$ là bình phương khoảng cách từ $q^{(j)}$ tới tâm con được chọn ở đoạn $j$.

::: definition Định nghĩa 07.29 (Khoảng cách bất đối xứng và đối xứng; Jégou, §III-A, tr.4)
Cho lượng tử hóa tích của Định nghĩa 07.27, truy vấn $q$ và véc-tơ $y$ của kho với véc-tơ tái dựng $\widehat y$.

- *Khoảng cách bất đối xứng* (asymmetric distance computation, ADC) là $\widetilde d(q,y)=\|q-\widehat y\|$.
- *Khoảng cách đối xứng* (symmetric distance computation, SDC) là $\widehat d(q,y)=\|\widehat q-\widehat y\|$, với $\widehat q$ là véc-tơ tái dựng của $q$.
:::

Ví dụ 07.15 tính $\widetilde d(q,x)^2=0{,}31$. "Bất đối xứng" nghĩa là truy vấn và véc-tơ kho được biểu diễn khác nhau: $q$ đầy đủ, $y$ chỉ có mã. ADC là $\widetilde d$ của Mệnh đề 07.7 cho chỉ mục PQ, nên chỉ mục PQ thiếu hàng xóm vì nguồn thứ hai. Thứ tự xếp hạng theo $\widetilde d$ và theo $\widetilde d^2$ trùng nhau vì căn bậc hai tăng, nên khi tìm hàng xóm chỉ cần bình phương.

Trong Ví dụ 07.15, số hạng của đoạn $j$ chỉ phụ thuộc $q^{(j)}$ và chỉ số $i_j$, mà $i_j$ chỉ có $k^*$ giá trị. Với một truy vấn, mỗi đoạn vì thế chỉ có $k^*$ số hạng khả dĩ; tính trước chúng thì chấm mỗi mã chỉ còn là tra bảng và cộng.

::: proposition Mệnh đề 07.30 (Phân tích khoảng cách bất đối xứng theo đoạn)
**Giả thiết.** Như Định nghĩa 07.29; với truy vấn $q$, đặt $T[j,i]=\|q^{(j)}-c^{(j)}_i\|^2$ với $1\le j\le m$, $0\le i<k^*$.

**Kết luận.** Với mọi $y$ có mã $(i_1(y),\ldots,i_m(y))$,

$$
\widetilde d(q,y)^2=\sum_{j=1}^mT[j,i_j(y)].
$$

**Điều kiện áp dụng.** Các đoạn phân hoạch tọa độ, như Mệnh đề 07.28.

**Phạm vi.** Bảng $T$ phụ thuộc $q$, nên được tính lại cho mỗi truy vấn.
:::

::: proof Chứng minh Mệnh đề 07.30
Áp dụng Mệnh đề 07.28(a) với $x=q$ và $c=\widehat y=(c^{(1)}_{i_1(y)}\mid\cdots\mid c^{(m)}_{i_m(y)})$: $\|q-\widehat y\|^2=\sum_j\|q^{(j)}-c^{(j)}_{i_j(y)}\|^2=\sum_jT[j,i_j(y)]$. $\square$
:::

Với truy vấn của Ví dụ 07.15, bảng $T$ có $m\times k^*=2\times2$ phần tử:

| $T[j,i]$ | $i=0$ | $i=1$ |
|---|---|---|
| $j=1$ | $0{,}02$ | $7{,}22$ |
| $j=2$ | $6{,}29$ | $0{,}29$ |

Mã $(0,1)$ cho $T[1,0]+T[2,1]=0{,}31$, như Ví dụ 07.15; mã $(1,0)$ cho $7{,}22+6{,}29=13{,}51$. Câu hỏi còn lại là ước lượng $\widetilde d$ sai lệch bao nhiêu so với $d$. Mệnh đề sau dùng bất đẳng thức tam giác của khoảng cách Euclid (Định nghĩa 06.14).

::: proposition Mệnh đề 07.31 (Cận sai số của ADC và SDC)
**Giả thiết.** $d$ là khoảng cách Euclid; $\widehat y$, $\widehat q$ là véc-tơ tái dựng của $y$, $q$ bởi một lượng tử hóa bất kỳ.

**Kết luận.**

- (a) $|d(q,y)-\widetilde d(q,y)|\le\|y-\widehat y\|$.
- (b) $|d(q,y)-\widehat d(q,y)|\le\|q-\widehat q\|+\|y-\widehat y\|$.

**Điều kiện áp dụng.** Mọi lượng tử hóa, kể cả lượng tử hóa véc-tơ và lượng tử hóa tích; bài báo PQ dẫn (a) ở dạng các bất đẳng thức (15)–(16) (Jégou, §III-B, tr.4–5).

**Phạm vi.** Cận áp dụng cho khoảng cách, không cho bình phương khoảng cách.
:::

::: proof Chứng minh Mệnh đề 07.31
**Bước 1 (chứng minh (a)).** Theo bất đẳng thức tam giác, $d(q,y)\le d(q,\widehat y)+d(\widehat y,y)$ và $d(q,\widehat y)\le d(q,y)+d(y,\widehat y)$. Hai bất đẳng thức cho $-\|y-\widehat y\|\le d(q,y)-\widetilde d(q,y)\le\|y-\widehat y\|$.

**Bước 2 (chứng minh (b)).** Tương tự, $|d(q,y)-d(\widehat q,y)|\le\|q-\widehat q\|$ và $|d(\widehat q,y)-d(\widehat q,\widehat y)|\le\|y-\widehat y\|$. Cộng hai bất đẳng thức và dùng bất đẳng thức tam giác cho giá trị tuyệt đối. $\square$
:::

Trên Ví dụ 07.15, $d(q,x)=\sqrt{0{,}07}\approx0{,}265$ và $\widetilde d(q,x)=\sqrt{0{,}31}\approx0{,}557$, nên sai lệch $0{,}292$ không vượt $\|x-\widehat x\|=\sqrt{0{,}18}\approx0{,}424$.

Truy vấn cũng được mã hóa thành $(0,1)$, vì $T[1,0]<T[1,1]$ và $T[2,1]<T[2,0]$, nên $\widehat q=\widehat x$ và $\widehat d(q,x)=0$: SDC không phân biệt được $x$ với mọi véc-tơ khác có cùng mã. Cận (b) cộng thêm sai số của $q$, $\sqrt{0{,}31}\approx0{,}557$. Jégou (§III-A, tr.4) chọn ADC vì sai lệch khoảng cách thấp hơn với độ phức tạp tương tự; ở tr.5, sai số bình phương trung bình của khoảng cách bị chặn bởi MSE với ADC và bởi $2\times$MSE với SDC.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ bất đẳng thức tam giác bằng cách đo bằng bình phương khoảng cách: trên Ví dụ 07.15, $|\|q-x\|^2-\|q-\widehat x\|^2|=|0{,}07-0{,}31|=0{,}24>\|x-\widehat x\|^2=0{,}18$, nên cận dạng (a) không đúng cho bình phương.

Bước 1 và Bước 2 chỉ dùng bất đẳng thức tam giác. Mệnh đề 07.30 và 07.31 cho phép viết thuật toán quét kho mã: một bảng cho mỗi truy vấn, một tổng $m$ số hạng cho mỗi mã.

::: algorithm Thuật toán 07.32 (Quét mã PQ bằng bảng tra)
**Đầu vào.** Truy vấn $q$; bộ mã con $\mathcal C^{(1)},\ldots,\mathcal C^{(m)}$; tập $S$ gồm $n_c$ cặp (chỉ số, mã PQ); số nguyên $K\ge1$.

**Đầu ra.** Tối đa $K$ chỉ số của $S$ có $\widetilde d(q,\cdot)$ nhỏ nhất, theo thứ tự $(\widetilde d,\text{chỉ số})$ tăng dần.

**Giả thiết.** Như Mệnh đề 07.30; $H$ là đống cực đại như Thuật toán 07.2.

1. Lập bảng $T[j,i]=\|q^{(j)}-c^{(j)}_i\|^2$ cho mọi $j$, $i$.
2. Với mỗi cặp $(t,(i_1,\ldots,i_m))\in S$: tính $\delta=\sum_jT[j,i_j]$; cập nhật $H$ bằng $(\delta,t)$ như bước 2 của Thuật toán 07.2.
3. Trả các chỉ số trong $H$ theo thứ tự tăng dần.

**Dừng.** Sau $n_c$ lượt ở bước 2.

**Trường hợp biên.** Khi $n_c<K$, trả $n_c$ chỉ số.

**Chi phí.**

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1: lập bảng | $mk^*$ phần tử | $\Theta(D/m)$ | $\Theta(k^*D)$; lưu $mk^*$ số |
| 2: chấm một mã | $n_c$ | $m$ lần tra, $m-1$ phép cộng | $\Theta(mn_c)$ |
| 2: cập nhật đống | $n_c$ | $O(\log K)$ | $O(n_c\log K)$ |
:::

Theo Mệnh đề 07.30, $\delta$ ở bước 2 bằng $\widetilde d(q,y_t)^2$, nên Thuật toán 07.32 là Thuật toán 07.2 với $d$ thay bằng $\widetilde d$ và kho thay bằng $S$; theo Mệnh đề 07.3, nó trả đúng $K$ phần tử nhỏ nhất của $S$ theo $\widetilde d$. So với tính trực tiếp $\Theta(D)$ mỗi véc-tơ, tổng $\Theta(k^*D+mn_c)$ có lợi khi $n_c$ lớn hơn nhiều $k^*$, vì bảng được dùng lại cho mọi mã.

::: example Ví dụ 07.16 (Quét đủ kho mã mười tỷ véc-tơ)
**Dữ kiện.** $N=10^{10}$, $D=3072$, $m=512$, $k^*=256$, $S=Y$. Giả sử máy xử lý $10^{12}$ thao tác mỗi giây.

**So sánh một truy vấn.**

| | Quét véc-tơ gốc | Quét mã PQ |
|---|---|---|
| dữ liệu đọc | $122{,}88$ TB | $5{,}12$ TB |
| phép toán | $ND\approx3{,}07\cdot10^{13}$ lượt tọa độ | $Nm=5{,}12\cdot10^{12}$ lần tra |
| số véc-tơ được chấm $n_c$ | $10^{10}$ | $10^{10}$ |
| thời gian | $30{,}72$ s | $5{,}12$ s |

**Kiểm tra lại.** Chi phí lập bảng $7{,}9\cdot10^5$ nhỏ hơn $Nm$ hơn sáu bậc; thời gian giảm đúng $D/m=6$ lần, bằng số tọa độ mỗi đoạn.
:::

::: remark Nhận xét 07.33 (Trong thực hành: tham số và cài đặt PQ)
Bài báo PQ (§II-B, tr.4) ghi rằng $k^*=256$ và $m=8$ thường là lựa chọn hợp lý, và chi phí tăng khi bảng tâm con không còn nằm trong bộ nhớ đệm. Bảng $T$ của một truy vấn có $mk^*$ số, $512\cdot256=131\,072$ số với cấu hình của Ví dụ 07.16. Theo bài báo (§III-A, tr.4), ưu điểm duy nhất của SDC là truy vấn cũng chỉ lưu bằng mã.
:::

::: exercise Bài tập 07.8 (Mã của một điểm khác)
Cho bộ mã $c_0=(0;\ 0)$, $c_1=(2;\ 0)$, $c_2=(0;\ 2)$ và điểm $y=(0{,}6;\ 1{,}5)$.

- (a) Tính bình phương khoảng cách từ $y$ tới ba tâm.
- (b) Xác định mã, véc-tơ tái dựng và sai số tái dựng của $y$.
:::

::: hint
Tính ba bình phương khoảng cách như Ví dụ 07.11.
:::

::: solution
**Câu (a).** $\|y-c_0\|^2=0{,}36+2{,}25=2{,}61$; $\|y-c_1\|^2=1{,}96+2{,}25=4{,}21$; $\|y-c_2\|^2=0{,}36+0{,}25=0{,}61$.

**Câu (b).** Mã 2; $\widehat y=(0;\ 2)$; sai số $0{,}61$.

**Kiểm tra lại.** $y_2=1{,}5>y_1=0{,}6$ và $y_2>1$, nên $y$ nằm trong ô của $c_2$ theo các ranh giới của Ví dụ 07.11.
:::

::: exercise Bài tập 07.9 (Chấm một mã bằng bảng tra)
Bảng tra của một truy vấn với $m=3$, $k^*=4$, chỉ số tâm $i=0,1,2,3$:

| $T[j,i]$ | $i=0$ | $i=1$ | $i=2$ | $i=3$ |
|---|---|---|---|---|
| $j=1$ | $1$ | $4$ | $0{,}5$ | $2$ |
| $j=2$ | $3$ | $0{,}2$ | $1$ | $5$ |
| $j=3$ | $0{,}7$ | $2$ | $3$ | $0{,}1$ |

- (a) Tính $\widetilde d^2$ của mã $(2,0,3)$.
- (b) Tìm mã có $\widetilde d^2$ nhỏ nhất.
:::

::: hint
Mã $(i_1,i_2,i_3)$ cho $T[1,i_1]+T[2,i_2]+T[3,i_3]$ (Mệnh đề 07.30); số hạng mỗi hàng chọn độc lập.
:::

::: solution
**Câu (a).** $T[1,2]+T[2,0]+T[3,3]=0{,}5+3+0{,}1=3{,}6$.

**Câu (b).** Mỗi hàng chọn phần tử nhỏ nhất: $i_1=2$ ($0{,}5$), $i_2=1$ ($0{,}2$), $i_3=3$ ($0{,}1$); mã $(2,1,3)$ cho $0{,}8$.

**Kiểm tra lại.** Câu (b) là Mệnh đề 07.28(b) đọc trên bảng: cực tiểu tổng bằng tổng các cực tiểu hàng; $0{,}8$ chính là $\|q-\widehat q\|^2$ với $\widehat q$ là véc-tơ tái dựng của $q$.
:::

::: exercise Bài tập 07.10 (Kích thước mã cho tập GIST)
Tập GIST của bài báo PQ có $1\,000\,991$ véc-tơ $D=960$ chiều (Jégou, Bảng III, tr.8). Với lượng tử hóa tích $m=8$, $k^*=256$ và số thực 4 byte, tính:

- (a) số byte mỗi mã;
- (b) số thực trong các bộ mã con;
- (c) dung lượng mã của cả kho và tỷ lệ so với kho gốc.
:::

::: hint
Dùng Mệnh đề 07.28(c).
:::

::: solution
**Câu (a).** Mã dài $8\cdot8=64$ bit, tức 8 byte.

**Câu (b).** $k^*D=256\cdot960=245\,760$ số thực.

**Câu (c).** Mã của kho: $1\,000\,991\cdot8=8\,007\,928$ byte; kho gốc: $1\,000\,991\cdot960\cdot4=3\,843\,805\,440$ byte; tỷ lệ $480$.

**Kiểm tra lại.** $960\cdot4/8=480$ không phụ thuộc số véc-tơ; mỗi đoạn có $960/8=120$ chiều.
:::

Như vậy, lượng tử hóa tích tạo mã dài từ các bộ mã con nhỏ (Định nghĩa 07.27, Mệnh đề 07.28), và khoảng cách bất đối xứng tính từ mã bằng bảng tra (Mệnh đề 07.30, Thuật toán 07.32) với sai lệch không vượt khoảng cách $\|y-\widehat y\|$ tới véc-tơ tái dựng (Mệnh đề 07.31). Kho mở đầu thu từ $122{,}88$ TB xuống $5{,}12$ TB. Tuy nhiên, lượng tử hóa tích giảm chi phí một phép đo nhưng giữ $n_c=N$. Trong Mục 5, chúng ta chỉ mở một phần kho mã bằng một lượng tử hóa thô.

<!-- note-topic-id: lec-07-topic-05 -->
## 5. Tệp đảo kết hợp lượng tử hóa tích (IVF-PQ)

Quét mã PQ của kho mở đầu chấm $n_c=10^{10}$ mã và mất $5{,}12$ giây cho một truy vấn (Ví dụ 07.16), gấp 512 lần ngân sách 10 ms. Chúng ta cần chọn một phần nhỏ các mã để chấm mà vẫn giữ các hàng xóm thật.

### 5.1 Tệp đảo

::: example Ví dụ 07.17 (Bốn danh sách đảo)
**Dữ kiện.** Bốn tâm $\mu_0=(2;\ 2)$, $\mu_1=(8;\ 2)$, $\mu_2=(2;\ 8)$, $\mu_3=(8;\ 8)$ và mười sáu điểm: $y_1=(1;\ 1{,}5)$, $y_2=(2{,}5;\ 1)$, $y_3=(4{,}5;\ 3{,}8)$, $y_4=(1{,}5;\ 3{,}2)$, $y_5=(7;\ 1)$, $y_6=(9;\ 1{,}5)$, $y_7=(8{,}5;\ 3)$, $y_8=(6{,}5;\ 2{,}5)$, $y_9=(1;\ 7)$, $y_{10}=(3;\ 7{,}5)$, $y_{11}=(2;\ 9)$, $y_{12}=(3{,}5;\ 8{,}8)$, $y_{13}=(7;\ 7)$, $y_{14}=(9;\ 8{,}5)$, $y_{15}=(8;\ 9{,}2)$, $y_{16}=(6{,}5;\ 8)$. Truy vấn $q=(6;\ 3{,}5)$.

**Gán điểm.** Mỗi điểm vào danh sách của tâm gần nó nhất: $L_0=\{y_1,y_2,y_3,y_4\}$, $L_1=\{y_5,y_6,y_7,y_8\}$, $L_2=\{y_9,\ldots,y_{12}\}$, $L_3=\{y_{13},\ldots,y_{16}\}$. Ví dụ: $\|y_3-\mu_0\|^2=9{,}49<\|y_3-\mu_1\|^2=15{,}49$.

**Chọn danh sách.** $\|q-\mu_0\|^2=18{,}25$, $\|q-\mu_1\|^2=6{,}25$, $\|q-\mu_2\|^2=36{,}25$, $\|q-\mu_3\|^2=24{,}25$. Mở hai danh sách gần nhất: $L_1$ rồi $L_0$.

**Kiểm tra lại.** Chỉ 8 trong 16 điểm được chấm; hai danh sách không mở ứng với hai tâm xa $q$ nhất.
:::

![Bốn tâm thô μ0 đến μ3 chia mặt phẳng thành bốn ô ứng với bốn danh sách đảo L0 đến L3, mỗi ô bốn điểm; truy vấn q ở (6; 3,5) gần μ1 nhất rồi đến μ0; với nprobe bằng 2 chỉ L1 và L0 được mở, hai ô còn lại viền nét đứt.](img/lec-07/tep-dao.svg)

Hai ô được mở mang nhãn "(mở)"; điểm $y_3$ nằm sát ranh giới giữa ô $L_0$ và ô $L_1$.

::: definition Định nghĩa 07.34 (Tệp đảo)
Một *lượng tử hóa thô* (coarse quantizer) là một lượng tử hóa véc-tơ với $k_c$ tâm $\mu_0,\ldots,\mu_{k_c-1}$ (Định nghĩa 07.24). Với $y\in Y$, đặt $a(y)$ là mã của $y$ theo lượng tử hóa thô, và *danh sách đảo* (inverted list) thứ $i$ là $L_i=\{y\in Y: a(y)=i\}$. Một *tệp đảo* (inverted file, IVF) lưu $k_c$ tâm và $k_c$ danh sách. Với truy vấn $q$ và số nguyên $1\le \mathit{nprobe}\le k_c$, tập $P$ gồm $\mathit{nprobe}$ chỉ số $i$ có $\|q-\mu_i\|$ nhỏ nhất, phá hòa theo chỉ số, và tập được đo là $S=\bigcup_{i\in P}L_i$.
:::

Các danh sách phân hoạch $Y$ vì mỗi $y$ có đúng một mã thô (Jégou, §IV-B–C, tr.6–7). Tệp đảo là một cách chọn $S$ trong Mệnh đề 07.7, nên một hàng xóm thật thiếu khi ô của nó không được mở. Ví dụ: $y_3=(4{,}5;\ 3{,}8)$ có $\|q-y_3\|^2=2{,}34$, là hàng xóm gần thứ hai của $q$ sau $y_8$ ($1{,}25$), nhưng $y_3\in L_0$; với $\mathit{nprobe}=1$, chỉ $L_1$ được mở và $y_3$ thiếu theo Mệnh đề 07.7(b). Một nhầm lẫn thường gặp là đọc $\mathit{nprobe}$ như số ứng viên: $\mathit{nprobe}$ là số danh sách, còn số ứng viên là $\sum_{i\in P}|L_i|$.

### 5.2 Mã hóa phần dư

Mỗi phần tử của danh sách cần một mã ngắn để chấm bằng bảng tra. Điểm trong cùng ô nằm gần tâm của ô, nên thay vì mã hóa $y$, IVF-PQ mã hóa *phần dư* (residual) $r(y)=y-\mu_{a(y)}$ bằng một lượng tử hóa tích chung cho mọi ô (Jégou, §IV-A, tr.6), và danh sách $L_i$ lưu cặp (mã định danh của $y$, mã PQ của $r(y)$). Khi quét $L_i$, truy vấn được dời về cùng gốc $\mu_i$: *truy vấn dư* (residual query) $\widetilde q_i=q-\mu_i$.

::: example Ví dụ 07.18 (Phần dư của $y_8$)
**Dữ kiện.** $y_8=(6{,}5;\ 2{,}5)\in L_1$, $\mu_1=(8;\ 2)$, $\mu_0=(2;\ 2)$, $q=(6;\ 3{,}5)$.

**Tính.** $r(y_8)=(-1{,}5;\ 0{,}5)$; $\widetilde q_1=(-2;\ 1{,}5)$; $\|\widetilde q_1-r(y_8)\|^2=0{,}25+1=1{,}25$.

**Kiểm tra lại.** $\|q-y_8\|^2=0{,}25+1=1{,}25$, cùng giá trị. Dùng nhầm $\widetilde q_0=(4;\ 1{,}5)$ cho $5{,}5^2+1^2=31{,}25$.
:::

![Hai ô dưới của ví dụ tệp đảo: mũi tên liền từ μ1 tới y8 là phần dư r(y8); hai đoạn nét đứt từ μ1 và μ0 tới q là truy vấn dư dùng khi quét L1 và L0.](img/lec-07/tep-dao-du.svg)

Mũi tên liền từ $\mu_1$ tới $y_8$ là $r(y_8)$; hai đoạn nét đứt từ $\mu_1$ và $\mu_0$ tới $q$ là $\widetilde q_1$ và $\widetilde q_0$. Mệnh đề sau nói đẳng thức của Ví dụ 07.18 đúng với mọi phần tử của mọi danh sách, miễn truy vấn dư lấy đúng tâm của danh sách.

::: proposition Mệnh đề 07.35 (Phần dư và truy vấn dư)
**Giả thiết.** Tệp đảo của Định nghĩa 07.34; $y\in L_i$; $\widehat r(y)$ là véc-tơ tái dựng của $r(y)$ bởi lượng tử hóa tích, và $\widehat y=\mu_i+\widehat r(y)$.

**Kết luận.**

- (a) $\|q-y\|=\|\widetilde q_i-r(y)\|$ và $\|q-\widehat y\|=\|\widetilde q_i-\widehat r(y)\|$; do đó ADC trên phần dư với bảng tra lập cho $\widetilde q_i$ cho đúng $\widetilde d(q,y)=\|q-\widehat y\|$, và $|d(q,y)-\widetilde d(q,y)|\le\|r(y)-\widehat r(y)\|$.
- (b) Nếu $\mu_i$ là trọng tâm của $L_i$, thì với mọi $c\in\mathbb R^D$, $\sum_{y\in L_i}\|r(y)\|^2\le\sum_{y\in L_i}\|y-c\|^2$.

**Điều kiện áp dụng.** (a) đúng với mọi tâm thô; (b) cần điều kiện Lloyd thứ hai cho ô $i$ (Nhận xét 07.26).

**Phạm vi.** (b) so tổng bình phương độ dài, không so sai số tái dựng của hai cách mã hóa.
:::

::: proof Chứng minh Mệnh đề 07.35
**Bước 1 (chứng minh (a)).** $q-y=(q-\mu_i)-(y-\mu_i)=\widetilde q_i-r(y)$, và tương tự $q-\widehat y=\widetilde q_i-\widehat r(y)$. Theo Mệnh đề 07.30 áp dụng cho truy vấn $\widetilde q_i$ và mã của $r(y)$, tổng tra bảng bằng $\|\widetilde q_i-\widehat r(y)\|^2$. Cận sai số là Mệnh đề 07.31(a) cho $\widetilde q_i$, $r(y)$, $\widehat r(y)$.

**Bước 2 (chứng minh (b)).** Với $\mu_i=\frac1{|L_i|}\sum_{y\in L_i}y$, ta có $\sum_{y\in L_i}(y-\mu_i)=0$. Khai triển

$$
\begin{aligned}
&\sum_{y\in L_i}\|y-c\|^2\\
&\quad=\sum_{y\in L_i}\|y-\mu_i\|^2\\
&\qquad+|L_i|\,\|\mu_i-c\|^2,
\end{aligned}
$$

vì số hạng chéo $2(\mu_i-c)\cdot\sum_{y\in L_i}(y-\mu_i)$ bằng 0. Số hạng cuối không âm. $\square$
:::

Kết luận (a) là đẳng thức chuyển gốc: khoảng cách không đổi khi dời cả $q$ lẫn $y$ đi cùng một véc-tơ $\mu_i$. Nhầm lẫn thường gặp là dùng một truy vấn dư cho mọi danh sách; mỗi danh sách có tâm riêng nên cần bảng tra riêng, tổng $\mathit{nprobe}$ bảng.

Kết luận (b) với $c=0$ nói rằng khi tâm là trọng tâm, phần dư có tổng bình phương độ dài không vượt tổng bình phương độ dài của chính các véc-tơ. Các tâm của Ví dụ 07.17 không là trọng tâm (trọng tâm của $L_0$ là $(2{,}375;\ 2{,}375)$), nên (b) không áp dụng cho ví dụ đó.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ điều kiện $y\in L_i$ ở (a), tức chấm $y$ bằng bảng của một tâm khác: Ví dụ 07.18 cho $31{,}25$ thay cho $1{,}25$.
- Bỏ điều kiện trọng tâm ở (b): với danh sách gồm một điểm $y=(1;\ 0)$ và tâm $\mu=(5;\ 0)$, $\|r(y)\|^2=16>\|y\|^2=1$.

Bước 1 dùng $y\in L_i$ để $r(y)$ được tính với đúng $\mu_i$; Bước 2 dùng $\sum(y-\mu_i)=0$, tức điều kiện trọng tâm.

### 5.3 Thuật toán và chi phí

Ghép tệp đảo, phần dư và Thuật toán 07.32 cho thủ tục truy vấn của bài báo PQ (§IV-C, tr.7). Đống $H$ ở đây giữ kết quả, khác hàng đợi $C$ của `SEARCH-LAYER`.

::: algorithm Thuật toán 07.36 (Truy vấn IVF-PQ)
**Đầu vào.** Truy vấn $q$; tâm thô $\mu_0,\ldots,\mu_{k_c-1}$; danh sách $L_i$ gồm các cặp (mã định danh, mã PQ của phần dư); bộ mã con của lượng tử hóa tích; số nguyên $K\ge1$ và $1\le \mathit{nprobe}\le k_c$.

**Đầu ra.** Tối đa $K$ mã định danh có $\widetilde d(q,\cdot)$ nhỏ nhất trong $S=\bigcup_{i\in P}L_i$, theo thứ tự tăng dần.

**Giả thiết.** Như Mệnh đề 07.35(a); $H$ là đống cực đại với dung lượng $K$.

1. Tính $\|q-\mu_i\|^2$ cho mọi $i$; lấy $P$ gồm $\mathit{nprobe}$ chỉ số nhỏ nhất.
2. Với mỗi $i\in P$: đặt $\widetilde q_i=q-\mu_i$; lập bảng $T_i$ cho $\widetilde q_i$; với mỗi cặp (id, mã) trong $L_i$, tính $\delta=\sum_jT_i[j,\text{mã}_j]$ và cập nhật $H$ bằng $(\delta,\text{id})$.
3. Trả các mã định danh trong $H$ theo thứ tự tăng dần.

**Dừng.** Sau khi duyệt hết $\sum_{i\in P}|L_i|$ phần tử.

**Trường hợp biên.** Thuật toán trả $\min\big(K,\sum_{i\in P}|L_i|\big)$ mã định danh; khi các danh sách mở có ít hơn $K$ phần tử, đầu ra thiếu.

**Chi phí.**

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1: khoảng cách tới tâm thô | $k_c$ | $\Theta(D)$ | $\Theta(k_cD)$ |
| 1: chọn $\mathit{nprobe}$ tâm | $k_c$ | $O(\log \mathit{nprobe})$ | $O(k_c\log \mathit{nprobe})$ |
| 2: lập bảng | $\mathit{nprobe}$ | $\Theta(k^*D)$ | $\Theta(\mathit{nprobe}\,k^*D)$ |
| 2: chấm mã | $\sum_{i\in P}|L_i|$ | $m$ lần tra | $\Theta\big(m\sum_{i\in P}|L_i|\big)$ |
| 2: cập nhật $H$ | $\sum_{i\in P}|L_i|$ | $O(\log K)$ | $O\big(\log K\sum_{i\in P}|L_i|\big)$ |
:::

Theo Mệnh đề 07.35(a), $\delta$ của mỗi phần tử bằng $\widetilde d(q,y)^2$, nên Thuật toán 07.36 là Thuật toán 07.32 chạy trên $S$ với một bảng cho mỗi danh sách; theo Mệnh đề 07.3, $H$ giữ đúng $K$ cặp nhỏ nhất đã chấm. Đầu ra là mã định danh, không là mã PQ.

::: example Ví dụ 07.19 (Truy vấn IVF-PQ trên bốn danh sách)
**Dữ kiện.** Mười sáu điểm và bốn tâm của Ví dụ 07.17; $q=(6;\ 3{,}5)$; $K=3$; $\mathit{nprobe}=2$. Giả sử mã phần dư tái dựng đúng phần dư, nên $\widetilde d=d$.

**Danh sách $L_1$.** Bình phương khoảng cách: $y_8$ $1{,}25$; $y_7$ $6{,}5$; $y_5$ $7{,}25$; $y_6$ $13$.

**Danh sách $L_0$.** $y_3$ $2{,}34$; $y_2$ $18{,}5$; $y_4$ $20{,}34$; $y_1$ $29$.

**Kết quả.** Sau 8 lần chấm, $H$ giữ $y_8$, $y_3$, $y_7$.

**Kiểm tra lại.** Trong cả kho, điểm gần thứ tư là $y_5$ ($7{,}25$) và các điểm của $L_2$, $L_3$ đều có bình phương khoảng cách ít nhất $13{,}25$, nên $\mathcal N_3(q)=\{8,3,7\}$ và $\operatorname{recall@}3(q)=1$.
:::

Ví dụ 07.19 tách tác dụng của $\mathit{nprobe}$ khỏi sai số mã bằng giả thiết $\widetilde d=d$; khi đó theo Mệnh đề 07.7(c), độ thu hồi bằng 1 khi và chỉ khi hai danh sách mở chứa cả ba hàng xóm thật. Mệnh đề sau cộng chi phí các bước.

::: proposition Mệnh đề 07.37 (Chi phí truy vấn IVF-PQ)
**Giả thiết.** Thuật toán 07.36 với $k_c$ tâm thô, lượng tử hóa tích $m$ đoạn, $k^*$ tâm mỗi đoạn.

**Kết luận.**

- (a) Chi phí một truy vấn là $\Theta(k_cD)+\Theta(\mathit{nprobe}\,k^*D)+\Theta\big(m\sum_{i\in P}|L_i|\big)$, cộng $O\big(k_c\log \mathit{nprobe}+\log K\sum_{i\in P}|L_i|\big)$ cho các đống.
- (b) Nếu mọi danh sách có đúng $N/k_c$ phần tử, thì $\sum_{i\in P}|L_i|=\mathit{nprobe}\,N/k_c$.

**Điều kiện áp dụng.** (a) đúng với mọi phân bố cỡ danh sách; (b) cần danh sách cân bằng.

**Phạm vi.** Mô hình đếm phép toán; không tính thời gian đọc dữ liệu.
:::

::: proof Chứng minh Mệnh đề 07.37
**Bước 1.** Cộng cột "Đóng góp" của bảng chi phí trong Thuật toán 07.36 được (a).

**Bước 2.** Với $|L_i|=N/k_c$ cho mọi $i$ và $|P|=\mathit{nprobe}$, tổng là $\mathit{nprobe}\cdot N/k_c$, được (b). $\square$
:::

Ba số hạng chính của (a) là chọn tâm thô, lập $\mathit{nprobe}$ bảng và chấm mã. Bài báo PQ (tr.7) dùng (b) với giả thiết danh sách cân bằng. Bỏ giả thiết đó: nếu một danh sách chứa $N-k_c+1$ véc-tơ và mỗi danh sách còn lại một véc-tơ, một truy vấn mở danh sách lớn chấm gần như cả kho với $\mathit{nprobe}=1$, trong khi (b) dự đoán $N/k_c$.

::: example Ví dụ 07.20 (IVF-PQ cho kho mười tỷ véc-tơ)
**Dữ kiện.** $N=10^{10}$, $D=3072$, $m=512$, $k^*=256$; giả sử $k_c=10^5$, $\mathit{nprobe}=64$, danh sách cân bằng và máy xử lý $10^{12}$ thao tác mỗi giây.

**Tính theo Mệnh đề 07.37.** Chọn tâm thô: $10^5\cdot3072\approx3{,}07\cdot10^8$. Lập bảng: $64\cdot256\cdot3072\approx5{,}03\cdot10^7$. Chấm mã: $64\cdot10^{10}/10^5=6{,}4\cdot10^6$ mã, mỗi mã 512 lần tra, $\approx3{,}28\cdot10^9$. Tổng $\approx3{,}63\cdot10^9$, tức $\approx3{,}6$ ms.

**Dữ liệu và bộ nhớ.** Mỗi phần tử danh sách gồm mã 512 byte và mã định danh 8 byte, nên truy vấn đọc $6{,}4\cdot10^6\cdot520\approx3{,}33$ GB; đọc chừng đó trong $3{,}6$ ms cần băng thông khoảng $0{,}92$ TB/s. Kho chiếm $(512+8)\cdot10^{10}=5{,}2$ TB, tâm thô $10^5\cdot3072\cdot4\approx1{,}23$ GB, bộ mã con $\approx3{,}1$ MB.

**Kiểm tra lại.** So với $5{,}12\cdot10^{12}$ lần tra của Ví dụ 07.16, số thao tác giảm khoảng $1\,409$ lần; số mã được chấm là $6{,}4\cdot10^6/10^{10}=0{,}064\%$ kho.
:::

::: remark Nhận xét 07.38 (Trong thực hành: tham số và hệ thống IVF-PQ)
Bài giảng 9 (tr.5) chọn $k_c=N^{1/2}$, tức khoảng $32\,000$ khi $N=10^9$, và nén mỗi véc-tơ thành 32 byte để một tỷ điểm vừa 32 GB bộ nhớ. Mở nhiều danh sách chỉ áp dụng cho truy vấn, không cho véc-tơ kho, vì gán một véc-tơ vào nhiều danh sách làm tăng bộ nhớ (Jégou, §IV-C, tr.7). Một lượng tử hóa tích chung được học trên phần dư của mọi ô; dùng một bộ cho mỗi ô cần $k_c\cdot D\cdot k^*$ số thực (Jégou, §IV-A, tr.6).
:::

::: exercise Bài tập 07.11 (Số danh sách mở và độ thu hồi)
Trên mười sáu điểm $y_1=(1;\ 1{,}5)$, $y_2=(2{,}5;\ 1)$, $y_3=(4{,}5;\ 3{,}8)$, $y_4=(1{,}5;\ 3{,}2)$ (danh sách $L_0$, tâm $\mu_0=(2;\ 2)$), $y_5=(7;\ 1)$, $y_6=(9;\ 1{,}5)$, $y_7=(8{,}5;\ 3)$, $y_8=(6{,}5;\ 2{,}5)$ (danh sách $L_1$, tâm $\mu_1=(8;\ 2)$), $y_9,\ldots,y_{12}$ (danh sách $L_2$, tâm $\mu_2=(2;\ 8)$), $y_{13}=(7;\ 7)$, $y_{14}=(9;\ 8{,}5)$, $y_{15}=(8;\ 9{,}2)$, $y_{16}=(6{,}5;\ 8)$ (danh sách $L_3$, tâm $\mu_3=(8;\ 8)$), truy vấn $q=(6;\ 3{,}5)$ và $\widetilde d=d$. Sáu điểm gần $q$ nhất của kho, theo thứ tự, là $y_8,y_3,y_7,y_5,y_6,y_{13}$. Chạy Thuật toán 07.36 và ghi danh sách mở, số mã được chấm, kết quả và độ thu hồi trong ba trường hợp:

- (a) $K=4$, $\mathit{nprobe}=1$;
- (b) $K=6$, $\mathit{nprobe}=2$;
- (c) $K=6$, $\mathit{nprobe}=3$.
:::

::: hint
Bình phương khoảng cách từ $q$ tới các tâm là $\mu_1$ $6{,}25$, $\mu_0$ $18{,}25$, $\mu_3$ $24{,}25$, $\mu_2$ $36{,}25$.
:::

::: solution
**Câu (a).** Mở $L_1$, chấm 4 mã: $y_8$ $1{,}25$; $y_7$ $6{,}5$; $y_5$ $7{,}25$; $y_6$ $13$. Kết quả cả bốn điểm của $L_1$; $\operatorname{recall@}4(q)=3/4$, thiếu $y_3\in L_0$.

**Câu (b).** Mở $L_1$, $L_0$, chấm 8 mã; $L_0$ cho $y_3$ $2{,}34$, $y_2$ $18{,}5$, $y_4$ $20{,}34$, $y_1$ $29$. Sáu điểm đầu là $y_8,y_3,y_7,y_5,y_6,y_2$; $\operatorname{recall@}6(q)=5/6$, thiếu $y_{13}\in L_3$.

**Câu (c).** Mở thêm $L_3$, chấm 12 mã; $L_3$ cho $y_{13}$ $13{,}25$, $y_{16}$ $20{,}5$, $y_{14}$ $34$, $y_{15}$ $36{,}49$. Sáu điểm đầu là $y_8,y_3,y_7,y_5,y_6,y_{13}$; $\operatorname{recall@}6(q)=1$.

**Kiểm tra lại.** Mỗi lần thiếu điểm đều do điểm nằm ngoài $S$ (Mệnh đề 07.7(b)); khi $\widetilde d=d$, độ thu hồi bằng số hàng xóm thật thuộc $S$ chia $K$ (Mệnh đề 07.7(d)): $3/4$, $5/6$, $6/6$.
:::

::: exercise Bài tập 07.12 (Một tỷ véc-tơ với danh sách cân bằng)
Kho có $N=10^9$ véc-tơ, $k_c=32\,000$ danh sách cân bằng, $\mathit{nprobe}=16$, lượng tử hóa tích $m=8$.

- (a) Tính số mã được chấm và số lần tra cho một truy vấn.
- (b) So với quét đủ kho mã.
:::

::: hint
Dùng Mệnh đề 07.37(b).
:::

::: solution
**Câu (a).** $16\cdot10^9/32\,000=500\,000$ mã; mỗi mã 8 lần tra, tổng $4\cdot10^6$ lần tra.

**Câu (b).** Quét đủ cần $8\cdot10^9$ lần tra, gấp $2\,000$ lần.

**Kiểm tra lại.** Tỷ lệ $2\,000=k_c/\mathit{nprobe}$; tỷ lệ này chỉ đúng khi danh sách cân bằng.
:::

::: exercise Bài tập 07.13 (Chẩn đoán độ thu hồi thấp)
Một chỉ mục IVF-PQ, còn véc-tơ gốc ở bộ nhớ ngoài, trả 10 mã định danh cho truy vấn $q$ với $K=10$. Trong 10 hàng xóm thật: 6 có trong kết quả; 3 nằm ở các danh sách không mở; 1 nằm ở một danh sách được mở nhưng xếp hạng 14 theo $\widetilde d$.

- (a) Tính $\operatorname{recall@}10(q)$.
- (b) Xếp 4 hàng xóm bị thiếu theo hai nguồn của Mệnh đề 07.7.
- (c) Tính độ thu hồi sau khi xếp hạng lại 20 ứng viên đầu theo $\widetilde d$ bằng khoảng cách đúng.
- (d) Nêu tham số phải đổi để tìm lại 3 hàng xóm còn lại.
:::

::: hint
Ở câu (c), áp dụng Mệnh đề 07.7(d) cho danh sách 20 ứng viên.
:::

::: solution
**Câu (a).** $\operatorname{recall@}10(q)=6/10$.

**Câu (b).** Ba điểm ngoài các danh sách mở thiếu vì không thuộc $S$ (Kết luận (b)); một điểm thiếu vì $\widetilde d\ne d$ xếp nó sau 10 điểm khác.

**Câu (c).** 20 ứng viên đầu chứa 7 hàng xóm thật (6 điểm đã trả và điểm hạng 14). Theo Mệnh đề 07.7(d) áp dụng cho $S$ là 20 ứng viên và $\widetilde d=d$, cả 7 điểm có mặt trong kết quả; độ thu hồi thành $7/10$.

**Câu (d).** Tăng $\mathit{nprobe}$ để các danh sách chứa 3 điểm đó được mở; xếp hạng lại không giúp, vì theo Mệnh đề 07.7(b) điểm ngoài $S$ luôn thiếu.

**Kiểm tra lại.** Hai cách sửa tác động lên hai thừa số khác nhau: tăng $\mathit{nprobe}$ tăng $n_c$, xếp hạng lại thêm 20 phép đo đúng, mỗi phép $\Theta(D)$ cộng một lần đọc véc-tơ gốc.
:::

Như vậy, tệp đảo chọn $S$ bằng một lượng tử hóa thô (Định nghĩa 07.34), phần dư cho phép chấm bằng bảng tra với cùng cận sai số (Mệnh đề 07.35), và Thuật toán 07.36 giảm đồng thời $n_c$ và chi phí một phép đo; với kho mở đầu, mô hình chi phí cho khoảng $3{,}6$ ms và $5{,}2$ TB (Ví dụ 07.20). Hai điều kiện còn để ngỏ là danh sách có cân bằng hay không và $\mathit{nprobe}$ bao nhiêu thì đủ độ thu hồi. Trong Mục 6, chúng ta đặt bốn cấu trúc trên cùng kho để chọn theo ngân sách; độ lệch danh sách được đo trên dữ liệu tổng hợp của sổ thực hành ở Tình huống 07.2.

<!-- note-topic-id: lec-07-topic-06 -->
## 6. So sánh bốn cấu trúc và chọn chỉ mục

Bảng sau thay số cho kho mở đầu ($N=10^{10}$, $D=3072$) với các tham số đã dùng: $M=16$ cho HNSW (Ví dụ 07.10); $m=512$, $k^*=256$ cho lượng tử hóa tích (Ví dụ 07.16); $k_c=10^5$, $\mathit{nprobe}=64$ cho IVF-PQ (Ví dụ 07.20). Với LSH, $b$ là số bảng và mỗi bảng lưu một mã định danh 8 byte cho mỗi véc-tơ.

| Cấu trúc | Thừa số giảm | Bảo đảm | Byte mỗi véc-tơ | Một truy vấn | Tham số |
|---|---|---|---|---|---|
| LSH | $n_c$ | véc-tơ có $d\le d_1$ vào $S$ với xác suất ít nhất $1-(1-p_1^r)^b$ (Mệnh đề 06.26) | $12\,288+8b$ | $n_c\cdot D$ lượt tọa độ, cộng tính $br$ giá trị băm của $q$ | $b$, $r$, họ băm |
| HNSW | $n_c$ | đúng trên các đỉnh đã thấy (Hệ quả 07.18); $O(\log N)$ phép đo dưới ba giả thiết (Mệnh đề 07.21) | $\approx12\,553$ | $\lvert V\rvert\cdot D$ lượt tọa độ | $M$, $\mathit{efConstruction}$, $\mathit{efSearch}$ |
| PQ quét đủ | chi phí một phép đo | $|d-\widetilde d|\le\|y-\widehat y\|$ (Mệnh đề 07.31) | 512 | $5{,}12\cdot10^{12}$ lần tra | $m$, $k^*$ |
| IVF-PQ | cả hai | như PQ trên $S$; thiếu điểm ở danh sách không mở | 520 | $\approx3{,}63\cdot10^9$ thao tác khi cân bằng | $k_c$, $\mathit{nprobe}$, $m$, $k^*$ |

Trong bảng, bộ nhớ và số thao tác được tính theo mô hình đếm; độ thu hồi không có mặt vì nó phụ thuộc dữ liệu và phải đo trên cùng tập truy vấn, cùng $K$ và cùng phần cứng (Nhận xét 07.6). Quyết định chỉ có nghĩa khi đã nêu ngân sách bộ nhớ, ngân sách độ trễ và ngưỡng độ thu hồi. Tình huống 07.1 kiểm hai ngân sách bộ nhớ và độ trễ, rồi chọn $\mathit{nprobe}$ theo ngưỡng độ thu hồi đo trên $Q$.

::: exercise Bài tập 07.14 (IVF-PQ trong 3 TB)
Kho mở đầu có $N=10^{10}$ véc-tơ $D=3072$ chiều; IVF-PQ dùng $k^*=256$ (1 byte mỗi đoạn), mã định danh 8 byte, $k_c=10^5$, $\mathit{nprobe}=64$, danh sách cân bằng. Ngân sách cho các danh sách là 3 TB.

- (a) Tìm số đoạn $m$ lớn nhất với $m\mid3072$ để các danh sách vừa ngân sách.
- (b) Với $m$ đó, tính dung lượng các danh sách và số thao tác của một truy vấn theo Mệnh đề 07.37; giả sử máy xử lý $10^{12}$ thao tác mỗi giây.
:::

::: hint
Mỗi phần tử danh sách chiếm $m+8$ byte; các ước của $3072=2^{10}\cdot3$ có dạng $2^a$ hoặc $3\cdot2^a$.
:::

::: solution
**Câu (a).** $(m+8)\cdot10^{10}\le3\cdot10^{12}$ cho $m\le292$. Các ước của 3072 gần 292 là 256 và 384, còn $3\cdot2^6=192$; ước lớn nhất không vượt 292 là $m=256$, mỗi đoạn 12 chiều.

**Câu (b).** Dung lượng $(256+8)\cdot10^{10}=2{,}64$ TB. Thao tác: $3{,}07\cdot10^8+5{,}03\cdot10^7+6{,}4\cdot10^6\cdot256\approx3{,}07\cdot10^8+5{,}03\cdot10^7+1{,}64\cdot10^9\approx2{,}0\cdot10^9$, tức $\approx2{,}0$ ms.

**Kiểm tra lại.** Hai số hạng đầu không phụ thuộc $m$; số hạng chấm mã giảm đúng một nửa so với Ví dụ 07.20 vì $m$ giảm từ 512 xuống 256. Đổi lại, mỗi đoạn 12 chiều chỉ có 256 tâm, gấp đôi số chiều mỗi đoạn của Ví dụ 07.20, nên độ thu hồi phải đo lại.
:::

Như vậy, LSH và HNSW giảm số véc-tơ được đo nhưng giữ véc-tơ gốc, lượng tử hóa tích nén véc-tơ nhưng vẫn quét đủ, còn IVF-PQ làm cả hai và trả giá bằng hai nguồn thiếu điểm. Khi chỉ mục không vừa bộ nhớ trong, chi phí đọc dữ liệu từ đĩa thành thừa số thứ ba của chi phí truy vấn.

<!-- note-topic-id: lec-07-topic-07 -->
<!-- note-collapsed -->
## Đọc thêm: Chọn lân cận đa dạng

Thuật toán 07.20 nối điểm mới với $M$ đỉnh gần nó nhất. Khi các đỉnh gần nhất cùng nằm một phía, các cạnh mới cùng chỉ một hướng, và một cụm điểm có thể mất liên kết với cụm bên cạnh. Bài báo HNSW đề xuất một quy tắc chọn khác (Thuật toán 4, tr.5).

::: algorithm Thuật toán 07.39 (Chọn lân cận theo quy tắc đa dạng)
**Đầu vào.** Điểm $x$; tập ứng viên $W$; số nguyên $M\ge1$.

**Đầu ra.** Tập $\mathcal R\subseteq W$ gồm tối đa $M$ lân cận.

1. Đặt $\mathcal R\leftarrow\varnothing$; xét các $y\in W$ theo $d(y,x)$ tăng dần.
2. Nhận $y$ vào $\mathcal R$ khi $d(y,x)<d(y,u)$ với mọi $u\in\mathcal R$; dừng khi $|\mathcal R|=M$.
3. Trả $\mathcal R$.

**Dừng.** Sau nhiều nhất $|W|$ lượt.

**Trường hợp biên.** Ứng viên đầu tiên luôn được nhận; $\mathcal R$ có thể có ít hơn $M$ phần tử.

**Chi phí.** Sắp $W$ tốn $O(|W|\log|W|)$; mỗi ứng viên so với nhiều nhất $M$ phần tử của $\mathcal R$, tổng $O(|W|M)$ khoảng cách, mỗi khoảng cách $\Theta(D)$.
:::

Một ứng viên gần một lân cận đã chọn hơn gần $x$ thì cạnh tới nó không mở thêm hướng mới, nên bị loại. Quy tắc thay bước "chọn $M$ đỉnh gần nhất" ở bước 4 của Thuật toán 07.20 và cũng dùng khi cắt bậc. Quy tắc Prune của DiskANN (bài giảng 9, tr.24) bỏ ứng viên $y$ khi có $u\in\mathcal R$ với $d(u,y)<d(x,y)/\alpha$; với $\alpha=1$, hai quy tắc chỉ khác nhau khi có hòa khoảng cách.

::: example Ví dụ 07.21 (Hai lân cận cho $x=(0;\ 0)$)
**Dữ kiện.** $x=(0;\ 0)$, $M=2$, bốn ứng viên $v_1=(2;\ 0{,}3)$, $v_2=(2{,}6;\ 0{,}9)$, $v_3=(2{,}4;\ -0{,}6)$, $v_4=(-3;\ 0{,}5)$.

**Thứ tự.** $d(v_1,x)\approx2{,}02$, $d(v_3,x)\approx2{,}47$, $d(v_2,x)\approx2{,}75$, $d(v_4,x)\approx3{,}04$.

**Chọn.** Nhận $v_1$. Loại $v_3$ vì $d(v_3,v_1)\approx0{,}98<2{,}47$. Loại $v_2$ vì $d(v_2,v_1)\approx0{,}85<2{,}75$. Nhận $v_4$ vì $d(v_4,v_1)\approx5{,}00>3{,}04$.

**Kiểm tra lại.** Quy tắc cho $\{v_1,v_4\}$ ở hai phía của $x$; chọn hai đỉnh gần nhất cho $\{v_1,v_3\}$ cùng một phía.
:::

![Điểm mới x có bốn ứng viên: v1, v2, v3 cùng một phía, v4 ở phía đối diện; chọn hai đỉnh gần nhất cho v1 và v3 cùng phía; quy tắc đa dạng cho v1 và v4 ở hai phía.](img/lec-07/note-lan-can-da-dang.svg)

Trên hình, ở khung trái, hai đỉnh gần nhất $v_1$, $v_3$ nằm cùng một phía của $x$; ở khung phải, quy tắc đa dạng giữ $v_1$ và $v_4$ ở hai phía.

<!-- note-topic-id: lec-07-topic-08 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 07.1 (Truy hồi ngữ nghĩa trên mười tỷ véc-tơ với 6 TB và 10 ms; BIODS 271, tr.16–18)
**Bài toán và dữ liệu.** Kho truy hồi ngữ nghĩa có $N=10^{10}$ véc-tơ nhúng $D=3072$ chiều, mỗi thành phần 4 byte (BIODS 271, tr.17). Giả sử máy chủ có 6 TB bộ nhớ trong, mỗi truy vấn được 10 ms, máy xử lý $10^{12}$ thao tác mỗi giây, và ứng dụng cần $K=10$ đoạn văn bản.

**Mô hình hóa.** Bài toán tìm gần đúng của Định nghĩa 07.1; chất lượng đo bằng $\overline{\operatorname{recall@}10}$ (Định nghĩa 07.4) trên một tập truy vấn đại diện $Q$.

**Kiểm giả thiết.** Mệnh đề 07.37(b) cần danh sách cân bằng; trên dữ liệu tổng hợp của sổ thực hành, giả thiết này không thỏa (Tình huống 07.2), nên cỡ các danh sách được mở phải đo trên kho của tình huống này trước khi dùng con số $3{,}6$ ms.

**Áp dụng.** LSH và HNSW lưu véc-tơ gốc nên cần hơn $122{,}88$ TB; HNSW cần $\approx125{,}5$ TB (Ví dụ 07.10). Cả hai vượt 6 TB. Quét đủ mã PQ vừa bộ nhớ với $5{,}12$ TB nhưng cần $5{,}12$ s (Ví dụ 07.16), vượt 10 ms. IVF-PQ với $k_c=10^5$, $\mathit{nprobe}=64$ cần $\approx5{,}2$ TB cộng $1{,}23$ GB tâm thô và $\approx3{,}6$ ms (Ví dụ 07.20).

**Chi phí.** Mỗi truy vấn đọc $\approx3{,}33$ GB, tức băng thông khoảng $0{,}92$ TB/s (Ví dụ 07.20).

**Diễn giải.** Trong bốn cấu trúc, chỉ IVF-PQ thỏa cả hai ngân sách theo mô hình đếm.

**Giới hạn.** Giá trị $\mathit{nprobe}$ chưa xác định được khi chưa có ngưỡng độ thu hồi: phải đo $\overline{\operatorname{recall@}10}$ trên $Q$ với vài giá trị $\mathit{nprobe}$ rồi chọn giá trị nhỏ nhất đạt ngưỡng. Nếu không đạt, phải tăng $m$ (thêm bộ nhớ) hoặc xếp hạng lại bằng véc-tơ gốc trên đĩa (thêm thời gian đọc), theo hai nguồn thiếu điểm của Mệnh đề 07.7.
:::

::: application Tình huống 07.2 (Tệp đảo trên dữ liệu tổng hợp với danh sách không cân bằng; sổ thực hành của bài giảng 8, ô mã 2–38)
**Bài toán và dữ liệu.** Sổ thực hành tạo dữ liệu tổng hợp 64 chiều gồm $10^6$ véc-tơ huấn luyện, kho $N=10^4$ véc-tơ và 100 truy vấn (ô mã 2). Ô mã 6–7 học $k_c=4096$ tâm bằng k-means trên tập huấn luyện; ô mã 27–28 gán mỗi véc-tơ của kho vào danh sách của tâm gần nhất; ô mã 35 mở $\mathit{nprobe}=13$ danh sách cho mỗi truy vấn và đếm số khoảng cách tới véc-tơ kho.

**Mô hình hóa.** Tệp đảo của Định nghĩa 07.34 với $\widetilde d=d$; chi phí quét theo Mệnh đề 07.37.

**Kiểm giả thiết.** Cỡ danh sách trung bình $10^4/4096\approx2{,}44$ không là số nguyên, nên các danh sách không thể cùng cỡ $N/k_c$ và giả thiết của Mệnh đề 07.37(b) không thỏa.

**Áp dụng.** Mệnh đề 07.37(b) dự đoán $13\cdot10^4/4096\approx31{,}7$ khoảng cách mỗi truy vấn. Ô mã 38 ghi trung bình 106 khoảng cách mỗi truy vấn, gấp $\approx3{,}3$ lần. Mỗi danh sách được mở chứa trung bình $106/13\approx8{,}2$ véc-tơ, so với cỡ trung bình $2{,}44$ của mọi danh sách.

**Chi phí.** Theo Mệnh đề 07.37(a), chọn tâm thô cần $4096$ khoảng cách; cộng 106 khoảng cách quét được $4202$, chỉ ít hơn quét đủ $10^4$ khoảng $2{,}4$ lần.

**Diễn giải.** Công thức $\mathit{nprobe}\,N/k_c$ đánh giá thấp chi phí quét $3{,}3$ lần vì các danh sách được mở lớn hơn danh sách trung bình.

**Giới hạn.** Chỉ dùng $\mathit{nprobe}\,N/k_c$ sau khi đã đo cỡ các danh sách được mở trên một tập truy vấn đại diện.
:::

Tình huống 07.2 cho thấy giả thiết cân bằng của Mệnh đề 07.37(b) quyết định độ chính xác của dự đoán chi phí, còn Mệnh đề 07.37(a) đúng với mọi cỡ danh sách.

**Ứng dụng trong các bài sau và hệ thống.**

- Faiss `IndexIVFPQ` và ScaNN dựa trên cấu trúc IVF-PQ của Mục 5, và tìm tâm thô bằng chính một chỉ mục gần đúng (bài giảng 8, tr.56).
- DiskANN giữ véc-tơ nén khoảng 32 byte trong bộ nhớ trong và đồ thị bậc khoảng 100 trên SSD (bài giảng 9, tr.35).
- Bài 12 đo chi phí bằng số lần đọc khối khi dữ liệu không vừa bộ nhớ trong; đó là thừa số còn thiếu trong mô hình đếm của Ví dụ 07.20.
- Bài 14 dùng danh sách đảo cho chỉ mục văn bản và chỉ mục không gian cho truy vấn hàng xóm chính xác ở số chiều thấp.

<!-- note-topic-id: lec-07-topic-09 -->
## Tóm tắt chương

Câu hỏi xuất phát của chương là tìm $K$ hàng xóm của một truy vấn trong kho $10^{10}$ véc-tơ $3072$ chiều với 6 TB bộ nhớ trong và 10 ms mỗi truy vấn, khi kho gốc chiếm $122{,}88$ TB và quét đầy đủ cần $30{,}72$ giây (Mệnh đề 07.3). Chúng ta nới bài toán thành tìm gần đúng (Định nghĩa 07.1), đo chất lượng bằng độ thu hồi (Định nghĩa 07.4) và tách chi phí thành số véc-tơ được đo nhân chi phí một phép đo, cùng hai nguồn thiếu điểm (Mệnh đề 07.7). Đồ thị lân cận giảm thừa số thứ nhất: tham lam dừng ở cực tiểu cục bộ (Mệnh đề 07.11), `SEARCH-LAYER` đúng trên các đỉnh đã thấy (Mệnh đề 07.13), và HNSW xếp các đồ thị thành tầng với phân phối hình học (Mệnh đề 07.19) để số phép đo tăng theo $\log N$ dưới ba giả thiết (Mệnh đề 07.21). Lượng tử hóa tích giảm thừa số thứ hai và bộ nhớ (Mệnh đề 07.28), tính khoảng cách bằng bảng tra (Mệnh đề 07.30) với sai lệch không vượt khoảng cách $\|y-\widehat y\|$ tới véc-tơ tái dựng (Mệnh đề 07.31), nhưng vẫn quét đủ. IVF-PQ giảm cả hai (Thuật toán 07.36, Mệnh đề 07.37); với khoảng $5{,}2$ TB và $3{,}6$ ms (Ví dụ 07.20), nó là cấu trúc duy nhất của chương vừa 6 TB và 10 ms trong Tình huống 07.1, với điều kiện danh sách cân bằng và $\mathit{nprobe}$ được chọn bằng độ thu hồi đo được. Chi phí đọc dữ liệu khi chỉ mục không vừa bộ nhớ trong để lại cho Bài 12.

**Định nghĩa và kết quả theo mục.**

- Mục 1: tìm đúng, tìm gần đúng, chỉ mục hàng xóm (Định nghĩa 07.1); quét đầy đủ (Thuật toán 07.2, Mệnh đề 07.3); độ thu hồi (Định nghĩa 07.4); recall@R (Nhận xét 07.5); bốn trục (Nhận xét 07.6); hai thừa số, hai nguồn thiếu điểm (Mệnh đề 07.7).
- Mục 2: đồ thị lân cận (Định nghĩa 07.8); tham lam (Thuật toán 07.9); cực tiểu cục bộ (Định nghĩa 07.10, Mệnh đề 07.11); `SEARCH-LAYER` (Thuật toán 07.12, Mệnh đề 07.13, Hệ quả 07.14); bề rộng chùm (Nhận xét 07.15).
- Mục 3: HNSW (Định nghĩa 07.16); truy vấn (Thuật toán 07.17, Hệ quả 07.18); phân phối tầng (Mệnh đề 07.19); chèn (Thuật toán 07.20); số phép đo (Mệnh đề 07.21); bộ nhớ (Mệnh đề 07.22); tham số (Nhận xét 07.23).
- Mục 4: lượng tử hóa véc-tơ (Định nghĩa 07.24, Thuật toán 07.25, Nhận xét 07.26); lượng tử hóa tích (Định nghĩa 07.27, Mệnh đề 07.28); ADC, SDC (Định nghĩa 07.29); bảng tra (Mệnh đề 07.30, Thuật toán 07.32); cận sai số (Mệnh đề 07.31); tham số (Nhận xét 07.33).
- Mục 5: tệp đảo (Định nghĩa 07.34); phần dư (Mệnh đề 07.35); truy vấn IVF-PQ (Thuật toán 07.36); chi phí (Mệnh đề 07.37); tham số (Nhận xét 07.38).
- Đọc thêm: chọn lân cận đa dạng (Thuật toán 07.39).

**Công thức và thuật toán cần nhớ.** Độ thu hồi, phân phối tầng và cận $B$ cho số liên kết kỳ vọng của một điểm HNSW:

$$
\operatorname{recall@}K(q)=\frac{|\widehat{\mathcal N}_K(q)\cap\mathcal N_K(q)|}{K},
$$

$$
\Pr[\ell\ge k]=\rho^k,
$$

$$
B=M_{\max,0}+M_{\max}\frac{\rho}{1-\rho}.
$$

Khoảng cách bất đối xứng, cận sai số và đẳng thức chuyển gốc:

$$
\widetilde d(q,y)^2=\sum_{j=1}^mT[j,i_j(y)],
$$

$$
|d(q,y)-\widetilde d(q,y)|\le\|y-\widehat y\|,
$$

$$
\|q-y\|=\|\widetilde q_i-r(y)\|.
$$

Các thuật toán: quét đầy đủ (Thuật toán 07.2), tham lam (Thuật toán 07.9), `SEARCH-LAYER` (Thuật toán 07.12), truy vấn và chèn HNSW (Thuật toán 07.17, 07.20), quét mã bằng bảng tra (Thuật toán 07.32), truy vấn IVF-PQ (Thuật toán 07.36). Chi phí truy vấn IVF-PQ, với danh sách cân bằng $\sum_{i\in P}|L_i|=\mathit{nprobe}\,N/k_c$:

$$
\begin{aligned}
&\Theta(k_cD)+\Theta(\mathit{nprobe}\,k^*D)\\
&\quad+\Theta\Big(m\sum_{i\in P}|L_i|\Big).
\end{aligned}
$$

**Giả thiết hay bị bỏ quên.**

- Thứ tự $(d,\text{chỉ số})$ phá hòa; bỏ nó, quét đầy đủ có thể trả sai tập và tham lam có thể không dừng (Mệnh đề 07.3, 07.11).
- `SEARCH-LAYER` chỉ đúng trên tập $V$ đã thấy (Ví dụ 07.5).
- Cận $O(\log N)$ của HNSW cần tầng độc lập với vị trí, đồ thị Delaunay chính xác và bậc bị chặn (Mệnh đề 07.21); đồ thị thật chỉ xấp xỉ.
- Phân tích theo đoạn của PQ cần các đoạn phân hoạch tọa độ (Mệnh đề 07.28); cận sai số áp dụng cho khoảng cách, không cho bình phương (Mệnh đề 07.31).
- Phần dư phải chấm bằng truy vấn dư của đúng danh sách chứa nó (Mệnh đề 07.35).
- Công thức $\mathit{nprobe}\,N/k_c$ cần danh sách cân bằng (Mệnh đề 07.37(b), Tình huống 07.2).
- Recall@R của bài báo PQ và của Faiss khác $\operatorname{recall@}K$ khi $K>1$ (Nhận xét 07.5).

<!-- note-topic-id: lec-07-topic-10 -->
## Bài tập củng cố

Bài tập 07.15–07.19 nằm trong [tệp bài tập Bài 07](material-viewer.html?doc=materials/lec-07/exercises.md&deck=lecture-07-chi-muc-hang-xom-gan-dung.html), gồm bài tập của bài giảng 8 và sổ thực hành đi kèm, cùng gợi ý và lời giải.

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Malkov, Yu. A. và Yashunin, D. A. (2020). *Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs*, IEEE Transactions on Pattern Analysis and Machine Intelligence 42(4). Số trang theo bản arXiv 1603.09320 (v4). Thuật toán 1–5, tr.4–5: Thuật toán 07.12, 07.17, 07.20, 07.39. §4.1, tr.5–6: $m_L=1/\ln M$, $M_{\max,0}$ (Mục 3.2). §4.2.1, tr.7: Mệnh đề 07.21. §4.2.3, tr.8: khoảng $M$ 6–48 và mã định danh 4 byte (Nhận xét 07.23).
- Jégou, H., Douze, M. và Schmid, C. (2011). *Product Quantization for Nearest Neighbor Search*, IEEE Transactions on Pattern Analysis and Machine Intelligence 33(1), 117–128. §II, tr.2–4: Mục 4.1–4.2. §III, tr.4–5: Mục 4.3. §IV, tr.6–7: Mục 5. §V-A, tr.8: Nhận xét 07.5 và Bài tập 07.10.
- Liberty, E. và Douze, M. (2023). Princeton COS 597A *Vector Search*, bài giảng 8 *Quantization for lossy vector compression*, tr.2–58, và sổ thực hành `class-08-runbook-for-students.ipynb`: Mục 1.3, 4, 5, Tình huống 07.2 và tệp bài tập.
- Simhadri, H. V. (2023). Princeton COS 597A *Vector Search*, bài giảng 9 *Graph indexes*, tr.2–35: Mục 2, 3, Nhận xét 07.38 và phần ứng dụng.
- Stanford BIODS 271 (2025), bài 12 (tệp L12, tiêu đề trang bìa *Improving LLM Performance*), tr.16–18: Mục 1, Ví dụ 07.14, Tình huống 07.1.
- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, Chương 3, qua các kết quả LSH của Bài 06 nhắc lại ở phần kiến thức tiên quyết, Mục 1 và Mục 6. Sách và bộ trang chiếu của các tác giả tại [http://www.mmds.org](http://www.mmds.org).
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press, §2.1 (bất biến vòng lặp) và §6.5 (hàng đợi ưu tiên): chứng minh Mệnh đề 07.3 và 07.13.
- Ghi chú Bài 01: Định nghĩa 01.2, 01.8, 01.17; Mệnh đề 01.16. Ghi chú Bài 06: Định nghĩa 06.14, 06.22; Định lý 06.36; Mệnh đề 06.26; Nhận xét 06.27.
