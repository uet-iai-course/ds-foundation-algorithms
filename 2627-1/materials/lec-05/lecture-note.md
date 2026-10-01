# Bài 05 — Biểu diễn tương đồng: Shingling và MinHash

Giải thuật nền tảng của Khoa học dữ liệu · Học kỳ 1, năm học 2026–2027.

[Bộ trang chiếu của Bài 05](lecture-05-bieu-dien-tuong-dong-shingling-va-minhash.html) trình bày tuyến chính. Tài liệu này giải thích các định nghĩa, ví dụ, chứng minh và thuật toán để có thể đọc độc lập. Nguồn chính là *Mining of Massive Datasets* (MMDS), ấn bản thứ ba, Chương 3, các mục 3.1–3.3; số trang dưới đây là số trang in trong sách.

Sau bài học, người học có thể chuyển văn bản thành tập shingle, tính độ tương đồng Jaccard, chứng minh quan hệ xác suất của MinHash, dùng chữ ký để ước lượng Jaccard và phân tích thuật toán tính chữ ký. Kiến thức đầu vào gồm chuỗi, tập hợp, hàm băm, vector, xác suất, kỳ vọng và phương sai cơ bản.

## 1. Tài liệu gần trùng và hai giới hạn tính toán

Một trang phản chiếu có thể giữ phần lớn nội dung của trang gốc nhưng thay thông tin máy chủ. Một bản tin có thể được đăng lại ở nhiều nơi, với một số đoạn bị lược hoặc thêm vào. Một bài đạo văn có thể đổi vài từ hoặc đổi thứ tự câu nhưng vẫn giữ phần lớn văn bản gốc. Kiểm tra hai chuỗi bằng nhau chỉ nhận ra trường hợp trùng hoàn toàn; bài toán gần trùng cần định lượng phần văn bản chung giữa những tài liệu còn có khác biệt. Các tình huống này xuất hiện ở phần mở đầu Chương 3 và §3.1.2, tr. 73–76.

Đầu vào là một kho gồm $C$ tài liệu. Đối với một cặp đã chọn, đầu ra cần có là một số đo tương đồng trên biểu diễn văn bản. Số đo trong bài dựa trên các đoạn con chung ở mức ký tự; tương đồng về ý nghĩa cần những kỹ thuật khác. Cách biểu diễn và quy tắc xử lý văn bản phải được xác định trước khi tính số đo.

![Hai tài liệu có các vùng văn bản chung và riêng; diện tích vùng không biểu diễn dung lượng.](img/lec-05/tai-lieu-gan-trung.svg)

Hai giới hạn cần phân biệt là kích thước biểu diễn của mỗi tài liệu và số cặp trong kho. Nếu so sánh mọi cặp không thứ tự của $C$ tài liệu phân biệt thì có

$$
\binom C2=\frac{C(C-1)}2
$$

cặp. Mỗi tài liệu ghép với $C-1$ tài liệu khác, nhưng cách đếm có thứ tự đếm mỗi cặp hai lần. Với một triệu tài liệu như quy mô nêu ở đầu chương, số cặp chính xác là $499\,999\,500\,000$.

![Tổng công việc gồm số cặp nhân với chi phí so sánh một cặp.](img/lec-05/quy-mo-so-sanh-cap.svg)

Bài 05 xây một biểu diễn ngắn để giảm dung lượng và chi phí so sánh **một cặp**. Việc thay biểu diễn không tự làm giảm số cặp. Bài 06 tiếp tục từ chữ ký để tạo các cặp ứng viên bằng băm nhạy cảm cục bộ (LSH).

::: exercise Tự kiểm tra
Một phương pháp thay mỗi tài liệu bằng một vector có $n$ thành phần và so sánh hai vector trong $\Theta(n)$ thời gian. Nếu vẫn xét mọi cặp, xác định biểu thức số phép so sánh thành phần theo $C,n$.
:::

::: solution Lời giải
Mỗi cặp dùng $n$ phép so bằng. Với $C(C-1)/2$ cặp, tổng là $nC(C-1)/2$. Giảm $n$ giảm chi phí một cặp, còn thừa số bậc hai theo $C$ vẫn hiện diện.
:::

## 2. Độ tương đồng Jaccard của hai tập hợp

Biểu diễn tài liệu bằng tập hợp cho phép tách hai đại lượng: số phần tử chung và số phần tử xuất hiện ở ít nhất một tập. Tỷ số của hai đại lượng này là Jaccard.

Với hai tập hữu hạn $S,T$ và $S\cup T\ne\varnothing$, định nghĩa

$$
\mathrm{SIM}(S,T)=\frac{|S\cap T|}{|S\cup T|}.
$$

Ký hiệu $|A|$ chỉ số phần tử của tập $A$. Phép hợp chỉ đếm mỗi phần tử một lần, kể cả khi phần tử ấy thuộc cả hai tập. Do $S\cap T\subseteq S\cup T$, luôn có $0\le\mathrm{SIM}(S,T)\le1$. Hai tập rời có hợp khác rỗng cho giá trị $0$; hai tập bằng nhau và khác rỗng cho giá trị $1$. Khi $S=T=\varnothing$, tỷ số trở thành $0/0$ và định nghĩa trên không áp dụng.

::: example Ba vùng của hai tập
Hình 3.1 của sách, tr. 75, có hai phần tử chỉ thuộc $S$, ba phần tử thuộc cả $S,T$ và ba phần tử chỉ thuộc $T$. Do đó

$$
|S\cap T|=3,\qquad |S\cup T|=2+3+3=8,
\qquad \mathrm{SIM}(S,T)=\frac38.
$$
:::

![Hình vẽ lại theo Hình 3.1: hai phần tử riêng của S, ba phần tử giao và ba phần tử riêng của T.](img/lec-05/jaccard-ba-vung.svg)

Tổng $|S|+|T|=5+6=11$ lớn hơn $|S\cup T|$ vì ba phần tử giao bị đếm hai lần. Hình biểu diễn quan hệ thuộc tập; diện tích hai miền tròn không mã hóa số lượng phần tử. Mẫu số dùng toàn bộ hợp để đặt lượng chung trong quy mô của cặp. Chỉ dùng kích thước giao sẽ không phân biệt một lượng chung trong hai tập nhỏ với cùng lượng chung trong hai tập rất lớn.

Tập hợp phải gắn với một cách chọn phần tử cụ thể. Trong ví dụ khách hàng của §3.1.3, tr. 76, phần tử có thể là mặt hàng đã mua. Ngưỡng có ý nghĩa cũng khác nhau giữa các ứng dụng: sách dự đoán hai trang phản chiếu có Jaccard trên 90%, còn với hai khách hàng, Jaccard 20% đã có thể đủ để xem hai người có sở thích tương tự. Với văn bản, phần tử sẽ là những đoạn con liên tiếp có độ dài cố định. Khi các phần tử được chọn khác đi, đại lượng Jaccard cũng có thể thay đổi.

Tuyến chính dùng tập hợp, vì vậy số lần một phần tử xuất hiện không được lưu. Biến thể đa tập của sách có quy ước khác và được trình bày riêng ở mục 12.

::: exercise Tự kiểm tra
(a) Với hai tập của Hình 3.1, thêm vào $T$ hai phần tử mới, không thuộc $S$. Tính lại Jaccard.

(b) Giải thích vì sao độ dài của hai chuỗi chưa đủ để xác định Jaccard giữa hai văn bản.
:::

::: solution Lời giải
(a) Giao vẫn có 3 phần tử, hợp tăng lên 10, nên Jaccard bằng $3/10$. Giá trị giảm vì mẫu số tăng còn tử số giữ nguyên.

(b) Jaccard cần biết các phần tử của hai tập để xác định giao và hợp. Độ dài chuỗi chỉ cho số ký tự, không xác định tập đặc trưng hoặc phần tử nào chung. Cần chọn quy tắc chuyển mỗi chuỗi thành tập, chẳng hạn quy tắc shingling ở mục tiếp theo.
:::

## 3. Shingling: chuyển chuỗi thành tập

### Định nghĩa và quy ước

Một **$k$-shingle** là một đoạn gồm $k$ ký tự liên tiếp. Cho chuỗi $D$ dài $\ell$ và số nguyên $k\ge1$. Đánh số ký tự từ $0$ đến $\ell-1$. Ký hiệu $D[i:i+k]$ chỉ đoạn gồm các ký tự ở vị trí $i,i+1,\ldots,i+k-1$; vị trí $i+k$ không được lấy. Tập shingle là

$$
S_k(D)=\{D[i:i+k]:0\le i\le\ell-k\}.
$$

Nếu $\ell<k$, không có cửa sổ hợp lệ và $S_k(D)=\varnothing$. Khi $k\le\ell$, số cửa sổ là $\ell-k+1$, còn số shingle phân biệt có thể nhỏ hơn do lặp.

### Ví dụ chạy tay

Ví dụ 3.3, tr. 78, dùng $D=\texttt{abcdabd}$ và $k=2$. Bảy ký tự tạo sáu cửa sổ:

| Vị trí bắt đầu $i$ | Cửa sổ | Tập sau phép chèn |
|---:|---|---|
| 0 | `ab` | {`ab`} |
| 1 | `bc` | {`ab`, `bc`} |
| 2 | `cd` | {`ab`, `bc`, `cd`} |
| 3 | `da` | {`ab`, `bc`, `cd`, `da`} |
| 4 | `ab` | {`ab`, `bc`, `cd`, `da`} |
| 5 | `bd` | {`ab`, `bc`, `cd`, `da`, `bd`} |

Cửa sổ tại vị trí $4$ trùng cửa sổ tại vị trí $0$, nên không tăng kích thước tập. Kết quả có năm phần tử:

$$
S_2(D)=\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da},\texttt{bd}\}.
$$

![Sáu cửa sổ hai ký tự của abcdabd; hai cửa sổ ab chỉ tạo một phần tử.](img/lec-05/cua-so-shingle.svg)

