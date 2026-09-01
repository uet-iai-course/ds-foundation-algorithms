# Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Xem bộ trang chiếu tại [Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ](../../lecture-09-dong-du-lieu-dem-momen-va-cua-so.html).

Một dòng sự kiện có thể kéo dài không giới hạn, còn bộ nhớ làm việc chỉ giữ được một trạng thái nhỏ. Cùng một dòng nhưng mỗi câu hỏi đòi hỏi một trạng thái khác: số khóa phân biệt, tần suất của một khóa, độ tập trung của phân phối, số bit 1 gần đây hoặc tổng giảm trọng số theo tuổi.

Bài này trình bày bốn phác thảo chính: Flajolet–Martin, Count-Min Sketch, AMS và DGIM. Phần cuối bổ sung cửa sổ suy giảm mũ để xử lý dữ liệu gần đây mà không dùng một ranh giới cứng.

## 1. Chọn phác thảo theo câu hỏi

Giả sử mỗi phần tử của dòng có một khóa và một thời điểm đến. Bảng đếm chính xác cần một ô cho mỗi khóa phân biệt, còn cửa sổ chính xác có thể cần giữ toàn bộ $N$ bit gần nhất. Hai cách này không phù hợp khi số khóa hoặc độ dài cửa sổ vượt ngân sách bộ nhớ.

![Bản đồ chọn cấu trúc theo đại lượng cần ước lượng và phạm vi thời gian](img/lec-09/decision-map.svg)

Hai quyết định cần chốt trước khi chọn thuật toán là đại lượng cần trả lời và phạm vi thời gian của truy vấn.

| Câu hỏi | Phạm vi | Cấu trúc |
|---|---|---|
| Có bao nhiêu khóa phân biệt? | toàn dòng | Flajolet–Martin |
| Một khóa xuất hiện bao nhiêu lần? | toàn dòng chỉ tăng | Count-Min Sketch |
| Phân phối tần suất tập trung đến mức nào? | toàn dòng | AMS cho $F_2$ |
| Có bao nhiêu bit 1 trong hậu tố gần đây? | cửa sổ cứng | DGIM |
| Tổng có trọng số giảm theo tuổi là bao nhiêu? | gần đây | cửa sổ suy giảm mũ |

Mỗi cấu trúc có một hợp đồng riêng về đầu vào, sai số và xác suất thất bại. Không thể chuyển bảo đảm của cấu trúc này sang cấu trúc khác.

::: exercise Tự kiểm
Một hệ thống cần đếm số địa chỉ IP phân biệt từ đầu ngày và đồng thời đếm số cảnh báo trong 10.000 sự kiện gần nhất. Hai truy vấn này khác nhau ở hai trục nào?
:::

::: solution
Truy vấn thứ nhất hỏi $F_0$ trên toàn dòng; truy vấn thứ hai hỏi một tổng trong cửa sổ gần đây. Chúng cần hai trạng thái khác nhau, chẳng hạn Flajolet–Martin và DGIM nếu cảnh báo được mã hóa thành bit.
:::

## 2. Flajolet–Martin đếm số khóa phân biệt

### Đặc tả

Đầu vào là dòng khóa và một hàm băm $h$ cho từ bit dài $L$. Cùng một khóa phải luôn nhận cùng giá trị băm. Với từ bit $y$, ký hiệu $\rho(y)$ là số bit 0 liên tiếp ở cuối. Trạng thái $R$ là giá trị $\rho$ lớn nhất đã thấy.

Với băm hữu hạn, bài này dùng quy ước $\rho(0)=L$. Dòng rỗng trả $0$; vì thế có thể khởi tạo $R=-\infty$ để phân biệt dòng rỗng với dòng không rỗng có $R=0$. Đây là quy ước biên của bài, không phải mệnh đề trích nguyên từ MMDS.

