# Bài 06 — Tìm cặp tương đồng bằng LSH

Bài 05 thu mỗi tài liệu về một chữ ký MinHash ngắn mà tỷ lệ hàng trùng ước lượng được độ tương đồng Jaccard. Trong chương này, chúng ta dùng các chữ ký ấy để tìm những cặp tài liệu tương đồng mà không phải so mọi cặp: phân dải (banding) chữ ký để chỉ xác minh các cặp cùng thùng (bucket), tính xác suất một cặp bị bỏ sót và công việc còn lại, khái quát cách làm này cho các độ đo khác ngoài Jaccard, rồi áp dụng cho ba bài toán của sách nguồn. Các phương pháp này có tên chung là băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH).

[Bộ trang chiếu Bài 06](lecture-06-tim-cap-tuong-dong-bang-lsh.html) trình bày cùng ký hiệu và dữ kiện.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Chia chữ ký thành dải (band), lập khóa dải, dựng thùng, khử lặp và xác minh tập cặp ứng viên trên một ma trận chữ ký nhỏ, và chứng minh đầu ra đúng trên tập ứng viên (Mục 2.1–2.2).
2. Tính xác suất thành ứng viên $P_{b,r}(s)$, chọn số dải $b$ và số hàng $r$ theo ngưỡng $t$, và đếm công việc phát cặp, xác minh (Mục 2.3–2.5).
3. Kiểm một họ hàm là $(d_1,d_2,p_1,p_2)$-nhạy cảm và tính bộ tham số sau phép ghép AND và OR (Mục 3).
4. Chạy họ chọn tọa độ, họ siêu phẳng (hyperplane) và họ chiếu có dịch trên dữ kiện nhỏ, nêu giả thiết của từng bảo đảm xác suất và chi phí tính chữ ký (Mục 4).
5. Chọn biểu diễn, họ hàm và bước xác minh cho đối sánh thực thể, đối sánh vân tay và bản tin gần trùng (Mục 5, Tình huống 06.1–06.4).

<!-- note-topic-id: lec-06-topic-18 -->
## Kiến thức tiên quyết

Ghi chú Bài 05 chưa đánh số hiệu, nên các kết quả của bài đó được dẫn theo mục, dưới dạng "ghi chú Bài 05, Mục k", và được phát biểu lại dưới đây.

- **Độ tương đồng Jaccard** (ghi chú Bài 05, Mục 2). Với hai tập hữu hạn $A$, $B$ không cùng rỗng, $\mathrm{SIM}(A,B)=|A\cap B|/|A\cup B|$. Giá trị nằm trong $[0,1]$ và bằng $1$ khi và chỉ khi $A=B$.
- **Shingle** (ghi chú Bài 05, Mục 3 và Mục 12). Một $k$-shingle của tài liệu là một đoạn liên tiếp dài $k$ trong biểu diễn văn bản đã chọn; tài liệu được biểu diễn bằng tập các shingle của nó. Mục 12 của ghi chú Bài 05 (đọc thêm) nêu một biến thể: mỗi shingle là một từ dừng cùng hai từ ngay sau nó; phần tử của tập khi đó là cụm ba từ chứ không là đoạn $k$ ký tự.
- **MinHash và định lý xác suất trùng** (ghi chú Bài 05, Mục 5–6). Với một hoán vị $\pi$ của vũ trụ đặc trưng hữu hạn, MinHash của tập không rỗng $A$ là phần tử của $A$ đứng đầu trong thứ tự $\pi$, $h_\pi(A)=\arg\min_{a\in A}\pi(a)$, trong đó $\pi(a)$ là vị trí của $a$; ghi chú Bài 05 trả định danh phần tử này, không trả vị trí. Nếu thay định danh bằng vị trí $\min_{a\in A}\pi(a)$, hai tập vẫn cho cùng biến cố $h_\pi(A)=h_\pi(B)$ vì $\pi$ là song ánh. Nếu $\pi$ được chọn đều trong mọi hoán vị và dùng chung cho hai tập không rỗng $A$, $B$, thì $\Pr[h_\pi(A)=h_\pi(B)]=\mathrm{SIM}(A,B)$: phần tử đứng đầu của $A\cup B$ phân phối đều trên $A\cup B$, và hai giá trị bằng nhau đúng khi phần tử ấy thuộc $A\cap B$.
- **Chữ ký và ước lượng Jaccard** (ghi chú Bài 05, Mục 7). Chữ ký gồm $n$ giá trị MinHash với $n$ hoán vị chọn độc lập. Tỷ lệ $\widehat s$ các thành phần trùng của hai chữ ký có kỳ vọng bằng Jaccard của hai tập gốc.
- **Hàm băm thay hoán vị** (ghi chú Bài 05, Mục 9 và 11). Khi tính thực tế, mỗi hoán vị được thay bằng một hàm băm trên mã hàng; tập rỗng cho giá trị quy ước $+\infty$ ở đầu ra của thuật toán quét $x\in\{0,\ldots,R-1\}$, chẳng hạn $f(x)=(\alpha x+\beta)\bmod R$. Một hàm như vậy có thể là song ánh, nhưng một họ gồm các song ánh riêng lẻ chưa tự tạo ra phép chọn đều trên mọi hoán vị mà định lý xác suất trùng cần.
- **Công cụ xác suất** (học phần Xác suất thống kê). Biến cố bù: $\Pr(\overline E)=1-\Pr(E)$. Với các biến cố độc lập, xác suất của giao bằng tích các xác suất. Chặn hợp: $\Pr(E\cup F)\le\Pr(E)+\Pr(F)$, không cần độc lập. Tuyến tính kỳ vọng: kỳ vọng của một tổng bằng tổng các kỳ vọng, không cần độc lập; kỳ vọng của một biến chỉ báo bằng xác suất của biến cố tương ứng. Bất đẳng thức Jensen: với hàm $g$ lồi trên một khoảng chứa giá trị của biến ngẫu nhiên $X$, $\mathbb E[g(X)]\ge g(\mathbb E[X])$; với $g$ lõm, bất đẳng thức đổi chiều.
- **Tích vô hướng và chuẩn Euclid** (học phần Đại số tuyến tính). Với $x,y\in\mathbb R^D$, $x\cdot y=\sum_{i=1}^Dx_iy_i$ và $\|x\|_2=\sqrt{x\cdot x}$. Theo bất đẳng thức Cauchy–Schwarz, với $x,y\ne0$ thương $x\cdot y/(\|x\|_2\|y\|_2)$ nằm trong $[-1,1]$.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một mục được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương, trừ các ngoại lệ nêu trong đoạn ngay sau bảng.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $C$ | số tài liệu, cũng là số cột của ma trận chữ ký | số nguyên dương |
| $S_c$ | tập đặc trưng của tài liệu $c$, $1\le c\le C$ | tập hữu hạn, không rỗng |
| $\mathrm{SIG}$; $V$ | ma trận chữ ký, cột $c$ là chữ ký của $S_c$; miền giá trị của một thành phần chữ ký | $V^{n\times C}$; tập giá trị |
| $n$ | độ dài chữ ký, tức số hàng của $\mathrm{SIG}$ | số nguyên dương, $n=br$ |
| $s$; $\widehat s$ | Jaccard của hai tập gốc của một cặp; tỷ lệ hàng chữ ký trùng của cặp ấy | $[0,1]$ |
| $t$ | ngưỡng chấp nhận trên Jaccard gốc | $[0,1]$ |
| $b$; $r$; $j$ | số dải; số hàng mỗi dải; chỉ số dải | số nguyên dương; $1\le j\le b$ |
| $z_{j,c}$; $k_{j,c}$ | tuple của cột $c$ ở dải $j$; khóa dải $(j,z_{j,c})$ | $V^r$; $\{1,\ldots,b\}\times V^r$ |
| $\mathcal C$ | tập cặp ứng viên | tập các cặp $(c,d)$ với $c<d$ |
| $Q$; $K$ | số lượt phát cặp trước khử lặp; số cặp ứng viên phân biệt, $K=\lvert\mathcal C\rvert$ | số nguyên không âm, $K\le Q$ |
| $u_{j,z}$ | số mã tài liệu trong thùng có tuple $z$ ở dải $j$ | số nguyên không âm |
| $T_J(c,d)$ | thời gian tính Jaccard gốc của cặp $(c,d)$ | số phép toán từ máy |
| $P_{b,r}(s)$ | xác suất một cặp có Jaccard $s$ thành ứng viên khi phân dải $b$ dải, $r$ hàng | $[0,1]$ |
| $s_{1/2}$ | nghiệm của $P_{b,r}(s)=1/2$ | $(0,1)$ |
| $d$; $d_J$; $d_H$ | độ đo khoảng cách tổng quát; khoảng cách Jaccard; khoảng cách Hamming | hàm vào $\mathbb R_{\ge0}$ |
| $\theta$ | góc giữa hai vector khác $0$ | $[0,\pi]$, đo bằng radian |
| $D$; $\Sigma$ | số chiều của vector; bảng ký hiệu của vector trong khoảng cách Hamming | số nguyên dương; tập hữu hạn |
| $\mathbf 1[E]$ | hàm chỉ báo, bằng $1$ khi mệnh đề $E$ đúng và $0$ khi $E$ sai | $\{0,1\}$ |
| $\mathcal H$; $h$ | họ hàm băm kèm phân phối chọn hàm; một hàm được chọn từ họ | tập hàm; hàm |
| $(d_1,d_2,p_1,p_2)$ | bộ tham số của họ nhạy cảm: ngưỡng gần, ngưỡng xa, cận dưới và cận trên của xác suất trùng | $0\le d_1<d_2$, $0\le p_2<p_1\le1$ |
| $m$ | số hàm trong chữ ký của Mục 4 | số nguyên dương |
| $v$; $\widehat p_{\ne}$; $\widehat\theta$ | pháp tuyến của siêu phẳng; tỷ lệ bit khác dấu; góc ước lượng | $\mathbb R^D\setminus\{0\}$; $[0,1]$; $[0,\pi]$ |
| $u$; $\delta$; $a$ | hướng chiếu đơn vị; độ dịch biên; độ rộng khoảng | vector đơn vị; $[0,a)$; số thực dương |
| $\ell$ | khoảng cách giữa hai hình chiếu, $\lvert u\cdot(x-y)\rvert$ | $\mathbb R_{\ge0}$ |
| $q_F$; $q_T$ | xác suất hai ảnh khác ngón, cùng ngón cùng có đủ ba ô của một hàm ba ô | $[0,1]$ |

Các quy ước đọc sau dùng trong cả chương.

- Cặp tài liệu luôn viết $(c,d)$ với $c<d$, nên mỗi cặp không thứ tự được đếm một lần.
- Số thập phân dùng dấu phẩy, ví dụ $0{,}8$. Trong một bộ tham số có số thập phân, các thành phần cách nhau bằng dấu chấm phẩy, ví dụ $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$. Góc đo bằng radian; giá trị theo độ chỉ dùng khi ghi kèm phép quy đổi, chẳng hạn $\pi/3=60^\circ$.
- Chữ $C$ nghiêng là số tài liệu, còn $\mathcal C$ là tập ứng viên. Tên vector trong Bài tập 06.23 viết chữ đứng $\mathrm A,\mathrm B,\mathrm C,\mathrm D$ để không trùng $C$ và $D$.
- Chữ $d$ đứng trong cặp $(c,d)$ là chỉ số tài liệu; $d(\cdot,\cdot)$ có hai đối số là hàm khoảng cách; chữ $a,b,c,d,e$ đứng trong một tập như $S_1=\{a,d\}$ là tên phần tử của dữ kiện Ví dụ 3.8, giữ nguyên theo sách.
- Chữ $\pi$ là hoán vị ở MinHash (Mục 1–3); trong $1-\theta/\pi$ và các góc của Mục 3.3, 4.2, 4.3, $\pi$ là hằng số.
- Chữ $L$ là độ dài dãy con chung dài nhất (Mục 3.4); $L$ trong giả mã của Thuật toán 06.4 là một danh sách thùng, còn $L_q$ là tên chuẩn. Chữ $k$ là độ dài shingle ở phần tiên quyết, khóa dải ở Thuật toán 06.4 và chỉ số khoảng ở Mục 4.3 cùng Bài tập 06.25–06.26; nghĩa được nêu tại chỗ.
- Chữ $u$ không chỉ số là hướng chiếu, còn $u_{j,z}$ là cỡ thùng. Chữ $z$ có hai chỉ số $z_{j,c}$ là tuple; ba điểm của Bài 3.7.5 được ký hiệu $z_1,z_2,z_3$ (sách viết $p_1,p_2,p_3$, trùng với hai cận của họ nhạy cảm); vector $z$ không chỉ số trong Bài 3.7.2 giữ tên của đề sách.
- Sách nguồn là Leskovec, Rajaraman và Ullman, *Mining of Massive Datasets* (MMDS), ấn bản 3, Chương 3. Số liệu trong các Ví dụ 3.8, 3.10–3.24 và các Bài 3.4.1–3.8.2 là số của sách. Vết chạy phân dải với $b=2$, $r=1$ trên dữ kiện Ví dụ 3.8, dữ kiện các bài tập không mang số bài sách và giả định thời gian $1\,\mu\mathrm{s}$ mỗi cặp là số liệu áp dụng của bản soạn. Sách đo góc bằng độ trong biểu thức $(180-d)/180$; ở đây góc đo bằng radian và bộ tham số viết $1-d/\pi$.

## Bản đồ chủ đề

Nhóm **cốt lõi** tạo mạch chính; **cầu nối** phát biểu lại tiên quyết; **bổ sung** lấp một khoảng trống cụ thể của nguồn; **đọc thêm** không cần để đạt mục tiêu.

| Chủ đề (`note-topic-id`) | Nhóm | Mục | Vai trò → sản phẩm dùng tiếp |
|---|---|---|---|
| Kiến thức tiên quyết (`lec-06-topic-18`) | cầu nối | Tiên quyết | Định lý MinHash, chữ ký, công cụ xác suất → Mục 1–2 |
| Bài toán tìm cặp (`lec-06-topic-01`) | cốt lõi | 1 | Kho một triệu tài liệu, đặc tả tập ứng viên → nhu cầu phân dải |
| Phân dải, khử lặp, xác minh (`lec-06-topic-02`) | cốt lõi | 2.1–2.2 | Khóa dải, Thuật toán 06.4, tính đúng → xác suất và chi phí |
| Xác suất, ngưỡng, hai loại sai số (`lec-06-topic-03`) | cốt lõi | 2.3–2.4 | $P_{b,r}(s)$, $s_{1/2}$, chọn $b$, $r$ → chi phí, phép ghép |
| Chi phí tạo và kiểm cặp (`lec-06-topic-04`) | bổ sung | 2.5 | $Q$, $K$, trường hợp xấu nhất → giới hạn của bảo đảm |
| Độ đo khoảng cách (`lec-06-topic-05`) | cốt lõi | 3.1–3.5 | Năm độ đo trên tập, vector, chuỗi → miền của họ nhạy cảm |
| Họ nhạy cảm theo tính cục bộ (`lec-06-topic-06`) | cốt lõi | 3.6 | Hai bảo đảm gần, xa → phép ghép |
| Phép ghép AND và OR (`lec-06-topic-07`) | cốt lõi | 3.7 | Biến đổi bộ tham số; phân dải là AND rồi OR → ba họ cơ sở |
| Họ chọn tọa độ (`lec-06-topic-08`) | cốt lõi | 4.1 | Xác suất $1-d_H/D$ → họ cho Hamming |
| Siêu phẳng và chữ ký dấu (`lec-06-topic-09`) | cốt lõi | 4.2 | Xác suất $1-\theta/\pi$, ước lượng góc → họ cho góc |
| Chiếu có dịch ngẫu nhiên (`lec-06-topic-10`) | cốt lõi; dịch đều là bổ sung | 4.3 | Bộ tham số $(a/2,2a,1/2,1/3)$ trong hai chiều → họ cho Euclid |
| Chi phí tính chữ ký ba họ (`lec-06-topic-17`) | bổ sung | 4.4 | Bảng đếm phép tính → so sánh với chi phí phân dải |
| Đối sánh thực thể (`lec-06-topic-11`) | cốt lõi | 5.1 | Ba hàm khóa cố định → Tình huống 06.1 |
| Đối sánh vân tay (`lec-06-topic-12`) | cốt lõi | 5.2 | Hàm ba ô, $q_F$, $q_T$ → Tình huống 06.2, Bài tập 06.28 |
| Bản tin gần trùng (`lec-06-topic-13`) | cốt lõi | 5.3 | Shingle theo từ dừng → Tình huống 06.3 |
| Tình huống áp dụng (`lec-06-topic-19`) | cốt lõi | Tình huống | Bốn bài toán giải trọn, hai tình huống giả thiết không thỏa → tóm tắt |
| Tóm tắt chương (`lec-06-topic-14`) | cốt lõi | Tóm tắt | Chuỗi kết quả, giả thiết hay bị bỏ quên → Bài 07 |
| Bài tập củng cố (`lec-06-topic-16`) | cốt lõi | Bài tập | Kiểm năm mục tiêu, sáu cụm bài sách |
| Đọc thêm và tài liệu (`lec-06-topic-15`) | đọc thêm | Tham khảo | Ánh xạ mục ↔ nguồn, các nhánh đọc tiếp |

Các độ đo ở Mục 3.1–3.5 là khái niệm phụ, không có thuật toán riêng, nên đi theo chu trình rút gọn: ví dụ, định nghĩa, tính chất và chứng minh, không có giả mã hay bảng chi phí. Nội dung đọc thêm của nguồn (tổ chức phân dải trên MapReduce, phép ghép 256 hàm, mở rộng định tính của họ Euclid) chỉ được chỉ dẫn ở mục tham khảo.

<!-- note-topic-id: lec-06-topic-01 -->
## 1. Bài toán tìm cặp tương đồng

Bài 05 kết thúc với một cách so hai tài liệu nhanh: thay hai tập shingle lớn bằng hai cột chữ ký MinHash dài $n$, rồi lấy tỷ lệ hàng trùng $\widehat s$ làm ước lượng của Jaccard, vì mỗi hàng trùng với xác suất đúng bằng Jaccard (ghi chú Bài 05, Mục 6–7). Kết quả đó giảm chi phí so một cặp. Nó chưa giảm số cặp phải so, và với một kho lớn, số cặp mới là đại lượng quyết định thời gian chạy.

::: example Ví dụ 06.1 (Kho một triệu tài liệu)
**Dữ kiện.** Theo Ví dụ 3.10 của MMDS (tr.92), kho có $C=10^6$ tài liệu; mỗi chữ ký có $n=250$ thành phần, mỗi thành phần là số nguyên 4 byte. Ta thêm giả định mỗi lần so một cặp chữ ký mất $1\,\mu\mathrm{s}$.

**Dung lượng chữ ký.** Ma trận chữ ký chiếm $10^6\cdot250\cdot4=10^9$ byte, tức khoảng 1 GB, vừa bộ nhớ chính của một máy.

**Số cặp.** Số cặp không thứ tự của $C$ tài liệu là số tổ hợp chập hai:

$$
\binom{10^6}{2}=\frac{10^6\cdot(10^6-1)}{2}=499\,999\,500\,000.
$$

Như vậy, so mọi cặp nghĩa là khoảng $5\cdot10^{11}$ lần so chữ ký.

**Thời gian.** Với $1\,\mu\mathrm{s}=10^{-6}$ giây mỗi cặp, tổng thời gian là $499\,999{,}5$ giây. Chia cho $86\,400$ giây mỗi ngày, ta được khoảng $5{,}787$ ngày.

**Kiểm tra lại.** $500\,000\cdot999\,999=499\,999\,500\,000$, khớp với số cặp ở trên.
:::

Ví dụ 06.1 tách hai chi phí. Chữ ký làm chi phí mỗi cặp nhỏ và làm dữ liệu vừa bộ nhớ; số cặp vẫn tăng theo bình phương số tài liệu. Con số $5{,}787$ ngày là phép tính dưới một giả định về thời gian mỗi cặp, không phải số đo của một hệ thống.

Để rút ngắn thời gian, chúng ta cần một thủ tục chỉ đưa ra một phần nhỏ các cặp để xác minh, và cần biết thủ tục ấy bỏ mất những cặp nào.

Một cách trực quan, chúng ta muốn một bộ lọc rẻ đặt các tài liệu giống nhau vào chung nhóm, rồi chỉ so các cặp trong cùng nhóm. Bộ lọc được phép sai theo hai hướng: để lọt cặp không đủ giống, và bỏ mất cặp đủ giống. Mô tả này chưa phải định nghĩa; định nghĩa sau đặt tên cho tập cặp mà bộ lọc trả về và cho hai loại sai.

::: definition Định nghĩa 06.1 (Bài toán tìm cặp tương đồng)
Cho $C$ tài liệu với các tập đặc trưng hữu hạn, không rỗng $S_1,\ldots,S_C$, và một ngưỡng chấp nhận $t\in[0,1]$.

**Bài toán tìm cặp tương đồng** là tính tập mọi cặp $(c,d)$ với $1\le c<d\le C$ và $\mathrm{SIM}(S_c,S_d)\ge t$.

Một **bộ tạo ứng viên** là thủ tục trả về một tập cặp $\mathcal C\subseteq\{(c,d):1\le c<d\le C\}$; mỗi phần tử của $\mathcal C$ là một **cặp ứng viên** (candidate pair).

**Xác minh** là bước tính Jaccard gốc $\mathrm{SIM}(S_c,S_d)$ cho từng cặp của $\mathcal C$ và giữ cặp có giá trị ít nhất $t$.

Một **ứng viên giả** (false positive) là cặp thuộc $\mathcal C$ có $\mathrm{SIM}(S_c,S_d)<t$. Một **cặp bỏ sót** (false negative) là cặp có $\mathrm{SIM}(S_c,S_d)\ge t$ nhưng không thuộc $\mathcal C$.
:::

Định nghĩa 06.1 chia việc tìm cặp thành hai bước có vai trò khác nhau. Bộ tạo ứng viên quyết định cặp nào được xét. Bước xác minh dùng dữ liệu gốc nên phán quyết của nó chính xác trên các cặp được xét. Hệ quả là hai loại sai có bản chất khác nhau: ứng viên giả chỉ tốn thêm một lần xác minh rồi bị loại, còn cặp bỏ sót không bao giờ được xét nên không bước nào sau đó tìm lại được.

Định nghĩa bao hàm Ví dụ 06.1 như một trường hợp biên. Bộ tạo tầm thường trả mọi cặp: nó không có cặp bỏ sót, nhưng $\lvert\mathcal C\rvert=499\,999\,500\,000$ và ta quay lại đúng phép so mọi cặp. Ở đầu kia, bộ tạo trả tập rỗng không tốn gì nhưng bỏ sót mọi cặp đạt ngưỡng. Một bộ tạo hữu ích nằm giữa hai cực này.

Băm nhạy cảm theo tính cục bộ (LSH) là tên chung của các bộ tạo ứng viên dùng hàm băm sao cho cặp càng giống càng dễ rơi vào cùng thùng.

::: remark Nhận xét 06.2 (Hai đại lượng $s$ và $\widehat s$)
Với một cặp cố định $(c,d)$, ta viết $s=\mathrm{SIM}(S_c,S_d)$ cho Jaccard của hai tập gốc và $\widehat s$ cho tỷ lệ hàng trùng của hai cột chữ ký. Đại lượng $s$ là tính chất của dữ liệu; $\widehat s$ còn phụ thuộc các hoán vị đã chọn khi lập chữ ký.

Ví dụ 3.8 của MMDS (tr.85–86) cho $S_1=\{a,d\}$, $S_4=\{a,c,d\}$ và hai hàng chữ ký trong đó cột 1 và cột 4 đều bằng $(1,0)$. Khi đó $\widehat s=1$, trong khi $s=2/3$. Định nghĩa 06.1 đặt ngưỡng trên $s$, nên bước xác minh tính $s$; giá trị $\widehat s$ chỉ dùng để tổ chức bộ tạo ứng viên.
:::

Bộ tạo ứng viên cần chạy trên dữ liệu đã có sau Bài 05, tức ma trận chữ ký, và không được duyệt mọi cặp. Hình sau cho cấu trúc của chương dưới dạng một quy trình bốn khối.

![Sơ đồ bốn khối nối từ trái sang phải: "Chữ ký" (ma trận chữ ký của các tài liệu), "Khóa dải" (mỗi cột tạo khóa từ từng dải), "Ứng viên" (tập cặp duy nhất trước khi xác minh) và "Kiểm tập gốc" (tính Jaccard trên tập gốc và giữ cặp đạt ngưỡng).](img/lec-06/quy-trinh-cap.svg)

Hình đọc từ trái sang phải theo đường đi của dữ liệu. Mục 2 xây hai khối giữa: lập khóa dải từ chữ ký, gom các cột cùng khóa và lấy hợp các cặp thành tập ứng viên $\mathcal C$; khối cuối là bước xác minh của Định nghĩa 06.1.

Mục 3 và Mục 4 thay khối đầu: chữ ký MinHash chỉ phục vụ Jaccard trên tập, nên với vector và chuỗi chúng ta cần một họ hàm băm khác hợp với độ đo đang dùng. Mục 5 đổi cách biểu diễn dữ liệu trước khối đầu cho ba bài toán cụ thể, còn hai khối cuối giữ nguyên.

::: exercise Bài tập 06.1
Dữ kiện: kho $C=10^6$ tài liệu, chữ ký $n=250$ thành phần 4 byte, giả định $1\,\mu\mathrm{s}$ mỗi lần so cặp (Ví dụ 06.1); hai tập $S_1=\{a,d\}$, $S_4=\{a,c,d\}$ có hai cột chữ ký cùng bằng $(1,0)$ (Nhận xét 06.2).

(a) Với chữ ký đã vừa bộ nhớ, nêu giới hạn còn lại của phép so mọi cặp và tập trung gian cần tạo trước khi tính Jaccard gốc.

(b) Với $C=10^5$ tài liệu và cùng giả định thời gian, tính số cặp, tổng thời gian và số lần số cặp giảm so với $C=10^6$.

(c) Cặp $(1,4)$ có $\widehat s=1$ và $s=2/3$. Nêu đại lượng quyết định cặp có đạt ngưỡng $t$ hay không.
:::

::: hint
Câu (b) dùng $\binom C2=C(C-1)/2$. Câu (c) xét bước nào của Định nghĩa 06.1 so với ngưỡng.
:::

::: solution
(a) Số cặp vẫn là $\binom{10^6}{2}=499\,999\,500\,000$. Cần tạo tập ứng viên $\mathcal C$ rồi chỉ tính Jaccard gốc trên các cặp trong tập này. Chữ ký ngắn giảm dữ liệu mỗi cặp nhưng chưa giảm số cặp.

(b) $\binom{10^5}{2}=4\,999\,950\,000$ cặp. Với $10^{-6}$ giây mỗi cặp, tổng thời gian khoảng $5\,000$ giây, gần $1{,}4$ giờ. Giảm số tài liệu 10 lần làm số cặp giảm khoảng 100 lần, vì số cặp tăng theo bình phương số tài liệu.

(c) Đại lượng quyết định là $s=\mathrm{SIM}(S_1,S_4)$, tính ở bước xác minh trên tập gốc. Giá trị $\widehat s=1$ chỉ là tỷ lệ trùng của hai hàng chữ ký đã lấy.

**Kiểm tra lại.** $499\,999\,500\,000/4\,999\,950\,000\approx100{,}0009$, khớp với "khoảng 100 lần".
:::

Như vậy, chúng ta đã đặt bài toán tìm cặp tương đồng (Định nghĩa 06.1), tách bộ tạo ứng viên khỏi bước xác minh và đặt tên cho hai loại sai; Ví dụ 06.1 cho thấy chữ ký đã giải quyết bộ nhớ nhưng chưa giải quyết số cặp. Tuy nhiên, định nghĩa chỉ nói bộ tạo phải trả về điều gì, chưa cho cách dựng một bộ tạo không duyệt mọi cặp, và chưa cho cách đo số cặp bỏ sót. Trong Mục 2, chúng ta dựng bộ tạo đầu tiên từ chính ma trận chữ ký bằng phép phân dải, chứng minh tính đúng của nó, tính xác suất một cặp được xét và đếm công việc còn lại.

## 2. Phân dải chữ ký MinHash

Sau Mục 1, kho một triệu tài liệu vẫn có khoảng $5\cdot10^{11}$ cặp, và bộ tạo ứng viên duy nhất chúng ta có là bộ tạo tầm thường trả mọi cặp. Dữ liệu sẵn có là ma trận chữ ký $\mathrm{SIG}\in V^{n\times C}$, có một cột cho mỗi tài liệu, cùng định lý MinHash: mỗi hàng của hai cột trùng nhau với xác suất bằng Jaccard của hai tập gốc. Việc cần làm là biến tính chất đó thành một bộ tạo ứng viên không duyệt mọi cặp, rồi đo cái giá của nó bằng xác suất bỏ sót và số phép xác minh.

<!-- note-topic-id: lec-06-topic-02 -->
### 2.1 Dải, khóa dải và tập ứng viên

Theo §3.4.1 của MMDS, cách tiếp cận chung của LSH là băm mỗi đối tượng nhiều lần sao cho đối tượng giống nhau dễ rơi vào cùng thùng hơn đối tượng khác nhau, rồi coi mọi cặp chung thùng ở ít nhất một lần băm là cặp ứng viên. Với chữ ký MinHash, một lựa chọn thô là dùng một hàng làm khóa băm. Khi đó cặp có Jaccard $0{,}3$ chung thùng với xác suất $0{,}3$, nên rất nhiều cặp xa thành ứng viên. Chúng ta cần một khóa khắt khe hơn một hàng nhưng vẫn cho cặp gần nhiều cơ hội gặp nhau.

Một cách trực quan, chúng ta cắt chữ ký thành nhiều đoạn ngắn và dùng mỗi đoạn làm một khóa. Hai cột chỉ chung khóa ở một đoạn khi trùng mọi hàng của đoạn ấy, điều dễ xảy ra với cột rất giống nhau và hiếm với cột ít giống. Vì có nhiều đoạn, một cặp giống nhau có nhiều cơ hội trùng ít nhất một đoạn. Mô tả này chưa phải định nghĩa; ví dụ sau cho thấy vì sao phải so cả đoạn chứ không so từng hàng.

