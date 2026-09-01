# Biểu diễn tương đồng: Shingling và MinHash

Xem bộ slide tại [Bài 05 — Biểu diễn tương đồng: Shingling và MinHash](lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html). Ghi chú phát triển các đặc tả, ví dụ và lập luận để có thể đọc độc lập.

## Mục tiêu và kiến thức tiên quyết

Sau bài này, người học có thể:

- Chuyển một tài liệu đã chuẩn hóa thành tập $k$-shingle $S_k(D)$ và xử lý đúng trường hợp $k>n$.
- Tính độ tương đồng Jaccard bằng giao–hợp và bằng thuật toán hai con trỏ trên danh sách đã sắp, kể cả quy ước khi hợp rỗng.
- Đặc tả MinHash lý tưởng $h_\pi$ trên vũ trụ hữu hạn, chạy tay Ví dụ 3.7 và chứng minh xác suất trùng bằng Jaccard dưới hoán vị đều.
- Dùng biến chỉ báo để suy kỳ vọng, tính không chệch và phương sai của ước lượng Jaccard từ chữ ký $p$ hàng.
- Lập chữ ký bằng một lượt quét ma trận thưa, phân tích chi phí và bộ nhớ.
- Phân biệt bảo đảm của hoán vị lý tưởng với hàm băm thực hành có va chạm hoặc không được lấy độc lập và đều.

Kiến thức tiên quyết: tập hợp, giao–hợp, hàm băm, biến chỉ báo Bernoulli, kỳ vọng, phương sai, tính độc lập và ma trận thưa 0/1. Ý nghĩa của từng khái niệm được nhắc ngắn trước lần dùng quyết định.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N$ | số tài liệu |
| $D_i$ | tài liệu thứ $i$ |
| $k$ | độ dài shingle |
| $C_i=S_k(D_i)$ | tập shingle của $D_i$ |
| $U$, $u=|U|$ | vũ trụ hữu hạn của shingle, số hàng |
| $A$ | ma trận đặc trưng thưa |
| $p$ | số hàng chữ ký |
| $z$ | số phần tử 1 của $A$ |
| $\pi$, $h_\pi$ | hoán vị hàng và MinHash lý tưởng |
| $SIG$ | ma trận chữ ký $p\times N$; mỗi ô thuộc $\{0,\ldots,u-1\}\cup\{\infty\}$ |

## 1. Quy mô so sánh cặp và vai trò của biểu diễn

Một kho gồm $N$ tài liệu cần so sánh từng cặp để tìm bản gần trùng. Số cặp tăng theo $N^2$, trong khi mỗi tài liệu có thể rất lớn.

::: example Ví dụ quy mô
Với $N=10^6$ tài liệu, số cặp là

$$\binom N2=\frac{N(N-1)}2=499\,999\,500\,000.$$

Ngay cả khi xử lý được một triệu cặp mỗi giây, riêng lượt quét này vẫn kéo dài gần sáu ngày. Nguồn: slide MMDS Chương 3, trang 24; Stanford CS246 `03-lsh.pdf`, trang 14.
:::

Trước khi giảm số cặp, ta cần một đại diện nhỏ hơn cho mỗi tài liệu mà vẫn giữ thông tin về độ tương đồng từ vựng. Luồng biểu diễn là

$$D_i\to C_i=S_k(D_i)\to\sigma(C_i).$$

Bước $D_i\to C_i$ (shingling) và bước $C_i\to\sigma(C_i)$ (chữ ký MinHash) làm giảm kích thước mỗi tài liệu; chúng không làm giảm số lượng cặp $\binom N2$. Việc giảm số cặp thuộc về một bước khác (LSH) nằm ngoài phạm vi bài này.

::: exercise Tự kiểm
Nếu số tài liệu tăng từ $N$ lên $2N$, số cặp tăng xấp xỉ bao nhiêu lần khi $N$ lớn?
:::

::: solution
Từ $N(N-1)/2$ lên $2N(2N-1)/2$; tỷ số tiến tới $4$ khi $N$ lớn.
:::

## 2. Shingling: chuyển tài liệu thành tập shingle