```text
FLAJOLET-MARTIN(x, h, R)
  r <- rho(h(x))
  R <- max(R, r)
  trả R

TRUY-VẤN(R)
  nếu dòng rỗng: trả 0
  ngược lại: trả 2^R
```

Điều kiện sau mỗi cập nhật: $R$ đúng bằng độ dài đuôi 0 lớn nhất trong các giá trị băm của những khóa đã thấy.

### Ví dụ chạy tay và lập luận ngưỡng

![Vết băm bốn khóa với số bit 0 liên tiếp ở cuối mỗi giá trị](img/lec-09/fm-trace.svg)

Trong mô hình băm lý tưởng, giá trị băm của các khóa phân biệt là đều và độc lập. Với $r\le L$,

$$\Pr[\rho(h(x))\ge r]=2^{-r}.$$

Nếu có $m$ khóa phân biệt thì

$$\Pr[\text{không khóa nào đạt }r]=(1-2^{-r})^m\approx e^{-m2^{-r}}.$$

Khi $m\gg 2^r$, ta gần như sẽ thấy một đuôi dài ít nhất $r$. Khi $m\ll 2^r$, xác suất đó nhỏ. Ngưỡng xuất hiện vì thế nằm quanh $m\approx2^r$, dẫn đến ước lượng thô $2^R$.

Lập luận này không chứng minh $2^R$ không chệch. Một đuôi hiếm nhưng rất dài có thể làm ước lượng tăng mạnh; phân phối của ước lượng đơn có đuôi nặng.

### Gộp nhiều bản sao

MMDS dùng thứ tự: chia các hàm băm thành nhóm, lấy trung bình $2^R$ trong từng nhóm, rồi lấy trung vị của các trung bình nhóm. Không đảo thứ tự hai phép gộp.

Ví dụ, ba nhóm có các ước lượng $(4,8)$, $(8,16)$ và $(2,4)$. Trung bình nhóm là $6,12,3$; trung vị cuối là $6$.

Với $q$ bản sao, cập nhật tốn $O(q)$ thời gian. Mỗi bản sao giữ một cực đại trong $[0,L]$, cần $O(\log L)$ bit, ngoài phần biểu diễn hoặc cố định hàm băm. Chất lượng phụ thuộc họ băm, số bản sao và cách chia nhóm.

::: exercise Tự kiểm
Vì sao một khóa xuất hiện một triệu lần vẫn chỉ đóng góp một giá trị băm cho Flajolet–Martin?
:::

::: solution
Hàm băm được cố định theo khóa. Mọi lần xuất hiện của cùng khóa cho cùng $h(x)$ và cùng $\rho(h(x))$, nên chỉ số $R$ không tăng vì lặp khóa.
:::

## 3. Count-Min Sketch ước lượng tần suất

### Đặc tả

Flajolet–Martin trả số khóa phân biệt. Nếu cần tần suất $f_x$ của một khóa cụ thể nhưng không thể giữ bộ đếm cho mọi khóa, ta dùng Count-Min Sketch.

Phần này xét dòng chỉ tăng: mỗi cập nhật $(x,\Delta)$ có $\Delta\ge0$. Đặt $n=\lVert f\rVert_1=\sum_x f_x$. Theo tham số hóa trong UMass CS514 Lecture 10, chọn $k\ge1$, $0<\varepsilon\le1$, $0<\delta<1$ và

$$m=\left\lceil\frac{2k}{\varepsilon}\right\rceil,
\qquad
t=\left\lceil\log_2\frac1\delta\right\rceil.$$

Bảng $C$ có $t$ hàng, mỗi hàng $m$ ô, khởi tạo bằng 0. Mỗi $h_j:U\to\{0,\dots,m-1\}$ được chọn từ một họ băm độc lập đôi một; các hàng độc lập với nhau.

```text
CẬP-NHẬT-COUNT-MIN(x, Delta)
  với j = 1,...,t:
    C[j, h_j(x)] <- C[j, h_j(x)] + Delta

TRUY-VẤN-COUNT-MIN(x)
  trả min_j C[j, h_j(x)]
```