::: example Ví dụ 06.2 (Năm cột, dải ba hàng)
**Dữ kiện.** Theo Ví dụ 3.11 và Hình 3.7 của MMDS (tr.92–93), chữ ký có $n=12$ hàng chia thành $b=4$ dải, mỗi dải $r=3$ hàng. Hình 3.7 của sách chỉ cho dải đầu; năm cột của dải này là

$$
(1,3,0),\quad (0,2,1),\quad (0,1,3),\quad (0,2,1),\quad (2,2,1).
$$

**Tính.** Cột 2 và cột 4 có cùng bộ ba giá trị $(0,2,1)$, nên chung thùng ở dải đầu. Cột 2 và cột 3 chỉ trùng thành phần đầu, bằng $0$; hai bộ ba khác nhau nên hai cột khác thùng. Cột 5 trùng hai thành phần cuối với cột 2 nhưng khác thành phần đầu, nên cũng khác thùng.

**Kết luận.** Trong mười cặp của năm cột, chỉ cặp $(2,4)$ chung thùng ở dải đầu. Chín hàng còn lại không được cho, nên chưa kết luận được cặp $(2,3)$ có chung thùng ở một dải khác hay không.

**Kiểm tra lại.** Năm bộ ba có bốn giá trị phân biệt, trong đó chỉ $(0,2,1)$ xuất hiện hai lần, ứng với đúng một cặp.
:::

Ví dụ 06.2 cho thấy điều kiện chung thùng ở một dải là trùng mọi hàng của dải, không phải trùng một hàng. Định nghĩa sau phát biểu điều kiện này cho mọi dải và đưa số dải vào khóa.

::: definition Định nghĩa 06.3 (Dải, khóa dải và tập ứng viên)
Cho ma trận chữ ký $\mathrm{SIG}\in V^{n\times C}$ và hai số nguyên dương $b$, $r$ với $n=br$.

**Dải** thứ $j$, $1\le j\le b$, gồm các hàng $(j-1)r+1,\ldots,jr$ của $\mathrm{SIG}$.

**Tuple** của cột $c$ ở dải $j$ là bộ $r$ giá trị có thứ tự $z_{j,c}=\bigl(\mathrm{SIG}_{(j-1)r+1,\,c},\ldots,\mathrm{SIG}_{jr,\,c}\bigr)\in V^r$.

**Khóa dải** của cột $c$ ở dải $j$ là $k_{j,c}=(j,z_{j,c})$. Hai cột $c$, $d$ **trùng dải** $j$ khi $k_{j,c}=k_{j,d}$. **Thùng** của khóa $k$ là tập các cột có khóa dải bằng $k$.

**Tập ứng viên của phân dải** là

$$
\mathcal C=\{(c,d):1\le c<d\le C,\ \exists j\in\{1,\ldots,b\}:\ k_{j,c}=k_{j,d}\}.
$$
:::

Định nghĩa có ba thành phần. Tham số $r$ quyết định độ khắt khe của một phép thử: hai cột phải trùng cả $r$ hàng của dải. Tham số $b$ quyết định số phép thử: chỉ cần trùng một trong $b$ dải. Khóa chứa cả số dải $j$, nên hai tuple bằng nhau ở hai dải khác nhau không tạo cùng khóa; nếu bỏ $j$, hai cột không trùng ở dải nào vẫn có thể chung thùng. Công thức của $\mathcal C$ đọc là: một cặp là ứng viên khi tồn tại ít nhất một dải mà ở đó hai cột trùng mọi hàng.

Định nghĩa bao hàm Ví dụ 06.2 như sau: $k_{1,2}=k_{1,4}=(1,(0,2,1))$, nên $(2,4)\in\mathcal C$; còn cặp $(2,3)$ thuộc $\mathcal C$ hay không phụ thuộc ba dải chưa được cho. Đòi trùng mọi hàng trong một dải là một phép ghép đồng thời, còn nhận cặp khi trùng ít nhất một dải là một phép ghép ít nhất một; Mục 3.7 định nghĩa hai phép ghép này cho mọi họ hàm băm (Định nghĩa 06.25) và chỉ ra phân dải là trường hợp riêng (Nhận xét 06.27). Ở đây chúng ta chỉ dùng hai tên gọi này để đọc định nghĩa.

![Ma trận chữ ký có n hàng chia thành bốn dải chồng lên nhau theo chiều dọc; mỗi dải gồm r hàng và tạo một khóa ghi là (1, tuple), (2, tuple), (3, tuple), (4, tuple); chú thích ghi b dải, mỗi dải r hàng, n = br.](img/lec-06/phan-dai-chu-ky.svg)

Trên hình, mỗi dải là một khối hàng liên tiếp; khóa bên phải mỗi dải mang số thứ tự của dải trước tuple. Hình ứng với các dòng "dải", "tuple" và "khóa dải" của Định nghĩa 06.3, với $b=4$ như Ví dụ 06.2.

### 2.2 Thuật toán phân dải và tính đúng

Định nghĩa 06.3 mô tả $\mathcal C$ bằng một điều kiện "tồn tại $j$" trên từng cặp. Kiểm điều kiện ấy cho từng cặp lại là duyệt mọi cặp. Để tránh điều đó, chúng ta gom các cột theo khóa vào thùng rồi chỉ phát cặp bên trong mỗi thùng. Ví dụ sau chạy tay toàn bộ quy trình trên dữ kiện của Bài 05.

::: example Ví dụ 06.3 (Bốn tập đặc trưng)
**Dữ kiện.** Theo Ví dụ 3.8 của MMDS (tr.85–86), bốn tập là

$$
S_1=\{a,d\},\quad S_2=\{c\},\quad S_3=\{b,d,e\},\quad S_4=\{a,c,d\},
$$

với ma trận chữ ký hai hàng đã tính ở Bài 05:

| Hàng chữ ký | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| 1 | 1 | 3 | 0 | 1 |
| 2 | 0 | 2 | 0 | 0 |

Ta chọn $b=2$, $r=1$ và ngưỡng $t=2/3$. Mỗi hàng là một dải; khóa của cột $c$ ở dải $j$ là $(j,(\mathrm{SIG}_{j,c}))$.

**Dựng thùng.** Bắt đầu với từ điển thùng $B$ rỗng. Ở dải 1, cột 1 tạo danh sách mới tại khóa $(1,(1))$; cột 2 tạo danh sách tại $(1,(3))$; cột 3 tạo danh sách tại $(1,(0))$; cột 4 có khóa $(1,(1))$ đã có nên được nối vào danh sách của cột 1. Ở dải 2, cột 1 tạo danh sách tại $(2,(0))$, cột 2 tạo danh sách tại $(2,(2))$, cột 3 và cột 4 được nối vào danh sách $(2,(0))$. Tổng cộng có $bC=8$ lượt chèn.

| Dải | Khóa | Danh sách mã | Cặp phát |
|---|---|---|---|
| 1 | $(1,(1))$ | 1, 4 | $(1,4)$ |
| 1 | $(1,(3))$ | 2 | không có |
| 1 | $(1,(0))$ | 3 | không có |
| 2 | $(2,(0))$ | 1, 3, 4 | $(1,3)$, $(1,4)$, $(3,4)$ |
| 2 | $(2,(2))$ | 2 | không có |

**Phát và khử lặp.** Có bốn lượt phát cặp; cặp $(1,4)$ được phát hai lần, một lần ở mỗi dải. Hợp các cặp vào tập $\mathrm{CAND}$ cho ba cặp phân biệt, đúng là tập ứng viên của dữ kiện này:

$$
\mathrm{CAND}=\mathcal C=\{(1,3),(1,4),(3,4)\}.
$$

**Xác minh.** Ba phép tính Jaccard gốc cho

$$
\mathrm{SIM}(S_1,S_3)=\frac14,\qquad
\mathrm{SIM}(S_1,S_4)=\frac23,\qquad
\mathrm{SIM}(S_3,S_4)=\frac15.
$$

Chỉ $(1,4)$ đạt ngưỡng $2/3$, nên tập kết quả là $\mathrm{OUT}=\{(1,4)\}$; hai cặp $(1,3)$ và $(3,4)$ là ứng viên giả.

**Kiểm tra lại.** $S_1\cap S_3=\{d\}$ và $S_1\cup S_3=\{a,b,d,e\}$ cho $1/4$; $S_1\cap S_4=\{a,d\}$ và $S_1\cup S_4=\{a,c,d\}$ cho $2/3$; $S_3\cap S_4=\{d\}$ và $S_3\cup S_4=\{a,b,c,d,e\}$ cho $1/5$. Tài liệu 2 không chung khóa với tài liệu nào nên không xuất hiện trong $\mathcal C$.
:::

Ví dụ 06.3 dùng hai hàm MinHash cố định, nên mọi bước đều xác định. Thuật toán sau viết lại các bước ấy cho dữ liệu tổng quát, với đúng tên gọi của ví dụ: từ điển thùng $B$, tập cặp $\mathrm{CAND}$ và tập kết quả $\mathrm{OUT}$.

::: algorithm Thuật toán 06.4 (Phân dải và xác minh)
**Đầu vào.** Ma trận chữ ký $\mathrm{SIG}\in V^{n\times C}$; các tập gốc hữu hạn, không rỗng $S_1,\ldots,S_C$; hai số nguyên dương $b$, $r$ với $n=br$; ngưỡng $t\in[0,1]$.

**Đầu ra.** Tập $\mathrm{OUT}=\{(c,d)\in\mathcal C:\ \mathrm{SIM}(S_c,S_d)\ge t\}$, với $\mathcal C$ của Định nghĩa 06.3.

**Giả thiết.** $B$ là bảng băm (hash table) so khóa đầy đủ; sau khi đọc khóa, tra và chèn tốn thời gian kỳ vọng $O(1)$. Đọc và sao chép một tuple dài $r$ tốn $O(r)$.

1. Khởi tạo $B$ là từ điển rỗng, $\mathrm{CAND}$ và $\mathrm{OUT}$ là tập rỗng.
2. Với mỗi dải $j=1,\ldots,b$ và mỗi cột $c=1,\ldots,C$: sao chép tuple $z\leftarrow z_{j,c}$, đặt $k\leftarrow(j,z)$; nếu $k$ chưa có trong $B$ thì tạo $B[k]$ là danh sách rỗng; nối $c$ vào cuối $B[k]$.
3. Với mỗi danh sách $L$ của $B$ và mỗi cặp $c<d$ thuộc $L$: thêm $(c,d)$ vào $\mathrm{CAND}$.
4. Với mỗi $(c,d)\in\mathrm{CAND}$: tính $\mathrm{SIM}(S_c,S_d)$; nếu giá trị ít nhất $t$ thì thêm $(c,d)$ vào $\mathrm{OUT}$.
5. Trả $\mathrm{OUT}$.

```text
B ← từ điển rỗng; CAND ← tập rỗng; OUT ← tập rỗng
với j = 1, …, b:
    với c = 1, …, C:
        z ← bản sao SIG[(j−1)r+1 : jr, c]
        k ← (j, z)
        nếu k chưa có trong B: B[k] ← danh sách rỗng
        B[k].append(c)
với mỗi danh sách L trong B:
    với mỗi c < d thuộc L: CAND.add((c, d))
với mỗi (c, d) trong CAND:
    nếu SIM(S_c, S_d) ≥ t: OUT.add((c, d))
trả OUT
```

**Dừng.** Bước 2 có $bC$ lượt; bước 3 duyệt hữu hạn danh sách, mỗi danh sách hữu hạn; bước 4 duyệt $\lvert\mathrm{CAND}\rvert\le\binom C2$ cặp. Thuật toán dừng.

**Trường hợp biên.** Với $C<2$ hoặc khi mọi thùng có ít hơn hai phần tử, bước 3 không phát cặp và $\mathrm{OUT}$ rỗng. Tập gốc rỗng nằm ngoài đầu vào vì Jaccard của hai tập rỗng không xác định.

**Chi phí.** Gọi $Q$ là số lượt thêm cặp ở bước 3, $K=\lvert\mathrm{CAND}\rvert$ và $T_J(c,d)$ là thời gian tính Jaccard gốc của cặp $(c,d)$; Mệnh đề 06.11 chứng minh bảng sau.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2: sao chép tuple, tra và chèn | $bC$ | $O(r)$ kỳ vọng | $O(nC)$ |
| 3: phát cặp vào tập | $Q$ | $O(1)$ kỳ vọng | $O(Q)$ |
| 4: xác minh | $K$ | $T_J(c,d)$ | $\sum_{(c,d)\in\mathcal C}T_J(c,d)$ |
:::

Thuật toán 06.4 thay điều kiện "tồn tại $j$" bằng việc gom cột: thao tác quyết định là nối mã cột vào danh sách của khóa dải của nó ở bước 2. Sau đó bước 3 chỉ xét các cặp nằm chung một danh sách, nên không lúc nào thuật toán duyệt mọi cặp của kho. Ví dụ 06.3 là một lượt chạy của thuật toán: bước 2 thực hiện 8 lượt chèn, bước 3 có 4 lượt phát và để lại 3 cặp, bước 4 tính 3 giá trị Jaccard.

Thuật toán có trả đúng tập $\mathcal C$ của Định nghĩa 06.3 không, kể cả khi một cặp chung thùng ở nhiều dải? Mệnh đề sau trả lời bằng một bất biến của bước 2.

::: proposition Mệnh đề 06.5 (Tính đúng của phân dải và xác minh)
**Giả thiết.** Ma trận $\mathrm{SIG}$ được cho và không đổi trong lần chạy; bảng $B$ so khóa đầy đủ $(j,z)$, gồm cả số dải; các tập $S_1,\ldots,S_C$ hữu hạn, không rỗng.

**Kết luận.** Thuật toán 06.4 dừng và trả đúng tập $\{(c,d)\in\mathcal C:\ \mathrm{SIM}(S_c,S_d)\ge t\}$.

**Điều kiện áp dụng.** Mọi $C\ge1$, mọi $b,r\ge1$ với $n=br$, mọi $t\in[0,1]$.

**Phạm vi.** Mệnh đề chỉ nói về các cặp trong $\mathcal C$. Nó không khẳng định mọi cặp đạt ngưỡng đều thuộc $\mathcal C$; xác suất điều đó xảy ra là nội dung của Định lý 06.7.
:::

::: proof Chứng minh Mệnh đề 06.5
Ý tưởng: bước 2 giữ một bất biến về các danh sách; khi bước 2 kết thúc, bất biến cho biết hai cột chung danh sách đúng khi chúng trùng một khóa dải. Phần còn lại là đọc bước 3 và bước 4.

**Bước 1 (bất biến và khởi tạo).** Bất biến của dải $j$ là: sau mỗi lượt chèn, mỗi cột đã xử lý ở dải $j$ nằm đúng một lần trong danh sách của khóa $k_{j,c}$; mỗi danh sách có khóa mang chỉ số $j$ chỉ chứa các cột đã xử lý có khóa đó; các danh sách của những dải trước không đổi. Ở đầu dải $j$, chưa có cột nào được xử lý ở dải này và, vì số dải nằm trong khóa, chưa có danh sách nào có khóa mang chỉ số $j$; hai vế đầu vì vậy không có trường hợp nào cần kiểm. Vế thứ ba đúng vì chưa có lượt chèn nào của dải $j$.

**Bước 2 (duy trì).** Xét lượt chèn cột $c$ ở dải $j$. Khóa $k=(j,z_{j,c})$ được tính đúng từ các hàng của dải $j$. Nếu $k$ mới, một danh sách rỗng được tạo; nếu $k$ đã có, các mã trong danh sách được giữ nguyên. Nối $c$ vào $B[k]$ đặt $c$ vào đúng danh sách của khóa của nó và không chạm danh sách nào khác, vì bảng so khóa đầy đủ nên chỉ một danh sách ứng với $k$. Bất biến được duy trì.

**Bước 3 (kết thúc dựng thùng).** Khi bước 2 xử lý xong mọi dải, theo Bước 1 và Bước 2, danh sách của khóa $(j,z)$ là đúng tập $\{c:\ z_{j,c}=z\}$. Do đó hai cột $c$, $d$ cùng nằm trong một danh sách khi và chỉ khi tồn tại $j$ với $k_{j,c}=k_{j,d}$.

**Bước 4 (phát cặp và xác minh).** Bước 3 của Thuật toán 06.4 thêm $(c,d)$ vào $\mathrm{CAND}$ đúng khi $c$, $d$ chung một danh sách; $\mathrm{CAND}$ là tập nên một cặp chung nhiều danh sách chỉ có mặt một lần. Theo kết luận của Bước 3 (kết thúc dựng thùng) và Định nghĩa 06.3, $\mathrm{CAND}=\mathcal C$. Bước 4 của Thuật toán 06.4 tính Jaccard, xác định vì các tập không rỗng, và giữ đúng các cặp có giá trị ít nhất $t$.

**Bước 5 (dừng).** Theo mục Dừng của Thuật toán 06.4, mọi vòng lặp hữu hạn. $\square$
:::

Mệnh đề 06.5 nói rằng sai số của phân dải không đến từ thuật toán: trên tập $\mathcal C$, kết quả chính xác. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ phép so khóa đầy đủ, chỉ so ô của bảng băm lưu trữ: nếu hai khóa $(1,(1))$ và $(1,(3))$ của Ví dụ 06.3 rơi vào cùng ô, danh sách của ô chứa các cột 1, 4 và 2, nên cặp $(1,2)$ được phát dù hai cột không trùng dải nào. Khi đó $\mathrm{CAND}\ne\mathcal C$, và với ngưỡng $t=0$ cặp $(1,2)$ còn xuất hiện trong đầu ra.
- Bỏ số dải khỏi khóa: với $C=2$, $b=2$, $r=1$, cột 1 bằng $(1,2)$ và cột 2 bằng $(2,1)$, hai cột không trùng dải nào nên $\mathcal C=\varnothing$. Nếu khóa chỉ là tuple, giá trị $(1)$ của cột 1 ở dải 1 và của cột 2 ở dải 2 rơi vào cùng thùng, nên cặp $(1,2)$ được phát.
- Bỏ điều kiện tập không rỗng: với $S_c=S_d=\varnothing$, thương $\lvert S_c\cap S_d\rvert/\lvert S_c\cup S_d\rvert$ có dạng $0/0$, nên bước 4 không xác định.

Bước 2 của chứng minh dùng phép so khóa đầy đủ và số dải trong khóa; Bước 4 dùng điều kiện tập không rỗng. Giả thiết ma trận không đổi cho phép đọc mệnh đề như một phát biểu xác định: tính ngẫu nhiên chỉ nằm ở lúc lập chữ ký, trước khi thuật toán chạy.

::: remark Nhận xét 06.6 (Bước lọc theo $\widehat s$)
Quy trình ở §3.4.3 của MMDS (tr.95–96) kiểm tỷ lệ trùng chữ ký $\widehat s$ của các ứng viên, rồi ghi bước kiểm tài liệu gốc là tùy chọn. Thuật toán 06.4 bỏ bước lọc theo $\widehat s$ và luôn kiểm Jaccard gốc. Lọc theo $\widehat s$ có thể thêm cặp bỏ sót: một cặp có $s\ge t$ nhưng $\widehat s<t$ sẽ bị loại trước khi tính $s$. Với Nhận xét 06.2, cặp $(1,4)$ có $\widehat s=1$ còn $s=2/3$, nên với chữ ký hai hàng, hai đại lượng lệch nhau $1/3$.
:::

**Trong thực hành.** Từ điển $B$ thường là bảng băm có khóa là bộ $(j,\text{tuple})$; ngôn ngữ có kiểu bộ bất biến cho phép dùng trực tiếp bộ này làm khóa. Bảng băm giải va chạm bằng phép so khóa bằng nhau, nên giả thiết so khóa đầy đủ của Mệnh đề 06.5 được bảo đảm bởi cấu trúc dữ liệu chứ không bởi số ô của bảng; MMDS thay điều này bằng giả định có rất nhiều thùng.

Sao chép tuple ở bước 2 làm khóa không phụ thuộc vùng nhớ của $\mathrm{SIG}$. Một cách tổ chức tương đương là dùng $b$ bảng, mỗi dải một bảng, với khóa chỉ là tuple; số dải khi đó nằm ở việc chọn bảng.

::: exercise Bài tập 06.2
Dữ kiện: $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$, $S_4=\{a,c,d\}$; ma trận chữ ký có hai hàng $(1,3,0,1)$ và $(0,2,0,0)$; ngưỡng $t=2/3$ (Ví dụ 06.3).

(a) Với $b=2$, $r=1$, giải thích vì sao cặp $(1,4)$ được phát hai lần nhưng chỉ được xác minh một lần.

(b) Với $b=1$, $r=2$, xác định các thùng, số lượt phát cặp, số cặp ứng viên phân biệt và tập kết quả.
:::

::: hint
Ở câu (b), một dải gồm cả hai hàng, nên tuple của mỗi cột là cột chữ ký đầy đủ.
:::

::: solution
(a) Cột 1 và cột 4 trùng ở dải 1 (cùng giá trị 1) và ở dải 2 (cùng giá trị 0), nên mỗi dải phát cặp một lần. Tập $\mathrm{CAND}$ khử lặp, và bước 4 duyệt từng phần tử của tập, nên cặp chỉ được xác minh một lần.

(b) Các tuple là $(1,0)$, $(3,2)$, $(0,0)$, $(1,0)$. Chỉ cột 1 và cột 4 chung thùng, nên có một lượt phát và một cặp ứng viên; tập kết quả vẫn là $\{(1,4)\}$ vì $\mathrm{SIM}(S_1,S_4)=2/3$.

**Kiểm tra lại.** So với $b=2$, $r=1$ của Ví dụ 06.3, đòi trùng cả hai hàng loại được hai ứng viên giả $(1,3)$ và $(3,4)$.
:::

<!-- note-topic-id: lec-06-topic-03 -->
### 2.3 Xác suất thành ứng viên

Mệnh đề 06.5 bảo đảm kết quả đúng trên $\mathcal C$, nhưng một cặp đạt ngưỡng không vào $\mathcal C$ thì bị bỏ sót. Xác suất bỏ sót một cặp có Jaccard $s$ là bao nhiêu, và phụ thuộc $b$, $r$ thế nào? Định lý 06.7 dưới đây trả lời câu hỏi này. Trong Ví dụ 06.3, hai hàm MinHash là cố định nên không có xác suất nào để tính; chúng ta chuyển sang mô hình trong đó $n$ hàm MinHash được chọn ngẫu nhiên khi lập chữ ký, còn cặp tài liệu được cố định trước.

Một cách trực quan, mỗi dải là một phép thử chặt mà cặp phải vượt qua ở cả $r$ hàng, còn $b$ dải cho $b$ lượt thử. Xác suất vượt một dải giảm nhanh khi $s$ giảm, nên cặp xa hiếm khi vượt dải nào; cặp gần có $b$ cơ hội nên hiếm khi trượt mọi dải. Mô tả này chưa phải định lý; ví dụ sau tính các xác suất ấy cho một cặp.

::: example Ví dụ 06.4 (Cặp $s=0{,}8$ qua 20 dải năm hàng)
**Dữ kiện.** Theo Ví dụ 3.12 của MMDS (tr.94–95), chữ ký dài $n=100$ chia thành $b=20$ dải, mỗi dải $r=5$ hàng; một cặp có Jaccard $s=0{,}8$. Mỗi hàng dùng một MinHash chọn độc lập.

**Một dải.** Mỗi hàng trùng với xác suất $0{,}8$, nên cả năm hàng trùng với xác suất $0{,}8^5=0{,}32768$. Dải không trùng với xác suất $1-0{,}32768=0{,}67232$.

**Hai mươi dải.** Không dải nào trùng với xác suất $0{,}67232^{20}\approx0{,}000356058$. Cặp thành ứng viên với xác suất $1-0{,}000356058\approx0{,}999643942$.

**Kiểm tra lại.** Xác suất bỏ sót khoảng $0{,}00036$, tức khoảng 1 trên 2 800 cặp có $s=0{,}8$; sách làm tròn thành 1 trên 3 000.
:::

Ví dụ 06.4 dùng ba phép tính: lũy thừa cho một dải, lũy thừa cho mọi dải, và biến cố bù. Định lý sau phát biểu chuỗi phép tính này cho mọi $s$, $b$, $r$ và chỉ rõ giả thiết của từng phép.

::: theorem Định lý 06.7 (Xác suất thành ứng viên)
**Giả thiết.** Cặp $(c,d)$ cố định, hai tập $S_c$, $S_d$ hữu hạn, không rỗng, có Jaccard $s$. Mỗi thành phần chữ ký là một MinHash lý tưởng: hoán vị được chọn đều trong mọi hoán vị và dùng chung cho mọi tập. Các hoán vị của $n=br$ thành phần được chọn độc lập. Thuật toán 06.4 so khóa dải đầy đủ.

**Kết luận.**

$$
\Pr[(c,d)\in\mathcal C]=P_{b,r}(s)=1-(1-s^r)^b. \tag{2.1}
$$

**Điều kiện áp dụng.** Xác suất lấy theo cách chọn $n$ hoán vị; cặp và hai tập gốc không ngẫu nhiên.

**Phạm vi.** Đây là xác suất của một cặp. Định lý không cần các cặp khác nhau độc lập và không cho tỷ lệ cặp bỏ sót trên toàn kho khi chưa biết phân bố độ tương đồng của các cặp.
:::

::: proof Chứng minh Định lý 06.7
**Bước 1 (một hàng).** Gọi $E_i$ là biến cố hai cột trùng ở hàng thứ $i$ của một dải. Theo định lý MinHash (ghi chú Bài 05, Mục 6), áp dụng cho hoán vị chọn đều dùng chung cho hai tập không rỗng, $\Pr(E_i)=s$.

**Bước 2 (một dải).** Hai cột trùng dải khi trùng cả $r$ hàng, tức biến cố $\bigcap_{i=1}^rE_i$; vì khóa được so đầy đủ, không có cách nào khác để chung thùng. Các hoán vị trong dải độc lập, nên

$$
\Pr\Bigl(\bigcap_{i=1}^rE_i\Bigr)=\prod_{i=1}^r\Pr(E_i)=s^r.
$$

**Bước 3 (không dải nào).** Một dải không trùng với xác suất $1-s^r$. Các dải dùng những hoán vị khác nhau, chọn độc lập, nên $b$ biến cố "dải $j$ không trùng" độc lập và

$$
\Pr[\text{không dải nào trùng}]=(1-s^r)^b.
$$

**Bước 4 (biến cố bù).** Theo Định nghĩa 06.3, cặp thuộc $\mathcal C$ khi có ít nhất một dải trùng, là biến cố bù của biến cố ở Bước 3. Do đó $\Pr[(c,d)\in\mathcal C]=1-(1-s^r)^b$. $\square$
:::

Công thức (2.1) đọc từ trong ra ngoài: $s^r$ là xác suất trùng một dải, $(1-s^r)^b$ là xác suất trượt mọi dải, và phần bù là xác suất được xét. Với $b=20$, $r=5$, $s=0{,}8$, công thức cho lại $0{,}999643942$ của Ví dụ 06.4. So với Mệnh đề 06.5, định lý này không nói gì về tính đúng mà nói về độ phủ: hai kết quả cùng nhau cho biết đầu ra là các cặp đạt ngưỡng đã được xét, và mỗi cặp đạt ngưỡng được xét với xác suất (2.1).

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ phép chọn đều hoán vị: nếu thứ tự cố định đặt phần tử $a$ lên đầu, thì với $S_1=\{a,d\}$, $S_4=\{a,c,d\}$ cả hai MinHash đều bằng $a$ ở mọi hàng. Cặp thành ứng viên với xác suất $1$, trong khi $s=2/3$ và $P_{b,r}(2/3)<1$.
- Bỏ độc lập trong một dải: nếu $r$ hàng của một dải dùng cùng một hoán vị, dải trùng đúng khi một MinHash trùng, với xác suất $s$ chứ không phải $s^r$; với $s=0{,}8$, $r=5$, đó là $0{,}8$ thay cho $0{,}32768$.
- Bỏ độc lập giữa các dải: nếu cả $b$ dải dùng lại cùng $r$ hoán vị, mọi dải cho cùng một kết quả và cặp thành ứng viên với xác suất $s^r$; với $s=0{,}8$, $r=5$, $b=20$, đó là $0{,}32768$ thay cho $0{,}999643942$.
- Bỏ phép so khóa đầy đủ: va chạm ô của bảng băm lưu trữ chỉ thêm cặp vào tập $\mathrm{CAND}$ mà thuật toán trả, $\mathrm{CAND}\supseteq\mathcal C$, nên chỉ còn $\Pr[(c,d)\in\mathrm{CAND}]\ge P_{b,r}(s)$. Cặp $(1,2)$ của Ví dụ 06.3 có $s=0$, nên $P_{b,r}(0)=0$, nhưng thành ứng viên nếu hai khóa $(1,(1))$ và $(1,(3))$ chung ô.
- Bỏ điều kiện tập không rỗng: theo quy ước đầu ra của thuật toán quét (ghi chú Bài 05, Mục 9 và 11), hai tập rỗng có cột chữ ký toàn $+\infty$, trùng mọi dải nên thành ứng viên với xác suất $1$, trong khi $s$ không xác định.

Bước 1 dùng phép chọn đều và tập không rỗng; Bước 2 dùng độc lập trong dải và phép so khóa đầy đủ; Bước 3 dùng độc lập giữa các dải.

::: corollary Hệ quả 06.8 (Xác suất bỏ sót)
**Giả thiết.** Như Định lý 06.7, và cặp có $s\ge t$.

**Kết luận.** Cặp bị bỏ sót, tức không thuộc đầu ra của Thuật toán 06.4, với xác suất $(1-s^r)^b$.

**Điều kiện áp dụng.** Xác suất theo cách chọn các hoán vị.

**Phạm vi.** Bước xác minh không giảm xác suất này: nó loại ứng viên giả nhưng không xét cặp ngoài $\mathcal C$.
:::

