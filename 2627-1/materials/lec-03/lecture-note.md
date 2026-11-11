# Bài 03 — PageRank: mô hình và tính toán

Máy tìm kiếm cần một điểm cho mỗi trang web mà người viết trang khó tự nâng lên. PageRank lấy điểm đó từ cấu trúc liên kết: mỗi trang chia điểm của mình cho các trang nó trỏ tới, và phép chia lặp lại tới khi điểm ổn định. Chúng ta lập mô hình này trên một đồ thị bốn trang, sửa nó để phép lặp hội tụ trên mọi đồ thị, chứng minh tốc độ hội tụ, rồi tính mỗi vòng lặp bằng MapReduce theo khối và đếm chi phí của cách tính đó.

[Bộ trang chiếu Bài 03](lecture-03-pagerank-mo-hinh-va-tinh-toan.html) trình bày cùng chủ đề; [tệp bài tập Bài 03](material-viewer.html?doc=materials/lec-03/exercises.md&deck=lecture-03-pagerank-mo-hinh-va-tinh-toan.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Lập ma trận liên kết của một đồ thị nhỏ, tính một vòng chia điểm và giải hệ $r=M_0r$ với điều kiện tổng bằng 1 (Mục 1, Mục 2.1).
2. Nhận diện nút cụt và bẫy liên kết, tính một vòng của quy tắc cập nhật đầy đủ và giải hệ PageRank có bước nhảy (Mục 2.2, Mục 2.3).
3. Chứng minh tổng điểm được bảo toàn và phép lặp hội tụ; dùng độ thay đổi $\Delta_t$ cùng cận sai số để chọn ngưỡng dừng (Mục 2.4, Mục 2.5).
4. Biểu diễn đồ thị bằng danh sách liên kết ra và theo khối; đặc tả Map, Combine, Reduce của một vòng theo khối và chứng minh nó cho cùng kết quả với phép tính trên một máy (Mục 3).
5. Tính dung lượng lưu, bộ nhớ một tác vụ, đầu vào Map, đầu vào Reduce có và không có Combine, và thời gian pha Map khi tăng số máy (Mục 4).
6. Chạy `pagerank.py` và đối chiếu kết quả với các phép tính tay của chương (Mục 5).
7. (Đọc thêm.) Loại nút cụt đệ quy và khôi phục điểm của các nút đã loại.

## Kiến thức tiên quyết

Số hiệu `01.k`, `02.k` chỉ ghi chú Bài 01, Bài 02; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Mô hình chi phí** (Định nghĩa 01.13). Khối lượng tính toán, bộ nhớ làm việc, đọc ghi, dữ liệu mạng và dung lượng lưu trữ là các đại lượng riêng, mỗi đại lượng có đơn vị riêng; số của hai đại lượng không cộng được với nhau.
- **Bất biến vòng lặp** (CLRS 4e, §2.1; Mệnh đề 01.12). Một mệnh đề đúng trước vòng đầu, được giữ qua mỗi vòng và khi vòng lặp dừng cho điều cần chứng minh.
- **Tính đúng của một công việc MapReduce** (Thuật toán 02.10, Mệnh đề 02.11). Khi đầu vào được chia theo vị trí, Map và Reduce xác định và dừng, Reduce không phụ thuộc thứ tự danh sách và hàm phân phối khóa $h$ là một hàm, mỗi khóa phân biệt $i$ nhận đúng một danh sách $L_i$ chứa mọi giá trị đi cùng $i$, và Reduce được gọi đúng một lần cho khóa đó.
- **Combine với hàm hoàn tất** (Định nghĩa 02.14, Mệnh đề 02.15). Nếu Reduce trên khóa $i$ trả $\phi(\bigoplus L_i)$ với $\oplus$ kết hợp, giao hoán và mỗi lần gọi Combine trên $(i,L)$ phát đúng một cặp $(i,\bigoplus L)$, thì Combine không đổi đầu ra của công việc. Combine chỉ gộp các cặp trong một tác vụ Map; hai cặp cùng khóa từ hai tác vụ khác nhau chỉ gặp nhau ở Reduce (Ví dụ 02.5).
- **Nhân ma trận–véc-tơ** (Định nghĩa 02.17, Thuật toán 02.18, Mệnh đề 02.19, Nhận xét 02.20, Tình huống 02.3). Map trên phần tử $a_{ij}$ phát $(i,a_{ij}v_j)$, Reduce cộng theo khóa hàng $i$ và trả $y_i=\sum_ja_{ij}v_j$. Khi ma trận chỉ lưu phần tử khác 0, hàng toàn 0 không có cặp nào và vắng khỏi đầu ra; khi $v$ không vừa bộ nhớ, ma trận được chia thành dải dọc.
- **Thời gian pha và mức tăng tốc** (Định nghĩa 02.30, 02.39). Thời gian một pha là $\max_\nu t_\nu$, với $t_\nu$ là tổng thời gian các tác vụ giao cho máy $\nu$; mức tăng tốc trên $P$ máy là $T_1/T_P$, tỷ số thời gian trên một máy và trên $P$ máy.
- **Chi phí truyền thông và cận truyền** (Định nghĩa 02.33, Mệnh đề 02.38). Chi phí truyền thông của một công việc là $C=I+H$, với $I$ là tổng đầu vào các tác vụ Map và $H$ là tổng đầu vào các tác vụ Reduce; chuyển $Q$ byte qua một đường nối có băng thông $B$ cần ít nhất $Q/B$ giây.
- **Đại số tuyến tính và xác suất.** Tích $y=Av$; một ma trận vuông khả nghịch khi và chỉ khi chỉ véc-tơ 0 có ảnh bằng 0; một phân phối trên $n$ phần tử là véc-tơ $r\ge0$ với $\sum_ir_i=1$; bất đẳng thức tam giác $\lvert a+b\rvert\le\lvert a\rvert+\lvert b\rvert$.

## Bảng ký hiệu

Các ký hiệu dưới đây dùng xuyên suốt chương; chữ chỉ dùng trong một ví dụ, một chứng minh hay một bài tập được giới thiệu tại chỗ. Mỗi chữ trong bảng giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $G=(V,E)$; $n$; $m$ | đồ thị web; số trang $n=\lvert V\rvert$; số liên kết $m=\lvert E\rvert$ | đồ thị có hướng hữu hạn; $n\ge1$; $m\ge0$ |
| $j\to i$ | liên kết từ trang nguồn $j$ tới trang đích $i$ | cạnh của $E$ |
| $d_j$; $\mathcal D$; $n_+$ | bậc ra của trang $j$; tập nút cụt $\{j:d_j=0\}$; số trang không cụt $n-\lvert\mathcal D\rvert$ | số nguyên $\ge0$; tập con của $V$ |
| $r$; $r_i$; $r^t$; $r^*$ | véc-tơ điểm; điểm của trang $i$; véc-tơ sau $t$ vòng; điểm cố định | $\mathbb R^n$, thường là phân phối |
| $u$; $\mathbf 1$; $\mathbf 1_{\mathcal D}$ | phân phối đều, $u_i=1/n$; véc-tơ toàn 1; véc-tơ chỉ báo của $\mathcal D$ | $\mathbb R^n$ |
| $M_0$ | ma trận liên kết, cột là trang nguồn | $\mathbb R^{n\times n}$, phần tử $\ge0$ |
| $\bar M$ | ma trận $M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$: cột nút cụt thay bằng $u$ | $\mathbb R^{n\times n}$, mọi cột tổng 1 |
| $\beta$ | xác suất đi theo một liên kết ra | $0<\beta<1$ |
| $\delta^t$ | tổng điểm ở nút cụt sau $t$ vòng, $\sum_{j\in\mathcal D}r^t_j$ | $[0,1]$ |
| $F$ | ánh xạ cập nhật đầy đủ, $r^{t+1}=F(r^t)$ | $\mathbb R^n\to\mathbb R^n$ |
| $\lVert x\rVert_1$; $\mathrm I_n$ | chuẩn tổng trị tuyệt đối, $\sum_i\lvert x_i\rvert$; ma trận đơn vị cấp $n$ | số thực $\ge0$; $\mathbb R^{n\times n}$ |
| $\Delta_t$; $\tau$; $\varepsilon$; $K$; $t_{\text{dừng}}$ | độ thay đổi $\lVert r^{t+1}-r^t\rVert_1$; ngưỡng dừng; sai số cần đạt; số vòng tối đa; số vòng thực chạy | $\Delta_t\ge0$; $\tau,\varepsilon>0$; $K,t_{\text{dừng}}$ nguyên dương |
| $z$; $z_i$ | tổng đóng góp chưa nhân $\beta$, $z=M_0r$; thành phần của trang $i$ | $\mathbb R^n$ |
| $k$; $V_b$; $M_{ab}$; $r_b$; $z_a$ | số dải mỗi chiều; dải trang thứ $b$; khối đích $V_a$, nguồn $V_b$; dải điểm; dải tổng | $1\le a,b\le k$ |
| $R$; $q$ | số bản ghi của biểu diễn khối; số cặp đầu ra Map sau Combine | số nguyên $\ge0$ |
| $s$ | tổng của $\beta M_0r$, phần điểm đi theo liên kết trong một vòng | $[0,\beta]$ |
| $S_{\text{dense}}$; $S_{\text{adj}}$; $S_{\text{blocks}}$ | dung lượng ma trận đặc; danh sách liên kết ra; biểu diễn khối | byte |
| $B_{\text{task}}$; $B_{\text{buf}}$ | bộ nhớ một tác vụ khối; bộ đệm đọc khối | byte |
| $I$; $H$; $C$; $Q$ | đầu vào Map; đầu vào Reduce, kể cả cặp khởi tạo; $C=I+H$; byte từ Map tới Reduce đi qua mạng | byte |
| $P$; $\nu$; $t_\nu$ | số máy; chỉ số máy; tổng thời gian các tác vụ giao cho máy $\nu$ | số nguyên $\ge1$; giây |
| $c_e$; $W$; $w_{\max}$ | thời gian xử lý một cạnh ở Map; tổng việc pha Map; việc của tác vụ nặng nhất | giây |
| $T_{\text{map}}$; $T_{\text{shuffle}}$; $T_\delta$; $T_{\text{reduce}}$; $T_{\text{sync}}$ | thời gian pha Map; pha chuyển dữ liệu trung gian (shuffle) và nhóm; pha tính $\delta$; pha Reduce; pha đồng bộ và kiểm dừng | giây |
| $T_{\text{round}}$; $T_{\text{setup}}$; $T_{\text{job}}$ | thời gian một vòng; khởi tạo; cả công việc | giây |
| $b_{\text{eff}}$ | băng thông của đường nối dùng chung mà mọi byte của $Q$ đi qua | byte/giây |

Các quy ước đọc sau dùng trong cả chương.

- Véc-tơ là véc-tơ cột; chỉ số trên $t$ đếm số vòng đã chạy, nên $r^0$ là véc-tơ khởi tạo. Bất đẳng thức giữa hai véc-tơ, như $r\ge0$, đọc theo từng thành phần.
- Số thập phân dùng dấu phẩy, ví dụ $0{,}8$; số nguyên lớn viết dạng lũy thừa, ví dụ $10^9$.
- Tên trang trong ví dụ viết chữ đứng, như trang $\mathrm A$ và điểm $r_{\mathrm A}$, để không lẫn với chữ nghiêng của biến; thứ tự hàng và cột của ma trận là thứ tự tên trang.
- Mô hình byte: một điểm là số thực 8 byte; một mã trang hoặc một bậc ra là số nguyên 4 byte.
- MMDS viết ma trận liên kết là $M$, véc-tơ điểm là $v$ và phân phối đều là $e/n$; ở đây là $M_0$, $r$ và $u$. Trang chiếu MMDS và CS246 viết tổng phần điểm đi theo liên kết là $S$; ở đây là $s$, vì chữ $S$ dành cho dung lượng.
- Một số chữ của Bài 02 có nghĩa khác trong chương này:

| Chữ | Nghĩa ở Bài 02 | Nghĩa ở Bài 03 |
|---|---|---|
| $m$ | số tác vụ Map | số liên kết |
| $r$ | số tác vụ Reduce | véc-tơ điểm |
| $k$ | một khóa | số dải mỗi chiều; khóa viết là trang đích $i$ |
| $q$ | cấp của ma trận | số cặp sau Combine |
| $\tau$ | thời gian một phép cộng | ngưỡng dừng; thời gian một cạnh là $c_e$ |
| $B$ | băng thông | không dùng riêng; băng thông là $b_{\text{eff}}$, bộ nhớ là $B_{\text{task}}$ |
| $W_P$; $S_P$ | tổng số phép toán; mức tăng tốc | $W$ là tổng việc pha Map tính bằng giây; mức tăng tốc gọi bằng tên, không dùng chữ $S$ |

- Viết tắt nguồn: MMDS (*Mining of Massive Datasets*, ấn bản 3); "trang chiếu MMDS" chỉ bộ trang chiếu Chương 5 của các tác giả MMDS; CS246 chỉ bài giảng 09-pagerank của Stanford CS246; chi tiết ở mục tài liệu tham khảo.

<!-- note-topic-id: lec-03-topic-01 -->
## 1. Bài toán xếp hạng trang web

Bài 02 đã cho cách nhân một ma trận với một véc-tơ trên cụm máy: Map phát $(i,a_{ij}v_j)$ với khóa là chỉ số hàng, Reduce cộng các giá trị của mỗi khóa (Thuật toán 02.18), và Reduce được phép áp một hàm hoàn tất sau phép cộng mà Combine vẫn dùng được (Mệnh đề 02.15). Bài 02 cũng nêu ma trận cần nhân: ma trận của PageRank có phần tử ở hàng $i$, cột $j$ khác 0 khi và chỉ khi trang $j$ có liên kết tới trang $i$, và PageRank lặp phép nhân với ma trận đó (Bài 02, Mục 3.1; Tình huống 02.3). Để dùng Thuật toán 02.18, chúng ta còn cần giá trị của các phần tử ấy, lý do phải lặp và điều kiện để phép lặp có giới hạn.

Máy tìm kiếm thời kỳ đầu xếp hạng trang theo các từ của truy vấn có trong trang, theo số lần và vị trí xuất hiện của chúng. Cách xếp hạng này bị lừa dễ dàng: người bán áo có thể chép từ "movie" hàng nghìn lần vào trang của mình, tô cùng màu nền để người xem không thấy, và trang bán áo đứng đầu kết quả của truy vấn "movie". Cách gian lận này gọi là *thư rác theo từ* (term spam), theo MMDS (§5.1.1, tr.176).

Đếm số liên kết trỏ vào trang cũng không đủ, vì người bán áo có thể dựng một "trại thư rác" (spam farm) một triệu trang, mỗi trang trỏ vào trang bán áo (MMDS, hộp "Simplified PageRank Doesn't Work", tr.177). Điểm cần tìm phải dựa trên liên kết, nhưng liên kết từ các trang không ai trỏ tới phải có giá trị thấp.

Điểm như vậy được tính trên cả đồ thị web. Với $n=10^9$ trang (trang chiếu MMDS, tr.48), chỉ việc lưu ma trận dưới dạng đặc đã cần $8\cdot10^{18}$ byte, như ví dụ sau tính.

::: example Ví dụ 03.1 (Ma trận đặc của một tỷ trang)
**Dữ kiện.** Đồ thị có $n=10^9$ trang. Ma trận $n\times n$ có phần tử ở hàng $i$, cột $j$ khác 0 khi trang $j$ trỏ tới trang $i$; theo mô hình byte của chương, mỗi ô là một số thực 8 byte.

**Tính.** Ma trận có $n^2=10^{18}$ ô, nên lưu dạng đặc cần
$$
8\cdot10^{18}\ \text{byte}=8\ \text{EB}.
$$

**Kiểm tra lại.** Đếm theo cột: $n=10^9$ cột, mỗi cột $10^9$ ô và $8\cdot10^9$ byte, tổng $10^9\cdot8\cdot10^9=8\cdot10^{18}$ byte.
:::

Bài toán xếp hạng vì vậy đặt ra ba câu hỏi:

- quy tắc nào biến cấu trúc liên kết thành điểm;
- phép lặp của quy tắc đó có cho một điểm duy nhất trên mọi đồ thị không;
- mỗi vòng lặp được tính thế nào khi ma trận không lưu được dưới dạng đặc.

![Sơ đồ đọc từ trên xuống. Khối trên cùng là bài toán trung tâm: xếp hạng 10⁹ trang theo cấu trúc liên kết, ma trận đặc cần 8 · 10¹⁸ byte. Sáu mũi tên xuống sáu cột; mỗi cột ghi câu hỏi của phần đó và, dưới đường kẻ đứt, các khái niệm chính. Mục 1: điểm của một trang lấy từ liên kết thế nào; đồ thị web, bậc ra, chia điểm theo liên kết ra. Mục 2: phép lặp có hội tụ tới một điểm duy nhất không; ma trận liên kết, nút cụt, bẫy, bước nhảy, tính co. Mục 3: tính một vòng thế nào khi ma trận không vừa một máy; danh sách liên kết ra, khối, MapReduce. Mục 4: một vòng tốn bao nhiêu; dung lượng, bộ nhớ, dữ liệu, thời gian. Cột đọc thêm, viền nét đứt: xử lý nút cụt bằng cách xóa chúng; loại nút cụt đệ quy, khôi phục điểm. Mục 5: chương trình có cho đúng số tính tay không; pagerank.py, ba lớp kiểm.](img/lec-03/note-cau-truc-chuong-03.svg)

Sơ đồ đọc từ trên xuống. Khối trên cùng ghi bài toán trung tâm với số liệu của Ví dụ 03.1. Sáu cột ứng với Mục 1–4, phần đọc thêm và Mục 5; mỗi cột ghi câu hỏi mà phần đó trả lời, và dưới đường kẻ đứt là các khái niệm dùng để trả lời. Cột đọc thêm có viền nét đứt vì các mục khác không dùng kết quả của nó.

### 1.1 Đồ thị web và bài toán xếp hạng

Một cách trực quan, một liên kết từ trang $j$ tới trang $i$ là một phiếu bầu của $j$ cho $i$: tác giả trang $j$ cho rằng trang $i$ đáng đọc (trang chiếu MMDS, tr.16–17).

MMDS nêu hai động cơ của cách nhìn này (§5.1.1, tr.177). Người dùng web "bầu bằng chân" (vote with their feet): họ đặt liên kết tới các trang họ cho là tốt. Hành vi của một người đi ngẫu nhiên theo liên kết cho biết trang nào hay được ghé thăm. Để biến ý tưởng này thành bài toán, trước hết cần đặc tả đầu vào và đầu ra.

::: definition Định nghĩa 03.1 (Đồ thị web, bậc ra và bài toán xếp hạng)
**Đồ thị web.** Đồ thị có hướng hữu hạn $G=(V,E)$ có $n=\lvert V\rvert\ge1$ nút, mỗi nút là một trang, và $m=\lvert E\rvert$ cạnh. Cạnh $j\to i$ thuộc $E$ khi trang $j$ có ít nhất một liên kết tới trang $i$; nhiều liên kết từ $j$ tới $i$ gộp thành một cạnh. Cạnh $j\to j$, gọi là khuyên (self-loop), được phép.

**Bậc ra.** Bậc ra (out-degree) của trang $j$ là $d_j=\lvert\{i:j\to i\}\rvert$, số trang mà $j$ trỏ tới.

**Bài toán xếp hạng.** Đầu vào là $G$. Đầu ra là một véc-tơ điểm $r\in\mathbb R^n$ với $r_i\ge0$ cho mọi $i$ và $\sum_{i\in V}r_i=1$, cùng thứ tự các trang theo điểm giảm dần; hai trang cùng điểm thì đồng hạng.
:::

Hai điều kiện của đầu ra cho phép đọc điểm như một phân phối xác suất trên các trang. Nhiều véc-tơ thỏa hai điều kiện này, chẳng hạn véc-tơ có mọi thành phần bằng $1/n$, nên quy tắc tính điểm phải được chọn thêm. Điểm ở đây chỉ phụ thuộc đồ thị, không phụ thuộc truy vấn: máy tìm kiếm chỉ xét các trang chứa từ của truy vấn, và PageRank là một thành phần trong điểm của các trang đó, bên cạnh các thuộc tính khác như vị trí xuất hiện của từ (MMDS, §5.1.6, tr.187).

::: example Ví dụ 03.2 (Bốn trang web và bậc ra)
**Dữ kiện.** Đồ thị của MMDS Hình 5.1 (tr.178) có $n=4$ trang và các cạnh:

- $\mathrm A\to\mathrm B$, $\mathrm A\to\mathrm C$, $\mathrm A\to\mathrm D$;
- $\mathrm B\to\mathrm A$, $\mathrm B\to\mathrm D$;
- $\mathrm C\to\mathrm A$;
- $\mathrm D\to\mathrm B$, $\mathrm D\to\mathrm C$.

**Bậc ra.** $d_{\mathrm A}=3$, $d_{\mathrm B}=2$, $d_{\mathrm C}=1$, $d_{\mathrm D}=2$.

**Kiểm tra lại.** $m=3+2+1+2=8$: tổng bậc ra bằng số cạnh, vì mỗi cạnh có đúng một nguồn.
:::

![Đồ thị bốn trang: A và B ở hàng trên, C và D ở hàng dưới; tám mũi tên có hướng: A tới B, C, D; B tới A và D; C tới A; D tới B và C.](img/lec-03/graph-pages.svg)

Đồ thị này là ví dụ xuyên suốt của chương. Mọi trang đều có liên kết ra, và từ mỗi trang đi theo các mũi tên tới được mọi trang khác.

Quy tắc chấm điểm đơn giản nhất là đếm liên kết vào. Ví dụ sau thử quy tắc đó trên bốn trang.

::: example Ví dụ 03.3 (Đếm liên kết vào)
**Dữ kiện.** Đồ thị của Ví dụ 03.2.

**Đếm.** A nhận liên kết từ B, C; B từ A, D; C từ A, D; D từ A, B. Mỗi trang có 2 liên kết vào.

**Chuẩn hóa.** Chia cho tổng $8$: mỗi trang được $2/8=1/4$, và bốn trang đồng hạng.

**Kiểm tra lại.** $4\cdot1/4=1$.
:::

![Cùng đồ thị bốn trang; hai cạnh vào A, từ B và từ C, được vẽ đậm, các cạnh còn lại nhạt; ghi chú A nhận 2 liên kết vào.](img/lec-03/graph-inlinks.svg)

Hình đánh dấu hai liên kết vào A. Đếm như vậy coi hai liên kết ngang giá, dù C chỉ trỏ tới một trang là A, còn A chia sự chú ý cho ba trang. Đếm liên kết vào cũng không phân biệt liên kết từ một trang quan trọng với liên kết từ một trang trong trại thư rác. Quy tắc cần tìm phải tính tới bậc ra của nguồn và điểm của nguồn.

<!-- note-topic-id: lec-03-topic-02 -->
### 1.2 Chia điểm theo liên kết ra

Về mặt ý tưởng, mỗi trang có một lượng điểm và chia đều lượng đó cho các trang nó trỏ tới; điểm mới của một trang là tổng các phần nó nhận được. Trang có bậc ra nhỏ gửi phần lớn hơn qua mỗi liên kết, và trang có điểm cao gửi nhiều hơn trang có điểm thấp. Để làm rõ quy tắc này, xem ví dụ sau.

::: example Ví dụ 03.4 (Một vòng chia điểm trên bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2, bậc ra $d=(3,2,1,2)$; mỗi trang bắt đầu với điểm $1/4$.

**Chia tại nguồn.**

- A chia $1/4$ cho ba đích: mỗi đích B, C, D nhận $1/12$.
- B chia cho hai đích: A và D mỗi trang nhận $1/8$.
- C chuyển cả $1/4$ cho A.
- D chia cho hai đích: B và C mỗi trang nhận $1/8$.

**Cộng tại đích.**

- A nhận từ B và C: $1/8+1/4=3/8$.
- B nhận từ A và D: $1/12+1/8=5/24$.
- C nhận từ A và D: $1/12+1/8=5/24$.
- D nhận từ A và B: $1/12+1/8=5/24$.

**Kết quả.** Điểm mới là $(3/8,5/24,5/24,5/24)$: A đứng đầu, B, C, D đồng hạng.

**Kiểm tra lại.** $3/8+3\cdot5/24=9/24+15/24=1$: phép chia không làm mất hay sinh thêm điểm.
:::

![Trang A bên trái với điểm cũ 1/4 gửi ba mũi tên tới B, C, D bên phải, mỗi mũi tên mang 1/12, tức một phần ba của 1/4.](img/lec-03/graph-distribute.svg)

![Hai mũi tên từ B và C vào A; B đóng góp 1/8 vì 1/4 chia 2, C đóng góp 1/4 vì 1/4 chia 1; điểm mới của A là 3/8.](img/lec-03/graph-receive.svg)

Hình thứ nhất là bước chia tại nguồn A; hình thứ hai là bước cộng tại đích A. Mỗi mũi tên mang điểm của nguồn chia cho bậc ra của nguồn, nên liên kết từ C nặng gấp đôi liên kết từ B. Định nghĩa sau viết hai bước này cho mọi đồ thị mà mọi trang có liên kết ra.

::: definition Định nghĩa 03.2 (Một vòng chia điểm đồng bộ)
Cho đồ thị web $G$ với $d_j>0$ cho mọi trang $j$, và véc-tơ điểm $r\in\mathbb R^n$. **Một vòng chia điểm** tạo véc-tơ $z\in\mathbb R^n$ với
$$
z_i=\sum_{j:\,j\to i}\frac{r_j}{d_j},\qquad i\in V.
$$
Vòng chia điểm là **đồng bộ**: mọi thành phần $z_i$ được tính từ cùng một véc-tơ $r$, và $r$ không đổi trong khi tính.
:::

Mỗi số hạng $r_j/d_j$ là phần mà nguồn $j$ gửi qua một liên kết; nó phụ thuộc bậc ra của nguồn, không phụ thuộc bậc vào của đích $i$. Tổng chạy trên các nguồn trỏ tới $i$, nên một trang không có liên kết vào nhận $z_i=0$.

Điều kiện $d_j>0$ cần cho phép chia. Ví dụ 03.4 là một vòng với $r=(1/4,1/4,1/4,1/4)$: $z_{\mathrm A}=r_{\mathrm B}/d_{\mathrm B}+r_{\mathrm C}/d_{\mathrm C}=1/8+1/4=3/8$, điểm mới của A.

Hai cách hiểu sai thường gặp đều làm sai con số.

- Chia theo bậc vào của đích: A có bậc vào 2, nên phần C gửi cho A thành $1/4\cdot1/2=1/8$ thay cho $1/4$, và $z_{\mathrm A}=1/4$ thay cho $3/8$. Mọi trang ở đây có bậc vào 2, nên cả bốn trang nhận $1/4$, đúng kết quả đếm liên kết vào của Ví dụ 03.3.
- Dùng điểm mới trong cùng vòng: tính lần lượt A, B, C, D và dùng ngay mỗi điểm vừa tính. A vẫn nhận $3/8$, nhưng B nhận $(3/8)/3+1/8=1/4$ thay cho $5/24$; C và D cũng nhận $1/4$, và tổng bốn điểm là $3/8+3/4=9/8$.

Quy tắc một vòng (Định nghĩa 03.2) tách A khỏi ba trang còn lại, điều mà đếm liên kết vào không làm được. Tuy nhiên, điểm sau một vòng chỉ dùng điểm khởi tạo đều của các nguồn, trong khi điểm của một trang phải phụ thuộc điểm của các nguồn trỏ tới nó; vòng chia điểm vì vậy phải được lặp. Định nghĩa 03.2 cũng không áp dụng được cho trang có $d_j=0$. Trong Mục 2, chúng ta viết vòng chia điểm thành phép nhân ma trận, lặp nó, sửa các chỗ phép lặp hỏng và chứng minh phép lặp đã sửa hội tụ.

<!-- note-topic-id: lec-03-topic-03 -->
## 2. Mô hình và thuật toán PageRank

Web thật có trang không có liên kết ra và có nhóm trang không trỏ ra ngoài nhóm (MMDS, §5.1.3, tr.182). Chúng ta cần biết khi nào phép lặp có giới hạn, giới hạn có duy nhất không, và phải sửa mô hình thế nào để có hai tính chất này trên mọi đồ thị.

### 2.1 Ma trận liên kết và phép lặp thô

Một cách trực quan, xét một *người lướt ngẫu nhiên* (random surfer): ở mỗi bước, người đó đứng ở một trang và chọn đều một trong các liên kết ra để đi tiếp (MMDS, §5.1.2, tr.178; trang chiếu MMDS, tr.31–32). Nếu ở bước $t$ người đó đứng ở trang $j$ với xác suất $r^t_j$, thì ở bước sau người đó tới trang $i$ qua liên kết $j\to i$ với xác suất $r^t_j/d_j$. Đó đúng là số hạng của Định nghĩa 03.2, nên một vòng chia điểm biến phân phối vị trí của người lướt ở bước $t$ thành phân phối ở bước $t+1$.

![Trang j bên trái mang điểm cũ r_j; ba mũi tên tới ba trang đích bên phải, mỗi mũi tên mang r_j/d_j; nhãn bước t tới t + 1.](img/lec-03/model-one-round.svg)

Hình cho thấy một nguồn $j$ gửi cùng một phần $r_j/d_j$ qua mỗi liên kết ra. Các phần này là hệ số của một ma trận, xếp theo cột nguồn.

::: definition Định nghĩa 03.3 (Ma trận liên kết)
Cho đồ thị web $G$ với các trang đánh số $1,\ldots,n$. **Ma trận liên kết** (transition matrix) $M_0\in\mathbb R^{n\times n}$ có phần tử ở hàng $i$, cột $j$
$$
(M_0)_{ij}=\begin{cases}1/d_j&\text{nếu }j\to i,\\0&\text{nếu không.}\end{cases}
$$
:::

Cột $j$ mô tả trang nguồn $j$: các phần tử khác 0 của cột nằm ở hàng của các đích và đều bằng $1/d_j$, nên một cột có $d_j>0$ có tổng 1. Một trang có $d_j=0$ không có cạnh $j\to i$ nào, nên cột của nó toàn 0; định nghĩa không chia cho 0. Hàng $i$ mô tả trang đích $i$: phần tử khác 0 của hàng $i$ nằm ở cột các nguồn trỏ tới $i$. Lỗi thường gặp khi lập ma trận từ hình là ghi các cạnh *vào* trang A ở cột A; theo định nghĩa, chúng nằm ở hàng A.

::: example Ví dụ 03.5 (Ma trận liên kết của bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2: $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$; $d=(3,2,1,2)$. Hàng và cột theo thứ tự A, B, C, D.

**Lập theo cột.** Cột A có $1/3$ ở hàng B, C, D; cột B có $1/2$ ở hàng A, D; cột C có $1$ ở hàng A; cột D có $1/2$ ở hàng B, C:
$$
M_0=\begin{pmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{pmatrix}.
$$

**Kiểm tra lại.** Mỗi cột có tổng 1; hàng A có hai phần tử khác 0, ở cột B và cột C, đúng hai liên kết vào A. Đây là ma trận của MMDS Ví dụ 5.1 (tr.178).
:::

![Bên trái, A trỏ tới B, C, D; đường nét đứt nối mỗi đích với hàng tương ứng của cột A, nơi ghi 1/3; hàng A của cột A ghi 0 vì A không trỏ tới chính nó.](img/lec-03/visual-column-a.svg)

Hình đọc cột A từ ba cạnh ra của A: mỗi cạnh $\mathrm A\to x$ đặt $1/3$ vào hàng $x$. Mệnh đề sau nói phép nhân với $M_0$ là vòng chia điểm.

::: proposition Mệnh đề 03.4 (Một vòng chia điểm là phép nhân với ma trận liên kết)
**Giả thiết.** $G$ là đồ thị web, $M_0$ là ma trận liên kết của nó và $r\in\mathbb R^n$.

**Kết luận.**

- (a) Với mọi trang $i$, $(M_0r)_i=\sum_{j:\,j\to i}r_j/d_j$; khi mọi $d_j>0$, $M_0r$ là véc-tơ $z$ của Định nghĩa 03.2.
- (b) Nếu mọi $d_j>0$ và $r$ là một phân phối thì $M_0r$ là một phân phối.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Phần (b) cần mọi trang có liên kết ra.
:::

::: proof
**Bước 1 (thành phần $i$).** Theo định nghĩa tích ma trận–véc-tơ, $(M_0r)_i=\sum_{j=1}^n(M_0)_{ij}r_j$. Theo Định nghĩa 03.3, số hạng thứ $j$ bằng $r_j/d_j$ khi $j\to i$ và bằng 0 khi không, nên tổng chỉ còn các nguồn trỏ tới $i$. Đó là (a).

**Bước 2 (không âm).** Mọi phần tử của $M_0$ không âm, $r\ge0$, nên mọi thành phần của $M_0r$ không âm.

**Bước 3 (tổng bằng 1).** Ta có
$$
\begin{aligned}
&\sum_{i=1}^n(M_0r)_i\\
&\quad=\sum_{j=1}^n r_j\sum_{i=1}^n(M_0)_{ij}\\
&\quad=\sum_{j=1}^n r_j=1 .
\end{aligned}
$$
Dòng thứ hai đổi thứ tự hai tổng; dòng thứ ba dùng tổng mỗi cột bằng 1, vì $d_j>0$, rồi tổng các $r_j$ bằng 1, vì $r$ là phân phối. Bước 2 và Bước 3 cho (b). $\square$
:::

Phần (a) nối Định nghĩa 03.2 với Định nghĩa 02.17 của Bài 02: một vòng chia điểm là bài toán nhân ma trận–véc-tơ với $A=M_0$ và $v=r$, và khóa hàng của Thuật toán 02.18 là trang đích. Phần (b) là cách đọc xác suất: nếu $r_j$ là xác suất người lướt ở trang $j$ thì $(M_0r)_i$ là xác suất người đó ở trang $i$ sau một bước (MMDS, §5.1.2, tr.179). Điều kiện $d_j>0$ không bỏ được: với một cột toàn 0, Bước 3 mất số hạng $r_j$ của cột đó.

Lặp phép nhân này cho phân phối của người lướt sau nhiều bước. Nếu dãy đó dừng ở một véc-tơ, véc-tơ đó không đổi khi nhân thêm với $M_0$.

::: definition Định nghĩa 03.5 (Phép lặp thô và điểm cố định)
Cho ma trận vuông $A\in\mathbb R^{n\times n}$. **Phép lặp lũy thừa** (power iteration) với $A$ là dãy $r^{t+1}=Ar^t$, $t=0,1,2,\ldots$, từ một véc-tơ $r^0$ cho trước.

Cho ma trận liên kết $M_0$ của đồ thị web $G$. **Phép lặp thô** là phép lặp lũy thừa với $A=M_0$ bắt đầu từ $r^0=u$, với $u_i=1/n$ cho mọi $i$:
$$
r^{t+1}=M_0r^t,\qquad t=0,1,2,\ldots
$$
Một **điểm cố định** của $M_0$ là một phân phối $r^*$ thỏa $r^*=M_0r^*$.
:::

Điểm cố định là véc-tơ riêng của $M_0$ ứng với trị riêng 1, chuẩn hóa để tổng bằng 1 (MMDS, §5.1.2, tr.179). Nếu $r^*=M_0r^*$ thì $cr^*$ cũng thỏa phương trình với mọi hằng số $c$, nên chính điều kiện tổng bằng 1 chọn ra một nghiệm (MMDS, hộp "Solving Linear Equations", tr.180). Với bốn trang, giải hệ bằng phép khử Gauss là đủ; với hàng tỷ trang, phép khử Gauss tốn thời gian bậc ba theo số phương trình, nên MMDS tính điểm cố định bằng phép lặp, mỗi vòng là một phép nhân ma trận thưa với véc-tơ (cùng hộp, tr.180).

::: example Ví dụ 03.6 (Lặp thô trên bốn trang)
**Dữ kiện.** $M_0$ của Ví dụ 03.5; $r^0=(1/4,1/4,1/4,1/4)$.

**Ba vòng đầu.** Theo Mệnh đề 03.4(a), $r^{t+1}_{\mathrm A}=r^t_{\mathrm B}/2+r^t_{\mathrm C}$, $r^{t+1}_{\mathrm B}=r^{t+1}_{\mathrm C}=r^t_{\mathrm A}/3+r^t_{\mathrm D}/2$ và $r^{t+1}_{\mathrm D}=r^t_{\mathrm A}/3+r^t_{\mathrm B}/2$:

- $r^1=(9/24,\,5/24,\,5/24,\,5/24)$, tức $(3/8,5/24,5/24,5/24)$ của Ví dụ 03.4;
- $r^2=(15/48,\,11/48,\,11/48,\,11/48)$;
- $r^3=(11/32,\,7/32,\,7/32,\,7/32)$.

**Điểm cố định.** Giải hệ $r=M_0r$ với điều kiện tổng bằng 1. Hàng B và hàng C của $M_0$ trùng nhau, nên $r_{\mathrm B}=r_{\mathrm C}$. Trừ phương trình hàng D khỏi phương trình hàng B: $r_{\mathrm B}-r_{\mathrm D}=\tfrac12(r_{\mathrm D}-r_{\mathrm B})$, nên $r_{\mathrm D}=r_{\mathrm B}$. Hàng A cho $r_{\mathrm A}=r_{\mathrm B}/2+r_{\mathrm C}=\tfrac32r_{\mathrm B}$, và điều kiện tổng $\tfrac32r_{\mathrm B}+3r_{\mathrm B}=1$ cho $r_{\mathrm B}=2/9$:
$$
r^*=(1/3,\,2/9,\,2/9,\,2/9).
$$
MMDS (Ví dụ 5.2, tr.179–180) cho cùng ba vòng đầu và cho biết dãy hội tụ tới $r^*$.

**Kiểm tra lại.** Hàng B: $r^*_{\mathrm A}/3+r^*_{\mathrm D}/2=1/9+1/9=2/9$; tổng $1/3+3\cdot2/9=1$.
:::

B, C, D có cùng điểm dù bậc ra khác nhau: $d_{\mathrm C}=1$, còn $d_{\mathrm B}=d_{\mathrm D}=2$. Điểm đo lượng nhận được từ các nguồn, không đo số liên kết ra. A nhận điểm từ C, trang chuyển toàn bộ điểm của mình cho A, nên A đứng đầu. Ba vòng đầu cũng cho B, C, D cùng điểm; bài tập sau chứng minh điều đó đúng ở mọi vòng.

::: exercise Bài tập 03.1 (Ba thành phần bằng nhau qua phép lặp; MMDS Bài 5.1.5, §5.1.7, tr.188)
Cho $M_0$ là ma trận liên kết của Ví dụ 03.5 (MMDS Ví dụ 5.1), hàng và cột theo thứ tự A, B, C, D. Chứng minh bằng quy nạp theo $t$: nếu véc-tơ $v\in\mathbb R^4$ có thành phần thứ hai, thứ ba và thứ tư bằng nhau thì $M_0^tv$ cũng có ba thành phần đó bằng nhau, với mọi $t\ge0$.
:::

::: hint
Viết $v=(v_1,x,x,x)$ và tính ba thành phần B, C, D của $M_0v$ theo hàng B, C, D của $M_0$.
:::

::: solution
**Bước cơ sở.** Với $t=0$, $M_0^0v=v$ có ba thành phần cuối bằng nhau theo giả thiết.

**Một bước nhân.** Cho $w=(w_1,x,x,x)$. Hàng B và hàng C của $M_0$ cùng là $(1/3,0,0,1/2)$, hàng D là $(1/3,1/2,0,0)$, nên
$$
\begin{aligned}
(M_0w)_{\mathrm B}&=\tfrac13w_1+\tfrac12x,\\
(M_0w)_{\mathrm C}&=\tfrac13w_1+\tfrac12x,\\
(M_0w)_{\mathrm D}&=\tfrac13w_1+\tfrac12x .
\end{aligned}
$$
Ba thành phần cuối của $M_0w$ bằng nhau.

**Bước quy nạp.** Giả sử $M_0^tv$ có ba thành phần cuối bằng nhau. Áp phép tính trên với $w=M_0^tv$ cho $M_0^{t+1}v=M_0(M_0^tv)$ có ba thành phần cuối bằng nhau. Theo nguyên lý quy nạp, kết luận đúng với mọi $t\ge0$.

**Kiểm tra lại.** Với $v=r^0=u$, ba vòng của Ví dụ 03.6 có B, C, D bằng $5/24$, $11/48$, $7/32$. Với $w$ bất kỳ, $(M_0w)_{\mathrm B}=(M_0w)_{\mathrm C}$ vì hai hàng trùng nhau, còn $(M_0w)_{\mathrm B}-(M_0w)_{\mathrm D}=(w_4-w_2)/2$; một bước nhân chỉ cần $w_2=w_4$.
:::

<!-- note-topic-id: lec-03-topic-04 -->
### 2.2 Nút cụt và bẫy liên kết

Đồ thị bốn trang có hai tính chất mà web thật không có: mọi trang có liên kết ra, và từ mọi trang đi tới được mọi trang. Một khảo sát đầu tiên về cấu trúc web (MMDS, §5.1.3, tr.181–182) cho thấy đồ thị web có dạng *nơ thắt* (bowtie) gồm các phần sau:

- một *thành phần liên thông mạnh* (strongly connected component, SCC) lớn, trong đó từ mỗi trang đi tới được mọi trang khác;
- *thành phần vào* (in-component): các trang đi tới được SCC nhưng không đi tới được từ SCC;
- *thành phần ra* (out-component): các trang đi tới được từ SCC nhưng không quay lại được SCC;
- *tua* (tendrils): trang đi tới được từ thành phần vào mà không tới được thành phần vào, và trang tới được thành phần ra mà không đi tới được từ thành phần ra;
- *ống* (tubes): trang đi tới được từ thành phần vào và đi tới được thành phần ra nhưng không liên hệ với SCC;
- *thành phần rời* (isolated components): các trang không nối với ba thành phần lớn.

![Sơ đồ nơ thắt của web. Ở giữa là thành phần liên thông mạnh. Bên trái là thành phần vào, có mũi tên sang thành phần liên thông mạnh; bên phải là thành phần ra, có mũi tên từ thành phần liên thông mạnh sang. Phía trên, các tua ra khỏi thành phần vào và các tua đi vào thành phần ra. Phía dưới, một ống nối thẳng thành phần vào với thành phần ra, không qua thành phần liên thông mạnh. Góc phải dưới là các thành phần rời, không có mũi tên nối.](img/lec-03/note-no-that-web.svg)

Theo chiều mũi tên của hình, người lướt đi từ thành phần vào sang SCC rồi sang thành phần ra, và không có mũi tên nào quay lại. Một người lướt đã vào thành phần ra thì không bao giờ rời đi, nên sau nhiều bước các trang của SCC và thành phần vào có xác suất bằng 0 (MMDS, §5.1.3, tr.182). MMDS tách hiện tượng này thành hai trở ngại: trang không có liên kết ra và nhóm trang không trỏ ra ngoài.

::: definition Định nghĩa 03.6 (Nút cụt và ma trận dưới ngẫu nhiên)
Một **nút cụt** (dead end) là một trang $j$ có $d_j=0$. Tập nút cụt của $G$ là $\mathcal D=\{j\in V:d_j=0\}$, và $n_+=n-\lvert\mathcal D\rvert$ là số trang không cụt.

Một ma trận không âm có tổng mỗi cột không vượt quá 1 gọi là **dưới ngẫu nhiên** (substochastic); khi mọi cột có tổng đúng 1, ma trận gọi là **ngẫu nhiên theo cột** (column stochastic).
:::

Theo Định nghĩa 03.3, cột $j$ của $M_0$ có tổng 1 khi $d_j>0$ và tổng 0 khi $j\in\mathcal D$. Vậy $M_0$ luôn dưới ngẫu nhiên, và ngẫu nhiên theo cột khi và chỉ khi $\mathcal D=\varnothing$. Bước 3 của chứng minh Mệnh đề 03.4 cho tổng điểm sau một vòng thô là $\sum_{j\notin\mathcal D}r_j$: điểm ở các nút cụt mất đi. Để làm rõ hậu quả, xem ví dụ sau.

::: example Ví dụ 03.7 (Nút cụt C trên bốn trang)
**Dữ kiện.** Đồ thị của MMDS Hình 5.3 (tr.183): đồ thị bốn trang của Ví dụ 03.2 bỏ cạnh $\mathrm C\to\mathrm A$, nên $d=(3,2,0,2)$ và $\mathcal D=\{\mathrm C\}$. Cột C của $M_0$ toàn 0, ba cột còn lại như Ví dụ 03.5; $r^0=u$.

**Lặp thô.** $r^{t+1}_{\mathrm A}=r^t_{\mathrm B}/2$, còn công thức của B, C, D như Ví dụ 03.6:

| Vòng $t$ | $r^t$ | $\sum_ir^t_i$ |
|---|---|---|
| 0 | $(1/4,1/4,1/4,1/4)$ | $1$ |
| 1 | $(1/8,5/24,5/24,5/24)$ | $3/4$ |
| 2 | $(5/48,7/48,7/48,7/48)$ | $13/24$ |
| 3 | $(7/96,31/288,31/288,31/288)$ | $19/48$ |

**Kết quả.** Mỗi vòng mất đúng phần điểm đang ở C: vòng 1 mất $r^0_{\mathrm C}=1/4$, vòng 2 mất $r^1_{\mathrm C}=5/24$. Dãy tiến về véc-tơ 0 (MMDS Ví dụ 5.3, tr.182–183).

**Kiểm tra lại.** $1-1/4=3/4$; $3/4-5/24=13/24$; $13/24-7/48=19/48$.
:::

![Đồ thị bốn trang đã xóa cạnh C tới A; C không còn mũi tên đi ra, tô màu nhạt, ghi không có liên kết ra.](img/lec-03/model-dead-end.svg)

Nút cụt làm điểm rò rỉ khỏi đồ thị. Trở ngại thứ hai giữ đủ tổng điểm nhưng dồn điểm vào một chỗ.

::: definition Định nghĩa 03.7 (Bẫy liên kết)
Một **bẫy liên kết** (spider trap) là một tập trang $T\subseteq V$ khác rỗng sao cho mọi trang của $T$ có liên kết ra và mọi liên kết ra từ một trang của $T$ đều tới một trang của $T$.
:::

Bẫy liên kết không chứa nút cụt, nên các cột của nó có tổng 1 và phép lặp thô không làm mất điểm. Nhưng người lướt đã vào $T$ thì không ra được, nên điểm dồn về $T$ (MMDS, §5.1.5, tr.185). Toàn bộ đồ thị $V$ của Ví dụ 03.2 cũng thỏa định nghĩa; định nghĩa có ích khi $T$ là một phần nhỏ của đồ thị.

::: example Ví dụ 03.8 (Bẫy một nút C trên bốn trang)
**Dữ kiện.** Đồ thị của MMDS Hình 5.6 (tr.186): đồ thị bốn trang thay cạnh $\mathrm C\to\mathrm A$ bằng khuyên $\mathrm C\to\mathrm C$, nên $d=(3,2,1,2)$ và $T=\{\mathrm C\}$ là một bẫy. $r^0=u$.

**Lặp thô.** $r^{t+1}_{\mathrm A}=r^t_{\mathrm B}/2$, $r^{t+1}_{\mathrm C}=r^t_{\mathrm A}/3+r^t_{\mathrm C}+r^t_{\mathrm D}/2$, còn B, D như Ví dụ 03.6:

| Vòng $t$ | $r^t$ |
|---|---|
| 1 | $(1/8,5/24,11/24,5/24)$ |
| 2 | $(5/48,7/48,29/48,7/48)$ |
| 3 | $(7/96,31/288,205/288,31/288)$ |

**Kết quả.** Điểm của C tăng qua mỗi vòng, và dãy tiến tới $(0,0,1,0)$: mọi điểm dồn về C (MMDS Ví dụ 5.5, tr.185–186).

**Kiểm tra lại.** Tổng mỗi vòng bằng 1, chẳng hạn $5/48+7/48+29/48+7/48=1$; khác Ví dụ 03.7, bẫy không làm mất điểm.
:::

![Đồ thị bốn trang trong đó cạnh C tới A được thay bằng khuyên từ C về chính C; nút C tô màu nhạt.](img/lec-03/model-spider-trap.svg)

Hai ví dụ cho hai hậu quả ngược nhau trên cùng bốn trang: nút cụt làm tổng điểm tiến về 0, bẫy dồn mọi điểm vào một trang. Trong cả hai trường hợp, giới hạn không cho thông tin về tầm quan trọng của A, B, D. Sửa dữ liệu bằng cách loại dần nút cụt khỏi đồ thị, như MMDS làm ở §5.1.4, không giải quyết được bẫy; vì vậy chúng ta đổi mô hình chuyển động của người lướt.

<!-- note-topic-id: lec-03-topic-05 -->
### 2.3 Bước nhảy và bù nút cụt

Về mặt ý tưởng, chúng ta cho người lướt thêm một lựa chọn. Ở mỗi bước, với xác suất $\beta$ người đó đi theo một liên kết ra chọn đều; với xác suất $1-\beta$ người đó *nhảy* tới một trang chọn đều trong $n$ trang, kể cả trang đang đứng. Giá trị $\beta$ thường chọn trong khoảng $0{,}8$ đến $0{,}9$ (MMDS, §5.1.5, tr.186).

MMDS gọi cách sửa này là *đánh thuế* (taxation): mỗi trang nộp phần $1-\beta$ điểm của mình để chia đều cho mọi trang (trang chiếu MMDS, tr.49). *Bước nhảy* (còn gọi là dịch chuyển, teleport) là tên của nhánh xác suất $1-\beta$; phân phối đều $u$ của nó gọi là *phân phối nhảy*, Bài 04 gọi là phân phối dịch chuyển.

Ở nút cụt không có liên kết để đi theo, nên chúng ta cho người lướt luôn nhảy đều, theo trang chiếu MMDS (tr.42) và CS246 (trang chiếu 45).

![Từ trang hiện tại có hai nhánh: nhánh xác suất β đi tới một đích liên kết, nhánh xác suất 1 − β đi tới một trang bất kỳ.](img/lec-03/model-teleport.svg)

![Điểm δ gom ở nút cụt được chia đều tới cả bốn trang A, B, C, D; mỗi trang nhận βδ/n; mũi tên nét đứt là phần chia của mô hình, không phải liên kết của đồ thị.](img/lec-03/model-dead-redistribute.svg)

Hình thứ nhất là lựa chọn ở một trang có liên kết ra; hình thứ hai là phần $\beta$ của các nút cụt, được chia đều cho cả $n$ trang qua các mũi tên nét đứt. Gộp hai nhánh, mỗi trang nhận ba phần: đóng góp qua liên kết, phần bù từ nút cụt và phần nhảy.

::: definition Định nghĩa 03.8 (Quy tắc cập nhật đầy đủ)
Cho đồ thị web $G$ với ma trận liên kết $M_0$, tập nút cụt $\mathcal D$, hằng số $0<\beta<1$ và $u_i=1/n$. Với $r\in\mathbb R^n$, đặt $\delta=\sum_{j\in\mathcal D}r_j$. **Ánh xạ cập nhật đầy đủ** $F:\mathbb R^n\to\mathbb R^n$ là
$$
\begin{aligned}
F(r)_i&=\beta\sum_{j:\,j\to i}\frac{r_j}{d_j}\\
&\quad+\frac{(1-\beta)+\beta\delta}{n}
\end{aligned}
$$
với mọi $i\in V$, dạng véc-tơ $F(r)=\beta M_0r+\big((1-\beta)+\beta\delta\big)u$. **PageRank lặp** bắt đầu từ $r^0=u$ và đặt $r^{t+1}=F(r^t)$; khi đó $\delta^t=\sum_{j\in\mathcal D}r^t_j$ là tổng điểm ở nút cụt sau $t$ vòng.
:::

$F(r)_i$ gồm ba số hạng:

- $\beta\sum_{j\to i}r_j/d_j$ là nhánh đi theo liên kết, bằng $\beta$ lần vòng chia điểm của Định nghĩa 03.2;
- $(1-\beta)/n$ là nhánh nhảy: mọi trang, kể cả nút cụt, nộp phần $1-\beta$, và tổng đó chia đều cho $n$ trang khi tổng điểm bằng 1;
- $\beta\delta/n$ là phần bù: phần $\beta$ của nút cụt không có liên kết để đi theo nên cũng chia đều.

Hai số hạng sau giống nhau ở mọi trang; ta gọi tổng của chúng là *phần chung* $((1-\beta)+\beta\delta)/n$. Lặp thô của Định nghĩa 03.5 là công thức trên với $\beta=1$ trên đồ thị không có nút cụt.

::: example Ví dụ 03.9 (Một vòng có bước nhảy trên bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2, không có nút cụt; $\beta=4/5$, $n=4$, $r^0=(1/4,1/4,1/4,1/4)$. Theo Ví dụ 03.4, $M_0r^0=(3/8,5/24,5/24,5/24)$.

**Phần chung.** $\delta^0=0$, nên phần chung là $(1-\beta)/n=(1/5)/4=1/20$.

**Từng trang.**

- A: $\tfrac45\cdot\tfrac38+\tfrac1{20}=\tfrac{3}{10}+\tfrac1{20}=\tfrac7{20}$.
- B, C, D: $\tfrac45\cdot\tfrac5{24}+\tfrac1{20}=\tfrac16+\tfrac1{20}=\tfrac{13}{60}$.

**Kiểm tra lại.** $7/20+3\cdot13/60=21/60+39/60=1$. So với $3/8$ của lặp thô, A giảm còn $7/20$: bước nhảy kéo các điểm về gần $1/4$.
:::

::: example Ví dụ 03.10 (Một vòng khi C là nút cụt)
**Dữ kiện.** Đồ thị của Ví dụ 03.7, $\mathcal D=\{\mathrm C\}$; $\beta=4/5$, $r^0=u$. Theo Ví dụ 03.7, $M_0r^0=(1/8,5/24,5/24,5/24)$.

**Phần chung.** $\delta^0=r^0_{\mathrm C}=1/4$; phần chung là $\big(\tfrac15+\tfrac45\cdot\tfrac14\big)/4=\tfrac25\cdot\tfrac14=\tfrac1{10}$.

**Từng trang.**

- A: $\tfrac45\cdot\tfrac18+\tfrac1{10}=\tfrac1{10}+\tfrac1{10}=\tfrac15$.
- B, C, D: $\tfrac45\cdot\tfrac5{24}+\tfrac1{10}=\tfrac16+\tfrac1{10}=\tfrac4{15}$.

**Kiểm tra lại.** $1/5+3\cdot4/15=1$: tổng vẫn bằng 1, khác tổng $3/4$ của vòng thô trong Ví dụ 03.7.
:::

Định nghĩa 03.8 viết phần bù riêng. MMDS và CS246 viết cùng quy tắc theo hai cách khác: thay cột nút cụt bằng $u$, hoặc tính phần rò rỉ rồi trả lại. Mệnh đề sau chứng minh ba cách là một.

::: proposition Mệnh đề 03.9 (Ba dạng của quy tắc cập nhật)
**Giả thiết.** $G$, $M_0$, $\mathcal D$, $\beta$, $u$ và $F$ như Định nghĩa 03.8; $\mathbf 1_{\mathcal D}\in\mathbb R^n$ có thành phần $j$ bằng 1 khi $j\in\mathcal D$ và bằng 0 khi không; $\bar M=M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$.

**Kết luận.**

- (a) $\bar M$ là $M_0$ với mỗi cột nút cụt thay bằng $u$; $\bar M$ ngẫu nhiên theo cột, và $F(r)=\beta\bar Mr+(1-\beta)u$ với mọi $r\in\mathbb R^n$.
- (b) Nếu $\sum_ir_i=1$, đặt $r'=\beta M_0r$ và $s=\sum_ir'_i$; khi đó $F(r)_i=r'_i+(1-s)/n$ với mọi $i$.
- (c) Nếu $\mathcal D=\varnothing$ thì $F(r)=\beta M_0r+(1-\beta)u$.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Dạng (b) cần tổng điểm bằng 1; dạng (a) và (c) đúng với mọi $r\in\mathbb R^n$.
:::

::: proof
**Bước 1 (dạng ma trận).** Phần tử $(i,j)$ của $u\,\mathbf 1_{\mathcal D}^{\mathsf T}$ là $u_i(\mathbf 1_{\mathcal D})_j$, bằng $1/n$ khi $j\in\mathcal D$ và 0 khi không. Cột nút cụt của $M_0$ toàn 0, nên cột đó của $\bar M$ là $u$; các cột khác giữ nguyên. Mỗi cột của $\bar M$ vì vậy không âm và có tổng 1: cột không cụt theo Định nghĩa 03.3, cột cụt vì $\sum_iu_i=1$. Với mọi $r$,
$$
\begin{aligned}
&\beta\bar Mr+(1-\beta)u\\
&\quad=\beta M_0r+\beta u\,(\mathbf 1_{\mathcal D}^{\mathsf T}r)\\
&\qquad+(1-\beta)u\\
&\quad=\beta M_0r+\big((1-\beta)+\beta\delta\big)u\\
&\quad=F(r).
\end{aligned}
$$
Dòng thứ hai dùng định nghĩa của $\bar M$, dòng thứ tư dùng $\mathbf 1_{\mathcal D}^{\mathsf T}r=\delta$, và dòng cuối là Định nghĩa 03.8.

**Bước 2 (phần rò rỉ).** Cột $j$ của $M_0$ có tổng 1 khi $j\notin\mathcal D$ và 0 khi $j\in\mathcal D$, nên đổi thứ tự tổng như Bước 3 của chứng minh Mệnh đề 03.4 cho
$$
\begin{aligned}
s&=\beta\sum_{j\notin\mathcal D}r_j=\beta\Big(\sum_jr_j-\delta\Big)\\
&=\beta(1-\delta),
\end{aligned}
$$
dấu bằng cuối dùng $\sum_jr_j=1$. Do đó $1-s=(1-\beta)+\beta\delta$, và $r'_i+(1-s)/n$ bằng $F(r)_i$ theo Định nghĩa 03.8.

**Bước 3 (không có nút cụt).** Khi $\mathcal D=\varnothing$, $\delta=0$ với mọi $r$, nên Định nghĩa 03.8 cho $F(r)=\beta M_0r+(1-\beta)u$. $\square$
:::

Dạng (a) là ma trận ngẫu nhiên theo cột của trang chiếu MMDS (tr.42) và CS246 (trang chiếu 45), nơi cột nút cụt được thay bằng cột $1/n$. Dạng (b) là thuật toán "trả lại phần điểm rò rỉ" của trang chiếu MMDS (tr.52) và CS246 (trang chiếu 54): tính $\beta M_0r$, đo tổng $s$, rồi cộng đều $(1-s)/n$. Dạng (c) là công thức đánh thuế $v'=\beta Mv+(1-\beta)e/n$ của MMDS (§5.1.5, tr.186), với $M=M_0$, $v=r$ và $e/n=u$. Ví dụ 03.10 là thể hiện của dạng (b): $s=\tfrac45\cdot\tfrac34=\tfrac35$ và $(1-s)/4=1/10$, đúng phần chung đã tính.

Bước nhảy sửa được bẫy của Ví dụ 03.8, như ví dụ sau cho thấy.

::: example Ví dụ 03.11 (Bẫy C có bước nhảy)
**Dữ kiện.** Đồ thị của Ví dụ 03.8, bẫy $\{\mathrm C\}$, không có nút cụt; $\beta=4/5$, $r^0=u$. Theo Mệnh đề 03.9(c), $F(r)=\tfrac45M_0r+\tfrac1{20}\mathbf 1$.

**Ba vòng đầu.**

| Vòng $t$ | $r^t$ |
|---|---|
| 1 | $(9/60,\,13/60,\,25/60,\,13/60)$ |
| 2 | $(41/300,\,53/300,\,153/300,\,53/300)$ |
| 3 | $(543/4500,\,707/4500,\,2543/4500,\,707/4500)$ |

Chẳng hạn, ở vòng 1, C nhận $\tfrac45\big(\tfrac1{12}+\tfrac14+\tfrac18\big)+\tfrac1{20}=\tfrac45\cdot\tfrac{11}{24}+\tfrac1{20}=\tfrac{11}{30}+\tfrac1{20}=\tfrac{25}{60}$.

**Giới hạn.** Dãy tiến tới
$$
r^*=\Big(\frac{15}{148},\,\frac{19}{148},\,\frac{95}{148},\,\frac{19}{148}\Big).
$$

**Kiểm tra lại.** Hàng C: $r^*_{\mathrm A}/3+r^*_{\mathrm C}+r^*_{\mathrm D}/2=\tfrac{10+190+19}{296}=\tfrac{219}{296}$, và $\tfrac45\cdot\tfrac{219}{296}+\tfrac1{20}=\tfrac{219}{370}+\tfrac1{20}=\tfrac{475}{740}=\tfrac{95}{148}$; tổng $(15+19+95+19)/148=1$.
:::

C vẫn giữ $95/148\approx0{,}64$ tổng điểm, hơn một nửa, nhưng mọi trang đều có điểm dương. Bước nhảy giới hạn tác dụng của bẫy nhưng không xóa nó.

Công thức đánh thuế của MMDS, dạng (c) của Mệnh đề 03.9, không có phần bù khi đồ thị có nút cụt. Khi đó, nếu $\sum_ir_i=1$, một vòng cho tổng $\beta(1-\delta)+(1-\beta)=1-\beta\delta$; trên biến thể C cụt với $\beta=4/5$ và $r^0=u$, một vòng không bù cho $(3/20,13/60,13/60,13/60)$, tổng $4/5$.

<!-- note-topic-id: lec-03-topic-06 -->
### 2.4 Thuật toán lặp và điều kiện dừng

Định nghĩa 03.8 cho một vòng; một chương trình còn phải chọn khi nào dừng. Điểm cố định chưa biết, nên chương trình không đo được sai số. Nó đo được độ thay đổi giữa hai vòng liên tiếp,
$$
\Delta_t=\lVert r^{t+1}-r^t\rVert_1=\sum_{i\in V}\lvert r^{t+1}_i-r^t_i\rvert,
$$
và dừng khi độ thay đổi không vượt một ngưỡng $\tau>0$ cho trước. Ví dụ 03.9 là vòng thứ nhất của thuật toán sau trên bốn trang.

::: algorithm Thuật toán 03.10 (PageRank lặp)
**Đầu vào.** Danh sách kề của $G$: với mỗi trang $j$, danh sách $\mathrm{out}[j]$ các đích của $j$, không có phần tử lặp, nên $d_j$ là độ dài của $\mathrm{out}[j]$; $n\ge1$; hằng số $0<\beta<1$; ngưỡng $\tau>0$; số vòng tối đa $K$ nguyên dương.

**Đầu ra.** Véc-tơ điểm $r$, số vòng $t_{\text{dừng}}$, độ thay đổi cuối $\Delta$ và trạng thái *đạt ngưỡng* hoặc *chưa đạt ngưỡng*.

**Giả thiết.** Mọi đích trong các danh sách là trang của $V$.

1. Đặt $r_i\leftarrow1/n$ cho mọi $i$ và $t\leftarrow0$.
2. Tính $\delta\leftarrow\sum_{j:\,d_j=0}r_j$.
3. Đặt $\mathrm{new}_i\leftarrow\big((1-\beta)+\beta\delta\big)/n$ cho mọi $i$.
4. Với mỗi trang $j$ có $d_j>0$ và mỗi $i\in\mathrm{out}[j]$: $\mathrm{new}_i\leftarrow\mathrm{new}_i+\beta r_j/d_j$.
5. Tính $\Delta\leftarrow\sum_i\lvert\mathrm{new}_i-r_i\rvert$; đặt $r\leftarrow\mathrm{new}$ và $t\leftarrow t+1$.
6. Nếu $\Delta\le\tau$: trả $(r,t,\Delta,\text{đạt ngưỡng})$. Nếu $t=K$: trả $(r,t,\Delta,\text{chưa đạt ngưỡng})$. Ngược lại, quay lại bước 2.

**Dừng.** Mỗi vòng tăng $t$ thêm 1, nên thuật toán dừng sau không quá $K$ vòng.

**Trường hợp biên.** Nếu mọi trang là nút cụt, kể cả khi $n=1$ và trang duy nhất không có liên kết, thì $\delta=1$ ở vòng đầu, phần chung bằng $1/n$, bước 4 không làm gì, nên $r^1=u=r^0$ và $\Delta=0$: thuật toán dừng sau một vòng với trạng thái đạt ngưỡng. Một khuyên $j\to j$ là một phần tử của $\mathrm{out}[j]$ như mọi cạnh khác. Một trang không có liên kết vào vẫn nhận phần chung ở bước 3.

**Chi phí.** Mô hình đếm số lần thực hiện thân vòng lặp, cho mỗi trang ở bước 2, 3, 5 và cho mỗi cạnh ở bước 4, trong một vòng:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2 (tổng nút cụt) | $n$ trang | 1 | $n$ |
| 3 (phần chung) | $n$ trang | 1 | $n$ |
| 4 (cộng đóng góp) | $m$ cạnh | 1 | $m$ |
| 5 (độ thay đổi, thay mảng) | $n$ trang | 1 | $n$ |

Mỗi vòng tốn $3n+m$ thao tác, tức $\Theta(n+m)$; bộ nhớ làm việc gồm hai mảng $r$ và $\mathrm{new}$, $16n$ byte theo mô hình 8 byte một điểm, cộng danh sách kề.
:::

```text
r[i] ← 1/n với mọi i
lặp t = 1, 2, ..., K:
    δ ← tổng r[j] trên các trang j có d[j] = 0
    với mọi i: new[i] ← ((1 − β) + β·δ) / n
    với mỗi j có d[j] > 0:
        với mỗi i trong out[j]:
            new[i] ← new[i] + β·r[j] / d[j]
    Δ ← tổng |new[i] − r[i]| trên mọi i
    r ← new
    nếu Δ ≤ τ: trả (r, t, Δ, đạt ngưỡng)
trả (r, K, Δ, chưa đạt ngưỡng)
```

Thao tác quyết định của thuật toán là ghi vào mảng mới $\mathrm{new}$ trong khi chỉ đọc mảng cũ $r$: mọi đóng góp của một vòng dùng cùng một véc-tơ, như Định nghĩa 03.2 yêu cầu. Bước 3 đặt phần chung trước khi cộng đóng góp, nên trang không có liên kết vào vẫn có điểm. Thuật toán để ngỏ cách chọn $\tau$ và $K$; Hệ quả 03.16 ở Mục 2.5 nối $\tau$ với sai số.

::: example Ví dụ 03.12 (Độ thay đổi hai vòng đầu trên bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2, $\beta=4/5$; theo Ví dụ 03.9, $r^0=(1/4,1/4,1/4,1/4)$ và $r^1=(7/20,13/60,13/60,13/60)$.

**Vòng hai.** $\delta^1=0$, phần chung $1/20$.

- A: $\tfrac45\big(\tfrac{13}{120}+\tfrac{13}{60}\big)+\tfrac1{20}=\tfrac45\cdot\tfrac{39}{120}+\tfrac1{20}=\tfrac{26}{100}+\tfrac5{100}=\tfrac{31}{100}$.
- B, C, D: $\tfrac45\big(\tfrac7{60}+\tfrac{13}{120}\big)+\tfrac1{20}=\tfrac45\cdot\tfrac{27}{120}+\tfrac1{20}=\tfrac{18}{100}+\tfrac5{100}=\tfrac{23}{100}$.

**Độ thay đổi.**

- $\Delta_0=\big\lvert\tfrac7{20}-\tfrac14\big\rvert+3\big\lvert\tfrac{13}{60}-\tfrac14\big\rvert=\tfrac1{10}+3\cdot\tfrac1{30}=\tfrac15$.
- $\Delta_1=\big\lvert\tfrac{31}{100}-\tfrac7{20}\big\rvert+3\big\lvert\tfrac{23}{100}-\tfrac{13}{60}\big\rvert=\tfrac1{25}+3\cdot\tfrac1{75}=\tfrac2{25}=0{,}08$.

**Quyết định dừng.** Với $\tau=0{,}1$: vòng một có $\Delta_0=0{,}2>\tau$, vòng hai có $\Delta_1=0{,}08\le\tau$, nên thuật toán trả $r^2=(31/100,23/100,23/100,23/100)$ sau $t_{\text{dừng}}=2$ vòng. Với $\tau=10^{-8}$, cả hai vòng chưa đạt ngưỡng và thuật toán chạy tiếp.

**Kiểm tra lại.** $31/100+3\cdot23/100=1$.
:::

Thuật toán đúng theo nghĩa sau: mỗi vòng tính đúng $F(r^t)$ của Định nghĩa 03.8, và trạng thái trả về đúng với điều kiện dừng.

::: proposition Mệnh đề 03.11 (Tính đúng của Thuật toán 03.10)
**Giả thiết.** Đầu vào thỏa các điều kiện của Thuật toán 03.10.

**Kết luận.**

- (a) Sau vòng thứ $t$, mảng $r$ bằng $r^t=F(r^{t-1})$ của Định nghĩa 03.8, với $r^0=u$.
- (b) Thuật toán dừng sau $t_{\text{dừng}}\le K$ vòng; nó trả trạng thái đạt ngưỡng khi và chỉ khi $\Delta_{t_{\text{dừng}}-1}\le\tau$, và khi đó $\Delta_t>\tau$ với mọi $t<t_{\text{dừng}}-1$.

**Điều kiện áp dụng.** Số học chính xác; bước 4 không ghi vào $r$.

**Phạm vi.** Mệnh đề nói thuật toán tính đúng dãy $r^t$; nó không nói $r^{t_{\text{dừng}}}$ gần $r^*$, điều Hệ quả 03.16 trả lời.
:::

::: proof
Chứng minh theo một vòng; vòng đầu dùng $r=r^0=u$ của bước 1.

**Bước 1 (khởi tạo bất biến).** Giả sử khi vào vòng, $r=r^{t}$. Bước 2 cho $\delta=\delta^t$ vì bước 2 chỉ đọc $r$. Xét các cạnh của bước 4 theo thứ tự thuật toán duyệt. Bất biến: sau khi xét một tập cạnh $E'\subseteq E$, với mọi $i$,
$$
\begin{aligned}
\mathrm{new}_i&=\frac{(1-\beta)+\beta\delta^t}{n}\\
&\quad+\beta\sum_{j:\,(j\to i)\in E'}\frac{r^t_j}{d_j}.
\end{aligned}
$$
Trước cạnh đầu tiên, $E'=\varnothing$ và bất biến đúng theo bước 3.

**Bước 2 (duy trì).** Xét thêm cạnh $j\to i$. Bước 4 chỉ cộng $\beta r_j/d_j$ vào $\mathrm{new}_i$, và $r_j=r^t_j$ vì không bước nào của vòng ghi vào $r$ trước bước 5. Vậy bất biến đúng với $E'\cup\{j\to i\}$; các thành phần khác của $\mathrm{new}$ không đổi.

**Bước 3 (kết thúc vòng).** Bước 4 duyệt mọi trang có $d_j>0$ và mọi đích của nó, tức mọi cạnh của $E$ đúng một lần, vì danh sách $\mathrm{out}[j]$ không có phần tử lặp. Khi $E'=E$, bất biến là Định nghĩa 03.8, nên $\mathrm{new}=F(r^t)=r^{t+1}$. Bước 5 tính $\Delta=\lVert r^{t+1}-r^t\rVert_1=\Delta_t$ trước khi thay $r$, rồi đặt $r=r^{t+1}$. Quy nạp theo số vòng cho (a).

**Bước 4 (dừng và trạng thái).** Sau vòng thứ $t$, giá trị $\Delta$ là $\Delta_{t-1}$. Bước 6 trả đạt ngưỡng ở vòng đầu tiên có $\Delta_{t-1}\le\tau$, nên mọi vòng trước đó có độ thay đổi lớn hơn $\tau$; nếu không vòng nào trong $K$ vòng đạt ngưỡng, bước 6 trả chưa đạt ngưỡng khi $t=K$. Đó là (b). $\square$
:::

Trên bốn trang với $\beta=4/5$ và $r^0=u$, bỏ một giả thiết của Mệnh đề 03.11 làm sai vòng đầu.

- Bỏ cập nhật đồng bộ, tức "bước 4 không ghi vào $r$": nếu các trang được tính lần lượt theo thứ tự A, B, C, D và mỗi trang dùng ngay điểm mới của các trang đã tính, vòng đầu cho $(7/20,73/300,73/300,361/1500)$ với tổng $404/375$, thay cho $(7/20,13/60,13/60,13/60)$.
- Bỏ "danh sách không có phần tử lặp": nếu danh sách của B ghi A hai lần, $[\mathrm A,\mathrm A,\mathrm D]$, thì $d_{\mathrm B}=3$, cột B thành $(2/3,0,0,1/3)^{\mathsf T}$, và vòng đầu cho $r^1_{\mathrm A}=23/60$, $r^1_{\mathrm D}=11/60$ thay cho $7/20$ và $13/60$.

Bước 2 của chứng minh dùng cập nhật đồng bộ; Bước 3 dùng danh sách không có phần tử lặp.

::: remark Nhận xét 03.12 (Trong thực hành: thuật toán lặp)
- Danh sách kề của thuật toán là từ điển `adj` của mã thực hành ở Mục 5; mọi trang phải là một khóa của từ điển, kể cả nút cụt (danh sách rỗng) và trang không có liên kết vào. Bỏ một nút cụt là đích của trang khác thì hàm `pagerank` báo lỗi `ValueError`, vì có một đích không phải khóa; bỏ một trang không có liên kết vào thì trang đó mất khỏi kết quả và $n$ trong phần chung bị sai.
- Số vòng phụ thuộc đồ thị và $\tau$. Với chính đồ thị Web, MMDS ghi rằng phép lặp lũy thừa cần 50–75 vòng để hội tụ tới sai số của số thực độ chính xác kép (§5.1.2, tr.179), và khoảng 50 phép nhân ma trận–véc-tơ cho một lần tính (§5.2, tr.189).
:::

<!-- note-topic-id: lec-03-topic-07 -->
### 2.5 Bảo toàn tổng điểm và hội tụ

Thuật toán 03.10 tính đúng dãy $r^t$, nhưng chưa có gì bảo đảm dãy đó là các phân phối, có giới hạn, hay dừng sau một số vòng nhỏ. Trên bốn trang, $\Delta_0=1/5$ và $\Delta_1=2/25$ giảm; trên đồ thị hai trang $\mathrm A\rightleftarrows\mathrm B$, phép lặp $r^{t+1}=M_0r^t$ từ $r^0=(1,0)$ cho $(0,1)$, $(1,0)$, $(0,1)$, … và không bao giờ dừng. Chúng ta chứng minh ba điều cho quy tắc đầy đủ: mỗi $r^t$ là một phân phối, dãy hội tụ tới một điểm cố định duy nhất với tốc độ $\beta^t$, và $\Delta_t$ chặn được sai số.

::: proposition Mệnh đề 03.13 (Bảo toàn tổng điểm)
**Giả thiết.** $F$ như Định nghĩa 03.8 với $0<\beta<1$; $r\in\mathbb R^n$ thỏa $r\ge0$ và $\sum_ir_i=1$.

**Kết luận.** $F(r)\ge0$ và $\sum_iF(r)_i=1$. Do đó mọi $r^t$ của PageRank lặp là một phân phối.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Mệnh đề không nói dãy $r^t$ hội tụ.
:::

::: proof
**Bước 1 (không âm).** Trong Định nghĩa 03.8, $\beta>0$, $1-\beta\ge0$, $r_j\ge0$ và $\delta\ge0$, nên mọi số hạng của $F(r)_i$ không âm.

**Bước 2 (ba phần của tổng).** Cộng $F(r)_i$ theo $i$. Phần đi theo liên kết cho $\beta\sum_{j\notin\mathcal D}r_j=\beta(1-\delta)$ theo Bước 2 của chứng minh Mệnh đề 03.9; phần chung được cộng $n$ lần, cho $(1-\beta)+\beta\delta$. Vậy
$$
\begin{aligned}
\sum_iF(r)_i&=\underbrace{\beta(1-\delta)}_{\text{theo liên kết}}+\underbrace{\beta\delta}_{\text{bù nút cụt}}\\
&\quad+\underbrace{(1-\beta)}_{\text{bước nhảy}}=1.
\end{aligned}
$$

**Bước 3 (mọi vòng).** $r^0=u$ là một phân phối; nếu $r^t$ là phân phối thì $r^{t+1}=F(r^t)$ là phân phối theo Bước 1 và Bước 2. Quy nạp theo $t$ cho kết luận. $\square$
:::

Trên biến thể C cụt của Ví dụ 03.10, với $\beta=4/5$ và $\delta^0=1/4$, ba phần là $\beta(1-\delta)=3/5$, $\beta\delta=1/5$ và $1-\beta=1/5$; bỏ phần bù thì tổng chỉ còn $4/5$ (Mục 2.3). Mệnh đề 03.13 là phép kiểm đầu tiên cho một chương trình PageRank: sau mỗi vòng, tổng điểm phải xấp xỉ 1 và không điểm nào âm.

Mệnh đề 03.13 cần cả hai giả thiết về $r$; trên bốn trang với $\beta=4/5$:

- Bỏ $r\ge0$: $r=(1/2,1/2,1/2,-1/2)$ có tổng 1, nhưng $F(r)=(13/20,-1/60,-1/60,23/60)$ có thành phần âm.
- Bỏ $\sum_ir_i=1$: $r=(1/2,1/2,1/2,1/2)$ cho $\sum_iF(r)_i=9/5$.

Bước 1 của chứng minh dùng $r\ge0$; Bước 2 dùng $\sum_ir_i=1$. Giả thiết $\beta<1$ không dùng ở đây; Định lý 03.15 cần nó.

Để so hai véc-tơ, ta dùng chuẩn $\lVert x\rVert_1=\sum_i\lvert x_i\rvert$, chuẩn mà $\Delta_t$ đã dùng. Bước 1 và Bước 2 của chứng minh hội tụ dựa vào bổ đề sau; theo Mệnh đề 03.9(a), $\bar M$ thỏa giả thiết của nó.

::: lemma Bổ đề 03.14 (Ma trận dưới ngẫu nhiên không làm tăng chuẩn $\ell_1$)
**Giả thiết.** $A\in\mathbb R^{n\times n}$ có mọi phần tử không âm và mọi cột có tổng không quá 1.

**Kết luận.** $\lVert Av\rVert_1\le\lVert v\rVert_1$ với mọi $v\in\mathbb R^n$; dấu bằng xảy ra khi mọi cột có tổng 1 và $v\ge0$.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Bổ đề không cho hệ số co nhỏ hơn 1.
:::

::: proof
$$
\begin{aligned}
\lVert Av\rVert_1&=\sum_{i=1}^n\Big\lvert\sum_{j=1}^nA_{ij}v_j\Big\rvert\\
&\le\sum_{i=1}^n\sum_{j=1}^nA_{ij}\lvert v_j\rvert\\
&=\sum_{j=1}^n\lvert v_j\rvert\sum_{i=1}^nA_{ij}\\
&\le\lVert v\rVert_1 .
\end{aligned}
$$
Dòng thứ nhất là định nghĩa chuẩn; dòng thứ hai dùng bất đẳng thức tam giác và $A_{ij}\ge0$; dòng thứ ba đổi thứ tự tổng; dòng cuối dùng tổng mỗi cột không quá 1. Khi $v\ge0$, mọi số hạng trong trị tuyệt đối không âm nên dấu bằng xảy ra ở dòng thứ hai; khi mọi cột có tổng 1, dấu bằng xảy ra ở dòng cuối. $\square$
:::

Hệ số co nhỏ hơn 1 đến từ $\beta$. Định lý sau cần Bổ đề 03.14, dạng (a) của Mệnh đề 03.9 và Mệnh đề 03.13.

::: theorem Định lý 03.15 (Hội tụ của PageRank đầy đủ)
**Giả thiết.** $G$ là đồ thị web hữu hạn với $n\ge1$; $0<\beta<1$; $F(r)=\beta\bar Mr+(1-\beta)u$ như Mệnh đề 03.9(a); $r^0$ là một phân phối và $r^{t+1}=F(r^t)$ với mọi $t\ge0$.

**Kết luận.**

- (a) $\lVert F(x)-F(y)\rVert_1\le\beta\lVert x-y\rVert_1$ với mọi $x,y\in\mathbb R^n$.
- (b) Có đúng một $r^*\in\mathbb R^n$ thỏa $r^*=F(r^*)$, và $r^*$ là một phân phối.
- (c) Với mọi $t\ge0$, $\lVert r^t-r^*\rVert_1\le\beta^t\lVert r^0-r^*\rVert_1\le2\beta^t$.

**Điều kiện áp dụng.** Số học chính xác; mỗi vòng là một phép cập nhật đồng bộ của Định nghĩa 03.8.

**Phạm vi.** Định lý không áp dụng cho $\beta=1$, cũng không áp dụng cho công thức đánh thuế không bù khi có nút cụt. Cận (c) đúng cho mọi đồ thị; trên một đồ thị cụ thể, dãy có thể hội tụ nhanh hơn.
:::

::: proof
**Bước 1 (tính co).** Phần nhảy $(1-\beta)u$ không phụ thuộc véc-tơ nên triệt tiêu trong hiệu: $F(x)-F(y)=\beta\bar M(x-y)$. Theo Bổ đề 03.14 với $A=\bar M$, $\lVert F(x)-F(y)\rVert_1=\beta\lVert\bar M(x-y)\rVert_1\le\beta\lVert x-y\rVert_1$. Đó là (a).

**Bước 2 (tồn tại và duy nhất).** Phương trình $r=F(r)$ tương đương với $(\mathrm I_n-\beta\bar M)r=(1-\beta)u$. Ma trận vuông $\mathrm I_n-\beta\bar M$ khả nghịch: nếu $(\mathrm I_n-\beta\bar M)v=0$ thì $v=\beta\bar Mv$, và Bổ đề 03.14 cho $\lVert v\rVert_1=\beta\lVert\bar Mv\rVert_1\le\beta\lVert v\rVert_1$, tức $(1-\beta)\lVert v\rVert_1\le0$; vì $\beta<1$, $v=0$. Vậy hệ có đúng một nghiệm
$$
r^*=(1-\beta)(\mathrm I_n-\beta\bar M)^{-1}u .
$$

**Bước 3 (tổng bằng 1).** Mọi cột của $\bar M$ có tổng 1, tức $\mathbf 1^{\mathsf T}\bar M=\mathbf 1^{\mathsf T}$, và $\mathbf 1^{\mathsf T}u=1$. Nhân hai vế của $r^*=\beta\bar Mr^*+(1-\beta)u$ với $\mathbf 1^{\mathsf T}$ cho $\mathbf 1^{\mathsf T}r^*=\beta\,\mathbf 1^{\mathsf T}r^*+(1-\beta)$, nên $(1-\beta)\mathbf 1^{\mathsf T}r^*=1-\beta$ và $\sum_ir^*_i=1$.

**Bước 4 (tốc độ).** Với mọi $t$, $r^{t+1}-r^*=F(r^t)-F(r^*)$, nên theo (a), $\lVert r^{t+1}-r^*\rVert_1\le\beta\lVert r^t-r^*\rVert_1$. Quy nạp theo $t$ cho $\lVert r^t-r^*\rVert_1\le\beta^t\lVert r^0-r^*\rVert_1$.

**Bước 5 (không âm).** Theo Mệnh đề 03.13 và Mệnh đề 03.9(a), mọi $r^t$ là phân phối, nên $r^t_i\ge0$. Giả sử $r^*_i<0$ với một $i$ nào đó. Khi đó với mọi $t$,
$$
\begin{aligned}
\lVert r^t-r^*\rVert_1&\ge\lvert r^t_i-r^*_i\rvert\\
&\ge-r^*_i>0,
\end{aligned}
$$
trái với Bước 4, vì vế phải của Bước 4 không quá $\beta^t\lVert r^0-r^*\rVert_1$ và tiến về 0. Vậy $r^*\ge0$, và cùng Bước 3, $r^*$ là một phân phối. Bước 2, 3, 5 cho (b).

**Bước 6 (cận theo 2).** Với hai phân phối $x,y$, $\lVert x-y\rVert_1\le\lVert x\rVert_1+\lVert y\rVert_1=1+1=2$ theo bất đẳng thức tam giác. Áp cho $x=r^0$, $y=r^*$ và kết hợp Bước 4 được (c). $\square$
:::

![Hai hàng: phân phối x qua phép cập nhật F thành F(x), phân phối y qua cùng F thành F(y); ghi chú so khoảng cách giữa hai phân phối trước và sau cập nhật, không so từng điểm.](img/lec-03/visual-contraction.svg)

Hình đặt hai phân phối qua cùng một phép cập nhật; theo (a), khoảng cách $\ell_1$ giữa hai kết quả không quá $\beta$ lần khoảng cách ban đầu, dù từng điểm có thể tăng hay giảm.

Bỏ một trong hai giả thiết sau của Định lý 03.15 thì kết luận sai.

- Bỏ $\beta<1$: trên đồ thị hai trang $\mathrm A\rightleftarrows\mathrm B$, $\bar M=M_0=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, và phép lặp $r^{t+1}=M_0r^t$ từ $r^0=(1,0)$ luân phiên $(0,1)$, $(1,0)$, không có giới hạn, dù $r^*=(1/2,1/2)$ thỏa $r^*=M_0r^*$. Trên bẫy C của Ví dụ 03.8, lặp thô hội tụ nhưng tới $(0,0,1,0)$.
- Bỏ cập nhật đồng bộ: trên bốn trang, vòng đầu tính lần lượt A, B, C, D và dùng ngay điểm mới cho tổng $404/375$, nên véc-tơ mới không còn là $F(r^0)$ và không còn là phân phối.

Bước 1 và Bước 2 dùng $\beta<1$ cùng tính ngẫu nhiên theo cột của $\bar M$; Bước 3 dùng phần bù, vì chính phần bù làm cột nút cụt có tổng 1, và Mệnh đề 03.17 cho phản ví dụ khi bỏ nó; Bước 4 dùng cập nhật đồng bộ $r^{t+1}=F(r^t)$; Bước 5 dùng Mệnh đề 03.13.

Trên đồ thị hai trang, quy tắc đầy đủ với $\beta=4/5$ cho $F(r)=\tfrac45(r_{\mathrm B},r_{\mathrm A})+\tfrac1{10}\mathbf 1$; từ $r^0=(1,0)$ ta có $\lVert r^t-r^*\rVert_1=(4/5)^t$, đúng bằng $\beta^t\lVert r^0-r^*\rVert_1$. Cận $\beta^t\lVert r^0-r^*\rVert_1$ của (c) vì vậy không cải thiện được nếu chỉ biết $\beta$. Định lý 03.15 không cần điều kiện nào về cấu trúc đồ thị: nó chỉ cần $\beta<1$, một tham số do người dùng thuật toán chọn. Một cách chứng minh khác cho (b) dùng tính đầy đủ của $\mathbb R^n$: theo (a), $\Delta_t\le\beta^t\Delta_0$, nên $\lVert r^p-r^q\rVert_1\le\beta^p\Delta_0/(1-\beta)$ với $q>p$; dãy $r^t$ là dãy Cauchy, và giới hạn của nó là một điểm cố định vì $F$ liên tục.

Định lý 03.15 cho tốc độ khi biết $r^*$, nhưng chương trình không biết $r^*$. Hệ quả sau đổi $\Delta_t$, đại lượng đo được, thành cận sai số.

::: corollary Hệ quả 03.16 (Cận sai số khi dừng)
**Giả thiết.** Như Định lý 03.15; $\Delta_t=\lVert r^{t+1}-r^t\rVert_1$.

**Kết luận.** Với mọi $t\ge0$,
$$
\lVert r^{t+1}-r^*\rVert_1\le\frac{\beta}{1-\beta}\,\Delta_t .
$$
Do đó, với $\varepsilon>0$, nếu Thuật toán 03.10 dùng ngưỡng $\tau\le(1-\beta)\varepsilon/\beta$ và trả trạng thái đạt ngưỡng thì véc-tơ trả về cách $r^*$ không quá $\varepsilon$.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Cận nói về $r^{t+1}$, véc-tơ đã tính xong ở vòng có độ thay đổi $\Delta_t$, và đúng với mọi $t$. Khi thuật toán dừng vì hết $K$ vòng, cận vẫn cho sai số không quá $\beta\Delta/(1-\beta)$ với $\Delta$ cuối, nhưng không bảo đảm sai số $\varepsilon$.
:::

::: proof
Theo Định lý 03.15(a) với $x=r^t$, $y=r^*$, rồi bất đẳng thức tam giác,
$$
\begin{aligned}
&\lVert r^{t+1}-r^*\rVert_1\\
&\quad\le\beta\lVert r^t-r^*\rVert_1\\
&\quad\le\beta\Delta_t+\beta\lVert r^{t+1}-r^*\rVert_1 .
\end{aligned}
$$
Dòng thứ hai dùng Định lý 03.15(a) và $r^*=F(r^*)$; dòng thứ ba dùng bất đẳng thức tam giác $\lVert r^t-r^*\rVert_1\le\lVert r^t-r^{t+1}\rVert_1+\lVert r^{t+1}-r^*\rVert_1=\Delta_t+\lVert r^{t+1}-r^*\rVert_1$.
Chuyển vế được $(1-\beta)\lVert r^{t+1}-r^*\rVert_1\le\beta\Delta_t$, và chia cho $1-\beta>0$ được kết luận. Khi thuật toán trả đạt ngưỡng sau $t_{\text{dừng}}$ vòng, véc-tơ trả về là $r^{t+1}$ với $t=t_{\text{dừng}}-1$ và $\Delta_t\le\tau$ (Mệnh đề 03.11), nên sai số không quá $\beta\tau/(1-\beta)\le\varepsilon$. $\square$
:::

Với $\beta=4/5$, hệ số là $\beta/(1-\beta)=4$: sai số không quá bốn lần độ thay đổi cuối, và để bảo đảm sai số $\varepsilon$ chỉ cần $\tau=\varepsilon/4$. Hệ số tăng nhanh khi $\beta$ gần 1: với $\beta=0{,}9$, hệ số là 9. Ví dụ sau đặt cận này cạnh sai số thật trên bốn trang.

::: example Ví dụ 03.13 (Nghiệm của bốn trang và sai số của $r^2$)
**Dữ kiện.** Đồ thị của Ví dụ 03.2, không có nút cụt; $\beta=4/5$; theo Ví dụ 03.12, $r^2=(31/100,23/100,23/100,23/100)$ và $\Delta_1=2/25$.

**Giải $r=F(r)$.** Theo Mệnh đề 03.9(c), $r_i=\tfrac45(M_0r)_i+\tfrac1{20}$. Hàng B và hàng C của $M_0$ trùng nhau, nên $r_{\mathrm B}=r_{\mathrm C}$. Trừ phương trình hàng D khỏi phương trình hàng B:
$$
\begin{aligned}
r_{\mathrm B}-r_{\mathrm D}&=\tfrac45\Big(\tfrac{r_{\mathrm A}}3+\tfrac{r_{\mathrm D}}2\Big)\\
&\quad-\tfrac45\Big(\tfrac{r_{\mathrm A}}3+\tfrac{r_{\mathrm B}}2\Big)\\
&=\tfrac25(r_{\mathrm D}-r_{\mathrm B}),
\end{aligned}
$$
nên $\tfrac75(r_{\mathrm B}-r_{\mathrm D})=0$ và $r_{\mathrm D}=r_{\mathrm B}$. Hàng A cho $r_{\mathrm A}=\tfrac45\cdot\tfrac32r_{\mathrm B}+\tfrac1{20}=\tfrac65r_{\mathrm B}+\tfrac1{20}$; điều kiện tổng $r_{\mathrm A}+3r_{\mathrm B}=1$ cho $\tfrac{21}5r_{\mathrm B}=\tfrac{19}{20}$, nên
$$
\begin{gathered}
r_{\mathrm B}=\frac{19}{84},\\
r_{\mathrm A}=\frac65\cdot\frac{19}{84}+\frac1{20}=\frac{9}{28},\\
r^*=\Big(\frac9{28},\frac{19}{84},\frac{19}{84},\frac{19}{84}\Big).
\end{gathered}
$$

**Sai số thật và cận.** $\lvert\tfrac{31}{100}-\tfrac9{28}\rvert=\tfrac2{175}$ và $\lvert\tfrac{23}{100}-\tfrac{19}{84}\rvert=\tfrac2{525}$, nên
$$
\begin{aligned}
\lVert r^2-r^*\rVert_1&=\frac2{175}+\frac6{525}\\
&=\frac4{175}\\
&\le4\Delta_1=\frac8{25} .
\end{aligned}
$$

**Cận theo số vòng.** Định lý 03.15(c) bảo đảm sai số $\varepsilon=10^{-8}$ khi $2\beta^t\le10^{-8}$, tức $t\ge\ln(2\cdot10^8)/\ln(5/4)\approx85{,}7$, nên 86 vòng là đủ.

**Kiểm tra lại.** Hàng B: $\tfrac45\big(\tfrac{9}{84}+\tfrac{19}{168}\big)+\tfrac1{20}=\tfrac45\cdot\tfrac{37}{168}+\tfrac1{20}=\tfrac{37}{210}+\tfrac1{20}=\tfrac{95}{420}=\tfrac{19}{84}$; tổng $\tfrac{27}{84}+\tfrac{57}{84}=1$.
:::

Trên bốn trang, sai số thật $4/175$ của $r^2$ nhỏ hơn cận $8/25$ đúng 14 lần.

Định lý 03.15 cũng cho biết điều gì xảy ra khi bỏ phần bù rồi chuẩn hóa lại kết quả, cách trang chiếu MMDS (tr.51) đề nghị khi ma trận có nút cụt.

::: proposition Mệnh đề 03.17 (Công thức đánh thuế không bù và chuẩn hóa lại)
**Giả thiết.** $G$, $M_0$, $\mathcal D$, $\beta$, $u$ và $F$ như Định nghĩa 03.8; $x\in\mathbb R^n$ thỏa $x=\beta M_0x+(1-\beta)u$; $\sigma=\sum_ix_i$ và $\delta_x=\sum_{j\in\mathcal D}x_j$.

**Kết luận.**

- (a) $\sigma=1-\dfrac{\beta\delta_x}{1-\beta}$; do đó $\sigma<1$ khi $\delta_x>0$.
- (b) Nếu $\sigma\ne0$ thì $x/\sigma$ là điểm cố định $r^*$ của $F$ trong Định lý 03.15.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Mệnh đề nói về điểm cố định của công thức không bù; nó không nói phép lặp của công thức đó hội tụ.
:::

::: proof
**Bước 1 (tổng).** Cột $j$ của $M_0$ có tổng 1 khi $j\notin\mathcal D$ và 0 khi $j\in\mathcal D$, nên cộng hai vế của $x=\beta M_0x+(1-\beta)u$ theo mọi thành phần cho $\sigma=\beta(\sigma-\delta_x)+(1-\beta)$. Chuyển vế được $(1-\beta)(\sigma-1)+\beta\delta_x=0$, tức (a).

**Bước 2 (chuẩn hóa).** Đặt $y=x/\sigma$; tổng điểm nút cụt của $y$ là $\delta_x/\sigma$. Theo Định nghĩa 03.8, $\sigma F(y)=\beta M_0x+\big((1-\beta)\sigma+\beta\delta_x\big)u$. Thay $\beta M_0x=x-(1-\beta)u$, vì $x$ là điểm cố định của công thức không bù, được $\sigma F(y)=x+\kappa u$ với $\kappa=(1-\beta)(\sigma-1)+\beta\delta_x$. Theo Bước 1, $\kappa=0$, nên $\sigma F(y)=x$; chia cho $\sigma$ được $F(y)=y$.

**Bước 3 (duy nhất).** Theo Định lý 03.15(b), $F$ có đúng một điểm cố định, nên $y=r^*$. $\square$
:::

Trên biến thể C cụt với $\beta=4/5$, điểm cố định của công thức không bù là $x=(15,19,19,19)/148$, với $\delta_x=19/148$. Theo (a), $\sigma=1-4\cdot\tfrac{19}{148}=\tfrac{72}{148}=\tfrac{18}{37}$, và $x/\sigma=(5/24,19/72,19/72,19/72)$, đúng điểm cố định của $F$ trên cùng đồ thị. Như MMDS nêu, tổng các điểm nhỏ hơn 1 nhưng không tiến về 0 (§5.1.5, tr.186–187); công thức không bù cho cùng thứ hạng với Định nghĩa 03.8, nhưng các điểm phải chuẩn hóa lại mới thành phân phối.

Biến thể C cụt cũng là phản ví dụ cho vai trò của phần bù trong Định lý 03.15. Bỏ phần bù, ma trận của phép lặp là $M_0$, có cột nút cụt tổng 0; Bổ đề 03.14 vẫn cho tính co, nhưng Bước 3 của chứng minh sai, và điểm cố định có tổng $18/37$ thay cho 1.

::: remark Nhận xét 03.18 (Trong thực hành: ngưỡng dừng và sai số)
- Trên số thực dấu phẩy động, một ngưỡng $\tau$ nhỏ hơn sai số làm tròn của tổng $n$ số thực có thể không bao giờ đạt. Khi đó thuật toán dừng vì hết $K$ vòng, trả trạng thái chưa đạt ngưỡng cùng $\Delta$ cuối, và Hệ quả 03.16 vẫn cho sai số không quá $\beta\Delta/(1-\beta)$ trên số học chính xác.
- Cận của Hệ quả 03.16 chỉ dùng tính co theo hệ số $\beta$, nên nó còn đúng khi phân phối đều $u$ trong phần nhảy $(1-\beta)u$ được thay bằng một phân phối nhảy khác trên $V$, miễn là phân phối đó không phụ thuộc $r$.
:::

::: exercise Bài tập 03.2 (Ngưỡng dừng trên đồ thị hai trang)
Đồ thị gồm hai trang $\mathrm A$, $\mathrm B$ với hai cạnh $\mathrm A\to\mathrm B$ và $\mathrm B\to\mathrm A$; $\beta=4/5$. Xét phép lặp $r^{t+1}=F(r^t)$ của Định nghĩa 03.8 từ $r^0=(1,0)$.

- (a) Tính $r^1$, $r^2$, $\Delta_0$, $\Delta_1$, rồi chứng minh $\Delta_t=\tfrac95(4/5)^t$ với mọi $t\ge0$.
- (b) Chọn $\tau$ theo Hệ quả 03.16 để sai số không quá $10^{-3}$. Xác định vòng mà Thuật toán 03.10, với bước 1 khởi tạo $r^0=(1,0)$, dừng ở trạng thái đạt ngưỡng, và sai số thật của véc-tơ trả về.
- (c) Xác định số vòng mà Định lý 03.15(c) cần để bảo đảm sai số không quá $10^{-3}$, rồi so với (b).
:::

::: hint
Đồ thị không có nút cụt nên $F(r)=\tfrac45(r_{\mathrm B},r_{\mathrm A})+\tfrac1{10}(1,1)$ và $r^*=(1/2,1/2)$. Viết $e^t=r^t-r^*$ và chỉ ra $e^{t+1}=-\tfrac45e^t$.
:::

::: solution
**Câu (a).** $r^1=\big(\tfrac45\cdot0+\tfrac1{10},\ \tfrac45\cdot1+\tfrac1{10}\big)=(1/10,9/10)$ và $r^2=\big(\tfrac45\cdot\tfrac9{10}+\tfrac1{10},\ \tfrac45\cdot\tfrac1{10}+\tfrac1{10}\big)=(41/50,9/50)$. Do đó $\Delta_0=\tfrac9{10}+\tfrac9{10}=\tfrac95$ và $\Delta_1=\tfrac{36}{50}+\tfrac{36}{50}=\tfrac{36}{25}$.

Với $r^*=(1/2,1/2)$ và $e^t=r^t-r^*$, mọi $e^t$ có dạng $(a,-a)$ vì $r^t$ và $r^*$ cùng tổng 1. Khi đó $e^{t+1}=F(r^t)-F(r^*)=\tfrac45(e^t_{\mathrm B},e^t_{\mathrm A})=-\tfrac45e^t$. Suy ra
$$
\begin{aligned}
\Delta_t&=\lVert e^{t+1}-e^t\rVert_1\\
&=\Big(1+\frac45\Big)\lVert e^t\rVert_1=\frac95\Big(\frac45\Big)^t,
\end{aligned}
$$
vì $\lVert e^0\rVert_1=\lvert1-\tfrac12\rvert+\lvert0-\tfrac12\rvert=1$ và $\lVert e^t\rVert_1=(4/5)^t$.

**Câu (b).** Hệ quả 03.16 với $\varepsilon=10^{-3}$ cho $\tau=(1-\beta)\varepsilon/\beta=10^{-3}/4=2{,}5\cdot10^{-4}$. Điều kiện $\tfrac95(4/5)^t\le2{,}5\cdot10^{-4}$ tương đương với $t\ge\ln7200/\ln(5/4)\approx39{,}8$. Do đó $\Delta_{39}\approx2{,}99\cdot10^{-4}>\tau$ và $\Delta_{40}\approx2{,}39\cdot10^{-4}\le\tau$: thuật toán dừng sau vòng thứ 41 và trả $r^{41}$. Sai số thật là $\lVert e^{41}\rVert_1=(4/5)^{41}\approx1{,}06\cdot10^{-4}$, còn cận của Hệ quả 03.16 là $4\Delta_{40}\approx9{,}57\cdot10^{-4}$; cả hai không quá $10^{-3}$.

**Câu (c).** Ở đây $\lVert r^0-r^*\rVert_1=1$, nên Định lý 03.15(c) cho sai số không quá $(4/5)^t$, và $(4/5)^t\le10^{-3}$ khi $t\ge\ln1000/\ln(5/4)\approx30{,}96$, tức sau 31 vòng. Cận dạng $2\beta^t$ cần $t\ge\ln2000/\ln(5/4)\approx34{,}06$, tức 35 vòng. Tiêu chí dừng theo $\Delta_t$ chạy thêm 10 vòng so với 31 vòng, vì $\Delta_t=\tfrac95\lVert e^t\rVert_1$ lớn hơn sai số; đổi lại, nó không cần biết $r^*$.

**Kiểm tra lại.** $\Delta_1/\Delta_0=(36/25)/(9/5)=4/5$; $r^2-r^*=(8/25,-8/25)$ có chuẩn $16/25=(4/5)^2$.
:::

Quy tắc có bước nhảy và phần bù (Định nghĩa 03.8) cho một phân phối duy nhất trên mọi đồ thị, phép lặp hội tụ với tốc độ $\beta^t$ (Định lý 03.15), và độ thay đổi $\Delta_t$ chặn được sai số (Hệ quả 03.16); trên bốn trang, PageRank là $(9/28,19/84,19/84,19/84)$. Tuy nhiên, Thuật toán 03.10 giữ cả đồ thị và hai véc-tơ trong bộ nhớ một máy. Trong Mục 3, chúng ta lưu đồ thị theo các liên kết và chia một vòng thành các tác vụ MapReduce.

<!-- note-topic-id: lec-03-topic-08 -->
## 3. Tính PageRank trên đồ thị lớn

Trung bình một trang web có khoảng 10 liên kết ra (MMDS, §5.2.1, tr.190). Với $n=10^9$ trang, $m\approx10^{10}$, nên chỉ $10^{10}/10^{18}=10^{-8}$ số ô của ma trận khác 0.

Lưu bậc ra của mọi trang và mọi đích, mỗi số 4 byte, cần $4(n+m)=4{,}4\cdot10^{10}$ byte; hai véc-tơ $r$ và $\mathrm{new}$ của Thuật toán 03.10 cần $16n=1{,}6\cdot10^{10}$ byte. MMDS cho rằng với kích thước Web hiện nay, véc-tơ điểm nhiều khả năng không vừa bộ nhớ chính (§5.2.2, tr.191). Chúng ta cần hai việc: một định dạng lưu đồ thị trên đĩa với đúng $4(n+m)$ byte đó, và một cách chia một vòng của Định nghĩa 03.8 thành các tác vụ MapReduce sao cho mỗi tác vụ chỉ giữ một phần của các véc-tơ trong bộ nhớ.

### 3.1 Danh sách liên kết ra

Ma trận liên kết có một tính chất mà ma trận thưa tổng quát không có: mọi phần tử khác 0 của cột $j$ đều bằng $1/d_j$. Biết $d_j$ và hàng của các phần tử đó là đủ để dựng lại cột, nên không cần lưu giá trị nào (MMDS, §5.2.1, tr.190).

::: definition Định nghĩa 03.19 (Danh sách liên kết ra)
**Danh sách liên kết ra** của đồ thị web $G$ gồm một bản ghi cho mỗi trang nguồn $j\in V$,
$$
\big(j,\ d_j,\ [i_1,\ldots,i_{d_j}]\big),
$$
trong đó $i_1,\ldots,i_{d_j}$ là các đích của $j$, mỗi đích một lần. Một nút cụt có bản ghi $(j,0,[\,])$.
:::

Bản ghi của $j$ là cột $j$ của $M_0$ viết gọn: hàng $i_\ell$ có giá trị $1/d_j$, các hàng khác bằng 0. Đây cũng là danh sách kề $\mathrm{out}[j]$ của Thuật toán 03.10, cộng bậc ra. Nút cụt vẫn giữ bản ghi dù cột của nó toàn 0, vì phần chung của Định nghĩa 03.8 cần $\delta=\sum_{j\in\mathcal D}r_j$; bỏ bản ghi đó làm mất điểm của nút cụt khỏi phép tính $\delta$.

::: example Ví dụ 03.14 (Danh sách liên kết ra của bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2.

**Bốn bản ghi** (MMDS Ví dụ 5.7, Hình 5.11, tr.190):

| Nguồn | Bậc ra | Đích |
|---|---|---|
| A | 3 | B, C, D |
| B | 2 | A, D |
| C | 1 | A |
| D | 2 | B, C |

**Dựng lại cột A.** Bản ghi của A có bậc 3 và ba đích B, C, D, nên cột A của $M_0$ có $1/3$ ở hàng B, C, D và 0 ở hàng A, đúng như Ví dụ 03.5.

**Kiểm tra lại.** Tổng cột bậc ra là $8=m$; số đích liệt kê cũng là 8.
:::

<!-- note-topic-id: lec-03-topic-09 -->
### 3.2 Một vòng là một công việc nhân ma trận–véc-tơ

Theo Mệnh đề 03.4(a), phần đi theo liên kết của một vòng là $z=M_0r$, với $z_i=\sum_{j\to i}r_j/d_j$. Phép tính có cùng dạng với Thuật toán 02.18: mỗi phần tử khác 0 của ma trận sinh một số hạng, và các số hạng cùng hàng phải gặp nhau. Ví dụ sau làm điều đó cho trang A.

::: example Ví dụ 03.15 (Cộng đóng góp về A bằng MapReduce)
**Dữ kiện.** Danh sách liên kết ra của Ví dụ 03.14; $r^0=(1/4,1/4,1/4,1/4)$; $\beta=4/5$, $\delta^0=0$.

**Map.** Map đọc bản ghi $(j,d_j,[\ldots])$ và phát $(i,r_j/d_j)$ cho mỗi đích $i$. Hai bản ghi có đích A:

- bản ghi $(\mathrm B,2,[\mathrm A,\mathrm D])$ phát $(\mathrm A,1/8)$ và $(\mathrm D,1/8)$;
- bản ghi $(\mathrm C,1,[\mathrm A])$ phát $(\mathrm A,1/4)$.

**Reduce cho khóa A.** Danh sách $L_{\mathrm A}=[1/8,1/4]$; tổng $z_{\mathrm A}=3/8$; hàm hoàn tất trả $\tfrac45\cdot\tfrac38+\tfrac{(1/5)+0}{4}=\tfrac3{10}+\tfrac1{20}=\tfrac7{20}$.

**Kiểm tra lại.** $7/20$ là $r^1_{\mathrm A}$ của Ví dụ 03.9.
:::

Reduce cộng các đóng góp chưa nhân $\beta$, rồi một hàm hoàn tất đổi tổng $3/8$ thành điểm mới. So với Thuật toán 02.18, cách tính một vòng có ba thay đổi và một giới hạn.

::: remark Nhận xét 03.20 (Từ Thuật toán 02.18 tới một vòng PageRank)
- **Chỉ các cạnh có thật.** Map đọc danh sách liên kết ra và phát một cặp $(i,r_j/d_j)$ cho mỗi cạnh $j\to i$, với khóa là trang đích; Thuật toán 02.18 phát một cặp cho mỗi bản ghi $(i,j,a_{ij})$.
- **Reduce có hàm hoàn tất.** Reduce trên khóa $i$ cộng danh sách thành $z_i$ rồi trả $\phi(z_i)=\beta z_i+\big((1-\beta)+\beta\delta\big)/n$. Phép cộng kết hợp, giao hoán, nên theo Mệnh đề 02.15 với $\oplus=+$, Combine cộng cục bộ được phép.
- **Trang không có liên kết vào.** Theo Nhận xét 02.20, một hàng không có phần tử khác 0 không có cặp nào và vắng khỏi đầu ra. Ở đây trang đó vẫn phải nhận phần chung, nên mỗi trang $i$ cần thêm một cặp khởi tạo $(i,0)$.
- **Giới hạn.** Thuật toán 02.18 giả thiết véc-tơ $v$ vừa bộ nhớ mỗi tác vụ Map. Khi $r$ không vừa, Tình huống 02.3 chia ma trận thành dải dọc và $r$ thành các đoạn tương ứng. Một dải dọc của $M_0$ vẫn đóng góp vào mọi thành phần của $z$, và $z$ dài bằng $r$ nên cũng không vừa bộ nhớ; nếu Map cộng dồn vào $z$ để dùng Combine, gần như mỗi số hạng phải đưa phần của $z$ chứa $z_i$ từ đĩa vào bộ nhớ. Hiện tượng này gọi là *đọc ghi lặp* (thrashing) và chậm hơn nhiều bậc độ lớn (MMDS, §5.2.3, tr.191).
:::

<!-- note-topic-id: lec-03-topic-10 -->
### 3.3 Chia khối

Về mặt ý tưởng, chúng ta chia cả hai chiều của ma trận. Nếu một tác vụ chỉ xử lý các cạnh có nguồn trong một nhóm trang và đích trong một nhóm trang khác, nó chỉ cần đọc phần $r$ của nhóm nguồn và chỉ cộng vào phần $z$ của nhóm đích, nên cả hai phần cùng vừa bộ nhớ (MMDS, §5.2.3, tr.192).

::: definition Định nghĩa 03.21 (Chia khối ma trận liên kết)
Cho đồ thị web $G$ và số nguyên $k\ge1$. Chia $V$ thành $k$ **dải** rời nhau $V_1,\ldots,V_k$ có hợp bằng $V$.

- **Dải điểm** $r_b$ là phần của $r$ trên các trang của $V_b$; **dải tổng** $z_a$ là phần của $z=M_0r$ trên $V_a$.
- **Khối** $M_{ab}$, với $1\le a,b\le k$, là phần của $M_0$ có hàng trong $V_a$ và cột trong $V_b$: nó chứa các cạnh $j\to i$ với nguồn $j\in V_b$ và đích $i\in V_a$.
- **Biểu diễn khối** của $M_{ab}$ gồm một bản ghi $(j,d_j,[\text{các đích của }j\text{ trong }V_a])$ cho mỗi nguồn $j\in V_b$ có ít nhất một đích trong $V_a$, trong đó $d_j$ là bậc ra của $j$ trên toàn đồ thị.
:::

Có $k^2$ khối, và mỗi cạnh $j\to i$ nằm trong đúng một khối, khối có $b$ là dải của $j$ và $a$ là dải của $i$. Theo Mệnh đề 03.4(a), dải tổng là $z_a=\sum_{b=1}^kM_{ab}r_b$, tổng của $k$ phép nhân khối.

Một nguồn có đích trong nhiều dải có bản ghi trong nhiều khối của cùng một cột khối, và bậc ra của nó được ghi lại ở mỗi bản ghi (MMDS, §5.2.4, tr.192–193). Bậc ghi trong bản ghi là bậc toàn cục, không phải số đích trong khối: đóng góp của một cạnh là $r_j/d_j$ dù cạnh nằm ở khối nào.

![Ma trận chia bốn khối. Dải điểm r₁ gồm A, B cấp cho cột khối chứa M₁₁ và M₂₁; dải r₂ gồm C, D cấp cho cột khối chứa M₁₂ và M₂₂. M₁₁ và M₁₂ cùng đóng góp vào dải tổng z₁ của đích A, B; M₂₁ và M₂₂ đóng góp vào z₂ của đích C, D. Hàng là đích, cột là nguồn.](img/lec-03/rlarge-blocks-grid.svg)

Trên hình, mỗi dải điểm cấp cho $k$ khối của cùng cột khối, và mỗi dải tổng nhận từ $k$ khối của cùng hàng khối. Với $k=2$, mỗi dải điểm được đọc hai lần trong một vòng.

::: example Ví dụ 03.16 (Bốn khối của bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2; $k=2$, $V_1=\{\mathrm A,\mathrm B\}$, $V_2=\{\mathrm C,\mathrm D\}$; $r^0=u$.

**Bốn khối** (MMDS Ví dụ 5.8, Hình 5.13–5.14, tr.193–194):

| Khối | Nguồn $\to$ đích | Bản ghi |
|---|---|---|
| $M_{11}$ (đích A, B; nguồn A, B) | $\mathrm A\to\mathrm B$, $\mathrm B\to\mathrm A$ | $(\mathrm A,3,[\mathrm B])$, $(\mathrm B,2,[\mathrm A])$ |
| $M_{12}$ (đích A, B; nguồn C, D) | $\mathrm C\to\mathrm A$, $\mathrm D\to\mathrm B$ | $(\mathrm C,1,[\mathrm A])$, $(\mathrm D,2,[\mathrm B])$ |
| $M_{21}$ (đích C, D; nguồn A, B) | $\mathrm A\to\mathrm C$, $\mathrm A\to\mathrm D$, $\mathrm B\to\mathrm D$ | $(\mathrm A,3,[\mathrm C,\mathrm D])$, $(\mathrm B,2,[\mathrm D])$ |
| $M_{22}$ (đích C, D; nguồn C, D) | $\mathrm D\to\mathrm C$ | $(\mathrm D,2,[\mathrm C])$ |

**Dải điểm.** $r_1=(r_{\mathrm A},r_{\mathrm B})=(1/4,1/4)$ cấp cho $M_{11}$ và $M_{21}$; $r_2=(r_{\mathrm C},r_{\mathrm D})=(1/4,1/4)$ cấp cho $M_{12}$ và $M_{22}$.

**Kiểm tra lại.** Có $2+2+2+1=7$ bản ghi và $1+1+1+1+2+1+1=8$ đích, bằng $m$. Bậc của A là 3 ở cả $M_{11}$ lẫn $M_{21}$. C không có bản ghi trong $M_{22}$ vì C không trỏ tới C hay D.
:::

Một tác vụ Map nhận một khối và dải điểm của cột khối đó. Ví dụ sau chạy tay tác vụ của $M_{21}$, khối có hai cạnh cùng đích.

::: example Ví dụ 03.17 (Map và Combine trên khối $M_{21}$)
**Dữ kiện.** Khối $M_{21}$ của Ví dụ 03.16 với hai bản ghi $(\mathrm A,3,[\mathrm C,\mathrm D])$, $(\mathrm B,2,[\mathrm D])$; dải $r_1=(1/4,1/4)$.

**Map.** Bản ghi của A phát $(\mathrm C,\tfrac{1/4}3)=(\mathrm C,1/12)$ và $(\mathrm D,1/12)$; bản ghi của B phát $(\mathrm D,\tfrac{1/4}2)=(\mathrm D,1/8)$.

**Combine.** Cộng theo khóa trong tác vụ: $(\mathrm C,1/12)$ giữ nguyên; $(\mathrm D,1/12+1/8)=(\mathrm D,5/24)$.

**Kiểm tra lại.** Tác vụ gửi đi 2 cặp thay cho 3; $1/12+5/24=7/24=1/12+1/12+1/8$, tổng không đổi.
:::

![Trong cùng tác vụ M₂₁, cạnh A tới D cho cặp (D, 1/12), cạnh B tới D cho cặp (D, 1/8); Combine cộng theo khóa thành một cặp (D, 5/24).](img/lec-03/cost-combine.svg)

Hình chỉ phần Combine của Ví dụ 03.17: hai cặp cùng khóa D trong một tác vụ thành một cặp. Thuật toán sau viết vòng hoàn chỉnh cho mọi khối.

::: algorithm Thuật toán 03.22 (Một vòng PageRank theo khối)
**Đầu vào.** Biểu diễn khối của $M_{ab}$ cho $1\le a,b\le k$; các dải $r_1,\ldots,r_k$ của véc-tơ $r$ hiện tại; danh sách liên kết ra của Định nghĩa 03.19, dùng để biết nút cụt; $n$ và $\beta$.

**Đầu ra.** Véc-tơ $F(r)$ dưới dạng $n$ cặp $(i,F(r)_i)$.

**Giả thiết.** Mọi tác vụ đọc cùng một véc-tơ $r$, không đổi trong vòng.

1. **Pha $\delta$.** Một công việc cộng $r_j$ trên các bản ghi có $d_j=0$ của danh sách liên kết ra, mỗi trang một lần, được $\delta$; giá trị này được gửi tới mọi tác vụ Reduce. Pha này có thể chạy song song với bước 3.
2. **Bản ghi khởi tạo.** Với mỗi trang $i\in V$, phát cặp $(i,0)$.
3. **Map.** Với mỗi khối $M_{ab}$, một tác vụ nhận khối và dải $r_b$; với mỗi bản ghi $(j,d_j,[i_1,\ldots])$ và mỗi đích $i_\ell$, phát $(i_\ell,r_j/d_j)$.
4. **Combine.** Trong mỗi tác vụ Map, với mỗi khóa $i$, thay các cặp $(i,x_1),\ldots,(i,x_c)$ bằng một cặp $(i,x_1+\cdots+x_c)$.
5. **Nhóm và Reduce.** Hệ thống nhóm mọi cặp theo khóa $i$; Reduce trên $(i,L_i)$ tính $z_i=\sum_{x\in L_i}x$ và phát $\big(i,\ \beta z_i+((1-\beta)+\beta\delta)/n\big)$.
6. **Độ thay đổi.** Một bước tổng hợp tính $\Delta=\sum_i\lvert F(r)_i-r_i\rvert$ cho điều kiện dừng của Thuật toán 03.10.

**Dừng.** Mỗi pha xử lý hữu hạn bản ghi.

**Trường hợp biên.** Trang không có liên kết vào chỉ có cặp $(i,0)$ và nhận đúng phần chung. Nút cụt không có bản ghi trong khối nào, chỉ có mặt ở bước 1. Với $k=1$, có một khối là toàn bộ danh sách liên kết ra.

**Chi phí.** Mô hình đếm bản ghi, cặp và phép cộng trong một vòng; Mệnh đề 03.26–03.29 đổi các số này thành byte và giây.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1 (pha $\delta$) | $n$ bản ghi | đọc một bậc; cộng nếu bậc bằng 0 | $n$ lần đọc, $\lvert\mathcal D\rvert$ phép cộng |
| 2 (cặp khởi tạo) | $n$ trang | phát một cặp | $n$ cặp |
| 3 (Map) | $m$ cạnh, $k^2$ tác vụ | một phép chia, phát một cặp | $m$ cặp; mỗi dải điểm đọc $k$ lần |
| 4 (Combine) | $m$ cặp | gộp các cặp cùng khóa trong một tác vụ | $m-q$ phép cộng, $q$ cặp |
| 5 (Reduce) | $n$ khóa, $q+n$ giá trị | cộng danh sách, áp hàm hoàn tất | $q$ phép cộng, $n$ lần tính hàm hoàn tất |
| 6 (độ thay đổi) | $n$ trang | một hiệu, một trị tuyệt đối | $n$ |
:::

```text
δ ← tổng r[j] trên các nguồn j có d[j] = 0      # một lần, từ danh sách liên kết ra
với mỗi trang i: phát (i, 0)
Map(M_ab, r_b):
    với mỗi bản ghi (j, d_j, đích) của M_ab:
        với mỗi i trong đích: phát (i, r_b[j] / d_j)
Combine(i, L): phát (i, tổng các phần tử của L)
Reduce(i, L_i):
    z_i ← tổng các phần tử của L_i
    phát (i, β·z_i + ((1 − β) + β·δ) / n)
```

Thao tác quyết định là chọn khóa là trang đích $i$ ở Map: mọi đóng góp cho $i$, từ mọi khối của hàng khối chứa $i$, gặp nhau ở một lần gọi Reduce. Có $k^2$ tác vụ Map, nhưng $k^2$ là số tác vụ, không phải số máy: bốn tác vụ của $k=2$ có thể chạy trên hai máy. Mỗi tác vụ Map chỉ cộng vào dải $z_a$ của hàng khối của nó, nên Combine chỉ cần giữ $n/k$ tổng bộ phận trong bộ nhớ (MMDS, §5.2.3, tr.192).

![Các giai đoạn trong một vòng, từ trái sang phải: điểm cũ r^t; Map và tổng δ; Combine; chuyển và nhóm theo khóa; Reduce; đo Δ và xét vòng tiếp theo.](img/lec-03/rlarge-round-pipeline.svg)

Sơ đồ xếp các bước của Thuật toán 03.22 theo thời gian: pha $\delta$ chạy cùng lúc với Map vì cả hai chỉ đọc $r$, nhưng phải xong trước Reduce vì hàm hoàn tất cần $\delta$.

::: example Ví dụ 03.18 (Gộp hai khối tại B)
**Dữ kiện.** Bốn khối của Ví dụ 03.16; $r^0=u$; $\beta=4/5$; đồ thị không có nút cụt nên pha $\delta$ cho $\delta=0$ và phần chung là $1/20$.

**Map.** Hai khối có đích B. Khối $M_{11}$ phát $(\mathrm B,\tfrac{1/4}3)=(\mathrm B,1/12)$ từ bản ghi $(\mathrm A,3,[\mathrm B])$; khối $M_{12}$ phát $(\mathrm B,\tfrac{1/4}2)=(\mathrm B,1/8)$ từ bản ghi $(\mathrm D,2,[\mathrm B])$. Mỗi khối chỉ có một cặp khóa B, nên Combine không gộp được gì.

**Reduce cho B.** $L_{\mathrm B}=[0,1/12,1/8]$, gồm cặp khởi tạo; $z_{\mathrm B}=5/24$; Reduce phát $(\mathrm B,\tfrac45\cdot\tfrac5{24}+\tfrac1{20})=(\mathrm B,13/60)$.

**Kiểm tra lại.** $13/60$ trùng $r^1_{\mathrm B}$ của Ví dụ 03.9, tính trên một máy.
:::

Hai cặp khóa B đến từ hai tác vụ khác nhau và chỉ gặp nhau ở Reduce, vì Combine chỉ gộp các cặp trong một tác vụ. Mệnh đề sau chứng minh mọi trang nhận đúng điểm của Định nghĩa 03.8, với mọi cách chia.

::: proposition Mệnh đề 03.23 (Tính đúng của cách chia khối)
**Giả thiết.**

- $V_1,\ldots,V_k$ là một phân hoạch của $V$, và các khối được lập theo Định nghĩa 03.21 với bậc ra toàn cục $d_j$.
- Mọi tác vụ Map đọc cùng một véc-tơ $r$, không đổi trong vòng.
- $\delta$ được tính một lần từ danh sách liên kết ra, mỗi nút cụt đúng một lần.
- Mỗi trang có đúng một cặp khởi tạo $(i,0)$.
- Công việc thỏa các giả thiết của Mệnh đề 02.11.

**Kết luận.** Thuật toán 03.22 phát đúng một cặp $(i,F(r)_i)$ cho mỗi trang $i\in V$, có hay không có Combine.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Mệnh đề nói về một vòng; điều kiện dừng và số vòng do Thuật toán 03.10 và Hệ quả 03.16 quyết định.
:::

::: proof
**Bước 1 (mỗi cạnh đúng một khối).** Vì các dải là một phân hoạch, cạnh $j\to i$ có đúng một $b$ với $j\in V_b$ và đúng một $a$ với $i\in V_a$, nên nằm trong đúng một khối $M_{ab}$ và trong đúng một bản ghi của khối đó, bản ghi của nguồn $j$. Map phát cho cạnh này đúng một cặp $(i,r_j/d_j)$, với $r_j$ đọc từ dải $r_b$ và $d_j$ là bậc toàn cục.

**Bước 2 (danh sách của trang $i$).** Theo Mệnh đề 02.11, Reduce được gọi đúng một lần cho khóa $i$, với danh sách $L_i$ chứa mọi giá trị đi cùng $i$. Không có Combine, $L_i$ gồm cặp khởi tạo $0$ và một giá trị $r_j/d_j$ cho mỗi cạnh $j\to i$ (Bước 1), nên
$$
z_i=0+\sum_{j:\,j\to i}\frac{r_j}{d_j}=(M_0r)_i .
$$
Cặp khởi tạo bảo đảm khóa $i$ có mặt cả khi $i$ không có liên kết vào; khi đó $z_i=0$.

**Bước 3 (Combine).** Reduce có dạng $\phi(\bigoplus L_i)$ với $\oplus=+$ và $\phi(z)=\beta z+((1-\beta)+\beta\delta)/n$; Combine phát đúng một cặp $(i,\sum L)$. Theo Mệnh đề 02.15, đầu ra như khi không có Combine.

**Bước 4 (phần chung).** Theo giả thiết thứ ba, $\delta=\sum_{j\in\mathcal D}r_j$. Reduce phát $\beta(M_0r)_i+((1-\beta)+\beta\delta)/n$, đúng $F(r)_i$ của Định nghĩa 03.8. $\square$
:::

Các giả thiết của Mệnh đề 03.23 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ trên bốn trang.

- Bỏ bậc ra toàn cục: nếu bản ghi của A trong $M_{21}$ ghi bậc 2, số đích của A trong khối, thì A gửi $1/8$ thay cho $1/12$ tới C và tới D; $z_{\mathrm C}=1/8+1/8=1/4$ thay cho $5/24$, và tổng $z$ thành $13/12$.
- Bỏ "$\delta$ một lần": nếu mỗi tác vụ Map cộng điểm các nút cụt trong dải nguồn của nó, mỗi nút cụt được đếm $k$ lần, vì dải đó cấp cho $k$ khối. Trên biến thể C cụt với $k=2$ và $r^0=u$, hai tác vụ $M_{12}$, $M_{22}$ cùng cộng $r_{\mathrm C}$, nên $\delta$ thành $1/2$ thay cho $1/4$, phần chung thành $(1/5+2/5)/4=3/20$ thay cho $1/10$, và tổng điểm mới thành $\tfrac45\cdot\tfrac34+4\cdot\tfrac3{20}=6/5$.
- Bỏ cặp khởi tạo: trên đồ thị bốn trang có thêm trang E chỉ có cạnh ra $\mathrm E\to\mathrm A$, E không có liên kết vào nên không khóa nào là E, và E vắng khỏi đầu ra thay vì nhận phần chung.
- Bỏ véc-tơ $r$ cố định trong vòng: nếu tác vụ của $M_{12}$ đọc $r_{\mathrm C}$ sau khi Reduce đã ghi giá trị mới $13/60$, A nhận $z_{\mathrm A}=1/8+13/60=41/120$ và điểm $97/300$ thay cho $7/20=105/300$; kết quả phụ thuộc lịch chạy tác vụ.

Bước 1 dùng phân hoạch và bậc toàn cục; Bước 2 dùng véc-tơ cố định, cặp khởi tạo và Mệnh đề 02.11; Bước 4 dùng giả thiết về $\delta$.

::: remark Nhận xét 03.24 (Trong thực hành: chia khối)
- Mỗi tác vụ giữ trong bộ nhớ dải $r_b$ và dải tổng $z_a$, mỗi dải $n/k$ thành phần, còn khối được đọc tuần tự (MMDS, §5.2.3, tr.192). Chọn $k$ đủ lớn thì hai dải vừa bộ nhớ một máy.
- Mỗi dải điểm được gửi tới $k$ tác vụ, nên $r$ được truyền $k$ lần mỗi vòng, còn mỗi phần của ma trận chỉ được gửi một lần. Với $n=10^9$ và $m\approx10^{10}$, ma trận lưu theo Định nghĩa 03.19 cần $4{,}4\cdot10^{10}$ byte, gấp $5{,}5$ lần véc-tơ $8\cdot10^9$ byte, nên đọc véc-tơ $k$ lần làm lượng truyền tăng ít khi $k$ nhỏ (MMDS, §5.2.3, tr.192).
- Trên số thực dấu phẩy động, Combine cộng các đóng góp theo thứ tự khác với Thuật toán 03.10, nên kết quả hai cách có thể khác ở các chữ số cuối. Phép so sánh dùng dung sai.
- Mỗi vòng là một công việc MapReduce riêng; véc-tơ đầu ra của vòng này được chia dải để làm đầu vào cho vòng sau.
:::

::: exercise Bài tập 03.3 (Biểu diễn khối của đồ thị có nút cụt; MMDS Bài 5.2.3, §5.2.6, tr.195)
Đồ thị của MMDS Hình 5.3 có bốn trang và các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm D\to\mathrm B,\mathrm C$; trang C không có liên kết ra. Dùng Định nghĩa 03.21 với mỗi dải 2 trang, tức $k=2$, $V_1=\{\mathrm A,\mathrm B\}$, $V_2=\{\mathrm C,\mathrm D\}$, lập biểu diễn của bốn khối $M_{11},M_{12},M_{21},M_{22}$.
:::

::: hint
Với mỗi khối, liệt kê các cạnh có nguồn trong dải cột và đích trong dải hàng, rồi gom theo nguồn; bậc ghi trong bản ghi là bậc trên cả đồ thị.
:::

::: solution
**Bậc ra.** $d_{\mathrm A}=3$, $d_{\mathrm B}=2$, $d_{\mathrm C}=0$, $d_{\mathrm D}=2$.

**Bốn khối.**

| Khối | Cạnh | Bản ghi |
|---|---|---|
| $M_{11}$ (đích A, B; nguồn A, B) | $\mathrm A\to\mathrm B$, $\mathrm B\to\mathrm A$ | $(\mathrm A,3,[\mathrm B])$, $(\mathrm B,2,[\mathrm A])$ |
| $M_{12}$ (đích A, B; nguồn C, D) | $\mathrm D\to\mathrm B$ | $(\mathrm D,2,[\mathrm B])$ |
| $M_{21}$ (đích C, D; nguồn A, B) | $\mathrm A\to\mathrm C$, $\mathrm A\to\mathrm D$, $\mathrm B\to\mathrm D$ | $(\mathrm A,3,[\mathrm C,\mathrm D])$, $(\mathrm B,2,[\mathrm D])$ |
| $M_{22}$ (đích C, D; nguồn C, D) | $\mathrm D\to\mathrm C$ | $(\mathrm D,2,[\mathrm C])$ |

**Nút cụt C.** C không có đích nào, nên theo Định nghĩa 03.21 nó không có bản ghi trong khối nào. Thuật toán 03.22 vẫn cần điểm của C ở pha $\delta$, nên C giữ bản ghi $(\mathrm C,0,[\,])$ trong danh sách liên kết ra.

**Kiểm tra lại.** Có $2+1+2+1=6$ bản ghi khối và $1+1+1+2+1+1=7$ đích, bằng số cạnh của Hình 5.3. So với Ví dụ 03.16, chỉ khối $M_{12}$ thay đổi: mất bản ghi $(\mathrm C,1,[\mathrm A])$ của cạnh đã xóa.
:::

Một vòng theo khối trả đúng $F(r)$ (Thuật toán 03.22, Mệnh đề 03.23), với điều kiện bậc ra là bậc toàn cục, $\delta$ được tính một lần và mỗi trang có cặp khởi tạo. Cái giá của cách chia là bậc ra ghi lặp ở nhiều khối và véc-tơ được đọc $k$ lần. Trong Mục 4, chúng ta đếm cái giá đó và thời gian của pha Map trên chính bốn khối của Ví dụ 03.16.

<!-- note-topic-id: lec-03-topic-11 -->
## 4. Chi phí và lợi ích của cách tính

Nếu Map xử lý mỗi cạnh trong một đơn vị thời gian, một máy xử lý cả tám cạnh của bốn trang tốn tám đơn vị; bốn máy, mỗi máy một khối của Ví dụ 03.16, cần ba đơn vị, vì khối $M_{21}$ có ba cạnh. Con số này cùng ba đại lượng khác được đo riêng: dung lượng lưu đồ thị, bộ nhớ một tác vụ, và dữ liệu các tác vụ đọc và gửi. Mỗi đại lượng là một mô hình chi phí riêng theo Định nghĩa 01.13; thời gian pha tính theo Định nghĩa 02.30.

::: definition Định nghĩa 03.25 (Các đại lượng chi phí của một vòng)
**Mô hình byte.** Một điểm hay một giá trị đóng góp là số thực 8 byte; một mã trang hay một bậc ra là số nguyên 4 byte; một cặp trung gian $(i,x)$ gồm khóa 4 byte và giá trị 8 byte, tức 12 byte.

- **Dung lượng** $S$ là số byte của một cách lưu đồ thị trên đĩa: $S_{\text{dense}}$ cho ma trận đặc, $S_{\text{adj}}$ cho danh sách liên kết ra với mã nguồn ngầm theo thứ tự bản ghi, $S_{\text{blocks}}$ cho biểu diễn khối của Định nghĩa 03.21, trong đó mỗi bản ghi ghi mã nguồn.
- **Bộ nhớ một tác vụ** $B_{\text{task}}$ là số byte một tác vụ Map giữ trong bộ nhớ chính khi xử lý một khối; $B_{\text{buf}}$ là phần dành cho bộ đệm đọc khối.
- **Dữ liệu** của một vòng gồm $I$, $H$ và $C=I+H$ theo Định nghĩa 02.33, trong đó $H$ tính cả các cặp khởi tạo; $Q$ là số byte từ các tác vụ Map tới các tác vụ Reduce đi qua mạng, và $b_{\text{eff}}$ là băng thông của đường nối dùng chung mà mọi byte đó đi qua.
- **Thời gian.** Giả sử Map tốn $c_e$ giây cho mỗi cạnh và bỏ qua đọc ghi, truyền và lập lịch trong pha Map. **Tổng việc** pha Map là $W$ giây; $w_{\max}$ là việc của tác vụ Map nặng nhất; $T_{\text{map}}$ là thời gian pha Map trên $P$ máy theo Định nghĩa 02.30.
:::

Mỗi đại lượng có đơn vị riêng: $S$, $B_{\text{task}}$, $I$, $H$, $Q$ đo bằng byte nhưng đo những thứ khác nhau, còn $W$ và $T_{\text{map}}$ đo bằng giây. Một nhầm lẫn thường gặp là đồng nhất $H$ với $Q$: $H$ đếm mọi cặp tới Reduce, kể cả cặp tới một tác vụ Reduce trên cùng máy, còn $Q$ chỉ đếm cặp đi qua mạng.

### 4.1 Dung lượng

Ba cách lưu khác nhau ở chỗ cái gì được ghi: mọi ô, chỉ các đích, hay các đích cùng mã nguồn và bậc lặp lại ở mỗi khối.

::: proposition Mệnh đề 03.26 (Dung lượng ba cách lưu)
**Giả thiết.** Đồ thị web $G$ có $n$ trang, $m$ cạnh và $n_+$ trang không cụt; mô hình byte của Định nghĩa 03.25; biểu diễn khối với $k$ dải có $R$ bản ghi.

**Kết luận.**
$$
\begin{gathered}
S_{\text{dense}}=8n^2,\\
S_{\text{adj}}=4(n+m),\\
S_{\text{blocks}}=8R+4m,
\end{gathered}
$$
và $n_+\le R\le\min(kn_+,m)$.

**Điều kiện áp dụng.** Không tính phần đầu tệp, chỉ mục hay nén.

**Phạm vi.** Mệnh đề đếm byte lưu trữ, không nói thời gian đọc.
:::

::: proof
**Bước 1 (ma trận đặc).** Có $n^2$ ô, mỗi ô 8 byte.

**Bước 2 (danh sách liên kết ra).** Mỗi trang có một bản ghi gồm bậc ra 4 byte, kể cả nút cụt với bậc 0, và một mã 4 byte cho mỗi đích. Mã nguồn suy ra từ thứ tự bản ghi. Tổng số đích là $\sum_jd_j=m$, nên $S_{\text{adj}}=4n+4m$.

**Bước 3 (biểu diễn khối).** Mỗi bản ghi khối ghi mã nguồn và bậc, 8 byte, cộng 4 byte cho mỗi đích trong khối. Theo Bước 1 của chứng minh Mệnh đề 03.23, mỗi cạnh nằm trong đúng một bản ghi, nên tổng số đích là $m$ và $S_{\text{blocks}}=8R+4m$.

**Bước 4 (số bản ghi).** Một nguồn không cụt $j$ có ít nhất một đích, nên có ít nhất một bản ghi; nó có bản ghi trong khối $M_{ab}$ với $b$ là dải của $j$ chỉ khi có đích trong $V_a$, nên có không quá $\min(k,d_j)$ bản ghi. Nút cụt không có bản ghi khối. Cộng theo nguồn:
$$
\begin{aligned}
n_+\le R&\le\sum_{j\notin\mathcal D}\min(k,d_j)\\
&\le\min\Big(kn_+,\ \sum_jd_j\Big)\\
&=\min(kn_+,m).\ \square
\end{aligned}
$$
:::

$S_{\text{dense}}$ tăng theo bình phương số trang, còn $S_{\text{adj}}$ tăng theo số trang cộng số liên kết; tỷ số $S_{\text{dense}}/S_{\text{adj}}=2n^2/(n+m)$ lớn khi $m$ nhỏ hơn nhiều so với $n^2$. Khi $m$ lớn hơn nhiều so với $n$, $S_{\text{adj}}$ chỉ hơn 4 byte cho mỗi phần tử khác 0 một chút, đúng như MMDS (§5.2.1, tr.190). Biểu diễn khối tốn thêm ở chỗ một nguồn có thể có bản ghi ở nhiều khối; số lần lặp của bậc ra không vượt quá chính bậc ra (MMDS, §5.2.4, tr.192–193), đúng bất đẳng thức $\min(k,d_j)\le d_j$ của Bước 4.

::: example Ví dụ 03.19 (Dung lượng trên bốn trang)
**Dữ kiện.** Đồ thị của Ví dụ 03.2: $n=4$, $m=8$, $n_+=4$; biểu diễn khối của Ví dụ 03.16 với $k=2$ có $R=7$ bản ghi.

**Tính.**

- $S_{\text{dense}}=8\cdot4^2=128$ byte.
- $S_{\text{adj}}=4\cdot(4+8)=48$ byte.
- $S_{\text{blocks}}=8\cdot7+4\cdot8=56+32=88$ byte.

**Kiểm tra lại.** $128/48=8/3=2\cdot16/12$, đúng $2n^2/(n+m)$; $R=7$ nằm giữa $n_+=4$ và $\min(kn_+,m)=\min(8,8)=8$. Biểu diễn khối tốn thêm $88-48=40$ byte vì A, B, D có bản ghi ở hai khối và mỗi bản ghi khối ghi mã nguồn.
:::

Trên bốn trang, ma trận gần như đặc, $8$ trong $16$ ô khác 0, nên lợi ích của danh sách liên kết ra chỉ là $128/48=8/3$ lần.

Hai cách ghi của Mệnh đề 03.26 quyết định con số trên bốn trang:

- Bỏ mã nguồn ngầm theo thứ tự bản ghi: mỗi bản ghi ghi thêm mã nguồn 4 byte, và danh sách liên kết ra cần $4(2n+m)=64$ byte thay cho 48.
- Bỏ điều kiện các dải rời nhau của Định nghĩa 03.21: với $V_1=\{\mathrm A,\mathrm B,\mathrm C\}$, $V_2=\{\mathrm C,\mathrm D\}$, cạnh $\mathrm A\to\mathrm C$ nằm trong cả $M_{11}$ lẫn $M_{21}$, nên tổng số đích ghi trong các khối lớn hơn $m$.

Bước 2 của chứng minh dùng mã nguồn ngầm; Bước 3 dùng các dải rời nhau.

<!-- note-topic-id: lec-03-topic-12 -->
### 4.2 Bộ nhớ một tác vụ và đầu vào Map

Một tác vụ Map của Thuật toán 03.22 đọc khối của nó tuần tự qua bộ đệm, nhưng phải giữ cả dải điểm $r_b$ để tra $r_j$ và dải tổng $z_a$ để Combine cộng dồn.

::: proposition Mệnh đề 03.27 (Bộ nhớ và đầu vào Map của một vòng theo khối)
**Giả thiết.** Mô hình byte của Định nghĩa 03.25; $k$ chia hết $n$ và mỗi dải có $n/k$ trang; mỗi tác vụ Map xử lý một khối, giữ $r_b$ và $z_a$ trong bộ nhớ và đọc khối qua bộ đệm $B_{\text{buf}}$ byte.

**Kết luận.**
$$
\begin{gathered}
B_{\text{task}}=\frac{16n}{k}+B_{\text{buf}},\\
I=S_{\text{blocks}}+8kn .
\end{gathered}
$$

**Điều kiện áp dụng.** $I$ chỉ đếm $k^2$ tác vụ Map của Thuật toán 03.22; pha $\delta$, cặp khởi tạo và bước tính $\Delta$ không được tính.

**Phạm vi.** $B_{\text{task}}$ là bộ nhớ làm việc của một tác vụ, không phải bộ nhớ của cả máy hay cả cụm.
:::

::: proof
**Bước 1 (bộ nhớ).** Hai dải $r_b$ và $z_a$, mỗi dải $n/k$ số thực 8 byte, chiếm $2\cdot8n/k=16n/k$ byte; cộng bộ đệm được $B_{\text{task}}$.

**Bước 2 (phần ma trận của $I$).** Mỗi khối là đầu vào của đúng một tác vụ, nên tổng phần ma trận là $S_{\text{blocks}}$.

**Bước 3 (phần véc-tơ của $I$).** Dải $r_b$, $8n/k$ byte, là đầu vào của $k$ tác vụ $M_{1b},\ldots,M_{kb}$. Có $k$ dải, nên phần véc-tơ là $k\cdot k\cdot8n/k=8kn$ byte, tức $r$ được đọc $k$ lần. Theo Định nghĩa 02.33, $I$ là tổng hai phần. $\square$
:::

$k$ tạo ra một đánh đổi: tăng $k$ làm $B_{\text{task}}$ giảm theo $1/k$ nhưng làm phần véc-tơ của $I$ tăng theo $k$. Cận trên $\min(kn_+,m)$ của $R$ cũng tăng theo $k$. MMDS chọn $k$ nhỏ nhất sao cho một phần $k$ của $r$ và một phần $k$ của véc-tơ kết quả vừa bộ nhớ (§5.2.5, tr.193–194), tức $k$ nhỏ nhất để $B_{\text{task}}$ không vượt bộ nhớ có sẵn.

::: example Ví dụ 03.20 (Bộ nhớ và đầu vào Map với $n=4$, $k=2$)
**Dữ kiện.** Bốn khối của Ví dụ 03.16; $n=4$, $k=2$, mỗi dải 2 trang; $S_{\text{blocks}}=88$ byte theo Ví dụ 03.19.

**Bộ nhớ.** $B_{\text{task}}=16\cdot4/2+B_{\text{buf}}=32$ byte cộng $B_{\text{buf}}$.

**Đầu vào từng tác vụ.**

| Tác vụ | Bản ghi (mã nguồn, bậc) | Mã đích | Dải điểm | Tổng |
|---|---|---|---|---|
| $M_{11}$ | $2\cdot8=16$ | $2\cdot4=8$ | $16$ | $40$ |
| $M_{12}$ | $2\cdot8=16$ | $2\cdot4=8$ | $16$ | $40$ |
| $M_{21}$ | $2\cdot8=16$ | $3\cdot4=12$ | $16$ | $44$ |
| $M_{22}$ | $1\cdot8=8$ | $1\cdot4=4$ | $16$ | $28$ |
| Cộng | $56$ | $32$ | $64$ | $152$ |

**Kiểm tra lại.** Phần ma trận $56+32=88=S_{\text{blocks}}$; phần véc-tơ $64=8\cdot2\cdot4=8kn$; $I=152$ byte.
:::

![Khối ma trận trên đĩa được đọc tuần tự qua bộ đệm B_buf; phép tính dùng dải điểm vào r_b và cộng dồn vào dải tích lũy z_a; mỗi dải n/k giá trị.](img/lec-03/cost-memory.svg)

Hình tách ba phần bộ nhớ của một tác vụ: bộ đệm chỉ giữ một phần nhỏ của khối, còn hai dải phải nằm trọn trong bộ nhớ. Đó là lý do $B_{\text{task}}$ phụ thuộc $n/k$ mà không phụ thuộc kích thước khối.

Hai giả thiết của Mệnh đề 03.27 có vai trò riêng.

- Bỏ "$k$ chia hết $n$": với $n=4$, $k=3$, các dải có 2, 1, 1 trang; tác vụ có dải 2 trang cần $32$ byte cộng $B_{\text{buf}}$, lớn hơn $16n/k\approx21{,}3$ byte, và bộ nhớ của tác vụ lớn nhất là $16\max_b\lvert V_b\rvert+B_{\text{buf}}$, bằng $16\lceil n/k\rceil+B_{\text{buf}}$ khi các dải chênh nhau không quá một trang.
- Bỏ "giữ $r_b$ và $z_a$ trong bộ nhớ": tác vụ phải đưa phần của $z_a$ từ đĩa vào bộ nhớ cho gần như mỗi số hạng, hiện tượng đọc ghi lặp của Nhận xét 03.20, và $B_{\text{task}}$ không còn là bộ nhớ của tác vụ.

Bước 1 của chứng minh dùng cả hai giả thiết; Bước 3 dùng việc mỗi khối nhận đúng dải điểm của cột khối của nó.

### 4.3 Combine, đầu vào Reduce và dữ liệu qua mạng

Ví dụ 03.17 cho thấy Combine thay hai cặp cùng khóa D của $M_{21}$ bằng một cặp. Mệnh đề sau đếm lượng đó cho mọi khối.

::: proposition Mệnh đề 03.28 (Đầu vào Reduce của một vòng theo khối)
**Giả thiết.** Mô hình byte của Định nghĩa 03.25; Thuật toán 03.22 với Combine gọi một lần cho mỗi khóa trên toàn bộ đầu ra của mỗi tác vụ Map; $q$ là số tổ hợp (khối, đích) sao cho khối có ít nhất một cạnh tới đích đó.

**Kết luận.**

- (a) Không có Combine, các tác vụ Map gửi $m$ cặp; có Combine, chúng gửi $q$ cặp, với $q\le m$.
- (b) Tính cả $n$ cặp khởi tạo, $H=12(m+n)$ byte không có Combine và $H=12(q+n)$ byte có Combine.
- (c) $Q\le H$, và pha chuyển dữ liệu trung gian kéo dài $T_{\text{shuffle}}\ge Q/b_{\text{eff}}$ giây.

**Điều kiện áp dụng.** Không nén, không chạy lại tác vụ; mọi byte của $Q$ đi qua một đường nối dùng chung có băng thông $b_{\text{eff}}$.

**Phạm vi.** Mệnh đề không cho giá trị của $Q$; $Q$ phụ thuộc vị trí các tác vụ Reduce.
:::

::: proof
**Bước 1 (không Combine).** Map phát một cặp cho mỗi cạnh (Bước 1 của chứng minh Mệnh đề 03.23), tức $m$ cặp 12 byte.

**Bước 2 (có Combine).** Trong một tác vụ, Combine thay mọi cặp cùng khóa $i$ bằng một cặp, nên tác vụ của $M_{ab}$ gửi một cặp cho mỗi đích có ít nhất một cạnh trong khối. Cộng trên các khối được $q$ cặp. Mỗi tổ hợp (khối, đích) ứng với ít nhất một cạnh, và mỗi cạnh ứng với đúng một tổ hợp (khối, đích), nên $q\le m$.

**Bước 3 (cặp khởi tạo).** Mỗi trang có một cặp $(i,0)$ 12 byte đi tới Reduce, không qua Combine; cộng với Bước 1 và Bước 2 được (b).

**Bước 4 (mạng).** Mỗi byte đi qua mạng từ Map tới Reduce là một byte của đầu vào Reduce, nên $Q\le H$. Theo điều kiện áp dụng, mọi byte của $Q$ đi qua một đường nối dùng chung có băng thông $b_{\text{eff}}$, nên theo Mệnh đề 02.38, việc chuyển chúng cần ít nhất $Q/b_{\text{eff}}$ giây. $\square$
:::

::: example Ví dụ 03.21 (Combine trên bốn trang)
**Dữ kiện.** Bốn khối của Ví dụ 03.16; $I=152$ byte theo Ví dụ 03.20.

**Đếm cặp.** Không có Combine: $m=8$ cặp. Có Combine: $M_{11}$ có đích A, B; $M_{12}$ có A, B; $M_{21}$ có C, D; $M_{22}$ có C; vậy $q=2+2+2+1=7$, vì chỉ $M_{21}$ có hai cạnh cùng đích D.

**Byte.**

| Phương án | Cặp từ Map | Cặp khởi tạo | $H$ | $C=I+H$ |
|---|---|---|---|---|
| Không Combine | 8 | 4 | $12\cdot12=144$ | $296$ |
| Có Combine | 7 | 4 | $11\cdot12=132$ | $284$ |

**Mạng.** $Q$ nằm giữa 0 và $H=132$ byte. Giả sử 7 cặp sau Combine đều đi qua mạng, còn 4 cặp khởi tạo được tạo trên máy chạy tác vụ Reduce nhận chúng; khi đó $Q=7\cdot12=84$ byte và $T_{\text{shuffle}}\ge84/b_{\text{eff}}$ giây.

**Kiểm tra lại.** Combine giảm $H$ đi $12$ byte, tức $12/144=1/12$ của $H$, và giảm $C$ đi $12/296\approx4{,}1\%$.
:::

![Bản ghi sau Combine trên máy 1 có thể tới Reduce cùng máy theo nhánh cục bộ, hoặc qua mạng tới Reduce trên máy 2; chỉ nhánh qua mạng góp vào Q.](img/lec-03/visual-network.svg)

Hình cho thấy vì sao dữ kiện của ví dụ không xác định $Q$: cùng một cặp góp vào $H$ trong cả hai nhánh, nhưng chỉ góp vào $Q$ khi đi qua mạng.

Mệnh đề 03.28 dựa vào cách gọi Combine và đường nối dùng chung:

- Bỏ "Combine gọi một lần cho mỗi khóa trên toàn bộ đầu ra của tác vụ": nếu Combine trong tác vụ $M_{21}$ chỉ được gọi trên từng cặp riêng lẻ, nó không gộp được gì, nên $q=8$ và $H=144$ thay cho $132$ byte.
- Bỏ "mọi byte của $Q$ đi qua một đường nối": nếu 84 byte của ví dụ chia đều cho hai đường nối riêng, mỗi đường băng thông $b_{\text{eff}}$, cận dưới chỉ còn $42/b_{\text{eff}}$ giây.

Bước 2 của chứng minh dùng cách gọi Combine; Bước 4 dùng đường nối dùng chung.

<!-- note-topic-id: lec-03-topic-13 -->
### 4.4 Thời gian của pha Map

Ba đơn vị ở đầu Mục 4, thay cho hai đơn vị nếu bốn máy chia đều tám cạnh, là trường hợp riêng của cận dưới sau.

::: proposition Mệnh đề 03.29 (Cận dưới thời gian pha Map)
**Giả thiết.** Mô hình thời gian của Định nghĩa 03.25; $k^2$ tác vụ Map, tác vụ của khối $M_{ab}$ có $m_{ab}$ cạnh; các tác vụ được giao nguyên vẹn cho $P\ge1$ máy giống nhau.

**Kết luận.** $W=mc_e$ không phụ thuộc $P$, và
$$
\begin{gathered}
T_{\text{map}}\ge\max\Big(\frac{W}{P},\ w_{\max}\Big),\\
w_{\max}=c_e\max_{a,b}m_{ab}.
\end{gathered}
$$

**Điều kiện áp dụng.** Mọi tác vụ sẵn sàng từ đầu pha, như Định nghĩa 02.30.

**Phạm vi.** Cận dưới; một lịch cụ thể có thể chậm hơn.
:::

::: proof
**Bước 1 (tổng việc).** Mỗi cạnh nằm trong đúng một khối (Mệnh đề 03.23, Bước 1), nên $\sum_{a,b}m_{ab}=m$ và $W=mc_e$ với mọi cách giao.

**Bước 2 (trung bình).** Theo Định nghĩa 02.30, $T_{\text{map}}=\max_\nu t_\nu$, với $\sum_\nu t_\nu=W$. Giá trị lớn nhất của $P$ số không nhỏ hơn trung bình của chúng, nên $T_{\text{map}}\ge W/P$.

**Bước 3 (tác vụ nặng nhất).** Máy nhận tác vụ có $\max m_{ab}$ cạnh có $t_\nu\ge w_{\max}$, nên $T_{\text{map}}\ge w_{\max}$. $\square$
:::

::: example Ví dụ 03.22 (Thời gian pha Map trên bốn khối)
**Dữ kiện.** Bốn khối của Ví dụ 03.16 có $m_{11}=2$, $m_{12}=2$, $m_{21}=3$, $m_{22}=1$ cạnh.

**Một máy.** $W=8c_e$ và $T_{\text{map}}=8c_e$.

**Bốn máy, mỗi máy một khối.** $T_{\text{map}}=\max(2,2,3,1)c_e=3c_e$. Mức tăng tốc của pha Map theo Định nghĩa 02.39 là $8c_e/3c_e=8/3$, nhỏ hơn 4.

**Hai máy.** Giao $M_{21}$, $M_{22}$ cho máy 1 và $M_{11}$, $M_{12}$ cho máy 2: $t_1=(3+1)c_e=4c_e$, $t_2=(2+2)c_e=4c_e$, nên $T_{\text{map}}=4c_e$.

**Kiểm tra lại.** Với $P=4$, cận của Mệnh đề 03.29 là $\max(2c_e,3c_e)=3c_e$; với $P=2$, cận là $\max(4c_e,3c_e)=4c_e$. Cả hai lịch đạt đúng cận dưới.
:::

![Hàng trên: một máy làm bốn khối nối tiếp 2, 2, 3, 1 đơn vị c_e, tổng 8. Bốn hàng dưới: bốn máy, mỗi máy một khối, cùng bắt đầu; máy chạy M₂₁ kết thúc cuối cùng, sau 3c_e.](img/lec-03/cost-timeline.svg)

Trên hình, ba máy rảnh trước khi máy chạy $M_{21}$ xong: khối nặng nhất quyết định thời gian pha. Thêm máy quá $P=W/w_{\max}$, ở đây $8/3$, không giảm cận dưới thêm nữa, trừ khi khối nặng được chia nhỏ, tức tăng $k$.

Mệnh đề 03.29 dùng hai giả thiết về cách giao tác vụ:

- Bỏ "giao nguyên vẹn": nếu ba cạnh của $M_{21}$ được chia cho hai máy, bốn máy có thể nhận 2, 2, 2, 2 cạnh và xong sau $2c_e=W/P$; cận $w_{\max}=3c_e$ không còn đúng.
- Bỏ "mọi tác vụ sẵn sàng từ đầu pha": nếu tác vụ $M_{22}$ chỉ sẵn sàng sau $3c_e$, bốn máy xong sau $4c_e$, lớn hơn cận $3c_e$; mệnh đề vẫn cho cận dưới nhưng cận không còn đạt được.

Bước 3 của chứng minh dùng giả thiết giao nguyên vẹn.

::: remark Nhận xét 03.30 (Trong thực hành: thời gian một vòng và cả công việc)
- Một vòng gồm các pha nối tiếp; khi các pha không chồng nhau,
$$
\begin{aligned}
T_{\text{round}}&\approx T_\delta+T_{\text{map}}\\
&\quad+T_{\text{shuffle}}+T_{\text{reduce}}\\
&\quad+T_{\text{sync}},
\end{aligned}
$$
với $T_{\text{sync}}$ là thời gian tổng hợp $\Delta$ và đồng bộ trước vòng sau. Nếu pha $\delta$ chạy cùng lúc với Map, thay $T_\delta+T_{\text{map}}$ bằng $\max(T_\delta,T_{\text{map}})$.
- Cả công việc chạy $t_{\text{dừng}}$ vòng: $T_{\text{job}}=T_{\text{setup}}+\sum_{t=1}^{t_{\text{dừng}}}T_{\text{round},t}$. Số vòng phụ thuộc $\tau$ và đồ thị; Hệ quả 03.16 cho $\tau$ ứng với sai số cần đạt.
- Thêm máy giảm $T_{\text{map}}$ tới cận $w_{\max}$, nhưng không giảm $T_{\text{setup}}$ hay $T_{\text{sync}}$; khi các tác vụ Reduce nằm trên máy khác các tác vụ Map gửi cặp cho chúng, các cặp đó góp vào $Q$ và kéo dài $T_{\text{shuffle}}$.
:::

::: exercise Bài tập 03.4 (Biểu diễn khối của một chuỗi; MMDS Bài 5.2.4, §5.2.6, tr.195)
Đồ thị web là một chuỗi $n\ge2$ trang như MMDS Hình 5.9 (tr.189): trang 1 có khuyên $1\to1$ và cạnh $1\to2$; với $2\le i\le n-1$, trang $i$ có đúng một cạnh $i\to i+1$; trang $n$ không có liên kết ra. Giả sử $k$ chia hết $n$ và dải $b$ gồm các trang $(b-1)n/k+1,\ldots,bn/k$. Mô tả biểu diễn khối của Định nghĩa 03.21 theo $k$: khối nào khác rỗng và mỗi khối chứa bản ghi nào.
:::

![Chuỗi trang 1, 2, 3, …, n từ trái sang phải; trang 1 có khuyên về chính nó; mỗi trang i trỏ tới trang i + 1; trang n ở cuối không có mũi tên đi ra.](img/lec-03/note-hinh-5-9.svg)

::: hint
Một cạnh $i\to i+1$ nằm trong khối chéo $M_{bb}$ khi $i$ và $i+1$ cùng dải, và nằm trong $M_{b+1,b}$ khi $i$ là trang cuối của dải $b$.
:::

::: solution
**Bậc ra.** $d_1=2$; $d_i=1$ với $2\le i\le n-1$; $d_n=0$. Số cạnh là $m=2+(n-2)=n$.

**Khối chứa từng cạnh.**

- Khuyên $1\to1$ có nguồn và đích ở dải 1, nên thuộc $M_{11}$.
- Cạnh $i\to i+1$ với $i$ không phải trang cuối của một dải có $i$ và $i+1$ cùng dải $b$, nên thuộc khối chéo $M_{bb}$.
- Cạnh $bn/k\to bn/k+1$ với $1\le b\le k-1$ đi từ trang cuối của dải $b$ sang trang đầu của dải $b+1$, nên thuộc $M_{b+1,b}$.

Vậy chỉ $2k-1$ khối có thể khác rỗng: $k$ khối chéo $M_{bb}$ và $k-1$ khối $M_{b+1,b}$ ngay dưới đường chéo. Trang $n$ là nút cụt, không có bản ghi khối nào. Nội dung các khối chia hai trường hợp.

- Khi $n/k\ge2$: $M_{11}$ có bản ghi $(1,2,[1,2])$ và các bản ghi $(i,1,[i+1])$ của các trang khác của dải 1 trừ trang cuối; mỗi $M_{bb}$ với $b\ge2$ có $n/k-1$ bản ghi $(i,1,[i+1])$, một cho mỗi trang của dải $b$ trừ trang cuối; mỗi $M_{b+1,b}$ có đúng một bản ghi $(bn/k,1,[bn/k+1])$.
- Khi $k=n$, mỗi dải có một trang: $M_{11}$ có bản ghi $(1,2,[1])$; $M_{21}$ có $(1,2,[2])$; mỗi $M_{b+1,b}$ với $b\ge2$ có $(b,1,[b+1])$; các khối chéo $M_{bb}$ với $b\ge2$ rỗng.

**Số bản ghi và dung lượng.** Trang 1 có hai đích. Khi $n/k\ge2$, hai đích cùng ở dải 1, nên mỗi trang không cụt có đúng một bản ghi và $R=n_+=n-1$. Khi $k=n$, trang 1 có hai bản ghi, trong $M_{11}$ và $M_{21}$, nên $R=n$. Theo Mệnh đề 03.26, $S_{\text{blocks}}=8R+4m$ cho $8(n-1)+4n$ và $8n+4n$:
$$
S_{\text{blocks}}=\begin{cases}12n-8,&n/k\ge2,\\12n,&k=n,\end{cases}
$$
trong khi $S_{\text{adj}}=4(n+m)=8n$.

**Kiểm tra lại.** Với $n=4$, $k=2$: dải $\{1,2\}$, $\{3,4\}$; $M_{11}$ có $(1,2,[1,2])$; $M_{21}$ có $(2,1,[3])$; $M_{22}$ có $(3,1,[4])$; $M_{12}$ rỗng. Vậy $R=3=n-1$, tổng số đích $2+1+1=4=m$ và $S_{\text{blocks}}=24+16=40=12\cdot4-8$. Khi $n/k\ge2$, $R$ không phụ thuộc $k$, và $S_{\text{blocks}}-S_{\text{adj}}=4n-8=4R-4$: mỗi bản ghi khối thêm 4 byte mã nguồn, còn biểu diễn khối không lưu bậc 0 của nút cụt $n$.
:::

Như vậy, cách chia khối đổi bộ nhớ một tác vụ $16n/k$ byte lấy việc đọc véc-tơ $k$ lần (Mệnh đề 03.27), Combine giảm đầu vào Reduce từ $12(m+n)$ xuống $12(q+n)$ byte (Mệnh đề 03.28), và thời gian pha Map không thấp hơn tác vụ nặng nhất (Mệnh đề 03.29); trên bốn trang, $I=152$, $H$ từ 144 còn 132 byte và $T_{\text{map}}=3c_e$ trên bốn máy. Các phép đếm này và các nghiệm của Mục 2 dùng số học chính xác; Mục 5 kiểm các nghiệm của Mục 2 trên số thực dấu phẩy động.

<!-- note-topic-id: lec-03-topic-14 -->
<!-- note-collapsed -->
## Đọc thêm: Loại nút cụt đệ quy

Chúng ta đã xử lý nút cụt bằng cách đổi mô hình: phần $\beta$ của nút cụt được chia đều (Định nghĩa 03.8). MMDS nêu thêm một cách xử lý bằng cách đổi dữ liệu: xóa nút cụt khỏi đồ thị, tính PageRank trên phần còn lại, rồi tính điểm cho các nút đã xóa (§5.1.4, tr.183–185). Xóa một nút cụt có thể biến nguồn của nó thành nút cụt mới, nên phép xóa phải lặp.

::: algorithm Thuật toán 03.31 (Loại nút cụt đệ quy và khôi phục điểm)
**Đầu vào.** Đồ thị web $G=(V,E)$ với bậc ra $d_p$ trên $G$ và, cho mỗi trang, danh sách các trang trỏ tới nó; một phương pháp tính PageRank cho đồ thị không có nút cụt.

**Đầu ra.** Một điểm $\hat r_v\ge0$ cho mỗi trang $v\in V$.

1. Đặt $G'\leftarrow G$ và danh sách xóa $X\leftarrow(\,)$ rỗng.
2. Trong khi $G'$ có nút cụt: chọn một nút cụt $v$ của $G'$, xóa $v$ cùng mọi cạnh vào $v$ khỏi $G'$, và nối $v$ vào cuối $X$.
3. Tính PageRank $\hat r$ của $G'$ bằng phương pháp đã chọn.
4. Duyệt $X$ theo thứ tự ngược: với mỗi $v$, đặt $\hat r_v\leftarrow\sum_{p:\,p\to v}\hat r_p/d_p$, tổng trên các nguồn $p$ của $v$ trong $G$, với $d_p$ là bậc ra trên $G$.

**Dừng.** Mỗi lần lặp của bước 2 xóa một nút, nên bước 2 lặp không quá $n$ lần.

**Trường hợp biên.** Một nút có khuyên không bao giờ thành nút cụt. Nếu $G'$ rỗng, chẳng hạn khi $G$ không có chu trình, bước 3 không cho điểm nào và mọi điểm khôi phục bằng 0.

**Chi phí.** Bước 2 giữ bậc ra hiện thời của mỗi nút và một hàng đợi các nút cụt. Mô hình đếm số lần thực hiện thân vòng lặp, không kể bước 3:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1 (bậc hiện thời, hàng đợi) | $n$ trang | 1 | $n$ |
| 2 (lấy nút cụt khỏi hàng đợi) | không quá $n$ nút | 1 | $\le n$ |
| 2 (xóa cạnh vào) | không quá $m$ cạnh | giảm bậc của nguồn; thêm nguồn vào hàng đợi khi bậc về 0 | $\le m$ |
| 4 (khôi phục) | không quá $m$ cạnh vào nút đã xóa | một phép chia, một phép cộng | $\le m$ |

Tổng là $O(n+m)$ thao tác cộng chi phí của bước 3.
:::

Bước 4 dùng được vì thứ tự xóa: khi $v$ bị xóa, mọi nguồn $p$ của $v$ còn cạnh $p\to v$, nên $p$ chưa là nút cụt và bị xóa sau $v$ hoặc ở lại $G'$. Duyệt ngược, mọi nguồn của $v$ đã có điểm khi tới lượt $v$ (MMDS, §5.1.4, tr.184). Bậc ra dùng ở bước 4 là bậc trên $G$, vì nguồn $p$ chia điểm cho mọi đích của nó, kể cả các đích đã bị xóa.

::: example Ví dụ 03.23 (Hai mức nút cụt; MMDS Ví dụ 5.4)
**Dữ kiện.** Đồ thị của MMDS Hình 5.4 (tr.184): $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm E$; $\mathrm D\to\mathrm B,\mathrm C$; E không có liên kết ra. Trên $G$, $d_{\mathrm A}=3$, $d_{\mathrm C}=1$, $d_{\mathrm D}=2$.

**Xóa.** E là nút cụt; xóa E và cạnh $\mathrm C\to\mathrm E$. Khi đó C thành nút cụt; xóa C và các cạnh $\mathrm A\to\mathrm C$, $\mathrm D\to\mathrm C$. Còn lại $G'$ gồm A, B, D với $\mathrm A\to\mathrm B,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm D\to\mathrm B$, không có nút cụt; $X=(\mathrm E,\mathrm C)$.

**PageRank của $G'$.** Lặp thô từ $(1/3,1/3,1/3)$ theo thứ tự A, B, D cho $(1/6,1/2,1/3)$, $(1/4,5/12,1/3)$, $(5/24,11/24,1/3)$ và hội tụ tới $(2/9,4/9,3/9)$ (MMDS, tr.184).

**Khôi phục.** Duyệt ngược $X$: C trước, rồi E.

- C có nguồn A, D trên $G$: $\hat r_{\mathrm C}=\tfrac13\cdot\tfrac29+\tfrac12\cdot\tfrac39=\tfrac4{54}+\tfrac9{54}=\tfrac{13}{54}$.
- E có nguồn C với $d_{\mathrm C}=1$: $\hat r_{\mathrm E}=\tfrac{13}{54}$.

**Kiểm tra lại.** Trên $G'$, hàng B: $\hat r_{\mathrm A}/2+\hat r_{\mathrm D}=\tfrac19+\tfrac39=\tfrac49$. Tổng năm điểm là $\tfrac29+\tfrac49+\tfrac39+2\cdot\tfrac{13}{54}=1+\tfrac{13}{27}=\tfrac{40}{27}>1$.
:::

![Bên trái: đồ thị Hình 5.4 với năm trang A, B, C, D, E; A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới E; D trỏ tới B, C; E không có cạnh ra. Mũi tên ở giữa ghi xóa E, rồi xóa C. Bên phải: đồ thị rút gọn Hình 5.5 gồm A, B, D; A trỏ tới B, D; B trỏ tới A, D; D trỏ tới B.](img/lec-03/note-loai-nut-cut.svg)

Hình đặt hai đồ thị cạnh nhau: sau hai lần xóa, A mất cạnh tới C nên có hai đích trên $G'$, còn D chỉ còn một đích. Bước khôi phục vẫn dùng $d_{\mathrm A}=3$ và $d_{\mathrm D}=2$ của đồ thị bên trái.

::: remark Nhận xét 03.32 (So với quy tắc bù nút cụt)
Điểm khôi phục của Ví dụ 03.23 có tổng $40/27$, nên chúng không còn là phân phối của người lướt; MMDS vẫn coi chúng là ước lượng chấp nhận được của tầm quan trọng tương đối (§5.1.4, tr.185). Quy tắc của Định nghĩa 03.8 giữ tổng bằng 1 (Mệnh đề 03.13) và áp dụng được trực tiếp cho đồ thị có nút cụt. Phép xóa cũng không xử lý bẫy: các SCC nhỏ trong thành phần ra, kể cả bẫy, không bị xóa (MMDS, chú thích 4, tr.183), nên $G'$ vẫn cần bước nhảy ở bước 3.
:::

::: exercise Bài tập 03.5 (Chuỗi nút cụt, phần đọc thêm; MMDS Bài 5.1.6, §5.1.7, tr.189)
Đồ thị là chuỗi $n\ge1$ trang như MMDS Hình 5.9: trang 1 có khuyên $1\to1$; khi $n\ge2$, trang 1 còn có cạnh $1\to2$, trang $i$ có cạnh $i\to i+1$ với $2\le i\le n-1$, và trang $n$ không có liên kết ra. Áp Thuật toán 03.31: loại nút cụt đệ quy, tính PageRank của đồ thị còn lại, rồi khôi phục điểm của các trang đã xóa. Xác định điểm của mỗi trang.
:::

::: hint
Xác định thứ tự xóa bắt đầu từ trang $n$, rồi xét đồ thị một trang có khuyên còn lại.
:::

::: solution
**Xóa.** Trang $n$ là nút cụt duy nhất; xóa nó làm trang $n-1$ thành nút cụt, và cứ thế. Thứ tự xóa là $X=(n,n-1,\ldots,2)$. Trang 1 còn khuyên nên không bị xóa; $G'$ là một trang với khuyên $1\to1$.

**PageRank của $G'$.** Ma trận liên kết của $G'$ là $(1)$, và phân phối duy nhất trên một trang là $\hat r_1=1$.

**Khôi phục.** Duyệt ngược $X$, tức $2,3,\ldots,n$.

- Trang 2 có nguồn duy nhất là trang 1, với $d_1=2$ trên $G$: $\hat r_2=1/2$.
- Với $3\le i\le n$, trang $i$ có nguồn duy nhất $i-1$ với $d_{i-1}=1$: $\hat r_i=\hat r_{i-1}=1/2$.

Vậy trang 1 có điểm 1 và mọi trang $2,\ldots,n$ có điểm $1/2$.

**Kiểm tra lại.** Tổng là $1+(n-1)/2$: bằng 1 khi $n=1$, đồ thị chỉ có trang 1, và lớn hơn 1 khi $n\ge2$, đúng như Nhận xét 03.32. Dùng $d_1=1$ trên $G'$ thay cho $d_1=2$ sẽ cho trang 2 điểm 1, sai bước 4 của Thuật toán 03.31.
:::

<!-- note-topic-id: lec-03-topic-15 -->
## 5. Thực hành tính PageRank

Ba đồ thị của MMDS, đồ thị gốc Hình 5.1, biến thể C cụt Hình 5.3 và biến thể bẫy C Hình 5.6, đã có nghiệm tính tay ở Mục 2. Một chương trình chạy Thuật toán 03.10 trên số thực dấu phẩy động phải cho cùng các con số đó, sai khác không quá ngưỡng đã chọn. Mã thực hành [pagerank.py](materials/lec-03/code/pagerank.py), kèm [hướng dẫn chạy](materials/lec-03/code/practice-README.md), cài đặt Thuật toán 03.10 bằng Python 3, chỉ dùng thư viện chuẩn (`argparse`, `json`, `math`, `sys`).

### 5.1 Dữ liệu và một vòng cập nhật

Đồ thị là một từ điển từ tên trang tới danh sách đích, đúng danh sách liên kết ra của Ví dụ 03.14 với bậc ra là độ dài danh sách:

```python
adj = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B", "C"],
}
```

Hàm `pagerank(adj, beta=0.8, tol=1e-8, max_iter=100)` trả về một từ điển gồm `rank` (điểm từng trang), `converged` (đạt ngưỡng hay không), `iterations` (số vòng) và `delta` (độ thay đổi cuối). Hàm kiểm đầu vào: $n\ge1$, mọi đích là một khóa của từ điển, $0<\beta<1$, `tol` dương và `max_iter` nguyên dương; cạnh trùng được gộp trong một bản sao, nên dữ liệu vào không bị sửa. Hàm `step` thực hiện một vòng của Định nghĩa 03.8:

```python
def step(adj, r, beta):
    n = len(adj)
    delta = sum(r[j] for j in adj if not adj[j])
    common = (1.0 - beta + beta * delta) / n
    new = {i: common for i in adj}
    for j, targets in adj.items():
        if not targets:
            continue
        share = beta * r[j] / len(targets)
        for i in targets:
            new[i] += share
    return new
```

::: remark Nhận xét 03.33 (Từ Thuật toán 03.10 tới `pagerank.py`)
- Dòng `delta = ...` của `step` là bước 2, tính $\delta$ từ véc-tơ cũ; dòng `common` và từ điển `new` là bước 3; vòng `for` lồng là bước 4, với `share` $=\beta r_j/d_j$.
- Trong vòng lặp của `pagerank`, biến cùng tên `delta` là độ thay đổi $\Delta=\sum_i\lvert\mathrm{new}_i-r_i\rvert$ của bước 5, không phải $\delta$. Hai biến ở hai hàm khác nhau.
- `step` chỉ đọc `r` và chỉ ghi `new`, nên mỗi vòng là cập nhật đồng bộ, giả thiết của Mệnh đề 03.11. Nút cụt được bỏ qua ở vòng `for` vì phần $\beta$ của nó đã nằm trong `common`.
- `tol` là $\tau$, `max_iter` là $K$, `iterations` là $t_{\text{dừng}}$, và `converged` là trạng thái đạt ngưỡng của bước 6. `pagerank` tính $\Delta$ trước khi gán `r = new`, như bước 5.
:::

### 5.2 Chạy chương trình và đối chiếu

Từ thư mục `2627-1`, lệnh sau chạy đồ thị gốc; đổi `--variant` thành `dead` hoặc `trap` để chạy hai biến thể:

```bash
python3 materials/lec-03/code/pagerank.py --variant base --beta 0.8 --tol 1e-8 --max-iter 100
```

Đầu ra là JSON gồm các tham số `variant`, `beta`, `tol`, `max_iter` và các kết quả `rank`, `converged`, `iterations`, `delta`, `rank_sum`, trong đó `rank_sum` là tổng các điểm.

::: example Ví dụ 03.24 (Kết quả chạy ba biến thể)
**Dữ kiện.** $\beta=0{,}8$, $\tau=10^{-8}$, $K=100$; ba đồ thị `base` (Ví dụ 03.2), `dead` (Ví dụ 03.7) và `trap` (Ví dụ 03.8).

**Kết quả.**

| Biến thể | Vòng | $\Delta$ cuối | Điểm A, B, C, D | Nghiệm chính xác |
|---|---|---|---|---|
| `base` | 20 | $5{,}50\cdot10^{-9}$ | $0{,}321429$; $0{,}226190$; $0{,}226190$; $0{,}226190$ | $(9/28,19/84,19/84,19/84)$, Ví dụ 03.13 |
| `dead` | 12 | $2{,}05\cdot10^{-9}$ | $0{,}208333$; $0{,}263889$; $0{,}263889$; $0{,}263889$ | $(5/24,19/72,19/72,19/72)$, Mệnh đề 03.17 |
| `trap` | 34 | $5{,}97\cdot10^{-9}$ | $0{,}101351$; $0{,}128378$; $0{,}641892$; $0{,}128378$ | $(15,19,95,19)/148$, Ví dụ 03.11 |

Cả ba lần chạy trả `converged` đúng; `rank_sum` là $1{,}0$ với `base`, `dead` và $0{,}9999999999999999$ với `trap`.

**Số vòng của `base`.** Theo Ví dụ 03.12, $r^1-r^0=(1/10,-1/30,-1/30,-1/30)=\tfrac1{30}(3,-1,-1,-1)$. Đồ thị không có nút cụt nên $\bar M=M_0$, và $M_0(3,-1,-1,-1)^{\mathsf T}=(-3/2,1/2,1/2,1/2)^{\mathsf T}=-\tfrac12(3,-1,-1,-1)^{\mathsf T}$. Vì $F(x)-F(y)=\beta M_0(x-y)$, ta có $r^{t+1}-r^t=(-\tfrac25)^t(r^1-r^0)$ và
$$
\Delta_t=\frac15\Big(\frac25\Big)^t .
$$
Do đó $\Delta_{18}\approx1{,}37\cdot10^{-8}>\tau$ và $\Delta_{19}\approx5{,}50\cdot10^{-9}\le\tau$: chương trình dừng sau vòng thứ 20 với đúng $\Delta$ cuối đã in.

**Sai số.** Theo Hệ quả 03.16, sai số của véc-tơ trả về không quá $4\cdot5{,}50\cdot10^{-9}=2{,}2\cdot10^{-8}$. Vì $r^0-r^*=(-1/14,1/42,1/42,1/42)$ cũng tỷ lệ với $(3,-1,-1,-1)$, sai số thật là $\lVert r^{20}-r^*\rVert_1=(2/5)^{20}\cdot\tfrac17\approx1{,}6\cdot10^{-9}$.

**Kiểm tra lại.** $\Delta_0=1/5$ và $\Delta_1=2/25$ trùng Ví dụ 03.12; giá trị in ra $0{,}32142857064$ của A khác $9/28=0{,}32142857142\ldots$ khoảng $8\cdot10^{-10}$.
:::

Trên đồ thị gốc, sai số giảm theo hệ số $2/5$ mỗi vòng, nhỏ hơn hệ số $\beta=4/5$ của Định lý 03.15: sau 20 vòng sai số thật khoảng $1{,}6\cdot10^{-9}$, trong khi cận (c) cần 86 vòng để bảo đảm sai số $10^{-8}$ (Ví dụ 03.13). Trên biến thể bẫy, phép lặp chậm hơn và cần 34 vòng.

Một chương trình PageRank được kiểm theo ba lớp, theo thứ tự từ rẻ tới đắt.

- **Bất biến.** Sau mỗi vòng, tổng điểm xấp xỉ 1 và mọi điểm không âm (Mệnh đề 03.13).
- **Một bước tính tay.** Từ $r^0=u$ với $\beta=0{,}8$, `step` trên `base` phải cho $r_{\mathrm A}=7/20$ và $r_{\mathrm B}=r_{\mathrm C}=r_{\mathrm D}=13/60$ (Ví dụ 03.9); trên `dead`, $r_{\mathrm A}=1/5$ và $r_{\mathrm B}=r_{\mathrm C}=r_{\mathrm D}=4/15$ (Ví dụ 03.10). Phép so sánh dùng `abs(got - want) <= 1e-12`.
- **Trường hợp biên.** Khi mọi trang là nút cụt, $\delta$ (biến `delta` của `step`) bằng 1, phần chung bằng $1/n$ và mỗi vòng trả lại phân phối đều, không có phép chia cho 0; một trang có khuyên `"A": ["A"]` có $d_{\mathrm A}=1$ và giữ lại toàn bộ phần đi theo liên kết của mình (Thuật toán 03.10, trường hợp biên).

Ngoài các lỗi của Nhận xét 03.12, hai lỗi thường gặp khi tự cài là cập nhật thẳng `r[i] += ...` khi duyệt cạnh, trộn điểm cũ với điểm mới trái với cập nhật đồng bộ, và so sánh hai số thực bằng `==`, làm phép kiểm một bước thất bại vì sai số làm tròn.

::: exercise Bài tập 03.6 (Một vòng và tổng điểm của biến thể nút cụt)
Biến thể `dead` của `pagerank.py` là đồ thị của Ví dụ 03.7: $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm D\to\mathrm B,\mathrm C$; C không có liên kết ra.

- (a) Từ thư mục `2627-1/materials/lec-03/code`, gọi `step` một lần với điểm đều $0{,}25$ cho mọi trang và $\beta=0{,}8$. Ghi kết quả và đối chiếu với Ví dụ 03.10 bằng dung sai $10^{-12}$.
- (b) Chạy `pagerank.py --variant dead` với $\beta=0{,}8$, $\tau=10^{-8}$, $K=100$. Giải thích giá trị `rank_sum` theo Mệnh đề 03.13, và giải thích vì sao `rank_sum` của biến thể `trap` trong Ví dụ 03.24 là $0{,}9999999999999999$.
:::

::: hint
Viết `adj` như Mục 5.1 nhưng với danh sách rỗng cho C. Với (b), so tổng chính xác của Mệnh đề 03.13 với tổng của bốn số thực dấu phẩy động.
:::

::: solution
**Câu (a).** Đoạn mã

```python
from pagerank import step
adj = {"A": ["B", "C", "D"], "B": ["A", "D"], "C": [], "D": ["B", "C"]}
r = {i: 0.25 for i in adj}
new = step(adj, r, 0.8)
```

cho `new` bằng `{'A': 0.2, 'B': 0.26666666666666666, 'C': 0.26666666666666666, 'D': 0.26666666666666666}`. Ví dụ 03.10 cho $1/5$ và $4/15$; cả hai hiệu `abs(new['A'] - 1/5)` và `abs(new['B'] - 4/15)` không quá $10^{-12}$, nên phép kiểm một bước đạt.

**Câu (b).** Lệnh `python3 pagerank.py --variant dead --beta 0.8 --tol 1e-8 --max-iter 100` trả `converged` đúng sau 12 vòng, $\Delta\approx2{,}05\cdot10^{-9}$ và `rank_sum` bằng $1{,}0$. Theo Mệnh đề 03.13, mọi $r^t$ có tổng đúng bằng 1 trên số học chính xác, vì phần bù trả lại phần $\beta\delta$ của nút cụt. Trên số thực dấu phẩy động, mỗi phép cộng làm tròn tới số biểu diễn được gần nhất, nên tổng của bốn điểm có thể lệch 1 ở chữ số cuối; với `trap`, độ lệch là một đơn vị làm tròn, $1-0{,}9999999999999999\approx1{,}1\cdot10^{-16}$. Vì vậy phép kiểm bất biến dùng dung sai.

**Kiểm tra lại.** Trên biến thể `dead`, $r^1-r^0=(-1/20,1/60,1/60,1/60)=\tfrac1{60}(-3,1,1,1)$ và $\bar M(-3,1,1,1)^{\mathsf T}=-\tfrac14(-3,1,1,1)^{\mathsf T}$, nên $\Delta_t=\tfrac1{10}(1/5)^t$. Khi đó $\Delta_{10}\approx1{,}02\cdot10^{-8}>\tau$ và $\Delta_{11}\approx2{,}05\cdot10^{-9}\le\tau$, khớp 12 vòng.
:::

Như vậy, chương trình cho đúng các nghiệm $9/28$, $19/84$; $5/24$, $19/72$; $15/148$, $95/148$ đã tính tay, với số vòng 20, 12 và 34. Chương trình chạy trên một máy nên không kiểm được các con số chi phí của Mục 4; Tình huống 03.1 áp các công thức đó cho $10^9$ trang.

<!-- note-topic-id: lec-03-topic-16 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 03.1 (Xếp hạng một tỷ trang trên cụm máy)
**Bài toán và dữ liệu.** Cần tính PageRank cho $n=10^9$ trang (trang chiếu MMDS, tr.48). Trung bình mỗi trang có khoảng 10 liên kết ra (MMDS, §5.2.1, tr.190), nên $m\approx10^{10}$. Mỗi điểm là số thực 8 byte, mỗi mã trang hay bậc ra 4 byte.

**Mô hình hóa.** Mỗi vòng là một lần áp $F$ của Định nghĩa 03.8, tính bằng Thuật toán 03.22 với $k^2$ khối; các vòng nối tiếp theo Thuật toán 03.10.

**Kiểm giả thiết.** Chọn $\beta$ trong khoảng $0{,}8$ đến $0{,}9$ (MMDS, §5.1.5, tr.186), nên $0<\beta<1$ và Định lý 03.15 áp dụng được dù Web có nút cụt và bẫy. Mỗi bản ghi khối ghi bậc ra toàn cục, $\delta$ được tính một lần từ danh sách liên kết ra và mỗi trang có một cặp khởi tạo, đúng các giả thiết của Mệnh đề 03.23. Chọn $k$ chia hết $n$ để dùng Mệnh đề 03.27.

**Áp dụng và chi phí.**

- Ma trận đặc: $S_{\text{dense}}=8\cdot10^{18}$ byte (Ví dụ 03.1); không lưu được.
- Danh sách liên kết ra: $S_{\text{adj}}=4(10^9+10^{10})=4{,}4\cdot10^{10}$ byte (Mệnh đề 03.26).
- Biểu diễn khối: $S_{\text{blocks}}=8R+4m\le12m=1{,}2\cdot10^{11}$ byte, vì $R\le m$.
- Hai véc-tơ trên một máy cần $16n=1{,}6\cdot10^{10}$ byte; một tác vụ khối cần $B_{\text{task}}=1{,}6\cdot10^{10}/k+B_{\text{buf}}$ byte. Gọi $B_{\max}$ là bộ nhớ dành cho một tác vụ; $k$ phải thỏa $k\ge1{,}6\cdot10^{10}/(B_{\max}-B_{\text{buf}})$, và $k$ nhỏ nhất thỏa điều kiện này cho phần véc-tơ $8\cdot10^9k$ của $I$ nhỏ nhất.
- Đầu vào Map mỗi vòng: $I=S_{\text{blocks}}+8\cdot10^9\,k$ byte (Mệnh đề 03.27); phần véc-tơ tăng tuyến tính theo $k$.
- Đầu vào Reduce mỗi vòng: $H=12(m+n)=1{,}32\cdot10^{11}$ byte khi không có Combine, và không quá số đó khi có Combine (Mệnh đề 03.28).
- Số vòng: với $\varepsilon=10^{-8}$ và $\beta=0{,}8$, Định lý 03.15(c) bảo đảm sai số $\varepsilon$ sau 86 vòng trên mọi đồ thị (Ví dụ 03.13), và Hệ quả 03.16 cho ngưỡng $\tau=\varepsilon/4=2{,}5\cdot10^{-9}$ để dừng sớm hơn. MMDS ghi rằng với đồ thị Web, 50–75 vòng đủ để hội tụ tới sai số của số thực độ chính xác kép (§5.1.2, tr.179).

**Diễn giải.** Bài toán không giải được bằng ma trận đặc, nhưng giải được bằng một chuỗi công việc MapReduce, mỗi vòng một công việc; 86 vòng đủ để bảo đảm sai số $10^{-8}$, và mỗi công việc đọc không quá $1{,}2\cdot10^{11}$ byte ma trận một lần và đọc véc-tơ $k$ lần.

**Giới hạn.** $Q$ và thời gian mỗi vòng phụ thuộc vị trí các tác vụ và băng thông $b_{\text{eff}}$, nên dữ kiện trên chỉ cho cận dưới $Q/b_{\text{eff}}$ (Mệnh đề 03.28); $k$ phụ thuộc bộ nhớ của từng máy. Tác vụ của một khối có nhiều cạnh làm chậm pha Map theo Mệnh đề 03.29.

**Dẫn ngược lý thuyết.** Định nghĩa 03.8, 03.21; Thuật toán 03.10, 03.22; Định lý 03.15; Hệ quả 03.16; Mệnh đề 03.23, 03.26–03.29.
:::

::: application Tình huống 03.2 (Lặp thô trên cấu trúc nơ thắt của Web)
**Bài toán và dữ liệu.** Đồ thị web có cấu trúc nơ thắt của Mục 2.2: một SCC lớn, thành phần vào, thành phần ra, tua, ống và thành phần rời (MMDS, §5.1.3, tr.181–182). Cần xếp hạng các trang bằng phép lặp thô $r^{t+1}=M_0r^t$ của Định nghĩa 03.5.

**Giả thiết bị vi phạm.** Định lý 03.15 cần $\beta<1$ và phần bù nút cụt; lặp thô là trường hợp $\beta=1$ không bù. Đồ thị cũng có nút cụt (Định nghĩa 03.6) và nhóm trang không trỏ ra ngoài (Định nghĩa 03.7).

**Hậu quả.** Người lướt vào thành phần ra không quay lại được, nên các trang của SCC và thành phần vào nhận điểm giới hạn bằng 0 (MMDS, §5.1.3, tr.182). Trên bốn trang, hai hậu quả có số cụ thể: với nút cụt C, tổng điểm giảm $1$, $3/4$, $13/24$, $19/48$ và tiến về 0 (Ví dụ 03.7); với bẫy C, dãy tiến tới $(0,0,1,0)$ (Ví dụ 03.8).

**Cách sửa.** Dùng Định nghĩa 03.8 với $\beta=4/5$: biến thể C cụt có điểm cố định $(5/24,19/72,19/72,19/72)$, tổng 1 (Mệnh đề 03.17); biến thể bẫy có $(15/148,19/148,95/148,19/148)$ (Ví dụ 03.11), mọi trang có điểm dương. Định lý 03.15 bảo đảm hội tụ với tốc độ $(4/5)^t$ bất kể cấu trúc nơ thắt.

**Giới hạn.** Bước nhảy giới hạn tác dụng của bẫy nhưng không xóa nó: bẫy một trang C vẫn giữ $95/148\approx64\%$ tổng điểm. Trên Web có bẫy hàng triệu trang do người phát tán liên kết rác dựng (MMDS, §5.1.5, tr.185).

**Dẫn ngược lý thuyết.** Định nghĩa 03.5–03.8; Ví dụ 03.7, 03.8, 03.11; Định lý 03.15; Mệnh đề 03.17.
:::

**Ứng dụng trong các bài sau của học phần.**

- Bài 04 thay phân phối nhảy đều $u$ (Bài 04 gọi là phân phối dịch chuyển) bằng một phân phối tập trung trên một tập trang theo chủ đề hoặc một tập trang tin cậy, để có PageRank theo chủ đề và TrustRank (MMDS, §5.3–5.4). Ma trận $\bar M$ và lập luận co của Định lý 03.15 giữ nguyên, Thuật toán 03.10 chỉ đổi bước 1 và bước 3, và Hệ quả 03.16 cho cùng cận sai số.
- Điểm PageRank $r^*$ được kết hợp với tập trang chứa từ của truy vấn; máy tìm kiếm lấy tập này từ chỉ mục ngược (inverted index), theo MMDS (§5.1.1, tr.176; §5.1.6, tr.187). Bài 14 trình bày chỉ mục ngược.

<!-- note-topic-id: lec-03-topic-17 -->
## Tóm tắt chương

Câu hỏi xuất phát của chương là xếp hạng $10^9$ trang web bằng cấu trúc liên kết, khi ma trận đặc của đồ thị đã cần $8\cdot10^{18}$ byte (Ví dụ 03.1). Mỗi trang chia điểm của mình đều cho các đích (Định nghĩa 03.2), và vòng chia điểm là phép nhân với ma trận liên kết $M_0$ (Định nghĩa 03.3, Mệnh đề 03.4); trên bốn trang, lặp thô cho $(1/3,2/9,2/9,2/9)$. Nút cụt làm tổng điểm tiến về 0 và bẫy dồn mọi điểm vào một trang (Ví dụ 03.7, 03.8), nên quy tắc đầy đủ thêm bước nhảy với xác suất $1-\beta$ và chia đều phần $\beta$ của nút cụt (Định nghĩa 03.8, Mệnh đề 03.9). Quy tắc này giữ tổng điểm bằng 1 (Mệnh đề 03.13), co theo hệ số $\beta$ trong chuẩn $\ell_1$, hội tụ tới một phân phối duy nhất (Định lý 03.15), và độ thay đổi $\Delta_t$ chặn sai số bởi $\beta\Delta_t/(1-\beta)$ (Hệ quả 03.16); PageRank của bốn trang là $(9/28,19/84,19/84,19/84)$. Lưu ma trận theo liên kết ra và chia thành $k^2$ khối cho phép tính mỗi vòng bằng một công việc MapReduce trả đúng $F(r)$ khi bậc ra là bậc toàn cục, $\delta$ được tính một lần và mỗi trang có cặp khởi tạo (Thuật toán 03.22, Mệnh đề 03.23). Trên bốn trang, Combine giảm $H$ từ 144 còn 132 byte và bốn máy cho pha Map mức tăng tốc $8/3$ (Mệnh đề 03.26–03.29); với $10^9$ trang, danh sách liên kết ra cần $4{,}4\cdot10^{10}$ byte thay cho $8\cdot10^{18}$, và Định lý 03.15 bảo đảm sai số $10^{-8}$ sau 86 vòng với $\beta=0{,}8$, mỗi vòng một công việc MapReduce (Tình huống 03.1). Chương trình `pagerank.py` cho đúng các nghiệm tính tay sau 20, 12 và 34 vòng. Giới hạn còn lại là PageRank chỉ cho một thứ hạng chung cho mọi truy vấn và vẫn bị bẫy do người phát tán liên kết rác dựng nâng điểm; Bài 04 đổi phân phối nhảy để xử lý hai điểm này.

**Định nghĩa và kết quả theo mục.**

- Mục 1: ma trận đặc của một tỷ trang (Ví dụ 03.1); đồ thị web, bậc ra và bài toán xếp hạng (Định nghĩa 03.1); một vòng chia điểm đồng bộ (Định nghĩa 03.2).
- Mục 2: ma trận liên kết (Định nghĩa 03.3, Mệnh đề 03.4); lặp thô và điểm cố định (Định nghĩa 03.5); nút cụt, bẫy liên kết (Định nghĩa 03.6, 03.7); quy tắc cập nhật đầy đủ và ba dạng của nó (Định nghĩa 03.8, Mệnh đề 03.9); PageRank lặp và tính đúng (Thuật toán 03.10, Mệnh đề 03.11, Nhận xét 03.12); bảo toàn tổng (Mệnh đề 03.13); hội tụ (Bổ đề 03.14, Định lý 03.15); cận sai số (Hệ quả 03.16); công thức không bù và chuẩn hóa lại (Mệnh đề 03.17); ngưỡng dừng trong thực hành (Nhận xét 03.18).
- Mục 3: danh sách liên kết ra (Định nghĩa 03.19); một vòng là công việc nhân ma trận–véc-tơ (Nhận xét 03.20); chia khối (Định nghĩa 03.21); một vòng theo khối và tính đúng (Thuật toán 03.22, Mệnh đề 03.23, Nhận xét 03.24).
- Mục 4: các đại lượng chi phí (Định nghĩa 03.25); dung lượng (Mệnh đề 03.26); bộ nhớ và đầu vào Map (Mệnh đề 03.27); đầu vào Reduce và mạng (Mệnh đề 03.28); thời gian pha Map (Mệnh đề 03.29); thời gian một vòng và cả công việc (Nhận xét 03.30).
- Đọc thêm: loại nút cụt đệ quy (Thuật toán 03.31, Ví dụ 03.23, Nhận xét 03.32).
- Mục 5: ánh xạ sang `pagerank.py` (Nhận xét 03.33); kết quả ba biến thể (Ví dụ 03.24).

**Công thức và thuật toán cần nhớ.**

$$
\begin{gathered}
(M_0)_{ij}=\begin{cases}1/d_j&j\to i,\\0&\text{khác,}\end{cases}\\
\bar M=M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}.
\end{gathered}
$$

$$
\begin{aligned}
F(r)&=\beta M_0r+\big((1-\beta)+\beta\delta\big)u\\
&=\beta\bar Mr+(1-\beta)u .
\end{aligned}
$$

$$
\begin{gathered}
\lVert F(x)-F(y)\rVert_1\le\beta\lVert x-y\rVert_1,\\
\lVert r^{t+1}-r^*\rVert_1\le\frac{\beta}{1-\beta}\Delta_t .
\end{gathered}
$$

$$
\begin{gathered}
S_{\text{dense}}=8n^2,\quad S_{\text{adj}}=4(n+m),\\
S_{\text{blocks}}=8R+4m .
\end{gathered}
$$

$$
\begin{gathered}
B_{\text{task}}=\frac{16n}k+B_{\text{buf}},\\
I=S_{\text{blocks}}+8kn,\\
T_{\text{map}}\ge\max\Big(\frac WP,w_{\max}\Big).
\end{gathered}
$$

Một vòng PageRank đặt phần chung $((1-\beta)+\beta\delta)/n$ cho mọi trang rồi cộng $\beta r_j/d_j$ qua mỗi cạnh, chỉ đọc véc-tơ cũ. Theo khối, Map phát $(i,r_j/d_j)$ với khóa là trang đích, Combine cộng cục bộ, và Reduce trả $\beta z_i+((1-\beta)+\beta\delta)/n$.

**Giả thiết hay bị bỏ quên.**

- Bậc ra là bậc trên toàn đồ thị, kể cả trong một khối; dùng số đích trong khối làm sai mọi đóng góp của nguồn đó.
- Cập nhật đồng bộ: mọi đóng góp của một vòng đọc cùng một véc-tơ cũ.
- Phần bù nút cụt: bỏ nó thì tổng điểm sau một vòng là $1-\beta\delta$, và điểm cố định phải chuẩn hóa lại.
- $\beta<1$: với $\beta=1$, phép lặp có thể dao động hoặc dồn mọi điểm vào một bẫy.
- $\Delta_t$ là độ thay đổi, không phải sai số; sai số không quá $\beta\Delta_t/(1-\beta)$.
- $\delta$ được tính một lần từ danh sách liên kết ra, không cộng trên các khối.
- Mỗi trang cần một cặp khởi tạo $(i,0)$, nếu không trang không có liên kết vào vắng khỏi đầu ra.
- $k^2$ là số tác vụ, không phải số máy; thời gian pha Map là tải lớn nhất, không phải tổng việc chia đều.

## Bài tập củng cố

Bài tập 03.7–03.12 nằm trong [tệp bài tập Bài 03](material-viewer.html?doc=materials/lec-03/exercises.md&deck=lecture-03-pagerank-mo-hinh-va-tinh-toan.html), cùng gợi ý và lời giải.

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press. Chương 5: §5.1.1, tr.176–177 và hộp tr.177: Mục 1, 1.1, mục Ứng dụng; §5.1.2, tr.177–180, Ví dụ 5.1–5.2, Hình 5.1, hộp tr.180: Mục 1.1, 2.1, Nhận xét 03.12; §5.1.3, tr.181–182, Hình 5.2: Mục 2.2, Tình huống 03.2; §5.1.4, tr.182–185, Ví dụ 5.3–5.4, Hình 5.3–5.5, chú thích 4: Mục 2.2, phần đọc thêm; §5.1.5, tr.185–187, Ví dụ 5.5–5.6, Hình 5.6: Mục 2.2, 2.3, Mệnh đề 03.17; §5.1.6, tr.187: Mục 1.1, mục Ứng dụng; §5.2–5.2.1, tr.189–190, Ví dụ 5.7, Hình 5.11: Mục 3, 3.1, 4.1, Tình huống 03.1; §5.2.2–5.2.4, tr.191–194, Ví dụ 5.8, Hình 5.12–5.14: Mục 3, 3.2, 3.3, Nhận xét 03.24; §5.2.5, tr.193–194: Mục 4.2; Bài 5.1.5, 5.2.3, 5.2.4, 5.1.6: Bài tập 03.1, 03.3, 03.4, 03.5; Bài 5.1.1–5.1.3, 5.1.7, 5.2.1, 5.2.2: tệp bài tập. Sách và trang chiếu của các tác giả: http://www.mmds.org.
- Leskovec, J., Rajaraman, A. và Ullman, J. D. Trang chiếu Chương 5 *Link Analysis: PageRank* của sách MMDS, bản trên http://www.mmds.org (không ghi năm). Tr.16–17: Mục 1.1; tr.31–32: Mục 2.1; tr.42: Mục 2.3, Mệnh đề 03.9; tr.48: Mục 1, Tình huống 03.1; tr.49: Mục 2.3; tr.51: Mệnh đề 03.17; tr.52: Mệnh đề 03.9.
- Leskovec, J. và Kanatsoulis, C. (2026). Stanford CS246, *Mining Massive Datasets*, bài 09-pagerank. Trang chiếu 45: Mục 2.3, Mệnh đề 03.9; 54: Mệnh đề 03.9.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press. §2.1: bất biến vòng lặp trong chứng minh Mệnh đề 03.11.
- Ghi chú Bài 01: Định nghĩa 01.13; Mệnh đề 01.12. Ghi chú Bài 02: Thuật toán 02.10, 02.18; Mệnh đề 02.11, 02.15, 02.19, 02.38; Định nghĩa 02.14, 02.17, 02.30, 02.33, 02.39; Nhận xét 02.20; Tình huống 02.3; Ví dụ 02.5.
- Mã thực hành `materials/lec-03/code/pagerank.py` và `materials/lec-03/code/practice-README.md`: Mục 5, Ví dụ 03.24, Bài tập 03.6.
