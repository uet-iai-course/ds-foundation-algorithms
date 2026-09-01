# Tìm cặp tương đồng bằng băm nhạy cảm cục bộ

Xem bộ slide tại [Bài 06 — Tìm cặp tương đồng bằng băm nhạy cảm cục bộ](../../lecture-06-tim-cap-tuong-dong-bang-lsh.html). Ghi chú này phát triển các đặc tả, ví dụ và lập luận để đọc độc lập; không chép lại trang chiếu.

## Mục tiêu và kiến thức tiên quyết

Sau bài này, người học có thể:

- Giải thích vì sao nén chữ ký chưa giải quyết số cặp, dùng Ví dụ 3.10 để tính quy mô.
- Chia chữ ký $p=br$ thành $b$ dải, tạo khóa `(chỉ-số-dải, vector đầy đủ)` và suy ra $q(s)=1-(1-s^r)^b$.
- Tính Ví dụ 3.12, ngưỡng nửa chính xác và hướng đổi $b,r$ khi $p$ cố định.
- Đặc tả thuật toán tạo tập ứng viên không thứ tự, chứng minh bất biến, hậu kiểm và phân biệt $bN+A$ bản ghi với $\Theta(pN+A)$ từ.
- Phát biểu họ LSH bằng hai ngưỡng gần–xa, hai cận xác suất và không gán bảo đảm cho vùng giữa.
- Suy ra phép khuếch đại AND/OR dưới giả thiết độc lập và giữ đúng thứ tự ghép trong Bài 3.6.1.
- Phân biệt miền, nguồn ngẫu nhiên, xác suất va chạm và trường hợp biên của Hamming, cosin, Euclid.
- Tính xác suất mô hình vân tay và phân biệt mô hình sách với bằng chứng hiệu năng hiện thời.

Kiến thức tiên quyết: tập shingle, độ tương đồng Jaccard $s$, chữ ký MinHash và $\Pr[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2)$; xác suất độc lập, tích vô hướng, góc giữa vector, khoảng cách Hamming và Euclid; mô hình MapReduce.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N$ | số đối tượng hoặc cột chữ ký |
| $p=br$ | số hàng chữ ký; $b$ dải, mỗi dải $r$ hàng |
| $s$ | độ tương đồng Jaccard thực của một cặp |
| $\rho$ | xác suất va chạm cơ sở của một cặp cố định dưới một hàm băm |
| $q(s)$ | xác suất một cặp có độ tương đồng $s$ trở thành ứng viên |
| $C$ | tập cặp ứng viên đã loại trùng |
| $A$ | số lượt sinh cặp trước loại trùng, $A=\sum_B\binom{|B|}{2}$ |
| $\tau$ | ngưỡng đối chiếu hậu kỳ |
| $F$ | phân phối trên họ hàm băm; $h\sim F$ |
| $\alpha_1,\alpha_2$ | cận xác suất va chạm, $\alpha_1>\alpha_2$ |
| $d_1,d_2$ | ngưỡng gần và xa, $d_1<d_2$ |
| $m$ | số chiều của vector Hamming hoặc cosin |
| $u$ | độ dịch ngẫu nhiên của các ngăn Euclid, $u\sim U[0,a)$ |

## 1. Chữ ký ngắn, số cặp vẫn lớn

### Vai trò

Bài 05 đã đưa mỗi tài liệu về chữ ký MinHash $p$ hàng. Chữ ký làm biểu diễn nhỏ hơn nhưng không làm giảm số cặp cần so sánh. Bài này xây một tầng lọc xác suất, gọi là băm nhạy cảm cục bộ (LSH), để giảm số cặp trước khi đối chiếu.

### Ví dụ 3.10: một gigabyte, nhưng sáu ngày

::: example Ví dụ quy mô
Giả sử có $N=10^6$ tài liệu, mỗi tài liệu có chữ ký $p=250$ số nguyên 4 byte. Mỗi chữ ký chiếm $250\cdot4=1000$ byte; toàn bộ chiếm khoảng $10^6$ KB, tức gần 1 GB. Số cặp là

$$\binom N2=\frac{N(N-1)}2=\frac{10^6(10^6-1)}2\approx4.999995\cdot10^{11}.$$

Nếu một phép tính độ tương đồng của một cặp chữ ký mất 1 microgiây, cả kết quả mất gần sáu ngày. Nút thắt là số cặp, không phải dung lượng lưu trữ. Nguồn: MMDS Ví dụ 3.10, §3.4.

Hình dưới minh họa chuỗi từ lưu chữ ký đến số cặp.
:::

![Một triệu chữ ký tạo gần năm trăm tỷ cặp, trong khi lưu chữ ký chỉ cần khoảng một gigabyte.](img/lec-06/quy-mo.svg)

### Phân biệt giảm chiều với giảm số cặp

Shingling và MinHash làm mỗi tài liệu ngắn hơn; chúng giảm chiều của biểu diễn nhưng không đụng tới $\binom N2$ cặp. Tìm cặp tương đồng yêu cầu giảm số cặp phải xử lý, đó là công việc của LSH. Không có cách nào tránh đối chiếu mọi cặp nếu mục tiêu là tính độ tương đồng của toàn bộ cặp; nhưng nếu chỉ cần các cặp có độ tương đồng từ $\tau$ trở lên thì có thể bỏ qua sớm những cặp khó có khả năng đạt ngưỡng.

::: exercise Tự kiểm
Nếu $N$ tăng từ $10^6$ lên $2\cdot10^6$, số cặp tăng gần bao nhiêu lần?
:::

