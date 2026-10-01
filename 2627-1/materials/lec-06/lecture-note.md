# Tìm cặp tương đồng bằng LSH

Bài 06 · Giải thuật nền tảng của Khoa học dữ liệu · Học kỳ 1, năm học 2026–2027.

[Bộ trang chiếu Bài 06](lecture-06-tim-cap-tuong-dong-bang-lsh.html) trình bày cùng ký hiệu và dữ kiện. Tài liệu này phát triển lập luận để có thể đọc độc lập. Sườn nội dung dựa trên *Mining of Massive Datasets* (MMDS), ấn bản 3, Chương 3, §§3.4–3.8, tr.91–122; các bài tập cuối tài liệu lấy trực tiếp từ chương này. Học liệu và slide chính thức của các tác giả được cung cấp tại [MMDS](http://www.mmds.org).

## Bài toán tìm cặp sau khi đã có chữ ký

Một kho tài liệu có thể được biểu diễn bằng các tập đặc trưng, chẳng hạn tập shingle. Shingle là một đoạn liên tiếp có độ dài cố định trong biểu diễn văn bản đã chọn. Tập đặc trưng cho phép đo sự trùng lặp; chữ ký MinHash rút gọn việc so sánh các tập lớn. Tuy nhiên, chữ ký ngắn chưa làm giảm số cặp cần xét.

Gọi $C$ là số tài liệu và $S_1,\ldots,S_C$ là các tập đặc trưng hữu hạn, không rỗng. Với hai tập $A,B$, độ tương đồng Jaccard là

$$
\mathrm{SIM}(A,B)=\frac{|A\cap B|}{|A\cup B|}.
$$

Một chữ ký có $n$ thành phần. Ma trận $\mathrm{SIG}\in V^{n\times C}$ chứa chữ ký của tài liệu $c$ ở cột $c$; $V$ là miền giá trị của một thành phần chữ ký. Với một cặp cố định $(c,d)$, đặt $s=\mathrm{SIM}(S_c,S_d)$; $\widehat s$ là tỷ lệ hàng trùng của hai cột chữ ký quan sát được. $s$ là tính chất của hai tập gốc, còn $\widehat s$ phụ thuộc các phép thử đã chọn.

Với một hoán vị $\pi$ trên vũ trụ đặc trưng hữu hạn, một MinHash lý tưởng trả thứ hạng nhỏ nhất $h_\pi(A)=\min_{a\in A}\pi(a)$. Khi $\pi$ được chọn đều và dùng chung cho hai tập, phần tử đứng đầu trong $A\cup B$ thuộc giao với xác suất $|A\cap B|/|A\cup B|$. Hai giá trị MinHash trùng đúng trong trường hợp ấy, nên $\Pr[h_\pi(A)=h_\pi(B)]=\mathrm{SIM}(A,B)$. Đây là kết quả MinHash từ Bài 05 được dùng lại trong bài này.

Với ngưỡng chấp nhận $t\in[0,1]$, đích tìm kiếm là các cặp không thứ tự $(c,d)$ thỏa $c<d$ và $s\ge t$. Một bộ tạo ứng viên trước hết sinh tập $\mathcal C$ nhỏ hơn hoặc bằng tập tất cả các cặp. Sau đó, mỗi cặp trong $\mathcal C$ được kiểm bằng Jaccard gốc. Cách làm này có thể bỏ sót cặp đạt ngưỡng nếu cặp ấy không vào $\mathcal C$.

::: example
Ví dụ 3.10 của MMDS xét một triệu tài liệu, mỗi chữ ký có 250 số nguyên, mỗi số chiếm 4 byte. Dung lượng chữ ký là $10^6\cdot250\cdot4=10^9$ byte. Số cặp vẫn là

$$
\binom{10^6}{2}=499\,999\,500\,000.
$$

Nếu giả sử mỗi lần so cặp mất $1\,\mu s$, tổng thời gian là $499\,999{,}5$ giây, xấp xỉ $5{,}787$ ngày. Đây là phép tính dưới giả định thời gian mỗi cặp, không phải kết quả đo một hệ thống. Giới hạn còn lại nằm ở số cặp, ngay cả khi chữ ký vừa bộ nhớ.
:::

Băm nhạy cảm theo tính cục bộ (LSH) tổ chức các phép thử sao cho cặp tương đồng có khả năng được sinh cao hơn. Phân dải MinHash là trường hợp đầu tiên: dữ liệu đã được biểu diễn và lấy chữ ký; nhiệm vụ mới là tổ chức các cột thành nhóm để sinh cặp.

![Chữ ký tạo khóa dải, sinh ứng viên duy nhất rồi kiểm trên tập gốc.](img/lec-06/quy-trinh-cap.svg)


::: exercise
Câu hỏi: (a) Với kho một triệu tài liệu và chữ ký đã vừa bộ nhớ, giới hạn nào vẫn còn? Nêu tập trung gian cần tạo trước khi kiểm Jaccard gốc. (b) Với $C=10^5$ tài liệu và $1\,\mu s$ mỗi cặp, tính số cặp và tổng thời gian.
:::

::: solution
(a) Số cặp vẫn là $\binom{10^6}{2}=499\,999\,500\,000$. Cần tạo tập ứng viên $\mathcal C$, rồi chỉ kiểm Jaccard gốc trên các cặp trong tập này. Chữ ký ngắn giảm dữ liệu mỗi cặp nhưng chưa giảm số cặp.

(b) $\binom{10^5}{2}=4\,999\,950\,000$ cặp, khoảng $5\,000$ giây, gần 1,4 giờ. Giảm số tài liệu 10 lần làm số cặp giảm khoảng 100 lần.
:::


Nguồn: MMDS 3e, §3.4 và Ví dụ 3.10, tr.91–92.

## Phân dải, sinh cặp và xác minh

### Đặc tả phép phân dải

§3.4.1 nêu cách tiếp cận chung của LSH: băm mỗi đối tượng nhiều lần sao cho đối tượng tương đồng dễ vào cùng thùng hơn, rồi xem mọi cặp cùng thùng ở ít nhất một lần băm là cặp ứng viên. Cặp không tương đồng mà vẫn thành ứng viên là ứng viên giả; cặp tương đồng không thành ứng viên là cặp bị bỏ sót. Với chữ ký MinHash, mỗi lần băm là một dải của chữ ký: cột càng giống nhau thì từng thành phần càng dễ trùng, nên càng dễ trùng toàn bộ một dải.

Chọn $b,r\in\mathbb N_{>0}$ sao cho $n=br$. Chia $n$ hàng chữ ký thành $b$ dải, mỗi dải gồm $r$ hàng liên tiếp. Với dải $j$ và tài liệu $c$, bộ $r$ giá trị có thứ tự (tuple) của dải là

$$
z_{j,c}=\mathrm{SIG}_{(j-1)r+1:jr,c},\qquad k_{j,c}=(j,z_{j,c}).
$$

Khóa gồm cả số dải. Hai tuple bằng nhau ở hai dải khác nhau không tạo cùng một khóa. Tập ứng viên được đặc tả bởi

$$
\mathcal C=\{(c,d):1\le c<d\le C,\ \exists j:\ k_{j,c}=k_{j,d}\}.
$$

Đầu ra sau xác minh là $\{(c,d)\in\mathcal C:\ \mathrm{SIM}(S_c,S_d)\ge t\}$.

Trong một dải, mọi thành phần phải trùng: đó là phép ghép đồng thời. Giữa các dải, chỉ cần một dải trùng: đó là phép ghép ít nhất một. Khi dùng bảng băm để lưu khóa, va chạm của hàm băm lưu trữ phải được giải bằng so sánh khóa đầy đủ; vị trí bảng trùng chưa thay thế phép bằng tuple.

![Mỗi dải tạo một khóa gồm số dải và tuple, với n bằng b nhân r.](img/lec-06/phan-dai-chu-ky.svg)

Với nhiều hàng trong một dải, chỉ trùng một hàng là chưa đủ. Dải đầu trong Hình 3.7, Ví dụ 3.11, có các cột

$$
(1,3,0),\ (0,2,1),\ (0,1,3),\ (0,2,1),\ (2,2,1).
$$

Cột 2 và 4 trùng tuple nên thành ứng viên; cột 2 và 3 chỉ trùng thành phần đầu. Sách giả định có rất nhiều thùng, nên xem hai cột cùng thùng khi và chỉ khi tuple bằng nhau. Chữ ký nguồn có 12 hàng và 4 dải, nhưng hình chỉ cho dải đầu. Vì vậy, khác tuple ở dải này chưa đủ kết luận hai cột không là ứng viên ở một dải khác.

### Vết chạy trên dữ kiện MinHash đã có

::: example
Dữ kiện từ Ví dụ 3.8, MMDS, tr.85–86:

$$
S_1=\{a,d\},\quad S_2=\{c\},\quad S_3=\{b,d,e\},\quad S_4=\{a,c,d\}.
$$

| Hàng chữ ký | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| 1 | 1 | 3 | 0 | 1 |
| 2 | 0 | 2 | 0 | 0 |

Áp dụng phân dải với $b=2,r=1,t=2/3$: mỗi hàng là một dải, và khóa của một cột ở dải $j$ là cặp gồm số dải và tuple một phần tử. Ở dải 1, chèn tài liệu 1 tạo danh sách tại khóa $(1,(1))$; chèn tài liệu 4 nối vào chính danh sách đó. Các thùng cuối cùng là:

| Dải | Khóa | Danh sách mã | Cặp phát |
|---|---|---|---|
| 1 | $(1,(1))$ | 1, 4 | $(1,4)$ |
| 1 | $(1,(3))$ | 2 | Không có |
| 1 | $(1,(0))$ | 3 | Không có |
| 2 | $(2,(0))$ | 1, 3, 4 | $(1,3),(1,4),(3,4)$ |
| 2 | $(2,(2))$ | 2 | Không có |

Có 8 lượt chèn tài liệu vào thùng và $Q=4$ lượt phát cặp; $Q$ đếm cả các lần một cặp được phát lại. Sau khử lặp, tập ứng viên có $K=|\mathcal C|=3$ cặp phân biệt:

$$
\mathcal C=\{(1,3),(1,4),(3,4)\}.
$$

Ba phép xác minh cho

$$
\mathrm{SIM}(S_1,S_3)=\frac14,\quad
\mathrm{SIM}(S_1,S_4)=\frac23,\quad
\mathrm{SIM}(S_3,S_4)=\frac15.
$$

Chỉ $(1,4)$ đạt ngưỡng. Hai cột 1 và 4 trùng cả hai hàng, nên $\widehat s=1$, trong khi Jaccard gốc bằng $2/3$. Ví dụ này phân biệt việc thực thi trên chữ ký cố định với phân tích xác suất của chữ ký ngẫu nhiên.
:::

### Thuật toán và tính đúng

Đầu vào gồm SIG, các tập nguồn hữu hạn không rỗng, $b,r$ và $t\in[0,1]$. Các tuple được sao chép để hợp đồng lưu trữ không phụ thuộc một vùng nhìn vào ma trận.

```text
B ← từ điển rỗng; CAND ← tập rỗng
với j = 1,…,b:
    với c = 1,…,C:
        z ← bản sao SIG[(j−1)r+1 : jr, c]
        k ← (j, z)
        nếu k chưa có trong B: B[k] ← []
        B[k].append(c)
với mỗi danh sách L trong B:
    với mỗi c < d thuộc L: CAND.add((c,d))
OUT ← tập rỗng
với mỗi (c,d) trong CAND:
    nếu SIM(S_c,S_d) ≥ t: OUT.add((c,d))
trả OUT
```

::: proof
Với SIG cố định, thuật toán trả đúng các cặp trong $\mathcal C$ có Jaccard ít nhất $t$.

Ở dải đang xét, bất biến sau mỗi lượt chèn là: mỗi mã đã xử lý xuất hiện trong đúng danh sách của khóa dải của nó. Trước dải đầu tiên, từ điển $B$ rỗng. Ở đầu mỗi dải $j$, chưa có khóa mang chỉ số $j$; các nhóm của những dải trước vẫn được giữ. Chưa có mã nào được xử lý ở dải $j$ nên bất biến của dải này đúng. Khi xét mã $c$, khóa $k$ được tính đúng từ dải $j$. Nếu khóa mới, danh sách rỗng được tạo; nếu khóa đã có, các mã trước đó được giữ nguyên. Nối $c$ vào danh sách này duy trì bất biến và không di chuyển mã khác. Các nhóm của những dải đã hoàn thành cũng không đổi vì số dải nằm trong khóa.

Khi dựng thùng kết thúc, hai mã ở cùng danh sách khi và chỉ khi chúng trùng một khóa dải. Phát mọi cặp $c<d$ trong từng danh sách rồi hợp bằng tập tạo đúng $\mathcal C$, bất kể một cặp xuất hiện ở bao nhiêu dải. Kiểm Jaccard gốc giữ đúng các phần tử của $\mathcal C$ đạt $t$. Mọi vòng lặp đều hữu hạn, nên thuật toán dừng.
:::

Kết luận này không nói rằng mọi cặp thật đều có mặt trong $\mathcal C$. Với $C<2$ hoặc thùng có dưới hai phần tử, không có cặp được phát. Tập nguồn rỗng nằm ngoài đặc tả hiện tại; không dùng một quy ước bổ sung cho Jaccard của hai tập rỗng. Quy trình §3.4.3 của sách kiểm tỷ lệ trùng chữ ký ở bước 6 và ghi bước 7 kiểm tài liệu gốc là tùy chọn. Thuật toán đang xét bỏ bước 6 vì lọc bằng $\widehat s$ có thể tạo thêm bỏ sót, đồng thời kiểm Jaccard gốc cho mọi ứng viên.


::: exercise
Câu hỏi: (a) Trong vết chạy hai dải, giải thích vì sao cặp $(1,4)$ được phát hai lần nhưng chỉ kiểm Jaccard một lần. (b) Với cùng chữ ký, dùng $b=1$, $r=2$: xác định các thùng, $Q$, $K$ và tập kết quả khi $t=2/3$.
:::

::: solution
(a) Hai cột 1 và 4 trùng ở cả dải 1 và dải 2 nên mỗi dải phát cặp một lần. Tập $\mathcal C$ khử lặp; vòng xác minh duyệt từng phần tử của tập nên chỉ kiểm cặp này một lần.

(b) Các tuple là $(1,0)$, $(3,2)$, $(0,0)$, $(1,0)$; chỉ cột 1 và 4 chung thùng, nên $Q=K=1$ và kết quả vẫn là $\{(1,4)\}$. Đòi trùng cả hai hàng đã loại hai ứng viên giả $(1,3)$ và $(3,4)$.
:::


Nguồn: MMDS 3e, §§3.4.1,3.4.3, tr.92–96. Giả mã và bất biến triển khai biến thể kiểm gốc trực tiếp của thủ tục nguồn.

## Xác suất ứng viên và lựa chọn tham số

### Mô hình xác suất

Cố định hai tập không rỗng có Jaccard $s$. Mỗi thành phần chữ ký dùng một MinHash lý tưởng: hoán vị được chọn đều, cùng hoán vị áp dụng cho mọi tập. Các thành phần được chọn độc lập. Định lý MinHash cho xác suất trùng một thành phần bằng $s$.

Tại tầng sinh ứng viên, một cặp dưới ngưỡng được sinh là ứng viên giả. Bỏ sót là sự kiện cặp có $s\ge t$ không được sinh. Đây là hai loại sự kiện theo một cặp có độ tương đồng xác định; chúng chưa là tỷ lệ lỗi trên toàn kho.

::: example
Với $s=0{,}8$, $r=5$, xác suất cả năm hàng của một dải trùng là $0{,}8^5=0{,}32768$. Xác suất dải này không trùng là $0{,}67232$. Nếu có $b=20$ dải độc lập, xác suất không dải nào trùng là

$$
(0{,}67232)^{20}\approx 0{,}000356058.
$$

Xác suất cặp được chọn vì vậy xấp xỉ $0{,}999643942$.
:::

::: proof
Đặt $E_i$ là sự kiện trùng thành phần thứ $i$ trong một dải. Độc lập cho

$$
\Pr\left(\bigcap_{i=1}^rE_i\right)=s^r.
$$

Một dải không trùng có xác suất $1-s^r$. Do các dải dùng những phép thử độc lập, không dải nào trùng có xác suất $(1-s^r)^b$. Lấy biến cố bù,

$$
P_{b,r}(s)=\Pr[(c,d)\in\mathcal C]=1-(1-s^r)^b.
$$

Độc lập được dùng trong một dải và giữa các dải. Không cần giả định các cặp tài liệu khác nhau độc lập.
:::

Với cặp đạt ngưỡng, xác suất bỏ sót là $(1-s^r)^b$. Kiểm Jaccard chính xác loại ứng viên giả khỏi tập kết quả, nhưng không sửa được bỏ sót ở bước sinh.

### Ba đại lượng ngưỡng khác nhau

Ngưỡng $t$ quy định tiêu chuẩn chấp nhận trên dữ liệu gốc. Điểm $s_{1/2}$ là Jaccard tại đó xác suất được chọn bằng một nửa. Từ $P(s)=1/2$ suy

$$
(1-s^r)^b=\frac12
\quad\Longrightarrow\quad
s_{1/2}=(1-2^{-1/b})^{1/r}.
$$

Giá trị $b^{-1/r}$ là xấp xỉ thường dùng cho vùng chuyển tiếp, không phải đẳng thức trên. Với $b=20,r=5$, ba số có thể là $t=0{,}8$, $s_{1/2}\approx0{,}508695962$ và $b^{-1/r}\approx0{,}549280272$. Chúng có vai trò khác nhau. Bước 4 của §3.4.3 chọn $b,r$ sao cho $(1/b)^{1/r}\approx t$; nếu cần tránh bỏ sót thì đặt giá trị này thấp hơn $t$, nếu cần hạn chế ứng viên giả để chạy nhanh thì đặt cao hơn $t$.

![Hai cấu hình cùng 100 hàng tạo các đường xác suất ứng viên khác nhau.](img/lec-06/xac-suat-phan-dai.svg)

| Cấu hình $(b,r)$ | $P(0{,}3)$ | $P(0{,}8)$ |
|---|---:|---:|
| $(20,5)$ | 0,047494259 | 0,999643942 |
| $(10,10)$ | 0,000059047 | 0,678859974 |

Cấu hình thứ hai giảm cơ hội nhận cặp có Jaccard 0,3 nhưng cũng giảm mạnh cơ hội nhận cặp có Jaccard 0,8. Với $r=1$, đường xác suất không có hình chữ S; tên “đường xác suất ứng viên” áp dụng mà không cần giả định hình dạng ấy. Diện tích tô dưới hoặc trên đường cũng không là tỷ lệ lỗi toàn kho khi chưa biết phân bố độ tương đồng của các cặp.

::: exercise
Câu hỏi: Với hai cấu hình trong bảng, cấu hình nào phù hợp hơn nếu ưu tiên giảm bỏ sót ở $s=0{,}8$? Cấu hình nào giảm số cặp được chọn ở $s=0{,}3$?
:::

::: solution
Ưu tiên giảm bỏ sót tại 0,8 chọn $(20,5)$ vì $1-P(0{,}8)\approx0{,}000356058$, so với $0{,}321140026$ của $(10,10)$. Ưu tiên giảm ứng viên tại 0,3 chọn $(10,10)$. Kết luận chỉ so đúng các độ tương đồng và mục tiêu đã nêu.
:::

Nguồn: MMDS 3e, §§3.4.2–3, tr.93–96; Bài 3.4.2, tr.96.

## Chi phí tạo và kiểm cặp

Phân tích bắt đầu khi đã có SIG và các tập gốc. Mỗi mã tài liệu hoặc tọa độ chiếm một từ máy. Đọc, sao chép và xử lý một tuple dài $r$ tốn $O(r)$; sau khi xử lý khóa, thao tác bảng băm có thời gian kỳ vọng $O(1)$. Chi phí Jaccard không được giả định là hằng số.

Gọi $u_{j,z}$ là số mã trong thùng tuple $z$ của dải $j$. Đặt

$$
Q=\sum_{j,z}\binom{u_{j,z}}2,\qquad K=|\mathcal C|\le Q.
$$

$Q$ đếm mọi lượt phát cặp, kể cả phát lặp; $K$ đếm cặp duy nhất phải xác minh. Trong vết chạy hai hàng, $Q=4,K=3$.

| Pha | Phép đếm | Chi phí kỳ vọng |
|---|---|---|
| Dựng thùng | $bC$ tuple, mỗi tuple dài $r$ | $O(brC)=O(nC)$ |
| Phát và khử lặp | $Q$ lần chèn cặp hai mã vào tập | $O(Q)$ |
| Xác minh | $K$ cặp duy nhất | $\sum_{(c,d)\in\mathcal C}T_J(c,d)$ |

Vì vậy, tổng thời gian kỳ vọng là

$$
O\left(nC+Q+\sum_{(c,d)\in\mathcal C}T_J(c,d)\right).
$$

Nếu các tập được lưu theo thứ tự tăng, phép trộn hai dãy đếm giao và hợp trong $O(|S_c|+|S_d|)$, nên đây là một cận cho $T_J(c,d)$. Kết luận phụ thuộc biểu diễn tập; nó không phát sinh chỉ từ việc chữ ký ngắn.

Sao chép khóa cần tối đa $nC$ từ; các danh sách thùng chứa $bC$ mã; tập cặp chứa $K$ cặp. Bộ nhớ phụ là $O(nC+K)$, ngoài ma trận SIG đầu vào và các tập nguồn. Việc tạo danh sách rỗng cho khóa mới xảy ra tối đa $bC$ lần nên đã nằm trong cận dựng thùng.

Trường hợp xấu, mọi cột vào cùng thùng ở mỗi dải:

$$
Q=b\binom C2,\qquad K=\binom C2.
$$

LSH không cho thời gian dưới bậc hai vô điều kiện. Với mô hình MinHash độc lập, tuyến tính kỳ vọng còn cho

$$
\mathbb E[K]=\sum_{c<d}P_{b,r}(s_{cd}),\qquad
\mathbb E[Q]=b\sum_{c<d}s_{cd}^r.
$$

Mỗi số hạng là kỳ vọng của một biến chỉ báo cho cặp hoặc cho cặp–dải. Phép cộng kỳ vọng không cần độc lập giữa các cặp. Hai biểu thức giải thích vì sao phân bố tương đồng của dữ liệu ảnh hưởng lượng công việc.


::: exercise
Câu hỏi: Vì sao thay $Q$ bằng $K$ trong chi phí phát cặp là sai? Dùng vết chạy $Q=4,K=3$ để giải thích.
:::

::: solution
Cặp $(1,4)$ được phát hai lần. Cả hai lượt đều cần xử lý và chèn vào tập dù lần thứ hai không thêm phần tử mới. Vì vậy có 4 lượt phát nhưng chỉ 3 cặp duy nhất cần xác minh; $Q$ đo công việc trước khử lặp, còn $K$ đo công việc sau khử lặp.
:::


Nguồn: phân tích phép đếm từ thuật toán MMDS 3e, §§3.4.1,3.4.3. Phân biệt $Q,K$ và hợp đồng sao chép khóa hoàn thiện mô hình chi phí của thủ tục.

## Miền dữ liệu và các độ đo

### Độ đo khoảng cách và chuẩn vector

Phân dải MinHash đã gắn xác suất với Jaccard trên tập. Khi đối tượng là vector hoặc chuỗi, bước chọn cặp cần một độ đo xác định ý nghĩa của “gần”. Mỗi độ đo lại cần một phép băm riêng để cặp gần dễ va chạm hơn cặp xa; phần tiếp theo xây khái niệm chung cho các phép băm này.

Trên miền $X$, một độ đo khoảng cách (metric) là hàm $d:X\times X\to\mathbb R_{\ge0}$ thỏa: $d(x,y)=0$ khi và chỉ khi $x=y$; đối xứng; và bất đẳng thức tam giác $d(x,z)\le d(x,y)+d(y,z)$.

Trên $\mathbb R^D$, với $q\ge1$,

$$
\|x-y\|_q=\left(\sum_{i=1}^D|x_i-y_i|^q\right)^{1/q},\qquad
\|x-y\|_\infty=\max_i|x_i-y_i|.
$$

Các trường hợp $q=1,2$ và $\infty$ lần lượt cộng độ lệch tuyệt đối, đo độ dài Euclid và lấy độ lệch lớn nhất. Điều kiện $q\ge1$ bảo đảm các biểu thức này là chuẩn và sinh metric.

Với $x=(2,7),y=(6,4)$, độ lệch hai tọa độ là 4 và 3. Do đó $L_1=7,L_2=5,L_\infty=4$. Cùng một cặp điểm nhận ba giá trị khác nhau; vì vậy ngưỡng “gần” chỉ có nghĩa khi đã chọn độ đo.

![Hai điểm với độ lệch tọa độ 4 và 3 trên hai trục cùng tỷ lệ.](img/lec-06/chuan-vector.svg)

### Khoảng cách Jaccard

Trên các tập hữu hạn không rỗng, đặt $d_J(A,B)=1-\mathrm{SIM}(A,B)$. Miền giá trị là $[0,1]$. Chẳng hạn $\mathrm{SIM}(S_1,S_4)=2/3$ cho $d_J(S_1,S_4)=1/3$.

::: proof
Tính không âm và đối xứng theo ngay từ giao và hợp. $d_J(A,B)=0$ tương đương giao bằng hợp, tức $A=B$.

Để chứng minh tam giác cho $A,B,C$, lấy cùng một MinHash lý tưởng trên hợp hữu hạn của ba tập. Nếu $h(A)\ne h(C)$ thì không thể đồng thời có $h(A)=h(B)$ và $h(B)=h(C)$. Vì vậy,

$$
\{h(A)\ne h(C)\}\subseteq
\{h(A)\ne h(B)\}\cup\{h(B)\ne h(C)\}.
$$

Lấy xác suất, dùng chặn hợp và $\Pr[h(A)\ne h(B)]=d_J(A,B)$, thu được $d_J(A,C)\le d_J(A,B)+d_J(B,C)$. Không dùng độc lập giữa hai biến cố ở vế phải.
:::

### Khoảng cách góc

Với vector khác 0, góc được định nghĩa bởi

$$
\theta(x,y)=\arccos\frac{x\cdot y}{\|x\|_2\|y\|_2}\in[0,\pi].
$$

Góc chỉ phụ thuộc hướng: $x$ và $2x$ có góc 0 dù là hai vector khác nhau. Vì vậy, metric góc có miền là các hướng, tức các lớp vector theo bội dương; có thể đại diện mỗi hướng bằng một vector đơn vị. Vector 0 nằm ngoài miền.

Với $x=(1,2,-1),y=(2,1,1)$, tích vô hướng bằng 3, hai chuẩn bằng $\sqrt6$, nên $\cos\theta=1/2$ và $\theta=\pi/3=60^\circ$. Giá trị $1-\cos\theta=1/2$ không bằng góc $\pi/3$.

Phác thảo hình học của tam giác: trên mặt cầu đơn vị, góc giữa hai hướng là độ dài cung ngắn nhất nối chúng. Đi từ hướng thứ nhất qua hướng trung gian rồi đến hướng thứ ba không ngắn hơn cung ngắn nhất nối trực tiếp. Lập luận này giải thích tam giác cho metric góc; nó không đồng nhất góc với khoảng cách dây cung Euclid.

### Chỉnh sửa bằng chèn và xóa

Với hai chuỗi $x,y$, khoảng cách chỉnh sửa ở đây là số thao tác chèn hoặc xóa ký tự ít nhất để biến $x$ thành $y$; mỗi thao tác có chi phí 1. Phép thay thế không được tính như một thao tác riêng. Một dãy con thu được bằng cách xóa một số ký tự và giữ thứ tự các ký tự còn lại; các ký tự không cần liên tiếp. Gọi $L$ là độ dài dãy con chung dài nhất.

Chuỗi $abcde$ và $acfdeg$ có dãy con chung $acde$, dài 4. Vết sửa $abcde\to acde\to acfde\to acfdeg$ gồm một lần xóa và hai lần chèn.

::: proof
Khoảng cách bằng $|x|+|y|-2L$. Để đạt cận trên, giữ một dãy con chung dài nhất, xóa $|x|-L$ ký tự còn lại của $x$, rồi chèn $|y|-L$ ký tự để tạo $y$.

Ngược lại, trong bất kỳ kịch bản sửa nào, các ký tự gốc sống sót giữ thứ tự và tạo một dãy con chung. Có nhiều nhất $L$ ký tự như vậy. Vì thế cần ít nhất $|x|-L$ lần xóa ký tự gốc và $|y|-L$ lần chèn; các thao tác thừa chỉ tăng chi phí. Hai cận trùng nhau.

Đảo một kịch bản sửa bằng đổi chèn thành xóa cho tính đối xứng. Nối kịch bản tối ưu từ $x$ đến $y$ với kịch bản từ $y$ đến $z$ cho một kịch bản từ $x$ đến $z$, nên khoảng cách tối ưu thỏa tam giác. Chi phí 0 chỉ xảy ra khi hai chuỗi bằng nhau.
:::

Ví dụ cho $5+6-2\cdot4=3$. Chi phí tính $L$ phải được phân tích từ một thuật toán tìm dãy con chung dài nhất; công thức khoảng cách chưa xác định chi phí đó.

### Hamming

Gọi $\Sigma$ là tập ký hiệu và $\mathbf1[E]$ là hàm chỉ báo: nhận 1 nếu mệnh đề $E$ đúng, nhận 0 nếu $E$ sai. Với hai vector cùng chiều trong $\Sigma^D$, đặt

$$
d_H(x,y)=\sum_{i=1}^D\mathbf1[x_i\ne y_i].
$$

Hai vector $10101$ và $11110$ khác ở các vị trí 2,4,5, nên khoảng cách bằng 3. Hamming so cùng vị trí, trong khi chỉnh sửa có thể thay đổi sự căn chỉnh bằng chèn hoặc xóa.

Tại từng tọa độ, nếu $x_i\ne z_i$ thì ít nhất một trong $x_i\ne y_i$ hoặc $y_i\ne z_i$ đúng. Do đó $\mathbf1[x_i\ne z_i]\le\mathbf1[x_i\ne y_i]+\mathbf1[y_i\ne z_i]$; cộng theo $i$ chứng minh tam giác. Các tiên đề còn lại theo trực tiếp từ định nghĩa.

Trên vector đặc, chuẩn, góc và Hamming đều tính được bằng một lượt qua $D$ tọa độ, tức $O(D)$ phép toán trong mô hình từ máy. Chi phí này chỉ tính độ đo của một cặp, chưa giải bài toán tìm cặp trên toàn kho.


::: exercise
Câu hỏi: Với $x=(1,2,-1)$ và $y=(2,1,1)$, phân biệt cosin với góc. Vì sao Hamming của hai vector $10101,11110$ đếm vị trí khác, còn chỉnh sửa chuỗi cho phép thay đổi cách căn chỉnh?
:::

::: solution
Cosin bằng $1/2$, còn góc bằng $\pi/3=60^\circ$. Hamming so cùng vị trí nên đếm ba vị trí 2,4,5. Chỉnh sửa cho phép chèn hoặc xóa ký tự, làm các vị trí được ghép với nhau thay đổi; khoảng cách là số thao tác ít nhất.
:::


Nguồn: MMDS 3e, §3.5, tr.96–103, Ví dụ 3.13–17.

## Họ băm nhạy cảm và phép ghép

### Hai bảo đảm gần và xa

Độ đo xác định cặp gần và xa. Bảo đảm tạo ứng viên còn cần một họ phép thử cùng phân phối lấy mẫu. MinHash là ví dụ đầu tiên: mỗi hoán vị ngẫu nhiên là một phép thử, và cặp có Jaccard cao dễ trùng hơn. Định nghĩa dưới đây giữ lại đúng tính chất ấy cho một độ đo bất kỳ.

Cho metric $d$ trên miền $X$ và một họ hàm $\mathcal H$ kèm phân phối lấy mẫu. Với $0\le d_1<d_2$ và $0\le p_2<p_1\le1$, họ là $(d_1,d_2,p_1,p_2)$-nhạy cảm nếu với mọi cặp cố định $x,y$:

$$
d(x,y)\le d_1\ \Longrightarrow\
\Pr_{h\sim\mathcal H}[h(x)=h(y)]\ge p_1,
$$

$$
d(x,y)\ge d_2\ \Longrightarrow\
\Pr_{h\sim\mathcal H}[h(x)=h(y)]\le p_2.
$$

Cùng hàm $h$ được áp dụng cho hai đối tượng. Nguồn ngẫu nhiên nằm ở việc lấy $h$; một hàm và một cặp đều cố định cho kết quả xác định. Miền $d_1<d(x,y)<d_2$ không có bảo đảm từ định nghĩa.

![Ba miền gần, giữa và xa cùng hai chiều bất đẳng thức xác suất.](img/lec-06/mien-gan-xa.svg)

MinHash có xác suất trùng $1-d_J$. Vì vậy, với $0\le d_1<d_2\le1$, họ là $(d_1,d_2,1-d_1,1-d_2)$-nhạy cảm. Ví dụ 3.18 dùng $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$. Hai cận tổng quát này chỉ phân biệt miền $d\le0{,}3$ và $d\ge0{,}6$.


::: exercise
Câu hỏi: Chỉ từ định nghĩa họ $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$, nêu bảo đảm tại $d=0{,}2$, $d=0{,}5$ và $d=0{,}8$.
:::

::: solution
Tại $0{,}2$, xác suất trùng ít nhất $0{,}7$. Tại $0{,}8$, xác suất không quá $0{,}4$. Tại $0{,}5$, định nghĩa họ không cho cận chung vì khoảng cách nằm giữa hai ngưỡng.
:::


### Ghép đồng thời và ghép ít nhất một

Cố định một cặp có xác suất trùng cơ sở đúng bằng $p$. Ghép đồng thời (AND) $r$ phép thử độc lập nhận cặp khi cả $r$ phép đều trùng. Có thể lưu khóa tuple $g(x)=(h_1(x),\ldots,h_r(x))$. Ghép ít nhất một (OR) $b$ phép thử độc lập nhận cặp khi có ít nhất một phép trùng, bằng nhiều bảng hoặc các quyết định cặp. Theo §3.6.3, một dải của phần phân dải chính là ghép đồng thời $r$ MinHash, còn việc nhận cặp khi trùng ít nhất một trong $b$ dải là ghép ít nhất một; phân dải là AND rồi OR trên họ MinHash.

::: proof
AND là giao của $r$ biến cố độc lập, nên xác suất bằng $p^r$. Biến cố đối của OR là tất cả $b$ phép không trùng, có xác suất $(1-p)^b$, nên xác suất OR bằng $1-(1-p)^b$.

Hai hàm $p\mapsto p^r$ và $p\mapsto1-(1-p)^b$ đều tăng trên $[0,1]$. Bởi vậy, cận dưới gần và cận trên xa được biến đổi theo cùng công thức. Đây là phép biến đổi các cận của họ; chỉ khi cặp có xác suất cơ sở đúng bằng $p$ mới có đẳng thức xác suất sau ghép tại $p$.
:::

Với họ $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$ và 16 phép thử, Ví dụ 3.19–20 so hai cấu trúc:

| Thứ tự | Phép biến đổi | Cận gần | Cận xa |
|---|---|---:|---:|
| AND 4 rồi OR 4 | $F(p)=1-(1-p^4)^4$ | 0,878497449 | 0,098534519 |
| OR 4 rồi AND 4 | $G(p)=[1-(1-p)^4]^4$ | 0,993615344 | 0,573951942 |

Trạng thái trung gian ở AND là $0{,}8^4=0{,}4096$ và $0{,}4^4=0{,}0256$; ở OR là $1-0{,}2^4=0{,}9984$ và $1-0{,}6^4=0{,}8704$. Thứ tự ghép làm thay đổi đánh đổi dù số phép thử bằng nhau.

![Bốn nhóm AND, mỗi nhóm bốn hàm cơ sở, được ghép OR bằng hợp cặp.](img/lec-06/ghep-and-or.svg)

Với AND $r$ rồi OR $b$, mỗi đối tượng cần $br$ giá trị cơ sở, tạo $b$ tuple và tra $b$ bảng; hợp các tập cặp của các bảng rồi xác minh. Với OR rồi AND, mỗi nhóm OR trước hết hợp các cặp của các bảng cơ sở; bước AND lấy giao các tập cặp thu được từ những nhóm OR đó. Quan hệ “chung ít nhất một bảng” có thể không bắc cầu, nên không thể mặc nhiên thay OR bằng phép bằng của một tuple đơn.

Số hàm cơ sở bằng tích các kích thước nhóm. Tuy nhiên, chi phí phát cặp còn phụ thuộc kích thước thùng, tức $Q$, và chi phí xác minh phụ thuộc $K$. Khuếch đại xác suất không tự chứng minh một cận thời gian tuyến tính.


::: exercise
Câu hỏi: (a) Viết các biểu thức của bốn chuỗi trong [Bài 3.6.1(a–d)](#nhieu-tang-and-or-bai-3-6-1-a-d). Với bảng 16 phép thử ở trên, giải thích vì sao cùng ngân sách vẫn có hai đánh đổi. (b) Áp dụng AND 2 rồi OR 2 cho họ MinHash $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$; tính hai cận mới.
:::

::: solution
Lời giải bốn chuỗi nằm trong khối gập của Bài 3.6.1. Với 16 phép thử, AND 4 rồi OR 4 cho $1-(1-p^4)^4$; OR 4 rồi AND 4 cho $[1-(1-p)^4]^4$. Hai phép biến đổi khác nhau nên biến đổi các cận gần/xa khác nhau. Theo bảng, cấu trúc thứ hai giữ cận gần cao hơn nhưng cũng có cận xa cao hơn.

(b) AND 2 cho $0{,}49$ và $0{,}16$; OR 2 cho $1-0{,}51^2=0{,}7399$ và $1-0{,}84^2=0{,}2944$. Độ chênh $p_1-p_2$ tăng từ $0{,}3$ lên $0{,}4455$.
:::


Nguồn: MMDS 3e, §§3.6.1–3, tr.103–108, Ví dụ 3.18–20.

## Ba họ băm theo độ đo

Tính metric của một độ đo chưa bảo đảm tồn tại họ LSH phù hợp. Với mỗi họ dưới đây, nguồn ngẫu nhiên và xác suất va chạm được xác lập riêng trước khi dùng các phép ghép đã có.

### Chọn tọa độ cho Hamming

Cho $x,y\in\Sigma^D$, với $\Sigma$ là một bảng chữ hữu hạn, ví dụ $\{0,1\}$, và $D>0$. Chọn đều chỉ số $I\in\{1,\ldots,D\}$ và đặt $h_I(x)=x_I$. Một lần chọn $I$ xác định một hàm cho cả kho; chọn chỉ số riêng cho từng đối tượng sẽ làm thay đổi phép thử.

Với $10101$ và $11110$, các tọa độ 1 và 3 trùng, còn 2,4,5 khác. Chọn $I=1$ trả hai giá trị 1; chọn $I=2$ trả 0 và 1. Có $D-d_H(x,y)$ chỉ số thuận lợi trong $D$ chỉ số đồng khả năng, do đó

$$
\Pr[h_I(x)=h_I(y)]=1-\frac{d_H(x,y)}D.
$$

Đây là chứng minh bằng đếm, không cần xấp xỉ. Với ví dụ, xác suất bằng $2/5$. Xác suất giảm tuyến tính theo $d_H$, nên với $d_1<d_2$ họ chọn tọa độ là $(d_1,d_2,1-d_1/D,1-d_2/D)$-nhạy cảm. Khi ghép nhiều lần, lấy chỉ số độc lập có hoàn lại; số hàm phân biệt hữu hạn không giới hạn số lần lấy mẫu độc lập.

Thuật toán mỗi phép thử chỉ đọc một phần tử mảng và trả giá trị đó, nên dừng sau một lần đọc, tốn $O(1)$ thời gian và lưu một chỉ số. Với $m$ phép thử, lưu $m$ chỉ số cùng $m$ giá trị mỗi đối tượng. Các cặp ứng viên vẫn được tổ chức bằng khung ghép và thùng đã xây.


::: exercise
Câu hỏi: Xác định các hàm nhận từng cặp của [Bài 3.7.1](#ham-toa-do-bai-3-7-1), rồi đối chiếu lời giải gập tại bài đó.
:::

::: solution
Với mỗi cặp, so các tọa độ cùng chỉ số; hàm $h_i$ nhận cặp đúng khi hai giá trị tại vị trí $i$ trùng. Bảng lời giải Bài 3.7.1 liệt kê đủ sáu tập chỉ số.
:::


Nguồn: MMDS 3e, §3.7.1, tr.109.

### Siêu phẳng, chữ ký dấu và góc

Với pháp tuyến $v\ne0$, siêu phẳng qua gốc là tập các điểm $x$ thỏa $v\cdot x=0$. Hàm băm dấu là

$$
h_v(x)=\operatorname{sign}(v\cdot x),\qquad
\operatorname{sign}(t)=\begin{cases}+1,&t\ge0,\\-1,&t<0.\end{cases}
$$

Nhân $x$ với $c>0$ không đổi dấu của $v\cdot x$, nên giá trị băm chỉ phụ thuộc hướng của $x$; đó là tính chất cần cho khoảng cách góc. Một pháp tuyến phải được giữ nguyên khi băm mọi vector. Pháp tuyến vuông góc mặt phân chia; nó không phải chính đường hoặc mặt phân chia.

![Pháp tuyến vuông góc mặt phân chia; hai phía nhận hai dấu.](img/lec-06/phap-tuyen-dau.svg)

Trong mô hình pháp tuyến đẳng hướng, mọi hướng của $v$ đồng khả năng. Với hai vector khác 0 tạo góc $\theta\in[0,\pi]$ đo radian, xác suất khác dấu là $\Pr[h_v(x)\ne h_v(y)]=\theta/\pi$, nên xác suất cùng dấu là $1-\theta/\pi$.

::: proof
Nếu $\theta=0$, hai vector cùng hướng nên có cùng dấu với xác suất 1. Nếu $\theta=\pi$, chúng đối hướng nên khác dấu với xác suất 1; tích vô hướng bằng 0 có xác suất 0 dưới phân phối liên tục đẳng hướng.

Với $0<\theta<\pi$, hai vector không cùng phương và sinh một mặt phẳng. Dấu tích vô hướng chỉ phụ thuộc hình chiếu của pháp tuyến vào mặt phẳng này. Tính đẳng hướng làm hướng chiếu có phân phối đều trên vòng tròn; trường hợp hình chiếu bằng 0 có xác suất 0. Có hai miền hướng pháp tuyến làm khác dấu, mỗi miền có góc $\theta$. Do đó,

$$
\Pr[h(x)\ne h(y)]=\frac{2\theta}{2\pi}=\frac\theta\pi,
\qquad
\Pr[h(x)=h(y)]=1-\frac\theta\pi.
$$

Kết luận cũng khớp hai trường hợp biên đã xét riêng.
:::

![Cung góc theta giữa hai vector và hai miền hướng pháp tuyến làm khác dấu.](img/lec-06/goc-tach-sieu-phang.svg)

Với $\theta=\pi/3=60^\circ$, xác suất cùng dấu bằng $2/3$. Tổng quát, họ siêu phẳng là $(d_1,d_2,1-d_1/\pi,1-d_2/\pi)$-nhạy cảm khi $0\le d_1<d_2\le\pi$; MMDS viết cùng bộ tham số theo độ, $(180-d)/180$. Dùng số độ trực tiếp trong $1-\theta/\pi$ sẽ sai đơn vị.

Chữ ký dấu gồm $m>0$ bit từ $m$ pháp tuyến. Đặt $p_{\ne}=\theta/\pi$; quy tắc ước lượng góc thay xác suất bằng tỷ lệ bit khác quan sát được:

$$
\widehat p_{\ne}=\frac1m\sum_{i=1}^m\mathbf1[h_{v_i}(x)\ne h_{v_i}(y)],\qquad
\widehat\theta=\pi\widehat p_{\ne}.
$$

Ví dụ dưới đây áp dụng quy tắc cho ba pháp tuyến dấu cố định. Các pháp tuyến ấy không có phân phối đẳng hướng, nên vết tính không nhận bảo đảm của mệnh đề trên.


::: example
Ví dụ 3.22 dùng $x=(3,4,5,6)$, $y=(4,3,2,1)$ và ba pháp tuyến cố định:

| Pháp tuyến | Tích với $x$ | Tích với $y$ |
|---|---:|---:|
| $(1,-1,1,1)$ | 10 | 4 |
| $(-1,1,-1,1)$ | 2 | −2 |
| $(1,1,-1,-1)$ | −4 | 4 |

Chữ ký dấu là $(+,+,-)$ và $(+,-,+)$. Tỷ lệ khác dấu bằng $2/3$ cho góc ước lượng $\widehat\theta=\pi(2/3)=2\pi/3=120^\circ$. Trong khi đó,

$$
x\cdot y=40,\quad\|x\|_2^2=86,\quad\|y\|_2^2=30,
$$

$$
\theta=\arccos\frac{40}{\sqrt{2580}}\approx38{,}047579^\circ.
$$

Hai góc khác xa nhau. Có hai vấn đề cần phân biệt: dùng ít phép thử và chọn pháp tuyến dấu $\pm1$ không có phân phối đẳng hướng. Với quy tắc dấu tại 0 đã nêu, ngay cả xét đủ 16 pháp tuyến dấu trong bốn chiều cũng chỉ có 4 trường hợp trái dấu, cho ước lượng $45^\circ$, không bằng góc thật.
:::


Để tạo chữ ký $m$ bit, chọn $m$ pháp tuyến độc lập theo phân phối đã nêu; tính $m$ tích vô hướng và dấu cho mỗi đối tượng. Với vector đặc $D$ chiều, chi phí là $O(mD)$, lưu $m$ bit mỗi đối tượng và $O(mD)$ từ cho các pháp tuyến. Các vòng tính hữu hạn, nên thuật toán dừng. Đây là chi phí lấy chữ ký; chi phí thùng và xác minh được tính thêm.


::: exercise
Câu hỏi: Tính chữ ký và hai loại góc trong [Bài 3.7.2](#chu-ky-dau-bai-3-7-2). Nêu điều kiện để dùng đẳng thức $\Pr[h_v(x)=h_v(y)]=1-\theta/\pi$.
:::

::: solution
Hai vector phải khác 0; pháp tuyến có phân phối đẳng hướng và được dùng chung cho cả hai; $\theta$ đo radian. Bài 3.7.2 cung cấp các pháp tuyến cố định để thực thi quy tắc ước lượng; lời giải gập tại bài đó không nhận chúng là mẫu đẳng hướng.
:::


Nguồn: MMDS 3e, §§3.7.2–3, tr.109–111. Hình quan hệ pháp tuyến đối chiếu [Stanford CS246, LSH II](https://web.stanford.edu/class/cs246/slides/04-lsh_theory.pdf), PDF 48–49; hình trong tài liệu được vẽ lại.

### Phép chiếu Euclid và dịch ngẫu nhiên

Phép chiếu dùng độ lớn tọa độ, khác với phép băm dấu chỉ giữ phía của mặt phân chia. Định nghĩa họ trong mặt phẳng $\mathbb R^2$: chọn $u$ đều trên các hướng đơn vị; chọn $\delta$ độc lập, đều trên $[0,a)$ với $a>0$; đặt

$$
h_{u,\delta}(x)=\left\lfloor\frac{u\cdot x+\delta}{a}\right\rfloor.
$$

Cùng cặp $(u,\delta)$ được dùng cho mọi điểm. Trên trục hình chiếu, thùng mã $k$ là khoảng $[ka-\delta,(k+1)a-\delta)$, đóng bên trái và mở bên phải.

::: example
Bài 3.7.5 cho ba điểm, ở đây ký hiệu $z_1=(1,2,3)$, $z_2=(0,2,4)$ và $z_3=(4,3,2)$ để không trùng với hai cận $p_1,p_2$ của họ nhạy cảm. Đây là ví dụ thực thi trên các trục cố định, không phải lấy hướng ngẫu nhiên trong mặt phẳng. Với trục thứ nhất, độ rộng $a=1$ và biên không dịch, các mã $\lfloor x_1/a\rfloor$ lần lượt là 1,0,4. Ba điểm thuộc các khoảng $[1,2),[0,1),[4,5)$, nên trục này chưa tạo cặp. Kết quả trên ba trục và hai độ rộng được tính đầy đủ ở phần bài tập.
:::

![Các khoảng có biên ka trừ delta trên trục hình chiếu.](img/lec-06/chia-khoang-dich.svg)

Dịch đều tránh việc một biên cố định luôn tách hai điểm rất gần nhưng ở hai phía biên. Cơ chế dịch và lượng tử hóa được đối chiếu Datar và cộng sự, §3.2; các cận số dưới đây được suy trong mô hình hướng đơn vị hai chiều của MMDS, không phải phát biểu tổng quát cho mọi số chiều.

::: proof
Cố định $u$ và đặt $\ell=|u\cdot(x-y)|$. Nếu $0<\ell<a$, trong một chu kỳ dịch dài $a$, các vị trí biên nằm giữa hai hình chiếu chiếm độ dài $\ell$. Chúng làm hai điểm khác thùng. Do $\delta$ đều, xác suất khác thùng là $\ell/a$, bỏ qua các điểm biên có xác suất 0.

Nếu $\ell=0$, hai hình chiếu bằng nhau nên luôn chung thùng. Nếu $\ell\ge a$, chúng không thể nằm trong cùng một khoảng nửa mở rộng $a$. Ba trường hợp cho

$$
\Pr_\delta[h(x)=h(y)\mid u]=\max(0,1-\ell/a).
$$
:::

![Đoạn nối dài rho, góc nhọn phi với trục chiếu và đoạn chiếu dài ell bằng rho nhân trị tuyệt đối cos phi.](img/lec-06/hinh-chieu-euclid.svg)

Đặt $\rho=\|x-y\|_2$. Họ hai chiều có bộ tham số $(a/2,2a,1/2,1/3)$:

::: proof
Nếu $\rho\le a/2$, với mọi hướng đơn vị $u$ ta có $\ell\le\rho$. Xác suất có điều kiện vì vậy ít nhất $1-\rho/a\ge1/2$. Lấy trung bình theo $u$ giữ cận dưới $1/2$.

Nếu $\rho\ge2a$, chung thùng cần $\ell<a$. Gọi $\phi\in[0,\pi/2]$ là góc nhọn giữa trục chiếu và đoạn nối hai điểm. Khi đó $\ell=\rho|\cos\phi|$, nên chung thùng cần $|\cos\phi|<a/\rho\le1/2$. Trong hai chiều, hướng đều làm $\phi$ đều trên $[0,\pi/2]$. Miền $\phi>\pi/3$ chiếm tỷ lệ

$$
\frac{\pi/2-\pi/3}{\pi/2}=\frac13.
$$

Điều kiện góc là cần, chưa đủ cho chung thùng, nên xác suất va chạm không quá $1/3$.
:::

Một phép băm tính tích vô hướng, cộng dịch, chia cho $a$ rồi lấy sàn; với vector đặc, chi phí là $O(D)$ mỗi phép thử. Ba trục cố định của bài tập không tự có bảo đảm ngẫu nhiên vừa chứng minh. Hằng số $1/3$ cũng không được chuyển sang mọi chiều, vì phân bố của góc nhọn thay đổi theo số chiều.


::: exercise
Câu hỏi: Khi $\ell<a$, hai hình chiếu có chắc chung thùng không? Nêu nguồn ngẫu nhiên và điều kiện số chiều của bộ $(a/2,2a,1/2,1/3)$.
:::

::: solution
Chưa chắc: nếu $0<\ell<a$, một biên có thể nằm giữa hai hình chiếu; xác suất chung thùng theo dịch là $1-\ell/a$. Trường hợp $\ell=0$ luôn chung thùng. Bộ cận cần hướng đơn vị đều trong mặt phẳng và dịch đều trên $[0,a)$ độc lập với hướng; cận xa $1/3$ ở đây chỉ được chứng minh trong hai chiều.
:::


Nguồn: MMDS 3e, §§3.7.4–5, tr.111–113; cơ chế dịch: Datar–Immorlica–Indyk–Mirrokni, [*Locality-Sensitive Hashing Scheme Based on p-Stable Distributions*](https://people.csail.mit.edu/nickle/pubs/pstable.pdf), §3.2, PDF 3. Phân phối ổn định không thuộc nội dung bài này.

### Chi phí tính chữ ký của ba họ

Mô hình đếm: vector đặc $D$ chiều, mỗi số chiếm một từ máy, mỗi phép đọc, nhân, cộng hoặc so sánh tốn thời gian hằng. Các số dưới đây được đếm từ định nghĩa hàm, không phải số đo.

| Họ | Phép tính của một hàm | Thời gian | Tham số lưu |
|---|---|---|---|
| Chọn tọa độ | 1 lần đọc | $O(1)$ | 1 chỉ số |
| Siêu phẳng | $D$ nhân, $D-1$ cộng, 1 so sánh | $O(D)$ | $D$ từ |
| Chiếu có dịch | $D$ nhân, $D$ cộng, 1 chia, 1 lấy sàn | $O(D)$ | $D+1$ từ |

Chữ ký gồm $m$ hàm cho $C$ vector cần $C\cdot m$ lần tính hàm, tức $O(Cm)$ với họ chọn tọa độ và $O(CmD)$ với hai họ còn lại. Tham số của $m$ hàm được dùng chung cho cả kho; mỗi vector lưu $m$ giá trị, là $m$ bit với chữ ký dấu và $m$ số nguyên với chữ ký chiếu. Với vector thưa có $\mathrm{nnz}(x)$ thành phần khác 0, tích vô hướng chỉ duyệt $\mathrm{nnz}(x)$ thành phần nên $D$ được thay bằng $\mathrm{nnz}(x)$. Sau khi có chữ ký, dựng thùng, phát $Q$ cặp và xác minh $K$ cặp được tính như ở mục chi phí phân dải.

::: exercise
Câu hỏi: Một kho có $C=10^6$ vector đặc $D=1000$ chiều. Đếm số phép nhân để tính chữ ký $m=200$ hàm siêu phẳng, số từ lưu các pháp tuyến và số bit chữ ký của cả kho.
:::

::: solution
Mỗi hàm cần $D$ phép nhân cho một vector, nên tổng là $C\cdot m\cdot D=10^6\cdot200\cdot1000=2\cdot10^{11}$ phép nhân. Các pháp tuyến cần $m\cdot D=2\cdot10^5$ từ, dùng chung cho cả kho. Chữ ký dấu cần $m=200$ bit mỗi vector, tức $2\cdot10^8$ bit cho cả kho.
:::

## Ba ứng dụng tìm cặp

### Đối sánh thực thể

Hai hồ sơ có thể mô tả cùng người hoặc cùng thực thể dù một số trường khác nhau. Đầu vào là hai nguồn hồ sơ; đầu ra mong muốn là các cặp cùng thực thể. Nếu mỗi nguồn có một triệu bản ghi, xét mọi cặp giữa hai nguồn cần $10^{12}$ phép đối chiếu.

Một quy tắc tạo ứng viên dùng ba trường tên, địa chỉ và điện thoại. Mỗi trường tạo một bảng khóa. Các cặp khớp ít nhất một trường được hợp và khử lặp, rồi chấm điểm bằng thông tin đầy đủ hơn. Đây là phép OR của ba hàm khóa, tức phân dải với $b=3$ dải, mỗi dải một hàm ($r=1$); ví dụ của sách thay bảng băm bằng ba lần sắp xếp theo từng trường. Cặp không khớp hoàn toàn trường nào bị bỏ sót. Ví dụ ở §3.8.2 dùng khoảng cách chỉnh sửa để tính điểm phạt theo từng trường, với hiệu chỉnh từ các bảng tên tương đương. Khóa khớp hoàn toàn tạo ứng viên, còn độ sai khác giữa chuỗi tham gia bước xác minh. Quy tắc chỉ bảo đảm rằng cặp khớp một trường được đưa vào tập ứng viên; khớp điện thoại chưa chứng minh hai hồ sơ cùng người.

![Ba bảng khóa tên, địa chỉ và điện thoại sinh ứng viên trước bước chấm điểm.](img/lec-06/khoa-thuc-the.svg)

Không có mô hình phân phối cho ba trường thì chưa thể gán các xác suất $p_1,p_2$ hoặc giả định chúng độc lập. Chi phí vẫn phụ thuộc số phần tử trong nhóm, số cặp phát và chi phí chấm điểm. Một trường phụ không tham gia tính điểm có thể kiểm chứng chất lượng của tập kết quả; “không tham gia tính điểm” không đồng nghĩa với độc lập thống kê. Mô hình kiểm bằng ngày được trình bày riêng ở phần đọc thêm.


::: exercise
Câu hỏi: Giải thích vì sao khớp số điện thoại chưa đủ xác nhận hai hồ sơ cùng một thực thể.
:::

::: solution
Một số điện thoại có thể được nhiều người dùng chung. Khớp trường tạo ứng viên; xác minh còn cần điểm đánh giá các trường và tiêu chuẩn chấp nhận cặp.
:::


Nguồn: MMDS 3e, §§3.8.1–3, tr.114–117.

### Đối sánh vân tay

Đặc trưng vân tay là vị trí đường vân kết thúc hoặc các đường vân nhập vào nhau. Sau chuẩn hóa kích thước và hướng, một ảnh được biểu diễn bằng tập ô trên lưới chứa các đặc trưng ấy. Tập ô có thể so bằng Jaccard, nhưng lưới chỉ khoảng 1000 ô nên tập đã nhỏ; MMDS dùng một họ khác thay vì rút gọn bằng MinHash. Có hai bài toán: một–nhiều, so một ảnh truy vấn với cả kho, và nhiều–nhiều, tìm mọi cặp trong kho. Một phép thử chọn ba ô từ lưới trước khi xét các ảnh. Mọi ảnh chứa đủ ba ô vào một thùng chung; mỗi ảnh thiếu ít nhất một ô nhận một thùng đơn riêng. Vì vậy, hai ảnh trùng phép thử khi cả hai cùng chứa đủ ba ô đã chọn. Nếu gom mọi ảnh thiếu ô vào một thùng, chúng cũng va chạm và công thức xác suất dưới đây sẽ không còn đúng.

![Ba ô được chọn trước ảnh; chỉ ảnh có đủ ba ô vào thùng chung.](img/lec-06/phep-thu-van-tay.svg)

Mô hình nguồn dùng xác suất một ô có đặc trưng bằng 0,2. Với hai bản cùng ngón, xác suất ảnh thứ hai có đặc trưng tại một ô đã có của ảnh thứ nhất bằng 0,8. Các biến cố cần nhân và các phép thử được giả định độc lập theo mô hình.

Với hai ảnh khác ngón, xác suất cả hai cùng có một ô là $0{,}2^2=0{,}04$. Với hai ảnh cùng ngón, xác suất cả hai cùng có một ô là $0{,}2\cdot0{,}8=0{,}16$. Cho ba ô:

$$
q_F=0{,}2^6=0{,}000064,\qquad q_T=(0{,}2\cdot0{,}8)^3=0{,}004096.
$$

Đây là xác suất cả hai ảnh có đủ ba ô; không điều kiện hóa ảnh truy vấn đã có sẵn ba ô đó. Hai ảnh cùng ngón hoặc khác ngón có vai trò tương ứng cặp cần tìm hoặc cặp giả trong ứng dụng này. Một hàm nhận cặp cùng ngón với xác suất chỉ khoảng $1/244$, dù gấp 64 lần cặp khác ngón; vì vậy cần ghép nhiều hàm.

OR 1024 phép thử cho xác suất ứng viên giả $1-(1-q_F)^{1024}\approx0{,}063436634$ và bỏ sót $(1-q_T)^{1024}\approx0{,}014951892$. Ghép AND hai nhóm OR 1024 độc lập cho

$$
P_F=[1-(1-q_F)^{1024}]^2\approx0{,}004024207,
$$

$$
P_{\rm miss}=1-[1-(1-q_T)^{1024}]^2\approx0{,}029680224.
$$

Cấu trúc AND giảm ứng viên giả khoảng 16 lần nhưng bỏ sót tăng gấp đôi. Với bài toán một–nhiều, xác suất nhận cặp khác ngón cũng là tỷ lệ kho phải so với ảnh truy vấn: khoảng $6{,}3\%$ với OR 1024 và khoảng $1/250$ với AND hai nhóm. Hai phương án ở đoạn này dùng 1024 và 2048 phép thử, nên chưa là so sánh cùng ngân sách. Bài 3.8.2 ở cuối tài liệu so OR 2048 với AND hai nhóm OR 1024. Các phép tính dùng giá trị chưa làm tròn; lấy $0{,}063^2$ sẽ cho số khác vì đã làm tròn trung gian. Những xác suất này thuộc mô hình, không là tỷ lệ đo trên một hệ nhận dạng vân tay.

Với một ảnh truy vấn, cấu trúc AND hai nhóm OR thực hiện bốn thao tác: hợp các mã ảnh trong những thùng phù hợp của nhóm thứ nhất; hợp tương tự ở nhóm thứ hai; lấy giao hai hợp; rồi so ảnh truy vấn với các ứng viên còn lại. Hợp và giao chỉ xử lý mã ảnh. Phép so vân tay được thực hiện sau đó và có chi phí riêng.

Bài toán tìm mọi cặp trong kho phát các cặp từ từng thùng, hợp trong mỗi nhóm OR rồi giao hai tập cặp. Cả hai dạng đều cần xác minh ứng viên. Các xác suất $q_T,q_F$ vẫn xét sự kiện cả hai ảnh chứa đủ ba ô được chọn trước khi xét ảnh; thao tác truy hồi không thay chúng bằng một xác suất đã điều kiện hóa ảnh truy vấn.


::: exercise
Câu hỏi: So hai cấu trúc cùng 2048 phép thử trong [Bài 3.8.2(a,b)](#hai-cau-truc-van-tay-bai-3-8-2-a-b), dùng $q_F,q_T$ chưa làm tròn.
:::

::: solution
Lời giải gập của Bài 3.8.2 cho thấy OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn. AND hai nhóm OR 1024 giảm ứng viên giả và tăng bỏ sót; chi phí xác minh áp dụng trên các ứng viên còn lại.
:::


Nguồn: MMDS 3e, §§3.8.4–5, Ví dụ 3.23, tr.117–120.

### Bản tin gần trùng

Hai trang có thể cùng xuất phát từ một văn bản báo chí nhưng khác quảng cáo hoặc phần bao quanh. Mục tiêu là tìm cùng văn bản, khác với tìm các bài chỉ cùng chủ đề. Chọn tập đặc trưng ảnh hưởng trực tiếp đến điều mà Jaccard và LSH đo.

Từ dừng là các từ xuất hiện rất thường xuyên. Trong tình huống của §3.8.6, văn xuôi có mật độ từ dừng cao hơn quảng cáo hoặc tiêu đề. Quy tắc tạo shingle gồm một token từ dừng và hai token tiếp theo làm phần văn xuôi đóng góp nhiều shingle hơn.

Ví dụ 3.24 dùng các từ dừng I, that, you, for, your. Chẳng hạn, từ “that” và hai token theo sau tạo “that you buy”:

- “Buy Sudzo.” không có token từ dừng trong quy tắc, nên không tạo shingle.
- “I recommend that you buy Sudzo for your laundry.” cho bốn shingle xác định: “I recommend that”, “that you buy”, “you buy Sudzo”, “for your laundry”.
- Shingle bắt đầu bằng “your” có dạng “your laundry x”, còn phụ thuộc token kế tiếp $x$ chưa được cho.

Câu dài cũng có thể là quảng cáo. Quy tắc ưu tiên những chuỗi mang dạng văn xuôi, không bảo đảm loại mọi quảng cáo.

Sau khi tạo tập shingle mới, có thể dùng lại MinHash, phân dải và xác minh Jaccard. Chi phí bao gồm đọc token, tạo đặc trưng và xử lý ứng viên.


::: exercise
Câu hỏi: Đầu ra cần tìm ở bài toán bản tin là cùng văn bản hay cùng chủ đề? Vì sao câu quảng cáo dài đã cho vẫn có thể tạo shingle?
:::

::: solution
Mục tiêu là các trang xuất phát từ cùng văn bản. Câu dài chứa các từ dừng I, that, you, for, your nên quy tắc vẫn tạo shingle, dù câu đó có thể là quảng cáo. Quy tắc chỉ ưu tiên biểu diễn văn xuôi, không xác định hoàn hảo ranh giới quảng cáo.
:::


Nguồn: MMDS 3e, §3.8.6, Ví dụ 3.24, tr.120–121.

## Tổng hợp và tự kiểm

Một quy trình tìm cặp cần quyết định biểu diễn, độ đo, họ cơ sở, cấu trúc ghép, cách tổ chức thùng và phép xác minh. $P(s)$ mô tả một xác suất theo cặp; $Q$ và $K$ đếm công việc. Kiểm chính xác trên tập gốc bảo đảm kết quả trong tập ứng viên, còn cặp đạt ngưỡng chưa sinh vẫn có thể bị bỏ sót. Với kho một triệu tài liệu ở mở bài, hiệu quả phụ thuộc lượng cặp thực tế được sinh, không chỉ dung lượng chữ ký.

::: exercise
Câu hỏi:

1. Với hai hàng SIG $(1,3,0,1)$ và $(0,2,0,0)$, $b=2,r=1$, xác định cặp phát lặp và $K$.
2. Với cặp có Jaccard $s\ge t$, viết xác suất bỏ sót trong mô hình MinHash độc lập.
3. Với họ $(.3,.6,.7,.4)$, nêu bảo đảm khi $d\ge.6$.
4. Phân biệt cấu trúc $1-(1-p^4)^4$ và $[1-(1-p)^4]^4$.
5. Nêu điều kiện để xác suất cùng dấu bằng $1-\theta/\pi$.
6. Giải thích vì sao cặp vân tay chung thùng vẫn cần xác minh.
:::

::: solution
Cặp $(1,4)$ phát hai lần; hợp có ba cặp nên $K=3$. Xác suất bỏ sót của cặp đạt ngưỡng là $(1-s^r)^b$. Khi $d\ge.6$, xác suất trùng không quá .4. Công thức thứ nhất là AND 4 rồi OR 4; công thức thứ hai là OR 4 rồi AND 4, với các phép thử độc lập. Công thức góc cần vector khác 0, cùng phép băm, pháp tuyến đẳng hướng và góc đo radian. Cặp vân tay khác ngón vẫn có xác suất trùng trong mô hình, nên chung thùng chưa xác nhận cùng ngón.
:::

## Đọc thêm có giới hạn

### Độ rộng khoảng của Bài 3.7.5(d)

Với ba điểm đã cho, cặp $(1,2)$ luôn trùng ở trục thứ hai vì hai tọa độ đều bằng 2, nên là ứng viên với mọi $a>0$.

Hai cặp $(1,3)$ và $(2,3)$ đều có thể trùng ở trục thứ hai khi $\lfloor2/a\rfloor=\lfloor3/a\rfloor$. Nếu giá trị chung là 0 thì $a>3$. Nếu giá trị chung là số nguyên $m\ge1$, cần đồng thời

$$
\frac3{m+1}<a\le\frac2m.
$$

Khoảng này không rỗng chỉ khi $3m<2(m+1)$, tức $m<2$, nên chỉ $m=1$ và $a\in(3/2,2]$. Các trục còn lại không thêm khoảng mới: trùng tọa độ 1 và 4, hoặc 0 và 4, đòi $a>4$; trùng 2 và 4 cũng chỉ xảy ra khi $a>4$. Với cặp $(1,3)$, trục thứ ba lặp điều kiện của tọa độ 2 và 3.

Vì vậy, mỗi cặp $(1,3),(2,3)$ là ứng viên đúng khi

$$
a\in(3/2,2]\cup(3,\infty).
$$

Tại $a=3/2$ và $a=3$ có một điểm trên biên nên hai mã khác; tại $a=2$, hai tọa độ 2 và 3 cùng mã 1. Quy tắc nửa mở quyết định các dấu đóng/mở này.

### Kiểm tập kết quả thực thể bằng trường ngày

Độ trễ của một cặp hồ sơ là ngày tạo hồ sơ ở nguồn B trừ ngày tạo hồ sơ ở nguồn A, tính bằng ngày. Ví dụ §3.8.3 chỉ xét độ trễ từ 0 đến 90 ngày. Mô hình ngẫu nhiên dùng trung bình 45 ngày; một giả thiết đủ để có giá trị này là độ trễ ngẫu nhiên phân bố đều trên khoảng 0–90. Đây là giả thiết làm rõ mô hình, không phải hệ quả của riêng giới hạn 0–90.

Trong ví dụ nguồn, nhóm cặp đạt điểm tối đa 300 có độ trễ trung bình 10 ngày. Mô hình xem nhóm này là các khớp đúng và dùng trung bình 10 ngày làm mốc của thành phần thật. Với một nhóm cặp cùng mức điểm được xét, gọi $x$ là độ trễ trung bình và $f$ là tỷ phần khớp đúng. Mô hình hỗn hợp cho

$$
x=10f+45(1-f),\qquad f=\frac{45-x}{35}.
$$

Suy luận cần hai nhóm tham chiếu đại diện cho các thành phần thật/ngẫu nhiên trong tập kết quả. Trường ngày không tham gia tính điểm; điều này tự nó chưa bảo đảm các giả thiết đại diện. Công thức ước lượng thành phần của một nhóm, không xác nhận từng cặp riêng. Một giá trị $x$ ngoài $[10,45]$ không tương thích với mô hình hai thành phần này.

Các nhánh khác chỉ dẫn đọc tiếp: Bài 3.4.4, tr.96, cho cách tổ chức MapReduce; Ví dụ 3.21, tr.108, cho phép ghép 256 hàm; Bài 3.6.2–4, tr.108, phân tích điểm bất động và đạo hàm; §3.7.5, tr.113, bàn về mở rộng định tính của họ Euclid. Các mục này không là tiên quyết của bài tập bắt buộc dưới đây.

## Bài tập nguồn và lời giải

Sáu cụm bài sau giữ dữ kiện và yêu cầu toán học của MMDS 3e. Cụm đầu gồm Bài 3.4.1–2; Bài 3.7.5 chỉ lấy (a–c), còn (d) đã giải ở phần đọc thêm. Máy tính có thể hỗ trợ lũy thừa và arccos. Không có yêu cầu cài đặt chương trình.

### Xác suất phân dải — Bài 3.4.1–2

Nguồn: §3.4.4, tr.96.

::: exercise
Câu hỏi:

1. Tính $P(s)=1-(1-s^r)^b$ cho $s=.1,.2,\ldots,.9$ với ba cấu hình $(r,b)=(3,10),(6,20),(5,50)$.
2. Với từng cấu hình, tìm $s$ để $P(s)=1/2$ và so với xấp xỉ $b^{-1/r}$.

Sản phẩm: bảng 27 xác suất; phép biến đổi và bảng ba cặp ngưỡng.
:::

::: hint
Giữ thứ tự $(r,b)$ của đề. Tính lũy thừa trước khi làm tròn. Để tìm nghiệm một nửa, trước hết cô lập $(1-s^r)^b$.
:::

::: solution
| $s$ | $r=3,b=10$ | $r=6,b=20$ | $r=5,b=50$ |
|---:|---:|---:|---:|
| .1 | .009955120 | .000020000 | .000499878 |
| .2 | .077180588 | .001279222 | .015875200 |
| .3 | .239448893 | .014479467 | .114539882 |
| .4 | .483870732 | .078809323 | .402283952 |
| .5 | .736924424 | .270187144 | .795550630 |
| .6 | .912267475 | .615414636 | .982533828 |
| .7 | .985015105 | .918185997 | .999898996 |
| .8 | .999234054 | .997712125 | .999999998 |
| .9 | .999997864 | .999999740 | xấp xỉ 1 |

Biến đổi $1-(1-s^r)^b=1/2$ cho $s=(1-2^{-1/b})^{1/r}$. Các kết quả:

| $(r,b)$ | Nghiệm chính xác | Xấp xỉ $b^{-1/r}$ |
|---|---:|---:|
| $(3,10)$ | .406088134 | .464158883 |
| $(6,20)$ | .569353387 | .606962231 |
| $(5,50)$ | .424394480 | .457305052 |

Cả ba xấp xỉ lớn hơn nghiệm một nửa. Giá trị cuối bảng xác suất chỉ làm tròn về 1, không bằng 1 chính xác. Đáp án cần đủ 27 ô, giữ đúng $r,b$ và phân biệt ngưỡng do người dùng đặt với nghiệm của phương trình xác suất.
:::

### Nhiều tầng AND/OR — Bài 3.6.1(a–d)

Nguồn: §3.6.4, tr.108.

::: exercise
Câu hỏi: Gọi $p$ là xác suất trùng của một MinHash cơ sở. Viết xác suất sau các phép ghép độc lập:

- (a) AND 2 rồi OR 3.
- (b) OR 3 rồi AND 2.
- (c) AND 2, OR 2, AND 2.
- (d) OR 2, AND 2, OR 2, AND 2.

Sản phẩm: bốn biểu thức, có trạng thái trung gian cho các tầng ghép.
:::

::: hint
Mỗi tầng AND 2 thay xác suất $q$ bằng $q^2$; mỗi tầng OR $b$ thay $q$ bằng $1-(1-q)^b$. Áp dụng theo đúng thứ tự từ trái sang phải.
:::

::: solution
(a) $p\to p^2\to1-(1-p^2)^3$.

(b) $p\to1-(1-p)^3\to[1-(1-p)^3]^2$.

(c) $p\to p^2\to1-(1-p^2)^2\to[1-(1-p^2)^2]^2$.

(d) Đặt $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$; kết quả $q_3^2$.

Mỗi lần ghép sử dụng các bản thử độc lập. Đảo thứ tự AND và OR nói chung làm đổi biểu thức.
:::

### Hàm tọa độ — Bài 3.7.1

Nguồn: §3.7.6, tr.113.

::: exercise
Câu hỏi: Họ gồm sáu hàm $h_i(x)=x_i$ với $i=1,\ldots,6$. Cho $A=000000$, $B=110011$, $C=010101$, $D=011100$. Xác định các hàm làm mỗi cặp trở thành ứng viên.

Sản phẩm: sáu tập chỉ số cho các cặp AB, AC, AD, BC, BD, CD.
:::

::: hint
Đánh chỉ số từ 1. So từng cột của hai vector; hàm $h_i$ nhận cặp khi hai bit ở cùng vị trí $i$ bằng nhau.
:::

::: solution
| Cặp | Chỉ số hàm nhận cặp | Hamming để đối chiếu |
|---|---|---:|
| AB | 3, 4 | 4 |
| AC | 1, 3, 5 | 3 |
| AD | 1, 5, 6 | 3 |
| BC | 2, 3, 6 | 3 |
| BD | 2 | 5 |
| CD | 1, 2, 4, 5 | 2 |

Chỉ nêu Hamming chưa trả lời đủ đề; sản phẩm cần tên các hàm tương ứng với vị trí trùng.
:::

### Chữ ký dấu — Bài 3.7.2

Nguồn: §3.7.6, tr.113–114.

::: exercise
Câu hỏi: Cho bốn pháp tuyến

$$
v_1=(1,1,1,-1),\quad v_2=(1,1,-1,1),\quad
v_3=(1,-1,1,1),\quad v_4=(-1,1,1,1).
$$

Với $x=(2,3,4,5)$, $y=(-2,3,-4,5)$ và $z=(2,-3,4,-5)$, tính chữ ký dấu. Với mỗi cặp, tính góc ước lượng từ chữ ký và góc thật. Dùng $\operatorname{sign}(0)=+1$.

Sản phẩm: bảng tích/dấu và bảng ba cặp góc.
:::

::: hint
Tính bốn tích vô hướng trước khi lấy dấu. Góc ước lượng bằng $\pi$ nhân tỷ lệ bit khác; góc thật tính từ tích vô hướng của cặp vector gốc.
:::

::: solution
| Vector | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký |
|---|---|---|
| $x$ | $(4,6,8,10)$ | $(+,+,+,+)$ |
| $y$ | $(-8,10,-4,6)$ | $(-,+,-,+)$ |
| $z$ | $(8,-10,4,-6)$ | $(+,-,+,-)$ |

Bình phương các chuẩn đều bằng 54; $x\cdot y=14$, $x\cdot z=-14$, $y\cdot z=-54$.

| Cặp | Tỷ lệ khác dấu | Góc ước lượng | Góc thật |
|---|---:|---|---|
| $x,y$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(7/27)\approx74.973886^\circ$ |
| $x,z$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(-7/27)\approx105.026114^\circ$ |
| $y,z$ | $4/4$ | $\pi=180^\circ$ | $\pi=180^\circ$ |

Bốn pháp tuyến là dữ kiện cố định. Vết tính không bảo đảm góc ước lượng bằng góc thật cho mọi cặp vector.
:::

### Ba trục chiếu — Bài 3.7.5(a–c)

Nguồn: §3.7.6, tr.114.

::: exercise
Câu hỏi: Cho $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ (sách ký hiệu $p_1,p_2,p_3$). Ba hàm là phép chiếu theo ba trục tọa độ; các khoảng có dạng $[ja,(j+1)a)$ với $j\in\mathbb Z$.

- (a) Gán thùng với $a=1$.
- (b) Lặp lại với $a=2$.
- (c) Tìm cặp ứng viên trong mỗi trường hợp.

Sản phẩm: hai bảng mã theo trục và hai tập cặp. Phần (d) được trình bày ở mục đọc thêm.
:::

::: hint
Mã ở trục $i$ là $\lfloor x_i/a\rfloor$. Chỉ so mã trong cùng trục; số dải hoặc trục là một phần của khóa.
:::

::: solution
| $a$ | Mã của $z_1$ theo ba trục | Mã của $z_2$ | Mã của $z_3$ | Tập cặp |
|---:|---|---|---|---|
| 1 | $(1,2,3)$ | $(0,2,4)$ | $(4,3,2)$ | $\{(1,2)\}$ |
| 2 | $(0,1,1)$ | $(0,1,2)$ | $(2,1,1)$ | $\{(1,2),(1,3),(2,3)\}$ |

Với $a=1$, chỉ $z_1,z_2$ trùng ở trục 2. Với $a=2$, cặp $(1,2)$ trùng ở trục 1 và 2; cặp $(1,3)$ trùng ở trục 2 và 3; cặp $(2,3)$ trùng ở trục 2. Hợp các cặp theo trục và khử lặp cho tập kết quả. Một tọa độ bằng $a$ thuộc $[a,2a)$, không thuộc $[0,a)$.
:::

### Hai cấu trúc vân tay — Bài 3.8.2(a,b)

Nguồn: §3.8.7, tr.121.

::: exercise
Câu hỏi: Mỗi ô có đặc trưng với xác suất .2. Với hai bản cùng ngón, ảnh thứ hai có đặc trưng tại một ô đã có ở ảnh thứ nhất với xác suất .8. Mỗi phép thử chọn ba ô từ lưới trước khi xét ảnh; các phép thử độc lập theo mô hình. Gọi $F_1$ là OR 1024 phép thử và $F_2$ là OR 2048 phép thử.

- (a) Tính xác suất ứng viên giả và bỏ sót của $F_2$.
- (b) So với AND hai nhóm $F_1$ độc lập.

Sản phẩm: bảng hai xác suất cho hai cấu trúc cùng 2048 phép thử.
:::

::: hint
Tính $q_F$ và $q_T$ từ mô hình một ô rồi ba ô. Với cặp cùng ngón, bỏ sót là biến cố bù của được nhận. Không dùng .063 hoặc .985 đã làm tròn làm đầu vào ghép tiếp.
:::

::: solution
Xác suất cơ sở là $q_F=.2^6=.000064$ và $q_T=(.2\cdot.8)^3=.004096$.

Với OR 2048:

$$
P_F=1-(1-q_F)^{2048}\approx.122849062.
$$

$$
P_{\rm miss}=(1-q_T)^{2048}\approx.000223559.
$$

Với AND hai nhóm OR 1024 độc lập:

$$
P_F=[1-(1-q_F)^{1024}]^2\approx.004024207.
$$

$$
P_{\rm miss}=1-[1-(1-q_T)^{1024}]^2\approx.029680224.
$$

OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn. AND hai nhóm OR 1024 giảm ứng viên giả và tăng bỏ sót. Hai phương án cùng ngân sách 2048 phép thử, nên khác biệt đến từ cấu trúc ghép. Đáp án phải giữ giả thiết độc lập và phân biệt xác suất cả hai ảnh có ba ô với xác suất có điều kiện khi một ảnh đã có ba ô.
:::

## Tài liệu tham khảo

- Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman. *Mining of Massive Datasets*, ấn bản 3, Chương 3, §§3.4–3.8, tr.91–122; Ví dụ 3.8, tr.85–86. [Sách và slide chính thức](http://www.mmds.org).
- Jure Leskovec. Stanford CS246, [LSH I](https://web.stanford.edu/class/cs246/slides/03-lsh.pdf) và [LSH II](https://web.stanford.edu/class/cs246/slides/04-lsh_theory.pdf), tháng 1-2026. Đối chiếu phân dải, phép ghép và hình học siêu phẳng; sách là nguồn trục của bài.
- Mayur Datar, Nicole Immorlica, Piotr Indyk, Vahab S. Mirrokni. [*Locality-Sensitive Hashing Scheme Based on p-Stable Distributions*](https://people.csail.mit.edu/nickle/pubs/pstable.pdf), SoCG 2004, §3.2. Dùng cơ chế dịch đều khi lượng tử hóa hình chiếu.