### Ví dụ va chạm

![Ba hàng Count-Min cho một khóa có tần suất thật 6 và nhiễu va chạm 3, 1, 5](img/lec-09/count-min.svg)

Giả sử $f_x=6$. Ba ô được hỏi chứa lần lượt $9,7,11$, nên $\widehat f_x=7$. Vì mọi cập nhật đều không âm, mỗi ô chứa $f_x$ cộng với nhiễu va chạm; do đó $\widehat f_x\ge f_x$.

### Từ nhiễu kỳ vọng đến bảo đảm

Đặt $Y_j=C[j,h_j(x)]-f_x$. Với một hàng, mỗi khóa $y\ne x$ va chạm với $x$ với xác suất $1/m$. Băm độc lập đôi một đủ để tính

$$\mathbb E[Y_j]\le\frac{n}{m}\le\frac{\varepsilon n}{2k}.$$

Do $Y_j\ge0$, bất đẳng thức Markov cho

$$\Pr\left[Y_j\ge\frac{\varepsilon n}{k}\right]\le\frac12.$$

Các hàng độc lập và truy vấn lấy giá trị nhỏ nhất. Xác suất mọi hàng đều xấu không quá $2^{-t}\le\delta$. Với một khóa $x$ cố định, xác suất ít nhất $1-\delta$ cho bảo đảm

$$f_x\le\widehat f_x\le f_x+\frac{\varepsilon n}{k}.$$

Cập nhật và truy vấn tốn $O(t)$ thời gian; bảng cần $O(mt)$ bộ đếm. Bảo đảm chỉ dùng cho dòng chỉ tăng. Phác thảo cũng không tự sinh danh sách khóa nặng: nếu cần mọi khóa nặng, phải có thêm cơ chế duy trì ứng viên.

::: exercise Tự kiểm
Vì sao cập nhật âm làm mất lập luận $\widehat f_x\ge f_x$?
:::

::: solution
Một ô chứa tổng của nhiều khóa. Khi một khóa khác bị trừ, ô có thể giảm dù $f_x$ không giảm. Quan hệ “giá trị thật cộng nhiễu không âm” không còn đúng.
:::

## 4. Mômen đo độ tập trung

Gọi $f_i$ là tần suất của khóa $i$. Mômen bậc $p$ là

$$F_p=\sum_i f_i^p.$$

$F_0$ là số khóa phân biệt; dùng quy ước $0^0=0$, tương đương chỉ đếm khóa có tần suất dương. $F_1$ là độ dài dòng. $F_2$ đo mức tập trung của tần suất.

MMDS cho hai phân phối cùng độ dài nhưng khác mức tập trung:

$$10^2+10\cdot9^2=910,$$

$$90^2+10\cdot1^2=8110.$$

Một truy vấn Count-Min chỉ cho tần suất của khóa được hỏi; $F_2$ tóm tắt cả phân phối.

## 5. Biến AMS không chệch cho $F_2$

### Ví dụ hậu tố

MMDS xét dòng độ dài $n=15$:

$$a,b,c,b,d,a,c,d,a,b,d,c,a,a,b.$$

Chọn đều một vị trí $I$. Gọi $c_I$ là số lần khóa tại vị trí $I$ xuất hiện trong hậu tố từ $I$ đến cuối dòng. Ba vị trí minh họa cho $c_I=3,2,2$.

![Ba vị trí chọn trên dòng độ dài 15 và các bộ đếm hậu tố tương ứng](img/lec-09/ams-trace.svg)

Với $X=n(2c_I-1)$, ba giá trị là $75,45,45$, có trung bình $55$. Giá trị thật của dòng là $F_2=59$. Một vài biến có thể lệch; bảo đảm của AMS nằm ở kỳ vọng.