### Đặc tả $k$-shingle
Một tài liệu là một chuỗi ký tự. Cho tài liệu $D$ đã chuẩn hóa, dài $n$; chọn $k\ge1$. Một $k$-shingle là một chuỗi con độ dài $k$ xuất hiện trong $D$. Tập shingle của $D$ là

$$S_k(D)=\{ D[i:i+k] \mid 0\le i\le n-k\},\quad k\le n,$$

và $S_k(D)=\varnothing$ khi $k>n$. Chỉ số dùng miền nửa mở $[0,n)$; tập chỉ giữ một bản sao của mỗi chuỗi con.

Quy tắc chuẩn hóa quyết định chuỗi đầu vào trước khi quét cửa sổ. Có thể thay một dãy khoảng trắng bằng một dấu cách để giữ biên từ, hoặc loại bỏ toàn bộ khoảng trắng; toàn bộ kho phải dùng cùng một quy tắc. Với $k=9$, chuỗi `touch down` giữ khoảng trắng có hai shingle `touch dow` và `ouch down`, còn `touchdown` có shingle `touchdown`. Nếu xóa khoảng trắng, hai biểu diễn này trùng nhau. Nguồn: MMDS Ví dụ 3.4, §3.2.1.

::: example Ví dụ 3.3: quét cửa sổ dài hai
Chuỗi $D=\texttt{abcdabd}$, $k=2$. Quét sáu cửa sổ: $\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da},\texttt{ab},\texttt{bd}$. Tập kết quả:

$$S_2(D)=\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da},\texttt{bd}\}.$$

Đoạn $\texttt{ab}$ xuất hiện hai lần nhưng chỉ đếm một thành viên của tập. Nguồn: MMDS Ví dụ 3.3, §3.2.1.
:::

Hình dưới minh họa phép quét cửa sổ dài hai trên chuỗi `abcdabd` trong MMDS Ví dụ 3.3.

![Chuỗi abcdabd tạo tập 2-shingle gồm ab, bc, cd, da và bd.](img/lec-05/cua-so-shingle.svg)

::: derivation Lập luận đúng của phép quét
Thuật toán quét một lượt:

```text
đầu vào: D[0..n-1], k>=1
C <- tập rỗng
nếu k > n thì trả C
cho i = 0,...,n-k:
  thêm D[i:i+k] vào C
trả C
```

Bất biến: trước mỗi vòng $i$, $C$ chứa đúng các shingle bắt đầu trước $i$. Sau $n-k+1$ cửa sổ, mọi vị trí hợp lệ đã được xét nên thuật toán dừng và trả $S_k(D)$.
:::

Nếu $k\le n$, tạo hoặc băm trực tiếp từng cửa sổ tốn $\Theta(k)$, nên tổng thời gian là $\Theta(k(n-k+1))$. Cận này giả sử đọc hoặc tạo một xâu con tốn $\Theta(k)$ và phép thêm vào tập không chi phối chi phí đó.

Băm lăn có thể giảm thời gian cập nhật mã của mỗi cửa sổ, nhưng không làm giảm $k$ hay số cửa sổ cần quét. Nó còn đưa thêm rủi ro va chạm, nên không được đồng nhất với cách tạo shingle trực tiếp.

### 2.1 Chọn $k$ để shingle đủ phân biệt
$k$ phải đủ lớn để xác suất một shingle bất kỳ xuất hiện trong một tài liệu cho trước là thấp. Nếu $k$ quá nhỏ (ví dụ $k=1$), hầu hết tài liệu chia sẻ nhiều shingle và mọi cặp đạt tương đồng cao. MMDS đề xuất $k=5$ cho email và $k=9$ cho tài liệu dài trong mô hình chữ tiếng Anh; đó là gợi ý, không phải hằng số phổ quát. Nguồn: MMDS §3.2.2.

Băm shingle không đồng nghĩa giảm $k$. Băm một xâu dài $k$ về một số nguyên giúp nén biểu diễn (giảm bộ nhớ) nhưng không làm tăng sức phân biệt; ngược lại, shingle dài phân biệt tốt hơn trước khi băm so với shingle ngắn cùng kích thước lưu. Nếu băm thẳng, va chạm có thể nhập hai shingle thành một phần tử.