Shingling giữ thứ tự ký tự **bên trong** mỗi đoạn con. Biểu diễn bằng tập không giữ số lần lặp hoặc toàn bộ thứ tự các đoạn trong tài liệu. Những đoạn con nằm hoàn toàn trong phần văn bản được giữ nguyên vẫn xuất hiện ở cả hai phiên bản, tạo phần tử chung để Jaccard đo được, kể cả khi các câu đổi thứ tự (mở đầu §3.2, tr. 78). Một thay đổi cục bộ chỉ ảnh hưởng ít cửa sổ: thay ký tự ở vị trí $i$ chỉ đổi các cửa sổ bắt đầu từ $i-k+1$ đến $i$, tức nhiều nhất $k$ cửa sổ.

### Thuật toán, tính đúng và chi phí

Đầu vào của thuật toán là chuỗi $D$ và số nguyên $k\ge1$; đầu ra là đúng tập $S_k(D)$.

```text
S ← ∅
for i = 0, …, ℓ − k:
    chèn D[i:i+k] vào S
return S
```

Vòng lặp không thực hiện bước nào nếu $\ell<k$. Sau khi đã xét $t$ vị trí đầu tiên, bất biến là

$$
S=\{D[j:j+k]:0\le j<t\}.
$$

Ban đầu $t=0$ và hai vế đều rỗng. Mỗi bước thêm đúng cửa sổ kế tiếp; phép chèn vào tập giữ một bản của mỗi chuỗi. Khi đã xét đủ $w=\max(0,\ell-k+1)$ vị trí, tập thu được đúng định nghĩa.

Mô hình trực tiếp tạo và băm một cửa sổ dài $k$ trong $O(k)$ thời gian. Với cấu trúc tập băm có chi phí chèn kỳ vọng theo độ dài khóa, phần xử lý $w$ cửa sổ tốn $O(wk)$ kỳ vọng; cộng khởi tạo là $O(1+wk)$. Lưu các chuỗi phân biệt tốn $O(k|S_k(D)|)$ ký tự, chưa tính đầu vào và chi tiết quản lý bộ nhớ. Không thể bỏ hệ số $k$ khi $k$ là tham số thay đổi mà chưa có một cách tính cửa sổ khác.

### Chọn độ dài và xử lý khoảng trắng

§3.2.2, tr. 79, nêu tiêu chí: chọn $k$ đủ lớn để xác suất một shingle cho trước xuất hiện trong một tài liệu cho trước là thấp. Ở cực đoan $k=1$, hầu hết trang Web chứa hầu hết ký tự thông dụng, nên gần như mọi cặp trang đều có Jaccard cao. Nếu bảng chữ cái có 27 ký tự thì có $27^5=14\,348\,907$ chuỗi dài 5 khả dĩ, lớn hơn nhiều độ dài một thư điện tử thông thường. Tuy nhiên, văn bản tự nhiên không phân bố đều trên các chuỗi. Khi $k$ quá nhỏ so với độ dài tài liệu, nhiều shingle phổ biến có thể cùng xuất hiện ở các tài liệu khác nhau. Sách dùng $20^k$ như một ước tính thực dụng và gợi ý $k=5$ cho thư điện tử, $k=9$ cho tài liệu dài (§3.2.2, tr. 79). Đây là quy tắc kinh nghiệm theo kiểu dữ liệu, không phải ngưỡng có bảo đảm cho mọi ngôn ngữ.

Khoảng trắng cũng là một phần của quy ước. Ví dụ 3.4, tr. 78, giữ $k=9$:

| Chuỗi | Số ký tự | Các shingle |
|---|---:|---|
| `touch down` | 10 | `touch dow`, `ouch down` |
| `touchdown` | 9 | `touchdown` |

Nếu xóa dấu cách trước khi tạo shingle thì hai chuỗi trở thành giống nhau. §3.2.1 đề nghị thay mỗi dãy ký tự trắng (dấu cách, tab, xuống dòng) bằng một dấu cách; cách này vẫn phân biệt shingle phủ hai từ với shingle nằm trong một từ. Quy tắc đã chọn phải được áp dụng nhất quán trong toàn bộ kho. Các chuỗi gốc trong ví dụ được giữ nguyên vì thay từ sẽ thay phép đếm ký tự.

### Băm shingle và giới hạn dung lượng

§3.2.3, tr. 79–80, mô tả mã hóa một shingle 9 ký tự bằng mã băm 32 bit, tức 4 byte. Số $9$ đo độ dài đoạn gốc, còn số $4$ đo dung lượng mã; $k$ vẫn là $9$. Mỗi mã vừa một từ máy nên các phép so sánh trên phần tử chỉ cần một thao tác.

Sách so sánh cách này với việc dùng trực tiếp 4-shingle, cũng chiếm 4 byte mỗi phần tử. Nếu chỉ khoảng 20 ký tự thường gặp, số 4-shingle có khả năng xuất hiện chỉ cỡ $20^4=160\,000$, nhỏ hơn nhiều so với $2^{32}$ giá trị của 4 byte; các tài liệu không liên quan dễ chung phần tử. Số 9-shingle có khả năng xuất hiện vượt xa $2^{32}$, nên sau khi băm, gần như mọi mã 4 byte đều có thể gặp. Với cùng dung lượng, mã của 9-shingle phân biệt tài liệu tốt hơn.

Hai shingle khác nhau có thể nhận cùng mã. Khi đó tập mã gộp những phần tử vốn phân biệt, nên Jaccard của tập mã có thể khác Jaccard của tập chuỗi.

Trong ví dụ `abcdabd`, số shingle là 5. Tập mã có đúng 5 phần tử **nếu không xảy ra va chạm**; nói chung số mã phân biệt không vượt số shingle phân biệt. Mã ngắn làm giảm dung lượng mỗi phần tử nhưng số phần tử vẫn có thể tăng theo độ dài tài liệu.

Băm shingle nhận một chuỗi con và trả một mã. MinHash ở các mục sau nhận một tập và tạo một thành phần chữ ký. Định lý MinHash áp dụng cho tập thực sự được cung cấp, không tự khôi phục các phần tử đã bị gộp do va chạm ở bước mã hóa.

::: exercise Tự kiểm tra
(a) Với `abcdabd`, $k=2$, nêu số cửa sổ, số shingle phân biệt và điều kiện để có cùng số mã phân biệt.

(b) Chuỗi `abcdabc` chỉ khác `abcdabd` ở ký tự cuối. Với $k=2$, tính Jaccard của hai tập shingle và giải thích vì sao giá trị gần 1.

(c) Giải thích vì sao 4-shingle và mã 4 byte của 9-shingle dùng cùng dung lượng nhưng không phân biệt tài liệu như nhau.

(d) Một tài liệu dài 50.000 ký tự, $k=9$, mỗi mã 4 byte. Giả sử mọi cửa sổ cho mã khác nhau; tính số phần tử và dung lượng tập mã.
:::

::: solution Lời giải
(a) Có 6 cửa sổ và 5 shingle phân biệt. Có 5 mã phân biệt nếu năm shingle nhận năm mã khác nhau.

(b) Tập của `abcdabc` là $\{\texttt{ab},\texttt{bc},\texttt{cd},\texttt{da}\}$. Giao với $S_2(\texttt{abcdabd})$ có 4 phần tử, hợp có 5, nên Jaccard bằng $4/5$. Ký tự cuối chỉ thuộc một cửa sổ, nên thay nó chỉ đổi một cửa sổ.

(c) Với khoảng 20 ký tự thường gặp, chỉ cỡ $20^4=160\,000$ 4-shingle có khả năng xuất hiện, nên tài liệu không liên quan dễ chung phần tử. Mã của 9-shingle phủ gần như mọi giá trị 4 byte.

(d) Có $50\,000-9+1=49\,992$ cửa sổ, nên tập có $49\,992$ mã và chiếm $199\,968$ byte, cỡ bốn lần dung lượng tài liệu. Đây là cận trên; cửa sổ lặp hoặc va chạm làm tập nhỏ hơn.
:::

## 4. Ma trận đặc trưng và biểu diễn theo hàng

Tập shingle có thể lớn dù từng mã đã ngắn. Mỗi cửa sổ tạo nhiều nhất một phần tử, nên $|S_k(D)|\le\max(0,\ell-k+1)$: số phần tử có thể gần bằng số ký tự của tài liệu. Ở tr. 81, sách minh họa một tài liệu dài 50.000 byte có tập mã shingle khoảng 200.000 byte khi mỗi mã dùng 4 byte. Lập luận giả sử phần lớn cửa sổ tạo phần tử khác nhau; con số chưa bao gồm chi phí cấu trúc lưu trữ. Với hàng triệu tài liệu, các tập này có thể không vừa bộ nhớ chính. Cần một chữ ký có số thành phần được chọn trước để biểu diễn cả tập.

Trước hết, một biểu diễn ma trận làm rõ quan hệ phần tử–tập. Cho vũ trụ hữu hạn $U$ có $R$ phần tử và $C$ tập $S_1,\ldots,S_C\subseteq U$. Gán cho mỗi phần tử một mã hàng $r\in\{0,\ldots,R-1\}$. Ma trận đặc trưng $M\in\{0,1\}^{R\times C}$ có

$$
M(r,c)=\begin{cases}
1,&\text{phần tử ở hàng }r\text{ thuộc }S_c,\\
0,&\text{ngược lại.}
\end{cases}
$$

Hàng biểu diễn phần tử, cột biểu diễn tập. Một cột toàn $0$ tương ứng tập rỗng; các định lý MinHash lý tưởng sẽ giả sử tập không rỗng.

::: example Ma trận Hình 3.2
Dữ liệu xuyên suốt lấy từ Hình 3.2, tr. 81. Vũ trụ là $U=\{a,b,c,d,e\}$, với mã hàng $a,b,c,d,e\leftrightarrow0,1,2,3,4$.

