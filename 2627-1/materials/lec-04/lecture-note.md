# Bài 04 — PageRank theo chủ đề, liên kết rác và HITS

PageRank của Bài 03 cho mỗi trang web một điểm duy nhất, giống nhau cho mọi truy vấn và mọi người dùng. Chúng ta giữ nguyên phép lặp đó và chỉ đổi nơi đến của bước dịch chuyển để có điểm theo chủ đề; dùng cùng phép lặp với một tập trang tin cậy để hạ điểm của các trang được nâng bằng liên kết rác; rồi gán cho mỗi trang hai điểm của thuật toán *tìm kiếm theo chủ đề dựa trên siêu liên kết* (hyperlink-induced topic search, HITS) để tách trang dẫn đường khỏi trang cung cấp thông tin.

[Bộ trang chiếu Bài 04](lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html) trình bày cùng chủ đề; [tệp bài tập Bài 04](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Lập phân phối dịch chuyển từ một tập chủ đề, chạy hai vòng PageRank theo chủ đề bằng tay và giải điểm cố định trên một đồ thị nhỏ (Mục 2.1, Mục 2.2).
2. Chứng minh tổng điểm được bảo toàn, phép lặp hội tụ và sai số bị chặn bởi $\beta\Delta_t/(1-\beta)$ với mọi phân phối dịch chuyển; ghép các véc-tơ chủ đề và đếm chi phí tiền tính, chi phí truy vấn (Mục 2.3–2.5).
3. Lập phương trình điểm của trang hỗ trợ và trang đích trong một cụm thao túng liên kết, giải điểm trang đích, tính hệ số khuếch đại và nêu các giả thiết của công thức (Mục 3).
4. Tính TrustRank và khối lượng rác trên cùng một mô hình, đọc dấu và độ lớn của chỉ số (Mục 4).
5. Lập ma trận kề $L$, chạy HITS bằng tay, giải thích phép chuẩn hóa theo giá trị lớn nhất và xác định giới hạn của phép lặp qua véc-tơ riêng của $LL^{\mathsf T}$ (Mục 5).
6. Chọn phương pháp theo đầu ra cần có, thông tin bổ sung, giả thiết và chi phí mỗi vòng (Mục 6).

## Kiến thức tiên quyết

Số hiệu `01.k`, `03.k` chỉ ghi chú Bài 01, Bài 03; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Đồ thị web và ma trận liên kết** (Định nghĩa 03.1, 03.3; Ví dụ 03.2, 03.5). Đồ thị web $G=(V,E)$ có $n$ trang; cạnh $j\to i$ khi trang $j$ có liên kết tới trang $i$; $d_j$ là bậc ra của $j$. Ma trận liên kết $M_0$ có $(M_0)_{ij}=1/d_j$ khi $j\to i$ và bằng 0 khi không, nên cột là trang nguồn và cột của một nút cụt ($d_j=0$) toàn 0. Đồ thị bốn trang G4 có các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$ và
$$
M_0=\begin{pmatrix}0&1/2&1&0\\1/3&0&0&1/2\\1/3&0&0&1/2\\1/3&1/2&0&0\end{pmatrix}.
$$
- **Quy tắc cập nhật đầy đủ** (Định nghĩa 03.8; Mệnh đề 03.9(a), (c)). Với $\beta=1$ và đồ thị không có nút cụt, phép lặp $r^{t+1}=M_0r^t$ là *lặp thô* (Định nghĩa 03.5); trên G4 nó cho $(1/3,2/9,2/9,2/9)$ (Ví dụ 03.6). Với $0<\beta<1$, $u_i=1/n$ và $\delta=\sum_{j\in\mathcal D}r_j$ là tổng điểm ở các nút cụt, $F(r)=\beta M_0r+\big((1-\beta)+\beta\delta\big)u$; viết gọn $F(r)=\beta\bar Mr+(1-\beta)u$ với $\bar M=M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$, ma trận $M_0$ có mỗi cột nút cụt thay bằng $u$, không âm và có mọi cột tổng 1. Khi $\mathcal D=\varnothing$, $F(r)=\beta M_0r+(1-\beta)u$. Bài 03 gọi nhánh xác suất $1-\beta$ là bước nhảy (còn gọi là dịch chuyển, teleport).
- **PageRank lặp** (Thuật toán 03.10; Mệnh đề 03.11). Khởi tạo $r\leftarrow u$; mỗi vòng đặt phần chung $((1-\beta)+\beta\delta)/n$ cho mọi trang rồi cộng $\beta r_j/d_j$ qua mỗi cạnh $j\to i$, chỉ đọc véc-tơ cũ, và dừng khi $\Delta\le\tau$ hoặc sau $K$ vòng. Mỗi vòng tốn $3n+\ell$ thao tác với $\ell$ là số cạnh (Bài 03 viết $3n+m$); sau vòng thứ $t$ mảng $r$ bằng $r^t=F(r^{t-1})$, và trạng thái đạt ngưỡng được trả đúng khi $\Delta\le\tau$ (Mệnh đề 03.11(b)).
- **Bảo toàn và hội tụ** (Mệnh đề 03.13; Bổ đề 03.14; Định lý 03.15; Hệ quả 03.16). Một vòng biến một phân phối thành một phân phối. Nếu $A$ không âm và mọi cột có tổng không quá 1 thì $\lVert Ax\rVert_1\le\lVert x\rVert_1$. Ánh xạ $F$ co hệ số $\beta$ theo chuẩn $\lVert\cdot\rVert_1$, có đúng một điểm cố định $r^*$, $r^*$ là phân phối, $\lVert r^t-r^*\rVert_1\le2\beta^t$, và với $\Delta_t=\lVert r^{t+1}-r^t\rVert_1$ thì $\lVert r^{t+1}-r^*\rVert_1\le\beta\Delta_t/(1-\beta)$.
- **Bẫy liên kết** (Định nghĩa 03.7). Một tập trang khác rỗng mà mọi trang của nó có liên kết ra và mọi liên kết ra đều ở lại trong tập; khi $\beta=1$, điểm dồn vào bẫy.
- **Ma trận đặc của một tỷ trang** (Ví dụ 03.1); **biến thể C cụt của G4** (Ví dụ 03.10). Với $n=10^9$ và 8 byte một ô, ma trận đặc cần $8\cdot10^{18}$ byte. Xóa cạnh $\mathrm C\to\mathrm A$ của G4 làm C thành nút cụt; với $r^0=u$, $\delta^0=1/4$.
- **Cận với phân phối khác** (Nhận xét 03.18). Cận của Hệ quả 03.16 chỉ dùng tính co, nên còn đúng khi $u$ trong phần $(1-\beta)u$ được thay bằng một phân phối khác trên $V$ không phụ thuộc $r$.
- **PageRank của G4** (Ví dụ 03.13). Với $\beta=4/5$, $r^*=(9/28,19/84,19/84,19/84)$; Định lý 03.15(c) bảo đảm sai số $10^{-8}$ sau 86 vòng, vì $2(4/5)^{86}\le10^{-8}$.
- **Một vòng trên cụm máy** (Định nghĩa 03.19; Thuật toán 03.22; Tình huống 03.1). Đồ thị lớn được lưu bằng danh sách liên kết ra, mỗi bản ghi gồm nguồn, bậc ra và danh sách đích; một vòng PageRank là một công việc MapReduce theo khối. Với $n=10^9$ trang và trung bình 10 liên kết ra mỗi trang, số cạnh khoảng $10^{10}$.
- **Mô hình chi phí** (Định nghĩa 01.13). Khối lượng tính toán, bộ nhớ làm việc và dung lượng lưu trữ là các đại lượng riêng, mỗi đại lượng có đơn vị riêng.
- **Đại số tuyến tính.** Một ma trận đối xứng thực $B\in\mathbb R^{n\times n}$ có trị riêng thực $\lambda_1\ge\cdots\ge\lambda_n$ và một cơ sở trực chuẩn $\psi_1,\dots,\psi_n$ gồm các véc-tơ riêng, $B\psi_i=\lambda_i\psi_i$ (định lý phổ). Với mọi $x\in\mathbb R^n$, $x^{\mathsf T}LL^{\mathsf T}x=\lVert L^{\mathsf T}x\rVert_2^2\ge0$, nên mọi trị riêng của $LL^{\mathsf T}$ không âm.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; chữ chỉ dùng trong một ví dụ, một chứng minh hay một bài tập được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $G=(V,E)$; $n$; $\ell$ | đồ thị web; số trang $\lvert V\rvert$; số cạnh $\lvert E\rvert$ | đồ thị có hướng hữu hạn; $n\ge1$; $\ell\ge0$ |
| $j\to i$; $d_j$; $\mathcal D$ | cạnh từ trang nguồn $j$ tới trang đích $i$; bậc ra của $j$; tập nút cụt $\{j:d_j=0\}$ | cạnh của $E$; số nguyên $\ge0$; tập con của $V$ |
| $M_0$; $\bar M$ | ma trận liên kết, cột là trang nguồn; $M_0+u\,\mathbf 1_{\mathcal D}^{\mathsf T}$ | $\mathbb R^{n\times n}$; $\bar M$ không âm, mọi cột tổng 1 |
| $u$; $\mathbf 1$; $\mathbf 1_{\mathcal D}$ | phân phối đều, $u_i=1/n$; véc-tơ toàn 1; véc-tơ chỉ báo của $\mathcal D$ | $\mathbb R^n$ |
| $\beta$; $\delta^t$ | xác suất đi theo một liên kết ra; tổng điểm ở nút cụt sau $t$ vòng | $0<\beta<1$; $[0,1]$ |
| $S$; $v$; $F_v$ | tập chủ đề (tập dịch chuyển); phân phối dịch chuyển; ánh xạ cập nhật với phân phối $v$ | $\varnothing\ne S\subseteq V$; $v\ge0$, $\sum_iv_i=1$; $\mathbb R^n\to\mathbb R^n$ |
| $r^t$; $r^*_v$ | véc-tơ điểm sau $t$ vòng; điểm cố định của $F_v$ (viết $r^*$ khi $v$ đã rõ) | phân phối trên $V$ |
| $\Delta_t$; $\tau$; $\varepsilon$; $K$ | độ thay đổi $\lVert r^{t+1}-r^t\rVert_1$; ngưỡng dừng; sai số cần đạt; số vòng tối đa | $\Delta_t\ge0$; $\tau,\varepsilon>0$; $K$ nguyên dương |
| $k$; $\theta$ | số chủ đề; chỉ số chủ đề | $\theta=1,\dots,k$ |
| $v^{(\theta)}$; $r^{(\theta)}$; $w_\theta$; $K_\theta$ | phân phối dịch chuyển của chủ đề $\theta$; điểm cố định tương ứng; trọng số chủ đề; số vòng thực chạy | phân phối; phân phối; $w_\theta\ge0$, $\sum_\theta w_\theta=1$; nguyên dương |
| $C$; $c$; $q_i$ | tập trang ứng viên của một truy vấn; $c=\lvert C\rvert$; điểm ghép $\sum_\theta w_\theta r^{(\theta)}_i$ | $C\subseteq V$ |
| $m$; $b$ | số trang hỗ trợ của một cụm thao túng; phần dịch chuyển mỗi trang nhận, $(1-\beta)/n$ | $m\ge1$; $b>0$ |
| $x$; $y$; $p$ | đóng góp theo cạnh từ ngoài cụm vào trang đích, đã nhân $\beta$ và chia bậc ra; điểm trang đích; điểm mỗi trang hỗ trợ | $\ge0$; điểm cố định |
| $T$; $v_T$ | tập trang tin cậy; phân phối đều trên $T$ | $\varnothing\ne T\subseteq V$ |
| $\rho$; $\rho^t$; $\delta_\rho^t$ | TrustRank; véc-tơ TrustRank sau $t$ vòng; tổng TrustRank ở nút cụt | phân phối |
| $s_i$ | khối lượng rác của trang $i$, $1-\rho_i/r_i$ | $(-\infty,1]$, cần $r_i>0$ |
| $L$ | ma trận kề (adjacency matrix), $L_{ij}=1$ khi $i\to j$; hàng là trang nguồn | $\{0,1\}^{n\times n}$ |
| $h$; $a$; $\tilde h$; $\tilde a$ | điểm trung tâm; điểm uy tín; hai véc-tơ thô trước chuẩn hóa | $\mathbb R^n$, không âm |
| $N(z)$ | chuẩn hóa theo giá trị lớn nhất, $z/\max_iz_i$ | cần $z\ge0$, $\max_iz_i>0$ |
| $K_{\mathrm H}$ | số vòng HITS thực chạy | nguyên dương |
| $\lambda_1\ge\cdots\ge\lambda_n$; $\psi_1,\dots,\psi_n$; $\gamma_i$ | trị riêng của $LL^{\mathsf T}$; véc-tơ riêng trực chuẩn tương ứng; hệ số $\psi_i^{\mathsf T}h^0$ | $\lambda_i\ge0$; $\mathbb R^n$; $\mathbb R$ |
| $\lVert x\rVert_1$; $\lVert x\rVert_2$; $\lVert x\rVert_\infty$ | $\sum_i\lvert x_i\rvert$; $\big(\sum_ix_i^2\big)^{1/2}$; $\max_i\lvert x_i\rvert$ | số thực $\ge0$ |

Các quy ước đọc sau dùng trong cả chương.

- Véc-tơ là véc-tơ cột; chỉ số trên $t$ đếm số vòng đã chạy, chỉ số trên trong ngoặc $(\theta)$ là nhãn chủ đề. Bất đẳng thức giữa hai véc-tơ, như $v\ge0$, đọc theo từng thành phần.
- Số thập phân dùng dấu phẩy, ví dụ $0{,}85$; số nguyên lớn viết dạng lũy thừa, ví dụ $10^9$.
- Tên trang viết chữ đứng, như trang $\mathrm A$ và điểm $r_{\mathrm A}$; thứ tự thành phần của véc-tơ và thứ tự hàng, cột của ma trận là thứ tự tên trang.
- Mô hình byte của Bài 03: một điểm là số thực 8 byte.
- Bài 03 viết số cạnh là $m$; ở đây số cạnh là $\ell$, vì $m$ là số trang hỗ trợ như trong MMDS. Phân phối đều $u$ của bước dịch chuyển mà Bài 03 gọi là phân phối nhảy là trường hợp $v=u$ của phân phối dịch chuyển.
- MMDS viết ma trận liên kết là $M$, véc-tơ điểm là $v$, phân phối dịch chuyển là $e_S/\lvert S\rvert$, trang đích và TrustRank đều là $t$; ở đây là $M_0$, $r$, $v$, "trang đích" và $\rho$, vì $t$ là chỉ số vòng. MMDS viết hằng chuẩn hóa của HITS là $\lambda,\mu$; ở đây chữ $\lambda$ dành cho trị riêng.
- Viết tắt nguồn: MMDS (*Mining of Massive Datasets*, ấn bản 3); "trang chiếu MMDS" chỉ bộ trang chiếu phần hai Chương 5 của các tác giả MMDS; CS246 chỉ bài giảng 10-spam của Stanford CS246; BHK (*Foundations of Data Science* của Blum, Hopcroft và Kannan); chi tiết ở mục tài liệu tham khảo.

<!-- note-topic-id: lec-04-topic-01 -->
## 1. Bài toán xếp hạng liên kết

Bài 03 đã cho mỗi đồ thị web và mỗi $\beta\in(0,1)$ đúng một véc-tơ PageRank $r^*$, nghiệm của $r=\beta\bar Mr+(1-\beta)u$, và một phép lặp hội tụ tới nó với tốc độ $\beta^t$ (Định lý 03.15). Véc-tơ này chỉ phụ thuộc đồ thị. Ba nhu cầu xếp hạng sau đòi nhiều hơn một véc-tơ như vậy:

- **ngữ cảnh của truy vấn:** truy vấn "jaguar" có thể chỉ loài báo đốm, hãng xe Jaguar, một phiên bản hệ điều hành MAC hay một máy chơi trò chơi cũ; nếu biết người dùng quan tâm tới ô tô thì máy tìm kiếm trả được các trang phù hợp hơn (MMDS, §5.3.1, tr.195);
- **liên kết tạo ra để tăng điểm:** sau khi PageRank làm thư rác theo từ mất tác dụng, người phát tán thư rác chuyển sang tạo liên kết để PageRank đánh giá quá cao một số trang (MMDS, §5.4, tr.199);
- **hai vai trò của một trang:** trang danh sách học phần của một khoa có giá trị vì dẫn tới các trang học phần, còn trang của một học phần có giá trị vì chứa nội dung; một điểm duy nhất không tách được hai vai trò này (MMDS, Ví dụ 5.13, tr.205).

Cách trực tiếp cho nhu cầu thứ nhất là lưu một véc-tơ PageRank riêng cho mỗi người dùng. MMDS ghi rằng không lưu được một véc-tơ dài nhiều tỷ thành phần cho mỗi người trong một tỷ người dùng (§5.3.1, tr.195–196); ví dụ sau tính con số đó.

::: example Ví dụ 04.1 (Một véc-tơ PageRank cho mỗi người dùng)
**Dữ kiện.** Có $10^9$ người dùng (MMDS, §5.3.1) và $n=10^9$ trang (Tình huống 03.1); mỗi điểm là số thực 8 byte.

**Tính.** Một véc-tơ toàn web chiếm $8n=8\cdot10^9$ byte. Một véc-tơ cho mỗi người dùng chiếm
$$
10^9\cdot8\cdot10^9=8\cdot10^{18}\ \text{byte},
$$
bằng dung lượng ma trận đặc của một tỷ trang trong Ví dụ 03.1.

**Phương án theo chủ đề.** Nếu chỉ lưu $k$ véc-tơ toàn web, mỗi véc-tơ cho một chủ đề, và mỗi người dùng lưu $k$ trọng số, dung lượng là $8kn+8k\cdot10^9$ byte. Với $k=16$, mỗi số hạng bằng $1{,}28\cdot10^{11}$ byte.

**Kiểm tra lại.** $8\cdot10^{18}/(2\cdot1{,}28\cdot10^{11})=3{,}125\cdot10^{7}$, nên phương án theo chủ đề cần ít hơn khoảng $3\cdot10^7$ lần dung lượng.
:::

![Hai cách lưu điểm xếp hạng. Hàng trên, phương án trực tiếp: mỗi người dùng có một véc-tơ điểm toàn web. Một đường nét đứt ngăn với phương án theo chủ đề ở hai hàng dưới: các chủ đề có véc-tơ điểm toàn web, còn mỗi người dùng chỉ có các trọng số chủ đề.](img/lec-04/luu-vector-theo-chu-de.svg)

Hình đặt hai phương án cạnh nhau. Ở hàng trên, số véc-tơ dài bằng số người dùng; ở hai hàng dưới, số véc-tơ dài bằng số chủ đề $k$, và phần riêng của mỗi người dùng chỉ còn $k$ số. Đổi lại, sở thích của một người dùng chỉ được biểu diễn qua các chủ đề đã chọn; MMDS ghi rằng cách này mất một phần độ chính xác (§5.3.1, tr.196).

![Sơ đồ cấu trúc chương, đọc từ trên xuống. Khối trên cùng: bài toán trung tâm, xếp hạng 10⁹ trang cho 10⁹ người dùng; một véc-tơ mỗi người cần 8 · 10¹⁸ byte. Sáu mũi tên xuống sáu cột; mỗi cột ghi câu hỏi của phần đó và, dưới đường kẻ đứt, các khái niệm chính. Mục 2: điểm phụ thuộc chủ đề bằng cách nào; phân phối dịch chuyển, tiền tính, ghép chủ đề. Mục 3: liên kết rác tăng điểm đến đâu; cụm thao túng, trang đích, trang hỗ trợ, hệ số khuếch đại. Mục 4: hạ điểm trang rác bằng thông tin nào; tập tin cậy, TrustRank, khối lượng rác. Mục 5: tách hai vai trò của một trang thế nào; trung tâm, uy tín, chuẩn hóa, véc-tơ riêng. Cột đọc thêm, viền nét đứt: HITS hội tụ nhanh đến đâu; khoảng cách trị riêng, trị riêng bội. Mục 6: chọn phương pháp nào; đầu ra, giả thiết, chi phí mỗi vòng.](img/lec-04/note-cau-truc-chuong-04.svg)

Sơ đồ đọc từ trên xuống. Khối trên cùng ghi bài toán trung tâm với số liệu của Ví dụ 04.1. Bốn cột đầu ứng với ba nhu cầu ở trên: Mục 2 xử lý ngữ cảnh, Mục 3 và Mục 4 xử lý liên kết rác, Mục 5 xử lý hai vai trò; Mục 6 đặt các phương pháp cạnh nhau. Cột đọc thêm có viền nét đứt vì các mục khác không dùng kết quả của nó.

Mọi phương pháp ở đây vẫn dùng nhánh đi theo liên kết của Bài 03. Bài tập sau ôn lại nhánh đó trên G4.

::: exercise Bài tập 04.1 (Đóng góp theo cạnh $\mathrm B\to\mathrm A$)
Trên G4 với các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$, mỗi trang có điểm $1/4$ và $\beta=4/5$. Tính phần điểm theo liên kết mà B chuyển tới A trong một vòng, và xác định phần tử tương ứng của $M_0$ (cột là trang nguồn).
:::

::: hint
Phần điểm qua một cạnh $j\to i$ là $\beta r_j/d_j$; bậc ra lấy tại nguồn của cạnh.
:::

::: solution
B có hai cạnh ra, tới A và D, nên $(M_0)_{\mathrm A\mathrm B}=1/d_{\mathrm B}=1/2$: phần tử ở hàng A, cột B. Phần điểm theo cạnh $\mathrm B\to\mathrm A$ là
$$
\beta\,r_{\mathrm B}\,(M_0)_{\mathrm A\mathrm B}=\frac45\cdot\frac14\cdot\frac12=\frac1{10}.
$$
Đây là một trong hai phần theo liên kết mà A nhận; phần thứ hai đến từ C và bằng $\tfrac45\cdot\tfrac14\cdot1=\tfrac15$.

**Kiểm tra lại.** Cột B của $M_0$ là $(1/2,0,0,1/2)^{\mathsf T}$, tổng 1, với hai phần tử khác 0 ở hàng A và hàng D, đúng hai cạnh ra của B.
:::

PageRank toàn cục cho mỗi đồ thị đúng một thứ tự trang; trên G4, A đứng đầu với $9/28$ (Ví dụ 03.13), cho mọi truy vấn và dù liên kết vào của A do ai tạo ra. Trong Mục 2, chúng ta giữ nhánh theo liên kết và quy tắc bù nút cụt, chỉ đổi nơi đến của bước dịch chuyển.

<!-- note-topic-id: lec-04-topic-02 -->
## 2. PageRank theo chủ đề

Giả sử trên G4, B và D là hai trang đã biết thuộc một chủ đề; MMDS lấy chủ đề thể thao làm ví dụ (§5.3.2, tr.196), và truy vấn "jaguar" của Mục 1 ứng với hai chủ đề động vật và ô tô. Chúng ta cần một quy tắc tính điểm ưu tiên các trang của chủ đề và các trang gần chúng theo liên kết, mà vẫn có các bảo đảm của Bài 03: tổng điểm bằng 1, phép lặp hội tụ tới một nghiệm duy nhất, và có cận sai số khi dừng. Chúng ta còn cần biết tính bao nhiêu véc-tơ trước khi có truy vấn và ghép chúng thế nào khi truy vấn đến.

### 2.1 Phân phối dịch chuyển

Về mặt ý tưởng, người lướt ngẫu nhiên của Bài 03 vẫn đi theo một liên kết ra với xác suất $\beta$, nhưng khi dịch chuyển với xác suất $1-\beta$, người đó chỉ đến một trang của chủ đề thay vì một trang bất kỳ trong $n$ trang. Người lướt vì vậy hay ở các trang của chủ đề hoặc các trang tới được từ chúng bằng một đường đi ngắn. Trực giác của MMDS là trang được các trang thể thao trỏ tới thường cũng nói về thể thao, và khả năng này giảm khi khoảng cách tới các trang thể thao đã biết tăng (§5.3.2, tr.196).

![Hai nhánh di chuyển từ trang hiện tại. Nhánh liền, xác suất β: đi tới đích của một cạnh ra. Nhánh nét đứt, xác suất 1 − β: dịch chuyển tới tập S.](img/lec-04/hai-nhanh-di-chuyen.svg)

So với bước nhảy của Định nghĩa 03.8, hình chỉ khác ở nhánh nét đứt: nơi đến là tập $S$, không còn là cả $n$ trang. Nhánh liền giữ nguyên, nên đồ thị và ma trận $M_0$ không đổi. Để làm rõ quy tắc này, xem ví dụ sau trên G4; trong hình dưới, hai trang của $S$ là B và D, có viền đôi và nhãn $S$.

![Đồ thị G4 của MMDS Hình 5.15: A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới A; D trỏ tới B, C. B và D có viền đôi và nhãn S, thuộc tập chủ đề.](img/lec-04/hinh-5-15.svg)

::: example Ví dụ 04.2 (Vòng thứ nhất trên G4 với tập chủ đề $\{\mathrm B,\mathrm D\}$)
**Dữ kiện.** Đồ thị G4: $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm A$; $\mathrm D\to\mathrm B,\mathrm C$; không có nút cụt; $\beta=4/5$. Tập chủ đề $S=\{\mathrm B,\mathrm D\}$; khi dịch chuyển, người lướt chọn đều một trong hai trang của $S$, nên phân phối chọn trang đích của bước dịch chuyển là
$$
v=(0,1/2,0,1/2).
$$
Theo MMDS Ví dụ 5.10, người lướt bắt đầu ở các trang của $S$: $r^0=v$.

**Theo liên kết.** B chia $r^0_{\mathrm B}=1/2$ cho A và D, mỗi trang $1/4$; D chia $1/2$ cho B và C, mỗi trang $1/4$; A và C có điểm 0. Do đó $M_0r^0=(1/4,1/4,1/4,1/4)$, và nhánh theo liên kết đóng góp $\beta\cdot1/4=1/5$ cho mỗi trang.

**Dịch chuyển.** Nhánh dịch chuyển mang $1-\beta=1/5$ tổng điểm và chia theo $v$: $(1-\beta)v=(0,1/10,0,1/10)$.

| Trang | Theo liên kết $\beta(M_0r^0)_i$ | Dịch chuyển $(1-\beta)v_i$ | $r^1_i$ |
|---|---:|---:|---:|
| A | $1/5$ | $0$ | $1/5$ |
| B | $1/5$ | $1/10$ | $3/10$ |
| C | $1/5$ | $0$ | $1/5$ |
| D | $1/5$ | $1/10$ | $3/10$ |

**Kiểm tra lại.** $1/5+3/10+1/5+3/10=1$. Nếu dịch chuyển đều như Bài 03, mỗi trang nhận $1/20$ thay cho $0$ hoặc $1/10$, và bốn điểm mới đều bằng $1/4$.
:::

Sau một vòng, B và D vượt A. Phép tính dùng ba đại lượng: ma trận $M_0$ của đồ thị, xác suất $\beta$ và phân phối $v$ của bước dịch chuyển. Định nghĩa sau viết quy tắc này cho mọi đồ thị, kể cả đồ thị có nút cụt.

::: definition Định nghĩa 04.1 (Phân phối dịch chuyển và PageRank theo chủ đề)
Cho đồ thị web $G$ với ma trận liên kết $M_0$, tập nút cụt $\mathcal D$, hằng số $0<\beta<1$ và $u_i=1/n$.

**Phân phối dịch chuyển.** Một *phân phối dịch chuyển* (teleport distribution) là một véc-tơ $v\in\mathbb R^n$ với $v\ge0$ và $\sum_iv_i=1$. Với một *tập chủ đề* $S\subseteq V$, $S\ne\varnothing$, còn gọi là *tập dịch chuyển* (teleport set), phân phối dịch chuyển đều trên $S$ là
$$
v_i=\begin{cases}1/\lvert S\rvert&\text{khi }i\in S,\\0&\text{khi }i\notin S.\end{cases}
$$

**Ánh xạ cập nhật.** Với $r\in\mathbb R^n$ và $\delta=\sum_{j\in\mathcal D}r_j$,
$$
\begin{aligned}
F_v(r)&=\beta M_0r+\beta\delta\,u\\
&\quad+(1-\beta)v.
\end{aligned}
$$

**PageRank theo chủ đề.** *PageRank theo chủ đề* (topic-sensitive PageRank) với phân phối $v$ là phân phối $r^*_v$ thỏa $r^*_v=F_v(r^*_v)$. Phép lặp bắt đầu từ một phân phối $r^0$ và đặt $r^{t+1}=F_v(r^t)$; khi đó $\delta^t=\sum_{j\in\mathcal D}r^t_j$.
:::

$F_v(r)$ gồm ba số hạng:

- $\beta M_0r$ là nhánh đi theo liên kết, như Bài 03;
- $\beta\delta\,u$ là phần bù nút cụt: phần $\beta$ của các nút cụt không có liên kết để đi theo nên được chia đều cho $n$ trang, như Bài 03;
- $(1-\beta)v$ là nhánh dịch chuyển: phần $1-\beta$ của mọi trang được chia theo $v$.

Theo Mệnh đề 03.9(a), $\beta M_0r+\beta\delta u=\beta\bar Mr$, nên $F_v(r)=\beta\bar Mr+(1-\beta)v$. Định lý 04.5 chứng minh $F_v$ có đúng một điểm cố định và điểm đó là một phân phối. Khi $v=u$, $F_u$ là ánh xạ $F$ của Định nghĩa 03.8 và $r^*_u$ là PageRank của Bài 03; phân phối dịch chuyển vì vậy tổng quát hóa phân phối đều $u$ của bước nhảy trong Bài 03. Ví dụ 04.2 là vòng đầu của phép lặp với $v=(0,1/2,0,1/2)$ và $\delta^0=0$, vì G4 không có nút cụt.

Bù nút cụt và dịch chuyển là hai thao tác khác nhau. Phần bù luôn chia theo $u$, kể cả khi $v$ tập trung trên $S$; đổi $v$ không đổi quy tắc bù. Với quy ước này, $\bar M$ chung cho mọi phân phối dịch chuyển.

::: example Ví dụ 04.3 (Vòng thứ hai và điểm cố định trên G4; MMDS Ví dụ 5.10)
**Dữ kiện.** G4, $\beta=4/5$, $v=(0,1/2,0,1/2)$, không có nút cụt; theo Ví dụ 04.2, $r^1=(1/5,3/10,1/5,3/10)$. Theo Định nghĩa 04.1, $r^{t+1}_i=\tfrac45(M_0r^t)_i+\tfrac15v_i$.

**Vòng hai.**

- A nhận từ B (bậc ra 2) và C (bậc ra 1): $r^2_{\mathrm A}=\tfrac45\big(\tfrac12\cdot\tfrac3{10}+\tfrac15\big)=\tfrac45\cdot\tfrac7{20}=\tfrac7{25}$.
- B nhận từ A (bậc ra 3), D (bậc ra 2) và phần dịch chuyển: $r^2_{\mathrm B}=\tfrac45\big(\tfrac13\cdot\tfrac15+\tfrac12\cdot\tfrac3{10}\big)+\tfrac1{10}=\tfrac45\cdot\tfrac{13}{60}+\tfrac1{10}=\tfrac{41}{150}$.
- C nhận từ A và D cùng phần theo liên kết như B nhưng không có phần dịch chuyển: $r^2_{\mathrm C}=\tfrac{13}{75}$.
- D nhận từ A và B: $r^2_{\mathrm D}=\tfrac45\big(\tfrac13\cdot\tfrac15+\tfrac12\cdot\tfrac3{10}\big)+\tfrac1{10}=\tfrac{41}{150}$.

**Điểm cố định.** Giải $r=\tfrac45M_0r+\tfrac15v$ với $\sum_ir_i=1$. Trừ phương trình hàng D khỏi phương trình hàng B:
$$
r_{\mathrm B}-r_{\mathrm D}=\tfrac45\Big(\tfrac{r_{\mathrm D}}2-\tfrac{r_{\mathrm B}}2\Big),
$$
nên $\tfrac75(r_{\mathrm B}-r_{\mathrm D})=0$ và $r_{\mathrm B}=r_{\mathrm D}$; gọi giá trị chung là $\sigma$. Hàng C có cùng phần theo liên kết như hàng B nhưng thiếu $\tfrac1{10}$, nên $r_{\mathrm C}=\sigma-\tfrac1{10}$. Hàng B cho $\sigma=\tfrac4{15}r_{\mathrm A}+\tfrac25\sigma+\tfrac1{10}$, tức $\sigma=\tfrac49r_{\mathrm A}+\tfrac16$. Điều kiện tổng $r_{\mathrm A}+3\sigma-\tfrac1{10}=1$ trở thành $\tfrac73r_{\mathrm A}=\tfrac35$, nên
$$
r^*_v=\Big(\frac9{35},\frac{59}{210},\frac{19}{105},\frac{59}{210}\Big).
$$

| Trạng thái | A | B | C | D |
|---|---:|---:|---:|---:|
| $r^1$ | $1/5$ | $3/10$ | $1/5$ | $3/10$ |
| $r^2$ | $7/25$ | $41/150$ | $13/75$ | $41/150$ |
| $r^3$ | $31/125$ | $71/250$ | $23/125$ | $71/250$ |
| $r^*_v$ | $9/35$ | $59/210$ | $19/105$ | $59/210$ |

**Kiểm tra lại.** Hàng A: $\tfrac45\big(\tfrac12\cdot\tfrac{59}{210}+\tfrac{19}{105}\big)=\tfrac45\cdot\tfrac{135}{420}=\tfrac9{35}$; tổng $\tfrac{54+59+38+59}{210}=1$. MMDS viết cùng các số với mẫu chung: $54/210$, $59/210$, $38/210$, $59/210$.
:::

Trên G4, B và D đứng đầu với $59/210\approx0{,}281$; ở Ví dụ 03.13, A đứng đầu. A và C nằm ngoài $S$ nhưng vẫn có điểm dương, $9/35$ và $19/105$, vì chúng nhận điểm qua liên kết từ B và D.

::: remark Nhận xét 04.2 (Ba véc-tơ dễ nhầm)
Ví dụ 04.3 dùng ba véc-tơ có cùng $n$ thành phần nhưng vai trò khác nhau.

- $v$ là đầu vào cố định, chọn trước khi lặp: xác suất chọn trang $i$ khi bước dịch chuyển xảy ra. $v$ không phải kết quả PageRank.
- $r^0$ là điểm khởi tạo. MMDS khởi tạo $r^0=v$ và ghi rằng phân phối ban đầu không ảnh hưởng tới giới hạn, chỉ có thể giúp phép lặp hội tụ nhanh hơn (§5.3.2, tr.197); Định lý 04.5(b) chứng minh vế thứ nhất.
- $r^*_v$ là kết quả. Trang ngoài $S$ có $v_i=0$ nhưng có thể có $r^*_{v,i}>0$, như A và C trên G4.
:::

<!-- note-topic-id: lec-04-topic-03 -->
### 2.2 Thuật toán và tính đúng

Trên một đồ thị lớn lưu bằng danh sách kề, một vòng của Định nghĩa 04.1 là Thuật toán 03.10 với hai chỗ khác: khởi tạo bằng $v$ thay cho $u$, và phần chung $((1-\beta)+\beta\delta)/n$ của Bài 03 tách thành phần bù $\beta\delta/n$, giống nhau ở mọi trang, và phần dịch chuyển $(1-\beta)v_i$, khác nhau theo trang.

::: algorithm Thuật toán 04.3 (PageRank theo chủ đề)
**Đầu vào.** Danh sách kề của $G$: với mỗi trang $j$, danh sách $\mathrm{out}[j]$ các đích của $j$, không có phần tử lặp, nên $d_j$ là độ dài của $\mathrm{out}[j]$; $n\ge1$; phân phối dịch chuyển $v$; hằng số $0<\beta<1$; ngưỡng $\tau>0$; số vòng tối đa $K$ nguyên dương.

**Đầu ra.** Véc-tơ điểm $r$, số vòng đã chạy, độ thay đổi cuối $\Delta$ và trạng thái *đạt ngưỡng* hoặc *hết số vòng* (Bài 03 gọi là chưa đạt ngưỡng).

**Giả thiết.** Mọi đích trong các danh sách là trang của $V$; $v\ge0$, $\sum_iv_i=1$, và $v$ không đổi trong khi lặp.

1. Đặt $r_i\leftarrow v_i$ cho mọi $i$ và $t\leftarrow0$.
2. Tính $\delta\leftarrow\sum_{j:\,d_j=0}r_j$.
3. Đặt $\mathrm{new}_i\leftarrow\beta\delta/n+(1-\beta)v_i$ cho mọi $i$.
4. Với mỗi trang $j$ có $d_j>0$ và mỗi $i\in\mathrm{out}[j]$: $\mathrm{new}_i\leftarrow\mathrm{new}_i+\beta r_j/d_j$.
5. Tính $\Delta\leftarrow\sum_i\lvert\mathrm{new}_i-r_i\rvert$; đặt $r\leftarrow\mathrm{new}$ và $t\leftarrow t+1$.
6. Nếu $\Delta\le\tau$: trả $(r,t,\Delta)$ với trạng thái đạt ngưỡng. Nếu $t=K$: trả $(r,t,\Delta)$ với trạng thái hết số vòng. Ngược lại, quay lại bước 2.

**Dừng.** Mỗi vòng tăng $t$ thêm 1, nên thuật toán dừng sau không quá $K$ vòng.

**Trường hợp biên.** Nếu mọi trang là nút cụt thì $M_0=0$, $\delta=1$ ở mọi vòng, bước 4 không làm gì, và $r^1=\beta u+(1-\beta)v$; đây vẫn là một phân phối, và $r^2=r^1$, nên với $K\ge2$ thuật toán trả trạng thái đạt ngưỡng không muộn hơn vòng thứ hai. Khi $v=u$, thuật toán là Thuật toán 03.10, và mảng $v$ không cần lưu.

**Chi phí.** Mô hình đếm số lần thực hiện thân vòng lặp trong một vòng, mỗi lần một thao tác:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2 (tổng nút cụt) | $n$ trang | 1 | $n$ |
| 3 (bù và dịch chuyển) | $n$ trang | 1 | $n$ |
| 4 (cộng đóng góp) | $\ell$ cạnh | 1 | $\ell$ |
| 5 (độ thay đổi, thay mảng) | $n$ trang | 1 | $n$ |

Mỗi vòng tốn $3n+\ell$ thao tác, tức $\Theta(n+\ell)$; bộ nhớ làm việc gồm ba mảng $r$, $\mathrm{new}$, $v$, tức $24n$ byte theo mô hình 8 byte một điểm, cộng danh sách kề.
:::

```text
r[i] ← v[i] với mọi i
lặp t = 1, 2, ..., K:
    δ ← tổng r[j] trên các trang j có d[j] = 0
    với mọi i: new[i] ← β·δ / n + (1 − β)·v[i]
    với mỗi j có d[j] > 0:
        với mỗi i trong out[j]:
            new[i] ← new[i] + β·r[j] / d[j]
    Δ ← tổng |new[i] − r[i]| trên mọi i
    r ← new
    nếu Δ ≤ τ: trả (r, t, Δ, đạt ngưỡng)
trả (r, K, Δ, hết số vòng)
```

Thao tác quyết định vẫn là ghi vào mảng mới $\mathrm{new}$ trong khi chỉ đọc mảng cũ $r$, như Thuật toán 03.10. Trong một vòng, bước 3 là chỗ duy nhất $v$ đi vào phép tính, còn bước 1 dùng $v$ để khởi tạo; bước 4 không dùng tới chủ đề. Trên G4 với $v=(0,1/2,0,1/2)$, bước 3 của vòng đầu đặt $\mathrm{new}=(0,1/10,0,1/10)$, vì $\delta=0$, và bước 4 cộng $1/5$ vào mỗi trang, đúng bảng của Ví dụ 04.2. Thuật toán để ngỏ cách chọn $\tau$ và $K$.

Thuật toán đúng theo nghĩa sau: mỗi vòng tính đúng $F_v(r^t)$, mọi véc-tơ nó tạo ra là phân phối, và trạng thái trả về khớp điều kiện dừng.

::: proposition Mệnh đề 04.4 (Tính đúng và bảo toàn của Thuật toán 04.3)
**Giả thiết.** Đầu vào thỏa các điều kiện của Thuật toán 04.3; $F_v$ như Định nghĩa 04.1.

**Kết luận.**

- (a) Sau vòng thứ $t$, mảng $r$ bằng $r^t=F_v(r^{t-1})$, với $r^0=v$.
- (b) Với mọi phân phối $r$, $F_v(r)$ là một phân phối; do đó mọi $r^t$ của thuật toán là phân phối.
- (c) Thuật toán dừng sau không quá $K$ vòng, và trả trạng thái đạt ngưỡng khi và chỉ khi độ thay đổi $\Delta$ của vòng cuối không vượt $\tau$.

**Điều kiện áp dụng.** Số học chính xác; bước 4 không ghi vào $r$.

**Phạm vi.** Mệnh đề không nói dãy $r^t$ hội tụ, cũng không nói $r^t$ gần $r^*_v$; Định lý 04.5 trả lời hai điều này.
:::

::: proof
**Bước 1 (một vòng tính đúng $F_v$).** Chứng minh Mệnh đề 03.11 dùng bất biến: sau khi bước 4 đã xét một tập cạnh $E'\subseteq E$, $\mathrm{new}_i$ bằng phần chung cộng $\beta\sum_{(j\to i)\in E'}r^t_j/d_j$. Thay phần chung bằng $\beta\delta^t/n+(1-\beta)v_i$ của bước 3, bất biến đúng trước cạnh đầu tiên và được giữ qua mỗi cạnh vì bước 4 chỉ cộng $\beta r_j/d_j$ vào $\mathrm{new}_i$ và không bước nào ghi vào $r$ trước bước 5. Khi $E'=E$,
$$
\begin{aligned}
\mathrm{new}_i&=\beta\sum_{j:\,j\to i}\frac{r^t_j}{d_j}+\frac{\beta\delta^t}n\\
&\quad+(1-\beta)v_i\\
&=F_v(r^t)_i
\end{aligned}
$$
theo Định nghĩa 04.1. Quy nạp theo số vòng, với $r^0=v$ ở bước 1, cho (a).

