# Bài 10 — Nén dữ liệu không mất thông tin

Chúng ta xây ba bộ nén cho dữ liệu phải khôi phục đúng từng bit: mã Huffman tĩnh (static Huffman coding), mã Huffman thích nghi (adaptive Huffman coding) và mã số học (arithmetic coding). Cả ba nhận xác suất của ký hiệu từ một mô hình, và với mỗi bộ nén chúng ta chứng minh khi nào bộ giải nén khôi phục đúng thông điệp và dòng bit dài bao nhiêu so với entropy.

[Bộ trang chiếu Bài 10](lecture-10-nen-du-lieu-khong-mat-thong-tin.html) trình bày cùng chủ đề; [tệp bài tập Bài 10](material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-nen-du-lieu-khong-mat-thong-tin.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đặc tả bài toán nén không mất thông tin (bảng chữ cái, thông điệp, mã, giải mã duy nhất, cách dừng), tách mô hình xác suất khỏi bộ mã và chứng minh rằng không mã nào rút ngắn được mọi thông điệp (Mục 1).
2. Kiểm tra một mã có phải mã tiền tố không, giải mã một dòng bit bằng cây mã, dùng bất đẳng thức Kraft để quyết định một bộ độ dài có thực hiện được không và dựng mã tương ứng (Mục 2).
3. Tính tự thông tin, entropy và độ dài trung bình; chứng minh $\bar\ell(c)\ge H(P)$ với mọi mã tiền tố và sự tồn tại của mã tiền tố có $\bar\ell(c)<H(P)+1$ (Mục 2).
4. Chạy thuật toán Huffman tĩnh, lập bảng mã và giải mã; chứng minh tính tối ưu bằng phép đổi chỗ và quy nạp; đếm chi phí dựng cây và đầu mục phải truyền (Mục 3).
5. Mô phỏng Huffman thích nghi với `ESCAPE`, `EOS`, lá trọng số 0, phép tăng–đổi và phép dựng lại; chứng minh phép tăng–đổi giữ tính chất anh em và hai phía luôn có cùng cây (Mục 4).
6. Mã hóa và giải mã bằng khoảng nửa mở, chọn chuỗi bit trong khoảng cuối và chứng minh độ dài chuỗi bit nhỏ hơn $I(x)+2$ (Mục 5).
7. Chạy mã số học với thanh ghi 16 bit gồm phát tiền tố chung và bit chờ, giải thích ràng buộc $N\le2^{R-2}$ cho tổng số đếm, và chọn cặp mô hình–bộ mã theo phân phối, số lượt đọc và đầu mục (Mục 6, Mục 7).

<!-- note-topic-id: lec-10-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `08.k` chỉ ghi chú Bài 08, `09.k` chỉ ghi chú Bài 09. Ghi chú Bài 05 chưa đánh số hiệu, nên được dẫn theo mục.

Trong các kết quả nhắc lại dưới đây, các chữ $r$, $t$, $m$, $u$, $\kappa$, $\varepsilon$ là biến tạm theo ký hiệu của bài được dẫn, không mang nghĩa của bảng ký hiệu Bài 10.

- **Thuật toán dòng một lượt** (Định nghĩa 08.1). Thuật toán giữ một trạng thái; phép cập nhật nhận trạng thái cũ cùng phần tử mới và trả trạng thái mới; mỗi phần tử được đọc đúng một lần. Bộ nén thích nghi ở Mục 4 là một thuật toán như vậy, với trạng thái là cây mã.
- **Số bit của một bộ đếm** (Bài 08, Mục 1.4, sau Định nghĩa 08.3). Một đại lượng nhận các giá trị $0,1,\ldots,r$ cần $\lceil\log_2(r+1)\rceil$ bit; do đó $k$ giá trị khác nhau cần $\lceil\log_2k\rceil$ bit.
- **Bảo đảm của Count-Min** (Định lý 09.37). Với $t$ hàng, mỗi hàng $m=\lceil2\kappa/\varepsilon\rceil$ ô, ước lượng $\widehat f_u$ của tần suất $f_u$ thỏa $\widehat f_u\ge f_u$, và $\widehat f_u<f_u+\varepsilon r/\kappa$ với xác suất ít nhất $1-2^{-t}$, trong đó $r$ là độ dài dòng. Bảng đếm chỉ trả lời truy vấn tần suất; từ nó không dựng lại được dòng.
- **Cây nhị phân** (học phần Cấu trúc dữ liệu và giải thuật). Gốc, lá, nút trong, cha, con, anh em, tổ tiên, hậu duệ; độ sâu của một nút là số cạnh từ gốc tới nút. Cây nhị phân *đầy đủ* (full binary tree) là cây mà mọi nút trong có đúng hai con; số nút trong của nó ít hơn số lá đúng 1.
- **Hàng đợi ưu tiên** (học phần Cấu trúc dữ liệu và giải thuật). Hàng đợi giữ các phần tử có khóa và có hai phép: lấy ra phần tử có khóa nhỏ nhất, và chèn. Cài bằng đống nhị phân (binary heap) chứa không quá $k$ phần tử, mỗi phép tốn $O(\log k)$ phép so sánh.
- **Xác suất rời rạc** (học phần Xác suất thống kê). Phân phối trên một tập hữu hạn có tổng bằng 1; kỳ vọng của tổng bằng tổng các kỳ vọng; với các ký hiệu độc lập cùng phân phối, xác suất của một chuỗi bằng tích xác suất các ký hiệu.
- **Logarit và một bất đẳng thức** (Giải tích 1). $\log_2(ab)=\log_2a+\log_2b$ và $\log_2\xi=\ln\xi/\ln2$. Với mọi $\xi>0$, $\ln\xi\le\xi-1$, dấu bằng xảy ra khi và chỉ khi $\xi=1$.
- **Phần nguyên** (Toán rời rạc). Với số thực $\upsilon$, $\upsilon\le\lceil\upsilon\rceil<\upsilon+1$ và $\upsilon-1<\lfloor\upsilon\rfloor\le\upsilon$; với hai số thực $\alpha\ge\beta$, $\lfloor\alpha\rfloor-\lfloor\beta\rfloor\ge\lfloor\alpha-\beta\rfloor$.
- **Phân số nhị phân** (Toán rời rạc). Chuỗi bit $b_1\cdots b_\ell$ biểu diễn số $0{,}b_1\cdots b_\ell$ (cơ số 2) $=\sum_{i=1}^{\ell}b_i2^{-i}$, một bội của $2^{-\ell}$ trong $[0;1)$.
- **Nguyên lý Dirichlet** (Toán rời rạc). Không có đơn ánh từ tập hữu hạn $A$ vào tập $B$ khi $\lvert A\rvert>\lvert B\rvert$.
- **Quy nạp và bất biến vòng lặp** (ghi chú Bài 05, Mục 10). Bất biến vòng lặp đúng trước lượt đầu, được giữ qua mỗi lượt và cho điều cần chứng minh khi vòng lặp dừng.

## Bảng ký hiệu

Các ký hiệu dưới đây dùng xuyên suốt chương; chữ chỉ dùng trong một mục hoặc một chứng minh được giới thiệu tại chỗ. Mỗi chữ trong bảng giữ nghĩa ghi trong bảng ở cả chương; ngoài ra $i$, $j$ còn làm chỉ số chạy trong tổng và chứng minh.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\Sigma$; $s$, $s'$; $k$ | bảng chữ cái; một ký hiệu; số ký hiệu, $k=\lvert\Sigma\rvert$ | tập hữu hạn có thứ tự cố định; $k\ge2$ |
| $x=x_1x_2\cdots x_n$; $n$ | thông điệp; độ dài thông điệp | $x_t\in\Sigma$; $n\ge1$ |
| $X=X_1\cdots X_n$ | thông điệp ngẫu nhiên | các $X_t$ độc lập, cùng phân phối $P$ |
| $\{0,1\}^*$; $u$, $u'$; $\lvert u\rvert$ | tập chuỗi bit hữu hạn; một chuỗi bit; độ dài của nó | |
| $c$; $c(s)$; $c^*$; $c_{\mathrm H}$ | mã ký hiệu; từ mã của $s$; mở rộng $c^*(x)=c(x_1)\cdots c(x_n)$; mã Huffman | $c:\Sigma\to\{0,1\}^*$ |
| $\ell_s$; $\ell_{\max}$ | độ dài từ mã của $s$; độ dài lớn nhất | số nguyên dương |
| $J(u)$; $K$ | khoảng mã của chuỗi bit $u$; tổng Kraft $\sum_s2^{-\ell_s}$ | khoảng nửa mở trong $[0;1)$; số thực dương |
| $f_s$; $N$ | số đếm của $s$; tổng số đếm $N=\sum_sf_s$ | số nguyên không âm; số nguyên dương |
| $p_s$; $P$ | xác suất của $s$ theo mô hình; phân phối $P=(p_s)_{s\in\Sigma}$ | $p_s\in(0;1]$, $\sum_sp_s=1$ |
| $\bar\ell(c)$ | độ dài trung bình $\sum_sp_s\ell_s$ | bit mỗi ký hiệu |
| $I(s)$; $I(x)$ | tự thông tin của ký hiệu, của thông điệp | bit |
| $H(P)$ | entropy của phân phối $P$ | $0\le H(P)\le\log_2k$ |
| $j$ | bậc của mô hình; độ dài khối khi mã Huffman trên khối ký hiệu | số nguyên không âm; số nguyên dương |
| $T$; $T_{\mathrm H}$; $\operatorname{depth}_T(s)$; $\operatorname{cost}(T)$; $\mathcal Q$ | cây mã; cây do Thuật toán 10.14 trả về; độ sâu của lá $s$; tổng $\sum_sf_s\operatorname{depth}_T(s)$; hàng đợi ưu tiên các nút chưa có cha | $\operatorname{cost}(T)$ là số nguyên không âm |
| $v$; $\operatorname{wt}(v)$; $k'$; $\#i$ | một nút của cây có trọng số; trọng số của nút; số lá của cây có trọng số; vị trí thứ $i$ trong danh sách của tính chất anh em | số nguyên không âm; $k'\ge2$; $1\le i\le2k'-1$ |
| $W_{\max}$ | ngưỡng trọng số gốc buộc dựng lại cây | số nguyên dương |
| `ESCAPE`; `EOS` | ký hiệu thoát; ký hiệu kết thúc dòng | ngoài 256 giá trị byte |
| $F(s)$ | xác suất tích lũy trước $s$, $\sum_{s'<s}p_{s'}$ | $[0;1)$ |
| $t$; $[a_t;\,a_t+w_t)$ | số ký hiệu đã mã hóa; khoảng sau $t$ ký hiệu, cận dưới $a_t$, độ rộng $w_t$ | $a_0=0$, $w_0=1$ |
| $z(u)$, $z$; $z_i$; $\lambda$ | số $0{,}b_1\cdots b_\ell$ (cơ số 2) của chuỗi bit $u$, tức điểm đầu của $J(u)$, và số nhị phân được phát ở mã số học; điểm đầu của khoảng thứ $i$ khi dựng mã từ bộ độ dài; số bit của $z$ | $[0;1)$; $[0;1)$; số nguyên dương |
| $R$; $Q$ | số bit của thanh ghi; $Q=2^{R-2}$, một phần tư phạm vi thanh ghi | $R\ge2$; $Q=16\,384$ khi $R=16$ |
| $G(s)$ | số đếm tích lũy trước $s$, $\sum_{s'<s}f_{s'}$ | $0\le G(s)<N$ |
| `low`, `high`, `range`, `code`, `count` | thanh ghi cận dưới; cận trên; $\texttt{high}-\texttt{low}+1$; thanh ghi đọc của bộ giải mã; số đếm bộ giải mã tính từ `code` để chọn ký hiệu | số nguyên $R$ bit; `count` là số nguyên |
| $m$ | số bit chờ | số nguyên không âm |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $0{,}2572167752$; hai đầu của một khoảng số ngăn bằng dấu chấm phẩy, ví dụ $[0{,}2;\,0{,}3)$. Số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $65\,536$.
- Chuỗi bit viết trong khối mã, bit cao bên trái, ví dụ `01001110110`; số nhị phân viết $0{,}01110_2$.
- Tên ký hiệu trong ví dụ viết chữ đứng, như A, B hay $\mathrm a,\mathrm b,\mathrm c$, để không lẫn với mã $c$ và cận dưới $a_t$.
- $\log_2$ là logarit cơ số 2, $\ln$ là logarit tự nhiên.
- Viết tắt nguồn: NG là sách *The Data Compression Book* (ấn bản 2) của Nelson và Gailly; CMU là bài giảng *Data Compression* của Blelloch cho học phần CMU 15-499, CMU-A1 là bài tập Assignment 1a của học phần đó cùng lời giải; EE398A-1 và EE398A-3 là bài giảng *Entropy and Lossless Coding* và *Arithmetic Coding* của Girod cho học phần Stanford EE398A.

## 1. Khôi phục chính xác: mô hình và bộ mã

Bài 09 xây các phác thảo trả lời truy vấn trên dòng bằng bộ nhớ nhỏ. Chẳng hạn, Count-Min dùng $t\cdot m$ bộ đếm và ước lượng tần suất của mọi phần tử với sai số chặn được (Định lý 09.37), nhưng từ bảng đếm đó không dựng lại được chính dòng dữ liệu. Nhiều bài toán lưu trữ cần điều ngược lại: một kho văn bản hoặc một kho nhật ký lớn phải được lưu hay truyền qua đường truyền có băng thông hạn chế, và bên nhận phải khôi phục đúng từng bit.

Khoảng cách giữa số bit đang dùng và số bit cần dùng có thể lớn. Nếu chữ 'e' chiếm $1/16$ số ký tự của một văn bản, mỗi lần xuất hiện của nó mang $\log_2 16=4$ bit thông tin, nên chuỗi "eeeee" mang 20 bit thông tin, trong khi mã ASCII 8 bit dùng 40 bit cho chuỗi đó (NG, tr.20). Để thu hẹp khoảng cách này mà vẫn khôi phục chính xác, chúng ta cần trả lời ba câu hỏi: một mã phải thỏa điều kiện gì để giải được, số bit trung bình nhỏ nhất có thể là bao nhiêu, và thuật toán nào đạt gần mức đó.

Ba bộ mã trả lời câu hỏi thứ ba; cấu trúc của chương như sơ đồ dưới đây.

![Sơ đồ cấu trúc chương: thông điệp x vào mô hình xác suất (Mục 1), mô hình cho phân phối P tới ba bộ mã Huffman tĩnh (Mục 3), Huffman thích nghi (Mục 4) và mã số học (Mục 5, 6); bộ giải mã dùng cùng mô hình để trả lại x. Khối Mục 2 (mã tiền tố, Kraft, entropy) đo cả ba bộ mã; khối Mục 7 chọn cặp mô hình–bộ mã.](img/lec-10/note-cau-truc-chuong-10.svg)

Trên sơ đồ, dữ liệu đi từ mô hình tới bộ mã: mô hình cho xác suất, bộ mã biến xác suất thành bit, bộ giải mã lặp lại đúng các bước đó. Khối Mục 2 ở dưới chứa các công cụ mà cả ba bộ mã dùng để đo và chứng minh.

<!-- note-topic-id: lec-10-topic-02 -->
### 1.1 Đặc tả nén không mất thông tin

::: example Ví dụ 10.1 (Thông điệp A–E với mã độ dài cố định)
**Dữ kiện.** Một thông điệp gồm $n=39$ ký hiệu trên bảng chữ cái $\{\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E\}$ với số đếm (NG, tr.32–33):

- A: 15;
- B: 7;
- C: 6;
- D: 6;
- E: 5.

**ASCII tốn 312 bit.** Mã ASCII dùng 8 bit mỗi ký hiệu, tổng $39\cdot8=312$ bit.

**Mã độ dài cố định tốn 117 bit.** Năm ký hiệu cần $\lceil\log_25\rceil=3$ bit nếu mọi từ mã dài bằng nhau (Bài 08, Mục 1.4), tổng $39\cdot3=117$ bit.

**Kiểm tra lại.** $15+7+6+6+5=39=n$, và $2^2<5\le2^3$.
:::

Mã 3 bit dùng cho A, ký hiệu chiếm $15/39\approx38\%$ thông điệp, cùng số bit như cho E. Gán cho A một từ mã ngắn hơn và cho E một từ mã dài hơn có thể giảm tổng số bit, nhưng khi các từ mã có độ dài khác nhau, bộ giải mã không còn cắt dòng bit thành các khối bằng nhau được. Chúng ta cần nêu chính xác yêu cầu đối với một mã như vậy.

::: definition Định nghĩa 10.1 (Mã ký hiệu và giải mã duy nhất)
- **Bảng chữ cái** (alphabet) $\Sigma$ là một tập hữu hạn gồm $k\ge2$ **ký hiệu** (symbol), có một thứ tự cố định. Một **thông điệp** (message) là chuỗi hữu hạn $x=x_1x_2\cdots x_n$ với $x_t\in\Sigma$; $\Sigma^*$ là tập mọi thông điệp.
- Một **mã ký hiệu** (symbol code) là ánh xạ $c:\Sigma\to\{0,1\}^*$ gán cho mỗi ký hiệu $s$ một chuỗi bit khác rỗng $c(s)$, gọi là **từ mã** (codeword) của $s$, với độ dài $\ell_s=\lvert c(s)\rvert$.
- **Mở rộng** của $c$ là ánh xạ $c^*:\Sigma^*\to\{0,1\}^*$ nối các từ mã:
$$
c^*(x_1\cdots x_n)=c(x_1)\cdots c(x_n).
$$
- Mã $c$ là **mã giải mã duy nhất** (uniquely decodable code) khi $c^*$ là đơn ánh: hai thông điệp khác nhau luôn cho hai dòng bit khác nhau.
:::

Định nghĩa tách hai tầng: mã $c$ chỉ gán từ mã cho từng ký hiệu, còn tính giải mã duy nhất là yêu cầu trên $c^*$, tức trên cả dòng bit nối liền. Mã độ dài cố định của Ví dụ 10.1 là trường hợp riêng với $\ell_s=3$ cho mọi $s$; nó giải mã duy nhất vì bộ giải mã cắt dòng bit thành từng khối 3 bit. Mã $\mathrm a=1$, $\mathrm b=01$, $\mathrm c=101$, $\mathrm d=011$ (CMU, trang chiếu 22) là một phản ví dụ: dòng `1011` là $c^*(\mathrm{aba})$, cũng là $c^*(\mathrm{ca})$ và $c^*(\mathrm{ad})$, nên $c^*$ không đơn ánh.

Chúng ta muốn mã ngắn hơn mã độ dài cố định trên dữ liệu thật. Không mã nào ngắn hơn trên mọi dữ liệu, như mệnh đề sau chứng minh.

::: proposition Mệnh đề 10.2 (Không mã nào rút ngắn mọi thông điệp)
**Giả thiết.** $n\ge1$ là số nguyên, độ dài thông điệp trên $\Sigma=\{0,1\}$; $\varphi$ là một ánh xạ từ $\{0,1\}^n$, tập các chuỗi $n$ bit, vào $\{0,1\}^*$.

**Kết luận.** Nếu $\varphi$ là đơn ánh thì có ít nhất một chuỗi $u\in\{0,1\}^n$ với $\lvert\varphi(u)\rvert\ge n$.

**Điều kiện áp dụng.** Chỉ cần $\varphi$ là đơn ánh, tức yêu cầu khôi phục chính xác; không cần giả thiết gì về cách $\varphi$ được tính.

**Phạm vi.** Mệnh đề nói về mọi bộ nén không mất thông tin, kể cả ba bộ mã của chương: mỗi bộ mã rút ngắn một số thông điệp thì phải giữ nguyên độ dài hoặc kéo dài ít nhất một thông điệp khác.
:::

::: proof
**Bước 1 (đếm chuỗi ngắn hơn).** Số chuỗi bit có độ dài $j$ là $2^j$, nên số chuỗi có độ dài nhỏ hơn $n$, kể cả chuỗi rỗng, là
$$
\sum_{j=0}^{n-1}2^j=2^n-1 .
$$

**Bước 2 (Dirichlet).** Giả sử mọi $u\in\{0,1\}^n$ có $\lvert\varphi(u)\rvert<n$. Khi đó $\varphi$ là đơn ánh từ một tập $2^n$ phần tử vào một tập $2^n-1$ phần tử, trái với nguyên lý Dirichlet. Vậy có $u$ với $\lvert\varphi(u)\rvert\ge n$. $\square$
:::

Với $n=3$, có 8 chuỗi 3 bit nhưng chỉ có 7 chuỗi ngắn hơn: 1 chuỗi rỗng, 2 chuỗi 1 bit và 4 chuỗi 2 bit. Ít nhất một trong 8 chuỗi phải nhận ảnh dài từ 3 bit trở lên. Nén chỉ có lợi trên những thông điệp mà mô hình gán xác suất cao, và trả giá trên những thông điệp ít xảy ra theo mô hình đó.

Nén không mất thông tin (lossless compression) khác nén mất thông tin (lossy compression, còn gọi là nén mất dữ liệu), loại nén chỉ yêu cầu bản khôi phục gần với bản gốc (NG, tr.18–19).

<!-- note-topic-id: lec-10-topic-03 -->
### 1.2 Mô hình xác suất, bộ mã và giao thức

Theo Mệnh đề 10.2, một bộ nén chỉ rút ngắn được những thông điệp mà nó coi là dễ xảy ra, và mức dễ xảy ra do mô hình quyết định. Cùng một chữ cái có thể nhận xác suất rất khác nhau.

::: example Ví dụ 10.2 (Chữ 'u' dưới hai mô hình)
**Dữ kiện.** Trong văn bản tiếng Anh, một mô hình không nhìn ký tự trước có thể gán cho 'u' xác suất 1%; một mô hình nhìn một ký tự trước, khi ký tự trước là 'q', có thể gán cho 'u' xác suất 95% (NG, tr.21).

**Tính.** Số bit thông tin của 'u' theo hai mô hình là
$$
\begin{aligned}
-\log_2 0{,}01&\approx6{,}64\ \text{bit},\\
-\log_2 0{,}95&\approx0{,}074\ \text{bit}.
\end{aligned}
$$

**Diễn giải.** Cùng một ký tự, ở cùng một vị trí, cần khoảng $6{,}64$ bit hay chỉ khoảng $0{,}074$ bit tùy mô hình.

**Kiểm tra lại.** $2^{-6{,}64}\approx0{,}0100$ và $2^{-0{,}074}\approx0{,}950$.
:::

Một cách trực quan, nén gồm hai việc tách rời: đoán ký hiệu tiếp theo, rồi biến lời đoán thành bit (NG, tr.19, Hình 2.1; CMU, trang chiếu 8). Chúng ta đặt tên cho hai việc đó.

::: definition Định nghĩa 10.3 (Mô hình xác suất và bộ mã)
- Một **mô hình xác suất** (statistical model) cho, trước mỗi vị trí $t$, một phân phối $P_t=(p_{t,s})_{s\in\Sigma}$ trên $\Sigma$, tính được từ các ký hiệu $x_1,\ldots,x_{t-1}$ đã xử lý và từ các dữ kiện hai phía đã thống nhất trước.
- Mô hình là **tĩnh** (static model, còn gọi là thích nghi tiến, forward adaptation) khi $P_t=P$ không đổi theo $t$; bảng xác suất hoặc bảng số đếm được dựng trước và truyền cho bên nhận, hoặc được hai phía thống nhất từ trước (EE398A-1, trang chiếu 23).
- Mô hình là **thích nghi** (adaptive model, còn gọi là thích nghi lùi, backward adaptation) khi $P_t$ được cập nhật sau mỗi ký hiệu theo một quy tắc tất định mà hai phía cùng chạy (EE398A-1, trang chiếu 23).
- Mô hình có **bậc** (order) $j$ khi $P_t$ chỉ phụ thuộc $j$ ký hiệu ngay trước vị trí $t$, $x_{t-j},\ldots,x_{t-1}$, cùng các số đếm đã có.
- Một **bộ mã** (coder) là thủ tục tất định nhận dãy phân phối $P_1,P_2,\ldots$ và thông điệp $x$, rồi phát dòng bit; bộ giải mã tương ứng nhận cùng dãy phân phối và dòng bit, rồi trả lại $x$.
:::

Mô hình quyết định xác suất, bộ mã quyết định cách biến xác suất thành bit; một bộ nén là một cặp mô hình–bộ mã. Mô hình "nhìn một ký tự trước" của Ví dụ 10.2 có bậc 1, mô hình còn lại có bậc 0. Một nhầm lẫn thường gặp là nói "mã Huffman nén kém": độ dài đầu ra phụ thuộc trước hết vào xác suất mà mô hình đưa cho bộ mã, nên câu đó nói về mô hình chứ không về bộ mã (NG, tr.19–20).

Hai phía chỉ khôi phục đúng khi chạy cùng một cặp mô hình–bộ mã trên cùng dữ kiện, gồm bốn thành phần.

::: remark Nhận xét 10.4 (Bốn thành phần của một giao thức nén)
Bên nén và bên giải nén phải dùng chung bốn thành phần:

1. bảng chữ cái và cách biểu diễn một ký hiệu chưa có trong mô hình;
2. mô hình tĩnh đã truyền, hoặc quy tắc khởi tạo và cập nhật của mô hình thích nghi;
3. quy tắc mã, gồm cả quy tắc phá hòa (tie-breaking rule) khi dựng cây và quy tắc làm tròn khi chia khoảng;
4. cách dừng: một ký hiệu kết thúc dòng `EOS` (end of stream) hoặc độ dài $n$ truyền kèm (NG, tr.52 và tr.99).
:::

Thiếu bất kỳ thành phần nào, bộ giải mã có thể đọc sai ngay cả khi nhận đúng từng bit. Bài tập sau cho một trường hợp cụ thể với thành phần thứ ba.

::: exercise Bài tập 10.1 (Hai quy tắc phá hòa)
Bảng số đếm A: 15, B: 7, C: 6, D: 6, E: 5 được truyền cho bên nhận. Quy tắc phá hòa thứ nhất ghép D với E trước, rồi B với C, cho A = `0`, B = `100`, C = `101`, D = `110`, E = `111`; quy tắc thứ hai quét số đếm theo thứ tự A–E với phép so sánh chặt, ghép E với C trước, rồi D với B, cho A = `0`, E = `100`, C = `101`, D = `110`, B = `111` (NG, tr.35–36, 62–63). Bên nén dùng mã thứ nhất, bên giải nén dùng mã thứ hai. Giải mã dòng bit `100111` ở bên nhận và so với thông điệp gốc. Chỉ ra thành phần của Nhận xét 10.4 chưa được hai phía thống nhất.
:::

::: hint
Mã hóa thông điệp gốc bằng mã thứ nhất trước.
:::

::: solution
Bên nén mã thông điệp BE thành `100` `111`. Bên nhận đọc `100` thành E và `111` thành B, nên được EB, sai cả hai ký hiệu dù không bit nào bị lỗi.

Hai phía có chung bảng chữ cái, chung bảng số đếm và chung cách dừng; thành phần còn thiếu là quy tắc phá hòa, một phần của quy tắc mã (thành phần 3). Trên thông điệp 39 ký hiệu của Ví dụ 10.1, hai cây có cùng chi phí $87$ bit, nên quy tắc phá hòa không ảnh hưởng tới độ dài mà chỉ ảnh hưởng tới tính đúng của giải mã.
:::

Như vậy, chúng ta đã có đặc tả của bài toán (Định nghĩa 10.1), biết rằng mọi bộ nén đều phải đánh cược vào một mô hình (Mệnh đề 10.2), và đã tách bộ nén thành mô hình, bộ mã cùng bốn thành phần của giao thức (Định nghĩa 10.3, Nhận xét 10.4). Tuy nhiên, Định nghĩa 10.1 chưa cho cách kiểm một mã có giải mã duy nhất không, và chưa cho biết một ký hiệu xác suất $p$ nên nhận từ mã dài bao nhiêu bit. Trong Mục 2, chúng ta trả lời hai câu hỏi đó bằng mã tiền tố, bất đẳng thức Kraft và entropy.

## 2. Mã tiền tố, bất đẳng thức Kraft và entropy

Để chọn độ dài từ mã cho A–E mà vẫn giải mã được, chúng ta cần một điều kiện trên các từ mã, một tiêu chuẩn cho bộ độ dài và một thước đo số bit tối thiểu.

<!-- note-topic-id: lec-10-topic-04 -->
### 2.1 Mã tiền tố và cây mã

Trong mã $\mathrm a=1$, $\mathrm b=01$, $\mathrm c=101$, $\mathrm d=011$, từ mã `1` của a là phần đầu của từ mã `101` của c. Sau khi đọc bit `1`, bộ giải mã không biết đã hết một từ mã hay mới bắt đầu một từ mã dài hơn.

::: definition Định nghĩa 10.5 (Mã tiền tố và cây mã)
- Chuỗi bit $u$ là **tiền tố** (prefix) của chuỗi bit $u'$ khi $u'$ là $u$ nối thêm một chuỗi bit, có thể rỗng; tiền tố là **thực sự** khi phần nối thêm khác rỗng.
- Mã ký hiệu $c$ là **mã tiền tố** (prefix code, còn gọi là prefix-free code hay mã tức thời, instantaneous code) khi với mọi hai ký hiệu $s\ne s'$, từ mã $c(s)$ không là tiền tố của $c(s')$.
- **Cây mã** (code tree) của $c$ là cây nhị phân có các nút là mọi tiền tố của mọi từ mã; gốc là chuỗi rỗng, con trái của nút $u$ là $u0$ và con phải là $u1$, khi chuỗi đó là tiền tố của một từ mã. Độ sâu của nút $u$ bằng $\lvert u\rvert$.
:::

Điều kiện chỉ xét từng cặp từ mã, nên kiểm được bằng $\binom k2$ phép so sánh; vì phần nối thêm được phép rỗng, các từ mã của mã tiền tố đôi một khác nhau. Mã độ dài cố định là mã tiền tố.