| Phần tử / $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| a / 0 | 1 | 0 | 0 | 1 |
| b / 1 | 0 | 0 | 1 | 0 |
| c / 2 | 0 | 1 | 0 | 1 |
| d / 3 | 1 | 0 | 1 | 1 |
| e / 4 | 0 | 0 | 1 | 0 |

Các cột lần lượt là $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$ và $S_4=\{a,c,d\}$. Chẳng hạn, $\mathrm{SIM}(S_1,S_4)=2/3$ vì giao là $\{a,d\}$ và hợp là $\{a,c,d\}$.
:::

Ma trận đặc trưng là cách mô tả dữ liệu; thực tế nó hầu như luôn thưa, nên không lưu ma trận đặc đủ $RC$ ô mà chỉ lưu vị trí các ô $1$. Danh sách cột có $1$ theo từng hàng của ví dụ là:

| Hàng | Danh sách cột |
|---|---|
| a / 0 | 1, 4 |
| b / 1 | 3 |
| c / 2 | 2, 4 |
| d / 3 | 1, 3, 4 |
| e / 4 | 3 |

Đặt $L=\operatorname{nnz}(M)$ là tổng số ô $1$. Tổng độ dài các danh sách bằng $L$; ở đây $L=2+1+2+3+1=9$, còn ma trận có $RC=20$ ô. Biểu diễn theo hàng sẽ cho phép tính các giá trị băm một lần cho phần tử rồi cập nhật đúng những tập chứa nó (xem mục 9). Ví dụ nhỏ không tự chứng minh danh sách dùng ít byte hơn: mỗi chỉ số cột cũng có chi phí lưu trữ.

::: exercise Tự kiểm tra
Xác định các cột có $1$ ở hàng $d$ và giải thích vì sao danh sách của hàng này có ba phần tử.
:::

::: solution Lời giải
Phần tử $d$ thuộc $S_1,S_3,S_4$, nên hàng $d$ có ba ô $1$ ở các cột 1, 3 và 4; cột 2 không chứa $d$. Khi tính chữ ký ở mục 9, chỉ ba cột này nhận ứng viên từ hàng $d$.
:::

## 5. MinHash theo một hoán vị

Chữ ký cần ngắn nhưng vẫn giữ liên hệ với Jaccard. MinHash thay cả tập bằng một phần tử đại diện, chọn bằng cùng một quy tắc cho mọi tập. Một thứ tự chung trên vũ trụ cho phép mỗi tập giữ đúng một đại diện: phần tử của tập xuất hiện đầu tiên. Quan hệ “chung thứ tự” là thiết yếu, vì hai tập phải được so dưới cùng một phép thử.

Cho hoán vị $\pi$ của $U$. Với $u\in U$, $\operatorname{rank}_\pi(u)$ là vị trí từ $1$ đến $R$ của $u$ trong thứ tự ấy. Với $S\subseteq U$, $S\ne\varnothing$, định nghĩa

$$
h_\pi(S)=\arg\min_{u\in S}\operatorname{rank}_\pi(u).
$$

Các hạng khác nhau nên phần tử đạt cực tiểu là duy nhất. Trong tài liệu này, $h_\pi(S)$ trả **định danh phần tử**, không trả vị trí hoặc giá trị băm. Nếu dùng hạng thay định danh bằng cùng một ánh xạ một-một thì quan hệ hai kết quả bằng nhau được giữ nguyên, nhưng hai loại giá trị vẫn cần được phân biệt khi ghi bảng.

::: example Thứ tự của Ví dụ 3.7
Dùng $\pi=(b,e,a,d,c)$ cho bốn tập ở Hình 3.2.

| Vị trí trong $\pi$ | Phần tử | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---|---:|---:|---:|---:|
| 1 | b | 0 | 0 | 1 | 0 |
| 2 | e | 0 | 0 | 1 | 0 |
| 3 | a | 1 | 0 | 0 | 1 |
| 4 | d | 1 | 0 | 1 | 1 |
| 5 | c | 0 | 1 | 0 | 1 |

Đọc ô $1$ đầu tiên trong từng cột cho kết quả:

| Đại lượng | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| Định danh $h_\pi(S_c)$ | a | c | b | a |
| Hạng nhỏ nhất | 3 | 5 | 1 | 3 |

$S_1$ không chứa $b,e$ nên gặp $a$ đầu tiên ở vị trí 3. $S_2$ chỉ chứa $c$. $S_3$ chứa ngay phần tử đầu $b$. $S_4$ gặp $a$ trước $d,c$. Dữ kiện lấy từ Ví dụ 3.7, Hình 3.3, tr. 82–83.
:::

![Hai tập S1 và S4 cùng gặp a đầu tiên theo thứ tự b,e,a,d,c.](img/lec-05/minhash-hoan-vi.svg)

Với một cặp $S,T$, các phần tử ngoài $S\cup T$ không thuộc tập nào nên không thể được chọn. Gọi $u$ là phần tử đầu của hợp theo $\pi$. Nếu $u$ thuộc giao thì nó đứng đầu cả hai tập. Nếu $u$ chỉ thuộc một tập thì tập ấy chọn $u$, còn tập kia phải chọn phần tử khác. Đây là quan hệ xác định dưới mọi thứ tự; việc chọn thứ tự ngẫu nhiên sẽ biến nó thành một đẳng thức xác suất.

::: exercise Tự kiểm tra
Trong thứ tự trên, $S_1$ và $S_4$ có cùng MinHash. Kết quả này có suy ra $S_1=S_4$ hay không?
:::

::: solution Lời giải
Không. Hai tập chọn cùng $a$ nhưng $c$ chỉ thuộc $S_4$. Một đại diện chung của một phép thử chưa xác định toàn bộ tập.
:::

## 6. Định lý xác suất trùng MinHash

### Phát biểu

Cho $S,T\subseteq U$ đều không rỗng. Chọn $\pi$ **đều từ toàn bộ $R!$ hoán vị** của $U$ và dùng cùng $\pi$ cho hai tập. Khi đó

$$
\Pr[h_\pi(S)=h_\pi(T)]=\mathrm{SIM}(S,T).
$$

Xác suất nằm trên cách chọn $\pi$, trong khi $S,T$ cố định. Phát biểu không nói rằng một phép thử cho ra chính giá trị Jaccard: một phép thử chỉ cho kết quả trùng hoặc không trùng.

### Phân hoạch các hàng và ví dụ

Đối với hai cột của ma trận đặc trưng, có ba loại hàng:

| Loại | Giá trị hai cột | Ý nghĩa |
|---|---|---|
| $X$ | $(1,1)$ | Phần tử thuộc giao |
| $Y$ | $(1,0)$ hoặc $(0,1)$ | Phần tử thuộc đúng một tập |
| $Z$ | $(0,0)$ | Phần tử ngoài hợp |

Đặt $x=|S\cap T|$ và $y=|(S\cup T)\setminus(S\cap T)|$. Hợp có $x+y$ phần tử. Với $S_1=\{a,d\}$, $S_4=\{a,c,d\}$, có $X=\{a,d\}$, $Y=\{c\}$, $Z=\{b,e\}$; do đó $x=2,y=1$.

![Phân hoạch cho S1,S4: a,d thuộc giao; c thuộc phần riêng; b,e ngoài hợp.](img/lec-05/phan-tu-dau-hop.svg)

### Chứng minh

::: proof Đẳng thức xác suất
Gọi $u$ là phần tử xuất hiện đầu tiên của $S\cup T$ theo $\pi$. Mỗi phần tử trong hợp có cùng xác suất đứng đầu: đổi tên hai phần tử của hợp tạo một song ánh giữa các hoán vị mà phần tử thứ nhất đứng đầu và các hoán vị mà phần tử thứ hai đứng đầu. Vì chọn đều mọi hoán vị, các nhóm có cùng xác suất. Tổng xác suất bằng 1, nên mỗi phần tử có xác suất $1/(x+y)$.

Nếu $u\in S\cap T$, không phần tử nào của một trong hai tập đứng trước $u$, vì mọi phần tử ấy cũng thuộc hợp. Do đó $h_\pi(S)=u=h_\pi(T)$.

Nếu $u$ thuộc đúng một tập, giả sử $u\in S\setminus T$, thì $h_\pi(S)=u$ nhưng $h_\pi(T)\ne u$. Trường hợp $u\in T\setminus S$ tương tự. Vậy

$$
\{h_\pi(S)=h_\pi(T)\}=\{u\in S\cap T\}.
$$

Có $x$ phần tử thuận lợi trong $x+y$ phần tử đồng khả năng, nên xác suất bằng $x/(x+y)=|S\cap T|/|S\cup T|$. Các hàng loại $Z$ không thể được chọn và không ảnh hưởng kết luận.
:::

Chứng minh theo §3.3.3, tr. 83. Nó bao gồm trường hợp hai tập rời, khi $x=0$, và hai tập bằng nhau, khi $y=0$. Tập không rỗng là điều kiện để mỗi MinHash được xác định. Một quy ước kỹ thuật cho cột rỗng ở thuật toán sau không thay điều kiện này.

::: exercise Tự kiểm tra
(a) Với $S_1,S_4$, tính xác suất trùng dưới hoán vị đều và giải thích bằng phần tử đầu của hợp.

(b) Đặt $S_1'=S_1\cup\{e\}$. Tính $\Pr[h_\pi(S_1')=h_\pi(S_4)]$ và giải thích vì sao giá trị giảm so với ý (a).
:::

::: solution Lời giải
(a) Hợp là $\{a,c,d\}$. Mỗi phần tử có xác suất $1/3$ đứng đầu. Các trường hợp đứng đầu là $a$ hoặc $d$ làm hai MinHash trùng, nên xác suất bằng $2/3$, đúng Jaccard của hai tập.

