# Bài tập Bài 05 — Biểu diễn tương đồng: Shingling và MinHash

Các bài tập củng cố 05.15–05.28 dưới đây lấy từ bài tập Chương 3 của sách *Mining of Massive Datasets*, ấn bản 3 (viết tắt MMDS), §3.1–3.3, kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 05.k là của [ghi chú Bài 05](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html), nơi Bài tập 05.1–05.14 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Đề sách viết độ dài tài liệu, cỡ vũ trụ và số hàng đều là $n$, cỡ tập con ở Bài 3.1.3 là $m$, và hàm băm hàng là $h_i$; ở đây độ dài tài liệu là $\ell$, cỡ vũ trụ và số hàng là $R$, cỡ tập con là $q$, hàm băm hàng là $f_i$, vì $n$ là độ dài chữ ký, $m$ là số hàng của phép thử rút gọn và $h_\pi$ là MinHash. Dấu (!) và (!!) sau số bài là mức khó và rất khó do MMDS đánh dấu. Năm bài 05.15, 05.19, 05.20, 05.21 và 05.22, tức MMDS Bài 3.1.1, 3.2.3, 3.3.1, 3.3.2 và 3.3.3, là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 05](lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html). Bài tập xếp theo ba mức; ba bài 05.17, 05.18 và 05.28 dùng phần đọc thêm của ghi chú.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Số cặp nhân chi phí một cặp; Jaccard theo cách chọn phần tử (Mục 1) | 05.1, 05.2 | 05.15 |
| 2. Tập $k$-shingle, Thuật toán 05.3, mã băm giữ Jaccard (Mục 2) | 05.3, 05.4 | 05.16, 05.19 |
| 3. Ma trận đặc trưng, MinHash, Định lý 05.10 (Mục 3) | 05.5, 05.6 | 05.20, 05.23, 05.26, 05.27 |
| 4. Chữ ký, ước lượng không chệch, chi phí so (Mục 4.1–4.3) | 05.7(a)(b), 05.9 | 05.22(c) |
| 5. Phương sai và độ dài chữ ký (Mục 4.4) | 05.7(c), 05.8 | — |
| 6. Thuật toán 05.18, bất biến, thời gian và bộ nhớ (Mục 5.1–5.4) | 05.10, 05.11 | 05.21, 05.22(a), 05.25 |
| 7. Hàm affine là hoán vị; giả thiết bị vi phạm (Mục 5.5, Tình huống 05.2, 05.3) | 05.12 | 05.22(b), 05.24 |
| Đọc thêm: đa tập, từ dừng, chia nhóm hàng | 05.13, 05.14 | 05.17, 05.18, 05.28 |

## Mức nhận biết

::: exercise Bài tập 05.15 (Jaccard của ba tập; MMDS Bài 3.1.1, §3.1.4, tr.78)
Cho ba tập $S_A=\{1,2,3,4\}$, $S_B=\{2,3,5,7\}$ và $S_C=\{2,4,6\}$. Tính độ tương đồng Jaccard của từng cặp. Trình bày bảng ba cặp gồm giao, hợp và tỷ số.
:::

::: hint
Liệt kê giao và hợp của từng cặp; mỗi phần tử của hợp được đếm một lần.
:::

::: solution
Theo Định nghĩa 01.9:

| Cặp | Giao | Hợp | Jaccard |
|---|---|---|---|
| $S_A$, $S_B$ | $\{2,3\}$ | $\{1,2,3,4,5,7\}$ | $2/6=1/3$ |
| $S_A$, $S_C$ | $\{2,4\}$ | $\{1,2,3,4,6\}$ | $2/5$ |
| $S_B$, $S_C$ | $\{2\}$ | $\{2,3,4,5,6,7\}$ | $1/6$ |

**Kiểm tra lại.** $|S\cup T|=|S|+|T|-|S\cap T|$ cho $4+4-2=6$, $4+3-2=5$, $4+3-1=6$. Lấy $|S|+|T|$ làm mẫu số sẽ đếm hai lần các phần tử giao.
:::

::: exercise Bài tập 05.16 (Mười 3-shingle đầu tiên; MMDS Bài 3.2.1, §3.2.5, tr.80)
Câu đầu tiên của MMDS §3.2 là

> The most effective way to represent documents as sets, for the purpose of identifying lexically similar documents is to construct from the document the set of short strings that appear within it.

Liệt kê mười 3-shingle đầu tiên của câu này, theo thứ tự vị trí bắt đầu, giữ chữ hoa và dấu cách như trong câu (Định nghĩa 05.2, Nhận xét 05.5).
:::

::: hint
Shingle thứ $j$ là $D[j:j+3]$ với $j=0,1,\ldots,9$; dấu cách cũng là một ký tự.
:::

::: solution
Với ␣ chỉ dấu cách, mười cửa sổ bắt đầu tại $0,\ldots,9$ là

| $j$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| $D[j:j+3]$ | `The` | `he␣` | `e␣m` | `␣mo` | `mos` | `ost` | `st␣` | `t␣e` | `␣ef` | `eff` |

