# Bài 05 — Biểu diễn tương đồng: Shingling và MinHash

Trong chương này, chúng ta biểu diễn mỗi tài liệu bằng tập các đoạn ký tự liên tiếp (shingle), thay tập ấy bằng một chữ ký MinHash ngắn sao cho tỷ lệ tọa độ trùng của hai chữ ký ước lượng được Jaccard của hai tập, rồi tính mọi chữ ký bằng một lượt quét các hàng của ma trận đặc trưng.

[Bộ trang chiếu Bài 05](lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html) trình bày cùng ký hiệu và dữ kiện; [tệp bài tập Bài 05](material-viewer.html?doc=materials/lec-05/exercises.md&deck=lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Tách tổng công việc tìm cặp gần trùng (near-duplicate) thành số cặp nhân chi phí một cặp, và đọc độ tương đồng Jaccard theo cách chọn phần tử của tập (Mục 1).
2. Lập tập $k$-shingle của một chuỗi theo một quy ước khoảng trắng, chứng minh tính đúng và đếm chi phí của thuật toán tạo tập shingle, và nêu điều kiện để mã băm của shingle giữ nguyên Jaccard (Mục 2).
3. Lập ma trận đặc trưng (characteristic matrix), tính MinHash theo một hoán vị (permutation) và chứng minh rằng hai tập trùng MinHash với xác suất bằng Jaccard của chúng (Mục 3).
4. Lập chữ ký MinHash (MinHash signature), ước lượng Jaccard từ hai chữ ký, chứng minh ước lượng không chệch (unbiased) và đếm chi phí so hai chữ ký (Mục 4.1–4.3).
5. Tính phương sai của ước lượng dưới giả thiết độc lập và chọn độ dài chữ ký theo độ lệch chuẩn cần đạt (Mục 4.4).
6. Chạy thuật toán quét hàng bằng tay, chứng minh bất biến của nó và đếm thời gian, bộ nhớ (Mục 5.1–5.4).
7. Kiểm điều kiện để một hàm affine modulo $R$ là hoán vị, và nêu hậu quả khi một giả thiết bị vi phạm: va chạm mã, tập rỗng, họ hàm không chọn đều trên mọi hoán vị (Mục 5.5, Tình huống 05.2, 05.3).

## Kiến thức tiên quyết

Số hiệu `01.k` chỉ ghi chú Bài 01; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Độ tương đồng Jaccard** (Định nghĩa 01.9; Ví dụ 01.6). Với hai tập hữu hạn $S,T$ có $S\cup T\ne\varnothing$, độ tương đồng Jaccard là $\mathrm{SIM}(S,T)=|S\cap T|/|S\cup T|$. Ta có $0\le\mathrm{SIM}(S,T)\le1$; $\mathrm{SIM}(S,T)=1$ khi và chỉ khi $S=T$, và $\mathrm{SIM}(S,T)=0$ khi và chỉ khi $S\cap T=\varnothing$. Khi $S=T=\varnothing$, biểu thức là $0/0$ và không xác định. Hai tập của MMDS Hình 3.1, với hai phần tử chỉ thuộc tập thứ nhất, ba phần tử chung và ba phần tử chỉ thuộc tập thứ hai, có Jaccard $3/8$.
- **Bài toán tìm cặp gần trùng** (Định nghĩa 01.10). Cho các tập hữu hạn, không rỗng của các tài liệu và một ngưỡng, trả mọi cặp chỉ số $(i,j)$ với $i<j$ có Jaccard không nhỏ hơn ngưỡng, mỗi cặp một lần.
- **Xét mọi cặp và chi phí của nó** (Thuật toán 01.11; Bổ đề 01.14; Mệnh đề 01.15; Ví dụ 01.8). Thuật toán xét đủ $\binom C2=C(C-1)/2$ cặp; với $C=10^6$ có $499\,999\,500\,000$ cặp. Với hai tập lưu thành danh sách tăng ngặt, thủ tục trộn tính giao và hợp của một cặp bằng không quá $|S|+|T|$ phép so sánh phần tử (Bổ đề 01.14), nên tổng chi phí là số cặp nhân chi phí một cặp (Mệnh đề 01.15).
- **Hàm băm** (Định nghĩa 01.8). Một hàm băm (hash function) nhận một khóa và trả một số thùng trong $\{0,1,\ldots,B-1\}$; một hàm băm đã chọn luôn trả cùng số thùng cho cùng khóa.
- **Mô hình chi phí và lượt quét** (Định nghĩa 01.13; Định nghĩa 01.4). Một mô hình chi phí chọn một đại lượng (khối lượng tính toán, bộ nhớ làm việc, dung lượng lưu trữ, …) và đơn vị đếm nó; các đại lượng khác nhau không cộng với nhau. Một lượt quét (pass) trên một tệp đọc mỗi khối của tệp đúng một lần.
- **Bất biến vòng lặp** (chứng minh Mệnh đề 01.12). Một bất biến vòng lặp (loop invariant) là một khẳng định về trạng thái đúng trước lượt đầu (khởi tạo), được giữ qua mỗi lượt (duy trì) và cho điều cần chứng minh khi vòng lặp dừng (kết thúc).
- **Kỳ vọng, phương sai và biến chỉ báo** (học phần Xác suất thống kê). Kỳ vọng của một tổng bằng tổng các kỳ vọng, không cần độc lập. Một biến chỉ báo (indicator variable) nhận giá trị 1 với xác suất $p$ và 0 với xác suất $1-p$ có kỳ vọng $p$ và phương sai $p(1-p)$. Với hằng số $a$, $\operatorname{Var}(aY)=a^2\operatorname{Var}(Y)$; hai biến độc lập có hiệp phương sai bằng 0, nên phương sai của tổng các biến độc lập bằng tổng các phương sai.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; chữ chỉ dùng trong một ví dụ, một chứng minh hay một bài tập được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $C$; $c$ | số tài liệu (số tập, số cột); chỉ số cột | số nguyên dương; $1\le c\le C$ |
| $S_c$; $S$, $T$ | tập phần tử của tài liệu $c$; hai tập của một cặp đang xét | tập con hữu hạn của $U$ |
| $\mathrm{SIM}(S,T)$ | độ tương đồng Jaccard (Định nghĩa 01.9) | $[0,1]$, cần $S\cup T\ne\varnothing$ |
| $t$ | ngưỡng tương đồng của bài toán tìm cặp gần trùng | $[0,1]$ |
| $D$; $\ell$ | một tài liệu, xem như chuỗi ký tự; độ dài của $D$ | chuỗi; số nguyên $\ge0$ |
| $k$; $D[j:j+k]$ | độ dài shingle; đoạn gồm các ký tự ở vị trí $j,\ldots,j+k-1$ | $k\ge1$; chuỗi dài $k$ |
| $S_k(D)$; $w$ | tập $k$-shingle của $D$; số cửa sổ, $w=\max(0,\ell-k+1)$ | tập chuỗi dài $k$; số nguyên $\ge0$ |
| $g$ | hàm mã hóa shingle thành mã 4 byte | chuỗi dài $k$ $\to\{0,\ldots,2^{32}-1\}$ |
| $U$; $R$; $r$ | vũ trụ phần tử; $R=\lvert U\rvert$; mã hàng của một phần tử | tập hữu hạn; $R\ge1$; $0\le r\le R-1$ |
| $M$; $L$ | ma trận đặc trưng; số ô 1 của $M$, $L=\operatorname{nnz}(M)$ | $\{0,1\}^{R\times C}$; $0\le L\le RC$ |
| $\pi$; $\operatorname{rank}_\pi(u)$ | hoán vị của $U$; hạng (vị trí) của $u$ trong thứ tự $\pi$ | song ánh; $\{1,\ldots,R\}$ |
| $h_\pi(S)$ | MinHash của $S$: phần tử của $S$ đứng đầu theo $\pi$ | phần tử của $S$, cần $S\ne\varnothing$ |
| $A$; $u$ | tập con khác rỗng của $U$ trong Bổ đề 05.9; phần tử đứng đầu của $S\cup T$ theo $\pi$ | $A\subseteq U$; $u\in S\cup T$ |
| $x$; $y$ | $\lvert S\cap T\rvert$; $\lvert S\cup T\rvert-\lvert S\cap T\rvert$ | số nguyên $\ge0$ |
| $\mathrm X$, $\mathrm Y$, $\mathrm Z$ | ba loại hàng của một cặp cột: thuộc giao, thuộc đúng một tập, ngoài hợp | nhãn loại hàng |
| $n$; $\pi_1,\ldots,\pi_n$ | độ dài chữ ký; các hoán vị của chữ ký | $n\ge1$ |
| $\sigma(S)$ | chữ ký MinHash của $S$ | véc-tơ cột dài $n$ |
| $\mathbf 1[E]$; $I_i$ | chỉ báo của mệnh đề $E$; $\mathbf 1[h_{\pi_i}(S)=h_{\pi_i}(T)]$ | $\{0,1\}$ |
| $s$; $\widehat s$ | $\mathrm{SIM}(S,T)$ của cặp đang xét; ước lượng $\widehat{\mathrm{SIM}}(S,T)$ | $[0,1]$; $\{0,1/n,\ldots,1\}$ |
| $\Pr$; $\mathbb E$; $\operatorname{Var}$ | xác suất, kỳ vọng, phương sai theo cách chọn hoán vị (hoặc hàm) | số thực |
| $f_i$; $V$; $+\infty$ | hàm băm hàng thứ $i$; miền giá trị của $f_i$; giá trị canh (sentinel) lớn hơn mọi phần tử của $V$ | $\{0,\ldots,R-1\}\to V$; tập hữu hạn có thứ tự toàn phần |
| $\mathrm{SIG}$; $v_i$ | ma trận chữ ký tính bằng hàm băm; giá trị $f_i(r)$ của hàng đang quét | $(V\cup\{+\infty\})^{n\times C}$; $V$ |
| $\alpha$, $\beta$ | hệ số của hàm affine $(\alpha r+\beta)\bmod R$ | số nguyên |
| $m$; $P$ | số hàng được xét trong một phép thử rút gọn; tập mã hàng của một nhóm hàng (Đọc thêm) | $1\le m<R$; $P\subseteq\{0,\ldots,R-1\}$ |

Các quy ước đọc sau dùng trong cả chương.

- Vị trí ký tự, mã hàng và vị trí bắt đầu cửa sổ đếm từ 0; hạng trong một hoán vị, chỉ số cột $c$ và chỉ số hàm $i$ đếm từ 1.
- Số thập phân dùng dấu phẩy, ví dụ $0{,}032$; số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $499\,999\,500\,000$, hoặc viết dạng lũy thừa.
- Tên phần tử viết chữ đứng, như phần tử $\mathrm a$ và tập $S_1=\{\mathrm a,\mathrm d\}$; trong bảng, tên phần tử viết a, b, c, d, e. Chuỗi viết bằng phông chữ máy, như `abcdabd`; ký hiệu ␣ chỉ một dấu cách khi cần nhìn thấy nó.
- $S_c$ với chỉ số là số hiệu cột chỉ tập của tài liệu $c$; tập shingle luôn được viết kèm tài liệu, $S_k(D)$.
- Bài 01 viết số tài liệu là $N$, tập của tài liệu thứ $i$ là $C_i$ và ngưỡng là $\tau$; ở đây là $C$, $S_c$ và $t$, theo MMDS. Bài 01 còn dùng $L$ cho cận số phần tử của một tập, $R$ cho tập kết quả và $M$ cho số khối của bộ nhớ chính; ở đây $L=\operatorname{nnz}(M)$, $R=\lvert U\rvert$ và $M$ là ma trận đặc trưng.
- MMDS viết độ dài tài liệu là $n$, hàm băm hàng là $h_i$, số hàng ở §3.3.6–3.3.7 là $k$ và nhóm hàng là $T$; ở đây là $\ell$, $f_i$, $R$ và $P$, vì $n$ là độ dài chữ ký, $h_\pi$ là MinHash, $k$ là độ dài shingle và $T$ là một tập của cặp đang xét.
- Viết tắt nguồn: MMDS (*Mining of Massive Datasets*, ấn bản 3); CS246 chỉ bài giảng LSH I của Stanford CS246; số trang là trang in của MMDS; chi tiết ở mục tài liệu tham khảo.

<!-- note-topic-id: lec-05-topic-01 -->
## 1. Tài liệu gần trùng và hai thừa số của chi phí

Thuật toán 01.11 trả đúng mọi cặp tài liệu gần trùng bằng cách xét đủ các cặp và tính Jaccard trên hai tập đầy đủ (Mệnh đề 01.12); chi phí của nó là số cặp nhân chi phí một cặp (Bổ đề 01.14, Mệnh đề 01.15).

Nhu cầu tìm tài liệu gần trùng xuất hiện ở nhiều dạng (MMDS, tr.73; §3.1.2, tr.75–76), bao gồm:

- **trang phản chiếu:** một trang được sao sang máy chủ khác, giữ phần lớn nội dung và chỉ đổi thông tin về máy chủ;
- **đạo văn:** một bài đổi vài từ hoặc đổi thứ tự câu nhưng giữ phần lớn văn bản gốc;
- **bản tin đăng lại:** một bản tin xuất hiện ở nhiều trang báo, với một số đoạn bị lược hoặc thêm vào.

Kiểm tra hai chuỗi bằng nhau chỉ nhận ra trường hợp trùng hoàn toàn. Giả sử bản tin gốc có hai câu, và bản đăng lại giữ nguyên hai câu ấy nhưng chèn một câu ở giữa.

![Bản tin gốc có hai câu; bản đăng lại giữ nguyên hai câu ấy và chèn thêm một câu ở giữa. Câu chung có nền xanh, viền liền; câu thêm có viền đứt và nhãn “thêm”. Hai chuỗi khác nhau từ đầu câu thứ hai.](img/lec-05/ban-tin-dang-lai.svg)

Trên hình, hai chuỗi khác nhau từ ký tự đầu của câu thứ hai, nên phép so từng ký tự kết luận hai tài liệu khác nhau, dù hai trong ba câu là chung. Bài toán gần trùng cần một số đo cho phần văn bản chung của hai tài liệu còn có khác biệt. Số đo của chương là Jaccard trên tập các đoạn con ở mức ký tự, và cách biểu diễn cùng quy tắc xử lý văn bản phải được chọn trước khi tính số đo.

Bài toán trung tâm của chương là ước lượng Jaccard của mọi cặp trong một kho $10^6$ tài liệu với dữ liệu nằm trong bộ nhớ chính. Một tài liệu $50\,000$ byte cho tập mã shingle khoảng $200\,000$ byte (MMDS, tr.81), nên tập mã của cả kho chiếm khoảng $10^6\cdot200\,000=2\cdot10^{11}$ byte; so trực tiếp một cặp tập mã tốn không quá $|S|+|T|$ phép so sánh (Bổ đề 01.14). Chúng ta xây dựng ba thứ: một cách biến mỗi tài liệu thành một tập, một chữ ký ngắn của tập mà từ đó ước lượng được Jaccard, và một thuật toán tính chữ ký cho cả kho trong một lượt đọc dữ liệu. Hình sau cho cấu trúc của chương.

![Sơ đồ cấu trúc chương, đọc từ trên xuống. Khối trên cùng: bài toán trung tâm, kho 10⁶ tài liệu, 499 999 500 000 cặp, tập mã shingle khoảng 200 000 byte mỗi tài liệu. Năm mũi tên xuống năm cột; mỗi cột ghi câu hỏi của mục và, dưới đường kẻ đứt, các khái niệm chính. Mục 1: tổng công việc gồm những thừa số nào; số cặp, chi phí một cặp, Jaccard. Mục 2: biến văn bản thành tập thế nào; tập k-shingle, khoảng trắng, mã 4 byte. Mục 3: một phép thử nào giữ Jaccard; ma trận đặc trưng, MinHash, xác suất trùng bằng SIM. Mục 4: ước lượng chính xác đến đâu; chữ ký, kỳ vọng s, phương sai s(1 − s)/n. Mục 5: tính chữ ký cho cả kho thế nào; hàm băm hàng, quét hàng, chi phí theo n, C, R, L. Hàng dưới: ô đọc thêm viền nét đứt dưới Mục 2 (đa tập, shingle theo từ dừng); mũi tên từ Mục 5 tới khối viền đậm "Bài 06: giảm số cặp phải so"; ô đọc thêm viền nét đứt dưới Mục 5 (rút ngắn phép quét).](img/lec-05/note-cau-truc-chuong-05.svg)

Sơ đồ đọc từ trên xuống. Khối trên cùng ghi bài toán trung tâm. Cột Mục 1 ghi hai thừa số của chi phí; bốn cột Mục 2 đến Mục 5 ghi các bước xử lý thừa số chi phí một cặp, theo thứ tự tập, phép thử, chữ ký, thuật toán tính chữ ký. Hai ô đọc thêm có viền nét đứt; cả hai nằm trong một phần đọc thêm thu gọn sau Mục 5. Mũi tên cuối chỉ thừa số còn lại, số cặp, thuộc Bài 06.

### 1.1 Số cặp và chi phí một cặp

Ví dụ sau so chi phí một cặp trên tập mã với chi phí một cặp trên chữ ký, ở quy mô của MMDS.

::: example Ví dụ 05.1 (Kho một triệu tài liệu; MMDS Ví dụ 3.10, tr.92, và tr.81)
**Dữ kiện.** Kho có $C=10^6$ tài liệu, tức $499\,999\,500\,000$ cặp (Ví dụ 01.8). Mỗi tập mã chiếm khoảng $200\,000$ byte, tức khoảng $50\,000$ mã 4 byte, và được lưu thành danh sách tăng ngặt; mỗi chữ ký có $n=250$ thành phần, và so một cặp chữ ký mất 1 micro giây.

**Chi phí một cặp.** Trên tập mã, Bổ đề 01.14 cho không quá $50\,000+50\,000=100\,000$ phép so sánh; trên chữ ký, $250$ phép so bằng.

**Tổng.** Trên tập mã, không quá $499\,999\,500\,000\cdot100\,000\approx5\cdot10^{16}$ phép so sánh; trên chữ ký, $499\,999\,500\,000\cdot250\approx1{,}25\cdot10^{14}$ phép so bằng. Với 1 micro giây mỗi cặp chữ ký, tổng thời gian là $499\,999{,}5$ giây, khoảng $5{,}79$ ngày trên một máy.

**Kiểm tra lại.** $100\,000/250=400$, và $1{,}25\cdot10^{14}\cdot400=5\cdot10^{16}$.
:::

Chữ ký làm giảm dung lượng và chi phí so **một cặp**, nên chúng ta nhắm vào thừa số thứ hai. Số cặp $\binom C2$ không đổi khi chỉ thay biểu diễn.

<!-- note-topic-id: lec-05-topic-02 -->
### 1.2 Jaccard trên tập phần tử đã chọn

Biểu diễn tài liệu bằng tập hợp tách hai đại lượng: số phần tử chung và số phần tử xuất hiện ở ít nhất một tập. Tỷ số của chúng là độ tương đồng Jaccard của Định nghĩa 01.9,
$$
\mathrm{SIM}(S,T)=\frac{|S\cap T|}{|S\cup T|},\qquad S\cup T\ne\varnothing,
$$
trong đó $|\cdot|$ chỉ số phần tử của một tập. Phép hợp đếm mỗi phần tử một lần, kể cả khi phần tử ấy thuộc cả hai tập; trong Ví dụ 01.6, $|S|+|T|=5+6=11$ lớn hơn $|S\cup T|=8$ vì ba phần tử giao bị đếm hai lần. Mẫu số là kích thước hợp, nên số phần tử chung được so với kích thước của cả cặp: ba phần tử chung trong hai tập năm phần tử cho Jaccard lớn hơn ba phần tử chung trong hai tập một nghìn phần tử.

Định nghĩa 01.9 cho một số khi đã có hai tập. Giá trị đó phụ thuộc vào việc chọn phần tử là gì, và ngưỡng có ý nghĩa cũng phụ thuộc ứng dụng.

::: remark Nhận xét 05.1 (Phần tử của tập và ngưỡng $t$ theo ứng dụng)
- Với văn bản, phần tử có thể là các đoạn con liên tiếp có độ dài cố định. Tập hợp không lưu số lần một phần tử xuất hiện.
- Với khách hàng của một cửa hàng trực tuyến, phần tử có thể là mặt hàng đã mua (MMDS, §3.1.3, tr.76).
- MMDS dự đoán hai trang phản chiếu có Jaccard trên $90\%$; với hai khách hàng, Jaccard $20\%$ có thể đã đủ bất thường để xem hai người có sở thích tương tự (§3.1.3, tr.76).
- Đặt ngưỡng của Định nghĩa 01.10 theo các mức này, ta có $t\approx0{,}9$ cho trang phản chiếu và $t=0{,}2$ cho khách hàng; một ngưỡng chỉ có nghĩa cùng với cách chọn phần tử đã dùng để lập tập.
:::

::: exercise Bài tập 05.1 (Chữ ký dài $n$ vẫn xét mọi cặp)
Một phương pháp thay mỗi tài liệu bằng một véc-tơ có $n$ thành phần và so hai véc-tơ bằng $n$ phép so bằng giữa các thành phần cùng vị trí. Nếu vẫn xét mọi cặp của kho $C$ tài liệu, xác định số phép so bằng theo $C$ và $n$, và chỉ ra thừa số không đổi khi giảm $n$.
:::

::: hint
Nhân số cặp không thứ tự với số phép so của một cặp.
:::

::: solution
Mỗi cặp dùng $n$ phép so bằng, và có $\binom C2=C(C-1)/2$ cặp, nên tổng là
$$
n\cdot\frac{C(C-1)}2 .
$$
Giảm $n$ chỉ giảm chi phí một cặp; thừa số $C(C-1)/2$, bậc hai theo $C$, không đổi.

**Kiểm tra lại.** Với $C=10^6$ và $n=250$, biểu thức bằng $250\cdot499\,999\,500\,000\approx1{,}25\cdot10^{14}$, đúng tổng trên chữ ký của Ví dụ 05.1.
:::

::: exercise Bài tập 05.2 (Thêm phần tử vào một tập)
Cho hai tập $S$, $T$ của Ví dụ 01.6: hai phần tử chỉ thuộc $S$, ba phần tử thuộc cả hai, ba phần tử chỉ thuộc $T$.

- (a) Thêm vào $T$ hai phần tử mới không thuộc $S$. Tính lại $\mathrm{SIM}(S,T)$.
- (b) Giải thích vì sao độ dài của hai chuỗi văn bản không đủ để xác định Jaccard giữa hai văn bản.
:::

::: hint
Câu (a): xác định xem giao hay hợp thay đổi. Câu (b): Jaccard cần biết những phần tử nào chung.
:::

::: solution
**Câu (a).** Giao vẫn có 3 phần tử; hợp tăng từ 8 lên 10. Do đó $\mathrm{SIM}(S,T)=3/10$. Giá trị giảm vì mẫu số tăng còn tử số giữ nguyên.

**Câu (b).** Định nghĩa 01.9 cần các phần tử của hai tập để lập giao và hợp. Độ dài chuỗi chỉ cho số ký tự, nên không xác định tập phần tử, cũng không xác định phần tử nào chung; phải chọn trước một quy tắc biến mỗi chuỗi thành một tập.

**Kiểm tra lại.** Câu (a): $|T|=6+2=8$ và $|S|+|T|-|S\cap T|=5+8-3=10$.
:::

Chi phí đã tách thành số cặp nhân chi phí một cặp (Ví dụ 05.1), và Jaccard chỉ có nghĩa khi cách chọn phần tử đã cố định (Nhận xét 05.1). Còn thiếu một quy tắc biến văn bản thành tập; trong Mục 2, chúng ta chọn phần tử là các đoạn $k$ ký tự liên tiếp.

<!-- note-topic-id: lec-05-topic-03 -->
## 2. Shingling: chuyển chuỗi thành tập

Bản tin đăng lại giữ nguyên hai câu của bản gốc nhưng khác bản gốc từ ký tự đầu của câu thứ hai, nên hai chuỗi không bằng nhau. Chúng ta cần một tập phần tử sao cho hai tài liệu chung nhiều câu hoặc cụm từ thì chung nhiều phần tử, kể cả khi các câu ấy xuất hiện theo thứ tự khác nhau (MMDS, mở đầu §3.2, tr.78). Cách đơn giản nhất là lấy mọi đoạn ngắn có độ dài cố định xuất hiện trong tài liệu.

### 2.1 Tập $k$-shingle

Ví dụ sau trượt một cửa sổ dài hai ký tự dọc một chuỗi bảy ký tự và giữ mỗi đoạn một lần.

::: example Ví dụ 05.2 (Tập 2-shingle của `abcdabd`; MMDS Ví dụ 3.3, tr.78)
**Dữ kiện.** $D=\texttt{abcdabd}$, $\ell=7$, $k=2$; các ký tự ở vị trí $0,\ldots,6$.

**Các cửa sổ.** Vị trí bắt đầu chạy từ 0 đến $\ell-k=5$, nên có sáu cửa sổ. Cột cuối ghi tập sau khi chèn cửa sổ của dòng đó.

| Vị trí bắt đầu $j$ | Cửa sổ | Tập sau phép chèn |
|---:|---|---|
| 0 | `ab` | {`ab`} |
| 1 | `bc` | {`ab`, `bc`} |
| 2 | `cd` | {`ab`, `bc`, `cd`} |
| 3 | `da` | {`ab`, `bc`, `cd`, `da`} |
| 4 | `ab` | {`ab`, `bc`, `cd`, `da`} |
| 5 | `bd` | {`ab`, `bc`, `cd`, `da`, `bd`} |

**Kết quả.** Cửa sổ ở vị trí 4 trùng cửa sổ ở vị trí 0 nên không làm tập lớn thêm:
$$
\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da},\texttt{bd}\}.
$$

