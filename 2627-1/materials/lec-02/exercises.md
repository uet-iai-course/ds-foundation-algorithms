# Bài tập Bài 02 — Mô hình tính toán MapReduce

Các bài tập củng cố 02.5–02.8 dưới đây lấy từ bài tập Chương 2 của sách *Mining of Massive Datasets*, ấn bản 3 (viết tắt MMDS), kèm gợi ý và lời giải. Mọi số hiệu Định nghĩa, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán, Ví dụ và Tình huống 02.k là của [ghi chú Bài 02](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html), nơi Bài tập 02.1–02.4 đứng ngay sau các mục; ký hiệu dùng như trong bảng ký hiệu của ghi chú. Bài 02.6, 02.7 và câu (d) của Bài 02.8, tức MMDS Bài 2.3.1(a), (b), (d), là bài tập trên lớp (recitation) của [bộ trang chiếu Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html). Bài tập xếp theo ba mức.

## Mục tiêu và bài tập

| Mục tiêu học tập của ghi chú | Bài tập trong ghi chú | Bài tập trong tệp này |
|---|---|---|
| 1. Đặc tả Map, Reduce, hàm phân phối, nhóm theo khóa; chạy tay và chứng minh một công việc (Mục 1, Mục 2) | 02.1 | 02.5 |
| 2. Điều kiện để Combine giữ nguyên kết quả; phản ví dụ trung bình trực tiếp (Mục 1.2, 2.4, 3.3) | 02.2 | 02.6, 02.7, 02.8 |
| 3. Chọn khóa và giá trị trung gian; chứng minh tính đúng (Mục 3) | 02.2 | 02.5, 02.6, 02.7, 02.8 |
| 4. Tổng khối lượng tính toán, thời gian, chi phí truyền thông, mức tăng tốc (Mục 4) | 02.1, 02.3 | — |
| 5. (Đọc thêm) Phần phải chạy lại khi máy hỏng; chạy lại không tính trùng; kỳ vọng thời gian khi tác vụ hỏng | 02.4 | — |
| 6. Chạy đếm từ trên Hadoop và đối chiếu bộ đếm (Mục 5) | — | — |

## Mức nhận biết

::: exercise Bài tập 02.5 (Nhân ma trận chữ nhật với véc-tơ; MMDS Bài 2.3.2, §2.3.11, tr.40)
Định nghĩa 02.17, Thuật toán 02.18 và Mệnh đề 02.19 viết cho ma trận vuông $q\times q$, như MMDS (§2.3.1). Tổng quát hóa thuật toán cho ma trận $A$ có $p$ hàng và $q$ cột, với $p,q\ge1$ bất kỳ. (Sách viết ma trận $r\times c$; ở đây ta viết $p\times q$ vì $r$ là số tác vụ Reduce; chữ $p$ chỉ dùng trong bài này.) Nêu rõ:

- (a) đầu vào, đầu ra, miền của khóa và độ dài của véc-tơ $v$;
- (b) hàm Map, Combine, Reduce, phần nào của thuật toán phụ thuộc $p$, $q$, và chứng minh tính đúng;
- (c) số cặp Map phát, độ dài mỗi danh sách $L_i$ và số phép cộng của Reduce khi không có Combine, với ma trận đặc.
:::

::: hint
Viết lại công thức $y_i=\sum_ja_{ij}v_j$ với hai giới hạn chỉ số khác nhau, rồi xem chỉ số nào đi vào khóa và chỉ số nào đi vào phép tra $v_j$.
:::

::: solution
**Câu (a).** Đầu vào là các bản ghi $(i,j,a_{ij})$ với $1\le i\le p$, $1\le j\le q$, mỗi tọa độ một bản ghi, và véc-tơ $v\in\mathbb R^q$ vừa bộ nhớ mỗi máy chạy Map. Đầu ra là $y=Av\in\mathbb R^p$, dưới dạng $p$ cặp $(i,y_i)$ với $y_i=\sum_{j=1}^{q}a_{ij}v_j$. Khóa nằm trong $\{1,\ldots,p\}$; $v$ có $q$ thành phần, bằng số cột, không phải số hàng.