```text
AMS-MỘT-BIẾN(I)
  khi đến vị trí I:
    lưu khóa e(I)
    c <- 1
  với mỗi phần tử sau I:
    nếu phần tử bằng e(I): c <- c + 1
  khi truy vấn:
    trả n(2c - 1)
```

### Chứng minh tính không chệch

**Mệnh đề.** Nếu $I$ được chọn đều trong $\{1,\dots,n\}$ và $c_I$ được đếm đúng thì $\mathbb E[X]=F_2$.

Xét một khóa $a$ xuất hiện $f_a$ lần. Nếu đọc các vị trí của $a$ từ cuối về đầu, các giá trị $c_I$ là $1,2,\dots,f_a$. Vì tổng $f_a$ số lẻ đầu tiên bằng $f_a^2$,

$$
\mathbb E[X]
=\frac1n\sum_{I=1}^n n(2c_I-1)
=\sum_a\left(1+3+\cdots+(2f_a-1)\right)
=\sum_a f_a^2
=F_2.
$$

Giả thiết chọn đều được dùng ở hệ số $1/n$; giả thiết đếm đúng hậu tố được dùng khi thay các $c_I$ bằng dãy $1,\dots,f_a$.

### Duy trì khi chưa biết độ dài dòng

Khi phần tử thứ $r$ đến, mỗi bản sao dùng lấy mẫu hồ chứa kích thước 1:

```text
với mỗi bản sao:
  với xác suất 1/r:
    thay khóa đang giữ bằng khóa mới
    đặt c <- 1
  nếu không thay và khóa mới bằng khóa đang giữ:
    c <- c + 1
  nếu không thay và khóa mới khác khóa đang giữ:
    giữ nguyên c
```

Sau bước $r$, mỗi vị trí có xác suất $1/r$ được chọn. Với $q$ bản sao độc lập, cập nhật tốn $O(q)$ thời gian và giữ $q$ khóa cùng $q$ bộ đếm. Không cần bảng đếm cho mọi khóa.

::: exercise Tự kiểm
Nếu không thay mẫu nhưng khóa mới trùng khóa đang giữ, vì sao phải tăng $c$?
:::

::: solution
$c$ phải đếm mọi lần khóa được chọn xuất hiện từ vị trí lấy mẫu đến cuối tiền tố. Bỏ lần trùng này làm biến AMS sai.
:::

## 6. DGIM biểu diễn cửa sổ bit

Đầu vào là dòng bit, độ dài cửa sổ $N$ và truy vấn số bit 1 trong $k$ vị trí gần nhất, với $1\le k\le N$. Biểu diễn chính xác mọi truy vấn hậu tố có thể cần $N$ bit. DGIM giảm bộ nhớ bằng cách gom các bit 1 thành bucket.

Mỗi bucket lưu kích thước $1,2,4,\dots$, bằng số bit 1 mà bucket đại diện, và mốc phải, là thời điểm của bit 1 mới nhất trong bucket. Bucket không phải một đoạn vị trí liên tục: giữa các bit 1 có thể có bit 0.

![Một trạng thái DGIM hợp lệ với kích thước bucket không giảm khi đi về quá khứ](img/lec-09/dgim-buckets.svg)

Sáu bất biến là:

1. đầu phải của mỗi bucket là một bit 1;
2. mọi bit 1 trong cửa sổ thuộc đúng một bucket;
3. không vị trí nào thuộc hai bucket;
4. kích thước bucket là lũy thừa của 2;
5. mỗi kích thước có một hoặc hai bucket;
6. đi từ mới về cũ, kích thước bucket không giảm.

Vì có $O(\log N)$ kích thước và tối đa hai bucket cho mỗi kích thước, tổng số bucket là $O(\log N)$.

```text
CẬP-NHẬT-DGIM(bit, thời_điểm)
  loại bucket cũ nhất nếu mốc phải đã ra ngoài cửa sổ N
  nếu bit = 0: trả
  tạo một bucket kích thước 1 tại thời điểm hiện tại
  khi có 3 bucket cùng kích thước:
    gộp hai bucket cũ nhất
    giữ mốc phải của bucket mới hơn trong hai bucket được gộp
```

