# Bài 01 — Bài toán dữ liệu lớn và mô hình thuật toán

Chúng ta đặt các bài toán của học phần vào một khung chung: đầu vào, đầu ra phải trả, tài nguyên bị giới hạn và mức chính xác phải bảo đảm. Bài toán tìm cặp tài liệu gần trùng được phân tích trọn vẹn trong khung đó, từ đặc tả, thuật toán xét mọi cặp và chứng minh tính đúng tới phép đếm chi phí. Trong mô hình hồ sơ lưu trú (phần đọc thêm), ta tính kỳ vọng số mẫu trùng xuất hiện chỉ do ngẫu nhiên.

[Bộ trang chiếu Bài 01](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html) trình bày cùng chủ đề; [tệp bài tập Bài 01](material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Nêu đầu vào, đầu ra và tài nguyên bị giới hạn của một bài toán dữ liệu; tính số khối của một tệp và số lần truyền khối của các lượt quét (Mục 1, Mục 2).
2. Đặc tả bài toán tìm cặp tài liệu gần trùng bằng độ tương đồng Jaccard và chứng minh thuật toán xét mọi cặp trả đúng tập $R$, mỗi cặp một lần (Mục 3.1–3.3).
3. Đếm chi phí của thuật toán xét mọi cặp; chứng minh bước xác minh tập ứng viên $A$ trả đúng $R$ khi và chỉ khi $R\subseteq A$ (Mục 3.4–3.5).
4. Gắn mỗi giới hạn tài nguyên đã gặp với một nhóm Bài 02–15 và với kiến thức nền cần ôn (Mục 4).

Phần đọc thêm: tính kỳ vọng số biến cố trùng ngẫu nhiên, chỉ ra chỗ dùng tính độc lập và chỗ dùng tính tuyến tính của kỳ vọng, chặn $\Pr(X\ge1)$ bằng bất đẳng thức Markov.

## Kiến thức tiên quyết

Các kiến thức dưới đây thuộc học phần tiên quyết UET.CS1058 (Cấu trúc dữ liệu và giải thuật) và các học phần toán.

- **Đếm cặp** (Toán rời rạc). Một tập $N$ phần tử có $\binom N2=N(N-1)/2$ cặp không thứ tự; khi $N<2$ số này bằng 0.
- **Tập hữu hạn** (Toán rời rạc). Với hai tập hữu hạn $C,C'$, giao $C\cap C'$ gồm các phần tử chung, hợp $C\cup C'$ đếm mỗi phần tử một lần, và $|C\cup C'|=|C|+|C'|-|C\cap C'|$.
- **Mô hình RAM và ký hiệu $O$** (UET.CS1058). Thuật toán đọc dữ liệu trong bộ nhớ truy cập ngẫu nhiên, mỗi phép toán cơ bản tốn một đơn vị; $g(x)=O(f(x))$ khi có hằng $c_0>0$ và $x_0$ sao cho $g(x)\le c_0f(x)$ với mọi $x\ge x_0$.
- **Danh sách đã sắp** (UET.CS1058). Một tập hữu hạn trên một tập có thứ tự toàn phần được lưu thành danh sách tăng ngặt, không có phần tử lặp.
- **Bất biến vòng lặp** (CLRS 4e, §2.1). Một mệnh đề đúng trước vòng đầu (khởi tạo), được giữ qua mỗi vòng (duy trì) và khi vòng lặp dừng cho điều cần chứng minh (kết thúc).
- **Bảng băm** (UET.CS1058). Hàm băm đưa khóa về một chỉ số thùng; phần tử có khóa $x$ nằm trong thùng mang chỉ số của $x$.
- **Xác suất rời rạc** (Xác suất thống kê). Nếu hai biến cố độc lập thì xác suất cả hai xảy ra bằng tích hai xác suất; biến chỉ báo $\mathbb 1_e$ bằng 1 khi $e$ xảy ra và bằng 0 khi không, nên $\mathbb E[\mathbb 1_e]=\Pr(e)$; kỳ vọng của một tổng bằng tổng các kỳ vọng, kể cả khi các số hạng không độc lập.

## Bảng ký hiệu

Các ký hiệu dưới đây dùng xuyên suốt chương; chữ chỉ dùng trong một mục hoặc một chứng minh được giới thiệu tại chỗ. Mỗi chữ trong bảng giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $N$ | số tài liệu của kho | số nguyên, $N\ge0$ |
| $C_i$ | tập đoạn ký tự của tài liệu thứ $i$ | tập hữu hạn, không rỗng |
| $C,C'$ | hai tập bất kỳ khi phát biểu một tính chất chung | tập hữu hạn |
| $\mathrm{SIM}(C,C')$ | độ tương đồng Jaccard $\lvert C\cap C'\rvert/\lvert C\cup C'\rvert$ | $[0,1]$, cần $C\cup C'\ne\varnothing$ |
| $\tau$ | ngưỡng tương đồng | $[0,1]$ |
| $a$; $c$ | tử số và mẫu số khi ngưỡng hữu tỷ, $\tau=a/c$ | số nguyên, $0\le a\le c$, $c>0$ |
| $(i,j)$ | một cặp tài liệu | $1\le i<j\le N$ |
| $R$ | tập mọi cặp đạt ngưỡng | tập con của các cặp $(i,j)$ |
| $L$ | số phần tử lớn nhất của một tập $C_i$ | số nguyên dương |
| $A$; $\widehat R$ | tập cặp ứng viên; tập cặp trả về sau xác minh | tập con của các cặp $(i,j)$ |
| $F$ | số khối của một tệp | số nguyên dương |
| $m$ | số lượt quét | số nguyên dương |
| $M$ | số khối bộ nhớ chính khả dụng | số nguyên dương |
| $n_r$; $b_r$ | số bản ghi; số khối của bảng $r$ khi nối bảng | số nguyên dương |
| $h$; $B$ | hàm băm; số thùng | $h(x)\in\{0,1,\ldots,B-1\}$ |
| $n$; $D$ | số véc-tơ của kho; số chiều | số nguyên dương |
| $\mathbf y$; $d(\cdot,\cdot)$ | véc-tơ truy vấn; hàm khoảng cách | $\mathbb R^D$; $d:\mathbb R^D\times\mathbb R^D\to[0,\infty)$ |
| $k$ | số hàng xóm phải trả | $1\le k\le n$ |
| $\mathcal N_k(\mathbf y)$; $\widehat{\mathcal N}_k(\mathbf y)$ | tập $k$ hàng xóm gần nhất chính xác; tập $k$ véc-tơ do một phương pháp trả về | tập $k$ định danh |
| $\operatorname{recall@}k$ | độ thu hồi tại $k$ | $[0,1]$ |
| $P$; $T$; $H$ | số người; số ngày quan sát; số khách sạn (phần đọc thêm) | số nguyên dương |
| $u,v$; $s,t$ | hai người; hai ngày khác nhau (phần đọc thêm) | |
| $q$; $p$ | xác suất một người lưu trú trong một ngày; xác suất một cặp người trùng khách sạn trong một ngày cho trước (phần đọc thêm) | $[0,1]$ |
| $X$; $\mathbb 1_e$ | số biến cố trùng; biến chỉ báo của biến cố $e$ (phần đọc thêm) | số nguyên không âm; $\{0,1\}$ |
| $\lambda$ | ngưỡng trong bất đẳng thức Markov (phần đọc thêm) | số thực dương |
| $\mathbb E$; $\Pr$ | kỳ vọng; xác suất | |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $0{,}01$; số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $65\,536$.
- Dung lượng tính bằng byte; 1 GB $=10^9$ byte, 1 TB $=10^{12}$ byte; một khối có $65\,536=2^{16}$ byte, cỡ khối mà MMDS dùng làm ví dụ (§1.3.4).
- $F$ và $M$ luôn tính bằng khối, không tính bằng byte.
- Bài 05–06 viết ngưỡng là $t$; ở đây ta viết $\tau$ vì $t$ chỉ một ngày trong phần đọc thêm. Bài 07 viết $N$, $K$, $q$ cho số véc-tơ, số hàng xóm và véc-tơ truy vấn; ở đây ta viết $n$, $k$, $\mathbf y$.
- Tên đối tượng trong ví dụ viết chữ đứng, như $\mathrm a,\mathrm b$ hay a.vn, để không lẫn với biến.
- Chữ "lượt" chỉ dùng cho lượt đọc hay lượt quét một tệp; mỗi lần thân vòng lặp chạy gọi là một vòng.
- Viết tắt nguồn: MMDS (*Mining of Massive Datasets*, ấn bản 3), BHK (*Foundations of Data Science*), DSC (*Database System Concepts*, ấn bản 7), CS246 (bài giảng mở đầu của Stanford CS246), BIODS 271 (bài giảng *Approximate Nearest Neighbor* của Stanford BIODS 271); chi tiết ở mục tài liệu tham khảo.

<!-- note-topic-id: lec-01-topic-01 -->
## 1. Tổng hợp và tìm kiếm dữ liệu web

Học phần Cấu trúc dữ liệu và giải thuật phân tích thuật toán trong mô hình RAM: đầu vào nằm sẵn trong bộ nhớ truy cập ngẫu nhiên, và thuật toán được đọc lại bất kỳ phần tử nào, bao nhiêu lần cũng được. Với lượng dữ liệu khổng lồ, giả thiết này không còn thực hiện được (BHK, tr.10). Khi đó chi phí của một thuật toán phụ thuộc vào việc dữ liệu nằm ở đâu, được đọc bao nhiêu lần và kết quả phải trả gồm những gì.

Bài toán trung tâm của chương: một kho web có $N=10^6$ tài liệu, cần trả mọi cặp tài liệu có độ tương đồng đạt một ngưỡng cho trước. Số cặp phải xét nếu so từng cặp là
$$
\begin{aligned}
\binom{10^6}{2}&=\frac{10^6\,(10^6-1)}{2}\\
&=499\,999\,500\,000,
\end{aligned}
$$
khoảng nửa nghìn tỷ cặp (MMDS, tr.73). Để phân tích bài toán này, chúng ta cần trả lời ba câu hỏi:

- chi phí được đo bằng đơn vị nào khi dữ liệu không nằm trong bộ nhớ;
- thế nào là trả đúng kết quả, và thuật toán xét mọi cặp tốn bao nhiêu;
- khi nào được phép xét ít cặp hơn mà vẫn trả đủ kết quả.

![Sơ đồ cấu trúc chương: khối trên cùng là bài toán trung tâm, trả mọi cặp tài liệu có SIM ≥ τ trong N = 10⁶ tài liệu, tức 499 999 500 000 cặp; ba mũi tên xuống ba cột. Câu hỏi 1, Mục 2: đo chi phí khi dữ liệu trên đĩa, kết quả là khối, lượt quét, F, 2F, 2mF. Câu hỏi 2, Mục 3.1–3.4: đặc tả R và xét mọi cặp, kết quả N(N−1)L phép so sánh. Câu hỏi 3, Mục 3.5 và 4: giảm số cặp khi nào vẫn đủ, kết quả R̂ = A ∩ R, đủ khi và chỉ khi R ⊆ A.](img/lec-01/note-cau-truc-chuong-01.svg)

Sơ đồ đọc từ trên xuống. Khối trên cùng ghi bài toán trung tâm với $N=10^6$ và số cặp vừa tính. Ba mũi tên dẫn xuống ba cột theo thứ tự ba câu hỏi; mỗi cột ghi mục trả lời câu hỏi và, dưới đường kẻ đứt, kết quả chính của mục đó, chẳng hạn $F$, $2F$, $2mF$ lần truyền khối ở cột thứ nhất.

### 1.1 Bài toán dữ liệu

Một kho thu thập web lưu tệp siêu dữ liệu, mỗi dòng có dạng `(URL, size, date, …)`: địa chỉ trang, kích thước trang tính bằng byte và ngày thu thập. Yêu cầu là tính, cho mỗi máy chủ, tổng số byte của mọi trang thuộc máy chủ đó (CS246, trang chiếu 62). Máy chủ được lấy từ địa chỉ trang. Để làm rõ đầu ra, xem ví dụ sau.

::: example Ví dụ 01.1 (Bốn bản ghi của tệp siêu dữ liệu)
**Dữ kiện.** Bốn dòng của tệp, đã tách máy chủ từ địa chỉ trang:

| Dòng | Máy chủ | Kích thước trang (byte) |
|---:|---|---:|
| 1 | a.vn | 40 |
| 2 | b.vn | 25 |
| 3 | a.vn | 15 |
| 4 | c.vn | 0 |

**Cộng theo máy chủ.** a.vn có hai dòng, $40+15=55$ byte; b.vn có $25$ byte; c.vn có $0$ byte.

**Đầu ra.** $\{(\text{a.vn},55),(\text{b.vn},25),(\text{c.vn},0)\}$.

**Kiểm tra lại.** Tổng của đầu ra $55+25+0=80$ bằng tổng cột kích thước $40+25+15+0=80$; c.vn có một trang trong kho nên có mặt trong đầu ra với tổng 0.
:::

Kho thật có tệp lớn hơn bộ nhớ chính, nên chương trình không nạp trọn tệp rồi cộng một lần được. Một cách xử lý là đọc tệp tuần tự và giữ một bảng tổng đang chạy cho mỗi máy chủ; bảng này cũng phải vừa bộ nhớ, và kích thước của nó tăng theo số máy chủ khác nhau.

![Tệp bản ghi trên đĩa gồm nhiều phần, bộ nhớ chính hữu hạn chỉ chứa được một phần; mũi tên nạp trọn tệp vào bộ nhớ bị chặn.](img/lec-01/kho-nhat-ky-bo-nho.svg)

Mũi tên bị chặn trên hình là cách nạp trọn tệp: cùng đầu vào, cùng đầu ra, nhưng giới hạn bộ nhớ đã loại cách làm này. Do đó, đặc tả một bài toán dữ liệu phải ghi cả tài nguyên được phép dùng.

::: definition Định nghĩa 01.1 (Bài toán dữ liệu)
Một **bài toán dữ liệu** gồm ba thành phần.

- **Miền đầu vào** $\mathcal I$: tập các đầu vào hợp lệ, mô tả kiểu, kích thước và điều kiện trước của dữ liệu. Mỗi phần tử $I\in\mathcal I$ là một **thể hiện** (instance) của bài toán.
- **Quan hệ đầu vào–đầu ra**: với mỗi $I\in\mathcal I$, tập $\mathrm{Out}(I)$ các đầu ra được chấp nhận. Thuật toán **đúng** khi trên mọi $I\in\mathcal I$ nó dừng và trả một phần tử của $\mathrm{Out}(I)$.
- **Ngân sách tài nguyên**: các giới hạn mà mọi lần chạy phải thỏa, như số khối bộ nhớ $M$, số lượt đọc dữ liệu, lượng dữ liệu truyền giữa các máy hoặc dung lượng lưu trữ.
:::

Hai thành phần đầu là cách CLRS định nghĩa một bài toán tính toán (CLRS 4e, §1.1); thành phần thứ ba là phần dữ liệu lớn thêm vào. Ví dụ 01.1 là một thể hiện: $I$ là bốn dòng của bảng, và $\mathrm{Out}(I)$ chỉ có một phần tử, tập ba cặp máy chủ–tổng.

Ba phản ví dụ cho thấy mỗi thành phần đều cần thiết.

- Bỏ quan hệ đầu vào–đầu ra: chương trình trả kích thước từng trang $40,25,15,0$ có đọc hết tệp nhưng không trả tổng theo máy chủ; chương trình bỏ c.vn vì tổng bằng 0 cũng trả đầu ra không thuộc $\mathrm{Out}(I)$.
- Bỏ miền đầu vào: nếu một dòng có kích thước âm, tổng không còn là số byte; miền phải ghi kích thước là số nguyên không âm.
- Bỏ ngân sách: trong mô hình RAM, cộng theo máy chủ là bài tập nhập môn; với tệp lớn hơn $M$ khối, cách nạp trọn tệp không còn dùng được.

### 1.2 Bảy bài toán trên kho web

Bảng dưới đây liệt kê bảy bài toán trên kho web theo Định nghĩa 01.1, cùng trở ngại khi làm trực tiếp và bài của học phần xử lý bài toán đó.

| Bài toán | Đầu vào | Đầu ra | Trở ngại của cách trực tiếp | Bài |
|---|---|---|---|---|
| Tổng kích thước theo máy chủ | tệp `(URL, size, date)` | tổng byte của mỗi máy chủ | tệp lớn hơn bộ nhớ; bảng tổng phải vừa bộ nhớ | 02 |
| Đếm từ | kho tài liệu chia trên nhiều máy | số lần xuất hiện trong toàn kho của mỗi từ | gom cả kho về một máy tốn đường truyền và dồn việc vào máy đó | 02 |
| Điểm quan trọng của trang (PageRank) | đồ thị liên kết có hướng | một điểm cho mỗi trang | mỗi vòng cập nhật đọc mọi liên kết; ma trận đặc cho mọi cặp trang lãng phí khi đồ thị thưa | 03 |
| Xếp hạng theo chủ đề | đồ thị liên kết và một chủ đề cần ưu tiên | điểm có xét chủ đề | không lưu được một véc-tơ điểm dài nhiều tỷ phần tử cho mỗi người trong một tỷ người dùng | 04 |
| Hạn chế liên kết rác | đồ thị có các trang do một bên tạo rác kiểm soát | điểm ít bị các trang đó đẩy lên | nhiều liên kết tới một trang không chứng tỏ nhiều nguồn độc lập | 04 |
| Cặp tài liệu gần trùng | $N$ tài liệu và ngưỡng $\tau$ | mọi cặp có độ tương đồng $\ge\tau$ | $499\,999\,500\,000$ cặp khi $N=10^6$ | 05–06 |
| $k$ hàng xóm gần nhất | $n$ véc-tơ, véc-tơ truy vấn $\mathbf y$ | $k$ véc-tơ gần $\mathbf y$ nhất | quét hết kho cho mỗi truy vấn | 07 |

Ở hàng thứ hai, một từ xuất hiện ba lần trong một tài liệu góp 3 vào số đếm. Ở hàng thứ tư, truy vấn "jaguar" có thể chỉ loài báo, hãng ô tô, một phiên bản hệ điều hành MAC hoặc một máy chơi trò chơi cũ; biết người dùng quan tâm ô tô thì máy tìm kiếm ưu tiên các trang về xe (MMDS, §5.3.1, tr.195–196). Ở hàng thứ năm, một trang đích được nhiều trang hỗ trợ cùng một chủ sở hữu trỏ tới, và trang đích trỏ ngược lại từng trang hỗ trợ (MMDS, Hình 5.16, tr.200).

Một cách trực quan, hai hàng cuối có đầu ra khác hẳn nhau. Tìm cặp gần trùng xét cả kho một lần và trả một tập cặp, có thể rất lớn. Tìm hàng xóm gần nhất nhận từng truy vấn, mỗi truy vấn trả đúng $k$ đối tượng, và công việc lặp lại với mọi truy vấn mới. Hàng cuối cần được nêu chính xác, kể cả trường hợp nhiều véc-tơ cách truy vấn bằng nhau.

![Một véc-tơ truy vấn được đối chiếu với từng đoạn tài liệu đã mã hóa thành véc-tơ bằng phép tính khoảng cách; kết quả là k đoạn tài liệu gần nhất.](img/lec-01/ung-dung-truy-hoi-vec-to.svg)

Trên hình, mỗi đoạn tài liệu và truy vấn được mã hóa thành véc-tơ cùng số chiều bằng cùng một phép mã hóa (BIODS 271 L12, tr.16); quét toàn kho nghĩa là tính khoảng cách từ truy vấn tới từng đoạn rồi giữ $k$ đoạn gần nhất.

::: definition Định nghĩa 01.2 ($k$ hàng xóm gần nhất chính xác)
Cho kho $n$ véc-tơ $\mathbf x_1,\ldots,\mathbf x_n\in\mathbb R^D$, véc-tơ truy vấn $\mathbf y\in\mathbb R^D$, một hàm khoảng cách $d:\mathbb R^D\times\mathbb R^D\to[0,\infty)$ và số nguyên $k$ với $1\le k\le n$. Sắp các chỉ số $1,\ldots,n$ theo cặp $(d(\mathbf x_i,\mathbf y),\,i)$ tăng dần theo thứ tự từ điển: khoảng cách nhỏ đứng trước, và khi hai véc-tơ cách $\mathbf y$ bằng nhau thì chỉ số nhỏ đứng trước. Tập **$k$ hàng xóm gần nhất** (k nearest neighbors) $\mathcal N_k(\mathbf y)$ là tập $k$ chỉ số đứng đầu thứ tự đó.
:::

Định nghĩa có ba điều kiện. Khoảng cách phải được chọn trước, vì cùng một kho có thể cho hai tập hàng xóm khác nhau với hai hàm khoảng cách. Điều kiện $1\le k\le n$ bảo đảm có đủ $k$ véc-tơ để trả. Quy tắc phá hòa làm $\mathcal N_k(\mathbf y)$ thành một tập duy nhất. Ví dụ: với $n=3$, $k=1$ và $d(\mathbf x_1,\mathbf y)=d(\mathbf x_2,\mathbf y)=1<d(\mathbf x_3,\mathbf y)$, không có quy tắc phá hòa thì cả $\{1\}$ lẫn $\{2\}$ đều "gần nhất"; quy tắc trên chọn $\mathcal N_1(\mathbf y)=\{1\}$.

::: example Ví dụ 01.2 (Quy mô của một kho véc-tơ)
**Dữ kiện.** Kho có $n=10^{10}$ véc-tơ, mỗi véc-tơ $D=3072$ thành phần, mỗi thành phần 32 bit, tức 4 byte (BIODS 271 L12, tr.17).

**Dung lượng kho.** $10^{10}\cdot3072\cdot4=1{,}2288\times10^{14}$ byte, tức $122{,}88$ TB.

**Công việc của một truy vấn khi quét hết kho.** Mọi $\mathbf x_i$ đều có thể thuộc $\mathcal N_k(\mathbf y)$, nên phải tính $n=10^{10}$ khoảng cách, mỗi khoảng cách đọc $3072$ thành phần.

**Kiểm tra lại.** $3072\cdot4=12\,288$ byte mỗi véc-tơ; $12\,288\cdot10^{10}=1{,}2288\times10^{14}$.
:::

Truy vấn tiếp theo lặp lại toàn bộ $10^{10}$ phép tính khoảng cách.

::: remark Nhận xét 01.3 (Trong thực hành: nhiều máy và máy hỏng)
Khi dữ liệu và tính toán chia trên nhiều máy, máy hỏng trở thành sự kiện thường xuyên: một máy chủ chạy khoảng 1000 ngày, nên với một triệu máy, mỗi ngày hỏng khoảng 1000 máy (CS246, trang chiếu 32). Sao chép dữ liệu qua mạng cũng tốn thời gian, nên các hệ thống đưa tính toán tới nơi lưu dữ liệu và lưu mỗi tệp thành nhiều bản (CS246, trang chiếu 33). Trong bài toán đếm từ, mỗi máy đếm phần kho của mình, và một tác vụ chạy lại sau khi máy hỏng không được làm mất hay đếm trùng đóng góp nào.
:::

::: exercise Bài tập 01.1 (Ba bài toán trên kho web)
Với mỗi bài toán sau, nêu đầu vào, đầu ra và trở ngại của cách làm trực tiếp theo ba thành phần của Định nghĩa 01.1.

- (a) Tính tổng kích thước theo máy chủ khi tệp bản ghi lớn hơn bộ nhớ.
- (b) Tìm mọi cặp gần trùng trong $10^6$ tài liệu.
- (c) Tìm $k$ đoạn tài liệu gần một véc-tơ truy vấn trong kho $10^{10}$ véc-tơ.
:::

::: hint
Trở ngại là thành phần ngân sách mà cách làm trực tiếp vi phạm: bộ nhớ, số phép tính hay công việc lặp lại mỗi truy vấn.
:::

::: solution
**Câu (a).** Đầu vào: tệp các dòng `(URL, size, date)`, kích thước là số nguyên không âm. Đầu ra: một cặp (máy chủ, tổng byte) cho mỗi máy chủ có trang trong kho. Trở ngại: tệp lớn hơn $M$ khối nên không nạp trọn được; bảng tổng cũng phải vừa bộ nhớ.

**Câu (b).** Đầu vào: $N=10^6$ tài liệu và ngưỡng $\tau$. Đầu ra: mọi cặp có độ tương đồng $\ge\tau$, mỗi cặp một lần. Trở ngại: so từng cặp phải xét $499\,999\,500\,000$ cặp.

**Câu (c).** Đầu vào: $n=10^{10}$ véc-tơ 3072 chiều, $\mathbf y$, $d$, $k$ và quy tắc phá hòa. Đầu ra: $\mathcal N_k(\mathbf y)$. Trở ngại: mỗi truy vấn cần $10^{10}$ phép tính khoảng cách trên kho $122{,}88$ TB (Ví dụ 01.2).

**Kiểm tra lại.** Ba đầu ra khác kiểu: một bảng theo khóa, một tập cặp, một tập $k$ chỉ số.
:::

::: exercise Bài tập 01.2 (Số đối tượng phải xét)
Kho có $10^6$ tài liệu, mỗi tài liệu cũng được mã hóa thành một véc-tơ. So số đối tượng phải xét của hai việc: (a) tìm mọi cặp gần trùng bằng cách so từng cặp; (b) trả lời một truy vấn $k$ hàng xóm gần nhất bằng cách quét hết kho. Cần bao nhiêu truy vấn để công việc của (b) bằng công việc của (a)?
:::

::: hint
Đếm cặp cho (a), đếm khoảng cách cho (b), rồi chia.
:::

::: solution
**Câu (a).** $\binom{10^6}{2}=499\,999\,500\,000$ cặp.

**Câu (b).** $10^6$ phép tính khoảng cách cho một truy vấn, không phụ thuộc $k$.

**Số truy vấn.** $499\,999\,500\,000/10^6=499\,999{,}5$, tức khoảng $5\times10^5$ truy vấn. Một truy vấn rẻ hơn tìm mọi cặp khoảng nửa triệu lần, nhưng công việc của (b) lặp lại theo số truy vấn.

**Kiểm tra lại.** $\binom N2/N=(N-1)/2$, với $N=10^6$ cho $499\,999{,}5$.
:::

Như vậy, chúng ta đã có Định nghĩa 01.1 để đặc tả một bài toán dữ liệu bằng miền đầu vào, quan hệ đầu vào–đầu ra và ngân sách tài nguyên, cùng Định nghĩa 01.2 cho đầu ra chính xác của tìm hàng xóm gần nhất. Tuy nhiên, ngân sách mới được nói bằng lời: "tệp lớn hơn bộ nhớ" chưa cho biết một cách đọc tốn bao nhiêu. Trong Mục 2, chúng ta lấy khối làm đơn vị đo khi dữ liệu nằm trên đĩa và đếm chi phí của một lượt quét.

<!-- note-topic-id: lec-01-topic-02 -->
## 2. Dòng dữ liệu, nén và truy vấn trên đĩa

Giả sử tệp siêu dữ liệu của Ví dụ 01.1 chiếm 1 TB trên đĩa, còn bộ nhớ chính có 1 GB, tức một phần nghìn tệp. Mọi cách xử lý tệp đều phải đọc nó từ đĩa theo từng phần, nên chúng ta cần một đơn vị đo việc đọc ghi. Ba nhóm bài toán sau còn đặt thêm giới hạn riêng: trạng thái giữ trong bộ nhớ với dữ liệu đến liên tục, dung lượng lưu với dữ liệu cần nén, và số khối phải đọc khi sắp xếp, tra cứu hay nối.

### 2.1 Khối và lượt quét

Đĩa trao đổi dữ liệu với bộ nhớ chính theo từng khối, không theo từng byte. MMDS (§1.3.4, tr.13) giả sử một đĩa từ với ba số liệu:

- một khối có $2^{16}=65\,536$ byte;
- truy cập và đọc một khối mất khoảng 10 mili giây, chậm hơn đọc một từ trong bộ nhớ chính ít nhất $10^5$ lần;
- đĩa chuyển dữ liệu vào bộ nhớ không nhanh hơn $10^8$ byte mỗi giây.

Khi chỉ cần vài byte, thời gian truyền khối lớn hơn nhiều thời gian tính trên khối đó. Vì vậy chi phí của thuật toán trên đĩa được đếm bằng số khối được truyền.

::: definition Định nghĩa 01.4 (Khối, lần truyền khối và lượt quét)
- **Khối** (block) là đơn vị nhỏ nhất mà hệ điều hành chuyển giữa đĩa và bộ nhớ chính. Một tệp chiếm $F$ khối; bộ nhớ chính chứa được $M$ khối.
- Một **lần truyền khối** (block transfer) là một lần đọc một khối từ đĩa vào bộ nhớ hoặc một lần ghi một khối từ bộ nhớ ra đĩa.
- Một **lượt quét** (pass) trên một tệp đọc mỗi khối của tệp đúng một lần.
- Trong **mô hình chi phí đọc ghi**, chi phí của một thuật toán là tổng số lần truyền khối; phép tính trên dữ liệu đã nằm trong bộ nhớ không được tính.
:::

Định nghĩa đổi đơn vị đo của mô hình RAM từ phép toán sang khối: hai thuật toán có cùng số phép so sánh vẫn có thể khác số lần truyền khối. Với khối $65\,536$ byte, một tệp $\beta$ byte chiếm $F=\lceil\beta/65\,536\rceil$ khối, vì khối cuối có thể không đầy.

::: example Ví dụ 01.3 (Tệp 1 TB)
**Dữ kiện.** Tệp $10^{12}$ byte; theo giả thiết của MMDS (§1.3.4, tr.13), khối $65\,536$ byte, tốc độ truyền tối đa $10^8$ byte/giây, và mỗi lần truy cập một khối riêng lẻ mất khoảng 10 mili giây.

**Số khối.** $10^{12}/65\,536=15\,258\,789{,}0625$, nên $F=15\,258\,790$ khối.

**Đọc tuần tự.** Ở tốc độ tối đa, đọc $10^{12}$ byte mất ít nhất $10^{12}/10^8=10^4$ giây, khoảng $2{,}78$ giờ.

**Đọc từng khối bằng một truy cập riêng.** $15\,258\,790\cdot0{,}01=152\,587{,}9$ giây, khoảng $1{,}53\times10^5$ giây hay $1{,}77$ ngày.

**Kiểm tra lại.** $15\,258\,789\cdot65\,536<10^{12}\le15\,258\,790\cdot65\,536$; $152\,587{,}9/86\,400\approx1{,}766$.
:::

Hai cách đọc cùng truyền $F$ khối nhưng thời gian khác nhau khoảng 15 lần, nên số lần truyền khối là đơn vị đếm của mô hình, khác số giây. Trong cả hai trường hợp, một lượt quét tệp 1 TB đã tốn hàng giờ, nên số lượt quét là đại lượng cần giảm.

::: proposition Mệnh đề 01.5 (Chi phí của lượt quét)
**Giả thiết.** Một tệp chiếm $F$ khối; trước mỗi lượt, không khối nào của tệp nằm sẵn trong bộ nhớ; mỗi lượt đọc mỗi khối đúng một lần; khi lượt ghi kết quả, tệp kết quả cũng chiếm $F$ khối và mỗi khối được ghi một lần.

**Kết luận.**

- (a) Một lượt chỉ đọc tốn đúng $F$ lần truyền khối.
- (b) Một lượt đọc tệp và ghi lại $F$ khối tốn $2F$ lần truyền khối.
- (c) $m$ lượt như (b) tốn $2mF$ lần truyền khối.

**Điều kiện áp dụng.** Chi phí được đo theo mô hình đọc ghi của Định nghĩa 01.4.

**Phạm vi.** Mệnh đề đếm lần truyền khối, không đếm thời gian, và không phân biệt đọc tuần tự với đọc ngẫu nhiên.
:::

::: proof
**Bước 1 (lượt đọc tốn $F$).** Mỗi khối không có sẵn trong bộ nhớ, nên phải được truyền vào ít nhất một lần; lượt đọc mỗi khối đúng một lần, nên mỗi khối được truyền đúng một lần. Tổng là $F$ [do giả thiết].

**Bước 2 (đọc và ghi tốn $2F$).** Phần ghi truyền $F$ khối ra đĩa, mỗi khối một lần, góp thêm $F$. Tổng là $F+F=2F$.

**Bước 3 ($m$ lượt tốn $2mF$).** Theo giả thiết, trước mỗi lượt không khối nào có sẵn trong bộ nhớ, nên mỗi lượt tốn $2F$ theo Bước 2. Cộng $m$ lượt được $2mF$. $\square$
:::

Các giả thiết của Mệnh đề 01.5 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "không khối nào có sẵn": nếu $F=3$ và một khối đã nằm trong bộ nhớ, lượt đọc chỉ tốn 2 lần truyền khối.
- Bỏ "mỗi khối đọc đúng một lần": một chương trình đọc lại khối đầu sau khi đọc hết tệp, khi khối đầu đã bị đẩy khỏi bộ nhớ, tốn $F+1$ lần truyền khối.
- Bỏ "tệp kết quả chiếm $F$ khối": bài toán tổng theo máy chủ ghi một bảng tổng nhỏ hơn tệp, nên lượt đọc và ghi tốn ít hơn $2F$.

Bước 1 dùng hai giả thiết đầu; Bước 2 dùng giả thiết về tệp kết quả; Bước 3 dùng giả thiết đầu cho từng lượt. Giả thiết đầu cũng là giả thiết trường hợp xấu nhất mà DSC dùng khi ước lượng chi phí (DSC, Chương 15, trang chiếu 9).

::: remark Nhận xét 01.6 (Trong thực hành: số khối và thời gian)
Ví dụ 01.3 cho thấy cùng $F$ lần truyền khối có thể mất khoảng $2{,}78$ giờ hay khoảng $1{,}77$ ngày tùy thứ tự truy cập. Vì vậy DSC tính thời gian bằng số lần truyền khối nhân $t_T$ cộng số lần dịch chuyển đầu đọc (seek) nhân $t_S$, trong đó $t_T$ là thời gian truyền một khối và $t_S$ là thời gian một lần dịch chuyển đầu đọc; đây là ký hiệu của DSC, chỉ dùng trong nhận xét này. Với khối 4 KB, $t_T=0{,}1$ mili giây, $t_S=4$ mili giây cho đĩa từ và $t_T=2$–$10$ micro giây, $t_S=20$–$90$ micro giây cho ổ thể rắn (SSD) (DSC, Chương 15, trang chiếu 8). Mệnh đề 01.5 so được hai thuật toán có cùng kiểu truy cập; khi kiểu truy cập khác nhau, cần đếm cả số lần dịch chuyển.
:::

### 2.2 Dòng dữ liệu

Một máy tìm kiếm nhận liên tục các bản ghi `(user, query, time)`: người dùng, truy vấn và thời điểm. Nó muốn trả lời câu hỏi "trong tháng vừa qua, một người dùng điển hình lặp lại bao nhiêu phần trong các truy vấn của mình?", nhưng chỉ được lưu $1/10$ số bản ghi (MMDS, §4.2.1, tr.136). Cách tự nhiên là giữ mỗi bản ghi với xác suất $1/10$. Ví dụ sau cho thấy cách này trả sai đại lượng cần đo.

::: example Ví dụ 01.4 (Mẫu theo từng truy vấn)
**Dữ kiện.** Trong tháng, một người dùng có $\mu_1$ truy vấn xuất hiện đúng một lần và $\mu_2$ truy vấn xuất hiện đúng hai lần; không truy vấn nào xuất hiện quá hai lần. Mỗi bản ghi được giữ độc lập với xác suất $1/10$ (MMDS, §4.2.1, tr.136–137).

**Tỷ lệ cần đo.** Trong $\mu_1+\mu_2$ truy vấn khác nhau, có $\mu_2$ truy vấn lặp, nên tỷ lệ là $\mu_2/(\mu_1+\mu_2)$.

**Số đếm kỳ vọng trên mẫu.** Một truy vấn lặp có cả hai lần trong mẫu với xác suất $(1/10)^2=1/100$, có đúng một lần với xác suất $2\cdot\frac1{10}\cdot\frac9{10}=18/100$. Trên mẫu, kỳ vọng số truy vấn xuất hiện hai lần là $\mu_2/100$, kỳ vọng số truy vấn xuất hiện một lần là $\mu_1/10+18\mu_2/100$.

**Tỷ số trên mẫu.** Tỷ số của hai số đếm kỳ vọng là
$$
\begin{aligned}
&\frac{\mu_2/100}{\mu_2/100+\mu_1/10+18\mu_2/100}\\
&\quad=\frac{\mu_2}{10\mu_1+19\mu_2}.
\end{aligned}
$$

**Kiểm tra lại.** Với $\mu_1=\mu_2=10$, đáp đúng là $1/2$, còn tỷ số trên mẫu là $10/290=1/29$. Với $\mu_1,\mu_2>0$, tỷ số trên mẫu luôn nhỏ hơn đáp đúng vì $10\mu_1+19\mu_2>\mu_1+\mu_2$.
:::

Sai lệch đến từ đơn vị lấy mẫu: câu hỏi nói về từng người dùng, còn mẫu chọn từng bản ghi nên làm vỡ các cặp truy vấn lặp. Nếu chọn $1/10$ số người dùng và giữ mọi truy vấn của họ, mỗi người dùng được giữ có đủ lịch sử, và tỷ lệ lặp tính trên người đó bằng $\mu_2/(\mu_1+\mu_2)$ (MMDS, §4.2.2, tr.137).

Bài toán thứ hai là lọc thư: dòng dữ liệu gồm các cặp (địa chỉ gửi, nội dung thư), và đầu ra cho qua thư khi và chỉ khi địa chỉ gửi thuộc danh sách cho phép gồm $10^9$ địa chỉ. Một địa chỉ điển hình có từ 20 byte trở lên, nên danh sách chiếm khoảng $2\times10^{10}$ byte trở lên, tức 20 GB trở lên, trong khi bộ nhớ chính giả sử có 1 GB, tức $8\cdot10^9$ bit (MMDS, §4.3.1, tr.139–140). Nếu danh sách nằm trên đĩa, mỗi thư đến có thể cần một lần đọc đĩa. Vấn đề là chọn trạng thái $8\cdot10^9$ bit nào để loại phần lớn thư ngoài danh sách mà không loại thư trong danh sách.

![Bên trái: nhật ký truy vấn đi qua bước chọn người dùng để tạo mẫu gồm toàn bộ truy vấn của người được chọn. Bên phải: mỗi thư đến được kiểm địa chỉ gửi theo danh sách cho phép rồi được nhận hoặc bị bỏ.](img/lec-01/ung-dung-dong-truy-van.svg)

Hai bài toán trên hình có chung ràng buộc: bản ghi đến liên tục, mỗi bản ghi được xử lý khi đến, và trạng thái giữ lại phải vừa bộ nhớ.

Nhật ký truy cập còn đặt hai câu hỏi đếm: số người dùng khác nhau đã gặp, và số lần truy cập trong một khoảng thời gian gần nhất (gọi là **cửa sổ**, window). Lưu mọi mã người dùng đã gặp có thể vượt bộ nhớ; một bộ đếm tổng số lần truy cập từ đầu không biết lần nào đã ra khỏi cửa sổ.

### 2.3 Nén dữ liệu

Một số đếm trả lời được một câu hỏi về nhật ký, nhưng không dựng lại được nhật ký. Khi dữ liệu phải được lưu để đọc lại, yêu cầu là giảm dung lượng mà vẫn khôi phục được dữ liệu với mức chính xác cho trước.

::: definition Định nghĩa 01.7 (Nén không mất thông tin và nén có mất thông tin)
Một **bộ nén** gồm bộ mã hóa $\mathrm{enc}$ biến dữ liệu $x$ thành chuỗi bit $\mathrm{enc}(x)$ và bộ giải mã $\mathrm{dec}$ biến chuỗi bit đó thành dữ liệu $\mathrm{dec}(\mathrm{enc}(x))$.

- Bộ nén là **không mất thông tin** (lossless) khi $\mathrm{dec}(\mathrm{enc}(x))=x$ với mọi $x$ trong miền đầu vào.
- Bộ nén là **có mất thông tin** (lossy) khi $\mathrm{dec}(\mathrm{enc}(x))$ được phép khác $x$, miễn thỏa một tiêu chí chất lượng mà ứng dụng quy định.
- **Dung lượng** của dữ liệu nén gồm $\mathrm{enc}(x)$ cùng mọi thông tin mà bộ giải mã cần nhưng không tự dựng lại được.
:::

Theo Định nghĩa 01.1, đầu ra chấp nhận được của bộ giải mã chỉ có $x$ với nén không mất thông tin, và là mọi dữ liệu đạt tiêu chí chất lượng với nén có mất thông tin. Ví dụ, chuỗi `aabaacabcabcb` gồm 13 ký tự có các cụm lặp `ab` và `abc` (CMU 15-499, *compression3-lz*, trang chiếu 13–14, 17, 19). Bộ mã hóa được khai thác các cụm lặp đó, nhưng bộ giải mã phải khôi phục đủ 13 ký tự theo đúng thứ tự; bỏ lần lặp thứ hai của `abc` thì không bộ giải mã nào biết phải chèn lại ở đâu.

![Dữ liệu mã cùng thông tin giải mã đi vào bộ giải mã và phải khôi phục đúng chuỗi aabaacabcabcb.](img/lec-01/ung-dung-nen-van-ban.svg)

Hình minh họa cách tính dung lượng trong Định nghĩa 01.7: dữ liệu mã và thông tin giải mã cùng chiếm dung lượng. Với ảnh, yêu cầu khác: thay các mức sáng gần nhau bằng một mức đại diện, gọi là **lượng tử hóa** (quantization), làm giảm số giá trị phải lưu nhưng không khôi phục được các mức ban đầu (Nelson và Gailly, Chương 11).

![Minh họa định tính: nhiều mức sáng gần nhau được gộp thành ít mức đại diện hơn, làm mất phân biệt giữa các mức ban đầu.](img/lec-01/ung-dung-nen-anh.svg)

Trên hình, hai mức đã gộp không còn phân biệt được sau giải mã. Vì thế một kết quả nén ảnh có mất thông tin phải báo cùng lúc hai đại lượng: dung lượng bản nén và sai khác giữa ảnh khôi phục với ảnh gốc theo tiêu chí đã chọn.

### 2.4 Dữ liệu trên đĩa: sắp xếp, tra cứu và nối

Với dữ liệu đã lưu trên đĩa, ba nhóm truy vấn thường gặp đều được đo bằng số lần truyền khối của Định nghĩa 01.4.

- **Sắp xếp** nhận tệp bản ghi chưa có thứ tự và trả tệp gồm đủ các bản ghi ấy theo khóa tăng dần, kể cả bản ghi có khóa lặp; sắp xếp không loại trùng. Khi tệp $F$ khối lớn hơn bộ nhớ, ta sắp từng phần vừa bộ nhớ rồi trộn các dãy đã sắp. DSC đếm $2F$ lần truyền khối cho việc tạo dãy và cho mỗi lượt trộn, trừ lượt trộn cuối chỉ tính $F$ vì kết quả có thể chuyển thẳng cho phép toán tiếp theo mà không ghi ra đĩa (DSC, Chương 15, trang chiếu 19–22).
- **Tra cứu** trả mọi bản ghi thỏa một điều kiện mà không quét cả tệp (DSC, Chương 14, 24, 31):
  - theo mã, như hồ sơ giảng viên có mã cho trước;
  - theo khoảng, như mọi hồ sơ có lương trong một đoạn;
  - theo hai từ khóa, bằng giao hai danh sách tài liệu của một **chỉ mục đảo** (inverted index);
  - theo một vùng bản đồ, trong đó **hộp bao** (bounding box) của một nhóm đối tượng chỉ cho ứng viên.
- **Nối** ghép hai bảng theo thuộc tính chung, như bảng sinh viên `student` với bảng đăng ký `takes` theo mã sinh viên; đầu ra gồm mọi cặp bản ghi trùng mã, và một sinh viên đăng ký nhiều môn tạo nhiều kết quả. Trong ví dụ của DSC, `student` có $5000$ bản ghi trong $100$ khối và `takes` có $10\,000$ bản ghi trong $400$ khối (DSC, Chương 15, trang chiếu 24). Giả sử bộ nhớ có $M=20$ khối, như ví dụ nối băm của DSC (Chương 15, trang chiếu 40); khi đó không bảng nào nạp trọn vào bộ nhớ được.

![Bảng hồ sơ sinh viên ghép với từng bản ghi đăng ký cùng mã để trả sinh viên kèm môn đã đăng ký.](img/lec-01/ung-dung-noi-bang.svg)

Hình cho thấy một hồ sơ sinh viên có thể ghép với nhiều bản ghi đăng ký. Quét lại cả bảng đăng ký cho mỗi sinh viên đọc cùng các khối nhiều lần.

Tra cứu theo mã cần một cấu trúc chỉ ra bản ghi có mã cho trước nằm ở khối nào. Một cấu trúc cho việc đó dùng hàm băm.

::: definition Định nghĩa 01.8 (Hàm băm và chỉ mục băm)
- Một **hàm băm** (hash function) $h$ nhận một **khóa băm** (hash-key) và trả một **số thùng** (bucket number), một số nguyên trong $\{0,1,\ldots,B-1\}$, với $B$ là số thùng.
- Một **chỉ mục** (index) trên một trường của tệp bản ghi là cấu trúc dữ liệu cho phép, với một giá trị $v$ của trường đó, lấy mọi bản ghi có giá trị $v$ ở trường đó mà không đọc mọi bản ghi của tệp.
- Một **chỉ mục băm** đặt mỗi bản ghi vào thùng số $h(\text{khóa})$, với khóa là giá trị của trường được chỉ mục. Để tìm các bản ghi có khóa $v$, ta tính $h(v)$ rồi chỉ duyệt thùng $h(v)$.
:::

Thùng có thể là một danh sách liên kết trong bộ nhớ hoặc một khối trên đĩa (MMDS, §1.3.3, tr.11–12). Chỉ mục băm đúng vì mọi bản ghi có khóa $v$ đều nằm trong thùng $h(v)$; nó nhanh khi mỗi thùng có ít bản ghi. Tính chất mong muốn của hàm băm là: khi khóa được rút từ một tập khóa hợp lý, mỗi thùng nhận số khóa xấp xỉ bằng nhau (MMDS, §1.3.2, tr.10).

::: example Ví dụ 01.5 (Chỉ mục băm theo số điện thoại)
**Dữ kiện.** Tệp bản ghi (tên, địa chỉ, số điện thoại) có chỉ mục băm trên trường số điện thoại; mỗi thùng là một danh sách liên kết, và một mảng $B$ đầu danh sách cho biết thùng $i$ bắt đầu ở đâu. Số điện thoại 800-555-1212 được băm vào thùng 17 (MMDS, Ví dụ 1.6, tr.12).

**Tra cứu.** Tính $h(\text{800-555-1212})=17$, đọc đầu danh sách thứ 17, duyệt danh sách đó và so số điện thoại của từng bản ghi với 800-555-1212.

**Kết quả.** Thùng 17 chứa mọi bản ghi có số 800-555-1212, và có thể chứa bản ghi có số khác được băm vào 17; phép so ở bước tra cứu loại các bản ghi đó.

**Kiểm tra lại.** Không bản ghi nào có số 800-555-1212 nằm ngoài thùng 17, vì vị trí của bản ghi do chính $h$ quyết định.
:::

::: exercise Bài tập 01.3 (Ba lượt sắp xếp)
Một thuật toán sắp xếp ngoài xử lý tệp $F$ khối qua ba lượt; mỗi lượt đọc hết tệp và ghi ra một tệp $F$ khối, và trước mỗi lượt không khối nào nằm sẵn trong bộ nhớ. Tính số lần truyền khối, rồi áp dụng cho tệp 1 TB với khối $65\,536$ byte.
:::

::: hint
Kiểm từng giả thiết của Mệnh đề 01.5 rồi dùng Kết luận (c).
:::

::: solution
**Kiểm giả thiết.** Mỗi lượt đọc mỗi khối một lần, ghi $F$ khối, và không khối nào có sẵn trước lượt; đó là giả thiết của Mệnh đề 01.5.

**Số lần truyền khối.** Theo Mệnh đề 01.5(c) với $m=3$: $2\cdot3\cdot F=6F$.

**Tệp 1 TB.** Theo Ví dụ 01.3, $F=15\,258\,790$, nên $6F=91\,552\,740$ lần truyền khối.

**Kiểm tra lại.** Mỗi lượt tốn $2F=30\,517\,580$; nhân 3 được $91\,552\,740$. Nếu lượt cuối không ghi kết quả ra đĩa, như quy ước của DSC, lượt đó tốn $F$ và tổng là $5F=76\,293\,950$.
:::

::: exercise Bài tập 01.4 (Số đếm, bản nén và ảnh)
- (a) Giải thích vì sao một số đếm người dùng khác nhau không thay được bản nén không mất thông tin của nhật ký truy cập.
- (b) Một phương pháp nén ảnh có mất thông tin được báo cáo bằng một con số duy nhất. Nêu hai đại lượng phải báo cùng nhau.
:::

::: hint
Dùng điều kiện $\mathrm{dec}(\mathrm{enc}(x))=x$ và tiêu chí chất lượng của Định nghĩa 01.7.
:::

::: solution
**Câu (a).** Hai nhật ký khác nhau có thể có cùng số người dùng khác nhau, ví dụ cùng hai người nhưng thứ tự các lần truy cập khác nhau. Từ một số đếm, không bộ giải mã nào khôi phục được cả hai nhật ký, nên số đếm không thỏa $\mathrm{dec}(\mathrm{enc}(x))=x$ của Định nghĩa 01.7.

**Câu (b).** Dung lượng bản nén, tính cả thông tin giải mã, và sai khác giữa ảnh khôi phục với ảnh gốc theo tiêu chí đã chọn. Chỉ báo dung lượng thì một bộ nén bỏ hết ảnh cũng "tốt nhất"; chỉ báo sai khác thì bản không nén cũng "tốt nhất".

**Kiểm tra lại.** Câu (a) là phản ví dụ cho tính đơn ánh của $\mathrm{enc}$; câu (b) dùng hai điều kiện cuối của Định nghĩa 01.7.
:::

Như vậy, chúng ta đã có đơn vị đo chi phí khi dữ liệu nằm trên đĩa (Định nghĩa 01.4) và công thức $F$, $2F$, $2mF$ cho các lượt quét (Mệnh đề 01.5); các bài toán dòng, nén và truy vấn trên đĩa được phát biểu bằng đầu ra và trạng thái phải giữ, và Định nghĩa 01.8 cho cấu trúc tra cứu đầu tiên. Tuy nhiên, chưa thuật toán nào được chứng minh đúng, và bài toán cặp gần trùng chưa có độ đo cho "gần trùng". Trong Mục 3, chúng ta đặc tả chính xác bài toán cặp gần trùng, chứng minh tính đúng của thuật toán xét mọi cặp và đếm chi phí của nó.

<!-- note-topic-id: lec-01-topic-03 -->
## 3. Đặc tả và đánh giá thuật toán

Bài toán trung tâm của chương, trả mọi cặp đạt ngưỡng trong $N=10^6$ tài liệu, cần một độ đo cho "gần trùng", một đặc tả chính xác của tập kết quả và một thuật toán có chứng minh tính đúng.

### 3.1 Độ tương đồng Jaccard

Trên web, nhiều trang là bản sao của nhau: một trang được sao sang máy chủ khác, giữ gần như toàn bộ nội dung và chỉ đổi phần thông tin về máy chủ và về các bản sao khác (MMDS, tr.73). So từng ký tự chỉ nhận ra hai tài liệu giống hệt; hai bản sao khác nhau ở vài dòng đã bị coi là khác (MMDS, §3.1.2, tr.75). Vì vậy mỗi tài liệu được biểu diễn bằng tập các **đoạn ký tự** (shingle), tức các chuỗi gồm một số cố định ký tự liên tiếp xuất hiện trong tài liệu, với cùng một độ dài đoạn cho cả kho. Một đoạn lặp nhiều lần trong văn bản chỉ là một phần tử của tập. Giả sử các tập $C_i$ đã có sẵn.

::: example Ví dụ 01.6 (Hai tập có ba phần tử chung)
**Dữ kiện.** Hai tập $C_1$, $C_2$ (MMDS, Ví dụ 3.1, tr.74; Hình 3.1, tr.75): hai phần tử chỉ thuộc $C_1$, ba phần tử thuộc cả hai, ba phần tử chỉ thuộc $C_2$.

**Giao và hợp.** $|C_1\cap C_2|=3$; $|C_1\cup C_2|=2+3+3=8$.

**Tỷ lệ phần chung.** $3/8$.

**Kiểm tra lại.** $|C_1|=5$, $|C_2|=6$, và $|C_1|+|C_2|-|C_1\cap C_2|=5+6-3=8=|C_1\cup C_2|$.
:::

![Hai tập S và T chồng lên nhau: hai phần tử chỉ thuộc S, ba phần tử chung, ba phần tử chỉ thuộc T; giao có ba phần tử, hợp có tám.](img/lec-01/danh-gia-jaccard.svg)

Hình ghi hai tập bằng chữ $S$ (tập $C_1$) và $T$ (tập $C_2$). Vùng giữa là giao, cả hình là hợp. Một cách trực quan, độ gần trùng nên là phần chung tính trên toàn bộ nội dung của hai tài liệu: hai tập lớn chung ba phần tử ít giống nhau hơn hai tập nhỏ chung ba phần tử. Chia số phần tử chung cho số phần tử của hợp cho đúng tỷ lệ đó.

::: definition Định nghĩa 01.9 (Độ tương đồng Jaccard)
Cho hai tập hữu hạn $C,C'$ với $C\cup C'\ne\varnothing$. **Độ tương đồng Jaccard** (Jaccard similarity) của chúng là
$$
\mathrm{SIM}(C,C')=\frac{|C\cap C'|}{|C\cup C'|}.
$$
:::

Tử số đếm các đoạn ký tự có trong cả hai tài liệu; mẫu số đếm mỗi đoạn có trong ít nhất một tài liệu đúng một lần. Vì $C\cap C'\subseteq C\cup C'$, ta có $0\le \mathrm{SIM}(C,C')\le1$. Ví dụ 01.6 là trường hợp $|C\cap C'|=3$, $|C\cup C'|=8$, nên $\mathrm{SIM}(C_1,C_2)=3/8$. Hai giá trị đầu mút có nghĩa như sau.

- $\mathrm{SIM}(C,C')=1$ khi và chỉ khi $C=C'$: giao bằng hợp chỉ khi mỗi phần tử của tập này thuộc tập kia.
- $\mathrm{SIM}(C,C')=0$ khi và chỉ khi $C\cap C'=\varnothing$.
- Khi $C=C'=\varnothing$, biểu thức là $0/0$ và không xác định; vì vậy định nghĩa đòi hỏi $C\cup C'\ne\varnothing$, và đặc tả dưới đây chỉ nhận tập không rỗng.

Trên tập đoạn ký tự, $\mathrm{SIM}$ đo độ giống nhau ở mức ký tự, không đo nghĩa (MMDS, §3.1.2, tr.74): hai tài liệu cùng nói về một chủ đề bằng câu chữ khác nhau có thể có $\mathrm{SIM}$ nhỏ.

### 3.2 Đặc tả bài toán tìm cặp gần trùng

Với độ đo đã có, đầu ra của bài toán trung tâm được viết thành một tập.

::: definition Định nghĩa 01.10 (Bài toán tìm cặp gần trùng)
**Đầu vào.** Số nguyên $N\ge0$; các tập hữu hạn, không rỗng $C_1,\ldots,C_N$, với $C_i$ là tập đoạn ký tự của tài liệu thứ $i$; ngưỡng $\tau\in[0,1]$.

**Đầu ra.** Tập
$$
\begin{aligned}
R=\{(i,j):\ &1\le i<j\le N,\\
&\mathrm{SIM}(C_i,C_j)\ge\tau\},
\end{aligned}
$$
mỗi cặp của $R$ xuất hiện đúng một lần; thứ tự xuất các cặp không quy định. Khi $N<2$, $R=\varnothing$.
:::

Đặc tả là một trường hợp của Định nghĩa 01.1: miền đầu vào là các bộ $(N,C_1,\ldots,C_N,\tau)$ thỏa điều kiện trên, và $\mathrm{Out}$ của mỗi đầu vào gồm mọi cách liệt kê $R$ không lặp. Điều kiện $i<j$ loại cặp một tài liệu với chính nó và chọn một trong hai thứ tự $(i,j)$, $(j,i)$ của cùng một cặp. Dấu $\ge$ nghĩa là cặp có $\mathrm{SIM}=\tau$ phải được trả. Yêu cầu có hai chiều: mọi cặp được trả đều đạt ngưỡng, và mọi cặp đạt ngưỡng đều được trả.

Từ đặc tả tới một con số đo được còn nhiều tầng. Bảng sau tách chúng ra trên chính bài toán này.

| Tầng | Nội dung trong bài toán cặp gần trùng |
|---|---|
| Đặc tả | trả đúng tập $R$ của Định nghĩa 01.10 |
| Biểu diễn | mỗi $C_i$ lưu thành danh sách tăng dần, không lặp |
| Thuật toán | duyệt các cặp $i<j$, tính $\mathrm{SIM}$ chính xác, xuất cặp đạt ngưỡng |
| Cài đặt | kiểu phần tử, phép so sánh, cách đọc tệp, cách so với ngưỡng |
| Kết quả thực nghiệm | các cặp và thời gian đo được trên một kho và một máy cụ thể |

Một lần chạy đúng trên một kho không chứng minh thuật toán đúng trên mọi đầu vào, và một lần chạy nhanh không chứng minh một cận tiệm cận.

### 3.3 Thuật toán xét mọi cặp

Cách trực tiếp là xét lần lượt mọi cặp $i<j$ theo hai vòng lặp lồng nhau, tính $\mathrm{SIM}$ và xuất cặp đạt ngưỡng. Trước khi viết giả mã, xem thứ tự các cặp và một vết chạy tay.

::: example Ví dụ 01.7 (Thứ tự xét cặp và một vết chạy)
**Dữ kiện.** (a) $N=4$, tập bất kỳ. (b) $N=3$ với $C_1,C_2$ của Ví dụ 01.6, $\mathrm{SIM}(C_1,C_2)=3/8$; giả sử $C_3=C_1$; ngưỡng $\tau=1/2$.

**Thứ tự với $N=4$.** Vòng lặp ngoài chạy $i=1,2,3$; vòng lặp trong chạy $j=i+1,\ldots,4$. Các cặp được xét theo thứ tự
$$
\begin{gathered}
(1,2),\ (1,3),\ (1,4),\\
(2,3),\ (2,4),\ (3,4),
\end{gathered}
$$
tức $3+2+1=6=\binom42$ cặp, mỗi cặp $i<j$ đúng một vòng.

**Vết chạy với $N=3$.**

| Vòng | Cặp | $\mathrm{SIM}$ | So với $\tau=1/2$ | Kết quả sau vòng |
|---:|---|---|---|---|
| 0 | | | | $\varnothing$ |
| 1 | $(1,2)$ | $3/8$ | nhỏ hơn, không xuất | $\varnothing$ |
| 2 | $(1,3)$ | $\mathrm{SIM}(C_1,C_1)=1$ | không nhỏ hơn, xuất | $\{(1,3)\}$ |
| 3 | $(2,3)$ | $\mathrm{SIM}(C_2,C_1)=3/8$ | nhỏ hơn, không xuất | $\{(1,3)\}$ |

Sau vòng 3, vòng lặp trong hết vì $j=3=N$ và vòng lặp ngoài hết vì $i=2=N-1$; thuật toán dừng.

**Kiểm tra lại.** Theo Định nghĩa 01.10, $R=\{(1,3)\}$: chỉ cặp $(1,3)$ có $\mathrm{SIM}\ge1/2$. Với $\tau=1/2$, phép so số nguyên ở cặp $(1,2)$ là $3\cdot2=6<1\cdot8=8$, cho cùng quyết định không xuất.
:::

::: algorithm Thuật toán 01.11 (Xét mọi cặp)
**Đầu vào.** $N$, $C_1,\ldots,C_N$, $\tau$ như Định nghĩa 01.10.

**Đầu ra.** Các cặp của $R$, xuất dần, mỗi cặp một lần.

**Giả thiết.** Bước 4 tính chính xác $\mathrm{SIM}(C_i,C_j)$ và bước 5 so chính xác với $\tau$.

1. Nếu $N<2$, dừng với kết quả rỗng.
2. Với $i=1,2,\ldots,N-1$:
3. $\quad$ với $j=i+1,\ldots,N$:
4. $\quad\quad$ tính $\mathrm{SIM}(C_i,C_j)$;
5. $\quad\quad$ nếu $\mathrm{SIM}(C_i,C_j)\ge\tau$, xuất cặp $(i,j)$.

**Dừng.** Sau vòng $i=N-1$, $j=N$; hai vòng lặp có số vòng hữu hạn.

**Trường hợp biên.** $N<2$ trả rỗng ở bước 1. Với $\tau=0$, mọi cặp được xuất; với $\tau=1$, chỉ các cặp $C_i=C_j$ được xuất. Cặp có $\mathrm{SIM}=\tau$ được xuất.

**Chi phí.** Bước 4–5 chạy $\binom N2$ vòng; mỗi vòng tốn chi phí tính $\mathrm{SIM}$ trên biểu diễn đã chọn của các tập.
:::

~~~text
nếu N < 2:
    kết thúc với kết quả rỗng
cho i = 1, ..., N−1:
    cho j = i+1, ..., N:
        tính chính xác SIM(Cᵢ, Cⱼ)
        nếu SIM(Cᵢ, Cⱼ) ≥ τ:
            xuất cặp (i, j)
~~~

Phép quyết định của thuật toán nằm ở bước 5: một cặp được xuất khi và chỉ khi nó đạt ngưỡng. Giả mã để mở cách tính $\mathrm{SIM}$ ở bước 4. Vết chạy của Ví dụ 01.7(b) là ba vòng của bước 4–5 với $N=3$.

::: proposition Mệnh đề 01.12 (Tính đúng của Thuật toán 01.11)
**Giả thiết.** Đầu vào thuộc miền của Định nghĩa 01.10: $N\ge0$, mọi $C_i$ hữu hạn và không rỗng, $\tau\in[0,1]$. Bước 4–5 quyết định chính xác $\mathrm{SIM}(C_i,C_j)\ge\tau$.

**Kết luận.** Thuật toán 01.11 dừng sau đúng $\binom N2$ vòng của bước 4–5 và xuất đúng tập $R$, mỗi cặp một lần.

**Điều kiện áp dụng.** Phép kiểm ở bước 5 là phép so chính xác; cài đặt bằng số dấu phẩy động phải được kiểm riêng ở gần ngưỡng.

**Phạm vi.** Tính đúng của đầu ra trên mọi đầu vào thuộc miền; mệnh đề không đếm chi phí.
:::

::: proof
Ý tưởng là một bất biến vòng lặp trên tập các cặp đã xét. Gọi $\mathcal S_\ell$ là tập $\ell$ cặp được xét đầu tiên và $\mathcal O_\ell$ là tập các cặp đã xuất sau $\ell$ vòng của bước 4–5.

**Mỗi cặp được xét đúng một vòng.** Vòng của bước 4–5 ứng với giá trị $(i,j)$ của hai biến lặp, với $1\le i\le N-1$ và $i+1\le j\le N$. Điều kiện đó tương đương $1\le i<j\le N$, nên các vòng ứng một–một với các cặp của miền trong Định nghĩa 01.10. Số vòng là
$$
\begin{aligned}
\sum_{i=1}^{N-1}(N-i)&=\frac{N(N-1)}{2}\\
&=\binom N2,
\end{aligned}
$$
hữu hạn, nên thuật toán dừng.

**Bất biến đúng khi bắt đầu.** Bất biến cần giữ là: $\mathcal O_\ell=R\cap\mathcal S_\ell$ và mỗi cặp của $\mathcal O_\ell$ đã được xuất đúng một lần. Với $\ell=0$, $\mathcal S_0=\mathcal O_0=\varnothing$, nên bất biến đúng.

**Bất biến được giữ qua mỗi vòng.** Giả sử bất biến đúng sau $\ell$ vòng, và vòng $\ell+1$ xét cặp $(i,j)$. Theo phần đầu của chứng minh, $(i,j)\notin\mathcal S_\ell$, nên $(i,j)$ chưa được xuất. Có hai trường hợp, căn cứ vào phép kiểm chính xác ở bước 5:

- nếu $\mathrm{SIM}(C_i,C_j)\ge\tau$ thì $(i,j)\in R$, thuật toán xuất $(i,j)$ một lần, và $\mathcal O_{\ell+1}=(R\cap\mathcal S_\ell)\cup\{(i,j)\}=R\cap\mathcal S_{\ell+1}$;
- nếu $\mathrm{SIM}(C_i,C_j)<\tau$ thì $(i,j)\notin R$, thuật toán không xuất, và $\mathcal O_{\ell+1}=R\cap\mathcal S_\ell=R\cap\mathcal S_{\ell+1}$.

Các cặp đã xuất trước đó không bị xuất lại, nên bất biến đúng sau vòng $\ell+1$.

**Khi dừng, kết quả bằng $R$.** Sau $\binom N2$ vòng, $\mathcal S_\ell$ là toàn bộ miền cặp, nên $\mathcal O_\ell=R$, mỗi cặp một lần. Khi $N<2$, bước 1 của thuật toán trả rỗng, và $R=\varnothing$ theo Định nghĩa 01.10. $\square$
:::

![Sáu cặp của bốn tài liệu xếp theo thứ tự xét; ba cặp đầu thuộc phần đã xét, ba cặp sau thuộc phần chưa xét; kết quả đang có gồm đúng các cặp đạt ngưỡng trong phần đã xét.](img/lec-01/danh-gia-tinh-dung.svg)

Hình chụp trạng thái sau $\ell=3$ vòng với $N=4$: $\mathcal S_3=\{(1,2),(1,3),(1,4)\}$, và kết quả đang có là $R\cap\mathcal S_3$. Bất biến của chứng minh là tính chất chung của mọi trạng thái như vậy, với $\ell=0,1,\ldots,6$; cột "Kết quả sau vòng" của Ví dụ 01.7(b) là $R\cap\mathcal S_\ell$ với $\ell=0,1,2,3$.

Các giả thiết của Mệnh đề 01.12 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "tập không rỗng": với $C_1=C_2=\varnothing$, bước 4 tính $0/0$ và không có giá trị để so với $\tau$.
- Bỏ "phép kiểm chính xác": một cài đặt làm tròn $\mathrm{SIM}$ có thể xuất một cặp có $\mathrm{SIM}$ nhỏ hơn $\tau$ một chút, hoặc bỏ một cặp có $\mathrm{SIM}=\tau$. Với $\tau=a/c$, phép so số nguyên $|C\cap C'|\cdot c\ge a\cdot|C\cup C'|$ tương đương $\mathrm{SIM}(C,C')\ge\tau$ và không làm tròn.
- Bỏ điều kiện $j>i$ của vòng lặp trong: thuật toán xuất cả cặp $(i,i)$ và cả hai thứ tự của một cặp (Bài tập 01.5).

Phần "mỗi cặp được xét đúng một vòng" dùng điều kiện $i<j$ của hai vòng lặp; phần "bất biến được giữ" dùng giả thiết tập không rỗng để $\mathrm{SIM}$ xác định và giả thiết phép kiểm chính xác để chia hai trường hợp.

**Trong thực hành.** Thuật toán xuất từng cặp ngay khi kiểm, nên không phải giữ toàn bộ $R$ trong bộ nhớ; việc ghi $R$ vẫn tốn chi phí. Phép so bằng số nguyên ở trên thỏa đúng giả thiết phép kiểm chính xác; cài đặt chia hai số thực rồi so với $\tau$ cần được kiểm thử ở các cặp có $\mathrm{SIM}$ gần $\tau$.

<!-- note-topic-id: lec-01-topic-04 -->
### 3.4 Mô hình chi phí và chi phí của xét mọi cặp

Mệnh đề 01.12 cho tính đúng; để biết thuật toán có chạy xong trong ngân sách, xét số liệu của MMDS (Ví dụ 3.10, tr.92). Kho có $10^6$ tài liệu; mỗi tài liệu đã được thay bằng một **chữ ký** (signature), tức một dãy ngắn các giá trị thay cho tập đoạn ký tự của tài liệu, ở đây dài 250 phần tử và chiếm 1000 byte. Cả kho chữ ký chiếm $10^6\cdot1000=10^9$ byte, vừa bộ nhớ chính của một máy tính xách tay; trên đĩa, nó chiếm $F=\lceil10^9/65\,536\rceil=15\,259$ khối, và theo Mệnh đề 01.5(a), đọc vào bộ nhớ chỉ tốn một lượt quét, tức $15\,259$ lần truyền khối. Nếu so một cặp chữ ký mất 1 micro giây, so mọi cặp mất
$$
\begin{aligned}
\binom{10^6}{2}\cdot10^{-6}\ \text{giây}&=499\,999{,}5\ \text{giây}\\
&\approx5{,}79\ \text{ngày}.
\end{aligned}
$$
Đọc ghi tốn một lượt quét, bộ nhớ đủ, còn tính toán tốn gần sáu ngày. Để chỉ ra giới hạn nằm ở đại lượng nào, chúng ta cần tách các đại lượng tài nguyên.

::: definition Định nghĩa 01.13 (Mô hình chi phí)
Một **mô hình chi phí** chọn một đại lượng và một đơn vị đếm đại lượng đó. Các đại lượng dùng trong học phần:

| Đại lượng | Đơn vị đếm hoặc điều kiện |
|---|---|
| Khối lượng tính toán | số phép toán cơ bản, ví dụ số phép so sánh phần tử, theo kích thước đầu vào |
| Bộ nhớ làm việc | dung lượng lớn nhất phải giữ đồng thời: trạng thái, dữ liệu đang dùng, bộ đệm |
| Đọc ghi và lượt quét | số lần truyền khối và số lượt đọc toàn bộ dữ liệu (Định nghĩa 01.4) |
| Dữ liệu mạng | lượng dữ liệu trao đổi giữa các máy |
| Dung lượng lưu trữ | dữ liệu đã lưu cùng phần phụ trợ, như thông tin giải mã hay chỉ mục |
| Độ trễ truy vấn | thời gian từ lúc nhận một truy vấn tới lúc trả kết quả |
| Chi phí xây dựng | thời gian và bộ nhớ để tạo một cấu trúc trước khi trả truy vấn |
| Chi phí cập nhật | công việc để phản ánh một thay đổi dữ liệu vào dữ liệu gốc và mọi cấu trúc phụ thuộc |
| Chất lượng | sai lệch của kết quả so với đặc tả, khi đặc tả cho phép kết quả gần đúng |
:::

Mỗi dòng là một mô hình riêng; con số của hai dòng không cộng được với nhau khi chưa có một mục tiêu chung. Hai cặp dễ nhầm là bộ nhớ làm việc (working memory) với dung lượng lưu trữ, và độ trễ (latency) với thông lượng (throughput), tức số truy vấn hoàn tất trong một đơn vị thời gian. Để đếm khối lượng tính toán của Thuật toán 01.11, ta cần chọn cách tính $\mathrm{SIM}$ ở bước 4.

Với biểu diễn danh sách tăng ngặt, giao và hợp của hai tập $C,C'$ tính được bằng **thủ tục trộn** hai con trỏ:

1. đặt mỗi con trỏ ở đầu một danh sách và biến đếm $\gamma=0$;
2. trong khi cả hai con trỏ chưa đi hết danh sách, so hai phần tử đang trỏ $w\in C$, $w'\in C'$: nếu $w=w'$ thì tăng $\gamma$ và tiến cả hai con trỏ; nếu $w<w'$ thì tiến con trỏ trên $C$; nếu $w>w'$ thì tiến con trỏ trên $C'$.

::: lemma Bổ đề 01.14 (Đếm giao và hợp bằng thủ tục trộn)
**Giả thiết.** Các phần tử thuộc một tập có thứ tự toàn phần; $C$ và $C'$ được lưu thành hai danh sách tăng ngặt; một phép so sánh hai phần tử trả một trong ba kết quả $<$, $=$, $>$.

**Kết luận.** Thủ tục trộn dừng sau không quá $|C|+|C'|$ phép so sánh, và khi dừng $\gamma=|C\cap C'|$; do đó $|C\cup C'|=|C|+|C'|-\gamma$.

**Điều kiện áp dụng.** Hai danh sách đã được sắp và không có phần tử lặp.

**Phạm vi.** Không tính chi phí tạo và sắp các danh sách.
:::

::: proof
**Số phép so sánh không quá $|C|+|C'|$.** Mỗi phép so sánh tiến ít nhất một con trỏ. Hai con trỏ tiến tổng cộng không quá $|C|+|C'|$ bước, nên có không quá $|C|+|C'|$ phép so sánh.

**Bất biến của thủ tục.** Gọi phần tử *đã qua* là phần tử đứng trước con trỏ trên danh sách của nó. Bất biến: mọi phần tử đã qua của mỗi danh sách nhỏ hơn phần tử đang trỏ của danh sách kia, và $\gamma$ bằng số phần tử chung trong các phần tử đã qua. Ban đầu chưa có phần tử nào đã qua và $\gamma=0$. Nếu $w<w'$: các phần tử đã qua của $C'$ nhỏ hơn $w$ theo bất biến, các phần tử còn lại của $C'$ không nhỏ hơn $w'>w$, nên $w\notin C'$ và $\gamma$ không đổi là đúng; vì $C$ tăng ngặt, phần tử trỏ mới của $C$ lớn hơn $w$, nên bất biến được giữ. Trường hợp $w>w'$ đối xứng. Nếu $w=w'$: phần tử này chung và được đếm một lần; hai danh sách tăng ngặt nên bất biến được giữ.

**Khi dừng, $\gamma=|C\cap C'|$.** Khi một danh sách, chẳng hạn $C$, đã đi hết, mọi phần tử còn lại $z$ của $C'$ không nhỏ hơn phần tử đang trỏ của $C'$, mà phần tử này lớn hơn mọi phần tử của $C$ theo bất biến; vậy $z\notin C$. Do đó $\gamma=|C\cap C'|$, và công thức của hợp suy ra từ $|C\cup C'|=|C|+|C'|-|C\cap C'|$. $\square$
:::

Với $\gamma=|C_i\cap C_j|$, bước 5 của Thuật toán 01.11 với $\tau=a/c$ là phép so số nguyên $\gamma\,c\ge a\,(|C_i|+|C_j|-\gamma)$, tốn hằng số phép toán. Chi phí của cả thuật toán bằng số vòng nhân chi phí mỗi vòng.

::: proposition Mệnh đề 01.15 (Chi phí của xét mọi cặp)
**Giả thiết.** Mỗi $C_i$ được lưu thành danh sách tăng ngặt có không quá $L$ phần tử; bước 4 của Thuật toán 01.11 dùng thủ tục trộn của Bổ đề 01.14.

**Kết luận.** Phần xét cặp của Thuật toán 01.11 dùng không quá
$$
\binom N2\cdot2L=N(N-1)L
$$
phép so sánh phần tử, tức $O(N^2L)$.

**Điều kiện áp dụng.** Mô hình chi phí là khối lượng tính toán, đếm phép so sánh phần tử; mọi tập nằm trong bộ nhớ.

**Phạm vi.** Đây là cận trên trong trường hợp xấu nhất của phần xét cặp. Cận chưa tính chi phí tạo và sắp các tập, chi phí ghi $R$, và chi phí đọc ghi khi các tập nằm trên đĩa.
:::

::: proof
**Có $\binom N2$ vòng.** Theo Mệnh đề 01.12, bước 4–5 chạy đúng $\binom N2$ vòng.

**Mỗi vòng tốn không quá $2L$ phép so sánh.** Theo Bổ đề 01.14, vòng xét $(i,j)$ dùng không quá $|C_i|+|C_j|\le2L$ phép so sánh.

**Tổng không quá $N(N-1)L$.** Nhân hai số trên: $\binom N2\cdot2L=\frac{N(N-1)}{2}\cdot2L=N(N-1)L\le N^2L$. $\square$
:::

Bảng sau đếm từng bước của Thuật toán 01.11.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| Kiểm $N<2$ (bước 1) | 1 | $O(1)$ | $O(1)$ |
| Trộn hai danh sách (bước 4) | $\binom N2$ | $\le2L$ phép so sánh | $\le N(N-1)L$ |
| So $\gamma c\ge a(\lvert C_i\rvert+\lvert C_j\rvert-\gamma)$ (bước 5) | $\binom N2$ | $O(1)$ | $O(N^2)$ |
| Xuất một cặp (bước 5) | $\lvert R\rvert$ | $O(1)$ | $O(\lvert R\rvert)$ |

Vì $|R|\le\binom N2$, hàng cuối không vượt hai hàng giữa, và tổng là $O(N^2L)$.

::: example Ví dụ 01.8 (Kho một triệu tài liệu)
**Dữ kiện.** $N=10^6$; mỗi tập có không quá $L$ phần tử.

**Số vòng kiểm.** $\binom{10^6}{2}=499\,999\,500\,000$.

**Cận số phép so sánh.** Theo Mệnh đề 01.15, $N(N-1)L=999\,999\,000\,000\cdot L$, khoảng $10^{12}L$.

**Khi kho tăng gấp đôi.** $\binom{2\cdot10^6}{2}\big/\binom{10^6}{2}=3\,999\,998/999\,999\approx4{,}000002$: số vòng kiểm tăng gần bốn lần.

**Kiểm tra lại.** $2\cdot499\,999\,500\,000=999\,999\,000\,000=10^6(10^6-1)$.
:::

Cận $O(N^2L)$ bị chi phối bởi thừa số $N^2$: với $N$ cố định, rút gọn mỗi tập chỉ giảm $L$, còn số vòng vẫn là $\binom N2$. Vì vậy chữ ký 1000 byte của MMDS Ví dụ 3.10 vẫn cần gần sáu ngày.

**Trong thực hành.** Ba điểm sau giới hạn việc dùng Mệnh đề 01.15 cho một hệ thống thật.

- Nếu $R$ chứa bậc $N^2$ cặp, chẳng hạn khi $\tau=0$, riêng việc ghi $R$ đã tốn bậc $N^2$ thao tác.
- Khi các tập nằm trên đĩa, chi phí đọc ghi theo Mệnh đề 01.5 phải được đếm riêng.
- Khi công việc chia trên nhiều máy, CS246 đo chi phí truyền thông (communication cost) bằng tổng dữ liệu vào ra của mọi tiến trình. Mô hình MapReduce gồm tác vụ Map tính đóng góp tại nơi lưu dữ liệu và tác vụ Reduce gộp các đóng góp cùng khóa; với mô hình này, chi phí truyền thông là kích thước tệp đầu vào, cộng hai lần tổng kích thước các tệp chuyển từ tác vụ Map sang tác vụ Reduce, cộng kích thước đầu ra của tác vụ Reduce (CS246, trang chiếu 67–68). Chi phí này được tính riêng với chi phí tính toán (trang chiếu 69).

### 3.5 Ứng viên, xác minh và độ thu hồi

Ví dụ 01.8 cho thấy muốn giảm chi phí phải giảm số cặp được kiểm. Một hướng là chọn trước một tập **cặp ứng viên** (candidate pair) $A$ nhỏ hơn nhiều so với $\binom N2$, rồi chỉ tính $\mathrm{SIM}$ chính xác trên các cặp của $A$; bước tính chính xác này gọi là **xác minh** (verification). MMDS (tr.73) chọn ứng viên bằng băm: hai tài liệu thành cặp ứng viên khi chúng rơi vào cùng một thùng (Định nghĩa 01.8) của ít nhất một trong nhiều hàm băm. Xác minh loại được các ứng viên không đạt ngưỡng, còn cặp đạt ngưỡng nằm ngoài $A$ thì không bước nào xét tới. Mệnh đề sau nói chính xác điều đó.

::: proposition Mệnh đề 01.16 (Xác minh ứng viên)
**Giả thiết.** $R$ là tập của Định nghĩa 01.10; $A$ là một tập bất kỳ các cặp $(i,j)$ với $1\le i<j\le N$; bước xác minh tính chính xác $\mathrm{SIM}(C_i,C_j)$ cho mọi $(i,j)\in A$ và trả tập $\widehat R$ các cặp của $A$ đạt ngưỡng.

**Kết luận.**

- (a) $\widehat R=A\cap R$.
- (b) $\widehat R\subseteq R$: mọi cặp được trả đều đạt ngưỡng.
- (c) $\widehat R=R$ khi và chỉ khi $R\subseteq A$.

**Điều kiện áp dụng.** Phép kiểm chính xác như trong Mệnh đề 01.12.

**Phạm vi.** Mệnh đề đúng với mọi tập $A$, bất kể cách tạo; chi phí tạo $A$ được tính riêng.
:::

::: proof
**(a) $\widehat R=A\cap R$.** Một cặp $(i,j)$ thuộc $\widehat R$ khi và chỉ khi $(i,j)\in A$ và $\mathrm{SIM}(C_i,C_j)\ge\tau$ [do phép kiểm chính xác], tức $(i,j)\in A$ và $(i,j)\in R$ [do Định nghĩa 01.10].

**(b) $\widehat R\subseteq R$.** Suy từ (a) vì $A\cap R\subseteq R$.

**(c), chiều đảo.** Nếu $R\subseteq A$ thì $A\cap R=R$, nên $\widehat R=R$ theo (a).

**(c), chiều thuận.** Nếu $\widehat R=R$ thì $R=A\cap R\subseteq A$. $\square$
:::

::: example Ví dụ 01.9 (Một cặp sai bị loại, một cặp đúng bị bỏ sót)
**Dữ kiện.** $N=3$; $R=\{(1,2),(2,3)\}$; tập ứng viên $A=\{(1,2),(1,3)\}$.

**Xác minh.** $(1,2)$ đạt ngưỡng, được trả; $(1,3)$ không đạt ngưỡng, bị loại.

**Kết quả.** $\widehat R=A\cap R=\{(1,2)\}$.

**Kiểm tra lại.** $(2,3)\in R$ nhưng $(2,3)\notin A$, nên $R\not\subseteq A$ và $\widehat R\ne R$, đúng Mệnh đề 01.16(c). Tỷ lệ cặp đúng được trả là $|\widehat R\cap R|/|R|=|\widehat R|/|R|=1/2$.
:::

Cặp $(1,3)$ của Ví dụ 01.9 là một **dương giả** (false positive, FP) của bước chọn ứng viên, còn gọi là *ứng viên giả*: được chọn nhưng không đạt ngưỡng, và bước xác minh loại nó. Cặp $(2,3)$ là một **âm giả** (false negative, FN), còn gọi là *cặp bỏ sót*: đạt ngưỡng nhưng không được chọn, và không bước nào sau đó tìm lại được nó. Với băm nhạy cảm theo tính cục bộ (locality-sensitive hashing, LSH), tỷ lệ âm giả giảm khi xét nhiều cặp ứng viên hơn (MMDS, tr.73).

Khi đầu ra chỉ chứa một phần kết quả đúng, chúng ta cần một đại lượng đo phần đó. Với bài toán cặp, đại lượng ấy là *độ thu hồi* (recall) $|\widehat R\cap R|/|R|$ khi $R\ne\varnothing$, bằng $|\widehat R|/|R|$ khi xác minh chính xác (Mệnh đề 01.16(b)), như $1/2$ ở Ví dụ 01.9. Bài toán hàng xóm gần nhất của Định nghĩa 01.2 dùng đại lượng tương tự.

::: definition Định nghĩa 01.17 (Độ thu hồi tại $k$)
Cho véc-tơ truy vấn $\mathbf y$, tập $k$ hàng xóm gần nhất chính xác $\mathcal N_k(\mathbf y)$ của Định nghĩa 01.2, và tập $\widehat{\mathcal N}_k(\mathbf y)$ gồm $k$ chỉ số phân biệt do một phương pháp trả về. **Độ thu hồi tại $k$** (recall@k) là
$$
\begin{aligned}
&\operatorname{recall@}k(\mathbf y)\\
&\quad=\frac{|\widehat{\mathcal N}_k(\mathbf y)\cap\mathcal N_k(\mathbf y)|}{k}.
\end{aligned}
$$
:::

Tử số đếm các hàng xóm thật được trả lại; vì cả hai tập đều có $k$ phần tử, mẫu số $k$ cũng là số hàng xóm thật. Độ thu hồi bằng 1 khi và chỉ khi phương pháp trả đúng $\mathcal N_k(\mathbf y)$. Định nghĩa phụ thuộc quy tắc phá hòa của Định nghĩa 01.2, vì quy tắc này quyết định $\mathcal N_k(\mathbf y)$.

::: example Ví dụ 01.10 (Ba trong năm hàng xóm thật)
**Dữ kiện.** $k=5$; $\mathcal N_5(\mathbf y)=\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$; phương pháp trả $\widehat{\mathcal N}_5(\mathbf y)=\{\mathrm c,\mathrm d,\mathrm e,\mathrm f,\mathrm g\}$.

**Giao.** $\{\mathrm c,\mathrm d,\mathrm e\}$, ba phần tử.

**Độ thu hồi.** $\operatorname{recall@}5(\mathbf y)=3/5$.

**Kiểm tra lại.** Hai hàng xóm thật $\mathrm a,\mathrm b$ bị thiếu, hai kết quả $\mathrm f,\mathrm g$ nằm ngoài tập đúng; $3+2=5$ ở cả hai tập.
:::

![Hai tập năm phần tử: tập đúng a, b, c, d, e và tập trả về c, d, e, f, g; ba phần tử chung c, d, e; a, b bị thiếu, f, g nằm ngoài tập đúng.](img/lec-01/danh-gia-do-thu-hoi.svg)

Hình đặt hai tập cạnh nhau: phần giao là ba hàng xóm được tìm lại; hai mục $\mathrm f,\mathrm g$ không bù được cho hai hàng xóm thật $\mathrm a,\mathrm b$, như cặp ứng viên giả không bù được cặp bỏ sót ở Ví dụ 01.9.

::: exercise Bài tập 01.5 (Vòng lặp trong bắt đầu từ $j=1$)
Trong Thuật toán 01.11, vòng lặp trong bị sửa thành $j=1,\ldots,N$. Chạy thuật toán đã sửa với $N=2$, $C_1,C_2$ của Ví dụ 01.6 ($\mathrm{SIM}(C_1,C_2)=3/8$) và $\tau=1/4$. Thuật toán vi phạm phần nào của Định nghĩa 01.10, và phần nào của chứng minh Mệnh đề 01.12 không còn đúng?
:::

::: hint
Tính $\mathrm{SIM}(C_1,C_1)$ và liệt kê các giá trị $(i,j)$ mà hai vòng lặp đi qua.
:::

::: solution
**Vết chạy.** Vòng lặp ngoài chỉ có $i=1$. Với $j=1$: $\mathrm{SIM}(C_1,C_1)=1\ge1/4$, xuất $(1,1)$. Với $j=2$: $\mathrm{SIM}(C_1,C_2)=3/8\ge1/4$, xuất $(1,2)$. Đầu ra là $\{(1,1),(1,2)\}$.

**Vi phạm đặc tả.** $(1,1)$ không thỏa $i<j$. Với $N\ge3$, thuật toán còn xuất cả $(1,2)$ và $(2,1)$ khi cặp đó đạt ngưỡng, nên một cặp xuất hiện hai lần. Vì mọi $C_i$ không rỗng, $\mathrm{SIM}(C_i,C_i)=1\ge\tau$ với mọi $\tau\in[0,1]$, nên cặp tự so luôn được xuất.

**Phần hỏng của chứng minh.** Phần "mỗi cặp được xét đúng một vòng": các vòng không còn ứng một–một với các cặp $1\le i<j\le N$.

**Kiểm tra lại.** Theo Định nghĩa 01.10, $R=\{(1,2)\}$; đầu ra đã sửa có thêm $(1,1)$.
:::

::: exercise Bài tập 01.6 (Mọi ngưỡng giữ một cặp)
Cặp $(1,2)$ có $\mathrm{SIM}(C_1,C_2)=3/8$. Xác định mọi $\tau\in[0,1]$ để $(1,2)\in R$, và viết phép so số nguyên tương ứng khi $\tau=a/c$.
:::

::: hint
Định nghĩa 01.10 dùng dấu $\ge$.
:::

::: solution
**Tập ngưỡng.** $(1,2)\in R$ khi và chỉ khi $3/8\ge\tau$, tức $\tau\in[0,3/8]$, kể cả $\tau=3/8$.

**Phép so số nguyên.** Với $|C_1\cap C_2|=3$, $|C_1\cup C_2|=8$ và $\tau=a/c$: $3c\ge8a$.

**Kiểm tra lại.** $\tau=3/8$: $3\cdot8=24\ge8\cdot3=24$, cặp được giữ; $\tau=2/5$: $3\cdot5=15<8\cdot2=16$, cặp bị loại, đúng vì $2/5>3/8$.
:::

::: exercise Bài tập 01.7 (Bộ lọc và xác minh chính xác)
Một bộ lọc chọn tập ứng viên $A$ nhưng không bảo đảm chọn mọi cặp đạt ngưỡng. Bước sau tính Jaccard chính xác cho mọi cặp trong $A$. Có thể cam kết trả đúng tập $R$ của Định nghĩa 01.10 không? Nêu điều kiện cần thêm.
:::

::: hint
Dùng Mệnh đề 01.16(c) và Ví dụ 01.9.
:::

::: solution
**Kết luận.** Không. Theo Mệnh đề 01.16(a), đầu ra là $A\cap R$; theo (c), đầu ra bằng $R$ khi và chỉ khi $R\subseteq A$, và bộ lọc không bảo đảm điều này.

**Phản ví dụ.** Ví dụ 01.9: $(2,3)\in R\setminus A$ không bao giờ được xác minh.

**Điều kiện cần thêm.** Hoặc bộ lọc bảo đảm $R\subseteq A$, hoặc đặc tả được đổi sang gần đúng, nêu rõ độ thu hồi $|\widehat R\cap R|/|R|$ chấp nhận được, bằng $|\widehat R|/|R|$ khi xác minh chính xác (Mệnh đề 01.16(b)).

**Kiểm tra lại.** Phép kiểm chính xác chỉ bảo đảm (b): mọi cặp được trả đều đạt ngưỡng.
:::

Như vậy, chúng ta đã đặc tả bài toán cặp gần trùng (Định nghĩa 01.9, 01.10), chứng minh Thuật toán 01.11 trả đúng $R$ (Mệnh đề 01.12), đếm chi phí $N(N-1)L$ phép so sánh của nó (Bổ đề 01.14, Mệnh đề 01.15), và chỉ ra rằng bước xác minh trả đủ $R$ khi và chỉ khi $R\subseteq A$ (Mệnh đề 01.16). Tuy nhiên, Mệnh đề 01.16 chỉ nêu điều kiện mà tập $A$ phải thỏa; cách tạo $A$, cũng như lời giải cho các giới hạn dòng, nén và đọc ghi của Mục 1–2, cần những phương pháp riêng. Trong Mục 4, chúng ta gắn từng giới hạn đã gặp với nhóm bài xử lý nó và với kiến thức nền mà nhóm bài đó cần.

<!-- note-topic-id: lec-01-topic-05 -->
## 4. Năm nhóm thuật toán và cách học

Ba giới hạn sau đã xuất hiện với số liệu cụ thể, và thuật toán trực tiếp không vượt qua được giới hạn nào:

- bài toán cặp gần trùng với $N=10^6$ tài liệu có $499\,999\,500\,000$ cặp (Ví dụ 01.8);
- bảng đăng ký `takes` chiếm 400 khối trong khi bộ nhớ chỉ có 20 khối (Mục 2.4);
- bản ghi truy vấn và thư đến liên tục, mỗi bản ghi phải được xử lý khi đến (Mục 2.2).

Mỗi giới hạn vi phạm một thành phần ngân sách khác nhau của Định nghĩa 01.1.

### 4.1 Giới hạn, nhóm bài và thuộc tính cần đánh giá

![Sơ đồ học phần: Bài 01, nền chung về đầu ra, tài nguyên và bảo đảm, nối tới năm nhóm bài liền nhau: Bài 02–04 phân tán và xếp hạng; Bài 05–07 tương đồng và tìm gần; Bài 08–09 dòng và cửa sổ; Bài 10–11 nén và khôi phục; Bài 12–15 lưu trữ và truy vấn.](img/lec-01/ban-do-hoc-phan.svg)

Sơ đồ đặt Bài 01 ở gốc và năm nhóm bài ở năm nhánh; các bài trong một nhóm được học liền nhau. Bảng sau ghi, cho từng bài, phương pháp sẽ học và thuộc tính mà lời giải phải được đánh giá theo, dùng các đại lượng của Định nghĩa 01.13.

| Bài | Phương pháp | Bài toán và thuộc tính cần đánh giá |
|---:|---|---|
| 02 | MapReduce: ánh xạ, nhóm theo khóa, rút gọn | tổng hợp trên kho phân tán; mỗi đóng góp được tính đúng một lần, dữ liệu mạng |
| 03 | PageRank: phép lặp, xử lý nút cụt (dead end) và bẫy nhện (spider trap) | xếp hạng trang; điều kiện hội tụ, tiêu chuẩn dừng, chi phí mỗi vòng |
| 04 | PageRank theo chủ đề, TrustRank, khối lượng rác (spam mass), HITS | chủ đề và liên kết rác; giả thiết về tín hiệu, giới hạn diễn giải |
| 05 | Đoạn ký tự, Jaccard, MinHash | biểu diễn gần trùng; xác suất hai giá trị MinHash bằng nhau |
| 06 | LSH: phân dải và khuếch đại | tạo tập ứng viên $A$; xác suất thành ứng viên, âm giả, số cặp phải xác minh |
| 07 | Đồ thị thế giới nhỏ phân tầng (hierarchical navigable small world, HNSW), lượng tử hóa tích (product quantization, PQ), chỉ mục phân vùng kết hợp PQ (IVF-PQ) | $k$ hàng xóm gần đúng; độ thu hồi, độ trễ, bộ nhớ, chi phí xây dựng |
| 08 | Lấy mẫu theo khóa, lấy mẫu hồ chứa, bộ lọc Bloom | dòng dữ liệu; đơn vị mẫu, trạng thái, sai số một phía |
| 09 | Flajolet–Martin, Count-Min, AMS, DGIM, suy giảm mũ | thống kê trên dòng; đại lượng ước lượng, cửa sổ, sai số, bộ nhớ |
| 10 | Huffman tĩnh, Huffman thích nghi, mã số học | nén không mất thông tin; độ dài mã, thông tin giải mã |
| 11 | LZ77, LZ78, LZW; JPEG | nén bằng từ điển và nén ảnh; khôi phục đúng hoặc sai khác cho phép |
| 12 | Sắp xếp trộn ngoài bộ nhớ, chọn thay thế | sắp tệp lớn; số lượt, số lần truyền khối, bộ đệm |
| 13 | B-Tree, B+-Tree, băm tĩnh, chỉ mục bitmap | tra theo khóa và khoảng; loại truy vấn, dung lượng, chi phí cập nhật |
| 14 | Chỉ mục đảo, R-tree, kd-tree, ball tree, Z-order | từ khóa và không gian; lọc ứng viên rồi kiểm chính xác |
| 15 | Nối vòng lặp, nối sắp xếp–trộn, nối băm, Grace Hash | nối bảng; trả mọi cặp khớp, ngân sách bộ nhớ, số lần truyền khối |

Mỗi nhóm khắc phục một giới hạn bằng một ý tưởng chung.

- **Phân tán và xếp hạng (Bài 02–04).** MapReduce tính đóng góp tại nơi lưu dữ liệu rồi gom các đóng góp cùng khóa; trong đếm từ, khóa là từ và giá trị là số lần xuất hiện.
- **Tương đồng và tìm gần (Bài 05–07).** Chữ ký MinHash và LSH tạo tập ứng viên $A$, sau đó xác minh theo Mệnh đề 01.16.
- **Dòng và cửa sổ (Bài 08–09).** Mỗi bản ghi được đọc một lần, và thuật toán chỉ giữ một trạng thái nhỏ: một mẫu, một mảng bit hay vài bộ đếm.
- **Nén và khôi phục (Bài 10–11).** Mọi bộ nén không mất thông tin phải thỏa $\mathrm{dec}(\mathrm{enc}(x))=x$ của Định nghĩa 01.7.
- **Lưu trữ và truy vấn (Bài 12–15).** Dữ liệu được sắp, được chỉ mục hay được phân hoạch sao cho mỗi truy vấn chỉ đọc ít khối, đếm theo Định nghĩa 01.4.

Quan hệ tiên quyết giữa các bài theo năm nhánh từ Bài 01:

- Bài 01 → 02 → 03 → 04;
- Bài 01 → 05 → 06 → 07;
- Bài 01 → 08 → 09;
- Bài 01 → 10 → 11;
- Bài 01 → 12 → 13 → 14, và Bài 12–13 → 15.

Một bài chỉ cần các bài đứng trước nó trên cùng nhánh, không cần toàn bộ các nhóm trước.

::: example Ví dụ 01.11 (Ghép ba giới hạn với nhóm bài)
**Dữ kiện.** Ba giới hạn đầu mục: (a) $499\,999\,500\,000$ cặp tài liệu; (b) bảng 400 khối với bộ nhớ 20 khối; (c) bản ghi đến liên tục.

**Câu (a).** Giới hạn thuộc khối lượng tính toán; chữ ký của cả kho vừa bộ nhớ (Mục 3.4). Nhóm Tương đồng và tìm gần: Bài 05 rút mỗi tập thành chữ ký, Bài 06 tạo tập ứng viên $A$ có $|A|$ nhỏ hơn nhiều so với $\binom N2$. Thuộc tính phải đánh giá: âm giả, vì theo Mệnh đề 01.16 các cặp của $R\setminus A$ bị mất.

**Câu (b).** Đại lượng chính là đọc ghi; bộ nhớ $M=20$ khối là ràng buộc. Nhóm Lưu trữ và truy vấn: Bài 15 nối hai bảng bằng các thuật toán đọc theo khối, dựa trên sắp xếp ngoài của Bài 12 và chỉ mục của Bài 13. Thuộc tính phải đánh giá: trả mọi cặp khớp và số lần truyền khối.

**Câu (c).** Giới hạn là mỗi bản ghi chỉ được đọc khi đến và trạng thái phải vừa bộ nhớ. Nhóm Dòng và cửa sổ: Bài 08 lấy mẫu và lọc, Bài 09 đếm. Thuộc tính phải đánh giá: đơn vị mẫu và sai số của từng đại lượng.

**Kiểm tra lại.** Ba giới hạn rơi vào ba nhóm khác nhau; đại lượng chính của Định nghĩa 01.13 lần lượt là khối lượng tính toán ở Câu (a), đọc ghi ở Câu (b) và bộ nhớ làm việc trên dòng ở Câu (c).
:::

<!-- note-topic-id: lec-01-topic-06 -->
### 4.2 Học phần, kiến thức nền và sản phẩm học tập

Đề cương học phần UET.DSE2053 quy định bốn chuẩn đầu ra học phần (course learning outcome, CLO):

- **CLO1:** diễn giải các nguyên lý và thuật toán cơ bản;
- **CLO2:** phân tích đặc điểm của bài toán dữ liệu quy mô lớn để chọn kỹ thuật phù hợp;
- **CLO3:** thiết kế và triển khai giải pháp bằng các thuật toán đã học;
- **CLO4:** có trách nhiệm khi thu thập, xử lý và chia sẻ dữ liệu.

Mỗi nhóm bài dùng một phần kiến thức nền riêng. Bảng sau ghi phần đó và việc nó được dùng.

| Nhóm bài | Kiến thức nền và việc được dùng |
|---|---|
| Phân tán và xếp hạng | cặp khóa–giá trị để gom đóng góp; đồ thị và ma trận để truyền điểm |
| Tương đồng và tìm gần | tập hợp để tính Jaccard; véc-tơ và khoảng cách để tìm hàng xóm |
| Dòng và cửa sổ | xác suất và kỳ vọng để phân tích mẫu và ước lượng |
| Nén và khôi phục | cây và phân phối ký hiệu để tạo mã; chuỗi và từ điển cho các cụm lặp |
| Lưu trữ và truy vấn | bản ghi, khối, cây và băm để tổ chức nơi cần đọc |

Phần cần ôn được nhận ra qua điểm chưa giải thích được: nếu chưa giải thích được vì sao $|C_1\cup C_2|=8$ trong Ví dụ 01.6, phần cần ôn là phép đếm trên tập hợp.

Mỗi kỹ năng của học phần cho một sản phẩm kiểm tra được, minh họa trên bài toán cặp gần trùng.

- **Đặc tả:** tập kết quả đúng và đủ, như $R$ của Định nghĩa 01.10.
- **Chạy tay:** trạng thái trước, thao tác và trạng thái sau trên một đầu vào nhỏ, như Ví dụ 01.7.
- **Chứng minh:** một bất biến được khởi tạo, duy trì và cho kết quả khi dừng, như Mệnh đề 01.12.
- **Phân tích chi phí:** bảng bước–số lần–chi phí–đóng góp trong một mô hình chi phí đã nêu, như Mệnh đề 01.15.
- **Báo cáo thực nghiệm:** dữ liệu, tập truy vấn, tập đúng, tham số, thiết bị và cách đo; độ thu hồi như $3/5$ của Ví dụ 01.10 đi cùng độ trễ và bộ nhớ đo trong cùng điều kiện.

Các sản phẩm này cụ thể hóa CLO1–CLO3. Một chương trình chạy đúng trên Ví dụ 01.7 chưa thay được chứng minh, vì nó chỉ kiểm một đầu vào; ca kiểm thử còn phải gồm $N<2$ và một cặp có $\mathrm{SIM}(C_i,C_j)=\tau$.

Trách nhiệm dữ liệu của CLO4 thể hiện qua cách làm việc cụ thể: ghi nguồn của thuật toán và dữ liệu, ghi phần đóng góp của từng người khi làm nhóm, báo cáo cả trường hợp bỏ sót và sai số, chỉ dùng dữ liệu được phép dùng. Trách nhiệm còn nằm ở cách diễn giải: $\mathrm{SIM}\ge\tau$ chưa đủ căn cứ để kết luận có hành vi sao chép.

::: exercise Bài tập 01.8 (Giới hạn, nhóm bài và kiến thức nền)
Với mỗi giới hạn sau, nêu nhóm bài xử lý nó và một phần kiến thức nền cần ôn cho nhóm đó.

- (a) Kho $10^{10}$ véc-tơ 3072 chiều; mỗi truy vấn $k$ hàng xóm gần nhất quét hết kho tốn $10^{10}$ phép tính khoảng cách (Ví dụ 01.2).
- (b) Một kho văn bản như chuỗi `aabaacabcabcb` phải được lưu với dung lượng nhỏ hơn và khôi phục đúng từng ký tự (Mục 2.3).
- (c) Không lưu được một véc-tơ điểm dài nhiều tỷ phần tử cho mỗi người trong một tỷ người dùng (Mục 1.2, hàng xếp hạng theo chủ đề).
:::

::: hint
Xác định trước đầu ra và đại lượng của Định nghĩa 01.13 bị vi phạm, rồi dùng bảng của Mục 4.1 và bảng kiến thức nền.
:::

::: solution
**Câu (a).** Đầu ra là $\mathcal N_k(\mathbf y)$ của Định nghĩa 01.2; đại lượng bị vi phạm là khối lượng tính toán của mỗi truy vấn, kéo theo độ trễ truy vấn. Nhóm Tương đồng và tìm gần, Bài 07. Kiến thức nền: véc-tơ và khoảng cách.

**Câu (b).** Đầu ra là bản nén thỏa $\mathrm{dec}(\mathrm{enc}(x))=x$ (Định nghĩa 01.7); đại lượng là dung lượng lưu trữ. Nhóm Nén và khôi phục, Bài 10–11. Kiến thức nền: cây và phân phối ký hiệu, chuỗi và từ điển.

**Câu (c).** Đầu ra là điểm của các trang có xét chủ đề; đại lượng bị vi phạm là dung lượng lưu trữ. Nhóm Phân tán và xếp hạng, Bài 04. Kiến thức nền: đồ thị và ma trận.

**Kiểm tra lại.** Ba câu rơi vào ba nhóm bài khác nhau nhưng chỉ hai đại lượng của Định nghĩa 01.13: khối lượng tính toán ở Câu (a), dung lượng lưu trữ ở Câu (b) và (c). Cùng một đại lượng có thể bị vi phạm ở hai nhóm bài khác nhau.
:::

Như vậy, chúng ta đã gắn ba giới hạn của Mục 1–3 với ba nhóm bài (Ví dụ 01.11), lập bảng phương pháp và thuộc tính cho Bài 02–15, và nêu sản phẩm học tập cho từng kỹ năng. Tuy nhiên, ba giới hạn này cần các thuật toán của Bài 05–06, 12–15 và 08–09.

<!-- note-topic-id: lec-01-topic-07 -->
<!-- note-collapsed -->
## Đọc thêm: Mẫu trùng ngẫu nhiên và suy luận

Giả sử một hệ thống đọc hồ sơ khách sạn của $10^9$ người trong $1000$ ngày và tìm các cặp người đã ở cùng một khách sạn trong hai ngày khác nhau. Số cặp người là $\binom{10^9}{2}=499\,999\,999\,500\,000\,000$, khoảng $5\times10^{17}$, nên một mẫu rất hiếm ở từng cặp người vẫn có thể xuất hiện nhiều lần chỉ do ngẫu nhiên. Để biết "nhiều" là bao nhiêu, chúng ta cần một mô hình xác suất cho dữ liệu và một phép tính kỳ vọng trong mô hình đó.

### Hồ sơ lưu trú và mô hình không phối hợp

Bài toán này xuất phát từ chương trình TIA (Total Information Awareness), đề xuất sau sự kiện ngày 11 tháng 9 năm 2001 để khai phá mọi dữ liệu tìm được, gồm cả hồ sơ khách sạn (MMDS, §1.2.1, tr.6). Khi tìm quá nhiều loại mẫu trong dữ liệu cùng lúc, ta sẽ thấy những mẫu trông đáng chú ý nhưng chỉ là sản phẩm của ngẫu nhiên. Khách sạn ở hai ngày có thể khác nhau; điều kiện trùng xét trong từng ngày (MMDS, §1.2.3, tr.7).

![Cặp người u, v ở cùng một khách sạn trong ngày s, rồi ở cùng một khách sạn trong ngày t khác s; khách sạn của ngày t có thể khác khách sạn của ngày s.](img/lec-01/suy-luan-mau-luu-tru.svg)

Hình vẽ một mẫu cần tìm, ứng với một cặp người và một cặp ngày. Để tính số mẫu, ta giả sử không có ai phối hợp: mọi người hành động ngẫu nhiên và độc lập (MMDS, §1.2.3, tr.7).

::: definition Định nghĩa 01.18 (Mô hình lưu trú không phối hợp)
Có $P$ người, quan sát trong $T$ ngày, với $H$ khách sạn. Với mỗi người và mỗi ngày:

- người đó đi khách sạn với xác suất $q$;
- nếu đi, người đó chọn một trong $H$ khách sạn với xác suất $1/H$ cho mỗi khách sạn.

Các lựa chọn của mọi cặp (người, ngày) độc lập với nhau. Giá trị của MMDS (§1.2.3, tr.7) là $P=10^9$, $T=1000$, $H=10^5$, $q=0{,}01$.
:::

Mô hình có ba giả thiết: độc lập giữa các người, độc lập giữa các ngày, và chọn khách sạn đều. Sức chứa 100 chỗ mỗi khách sạn cho $H=10^9\cdot0{,}01/100=10^5$. Mô hình không áp sức chứa thành ràng buộc, vì ràng buộc đó làm các lựa chọn phụ thuộc nhau. Đây là một *mô hình nền* (null model): nó mô tả dữ liệu khi không có phối hợp, để so với dữ liệu quan sát được.

::: example Ví dụ 01.12 (Xác suất trùng trong một ngày và trong hai ngày)
**Dữ kiện.** Mô hình của Định nghĩa 01.18 với $q=0{,}01$, $H=10^5$; hai người $u\ne v$.

**Cả hai cùng đi trong một ngày cho trước.** Theo độc lập giữa người, $q\cdot q=q^2=10^{-4}$.

**Cùng khách sạn khi cả hai đã đi.** Cố định khách sạn của $u$; $v$ chọn đúng khách sạn đó với xác suất $1/H=10^{-5}$.

**Một ngày.** $p=q^2/H=10^{-4}/10^5=10^{-9}$.

**Hai ngày khác nhau $s,t$ cho trước.** Theo độc lập giữa ngày, $p\cdot p=p^2=10^{-18}$; khách sạn của ngày $s$ và ngày $t$ không cần giống nhau.

**Kiểm tra lại.** $(10^{-2})^2=10^{-4}$; $10^{-4}\cdot10^{-5}=10^{-9}$; $(10^{-9})^2=10^{-18}$.
:::

![Mẫu hai ngày thỏa điều kiện khi cặp người trùng khách sạn trong ngày s và cũng trùng trong ngày t; độc lập giữa ngày cho phép nhân hai xác suất.](img/lec-01/suy-luan-hai-ngay.svg)

Hình ghép hai điều kiện "trùng ngày $s$" và "trùng ngày $t$" bằng chữ "và": đó là chỗ phép nhân $p\cdot p$ dùng giả thiết độc lập giữa ngày. Xác suất $1/H$ nói về hai người trong cùng một ngày, không nói về một người trong hai ngày.

Để đếm số mẫu trong toàn bộ dữ liệu, chúng ta cần chỉ rõ một "lần thử" là gì và biến nào đếm chúng.

::: definition Định nghĩa 01.19 (Phép thử và số biến cố trùng)
Một **phép thử** là một cặp gồm một cặp người không thứ tự $\{u,v\}$ và một cặp ngày không thứ tự $\{s,t\}$ với $s\ne t$; có $\binom P2\binom T2$ phép thử. Biến cố $e$ của phép thử xảy ra khi $u$ và $v$ ở cùng khách sạn trong ngày $s$ và ở cùng khách sạn trong ngày $t$. Số **biến cố trùng** là
$$
X=\sum_{\text{phép thử}}\mathbb 1_e .
$$
:::

$X$ đếm các bộ (cặp người, cặp ngày), không đếm cặp người: một cặp người trùng trong nhiều ngày góp nhiều biến cố vào $X$. Mỗi biến chỉ báo $\mathbb 1_e$ nhận giá trị 1 với xác suất $p^2$ theo Ví dụ 01.12. Kỳ vọng của $X$ suy ra từ tính tuyến tính của kỳ vọng.

::: proposition Mệnh đề 01.20 (Kỳ vọng số biến cố trùng)
**Giả thiết.** Dữ liệu sinh theo mô hình của Định nghĩa 01.18; $X$ như Định nghĩa 01.19.

**Kết luận.**
$$
\begin{gathered}
\mathbb E[X]=\binom P2\binom T2p^2,\\
p=\frac{q^2}{H}.
\end{gathered}
$$

**Điều kiện áp dụng.** Cần độc lập giữa người, độc lập giữa ngày và chọn khách sạn đều; không cần các phép thử độc lập với nhau.

**Phạm vi.** $\mathbb E[X]$ là trung bình của $X$ qua các lần sinh dữ liệu theo mô hình; mệnh đề không cho phân phối của $X$.
:::

::: proof
**Bước 1 (một ngày).** Với một cặp người và một ngày cho trước, cả hai cùng đi với xác suất $q^2$ [do độc lập giữa người]. Khi cả hai đã đi, xác suất cùng khách sạn là
$$
\sum_{\eta=1}^{H}\frac1H\cdot\frac1H=\frac1H
$$
[do chọn đều và độc lập giữa người; $\eta$ chạy qua các khách sạn]. Vậy xác suất trùng trong ngày đó là $p=q^2/H$.

**Bước 2 (hai ngày).** Biến cố trùng ngày $s$ chỉ phụ thuộc lựa chọn của ngày $s$, biến cố trùng ngày $t$ chỉ phụ thuộc lựa chọn của ngày $t$; hai biến cố độc lập [do độc lập giữa ngày], nên $\Pr(e)=p^2$.

**Bước 3 (biến chỉ báo).** $\mathbb E[\mathbb 1_e]=\Pr(e)=p^2$ cho mọi phép thử.

**Bước 4 (cộng).** Theo tính tuyến tính của kỳ vọng,
$$
\begin{aligned}
\mathbb E[X]&=\sum_{\text{phép thử}}\mathbb E[\mathbb 1_e]\\
&=\binom P2\binom T2p^2 .
\end{aligned}
$$
Tuyến tính của kỳ vọng đúng với mọi tổng hữu hạn biến ngẫu nhiên. Các phép thử chung một người hoặc một ngày phụ thuộc nhau, nhưng bước này không cần độc lập. $\square$
:::

Các giả thiết của Mệnh đề 01.20 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ độc lập giữa người: giả sử hai người $u,v$ luôn đi cùng nhau và ở cùng khách sạn. Khi đó xác suất họ trùng trong một ngày là $q=0{,}01$, lớn gấp $10^7$ lần $p=10^{-9}$.
- Bỏ chọn đều: giả sử mọi người đi khách sạn đều chọn khách sạn 1. Khi đó cả hai cùng đi là đủ để trùng, và $p=q^2=10^{-4}$, lớn gấp $10^5$ lần.
- Bỏ độc lập giữa ngày: giả sử lựa chọn của mỗi người ở ngày $t$ lặp lại đúng lựa chọn ở ngày $s$. Khi đó trùng ngày $s$ kéo theo trùng ngày $t$, và xác suất của biến cố là $p=10^{-9}$, không phải $p^2=10^{-18}$.

Bước 1 dùng độc lập giữa người và chọn đều; Bước 2 dùng độc lập giữa ngày; Bước 4 không dùng giả thiết nào ngoài tính tuyến tính của kỳ vọng.

::: example Ví dụ 01.13 (Số biến cố trùng với số liệu của MMDS)
**Dữ kiện.** $P=10^9$, $T=1000$, $p^2=10^{-18}$ (Ví dụ 01.12).

**Số cặp người và số cặp ngày.** $\binom{10^9}{2}=499\,999\,999\,500\,000\,000$; $\binom{1000}{2}=499\,500$.

**Kỳ vọng.** Theo Mệnh đề 01.20,
$$
\begin{aligned}
\mathbb E[X]&=499\,999\,999\,500\,000\,000\\
&\quad\cdot499\,500\cdot10^{-18}\\
&=249\,749{,}99975025\\
&\approx249\,750 .
\end{aligned}
$$

**Xấp xỉ.** Với $\binom n2\approx n^2/2$, $\mathbb E[X]\approx5\times10^{17}\cdot5\times10^5\cdot10^{-18}=250\,000$ (MMDS, tr.7).

**Kiểm tra lại.** $499\,999\,999\,500\,000\,000\cdot499\,500=249\,749\,999\,750\,250\,000\,000\,000$, nhân $10^{-18}$ được $249\,749{,}99975025$.
:::

Nếu thật sự có 10 cặp người phối hợp, cảnh sát phải điều tra khoảng một phần tư triệu cặp khác để tìm ra 10 cặp đó (MMDS, tr.8). Số cặp người phân biệt có tên trong đầu ra không vượt $X$, vì một cặp người có thể góp nhiều biến cố, như ví dụ sau.

::: example Ví dụ 01.14 (Một cặp người trùng trong ba ngày)
**Dữ kiện.** Cặp người $\{u,v\}$ ở cùng khách sạn trong đúng ba ngày $s_1,s_2,s_3$ và không trùng ngày nào khác.

**Các phép thử xảy ra.** Mọi cặp ngày chọn trong $\{s_1,s_2,s_3\}$: $\{s_1,s_2\}$, $\{s_1,s_3\}$, $\{s_2,s_3\}$.

**Đóng góp vào $X$.** $\binom32=3$ biến cố, dù chỉ có một cặp người.

**Kiểm tra lại.** Một cặp ngày có ngày ngoài $\{s_1,s_2,s_3\}$ không xảy ra vì cặp người không trùng ngày đó.
:::

### Bất đẳng thức Markov và nguyên lý Bonferroni

Kỳ vọng $249\,750$ cho biết trung bình có nhiều biến cố trùng ngẫu nhiên. Khi kỳ vọng nhỏ, chúng ta muốn đi xa hơn: chặn xác suất có ít nhất một biến cố trùng ngẫu nhiên. Công cụ cho việc đó chỉ dùng kỳ vọng.

::: lemma Bổ đề 01.21 (Bất đẳng thức Markov, dạng rời rạc)
**Giả thiết.** $X$ là biến ngẫu nhiên không âm nhận hữu hạn hoặc đếm được giá trị; $\lambda>0$.

**Kết luận.**
$$
\Pr(X\ge\lambda)\le\frac{\mathbb E[X]}{\lambda}.
$$

**Điều kiện áp dụng.** $X\ge0$, $\mathbb E[X]<\infty$ và $\lambda>0$.

**Phạm vi.** Bất đẳng thức đúng cho mọi biến ngẫu nhiên không âm, kể cả biến có mật độ (BHK, Định lý 2.1, tr.13); chứng minh dưới đây dành cho trường hợp rời rạc.
:::

::: proof
**Bước 1 (bỏ các giá trị nhỏ).** Vì mọi giá trị $x$ của $X$ không âm,
$$
\begin{aligned}
\mathbb E[X]&=\sum_x x\Pr(X=x)\\
&\ge\sum_{x\ge\lambda}x\Pr(X=x).
\end{aligned}
$$

**Bước 2 (thay $x$ bằng $\lambda$).** Trong tổng còn lại $x\ge\lambda$, nên
$$
\begin{aligned}
&\sum_{x\ge\lambda}x\Pr(X=x)\\
&\quad\ge\sum_{x\ge\lambda}\lambda\Pr(X=x)\\
&\quad=\lambda\Pr(X\ge\lambda).
\end{aligned}
$$

**Bước 3 (chia).** Ghép hai bước và chia cho $\lambda>0$ được $\Pr(X\ge\lambda)\le\mathbb E[X]/\lambda$. $\square$
:::

Bỏ giả thiết $X\ge0$ thì kết luận sai: với $X=-1$ chắc chắn và $\lambda=1$, $\Pr(X\ge1)=0$ nhưng $\mathbb E[X]/\lambda=-1<0$. Bước 1 dùng chính giả thiết này để bỏ các số hạng $x<\lambda$.

::: corollary Hệ quả 01.22 (Xác suất có ít nhất một biến cố)
**Giả thiết.** $X$ nhận giá trị nguyên không âm.

**Kết luận.** $\Pr(X\ge1)\le\mathbb E[X]$.

**Điều kiện áp dụng.** Như Bổ đề 01.21 với $\lambda=1$.

**Phạm vi.** Cận chỉ có ích khi $\mathbb E[X]<1$.
:::

::: proof
Vì $X$ nguyên không âm, $\mathbb 1_{\{X\ge1\}}\le X$: khi $X=0$ hai vế bằng 0, khi $X\ge1$ vế trái bằng 1 và vế phải không nhỏ hơn 1. Lấy kỳ vọng hai vế được $\Pr(X\ge1)\le\mathbb E[X]$; đây cũng là Bổ đề 01.21 với $\lambda=1$. $\square$
:::

Với $\mathbb E[X]\approx249\,750$ của Ví dụ 01.13, cận $\Pr(X\ge1)\le249\,750$ không cho thông tin. Nếu đổi tiêu chuẩn trùng thành ba ngày khác nhau, như MMDS Bài 1.2.1(c), cùng lập luận của Mệnh đề 01.20 với bộ ba ngày thay cho cặp ngày cho kỳ vọng $\binom{10^9}{2}\binom{1000}{3}p^3\approx0{,}0831$ (Bài tập 01.10). Khi đó Hệ quả 01.22 cho: trong mô hình không phối hợp, xác suất có ít nhất một biến cố trùng ba ngày không quá $0{,}0831$. Hiểu theo tần suất, tỷ lệ các bộ dữ liệu sinh theo mô hình có chứa ít nhất một biến cố như vậy không vượt $8{,}31\%$.

::: remark Nhận xét 01.23 (Nguyên lý Bonferroni)
MMDS (§1.2.2, tr.6–7) phát biểu một quy tắc phi hình thức, gọi là **nguyên lý Bonferroni** (Bonferroni's principle): tính kỳ vọng số lần xuất hiện của loại mẫu đang tìm, với giả sử dữ liệu hoàn toàn ngẫu nhiên; nếu số này lớn hơn nhiều số mẫu thật mà ta hy vọng tìm thấy, thì hầu hết mẫu tìm được là sản phẩm của ngẫu nhiên chứ không phải bằng chứng. Với hồ sơ lưu trú, $249\,750$ biến cố ngẫu nhiên so với 10 cặp thật cho đúng tình huống đó. Cách tránh là tìm những mẫu hiếm đến mức khó xuất hiện trong dữ liệu ngẫu nhiên, như tiêu chuẩn ba ngày ở trên.

| Kết quả đã có | Điều kết luận được |
|---|---|
| thuật toán liệt kê đủ mọi mẫu trùng | mọi mẫu trong đầu ra thỏa điều kiện tìm kiếm |
| mô hình không phối hợp cho $\mathbb E[X]\approx249\,750$ | đầu ra có thể chứa rất nhiều mẫu ngẫu nhiên |
| một cặp người có tên trong đầu ra | chưa đủ để tính xác suất cặp đó phối hợp; cần thêm tỷ lệ nền và mô hình cho cặp phối hợp |

Thuật toán chạy đúng không xác nhận giả thiết độc lập của mô hình nền. Tương tự, một cặp tài liệu có $\mathrm{SIM}\ge\tau$ chưa đủ để kết luận có hành vi sao chép.
:::

::: exercise Bài tập 01.9 (Chỗ dùng độc lập và chỗ dùng tuyến tính)
Trong phép tính $\mathbb E[X]=\binom P2\binom T2p^2$ của Mệnh đề 01.20:

- (a) chỉ ra mỗi chỗ dùng giả thiết độc lập và nói đó là độc lập giữa những gì;
- (b) chỉ ra chỗ dùng tính tuyến tính của kỳ vọng và giải thích vì sao ở đó không cần độc lập;
- (c) cho hai phép thử phụ thuộc nhau.
:::

::: hint
Đi lần lượt qua các thừa số $q^2$, $1/H$, $p^2$ rồi tới phép cộng trên mọi phép thử.
:::

::: solution
**Câu (a).** Thừa số $q^2$ dùng độc lập giữa hai người trong cùng một ngày. Thừa số $1/H$ dùng chọn đều và độc lập giữa lựa chọn khách sạn của hai người. Thừa số $p^2$ dùng độc lập giữa hai ngày.

**Câu (b).** Bước 4 của chứng minh: $\mathbb E[\sum\mathbb 1_e]=\sum\mathbb E[\mathbb 1_e]$. Đẳng thức này đúng với mọi tổng hữu hạn biến ngẫu nhiên, không cần độc lập.

**Câu (c).** Phép thử $(\{u,v\},\{s,t\})$ và $(\{u,u'\},\{s,t\})$, với $u'$ là người thứ ba, chung người $u$ và chung hai ngày. Biết biến cố thứ nhất xảy ra thì $u$ chắc chắn đi khách sạn trong ngày $s$ và ngày $t$, nên xác suất của biến cố thứ hai thành $(q/H)^2=(10^{-7})^2=10^{-14}$, lớn hơn $p^2=10^{-18}$; hai biến cố không độc lập.

**Kiểm tra lại.** Không có bước nào nhân xác suất của hai phép thử khác nhau; phép nhân chỉ xuất hiện bên trong một phép thử.
:::

Như vậy, chúng ta đã tính $\mathbb E[X]\approx249\,750$ biến cố trùng ngẫu nhiên trong mô hình không phối hợp (Định nghĩa 01.18, 01.19, Mệnh đề 01.20), chặn xác suất có ít nhất một biến cố bằng bất đẳng thức Markov (Bổ đề 01.21, Hệ quả 01.22), và nêu giới hạn của kết luận rút ra từ một mẫu trùng (Nhận xét 01.23). Mô hình chỉ cho kỳ vọng dưới giả thiết độc lập; nó không cho biết một cặp cụ thể có phối hợp hay không.

## Tình huống áp dụng và ứng dụng

::: application Tình huống 01.1 (Một triệu tài liệu với chữ ký trong bộ nhớ)
**Bài toán và dữ liệu.** Kho có $N=10^6$ tài liệu; mỗi tài liệu được thay bằng một chữ ký dài 250 phần tử, chiếm 1000 byte; so một cặp chữ ký mất 1 micro giây (MMDS, Ví dụ 3.10, tr.92). Cần mọi cặp có độ tương đồng đạt ngưỡng.

**Mô hình hóa.** Thuật toán 01.11, với phép so hai chữ ký thay cho bước 4. Phép so chữ ký cho một ước lượng của $\mathrm{SIM}$, không cho giá trị chính xác.

**Kiểm giả thiết.** Bộ nhớ: $10^6\cdot1000=10^9$ byte vừa bộ nhớ chính, và đọc tệp chữ ký tốn một lượt quét, tức $15\,259$ lần truyền khối (Mệnh đề 01.5(a)). Giả thiết phép kiểm chính xác của Mệnh đề 01.12 bị vi phạm, nên kết luận "xuất đúng $R$" không còn được bảo đảm. Phần "mỗi cặp được xét đúng một vòng" của chứng minh chỉ dùng điều kiện $i<j$ của hai vòng lặp, nên số vòng vẫn là $\binom N2$.

**Áp dụng.** $\binom{10^6}{2}=499\,999\,500\,000$ vòng so.

**Chi phí.** Theo cách đếm của Mệnh đề 01.15, số vòng nhân chi phí mỗi vòng: $499\,999\,500\,000\cdot10^{-6}=499\,999{,}5$ giây, khoảng $5{,}79$ ngày.

**Diễn giải.** Giới hạn nằm ở khối lượng tính toán, không ở bộ nhớ hay đọc ghi. Muốn giảm, phải kiểm ít cặp hơn.

**Giới hạn.** Theo Mệnh đề 01.16, nếu chỉ xác minh một tập ứng viên $A$ bằng phép kiểm chính xác trên các tập gốc, đầu ra là $A\cap R$, và mọi cặp của $R\setminus A$ là cặp bỏ sót. Nếu bước xác minh cũng dùng chữ ký, giả thiết phép kiểm chính xác của Mệnh đề 01.16 bị vi phạm, nên cả $\widehat R\subseteq R$ cũng không còn được bảo đảm: đầu ra có thể chứa ứng viên giả.

**Dẫn ngược lý thuyết.** Định nghĩa 01.10, 01.13; Thuật toán 01.11; Mệnh đề 01.5, 01.12, 01.15, 01.16.
:::

::: application Tình huống 01.2 (Nối bảng sinh viên với bảng đăng ký)
**Bài toán và dữ liệu.** Bảng `student` có $n_{\text{student}}=5000$ bản ghi trong $b_{\text{student}}=100$ khối; bảng `takes` có $n_{\text{takes}}=10\,000$ bản ghi trong $b_{\text{takes}}=400$ khối (DSC, Chương 15, trang chiếu 24). Bộ nhớ có $M=20$ khối, như ví dụ nối băm của DSC (trang chiếu 40). Cần mọi cặp bản ghi trùng mã sinh viên.

**Mô hình hóa.** Chi phí là số lần truyền khối (Định nghĩa 01.4, 01.13), không tính phần ghi đầu ra. Nối vòng lặp lồng nhau quét bảng trong một lần cho mỗi bản ghi của bảng ngoài; nối theo khối quét bảng trong một lần cho mỗi khối, hay mỗi nhóm khối, của bảng ngoài (DSC, Chương 15, trang chiếu 25–28).

**Kiểm giả thiết.** Hai bảng đều lớn hơn 20 khối, nên bảng trong phải được đọc lại; theo Mệnh đề 01.5(a), mỗi lượt quét bảng trong tốn đúng số khối của bảng.

**Áp dụng và chi phí.** Các phép đếm sau dùng công thức của DSC (trang chiếu 26, 28) với cùng bộ nhớ 20 khối; các cách khác nhau ở số khối bộ nhớ mà thuật toán dùng.

- Theo bản ghi, mỗi bảng dùng một khối bộ nhớ, `student` làm bảng ngoài: $5000\cdot400+100=2\,000\,100$ lần truyền khối, cộng $5000+100=5100$ lần dịch chuyển đầu đọc.
- Theo bản ghi, `takes` làm bảng ngoài: $10\,000\cdot100+400=1\,000\,400$ lần truyền khối.
- Theo khối, mỗi bảng dùng một khối bộ nhớ: $100\cdot400+100=40\,100$.
- Theo khối, dùng $M-2=18$ khối cho bảng ngoài `student`, hai khối còn lại cho bảng trong và đầu ra: $\lceil100/18\rceil\cdot400+100=6\cdot400+100=2\,500$.

**Diễn giải.** Mỗi dòng là "số lượt quét bảng trong nhân số khối của nó, cộng một lượt quét bảng ngoài". Đổi từ duyệt theo bản ghi sang theo khối giảm số lượt quét bảng trong từ $5000$ xuống $100$; dùng 18 khối bộ nhớ cho bảng ngoài giảm tiếp xuống $6$. Khi không có chỉ mục, mỗi bảng phải được đọc ít nhất một lần, nên các thuật toán trên tốn ít nhất $100+400=500$ lần truyền khối; DSC đạt đúng 500 khi bảng nhỏ hơn vừa bộ nhớ (trang chiếu 26), điều không xảy ra với $M=20$.

**Giới hạn.** Phép đếm không tính chi phí ghi kết quả và chưa dùng thứ tự hay chỉ mục của hai bảng. Bài 15 xây các thuật toán nối dùng sắp xếp, chỉ mục và băm.

**Dẫn ngược lý thuyết.** Định nghĩa 01.1, 01.4, 01.13; Mệnh đề 01.5.
:::

::: application Tình huống 01.3 (Hàm băm gặp tập khóa toàn số chẵn)
**Bài toán và dữ liệu.** Một chỉ mục băm theo Định nghĩa 01.8 dùng $h(x)=x\bmod B$ với $B=10$ thùng. Mọi khóa là số nguyên dương chẵn (MMDS, Ví dụ 1.5, §1.3.2, tr.10).

**Mô hình hóa.** Khóa $x$ vào thùng $x\bmod10$. Với khóa chẵn, $x\bmod10\in\{0,2,4,6,8\}$.

**Kiểm giả thiết.** Tập các số nguyên dương chẵn vẫn là một tập khóa hợp lý, nhưng mọi khóa có chung ước 2 với $B=10$, nên $h$ không phân tán khóa đều: năm thùng lẻ luôn rỗng, còn các khóa chẵn chia đều vào năm thùng chẵn, mỗi thùng $1/5$ số khóa thay vì $1/10$. Tính chất "mỗi thùng nhận số khóa xấp xỉ bằng nhau" nêu sau Định nghĩa 01.8 không đạt.

**Hậu quả.** Chỉ mục vẫn đúng: mọi bản ghi có khóa $v$ vẫn nằm trong thùng $h(v)$. Nhưng mỗi thùng khác rỗng chứa gấp đôi số bản ghi so với khi khóa chia đều, nên mỗi lần tra phải duyệt gấp đôi.

**Khắc phục.** Với $B=11$, mỗi thùng nhận $1/11$ số khóa chẵn (MMDS, tr.10). Tổng quát, khi khóa là số nguyên, chọn $B$ có ước chung với mọi hoặc hầu hết các khóa làm phân bố vào thùng không đều; vì vậy người ta thường chọn $B$ là số nguyên tố, dù vẫn phải xét trường hợp mọi khóa là bội của $B$ (MMDS, tr.10–11).

**Dẫn ngược lý thuyết.** Định nghĩa 01.8; Ví dụ 01.5.
:::

**Ứng dụng trong các bài sau của học phần.**

- Khối và lượt quét (Định nghĩa 01.4, Mệnh đề 01.5) là đơn vị chi phí của Bài 12–15.
- Tập $R$ (Định nghĩa 01.9, 01.10) là đầu ra mà chữ ký MinHash của Bài 05 và LSH của Bài 06 hướng tới; điều kiện $R\subseteq A$ (Mệnh đề 01.16) là cơ sở để đo âm giả ở Bài 06.
- Độ thu hồi tại $k$ (Định nghĩa 01.17) là đại lượng chất lượng của các chỉ mục hàng xóm gần đúng ở Bài 07.
- Mô hình chi phí (Định nghĩa 01.13) đo chi phí mỗi vòng cập nhật PageRank ở Bài 03.
- Yêu cầu $\mathrm{dec}(\mathrm{enc}(x))=x$ (Định nghĩa 01.7) là đặc tả khôi phục của Bài 10–11.
- Chỉ mục băm (Định nghĩa 01.8) là điểm xuất phát của băm tĩnh ở Bài 13.
- Tuyến tính của kỳ vọng và bất đẳng thức Markov (Mệnh đề 01.20, Bổ đề 01.21, phần đọc thêm) là công cụ phân tích lấy mẫu và phác thảo ở Bài 08–09 (Bổ đề 09.32).
- Bài toán đếm từ và yêu cầu mỗi đóng góp được tính đúng một lần (Mục 1.2, Nhận xét 01.3) là bài toán mở đầu của MapReduce ở Bài 02.

## Tóm tắt chương

Câu hỏi xuất phát của chương là trả mọi cặp đạt ngưỡng trong $N=10^6$ tài liệu: chữ ký của cả kho vừa bộ nhớ, nhưng số cặp là $499\,999\,500\,000$. Một bài toán dữ liệu gồm miền đầu vào, quan hệ đầu vào–đầu ra và ngân sách tài nguyên (Định nghĩa 01.1), và khi dữ liệu nằm trên đĩa, ngân sách được đo bằng số lần truyền khối: một lượt quét tệp $F$ khối tốn $F$, đọc và ghi lại tốn $2F$, $m$ lượt tốn $2mF$ (Định nghĩa 01.4, Mệnh đề 01.5). Với độ tương đồng Jaccard (Định nghĩa 01.9), tập kết quả là $R$ của Định nghĩa 01.10, và thuật toán xét mọi cặp trả đúng $R$ nhờ một bất biến trên tập cặp đã xét (Thuật toán 01.11, Mệnh đề 01.12). Thuật toán đó tốn không quá $N(N-1)L$ phép so sánh (Bổ đề 01.14, Mệnh đề 01.15), tức gần sáu ngày cho một triệu chữ ký trong bộ nhớ (Tình huống 01.1). Xét ít cặp hơn qua một tập ứng viên $A$ trả đúng $R$ khi và chỉ khi $R\subseteq A$ (Mệnh đề 01.16); các giới hạn về số cặp, đọc ghi và dòng dữ liệu được ba nhóm của Bài 02–15 xử lý (Mục 4). Trong mô hình hồ sơ lưu trú không phối hợp, kỳ vọng số biến cố trùng chỉ do ngẫu nhiên là khoảng $249\,750$ (Mệnh đề 01.20, phần đọc thêm). Các giới hạn còn lại, gồm cách tạo $A$, cách xử lý dòng và cách nối bảng lớn, là nội dung của các bài sau, bắt đầu với đếm từ trên kho phân tán (Mục 1.2, Nhận xét 01.3): bộ trang chiếu [Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) đặc tả MapReduce cho bài toán này, với yêu cầu mỗi lần xuất hiện của một từ góp đúng một lần vào số đếm.

**Định nghĩa và kết quả theo mục.**

- Mục 1: bài toán dữ liệu (Định nghĩa 01.1); $k$ hàng xóm gần nhất chính xác (Định nghĩa 01.2); nhiều máy và máy hỏng (Nhận xét 01.3).
- Mục 2: khối, lần truyền khối, lượt quét (Định nghĩa 01.4); chi phí lượt quét (Mệnh đề 01.5, Nhận xét 01.6); nén không mất và có mất thông tin (Định nghĩa 01.7); hàm băm và chỉ mục băm (Định nghĩa 01.8).
- Mục 3: Jaccard (Định nghĩa 01.9); bài toán cặp gần trùng (Định nghĩa 01.10); xét mọi cặp (Thuật toán 01.11) và tính đúng (Mệnh đề 01.12); mô hình chi phí (Định nghĩa 01.13); thủ tục trộn (Bổ đề 01.14); chi phí xét mọi cặp (Mệnh đề 01.15); xác minh ứng viên (Mệnh đề 01.16); độ thu hồi (Định nghĩa 01.17).
- Mục 4: bảng giới hạn, nhóm bài và thuộc tính cần đánh giá; ghép giới hạn với nhóm bài (Ví dụ 01.11); CLO1–CLO4 và sản phẩm học tập.
- Phần đọc thêm: mô hình lưu trú không phối hợp (Định nghĩa 01.18); phép thử và số biến cố trùng (Định nghĩa 01.19); kỳ vọng (Mệnh đề 01.20); Markov (Bổ đề 01.21, Hệ quả 01.22); nguyên lý Bonferroni (Nhận xét 01.23).

**Công thức và thuật toán cần nhớ.**

$$
\begin{gathered}
\mathrm{SIM}(C,C')=\frac{|C\cap C'|}{|C\cup C'|},\\
R=\{(i,j):1\le i<j\le N,\\ \mathrm{SIM}(C_i,C_j)\ge\tau\},\\
\binom N2=\frac{N(N-1)}{2}.
\end{gathered}
$$

Xét mọi cặp tốn không quá $N(N-1)L$ phép so sánh; một lượt quét tốn $F$, đọc và ghi lại tốn $2F$, $m$ lượt tốn $2mF$ lần truyền khối. Với xác minh ứng viên:

$$
\begin{gathered}
\widehat R=A\cap R,\\
\widehat R=R\iff R\subseteq A.
\end{gathered}
$$

Thuật toán xét mọi cặp duyệt $i=1,\ldots,N-1$ và $j=i+1,\ldots,N$, tính $\mathrm{SIM}$ chính xác và xuất $(i,j)$ khi $\mathrm{SIM}\ge\tau$.

**Giả thiết hay bị bỏ quên.**

- Jaccard cần $C\cup C'\ne\varnothing$; tập rỗng cho $0/0$.
- Tính đúng của xét mọi cặp cần phép so với ngưỡng chính xác; với $\tau=a/c$, so số nguyên $|C\cap C'|\cdot c\ge a\cdot|C\cup C'|$.
- $O(N^2L)$ là cận trên của phần xét cặp, chưa tính tạo các tập, ghi $R$ và đọc ghi đĩa.
- Xác minh chính xác chỉ bảo đảm $\widehat R\subseteq R$; đủ $R$ cần thêm $R\subseteq A$.
- Số lần truyền khối khác số giây: với cùng $F$ khối, đọc từng khối bằng một truy cập riêng chậm hơn đọc tuần tự khoảng 15 lần theo giả thiết của MMDS (Ví dụ 01.3).

<!-- note-topic-id: lec-01-topic-08 -->
## Bài tập củng cố

Bài tập 01.10–01.11 nằm trong [tệp bài tập Bài 01](material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html), cùng gợi ý và lời giải. Hai bài này dùng mô hình lưu trú của phần đọc thêm *Mẫu trùng ngẫu nhiên và suy luận* (Định nghĩa 01.18 – Nhận xét 01.23).

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press. §1.2.1–1.2.4, tr.6–8: phần đọc thêm, Bài tập 01.10, 01.11; §1.3.2–1.3.3, tr.10–12: Định nghĩa 01.8, Ví dụ 01.5, Tình huống 01.3; §1.3.4, tr.13: Mục 2.1; Chương 3, tr.73–75, Ví dụ 3.1, tr.74 và Hình 3.1, tr.75: Mục 1, Mục 3.1, Mục 3.5; Ví dụ 3.10, tr.92: Mục 3.4, Tình huống 01.1; §4.2.1–4.2.2, tr.136–137 và §4.3.1, tr.139–140: Mục 2.2; §5.3.1, tr.195–196 và Hình 5.16, tr.200: Mục 1.2. Sách và trang chiếu của các tác giả: http://www.mmds.org.
- Blum, A., Hopcroft, J. và Kannan, R., *Foundations of Data Science*, bản ngày 04/01/2018. Chương 1, tr.9–11: mô hình RAM ở mở đầu Mục 1; §2.1–2.2, tr.12–15, và Định lý 2.1, tr.13: Bổ đề 01.21.
- Leskovec, J. Stanford CS246, *Mining Massive Datasets*, bài 01-intro, trang chiếu 32–33: Nhận xét 01.3; trang chiếu 62: Mục 1.1; trang chiếu 67–69: chi phí truyền thông (communication cost) ở Mục 3.4.
- Silberschatz, A., Korth, H. F. và Sudarshan, S. (2019). *Database System Concepts*, ấn bản 7, McGraw-Hill. Trang chiếu Chương 15, 8–9: mô hình chi phí ở Mục 2.1, Nhận xét 01.6; 19–22: sắp xếp ngoài ở Mục 2.4; 24–28: Tình huống 01.2; 40: giả thiết bộ nhớ $M=20$ khối ở Mục 2.4 và Tình huống 01.2; Chương 14, 24 và 31: tra cứu theo khóa, theo vùng và theo từ khóa ở Mục 2.4.
- Nelson, M. và Gailly, J.-L. (1995). *The Data Compression Book*, ấn bản 2, M&T Books. Chương 3 và 11: Mục 2.3.
- Blelloch, G. CMU 15-499, *Algorithms in the Real World: Data Compression*, phần LZ (compression3-lz), trang chiếu 13–14, 17, 19: chuỗi `aabaacabcabcb` ở Mục 2.3.
- Stanford BIODS 271, bài L12 *Approximate Nearest Neighbor*, tr.16–18: Mục 1.2, Ví dụ 01.2.
- Princeton COS 597A, lớp 8 và 9: độ thu hồi tại $k$ làm thước đo chất lượng của tìm kiếm véc-tơ, Định nghĩa 01.17.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press. §1.1: bài toán tính toán, Định nghĩa 01.1; §2.1: bất biến vòng lặp, chứng minh Mệnh đề 01.12 và Bổ đề 01.14.
- Đề cương học phần UET.DSE2053: mã, số tín chỉ, tiên quyết và CLO1–CLO4 ở Mục 4.2; thứ tự và quan hệ tiên quyết của Bài 02–15 ở Mục 4.1.
- Đọc tiếp: [Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html), *MapReduce và ngăn xếp xử lý dữ liệu lớn*.