::: solution
Từ $N(N-1)/2$ lên $2N(2N-1)/2$; tỷ số ~ $4$ khi $N$ lớn, nên số cặp tăng gần bốn lần.
:::

## 2. Phân dải và khóa đầy đủ

### Vai trò

Ta cần một điều kiện rẻ để quyết định cặp có là ứng viên hay không, mà vẫn ưu tiên cặp giống nhau. Phân dải nhóm các hàng chữ ký lại và yêu cầu trùng toàn bộ một nhóm.

### Đặc tả

Chia ma trận chữ ký $\Sigma\in V^{p\times N}$ với $p=br$ thành $b$ dải, mỗi dải $r$ hàng. Với mỗi dải $\ell$ và mỗi cột $i$, vector dải là phần chữ ký từ hàng $(\ell-1)r+1$ đến $\ell r$. Một cặp không thứ tự $\{i,j\}$ trở thành ứng viên nếu tồn tại dải $\ell$ sao cho hai vector dải của $i$ và $j$ bằng nhau:

$$\{i,j\}\in C\iff \exists \ell\in\{1,\ldots,b\}:\ \Sigma_{(\ell-1)r+1:\ell r,i}=\Sigma_{(\ell-1)r+1:\ell r,j}.$$

Tập $C$ là tập cặp không thứ tự, đã loại trùng. Điều kiện này không khẳng định độ tương đồng cuối cùng đạt $\tau$; đó là nhiệm vụ của đối chiếu hậu kỳ.

### Ví dụ 3.11: chạy tay phép phân dải

::: example Ba chữ ký, mỗi chữ ký sáu hàng
Chia thành ba dải, mỗi dải hai hàng:

| Dải | $D_1$ | $D_2$ | $D_3$ |
|---|---|---|---|
| 1 | (2,5) | (2,8) | (7,5) |
| 2 | (4,1) | (4,1) | (4,9) |
| 3 | (6,3) | (0,3) | (6,9) |

Chỉ $\{D_1,D_2\}$ trùng trọn dải 2 nên là ứng viên. $D_1,D_3$ và $D_2,D_3$ có một vài tọa độ bằng nhau nhưng không có vector dải nào bằng nhau, nên không phải ứng viên. Ví dụ này thu gọn cách chia $12$ hàng thành bốn dải trong MMDS Ví dụ 3.11, nhưng giữ nguyên nguyên tắc: trùng trọn một dải là đủ để trở thành ứng viên.
:::

### Khóa dải đầy đủ

Khóa của một dải phải gồm chỉ số dải và toàn bộ vector $r$ hàng: $(\ell,\text{vector})$. Nếu triển khai bằng cách băm khóa về một mã rút gọn để tìm ngăn, bảng ngăn vẫn phải kiểm tra lại khóa đầy đủ sau khi mã va chạm; hai vector khác nhau vào cùng mã không được gộp thành một ngăn. Nguồn: MMDS §3.4.1.

![Khóa gồm số dải và toàn bộ vector của dải, không chỉ mã rút gọn.](img/lec-06/khoa-band.svg)

### Lập luận bao phủ

Nếu hai cột trùng toàn bộ dải $\ell$, chúng phát ra cùng khóa $(\ell,\text{vector})$, vào cùng ngăn. Khi liệt kê mọi cặp trong ngăn, cặp đó được thêm vào $C$. Vì vậy mọi cặp thỏa điều kiện phân dải đều xuất hiện trong $C$. Lập luận này không nói gì về cặp không thỏa điều kiện; phần xác suất sẽ định lượng xác suất bỏ sót.

### Trường hợp biên

- $r=1$: chỉ cần trùng một hàng, nhiều ứng viên, dương tính giả cao.
- $b=1$: phải trùng toàn bộ chữ ký, ít ứng viên, âm tính giả cao.

Với $p=br$ cố định, tăng $r$ và giảm $b$ làm $q(s)$ giảm trên $0<s<1$; điều này giảm dương tính giả nhưng tăng xác suất bỏ sót ở mọi mức chưa bằng 1. Phần sau định lượng bằng $q(s)$.

::: exercise Tự kiểm
Vì sao mỗi kết quả "không" phải vào một ngăn đơn riêng, thay vì gom mọi kết quả "không" vào chung một ngăn?
:::

::: solution
Ngăn đơn "không" đặt mỗi thực thể vào ngăn riêng nên ngăn nào cũng chứa một phần tử, không sinh cặp nào. Gom chúng chung một ngăn làm mọi cặp trong ngăn thành ứng viên, tức toàn bộ cặp không liên quan.
:::

## 3. Xác suất trở thành ứng viên và ngưỡng

### Vai trò

Cố định một cặp có độ tương đồng Jaccard $s$. Ta cần xác suất cặp này trùng ít nhất một dải; đây là đại lượng theo cặp, không phải tỷ lệ lỗi của kho.

### Giả thiết độc lập và xác suất một dải

Mỗi hàng MinHash trùng với xác suất $s$. Trong một dải có $r$ hàng; nếu các hàng độc lập, xác suất trùng toàn bộ dải là $s^r$. Xác suất không trùng dải $\ell$ là $1-s^r$. Độc lập giữa các hàng là điều kiện cho phép nhân; tái sử dụng các hàng phụ thuộc nhau làm đẳng thức không còn đúng.

### Công thức ứng viên

Xác suất không dải nào trùng là $(1-s^r)^b$. Biến cố bù cho xác suất có ít nhất một dải trùng:

$$q(s)=1-(1-s^r)^b.$$