(b) Giao vẫn là $\{a,d\}$, hợp thành $\{a,c,d,e\}$. Xác suất bằng $2/4=1/2$. Phần tử $e$ mở rộng hợp nhưng không thuộc giao, nên làm tăng khả năng phần tử đầu của hợp rơi vào phần riêng.
:::

## 7. Chữ ký và ước lượng Jaccard

### Định nghĩa

Một thành phần MinHash chỉ là một phép thử. Chọn $n\ge1$ hoán vị $\pi_1,\ldots,\pi_n$ và dùng cùng bộ hoán vị cho mọi tập. Chữ ký lý tưởng của tập không rỗng $S$ là vector

$$
\sigma(S)=\bigl(h_{\pi_1}(S),\ldots,h_{\pi_n}(S)\bigr)^{\mathsf T}.
$$

Đặt các chữ ký thành cột tạo ma trận có $n$ hàng phép thử và $C$ cột tập. §3.3.4, tr. 83, gợi ý $n$ khoảng 100 đến vài trăm, trong khi số hàng $R$ của ma trận đặc trưng là số phần tử khác nhau của cả kho. Đây là một kiểu hàng khác với ma trận đặc trưng, nơi mỗi hàng là một phần tử của $U$. Trong mô hình lý tưởng dùng để phân tích, mỗi hoán vị đều; giả thiết độc lập giữa các hoán vị sẽ cần thêm khi tính phương sai.

Ước lượng Jaccard là tỷ lệ các tọa độ tương ứng bằng nhau:

$$
\widehat{\mathrm{SIM}}(S,T)
=\frac1n\sum_{i=1}^n\mathbf1\{h_{\pi_i}(S)=h_{\pi_i}(T)\}.
$$

Biến chỉ báo $\mathbf1\{E\}$ bằng $1$ nếu $E$ đúng và bằng $0$ nếu sai. Tọa độ $i$ chỉ so với tọa độ $i$, vì chúng dùng cùng hoán vị. Lấy Jaccard giữa hai **tập giá trị** của chữ ký sẽ bỏ vị trí và tạo một phép tính khác.

### Ví dụ hai thứ tự cố định

Các tập vẫn là $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$, $S_4=\{a,c,d\}$. Hai thứ tự sau suy trực tiếp bằng cách sắp tăng các hàm của Ví dụ 3.8; ở đây chúng chỉ minh họa phép chọn phần tử.

| Thứ tự | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| $\pi_1=(e,a,b,c,d)$ | a | c | e | a |
| $\pi_2=(d,a,c,e,b)$ | d | c | d | d |

Chữ ký của $S_1,S_4$ đều là $(a,d)^{\mathsf T}$. Hai tọa độ trùng cho ước lượng $2/2=1$, trong khi $\mathrm{SIM}(S_1,S_4)=2/3$. Ngược lại, $\sigma(S_2)=(c,c)^{\mathsf T}$ và $\sigma(S_4)=(a,d)^{\mathsf T}$ không trùng tọa độ nào, nên ước lượng bằng $0$ trong khi $\mathrm{SIM}(S_2,S_4)=1/3$. Với $n$ nhỏ, ước lượng có thể lệch về cả hai phía. Ví dụ cố định này minh họa sai khác giữa một tỷ lệ hữu hạn và Jaccard thật; nó không là bằng chứng về phân phối chọn đều của hoán vị.

### Kỳ vọng số đếm và kỳ vọng tỷ lệ

Giữ cố định một cặp $S,T$, đặt $s=\mathrm{SIM}(S,T)$ và

$$
X_i=\mathbf1\{h_{\pi_i}(S)=h_{\pi_i}(T)\}.
$$

Khi mỗi $\pi_i$ đều, định lý cho $\Pr[X_i=1]=s$. Do $X_i$ chỉ nhận $0,1$, có $\mathbb E[X_i]=s$. Bởi tính tuyến tính của kỳ vọng,

$$
\mathbb E\!\left[\sum_{i=1}^nX_i\right]=\sum_{i=1}^n\mathbb E[X_i]=ns,
$$

và

$$
\mathbb E[\widehat{\mathrm{SIM}}(S,T)]=\frac1n ns=s.
$$

Do đó ước lượng không chệch trong mô hình trên. Kỳ vọng **số lần trùng** là $ns$; kỳ vọng **tỷ lệ trùng** là $s$. Hai kết quả này chỉ cần mỗi hoán vị có phân phối đều; tính tuyến tính của kỳ vọng không cần độc lập. Đây cũng là phân biệt cần giữ khi đọc cách diễn đạt ở §3.3.4, tr. 84.

### Chi phí so sánh

Nếu mỗi thành phần vừa một từ máy và phép so bằng tốn $O(1)$, hai chữ ký cần $n$ phép so bằng, tức $\Theta(n)$ thời gian, không phụ thuộc độ dài hai tài liệu hay kích thước hai tập shingle. Nếu làm cho mọi cặp trong kho, số phép so bằng là $nC(C-1)/2$. Chi phí tạo chữ ký là một bước riêng và được phân tích ở mục 10.

::: exercise Tự kiểm tra
Với cặp $S_1,S_4$ và $n=100$ hoán vị đều, tính kỳ vọng số tọa độ trùng và kỳ vọng tỷ lệ trùng.
:::

::: solution Lời giải
Jaccard thật là $s=2/3$. Kỳ vọng số tọa độ trùng bằng $ns=200/3$; một kỳ vọng của số đếm có thể không nguyên. Kỳ vọng tỷ lệ là $s=2/3$.
:::

## 8. Phương sai và đánh đổi độ dài chữ ký

Độ không chệch chỉ nói về trung bình của các lần lấy mẫu. Để mô tả mức dao động, giả sử thêm rằng $\pi_1,\ldots,\pi_n$ độc lập. Khi đó $X_1,\ldots,X_n$ là các biến Bernoulli độc lập cùng tham số $s$.

Do $X_i^2=X_i$,

$$
\operatorname{Var}(X_i)=\mathbb E[X_i^2]-(\mathbb E[X_i])^2=s-s^2=s(1-s).
$$

Độc lập làm các hiệp phương sai giữa những tọa độ khác nhau bằng $0$. Vì vậy

$$
\operatorname{Var}(\widehat{\mathrm{SIM}})
=\operatorname{Var}\!\left(\frac1n\sum_{i=1}^nX_i\right)
=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)
=\frac{s(1-s)}n.
$$

Độ lệch chuẩn tương ứng là $\sqrt{s(1-s)/n}$, giảm theo $1/\sqrt n$: muốn giảm độ lệch chuẩn một nửa phải tăng $n$ gấp bốn. Lập luận dùng mô hình chữ ký §3.3.4 và kiến thức phương sai cơ bản; không giả định công thức này cho một bộ hàm băm cố định bất kỳ.

Với $s=2/3$, phương sai là $2/(9n)$. Khi $n=100$, phương sai bằng $1/450$. Tăng $n$ giảm phương sai theo $1/n$, nhưng đồng thời tăng tuyến tính số thành phần cần lưu và số phép so bằng cho một cặp. Nếu $s=0$ hoặc $s=1$, phương sai bằng $0$ trong mô hình lý tưởng, phù hợp với việc mọi phép thử lần lượt luôn khác hoặc luôn trùng.

Kết quả về phương sai không khẳng định rằng một chữ ký dài hơn trong một lần chạy cụ thể luôn có sai số nhỏ hơn. Các tọa độ mới vẫn là kết quả ngẫu nhiên. Cũng không được áp dụng phép cộng phương sai như trên khi các phép thử có phụ thuộc mà chưa xét các số hạng hiệp phương sai.

::: exercise Tự kiểm tra
Nêu giả thiết thêm cần có để chuyển từ kết quả về kỳ vọng sang công thức phương sai trên. Phân biệt tác dụng của tăng $n$ đối với sai số quan sát và phương sai.
:::

::: solution Lời giải
Công thức phương sai dùng tính độc lập của các hoán vị, ngoài tính đều của mỗi hoán vị. Tăng $n$ giảm phương sai của ước lượng trong mô hình; nó không bảo đảm sai số tuyệt đối của từng mẫu cụ thể giảm sau mỗi lần bổ sung tọa độ.
:::

## 9. Tính chữ ký bằng cách quét các hàng

### Từ hoán vị sang giá trị băm

Lưu hoặc sắp xếp nhiều hoán vị của một vũ trụ lớn có thể tốn nhiều công việc. §3.3.5, tr. 84–86, thay việc duyệt riêng từng hoán vị bằng tính giá trị băm của từng hàng và cập nhật các cực tiểu. Các hàm phải dùng chung cho mọi cột.

Phép quét có một đặc tả xác định, kể cả khi các hàm được chọn chưa đáp ứng mô hình xác suất lý tưởng. Cho các số nguyên dương $R,C,n$, ma trận $M\in\{0,1\}^{R\times C}$ và các hàm

$$
f_i:\{0,\ldots,R-1\}\longrightarrow V,\qquad i=1,\ldots,n,
$$

trong đó $V$ là một miền hữu hạn có thứ tự toàn phần. Các chỉ số là $r=0,\ldots,R-1$, $c=1,\ldots,C$ và $i=1,\ldots,n$. Thêm giá trị canh $+\infty$ lớn hơn mọi phần tử của $V$. Đầu ra là ma trận $\mathrm{SIG}$ kích thước $n\times C$ với

$$
\mathrm{SIG}(i,c)
=\min\bigl(\{f_i(r):0\le r<R,\ M(r,c)=1\}\cup\{+\infty\}\bigr).
$$

Với cột không rỗng, ít nhất một ứng viên hữu hạn được lấy vào phép min nên kết quả hữu hạn. Với cột rỗng, tập lấy cực tiểu chỉ có $+\infty$; mọi thành phần của cột chữ ký bằng $+\infty$. Đây là quy ước đầu ra của thuật toán, không phải định nghĩa Jaccard cho hai tập rỗng.