Mỗi lần gộp làm kích thước tăng gấp đôi, nên dừng sau nhiều nhất $O(\log N)$ mức. Nếu viết dãy kích thước từ cũ đến mới:

$$1,1,1\longrightarrow2,1,$$

$$2,2,2,1\longrightarrow4,2,1,$$

$$4,4,4,2,1\longrightarrow8,4,2,1.$$

Luôn gộp hai bucket cũ nhất trong ba bucket cùng kích thước.

## 7. Truy vấn, sai số và chi phí DGIM

Với hậu tố độ dài $k$, tìm bucket cũ nhất $b^*$ có mốc phải nằm trong hậu tố. Cộng đủ mọi bucket mới hơn và cộng một nửa bucket biên:

$$\widehat c(k)=A+\frac{|b^*|}{2},
\qquad
A=\sum_{b\text{ mới hơn }b^*}|b|.$$

Nếu không có mốc phải nào trong hậu tố, trả $0$.

![Ranh giới mười bit gần nhất và bucket biên kích thước 4](img/lec-09/dgim-query-10.svg)

Trong ví dụ MMDS, bucket biên có kích thước $4$; các bucket mới hơn có kích thước $2,1,1$. Vì vậy

$$\widehat c(10)=\frac42+2+1+1=6,$$

trong khi số thật là $5$.

### Chứng minh cận sai số 50%

Nếu số thật $c=0$, thuật toán trả $0$. Xét $c>0$. Đặt $s=|b^*|$. Do mỗi kích thước có một hoặc hai bucket và kích thước không giảm khi đi về quá khứ, các bucket mới hơn có tổng ít nhất

$$A\ge1+2+\cdots+\frac{s}{2}=s-1.$$

Hậu tố chứa ít nhất bit 1 tại mốc phải của $b^*$, nên $c\ge A+1\ge s$.

Gọi $r$ là số bit 1 của $b^*$ thực sự nằm trong hậu tố. Khi đó

$$c=A+r,\qquad1\le r\le s,$$

trong khi $\widehat c=A+s/2$. Dù ước lượng cao hay thấp,

$$|\widehat c-c|\le\frac{s}{2}.$$

Vì $c\ge s$,

$$\frac{|\widehat c-c|}{c}\le\frac{s/2}{c}\le\frac12.$$

Do đó

$$\frac12c\le\widehat c\le\frac32c.$$

DGIM có $O(\log N)$ bucket. Mỗi bucket cần $O(\log N)$ bit để lưu kích thước và mốc thời gian modulo $N$, nên tổng bộ nhớ là $O(\log^2N)$ bit. Cập nhật có chi phí xấu nhất $O(\log N)$, nhưng số lần gộp khấu hao là $O(1)$. Truy vấn duyệt $O(\log N)$ bucket.

::: exercise Tự kiểm
Vì sao bộ nhớ DGIM là $O(\log^2N)$ bit chứ không phải $O(\log N)$ bit?
:::

::: solution
Có $O(\log N)$ bucket, nhưng mỗi bucket cần $O(\log N)$ bit để lưu kích thước và mốc thời gian. Nhân hai đại lượng cho $O(\log^2N)$ bit.
:::

## 8. Cửa sổ suy giảm mũ

DGIM dùng một biên cứng: dữ liệu bên ngoài cửa sổ không còn đóng góp. Với độ phổ biến gần đây, ta có thể muốn sự kiện cũ giảm ảnh hưởng dần thay vì biến mất đột ngột.

![So sánh trọng số của cửa sổ cứng và cửa sổ suy giảm mũ](img/lec-09/window-weights.svg)

Với dòng số $a_1,a_2,\dots$ và $0<c<1$, định nghĩa

$$S_t=\sum_{i=0}^{t-1}a_{t-i}(1-c)^i.$$