::: proof Chứng minh Hệ quả 06.8
Theo Mệnh đề 06.5, cặp có $s\ge t$ thuộc đầu ra khi và chỉ khi nó thuộc $\mathcal C$. Theo Định lý 06.7, biến cố $(c,d)\notin\mathcal C$ có xác suất $1-P_{b,r}(s)=(1-s^r)^b$. $\square$
:::

**Trong thực hành.** Khi lập chữ ký, mỗi hoán vị được thay bằng một hàm băm trên mã hàng, chẳng hạn $f(x)=(\alpha x+\beta)\bmod R$ (ghi chú Bài 05, Mục 9 và 11). Họ hàm này không chọn đều trên mọi hoán vị, nên Bước 1 của chứng minh, $\Pr(E_i)=s$, chỉ còn là xấp xỉ, và (2.1) là dự đoán của mô hình chứ không phải đẳng thức về dữ liệu.

Chữ ký được lập một lần rồi dùng lại cho mọi lần chạy Thuật toán 06.4, nên với một chữ ký đã lập, tập bỏ sót là cố định. Khi cần một con số cho cả kho, tuyến tính kỳ vọng cho số cặp bỏ sót kỳ vọng bằng tổng $(1-s_{cd}^r)^b$ trên các cặp có $s_{cd}\ge t$, với $s_{cd}=\mathrm{SIM}(S_c,S_d)$; con số này cần biết phân bố của $s_{cd}$, điều Định lý 06.7 không cung cấp.

### 2.4 Ngưỡng và chọn tham số

Với độ dài chữ ký $n$ cho trước, chúng ta còn phải chọn cách tách $n=br$. Tăng $r$ làm mỗi dải khắt khe hơn; tăng $b$ cho thêm lượt thử. Để chọn được, chúng ta cần biết hình dạng của hàm $s\mapsto P_{b,r}(s)$ và vị trí vùng chuyển tiếp của nó so với ngưỡng $t$.

Một cách trực quan, khi $b\ge2$ và $r\ge2$, đồ thị của $P_{b,r}$ là một đường cong S (S-curve): gần $0$ với $s$ nhỏ, gần $1$ với $s$ lớn, và tăng nhanh trong một vùng hẹp. Cặp có $s$ dưới vùng này hiếm khi thành ứng viên, cặp có $s$ trên vùng này hiếm khi bị bỏ sót. Mô tả này chưa phải định nghĩa; ví dụ sau so hai cách tách cùng $n=100$.

::: example Ví dụ 06.5 (Hai cấu hình cùng 100 hàng)
**Dữ kiện.** Chữ ký dài $n=100$; hai cấu hình $(b,r)=(20,5)$ của Ví dụ 3.12 (MMDS, tr.94–95) và $(b,r)=(10,10)$; hai cặp có Jaccard $0{,}3$ và $0{,}8$.

**Tính.** Thế vào (2.1), ta được bảng sau.

| Cấu hình $(b,r)$ | $P_{b,r}(0{,}3)$ | $P_{b,r}(0{,}8)$ |
|---|---:|---:|
| $(20,5)$ | 0,047494259 | 0,999643942 |
| $(10,10)$ | 0,000059047 | 0,678859974 |

**Diễn giải.** Cấu hình $(10,10)$ gần như loại hẳn cặp có Jaccard $0{,}3$, nhưng bỏ sót cặp có Jaccard $0{,}8$ với xác suất $1-0{,}678859974=0{,}321140026$, khoảng $32\%$. Cấu hình $(20,5)$ nhận cặp $0{,}3$ với xác suất khoảng $4{,}7\%$ nhưng gần như không bỏ sót cặp $0{,}8$.

**Kiểm tra lại.** Với $(10,10)$: $0{,}8^{10}\approx0{,}107374$ và $1-(1-0{,}107374)^{10}\approx0{,}678860$, khớp với bảng.
:::

![Đồ thị hai đường xác suất thành ứng viên P(s) = 1 − (1 − s^r)^b theo Jaccard thật s trên đoạn từ 0 đến 1, cho hai cấu hình b × r bằng 20 × 5 và 10 × 10, cùng độ dài chữ ký n = 100; đường 10 × 10 nằm bên phải và dốc hơn đường 20 × 5.](img/lec-06/xac-suat-phan-dai.svg)

Trên hình, trục hoành là Jaccard thật $s$, trục tung là $P_{b,r}(s)$. Đường $20\times5$ đi lên sớm hơn, nên nhận nhiều cặp vừa phải hơn và bỏ sót ít cặp gần hơn; đường $10\times10$ dời vùng chuyển tiếp sang phải. Hai giá trị ở cột $s=0{,}8$ của bảng là hai điểm trên hai đường tại hoành độ $0{,}8$. Nhãn trục trên hình dùng dấu chấm thập phân.

Vị trí vùng chuyển tiếp được đo bằng điểm mà xác suất thành ứng viên bằng một nửa.

::: proposition Mệnh đề 06.9 (Nghiệm một nửa)
**Giả thiết.** $b$, $r$ là số nguyên dương; $P_{b,r}$ cho bởi (2.1) trên $[0,1]$.

**Kết luận.** Phương trình $P_{b,r}(s)=1/2$ có nghiệm duy nhất trên $[0,1]$:

$$
s_{1/2}=\bigl(1-2^{-1/b}\bigr)^{1/r}. \tag{2.2}
$$

**Điều kiện áp dụng.** Mọi $b,r\ge1$.

**Phạm vi.** Mệnh đề là phép biến đổi đại số; nó không đồng nhất $s_{1/2}$ với ngưỡng $t$ do người dùng đặt.
:::

::: proof Chứng minh Mệnh đề 06.9
Hàm $s\mapsto s^r$ tăng chặt trên $[0,1]$, nên $s\mapsto1-(1-s^r)^b$ cũng tăng chặt, đi từ $0$ tại $s=0$ đến $1$ tại $s=1$; vì liên tục, phương trình có đúng một nghiệm. Biến đổi tương đương:

$$
\begin{aligned}
1-(1-s^r)^b=\tfrac12
&\iff (1-s^r)^b=\tfrac12 &&\text{(chuyển vế)}\\
&\iff 1-s^r=2^{-1/b} &&\text{(lấy căn bậc } b\text{, hai vế dương)}\\
&\iff s=\bigl(1-2^{-1/b}\bigr)^{1/r} &&\text{(lấy căn bậc } r\text{, } s\ge0\text{).}
\end{aligned}
$$

$\square$
:::

Với $b=20$, $r=5$, công thức (2.2) cho $s_{1/2}\approx0{,}508695962$. MMDS dùng xấp xỉ $(1/b)^{1/r}$ cho vị trí vùng chuyển tiếp, ở đây bằng $0{,}549280272$; tại điểm này $P_{20,5}\approx0{,}641514078$, nên xấp xỉ không phải nghiệm một nửa.

::: remark Nhận xét 06.10 (Ba đại lượng ngưỡng và quy tắc chọn $b$, $r$)
Ba số $t$, $s_{1/2}$ và $(1/b)^{1/r}$ có ba vai trò. Ngưỡng $t$ là tiêu chuẩn chấp nhận trên dữ liệu gốc, do bài toán quy định. Nghiệm $s_{1/2}$ là tính chất của cấu hình $(b,r)$. Giá trị $(1/b)^{1/r}$ là xấp xỉ dễ tính của vùng chuyển tiếp. Với $(b,r)=(20,5)$ và $t=0{,}8$, ba số là $0{,}8$, khoảng $0{,}509$ và khoảng $0{,}549$.

Quy trình §3.4.3 của MMDS (tr.95) chọn $b$, $r$ sao cho $(1/b)^{1/r}\approx t$. Nếu ưu tiên tránh bỏ sót, đặt giá trị này thấp hơn $t$; nếu ưu tiên ít ứng viên giả để chạy nhanh, đặt cao hơn $t$.

Dạng chữ S cần cả $b\ge2$ và $r\ge2$. Với $r=1$, $P_{b,1}(s)=1-(1-s)^b$ lõm; với $b=1$, $P_{1,r}(s)=s^r$ lồi; cả hai không có điểm uốn, nên tên gọi chung là "đường xác suất thành ứng viên". Diện tích dưới hay trên đường cũng không phải tỷ lệ lỗi của kho khi chưa biết phân bố độ tương đồng của các cặp.
:::

**Trong thực hành.** Độ dài $n$ thường bị chặn bởi bộ nhớ của ma trận chữ ký, như $10^9$ byte của Ví dụ 06.1 với $n=250$. Trong ngân sách ấy, chọn $(b,r)$ là chọn vị trí vùng chuyển tiếp so với $t$: Ví dụ 06.5 cho thấy cùng $n=100$, một cấu hình ưu tiên độ phủ còn cấu hình kia ưu tiên ít ứng viên. Số ứng viên giả không được đọc trực tiếp từ đường cong; nó được đếm qua $K$ ở Mục 2.5.

::: exercise Bài tập 06.3
Dữ kiện: chữ ký dài $n=100$; hai cấu hình $(b,r)=(20,5)$ và $(10,10)$ với $P_{20,5}(0{,}3)=0{,}047494259$, $P_{20,5}(0{,}8)=0{,}999643942$, $P_{10,10}(0{,}3)=0{,}000059047$, $P_{10,10}(0{,}8)=0{,}678859974$ (Ví dụ 06.5); vết chạy của Ví dụ 06.3 trên bốn tập $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$, $S_4=\{a,c,d\}$ với hai hàng chữ ký cố định $(1,3,0,1)$ và $(0,2,0,0)$, $b=2$, $r=1$.

(a) Xác định cấu hình phù hợp khi ưu tiên giảm bỏ sót ở $s=0{,}8$, và cấu hình phù hợp khi ưu tiên giảm số cặp được chọn ở $s=0{,}3$.

(b) Viết $P_{2,1}(s)$ và $P_{1,2}(s)$; tính hai hàm tại $s=1/4$ và $s=2/3$.

(c) Giải thích vì sao vết chạy của Ví dụ 06.3, với hai hàm MinHash cố định, không chứng minh được các công thức ở câu (b).
:::

::: hint
Câu (b) thế $b$, $r$ vào (2.1). Câu (c) xét nguồn ngẫu nhiên trong giả thiết của Định lý 06.7.
:::

::: solution
(a) Ưu tiên giảm bỏ sót tại $0{,}8$ chọn $(20,5)$, vì xác suất bỏ sót là khoảng $0{,}000356058$, so với $0{,}321140026$ của $(10,10)$. Ưu tiên giảm ứng viên tại $0{,}3$ chọn $(10,10)$. Kết luận chỉ so đúng hai độ tương đồng và hai mục tiêu đã nêu.

(b) $P_{2,1}(s)=1-(1-s)^2$ và $P_{1,2}(s)=s^2$. Tại $s=1/4$: $7/16$ và $1/16$. Tại $s=2/3$: $8/9$ và $4/9$. Cấu hình một dải hai hàng nhận ít cặp xa hơn nhưng cũng bỏ sót cặp gần nhiều hơn.

(c) Công thức là xác suất theo cách chọn ngẫu nhiên các hoán vị. Một bộ hàm cố định chỉ cho một kết quả xác định trên dữ liệu đã cho, như Mệnh đề 06.5 mô tả.

**Kiểm tra lại.** $1-(3/4)^2=7/16$ và $1-(1/3)^2=8/9$.
:::

<!-- note-topic-id: lec-06-topic-04 -->
### 2.5 Chi phí tạo và kiểm cặp

Định lý 06.7 cho biết cặp nào có khả năng được xét, nhưng chưa cho biết thuật toán làm bao nhiêu việc. Với kho một triệu tài liệu, câu hỏi cần trả lời là: số cặp được phát và được xác minh có nhỏ hơn $499\,999\,500\,000$ hay không, và trong điều kiện nào. Chúng ta đếm công việc của Thuật toán 06.4 theo từng bước, bắt đầu từ vết chạy đã có.

::: example Ví dụ 06.6 (Công việc trên bốn tập đặc trưng)
**Dữ kiện.** Vết chạy của Ví dụ 06.3: $C=4$, $b=2$, $r=1$; dải 1 có các thùng cỡ $2$, $1$, $1$; dải 2 có các thùng cỡ $3$, $1$; tập ứng viên $\{(1,3),(1,4),(3,4)\}$.

**Đếm.** Bước 2 có $bC=8$ lượt chèn. Một thùng cỡ $u$ phát $\binom u2$ cặp, nên bước 3 có $\binom22+\binom32=1+3=4$ lượt phát. Sau khử lặp còn $3$ cặp, nên bước 4 tính $3$ giá trị Jaccard.

**Kiểm tra lại.** Bốn lượt phát gồm $(1,4)$ ở dải 1 và $(1,3)$, $(1,4)$, $(3,4)$ ở dải 2; cặp $(1,4)$ lặp một lần, nên $4-1=3$.
:::

Mô hình chi phí như sau. Ma trận $\mathrm{SIG}$ và các tập gốc đã có sẵn; chi phí lập chữ ký thuộc Bài 05. Mỗi mã tài liệu và mỗi thành phần chữ ký chiếm một từ máy. Đọc, sao chép hoặc so một tuple dài $r$ tốn $O(r)$; sau khi đọc khóa, tra và chèn bảng băm tốn thời gian kỳ vọng $O(1)$, kỳ vọng lấy theo hàm băm của bảng. Thời gian tính Jaccard gốc không được giả định là hằng.

Ví dụ 06.6 dùng hai số đếm khác nhau. Gọi $u_{j,z}$ là số mã tài liệu trong thùng có tuple $z$ ở dải $j$. Số lượt phát cặp và số cặp phân biệt là

$$
Q=\sum_{j=1}^b\sum_{z}\binom{u_{j,z}}2,\qquad K=\lvert\mathcal C\rvert\le Q. \tag{2.3}
$$

Tổng thứ nhất chạy trên mọi thùng khác rỗng của mọi dải; $Q$ đếm cả các lần một cặp được phát lại ở dải khác, còn $K$ đếm mỗi cặp một lần. Gọi $T_J(c,d)$ là thời gian tính $\mathrm{SIM}(S_c,S_d)$.

::: proposition Mệnh đề 06.11 (Chi phí của Thuật toán 06.4)
**Giả thiết.** Mô hình chi phí vừa nêu.

**Kết luận.** Thời gian chạy kỳ vọng là

$$
O\Bigl(nC+Q+\sum_{(c,d)\in\mathcal C}T_J(c,d)\Bigr),
$$

và bộ nhớ phụ là $O(nC+K)$ từ, ngoài $\mathrm{SIG}$ và các tập gốc. Nếu mỗi tập được lưu thành mảng đã sắp xếp, $T_J(c,d)=O(\lvert S_c\rvert+\lvert S_d\rvert)$.

**Điều kiện áp dụng.** $\mathrm{SIG}$ đã có; bảng băm so khóa đầy đủ.

**Phạm vi.** Kỳ vọng lấy theo hàm băm của bảng, không theo dữ liệu. $Q$ và $K$ phụ thuộc dữ liệu và chữ ký; mệnh đề không cho cận nào nhỏ hơn bậc hai cho chúng.
:::

::: proof Chứng minh Mệnh đề 06.11
**Bước 1 (thời gian theo bước).** Mỗi hàng của bảng sau ứng với một bước của Thuật toán 06.4.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2: sao chép tuple, lập khóa, tra và chèn | $bC$ | $O(r)$ kỳ vọng | $O(brC)=O(nC)$ |
| 2: tạo danh sách rỗng cho khóa mới | tối đa $bC$ | $O(1)$ | $O(bC)$ |
| 3: duyệt danh sách | tối đa $bC$ danh sách | $O(1)$ ngoài phần phát cặp | $O(bC)$ |
| 3: phát một cặp vào tập | $Q$ | $O(1)$ kỳ vọng | $O(Q)$ |
| 4: xác minh một cặp | $K$ | $T_J(c,d)$ | $\sum_{(c,d)\in\mathcal C}T_J(c,d)$ |

Hai hàng $O(bC)$ nằm trong $O(nC)$ vì $b\le br=n$. Số lần ở hàng thứ tư bằng $Q$ vì một thùng cỡ $u_{j,z}$ có đúng $\binom{u_{j,z}}2$ cặp $c<d$; cộng theo mọi thùng cho (2.3). Cộng cột đóng góp cho cận thời gian của mệnh đề.

**Bước 2 (bộ nhớ).** Có tối đa $bC$ khóa phân biệt, mỗi khóa lưu một tuple dài $r$, tổng tối đa $brC=nC$ từ. Các danh sách chứa tổng cộng $bC$ mã. Tập $\mathrm{CAND}$ chứa $K$ cặp và $\mathrm{OUT}$ chứa không quá $K$ cặp. Cộng lại được $O(nC+K)$.

**Bước 3 (xác minh trên mảng đã sắp xếp).** Phép trộn hai mảng tăng dần duyệt mỗi phần tử một lần, đếm được $\lvert S_c\cap S_d\rvert$ và $\lvert S_c\cup S_d\rvert$, nên tốn $O(\lvert S_c\rvert+\lvert S_d\rvert)$. $\square$
:::

Mệnh đề 06.11 tách chi phí thành ba phần có nguồn gốc khác nhau: $nC$ là chi phí đọc chữ ký, tuyến tính theo kích thước đầu vào; $Q$ là chi phí gom cặp, phụ thuộc cỡ thùng; tổng $T_J$ là chi phí xác minh, phụ thuộc $K$ và kích thước các tập. Với Ví dụ 06.6, ba phần là $8$ lượt chèn, $4$ lượt phát và $3$ phép tính Jaccard.

Một nhầm lẫn thường gặp là thay $Q$ bằng $K$ trong chi phí phát cặp; lượt phát lặp vẫn tốn một thao tác dù không thêm phần tử mới.

::: remark Nhận xét 06.12 (Trường hợp xấu nhất)
Nếu mọi cột có cùng tuple ở mọi dải, chẳng hạn khi mọi tài liệu giống hệt nhau, thì mỗi dải có một thùng cỡ $C$ và

$$
Q=b\binom C2,\qquad K=\binom C2.
$$

Với kho một triệu tài liệu, $K=499\,999\,500\,000$, đúng số cặp của Ví dụ 06.1. Vì vậy phân dải không cho thời gian dưới bậc hai một cách vô điều kiện; lợi ích của nó phụ thuộc phân bố độ tương đồng của dữ liệu.
:::

Khi dữ liệu không rơi vào trường hợp xấu nhất, kỳ vọng của $Q$ và $K$ theo cách chọn hoán vị cho biết lượng công việc điển hình.

::: proposition Mệnh đề 06.13 (Kỳ vọng của $K$ và $Q$)
**Giả thiết.** Các giả thiết của Định lý 06.7 cho mọi cặp; $s_{cd}=\mathrm{SIM}(S_c,S_d)$.

**Kết luận.**

$$
\mathbb E[K]=\sum_{c<d}P_{b,r}(s_{cd}),\qquad \mathbb E[Q]=b\sum_{c<d}s_{cd}^r.
$$

**Điều kiện áp dụng.** Không cần các cặp khác nhau độc lập.

**Phạm vi.** Đây là kỳ vọng, không phải cận với xác suất cao và không phải chi phí xấu nhất.
:::

::: proof Chứng minh Mệnh đề 06.13
**Bước 1 (viết thành tổng chỉ báo).** $K=\sum_{c<d}\mathbf 1[(c,d)\in\mathcal C]$. Mỗi lượt phát ở dải $j$ ứng với đúng một cặp chung khóa ở dải đó, nên $Q=\sum_{j=1}^b\sum_{c<d}\mathbf 1[k_{j,c}=k_{j,d}]$.

**Bước 2 (lấy kỳ vọng).** Kỳ vọng của một chỉ báo bằng xác suất của biến cố. Theo Định lý 06.7, $\Pr[(c,d)\in\mathcal C]=P_{b,r}(s_{cd})$; theo Bước 2 của chứng minh định lý, $\Pr[k_{j,c}=k_{j,d}]=s_{cd}^r$. Tuyến tính kỳ vọng, không cần độc lập giữa các số hạng, cho hai đẳng thức. $\square$
:::

**Trong thực hành.** Mệnh đề 06.13 cho thấy mỗi cặp có $s_{cd}$ gần $1$ đóng góp gần $b$ vào $\mathbb E[Q]$ và gần $1$ vào $\mathbb E[K]$. Kho web chứa nhiều bản sao của cùng một trang tạo những thùng lớn ở mọi dải, và $Q$ tăng theo bình phương cỡ nhóm bản sao; đây là trường hợp gần với Nhận xét 06.12 trên một phần của kho.

Ngược lại, nếu hầu hết các cặp có $s_{cd}$ nhỏ, các số hạng $s_{cd}^r$ nhỏ và công việc tập trung ở số ít cặp gần. Cùng một cấu hình $(b,r)$ vì vậy có thể nhanh trên kho này và chậm trên kho khác.

Áp dụng cho kho một triệu tài liệu của Ví dụ 06.1 với $(b,r)=(20,5)$, ta giả định thêm, như một giả định minh họa về phân bố tương đồng chứ không phải số đo, rằng ngoài $N$ cặp gần, mọi cặp có $s_{cd}\le0{,}1$. Vì $P_{20,5}$ tăng theo $s$ và $P_{20,5}(0{,}1)=1-(1-10^{-5})^{20}\approx1{,}9998\cdot10^{-4}$, mỗi cặp nền đóng góp không quá $2\cdot10^{-4}$ vào $\mathbb E[K]$, còn mỗi cặp gần không quá $1$. Có không quá $499\,999\,500\,000$ cặp nền, nên Mệnh đề 06.13 cho $\mathbb E[K]\le N+10^8$; tương tự, mỗi cặp nền đóng góp $20\,s_{cd}^5\le2\cdot10^{-4}$ vào $\mathbb E[Q]$, nên $\mathbb E[Q]\le20N+10^8$. Hai chặn này không cần các cặp độc lập.

Với giả định $1\,\mu\mathrm{s}$ mỗi lần so cặp của Ví dụ 06.1 và $N\ll10^8$, thời gian xác minh kỳ vọng không quá khoảng $100$ giây, so với khoảng $5{,}79$ ngày khi xét mọi cặp. Không có giả định về phân bố tương đồng thì chặn này không còn, và trường hợp xấu nhất vẫn là $K=\binom C2$ (Nhận xét 06.12).

::: exercise Bài tập 06.4
Dữ kiện: vết chạy của Ví dụ 06.3 với $b=2$, $r=1$ có bốn lượt phát $(1,4)$, $(1,3)$, $(1,4)$, $(3,4)$ và tập ứng viên $\{(1,3),(1,4),(3,4)\}$.

Giải thích vì sao thay $Q$ bằng $K$ trong chi phí của bước phát cặp là sai, dùng các số $Q=4$, $K=3$.
:::

::: hint
Xét thao tác mà bước 3 của Thuật toán 06.4 thực hiện với lượt phát thứ hai của $(1,4)$.
:::

::: solution
Cặp $(1,4)$ được phát hai lần. Cả hai lượt đều phải xử lý và chèn vào tập, dù lượt thứ hai không thêm phần tử mới. Vì vậy bước 3 thực hiện $Q=4$ thao tác, còn bước 4 chỉ xác minh $K=3$ cặp. $Q$ đo công việc trước khử lặp, $K$ đo công việc sau khử lặp.

**Kiểm tra lại.** $Q-K=1$ bằng số lần phát lặp của $(1,4)$.
:::

Như vậy, chúng ta đã dựng bộ tạo ứng viên đầu tiên: phân dải chữ ký (Định nghĩa 06.3), thực hiện bằng Thuật toán 06.4, đúng trên tập ứng viên (Mệnh đề 06.5), xét một cặp có Jaccard $s$ với xác suất $P_{b,r}(s)$ (Định lý 06.7), có vùng chuyển tiếp điều chỉnh được qua $(b,r)$ (Mệnh đề 06.9), và tốn công việc $O(nC+Q+\sum T_J)$ (Mệnh đề 06.11).

Tuy nhiên, mọi kết quả trên dựa vào một tính chất riêng của MinHash: một hàng trùng với xác suất bằng Jaccard. Tính chất đó chỉ nói về tập; nó không cho cách tìm cặp vector gần theo góc hay theo khoảng cách Euclid, hoặc cặp chuỗi gần theo số thao tác sửa. Trong Mục 3, chúng ta định nghĩa các độ đo khoảng cách cho những kiểu dữ liệu này, rồi tách từ MinHash ra tính chất chung mà một họ hàm băm cần có để phân dải còn dùng được.

## 3. Khoảng cách và họ nhạy cảm

Với bốn tập đặc trưng, Định lý 06.7 dựa vào việc cặp $(1,4)$ trùng một hàng MinHash với xác suất $\mathrm{SIM}(S_1,S_4)=2/3$. Nếu mỗi tài liệu của kho một triệu tài liệu được biểu diễn bằng một vector đặc trưng số thay cho một tập shingle, không có tập nào để lấy MinHash, và câu hỏi "hai tài liệu có gần nhau không" cần một độ đo khác cùng một họ hàm băm hợp với độ đo ấy.

<!-- note-topic-id: lec-06-topic-05 -->
### 3.1 Độ đo khoảng cách và chuẩn vector

Một cách trực quan, khoảng cách là một con số đo hai đối tượng khác nhau bao nhiêu, bằng $0$ khi chúng trùng nhau và không cho phép đi đường vòng ngắn hơn đường thẳng. Mô tả này chưa phải định nghĩa. Ví dụ sau cho thấy cùng hai điểm có thể nhận nhiều giá trị khoảng cách, tùy cách đo.

::: example Ví dụ 06.7 (Ba độ đo trên hai điểm)
**Dữ kiện.** Theo Ví dụ 3.13 của MMDS (tr.98), $x=(2,7)$ và $y=(6,4)$ trong $\mathbb R^2$.

**Tính.** Độ lệch theo hai tọa độ là $\lvert2-6\rvert=4$ và $\lvert7-4\rvert=3$. Cộng hai độ lệch cho $7$; lấy căn tổng bình phương cho $\sqrt{16+9}=5$; lấy độ lệch lớn nhất cho $4$.

**Kiểm tra lại.** Tam giác vuông có hai cạnh góc vuông $3$ và $4$ có cạnh huyền $5$.
:::

![Hai điểm x = (2,7) và y = (6,4) trên hệ trục cùng tỷ lệ; đoạn ngang ghi độ lệch tọa độ thứ nhất Δ₁ = 4, đoạn dọc ghi độ lệch tọa độ thứ hai Δ₂ = 3, đoạn nối hai điểm ghi L₂ = 5.](img/lec-06/chuan-vector.svg)

Trên hình, hai đoạn vuông góc là hai độ lệch tọa độ, và đoạn chéo là khoảng cách Euclid. Ba con số $7$, $5$, $4$ của Ví dụ 06.7 lần lượt cộng hai đoạn vuông góc, đo đoạn chéo và lấy đoạn dài hơn.

::: definition Định nghĩa 06.14 (Độ đo khoảng cách; chuẩn $L_q$)
Một **độ đo khoảng cách** (metric) trên miền $X$ là hàm $d:X\times X\to\mathbb R_{\ge0}$ thỏa, với mọi $x,y,w\in X$:

1. $d(x,y)=0$ khi và chỉ khi $x=y$;
2. $d(x,y)=d(y,x)$;
3. $d(x,w)\le d(x,y)+d(y,w)$ (bất đẳng thức tam giác).

Trên $\mathbb R^D$, với $q\ge1$, **khoảng cách $L_q$** và **khoảng cách $L_\infty$** là

$$
\|x-y\|_q=\Bigl(\sum_{i=1}^D\lvert x_i-y_i\rvert^q\Bigr)^{1/q},\qquad \|x-y\|_\infty=\max_{1\le i\le D}\lvert x_i-y_i\rvert.
$$
:::

Ba tiên đề nói rằng khoảng cách phân biệt được hai đối tượng khác nhau, không phụ thuộc thứ tự, và đường trực tiếp không dài hơn đường qua một điểm trung gian. Ba số của Ví dụ 06.7 là $L_1$, $L_2$ và $L_\infty$.

MMDS §3.5.2 (tr.97–98) định nghĩa chuẩn $L_r$ cho mọi hằng $r$; điều kiện $q\ge1$ là điều kiện bảo đảm bất đẳng thức tam giác, tức bất đẳng thức Minkowski, mà ta dùng ở đây không chứng minh lại. Điều kiện này không bỏ được: với $q=1/2$ và ba điểm $(0,0)$, $(1,0)$, $(1,1)$, công thức cho $d((0,0),(1,1))=(1+1)^2=4$, lớn hơn tổng $1+1$ của hai đoạn qua $(1,0)$.

### 3.2 Khoảng cách Jaccard

Với tập, độ tương đồng Jaccard đã có; khoảng cách tương ứng là phần bù của nó. Ví dụ, $\mathrm{SIM}(S_1,S_4)=2/3$ cho khoảng cách $1/3$.

::: proposition Mệnh đề 06.15 (Khoảng cách Jaccard)
**Giả thiết.** $A$, $B$, $W$ là các tập hữu hạn, không rỗng; $h$ là MinHash lý tưởng với hoán vị chọn đều trên hợp của các tập đang xét.

**Kết luận.** Hàm $d_J(A,B)=1-\mathrm{SIM}(A,B)$ là một độ đo khoảng cách, nhận giá trị trong $[0,1]$, và $d_J(A,B)=\Pr[h(A)\ne h(B)]$.

**Điều kiện áp dụng.** Mọi họ tập hữu hạn, không rỗng trên một vũ trụ hữu hạn.

**Phạm vi.** Hai tập rỗng nằm ngoài miền vì $\mathrm{SIM}$ không xác định.
:::

::: proof Chứng minh Mệnh đề 06.15
**Bước 1 (liên hệ xác suất).** Theo định lý MinHash, $\Pr[h(A)=h(B)]=\mathrm{SIM}(A,B)$; lấy biến cố bù được $\Pr[h(A)\ne h(B)]=d_J(A,B)$.

**Bước 2 (miền giá trị, tiên đề 1 và 2).** $0\le d_J\le1$ vì $0\le\mathrm{SIM}\le1$. $d_J(A,B)=0$ khi và chỉ khi $\lvert A\cap B\rvert=\lvert A\cup B\rvert$, tức $A=B$. Đối xứng theo từ đối xứng của giao và hợp.