$\mathrm{SIG}(i,c)$ lưu **giá trị băm**, khác với định danh $h_{\pi_i}(S_c)$ ở mô hình lý tưởng. Nếu $f_i$ là song ánh trên các mã hàng, sắp hàng theo giá trị $f_i$ tăng dần tạo một hoán vị. Hàng đạt cực tiểu là phần tử thắng theo thứ tự đó. Việc so hai cực tiểu bằng nhau khi ấy tương đương so hai định danh thắng bằng nhau. Nếu có va chạm, sự tương đương này có thể không còn.

### Dữ kiện Ví dụ 3.8

Giữ ma trận Hình 3.2 và mã hàng $a,b,c,d,e\leftrightarrow0,1,2,3,4$. Hình 3.4, tr. 85, dùng hai hàm

$$
f_1(r)=(r+1)\bmod5,\qquad f_2(r)=(3r+1)\bmod5.
$$

Phần dư được lấy trong $\{0,1,2,3,4\}$.

| $r$ | Phần tử | Các cột có 1 | $f_1(r)$ | $f_2(r)$ |
|---:|---|---|---:|---:|
| 0 | a | 1, 4 | 1 | 1 |
| 1 | b | 3 | 2 | 4 |
| 2 | c | 2, 4 | 3 | 2 |
| 3 | d | 1, 3, 4 | 4 | 0 |
| 4 | e | 3 | 0 | 3 |

Sắp tăng cột $f_1$ cho thứ tự $(e,a,b,c,d)$; sắp tăng cột $f_2$ cho thứ tự $(d,a,c,e,b)$. Đó chính là hai thứ tự đã dùng để minh họa chữ ký định danh ở mục 7. Với $S_1,S_4$, tọa độ thứ nhất chọn $a\leftrightarrow r=0$, có $f_1(0)=1$; tọa độ thứ hai chọn $d\leftrightarrow r=3$, có $f_2(3)=0$. Vì vậy chữ ký định danh $(a,d)^{\mathsf T}$ được lưu bằng chữ ký giá trị $(1,0)^{\mathsf T}$. Hai hàm cố định này không va chạm, nên phép so bằng được bảo toàn; tính không va chạm không chứng minh phân phối chọn đều hoán vị.

### Vết chạy đầy đủ

Khởi tạo mọi ô chữ ký bằng $+\infty$. Với mỗi hàng, tính hai giá trị băm rồi cập nhật từng thành phần của những cột có $1$. Bảng dưới ghi hai hàng chữ ký sau mỗi bước; vị trí trong mỗi vector lần lượt ứng với $S_1,S_2,S_3,S_4$.

| Trạng thái | Hàng chữ ký thứ nhất | Hàng chữ ký thứ hai |
|---|---|---|
| Khởi tạo | $(+\infty,+\infty,+\infty,+\infty)$ | $(+\infty,+\infty,+\infty,+\infty)$ |
| Sau $r=0$ | $(1,+\infty,+\infty,1)$ | $(1,+\infty,+\infty,1)$ |
| Sau $r=1$ | $(1,+\infty,2,1)$ | $(1,+\infty,4,1)$ |
| Sau $r=2$ | $(1,3,2,1)$ | $(1,2,4,1)$ |
| Sau $r=3$ | $(1,3,2,1)$ | $(0,2,0,0)$ |
| Sau $r=4$ | $(1,3,0,1)$ | $(0,2,0,0)$ |

Ở hàng $0$, chỉ $S_1,S_4$ chứa $a$. Cả hai giá trị băm bằng $1$, nên bốn phép min biến bốn ô từ $+\infty$ thành $1$. Hai cột còn lại giữ nguyên dù giá trị băm đã được tính.

Ở hàng $1$, chỉ chữ ký của $S_3$ nhận cặp $(2,4)$ và có giá trị hữu hạn đầu tiên. Ở hàng $2$, chữ ký của $S_2$ nhận $(3,2)$ từ trạng thái vô cực, còn chữ ký của $S_4$ đã có $(1,1)$ nên

$$
\min(1,3)=1,\qquad \min(1,2)=1.
$$

Hai phép min này vẫn được thực hiện dù không ô nào thay đổi. Vì vậy số phép min không bằng số lần giá trị lưu giảm xuống.

Hàng $3$ cung cấp ứng viên $(4,0)$ cho chữ ký của $S_1,S_3,S_4$. Chỉ thành phần thứ hai giảm về $0$. Hàng $4$ chỉ thuộc $S_3$ và cung cấp $(0,3)$: thành phần thứ nhất giảm từ $2$ về $0$, còn thành phần thứ hai giữ $0$ vì $\min(0,3)=0$. Các tọa độ của một chữ ký có thể đạt cực tiểu tại những phần tử khác nhau.

Kết quả cuối cùng là

$$
\mathrm{SIG}=\begin{pmatrix}
1&3&0&1\\
0&2&0&0
\end{pmatrix}.
$$

Cặp $S_1,S_4$ trùng cả hai tọa độ, nên ước lượng bằng $1$ so với Jaccard thật $2/3$. Cặp $S_1,S_3$ chỉ trùng tọa độ thứ hai, nên ước lượng bằng $1/2$ so với giá trị thật $1/4$. Các kết quả của bộ hàm cố định không phải phát biểu kỳ vọng trên phân phối hoán vị.

### Giả mã

```text
SIG(i, c) ← +∞ với mọi i = 1, …, n và c = 1, …, C
for r = 0, …, R − 1:
    vᵢ ← fᵢ(r) với i = 1, …, n
    for mỗi c có M(r, c) = 1:
        for i = 1, …, n:
            SIG(i, c) ← min(SIG(i, c), vᵢ)
return SIG
```

Mỗi giá trị $f_i(r)$ được tính một lần ở hàng $r$ rồi dùng cho mọi cột chứa phần tử ấy. Nếu đầu vào là danh sách cột có $1$ theo hàng, vòng lặp đi trực tiếp qua danh sách; nếu đầu vào là ma trận đặc, cần kiểm ô để tìm các cột tương ứng. Sau $R$ hàng, thuật toán dừng. Phép min có tính giao hoán và kết hợp, nên đổi thứ tự quét không đổi cực tiểu cuối cùng, dù các trạng thái trung gian có thể khác.

![Phép quét tính các giá trị băm cho hàng, tìm các cột có 1 rồi cập nhật từng thành phần bằng min.](img/lec-05/quet-ma-tran-thua.svg)

::: exercise Tự kiểm tra
Khi xử lý hàng $2$, giải thích vì sao chữ ký của $S_2$ thay đổi còn chữ ký của $S_4$ không đổi dù cả hai cột đều có ô $1$ ở hàng này.
:::

::: solution Lời giải
Trước hàng $2$, chữ ký của $S_2$ còn hai giá trị $+\infty$ nên ứng viên $(3,2)$ làm chúng giảm. Chữ ký của $S_4$ đang có $(1,1)$; mỗi ứng viên mới đều lớn hơn giá trị đã lưu, nên kết quả hai phép min vẫn là $(1,1)$.
:::

## 10. Bất biến, số phép tính và bộ nhớ

### Chứng minh thuật toán tính đúng cực tiểu

::: proof Bất biến sau tập hàng đã quét
Gọi $A$ là tập các mã hàng đã xử lý. Bất biến với mọi $i=1,\ldots,n$ và $c=1,\ldots,C$ là

$$
\mathrm{SIG}(i,c)
=\min\bigl(\{f_i(r):r\in A,\ M(r,c)=1\}\cup\{+\infty\}\bigr).
$$

**Khởi tạo.** Khi $A=\varnothing$, tập ứng viên hữu hạn rỗng. Cực tiểu của $\{+\infty\}$ bằng $+\infty$, đúng giá trị khởi tạo.

**Duy trì.** Xét một hàng mới $r$. Nếu $M(r,c)=0$, hàng này không thêm ứng viên cho cột $c$, nên giữ trạng thái là đúng. Nếu $M(r,c)=1$, tập ứng viên được bổ sung $f_i(r)$. Cực tiểu của tập mới bằng min giữa cực tiểu cũ và $f_i(r)$, đúng phép cập nhật. Do đó bất biến giữ sau khi thêm $r$ vào $A$.

**Kết thúc.** Vòng lặp xử lý đúng $R$ hàng rồi dừng, nên $A=\{0,\ldots,R-1\}$. Công thức bất biến trở thành hậu điều kiện ở mục 9. Với cột rỗng, không bước nào thêm giá trị hữu hạn nên kết quả vẫn là $+\infty$.
:::

Chứng minh xác nhận thuật toán tính đúng cực tiểu của các hàm đã cho. Nó không xác nhận rằng một họ hàm bất kỳ là phân phối hoán vị đều, cũng không suy ra chất lượng ước lượng khi giả thiết xác suất chưa được đáp ứng.

### Mô hình chi phí

Giả sử đầu vào đã có, mỗi mã hàng, mã cột và giá trị chữ ký vừa một từ máy; tính một hàm $f_i(r)$, kiểm một ô và lấy min đều tốn $O(1)$. Đặt $L=\operatorname{nnz}(M)$, tức **tổng số ô $1$** trong ma trận. Nếu dùng danh sách, giả sử các danh sách cột có $1$ theo hàng đã được xây sẵn.

| Công việc | Căn cứ đếm | Số thao tác | Ví dụ $R=5,C=4,n=2,L=9$ |
|---|---|---|---:|
| Khởi tạo chữ ký | Một lần cho mỗi ô đầu ra | $nC$ | 8 |
| Tính giá trị băm | $n$ hàm cho mỗi hàng | $nR$ | 10 |
| Kiểm ô của ma trận đặc | Một lần cho mỗi ô đầu vào | $RC$ | 20 |
| Lấy min | $n$ thành phần cho mỗi ô $1$ | $nL$ | 18 |

Nếu lưu ma trận đặc, tổng thời gian là