| | Đoạn dài | Mã gọn |
|---|---|---|
| Ý tưởng | Tạo $k$-shingle để có sức phân biệt | Băm shingle về số nguyên gọn |
| Rủi ro | số cửa sổ và bộ nhớ | va chạm nhập hai shingle |

::: exercise Tự kiểm
Với $D=\texttt{abcdabd}$ và $k=7$, tập $S_k(D)$ có bao nhiêu phần tử? Điều gì xảy ra khi $k=8$?
:::

::: solution
Khi $k=7$, chỉ có một cửa sổ nên $S_7(D)=\{\texttt{abcdabd}\}$. Khi $k=8>n$, tập shingle rỗng.
:::

## 3. Độ tương đồng Jaccard

Cho hai tập shingle $C_1,C_2\neq\varnothing$, độ tương đồng Jaccard là tỷ lệ phần tử chung trên phần tử xuất hiện ở ít nhất một tập:

$$J(C_1,C_2)=\frac{|C_1\cap C_2|}{|C_1\cup C_2|}=\frac{x}{x+y},$$

trong đó $x=|C_1\cap C_2|$ và $y=|C_1\triangle C_2|$ là số phần tử thuộc đúng một tập. Nguồn: MMDS §3.1.1.

::: example Ví dụ 3.1
Cho hai tập $S,T$ với ba phần tử trong giao và tám phần tử xuất hiện ở ít nhất một tập. Khi đó

$$J(S,T)=3/8.$$

Hình dưới thể hiện ba loại hàng X, Y, Z: hàng X có số 1 ở cả hai cột, hàng Y có đúng một số 1, hàng Z có hai số 0.
:::

![Hai tập chia thành vùng giao X, vùng chỉ thuộc một tập Y và vùng ngoài Z.](img/lec-05/jaccard-ba-vung.svg)

Hàng loại Z không ảnh hưởng tới tỷ lệ; Jaccard chỉ phụ thuộc các hàng loại X và Y, tức $x/(x+y)$.

### 3.1 Quy ước hợp rỗng
$J$ chỉ định nghĩa khi $C_1\cup C_2\neq\varnothing$. Khi cả hai tập rỗng (có thể xảy ra với tài liệu ngắn hơn $k$), học phần quy ước trả "không xác định" thay vì chia cho 0. Tập rỗng không có MinHash hữu hạn và không được dùng để ước lượng. Ta có $0\le J\le1$; $J=1$ đúng khi $C_1=C_2\neq\varnothing$; $J=0$ khi hai tập rời nhau và có ít nhất một tập không rỗng.

### 3.2 Thuật toán hai con trỏ trên danh sách đã sắp
Giả sử $C_1,C_2$ là danh sách sắp tăng dần, không lặp. Duyệt đồng thời hai danh sách bằng hai con trỏ.

```text
đầu vào: C1,C2 tăng dần, không lặp
(i,j,giao,hợp) <- (0,0,0,0)
trong khi i<|C1| và j<|C2|:
  nếu C1[i]=C2[j]: tăng i,j,giao,hợp
  ngược lại nếu C1[i]<C2[j]: tăng i,hợp
  ngược lại: tăng j,hợp
cộng phần tử còn lại vào hợp
trả giao/hợp nếu hợp>0; nếu không, trả "không xác định"
```

Ba nhánh loại trừ nhau nên mỗi vòng chỉ cập nhật đúng một trường hợp. Bất biến: các biến mô tả đúng hai tiền tố đã xử lý. Mỗi vòng tăng ít nhất một chỉ số nên thuật toán dừng. Nếu hợp rỗng, trả "không xác định", không chia cho 0. Thời gian trường hợp xấu nhất $\Theta(|C_1|+|C_2|)$, bộ nhớ phụ $O(1)$. Mỗi phép so sánh một cặp danh sách tốn thời gian tuyến tính; nhân với $\binom N2$ cặp vẫn quá tải với dữ liệu lớn.

::: exercise Tự kiểm
Tính $J(\varnothing,\{a\})$ và nêu kết quả của học phần cho $J(\varnothing,\varnothing)$.
:::