**Bước 3 (tam giác).** Dùng cùng một $h$ cho ba tập. Nếu $h(A)\ne h(W)$ thì không thể đồng thời có $h(A)=h(B)$ và $h(B)=h(W)$, nên

$$
\{h(A)\ne h(W)\}\subseteq\{h(A)\ne h(B)\}\cup\{h(B)\ne h(W)\}.
$$

Lấy xác suất, dùng chặn hợp và Bước 1, ta được $d_J(A,W)\le d_J(A,B)+d_J(B,W)$. Chặn hợp không cần độc lập giữa hai biến cố ở vế phải. $\square$
:::

Mệnh đề 06.15 là cầu nối giữa Mục 2 và phần còn lại của Mục 3: khoảng cách Jaccard bằng xác suất hai giá trị MinHash khác nhau. Mục 3.6 lấy quan hệ "xác suất trùng giảm khi khoảng cách tăng" làm định nghĩa cho mọi độ đo.

### 3.3 Khoảng cách góc

Với vector, nhiều ứng dụng chỉ quan tâm hướng chứ không quan tâm độ dài, chẳng hạn khi nhân đôi mọi tần suất của một tài liệu không làm đổi nội dung của nó.

::: example Ví dụ 06.8 (Góc giữa hai vector)
**Dữ kiện.** Theo Ví dụ 3.14 của MMDS (tr.99), $x=(1,2,-1)$ và $y=(2,1,1)$.

**Tính.** $x\cdot y=2+2-1=3$; $\|x\|_2=\|y\|_2=\sqrt6$. Do đó $\cos\theta=3/6=1/2$ và $\theta=\pi/3=60^\circ$.

**Kiểm tra lại.** $\cos(\pi/3)=1/2$. Giá trị $1-\cos\theta=1/2$ khác góc $\pi/3\approx1{,}047$.
:::

::: definition Định nghĩa 06.16 (Khoảng cách góc)
Với hai vector khác $0$ trong $\mathbb R^D$, **khoảng cách góc** là

$$
\theta(x,y)=\arccos\frac{x\cdot y}{\|x\|_2\|y\|_2}\in[0,\pi].
$$

Miền của khoảng cách góc là tập các hướng, tức các lớp vector khác $0$ sai khác một hệ số dương; mỗi hướng có thể đại diện bằng một vector đơn vị.
:::

Biểu thức trong $\arccos$ là độ tương đồng cosin (cosine similarity), nằm trong $[-1,1]$ theo Cauchy–Schwarz, nên góc xác định. Góc chỉ phụ thuộc hướng: $x$ và $2x$ có góc $0$ dù là hai vector khác nhau, nên tiên đề "$d=0$ khi và chỉ khi trùng nhau" chỉ đúng trên các hướng. Vector $0$ không có hướng và nằm ngoài miền.

::: remark Nhận xét 06.17 (Góc và cosin)
Khoảng cách góc khác độ tương đồng cosin $\cos\theta$ và khác $1-\cos\theta$; Ví dụ 06.8 cho $\theta=\pi/3$ trong khi $1-\cos\theta=1/2$. Bất đẳng thức tam giác của góc có một phác thảo hình học: trên mặt cầu đơn vị, góc giữa hai hướng là độ dài cung ngắn nhất nối chúng, và đi qua một hướng trung gian không ngắn hơn cung trực tiếp. MMDS §3.5.4 (tr.99) cũng chỉ lập luận bằng hình học; đây là phác thảo, không phải chứng minh đầy đủ.
:::

### 3.4 Khoảng cách chỉnh sửa

Với chuỗi, hai chuỗi gần nhau khi sửa ít ký tự là biến chuỗi này thành chuỗi kia.

::: example Ví dụ 06.9 (Sửa abcde thành acfdeg)
**Dữ kiện.** Theo Ví dụ 3.15–3.16 của MMDS (tr.100), $x=abcde$ và $y=acfdeg$; chỉ dùng thao tác chèn hoặc xóa một ký tự.

**Tính.** Vết sửa $abcde\to acde\to acfde\to acfdeg$ gồm xóa $b$, chèn $f$, chèn $g$: ba thao tác. Chuỗi $acde$ được giữ nguyên thứ tự trong cả hai chuỗi; nó dài $4$.

**Kiểm tra lại.** $\lvert x\rvert+\lvert y\rvert-2\cdot4=5+6-8=3$, bằng số thao tác của vết sửa.
:::

::: definition Định nghĩa 06.18 (Khoảng cách chỉnh sửa; dãy con chung dài nhất)
Một **dãy con** của chuỗi $x$ là chuỗi thu được bằng cách xóa một số ký tự của $x$ và giữ thứ tự các ký tự còn lại; các ký tự giữ lại không cần liên tiếp. **Dãy con chung dài nhất** (longest common subsequence) của $x$ và $y$ là dãy con chung có độ dài lớn nhất; ký hiệu độ dài đó là $L$.

**Khoảng cách chỉnh sửa** (edit distance) $d(x,y)$ là số thao tác chèn hoặc xóa một ký tự ít nhất để biến $x$ thành $y$. Phép thay một ký tự không là thao tác riêng.
:::

Ví dụ 06.9 có $L=4$ với dãy con $acde$. Đếm số thao tác ít nhất trực tiếp từ định nghĩa đòi hỏi xét mọi vết sửa; mệnh đề sau thay việc đó bằng $L$.

::: proposition Mệnh đề 06.19 (Khoảng cách chỉnh sửa qua dãy con chung)
**Giả thiết.** $x$, $y$ là hai chuỗi hữu hạn; chỉ dùng chèn và xóa.

**Kết luận.** $d(x,y)=\lvert x\rvert+\lvert y\rvert-2L$, và $d$ là một độ đo khoảng cách trên tập chuỗi hữu hạn.

**Điều kiện áp dụng.** Mọi bảng chữ cái.

**Phạm vi.** Mệnh đề không cho thuật toán tính $L$; chi phí tính $L$ không được phân tích ở chương này.
:::

::: proof Chứng minh Mệnh đề 06.19
**Bước 1 (cận trên).** Giữ một dãy con chung dài $L$, xóa $\lvert x\rvert-L$ ký tự còn lại của $x$, rồi chèn $\lvert y\rvert-L$ ký tự để được $y$. Vết sửa này dùng $\lvert x\rvert+\lvert y\rvert-2L$ thao tác.

**Bước 2 (cận dưới).** Trong một vết sửa bất kỳ, các ký tự của $x$ không bị xóa giữ thứ tự và xuất hiện trong $y$, nên tạo một dãy con chung; có nhiều nhất $L$ ký tự như vậy. Vì thế vết sửa xóa ít nhất $\lvert x\rvert-L$ ký tự và chèn ít nhất $\lvert y\rvert-L$ ký tự. Hai cận trùng nhau.

**Bước 3 (tiên đề).** Chi phí $0$ chỉ xảy ra khi không có thao tác nào, tức $x=y$. Đảo một vết sửa, đổi chèn thành xóa và ngược lại, cho đối xứng. Nối vết sửa tối ưu từ $x$ đến $y$ với vết sửa tối ưu từ $y$ đến $w$ cho một vết sửa từ $x$ đến $w$, nên $d(x,w)\le d(x,y)+d(y,w)$. $\square$
:::

### 3.5 Khoảng cách Hamming

Khi hai vector cùng chiều và vị trí của mỗi thành phần có ý nghĩa cố định, ta chỉ cần đếm số vị trí khác nhau.

::: example Ví dụ 06.10 (Hai vector bit)
**Dữ kiện.** Theo Ví dụ 3.17 của MMDS (tr.101), $x=10101$ và $y=11110$, $D=5$.

**Tính.** So từng vị trí: vị trí 1 và 3 trùng, vị trí 2, 4, 5 khác. Khoảng cách là $3$.

**Kiểm tra lại.** Hai vị trí trùng cộng ba vị trí khác bằng $D=5$.
:::

::: definition Định nghĩa 06.20 (Khoảng cách Hamming)
Cho bảng ký hiệu hữu hạn $\Sigma$ và $D\ge1$. Với $x,y\in\Sigma^D$, **khoảng cách Hamming** là

$$
d_H(x,y)=\sum_{i=1}^D\mathbf 1[x_i\ne y_i].
$$
:::

Công thức đếm số tọa độ khác nhau: mỗi số hạng bằng $1$ ở vị trí khác và $0$ ở vị trí trùng. Khác với khoảng cách chỉnh sửa, Hamming so cùng vị trí và không cho phép dời căn chỉnh: $abcde$ và $acde$ không cùng độ dài nên không có khoảng cách Hamming, trong khi khoảng cách chỉnh sửa của chúng là $1$.

::: remark Nhận xét 06.21 (Hamming là độ đo; chi phí tính độ đo)
Tại mỗi tọa độ, nếu $x_i\ne w_i$ thì ít nhất một trong hai điều $x_i\ne y_i$, $y_i\ne w_i$ đúng, nên $\mathbf 1[x_i\ne w_i]\le\mathbf 1[x_i\ne y_i]+\mathbf 1[y_i\ne w_i]$; cộng theo $i$ cho bất đẳng thức tam giác. Tổng bằng $0$ khi và chỉ khi mọi số hạng bằng $0$, tức $x=y$; đối xứng vì $x_i\ne y_i$ khi và chỉ khi $y_i\ne x_i$.

Trên vector đặc, các chuẩn $L_q$, góc và Hamming đều tính được trong một lượt qua $D$ tọa độ, tức $O(D)$ phép toán từ máy. Chi phí đó là của một cặp; nó chưa giải bài toán tìm cặp trên toàn kho.
:::

::: exercise Bài tập 06.5
Dữ kiện: $x=(1,2,-1)$, $y=(2,1,1)$ (Ví dụ 06.8); hai vector bit $10101$, $11110$ (Ví dụ 06.10); hai chuỗi $abc$ và $bca$; hai vector $(1,1,0)$ và $(1,0,0)$.

(a) Phân biệt độ tương đồng cosin với khoảng cách góc trên cặp $x$, $y$.

(b) Giải thích vì sao Hamming của $10101$, $11110$ đếm vị trí khác, còn khoảng cách chỉnh sửa cho phép thay đổi căn chỉnh.

(c) Tính khoảng cách chỉnh sửa giữa $abc$ và $bca$.

(d) Tính góc giữa $(1,1,0)$ và $(1,0,0)$.
:::

::: hint
Câu (c) tìm một dãy con chung dài nhất rồi dùng Mệnh đề 06.19. Câu (d) tính tích vô hướng và hai chuẩn trước khi lấy $\arccos$.
:::

::: solution
(a) Cosin bằng $1/2$, còn góc bằng $\pi/3=60^\circ$.

(b) Hamming so cùng vị trí nên đếm ba vị trí 2, 4, 5. Khoảng cách chỉnh sửa cho phép chèn hoặc xóa, làm các vị trí được ghép với nhau thay đổi; nó là số thao tác ít nhất.

(c) Dãy con chung dài nhất là $bc$, $L=2$, nên khoảng cách là $3+3-2\cdot2=2$: xóa $a$ ở đầu, chèn $a$ ở cuối.

(d) Tích vô hướng bằng $1$, hai chuẩn là $\sqrt2$ và $1$, nên $\cos\theta=1/\sqrt2$ và $\theta=\pi/4=45^\circ$.

**Kiểm tra lại.** Ở (c), $abc$ và $bca$ không có dãy con chung dài $3$ vì hai chuỗi khác nhau.
:::

<!-- note-topic-id: lec-06-topic-06 -->
### 3.6 Họ nhạy cảm theo tính cục bộ

Phân dải dùng được vì MinHash có một tính chất định lượng: cặp càng gần càng dễ trùng. Với bốn tập đặc trưng, cặp $(1,4)$ có $d_J=1/3$ và trùng một MinHash với xác suất $2/3$; cặp $(1,3)$ có $d_J=3/4$ và trùng với xác suất $1/4$. Để dùng cùng ý tưởng cho góc, Hamming hay khoảng cách Euclid, chúng ta cần phát biểu tính chất này mà không đòi xác suất trùng có một công thức đúng như MinHash.

Một cách trực quan, phân dải chỉ cần biết xác suất trùng ở hai phía của vùng quan tâm: cặp đủ gần phải trùng đủ thường để vượt ít nhất một dải, cặp đủ xa phải trùng đủ hiếm; xác suất của cặp ở giữa không ảnh hưởng tới hai loại sai số tại hai ngưỡng. Vì vậy chúng ta chỉ đòi hai bảo đảm và không đòi gì với cặp ở giữa. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.22 (Họ nhạy cảm theo tính cục bộ)
Cho độ đo khoảng cách $d$ trên miền $X$ và một họ hàm $\mathcal H$ trên $X$ kèm một phân phối chọn hàm. Với $0\le d_1<d_2$ và $0\le p_2<p_1\le1$, họ $\mathcal H$ là **$(d_1,d_2,p_1,p_2)$-nhạy cảm** (locality-sensitive family) nếu với mọi cặp cố định $x,y\in X$:

$$
d(x,y)\le d_1\ \Longrightarrow\ \Pr_{h\sim\mathcal H}[h(x)=h(y)]\ge p_1,
$$

$$
d(x,y)\ge d_2\ \Longrightarrow\ \Pr_{h\sim\mathcal H}[h(x)=h(y)]\le p_2.
$$

Trong cả hai bất đẳng thức, cùng một hàm $h$ được áp dụng cho $x$ và $y$, và xác suất lấy theo cách chọn $h$.
:::

Định nghĩa có bốn tham số: $d_1$ là ngưỡng gần, $d_2$ là ngưỡng xa, $p_1$ là cận dưới của xác suất trùng với cặp gần, $p_2$ là cận trên với cặp xa. Nguồn ngẫu nhiên nằm ở việc chọn $h$; với một hàm cố định và một cặp cố định, việc trùng hay không là xác định. Miền $d_1<d(x,y)<d_2$ không có bảo đảm nào. So với MinHash, định nghĩa yếu hơn ở chỗ chỉ đòi hai bất đẳng thức tại hai ngưỡng, nhưng áp dụng được cho mọi độ đo.

![Trục khoảng cách d chia ba miền: miền gần d ≤ d₁ ghi xác suất trùng ít nhất p₁, miền giữa d₁ < d < d₂ ghi không có cận chung, miền xa d ≥ d₂ ghi xác suất trùng nhiều nhất p₂.](img/lec-06/mien-gan-xa.svg)

Hình đặt hai bất đẳng thức của Định nghĩa 06.22 lên trục khoảng cách. Hai mũi tên xác suất chỉ có ở hai miền ngoài; miền giữa để trống vì định nghĩa không ràng buộc gì ở đó.

::: corollary Hệ quả 06.23 (Họ MinHash)
**Giả thiết.** Miền là các tập hữu hạn, không rỗng với khoảng cách $d_J$; họ gồm các MinHash lý tưởng với hoán vị chọn đều; $0\le d_1<d_2\le1$.

**Kết luận.** Họ MinHash là $(d_1,d_2,1-d_1,1-d_2)$-nhạy cảm.

**Điều kiện áp dụng.** Như Mệnh đề 06.15.

**Phạm vi.** Với họ này, xác suất trùng của mỗi cặp bằng đúng $1-d_J$; các họ của Mục 4 nói chung chỉ cho cận.
:::

::: proof Chứng minh Hệ quả 06.23
Theo Mệnh đề 06.15, $\Pr[h(A)=h(B)]=1-d_J(A,B)$. Nếu $d_J(A,B)\le d_1$ thì xác suất ít nhất $1-d_1$; nếu $d_J(A,B)\ge d_2$ thì xác suất nhiều nhất $1-d_2$. Từ $d_1<d_2$ suy ra $1-d_2<1-d_1$, đúng thứ tự $p_2<p_1$ của Định nghĩa 06.22. $\square$
:::

::: example Ví dụ 06.11 (Họ MinHash với hai ngưỡng $0{,}3$ và $0{,}6$)
**Dữ kiện.** Theo Ví dụ 3.18 của MMDS (tr.105), $d_1=0{,}3$, $d_2=0{,}6$.

**Tính.** Theo Hệ quả 06.23, họ MinHash là $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$-nhạy cảm: cặp có khoảng cách Jaccard không quá $0{,}3$, tức Jaccard ít nhất $0{,}7$, trùng với xác suất ít nhất $0{,}7$; cặp có khoảng cách ít nhất $0{,}6$ trùng với xác suất nhiều nhất $0{,}4$.

**Kiểm tra lại.** Cặp $(1,4)$ có $d_J=1/3\approx0{,}333$, rơi vào miền giữa của họ này, nên định nghĩa không cho bảo đảm nào cho nó, dù xác suất thật của nó là $2/3$.
:::

::: exercise Bài tập 06.6
Dữ kiện: họ MinHash $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$-nhạy cảm (Ví dụ 06.11). Chỉ dùng định nghĩa họ nhạy cảm, nêu bảo đảm cho cặp có khoảng cách $0{,}2$, $0{,}5$ và $0{,}8$.
:::

::: hint
Xác định mỗi khoảng cách thuộc miền gần, miền giữa hay miền xa.
:::

::: solution
Tại $0{,}2$, xác suất trùng ít nhất $0{,}7$. Tại $0{,}8$, xác suất trùng nhiều nhất $0{,}4$. Tại $0{,}5$, khoảng cách nằm giữa hai ngưỡng nên định nghĩa không cho cận nào.

**Kiểm tra lại.** Hệ quả 06.23 cho xác suất thật tại $0{,}5$ là $0{,}5$, nằm giữa hai mức $0{,}4$ và $0{,}7$, nhưng định nghĩa họ không dùng thông tin này.
:::

::: remark Nhận xét 06.24 (Bộ tham số là cận, không là xác suất của từng cặp)
Hai nhầm lẫn thường gặp khi đọc Định nghĩa 06.22.

- Đọc $p_1$, $p_2$ như xác suất trùng của mọi cặp gần, mọi cặp xa. Thực ra chúng chỉ là cận: cặp có $d_J=0{,}2$ trong họ MinHash $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$ trùng với xác suất $0{,}8$, lớn hơn $p_1=0{,}7$. Với họ MinHash, Hệ quả 06.23 cho đúng một đẳng thức; các họ khác nói chung chỉ cho bất đẳng thức.
- Bỏ điều kiện cùng hàm cho hai đối tượng. Nếu $S_1=\{a,d\}$ được băm hai lần bằng hai hoán vị chọn độc lập, mỗi lần cho $a$ hoặc $d$ với xác suất $1/2$, nên hai giá trị trùng với xác suất $1/2$ dù khoảng cách bằng $0$. Biến cố trùng khi đó không đo khoảng cách.

Miền giữa $d_1<d<d_2$ cũng không có nghĩa là xác suất ở đó nằm giữa $p_2$ và $p_1$; định nghĩa không nói gì về miền này.
:::

<!-- note-topic-id: lec-06-topic-07 -->
### 3.7 Phép ghép AND và OR

Một hàm băm cơ sở thường chỉ tách hai mức xác suất một khoảng nhỏ. Theo Ví dụ 3.19 của MMDS (tr.106), xét họ $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$-nhạy cảm: cặp gần trùng với xác suất ít nhất $0{,}8$, cặp xa nhiều nhất $0{,}4$. Một phép thử như vậy để lọt nhiều cặp xa.

Nếu đòi bốn hàm độc lập cùng trùng, hai mức thành $0{,}8^4=0{,}4096$ và $0{,}4^4=0{,}0256$; nếu chỉ đòi ít nhất một trong bốn hàm trùng, hai mức thành $1-0{,}2^4=0{,}9984$ và $1-0{,}6^4=0{,}8704$. Cách thứ nhất hạ mạnh mức của cặp xa nhưng cũng hạ mức của cặp gần; cách thứ hai làm ngược lại.

Một cách trực quan, đòi mọi hàm cùng trùng làm phép thử khắt khe hơn, còn chấp nhận một hàm trùng làm phép thử dễ dãi hơn; ghép hai cách theo thứ tự thích hợp có thể đẩy mức của cặp gần lên gần $1$ và mức của cặp xa xuống gần $0$. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.25 (Phép ghép AND và OR)
Cho họ $\mathcal H$ kèm phân phối chọn hàm.

**Phép ghép đồng thời** (AND-construction) bậc $r$ chọn độc lập $r$ hàm $h_1,\ldots,h_r$ từ $\mathcal H$ và đặt $g(x)=(h_1(x),\ldots,h_r(x))$. Cặp $x$, $y$ được nhận khi $g(x)=g(y)$, tức cả $r$ hàm cùng trùng.

**Phép ghép ít nhất một** (OR-construction) bậc $b$ chọn độc lập $b$ hàm $h_1,\ldots,h_b$ từ $\mathcal H$. Cặp $x$, $y$ được nhận khi tồn tại $i$ với $h_i(x)=h_i(y)$.
:::

Phép ghép đồng thời tạo một hàm mới có giá trị là tuple, nên có thể băm trực tiếp. Phép ghép ít nhất một là một quy tắc nhận cặp qua $b$ bảng, không phải một hàm băm duy nhất: quan hệ "trùng ít nhất một bảng" có thể không bắc cầu, vì $x$ trùng $y$ ở bảng 1 và $y$ trùng $w$ ở bảng 2 không kéo theo $x$ trùng $w$ ở bảng nào. Cả hai phép đều có thể áp dụng cho họ đã ghép, theo bất kỳ thứ tự nào.

::: proposition Mệnh đề 06.26 (Xác suất sau phép ghép)
**Giả thiết.** Họ $\mathcal H$ là $(d_1,d_2,p_1,p_2)$-nhạy cảm; các hàm trong một phép ghép được chọn độc lập theo cùng phân phối; cùng các hàm được áp dụng cho mọi đối tượng.

**Kết luận.** Với một cặp có xác suất trùng cơ sở đúng bằng $p$, phép ghép đồng thời bậc $r$ nhận cặp với xác suất $p^r$, phép ghép ít nhất một bậc $b$ nhận cặp với xác suất $1-(1-p)^b$. Do đó họ ghép đồng thời là $(d_1,d_2,p_1^r,p_2^r)$-nhạy cảm và họ ghép ít nhất một là $(d_1,d_2,1-(1-p_1)^b,1-(1-p_2)^b)$-nhạy cảm.

**Điều kiện áp dụng.** Mọi $r,b\ge1$; áp dụng lặp cho nhiều tầng ghép khi mỗi tầng dùng các bản độc lập của tầng trước.

**Phạm vi.** Hai ngưỡng $d_1$, $d_2$ không đổi; chỉ hai mức xác suất được biến đổi.
:::

::: proof Chứng minh Mệnh đề 06.26
**Bước 1 (AND).** Biến cố nhận cặp là giao của $r$ biến cố "$h_i(x)=h_i(y)$", mỗi biến cố có xác suất $p$. Các hàm độc lập nên xác suất của giao là $p^r$.

**Bước 2 (OR).** Biến cố không nhận cặp là giao của $b$ biến cố "$h_i(x)\ne h_i(y)$", mỗi biến cố có xác suất $1-p$; do độc lập, xác suất là $(1-p)^b$. Lấy biến cố bù được $1-(1-p)^b$.

**Bước 3 (biến đổi cận).** Hai hàm $p\mapsto p^r$ và $p\mapsto1-(1-p)^b$ tăng trên $[0,1]$. Nếu cặp gần có xác suất cơ sở ít nhất $p_1$, xác suất sau ghép ít nhất giá trị của hàm tại $p_1$; tương tự, cặp xa cho cận trên tại $p_2$. Tính tăng chặt của hai hàm giữ thứ tự của hai mức sau ghép. $\square$
:::

Mệnh đề 06.26 mở rộng Định lý 06.7 từ MinHash sang mọi họ nhạy cảm. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ độc lập giữa các hàm: nếu phép ghép đồng thời bậc $4$ dùng lại cùng một hàm bốn lần, $g(x)=g(y)$ đúng khi hàm đó trùng, với xác suất $p$; cặp có $p=0{,}8$ được nhận với xác suất $0{,}8$ chứ không phải $0{,}4096$. Tương tự, phép ghép ít nhất một bậc $4$ dùng lại một hàm cho $0{,}8$ thay cho $0{,}9984$.
- Bỏ điều kiện cùng hàm cho mọi đối tượng: nếu $x$ được băm bằng $h_1$ còn $y$ bằng một hàm $h_1'$ chọn riêng, biến cố "$h_1(x)=h_1'(y)$" không còn là biến cố trùng của Định nghĩa 06.22. Với $x=y=S_1=\{a,d\}$ và hai hoán vị độc lập, hai MinHash trùng với xác suất $1/2$ thay cho $1$ (Nhận xét 06.24).

Bước 1 và Bước 2 dùng độc lập; giả thiết cùng hàm cho mọi đối tượng cho phép dùng cận $p_1$, $p_2$ của họ cơ sở ở Bước 3.

::: example Ví dụ 06.12 (Hai thứ tự ghép trên 16 phép thử)
**Dữ kiện.** Theo Ví dụ 3.19–3.20 của MMDS (tr.106–108), họ cơ sở $(0{,}2;\ 0{,}6;\ 0{,}8;\ 0{,}4)$-nhạy cảm; ngân sách 16 hàm cơ sở, chia thành $4\times4$.

**AND 4 rồi OR 4.** Tầng trong cho $0{,}8^4=0{,}4096$ và $0{,}4^4=0{,}0256$. Tầng ngoài cho $F(p)=1-(1-p^4)^4$, tức $F(0{,}8)\approx0{,}878497449$ và $F(0{,}4)\approx0{,}098534519$.

**OR 4 rồi AND 4.** Tầng trong cho $1-0{,}2^4=0{,}9984$ và $1-0{,}6^4=0{,}8704$. Tầng ngoài cho $G(p)=[1-(1-p)^4]^4$, tức $G(0{,}8)\approx0{,}993615344$ và $G(0{,}4)\approx0{,}573951942$.

**Diễn giải.** Cùng 16 hàm, AND rồi OR cho họ $(0{,}2;\ 0{,}6;\ 0{,}878497449;\ 0{,}098534519)$-nhạy cảm: mức cặp xa xuống dưới $0{,}1$. OR rồi AND giữ mức cặp gần trên $0{,}99$ nhưng để cặp xa lọt với xác suất tới $0{,}57$.

**Kiểm tra lại.** $0{,}9984^4\approx0{,}993615$ và $0{,}8704^4\approx0{,}573952$.
:::

![Mười sáu hàm h1 đến h16 chia thành bốn nhóm bốn hàm; mỗi nhóm qua một khối AND 4 tạo một tuple (một dải); bốn tuple đi vào một khối OR 4 thực hiện bằng hợp các tập cặp.](img/lec-06/ghep-and-or.svg)

Hình vẽ cấu trúc AND 4 rồi OR 4 của Ví dụ 06.12: mỗi nhóm bốn hàm là một dải tạo một tuple, và khối OR là phép hợp các tập cặp của bốn bảng.

::: remark Nhận xét 06.27 (Phân dải là AND rồi OR)
Phân dải của Mục 2 là phép ghép đồng thời bậc $r$ trên họ MinHash, rồi phép ghép ít nhất một bậc $b$: mỗi dải là một tuple $g$, và Định nghĩa 06.3 nhận cặp khi trùng ít nhất một dải. Với họ MinHash, xác suất cơ sở đúng bằng $p=s$, nên Mệnh đề 06.26 cho lại $P_{b,r}(s)=1-(1-s^r)^b$ của Định lý 06.7; cấu trúc của Ví dụ 06.12 là $F(s)=P_{4,4}(s)$. Số hàm cơ sở bằng tích các bậc ghép, ở đây $br$. Mệnh đề 06.26 chỉ biến đổi xác suất; thời gian phát cặp vẫn phụ thuộc cỡ thùng qua $Q$, và thời gian xác minh phụ thuộc $K$ (Mệnh đề 06.11).
:::

**Trong thực hành.** Cấu trúc AND $r$ rồi OR $b$ được cài như Thuật toán 06.4: mỗi đối tượng tính $br$ giá trị cơ sở, tạo $b$ tuple, chèn vào $b$ bảng, rồi hợp các tập cặp. Bộ nhớ của các bảng tăng tuyến tính theo $b$.

Cấu trúc OR rồi AND không cài được bằng một tuple duy nhất, vì quan hệ "trùng ít nhất một bảng" không bắc cầu: mỗi nhóm OR phải hợp các cặp của các bảng cơ sở thành một tập cặp, rồi tầng AND lấy giao các tập cặp của các nhóm. §3.6.1 của MMDS định nghĩa hàm của một họ như một quyết định trên từng cặp, nên phép ghép OR rồi AND vẫn có nghĩa dù không có một giá trị băm duy nhất.

::: exercise Bài tập 06.7
Dữ kiện: họ MinHash $(0{,}3;\ 0{,}6;\ 0{,}7;\ 0{,}4)$-nhạy cảm (Ví dụ 06.11). Áp dụng AND 2 rồi OR 2, với các hàm độc lập. Tính hai cận mới và so độ chênh $p_1-p_2$ trước và sau.
:::

::: hint
Tầng AND 2 thay $p$ bằng $p^2$; tầng OR 2 thay $q$ bằng $1-(1-q)^2$.
:::

::: solution
AND 2 cho $0{,}7^2=0{,}49$ và $0{,}4^2=0{,}16$. OR 2 cho $1-0{,}51^2=0{,}7399$ và $1-0{,}84^2=0{,}2944$. Họ mới là $(0{,}3;\ 0{,}6;\ 0{,}7399;\ 0{,}2944)$-nhạy cảm. Độ chênh tăng từ $0{,}3$ lên $0{,}7399-0{,}2944=0{,}4455$.

**Kiểm tra lại.** $0{,}51^2=0{,}2601$ và $0{,}84^2=0{,}7056$.
:::

Như vậy, chúng ta đã có ngôn ngữ chung cho mọi độ đo: độ đo khoảng cách (Định nghĩa 06.14) với năm trường hợp của MMDS, họ $(d_1,d_2,p_1,p_2)$-nhạy cảm (Định nghĩa 06.22) với MinHash là trường hợp riêng (Hệ quả 06.23), và hai phép ghép biến đổi bộ tham số (Mệnh đề 06.26), trong đó phân dải là AND rồi OR (Nhận xét 06.27).