**Bước 2 (không âm).** Mọi hệ số $\beta$, $1-\beta$, $1/d_j$, $1/n$ và mọi thành phần $r_j$, $\delta$, $v_i$ đều không âm, nên $F_v(r)\ge0$.

**Bước 3 (ba phần của tổng).** Cột $j$ của $M_0$ có tổng 1 khi $j\notin\mathcal D$ và tổng 0 khi $j\in\mathcal D$, nên $\sum_i(\beta M_0r)_i=\beta\sum_{j\notin\mathcal D}r_j=\beta(1-\delta)$ khi $\sum_jr_j=1$. Cộng theo $i$:
$$
\begin{aligned}
\sum_iF_v(r)_i&=\beta(1-\delta)\\
&\quad+\beta\delta\sum_iu_i\\
&\quad+(1-\beta)\sum_iv_i\\
&=\beta(1-\delta)+\beta\delta\\
&\quad+(1-\beta)=1.
\end{aligned}
$$
Dòng thứ hai dùng $\sum_iu_i=1$ và $\sum_iv_i=1$.

**Bước 4 (mọi vòng).** $r^0=v$ là phân phối theo giả thiết; nếu $r^t$ là phân phối thì $r^{t+1}=F_v(r^t)$ là phân phối theo Bước 2 và Bước 3. Quy nạp theo $t$ cho (b).

**Bước 5 (dừng và trạng thái).** Bước 5 và bước 6 của Thuật toán 04.3 trùng bước 5 và bước 6 của Thuật toán 03.10, nên lập luận ở Bước 4 của chứng minh Mệnh đề 03.11 cho (c). $\square$
:::

Ba phần của Bước 3 là phần đi theo liên kết, phần bù nút cụt và phần dịch chuyển; chỉ phần thứ ba khác Mệnh đề 03.13, và nó cần đúng một điều kiện mới, $\sum_iv_i=1$. Mệnh đề 04.4 cần ba giả thiết; với $\beta=4/5$, bỏ từng giả thiết cho một phản ví dụ.

- Bỏ $\sum_iv_i=1$: nếu quên chia cho $\lvert S\rvert$ và dùng $v=(0,1,0,1)$, vòng đầu từ $r^0=v$ cho $(2/5,3/5,2/5,3/5)$ với tổng 2, và mọi vòng sau cũng có tổng 2. Vì $F_v$ tuyến tính theo phần dịch chuyển, điểm cố định của phép lặp này là $2r^*_v=(18/35,59/105,38/105,59/105)$: thứ tự trang đúng nhưng các điểm không còn là phân phối.
- Bỏ cập nhật đồng bộ, tức "bước 4 không ghi vào $r$": nếu tính lần lượt A, B, C, D từ $r^0=v$ và dùng ngay mỗi điểm vừa tính, vòng đầu cho $(1/5,53/150,19/75,221/750)$ với tổng $413/375$, thay cho $r^1=(1/5,3/10,1/5,3/10)$.
- Bỏ bù nút cụt: trên biến thể của G4 trong đó C là nút cụt (Ví dụ 03.10), với $v=u$ và $r^0=u$, ta có $\delta^0=1/4$, và bỏ số hạng $\beta\delta u$ làm tổng sau một vòng còn $1-\beta\delta^0=4/5$.

Bước 1 của chứng minh dùng cập nhật đồng bộ; Bước 3 dùng phần bù và $\sum_iv_i=1$; Bước 4 dùng $r^0=v$ là phân phối.

<!-- note-topic-id: lec-04-topic-04 -->
### 2.3 Hội tụ và cận sai số

Mệnh đề 04.4 bảo đảm mỗi $r^t$ là một phân phối, nhưng chưa cho biết dãy có giới hạn, giới hạn có phụ thuộc $r^0$ không, và khi nào dừng thì đủ gần giới hạn. Trên G4, ba vòng đầu $r^1$, $r^2$, $r^3$ của Ví dụ 04.3 tiến dần tới $r^*_v$; muốn có bảo đảm cho mọi đồ thị, ta cần lập luận co của Bài 03. Nhận xét 03.18 đã ghi rằng cận của Hệ quả 03.16 còn đúng khi phân phối đều được thay bằng một phân phối khác; định lý sau mở rộng cả Định lý 03.15 cho $F_v$ và chỉ ra hai chỗ cần thay.

::: theorem Định lý 04.5 (Hội tụ và cận sai số với phân phối dịch chuyển bất kỳ)
**Giả thiết.** $G$ là đồ thị web hữu hạn với $n\ge1$; $0<\beta<1$; $v$ là một phân phối trên $V$ không phụ thuộc $r$; $F_v(r)=\beta\bar Mr+(1-\beta)v$ như Định nghĩa 04.1; $r^0$ là một phân phối và $r^{t+1}=F_v(r^t)$ với mọi $t\ge0$; $\Delta_t=\lVert r^{t+1}-r^t\rVert_1$.

**Kết luận.**