::: example Ví dụ 10.3 (Hai mã cho A–E)
**Dữ kiện.** Hai mã cho bảng chữ cái của Ví dụ 10.1:

- mã Huffman (NG, tr.36): A = `0`, B = `100`, C = `101`, D = `110`, E = `111`;
- mã Shannon–Fano (NG, tr.31): A = `00`, B = `01`, C = `10`, D = `110`, E = `111`.

**Kiểm điều kiện tiền tố.** Ở mã thứ nhất, `0` là từ mã duy nhất bắt đầu bằng bit 0; bốn từ mã còn lại cùng dài 3 bit và đôi một khác nhau. Ở mã thứ hai, ba từ mã 2 bit đôi một khác nhau, và hai từ mã 3 bit bắt đầu bằng `11`, không trùng với `00`, `01`, `10`. Cả hai là mã tiền tố.

**Giải mã.** Trên mã thứ nhất, đọc dòng `0101100111` từ trái sang phải và cắt ngay khi phần đã đọc là một từ mã:

- `0` là từ mã của A;
- `1`, `10` chưa là từ mã, `101` là từ mã của C;
- `100` là từ mã của B;
- `111` là từ mã của E.

Thông điệp là ACBE.

**Kiểm tra lại.** $1+3+3+3=10$ bit, bằng độ dài dòng, và $c^*(\mathrm{ACBE})=$ `0` `101` `100` `111`.
:::

Một cách trực quan, cây mã là một trò chơi hỏi–đáp: mỗi bit trả lời một câu hỏi có–không, và từ mã là đường đi từ gốc tới câu trả lời cuối cùng (EE398A-1, trang chiếu 3–4). Từ mã $c(s)$ là tiền tố của $c(s')$ đúng khi nút $c(s)$ là tổ tiên của nút $c(s')$ trên cây mã. Mã tiền tố là mã mà không từ mã nào nằm trên đường đi tới một từ mã khác, tức mọi từ mã là lá.

::: proposition Mệnh đề 10.6 (Mã tiền tố, cây mã và giải mã tức thời)
**Giả thiết.** $c$ là một mã ký hiệu trên $\Sigma$.

**Kết luận.**

- (a) $c$ là mã tiền tố khi và chỉ khi $c$ là đơn ánh và các lá của cây mã của $c$ đúng là các từ mã của $c$.
- (b) Nếu $c$ là mã tiền tố thì $c$ giải mã duy nhất.
- (c) Nếu $c$ là mã tiền tố, thủ tục đi từ gốc theo từng bit, phát ký hiệu khi tới một lá rồi quay về gốc, giải đúng mọi dòng $c^*(x)$; mỗi ký hiệu được nhận ra ngay khi đọc bit cuối của từ mã của nó.

**Điều kiện áp dụng.** Chỉ dùng điều kiện tiền tố của Định nghĩa 10.5; không cần xác suất.

**Phạm vi.** Chiều ngược của (b) sai: có mã giải mã duy nhất không là mã tiền tố (Bài tập 10.10). Thủ tục ở (c) cần biết khi nào dừng, bằng `EOS` hoặc độ dài $n$.
:::

::: proof
**Bước 1 (phần (a)).** Một nút $u$ của cây mã là nút trong khi và chỉ khi $u$ là tiền tố thực sự của một từ mã, vì khi đó $u0$ hoặc $u1$ là tiền tố của từ mã đó. Một lá $u$ của cây mã là tiền tố của một từ mã nhưng không là tiền tố thực sự của từ mã nào, nên $u$ là chính từ mã đó; vậy mọi lá là từ mã. Do đó các lá đúng là các từ mã khi và chỉ khi không từ mã nào là nút trong, tức không từ mã nào là tiền tố thực sự của một từ mã khác. Cùng với việc các từ mã đôi một khác nhau, đó là điều kiện tiền tố.

**Bước 2 (phần (b), quy nạp theo $\lvert x\rvert+\lvert y\rvert$).** Giả sử $c^*(x)=c^*(y)$; ta chứng minh $x=y$. Nếu một trong hai thông điệp rỗng thì dòng bit chung rỗng, nên thông điệp kia cũng rỗng, vì mọi từ mã khác rỗng. Nếu cả hai khác rỗng, $c(x_1)$ và $c(y_1)$ cùng là phần đầu của một dòng bit, nên chuỗi ngắn hơn là tiền tố của chuỗi dài hơn. Theo điều kiện tiền tố, điều này chỉ xảy ra khi $x_1=y_1$. Bỏ từ mã chung ở đầu hai dòng, ta được $c^*(x_2\cdots)=c^*(y_2\cdots)$ với tổng độ dài nhỏ hơn, và giả thiết quy nạp cho $x_2\cdots=y_2\cdots$.

**Bước 3 (phần (c)).** Sau khi thủ tục đã phát đúng $x_1,\ldots,x_{t-1}$ và đứng ở gốc, các bit tiếp theo bắt đầu bằng $c(x_t)$. Đi theo các bit đó, thủ tục qua các tiền tố thực sự của $c(x_t)$, là các nút trong theo Bước 1, và tới lá $c(x_t)$ đúng ở bit cuối của từ mã. Vậy ký hiệu thứ $t$ được phát đúng và thủ tục trở về gốc ở đầu từ mã tiếp theo; quy nạp theo $t$ cho kết luận. $\square$
:::

Thủ tục ở (c) tốn một bước đi xuống cây cho mỗi bit đọc vào, nên giải mã $c^*(x)$ tốn $\sum_t\ell_{x_t}$ bước. Đây cũng là cách giải mã của thuật toán Huffman tĩnh (NG, tr.55).

![Phía trên: cây mã của mã A = 0, B = 100, C = 101, D = 110, E = 111, đường 1, 0, 1 tới C được tô đậm. Phía dưới: đoạn từ 0 tới 1 chia thành năm khoảng mã, từ 0 tới 0,5 cho từ mã 0 và bốn khoảng rộng 1/8 cho 100, 101, 110, 111.](img/lec-10/note-cay-ma-khoang-kraft.svg)

Phần trên của hình là cây mã của mã Huffman A–E: năm từ mã là năm lá, đường tô đậm là ba bước đi xuống khi giải mã `101` thành C ở Ví dụ 10.3. Phần dưới được đọc ở tiểu mục sau.

<!-- note-topic-id: lec-10-topic-05 -->
### 2.2 Khoảng mã và bất đẳng thức Kraft

Không phải bộ độ dài nào cũng dùng được. Với ba ký hiệu và độ dài $(1,1,2)$, hai từ mã 1 bit phải là `0` và `1`, và mọi chuỗi 2 bit đều nhận một trong hai làm tiền tố, nên không còn chỗ cho ký hiệu thứ ba. Chúng ta cần một tiêu chuẩn quyết định một bộ độ dài có là độ dài của một mã tiền tố không.

Một cách trực quan, mỗi từ mã độ dài $\ell$ chiếm một phần độ rộng $2^{-\ell}$ của đoạn $[0;1)$, và các từ mã của một mã tiền tố không được chiếm chồng lên nhau. Chúng ta gán cho mỗi chuỗi bit phần đoạn đó.

::: definition Định nghĩa 10.7 (Khoảng mã và tổng Kraft)
- Với chuỗi bit $u=b_1\cdots b_\ell$, $\ell\ge1$, đặt $z(u)=0{,}b_1\cdots b_\ell$ (cơ số 2) $=\sum_{i=1}^{\ell}b_i2^{-i}$. **Khoảng mã** (code interval) của $u$ là khoảng nửa mở
$$
J(u)=\bigl[z(u);\,z(u)+2^{-\ell}\bigr).
$$
- **Tổng Kraft** (Kraft sum) của bộ độ dài nguyên dương $(\ell_s)_{s\in\Sigma}$ là
$$
K=\sum_{s\in\Sigma}2^{-\ell_s}.
$$
:::

Khoảng mã $J(u)$ gồm đúng các số trong $[0;1)$ có khai triển nhị phân bắt đầu bằng $u$, nếu với mỗi số ta chọn khai triển không kết thúc bằng dãy 1 vô hạn (CMU, trang chiếu 45–46). Độ rộng của $J(u)$ là $2^{-\lvert u\rvert}$, nên tổng Kraft của một mã bằng tổng độ rộng các khoảng mã của nó. Phần dưới của hình trên vẽ năm khoảng mã của mã Huffman A–E: $J(\texttt{0})=[0;\,0{,}5)$ và bốn khoảng rộng $1/8$ từ $0{,}5$ tới $1$; năm khoảng rời nhau, phủ kín $[0;1)$, và tổng Kraft bằng $1/2+4\cdot1/8=1$.

Quan hệ tiền tố ứng với quan hệ giữa các khoảng mã như sau.

::: lemma Bổ đề 10.8 (Tiền tố và khoảng mã)
**Giả thiết.** $u$, $u'$ là hai chuỗi bit khác rỗng.

**Kết luận.**