Tuy nhiên, ngoài MinHash cho Jaccard, chúng ta chưa có họ nhạy cảm nào; tính chất độ đo của góc, Hamming hay khoảng cách Euclid không tự sinh ra một họ như vậy. Trong Mục 4, chúng ta dựng ba họ cơ sở cho Hamming, góc và khoảng cách Euclid, chứng minh bộ tham số của từng họ, rồi dùng lại phép ghép và Thuật toán 06.4 mà không đổi gì.

## 4. Các họ băm theo độ đo

Với bốn tập đặc trưng, họ MinHash cho đúng xác suất trùng $1-d_J$, nhưng đó là họ cụ thể duy nhất đã có. Nếu kho một triệu tài liệu được lưu thành vector bit cần tìm cặp gần theo Hamming, hoặc thành vector đặc trưng số cần tìm cặp có góc nhỏ hay gần theo khoảng cách Euclid, chúng ta chưa có hàm băm nào để đưa vào Thuật toán 06.4. Việc còn thiếu là một họ băm có bộ tham số chứng minh được cho từng độ đo.

<!-- note-topic-id: lec-06-topic-08 -->
### 4.1 Họ chọn tọa độ cho khoảng cách Hamming

Một cách trực quan, hai vector bit càng ít vị trí khác nhau thì một vị trí chọn ngẫu nhiên càng dễ là vị trí trùng; đọc một tọa độ là một phép thử rẻ nhất có thể. Mô tả này chưa phải định nghĩa.

::: example Ví dụ 06.13 (Hai vector bit theo từng chỉ số)
**Dữ kiện.** $x=10101$, $y=11110$, $D=5$ (Ví dụ 06.10); hàm $h_i$ trả tọa độ thứ $i$.

**Tính.** $h_1$ trả $1$ và $1$; $h_2$ trả $0$ và $1$; $h_3$ trả $1$ và $1$; $h_4$ trả $0$ và $1$; $h_5$ trả $1$ và $0$. Hai hàm $h_1$, $h_3$ cho cùng giá trị.

**Kết luận.** Nếu chọn chỉ số đều trong năm chỉ số, cặp trùng với xác suất $2/5=1-3/5=1-d_H(x,y)/D$.

**Kiểm tra lại.** Hai chỉ số trùng cộng ba chỉ số khác bằng $5$.
:::

::: definition Định nghĩa 06.28 (Họ chọn tọa độ)
Cho $D\ge1$ và bảng ký hiệu hữu hạn $\Sigma$. Với mỗi $i\in\{1,\ldots,D\}$, hàm $h_i:\Sigma^D\to\Sigma$ là $h_i(x)=x_i$. **Họ chọn tọa độ** gồm $D$ hàm này, với phân phối chọn chỉ số $I$ đều trên $\{1,\ldots,D\}$; một lần chọn $I$ cho một hàm $h_I$ dùng chung cho mọi vector của kho.
:::

Định nghĩa bao hàm Ví dụ 06.13 với $D=5$. Điều kiện "dùng chung cho mọi vector" là điều kiện "cùng $h$" của Định nghĩa 06.22: chọn chỉ số riêng cho từng vector làm phép thử không còn đo sự trùng tại cùng vị trí.

::: proposition Mệnh đề 06.29 (Xác suất trùng của họ chọn tọa độ)
**Giả thiết.** $x,y\in\Sigma^D$; $I$ đều trên $\{1,\ldots,D\}$, dùng chung cho $x$ và $y$.

**Kết luận.** $\Pr[h_I(x)=h_I(y)]=1-d_H(x,y)/D$. Do đó, với $0\le d_1<d_2\le D$, họ chọn tọa độ là $(d_1,d_2,1-d_1/D,1-d_2/D)$-nhạy cảm.

**Điều kiện áp dụng.** Mọi $D\ge1$, mọi bảng ký hiệu hữu hạn.

**Phạm vi.** Đẳng thức đúng chính xác, không phải xấp xỉ.
:::

::: proof Chứng minh Mệnh đề 06.29
**Bước 1 (đếm).** Biến cố $h_I(x)=h_I(y)$ xảy ra đúng khi $I$ thuộc tập các vị trí trùng, có $D-d_H(x,y)$ phần tử theo Định nghĩa 06.20. Vì $I$ đều trên $D$ chỉ số, xác suất là $(D-d_H(x,y))/D=1-d_H(x,y)/D$.

**Bước 2 (bộ tham số).** Hàm $d\mapsto1-d/D$ giảm, nên $d_H\le d_1$ cho xác suất ít nhất $1-d_1/D$ và $d_H\ge d_2$ cho xác suất nhiều nhất $1-d_2/D$; $d_1<d_2$ cho $1-d_2/D<1-d_1/D$. $\square$
:::

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ phép chọn đều: nếu $I$ luôn bằng $1$, cặp $10101$, $11110$ trùng với xác suất $1$ thay cho $2/5$.
- Bỏ chỉ số dùng chung: nếu $x$ và $y$ nhận hai chỉ số chọn riêng, thì với $x=y=10101$, cặp chỉ số $(1,2)$ cho hai giá trị $1$ và $0$; cặp vector trùng nhau, $d_H=0$, không còn trùng với xác suất $1$.

Bước 1 dùng cả hai giả thiết: phép chọn đều cho mẫu số $D$, chỉ số dùng chung cho phép đếm trên tập vị trí trùng.

Mệnh đề 06.29 có cùng dạng với Hệ quả 06.23: xác suất trùng bằng một trừ khoảng cách chuẩn hóa về $[0,1]$, ở đây $d_H/D$, ở đó $d_J$. Cả hai là đẳng thức, nên mọi cặp ngưỡng $d_1<d_2$ cho một bộ tham số. Khác biệt nằm ở số hàm: họ chọn tọa độ chỉ có $D$ hàm phân biệt, nên phép ghép phải lấy chỉ số có hoàn lại (Nhận xét 06.30).

::: remark Nhận xét 06.30 (Ghép nhiều hàm chọn tọa độ)
Họ chỉ có $D$ hàm, nhưng Mệnh đề 06.26 cần các hàm chọn độc lập. Khi ghép, các chỉ số được lấy độc lập, có hoàn lại; hai chỉ số có thể trùng nhau, và điều này không làm sai phép nhân xác suất. Mỗi phép thử chỉ đọc một phần tử của mảng, nên tốn $O(1)$ thời gian và lưu một chỉ số; $m$ phép thử lưu $m$ chỉ số dùng chung và $m$ giá trị mỗi vector.
:::

**Trong thực hành.** Vector bit thường được lưu thành các từ máy; đọc tọa độ $I$ là một phép dịch và một phép che bit, nên chi phí $O(1)$ của Nhận xét 06.30 đạt được. Các $m$ chỉ số được chọn một lần, lưu lại và dùng cho mọi vector của kho; nếu dữ liệu nạp sau dùng chỉ số khác, chữ ký cũ và mới không còn so được với nhau, vì giả thiết chỉ số dùng chung của Mệnh đề 06.29 bị vi phạm.

::: exercise Bài tập 06.8
Dữ kiện: $x=11001$, $y=10011$, $D=5$; họ chọn tọa độ với chỉ số chọn đều. Tính xác suất trùng của một hàm, và của phép ghép đồng thời bậc 2 với hai chỉ số lấy độc lập, có hoàn lại.
:::

::: hint
Đếm số vị trí khác trước, rồi dùng Mệnh đề 06.29 và Mệnh đề 06.26.
:::

::: solution
Hai vector khác tại vị trí 2 và 4, nên $d_H=2$ và xác suất trùng là $1-2/5=3/5$. Với hai chỉ số độc lập, phép ghép đồng thời cho $(3/5)^2=9/25=0{,}36$.

**Kiểm tra lại.** Ba vị trí trùng là 1, 3, 5, đúng $3$ trên $5$.
:::

<!-- note-topic-id: lec-06-topic-09 -->
### 4.2 Siêu phẳng, chữ ký dấu và khoảng cách góc

Khoảng cách góc chỉ phụ thuộc hướng, nên hàm băm cần cho cùng giá trị với $x$ và $2x$. Dấu của một tích vô hướng có tính chất đó.

::: example Ví dụ 06.14 (Dấu theo hai pháp tuyến)
**Dữ kiện.** Theo Ví dụ 3.22 của MMDS (tr.111), $x=(3,4,5,6)$, $y=(4,3,2,1)$; hai vector $v_1=(1,-1,1,1)$, $v_2=(-1,1,-1,1)$.

**Tính.** $v_1\cdot x=3-4+5+6=10$ và $v_1\cdot y=4-3+2+1=4$: cùng dấu dương. $v_2\cdot x=-3+4-5+6=2$ và $v_2\cdot y=-4+3-2+1=-2$: khác dấu.

**Kiểm tra lại.** $v_1\cdot(2x)=20$ vẫn dương: nhân $x$ với hệ số dương không đổi dấu.
:::

Một cách trực quan, mỗi vector $v$ xác định một siêu phẳng qua gốc vuông góc với nó; dấu cho biết điểm nằm phía nào. Hai vector có góc nhỏ hiếm khi bị một siêu phẳng ngẫu nhiên tách ra hai phía. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.31 (Hàm băm dấu và họ siêu phẳng)
Với $v\in\mathbb R^D$, $v\ne0$, **siêu phẳng** qua gốc với **pháp tuyến** (normal vector) $v$ là tập $\{x:\ v\cdot x=0\}$. **Hàm băm dấu** là

$$
h_v(x)=\operatorname{sign}(v\cdot x),\qquad \operatorname{sign}(\tau)=\begin{cases}+1,&\tau\ge0,\\-1,&\tau<0.\end{cases}
$$

**Họ siêu phẳng** gồm các hàm $h_v$, với $v$ chọn theo một phân phối **đẳng hướng** (isotropic): phân phối của $v$ không đổi qua mọi phép quay quanh gốc, nên hướng của $v$ đều trên mặt cầu đơn vị. Cùng một $v$ được dùng cho mọi vector.
:::

Pháp tuyến vuông góc với mặt phân chia; nó không phải chính mặt đó. Quy ước $\operatorname{sign}(0)=+1$ làm hàm xác định khắp nơi. Ví dụ 06.14 dùng hai pháp tuyến cố định có tọa độ $\pm1$; chúng là hai hàm của họ, nhưng chọn chúng theo cách đó không phải phép chọn đẳng hướng.

![Hình hai chiều: mặt phân chia v · x = 0 nằm ngang; pháp tuyến v vuông góc với nó, hướng lên miền ghi Dấu +; nửa dưới ghi Dấu −.](img/lec-06/phap-tuyen-dau.svg)

Hình chỉ mô tả quan hệ trong mặt phẳng, không phải tọa độ của Ví dụ 06.14: mọi điểm phía mà $v$ chỉ tới có $h_v=+1$, mọi điểm phía còn lại có $h_v=-1$.

::: theorem Định lý 06.32 (Xác suất cùng dấu)
**Giả thiết.** $x,y\in\mathbb R^D$ khác $0$ tạo góc $\theta\in[0,\pi]$ đo bằng radian; $v$ chọn theo phân phối đẳng hướng, dùng chung cho $x$ và $y$.

**Kết luận.** $\Pr[h_v(x)\ne h_v(y)]=\theta/\pi$ và $\Pr[h_v(x)=h_v(y)]=1-\theta/\pi$. Do đó, với $0\le d_1<d_2\le\pi$, họ siêu phẳng là $(d_1,d_2,1-d_1/\pi,1-d_2/\pi)$-nhạy cảm theo khoảng cách góc.

**Điều kiện áp dụng.** Mọi $D\ge1$; khi $D=1$ chỉ xảy ra hai trường hợp $\theta\in\{0,\pi\}$ của Bước 1.

**Phạm vi.** Định lý không áp dụng cho pháp tuyến chọn theo phân phối không đẳng hướng, như các vector $\pm1$ của Ví dụ 06.14.
:::

::: proof Chứng minh Định lý 06.32
**Bước 1 (hai trường hợp biên).** Nếu $\theta=0$, $y=\lambda x$ với $\lambda>0$, nên $v\cdot y=\lambda\,v\cdot x$ cùng dấu và cùng bằng $0$ hay không; hai giá trị băm luôn bằng nhau. Nếu $\theta=\pi$, $y=-\lambda x$ với $\lambda>0$; hai tích vô hướng trái dấu trừ khi $v\cdot x=0$, biến cố có xác suất $0$ dưới phân phối đẳng hướng. Cả hai trường hợp khớp với $\theta/\pi$.

**Bước 2 (chuyển về mặt phẳng).** Với $0<\theta<\pi$, $x$ và $y$ không cùng phương nên sinh một mặt phẳng $\Pi$. Viết $v=v_\Pi+v_\perp$ với $v_\Pi\in\Pi$ và $v_\perp$ vuông góc với $\Pi$. Vì $x,y\in\Pi$, $v\cdot x=v_\Pi\cdot x$ và $v\cdot y=v_\Pi\cdot y$. Mọi phép quay trong $\Pi$, giữ nguyên phần vuông góc với $\Pi$, là một phép quay quanh gốc, nên theo tính đẳng hướng nó không đổi phân phối của $v$; do đó phân phối hướng của $v_\Pi$ không đổi qua mọi phép quay trong $\Pi$, tức đều trên đường tròn đơn vị của $\Pi$. Biến cố $v_\Pi=0$ có xác suất $0$.

**Bước 3 (đếm góc).** Trong $\Pi$, dấu của $v_\Pi\cdot x$ đổi khi hướng của $v_\Pi$ đi qua đường thẳng vuông góc với $x$, và tương tự với $y$. Hai dấu khác nhau đúng khi hướng của $v_\Pi$ nằm giữa hai đường vuông góc ấy, gồm hai cung đối nhau, mỗi cung có số đo $\theta$. Do hướng đều trên đường tròn,

$$
\Pr[h_v(x)\ne h_v(y)]=\frac{2\theta}{2\pi}=\frac\theta\pi.
$$

Lấy biến cố bù được xác suất cùng dấu; bộ tham số suy ra như Bước 2 của chứng minh Mệnh đề 06.29, với hàm giảm $\theta\mapsto1-\theta/\pi$. $\square$
:::

![Đường tròn với hai mũi tên x và y tạo góc θ, có cung θ giữa chúng; hai miền hướng pháp tuyến đối nhau làm khác dấu, mỗi miền có góc θ; chú giải ghi tổng góc 2θ trên góc 2π và hướng hình chiếu pháp tuyến đều trên vòng tròn.](img/lec-06/goc-tach-sieu-phang.svg)

Hình vẽ Bước 3 trong mặt phẳng $\Pi$: hai miền tô là các hướng của $v_\Pi$ làm $x$, $y$ khác dấu, tổng số đo $2\theta$ trên cả vòng $2\pi$. Với $\theta=\pi/3$ của Ví dụ 06.8, xác suất cùng dấu là $2/3$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ tính đẳng hướng: nếu $v$ chọn đều trong 16 vector có tọa độ $\pm1$ của $\mathbb R^4$, thì với $x=(3,4,5,6)$, $y=(4,3,2,1)$ có đúng 4 vector cho hai dấu khác nhau theo quy ước $\operatorname{sign}(0)=+1$, nên xác suất khác dấu là $1/4$, ứng với góc $45^\circ$, trong khi góc thật xấp xỉ $38{,}047579^\circ$ (Tình huống 06.4).
- Bỏ đơn vị radian: thay $\theta=60$ (độ) vào $1-\theta/\pi$ cho một số âm, không phải xác suất; giá trị đúng là $1-(\pi/3)/\pi=2/3$.
- Bỏ điều kiện khác $0$: với $x=0$, $v\cdot x=0$ nên $h_v(x)=+1$ với mọi $v$, trong khi góc giữa $0$ và $y$ không xác định.
- Bỏ pháp tuyến dùng chung: nếu $x$ và $y$ được băm bằng hai pháp tuyến đẳng hướng độc lập, thì với $y=x$, mỗi dấu bằng $+1$ hay $-1$ với xác suất $1/2$ độc lập nhau, nên hai giá trị trùng với xác suất $1/2$ thay cho $1$.

Bước 1 dùng điều kiện khác $0$; Bước 2 dùng pháp tuyến dùng chung và tính đẳng hướng; Bước 3 dùng tính đẳng hướng và đơn vị radian.

Định lý 06.32 có cùng dạng với Hệ quả 06.23 và Mệnh đề 06.29: xác suất trùng bằng một trừ khoảng cách chuẩn hóa, ở đây $\theta/\pi$, và là đẳng thức. Giả thiết quyết định không còn là phép chọn đều một chỉ số trong tập hữu hạn mà là tính đẳng hướng của một vector liên tục; cái giá là mỗi hàm tốn $O(D)$ thay cho $O(1)$.

**Trong thực hành.** MMDS §3.7.3 hạn chế pháp tuyến vào các vector có tọa độ $\pm1$; khi đó tích vô hướng chỉ cần cộng và trừ các tọa độ. Lựa chọn này giảm chi phí tính nhưng bỏ tính đẳng hướng, nên Định lý 06.32 không còn bảo đảm; Tình huống 06.4 đo hậu quả trên Ví dụ 3.22. Các pháp tuyến được sinh một lần và lưu lại, vì mọi vector của kho phải được băm bằng cùng các pháp tuyến.

Từ Định lý 06.32, mỗi bit dấu là một phép thử có xác suất khác dấu $\theta/\pi$, nên tỷ lệ bit khác dấu trên nhiều pháp tuyến cho một ước lượng của góc. Dãy $m$ bit dấu của một vector theo $m$ pháp tuyến gọi là **chữ ký dấu** (sketch) của vector. Ví dụ sau chạy quy tắc này với ba pháp tuyến cố định của sách.

::: example Ví dụ 06.15 (Chữ ký dấu với ba pháp tuyến cố định)
**Dữ kiện.** Theo Ví dụ 3.22 của MMDS (tr.111), $x=(3,4,5,6)$, $y=(4,3,2,1)$ và ba pháp tuyến $v_1=(1,-1,1,1)$, $v_2=(-1,1,-1,1)$, $v_3=(1,1,-1,-1)$.

**Tích và dấu.**

| Pháp tuyến | Tích với $x$ | Tích với $y$ |
|---|---:|---:|
| $v_1$ | 10 | 4 |
| $v_2$ | 2 | −2 |
| $v_3$ | −4 | 4 |

Chữ ký dấu của $x$ là $(+,+,-)$, của $y$ là $(+,-,+)$; hai bit cuối khác nhau.

**Ước lượng.** Tỷ lệ bit khác dấu $\widehat p_{\ne}=2/3$, nên góc ước lượng $\widehat\theta=\pi\cdot2/3=2\pi/3=120^\circ$.

**Góc thật.** $x\cdot y=40$, $\|x\|_2^2=86$, $\|y\|_2^2=30$, nên $\theta=\arccos(40/\sqrt{2580})\approx38{,}047579^\circ$.

**Kiểm tra lại.** $86\cdot30=2580$ và $40/\sqrt{2580}\approx0{,}7875$, cho góc khoảng $38{,}05^\circ$, xa $120^\circ$.
:::

::: algorithm Thuật toán 06.33 (Chữ ký dấu và ước lượng góc)
**Đầu vào.** Các vector khác $0$ $x_1,\ldots,x_C\in\mathbb R^D$; số bit $m\ge1$.

**Đầu ra.** Chữ ký dấu $m$ bit của mỗi vector; với một cặp $(c,d)$, góc ước lượng $\widehat\theta_{cd}$.

**Giả thiết.** Các pháp tuyến được chọn độc lập theo phân phối đẳng hướng và dùng chung cho mọi vector.

1. Chọn $m$ pháp tuyến $v_1,\ldots,v_m$ độc lập theo một phân phối đẳng hướng, chẳng hạn mỗi tọa độ lấy độc lập theo phân phối chuẩn tắc; cách sinh và chứng minh tính đẳng hướng của nó nằm ngoài phạm vi chương, MMDS §3.7.2 chỉ nói chọn vector ngẫu nhiên. Biến thể có tọa độ $\pm1$ của Ví dụ 3.22 không đẳng hướng.
2. Với mỗi vector $x_c$ và mỗi $i$: tính $v_i\cdot x_c$ và ghi bit $h_{v_i}(x_c)$.
3. Với một cặp $(c,d)$: đếm số bit khác nhau, đặt $\widehat p_{\ne}$ là tỷ lệ bit khác trên $m$ và $\widehat\theta_{cd}=\pi\,\widehat p_{\ne}$.

```text
chọn v_1, …, v_m độc lập, đẳng hướng
với c = 1, …, C:
    với i = 1, …, m:
        sig[c][i] ← +1 nếu v_i · x_c ≥ 0, ngược lại −1
ước lượng cặp (c, d):
    p ← (số i có sig[c][i] ≠ sig[d][i]) / m
    trả π · p
```

**Dừng.** Các vòng lặp có $Cm$ và $m$ lượt.

**Trường hợp biên.** Vector $0$ nằm ngoài đầu vào; tích vô hướng bằng $0$ cho bit $+1$.

**Chi phí.** Bảng đếm cho vector đặc:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1: lưu pháp tuyến | $m$ | $D$ từ | $O(mD)$ bộ nhớ |
| 2: tích vô hướng và dấu | $Cm$ | $O(D)$ | $O(CmD)$ thời gian |
| 3: so hai chữ ký | $1$ mỗi cặp | $O(m)$ | $O(m)$ mỗi cặp |
:::

Theo Định lý 06.32 và tuyến tính kỳ vọng, $\mathbb E[\widehat p_{\ne}]=\theta/\pi$, nên $\pi\widehat p_{\ne}$ là ước lượng có kỳ vọng bằng góc khi giả thiết của thuật toán thỏa. Ví dụ 06.15 chạy bước 2 và bước 3 với $m=3$ nhưng vi phạm giả thiết đẳng hướng; độ lệch $120^\circ$ so với $38{,}05^\circ$ đến từ cả số bit ít và phân phối pháp tuyến.

**Trong thực hành.** Chữ ký dấu được lưu thành dãy $m$ bit, và số bit khác nhau ở bước 3 là khoảng cách Hamming của hai dãy bit; vì vậy các chữ ký dấu có thể đưa tiếp vào họ chọn tọa độ của Mục 4.1 và Thuật toán 06.4 mà không đọc lại vector gốc. Khi các pháp tuyến độc lập và đẳng hướng, $m$ bit khác dấu là $m$ biến Bernoulli độc lập tham số $\theta/\pi$, nên phương sai của $\widehat p_{\ne}$ là $(\theta/\pi)(1-\theta/\pi)/m$, giảm tỷ lệ nghịch với $m$; điều này không sửa được sai lệch do pháp tuyến $\pm1$ ở Tình huống 06.4.

::: exercise Bài tập 06.9
Dữ kiện: $x=(1,0)$, $y=(-1,1)$ trong $\mathbb R^2$; họ siêu phẳng với pháp tuyến đẳng hướng.

(a) Tính xác suất cùng dấu của $x$ và $y$.

(b) Nêu các điều kiện để dùng đẳng thức $\Pr[h_v(x)=h_v(y)]=1-\theta/\pi$.
:::

::: hint
Tính góc bằng radian trước khi thế vào công thức.
:::

::: solution
(a) $x\cdot y=-1$, $\|x\|_2=1$, $\|y\|_2=\sqrt2$, nên $\cos\theta=-1/\sqrt2$ và $\theta=3\pi/4$. Xác suất cùng dấu là $1-3/4=1/4$.

(b) Hai vector khác $0$; pháp tuyến chọn theo phân phối đẳng hướng và dùng chung cho cả hai; $\theta$ đo bằng radian.

**Kiểm tra lại.** $3\pi/4=135^\circ$, và $1-135/180=1/4$ theo cách viết bằng độ của MMDS.
:::

<!-- note-topic-id: lec-06-topic-10 -->
### 4.3 Chiếu có dịch ngẫu nhiên cho khoảng cách Euclid

Hàm băm dấu bỏ mất độ dài, nên không phân biệt được hai điểm cùng hướng nhưng cách xa nhau. Khoảng cách Euclid cần một hàm giữ độ lớn của tọa độ. Một cách tự nhiên là chiếu điểm lên một đường thẳng, chia đường thẳng thành các khoảng bằng nhau và dùng chỉ số khoảng làm giá trị băm.

::: example Ví dụ 06.16 (Ba điểm trên trục thứ nhất)
**Dữ kiện.** Theo Bài 3.7.5 của MMDS (tr.114), ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$. Chiếu lên trục thứ nhất, chia trục thành các khoảng nửa mở $[ka,(k+1)a)$ với $a=1$, không dịch biên.

**Tính.** Mã của một điểm là $\lfloor x_1/a\rfloor$, lần lượt $1$, $0$, $4$. Ba điểm thuộc ba khoảng $[1,2)$, $[0,1)$, $[4,5)$.

**Kết luận.** Trục này không đặt hai điểm nào vào cùng thùng. Kết quả trên ba trục và hai độ rộng là nội dung của Bài tập 06.25.

**Kiểm tra lại.** $\lfloor1\rfloor=1$, $\lfloor0\rfloor=0$, $\lfloor4\rfloor=4$.
:::

Ví dụ 06.16 dùng một trục cố định và các biên cố định tại các số nguyên. Hai điểm có hình chiếu $1-\varepsilon$ và $1+\varepsilon$, với $\varepsilon>0$ nhỏ, rất gần nhau nhưng luôn bị biên $1$ tách ra. Một cách trực quan, chọn ngẫu nhiên cả hướng chiếu lẫn vị trí biên làm xác suất hai điểm chung thùng phụ thuộc vào khoảng cách giữa chúng chứ không vào vị trí của chúng so với một lưới cố định. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.34 (Họ chiếu có dịch)
Cho số chiều $D\ge1$ và độ rộng khoảng $a>0$. Một hàm của **họ chiếu có dịch** trên $\mathbb R^D$ được xác định bởi một vector đơn vị $u\in\mathbb R^D$ và một độ dịch $\delta\in[0,a)$:

$$
h_{u,\delta}(x)=\Bigl\lfloor\frac{u\cdot x+\delta}{a}\Bigr\rfloor.
$$

Phân phối chọn hàm: $u$ đều trên mặt cầu đơn vị của $\mathbb R^D$, với $D=2$ là đường tròn đơn vị; $\delta$ đều trên $[0,a)$, độc lập với $u$. Cùng cặp $(u,\delta)$ được dùng cho mọi điểm.
:::

Giá trị $h_{u,\delta}(x)$ gọi là chỉ số khoảng, trên trang chiếu gọi là mã thùng. Trên đường thẳng hướng $u$, thùng có chỉ số $k$ là khoảng $[ka-\delta,(k+1)a-\delta)$, đóng bên trái và mở bên phải. Ví dụ 06.16 dùng một hàm cùng dạng trên $\mathbb R^3$ với $u=e_1=(1,0,0)$ và $\delta=0$, nên nó là một hàm của họ với $D=3$ nhưng không phải một phép chọn ngẫu nhiên. MMDS §3.7.4 (tr.111–113) mô tả phép chiếu lên đường thẳng ngẫu nhiên và chia khoảng nhưng không có độ dịch; cơ chế dịch đều được lấy theo Datar, Immorlica, Indyk và Mirrokni (2004, §3.2).

![Trục hình chiếu chia thành các khoảng nửa mở độ rộng a, đánh số k = −2 đến k = 2, biên có dạng ka − δ; hai hình chiếu u·x và u·y cách nhau ℓ, có thể bị một biên tách ra.](img/lec-06/chia-khoang-dich.svg)

Hình cho thấy hai hình chiếu cách nhau $\ell$ và các biên cách đều $a$; dịch $\delta$ trượt toàn bộ lưới biên. Hai điểm khác thùng đúng khi có một biên nằm giữa hai hình chiếu.

::: lemma Bổ đề 06.35 (Xác suất chung thùng khi cố định hướng)
**Giả thiết.** $x,y\in\mathbb R^D$; vector đơn vị $u$ cố định; $\ell=\lvert u\cdot(x-y)\rvert$; $\delta$ đều trên $[0,a)$, dùng chung cho hai điểm.

**Kết luận.** $\Pr_\delta[h_{u,\delta}(x)=h_{u,\delta}(y)\mid u]=\max(0,1-\ell/a)$.

**Điều kiện áp dụng.** Mọi $a>0$.

**Phạm vi.** Bổ đề cố định $u$ và chỉ dùng hình chiếu lên một đường thẳng, nên đúng với mọi $D$; Định lý 06.36 lấy trung bình theo $u$ khi $D=2$.
:::

::: proof Chứng minh Bổ đề 06.35
**Bước 1 ($\ell=0$).** Hai hình chiếu bằng nhau nên luôn chung thùng; xác suất $1=1-0/a$.

**Bước 2 ($0<\ell<a$).** Các biên lặp lại với chu kỳ $a$. Khi $\delta$ chạy trên $[0,a)$, một biên nằm giữa hai hình chiếu khi vị trí biên rơi vào đoạn dài $\ell$ giữa chúng, và vì $\ell<a$ có nhiều nhất một biên như vậy. Do $\delta$ đều, xác suất có biên ở giữa là $\ell/a$, bỏ qua trường hợp biên trùng đúng một hình chiếu, có xác suất $0$. Xác suất chung thùng là $1-\ell/a$.

**Bước 3 ($\ell\ge a$).** Một khoảng nửa mở rộng $a$ không chứa hai điểm cách nhau ít nhất $a$, nên xác suất chung thùng là $0$.

Ba trường hợp gộp lại thành $\max(0,1-\ell/a)$. $\square$
:::

Bổ đề nói rằng, sau khi cố định hướng, xác suất chung thùng giảm tuyến tính theo khoảng cách của hai hình chiếu. Giả thiết dịch đều không bỏ được: với $\delta=0$ cố định và $a=1$, hai hình chiếu $1-\varepsilon$ và $1+\varepsilon$, $0<\varepsilon<1/2$, có mã $0$ và $1$, nên không bao giờ chung thùng dù $\ell=2\varepsilon$ nhỏ tùy ý và công thức cho $1-2\varepsilon$. Bước 2 là bước dùng giả thiết này.