Xác suất $q(s)$ là biên theo mô hình: trong dải đóng góp $s^r$ (độc lập), giữa các dải đóng góp lũy thừa $b$ (độc lập). Khóa dải được so bằng toàn bộ vector. Nguồn: MMDS §3.4.2.

::: derivation Chứng minh bù
Gọi $A_\ell$ là biến cố "dải $\ell$ trùng toàn bộ". Với cặp có độ tương đồng $s$ và các hàng độc lập, $\Pr[A_\ell]=s^r$. Các dải dùng các nhóm hàng rời nhau nên các $A_\ell$ độc lập:

$$\Pr[\text{ít nhất một dải trùng}]=\Pr\left[\bigcup_\ell A_\ell\right]=1-\Pr\left[\bigcap_\ell \overline{A_\ell}\right]=1-\prod_\ell(1-s^r)=1-(1-s^r)^b.$$
:::

### Ví dụ 3.12: $b=20,r=5,s=0.8$

::: example Ví dụ tính
Một dải trùng với xác suất $0.8^5=0.32768$. Không dải nào trùng với $(1-0.8^5)^{20}\approx0.00035$. Xác suất có ít nhất một dải trùng:

$$q(0.8)=1-(1-0.8^5)^{20}\approx0.99965.$$

Cặp tương đồng 0.8 bị bỏ sót với xác suất khoảng 0.00035, gần 1 trên 2800. Nguồn: MMDS Ví dụ 3.12, §3.4.2.
:::

Với $b>1$ và $r>1$, $q(s)$ có dạng chữ S: thấp dưới ngưỡng, dốc ở giữa, cao trên ngưỡng. Nếu $b=1$ hoặc $r=1$, đường cong không còn đủ hai phía phẳng để có dạng chữ S rõ. Hình dưới minh họa trường hợp $b,r>1$.

![Xác suất trở thành ứng viên q theo độ tương đồng s có dạng chữ S khi b và r đều lớn hơn một.](img/lec-06/duong-cong-s.svg)

### Ngưỡng nửa chính xác

Ngưỡng nửa $s_{1/2}$ là giá trị $s$ làm $q(s)=1/2$:

$$1-(1-s^r)^b=\tfrac12\iff (1-s^r)^b=\tfrac12\iff s^r=1-2^{-1/b}\iff s=(1-2^{-1/b})^{1/r}.$$

Đây là điểm chuyển của bộ lọc, không phải ngưỡng quyết định cuối; ngưỡng cuối vẫn là $\tau$ ở bước đối chiếu. Với $b$ lớn, khai triển bậc một cho $s_{1/2}\approx(\ln2/b)^{1/r}$; dạng $(1/b)^{1/r}$ trong một số slide chỉ là quy tắc rất thô. Nguồn: suy ra từ MMDS §3.4.2.

### Chọn $b,r$ dưới ràng buộc $p=br$

Chọn ngưỡng hậu kiểm $\tau$. Với mỗi ước $r$ của $p$, đặt $b=p/r$, rồi so $q(\tau)$, xác suất dưới $\tau$ và chi phí ứng viên. Khi giữ $p$ cố định, tăng $r$ và giảm $b$ làm $q(s)$ giảm với mọi $0<s<1$. Điều này giảm kỳ vọng dương tính giả nhưng tăng xác suất bỏ sót ở mọi mức chưa bằng 1. Với $b=20,r=5,s=0.3$, $q(0.3)=1-(1-0.3^5)^{20}\approx0.047$. Slide MMDS trang 50 ghi nhầm "0.3%", nhưng phép tính dùng $s=0.3$, tức 30%.

::: exercise Tự kiểm
Giữ $p$ cố định. Muốn giảm dương tính giả dưới $\tau$ nên tăng $r$ hay giảm $r$? Cái giá phải trả là gì?
:::

::: solution
Tăng $r$ và giảm $b$. Với $p$ cố định và $0<s<1$, $s^r$ giảm khi $r$ tăng nên mỗi dải khó trùng hơn, dẫn tới $q(s)=1-(1-s^r)^b$ giảm với mọi $s$. Dương tính giả giảm, nhưng xác suất bỏ sót tăng ở mọi mức chưa bằng 1.
:::

## 4. Thuật toán tạo và hậu kiểm ứng viên

### Vai trò

$q(s)$ mô tả chất lượng lọc. Hệ thống vẫn cần gom ngăn, sinh cặp, loại trùng và đối chiếu hậu kỳ. Phần này tách phân tích xác suất khỏi đặc tả thuật toán.

### Đặc tả thuật toán

Đầu vào: ma trận $\Sigma\in V^{p\times N}$ với $p=br$; khóa `(chỉ-số-dải, vector đầy đủ)` giữ toàn bộ $v\in V^r$.

Điều kiện trước: $\Sigma$ hợp lệ, $p=br$, $N\ge1$.

Đầu ra: tập cặp ứng viên $C$ đã loại trùng.

Điều kiện sau: $C$ chứa đúng các cặp trùng ít nhất một dải.

Giả mã:

```text
đầu vào: Sigma (p x N), b, r với p = br
C <- tập rỗng
với mỗi cột i = 1..N:
  với mỗi dải l = 1..b:
    thêm i vào ngăn B[l, vector_dải(Sigma, l, i)]
với mỗi ngăn B:
  với mỗi cặp không thứ tự {i,j} trong B:
    thêm {i,j} vào C
trả C
```

### Vết chạy nhỏ

::: example Ngăn trước, cặp sau
Hai ngăn đã gom xong: $(1,(2,5))\mapsto[1,4,7]$ và $(2,(4,1))\mapsto[1,4]$. Trước loại trùng, cặp $\{1,4\}$ xuất hiện hai lần. Sau phép hợp, $C=\{\{1,4\},\{1,7\},\{4,7\}\}$.
:::