Nếu mọi $a_i=1$, tổng trọng số hữu hạn là

$$\sum_{i=0}^{t-1}(1-c)^i=\frac{1-(1-c)^t}{c},$$

và chỉ tiến tới $1/c$ khi $t\to\infty$.

Tách hạng mới nhất cho truy hồi

$$
\begin{aligned}
S_{t+1}
&=a_{t+1}+\sum_{i=1}^{t}a_{t+1-i}(1-c)^i\\
&=a_{t+1}+(1-c)\sum_{j=0}^{t-1}a_{t-j}(1-c)^j\\
&=a_{t+1}+(1-c)S_t.
\end{aligned}
$$

Với một tổng, cập nhật và bộ nhớ đều là $O(1)$.

::: exercise Tự kiểm
Nếu $a_t=1$ với mọi $t$ và $c=1/2$, dãy $S_t$ tiến tới giá trị nào?
:::

::: solution
$S_t=2(1-2^{-t})$, nên dãy tiến tới $1/c=2$.
:::

## 9. So sánh các hợp đồng

| Cấu trúc | Đầu ra | Điều kiện chính | Cập nhật | Trạng thái | Bảo đảm hoặc giới hạn |
|---|---|---|---|---|---|
| Flajolet–Martin | $F_0$ | băm khóa đều, độc lập | $O(q)$ | $q$ cực đại đuôi băm | ước lượng đơn có đuôi nặng; gộp trung bình rồi trung vị |
| Count-Min Sketch | $f_x$ | dòng chỉ tăng | $O(t)$ | $mt$ bộ đếm | cận trên một phía cho khóa cố định với xác suất ít nhất $1-\delta$ |
| AMS | $F_2$ | vị trí được chọn đều | $O(q)$ | $q$ khóa và bộ đếm hậu tố | không chệch theo kỳ vọng; một biến có thể dao động mạnh |
| DGIM | số bit 1 trong hậu tố | dòng bit, $1\le k\le N$ | $O(\log N)$ xấu nhất, $O(1)$ khấu hao | $O(\log^2N)$ bit | sai số tương đối không quá 50% khi $c>0$ |
| Cửa sổ suy giảm mũ | tổng theo tuổi | $0<c<1$ | $O(1)$ | một tổng | chính xác theo định nghĩa; không phải cửa sổ cứng |

Kết quả chỉ có ý nghĩa khi đi kèm điều kiện áp dụng. FM cần mô hình băm và phép gộp đúng; Count-Min cần dòng chỉ tăng; AMS đúng theo kỳ vọng; DGIM xấp xỉ một hậu tố bit; cửa sổ suy giảm dùng tổng hữu hạn trước khi lấy giới hạn $1/c$.

## 10. Bài tập từ MMDS

Các bài dưới đây giữ nguyên dữ kiện và yêu cầu của MMDS. Phần lời giải được trình bày để tự kiểm.

::: exercise
**Bài tập 4.4.1 (tr.145).** Cho dòng $3,1,4,1,5,9,2,6,5$. Xem kết quả băm là số nhị phân 5 bit. Với mỗi hàm sau, tính độ dài đuôi cho từng phần tử, tìm $R$ và ước lượng $2^R$:

1. $h_1(x)=2x+1\pmod{32}$;
2. $h_2(x)=3x+7\pmod{32}$;
3. $h_3(x)=4x\pmod{32}$.
:::

::: solution
| $x$ | 3 | 1 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| $\rho(h_1(x))$ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $\rho(h_2(x))$ | 4 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| $\rho(h_3(x))$ | 2 | 2 | 4 | 2 | 2 | 2 | 3 | 3 | 2 |

Ba cực đại là $0,4,4$, nên ba ước lượng là $1,16,16$.
:::

::: exercise
**Bài tập 4.5.1 (tr.150).** Với dòng $3,1,4,1,3,4,2,1,2$, lập bảng tần suất rồi tính mômen bậc hai và bậc ba.
:::