::: theorem Định lý 06.36 (Họ chiếu có dịch trong hai chiều)
**Giả thiết.** $D=2$; $x,y\in\mathbb R^2$, $\rho=\|x-y\|_2$; $u$ đều trên đường tròn đơn vị, $\delta$ đều trên $[0,a)$, độc lập với $u$; cùng $(u,\delta)$ cho hai điểm.

**Kết luận.** Nếu $\rho\le a/2$ thì xác suất chung thùng ít nhất $1/2$; nếu $\rho\ge2a$ thì xác suất chung thùng nhiều nhất $1/3$. Do đó họ chiếu có dịch là $(a/2,2a,1/2,1/3)$-nhạy cảm theo khoảng cách Euclid trên $\mathbb R^2$.

**Điều kiện áp dụng.** Mọi $a>0$. Cận gần dùng dịch đều; cận xa chỉ dùng hướng đều và đúng với mọi cách chọn $\delta$, kể cả $\delta$ cố định.

**Phạm vi.** Định lý được phát biểu và chứng minh cho $D=2$, theo MMDS §3.7.4 (tr.111–113); chương không phát biểu cận xa cho số chiều khác.
:::

::: proof Chứng minh Định lý 06.36
**Bước 1 (cận gần).** Với mọi hướng đơn vị $u$, $\ell=\lvert u\cdot(x-y)\rvert\le\|u\|_2\|x-y\|_2=\rho$ theo Cauchy–Schwarz. Nếu $\rho\le a/2$, Bổ đề 06.35 cho xác suất có điều kiện ít nhất $1-\rho/a\ge1/2$ với mọi $u$; lấy trung bình theo $u$ giữ cận $1/2$.

**Bước 2 (cận xa).** Gọi $\phi\in[0,\pi/2]$ là góc nhọn giữa đường chiếu và đoạn nối hai điểm. Khi đó $\ell=\rho\lvert\cos\phi\rvert$. Với mọi $\delta$, một khoảng nửa mở rộng $a$ không chứa hai hình chiếu cách nhau ít nhất $a$ (Bước 3 của chứng minh Bổ đề 06.35), nên chung thùng cần $\ell<a$, tức $\lvert\cos\phi\rvert<a/\rho\le1/2$ khi $\rho\ge2a$, tức $\phi>\pi/3$. Trong mặt phẳng, gọi $\alpha$ là góc cực của $u$, đều trên $[0,2\pi)$, và $\beta$ là góc cực của $x-y$. Khi đó $\gamma=(\alpha-\beta)\bmod\pi$ đều trên $[0,\pi)$ và $\phi=\min(\gamma,\pi-\gamma)$; với $0\le\psi\le\pi/2$, $\Pr[\phi\le\psi]=\Pr[\gamma\le\psi]+\Pr[\gamma\ge\pi-\psi]=2\psi/\pi$, nên $\phi$ đều trên $[0,\pi/2]$ và

$$
\Pr[\phi>\pi/3]=\frac{\pi/2-\pi/3}{\pi/2}=\frac13.
$$

Điều kiện $\phi>\pi/3$ cần nhưng chưa đủ cho chung thùng, nên xác suất chung thùng nhiều nhất $1/3$. Bước này không dùng phân phối của $\delta$. $\square$
:::

![Đoạn nối x với y dài ρ tạo góc nhọn φ với trục chiếu u; đường vuông góc nét đứt xác định đoạn chiếu dài ℓ = ρ |cos φ|.](img/lec-06/hinh-chieu-euclid.svg)

Hình minh họa đẳng thức $\ell=\rho\lvert\cos\phi\rvert$ của Bước 2: góc $\phi$ càng gần $\pi/2$, hình chiếu càng ngắn dù đoạn nối dài. Hình không ấn định tỷ lệ giữa $\rho$ và $a$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ dịch đều: với $\delta=0$ cố định, hai điểm $(\varepsilon,0)$ và $(-\varepsilon,0)$ với $0<\varepsilon\le a/4$ có $\rho=2\varepsilon\le a/2$. Với mọi hướng có $\cos\phi\ne0$, hai hình chiếu $\pm\varepsilon\cos\phi$ nằm hai phía của biên $0$, có mã $0$ và $-1$, nên xác suất chung thùng bằng $0$, nhỏ hơn $1/2$.
- Bỏ hướng đều: nếu $u$ luôn vuông góc với $x-y$, thì $\ell=0$ và hai điểm luôn chung thùng với mọi $\rho$, kể cả $\rho\ge2a$; xác suất $1$ lớn hơn $1/3$.

Bước 1 dùng dịch đều qua Bổ đề 06.35 và đúng với từng hướng, nên không cần hướng đều. Bước 2 dùng hướng đều trong mặt phẳng để có $\phi$ đều và đúng với mọi $\delta$, nên không cần dịch đều. Giới hạn hai chiều chỉ thuộc Bước 2: tính chất "$\phi$ đều trên $[0,\pi/2]$" đúng trong mặt phẳng; ngoài hai chiều, chứng minh trên không cho cận $1/3$ và chương này không phát biểu cận thay thế.

::: remark Nhận xét 06.37 (Trục cố định, ngưỡng gần nhau và chi phí)
Ba trục cố định của Bài tập 06.25 là ba hàm cụ thể của họ, không phải phép chọn ngẫu nhiên, nên không thừa hưởng bảo đảm của Định lý 06.36. Các ngưỡng $a/2$ và $2a$ cách nhau bốn lần.

MMDS §3.7.5 (tr.113) nêu một lập luận định tính cho mọi cặp $d_1<d_2$ và mọi số chiều: với phép chiếu lên đường thẳng ngẫu nhiên và chia khoảng, xác suất chung thùng $p_1$ ở khoảng cách $d_1$ lớn hơn xác suất $p_2$ ở khoảng cách $d_2$, vì xác suất này tăng khi khoảng cách giảm; sau đó phép ghép AND và OR của Mục 3.7 kéo $p_1$ và $p_2$ ra xa nhau. Sách không tính $p_1$, $p_2$, không chứng minh tính đơn điệu và không dùng độ dịch, nên lập luận này chỉ được dùng như định hướng, không như một định lý.

Mỗi hàm tính một tích vô hướng, cộng dịch, chia cho $a$ và lấy sàn, tốn $O(D)$ trên vector $D$ chiều.
:::

**Trong thực hành.** Dữ liệu vector thường có nhiều hơn hai chiều. Định nghĩa 06.34 dùng được trên $\mathbb R^D$ và Bước 1 của chứng minh Định lý 06.36 đúng với từng hướng, nhưng cận xa $1/3$ chỉ được chứng minh cho hai chiều; MMDS §3.7.5 chỉ nêu định tính rằng phép chiếu lên đường thẳng ngẫu nhiên và chia khoảng vẫn cho một họ nhạy cảm trong nhiều chiều. Hằng $1/3$ không được chuyển sang chiều khác. Độ rộng $a$ đặt thang đo của "gần": cùng một cặp điểm có thể là cặp gần với $a$ lớn và cặp xa với $a$ nhỏ, nên $a$ phải chọn theo khoảng cách cần phân biệt của bài toán.

::: exercise Bài tập 06.10
Dữ kiện: họ chiếu có dịch trên $\mathbb R^2$ với $a=2$ (Định nghĩa 06.34).

(a) Với $u$ cố định, hai hình chiếu cách nhau $\ell=0{,}5$. Tính xác suất chung thùng theo $\delta$.

(b) Với $0<\ell<a$, xác định hai hình chiếu có chắc chung thùng hay không.

(c) Một cặp có $\|x-y\|_2=5$. Nêu cận xác suất chung thùng và các giả thiết cần cho cận đó.
:::

::: hint
Câu (a), (b) dùng Bổ đề 06.35. Câu (c) so $5$ với $2a$.
:::

::: solution
(a) $1-0{,}5/2=0{,}75$.

(b) Chưa chắc: một biên có thể nằm giữa hai hình chiếu; xác suất chung thùng là $1-\ell/a<1$. Chỉ trường hợp $\ell=0$ luôn chung thùng.

(c) Vì $5\ge2a=4$, cặp là cặp xa và xác suất chung thùng nhiều nhất $1/3$. Cận cần $u$ đều trên đường tròn, cùng hàm cho hai điểm và dữ liệu hai chiều. Theo Bước 2 của chứng minh Định lý 06.36, cận xa đúng với mọi cách chọn $\delta$, nên không cần dịch đều.

**Kiểm tra lại.** Ở (a), $\ell=0{,}5<a=2$ nên trường hợp $\max$ lấy nhánh $1-\ell/a$.
:::

<!-- note-topic-id: lec-06-topic-17 -->
### 4.4 Chi phí tính chữ ký của ba họ

Ba họ có xác suất trùng khác nhau và cũng có chi phí tính khác nhau. Chi phí phân dải ở Mệnh đề 06.11 bắt đầu khi chữ ký đã có; với họ MinHash, chữ ký thuộc Bài 05, còn với ba họ mới, chữ ký phải được tính từ vector. Mô hình đếm: vector đặc $D$ chiều, mỗi số chiếm một từ máy, mỗi phép đọc, nhân, cộng, chia, so sánh hoặc lấy sàn tốn thời gian hằng.

::: proposition Mệnh đề 06.38 (Chi phí tính chữ ký của ba họ)
**Giả thiết.** Mô hình đếm vừa nêu; chữ ký gồm $m$ hàm cho $C$ vector; tham số của $m$ hàm được chọn trước và dùng chung.

**Kết luận.** Tính chữ ký tốn $O(Cm)$ thời gian với họ chọn tọa độ và $O(CmD)$ với họ siêu phẳng và họ chiếu có dịch. Tham số của các hàm chiếm $O(m)$ từ với họ thứ nhất và $O(mD)$ từ với hai họ còn lại; mỗi vector lưu $m$ giá trị.

**Điều kiện áp dụng.** Vector đặc. Với vector thưa có $\mathrm{nnz}(x)$ thành phần khác $0$, tích vô hướng chỉ duyệt các thành phần ấy, nên $D$ được thay bằng $\mathrm{nnz}(x)$.

**Phạm vi.** Đây là chi phí lấy chữ ký; dựng thùng, phát $Q$ cặp và xác minh $K$ cặp được tính thêm theo Mệnh đề 06.11.
:::

::: proof Chứng minh Mệnh đề 06.38
Đếm phép tính của một hàm trên một vector, theo Định nghĩa 06.28, 06.31 và 06.34:

| Họ | Phép tính của một hàm | Thời gian | Tham số lưu |
|---|---|---|---|
| Chọn tọa độ | 1 lần đọc | $O(1)$ | 1 chỉ số |
| Siêu phẳng | $D$ phép nhân, $D-1$ phép cộng, 1 so sánh | $O(D)$ | $D$ từ |
| Chiếu có dịch | $D$ phép nhân, $D$ phép cộng, 1 phép chia, 1 lấy sàn | $O(D)$ | $D+1$ từ |

Chữ ký cần $Cm$ lần tính hàm; nhân với cột thời gian cho kết luận. Tham số của $m$ hàm được lưu một lần cho cả kho. $\square$
:::

**Trong thực hành.** Với $D$ lớn, phần tốn kém là $m$ tích vô hướng trên mỗi vector. Xếp $m$ pháp tuyến thành một ma trận $m\times D$ thì chữ ký của cả kho là một phép nhân ma trận, tính được theo khối và song song theo vector mà không đổi số phép nhân $CmD$. Với vector thưa, như vector tần suất từ của văn bản, chi phí tính theo $\mathrm{nnz}(x)$ của Điều kiện áp dụng. Bộ tham số $O(mD)$ phải được lưu cùng kho, vì vector nạp sau phải dùng đúng các pháp tuyến và độ dịch ấy thì chữ ký mới so được với chữ ký cũ.

Mệnh đề 06.38 cho thấy họ chọn tọa độ rẻ hơn hai họ kia một thừa số $D$, đổi lại chỉ dùng được cho Hamming. Bảng của Ví dụ 06.15 có $6$ tích vô hướng, ba pháp tuyến nhân với hai vector, mỗi tích $4$ phép nhân; tổng $6\cdot4=24$ phép nhân khớp với $CmD=2\cdot3\cdot4$.

::: exercise Bài tập 06.11
Dữ kiện: kho $C=10^6$ vector đặc, $D=1000$ chiều; chữ ký $m=200$ hàm siêu phẳng.

Đếm số phép nhân để tính chữ ký, số từ lưu các pháp tuyến và số bit chữ ký của cả kho.
:::

::: hint
Mỗi hàm cần $D$ phép nhân cho một vector; các pháp tuyến dùng chung cho cả kho.
:::

::: solution
Số phép nhân là $C\cdot m\cdot D=10^6\cdot200\cdot1000=2\cdot10^{11}$. Các pháp tuyến cần $m\cdot D=2\cdot10^5$ từ. Chữ ký dấu cần $m=200$ bit mỗi vector, tức $2\cdot10^8$ bit cho cả kho.

**Kiểm tra lại.** Dữ liệu gốc có $C\cdot D=10^9$ số, mỗi số một từ. Với từ $64$ bit, dữ liệu gốc chiếm $6{,}4\cdot10^{10}$ bit, gấp $320$ lần $2\cdot10^8$ bit chữ ký.
:::

Như vậy, chúng ta đã có ba họ cơ sở với bộ tham số chứng minh được: họ chọn tọa độ cho Hamming (Mệnh đề 06.29), họ siêu phẳng cho góc (Định lý 06.32) cùng quy tắc ước lượng góc (Thuật toán 06.33), và họ chiếu có dịch cho khoảng cách Euclid trong hai chiều (Bổ đề 06.35, Định lý 06.36); chi phí lấy chữ ký là $O(Cm)$ hoặc $O(CmD)$ (Mệnh đề 06.38). Mỗi họ đưa vào phép ghép của Mục 3.7 và Thuật toán 06.4 mà không đổi thùng hay bước xác minh.

Tuy nhiên, các kết quả này giả định dữ liệu đã ở dạng tập, vector bit hay vector số với độ đo đã chọn, và giả định hàm băm được chọn ngẫu nhiên từ một họ. Trong Mục 5, chúng ta xét ba bài toán của MMDS §3.8, nơi việc chọn biểu diễn, chọn hàm và thậm chí việc có hay không một phân phối chọn hàm là phần chính của lời giải.

## 5. Ứng dụng tìm cặp tương đồng

Kho một triệu tài liệu đã có sẵn biểu diễn tập và họ MinHash, nên cả năm thành phần của khung tìm cặp (biểu diễn, họ cơ sở, phép ghép, thùng, xác minh) đều xác định. Ba bài toán của MMDS §3.8 thì không: hồ sơ khách hàng, ảnh vân tay và trang báo kèm quảng cáo chưa có biểu diễn hay họ ngẫu nhiên đã chứng minh. Với từng bài toán, chúng ta xác định thành phần nào phải đổi và giả thiết nào còn đúng.

<!-- note-topic-id: lec-06-topic-11 -->
### 5.1 Đối sánh thực thể

Theo MMDS §3.8.1–3.8.2 (tr.114–116), hai nguồn mỗi nguồn khoảng $10^6$ hồ sơ khách hàng, gồm tên, địa chỉ và điện thoại, cần được ghép các cặp hồ sơ cùng mô tả một người. Chấm điểm mọi cặp giữa hai nguồn cần $10^{12}$ lần. Hai hồ sơ của cùng một người thường khác nhau ở cách viết tên, lỗi gõ hoặc số điện thoại cũ, nên không thể đòi mọi trường trùng nhau.

Một cách trực quan, hai hồ sơ của cùng một người thường trùng hoàn toàn ở ít nhất một trường, nên mỗi trường có thể đóng vai một dải của Mục 2. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.39 (Hàm khóa và quy tắc ứng viên theo trường)
Một **hàm khóa** gán cho mỗi hồ sơ giá trị của một trường: tên, địa chỉ hoặc điện thoại. Một cặp gồm một hồ sơ của nguồn A và một hồ sơ của nguồn B là **cặp ứng viên** khi hai hồ sơ có cùng giá trị ở ít nhất một trong ba hàm khóa. Mỗi cặp ứng viên được **chấm điểm** trên cả ba trường và được nhận khi điểm vượt một ngưỡng.
:::

Quy tắc ứng viên là phép ghép ít nhất một trên ba hàm khóa, tức phân dải với $b=3$ dải, mỗi dải một hàm, $r=1$; MMDS thay bảng băm bằng ba lần sắp xếp hai nguồn theo từng trường. Bước chấm điểm đóng vai bước xác minh: ở §3.8.2, điểm phạt của mỗi trường dựa trên khoảng cách chỉnh sửa của Định nghĩa 06.18 giữa hai giá trị, có hiệu chỉnh bằng các bảng công khai ghi những tên cùng chỉ một người, chẳng hạn tên gọi tắt Bill của William. Khóa trùng hoàn toàn chỉ tạo ứng viên; mức sai khác giữa hai chuỗi chỉ dùng ở bước chấm điểm.

![Ba bảng khóa Tên, Địa chỉ và Điện thoại cùng sinh cặp; ba tập cặp đi vào khối Hợp ứng viên, rồi vào khối Chấm điểm, xác minh.](img/lec-06/khoa-thuc-the.svg)

Hình đặt ba hàm khóa song song như ba dải; khối hợp ứng viên là phép khử lặp của bước 3 trong Thuật toán 06.4, khối chấm điểm là bước 4 với phép kiểm khác.

::: remark Nhận xét 06.40 (Hàm khóa cố định không cho cận xác suất)
Ba hàm khóa là cố định, không được chọn ngẫu nhiên từ một họ. Vì vậy không có phân phối để áp dụng Định nghĩa 06.22 hay Mệnh đề 06.26, và công thức $1-(1-p)^b$ không cho xác suất bỏ sót. Một cặp cùng người không trùng hoàn toàn trường nào thì bị bỏ sót chắc chắn. Ba trường của cùng một người cũng không độc lập: đổi địa chỉ thường đi kèm đổi điện thoại. Chất lượng của tập kết quả vì vậy phải đo gián tiếp; Tình huống 06.1 trình bày cách đo của MMDS bằng một trường không dùng khi chấm điểm.
:::

Bước chấm điểm thay bước xác minh bằng Jaccard của Mục 2, nên cần biết điểm được tính thế nào. Ví dụ sau dùng thang điểm của MMDS và khoảng cách chỉnh sửa của Mục 3.4.

::: example Ví dụ 06.17 (Thang điểm chấm và tên tương đương)
**Dữ kiện.** Theo MMDS §3.8.2 (tr.115–116), mỗi trường tên, địa chỉ, điện thoại được 100 điểm, nên hai hồ sơ trùng hoàn toàn cả ba trường được 300 điểm. Mỗi trường sai khác bị trừ điểm; mức trừ ban đầu dựa trên khoảng cách chỉnh sửa và tăng theo bình phương khoảng cách. Các bảng tên công khai sau đó giảm mức trừ: "Bill" và "William" được coi như chỉ khác một chữ cái.

**Tính.** Theo Mệnh đề 06.19, $d(x,y)=\lvert x\rvert+\lvert y\rvert-2L$. Chuỗi "Bill" dài 4, "William" dài 7, dãy con chung dài nhất là "ill" với $L=3$, nên $d=4+7-2\cdot3=5$.

**Kết luận.** Giả sử mức trừ ở một trường có dạng $c\,d^2$ với hằng $c$ mà sách không cho. Nếu "khác một chữ cái" được đọc là $d=1$, bảng tên tương đương thay $d=5$ bằng $1$ và giảm mức trừ ở trường tên $25$ lần. Theo Định nghĩa 06.18, thay một chữ cái cần một lần xóa và một lần chèn, tức $d=2$; khi đó mức trừ giảm $25/4$ lần. Riêng khoảng cách chỉnh sửa xếp Bill và William vào loại sai khác lớn, dù hai tên thường chỉ cùng một người.

**Kiểm tra lại.** Một dãy năm thao tác: xóa "B" được "ill", chèn "W" ở đầu được "Will", chèn "i", "a", "m" ở cuối được "William". Không có dãy con chung dài 4, vì chữ "B" không có trong "William"; vậy $L=3$ và $d=5$ là nhỏ nhất.
:::

::: exercise Bài tập 06.12
Dữ kiện: quy tắc ứng viên theo ba trường tên, địa chỉ, điện thoại (Định nghĩa 06.39). Hai hồ sơ có tên "Bob S. Jomes" và "Robert Jones Jr.", cùng địa chỉ, khác điện thoại.

Xác định cặp có thành ứng viên không, qua hàm khóa nào, và bước nào quyết định hai hồ sơ cùng người.
:::

::: hint
Khóa đòi trùng hoàn toàn; xét từng trường.
:::

::: solution
Tên không trùng hoàn toàn và điện thoại khác, nhưng địa chỉ trùng, nên cặp thành ứng viên qua khóa địa chỉ. Bước chấm điểm theo ba trường và ngưỡng điểm quyết định hai hồ sơ cùng người; trùng địa chỉ không đủ, vì nhiều người có thể chung một địa chỉ.

**Kiểm tra lại.** Nếu địa chỉ cũng khác, cặp không thành ứng viên dù tên gần giống, và bị bỏ sót theo Nhận xét 06.40.
:::

<!-- note-topic-id: lec-06-topic-12 -->
### 5.2 Đối sánh vân tay

Theo MMDS §3.8.4 (tr.117–118), một ảnh vân tay sau khi chuẩn hóa kích thước và hướng được biểu diễn bằng tập các ô của một lưới chứa điểm đặc trưng (minutia), tức vị trí một đường vân kết thúc hoặc hai đường vân nhập vào nhau. Hai tập ô có thể so bằng Jaccard, nhưng lưới chỉ khoảng 1000 ô nên tập đã nhỏ, và MMDS dùng một họ hàm khác thay cho việc rút gọn bằng MinHash. Có hai bài toán: một–nhiều, so một ảnh truy vấn với cả kho; nhiều–nhiều, tìm mọi cặp trong kho.

Một cách trực quan, hai ảnh của cùng một ngón có điểm đặc trưng ở gần như cùng các ô, nên nếu ta chọn trước vài ô, hai ảnh cùng ngón dễ cùng có đủ các ô ấy hơn hai ảnh khác ngón. Mô tả này chưa phải định nghĩa.

::: definition Định nghĩa 06.41 (Hàm ba ô cho vân tay)
Mỗi ảnh được biểu diễn bằng tập ô của lưới có điểm đặc trưng. Một **hàm ba ô** $f$ được xác định bởi ba ô chọn từ lưới trước khi xét ảnh. Mọi ảnh có điểm đặc trưng ở cả ba ô được đặt vào một **thùng chung**; mỗi ảnh thiếu ít nhất một trong ba ô được đặt vào một **thùng đơn** riêng của nó. Hai ảnh **va chạm** theo $f$ khi chúng cùng nằm trong thùng chung.
:::

Thùng đơn là điểm khác với bảng băm thông thường: nếu gom mọi ảnh thiếu ô vào một thùng, các ảnh ấy cũng va chạm và xác suất ở Mệnh đề 06.42 không còn đúng. Trong khung của Định nghĩa 06.1, cặp ảnh cùng ngón là cặp cần tìm, còn cặp ảnh khác ngón được nhận làm ứng viên là ứng viên giả.

![Lưới khái niệm với ba ô đánh dấu × được chọn từ lưới trước khi xét ảnh; ảnh có đủ ba ô đi vào thùng chung, ảnh thiếu ít nhất một ô đi vào thùng riêng.](img/lec-06/phep-thu-van-tay.svg)

Hình cho thấy ba ô được cố định trước, rồi mỗi ảnh được đưa vào thùng chung hay thùng riêng theo việc có đủ ba ô.

::: proposition Mệnh đề 06.42 (Xác suất va chạm của hàm ba ô)
**Giả thiết.** Theo mô hình của MMDS §3.8.5, mỗi ô của một ảnh có điểm đặc trưng với xác suất $0{,}2$, độc lập giữa các ô và giữa hai ảnh khác ngón. Với hai ảnh cùng ngón, nếu ảnh thứ nhất có điểm đặc trưng ở một ô thì ảnh thứ hai có ở ô đó với xác suất $0{,}8$, độc lập giữa các ô. Ba ô được chọn trước khi xét ảnh.

**Kết luận.** Hai ảnh khác ngón va chạm theo $f$ với xác suất $q_F=0{,}2^6=0{,}000064$; hai ảnh cùng ngón va chạm với xác suất $q_T=(0{,}2\cdot0{,}8)^3=0{,}004096$.

**Điều kiện áp dụng.** Xác suất lấy theo mô hình sinh ảnh, với ba ô cố định.

**Phạm vi.** Đây là xác suất cả hai ảnh có đủ ba ô; nó không điều kiện hóa việc ảnh truy vấn đã có sẵn ba ô. Các số thuộc mô hình, không phải số đo trên một hệ nhận dạng.
:::

::: proof Chứng minh Mệnh đề 06.42
**Bước 1 (một ô).** Với hai ảnh khác ngón, cả hai có điểm đặc trưng ở một ô với xác suất $0{,}2\cdot0{,}2=0{,}04$, do độc lập giữa hai ảnh. Với hai ảnh cùng ngón, xác suất là $0{,}2\cdot0{,}8=0{,}16$: ảnh thứ nhất có ô đó, rồi ảnh thứ hai có ô đó với xác suất có điều kiện $0{,}8$.

**Bước 2 (ba ô).** Theo Định nghĩa 06.41, hai ảnh va chạm khi cả hai có đủ ba ô. Các ô độc lập, nên $q_F=0{,}04^3=0{,}2^6=0{,}000064$ và $q_T=0{,}16^3=0{,}004096$. $\square$
:::

Mệnh đề 06.42 cho thấy một hàm ba ô nhận cặp cùng ngón với xác suất chỉ khoảng $1/244$, dù gấp $64$ lần cặp khác ngón; cần ghép nhiều hàm. Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ độc lập giữa các ô: nếu ba ô luôn cùng có hoặc cùng không có điểm đặc trưng, mỗi ảnh có đủ ba ô với xác suất $0{,}2$, nên hai ảnh khác ngón va chạm với xác suất $0{,}2\cdot0{,}2=0{,}04$ thay cho $0{,}000064$.
- Bỏ việc chọn ô trước khi xét ảnh: nếu ba ô được chọn trong các ô mà ảnh truy vấn đã có, ảnh truy vấn chắc chắn có đủ ba ô, và một ảnh cùng ngón va chạm với xác suất $0{,}8^3=0{,}512$ thay cho $0{,}004096$.

Bước 1 dùng mô hình một ô; Bước 2 dùng độc lập giữa các ô và việc ba ô cố định trước.

::: example Ví dụ 06.18 (Hai cấu trúc ghép cho vân tay)
**Dữ kiện.** Theo Ví dụ 3.23 của MMDS (tr.118–120), $q_F=0{,}000064$, $q_T=0{,}004096$ (Mệnh đề 06.42); các hàm ba ô được chọn độc lập.

**Giả thiết độc lập thêm.** Mệnh đề 06.26 cho xác suất theo cách chọn hàm khi cặp đối tượng cố định. Ở đây $q_F$, $q_T$ lấy theo mô hình sinh ảnh, và mọi hàm cùng xét một cặp ảnh, nên theo mô hình ấy các biến cố va chạm theo những hàm khác nhau không độc lập: một ảnh có nhiều điểm đặc trưng dễ va chạm theo nhiều hàm. MMDS tính như thể các biến cố va chạm theo các hàm khác nhau, và giữa hai nhóm của cấu trúc AND, là độc lập. Các số dưới đây dùng giả thiết thêm này; Tình huống 06.2 nêu hướng sai lệch của nó.

**OR 1024.** Dưới giả thiết độc lập thêm, cặp khác ngón được nhận với xác suất $1-(1-q_F)^{1024}\approx0{,}063436634$; cặp cùng ngón bị bỏ sót với xác suất $(1-q_T)^{1024}\approx0{,}014951892$.

**AND hai nhóm OR 1024.** Ghép đồng thời hai nhóm độc lập cho

$$
P_F=\bigl[1-(1-q_F)^{1024}\bigr]^2\approx0{,}004024207,\qquad P_{\rm miss}=1-\bigl[1-(1-q_T)^{1024}\bigr]^2\approx0{,}029680224.
$$

**Diễn giải.** Cấu trúc AND giảm xác suất nhận cặp khác ngón khoảng 16 lần, nhưng xác suất bỏ sót tăng gấp đôi. Hai cấu trúc dùng 1024 và 2048 hàm, nên đây chưa là so sánh cùng ngân sách; Bài tập 06.28 so OR 2048 với AND hai nhóm OR 1024.

**Kiểm tra lại.** $0{,}063436634^2\approx0{,}004024207$, khớp với $P_F$. Lấy $0{,}063^2=0{,}003969$ sẽ cho số khác, vì đã làm tròn trung gian.
:::

**Trong thực hành.** Các xác suất $0{,}2$ và $0{,}8$ là giả định của mô hình MMDS, không phải tần suất đo trên một cơ sở dữ liệu vân tay. Với một ảnh truy vấn, cấu trúc AND hai nhóm OR thực hiện bốn thao tác: hợp các mã ảnh trong những thùng chung phù hợp của nhóm thứ nhất, hợp tương tự ở nhóm thứ hai, lấy giao hai hợp, rồi so ảnh truy vấn với các ứng viên còn lại; phép so vân tay cuối cùng có chi phí riêng. Tình huống 06.2 dùng các số này cho bài toán một–nhiều.

::: exercise Bài tập 06.13
Dữ kiện: $q_F=0{,}000064$, $q_T=0{,}004096$ (Mệnh đề 06.42); các hàm ba ô chọn độc lập, và dùng giả thiết độc lập thêm của MMDS nêu ở Ví dụ 06.18.

Dùng OR 512 thay cho OR 1024. Tính xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón, rồi so với OR 1024 của Ví dụ 06.18.
:::

::: hint
Thế $b=512$ vào hai công thức của phép ghép ít nhất một; dùng $q_F$, $q_T$ chưa làm tròn.
:::

::: solution
$1-(1-0{,}000064)^{512}\approx0{,}0322$ và $(1-0{,}004096)^{512}\approx0{,}1223$. So với OR 1024 ($0{,}0634$ và $0{,}0150$), xác suất nhận cặp khác ngón giảm khoảng một nửa nhưng xác suất bỏ sót tăng khoảng tám lần.