### Bất biến của giai đoạn sinh cặp

::: proof Chứng minh bất biến
Sau khi duyệt $t$ ngăn đã gom xong, $C$ là hợp của mọi cặp không thứ tự nằm trong $t$ ngăn đó.

1. Khởi tạo: chưa duyệt ngăn nào, $C=\varnothing$, bất biến đúng.
2. Duy trì: liệt kê đủ cặp của ngăn kế tiếp và lấy hợp; cặp lặp bị hợp loại mà vẫn không mất cặp nào.
3. Kết thúc: đã duyệt mọi ngăn, nên $C$ đúng theo đặc tả ứng viên.

Thuật toán có hai giai đoạn. Giai đoạn một xây xong các ngăn. Bất biến ở trên thuộc giai đoạn hai, khi lần lượt duyệt các ngăn đã hoàn tất.
:::

### Dừng, chi phí và bộ nhớ

Vòng lặp hữu hạn: $N$ cột, $b$ dải, rồi danh sách ngăn hữu hạn. Nếu bảng băm và tập hợp hỗ trợ thao tác trong thời gian kỳ vọng hằng số, chi phí kỳ vọng là $\Theta(pN+\mathbb E[A])$.

Ký hiệu: $A=\sum_B\binom{|B|}{2}$ là số lượt sinh cặp trước loại trùng; $|C|$ là số cặp sau loại trùng.

| Đại lượng | Cận |
|---|---|
| Lượt sinh cặp | $A=\sum_B\binom{|B|}{2}$ |
| Thời gian | $\Theta(pN+A)$; xấu nhất $A=\Theta(bN^2)$ |
| Bộ nhớ phụ trợ | $O(bN+|C|)$ nếu khóa tham chiếu chữ ký; đầu vào $\Sigma$ là $\Theta(pN)$ |
| Đối chiếu chữ ký | $O(p|C|)$ và chỉ ước lượng Jaccard |

Phân biệt ba đại lượng:

- $bN+A$ là số **bản ghi trung gian**: mỗi khối dải–cột phát một bản ghi (tổng $bN$), mỗi lượt sinh cặp trước loại trùng phát một bản ghi (tổng $A$).
- $\Theta(pN+A)$ là **dung lượng từ truyền**: mỗi khóa dải đầy đủ có $\Theta(r)$ thành phần, nên tổng theo số từ là $\Theta(pN+A)$, chưa tính hằng số mã hóa.
- $O(p|C|)$ là chi phí **đối chiếu chữ ký** trên các cặp đã loại trùng.

Nếu vật hóa mọi vector dải thay vì tham chiếu chữ ký, phần khóa cũng có thể tốn $O(pN)$. Nếu truyền mã băm rút gọn, bộ giảm vẫn phải đối chiếu vector đầy đủ để không gộp hai khóa khác nhau do va chạm mã.

### Hậu kiểm

Đối chiếu chữ ký đầy đủ cho tỷ lệ hàng trùng, là ước lượng Jaccard; đối chiếu tập shingle hoặc dữ liệu gốc mới cho Jaccard chính xác. Quyết định cuối dùng ngưỡng $\tau$.

![Luồng từ chữ ký được chia dải, gom ngăn, sinh cặp, loại trùng rồi đối chiếu hậu kỳ.](img/lec-06/luong-ung-vien.svg)

::: exercise Tự kiểm
Với một triệu chữ ký, cần so sánh những đại lượng nào để đánh giá chi phí mà không khởi tạo mọi cặp?
:::

::: solution
So sánh $pN$ (kích thước chữ ký), $A$ (lượt sinh cặp trước loại trùng) và $|C|$ (số cặp ứng viên sau loại trùng). Không khởi tạo $\binom N2$; chỉ sinh cặp có cùng một ngăn.
:::

## 5. Định nghĩa họ băm nhạy cảm cục bộ

### Vai trò

Phân dải dùng MinHash cho Jaccard. Cần một ngôn ngữ chung cho các độ đo khác: Hamming, cosin, Euclid.

### Ví dụ từ MinHash

::: example Ví dụ 3.18
Chọn ngẫu nhiên một hàm MinHash; đặt $d=1-J$. Với khoảng cách Jaccard:

- Cặp gần $d(x,y)\le0.3$ tương đương $J(x,y)\ge0.7$, xác suất va chạm $\rho\ge0.7$.
- Cặp xa $d(x,y)\ge0.6$ tương đương $J(x,y)\le0.4$, xác suất va chạm $\rho\le0.4$.

Họ MinHash là một họ $(0.3,0.6,0.7,0.4)$-nhạy. Vùng giữa $0.3<d<0.6$ chưa có bảo đảm. Nguồn: MMDS §3.6.2, Ví dụ 3.18.
:::

### Đặc tả $h\sim F$

Cho khoảng cách $d$ và $d_1<d_2$. Một phân phối $F$ trên các hàm băm là $(d_1,d_2,\alpha_1,\alpha_2)$-nhạy nếu hàm $h$ được lấy theo $h\sim F$ thỏa:

- $d(x,y)\le d_1$ kéo theo $\Pr[f(x)=f(y)]\ge\alpha_1$;
- $d(x,y)\ge d_2$ kéo theo $\Pr[f(x)=f(y)]\le\alpha_2$.

Xác suất lấy theo phép chọn $h\sim F$, không phải "với mọi $h$". Yêu cầu $d_1<d_2$ và $0\le\alpha_2<\alpha_1\le1$. Không phát biểu bảo đảm cho $d_1<d<d_2$. Nguồn: MMDS §3.6.1.