$$
\Theta(nC+nR+RC+nL).
$$

Nếu đã có danh sách cột có $1$ theo hàng, không cần quét các ô $0$, nên thời gian là

$$
\Theta(nC+nR+nL).
$$

Chi phí xây danh sách từ ma trận đặc không nằm trong giả thiết đầu vào thứ hai; nếu cần xây, phải tính thêm phần công việc đó. $nL$ đếm mọi phép min, bao gồm các phép giữ nguyên giá trị. Với Ví dụ 3.8, $nL=2\cdot9=18$.

Thuật toán đi qua các hàng một lần. Đếm trên là mô hình thao tác trong bộ nhớ; chưa là một cận I/O theo khối vì chưa quy định kích thước khối hoặc cách đặt dữ liệu trên thiết bị lưu trữ. Nếu đầu vào được đọc tuần tự theo hàng, mô tả một lượt quét vẫn giữ nguyên.

### Bộ nhớ và ý nghĩa của nén

Đầu ra cần $nC$ giá trị, tức $\Theta(nC)$ từ máy. Bộ đệm $v_1,\ldots,v_n$ cho một hàng cần $\Theta(n)$ từ. Hai số này chưa bao gồm ma trận hoặc danh sách đầu vào nếu chúng vẫn được giữ trong bộ nhớ.

Việc $n<R$ chỉ so sánh số hàng. Ma trận đặc trưng có ô nhị phân, còn chữ ký thường có giá trị nhiều bit; do đó không thể suy dung lượng bit giảm chỉ từ số hàng. Ví dụ ở tr. 81 minh họa tập mã khoảng 200.000 byte được thay bằng chữ ký 1.000 byte. Đó là một tình huống dung lượng trong sách, không phải bảo đảm rằng mọi chữ ký 1.000 byte đạt một mức sai số định trước.

::: exercise Tự kiểm tra
Với dữ liệu Ví dụ 3.8, nêu số lần khởi tạo, tính hàm băm, kiểm ô khi dùng ma trận đặc và lấy min. Xác định phần nào biến mất nếu đầu vào đã là danh sách cột có $1$ theo hàng.
:::

::: solution Lời giải
Các số lần lần lượt là $nC=8$, $nR=10$, $RC=20$ và $nL=18$. Với danh sách đã xây sẵn, không cần 20 phép kiểm ô của ma trận đặc; vẫn cần khởi tạo, tính băm và cập nhật các ô $1$.
:::

## 11. Giới hạn của hàm băm và trường hợp biên

### Hai tầng va chạm

Va chạm mã shingle xảy ra trước khi tạo chữ ký: hai chuỗi con khác nhau bị gộp thành cùng phần tử. Khi đó tập đầu vào đã thay đổi. Va chạm của hàm băm hàng xảy ra trong bước tính cực tiểu: hai phần tử khác nhau có thể cho cùng giá trị $f_i(r)$. Khi ấy hai tập rời cũng có thể có cực tiểu bằng nhau.

Vì vậy cần tách ba đối tượng: văn bản gốc, tập phần tử được chọn sau mã hóa và chữ ký của tập ấy. Định lý lý tưởng chỉ bảo toàn Jaccard của tập đã xác định, dưới các giả thiết về phép chọn.

### Hoán vị affine và điều kiện xác suất

Với mã hàng $0,\ldots,R-1$, xét

$$
f(r)=(ar+b)\bmod R.
$$

Hàm là hoán vị của các phần dư khi $\gcd(a,R)=1$. Thật vậy, nếu $f(r)=f(t)$ thì $a(r-t)\equiv0\pmod R$. Do $a$ khả nghịch modulo $R$, suy ra $r\equiv t\pmod R$; với hai mã hàng trong miền, có $r=t$. Hàm đơn ánh trên một tập hữu hạn có cùng miền và đích nên là song ánh.

Ngược lại, nếu $d=\gcd(a,R)>1$, hai mã $0$ và $R/d$ khác nhau nhưng

$$
a(R/d)\equiv0\pmod R,
$$

nên chúng nhận cùng giá trị sau khi cộng $b$. Vì vậy đây chính là điều kiện cho họ hàm trên. Số hàng nguyên tố không phải điều kiện cần. Trong Bài 3.3.3, hệ số $5$ modulo $6$ vẫn cho một hoán vị vì $\gcd(5,6)=1$.

Song ánh chỉ bảo đảm mỗi hàng có một giá trị khác nhau. Định lý ở mục 6 dùng cách chọn **đều trên toàn bộ hoán vị**. Một họ gồm các hàm riêng lẻ đều là song ánh chưa tự đáp ứng phân phối ấy. Kiểm bảng giá trị của một hàm có thể phát hiện va chạm; phép kiểm đó không xác định phân phối ngẫu nhiên của cả họ.

### Tập rỗng và chất lượng biểu diễn

Nếu $\ell<k$, tập shingle rỗng. Thuật toán quét vẫn trả cột $+\infty$ theo đặc tả, nhưng so hai cột vô cực rồi lấy tỷ lệ trùng không mở rộng được định lý đã chứng minh. Cần xử lý tập rỗng theo một quy ước riêng của ứng dụng trước khi diễn giải tương đồng.

Tập shingle giữ các đoạn con cục bộ, không giữ số lần lặp và toàn bộ thứ tự tài liệu. Vì thế kết quả phải được đọc là tương đồng theo biểu diễn đã chọn. Chữ ký giảm chi phí của biểu diễn đó; nó không sửa một lựa chọn đặc trưng không phù hợp với mục tiêu ứng dụng.

::: exercise Tự kiểm tra
Giải thích vì sao chứng minh bất biến của phép quét và chứng minh xác suất trùng MinHash là hai kết quả khác nhau.
:::

::: solution Lời giải
Bất biến chứng minh rằng đầu ra là các cực tiểu của những hàm đã cung cấp, kể cả hàm có va chạm. Định lý xác suất cần cùng một hoán vị đều và các tập không rỗng. Tính đúng của phép min không cung cấp những giả thiết xác suất còn thiếu.
:::

## 12. Đọc thêm: đa tập và shingle dựa trên từ dừng

Hai biến thể trong §3.1.3 và §3.2.4 giúp làm rõ việc chọn biểu diễn. Chúng không thay quy ước tập hợp của tuyến chính.

### Quy ước đa tập trong sách

Một đa tập cho phép một phần tử xuất hiện nhiều lần. Gọi $m_{B_1}(u)$ là số lần xuất hiện của $u$ trong đa tập $B_1$. Theo quy ước của §3.1.3, tr. 77, giao dùng số lần nhỏ hơn, còn hợp đa tập cộng các số lần. Cho hai đa tập hữu hạn $B_1,B_2$ với $\sum_u(m_{B_1}(u)+m_{B_2}(u))>0$. Điều kiện này loại trường hợp cả hai đa tập rỗng. Độ tương đồng được tính bằng

$$
\frac{\sum_u\min(m_{B_1}(u),m_{B_2}(u))}{\sum_u(m_{B_1}(u)+m_{B_2}(u))}.
$$

Với $B_1=\{a,a,a,b\}$ và $B_2=\{a,a,b,b,c\}$ của nguồn, giao chứa hai bản $a$ và một bản $b$, tổng là 3. Hợp theo phép cộng có $4+5=9$ phần tử tính cả số lần lặp. Tỷ số là $3/9=1/3$.

Trong quy ước này, một đa tập không rỗng so với chính nó cho $1/2$, không phải $1$. Chú thích của sách cũng nêu một quy ước hợp khác dùng số lần lớn hơn; hai quy ước tạo hai mẫu số khác nhau. Không được thay mẫu số của nguồn mà vẫn giữ cùng kết luận. Định lý MinHash đã chứng minh cho tập hợp không tự áp dụng cho đa tập theo công thức trên.

### Shingle bắt đầu bằng từ dừng

Các từ dừng là những từ xuất hiện thường xuyên và có thể dùng để xác định một kiểu shingle khác. §3.2.4, tr. 80, xét mỗi shingle gồm một từ dừng và hai từ ngay sau nó. Mục tiêu của ví dụ là làm nổi bật phần văn bản của bài báo so với những câu quảng cáo ngắn.

Ví dụ 3.5 dùng câu:

> *A* spokesperson *for* *the* Sudzo Corporation revealed today *that* studies *have* shown *it* *is* good *for* people *to* buy Sudzo products.

Các từ in nghiêng là chín vị trí bắt đầu được sách chọn: `A`, `for`, `the`, `that`, `have`, `it`, `is`, `for`, `to`. Hai lần `for` là hai vị trí khác nhau. Chín shingle là:

| Vị trí bắt đầu được chọn | Shingle ba từ |
|---|---|
| `A` | `A spokesperson for` |
| `for` lần đầu | `for the Sudzo` |
| `the` | `the Sudzo Corporation` |
| `that` | `that studies have` |
| `have` | `have shown it` |
| `it` | `it is good` |
| `is` | `is good for` |
| `for` lần sau | `for people to` |
| `to` | `to buy Sudzo` |

Câu quảng cáo `Buy Sudzo.` không tạo shingle như vậy. Những chuỗi tiếng Anh này là dữ kiện nguồn, được giữ nguyên để bảo toàn phép tạo đặc trưng.

Biến thể này thay đổi phần tử của tập: phần tử là một cụm ba từ được chọn theo vị trí từ dừng, không còn là mọi đoạn $k$ ký tự. Nó có thể giữ nguyên công thức Jaccard trên tập mới nhưng đo một biểu diễn khác. Danh sách từ dừng và quy tắc tách từ phải được xác định nhất quán trước khi dùng.

::: exercise Tự kiểm tra
Nêu hai quy ước cần phân biệt khi chuyển từ tuyến chính sang các biến thể trên.
:::