::: solution
$J(\varnothing,\{a\})=0$ vì giao rỗng và hợp có một phần tử. $J(\varnothing,\varnothing)$ được trả là “không xác định”.
:::

## 4. MinHash lý tưởng

Vì so một cặp trên hai tập shingle vẫn tốn thời gian tuyến tính, ta thay mỗi tập bằng một chữ ký ngắn. Chữ ký MinHash lý tưởng dựa trên một hoán vị đều của vũ trụ. Nguồn: MMDS §§3.3.1–3.3.3.

### 4.1 Ma trận đặc trưng là mô hình
Một vũ trụ hữu hạn $U$, $u=|U|$, được biểu diễn thành ma trận $A$: mỗi hàng ứng với một phần tử của $U$, mỗi cột ứng với một tập $C_j$. Ô $(r,j)=1$ khi hàng $r\in C_j$, nếu không là 0. Ma trận thường rất thưa nên triển khai lưu vị trí của các số 1 thay vì lưu ma trận đặc. Hình quy-mo-so-sanh-cap thể hiện chuỗi biểu diễn từ tài liệu đến chữ ký.

![Một triệu tài liệu tạo xấp xỉ năm trăm tỷ cặp, cần shingle và MinHash.](img/lec-05/quy-mo-so-sanh-cap.svg)

### 4.2 Đặc tả $h_\pi$
Cho hoán vị $\pi$ của $U$ và tập không rỗng $C\subseteq U$. MinHash của $C$ là phần tử của $C$ xuất hiện sớm nhất trong thứ tự $\pi$:

$$h_\pi(C)=\arg\min_{r\in C}\pi(r).$$

Điều kiện trước: $\varnothing\neq C\subseteq U$; $\pi$ là hoán vị của $U$. Tập rỗng không có MinHash hữu hạn. Mỗi ô của chữ ký thuộc $\{0,\ldots,u-1\}\cup\{\infty\}$; giá trị canh $\infty$ dùng cho cột rỗng.

### 4.3 Ví dụ 3.7: thứ tự $b,e,a,d,c$
Xét bốn tập trên $\{a,b,c,d,e\}$: $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$, $S_4=\{a,c,d\}$. Với hoán vị $b,e,a,d,c$, quét từ trên xuống:

- $S_3$ gặp số 1 đầu tiên ở $b$,
- $S_1,S_4$ gặp số 1 ở $a$,
- $S_2$ gặp số 1 ở $c$.

Vậy $h_\pi(S_1)=a$, $h_\pi(S_2)=c$, $h_\pi(S_3)=b$, $h_\pi(S_4)=a$. Dữ kiện bốn tập lấy từ MMDS Hình 3.2; phép quét theo hoán vị được trình bày ở Hình 3.3 và Ví dụ 3.7, §3.3.2.

![Ma trận quét theo b,e,a,d,c cho MinHash lần lượt a,c,b,a.](img/lec-05/minhash-hoan-vi.svg)

Điểm quyết định là phần tử xuất hiện đầu tiên trong hợp của hai tập. Nếu phần tử ấy thuộc cả hai tập, hai MinHash trùng; nếu nó chỉ thuộc một tập, hai MinHash khác nhau. Các hàng nằm ngoài hợp không thể trở thành MinHash và được bỏ khỏi lập luận.

### 4.4 Mệnh đề bảo toàn xác suất
Cho $C_1,C_2\neq\varnothing$. Nếu $\pi$ được chọn đều trên mọi hoán vị của $U$, thì

$$\Pr_\pi[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2).$$

::: proof Chứng minh
Chỉ xét hai cột tương ứng với $C_1,C_2$. Mỗi hàng thuộc một trong ba loại:

1. X: có 1 ở cả hai cột.
2. Y: có đúng một số 1.
3. Z: hai số 0.

Gọi $x,y$ lần lượt là số hàng loại X, Y. Vì $\pi$ đều, phần tử đầu tiên trong hợp $C_1\cup C_2$ (sau khi bỏ các hàng Z) phân bố đều, nên xác suất hàng đầu thuộc X là $x/(x+y)$.