- (a) Nếu $u$ là tiền tố của $u'$ thì $J(u')\subseteq J(u)$.
- (b) Nếu không chuỗi nào là tiền tố của chuỗi kia thì $J(u)\cap J(u')=\varnothing$.
- (c) Một tập chuỗi bit có điều kiện tiền tố (không chuỗi nào là tiền tố của chuỗi khác) khi và chỉ khi các khoảng mã của chúng đôi một rời nhau.

**Điều kiện áp dụng.** Khoảng mã là nửa mở.

**Phạm vi.** Phần (a), (b) so hai chuỗi; phần (c) cho một tập chuỗi và đòi điều kiện trên mọi cặp.
:::

::: proof
Đặt $\ell=\lvert u\rvert$ và $\operatorname{val}(u)=2^{\ell}z(u)$, số nguyên có biểu diễn nhị phân là $u$, với $0\le\operatorname{val}(u)\le2^\ell-1$.

**Bước 1 (phần (a)).** Đặt $\ell'=\lvert u'\rvert\ge\ell$ và gọi $e$ là số nguyên biểu diễn bởi $\ell'-\ell$ bit cuối của $u'$, với $e=0$ khi $\ell'=\ell$. Vì $u'$ bắt đầu bằng $u$, $z(u')=z(u)+2^{-\ell'}e$ với $0\le e\le2^{\ell'-\ell}-1$. Do đó $z(u')\ge z(u)$ và
$$
\begin{aligned}
z(u')+2^{-\ell'}&\le z(u)+2^{-\ell'}2^{\ell'-\ell}\\
&=z(u)+2^{-\ell}.
\end{aligned}
$$
Hai bất đẳng thức cho $J(u')\subseteq J(u)$.

**Bước 2 (phần (b)).** Giả sử $\ell\le\lvert u'\rvert$ và gọi $u''$ là $\ell$ bit đầu của $u'$. Vì $u$ không là tiền tố của $u'$, $u''\ne u$. Các khoảng $[j2^{-\ell};\,(j+1)2^{-\ell})$ với $j=0,\ldots,2^\ell-1$ rời nhau, và $J(u)$, $J(u'')$ là hai khoảng khác nhau trong số đó, ứng với $j=\operatorname{val}(u)\ne\operatorname{val}(u'')$. Theo Bước 1, $J(u')\subseteq J(u'')$, nên $J(u')\cap J(u)=\varnothing$. Trường hợp $\ell>\lvert u'\rvert$ đổi vai hai chuỗi.

**Bước 3 (phần (c)).** Nếu tập có điều kiện tiền tố, mọi cặp rơi vào phần (b), nên các khoảng mã đôi một rời nhau. Ngược lại, nếu một chuỗi là tiền tố của chuỗi khác, phần (a) cho hai khoảng lồng nhau; hai khoảng này khác rỗng nên giao nhau. $\square$
:::

Bỏ "nửa mở" thì (b) sai: `0` và `1` không là tiền tố của nhau, nhưng hai khoảng đóng $[0;\tfrac12]$ và $[\tfrac12;1]$ chung điểm $\tfrac12$.

Để làm rõ, ta kiểm tổng Kraft của các bộ độ dài đã gặp, rồi dựng một mã tiền tố từ một bộ độ dài bằng cách xếp các khoảng mã liền nhau từ trái sang phải.

::: example Ví dụ 10.4 (Bốn tổng Kraft và một mã dựng từ độ dài)
**Dữ kiện.** Bốn bộ độ dài:

- $(1,1,2)$ cho ba ký hiệu;
- $(1,3,3,3,3)$ của mã Huffman A–E;
- $(2,2,2,3,3)$ của mã Shannon–Fano A–E;
- $(2,3,3,3,3)$ cho A–E.

**Tổng Kraft.**

- $(1,1,2)$: $K=\tfrac12+\tfrac12+\tfrac14=1{,}25$;
- $(1,3,3,3,3)$: $K=\tfrac12+4\cdot\tfrac18=1$;
- $(2,2,2,3,3)$: $K=3\cdot\tfrac14+2\cdot\tfrac18=1$;
- $(2,3,3,3,3)$: $K=\tfrac14+4\cdot\tfrac18=0{,}75$.

**Dựng mã cho $(2,3,3,3,3)$.** Xếp độ dài tăng dần và đặt điểm đầu của khoảng thứ $i$ bằng tổng độ rộng các khoảng trước nó, $z_i=\sum_{j<i}2^{-\ell_j}$:

| $i$ | $\ell_i$ | $z_i$ | $z_i$ viết $\ell_i$ bit | khoảng mã |
|---|---|---|---|---|
| 1 | 2 | $0$ | `00` | $[0;\,0{,}25)$ |
| 2 | 3 | $1/4$ | `010` | $[0{,}25;\,0{,}375)$ |
| 3 | 3 | $3/8$ | `011` | $[0{,}375;\,0{,}5)$ |
| 4 | 3 | $1/2$ | `100` | $[0{,}5;\,0{,}625)$ |
| 5 | 3 | $5/8$ | `101` | $[0{,}625;\,0{,}75)$ |

**Kiểm tra lại.** Năm khoảng nằm liền nhau trong $[0;\,0{,}75)$ nên rời nhau, và theo Bổ đề 10.8(c) năm từ mã `00`, `010`, `011`, `100`, `101` có điều kiện tiền tố; phần $[0{,}75;\,1)$ còn trống ứng với tổng Kraft $0{,}75<1$.
:::

Bộ $(1,1,2)$ có tổng lớn hơn 1, đúng bộ không có mã tiền tố. Tổng Kraft quyết định hoàn toàn câu hỏi này.

::: theorem Định lý 10.9 (Bất đẳng thức Kraft cho mã tiền tố)
**Giả thiết.** $(\ell_s)_{s\in\Sigma}$ là một bộ số nguyên dương, $K=\sum_s2^{-\ell_s}$.

**Kết luận.**

- (a) Nếu $c$ là mã tiền tố với $\lvert c(s)\rvert=\ell_s$ thì $K\le1$.
- (b) Nếu $K\le1$ thì có mã tiền tố $c$ với $\lvert c(s)\rvert=\ell_s$ cho mọi $s$.
- (c) Với $c$ là mã tiền tố, $K=1$ khi và chỉ khi cây mã của $c$ là cây nhị phân đầy đủ.

**Điều kiện áp dụng.** Phần (a) cần điều kiện tiền tố; phần (b) chỉ cần các độ dài nguyên dương.

**Phạm vi.** Định lý nói về độ dài, không nói về xác suất hay về một bộ từ mã cụ thể: mã $\mathrm a=1$, $\mathrm b=01$, $\mathrm c=101$, $\mathrm d=011$ có $K=1$ nhưng không giải mã duy nhất.
:::

::: proof
**Bước 1 (phần (a)).** Theo Mệnh đề 10.6(a), các từ mã là các chuỗi đôi một không là tiền tố của nhau, nên theo Bổ đề 10.8(c) các khoảng mã $J(c(s))$ đôi một rời nhau. Chúng đều nằm trong $[0;1)$, nên tổng độ rộng không vượt 1:
$$
K=\sum_{s}2^{-\ell_s}\le1 .
$$

**Bước 2 (phần (b), dựng mã).** Đánh số các ký hiệu $\varsigma_1,\ldots,\varsigma_k$ sao cho $\ell_1\le\ell_2\le\cdots\le\ell_k$, với $\ell_i=\ell_{\varsigma_i}$, và đặt $z_i=\sum_{j<i}2^{-\ell_j}$. Mỗi số hạng $2^{-\ell_j}$ với $j<i$ là bội của $2^{-\ell_i}$ vì $\ell_j\le\ell_i$, nên $2^{\ell_i}z_i$ là số nguyên. Hơn nữa
$$
z_i+2^{-\ell_i}=z_{i+1}\le z_{k+1}=K\le1,
$$
nên $0\le2^{\ell_i}z_i\le2^{\ell_i}-1$. Gán cho $\varsigma_i$ chuỗi $\ell_i$ bit biểu diễn số nguyên $2^{\ell_i}z_i$; khi đó $z(c(\varsigma_i))=z_i$ và $J(c(\varsigma_i))=[z_i;\,z_{i+1})$.

**Bước 3 (phần (b), điều kiện tiền tố).** Các khoảng $[z_1;z_2)$, $[z_2;z_3)$, …, $[z_k;z_{k+1})$ nằm liền nhau nên đôi một rời nhau. Theo Bổ đề 10.8(c), các từ mã đôi một không là tiền tố của nhau, tức $c$ là mã tiền tố với đúng các độ dài $\ell_s$.

**Bước 4 (phần (c), cây đầy đủ cho $K=1$).** Quy nạp theo số lá $k\ge2$. Với $k=2$, cây đầy đủ có hai lá ở độ sâu 1 và $K=1/2+1/2=1$. Với $k\ge3$, lấy một lá $u$ ở độ sâu lớn nhất $d$. Vì cây đầy đủ, cha của $u$ có thêm một con $u'$; $u'$ là lá vì một nút trong ở độ sâu $d$ sẽ có con ở độ sâu $d+1$. Bỏ hai lá $u$, $u'$ thì cha của chúng thành lá ở độ sâu $d-1$, cây vẫn đầy đủ với $k-1$ lá, và tổng Kraft thay đổi
$$
2^{-(d-1)}-2\cdot2^{-d}=0 .
$$
Theo giả thiết quy nạp, tổng của cây nhỏ hơn bằng 1, nên tổng của cây ban đầu bằng 1.

**Bước 5 (phần (c), cây không đầy đủ cho $K<1$).** Nếu một nút trong $v$ ở độ sâu $d$ chỉ có một con, thêm con còn thiếu làm một từ mã mới. Mã mới vẫn là mã tiền tố, vì từ mã mới không có hậu duệ trên cây và tổ tiên của nó là các nút trong, không là từ mã. Theo phần (a), $K+2^{-(d+1)}\le1$, nên $K<1$. $\square$
:::

Tóm lại, một bộ độ dài nguyên dương là bộ độ dài của một mã tiền tố khi và chỉ khi $K\le1$. Ví dụ 10.4 là Bước 2 và Bước 3 chạy trên $(2,3,3,3,3)$; theo Bước 2, $z_6=K=0{,}75$, nên mã để trống $[0{,}75;1)$, đúng khoảng mã của `11`, nên đổi `101` thành `11` vẫn cho mã tiền tố, với độ dài $(2,3,3,3,2)$ và $K=7/8$.

Các phản ví dụ sau cho thấy từng giả thiết đều cần:

- Bỏ "mã tiền tố" ở (a): mã `0`, `01`, `10`, `11` cho bốn ký hiệu có $K=1/2+3/4=1{,}25>1$, và nó không giải mã duy nhất, vì `01011001` đọc được theo hai cách (EE398A-1, trang chiếu 12).
- Bỏ "mã tiền tố" ở (c): mã $\mathrm a=1$, $\mathrm b=01$, $\mathrm c=101$, $\mathrm d=011$ có $K=1$, nhưng trên cây mã của nó nút `0` chỉ có một con là `01`, nên cây không đầy đủ.

Bước 1 dùng điều kiện tiền tố qua Bổ đề 10.8; Bước 4 dùng Mệnh đề 10.6(a) để $K$ là tổng của $2^{-\text{độ sâu}}$ trên các lá; Bước 5 dùng điều kiện tiền tố để từ mã mới vẫn cho một mã tiền tố.

**Trong thực hành.** Bước 2 chỉ cần bộ độ dài và thứ tự ký hiệu, nên hai phía biết cùng bộ độ dài dựng được cùng một mã tiền tố mà không trao đổi từ mã. Tổng $K$ cũng là phép kiểm một bảng độ dài: $K>1$ thì không có mã tiền tố nào, $K<1$ thì còn một khoảng trống để rút ngắn ít nhất một từ mã.

::: remark Nhận xét 10.10 (Mã giải mã duy nhất và bất đẳng thức McMillan)
Phần (a) còn đúng khi thay "mã tiền tố" bằng "mã giải mã duy nhất": mọi mã giải mã duy nhất có $K\le1$ (bất đẳng thức McMillan; CMU, trang chiếu 28; EE398A-1, trang chiếu 13). Chứng minh nằm ngoài phạm vi học phần; ý chính là đếm các dòng bit sinh bởi thông điệp $n$ ký hiệu qua lũy thừa $K^n$. Theo phần (b), mọi bộ độ dài của một mã giải mã duy nhất cũng là bộ độ dài của một mã tiền tố, nên khi tìm mã ngắn nhất chỉ cần xét mã tiền tố.
:::

::: exercise Bài tập 10.2 (Kiểm và dựng theo tổng Kraft)
Với mỗi bộ độ dài sau, tính tổng Kraft, cho biết có mã tiền tố với đúng các độ dài đó không, và nếu có thì dựng một mã theo Bước 2 của chứng minh Định lý 10.9:

- $(2,2,2,2,3)$;
- $(1,3,3,3,4)$;
- $(2,2,2,3,4,4)$, bộ độ dài của mã `00`, `01`, `10`, `111`, `1100`, `1101` (EE398A-1, trang chiếu 15).
:::

::: hint
Tính $K$ bằng phân số có mẫu $2^{\ell_{\max}}$; với bộ khả thi, sắp độ dài tăng dần và lập bảng $z_i$ như Ví dụ 10.4.
:::

::: solution
**Bộ $(2,2,2,2,3)$.** $K=4\cdot\tfrac14+\tfrac18=\tfrac98>1$, nên theo Định lý 10.9(a) không có mã tiền tố nào.

**Bộ $(1,3,3,3,4)$.** $K=\tfrac12+3\cdot\tfrac18+\tfrac1{16}=\tfrac{15}{16}\le1$. Các điểm đầu là $z_1=0$, $z_2=\tfrac12$, $z_3=\tfrac58$, $z_4=\tfrac34$, $z_5=\tfrac78$, cho các từ mã `0`, `100`, `101`, `110`, `1110`. Khoảng $[\tfrac{15}{16};1)$ còn trống, đúng như $K<1$.

**Bộ $(2,2,2,3,4,4)$.** $K=3\cdot\tfrac14+\tfrac18+2\cdot\tfrac1{16}=1$. Các điểm đầu là $0$, $\tfrac14$, $\tfrac12$, $\tfrac34$, $\tfrac78$, $\tfrac{15}{16}$, cho `00`, `01`, `10`, `110`, `1110`, `1111`. Mã này khác mã cho trong đề nhưng có cùng bộ độ dài; cả hai có $K=1$, nên theo Định lý 10.9(c) cây mã của cả hai đều đầy đủ.
:::

<!-- note-topic-id: lec-10-topic-06 -->
### 2.3 Tự thông tin và entropy

Theo Định lý 10.9, các mã tiền tố cho A–E có thể dùng bộ độ dài $(1,3,3,3,3)$ với $87$ bit hay $(2,2,2,3,3)$ với $15\cdot2+7\cdot2+6\cdot2+6\cdot3+5\cdot3=89$ bit. Để biết 87 bit là tốt hay chưa, chúng ta cần một mức đích không phụ thuộc vào một mã cụ thể. Chuỗi "eeeee" của Mục 1 gợi ý mức đích đó: một ký hiệu xác suất $1/16$ mang $\log_2 16=4$ bit.

::: definition Định nghĩa 10.11 (Tự thông tin, entropy và độ dài trung bình)
Cho phân phối $P=(p_s)_{s\in\Sigma}$ với mọi $p_s>0$.

- **Tự thông tin** (self-information, còn gọi là lượng thông tin, information content) của ký hiệu $s$ là
$$
I(s)=-\log_2p_s\ \text{bit}.
$$
- Với mô hình tĩnh $P$, tự thông tin của thông điệp $x=x_1\cdots x_n$ là
$$
I(x)=\sum_{t=1}^{n}I(x_t)=-\log_2\prod_{t=1}^{n}p_{x_t}.
$$
- **Entropy** (entropy) của $P$ là kỳ vọng của tự thông tin:
$$
H(P)=\sum_{s\in\Sigma}p_s\log_2\frac1{p_s}.
$$
- **Độ dài trung bình** (average length, expected code length) của mã $c$ theo $P$ là $\bar\ell(c)=\sum_sp_s\ell_s$. Một mã tiền tố là **mã tiền tố tối ưu** (optimal prefix code) cho $P$ khi $\bar\ell(c)$ nhỏ nhất trong mọi mã tiền tố trên $\Sigma$ (CMU, trang chiếu 26).
- Với số đếm $f$, một **cây tối ưu** là cây mã có $k$ lá mang tên các ký hiệu làm nhỏ nhất $\operatorname{cost}(T)=\sum_sf_s\operatorname{depth}_T(s)$.
:::

Ký hiệu hiếm có tự thông tin lớn. Entropy là trung bình của $I(s)$ theo $P$, cùng đơn vị bit mỗi ký hiệu với $\bar\ell(c)$: một bên là đích, một bên là chi phí của mã. Khi $p_s=f_s/N$ lấy từ chính thông điệp, với $N=n$, ta có hai đẳng thức dùng nhiều lần:
$$
\begin{gathered}
N\,\bar\ell(c)=\sum_sf_s\ell_s,\\
N\,H(P)=\sum_sf_sI(s)=I(x).
\end{gathered}
$$
Vế trái của đẳng thức thứ nhất là số bit của $c^*(x)$; với cây mã $T$ của $c$, nó bằng $\operatorname{cost}(T)=\sum_sf_s\operatorname{depth}_T(s)$.

::: example Ví dụ 10.5 (Tự thông tin và entropy)
**Dữ kiện.** Thông điệp A–E của Ví dụ 10.1: A: 15, B: 7, C: 6, D: 6, E: 5, $N=39$; mô hình $p_s=f_s/39$.

**Tính.** Tự thông tin của từng ký hiệu và phần đóng góp $f_sI(s)$ (NG, tr.33):

| $s$ | $f_s$ | $I(s)$ (bit) | $f_sI(s)$ (bit) |
|---|---|---|---|
| A | 15 | $1{,}38$ | $20{,}68$ |
| B | 7 | $2{,}48$ | $17{,}35$ |
| C | 6 | $2{,}70$ | $16{,}20$ |
| D | 6 | $2{,}70$ | $16{,}20$ |
| E | 5 | $2{,}96$ | $14{,}82$ |

Tổng $I(x)\approx85{,}25$ bit, giá trị chính xác hơn là $85{,}247$ bit; entropy là $H(P)=85{,}247/39\approx2{,}186$ bit mỗi ký hiệu.

**Ba phân phối khác** (CMU, trang chiếu 14):

- ba xác suất $0{,}25$ và hai xác suất $0{,}125$: $H=2{,}25$;
- một xác suất $0{,}5$ và bốn xác suất $0{,}125$: $H=2$;
- một xác suất $0{,}75$ và bốn xác suất $0{,}0625$: $H\approx1{,}31$.

**Kiểm tra lại.** $20{,}68+17{,}35+16{,}20+16{,}20+14{,}82=85{,}25$.
:::

Một cách trực quan, ký hiệu xác suất $2^{-\ell}$ ứng với một lá ở độ sâu $\ell$, vì mỗi bit chia đôi khả năng còn lại (EE398A-1, trang chiếu 6). Phân phối càng lệch thì entropy càng nhỏ, và $0\le H(P)\le\log_2k$ với giá trị lớn nhất khi phân phối đều (EE398A-1, trang chiếu 8); với năm ký hiệu, $\log_25\approx2{,}32$.

Hai nhầm lẫn thường gặp cần tách ra. Thứ nhất, $-\log_2p_s$ là tự thông tin $I(s)$ và tổng của nó trên thông điệp là $I(x)$; chữ entropy chỉ dùng cho kỳ vọng $H(P)$. Thứ hai, entropy là của một mô hình, không phải của văn bản: chữ 'u' của Ví dụ 10.2 có tự thông tin $6{,}64$ bit hay $0{,}074$ bit tùy mô hình.

<!-- note-topic-id: lec-10-topic-07 -->
### 2.4 Cận entropy cho mã tiền tố

Thông điệp A–E có $I(x)\approx85{,}25$ bit. Để dùng con số này làm đích, chúng ta cần biết hai điều: không mã tiền tố nào xuống dưới nó, và luôn có mã tiền tố đến đủ gần nó.

::: theorem Định lý 10.12 (Cận dưới entropy; phần cận dưới của định lý mã hóa không nhiễu của Shannon, Shannon's noiseless coding theorem)
**Giả thiết.** $P=(p_s)_{s\in\Sigma}$ là phân phối với mọi $p_s>0$; $c$ là mã tiền tố trên $\Sigma$ với độ dài $\ell_s$.

**Kết luận.** $\bar\ell(c)\ge H(P)$, dấu bằng xảy ra khi và chỉ khi $p_s=2^{-\ell_s}$ với mọi $s$.

**Điều kiện áp dụng.** $P$ là phân phối của chính mô hình dùng để đo $\bar\ell(c)$; với một bảng mã dựng từ dữ liệu khác, cận nói về phân phối của bảng chứ không về tệp đang nén (Tình huống 10.3(a)).

**Phạm vi.** Cận nói về độ dài trung bình theo $P$, không về một thông điệp cụ thể. Theo Nhận xét 10.10, kết luận vẫn đúng cho mã giải mã duy nhất.
:::

::: proof
Ta viết $H(P)-\bar\ell(c)$ thành một tổng có dạng $\sum_sp_s\log_2\xi_s$, chặn từng logarit bằng $\ln\xi\le\xi-1$, rồi dùng tổng Kraft.

**Bước 1 (gộp hai tổng).** Vì $\ell_s=\log_22^{\ell_s}$,
$$
\begin{aligned}
&H(P)-\bar\ell(c)\\
&\quad=\sum_sp_s\Bigl(\log_2\frac1{p_s}-\log_22^{\ell_s}\Bigr)\\
&\quad=\sum_sp_s\log_2\frac{2^{-\ell_s}}{p_s}.
\end{aligned}
$$

**Bước 2 (chặn từng logarit).** Đặt $\xi_s=2^{-\ell_s}/p_s>0$. Theo $\log_2\xi=\ln\xi/\ln2$ và $\ln\xi\le\xi-1$, cùng với $p_s>0$,
$$
\begin{aligned}
&\sum_sp_s\log_2\xi_s\\
&\quad\le\frac1{\ln2}\sum_sp_s(\xi_s-1)\\
&\quad=\frac1{\ln2}\Bigl(\sum_s2^{-\ell_s}-\sum_sp_s\Bigr)\\
&\quad=\frac1{\ln2}(K-1).
\end{aligned}
$$
Đẳng thức thứ nhất dùng $p_s\xi_s=2^{-\ell_s}$, đẳng thức thứ hai dùng $\sum_sp_s=1$.

**Bước 3 (dùng Kraft).** Vì $c$ là mã tiền tố, Định lý 10.9(a) cho $K\le1$, nên vế phải không dương và $H(P)-\bar\ell(c)\le0$.

**Bước 4 (dấu bằng).** Dấu bằng xảy ra khi và chỉ khi cả Bước 2 và Bước 3 là đẳng thức. Bước 2 là đẳng thức khi và chỉ khi $\ln\xi_s=\xi_s-1$, tức $\xi_s=1$, với mọi $s$, vì mọi trọng số $p_s$ dương. Khi đó $p_s=2^{-\ell_s}$ và $K=\sum_sp_s=1$, nên Bước 3 cũng là đẳng thức. Ngược lại, nếu $p_s=2^{-\ell_s}$ với mọi $s$ thì $\bar\ell(c)=\sum_sp_s\log_2(1/p_s)=H(P)$. $\square$
:::

Ở chiều ngược lại, có mã tiền tố cách đích $H(P)$ dưới 1 bit mỗi ký hiệu.

::: theorem Định lý 10.13 (Cận trên: độ dài Shannon)
**Giả thiết.** $P=(p_s)_{s\in\Sigma}$ là phân phối với mọi $p_s>0$, $k\ge2$. Đặt $\ell_s=\lceil-\log_2p_s\rceil$, gọi là độ dài Shannon của $s$.

**Kết luận.** Có mã tiền tố $c$ với đúng các độ dài $\ell_s$, và $\bar\ell(c)<H(P)+1$.

**Điều kiện áp dụng.** Mọi $p_s>0$ và $k\ge2$, để mọi độ dài Shannon là số nguyên dương; với $k=1$, $p_s=1$ cho $\ell_s=0$.

**Phạm vi.** Mã của định lý không nhất thiết tối ưu: ở A–E nó tốn 102 bit so với 87 bit (Ví dụ 10.6); định lý cho biết mã tiền tố tối ưu có $\bar\ell<H(P)+1$.
:::

::: proof
**Bước 1 (độ dài hợp lệ).** Vì $k\ge2$ và mọi $p_s>0$, mỗi $p_s<1$, nên $-\log_2p_s>0$ và $\ell_s\ge1$ là số nguyên dương.

**Bước 2 (tổng Kraft).** Từ $\ell_s\ge-\log_2p_s$ suy ra $2^{-\ell_s}\le p_s$, nên
$$
K=\sum_s2^{-\ell_s}\le\sum_sp_s=1 .
$$
Theo Định lý 10.9(b), có mã tiền tố $c$ với các độ dài $\ell_s$.

**Bước 3 (độ dài trung bình).** Theo $\lceil\upsilon\rceil<\upsilon+1$, $\ell_s<-\log_2p_s+1$. Nhân với $p_s>0$ rồi cộng theo $s$:
$$
\begin{aligned}
\bar\ell(c)&=\sum_sp_s\ell_s\\
&<\sum_sp_s\Bigl(\log_2\frac1{p_s}+1\Bigr)\\
&=H(P)+1.\qquad\square
\end{aligned}
$$
:::

::: example Ví dụ 10.6 (Độ dài Shannon cho A–E)
**Dữ kiện.** Tự thông tin của Ví dụ 10.5: $I(\mathrm A)=1{,}38$, $I(\mathrm B)=2{,}48$, $I(\mathrm C)=I(\mathrm D)=2{,}70$, $I(\mathrm E)=2{,}96$ bit; số đếm 15, 7, 6, 6, 5.

**Tính.** Làm tròn lên được độ dài Shannon $(2,3,3,3,3)$. Bộ độ dài này có tổng Kraft $0{,}75$ (Ví dụ 10.4), và mã dựng ở Ví dụ 10.4 dùng
$$
15\cdot2+(7+6+6+5)\cdot3=30+72=102\ \text{bit}.
$$

**Đọc hai định lý.** Theo bit cho cả thông điệp, $I(x)\approx85{,}25$, nên $I(x)\le102<I(x)+39\approx124{,}25$; theo bit mỗi ký hiệu, $2{,}186\le2{,}615<3{,}186$.

**Kiểm tra lại.** Mã Huffman A–E dùng 87 bit, nằm giữa $85{,}25$ và $102$, nên mã của Định lý 10.13 không tối ưu ở đây.
:::

Hai định lý kẹp mã tiền tố tối ưu trong khoảng $[H(P);\,H(P)+1)$ bit mỗi ký hiệu, hay $[I(x);\,I(x)+N)$ bit cho thông điệp khi $p_s=f_s/N$. Cận dưới đúng cho mọi mã tiền tố, còn cận trên được chứng minh bằng một mã cụ thể.

Khi bỏ một giả thiết, hai định lý có thể sai:

- Bỏ "mã tiền tố" ở Định lý 10.12: với $P=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ và mã `0`, `01`, `10`, `11`, $\bar\ell=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot2+\tfrac18\cdot2=1{,}5$, nhỏ hơn $H(P)=1{,}75$; mã này không giải mã duy nhất (EE398A-1, trang chiếu 12).
- Bỏ "mọi $p_s>0$": một ký hiệu có $p_s=0$ có tự thông tin vô hạn và không có độ dài Shannon; các ký hiệu đó bị loại khỏi bảng chữ cái của mô hình tĩnh.

Bước 3 của Định lý 10.12 dùng điều kiện tiền tố qua $K\le1$; Bước 2 của cả hai định lý dùng $p_s>0$.

**Trong thực hành.** Hai định lý nói về độ dài trung bình theo phân phối $P$ của mô hình. Khi $p_s=f_s/N$ lấy từ chính thông điệp, chúng đọc trực tiếp trên thông điệp: mọi mã tiền tố tốn ít nhất $I(x)$ bit, như $85{,}25$ bit cho A–E. Khi xác suất lấy từ dữ liệu khác, như một bảng mã dùng chung, các cận nói về bảng chứ không về tệp đang nén (Tình huống 10.3).

::: exercise Bài tập 10.3 (Trường hợp dấu bằng)
Cho $P=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ trên bốn ký hiệu (EE398A-1, trang chiếu 17). Tính $H(P)$, các độ dài Shannon, một mã tiền tố có các độ dài đó và $\bar\ell$ của nó. Kiểm điều kiện dấu bằng của Định lý 10.12. So với mã độ dài cố định 2 bit.
:::

::: hint
Mọi xác suất là lũy thừa của $\tfrac12$, nên $-\log_2p_s$ đã là số nguyên.
:::

::: solution
$H(P)=\tfrac12\cdot1+\tfrac14\cdot2+2\cdot\tfrac18\cdot3=0{,}5+0{,}5+0{,}75=1{,}75$ bit. Độ dài Shannon là $(1,2,3,3)$, với tổng Kraft $\tfrac12+\tfrac14+\tfrac18+\tfrac18=1$; Bước 2 của Định lý 10.9 cho mã `0`, `10`, `110`, `111`.

Độ dài trung bình là $\bar\ell=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=1{,}75=H(P)$. Điều kiện dấu bằng $p_s=2^{-\ell_s}$ đúng với cả bốn ký hiệu. Mã độ dài cố định dùng 2 bit mỗi ký hiệu, thừa $0{,}25$ bit so với entropy.
:::

Như vậy, chúng ta đã có điều kiện giải mã kiểm được trên từng cặp từ mã (Định nghĩa 10.5, Mệnh đề 10.6), tiêu chuẩn cho bộ độ dài thực hiện được (Định lý 10.9) và mức đích có cận hai phía cho mã tiền tố tối ưu (Định lý 10.12, 10.13). Tuy nhiên, hai định lý không chỉ ra cách tìm mã tiền tố tối ưu cho một bảng số đếm cho trước. Trong Mục 3, chúng ta dựng mã đó bằng thuật toán Huffman.

## 3. Mã Huffman tĩnh

Với thông điệp A–E, mã dựng từ độ dài Shannon tốn 102 bit, mã Huffman của Ví dụ 10.3 tốn 87 bit, còn mức đích là $I(x)\approx85{,}25$ bit. Chúng ta xét một phương pháp chia từ trên xuống có trước, chỉ ra nó dừng ở 89 bit, rồi xây thuật toán Huffman, chứng minh nó tối ưu và đếm chi phí của nó, kể cả đầu mục.

<!-- note-topic-id: lec-10-topic-08 -->
### 3.1 Shannon–Fano: chia từ trên xuống

Mã Shannon–Fano (Shannon–Fano coding) dựng cây từ gốc xuống: sắp các ký hiệu theo số đếm giảm dần, chia danh sách thành hai nhóm có tổng số đếm gần nhau nhất, gán bit 0 cho nhóm trên và bit 1 cho nhóm dưới, rồi lặp lại trên từng nhóm cho tới khi mỗi nhóm còn một ký hiệu (NG, tr.32).

::: example Ví dụ 10.7 (Shannon–Fano cho A–E)
**Dữ kiện.** A: 15, B: 7, C: 6, D: 6, E: 5, đã sắp giảm dần (NG, tr.32–33).

**Bốn lần chia.**

1. Chia giữa B và C: nhóm trên $15+7=22$, nhóm dưới $6+6+5=17$. Chia sau A cho $15$ và $24$, lệch hơn.
2. Nhóm $\{\mathrm A,\mathrm B\}$ chia giữa A và B.
3. Nhóm $\{\mathrm C,\mathrm D,\mathrm E\}$ chia giữa C và $\{\mathrm D,\mathrm E\}$, với tổng $6$ và $11$.
4. Nhóm $\{\mathrm D,\mathrm E\}$ chia giữa D và E.

**Kết quả.** Mã A = `00`, B = `01`, C = `10`, D = `110`, E = `111`, tốn
$$
(15+7+6)\cdot2+(6+5)\cdot3=56+33=89\ \text{bit}.
$$

**Kiểm tra lại.** Tổng Kraft $3\cdot\tfrac14+2\cdot\tfrac18=1$, và $85{,}25\le89$.
:::

Phương pháp này tạo mã tiền tố có độ dài gần $I(s)$ nhưng không bảo đảm tối ưu: mã Huffman 87 bit ngắn hơn 2 bit, vì đưa A lên độ sâu 1 tiết kiệm 15 bit trong khi đẩy B, C xuống độ sâu 3 chỉ tốn thêm 13 bit (NG, tr.37). Lần chia đầu chỉ cân bằng hai tổng và không nhìn tới cách các nhóm sẽ được chia tiếp.

<!-- note-topic-id: lec-10-topic-09 -->
### 3.2 Thuật toán Huffman

Shannon–Fano quyết định bit đầu của mọi từ mã trước và dừng ở 89 bit cho A–E. Cách dựng của Huffman tương tự ở chỗ cũng tạo một cây mã, nhưng khác ở chiều dựng: nó quyết định bit cuối của hai từ mã dài nhất trước, từ các lá lên gốc. Lý do là có một cây tối ưu trong đó hai ký hiệu ít gặp nhất là hai lá anh em sâu nhất (Bổ đề 10.16); ghép chúng thành một ký hiệu có số đếm bằng tổng, ta được bài toán cùng loại với một ký hiệu ít hơn. Để làm rõ, xem phép chạy tay sau với hàng đợi ưu tiên chứa các nút chưa có cha.

::: example Ví dụ 10.8 (Chạy tay Huffman cho A–E)
**Dữ kiện.** A: 15, B: 7, C: 6, D: 6, E: 5 (NG, tr.35–36). Hàng đợi ban đầu chứa năm lá; mỗi nút ghi tên và trọng số.

**Bốn lượt ghép.**

| Lượt | Hàng đợi trước | Lấy ra | Nút mới | Hàng đợi sau |
|---|---|---|---|---|
| 1 | A15, B7, C6, D6, E5 | E5, D6 | DE11 | A15, B7, C6, DE11 |
| 2 | A15, B7, C6, DE11 | C6, B7 | BC13 | A15, DE11, BC13 |
| 3 | A15, DE11, BC13 | DE11, BC13 | 24 | A15, 24 |
| 4 | A15, 24 | A15, 24 | gốc 39 | gốc 39 |

Ở lượt 1, C và D cùng trọng số 6. Quy tắc phá hòa ở đây chọn D; chọn C cho từ mã khác với cùng 87 bit (NG, tr.35). Sau lượt 1, ta đã biết bit cuối của D và E.

**Gán bit.** Gốc cho A bit 0 và nút 24 bit 1; nút 24 cho BC13 bit 0 và DE11 bit 1; BC13 cho B bit 0, C bit 1; DE11 cho D bit 0, E bit 1 (NG, tr.35–36). Đọc nhãn từ gốc xuống lá được A = `0`, B = `100`, C = `101`, D = `110`, E = `111`.

**Số bit.** $15\cdot1+(7+6+6+5)\cdot3=15+72=87$ bit.

**Kiểm tra lại.** Trọng số gốc $39=N$; tổng Kraft $\tfrac12+4\cdot\tfrac18=1$, đúng với cây đầy đủ theo Định lý 10.9(c).
:::

![Cây Huffman của A–E: gốc 39 có lá A 15 ở nhánh 0 và nút 24 ở nhánh 1; nút 24 có con 13 (B 7, C 6) và 11 (D 6, E 5); mỗi nút trong ghi lượt ghép 1 đến 4. Từ mã A 0, B 100, C 101, D 110, E 111.](img/lec-10/note-huffman-a-e.svg)

Trên hình, mỗi nút trong mang số lượt ghép đã tạo ra nó: hai lá nhẹ nhất D, E bị ghép ở lượt 1 và nằm sâu nhất, còn A, ký hiệu nặng nhất, chỉ được nối vào gốc ở lượt cuối. Thuật toán tổng quát chạy đúng các bước của bảng trên.

::: algorithm Thuật toán 10.14 (Huffman tĩnh)
**Đầu vào.** Bảng chữ cái $\Sigma$ với $k$ ký hiệu và số đếm $f_s$.

**Đầu ra.** Cây nhị phân đầy đủ $T$ có $k$ lá, mỗi lá là một ký hiệu; bảng mã $c$; dòng bit $c^*(x)$ khi mã hóa, hoặc thông điệp $x$ khi giải mã.

**Giả thiết.** $k\ge2$ và mọi $f_s\ge1$; một quy tắc phá hòa và một quy tắc gán bit cho hai con, cả hai cố định và chung cho hai phía.

**Các bước.**

1. Khởi tạo: tạo một lá cho mỗi $s\in\Sigma$ với trọng số $f_s$; đưa $k$ lá vào hàng đợi ưu tiên $\mathcal Q$ theo trọng số.
2. Lặp $k-1$ lượt: lấy ra khỏi $\mathcal Q$ hai nút $v_1$, $v_2$ có trọng số nhỏ nhất, phá hòa theo quy tắc chung; tạo nút cha $v$ có hai con $v_1$, $v_2$ với $\operatorname{wt}(v)=\operatorname{wt}(v_1)+\operatorname{wt}(v_2)$; gán bit 0, 1 cho hai cạnh theo quy tắc chung; chèn $v$ vào $\mathcal Q$.
3. Nút duy nhất còn lại trong $\mathcal Q$ là gốc của $T$.
4. Dựng bảng mã bằng một lần duyệt $T$ từ gốc: từ mã của lá $s$ là dãy bit trên đường từ gốc tới $s$.
5. Mã hóa: với $t=1,\ldots,n$, phát $c(x_t)$.
6. Giải mã: đi từ gốc theo từng bit, phát ký hiệu khi tới lá rồi quay về gốc (Mệnh đề 10.6(c)).

**Dừng.** Mỗi lượt giảm số nút trong $\mathcal Q$ đi 1, nên sau $k-1$ lượt $\mathcal Q$ còn đúng một nút. Giải mã dừng sau $n$ ký hiệu hoặc khi gặp `EOS`.

**Trường hợp biên.** Với $k=1$, vòng lặp không chạy và lá duy nhất có từ mã rỗng, trái Định nghĩa 10.1; giao thức luôn thêm `EOS` với số đếm 1 (NG, tr.52) nên bảng chữ cái có ít nhất hai ký hiệu khi tệp khác rỗng. Ký hiệu có $f_s=0$ không vào $\mathcal Q$ (NG, tr.54). Các bước vẫn chạy được khi có trọng số 0. Khi có hòa, mọi lựa chọn đều hợp lệ, nhưng hai phía phải chọn như nhau.

**Chi phí.** $k-1$ lượt, mỗi lượt hai phép lấy ra và một phép chèn: $O(k\log k)$ với đống nhị phân, $O(k^2)$ với phép quét mảng nút; dựng bảng mã $O(\sum_s\ell_s)$; mã hóa và giải mã tỷ lệ với số bit (Nhận xét 10.20).
:::

```text
HUFFMAN(Σ, f):
    𝒬 ← hàng đợi ưu tiên chứa lá s với khóa f[s], với mọi s ∈ Σ
    với r = 1, …, k − 1:
        v1 ← EXTRACT-MIN(𝒬);  v2 ← EXTRACT-MIN(𝒬)
        v  ← nút mới, hai con v1, v2, wt(v) = wt(v1) + wt(v2)
        gán bit 0, 1 cho hai con theo quy tắc chung
        INSERT(𝒬, v)
    trả về EXTRACT-MIN(𝒬)        ▷ gốc của T
```

Phép quyết định của thuật toán là chọn hai nút nhẹ nhất; mọi bước khác chỉ là ghi chép. Quy tắc phá hòa và quy tắc gán bit thuộc giao thức (Bài tập 10.1). Trên Ví dụ 10.8, hàng đợi ban đầu là bảng số đếm, bốn lượt là bốn lần lặp của vòng `với`, và nút trả về là gốc 39; Bài tập 10.11 dùng quy tắc "bit 0 cho nút lấy ra trước".

::: exercise Bài tập 10.4 (Huffman cho năm ký hiệu lệch)
Một thông điệp có số đếm E: 20, A: 20, X: 3, Y: 3, Z: 2 (NG, Chương 2, tr.23). Chạy Thuật toán 10.14, cho độ dài từ mã của từng ký hiệu và tổng số bit. Tính $I(x)$ với $p_s=f_s/48$ và so với số bit Huffman.
:::

::: hint
Lượt 1 ghép Z với một trong hai ký hiệu trọng số 3.
:::

::: solution
**Các lượt.** Với quy tắc phá hòa chọn X trước Y: Z2 và X3 thành 5; Y3 và 5 thành 8; 8 và một trong hai ký hiệu trọng số 20, chẳng hạn E, thành 28; A20 và 28 thành gốc 48.

**Độ dài và số bit.** A: 1, E: 2, Y: 3, X: 4, Z: 4, tổng
$$
20\cdot1+20\cdot2+3\cdot3+3\cdot4+2\cdot4=89\ \text{bit}.
$$

**Tự thông tin.** $I(\mathrm E)=I(\mathrm A)=\log_2(48/20)\approx1{,}263$, $I(\mathrm X)=I(\mathrm Y)=\log_216=4$, $I(\mathrm Z)=\log_224\approx4{,}585$ bit, nên
$$
\begin{aligned}
I(x)&\approx40\cdot1{,}263+6\cdot4+2\cdot4{,}585\\
&\approx83{,}69\ \text{bit}.
\end{aligned}
$$
Huffman thừa khoảng $5{,}3$ bit, tức khoảng 6%.
:::

<!-- note-topic-id: lec-10-topic-10 -->
### 3.3 Tính tối ưu

Thuật toán Huffman là tham lam: mỗi lượt chọn hai nút nhẹ nhất và không xét lại. Để chứng minh nó cho mã tiền tố tối ưu, chúng ta cần biết đổi chỗ hai lá làm chi phí thay đổi bao nhiêu.

::: example Ví dụ 10.9 (Đổi chỗ hai lá trên cây A–E)
**Dữ kiện.** Cây Huffman của Ví dụ 10.8: A ở độ sâu 1, B, C, D, E ở độ sâu 3; chi phí 87 bit.

**Tính.** Đổi chỗ A (15) với E (5): A xuống độ sâu 3, E lên độ sâu 1. Chi phí mới là
$$
15\cdot3+7\cdot3+6\cdot3+6\cdot3+5\cdot1=107\ \text{bit}.
$$

**Công thức đổi chỗ.** Đổi hai lá $s$, $s'$ có độ sâu $d_s$, $d_{s'}$ làm chi phí thay đổi
$$
\begin{aligned}
\Delta&=f_sd_{s'}+f_{s'}d_s-f_sd_s-f_{s'}d_{s'}\\
&=(f_s-f_{s'})(d_{s'}-d_s).
\end{aligned}
$$
Với A và E: $\Delta=(15-5)(3-1)=20$, khớp $107-87$.

**Diễn giải.** $\Delta\le0$ khi ký hiệu nặng hơn được đưa lên nông hơn (CMU, trang chiếu 31).

**Kiểm tra lại.** Với B và C cùng độ sâu 3, $\Delta=(7-6)(3-3)=0$.
:::

Một cách trực quan, đưa ký hiệu nhẹ xuống sâu không làm tăng chi phí, và co hai lá anh em thành một lá chỉ bớt một khoản cố định; ba bổ đề sau biến hai ý đó thành phép quy nạp. Cây mã của một mã tiền tố có lá đúng là các từ mã (Mệnh đề 10.6(a)), nên một mã tiền tố tương ứng với một cây có $k$ lá mang tên các ký hiệu. Vì $\operatorname{cost}(T)=N\bar\ell(c)$, cây tối ưu (Định nghĩa 10.11) cho đúng mã tiền tố tối ưu với $p_s=f_s/N$.

::: lemma Bổ đề 10.15 (Cây tối ưu là cây đầy đủ)
**Giả thiết.** Mọi $f_s\ge1$; $T$ là cây tối ưu.

**Kết luận.** Mọi nút trong của $T$ có đúng hai con.

**Điều kiện áp dụng.** Cần $f_s>0$; với một số đếm bằng 0, có thể có cây tối ưu không đầy đủ.

**Phạm vi.** Chỉ nói về cây tối ưu; một cây không tối ưu có thể có nút trong một con.
:::

::: proof
Giả sử nút trong $v$ chỉ có một con $v'$. Thay cây con gốc $v$ bằng cây con gốc $v'$, tức nối $v'$ vào chỗ của $v$. Mọi lá trong cây con của $v'$ giảm độ sâu đi 1, các lá khác giữ nguyên, và các lá vẫn là lá nên mã vẫn là mã tiền tố. Cây con của $v'$ chứa ít nhất một lá $s$, nên chi phí giảm ít nhất $f_s\ge1$, trái với tính tối ưu của $T$. $\square$
:::

Bỏ "$f_s\ge1$" thì kết luận sai: với a: 1, b: 1, c: 0, mã a = `0`, b = `10`, c = `110` có chi phí $1\cdot1+1\cdot2+0\cdot3=3$, nhưng nút `11` của cây mã chỉ có một con. Chi phí 3 là nhỏ nhất, vì theo Định lý 10.9(a), a và b không thể cùng có từ mã 1 bit khi còn từ mã thứ ba.

::: lemma Bổ đề 10.16 (Hai ký hiệu ít gặp nhất là anh em sâu nhất)
**Giả thiết.** $k\ge2$, mọi $f_s\ge1$. $s_1$ là một ký hiệu có số đếm nhỏ nhất, $s_2$ là một ký hiệu có số đếm nhỏ nhất trong $\Sigma\setminus\{s_1\}$.

**Kết luận.** Có một cây tối ưu trong đó $s_1$ và $s_2$ là hai lá anh em ở độ sâu lớn nhất của cây.

**Điều kiện áp dụng.** Đúng với mọi cách chọn $s_1$, $s_2$ khi có hòa, nên áp dụng được cho đúng hai ký hiệu mà Thuật toán 10.14 lấy ra ở lượt đầu.

**Phạm vi.** Bổ đề chỉ khẳng định sự tồn tại; không phải mọi cây tối ưu đều đặt $s_1$, $s_2$ làm anh em.
:::

::: proof
**Bước 1 (có cây tối ưu).** Chi phí của mọi cây là số nguyên dương, và có ít nhất một cây, chẳng hạn cây của mã độ dài cố định. Tập các chi phí có phần tử nhỏ nhất, nên có cây tối ưu $T$.

**Bước 2 (hai lá anh em sâu nhất).** Gọi $d$ là độ sâu lớn nhất của một lá trong $T$ và $\sigma$ là một lá ở độ sâu $d$. Vì $k\ge2$, $\sigma$ không là gốc; theo Bổ đề 10.15, cha của $\sigma$ có thêm một con $\sigma'$. Nút $\sigma'$ là lá, vì nếu là nút trong, nó sẽ có hậu duệ là lá ở độ sâu lớn hơn $d$.

**Bước 3 (đặt tên cho phép đổi).** Đặt tên hai lá $\sigma$, $\sigma'$ theo ba trường hợp:

- $s_1\in\{\sigma,\sigma'\}$: đặt tên sao cho $s_1=\sigma$;
- chỉ $s_2\in\{\sigma,\sigma'\}$: đặt tên sao cho $s_2=\sigma'$;
- không ký hiệu nào trong hai ký hiệu ở cặp đó: giữ nguyên tên.

Trong cả ba trường hợp, $s_2\ne\sigma$, và ký hiệu đang ở $\sigma'$ khác $s_1$ hoặc chính là $s_2$.

**Bước 4 (đổi $s_1$ với $\sigma$).** Nếu $s_1\ne\sigma$, đổi chỗ hai lá. Theo công thức của Ví dụ 10.9, chi phí thay đổi
$$
\Delta_1=(f_{s_1}-f_\sigma)(d-d_{s_1})\le0,
$$
vì $f_{s_1}\le f_\sigma$ theo cách chọn $s_1$, và $d\ge d_{s_1}$ theo cách chọn $d$. Phép đổi không di chuyển $s_2$ vì $s_2\ne\sigma$.

**Bước 5 (đổi $s_2$ với $\sigma'$).** Nếu $s_2$ chưa ở $\sigma'$, ký hiệu đang ở $\sigma'$ là một ký hiệu $s'\ne s_1$, nên $f_{s'}\ge f_{s_2}$ theo cách chọn $s_2$. Đổi chỗ $s_2$ với $s'$ thay đổi chi phí
$$
\Delta_2=(f_{s_2}-f_{s'})(d-d_{s_2})\le0 ,
$$
vì $d\ge d_{s_2}$ theo cách chọn $d$.

**Bước 6 (kết luận).** Cây sau hai phép đổi có chi phí không lớn hơn $\operatorname{cost}(T)$, nên cũng tối ưu, và có $s_1$, $s_2$ là hai lá anh em ở độ sâu $d$. $\square$
:::

::: lemma Bổ đề 10.17 (Co một cặp anh em)
**Giả thiết.** $T$ là cây mã trên $\Sigma$ trong đó $s_1$, $s_2$ là hai lá anh em với cha $v$. Gọi $s_{12}$ là một ký hiệu mới, $\Sigma'=(\Sigma\setminus\{s_1,s_2\})\cup\{s_{12}\}$ với $f_{s_{12}}=f_{s_1}+f_{s_2}$, và $T'$ là cây thu được từ $T$ khi bỏ hai lá $s_1$, $s_2$ và đặt tên $s_{12}$ cho $v$.

**Kết luận.**
$$
\operatorname{cost}(T)=\operatorname{cost}(T')+f_{s_1}+f_{s_2}.
$$
Ngược lại, từ mọi cây $T'$ trên $\Sigma'$, gắn hai con $s_1$, $s_2$ vào lá $s_{12}$ cho một cây $T$ trên $\Sigma$ thỏa cùng đẳng thức.

**Điều kiện áp dụng.** $s_1$, $s_2$ phải là anh em; không cần là hai ký hiệu ít gặp nhất.

**Phạm vi.** Đẳng thức đúng cho mọi cây, tối ưu hay không.
:::

::: proof
Gọi $d$ là độ sâu của $v$; hai lá $s_1$, $s_2$ có độ sâu $d+1$. Mọi lá khác có cùng độ sâu trong $T$ và $T'$. Do đó
$$
\begin{aligned}
&\operatorname{cost}(T)-\operatorname{cost}(T')\\
&\quad=(f_{s_1}+f_{s_2})(d+1)-(f_{s_1}+f_{s_2})d\\
&\quad=f_{s_1}+f_{s_2}.
\end{aligned}
$$
Phép gắn hai con vào $s_{12}$ là phép ngược của phép co, nên chiều ngược lại có cùng phép tính. $\square$
:::

::: theorem Định lý 10.18 (Huffman cho mã tiền tố tối ưu)
**Giả thiết.** $k\ge2$, mọi $f_s\ge1$; $T_{\mathrm H}$ là cây do Thuật toán 10.14 trả về, với một quy tắc phá hòa bất kỳ.

**Kết luận.** $\operatorname{cost}(T_{\mathrm H})\le\operatorname{cost}(T)$ với mọi cây mã $T$ của một mã tiền tố trên $\Sigma$; nói cách khác, mã Huffman là mã tiền tố tối ưu cho $p_s=f_s/N$.

**Điều kiện áp dụng.** Mỗi lượt ghép hai nút nhẹ nhất; mã là mã ký hiệu, tức mỗi ký hiệu một từ mã với số nguyên bit; xác suất là của mô hình đã cho.

**Phạm vi.** Định lý so sánh với mọi mã tiền tố, và theo Nhận xét 10.10 với mọi mã giải mã duy nhất; nó không so sánh với cách mã gộp nhiều ký hiệu hay mã cả chuỗi.
:::

::: proof
Quy nạp theo $k$.

**Bước 1 (cơ sở $k=2$).** Thuật toán ghép hai lá vào gốc, mỗi lá ở độ sâu 1, chi phí $f_{s_1}+f_{s_2}=N$. Mọi mã tiền tố có mọi $\ell_s\ge1$, nên mọi cây có chi phí ít nhất $N$.

**Bước 2 (lượt đầu và bài toán nhỏ hơn).** Với $k\ge3$, gọi $s_1$, $s_2$ là hai nút Thuật toán 10.14 lấy ra ở lượt đầu, theo thứ tự lấy ra. Khi đó $s_1$ có số đếm nhỏ nhất và $s_2$ có số đếm nhỏ nhất trong phần còn lại. Từ lượt thứ hai, thuật toán chạy đúng như khi nhận đầu vào $\Sigma'$ với ký hiệu $s_{12}$ có số đếm $f_{s_1}+f_{s_2}$ của Bổ đề 10.17, với quy tắc phá hòa cảm sinh từ quy tắc ban đầu. Gọi $T'_{\mathrm H}$ là cây mà các lượt 2 đến $k-1$ tạo ra; đó là một lần chạy của thuật toán trên $\Sigma'$; $T_{\mathrm H}$ thu được từ $T'_{\mathrm H}$ khi gắn $s_1$, $s_2$ vào lá $s_{12}$.

**Bước 3 (giả thiết quy nạp).** $\Sigma'$ có $k-1\ge2$ ký hiệu với mọi số đếm dương, nên theo giả thiết quy nạp, áp dụng cho mọi quy tắc phá hòa, $T'_{\mathrm H}$ tối ưu trên $\Sigma'$.

**Bước 4 (so sánh với một cây tối ưu).** Theo Bổ đề 10.16, có cây tối ưu $T^*$ trên $\Sigma$ trong đó $s_1$, $s_2$ là anh em. Co cặp đó được cây $T^{*\prime}$ trên $\Sigma'$. Áp dụng Bổ đề 10.17 hai lần,
$$
\begin{aligned}
&\operatorname{cost}(T^*)\\
&\quad=\operatorname{cost}(T^{*\prime})+f_{s_1}+f_{s_2}\\
&\quad\ge\operatorname{cost}(T'_{\mathrm H})+f_{s_1}+f_{s_2}\\
&\quad=\operatorname{cost}(T_{\mathrm H}).
\end{aligned}
$$
Bất đẳng thức dùng Bước 3. Vì $T^*$ tối ưu, $T_{\mathrm H}$ cũng tối ưu. $\square$
:::

Phép chọn "hai nút nhẹ nhất" được dùng đúng một lần, ở Bước 2: nó cho phép áp dụng Bổ đề 10.16 cho đúng cặp $s_1$, $s_2$ mà thuật toán đã ghép. Kết quả không phụ thuộc quy tắc phá hòa, nên mọi cách phá hòa cho cùng chi phí tối ưu (NG, tr.35); tuy vậy, các cây khác nhau cho từ mã khác nhau, nên giao thức vẫn phải cố định quy tắc (Bài tập 10.1).

Mỗi giả thiết của Định lý 10.18 đều cần:

- Bỏ "ghép hai nút nhẹ nhất": cây Shannon–Fano của Ví dụ 10.7 cũng là một cây đầy đủ dựng theo quy tắc khác, và tốn 89 bit so với 87 bit.
- Bỏ "mã ký hiệu nguyên bit": khi được mã cả chuỗi, có thể dùng ít hơn 1 bit mỗi ký hiệu; với hai ký hiệu xác suất $0{,}9$ và $0{,}1$, mọi mã ký hiệu dùng ít nhất 1 bit mỗi ký hiệu, trong khi $H\approx0{,}47$ bit. Mã Huffman trên các khối $j$ ký hiệu đạt $H\le\bar\ell/j<H+1/j$ bit mỗi ký hiệu, nhưng bảng chữ cái của nó có $k^j$ phần tử (EE398A-1, trang chiếu 21; NG, tr.96).
- Bỏ "xác suất của mô hình đã cho": nếu số đếm truyền cho bộ mã khác số đếm thật của thông điệp, cây tối ưu cho số đếm truyền đi, không cho thông điệp (Tình huống 10.3).

Ghép Định lý 10.18 với hai cận của Mục 2 cho vị trí chính xác của mã Huffman so với entropy.

::: corollary Hệ quả 10.19 (Cận entropy của mã Huffman)
**Giả thiết.** Như Định lý 10.18, với $p_s=f_s/N$; $c_{\mathrm H}$ là mã Huffman.

**Kết luận.** $H(P)\le\bar\ell(c_{\mathrm H})<H(P)+1$; nhân với $N$, $I(x)\le\operatorname{cost}(T_{\mathrm H})<I(x)+N$.

**Điều kiện áp dụng.** Như Định lý 10.18.

**Phạm vi.** Khi $H(P)$ nhỏ so với 1, phần thừa tới gần 1 bit mỗi ký hiệu có thể lớn hơn chính $H(P)$, như ở nguồn nhị phân lệch.
:::

::: proof
Cận dưới là Định lý 10.12 áp dụng cho mã tiền tố $c_{\mathrm H}$. Theo Định lý 10.13, có mã tiền tố $c$ với $\bar\ell(c)<H(P)+1$; theo Định lý 10.18, $\bar\ell(c_{\mathrm H})\le\bar\ell(c)$. $\square$
:::

::: example Ví dụ 10.10 (Đọc Hệ quả 10.19 trên A–E)
**Dữ kiện.** $H(P)\approx2{,}186$ bit (Ví dụ 10.5); mã Huffman tốn 87 bit cho $N=39$ ký hiệu (Ví dụ 10.8).

**Tính.** $\bar\ell(c_{\mathrm H})=87/39\approx2{,}231$, và
$$
2{,}186\le2{,}231<3{,}186 .
$$

**Diễn giải.** Mã Huffman thừa khoảng $0{,}045$ bit mỗi ký hiệu so với entropy, tức $87-85{,}25\approx1{,}75$ bit trên cả thông điệp; Hệ quả 10.19 cho phép thừa tới gần 39 bit.

**Kiểm tra lại.** $39\cdot2{,}186\approx85{,}25$ và $39\cdot2{,}231\approx87$.
:::

Khi xác suất lớn nhất tiến gần 1, $H(P)$ tiến về 0 nhưng mã Huffman vẫn dùng ít nhất 1 bit mỗi ký hiệu; giới hạn này là điểm xuất phát của mã số học.

<!-- note-topic-id: lec-10-topic-11 -->
### 3.4 Chi phí và đầu mục

Bộ nén tĩnh đọc dữ liệu hai lần và phải gửi đủ thông tin để bên nhận dựng lại đúng cây; hai khoản này nằm ngoài Định lý 10.18, vốn chỉ đo phần thân $\operatorname{cost}(T)$. Mô hình chi phí đếm phép so sánh và phép ghi của hàng đợi ưu tiên cài bằng đống nhị phân, trong trường hợp xấu nhất.

::: remark Nhận xét 10.20 (Chi phí của Huffman tĩnh và đầu mục)
| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| đếm số đếm (lượt đọc thứ nhất) | $n$ | $O(1)$ | $O(n)$ |
| đưa $k$ lá vào $\mathcal Q$ | $k$ | $O(\log k)$ | $O(k\log k)$ |
| ghép (hai lần lấy ra, một lần chèn) | $k-1$ | $O(\log k)$ | $O(k\log k)$ |
| dựng bảng mã (duyệt cây) | $2k-1$ nút | $O(1)$ cộng độ dài từ mã ghi ra | $O(\sum_s\ell_s)$ |
| mã hóa (lượt đọc thứ hai) | $n$ | $O(\ell_{x_t})$ | $O(\operatorname{cost}(T))$ |
| giải mã | $\operatorname{cost}(T)$ bit | $O(1)$ | $O(\operatorname{cost}(T))$ |

Tổng thời gian là $O(n+k\log k+\operatorname{cost}(T))$, trong đó $\operatorname{cost}(T)\le n\,\ell_{\max}$, và $\operatorname{cost}(T)<I(x)+n$ khi cây dựng từ số đếm thật (Hệ quả 10.19); bộ nhớ là $k$ số đếm và $2k-1$ nút. Cài đặt bằng phép quét mảng nút thay cho đống tốn $O(k)$ mỗi lượt và $O(k^2)$ cho cả cây (NG, tr.54, 62); với $k=257$ ký hiệu, số nút không quá $2\cdot257-1=513$.

Đầu mục (header, còn gọi là thông tin phụ, side information) của bộ nén tĩnh được tổ chức như sau (NG, tr.52–54):

- bảng chữ cái có 257 ký hiệu: 256 giá trị byte và `EOS`;
- số đếm được co để vừa một byte, nên khi dựng cây mọi phép tính vừa số nguyên 16 bit; phép co không bảo đảm từ mã dài không quá 16 bit, vì gốc có thể tới $256\cdot254+1=65\,025$, vượt xa $4\,181$, ngưỡng mà dưới nó cận Fibonacci loại từ mã 17 bit (Nhận xét 10.28);
- bên nén gửi bảng số đếm đã co, 256 byte, thay cho mảng nút 4K byte của cây, vì bên nhận chạy Thuật toán 10.14 trên cùng số đếm dựng lại đúng cây;
- số đếm 0 được bỏ bằng cách gửi từng dải ký hiệu liên tiếp: ký hiệu đầu, ký hiệu cuối, các số đếm trong dải, và một số 0 ở cuối; đầu mục bậc 0 thêm khoảng 250 byte mỗi tệp (NG, tr.67);
- với mô hình bậc 1, mỗi ký hiệu đứng trước có một bảng riêng, tổng 257 bảng (NG, tr.67), và bảng số đếm tới khoảng $65\,536$ byte (NG, tr.24).
:::

**Trong thực hành.** Vì số đếm bị co, Định lý 10.18 bảo đảm tối ưu cho số đếm đã co chứ không cho số đếm thật. Hai lượt đọc đòi hỏi đầu vào đọc lại được từ đầu: chương trình đếm tới cuối tệp rồi quay lại đầu để mã hóa (NG, tr.52), nên cách này không dùng được cho dòng chỉ đọc một lần. Bộ nén bậc 0 này nhỏ, ít tốn bộ nhớ và nhanh (NG, tr.66).

Như vậy, chúng ta đã có thuật toán Huffman (Thuật toán 10.14), chứng minh nó cho mã tiền tố tối ưu (Định lý 10.18) nằm trong khoảng $[H;\,H+1)$ bit mỗi ký hiệu (Hệ quả 10.19), và đếm chi phí của nó (Nhận xét 10.20). Tuy nhiên, bộ nén tĩnh cần lượt đếm trước và một đầu mục tăng nhanh theo bậc của mô hình. Trong Mục 4, chúng ta bỏ cả hai bằng cách để hai phía cùng cập nhật cây sau mỗi ký hiệu.

## 4. Mã Huffman thích nghi

Mô hình thích nghi của Định nghĩa 10.3 bỏ lượt đếm và đầu mục: hai phía bắt đầu từ cùng một cây và cùng cập nhật cây sau mỗi ký hiệu, nên bộ nén là một thuật toán dòng một lượt theo Định nghĩa 08.1 với trạng thái là cây. Chạy lại Thuật toán 10.14 sau mỗi ký hiệu tốn $O(k\log k)$ mỗi ký hiệu (NG, tr.68). Chúng ta cần một phép cập nhật cục bộ trên đường từ lá tới gốc mà vẫn giữ cây là cây Huffman của các trọng số hiện thời (NG, Chương 4).

<!-- note-topic-id: lec-10-topic-12 -->
### 4.1 Tính chất anh em

Để cập nhật cục bộ, chúng ta cần một đặc trưng của cây Huffman kiểm được trên chính cây, không cần chạy lại thuật toán. Chúng ta liệt kê các nút của một cây Huffman theo trọng số.

::: example Ví dụ 10.11 (Danh sách nút của một cây Huffman)
**Dữ kiện.** Năm ký hiệu với trọng số A: 1, B: 2, C: 2, D: 2, E: 10 (NG, tr.68). Thuật toán 10.14 ghép A với B thành 3, C với D thành 4, hai nút đó thành 7, rồi 7 với E thành gốc 17.

**Danh sách theo trọng số không giảm.** Đánh vị trí $\#1$ đến $\#9$:

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ | $\#8$ | $\#9$ |
|---|---|---|---|---|---|---|---|---|---|
| Nút | A | B | C | D | (A, B) | (C, D) | ($\#5$, $\#6$) | E | gốc |
| Trọng số | 1 | 2 | 2 | 2 | 3 | 4 | 7 | 10 | 17 |

**Quan sát.** Bốn cặp vị trí $(\#1,\#2)$, $(\#3,\#4)$, $(\#5,\#6)$, $(\#7,\#8)$ đều là cặp anh em, và gốc đứng cuối.

**Kiểm tra lại.** Mỗi nút trong bằng tổng hai con: $1+2=3$, $2+2=4$, $3+4=7$, $7+10=17$.
:::

Danh sách trên đúng là thứ tự các nút bị lấy ra khỏi hàng đợi khi chạy Thuật toán 10.14: lượt 1 lấy A, B; lượt 2 lấy C, D; lượt 3 lấy hai nút 3 và 4; lượt 4 lấy 7 và E. Chúng ta đặt tên cho tính chất của danh sách này.

::: definition Định nghĩa 10.21 (Cây có trọng số, tính chất anh em và cây Huffman)
- Một **cây có trọng số** (weighted tree) là cây nhị phân đầy đủ có $k'\ge2$ lá, mỗi lá mang một ký hiệu và một trọng số nguyên không âm, và mỗi nút trong có trọng số bằng tổng trọng số của hai con. Cây có $2k'-1$ nút.
- Cây có trọng số có **tính chất anh em** (sibling property) khi các nút xếp được thành danh sách $v_1,v_2,\ldots,v_{2k'-1}$ sao cho
$$
\operatorname{wt}(v_1)\le\cdots\le\operatorname{wt}(v_{2k'-1}),
$$
và với mỗi $j=1,\ldots,k'-1$, hai nút $v_{2j-1}$, $v_{2j}$ là anh em. Khi đó $v_{2k'-1}$ là gốc, vì mọi nút khác đã có anh em trong một cặp; vị trí của $v_i$ được viết là $\#i$.
- Một **cây Huffman** cho một bộ trọng số lá nguyên không âm là cây mà các bước 1–3 của Thuật toán 10.14, chạy trên các trọng số đó, có thể trả về với một quy tắc phá hòa nào đó.
:::

Một phản ví dụ là cây có lá A: 1, B: 1, C: 3, D: 3, trong đó A, B là anh em dưới nút trọng số 2, C, D là anh em dưới nút trọng số 6, và gốc trọng số 8 (NG, Hình 4.8). Trong mọi danh sách không giảm, nút trọng số 2 phải đứng sau A, B và trước C, D, tức ở $\#3$, kề với một lá trọng số 3 không phải anh em của nó. Cây không có tính chất anh em, và nó cũng không là cây Huffman: Thuật toán 10.14 ghép nút trọng số 2 với một lá trọng số 3 ở lượt thứ hai.

Một cách trực quan, danh sách của tính chất anh em ghi lại thứ tự ghép của thuật toán Huffman: hai nút đầu danh sách là hai nút nhẹ nhất, và chúng là anh em. Giữ được danh sách thì giữ được một lần chạy của Thuật toán 10.14 trên các trọng số hiện thời.

::: theorem Định lý 10.22 (Tính chất anh em đặc trưng cây Huffman)
**Giả thiết.** $T$ là cây có trọng số với $k'\ge2$ lá, mọi lá có trọng số nguyên không âm; chiều ngược thêm giả thiết mọi lá có trọng số ít nhất 1.

**Kết luận.** $T$ là cây Huffman cho các trọng số lá của nó khi và chỉ khi $T$ có tính chất anh em.

**Điều kiện áp dụng.** Chiều "cây Huffman thì có tính chất anh em" dùng được khi có lá trọng số 0, như ở Thuật toán 10.29; chiều ngược kiểm mọi lá có trọng số dương.

**Phạm vi.** Kết hợp với Định lý 10.18, mọi cây có trọng số có tính chất anh em và mọi lá trọng số ít nhất 1 cho một mã tiền tố tối ưu với các trọng số lá làm số đếm.
:::

::: proof
**Bước 1 (chiều thuận: dựng danh sách).** Giả sử Thuật toán 10.14 trả về $T$. Ở lượt $r=1,\ldots,k'-1$, nó lấy ra hai nút $\mu_r$, $\nu_r$ theo thứ tự đó và tạo cha $\pi_r$. Mỗi nút khác gốc được đưa vào hàng đợi đúng một lần, lá lúc khởi tạo và nút trong lúc được tạo, và được lấy ra đúng một lần. Do đó danh sách
$$
\mu_1,\nu_1,\ldots,\mu_{k'-1},\nu_{k'-1},\text{gốc}
$$
chứa mỗi nút đúng một lần, và mỗi cặp $\mu_r$, $\nu_r$ là anh em.

**Bước 2 (chiều thuận: trọng số không giảm).** Trong một lượt, $\operatorname{wt}(\mu_r)\le\operatorname{wt}(\nu_r)$ vì $\mu_r$ được lấy ra trước. Giữa hai lượt, mọi nút còn lại trong hàng đợi sau khi lấy $\mu_r$, $\nu_r$ có trọng số ít nhất $\operatorname{wt}(\nu_r)$, vì $\nu_r$ nhỏ nhất trong số đó; nút mới có
$$
\begin{aligned}
\operatorname{wt}(\pi_r)&=\operatorname{wt}(\mu_r)+\operatorname{wt}(\nu_r)\\
&\ge\operatorname{wt}(\nu_r),
\end{aligned}
$$
vì trọng số không âm. Vậy mọi nút trong hàng đợi ở lượt $r+1$ có trọng số ít nhất $\operatorname{wt}(\nu_r)$, nên $\operatorname{wt}(\mu_{r+1})\ge\operatorname{wt}(\nu_r)$; cùng lập luận cho gốc sau lượt cuối. Danh sách có trọng số không giảm, nên $T$ có tính chất anh em.

**Bước 3 (chiều ngược: con đứng trước cha).** Giả sử $T$ có tính chất anh em với danh sách $v_1,\ldots,v_{2k'-1}$ và mọi lá có trọng số ít nhất 1. Khi đó mọi nút có trọng số ít nhất 1, nên mỗi nút trong có trọng số lớn hơn hẳn trọng số của từng con. Vì danh sách không giảm, mỗi con đứng trước cha của nó.

**Bước 4 (chiều ngược: quy nạp theo $k'$).** Với $k'=2$, cây có hai lá dưới gốc và đó là cây duy nhất thuật toán trả về. Với $k'\ge3$, xét $v_1$, $v_2$. Nếu $v_1$ là nút trong, hai con của nó phải đứng trước $v_1$ theo Bước 3, điều không thể. Nếu $v_2$ là nút trong, hai con của nó phải đứng ở các vị trí nhỏ hơn 2, cũng không thể. Vậy $v_1$, $v_2$ là hai lá anh em, có trọng số nhỏ nhất trong mọi nút, nên nhỏ nhất trong mọi lá. Lượt đầu của thuật toán, với quy tắc phá hòa chọn $v_1$ rồi $v_2$, lấy ra đúng hai lá này và tạo đúng cha $\pi$ của chúng.

**Bước 5 (chiều ngược: cây nhỏ hơn).** Bỏ $v_1$, $v_2$ khỏi $T$ và coi $\pi$ là một lá có trọng số $\operatorname{wt}(v_1)+\operatorname{wt}(v_2)\ge2$. Cây $T'$ nhận được có $k'-1\ge2$ lá, vẫn là cây có trọng số, và danh sách $v_3,\ldots,v_{2k'-1}$ vẫn không giảm với các cặp anh em ở vị trí $(\#3,\#4),(\#5,\#6),\ldots$. Theo giả thiết quy nạp, có một lần chạy thuật toán trên các lá của $T'$ trả về $T'$. Hàng đợi của thuật toán trên $T$ sau lượt đầu gồm đúng các lá của $T'$, nên tiếp tục bằng lần chạy đó cho $T$. $\square$
:::

Bỏ một điều kiện của tính chất anh em thì cây có thể không là cây Huffman:

- Bỏ "danh sách không giảm": cây A1, B1, C3, D3 vừa xét có các cặp anh em xếp cạnh nhau được, nhưng không theo trọng số không giảm, và không là cây Huffman.
- Bỏ "anh em đứng cạnh nhau": cây có gốc với hai con là lá A1 và một nút trọng số 6, nút đó có hai con là lá B2 và một nút trọng số 4 với hai lá C2, D2, cho danh sách trọng số $1,2,2,2,4,6,7$ không giảm, nhưng A và B ở $\#1$, $\#2$ không là anh em; chi phí của nó là $1\cdot1+2\cdot2+2\cdot3+2\cdot3=17$, còn cây Huffman cho bốn trọng số này có chi phí $2\cdot(1+2+2+2)=14$.

Bước 2 dùng trọng số không âm; Bước 3 và Bước 4 dùng trọng số dương để loại trường hợp một nút trong đứng trước con của nó.

**Trong thực hành.** Cài đặt không chạy lại Thuật toán 10.14 mà giữ các nút trong một mảng sắp theo trọng số giảm dần từ gốc, hai con của một nút ở hai chỉ số liền nhau, nên mảng chính là danh sách của Định nghĩa 10.21 viết ngược và mỗi nút chỉ cần một con trỏ tới con đầu (NG, tr.78–81); giữ mảng đúng thứ tự là giữ được cây Huffman.

Trên cây có tính chất anh em, cài đặt gán bit cho hai con theo vị trí: trong mỗi cặp $(\#(2j-1),\#2j)$, nút ở vị trí lẻ nhận bit 1, nút ở vị trí chẵn nhận bit 0 (NG, mã nguồn, tr.81, 92). Với cây của Ví dụ 10.11, quy ước cho E = `0`, D = `100`, C = `101`, B = `110`, A = `111`.

![Cây của Ví dụ 10.11 với vị trí và trọng số: gốc #9 (17), E #8 (10), #7 (7), #6 (4), #5 (3), D #4, C #3, B #2 cùng trọng số 2, A #1 (1). Phía dưới là danh sách #1 đến #9 với trọng số 1, 2, 2, 2, 3, 4, 7, 10, 17 và ngoặc nối các cặp anh em #1–#2, #3–#4, #5–#6, #7–#8.](img/lec-10/note-tinh-chat-anh-em.svg)

Trên hình, mỗi ngoặc dưới danh sách nối hai nút anh em đứng cạnh nhau, và dãy trọng số đọc từ trái sang phải không giảm; đó là hai điều kiện của Định nghĩa 10.21.

<!-- note-topic-id: lec-10-topic-13 -->
### 4.2 Tăng trọng số và đổi nút

Khi bộ nén đọc thêm một A, số đếm của A tăng 1, nên trọng số của lá A và của mọi tổ tiên của nó tăng 1. Phép tăng đó đôi khi giữ, đôi khi phá tính chất anh em. Ví dụ sau sửa lại bằng một phép đổi nút (NG, tr.68–71).

::: example Ví dụ 10.12 (Tăng A từ 1 lên 3)
**Dữ kiện.** Cây của Ví dụ 10.11, danh sách A1, B2, C2, D2, $(\mathrm A,\mathrm B)3$, $(\mathrm C,\mathrm D)4$, $\#7$: 7, E10, gốc 17 (NG, tr.68–71).

**Lần tăng thứ nhất, A từ 1 lên 2.** Tăng lá A ở $\#1$, rồi $\#5$, $\#7$, gốc $\#9$:

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ | $\#8$ | $\#9$ |
|---|---|---|---|---|---|---|---|---|---|
| Nút | A | B | C | D | (A, B) | (C, D) | ($\#5$, $\#6$) | E | gốc |
| Trọng số | 2 | 2 | 2 | 2 | 4 | 4 | 8 | 10 | 18 |

Danh sách vẫn không giảm; không cần đổi nút (NG, Hình 4.2).

**Lần tăng thứ hai, A từ 2 lên 3.** Nếu chỉ tăng A thành 3 tại $\#1$, A đứng trước B, C, D trọng số 2 và danh sách mất tính không giảm. Ta đổi A với nút cuối cùng trong danh sách có cùng trọng số cũ 2, là D ở $\#4$, rồi mới tăng (NG, tr.70):

1. Đổi A và D: A sang $\#4$ làm con của $\#6$, D sang $\#1$ làm con của $\#5$. Hai cây con cùng trọng số 2 nên trọng số của $\#5$ và $\#6$ không đổi.
2. Tăng A tại $\#4$ thành 3. Lúc này $\#6$ vẫn có trọng số 4 dù hai con là C2 và A3.
3. Tiếp tục từ cha mới của A là $\#6$: các nút trọng số 4 là $\#5$, $\#6$, nút cuối là chính $\#6$, nên không đổi; tăng thành 5.
4. Nút $\#7$ trọng số 8 là nút cuối của khối trọng số 8; tăng thành 9. Gốc tăng thành 19.

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ | $\#8$ | $\#9$ |
|---|---|---|---|---|---|---|---|---|---|
| Nút | D | B | C | A | (D, B) | (C, A) | ($\#5$, $\#6$) | E | gốc |
| Trọng số | 2 | 2 | 2 | 3 | 4 | 5 | 9 | 10 | 19 |

**Kiểm tra lại.** Danh sách không giảm, bốn cặp vẫn là anh em, mỗi nút trong bằng tổng hai con. A và D vẫn có từ mã 3 bit (NG, tr.71).
:::

Nút được chọn để đổi là nút cuối cùng của *khối* trọng số $q$, tức đoạn liên tiếp các vị trí có trọng số $q$ trong danh sách. Một cách trực quan, đưa nút đang tăng tới cuối khối rồi mới tăng làm nó đứng đúng chỗ: các nút trước nó nặng không quá $q$, các nút sau nặng ít nhất $q+1$; hai nút đổi có cùng trọng số nên không cha nào bị sai tổng. Trong ví dụ sau, nút cuối khối có lúc là một nút trong.

::: example Ví dụ 10.13 (Tăng A từ 3 lên 5)
**Dữ kiện.** Danh sách cuối của Ví dụ 10.12: D2, B2, C2, A3, $(\mathrm D,\mathrm B)4$, $(\mathrm C,\mathrm A)5$, $\#7$: 9, E10, gốc 19.

**Lần tăng thứ ba, A từ 3 lên 4.** A ở $\#4$ là nút duy nhất trọng số 3, không đổi; tăng A, $\#6$, $\#7$, gốc thành 4, 6, 10, 20. Danh sách mới là D2, B2, C2, A4, $(\mathrm D,\mathrm B)4$, $(\mathrm C,\mathrm A)6$, $\#7$: 10, E10, gốc 20.

**Lần tăng thứ tư, A từ 4 lên 5.**

1. Khối trọng số 4 gồm A ở $\#4$ và nút trong $(\mathrm D,\mathrm B)$ ở $\#5$. Đổi A với nút $\#5$: A sang $\#5$ làm con của $\#7$, cây con $(\mathrm D,\mathrm B)$ sang $\#4$ làm con của $\#6$. Tăng A thành 5.
2. Cha mới của A là $\#7$, trọng số 10. Khối trọng số 10 gồm $\#7$ và E ở $\#8$; đổi $\#7$ với E. Hai nút đều là con của gốc, nên hình dạng cây không đổi, chỉ hai vị trí đổi chỗ. Tăng nút trong vừa chuyển sang $\#8$ thành 11.
3. Tăng gốc thành 21.

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ | $\#8$ | $\#9$ |
|---|---|---|---|---|---|---|---|---|---|
| Nút | D | B | C | (D, B) | A | (C, $\#4$) | E | (A, $\#6$) | gốc |
| Trọng số | 2 | 2 | 2 | 4 | 5 | 6 | 10 | 11 | 21 |

**Độ dài từ mã.** E: 1 bit, A: 2 bit, C: 3 bit, B và D: 4 bit (NG, tr.71).

**Kiểm tra lại.** Tổng Kraft $\tfrac12+\tfrac14+\tfrac18+2\cdot\tfrac1{16}=1$, đúng với cây đầy đủ.
:::

![Hai cây. Cây trên, sau lần tăng thứ hai, có danh sách 2, 2, 2, 3, 4, 5, 9, 10, 19 và mũi tên nét đứt "đổi A với D". Cây dưới, sau lần tăng thứ tư, có danh sách 2, 2, 2, 4, 5, 6, 10, 11, 21, ghi chú "đổi A với #5, rồi đổi #7 với E", và độ dài A 2 bit, C 3 bit, B và D 4 bit, E 1 bit.](img/lec-10/note-tang-doi-a.svg)

Ở cây dưới của hình, A đã lên độ sâu 2 và cây con $(\mathrm D,\mathrm B)$ xuống độ sâu 3: chỉ phép đổi làm thay đổi hình dạng cây.

::: algorithm Thuật toán 10.23 (Tăng trọng số và đổi nút)
**Đầu vào.** Cây có trọng số có tính chất anh em, cùng danh sách vị trí; ký hiệu $s$ có lá trong cây.

**Đầu ra.** Cùng cây sau khi trọng số của $s$ tăng 1, với các phép đổi cần thiết, vẫn có tính chất anh em.

**Giả thiết.** Mỗi nút khác gốc đứng trước cha của nó trong danh sách; mọi lá có trọng số ít nhất 1, trừ có thể lá của $s$ vừa được thêm với trọng số 0.

**Các bước.**

1. Nếu trọng số gốc bằng $W_{\max}$, dựng lại cây bằng Thuật toán 10.29.
2. Khởi tạo: đặt $v$ là lá của $s$.
3. Lặp cho tới khi $v$ là gốc: gọi $q=\operatorname{wt}(v)$ và $\hat v$ là nút ở vị trí lớn nhất có trọng số $q$; nếu $\hat v\ne v$, đổi chỗ hai cây con gốc $v$ và $\hat v$, tức hai nút đổi vị trí và mỗi nút nhận cha của vị trí mới; tăng $\operatorname{wt}(v)$ thêm 1; đặt $v$ là cha hiện tại của $v$.
4. Tăng trọng số gốc thêm 1.

**Dừng.** Vị trí của $v$ tăng ngặt sau mỗi lượt, vì cha đứng sau vị trí mới của $v$ (giả thiết, giữ bởi Định lý 10.25); cây có $k'$ lá có $2k'-1$ vị trí, nên sau nhiều nhất $2k'-2$ lượt $v$ là gốc.

**Trường hợp biên.** Gốc không bao giờ bị đổi. Nút cuối khối có thể là chính $v$ (không đổi), một lá, hoặc một nút trong như ở Ví dụ 10.13.

**Chi phí.** Với $h$ là số lượt của bước 3 và cây có $k'$ lá, mô hình đếm phép so sánh và phép ghi trên mảng nút trong trường hợp xấu nhất:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| tăng trọng số | $h+1$ | $O(1)$ | $O(h)$ |
| quét lùi tìm nút cuối khối (NG, tr.83) | $h$ | $O(2k'-1)$ | $O(hk')$ |
| đổi hai phần tử mảng, sửa con trỏ cha (NG, tr.84) | $\le h$ | $O(1)$ | $O(h)$ |

Số lượt $h$ là số nút trên đường đi thực tế, có thể khác độ sâu ban đầu của lá vì đường đi tiếp từ cha mới. Số phép tăng trung bình tương ứng với độ dài trung bình của từ mã (NG, tr.69).
:::

```text
UPDATE(T, s):
    nếu wt(gốc) = Wmax: REBUILD(T)
    v ← lá(s)
    trong khi v ≠ gốc:
        v̂ ← nút ở vị trí lớn nhất có wt(v̂) = wt(v)
        nếu v̂ ≠ v: SWAP(v, v̂)          ▷ v sang vị trí của v̂
        wt(v) ← wt(v) + 1
        v ← cha(v)
    wt(gốc) ← wt(gốc) + 1
```

Phép quyết định là tìm nút cuối khối của trọng số cũ (NG, tr.83–84); thuật toán không để ngỏ lựa chọn nào.

**Câu hỏi.** Nút cuối khối $\hat v$ có thể là tổ tiên của $v$ không? Nếu có, phép đổi vô nghĩa vì cây con gốc $\hat v$ chứa $v$. Bổ đề 10.24 chứng minh điều đó không xảy ra.

::: lemma Bổ đề 10.24 (Nút cuối khối không là tổ tiên)
**Giả thiết.** Đang ở một lượt của bước 3 trong Thuật toán 10.23, với nút $v\ne$ gốc có trọng số $q$; mọi nút khác $v$ đều có trọng số bằng tổng hai con nếu là nút trong; mọi lá có trọng số ít nhất 1, trừ $v$ khi $v$ là lá mới trọng số 0; mỗi nút khác gốc đứng trước cha của nó trong danh sách.

**Kết luận.** Nút $\hat v$ ở vị trí lớn nhất có trọng số $q$ không là tổ tiên, cũng không là hậu duệ thực sự của $v$.

**Điều kiện áp dụng.** Giả thiết về trọng số dương đúng trong mọi trạng thái Thuật toán 10.26 tạo ra: `ESCAPE` và `EOS` có trọng số 1 và không bao giờ được tăng, lá mới chỉ có trọng số 0 trong lần cập nhật ngay sau khi được thêm, và phép co $\lfloor(\omega+1)/2\rfloor$ không đưa lá có trọng số dương về 0.

**Phạm vi.** Bổ đề cần mọi lá khác $v$ có trọng số dương: nếu anh em của $v$ có trọng số 0, cha của $v$ cũng có trọng số $q$ và có thể là nút cuối khối.
:::

::: proof
**Bước 1 (anh em của $v$ có trọng số dương).** Cây con gốc tại anh em $\sigma$ của $v$ không chứa $v$, nên mọi lá của nó có trọng số ít nhất 1 và mọi nút trong của nó có trọng số bằng tổng hai con. Quy nạp từ lá lên cho $\operatorname{wt}(\sigma)$ không nhỏ hơn số lá của cây con đó, tức ít nhất 1.

**Bước 2 (tổ tiên nặng hơn $q$).** Cha $\pi$ của $v$ khác $v$, nên $\operatorname{wt}(\pi)=q+\operatorname{wt}(\sigma)\ge q+1$. Mỗi tổ tiên xa hơn có trọng số bằng tổng hai con, trong đó có một tổ tiên gần hơn, nên trọng số không nhỏ hơn $q+1$. Vậy không tổ tiên nào có trọng số $q$, và $\hat v$ không là tổ tiên của $v$.

**Bước 3 (hậu duệ đứng trước $v$).** Mọi hậu duệ thực sự của $v$ đứng trước $v$ trong danh sách, vì mỗi nút đứng trước cha của nó. Nút $\hat v$ có vị trí không nhỏ hơn vị trí của $v$, nên $\hat v$ không là hậu duệ thực sự của $v$. $\square$
:::

Ở Ví dụ 10.13, nút cuối khối $(\mathrm D,\mathrm B)$ trọng số 4 nằm ở nhánh khác với A, còn các tổ tiên của A có trọng số 6, 10, 20.

::: theorem Định lý 10.25 (Phép tăng–đổi giữ tính chất anh em)
**Giả thiết.** Trước bước 2 của Thuật toán 10.23, sau phép dựng lại ở bước 1 nếu có, cây là cây có trọng số có tính chất anh em, với danh sách mà mỗi nút đứng trước cha; mọi lá có trọng số ít nhất 1, trừ có thể lá của $s$ có trọng số 0.

**Kết luận.** Sau Thuật toán 10.23, cây là cây có trọng số có tính chất anh em, trọng số của lá $s$ tăng 1 và các lá khác giữ nguyên. Do đó cây là cây Huffman cho các trọng số mới (Định lý 10.22), và mã của nó là mã tiền tố tối ưu cho các trọng số hiện thời (Định lý 10.18).

**Điều kiện áp dụng.** Mọi phép đổi chọn nút cuối khối của trọng số cũ; hai nút đổi chỗ mang theo cây con của chúng.

**Phạm vi.** Tối ưu được hiểu cho trọng số hiện thời của cây: số đếm đã đọc sau các lần co, cùng hai lá `ESCAPE`, `EOS` trọng số 1; không cho số đếm của cả thông điệp.
:::

::: proof
Chứng minh dùng bất biến vòng lặp cho bước 3. Gọi $v$ là nút sắp được xử lý ở đầu một lượt. Bất biến gồm bốn điều:

- (I1) trọng số không giảm theo vị trí;
- (I2) với mọi $j$, hai nút ở $\#(2j-1)$ và $\#2j$ là anh em;
- (I3) mọi nút trong khác $v$ có trọng số bằng tổng hai con; nếu $v$ là nút trong, trọng số của nó nhỏ hơn tổng hai con đúng 1;
- (I4) mỗi nút khác gốc đứng trước cha của nó.

**Bước 1 (khởi tạo).** Ở lượt đầu, $v$ là lá của $s$. Giả thiết của định lý cho (I1), (I2), (I4), và (I3) đúng vì chưa trọng số nào thay đổi.

**Bước 2 (phép đổi giữ bất biến).** Gọi $q=\operatorname{wt}(v)$ và $\hat v$ là nút cuối khối trọng số $q$. Theo Bổ đề 10.24, nếu $\hat v\ne v$ thì hai cây con gốc $v$ và $\hat v$ rời nhau, nên phép đổi hợp lệ. Từng bất biến được giữ:

- (I1): hai nút có cùng trọng số $q$.
- (I2): phép đổi chỉ đổi người chiếm hai vị trí, còn mỗi vị trí giữ cha của nó.
- (I3): mỗi cha nhận một con có cùng trọng số với con cũ.
- (I4), với ba nhóm nút:
  - $v$ chuyển lên vị trí của $\hat v$, và cha mới của nó đứng sau vị trí đó theo (I4) cũ; $\hat v$ chuyển xuống vị trí cũ của $v$, và cha mới của nó đứng sau vị trí đó;
  - các con của $v$ đứng trước vị trí cũ của $v$ nên vẫn đứng trước vị trí mới;
  - các con của $\hat v$, nếu $\hat v$ là nút trong, có tổng trọng số $q$ theo (I3), và mỗi con có trọng số dương, vì lá trọng số 0, nếu có, là chính $v$; nên mỗi con nhẹ hơn $q$ và đứng trước cả khối trọng số $q$, tức trước vị trí cũ của $v$.

**Bước 3 (phép tăng giữ bất biến).** Sau phép đổi, $v$ ở vị trí cuối của khối trọng số $q$. Nút ở vị trí kế tiếp, nếu có, có trọng số lớn hơn $q$, tức ít nhất $q+1$; tăng $v$ thành $q+1$ giữ (I1). Trọng số của $v$ giờ bằng tổng hai con nếu $v$ là nút trong, còn cha $\pi$ của $v$ nhỏ hơn tổng hai con đúng 1. Đặt $v\leftarrow\pi$ cho đúng (I3) ở đầu lượt sau; (I2), (I4) không đổi vì không vị trí nào đổi.

**Bước 4 (kết thúc).** Khi $v$ là gốc, (I3) nói gốc thiếu đúng 1; bước 4 của thuật toán tăng gốc, nên mọi nút trong có trọng số bằng tổng hai con. Cùng với (I1), (I2), cây là cây có trọng số có tính chất anh em. Trọng số lá chỉ thay đổi ở $s$, tăng đúng 1, và mọi lá giờ có trọng số ít nhất 1. Định lý 10.22 cho cây là cây Huffman, và Định lý 10.18 cho tính tối ưu. $\square$
:::

Bất biến (I3) giải thích trạng thái ở bước 2 của Ví dụ 10.12: nút $\#6$ ghi 4 trong khi hai con có tổng 5, vì $\#6$ là nút sắp được xử lý.

Thiếu một giả thiết, phép tăng–đổi có thể phá tính chất anh em:

- Bỏ "đổi với nút cuối khối": ở lần tăng thứ hai của Ví dụ 10.12, nếu không đổi, danh sách thành A3, B2, C2, D2, … và không còn không giảm; Tình huống 10.3 cho hậu quả khi bộ giải mã bỏ phép đổi này.
- Bỏ "mọi lá có trọng số dương": nếu một lá $\sigma$ trọng số 0 là anh em của $v$ trọng số $q$, cha của chúng cũng có trọng số $q$ và có thể là nút cuối khối, tức chính tổ tiên mà Bổ đề 10.24 loại trừ.

**Trong thực hành.** Vì hai con của một nút luôn nằm ở hai chỉ số liền nhau trong mảng nút, điều (I2) được bảo đảm bởi chính cách lưu. Một bảng phụ ánh xạ mỗi ký hiệu tới chỉ số lá của nó, nên bộ nén tìm lá của $s$ trong $O(1)$.

<!-- note-topic-id: lec-10-topic-14 -->
### 4.3 Ký hiệu mới, `ESCAPE`, `EOS` và đồng bộ hai phía

Thuật toán 10.23 cập nhật một cây đã có; cây khởi tạo phải được hai phía biết trước mà không cần bảng số đếm. Cây đủ 256 lá giá trị byte trọng số 1 cho mỗi ký hiệu đúng 8 bit lúc đầu, như ASCII, và với thông điệp ngắn, các lá của những ký hiệu không xuất hiện làm lệch thống kê (NG, tr.73). Do đó cây khởi tạo chỉ có hai lá: `ESCAPE` ở $\#1$ và `EOS` ở $\#2$, mỗi lá trọng số 1, dưới gốc trọng số 2 (NG, Hình 4.5, tr.74); hai lá này không bao giờ được tăng, nên luôn có trọng số 1. `EOS` cần một lá riêng vì 8 bit thô chỉ biểu diễn được 256 giá trị byte (NG, tr.90).

Một ký hiệu chưa có trong cây được gửi bằng từ mã của `ESCAPE` rồi 8 bit thô của ký hiệu. Sau đó hai phía thêm một lá cho ký hiệu đó: nút nhẹ nhất, ở $\#1$, trở thành nút trong với hai con là bản sao của nút cũ và một lá mới trọng số 0; rồi Thuật toán 10.23 tăng lá mới (NG, tr.82–83).

::: example Ví dụ 10.14 (Thêm ký hiệu E vào cây A, B, C, D)
**Dữ kiện.** Cây sau, bỏ qua hai lá `ESCAPE` và `EOS` (NG, Hình 4.10, tr.82):

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ |
|---|---|---|---|---|---|---|---|
| Nút | A | B | C | D | (A, B) | (C, D) | gốc |
| Trọng số | 1 | 2 | 2 | 3 | 3 | 5 | 8 |

Ký hiệu tiếp theo là E, chưa có trong cây; mã ASCII của E là $69=01000101_2$.

**Mã hóa.** Bộ mã phát từ mã hiện tại của `ESCAPE`, rồi 8 bit `01000101`.

**Thêm lá.** Nút nhẹ nhất là A ở $\#1$. Vị trí đó thành một nút trong trọng số 1 có hai con: A trọng số 1 và lá mới E trọng số 0. Hai nút mới đứng đầu danh sách, nên mọi vị trí cũ tăng thêm 2:

| Vị trí | $\#1$ | $\#2$ | $\#3$ | $\#4$ | $\#5$ | $\#6$ | $\#7$ | $\#8$ | $\#9$ |
|---|---|---|---|---|---|---|---|---|---|
| Nút | E | A | (E, A) | B | C | D | ($\#3$, B) | (C, D) | gốc |
| Trọng số | 0 | 1 | 1 | 2 | 2 | 3 | 3 | 5 | 8 |

Vì lá mới có trọng số 0, không trọng số nào khác thay đổi, và danh sách vẫn có tính chất anh em.

**Cập nhật E.** E ở $\#1$ là nút duy nhất trọng số 0, không đổi, tăng thành 1. Cha $\#3$ trọng số 1 là nút cuối khối trọng số 1, tăng thành 2. Cha $\#7$ trọng số 3 là nút cuối khối trọng số 3, tăng thành 4. Gốc tăng thành 9. Danh sách cuối là $1,1,2,2,2,3,4,5,9$.

**Kiểm tra lại.** $1+1=2$, $2+2=4$, $2+3=5$, $4+5=9$; danh sách không giảm, và theo quy ước bit ở Mục 4.1, E = `111`, A = `110`, cùng dài 3 bit.
:::

![Hai cây. Cây trên, trước khi thêm E, có danh sách 1, 2, 2, 3, 3, 5, 8. Cây dưới, sau khi thêm và cập nhật E: vị trí cũ của A thành nút trong #3 với hai con A #2 (1) và lá mới E #1, trọng số 0 rồi 1; đường từ E tới gốc được tô đậm; danh sách 1, 1, 2, 2, 2, 3, 4, 5, 9.](img/lec-10/note-them-la-trong-so-0.svg)

Trên hình, lá mới được thêm dưới vị trí của nút nhẹ nhất, nên trong các lá cũ chỉ lá nhẹ nhất, A, dài thêm 1 bit. Ghép cây khởi tạo, phép thêm lá và Thuật toán 10.23, ta được bộ nén và bộ giải nén.

::: algorithm Thuật toán 10.26 (Mã hóa và giải mã Huffman thích nghi)
**Đầu vào.** Bộ nén: thông điệp $x_1\cdots x_n$ gồm các byte. Bộ giải nén: dòng bit do bộ nén phát.

**Đầu ra.** Bộ nén: dòng bit. Bộ giải nén: thông điệp $x_1\cdots x_n$.

**Giả thiết.** Hai phía dùng cùng cây khởi tạo, cùng quy tắc gán bit theo vị trí, cùng phép thêm lá, cùng Thuật toán 10.23 với cùng $W_{\max}$.

**Các bước của bộ nén.**

1. Khởi tạo cây: gốc trọng số 2, hai lá `ESCAPE` ở $\#1$ và `EOS` ở $\#2$, trọng số 1; theo quy ước bit, `ESCAPE` = `1` và `EOS` = `0`.
2. Với $t=1,\ldots,n$: nếu $x_t$ có lá trong cây, phát từ mã của lá đó; nếu không, phát từ mã của `ESCAPE`, phát 8 bit của $x_t$ và thêm lá $x_t$ trọng số 0. Sau đó cập nhật cây bằng Thuật toán 10.23 với $s=x_t$.
3. Phát từ mã của `EOS`.

**Các bước của bộ giải nén.**

1. Khởi tạo cây như bộ nén.
2. Lặp: đi từ gốc theo từng bit tới một lá. Nếu lá là `EOS`, dừng. Nếu lá là `ESCAPE`, đọc 8 bit tiếp theo thành ký hiệu $s$ và thêm lá $s$ trọng số 0; nếu không, $s$ là ký hiệu của lá. Phát $s$ và cập nhật cây bằng Thuật toán 10.23.

**Dừng.** Bộ giải nén dừng khi gặp `EOS`; `EOS` không được cập nhật ở cả hai phía.

**Trường hợp biên.** Thông điệp rỗng thành một bit `0`, từ mã của `EOS` trên cây khởi tạo. Ký hiệu đầu tiên luôn đi qua `ESCAPE`.

**Chi phí.** Mỗi ký hiệu: một lần đi cây, $O(\ell)$ với $\ell$ là độ dài từ mã, một lần cập nhật như Thuật toán 10.23, và 8 bit thô nếu ký hiệu mới.
:::

Cả hai phía cập nhật sau khi xử lý ký hiệu, nên ký hiệu thứ $t$ được mã và giải trên cùng cây sau $t-1$ ký hiệu (NG, tr.25, tr.80).

::: proposition Mệnh đề 10.27 (Đồng bộ hai phía)
**Giả thiết.** Hai phía chạy Thuật toán 10.26 với cùng giả thiết; dòng bit được truyền không lỗi.

**Kết luận.** Với mọi $t=1,\ldots,n+1$, trước khi xử lý ký hiệu thứ $t$ (ký hiệu thứ $n+1$ là `EOS`), hai phía có cùng cây. Do đó bộ giải nén trả về đúng $x_1\cdots x_n$.

**Điều kiện áp dụng.** Mọi thủ tục cập nhật phải tất định và giống hệt nhau ở hai phía, kể cả quy tắc chọn nút cuối khối và thời điểm dựng lại.

**Phạm vi.** Mệnh đề giả thiết kênh truyền không lỗi; một bit sai làm bộ giải nén đi nhầm lá, và từ đó hai cây có thể lệch nhau mãi.
:::

::: proof
Quy nạp theo $t$.

**Bước 1 (cơ sở).** Với $t=1$, hai phía có cùng cây khởi tạo.

**Bước 2 (giải mã đúng ký hiệu thứ $t$).** Giả sử hai phía có cùng cây $T_t$. Cây $T_t$ là cây nhị phân đầy đủ với các ký hiệu ở lá, nên mã của nó là mã tiền tố (Mệnh đề 10.6(a)). Nếu $x_t$ có lá, bộ nén phát $c(x_t)$ và bộ giải nén, đi từ gốc, tới đúng lá đó theo Mệnh đề 10.6(c). Nếu $x_t$ chưa có lá, bộ nén phát $c(\texttt{ESCAPE})$ rồi 8 bit; bộ giải nén tới lá `ESCAPE` rồi đọc đúng 8 bit đó. Với $t=n+1$, bộ giải nén tới lá `EOS` và dừng.

**Bước 3 (cùng cây sau ký hiệu thứ $t$).** Với $t\le n$, hai phía đã biết cùng ký hiệu $x_t$ và cùng việc nó có lá hay chưa. Phép thêm lá và Thuật toán 10.23 là tất định, kể cả kiểm $W_{\max}$ và dựng lại, nên từ cùng $T_t$ và cùng $x_t$, hai phía có cùng $T_{t+1}$. $\square$
:::

Bỏ "cùng thủ tục" thì kết luận sai: nếu bộ giải mã bỏ phép đổi A với D ở lần tăng thứ hai của Ví dụ 10.12, hai cây khác nhau, và từ mã `100` của A ở bộ mã được bộ giải mã đọc thành D (Tình huống 10.3(b)).

**Trong thực hành.** Mỗi ký hiệu mới tốn từ mã của `ESCAPE` cộng 8 bit thô, nên lần đầu gặp một byte tốn ít nhất 9 bit. Mô hình thích nghi bắt đầu gần như không biết gì về dữ liệu, gọi là khởi đầu nguội (cold start), và chỉ cho tỷ lệ nén khá sau vài nghìn byte (NG, tr.25). Nó theo kịp thay đổi cục bộ khi dữ liệu gần đây được tính nặng hơn bằng phép co định kỳ (NG, tr.77).


<!-- note-topic-id: lec-10-topic-15 -->
### 4.4 Chống tràn và dựng lại cây

Trọng số chỉ tăng, nên sau đủ nhiều ký hiệu chúng vượt khả năng của biến lưu trữ. Có hai giới hạn (NG, tr.74):

- trọng số gốc vượt cỡ của bộ đếm, 16 bit;
- từ mã dài nhất vượt cỡ của biến nguyên mà bộ nén dùng để tích các bit khi đi từ lá lên gốc, vì bộ nén thu các bit theo thứ tự ngược rồi mới phát.

Với biến tích bit 16 bit, giới hạn thứ hai có thể đến sớm hơn, vì một cây lệch có từ mã dài với trọng số gốc không lớn. Đặt $\mathrm{fib}(0)=\mathrm{fib}(1)=1$ và $\mathrm{fib}(i)=\mathrm{fib}(i-1)+\mathrm{fib}(i-2)$.

::: example Ví dụ 10.15 (Cây Fibonacci)
**Dữ kiện.** Sáu lá: A, B, C trọng số 1 và ba lá trọng số 2, 3, 5 (NG, Hình 4.6, tr.75).

**Chạy Thuật toán 10.14.** Với quy tắc phá hòa ưu tiên nút vừa tạo, mỗi lượt ghép nút vừa tạo với lá nhẹ nhất còn lại:

1. A1 và B1 thành 2;
2. 2 và C1 thành 3;
3. 3 và lá 2 thành 5;
4. 5 và lá 3 thành 8;
5. 8 và lá 5 thành gốc 13.

**Kết quả.** Cây là một đường lệch: A, B ở độ sâu 5, C ở độ sâu 4, các lá 2, 3, 5 ở độ sâu 3, 2, 1. Các nút trong có trọng số $2,3,5,8,13=\mathrm{fib}(2),\ldots,\mathrm{fib}(6)$, và từ mã dài nhất có $5=6-1$ bit.

**Kiểm tra lại.** $1+1+1+2+3+5=13$, bằng trọng số gốc.
:::

::: remark Nhận xét 10.28 (Ngưỡng Fibonacci và ngưỡng của cài đặt)
Cận Fibonacci: nếu mọi lá có trọng số ít nhất 1 và cây Huffman có một từ mã dài $d$ bit, thì trọng số gốc ít nhất $\mathrm{fib}(d+1)$ (NG, tr.74–75); chứng minh nằm ngoài phạm vi học phần. Ví dụ 10.15 đạt đúng cận này với $d=5$ và gốc $13=\mathrm{fib}(6)$. Theo đó, nếu từ mã được tích trong số nguyên 16 bit, gốc nhỏ hơn $4\,181=\mathrm{fib}(18)$ thì không có từ mã 17 bit, còn gốc đạt $4\,181$ đã có thể có từ mã 17 bit gây tràn. Ngưỡng $W_{\max}$ được chọn bằng `0x8000` $=32\,768$, và từ mã được tích trong biến `unsigned long` (NG, tr.88, 91).
:::

Khi trọng số gốc đạt $W_{\max}$, mọi trọng số lá được co thành $\lfloor(\omega+1)/2\rfloor$, với $\omega$ là trọng số cũ của lá, nên không lá có trọng số dương nào về 0 (NG, mã nguồn, tr.85), rồi cây được dựng lại từ các lá (NG, tr.75–77). Giữ hình dạng cũ có thể làm mất tính chất anh em (Bài tập 10.5). Chúng ta chạy tay bước dựng mới (NG, Hình 4.11–4.12).

::: example Ví dụ 10.16 (Dựng lại cây từ bốn lá)
**Dữ kiện.** Sau khi co, bốn lá có trọng số A: 1, B: 3, C: 5, D: 7 (NG, tr.86). Danh sách lá theo trọng số tăng dần là A1, B3, C5, D7.

**Ghép theo danh sách.** Bước dựng lại không dùng hàng đợi mà giữ một danh sách sắp theo trọng số, ghép hai nút nhẹ nhất chưa ghép rồi chèn nút mới vào đúng chỗ trong danh sách:

1. Ghép A1 và B3 thành 4; chèn 4 trước C5 vì $4<5$: danh sách A1, B3, (A, B)4, C5, D7.
2. Ghép (A, B)4 và C5 thành 9; chèn sau D7: danh sách A1, B3, 4, C5, D7, 9.
3. Ghép D7 và 9 thành gốc 16.

**Kết quả.** Độ dài từ mã: D 1 bit, C 2 bit, A và B 3 bit. Danh sách cuối $1,3,4,5,7,9,16$ có các cặp anh em ở $(\#1,\#2)$, $(\#3,\#4)$, $(\#5,\#6)$.

**Kiểm tra lại.** $1+3+5+7=16$.
:::

Bước dựng lại là Thuật toán 10.14 với hàng đợi ưu tiên cài bằng danh sách sắp: mỗi lần lấy hai phần tử đầu và chèn nút mới bằng phép chèn có thứ tự.

::: algorithm Thuật toán 10.29 (Co trọng số và dựng lại cây)
**Đầu vào.** Cây hiện thời với $k'\ge2$ lá, gốc có trọng số $W_{\max}$.

**Giả thiết.** Mọi lá có trọng số ít nhất 1, trừ có thể lá vừa được thêm, có trọng số 0; Thuật toán 10.26 thêm lá trước khi Thuật toán 10.23 kiểm $W_{\max}$ (NG, tr.91–93), nên trường hợp này xảy ra được, và lá đó giữ trọng số 0 sau khi co.

**Đầu ra.** Cây có trọng số mới có tính chất anh em, cùng tập lá, mỗi lá có trọng số $\lfloor(\omega+1)/2\rfloor$ với $\omega$ là trọng số cũ.

**Các bước.**

1. Khởi tạo: giữ các lá, bỏ mọi nút trong; thay trọng số mỗi lá $\omega$ bằng $\lfloor(\omega+1)/2\rfloor$.
2. Xếp các lá theo trọng số tăng dần thành một danh sách.
3. Lặp $k'-1$ lần: ghép hai nút nhẹ nhất chưa có cha thành một nút mới có trọng số bằng tổng; chèn nút mới vào danh sách ngay sau nút cuối cùng có trọng số không lớn hơn nó.
4. Sau khi mọi nút đã có vị trí cố định, gán con trỏ cha cho mọi nút.

**Dừng.** Sau $k'-1$ lần ghép, nút cuối của danh sách là gốc.

**Trường hợp biên.** Lá trọng số 1 vẫn có trọng số $\lfloor2/2\rfloor=1$, nên hai lá `ESCAPE` và `EOS` luôn có trọng số 1; lá trọng số 0 giữ 0.

**Chi phí.** Bước 1 và 2 tốn $O(k')$ khi danh sách lá đã sắp, như trong mảng nút; mỗi lần chèn ở bước 3 dịch tới $O(k')$ phần tử (NG, tr.86), tổng $O(k'^2)$. Phép dựng lại chỉ xảy ra khi gốc đạt $W_{\max}$; sau đó gốc còn khoảng $W_{\max}/2$, nên giữa hai lần dựng lại có cỡ $W_{\max}/2$ ký hiệu.
:::

Con trỏ cha được gán sau cùng vì các nút chưa được ghép còn bị dịch chỗ khi chèn (NG, tr.86). Về tính đúng, bước 3 là một lần chạy Thuật toán 10.14 trên các trọng số đã co, với quy tắc phá hòa của phép chèn, nên cây là cây Huffman; theo Định lý 10.22, chiều thuận, nó có tính chất anh em, kể cả khi có lá trọng số 0. Phép chèn đặt nút mới sau mọi nút không nặng hơn nó, nên mỗi nút đứng trước cha; vì vậy các bước 2–4 của Thuật toán 10.23 chạy trên cây mới thỏa giả thiết của Định lý 10.25.

**Trong thực hành.** Trong thử nghiệm của NG (tr.77), co trọng số định kỳ thường cho tỷ lệ nén tốt hơn hoãn việc co, vì dòng dữ liệu thường có hiệu ứng gần đây: số liệu gần đây dự báo ký hiệu sắp tới tốt hơn; điểm co tốt nhất phụ thuộc loại dữ liệu.

::: exercise Bài tập 10.5 (Chia đôi bỏ phần lẻ và làm tròn lên)
Cây Huffman của bốn lá A: 3, B: 3, C: 6, D: 6 có A, B là anh em dưới nút trọng số 6 và C, D là anh em dưới nút trọng số 12, gốc 18 (NG, Hình 4.7, tr.76). Chia đôi bỏ phần lẻ cho A1, B1, C3, D3; giữ hình dạng cũ thì được cây A1, B1, C3, D3 ở Mục 4.1, không có tính chất anh em. (a) Dựng cây Huffman cho A1, B1, C3, D3 và ghi danh sách vị trí. (b) Co bằng $\lfloor(\omega+1)/2\rfloor$, giữ hình dạng cây, tính lại trọng số các nút trong và kiểm tính chất anh em.
:::

::: hint
Ở (a), chạy Thuật toán 10.14 trên A1, B1, C3, D3.
:::

::: solution
**(a)** Lá đã co là A1, B1, C3, D3. Thuật toán 10.14 cho A1 và B1 thành 2, rồi 2 và C3 thành 5, rồi D3 và 5 thành 8: độ sâu D 1, C 2, A và B 3, danh sách $1,1,2,3,3,5,8$ (NG, Hình 4.9).

**(b)** Lá thành A2, B2, C3, D3; các nút trong là $2+2=4$, $3+3=6$, gốc 10. Danh sách $2,2,3,3,4,6,10$ không giảm với các cặp $(\mathrm A,\mathrm B)$, $(\mathrm C,\mathrm D)$, $(4,6)$; cây giữ tính chất anh em và hình dạng cân bằng.
:::

Như vậy, chúng ta đã có một bộ nén một lượt không cần đầu mục (Thuật toán 10.26): phép tăng–đổi giữ tính chất anh em (Định lý 10.25), nên sau mỗi ký hiệu cây là cây Huffman tối ưu cho trọng số hiện thời của nó; hai phía luôn có cùng cây (Mệnh đề 10.27); phép co và dựng lại giữ trọng số trong giới hạn của cài đặt (Thuật toán 10.29). Tuy nhiên, cả hai mã Huffman vẫn gán cho mỗi ký hiệu một từ mã nguyên bit, nên mỗi ký hiệu tốn ít nhất 1 bit. Trong Mục 5, chúng ta mã cả chuỗi bằng một khoảng số thực để bỏ giới hạn đó.

## 5. Mã số học với số thực

Với ký hiệu xác suất $1/3$, tự thông tin là $1{,}585$ bit nhưng mã Huffman phải dùng 1 hoặc 2 bit; với ký hiệu xác suất $0{,}9$, tự thông tin là $0{,}152$ bit nhưng mã Huffman dùng 1 bit, dài gấp khoảng $6{,}6$ lần. Với ảnh hai màu của máy fax, mọi mã ký hiệu dùng ít nhất 1 bit mỗi điểm ảnh, mã Huffman dùng đúng 1 bit, và không nén được gì (NG, tr.96). Với $1\,000$ ký hiệu xác suất $0{,}999$, tổng tự thông tin chỉ khoảng $1{,}44$ bit, còn mã Huffman tốn $1\,000$ bit (CMU, trang chiếu 37). Để đến gần $I(x)$ khi xác suất lớn, chúng ta mã cả thông điệp thành một số trong $[0;1)$ thay vì nối các từ mã.

<!-- note-topic-id: lec-10-topic-16 -->
### 5.1 Khoảng của một chuỗi

Xét thông điệp BILL GATES, mười ký hiệu kể cả khoảng trắng, với mô hình tĩnh chia $[0;1)$ thành chín khoảng (NG, tr.97):

| Ký hiệu | khoảng trắng | A | B | E | G | I | L | S | T |
|---|---|---|---|---|---|---|---|---|---|
| $p_s$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}2$ | $0{,}1$ | $0{,}1$ |
| khoảng | $[0;\,0{,}1)$ | $[0{,}1;\,0{,}2)$ | $[0{,}2;\,0{,}3)$ | $[0{,}3;\,0{,}4)$ | $[0{,}4;\,0{,}5)$ | $[0{,}5;\,0{,}6)$ | $[0{,}6;\,0{,}8)$ | $[0{,}8;\,0{,}9)$ | $[0{,}9;\,1)$ |

Ký hiệu đầu B thu hẹp $[0;1)$ thành khoảng của B, $[0{,}2;\,0{,}3)$. Ký hiệu thứ hai I chọn trong khoảng đó phần tương ứng với khoảng của I, tức đoạn từ 50% tới 60% của độ dài: $[0{,}25;\,0{,}26)$. Ký hiệu thứ ba L chọn đoạn từ 60% tới 80%: $[0{,}256;\,0{,}258)$. Chúng ta viết phép thu hẹp này thành công thức.

::: definition Định nghĩa 10.30 (Khoảng ký hiệu và khoảng chuỗi)
Cho mô hình tĩnh $P$ với mọi $p_s>0$ và thứ tự cố định trên $\Sigma$.

- **Xác suất tích lũy** (cumulative probability) trước $s$ là $F(s)=\sum_{s'<s}p_{s'}$, không gồm chính $s$. **Khoảng ký hiệu** (symbol interval) của $s$ là $[F(s);\,F(s)+p_s)$.
- **Khoảng chuỗi** (sequence interval) của $x_1\cdots x_t$ là $[a_t;\,a_t+w_t)$, xác định bởi $a_0=0$, $w_0=1$ và với $t\ge1$
$$
\begin{aligned}
a_t&=a_{t-1}+w_{t-1}F(x_t),\\
w_t&=w_{t-1}\,p_{x_t}.
\end{aligned}
$$
:::

Cận dưới dời lên một phần $F(x_t)$ của độ rộng cũ, độ rộng mới bằng phần $p_{x_t}$ của độ rộng cũ. Các khoảng là nửa mở: mỗi ký hiệu sở hữu mọi số từ cận dưới tới cận trên nhưng không gồm cận trên, nên điểm $0{,}2$ thuộc B chứ không thuộc A (NG, tr.97). $F(s)$ loại trừ chính $s$; dùng hàm phân phối tích lũy $\sum_{s'\le s}p_{s'}$ sẽ lệch một ký hiệu. Thứ tự trên $\Sigma$ là tùy ý nhưng phải là một phần của giao thức.

::: example Ví dụ 10.17 (Mã hóa BILL GATES)
**Dữ kiện.** Thông điệp B, I, L, L, khoảng trắng, G, A, T, E, S với bảng khoảng ký hiệu sau:

| Ký hiệu | khoảng trắng | A | B | E | G | I | L | S | T |
|---|---|---|---|---|---|---|---|---|---|
| $p_s$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}1$ | $0{,}2$ | $0{,}1$ | $0{,}1$ |
| khoảng | $[0;\,0{,}1)$ | $[0{,}1;\,0{,}2)$ | $[0{,}2;\,0{,}3)$ | $[0{,}3;\,0{,}4)$ | $[0{,}4;\,0{,}5)$ | $[0{,}5;\,0{,}6)$ | $[0{,}6;\,0{,}8)$ | $[0{,}8;\,0{,}9)$ | $[0{,}9;\,1)$ |

**Tính.** Mỗi dòng áp dụng hai công thức của Định nghĩa 10.30 (NG, tr.98):

| $t$ | $x_t$ | $a_t$ | $a_t+w_t$ | $w_t$ |
|---|---|---|---|---|
| 1 | B | $0{,}2$ | $0{,}3$ | $10^{-1}$ |
| 2 | I | $0{,}25$ | $0{,}26$ | $10^{-2}$ |
| 3 | L | $0{,}256$ | $0{,}258$ | $2\cdot10^{-3}$ |
| 4 | L | $0{,}2572$ | $0{,}2576$ | $4\cdot10^{-4}$ |
| 5 | khoảng trắng | $0{,}2572$ | $0{,}25724$ | $4\cdot10^{-5}$ |
| 6 | G | $0{,}257216$ | $0{,}25722$ | $4\cdot10^{-6}$ |
| 7 | A | $0{,}2572164$ | $0{,}2572168$ | $4\cdot10^{-7}$ |
| 8 | T | $0{,}25721676$ | $0{,}2572168$ | $4\cdot10^{-8}$ |
| 9 | E | $0{,}257216772$ | $0{,}257216776$ | $4\cdot10^{-9}$ |
| 10 | S | $0{,}2572167752$ | $0{,}2572167756$ | $4\cdot10^{-10}$ |

**Kiểm tra lại.** Độ rộng cuối bằng tích các xác suất, $0{,}1^8\cdot0{,}2^2=4\cdot10^{-10}$, và $I(x)=-\log_2(4\cdot10^{-10})\approx31{,}22$ bit.
:::

![Ba thanh ngang chồng nhau, mỗi thanh chia thành chín khoảng ký hiệu theo thứ tự khoảng trắng, A, B, E, G, I, L, S, T, L rộng gấp đôi. Thanh 1 từ 0 tới 1 tô ô B; thanh 2 từ 0,2 tới 0,3 tô ô I; thanh 3 từ 0,25 tới 0,26 tô ô L. Sau B, I, L, khoảng là từ 0,256 tới 0,258, độ rộng 0,002.](img/lec-10/note-khoang-bill-gates.svg)

Một cách trực quan, mỗi ký hiệu chọn một phần của khoảng hiện thời tỷ lệ với xác suất của nó. Trên hình, mỗi thanh dưới là bản phóng to của ô được tô ở thanh trên, nên cùng một phép chia lặp lại. Phép thu hẹp có ba tính chất sau.

::: proposition Mệnh đề 10.31 (Khoảng chuỗi lồng nhau, độ rộng bằng xác suất, phân hoạch)
**Giả thiết.** Mô hình tĩnh $P$ với mọi $p_s>0$; khoảng chuỗi như Định nghĩa 10.30.

**Kết luận.**

- (a) $[a_t;\,a_t+w_t)\subseteq[a_{t-1};\,a_{t-1}+w_{t-1})$ với mọi $t\ge1$.
- (b) $w_n=\prod_{t=1}^{n}p_{x_t}$, nên $-\log_2w_n=I(x)$.
- (c) Với mỗi $n\ge1$, khoảng chuỗi của $k^n$ thông điệp độ dài $n$ đôi một rời nhau và có hợp bằng $[0;1)$.

**Điều kiện áp dụng.** Các khoảng là nửa mở và các phép tính là chính xác, không làm tròn.

**Phạm vi.** Với mô hình thích nghi, $p_{x_t}$ được thay bằng xác suất ở bước $t$ và chứng minh không đổi.
:::

::: proof
**Bước 1 (phần (a), (b)).** Vì $0\le F(x_t)$ và $F(x_t)+p_{x_t}\le1$,
$$
\begin{aligned}
a_t&=a_{t-1}+w_{t-1}F(x_t)\\
&\ge a_{t-1},\\
a_t+w_t&=a_{t-1}+w_{t-1}\bigl(F(x_t)+p_{x_t}\bigr)\\
&\le a_{t-1}+w_{t-1}.
\end{aligned}
$$
Công thức $w_t=w_{t-1}p_{x_t}$ với $w_0=1$ cho (b) bằng quy nạp.

**Bước 2 (phần (c), quy nạp theo $n$).** Với $n=0$, chuỗi rỗng có khoảng $[0;1)$. Giả sử các khoảng của mọi chuỗi độ dài $n-1$ đôi một rời nhau và phủ $[0;1)$. Xếp các ký hiệu theo thứ tự $\varsigma_1<\cdots<\varsigma_k$; khi đó $F(\varsigma_1)=0$, $F(\varsigma_{i+1})=F(\varsigma_i)+p_{\varsigma_i}$ và $F(\varsigma_k)+p_{\varsigma_k}=1$. Với một chuỗi $y$ độ dài $n-1$ có khoảng $[a;\,a+w)$, các khoảng của $y\varsigma_1,\ldots,y\varsigma_k$ là
$$
\bigl[a+wF(\varsigma_i);\,a+wF(\varsigma_{i+1})\bigr),
$$
với $i=1,\ldots,k$ và quy ước $F(\varsigma_{k+1})=1$. Chúng nằm liền nhau từ $a$ tới $a+w$, nên đôi một rời nhau và có hợp bằng $[a;\,a+w)$. Lấy hợp theo mọi $y$ và dùng giả thiết quy nạp được (c). $\square$
:::

Phần (b) là cầu nối giữa khoảng và số bit: độ rộng của khoảng cuối bằng xác suất của thông điệp theo mô hình. Ở BILL GATES, $w_{10}=4\cdot10^{-10}$ ứng với $31{,}22$ bit. Phần (c) là cơ sở của giải mã: mỗi số trong $[0;1)$ thuộc khoảng của đúng một thông điệp độ dài $n$. Bỏ "khoảng nửa mở" thì (c) sai: với khoảng đóng, điểm $0{,}2$ thuộc cả khoảng của A lẫn khoảng của B.

### 5.2 Mã hóa và giải mã

Bộ mã chỉ cần phát một số $z$ trong khoảng cuối. Bộ giải mã tìm ký hiệu đầu bằng cách xem $z$ thuộc khoảng ký hiệu nào, rồi đưa $z$ về thang $[0;1)$ để tìm ký hiệu tiếp theo. Với $z=0{,}2572167752$: $z\in[0{,}2;\,0{,}3)$ nên ký hiệu đầu là B, và $(z-0{,}2)/0{,}1=0{,}572167752$ thuộc khoảng của I.

::: algorithm Thuật toán 10.32 (Mã số học với số thực)
**Đầu vào.** Mô hình tĩnh $P$ với mọi $p_s>0$, xác suất tích lũy $F$; bộ mã nhận thông điệp $x_1\cdots x_n$; bộ giải mã nhận số $z$ và độ dài $n$.

**Đầu ra.** Bộ mã: một số $z\in[a_n;\,a_n+w_n)$. Bộ giải mã: thông điệp $x_1\cdots x_n$.

**Giả thiết.** Phép tính số thực chính xác; hai phía dùng cùng $P$ và cùng thứ tự ký hiệu.

**Các bước của bộ mã.**

1. Đặt $a\gets0$, $w\gets1$.
2. Với $t=1,\ldots,n$: $a\gets a+wF(x_t)$, rồi $w\gets w\,p_{x_t}$.
3. Phát một số $z\in[a;\,a+w)$; mọi số trong khoảng đều giải đúng (Mệnh đề 10.31), và số bit của $z$ được chọn ở Mục 5.4.

**Các bước của bộ giải mã.**

1. Đặt $\zeta\gets z$.
2. Với $t=1,\ldots,n$: tìm ký hiệu $s$ có $F(s)\le\zeta<F(s)+p_s$, phát $x_t=s$, rồi đặt $\zeta\gets(\zeta-F(s))/p_s$.

**Dừng.** Sau $n$ ký hiệu, hoặc khi giải ra `EOS` nếu mô hình có ký hiệu này.

**Trường hợp biên.** Khi $\zeta$ trùng cận dưới của một khoảng ký hiệu, $\zeta$ thuộc khoảng đó, theo quy ước nửa mở. Ký hiệu có $p_s=0$ không được phép, vì khoảng của nó rỗng.

**Chi phí.** Mỗi ký hiệu tốn $O(1)$ phép số học ở bộ mã; bộ giải mã thêm một lần tìm khoảng, $O(k)$ khi quét tuyến tính. Với số thực chính xác, số chữ số của $a$ và $w$ tăng theo $n$, nên chi phí thực của mỗi phép tính tăng theo độ dài thông điệp.
:::

Tính đúng của bộ giải mã suy từ Mệnh đề 10.31. Nếu $z$ thuộc khoảng chuỗi của $x$, thì theo (a) $z$ thuộc khoảng của $x_1$, và theo (c) với $n=1$ nó không thuộc khoảng ký hiệu nào khác, nên ký hiệu đầu được giải đúng. Phép biến đổi $\zeta\mapsto(\zeta-F(x_1))/p_{x_1}$ đưa khoảng của $x_1$ về $[0;1)$ và đưa khoảng chuỗi của $x$ về khoảng chuỗi của $x_2\cdots x_n$; quy nạp theo $n$ cho kết luận.

::: example Ví dụ 10.18 (Giải mã BILL GATES)
**Dữ kiện.** $z=0{,}2572167752$, $n=10$, bảng khoảng ký hiệu của BILL GATES (Ví dụ 10.17).

**Tính.** Bắt đầu với $\zeta=z$, mỗi dòng tìm khoảng chứa $\zeta$ rồi tính $\zeta\gets(\zeta-F(s))/p_s$ (NG, tr.99):

| $\zeta$ | ký hiệu | khoảng | $\zeta$ mới |
|---|---|---|---|
| $0{,}2572167752$ | B | $[0{,}2;\,0{,}3)$ | $0{,}572167752$ |
| $0{,}572167752$ | I | $[0{,}5;\,0{,}6)$ | $0{,}72167752$ |
| $0{,}72167752$ | L | $[0{,}6;\,0{,}8)$ | $0{,}6083876$ |
| $0{,}6083876$ | L | $[0{,}6;\,0{,}8)$ | $0{,}041938$ |
| $0{,}041938$ | khoảng trắng | $[0;\,0{,}1)$ | $0{,}41938$ |
| $0{,}41938$ | G | $[0{,}4;\,0{,}5)$ | $0{,}1938$ |
| $0{,}1938$ | A | $[0{,}1;\,0{,}2)$ | $0{,}938$ |
| $0{,}938$ | T | $[0{,}9;\,1)$ | $0{,}38$ |
| $0{,}38$ | E | $[0{,}3;\,0{,}4)$ | $0{,}8$ |
| $0{,}8$ | S | $[0{,}8;\,0{,}9)$ | $0$ |

**Kiểm tra lại.** Mười ký hiệu giải ra là BILL GATES. Bộ giải mã dừng nhờ biết $n=10$; nếu không biết $n$, số 0 ở dòng cuối vẫn thuộc khoảng của khoảng trắng và bộ giải mã sẽ phát thêm ký hiệu.
:::

<!-- note-topic-id: lec-10-topic-17 -->
### 5.3 Cách dừng và khoảng mã

Dòng cuối của Ví dụ 10.18 cho thấy bộ giải mã cần biết khi nào dừng. Có hai cách dừng: truyền kèm độ dài, hoặc thêm vào mô hình một ký hiệu kết thúc dòng chỉ xuất hiện ở cuối thông điệp (NG, tr.99). Bộ mã thanh ghi ở Mục 6 dùng cách thứ hai. Khi dùng `EOS`, các thông điệp có độ dài khác nhau, nên Mệnh đề 10.31(c) không còn đủ.

::: proposition Mệnh đề 10.33 (Thông điệp kết thúc bằng `EOS`)
**Giả thiết.** `EOS` là một ký hiệu của $\Sigma$ với $p_{\texttt{EOS}}>0$; $x$ và $y$ là hai thông điệp khác nhau, mỗi thông điệp có `EOS` ở vị trí cuối và chỉ ở đó.

**Kết luận.** Khoảng chuỗi của $x$ và của $y$ rời nhau.

**Điều kiện áp dụng.** `EOS` không xuất hiện ở giữa thông điệp.

**Phạm vi.** Mệnh đề chỉ cần cho cách dừng bằng `EOS`; với độ dài $n$ truyền kèm, Mệnh đề 10.31(c) đã đủ.
:::

::: proof
Nếu $x$ là tiền tố thực sự của $y$, ký hiệu cuối của $x$ là `EOS` và xuất hiện trong $y$ ở một vị trí không phải vị trí cuối, trái giả thiết; tương tự với vai trò đổi lại. Vậy có vị trí $t\le\min(\lvert x\rvert,\lvert y\rvert)$ đầu tiên mà $x_t\ne y_t$. Hai chuỗi $x_1\cdots x_t$ và $y_1\cdots y_t$ khác nhau và cùng độ dài, nên khoảng chuỗi của chúng rời nhau theo Mệnh đề 10.31(c). Theo Mệnh đề 10.31(a), khoảng của $x$ và của $y$ nằm trong hai khoảng đó, nên cũng rời nhau. $\square$
:::

Bỏ "`EOS` chỉ ở cuối" thì kết luận sai: với mô hình A: $0{,}9$, `EOS`: $0{,}1$ theo thứ tự đó, thông điệp A `EOS` có khoảng $[0{,}81;\,0{,}9)$, còn A `EOS` A `EOS` có khoảng $[0{,}8829;\,0{,}891)$ nằm trong khoảng đó.

Một số $z$ trong khoảng cuối đủ để giải mã khi bộ giải mã biết cách dừng, nhưng số bit của $z$ chưa được chọn. Để làm rõ, ta tìm chuỗi bit ngắn nhất cho một thông điệp có xác suất lớn.

::: example Ví dụ 10.19 (Bảy chữ A và ký hiệu kết thúc)
**Dữ kiện.** Mô hình hai ký hiệu A với xác suất $0{,}9$ và END với xác suất $0{,}1$, khoảng ký hiệu $[0;\,0{,}9)$ và $[0{,}9;\,1)$; thông điệp gồm bảy chữ A rồi END (NG, tr.104).

**Khoảng cuối.** Sau bảy chữ A, $a_7=0$ và $w_7=0{,}9^7=0{,}4782969$; END cho
$$
\begin{aligned}
a_8&=0{,}9^7\cdot0{,}9=0{,}43046721,\\
w_8&=0{,}9^7\cdot0{,}1=0{,}04782969.
\end{aligned}
$$
Khoảng cuối là $[0{,}43046721;\,0{,}4782969)$, và $I(x)=-\log_2w_8\approx4{,}386$ bit.

**Chuỗi bit.** Số thập phân $0{,}45$ nằm trong khoảng cuối và cần hai chữ số, tương đương $\log_2100\approx6{,}64$ bit. Với số nhị phân, xét các chuỗi bit có khoảng mã (Định nghĩa 10.7) nằm trong khoảng cuối:

- 4 bit: `0111` có khoảng mã $[0{,}4375;\,0{,}5)$, vượt cận trên $0{,}4782969$; không chuỗi 4 bit nào khác có khoảng mã nằm trong khoảng cuối;
- 5 bit: `01110` có khoảng mã $[0{,}4375;\,0{,}46875)$, nằm trong khoảng cuối.

**So với Huffman.** Bảng chữ cái có hai ký hiệu, nên mã Huffman dùng 1 bit cho mỗi ký hiệu, tức 8 bit.

**Kiểm tra lại.** $0{,}43046721\le0{,}4375$ và $0{,}46875\le0{,}4782969$.
:::

![Trục số từ 0,42 tới 0,51: khoảng chuỗi từ 0,4305 tới 0,4783 của bảy chữ A và END; khoảng mã của 01110 và của 011101 nằm trong nó; khoảng mã của 0111, từ 0,4375 tới 0,5, viền nét đứt, vượt cận trên.](img/lec-10/note-khoang-ma-trong-khoang-chuoi.svg)

Trên hình, khoảng mã của `0111` vượt cận trên của khoảng cuối, còn khoảng mã của `01110` và `011101` nằm trọn trong nó; `011101` là chuỗi do quy tắc của Định lý 10.34 dưới đây cho. Khi khoảng mã nằm trọn trong khoảng chuỗi, mọi phần kéo dài của chuỗi bit đều chỉ vào khoảng chuỗi, nên dòng bit tự kết thúc và các dòng bit của những thông điệp khác nhau tạo thành một mã tiền tố.

### 5.4 Cận độ dài

Chúng ta cần một quy tắc chọn chuỗi bit có khoảng mã nằm trong khoảng chuỗi, với độ dài gần $I(x)$. Quy tắc lấy trung điểm của khoảng chuỗi rồi cắt khai triển nhị phân của nó còn $\lambda$ bit (CMU, trang chiếu 48).

::: theorem Định lý 10.34 (Khoảng mã trong khoảng chuỗi và cận độ dài)
**Giả thiết.** Khoảng chuỗi cuối $[a_n;\,a_n+w_n)$ của một thông điệp, với $w_n>0$. Đặt
$$
\begin{gathered}
\lambda=\lceil-\log_2w_n\rceil+1,\\
z=2^{-\lambda}\Bigl\lfloor2^{\lambda}\bigl(a_n+\tfrac{w_n}2\bigr)\Bigr\rfloor,
\end{gathered}
$$
và gọi $b_1\cdots b_\lambda$ là chuỗi $\lambda$ bit có $z=0{,}b_1\cdots b_\lambda$.

**Kết luận.**

- (a) Khoảng mã của $b_1\cdots b_\lambda$ nằm trong khoảng chuỗi: $[z;\,z+2^{-\lambda})\subseteq[a_n;\,a_n+w_n)$.
- (b) Nếu các thông điệp có khoảng chuỗi đôi một rời nhau, như khi cùng độ dài (Mệnh đề 10.31(c)) hoặc cùng kết thúc bằng `EOS` (Mệnh đề 10.33), thì các chuỗi bit của chúng tạo thành một mã tiền tố.
- (c) $I(x)\le\lambda<I(x)+2$; hơn nữa mọi chuỗi bit có khoảng mã nằm trong khoảng chuỗi có độ dài ít nhất $I(x)$.

**Điều kiện áp dụng.** Số học chính xác; khoảng chuỗi của các thông điệp cần phân biệt đôi một rời nhau, nhờ độ dài biết trước hoặc `EOS`.

**Phạm vi.** Quy tắc không luôn cho chuỗi ngắn nhất (Bài tập 10.20). Kết quả là của mã số học lý tưởng; bộ mã thanh ghi ở Mục 6 kết thúc theo quy tắc khác và có thêm các khoản cố định.
:::

::: proof
**Bước 1 (bước lưới nhỏ hơn nửa độ rộng).** Từ $\lambda\ge-\log_2w_n+1$ suy ra $2^{-\lambda}\le w_n/2$.

**Bước 2 (đầu dưới).** Theo $\lfloor\upsilon\rfloor>\upsilon-1$ và Bước 1,
$$
\begin{aligned}
z&>a_n+\tfrac{w_n}2-2^{-\lambda}\\
&\ge a_n+\tfrac{w_n}2-\tfrac{w_n}2=a_n .
\end{aligned}
$$

**Bước 3 (đầu trên).** Theo $\lfloor\upsilon\rfloor\le\upsilon$ và Bước 1,
$$
\begin{aligned}
z+2^{-\lambda}&\le a_n+\tfrac{w_n}2+2^{-\lambda}\\
&\le a_n+w_n .
\end{aligned}
$$
Vì $a_n+w_n\le1$ theo Mệnh đề 10.31(a), $0\le z<1$ và $2^\lambda z$ là số nguyên trong $[0;\,2^\lambda)$, nên chuỗi $b_1\cdots b_\lambda$ tồn tại; Bước 2 và Bước 3 cho (a).

**Bước 4 (phần (b)).** Khoảng mã của mỗi chuỗi bit nằm trong khoảng chuỗi của thông điệp của nó; các khoảng chuỗi đôi một rời nhau, nên các khoảng mã cũng vậy. Theo Bổ đề 10.8(c), các chuỗi bit tạo thành một mã tiền tố.

**Bước 5 (phần (c)).** Theo $\lceil\upsilon\rceil<\upsilon+1$, $\lambda<I(x)+2$, và $\lambda\ge I(x)+1>I(x)$. Một chuỗi bit độ dài $\lambda'$ có khoảng mã nằm trong khoảng chuỗi thì $2^{-\lambda'}\le w_n$, tức $\lambda'\ge-\log_2w_n=I(x)$. $\square$
:::

Ở Ví dụ 10.19, $I(x)\approx4{,}386$ nên quy tắc cho $\lambda=\lceil4{,}386\rceil+1=6$: trung điểm $a_8+w_8/2\approx0{,}45438$, nhân $2^6$ được $29{,}08$, nên $z=29/64$ và chuỗi bit là `011101`, có khoảng mã $[0{,}453125;\,0{,}46875)$. Chuỗi ngắn nhất `01110` có 5 bit, đúng bằng cận dưới $\lceil I(x)\rceil=5$ của (c).

Lấy kỳ vọng hai vế của (c) cho cận theo entropy khi thông điệp ngẫu nhiên.

::: corollary Hệ quả 10.35 (Độ dài kỳ vọng của mã số học)
**Giả thiết.** $X=X_1\cdots X_n$ gồm $n$ ký hiệu độc lập cùng phân phối $P$, và mã số học dùng đúng mô hình $P$ với độ dài $n$ đã biết.

**Kết luận.** Số bit kỳ vọng $\mathbb E[\lambda(X)]$ thỏa $nH(P)\le\mathbb E[\lambda(X)]<nH(P)+2$.

**Điều kiện áp dụng.** Mô hình đúng là phân phối sinh dữ liệu; các ký hiệu độc lập.

**Phạm vi.** Phần thừa kỳ vọng của mã Huffman từng ký hiệu là $n(\bar\ell(c_{\mathrm H})-H(P))$, tuyến tính theo $n$ trừ khi mọi $p_s$ là lũy thừa của $\tfrac12$; phần thừa của mã số học lý tưởng dưới 2 bit cho cả thông điệp.
:::

::: proof
Theo Mệnh đề 10.31(b), $I(X)=\sum_{t=1}^{n}-\log_2p_{X_t}$. Theo tuyến tính kỳ vọng và vì mỗi $X_t$ có phân phối $P$, $\mathbb E[I(X)]=nH(P)$. Lấy kỳ vọng hai vế của $I(X)\le\lambda(X)<I(X)+2$ ở Định lý 10.34(c). $\square$
:::

Định lý 10.34 và Hệ quả 10.35 có thể sai khi bỏ một giả thiết:

- Bỏ quy tắc chọn chuỗi của Định lý 10.34: chuỗi `0111` của Ví dụ 10.19 biểu diễn $0{,}4375$, nằm trong khoảng chuỗi, nhưng khoảng mã $[0{,}4375;\,0{,}5)$ vượt cận trên $0{,}4783$, nên chỉ giải đúng khi bộ giải mã đệm bit 0.
- Bỏ "mô hình đúng" ở Hệ quả 10.35: với bảng mã dựng từ dữ liệu khác, số bit kỳ vọng có thể vượt xa $nH$, như tệp Q, Z của Tình huống 10.3(a).

**Trong thực hành.** Thuật toán 10.32 và Định lý 10.34 cần $a_n$ và $w_n$ chính xác, mà $w_n$ giảm theo hàm mũ của $n$; một số thực 80 bit không đủ cho thông điệp dài (NG, tr.100; EE398A-3, trang chiếu 10). Cài đặt thật dùng thanh ghi số nguyên cố định và phát dần các bit đã chắc chắn.

::: exercise Bài tập 10.6 (Ba ký hiệu và một số thập phân)
Mô hình ba ký hiệu $p(\mathrm a)=0{,}2$, $p(\mathrm b)=0{,}5$, $p(\mathrm c)=0{,}3$ theo thứ tự a, b, c (CMU, trang chiếu 39–44). Tính khoảng chuỗi của bac; tính $\lambda$ và chuỗi bit theo Định lý 10.34, và tìm chuỗi bit ngắn nhất có khoảng mã nằm trong khoảng chuỗi. Giải mã số $0{,}49$ khi biết thông điệp có 3 ký hiệu.
:::

::: hint
$F(\mathrm a)=0$, $F(\mathrm b)=0{,}2$, $F(\mathrm c)=0{,}7$.
:::

::: solution
**Khoảng chuỗi.** b cho $[0{,}2;\,0{,}7)$, rộng $0{,}5$; a cho $[0{,}2;\,0{,}3)$, rộng $0{,}1$; c cho $a_3=0{,}2+0{,}1\cdot0{,}7=0{,}27$, $w_3=0{,}03$, tức $[0{,}27;\,0{,}3)$ (CMU, trang chiếu 40).

**Chuỗi bit.** $I=-\log_20{,}03\approx5{,}06$, nên $\lambda=6+1=7$. Trung điểm $0{,}285$ nhân $2^7$ được $36{,}48$, nên $z=36/128=0{,}28125$, chuỗi `0100100`, khoảng mã $[0{,}28125;\,0{,}2890625)\subseteq[0{,}27;\,0{,}3)$. Chuỗi 6 bit `010010` có khoảng mã $[0{,}28125;\,0{,}296875)$, cũng nằm trong khoảng chuỗi; mọi chuỗi 5 bit có khoảng rộng $1/32=0{,}03125>0{,}03$ nên không nằm trong được. Chuỗi ngắn nhất có 6 bit, bằng $\lceil I\rceil$.

**Giải mã $0{,}49$.** $0{,}49\in[0{,}2;\,0{,}7)$ cho b, $\zeta\gets0{,}58$; $0{,}58$ cho b, $\zeta\gets0{,}76$; $0{,}76\in[0{,}7;\,1)$ cho c. Thông điệp là bbc (CMU, trang chiếu 44).
:::

Như vậy, chúng ta đã mã cả thông điệp bằng một khoảng có độ rộng bằng xác suất của nó (Định nghĩa 10.30, Mệnh đề 10.31), giải mã bằng phép thu hẹp ngược (Thuật toán 10.32), dừng bằng độ dài hoặc `EOS` (Mệnh đề 10.33), và chọn chuỗi bit dài dưới $I(x)+2$ (Định lý 10.34, Hệ quả 10.35). Tuy nhiên, mọi kết quả này giả thiết số học chính xác vô hạn. Trong Mục 6, chúng ta thay số thực bằng hai thanh ghi 16 bit và chứng minh rằng các bit phát ra là đúng và khoảng của mỗi ký hiệu khác rỗng.

## 6. Mã số học với thanh ghi hữu hạn

Ở BILL GATES, khoảng cuối đã cần mười chữ số thập phân (Ví dụ 10.17), và số chữ số tăng tuyến tính theo $n$. Để cài đặt bằng hai thanh ghi 16 bit và số đếm nguyên (NG, tr.100, 105–108), chúng ta cần ba điều:

- phát dần các chữ số đã chắc chắn để thanh ghi không phải dài thêm;
- xử lý khoảng co quanh điểm giữa khi chưa chữ số nào chắc chắn;
- điều kiện để phép chia nguyên không làm khoảng của một ký hiệu thành rỗng.

<!-- note-topic-id: lec-10-topic-18 -->
### 6.1 Thanh ghi và phát tiền tố chung

Mô hình số nguyên dùng số đếm $f_s\ge1$, số đếm tích lũy $G(s)=\sum_{s'<s}f_{s'}$ và tổng $N=\sum_sf_s$, nên khoảng ký hiệu của $s$ là $[G(s)/N;\,(G(s)+f_s)/N)$. Thanh ghi `high` được hiểu là theo sau bởi vô hạn bit 1, vì cận trên thật của khoảng có thể gần 1 hơn mọi số $R$ bit; do đó độ rộng là $\texttt{high}-\texttt{low}+1$ (NG, tr.100).

::: definition Định nghĩa 10.36 (Thanh ghi của bộ mã số học nguyên)
Cho số nguyên $R\ge2$, $Q=2^{R-2}$, số đếm $f_s\ge1$, $G(s)$ và $N$ như trên.

Hai **thanh ghi** (register) `low`, `high` là số nguyên trong $\{0,\ldots,2^R-1\}$ với $\texttt{low}\le\texttt{high}$; cặp thanh ghi biểu diễn khoảng nửa mở
$$
\Bigl[\frac{\texttt{low}}{2^R};\ \frac{\texttt{high}+1}{2^R}\Bigr),
$$
và $\texttt{range}=\texttt{high}-\texttt{low}+1$. Khởi tạo $\texttt{low}=0$, $\texttt{high}=2^R-1$, tức khoảng $[0;1)$.

**Thu hẹp** theo ký hiệu $s$, với `range`, `low` của trạng thái trước, là phép gán
$$
\begin{aligned}
\texttt{high}&\gets\texttt{low}-1+\Bigl\lfloor\frac{\texttt{range}\,(G(s)+f_s)}{N}\Bigr\rfloor,\\
\texttt{low}&\gets\texttt{low}+\Bigl\lfloor\frac{\texttt{range}\,G(s)}{N}\Bigr\rfloor.
\end{aligned}
$$

Trên thang thanh ghi, $2Q$ là điểm giữa và $4Q=2^R$. Gọi $[a;\,a+w)$ là khoảng thực của cặp thanh ghi và $\eta$ là một điểm trong khoảng; có ba trường hợp **chuẩn hóa** (renormalization) (NG, tr.111; CMU, trang chiếu 55):

- **nửa dưới**: $\texttt{high}<2Q$, tức $a+w\le\tfrac12$: mọi điểm của khoảng có bit đầu 0; phát 0, và khoảng được phóng to theo $\eta\mapsto2\eta$;
- **nửa trên**: $\texttt{low}\ge2Q$, tức $a\ge\tfrac12$: mọi điểm có bit đầu 1; phát 1, và $\eta\mapsto2\eta-1$;
- **khoảng giữa**: $Q\le\texttt{low}$ và $\texttt{high}<3Q$, khi không thuộc hai trường hợp trên, tức $\tfrac14\le a$, $a+w\le\tfrac34$: chưa biết bit đầu; tăng số **bit chờ** $m$ (pending bits), và $\eta\mapsto2\eta-\tfrac12$. Mỗi bit chờ được phát ngay sau bit đầu được quyết định và có giá trị ngược với bit đó.
:::

Phép thu hẹp là truy hồi của Định nghĩa 10.30 trên số nguyên: $\texttt{range}/2^R$ đóng vai $w_{t-1}$, còn $G(s)/N$ và $(G(s)+f_s)/N$ đóng vai $F(s)$ và $F(s)+p_s$; phép chia nguyên làm tròn xuống, nên khoảng nguyên chỉ xấp xỉ khoảng thực. `high` được tính trước, từ giá trị cũ của `low` (NG, tr.111).

::: example Ví dụ 10.20 (Thanh ghi năm chữ số thập phân cho BILL GATES)
**Dữ kiện.** Thanh ghi năm chữ số thập phân, khởi tạo $\texttt{high}=99999$, $\texttt{low}=00000$, với bảng khoảng ký hiệu của BILL GATES ở Ví dụ 10.17 (NG, tr.101–102); ở hệ thập phân, $\texttt{range}=\texttt{high}-\texttt{low}+1$ và khoảng ký hiệu cho bằng phần mười.

**Quy tắc phát.** Khi chữ số đầu của `high` và `low` bằng nhau, bộ mã phát chữ số đó, dịch hai thanh ghi sang trái một chữ số, đưa 9 vào cuối `high` và 0 vào cuối `low`.

**Vết.**

| Ký hiệu | `high`, `low` sau thu hẹp | phát | `high`, `low` sau dịch |
|---|---|---|---|
| B | 29999, 20000 | 2 | 99999, 00000 |
| I | 59999, 50000 | 5 | 99999, 00000 |
| L | 79999, 60000 | | |
| L | 75999, 72000 | 7 | 59999, 20000 |
| khoảng trắng | 23999, 20000 | 2 | 39999, 00000 |
| G | 19999, 16000 | 1 | 99999, 60000 |
| A | 67999, 64000 | 6 | 79999, 40000 |
| T | 79999, 76000 | 7 | 99999, 60000 |
| E | 75999, 72000 | 7 | 59999, 20000 |
| S | 55999, 52000 | 5 | 59999, 20000 |

Sau ký hiệu cuối, bộ mã phát hai chữ số đầu của `low`, là 2 và 0. Dòng bit thập phân là $0{,}25721677520$.

**Kiểm tra lại.** $0{,}2572167752$ là cận dưới của khoảng cuối ở Ví dụ 10.17. Sau phép dịch đầu, $\texttt{range}=99999-0+1=100\,000$.
:::

Một cách trực quan, khoảng chỉ co lại, nên khi `high` và `low` đã có chung chữ số đầu, mọi khoảng về sau cũng có chữ số đầu đó, và chữ số này đã thuộc kết quả (NG, tr.101). Phát nó rồi dịch là phóng to khoảng còn lại lên 10 lần, đúng như bộ giải mã của Thuật toán 10.32 phóng to sau mỗi ký hiệu.

<!-- note-topic-id: lec-10-topic-19 -->
### 6.2 Tràn dưới và bit chờ

Quy tắc phát chữ số đầu chung có thể kẹt. Chẳng hạn, ở trạng thái $\texttt{high}=70000$, $\texttt{low}=69999$ (NG, tr.102), chữ số đầu khác nhau mà khoảng chỉ còn hai giá trị, nên không ký hiệu nào còn khoảng con. Hiện tượng khoảng co quanh một điểm ranh giới như vậy gọi là tràn dưới (underflow).

Với $\texttt{high}=40344$, $\texttt{low}=39810$, khoảng rộng 535 đơn vị nhưng chữ số đầu là 4 và 3. Bộ mã xóa chữ số thứ hai của cả hai thanh ghi, dịch phần còn lại sang trái và tăng một bộ đếm: $40344\to43449$, $39810\to38100$, bộ đếm bằng 1. Khi chữ số đầu cuối cùng được quyết định, các chữ số bị xóa được phát sau nó: 9 nếu chữ số đầu là 3, 0 nếu chữ số đầu là 4 (NG, tr.102–103).

Trên hệ nhị phân, trường hợp khoảng giữa của Định nghĩa 10.36 ứng với phép xóa chữ số thứ hai này: bộ mã chưa biết bit đầu, nên tăng số bit chờ $m$, rồi phát $m$ bit chờ, mỗi bit ngược với bit đầu, ngay sau bit đầu được quyết định.

::: algorithm Thuật toán 10.37 (Mã hóa một ký hiệu với chuẩn hóa)
**Đầu vào.** Trạng thái `low`, `high`, $m$; ký hiệu $s$ với $G(s)$, $f_s$.

**Giả thiết.** $f_s\ge1$ và $N\le Q=2^{R-2}$; trước ký hiệu đầu, $\texttt{low}=0$, $\texttt{high}=2^R-1$ (Định nghĩa 10.36) và $m=0$.

**Đầu ra.** Trạng thái mới và các bit được phát.

**Các bước.**

1. Thu hẹp theo $s$ như Định nghĩa 10.36.
2. Lặp:
   1. nếu $\texttt{high}<2Q$: phát 0 rồi $m$ bit 1, đặt $m\gets0$;
   2. nếu không, và $\texttt{low}\ge2Q$: phát 1 rồi $m$ bit 0, đặt $m\gets0$, rồi trừ $2Q$ khỏi cả hai thanh ghi;
   3. nếu không, và $\texttt{low}\ge Q$, $\texttt{high}<3Q$: đặt $m\gets m+1$ và trừ $Q$ khỏi cả hai thanh ghi;
   4. nếu không trường hợp nào thỏa: dừng vòng lặp;

   sau mỗi trường hợp 1–3: $\texttt{low}\gets2\,\texttt{low}$, $\texttt{high}\gets2\,\texttt{high}+1$.

**Dừng.** Mỗi lần lặp nhân `range` lên 2, mà `range` không vượt $2^R$, nên vòng lặp dừng; khi dừng, $\texttt{low}<2Q\le\texttt{high}$ và $\texttt{low}<Q$ hoặc $\texttt{high}\ge3Q$.

**Trường hợp biên.** $m$ có thể tăng qua nhiều ký hiệu liên tiếp và chỉ về 0 khi một bit được phát; $m$ là một bộ đếm chung cho cả thông điệp.

**Chi phí.** Hai phép nhân, hai phép chia nguyên trên số $2R$ bit, cộng một lần lặp cho mỗi bit được phát hoặc được đưa vào $m$.
:::

```text
ENCODE-SYMBOL(s):
    range ← high − low + 1
    high ← low + ⌊range·(G[s] + f[s]) / N⌋ − 1
    low  ← low + ⌊range·G[s] / N⌋
    lặp:
        nếu high < 2Q:                      OUTPUT(0); OUTPUT(1 lặp m lần); m ← 0
        ngược lại nếu low ≥ 2Q:             OUTPUT(1); OUTPUT(0 lặp m lần); m ← 0
                                            low ← low − 2Q; high ← high − 2Q
        ngược lại nếu low ≥ Q và high < 3Q: m ← m + 1; low ← low − Q; high ← high − Q
        ngược lại: thoát vòng lặp
        low ← 2·low; high ← 2·high + 1
```

Phép quyết định của thuật toán là so hai thanh ghi với ba ngưỡng $Q$, $2Q$, $3Q$. Trừ $2Q$ hoặc $Q$ rồi nhân đôi chính là các phép $\eta\mapsto2\eta-1$ và $\eta\mapsto2\eta-\tfrac12$ trên thang thực.

![Ba trục số từ 0 tới 1 có vạch ở 1/4, 1/2, 3/4. Nửa dưới: khoảng hiện thời trong đoạn từ 0 tới 1/2, phát 0 rồi m bit 1, η ↦ 2η. Nửa trên: khoảng trong đoạn từ 1/2 tới 1, phát 1 rồi m bit 0, η ↦ 2η − 1. Khoảng giữa: khoảng trong đoạn từ 1/4 tới 3/4 và chứa 1/2, m ← m + 1, η ↦ 2η − 1/2.](img/lec-10/note-ba-nhanh-chuan-hoa.svg)

Trên hình, ba trường hợp đặt trên cùng một thang: ở hai trục đầu, khoảng nằm hẳn về một phía của $\tfrac12$ nên bit đầu đã biết; ở trục thứ ba, khoảng chứa $\tfrac12$ nhưng nằm trong $[\tfrac14;\,\tfrac34)$, nên chỉ biết rằng hai bit đầu khác nhau. Chúng ta chạy thuật toán với $R=16$ trên một mô hình ba ký hiệu (CMU-A1, bài 3).

::: example Ví dụ 10.21 (Vết 16 bit cho "cbb")
**Dữ kiện.** $R=16$, $Q=16\,384$. Số đếm $f_{\mathrm a}=1$, $f_{\mathrm b}=2$, $f_{\mathrm c}=7$, thứ tự a, b, c, nên $G(\mathrm a)=0$, $G(\mathrm b)=1$, $G(\mathrm c)=3$, $N=10$, tức $p=(0{,}1;\,0{,}2;\,0{,}7)$. Thông điệp cbb, bộ giải mã biết $n=3$.

**Khoảng thực.** Theo Định nghĩa 10.30, c cho $[0{,}3;\,1)$, b cho $[0{,}37;\,0{,}51)$, b cho $[0{,}384;\,0{,}412)$.

**Vết.** Mỗi dòng ghi hai thanh ghi trước thao tác của dòng đó; "thu hẹp" là kết quả bước 1, các dòng sau là các lần lặp của bước 2.

| Bước | `low` | `high` | thao tác | phát | $m$ |
|---|---|---|---|---|---|
| c: thu hẹp | `0100110011001100` ($19\,660$) | `1111111111111111` ($65\,535$) | dừng | | 0 |
| b: thu hẹp | `0101111010110111` ($24\,247$) | `1000001010001101` ($33\,421$) | khoảng giữa | | 1 |
| | `0011110101101110` | `1000010100011011` | dừng | | 1 |
| b: thu hẹp | `0100010010011001` ($17\,561$) | `0101001011101110` ($21\,230$) | nửa dưới | `01` | 0 |
| | `1000100100110010` | `1010010111011101` | nửa trên | `1` | 0 |
| | `0001001001100100` | `0100101110111011` | nửa dưới | `0` | 0 |
| | `0010010011001000` | `1001011101110111` | dừng | | 0 |

Để kết thúc, bộ mã phát bit thứ hai của `low` rồi $m+1$ bit ngược với nó (NG, tr.113): bit thứ hai của `low` là 0 và $m=0$, nên bộ mã phát `0` rồi một bit `1`, tức `01`.

**Kết quả.** Dòng bit `011001`, 6 bit chưa kể 16 bit 0 đệm, biểu diễn $0{,}390625$.

**Kiểm tra lại.** $0{,}384\le0{,}390625<0{,}412$. Ở ký hiệu b thứ nhất, khoảng co quanh điểm giữa nên một bit bị đưa vào $m$; ký hiệu b thứ hai đưa khoảng vào nửa dưới, nên bit `0` được phát cùng bit chờ `1`.
:::

Các bit được phát luôn đúng và khoảng không bao giờ rỗng; chúng ta chứng minh hai điều đó.

::: lemma Bổ đề 10.38 (Bit phát ra và bit chờ là đúng)
**Giả thiết.** Tại một thời điểm có $m=0$, khoảng thực của hai thanh ghi là $\mathcal I_0\subseteq[0;1)$. Sau đó Thuật toán 10.37 thực hiện các phép thu hẹp xen với đúng $m'\ge0$ lần trường hợp khoảng giữa, rồi một lần trường hợp nửa dưới hoặc nửa trên; $\mathcal I_1$ là khoảng thực của hai thanh ghi ngay trước lần đó. Đặt
$$
\psi(\eta)=2^{m'}\bigl(\eta-\tfrac12\bigr)+\tfrac12 .
$$

**Kết luận.** $\psi^{-1}(\mathcal I_1)\subseteq\mathcal I_0$. Nếu lần cuối là nửa dưới, mọi điểm của $\psi^{-1}(\mathcal I_1)$ có khai triển nhị phân bắt đầu bằng $0\,1^{m'}$; nếu là nửa trên, bằng $1\,0^{m'}$. Đó đúng là các bit thuật toán phát.

**Điều kiện áp dụng.** Khoảng là nửa mở; khai triển nhị phân được chọn không kết thúc bằng dãy 1 vô hạn.

**Phạm vi.** $\psi^{-1}(\mathcal I_1)$ là khoảng hiện thời viết trên thang của thanh ghi tại thời điểm $m=0$; các điểm khác của $\mathcal I_0$ có thể bắt đầu bằng bit khác. Áp dụng lặp lại, mọi bit đã phát là tiền tố chung của mọi điểm trong khoảng nguyên hiện thời và mọi khoảng về sau, viết trên thang ban đầu.
:::

::: proof
**Bước 1 (thu hẹp và phép giữa).** Phép thu hẹp cho khoảng con của khoảng hiện thời, vì `low` mới không nhỏ hơn `low` cũ và `high` mới không lớn hơn `high` cũ, do $0\le G(s)$ và $G(s)+f_s\le N$. Phép giữa $\eta\mapsto2\eta-\tfrac12$ giữ điểm $\tfrac12$ và nhân khoảng cách tới $\tfrac12$ lên 2, nên hợp của $j$ phép giữa là $\psi_j(\eta)=2^{j}(\eta-\tfrac12)+\tfrac12$, một ánh xạ tăng. Quy nạp theo số thao tác: sau $j$ phép giữa và các phép thu hẹp xen giữa, khoảng hiện thời là $\psi_j(\mathcal I)$ với $\mathcal I\subseteq\mathcal I_0$, vì một phép thu hẹp trên thang hiện thời ứng qua $\psi_j^{-1}$ với một phép lấy khoảng con trên thang của $\mathcal I_0$. Với $j=m'$ ta được $\mathcal I_1=\psi(\mathcal I)$, tức $\psi^{-1}(\mathcal I_1)=\mathcal I\subseteq\mathcal I_0$.

**Bước 2 (nửa dưới).** Nếu lần cuối là nửa dưới thì $\mathcal I_1\subseteq[0;\tfrac12)$. Với $\eta\in\psi^{-1}(\mathcal I_1)$, $0\le\psi(\eta)<\tfrac12$ cho
$$
\tfrac12-2^{-(m'+1)}\le\eta<\tfrac12 .
$$
Đoạn này là khoảng mã của chuỗi $0\,1^{m'}$, vì $z(0\,1^{m'})=\sum_{i=2}^{m'+1}2^{-i}=\tfrac12-2^{-(m'+1)}$ và độ rộng là $2^{-(m'+1)}$. Theo Định nghĩa 10.7, mọi điểm của $\psi^{-1}(\mathcal I_1)$ có khai triển bắt đầu bằng $0\,1^{m'}$.

**Bước 3 (nửa trên).** Tương tự, $\mathcal I_1\subseteq[\tfrac12;1)$ cho $\tfrac12\le\eta<\tfrac12+2^{-(m'+1)}$, khoảng mã của $1\,0^{m'}$.

**Bước 4 (các bit phát).** Ở trường hợp nửa dưới, thuật toán phát 0 rồi $m'$ bit 1; ở nửa trên, 1 rồi $m'$ bit 0. Đó đúng là $0\,1^{m'}$ và $1\,0^{m'}$. Sau phép phóng to cuối, khoảng mới là ảnh của $\psi^{-1}(\mathcal I_1)$ qua phép biến đổi bỏ $m'+1$ bit đầu, $m$ trở về 0, nên lập luận lặp lại cho các bit tiếp theo. $\square$
:::

Ở Ví dụ 10.21, sau ký hiệu c có $m=0$ và chưa bit nào được phát, nên $\mathcal I_0=[19\,660/2^{16};\,1)\approx[0{,}29999;\,1)$. Ký hiệu b thứ nhất cho một lần khoảng giữa, $m'=1$; sau ký hiệu b thứ hai, $\mathcal I_1=[17\,561/2^{16};\,21\,231/2^{16})\approx[0{,}26796;\,0{,}32396)$ nằm trong nửa dưới. Kéo về thang ban đầu, $\psi^{-1}(\mathcal I_1)\approx[0{,}38398;\,0{,}41198)$, gần đúng khoảng thực $[0{,}384;\,0{,}412)$ của cbb và nằm trong khoảng mã $[0{,}25;\,0{,}5)$ của `01`, đúng hai bit được phát. Điểm $0{,}9\in\mathcal I_0$ bắt đầu bằng bit 1, nên kết luận không đúng cho cả $\mathcal I_0$.

::: lemma Bổ đề 10.39 (Khoảng con nguyên không rỗng)
**Giả thiết.** $R\ge2$, $Q=2^{R-2}$; số đếm $f_s\ge1$ với mọi $s$ và $N\le Q$. Trạng thái `low`, `high` là trạng thái khởi tạo hoặc trạng thái khi vòng lặp chuẩn hóa của Thuật toán 10.37 dừng.

**Kết luận.** $\texttt{range}\ge Q+2$, và với mọi ký hiệu $s$, phép thu hẹp cho $\texttt{low}\le\texttt{high}$, tức khoảng nguyên của $s$ khác rỗng, và khoảng mới nằm trong khoảng cũ.

**Điều kiện áp dụng.** Cần cả $f_s\ge1$ lẫn $N\le Q$. Với $R=16$, điều kiện $N<2^{14}=16\,384$ (NG, tr.108; CMU, trang chiếu 53) kéo theo $N\le Q$.

**Phạm vi.** Bổ đề chỉ bảo đảm khoảng khác rỗng; khoảng nguyên vẫn hẹp hơn khoảng thực một chút do làm tròn.
:::

::: proof
**Bước 1 (độ rộng sau chuẩn hóa).** Ở trạng thái khởi tạo, $\texttt{range}=2^R=4Q$. Khi vòng lặp dừng, không trường hợp nào thỏa, nên $\texttt{low}<2Q\le\texttt{high}$, và $\texttt{low}<Q$ hoặc $\texttt{high}\ge3Q$. Có hai trường hợp:

- $\texttt{low}\le Q-1$: khi đó $\texttt{range}\ge2Q-(Q-1)+1=Q+2$;
- $\texttt{high}\ge3Q$: khi đó $\texttt{range}\ge3Q-(2Q-1)+1=Q+2$.

**Bước 2 (khoảng con khác rỗng).** Đặt $\alpha=\texttt{range}\,(G(s)+f_s)/N$ và $\beta=\texttt{range}\,G(s)/N$. Phép thu hẹp cho $\texttt{high}-\texttt{low}=\lfloor\alpha\rfloor-\lfloor\beta\rfloor-1$ với các giá trị mới. Theo $\lfloor\alpha\rfloor-\lfloor\beta\rfloor\ge\lfloor\alpha-\beta\rfloor$,
$$
\begin{aligned}
\lfloor\alpha\rfloor-\lfloor\beta\rfloor&\ge\Bigl\lfloor\frac{\texttt{range}\,f_s}{N}\Bigr\rfloor\\
&\ge\Bigl\lfloor\frac{Q+2}{Q}\Bigr\rfloor\ge1,
\end{aligned}
$$
vì $f_s\ge1$, $N\le Q$ và Bước 1. Do đó $\texttt{high}\ge\texttt{low}$.

**Bước 3 (nằm trong khoảng cũ).** $\beta\ge0$ cho `low` mới không nhỏ hơn `low` cũ. Vì $G(s)+f_s\le N$, $\lfloor\alpha\rfloor\le\texttt{range}$, nên `high` mới không lớn hơn $\texttt{low}+\texttt{range}-1$, là `high` cũ. $\square$
:::

Bổ đề cần cả hai điều kiện:

- Bỏ "$f_s\ge1$": một ký hiệu có $f_s=0$ có khoảng rỗng ngay từ mô hình, nên không mã được.
- Bỏ "$N\le Q$": với $R=16$, trạng thái $\texttt{low}=16\,383$, $\texttt{high}=32\,768$ là trạng thái dừng hợp lệ với $\texttt{range}=16\,386$; nếu $N=20\,000$ và $f_s=1$, $G(s)=0$, thì $\lfloor16\,386/20\,000\rfloor=0$, nên `high` mới bằng $\texttt{low}-1$ và khoảng rỗng.

Bước 2 dùng cả hai giả thiết; Bước 1 dùng điều kiện dừng của vòng lặp.

**Trong thực hành.** Để có $N<16\,384$, bộ nén chia mọi số đếm để vừa một byte, đặt về 1 những số đếm khác 0 bị chia thành 0, rồi nếu tổng còn lớn thì chia tiếp cho 2 hoặc 4 (NG, tr.108–109). Sau lần chia thứ hai, bước đặt về 1 phải được lặp lại; nếu không, một số đếm 1 thành 0 và vi phạm giả thiết $f_s\ge1$ của Bổ đề 10.39. Số đếm được truyền trong đầu mục như bảng số đếm của Huffman tĩnh.

::: exercise Bài tập 10.7 (Bảng số đếm tích lũy)
Mô hình số nguyên có số đếm A: 5, B: 2, C: 3, D: 3, E: 8 (NG, tr.107). Lập bảng $G(s)$ và $N$, kiểm điều kiện $N\le Q$ với $R=16$. Với trạng thái khởi tạo $\texttt{low}=0$, $\texttt{high}=65\,535$, bộ giải mã tính $\texttt{count}=\lfloor((\texttt{code}-\texttt{low}+1)N-1)/\texttt{range}\rfloor$ và chọn ký hiệu có $G(s)\le\texttt{count}<G(s)+f_s$ (NG, tr.113–114). Tìm ký hiệu khi $\texttt{code}=24\,576$ và khi $\texttt{code}=40\,960$.
:::

::: hint
$\texttt{range}=65\,536$ ở trạng thái khởi tạo.
:::

::: solution
$G(\mathrm A)=0$, $G(\mathrm B)=5$, $G(\mathrm C)=7$, $G(\mathrm D)=10$, $G(\mathrm E)=13$ và $N=21\le Q=16\,384$.

Với $\texttt{code}=24\,576$: $\lfloor(24\,577\cdot21-1)/65\,536\rfloor=\lfloor516\,116/65\,536\rfloor=7$, và $G(\mathrm C)=7\le7<10$, nên ký hiệu là C. Với $\texttt{code}=40\,960$: $\lfloor(40\,961\cdot21-1)/65\,536\rfloor=\lfloor860\,180/65\,536\rfloor=13$, nên ký hiệu là E.

**Kiểm tra lại.** $24\,576/65\,536=0{,}375\in[7/21;\,10/21)\approx[0{,}333;\,0{,}476)$ và $40\,960/65\,536=0{,}625\in[13/21;\,1)\approx[0{,}619;\,1)$.
:::

<!-- note-topic-id: lec-10-topic-20 -->
### 6.3 Giải mã nguyên và kết thúc dòng

Bộ giải mã giữ cùng `low`, `high` như bộ mã và thêm thanh ghi `code` chứa $R$ bit tiếp theo của dòng bit. Trên dòng `011001` của Ví dụ 10.21, đệm thêm bit 0, thanh ghi đầu là $\texttt{code}=$ `0110010000000000` $=25\,600$. Ký hiệu đầu: $\texttt{range}=65\,536$, $\texttt{count}=\lfloor(25\,601\cdot10-1)/65\,536\rfloor=3$, và $G(\mathrm c)=3\le3<10$, nên ký hiệu là c. Bộ giải mã thu hẹp như bộ mã, được $\texttt{low}=19\,660$, $\texttt{range}=45\,876$, không cần dịch; ký hiệu thứ hai có $\texttt{count}=\lfloor(5\,941\cdot10-1)/45\,876\rfloor=1$, và $G(\mathrm b)=1\le1<3$, tức b.

::: algorithm Thuật toán 10.40 (Giải mã nguyên và kết thúc dòng)
**Đầu vào.** Dòng bit do bộ mã phát, gồm cả phần kết thúc; mô hình $f_s$, $G(s)$, $N$ như bộ mã.

**Giả thiết.** Như Thuật toán 10.37: $f_s\ge1$, $N\le Q$; hai phía dùng cùng $R$, cùng thứ tự ký hiệu và cùng công thức làm tròn; `EOS` là một ký hiệu của mô hình.

**Đầu ra.** Thông điệp, dừng khi giải ra `EOS`.

**Kết thúc ở bộ mã.** Sau khi mã `EOS`, bộ mã phát bit thứ hai của `low` rồi $m+1$ bit ngược với nó, tức 2 bit cộng các bit chờ (NG, tr.113); sau đó phát 16 bit 0, vì bộ giải mã luôn đọc trước 16 bit (NG, tr.105–106).

**Các bước của bộ giải mã.**

1. Khởi tạo: $\texttt{low}=0$, $\texttt{high}=2^R-1$, và nạp $R$ bit đầu vào `code`.
2. Lặp: tính $\texttt{range}$ và $\texttt{count}=\lfloor((\texttt{code}-\texttt{low}+1)N-1)/\texttt{range}\rfloor$; tìm $s$ với $G(s)\le\texttt{count}<G(s)+f_s$; nếu $s$ là `EOS`, dừng; phát $s$.
3. Thu hẹp `low`, `high` theo $s$ như bộ mã, rồi chạy cùng vòng lặp chuẩn hóa; ở mỗi lần lặp, `code` chịu cùng phép trừ và nhân đôi như hai thanh ghi rồi nhận thêm một bit vào cuối.

**Dừng.** Khi giải ra `EOS`; nếu dùng độ dài $n$ truyền kèm, sau $n$ ký hiệu.

**Trường hợp biên.** Bộ giải mã không đọc quá cuối tệp: 16 bit 0 bộ mã đã phát đủ cho các lần đọc trước (NG, tr.106).

**Chi phí.** Mỗi ký hiệu: $O(1)$ phép số học trên số $2R$ bit, một lần tìm ký hiệu, $O(k)$ với phép quét tuyến tính trong bảng số đếm tích lũy (NG, tr.114), và một lần lặp cho mỗi bit đọc vào.
:::

Hai bit kết thúc chọn một điểm trong khoảng hiện thời: nếu bit thứ hai của `low` là 0 thì $\texttt{low}<Q$, và điểm $\tfrac14$, ứng với `01`, nằm trong khoảng vì $\texttt{high}\ge2Q$; nếu là 1 thì $\texttt{high}\ge3Q$ và điểm $\tfrac12$, ứng với `10`, nằm trong khoảng. Quy tắc này phát một điểm và dựa vào 16 bit 0 đệm phía sau, khác Định lý 10.34, nơi chuỗi bit có khoảng mã nằm trọn trong khoảng chuỗi.

::: proposition Mệnh đề 10.41 (Bộ giải mã nguyên đồng bộ với bộ mã)
**Giả thiết.** Bộ mã chạy Thuật toán 10.37 cho mọi ký hiệu rồi kết thúc như Thuật toán 10.40; bộ giải mã chạy Thuật toán 10.40 với cùng mô hình; giả thiết của Bổ đề 10.39 thỏa.

**Kết luận.** Trước mỗi ký hiệu, hai phía có cùng `low`, `high`, và bộ giải mã chọn đúng ký hiệu mà bộ mã đã mã.

**Điều kiện áp dụng.** Cùng $R$, cùng $N$, cùng thứ tự ký hiệu, cùng công thức làm tròn ở hai phía.

**Phạm vi.** Mệnh đề giả thiết kênh truyền không lỗi và hai phía dùng cùng mô hình trước mỗi ký hiệu. Chứng minh đầy đủ nằm ngoài phạm vi học phần (Witten, Neal và Cleary, 1987).
:::

::: proof
Phác thảo. Bộ giải mã thực hiện đúng các phép thu hẹp và chuẩn hóa của bộ mã, trên cùng số nguyên, nên nếu nó chọn đúng ký hiệu thì hai phía có cùng `low`, `high` ở bước sau. Để nó chọn đúng, cần chứng minh `code`, cùng các bit đọc tiếp theo, biểu diễn một điểm thuộc khoảng con nguyên của ký hiệu đang mã; điều này dùng Bổ đề 10.38 cho các bit đã phát và một phân tích phép chia nguyên trong công thức `count`, gồm tính đơn điệu của phép làm tròn (Witten, Neal và Cleary, 1987). $\square$
:::

Bỏ giả thiết của Bổ đề 10.39 thì kết luận sai: ở phản ví dụ $N=20\,000$ sau bổ đề đó, khoảng con của ký hiệu rỗng, nên bộ mã không mã được ký hiệu đó.

**Chi phí.** Mô hình đếm phép số học trên từ $2R$ bit, mỗi phép $O(1)$, trong trường hợp xấu nhất, với $n$ ký hiệu, $k$ ký hiệu trong bảng chữ cái và $\lambda$ bit phát ra.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| đếm, co số đếm, lập bảng $G$ (lượt đọc thứ nhất) | $n$ và $k$ | $O(1)$ | $O(n+k)$ |
| thu hẹp khi mã hóa hoặc giải mã | $n$ | $O(1)$ | $O(n)$ |
| lặp chuẩn hóa | mỗi bit phát, mỗi bit chờ | $O(1)$ | $O(\lambda)$ |
| tìm ký hiệu khi giải mã, quét bảng $G$ (NG, tr.114) | $n$ | $O(k)$ | $O(nk)$ |
| đầu mục số đếm | 1 | $k$ số đếm | $O(k)$ |

Bộ nhớ gồm bảng $G$ với $k+1$ số và ba thanh ghi, tức $O(k)$; như Huffman tĩnh, bộ mã đọc dữ liệu hai lần.

**Trong thực hành.** So với cận $\lambda<I(x)+2$ của Định lý 10.34, bộ mã của Thuật toán 10.37 và 10.40 có thêm bốn khoản cố định và tổn thất do làm tròn ở mỗi ký hiệu (EE398A-3, trang chiếu 13–14):

- ký hiệu `EOS` với số đếm 1 tốn khoảng $\log_2N$ bit, tới 14 bit;
- quy tắc kết thúc thêm 2 bit, cùng $m$ bit chờ còn lại (NG, tr.113, 122);
- 16 bit 0 đệm làm tệp dài thêm 2 byte (NG, tr.105–106);
- đầu mục số đếm như Huffman tĩnh.

Như vậy, chúng ta đã có bộ mã số học với thanh ghi $R$ bit (Định nghĩa 10.36, Thuật toán 10.37) mà các bit phát ra là đúng (Bổ đề 10.38) và mọi ký hiệu luôn có khoảng con khác rỗng khi $f_s\ge1$, $N\le2^{R-2}$ (Bổ đề 10.39), cùng bộ giải mã và quy tắc kết thúc (Thuật toán 10.40, Mệnh đề 10.41). Tuy nhiên, chưa có tiêu chí để chọn một trong ba bộ nén cho một tệp cụ thể. Trong Mục 7, chúng ta đặt chúng cạnh nhau trên cùng các thông điệp.

<!-- note-topic-id: lec-10-topic-21 -->
## 7. Chọn cặp mô hình–bộ mã

Một kho văn bản nén bằng Huffman tĩnh bậc 1 phải gửi bảng số đếm $65\,536$ byte, so với 256 byte ở bậc 0 (NG, tr.24), nên bậc 1 chỉ có lợi trên tệp đủ lớn. Để chọn một bộ nén cho một tệp cụ thể, chúng ta đặt các kết quả cạnh nhau với $n$ là độ dài thông điệp và $k$ là cỡ bảng chữ cái.

| Cặp | Đầu vào | Bảo đảm | Chi phí |
|---|---|---|---|
| tĩnh + Huffman (Thuật toán 10.14) | hai lượt đọc; số đếm gửi trong đầu mục | mã tiền tố tối ưu cho số đếm đã gửi; $I(x)\le$ thân $<I(x)+n$ khi số đếm gửi là số đếm thật (Hệ quả 10.19) | $O(n+k\log k)$ cộng số bit; đầu mục khoảng 256 byte ở bậc 0 |
| thích nghi + Huffman (Thuật toán 10.26) | một lượt; không đầu mục | sau mỗi ký hiệu, cây tối ưu cho trọng số hiện thời (Định lý 10.25); hai phía đồng bộ (Mệnh đề 10.27) | mỗi ký hiệu một lần đi cây và một lần cập nhật; thêm `ESCAPE` và 8 bit cho ký hiệu mới; khởi đầu nguội |
| tĩnh + Huffman trên khối $j$ ký hiệu | bảng chữ cái $k^j$ phần tử | $H\le\bar\ell/j<H+1/j$ bit mỗi ký hiệu (EE398A-1, trang chiếu 21) | bảng mã và đầu mục tăng theo $k^j$ |
| tĩnh + số học (Thuật toán 10.37, 10.40) | hai lượt đọc; số đếm gửi trong đầu mục | lý tưởng: ít hơn $I(x)+2$ bit (Định lý 10.34); nguyên: đúng khi $f_s\ge1$, $N\le2^{R-2}$ (Bổ đề 10.39), cộng các khoản cố định của Mục 6.3 | $O(1)$ phép nhân, chia mỗi ký hiệu, cộng tìm ký hiệu $O(k)$ khi giải mã |

Trên thông điệp A–E, số bit là 312 với ASCII, 117 với mã độ dài cố định, 102 với độ dài Shannon, 89 với Shannon–Fano, 87 với Huffman và $\lambda=\lceil85{,}247\rceil+1=87$ với mã số học lý tưởng cùng mô hình, so với đích $I(x)\approx85{,}25$ bit. Năm tiêu chí, kèm số liệu:

- xác suất gần 1: mọi mã ký hiệu dùng ít nhất 1 bit mỗi ký hiệu, còn mã số học dùng gần $I(x)$ bit: 6 bit thay cho 8 bit ở Ví dụ 10.19 (chuỗi ngắn nhất 5 bit);
- thông điệp ngắn: khoản 2 bit của Định lý 10.34 chưa được bù lại; trên BILL GATES, cây Huffman của tám số đếm 1 và số đếm 2 của L có các nút trong trọng số $2,2,2,2,4,4,6,10$, nên tốn 32 bit (chi phí bằng tổng trọng số nút trong, áp dụng lặp Bổ đề 10.17), còn quy tắc của Định lý 10.34 dùng $\lceil31{,}22\rceil+1=33$ bit;
- phân phối có mọi xác suất là lũy thừa của $\tfrac12$: mã Huffman đạt đúng entropy (Định lý 10.12, 10.13, 10.18);
- một lượt đọc hoặc đầu mục lớn so với thân: mô hình thích nghi bỏ đầu mục, đổi lại khởi đầu nguội và chi phí `ESCAPE` (Mục 4.3);
- tốc độ: mã số học chậm hơn đáng kể, còn Huffman bậc 0 nhỏ và nhanh (NG, tr.23, 66); khi thu hẹp khoảng, mỗi ký hiệu tốn hai phép nhân và hai phép chia nguyên (Thuật toán 10.37).

::: exercise Bài tập 10.8 (Chọn mô hình theo cỡ tệp)
Một bộ nén tĩnh bậc 1 gửi bảng số đếm $65\,536$ byte, bộ nén tĩnh bậc 0 gửi 256 byte (NG, tr.24). Trên một tệp, thân dòng bit của bộ nén bậc 1 ngắn hơn của bộ nén bậc 0 là $\delta$ byte. Tìm điều kiện của $\delta$ để bộ nén bậc 1 cho tệp nén ngắn hơn. Với $\delta$ bằng 5% thân của bộ nén bậc 0, tính độ dài tối thiểu của thân đó. Chỉ ra bộ nén của chương không cần điều kiện này.
:::

::: hint
Tổng độ dài là đầu mục cộng thân.
:::

::: solution
Bộ nén bậc 1 ngắn hơn khi $65\,536+(L_0-\delta)<256+L_0$, với $L_0$ là thân của bộ nén bậc 0, tức $\delta>65\,280$ byte. Nếu $\delta=0{,}05L_0$ thì cần $L_0>65\,280/0{,}05=1\,305\,600$ byte, khoảng 1,3 MB. Mô hình thích nghi (Thuật toán 10.26) không gửi bảng số đếm, nên không có điều kiện này. Do đó, với mô hình bậc cao, mô hình thích nghi được dùng (NG, tr.67).
:::

Như vậy, việc chọn bộ nén phụ thuộc phân phối, số lượt đọc được phép và cỡ đầu mục: Hệ quả 10.19 và Định lý 10.34 chặn phần thân, còn Bài tập 10.8 cho điều kiện về đầu mục. Tuy nhiên, cả ba bộ nén vẫn mã từng ký hiệu theo một mô hình đếm; Bài 11 khai thác các chuỗi lặp lại bằng từ điển.

<!-- note-topic-id: lec-10-topic-22 -->
## Tình huống áp dụng và ứng dụng

- Tình huống 10.1: dữ liệu thỏa giả thiết của Định lý 10.18 và Định lý 10.25.
- Tình huống 10.2: nguồn độc lập thỏa giả thiết của Hệ quả 10.35; ảnh fax thật vi phạm giả thiết độc lập của hệ quả đó.
- Tình huống 10.3: bảng mã dựng từ dữ liệu khác vi phạm giả thiết về số đếm của Định lý 10.18; bộ giải mã bỏ phép đổi vi phạm giả thiết đồng bộ của Mệnh đề 10.27.

::: application Tình huống 10.1 (Đầu mục của mô hình bậc 0 và bậc 1)
**Bài toán và dữ liệu.** Một kho văn bản được nén bằng mã Huffman tĩnh. Đầu mục là bảng số đếm 256 byte với mô hình bậc 0 và $65\,536$ byte với mô hình bậc 1 (NG, tr.24). Thân của bậc 1 ngắn hơn thân $L_0$ của bậc 0 là $\delta=0{,}05L_0$ byte.

**Mô hình hóa và kiểm giả thiết.** Tổng độ dài bằng đầu mục cộng thân $\operatorname{cost}(T)$. Định lý 10.18 áp dụng cho thân với số đếm đã gửi, mọi số đếm dương, nhưng không nói gì về đầu mục.

**Áp dụng và chi phí.** Theo Bài tập 10.8, bậc 1 cho tệp ngắn hơn khi và chỉ khi $L_0>1\,305\,600$ byte, khoảng 1,3 MB; kho nhỏ hơn dùng bậc 0. Bộ nén tĩnh đọc tệp hai lần.

**Diễn giải và giới hạn.** Với tệp nhỏ hoặc dòng chỉ đọc được một lần, Thuật toán 10.26 không cần đầu mục và chạy một lượt; theo Định lý 10.25, cây tối ưu cho trọng số hiện thời của nó, tức số đếm đã đọc sau các lần co. Đổi lại, mô hình thích nghi chỉ cho tỷ lệ nén khá sau vài nghìn byte (NG, tr.25), so với đầu mục 256 byte của mã tĩnh bậc 0.

**Dẫn ngược lý thuyết.** Định nghĩa 10.3, Thuật toán 10.14, Định lý 10.18, Nhận xét 10.20, Định lý 10.25, Thuật toán 10.26, 10.29, Bài tập 10.8.
:::

::: application Tình huống 10.2 (Nguồn nhị phân lệch)
**Bài toán và dữ liệu.** Ảnh hai màu của máy fax có bảng chữ cái hai ký hiệu (NG, tr.96). Giả sử một mô hình tĩnh gán cho điểm trắng xác suất $0{,}9$.

**Mô hình hóa.** Mỗi điểm ảnh là một ký hiệu; $H(P)=-0{,}9\log_20{,}9-0{,}1\log_20{,}1\approx0{,}469$ bit.

**Kiểm giả thiết.** Với mã Huffman, Hệ quả 10.19 cho $0{,}469\le\bar\ell<1{,}469$, nhưng mã Huffman trên hai ký hiệu có $\bar\ell=1$. Với mã số học, Định lý 10.34 cần số học chính xác, được thay bằng Thuật toán 10.37 với số đếm thỏa Bổ đề 10.39.

**Áp dụng.** Trên thông điệp bảy chữ A và END của Ví dụ 10.19, mã Huffman dùng 8 bit, mã số học 5 bit với quy tắc ngắn nhất và 6 bit với quy tắc của Định lý 10.34. Một thí nghiệm với $100\,000$ số 0, xác suất $16\,382/16\,383$, cho tệp nén dài 3 byte, so với ít nhất $100\,001$ bit, tức $12\,501$ byte, của mã Huffman (NG, tr.104). Tự thông tin gồm khoảng $8{,}81$ bit của $100\,000$ số 0 và khoảng $14{,}00$ bit của `EOS`, tổng $22{,}81$ bit; cận dưới $I(x)$ này không vượt quá 3 byte.

**Diễn giải và giới hạn.** Theo Hệ quả 10.35, với $n$ điểm ảnh độc lập, mã số học lý tưởng tốn kỳ vọng dưới $0{,}469n+2$ bit, mã Huffman $n$ bit; bộ mã thanh ghi 16 bit thêm các khoản cố định của Mục 6.3. Ảnh fax thật có các điểm đi thành loạt nên không độc lập, trái giả thiết của Hệ quả 10.35; gom các bit thành gói rồi mã Huffman các gói là một cách khác (NG, tr.96).

**Dẫn ngược lý thuyết.** Định nghĩa 10.11, Hệ quả 10.19, Định lý 10.34, Hệ quả 10.35, Thuật toán 10.37, Bổ đề 10.39.
:::

::: application Tình huống 10.3 (Mô hình không khớp dữ liệu và hai phía khác thủ tục)
**(a) Bảng mã dùng chung không khớp tệp.** Một bảng mã Huffman mẫu cho văn bản (NG, tr.22) có E = `100` dài 3 bit còn Q = `01101110001` và Z = `01101110000` dài 11 bit. Dùng bảng này làm mô hình tĩnh dùng chung cho một tệp chỉ gồm các chữ Q và Z, mỗi ký tự tốn 11 bit so với 8 bit ASCII, tức dài thêm $3/8=37{,}5\%$.

**Kiểm giả thiết (a).** Định lý 10.18 và Hệ quả 10.19 giả thiết số đếm là của chính thông điệp; ở đây số đếm là của văn bản dùng để dựng bảng, nên giả thiết bị vi phạm. Mệnh đề 10.2 cho biết một mã có ích trên văn bản thường phải kéo dài một số thông điệp khác. Khi dữ liệu không khớp thống kê, đầu ra có thể dài hơn đầu vào (NG, tr.24), như mức $37{,}5\%$ ở trên.

**(b) Bộ giải mã bỏ phép đổi.** Hai phía bắt đầu từ cây sau lần tăng thứ nhất của Ví dụ 10.12: A, B, C, D trọng số 2, E trọng số 10. Ký hiệu tiếp theo là A. Bộ mã chạy đúng Thuật toán 10.23, đổi A với D, nên sau bước này A = `100`, D = `111` theo quy ước bit ở Mục 4.1. Bộ giải mã bỏ phép đổi, chỉ tăng trọng số, nên giữ cây cũ với A = `111`, D = `100`.

**Hậu quả (b).** Nếu ký hiệu tiếp theo lại là A, bộ mã phát `100`, và bộ giải mã đọc `100` thành D. Từ đó hai cây khác nhau và mọi ký hiệu sau có thể bị giải sai, dù không bit nào bị lỗi. Danh sách của bộ giải mã A3, B2, C2, D2, … không còn không giảm, nên cây của nó không có tính chất anh em.

**Kiểm giả thiết (b).** Mệnh đề 10.27 cần hai phía chạy cùng thủ tục; bước "đổi với nút cuối khối" của Định lý 10.25 bị bỏ ở một phía.

**Dẫn ngược lý thuyết.** Mệnh đề 10.2, Định lý 10.18, Hệ quả 10.19, Thuật toán 10.23, Định lý 10.25, Mệnh đề 10.27.
:::

**Ứng dụng trong các nguồn và trong bài sau.**

- Mã Huffman có mặt trong các chương trình nén thương mại, máy fax và JPEG (NG, tr.37). Máy fax ITU-T Group 3 dùng mã độ dài loạt (run-length) cộng Huffman; JPEG dùng phép biến đổi, mã độ dài loạt và mã số học (CMU, trang chiếu 2–3).
- gzip dùng LZ77 và PKZip dùng một biến thể của LZW (CMU, trang chiếu 2), là các phương pháp nén bằng từ điển của Bài 11.
- Bài 11 cũng xét nén mất thông tin như JPEG, nơi yêu cầu khôi phục đúng từng bit của Định nghĩa 10.1 được thay bằng yêu cầu khôi phục gần đúng.

<!-- note-topic-id: lec-10-topic-23 -->
## Tóm tắt chương

Các phác thảo của Bài 09 trả lời truy vấn nhưng không dựng lại được dòng; câu hỏi xuất phát của Bài 10 là lưu hay truyền dữ liệu mà khôi phục đúng từng bit, với đặc tả là mã giải mã duy nhất (Định nghĩa 10.1) và giới hạn rằng không mã nào rút ngắn mọi thông điệp (Mệnh đề 10.2). Mã tiền tố cho điều kiện giải mã kiểm được trên từng cặp từ mã (Mệnh đề 10.6), bất đẳng thức Kraft quyết định bộ độ dài nào thực hiện được (Định lý 10.9), và entropy kẹp mã tiền tố tối ưu trong $[H;\,H+1)$ bit mỗi ký hiệu (Định lý 10.12, 10.13). Thuật toán Huffman dựng mã tiền tố tối ưu bằng cách ghép hai nút nhẹ nhất (Định lý 10.18, Hệ quả 10.19), nhưng cần hai lượt đọc và một đầu mục tăng nhanh theo bậc mô hình. Huffman thích nghi bỏ đầu mục bằng phép tăng–đổi giữ tính chất anh em (Định lý 10.22, 10.25), với hai phía luôn đồng bộ (Mệnh đề 10.27). Mọi mã ký hiệu tốn ít nhất 1 bit mỗi ký hiệu, nên mã số học mã cả thông điệp bằng một khoảng có độ rộng bằng xác suất của nó (Mệnh đề 10.31) và dùng ít hơn $I(x)+2$ bit (Định lý 10.34). Thanh ghi 16 bit thay cho số thực nhờ phát tiền tố chung và bit chờ, đúng khi mọi số đếm dương và $N\le2^{R-2}$ (Bổ đề 10.38, 10.39). Trên thông điệp A–E, số bit giảm từ 312 với ASCII xuống 87 với Huffman và với mã số học lý tưởng, so với đích $85{,}25$ bit. Cả ba bộ nén dùng mô hình đếm từng ký hiệu; Bài 11 khai thác các chuỗi lặp lại bằng từ điển.

**Định nghĩa và kết quả theo mục.**

- Mục 1: mã ký hiệu và giải mã duy nhất (Định nghĩa 10.1); không mã nào rút ngắn mọi thông điệp (Mệnh đề 10.2); mô hình và bộ mã (Định nghĩa 10.3); bốn thành phần giao thức (Nhận xét 10.4).
- Mục 2: mã tiền tố (Định nghĩa 10.5, Mệnh đề 10.6); khoảng mã (Định nghĩa 10.7, Bổ đề 10.8); Kraft (Định lý 10.9, Nhận xét 10.10); tự thông tin, entropy (Định nghĩa 10.11); hai cận entropy (Định lý 10.12, 10.13).
- Mục 3: Huffman tĩnh (Thuật toán 10.14); tối ưu (Bổ đề 10.15–10.17, Định lý 10.18, Hệ quả 10.19); chi phí và đầu mục (Nhận xét 10.20).
- Mục 4: tính chất anh em (Định nghĩa 10.21, Định lý 10.22); tăng–đổi (Thuật toán 10.23, Bổ đề 10.24, Định lý 10.25); mã hóa thích nghi (Thuật toán 10.26, Mệnh đề 10.27); chống tràn (Nhận xét 10.28, Thuật toán 10.29).
- Mục 5: khoảng chuỗi (Định nghĩa 10.30, Mệnh đề 10.31); mã hóa và giải mã (Thuật toán 10.32); `EOS` (Mệnh đề 10.33); cận độ dài (Định lý 10.34, Hệ quả 10.35).
- Mục 6: thanh ghi (Định nghĩa 10.36); chuẩn hóa (Thuật toán 10.37, Bổ đề 10.38, 10.39); giải mã và kết thúc (Thuật toán 10.40, Mệnh đề 10.41).
- Mục 7: bảng chọn cặp mô hình–bộ mã.

**Công thức và thuật toán cần nhớ.**

$$
\begin{gathered}
\sum_s2^{-\ell_s}\le1,\\
H(P)=\sum_sp_s\log_2\frac1{p_s},\\
H(P)\le\bar\ell(c_{\mathrm H})<H(P)+1.
\end{gathered}
$$

Với mã số học:

$$
\begin{gathered}
a_t=a_{t-1}+w_{t-1}F(x_t),\\
w_t=w_{t-1}p_{x_t},\\
\lambda=\lceil-\log_2w_n\rceil+1<I(x)+2 .
\end{gathered}
$$

Huffman tĩnh ghép hai nút nhẹ nhất trong $k-1$ lượt. Huffman thích nghi đi từ lá lên gốc, đổi nút đang tăng với nút cuối khối cùng trọng số rồi tăng. Mã số học nguyên, sau mỗi phép thu hẹp, lặp ba trường hợp: nửa dưới (phát 0 và $m$ bit 1), nửa trên (phát 1 và $m$ bit 0), khoảng giữa (tăng $m$).

**Giả thiết hay bị bỏ quên.**

- Mã tiền tố là trường hợp riêng của mã giải mã duy nhất; tổng Kraft bằng 1 không bảo đảm một bộ từ mã cụ thể giải được.
- Tối ưu của Huffman chỉ trong lớp mã ký hiệu nguyên bit và cho số đếm đã đưa vào; quy tắc phá hòa và gán bit thuộc giao thức.
- Huffman thích nghi cần mọi lá có trọng số dương ngoài lá vừa thêm, và hai phía chạy cùng thủ tục, kể cả thời điểm dựng lại.
- Khoảng là nửa mở; $F(s)$ không gồm chính $s$; bộ giải mã phải biết cách dừng.
- Mã số học nguyên cần $f_s\ge1$ và $N\le2^{R-2}$; Hệ quả 10.35 cần mô hình đúng và ký hiệu độc lập.

<!-- note-topic-id: lec-10-topic-24 -->
## Bài tập củng cố

Bài tập 10.9–10.21 nằm trong [tệp bài tập Bài 10](material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-nen-du-lieu-khong-mat-thong-tin.html), cùng gợi ý và lời giải.

<!-- note-topic-id: lec-10-topic-25 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

Số trang của NG là số trang của tệp PDF trong bộ nguồn của học phần; số trang in của sách không được dùng.

- Nelson, M. và Gailly, J.-L. (1995). *The Data Compression Book*, ấn bản 2, M&T Books. Chương 2, tr.18–25: Mục 1, Mục 2.3, Tình huống 10.3(a), Bài tập 10.21; tên "entropy của một ký hiệu" và "entropy của thông điệp" (tr.20) ứng với tự thông tin $I(s)$ và $I(x)$. Chương 3, tr.30–37 và 51–66: Ví dụ 10.1, 10.5, 10.7, 10.8, Nhận xét 10.20, Bài tập 10.1, 10.4, 10.11. Chương 4, tr.66–95: Mục 4, Bài tập 10.5, 10.14, 10.16. Chương 5, tr.96–126: Mục 5, Mục 6, Bài tập 10.7, 10.17. Thư mục, tr.384–385: Huffman (1952) và Witten, Neal, Cleary (1987).
- Blelloch, G. CMU 15-499, *Algorithms in the Real World: Data Compression*, phần 1–2, trang chiếu 2–8, 13–14, 20–56: Mục 1–3, Mục 5, Mục 6, phần Ứng dụng, Bài tập 10.6, 10.9, 10.20. Assignment 1a và lời giải, bài 2–4: Bài tập 10.10, 10.12, 10.13, 10.15.
- Girod, B. Stanford EE398A, *Entropy and Lossless Coding*, trang chiếu 3–23: Mục 2, Định nghĩa 10.3; *Arithmetic Coding*, trang chiếu 2–14: Mục 5, Mục 6.3.
- Stanford CS106B, *Huffman Coding*, tr.130–132 và 182: hàng đợi ưu tiên trong Huffman, Mệnh đề 10.2.
- Chứng minh nằm ngoài phạm vi học phần: bất đẳng thức McMillan (EE398A-1, trang chiếu 13; CMU, trang chiếu 28); cận Fibonacci cho độ dài từ mã Huffman (NG, tr.74–75); tính đúng của bộ giải mã số học nguyên, trong Witten, I. H., Neal, R. M. và Cleary, J. G. (1987), "Arithmetic Coding for Data Compression", *Communications of the ACM* 30(6), tr.520–540 (NG, tr.133, 385).
- Đọc thêm, không cần cho bài tập: mã khối và mã Huffman cắt ngắn (EE398A-1, trang chiếu 21–22); entropy có điều kiện và nguồn Markov (CMU, trang chiếu 15–16; CMU-A1, bài 1); mô hình bậc cao và mã số học thích nghi (NG, Chương 6, từ tr.127; CMU, trang chiếu 61–73); cài đặt mã số học bằng lan truyền nhớ và tổn thất do làm tròn (EE398A-3, trang chiếu 10–14).
- Đọc tiếp: [Bài 11](lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html), *Nén bằng từ điển và nén mất dữ liệu*.
- Ghi chú Bài 08, Bài 09 (Định lý 09.37) và Bài 05 (Mục 10): các kết quả nhắc lại ở phần kiến thức tiên quyết.