::: solution Lời giải
Với đa tập, phải nêu cách đếm số lần và đặc biệt mẫu số của phép hợp. Với shingle từ dừng, phải nêu đơn vị là từ và quy tắc chọn vị trí bắt đầu. Không thể dùng nguyên các phép đếm cửa sổ ký tự hoặc giả thiết của MinHash trên tập để thay cho những quy ước chưa xác định.
:::

## 13. Đọc thêm: rút ngắn lượt tìm và nhóm hàng

§§3.3.6–3.3.7, tr. 86–90, xét cách giảm số hàng phải xử lý cho mỗi thành phần. Các cách này cần xử lý những phép thử không cung cấp thông tin và không thay thuật toán đầy đủ đã chứng minh ở tuyến chính.

### Chỉ xét phần đầu của một hoán vị

Một cách trong §3.3.6 chọn đều một hoán vị của $U$, rồi chỉ xét $m$ hàng đầu, với $m$ nguyên và $1\le m<R$. Nếu một tập không có phần tử nào trong phần đầu ấy, giá trị của nó được ghi là $+\infty$ cho phép thử này. Đối với một cặp tập, có ba trường hợp:

| Kết quả của một phép thử | Cách xử lý |
|---|---|
| Cả hai giá trị hữu hạn | So bằng như thường lệ |
| Một hữu hạn, một $+\infty$ | Ghi nhận không trùng |
| Cả hai đều $+\infty$ | Không tính vào số trùng hoặc mẫu số |

Hai kết quả vô cực chỉ nói rằng đoạn đã xét không gặp phần tử của cả hai tập. Đếm chúng là trùng sẽ ghi nhận bằng chứng tương đồng từ việc không quan sát được phần tử. Tỷ lệ phải dùng các phép thử có thông tin; nếu không có phép thử nào như vậy thì tỷ lệ chưa được xác định.

Bảng xử lý trên không đủ để áp dụng ngay công thức phương sai $s(1-s)/n$: số phép thử hữu ích có thể khác giữa các cặp và là một đại lượng ngẫu nhiên. Tuyến chính giữ toàn bộ các hàng nên không có mẫu số thay đổi này.

### Nhóm các hàng

§3.3.7 xem một nhóm hàng như một tập con $T\subseteq U$. Trong nhóm, hai tập trở thành $S_1\cap T$ và $S_2\cap T$. Jaccard tính trong một nhóm có thể khác Jaccard toàn cục. Các điều kiện chọn nhóm ngẫu nhiên trong nguồn là một phần của phương pháp; không thể thay bằng bất kỳ cách chia cố định nào rồi suy rằng trung bình các tỷ số luôn bằng tỷ số toàn cục.

Hình 3.5 chia tám hàng thành hai nhóm bốn hàng:

| Hàng | $S_1$ | $S_2$ | $S_3$ | Nhóm |
|---:|---:|---:|---:|---|
| 1 | 0 | 0 | 0 | Bốn hàng đầu |
| 2 | 0 | 0 | 0 | Bốn hàng đầu |
| 3 | 0 | 0 | 1 | Bốn hàng đầu |
| 4 | 0 | 1 | 1 | Bốn hàng đầu |
| 5 | 1 | 1 | 1 | Bốn hàng cuối |
| 6 | 1 | 1 | 0 | Bốn hàng cuối |
| 7 | 1 | 0 | 0 | Bốn hàng cuối |
| 8 | 0 | 0 | 0 | Bốn hàng cuối |

Với cặp $S_1,S_2$, giao toàn cục có 2 phần tử, hợp có 4 nên Jaccard là $1/2$. Trong nhóm đầu, giao rỗng và hợp có 1 phần tử, cho $0$. Trong nhóm cuối, giao có 2 và hợp có 3, cho $2/3$. Trung bình hai giá trị theo nhóm là

$$
\frac12\left(0+\frac23\right)=\frac13\ne\frac12.
$$

Ví dụ cho thấy trung bình không trọng số của các tỷ số cục bộ không đồng nhất với tỷ số toàn cục. Những trường hợp hai tập hạn chế đều rỗng cũng cần loại khỏi phép so sánh tương ứng; không được tự gán trùng từ hai lần không quan sát được phần tử.

::: exercise Tự kiểm tra
Trong phương pháp chỉ xét một phần hoán vị, giải thích vì sao hai giá trị $+\infty$ không được tính là một lần trùng.
:::

::: solution Lời giải
Không tập nào có phần tử trong các hàng đã xét, nên chưa có phần tử thắng để so sánh. Hai giá trị canh giống nhau chỉ biểu thị cùng thiếu thông tin. Đếm chúng là trùng sẽ đồng nhất sự vắng mặt trong mẫu với việc chọn được cùng phần tử.
:::

## 14. Tổng kết và bài tập từ giáo trình

### Các phân biệt cần giữ

Quy trình đi từ chuỗi tới tập shingle, từ tập tới chữ ký và từ chữ ký tới tỷ lệ trùng tọa độ. Trong mô hình hoán vị đều, tỷ lệ này có kỳ vọng bằng Jaccard của tập đầu vào. Thuật toán quét hàng tính các cực tiểu; bất biến chứng minh tính đúng, còn mô hình lựa chọn hàm quyết định bảo đảm xác suất.

![Quy trình biểu diễn: tài liệu, tập shingle, chữ ký rồi tỷ lệ tọa độ trùng.](img/lec-05/quy-trinh-bieu-dien.svg)

Sáu nhiệm vụ tự kiểm bao quát tuyến chính:

1. Giải thích vì sao hai lần `ab` trong `abcdabd` chỉ tạo một phần tử của tập shingle.
2. Phân biệt 9 ký tự của đoạn gốc với 4 byte của mã băm.
3. Xác định đối tượng ở hàng và cột của ma trận đặc trưng.
4. Nêu biến cố tương đương hai MinHash trùng dưới cùng một thứ tự.
5. Viết công thức tỷ lệ trùng của $n$ tọa độ tương ứng.
6. Nêu giới hạn còn lại khi vẫn so sánh mọi cặp trong kho $C$ tài liệu.

::: solution Đáp án tự kiểm
Tập hợp giữ một bản của mỗi phần tử nên hai cửa sổ `ab` chỉ tạo một shingle. Số ký tự xác định độ dài shingle, còn số byte xác định dung lượng mã. Ma trận đặc trưng có hàng là phần tử và cột là tập. Hai MinHash trùng khi phần tử đầu trong hợp thuộc giao. Ước lượng là $\widehat{\mathrm{SIM}}=n^{-1}\sum_{i=1}^n\mathbf1\{h_{\pi_i}(S)=h_{\pi_i}(T)\}$. Nếu chưa chọn ứng viên thì vẫn có $C(C-1)/2$ cặp; chữ ký chỉ thay chi phí một cặp.
:::

### Bài 3.1.1 — Tính Jaccard

Nguồn: MMDS 3e, §3.1.4, tr. 78. Các nhãn $S_A,S_B,S_C$ dùng để gọi ba tập của đề.

::: exercise Đề bài
Cho $S_A=\{1,2,3,4\}$, $S_B=\{2,3,5,7\}$ và $S_C=\{2,4,6\}$. Tính độ tương đồng Jaccard của từng cặp tập. Trình bày bảng ba cặp gồm giao, hợp và tỷ số.
:::

::: solution Lời giải
Mỗi phần tử chỉ được đếm một lần trong hợp.

| Cặp | Giao | Hợp | Jaccard |
|---|---|---|---|
| $S_A,S_B$ | $\{2,3\}$ | $\{1,2,3,4,5,7\}$ | $2/6=1/3$ |
| $S_A,S_C$ | $\{2,4\}$ | $\{1,2,3,4,6\}$ | $2/5$ |
| $S_B,S_C$ | $\{2\}$ | $\{2,3,4,5,6,7\}$ | $1/6$ |

Tử số lần lượt là 2, 2, 1; mẫu số là 6, 5, 6. Dùng tổng kích thước hai tập làm mẫu số sẽ đếm lặp các phần tử giao.
:::

### Bài 3.2.3 — Số lượng shingle lớn nhất

Nguồn: MMDS 3e, §3.2.5, tr. 81. Ký hiệu độ dài tài liệu trong đề gốc là $n$, được đổi thành $\ell$ để dành $n$ cho độ dài chữ ký.

::: exercise Đề bài
Một tài liệu dài $\ell$ byte. Giả sử bảng chữ cái đủ lớn để có ít nhất $\ell$ chuỗi độ dài $k$. Xác định số $k$-shingle lớn nhất tài liệu có thể có. Trình bày công thức theo $\ell,k$ và lập luận theo vị trí cửa sổ.
:::

::: solution Đáp số và cận trên
Trong mô hình của bài này, mỗi ký tự chiếm một byte; tài liệu có $\ell$ vị trí ký tự và cửa sổ dài $k$ dùng cùng đơn vị. Công thức theo độ dài byte này không áp dụng trực tiếp cho số ký tự đã giải mã nếu một ký tự chiếm nhiều byte.

Nếu $1\le k\le\ell$, vị trí bắt đầu chạy từ $0$ đến $\ell-k$, nên có $\ell-k+1$ cửa sổ. Mỗi cửa sổ tạo nhiều nhất một shingle; các cửa sổ trùng nhau chỉ giảm số phần tử phân biệt. Vì vậy số shingle phân biệt không vượt $\ell-k+1$.

Nếu $\ell<k$, không có cửa sổ nào. Đáp số của bài nguồn, dưới giả thiết đã nêu, là

$$
\max(0,\ell-k+1).
$$

Lập luận đếm vị trí trên chứng minh cận trên. Sự tồn tại một chuỗi có các cửa sổ chồng lấn đều khác nhau, tức phần đạt cận, không được chứng minh trong phác thảo này.

Giả thiết nói về số **chuỗi độ dài $k$ khả dĩ**, không yêu cầu bảng chữ cái có ít nhất $\ell$ ký tự khác nhau.
:::

### Bài 3.3.1 — Jaccard và đếm hoán vị