Nếu hàng đầu thuộc X thì cả hai cột cùng gặp số 1 đầu tiên ở cùng hàng, vì vậy $h_\pi(C_1)=h_\pi(C_2)$: trùng. Nếu hàng đầu thuộc Y thì đúng một cột gặp số 1 và cột kia phải đi tiếp xuống, nên hai MinHash khác nhau. Vậy

$$\Pr[h_\pi(C_1)=h_\pi(C_2)]=\frac{x}{x+y}=J(C_1,C_2).$$

Giả thiết "đều" là quyết định; kết luận không chuyển tự động sang một hàm băm ngẫu nhiên bất kỳ.
:::

::: exercise Tự kiểm
Hai tập khác rỗng và rời nhau có thể nhận cùng MinHash dưới một hoán vị thật hay không?
:::

::: solution
Không. MinHash trả một phần tử của mỗi tập; hai tập rời nhau không có phần tử chung để hai kết quả bằng nhau.
:::

## 5. Chữ ký MinHash: kỳ vọng và phương sai

Từ một phép thử MinHash, ta ghép $p$ phép thử độc lập, mỗi phép dùng một hoán vị đều $\pi_1,\ldots,\pi_p$. Chữ ký của $C$ là

$$\sigma(C)=[ h_{\pi_1}(C),\ldots,h_{\pi_p}(C)]^T.$$

::: example Tỷ lệ hàng trùng là một ước lượng
Trong Ví dụ 3.8, với $p=2$, hai cột $S_1$ và $S_4$ đều có chữ ký $(1,0)^T$. Tỷ lệ hàng trùng là $2/2=1$, trong khi Jaccard thật bằng $2/3$. Ví dụ nhỏ này cho thấy ước lượng không chệch vẫn có thể lệch nhiều ở một lần lấy mẫu khi $p$ nhỏ.
:::

Với mỗi cặp $C_1,C_2$, định nghĩa biến chỉ báo $X_i=\mathbf 1[h_{\pi_i}(C_1)=h_{\pi_i}(C_2)]$ và tổng số hàng trùng $X=\sum_{i=1}^p X_i$.

::: derivation Suy dẫn kỳ vọng và phương sai
Các $X_i$ độc lập vì $\pi_i$ độc lập; mỗi $X_i$ là Bernoulli với $\Pr[X_i=1]=J$. Kỳ vọng số hàng trùng:

$$\mathbb E\left[\sum_i X_i\right]=\sum_i\mathbb E[X_i]=pJ.$$

Tỷ lệ hàng trùng $\hat J=X/p$ có kỳ vọng:

$$\mathbb E[\hat J]=\frac1p\mathbb E[X]=\frac{pJ}{p}=J,$$

nên $\hat J$ không chệch. Do độc lập,

$$\operatorname{Var}(\hat J)=\frac1{p^2}\sum_i\operatorname{Var}(X_i)=\frac{J(1-J)}p\le\frac1{4p}.$$

Cận cuối từ $J(1-J)\le1/4$. Độc lập cần thiết cho phương sai; tuyến tính kỳ vọng không cần độc lập.
:::

Tăng $p$ giảm phương sai nhưng làm thời gian cập nhật và bộ nhớ tăng tuyến tính. Kết luận này chỉ áp dụng cho mô hình lý tưởng với các $\pi_i$ độc lập và đều. Không áp dụng cận phương sai cho một bộ hàm thiếu một trong hai giả thiết nếu chưa có chứng minh riêng.

::: exercise Tự kiểm
Nếu tăng $p$ lên bốn lần, phương sai và độ lệch chuẩn của $\hat J$ thay đổi thế nào trong mô hình lý tưởng?
:::

::: solution
Phương sai giảm còn một phần tư; độ lệch chuẩn giảm còn một nửa.
:::

## 6. Quét ma trận thưa trong thực hành

Hoán vị ma trận lớn không khả thi. MMDS thay hoán vị bằng hàm băm trên số hàng. Nguồn: MMDS §3.3.5.

Đầu vào: vũ trụ $U$, $u=|U|$; $N$ cột; $p$ hàm $h_i:U\to\{0,\ldots,u-1\}$. Dữ liệu thưa được nhóm theo hàng, tức một luồng các cặp $(r,c)$ thỏa $A[r,c]=1$. Đầu ra: $SIG\in(\{0,\ldots,u-1\}\cup\{\infty\})^{p\times N}$.