::: solution
Các tần suất là $f_1=3$ và $f_2=f_3=f_4=2$. Vì vậy

$$F_2=3^2+3\cdot2^2=21,
\qquad
F_3=3^3+3\cdot2^3=51.$$
:::

::: exercise
**Bài tập 4.5.3 (tr.150).** Với dòng của Bài tập 4.5.1, tại mỗi vị trí $i=1,\dots,9$, tính $c_i$: số lần khóa ở vị trí $i$ xuất hiện từ vị trí $i$ đến cuối dòng. Sản phẩm là một hàng gồm chín giá trị $c_i$ theo đúng thứ tự; không cần tính $X_i$.
:::

::: solution
Đọc từng hậu tố cho

$$c_i=[2,3,2,2,1,1,2,1,1].$$

Ta có $\sum_i c_i=15$. Nếu tính thêm để tự kiểm,

$$\frac19\sum_{i=1}^9 9(2c_i-1)=2\sum_i c_i-9=21,$$

khớp với $F_2$ ở bài trước.
:::

::: exercise
**Bài tập 4.6.1 (tr.157).** Trên trạng thái DGIM của Hình 4.2, ước lượng số bit 1 trong $k=5$ và $k=15$ vị trí cuối. So sánh với số thật và báo sai lệch.

![Trạng thái DGIM với hai ranh giới truy vấn k bằng 5 và k bằng 15, không hiển thị đáp án](img/lec-09/dgim-exercise.svg)
:::

::: solution
- Với $k=5$, ước lượng là $3$, đúng bằng số thật.
- Với $k=15$, ước lượng là $10$, số thật là $9$. Sai lệch là $+1$ và sai số tương đối là $1/9$.
:::

::: exercise
**Bài tập 4.6.3 (tr.157).** Bắt đầu từ trạng thái Hình 4.3 dưới đây. Thêm lần lượt ba bit 1. Sau mỗi lần, ghi dãy kích thước bucket từ cũ đến mới và mọi phép gộp. Giả sử các bit 1 đang thấy chưa rời cửa sổ.

![Trạng thái đầu DGIM từ cũ đến mới với phần trái chưa xác định và đuôi bucket 4, 4, 2, 2, 1](img/lec-09/dgim-cascade-exercise.svg)
:::

::: solution
Đuôi trạng thái đầu là $\dots,4,4,2,2,1$.

- Sau bit 1 thứ nhất: $\dots,4,4,2,2,1,1$.
- Sau bit 1 thứ hai: ba bucket kích thước 1 gây gộp lan qua kích thước 2 và 4, cho $\dots,8,4,2,1$.
- Sau bit 1 thứ ba: $\dots,8,4,2,1,1$.

Mỗi lần gộp giữ mốc phải của bucket mới hơn trong hai bucket được gộp. Phần trái của hình không xác định hoàn toàn: nếu trước đó đã có hai bucket kích thước 8, bucket 8 vừa tạo sẽ tiếp tục gây gộp lên 16, rồi có thể lan lên mức cao hơn.
:::

## Tóm tắt nguồn

- Leskovec, Rajaraman và Ullman, *Mining of Massive Datasets*, Chương 4, mục 4.4–4.7, tr.142–159.
- Slide MMDS *Data Streams 1–2*; slide Stanford CS246 2017 được dùng để đối chiếu thứ tự gộp Flajolet–Martin và diễn đạt DGIM.
- UMass CS514 Lecture 10 là nguồn cho Count-Min Sketch và tham số hóa dùng trong bài.
- Bài tập: MMDS 4.4.1, 4.5.1, 4.5.3, 4.6.1 và 4.6.3.

HyperLogLog chuẩn, Count-Min có cập nhật âm, thuật toán sinh khóa nặng, DGIM với sai số tùy ý và duy trì suy giảm cho nhiều khóa nằm ngoài phạm vi bài này.