Nguồn: MMDS 3e, §3.3.8, tr. 90; ma trận Hình 3.2, tr. 81.

::: exercise Đề bài
Cho ma trận sau:

| Phần tử | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---:|---:|---:|---:|
| a | 1 | 0 | 0 | 1 |
| b | 0 | 0 | 1 | 0 |
| c | 0 | 1 | 0 | 1 |
| d | 1 | 0 | 1 | 1 |
| e | 0 | 0 | 1 | 0 |

(a) Tính Jaccard của mọi cặp cột. Trình bày kích thước giao, hợp và tỷ số.

(b) Với mỗi cặp, tính tỷ lệ trong 120 hoán vị của năm hàng làm hai MinHash bằng nhau. Trình bày số hoán vị trùng, tỷ lệ và đối chiếu ý (a).
:::

::: solution Lời giải ý (a)
Các tập là $S_1=\{a,d\}$, $S_2=\{c\}$, $S_3=\{b,d,e\}$, $S_4=\{a,c,d\}$.

| Cặp | Giao | Hợp | Kích thước giao / hợp | Jaccard |
|---|---|---|---|---|
| 1–2 | $\varnothing$ | $\{a,c,d\}$ | $0/3$ | $0$ |
| 1–3 | $\{d\}$ | $\{a,b,d,e\}$ | $1/4$ | $1/4$ |
| 1–4 | $\{a,d\}$ | $\{a,c,d\}$ | $2/3$ | $2/3$ |
| 2–3 | $\varnothing$ | $\{b,c,d,e\}$ | $0/4$ | $0$ |
| 2–4 | $\{c\}$ | $\{a,c,d\}$ | $1/3$ | $1/3$ |
| 3–4 | $\{d\}$ | $\{a,b,c,d,e\}$ | $1/5$ | $1/5$ |
:::

::: solution Lời giải ý (b)
Có $5!=120$ hoán vị. Xét một cặp có hợp gồm $q$ phần tử. Bằng cách đổi tên các phần tử trong hợp, số hoán vị mà mỗi phần tử đứng đầu hợp là như nhau. Các nhóm này phân hoạch 120 hoán vị, nên mỗi nhóm có $120/q$ phần tử. Hai MinHash trùng đúng khi phần tử đứng đầu thuộc giao. Nếu giao có $x$ phần tử, số hoán vị trùng bằng $x\cdot120/q$.

| Cặp | $x$ | $q$ | Số hoán vị trùng | Tỷ lệ |
|---|---:|---:|---:|---|
| 1–2 | 0 | 3 | 0 | $0$ |
| 1–3 | 1 | 4 | 30 | $1/4$ |
| 1–4 | 2 | 3 | 80 | $2/3$ |
| 2–3 | 0 | 4 | 0 | $0$ |
| 2–4 | 1 | 3 | 40 | $1/3$ |
| 3–4 | 1 | 5 | 24 | $1/5$ |

Các tỷ lệ bằng Jaccard ở ý (a), phù hợp định lý. Phép đếm dựa trên đối xứng của 120 hoán vị, không cần liệt kê từng thứ tự.
:::

### Bài 3.3.2 — Bổ sung hai hàng chữ ký

Nguồn: MMDS 3e, §3.3.8, tr. 90; dữ liệu Hình 3.4, tr. 85, và Ví dụ 3.8, tr. 85–86. Ký hiệu hàm $h_3,h_4$ của đề được đổi thành $f_3,f_4$ để phân biệt băm hàng với MinHash trên tập.

::: exercise Đề bài
Dùng dữ liệu sau với mã hàng $0$ đến $4$:

| $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 | 1 |
| 4 | 0 | 0 | 1 | 0 |

Tính hai hàng chữ ký bổ sung bởi (a) $f_3(r)=(2r+4)\bmod5$ và (b) $f_4(r)=(3r-1)\bmod5$. Trình bày bảng giá trị hai hàm và hai hàng chữ ký.
:::

::: solution Lời giải
Phần dư nằm trong $\{0,1,2,3,4\}$; đặc biệt $(-1)\bmod5=4$.

| $r$ | $f_3(r)$ | $f_4(r)$ |
|---:|---:|---:|
| 0 | 4 | 4 |
| 1 | 1 | 2 |
| 2 | 3 | 0 |
| 3 | 0 | 3 |
| 4 | 2 | 1 |

Các tập hàng của bốn cột là $\{0,3\}$, $\{2\}$, $\{1,3,4\}$ và $\{0,2,3\}$. Lấy min đúng trên các tập hàng này:

| Hàm | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---|---|---|---|---|
| $f_3$ | $\min(4,0)=0$ | $3$ | $\min(1,0,2)=0$ | $\min(4,3,0)=0$ |
| $f_4$ | $\min(4,3)=3$ | $0$ | $\min(2,3,1)=1$ | $\min(4,0,3)=0$ |

Hai hàng mới là $(0,3,0,0)$ và $(3,0,1,0)$.
:::

### Bài 3.3.3 — Chữ ký, hoán vị và ước lượng

Nguồn: MMDS 3e, §3.3.8, tr. 90–91; Hình 3.6. Ký hiệu hàm của nguồn được đổi thành $f_i$ như ở thuật toán tính chữ ký.

::: exercise Đề bài
Cho ma trận sáu hàng:

| $r$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 2 | 1 | 0 | 0 | 1 |
| 3 | 0 | 0 | 1 | 0 |
| 4 | 0 | 0 | 1 | 1 |
| 5 | 1 | 0 | 0 | 0 |

Dùng $f_1(r)=(2r+1)\bmod6$, $f_2(r)=(3r+2)\bmod6$ và $f_3(r)=(5r+2)\bmod6$.

(a) Tính chữ ký mỗi cột.

(b) Xác định những hàm là hoán vị.

(c) Với sáu cặp cột, so sánh Jaccard ước lượng từ chữ ký với giá trị đúng. Trình bày bảng ước lượng, Jaccard thật và sai lệch tuyệt đối.
:::

::: solution Lời giải ý (a) và (b)
Bảng giá trị theo mã hàng:

| $r$ | $f_1(r)$ | $f_2(r)$ | $f_3(r)$ |
|---:|---:|---:|---:|
| 0 | 1 | 2 | 2 |
| 1 | 3 | 5 | 1 |
| 2 | 5 | 2 | 0 |
| 3 | 1 | 5 | 5 |
| 4 | 3 | 2 | 4 |
| 5 | 5 | 5 | 3 |

Các cột là $S_1=\{2,5\}$, $S_2=\{0,1\}$, $S_3=\{3,4\}$ và $S_4=\{0,2,4\}$. Lấy cực tiểu trên từng tập hàng cho ma trận

$$
\mathrm{SIG}=\begin{pmatrix}
5&1&1&1\\
2&2&2&2\\
0&1&4&0
\end{pmatrix}.
$$

Chẳng hạn, $S_4$ có các giá trị $(1,5,3)$ ở hàm thứ nhất, $(2,2,2)$ ở hàm thứ hai và $(2,0,4)$ ở hàm thứ ba; các cực tiểu là $(1,2,0)^{\mathsf T}$.

Chỉ $f_3$ nhận đủ sáu giá trị khác nhau nên là hoán vị. $f_1$ và $f_2$ có va chạm; tương ứng $\gcd(2,6)=2$, $\gcd(3,6)=3$, còn $\gcd(5,6)=1$. Ví dụ cho thấy modulo hợp số vẫn có thể tạo một hoán vị.
:::

::: solution Lời giải ý (c)
So sánh đúng các tọa độ tương ứng, rồi chia số lần trùng cho 3:

| Cặp | Số tọa độ trùng | Ước lượng | Jaccard thật | Sai lệch tuyệt đối |
|---|---:|---|---|---|
| 1–2 | 1 | $1/3$ | $0$ | $1/3$ |
| 1–3 | 1 | $1/3$ | $0$ | $1/3$ |
| 1–4 | 2 | $2/3$ | $1/4$ | $5/12$ |
| 2–3 | 2 | $2/3$ | $0$ | $2/3$ |
| 2–4 | 2 | $2/3$ | $1/4$ | $5/12$ |
| 3–4 | 2 | $2/3$ | $1/4$ | $5/12$ |

Các cặp 1–2, 1–3, 2–3 rời nhau. Mỗi cặp trong ba cặp còn lại có giao gồm một phần tử và hợp gồm bốn phần tử. Hai hàm đầu có va chạm nên các tập rời vẫn có thể có cực tiểu bằng nhau. Bộ ba hàm cố định này không đáp ứng mô hình chọn đều hoán vị; không thể dùng kết quả của nó để phủ định định lý lý tưởng. Ba thành phần cũng là một chữ ký ngắn, nhưng tăng số hàm không tự sửa một phân phối lựa chọn sai.
:::

### Nguồn và phạm vi

- Jure Leskovec, Anand Rajaraman và Jeffrey D. Ullman, *Mining of Massive Datasets* (MMDS), ấn bản thứ ba, Chương 3, §§3.1–3.3, tr. 73–91. Sách, slide chính thức và thông tin của tác giả có tại [mmds.org](http://www.mmds.org).
- Slide chính thức MMDS về tìm đối tượng tương đồng được dùng cùng sách để tổ chức trực giác và các bước tính. Các hình trong tài liệu đã được vẽ lại; bảng, ví dụ và bài tập giữ dữ kiện nguồn.
- Slide Stanford CS246 về LSH được đối chiếu ở phần shingling và MinHash. Phân dải chữ ký và tạo cặp ứng viên thuộc Bài 06; không là tiên quyết của các bài tập ở đây.

Toàn bộ số liệu dung lượng là ví dụ của nguồn. Các công thức chi phí là phép đếm từ giả mã dưới mô hình đã nêu, không phải kết quả đo tốc độ. Công thức phương sai được suy từ mô hình hoán vị đều, độc lập và các tính chất của biến chỉ báo.