**Kiểm tra lại.** $(1-q_T)^{1024}$ là bình phương của $(1-q_T)^{512}$: $0{,}1223^2\approx0{,}0150$.
:::

<!-- note-topic-id: lec-06-topic-13 -->
### 5.3 Bản tin gần trùng

Theo MMDS §3.8.6 (tr.120–121), một bản tin được đăng lại trên nhiều trang báo, mỗi trang bao quanh bằng quảng cáo và tiêu đề riêng. Cần tìm các cặp trang mang cùng văn bản gốc, khác với các cặp chỉ cùng chủ đề. Nếu dùng $k$-shingle ký tự (ghi chú Bài 05, Mục 3), phần quảng cáo đóng góp shingle ngang với phần bản tin và làm Jaccard phản ánh cả hai.

Một cách trực quan, văn xuôi của bản tin chứa nhiều từ rất thông dụng, còn quảng cáo thường là cụm ngắn ít từ như vậy; nếu chỉ lấy đặc trưng bắt đầu tại những từ đó, tập đặc trưng tập trung vào phần bản tin. Mô tả này chưa phải định nghĩa.

Ghi chú Bài 05, Mục 12 (MMDS §3.2.4, tr.80) đã giới thiệu shingle bắt đầu bằng từ dừng như một nội dung đọc thêm; định nghĩa được nhắc lại dưới đây để dùng cho bài toán bản tin.

::: definition Định nghĩa 06.43 (Từ dừng và shingle theo từ dừng)
**Từ dừng** (stop word) là từ xuất hiện rất thường xuyên trong ngôn ngữ, cho trước bằng một danh sách. **Shingle theo từ dừng** của một văn bản là một từ dừng cùng hai từ đứng ngay sau nó.
:::

Định nghĩa đổi bước biểu diễn của khung tìm cặp, còn MinHash, phân dải và xác minh giữ nguyên. Ví dụ sau dùng danh sách năm từ dừng của sách.

::: example Ví dụ 06.19 (Shingle theo từ dừng trên hai câu)
**Dữ kiện.** Theo Ví dụ 3.24 của MMDS (tr.120–121), từ dừng là I, that, you, for, your. Hai câu là "Buy Sudzo." và "I recommend that you buy Sudzo for your laundry."

**Tính.** Câu thứ nhất không có từ dừng nên không có shingle. Câu thứ hai cho bốn shingle xác định: "I recommend that", "that you buy", "you buy Sudzo", "for your laundry". Shingle bắt đầu bằng "your" có dạng "your laundry x", phụ thuộc từ $x$ đứng sau câu, chưa được cho.

**Kiểm tra lại.** Câu thứ hai có năm lần xuất hiện từ dừng (I, that, you, for, your), ứng với bốn shingle xác định và một shingle còn thiếu từ.
:::

Câu quảng cáo ngắn "Buy Sudzo." không đóng góp shingle nào, còn câu văn xuôi cùng nội dung quảng cáo đóng góp bốn shingle xác định. Quy tắc này ưu tiên chuỗi có dạng văn xuôi; nó không bảo đảm loại mọi quảng cáo, vì một câu quảng cáo dài vẫn chứa từ dừng.

::: exercise Bài tập 06.14
Dữ kiện: từ dừng I, that, you, for, your (Ví dụ 06.19). Liệt kê các shingle theo từ dừng có đủ hai từ theo sau trong câu "The report said that you should wait for your turn."
:::

::: hint
Chỉ bắt đầu shingle tại một từ trong danh sách từ dừng.
:::

::: solution
"that you should", "you should wait", "for your turn". Shingle bắt đầu bằng "your" chỉ có một từ theo sau trong câu nên chưa xác định. "The" và "report" không thuộc danh sách từ dừng của ví dụ.

**Kiểm tra lại.** Câu có bốn từ dừng (that, you, for, your), cho ba shingle đủ và một shingle thiếu.
:::

Như vậy, ba ứng dụng dùng lại khung của Mục 2–4 bằng cách đổi đúng một thành phần: đối sánh thực thể thay họ ngẫu nhiên bằng ba hàm khóa cố định (Định nghĩa 06.39), vân tay thay MinHash bằng hàm ba ô với xác suất tính được dưới một mô hình (Mệnh đề 06.42), bản tin thay cách tạo tập đặc trưng (Định nghĩa 06.43). Thùng, khử lặp và xác minh giữ nguyên trong cả ba. Tuy nhiên, Mục 5 mới mô tả cơ chế; chưa giải trọn một bài toán từ dữ liệu đến kết luận, và chưa đo hậu quả khi một giả thiết như tính ngẫu nhiên của hàm băm hay tính đẳng hướng của pháp tuyến không thỏa. Phần tình huống áp dụng dưới đây làm việc đó.

<!-- note-topic-id: lec-06-topic-19 -->
## Tình huống áp dụng và ứng dụng

Bốn tình huống dưới đây giải trọn bốn bài toán bằng công cụ của chương. Tình huống 06.2 dùng các kết quả của chương cùng giả thiết độc lập thêm của MMDS (Ví dụ 06.18). Tình huống 06.3 dùng mô hình MinHash lý tưởng của Định lý 06.7; hàm băm khi tính thực tế chỉ xấp xỉ mô hình này. Tình huống 06.1 và 06.4 là hai trường hợp giả thiết không thỏa, và nêu hậu quả.

::: application Tình huống 06.1 (Đối sánh hồ sơ hai nguồn và kiểm bằng trường ngày)
**Bài toán và dữ liệu.** Theo MMDS §3.8.2–3.8.3 (tr.115–117), hai nguồn A và B, mỗi nguồn khoảng $10^6$ hồ sơ có tên, địa chỉ, điện thoại và ngày tạo hồ sơ. Cần các cặp hồ sơ cùng một người và một ước lượng chất lượng của tập kết quả.

**Mô hình hóa.** Ba hàm khóa tên, địa chỉ, điện thoại tạo ứng viên theo Định nghĩa 06.39; mỗi trường là một dải với $r=1$, và hợp ba tập cặp là bước 3 của Thuật toán 06.4. Bước chấm điểm thay bước xác minh: điểm của một cặp là tổng điểm của ba trường, tối đa 300, trong đó điểm mỗi trường bị trừ theo điểm phạt dựa trên khoảng cách chỉnh sửa (Định nghĩa 06.18).

**Kiểm giả thiết.** Ba hàm khóa cố định, không chọn ngẫu nhiên, và các trường của một người không độc lập. Giả thiết của Định lý 06.7 và Mệnh đề 06.26 không thỏa, nên không có xác suất bỏ sót (Nhận xét 06.40). Trường ngày không tham gia tính điểm; điều này chưa có nghĩa nó độc lập thống kê với điểm.

**Áp dụng.** Độ trễ của một cặp là ngày tạo hồ sơ ở B trừ ngày tạo ở A, chỉ xét từ 0 đến 90 ngày. Với cặp ghép ngẫu nhiên, mô hình dùng độ trễ trung bình 45 ngày; một giả thiết đủ để có giá trị này là độ trễ ngẫu nhiên phân bố đều trên 0–90. Nhóm cặp đạt điểm tối đa 300 có độ trễ trung bình 10 ngày và được coi là các khớp đúng. Với một nhóm cặp cùng mức điểm có độ trễ trung bình $x$, gọi $f$ là tỷ phần khớp đúng. Coi nhóm là hỗn hợp hai thành phần: tỷ phần $f$ khớp đúng có độ trễ trung bình 10 ngày, tỷ phần $1-f$ ghép ngẫu nhiên có độ trễ trung bình 45 ngày. Độ trễ trung bình của cả nhóm khi đó là

$$
x=10f+45(1-f),\qquad f=\frac{45-x}{35}.
$$

**Chi phí.** So mọi cặp cần $10^{12}$ lần chấm điểm. Với ba hàm khóa, số cặp được chấm là số cặp chung ít nhất một khóa; theo Mệnh đề 06.11, số này phụ thuộc cỡ các nhóm cùng giá trị khóa, chẳng hạn một địa chỉ chung của nhiều hồ sơ, và mỗi lần chấm điểm còn tốn chi phí tính khoảng cách chỉnh sửa trên ba trường.

**Diễn giải.** Công thức ước lượng tỷ phần khớp đúng của cả một nhóm điểm, không xác nhận từng cặp. Một giá trị $x$ ngoài đoạn $[10,45]$ không tương thích với mô hình hai thành phần.

**Kết luận.** Theo khung "When Are Record Matches Good Enough?" của MMDS (tr.117), với các mức điểm từ 185 trở lên, $x$ rất gần 10, nên $f\approx1$. Mức 185 ứng với một trường trùng hoàn toàn, một trường khác hẳn và trường thứ ba sai khác nhỏ; các nhóm điểm này gần như chỉ gồm cặp cùng người. Ở mức 115, ứng với một trường trùng và hai trường chỉ giống nhẹ, $x$ nhỏ hơn 45 rõ rệt, nên $f>0$: một phần các cặp này cùng người. Sách không cho giá trị $x$ ở mức 115, nên tỷ phần $f$ tại đó không xác định được từ dữ kiện.

**Giới hạn.** Ước lượng cần hai nhóm tham chiếu đại diện cho thành phần thật và thành phần ngẫu nhiên. Cặp cùng người không trùng hoàn toàn trường nào bị bỏ sót, và trường ngày không đo được số cặp bỏ sót này, vì chúng không có mặt trong tập kết quả.

**Dẫn ngược lý thuyết.** Định nghĩa 06.39, Nhận xét 06.40 (giả thiết không thỏa), Thuật toán 06.4 (bước 2–3), Mệnh đề 06.11, Định nghĩa 06.18.
:::

::: application Tình huống 06.2 (Truy vấn vân tay một–nhiều)
**Bài toán và dữ liệu.** Theo MMDS §3.8.5 (tr.118–120), một ảnh vân tay truy vấn cần được so với một kho ảnh đã lưu; mỗi ảnh là tập ô có điểm đặc trưng.

**Mô hình hóa.** Mỗi hàm ba ô là một hàm của Định nghĩa 06.41. Hai cấu trúc được xét: OR 1024 hàm, và AND hai nhóm, mỗi nhóm OR 1024 hàm.

**Kiểm giả thiết.** Mô hình $0{,}2$ và $0{,}8$ với độc lập giữa các ô là giả thiết của Mệnh đề 06.42; ba ô của mỗi hàm được chọn trước khi xét ảnh; các hàm chọn độc lập. Mệnh đề 06.26 không cho phép nhân xác suất qua 1024 hàm và qua hai nhóm, vì $q_F$, $q_T$ lấy theo mô hình ảnh và mọi hàm xét chung một cặp ảnh; phép nhân dùng giả thiết độc lập thêm của MMDS (Ví dụ 06.18).

**Áp dụng.** Theo Ví dụ 06.18, một ảnh khác ngón thành ứng viên với xác suất khoảng $0{,}0634$ dưới OR 1024 và khoảng $0{,}004024$ dưới AND hai nhóm. Theo tuyến tính kỳ vọng (Kiến thức tiên quyết), đây cũng là tỷ phần kỳ vọng của các ảnh khác ngón trong kho phải so với ảnh truy vấn: khoảng $6{,}3\%$ và khoảng $1/250$. Xác suất bỏ sót ảnh cùng ngón là khoảng $0{,}0150$ và $0{,}0297$.

**Chi phí.** Với mỗi hàm, kiểm ảnh truy vấn có đủ ba ô hay không; nếu có, đọc thùng chung của hàm đó. Cấu trúc AND hợp mã ảnh trong các thùng của từng nhóm, lấy giao hai hợp, rồi so vân tay với các ứng viên còn lại. Hợp và giao chỉ xử lý mã ảnh; số phép so vân tay tỷ lệ với tỷ phần ở bước Áp dụng.

**Diễn giải.** Cấu trúc AND giảm số ảnh khác ngón phải so khoảng 16 lần, đổi lại xác suất bỏ sót tăng gấp đôi. Lựa chọn phụ thuộc chi phí của một phép so so với hậu quả của một lần bỏ sót.

**Giới hạn.** Hai cấu trúc dùng ngân sách 1024 và 2048 hàm. Với cấu trúc OR, giả thiết độc lập thêm làm lệch các số theo một chiều xác định. Với một cặp ảnh cùng ngón cố định, gọi $p$ là xác suất va chạm theo cách chọn ba ô; khi đó $q_T=\mathbb E[p]$, kỳ vọng lấy theo mô hình ảnh. Vì các hàm chọn độc lập, xác suất bỏ sót thật dưới OR 1024 là $\mathbb E[(1-p)^{1024}]$. Hàm $t\mapsto(1-t)^{1024}$ lồi trên $[0,1]$, nên theo bất đẳng thức Jensen $\mathbb E[(1-p)^{1024}]\ge(1-q_T)^{1024}$: số $0{,}0150$ của sách là cận dưới của xác suất bỏ sót. Tương tự, hàm $t\mapsto1-(1-t)^{1024}$ lõm, nên $0{,}0634$ là cận trên của xác suất nhận một ảnh khác ngón dưới OR 1024. Với AND hai nhóm, hàm $t\mapsto[1-(1-t)^{1024}]^2$ không lồi cũng không lõm trên $[0,1]$, nên bất đẳng thức Jensen không cho chiều sai lệch: hai số $0{,}004024$ và $0{,}0297$ dựa trên giả định độc lập, và không có bất đẳng thức một chiều.

**Dẫn ngược lý thuyết.** Định nghĩa 06.41, Mệnh đề 06.42, Mệnh đề 06.26, Ví dụ 06.18 (giả thiết độc lập thêm), tuyến tính kỳ vọng.
:::

::: application Tình huống 06.3 (Bản tin gần trùng)
**Bài toán và dữ liệu.** Theo MMDS §3.8.6 (tr.120–121), hai trang, mỗi trang gồm một nửa là bản tin và một nửa là quảng cáo. Cần nhận cặp trang cùng bản tin khác quảng cáo, và không nhận cặp cùng quảng cáo khác bản tin.

**Mô hình hóa.** Mỗi trang được biểu diễn bằng tập shingle theo từ dừng (Định nghĩa 06.43), sau đó lập chữ ký MinHash và chạy Thuật toán 06.4 như với mọi tập.

**Kiểm giả thiết.** Định lý 06.7 cần tập không rỗng và MinHash lý tưởng, tức hoán vị chọn đều và độc lập; hàm băm khi tính thực tế chỉ xấp xỉ mô hình này. Tập shingle của một trang có văn xuôi là không rỗng. Lập luận của MMDS giả định shingle theo từ dừng tập trung ở phần bản tin.

**Áp dụng.** Theo MMDS, với shingle theo từ dừng, cặp cùng bản tin khác quảng cáo có Jaccard khoảng $0{,}75$, còn cặp cùng quảng cáo khác bản tin chỉ khoảng $0{,}25$. Với shingle 10 ký tự liên tiếp, cả hai trường hợp đều cho khoảng $1/3$. Chọn $(b,r)=(20,5)$ của Ví dụ 3.12 (MMDS, tr.94–95), có $s_{1/2}\approx0{,}509$ nằm giữa $0{,}25$ và $0{,}75$. Vì $P_{20,5}$ tăng theo $s$, công thức (2.1) cho $P_{20,5}(0{,}25)\le P_{20,5}(0{,}3)=0{,}047494259$ và $P_{20,5}(0{,}75)\ge P_{20,5}(0{,}6)=0{,}801902454$: cặp cùng bản tin thành ứng viên với xác suất ít nhất khoảng $0{,}80$, cặp chỉ cùng quảng cáo với xác suất nhiều nhất khoảng $0{,}047$.

Với shingle 10 ký tự, cả hai loại cặp có Jaccard khoảng $1/3$, nên cả hai thành ứng viên với cùng một xác suất nằm giữa $P_{20,5}(0{,}3)=0{,}047494259$ và $P_{20,5}(0{,}4)=0{,}186049552$.

**Chi phí.** Tạo shingle cần một lượt đọc các từ của trang; chữ ký và phân dải tốn như Mục 2.

**Diễn giải.** Đổi biểu diễn làm hai loại cặp tách xa nhau trên trục Jaccard, nên đường xác suất của Mục 2.4 phân biệt được chúng. Với shingle ký tự, hai loại cặp có cùng Jaccard, nên mọi cấu hình $(b,r)$ cho chúng cùng xác suất thành ứng viên và không phân biệt được.

**Giới hạn.** Hai giá trị $0{,}75$ và $0{,}25$ là ước lượng của sách cho trang chia đôi; câu quảng cáo dài vẫn chứa từ dừng.

**Dẫn ngược lý thuyết.** Định nghĩa 06.43, Ví dụ 06.19, Định lý 06.7, Mệnh đề 06.9, Nhận xét 06.10, Thuật toán 06.4.
:::

::: application Tình huống 06.4 (Ước lượng góc bằng pháp tuyến có tọa độ $\pm1$)
**Bài toán và dữ liệu.** Theo MMDS §3.7.3 và Ví dụ 3.22 (tr.110–111), cần ước lượng góc giữa $x=(3,4,5,6)$ và $y=(4,3,2,1)$ bằng chữ ký dấu, với pháp tuyến có tọa độ $\pm1$; sách coi các vector này là đủ ngẫu nhiên, và tích vô hướng với chúng chỉ cần cộng, trừ.

**Mô hình hóa.** Chữ ký dấu và quy tắc $\widehat\theta=\pi\widehat p_{\ne}$ của Thuật toán 06.33.

**Kiểm giả thiết.** Thuật toán 06.33 và Định lý 06.32 cần pháp tuyến đẳng hướng. Vector $\pm1$ chọn đều trong 16 vector của $\mathbb R^4$ không đẳng hướng: chúng chỉ có 16 hướng. Giả thiết không thỏa.

**Áp dụng.** Với ba pháp tuyến của Ví dụ 06.15, $\widehat\theta=120^\circ$. Xét đủ 16 pháp tuyến với quy ước $\operatorname{sign}(0)=+1$, có 4 pháp tuyến cho hai dấu khác nhau, nên tỷ lệ khác dấu là $1/4$ và góc ước lượng là $45^\circ$. Góc thật là $\arccos(40/\sqrt{2580})\approx38{,}047579^\circ$.

**Chi phí.** Theo Mệnh đề 06.38, một hàm siêu phẳng tốn $D$ phép nhân; với tọa độ $\pm1$, các phép nhân thành phép đổi dấu, nên chỉ còn khoảng $D-1$ phép cộng hoặc trừ.

**Diễn giải.** Có hai nguồn sai. Ba bit cho một ước lượng thô: $120^\circ$ so với $45^\circ$ của toàn bộ 16 pháp tuyến. Phân phối không đẳng hướng tạo sai lệch không mất đi khi dùng hết các pháp tuyến: $45^\circ$ so với $38{,}05^\circ$.

**Giới hạn.** Tình huống chỉ đo sai lệch trên một cặp vector; nó không cho cận sai lệch chung của phân phối $\pm1$.

**Dẫn ngược lý thuyết.** Định nghĩa 06.31, Định lý 06.32 (giả thiết đẳng hướng bị vi phạm), Thuật toán 06.33, Ví dụ 06.15, Mệnh đề 06.38.
:::

**Ứng dụng trong các bài sau.**

- Bài 07 (Chỉ mục hàng xóm gần đúng) dùng LSH của chương này làm bộ lọc ứng viên cho truy vấn: vector truy vấn được băm bằng cùng các hàm, và chỉ các vector cùng thùng được đo khoảng cách. LSH được đặt trong bảng so sánh với đồ thị thế giới nhỏ phân tầng (Hierarchical Navigable Small World, HNSW) và lượng tử hóa tích (product quantization, PQ).
- Bài 3.4.4 của MMDS (tr.96) đặt việc phân dải trên MapReduce. Trong mô hình của Bài 02, hàm map phát các cặp khóa–giá trị và mọi giá trị cùng khóa được gom về một lần gọi reduce; khóa dải $(j,z)$ của Định nghĩa 06.3 có thể làm khóa, với mã tài liệu làm giá trị, để mỗi lần gọi reduce nhận đúng một thùng.

<!-- note-topic-id: lec-06-topic-14 -->
## Tóm tắt chương

Chương bắt đầu từ giới hạn của Bài 05: chữ ký MinHash làm kho một triệu tài liệu vừa bộ nhớ, nhưng số cặp vẫn là $499\,999\,500\,000$ (Ví dụ 06.1). Chúng ta tách bài toán thành bộ tạo ứng viên và bước xác minh (Định nghĩa 06.1), rồi dựng bộ tạo đầu tiên bằng phân dải chữ ký (Định nghĩa 06.3, Thuật toán 06.4), đúng trên tập ứng viên (Mệnh đề 06.5).

Một cặp có Jaccard $s$ được xét với xác suất $P_{b,r}(s)=1-(1-s^r)^b$ (Định lý 06.7), nên cặp đạt ngưỡng bị bỏ sót với xác suất $(1-s^r)^b$ (Hệ quả 06.8), và cách tách $n=br$ dời vùng chuyển tiếp của đường xác suất (Mệnh đề 06.9). Công việc là $O(nC+Q+\sum T_J)$ nhưng $K$ có thể bằng $\binom C2$ trong trường hợp xấu nhất (Mệnh đề 06.11, Nhận xét 06.12).

Chúng ta khái quát hóa tính chất của MinHash thành họ $(d_1,d_2,p_1,p_2)$-nhạy cảm (Định nghĩa 06.22), dựng hai phép ghép (Mệnh đề 06.26) và ba họ cơ sở theo Hamming, góc và khoảng cách Euclid (Mệnh đề 06.29, Định lý 06.32, Định lý 06.36). Ba ứng dụng chỉ đổi biểu diễn hoặc họ hàm, còn thùng và xác minh giữ nguyên.

Với kho một triệu tài liệu, giả định thêm rằng ngoài $N$ cặp gần, mọi cặp có $s\le0{,}1$. Với $(b,r)=(20,5)$, $P_{20,5}(0{,}1)\approx2\cdot10^{-4}$, nên theo Mệnh đề 06.13, không cần các cặp độc lập, $\mathbb E[K]\le N+10^8$ và $\mathbb E[Q]\le20N+10^8$. Với $1\,\mu\mathrm{s}$ mỗi lần so cặp và $N\ll10^8$, thời gian xác minh kỳ vọng không quá khoảng $100$ giây, so với khoảng $5{,}79$ ngày khi xét mọi cặp; không có giả định về phân bố tương đồng, trường hợp xấu nhất vẫn là $K=\binom C2$ (Nhận xét 06.12). Giới hạn còn lại là truy vấn hàng xóm gần trên vector: Bài 07 dùng LSH làm bộ lọc ứng viên cho truy vấn và so nó với đồ thị thế giới nhỏ phân tầng (HNSW) và lượng tử hóa tích (PQ).

**Định nghĩa và kết quả theo mục.**

- Mục 1: bài toán tìm cặp, bộ tạo ứng viên, ứng viên giả, cặp bỏ sót (Định nghĩa 06.1); $s$ và $\widehat s$ (Nhận xét 06.2).
- Mục 2: dải, khóa dải, tập ứng viên (Định nghĩa 06.3); Thuật toán 06.4; tính đúng (Mệnh đề 06.5); bước lọc theo $\widehat s$ (Nhận xét 06.6); xác suất thành ứng viên (Định lý 06.7); xác suất bỏ sót (Hệ quả 06.8); nghiệm một nửa (Mệnh đề 06.9); ba đại lượng ngưỡng (Nhận xét 06.10); chi phí (Mệnh đề 06.11); trường hợp xấu nhất (Nhận xét 06.12); kỳ vọng của $K$, $Q$ (Mệnh đề 06.13).
- Mục 3: độ đo khoảng cách, chuẩn $L_q$ (Định nghĩa 06.14); khoảng cách Jaccard (Mệnh đề 06.15); khoảng cách góc (Định nghĩa 06.16, Nhận xét 06.17); khoảng cách chỉnh sửa (Định nghĩa 06.18, Mệnh đề 06.19); Hamming (Định nghĩa 06.20, Nhận xét 06.21); họ nhạy cảm (Định nghĩa 06.22); họ MinHash (Hệ quả 06.23); bộ tham số là cận (Nhận xét 06.24); phép ghép (Định nghĩa 06.25, Mệnh đề 06.26); phân dải là AND rồi OR (Nhận xét 06.27).
- Mục 4: họ chọn tọa độ (Định nghĩa 06.28, Mệnh đề 06.29, Nhận xét 06.30); họ siêu phẳng (Định nghĩa 06.31, Định lý 06.32); chữ ký dấu (Thuật toán 06.33); họ chiếu có dịch (Định nghĩa 06.34, Bổ đề 06.35, Định lý 06.36, Nhận xét 06.37); chi phí chữ ký (Mệnh đề 06.38).
- Mục 5: hàm khóa (Định nghĩa 06.39, Nhận xét 06.40); hàm ba ô (Định nghĩa 06.41, Mệnh đề 06.42); shingle theo từ dừng (Định nghĩa 06.43).

**Công thức và thuật toán cần nhớ.** Xác suất thành ứng viên và nghiệm một nửa:

$$
P_{b,r}(s)=1-(1-s^r)^b,\qquad s_{1/2}=\bigl(1-2^{-1/b}\bigr)^{1/r}.
$$

Công việc của Thuật toán 06.4:

$$
Q=\sum_{j,z}\binom{u_{j,z}}2,\qquad K=\lvert\mathcal C\rvert\le Q,\qquad O\Bigl(nC+Q+\sum_{(c,d)\in\mathcal C}T_J(c,d)\Bigr).
$$

Phép ghép đồng thời bậc $r$ và ít nhất một bậc $b$ trên xác suất cơ sở $p$:

$$
p\mapsto p^r,\qquad p\mapsto1-(1-p)^b.
$$

Xác suất trùng của ba họ cơ sở và của hàm ba ô:

$$
1-\frac{d_H}{D},\qquad 1-\frac\theta\pi,\qquad \max\Bigl(0,1-\frac\ell a\Bigr),\qquad q_F=0{,}2^6,\quad q_T=(0{,}2\cdot0{,}8)^3.
$$

**Giả thiết hay bị bỏ quên.**

- Định lý 06.7 cần các MinHash chọn độc lập trong mỗi dải và giữa các dải. Dùng lại một hàm cho mọi hàng của một dải làm xác suất trùng dải là $s$ thay cho $s^r$; dùng lại cùng $r$ hàm cho mọi dải làm xác suất thành ứng viên là $s^r$ thay cho $P_{b,r}(s)$.
- Xác suất trong định nghĩa họ nhạy cảm lấy theo cách chọn hàm, với cùng một hàm cho hai đối tượng.
- $P_{b,r}(s)$ là xác suất theo cặp, không phải tỷ lệ lỗi của kho; $\widehat s$ không phải $s$.
- Kỳ vọng của $K$, $Q$ ở Mệnh đề 06.13 lấy theo cách chọn hoán vị, không phải chi phí xấu nhất; Nhận xét 06.12 cho $K=\binom C2$. Kỳ vọng ở Mệnh đề 06.11 chỉ lấy theo hàm băm của bảng.
- Định lý 06.32 cần pháp tuyến đẳng hướng và góc đo bằng radian; vector $\pm1$ không đẳng hướng (Tình huống 06.4).
- Cận $1/2$ của Định lý 06.36 cần dịch đều; cận $1/3$ chỉ được chứng minh trong hai chiều, cần hướng đều nhưng không cần dịch đều. Trục cố định không có bảo đảm.
- Hàm khóa cố định không cho xác suất bỏ sót (Nhận xét 06.40). Các số của mô hình vân tay là dự đoán của mô hình, dựa thêm vào giả thiết độc lập của MMDS; với cấu trúc OR, số bỏ sót của sách là cận dưới, còn với AND hai nhóm không có bất đẳng thức một chiều (Tình huống 06.2).
- Xác minh loại ứng viên giả nhưng không lấy lại cặp bỏ sót.

<!-- note-topic-id: lec-06-topic-16 -->
## Bài tập củng cố

Các bài tập trong các mục và mười sáu bài dưới đây là bộ bài tập của chương. Mục tiêu 1 được kiểm bởi Bài tập 06.2, 06.4, 06.17, 06.30; mục tiêu 2 bởi Bài tập 06.3, 06.16, 06.18, 06.20, 06.21, 06.29; mục tiêu 3 bởi Bài tập 06.6, 06.7, 06.15, 06.19, 06.22; mục tiêu 4 bởi Bài tập 06.8–06.11, 06.23–06.26; mục tiêu 5 bởi Bài tập 06.12–06.14, 06.27, 06.28. Bảy bài mang số bài sách (Bài tập 06.20–06.25 và 06.28) là bài của phần bài tập vận dụng trên lớp; Bài tập 06.26 là phần (d) của Bài 3.7.5, dành cho tự học. Máy tính được dùng cho lũy thừa và $\arccos$; không có yêu cầu viết chương trình.

### Mức nhận biết

::: exercise Bài tập 06.15
Dữ kiện: họ MinHash trên các tập hữu hạn, không rỗng với khoảng cách Jaccard (Hệ quả 06.23).

Viết bộ tham số của họ MinHash với $d_1=0{,}2$, $d_2=0{,}5$, rồi bộ tham số của họ sau phép ghép đồng thời bậc 2.
:::

::: hint
Hệ quả 06.23 cho $p_i=1-d_i$; phép ghép đồng thời giữ $d_1$, $d_2$ và bình phương hai mức xác suất.
:::

::: solution
Họ MinHash là $(0{,}2;\ 0{,}5;\ 0{,}8;\ 0{,}5)$-nhạy cảm. Với hai hàm độc lập, phép ghép đồng thời bậc 2 cho $(0{,}2;\ 0{,}5;\ 0{,}64;\ 0{,}25)$.

**Kiểm tra lại.** Hai ngưỡng khoảng cách không đổi khi ghép; $0{,}8^2=0{,}64$ và $0{,}5^2=0{,}25$.
:::

::: exercise Bài tập 06.16
Dữ kiện: phân dải với $b$ dải, $r$ hàng mỗi dải, $P_{b,r}(s)=1-(1-s^r)^b$ (Định lý 06.7).