**Kiểm tra lại.** Sáu cửa sổ, năm phần tử phân biệt; hiệu bằng một, đúng số lần lặp của `ab`.
:::

![Chuỗi abcdabd có bảy ký tự ở vị trí 0 đến 6. Sáu cửa sổ dài hai lần lượt là ab, bc, cd, da, ab, bd. Hai cửa sổ ab cùng tạo một phần tử của tập shingle.](img/lec-05/cua-so-shingle.svg)

Trên hình, mỗi cửa sổ là một khung dài hai ô bắt đầu ở một vị trí; hai khung `ab` ở vị trí 0 và 4 cùng trỏ tới một phần tử của tập. Định nghĩa sau ghi lại phép lập tập này cho mọi chuỗi và mọi độ dài cửa sổ.

::: definition Định nghĩa 05.2 (Cửa sổ và tập $k$-shingle)
Cho chuỗi ký tự $D$ dài $\ell\ge0$, các ký tự đánh số từ $0$ đến $\ell-1$, và số nguyên $k\ge1$.

- Với $0\le j\le\ell-k$, *cửa sổ* (window) tại vị trí $j$ là đoạn $D[j:j+k]$ gồm các ký tự ở vị trí $j,j+1,\ldots,j+k-1$; vị trí $j+k$ không được lấy.
- Một *$k$-shingle* (còn gọi là $k$-gram) của $D$ là một chuỗi dài $k$ xuất hiện như một cửa sổ của $D$ (MMDS, §3.2.1, tr.78; tên $k$-gram: trang chiếu MMDS, tr.20; CS246, trang chiếu 18).
- *Tập $k$-shingle* của $D$ là
$$
S_k(D)=\{D[j:j+k]:0\le j\le\ell-k\}.
$$
:::

Tập $S_k(D)$ là một tập hợp theo nghĩa của Định nghĩa 01.9, nên Jaccard của hai tài liệu được tính trên hai tập shingle của chúng. Định nghĩa có ba hệ quả trực tiếp.

- Nếu $\ell<k$, không có vị trí bắt đầu hợp lệ và $S_k(D)=\varnothing$.
- Nếu $k\le\ell$, số cửa sổ là $\ell-k+1$; viết chung cho mọi $\ell$, số cửa sổ là $w=\max(0,\ell-k+1)$.
- Mỗi cửa sổ cho nhiều nhất một phần tử, nên $|S_k(D)|\le w$; dấu bằng xảy ra khi và chỉ khi các cửa sổ đôi một khác nhau. Ví dụ 05.2 là trường hợp $\ell=7$, $k=2$, $w=6$ và $|S_2(D)|=5$.

Ở trường hợp giới hạn $k=1$, tập shingle là tập các ký tự của tài liệu; hầu hết trang web chứa hầu hết các ký tự thông dụng, nên gần như mọi cặp trang có Jaccard cao (MMDS, §3.2.2, tr.79). Vì vậy $k$ quá nhỏ làm mất khả năng phân biệt giữa các tài liệu.

Một cách trực quan, shingling giữ thứ tự ký tự bên trong mỗi đoạn dài $k$, còn thứ tự giữa các đoạn và số lần lặp thì không được lưu. Những đoạn nằm trọn trong phần văn bản không bị sửa xuất hiện ở cả hai phiên bản, nên tạo phần tử chung, kể cả khi các câu đổi chỗ. Thay ký tự ở vị trí $j_0$ chỉ đổi các cửa sổ chứa vị trí ấy, tức các cửa sổ bắt đầu từ $\max(0,j_0-k+1)$ đến $\min(j_0,\ell-k)$, nhiều nhất $k$ cửa sổ. Để làm rõ điều này, xem ví dụ sau.

::: example Ví dụ 05.3 (Một ký tự đổi: `abcxabd`)
**Dữ kiện.** $D=\texttt{abcdabd}$, $D'=\texttt{abcxabd}$, $k=2$; hai chuỗi chỉ khác nhau ở vị trí $3$.

**Cửa sổ đổi.** Các cửa sổ chứa vị trí 3 bắt đầu tại $2$ và $3$: `cd`, `da` của $D$ thành `cx`, `xa` của $D'$. Bốn cửa sổ còn lại trùng nhau.