![Họ LSH bảo đảm cận xác suất cho cặp gần và cặp xa; vùng giữa không có kết luận bắt buộc.](img/lec-06/ho-lsh.svg)

### Kiểm giả thiết

Mỗi họ chỉ hợp cho một độ đo. Với MinHash, $\rho=\Pr[h(x)=h(y)]$ đúng bằng Jaccard dưới hoán vị đều; với họ khác, $\rho$ là xác suất va chạm riêng của độ đo đó, không truyền công thức từ họ này sang họ khác.

::: exercise Tự kiểm
Một cặp có khoảng cách $d$ với $d_1<d<d_2$. Họ LSH có bảo đảm nào cho xác suất va chạm của cặp này không?
:::

::: solution
Không. Định nghĩa chỉ bảo đảm cận dưới ở $d\le d_1$ và cận trên ở $d\ge d_2$; vùng giữa không có kết luận bắt buộc.
:::

Phân dải MinHash là một trường hợp cụ thể. Định nghĩa vừa nêu cho phép xét các họ băm trên những không gian khác.

## 6. Khuếch đại AND/OR

### Vai trò

Từ một họ cơ sở có xác suất va chạm $\rho$, ta ghép nhiều hàm để tách xác suất của cặp gần khỏi xác suất của cặp xa. Các công thức lũy thừa dưới đây đòi hỏi những phép băm độc lập.

### Phép ghép AND

Lấy $r$ hàm độc lập $h_1,\ldots,h_r$ và ghép chúng thành

$$g(x)=(h_1(x),\ldots,h_r(x)),\qquad \rho\mapsto\rho^r.$$

AND đòi hỏi mọi nhánh cùng trùng. Nó làm cả hai xác suất giảm, nhưng xác suất nhỏ giảm nhanh hơn.

### Phép ghép OR

Lấy $b$ bản sao độc lập và coi là va chạm nếu ít nhất một bản sao trùng:

$$\rho\mapsto1-(1-\rho)^b.$$

OR chỉ đòi hỏi một nhánh trùng. Nó làm cả hai xác suất tăng, nhưng xác suất lớn tiến gần 1 nhanh hơn.

::: example Một phép tính ngắn
Với $\rho=0.8$, AND 2 cho $0.8^2=0.64$. OR 3 cho $1-(1-0.8)^3=0.992$. Cùng một xác suất cơ sở nhưng hai phép ghép phục vụ hai mục tiêu khác nhau.
:::

::: proof Lập luận theo tính độc lập
Với AND, xác suất cả $r$ hàm cùng trùng là $\rho^r$. Với OR, xác suất không hàm nào trùng là $(1-\rho)^b$; lấy biến cố bù được $1-(1-\rho)^b$. Nếu các hàm phụ thuộc nhau, không được dùng hai lũy thừa này.
:::

### Thứ tự và đánh đổi

AND và OR không giao hoán. Ghép theo thứ tự khác nhau tạo các hàm xác suất khác nhau. AND thường giảm dương tính giả nhưng tăng âm tính giả; OR đi theo chiều ngược lại. Mô hình vân tay ở mục 10 cho thấy cách ghép hai tầng để cân bằng hai loại lỗi.

![AND yêu cầu mọi nhánh trùng; OR chỉ yêu cầu ít nhất một nhánh trùng.](img/lec-06/and-or.svg)

::: exercise Tự kiểm
Trong sơ đồ, phép nào yêu cầu mọi nhánh trùng và phép nào chỉ yêu cầu một nhánh trùng?
:::

::: solution
AND yêu cầu mọi nhánh; OR chỉ yêu cầu ít nhất một nhánh.
:::

## 7. Họ Hamming

### Vai trò và đặc tả

Họ này dùng cho vector rời rạc với khoảng cách Hamming. Với $x,y\in\mathcal A^m$, chọn đều tọa độ $I$ trên $\{1,\ldots,m\}$ và đặt $h_I(x)=x_I$. Khi đó

$$\Pr[h_I(x)=h_I(y)]=1-\frac{H(x,y)}m.$$

Trực quan, trong $m$ tọa độ có $H(x,y)$ tọa độ khác và $m-H(x,y)$ tọa độ trùng. Phép băm chỉ chọn ngẫu nhiên một tọa độ để nhìn. Nguồn: MMDS §3.7.1.

::: proof Chứng minh bằng phép đếm
Hai vector trùng ở đúng $m-H(x,y)$ tọa độ. Vì $I$ được chọn đều, xác suất chọn trúng một tọa độ bằng nhau là

$$\frac{m-H(x,y)}m=1-\frac{H(x,y)}m.$$
:::

### Miền và giới hạn

Họ trên là $(d_1,d_2,1-d_1/m,1-d_2/m)$-nhạy với $0\le d_1<d_2\le m$. Khoảng cách Hamming chạy từ 0 đến $m$, nên xác suất phải chuẩn hóa theo $m$. Họ cơ sở chỉ có $m$ hàm tọa độ; khi $m$ nhỏ, số phép chọn độc lập khác nhau cũng bị hạn chế.

::: exercise Tự kiểm
Với $x=000000$ và $y=110011$ trong $\{0,1\}^6$, xác suất chọn một tọa độ đều để hai giá trị bằng nhau là bao nhiêu?
:::

::: solution
$H(x,y)=4$, nên xác suất là $1-4/6=1/3$. Hai vector trùng ở vị trí 3 và 4.
:::

## 8. Họ cosin

### Vai trò và đặc tả