Mười chuỗi đôi một khác nhau, nên đây cũng là mười phần tử đầu tiên được chèn vào tập $S_3(D)$ theo Thuật toán 05.3.

**Kiểm tra lại.** Mười hai ký tự đầu của câu là `The␣most␣eff`; mười cửa sổ dài 3 bắt đầu tại $0,\ldots,9$ dùng hết mười hai ký tự này. Bỏ dấu cách sẽ làm mất `he␣`, `e␣m`, `␣mo`, `st␣`, `t␣e`, `␣ef`.
:::

::: exercise Bài tập 05.17 (Jaccard của ba đa tập; MMDS Bài 3.1.2, §3.1.4, tr.78; Đọc thêm)
Theo Định nghĩa 05.24, tính độ tương đồng Jaccard của từng cặp trong ba đa tập $B_1=\{1,1,1,2\}$, $B_2=\{1,1,2,2,3\}$ và $B_3=\{1,2,3,4\}$.
:::

::: hint
Lập bảng bội $\mu_B(u)$ của mỗi phần tử; tử số cộng các bội nhỏ hơn, mẫu số cộng kích thước hai đa tập.
:::

::: solution
Bảng bội:

| $u$ | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| $\mu_{B_1}(u)$ | 3 | 1 | 0 | 0 |
| $\mu_{B_2}(u)$ | 2 | 2 | 1 | 0 |
| $\mu_{B_3}(u)$ | 1 | 1 | 1 | 1 |

- $B_1$, $B_2$: tử số $2+1+0+0=3$, mẫu số $4+5=9$, Jaccard $1/3$.
- $B_1$, $B_3$: tử số $1+1=2$, mẫu số $4+4=8$, Jaccard $1/4$.
- $B_2$, $B_3$: tử số $1+1+1=3$, mẫu số $5+4=9$, Jaccard $1/3$.

**Kiểm tra lại.** Cặp $B_1$, $B_2$ trùng Ví dụ 05.14 sau khi đổi tên $\mathrm a\to1$, $\mathrm b\to2$, $\mathrm c\to3$. Cả ba giá trị không vượt $1/2$, giá trị lớn nhất của Định nghĩa 05.24.
:::

::: exercise Bài tập 05.18 (Shingle theo từ dừng ba chữ cái; MMDS Bài 3.2.2, §3.2.5, tr.81; Đọc thêm)
Dùng shingle theo từ dừng của Định nghĩa 05.25, với từ dừng là mọi từ có không quá ba chữ cái. Liệt kê các shingle của câu đầu tiên của MMDS §3.2 ở Bài tập 05.16; bỏ dấu câu khi tách từ.
:::

::: hint
Đánh dấu mọi từ có một, hai hoặc ba chữ cái, kể cả "The", "way", "set"; một từ dừng chỉ tạo shingle khi có đủ hai từ đứng sau.
:::

::: solution
Câu có 32 từ. Các từ dừng, theo thứ tự, là The, way, to, as, for, the, of, is, to, the, the, set, of, it: 14 từ. Từ dừng cuối "it" là từ cuối câu nên không tạo shingle; mười ba từ dừng còn lại cho mười ba shingle:

| Từ dừng | Shingle | Từ dừng | Shingle |
|---|---|---|---|
| The | `The most effective` | to | `to construct from` |
| way | `way to represent` | the | `the document the` |
| to | `to represent documents` | the | `the set of` |
| as | `as sets for` | set | `set of short` |
| for | `for the purpose` | of | `of short strings` |
| the | `the purpose of` | | |
| of | `of identifying lexically` | | |
| is | `is to construct` | | |

Hai shingle `to represent documents` và `to construct from` bắt đầu bằng cùng từ "to" nhưng là hai chuỗi khác nhau, nên tập có đủ 13 phần tử.

**Kiểm tra lại.** $14-1=13$; các từ dài bốn chữ cái trở lên như "most", "that", "from" không là từ dừng theo quy ước của đề.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 05.19 (Số $k$-shingle lớn nhất; MMDS Bài 3.2.3, §3.2.5, tr.81)
Một tài liệu dài $\ell$ byte, mỗi ký tự một byte. Giả sử bảng chữ cái đủ lớn để số chuỗi độ dài $k$ khả dĩ ít nhất bằng $\ell$. Xác định số $k$-shingle lớn nhất mà tài liệu có thể có, theo $\ell$ và $k$, và lập luận theo vị trí cửa sổ.
:::

::: hint
Đếm các vị trí bắt đầu hợp lệ; mỗi vị trí cho nhiều nhất một shingle.
:::

::: solution
**Cận trên.** Nếu $1\le k\le\ell$, vị trí bắt đầu chạy từ $0$ đến $\ell-k$, nên có $\ell-k+1$ cửa sổ (Định nghĩa 05.2). Mỗi cửa sổ cho nhiều nhất một shingle; cửa sổ trùng nhau chỉ làm giảm số phần tử phân biệt. Vì vậy $|S_k(D)|\le\ell-k+1$ (Mệnh đề 05.4(b)). Nếu $\ell<k$, không có cửa sổ nào và $S_k(D)=\varnothing$. Gộp hai trường hợp, số shingle không vượt $\max(0,\ell-k+1)$.