**Câu (b).** Thuật toán 02.18 giữ nguyên: Map trên $(i,j,a_{ij})$ phát $(i,a_{ij}v_j)$; Combine và Reduce cộng các giá trị của khóa $i$. Chỉ có hai chỗ phụ thuộc kích thước: chỉ số cột $j$, dùng để tra $v_j$, chạy tới $q$, và khóa hàng $i$ chạy tới $p$. Chứng minh của Mệnh đề 02.19 không dùng điều kiện số hàng bằng số cột: Bước 1 chỉ cần mỗi tọa độ một bản ghi, nên khóa của $Z$ là $1,\ldots,p$ và $L_i$ là một hoán vị của $(a_{i1}v_1,\ldots,a_{iq}v_q)$; Bước 2 và Bước 3 giữ nguyên. Vậy đầu ra gồm đúng $p$ cặp $(i,y_i)$.

**Câu (c).** Map phát $pq$ cặp, một cho mỗi bản ghi. Mỗi danh sách $L_i$ có $q$ tích, và Reduce cho hàng $i$ làm $q-1$ phép cộng khi tổng khởi tạo bằng phần tử đầu, tổng $p(q-1)$ phép cộng.

**Kiểm tra lại.** Với $p=q=4$ ta được Ví dụ 02.6: 16 cặp, mỗi $L_i$ có 4 tích, $4\cdot3=12$ phép cộng khi không Combine. Ma trận $1\times q$ cho một khóa với danh sách $q$ tích; ma trận $p\times1$ cho $p$ khóa, mỗi danh sách một tích và Reduce không làm phép cộng nào.
:::

## Mức tính toán hoặc chứng minh

::: exercise Bài tập 02.6 (Số nguyên lớn nhất; MMDS Bài 2.3.1(a), §2.3.11, tr.40)
Một tệp rất lớn chứa $n\ge1$ số nguyên $a_1,\ldots,a_n$, chia thành $m$ phần cho $m$ tác vụ Map. Thiết kế thuật toán MapReduce trả số nguyên lớn nhất của tệp; có thể giả sử khóa của cặp đầu ra bị bỏ đi.

- (a) Nêu hàm Map, Combine, Reduce.
- (b) Chứng minh thuật toán đúng, có hay không có Combine.
- (c) Đếm số cặp trung gian gửi tới Reduce khi Combine được gọi một lần cho khóa của mỗi tác vụ Map. Nêu cách xử lý tệp rỗng.
:::

::: hint
Dùng một khóa chung $g$ để mọi giá trị về một reducer, và kiểm phép lấy giá trị lớn nhất theo các giả thiết của Mệnh đề 02.15.
:::

::: solution
**Câu (a).** Map trên $a_i$ phát $(g,a_i)$. Combine và Reduce nhận $(g,L)$ và phát $(g,\max L)$.

**Câu (b).** Phép $x\oplus y=\max(x,y)$ trên $\mathbb Z$ giao hoán, và kết hợp vì $\max(\max(x,y),z)$ và $\max(x,\max(y,z))$ đều bằng số lớn nhất trong ba số $x,y,z$. Với $L$ khác rỗng, $\bigoplus L=\max L$. Theo Mệnh đề 02.11, Reduce được gọi một lần cho khóa $g$ với $L_g$ chứa đúng các giá trị $a_1,\ldots,a_n$, nên phát $\max_ia_i$; phép lấy giá trị lớn nhất không phụ thuộc thứ tự. Combine phát đúng một cặp $(g,\bigoplus L)$ và Reduce là $\phi(\bigoplus L)$ với $\phi$ đồng nhất, nên theo Mệnh đề 02.15, Combine không đổi kết quả.