Họ này dùng cho hai vector khác 0 khi độ gần được biểu diễn bằng góc. Chọn pháp tuyến đẳng hướng $v$, chẳng hạn $v\sim\mathcal N(0,I_m)$, rồi đặt $h_v(x)=\operatorname{sign}(v^\top x)$. Với $x,y\ne0$ và góc $\theta\in[0,\pi]$ đo bằng radian,

$$\Pr[h_v(x)=h_v(y)]=1-\frac{\theta}{\pi}.$$

![Hai vector khác 0 và một siêu phẳng có pháp tuyến ngẫu nhiên; xác suất hai vector cùng phía bằng một trừ theta chia pi.](img/lec-06/sieu-phang.svg)

::: proof Lập luận hình học
Hai vector cố định xác định một mặt phẳng. Siêu phẳng ngẫu nhiên tách chúng khi hình chiếu của pháp tuyến nằm trong nêm góc có tổng độ rộng $\theta$ trên chu kỳ $\pi$. Xác suất khác dấu là $\theta/\pi$; lấy biến cố bù được xác suất cùng dấu $1-\theta/\pi$.
:::

### Điều kiện và trường hợp biên

- Phải có $x,y\ne0$ để góc được xác định.
- Với phân phối Gaussian liên tục, $\Pr[v^\top x=0]=0$ cho một vector khác 0 cố định; cài đặt vẫn cần quy ước dấu tại 0.
- Pháp tuyến phải đẳng hướng. Lấy $v\in\{\pm1\}^m$ theo phân phối Rademacher không cho đẳng thức tổng quát trên mọi dữ liệu. Nguồn: MMDS §3.7.2; Stanford CS246 bài 04 dùng để đối chiếu trực quan.

::: exercise Tự kiểm
Với góc $\theta=60^\circ$, xác suất hai vector được băm cùng phía là bao nhiêu? Phân phối của pháp tuyến phải thỏa điều kiện gì?
:::

::: solution
$\theta=60^\circ=\pi/3$, nên xác suất là $1-(\pi/3)/\pi=2/3$. Hai vector phải khác 0 và pháp tuyến phải đẳng hướng.
:::

## 9. Họ Euclid

### Xây dựng hình học hai chiều của MMDS

MMDS §3.7.4 xây một họ cho mặt phẳng: chọn đường thẳng ngẫu nhiên, chia đường thành các đoạn dài $a$, rồi băm điểm theo ngăn chứa hình chiếu của nó. Với hai điểm cách nhau $d$:

- nếu $d\le a/2$, xác suất cùng ngăn ít nhất là $1/2$;
- nếu $d\ge2a$, xác suất cùng ngăn không vượt quá $1/3$.

Do đó họ là $(a/2,2a,1/2,1/3)$-nhạy. Phát biểu này dùng trực tiếp hai ngưỡng đã kiểm; không lặp lại điều kiện bị in đảo chiều trong phần diễn giải của sách.

### Phép chiếu–dịch dựa trên phân phối ổn định

Datar, Immorlica, Indyk và Mirrokni xây một họ cho nhiều chiều bằng phân phối $p$-ổn định. Với chuẩn L2, lấy $v\sim\mathcal N(0,I_m)$ và độ dịch $u\sim U[0,a)$ độc lập với $v$:

$$h_{v,u}(x)=\left\lfloor\frac{v^\top x+u}{a}\right\rfloor,\qquad a>0.$$

Giữ $v$ cố định và đặt $\delta=v^\top(x-y)$. Xác suất theo $u$ để hai hình chiếu rơi cùng ngăn là $\max(0,1-|\delta|/a)$. Xác suất đầy đủ còn phải lấy trung bình theo $v$; không được dùng công thức có điều kiện này như một công thức chỉ phụ thuộc khoảng cách. Gaussian là trường hợp $p=2$ của họ phân phối ổn định. Nguồn: Datar et al., §3.2, DOI `10.1145/997817.997857`; MMDS §§3.7.4–3.7.5.

![Chiếu hai điểm lên một trục, rồi chia trục thành các ngăn rộng a với độ dịch u ngẫu nhiên.](img/lec-06/euclid-dich.svg)

### Giới hạn và tự kiểm

Độ dịch $u$ làm biên ngăn không cố định. Hai cặp có cùng chênh lệch hình chiếu vẫn có thể rơi khác ngăn nếu vị trí của chúng so với biên khác nhau. Họ Euclid có nguồn ngẫu nhiên và luật va chạm riêng; không chuyển công thức từ Hamming hoặc cosin sang đây.

::: exercise Tự kiểm
Trong $h_{v,u}$, độ dịch $u$ có vai trò gì? Với chuẩn L2, các thành phần của $v$ được lấy theo phân phối nào?
:::

::: solution
$u$ dịch lưới ngăn để vị trí biên không bị cố định. Với chuẩn L2, các thành phần của $v$ là các biến Gaussian độc lập; $u$ độc lập với $v$ và phân phối đều trên $[0,a)$.
:::

## 10. Mô hình khớp vân tay

### Vai trò và mô hình ô lưới

Đây là mô hình minh họa trong MMDS, không phải bằng chứng về hiệu năng của một hệ nhận dạng hiện hành. Mỗi dấu vân tay được biểu diễn bằng tập ô lưới có điểm đặc trưng. Một hàm cơ sở chọn ba ô và yêu cầu cả ba ô cùng có điểm: đây là phép AND trong một hàm. Sau đó các hàm được ghép bằng OR, hoặc bằng AND của hai nhóm OR.