**Đạt cận.** Muốn đạt cận cần ít nhất $\ell-k+1$ chuỗi dài $k$ khác nhau; giả thiết của đề, $\lvert\Sigma\rvert^k\ge\ell\ge\ell-k+1$ với $\Sigma$ là bảng chữ cái, bảo đảm điều này. Khi bảng chữ cái có ít nhất $\ell-k+1$ ký tự, có một phép dựng tường minh: lấy $\ell-k+1$ ký tự đầu đôi một khác nhau và $k-1$ ký tự cuối tùy ý. Hai cửa sổ ở hai vị trí khác nhau bắt đầu bằng hai ký tự khác nhau, nên $\ell-k+1$ cửa sổ đôi một khác nhau và số shingle đúng bằng $\ell-k+1$. Với bảng chữ cái nhỏ hơn, cận vẫn đạt được trong các trường hợp như `00010111` ở dưới, với hai ký tự.

**Kết luận.** Số $k$-shingle không vượt $\max(0,\ell-k+1)$, và cận này đạt được khi bảng chữ cái có ít nhất $\ell-k+1$ ký tự.

**Kiểm tra lại.** `abcdabd` với $\ell=7$, $k=2$ có 6 cửa sổ nhưng 5 shingle (Ví dụ 05.2), dưới cận vì `ab` lặp. Với $\ell=6$, $k=3$, chuỗi `abcdaa` có bốn ký tự đầu khác nhau và bốn cửa sổ `abc`, `bcd`, `cda`, `daa` khác nhau. Với bảng chữ cái $\{0,1\}$, $k=3$, $\ell=8$, ta có $2^3=8\ge\ell$, và chuỗi `00010111` có sáu cửa sổ `000`, `001`, `010`, `101`, `011`, `111` đôi một khác nhau, đạt $\ell-k+1=6$.
:::

::: exercise Bài tập 05.20 (Jaccard và 120 hoán vị của Hình 3.2; MMDS Bài 3.3.1, câu (b) (!), §3.3.8, tr.90)
Cho ma trận đặc trưng của MMDS Hình 3.2 (Ví dụ 05.5):

| Phần tử | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| a | 1 | 0 | 0 | 1 |
| b | 0 | 0 | 1 | 0 |
| c | 0 | 1 | 0 | 1 |
| d | 1 | 0 | 1 | 1 |
| e | 0 | 0 | 1 | 0 |

- (a) Tính Jaccard của mọi cặp cột; trình bày kích thước giao, hợp và tỷ số.
- (b) Với mỗi cặp, tính tỷ lệ trong $5!=120$ hoán vị của năm hàng làm hai MinHash bằng nhau; trình bày số hoán vị trùng và đối chiếu với câu (a).
:::

::: hint
Câu (b): không cần liệt kê 120 hoán vị. Đếm số hoán vị mà mỗi phần tử của hợp đứng đầu hợp, như trong chứng minh Bổ đề 05.9.
:::

::: solution
**Câu (a).** Các tập là $S_1=\{\mathrm a,\mathrm d\}$, $S_2=\{\mathrm c\}$, $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$.