::: example Ví dụ 3.8: diễn tiến trên Hình 3.4
Ma trận của Hình 3.4 (các tập $\{0,3\},\{2\},\{1,3,4\},\{0,2,3\}$ ở các cột $S_1,\ldots,S_4$) dùng hai hàm $h_1(x)=x+1\bmod5$, $h_2(x)=3x+1\bmod5$. Khởi đầu bảng chứa đầy $\infty$; quét từng hàng $r=0,\ldots,4$ theo các cột có số 1:

| $r$ | Cột có 1 | $h_1$ | $h_2$ | Thay đổi |
|---|---|---|---|---|
| 0 | $S_1,S_4$ | 1 | 1 | $S_1,S_4\leftarrow(1,1)$ |
| 1 | $S_3$ | 2 | 4 | $S_3\leftarrow(2,4)$ |
| 2 | $S_2,S_4$ | 3 | 2 | $S_2\leftarrow(3,2)$ (cột $S_4$ giữ $(1,1)$) |
| 3 | $S_1,S_3,S_4$ | 4 | 0 | Hàng $h_2$ của ba cột hạ về 0 |
| 4 | $S_3$ | 0 | 3 | $SIG[1,S_3]\leftarrow0$ |

Kết quả cuối: hàng $h_1$ là $(1,3,0,1)$, hàng $h_2$ là $(0,2,0,0)$. Hai hàm trong Ví dụ 3.8 khác $h_3,h_4$ của Bài 3.3.2. Nguồn: MMDS Ví dụ 3.8, §3.3.5.
:::

Hình dưới minh họa cách mỗi phần tử 1 tại hàng $r$, cột $c$ cập nhật $p$ ô chữ ký của cột đó.

![Mỗi phần tử một tại hàng r cột c cập nhật p giá trị chữ ký của cột c.](img/lec-05/quet-ma-tran-thua.svg)

::: derivation Bất biến của luồng nhóm theo hàng
Giả mã:

```text
SIG[1..p,1..N] <- vô cùng
cho từng hàng r trong luồng nhóm theo hàng:
  tính h1(r),...,hp(r)
  cho từng c có A[r,c]=1:
    cho i = 1,...,p:
      SIG[i,c] <- min(SIG[i,c], hi(r))
đánh dấu cột toàn vô cùng là không hợp lệ; trả SIG
```

Bất biến: sau một tiền tố hàng, $SIG[i,c]$ là mã nhỏ nhất của các hàng đã thấy thuộc cột $c$. Bất biến đúng lúc khởi tạo vì min của tập rỗng được quy ước là $\infty$. Mỗi cập nhật lấy min với hàng mới; chỉ cột có số 1 mới có thể hạ giá trị. Thuật toán dừng sau hữu hạn hàng và số 1. Cột rỗng giữ toàn $\infty$ và bị đánh dấu không hợp lệ; hai giá trị $\infty$ không được tính là một hàng trùng.
:::

### 6.1 Chi phí và bộ nhớ
Gọi $z=|\{(r,c):A[r,c]=1\}|$.

| Đại lượng | Cận |
|---|---|
| Thời gian | $O(pu+pz)$ |
| Bộ nhớ chữ ký | $\Theta(pN)$ từ, tức $\Theta(pN\log(u+1))$ bit |

Cận $O(pu+pz)$ dùng ba giả thiết:

1. đầu vào được nhóm theo hàng để mỗi $h_i(r)$ chỉ tính một lần;
2. tính một giá trị băm, lấy min và truy cập một ô đều tốn $O(1)$;
3. một ô cần $\Theta(\log(u+1))$ bit để biểu diễn $u$ mã hữu hạn cùng giá trị canh $\infty$.

Nếu đầu vào không nhóm theo hàng, mỗi phần tử 1 phải tính $p$ hàm; phần băm và cập nhật khi đó tốn $O(pz)$.

::: exercise Tự kiểm
Một cột không chứa phần tử 1 có chữ ký nào sau khi quét? Có được so nó với một cột rỗng khác bằng cách đếm $\infty=\infty$ hay không?
:::

