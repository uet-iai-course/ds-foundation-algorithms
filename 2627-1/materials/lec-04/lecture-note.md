# Bài 04. PageRank theo chủ đề, liên kết rác và HITS

Bài này tiếp tục mô hình PageRank của Bài 03 theo các mục §5.3–5.5 của *Mining of Massive Datasets*, ấn bản 3, trang 195–208. [Bộ trang chiếu Bài 04](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html) dùng cùng dữ kiện và ký hiệu. Sách và slide chính thức được công bố tại [MMDS](http://www.mmds.org).

Sau khi học, người học có thể lập và tính PageRank theo một phân phối dịch chuyển; suy ra tác động của cụm thao túng liên kết; diễn giải TrustRank và Spam Mass; tính hai vector HITS; so sánh ý nghĩa đầu ra và chi phí của các phương pháp. Kiến thức đầu vào gồm đồ thị có hướng, phép nhân ma trận–vector, phân phối xác suất và phép lặp PageRank có bù nút cụt.

## 1. Yêu cầu xếp hạng và ký hiệu

Một vector PageRank toàn cục gán điểm cho trang theo cấu trúc liên kết, nhưng không thay đổi khi ngữ cảnh truy vấn thay đổi. Ví dụ “jaguar” của MMDS §5.3.1 có thể chỉ loài báo đốm hoặc hãng xe Jaguar. Hai ngữ cảnh cần những ưu tiên khác nhau dù đồ thị web vẫn giữ nguyên. Quy mô minh họa trong MMDS: khoảng một tỷ người dùng, mỗi vector có nhiều tỷ thành phần. Lưu một vector dài bằng số trang cho mỗi người dùng đòi hỏi nhân bản dữ liệu điểm theo số người dùng. PageRank theo chủ đề dùng một số ít vector toàn web và biểu diễn quan tâm của người dùng bằng các trọng số chủ đề.

Liên kết còn có thể được tạo để tăng điểm của một trang đích. Khi đó cần phân tích cấu trúc thao túng và bổ sung thông tin từ các trang đã được đánh giá tin cậy. Một yêu cầu khác là phân biệt trang cung cấp thông tin với trang dẫn tới nguồn thông tin; HITS gán hai điểm cho hai vai trò ấy.

### 1.1. Quy ước PageRank

Cho đồ thị có hướng $G=(V,E)$, $n=|V|\ge1$ đỉnh và $\ell=|E|$ cạnh. Đặt $d_j$ là bậc ra của đỉnh $j$. Mọi vector điểm là vector cột. Ma trận $M_0\in\mathbb R^{n\times n}$ dùng **cột nguồn**:

$$
(M_0)_{ij}=\begin{cases}
1/d_j,&j\to i\text{ và }d_j>0,\\
0,&\text{trường hợp còn lại}.
\end{cases}
$$

Vì vậy, cột của một nút cụt bằng $0$. Gọi $u=\mathbf1/n$ là phân phối đều dùng để bù nút cụt. Ở vòng $t$, tổng điểm nằm tại các nút cụt là

$$\delta^t=\sum_{j:d_j=0}r_j^t.$$

Nếu $z_j=1$ tại nút cụt và bằng $0$ ở các đỉnh khác, ma trận đã bù là $\bar M=M_0+uz^\mathsf T$. Mỗi cột của $\bar M$ có tổng bằng $1$. Ký hiệu này được dùng khi chứng minh; thuật toán chỉ cần danh sách kề, không cần lưu ma trận đặc.

| Ký hiệu | Ý nghĩa |
|---|---|
| $S$, $T$ | Tập trang chủ đề và tập trang tin cậy; đều không rỗng |
| $v$, $v_T$ | Phân phối dịch chuyển theo chủ đề hoặc theo tập tin cậy |
| $\beta\in(0,1)$ | Xác suất đi theo liên kết |
| $r^t$, $r^*$ | Trạng thái PageRank ở vòng $t$ và điểm cố định |
| $\rho$, $s_i$ | Vector TrustRank và chỉ số Spam Mass của trang $i$ |
| $\tau>0$, $K\ge1$ | Ngưỡng thay đổi và số vòng tối đa |
| $m,n,x,y,p,b$ | Số hỗ trợ, số trang toàn đồ thị và các đại lượng của cụm thao túng ở §3 |
| $L,h,a$ | Ma trận liên kết hàng nguồn, điểm trung tâm và điểm uy tín của HITS ở §5 |

Bù nút cụt và dịch chuyển là hai thao tác khác nhau: $u$ luôn đều trên toàn đồ thị; $v$ có thể tập trung ở một tập chủ đề. Đổi $v$ không làm đổi quy tắc bù.

::: exercise
Trên G4 có các cạnh A→B,C,D; B→A,D; C→A; D→B,C, cho mỗi trang điểm $1/4$ và $\beta=4/5$. Tính đóng góp theo cạnh B→A và xác định ô tương ứng của $M_0$.
:::

::: solution
B có hai cạnh ra, nên $(M_0)_{AB}=1/2$. Đóng góp tới A là $(4/5)(1/4)(1/2)=1/10$. Đây chỉ là phần theo cạnh B→A, chưa gồm các nguồn điểm khác của A.
:::

## 2. PageRank theo chủ đề

### 2.1. Phân phối dịch chuyển và bài toán điểm cố định

Tập $S\subseteq V$, $S\ne\varnothing$, biểu diễn các trang đại diện cho một chủ đề. Trong trường hợp đều trên $S$,

$$v_i=\begin{cases}1/|S|,&i\in S,\\0,&i\notin S.\end{cases}$$

Tổng quát hơn, $v\ge0$ và $\sum_i v_i=1$. Ở một bước, nhánh theo liên kết có xác suất $\beta$, còn nhánh dịch chuyển có xác suất $1-\beta$ và chọn trang theo $v$. Điểm được cập nhật bởi

$$r^{t+1}=\beta M_0r^t+\beta\delta^t u+(1-\beta)v.$$

Bài toán là tìm phân phối $r^*$ thỏa

$$r^*=\beta\bar Mr^*+(1-\beta)v.$$

Các trang ngoài $S$ vẫn có thể nhận điểm theo cạnh. Tập chủ đề xác định nơi nhận phần dịch chuyển, không loại các trang còn lại khỏi đồ thị. Đây là cơ chế §5.3.2 của MMDS, trang 196, kết hợp quy tắc bù đều đã học ở Bài 03.

### 2.2. Ví dụ bốn trang

Dùng G4 của Hình 5.15, MMDS trang 197. Tám cạnh là A→B,C,D; B→A,D; C→A; D→B,C. Không có nút cụt; thứ tự các thành phần là A, B, C, D.

![G4 với tám cạnh; B và D được đánh dấu bằng viền đôi và nhãn thuộc tập chủ đề S.](img/lec-04/hinh-5-15.svg)

Ma trận và phân phối dịch chuyển với $\beta=4/5$, $S=\{B,D\}$ là

$$M_0=\begin{pmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{pmatrix},\qquad v=(0,1/2,0,1/2)^\mathsf T.$$

::: example
Khởi tạo $r^0=v$. Phần thêm do dịch chuyển là $(1-\beta)v=(0,1/10,0,1/10)^\mathsf T$ trong mọi vòng. Ở vòng thứ nhất, B chuyển $1/4$ cho A và D trước khi nhân $\beta$; D chuyển $1/4$ cho B và C. Do đó $M_0r^0=(1/4,1/4,1/4,1/4)^\mathsf T$.

| Trang | Theo liên kết $\beta(M_0r^0)_i$ | Dịch chuyển | $r_i^1$ |
|---|---:|---:|---:|
| A | $1/5$ | $0$ | $1/5$ |
| B | $1/5$ | $1/10$ | $3/10$ |
| C | $1/5$ | $0$ | $1/5$ |
| D | $1/5$ | $1/10$ | $3/10$ |

Ở vòng thứ hai, A nhận từ B và C:

$$r_A^2=\frac45\left(\frac12\frac3{10}+\frac15\right)=\frac7{25}.$$

B nhận từ A, D và phần dịch chuyển:

$$r_B^2=\frac45\left(\frac13\frac15+\frac12\frac3{10}\right)+\frac1{10}=\frac{41}{150}.$$

C nhận cùng phần theo cạnh như B, nhưng không nhận $1/10$ do dịch chuyển. Các vòng và nghiệm chính xác được phân biệt trong bảng:

| Trạng thái | A | B | C | D |
|---|---:|---:|---:|---:|
| $r^1$ | $1/5$ | $3/10$ | $1/5$ | $3/10$ |
| $r^2$ | $7/25$ | $41/150$ | $13/75$ | $41/150$ |
| $r^3$ | $31/125$ | $71/250$ | $23/125$ | $71/250$ |
| $r^*$ | $9/35$ | $59/210$ | $19/105$ | $59/210$ |

Để tìm hàng cuối, giải hệ $r=\beta M_0r+(1-\beta)v$ và $\sum_i r_i=1$. Hai phương trình tại B, D cho $r_B=r_D=q$; phương trình tại C cho $r_C=q-1/10$. Từ phương trình tại B, $q=4r_A/9+1/6$. Thế vào $r_A+3q-1/10=1$ được $r_A=9/35$ và $q=59/210$. A và C nằm ngoài $S$ nhưng vẫn có điểm dương do nhận liên kết.
:::

### 2.3. Thuật toán trên danh sách kề

Đầu vào gồm $G$, $v$, $\beta$, $\tau>0$ và số nguyên $K\ge1$. Danh sách `out[j]` chứa các đích của cạnh ra từ $j$. Thuật toán trả vector tính được cùng trạng thái đạt ngưỡng hay hết số vòng.

```text
r ← v
với t = 0, ..., K - 1:
    delta ← tổng r[j] trên các nút cụt
    với mỗi i: new[i] ← beta * delta / n + (1 - beta) * v[i]
    với mỗi j có d[j] > 0:
        với mỗi i thuộc out[j]:
            new[i] ← new[i] + beta * r[j] / d[j]
    Delta ← tổng |new[i] - r[i]|
    r ← new
    nếu Delta ≤ tau: trả về (r, đạt ngưỡng)
trả về (r, hết số vòng)
```

Mỗi vòng chỉ đọc đóng góp từ vector cũ `r` và ghi vào `new`. Nếu cập nhật từng thành phần ngay trong `r`, những cạnh duyệt sau có thể dùng điểm của vòng mới; khi đó không còn đúng phép cập nhật đồng thời đã đặc tả. Với đồ thị toàn nút cụt, $M_0=0$, $\delta^t=1$ và bước lặp cho $r^{t+1}=\beta u+(1-\beta)v$, vẫn là một phân phối hợp lệ.

### 2.4. Bảo toàn, hội tụ và sai số dừng

**Mệnh đề bảo toàn.** Nếu $r^t$ không âm và có tổng bằng $1$, thì $r^{t+1}$ cũng không âm và có tổng bằng $1$.

::: proof
Mỗi cột không cụt của $M_0$ có tổng bằng $1$, còn mỗi cột cụt có tổng bằng $0$. Vì thế tổng điểm của ba số hạng cập nhật lần lượt là $\beta(1-\delta^t)$, $\beta\delta^t$ và $1-\beta$. Tổng của chúng bằng $1$. Mọi hệ số và mọi thành phần đầu vào đều không âm. Cơ sở $r^0=v$ thỏa các điều kiện, nên quy nạp cho kết luận ở mọi vòng.
:::

Bảo toàn tổng điểm chưa chứng minh hội tụ. Đặt $F(r)=\beta\bar Mr+(1-\beta)v$. Vì mỗi cột của $\bar M$ không âm và có tổng bằng $1$, $F$ là phép co theo chuẩn $\|x\|_1=\sum_i|x_i|$.

::: proof
Với hai vector $p,q$, phần dịch chuyển triệt tiêu và bất đẳng thức tam giác cho

$$\begin{aligned}
\|F(p)-F(q)\|_1
&\le\beta\sum_i\sum_j\bar M_{ij}|p_j-q_j|\\
&=\beta\sum_j|p_j-q_j|\sum_i\bar M_{ij}\\
&=\beta\|p-q\|_1.
\end{aligned}$$

Do $0<\beta<1$, các sai khác liên tiếp giảm theo cấp số nhân. Tổng khoảng cách từ một trạng thái tới các trạng thái sau bị chặn bởi một cấp số nhân có phần đuôi tiến về $0$; dãy là Cauchy và hội tụ trong $\mathbb R^n$. Tính liên tục của $F$ cho giới hạn thỏa phương trình điểm cố định. Nếu $r^*$ và $q^*$ đều là điểm cố định thì $\|r^*-q^*\|_1\le\beta\|r^*-q^*\|_1$, nên chúng bằng nhau. Bảo toàn và tính đóng của tập phân phối bảo đảm nghiệm là một phân phối.
:::

Đặt $\Delta=\|r^{t+1}-r^t\|_1$. Sai số của **vector mới** được chặn bằng tổng các sai khác sau nó:

$$\|r^{t+1}-r^*\|_1\le\beta\Delta+\beta^2\Delta+\cdots=\frac{\beta}{1-\beta}\Delta.$$

Với $\beta=4/5$, cận là $4\Delta$. Để bảo đảm sai số không quá $\varepsilon$, có thể chọn $\tau\le(1-\beta)\varepsilon/\beta$ và chỉ xác nhận cận khi $\Delta\le\tau$. Hết $K$ vòng là trạng thái hết giới hạn, không tự xác nhận sai số. Lập luận này mở rộng phép co của Bài 03 cho phân phối dịch chuyển cố định bất kỳ.

### 2.5. Kết hợp chủ đề và chi phí

Giả sử $k$ chủ đề dùng cùng $\bar M$ và $\beta$. Chủ đề $j$ có phân phối $v^{(j)}$ và nghiệm $r^{(j)}$. Với trọng số $w_j\ge0$, $\sum_jw_j=1$, đặt

$$v=\sum_{j=1}^kw_jv^{(j)},\qquad r=\sum_{j=1}^kw_jr^{(j)}.$$

Nhân phương trình điểm cố định thứ $j$ với $w_j$ rồi cộng cho

$$\beta\bar Mr+(1-\beta)v=\sum_jw_j\left[\beta\bar Mr^{(j)}+(1-\beta)v^{(j)}\right]=r.$$

Do nghiệm là duy nhất, $r$ chính là nghiệm cho phân phối ghép $v$. Điều kiện cùng ma trận bù và cùng $\beta$ cho phép đưa toán tử ra ngoài tổng; nếu thay hai đối tượng đó theo chủ đề thì suy luận này không còn áp dụng.

Mô hình chi phí coi mỗi phép toán vô hướng có chi phí đơn vị, với đầu vào bằng danh sách kề. Mỗi vòng duyệt $\ell$ cạnh để cộng điểm và duyệt $n$ đỉnh một số lần cố định để bù, dịch chuyển, so sánh. Thời gian mỗi vòng là $\Theta(n+\ell)$. Đầu vào chiếm $\Theta(n+\ell)$ ô; các vector trạng thái cần bộ nhớ phụ $\Theta(n)$.

Nếu chủ đề $j$ thực chạy $K_j$ vòng, tổng tiền tính độc lập là

$$\Theta\left(\left(\sum_{j=1}^kK_j\right)(n+\ell)\right).$$

Giới hạn $K_j\le K$ cho cận $O(kK(n+\ell))$. Nếu mọi vector chạy đủ $K$ vòng, chi phí là $\Theta(kK(n+\ell))$. Lưu $k$ nghiệm cần $\Theta(kn)$ số. Khi đã có $c$ trang ứng viên, ghép điểm của chúng cần $\Theta(kc)$ phép nhân–cộng; phép đếm này chưa gồm tìm ứng viên hoặc xác định chủ đề truy vấn.

Nhờ kết hợp tuyến tính, truy vấn “jaguar” có thể dùng trọng số theo động vật hoặc ô tô trên các vector đã lưu. Phương án này xử lý ngữ cảnh xếp hạng; nó chưa xử lý việc các cạnh bị tạo có chủ đích để làm tăng điểm.

::: exercise
Từ $r^1=(1/5,3/10,1/5,3/10)^\mathsf T$ của G4, tính $r_C^2$. Giải thích kết quả đối với mệnh đề “một trang ngoài tập dịch chuyển luôn có điểm bằng $0$”.
:::

::: solution
C nhận theo cạnh từ A và D, nên $r_C^2=(4/5)[(1/3)(1/5)+(1/2)(3/10)]=13/75$. C không nhận dịch chuyển trực tiếp nhưng điểm vẫn dương. Mệnh đề đã nêu là sai.
:::

## 3. Cụm thao túng liên kết

### 3.1. Kiến trúc và giả thiết

Liên kết rác được tạo nhằm làm tăng điểm xếp hạng không tương xứng với giá trị nội dung. MMDS §5.4.1–5.4.2 phân biệt trang không thể tác động, trang có thể đặt liên kết và trang thuộc quyền sở hữu. Mô hình sau xét PageRank toàn cục với dịch chuyển đều, thay cho phân phối chủ đề của §2.

![Ba vùng trong Hình 5.16; các liên kết ngoài đi vào đích, đích và m hỗ trợ có cạnh qua lại.](img/lec-04/hinh-5-16-cum-thao-tung.svg)

Đồ thị toàn cục có $n$ trang, không có nút cụt; $0<\beta<1$. Cụm gồm một đích và $m\ge1$ hỗ trợ, với $n\ge m+1$. Đích chỉ trỏ tới toàn bộ $m$ hỗ trợ. Mỗi hỗ trợ chỉ trỏ lại đích và chỉ nhận cạnh từ đích. Mọi cạnh từ ngoài đi vào cụm đều kết thúc ở đích. Hình chỉ biểu diễn các liên kết liên quan đến cụm, không liệt kê toàn bộ cạnh của các trang bên ngoài.

Gọi $y$ là điểm đích và $p$ là điểm mỗi hỗ trợ ở trạng thái cân bằng. Mỗi trang nhận bước dịch chuyển $b=(1-\beta)/n$. Đại lượng $x$ là tổng đóng góp theo cạnh từ ngoài tới đích:

$$x=\sum_{j\text{ ngoài cụm}:j\to\text{đích}}\frac{\beta r_j}{d_j}.$$

Như vậy $x$ đã nhân $\beta$ và chia bậc ra. Nó là đóng góp tại trạng thái cân bằng của toàn đồ thị, không phải giá trị có thể tăng tùy ý mà bỏ qua điều kiện tổng điểm bằng $1$.

### 3.2. Cân bằng điểm hỗ trợ và đích

Đích có đúng $m$ cạnh ra nên truyền $\beta y/m$ tới mỗi hỗ trợ. Các hỗ trợ không nhận cạnh ngoài; bởi vậy

$$p=\frac{\beta y}{m}+b.$$

Mỗi hỗ trợ có một cạnh ra, truyền $\beta p$ về đích. Ba nguồn tại đích là đóng góp ngoài $x$, tổng quay lại $\beta mp$ và bước dịch chuyển $b$:

$$y=x+\beta mp+b.$$

![Ba nguồn đóng góp x, beta m p và b cùng đi vào trang đích có điểm y.](img/lec-04/luong-hang-trong-cum.svg)

::: derivation
Thế biểu thức của $p$ vào phương trình đích:

$$\begin{aligned}
y&=x+\beta m\left(\frac{\beta y}{m}+b\right)+b\\
 &=x+\beta^2y+\beta mb+b.
\end{aligned}$$

Do $1-\beta^2>0$,

$$y=\frac{x+\beta mb+b}{1-\beta^2}.$$

Hạng $\beta^2y$ mô tả điểm đi từ đích qua hỗ trợ rồi quay lại. Số hỗ trợ triệt tiêu trong hạng này vì điểm được chia cho $m$ rồi cộng từ $m$ hỗ trợ; số hỗ trợ vẫn còn trong tổng điểm dịch chuyển mà chúng nhận.
:::

### 3.3. Xấp xỉ trong sách và phạm vi kết luận

MMDS trang 201 bỏ riêng bước dịch chuyển trực tiếp tới đích. Biểu thức tương ứng là

$$y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\frac mn.$$

Không bỏ bước dịch chuyển tại các hỗ trợ: tổng của chúng tạo thành số hạng tỷ lệ với $m/n$. Sai khác giữa nghiệm đầy đủ và biểu thức xấp xỉ là

$$\frac{b}{1-\beta^2}=\frac1{n(1+\beta)}.$$

Với $\beta=0.85=17/20$ của Ví dụ 5.11, hệ số của $x$ là $400/111\approx3.6036$ và hệ số của $m/n$ là $17/37\approx0.45946$. Phần $x$ được nhân khoảng $3.6$ lần, tương ứng phần tăng so với $x$ khoảng $260.36\%$. Đây là phép tính của mô hình, không phải số đo trên một hệ tìm kiếm hiện hành.

Cụm cần $m$ trang hỗ trợ và $2m$ cạnh nội bộ: $m$ cạnh đi từ đích và $m$ cạnh quay lại. Công thức phải được lập lại nếu thêm cạnh ngoài vào hỗ trợ, thêm cạnh ra của đích hoặc thay cấu trúc hỗ trợ. Một cụm liên kết dày có thể phục vụ chức năng hợp lệ; hình dạng đồ thị riêng lẻ chưa xác nhận nội dung rác. TrustRank đưa thông tin đánh giá bên ngoài vào phép xếp hạng.

::: exercise
Trong mô hình vừa xét, sửa phương trình $y=\beta x+\beta mp$ và xác định hạng của nghiệm $y$ bị lược trong xấp xỉ của sách.
:::

::: solution
Phương trình đầy đủ là $y=x+\beta mp+b$. Nhân thêm $\beta$ vào $x$ là đếm hệ số theo cạnh lần thứ hai; thiếu $b$ là bỏ bước dịch chuyển tại đích. Sau khi giải, hạng bị lược khỏi nghiệm là $b/(1-\beta^2)$, không chỉ là $b$.
:::

## 4. TrustRank và Spam Mass

### 4.1. Tập tin cậy và phép lặp

TrustRank dùng các trang đã được đánh giá tin cậy làm tập dịch chuyển $T$. Giả định của mô hình là các trang tin cậy ít tạo liên kết tới trang rác. Đây là giả định về xu hướng liên kết; nó không có tính tuyệt đối, chẳng hạn khi trang cho phép người khác đặt liên kết.

Với $T\ne\varnothing$, chọn $v_T$ đều trên $T$ và bằng $0$ bên ngoài. Khởi tạo $\rho^0=v_T$; phép lặp là

$$\rho^{t+1}=\beta M_0\rho^t+\beta\delta_\rho^t u+(1-\beta)v_T,\qquad \delta_\rho^t=\sum_{j:d_j=0}\rho_j^t.$$

Đây là thuật toán ở §2 với $r$ thay bằng $\rho$ và $v$ thay bằng $v_T$. Bù nút cụt, điều kiện dừng, bảo toàn và tính co được giữ nguyên. Thông tin về độ tin cậy của hạt giống đến từ đánh giá ngoài phép lặp; vector kết quả không tự chứng nhận tính đúng của đánh giá đó. Nguồn: MMDS §5.4.4, trang 202–203.

### 4.2. Ví dụ trên cùng đồ thị G4

Chọn $T=\{B,D\}$ và $\beta=4/5$. Tập dịch chuyển có cùng các đỉnh như ví dụ chủ đề, nên nghiệm số không đổi:

$$\rho=(9/35,59/210,19/105,59/210)^\mathsf T.$$

![G4 giữ tám cạnh; B và D có viền đôi và nhãn tập tin cậy T.](img/lec-04/hinh-5-15-tin-cay.svg)

A và C không thuộc $T$ nhưng vẫn nhận điểm qua cạnh. Để đo thay đổi so với xếp hạng toàn cục, tính PageRank $r$ với phân phối đều $u$, giữ cùng đồ thị, cùng quy tắc bù và cùng $\beta=4/5$. Nghiệm là

$$r=(9/28,19/84,19/84,19/84)^\mathsf T.$$

| Trang | $r_i$ | $\rho_i$ | $r_i-\rho_i$ |
|---|---:|---:|---:|
| A | $9/28$ | $9/35$ | $9/140$ |
| B | $19/84$ | $59/210$ | $-23/420$ |
| C | $19/84$ | $19/105$ | $19/420$ |
| D | $19/84$ | $59/210$ | $-23/420$ |

Cả hai vector có tổng bằng $1$, nên tổng cột hiệu bằng $0$. Bảng tính lại PageRank nền với cùng $\beta$ để tách ảnh hưởng của phân phối dịch chuyển. Các số này không phải bản chép Hình 5.17: hình nguồn dùng PageRank không dịch chuyển của Ví dụ 5.2 làm nền và TrustRank với $\beta=0.8$.

### 4.3. Định nghĩa và cách diễn giải Spam Mass

Với $r_i>0$, MMDS §5.4.5, trang 203, định nghĩa chỉ số Spam Mass:

$$s_i=\frac{r_i-\rho_i}{r_i}=1-\frac{\rho_i}{r_i}.$$

Đây là chênh lệch tương đối so với điểm nền, không phải một xác suất. Trên G4:

| Trang | Phép tính | $s_i$ |
|---|---|---:|
| A | $(9/140)/(9/28)$ | $1/5$ |
| B | $(-23/420)/(19/84)$ | $-23/95$ |
| C | $(19/420)/(19/84)$ | $1/5$ |
| D | $(-23/420)/(19/84)$ | $-23/95$ |

Giá trị âm tại B và D biểu thị $\rho_i>r_i$. Thay số âm bằng $0$ làm đổi định nghĩa và mất thông tin hướng thay đổi. Giá trị gần $1$ biểu thị $\rho_i$ nhỏ so với $r_i$, có thể hỗ trợ chọn trang cần rà soát theo giả định của mô hình; chỉ số dương không chứng minh trang đó là rác.

Tập $T$ nhỏ làm giảm công sức đánh giá nhưng có thể thiếu độ phủ. Điểm tin cậy thấp có thể phản ánh một vùng nội dung ít liên hệ với hạt giống đã chọn. Vì thế chất lượng và độ phủ của $T$ ảnh hưởng cách diễn giải điểm.

### 4.4. Chi phí và kiểm tra

Hai vector $r,\rho$ dùng hai phép lặp thưa, mỗi vòng $\Theta(n+\ell)$. Nếu chúng thực chạy $K_r,K_\rho$ vòng, tổng thời gian lặp là $\Theta((K_r+K_\rho)(n+\ell))$. Khi đã có hai vector, tính toàn bộ $s_i$ cần $\Theta(n)$ phép toán. Chi phí đánh giá hạt giống không nằm trong mô hình đếm phép toán đồ thị này.

::: exercise
Cho $r_B=19/84$, $\rho_B=59/210$ và $s_A=1/5$. Tính $s_B$, giải thích dấu của nó và đánh giá kết luận “A chắc chắn là trang rác”.
:::

::: solution
$s_B=-23/95<0$ vì TrustRank tại B lớn hơn PageRank nền. Chỉ số tại A cho biết điểm giảm tương đối khi chuyển sang tập tin cậy đã chọn; nó chưa chứng minh nội dung của A là rác. Kết luận còn phụ thuộc độ phủ và chất lượng tập tin cậy, cùng giả định liên kết của mô hình.
:::

TrustRank thay nguồn dịch chuyển để thể hiện tin cậy. HITS thay ý nghĩa đầu ra thành hai vai trò cấu trúc; điểm uy tín trong HITS không đồng nghĩa với điểm tin cậy vừa xét.

## 5. Điểm trung tâm và điểm uy tín trong HITS

### 5.1. Hai vai trò của trang

Trong Ví dụ 5.13 của MMDS §5.5.1, trang danh sách học phần dẫn tới các trang của từng học phần. Trang học phần cung cấp nội dung, còn trang danh sách chỉ dẫn tới nguồn nội dung. Thuật toán tìm kiếm theo chủ đề dựa trên siêu liên kết (HITS) gán cho mỗi trang $i$ điểm trung tâm $h_i$ và điểm uy tín $a_i$.

![Trang danh mục học phần trỏ tới hai trang học phần; nhãn trung tâm ở danh mục và uy tín ở các trang đích.](img/lec-04/cap-vai-tro-hits.svg)

Đầu vào là đồ thị các trang và liên kết đã chọn. Uy tín nhận tổng điểm trung tâm theo các cạnh vào; trung tâm nhận tổng điểm uy tín theo các cạnh ra. Một trang có cả hai điểm, dù ví dụ chức năng làm rõ hai vai trò bằng các trang khác nhau.

### 5.2. Định nghĩa phép cập nhật

Ma trận $L\in\{0,1\}^{n\times n}$ của HITS dùng **hàng nguồn**: $L_{ij}=1$ khi $i\to j$, bằng $0$ nếu không. Với vector không âm $q$ có phần tử lớn nhất dương, định nghĩa

$$N(q)=\frac{q}{\max_iq_i}.$$

Khởi tạo $h^0=a^0=\mathbf1$. Mỗi vòng tính uy tín trước, rồi tính trung tâm bằng uy tín vừa cập nhật:

$$\widetilde a=L^\mathsf Th^t,\qquad a^{t+1}=N(\widetilde a),$$
$$\widetilde h=La^{t+1},\qquad h^{t+1}=N(\widetilde h).$$

Mỗi cạnh đóng góp trọn điểm nguồn hoặc đích tương ứng; HITS không chia cho bậc ra. Chia toàn vector cho cùng số dương giữ tỷ lệ và thứ tự các thành phần, đồng thời đưa giá trị lớn nhất về $1$. Tổng các thành phần không nhất thiết bằng $1$; hai vector không phải phân phối xác suất.

### 5.3. Hai vòng trên đồ thị năm trang

G5 của Hình 5.18, MMDS trang 206, có các cạnh A→B,C,D; B→A,D; C→E; D→B,C. E không có cạnh ra. So với G4, cạnh C→A được thay bằng C→E. Thứ tự vector là A, B, C, D, E.

![G5 có năm đỉnh và tám cạnh; C trỏ E thay vì A, E không có cạnh ra.](img/lec-04/hinh-5-18.svg)

$$L=\begin{pmatrix}0&1&1&1&0\\1&0&0&1&0\\0&0&0&0&1\\0&1&1&0&0\\0&0&0&0&0\end{pmatrix}.$$

::: example
Với $h^0$ toàn $1$, uy tín thô là $(1,2,2,2,1)^\mathsf T$. Chẳng hạn, B nhận từ A và D nên có $1+1=2$; E nhận từ C nên có $1$. Giá trị lớn nhất là $2$:

$$a^1=(1/2,1,1,1,1/2)^\mathsf T.$$

Trung tâm thô dùng $a^1$, không dùng $a^0$:

| Trang | Tổng uy tín theo cạnh ra | Trung tâm thô | $h_i^1$ |
|---|---|---:|---:|
| A | $1+1+1$ | $3$ | $1$ |
| B | $1/2+1$ | $3/2$ | $1/2$ |
| C | $1/2$ | $1/2$ | $1/6$ |
| D | $1+1$ | $2$ | $2/3$ |
| E | $0$ | $0$ | $0$ |

Chuẩn hóa bằng giá trị lớn nhất $3$ cho $h^1=(1,1/2,1/6,2/3,0)^\mathsf T$. E có trung tâm bằng $0$ nhưng uy tín bằng $1/2$, vì không có cạnh ra vẫn có thể có cạnh vào.

Ở vòng hai, uy tín thô tại B là $h_A^1+h_D^1=5/3$. Đây là giá trị lớn nhất của vector thô. Sau khi chuẩn hóa uy tín, trung tâm thô tại A bằng $1+1+9/10=29/10$, là mẫu số chuẩn hóa trung tâm:

| Trang | $\widetilde a$ | $a^2$ | $\widetilde h$ | $h^2$ |
|---|---:|---:|---:|---:|
| A | $1/2$ | $3/10$ | $29/10$ | $1$ |
| B | $5/3$ | $1$ | $6/5$ | $12/29$ |
| C | $5/3$ | $1$ | $1/10$ | $1/29$ |
| D | $3/2$ | $9/10$ | $2$ | $20/29$ |
| E | $1/6$ | $1/10$ | $0$ | $0$ |

Hai phép chuẩn hóa trong cùng vòng có thể dùng hai mẫu số khác nhau. Các hàng ở vòng hai là trạng thái trung gian, chưa phải nghiệm giới hạn. Vết tính này dùng quy ước của §5.5.2, Ví dụ 5.15, trang 206–207.
:::

### 5.4. Thuật toán, bất biến và điều kiện dừng

Đầu vào gồm đồ thị có $n\ge1$ đỉnh, ít nhất một cạnh, ngưỡng $\tau>0$ và giới hạn $K\ge1$. Nếu đồ thị không có cạnh, thuật toán trả trạng thái không xác định theo chuẩn hóa bằng giá trị lớn nhất, trước khi thực hiện phép chia.

```text
nếu đồ thị không có cạnh: trả về không xác định khi chuẩn hóa bằng giá trị lớn nhất
h ← vector toàn 1; a ← vector toàn 1
với t = 0, ..., K - 1:
    a_new ← N(L chuyển vị * h)
    h_new ← N(L * a_new)
    Delta_a ← max |a_new[i] - a[i]|
    Delta_h ← max |h_new[i] - h[i]|
    a ← a_new; h ← h_new
    nếu max(Delta_a, Delta_h) ≤ tau:
        trả về (h, a, đạt ngưỡng)
trả về (h, a, hết số vòng)
```

Các tích được tính bằng duyệt cạnh. Với ít nhất một cạnh $i\to j$, khởi tạo dương cho $\widetilde a_j>0$. Trang nguồn $i$ sau đó nhận $a_j>0$ nên có $\widetilde h_i>0$. Lập luận tiếp tục ở các vòng sau cho các nguồn có cạnh ra. Vì vậy, cả hai vector thô có phần tử lớn nhất dương; chuẩn hóa được xác định. Mỗi trạng thái sau cập nhật không âm và có giá trị lớn nhất bằng $1$.

Điều kiện dừng kiểm cả hai vector theo chuẩn vô cùng $\|q\|_\infty=\max_i|q_i|$. Đạt ngưỡng chỉ xác nhận hai trạng thái liên tiếp thay đổi ít theo tiêu chí đã chọn; không có cận sai số PageRank ở §2 để áp dụng trực tiếp cho HITS. Hết $K$ vòng phải được báo riêng.

### 5.5. Điểm ổn định và phác thảo điều kiện hội tụ

Tại cặp điểm ổn định chuẩn hóa, tồn tại $\lambda,\mu>0$ sao cho

$$h=\lambda La,\qquad a=\mu L^\mathsf Th.$$

Thế một quan hệ vào quan hệ kia cho

$$h=\lambda\mu LL^\mathsf Th,\qquad a=\lambda\mu L^\mathsf TLa.$$

Vì vậy, hướng của các điểm ổn định liên hệ với các hướng riêng của hai tích ma trận. Các hệ số chuẩn hóa chỉ thay độ lớn, không thay hướng của một vector khác $0$.

Một điều kiện đủ cho hướng giới hạn duy nhất là trị riêng lớn nhất của $LL^\mathsf T$ là đơn và khởi tạo có thành phần khác $0$ theo hướng riêng ấy. Ma trận $LL^\mathsf T$ đối xứng nửa xác định dương. Trong phân tích theo các hướng riêng, thành phần ứng với trị riêng nhỏ hơn tăng chậm hơn qua phép lặp; tỷ lệ của nó so với thành phần lớn nhất giảm sau chuẩn hóa. Nếu trị riêng lớn nhất có nhiều hướng độc lập, hướng giới hạn có thể phụ thuộc khởi tạo. Đây là phác thảo điều kiện đủ cho phép lặp lũy thừa, không phải khẳng định duy nhất vô điều kiện cho mọi đồ thị.

Trên G5, hai giới hạn làm tròn là

$$h\approx(1,0.3583,0,0.7165,0)^\mathsf T,\qquad a\approx(0.2087,1,1,0.7913,0)^\mathsf T.$$

Các giá trị này phải được phân biệt với hai vòng hữu hạn ở §5.3.

### 5.6. Chi phí và kiểm tra

Với danh sách cạnh và phép toán vô hướng có chi phí đơn vị, một vòng gồm:

| Công việc | Số đối tượng xử lý |
|---|---:|
| Cộng $h_i$ vào uy tín tại $j$ theo cạnh $i\to j$ | $\ell$ cạnh |
| Cộng $a_j$ mới vào trung tâm tại $i$ | $\ell$ cạnh |
| Chuẩn hóa và so sánh hai vector | Số lượt cố định trên $n$ đỉnh |

Thời gian mỗi vòng là $\Theta(n+\ell)$, bộ nhớ phụ $\Theta(n)$ và bộ nhớ đầu vào $\Theta(n+\ell)$. Nếu thực chạy $K'$ vòng thì tổng là $\Theta(K'(n+\ell))$. Hai lượt cạnh tạo hệ số công việc khác PageRank dù cùng bậc tiệm cận. Tích $LL^\mathsf T$ có thể chứa nhiều phần tử khác $0$ hơn $L$ vì nối các trang chung đích. Thuật toán không tạo hai tích ma trận này để chạy; chúng chỉ phục vụ lập luận về điểm ổn định.

::: exercise
Cho $a^1=(1/2,1,1,1,1/2)^\mathsf T$ trên G5; giá trị trung tâm thô lớn nhất là $3$. Tính $h_B^1$, giải thích việc không chia thêm cho bậc ra của B và xác định $h_E^1$.
:::

::: solution
B trỏ A và D nên trung tâm thô bằng $1/2+1=3/2$, suy ra $h_B^1=(3/2)/3=1/2$. HITS lấy tổng uy tín các đích, không lấy trung bình theo bậc ra. E không có cạnh ra nên tổng rỗng bằng $0$ và $h_E^1=0$.
:::

## 6. Lựa chọn phương pháp

| Yêu cầu | Phương pháp | Điều kiện và ý nghĩa đầu ra |
|---|---|---|
| Xếp hạng “jaguar” theo động vật hoặc ô tô | PageRank theo chủ đề | Có tập chủ đề hoặc trọng số; đầu ra là một phân phối điểm theo ngữ cảnh |
| Đánh giá ảnh hưởng của liên kết thao túng | TrustRank và Spam Mass | Có tập tin cậy phù hợp; chỉ số chênh lệch hỗ trợ rà soát, không tự tạo nhãn chắc chắn |
| Nhận diện trang danh sách và trang nội dung học phần | HITS | Cần hai vai trò trung tâm, uy tín; hai vector được chuẩn hóa bằng giá trị lớn nhất |

Cùng bậc chi phí $\Theta(n+\ell)$ mỗi vòng chưa đủ suy ra cùng thời gian chạy. Số vòng thực, tiêu chí dừng, hệ số công việc, biểu diễn dữ liệu và chi phí chuẩn bị thông tin bên ngoài đều có thể khác nhau.

::: exercise
1. Giữ G4 và $\beta=4/5$, đổi tập dịch chuyển từ $\{B,D\}$ sang $\{A\}$. Xác định thành phần thay đổi trong phép lặp.
2. Giải thích vì sao $x$ của cụm thao túng không được nhân thêm $\beta$.
3. Đánh giá việc thay mọi giá trị Spam Mass âm bằng $0$.
4. Nêu hai đại lượng cần biết thêm ngoài bậc chi phí mỗi vòng khi so sánh thời gian PageRank theo chủ đề với HITS.
5. Phân biệt điểm uy tín HITS với điểm tin cậy TrustRank.
:::

::: solution
1. $M_0$ và $\beta$ giữ nguyên; $v$ đổi thành $(1,0,0,0)^\mathsf T$. Khởi tạo $r^0=v$ cũng đổi. G4 không có nút cụt.
2. Mỗi hạng trong $x$ đã là $\beta r_j/d_j$; nhân thêm làm áp dụng hệ số theo cạnh lần thứ hai.
3. Phép thay đổi làm mất thông tin $\rho_i>r_i$ và đổi định nghĩa chỉ số.
4. Chẳng hạn, số vòng thực và hệ số công việc mỗi vòng; còn cần xét tiêu chí dừng, thực thi và chi phí chuẩn bị khi so sánh hệ thống đầy đủ.
5. Uy tín HITS nhận điểm từ các trang trung tâm theo cấu trúc liên kết; TrustRank là phân phối PageRank ưu tiên các hạt giống được đánh giá tin cậy bên ngoài.
:::

## 7. Bài tập từ giáo trình

Ba bài sau dùng trực tiếp MMDS: Bài 5.3.1(a,b), Bài 5.4.1(a,c) và Bài 5.5.2. Mỗi bài dự kiến 20 phút, tổng 60 phút. Các ý được dịch và tách yêu cầu trình bày; dữ kiện và yêu cầu toán học giữ theo nguồn.

### 7.1. PageRank với hai tập dịch chuyển

::: exercise
**Bài 5.3.1(a,b), MMDS §5.3.5, trang 199.** Trên đồ thị Hình 5.15, tính PageRank theo chủ đề khi tập dịch chuyển là (a) chỉ A; (b) A và C. Dùng $\beta=0.8$ kế thừa Ví dụ 5.10.

G4 có A→B,C,D; B→A,D; C→A; D→B,C. Trình bày phân phối dịch chuyển, hệ phương trình và vector theo thứ tự A,B,C,D. Kiểm cả tổng bằng $1$ và phương trình điểm cố định.
:::

![G4 trung tính với đủ tám cạnh, không đánh dấu sẵn tập dịch chuyển.](img/lec-04/hinh-5-1-trung-tinh.svg)

::: hint
Giữ $M_0$ của §2.2 và chỉ đổi $v$. Các phương trình tại B và D cho phép tìm quan hệ giữa $r_B$ và $r_D$ trước khi giải toàn hệ.
:::

::: solution
(a) Với $v=(1,0,0,0)^\mathsf T$, hệ là

$$\begin{aligned}
r_A&=\frac25r_B+\frac45r_C+\frac15,\\
r_B&=\frac4{15}r_A+\frac25r_D,\\
r_C&=\frac4{15}r_A+\frac25r_D,\\
r_D&=\frac4{15}r_A+\frac25r_B.
\end{aligned}$$

Lấy phương trình B trừ D cho $r_B-r_D=(2/5)(r_D-r_B)$, suy ra $r_B=r_D$. B và C có cùng vế phải nên cũng bằng nhau. Gọi điểm chung là $q$; phương trình B cho $q=4r_A/9$. Từ $r_A+3q=1$ suy ra

$$r=(3/7,4/21,4/21,4/21)^\mathsf T.$$

(b) Với $v=(1/2,0,1/2,0)^\mathsf T$, dịch chuyển tại A là $1/10$, tại C là $1/10$. Các phương trình tại B, D giữ nguyên, nên $r_B=r_D=q=4r_A/9$. Phương trình C cho $r_C=q+1/10$. Điều kiện tổng bằng $1$ trở thành $r_A+3q+1/10=1$, do đó

$$r=(27/70,6/35,19/70,6/35)^\mathsf T.$$

Trong ý (b), phần dịch chuyển tại A giảm từ $1/5$ xuống $1/10$ so với (a); không cộng thêm $1/10$ vào phương trình A của (a). Thế hai nghiệm vào từng hệ xác nhận phương trình điểm cố định; phép kiểm tổng riêng lẻ chưa đủ.
:::

### 7.2. Thay cấu trúc của trang hỗ trợ

::: exercise
**Bài 5.4.1(a,c), MMDS §5.4.6, trang 203–204.** Lặp phân tích Hình 5.16 khi mỗi trang hỗ trợ (a) chỉ trỏ tới chính nó thay vì đích; (c) trỏ tới cả chính nó và đích.

Giữ đồ thị không nút cụt, dịch chuyển đều, $0<\beta<1$, $m\ge1$, $n\ge m+1$. Đích vẫn chỉ trỏ tới $m$ hỗ trợ; các hỗ trợ không nhận cạnh từ ngoài cụm; mọi cạnh ngoài vào cụm tới đích. $x$ đã nhân $\beta$ và chia bậc ra tại nguồn; $b=(1-\beta)/n$.

Trình bày phương trình của $p,y$, biểu thức $y$ theo $x,m,n,\beta$, và phân biệt nghiệm chính xác với xấp xỉ của sách.
:::

![Biến thể a: đích trỏ tới hỗ trợ, mỗi hỗ trợ chỉ có khuyên và không còn cạnh quay về đích.](img/lec-04/ho-tro-tu-khuyen.svg)

![Biến thể c: đích trỏ tới hỗ trợ, mỗi hỗ trợ có một khuyên và một cạnh quay về đích.](img/lec-04/ho-tro-khuyen-va-dich.svg)

::: hint
Trong (a), không còn dòng theo cạnh từ hỗ trợ về đích. Trong (c), hỗ trợ có hai cạnh ra nên mỗi cạnh nhận một nửa điểm theo liên kết của hỗ trợ.
:::

::: solution
(a) Hai phương trình là

$$p=\frac{\beta y}{m}+\beta p+b,\qquad y=x+b.$$

Suy ra $p=(\beta y/m+b)/(1-\beta)$. Nếu bỏ riêng bước dịch chuyển trực tiếp tới đích theo phép phân tích của sách thì $y\approx x$.

(c) Do mỗi hỗ trợ chia theo hai cạnh ra,

$$p=\frac{\beta y}{m}+\frac\beta2p+b,\qquad y=x+\frac{\beta m}{2}p+b.$$

Từ phương trình đầu, $(2-\beta)p=2\beta y/m+2b$. Thế vào phương trình đích:

$$(2-\beta)y=(2-\beta)(x+b)+\beta^2y+\beta mb.$$

Vì $2-\beta-\beta^2=(1-\beta)(2+\beta)>0$, nghiệm đầy đủ là

$$y=\frac{(2-\beta)(x+b)+\beta mb}{(1-\beta)(2+\beta)}.$$

Bỏ riêng $b$ trực tiếp tới đích cho

$$y\approx\frac{2-\beta}{(1-\beta)(2+\beta)}x+\frac\beta{2+\beta}\frac mn.$$

Phần dịch chuyển tại các hỗ trợ vẫn được giữ. Trong cả hai biến thể, khuyên khiến hỗ trợ nhận điểm từ chính nó; giả thiết phù hợp là không nhận cạnh từ ngoài cụm, không phải chỉ nhận cạnh từ đích.
:::

### 7.3. HITS trên chuỗi có khuyên

::: exercise
**Bài 5.5.2, MMDS §5.5.3, trang 208; Hình 5.9, trang 189.** Đồ thị có $n\ge1$ đỉnh, cạnh $1\to1$ và các cạnh $i\to i+1$ với $1\le i<n$. Tính các vector trung tâm và uy tín theo $n$.

Khởi tạo $h^0=a^0=\mathbf1$ và chuẩn hóa giá trị lớn nhất bằng $1$ sau mỗi phép nhân. Trình bày hai vector giới hạn, lập luận từ phép lặp hoặc ma trận, cùng hai trường hợp biên $n=1$, $n=2$.
:::

![Chuỗi có khuyên tại đỉnh 1 và cạnh i tới i cộng một; các đỉnh giữa được viết bằng dấu chấm lửng.](img/lec-04/chuoi-co-khuyen.svg)

::: hint
Với $n\ge2$, hàng 1 của $L$ có hai số $1$ tại cột 1 và 2; mỗi hàng giữa có một số $1$; hàng cuối bằng $0$. Các tập cột khác $0$ của các hàng khác nhau rời nhau.
:::

::: solution
Với $n\ge2$,

$$LL^\mathsf T=\operatorname{diag}(2,\underbrace{1,\ldots,1}_{n-2},0).$$

Từ $h^0=\mathbf1$, mỗi đỉnh nhận đúng một đóng góp nên $a^1=\mathbf1$. Trung tâm thô là $(2,1,\ldots,1,0)^\mathsf T$; chia cho $2$ cho $h^1=(1,1/2,\ldots,1/2,0)^\mathsf T$.

Giả sử $h^t=(1,2^{-t},\ldots,2^{-t},0)^\mathsf T$ với $t\ge1$. Đỉnh 1 và 2 đều nhận từ đỉnh 1, nên hai thành phần đầu của $a^{t+1}$ bằng $1$; các thành phần còn lại bằng $2^{-t}$. Trung tâm thô tiếp theo có thành phần đầu bằng $2$, các thành phần giữa bằng $2^{-t}$ và thành phần cuối bằng $0$. Sau chuẩn hóa, công thức quy nạp được giữ ở vòng $t+1$. Vì vậy,

$$h^t=(1,\underbrace{2^{-t},\ldots,2^{-t}}_{n-2},0)^\mathsf T,$$
$$a^t=(1,1,\underbrace{2^{-(t-1)},\ldots,2^{-(t-1)}}_{n-2})^\mathsf T\qquad(t\ge1).$$

Lấy giới hạn:

$$h^*=(1,0,\ldots,0)^\mathsf T,\qquad a^*=(1,1,0,\ldots,0)^\mathsf T.$$

Với $n=2$, các phần giữa rỗng; cặp giới hạn đạt ngay sau vòng thứ nhất. Với $n=1$, vẫn còn khuyên $1\to1$, nên $L=[1]$ và $h=a=(1)$ ở mọi vòng. Không có phép chia cho $0$ trong trường hợp này. Bỏ khuyên tại đỉnh 1 làm đổi ma trận, phép lặp và nghiệm của bài nguồn.
:::

## Tài liệu tham khảo

Jure Leskovec, Anand Rajaraman và Jeffrey D. Ullman, *Mining of Massive Datasets*, ấn bản 3, Chương 5: §5.3, trang 195–199; §5.4, trang 199–204; §5.5, trang 204–208. Ví dụ và hình được vẽ lại theo sách; các bảng PageRank/TrustRank dùng cùng $\beta=4/5$ như đã nêu ở §4.2. [Trang sách và slide chính thức MMDS](http://www.mmds.org).