Khi hai dấu cùng cho kết quả "có", chúng vào cùng ngăn. Mỗi kết quả "không" phải vào một ngăn đơn riêng; gom mọi kết quả "không" vào chung một ngăn sẽ sinh gần như mọi cặp. Mô hình giả sử xác suất một dấu ngẫu nhiên có điểm trong một ô là 0.2. Nếu hai dấu cùng ngón và dấu thứ nhất có điểm ở một ô, xác suất dấu thứ hai có điểm tương ứng là 0.8. Nguồn: MMDS §§3.8.4–3.8.5.

![Ba ô đặc trưng tạo một ngăn có và các ngăn đơn không, không gom chung để tránh sinh mọi cặp.](img/lec-06/van-tay.svg)

### Xác suất cơ sở

::: example Xác suất của một hàm ba ô
Với hai dấu cùng ngón, xác suất dấu thứ nhất có điểm ở cả ba ô là $0.2^3$. Khi đó, xác suất dấu thứ hai có điểm ở ba ô tương ứng là $0.8^3$. Theo giả thiết độc lập của mô hình,

$$\rho_1=0.2^3\cdot0.8^3=0.004096.$$

Với hai dấu khác ngón, sáu biến cố có điểm độc lập, mỗi biến cố có xác suất 0.2:

$$\rho_0=0.2^6=0.000064.$$
:::

### Hai tầng khuếch đại

- OR nhiều hàm độc lập làm tăng cơ hội phát hiện, đồng thời tăng dương tính giả.
- AND của hai nhóm OR làm giảm dương tính giả, đồng thời tăng âm tính giả.

Các xác suất trên là giả thiết của mô hình sách, không phải số liệu thực nghiệm hiện thời. Bài 3.8.2 tính cụ thể hai cấu hình dùng tổng cộng 2048 hàm.

::: exercise Tự kiểm
Vì sao mỗi dấu vân tay không thỏa bộ ba ô phải vào một ngăn đơn riêng, thay vì gom vào một ngăn chung?
:::

::: solution
Ngăn đơn chứa đúng một dấu nên không sinh cặp. Nếu gom mọi kết quả "không" vào chung một ngăn, mọi cặp trong ngăn đều trở thành ứng viên dù không có bằng chứng trùng bộ ba ô.
:::

## 11. Ba bài tập nguồn và tổng hợp

Ba bài sau giữ nguyên dữ kiện và yêu cầu của MMDS 3e; các bước nhỏ chỉ giúp theo dõi lời giải.

### Bài 3.4.4 — hai công việc MapReduce

::: exercise Bài 3.4.4
Mỗi bản ghi đầu vào là $(i,\Sigma_{:,i})$; chữ ký có $p=br$ hàng. Dùng hai công việc MapReduce để tạo, với mỗi cột $i$, danh sách mọi cột $j>i$ cần so sánh. Nêu kiểu khóa–giá trị vào và ra của bộ ánh xạ, bộ giảm ở cả hai công việc, cùng quy tắc loại trùng.
:::

::: hint
Khóa của công việc 1 phải phân biệt dải và giữ toàn bộ vector dải. Bộ giảm của công việc 2 chỉ xuất $j>i$ và lấy hợp để loại cặp lặp qua nhiều dải.
:::

::: solution
**Công việc 1 — tạo ngăn theo dải**

```text
map(i, chữ_ký):
  với mỗi dải l:
    emit((l, vector_dải(Sigma, l, i)), i)
reduce(khóa, danh_sách_i):
  emit(khóa, danh_sách_i)
```

Bộ ánh xạ phát khóa $(l,\text{vector dải})$ và giá trị $i$. Bộ giảm gom danh sách chỉ số theo khóa; có thể bỏ ngăn một phần tử. Nếu khóa được mã hóa bằng một giá trị băm rút gọn, vẫn phải kiểm vector đầy đủ sau va chạm mã.

**Công việc 2 — tạo danh sách so sánh**

```text
map((l, v), danh_sách_i):
  với mỗi cặp {i, j} trong danh_sách_i, i < j:
    emit(i, j)
reduce(i, danh_sách_j):
  emit(i, sắp_xếp(loại_trùng(danh_sách_j)))
```

Bộ ánh xạ chuẩn hóa $i<j$ và phát $(i,j)$ cho mỗi cặp. Bộ giảm lấy hợp để loại cặp lặp qua nhiều dải. Đầu ra có dạng $i\mapsto\{j:j>i\}$.
:::

### Bài 3.6.1 — bốn chuỗi AND/OR

::: exercise Bài 3.6.1
Với một họ băm cơ sở có xác suất va chạm $\rho$, viết xác suất sau mỗi chuỗi: (a) AND 2 rồi OR 3; (b) OR 3 rồi AND 2; (c) AND 2 → OR 2 → AND 2; (d) OR 2 → AND 2 → OR 2 → AND 2.
:::

::: hint
Sau AND $r$, thay $\rho$ bằng $\rho^r$. Sau OR $b$, thay $\rho$ bằng $1-(1-\rho)^b$. Ghi giá trị trung gian sau từng phép.
:::

::: solution
(a) AND 2 cho $\rho^2$, rồi OR 3 cho

$$1-(1-\rho^2)^3.$$

(b) OR 3 cho $1-(1-\rho)^3$, rồi AND 2 cho

$$\bigl[1-(1-\rho)^3\bigr]^2.$$

(c) AND 2 cho $\rho^2$, OR 2 cho $1-(1-\rho^2)^2$, rồi AND 2 cho

$$\bigl[1-(1-\rho^2)^2\bigr]^2.$$

(d) Đặt $z_1=1-(1-\rho)^2$, $z_2=z_1^2$ và $z_3=1-(1-z_2)^2$. Kết quả sau AND 2 là