- (a) $\lVert F_v(r)-F_v(r')\rVert_1\le\beta\lVert r-r'\rVert_1$ với mọi $r,r'\in\mathbb R^n$.
- (b) Có đúng một $r^*_v\in\mathbb R^n$ thỏa $r^*_v=F_v(r^*_v)$; $r^*_v$ là một phân phối và không phụ thuộc $r^0$.
- (c) $\lVert r^t-r^*_v\rVert_1\le\beta^t\lVert r^0-r^*_v\rVert_1\le2\beta^t$ với mọi $t\ge0$.
- (d) $\lVert r^{t+1}-r^*_v\rVert_1\le\dfrac{\beta}{1-\beta}\Delta_t$ với mọi $t\ge0$; do đó nếu Thuật toán 04.3 dùng ngưỡng $\tau\le(1-\beta)\varepsilon/\beta$ và trả trạng thái đạt ngưỡng thì véc-tơ trả về cách $r^*_v$ không quá $\varepsilon$.

**Điều kiện áp dụng.** Số học chính xác; mỗi vòng là một phép cập nhật đồng bộ của Định nghĩa 04.1.

**Phạm vi.** Định lý không áp dụng cho $\beta=1$. Các cận đúng cho mọi đồ thị và mọi phân phối dịch chuyển; trên một đồ thị cụ thể, dãy có thể hội tụ nhanh hơn. Khi thuật toán dừng vì hết $K$ vòng, (d) vẫn cho sai số không quá $\beta\Delta/(1-\beta)$ với $\Delta$ cuối, nhưng không bảo đảm sai số $\varepsilon$.
:::

::: proof
Bước 1–5 đi theo các bước cùng tên của chứng minh Định lý 03.15, với cận theo 2 (Bước 6 của Bài 03) gộp vào Bước 5; Bước 6 đi theo chứng minh Hệ quả 03.16. Phân phối đều $u$ trong phần dịch chuyển được thay bằng $v$, và chỉ hai bước dùng tới phần này.

**Bước 1 (tính co; khác Bài 03 ở phần dịch chuyển).** Phần $(1-\beta)v$ không phụ thuộc véc-tơ nên triệt tiêu trong hiệu: $F_v(r)-F_v(r')=\beta\bar M(r-r')$. Ma trận $\bar M$ không âm và có mọi cột tổng 1 (Mệnh đề 03.9(a)), nên Bổ đề 03.14 cho
$$
\begin{aligned}
&\lVert F_v(r)-F_v(r')\rVert_1\\
&\quad=\beta\lVert\bar M(r-r')\rVert_1\\
&\quad\le\beta\lVert r-r'\rVert_1 .
\end{aligned}
$$
Đó là (a). Bước này dùng giả thiết $v$ không phụ thuộc $r$.

**Bước 2 (tồn tại và duy nhất).** Như Bước 2 của Định lý 03.15: ma trận $\mathrm I_n-\beta\bar M$ khả nghịch vì $\beta<1$, nên $r=F_v(r)$ có đúng một nghiệm $r^*_v=(1-\beta)(\mathrm I_n-\beta\bar M)^{-1}v$. Nghiệm này chỉ phụ thuộc $G$, $\beta$, $v$, không phụ thuộc $r^0$.

**Bước 3 (tổng bằng 1; khác Bài 03 ở phần dịch chuyển).** Nhân hai vế của $r^*_v=\beta\bar Mr^*_v+(1-\beta)v$ với $\mathbf 1^{\mathsf T}$, dùng $\mathbf 1^{\mathsf T}\bar M=\mathbf 1^{\mathsf T}$ và $\mathbf 1^{\mathsf T}v=1$:
$$
\mathbf 1^{\mathsf T}r^*_v=\beta\,\mathbf 1^{\mathsf T}r^*_v+(1-\beta),
$$
nên $\sum_ir^*_{v,i}=1$. Bước này dùng giả thiết $\sum_iv_i=1$.

**Bước 4 (tốc độ).** $r^{t+1}-r^*_v=F_v(r^t)-F_v(r^*_v)$, nên theo (a), $\lVert r^{t+1}-r^*_v\rVert_1\le\beta\lVert r^t-r^*_v\rVert_1$; quy nạp theo $t$ cho vế trái của (c).

**Bước 5 (không âm).** Mọi $r^t$ là phân phối (Mệnh đề 04.4(b)). Nếu $r^*_{v,i}<0$ với một $i$ thì $\lVert r^t-r^*_v\rVert_1\ge-r^*_{v,i}>0$ với mọi $t$, trái với Bước 4. Cùng Bước 3, $r^*_v$ là phân phối; Bước 2, 3, 5 cho (b). Hai phân phối cách nhau không quá $2$ theo $\lVert\cdot\rVert_1$, nên (c) đúng.

**Bước 6 (cận theo độ thay đổi).** Như chứng minh Hệ quả 03.16:
$$
\begin{aligned}
&\lVert r^{t+1}-r^*_v\rVert_1\\
&\quad\le\beta\lVert r^t-r^*_v\rVert_1\\
&\quad\le\beta\Delta_t+\beta\lVert r^{t+1}-r^*_v\rVert_1 .
\end{aligned}
$$
Dòng thứ nhất là Bước 4; dòng thứ hai dùng bất đẳng thức tam giác $\lVert r^t-r^*_v\rVert_1\le\Delta_t+\lVert r^{t+1}-r^*_v\rVert_1$. Chuyển vế và chia cho $1-\beta>0$ được (d). Khi thuật toán trả trạng thái đạt ngưỡng, véc-tơ trả về là $r^{t+1}$ với $\Delta_t\le\tau$, nên sai số không quá $\beta\tau/(1-\beta)\le\varepsilon$. $\square$
:::

Định lý 04.5 với $v=u$ là Định lý 03.15 cộng Hệ quả 03.16; nó mở rộng hai kết quả đó cho mọi phân phối dịch chuyển mà không thêm giả thiết nào về đồ thị. Cái giá duy nhất là hai điều kiện mới về $v$: không phụ thuộc $r$ và có tổng 1. Bỏ một trong ba giả thiết sau thì kết luận sai.

- Bỏ "$v$ không phụ thuộc $r$": trên đồ thị hai trang chỉ gồm hai khuyên $\mathrm A\to\mathrm A$ và $\mathrm B\to\mathrm B$, ta có $\bar M=\mathrm I_2$. Nếu chọn $v(r)=r$, tức dịch chuyển tới chính phân phối hiện tại, thì $F(r)=\beta r+(1-\beta)r=r$ với mọi $r$, nên mọi phân phối là điểm cố định và (b) sai.
- Bỏ $\sum_iv_i=1$: với $v=(0,1,0,1)$ trên G4, điểm cố định là $2r^*_v$, tổng 2 (sau Mệnh đề 04.4), nên (b) sai ở chỗ "$r^*_v$ là một phân phối".
- Bỏ $\beta<1$: với $\beta=1$, phần dịch chuyển biến mất và phép lặp là lặp thô của Bài 03; trên đồ thị hai trang $\mathrm A\rightleftarrows\mathrm B$, từ $r^0=(1,0)$ dãy luân phiên $(0,1)$, $(1,0)$ và không có giới hạn.

Bước 1 dùng giả thiết thứ nhất; Bước 3 dùng giả thiết thứ hai; Bước 2, Bước 4 và Bước 6 dùng $\beta<1$. Ví dụ sau so cận (d) với sai số thật trên G4.

::: example Ví dụ 04.4 (Cận sai số của $r^2$ trên G4)
**Dữ kiện.** G4, $\beta=4/5$, $v=(0,1/2,0,1/2)$; theo Ví dụ 04.3, $r^1=(1/5,3/10,1/5,3/10)$, $r^2=(7/25,41/150,13/75,41/150)$ và $r^*_v=(9/35,59/210,19/105,59/210)$.

**Độ thay đổi.** $r^2-r^1=(2/25,-2/75,-2/75,-2/75)$, nên
$$
\Delta_1=\frac2{25}+3\cdot\frac2{75}=\frac4{25}.
$$

**Cận.** Định lý 04.5(d) với $\beta/(1-\beta)=4$ cho $\lVert r^2-r^*_v\rVert_1\le4\Delta_1=16/25$.

**Sai số thật.** $\lvert\tfrac7{25}-\tfrac9{35}\rvert=\tfrac4{175}$; mỗi thành phần B, C, D lệch $\tfrac4{525}$. Do đó $\lVert r^2-r^*_v\rVert_1=\tfrac4{175}+\tfrac{12}{525}=\tfrac8{175}\approx0{,}046$.

**Ngưỡng dừng.** Để bảo đảm sai số $\varepsilon$, đủ chọn $\tau=(1-\beta)\varepsilon/\beta=\varepsilon/4$.

**Kiểm tra lại.** $\tfrac8{175}\le\tfrac{16}{25}=\tfrac{112}{175}$: cận lớn hơn sai số thật 14 lần, đúng tỷ số của Ví dụ 03.13 với phân phối đều.
:::

Trong thực hành, Định lý 04.5 cho phép mỗi chủ đề dùng cùng tiêu chí dừng như PageRank toàn cục: ngưỡng $\tau=(1-\beta)\varepsilon/\beta$ bảo đảm sai số $\varepsilon$ bất kể tập chủ đề nào, và cận $2\beta^t$ cho số vòng đủ dùng cho mọi chủ đề. Với $\beta=0{,}8$ và $\varepsilon=10^{-8}$, cận này cho 86 vòng như Ví dụ 03.13, vì cận không phụ thuộc $v$. Giả thiết "$v$ không phụ thuộc $r$" được bảo đảm khi $v$ được chọn xong trước khi lặp và giữ nguyên qua các vòng, như bước 1 và bước 3 của Thuật toán 04.3.

<!-- note-topic-id: lec-04-topic-05 -->
### 2.4 Ghép nhiều chủ đề

Định lý 04.5 cho một véc-tơ đúng cho mỗi phân phối dịch chuyển, trong khi mỗi truy vấn có một tổ hợp mức quan tâm riêng tới các chủ đề. MMDS đề xuất trộn các véc-tơ chủ đề theo tỷ lệ các trang người dùng vừa xem thuộc mỗi chủ đề (§5.3.4, tr.199). Tính lại PageRank cho từng tổ hợp khi truy vấn đến tốn $\Theta(K(n+\ell))$ thao tác, với $K$ vòng trên toàn web. Chúng ta cần biết có thể tính trước một véc-tơ cho mỗi chủ đề rồi ghép các véc-tơ đó khi truy vấn đến hay không.

Gọi $k$ là số chủ đề, $\theta=1,\dots,k$ là chỉ số chủ đề, $v^{(\theta)}$ là phân phối dịch chuyển của chủ đề $\theta$ và $r^{(\theta)}=r^*_{v^{(\theta)}}$ là PageRank theo chủ đề tương ứng. Mức quan tâm là các trọng số $w_\theta\ge0$ với $\sum_\theta w_\theta=1$; chỉ số $\theta$ trong ngoặc phân biệt nhãn chủ đề với chỉ số vòng $t$. Ví dụ sau ghép chủ đề $\{\mathrm B,\mathrm D\}$ với PageRank toàn cục trên G4.

::: example Ví dụ 04.5 (Ghép chủ đề $\{\mathrm B,\mathrm D\}$ với PageRank toàn cục)
**Dữ kiện.** G4, $\beta=4/5$. Chủ đề 1 có $v^{(1)}=(0,1/2,0,1/2)$ và $r^{(1)}=(9/35,59/210,19/105,59/210)$ (Ví dụ 04.3); chủ đề 2 là PageRank toàn cục, $v^{(2)}=u$ và $r^{(2)}=(9/28,19/84,19/84,19/84)$ (Ví dụ 03.13). Trọng số $w=(1/3,2/3)$.

**Phân phối ghép.** $v=\tfrac13v^{(1)}+\tfrac23u=(1/6,1/3,1/6,1/3)$.

**Giải trực tiếp $r=F_v(r)$.** Hàng B và hàng D có cùng dạng nên $r_{\mathrm B}=r_{\mathrm D}=\sigma$, như Ví dụ 04.3. Hàng B: $\sigma=\tfrac4{15}r_{\mathrm A}+\tfrac25\sigma+\tfrac1{15}$, nên $\sigma=\tfrac49r_{\mathrm A}+\tfrac19$. Hàng C có cùng phần theo liên kết như hàng B, nhưng phần dịch chuyển $\tfrac15\cdot\tfrac16=\tfrac1{30}$ thay cho $\tfrac1{15}$, nên $r_{\mathrm C}=\sigma-\tfrac1{30}$. Điều kiện tổng $r_{\mathrm A}+3\sigma-\tfrac1{30}=1$ cho $\tfrac73r_{\mathrm A}=\tfrac7{10}$, nên
$$
r^*_v=\Big(\frac3{10},\frac{11}{45},\frac{19}{90},\frac{11}{45}\Big).
$$

**Ghép hai véc-tơ đã có.**

- A: $\tfrac13\cdot\tfrac9{35}+\tfrac23\cdot\tfrac9{28}=\tfrac3{35}+\tfrac3{14}=\tfrac3{10}$.
- B, D: $\tfrac13\cdot\tfrac{59}{210}+\tfrac23\cdot\tfrac{19}{84}=\tfrac{59}{630}+\tfrac{95}{630}=\tfrac{11}{45}$.
- C: $\tfrac13\cdot\tfrac{19}{105}+\tfrac23\cdot\tfrac{19}{84}=\tfrac{38}{630}+\tfrac{95}{630}=\tfrac{19}{90}$.

**Kiểm tra lại.** Hai cách cho cùng véc-tơ; tổng $\tfrac{27+22+19+22}{90}=1$.
:::

Mệnh đề sau chứng minh đẳng thức này cho mọi đồ thị, và cho cả trường hợp các véc-tơ chủ đề được lưu dưới dạng xấp xỉ.

::: proposition Mệnh đề 04.6 (Tuyến tính theo phân phối dịch chuyển)
**Giả thiết.** $G$, $\beta$ và $\bar M$ như Định lý 04.5, dùng chung cho mọi chủ đề; $v^{(1)},\dots,v^{(k)}$ là các phân phối dịch chuyển và $r^{(\theta)}=r^*_{v^{(\theta)}}$; $w_\theta\ge0$, $\sum_\theta w_\theta=1$; $v=\sum_\theta w_\theta v^{(\theta)}$.

**Kết luận.**

- (a) $v$ là một phân phối dịch chuyển và $r^*_v=\sum_{\theta=1}^kw_\theta r^{(\theta)}$.
- (b) Nếu $\hat r^{(\theta)}$ là các véc-tơ xấp xỉ $r^{(\theta)}$ thì
$$
\begin{aligned}
&\Big\lVert\sum_\theta w_\theta\hat r^{(\theta)}-r^*_v\Big\rVert_1\\
&\quad\le\sum_\theta w_\theta\big\lVert\hat r^{(\theta)}-r^{(\theta)}\big\rVert_1 .
\end{aligned}
$$

**Điều kiện áp dụng.** Số học chính xác; mọi chủ đề dùng cùng đồ thị, cùng $\beta$ và cùng quy tắc bù nút cụt theo $u$.

**Phạm vi.** Kết luận nói về các điểm cố định. Với các vòng lặp hữu hạn, $\sum_\theta w_\theta r^{t,(\theta)}=r^t$ ở mọi vòng $t$ khi $\sum_\theta w_\theta r^{0,(\theta)}=r^0$, chẳng hạn khi khởi tạo bằng $v^{(\theta)}$ và $v$ như Thuật toán 04.3.
:::

::: proof
**Bước 1 ($v$ là phân phối).** $v\ge0$ vì mọi $w_\theta\ge0$ và $v^{(\theta)}\ge0$; $\sum_iv_i=\sum_\theta w_\theta\sum_iv^{(\theta)}_i=\sum_\theta w_\theta=1$.

**Bước 2 (tổ hợp là điểm cố định).** Đặt $g=\sum_\theta w_\theta r^{(\theta)}$. Mỗi $r^{(\theta)}$ thỏa $r^{(\theta)}=\beta\bar Mr^{(\theta)}+(1-\beta)v^{(\theta)}$. Nhân phương trình thứ $\theta$ với $w_\theta$ rồi cộng, dùng tính tuyến tính của phép nhân với $\bar M$:
$$
\begin{aligned}
g&=\beta\bar M\sum_\theta w_\theta r^{(\theta)}\\
&\quad+(1-\beta)\sum_\theta w_\theta v^{(\theta)}\\
&=\beta\bar Mg+(1-\beta)v\\
&=F_v(g).
\end{aligned}
$$
Dòng thứ nhất cần $\bar M$ và $\beta$ chung cho mọi $\theta$ để đưa ra ngoài tổng.

**Bước 3 (duy nhất).** Theo Định lý 04.5(b), $F_v$ có đúng một điểm cố định, nên $g=r^*_v$. Đó là (a).

**Bước 4 (xấp xỉ).** Theo (a), $\sum_\theta w_\theta\hat r^{(\theta)}-r^*_v=\sum_\theta w_\theta\big(\hat r^{(\theta)}-r^{(\theta)}\big)$; bất đẳng thức tam giác và $w_\theta\ge0$ cho (b). $\square$
:::

Theo Bước 2 của chứng minh Định lý 04.5, $r^*_v=(1-\beta)(\mathrm I_n-\beta\bar M)^{-1}v$ là một hàm tuyến tính của $v$; Mệnh đề 04.6(a) là tính chất này viết cho tổ hợp lồi các phân phối: phân phối ghép cho véc-tơ ghép. Nhờ (b), nếu mỗi véc-tơ chủ đề được tính tới sai số $\varepsilon$ bằng ngưỡng của Định lý 04.5(d) thì véc-tơ ghép cũng có sai số không quá $\varepsilon$. Hai giả thiết "cùng $\beta$" và "bù theo $u$" không bỏ được:

- Bỏ "cùng $\beta$": trên G4, chủ đề $\{\mathrm B,\mathrm D\}$ với $\beta=4/5$ cho $r^*_v$ của Ví dụ 04.3, chủ đề $\{\mathrm C\}$ với $\beta=1/2$ cho $(3/10,1/15,17/30,1/15)$. Trung bình hai véc-tơ là $(39/140,73/420,157/420,73/420)$, trong khi PageRank với $v=\tfrac12v_{\{\mathrm B,\mathrm D\}}+\tfrac12v_{\{\mathrm C\}}=(0,1/4,1/2,1/4)$ và $\beta=4/5$ có thành phần A bằng $3/10=42/140$, khác $39/140$.
- Bỏ "bù theo $u$": trên biến thể của G4 trong đó C là nút cụt (Ví dụ 03.10), với $\beta=1/2$, xét hai chủ đề $\{\mathrm A\}$, $\{\mathrm C\}$ và $w=(1/2,1/2)$. Bù theo $u$ thì hai cách cho cùng véc-tơ. Nếu phần điểm của nút cụt được chia theo phân phối dịch chuyển của từng chủ đề, ma trận $\bar M$ đổi theo chủ đề: PageRank với $v$ đều trên $\{\mathrm A,\mathrm C\}$ là $(18/47,4/47,21/47,4/47)$, còn trung bình hai véc-tơ chủ đề là $(3/10,1/15,17/30,1/15)$, trùng với véc-tơ ở gạch trên; thành phần A là $18/47\approx0{,}383$ so với $0{,}3$.

Bước 2 của chứng minh dùng cả hai giả thiết: chỉ khi $\beta$ và $\bar M$ chung cho mọi chủ đề thì toán tử mới đưa ra ngoài tổng được. Đây là lý do Định nghĩa 04.1 giữ phần bù theo $u$.

<!-- note-topic-id: lec-04-topic-06 -->
### 2.5 Chi phí tiền tính và truy vấn

Mệnh đề 04.6 tách công việc thành hai pha. Trước khi có truy vấn, ta tính và lưu $k$ véc-tơ $r^{(\theta)}$ trên toàn web. Khi có truy vấn, máy tìm kiếm đã có tập trang ứng viên $C$, với $c=\lvert C\rvert$, và các trọng số $w_\theta$ của truy vấn; với mỗi $i\in C$, nó tính *điểm ghép*
$$
q_i=\sum_{\theta=1}^kw_\theta r^{(\theta)}_i,
$$
và theo Mệnh đề 04.6(a), $q_i$ đúng bằng thành phần $i$ của PageRank với phân phối dịch chuyển $\sum_\theta w_\theta v^{(\theta)}$.

![Tiền tính và xếp hạng truy vấn. Hàng trên, tiền tính: chọn chủ đề, chọn tập dịch chuyển, tính và lưu véc-tơ điểm. Hàng dưới, truy vấn: trọng số chủ đề, lấy hoặc ghép điểm đã lưu, xếp hạng ứng viên. Một mũi tên "điểm đã lưu" nối hàng trên xuống hàng dưới.](img/lec-04/tien-tinh-va-truy-van.svg)

Hình tách hai pha theo thời điểm chạy: hàng trên chạy một lần cho mọi truy vấn, hàng dưới chạy cho mỗi truy vấn và chỉ đọc các điểm đã lưu. Mệnh đề sau đếm chi phí của từng pha.

::: proposition Mệnh đề 04.7 (Chi phí PageRank theo chủ đề)
**Giả thiết.** Mô hình chi phí đơn vị cho mỗi phép toán vô hướng; đầu vào là danh sách kề của $G$; chủ đề $\theta$ được tính bằng Thuật toán 04.3 và thực chạy $K_\theta\le K$ vòng; truy vấn có tập ứng viên $C$ đã biết, $c=\lvert C\rvert$, và $k$ trọng số đã biết.

**Kết luận.**

- (a) Tiền tính $k$ véc-tơ tốn $\Theta\big((\sum_\theta K_\theta)(n+\ell)\big)$ thao tác, không quá $O(kK(n+\ell))$; nếu mọi chủ đề chạy đủ $K$ vòng thì bằng $\Theta(kK(n+\ell))$.
- (b) Bộ nhớ khi tiền tính gồm đầu vào $\Theta(n+\ell)$ và bộ nhớ làm việc $\Theta(n)$ cho một chủ đề tại một thời điểm; kết quả lưu gồm $kn$ số.
- (c) Ghép điểm cho một truy vấn tốn $\Theta(kc)$ thao tác.

**Điều kiện áp dụng.** Các chủ đề được tính lần lượt, mỗi lần dùng lại cùng danh sách kề.

**Phạm vi.** Phép đếm không gồm việc tìm tập ứng viên $C$, suy ra trọng số từ truy vấn và sắp xếp $c$ điểm ghép. Mệnh đề không chặn $K_\theta$; $K_\theta$ phụ thuộc đồ thị và $\tau$.
:::

::: proof
**Bước 1 (tiền tính).** Theo bảng chi phí của Thuật toán 04.3, mỗi vòng tốn $3n+\ell$ thao tác. Chủ đề $\theta$ chạy $K_\theta$ vòng, nên tổng là $(3n+\ell)\sum_\theta K_\theta=\Theta\big((\sum_\theta K_\theta)(n+\ell)\big)$; vì $K_\theta\le K$, tổng không quá $(3n+\ell)kK$. Đó là (a).

**Bước 2 (bộ nhớ).** Một lần chạy cần danh sách kề và ba mảng độ dài $n$; véc-tơ kết quả của chủ đề $\theta$ được ghi ra trước khi chạy chủ đề $\theta+1$, nên tổng kết quả là $kn$ số. Đó là (b).

**Bước 3 (truy vấn).** Với mỗi $i\in C$, $q_i$ cần đọc $k$ điểm đã lưu và $k$ trọng số, $k$ phép nhân và $k-1$ phép cộng, tức $2k-1$ thao tác; trên $c$ ứng viên là $c(2k-1)=\Theta(kc)$. Đó là (c). $\square$
:::

Mệnh đề 04.7 cho thấy cái giá của tiền tính tăng tuyến tính theo số chủ đề $k$ và không phụ thuộc số người dùng, còn cái giá của một truy vấn không phụ thuộc $n$ hay $\ell$. So với Ví dụ 04.1, phần lưu riêng của mỗi người dùng giảm từ $n$ số xuống $k$ trọng số. Hai tính chất này cần Mệnh đề 04.6: không có tính tuyến tính, mỗi tổ hợp trọng số mới đòi một lần lặp $\Theta(K(n+\ell))$.

::: remark Nhận xét 04.8 (Trong thực hành: chủ đề, trọng số và tiền tính)
- MMDS nêu bốn bước dùng PageRank theo chủ đề trong máy tìm kiếm (§5.3.3, tr.197–198): chọn các chủ đề; chọn tập dịch chuyển cho mỗi chủ đề và tính véc-tơ tương ứng; xác định chủ đề liên quan tới truy vấn; dùng véc-tơ của các chủ đề đó khi sắp kết quả. Hai bước đầu là pha tiền tính của Mệnh đề 04.7; hai bước sau là pha truy vấn.
- Một tập chủ đề MMDS dùng làm ví dụ là 16 hạng mục cấp cao nhất của danh mục mở DMOZ, như thể thao, y học, nên có 16 véc-tơ (Ví dụ 5.9, tr.196).
- Trọng số $w_\theta$ là đầu vào của phép ghép. MMDS nêu ba cách xác định chủ đề của truy vấn: người dùng chọn từ một danh sách; suy ra từ các từ trong những trang người dùng vừa xem hoặc những truy vấn gần đây; suy ra từ thông tin về người dùng (§5.3.3, tr.198). Cách thứ hai cần phân loại một trang theo chủ đề bằng độ tương đồng Jaccard giữa tập từ của trang và tập từ đặc trưng của chủ đề (§5.3.4, tr.198–199); độ tương đồng này là chủ đề của Bài 05.
- Mệnh đề 04.6 chỉ đúng khi mọi chủ đề dùng cùng $\beta$ và cùng quy tắc bù; một hệ thống tính các chủ đề ở những thời điểm khác nhau phải giữ cả hai cố định, và cũng phải dùng cùng một đồ thị.
- Các véc-tơ lưu là xấp xỉ $\hat r^{(\theta)}$ tại vòng dừng; theo Mệnh đề 04.6(b), dừng mỗi chủ đề ở sai số $\varepsilon$ đủ cho sai số $\varepsilon$ của mọi phép ghép.
:::

::: exercise Bài tập 04.2 (Vòng thứ tư và cận sai số trên G4)
Trên G4 với $\beta=4/5$ và tập chủ đề $S=\{\mathrm B,\mathrm D\}$, cho $r^3=(31/125,71/250,23/125,71/250)$ và $r^*_v=(9/35,59/210,19/105,59/210)$.

- (a) Tính $r^4_{\mathrm C}$, nêu các trang đóng góp vào nó, rồi tính cả véc-tơ $r^4$.
- (b) Tính $\Delta_3=\lVert r^4-r^3\rVert_1$, cận của Định lý 04.5(d) cho $\lVert r^4-r^*_v\rVert_1$ và sai số thật $\lVert r^4-r^*_v\rVert_1$.
- (c) Đánh giá mệnh đề "trong PageRank theo chủ đề, một trang ngoài tập chủ đề luôn có điểm bằng 0".
:::

::: hint
C nhận điểm qua cạnh $\mathrm A\to\mathrm C$ và $\mathrm D\to\mathrm C$ và không nằm trong $S$. Với $\beta=4/5$, hệ số của cận là $\beta/(1-\beta)=4$.
:::

::: solution
**Câu (a).** C nhận từ A (bậc ra 3) phần $\tfrac13\cdot\tfrac{31}{125}=\tfrac{31}{375}$ và từ D (bậc ra 2) phần $\tfrac12\cdot\tfrac{71}{250}=\tfrac{71}{500}$, không có phần dịch chuyển:
$$
\begin{aligned}
r^4_{\mathrm C}&=\frac45\Big(\frac{31}{375}+\frac{71}{500}\Big)\\
&=\frac45\cdot\frac{337}{1500}=\frac{337}{1875}.
\end{aligned}
$$
Tương tự, $r^4_{\mathrm A}=\tfrac45\big(\tfrac12\cdot\tfrac{71}{250}+\tfrac{23}{125}\big)=\tfrac45\cdot\tfrac{163}{500}=\tfrac{163}{625}$, và B, D nhận cùng phần theo liên kết như C cộng phần dịch chuyển $\tfrac1{10}$: $r^4_{\mathrm B}=r^4_{\mathrm D}=\tfrac{337}{1875}+\tfrac1{10}=\tfrac{1049}{3750}$. Vậy
$$
\begin{aligned}
r^4=\Big(&\frac{163}{625},\frac{1049}{3750},\\
&\frac{337}{1875},\frac{1049}{3750}\Big).
\end{aligned}
$$

**Câu (b).** $r^4-r^3=(8/625,-8/1875,-8/1875,-8/1875)$, nên $\Delta_3=\tfrac8{625}+\tfrac{24}{1875}=\tfrac{16}{625}$, và cận là $4\Delta_3=\tfrac{64}{625}=0{,}1024$. Sai số thật: $\lvert\tfrac{163}{625}-\tfrac9{35}\rvert=\tfrac{16}{4375}$, mỗi thành phần B, C, D lệch $\tfrac{16}{13125}$, nên $\lVert r^4-r^*_v\rVert_1=\tfrac{16}{4375}+\tfrac{48}{13125}=\tfrac{32}{4375}\approx0{,}0073$.

**Câu (c).** Mệnh đề sai: $\mathrm C\notin S$ nhưng $r^*_{v,\mathrm C}=19/105>0$, vì C nhận điểm qua cạnh từ A và D, hai trang có điểm dương. Theo Định nghĩa 04.1, một trang $i\notin S$ có $r^*_{v,i}=\beta\sum_{j\to i}r^*_{v,j}/d_j+\beta\delta/n$; trên đồ thị không có nút cụt, trang ngoài $S$ có điểm 0 khi mọi trang trỏ tới nó có điểm 0, chẳng hạn khi nó không có liên kết vào.

**Kiểm tra lại.** Tổng $r^4$ là $\tfrac{978+1049+674+1049}{3750}=1$. Sai số thật giảm từ $\tfrac8{175}$ của $r^2$ (Ví dụ 04.4) xuống $\tfrac{32}{4375}=\big(\tfrac25\big)^2\cdot\tfrac8{175}$, nhanh hơn cận $\beta^t$ của Định lý 04.5(c).
:::

::: exercise Bài tập 04.3 (Tập dịch chuyển $\{\mathrm C\}$ và phép ghép)
Giữ G4 và $\beta=4/5$, đổi tập chủ đề từ $\{\mathrm B,\mathrm D\}$ sang $\{\mathrm C\}$.

- (a) Xác định các đại lượng của Thuật toán 04.3 thay đổi và các đại lượng giữ nguyên.
- (b) Tính PageRank theo chủ đề $r^*_v$ với tập chủ đề $\{\mathrm C\}$.
- (c) Không giải hệ mới, dùng (b), PageRank $(9/28,19/84,19/84,19/84)$ của Ví dụ 03.13 và Mệnh đề 04.6 để tính PageRank với phân phối dịch chuyển $(1/8,1/8,5/8,1/8)$.
- (d) Hai véc-tơ của (c) đã được lưu. Đếm số thao tác ghép điểm cho một truy vấn có ba trang ứng viên.
:::

::: hint
Chỉ phân phối dịch chuyển và khởi tạo đổi; trong hệ phương trình, hàng B và hàng D vẫn có cùng dạng. Với (c), viết $(1/8,1/8,5/8,1/8)$ thành tổ hợp của $(0,0,1,0)$ và $u$.
:::

::: solution
**Câu (a).** Đồ thị, $M_0$, $\beta=4/5$ và quy tắc bù giữ nguyên; G4 không có nút cụt nên $\delta=0$. Phân phối dịch chuyển đổi từ $(0,1/2,0,1/2)$ sang $v=(0,0,1,0)$, và khởi tạo $r^0=v$ của bước 1 đổi theo. Ở bước 3, phần dịch chuyển $1/5$ dồn cả vào C.

**Câu (b).** Hàng B và hàng D không có phần dịch chuyển: $r_{\mathrm B}=\tfrac45\big(\tfrac{r_{\mathrm A}}3+\tfrac{r_{\mathrm D}}2\big)$, $r_{\mathrm D}=\tfrac45\big(\tfrac{r_{\mathrm A}}3+\tfrac{r_{\mathrm B}}2\big)$. Trừ hai phương trình cho $r_{\mathrm B}=r_{\mathrm D}=\sigma$, và hàng B cho $\sigma=\tfrac4{15}r_{\mathrm A}+\tfrac25\sigma$, tức $\sigma=\tfrac49r_{\mathrm A}$. Hàng C có cùng phần theo liên kết như hàng B cộng $\tfrac15$, nên $r_{\mathrm C}=\sigma+\tfrac15$. Điều kiện tổng $r_{\mathrm A}+3\sigma+\tfrac15=1$ cho $\tfrac73r_{\mathrm A}=\tfrac45$, nên
$$
r^*_v=\Big(\frac{12}{35},\frac{16}{105},\frac{37}{105},\frac{16}{105}\Big).
$$

**Câu (c).** $(1/8,1/8,5/8,1/8)=\tfrac12(0,0,1,0)+\tfrac12u$, và hai chủ đề dùng cùng G4, cùng $\beta$. Theo Mệnh đề 04.6(a), PageRank cần tìm là trung bình hai véc-tơ:

- A: $\tfrac12\big(\tfrac{12}{35}+\tfrac9{28}\big)=\tfrac12\cdot\tfrac{93}{140}=\tfrac{93}{280}$;
- B, D: $\tfrac12\big(\tfrac{16}{105}+\tfrac{19}{84}\big)=\tfrac12\cdot\tfrac{159}{420}=\tfrac{53}{280}$;
- C: $\tfrac12\big(\tfrac{37}{105}+\tfrac{19}{84}\big)=\tfrac12\cdot\tfrac{243}{420}=\tfrac{81}{280}$.

**Câu (d).** Theo Mệnh đề 04.7(c) với $k=2$ và $c=3$, mỗi ứng viên cần 2 phép nhân và 1 phép cộng, tổng $c(2k-1)=9$ thao tác.

**Kiểm tra lại.** Hàng A của (b): $\tfrac45\big(\tfrac12\cdot\tfrac{16}{105}+\tfrac{37}{105}\big)=\tfrac45\cdot\tfrac{45}{105}=\tfrac{12}{35}$; tổng $\tfrac{36+16+37+16}{105}=1$. Tổng ở (c) là $\tfrac{93+53+81+53}{280}=1$, và hàng C của phép lặp với $v=(1/8,1/8,5/8,1/8)$: $\tfrac45\big(\tfrac13\cdot\tfrac{93}{280}+\tfrac12\cdot\tfrac{53}{280}\big)+\tfrac15\cdot\tfrac58=\tfrac45\cdot\tfrac{345}{1680}+\tfrac18=\tfrac{23}{140}+\tfrac18=\tfrac{81}{280}$.
:::

Như vậy, chúng ta đã có PageRank theo chủ đề (Định nghĩa 04.1), thuật toán tính nó với cùng chi phí $3n+\ell$ mỗi vòng như Bài 03 (Thuật toán 04.3, Mệnh đề 04.4), các bảo đảm hội tụ và cận dừng của Bài 03 cho mọi phân phối dịch chuyển (Định lý 04.5), và cách ghép các chủ đề tính trước với chi phí $\Theta(kc)$ mỗi truy vấn (Mệnh đề 04.6, 04.7). Tuy nhiên, mọi biến thể của PageRank vẫn cộng điểm qua liên kết vào, và người kiểm soát được một phần đồ thị có thể thêm liên kết để tăng điểm một trang. Trong Mục 3, chúng ta trở lại PageRank với dịch chuyển đều và tính xem một cấu trúc liên kết đơn giản tăng điểm trang đích đến đâu.

<!-- note-topic-id: lec-04-topic-07 -->
## 3. Cơ chế liên kết rác

Trên G4, PageRank xếp A đứng đầu với $9/28\approx0{,}32$ (Ví dụ 03.13); điểm đó đến từ các liên kết mà B và C đặt tới A, với dịch chuyển đều $v=u$. Kỹ thuật tạo liên kết để PageRank đánh giá một trang cao hơn mức nội dung của nó gọi chung là *liên kết rác* (link spam) (MMDS, §5.4, tr.199). Theo MMDS (§5.4.1, tr.199–200), từ phía người tạo liên kết rác, web chia làm ba vùng:

- *trang không thể tác động* (inaccessible pages): phần lớn web;
- *trang có thể tác động* (accessible pages): trang không thuộc quyền người đó nhưng cho phép người khác đăng nội dung, như blog hay báo có mục bình luận, nơi người đó đặt được liên kết;
- *trang sở hữu* (own pages): trang người đó sở hữu và điều khiển.

Không có liên kết nào từ bên ngoài thì máy tìm kiếm không thu thập các trang sở hữu, nên chúng không có tác dụng (MMDS, §5.4.1, tr.200). Người tạo liên kết rác vì vậy cần ít nhất một liên kết từ một trang có thể tác động. Chúng ta cần biết với một liên kết như vậy và một số trang sở hữu, người đó tăng được điểm của một trang đến đâu. Để thấy hiện tượng trên số cụ thể, xem ví dụ sau.

::: example Ví dụ 04.6 (Một cụm hai trang hỗ trợ gắn vào G4)
**Dữ kiện.** Đồ thị bảy trang gồm G4 và ba trang sở hữu $\mathrm Y$, $\mathrm P_1$, $\mathrm P_2$ với các cạnh:

- $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm D\to\mathrm B,\mathrm C$, như G4;
- $\mathrm C\to\mathrm A,\mathrm Y$: C là trang có thể tác động, trên đó người tạo liên kết rác đặt thêm một liên kết tới $\mathrm Y$;
- $\mathrm Y\to\mathrm P_1,\mathrm P_2$; $\mathrm P_1\to\mathrm Y$; $\mathrm P_2\to\mathrm Y$.

$n=7$, không có nút cụt, $\beta=4/5$, $v=u$, nên phần dịch chuyển mỗi trang nhận là $(1-\beta)/7=1/35$. Thứ tự thành phần: A, B, C, D, Y, $\mathrm P_1$, $\mathrm P_2$.

**Một vòng từ $r^0=u$.**

- $\mathrm Y$ nhận từ C (bậc ra 2) và từ $\mathrm P_1$, $\mathrm P_2$ (bậc ra 1): $\tfrac45\big(\tfrac12\cdot\tfrac17+\tfrac17+\tfrac17\big)+\tfrac1{35}=\tfrac2{35}+\tfrac8{35}+\tfrac1{35}=\tfrac{11}{35}$.
- $\mathrm P_1$ nhận từ $\mathrm Y$ (bậc ra 2): $\tfrac45\cdot\tfrac12\cdot\tfrac17+\tfrac1{35}=\tfrac3{35}$; $\mathrm P_2$ cũng vậy.
- A nhận từ B (bậc ra 2) và C (bậc ra 2): $\tfrac45\big(\tfrac1{14}+\tfrac1{14}\big)+\tfrac1{35}=\tfrac17$; B, C, D mỗi trang nhận $\tfrac{13}{105}$.

**Điểm cố định.** Đồ thị không có nút cụt, nên $r^*=\tfrac45M_0r^*+\tfrac1{35}\mathbf 1$ (Mệnh đề 03.9(c)), một hệ có đúng một nghiệm. Ba trang $\mathrm Y$, $\mathrm P_1$, $\mathrm P_2$ không trỏ ra ngoài cụm, nên bốn phương trình của A, B, C, D chỉ chứa điểm của A, B, C, D. Hàng B và hàng C trùng nhau, vì cả hai trang cùng nhận từ A và D, và trừ hàng D khỏi hàng B cho $r_{\mathrm B}=r_{\mathrm D}$ như Ví dụ 04.3; gọi giá trị chung là $\sigma$. Hàng A cho $r_{\mathrm A}=\tfrac45\big(\tfrac\sigma2+\tfrac\sigma2\big)+\tfrac1{35}$, hàng B cho $\sigma=\tfrac4{15}r_{\mathrm A}+\tfrac25\sigma+\tfrac1{35}$, tức $\sigma=\tfrac49r_{\mathrm A}+\tfrac1{21}$; thế vào hàng A được $\tfrac{29}{45}r_{\mathrm A}=\tfrac1{15}$, nên $r_{\mathrm A}=\tfrac3{29}$ và $\sigma=\tfrac{19}{203}$. Trong cụm, $\mathrm P_1$ và $\mathrm P_2$ có cùng phương trình $r_{\mathrm P_k}=\tfrac25r_{\mathrm Y}+\tfrac1{35}$, và hàng $\mathrm Y$ là $r_{\mathrm Y}=\tfrac45\big(\tfrac\sigma2+2r_{\mathrm P_1}\big)+\tfrac1{35}$; thế vào được $\tfrac9{25}r_{\mathrm Y}=\tfrac25\sigma+\tfrac{13}{175}=\tfrac{81}{725}$. Vậy
$$
\begin{aligned}
r^*=\Big(&\frac3{29},\frac{19}{203},\frac{19}{203},\frac{19}{203},\\
&\frac9{29},\frac{31}{203},\frac{31}{203}\Big).
\end{aligned}
$$

**Kiểm tra lại.** Hàng $\mathrm Y$: $\tfrac45\big(\tfrac12\cdot\tfrac{19}{203}+2\cdot\tfrac{31}{203}\big)+\tfrac1{35}=\tfrac45\cdot\tfrac{143}{406}+\tfrac1{35}=\tfrac{286}{1015}+\tfrac{29}{1015}=\tfrac{315}{1015}=\tfrac9{29}$; tổng $\tfrac{21+57+63+62}{203}=1$.
:::

![Đồ thị bảy trang, β = 4/5. Bốn trang A, B, C, D ở trên giữ các cạnh của G4: A tới B, C, D; B tới A, D; C tới A; D tới B, C; thêm một cạnh màu cam, đậm, nhãn "cạnh duy nhất vào cụm", từ C tới trang đích Y. Khung nét đứt màu cam ở dưới là cụm thao túng: Y trỏ tới hai trang hỗ trợ P1, P2, và mỗi trang hỗ trợ chỉ trỏ lại Y. Nhãn bên mỗi trang ghi PageRank: A 3/29; B, C, D mỗi trang 19/203; Y 9/29; P1, P2 mỗi trang 31/203.](img/lec-04/note-g4-cum-thao-tung.svg)

Trang $\mathrm Y$ chỉ nhận một liên kết từ phần còn lại của web, nhưng có điểm lớn nhất trong bảy trang, $9/29\approx0{,}31$. Hình cho thấy nguồn của điểm đó: phần điểm $\mathrm Y$ gửi tới $\mathrm P_1$, $\mathrm P_2$ quay lại $\mathrm Y$ sau hai bước theo liên kết, và hai trang hỗ trợ còn thu phần dịch chuyển của chính chúng rồi chuyển về $\mathrm Y$. Trong khi đó A giảm từ $9/28$ xuống $3/29\approx0{,}10$, vì C chia điểm của mình cho A và $\mathrm Y$ và tổng điểm toàn đồ thị vẫn bằng 1. Định nghĩa sau mô tả cấu trúc này cho mọi số trang hỗ trợ.

::: definition Định nghĩa 04.9 (Liên kết rác và cụm thao túng liên kết)
**Liên kết rác.** Liên kết rác là liên kết được tạo để tăng PageRank của một trang hơn mức nội dung của trang đó.

**Cụm thao túng liên kết.** Một *cụm thao túng liên kết* (còn gọi là trại thư rác, spam farm) trong đồ thị web $G$ với $n$ trang gồm một *trang đích* (target page) và $m\ge1$ *trang hỗ trợ* (supporting pages), $m+1\le n$, thỏa ba điều kiện:

- trang đích có cạnh tới mọi trang hỗ trợ và không có cạnh nào khác, nên bậc ra của nó là $m$;
- mỗi trang hỗ trợ có đúng một cạnh ra, tới trang đích;
- mỗi trang hỗ trợ chỉ nhận cạnh từ trang đích; do đó mọi cạnh từ một trang ngoài cụm vào cụm đều kết thúc ở trang đích.

**Các đại lượng.** Cho $r^*$ là PageRank của $G$ với dịch chuyển đều (Định nghĩa 03.8), $0<\beta<1$. Đặt $b=(1-\beta)/n$ và gọi $y$ là điểm $r^*$ của trang đích. *Đóng góp từ ngoài* vào trang đích là
$$
x=\sum_{j\in J}\frac{\beta\,r^*_j}{d_j},
$$
với $J$ là tập các trang ngoài cụm có cạnh tới trang đích: tổng phần điểm theo liên kết mà các trang ngoài cụm chuyển tới trang đích, đã nhân $\beta$ và chia bậc ra tại nguồn.
:::

![Hình 5.16 của MMDS vẽ lại. Ba vùng từ trái sang phải: trang không thể tác động, trang có thể tác động, trang sở hữu. Mũi tên từ vùng giữa đi vào trang Đích, ghi đóng góp từ ngoài vào đích; vùng không thể tác động nằm ngoài quyền tác động. Trong vùng sở hữu, Đích trỏ tới m trang hỗ trợ H1, H2, …, Hm và mỗi trang hỗ trợ trỏ lại Đích.](img/lec-04/hinh-5-16-cum-thao-tung.svg)

Hình đặt cụm vào ba vùng của web: chỉ các mũi tên từ vùng giữa đi vào cụm, và chúng chỉ tới trang đích, đúng hệ quả của điều kiện thứ ba. Trong vùng sở hữu, $m$ cạnh đi từ trang đích và $m$ cạnh quay lại, tổng $2m$ cạnh nội bộ. Ví dụ 04.6 là một cụm với $m=2$, trang đích $\mathrm Y$, hai trang hỗ trợ $\mathrm P_1$, $\mathrm P_2$, và một trang có thể tác động là C. Bài 03 dùng trại thư rác gồm các trang chỉ trỏ vào trang đích để cho thấy đếm liên kết vào không đủ; Định nghĩa 04.9 thêm các cạnh từ trang đích tới mọi trang hỗ trợ. Với các cạnh đó, trang đích cùng các trang hỗ trợ tạo thành một bẫy liên kết (Định nghĩa 03.7): mọi liên kết ra của chúng ở lại trong cụm, nên điểm chỉ rời cụm qua bước dịch chuyển, và người tạo cụm không cần nhiều liên kết từ ngoài.

Hai nhầm lẫn thường gặp về $x$. Thứ nhất, $x$ đã gồm hệ số $\beta$ và phép chia cho bậc ra tại nguồn; nhân thêm $\beta$ là áp hệ số đó hai lần. Thứ hai, $x$ là đại lượng tại điểm cố định của cả đồ thị, nên không chọn tùy ý được: $x\le\beta\sum_{j\in J}r^*_j<\beta$, vì tổng điểm bằng 1. Trên đồ thị bảy trang, $x=\tfrac45\cdot\tfrac12\cdot\tfrac{19}{203}=\tfrac{38}{1015}$.

::: proposition Mệnh đề 04.10 (Điểm của trang hỗ trợ và trang đích)
**Giả thiết.** $G$ không có nút cụt; $0<\beta<1$; $G$ chứa một cụm thao túng liên kết với $m$ trang hỗ trợ; $r^*$, $b$, $x$, $y$ như Định nghĩa 04.9.

**Kết luận.**

- (a) Mọi trang hỗ trợ có cùng điểm $p$, và
$$
p=\frac{\beta y}m+b .
$$
- (b) $y=x+\beta mp+b$.
- (c) $y=\dfrac{x+\beta mb+b}{1-\beta^2}$.

**Điều kiện áp dụng.** Số học chính xác; $r^*$ là điểm cố định chính xác.

**Phạm vi.** (c) là đẳng thức giữa các đại lượng tại điểm cố định; $x$ phụ thuộc toàn bộ đồ thị và chỉ được tính sau khi biết $r^*$ của các trang ngoài cụm.
:::

::: proof
**Bước 1 (phương trình điểm cố định).** $G$ không có nút cụt nên $\delta=0$, và theo Mệnh đề 03.9(c), với mọi trang $i$,
$$
r^*_i=\beta\sum_{j:\,j\to i}\frac{r^*_j}{d_j}+b .
$$

**Bước 2 (trang hỗ trợ).** Một trang hỗ trợ chỉ nhận cạnh từ trang đích (điều kiện thứ ba), và trang đích có bậc ra $m$ (điều kiện thứ nhất). Tổng ở Bước 1 chỉ có một số hạng, $y/m$, nên điểm của mọi trang hỗ trợ bằng $\beta y/m+b$. Đó là (a).

**Bước 3 (trang đích).** Các nguồn trỏ tới trang đích gồm các trang ngoài cụm và các trang hỗ trợ; trang đích không trỏ tới chính nó (điều kiện thứ nhất). Phần từ ngoài cụm là $x$ theo định nghĩa. Mỗi trang hỗ trợ có bậc ra 1 (điều kiện thứ hai) và điểm $p$, nên đóng góp $\beta p$; $m$ trang đóng góp $\beta mp$. Cộng phần dịch chuyển $b$ được (b).

**Bước 4 (giải).** Thế (a) vào (b):
$$
\begin{aligned}
y&=x+\beta m\Big(\frac{\beta y}m+b\Big)+b\\
&=x+\beta^2y+\beta mb+b .
\end{aligned}
$$
Chuyển $\beta^2y$ sang vế trái và chia cho $1-\beta^2>0$, vì $0<\beta<1$, được (c). $\square$
:::

Số hạng $\beta^2y$ là phần điểm đi từ trang đích sang các trang hỗ trợ rồi quay lại sau hai bước theo liên kết, mỗi bước nhân $\beta$: phần điểm được bẫy giữ lại. Số trang hỗ trợ triệt tiêu trong số hạng này, vì điểm được chia cho $m$ rồi cộng lại từ $m$ trang. Số $m$ còn lại trong $\beta mb$: mỗi trang hỗ trợ thu phần dịch chuyển $b$ của chính nó và chuyển $\beta b$ về trang đích.

![Ba nguồn điểm tại trang đích. Trên trái, mũi tên x từ bên ngoài; trên phải, mũi tên βmp từ m trang hỗ trợ, mỗi trang điểm p; dưới trái, mũi tên nét đứt b của bước dịch chuyển; cả ba đi vào trang đích có điểm y.](img/lec-04/luong-hang-trong-cum.svg)

Hình là Bước 3 của chứng minh: ba mũi tên vào trang đích ứng với ba số hạng $x$, $\beta mp$ và $b$ của (b).

::: example Ví dụ 04.7 (Kiểm Mệnh đề 04.10 trên đồ thị bảy trang)
**Dữ kiện.** Đồ thị của Ví dụ 04.6: $n=7$, $m=2$, $\beta=4/5$, không có nút cụt; cụm gồm trang đích $\mathrm Y$ và hai trang hỗ trợ $\mathrm P_1$, $\mathrm P_2$; trang ngoài cụm duy nhất trỏ tới $\mathrm Y$ là C, với bậc ra 2 và $r^*_{\mathrm C}=19/203$.

**Kiểm giả thiết.** $\mathrm Y$ chỉ trỏ tới $\mathrm P_1$, $\mathrm P_2$; mỗi trang hỗ trợ chỉ trỏ tới $\mathrm Y$ và chỉ nhận cạnh từ $\mathrm Y$; cạnh duy nhất từ ngoài vào cụm là $\mathrm C\to\mathrm Y$.

**Các đại lượng.** $b=\tfrac15\cdot\tfrac17=\tfrac1{35}$ và $x=\tfrac45\cdot\tfrac12\cdot\tfrac{19}{203}=\tfrac{38}{1015}$.

**Áp dụng (c).** $x+\beta mb+b=\tfrac{38}{1015}+\tfrac85\cdot\tfrac1{35}+\tfrac1{35}=\tfrac{190+232+145}{5075}=\tfrac{81}{725}$, và $1-\beta^2=\tfrac9{25}$, nên
$$
y=\frac{81}{725}\cdot\frac{25}9=\frac9{29}.
$$

**Áp dụng (a).** $p=\tfrac45\cdot\tfrac12\cdot\tfrac9{29}+\tfrac1{35}=\tfrac{18}{145}+\tfrac1{35}=\tfrac{126+29}{1015}=\tfrac{31}{203}$.

**Kiểm tra lại.** Hai giá trị trùng với $r^*_{\mathrm Y}$ và $r^*_{\mathrm P_1}$ của Ví dụ 04.6; (b) cho $\tfrac{38}{1015}+\tfrac85\cdot\tfrac{31}{203}+\tfrac1{35}=\tfrac{38+248+29}{1015}=\tfrac9{29}$.
:::

Công thức (c) chính xác, nhưng còn chứa $b$ và $m$ trong cùng một số hạng. Viết $b=(1-\beta)/n$ tách được phần đến từ $x$ và phần đến từ số trang hỗ trợ.

::: corollary Hệ quả 04.11 (Hệ số khuếch đại của cụm; MMDS §5.4.2, Ví dụ 5.11)
**Giả thiết.** Như Mệnh đề 04.10.

**Kết luận.**
$$
\begin{aligned}
y&=\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\cdot\frac mn\\
&\quad+\frac1{n(1+\beta)} .
\end{aligned}
$$
Bỏ số hạng cuối được xấp xỉ của MMDS,
$$
y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\cdot\frac mn ,
$$
với sai số đúng bằng $1/\big(n(1+\beta)\big)$. Hệ số $1/(1-\beta^2)$ gọi là *hệ số khuếch đại* của cụm.

**Điều kiện áp dụng.** Như Mệnh đề 04.10.

**Phạm vi.** Số hạng bị bỏ là phần dịch chuyển trực tiếp vào trang đích sau khi khuếch đại; nó nhỏ khi $n$ lớn, nhưng không nhỏ trên đồ thị vài trang.
:::

::: proof
Thay $b=(1-\beta)/n$ vào Mệnh đề 04.10(c) và dùng $1-\beta^2=(1-\beta)(1+\beta)$:
$$
\begin{aligned}
\frac{\beta mb}{1-\beta^2}&=\frac{\beta m(1-\beta)}{n(1-\beta)(1+\beta)}\\
&=\frac{\beta}{1+\beta}\cdot\frac mn,\\
\frac{b}{1-\beta^2}&=\frac{1-\beta}{n(1-\beta)(1+\beta)}\\
&=\frac1{n(1+\beta)} .
\end{aligned}
$$
Cộng với $x/(1-\beta^2)$ được kết luận. $\square$
:::

MMDS lấy $\beta=0{,}85=17/20$ (Ví dụ 5.11, tr.201). Khi đó
$$
\begin{gathered}
\frac1{1-\beta^2}=\frac{400}{111}\approx3{,}6036,\\
\frac{\beta}{1+\beta}=\frac{17}{37}\approx0{,}45946 .
\end{gathered}
$$
Cụm nhân đóng góp từ ngoài khoảng $3{,}6$ lần, và thêm một lượng khoảng $0{,}46$ lần tỷ lệ $m/n$ của web thuộc cụm. Trên đồ thị bảy trang của Ví dụ 04.7, với $\beta=4/5$, hệ số khuếch đại là $25/9$, ba số hạng của Hệ quả 04.11 là $\tfrac{190}{1827}$, $\tfrac8{63}$ và $\tfrac5{63}$; xấp xỉ cho $\tfrac{422}{1827}\approx0{,}231$ thay cho $\tfrac9{29}\approx0{,}310$, vì với $n=7$ số hạng bị bỏ $\tfrac5{63}\approx0{,}079$ không nhỏ.

Công thức của Mệnh đề 04.10 phụ thuộc đúng kiến trúc của Định nghĩa 04.9; mỗi điều kiện bị bỏ đổi một phương trình.

- Bỏ "mỗi trang hỗ trợ chỉ nhận cạnh từ trang đích": nếu mỗi trang hỗ trợ nhận thêm đóng góp $x'$ từ ngoài cụm, đã nhân $\beta$ và chia bậc ra, thì $p=\beta y/m+x'+b$, phương trình (b) giữ dạng, và $y=\big(x+\beta m(x'+b)+b\big)/(1-\beta^2)$: phần $x'$ cũng được đưa về trang đích.
- Bỏ "trang đích không có cạnh nào khác": nếu trang đích có thêm $e$ cạnh ra ngoài cụm, bậc ra của nó là $m+e$, nên $p=\beta y/(m+e)+b$ và $y=(x+\beta mb+b)\big/\big(1-\beta^2m/(m+e)\big)$; với $\beta=17/20$, $m=e=1$, hệ số của $x$ giảm từ $3{,}60$ xuống khoảng $1{,}57$.
- Bỏ "$G$ không có nút cụt": mỗi trang, kể cả trang đích và trang hỗ trợ, nhận thêm phần bù $\beta\delta/n$, nên $b$ trong (a) và (b) được thay bằng $b+\beta\delta/n$.

Bước 1 dùng giả thiết không có nút cụt; Bước 2 dùng điều kiện thứ nhất và thứ ba; Bước 3 dùng điều kiện thứ nhất, thứ hai và định nghĩa của $x$.

::: remark Nhận xét 04.12 (Trong thực hành: hai hướng chống liên kết rác)
- MMDS nêu hai hướng (§5.4.3, tr.202). Hướng thứ nhất tìm các cấu trúc như cụm của Định nghĩa 04.9, nơi một trang trỏ tới rất nhiều trang và các trang đó trỏ ngược lại, rồi loại chúng khỏi chỉ mục. Người tạo liên kết rác khi đó chuyển sang cấu trúc khác có cùng tác dụng; các điều kiện bị bỏ ở trên là vài biến thể như vậy, và MMDS ghi rằng số biến thể gần như không có giới hạn. Hướng thứ hai sửa định nghĩa PageRank để điểm của trang rác tự giảm mà không cần định vị cụm.
- Theo Hệ quả 04.11, phần do trang hỗ trợ đem lại là $\tfrac{\beta}{1+\beta}\cdot\tfrac mn<\tfrac m{2n}$, tăng tuyến tính theo tỷ lệ $m/n$ của web thuộc cụm, và $y\le1$ vì tổng điểm bằng 1. Với $n=10^9$, điểm trung bình một trang là $10^{-9}$, nên một cụm $10^6$ trang hỗ trợ đã đem lại cho trang đích một lượng khoảng $0{,}46\cdot10^{-3}$, gấp khoảng $4{,}6\cdot10^5$ lần điểm trung bình, khi $\beta=0{,}85$.
- Định nghĩa 04.9 chỉ dùng cấu trúc liên kết, nên mọi cấu trúc cùng dạng đều thỏa nó, chẳng hạn một trang mục lục chỉ trỏ tới các trang con, mỗi trang con chỉ trỏ về mục lục và chỉ được mục lục trỏ tới.
:::

::: exercise Bài tập 04.4 (Hệ số khuếch đại khi $\beta=0{,}9$ và một phương trình sai)
Xét cụm thao túng của Định nghĩa 04.9 trên đồ thị không có nút cụt.

- (a) Với $\beta=0{,}9$, tính hệ số của $x$ và của $m/n$ trong xấp xỉ của Hệ quả 04.11, rồi so với $\beta=0{,}85$.
- (b) Một lời giải viết phương trình trang đích là $y=\beta x+\beta mp$. Chỉ ra hai lỗi và nêu số hạng bị lược khỏi nghiệm $y$ trong xấp xỉ của MMDS.
:::

::: hint
Viết $\beta=9/10$ dưới dạng phân số. Với câu (b), xem lại $x$ đã gồm những hệ số nào và trang đích nhận những phần điểm nào ở Bước 3 của chứng minh Mệnh đề 04.10.
:::

::: solution
**Câu (a).** Với $\beta=9/10$, $1-\beta^2=19/100$, nên hệ số của $x$ là $100/19\approx5{,}26$; hệ số của $m/n$ là $\beta/(1+\beta)=9/19\approx0{,}47$. Với $\beta=17/20$, hai hệ số là $400/111\approx3{,}60$ và $17/37\approx0{,}46$. Khi $\beta$ tăng, mỗi bước theo liên kết mất ít điểm hơn cho bước dịch chuyển, nên vòng trang đích → trang hỗ trợ → trang đích giữ lại phần $\beta^2$ lớn hơn, và hệ số khuếch đại tăng từ $3{,}6$ lên khoảng $5{,}3$.

**Câu (b).** Lỗi thứ nhất: $x$ đã nhân $\beta$ và chia bậc ra tại nguồn, nên viết $\beta x$ là áp hệ số $\beta$ hai lần. Lỗi thứ hai: thiếu phần dịch chuyển $b$ vào trang đích. Phương trình đúng là $y=x+\beta mp+b$. Sau khi giải, số hạng bị lược trong xấp xỉ của MMDS là $b/(1-\beta^2)=1/\big(n(1+\beta)\big)$, không phải $b$.

**Kiểm tra lại.** Thế $\beta=0{,}9$: $1/(1-0{,}81)=1/0{,}19\approx5{,}26$. Hệ số của $m/n$ và hệ số $1/(1+\beta)$ trong số hạng bị lược $1/\big(n(1+\beta)\big)$ có tổng $\tfrac{\beta+1}{1+\beta}=1$; với $\beta=0{,}9$ là $\tfrac9{19}+\tfrac{10}{19}=1$.
:::

Mệnh đề 04.10 cho điểm trang đích của một cụm thao túng (Định nghĩa 04.9) ở dạng chính xác, và cụm nhân đóng góp từ ngoài với hệ số $1/(1-\beta^2)$, khoảng $3{,}6$ khi $\beta=0{,}85$ (Hệ quả 04.11); trên đồ thị bảy trang, một liên kết từ C đủ đưa trang đích lên đầu. Phép lặp PageRank không có thông tin nào để phân biệt cụm này với một cấu trúc hợp lệ cùng dạng, và số biến thể của cụm gần như không có giới hạn (Nhận xét 04.12). Trong Mục 4, chúng ta dùng một tập trang đã được đánh giá tin cậy, thông tin mà người tạo liên kết rác không kiểm soát được, làm phân phối dịch chuyển của Mục 2.

<!-- note-topic-id: lec-04-topic-08 -->
## 4. TrustRank và khối lượng rác

Một máy tìm kiếm chạy PageRank trên đồ thị bảy trang chỉ thấy bảy con số, không thấy cấu trúc nào là cụm thao túng và trang nào là trang đích. Nó cần một cách tính điểm dựa trên thông tin bên ngoài đồ thị, và một chỉ số so điểm mới đó với PageRank của từng trang. Phân phối dịch chuyển tập trung trên một tập trang chọn trước, của Định nghĩa 04.1, là công cụ cho việc thứ nhất.

### 4.1 TrustRank

Về mặt ý tưởng, một trang rác dễ đặt liên kết tới một trang tin cậy, nhưng một trang tin cậy hiếm khi đặt liên kết tới một trang rác (MMDS, §5.4.4, tr.202). Nếu người lướt chỉ dịch chuyển tới các trang tin cậy, điểm lan từ các trang đó qua nhiều bước theo các đường đi xuất phát từ chúng, và ít khi tới được trang rác. Ngoài phần bù nút cụt chia đều $\beta\delta_\rho/n$, một trang rác chỉ nhận TrustRank qua các đường đi xuất phát từ $T$ và đi qua một trang có thể tác động.

![Tập tin cậy và lan truyền điểm. Một khung ghi tập tin cậy T, đánh giá bên ngoài; các liên kết ra từ các trang trong T truyền điểm tới các trang ngoài T.](img/lec-04/tap-tin-cay.svg)

Hình tách hai bước: tập $T$ được chọn và đánh giá bên ngoài đồ thị, rồi điểm lan từ $T$ theo các liên kết ra, qua nhiều bước, tới các trang ngoài $T$; hình vẽ bước đầu tiên.

::: definition Định nghĩa 04.13 (Tập tin cậy và TrustRank; MMDS §5.4.4)
**Tập tin cậy.** Một *tập hạt giống* (seed set) là một tập trang được đưa cho người đánh giá; phần của nó được xác nhận không phải rác là *tập tin cậy* (trusted set) $T\subseteq V$, $T\ne\varnothing$ (trang chiếu MMDS, tr.38–39). Phân phối đều trên $T$ là $(v_T)_i=1/\lvert T\rvert$ khi $i\in T$ và bằng 0 khi không.

**TrustRank.** *TrustRank* của $G$ với tập tin cậy $T$ và hằng số $0<\beta<1$ là PageRank theo chủ đề (Định nghĩa 04.1) với phân phối dịch chuyển $v_T$:
$$
\begin{gathered}
\rho=r^*_{v_T},\\
\rho=\beta\bar M\rho+(1-\beta)v_T .
\end{gathered}
$$
Phép lặp TrustRank là $\rho^{t+1}=\beta M_0\rho^t+\beta\delta_\rho^tu+(1-\beta)v_T$ với $\delta_\rho^t=\sum_{j\in\mathcal D}\rho^t_j$, khởi tạo $\rho^0=v_T$.

**Giả thiết.** Mô hình dùng *giả thiết cách ly gần đúng* (approximate isolation): các trang của $T$ hiếm khi trỏ tới trang rác (trang chiếu MMDS, tr.38).
:::

TrustRank là PageRank theo chủ đề trong đó "chủ đề" là tập các trang được tin là không phải rác (MMDS, §5.4.4, tr.202). Vì vậy không cần thuật toán hay chứng minh mới: Thuật toán 04.3 với $v=v_T$ tính $\rho$; Mệnh đề 04.4 cho mỗi $\rho^t$ là phân phối; Định lý 04.5 cho $\rho$ tồn tại, duy nhất, và cận dừng $\lVert\rho^{t+1}-\rho\rVert_1\le\beta\Delta_t/(1-\beta)$. Điều mới nằm ở ý nghĩa của $T$ và ở giả thiết cách ly gần đúng, một giả thiết về cách người ta đặt liên kết mà đồ thị không ghi lại.

Hai cách chọn $T$ đã được thử (MMDS, §5.4.4, tr.202–203):

- người đánh giá xem xét một tập trang và quyết định trang nào tin cậy, chẳng hạn các trang có PageRank cao nhất, vì liên kết rác có thể đưa một trang từ cuối bảng lên giữa bảng nhưng gần như không đưa được lên gần đầu bảng;
- chọn một miền mà thành viên được kiểm soát, như .edu, .mil, .gov; để không chỉ gồm trang của Mỹ, thêm các miền tương tự của nước khác như ac.il, edu.sg.

Lý lẽ của cách thứ nhất dựa vào quy mô. Theo Hệ quả 04.11, phần điểm do $m$ trang hỗ trợ đem lại cỡ $\tfrac{\beta}{1+\beta}\cdot\tfrac mn$. Trên đồ thị bảy trang, $m/n=2/7$, nên $\mathrm Y$ lên đầu. Chọn tập hạt giống theo PageRank cao sẽ đưa $\mathrm Y$ vào tập hạt giống, và người đánh giá phải loại $\mathrm Y$ khỏi $T$. Với $n=10^9$, một cụm $10^6$ trang hỗ trợ chỉ đem lại khoảng $0{,}46\cdot10^{-3}$ khi $\beta=0{,}85$ (Nhận xét 04.12).

Một trang có mục cho phép người khác đăng bình luận không được coi là tin cậy, kể cả khi nội dung của chính nó đáng tin, như trang một tờ báo uy tín cho phép bạn đọc bình luận (MMDS, §5.4.4, tr.202). Lý do là trang như vậy thuộc vùng có thể tác động của Mục 3, nơi người tạo liên kết rác đặt được liên kết.

::: example Ví dụ 04.8 (TrustRank trên G4 với $T=\{\mathrm B,\mathrm D\}$)
**Dữ kiện.** G4, $\beta=4/5$. Giả sử B và D đã được đánh giá là tin cậy: $T=\{\mathrm B,\mathrm D\}$, nên $v_T=(0,1/2,0,1/2)$.

**Tính.** $v_T$ trùng phân phối dịch chuyển $v$ của Ví dụ 04.3, và theo Định lý 04.5(b) điểm cố định chỉ phụ thuộc $G$, $\beta$ và phân phối dịch chuyển. Do đó
$$
\rho=\Big(\frac9{35},\frac{59}{210},\frac{19}{105},\frac{59}{210}\Big).
$$

**Kiểm tra lại.** Hàng C: $\tfrac45\big(\tfrac13\cdot\tfrac9{35}+\tfrac12\cdot\tfrac{59}{210}\big)=\tfrac45\cdot\tfrac{36+59}{420}=\tfrac{19}{105}$, đúng thành phần C.
:::

![Đồ thị G4 của MMDS Hình 5.15: A trỏ tới B, C, D; B trỏ tới A, D; C trỏ tới A; D trỏ tới B, C. B và D có viền đôi và nhãn T, thuộc tập tin cậy.](img/lec-04/hinh-5-15-tin-cay.svg)

Cùng một véc-tơ nhận hai cách đọc theo ý nghĩa của tập được chọn: với $S=\{\mathrm B,\mathrm D\}$ là tập chủ đề, nó là điểm theo chủ đề; với $T=\{\mathrm B,\mathrm D\}$ là tập tin cậy, nó là TrustRank. A và C không thuộc $T$ nhưng nhận điểm qua cạnh từ B và D.

<!-- note-topic-id: lec-04-topic-09 -->
### 4.2 Khối lượng rác

Trang chiếu MMDS (tr.39) đánh dấu rác bằng một ngưỡng trên TrustRank: mọi trang có TrustRank dưới ngưỡng bị coi là rác. Trên G4 với $T=\{\mathrm B,\mathrm D\}$, ngưỡng đó đánh dấu C trước tiên vì $\rho_{\mathrm C}=19/105$ nhỏ nhất, dù PageRank của C bằng của B và D, $19/84$; $\rho_{\mathrm C}$ nhỏ vì C không thuộc $T$ và không được B trỏ tới. Vì vậy cần so TrustRank của một trang với PageRank của chính nó. Ví dụ sau đặt hai véc-tơ cạnh nhau.

::: example Ví dụ 04.9 (Hiệu PageRank và TrustRank trên G4)
**Dữ kiện.** G4, $\beta=4/5$. PageRank với dịch chuyển đều $r=(9/28,19/84,19/84,19/84)$ (Ví dụ 03.13); TrustRank với $T=\{\mathrm B,\mathrm D\}$, $\rho=(9/35,59/210,19/105,59/210)$ (Ví dụ 04.8). Hai véc-tơ dùng cùng đồ thị, cùng $\beta$ và cùng quy tắc bù.

**Tính.**

| Trang | $r_i$ | $\rho_i$ | $r_i-\rho_i$ |
|---|---:|---:|---:|
| A | $9/28$ | $9/35$ | $9/140$ |
| B | $19/84$ | $59/210$ | $-23/420$ |
| C | $19/84$ | $19/105$ | $19/420$ |
| D | $19/84$ | $59/210$ | $-23/420$ |

**Kiểm tra lại.** Hai véc-tơ có tổng 1 nên cột hiệu có tổng 0: $\tfrac{27-23+19-23}{420}=0$.
:::

A và C giảm điểm khi chuyển sang TrustRank, B và D tăng. Mức giảm tuyệt đối của A, $9/140$, lớn hơn của C, $19/420$, nhưng A cũng có PageRank lớn hơn; so hai mức giảm cần chia cho điểm nền của từng trang. Đó là định nghĩa sau.

::: definition Định nghĩa 04.14 (Khối lượng rác; MMDS §5.4.5)
Cho PageRank $r$ với dịch chuyển đều và TrustRank $\rho$ với tập tin cậy $T$, tính trên cùng đồ thị, cùng $\beta$ và cùng quy tắc bù nút cụt. *Khối lượng rác* (spam mass) của trang $i$ với $r_i>0$ là
$$
s_i=\frac{r_i-\rho_i}{r_i}=1-\frac{\rho_i}{r_i} .
$$
:::

$s_i$ là phần của PageRank $r_i$ bị mất khi bước dịch chuyển chỉ đi vào tập tin cậy: $\rho_i=(1-s_i)r_i$. Vì $\rho_i\ge0$, $s_i\le1$; $s_i=1$ đúng khi $\rho_i=0$, tức trang không nhận chút điểm nào lan từ $T$. Khi $\rho_i>r_i$, $s_i<0$: trang được tập tin cậy nâng điểm. MMDS đọc chỉ số như sau (§5.4.5, tr.203): khối lượng rác âm hoặc dương nhỏ cho thấy trang có lẽ không phải rác, còn khối lượng rác gần 1 cho thấy trang có lẽ là rác; máy tìm kiếm có thể loại các trang có khối lượng rác cao khỏi chỉ mục mà không cần nhận ra cấu trúc của từng cụm.

Khối lượng rác là một độ đo dẫn xuất từ hai véc-tơ đã có, nên không có thuật toán lặp riêng. Nhầm lẫn thường gặp là đọc $s_i$ như xác suất trang $i$ là rác. $s_i$ có thể âm, và nó so $\rho_i$ với $r_i$ trên cùng đồ thị. Một $s_i$ lớn có thể do liên kết rác hoặc do $T$ thiếu độ phủ, và chỉ số không phân biệt được hai nguyên nhân.

::: example Ví dụ 04.10 (Khối lượng rác trên G4)
**Dữ kiện.** Bảng của Ví dụ 04.9; $r_i>0$ với mọi $i$.

**Tính.**

| Trang | Phép tính | $s_i$ |
|---|---|---:|
| A | $\dfrac{9/140}{9/28}$ | $1/5$ |
| B | $\dfrac{-23/420}{19/84}$ | $-23/95$ |
| C | $\dfrac{19/420}{19/84}$ | $1/5$ |
| D | $\dfrac{-23/420}{19/84}$ | $-23/95$ |

**Diễn giải.** B và D, hai trang được đánh giá tin cậy, có khối lượng rác âm, $-23/95\approx-0{,}24$. A và C có $1/5$, gần 0 hơn gần 1, nên theo cách đọc của MMDS chúng có lẽ không phải rác.

**Kiểm tra lại.** $\sum_ir_is_i=\sum_i(r_i-\rho_i)=0$: $\tfrac9{28}\cdot\tfrac15+\tfrac{19}{84}\cdot\tfrac15-2\cdot\tfrac{19}{84}\cdot\tfrac{23}{95}=\tfrac{27+19-46}{420}=0$.
:::

A và C có cùng khối lượng rác $1/5$ dù mức giảm tuyệt đối khác nhau: cả hai có $\rho_i=\tfrac45r_i$, tức giảm $20\%$ so với điểm nền của chính trang. Dòng kiểm tra dùng một tính chất đúng cho mọi đồ thị: vì $r$ và $\rho$ đều có tổng 1, $\sum_ir_is_i=\sum_i(r_i-\rho_i)=0$. Do đó nếu có trang với $s_i>0$ thì phải có trang với $s_i<0$; chỉ số không thể dương ở mọi trang.

::: remark Nhận xét 04.15 (Điều kiện cùng mô hình nền)
Định nghĩa 04.14 đòi $r$ và $\rho$ cùng $\beta$. Nếu dùng lặp thô $r=(1/3,2/9,2/9,2/9)$ (Ví dụ 03.6, $\beta=1$) làm nền cho TrustRank $\rho$ của Ví dụ 04.8, tính với $\beta=4/5$, thì $s_{\mathrm A}=8/35\approx0{,}229$, $s_{\mathrm B}=s_{\mathrm D}=-37/140\approx-0{,}264$ và $s_{\mathrm C}=13/70\approx0{,}186$, khác bảng của Ví dụ 04.10 dù $\rho$ như nhau: A và C không còn bằng nhau, và A xếp trên C. Với nền khác $\beta$, chỉ số đo cả khác biệt giữa hai mô hình nền, không chỉ ảnh hưởng của tập tin cậy.
:::

::: remark Nhận xét 04.16 (Trong thực hành: chi phí và tập tin cậy)
- Theo Thuật toán 04.3, PageRank nền chạy $K_r$ vòng và TrustRank chạy $K_\rho$ vòng, mỗi vòng $3n+\ell$ thao tác; khi đã có hai véc-tơ, tính mọi $s_i$ cần $n$ phép chia và $n$ phép trừ. Tổng là $\Theta\big((K_r+K_\rho)(n+\ell)\big)$ thao tác, và lưu thêm một véc-tơ $n$ số. Chi phí đánh giá các trang của $T$ bằng người hay bằng quy trình kiểm soát miền nằm ngoài mô hình đếm này.
- Tập $T$ nhỏ giảm công đánh giá nhưng có thể không phủ một vùng nội dung hợp lệ. Trang thuộc vùng đó nhận ít điểm lan từ $T$, nên có $\rho_i$ nhỏ và khối lượng rác lớn dù không phải rác. MMDS nêu vấn đề độ phủ khi chọn miền .edu: tập đó gần như chỉ gồm trang của Mỹ (§5.4.4, tr.202–203).
- Giả thiết cách ly gần đúng bị vi phạm khi $T$ chứa trang cho phép người khác đặt liên kết.
- MMDS nhận định nhiều khả năng các máy tìm kiếm ngày nay dùng cách chọn $T$ theo miền như một bước thường lệ, nên điều ta gọi là PageRank thật ra là một dạng TrustRank (§5.4.4, tr.203).
:::

::: exercise Bài tập 04.5 (Khối lượng rác với tập tin cậy $\{\mathrm C\}$)
Trên G4 với $\beta=4/5$, giả sử chỉ C được đánh giá là tin cậy: $T=\{\mathrm C\}$. Theo Bài tập 04.3(b), TrustRank là $\rho=(12/35,16/105,37/105,16/105)$.

- (a) Với PageRank nền $r=(9/28,19/84,19/84,19/84)$ cùng $\beta$ (Ví dụ 03.13), tính khối lượng rác của bốn trang.
- (b) Với lặp thô $r=(1/3,2/9,2/9,2/9)$ (Ví dụ 03.6) làm nền, tính $s_{\mathrm B}$ và nêu đại lượng làm kết quả khác (a).
- (c) Đánh giá kết luận "B và D có khối lượng rác dương lớn nhất, nên là trang rác".
:::

::: hint
Dùng $s_i=1-\rho_i/r_i$. Với (c), xem điểm lan từ C tới B và D qua những đường đi nào.
:::

::: solution
**Câu (a).**

- A: $s_{\mathrm A}=1-\tfrac{12}{35}\cdot\tfrac{28}9=1-\tfrac{16}{15}=-\tfrac1{15}$.
- B, D: $s_{\mathrm B}=s_{\mathrm D}=1-\tfrac{16}{105}\cdot\tfrac{84}{19}=1-\tfrac{64}{95}=\tfrac{31}{95}\approx0{,}326$.
- C: $s_{\mathrm C}=1-\tfrac{37}{105}\cdot\tfrac{84}{19}=1-\tfrac{148}{95}=-\tfrac{53}{95}\approx-0{,}558$.

C thuộc $T$ nên có khối lượng rác âm; A nhận toàn bộ phần theo liên kết của C nên cũng âm.

**Câu (b).** $s_{\mathrm B}=1-\dfrac{16/105}{2/9}=1-\dfrac{24}{35}=\dfrac{11}{35}\approx0{,}314$. Kết quả khác (a) vì PageRank nền khác: lặp thô là trường hợp $\beta=1$, còn TrustRank dùng $\beta=4/5$. Giả thiết "cùng $\beta$" của Định nghĩa 04.14 bị bỏ, nên chỉ số đo cả khác biệt giữa hai mô hình nền (Nhận xét 04.15).

**Câu (c).** Kết luận không có căn cứ. C chỉ trỏ tới A, nên TrustRank tới B và D sau ít nhất hai bước, qua A; B và D có $\rho$ nhỏ so với $r$ vì $T=\{\mathrm C\}$ phủ kém; G4 không chứa liên kết rác nào. Khối lượng rác không phân biệt được hai nguyên nhân này. Ngoài ra, $31/95\approx0{,}33$ không gần 1, nên theo cách đọc của MMDS chưa đủ để kết luận B, D là rác.

**Kiểm tra lại.** $\sum_ir_is_i=\tfrac9{28}\cdot\big(-\tfrac1{15}\big)+2\cdot\tfrac{19}{84}\cdot\tfrac{31}{95}+\tfrac{19}{84}\cdot\big(-\tfrac{53}{95}\big)=\tfrac{-9+62-53}{420}=0$, đúng vì $r$ và $\rho$ cùng có tổng 1.
:::

TrustRank là PageRank theo chủ đề với phân phối dịch chuyển đều trên tập tin cậy (Định nghĩa 04.13), nên thừa hưởng thuật toán và mọi bảo đảm của Mục 2. Khối lượng rác so TrustRank với PageRank cùng mô hình (Định nghĩa 04.14) và đánh dấu trang có TrustRank nhỏ so với PageRank của chính nó, với chi phí hai phép lặp và một lượt $\Theta(n)$. Cả hai công cụ vẫn gán mỗi trang một điểm. Trong Mục 5, chúng ta gán mỗi trang hai điểm để tách trang dẫn đường khỏi trang cung cấp thông tin.

<!-- note-topic-id: lec-04-topic-10 -->
## 5. HITS

Theo MMDS Ví dụ 5.13 (tr.205), một khoa có trang danh sách mọi học phần, với liên kết tới trang của từng học phần, nơi ghi giảng viên, giáo trình và đề cương. Muốn biết về một học phần, người đọc cần trang của học phần đó; muốn biết khoa có những học phần nào, người đọc cần trang danh sách trước. Hai trang có giá trị theo hai cách khác nhau, và một điểm duy nhất trộn hai cách đó. Chúng ta cần hai điểm cho mỗi trang, một phép lặp tính chúng, và biết phép lặp đó hội tụ tới đâu.

### 5.1 Hai vai trò và phép cập nhật

Theo MMDS (§5.5.1, tr.204), *trang uy tín* (authority) là trang có giá trị vì cung cấp thông tin về một chủ đề; *trang trung tâm* (hub) là trang có giá trị vì chỉ tới nơi có thông tin về chủ đề đó. Trong Ví dụ 5.13, trang học phần là trang uy tín và trang danh sách học phần là trang trung tâm. Thuật toán HITS gán cho mỗi trang $i$ một *điểm trung tâm* $h_i$ (hubbiness) và một *điểm uy tín* $a_i$ (authority score).

![Ví dụ 5.13 của MMDS. Trang danh mục học phần bên trái, nhãn trang trung tâm, có các mũi tên tới các trang học phần bên phải, nhãn trang uy tín.](img/lec-04/cap-vai-tro-hits.svg)

Hình chỉ có mũi tên từ trang danh mục tới các trang học phần: trang danh mục là trang trung tâm vì trỏ tới các trang học phần, còn mỗi trang học phần là trang uy tín vì được trang danh mục trỏ tới.

Về mặt ý tưởng, hai điểm định nghĩa lẫn nhau: một trang là trang trung tâm tốt nếu nó trỏ tới các trang uy tín tốt, và là trang uy tín tốt nếu được các trang trung tâm tốt trỏ tới (MMDS, §5.5.1, tr.205). Mỗi trang có cả hai điểm; hai vai trò không chia các trang thành hai tập rời nhau. Như MMDS (§5.5, tr.204), ta mô tả HITS trên một đồ thị cho trước.

Cách tính trực tiếp nhất: cộng điểm trung tâm của các trang trỏ tới để được điểm uy tín, rồi cộng điểm uy tín của các trang được trỏ tới để được điểm trung tâm. MMDS ghi rằng nếu chỉ cộng thì các giá trị thường tăng vượt mọi giới hạn qua các vòng, nên sau mỗi phép cộng ta chia cả véc-tơ cho thành phần lớn nhất của nó (MMDS, §5.5.2, tr.205). Để làm rõ quy tắc này, xem ví dụ sau trên đồ thị năm trang của MMDS.

![Đồ thị G5 của MMDS Hình 5.18 với năm trang A, B, C, D, E và tám cạnh: A tới B, C, D; B tới A, D; C tới E; D tới B, C. E không có cạnh ra.](img/lec-04/hinh-5-18.svg)

Trên hình, G5 giữ các cạnh của G4 trừ cạnh từ C: C chỉ trỏ tới E, và E không trỏ tới đâu.

::: example Ví dụ 04.11 (Bước uy tín và bước trung tâm thứ nhất trên G5; MMDS Ví dụ 5.15)
**Dữ kiện.** Đồ thị G5 (MMDS Hình 5.18, tr.206) có năm trang và các cạnh $\mathrm A\to\mathrm B,\mathrm C,\mathrm D$; $\mathrm B\to\mathrm A,\mathrm D$; $\mathrm C\to\mathrm E$; $\mathrm D\to\mathrm B,\mathrm C$; E là nút cụt. Khởi tạo điểm trung tâm $h^0=(1,1,1,1,1)$, thứ tự A, B, C, D, E.

**Bước uy tín.** Uy tín thô $\tilde a_j$ là tổng $h^0_i$ trên các trang $i$ trỏ tới $j$:

| Trang | Trang trỏ tới | $\tilde a_j$ | $a^1_j=\tilde a_j/2$ |
|---|---|---:|---:|
| A | B | $1$ | $1/2$ |
| B | A, D | $2$ | $1$ |
| C | A, D | $2$ | $1$ |
| D | A, B | $2$ | $1$ |
| E | C | $1$ | $1/2$ |

Giá trị lớn nhất của véc-tơ thô là 2, nên $a^1=(1/2,1,1,1,1/2)$.

**Bước trung tâm.** Trung tâm thô $\tilde h_i$ là tổng $a^1_j$ trên các trang $j$ mà $i$ trỏ tới, dùng $a^1$ vừa tính:

| Trang | Trang được trỏ tới | $\tilde h_i$ | $h^1_i=\tilde h_i/3$ |
|---|---|---:|---:|
| A | B, C, D | $1+1+1=3$ | $1$ |
| B | A, D | $1/2+1=3/2$ | $1/2$ |
| C | E | $1/2$ | $1/6$ |
| D | B, C | $1+1=2$ | $2/3$ |
| E | (không có) | $0$ | $0$ |

**Kiểm tra lại.** Giá trị lớn nhất của mỗi véc-tơ chuẩn hóa là 1. E có $h^1_{\mathrm E}=0$ vì không có cạnh ra, nhưng $a^1_{\mathrm E}=1/2$ vì có cạnh vào từ C.
:::

Phép tính không chia điểm theo bậc ra như PageRank: A trỏ tới ba trang và đóng góp trọn $h_{\mathrm A}=1$ cho mỗi trang. Hai phép chia trong một vòng dùng hai mẫu số khác nhau, $2$ và $3$, vì mỗi véc-tơ được chia cho thành phần lớn nhất của chính nó. Định nghĩa sau viết hai bước này bằng một ma trận.

::: definition Định nghĩa 04.17 (Ma trận kề, chuẩn hóa và phép cập nhật HITS)
**Ma trận kề.** Với đồ thị $G$ có $n$ trang, *ma trận kề* (adjacency matrix) $L\in\{0,1\}^{n\times n}$ có $L_{ij}=1$ khi $i\to j$ và $L_{ij}=0$ khi không; hàng là trang nguồn.

**Chuẩn hóa theo giá trị lớn nhất.** Với $z\in\mathbb R^n$, $z\ge0$ và $\max_iz_i>0$, đặt $N(z)=z/\max_iz_i$.

**Phép cập nhật HITS.** Với $h^0\in\mathbb R^n$ có mọi thành phần dương, với $t\ge0$,
$$
\begin{aligned}
\tilde a^{t+1}&=L^{\mathsf T}h^t,\\
a^{t+1}&=N(\tilde a^{t+1}),\\
\tilde h^{t+1}&=La^{t+1},\\
h^{t+1}&=N(\tilde h^{t+1}).
\end{aligned}
$$
Véc-tơ $a^t$ là *điểm uy tín*, $h^t$ là *điểm trung tâm* sau $t$ vòng. MMDS dùng $h^0=\mathbf 1$.
:::

Thành phần $j$ của $L^{\mathsf T}h$ là $\sum_i L_{ij}h_i=\sum_{i:\,i\to j}h_i$, tổng điểm trung tâm của các trang trỏ tới $j$; thành phần $i$ của $La$ là $\sum_{j:\,i\to j}a_j$, tổng điểm uy tín của các trang mà $i$ trỏ tới. Đó đúng là hai bước của Ví dụ 04.11, với
$$
L=\begin{pmatrix}0&1&1&1&0\\1&0&0&1&0\\0&0&0&0&1\\0&1&1&0&0\\0&0&0&0&0\end{pmatrix}
$$
cho G5: hàng A có số 1 ở cột B, C, D; hàng E toàn 0 vì E là nút cụt.

Phép $N$ chia mọi thành phần cho cùng một số dương, nên giữ mọi tỷ số $z_i/z_j$ và thứ tự các thành phần, đồng thời đưa thành phần lớn nhất về 1; ví dụ, $N\big((1,2,2,2,1)\big)=(1/2,1,1,1,1/2)$ có tổng 4. Hai véc-tơ HITS vì vậy không phải phân phối xác suất.

$N(0)$ không xác định, nên phép cập nhật cần véc-tơ thô khác 0; Mệnh đề 04.20 chứng minh điều này khi đồ thị có ít nhất một cạnh.

Theo MMDS Ví dụ 5.14 (tr.205), nút cụt và bẫy liên kết (Định nghĩa 03.7) không ngăn phép lặp HITS hội tụ tới một cặp véc-tơ có nghĩa, nên HITS không cần dịch chuyển hay sửa đồ thị: E của G5 được giữ nguyên.

::: example Ví dụ 04.12 (Vòng thứ hai trên G5)
**Dữ kiện.** G5 và ma trận kề $L$ viết sau Định nghĩa 04.17; theo Ví dụ 04.11, $h^1=(1,1/2,1/6,2/3,0)$.

**Bước uy tín.** $\tilde a^2=L^{\mathsf T}h^1$: A nhận từ B, $\tilde a_{\mathrm A}=1/2$; B nhận từ A, D, $\tilde a_{\mathrm B}=1+2/3=5/3$; C nhận từ A, D, $\tilde a_{\mathrm C}=5/3$; D nhận từ A, B, $\tilde a_{\mathrm D}=1+1/2=3/2$; E nhận từ C, $\tilde a_{\mathrm E}=1/6$. Chia cho $5/3$.

**Bước trung tâm.** $\tilde h^2=La^2$ với $a^2=(3/10,1,1,9/10,1/10)$: $\tilde h_{\mathrm A}=1+1+9/10=29/10$, $\tilde h_{\mathrm B}=3/10+9/10=6/5$, $\tilde h_{\mathrm C}=1/10$, $\tilde h_{\mathrm D}=1+1=2$, $\tilde h_{\mathrm E}=0$. Chia cho $29/10$.

| Trang | $\tilde a^2$ | $a^2$ | $\tilde h^2$ | $h^2$ |
|---|---:|---:|---:|---:|
| A | $1/2$ | $3/10$ | $29/10$ | $1$ |
| B | $5/3$ | $1$ | $6/5$ | $12/29$ |
| C | $5/3$ | $1$ | $1/10$ | $1/29$ |
| D | $3/2$ | $9/10$ | $2$ | $20/29$ |
| E | $1/6$ | $1/10$ | $0$ | $0$ |

**Kiểm tra lại.** Các cột $a^2$ và $h^2$ trùng các véc-tơ $a$ và $h$ của vòng hai trong MMDS Hình 5.20 (tr.207). Điểm trung tâm của C giảm từ $1/6$ xuống $1/29$, điểm uy tín của E giảm từ $1/2$ xuống $1/10$: hai điểm này chỉ dựa vào nhau qua cạnh $\mathrm C\to\mathrm E$.
:::

::: remark Nhận xét 04.18 (So $L^{\mathsf T}$ với $M_0$)
Cả $L^{\mathsf T}$ và $M_0$ có phần tử khác 0 ở hàng $j$, cột $i$ cho mỗi cạnh $i\to j$, nhưng giá trị khác nhau (MMDS, §5.5.2, tr.205):

| Biểu diễn | Vị trí của cạnh $i\to j$ | Giá trị |
|---|---|---|
| $L$ của HITS | hàng $i$, cột $j$ | $1$ |
| $L^{\mathsf T}$ | hàng $j$, cột $i$ | $1$ |
| $M_0$ của PageRank | hàng $j$, cột $i$ | $1/d_i$ |

Dùng $M_0$ thay cho $L^{\mathsf T}$ trong bước uy tín đầu tiên trên G5 cho $M_0\mathbf 1=(1/2,5/6,5/6,5/6,1)$ thay cho $(1,2,2,2,1)$: E vượt lên đầu vì C chỉ có một cạnh ra, còn A, đóng góp $1/3$ cho mỗi đích, kéo B, C, D xuống. Phép chia theo bậc ra là cách PageRank chia điểm của nguồn; HITS cộng trọn điểm của nguồn qua mỗi cạnh.
:::

<!-- note-topic-id: lec-04-topic-11 -->
### 5.2 Thuật toán và tính xác định của chuẩn hóa

Trên đồ thị lớn, hai phép nhân $L^{\mathsf T}h$ và $La$ được tính bằng cách duyệt danh sách cạnh hai lượt, không lưu $L$ dạng đặc. Khác Thuật toán 04.3, HITS giữ hai véc-tơ, và vì chúng không phải phân phối, độ thay đổi được đo bằng chuẩn cực đại $\lVert z\rVert_\infty=\max_i\lvert z_i\rvert$.

::: algorithm Thuật toán 04.19 (HITS)
**Đầu vào.** Danh sách cạnh của $G$ với $n\ge1$ trang và $\ell\ge1$ cạnh; ngưỡng $\tau>0$; số vòng tối đa $K$ nguyên dương.

**Đầu ra.** Điểm trung tâm $h$, điểm uy tín $a$, số vòng đã chạy và trạng thái *đạt ngưỡng* hoặc *hết số vòng*.

**Giả thiết.** Đồ thị có ít nhất một cạnh.

1. Đặt $h_i\leftarrow1$, $a_i\leftarrow1$ cho mọi $i$ và $t\leftarrow0$.
2. Đặt $\tilde a_j\leftarrow0$ cho mọi $j$; với mỗi cạnh $i\to j$: $\tilde a_j\leftarrow\tilde a_j+h_i$. Đặt $a'\leftarrow\tilde a/\max_j\tilde a_j$, véc-tơ uy tín mới.
3. Đặt $\tilde h_i\leftarrow0$ cho mọi $i$; với mỗi cạnh $i\to j$: $\tilde h_i\leftarrow\tilde h_i+a'_j$. Đặt $h'\leftarrow\tilde h/\max_i\tilde h_i$, véc-tơ trung tâm mới.
4. Tính $\Delta_a\leftarrow\lVert a'-a\rVert_\infty$, $\Delta_h\leftarrow\lVert h'-h\rVert_\infty$; đặt $a\leftarrow a'$, $h\leftarrow h'$, $t\leftarrow t+1$.
5. Nếu $\max(\Delta_a,\Delta_h)\le\tau$: trả $(h,a,t)$ với trạng thái đạt ngưỡng. Nếu $t=K$: trả $(h,a,t)$ với trạng thái hết số vòng. Ngược lại, quay lại bước 2.

**Dừng.** Mỗi vòng tăng $t$ thêm 1, nên thuật toán dừng sau không quá $K$ vòng.

**Trường hợp biên.** Đồ thị không có cạnh nằm ngoài giả thiết: khi đó $\tilde a=0$ và phép chia ở bước 2 không xác định. Giá trị khởi tạo của $a$ ở bước 1 chỉ dùng để tính $\Delta_a$ ở vòng đầu; $a^1$ chỉ phụ thuộc $h^0$. Một trang không có cạnh ra có $\tilde h_i=0$ ở mọi vòng.

**Chi phí.** Mô hình đếm số lần thực hiện thân vòng lặp trong một vòng, mỗi lần một thao tác:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2 (đặt 0; cộng $h_i$ vào $\tilde a_j$; tìm giá trị lớn nhất và chia) | $n$ trang; $\ell$ cạnh; $2n$ lượt trên trang | 1 | $3n+\ell$ |
| 3 (đặt 0; cộng $a'_j$ vào $\tilde h_i$; tìm giá trị lớn nhất và chia) | $n$ trang; $\ell$ cạnh; $2n$ lượt trên trang | 1 | $3n+\ell$ |
| 4 (hai độ thay đổi, thay mảng) | $n$ trang | 2 | $2n$ |

Mỗi vòng tốn $8n+2\ell$ thao tác, tức $\Theta(n+\ell)$; bộ nhớ làm việc gồm bốn mảng độ dài $n$ cộng danh sách cạnh.
:::

```text
h[i] ← 1, a[i] ← 1 với mọi i
lặp t = 1, 2, ..., K:
    ã[j] ← 0 với mọi j
    với mỗi cạnh i → j: ã[j] ← ã[j] + h[i]
    a' ← ã / max(ã)
    h̃[i] ← 0 với mọi i
    với mỗi cạnh i → j: h̃[i] ← h̃[i] + a'[j]
    h' ← h̃ / max(h̃)
    Δ_a ← max |a'[i] − a[i]|;  Δ_h ← max |h'[i] − h[i]|
    a ← a';  h ← h'
    nếu max(Δ_a, Δ_h) ≤ τ: trả (h, a, t, đạt ngưỡng)
trả (h, a, K, hết số vòng)
```

Thao tác quyết định là thứ tự hai lượt cạnh: lượt thứ hai dùng $a'$ vừa chuẩn hóa, không dùng $a$ cũ, đúng Định nghĩa 04.17. Dùng $a^0=\mathbf 1$ ở bước trung tâm đầu tiên trên G5 cho trung tâm thô $(3,2,1,2,0)$ thay cho $(3,3/2,1/2,2,0)$ của Ví dụ 04.11. Thuật toán để ngỏ hai câu hỏi: phép chia ở bước 2 và bước 3 có luôn xác định không, và dãy có giới hạn không. Mệnh đề sau trả lời câu hỏi thứ nhất.

::: proposition Mệnh đề 04.20 (Tính xác định của chuẩn hóa)
**Giả thiết.** $G$ có ít nhất một cạnh; $h^0$ có mọi thành phần dương; $h^t$, $a^t$ theo Định nghĩa 04.17.

**Kết luận.** Với mọi $t\ge1$:

- (a) $\max_j\tilde a^t_j>0$ và $\max_i\tilde h^t_i>0$, nên $a^t$ và $h^t$ xác định;
- (b) $a^t_j>0$ với mọi trang $j$ có cạnh vào, và $h^t_i>0$ với mọi trang $i$ có cạnh ra;
- (c) $a^t\ge0$, $h^t\ge0$, và giá trị lớn nhất của mỗi véc-tơ bằng 1.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Mệnh đề nói về mọi vòng hữu hạn; giới hạn có thể bằng 0 ở trang có cạnh ra, như điểm trung tâm của C trên G5 (Ví dụ 04.13).
:::

::: proof
Chứng minh bằng quy nạp theo $t$ mệnh đề $P(t)$: $h^t_i>0$ với mọi trang $i$ có cạnh ra, và $h^t\ge0$. $P(0)$ đúng vì mọi thành phần của $h^0$ dương.

**Bước 1 (bước uy tín).** Giả sử $P(t)$. Mọi số hạng của $\tilde a^{t+1}_j=\sum_{i\to j}h^t_i$ không âm, nên $\tilde a^{t+1}\ge0$. Nếu $j$ có một cạnh vào $i\to j$ thì $i$ có cạnh ra, nên $\tilde a^{t+1}_j\ge h^t_i>0$. Đồ thị có ít nhất một cạnh, nên có ít nhất một $j$ như vậy và $\max_j\tilde a^{t+1}_j>0$; $a^{t+1}=N(\tilde a^{t+1})$ xác định, không âm, có giá trị lớn nhất 1 và dương ở mọi trang có cạnh vào.

**Bước 2 (bước trung tâm).** Nếu $i$ có một cạnh ra $i\to j$ thì $j$ có cạnh vào, nên $\tilde h^{t+1}_i\ge a^{t+1}_j>0$ theo Bước 1; mọi số hạng của $\tilde h^{t+1}$ không âm. Do đó $\max_i\tilde h^{t+1}_i>0$, $h^{t+1}$ xác định, không âm, có giá trị lớn nhất 1, và $P(t+1)$ đúng.

**Bước 3 (kết luận).** Quy nạp cho $P(t)$ với mọi $t$; Bước 1 và Bước 2 ở mỗi vòng cho (a), (b), (c). $\square$
:::

Mệnh đề 04.20 cần hai giả thiết; bỏ từng giả thiết cho một phản ví dụ.

- Bỏ "ít nhất một cạnh": $\tilde a^1=0$ và $N(0)$ không xác định.
- Bỏ "$h^0$ có mọi thành phần dương": trên G5 với $h^0=(0,0,1,0,0)$, chỉ C có điểm trung tâm dương, nên $a^1=N\big((0,0,0,0,1)\big)$ chỉ dương ở E, và $h^1=(0,0,1,0,0)$; các trang A, B, D có cạnh ra nhưng điểm trung tâm bằng 0 ở mọi vòng, nên (b) sai.

Bước 1 dùng giả thiết thứ nhất; giả thiết thứ hai là cơ sở $P(0)$ của quy nạp.

Điều kiện dừng của Thuật toán 04.19 chỉ xác nhận hai véc-tơ liên tiếp khác nhau không quá $\tau$ theo chuẩn cực đại. Khác Định lý 04.5(d), HITS không có hệ số co $\beta$ chọn trước, nên $\Delta$ nhỏ không cho cận sai số tới giới hạn; khi hết $K$ vòng, thuật toán báo riêng trạng thái đó.

<!-- note-topic-id: lec-04-topic-12 -->
### 5.3 Giới hạn của phép lặp

Trên G5, điểm trung tâm của C giảm từ $1/6$ xuống $1/29$ rồi $1/139$ ở vòng thứ ba, điểm uy tín của E giảm từ $1/2$ xuống $1/10$. Để tìm giới hạn, ta viết lại hai bước của một vòng thành một phép nhân ma trận duy nhất.

::: lemma Bổ đề 04.21 (Hướng của $h^t$)
**Giả thiết.** Như Mệnh đề 04.20.

**Kết luận.** Với mọi $t\ge1$,
$$
h^t=N\big((LL^{\mathsf T})^th^0\big).
$$

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Bổ đề cho hướng của $h^t$; nó không nói dãy hội tụ.
:::

::: proof
**Bước 1 ($N$ bỏ qua hệ số dương).** Với $z\ge0$, $\max_iz_i>0$ và $\alpha>0$, $N(\alpha z)=\alpha z/(\alpha\max_iz_i)=N(z)$.

**Bước 2 (quy nạp).** Ta chứng minh $h^t=\alpha_t(LL^{\mathsf T})^th^0$ với một số $\alpha_t>0$, cho mọi $t\ge0$; với $t=0$, $\alpha_0=1$. Giả sử điều đó đúng với $t$. Theo Định nghĩa 04.17, $a^{t+1}=L^{\mathsf T}h^t/\mu_t$ với $\mu_t=\max_j\tilde a^{t+1}_j>0$ (Mệnh đề 04.20(a)), nên
$$
\tilde h^{t+1}=La^{t+1}=\frac{\alpha_t}{\mu_t}(LL^{\mathsf T})^{t+1}h^0 ,
$$
và $h^{t+1}=\tilde h^{t+1}/\mu'_t$ với $\mu'_t=\max_i\tilde h^{t+1}_i>0$; đặt $\alpha_{t+1}=\alpha_t/(\mu_t\mu'_t)>0$.

**Bước 3 (kết luận).** Với $t\ge1$, $h^t$ có thành phần lớn nhất bằng 1 (Mệnh đề 04.20(c)), nên $h^t=N(h^t)=N\big(\alpha_t(LL^{\mathsf T})^th^0\big)=N\big((LL^{\mathsf T})^th^0\big)$ theo Bước 1. $\square$
:::

Theo Bổ đề 04.21, sau $t$ vòng $h^t$ có cùng hướng với $(LL^{\mathsf T})^th^0$: HITS là phép lặp lũy thừa (power iteration) trên ma trận đối xứng $LL^{\mathsf T}$, chuẩn hóa sau mỗi vòng. MMDS viết điều kiện tại giới hạn dưới dạng $h=\lambda La$, $a=\mu L^{\mathsf T}h$ với hai hằng chuẩn hóa, rồi thế một quan hệ vào quan hệ kia (§5.5.2, tr.206). Ở đây, $h$ tỷ lệ dương với $La$ và $a$ tỷ lệ dương với $L^{\mathsf T}h$, nên $h$ tỷ lệ dương với $LL^{\mathsf T}h$: $h$ là một véc-tơ riêng của $LL^{\mathsf T}$. Định lý sau cho biết véc-tơ riêng nào và dưới giả thiết nào.

::: theorem Định lý 04.22 (Giới hạn của HITS)
**Giả thiết.** $G$ có ít nhất một cạnh; $h^0$ có mọi thành phần dương; $LL^{\mathsf T}$ có các trị riêng $\lambda_1>\lambda_2\ge\cdots\ge\lambda_n\ge0$, tức trị riêng lớn nhất là đơn, với cơ sở trực chuẩn véc-tơ riêng $\psi_1,\dots,\psi_n$.

**Kết luận.**

- (a) Có thể chọn dấu của $\psi_1$ để $\psi_1\ge0$; khi đó $\gamma_1=\psi_1^{\mathsf T}h^0>0$.
- (b) $h^t\to h^*=N(\psi_1)$ và $a^t\to a^*=N(L^{\mathsf T}\psi_1)$ khi $t\to\infty$; hai giới hạn không phụ thuộc $h^0$.
- (c) $LL^{\mathsf T}h^*=\lambda_1h^*$, $L^{\mathsf T}La^*=\lambda_1a^*$, $a^*=N(L^{\mathsf T}h^*)$ và $h^*=N(La^*)$.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Định lý không cho số vòng cần để đạt một sai số cho trước; theo Bước 4 của chứng minh, phần sai lệch giảm theo $(\lambda_i/\lambda_1)^t$, nên tốc độ phụ thuộc tỷ số $\lambda_2/\lambda_1$ của từng đồ thị. Khi trị riêng lớn nhất không đơn, giới hạn có thể phụ thuộc $h^0$.
:::

::: proof
Ý tưởng: khai triển $h^0$ theo các véc-tơ riêng; sau $t$ vòng, thành phần theo $\psi_1$ được nhân $\lambda_1^t$, các thành phần khác được nhân $\lambda_i^t$ nhỏ hơn, nên sau chuẩn hóa chỉ còn hướng $\psi_1$. Bước 1 và Bước 4 theo lập luận phép lặp lũy thừa của BHK (§3.7, tr.51–52), được BHK áp dụng cho HITS (§3.9.4, tr.62); Bước 3 chứng minh véc-tơ riêng chọn được không âm.

**Bước 1 (khai triển).** Theo định lý phổ, $h^0=\sum_{i=1}^n\gamma_i\psi_i$ với $\gamma_i=\psi_i^{\mathsf T}h^0$, và $(LL^{\mathsf T})^th^0=\sum_i\gamma_i\lambda_i^t\psi_i$.

**Bước 2 ($\lambda_1>0$).** Với một cạnh $i\to j$, phần tử đường chéo $(LL^{\mathsf T})_{ii}=d_i\ge1$, nên vết của $LL^{\mathsf T}$, bằng tổng các trị riêng, ít nhất bằng 1; vì mọi trị riêng không âm, $\lambda_1\ge1/n>0$.

**Bước 3 (véc-tơ riêng không âm).** Với $z\in\mathbb R^n$ và $\lVert z\rVert_2=1$, viết $z=\sum_i\xi_i\psi_i$; khi đó $z^{\mathsf T}LL^{\mathsf T}z=\sum_i\lambda_i\xi_i^2\le\lambda_1$, dấu bằng xảy ra khi và chỉ khi $\xi_i=0$ với mọi $i\ge2$, vì $\lambda_i<\lambda_1$ khi $i\ge2$. Đặt $\lvert\psi_1\rvert$ là véc-tơ các trị tuyệt đối của $\psi_1$. Mọi phần tử của $LL^{\mathsf T}$ không âm, nên
$$
\begin{aligned}
&\lvert\psi_1\rvert^{\mathsf T}LL^{\mathsf T}\lvert\psi_1\rvert\\
&\quad\ge\psi_1^{\mathsf T}LL^{\mathsf T}\psi_1=\lambda_1 .
\end{aligned}
$$
Do $\lVert\lvert\psi_1\rvert\rVert_2=1$, dấu bằng xảy ra, nên $\lvert\psi_1\rvert$ là bội của $\psi_1$ có cùng độ dài, tức $\lvert\psi_1\rvert=\pm\psi_1$. Chọn dấu để $\psi_1=\lvert\psi_1\rvert\ge0$. Khi đó $\psi_1\ne0$ và $h^0$ có mọi thành phần dương, nên $\gamma_1=\sum_i\psi_{1,i}h^0_i>0$. Đó là (a).

**Bước 4 (giới hạn của $h$).** Theo Bước 1,
$$
\begin{aligned}
\frac{(LL^{\mathsf T})^th^0}{\lambda_1^t}&=\gamma_1\psi_1\\
&\quad+\sum_{i\ge2}\gamma_i\Big(\frac{\lambda_i}{\lambda_1}\Big)^t\psi_i\\
&\longrightarrow\gamma_1\psi_1,
\end{aligned}
$$
vì $0\le\lambda_i/\lambda_1<1$ khi $i\ge2$. Theo Bổ đề 04.21 và Bước 1 của chứng minh bổ đề, $h^t=N\big((LL^{\mathsf T})^th^0/\lambda_1^t\big)$ với mọi $t\ge1$. Hàm $N$ liên tục tại mọi $z$ có $\max_iz_i>0$, và $\gamma_1\psi_1\ge0$ có thành phần lớn nhất dương, nên $h^t\to N(\gamma_1\psi_1)=N(\psi_1)$; giới hạn này không chứa $h^0$.

**Bước 5 (giới hạn của $a$).** $L^{\mathsf T}\psi_1\ge0$ vì $L\ge0$ và $\psi_1\ge0$, và $\lVert L^{\mathsf T}\psi_1\rVert_2^2=\psi_1^{\mathsf T}LL^{\mathsf T}\psi_1=\lambda_1>0$, nên $L^{\mathsf T}h^*$ có thành phần lớn nhất dương. Theo Định nghĩa 04.17, $a^{t+1}=N(L^{\mathsf T}h^t)$; tính liên tục của phép nhân với $L^{\mathsf T}$ và của $N$ cho $a^t\to N(L^{\mathsf T}h^*)=N(L^{\mathsf T}\psi_1)$.

**Bước 6 (phương trình tại giới hạn).** $h^*$ là bội dương của $\psi_1$, nên $LL^{\mathsf T}h^*=\lambda_1h^*$. Đặt $\phi=L^{\mathsf T}\psi_1$; khi đó $L^{\mathsf T}L\phi=L^{\mathsf T}(LL^{\mathsf T}\psi_1)=\lambda_1\phi$, và $a^*$ là bội dương của $\phi$, nên $L^{\mathsf T}La^*=\lambda_1a^*$. $La^*$ là bội dương của $L\phi=\lambda_1\psi_1$, nên $N(La^*)=N(\psi_1)=h^*$. Đó là (c). $\square$
:::

Định lý 04.22 thay quan sát "ba vòng tiến dần tới một giới hạn" bằng một mô tả chính xác: giới hạn của điểm trung tâm là véc-tơ riêng của $LL^{\mathsf T}$ ứng với trị riêng lớn nhất, và giới hạn của điểm uy tín là véc-tơ riêng của $L^{\mathsf T}L$ ứng với cùng trị riêng. So với Định lý 04.5, định lý này không có hệ số co chọn trước: giả thiết nằm ở phổ của ma trận do đồ thị quyết định. Ví dụ sau tính giới hạn trên G5 bằng hệ phương trình, theo cách của MMDS.

::: example Ví dụ 04.13 (Giới hạn trên G5; MMDS Ví dụ 5.15)
**Dữ kiện.** G5 với $L$ như sau Định nghĩa 04.17. Phần tử $(i,k)$ của $LL^{\mathsf T}$ là số trang mà cả $i$ và $k$ cùng trỏ tới:
$$
LL^{\mathsf T}=\begin{pmatrix}3&1&0&2&0\\1&2&0&0&0\\0&0&1&0&0\\2&0&0&2&0\\0&0&0&0&0\end{pmatrix}.
$$

**Lập hệ.** Gọi $\nu$ là trị riêng và $(h_{\mathrm A},\dots,h_{\mathrm E})$ là véc-tơ riêng:

- $\nu h_{\mathrm A}=3h_{\mathrm A}+h_{\mathrm B}+2h_{\mathrm D}$;
- $\nu h_{\mathrm B}=h_{\mathrm A}+2h_{\mathrm B}$, nên $h_{\mathrm B}=h_{\mathrm A}/(\nu-2)$;
- $\nu h_{\mathrm C}=h_{\mathrm C}$;
- $\nu h_{\mathrm D}=2h_{\mathrm A}+2h_{\mathrm D}$, nên $h_{\mathrm D}=2h_{\mathrm A}/(\nu-2)$;
- $\nu h_{\mathrm E}=0$.

**Trị riêng lớn nhất.** Thế $h_{\mathrm B}$, $h_{\mathrm D}$ vào phương trình đầu và chia cho $h_{\mathrm A}\ne0$: $\nu=3+5/(\nu-2)$, tức $\nu^2-5\nu+1=0$, nghiệm lớn $\nu=(5+\sqrt{21})/2\approx4{,}7913$. Khối A, B, D có đa thức đặc trưng $(\nu-2)(\nu^2-5\nu+1)$, nên các trị riêng của $LL^{\mathsf T}$ là $\tfrac{5+\sqrt{21}}2$, $2$, $1$ (hàng C), $\tfrac{5-\sqrt{21}}2\approx0{,}2087$ và $0$ (hàng E): trị riêng lớn nhất là đơn và Định lý 04.22 áp dụng được.

**Điểm trung tâm.** Với $\nu\ne1$ và $\nu\ne0$, hai phương trình hàng C, E cho $h_{\mathrm C}=h_{\mathrm E}=0$. Đặt $h_{\mathrm A}=1$; $\nu-2=(1+\sqrt{21})/2$, nên
$$
\begin{aligned}
h^*&=\Big(1,\ \frac{\sqrt{21}-1}{10},\ 0,\\
&\qquad\frac{\sqrt{21}-1}5,\ 0\Big)\\
&\approx(1;\,0{,}3583;\,0;\,0{,}7165;\,0).
\end{aligned}
$$

**Điểm uy tín.** $L^{\mathsf T}h^*$: A nhận từ B, $\tfrac{\sqrt{21}-1}{10}$; B và C nhận từ A, D, $1+\tfrac{\sqrt{21}-1}5=\tfrac{4+\sqrt{21}}5$; D nhận từ A, B, $\tfrac{9+\sqrt{21}}{10}$; E nhận từ C, $0$. Chia cho giá trị lớn nhất $\tfrac{4+\sqrt{21}}5$:
$$
\begin{aligned}
a^*&=\Big(\frac{5-\sqrt{21}}2,\ 1,\ 1,\\
&\qquad\frac{\sqrt{21}-3}2,\ 0\Big)\\
&\approx(0{,}2087;\,1;\,1;\,0{,}7913;\,0).
\end{aligned}
$$

**Kiểm tra lại.** Hàng A: $3+\tfrac{\sqrt{21}-1}{10}+2\cdot\tfrac{\sqrt{21}-1}5=\tfrac{25+5\sqrt{21}}{10}=\tfrac{5+\sqrt{21}}2=\nu$. Vòng thứ ba của phép lặp, $h^3=(1,53/139,1/139,98/139,0)\approx(1;\,0{,}381;\,0{,}007;\,0{,}705;\,0)$, đã gần $h^*$.
:::

Kết quả có cách đọc trực tiếp trên đồ thị (MMDS, tr.208). E không trỏ tới đâu nên điểm trung tâm bằng 0. Điểm trung tâm của C chỉ dựa vào điểm uy tín của E và ngược lại, nên cả hai tiến về 0: trên $LL^{\mathsf T}$, C nằm trong một khối riêng với trị riêng $1<\lambda_1$. A là trang trung tâm lớn nhất vì trỏ tới ba trang uy tín lớn nhất B, C, D; B và C là hai trang uy tín lớn nhất vì được hai trang trung tâm lớn nhất A và D trỏ tới.

Định lý 04.22 cần trị riêng lớn nhất đơn và khởi tạo dương; bỏ một trong hai thì kết luận (b) sai.

- Bỏ "trị riêng lớn nhất là đơn": đồ thị bốn trang với hai cạnh $\mathrm A\to\mathrm B$, $\mathrm C\to\mathrm D$ có $LL^{\mathsf T}=\mathrm{diag}(1,0,1,0)$, trị riêng 1 bội hai. Từ $h^0=(1,1,1,1)$, mọi vòng cho $a=(0,1,0,1)$, $h=(1,0,1,0)$; từ $h^0=(1,1,1/2,1)$, mọi vòng cho $a=(0,1,0,1/2)$, $h=(1,0,1/2,0)$. Hai khởi tạo dương cho hai giới hạn khác nhau.
- Bỏ "$h^0$ có mọi thành phần dương": trên G5 với $h^0=(0,0,1,0,0)$, $h^t=(0,0,1,0,0)$ ở mọi vòng (sau Mệnh đề 04.20), khác $h^*$ của Ví dụ 04.13; ở đây $\gamma_1=\psi_1^{\mathsf T}h^0=\psi_{1,\mathrm C}=0$.

Bước 3 và Bước 4 của chứng minh dùng giả thiết trị riêng đơn: Bước 3 để $\lvert\psi_1\rvert$ cùng hướng với $\psi_1$, Bước 4 để mọi tỷ số $\lambda_i/\lambda_1$ với $i\ge2$ nhỏ hơn 1. Giả thiết $h^0$ dương cho $\gamma_1>0$ ở Bước 3, và nhờ đó $N(\gamma_1\psi_1)$ xác định ở Bước 4.

<!-- note-topic-id: lec-04-topic-13 -->
### 5.4 Chi phí

Bổ đề 04.21 nói HITS là phép lặp trên $LL^{\mathsf T}$, nên có hai cách tính một vòng: dựng $LL^{\mathsf T}$ một lần rồi nhân với $h$, hoặc nhân lần lượt với $L^{\mathsf T}$ và $L$ như Thuật toán 04.19. MMDS chọn cách thứ hai vì $LL^{\mathsf T}$ và $L^{\mathsf T}L$ không thưa như $L$ và $L^{\mathsf T}$ (§5.5.2, tr.206). Mệnh đề sau đếm chi phí của cách thứ hai.

::: proposition Mệnh đề 04.23 (Chi phí một vòng HITS)
**Giả thiết.** Mô hình chi phí đơn vị cho mỗi phép toán vô hướng; đầu vào là danh sách $\ell$ cạnh của đồ thị $n$ trang; Thuật toán 04.19 thực chạy $K_{\mathrm H}$ vòng.

**Kết luận.** Mỗi vòng tốn $2\ell$ phép cộng theo cạnh và $\Theta(n)$ thao tác trên các trang, tức $\Theta(n+\ell)$; bộ nhớ làm việc là $\Theta(n)$ ngoài đầu vào $\Theta(n+\ell)$; cả thuật toán tốn $\Theta\big(K_{\mathrm H}(n+\ell)\big)$.

**Điều kiện áp dụng.** Như Thuật toán 04.19.

**Phạm vi.** $K_{\mathrm H}$ phụ thuộc đồ thị và $\tau$; mệnh đề không chặn $K_{\mathrm H}$.
:::

::: proof
Theo bảng chi phí của Thuật toán 04.19, mỗi cạnh $i\to j$ được dùng đúng hai lần mỗi vòng: một lần ở bước 2 cộng $h_i$ vào $\tilde a_j$, một lần ở bước 3 cộng $a'_j$ vào $\tilde h_i$, tổng $2\ell$ phép cộng. Các bước đặt 0, tìm giá trị lớn nhất, chia và đo độ thay đổi duyệt mỗi trang một số lần không phụ thuộc $n$, tổng $\Theta(n)$. Bốn mảng độ dài $n$ là bộ nhớ làm việc. Nhân với $K_{\mathrm H}$ vòng được tổng. $\square$
:::

Trên đồ thị bốn trang với ba cạnh $\mathrm A\to\mathrm D$, $\mathrm B\to\mathrm D$, $\mathrm C\to\mathrm D$, $L$ có 3 phần tử khác 0 nhưng $LL^{\mathsf T}$ có 9: ba trang A, B, C cùng trỏ tới D, nên mọi phần tử $(LL^{\mathsf T})_{ik}$ với $i,k\in\{\mathrm A,\mathrm B,\mathrm C\}$ bằng 1. Tổng quát, một trang có $d^{\mathrm{in}}$ cạnh vào đóng góp $d^{\mathrm{in}}$ phần tử vào $L$ nhưng đóng góp vào $(d^{\mathrm{in}})^2$ phần tử của $LL^{\mathsf T}$. So với Thuật toán 04.3, một vòng HITS duyệt cạnh hai lần thay cho một lần: cùng bậc $\Theta(n+\ell)$, khác hệ số.

::: remark Nhận xét 04.24 (Trong thực hành: HITS)
- HITS ban đầu được thiết kế để chạy trên tập trang trả lời một truy vấn, cùng lúc xử lý truy vấn đó, khác PageRank là bước tiền xử lý (MMDS, §5.5, tr.204); khi đó $n$ và $\ell$ là kích thước của đồ thị con, và cả thuật toán chạy cho mỗi truy vấn.
- Trên đồ thị cỡ web, cách duy nhất để tính hai véc-tơ là phép lặp (MMDS, tr.208). Mỗi lượt cạnh ở bước 2 và bước 3 là một phép nhân ma trận–véc-tơ, nên chạy được bằng công việc MapReduce theo khối của Thuật toán 03.22 với ba thay đổi: phần tử của ma trận là 1 thay cho $1/d_j$; không có phần chung $((1-\beta)+\beta\delta)/n$ và pha tính $\delta$; sau mỗi phép nhân có thêm một pha tìm giá trị lớn nhất trên toàn véc-tơ trước khi chuẩn hóa. Bước uy tín dùng $L^{\mathsf T}$, bước trung tâm dùng $L$.
- Giả thiết trị riêng lớn nhất đơn của Định lý 04.22 phụ thuộc đồ thị, như phản ví dụ sau định lý.
- MMDS nêu một cách chuẩn hóa khác: chia cho tổng các thành phần (§5.5.2, tr.205). Hai cách cho cùng hướng ở mọi vòng nhưng khác số, nên khi so kết quả của hai chương trình, cần biết chúng dùng cách chuẩn hóa nào.
:::

::: exercise Bài tập 04.6 (Vòng thứ ba trên G5)
Trên G5 với $h^2=(1,12/29,1/29,20/29,0)$ (Ví dụ 04.12):

- (a) Tính uy tín thô $\tilde a^3_{\mathrm D}$ và điểm uy tín $a^3_{\mathrm D}$.
- (b) Nếu mỗi nguồn chia $h_i$ cho bậc ra của mình trước khi cộng, tính lại $\tilde a^3_{\mathrm D}$ và nêu định nghĩa bị thay.
- (c) Tính $a^3_{\mathrm E}$ và giải thích vì sao E có điểm uy tín dương dù không có cạnh ra.
:::

::: hint
D nhận cạnh từ A và B. Giá trị lớn nhất của $\tilde a^3$ đạt ở B và C, cùng nhận từ A và D.
:::

::: solution
**Câu (a).** $\tilde a^3_{\mathrm D}=h^2_{\mathrm A}+h^2_{\mathrm B}=1+\tfrac{12}{29}=\tfrac{41}{29}$. Giá trị lớn nhất của $\tilde a^3$ là $\tilde a^3_{\mathrm B}=\tilde a^3_{\mathrm C}=h^2_{\mathrm A}+h^2_{\mathrm D}=\tfrac{49}{29}$, nên $a^3_{\mathrm D}=\tfrac{41}{49}$. Cả véc-tơ là $a^3=(12/49,1,1,41/49,1/49)$.

**Câu (b).** A có bậc ra 3, B có bậc ra 2, nên $\tilde a^3_{\mathrm D}=\tfrac13+\tfrac12\cdot\tfrac{12}{29}=\tfrac13+\tfrac6{29}=\tfrac{47}{87}$, khác $\tfrac{41}{29}=\tfrac{123}{87}$. Phép chia này thay $L^{\mathsf T}$ của Định nghĩa 04.17 bằng $M_0$ (Nhận xét 04.18): điểm uy tín không còn là tổng điểm trung tâm của các trang trỏ tới.

**Câu (c).** E chỉ nhận cạnh từ C, nên $\tilde a^3_{\mathrm E}=h^2_{\mathrm C}=\tfrac1{29}$ và $a^3_{\mathrm E}=\tfrac1{49}$. Điểm uy tín phụ thuộc cạnh vào; thiếu cạnh ra chỉ làm điểm trung tâm của E bằng 0. Theo Mệnh đề 04.20(b), $a^t_{\mathrm E}>0$ ở mọi vòng, nhưng theo Ví dụ 04.13 giới hạn của nó bằng 0.

**Kiểm tra lại.** A chỉ nhận cạnh từ B, nên $a^3_{\mathrm A}=\tfrac{12}{29}\cdot\tfrac{29}{49}=\tfrac{12}{49}$, và giá trị lớn nhất của $a^3$ là 1, ở B và C. Dãy $a^1_{\mathrm D}=1$, $a^2_{\mathrm D}=0{,}9$, $a^3_{\mathrm D}=\tfrac{41}{49}\approx0{,}837$ giảm dần về $a^*_{\mathrm D}\approx0{,}7913$ của Ví dụ 04.13.
:::

HITS gán mỗi trang hai điểm định nghĩa lẫn nhau qua ma trận kề $L$ (Định nghĩa 04.17); Thuật toán 04.19 tính chúng bằng hai lượt cạnh mỗi vòng với chi phí $\Theta(n+\ell)$ (Mệnh đề 04.23), và phép chuẩn hóa luôn xác định khi đồ thị có cạnh (Mệnh đề 04.20). Phép lặp là phép lặp lũy thừa trên $LL^{\mathsf T}$ (Bổ đề 04.21), nên khi trị riêng lớn nhất là đơn, hai véc-tơ hội tụ tới véc-tơ riêng tương ứng của $LL^{\mathsf T}$ và $L^{\mathsf T}L$ (Định lý 04.22); trên G5, $h^*\approx(1;\,0{,}3583;\,0;\,0{,}7165;\,0)$. Định lý không cho số vòng cần thiết, và khi trị riêng lớn nhất là bội, giới hạn có thể phụ thuộc $h^0$. Trong Mục 6, chúng ta đặt bốn công cụ của chương cạnh nhau.

<!-- note-topic-id: lec-04-topic-14 -->
<!-- note-collapsed -->
## Đọc thêm: Tốc độ hội tụ của HITS

Trên G5, khoảng cách $\lVert h^t-h^*\rVert_\infty$ là khoảng $0{,}167$ sau một vòng, $0{,}056$ sau hai vòng, $0{,}023$ sau ba vòng và $5{,}1\cdot10^{-5}$ sau mười vòng; từ vòng thứ ba, mỗi vòng nhân sai số với khoảng $0{,}42$. Kết quả sau, theo lập luận của BHK (Định lý 3.11, tr.52–53), giải thích con số này và cho biết phép lặp vẫn bảo đảm gì khi trị riêng lớn nhất không đơn. Trong phần này, $\hat h^0=h^0/\lVert h^0\rVert_2$ là khởi tạo chuẩn hóa độ dài 1, $\hat\gamma_i=\psi_i^{\mathsf T}\hat h^0$, và $z_t=(LL^{\mathsf T})^t\hat h^0/\lVert(LL^{\mathsf T})^t\hat h^0\rVert_2$.

::: theorem Định lý 04.25 (Phép lặp lũy thừa với khoảng cách trị riêng)
**Giả thiết.** $LL^{\mathsf T}$ có các trị riêng $\lambda_1\ge\cdots\ge\lambda_n\ge0$, $\lambda_1>0$, với cơ sở trực chuẩn véc-tơ riêng $\psi_1,\dots,\psi_n$; $\lvert\hat\gamma_1\rvert\ge\eta>0$; $0<\kappa<1$; $U$ là không gian sinh bởi các $\psi_i$ có $\lambda_i>\kappa\lambda_1$.

**Kết luận.** Với mọi $t\ge1$, thành phần của $z_t$ vuông góc với $U$ có độ dài không quá $\kappa^t/\eta$. Đặc biệt, khi $\lambda_1>\lambda_2>0$ và $\kappa=\lambda_2/\lambda_1$, $U$ là đường thẳng sinh bởi $\psi_1$, và khoảng cách từ $z_t$ tới đường thẳng đó không quá $(\lambda_2/\lambda_1)^t/\eta$.

**Điều kiện áp dụng.** Số học chính xác.

**Phạm vi.** Cận đo theo chuẩn $\lVert\cdot\rVert_2$ trên véc-tơ độ dài 1; khi $G$ có ít nhất một cạnh và $h^0$ có mọi thành phần dương, Bổ đề 04.21 cho $h^t$ là bội dương của $z_t$.
:::

::: proof
**Bước 1 (khai triển).** $\hat h^0=\sum_i\hat\gamma_i\psi_i$ với $\sum_i\hat\gamma_i^2=\lVert\hat h^0\rVert_2^2=1$ và $\lvert\hat\gamma_1\rvert\ge\eta$; khi đó $(LL^{\mathsf T})^t\hat h^0=\sum_i\hat\gamma_i\lambda_i^t\psi_i$.

**Bước 2 (cận dưới của độ dài).** Các $\psi_i$ trực chuẩn, nên
$$
\begin{aligned}
\lVert(LL^{\mathsf T})^t\hat h^0\rVert_2^2&=\sum_i\hat\gamma_i^2\lambda_i^{2t}\\
&\ge\hat\gamma_1^2\lambda_1^{2t}\ge\eta^2\lambda_1^{2t}.
\end{aligned}
$$

**Bước 3 (cận trên của phần vuông góc).** Thành phần của $(LL^{\mathsf T})^t\hat h^0$ vuông góc với $U$ là $\sum_{i:\,\lambda_i\le\kappa\lambda_1}\hat\gamma_i\lambda_i^t\psi_i$, có bình phương độ dài
$$
\begin{aligned}
&\sum_{i:\,\lambda_i\le\kappa\lambda_1}\hat\gamma_i^2\lambda_i^{2t}\\
&\quad\le\kappa^{2t}\lambda_1^{2t}\sum_i\hat\gamma_i^2=\kappa^{2t}\lambda_1^{2t}.
\end{aligned}
$$

**Bước 4 (tỷ số).** Chia căn bậc hai của Bước 3 cho căn bậc hai của Bước 2 được cận $\kappa^t/\eta$ cho thành phần vuông góc của $z_t$. Khi $\lambda_1>\lambda_2>0$ và $\kappa=\lambda_2/\lambda_1$, chỉ $\lambda_1$ lớn hơn $\kappa\lambda_1$, nên $U$ sinh bởi $\psi_1$. $\square$
:::

Cận giảm theo cấp số nhân với công bội $\lambda_2/\lambda_1$, khoảng cách tương đối giữa hai trị riêng lớn nhất. Hằng số $1/\eta$ đo mức khởi tạo lệch khỏi $\psi_1$; với $h^0=\mathbf 1$ và $\psi_1\ge0$, đúng khi $\lambda_1$ đơn (Định lý 04.22(a)), có thể lấy $\eta=\sum_i\psi_{1,i}/\sqrt n>0$. Khi trị riêng lớn nhất là bội, vẫn chọn được $\kappa<1$ sao cho $U$ chỉ gồm các véc-tơ riêng của $\lambda_1$: phép lặp đưa $z_t$ về không gian riêng của $\lambda_1$, nhưng vị trí trong không gian đó do $h^0$ quyết định.

::: example Ví dụ 04.14 (Tốc độ trên G5 và trên hai thành phần rời nhau)
**Dữ kiện.** G5 có trị riêng $\lambda_1=\tfrac{5+\sqrt{21}}2$ và $\lambda_2=2$ (Ví dụ 04.13), $h^0=\mathbf 1$. Đồ thị bốn trang với $\mathrm A\to\mathrm B$, $\mathrm C\to\mathrm D$ có $LL^{\mathsf T}=\mathrm{diag}(1,0,1,0)$.

**G5.** $\kappa=\lambda_2/\lambda_1=4/(5+\sqrt{21})=5-\sqrt{21}\approx0{,}4174$. Véc-tơ riêng đơn vị $\psi_1\approx(0{,}7805;\,0{,}2796;\,0;\,0{,}5592;\,0)$ và $\hat h^0=\mathbf 1/\sqrt5$ cho $\eta=\psi_1^{\mathsf T}\hat h^0\approx0{,}7242$. Định lý 04.25 bảo đảm thành phần vuông góc với $\psi_1$ không quá $10^{-3}$ khi $\kappa^t/\eta\le10^{-3}$, tức $t\ge\ln(0{,}7242\cdot10^{-3})/\ln0{,}4174\approx8{,}3$, nên 9 vòng là đủ. Thành phần vuông góc thật sau 9 vòng là khoảng $1{,}1\cdot10^{-4}$, và tỷ số giữa hai vòng liên tiếp là khoảng $0{,}417$, đúng $\kappa$.

**Hai thành phần rời nhau.** $\lambda_1=\lambda_2=1$, $\lambda_3=\lambda_4=0$. Với mọi $\kappa\in(0,1)$, $U$ là không gian sinh bởi hai véc-tơ đơn vị của A và C, và thành phần vuông góc với $U$ bằng 0 ngay từ $t=1$. Từ $h^0=(1,1,1,1)$, $z_1$ tỷ lệ với $(1,0,1,0)$; từ $h^0=(1,1,1/2,1)$, $z_1$ tỷ lệ với $(1,0,1/2,0)$: cả hai nằm trong $U$ nhưng khác hướng, đúng hai giới hạn sau Định lý 04.22.

**Kiểm tra lại.** $\kappa^9/\eta\approx(0{,}4174)^9/0{,}7242\approx5{,}3\cdot10^{-4}\le10^{-3}$, còn $\kappa^8/\eta\approx1{,}27\cdot10^{-3}>10^{-3}$.
:::

<!-- note-topic-id: lec-04-topic-15 -->
## 6. So sánh các phương pháp xếp hạng liên kết

Mục 1 nêu ba nhu cầu: thứ hạng theo ngữ cảnh truy vấn, thứ hạng khó thao túng bằng liên kết, và hai vai trò của một trang. Chương trả lời ba nhu cầu đó bằng ba phép lặp và một chỉ số dẫn xuất; mỗi phép lặp chạy trên danh sách kề với chi phí $\Theta(n+\ell)$ mỗi vòng. Điều phân biệt chúng là thông tin phải có thêm, đầu ra và giả thiết mà bảo đảm cần.

| Công cụ | Đầu vào thêm | Đầu ra | Giả thiết không được bỏ | Chi phí |
|---|---|---|---|---|
| PageRank theo chủ đề | tập chủ đề $S$ hoặc phân phối $v$; trọng số $w_\theta$ khi ghép | một phân phối mỗi chủ đề; điểm ghép $q_i$ | $v$ là phân phối cố định; $0<\beta<1$; ghép cần cùng $\beta$, cùng bù theo $u$ | $3n+\ell$ mỗi vòng; truy vấn $\Theta(kc)$ |
| TrustRank | tập tin cậy $T$ đánh giá bên ngoài | một phân phối $\rho$ | như trên; $T$ hiếm khi trỏ tới trang rác | $3n+\ell$ mỗi vòng |
| Khối lượng rác | $r$ và $\rho$ | chỉ số $s_i\le1$ mỗi trang | $r$, $\rho$ cùng đồ thị, cùng $\beta$, cùng bù; $r_i>0$ | hai phép lặp, thêm $\Theta(n)$ |
| HITS | đồ thị con của truy vấn, khi chạy theo truy vấn | hai véc-tơ $h$, $a$ với giá trị lớn nhất 1 | đồ thị có ít nhất một cạnh; giới hạn duy nhất cần trị riêng lớn nhất của $LL^{\mathsf T}$ đơn | $8n+2\ell$ mỗi vòng |

Bảng đọc theo cột. Cột đầu vào thêm cho thấy PageRank theo chủ đề và TrustRank dùng cùng phép lặp nhưng cần hai loại thông tin khác nhau: một tập trang theo chủ đề, hoặc một tập trang được đánh giá tin cậy. Cột đầu ra cho thấy chỉ HITS trả hai điểm cho mỗi trang, và chỉ hai phép lặp đầu trả phân phối xác suất. Điểm uy tín của HITS và điểm tin cậy của TrustRank có tên gần nhau nhưng khác nghĩa: điểm uy tín nhận từ các trang trung tâm theo cấu trúc liên kết, còn TrustRank là phân phối lan từ các trang được đánh giá bên ngoài.

Cùng bậc $\Theta(n+\ell)$ mỗi vòng không suy ra cùng thời gian chạy. Hai phép lặp có thể cần số vòng khác nhau: PageRank theo chủ đề có cận $2\beta^t$ chỉ phụ thuộc $\beta$ (Định lý 04.5), còn phần sai lệch của HITS giảm theo $(\lambda_i/\lambda_1)^t$ (Bước 4 của chứng minh Định lý 04.22), do đồ thị quyết định. Hệ số công việc cũng khác, $3n+\ell$ so với $8n+2\ell$; và việc chuẩn bị tập chủ đề hay tập tin cậy không nằm trong chi phí một vòng.

::: exercise Bài tập 04.7 (Năm câu tự kiểm tra)
Trả lời và nêu kết quả của chương đã dùng.

- (a) Trên đồ thị $n=10^9$ trang, $\ell=10^{10}$ cạnh, so tổng thao tác của việc tiền tính 16 véc-tơ chủ đề, mỗi véc-tơ 86 vòng, với một lần chạy HITS 86 vòng trên cùng đồ thị. Nêu các đại lượng mà phép so này bỏ qua.
- (b) Xét cụm thao túng của Định nghĩa 04.9 trên đồ thị không có nút cụt, và TrustRank với tập tin cậy $T$ không chứa trang nào của cụm. Viết phương trình của điểm TrustRank $p$ mỗi trang hỗ trợ và $y$ của trang đích, với $x_\rho$ là đóng góp TrustRank từ ngoài vào trang đích; nêu các số hạng của Mệnh đề 04.10 bị mất.
- (c) Chứng minh rằng nếu tập tin cậy là toàn bộ $V$ thì khối lượng rác của mọi trang bằng 0.
- (d) Trên đồ thị bảy trang của Ví dụ 04.6, tính điểm uy tín $a^1$ của HITS từ $h^0=\mathbf 1$. Trang nào có điểm uy tín lớn nhất, và điều đó so với thứ hạng PageRank thế nào?
- (e) Đồ thị gồm hai bản sao rời nhau của G4. Xác định trị riêng lớn nhất của $LL^{\mathsf T}$ có đơn không, rồi so giới hạn của HITS khi khởi tạo $h^0=\mathbf 1$ và khi khởi tạo bằng 1 trên bản sao thứ nhất, $1/2$ trên bản sao thứ hai.
:::

::: hint
Câu (b): trong TrustRank, phần dịch chuyển chỉ đi vào $T$. Câu (c): khi $T=V$, $v_T=u$. Câu (e): $LL^{\mathsf T}$ có dạng khối, mỗi khối là $LL^{\mathsf T}$ của G4; dùng Bổ đề 04.21.
:::

::: solution
**Câu (a).** Theo Mệnh đề 04.7(a) và bảng chi phí của Thuật toán 04.3, tiền tính tốn $16\cdot86\cdot(3n+\ell)=16\cdot86\cdot1{,}3\cdot10^{10}\approx1{,}79\cdot10^{13}$ thao tác. Theo Mệnh đề 04.23 và bảng chi phí của Thuật toán 04.19, HITS tốn $86\cdot(8n+2\ell)=86\cdot2{,}8\cdot10^{10}\approx2{,}41\cdot10^{12}$ thao tác, ít hơn khoảng $7{,}4$ lần. Phép so bỏ qua số vòng thực chạy, khác nhau giữa hai phép lặp ($2\beta^t$ của Định lý 04.5 so với $(\lambda_i/\lambda_1)^t$ của Định lý 04.22); tiêu chí dừng khác nhau ($\lVert\cdot\rVert_1$ và $\lVert\cdot\rVert_\infty$); việc HITS chạy theo truy vấn trên đồ thị con, mỗi truy vấn một lần, còn tiền tính chạy một lần cho mọi truy vấn; và việc chuẩn bị tập chủ đề.

**Câu (b).** Phân phối $v_T$ bằng 0 trên cụm, nên mọi trang của cụm không nhận phần dịch chuyển; đồ thị không có nút cụt nên không có phần bù. Bước 2 và Bước 3 của chứng minh Mệnh đề 04.10 cho
$$
p=\frac{\beta y}m,\qquad y=x_\rho+\beta mp ,
$$
nên $y=x_\rho/(1-\beta^2)$. Các số hạng $b$ ở trang đích và $\beta mb$ từ trang hỗ trợ mất: cụm chỉ khuếch đại phần TrustRank đã tới trang đích qua liên kết từ ngoài, và số trang hỗ trợ $m$ không còn đóng góp.

**Câu (c).** Khi $T=V$, $v_T=u$, nên TrustRank và PageRank là điểm cố định của cùng ánh xạ $F_u$ với cùng $\beta$ và cùng quy tắc bù. Theo Định lý 04.5(b), điểm cố định đó duy nhất, nên $\rho=r$. Mọi trang nhận ít nhất phần dịch chuyển $(1-\beta)/n>0$, nên $r_i>0$ và $s_i=1-\rho_i/r_i=0$ với mọi $i$.

**Câu (d).** Uy tín thô là số cạnh vào: A, B, C, D mỗi trang 2; $\mathrm Y$ có 3, từ C, $\mathrm P_1$, $\mathrm P_2$; $\mathrm P_1$, $\mathrm P_2$ mỗi trang 1. Chia cho 3: $a^1=(2/3,2/3,2/3,2/3,1,1/3,1/3)$. Trang đích $\mathrm Y$ có điểm uy tín lớn nhất, như trong PageRank (Ví dụ 04.6): các cạnh từ trang hỗ trợ về trang đích cũng nâng điểm uy tín của nó.

**Câu (e).** Theo thứ tự các trang của bản sao thứ nhất rồi bản sao thứ hai, $LL^{\mathsf T}$ có hai khối đường chéo, mỗi khối là $LL^{\mathsf T}$ của G4. Vì vậy trị riêng lớn nhất $\lambda_1$ của $LL^{\mathsf T}$ của G4 là trị riêng bội hai của ma trận này, và giả thiết của Định lý 04.22 không thỏa. Theo Bổ đề 04.21, $h^t=N\big((LL^{\mathsf T})^th^0\big)$, và $(LL^{\mathsf T})^t$ tác động riêng trên từng khối. Với $h^0=\mathbf 1$, hai khối nhận cùng véc-tơ ở mọi vòng, nên giới hạn là giới hạn của HITS trên G4 lặp lại ở hai bản sao. Với khởi tạo $1/2$ trên bản sao thứ hai, khối thứ hai luôn bằng một nửa khối thứ nhất, nên giới hạn trên bản sao thứ hai bằng một nửa: giới hạn phụ thuộc $h^0$.

**Kiểm tra lại.** Ở câu (a), tỷ số $16\cdot13/28\approx7{,}43$. Ở câu (b), cho $x_\rho=x$ và thêm lại $b$, $\beta mb$ thì được đúng Mệnh đề 04.10(c). Ở câu (d), tổng uy tín thô $4\cdot2+3+1+1=13$ bằng số cạnh của đồ thị bảy trang, vì mỗi cạnh góp $h^0_i=1$.
:::

Ba phép lặp và một chỉ số của chương dùng chung mô hình chi phí và khác nhau ở thông tin đầu vào, đầu ra và giả thiết: PageRank theo chủ đề và TrustRank đổi phân phối dịch chuyển của cùng một phép lặp, khối lượng rác so hai phép lặp, còn HITS đổi đầu ra thành hai vai trò.

<!-- note-topic-id: lec-04-topic-16 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 04.1 (Tiền tính 16 véc-tơ chủ đề cho một tỷ người dùng)
**Bài toán và dữ liệu.** Máy tìm kiếm phục vụ $10^9$ người dùng (MMDS, §5.3.1) trên $n=10^9$ trang với $\ell\approx10^{10}$ cạnh (Tình huống 03.1); mỗi điểm 8 byte. Chủ đề là 16 hạng mục cấp cao nhất của DMOZ (MMDS, Ví dụ 5.9). Cần thứ hạng theo mức quan tâm của từng người dùng tới 16 chủ đề, với sai số $\varepsilon=10^{-8}$ theo $\lVert\cdot\rVert_1$ cho mỗi véc-tơ.

**Mô hình hóa.** Chủ đề $\theta$ có phân phối dịch chuyển $v^{(\theta)}$ đều trên các trang được phân loại vào chủ đề đó; véc-tơ $r^{(\theta)}$ là PageRank theo chủ đề (Định nghĩa 04.1), tính bằng Thuật toán 04.3. Người dùng lưu trọng số $w_\theta$; điểm của trang ứng viên $i$ là $q_i=\sum_\theta w_\theta r^{(\theta)}_i$.

**Kiểm giả thiết.** Mọi chủ đề dùng cùng đồ thị, cùng $\beta=0{,}8$ và cùng quy tắc bù nút cụt theo $u$, nên Mệnh đề 04.6 áp dụng được: $q$ là PageRank với phân phối dịch chuyển $\sum_\theta w_\theta v^{(\theta)}$. Mỗi $v^{(\theta)}$ được chọn trước khi lặp và không đổi, và $0<\beta<1$, nên Định lý 04.5 áp dụng được dù web có nút cụt.

**Áp dụng và chi phí.**

- Dung lượng: theo Ví dụ 04.1 với $k=16$, các véc-tơ chủ đề và các trọng số cần tổng $2\cdot1{,}28\cdot10^{11}$ byte.
- Số vòng: Định lý 04.5(c) cho $\lVert r^t-r^{(\theta)}\rVert_1\le2(0{,}8)^t$, và $2(0{,}8)^{86}\le10^{-8}$, nên 86 vòng đủ cho mọi chủ đề (Ví dụ 03.13); dùng ngưỡng $\tau=\varepsilon/4=2{,}5\cdot10^{-9}$ của Định lý 04.5(d), một chủ đề có thể dừng sớm hơn.
- Tiền tính: theo Mệnh đề 04.7(a), không quá $16\cdot86\cdot(3n+\ell)=16\cdot86\cdot1{,}3\cdot10^{10}\approx1{,}79\cdot10^{13}$ thao tác; mỗi vòng là một công việc MapReduce theo khối (Thuật toán 03.22), nên tổng không quá $16\cdot86=1376$ công việc.
- Truy vấn: theo Mệnh đề 04.7(c), $c(2k-1)=31c$ thao tác cho $c$ trang ứng viên, không phụ thuộc $n$.
- Sai số ghép: theo Mệnh đề 04.6(b), nếu mỗi véc-tơ chủ đề có sai số không quá $10^{-8}$ thì véc-tơ ghép cũng vậy.

**Diễn giải.** Tiền tính chạy một lần cho mọi người dùng, trong không quá 1376 công việc MapReduce; mỗi truy vấn chỉ đọc $16$ điểm đã lưu cho mỗi ứng viên.

**Giới hạn.** Sở thích ngoài 16 chủ đề không biểu diễn được: MMDS ghi cách này mất một phần độ chính xác so với một véc-tơ riêng mỗi người (§5.3.1, tr.196). Việc xác định $w_\theta$ cho một truy vấn và tìm tập ứng viên $C$ không nằm trong phép đếm.

**Dẫn ngược lý thuyết.** Định nghĩa 04.1; Thuật toán 04.3; Định lý 04.5(c), (d); Mệnh đề 04.6, 04.7; Ví dụ 04.1.
:::

::: application Tình huống 04.2 (Phát hiện trang đích bằng khối lượng rác)
**Bài toán và dữ liệu.** Đồ thị bảy trang của Ví dụ 04.6: G4 với thêm cạnh $\mathrm C\to\mathrm Y$, và cụm gồm trang đích $\mathrm Y$ với hai trang hỗ trợ $\mathrm P_1$, $\mathrm P_2$; $\beta=4/5$. PageRank là
$$
\begin{aligned}
r=\Big(&\frac3{29},\frac{19}{203},\frac{19}{203},\frac{19}{203},\\
&\frac9{29},\frac{31}{203},\frac{31}{203}\Big):
\end{aligned}
$$
$\mathrm Y$ đứng đầu. Máy tìm kiếm không biết cụm ở đâu; nó biết B và D là hai trang tin cậy.

**Mô hình hóa.** Tập tin cậy $T=\{\mathrm B,\mathrm D\}$, TrustRank $\rho$ (Định nghĩa 04.13), khối lượng rác $s_i$ (Định nghĩa 04.14).

**Kiểm giả thiết.** B trỏ tới A, D; D trỏ tới B, C: không trang nào của $T$ trỏ tới cụm, nên giả thiết cách ly gần đúng thỏa. $r$ và $\rho$ cùng đồ thị, cùng $\beta=4/5$, đồ thị không có nút cụt, và $r_i>0$ với mọi $i$.

**Áp dụng.** Thuật toán 04.3 với $v_T=(0,1/2,0,1/2,0,0,0)$ hội tụ tới nghiệm của hệ bảy phương trình. Hệ giải như Ví dụ 04.6: phần G4 có B và D đối xứng, hàng C bằng hàng B trừ phần dịch chuyển $\tfrac1{10}$; cụm không nhận phần dịch chuyển, nên theo Bước 2–3 của chứng minh Mệnh đề 04.10, với phần dịch chuyển bằng 0 trên cụm (Bài tập 04.7(b)), $\rho_{\mathrm Y}=x_\rho/(1-\beta^2)$ với $x_\rho=\tfrac25\rho_{\mathrm C}$, và $\rho_{\mathrm P_k}=\tfrac25\rho_{\mathrm Y}$. Kết quả là
$$
\begin{aligned}
\rho=\Big(&\frac{21}{145},\frac{67}{290},\frac{19}{145},\frac{67}{290},\\
&\frac{38}{261},\frac{76}{1305},\frac{76}{1305}\Big),
\end{aligned}
$$
và khối lượng rác
$$
\begin{aligned}
s&=\Big(-\frac25,-\frac{279}{190},\\
&\quad-\frac25,-\frac{279}{190},\\
&\quad\frac{43}{81},\frac{863}{1395},\frac{863}{1395}\Big)\\
&\approx(-0{,}40;\,-1{,}47;\,-0{,}40;\\
&\quad-1{,}47;\,0{,}53;\,0{,}62;\,0{,}62).
\end{aligned}
$$
Chẳng hạn, $s_{\mathrm Y}=1-\dfrac{38/261}{9/29}=1-\dfrac{38}{81}=\dfrac{43}{81}$. Chi phí là hai phép lặp, 7 phép chia và 7 phép trừ (Nhận xét 04.16).

**Diễn giải.** Ba trang của cụm là ba trang duy nhất có khối lượng rác dương, và chúng đứng đầu thứ tự rà soát; bốn trang của G4 có khối lượng rác âm. TrustRank chỉ tới được cụm qua cạnh $\mathrm C\to\mathrm Y$. Theo Mệnh đề 04.10, một phần PageRank của $\mathrm Y$ đến từ phần dịch chuyển đều vào $\mathrm P_1$, $\mathrm P_2$ và $\mathrm Y$; khi phần dịch chuyển chỉ vào $T$, phần này mất, và $\mathrm Y$ giữ lại $\rho_{\mathrm Y}/r_{\mathrm Y}=38/81\approx47\%$ điểm của mình.

**Giới hạn.** $0{,}53$ và $0{,}62$ không gần 1, nên theo cách đọc của MMDS không đủ để kết luận ba trang của cụm là rác; chúng là ba giá trị lớn nhất nên đứng đầu thứ tự rà soát. C chỉ cách D một cạnh, nên một phần TrustRank vẫn chảy vào cụm.

**Kiểm tra lại.** $\sum_ir_is_i=\sum_i(r_i-\rho_i)=0$: hai véc-tơ cùng có tổng 1, và tổng $\rho$ là $\tfrac{378+603+342+603+380+152+152}{2610}=1$.

**Dẫn ngược lý thuyết.** Định nghĩa 04.9, 04.13, 04.14; Mệnh đề 04.10; Thuật toán 04.3; Định lý 04.5; Ví dụ 04.6.
:::

![Đồ thị bảy trang, β = 4/5. B và D có viền đôi màu xanh lục và nhãn T: tập tin cậy T = {B, D}. Cạnh từ C tới trang đích Y vẽ nét đứt màu cam, đậm, nhãn liên kết bình luận. Nhãn mỗi trang ghi khối lượng rác s khi PageRank nền và TrustRank cùng β: A và C mỗi trang −0,40; B và D mỗi trang −1,47; Y 0,53; P1 và P2 mỗi trang 0,62.](img/lec-04/note-g4-cum-tin-cay.svg)

Hình ghi khối lượng rác của Tình huống 04.2 cạnh từng trang. Cạnh $\mathrm C\to\mathrm Y$ vẽ nét đứt vì đó là liên kết người tạo cụm đặt vào mục bình luận của C; Tình huống 04.3 xét điều gì xảy ra nếu C được đưa vào tập tin cậy.

::: application Tình huống 04.3 (Tập tin cậy chứa trang cho phép bình luận)
**Bài toán và dữ liệu.** Cùng đồ thị bảy trang và $\beta=4/5$. C là một trang có nội dung đáng tin, nhưng cho phép người đọc đăng bình luận có liên kết, và liên kết $\mathrm C\to\mathrm Y$ là một bình luận như vậy. Người đánh giá xem nội dung của C và đưa C vào tập tin cậy.

**Giả thiết bị vi phạm.** Định nghĩa 04.13 giả thiết các trang của $T$ hiếm khi trỏ tới trang rác; MMDS ghi rằng trang cho phép người khác đặt liên kết không được coi là tin cậy, kể cả khi nội dung của nó đáng tin (§5.4.4, tr.202). C trỏ trực tiếp tới trang đích.

**Hậu quả.**

- Với $T=\{\mathrm B,\mathrm C,\mathrm D\}$: $\rho_{\mathrm Y}=50/261$, nên $s_{\mathrm Y}=1-\tfrac{50/261}{9/29}=\tfrac{31}{81}\approx0{,}38$, và hai trang hỗ trợ có $s=139/279\approx0{,}50$; so với Tình huống 04.2, khối lượng rác của trang đích giảm từ $0{,}53$ xuống $0{,}38$.
- Với $T=\{\mathrm C\}$: $s_{\mathrm Y}=7/81\approx0{,}09$, gần 0, nên theo cách đọc của MMDS trang đích "có lẽ không phải rác"; hai trang hỗ trợ có $s\approx0{,}26$, còn B và D, hai trang không thuộc cụm, có $s=39/95\approx0{,}41$. Thứ tự rà soát đặt B và D trước cả ba trang của cụm.

Hai tập tin cậy giải như Tình huống 04.2. Với $T=\{\mathrm B,\mathrm C,\mathrm D\}$, $\rho_{\mathrm C}=5/29$, nên $\rho_{\mathrm Y}=\tfrac25\cdot\tfrac5{29}\cdot\tfrac{25}9=\tfrac{50}{261}$. Phần dịch chuyển vào C đi thẳng qua liên kết bình luận vào trang đích, rồi được cụm khuếch đại theo Bước 2–3 của chứng minh Mệnh đề 04.10, với phần dịch chuyển bằng 0 trên cụm (Bài tập 04.7(b)): $\rho_{\mathrm Y}=x_\rho/(1-\beta^2)$, với $x_\rho$ lớn hơn.

**Cách sửa.** Loại các trang cho phép người khác đặt liên kết khỏi $T$, như MMDS chỉ ra; với $T=\{\mathrm B,\mathrm D\}$, kết quả trở về Tình huống 04.2, nơi ba trang của cụm đứng đầu thứ tự rà soát.

**Giới hạn.** Một trang tin cậy vẫn có thể trỏ tới trang rác qua đường đi dài; giả thiết cách ly là gần đúng, nên khối lượng rác chỉ đánh dấu trang cần rà soát.

**Dẫn ngược lý thuyết.** Định nghĩa 04.9, 04.13, 04.14; Mệnh đề 04.10; Nhận xét 04.16.
:::

**Ứng dụng trong các bài sau của học phần.**

- MMDS dùng độ tương đồng Jaccard (Định nghĩa 01.9) để xếp một trang vào chủ đề có tập từ đặc trưng gần nhất, một cách suy ra trọng số $w_\theta$ từ các trang người dùng vừa xem (§5.3.4, tr.198–199). Bài 05 biểu diễn tài liệu thành tập và ước lượng Jaccard bằng chữ ký MinHash.
- Mệnh đề 04.7(c) giả thiết tập trang ứng viên $C$ của truy vấn đã có. Máy tìm kiếm lấy tập này từ chỉ mục ngược (inverted index), như mục Ứng dụng của Bài 03 đã nêu; Bài 14 trình bày chỉ mục ngược.

<!-- note-topic-id: lec-04-topic-17 -->
## Tóm tắt chương

Câu hỏi xuất phát của chương là xếp hạng $10^9$ trang theo ngữ cảnh của từng người dùng, khó thao túng bằng liên kết và tách được hai vai trò của một trang, khi một véc-tơ PageRank cho mỗi người dùng đã cần $8\cdot10^{18}$ byte (Ví dụ 04.1). Thay phân phối đều của bước dịch chuyển bằng một phân phối $v$ bất kỳ, giữ phần bù nút cụt theo $u$, cho PageRank theo chủ đề với cùng thuật toán và mọi bảo đảm của Bài 03 (Định nghĩa 04.1, Thuật toán 04.3, Mệnh đề 04.4, Định lý 04.5). Vì nghiệm tuyến tính theo $v$, $k$ véc-tơ chủ đề tính trước ghép được thành nghiệm của mọi tổ hợp trọng số với chi phí $\Theta(kc)$ mỗi truy vấn, và với 16 chủ đề, các véc-tơ chủ đề cùng trọng số của mọi người dùng cần $2{,}56\cdot10^{11}$ byte thay cho $8\cdot10^{18}$ byte (Mệnh đề 04.6, 04.7; Tình huống 04.1). Một cụm thao túng gồm trang đích và $m$ trang hỗ trợ nhân đóng góp từ ngoài với hệ số $1/(1-\beta^2)$, bằng $400/111\approx3{,}6$ khi $\beta=0{,}85$ (Định nghĩa 04.9, Mệnh đề 04.10, Hệ quả 04.11). TrustRank là PageRank theo chủ đề với tập tin cậy, và khối lượng rác đánh dấu trang có TrustRank nhỏ so với PageRank của chính nó (Định nghĩa 04.13, 04.14); khi tập tin cậy chứa trang cho phép bình luận, khối lượng rác của trang đích giảm, và khi tập tin cậy chỉ gồm trang đó, hai trang ngoài cụm đứng trước cả ba trang của cụm (Tình huống 04.2, 04.3). HITS gán mỗi trang điểm trung tâm và điểm uy tín bằng hai lượt cạnh mỗi vòng, và là phép lặp lũy thừa trên $LL^{\mathsf T}$ nên hội tụ tới véc-tơ riêng của trị riêng lớn nhất khi trị riêng đó đơn (Định nghĩa 04.17, Thuật toán 04.19, Mệnh đề 04.20, Bổ đề 04.21, Định lý 04.22). Giới hạn còn lại: PageRank theo chủ đề và TrustRank cần thông tin bên ngoài đồ thị (tập chủ đề, trọng số, tập tin cậy), HITS chạy theo truy vấn cần đồ thị con của truy vấn, và mọi công cụ cần tập trang ứng viên; Bài 05 ước lượng độ tương đồng Jaccard (Định nghĩa 01.9), mà MMDS dùng để suy ra chủ đề, bằng chữ ký MinHash, và Bài 14 cho chỉ mục ngược tạo ra tập ứng viên.

**Định nghĩa và kết quả theo mục.**

- Mục 1: một véc-tơ cho mỗi người dùng (Ví dụ 04.1).
- Mục 2: phân phối dịch chuyển và PageRank theo chủ đề (Định nghĩa 04.1, Nhận xét 04.2); thuật toán, tính đúng và bảo toàn (Thuật toán 04.3, Mệnh đề 04.4); hội tụ và cận sai số (Định lý 04.5); tuyến tính theo phân phối dịch chuyển (Mệnh đề 04.6); chi phí tiền tính và truy vấn (Mệnh đề 04.7, Nhận xét 04.8).
- Mục 3: liên kết rác và cụm thao túng (Định nghĩa 04.9); điểm trang hỗ trợ và trang đích (Mệnh đề 04.10); hệ số khuếch đại (Hệ quả 04.11); hai hướng chống liên kết rác (Nhận xét 04.12).
- Mục 4: tập tin cậy và TrustRank (Định nghĩa 04.13); khối lượng rác (Định nghĩa 04.14); điều kiện cùng mô hình nền (Nhận xét 04.15); chi phí và tập tin cậy trong thực hành (Nhận xét 04.16).
- Mục 5: ma trận kề, chuẩn hóa và phép cập nhật HITS (Định nghĩa 04.17, Nhận xét 04.18); thuật toán HITS và tính xác định của chuẩn hóa (Thuật toán 04.19, Mệnh đề 04.20); hướng của $h^t$ và giới hạn (Bổ đề 04.21, Định lý 04.22); chi phí (Mệnh đề 04.23, Nhận xét 04.24).
- Đọc thêm: phép lặp lũy thừa với khoảng cách trị riêng (Định lý 04.25, Ví dụ 04.14).
- Mục 6: bảng so sánh ba phép lặp và một chỉ số dẫn xuất.

**Công thức và thuật toán cần nhớ.**

$$
\begin{aligned}
F_v(r)&=\beta M_0r+\beta\delta\,u+(1-\beta)v\\
&=\beta\bar Mr+(1-\beta)v .
\end{aligned}
$$

$$
\begin{gathered}
\lVert r^{t+1}-r^*_v\rVert_1\le\frac{\beta}{1-\beta}\Delta_t,\\
r^*_{\sum_\theta w_\theta v^{(\theta)}}=\sum_\theta w_\theta r^{(\theta)} .
\end{gathered}
$$

$$
\begin{gathered}
p=\frac{\beta y}m+b,\qquad b=\frac{1-\beta}n,\\
y=\frac{x+\beta mb+b}{1-\beta^2} .
\end{gathered}
$$

$$
\begin{gathered}
y\approx\frac{x}{1-\beta^2}+\frac{\beta}{1+\beta}\cdot\frac mn,\\
s_i=1-\frac{\rho_i}{r_i}.
\end{gathered}
$$

$$
\begin{gathered}
a^{t+1}=N(L^{\mathsf T}h^t),\\
h^{t+1}=N(La^{t+1}),\\
LL^{\mathsf T}h^*=\lambda_1h^* .
\end{gathered}
$$

Một vòng PageRank theo chủ đề đặt $\beta\delta/n+(1-\beta)v_i$ cho mỗi trang rồi cộng $\beta r_j/d_j$ qua mỗi cạnh, chỉ đọc véc-tơ cũ: $3n+\ell$ thao tác. Một vòng HITS cộng $h_i$ vào $\tilde a_j$ qua mỗi cạnh, chuẩn hóa, rồi cộng $a_j$ mới vào $\tilde h_i$ qua mỗi cạnh và chuẩn hóa: $8n+2\ell$ thao tác.

**Giả thiết hay bị bỏ quên.**

- Phần bù nút cụt chia theo $u$, không theo $v$; chia theo $v$ làm mất tính tuyến tính khi ghép chủ đề.
- $v$ là phân phối: quên chia cho $\lvert S\rvert$ làm tổng điểm bằng $\lvert S\rvert$.
- Ghép chủ đề cần cùng đồ thị, cùng $\beta$ và cùng quy tắc bù cho mọi chủ đề.
- $x$ đã nhân $\beta$ và chia bậc ra; phương trình trang đích có cả phần dịch chuyển $b$.
- Công thức trang đích đúng cho đúng kiến trúc của Định nghĩa 04.9 trên đồ thị không có nút cụt.
- $r$ và $\rho$ của khối lượng rác phải cùng mô hình, cùng $\beta$; khối lượng rác không phải xác suất và có thể âm.
- Tập tin cậy không chứa trang cho phép người khác đặt liên kết.
- HITS không chia điểm theo bậc ra; bước trung tâm dùng điểm uy tín vừa cập nhật.
- Giới hạn duy nhất của HITS cần trị riêng lớn nhất của $LL^{\mathsf T}$ đơn; $\Delta$ nhỏ không phải cận sai số của HITS.

## Bài tập củng cố

Bài tập 04.8–04.14 nằm trong [tệp bài tập Bài 04](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-pagerank-theo-chu-de-lien-ket-rac-va-hits.html), cùng gợi ý và lời giải.

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press. Chương 5: §5.3.1, tr.195–196, Ví dụ 5.9: Mục 1, Ví dụ 04.1, Nhận xét 04.8, Tình huống 04.1; §5.3.2, tr.196–197, Ví dụ 5.10, Hình 5.15: Mục 2.1, Ví dụ 04.2, 04.3, Nhận xét 04.2; §5.3.3–5.3.4, tr.197–199: Mục 2.5, Nhận xét 04.8, mục Ứng dụng; §5.4–5.4.2, tr.199–201, Hình 5.16, Ví dụ 5.11: Mục 3; §5.4.3, tr.202: Nhận xét 04.12; §5.4.4, tr.202–203: Mục 4.1, Nhận xét 04.16, Tình huống 04.3; §5.4.5, tr.203, Ví dụ 5.12, Hình 5.17: Mục 4.2, Nhận xét 04.15; §5.5–5.5.2, tr.204–208, Ví dụ 5.13–5.15, Hình 5.18–5.20: Mục 5; §5.1.2, Hình 5.1, tr.178: đồ thị G4. Bài 5.3.1, 5.4.1, 5.4.2, 5.5.1, 5.5.2: tệp bài tập. Sách và trang chiếu của các tác giả: http://www.mmds.org.
- Leskovec, J., Rajaraman, A. và Ullman, J. D. Trang chiếu Chương 5 *Link Analysis*, phần hai, của sách MMDS, bản trên http://www.mmds.org (không ghi năm). Tr.7–11: Mục 2; tr.31–35: Mục 3, Nhận xét 04.12; tr.38–45: Mục 4, Định nghĩa 04.13 (tập hạt giống, tập tin cậy, giả thiết cách ly gần đúng, tr.38–39) và ngưỡng TrustRank (tr.39); tr.47–60: Mục 5.
- Leskovec, J. và Kanatsoulis, C. (2026). Stanford CS246, *Mining Massive Datasets*, bài 10-spam. Trang chiếu 5–14: Mục 2; 51–55: Mục 3, Nhận xét 04.12; 58–65: Mục 4.
- Blum, A., Hopcroft, J. và Kannan, R., *Foundations of Data Science*, bản ngày 04/01/2018. §3.7, tr.51–53, Định lý 3.11: chứng minh Định lý 04.22 và Định lý 04.25; §3.9.4, tr.62: HITS là phép lặp lũy thừa, Mục 5.3.
- Ghi chú Bài 01: Định nghĩa 01.9, 01.13. Ghi chú Bài 03: Định nghĩa 03.1, 03.3, 03.5, 03.7, 03.8, 03.19; Mệnh đề 03.9, 03.11, 03.13; Thuật toán 03.10, 03.22; Bổ đề 03.14; Định lý 03.15; Hệ quả 03.16; Nhận xét 03.18; Ví dụ 03.1, 03.2, 03.5, 03.6, 03.10, 03.13; Tình huống 03.1.
- Mã minh họa `materials/lec-04/code/link_analysis.py` và `materials/lec-04/code/practice-README.md`: PageRank theo chủ đề, TrustRank và HITS trên G4, G5. Lệnh `trust` tính khối lượng rác với PageRank nền $\beta=1$, không theo điều kiện cùng $\beta$ của Định nghĩa 04.14.