**Câu (c).** Không có Combine, $H=n$ cặp. Có Combine, theo cùng lập luận như Mệnh đề 02.35(b) với một khóa duy nhất $g$, mỗi tác vụ Map có ít nhất một số gửi đúng một cặp, nên $H=m$ khi mọi phần khác rỗng. Với tệp rỗng, Map không phát cặp nào, không có nhóm và Reduce không được gọi; chương trình chính phải báo "không có giá trị lớn nhất". Trả 0 là sai: tệp rỗng không có giá trị lớn nhất; dùng 0 làm giá trị khởi tạo của phép lấy giá trị lớn nhất cũng sai với tệp toàn số âm.

**Kiểm tra lại.** Với hai tác vụ Map giữ $[2,4]$ và $[9]$, Combine phát 4 và 9, Reduce phát 9, đúng giá trị lớn nhất của $2,4,9$.
:::

::: exercise Bài tập 02.7 (Trung bình cộng của tệp số nguyên; MMDS Bài 2.3.1(b), §2.3.11, tr.40)
Một tệp rất lớn chứa $n$ số nguyên $a_1,\ldots,a_n$, chia thành $m$ phần cho $m$ tác vụ Map. Thiết kế thuật toán MapReduce trả trung bình cộng của mọi số trong tệp; có thể giả sử khóa của cặp đầu ra bị bỏ đi.

- (a) Nêu hàm Map, Combine, Reduce và kiểu giá trị mỗi hàm phát.
- (b) Giải thích vì sao dùng Reduce làm Combine thì sai, bằng một phản ví dụ có số.
- (c) Nêu điều kiện để kết quả xác định, và chỉ ra lỗi khi Reduce dùng phép chia nguyên.
:::

::: hint
Gộp trạng thái tổng–số lượng, không gộp trung bình; phép chia chỉ làm ở Reduce.
:::

::: solution
**Câu (a).** Áp Thuật toán 02.25: Map trên $a_i$ phát $(g,(a_i,1))$; Combine nhận $(g,L)$ và phát $(g,\bigoplus L)$ với $(s,\kappa)\oplus(s',\kappa')=(s+s',\kappa+\kappa')$; Reduce tính $(s^\ast,\kappa^\ast)=\bigoplus L$ và phát $(g,s^\ast/\kappa^\ast)$. Map và Combine phát trạng thái $(s,\kappa)$; Reduce phát một số. Tính đúng là Mệnh đề 02.26.

**Câu (b).** Reduce phát một số, không phát trạng thái, nên dùng nó làm Combine vi phạm điều kiện giữ kiểu $V_2$ của Mệnh đề 02.15. Nếu các số đó vẫn được lấy trung bình ở Reduce: với hai tác vụ Map giữ $[2,4]$ và $[9]$, Combine phát 3 và 9, Reduce phát $(3+9)/2=6$, trong khi trung bình đúng là $15/3=5$.

**Câu (c).** Kết quả xác định khi $n\ge1$. Với tệp rỗng, không có nhóm và Reduce không phát cặp nào; trung bình không xác định vì số phần tử bằng 0, nên chương trình chính phải báo "trung bình không xác định" thay cho trả 0. Với số nguyên, tổng $s^\ast$ tính chính xác khi không tràn, nên giả thiết số học chính xác của Mệnh đề 02.26 thỏa. Nhưng $\mu=s^\ast/\kappa^\ast$ có thể không nguyên, nên Reduce phải chia ra số hữu tỷ hoặc số thực: với tệp $1,2$, phép chia nguyên $3$ chia $2$ lấy phần nguyên cho 1, còn trung bình đúng là $1{,}5$.

**Kiểm tra lại.** Với $2,4,9$: Combine phát $(6,2)$ và $(9,1)$, Reduce gộp được $(15,3)$ và phát 5.
:::

## Mức vận dụng

::: exercise Bài tập 02.8 (Tập giá trị phân biệt và số giá trị phân biệt; MMDS Bài 2.3.1(c), (d), §2.3.11, tr.40)
Một tệp rất lớn chứa $n$ số nguyên. Thiết kế thuật toán MapReduce trả:

- (c) chính tập các số nguyên đó, mỗi số chỉ xuất hiện một lần;
- (d) số giá trị phân biệt của tệp, ký hiệu $D$ như Định nghĩa 02.21 với từ thay bằng số nguyên.

Có thể giả sử khóa của mỗi cặp đầu ra bị bỏ đi. Với mỗi câu, nêu hàm Map, Combine, Reduce, chứng minh tính đúng, xử lý tệp rỗng và đếm số cặp trung gian, số cặp đầu ra của mỗi công việc.
:::

::: hint
Ở câu (c), dùng chính số nguyên làm khóa để các bản trùng gặp nhau, như công việc 1 của Thuật toán 02.22; vì khóa đầu ra bị bỏ, giá trị đầu ra phải mang số nguyên. Ở câu (d), đếm các cặp đầu ra của câu (c).
:::

::: solution
**Câu (c).** Map trên số $a$ phát $(a,a)$. Combine và Reduce nhận $(a,L)$ và phát một cặp $(a,a)$. Bỏ khóa của cặp đầu ra còn lại giá trị $a$.

- Tính đúng: theo Mệnh đề 02.11, mỗi giá trị phân biệt $a$ của tệp là một khóa của $Z$ và Reduce được gọi đúng một lần cho nó, phát đúng một cặp; một số không có trong tệp không là khóa. Vậy đầu ra là tập các giá trị, mỗi giá trị một lần. Với $\oplus=\max$ trên $\mathbb Z$, phép gộp kết hợp, giao hoán, và trên danh sách gồm toàn giá trị $a$ thì $\bigoplus L=a$; Combine và Reduce có dạng của Mệnh đề 02.15 với $\phi$ đồng nhất, nên Combine không đổi kết quả. Đây là phép loại trùng của Bài tập 02.2.
- Tệp rỗng: đầu ra rỗng, đúng là tập rỗng.
- Số cặp: Map phát $n$ cặp; sau Combine, mỗi tác vụ Map gửi một cặp cho mỗi giá trị phân biệt của phần nó đọc, nên $H\le n$; đầu ra có $D$ cặp.

**Câu (d).** Dùng hai công việc như Thuật toán 02.22. Công việc 1 là câu (c). Công việc 2: Map đổi mỗi cặp $(a,a)$ thành $(g,1)$; Combine và Reduce cộng các giá trị của khóa $g$; giá trị của cặp đầu ra là $D$. Chương trình chính trả $D=0$ khi công việc 1 không có đầu ra, vì khi đó công việc 2 không có nhóm nào và Reduce không được gọi.

- Tính đúng: đầu ra của công việc 1 có đúng một cặp cho mỗi giá trị phân biệt; công việc 2 đếm các cặp đó bằng phép cộng, kết hợp và giao hoán. Lập luận giống Mệnh đề 02.23 với từ thay bằng số nguyên.
- Số cặp: công việc 1 có tối đa $n$ cặp trung gian và $D$ cặp đầu ra; công việc 2 có $D$ cặp trung gian khi không Combine, nhiều nhất một cặp mỗi tác vụ Map khi có Combine, và một cặp đầu ra.
- Đề không quy định số công việc. Một công việc với một tác vụ Reduce giữ tập các giá trị đã gặp cũng trả đúng $D$, nhưng tác vụ đó cần bộ nhớ tỷ lệ với $D$; cộng số giá trị phân biệt của từng tác vụ Map thì sai khi một giá trị có mặt ở hai tác vụ, như $2+2=4$ thay cho 3 ở Ví dụ 02.7.

**Kiểm tra lại.** Tệp $2,4,2$ với hai tác vụ Map giữ $[2,4]$ và $[2]$: công việc 1 cho Reduce nhận khóa 2 với $[2,2]$ và khóa 4 với $[4]$, phát $(2,2)$, $(4,4)$; tập là $\{2,4\}$; công việc 2 nhận 2 cặp và phát $(g,2)$, nên $D=2$. Cộng số giá trị phân biệt của hai phần cho $2+1=3$, sai.
:::