::: solution
Chữ ký vẫn toàn $\infty$ và bị đánh dấu không hợp lệ. Hai cột cùng giữ $\infty$ không được tính là một hàng trùng.
:::

## 7. Giới hạn của hàm băm thực hành

Mô hình lý tưởng và triển khai thực hành là hai mô hình khác nhau.

| Mô hình lý tưởng | Mô hình thực hành |
|---|---|
| $\pi$ là hoán vị đều của $U$; định lý xác suất đúng chính xác. | $h_i(r)$ có thể va chạm hoặc không cho thứ tự đều. |
| Các $\pi_i$ độc lập và đều. | Một bộ hàm cố định không nhất thiết được lấy độc lập và đều từ mọi hoán vị. |

Định lý ở Mục 4.4 không tự động chuyển sang dạng thực hành. MMDS chấp nhận xấp xỉ khi miền lớn và va chạm ít; tuy nhiên, va chạm hoặc cách chọn hàm không độc lập và đều làm mất các điều kiện bảo đảm. Bài tập 3.3.3 minh họa sai lệch này trên một trường hợp nhỏ.

::: exercise Tự kiểm
Hai tập rời nhau có thể nhận cùng mã nhỏ nhất khi hàm băm thực hành có va chạm hay không? Điều này có bác bỏ định lý MinHash không?
:::

::: solution
Có thể. Hai phần tử khác nhau có thể nhận cùng mã. Điều đó không bác bỏ định lý vì hàm có va chạm không phải hoán vị của vũ trụ.
:::

## 8. Bài tập nguồn và tổng hợp

Bốn bài sau giữ nguyên dữ kiện, yêu cầu và được lấy trực tiếp từ MMDS 3e: 3.1.1 (§3.1, trang 78), 3.2.3 (§3.2, trang 81), 3.3.2 và 3.3.3 (§3.3, trang 90–91).

::: exercise Bài 3.1.1
$A=\{1,2,3,4\}$, $B=\{2,3,5,7\}$, $C=\{2,4,6\}$. Tính độ tương đồng Jaccard của mỗi cặp.
:::

::: hint
Với mỗi cặp, tính giao và hợp rồi rút gọn phân số.
:::

::: solution
$A\cap B=\{2,3\}$, $A\cup B=\{1,2,3,4,5,7\}$, nên $J(A,B)=2/6=1/3$. $A\cap C=\{2,4\}$, $A\cup C=\{1,2,3,4,6\}$, nên $J(A,C)=2/5$. $B\cap C=\{2\}$, $B\cup C=\{2,3,4,5,6,7\}$, nên $J(B,C)=1/6$.
:::

::: exercise Bài 3.2.3
Một tài liệu có $n$ byte. Bảng chữ cái đủ lớn để có ít nhất $n$ chuỗi độ dài $k$. Xác định số $k$-shingle khác nhau lớn nhất.
:::

::: hint
Chỉ có $n-k+1$ vị trí bắt đầu cửa sổ nếu $k\le n$.
:::

::: solution
Đáp án $\max(0,n-k+1)$. Có nhiều nhất $n-k+1$ vị trí bắt đầu nếu $k\le n$. Cận đạt được bằng một đoạn của chuỗi de Bruijn bậc $k$ trong đó $n-k+1$ cửa sổ độ dài $k$ đôi một khác nhau. Giả thiết bảng chữ đủ lớn để có ít nhất $n$ chuỗi độ dài $k$ bảo đảm tồn tại một đoạn đủ dài. Nếu $k>n$, lấy $0$. Nguồn: MMDS Bài tập 3.2.3, trang 81.
:::

::: exercise Bài 3.3.2
Với dữ liệu Hình 3.4 ($\{0,3\},\{2\},\{1,3,4\},\{0,2,3\}$ ở các cột $S_1,\ldots,S_4$), tính $h_3(x)=2x+4\bmod5$ và $h_4(x)=3x-1\bmod5$, rồi thêm hai hàng chữ ký mới.
:::

::: hint
Tính bảng mười giá trị băm rồi, với mỗi cột, lấy min của các hàng thuộc tập đó.
:::