$$z_3^2=\Bigl[1-\bigl(1-z_2\bigr)^2\Bigr]^2.$$
:::

### Bài 3.8.2 — mô hình vân tay

::: exercise Bài 3.8.2
Trong mô hình §3.8.5, xác suất có điểm trong một ô là 0.2. Với hai dấu cùng ngón, nếu dấu thứ nhất có điểm trong một ô thì dấu thứ hai có điểm tương ứng với xác suất 0.8. Mỗi hàm dùng ba ô. Tính tỷ lệ dương tính giả và âm tính giả cho (a) OR 2048 hàm và (b) AND của hai nhóm OR 1024 hàm.
:::

::: hint
Dùng $\rho_1=0.2^3\cdot0.8^3=0.004096$ cho hai dấu cùng ngón và $\rho_0=0.2^6=0.000064$ cho hai dấu khác ngón. Với OR 2048, tính $1-(1-\rho_1)^{2048}$ và $1-(1-\rho_0)^{2048}$.
:::

::: solution
**Xác suất cơ sở**

$$\rho_1=0.004096,\qquad \rho_0=0.000064.$$

**(a) OR 2048**, với các hàm độc lập:

- Dương tính thật (TP): $1-(1-\rho_1)^{2048}\approx0.999776$.
- Âm tính giả (FN): $(1-\rho_1)^{2048}\approx0.000224$.
- Dương tính giả (FP): $1-(1-\rho_0)^{2048}\approx0.122849$.

**(b) AND của hai nhóm OR 1024**

Với một nhóm,

$$u_1=1-(1-\rho_1)^{1024}\approx0.985048,$$

$$u_0=1-(1-\rho_0)^{1024}\approx0.063437.$$

AND hai nhóm cho

- TP: $u_1^2\approx0.970320$;
- FN: $1-u_1^2\approx0.029680$;
- FP: $u_0^2\approx0.004024$.

| Đại lượng | OR 2048 | AND 2 × (OR 1024) |
|---|---:|---:|
| TP | $0.999776$ | $0.970320$ |
| FN | $0.000224$ | $0.029680$ |
| FP | $0.122849$ | $0.004024$ |

Phương án (b) hạ mạnh dương tính giả, đổi lại âm tính giả tăng. Giá trị gần $0.9998$ là xác suất dương tính thật của OR 2048, không phải âm tính giả.
:::

LSH đã chuyển bài toán từ quét mọi cặp sang tạo một tập ứng viên có thể điều chỉnh bằng xác suất. Bài 07 tiếp tục với tìm kiếm lân cận gần đúng; các cấu trúc HNSW, PQ và IVF-PQ không thuộc phạm vi bài này.

## Bảng tự kiểm

| Câu hỏi | Dụng cụ kiểm tra |
|---|---|
| Vì sao chữ ký ngắn không giảm số cặp? | Ví dụ 3.10 và phép đếm $\binom N2$ |
| Khóa dải phải gồm gì? | `(chỉ-số-dải, vector đầy đủ)`; kiểm khóa sau va chạm mã |
| $q(s)$ đúng khi nào, ngưỡng nửa là gì? | Tính độc lập; $s_{1/2}=(1-2^{-1/b})^{1/r}$ |
| Giữ $p$ cố định, tăng $r$ gây tác động gì? | $q(s)$ giảm trên $0<s<1$; dương tính giả giảm, bỏ sót tăng |
| Thuật toán tạo ứng viên có bất biến và chi phí nào? | Hợp cặp theo ngăn; $bN+A$, $\Theta(pN+A)$, $O(p|C|)$ |
| Họ LSH bảo đảm ở đâu? | Hai miền $d\le d_1$ và $d\ge d_2$; không bảo đảm vùng giữa |
| AND/OR dùng lũy thừa khi nào? | Khi các phép băm độc lập |
| Xác suất va chạm Hamming là gì? | $1-H(x,y)/m$ |
| Họ cosin cần điều kiện nào? | Vector khác 0, pháp tuyến đẳng hướng, góc tính bằng radian |
| Hai xây dựng Euclid khác nhau ở đâu? | Hình học 2D của MMDS và chiếu–dịch dựa trên phân phối ổn định |
| Ngăn "có" và "không" trong mô hình vân tay khác nhau ra sao? | Ngăn "có" gom cặp; mỗi kết quả "không" vào ngăn đơn |
| TP, FN, FP trong Bài 3.8.2 là bao nhiêu? | So OR 2048 với AND 2 × (OR 1024) |

## Tài liệu tham khảo

- Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman, *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, 2020. Chương 3, §§3.4, 3.6–3.8; Ví dụ 3.10–3.12, 3.18; Bài 3.4.4, 3.6.1, 3.8.2; §3.5 dùng cho định nghĩa khoảng cách.
- Mayur Datar, Nicole Immorlica, Piotr Indyk và Vahab S. Mirrokni, “Locality-Sensitive Hashing Scheme Based on p-Stable Distributions”, SoCG 2004, §3.2, DOI `10.1145/997817.997857`; [bản tác giả](https://immorlica.com/pubs/pstable.pdf).
- Stanford CS246, “Locality-Sensitive Hashing” (`03-lsh.pdf`, `04-lsh_theory.pdf`), dùng để đối chiếu cấu trúc khuếch đại và siêu phẳng ngẫu nhiên; các mệnh đề được kiểm lại bằng MMDS.
- Slide MMDS `ch03-lsh.pdf`, dùng để đối chiếu từng cụm; lỗi “0.3%” ở slide 50 được sửa thành $s=0.3$ (30%).