**Hai tập.** $S_2(D)=\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da},\texttt{bd}\}$ và $S_2(D')=\{\texttt{ab},\texttt{bc},\texttt{cx},\texttt{xa},\texttt{bd}\}$. Giao có 3 phần tử, hợp có 7, nên
$$
\mathrm{SIM}\bigl(S_2(D),S_2(D')\bigr)=\frac37 .
$$

**Kiểm tra lại.** Số cửa sổ đổi là $\min(3,5)-\max(0,2)+1=2\le k$; $|S_2(D)|+|S_2(D')|-3=5+5-3=7$.
:::

Một ký tự đổi trong bảy ký tự đã hạ Jaccard xuống $3/7$, vì hai trong sáu cửa sổ đổi. Với tài liệu $50\,000$ ký tự và $k=9$, cùng một thay đổi cục bộ đổi nhiều nhất 9 trong $49\,992$ cửa sổ.

### 2.2 Thuật toán tạo tập shingle

Bảng của Ví dụ 05.2 là một lượt chạy tay: duyệt vị trí bắt đầu từ trái sang phải và chèn từng cửa sổ vào một tập. Thuật toán sau làm đúng việc đó; thao tác quyết định là phép chèn vào tập, vốn giữ một bản của mỗi chuỗi.

::: algorithm Thuật toán 05.3 (Tạo tập shingle)
**Đầu vào.** Chuỗi $D$ dài $\ell\ge0$; số nguyên $k\ge1$.

**Đầu ra.** Tập $S_k(D)$ của Định nghĩa 05.2.

**Giả thiết.** Tập $S$ được cài bằng bảng băm các chuỗi: phép chèn một chuỗi dài $k$ giữ đúng một bản của mỗi chuỗi và tốn thời gian kỳ vọng $O(k)$.

1. Đặt $S\leftarrow\varnothing$.
2. Với $j=0,1,\ldots,\ell-k$: chèn $D[j:j+k]$ vào $S$.
3. Trả $S$.

**Dừng.** Bước 2 chạy đúng $w=\max(0,\ell-k+1)$ lần rồi dừng.

**Trường hợp biên.** Nếu $\ell<k$, bước 2 không chạy lần nào và thuật toán trả $\varnothing$.

**Chi phí.** Mô hình: tạo một cửa sổ dài $k$ tốn $O(k)$; chèn tốn $O(k)$ kỳ vọng.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1 (khởi tạo) | 1 | $O(1)$ | $O(1)$ |
| 2 (tạo và chèn cửa sổ) | $w$ | $O(k)$ kỳ vọng | $O(wk)$ kỳ vọng |
| 3 (trả) | 1 | $O(1)$ | $O(1)$ |

Tổng thời gian kỳ vọng là $O(1+wk)$; bộ nhớ của tập là $O(k\,|S_k(D)|)$ ký tự, chưa tính đầu vào.
:::

```text
S ← ∅
for j = 0, …, ℓ − k:
    chèn D[j:j+k] vào S
return S
```

Giả mã dùng đúng ký hiệu của Ví dụ 05.2: với `abcdabd` và $k=2$, vòng lặp chạy $j=0,\ldots,5$, và trạng thái của $S$ sau mỗi vòng là cột cuối của bảng. Quy ước khoảng trắng của $D$ được chọn trước khi chạy thuật toán.

::: proposition Mệnh đề 05.4 (Tính đúng và chi phí của Thuật toán 05.3)
**Giả thiết.** Đầu vào và giả thiết của Thuật toán 05.3.

**Kết luận.**

- (a) Thuật toán dừng và trả đúng $S_k(D)$.
- (b) $|S_k(D)|\le w=\max(0,\ell-k+1)$.
- (c) Thời gian kỳ vọng là $O(1+wk)$.

**Điều kiện áp dụng.** Kỳ vọng ở (c) lấy theo hàm băm của bảng băm; chi phí $O(k)$ của một phép chèn là giả thiết về cấu trúc dữ liệu.

**Phạm vi.** Một tài liệu; với cả kho, thời gian là tổng của các cận $O(1+wk)$ theo từng tài liệu.
:::

::: proof
**Bước 1 (bất biến).** Gọi $q$ là số vòng đã chạy của bước 2. Ta chứng minh bất biến
$$
S=\{D[j:j+k]:0\le j<q\}.
$$
Khởi tạo: $q=0$, và cả hai vế đều rỗng theo bước 1. Duy trì: vòng thứ $q+1$ chèn $D[q:q+k]$; phép chèn giữ đúng một bản của mỗi chuỗi, nên sau vòng đó $S=\{D[j:j+k]:0\le j<q+1\}$.

**Bước 2 (kết thúc).** Bước 2 chạy đúng $w$ vòng, với $w=\ell-k+1$ khi $k\le\ell$ và $w=0$ khi $\ell<k$. Khi dừng, $q=w$ và bất biến cho $S=\{D[j:j+k]:0\le j\le\ell-k\}=S_k(D)$ theo Định nghĩa 05.2. Điều này cho (a).

**Bước 3 (cận số phần tử).** Mỗi vòng thêm vào $S$ nhiều nhất một phần tử mới, nên $|S|\le w$ khi dừng. Điều này cho (b).

**Bước 4 (chi phí).** Theo bảng chi phí của Thuật toán 05.3, tổng là $O(1)+w\cdot O(k)=O(1+wk)$ kỳ vọng, do tính tuyến tính của kỳ vọng áp dụng cho $w$ phép chèn. Điều này cho (c). $\square$
:::

Các giả thiết của Mệnh đề 05.4 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "phép chèn giữ đúng một bản": nếu $S$ là một danh sách nối thêm, với `abcdabd` và $k=2$ thuật toán trả sáu phần tử, trong đó `ab` hai lần; kết quả là danh sách cửa sổ có độ dài $w$, không phải $S_2(D)$.
- Bỏ "chèn tốn $O(k)$ kỳ vọng": nếu kiểm trùng bằng cách so cửa sổ mới với mọi phần tử đã có, vòng thứ $q+1$ tốn tới $O(qk)$, và với các cửa sổ đôi một khác nhau tổng là $O(w^2k)$.

**Trong thực hành.** Tập $S$ là bảng băm các chuỗi con của tài liệu, và Thuật toán 05.3 chạy một lần cho mỗi tài liệu của kho. Với tài liệu $50\,000$ ký tự và $k=9$, bước 2 chạy $w=49\,992$ lần và tạo cửa sổ tốn khoảng $wk=449\,928$ lần đọc ký tự; tập có không quá $49\,992$ phần tử, gần bằng số ký tự của tài liệu. Lưu mỗi phần tử bằng 9 byte thì tập chiếm tới $9\cdot49\,992=449\,928$ byte, khoảng chín lần dung lượng tài liệu.

### 2.3 Độ dài shingle và khoảng trắng

Định nghĩa 05.2 coi tài liệu là một chuỗi ký tự cố định; dấu cách, dấu tab và ký tự xuống dòng đều là ký tự. Ví dụ sau cho thấy cách xử lý khoảng trắng thay đổi tập shingle.

::: example Ví dụ 05.4 (`touch down` và `touchdown`, $k=9$; MMDS Ví dụ 3.4, tr.78)
**Dữ kiện.** Hai cụm `touch down` (10 ký tự, có một dấu cách) và `touchdown` (9 ký tự); $k=9$.

**Giữ dấu cách.**

| Chuỗi | Số ký tự | Các 9-shingle |
|---|---:|---|
| `touch down` | 10 | `touch␣dow`, `ouch␣down` |
| `touchdown` | 9 | `touchdown` |

Hai tập không có phần tử chung.

**Xóa mọi khoảng trắng.** Cả hai chuỗi trở thành `touchdown` và có cùng tập $\{\texttt{touchdown}\}$.

**Kiểm tra lại.** Chuỗi 10 ký tự có $10-9+1=2$ cửa sổ; chuỗi 9 ký tự có một cửa sổ.
:::

Ví dụ cho thấy quy ước khoảng trắng là một phần của biểu diễn. Cùng với quy ước đó, độ dài $k$ quyết định một tài liệu tạo ra những phần tử nào.

::: remark Nhận xét 05.5 (Chọn $k$ và quy ước khoảng trắng)
- **Khoảng trắng.** MMDS đề nghị thay mỗi dãy gồm một hay nhiều ký tự trắng (dấu cách, tab, xuống dòng) bằng một dấu cách (§3.2.1, tr.78). Cách này giữ được sự phân biệt giữa shingle phủ hai từ và shingle nằm trong một từ, như `touch␣dow` và `touchdown`. Quy ước đã chọn phải dùng chung cho cả kho.
- **Tiêu chí chọn $k$.** $k$ phải đủ lớn để xác suất một shingle cho trước xuất hiện trong một tài liệu cho trước là thấp (§3.2.2, tr.79).
- **Ước lượng số shingle khả dĩ.** Nếu thư điện tử chỉ gồm chữ cái và một ký tự trắng, có $27^5=14\,348\,907$ chuỗi dài 5, lớn hơn nhiều độ dài một thư điện tử. Các ký tự không xuất hiện với cùng xác suất, nên MMDS ước lượng số $k$-shingle bằng $20^k$, như thể chỉ có 20 ký tự (§3.2.2, tr.79).
- **Giá trị khuyến nghị.** MMDS dùng $k=5$ cho thư điện tử và $k=9$ cho tài liệu dài như bài báo khoa học (§3.2.2, tr.79).
:::

Quy ước khoảng trắng biến đổi $D$ trước khi chạy Thuật toán 05.3, còn $k$ là tham số của thuật toán; hai tài liệu chỉ so được với nhau khi chúng dùng cùng quy ước và cùng $k$.

### 2.4 Băm shingle

Một 9-shingle chiếm 9 byte, và theo Mệnh đề 05.4(b), tài liệu $50\,000$ ký tự có tới $49\,992$ shingle. MMDS thay mỗi shingle bằng một số nguyên trong $\{0,\ldots,2^{32}-1\}$, tức 4 byte, do một hàm băm $g$ trả về; mỗi mã vừa một từ máy, nên so hai phần tử chỉ cần một thao tác (§3.2.3, tr.79). Tập biểu diễn tài liệu khi đó là tập mã $g(S_k(D))=\{g(a):a\in S_k(D)\}$. Hai shingle khác nhau có thể nhận cùng mã, tức một *va chạm* (collision). Mệnh đề sau nêu điều kiện để tập mã cho cùng Jaccard với tập shingle.

::: proposition Mệnh đề 05.6 (Mã không va chạm bảo toàn Jaccard)
**Giả thiết.** $S$, $T$ là hai tập hữu hạn các chuỗi dài $k$, $S\cup T\ne\varnothing$; một hàm $g$ từ các chuỗi dài $k$ vào $\{0,\ldots,2^{32}-1\}$ được dùng cho cả hai tập và đơn ánh trên $S\cup T$.

**Kết luận.** $|g(S)|=|S|$, $|g(T)|=|T|$ và
$$
\mathrm{SIM}\bigl(g(S),g(T)\bigr)=\mathrm{SIM}(S,T).
$$

**Điều kiện áp dụng.** Cùng một hàm $g$ được dùng cho mọi tài liệu của kho; $S$ và $T$ được lập với cùng $k$ và cùng quy ước khoảng trắng, để Jaccard của chúng so được hai tài liệu (Nhận xét 05.1, Ví dụ 05.4).

**Phạm vi.** Chỉ cần $g$ đơn ánh trên $S\cup T$ của cặp đang xét. Trên toàn bộ các chuỗi dài 9 thì $g$ không thể đơn ánh, vì số chuỗi lớn hơn số mã: với 27 ký tự đã có $27^9\approx7{,}6\cdot10^{12}>2^{32}$ chuỗi.
:::

::: proof
**Bước 1 (hợp).** Với mọi hàm $g$, $g(S\cup T)=g(S)\cup g(T)$, vì một mã thuộc $g(S\cup T)$ khi và chỉ khi nó là mã của một phần tử thuộc $S$ hoặc thuộc $T$.

**Bước 2 (giao).** Luôn có $g(S\cap T)\subseteq g(S)\cap g(T)$. Ngược lại, lấy $z\in g(S)\cap g(T)$: tồn tại $a\in S$, $b\in T$ với $g(a)=g(b)=z$. Vì $a,b\in S\cup T$ và $g$ đơn ánh trên $S\cup T$, $a=b\in S\cap T$, nên $z\in g(S\cap T)$. Do đó $g(S\cap T)=g(S)\cap g(T)$.

**Bước 3 (số phần tử).** Một hàm đơn ánh trên một tập hữu hạn $A$ cho $|g(A)|=|A|$. Áp dụng cho $A=S$, $T$, $S\cap T$, $S\cup T$, đều là tập con của $S\cup T$, rồi dùng Bước 1 và Bước 2:
$$
\mathrm{SIM}\bigl(g(S),g(T)\bigr)=\frac{|g(S\cap T)|}{|g(S\cup T)|}=\frac{|S\cap T|}{|S\cup T|}.
$$
Mẫu số khác 0 vì $S\cup T\ne\varnothing$. $\square$
:::

Các giả thiết của Mệnh đề 05.6 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "đơn ánh trên $S\cup T$": với $S=\{\texttt{ab},\texttt{bc},\texttt{cd}\}$, $T=\{\texttt{ab}\}$ ta có $\mathrm{SIM}(S,T)=1/3$; nếu $g(\texttt{bc})=g(\texttt{cd})$ và $g(\texttt{ab})$ khác mã đó thì $g(S)$ chỉ có hai mã, $g(T)$ có một mã chung với $g(S)$, và $\mathrm{SIM}(g(S),g(T))=1/2$.
- Bỏ "cùng một hàm $g$ cho hai tập": nếu $S=T=\{\texttt{ab}\}$ nhưng $T$ được mã bằng một hàm $g'$ với $g'(\texttt{ab})\ne g(\texttt{ab})$, thì $g(S)\cap g'(T)=\varnothing$ và Jaccard trên tập mã bằng 0 thay cho 1.

Trong Ví dụ 05.2, tập mã có đúng 5 phần tử khi năm shingle nhận năm mã khác nhau; nói chung số mã phân biệt không vượt số shingle phân biệt.

**Trong thực hành.** Với tài liệu $50\,000$ ký tự và $k=9$, tập mã có không quá $49\,992$ mã (Mệnh đề 05.4(b)), tức không quá $4\cdot49\,992=199\,968$ byte, khoảng bốn lần dung lượng tài liệu, đúng tỷ lệ MMDS nêu ở tr.81. MMDS so hai cách cùng dùng 4 byte cho một phần tử: dùng thẳng 4-shingle, hoặc băm 9-shingle xuống 4 byte (§3.2.3, tr.79–80). Với quy tắc 20 ký tự của Nhận xét 05.5, số 4-shingle có khả năng xuất hiện chỉ khoảng $20^4=160\,000$, tức khoảng $3{,}7\cdot10^{-5}$ của $2^{32}=4\,294\,967\,296$ giá trị 4 byte, nên mọi tài liệu dồn phần tử vào cùng một nhóm nhỏ giá trị. Số 9-shingle có khả năng xuất hiện, khoảng $20^9=5{,}12\cdot10^{11}$, vượt xa $2^{32}$, nên sau khi băm gần như mọi mã 4 byte đều có thể gặp. Với cùng dung lượng, mã của 9-shingle phân biệt tài liệu tốt hơn; đổi lại, $g$ không đơn ánh trên toàn miền, và giả thiết của Mệnh đề 05.6 phải đúng trên từng cặp mới giữ được Jaccard.

::: exercise Bài tập 05.3 (Cửa sổ, shingle và Jaccard của chuỗi ngắn)
- (a) Với $k=3$, lập $S_3(\texttt{abcdabd})$ và $S_3(\texttt{abcxabd})$, tính Jaccard của hai tập, và so với giá trị $3/7$ của $k=2$ (Ví dụ 05.3) bằng số cửa sổ bị đổi.
- (b) Chuỗi `abcdabc` chỉ khác `abcdabd` ở ký tự cuối. Với $k=2$, tính Jaccard của hai tập shingle và giải thích vì sao giá trị gần 1.
- (c) Với $k=2$, tính Jaccard của tập shingle của `abab` và `baba`, rồi nêu điều tập shingle không lưu.
:::

::: hint
Câu (a): các cửa sổ chứa vị trí 3. Câu (b): ký tự cuối thuộc bao nhiêu cửa sổ. Câu (c): liệt kê cửa sổ của từng chuỗi trước khi bỏ phần tử lặp.
:::

::: solution
**Câu (a).** Mỗi chuỗi có $7-3+1=5$ cửa sổ đôi một khác nhau: $S_3(\texttt{abcdabd})=\{\texttt{abc},\texttt{bcd},\texttt{cda},\texttt{dab},\texttt{abd}\}$ và $S_3(\texttt{abcxabd})=\{\texttt{abc},\texttt{bcx},\texttt{cxa},\texttt{xab},\texttt{abd}\}$. Giao là $\{\texttt{abc},\texttt{abd}\}$, hợp có 8 phần tử, nên Jaccard bằng $2/8=1/4<3/7$. Với $k=3$, ba cửa sổ chứa vị trí 3 (bắt đầu tại 1, 2, 3) đổi, trong khi với $k=2$ chỉ hai cửa sổ đổi.

**Câu (b).** $S_2(\texttt{abcdabc})=\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da}\}$. Giao với $S_2(\texttt{abcdabd})$ có 4 phần tử, hợp có 5, nên Jaccard bằng $4/5$. Ký tự cuối chỉ thuộc một cửa sổ, cửa sổ ở vị trí 5, nên thay nó chỉ đổi một cửa sổ: `bd` thành `bc`, và `bc` đã có trong tập.

**Câu (c).** `abab` có các cửa sổ `ab`, `ba`, `ab`; `baba` có `ba`, `ab`, `ba`. Cả hai có tập $\{\texttt{ab},\texttt{ba}\}$, nên Jaccard bằng 1 dù hai chuỗi khác nhau. Tập shingle không lưu thứ tự giữa các cửa sổ và số lần mỗi cửa sổ xuất hiện.

**Kiểm tra lại.** Câu (a): $5+5-2=8$; số cửa sổ đổi $\min(3,4)-\max(0,1)+1=3=k$. Câu (b): $|S|+|T|-|S\cap T|=5+4-4=5$. Câu (c): Jaccard bằng 1 khi và chỉ khi hai tập bằng nhau (Định nghĩa 01.9).
:::

::: exercise Bài tập 05.4 (Mã 4 byte và dung lượng tập mã)
- (a) Với quy tắc 20 ký tự của Nhận xét 05.5, tìm $k$ nhỏ nhất để số $k$-shingle có khả năng xuất hiện, $20^k$, vượt số mã 4 byte $2^{32}$.
- (b) Một thư điện tử dài $2\,000$ ký tự được lập tập 5-shingle theo khuyến nghị của MMDS, mỗi shingle mã hóa 4 byte. Tính cận trên của số phần tử và dung lượng tập mã, và so với dung lượng thư.
- (c) Cho $S=\{\texttt{ab},\texttt{bc}\}$ và $T=\{\texttt{cd},\texttt{da}\}$, với $g(\texttt{bc})=g(\texttt{cd})$ và các mã khác đôi một khác nhau. Tính $\mathrm{SIM}(S,T)$ và $\mathrm{SIM}(g(S),g(T))$.
:::

::: hint
Câu (a): so $20^7$ và $20^8$ với $2^{32}\approx4{,}29\cdot10^9$. Câu (b): dùng $w=\ell-k+1$. Câu (c): liệt kê hai tập mã.
:::

::: solution
**Câu (a).** $20^7=1{,}28\cdot10^9<2^{32}\approx4{,}29\cdot10^9<20^8=2{,}56\cdot10^{10}$, nên $k=8$ là giá trị nhỏ nhất. Với $k\ge8$, số shingle có khả năng xuất hiện vượt số mã, nên mã 4 byte của chúng có thể gặp mọi giá trị 4 byte.

**Câu (b).** Có $2\,000-5+1=1\,996$ cửa sổ, nên tập mã có không quá $1\,996$ phần tử và chiếm không quá $4\cdot1\,996=7\,984$ byte, khoảng bốn lần dung lượng thư. Cửa sổ lặp hoặc va chạm làm tập nhỏ hơn.

**Câu (c).** $S\cap T=\varnothing$ nên $\mathrm{SIM}(S,T)=0$. Đặt $z=g(\texttt{bc})=g(\texttt{cd})$; $g(S)=\{g(\texttt{ab}),z\}$ và $g(T)=\{z,g(\texttt{da})\}$ có giao $\{z\}$ và hợp ba phần tử, nên $\mathrm{SIM}(g(S),g(T))=1/3$. Hai tài liệu không chung shingle nào vẫn có Jaccard dương trên tập mã.

**Kiểm tra lại.** Câu (b): $7\,984/2\,000\approx4$, cùng tỷ lệ với tài liệu $50\,000$ ký tự. Câu (c): $g$ không đơn ánh trên $S\cup T$, nên Mệnh đề 05.6 không áp dụng.
:::

Tập $k$-shingle (Định nghĩa 05.2) lập được trong thời gian kỳ vọng $O(1+wk)$ (Thuật toán 05.3, Mệnh đề 05.4), với quy ước khoảng trắng và độ dài $k$ của Nhận xét 05.5, và mã 4 byte giữ Jaccard khi không va chạm trên cặp đang xét (Mệnh đề 05.6). Tuy nhiên, tập mã của một tài liệu $50\,000$ ký tự vẫn có cận trên $199\,968$ byte. Trong Mục 3, chúng ta thay cả tập bằng một phần tử đại diện chọn theo một thứ tự chung và chứng minh rằng phép thay này giữ Jaccard theo nghĩa xác suất.

<!-- note-topic-id: lec-05-topic-04 -->
## 3. MinHash theo một hoán vị

Với hàng triệu tài liệu, các tập mã shingle có thể không vừa bộ nhớ chính, vì mỗi tập gấp khoảng bốn lần tài liệu của nó (MMDS, mở đầu §3.3, tr.81). Chúng ta cần thay mỗi tập bằng một *chữ ký* (signature) có số thành phần chọn trước, không phụ thuộc kích thước tập, sao cho từ hai chữ ký ước lượng được Jaccard của hai tập. Bước đầu tiên là một phép thử cho đúng một thành phần của chữ ký; để phát biểu nó, chúng ta đặt mọi tập của kho vào một ma trận.

### 3.1 Ma trận đặc trưng

Ví dụ sau dùng một vũ trụ năm phần tử và bốn tập.

::: example Ví dụ 05.5 (Bốn tập đặc trưng; MMDS Ví dụ 3.6, Hình 3.2, tr.81–82)
**Dữ kiện.** Vũ trụ $U=\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$ với mã hàng $\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\leftrightarrow0,1,2,3,4$, và bốn tập
$$
S_1=\{\mathrm a,\mathrm d\},\quad S_2=\{\mathrm c\},\quad S_3=\{\mathrm b,\mathrm d,\mathrm e\},\quad S_4=\{\mathrm a,\mathrm c,\mathrm d\}.
$$

**Bảng phần tử–tập.** Ô ở hàng $u$, cột $S_c$ bằng 1 khi $u\in S_c$.

| Phần tử / $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| a / 0 | 1 | 0 | 0 | 1 |
| b / 1 | 0 | 0 | 1 | 0 |
| c / 2 | 0 | 1 | 0 | 1 |
| d / 3 | 1 | 0 | 1 | 1 |
| e / 4 | 0 | 0 | 1 | 0 |

**Một cặp.** Giao của $S_1$, $S_4$ là $\{\mathrm a,\mathrm d\}$, hợp là $\{\mathrm a,\mathrm c,\mathrm d\}$, nên $\mathrm{SIM}(S_1,S_4)=2/3$.

**Kiểm tra lại.** Tổng của cột $S_c$ bằng $|S_c|$: $2,1,3,3$.
:::

::: definition Định nghĩa 05.7 (Ma trận đặc trưng và biểu diễn theo hàng)
Cho vũ trụ hữu hạn $U$ có $R\ge1$ phần tử, mỗi phần tử gán một mã hàng $r\in\{0,\ldots,R-1\}$ khác nhau, và $C$ tập $S_1,\ldots,S_C\subseteq U$.

- *Ma trận đặc trưng* (characteristic matrix) là $M\in\{0,1\}^{R\times C}$ với
$$
M(r,c)=\begin{cases}1,&\text{phần tử có mã hàng }r\text{ thuộc }S_c,\\0,&\text{ngược lại.}\end{cases}
$$
- $L=\operatorname{nnz}(M)=\sum_{r,c}M(r,c)=\sum_c|S_c|$ là số ô 1 của $M$.
- *Biểu diễn theo hàng* của $M$ gồm, với mỗi $r$, danh sách các chỉ số cột $c$ có $M(r,c)=1$; tổng độ dài các danh sách bằng $L$.
:::

Hàng biểu diễn phần tử, cột biểu diễn tập: cột $c$ là véc-tơ chỉ báo của $S_c$ trên $U$, và một cột toàn 0 ứng với tập rỗng. Jaccard đọc được trên hai cột: tử số đếm các hàng có 1 ở cả hai cột, mẫu số đếm các hàng có 1 ở ít nhất một cột. Ma trận là một cách nhìn dữ liệu; trong thực tế nó hầu như luôn thưa, tức có nhiều ô 0 hơn nhiều so với ô 1, nên dữ liệu được lưu bằng vị trí các ô 1 (MMDS, §3.3.1, tr.82). Với Ví dụ 05.5, biểu diễn theo hàng là:

| Hàng | Danh sách cột |
|---|---|
| a / 0 | 1, 4 |
| b / 1 | 3 |
| c / 2 | 2, 4 |
| d / 3 | 1, 3, 4 |
| e / 4 | 3 |

Ở đây $L=2+1+2+3+1=9$, còn ma trận đặc (dense, lưu mọi ô) có $RC=20$ ô. Mỗi chỉ số cột cũng chiếm một từ máy, nên biểu diễn theo hàng tiết kiệm khi $L$ nhỏ hơn nhiều so với $RC$. Biểu diễn này cho phép, với mỗi phần tử, đi thẳng tới những tập chứa nó mà không đọc các ô 0.

Với một kho văn bản, $U$ là tập các mã shingle xuất hiện trong ít nhất một tài liệu, và mã hàng của một mã là thứ tự của nó khi các mã trong $U$ được xếp tăng dần; do đó $R\le2^{32}$ khi dùng mã 4 byte.

<!-- note-topic-id: lec-05-topic-05 -->
### 3.2 MinHash

Về mặt ý tưởng, một thành phần chữ ký thay cả tập bằng một phần tử đại diện, chọn bằng cùng một quy tắc cho mọi tập. Một thứ tự chung trên $U$ cho mỗi tập đúng một đại diện: phần tử của tập đứng đầu trong thứ tự ấy. Thứ tự phải chung cho mọi tập, vì hai tập chỉ so được với nhau dưới cùng một phép thử. Để làm rõ quy tắc này, xem ví dụ sau.

::: example Ví dụ 05.6 (Thứ tự $(\mathrm b,\mathrm e,\mathrm a,\mathrm d,\mathrm c)$; MMDS Ví dụ 3.7, Hình 3.3, tr.82–83)
**Dữ kiện.** Bốn tập của Ví dụ 05.5: $S_1=\{\mathrm a,\mathrm d\}$, $S_2=\{\mathrm c\}$, $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$; thứ tự $\pi=(\mathrm b,\mathrm e,\mathrm a,\mathrm d,\mathrm c)$.

**Xếp lại hàng.** Các hàng của ma trận đặc trưng xếp theo $\pi$:

| Vị trí trong $\pi$ | Phần tử | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---|---:|---:|---:|---:|
| 1 | b | 0 | 0 | 1 | 0 |
| 2 | e | 0 | 0 | 1 | 0 |
| 3 | a | 1 | 0 | 0 | 1 |
| 4 | d | 1 | 0 | 1 | 1 |
| 5 | c | 0 | 1 | 0 | 1 |

**Đọc ô 1 đầu tiên của mỗi cột.**

| Đại lượng | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| Phần tử đứng đầu | a | c | b | a |
| Vị trí của nó trong $\pi$ | 3 | 5 | 1 | 3 |

$S_1$ không chứa b, e nên gặp a đầu tiên ở vị trí 3; $S_2$ chỉ chứa c; $S_3$ chứa ngay phần tử đầu b; $S_4$ gặp a trước d và c.

**Kiểm tra lại.** Phần tử đứng đầu của mỗi tập thuộc tập đó, và mọi phần tử khác của tập đứng sau nó trong $\pi$: với $S_4$, a ở vị trí 3, d ở vị trí 4, c ở vị trí 5.
:::

![Hai tập S1 = {a, d} và S4 = {a, c, d} dùng chung thứ tự b, e, a, d, c. Cả hai gặp a trước tiên; b và e nằm ngoài hợp của hai tập nên không ảnh hưởng lựa chọn.](img/lec-05/minhash-hoan-vi.svg)

Hình chỉ hai cột $S_1$, $S_4$ trên thứ tự $\pi$: hai phần tử đầu b, e không thuộc tập nào trong hai tập, và cả hai cột dừng ở a. Định nghĩa sau ghi lại phép chọn này.

::: definition Định nghĩa 05.8 (Hạng và MinHash)
Cho một hoán vị $\pi$ của $U$ (còn gọi là thứ tự liệt kê), tức một cách liệt kê mỗi phần tử của $U$ đúng một lần.

- *Hạng* (rank) của $u\in U$ là vị trí $\operatorname{rank}_\pi(u)\in\{1,\ldots,R\}$ của $u$ trong $\pi$.
- *MinHash* của một tập $S\subseteq U$, $S\ne\varnothing$, theo $\pi$ là
$$
h_\pi(S)=\arg\min_{u\in S}\operatorname{rank}_\pi(u).
$$
:::

Các hạng đôi một khác nhau, nên phần tử đạt cực tiểu là duy nhất và $h_\pi(S)\in S$. Theo Định nghĩa 05.7, $h_\pi(S_c)$ là phần tử ứng với ô 1 đầu tiên của cột $c$ khi các hàng được xếp theo $\pi$.

Ở đây $h_\pi(S)$ là định danh của phần tử đứng đầu, như a ở Ví dụ 05.6; MMDS gọi giá trị này là số hiệu của hàng đầu tiên, theo thứ tự đã hoán vị, mà cột có 1 (§3.3.2, tr.82). Ghi hạng $\min_{u\in S}\operatorname{rank}_\pi(u)$ thay cho định danh cũng được: hạng và định danh tương ứng một–một dưới cùng $\pi$, nên quan hệ "hai MinHash bằng nhau" không đổi. Hai loại giá trị vẫn được ghi tách bạch trong bảng, như hai dòng của Ví dụ 05.6.

Điều kiện $S\ne\varnothing$ là cần: với $S=\varnothing$, tập lấy cực tiểu rỗng và $h_\pi(\varnothing)$ không xác định.

<!-- note-topic-id: lec-05-topic-06 -->
### 3.3 Định lý xác suất trùng MinHash

Một hoán vị cố định cho mỗi cặp tập một kết quả xác định: trùng hoặc không. Ở Ví dụ 05.6, $h_\pi(S_1)=h_\pi(S_4)=\mathrm a$ dù $\mathrm{SIM}(S_1,S_4)=2/3$. Để nối MinHash với Jaccard, chúng ta chọn hoán vị ngẫu nhiên và hỏi xác suất trùng. Ví dụ sau tách các hàng của một cặp cột thành ba loại.

::: example Ví dụ 05.7 (Ba loại hàng của $S_1$, $S_4$)
**Dữ kiện.** $S_1=\{\mathrm a,\mathrm d\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$ trên $U=\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$.

**Ba loại hàng.** Theo giá trị của hai cột tại mỗi hàng (MMDS, §3.3.3, tr.83):

| Loại | Giá trị hai cột | Ý nghĩa | Các hàng |
|---|---|---|---|
| $\mathrm X$ | $(1,1)$ | phần tử thuộc giao | a, d |
| $\mathrm Y$ | $(1,0)$ hoặc $(0,1)$ | phần tử thuộc đúng một tập | c |
| $\mathrm Z$ | $(0,0)$ | phần tử ngoài hợp | b, e |

**Hai số đếm.** $x=|S_1\cap S_4|=2$ hàng loại $\mathrm X$, $y=|S_1\cup S_4|-|S_1\cap S_4|=1$ hàng loại $\mathrm Y$, nên $\mathrm{SIM}(S_1,S_4)=x/(x+y)=2/3$.

**Kiểm tra lại.** $x+y+2=5=R$: hai hàng loại $\mathrm Z$.
:::

![Phân loại các hàng cho S1 và S4: a, d thuộc giao, loại X; c thuộc phần riêng, loại Y; b, e ngoài hợp, loại Z. Trong một hoán vị đều, phần tử đầu của hợp chia đều cho a, c, d; hai trên ba lựa chọn làm hai MinHash bằng nhau.](img/lec-05/phan-tu-dau-hop.svg)

Trên hình, chỉ ba hàng a, c, d của hợp ảnh hưởng tới phép chọn. Một phần tử ngoài $S\cup T$ không thuộc tập nào nên không bao giờ được chọn. Gọi $u$ là phần tử đứng đầu của hợp theo $\pi$. Nếu $u$ thuộc giao, nó đứng đầu cả hai tập; nếu $u$ chỉ thuộc một tập, tập ấy chọn $u$ còn tập kia chọn một phần tử khác. Quan hệ này đúng với mọi hoán vị; khi hoán vị được chọn ngẫu nhiên, nó trở thành một đẳng thức xác suất. Trước hết ta cần phân phối của $u$.

::: lemma Bổ đề 05.9 (Phần tử đứng đầu phân phối đều)
**Giả thiết.** $A\subseteq U$, $A\ne\varnothing$; $\pi$ được chọn đều trong $R!$ hoán vị của $U$.

**Kết luận.** Với mỗi $a\in A$,
$$
\Pr\bigl[h_\pi(A)=a\bigr]=\frac1{|A|}.
$$

**Điều kiện áp dụng.** Xác suất lấy theo cách chọn $\pi$; $A$ cố định, không phụ thuộc $\pi$.

**Phạm vi.** Phân phối của phần tử đứng đầu của một tập; với $A=S\cup T$, đó là phần tử quyết định hai MinHash có trùng hay không.
:::

::: proof
**Bước 1 (một song ánh).** Lấy $a,a'\in A$. Gọi $\Pi_a$ là tập các hoán vị $\pi$ có $h_\pi(A)=a$. Phép đổi chỗ $a$ và $a'$ trong thứ tự liệt kê biến mỗi $\pi\in\Pi_a$ thành một hoán vị $\pi'$ trong đó $a'$ chiếm vị trí cũ của $a$, $a$ chiếm vị trí cũ của $a'$, đứng sau vị trí cũ của $a$, và mọi phần tử khác giữ vị trí; do đó $a'$ đứng trước mọi phần tử khác của $A$, tức $\pi'\in\Pi_{a'}$. Áp dụng cùng phép đổi chỗ hai lần cho lại $\pi$, nên đây là một song ánh từ $\Pi_a$ lên $\Pi_{a'}$, và $|\Pi_a|=|\Pi_{a'}|$.

**Bước 2 (phân hoạch).** Vì $A\ne\varnothing$, mỗi hoán vị có đúng một phần tử của $A$ đứng đầu, nên các tập $\Pi_a$, $a\in A$, phân hoạch $R!$ hoán vị thành $|A|$ phần có cùng cỡ. Mỗi phần có $R!/|A|$ hoán vị.

**Bước 3 (xác suất).** $\pi$ chọn đều, nên $\Pr[h_\pi(A)=a]=|\Pi_a|/R!=1/|A|$. $\square$
:::

Bổ đề 05.9 là chỗ duy nhất dùng tính đều của $\pi$. Định lý sau, phát biểu ở MMDS §3.3.3, tr.83, nối phân phối đó với giao và hợp.

::: theorem Định lý 05.10 (Xác suất trùng MinHash)
**Giả thiết.** $U$ hữu hạn, $|U|=R$; $S,T\subseteq U$, $S\ne\varnothing$, $T\ne\varnothing$; $\pi$ được chọn đều trong $R!$ hoán vị của $U$, và cùng $\pi$ dùng cho hai tập.

**Kết luận.**
$$
\Pr\bigl[h_\pi(S)=h_\pi(T)\bigr]=\mathrm{SIM}(S,T).
$$

**Điều kiện áp dụng.** Xác suất lấy theo cách chọn $\pi$, còn $S$, $T$ cố định; phân phối của $\pi$ đều trên mọi hoán vị của $U$.

**Phạm vi.** Một phép thử cho kết quả trùng hoặc không trùng, và $\mathrm{SIM}(S,T)$ là xác suất của kết quả trùng. Khi mã shingle va chạm, xác suất này bằng Jaccard của hai tập mã, có thể khác Jaccard của hai tập shingle (Mệnh đề 05.6).
:::

::: proof
Đặt $A=S\cup T$, khác rỗng vì $S\ne\varnothing$, và $u=h_\pi(A)$ là phần tử đứng đầu của hợp. Đặt $x=|S\cap T|$ và $y=|A|-x$.

**Bước 1 (phân phối của $u$).** Theo Bổ đề 05.9 với $A=S\cup T$, $u$ có phân phối đều trên $A$: mỗi phần tử của hợp có xác suất $1/(x+y)$.

**Bước 2 (trùng khi và chỉ khi $u$ thuộc giao).** Nếu $u\in S$, mọi phần tử của $S$ thuộc $A$, nên có hạng không nhỏ hơn hạng của $u$; do đó $h_\pi(S)=u$. Tương tự với $T$.

- Nếu $u\in S\cap T$ thì $h_\pi(S)=u=h_\pi(T)$.
- Nếu $u\in S\setminus T$ thì $h_\pi(S)=u$, còn $h_\pi(T)\in T$ nên $h_\pi(T)\ne u$; hai MinHash khác nhau. Trường hợp $u\in T\setminus S$ đối xứng.

Vậy biến cố $\{h_\pi(S)=h_\pi(T)\}$ trùng với biến cố $\{u\in S\cap T\}$.

**Bước 3 (đếm).** Theo Bước 1 và Bước 2,
$$
\Pr\bigl[h_\pi(S)=h_\pi(T)\bigr]=\Pr[u\in S\cap T]=\frac{x}{x+y}=\frac{|S\cap T|}{|S\cup T|}=\mathrm{SIM}(S,T).
$$
Lập luận bao gồm hai tập rời ($x=0$, xác suất 0) và hai tập bằng nhau ($y=0$, xác suất 1); các hàng loại $\mathrm Z$ không bao giờ được chọn. $\square$
:::

Các giả thiết của Định lý 05.10 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "cùng $\pi$ cho hai tập": so $S_1=\{\mathrm a,\mathrm d\}$ với chính nó dưới hai hoán vị $\pi$, $\pi'$ chọn đều và độc lập. Theo Bổ đề 05.9, mỗi MinHash là a hoặc d với xác suất $1/2$, nên xác suất trùng là $(1/2)^2+(1/2)^2=1/2<1=\mathrm{SIM}(S_1,S_1)$.
- Bỏ "$\pi$ chọn đều trên mọi hoán vị": với $\pi=(\mathrm b,\mathrm e,\mathrm a,\mathrm d,\mathrm c)$ cố định, $S_1$ và $S_4$ trùng với xác suất 1 (Ví dụ 05.6), khác $\mathrm{SIM}(S_1,S_4)=2/3$.
- Bỏ "$S\ne\varnothing$, $T\ne\varnothing$": $h_\pi(\varnothing)$ không xác định (Định nghĩa 05.8), nên vế trái không có nghĩa; với $S=T=\varnothing$, vế phải là $0/0$.

Bước 1 của chứng minh dùng tính đều của $\pi$; Bước 2 dùng việc hai MinHash lấy theo cùng một hoán vị; cả hai bước dùng giả thiết không rỗng. Ví dụ sau áp dụng định lý cho cặp $S_1$, $S_4$ của Ví dụ 05.7.

::: example Ví dụ 05.8 (Kiểm Định lý 05.10 trên $S_1$, $S_4$)
**Dữ kiện.** $S_1=\{\mathrm a,\mathrm d\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$; $\pi$ chọn đều trong $5!=120$ hoán vị của $U$.

**Phần tử đầu của hợp.** Hợp là $\{\mathrm a,\mathrm c,\mathrm d\}$; theo Bổ đề 05.9, mỗi phần tử đứng đầu hợp với xác suất $1/3$.

**Xác suất trùng.** Hai MinHash trùng khi phần tử đứng đầu là a hoặc d, nên xác suất bằng $2/3$; khi phần tử đứng đầu là c, $h_\pi(S_4)=\mathrm c$ còn $h_\pi(S_1)\in\{\mathrm a,\mathrm d\}$.

**Kiểm tra lại.** $x/(x+y)=2/3=\mathrm{SIM}(S_1,S_4)$ với $x=2$, $y=1$ của Ví dụ 05.7. Thứ tự $(\mathrm b,\mathrm e,\mathrm a,\mathrm d,\mathrm c)$ của Ví dụ 05.6 thuộc nhóm hoán vị có a đứng đầu hợp, nên cho kết quả trùng.
:::

**Trong thực hành.** Ma trận đặc trưng của một kho có $R$ bằng số mã shingle khác nhau xuất hiện trong kho, tới $2^{32}$ hàng khi dùng mã 4 byte. Một ma trận đặc trưng lớn không hoán vị tường minh được: ngay việc chọn một hoán vị ngẫu nhiên của hàng triệu hoặc hàng tỷ hàng cũng tốn thời gian, và sắp xếp lại các hàng còn tốn hơn (MMDS, §3.3.5, tr.84). Vì vậy giả thiết "$\pi$ chọn đều trên $R!$ hoán vị" chỉ đúng trong mô hình phân tích; cài đặt thay $\pi$ bằng một hàm băm trên mã hàng, và khi đó Định lý 05.10 cho một đẳng thức của mô hình, còn trên dữ liệu thật xác suất trùng chỉ xấp xỉ Jaccard (Nhận xét 05.23, Tình huống 05.3). Xác suất trong định lý lấy theo cách chọn $\pi$ cho một cặp cố định; tỷ lệ cặp trùng trong cả kho là một đại lượng khác, phụ thuộc vào Jaccard của từng cặp.

::: exercise Bài tập 05.5 (Thêm một phần tử và đổi hoán vị)
Cho bốn tập $S_1=\{\mathrm a,\mathrm d\}$, $S_2=\{\mathrm c\}$, $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$ của Ví dụ 05.5.

- (a) Thêm phần tử f với mã hàng 5, thuộc $S_2$ và $S_3$. Viết danh sách của hàng f trong biểu diễn theo hàng, tính $L$ và $RC$ mới, và tính $\mathrm{SIM}(S_2,S_3)$ trước và sau khi thêm f.
- (b) Với các tập ban đầu và hoán vị $\pi=(\mathrm c,\mathrm e,\mathrm b,\mathrm a,\mathrm d)$, tính $h_\pi$ của bốn tập, chỉ ra các cặp có MinHash trùng, và so mỗi cặp $S_1$, $S_4$ và $S_2$, $S_4$ với Jaccard của nó.
:::

::: hint
Câu (a): mỗi phần tử mới thêm một hàng; mỗi ô 1 mới tăng $L$ thêm một. Câu (b): đọc ô 1 đầu tiên của mỗi cột theo $\pi$.
:::

::: solution
**Câu (a).** Hàng f (mã 5) có danh sách cột 2, 3. Khi đó $R=6$, $L=9+2=11$ và $RC=6\cdot4=24$. Trước khi thêm, $S_2=\{\mathrm c\}$ và $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$ rời nhau, nên $\mathrm{SIM}(S_2,S_3)=0$; sau khi thêm, giao là $\{\mathrm f\}$, hợp là $\{\mathrm b,\mathrm c,\mathrm d,\mathrm e,\mathrm f\}$, nên $\mathrm{SIM}=1/5$.

**Câu (b).** Theo $\pi=(\mathrm c,\mathrm e,\mathrm b,\mathrm a,\mathrm d)$: $h_\pi(S_1)=\mathrm a$ (a đứng trước d), $h_\pi(S_2)=\mathrm c$, $h_\pi(S_3)=\mathrm e$, $h_\pi(S_4)=\mathrm c$. Chỉ cặp $S_2$, $S_4$ trùng, với Jaccard $1/3$; cặp $S_1$, $S_4$ không trùng, dù có Jaccard $2/3$. Phần tử đứng đầu hợp $\{\mathrm a,\mathrm c,\mathrm d\}$ của $S_1$, $S_4$ là c, thuộc phần riêng.

**Kiểm tra lại.** Câu (a): tổng độ dài các danh sách là $2+1+2+3+1+2=11=L$. Câu (b): một hoán vị cố định cho mỗi cặp kết quả 0 hoặc 1; cùng hoán vị có thể cho 1 với cặp có Jaccard $1/3$ và 0 với cặp có Jaccard $2/3$.
:::

::: exercise Bài tập 05.6 (Thêm một phần tử riêng)
Cho $S_1=\{\mathrm a,\mathrm d\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$ và $S_1'=S_1\cup\{\mathrm e\}$. Với $\pi$ chọn đều trong mọi hoán vị của $U=\{\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\}$, tính $\Pr[h_\pi(S_1')=h_\pi(S_4)]$ và giải thích vì sao giá trị giảm so với $\Pr[h_\pi(S_1)=h_\pi(S_4)]$.
:::

::: hint
Xác định giao và hợp mới, rồi dùng Định lý 05.10.
:::

::: solution
Giao vẫn là $\{\mathrm a,\mathrm d\}$; hợp thành $\{\mathrm a,\mathrm c,\mathrm d,\mathrm e\}$. Hai tập đều không rỗng và dùng chung $\pi$ chọn đều, nên theo Định lý 05.10
$$
\Pr\bigl[h_\pi(S_1')=h_\pi(S_4)\bigr]=\frac24=\frac12 .
$$
Phần tử e mở rộng hợp nhưng không thuộc giao: theo Bổ đề 05.9 phần tử đứng đầu hợp giờ chia đều cho bốn phần tử, và hai trong bốn phần tử (c, e) thuộc phần riêng, so với một trong ba trước đó.

**Kiểm tra lại.** $1/2<2/3$ (Ví dụ 05.8); $x=2$, $y=2$, $x/(x+y)=1/2$.
:::

Ma trận đặc trưng (Định nghĩa 05.7) và MinHash theo một hoán vị (Định nghĩa 05.8) cho một phép thử có xác suất trùng đúng bằng Jaccard khi hoán vị chọn đều (Bổ đề 05.9, Định lý 05.10). Một hoán vị cố định lại cho mỗi cặp một kết quả xác định, như kết quả trùng của cặp $S_1$, $S_4$ có Jaccard $2/3$ ở Ví dụ 05.6. Trong Mục 4, chúng ta ghép $n$ phép thử thành một chữ ký và lấy tỷ lệ tọa độ trùng làm ước lượng.

<!-- note-topic-id: lec-05-topic-07 -->
## 4. Chữ ký MinHash và ước lượng Jaccard

Theo Định lý 05.10, một phép thử MinHash cho cặp $S_1$, $S_4$ kết quả trùng với xác suất $2/3$, nhưng mỗi lần chạy chỉ thấy 0 hoặc 1, nên một phép thử không cho một số gần $2/3$.

### 4.1 Chữ ký và ước lượng

Ví dụ sau dùng hai hoán vị cố định cho cả bốn tập và so các chữ ký theo từng tọa độ.

::: example Ví dụ 05.9 (Hai hoán vị cố định trên bốn tập đặc trưng)
**Dữ kiện.** $S_1=\{\mathrm a,\mathrm d\}$, $S_2=\{\mathrm c\}$, $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$; hai hoán vị $\pi_1=(\mathrm e,\mathrm a,\mathrm b,\mathrm c,\mathrm d)$ và $\pi_2=(\mathrm d,\mathrm a,\mathrm c,\mathrm e,\mathrm b)$, dùng chung cho mọi tập.

**Phần tử đứng đầu.**

| Hoán vị | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| $\pi_1=(\mathrm e,\mathrm a,\mathrm b,\mathrm c,\mathrm d)$ | a | c | e | a |
| $\pi_2=(\mathrm d,\mathrm a,\mathrm c,\mathrm e,\mathrm b)$ | d | c | d | d |

**So theo tọa độ.** Cột của $S_1$ và $S_4$ đều là $(\mathrm a,\mathrm d)^{\mathsf T}$: hai tọa độ trùng, tỷ lệ $2/2=1$, trong khi $\mathrm{SIM}(S_1,S_4)=2/3$. Cột của $S_2$ là $(\mathrm c,\mathrm c)^{\mathsf T}$, của $S_4$ là $(\mathrm a,\mathrm d)^{\mathsf T}$: không tọa độ nào trùng, tỷ lệ 0, trong khi $\mathrm{SIM}(S_2,S_4)=1/3$.

**Kiểm tra lại.** Với $\pi_2$, d đứng đầu nên mọi tập chứa d chọn d: $S_1$, $S_3$, $S_4$; $S_2$ không chứa d và chọn c, đứng thứ ba.
:::

Với hai tọa độ, tỷ lệ chỉ nhận ba giá trị $0$, $1/2$, $1$, và trên cùng bốn tập tỷ lệ lệch khỏi Jaccard về cả hai phía. Định nghĩa sau ghi lại phép lập chữ ký cho $n$ hoán vị bất kỳ.

::: definition Định nghĩa 05.11 (Chữ ký MinHash, ma trận chữ ký và ước lượng Jaccard)
Cho số nguyên $n\ge1$ và $n$ hoán vị $\pi_1,\ldots,\pi_n$ của $U$, dùng chung cho mọi tập.

- *Chữ ký MinHash* (MinHash signature) của tập $S\ne\varnothing$ là véc-tơ cột
$$
\sigma(S)=\bigl(h_{\pi_1}(S),\ldots,h_{\pi_n}(S)\bigr)^{\mathsf T}.
$$
- *Ma trận chữ ký* (signature matrix) của $S_1,\ldots,S_C$, các tập không rỗng, là ma trận $n\times C$ có cột $c$ là $\sigma(S_c)$.
- *Ước lượng Jaccard* của hai tập không rỗng $S$, $T$ là tỷ lệ tọa độ trùng của hai chữ ký,
$$
\widehat s=\widehat{\mathrm{SIM}}(S,T)=\frac1n\sum_{i=1}^n\mathbf 1\bigl[h_{\pi_i}(S)=h_{\pi_i}(T)\bigr],
$$
trong đó $\mathbf 1[E]$ bằng 1 khi mệnh đề $E$ đúng và bằng 0 khi $E$ sai.
:::

Hàng của ma trận chữ ký là một phép thử, còn hàng của ma trận đặc trưng là một phần tử của $U$; ma trận chữ ký có cùng $C$ cột nhưng chỉ $n$ hàng (MMDS, §3.3.4, tr.83–84). Tọa độ $i$ của hai chữ ký chỉ được so với nhau vì chúng dùng cùng $\pi_i$. Ví dụ 05.9 là trường hợp $n=2$ của Định nghĩa 05.11, với ước lượng $\widehat{\mathrm{SIM}}(S_1,S_4)=1$ và $\widehat{\mathrm{SIM}}(S_2,S_4)=0$.

Một nhầm lẫn thường gặp là lấy Jaccard giữa hai tập giá trị của hai chữ ký: hai chữ ký $(\mathrm a,\mathrm d)^{\mathsf T}$ và $(\mathrm d,\mathrm a)^{\mathsf T}$ có cùng tập giá trị $\{\mathrm a,\mathrm d\}$ nhưng không trùng tọa độ nào, nên $\widehat s=0$ trong khi Jaccard của hai tập giá trị bằng 1.

Ước lượng $\widehat s$ là một số tính được từ hai chữ ký, còn $s=\mathrm{SIM}(S,T)$ là số cần ước lượng; khi các hoán vị được chọn ngẫu nhiên, $\widehat s$ là một biến ngẫu nhiên.

### 4.2 Kỳ vọng của ước lượng

Giữ cố định một cặp $S$, $T$ không rỗng và đặt $s=\mathrm{SIM}(S,T)$ cùng
$$
I_i=\mathbf 1\bigl[h_{\pi_i}(S)=h_{\pi_i}(T)\bigr],\qquad i=1,\ldots,n,
$$
nên $\widehat s=\frac1n\sum_iI_i$. Mỗi $I_i$ là kết quả của một phép thử của Định lý 05.10. Kết quả sau dùng định lý ấy cho từng tọa độ rồi cộng lại.

::: proposition Mệnh đề 05.12 (Ước lượng không chệch)
**Giả thiết.** $S$, $T$ không rỗng; $n\ge1$; mỗi $\pi_i$ được chọn đều trong $R!$ hoán vị của $U$, và cùng bộ $\pi_1,\ldots,\pi_n$ dùng cho hai tập.

**Kết luận.**
$$
\mathbb E\Bigl[\sum_{i=1}^nI_i\Bigr]=ns,\qquad \mathbb E[\widehat s]=s.
$$

**Điều kiện áp dụng.** Không cần các $\pi_i$ độc lập với nhau.

**Phạm vi.** Kỳ vọng là trung bình của $\widehat s$ qua các lần chọn bộ hoán vị; độ dao động của $\widehat s$ được đo bằng phương sai ở Mệnh đề 05.14.
:::

::: proof
**Bước 1 (một tọa độ).** $I_i$ chỉ nhận giá trị 0 hoặc 1, nên $\mathbb E[I_i]=\Pr[I_i=1]$. Theo Định lý 05.10 áp dụng cho $\pi_i$, $\Pr[I_i=1]=s$.

**Bước 2 (tổng).** Theo tính tuyến tính của kỳ vọng, vốn không cần độc lập,
$$
\mathbb E\Bigl[\sum_{i=1}^nI_i\Bigr]=\sum_{i=1}^n\mathbb E[I_i]=ns .
$$

**Bước 3 (tỷ lệ).** Nhân với hằng số $1/n$: $\mathbb E[\widehat s]=\frac1n\cdot ns=s$. $\square$
:::

Mệnh đề 05.12 phân biệt hai đại lượng: kỳ vọng số tọa độ trùng là $ns$, kỳ vọng tỷ lệ tọa độ trùng là $s$. Các giả thiết của Mệnh đề 05.12 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "mỗi $\pi_i$ chọn đều": nếu mọi $\pi_i$ bằng $(\mathrm b,\mathrm e,\mathrm a,\mathrm d,\mathrm c)$, thì $\widehat{\mathrm{SIM}}(S_1,S_4)=1$ với mọi bộ, nên kỳ vọng bằng $1\ne2/3$.
- Bỏ "cùng bộ hoán vị cho hai tập": so $S_1$ với chính nó, $S_1$ dùng $\pi_i$ còn bản sao dùng $\pi_i'$ độc lập; theo phản ví dụ thứ nhất sau Định lý 05.10, mỗi tọa độ trùng với xác suất $1/2$, nên $\mathbb E[\widehat s]=1/2\ne1$.

Điều kiện "không cần độc lập" cũng có ví dụ: nếu chọn đều một hoán vị $\pi$ rồi đặt $\pi_1=\cdots=\pi_n=\pi$, mọi $I_i$ bằng nhau, $\widehat s$ chỉ nhận 0 hoặc 1, nhưng vẫn có $\mathbb E[\widehat s]=s$. Không chệch chưa đủ để $\widehat s$ gần $s$.

### 4.3 Chi phí so sánh

Chữ ký được lập để so nhanh. Mô hình: mỗi thành phần chữ ký vừa một từ máy, và một phép so bằng hai thành phần tốn $O(1)$. Phép tính $\widehat s$ duyệt $n$ tọa độ, đếm các vị trí bằng nhau rồi chia cho $n$.

::: proposition Mệnh đề 05.13 (Chi phí so sánh hai chữ ký và mọi cặp)
**Giả thiết.** Mô hình trên; các chữ ký đã có.

**Kết luận.**

- (a) Tính $\widehat s$ cho một cặp tốn $n$ phép so bằng, tức $\Theta(n)$ thời gian.
- (b) Tính $\widehat s$ cho mọi cặp của $C$ chữ ký tốn $nC(C-1)/2$ phép so bằng.

**Điều kiện áp dụng.** Mọi chữ ký có cùng độ dài $n$ và cùng nằm trong bộ nhớ.

**Phạm vi.** Chi phí không phụ thuộc độ dài tài liệu hay kích thước tập shingle; chi phí lập chữ ký là một bước riêng (Mệnh đề 05.21).
:::

::: proof
Phép đếm theo bảng bước–số lần–chi phí.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| So một cặp chữ ký | 1 | $n$ phép so | $\Theta(n)$ |
| So mọi cặp trong kho | $C(C-1)/2$ | $n$ phép so | $nC(C-1)/2$ phép so |

Dòng đầu cho (a): mỗi tọa độ một phép so, cộng một phép chia. Dòng sau cho (b): số cặp không thứ tự là $\binom C2$, như ở Bài tập 05.1. $\square$
:::

So với Bổ đề 01.14, chi phí một cặp đổi từ không quá $|S|+|T|$ phép so sánh phần tử, tăng theo độ dài tài liệu, thành đúng $n$ phép so bằng.

<!-- note-topic-id: lec-05-topic-08 -->
### 4.4 Phương sai và độ dài chữ ký

Mệnh đề 05.12 nói về trung bình của $\widehat s$ qua các lần chọn hoán vị. Để đo mức dao động, chúng ta thêm giả thiết các hoán vị độc lập; MMDS cũng chọn các hoán vị độc lập và coi mỗi hàng của ma trận chữ ký là một phép thử độc lập (§3.3.4, tr.84). Khi đó $I_1,\ldots,I_n$ là các biến chỉ báo độc lập, cùng nhận 1 với xác suất $s$.

::: proposition Mệnh đề 05.14 (Phương sai của ước lượng)
**Giả thiết.** Các giả thiết của Mệnh đề 05.12, và thêm: $\pi_1,\ldots,\pi_n$ độc lập.

**Kết luận.**
$$
\operatorname{Var}(\widehat s)=\frac{s(1-s)}n,\qquad \text{độ lệch chuẩn }\sqrt{\frac{s(1-s)}n}.
$$

**Điều kiện áp dụng.** Mỗi $\pi_i$ chọn đều trên mọi hoán vị, các $\pi_i$ độc lập, và cùng bộ hoán vị dùng cho hai tập.

**Phạm vi.** Phương sai mô tả độ dao động của $\widehat s$ qua các lần chọn bộ hoán vị; sai số của một lần chọn cụ thể là một giá trị của $\widehat s-s$.
:::

::: proof
**Bước 1 (một tọa độ).** Vì $I_i\in\{0,1\}$, $I_i^2=I_i$, nên theo Bước 1 của chứng minh Mệnh đề 05.12
$$
\operatorname{Var}(I_i)=\mathbb E[I_i^2]-(\mathbb E[I_i])^2=s-s^2=s(1-s).
$$

**Bước 2 (trung bình của các biến độc lập cùng phân phối).** Cho $W_1,\ldots,W_n$ độc lập, cùng phân phối, có phương sai hữu hạn. Hai biến độc lập có hiệp phương sai bằng 0, nên phương sai của tổng bằng tổng các phương sai; hằng số $1/n$ ra ngoài phương sai với bình phương. Do đó
$$
\operatorname{Var}\Bigl(\frac1n\sum_{i=1}^nW_i\Bigr)=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(W_i)=\frac{\operatorname{Var}(W_1)}n .
$$

**Bước 3 (áp dụng).** Mỗi $I_i$ là hàm của riêng $\pi_i$, nên các $I_i$ độc lập khi các $\pi_i$ độc lập; theo Bước 1, chúng cùng phân phối. Bước 2 với $W_i=I_i$ cho $\operatorname{Var}(\widehat s)=s(1-s)/n$, và độ lệch chuẩn là căn bậc hai của phương sai. $\square$
:::

Bước 1 chỉ dùng cấu trúc của chữ ký; Bước 2 là đẳng thức chung cho trung bình các biến độc lập cùng phân phối; Bước 3 là bước duy nhất dùng giả thiết độc lập của các $\pi_i$. Bỏ giả thiết này thì có phản ví dụ: với $\pi_1=\cdots=\pi_n$ là cùng một hoán vị chọn đều, $\widehat s=I_1$ nên $\operatorname{Var}(\widehat s)=s(1-s)$ với mọi $n$, không giảm theo $n$.

Độ lệch chuẩn chứa $s$, mà $s$ chưa biết khi chọn $n$. Hệ quả sau cho một cận không phụ thuộc $s$.

::: corollary Hệ quả 05.15 (Cận độ lệch chuẩn $1/(2\sqrt n)$)
**Giả thiết.** Các giả thiết của Mệnh đề 05.14.

**Kết luận.** Với mọi $s\in[0,1]$,
$$
\sqrt{\operatorname{Var}(\widehat s)}\le\frac1{2\sqrt n}.
$$

**Điều kiện áp dụng.** Như Mệnh đề 05.14.

**Phạm vi.** Cận đạt dấu bằng khi $s=1/2$; với $s=0{,}1$, độ lệch chuẩn là $\sqrt{0{,}09/n}=0{,}3/\sqrt n$, bằng $0{,}6$ lần cận.
:::

::: proof
Ta có $s(1-s)=\tfrac14-\bigl(s-\tfrac12\bigr)^2\le\tfrac14$, với dấu bằng khi $s=1/2$. Thay vào Mệnh đề 05.14: $\operatorname{Var}(\widehat s)\le1/(4n)$, và lấy căn bậc hai hai vế. $\square$
:::

Muốn giảm cận độ lệch chuẩn một nửa phải tăng $n$ gấp bốn, và theo Mệnh đề 05.13 số phép so một cặp tăng theo đúng $n$. Ví dụ sau thay số cho cặp $S_1$, $S_4$.

::: example Ví dụ 05.10 (Phương sai khi $s=2/3$)
**Dữ kiện.** $s=\mathrm{SIM}(S_1,S_4)=2/3$; các hoán vị chọn đều và độc lập.

**Phương sai.** $s(1-s)=\tfrac23\cdot\tfrac13=\tfrac29$, nên $\operatorname{Var}(\widehat s)=2/(9n)$.

**Hai độ dài.**

| $n$ | $\operatorname{Var}(\widehat s)$ | Độ lệch chuẩn | Cận $1/(2\sqrt n)$ |
|---:|---|---|---|
| 100 | $2/900=1/450$ | $\approx0{,}047$ | $0{,}05$ |
| 250 | $2/2250=1/1125$ | $\approx0{,}030$ | $\approx0{,}032$ |

**Kiểm tra lại.** $\sqrt{1/450}\approx0{,}0471\le0{,}05$ và $\sqrt{1/1125}\approx0{,}0298\le0{,}0316$, đúng Hệ quả 05.15. Với $s=0$ hoặc $s=1$, $s(1-s)=0$: mọi phép thử lần lượt luôn khác hoặc luôn trùng.
:::

::: remark Nhận xét 05.16 (Hai cách đọc sai Mệnh đề 05.14)
- **Một lần chạy cụ thể.** Một chữ ký dài hơn có phương sai nhỏ hơn, nhưng trong một lần chạy, thêm tọa độ có thể làm sai số quan sát $|\widehat s-s|$ tăng: với $s=2/3$, chữ ký $n=1$ cho $\widehat s=1$ có sai số $1/3$; thêm một tọa độ không trùng cho $\widehat s=1/2$, sai số $1/6$; thêm tiếp một tọa độ không trùng cho $\widehat s=1/3$, sai số $1/3$.
- **Phép thử phụ thuộc.** Khi các tọa độ phụ thuộc nhau, phương sai của tổng có thêm các số hạng hiệp phương sai, và công thức $s(1-s)/n$ không áp dụng.
:::

**Trong thực hành.** Số hoán vị được gợi ý là khoảng 100 hoặc vài trăm (MMDS, §3.3.4, tr.83), trong khi số hàng $R$ của ma trận đặc trưng là số phần tử khác nhau của cả kho. Với mã 4 byte, chữ ký 1 000 byte có $n=250$ thành phần, và theo Hệ quả 05.15 độ lệch chuẩn của $\widehat s$ không vượt $1/(2\sqrt{250})\approx0{,}032$ trong mô hình hoán vị đều, độc lập; với chữ ký 1 000 byte, ước lượng thường lệch không quá vài phần trăm (MMDS, tr.81). Chọn $n$ là đánh đổi giữa độ lệch chuẩn, giảm theo $1/\sqrt n$, với bộ nhớ chữ ký và số phép so một cặp, tăng theo $n$ (Mệnh đề 05.13); Tình huống 05.1 thay số cho kho một triệu tài liệu.

::: exercise Bài tập 05.7 (Kỳ vọng và độ lệch chuẩn theo số liệu)
- (a) Với cặp $S_1=\{\mathrm a,\mathrm d\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$ và $n=100$ hoán vị chọn đều, tính kỳ vọng số tọa độ trùng và kỳ vọng tỷ lệ tọa độ trùng.
- (b) Cho $|S\cap T|=3$, $|S\cup T|=12$ và $n=200$ hoán vị chọn đều. Tính xác suất hai MinHash trùng ở một tọa độ và kỳ vọng số tọa độ trùng.
- (c) Với dữ kiện của câu (b) và các hoán vị độc lập, tính độ lệch chuẩn của $\widehat s$.
:::

::: hint
Câu (a), (b): Định lý 05.10 rồi Mệnh đề 05.12. Câu (c): Mệnh đề 05.14 với $s=1/4$.
:::

::: solution
**Câu (a).** $s=2/3$. Kỳ vọng số tọa độ trùng là $ns=100\cdot\tfrac23=200/3\approx66{,}7$; một kỳ vọng của số đếm có thể không nguyên. Kỳ vọng tỷ lệ là $s=2/3$.

**Câu (b).** Theo Định lý 05.10, xác suất trùng ở một tọa độ là $3/12=1/4$; theo Mệnh đề 05.12, kỳ vọng số tọa độ trùng là $200\cdot1/4=50$.

**Câu (c).** $s(1-s)=\tfrac14\cdot\tfrac34=\tfrac3{16}$, nên độ lệch chuẩn là $\sqrt{(3/16)/200}=\sqrt{3/3200}\approx0{,}031$.

**Kiểm tra lại.** Câu (c): $0{,}031\le1/(2\sqrt{200})\approx0{,}035$, đúng Hệ quả 05.15.
:::

::: exercise Bài tập 05.8 (Độ dài chữ ký cần thiết)
Các hoán vị chọn đều và độc lập.

- (a) Với $s=2/3$, xác định $n$ nhỏ nhất để độ lệch chuẩn của $\widehat s$ không vượt $0{,}02$, và số phép so bằng cho một cặp khi đó.
- (b) Khi chưa biết $s$, xác định $n$ nhỏ nhất để độ lệch chuẩn không vượt $0{,}02$ với mọi $s\in[0,1]$, và so với câu (a).
:::

::: hint
Câu (a): giải $2/(9n)\le0{,}02^2$ theo $n$ nguyên. Câu (b): dùng Hệ quả 05.15.
:::

::: solution
**Câu (a).** Theo Mệnh đề 05.14, cần $\sqrt{2/(9n)}\le0{,}02$, tức $2/(9n)\le0{,}0004$, hay $n\ge2/(9\cdot0{,}0004)=5\,000/9\approx555{,}6$. Vậy $n=556$, và theo Mệnh đề 05.13, so một cặp cần 556 phép so bằng.

**Câu (b).** Theo Hệ quả 05.15, đủ để $1/(2\sqrt n)\le0{,}02$, tức $\sqrt n\ge25$, hay $n\ge625$; với $s=1/2$, độ lệch chuẩn đúng bằng cận, nên $n=625$ là nhỏ nhất. Không biết $s$ thì cần thêm $625-556=69$ thành phần.

**Kiểm tra lại.** Câu (a): $2/(9\cdot556)\approx0{,}000\,3997\le0{,}0004$, còn $2/(9\cdot555)\approx0{,}000\,4004>0{,}0004$. Câu (b): $1/(4\cdot625)=0{,}0004$.
:::

::: exercise Bài tập 05.9 (Tập mã hay chữ ký cho kho $10^4$ thư điện tử)
Kho có $C=10^4$ thư điện tử; tập mã của mỗi thư có không quá $1\,996$ phần tử (Bài tập 05.4(b)), và chữ ký dài $n=200$. So số phép so khi xét mọi cặp trên tập mã, dùng thủ tục trộn của Bổ đề 01.14, với số phép so bằng trên chữ ký, và tìm tỷ số của hai cận.
:::

::: hint
Nhân số cặp với cận chi phí một cặp của mỗi cách.
:::

::: solution
Có $C(C-1)/2=10^4\cdot9\,999/2=49\,995\,000$ cặp. Trên tập mã, một cặp tốn không quá $1\,996+1\,996=3\,992$ phép so sánh (Bổ đề 01.14), nên tổng không quá $49\,995\,000\cdot3\,992=199\,580\,040\,000\approx2\cdot10^{11}$. Trên chữ ký, một cặp tốn $200$ phép so bằng (Mệnh đề 05.13), nên tổng là $49\,995\,000\cdot200=9\,999\,000\,000\approx10^{10}$. Tỷ số của hai cận là $3\,992/200=19{,}96$, không phụ thuộc $C$, vì cả hai cách có cùng số cặp.

**Kiểm tra lại.** $199\,580\,040\,000/9\,999\,000\,000=19{,}96$.
:::

Ước lượng $\widehat s$ của Định nghĩa 05.11 không chệch khi mỗi hoán vị chọn đều (Mệnh đề 05.12), có độ lệch chuẩn không quá $1/(2\sqrt n)$ khi các hoán vị thêm độc lập (Mệnh đề 05.14, Hệ quả 05.15), và so một cặp tốn $n$ phép so (Mệnh đề 05.13). Các kết quả này giả sử có sẵn $n$ hoán vị của $U$. Trong Mục 5, chúng ta thay mỗi hoán vị bằng một hàm băm trên mã hàng và tính toàn bộ ma trận chữ ký trong một lượt quét.

<!-- note-topic-id: lec-05-topic-09 -->
## 5. Tính chữ ký bằng hàm băm

Ví dụ 05.9 liệt kê tường minh hai hoán vị của năm phần tử. Với $R$ cỡ $2^{32}$ mã hàng, mỗi hoán vị cần $R$ số. MMDS mô phỏng mỗi hoán vị bằng một hàm băm $f_i$ trên mã hàng: xem như hàng $r$ được đưa tới vị trí $f_i(r)$, nên trong một cột, hàng có giá trị băm nhỏ nhất đóng vai phần tử đứng đầu (§3.3.5, tr.84). Lưu một hàm băm chỉ cần vài hệ số, thay cho $R$ số của một hoán vị.

### 5.1 Hàm băm thay hoán vị

Ví dụ sau dùng hai hàm băm hàng của MMDS trên bốn tập đặc trưng.

::: example Ví dụ 05.11 (Hai hàm băm hàng; MMDS Ví dụ 3.8, Hình 3.4, tr.85)
**Dữ kiện.** Bốn tập của Ví dụ 05.5, mã hàng $\mathrm a,\mathrm b,\mathrm c,\mathrm d,\mathrm e\leftrightarrow0,1,2,3,4$, và hai hàm
$$
f_1(r)=(r+1)\bmod5,\qquad f_2(r)=(3r+1)\bmod5,
$$
với phần dư lấy trong $\{0,1,2,3,4\}$.

**Bảng giá trị.**

| $r$ | Phần tử | Các cột có 1 | $f_1(r)$ | $f_2(r)$ |
|---:|---|---|---:|---:|
| 0 | a | 1, 4 | 1 | 1 |
| 1 | b | 3 | 2 | 4 |
| 2 | c | 2, 4 | 3 | 2 |
| 3 | d | 1, 3, 4 | 4 | 0 |
| 4 | e | 3 | 0 | 3 |

**Thứ tự cảm sinh.** Sắp các hàng theo $f_1$ tăng cho thứ tự $(\mathrm e,\mathrm a,\mathrm b,\mathrm c,\mathrm d)$; sắp theo $f_2$ tăng cho $(\mathrm d,\mathrm a,\mathrm c,\mathrm e,\mathrm b)$. Đó là hai hoán vị $\pi_1$, $\pi_2$ của Ví dụ 05.9.

**Một cột.** $S_1$ có các hàng $0$, $3$. Tọa độ thứ nhất: $\min(f_1(0),f_1(3))=\min(1,4)=1$, đạt tại hàng 0, tức a. Tọa độ thứ hai: $\min(f_2(0),f_2(3))=\min(1,0)=0$, đạt tại hàng 3, tức d. Chữ ký $(\mathrm a,\mathrm d)^{\mathsf T}$ của Ví dụ 05.9 được lưu bằng các giá trị băm nhỏ nhất $(1,0)^{\mathsf T}$.

**Kiểm tra lại.** Mỗi cột $f_1$, $f_2$ của bảng chứa đủ năm giá trị $0,\ldots,4$, nên không có hai hàng cùng giá trị.
:::

![Bảng f1 của năm hàng a đến e cho 1, 2, 3, 4, 0; sắp theo f1 tăng được thứ tự e, a, b, c, d. Trong S1 = {a, d}, a đứng đầu và có giá trị băm nhỏ nhất: min(f1(0), f1(3)) = min(1, 4) = 1.](img/lec-05/bam-thay-hoan-vi.svg)

Hình đặt bảng $f_1$ cạnh thứ tự cảm sinh: phần tử đứng đầu của $S_1$ theo thứ tự ấy, a, cũng là hàng có giá trị $f_1$ nhỏ nhất trong $S_1$. Khi hàm không có hai hàng cùng giá trị, phần tử đứng đầu của một tập là hàng có giá trị băm nhỏ nhất, nên chỉ cần lấy cực tiểu, không cần sắp xếp. Đặc tả sau nêu đầu ra cho mọi bộ hàm, kể cả hàm có va chạm.

::: definition Định nghĩa 05.17 (Bài toán tính ma trận chữ ký)
**Đầu vào.** Các số nguyên dương $R$, $C$, $n$; ma trận đặc trưng $M\in\{0,1\}^{R\times C}$ (Định nghĩa 05.7), cho dưới dạng ma trận đặc hoặc biểu diễn theo hàng; $n$ hàm
$$
f_i:\{0,\ldots,R-1\}\longrightarrow V,\qquad i=1,\ldots,n,
$$
trong đó $V$ là một tập hữu hạn có thứ tự toàn phần. Mỗi $f_i$ là một hàm cố định: nó cho cùng giá trị trên cùng mã hàng ở mọi lần gọi và được dùng chung cho mọi cột. Giá trị canh $+\infty$ lớn hơn mọi phần tử của $V$.

**Đầu ra.** Ma trận $\mathrm{SIG}\in(V\cup\{+\infty\})^{n\times C}$ với
$$
\mathrm{SIG}(i,c)=\min\bigl(\{f_i(r):0\le r<R,\ M(r,c)=1\}\cup\{+\infty\}\bigr),
$$
cho $i=1,\ldots,n$ và $c=1,\ldots,C$.
:::

Với cột không rỗng, tập lấy cực tiểu có ít nhất một giá trị hữu hạn, nên $\mathrm{SIG}(i,c)\in V$. Với cột rỗng, tập ấy chỉ có $+\infty$, nên mọi thành phần của cột chữ ký bằng $+\infty$; đây là quy ước đầu ra, còn $\mathrm{SIM}(\varnothing,\varnothing)$ vẫn không xác định.

Định nghĩa 05.17 khác Định nghĩa 05.11 ở hai điểm. Thứ nhất, $\mathrm{SIG}(i,c)$ lưu giá trị băm nhỏ nhất, còn $h_{\pi_i}(S_c)$ là định danh phần tử. Thứ hai, $f_i$ là một hàm đã cho, không cần là song ánh. Nếu $f_i$ là đơn ánh trên các mã hàng (với $V=\{0,\ldots,R-1\}$, đơn ánh tương đương song ánh), sắp hàng theo $f_i$ tăng cho một hoán vị $\pi_i$, hàng đạt cực tiểu của cột $c$ là $h_{\pi_i}(S_c)$, và vì $f_i$ đơn ánh,
$$
\mathrm{SIG}(i,c)=\mathrm{SIG}(i,c')\iff h_{\pi_i}(S_c)=h_{\pi_i}(S_{c'})
$$
với hai cột không rỗng $c$, $c'$. Khi đó so giá trị cho cùng kết quả với so định danh, và ước lượng $\widehat s$ của Định nghĩa 05.11 tính được từ $\mathrm{SIG}$. Nếu $f_i$ có va chạm, hai hàng khác nhau có thể cho cùng cực tiểu, và tương đương này có thể hỏng.

### 5.2 Thuật toán quét hàng

Định nghĩa 05.17 lấy cực tiểu theo từng cột, nhưng biểu diễn theo hàng cho dữ liệu theo từng phần tử. Ví dụ sau tính cùng ma trận bằng cách đọc lần lượt các hàng, tính $n$ giá trị băm một lần cho mỗi hàng, rồi cập nhật đúng những cột có 1.

::: example Ví dụ 05.12 (Vết chạy trên bốn tập đặc trưng; MMDS Ví dụ 3.8, tr.85–86)
**Dữ kiện.** Bảng của Ví dụ 05.11: hàng 0 (a) có 1 ở cột 1, 4 và $(f_1,f_2)=(1,1)$; hàng 1 (b) ở cột 3, $(2,4)$; hàng 2 (c) ở cột 2, 4, $(3,2)$; hàng 3 (d) ở cột 1, 3, 4, $(4,0)$; hàng 4 (e) ở cột 3, $(0,3)$.

**Vết chạy.** Khởi tạo mọi ô bằng $+\infty$. Mỗi dòng ghi hai hàng của $\mathrm{SIG}$ sau khi xử lý một hàng; vị trí trong véc-tơ ứng với $S_1,S_2,S_3,S_4$.

| Trạng thái | Hàng chữ ký thứ nhất ($f_1$) | Hàng chữ ký thứ hai ($f_2$) |
|---|---|---|
| Khởi tạo | $(+\infty,+\infty,+\infty,+\infty)$ | $(+\infty,+\infty,+\infty,+\infty)$ |
| Sau $r=0$ | $(1,+\infty,+\infty,1)$ | $(1,+\infty,+\infty,1)$ |
| Sau $r=1$ | $(1,+\infty,2,1)$ | $(1,+\infty,4,1)$ |
| Sau $r=2$ | $(1,3,2,1)$ | $(1,2,4,1)$ |
| Sau $r=3$ | $(1,3,2,1)$ | $(0,2,0,0)$ |
| Sau $r=4$ | $(1,3,0,1)$ | $(0,2,0,0)$ |

**Đọc từng hàng.**

- Hàng 0: chỉ $S_1$, $S_4$ chứa a; hai giá trị băm bằng 1, nên bốn phép min đổi bốn ô từ $+\infty$ thành 1. Hai cột còn lại giữ nguyên dù giá trị băm đã được tính.
- Hàng 1: chỉ cột $S_3$ nhận $(2,4)$, giá trị hữu hạn đầu tiên của nó.
- Hàng 2: cột $S_2$ nhận $(3,2)$ từ trạng thái vô cực; cột $S_4$ đang là $(1,1)$ nên $\min(1,3)=1$ và $\min(1,2)=1$. Hai phép min này được thực hiện dù không ô nào đổi.
- Hàng 3: ứng viên $(4,0)$ cho $S_1$, $S_3$, $S_4$; chỉ thành phần thứ hai giảm về 0.
- Hàng 4: chỉ $S_3$ nhận $(0,3)$; thành phần thứ nhất giảm từ 2 về 0, thành phần thứ hai giữ 0 vì $\min(0,3)=0$.

**Kết quả.**
$$
\mathrm{SIG}=\begin{pmatrix}1&3&0&1\\0&2&0&0\end{pmatrix}.
$$
Cặp $S_1$, $S_4$ trùng cả hai tọa độ, nên $\widehat s=1$ so với $\mathrm{SIM}(S_1,S_4)=2/3$; cặp $S_1$, $S_3$ trùng tọa độ thứ hai, nên $\widehat s=1/2$ so với $\mathrm{SIM}(S_1,S_3)=1/4$.

**Kiểm tra lại.** Theo Định nghĩa 05.17, $\mathrm{SIG}(1,3)=\min(f_1(1),f_1(3),f_1(4))=\min(2,4,0)=0$ và $\mathrm{SIG}(2,3)=\min(4,0,3)=0$; số phép min là $2\cdot9=18$, tức hai phép cho mỗi ô 1. Cột $S_3$ đạt hai cực tiểu ở hai hàng khác nhau (e cho $f_1$, d cho $f_2$).
:::

Số phép min (18) không bằng số lần một ô giảm giá trị: ở hàng 2, hai phép min của cột $S_4$ giữ nguyên giá trị. Thuật toán sau làm đúng vết chạy trên cho mọi đầu vào.

::: algorithm Thuật toán 05.18 (Quét hàng)
**Đầu vào.** Như Định nghĩa 05.17: $R$, $C$, $n$; với mỗi hàng $r$, danh sách các cột $c$ có $M(r,c)=1$ (hoặc ma trận đặc $M$); các hàm $f_1,\ldots,f_n$.

**Đầu ra.** Ma trận $\mathrm{SIG}$ của Định nghĩa 05.17.

**Giả thiết.** Mỗi $f_i$ cố định và dùng chung cho mọi cột; $+\infty$ lớn hơn mọi phần tử của $V$.

1. Đặt $\mathrm{SIG}(i,c)\leftarrow+\infty$ với mọi $i=1,\ldots,n$ và $c=1,\ldots,C$.
2. Với mỗi hàng $r=0,1,\ldots,R-1$:
   1. tính $v_i\leftarrow f_i(r)$ với $i=1,\ldots,n$;
   2. với mỗi cột $c$ có $M(r,c)=1$ và mỗi $i=1,\ldots,n$: đặt $\mathrm{SIG}(i,c)\leftarrow\min(\mathrm{SIG}(i,c),v_i)$.
3. Trả $\mathrm{SIG}$.

**Dừng.** Bước 2 xử lý mỗi hàng đúng một lần và dừng sau $R$ hàng.

**Trường hợp biên.** Cột không có ô 1 nào không được cập nhật và giữ toàn $+\infty$. Thứ tự xử lý các hàng ở bước 2 có thể tùy ý (Hệ quả 05.20). Với ma trận đặc, bước 2.2 phải kiểm $C$ ô của hàng $r$; với biểu diễn theo hàng, nó đi thẳng qua danh sách.

**Chi phí.** Mô hình: mỗi mã hàng, chỉ số cột và giá trị chữ ký vừa một từ máy; ghi một ô, tính một $f_i(r)$, kiểm một ô và lấy một phép min đều tốn một đơn vị.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1 (khởi tạo) | $nC$ ô | 1 | $nC$ |
| 2.1 (tính băm) | $nR$ giá trị | 1 | $nR$ |
| 2.2, kiểm ô (chỉ ma trận đặc) | $RC$ ô | 1 | $RC$ |
| 2.2, lấy min | $n$ cho mỗi ô 1, tức $nL$ | 1 | $nL$ |

Tổng là $nC+nR+RC+nL$ thao tác với ma trận đặc và $nC+nR+nL$ với biểu diễn theo hàng, cộng $O(1)$ cho bước 3 (Mệnh đề 05.21).
:::

```text
SIG(i, c) ← +∞ với mọi i = 1, …, n và c = 1, …, C
for r = 0, …, R − 1:
    vᵢ ← fᵢ(r) với i = 1, …, n
    for mỗi c có M(r, c) = 1:
        for i = 1, …, n:
            SIG(i, c) ← min(SIG(i, c), vᵢ)
return SIG
```

Thao tác quyết định là phép min ở bước 2.2: mỗi giá trị $v_i=f_i(r)$ được tính một lần ở hàng $r$ rồi dùng cho mọi cột chứa phần tử ấy, nên hàm $f_i$ tự động được dùng chung cho mọi cột. Giả mã dùng đúng ký hiệu của Ví dụ 05.12: với $n=2$, mỗi dòng của bảng vết chạy là trạng thái sau một lượt của vòng ngoài. Thuật toán để ngỏ cách chọn các $f_i$.

![Phép quét hàng: với mỗi hàng r, tính n giá trị băm một lần; danh sách cột chứa hàng r xác định các chữ ký cần cập nhật bằng phép min theo từng thành phần; sau đó chuyển tới hàng kế tiếp.](img/lec-05/quet-ma-tran-thua.svg)

Hình đọc từ trái sang phải cho một hàng: khối tính $n$ giá trị băm, danh sách cột của hàng, và các cột chữ ký nhận phép min. Chỉ những cột có trong danh sách được chạm tới; đó là lý do biểu diễn theo hàng loại được các ô 0.

<!-- note-topic-id: lec-05-topic-10 -->
### 5.3 Tính đúng

Vết chạy của Ví dụ 05.12 cho đúng ma trận của Định nghĩa 05.17 trên một đầu vào. Muốn có kết luận cho mọi đầu vào, chúng ta dùng một bất biến trên tập các hàng đã xử lý.

::: proposition Mệnh đề 05.19 (Tính đúng của Thuật toán 05.18)
**Giả thiết.** Đầu vào và giả thiết của Thuật toán 05.18.

**Kết luận.** Thuật toán dừng sau $R$ lượt của bước 2 và trả đúng ma trận $\mathrm{SIG}$ của Định nghĩa 05.17, kể cả các cột rỗng.

**Điều kiện áp dụng.** Phép min và phép so trên $V\cup\{+\infty\}$ chính xác; không bước nào ngoài bước 1 và bước 2.2 ghi vào $\mathrm{SIG}$.

**Phạm vi.** Giá trị của các cực tiểu, với mọi bộ hàm $f_i$, kể cả hàm có va chạm; bảo đảm xác suất cho $\widehat s$ cần thêm các giả thiết của Định lý 05.10.
:::

::: proof
Gọi $H$ là tập các mã hàng đã xử lý ở bước 2. Bất biến: với mọi $i=1,\ldots,n$ và $c=1,\ldots,C$,
$$
\mathrm{SIG}(i,c)=\min\bigl(\{f_i(r):r\in H,\ M(r,c)=1\}\cup\{+\infty\}\bigr).
$$

**Bước 1 (khởi tạo).** Khi $H=\varnothing$, tập giá trị hữu hạn rỗng, và cực tiểu của $\{+\infty\}$ là $+\infty$, đúng giá trị đặt ở bước 1.

**Bước 2 (duy trì).** Xét một hàng mới $r\notin H$. Nếu $M(r,c)=0$, hàng $r$ không thêm giá trị nào cho cột $c$, và bước 2.2 không chạm tới cột $c$, nên bất biến của cột $c$ giữ nguyên. Nếu $M(r,c)=1$, tập giá trị của cột $c$ ở thành phần $i$ được thêm đúng $f_i(r)=v_i$; cực tiểu của tập mới bằng $\min$ của cực tiểu cũ và $v_i$, đúng phép gán ở bước 2.2. Vậy bất biến đúng với $H\cup\{r\}$.

**Bước 3 (kết thúc).** Vòng lặp xử lý mỗi mã hàng đúng một lần và dừng khi $H=\{0,\ldots,R-1\}$. Thay vào bất biến được đúng công thức đầu ra của Định nghĩa 05.17. Với cột rỗng, không bước nào thêm giá trị hữu hạn, nên kết quả là $+\infty$. $\square$
:::

Các giả thiết của Mệnh đề 05.19 và cấu trúc bước 2 của Thuật toán 05.18 có vai trò riêng, và mỗi điều bị bỏ đều có phản ví dụ. Các phản ví dụ dưới đây dùng dữ kiện của Ví dụ 05.12.

- Bỏ "$+\infty$ lớn hơn mọi phần tử của $V$": nếu khởi tạo bằng $0\in V$, mọi phép min giữ 0 và thuật toán trả ma trận toàn 0, trong khi $\mathrm{SIG}(1,1)=1$.
- Bỏ việc bước 2 xử lý đủ $R$ hàng: nếu dừng sau ba hàng $r=0,1,2$, cột $S_1$ là $(1,1)^{\mathsf T}$ thay cho $(1,0)^{\mathsf T}$, vì hàng 3 với $f_2(3)=0$ chưa được xét.
- Bỏ "$f_i$ cố định": nếu bước 2.1 được tính lại cho từng cột và $f_2$ cho hàng 3 giá trị 0 với cột $S_1$ nhưng giá trị 4 với cột $S_4$, thì cột $S_4$ cho $\min(1,2,4)=1$ ở thành phần thứ hai, và $S_1$, $S_4$ không còn so được dưới cùng một thứ tự.

Bước 1 của chứng minh dùng giả thiết về $+\infty$; Bước 3 dùng việc bước 2 xử lý đủ $R$ hàng; Bước 2 dùng việc mỗi $v_i$ là một giá trị duy nhất của $f_i(r)$ cho mọi cột. Bất biến không phụ thuộc thứ tự các hàng, nên ta có hệ quả sau.

::: corollary Hệ quả 05.20 (Thứ tự quét không đổi kết quả)
**Giả thiết.** Các giả thiết của Mệnh đề 05.19; bước 2 xử lý các hàng theo một thứ tự bất kỳ, mỗi hàng đúng một lần.

**Kết luận.** Ma trận trả về không phụ thuộc thứ tự quét.

**Điều kiện áp dụng.** Như Mệnh đề 05.19.

**Phạm vi.** Các trạng thái trung gian có thể khác nhau giữa hai thứ tự; chỉ trạng thái cuối trùng nhau.
:::

::: proof
Chứng minh Mệnh đề 05.19 không dùng thứ tự của các hàng: bước duy trì đúng với bất kỳ hàng $r\notin H$ nào được xử lý tiếp. Khi dừng, $H=\{0,\ldots,R-1\}$ với mọi thứ tự, nên $\mathrm{SIG}$ bằng cùng một vế phải của Định nghĩa 05.17. Điều này ứng với tính giao hoán và kết hợp của phép min: cực tiểu của cùng một tập giá trị không phụ thuộc thứ tự lấy. $\square$
:::

### 5.4 Chi phí thời gian và bộ nhớ

Bảng chi phí của Thuật toán 05.18 đếm bốn loại thao tác. Mệnh đề sau cộng chúng lại cho hai dạng đầu vào.

::: proposition Mệnh đề 05.21 (Chi phí thời gian và bộ nhớ của Thuật toán 05.18)
**Giả thiết.** Mô hình chi phí của Thuật toán 05.18; $L=\operatorname{nnz}(M)$.

**Kết luận.**

- (a) Với ma trận đặc, thời gian là $\Theta(nC+nR+RC+nL)$.
- (b) Với biểu diễn theo hàng đã có sẵn, thời gian là $\Theta(nC+nR+nL)$.
- (c) Bộ nhớ làm việc gồm $\Theta(nC)$ từ máy cho $\mathrm{SIG}$ và $\Theta(n)$ từ máy cho $v_1,\ldots,v_n$, chưa tính đầu vào.
- (d) Thuật toán đọc mỗi hàng của đầu vào đúng một lần.

**Điều kiện áp dụng.** Đầu vào đã có; chi phí xây biểu diễn theo hàng từ ma trận đặc không nằm trong (b).

**Phạm vi.** Đơn vị là thao tác của mô hình chi phí; $nL$ đếm mọi phép min, kể cả phép giữ nguyên giá trị.
:::

::: proof
**Bước 1 (thời gian).** Cộng cột đóng góp của bảng chi phí: $nC+nR+RC+nL$ với ma trận đặc. Với biểu diễn theo hàng, bước 2.2 đi thẳng qua danh sách của hàng $r$, nên không có $RC$ phép kiểm ô; đọc $L$ phần tử danh sách tốn $L\le nL$, không đổi bậc. Điều này cho (a) và (b).

**Bước 2 (bộ nhớ).** $\mathrm{SIG}$ có $nC$ ô, mỗi ô một từ; bộ đệm $v_1,\ldots,v_n$ của hàng đang xét có $n$ từ và được dùng lại cho hàng sau. Điều này cho (c).

**Bước 3 (một lượt).** Bước 2 xử lý mỗi hàng đúng một lần (Mệnh đề 05.19). Điều này cho (d). $\square$
:::

Mệnh đề 05.21(d) nghĩa là khi đầu vào nằm trên đĩa theo thứ tự hàng, tính toàn bộ ma trận chữ ký tốn một lượt quét (Định nghĩa 01.4). Ví dụ sau thay số cho bốn tập đặc trưng.

::: example Ví dụ 05.13 (Đếm thao tác trên Ví dụ 05.12)
**Dữ kiện.** $R=5$, $C=4$, $n=2$; $L=2+1+2+3+1=9$ (Định nghĩa 05.7, Ví dụ 05.5).

**Bốn loại thao tác.**

| Bước | Số lần | Giá trị |
|---|---|---:|
| Khởi tạo | $nC=2\cdot4$ | 8 |
| Tính băm | $nR=2\cdot5$ | 10 |
| Kiểm ô (ma trận đặc) | $RC=5\cdot4$ | 20 |
| Lấy min | $nL=2\cdot9$ | 18 |

**Tổng.** Ma trận đặc: $8+10+20+18=56$ thao tác; biểu diễn theo hàng: $8+10+18=36$ thao tác.

**Kiểm tra lại.** Số phép min theo từng hàng của vết chạy là $4+2+4+6+2=18$, kể cả hai phép min ở hàng 2 giữ nguyên giá trị của cột $S_4$.
:::

Trên ví dụ nhỏ, phép kiểm ô chiếm 20 trong 56 thao tác. Với ma trận thưa của dữ liệu thật, $RC$ lớn hơn nhiều so với $nC+nR+nL$ khi $n$ nhỏ hơn nhiều so với $R$ và $C$, và tỷ lệ ô 1, $L/(RC)$, nhỏ hơn nhiều so với $1/n$; khi đó biểu diễn theo hàng loại đúng số hạng chi phối.

**Trong thực hành.** Đầu ra của Thuật toán 05.18 cần $nC$ giá trị. Với mã 4 byte và $n=250$, mỗi chữ ký chiếm $250\cdot4=1\,000$ byte, thay cho tập mã khoảng $200\,000$ byte của một tài liệu $50\,000$ byte, tức khoảng $1/200$ (MMDS, tr.81). So số hàng $n<R$ chưa đủ để kết luận tiết kiệm: một ô của ma trận đặc trưng là một bit, còn một thành phần chữ ký là một từ máy. Cần so $nC$ từ máy của chữ ký với $L$ chỉ số của biểu diễn theo hàng. Với $10^6$ tài liệu, ma trận chữ ký chiếm $10^9$ byte, vừa bộ nhớ chính (MMDS Ví dụ 3.10, tr.92); Tình huống 05.1 đếm thêm thời gian lập nó.

<!-- note-topic-id: lec-05-topic-11 -->
### 5.5 Điều kiện đối với hàm băm hàng

Mệnh đề 05.19 đúng với mọi bộ hàm, còn tương đương "so giá trị ⟺ so định danh" ở Mục 5.1 được bảo đảm khi mỗi $f_i$ đơn ánh; với $V=\{0,\ldots,R-1\}$, đơn ánh tương đương song ánh. Hai hàm của Ví dụ 05.11 có dạng $(\alpha r+\beta)\bmod R$; mệnh đề sau cho điều kiện chính xác để một hàm như vậy là hoán vị.

::: proposition Mệnh đề 05.22 (Hàm affine là hoán vị khi và chỉ khi $\gcd(\alpha,R)=1$)
**Giả thiết.** $R\ge1$; $\alpha$, $\beta$ là số nguyên; $f(r)=(\alpha r+\beta)\bmod R$ với phần dư lấy trong $\{0,\ldots,R-1\}$.

**Kết luận.** $f$ là một song ánh từ $\{0,\ldots,R-1\}$ lên chính nó khi và chỉ khi $\gcd(\alpha,R)=1$.

**Điều kiện áp dụng.** $f$ xét trên đúng $R$ mã hàng, với cùng modulo $R$.

**Phạm vi.** Một hàm cố định với $\alpha$, $\beta$ đã chọn.
:::

::: proof
**Bước 1 ($\gcd(\alpha,R)=1$ kéo theo song ánh).** Giả sử $f(r)=f(r')$ với $r,r'\in\{0,\ldots,R-1\}$. Khi đó $\alpha(r-r')\equiv0\pmod R$. Vì $\gcd(\alpha,R)=1$, $R$ chia hết $r-r'$; mà $|r-r'|<R$, nên $r=r'$. Vậy $f$ đơn ánh, và một đơn ánh từ một tập hữu hạn vào chính nó là song ánh.

**Bước 2 ($d=\gcd(\alpha,R)>1$ kéo theo va chạm).** Đặt $r'=R/d$, một mã hàng trong $\{1,\ldots,R-1\}$ vì $d>1$ và $d$ chia hết $R$. Ta có $\alpha r'=(\alpha/d)R\equiv0\pmod R$, nên $f(r')=\beta\bmod R=f(0)$ với $r'\ne0$. Vậy $f$ không đơn ánh. Bước 1 và Bước 2 cho hai chiều của mệnh đề. $\square$
:::

Hai hàm của Ví dụ 05.11 có hệ số $\alpha=1$ và $\alpha=3$, nguyên tố cùng nhau với $R=5$, nên là hoán vị, đúng như bảng giá trị. $R$ không cần là số nguyên tố: với $R=4$, hàm $(3r+1)\bmod4$ cho $1,0,3,2$, một hoán vị vì $\gcd(3,4)=1$; còn $(2r+1)\bmod4$ cho $1,3,1,3$, và hai hàng $0$, $R/d=2$ cùng giá trị 1, đúng Bước 2 với $d=2$.

::: remark Nhận xét 05.23 (Song ánh, phân phối đều và hai tầng va chạm)
- **Song ánh chưa đủ.** Định lý 05.10 cần $\pi$ chọn đều trên mọi $R!$ hoán vị. Họ các hàm affine song ánh modulo 5, $\{(\alpha r+\beta)\bmod5:\alpha\in\{1,2,3,4\},\ \beta\in\{0,\ldots,4\}\}$, chỉ có 20 hàm, trong khi có $5!=120$ hoán vị. Chọn đều một hàm trong họ này, cặp $S_1$, $S_4$ của Ví dụ 05.5 trùng ở 13 trong 20 hàm, tức với xác suất $13/20$, khác $\mathrm{SIM}(S_1,S_4)=2/3$; cặp $S_2$, $S_4$ trùng với xác suất $7/20$, khác $1/3$. Kiểm bảng giá trị của từng hàm phát hiện được va chạm nhưng không xác định được phân phối của cả họ.
- **Hai tầng va chạm.** Va chạm của mã shingle (Mục 2.4) xảy ra trước khi lập chữ ký: hai chuỗi con khác nhau bị gộp thành một phần tử, nên tập đầu vào đã đổi. Va chạm của hàm băm hàng xảy ra trong phép lấy cực tiểu: hai hàng khác nhau cho cùng giá trị $f_i(r)$, nên hai tập rời có thể có cùng cực tiểu. Do đó có ba đối tượng cần tách: văn bản gốc, tập phần tử sau mã hóa và chữ ký của tập ấy; Định lý 05.10 bảo toàn Jaccard của tập phần tử sau mã hóa.
- **Họ hàm trong cài đặt.** CS246 (trang chiếu 33) chọn ngẫu nhiên các hàm dạng $((\alpha r+\beta)\bmod p)\bmod R$, với $\alpha$, $\beta$ nguyên ngẫu nhiên và $p$ là số nguyên tố, $p>R$ (CS246 viết $h_{a,b}$ và $N$). Lấy $\bmod R$ sau $\bmod p$ có thể cho hai hàng cùng giá trị, nên thứ tự cảm sinh không luôn là hoán vị; họ cũng chỉ có không quá $p^2$ hàm, nên khi $p^2<R!$ nó không chọn đều trên mọi hoán vị. Các đẳng thức của Mục 3 và Mục 4 khi đó trở thành xấp xỉ.
:::

Tập rỗng là trường hợp biên còn lại: nếu tài liệu ngắn hơn $k$ ký tự thì $S_k(D)=\varnothing$ (Định nghĩa 05.2), Thuật toán 05.18 vẫn trả cột toàn $+\infty$ theo đặc tả, nhưng Định lý 05.10 không áp dụng cho cột ấy.

::: exercise Bài tập 05.10 (Hàng chữ ký thứ ba)
Dùng bốn tập đặc trưng của Ví dụ 05.12: hàng 0 có 1 ở cột 1, 4; hàng 1 ở cột 3; hàng 2 ở cột 2, 4; hàng 3 ở cột 1, 3, 4; hàng 4 ở cột 3. Thêm hàm $f_3(r)=(4r+2)\bmod5$. Chạy Thuật toán 05.18 cho riêng hàng chữ ký thứ ba, ghi trạng thái $(\mathrm{SIG}(3,1),\ldots,\mathrm{SIG}(3,4))$ sau mỗi hàng, và đếm các phép min không làm ô nào giảm.
:::

::: hint
Lập bảng $f_3(0),\ldots,f_3(4)$ trước; mỗi ô 1 của hàng $r$ gây một phép min với $f_3(r)$.
:::

::: solution
Các giá trị là $f_3(0),\ldots,f_3(4)=2,1,0,4,3$.

| Trạng thái | $(\mathrm{SIG}(3,1),\mathrm{SIG}(3,2),\mathrm{SIG}(3,3),\mathrm{SIG}(3,4))$ | Phép min không giảm |
|---|---|---:|
| Khởi tạo | $(+\infty,+\infty,+\infty,+\infty)$ | — |
| Sau $r=0$ ($v=2$, cột 1, 4) | $(2,+\infty,+\infty,2)$ | 0 |
| Sau $r=1$ ($v=1$, cột 3) | $(2,+\infty,1,2)$ | 0 |
| Sau $r=2$ ($v=0$, cột 2, 4) | $(2,0,1,0)$ | 0 |
| Sau $r=3$ ($v=4$, cột 1, 3, 4) | $(2,0,1,0)$ | 3 |
| Sau $r=4$ ($v=3$, cột 3) | $(2,0,1,0)$ | 1 |

Có 9 phép min, trong đó 4 phép không làm ô nào giảm: ba phép ở hàng 3, vì $4$ lớn hơn mọi giá trị đang lưu, và một phép ở hàng 4. Hàng chữ ký mới là $(2,0,1,0)$.

**Kiểm tra lại.** $\gcd(4,5)=1$ nên $f_3$ là hoán vị (Mệnh đề 05.22); theo Định nghĩa 05.17, $\mathrm{SIG}(3,3)=\min(f_3(1),f_3(3),f_3(4))=\min(1,4,3)=1$.
:::

::: exercise Bài tập 05.11 (Số thao tác và quét ngược)
Dùng dữ kiện của Ví dụ 05.11: $R=5$, $C=4$, $n=2$, $L=9$; hàng 0 có 1 ở cột 1, 4 và $(f_1,f_2)=(1,1)$; hàng 1 ở cột 3, $(2,4)$; hàng 2 ở cột 2, 4, $(3,2)$; hàng 3 ở cột 1, 3, 4, $(4,0)$; hàng 4 ở cột 3, $(0,3)$.

- (a) Thêm hàm thứ ba, tức $n=3$. Đếm số lần khởi tạo, tính hàm băm, kiểm ô khi dùng ma trận đặc và lấy min, rồi tính tổng cho ma trận đặc và cho biểu diễn theo hàng.
- (b) Quét các hàng theo thứ tự ngược $r=4,3,2,1,0$. Ghi trạng thái chữ ký sau $r=4$ và sau $r=3$, rồi giải thích vì sao ma trận cuối không đổi.
:::

::: hint
Câu (a): bảng chi phí của Thuật toán 05.18. Câu (b): Hệ quả 05.20.
:::

::: solution
**Câu (a).** Với $n=3$: $nC=12$, $nR=15$, $RC=20$ và $nL=3\cdot9=27$. Ma trận đặc cần $12+15+20+27=74$ thao tác; biểu diễn theo hàng bỏ 20 phép kiểm ô nên cần $54$. Thêm một hàm tăng ba số hạng $nC$, $nR$, $nL$ theo $n$, còn $RC$ không đổi.

**Câu (b).** Hàng 4 (e) chỉ thuộc $S_3$ và cho $(0,3)$, nên sau $r=4$ chỉ cột 3 là $(0,3)^{\mathsf T}$, ba cột còn lại là $(+\infty,+\infty)^{\mathsf T}$. Hàng 3 (d) cho $(4,0)$ ở các cột 1, 3, 4, nên sau $r=3$ bốn cột là $(4,0)^{\mathsf T}$, $(+\infty,+\infty)^{\mathsf T}$, $(0,0)^{\mathsf T}$, $(4,0)^{\mathsf T}$. Sau cả năm hàng, ma trận vẫn là $\begin{pmatrix}1&3&0&1\\0&2&0&0\end{pmatrix}$: theo Hệ quả 05.20, mỗi ô là cực tiểu của cùng một tập giá trị, nên thứ tự quét chỉ đổi các trạng thái trung gian.

**Kiểm tra lại.** Câu (a): $74-56=18=C+R+L$, đúng phần tăng khi $n$ tăng thêm 1 so với Ví dụ 05.13. Câu (b): sau $r=2$ (c, $(3,2)$ ở cột 2, 4), cột 4 thành $(\min(4,3),\min(0,2))=(3,0)$; hàng 0 hạ nó về $(1,0)$, đúng cột $S_4$ của ma trận cuối.
:::

::: exercise Bài tập 05.12 (Một hàm affine modulo 6 và hai loại bảo đảm)
- (a) Với $f(r)=(4r+1)\bmod6$, tính thành phần chữ ký của tập hàng $\{0,3\}$, và xác định $f$ có là hoán vị của $\{0,\ldots,5\}$ không.
- (b) Dùng $f$ của câu (a) làm hàm duy nhất ($n=1$) cho hai tập rời $S=\{0\}$ và $T=\{3\}$ trên sáu hàng. Tính $\widehat s$ và so với $\mathrm{SIM}(S,T)$; chỉ ra kết quả nào trong Mệnh đề 05.19 và Định lý 05.10 vẫn đúng trên dữ kiện này.
:::

::: hint
Câu (a): tính $f(0)$, $f(3)$ và dùng Mệnh đề 05.22. Câu (b): mỗi kết quả cần những giả thiết nào, và $f$ thỏa giả thiết nào.
:::

::: solution
**Câu (a).** $f(0)=1$ và $f(3)=13\bmod6=1$, nên thành phần chữ ký là $\min(1,1)=1$, và hai hàng của tập va chạm. Vì $\gcd(4,6)=2\ne1$, theo Mệnh đề 05.22 $f$ không là hoán vị; các giá trị $f(0),\ldots,f(5)$ là $1,5,3,1,5,3$, chỉ phủ ba phần dư.

**Câu (b).** $\mathrm{SIG}$ của $S$ là $f(0)=1$, của $T$ là $f(3)=1$, nên $\widehat s=1$, trong khi $S\cap T=\varnothing$ cho $\mathrm{SIM}(S,T)=0$. Thuật toán 05.18 vẫn trả đúng các cực tiểu, nên Mệnh đề 05.19 đúng với $f$. Định lý 05.10 không áp dụng: $f$ không là hoán vị, và một hàm cố định không phải hoán vị chọn đều.

**Kiểm tra lại.** Câu (a): với $d=2$, Bước 2 của chứng minh Mệnh đề 05.22 cho hai hàng $0$ và $R/d=3$ cùng giá trị, đúng cặp hàng của tập $\{0,3\}$. Câu (b): với một hoán vị, hai tập rời luôn cho hai cực tiểu khác nhau.
:::

Thuật toán 05.18 tính đúng ma trận chữ ký của Định nghĩa 05.17 với mọi bộ hàm và mọi thứ tự quét (Mệnh đề 05.19, Hệ quả 05.20), trong một lượt quét với $\Theta(nC+nR+nL)$ thao tác và $\Theta(nC)$ từ máy bộ nhớ (Mệnh đề 05.21). Hàm affine là hoán vị khi và chỉ khi $\gcd(\alpha,R)=1$ (Mệnh đề 05.22), nhưng một họ song ánh vẫn chưa chọn đều trên mọi hoán vị (Nhận xét 05.23). Số cặp $\binom C2$ của Ví dụ 05.1 không đổi; Bài 06 giảm thừa số này bằng phân dải ma trận chữ ký.

<!-- note-collapsed -->
## Đọc thêm: Biến thể của biểu diễn và của phép quét

Từ Mục 1 đến Mục 5, chúng ta cố định hai lựa chọn: phần tử của tập là các đoạn $k$ ký tự, và mỗi thành phần chữ ký được tính trên đủ $R$ hàng. MMDS xét biến thể của cả hai lựa chọn. Biến thể của biểu diễn đổi đối tượng mà Jaccard đo, nên Định lý 05.10 không áp dụng cho Định nghĩa 05.24; biến thể của phép quét đổi số phép thử được tính vào ước lượng, nên công thức $s(1-s)/n$ của Mệnh đề 05.14 không áp dụng trực tiếp cho Nhận xét 05.26.

<!-- note-topic-id: lec-05-topic-12 -->
### Đa tập và shingle theo từ dừng

MMDS nêu hai biến thể của biểu diễn: đếm cả số lần xuất hiện của mỗi phần tử (§3.1.3, tr.77), và chọn phần tử là cụm từ bắt đầu bằng một từ dừng (§3.2.4, tr.80).

Một *đa tập* (bag, multiset) cho phép một phần tử xuất hiện nhiều lần; ký hiệu $\mu_B(u)$ là số lần $u$ xuất hiện trong đa tập $B$, gọi là bội của $u$.

::: definition Định nghĩa 05.24 (Độ tương đồng Jaccard của đa tập; MMDS §3.1.3, tr.77)
Cho hai đa tập hữu hạn $B_1$, $B_2$ với $\sum_u\bigl(\mu_{B_1}(u)+\mu_{B_2}(u)\bigr)>0$. Giao đa tập lấy bội nhỏ hơn, hợp đa tập cộng các bội, và *độ tương đồng Jaccard của đa tập* là
$$
\frac{\sum_u\min\bigl(\mu_{B_1}(u),\mu_{B_2}(u)\bigr)}{\sum_u\bigl(\mu_{B_1}(u)+\mu_{B_2}(u)\bigr)}.
$$
:::

Điều kiện về tổng loại trường hợp cả hai đa tập rỗng. Vì $\min(p,q)\le(p+q)/2$ với mọi $p,q\ge0$, giá trị không vượt $1/2$, và bằng $1/2$ khi $B_1=B_2$. MMDS nêu thêm một quy ước khác lấy bội lớn hơn cho phép hợp, khi muốn một đa tập so với chính nó cho 1 (tr.77, chú thích 2); hai quy ước cho hai mẫu số khác nhau.

::: example Ví dụ 05.14 (Hai đa tập; MMDS Ví dụ 3.2, tr.77)
**Dữ kiện.** $B_1=\{\mathrm a,\mathrm a,\mathrm a,\mathrm b\}$, $B_2=\{\mathrm a,\mathrm a,\mathrm b,\mathrm b,\mathrm c\}$.

**Giao.** $\min(3,2)+\min(1,2)+\min(0,1)=2+1+0=3$.

**Hợp.** $4+5=9$ phần tử tính cả bội.

**Kết quả.** $3/9=1/3$.

**Kiểm tra lại.** $B_1$ so với chính nó cho $4/8=1/2$, giá trị lớn nhất của Định nghĩa 05.24.
:::

Biến thể thứ hai giữ tập hợp nhưng đổi phần tử. *Từ dừng* (stop word) là những từ xuất hiện rất thường xuyên, như "and", "you", "to" (MMDS, §3.2.4, tr.80).

::: definition Định nghĩa 05.25 (Shingle theo từ dừng; MMDS §3.2.4, tr.80)
Cho một danh sách từ dừng cố định và một quy tắc tách tài liệu thành dãy từ. Một *shingle theo từ dừng* là cụm ba từ liên tiếp gồm một từ dừng và hai từ ngay sau nó, dù hai từ này có là từ dừng hay không. Tập shingle theo từ dừng của tài liệu gồm mọi cụm như vậy.
:::

Phần tử bây giờ là một cụm ba từ chọn theo vị trí từ dừng, không còn là mọi đoạn $k$ ký tự. MMDS dùng biến thể này cho bài toán bản tin đăng lại: văn xuôi của bài báo có nhiều từ dừng hơn các phần bao quanh như quảng cáo, nên bài báo đóng góp nhiều shingle hơn vào tập của trang (§3.2.4, tr.80).

::: example Ví dụ 05.15 (Câu Sudzo; MMDS Ví dụ 3.5, tr.80)
**Dữ kiện.** Câu "A spokesperson for the Sudzo Corporation revealed today that studies have shown it is good for people to buy Sudzo products." với chín từ dừng mà MMDS in nghiêng: A, for, the, that, have, it, is, for, to. Quảng cáo "Buy Sudzo." không chứa từ dừng nào trong danh sách.

**Các shingle.**

| Vị trí bắt đầu | Shingle ba từ |
|---|---|
| A | `A spokesperson for` |
| for, lần đầu | `for the Sudzo` |
| the | `the Sudzo Corporation` |
| that | `that studies have` |
| have | `have shown it` |
| it | `it is good` |
| is | `is good for` |
| for, lần sau | `for people to` |
| to | `to buy Sudzo` |

**Kiểm tra lại.** Chín vị trí bắt đầu cho chín shingle, vì mỗi từ dừng đều có đủ hai từ đứng sau; hai lần `for` là hai vị trí khác nhau. Quảng cáo không tạo shingle nào.
:::

Danh sách từ dừng và quy tắc tách từ là một phần của biểu diễn, như quy ước khoảng trắng ở Nhận xét 05.5: hai tài liệu chỉ so được khi dùng cùng danh sách và cùng quy tắc.

::: exercise Bài tập 05.13 (Ba cách đo hai đa tập nhỏ)
Cho hai đa tập $B_1=\{\mathrm a,\mathrm a,\mathrm b\}$ và $B_2=\{\mathrm a,\mathrm b,\mathrm b\}$. Tính độ tương đồng của chúng theo Định nghĩa 05.24, theo quy ước lấy bội lớn hơn cho phép hợp, và theo Jaccard của hai tập phần tử phân biệt (Định nghĩa 01.9).
:::

::: hint
Lập bảng bội của a và b trong hai đa tập.
:::

::: solution
Bội của a là $(2,1)$, của b là $(1,2)$. Tử số chung của hai quy ước đa tập là $\min(2,1)+\min(1,2)=2$.

- Định nghĩa 05.24: mẫu số $3+3=6$, độ tương đồng $2/6=1/3$.
- Lấy bội lớn hơn: mẫu số $\max(2,1)+\max(1,2)=4$, độ tương đồng $2/4=1/2$.
- Tập phần tử phân biệt: hai tập đều là $\{\mathrm a,\mathrm b\}$, Jaccard bằng 1.

Ba giá trị khác nhau trên cùng hai đa tập, nên quy ước đếm bội phải được nêu trước khi so.

**Kiểm tra lại.** Theo Định nghĩa 05.24, giá trị không vượt $1/2$; $1/3\le1/2$.
:::

<!-- note-topic-id: lec-05-topic-13 -->
### Rút ngắn phép quét và chia nhóm hàng

Thuật toán 05.18 đọc cả $R$ hàng cho mỗi lần lập chữ ký. MMDS xét cách chỉ đọc một phần các hàng cho mỗi thành phần (§§3.3.6–3.3.7, tr.86–90). Cách này cần một quy tắc cho những phép thử không gặp phần tử nào của tập.

Cách thứ nhất chọn đều một hoán vị của $U$, nhưng chỉ xét $m$ hàng đầu theo hoán vị ấy, với $m$ nguyên và $1\le m<R$; công việc giảm khoảng $R/m$ lần (§3.3.6, tr.86–87). Nếu một cột không có ô 1 nào trong $m$ hàng đầu, giá trị của nó ở phép thử này được ghi là $+\infty$.

::: remark Nhận xét 05.26 (Phép thử trên $m$ hàng đầu; MMDS §3.3.6, tr.87)
Khi so hai cột ở một phép thử chỉ xét $m$ hàng đầu, có ba trường hợp:

| Kết quả của phép thử | Cách xử lý |
|---|---|
| Cả hai giá trị hữu hạn | So bằng như thường lệ |
| Một hữu hạn, một $+\infty$ | Ghi nhận không trùng |
| Cả hai đều $+\infty$ | Không tính vào số trùng, cũng không tính vào mẫu số |

- Ở trường hợp thứ hai, cột có $+\infty$ có phần tử đứng đầu nằm sau $m$ hàng đầu, còn cột kia có phần tử đứng đầu trong $m$ hàng đầu, nên hai phần tử đứng đầu chắc chắn khác nhau.
- Ở trường hợp thứ ba, đoạn đã xét không gặp phần tử nào của hai tập, nên phép thử không mang thông tin về Jaccard. Đếm nó là trùng sẽ đồng nhất việc không quan sát được phần tử với việc chọn được cùng phần tử.
- Tỷ lệ trùng được tính trên các phép thử có thông tin; nếu không có phép thử nào như vậy, tỷ lệ không xác định. Số phép thử có thông tin là một biến ngẫu nhiên và có thể khác nhau giữa các cặp, nên công thức $s(1-s)/n$ của Mệnh đề 05.14 không áp dụng trực tiếp.
:::

Cách thứ hai giữ các hàng cố định, chia chúng thành các nhóm $m$ hàng và lấy một giá trị MinHash từ mỗi nhóm, nên một hàm băm và một lượt quét cho nhiều thành phần (§3.3.7, tr.87–89). Gọi $P$ là tập mã hàng của một nhóm. Trong nhóm, hai tập trở thành $S\cap P$ và $T\cap P$; nếu ít nhất một trong hai khác rỗng và hoán vị trong nhóm chọn đều, xác suất trùng là Jaccard của hai tập hạn chế
$$
\frac{|S\cap T\cap P|}{|(S\cup T)\cap P|},
$$
và khi $P$ là một tập con ngẫu nhiên của vũ trụ, kỳ vọng của tỷ số này bằng $\mathrm{SIM}(S,T)$ (MMDS, tr.88). Với một cách chia cố định, trung bình các tỷ số theo nhóm có thể khác $\mathrm{SIM}(S,T)$, như ví dụ sau.

::: example Ví dụ 05.16 (Hai nhóm bốn hàng; MMDS Ví dụ 3.9, Hình 3.5, tr.89–90)
**Dữ kiện.** Tám hàng, mã $0,\ldots,7$, chia thành hai nhóm $P_1=\{0,1,2,3\}$ và $P_2=\{4,5,6,7\}$; ba tập:

| Hàng | $S_1$ | $S_2$ | $S_3$ | Nhóm |
|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | $P_1$ |
| 1 | 0 | 0 | 0 | $P_1$ |
| 2 | 0 | 0 | 1 | $P_1$ |
| 3 | 0 | 1 | 1 | $P_1$ |
| 4 | 1 | 1 | 1 | $P_2$ |
| 5 | 1 | 1 | 0 | $P_2$ |
| 6 | 1 | 0 | 0 | $P_2$ |
| 7 | 0 | 0 | 0 | $P_2$ |

**Ba cặp.**

| Cặp | Jaccard toàn cục | Trong $P_1$ | Trong $P_2$ | Trung bình hai nhóm |
|---|---|---|---|---|
| $S_1$, $S_2$ | $2/4=1/2$ | $0/1=0$ | $2/3$ | $1/3$ |
| $S_1$, $S_3$ | $1/5$ | $0/2=0$ | $1/3$ | $1/6$ |
| $S_2$, $S_3$ | $2/4=1/2$ | $1/2$ | $1/2$ | $1/2$ |

Trong $P_1$, $S_1\cap P_1=\varnothing$, nên MinHash của $S_1$ trong nhóm này là $+\infty$ và không bao giờ trùng MinHash của $S_2$.

**Kiểm tra lại.** Với $S_1$, $S_2$: $\tfrac12\bigl(0+\tfrac23\bigr)=\tfrac13\ne\tfrac12$; với $S_1$, $S_3$: $\tfrac12\bigl(0+\tfrac13\bigr)=\tfrac16\ne\tfrac15$; với $S_2$, $S_3$: hai nhóm cùng tỷ số $1/2$, nên trung bình bằng giá trị toàn cục.
:::

Trung bình không trọng số của các tỷ số cục bộ khác tỷ số toàn cục, vì các nhóm có hợp với kích thước khác nhau: ở cặp $S_1$, $S_2$, nhóm $P_1$ có hợp một phần tử nhưng góp một nửa trọng số. Khi mỗi giá trị MinHash dựa trên nhiều hơn bốn hàng rất nhiều, sai số kỳ vọng tiến về 0 (MMDS, tr.89).

::: exercise Bài tập 05.14 (Hai cách chia khác của tám hàng)
Dùng ba tập của Ví dụ 05.16 trên tám hàng $0,\ldots,7$: $S_1=\{4,5,6\}$, $S_2=\{3,4,5\}$, $S_3=\{2,3,4\}$.

- (a) Chia thành hàng chẵn $\{0,2,4,6\}$ và hàng lẻ $\{1,3,5,7\}$. Tính trung bình hai Jaccard hạn chế cho cặp $S_1$, $S_2$ và cặp $S_1$, $S_3$, rồi so với Jaccard toàn cục.
- (b) Với cặp $S_1$, $S_2$ và cách chia $\{0,1,2,7\}$, $\{3,4,5,6\}$, xác định trường hợp của Nhận xét 05.26 mà các phép thử trong nhóm thứ nhất thuộc vào, và tỷ lệ trùng kỳ vọng khi chỉ tính các phép thử có thông tin.
:::

::: hint
Với mỗi nhóm $P$, lập $S\cap P$ và $T\cap P$ trước khi chia giao cho hợp.
:::

::: solution
**Câu (a).** Cặp $S_1$, $S_2$: hàng chẵn cho $\{4,6\}$ và $\{4\}$, Jaccard $1/2$; hàng lẻ cho $\{5\}$ và $\{3,5\}$, Jaccard $1/2$; trung bình $1/2$, bằng $\mathrm{SIM}(S_1,S_2)=1/2$. Cặp $S_1$, $S_3$: hàng chẵn cho $\{4,6\}$ và $\{2,4\}$, Jaccard $1/3$; hàng lẻ cho $\{5\}$ và $\{3\}$, Jaccard 0; trung bình $1/6\ne1/5=\mathrm{SIM}(S_1,S_3)$. Cách chia chẵn–lẻ sửa được sai lệch của cặp thứ nhất so với Ví dụ 05.16, nhưng không sửa được cặp thứ hai.

**Câu (b).** Nhóm $\{0,1,2,7\}$ không chứa phần tử nào của $S_1\cup S_2=\{3,4,5,6\}$, nên mọi phép thử trong nhóm này cho hai giá trị $+\infty$, thuộc trường hợp thứ ba, và bị loại khỏi cả tử số lẫn mẫu số. Chỉ nhóm $\{3,4,5,6\}$ còn lại, với Jaccard hạn chế $2/4=1/2$, nên tỷ lệ trùng kỳ vọng là $1/2$.

**Kiểm tra lại.** Câu (b): nếu đếm hai giá trị $+\infty$ là trùng, trung bình hai nhóm thành $\tfrac12(1+\tfrac12)=\tfrac34\ne\tfrac12$.
:::

<!-- note-topic-id: lec-05-topic-14 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 05.1 (Một triệu tài liệu, chữ ký 250 thành phần)
**Bài toán và dữ liệu.** Kho có $C=10^6$ tài liệu, mỗi tài liệu khoảng $50\,000$ byte, mỗi ký tự một byte (MMDS, tr.73, tr.81; Ví dụ 3.10, tr.92). Cần ước lượng Jaccard của mọi cặp với dữ liệu nằm trong bộ nhớ chính.

**Mô hình hóa.** Mỗi tài liệu được chuẩn hóa khoảng trắng theo Nhận xét 05.5 rồi lập tập 9-shingle (Định nghĩa 05.2, Thuật toán 05.3); mỗi shingle được mã hóa 4 byte bằng một hàm $g$ chung (Mục 2.4). Các tập mã lập thành ma trận đặc trưng (Định nghĩa 05.7) với $R\le2^{32}$ hàng, mỗi hàng là một mã xuất hiện trong kho; ma trận chữ ký dài $n=250$ được tính bằng Thuật toán 05.18 (Định nghĩa 05.17).

**Kiểm giả thiết.**

- Mệnh đề 05.6 cần $g$ đơn ánh trên $S\cup T$ của mỗi cặp; với tới $2\cdot49\,992=99\,984$ shingle trong $S\cup T$ và $2^{32}$ mã, giả thiết này không được bảo đảm, và khi có va chạm, Jaccard được bảo toàn là Jaccard của tập mã.
- Định lý 05.10 và Mệnh đề 05.12 cần mỗi hoán vị chọn đều trên mọi hoán vị; Mệnh đề 05.14 cần thêm các hoán vị độc lập. Họ hàm băm hàng dùng trong cài đặt không đáp ứng giả thiết thứ nhất (Nhận xét 05.23), nên các con số dưới đây là của mô hình.
- Biểu diễn theo hàng của ma trận đặc trưng được giả sử đã có; chi phí chuyển dữ liệu từ dạng theo tài liệu sang dạng theo hàng không được tính.
- Giả sử mọi tài liệu dài ít nhất $k=9$ ký tự, nên mọi tập không rỗng.

**Áp dụng và chi phí.**

- Tập mã: theo Mệnh đề 05.4(b), mỗi tài liệu có không quá $49\,992$ mã, tức $199\,968$ byte; cả kho tới khoảng $2\cdot10^{11}$ byte.
- Chữ ký: $n=250$ thành phần, mỗi thành phần 4 byte, nên 1 000 byte mỗi tài liệu và $10^9$ byte cho cả kho (Mệnh đề 05.21(c)).
- Độ chính xác: theo Hệ quả 05.15, độ lệch chuẩn của $\widehat s$ không vượt $1/(2\sqrt{250})\approx0{,}032$ với mọi cặp.
- Lập chữ ký: theo Mệnh đề 05.21(b), một lượt quét với $\Theta(nC+nR+nL)$ thao tác, trong đó $nC=2{,}5\cdot10^8$, $nR\le250\cdot2^{32}\approx1{,}07\cdot10^{12}$ và, với $L\le10^6\cdot49\,992\approx5\cdot10^{10}$, $nL\le1{,}25\cdot10^{13}$ phép min.
- So một cặp: 250 phép so bằng (Mệnh đề 05.13(a)).

**Diễn giải.** Chữ ký giảm dữ liệu của mỗi tài liệu khoảng 200 lần và đưa cả kho vào $10^9$ byte bộ nhớ, với độ lệch chuẩn của mỗi ước lượng không vượt $0{,}032$ trong mô hình.

**Giới hạn.** Số cặp vẫn là $499\,999\,500\,000$; với 1 micro giây mỗi cặp, so mọi cặp mất khoảng $5{,}79$ ngày (Ví dụ 05.1).

**Dẫn ngược lý thuyết.** Định nghĩa 05.2, 05.7, 05.11, 05.17; Thuật toán 05.3, 05.18; Mệnh đề 05.4, 05.6, 05.12, 05.13, 05.14, 05.21; Định lý 05.10; Hệ quả 05.15; Nhận xét 05.5, 05.23.
:::

::: application Tình huống 05.2 (Tài liệu ngắn hơn độ dài shingle)
**Bài toán và dữ liệu.** Trong kho của Tình huống 05.1, với $k=9$, có những tài liệu chỉ gồm một dòng ngắn. Giả sử hai tài liệu là `Mua ngay` (8 ký tự) và `Gia soc` (7 ký tự), không chung từ nào.

**Mô hình hóa.** Định nghĩa 05.2 với $\ell\le8<k=9$ cho $S_9(D)=\varnothing$ ở cả hai tài liệu; hai cột tương ứng của ma trận đặc trưng toàn 0.

**Kiểm giả thiết.** Định lý 05.10 cần $S\ne\varnothing$ và $T\ne\varnothing$; giả thiết này bị vi phạm. $\mathrm{SIM}(\varnothing,\varnothing)$ là $0/0$, không xác định.

**Áp dụng.** Thuật toán 05.18 vẫn trả hai cột toàn $+\infty$ theo đặc tả (Định nghĩa 05.17, Mệnh đề 05.19). Hai cột trùng ở mọi tọa độ, nên phép tính tỷ lệ cho $\widehat s=1$: hai dòng quảng cáo khác hẳn nhau bị báo là trùng hoàn toàn.

**Chi phí.** Phát hiện các tài liệu có $\ell<k$ tốn một phép so độ dài cho mỗi tài liệu, tức $C$ phép so; tương đương, đếm số ô 1 của mỗi cột trong lượt quét.

**Diễn giải.** Mọi cặp hai tài liệu ngắn hơn $k$ ký tự đều nhận $\widehat s=1$, giá trị lớn nhất có thể, bất kể nội dung.

**Giới hạn.** Giá trị gán cho cặp hai tập rỗng là một quy ước của ứng dụng.

**Dẫn ngược lý thuyết.** Định nghĩa 05.2, 05.17; Định lý 05.10 (giả thiết không rỗng); Mệnh đề 05.19; Thuật toán 05.18.
:::

::: application Tình huống 05.3 (Một bộ hàm băm cố định trên bốn tập đặc trưng)
**Bài toán và dữ liệu.** Trước khi dùng cho cả kho, một nhóm kiểm hai hàm băm hàng $f_1(r)=(r+1)\bmod5$, $f_2(r)=(3r+1)\bmod5$ trên bốn tập $S_1=\{\mathrm a,\mathrm d\}$, $S_2=\{\mathrm c\}$, $S_3=\{\mathrm b,\mathrm d,\mathrm e\}$, $S_4=\{\mathrm a,\mathrm c,\mathrm d\}$, mã hàng $0,\ldots,4$ (MMDS Ví dụ 3.8).

**Mô hình hóa.** Ma trận chữ ký $n=2$ của Thuật toán 05.18 là $\mathrm{SIG}=\begin{pmatrix}1&3&0&1\\0&2&0&0\end{pmatrix}$ (Ví dụ 05.12).

**Kiểm giả thiết.** Theo Mệnh đề 05.22, hai hàm là song ánh vì $\gcd(1,5)=\gcd(3,5)=1$, nên mỗi tọa độ là MinHash theo một hoán vị (Mục 5.1). Hai hàm là một lựa chọn cố định, không được chọn ngẫu nhiên đều và độc lập, nên Mệnh đề 05.12 và 05.14 không áp dụng cho bộ hàm này.

**Áp dụng.**

| Cặp | $\widehat s$ | $\mathrm{SIM}$ | $\widehat s-\mathrm{SIM}$ |
|---|---|---|---|
| $S_1$, $S_2$ | 0 | 0 | 0 |
| $S_1$, $S_3$ | $1/2$ | $1/4$ | $1/4$ |
| $S_1$, $S_4$ | 1 | $2/3$ | $1/3$ |
| $S_2$, $S_3$ | 0 | 0 | 0 |
| $S_2$, $S_4$ | 0 | $1/3$ | $-1/3$ |
| $S_3$, $S_4$ | $1/2$ | $1/5$ | $3/10$ |

**Chi phí.** 36 thao tác với biểu diễn theo hàng (Ví dụ 05.13), cộng 2 phép so cho mỗi cặp.

**Diễn giải.** Hai cặp rời có $\widehat s=0$, đúng; bốn cặp còn lại lệch tới $1/3$ về cả hai phía. Với một bộ hàm cố định, Mệnh đề 05.12 và 05.14 không cho bảo đảm nào.

**Giới hạn.** Một bảng sáu cặp không kiểm được phân phối của một họ hàm (Nhận xét 05.23); muốn ước lượng đáng tin, cần $n$ lớn và các hàm chọn ngẫu nhiên từ một họ.

**Dẫn ngược lý thuyết.** Định nghĩa 05.11, 05.17; Thuật toán 05.18; Mệnh đề 05.12, 05.14, 05.22; Nhận xét 05.23.
:::

Các khái niệm của chương được dùng lại ở các bài sau của học phần.

- **Bài 06 (tìm cặp tương đồng bằng LSH).** Bài 06 chia ma trận chữ ký thành dải và chỉ xác minh các cặp cùng thùng; xác suất một cặp thành ứng viên được tính từ Định lý 05.10 cho từng hàng của dải, và cột toàn $+\infty$ của Tình huống 05.2 là một trường hợp biên của nó.
- **Bài 08 và Bài 09 (dòng dữ liệu).** Các phác thảo trên dòng dùng hàm băm cố định theo nghĩa của Định nghĩa 05.17, cho cùng giá trị trên cùng đầu vào ở mọi lần gọi; Bài 09 dùng đẳng thức phương sai của trung bình các phép thử độc lập ở Bước 2 trong chứng minh Mệnh đề 05.14.
- **Bài 08 đến Bài 10.** Các chứng minh tính đúng dùng dạng bất biến khởi tạo, duy trì, kết thúc của Mệnh đề 05.19.

<!-- note-topic-id: lec-05-topic-15 -->
## Tóm tắt chương

Câu hỏi xuất phát của chương là ước lượng Jaccard của mọi cặp trong kho $10^6$ tài liệu với dữ liệu trong bộ nhớ chính, khi tập mã của mỗi tài liệu chiếm khoảng $200\,000$ byte và một cặp tập mã tốn tới $100\,000$ phép so sánh (Ví dụ 05.1). Chúng ta biến mỗi tài liệu thành tập $k$-shingle bằng một thuật toán thời gian kỳ vọng $O(1+wk)$ và mã hóa mỗi shingle bằng 4 byte, giữ nguyên Jaccard khi mã không va chạm trên cặp đang xét (Định nghĩa 05.2, Thuật toán 05.3, Mệnh đề 05.4, 05.6). Tập mã vẫn gấp khoảng bốn lần tài liệu, nên chúng ta thay cả tập bằng phần tử đứng đầu theo một hoán vị chung và chứng minh hai tập trùng MinHash với xác suất đúng bằng Jaccard khi hoán vị chọn đều (Định nghĩa 05.8, Bổ đề 05.9, Định lý 05.10). Lặp phép thử với $n$ hoán vị cho chữ ký và ước lượng $\widehat s$ không chệch, có phương sai $s(1-s)/n$ khi các hoán vị độc lập, so một cặp bằng $n$ phép so (Định nghĩa 05.11, Mệnh đề 05.12–05.14, Hệ quả 05.15). Thay hoán vị bằng hàm băm trên mã hàng, Thuật toán 05.18 tính cả ma trận chữ ký trong một lượt quét với $\Theta(nC+nR+nL)$ thao tác và đúng với mọi bộ hàm (Mệnh đề 05.19, 05.21). Hàm affine là hoán vị khi và chỉ khi hệ số nguyên tố cùng nhau với $R$, nhưng một họ song ánh vẫn chưa chọn đều trên mọi hoán vị (Mệnh đề 05.22, Nhận xét 05.23). Với $n=250$, cả kho vừa $10^9$ byte và độ lệch chuẩn không vượt $0{,}032$ (Tình huống 05.1), nhưng số cặp vẫn là $499\,999\,500\,000$; Bài 06 giảm thừa số này bằng phân dải chữ ký.

![Quy trình biểu diễn: tài liệu được chuyển thành tập shingle; tập tạo chữ ký MinHash; tỷ lệ các tọa độ tương ứng trùng nhau ước lượng Jaccard của biểu diễn tập. Quy trình không chọn cặp ứng viên.](img/lec-05/quy-trinh-bieu-dien.svg)

Hình tóm tắt ba bước biến đổi của chương, từ tài liệu tới tập, từ tập tới chữ ký, và từ hai chữ ký tới tỷ lệ tọa độ trùng; bước chọn cặp ứng viên nằm ngoài quy trình này.

**Định nghĩa và kết quả theo mục.**

- Mục 1: kho một triệu tài liệu (Ví dụ 05.1); phần tử của tập và ngưỡng theo ứng dụng (Nhận xét 05.1).
- Mục 2: cửa sổ và tập $k$-shingle (Định nghĩa 05.2); thuật toán tạo tập shingle, tính đúng và chi phí (Thuật toán 05.3, Mệnh đề 05.4); chọn $k$ và quy ước khoảng trắng (Nhận xét 05.5); mã không va chạm bảo toàn Jaccard (Mệnh đề 05.6).
- Mục 3: ma trận đặc trưng và biểu diễn theo hàng (Định nghĩa 05.7); hạng và MinHash (Định nghĩa 05.8); phần tử đứng đầu phân phối đều (Bổ đề 05.9); xác suất trùng MinHash (Định lý 05.10).
- Mục 4: chữ ký, ma trận chữ ký và ước lượng (Định nghĩa 05.11); ước lượng không chệch (Mệnh đề 05.12); chi phí so sánh (Mệnh đề 05.13); phương sai (Mệnh đề 05.14); cận độ lệch chuẩn (Hệ quả 05.15); hai cách đọc sai (Nhận xét 05.16).
- Mục 5: bài toán tính ma trận chữ ký (Định nghĩa 05.17); quét hàng (Thuật toán 05.18); tính đúng và thứ tự quét (Mệnh đề 05.19, Hệ quả 05.20); chi phí thời gian và bộ nhớ (Mệnh đề 05.21); hàm affine là hoán vị (Mệnh đề 05.22); song ánh, phân phối đều và hai tầng va chạm (Nhận xét 05.23).
- Đọc thêm: Jaccard của đa tập (Định nghĩa 05.24); shingle theo từ dừng (Định nghĩa 05.25); phép thử trên $m$ hàng đầu (Nhận xét 05.26).

**Công thức và thuật toán cần nhớ.**

$$
\binom C2=\frac{C(C-1)}2,\qquad S_k(D)=\{D[j:j+k]:0\le j\le\ell-k\},\qquad |S_k(D)|\le\max(0,\ell-k+1).
$$

$$
h_\pi(S)=\arg\min_{u\in S}\operatorname{rank}_\pi(u),\qquad \Pr\bigl[h_\pi(S)=h_\pi(T)\bigr]=\mathrm{SIM}(S,T).
$$

$$
\widehat s=\frac1n\sum_{i=1}^n\mathbf 1\bigl[h_{\pi_i}(S)=h_{\pi_i}(T)\bigr],\qquad \mathbb E[\widehat s]=s,\qquad \operatorname{Var}(\widehat s)=\frac{s(1-s)}n\le\frac1{4n}.
$$

$$
\mathrm{SIG}(i,c)=\min\bigl(\{f_i(r):M(r,c)=1\}\cup\{+\infty\}\bigr),\qquad \Theta(nC+nR+nL).
$$

Thuật toán quét hàng khởi tạo mọi ô bằng $+\infty$, rồi với mỗi hàng tính $n$ giá trị băm một lần và lấy min vào mọi cột có 1 ở hàng đó. Hàm $(\alpha r+\beta)\bmod R$ là hoán vị khi và chỉ khi $\gcd(\alpha,R)=1$.

**Giả thiết hay bị bỏ quên.**

- Jaccard cần $S\cup T\ne\varnothing$; MinHash cần tập không rỗng; cột toàn $+\infty$ là quy ước đầu ra, không là Jaccard.
- Hai tài liệu chỉ so được khi dùng cùng $k$, cùng quy ước khoảng trắng và cùng hàm mã $g$.
- Định lý 05.10 cần cùng một hoán vị cho hai tập, chọn đều trên mọi hoán vị.
- Không chệch chỉ cần mỗi hoán vị chọn đều; công thức phương sai cần thêm độc lập.
- So hai chữ ký theo cùng tọa độ, không lấy Jaccard của hai tập giá trị.
- Tính đúng của phép quét không thay cho giả thiết xác suất; song ánh không kéo theo phân phối đều trên mọi hoán vị.
- Chữ ký giảm chi phí một cặp, không giảm số cặp.

<!-- note-topic-id: lec-05-topic-16 -->
## Bài tập củng cố

Bài tập 05.15–05.28 nằm trong [tệp bài tập Bài 05](material-viewer.html?doc=materials/lec-05/exercises.md&deck=lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html), cùng gợi ý và lời giải.

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, Chương 3. Mở chương, tr.73, và §3.1.1–3.1.3, tr.74–77: Mục 1, Nhận xét 05.1, Ví dụ 05.14; §3.2.1–3.2.3, tr.78–80, Ví dụ 3.3, 3.4: Mục 2; §3.2.4, tr.80, Ví dụ 3.5: Định nghĩa 05.25, Ví dụ 05.15; mở §3.3, tr.81, và §3.3.1–3.3.3, tr.81–83, Ví dụ 3.6, 3.7, Hình 3.2, 3.3: Mục 3; §3.3.4, tr.83–84: Mục 4; §3.3.5, tr.84–86, Ví dụ 3.8, Hình 3.4: Mục 5, Tình huống 05.3; §3.3.6–3.3.7, tr.86–90, Ví dụ 3.9, Hình 3.5: phần đọc thêm, Nhận xét 05.26, Ví dụ 05.16; Ví dụ 3.10, tr.92: Ví dụ 05.1, Tình huống 05.1. Bài 3.1.1–3.1.3, 3.2.1–3.2.3, 3.3.1–3.3.9: tệp bài tập. Sách và trang chiếu của các tác giả: [http://www.mmds.org](http://www.mmds.org); phần lớn sườn, ví dụ và bài tập của chương dựa trên nguồn này.
- Leskovec, J., Rajaraman, A. và Ullman, J. D. Trang chiếu Chương 3 *Finding Similar Items: Locality Sensitive Hashing* của sách MMDS, bản trên http://www.mmds.org (không ghi năm). Tr.18–22: Mục 2; tr.25–35: Mục 3; tr.36–39: Mục 4, Mục 5.
- Leskovec, J. (2026). Stanford CS246, *Mining Massive Datasets*, bài LSH I (03-lsh). Trang chiếu 17–22: Mục 2, Mục 3.1; 23–31: Mục 3.2–3.3, Mục 4; 32–33: Mục 5, Nhận xét 05.23.
- Ghi chú Bài 01: Định nghĩa 01.4, 01.8, 01.9, 01.10, 01.13; Thuật toán 01.11; Bổ đề 01.14; Mệnh đề 01.12, 01.15; Ví dụ 01.6, 01.8.