| Cặp | Giao | Hợp | $\lvert\text{giao}\rvert/\lvert\text{hợp}\rvert$ |
|---|---|---|---|
| 1–2 | $\varnothing$ | $\{\mathrm a,\mathrm c,\mathrm d\}$ | $0/3=0$ |
| 1–3 | $\{\mathrm d\}$ | $\{\mathrm a,\mathrm b,\mathrm d,\mathrm e\}$ | $1/4$ |
| 1–4 | $\{\mathrm a,\mathrm d\}$ | $\{\mathrm a,\mathrm c,\mathrm d\}$ | $2/3$ |
| 2–3 | $\varnothing$ | $\{\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$ | $0/4=0$ |
| 2–4 | $\{\mathrm c\}$ | $\{\mathrm a,\mathrm c,\mathrm d\}$ | $1/3$ |
| 3–4 | $\{\mathrm d\}$ | $\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$ | $1/5$ |

**Câu (b).** Xét một cặp có giao gồm $x$ phần tử và hợp gồm $x+y$ phần tử. Theo Bước 1 và Bước 2 trong chứng minh Bổ đề 05.9, các hoán vị chia thành $x+y$ nhóm cùng cỡ theo phần tử đứng đầu hợp, mỗi nhóm $120/(x+y)$ hoán vị. Theo Bước 2 trong chứng minh Định lý 05.10, hai MinHash bằng nhau đúng khi phần tử đứng đầu hợp thuộc giao, nên số hoán vị trùng là $x\cdot120/(x+y)$.

| Cặp | $x$ | $x+y$ | Số hoán vị trùng | Tỷ lệ |
|---|---:|---:|---:|---|
| 1–2 | 0 | 3 | 0 | 0 |
| 1–3 | 1 | 4 | 30 | $1/4$ |
| 1–4 | 2 | 3 | 80 | $2/3$ |
| 2–3 | 0 | 4 | 0 | 0 |
| 2–4 | 1 | 3 | 40 | $1/3$ |
| 3–4 | 1 | 5 | 24 | $1/5$ |

Mọi tỷ lệ bằng Jaccard của câu (a), đúng Định lý 05.10.

**Kiểm tra lại.** $120/(x+y)$ nguyên với $x+y\in\{3,4,5\}$; ở cặp 1–4, 80 hoán vị là hai nhóm 40 hoán vị có a hoặc d đứng đầu hợp, và nhóm còn lại, c đứng đầu, gồm 40 hoán vị.
:::

::: exercise Bài tập 05.21 (Hai hàng chữ ký bổ sung; MMDS Bài 3.3.2, §3.3.8, tr.90)
Dùng dữ liệu của MMDS Hình 3.4 (Ví dụ 05.11), mã hàng $0$ đến $4$:

| $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 | 1 |
| 4 | 0 | 0 | 1 | 0 |

Ma trận chữ ký của $f_1(r)=(r+1)\bmod5$, $f_2(r)=(3r+1)\bmod5$ là $\begin{pmatrix}1&3&0&1\\0&2&0&0\end{pmatrix}$ (Ví dụ 05.12). Thêm vào chữ ký các giá trị của

- (a) $f_3(r)=(2r+4)\bmod5$;
- (b) $f_4(r)=(3r-1)\bmod5$.

Trình bày bảng giá trị hai hàm và hai hàng chữ ký mới.
:::

::: hint
Phần dư lấy trong $\{0,\ldots,4\}$, nên $(-1)\bmod5=4$. Lấy cực tiểu trên tập hàng của từng cột.
:::

::: solution
**Bảng giá trị.**

| $r$ | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| $f_3(r)$ | 4 | 1 | 3 | 0 | 2 |
| $f_4(r)$ | 4 | 2 | 0 | 3 | 1 |

Tập hàng của bốn cột là $\{0,3\}$, $\{2\}$, $\{1,3,4\}$, $\{0,2,3\}$.

**Câu (a).** $\mathrm{SIG}(3,\cdot)$: $S_1$: $\min(4,0)=0$; $S_2$: $3$; $S_3$: $\min(1,0,2)=0$; $S_4$: $\min(4,3,0)=0$. Hàng mới là $(0,3,0,0)$.

**Câu (b).** $\mathrm{SIG}(4,\cdot)$: $S_1$: $\min(4,3)=3$; $S_2$: $0$; $S_3$: $\min(2,3,1)=1$; $S_4$: $\min(4,0,3)=0$. Hàng mới là $(3,0,1,0)$.

Ma trận chữ ký bốn hàng là
$$
\begin{pmatrix}1&3&0&1\\0&2&0&0\\0&3&0&0\\3&0&1&0\end{pmatrix}.
$$
Theo Định nghĩa 05.11, ước lượng từ bốn hàng của sáu cặp 1–2, 1–3, 1–4, 2–3, 2–4, 3–4 là $0$, $1/2$, $3/4$, $0$, $1/4$, $1/2$, so với Jaccard $0$, $1/4$, $2/3$, $0$, $1/3$, $1/5$ của Bài tập 05.20(a).

**Kiểm tra lại.** $f_3$ và $f_4$ là hoán vị vì $\gcd(2,5)=\gcd(3,5)=1$ (Mệnh đề 05.22), đúng với hai hàng của bảng giá trị đều chứa đủ $0,\ldots,4$; do đó mỗi giá trị cực tiểu ứng với đúng một hàng.
:::

::: exercise Bài tập 05.22 (Chữ ký với ba hàm modulo 6; MMDS Bài 3.3.3, §3.3.8, tr.90–91)
Cho ma trận sáu hàng của MMDS Hình 3.6:

| $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 | 1 |
| 3 | 0 | 0 | 1 | 0 |
| 4 | 0 | 0 | 1 | 1 |
| 5 | 1 | 0 | 0 | 0 |

và ba hàm $f_1(r)=(2r+1)\bmod6$, $f_2(r)=(3r+2)\bmod6$, $f_3(r)=(5r+2)\bmod6$.

- (a) Tính chữ ký MinHash của mỗi cột.
- (b) Xác định những hàm là hoán vị của $\{0,\ldots,5\}$.
- (c) Với sáu cặp cột, so Jaccard ước lượng từ chữ ký với Jaccard thật; trình bày ước lượng, giá trị thật và sai lệch.
:::

::: hint
Câu (a): lập bảng giá trị ba hàm trước, rồi chạy Thuật toán 05.18 hoặc lấy cực tiểu theo Định nghĩa 05.17. Câu (b): Mệnh đề 05.22.
:::

::: solution
**Câu (a).** Bảng giá trị:

| $r$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| $f_1(r)$ | 1 | 3 | 5 | 1 | 3 | 5 |
| $f_2(r)$ | 2 | 5 | 2 | 5 | 2 | 5 |
| $f_3(r)$ | 2 | 1 | 0 | 5 | 4 | 3 |

Các tập hàng là $S_1=\{2,5\}$, $S_2=\{0,1\}$, $S_3=\{3,4\}$, $S_4=\{0,2,4\}$. Lấy cực tiểu trên từng tập hàng, theo thứ tự $f_1$, $f_2$, $f_3$:

- $S_1$: $\min(5,5)=5$, $\min(2,5)=2$, $\min(0,3)=0$;
- $S_2$: $\min(1,3)=1$, $\min(2,5)=2$, $\min(2,1)=1$;
- $S_3$: $\min(1,3)=1$, $\min(5,2)=2$, $\min(5,4)=4$;
- $S_4$: $\min(1,5,3)=1$, $\min(2,2,2)=2$, $\min(2,0,4)=0$.

Vậy
$$
\mathrm{SIG}=\begin{pmatrix}5&1&1&1\\2&2&2&2\\0&1&4&0\end{pmatrix}.
$$

**Câu (b).** Chỉ $f_3$ nhận đủ sáu giá trị khác nhau, nên chỉ $f_3$ là hoán vị. Theo Mệnh đề 05.22: $\gcd(2,6)=2$, $\gcd(3,6)=3$, còn $\gcd(5,6)=1$; modulo 6 là hợp số nhưng hệ số 5 vẫn cho một hoán vị.

**Câu (c).** So từng tọa độ rồi chia cho $n=3$:

| Cặp | Số tọa độ trùng | Ước lượng | Jaccard thật | Sai lệch (ước lượng − thật) |
|---|---:|---|---|---|
| 1–2 | 1 | $1/3$ | $0$ | $1/3$ |
| 1–3 | 1 | $1/3$ | $0$ | $1/3$ |
| 1–4 | 2 | $2/3$ | $1/4$ | $5/12$ |
| 2–3 | 2 | $2/3$ | $0$ | $2/3$ |
| 2–4 | 2 | $2/3$ | $1/4$ | $5/12$ |
| 3–4 | 2 | $2/3$ | $1/4$ | $5/12$ |

Ba cặp 1–2, 1–3, 2–3 rời nhau nhưng vẫn có tọa độ trùng, vì $f_1$ và $f_2$ có va chạm: hai hàng khác nhau cho cùng giá trị cực tiểu (Nhận xét 05.23). Mọi ước lượng đều lớn hơn giá trị thật.

**Kiểm tra lại.** Hàng $f_2$ của $\mathrm{SIG}$ toàn 2 vì $f_2$ cho 2 trên mọi hàng chẵn và mỗi cột chứa ít nhất một hàng chẵn; riêng hàng $f_3$, một hoán vị, cho các tập rời $S_1$, $S_2$ hai giá trị khác nhau $0$ và $1$.
:::

::: exercise Bài tập 05.23 (Tập rời luôn cho ước lượng đúng; MMDS Bài 3.3.5 (!), §3.3.8, tr.91)
Chứng minh: nếu hai tập không rỗng $S$, $T$ có $\mathrm{SIM}(S,T)=0$ thì với mọi bộ hoán vị $\pi_1,\ldots,\pi_n$, ước lượng $\widehat s$ của Định nghĩa 05.11 bằng 0, tức MinHash luôn cho ước lượng đúng.
:::

::: hint
Xét một tọa độ $i$ và giả sử hai MinHash ở tọa độ đó bằng nhau.
:::

::: solution
$\mathrm{SIM}(S,T)=0$ khi và chỉ khi $S\cap T=\varnothing$ (Định nghĩa 01.9). Với mọi hoán vị $\pi_i$, $h_{\pi_i}(S)\in S$ và $h_{\pi_i}(T)\in T$ theo Định nghĩa 05.8; nếu hai phần tử bằng nhau, phần tử chung ấy thuộc $S\cap T$, mâu thuẫn. Do đó mọi chỉ báo $\mathbf 1[h_{\pi_i}(S)=h_{\pi_i}(T)]$ bằng 0, và $\widehat s=0=\mathrm{SIM}(S,T)$ với mọi bộ hoán vị, không cần giả thiết chọn đều. $\square$

Lập luận dùng việc mỗi thành phần chữ ký là một phần tử của tập. Với hàm băm hàng có va chạm, chữ ký lưu giá trị băm, và hai tập rời có thể có cùng giá trị cực tiểu: ở Bài tập 05.22(c), cặp rời 1–2 cho ước lượng $1/3$.

**Kiểm tra lại.** Bài tập 05.20(b) cho 0 hoán vị trùng ở hai cặp rời 1–2 và 2–3 trong 120 hoán vị.
:::

## Mức vận dụng

::: exercise Bài tập 05.24 (Xử lý tập rỗng; MMDS Bài 3.3.8 (!), §3.3.8, tr.91)
Khi MinHash chỉ tính trên một phần các hàng, một cột có thể toàn 0 trên các hàng được xét dù tập khác rỗng (MMDS §3.3.6). Nếu tính trên mọi hàng, như Định nghĩa 05.8 và Thuật toán 05.18, thì một cột toàn 0 khi và chỉ khi nó biểu diễn tập rỗng. Xác định cách xử lý tập rỗng để việc ước lượng Jaccard từ chữ ký không sinh sai số.
:::

::: hint
Xét riêng ba loại cặp: hai tập không rỗng, một rỗng và một không rỗng, hai tập rỗng; với mỗi loại, so giá trị $\widehat s$ mà Thuật toán 05.18 cho với $\mathrm{SIM}$.
:::

::: solution
**Đầu ra của phép quét.** Theo Định nghĩa 05.17 và Mệnh đề 05.19, cột của tập rỗng có chữ ký toàn $+\infty$, còn cột không rỗng có mọi thành phần hữu hạn.

**Một rỗng, một không rỗng.** Với $T\ne\varnothing$, $\mathrm{SIM}(\varnothing,T)=0/|T|=0$. Mỗi tọa độ so $+\infty$ với một giá trị hữu hạn nên không trùng, và $\widehat s=0$: không có sai số, miễn là $+\infty$ khác mọi giá trị thật của $f_i$, tức lớn hơn mọi phần tử của $V$.

**Hai tập rỗng.** Hai cột toàn $+\infty$ trùng ở mọi tọa độ, nên phép tính tỷ lệ cho $\widehat s=1$, trong khi $\mathrm{SIM}(\varnothing,\varnothing)=0/0$ không xác định. Đây là chỗ duy nhất sinh sai số.

**Cách xử lý.** Phát hiện tập rỗng trước khi so: một cột có chữ ký toàn $+\infty$, hoặc một tài liệu có $\ell<k$ (Định nghĩa 05.2), hoặc đếm được không ô 1 nào trong lượt quét. Với một cặp hai tập rỗng, không lấy tỷ lệ tọa độ trùng mà gán giá trị theo quy ước của ứng dụng, hoặc loại cặp khỏi phép so. Nếu ứng dụng quy ước $\mathrm{SIM}(\varnothing,\varnothing)=1$, phép so $+\infty=+\infty$ cho đúng quy ước đó; nếu quy ước là 0, phải gán riêng.

**Kiểm tra lại.** Tình huống 05.2 của ghi chú là trường hợp hai dòng `Mua ngay`, `Gia soc` với $k=9$: không xử lý thì $\widehat s=1$; sau khi phát hiện hai cột rỗng, cặp được xử lý theo quy ước và không còn ước lượng sai.
:::

::: exercise Bài tập 05.25 (Tính chữ ký bằng MapReduce khi ma trận chia theo hàng; MMDS Bài 3.3.7 (!), §3.3.8, tr.91)
Nhắc lại từ ghi chú Bài 02: hàm Map nhận một phần tử đầu vào và phát một dãy cặp khóa–giá trị (Định nghĩa 02.6); các cặp được nhóm theo khóa, và hàm Reduce nhận một khóa cùng danh sách mọi giá trị của khóa ấy (Định nghĩa 02.7, 02.8). Nếu $\oplus$ kết hợp và giao hoán (Định nghĩa 02.1), phép gộp một dãy không phụ thuộc thứ tự và cách chia nhóm (Bổ đề 02.2); khi Reduce áp $\oplus$ rồi một hàm hoàn tất, một hàm Combine phát $(k,\bigoplus L)$ ở tác vụ Map không đổi kết quả (Định nghĩa 02.14, Mệnh đề 02.15).

Ma trận đặc trưng được lưu thành các khối hàng: mỗi tác vụ Map nhận mọi hàm $f_1,\ldots,f_n$ và một khối gồm một tập mã hàng $P$, với mỗi $r\in P$ là danh sách các cột có 1 ở hàng $r$. Thiết kế hàm Map và hàm Reduce để tính ma trận chữ ký của Định nghĩa 05.17, chứng minh đầu ra đúng, và kiểm thiết kế trên Ví dụ 05.12 với hai khối $P_1=\{0,1\}$, $P_2=\{2,3,4\}$.
:::

::: hint
Phép min theo từng thành phần trên $(V\cup\{+\infty\})^n$ là một phép gộp kết hợp, giao hoán; min trên mọi hàng bằng min của các min theo khối.
:::

::: solution
**Thiết kế.**

- Map nhận khối $P$. Với mỗi cột $c$ có ít nhất một ô 1 trong $P$, Map tính véc-tơ $\bigl(\min\{f_i(r):r\in P,\ M(r,c)=1\}\bigr)_{i=1,\ldots,n}$ và phát cặp $(c,\text{véc-tơ})$.
- Reduce nhận khóa $c$ cùng danh sách các véc-tơ do các khối phát cho $c$, lấy min theo từng thành phần và phát $(c,\text{véc-tơ min})$.
- Sau công việc, mọi cột không nhận được cặp nào là cột rỗng và được gán chữ ký toàn $+\infty$.

**Tính đúng.** Với một cột $c$ không rỗng và một thành phần $i$, các khối phân hoạch tập hàng $\{r:M(r,c)=1\}$. Phép min kết hợp và giao hoán (Định nghĩa 02.1), nên theo Bổ đề 02.2(c), min của các min theo khối bằng min trên toàn bộ tập hàng, tức $\mathrm{SIG}(i,c)$ của Định nghĩa 05.17; thứ tự các véc-tơ trong danh sách của Reduce không ảnh hưởng, như Hệ quả 05.20 với thứ tự quét. Một khối không có ô 1 nào của cột $c$ không phát cặp cho $c$, đúng vì nó không thêm giá trị nào vào tập lấy cực tiểu. Reduce áp phép min theo từng thành phần, kết hợp và giao hoán, rồi hàm hoàn tất đồng nhất, nên thỏa giả thiết của Mệnh đề 02.15; một Combine lấy min các véc-tơ cùng khóa ở một tác vụ Map không đổi kết quả khi tác vụ đó xử lý nhiều khối (Định nghĩa 02.14).

**Kiểm trên Ví dụ 05.12.** Giá trị $(f_1,f_2)$ của năm hàng là $(1,1)$, $(2,4)$, $(3,2)$, $(4,0)$, $(0,3)$.

- Map trên $P_1=\{0,1\}$: hàng 0 thuộc $S_1$, $S_4$; hàng 1 thuộc $S_3$. Phát $(S_1,(1,1))$, $(S_3,(2,4))$, $(S_4,(1,1))$.
- Map trên $P_2=\{2,3,4\}$: phát $(S_1,(4,0))$, $(S_2,(3,2))$, $(S_3,(\min(4,0),\min(0,3)))=(S_3,(0,0))$, $(S_4,(\min(3,4),\min(2,0)))=(S_4,(3,0))$.
- Reduce: $S_1$: $\min((1,1),(4,0))=(1,0)$; $S_2$: $(3,2)$; $S_3$: $\min((2,4),(0,0))=(0,0)$; $S_4$: $\min((1,1),(3,0))=(1,0)$.

Kết quả là $\begin{pmatrix}1&3&0&1\\0&2&0&0\end{pmatrix}$, đúng ma trận của Ví dụ 05.12.

**Kiểm tra lại.** Số cặp Map phát ra bằng tổng theo khối của số cột có 1 trong khối: $3+4=7$, không quá số khối nhân $C$, $2\cdot4=8$; mỗi cặp mang $n$ giá trị.
:::

::: exercise Bài tập 05.26 (Hoán vị vòng không đủ; MMDS Bài 3.3.6 (!!), §3.3.8, tr.91)
Thay vì chọn đều trong mọi hoán vị của $R$ hàng, chỉ chọn đều một hàng bắt đầu $r$ rồi xét các hàng theo thứ tự $r,r+1,\ldots,R-1,0,1,\ldots,r-1$; có $R$ hoán vị vòng như vậy. Cho một ví dụ ma trận hai cột mà trung bình qua mọi hoán vị vòng của chỉ báo "hai MinHash bằng nhau" khác Jaccard của hai cột.
:::

::: hint
Thử ba hàng và hai tập lồng nhau; giả thiết nào của Bổ đề 05.9 bị bỏ.
:::

::: solution
**Ví dụ.** Ba hàng $0,1,2$; $S=\{0\}$, $T=\{0,1\}$; $\mathrm{SIM}(S,T)=1/2$.

| Hàng bắt đầu | Thứ tự | $h_\pi(S)$ | $h_\pi(T)$ | Trùng |
|---:|---|---:|---:|---|
| 0 | $0,1,2$ | 0 | 0 | có |
| 1 | $1,2,0$ | 0 | 1 | không |
| 2 | $2,0,1$ | 0 | 0 | có |

Trung bình qua ba hoán vị vòng là $2/3\ne1/2$.

**Nguyên nhân.** Bổ đề 05.9 cần $\pi$ chọn đều trên mọi hoán vị. Với hoán vị vòng, phần tử đứng đầu của $S\cup T=\{0,1\}$ là 0 ở hai trong ba thứ tự, vì hàng 2 ngoài hợp đứng ngay trước hàng 0 theo vòng: một phần tử đứng sau một đoạn dài các hàng ngoài hợp có nhiều thứ tự hơn để đứng đầu. Phân phối của phần tử đứng đầu không đều, và Bước 1 trong chứng minh Định lý 05.10 hỏng.

**Kiểm tra lại.** Với chỉ hai hàng $\{0,1\}$ và cùng $S$, $T$, hai thứ tự vòng $0,1$ và $1,0$ cho trùng, không trùng, trung bình $1/2=\mathrm{SIM}$: cần ít nhất một hàng ngoài hợp. Trên ma trận Hình 3.2 với thứ tự hàng a, b, c, d, e, năm hoán vị vòng cho cặp $S_1$, $S_3$ tỷ lệ $2/5\ne1/4$ và cặp $S_1$, $S_4$ tỷ lệ $3/5\ne2/3$.
:::

::: exercise Bài tập 05.27 (Kỳ vọng Jaccard của hai tập con ngẫu nhiên; MMDS Bài 3.1.3 (!!), §3.1.4, tr.78, và Bài 3.3.4 (!), §3.3.8, tr.91)
Vũ trụ $U$ có $R$ phần tử. Chọn hai tập con $S$, $T$ độc lập, mỗi tập chọn đều trong các tập con gồm đúng $q$ phần tử của $U$, với $1\le q\le R$.

- (a) Tính kỳ vọng của $\mathrm{SIM}(S,T)$ (Bài 3.1.3).
- (b) Dùng quan hệ giữa Jaccard và xác suất trùng MinHash để tính lại kỳ vọng này (Bài 3.3.4).
:::

::: hint
Câu (a): phân phối của $K=|S\cap T|$ khi $S$ cố định là phân phối siêu bội. Câu (b): theo Định lý 05.10, $\mathbb E[\mathrm{SIM}(S,T)]$ là xác suất trùng MinHash khi $\pi$ cũng chọn ngẫu nhiên; cố định $\pi$ và tìm phân phối của hạng nhỏ nhất của $S$.
:::

::: solution
**Câu (a).** Cố định $S$; $T$ chọn đều trong $\binom Rq$ tập con. Số tập $T$ có đúng $x$ phần tử chung với $S$ là $\binom qx\binom{R-q}{q-x}$, nên
$$
\Pr[K=x]=\frac{\binom qx\binom{R-q}{q-x}}{\binom Rq}.
$$
Khi $|S\cap T|=x$, $|S\cup T|=2q-x$ và $\mathrm{SIM}(S,T)=x/(2q-x)$. Phân phối này không phụ thuộc $S$, nên
$$
\mathbb E[\mathrm{SIM}(S,T)]=\sum_{x=0}^{q}\Pr[K=x]\cdot\frac{x}{2q-x}.
$$

**Câu (b).** Chọn thêm $\pi$ đều, độc lập với $S$, $T$. Theo Định lý 05.10 cho từng cặp $S$, $T$ cố định, cả hai không rỗng vì $q\ge1$, rồi lấy kỳ vọng theo $S$, $T$,
$$
\mathbb E[\mathrm{SIM}(S,T)]=\Pr\bigl[h_\pi(S)=h_\pi(T)\bigr],
$$
với xác suất lấy theo $S$, $T$ và $\pi$. Cố định $\pi$. Hạng nhỏ nhất của $S$ bằng $j$ khi $S$ chứa phần tử hạng $j$ và $q-1$ phần tử còn lại nằm trong $R-j$ phần tử có hạng lớn hơn, nên
$$
\Pr\Bigl[\min_{u\in S}\operatorname{rank}_\pi(u)=j\Bigr]=\frac{\binom{R-j}{q-1}}{\binom Rq}
$$
với $j=1,\ldots,R-q+1$. Với $\pi$ cố định, $h_\pi(S)=h_\pi(T)$ khi và chỉ khi hai hạng nhỏ nhất bằng nhau; $S$, $T$ độc lập, nên
$$
\mathbb E[\mathrm{SIM}(S,T)]=\sum_{j=1}^{R-q+1}\left(\frac{\binom{R-j}{q-1}}{\binom Rq}\right)^2 .
$$
Vế phải không phụ thuộc $\pi$, nên đúng cả khi $\pi$ ngẫu nhiên. Công thức này chỉ cần tổng các bình phương, không cần tỷ số $x/(2q-x)$ của câu (a).

**Kiểm tra lại.** Với $R=4$, $q=2$: câu (a) cho $\Pr[K=0]=1/6$, $\Pr[K=1]=4/6$, $\Pr[K=2]=1/6$, nên kỳ vọng là $\tfrac46\cdot\tfrac13+\tfrac16\cdot1=\tfrac7{18}$; câu (b) cho $(3^2+2^2+1^2)/6^2=14/36=7/18$.
:::

::: exercise Bài tập 05.28 (Trung bình theo nửa trên và nửa dưới; MMDS Bài 3.3.9 (!!), §3.3.8, tr.91; Đọc thêm)
Trong Ví dụ 05.16 (MMDS Ví dụ 3.9), mỗi ước lượng Jaccard thu được bằng trung bình Jaccard của nửa trên và nửa dưới các hàng đều nhỏ hơn hoặc bằng Jaccard thật. Xác định có tồn tại một cặp cột của một ma trận tám hàng, chia thành nửa trên $P_1=\{0,1,2,3\}$ và nửa dưới $P_2=\{4,5,6,7\}$, mà trung bình Jaccard của hai nửa lớn hơn Jaccard thật hay không; nếu có, cho một ví dụ.
:::

::: hint
Trung bình không trọng số của hai tỷ số có thể khác tỷ số của tổng, như ở Ví dụ 05.16.
:::

::: solution
Có. Cho $S_1$ có ô 1 ở các hàng $0,4,5,6$ và $S_2$ có ô 1 ở các hàng $0,4$.

| Phạm vi | Giao | Hợp | Jaccard |
|---|---|---|---|
| Nửa trên $P_1$ | $\{0\}$ | $\{0\}$ | $1$ |
| Nửa dưới $P_2$ | $\{4\}$ | $\{4,5,6\}$ | $1/3$ |
| Toàn bộ | $\{0,4\}$ | $\{0,4,5,6\}$ | $1/2$ |

Trung bình hai nửa là $\tfrac12\bigl(1+\tfrac13\bigr)=\tfrac23>\tfrac12$. Trung bình không trọng số cho nửa trên, với hợp chỉ một phần tử, cùng trọng số với nửa dưới, với hợp ba phần tử (Ví dụ 05.16).

**Kiểm tra lại.** Trung bình có trọng số theo kích thước hợp, $\tfrac14\cdot1+\tfrac34\cdot\tfrac13=\tfrac12$, đúng Jaccard toàn bộ.
:::