::: solution
$h_3(0..4)=(4,1,3,0,2)$; hàng $h_3$ của chữ ký là $(0,3,0,0)$. $h_4(0..4)=(4,2,0,3,1)$; hàng $h_4$ là $(3,0,1,0)$. Ví dụ: cột $S_1=\{0,3\}$ với $h_3$ lấy $\min(h_3(0),h_3(3))=\min(4,0)=0$.
:::

::: exercise Bài 3.3.3
Ma trận Hình 3.6 có sáu hàng: $S_1=\{2,5\}$, $S_2=\{0,1\}$, $S_3=\{3,4\}$, $S_4=\{0,2,4\}$. Dùng $h_1=2x+1\bmod6$, $h_2=3x+2\bmod6$, $h_3=5x+2\bmod6$.

1. Tính chữ ký cho bốn cột.
2. Xác định hàm nào là hoán vị thật.
3. So sánh ước lượng và Jaccard thật cho sáu cặp.
:::

::: hint
Tính sáu giá trị của từng hàm trên $\{0,\ldots,5\}$ rồi lấy min theo cột. Một hàm là hoán vị thật nếu không có mã lặp trên toàn miền.
:::

::: solution
Sáu giá trị của từng hàm: $h_1=(1,3,5,1,3,5)$, $h_2=(2,5,2,5,2,5)$, $h_3=(2,1,0,5,4,3)$. Chỉ $h_3$ là hoán vị thật (đủ $\{0,\ldots,5\}$); $h_1,h_2$ có va chạm.

Ma trận chữ ký (các hàng $h_1,h_2,h_3$):

| | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| $h_1$ | 5 | 1 | 1 | 1 |
| $h_2$ | 2 | 2 | 2 | 2 |
| $h_3$ | 0 | 1 | 4 | 0 |

Ví dụ: $S_1=\{2,5\}$ với $h_2$ lấy $\min(h_2(2),h_2(5))=\min(2,5)=2$. Sáu cặp được xếp theo thứ tự:

1. $(S_1,S_2)$;
2. $(S_1,S_3)$;
3. $(S_1,S_4)$;
4. $(S_2,S_3)$;
5. $(S_2,S_4)$;
6. $(S_3,S_4)$.

Ước lượng Jaccard tương ứng là

$$\hat J=(1/3,1/3,2/3,2/3,2/3,2/3).$$

Jaccard thật của các cặp này lần lượt là $(0,0,1/4,0,1/4,1/4)$. Ví dụ $J(S_1,S_3)=0$ vì $S_1,S_3$ rời nhau. Sai lệch có hai nguyên nhân: $h_1,h_2$ va chạm, chẳng hạn $h_2$ cho cùng min 2 ở mọi cột; bộ ba hàm cố định cũng không được lấy độc lập và đều từ mọi hoán vị. Các giả thiết của định lý MinHash vì thế không thỏa. Nguồn: MMDS Bài tập 3.3.3, trang 90–91.
:::

### Tự kiểm cuối bài

| Bạn cần làm được | Dữ kiện dùng để kiểm |
|---|---|
| Tạo tập shingle và xử lý biên | `abcdabd` với $k=2,7,8$ |
| Tính Jaccard và xử lý hợp rỗng | Ví dụ 3.1 và Bài 3.1.1 |
| Phát biểu, chứng minh định lý MinHash | Ba loại hàng X, Y, Z |
| Tính kỳ vọng và phương sai của $\hat J$ | $p$ biến chỉ báo Bernoulli |
| Lập chữ ký trên dữ liệu thưa | Hình 3.4 và Bài 3.3.2 |
| Nhận ra khi bảo đảm lý tưởng không áp dụng | Hình 3.6 và Bài 3.3.3 |

## Tổng kết và ranh giới sang LSH

Chuỗi biểu diễn $D_i\to C_i\to\sigma(C_i)$ cho mỗi tài liệu một biểu diễn nhỏ trong khi ước lượng gần đúng Jaccard từ tỷ lệ hàng trùng của chữ ký. Vẫn còn thiếu một bước để tìm trong $\binom N2$ cặp những cặp đáng so sánh; bước này (Locality-Sensitive Hashing) thuộc Bài 6.