Giữ $r$ và tăng $b$. Xác định ảnh hưởng tới số cặp bỏ sót và tới $K$.
:::

::: hint
Xét chiều biến thiên của $(1-s^r)^b$ theo $b$ với $s$ cố định trong $(0,1)$.
:::

::: solution
Với $0<s<1$, $0<1-s^r<1$ nên $(1-s^r)^b$ giảm khi $b$ tăng, và $P_{b,r}(s)$ tăng với mọi $s$. Mỗi cặp đạt ngưỡng có xác suất bỏ sót nhỏ hơn, nên kỳ vọng của số cặp bỏ sót giảm; mỗi cặp xa cũng có xác suất thành ứng viên lớn hơn, nên kỳ vọng của $K$ và của thời gian xác minh tăng; kỳ vọng của $Q$ cũng tăng vì có thêm dải (Mệnh đề 06.13). Độ dài chữ ký $n=br$ và chi phí lập chữ ký cũng tăng.

**Kiểm tra lại.** Tại $s=0{,}8$, $r=5$: $b=20$ cho xác suất bỏ sót $0{,}67232^{20}\approx0{,}000356$, nhỏ hơn $0{,}67232$ của $b=1$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 06.17
Dữ kiện: ma trận chữ ký có hai hàng $(2,1,2,0)$ và $(1,1,1,1)$ cho bốn tài liệu; $b=2$, $r=1$.

Tính $Q$, $K$ và nêu cặp được phát lặp.
:::

::: hint
Lập các thùng của từng dải; một thùng cỡ $u$ phát $\binom u2$ cặp.
:::

::: solution
Dải 1 có các thùng $\{1,3\}$ (giá trị 2), $\{2\}$, $\{4\}$; dải 2 có một thùng $\{1,2,3,4\}$ (giá trị 1). Do đó $Q=\binom22+\binom42=1+6=7$. Dải 2 đã phát đủ sáu cặp, nên $K=6$, và cặp $(1,3)$ được phát hai lần.

**Kiểm tra lại.** $Q-K=1$, đúng một lượt phát lặp.
:::

::: exercise Bài tập 06.18
Dữ kiện: phân dải với $b=10$, $r=4$ (Định lý 06.7, Nhận xét 06.10).

Tính ngưỡng xấp xỉ $(1/b)^{1/r}$ và xác suất thành ứng viên của cặp có $s=0{,}8$ và $s=0{,}3$.
:::

::: hint
Tính $s^4$ trước, rồi thế vào (2.1); làm tròn ở bước cuối.
:::

::: solution
$(1/10)^{1/4}=0{,}1^{1/4}\approx0{,}562$. Với $s=0{,}8$: $0{,}8^4=0{,}4096$ và $P=1-(1-0{,}4096)^{10}\approx0{,}9949$. Với $s=0{,}3$: $0{,}3^4=0{,}0081$ và $P=1-(1-0{,}0081)^{10}\approx0{,}0781$.

**Kiểm tra lại.** $0{,}562^4\approx0{,}0998$, gần $1/b=0{,}1$.
:::

::: exercise Bài tập 06.19
Dữ kiện: họ siêu phẳng với pháp tuyến đẳng hướng (Định lý 06.32); cặp gần là cặp có $\theta\le\pi/6$, cặp xa là cặp có $\theta\ge\pi/2$.

Tính $p_1$, $p_2$ và hai cận sau phép ghép AND 2 rồi OR 2.
:::

::: hint
Định lý 06.32 cho $p_i=1-d_i/\pi$; cấu trúc AND 2 rồi OR 2 là $F(p)=1-(1-p^2)^2$.
:::

::: solution
$p_1=1-1/6=5/6$ và $p_2=1-1/2=1/2$. Với $F(p)=1-(1-p^2)^2$: $F(5/6)\approx0{,}9066$ và $F(1/2)=1-(3/4)^2=0{,}4375$.

**Kiểm tra lại.** $(5/6)^2=25/36$, $1-25/36=11/36$, $(11/36)^2\approx0{,}0934$, nên $F(5/6)\approx0{,}9066$.
:::

::: exercise Bài tập 06.20 (Bài 3.4.1, MMDS §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$ (Định lý 06.7); ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$, viết theo thứ tự $(r,b)$ của đề sách.

Tính $P(s)$ cho $s=0{,}1;\ 0{,}2;\ \ldots;\ 0{,}9$ với cả ba cấu hình. Sản phẩm là bảng 27 xác suất.
:::

::: hint
Giữ thứ tự $(r,b)$ của đề. Tính $s^r$ trước, rồi $(1-s^r)^b$, và chỉ làm tròn kết quả cuối.
:::

::: solution
| $s$ | $r=3,b=10$ | $r=6,b=20$ | $r=5,b=50$ |
|---:|---:|---:|---:|
| 0,1 | 0,009955120 | 0,000020000 | 0,000499878 |
| 0,2 | 0,077180588 | 0,001279222 | 0,015875200 |
| 0,3 | 0,239448893 | 0,014479467 | 0,114539882 |
| 0,4 | 0,483870732 | 0,078809323 | 0,402283952 |
| 0,5 | 0,736924424 | 0,270187144 | 0,795550630 |
| 0,6 | 0,912267475 | 0,615414636 | 0,982533828 |
| 0,7 | 0,985015105 | 0,918185997 | 0,999898996 |
| 0,8 | 0,999234054 | 0,997712125 | 0,999999998 |
| 0,9 | 0,999997864 | 0,999999740 | xấp xỉ 1 |

Giá trị cuối bảng chỉ làm tròn về $1$, không bằng $1$ chính xác. Đổi chỗ $r$ và $b$ cho một hàm khác: chẳng hạn $(r,b)=(10,3)$ cho $P(0{,}5)=1-(1-2^{-10})^3\approx0{,}002927$, khác $0{,}736924424$ của $(3,10)$.

**Kiểm tra lại.** Tại $s=0{,}1$, $r=3$, $b=10$: $1-(1-0{,}001)^{10}\approx0{,}009955$.
:::

::: exercise Bài tập 06.21 (Bài 3.4.2, MMDS §3.4.4, tr.96)
Dữ kiện: xác suất thành ứng viên $P(s)=1-(1-s^r)^b$; ba cấu hình $(r,b)=(3,10)$, $(6,20)$, $(5,50)$ của Bài tập 06.20.

Với từng cấu hình, tìm $s$ để $P(s)=1/2$ và so với xấp xỉ $(1/b)^{1/r}$. Sản phẩm là phép biến đổi và bảng ba cặp ngưỡng.
:::

::: hint
Cô lập $(1-s^r)^b$ trước, rồi lấy căn bậc $b$ và căn bậc $r$ (Mệnh đề 06.9).
:::

::: solution
Biến đổi $1-(1-s^r)^b=1/2$ cho $s=(1-2^{-1/b})^{1/r}$.

| $(r,b)$ | Nghiệm chính xác | Xấp xỉ $(1/b)^{1/r}$ |
|---|---:|---:|
| $(3,10)$ | 0,406088134 | 0,464158883 |
| $(6,20)$ | 0,569353387 | 0,606962231 |
| $(5,50)$ | 0,424394480 | 0,457305052 |

Cả ba xấp xỉ lớn hơn nghiệm một nửa. Các nghiệm này là tính chất của cấu hình, không phải ngưỡng $t$ do bài toán đặt (Nhận xét 06.10).

**Kiểm tra lại.** Với $(3,10)$: $0{,}406088134^3\approx0{,}066967$, và $(1-0{,}066967)^{10}\approx0{,}5$.
:::

::: exercise Bài tập 06.22 (Bài 3.6.1(a–d), MMDS §3.6.4, tr.108)
Dữ kiện: $p$ là xác suất trùng của một MinHash cơ sở; mọi phép ghép dùng các bản thử độc lập (Mệnh đề 06.26).

Viết xác suất nhận cặp sau các chuỗi ghép, theo thứ tự từ trái sang phải:

- (a) AND 2 rồi OR 3.
- (b) OR 3 rồi AND 2.
- (c) AND 2, OR 2, AND 2.
- (d) OR 2, AND 2, OR 2, AND 2.

Sản phẩm là bốn biểu thức, có trạng thái trung gian cho từng tầng.
:::

::: hint
Mỗi tầng AND $k$ thay xác suất $q$ bằng $q^k$; mỗi tầng OR $k$ thay $q$ bằng $1-(1-q)^k$.
:::

::: solution
(a) $p\to p^2\to1-(1-p^2)^3$.

(b) $p\to1-(1-p)^3\to\bigl[1-(1-p)^3\bigr]^2$.

(c) $p\to p^2\to1-(1-p^2)^2\to\bigl[1-(1-p^2)^2\bigr]^2$.

(d) Đặt $q_1=1-(1-p)^2$, $q_2=q_1^2$, $q_3=1-(1-q_2)^2$; kết quả là $q_3^2$.

Mỗi tầng dùng các bản thử độc lập của tầng trước. Đảo thứ tự AND và OR nói chung làm đổi biểu thức, như (a) so với (b).

**Kiểm tra lại.** Tại $p=1$ cả bốn biểu thức bằng $1$; tại $p=0$ cả bốn bằng $0$.
:::

::: exercise Bài tập 06.23 (Bài 3.7.1, MMDS §3.7.6, tr.113)
Dữ kiện: họ gồm sáu hàm $h_i(x)=x_i$, $i=1,\ldots,6$ (Định nghĩa 06.28); bốn vector $\mathrm A=000000$, $\mathrm B=110011$, $\mathrm C=010101$, $\mathrm D=011100$.

Với mỗi cặp vector, xác định các hàm làm cặp đó thành ứng viên. Sản phẩm là sáu tập chỉ số cho các cặp AB, AC, AD, BC, BD, CD.
:::

::: hint
Đánh chỉ số từ 1. Hàm $h_i$ nhận cặp khi hai bit ở vị trí $i$ bằng nhau.
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

Số hàm nhận một cặp bằng $6$ trừ khoảng cách Hamming, nên cặp CD gần nhất được nhiều hàm nhận nhất, cặp BD xa nhất chỉ được một hàm nhận.

**Kiểm tra lại.** Ở mỗi hàng, số chỉ số cộng khoảng cách Hamming bằng $6$.
:::

::: exercise Bài tập 06.24 (Bài 3.7.2, MMDS §3.7.6, tr.113–114)
Dữ kiện: bốn pháp tuyến

$$
v_1=(1,1,1,-1),\quad v_2=(1,1,-1,1),\quad v_3=(1,-1,1,1),\quad v_4=(-1,1,1,1);
$$

ba vector $x=(2,3,4,5)$, $y=(-2,3,-4,5)$, $z=(2,-3,4,-5)$; quy ước $\operatorname{sign}(0)=+1$.

Tính chữ ký dấu của ba vector. Với mỗi cặp, tính góc ước lượng từ chữ ký (Thuật toán 06.33) và góc thật. Sản phẩm là bảng tích và dấu, và bảng ba cặp góc.
:::

::: hint
Tính bốn tích vô hướng trước khi lấy dấu. Góc ước lượng bằng $\pi$ nhân tỷ lệ bit khác; góc thật tính từ tích vô hướng của hai vector gốc.
:::

::: solution
| Vector | Tích với $(v_1,v_2,v_3,v_4)$ | Chữ ký |
|---|---|---|
| $x$ | $(4,6,8,10)$ | $(+,+,+,+)$ |
| $y$ | $(-8,10,-4,6)$ | $(-,+,-,+)$ |
| $z$ | $(8,-10,4,-6)$ | $(+,-,+,-)$ |

Bình phương ba chuẩn đều bằng $54$; $x\cdot y=14$, $x\cdot z=-14$, $y\cdot z=-54$.

| Cặp | Tỷ lệ khác dấu | Góc ước lượng | Góc thật |
|---|---:|---|---|
| $x,y$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(7/27)\approx74{,}973886^\circ$ |
| $x,z$ | $2/4$ | $\pi/2=90^\circ$ | $\arccos(-7/27)\approx105{,}026114^\circ$ |
| $y,z$ | $4/4$ | $\pi=180^\circ$ | $\pi=180^\circ$ |

Bốn pháp tuyến là dữ kiện cố định, không phải mẫu đẳng hướng, nên vết tính không bảo đảm góc ước lượng bằng góc thật (Tình huống 06.4).

**Kiểm tra lại.** $14/54=7/27$; $y=-z$ nên góc giữa $y$ và $z$ bằng $\pi$.
:::

::: exercise Bài tập 06.25 (Bài 3.7.5(a–c), MMDS §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ (sách ký hiệu $p_1,p_2,p_3$). Ba hàm là phép chiếu lên ba trục tọa độ; các khoảng có dạng $[ka,(k+1)a)$ với $k\in\mathbb Z$ (sách viết chỉ số là $j$; chương này dành $j$ cho số dải), không dịch biên.

- (a) Gán thùng với $a=1$.
- (b) Lặp lại với $a=2$.
- (c) Tìm các cặp ứng viên trong mỗi trường hợp.

Sản phẩm là hai bảng mã theo trục và hai tập cặp.
:::

::: hint
Mã của một điểm ở trục $i$ là $\lfloor x_i/a\rfloor$. Chỉ so mã trong cùng trục; số trục là một phần của khóa, như số dải ở Định nghĩa 06.3.
:::

::: solution
| $a$ | Mã của $z_1$ theo ba trục | Mã của $z_2$ | Mã của $z_3$ | Tập cặp |
|---:|---|---|---|---|
| 1 | $(1,2,3)$ | $(0,2,4)$ | $(4,3,2)$ | $\{(1,2)\}$ |
| 2 | $(0,1,1)$ | $(0,1,2)$ | $(2,1,1)$ | $\{(1,2),(1,3),(2,3)\}$ |

Với $a=1$, chỉ $z_1$, $z_2$ trùng ở trục 2. Với $a=2$, cặp $(1,2)$ trùng ở trục 1 và trục 2; cặp $(1,3)$ trùng ở trục 2 và trục 3; cặp $(2,3)$ trùng ở trục 2. Hợp các cặp theo trục và khử lặp cho tập kết quả.

**Kiểm tra lại.** Một tọa độ bằng $a$ thuộc $[a,2a)$, không thuộc $[0,a)$: tọa độ $2$ với $a=2$ có mã $1$.
:::

::: exercise Bài tập 06.26 (Bài 3.7.5(d), MMDS §3.7.6, tr.114)
Dữ kiện: ba điểm $z_1=(1,2,3)$, $z_2=(0,2,4)$, $z_3=(4,3,2)$ và ba phép chiếu lên ba trục tọa độ như Bài tập 06.25; độ rộng $a>0$ tùy ý, khoảng nửa mở $[ka,(k+1)a)$, $k\in\mathbb Z$, không dịch biên.

Với mỗi cặp điểm, tìm mọi giá trị $a$ làm cặp đó thành ứng viên.
:::

::: hint
Hai số $\alpha<\beta$ không âm cùng mã khi $\lfloor\alpha/a\rfloor=\lfloor\beta/a\rfloor$. Xét riêng giá trị mã chung bằng $0$ và bằng một số nguyên $k\ge1$.
:::

::: solution
**Cặp $(1,2)$.** Hai điểm có cùng tọa độ thứ hai, bằng $2$, nên luôn chung thùng ở trục 2: ứng viên với mọi $a>0$.

**Cặp $(1,3)$ và $(2,3)$ ở trục 2.** Hai tọa độ là $2$ và $3$. Mã chung bằng $0$ khi $a>3$. Mã chung bằng một số nguyên $k\ge1$ khi đồng thời $ka\le2$ và $3<(k+1)a$, tức

$$
\frac3{k+1}<a\le\frac2k .
$$

Khoảng này khác rỗng chỉ khi $3k<2(k+1)$, tức $k<2$, nên chỉ $k=1$ và $a\in(3/2,2]$.

**Các trục còn lại.** Ở trục 1, cặp $(1,3)$ có tọa độ $1$ và $4$, cặp $(2,3)$ có $0$ và $4$; ở trục 3, cặp $(2,3)$ có $4$ và $2$. Mỗi trường hợp chỉ trùng mã khi $a>4$, đã nằm trong $(3,\infty)$. Ở trục 3, cặp $(1,3)$ có tọa độ $3$ và $2$, lặp lại điều kiện của trục 2.

**Kết luận.** Mỗi cặp $(1,3)$, $(2,3)$ là ứng viên đúng khi

$$
a\in(3/2,2]\cup(3,\infty).
$$

**Kiểm tra lại.** Tại $a=3/2$, $\lfloor3/1{,}5\rfloor=2\ne\lfloor2/1{,}5\rfloor=1$; tại $a=3$, $\lfloor3/3\rfloor=1\ne\lfloor2/3\rfloor=0$; tại $a=2$, hai tọa độ $2$ và $3$ cùng mã $1$. Quy tắc nửa mở quyết định các dấu đóng, mở này.
:::

### Mức vận dụng

::: exercise Bài tập 06.27
Dữ kiện: kho $C$ ảnh, mỗi ảnh một vector đặc trưng thực 128 chiều; cần tìm các cặp ảnh có góc nhỏ.

Chọn họ cơ sở trong Mục 4 và nêu chi phí tính chữ ký $m$ bit.
:::

::: hint
Xác định độ đo của bài toán trước, rồi dùng Mệnh đề 06.38.
:::

::: solution
Dùng họ siêu phẳng (Định lý 06.32), vì độ đo là góc và chỉ phụ thuộc hướng. Theo Mệnh đề 06.38 với $D=128$, tính chữ ký cần $C\cdot m\cdot128$ phép nhân, tức $O(CmD)$; mỗi ảnh lưu $m$ bit, và các pháp tuyến cần $128m$ số. Dựng thùng, phát cặp và xác minh được tính thêm theo Mệnh đề 06.11.

**Kiểm tra lại.** Họ chọn tọa độ dùng cho Hamming trên vector rời rạc, còn họ chiếu có dịch đo khoảng cách Euclid, phụ thuộc cả độ dài; cả hai không đo đúng góc.
:::

::: exercise Bài tập 06.28 (Bài 3.8.2(a,b), MMDS §3.8.7, tr.121)
Dữ kiện: mỗi ô có điểm đặc trưng với xác suất $0{,}2$; với hai ảnh cùng ngón, ảnh thứ hai có điểm đặc trưng tại một ô đã có ở ảnh thứ nhất với xác suất $0{,}8$; mỗi hàm chọn ba ô từ lưới trước khi xét ảnh; các hàm độc lập theo mô hình (Mệnh đề 06.42). Gọi $F_1$ là OR 1024 hàm và $F_2$ là OR 2048 hàm.

- (a) Tính xác suất nhận cặp khác ngón và xác suất bỏ sót cặp cùng ngón của $F_2$.
- (b) So với cấu trúc AND hai nhóm $F_1$ độc lập.

Sản phẩm là bảng hai xác suất cho hai cấu trúc cùng 2048 hàm.
:::

::: hint
Tính $q_F$ và $q_T$ từ mô hình một ô rồi ba ô. Với cặp cùng ngón, bỏ sót là biến cố bù của được nhận. Không dùng các giá trị đã làm tròn như $0{,}063$ làm đầu vào ghép tiếp.
:::

::: solution
Xác suất cơ sở là $q_F=0{,}2^6=0{,}000064$ và $q_T=(0{,}2\cdot0{,}8)^3=0{,}004096$.

| Cấu trúc | Nhận cặp khác ngón | Bỏ sót cặp cùng ngón |
|---|---:|---:|
| $F_2$: OR 2048 | $1-(1-q_F)^{2048}\approx0{,}122849062$ | $(1-q_T)^{2048}\approx0{,}000223559$ |
| AND hai nhóm $F_1$ | $\bigl[1-(1-q_F)^{1024}\bigr]^2\approx0{,}004024207$ | $1-\bigl[1-(1-q_T)^{1024}\bigr]^2\approx0{,}029680224$ |

OR 2048 giảm bỏ sót nhưng nhận nhiều cặp khác ngón hơn. AND hai nhóm OR 1024 giảm ứng viên giả và tăng bỏ sót. Hai phương án cùng ngân sách 2048 hàm, nên khác biệt đến từ cấu trúc ghép. Các xác suất trên là xác suất cả hai ảnh có đủ ba ô, không phải xác suất có điều kiện khi ảnh truy vấn đã có ba ô (Mệnh đề 06.42).

Các phép nhân qua 1024 hoặc 2048 hàm dùng giả thiết độc lập thêm của MMDS (Ví dụ 06.18), không suy ra từ Mệnh đề 06.26. Với $p$ là xác suất va chạm của một cặp ảnh cùng ngón cố định theo cách chọn ba ô, $q_T=\mathbb E[p]$ và xác suất bỏ sót thật của $F_2$ là $\mathbb E[(1-p)^{2048}]$. Hàm $t\mapsto(1-t)^{2048}$ lồi, nên theo bất đẳng thức Jensen xác suất này ít nhất $(1-q_T)^{2048}\approx0{,}000223559$: số bỏ sót của $F_2$ trong bảng là cận dưới. Với AND hai nhóm $F_1$, hàm $t\mapsto1-[1-(1-t)^{1024}]^2$ không lồi cũng không lõm, nên số $0{,}029680224$ dựa trên giả định độc lập và không có bất đẳng thức một chiều.

**Kiểm tra lại.** $(1-q_T)^{2048}$ là bình phương của $(1-q_T)^{1024}\approx0{,}014951892$, và $0{,}014951892^2\approx0{,}000223559$.
:::

::: exercise Bài tập 06.29
Dữ kiện: chữ ký dài $n=100$; bốn cấu hình $(b,r)\in\{(50,2),(25,4),(20,5),(10,10)\}$, đều có $br=100$; ngưỡng $t=0{,}6$; bài toán ưu tiên tránh bỏ sót các cặp đạt ngưỡng.

(a) Tính $s_{1/2}$ theo (2.2) và xấp xỉ $(1/b)^{1/r}$ cho bốn cấu hình.

(b) Theo quy tắc của Nhận xét 06.10, giữ các cấu hình có $(1/b)^{1/r}<t$; trong số đó chọn cấu hình có $P_{b,r}(0{,}3)$ nhỏ nhất, với $s=0{,}3$ là cặp xa đại diện như Ví dụ 06.5.

(c) Với cấu hình được chọn, tính xác suất bỏ sót một cặp có $s=0{,}7$.
:::

::: hint
Câu (b) cần $P_{b,r}(0{,}3)=1-(1-0{,}3^r)^b$ cho các cấu hình còn lại sau bước lọc. Câu (c) dùng Hệ quả 06.8.
:::

::: solution
(a)

| $(b,r)$ | $s_{1/2}$ | $(1/b)^{1/r}$ | $P_{b,r}(0{,}3)$ |
|---|---:|---:|---:|
| $(50,2)$ | 0,117334119 | 0,141421356 | 0,991044917 |
| $(25,4)$ | 0,406648983 | 0,447213595 | 0,183986664 |
| $(20,5)$ | 0,508695962 | 0,549280272 | 0,047494259 |
| $(10,10)$ | 0,763108147 | 0,794328235 | 0,000059047 |

(b) Ba cấu hình đầu có $(1/b)^{1/r}<0{,}6$; cấu hình $(10,10)$ bị loại vì vùng chuyển tiếp nằm trên $t$. Trong ba cấu hình còn lại, $(20,5)$ có $P_{b,r}(0{,}3)$ nhỏ nhất, nên được chọn.

(c) Theo Hệ quả 06.8, xác suất bỏ sót là $(1-0{,}7^5)^{20}=(1-0{,}16807)^{20}=0{,}83193^{20}\approx0{,}025219456$.

**Kiểm tra lại.** Cấu hình bị loại $(10,10)$ bỏ sót cặp $s=0{,}7$ với xác suất $(1-0{,}7^{10})^{10}\approx0{,}750855826$, lớn hơn nhiều so với $0{,}025$; điều này khớp với việc nó đặt vùng chuyển tiếp trên $t$.
:::

::: exercise Bài tập 06.30
Dữ kiện: một biến thể của Thuật toán 06.4 dùng $b$ bảng băm $B_1,\ldots,B_b$ so khóa đầy đủ. Ở bước 2, cột $c$ của dải $j$ được nối vào danh sách $B_j[z_{j,c}]$, với khóa chỉ là tuple; bước 3 duyệt mọi danh sách của mọi bảng. Ma trận chữ ký có $n=4$, $b=2$, $r=2$ và ba cột, mỗi cột viết từ hàng 1 đến hàng 4: cột 1 là $(1,2,3,4)$, cột 2 là $(3,4,1,2)$, cột 3 là $(1,2,5,6)$.

(a) Chứng minh tập $\mathrm{CAND}$ của biến thể bằng tập ứng viên $\mathcal C$ của Định nghĩa 06.3.

(b) Tính $\mathcal C$, tập $\mathrm{CAND}$ của biến thể, và tập $\mathrm{CAND}$ khi dùng một bảng duy nhất với khóa chỉ là tuple.
:::

::: hint
Câu (a) lặp lại bất biến của chứng minh Mệnh đề 06.5 cho từng bảng $B_j$; số dải nằm ở việc chọn bảng thay vì nằm trong khóa. Câu (b) viết hai tuple của mỗi cột trước khi dựng thùng.
:::

::: solution
(a) Bảng $B_j$ chỉ nhận các lượt chèn của dải $j$. Áp dụng bất biến của Bước 1 và Bước 2 trong chứng minh Mệnh đề 06.5 cho riêng $B_j$: khi bước 2 kết thúc, danh sách $B_j[z]$ là đúng tập $\{c:\ z_{j,c}=z\}$. Do đó $c$, $d$ chung một danh sách của $B_j$ khi và chỉ khi $z_{j,c}=z_{j,d}$, tức $k_{j,c}=k_{j,d}$. Bước 3 thêm $(c,d)$ vào $\mathrm{CAND}$ khi và chỉ khi tồn tại $j$ để $c$, $d$ chung một danh sách của $B_j$, tức tồn tại $j$ với $k_{j,c}=k_{j,d}$. Theo Định nghĩa 06.3, $\mathrm{CAND}=\mathcal C$. $\square$

(b) Tuple ở dải 1 là $(1,2)$, $(3,4)$, $(1,2)$ cho ba cột; ở dải 2 là $(3,4)$, $(1,2)$, $(5,6)$. Chỉ cột 1 và cột 3 trùng một dải, nên $\mathcal C=\{(1,3)\}$.

| Cách tổ chức | Danh sách có ít nhất hai cột | $\mathrm{CAND}$ |
|---|---|---|
| $b$ bảng | $B_1[(1,2)]=[1,3]$ | $\{(1,3)\}$ |
| Một bảng, khóa chỉ là tuple | $[(1,2)]=[1,3,2]$; $[(3,4)]=[2,1]$ | $\{(1,2),(1,3),(2,3)\}$ |

Với một bảng có khóa chỉ là tuple, tuple $(1,2)$ của cột 2 ở dải 2 rơi vào danh sách của cột 1 và cột 3 ở dải 1, và tuple $(3,4)$ của cột 1 ở dải 2 rơi vào danh sách của cột 2 ở dải 1. Hai cặp $(1,2)$ và $(2,3)$ được phát dù không trùng dải nào: $\mathrm{CAND}\ne\mathcal C$.

**Kiểm tra lại.** Cặp $(1,2)$ so dải 1: $(1,2)\ne(3,4)$; dải 2: $(3,4)\ne(1,2)$. Cặp $(2,3)$ so dải 1: $(3,4)\ne(1,2)$; dải 2: $(1,2)\ne(5,6)$. Cả hai không thuộc $\mathcal C$.
:::

<!-- note-topic-id: lec-06-topic-15 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, Chương 3. Ví dụ 3.8, tr.85–86: dữ kiện bốn tập đặc trưng. §3.4, tr.91–96: Mục 1 và Mục 2. §3.5, tr.96–103: Mục 3.1–3.5. §3.6, tr.103–108: Mục 3.6–3.7. §3.7, tr.108–114: Mục 4. §3.8, tr.114–122: Mục 5 và các tình huống áp dụng. Bài tập 06.20–06.26 và 06.28 lấy từ §§3.4.4, 3.6.4, 3.7.6, 3.8.7. Sách và bộ trang chiếu của các tác giả tại [http://www.mmds.org](http://www.mmds.org); phần lớn sườn, ví dụ và bài tập của chương dựa trên nguồn này.
- Leskovec, J. (2026). Stanford CS246, [LSH I](https://web.stanford.edu/class/cs246/slides/03-lsh.pdf) và [LSH II](https://web.stanford.edu/class/cs246/slides/04-lsh_theory.pdf). Đối chiếu phân dải, phép ghép và hình học pháp tuyến của Mục 4.2; hình trong ghi chú được vẽ lại.
- Datar, M., Immorlica, N., Indyk, P. và Mirrokni, V. S. (2004). [*Locality-Sensitive Hashing Scheme Based on p-Stable Distributions*](https://people.csail.mit.edu/nickle/pubs/pstable.pdf), SoCG 2004, §3.2. Cơ chế dịch đều của Định nghĩa 06.34 và Bổ đề 06.35. Bộ tham số $(a/2,2a,1/2,1/3)$ và lập luận góc của Định lý 06.36 theo MMDS §3.7.4 (tr.111–113); ghi chú viết đủ các bước và thêm độ dịch đều cho cận gần. Phân phối ổn định không thuộc chương này.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press, §2.1. Cách phát biểu bất biến vòng lặp với ba phần khởi tạo, duy trì, kết thúc, dùng cho chứng minh Mệnh đề 06.5.
- Đọc tiếp, không là tiên quyết của bài tập: Bài 3.4.4 của MMDS (tr.96) về tổ chức phân dải trên MapReduce; Ví dụ 3.21 (tr.108) về phép ghép 256 hàm; Bài 3.6.2–3.6.4 (tr.108) về điểm bất động và độ dốc của các hàm ghép; §3.7.5 (tr.113) về mở rộng định tính của họ chiếu sang nhiều chiều.
- Ghi chú Bài 05, *Biểu diễn tương đồng: Shingling và MinHash*, Mục 2–3, 5–7, 9 và 11: các kết quả nhắc lại ở phần kiến thức tiên quyết.
