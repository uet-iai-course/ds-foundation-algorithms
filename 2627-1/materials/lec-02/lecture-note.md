# Bài 02 — Mô hình tính toán MapReduce

Kho dữ liệu web lớn hơn bộ nhớ và đĩa của một máy, nên phải được lưu và xử lý trên nhiều máy. MapReduce là mô hình tính toán cho việc đó: người lập trình viết hai hàm Map và Reduce, còn hệ thống chia đầu vào, nhóm các cặp trung gian theo khóa và chạy lại các tác vụ trên máy hỏng. Chúng ta chứng minh mô hình trả đúng kết quả, áp nó cho đếm từ và ba bài toán gộp khác, đo chi phí khi thêm máy và chạy lại bài đếm từ trên một cụm Hadoop.

[Bộ trang chiếu Bài 02](lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) trình bày cùng chủ đề; [tệp bài tập Bài 02](material-viewer.html?doc=materials/lec-02/exercises.md&deck=lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đặc tả hàm Map, hàm Reduce, hàm phân phối và phép nhóm theo khóa; chạy tay một công việc đếm từ và chứng minh một công việc trả đúng một kết quả Reduce cho mỗi khóa (Mục 1, Mục 2).
2. Phát biểu điều kiện để hàm Combine giữ nguyên kết quả, chứng minh điều kiện đó bằng tính kết hợp và giao hoán, và chỉ ra phản ví dụ trung bình trực tiếp (Mục 1.2, Mục 2.4, Mục 3.3).
3. Chọn khóa và giá trị trung gian cho nhân ma trận–véc-tơ, đếm từ phân biệt và trung bình cộng; chứng minh tính đúng của từng thiết kế (Mục 3).
4. Tính tổng khối lượng tính toán, thời gian từng pha và cả công việc, chi phí truyền thông $C=I+H$, thời gian truyền và mức tăng tốc; nêu quan hệ giữa quy ước $I+H$ của sách MMDS và quy ước $I+2H+O$ của trang chiếu MMDS và CS246 (Mục 4).
5. (Đọc thêm.) Xác định phần phải chạy lại khi máy chạy Map, máy chạy Reduce hoặc tiến trình điều phối hỏng, giải thích vì sao chạy lại không làm một đóng góp bị tính hai lần, và tính kỳ vọng thời gian thực thi khi tác vụ hỏng.
6. Chạy đếm từ trên cụm Hadoop và đối chiếu kết quả, bộ đếm bản ghi với phép tính tay (Mục 5).

## Kiến thức tiên quyết

Số hiệu `01.k` chỉ ghi chú Bài 01; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Bài toán dữ liệu** (Định nghĩa 01.1). Một bài toán dữ liệu gồm miền đầu vào, quan hệ đầu vào–đầu ra và ngân sách tài nguyên; thuật toán đúng khi trên mọi đầu vào hợp lệ nó dừng và trả một đầu ra được chấp nhận.
- **Khối và lượt quét** (Định nghĩa 01.4, Mệnh đề 01.5). Đĩa trao đổi dữ liệu theo khối; một lượt quét tệp $F$ khối đọc mỗi khối đúng một lần và tốn $F$ lần truyền khối.
- **Hàm băm** (Định nghĩa 01.8). Hàm băm đưa mỗi khóa về một số thùng, các thùng đánh số từ 0; mọi bản ghi cùng khóa nằm trong cùng một thùng.
- **Mô hình chi phí** (Định nghĩa 01.13). Khối lượng tính toán, bộ nhớ làm việc, đọc ghi và dữ liệu mạng là các đại lượng riêng, mỗi đại lượng có đơn vị riêng; số của hai đại lượng không cộng được với nhau khi chưa đổi về cùng một đơn vị hay một mục tiêu chung.
- **Nhiều máy và máy hỏng** (Nhận xét 01.3). Trung bình một máy chủ hỏng sau khoảng 1000 ngày, nên với một triệu máy, mỗi ngày hỏng khoảng 1000 máy; trong bài toán đếm từ, một tác vụ chạy lại sau khi máy hỏng không được làm mất hay đếm trùng đóng góp nào.
- **Chi phí truyền thông theo CS246** (Bài 01, đoạn "Trong thực hành" sau Mệnh đề 01.15). Với một công việc MapReduce, chi phí truyền thông là kích thước tệp đầu vào, cộng hai lần tổng kích thước các tệp chuyển từ tác vụ Map sang tác vụ Reduce, cộng kích thước đầu ra của tác vụ Reduce.
- **Bất biến vòng lặp và quy nạp** (CLRS 4e, §2.1; Mệnh đề 01.12). Một mệnh đề đúng trước vòng đầu, được giữ qua mỗi vòng và khi vòng lặp dừng cho điều cần chứng minh.
- **Đại số tuyến tính và xác suất cơ bản.** Tích ma trận–véc-tơ $y_i=\sum_j a_{ij}v_j$; kỳ vọng của một tổng bằng tổng các kỳ vọng.

## Bảng ký hiệu

Các ký hiệu dưới đây dùng xuyên suốt chương; chữ chỉ dùng trong một ví dụ, một chứng minh hay một bài tập được giới thiệu tại chỗ. Mỗi chữ trong bảng giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $n$ | số bản ghi đầu vào của bài toán đang xét (văn bản hoặc số) | số nguyên, $n\ge0$ |
| $d_i$; $\ell_i$ | văn bản thứ $i$; số từ của $d_i$, tính cả từ lặp | dãy từ; số nguyên $\ge0$ |
| $w$; $c_i(w)$; $c(w)$ | một từ; số lần $w$ xuất hiện trong $d_i$; trong cả kho | từ; số nguyên $\ge0$ |
| $\mathcal W$; $\mathcal W_i$; $D$ | tập từ xuất hiện trong kho; tập từ của $d_i$; số từ phân biệt $D=\lvert\mathcal W\rvert$ | tập hữu hạn; số nguyên $\ge0$ |
| $K_1,V_1$; $K_2,V_2$; $K_3,V_3$ | miền khóa và miền giá trị của đầu vào; của cặp trung gian; của đầu ra | tập |
| $(k,x)$ | một cặp khóa–giá trị | $K\times V$ |
| $\Omega^*$ | tập các dãy hữu hạn trên tập $\Omega$, gồm dãy rỗng, giữ phần tử lặp | tập dãy |
| $X$; $X_1,\ldots,X_m$ | dãy cặp đầu vào; các phần đầu vào | dãy trên $K_1\times V_1$ |
| $m$; $r$ | số tác vụ Map; số tác vụ Reduce | số nguyên $\ge1$ |
| $Z$ | dãy cặp trung gian do mọi lần gọi Map phát | dãy trên $K_2\times V_2$ |
| $h$ | hàm phân phối | $K_2\to\{0,\ldots,r-1\}$ |
| $L_k$ | danh sách giá trị đi cùng khóa $k$ | dãy trên $V_2$ |
| $Y$ | dãy cặp đầu ra | dãy trên $K_3\times V_3$ |
| $\oplus$; $E$ | phép gộp kết hợp, giao hoán; miền của nó | $\oplus:E\times E\to E$ |
| $A=(a_{ij})$; $q$ | ma trận vuông; cấp của ma trận | $\mathbb R^{q\times q}$; $q\ge1$ |
| $v$; $y$ | véc-tơ đầu vào; véc-tơ kết quả $y=Av$ | $\mathbb R^q$ |
| $g$ | khóa chung cố định | một nhãn |
| $a_1,\ldots,a_n$; $\mu$ | dãy số; trung bình cộng | $\mathbb R$ |
| $(s,\kappa)$; $(s^\ast,\kappa^\ast)$ | trạng thái tổng–số lượng; trạng thái gộp cuối ở Reduce | $\mathbb R\times\mathbb N_{\ge1}$ |
| $P$; $u$; $t_u$ | số máy; chỉ số máy; tổng thời gian các tác vụ giao cho máy $u$ | số nguyên; giây |
| $\tau$; $W_P$ | thời gian một phép cộng; tổng khối lượng tính toán trên $P$ máy | giây, $\tau>0$; số phép toán |
| $T_{\text{pha}}$; $T_P$; $T_1$; $S_P$ | thời gian một pha; cả công việc trên $P$ máy; trên một máy; mức tăng tốc $T_1/T_P$ | giây; số thực dương |
| $I$; $H$; $C$; $O$ | tổng đầu vào các tác vụ Map; tổng đầu vào các tác vụ Reduce; chi phí truyền thông $C=I+H$; tổng đầu ra các tác vụ Reduce | byte, MB hoặc số bản ghi |
| $Q$; $B$; $\lambda$; $T_{\text{truyền}}$ | lượng dữ liệu qua một đường truyền; băng thông; độ trễ khởi đầu; thời gian truyền | MB; MB/s; giây; giây |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $2{,}5$; số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $10\,000$.
- 1 KB $=10^3$ byte, 1 MB $=10^6$ byte, 1 TB $=10^{12}$ byte, 1 MiB $=2^{20}$ byte.
- Tên đối tượng trong ví dụ viết chữ đứng, như máy $\mathrm A$, khối $\mathrm A$ hay a.vn, để không lẫn với biến; văn bản ví dụ viết trong ngoặc kép, như "mèo chó mèo", còn cặp khóa–giá trị viết (mèo, 1).
- "MapReduce" viết liền chỉ mô hình; "Map", "Reduce", "Combine" viết hoa chỉ hàm hoặc tác vụ cùng tên. Chữ "lượt" chỉ dùng cho lượt quét một tệp.
- MMDS viết ma trận $M$ với phần tử $m_{ij}$ và kết quả $x$; ở đây ma trận là $A$, phần tử $a_{ij}$, kết quả $y$, vì $m$ là số tác vụ Map và $x$ là giá trị của một cặp.
- Viết tắt nguồn: MMDS (*Mining of Massive Datasets*, ấn bản 3); "trang chiếu MMDS" chỉ bộ trang chiếu Chương 2 của các tác giả MMDS; CS246 (bài giảng mở đầu 01-intro của Stanford CS246); chi tiết ở mục tài liệu tham khảo.

<!-- note-topic-id: lec-02-topic-01 -->
## 1. Xử lý dữ liệu trên cụm máy

Bài 01 đã nêu bài toán đếm từ trên một kho tài liệu chia trên nhiều máy (Bài 01, Mục 1.2) cùng hai yêu cầu: máy hỏng là chuyện xảy ra hằng ngày, và một tác vụ chạy lại không được làm mất hay đếm trùng đóng góp nào (Nhận xét 01.3). Bài 01 cũng tách dữ liệu mạng khỏi khối lượng tính toán thành hai đại lượng chi phí riêng (Định nghĩa 01.13). Nhưng Bài 01 chưa cho cách viết một chương trình chạy trên nhiều máy mà vẫn trả đúng số đếm. Bài toán trung tâm của chương là đếm số lần xuất hiện của mỗi từ trong một kho web lớn hơn bộ nhớ, đĩa và băng thông đọc của một máy.

![Sơ đồ cấu trúc chương đọc từ trên xuống. Khối trên cùng là bài toán trung tâm: đếm từ trên kho web nằm ở nhiều máy, hơn 400 TB, một máy đọc 35 MB/s mất khoảng 132 ngày. Sáu mũi tên xuống sáu cột. Mục 1: cụm máy, hệ tệp phân tán; kết quả Bổ đề 02.2, gộp không phụ thuộc thứ tự. Mục 2: Map, nhóm theo khóa, Reduce; kết quả Mệnh đề 02.11 và 02.15. Mục 3: ba thiết kế khóa và giá trị; kết quả y = Av, D = 3, μ = s*/κ*. Mục 4: chi phí song song hóa; kết quả W_P = n − 1, thời gian pha là giá trị lớn nhất, C = I + H, S_P = T₁/T_P. Cột đọc thêm, viền nét đứt: thực thi và phục hồi; Mệnh đề 02.41 và 02.43. Mục 5: thực hành Hadoop; 5 cặp Map, 4 cặp sau Combine, 3 cặp Reduce.](img/lec-02/note-cau-truc-chuong-02.svg)

Sơ đồ đọc từ trên xuống. Khối trên cùng ghi bài toán trung tâm với số liệu của Ví dụ 02.1. Sáu cột ứng với Mục 1–4, phần đọc thêm về hệ thống thực thi và Mục 5; dưới đường kẻ đứt của mỗi cột là kết quả chính của phần đó. Cột đọc thêm có viền nét đứt.

### 1.1 Kho web trên một máy

Để thấy vì sao một máy không đủ, ta tính thời gian đọc kho web với số liệu của trang chiếu MMDS.

::: example Ví dụ 02.1 (Đọc kho web trên một máy)
**Dữ kiện.** Kho có hơn 20 tỷ trang web, mỗi trang khoảng 20 KB; một máy đọc đĩa với tốc độ 30–35 MB/s; lưu kho cần khoảng 1000 ổ đĩa (trang chiếu MMDS, tr.4).

**Dung lượng.** $2\times10^{10}\cdot2\times10^{4}=4\times10^{14}$ byte, tức 400 TB.

**Đọc trên một máy.** Với 35 MB/s,
$$
\begin{aligned}
\frac{4\times10^{14}}{3{,}5\times10^{7}}&\approx1{,}14\times10^{7}\ \text{giây}\\
&\approx132\ \text{ngày};
\end{aligned}
$$
với 30 MB/s, $4\times10^{14}/(3\times10^{7})\approx1{,}33\times10^{7}$ giây, khoảng 154 ngày. Trang chiếu MMDS làm tròn thành "khoảng 4 tháng".

**Đọc trên 1000 máy.** Giả sử mỗi ổ đĩa gắn với một máy và 1000 máy đọc đồng thời phần của mình. Mỗi máy đọc $4\times10^{11}$ byte, mất $4\times10^{11}/(3{,}5\times10^{7})\approx1{,}14\times10^{4}$ giây, khoảng $3{,}2$ giờ.

**Kiểm tra lại.** $1{,}143\times10^7/86\,400\approx132{,}3$; thời gian trên 1000 máy bằng đúng một phần nghìn thời gian trên một máy, vì mỗi máy đọc một phần nghìn kho với cùng tốc độ.
:::

Một lượt quét kho trên một máy mất hơn bốn tháng, nên kho phải nằm trên nhiều máy và các máy phải đọc đồng thời. Phép chia cho 1000 ở Ví dụ 02.1 chỉ đúng khi mỗi máy đọc phần nằm trên đĩa của chính nó, không gửi qua mạng tới một máy. Từ đó, một mô hình tính toán cho kho này phải đáp ứng bốn yêu cầu:

- dữ liệu nằm trên nhiều máy và mỗi phần được xử lý ở nơi lưu;
- các máy tính toán song song;
- tính toán được đưa tới gần dữ liệu để giảm lượng truyền qua mạng (CS246, trang chiếu 33);
- việc chia việc, lập lịch và chạy lại khi máy hỏng do hệ thống đảm nhiệm, không do người lập trình viết lại cho mỗi bài toán.

<!-- note-topic-id: lec-02-topic-02 -->
### 1.2 Gộp kết quả cục bộ

Yêu cầu thứ nhất buộc mỗi máy tính một kết quả cục bộ trên phần của nó, rồi các kết quả cục bộ được gộp lại. Phép tính đơn giản nhất có dạng đó là cộng một dãy số.

::: example Ví dụ 02.2 (Cộng sáu số trên ba máy)
**Dữ kiện.** Dãy $a_1,\ldots,a_6=2,4,9,1,3,5$ nằm trên ba máy:

- máy 1 giữ $a_1=2$, $a_4=1$;
- máy 2 giữ $a_2=4$, $a_5=3$;
- máy 3 giữ $a_3=9$, $a_6=5$.

**Tổng bộ phận.** Máy 1 tính $2+1=3$, máy 2 tính $4+3=7$, máy 3 tính $9+5=14$; ba máy tính đồng thời.

**Gộp.** $3+7+14=24$.

**Kiểm tra lại.** Cộng theo thứ tự chỉ số: $2+4+9+1+3+5=24$.
:::

![Ba khối trên là ba máy. Máy 1 giữ a₁ = 2 và a₄ = 1, tổng bộ phận 3; máy 2 giữ a₂ = 4 và a₅ = 3, tổng bộ phận 7; máy 3 giữ a₃ = 9 và a₆ = 5, tổng bộ phận 14. Ba mũi tên dẫn xuống khối gộp: 3 + 7 + 14 = 24, bằng a₁ + a₂ + ⋯ + a₆.](img/lec-02/note-cong-sau-so.svg)

Trên hình, mỗi số nằm ở đúng một máy và góp đúng một lần vào một tổng bộ phận; kết quả gộp vẫn bằng tổng theo thứ tự chỉ số. Một cách trực quan, cách tính cục bộ rồi gộp đúng vì phép cộng cho phép đổi thứ tự các số và đổi cách nhóm chúng.

::: definition Định nghĩa 02.1 (Phép gộp kết hợp, giao hoán)
Cho tập $E$ và phép toán $\oplus:E\times E\to E$.

- $\oplus$ **kết hợp** (associative) khi $(x\oplus y)\oplus z=x\oplus(y\oplus z)$ với mọi $x,y,z\in E$.
- $\oplus$ **giao hoán** (commutative) khi $x\oplus y=y\oplus x$ với mọi $x,y\in E$.
- Với một dãy hữu hạn khác rỗng $e_1,\ldots,e_\ell$ trên $E$, **phép gộp của dãy** được định nghĩa từ trái sang phải: $\bigoplus(e_1)=e_1$, và với $\ell\ge2$,
$$
\begin{aligned}
&\textstyle\bigoplus(e_1,\ldots,e_\ell)\\
&=\textstyle\bigoplus(e_1,\ldots,e_{\ell-1})\oplus e_\ell .
\end{aligned}
$$
:::

Phép toán $\oplus$ phải đóng trên $E$: kết quả gộp hai phần tử của $E$ lại là phần tử của $E$, nên có thể gộp tiếp. Phép cộng số nguyên, phép lấy giá trị lớn nhất trên số nguyên, phép cộng từng thành phần trên cặp số đều kết hợp và giao hoán.

Phép gộp của dãy chỉ được định nghĩa cho dãy khác rỗng; một máy không giữ phần tử nào thì không phát tổng bộ phận, thay vì phát một "phần tử rỗng" chưa có nghĩa trong $E$.

Hai phép toán sau thiếu lần lượt tính kết hợp và tính giao hoán.

- Phép trừ không kết hợp: $(5-3)-1=1$ còn $5-(3-1)=3$.
- Phép "lấy phần tử đầu" $x\oplus y=x$ kết hợp, vì cả hai vế bằng $x$, nhưng không giao hoán: $2\oplus4=2$ còn $4\oplus2=4$.

Kết quả sau là lý do để mọi cách chia dãy cho các máy cho cùng một kết quả gộp.

::: lemma Bổ đề 02.2 (Gộp không phụ thuộc thứ tự và cách nhóm)
**Giả thiết.** $\oplus:E\times E\to E$ kết hợp và giao hoán; $e_1,\ldots,e_\ell$ là dãy hữu hạn khác rỗng trên $E$.

**Kết luận.**

- (a) Với hai dãy khác rỗng $\mathbf u,\mathbf u'$ và dãy nối $\mathbf u\cdot \mathbf u'$, $\bigoplus(\mathbf u\cdot \mathbf u')=\big(\bigoplus \mathbf u\big)\oplus\big(\bigoplus \mathbf u'\big)$.
- (b) Với mọi hoán vị $\pi$ của $\{1,\ldots,\ell\}$, $\bigoplus(e_{\pi(1)},\ldots,e_{\pi(\ell)})=\bigoplus(e_1,\ldots,e_\ell)$.
- (c) Với mọi phân hoạch $\{1,\ldots,\ell\}=G_1\cup\cdots\cup G_\sigma$ thành các nhóm khác rỗng, rời nhau, gọi $\gamma_j$ là phép gộp của các $e_i$ có $i\in G_j$; khi đó $\bigoplus(\gamma_1,\ldots,\gamma_\sigma)=\bigoplus(e_1,\ldots,e_\ell)$.

**Điều kiện áp dụng.** Mỗi phần tử của dãy thuộc đúng một nhóm; phép toán được tính chính xác trên $E$.

**Phạm vi.** Bổ đề nói về giá trị của phép gộp, không nói về số phép toán hay thời gian.
:::

::: proof
**Bước 1 (gộp hai dãy nối nhau).** Chứng minh (a) bằng quy nạp theo độ dài $\ell'$ của $\mathbf u'$. Khi $\ell'=1$, $\mathbf u'=(e)$ và $\bigoplus(\mathbf u\cdot(e))=\big(\bigoplus \mathbf u\big)\oplus e$ theo định nghĩa phép gộp của dãy. Giả sử (a) đúng với mọi $\mathbf u'$ dài $\ell'-1\ge1$, và $\mathbf u'=\mathbf u''\cdot(e)$ với $\mathbf u''$ dài $\ell'-1$. Viết gọn $\bar{\mathbf u}=\bigoplus \mathbf u$ cho mỗi dãy khác rỗng $\mathbf u$. Khi đó
$$
\begin{aligned}
\textstyle\bigoplus(\mathbf u\cdot \mathbf u')&=\textstyle\bigoplus(\mathbf u\cdot \mathbf u'')\oplus e\\
&=(\bar{\mathbf u}\oplus\bar{\mathbf u}'')\oplus e\\
&=\bar{\mathbf u}\oplus(\bar{\mathbf u}''\oplus e)\\
&=\bar{\mathbf u}\oplus\bar{\mathbf u}',
\end{aligned}
$$
trong đó dòng đầu theo định nghĩa phép gộp của dãy, dòng hai theo giả thiết quy nạp, dòng ba theo tính kết hợp và dòng cuối lại theo định nghĩa.

**Bước 2 (đổi thứ tự).** Chứng minh (b) bằng quy nạp theo $\ell$. Với $\ell=1$ chỉ có hoán vị đồng nhất. Giả sử (b) đúng cho mọi dãy dài $\ell-1\ge1$. Viết dãy đã hoán vị thành $\mathbf u\cdot(e_\ell)\cdot \mathbf u'$, với $\mathbf u,\mathbf u'$ có thể rỗng. Nếu cả $\mathbf u$ và $\mathbf u'$ khác rỗng,
$$
\begin{aligned}
&\textstyle\bigoplus\big(\mathbf u\cdot(e_\ell)\cdot \mathbf u'\big)\\
&\quad=(\bar{\mathbf u}\oplus e_\ell)\oplus\bar{\mathbf u}'\\
&\quad=\bar{\mathbf u}\oplus(e_\ell\oplus\bar{\mathbf u}')\\
&\quad=\bar{\mathbf u}\oplus(\bar{\mathbf u}'\oplus e_\ell)\\
&\quad=(\bar{\mathbf u}\oplus\bar{\mathbf u}')\oplus e_\ell\\
&\quad=\textstyle\bigoplus(\mathbf u\cdot \mathbf u')\oplus e_\ell,
\end{aligned}
$$
các đẳng thức lần lượt theo (a), tính kết hợp, tính giao hoán, tính kết hợp và (a).
Khi $\mathbf u'$ rỗng, dãy đã hoán vị là $\mathbf u\cdot(e_\ell)$ và đẳng thức cuối có ngay từ định nghĩa; khi $\mathbf u$ rỗng, chuỗi trên bỏ số hạng $\bar{\mathbf u}$ và chỉ dùng tính giao hoán. Dãy $\mathbf u\cdot \mathbf u'$ là một hoán vị của $e_1,\ldots,e_{\ell-1}$, nên theo giả thiết quy nạp $\bigoplus(\mathbf u\cdot \mathbf u')=\bigoplus(e_1,\ldots,e_{\ell-1})$, và vế phải bằng $\bigoplus(e_1,\ldots,e_\ell)$ theo định nghĩa.

**Bước 3 (đổi cách nhóm).** Theo (b), xếp lại dãy sao cho các phần tử của $G_1$ đứng trước, rồi đến $G_2$, …, $G_\sigma$; phép gộp không đổi. Áp (a) $\sigma-1$ lần cho dãy đã xếp lại được $\bigoplus(\gamma_1,\ldots,\gamma_\sigma)$. $\square$
:::

Ví dụ 02.2 là trường hợp $E=\mathbb Z$, $\oplus=+$, $\ell=6$ với ba nhóm $G_1=\{1,4\}$, $G_2=\{2,5\}$, $G_3=\{3,6\}$; ba tổng bộ phận $3,7,14$ là $\gamma_1,\gamma_2,\gamma_3$.

Các giả thiết của Bổ đề 02.2 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ tính giao hoán: với phép "lấy phần tử đầu", hai máy giữ $(2)$ và $(4)$ cho kết quả gộp $2$ hoặc $4$ tùy máy nào báo trước.
- Bỏ tính kết hợp: trung bình hai số $\mathrm{tb}(x,y)=(x+y)/2$ giao hoán nhưng không kết hợp; nhóm $\{2,4\}$ rồi $\{9\}$ cho $\mathrm{tb}(\mathrm{tb}(2,4),9)=6$, còn nhóm $\{2\}$ rồi $\{4,9\}$ cho $\mathrm{tb}(2;6{,}5)=4{,}25$, trong khi trung bình đúng của $2,4,9$ là $5$.
- Bỏ "mỗi phần tử thuộc đúng một nhóm": nếu số $a_1=2$ có hai bản sao trên hai máy và cả hai được cộng, tổng là $26$ thay cho $24$.

Bước 1 chỉ dùng tính kết hợp; Bước 2 cần thêm tính giao hoán để đưa $e_\ell$ về cuối; Bước 3 dùng điều kiện mỗi phần tử thuộc đúng một nhóm.

**Trong thực hành.** Phép cộng số dấu phẩy động trên máy tính không kết hợp. Với số double của Python, $(0{,}1+0{,}2)+0{,}3$ cho `0.6000000000000001` còn $0{,}1+(0{,}2+0{,}3)$ cho `0.6`. Bổ đề 02.2 vì vậy áp được cho số nguyên không tràn, cho phép lấy giá trị lớn nhất và cho số hữu tỷ chính xác; với số dấu phẩy động, các cách chia dãy khác nhau có thể cho kết quả khác nhau ở các chữ số cuối, và chương trình kiểm thử phải so kết quả với một sai số cho phép.

<!-- note-topic-id: lec-02-topic-03 -->
### 1.3 Cụm máy và hệ thống tệp phân tán

Ví dụ 02.2 giả sử mỗi số nằm sẵn ở một máy. Trên một kho thật, việc đặt dữ liệu lên các máy và giữ dữ liệu khi máy hỏng do hai tầng đảm nhiệm (MMDS, §2.1): tổ chức vật lý của các máy và một hệ thống tệp chia tệp thành khối, lưu mỗi khối thành nhiều bản.

Các máy tính toán, gọi là **nút** (compute node), được xếp trong các tủ máy (rack), mỗi tủ khoảng 8–64 nút; các nút trong một tủ nối với nhau bằng mạng, thường là Ethernet gigabit, và các tủ nối với nhau bằng một tầng mạng hoặc bộ chuyển mạch (switch) khác (MMDS, §2.1.1, tr.22–23). Trang chiếu MMDS (tr.5) ghi 16–64 nút mỗi tủ, băng thông 1 Gbps giữa hai nút bất kỳ trong một tủ và 2–10 Gbps trên đường trục giữa các tủ. Với kiến trúc này có hai kiểu hỏng chính: mất một nút, chẳng hạn khi đĩa của nút hỏng, và mất cả một tủ, khi mạng nối các nút của tủ với bên ngoài hỏng (MMDS, tr.23).

::: definition Định nghĩa 02.3 (Cụm máy và hệ thống tệp phân tán)
- Một **cụm máy** (computing cluster) là tập các nút tính toán xếp trong các tủ máy; các nút trong một tủ nối bằng mạng của tủ, các tủ nối bằng mạng liên tủ.
- Một **hệ thống tệp phân tán** (distributed file system, DFS) lưu mỗi tệp thành các **khối** (chunk) cỡ cố định, thường 64 MB; mỗi khối có nhiều **bản sao** (replica), thường ba bản, đặt trên các nút sao cho không phải mọi bản sao nằm trong cùng một tủ; mất một tủ khi đó không làm mất mọi bản sao.
- Vị trí các khối của mỗi tệp được ghi ở **nút chủ** (master node, còn gọi là name node), nút giữ siêu dữ liệu của hệ thống tệp; nút chủ cũng được nhân bản.
- DFS dành cho tệp rất lớn, có thể tới hàng terabyte, hiếm khi cập nhật tại chỗ; tệp chủ yếu được đọc làm dữ liệu cho tính toán và đôi khi được ghi nối thêm.
:::

Định nghĩa theo MMDS (§2.1.2, tr.24). CS246 (trang chiếu 35) ghi cỡ khối 16–64 MB và hệ số nhân bản 2 hoặc 3.

Khối của DFS khác khối của Định nghĩa 01.4: khối đĩa vài chục kilobyte là đơn vị truyền giữa đĩa và bộ nhớ, còn khối DFS hàng chục megabyte là đơn vị lưu và nhân bản giữa các máy.

Bản sao thuộc về lưu trữ: ba bản sao của một khối chứa cùng dữ liệu, nên một phép tính phải đọc khối đó đúng một lần. Nếu đọc cả ba bản, mỗi từ trong khối được đếm ba lần, đúng kiểu đếm trùng mà Nhận xét 01.3 cấm.

![Các rack, kết nối mạng và bản sao khối trong HDFS. Tệp chia thành hai khối A và B. Tủ rack 1 gồm máy 1 lưu A và B, máy 2 lưu B; tủ rack 2 gồm máy 3 lưu A và B, máy 4 lưu A. Mỗi tủ có bộ chuyển mạch riêng nối tới bộ chuyển mạch liên rack. Mỗi khối có ba bản sao trên hai rack.](img/lec-02/hdfs-racks.svg)

Hình vẽ một tệp hai khối $\mathrm A,\mathrm B$, mỗi khối ba bản sao. Khối $\mathrm A$ nằm ở máy 1, máy 3 và máy 4; khối $\mathrm B$ ở máy 1, máy 2 và máy 3. Không khối nào có mọi bản sao trong cùng một tủ, nên mất máy 1 hay mất cả tủ 1 thì cả $\mathrm A$ lẫn $\mathrm B$ vẫn đọc được. Hình cũng cho thứ tự ưu tiên khi chọn nơi chạy một phép tính trên khối $\mathrm A$: máy có bản sao của $\mathrm A$ đọc tại chỗ, không qua mạng; máy khác cùng tủ với một bản sao đọc qua bộ chuyển mạch của tủ; máy ở tủ khác phải dùng đường nối liên tủ, là đường mà mọi cặp máy khác tủ dùng chung. Đây là nghĩa cụ thể của yêu cầu "đưa tính toán tới gần dữ liệu" ở Mục 1.1.

::: remark Nhận xét 02.4 (Trong thực hành: khi nào không dùng DFS)
DFS và MapReduce chỉ có lợi khi tệp rất lớn và hiếm khi cập nhật tại chỗ. Hệ đặt chỗ của hãng hàng không không hợp với DFS dù dữ liệu rất lớn, vì dữ liệu thay đổi liên tục (MMDS, tr.24). Một nhà bán lẻ trực tuyến không dùng MapReduce để tìm sản phẩm và ghi giao dịch, vì các thao tác đó ít tính toán và thay đổi cơ sở dữ liệu, nhưng có thể dùng nó cho truy vấn phân tích, như tìm cho mỗi người dùng những người có hành vi mua giống nhất (MMDS, tr.30–31). Hệ thống tệp phân tán Hadoop (Hadoop Distributed File System, HDFS) là một bản cài đặt mã nguồn mở của DFS, dùng cùng Hadoop, bản cài đặt mã nguồn mở của MapReduce (MMDS, tr.24); cụm ở Mục 5 dùng HDFS.
:::

Như vậy, chúng ta đã có Bổ đề 02.2: với một phép gộp kết hợp và giao hoán, tính kết quả cục bộ trên từng máy rồi gộp cho cùng kết quả với tính trên một máy, miễn là mỗi phần tử góp đúng một lần. Chúng ta cũng có mô hình lưu trữ của Định nghĩa 02.3, trong đó bản sao chỉ phục vụ độ bền và vị trí đọc. Tuy nhiên, Ví dụ 02.2 chỉ có một kết quả cần gộp. Bài toán đếm từ có một số đếm cho mỗi từ, và các lần xuất hiện của cùng một từ nằm rải trên nhiều máy. Trong Mục 2, chúng ta xây mô hình đưa mọi đóng góp của cùng một từ về một chỗ để gộp.

<!-- note-topic-id: lec-02-topic-04 -->
## 2. Mô hình tính toán MapReduce

Xét kho nhỏ nhất còn giữ được khó khăn của Mục 1: hai văn bản $d_1=$ "mèo chó mèo" và $d_2=$ "chó chim" nằm trên hai máy. Từ "mèo" chỉ có trong $d_1$, nhưng từ "chó" có một lần xuất hiện ở mỗi máy. Máy giữ $d_1$ biết chó xuất hiện một lần, máy giữ $d_2$ cũng vậy; số đếm đúng là 2, và không máy nào tự tính được con số đó.

### 2.1 Bài toán đếm từ

Trước khi thiết kế cách tính, cần nêu chính xác đầu ra phải trả.

::: example Ví dụ 02.3 (Đầu ra cần trả cho hai văn bản)
**Dữ kiện.** $d_1=$ "mèo chó mèo", $d_2=$ "chó chim"; các từ đã được tách theo khoảng trắng.

**Đếm.** mèo xuất hiện 2 lần, cả hai trong $d_1$; chó xuất hiện 2 lần, một lần trong mỗi văn bản; chim xuất hiện 1 lần, trong $d_2$.

**Đầu ra.** Ba cặp (mèo, 2), (chó, 2), (chim, 1), không quy định thứ tự.

**Kiểm tra lại.** $2+2+1=5$, bằng tổng số từ $3+2$ của hai văn bản.
:::

::: definition Định nghĩa 02.5 (Bài toán đếm từ)
**Đầu vào.** $n\ge0$ văn bản $d_1,\ldots,d_n$, mỗi văn bản là một dãy từ $d_i=(w_{i1},\ldots,w_{i\ell_i})$ với $\ell_i\ge0$ từ, sau một quy tắc tách từ cố định.

**Đại lượng.** Với mỗi từ $w$, số lần $w$ xuất hiện trong $d_i$ là $c_i(w)=\lvert\{j:1\le j\le\ell_i,\ w_{ij}=w\}\rvert$; tập từ của $d_i$ là $\mathcal W_i=\{w_{i1},\ldots,w_{i\ell_i}\}$, tập từ của kho là $\mathcal W=\mathcal W_1\cup\cdots\cup\mathcal W_n$, và
$$
c(w)=\sum_{i=1}^{n}c_i(w).
$$

**Đầu ra.** Đúng một cặp $(w,c(w))$ cho mỗi $w\in\mathcal W$, không quy định thứ tự. Khi mọi văn bản rỗng, $\mathcal W=\varnothing$ và đầu ra rỗng.

**Ngân sách.** Kho lớn hơn bộ nhớ và đĩa của một máy; các văn bản nằm trên nhiều máy.
:::

Định nghĩa là một bài toán dữ liệu theo nghĩa của Định nghĩa 01.1: miền đầu vào là các dãy văn bản đã tách từ, quan hệ đầu vào–đầu ra cho đúng một tập cặp được chấp nhận, và ngân sách loại cách gom cả kho về một máy. Số đếm $c(w)$ là tổng của các đóng góp $c_i(w)$ nằm ở nhiều máy; đó là chỗ khó của bài toán. Ví dụ 02.3 là thể hiện với $n=2$, $\ell_1=3$, $\ell_2=2$, $\mathcal W_1=\{\text{mèo},\text{chó}\}$, $\mathcal W_2=\{\text{chó},\text{chim}\}$, $c(\text{chó})=c_1(\text{chó})+c_2(\text{chó})=1+1=2$.

Hai cách hiểu sai thường gặp đều làm sai đầu ra. Bài toán đếm số lần xuất hiện, không đếm số văn bản chứa từ: mèo và chó cùng có số đếm 2, nhưng mèo nằm trong một văn bản còn chó nằm trong hai, và đếm số văn bản chứa từ cho mèo 1 thay cho 2. Chia cho tổng số từ để được tần suất tương đối cho mèo $2/5$; đó là một bài toán khác, cần thêm tổng số từ của kho. Đầu ra chỉ chứa các từ có trong kho: một từ không xuất hiện không có cặp $(w,0)$.

<!-- note-topic-id: lec-02-topic-05 -->
### 2.2 Hàm Map, hàm Reduce và nhóm theo khóa

Trên một máy, đếm từ trên một tệp lớn hơn bộ nhớ có thể làm bằng ba bước: tách tệp thành các từ, mỗi từ một dòng; sắp xếp các dòng để các dòng cùng từ đứng liền nhau; đếm độ dài mỗi đoạn dòng giống nhau. Trên hệ Unix, ba bước đó có dạng dòng lệnh `words(doc.txt) | sort | uniq -c`, với `words` là chương trình tách từ (trang chiếu MMDS, tr.13). Về mặt ý tưởng, MapReduce giữ đúng ba bước này. Bước tách biến mỗi phần tử đầu vào thành các cặp (từ, 1) và chạy độc lập trên từng phần của kho; bước sắp xếp trở thành bước **nhóm theo khóa** (group by key), gom mọi cặp cùng khóa, dù phát ở máy nào; bước đếm xử lý từng khóa độc lập. Bước đầu và bước cuối là hai hàm do người lập trình viết, chạy song song trên nhiều máy; bước giữa do hệ thống thực hiện và không phụ thuộc bài toán (MMDS, §2.2, tr.25). Ba định nghĩa sau phát biểu ba bước đó cho một bài toán bất kỳ.

::: definition Định nghĩa 02.6 (Hàm Map)
Cho $K_1,V_1$ là miền khóa và miền giá trị của đầu vào, $K_2,V_2$ là miền khóa và miền giá trị trung gian. Với tập $\Omega$, ký hiệu $\Omega^*$ là tập các dãy hữu hạn trên $\Omega$, gồm cả dãy rỗng; một dãy giữ thứ tự và giữ phần tử lặp. Một **hàm Map** là một hàm
$$
\mathrm{Map}:K_1\times V_1\longrightarrow(K_2\times V_2)^*,
$$
biến một cặp đầu vào thành một dãy **cặp trung gian**. Mỗi lần gọi Map **phát** (emit) các cặp của dãy đó; các khóa phát ra không cần khác nhau.
:::

Một lần gọi Map nhận một phần tử đầu vào và phát không, một hay nhiều cặp. Trong đếm từ, phần tử đầu vào là cặp (mã văn bản, nội dung), chẳng hạn $(1,d_1)$, và $\mathrm{Map}(1,d_1)$ là dãy (mèo, 1), (chó, 1), (mèo, 1). Khóa đầu vào ở đây là mã văn bản và Map không dùng nó; MMDS giữ dạng khóa–giá trị cho đầu vào để đầu ra của một công việc làm được đầu vào của công việc sau (§2.2.1, tr.25). Khóa trung gian không phải "khóa" theo nghĩa cơ sở dữ liệu: cùng một văn bản phát hai cặp cùng khóa mèo.

Đầu ra của Map phải là dãy, không phải tập. Nếu $\mathrm{Map}(1,d_1)$ là tập $\{(\text{mèo},1),(\text{chó},1)\}$, hai lần xuất hiện của mèo nhập thành một và số đếm cuối cùng của mèo là 1 thay cho 2.

::: definition Định nghĩa 02.7 (Hàm Reduce và reducer)
Cho $K_3,V_3$ là miền khóa và miền giá trị của đầu ra. Một **hàm Reduce** là một hàm
$$
\begin{aligned}
\mathrm{Reduce}:{}&K_2\times V_2^*\\
&\longrightarrow(K_3\times V_3)^*,
\end{aligned}
$$
nhận một khóa trung gian $k$ cùng một danh sách giá trị và phát một dãy cặp đầu ra. Một lần áp hàm Reduce cho một khóa cùng danh sách giá trị của khóa đó gọi là một **reducer**.
:::

Reduce nhận cả danh sách giá trị của một khóa, không nhận từng cặp. Trong đếm từ, $\mathrm{Reduce}(\text{mèo},[1,1])$ cộng các phần tử của danh sách và phát (mèo, 2). Kiểu đầu ra có thể khác kiểu trung gian (MMDS, §2.2.3, tr.27): khi tính trung bình, giá trị trung gian là cặp tổng–số lượng còn giá trị đầu ra là một số.

Thuật ngữ reducer theo MMDS: một reducer là một lần áp dụng hàm, còn một **tác vụ** (task) Reduce là một đơn vị công việc được giao cho một máy và thực hiện một hoặc nhiều reducer.

Còn phải nói rõ danh sách giá trị của khóa $k$ gồm những gì, và cặp $(k,x)$ phát ở một máy đi tới tác vụ Reduce nào. MMDS dùng một hàm băm cho việc thứ hai (MMDS, §2.2.2, tr.26–27; trang chiếu MMDS, tr.32).

::: definition Định nghĩa 02.8 (Hàm phân phối và nhóm theo khóa)
Cho $r\ge1$ là số tác vụ Reduce và $Z$ là dãy mọi cặp trung gian do mọi lần gọi Map phát, theo một thứ tự nào đó.

- Một **hàm phân phối** (partitioning function) là một hàm $h:K_2\to\{0,\ldots,r-1\}$; cặp $(k,x)$ được gửi tới tác vụ Reduce số $h(k)$.
- Với mỗi khóa $k$ xuất hiện trong $Z$, **danh sách giá trị** của $k$ là dãy
$$
L_k=[\,x\mid(k,x)\in Z\,],
$$
gồm mọi giá trị đi cùng $k$ trong $Z$, mỗi lần phát là một phần tử, giữ phần tử lặp. Hệ thống chỉ bảo đảm $L_k$ đến một hoán vị: thứ tự các phần tử của $L_k$ không được quy định.
- **Nhóm theo khóa** là việc tạo các cặp $(k,L_k)$, mỗi khóa phân biệt của $Z$ đúng một cặp, và giao $(k,L_k)$ cho tác vụ $h(k)$.
:::

Hàm phân phối là một hàm băm theo Định nghĩa 01.8 với số thùng bằng $r$: mỗi thùng là một tác vụ Reduce. Lựa chọn mặc định là $h(k)=\mathrm{hash}(k)\bmod r$, và người dùng có thể thay hàm này, nhưng với mọi cách chọn, mỗi khóa được giao cho đúng một tác vụ Reduce (MMDS, chú thích 1, tr.27). Hai khóa khác nhau có thể cùng một tác vụ; chúng vẫn là hai nhóm và hai reducer.

Ký hiệu $L_k=[\,x\mid(k,x)\in Z\,]$ đọc là "danh sách các $x$ sao cho cặp $(k,x)$ là một phần tử của $Z$"; mỗi lần phát là một phần tử riêng của $Z$, nên hai lần phát (mèo, 1) cho hai số 1 trong $L_{\text{mèo}}$.

Ví dụ sau cho thấy ba định nghĩa bao hàm phép đếm của Ví dụ 02.3 ở chỗ nào.

::: example Ví dụ 02.4 (Vết chạy đếm từ)
**Dữ kiện.** $d_1=$ "mèo chó mèo", $d_2=$ "chó chim". Map phát $(w,1)$ cho mỗi lần xuất hiện của từ $w$; Reduce cộng các giá trị của danh sách.

**Map (Định nghĩa 02.6).**

| Lần gọi | Cặp phát ra |
|---|---|
| $\mathrm{Map}(1,d_1)$ | (mèo, 1), (chó, 1), (mèo, 1) |
| $\mathrm{Map}(2,d_2)$ | (chó, 1), (chim, 1) |

Dãy $Z$ gồm 5 cặp.

**Nhóm theo khóa (Định nghĩa 02.8).** $L_{\text{mèo}}=[1,1]$, $L_{\text{chó}}=[1,1]$, $L_{\text{chim}}=[1]$. Danh sách của chó có một giá trị từ $d_1$ và một giá trị từ $d_2$.

**Reduce (Định nghĩa 02.7).** $\mathrm{Reduce}(\text{mèo},[1,1])=$ (mèo, 2); $\mathrm{Reduce}(\text{chó},[1,1])=$ (chó, 2); $\mathrm{Reduce}(\text{chim},[1])=$ (chim, 1).

**Kiểm tra lại.** Đầu ra trùng Ví dụ 02.3; tổng các số đếm $2+2+1=5$ bằng số cặp của $Z$.
:::

Bước Map không cần biết văn bản khác chứa gì; bước Reduce cho chó cần cả hai giá trị 1 nhưng không cần biết chúng đến từ máy nào. Toàn bộ việc "đưa về một chỗ" nằm ở bước nhóm theo khóa. Hai hàm của vết chạy viết thành thuật toán như sau.

::: algorithm Thuật toán 02.9 (Map và Reduce cho đếm từ)
**Đầu vào.** Map: một cặp $(i,d_i)$ với $d_i=(w_{i1},\ldots,w_{i\ell_i})$. Reduce: một từ $w$ và danh sách $L_w$ các số nguyên dương.

**Đầu ra.** Map: dãy $\ell_i$ cặp $(w_{ij},1)$. Reduce: một cặp $(w,\sum_{x\in L_w}x)$.

**Giả thiết.** Mọi văn bản dùng cùng một quy tắc tách từ; số đếm vừa một ô nhớ.

1. $\mathrm{Map}(i,d_i)$: với $j=1,\ldots,\ell_i$, phát $(w_{ij},1)$.
2. $\mathrm{Reduce}(w,L_w)$: đặt $\mathit{tổng}=0$; với mỗi $x$ trong $L_w$, đặt $\mathit{tổng}=\mathit{tổng}+x$; phát $(w,\mathit{tổng})$.

**Dừng.** Map dừng sau $\ell_i$ vòng; Reduce dừng sau $\lvert L_w\rvert$ vòng.

**Trường hợp biên.** Văn bản rỗng không phát cặp nào. Reduce không được gọi với danh sách rỗng, vì một từ không xuất hiện không có nhóm.

**Chi phí.** Mô hình đếm phép toán: Map trên $d_i$ làm $\ell_i$ lần phát; Reduce cho $w$ làm $\lvert L_w\rvert$ phép cộng, vì tổng được khởi tạo bằng 0; bộ nhớ của Reduce là một biến tổng, không phụ thuộc $\lvert L_w\rvert$.
:::

```text
Map(i, d):
    với mỗi từ w trong d, theo thứ tự:
        phát (w, 1)

Reduce(w, L):
    tổng = 0
    với mỗi x trong L:
        tổng = tổng + x
    phát (w, tổng)
```

Reduce đọc $L_w$ lần lượt từng phần tử và chỉ giữ một biến tổng, nên không cần nạp cả danh sách vào bộ nhớ. Phép cộng không phụ thuộc thứ tự các phần tử của $L_w$, điều cần thiết vì Định nghĩa 02.8 không quy định thứ tự đó.

<!-- note-topic-id: lec-02-topic-06 -->
### 2.3 Một công việc MapReduce và tính đúng

Ba định nghĩa trên mô tả từng bước; một **công việc** (job) MapReduce ghép chúng với việc chia đầu vào cho nhiều tác vụ.

![Luồng một công việc MapReduce đọc từ trái sang phải qua tám khối. Khối dữ liệu viền mảnh: đầu vào X thuộc (K₁ × V₁)*, dãy Z các cặp trung gian thuộc (K₂ × V₂)*, các nhóm (k, L_k), đầu ra Y thuộc (K₃ × V₃)*. Khối hệ thống thực hiện viền xám nét đứt: chia X thành X₁, …, X_m theo vị trí; phân phối bằng h và nhóm theo khóa. Khối người lập trình viết viền cam liền, đậm: Map với m tác vụ, một lần gọi cho mỗi cặp; Reduce với r tác vụ, một lần gọi cho mỗi khóa. Dưới đường kẻ đứt là ví dụ cặp (chó, 1) từ d₂: h(chó) chọn một tác vụ Reduce, nhóm của chó là [1, 1], Reduce phát (chó, 2).](img/lec-02/note-luong-mapreduce.svg)

Hình vẽ lại sơ đồ của MMDS (Hình 2.2, tr.26) với ký hiệu của chương: khối viền cam liền là phần người lập trình viết, khối viền xám nét đứt là phần hệ thống làm. Theo dòng ví dụ dưới hình, cặp (chó, 1) phát từ $d_2$ đi tới tác vụ $h(\text{chó})$, nơi nó gặp cặp (chó, 1) phát từ $d_1$. Thuật toán sau viết luồng đó thành giả mã.

::: algorithm Thuật toán 02.10 (Một công việc MapReduce)
**Đầu vào.** Dãy cặp $X\in(K_1\times V_1)^*$; hàm Map, hàm Reduce; số tác vụ $m,r\ge1$; hàm phân phối $h:K_2\to\{0,\ldots,r-1\}$.

**Đầu ra.** Dãy cặp $Y\in(K_3\times V_3)^*$, không quy định thứ tự.

**Giả thiết.** Map và Reduce xác định và dừng trên mọi đầu vào.

1. Hệ thống chia $X$ theo vị trí bản ghi thành $m$ phần $X_1,\ldots,X_m$: mỗi vị trí của $X$ thuộc đúng một phần.
2. Song song với $j=1,\ldots,m$: tác vụ Map $j$ gọi Map cho mỗi cặp của $X_j$ và nối các dãy phát ra thành $Z_j$.
3. Hệ thống nối $Z_1,\ldots,Z_m$ thành $Z$, giữ mọi phần tử.
4. Song song với $z=0,\ldots,r-1$: với mỗi khóa phân biệt $k$ của $Z$ có $h(k)=z$, tác vụ Reduce $z$ nhận $L_k$ và nối dãy $\mathrm{Reduce}(k,L_k)$ vào $Y_z$.
5. Trả $Y$ là dãy nối $Y_0,\ldots,Y_{r-1}$.

**Dừng.** Mỗi bước có hữu hạn lần gọi hàm, và mỗi lần gọi dừng.

**Trường hợp biên.** $X$ rỗng cho $Z$ rỗng và $Y$ rỗng. Một phần $X_j$ có thể rỗng; một tác vụ Reduce có thể không nhận khóa nào và cho $Y_z$ rỗng.

**Chi phí.** Không có công thức chung: chi phí phụ thuộc hai hàm do người dùng viết và lượng dữ liệu trung gian, nên được đếm riêng cho từng bài toán.
:::

```text
chia X thành X_1, ..., X_m theo vị trí bản ghi
song song với j = 1, ..., m:
    Z_j ← nối các dãy Map(k, x) với mỗi (k, x) trong X_j
Z ← nối Z_1, ..., Z_m, giữ mọi phần tử
song song với z = 0, ..., r−1:
    Y_z ← dãy rỗng
    với mỗi khóa phân biệt k của Z có h(k) = z:
        L_k ← danh sách các x với (k, x) thuộc Z
        nối Reduce(k, L_k) vào Y_z
trả Y ← nối Y_0, ..., Y_{r−1}
```

Thao tác quyết định của thuật toán là dòng tạo $L_k$ cùng điều kiện $h(k)=z$: mọi cặp cùng khóa, từ mọi tác vụ Map, đi về một nhóm của một tác vụ Reduce. Giả mã không quy định cách tạo $L_k$. Một cài đặt quét lại $Z$ cho mỗi khóa sẽ đọc $Z$ nhiều lần; hệ thống thật sắp xếp và trộn các tệp trung gian theo khóa, tức thực hiện bước `sort` của Mục 2.2 trên nhiều máy (MMDS, §2.2, tr.25; §2.2.2, tr.27; CS246, trang chiếu 44). Bước 3 là một bước logic: $Z$ không cần nằm trên một máy, và các phần của $Z$ nằm ở các máy chạy Map.

Muốn chứng minh một công việc trả đúng kết quả, cần tách phần do khung bảo đảm khỏi phần phụ thuộc hai hàm của người lập trình. Mệnh đề sau nói khung bảo đảm gì.

::: proposition Mệnh đề 02.11 (Tính đúng của một công việc MapReduce)
**Giả thiết.**

- Bước 1 của Thuật toán 02.10 chia $X$ theo vị trí: mỗi vị trí của $X$ thuộc đúng một phần $X_j$.
- Map và Reduce xác định và dừng trên mọi đầu vào.
- Reduce không phụ thuộc thứ tự của danh sách giá trị: $\mathrm{Reduce}(k,L)=\mathrm{Reduce}(k,L')$ khi $L'$ là một hoán vị của $L$.
- $h$ là một hàm: mỗi khóa có đúng một giá trị $h(k)$.

**Kết luận.** Thuật toán 02.10 dừng và $Y$ là dãy nối, theo một thứ tự nào đó, của các dãy $\mathrm{Reduce}(k,L_k)$, mỗi khóa phân biệt $k$ của $Z$ đúng một dãy, trong đó $L_k$ chứa mọi giá trị đi cùng $k$ trong $Z$, dãy nối các $\mathrm{Map}(k',x')$ với $(k',x')$ thuộc $X$.

**Điều kiện áp dụng.** Công việc chạy không lỗi, không có tác vụ nào phải chạy lại.

**Phạm vi.** Mệnh đề không nói hai hàm của người lập trình giải đúng bài toán; nó cũng không quy định thứ tự các cặp trong $Y$.
:::

::: proof
**Bước 1 (Map được gọi đúng một lần cho mỗi vị trí).** Theo giả thiết thứ nhất, mỗi vị trí của $X$ thuộc đúng một phần $X_j$, và tác vụ Map $j$ gọi Map một lần cho mỗi cặp của $X_j$. Vậy Map được gọi đúng một lần cho mỗi vị trí của $X$; hai bản ghi cùng nội dung ở hai vị trí là hai lần gọi.

**Bước 2 ($Z$ chứa đúng các cặp phát ra).** Phép nối ở bước 2–3 của Thuật toán 02.10 không bỏ và không nhân phần tử nào, nên $Z$ chứa đúng các cặp do các lần gọi ở Bước 1 phát, kể cả các cặp lặp. Map xác định, nên dãy $Z$ được xác định bởi $X$ đến một hoán vị.

**Bước 3 (mỗi khóa đúng một nhóm, ở đúng một tác vụ).** Với mỗi khóa phân biệt $k$ của $Z$, giả thiết thứ tư cho đúng một tác vụ $z=h(k)$. Tác vụ đó tạo $L_k$ từ mọi cặp của $Z$ có khóa $k$, nên $L_k$ chứa mọi giá trị đi cùng $k$, mỗi lần phát một phần tử. Các tác vụ khác không nhận $k$, nên Reduce được gọi đúng một lần cho $k$.

**Bước 4 (kết quả không phụ thuộc thứ tự).** Hệ thống chỉ xác định $L_k$ đến một hoán vị. Theo giả thiết thứ ba, mọi hoán vị cho cùng $\mathrm{Reduce}(k,L_k)$, và Reduce xác định nên dãy đó được xác định. $Y$ là dãy nối các $Y_z$, mỗi $Y_z$ là dãy nối các $\mathrm{Reduce}(k,L_k)$ với $h(k)=z$, nên $Y$ gồm đúng các dãy $\mathrm{Reduce}(k,L_k)$, mỗi khóa một lần.

**Bước 5 (dừng).** $X$ hữu hạn, mỗi lần gọi Map dừng và phát dãy hữu hạn, nên $Z$ hữu hạn và có hữu hạn khóa; mỗi lần gọi Reduce dừng. Khi $X$ rỗng, $Z$ rỗng, không có khóa nào và $Y$ rỗng. $\square$
:::

Các giả thiết của Mệnh đề 02.11 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "mỗi vị trí thuộc đúng một phần": nếu $d_2$ được đưa vào cả hai phần, chẳng hạn vì hai bản sao của khối chứa $d_2$ cùng được đọc, chó nhận $L_{\text{chó}}=[1,1,1]$ và được đếm 3.
- Bỏ "$h$ là một hàm": nếu hai cặp (chó, 1) đi tới hai tác vụ Reduce khác nhau, mỗi tác vụ có một nhóm $[1]$ và đầu ra có hai cặp (chó, 1) thay cho một cặp (chó, 2).
- Bỏ "Reduce không phụ thuộc thứ tự": một hàm Reduce phát giá trị đầu tiên của danh sách cho cùng một kết quả trên $[1,1]$ của đếm từ, nhưng trên danh sách $[5,4]$ của hàng 1 ở Ví dụ 02.6 thì phát 5 hoặc 4 tùy thứ tự hệ thống giao.
- Bỏ "Map và Reduce dừng": một hàm Map lặp vô hạn trên một văn bản làm tác vụ Map của văn bản đó không bao giờ xong, nên bước nhóm không bắt đầu được.

Bước 1 dùng giả thiết thứ nhất, Bước 3 dùng giả thiết thứ tư, Bước 4 dùng giả thiết thứ ba, và Bước 2, Bước 5 dùng giả thiết thứ hai. Mệnh đề 02.11 tách trách nhiệm: khung bảo đảm mỗi khóa gặp đủ giá trị của nó đúng một lần; người lập trình phải chứng minh $\mathrm{Reduce}(k,L_k)$ là kết quả cần cho khóa $k$. Với đếm từ, phần thứ hai là một phép đếm.

::: corollary Hệ quả 02.12 (Tính đúng của đếm từ)
**Giả thiết.** Đầu vào thỏa Định nghĩa 02.5 và được biểu diễn thành $X=((1,d_1),\ldots,(n,d_n))$; công việc dùng Map và Reduce của Thuật toán 02.9 và thỏa các giả thiết của Mệnh đề 02.11.

**Kết luận.** $Y$ gồm đúng các cặp $(w,c(w))$, mỗi $w\in\mathcal W$ một cặp.

**Điều kiện áp dụng.** Phép cộng số nguyên chính xác, không tràn.

**Phạm vi.** Không quy định thứ tự các cặp trong $Y$.
:::

::: proof
**Khóa của $Z$ là $\mathcal W$.** Map phát $(w_{ij},1)$ cho mỗi vị trí $j$ của mỗi văn bản $d_i$, nên một từ là khóa của $Z$ khi và chỉ khi nó xuất hiện trong ít nhất một văn bản, tức khi và chỉ khi nó thuộc $\mathcal W$.

**Độ dài danh sách.** Mỗi lần xuất hiện của $w$ trong $d_i$ phát đúng một cặp $(w,1)$, nên theo Mệnh đề 02.11,
$$
\lvert L_w\rvert=\sum_{i=1}^{n}c_i(w)=c(w).
$$

**Giá trị Reduce.** Mọi phần tử của $L_w$ bằng 1, nên Reduce phát $(w,\lvert L_w\rvert)=(w,c(w))$. Phép cộng không phụ thuộc thứ tự, nên giả thiết thứ ba của Mệnh đề 02.11 thỏa. Theo Mệnh đề 02.11, $Y$ có đúng một cặp cho mỗi khóa của $Z$, tức cho mỗi $w\in\mathcal W$. $\square$
:::

Ví dụ 02.4 là thể hiện của hệ quả: $\lvert L_{\text{chó}}\rvert=c_1(\text{chó})+c_2(\text{chó})=1+1$. Hệ quả là trường hợp riêng của Mệnh đề 02.11 vì nó chỉ thêm một bước tính trên danh sách $L_w$; các bài toán của Mục 3 cũng được chứng minh theo cách đó, bằng cách chỉ ra $L_k$ chứa gì và Reduce biến $L_k$ thành gì.

::: remark Nhận xét 02.13 (Reducer, tác vụ Reduce và lệch tải)
Thời gian của một reducer tăng theo độ dài danh sách của nó, và độ dài các danh sách thường chênh lệch nhiều giữa các khóa; trong đếm từ, $\lvert L_w\rvert=c(w)$ lớn với từ phổ biến và bằng 1 với từ hiếm. Nếu mỗi reducer là một tác vụ Reduce riêng, các tác vụ có thời gian chênh lệch lớn, hiện tượng gọi là **lệch tải** (skew).

Giao các khóa ngẫu nhiên vào ít tác vụ Reduce hơn số khóa làm thời gian các tác vụ gần nhau hơn, vì mỗi tác vụ gồm nhiều khóa; dùng nhiều tác vụ hơn số máy cho phép một tác vụ dài chiếm trọn một máy trong khi vài tác vụ ngắn chạy lần lượt trên một máy khác (MMDS, hộp "Reducers, Reduce Tasks, Compute Nodes, and Skew", tr.28).

Số tác vụ Map $m$ thường lớn hơn nhiều số máy, chẳng hạn một tác vụ cho mỗi khối DFS, còn số tác vụ Reduce $r$ thường nhỏ hơn $m$ (trang chiếu MMDS, tr.27): mỗi tác vụ Map tạo một tệp trung gian cho mỗi tác vụ Reduce, nên $r$ lớn làm số tệp trung gian tăng theo tích $mr$ (MMDS, §2.2.5, tr.29).

**Trong thực hành.** Trên một hệ thống thật, giả thiết chia theo vị trí của Mệnh đề 02.11 do hệ thống giữ khi mỗi phần đầu vào được đọc từ đúng một bản sao. Hai giả thiết còn lại do người lập trình giữ: một hàm Map dùng số ngẫu nhiên hay đọc đồng hồ không xác định, và một hàm Reduce lấy giá trị đầu của danh sách phụ thuộc thứ tự. Khi đọc nhật ký của một công việc thật, cần phân biệt hàm với tác vụ (một tác vụ Map gọi hàm Map nhiều lần), văn bản với khối (một khối DFS chứa nhiều văn bản) và từ với máy (một tác vụ Reduce nhận nhiều từ).
:::

<!-- note-topic-id: lec-02-topic-07 -->
### 2.4 Gộp cục bộ bằng hàm Combine

Trong Ví dụ 02.4, tác vụ Map đọc $d_1$ phát hai cặp (mèo, 1). Cả hai đi qua mạng tới cùng một tác vụ Reduce, chỉ để được cộng thành 2. Nếu tác vụ Map cộng trước, nó gửi một cặp (mèo, 2) thay cho hai cặp. Trên kho web, một tác vụ Map phát một cặp cho mỗi lần xuất hiện của một từ phổ biến trong phần của nó; gộp tại chỗ thay mọi cặp đó bằng một cặp. Bổ đề 02.2 cho biết khi nào việc cộng trước như vậy an toàn.

::: definition Định nghĩa 02.14 (Hàm Combine)
Một **hàm Combine** (combiner) là một hàm
$$
\begin{aligned}
\mathrm{Combine}:{}&K_2\times V_2^*\\
&\longrightarrow(K_2\times V_2)^*
\end{aligned}
$$
chạy trên đầu ra của một tác vụ Map, trước khi các cặp được gửi đi. Một lần gọi nhận một khóa $k$ cùng một danh sách khác rỗng $L$ gồm một số giá trị của khóa $k$ đang chờ gửi ở tác vụ đó, do Map hoặc một lần gọi Combine trước phát, rồi phát các cặp cùng khóa $k$ và cùng kiểu giá trị $V_2$ để thay cho các cặp của $L$. Hệ thống có thể gọi Combine không lần, một lần hay nhiều lần, trên các phần bất kỳ của đầu ra một tác vụ Map.
:::

Combine có cùng kiểu đầu vào với Reduce nhưng đầu ra phải là cặp trung gian, vì các cặp nó phát còn đi tiếp tới bước nhóm và tới Reduce. Combine chỉ thấy dữ liệu của một tác vụ Map, nên không thay được bước nhóm: hai cặp (chó, 1) từ hai tác vụ Map vẫn phải gặp nhau ở Reduce. Vì hệ thống được phép bỏ qua Combine hay gọi nó nhiều lần, kết quả của công việc không được phụ thuộc số lần gọi.

::: example Ví dụ 02.5 (Combine trên hai văn bản)
**Dữ kiện.** $d_1=$ "mèo chó mèo" ở tác vụ Map 1, $d_2=$ "chó chim" ở tác vụ Map 2. Combine nhận $(w,L)$ và phát $(w,\sum_{x\in L}x)$; Combine được gọi một lần cho mỗi khóa trên toàn bộ đầu ra của mỗi tác vụ Map.

**Tác vụ Map 1.** Map phát (mèo, 1), (chó, 1), (mèo, 1). Combine nhận (mèo, [1, 1]) và (chó, [1]), phát (mèo, 2), (chó, 1).

**Tác vụ Map 2.** Map phát (chó, 1), (chim, 1). Combine nhận (chó, [1]) và (chim, [1]), phát lại đúng hai cặp đó.

**Nhóm và Reduce.** $L_{\text{mèo}}=[2]$, $L_{\text{chó}}=[1,1]$, $L_{\text{chim}}=[1]$; Reduce phát (mèo, 2), (chó, 2), (chim, 1).

**Kiểm tra lại.** Số cặp gửi đi giảm từ 5 xuống 4; đầu ra trùng Ví dụ 02.4.
:::

![Hai hàng là hai tác vụ Map. Tác vụ Map 1 đọc d₁ = “mèo chó mèo”, Map phát (mèo, 1), (chó, 1), (mèo, 1); Combine gửi qua mạng (mèo, 2), (chó, 1). Tác vụ Map 2 đọc d₂ = “chó chim”, phát và gửi (chó, 1), (chim, 1). Bên phải, nhóm theo khóa và Reduce: mèo [2] cho (mèo, 2); chó [1, 1], một giá trị từ mỗi tác vụ Map, cho (chó, 2); chim [1] cho (chim, 1). Trước Combine 5 cặp, sau Combine 4 cặp.](img/lec-02/note-combine-dem-tu.svg)

Ở hàng trên của hình, hai cặp (mèo, 1) trong khung "Map phát" thành một cặp (mèo, 2) trong khung "Gửi qua mạng"; ở hàng dưới, Combine không gộp được gì vì $d_2$ không có từ lặp. Hai mũi tên cùng tới nhóm của chó là đóng góp mà chỉ bước nhóm theo khóa gộp được.

Phép cộng trong Ví dụ 02.5 có thể thay bằng phép gộp kết hợp, giao hoán bất kỳ. Một số bài toán còn cần một bước biến kết quả gộp thành đầu ra, như chia tổng cho số phần tử khi tính trung bình, nên mệnh đề sau cho phép Reduce áp một **hàm hoàn tất** $\phi$ sau phép gộp.

::: proposition Mệnh đề 02.15 (Combine giữ nguyên kết quả)
**Giả thiết.**

- $V_2=E$ và $\oplus:E\times E\to E$ là phép gộp kết hợp, giao hoán (Định nghĩa 02.1).
- Có hàm hoàn tất $\phi:E\to V_3$ sao cho với mọi khóa $k$ và mọi danh sách khác rỗng $L$, $\mathrm{Reduce}(k,L)=\big((k,\phi(\bigoplus L))\big)$.
- Mỗi lần gọi Combine trên $(k,L)$ phát đúng một cặp $(k,\bigoplus L)$.

**Kết luận.** Với mọi cách hệ thống gọi Combine, kể cả không gọi lần nào, tác vụ Reduce nhận cho khóa $k$ một danh sách $L'_k$ thỏa $\bigoplus L'_k=\bigoplus L_k$, và $\mathrm{Reduce}(k,L'_k)=\mathrm{Reduce}(k,L_k)$. Do đó đầu ra của công việc như khi không có Combine.

**Điều kiện áp dụng.** Các giả thiết của Mệnh đề 02.11; phép gộp được tính chính xác.

**Phạm vi.** Mệnh đề nói về kết quả, không nói Combine làm giảm bao nhiêu cặp.
:::

::: proof
Ý tưởng là một bất biến trên danh sách các giá trị của khóa $k$ còn chờ gửi tới Reduce.

**Bước 1 (bất biến).** Gọi $M_k$ là dãy nối, qua mọi tác vụ Map, các giá trị của khóa $k$ đang chờ gửi. Bất biến: $M_k$ khác rỗng và $\bigoplus M_k=\bigoplus L_k$. Trước lần gọi Combine đầu tiên, $M_k$ là đầu ra của Map, tức $M_k$ là một hoán vị của $L_k$; theo Bổ đề 02.2(b), bất biến đúng.

**Bước 2 (một lần gọi Combine giữ bất biến).** Một lần gọi nhận một phần $L$ khác rỗng của $M_k$ và thay $L$ bằng một phần tử $\bigoplus L$. Gọi $M'_k$ là dãy sau khi thay. Phân hoạch các vị trí của $M_k$ thành nhóm các vị trí của $L$ và các nhóm một phần tử cho mọi vị trí còn lại. Theo Bổ đề 02.2(c), $\bigoplus M_k$ bằng phép gộp của $\bigoplus L$ với các phần tử còn lại; theo Bổ đề 02.2(b), phép gộp này không phụ thuộc vị trí của $\bigoplus L$ trong dãy, nên bằng $\bigoplus M'_k$. Combine giữ khóa $k$, nên phần tử mới vẫn thuộc nhóm của $k$; giữ kiểu $E$, nên phép gộp tiếp theo vẫn xác định; $M'_k$ có ít nhất phần tử $\bigoplus L$, nên khác rỗng.

**Bước 3 (kết thúc).** Số lần gọi Combine hữu hạn. Theo quy nạp trên số lần gọi, khi các cặp được gửi đi, danh sách $L'_k=M_k$ mà Reduce nhận thỏa $\bigoplus L'_k=\bigoplus L_k$, và
$$
\begin{aligned}
&\mathrm{Reduce}(k,L'_k)\\
&\quad=\Big(\big(k,\phi(\textstyle\bigoplus L'_k)\big)\Big)\\
&\quad=\Big(\big(k,\phi(\textstyle\bigoplus L_k)\big)\Big)\\
&\quad=\mathrm{Reduce}(k,L_k).
\end{aligned}
$$
Điều này đúng với mọi khóa, nên theo Mệnh đề 02.11, đầu ra của công việc như khi không có Combine. $\square$
:::

Đếm từ là trường hợp $E=\mathbb N$, $\oplus=+$ và $\phi$ là hàm đồng nhất; khi đó Combine và Reduce dùng chung một hàm. Phép lấy giá trị lớn nhất với $\phi$ đồng nhất cũng thỏa mệnh đề. Mệnh đề 02.15 tổng quát hơn điều kiện "Reduce kết hợp và giao hoán" của MMDS (§2.2.4, tr.27) ở chỗ cho phép $\phi$, và nó dùng Bổ đề 02.2 cho từng lần gọi Combine.

Các giả thiết của Mệnh đề 02.15 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "kết hợp": dùng trung bình hai số $\mathrm{tb}$ của Mục 1.2 làm phép gộp trên dãy $2,4,9$, với tác vụ Map 1 giữ $[2,4]$ và tác vụ Map 2 giữ $[9]$. Combine phát 3 và 9, Reduce lấy trung bình được 6, còn trung bình đúng là 5.
- Bỏ "giao hoán": dùng phép "lấy phần tử đầu" của Mục 1.2 làm phép gộp. Với hai tác vụ Map phát (mèo, 2) và (mèo, 4), Reduce phát 2 hoặc 4 tùy cặp nào tới trước.
- Bỏ dạng $\phi(\bigoplus L)$: một hàm Reduce phát độ dài danh sách, dùng cùng Combine cộng của đếm từ. Không có Combine, $L_{\text{mèo}}=[1,1]$ và Reduce phát 2; có Combine, $L_{\text{mèo}}=[2]$ và Reduce phát 1.
- Bỏ điều kiện giữ khóa của Định nghĩa 02.14: một Combine đổi khóa (chó, 1) thành (chó!, 1) tạo một nhóm mới, và đầu ra có thêm một cặp lạ.
- Bỏ điều kiện giữ kiểu của Định nghĩa 02.14: một Combine của đếm từ phát cặp số (tổng, số phần tử) thay cho một số; phép cộng của Reduce không xác định trên kiểu đó.

Bước 1 và Bước 2 dùng tính kết hợp và giao hoán qua Bổ đề 02.2; Bước 2 dùng hai điều kiện giữ khóa và giữ kiểu; Bước 3 dùng dạng $\phi(\bigoplus L)$ của Reduce.

::: remark Nhận xét 02.16 (Trong thực hành: Combine)
Hàm Combine thường là chính hàm Reduce, và chỉ dùng được như vậy khi hàm Reduce kết hợp và giao hoán (trang chiếu MMDS, tr.30).

Combine không giảm số cặp khi một tác vụ Map không có khóa lặp: tác vụ Map 2 của Ví dụ 02.5 gửi 2 cặp như khi không có Combine. Đổi lại, Combine tốn thêm phép cộng ở phía Map; nó có lợi khi thời gian truyền tiết kiệm được lớn hơn thời gian tính thêm. Vì hệ thống có thể gọi Combine số lần khác nhau giữa hai lần chạy cùng một công việc, số cặp sau Combine không cố định, còn đầu ra cuối thì cố định theo Mệnh đề 02.15.
:::

::: exercise Bài tập 02.1 (Lệch tải giữa các reducer trong đếm từ; MMDS Bài 2.2.1, §2.2.7, tr.30)
Chạy đếm từ theo Thuật toán 02.9 trên một kho lớn như một bản sao của web, với 100 tác vụ Map và một số tác vụ Reduce.

- (a) Không dùng Combine ở các tác vụ Map. Thời gian xử lý danh sách giá trị của các reducer có chênh lệch đáng kể không? Giải thích.
- (b) Gộp ngẫu nhiên các reducer vào một số ít tác vụ Reduce, chẳng hạn 10 tác vụ. Lệch tải giữa các tác vụ có đáng kể không? Nếu gộp vào $10\,000$ tác vụ Reduce thì sao?
- (c) Dùng Combine ở 100 tác vụ Map. Lệch tải có đáng kể không? Giải thích.
:::

::: hint
Thời gian của reducer cho từ $w$ tỷ lệ với $\lvert L_w\rvert$. So tải của từ phổ biến nhất với tải trung bình của một tác vụ Reduce.
:::

::: solution
**Mô hình.** Để định lượng, giả sử tần suất từ theo định luật Zipf (MMDS, §1.3.6, tr.16): xếp các từ theo số lần xuất hiện giảm dần, từ thứ $\xi$ xuất hiện $\alpha\xi^{-1/2}$ lần với hằng số $\alpha>0$; kho có $D$ từ phân biệt.

**Câu (a).** Không có Combine, $\lvert L_w\rvert=c(w)$ theo Hệ quả 02.12. Từ thứ nhất có danh sách dài $\alpha$, từ thứ $\xi$ có danh sách dài $\alpha\xi^{-1/2}$, tức ngắn hơn $\sqrt\xi$ lần; từ thứ $10^6$ có danh sách ngắn hơn từ thứ nhất $1000$ lần. Thời gian các reducer vì vậy chênh lệch đáng kể.

**Câu (b).** Tổng số lần xuất hiện là $N=\alpha\sum_{\xi=1}^{D}\xi^{-1/2}$. Vì $\xi^{-1/2}$ giảm, so tổng với tích phân cho
$$
\begin{aligned}
\sum_{\xi=1}^{D}\xi^{-1/2}&\ge2\sqrt{D+1}-2,\\
\sum_{\xi=1}^{D}\xi^{-1/2}&\le2\sqrt D-1 .
\end{aligned}
$$
Với $r$ tác vụ chia khóa ngẫu nhiên, mỗi tác vụ có tải trung bình $N/r$, và tác vụ nhận từ thứ nhất có tải ít nhất $\alpha$. Tỷ số giữa $\alpha$ và tải trung bình thỏa
$$
\begin{aligned}
\frac{r\alpha}{N}&\ge\frac{r}{2\sqrt D-1},\\
\frac{r\alpha}{N}&\le\frac{r}{2\sqrt{D+1}-2}.
\end{aligned}
$$

- Với $r=10$: tỷ số không quá $10/(2\sqrt{D+1}-2)$, tức không quá $0{,}01$ khi $D\ge251\,000$ và không quá $0{,}051$ khi $D\ge10^4$. Từ phổ biến nhất chỉ thêm vài phần trăm tải trung bình vào tác vụ chứa nó, các từ khác còn nhỏ hơn, và mỗi tác vụ gồm khoảng $D/10$ từ nên tổng của các tác vụ gần nhau. Lệch tải không đáng kể; đây là hiệu ứng lấy trung bình của hộp tr.28 của MMDS.
- Với $r=10\,000$, mỗi tác vụ chỉ còn khoảng $D/10\,000$ từ để lấy trung bình, và hai cận cho ba trường hợp:
  - cận dưới $10\,000/(2\sqrt D-1)$ không nhỏ hơn 1 khi $D\le25\,005\,000$; khi đó tác vụ chứa từ phổ biến nhất có tải ít nhất khoảng gấp đôi trung bình, và lệch tải đáng kể;
  - cận dưới lớn hơn $0{,}01$ khi $D\le250\,000\,500\,000$; khi đó từ phổ biến nhất thêm hơn 1% tải trung bình vào tác vụ chứa nó, nên theo cùng ngưỡng 1% như với $r=10$, phần thêm không còn nhỏ;
  - cận trên $10\,000/(2\sqrt{D+1}-2)$ không quá $0{,}01$ khi $D\ge250\,001\,000\,000$; khi đó phần thêm không quá 1%.

  Nếu $D$ nằm giữa hai ngưỡng của hai trường hợp cuối thì hai cận không quyết định được tỷ số so với 1%.
- Theo hộp tr.28 của MMDS, khi số tác vụ Reduce lớn hơn số máy, một tác vụ dài chiếm trọn một máy trong khi nhiều tác vụ ngắn chạy lần lượt trên các máy khác; lệch giữa các máy vì vậy nhỏ hơn lệch giữa các tác vụ.

**Câu (c).** Với Combine gọi một lần cho mỗi khóa trên đầu ra của mỗi tác vụ Map, mỗi tác vụ Map gửi nhiều nhất một cặp cho mỗi từ. Do đó $\lvert L_w\rvert\le100$ với mọi $w$, và mỗi reducer làm không quá 99 phép cộng khi tổng khởi tạo bằng phần tử đầu, hay 100 phép khi khởi tạo bằng 0. Danh sách dài nhất chỉ có 100 phần tử, nên thời gian của mọi reducer đều nhỏ, và chênh lệch giữa chúng không còn đáng kể. Phần việc đếm của từ phổ biến chuyển sang các tác vụ Map, mỗi tác vụ xử lý một phần kho cùng cỡ.

**Kiểm tra lại.** Với $D=10^6$, tính trực tiếp $\sum_{\xi=1}^{D}\xi^{-1/2}\approx1998{,}54$, nằm giữa hai cận $1998{,}00$ và $1999$. Câu (c) nhất quán với Mệnh đề 02.15: Combine không đổi số đếm, chỉ đổi độ dài danh sách.
:::

Như vậy, chúng ta đã có mô hình MapReduce gồm hàm Map, hàm Reduce và phép nhóm theo khóa (Định nghĩa 02.6–02.8), Thuật toán 02.10 cho một công việc và Mệnh đề 02.11 cho phần khung bảo đảm: mỗi khóa gặp đủ giá trị của nó đúng một lần. Đếm từ đúng theo Hệ quả 02.12, và Combine giữ nguyên kết quả khi Reduce có dạng $\phi(\bigoplus L)$ với $\oplus$ kết hợp, giao hoán (Mệnh đề 02.15). Tuy nhiên, đếm từ có khóa và giá trị cho sẵn: khóa là từ, giá trị là số đếm. Với bài toán khác, khóa và giá trị trung gian phải được chọn sao cho Reduce tính được kết quả và Combine dùng được. Trong Mục 3, chúng ta chọn chúng cho ba bài toán.

<!-- note-topic-id: lec-02-topic-08 -->
## 3. Các ví dụ MapReduce

Ba bài toán của mục đòi ba kiểu giá trị trung gian khác nhau: một tích của phần tử ma trận với thành phần véc-tơ, một dấu hiệu "từ này có mặt", và một cặp tổng–số lượng. Tính đúng của cả ba được chứng minh bằng Mệnh đề 02.11 cho phần khung và Mệnh đề 02.15 cho Combine.

### 3.1 Nhân ma trận–véc-tơ

Xếp hạng trang web theo PageRank lặp đi lặp lại phép nhân một ma trận với một véc-tơ, và số chiều ở đó cỡ hàng nghìn tỷ (MMDS, tr.31). Ma trận này thưa, trung bình 10–15 phần tử khác 0 mỗi hàng, vì phần tử ở hàng $i$, cột $j$ khác 0 khi và chỉ khi trang $j$ có liên kết tới trang $i$; một ma trận đặc cạnh $10^{12}$ có $10^{24}$ phần tử và không lưu được (MMDS, chú thích 3, tr.31). MapReduce của Google được tạo ra trước hết để thực hiện các phép nhân ma trận–véc-tơ cỡ này (MMDS, tr.31). Như MMDS, chúng ta đặc tả bài toán cho ma trận vuông.

::: definition Định nghĩa 02.17 (Bài toán nhân ma trận–véc-tơ)
**Đầu vào.** Ma trận vuông $A=(a_{ij})\in\mathbb R^{q\times q}$ với $q\ge1$, lưu thành các bản ghi $(i,j,a_{ij})$, mỗi tọa độ $(i,j)$ với $1\le i,j\le q$ đúng một bản ghi, kể cả khi $a_{ij}=0$; véc-tơ $v=(v_1,\ldots,v_q)\in\mathbb R^q$.

**Đầu ra.** Véc-tơ $y=Av\in\mathbb R^q$ dưới dạng $q$ cặp $(i,y_i)$, với
$$
y_i=\sum_{j=1}^{q}a_{ij}v_j,\qquad 1\le i\le q.
$$

**Giả thiết.** $v$ vừa bộ nhớ của mỗi máy chạy tác vụ Map; các phép toán số học chính xác.
:::

Đầu ra có một thành phần $y_i$ cho mỗi hàng, và $y_i$ là tổng của $q$ tích $a_{ij}v_j$ nằm trên hàng $i$ của $A$. Các bản ghi của hàng $i$ có thể nằm ở nhiều khối DFS khác nhau, nên các tích của cùng một hàng phải được đưa về một chỗ, như các lần xuất hiện của cùng một từ ở Mục 2. Giả thiết bộ nhớ cho phép mỗi tác vụ Map đọc $v$ một lần rồi tra $v_j$ cho mọi bản ghi của nó (MMDS, §2.3.1, tr.31).

Một bản ghi cho một bước tính tay. Xét bản ghi $(2,3,2)$ ở hàng 2, cột 3, với $v_3=3$; Map tính $2\cdot3=6$ và phát cặp $(2,6)$. Khóa là chỉ số hàng 2 vì 6 là một số hạng của $y_2$. Thuật toán sau làm bước đó cho mọi bản ghi.

::: algorithm Thuật toán 02.18 (Nhân ma trận–véc-tơ)
**Đầu vào.** Các bản ghi $(i,j,a_{ij})$ của $A$, chia thành $m$ phần; véc-tơ $v$ trong bộ nhớ của mỗi tác vụ Map.

**Đầu ra.** Các cặp $(i,y_i)$, $1\le i\le q$.

**Giả thiết.** Như Định nghĩa 02.17.

1. Mỗi tác vụ Map đọc $v$ vào bộ nhớ một lần.
2. $\mathrm{Map}$ trên bản ghi $(i,j,a_{ij})$: phát $(i,a_{ij}v_j)$.
3. $\mathrm{Combine}(i,L)$: phát $(i,\sum_{x\in L}x)$.
4. $\mathrm{Reduce}(i,L)$: phát $(i,\sum_{x\in L}x)$.

**Dừng.** Mỗi phần có hữu hạn bản ghi; mỗi danh sách hữu hạn.

**Trường hợp biên.** Một hàng toàn số 0 vẫn có $q$ bản ghi, nên vẫn có nhóm và Reduce phát $(i,0)$.

**Chi phí.** Mô hình đếm phép toán số học, không có Combine, mỗi tổng khởi tạo bằng phần tử đầu như Mệnh đề 02.29:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| Đọc $v$ (bước 1) | $m$ tác vụ Map | $q$ thành phần | $mq$ thành phần đọc |
| Map (bước 2) | $q^2$ bản ghi | 1 phép nhân | $q^2$ phép nhân |
| Reduce (bước 4) | $q$ hàng | $q-1$ phép cộng | $q(q-1)$ phép cộng |

Có Combine, tổng số phép cộng ở Combine và Reduce vẫn là $q(q-1)$, chỉ chuyển một phần sang phía Map.
:::

```text
Map(phần của A):            # v đã nằm trong bộ nhớ
    với mỗi bản ghi (i, j, a_ij):
        phát (i, a_ij * v[j])
Combine(i, L): phát (i, tổng các phần tử của L)
Reduce(i, L):  phát (i, tổng các phần tử của L)
```

Thao tác quyết định là chọn khóa $i$ ở bước 2: mọi số hạng của $y_i$ mang cùng khóa nên gặp nhau ở một reducer. Combine và Reduce là cùng một phép cộng, nên Combine được phép theo Mệnh đề 02.15 với $\oplus=+$, $\phi$ đồng nhất.

::: example Ví dụ 02.6 (Ma trận $4\times4$ chia bốn khối con)
**Dữ kiện.**
$$
\begin{gathered}
A=\left[\begin{array}{cc|cc}1&2&0&1\\0&1&2&0\\\hline2&0&1&1\\1&1&0&2\end{array}\right],\\
v=(1,2,3,4).
\end{gathered}
$$
Các bản ghi của $A$ chia thành bốn khối con $2\times2$: $A_{11}$ gồm hàng 1–2, cột 1–2; $A_{12}$ gồm hàng 1–2, cột 3–4; $A_{21}$ gồm hàng 3–4, cột 1–2; $A_{22}$ gồm hàng 3–4, cột 3–4. Mỗi khối con là một phần, giao cho một tác vụ Map; chỉ số $i,j$ trong bản ghi là chỉ số của cả ma trận.

**Map và Combine.**

| Khối con | Cặp Map phát | Combine phát |
|---|---|---|
| $A_{11}$ | $(1,1\cdot1),(1,2\cdot2),(2,0\cdot1),(2,1\cdot2)$ = $(1,1),(1,4),(2,0),(2,2)$ | $(1,5),(2,2)$ |
| $A_{12}$ | $(1,0\cdot3),(1,1\cdot4),(2,2\cdot3),(2,0\cdot4)$ = $(1,0),(1,4),(2,6),(2,0)$ | $(1,4),(2,6)$ |
| $A_{21}$ | $(3,2\cdot1),(3,0\cdot2),(4,1\cdot1),(4,1\cdot2)$ = $(3,2),(3,0),(4,1),(4,2)$ | $(3,2),(4,3)$ |
| $A_{22}$ | $(3,1\cdot3),(3,1\cdot4),(4,0\cdot3),(4,2\cdot4)$ = $(3,3),(3,4),(4,0),(4,8)$ | $(3,7),(4,8)$ |

Map phát 16 cặp, kể cả bốn tích bằng 0; Combine còn 8 cặp.

**Nhóm và Reduce.** $L_1=[5,4]$, $L_2=[2,6]$, $L_3=[2,7]$, $L_4=[3,8]$; Reduce phát $(1,9)$, $(2,8)$, $(3,9)$, $(4,11)$.

**Kiểm tra lại.** Tính trực tiếp từng hàng: $1+4+0+4=9$, $0+2+6+0=8$, $2+0+3+4=9$, $1+2+0+8=11$. Vậy $y=(9,8,9,11)$.
:::

![Bên trái là ma trận A cỡ 4 × 4 với các hàng 1, 2, 0, 1; 0, 1, 2, 0; 2, 0, 1, 1; 1, 1, 0, 2, chia bằng nét đậm thành bốn khối A₁₁, A₁₂ ở trên và A₂₁, A₂₂ ở dưới, cạnh đó là v = (1, 2, 3, 4). Cột giữa ghi các cặp Combine phát trong mỗi khối: A₁₁ cho (1, 5), (2, 2); A₁₂ cho (1, 4), (2, 6); A₂₁ cho (3, 2), (4, 3); A₂₂ cho (3, 7), (4, 8). Cột phải là Reduce theo khóa hàng: i = 1 nhận [5, 4], y₁ = 9; i = 2 nhận [2, 6], y₂ = 8; i = 3 nhận [2, 7], y₃ = 9; i = 4 nhận [3, 8], y₄ = 11.](img/lec-02/note-ma-tran-khoi.svg)

Trên hình, mỗi khóa hàng nhận đúng hai tổng bộ phận, một từ mỗi khối con mà hàng đó cắt qua, chẳng hạn $5$ từ $A_{11}$ và $4$ từ $A_{12}$ cho $i=1$. Tổng $5+4$ chỉ được tính ở Reduce, giống cặp (chó, 1) từ hai tác vụ Map ở Ví dụ 02.5.

::: proposition Mệnh đề 02.19 (Tính đúng của nhân ma trận–véc-tơ)
**Giả thiết.** Đầu vào thỏa Định nghĩa 02.17; công việc dùng Thuật toán 02.18 và thỏa các giả thiết của Mệnh đề 02.11.

**Kết luận.** Đầu ra gồm đúng $q$ cặp $(i,y_i)$ với $y_i=\sum_{j=1}^{q}a_{ij}v_j$, có hay không có Combine.

**Điều kiện áp dụng.** Số học chính xác; mỗi tọa độ đúng một bản ghi.

**Phạm vi.** Mệnh đề không dùng giả thiết $v$ vừa bộ nhớ; giả thiết đó chỉ ảnh hưởng chi phí.
:::

::: proof
**Bước 1 (danh sách của hàng $i$).** Mỗi tọa độ $(i,j)$ có đúng một bản ghi, và theo Mệnh đề 02.11, Map được gọi đúng một lần cho bản ghi đó, phát $(i,a_{ij}v_j)$. Vậy khóa của $Z$ là $1,\ldots,q$, và khi không có Combine, $L_i$ là một hoán vị của $(a_{i1}v_1,\ldots,a_{iq}v_q)$.

**Bước 2 (giá trị Reduce).** Reduce cộng các phần tử của $L_i$; phép cộng không phụ thuộc thứ tự, nên Reduce phát $(i,\sum_{j}a_{ij}v_j)=(i,y_i)$.

**Bước 3 (Combine).** Combine và Reduce có dạng của Mệnh đề 02.15 với $E=\mathbb R$, $\oplus=+$, $\phi$ đồng nhất, nên có Combine thì đầu ra không đổi. $\square$
:::

Các lựa chọn và giả thiết của thiết kế có vai trò riêng, và mỗi điều bị bỏ đều có phản ví dụ trên Ví dụ 02.6.

- Bỏ khóa hàng, dùng khóa cột $j$: nhóm của cột $j$ gồm các tích $a_{1j}v_j,\ldots,a_{qj}v_j$, là các số hạng của $q$ thành phần khác nhau. Nhóm của cột 1 là $[1,0,2,1]$, tổng bằng 4, không xuất hiện trong $y=(9,8,9,11)$.
- Bỏ "mỗi tọa độ đúng một bản ghi": nếu bản ghi $(1,2,2)$ có mặt hai lần, $L_1$ có hai số 4 và $y_1=13$.

Bước 1 của chứng minh dùng giả thiết mỗi tọa độ một bản ghi; Bước 2 dùng việc khóa là hàng.

::: remark Nhận xét 02.20 (Trong thực hành: ma trận thưa và véc-tơ lớn)
- Ma trận của PageRank chỉ lưu phần tử khác 0. Khi đó một hàng toàn số 0 không có bản ghi, không có nhóm, và đầu ra thiếu cặp $(i,0)$; chương trình chính phải coi mọi hàng vắng mặt là $y_i=0$.
- Khi $v$ không vừa bộ nhớ, thuật toán vẫn đúng nhưng mỗi tác vụ Map phải đưa từng phần của $v$ từ đĩa vào bộ nhớ nhiều lần; Tình huống 02.3 nêu cách chia dải dọc của MMDS (§2.3.2, tr.32) và chi phí của nó.
- Với số dấu phẩy động, các tổng bộ phận của Combine có thể làm $y_i$ khác ở các chữ số cuối so với tổng theo thứ tự cột, như ví dụ $0{,}1+0{,}2+0{,}3$ ở Mục 1.2.
:::

<!-- note-topic-id: lec-02-topic-09 -->
### 3.2 Đếm từ phân biệt

Văn bản $d_1=$ "mèo chó mèo" có 2 từ phân biệt, $d_2=$ "chó chim" cũng có 2, nhưng cả kho chỉ có 3 từ phân biệt: mèo, chó, chim. Cộng số từ phân biệt của từng văn bản cho $2+2=4$, sai vì chó có mặt ở cả hai văn bản. Số từ phân biệt không gộp được bằng phép cộng; ta cần loại trùng trước rồi mới đếm.

::: definition Định nghĩa 02.21 (Bài toán đếm từ phân biệt)
**Đầu vào.** $n\ge0$ văn bản $d_1,\ldots,d_n$ đã tách từ theo cùng một quy tắc; $\mathcal W_i$ là tập từ của $d_i$.

**Đầu ra.** Số từ phân biệt của kho,
$$
D=\Big\lvert\bigcup_{i=1}^{n}\mathcal W_i\Big\rvert .
$$
Khi mọi văn bản rỗng, $D=0$.
:::

$D$ bằng $\lvert\mathcal W\rvert$ của Định nghĩa 02.5, nhưng bài toán chỉ cần một số, không cần số đếm của từng từ. Hợp các tập ở công thức đếm mỗi từ một lần dù nó có mặt ở bao nhiêu văn bản; tổng $\sum_i\lvert\mathcal W_i\rvert$ thì đếm một từ một lần cho mỗi văn bản chứa nó. Hai đại lượng bằng nhau khi và chỉ khi các tập $\mathcal W_i$ đôi một rời nhau.

Bước tính tay đầu tiên là loại trùng tại chỗ. Tác vụ Map đọc $d_1$ phát (mèo, 1), (chó, 1), (mèo, 1); nếu nhóm theo từ, mèo có danh sách $[1,1]$. Điều cần biết chỉ là mèo có mặt, nên danh sách đó được thay bằng một cặp (mèo, 1). Làm như vậy cho mọi từ trên cả kho được đúng một cặp cho mỗi từ phân biệt, rồi chỉ còn đếm số cặp. Hai bước dùng hai khóa khác nhau, nên cần hai công việc nối tiếp, gọi bởi một **chương trình chính** (driver): chương trình chạy ngoài khung MapReduce, gọi lần lượt các công việc và đọc đầu ra của chúng.

::: algorithm Thuật toán 02.22 (Đếm từ phân biệt bằng hai công việc)
**Đầu vào.** $n$ văn bản như Định nghĩa 02.21.

**Đầu ra.** Số $D$.

**Giả thiết.** Các giả thiết của Mệnh đề 02.11 cho cả hai công việc; $g$ là một khóa cố định, không phải một từ.

| Hàm | Công việc 1: loại trùng, khóa $w$ | Công việc 2: đếm, khóa $g$ |
|---|---|---|
| Map | với mỗi lần từ $w$ xuất hiện, phát $(w,1)$ | nhận $(w,1)$, phát $(g,1)$ |
| Combine | nhận $(w,L)$, phát $(w,1)$ | nhận $(g,L)$, phát $(g,\sum_{x\in L}x)$ |
| Reduce | nhận $(w,L)$, phát $(w,1)$ | nhận $(g,L)$, phát $(g,\sum_{x\in L}x)$ |

1. Chương trình chính chạy công việc 1 trên các văn bản.
2. Nếu công việc 1 không có cặp đầu ra, chương trình chính trả $D=0$ và dừng.
3. Chương trình chính chạy công việc 2 trên đầu ra của công việc 1; giá trị của cặp đầu ra duy nhất $(g,\cdot)$ là $D$.

**Dừng.** Mỗi công việc dừng theo Mệnh đề 02.11.

**Trường hợp biên.** Mọi văn bản rỗng: công việc 1 không phát cặp nào, và Reduce không được gọi cho danh sách rỗng, nên bước 2 trả 0.

**Chi phí.** Công việc 1 có $\sum_i\ell_i$ cặp trung gian khi không Combine và $D$ cặp đầu ra; công việc 2 có $D$ cặp trung gian khi không Combine và một cặp đầu ra.
:::

Hai hàm Combine có hai vai khác nhau: ở công việc 1, Combine giữ dấu hiệu có mặt; ở công việc 2, Combine giữ tổng.

::: example Ví dụ 02.7 (Vết chạy đếm từ phân biệt)
**Dữ kiện.** $d_1=$ "mèo chó mèo" ở tác vụ Map 1, $d_2=$ "chó chim" ở tác vụ Map 2 của công việc 1; Combine gọi một lần cho mỗi khóa trên toàn bộ đầu ra của mỗi tác vụ.

**Công việc 1.**

| Bước | Dữ liệu |
|---|---|
| Map | 5 cặp: (mèo, 1), (chó, 1), (mèo, 1) từ $d_1$; (chó, 1), (chim, 1) từ $d_2$ |
| Combine | 4 cặp: (mèo, 1), (chó, 1) từ $d_1$; (chó, 1), (chim, 1) từ $d_2$ |
| Nhóm | mèo: $[1]$; chó: $[1,1]$; chim: $[1]$ |
| Reduce | 3 cặp: (mèo, 1), (chó, 1), (chim, 1) |

**Công việc 2.** Map phát $(g,1)$ ba lần; nhóm $L_g=[1,1,1]$; Reduce phát $(g,3)$.

**Kết quả.** $D=3$.

**Kiểm tra lại.** $\mathcal W_1\cup\mathcal W_2=\{\text{mèo},\text{chó}\}\cup\{\text{chó},\text{chim}\}=\{\text{mèo},\text{chó},\text{chim}\}$ có 3 phần tử; $\lvert\mathcal W_1\rvert+\lvert\mathcal W_2\rvert=4$ đếm chó hai lần.
:::

![Hai khung đọc từ trái sang phải. Khung trái là công việc 1 với khóa là từ: Map phát 5 cặp, d₁ cho (mèo, 1), (chó, 1), (mèo, 1), d₂ cho (chó, 1), (chim, 1); Combine còn 4 cặp; Reduce nhận mèo [1], chó [1, 1], chim [1] và phát đúng một cặp (w, 1) cho mỗi từ phân biệt, 3 cặp. Khung phải là công việc 2 với khóa chung g: Map đổi mỗi cặp thành (g, 1), nhóm g có [1, 1, 1], Reduce phát (g, 3), nên D = 3. Dòng cuối: cộng số từ phân biệt của từng văn bản cho 2 + 2 = 4 vì chó bị đếm hai lần.](img/lec-02/note-hai-cong-viec.svg)

Trên hình, Combine loại được lần lặp của mèo trong $d_1$ nhưng không loại được hai cặp (chó, 1) ở hai tác vụ; Reduce của công việc 1 làm việc đó, và công việc 2 chỉ đếm các cặp còn lại.

::: proposition Mệnh đề 02.23 (Tính đúng của đếm từ phân biệt)
**Giả thiết.** Đầu vào thỏa Định nghĩa 02.21; hai công việc của Thuật toán 02.22 thỏa các giả thiết của Mệnh đề 02.11.

**Kết luận.** Thuật toán 02.22 trả đúng $D$, có hay không có Combine ở mỗi công việc.

**Điều kiện áp dụng.** Mọi văn bản dùng cùng một quy tắc tách từ.

**Phạm vi.** Mệnh đề không quy định số công việc tối thiểu; nó chứng minh tính đúng của phương án hai công việc.
:::

::: proof
**Bước 1 (đầu ra công việc 1).** Map phát $(w,1)$ cho mỗi lần xuất hiện, nên tập khóa của $Z$ là $\bigcup_i\mathcal W_i$. Theo Mệnh đề 02.11, Reduce được gọi đúng một lần cho mỗi khóa đó và phát đúng một cặp $(w,1)$. Vậy đầu ra của công việc 1 có đúng một cặp cho mỗi từ phân biệt.

**Bước 2 (Combine của công việc 1).** Trên $E=\{1\}$, phép $x\oplus y=1$ kết hợp và giao hoán, và $\bigoplus L=1$ với mọi danh sách khác rỗng. Combine và Reduce của công việc 1 có dạng của Mệnh đề 02.15 với $\phi$ đồng nhất, nên Combine không đổi đầu ra của công việc 1.

**Bước 3 (công việc 2).** Công việc 2 nhận $\lvert\bigcup_i\mathcal W_i\rvert=D$ cặp và Map đổi mỗi cặp thành $(g,1)$. Khi $D\ge1$, khóa $g$ có danh sách gồm $D$ số 1 và Reduce phát $(g,D)$; Combine là phép cộng, đúng theo Mệnh đề 02.15. Khi $D=0$, bước 2 của thuật toán trả 0. $\square$
:::

Công việc 1 chính là phép loại trùng của MMDS: Reduce biến một khóa cùng danh sách các bản lặp của nó thành một cặp duy nhất (§2.3.5, tr.36). MMDS ghi rằng phép loại trùng kết hợp và giao hoán, nên Combine loại được các bản trùng sinh ra trong một tác vụ Map, nhưng Reduce vẫn cần để loại hai bản trùng đến từ hai tác vụ Map khác nhau.

Một phương án khác dùng một công việc với một tác vụ Reduce giữ cả tập từ trong bộ nhớ; nó cũng đúng nhưng cần bộ nhớ tỷ lệ với $D$ ở một máy, trái với ngân sách của bài toán khi $D$ lớn.

**Trong thực hành.** Biểu diễn kho trang web bằng một ma trận trang–từ, mỗi hàng một trang và mỗi cột một từ, cần biết số cột, tức số từ phân biệt của kho sau một quy tắc tách từ cố định. Với hai văn bản của Ví dụ 02.7, $D=3$ nên ma trận có 3 cột, ứng với mèo, chó, chim. Gán mỗi từ một chỉ số cột là một bước riêng, dùng đầu ra của công việc 1.

::: exercise Bài tập 02.2 (Loại trùng có tính kết hợp và giao hoán; MMDS Bài 2.3.6, §2.3.11, tr.41)
MMDS (§2.3.5) khẳng định phép loại trùng có tính kết hợp và giao hoán. Gọi một danh sách là **không lặp** khi mỗi phần tử có mặt trong nó nhiều nhất một lần, và hai danh sách không lặp là **bằng nhau đến hoán vị** khi chúng có cùng tập phần tử. Với hai danh sách không lặp $L,L'$, định nghĩa $L\odot L'$ là danh sách không lặp có tập phần tử $\mathrm{set}(L)\cup\mathrm{set}(L')$, xác định đến hoán vị; đây là kết quả loại trùng trên danh sách nối $L\cdot L'$.

Chứng minh $\odot$ giao hoán và kết hợp, đến hoán vị.
:::

::: hint
Một danh sách không lặp được xác định, đến hoán vị, bởi tập phần tử của nó; chuyển mọi đẳng thức về đẳng thức giữa các tập.
:::

::: solution
**Quy về tập.** Theo định nghĩa, $\mathrm{set}(L\odot L')=\mathrm{set}(L)\cup\mathrm{set}(L')$. Hai danh sách không lặp bằng nhau đến hoán vị khi và chỉ khi tập phần tử bằng nhau, nên chỉ cần so tập phần tử.

**Giao hoán.** $\mathrm{set}(L\odot L')=\mathrm{set}(L)\cup\mathrm{set}(L')=\mathrm{set}(L')\cup\mathrm{set}(L)=\mathrm{set}(L'\odot L)$, theo tính giao hoán của hợp tập.

**Kết hợp.** Với ba danh sách không lặp $L_1,L_2,L_3$ và $\Sigma_i=\mathrm{set}(L_i)$,
$$
\begin{aligned}
&\mathrm{set}\big((L_1\odot L_2)\odot L_3\big)\\
&\quad=(\Sigma_1\cup\Sigma_2)\cup\Sigma_3\\
&\quad=\Sigma_1\cup(\Sigma_2\cup\Sigma_3)\\
&\quad=\mathrm{set}\big(L_1\odot(L_2\odot L_3)\big),
\end{aligned}
$$
dòng thứ ba theo tính kết hợp của hợp tập.

**Áp vào Combine.** Áp Bổ đề 02.2 với $E$ là họ các tập hữu hạn và $\oplus=\cup$, vì $\mathrm{set}(L\odot L')=\mathrm{set}(L)\cup\mathrm{set}(L')$: loại trùng trong từng tác vụ Map rồi loại trùng các kết quả vẫn cho cùng một tập, nên Combine dùng được trong công việc 1 của Thuật toán 02.22.

**Kiểm tra lại.** Với $L=[\text{mèo},\text{chó}]$ và $L'=[\text{chó},\text{chim}]$, cả $L\odot L'$ và $L'\odot L$ có tập $\{\text{mèo},\text{chó},\text{chim}\}$; đó là ba cặp đầu ra của công việc 1 trong Ví dụ 02.7.
:::

<!-- note-topic-id: lec-02-topic-10 -->
### 3.3 Trung bình cộng và quy tắc chọn trạng thái

Dãy $2,4,9$ có trung bình $15/3=5$. Giả sử tác vụ Map 1 giữ $[2,4]$ và tác vụ Map 2 giữ $[9]$. Trung bình cục bộ là $3$ và $9$, và trung bình của hai số đó là $6$. Phép tính sai vì nhóm $[2,4]$ có hai phần tử nhưng được tính như nhóm $[9]$ một phần tử: trung bình cục bộ bỏ mất số phần tử của nhóm. Bổ đề 02.2 không áp được vì phép lấy trung bình hai số không kết hợp (Mục 1.2). Ta cần một giá trị trung gian giữ đủ thông tin để gộp.

::: definition Định nghĩa 02.24 (Bài toán trung bình cộng và trạng thái tổng–số lượng)
**Bài toán.** Đầu vào là dãy số thực $a_1,\ldots,a_n$ với $n\ge1$; đầu ra là trung bình cộng
$$
\mu=\frac1n\sum_{i=1}^{n}a_i .
$$
Dãy rỗng không có trung bình.

**Trạng thái.** Một **trạng thái tổng–số lượng** là cặp $(s,\kappa)\in\mathbb R\times\mathbb N_{\ge1}$, với $s$ là tổng và $\kappa\ge1$ là số phần tử của một nhóm khác rỗng các phần tử của dãy. Phép gộp hai trạng thái là phép cộng từng thành phần:
$$
\begin{aligned}
&(s,\kappa)\oplus(s',\kappa')\\
&\quad=(s+s',\ \kappa+\kappa').
\end{aligned}
$$
:::

Phép cộng từng thành phần đóng trên $\mathbb R\times\mathbb N_{\ge1}$, kết hợp và giao hoán, vì phép cộng trên mỗi thành phần có hai tính chất đó; vậy Bổ đề 02.2 áp được cho trạng thái. Trạng thái giữ đủ thông tin để gộp: từ $(s,\kappa)$ của hai nhóm rời nhau, tổng và số phần tử của nhóm hợp là $(s+s',\kappa+\kappa')$, còn từ hai trung bình $s/\kappa$, $s'/\kappa'$ thì không tính được trung bình của nhóm hợp khi không biết $\kappa,\kappa'$. Một bước tính tay: $(2,1)\oplus(4,1)=(6,2)$, và $6/2=3$ là trung bình của nhóm $[2,4]$.

::: algorithm Thuật toán 02.25 (Trung bình cộng)
**Đầu vào.** Dãy $a_1,\ldots,a_n$ với $n\ge1$, chia thành $m$ phần; một khóa chung $g$.

**Đầu ra.** Cặp $(g,\mu)$.

**Giả thiết.** Các giả thiết của Mệnh đề 02.11; số học chính xác.

1. $\mathrm{Map}$ trên phần tử $a_i$: phát $(g,(a_i,1))$.
2. $\mathrm{Combine}(g,L)$: phát $(g,\bigoplus L)$, với $\oplus$ của Định nghĩa 02.24.
3. $\mathrm{Reduce}(g,L)$: tính $(s^\ast,\kappa^\ast)=\bigoplus L$ rồi phát $(g,s^\ast/\kappa^\ast)$.

**Dừng.** Mọi danh sách hữu hạn.

**Trường hợp biên.** $n=1$ cho $L_g=[(a_1,1)]$ và $\mu=a_1$. Với $n=0$, không có nhóm nào và chương trình chính phải báo rằng trung bình không xác định.

**Chi phí.** Mô hình đếm phép toán số học, không có Combine, gộp khởi tạo bằng trạng thái đầu:

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| Map (bước 1) | $n$ phần tử | 1 lần phát | $n$ lần phát |
| Gộp ở Reduce (bước 3) | $n-1$ lần gộp | 2 phép cộng | $2(n-1)$ phép cộng |
| Chia ở Reduce (bước 3) | 1 | 1 phép chia | 1 phép chia |

Có Combine, số lần gộp vẫn là $n-1$, chia giữa Combine và Reduce; phép chia vẫn chỉ một lần.
:::

| Hàm | Đầu vào → cặp phát ra | Kiểu giá trị phát ra |
|---|---|---|
| Map | $a_i\ \longrightarrow\ (g,(a_i,1))$ | trạng thái $(s,\kappa)$ |
| Combine | $(g,L)\ \longrightarrow\ (g,\bigoplus L)$ | trạng thái $(s,\kappa)$ |
| Reduce | $(g,L)\ \longrightarrow\ (g,s^\ast/\kappa^\ast)$ | một số |

Thao tác quyết định là phép chia ở bước 3: nó chỉ được làm một lần, ở Reduce, sau khi mọi trạng thái đã gộp. Combine và Reduce ở đây khác nhau, khác với đếm từ và nhân ma trận.

::: example Ví dụ 02.8 (Trung bình của 2, 4, 9)
**Dữ kiện.** Tác vụ Map 1 giữ $[2,4]$, tác vụ Map 2 giữ $[9]$; $n=3$.

**Tác vụ Map 1.** Map phát $(g,(2,1))$, $(g,(4,1))$; Combine phát $(g,(6,2))$.

**Tác vụ Map 2.** Map phát $(g,(9,1))$; Combine phát lại cặp đó.

**Reduce.** $L_g=[(6,2),(9,1)]$, $(s^\ast,\kappa^\ast)=(15,3)$, phát $(g,15/3)=(g,5)$.

**Kiểm tra lại.** $(2+4+9)/3=5$. Chia sớm ở Combine cho $3$ và $9$, và trung bình của chúng là $6\ne5$.
:::

![Hai khung trái là hai tác vụ Map. Tác vụ Map 1 giữ [2, 4], gộp (2, 1) ⊕ (4, 1) = (6, 2) và Combine phát (g, (6, 2)); tác vụ Map 2 giữ [9] và phát (g, (9, 1)). Hai mũi tên dẫn tới Reduce: (6, 2) ⊕ (9, 1) = (15, 3), rồi μ = 15/3 = 5, ghi là đúng. Dưới đường kẻ đứt, một khung viền nét đứt màu đỏ ghi cách sai: chia sớm cho 3 và 9, trung bình của 3 và 9 là 6, khác 5.](img/lec-02/note-trang-thai-tong-so-luong.svg)

Hình đặt cách đúng ở trên và cách sai trong khung nét đứt ở dưới. Ở cách đúng, số $2$ trong cặp $(6,2)$ đi cùng tổng 6 tới Reduce, nên Reduce biết nhóm của tác vụ Map 1 có hai phần tử. Ở cách sai, thông tin đó mất ngay tại tác vụ Map.

::: proposition Mệnh đề 02.26 (Tính đúng của trung bình cộng)
**Giả thiết.** $n\ge1$; công việc dùng Thuật toán 02.25 và thỏa các giả thiết của Mệnh đề 02.11; số học chính xác.

**Kết luận.** Công việc phát đúng một cặp $(g,\mu)$, có hay không có Combine.

**Điều kiện áp dụng.** Mỗi phần tử của dãy thuộc đúng một phần đầu vào; hai phần tử bằng nhau ở hai vị trí là hai đóng góp.

**Phạm vi.** Mệnh đề không nói về sai số làm tròn khi dùng số dấu phẩy động.
:::

::: proof
**Bước 1 (bất biến).** Bất biến: mỗi trạng thái $(s,\kappa)$ đang chờ gửi hoặc đã tới Reduce là tổng và số phần tử của một nhóm vị trí của dãy, và các nhóm của các trạng thái khác nhau rời nhau. Khi Map phát $(a_i,1)$, nhóm là $\{i\}$, nên bất biến đúng.

**Bước 2 (gộp giữ bất biến).** Gộp hai trạng thái của hai nhóm rời nhau $G,G'$ cho $\big(\sum_{i\in G}a_i+\sum_{i\in G'}a_i,\ \lvert G\rvert+\lvert G'\rvert\big)$, đúng là tổng và số phần tử của $G\cup G'$; nhóm mới rời với mọi nhóm còn lại.

**Bước 3 (kết thúc).** Theo Mệnh đề 02.11, Reduce được gọi đúng một lần cho khóa $g$ với danh sách chứa trạng thái của mọi nhóm, và các nhóm đó phủ mọi vị trí $1,\ldots,n$. Theo Bước 2, $(s^\ast,\kappa^\ast)=(\sum_{i=1}^{n}a_i,\ n)$. Vì $n\ge1$, $\kappa^\ast>0$ và $s^\ast/\kappa^\ast=\mu$. Combine không đổi kết quả theo Mệnh đề 02.15, với $E=\mathbb R\times\mathbb N_{\ge1}$, $\oplus$ của Định nghĩa 02.24 và $\phi(s,\kappa)=s/\kappa$. $\square$
:::

Mệnh đề 02.26 là trường hợp của Mệnh đề 02.15 có hàm hoàn tất khác đồng nhất: Combine phát trạng thái, Reduce phát một số. Các giả thiết của nó có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $n\ge1$: với $n=0$, không có nhóm và Reduce không phát cặp nào; $\mu$ không xác định vì số phần tử bằng 0.
- Bỏ trạng thái đủ: dùng hàm Reduce, vốn phát $s/\kappa$, làm Combine; với $[2,4]$ và $[9]$, Combine phát 3 và 9, và Reduce không còn biết hai nhóm có 2 và 1 phần tử.
- Bỏ "mỗi phần tử thuộc đúng một phần": nếu số 9 được đọc hai lần, Reduce gộp được $(24,4)$ và phát $6$.

**Trong thực hành.** Với số dấu phẩy động, các tổng bộ phận $s$ có thể khác ở các chữ số cuối tùy cách chia dãy, như ví dụ $0{,}1+0{,}2+0{,}3$ ở Mục 1.2, còn thành phần $\kappa$ là số nguyên nên luôn chính xác.

::: example Ví dụ 02.9 (Số từ trung bình mỗi trang)
**Dữ kiện.** Hai trang web $d_1=$ "mèo chó mèo" và $d_2=$ "chó chim"; $a_i=\ell_i$ là số từ của trang $i$, tính cả từ lặp.

**Trạng thái.** Tác vụ Map của $d_1$ phát $(g,(3,1))$, tác vụ Map của $d_2$ phát $(g,(2,1))$; Reduce gộp được $(5,2)$.

**Kết quả.** $\mu=5/2=2{,}5$ từ mỗi trang.

**Kiểm tra lại.** Tổng số từ của kho là $5$, bằng số cặp Map phát trong Ví dụ 02.4; số trang là $2$. Một trang rỗng vẫn góp trạng thái $(0,1)$: nếu kho có thêm một trang rỗng, $\mu=5/3$, và bỏ trang đó làm sai mẫu số.
:::

Ba bài toán trên và đếm từ cho một quy tắc chung: khóa được chọn theo thành phần của đầu ra mà các đóng góp phải gặp nhau để tạo ra, và giá trị trung gian là trạng thái nhỏ nhất đủ để gộp hai nhóm rời nhau bằng một phép kết hợp, giao hoán.

::: remark Nhận xét 02.27 (Quy tắc chọn khóa và trạng thái)
| Bài toán | Khóa | Giá trị trung gian | Phép gộp $\oplus$ | Hàm hoàn tất $\phi$ |
|---|---|---|---|---|
| Đếm từ (Hệ quả 02.12) | từ $w$ | số đếm | cộng | đồng nhất |
| Nhân ma trận–véc-tơ (Mệnh đề 02.19) | hàng $i$ | tích hoặc tổng bộ phận | cộng | đồng nhất |
| Đếm từ phân biệt, công việc 1 (Mệnh đề 02.23) | từ $w$ | dấu hiệu có mặt $1$ | $x\oplus y=1$ | đồng nhất |
| Đếm từ phân biệt, công việc 2 | khóa chung $g$ | số đếm | cộng | đồng nhất |
| Trung bình cộng (Mệnh đề 02.26) | khóa chung $g$ | trạng thái $(s,\kappa)$ | cộng từng thành phần | $s/\kappa$ |

Khóa chung $g$ dồn mọi giá trị về một reducer, nên các phép gộp của Reduce chỉ chạy trên một máy; Combine làm cho reducer đó chỉ nhận một trạng thái từ mỗi tác vụ Map thay cho một giá trị từ mỗi phần tử.
:::

Như vậy, chúng ta đã có ba thiết kế với ba chứng minh tính đúng: nhân ma trận–véc-tơ với khóa hàng (Thuật toán 02.18, Mệnh đề 02.19), đếm từ phân biệt bằng hai công việc (Thuật toán 02.22, Mệnh đề 02.23) và trung bình cộng với trạng thái tổng–số lượng (Thuật toán 02.25, Mệnh đề 02.26); cả ba quy về Mệnh đề 02.11 cho phần khung và Mệnh đề 02.15 cho Combine. Tuy nhiên, tính đúng chưa cho biết chạy trên nhiều máy có nhanh hơn một máy hay không, và Combine có thật sự có lợi hay không. Trong Mục 4, chúng ta đo tổng khối lượng tính toán, thời gian và lượng dữ liệu truyền của các thiết kế này.

<!-- note-topic-id: lec-02-topic-11 -->
## 4. Chi phí và lợi ích của song song hóa

Cộng 16 số trên một máy cần 15 phép cộng. Chia 16 số cho 4 máy thì số phép cộng vẫn là 15, nhưng 4 máy cộng cùng lúc nên công việc xong sớm hơn. Hai con số "bao nhiêu phép cộng" và "bao lâu thì xong" vì vậy phải được đo riêng; ngoài ra còn lượng dữ liệu đi qua mạng, đại lượng mà Định nghĩa 01.13 tách khỏi khối lượng tính toán.

### 4.1 Tổng khối lượng tính toán

::: definition Định nghĩa 02.28 (Ba đại lượng chi phí của một công việc)
Cho một công việc chạy trên $P\ge1$ máy giống nhau.

- **Tổng khối lượng tính toán** $W_P$ là tổng số phép toán cơ bản mà mọi máy thực hiện, theo một mô hình đếm đã chọn; đơn vị là số phép toán.
- **Thời gian hoàn thành** $T_P$ là thời gian từ lúc công việc bắt đầu tới lúc có đủ đầu ra; đơn vị là giây.
- **Lượng dữ liệu** là số byte hoặc số bản ghi mà các tác vụ đọc, hoặc gửi qua một đường truyền.
:::

Ba đại lượng là ba mô hình chi phí theo Định nghĩa 01.13, với ba đơn vị khác nhau; con số của chúng không cộng được với nhau. $W_P$ trả lời "tốn bao nhiêu việc", $T_P$ trả lời "phải chờ bao lâu", còn lượng dữ liệu trả lời "mạng phải chở bao nhiêu". Một nhầm lẫn thường gặp là coi $W_P$ như $T_P$: thêm máy có thể giảm $T_P$ mà không giảm $W_P$.

::: example Ví dụ 02.10 (Số phép cộng khi cộng 16 số trên 4 máy)
**Dữ kiện.** $n=16$ số, $P=4$ máy, mỗi máy giữ 4 số. Mỗi tổng được khởi tạo bằng phần tử đầu của nó. Chỉ đếm phép cộng.

**Cộng cục bộ.** Mỗi máy cộng 4 số bằng 3 phép cộng; 4 máy làm $4\cdot3=12$ phép cộng.

**Gộp.** Một máy cộng 4 tổng cục bộ bằng 3 phép cộng.

**Tổng khối lượng tính toán.** $W_4=12+3=15$.

**Kiểm tra lại.** Một máy cộng 16 số bằng $16-1=15$ phép cộng; $W_4=W_1$.
:::

::: proposition Mệnh đề 02.29 (Tổng khối lượng tính toán của cộng một dãy)
**Giả thiết.** $n\ge P\ge1$ và $P$ chia hết $n$; mỗi máy giữ $n/P$ số; mỗi máy cộng các số của mình, rồi một máy cộng $P$ tổng cục bộ; mọi tổng được khởi tạo bằng phần tử đầu; chỉ đếm phép cộng.

**Kết luận.** $W_P=n-1$, không phụ thuộc $P$.

**Điều kiện áp dụng.** Số học chính xác; mô hình đếm phép cộng.

**Phạm vi.** Mệnh đề đếm phép toán, không đếm thời gian hay dữ liệu truyền.
:::

::: proof
Bảng sau đếm từng bước theo số lần, chi phí mỗi lần và đóng góp.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| Cộng cục bộ trên một máy | $P$ | $n/P-1$ phép cộng | $P(n/P-1)=n-P$ |
| Gộp $P$ tổng cục bộ | $1$ | $P-1$ phép cộng | $P-1$ |

Một dãy $\ell\ge1$ số khởi tạo bằng phần tử đầu cần $\ell-1$ phép cộng, nên hai cột chi phí đúng với $\ell=n/P$ và $\ell=P$. Cộng hai đóng góp:
$$
\begin{aligned}
W_P&=(n-P)+(P-1)\\
&=n-1.
\end{aligned}
$$
$\square$
:::

Tổng khối lượng tính toán không đổi vì mỗi phép cộng gộp hai giá trị thành một, nên từ $n$ số xuống còn một tổng luôn cần $n-1$ phép cộng, dù phép cộng diễn ra ở máy nào. Giả thiết khởi tạo bằng phần tử đầu ảnh hưởng tới con số: nếu mọi tổng, cục bộ và gộp, đều khởi tạo bằng 0, mỗi máy làm $n/P$ phép cộng và bước gộp làm $P$ phép cộng, nên $W_P=n+P$, phụ thuộc $P$; với $n=16$, $P=4$ là $20$ phép cộng thay cho $15$. Trong cả hai cách đếm, song song hóa không giảm tổng khối lượng tính toán; nó chia công việc cho nhiều máy.

<!-- note-topic-id: lec-02-topic-12 -->
### 4.2 Thời gian của một pha và của cả công việc

Một công việc MapReduce chạy theo các **pha** (phase) nối tiếp nhau: pha Map, pha chuyển và nhóm, pha Reduce, cùng phần điều phối ban đầu. Trong một pha, các máy làm đồng thời, và pha kết thúc khi máy cuối cùng làm xong phần việc của nó.

::: definition Định nghĩa 02.30 (Thời gian của một pha và của cả công việc)
**Giả thiết mô hình.** Mọi tác vụ của một pha sẵn sàng từ đầu pha; mỗi máy chạy lần lượt các tác vụ được giao, không nghỉ, không lỗi; các pha nối tiếp nhau.

- Với máy $u$, gọi $t_u$ là tổng thời gian các tác vụ của pha được giao cho máy $u$. **Thời gian của pha** là
$$
T_{\text{pha}}=\max_{u}t_u .
$$
- **Thời gian của cả công việc** trên $P$ máy là tổng thời gian các pha, $T_P=\sum_{\text{pha}}T_{\text{pha}}$.
:::

Thời gian của pha là giá trị lớn nhất, không phải tổng: các máy chạy đồng thời, nên pha chỉ phải chờ máy chậm nhất. Nó cũng không phải thời gian của tác vụ dài nhất, vì một máy có thể phải chạy nhiều tác vụ nối tiếp. Ví dụ sau cho thấy cả hai điểm.

::: example Ví dụ 02.11 (Thời gian một pha trên ba máy)
**Dữ kiện.** Năm tác vụ $\mathrm A$–$\mathrm E$ của một pha giao cho ba máy:

- máy 1 chạy $\mathrm A$ và $\mathrm B$, mỗi tác vụ 2 giây;
- máy 2 chạy $\mathrm C$ và $\mathrm D$, mỗi tác vụ 3 giây;
- máy 3 chạy $\mathrm E$, 3 giây.

**Tải từng máy.** $t_1=2+2=4$, $t_2=3+3=6$, $t_3=3$ giây.

**Thời gian pha.** $T_{\text{pha}}=\max(4,6,3)=6$ giây.

**Kiểm tra lại.** Tác vụ dài nhất chỉ 3 giây, nhưng máy 2 chạy hai tác vụ 3 giây nối tiếp; tổng thời gian làm việc của ba máy là $13$ giây, lớn hơn thời gian pha.
:::

![Biểu đồ thời gian từ 0 đến 6 giây cho ba máy. Máy 1 chạy tác vụ A 2 giây rồi B 2 giây, xong ở giây 4. Máy 2 chạy C 3 giây rồi D 3 giây, xong ở giây 6. Máy 3 chạy E 3 giây, xong ở giây 3.](img/lec-02/cost-03.svg)

Trên hình, mỗi hàng là một máy và mỗi thanh là một tác vụ. Máy 1 và máy 3 xong trước và chờ; pha kết thúc ở giây 6, cuối thanh $\mathrm D$ của máy 2. Nếu giao lại $\mathrm A,\mathrm C$ cho máy 1 và $\mathrm B,\mathrm D$ cho máy 2, tải thành $5,5,3$ và thời gian pha còn 5 giây với cùng năm tác vụ. Giảm thời gian pha là cân bằng tải giữa các máy, tức giảm lệch tải theo nghĩa của Nhận xét 02.13.

::: example Ví dụ 02.12 (Thời gian cộng 16 số trên bốn máy)
**Dữ kiện.** $n=16$, $P=4$, mỗi máy giữ 4 số; một phép cộng mất $\tau>0$ giây; dữ liệu đã nằm tại mỗi máy; hai pha nối tiếp, bỏ qua đọc ghi, truyền và điều phối.

**Pha Map.** Bốn máy cộng đồng thời, mỗi máy 3 phép cộng: $T_{\text{Map}}=3\tau$.

**Pha Reduce.** Một máy gộp 4 tổng bằng 3 phép cộng: $T_{\text{Reduce}}=3\tau$.

**Cả công việc.** $T_4=3\tau+3\tau=6\tau$, so với $T_1=15\tau$ trên một máy.

**Kiểm tra lại.** Tổng khối lượng tính toán vẫn là $4\cdot3+3=15$ phép cộng (Ví dụ 02.10); thời gian giảm vì 12 phép cộng của pha Map diễn ra trong $3\tau$.
:::

![Biểu đồ thời gian theo đơn vị τ từ 0 đến 15τ. Hàng trên: 1 máy cộng 16 số mất 15τ. Bốn hàng dưới: máy 1 đến máy 4 mỗi máy cộng 4 số trong 3τ ở pha Map; sau đó máy 1 gộp 4 tổng trong 3τ ở pha Reduce; công việc kết thúc sau 6τ.](img/lec-02/cost-04.svg)

Trên hình, bốn máy làm 12 phép cộng của pha Map song song trong $3\tau$, rồi máy 1 làm 3 phép cộng của pha Reduce; khoảng từ $6\tau$ đến $15\tau$ là thời gian tiết kiệm được so với một máy.

::: proposition Mệnh đề 02.31 (Thời gian cộng một dãy trên $P$ máy)
**Giả thiết.** Như Mệnh đề 02.29; mỗi phép cộng mất $\tau$ giây; hai pha nối tiếp theo Định nghĩa 02.30; bỏ qua đọc ghi, truyền và điều phối.

**Kết luận.**
$$
T_P=\Big(\frac nP-1\Big)\tau+(P-1)\tau .
$$

**Điều kiện áp dụng.** Bước gộp do một máy làm tuần tự.

**Phạm vi.** Công thức dành cho cách gộp tuần tự này; gộp theo cây cho một lịch khác.
:::

::: proof
**Pha cộng cục bộ.** Mỗi máy làm $n/P-1$ phép cộng, nên $t_u=(n/P-1)\tau$ với mọi $u$ và $T_{\text{Map}}=\max_ut_u=(n/P-1)\tau$ theo Định nghĩa 02.30.

**Pha gộp.** Chỉ một máy làm việc, với $P-1$ phép cộng, nên $T_{\text{Reduce}}=(P-1)\tau$.

**Cộng hai pha.** Theo Định nghĩa 02.30, $T_P=T_{\text{Map}}+T_{\text{Reduce}}$. $\square$
:::

Hai trường hợp biên cho cùng một giá trị: $P=1$ cho $T_1=(n-1)\tau$, một máy làm hết; $P=n$ cho pha cục bộ bằng 0 và pha gộp $(n-1)\tau$, một máy gộp hết. Thời gian nhỏ nhất nằm ở giữa, và hệ quả sau chỉ ra vị trí của nó.

::: corollary Hệ quả 02.32 (Số máy cho thời gian nhỏ nhất)
**Giả thiết.** Như Mệnh đề 02.31.

**Kết luận.** $T_P\ge(2\sqrt n-2)\tau$, với dấu bằng khi và chỉ khi $P=\sqrt n$.

**Điều kiện áp dụng.** Dấu bằng đạt được khi $\sqrt n$ là số nguyên; khi đó $P=\sqrt n$ chia hết $n$.

**Phạm vi.** Chỉ cho cách gộp tuần tự của Mệnh đề 02.31.
:::

::: proof
Theo bất đẳng thức giữa trung bình cộng và trung bình nhân của hai số dương $n/P$ và $P$,
$$
\frac nP+P\ge2\sqrt{\frac nP\cdot P}=2\sqrt n,
$$
với dấu bằng khi và chỉ khi $n/P=P$, tức $P=\sqrt n$. Thay vào Mệnh đề 02.31, $T_P=(n/P+P-2)\tau\ge(2\sqrt n-2)\tau$. $\square$
:::

Với $n=16$, các giá trị $P=1,2,4,8,16$ cho $T_P=15\tau,8\tau,6\tau,8\tau,15\tau$; nhỏ nhất ở $P=4=\sqrt{16}$, đúng $6\tau=(2\cdot4-2)\tau$ của Ví dụ 02.12. Thêm máy quá $\sqrt n$ làm tăng thời gian, vì phần gộp tuần tự dài thêm nhanh hơn phần cục bộ ngắn đi.

**Trong thực hành.** Pha gộp tuần tự của Mệnh đề 02.31 ứng với một tác vụ Reduce duy nhất nhận mọi tổng cục bộ, như khi dùng khóa chung $g$ ở Mục 3.3.

::: example Ví dụ 02.13 (Thời gian của một công việc bốn pha)
**Dữ kiện.** Giả sử một công việc trên $P=4$ máy có bốn pha nối tiếp: điều phối 1 giây; pha Map 4 giây, đã là thời gian của máy chậm nhất; chuyển và nhóm 3 giây; pha Reduce 2 giây.

**Thời gian.** $T_4=1+4+3+2=10$ giây.

**Kiểm tra lại.** Các mốc thời gian là 0, 1, 5, 8, 10 giây; mỗi pha bắt đầu đúng lúc pha trước kết thúc.
:::

![Trục thời gian từ 0 đến 10 giây chia bốn đoạn nối tiếp: điều phối từ 0 đến 1 giây, Map 4 giây từ 1 đến 5, truyền và nhóm 3 giây từ 5 đến 8, Reduce 2 giây từ 8 đến 10.](img/lec-02/cost-09.svg)

Đọc hình theo các mốc trên trục: pha Map đã gồm thời gian đọc đầu vào, pha giữa gồm truyền và sắp xếp, pha Reduce gồm ghi đầu ra. Hệ thống thật cho các pha chồng lên nhau một phần: việc chuyển đầu ra của các tác vụ Map đã xong có thể chạy song song với các tác vụ Map khác (trang chiếu MMDS, tr.28). Khi đó Định nghĩa 02.30 cho một cận trên của thời gian.

<!-- note-topic-id: lec-02-topic-13 -->
### 4.3 Chi phí truyền thông

Thời gian của các pha giữa phụ thuộc lượng dữ liệu phải chuyển. MMDS lấy lượng dữ liệu làm thước đo chính để so các thuật toán trên cụm máy.

::: definition Định nghĩa 02.33 (Chi phí truyền thông)
- **Chi phí truyền thông** (communication cost) của một tác vụ là kích thước đầu vào của tác vụ đó, đo bằng byte hoặc số bản ghi.
- Chi phí truyền thông của một thuật toán là tổng chi phí truyền thông của mọi tác vụ thực hiện thuật toán.
- Với một công việc MapReduce, gọi $I$ là tổng kích thước đầu vào của các tác vụ Map và $H$ là tổng kích thước đầu vào của các tác vụ Reduce; chi phí truyền thông của công việc là
$$
C=I+H .
$$
:::

Định nghĩa theo MMDS (§2.5.1, tr.53–54). Theo định nghĩa, $I$ được tính cả khi tác vụ Map đọc khối nằm ngay trên máy của nó: dữ liệu vẫn phải chuyển từ đĩa vào bộ nhớ (MMDS, Ví dụ 2.14, tr.55). $H$ là đầu ra của các tác vụ Map sau Combine, vì đó là đầu vào của các tác vụ Reduce; đầu ra của các tác vụ Reduce không được tính.

::: example Ví dụ 02.14 (Chi phí truyền thông của một công việc)
**Dữ kiện.** Giả sử các tác vụ Map đọc tổng cộng $I=100$ MB, và các tác vụ Reduce nhận tổng cộng $H=40$ MB.

**Chi phí truyền thông.** $C=I+H=100+40=140$ MB.

**Kiểm tra lại.** Đầu ra cuối của các tác vụ Reduce không có mặt trong phép cộng.
:::

![Sơ đồ ba khối nối tiếp: đầu vào Map I = 100 MB đi vào Map; đầu vào Reduce H = 40 MB đi vào Reduce; kết quả cuối ghi chú là không tính vào C.](img/lec-02/cost-05.svg)

Hình đánh dấu hai chỗ được đếm: dữ liệu đi vào Map và dữ liệu đi vào Reduce. Kết quả cuối nằm ngoài $C$ theo quy ước của MMDS.

::: remark Nhận xét 02.34 (Lý do đếm truyền thông; hai quy ước)
MMDS nêu ba lý do để chi phí truyền thông thường chi phối chi phí của một thuật toán trên cụm (§2.5.1, tr.54):

- thuật toán của mỗi tác vụ thường đơn giản, thường tuyến tính theo kích thước đầu vào;
- tốc độ mạng điển hình của một cụm là một gigabit mỗi giây, chậm so với tốc độ bộ xử lý, và nhiều máy thường tranh nhau cùng đường truyền;
- ngay cả khi tác vụ chạy trên máy có bản sao của khối, khối nằm trên đĩa và thời gian đưa nó vào bộ nhớ có thể lớn hơn thời gian xử lý.

MMDS chỉ đếm đầu vào vì hai lẽ: đầu ra của một tác vụ là đầu vào của tác vụ sau nên đã được đếm ở đó, và đầu ra cuối của một thuật toán thường nhỏ so với đầu vào và dữ liệu trung gian (tr.54–55).

Trang chiếu MMDS (tr.39) và CS246 (trang chiếu 68) dùng một quy ước khác: chi phí truyền thông là tổng đọc ghi của mọi tiến trình, bằng kích thước tệp đầu vào cộng hai lần tổng các tệp chuyển từ Map sang Reduce cộng tổng đầu ra của Reduce, tức
$$
I+2H+O=C+H+O,
$$
với $O$ là tổng kích thước đầu ra của các tác vụ Reduce. Thừa số 2 có vì quy ước này đếm đọc ghi của mọi tiến trình: mỗi tệp trung gian được đếm một lần như đầu ra của tác vụ Map và một lần như đầu vào của tác vụ Reduce (trang chiếu MMDS, tr.38; CS246, trang chiếu 67–68). Đây là quy ước mà Bài 01 đã dẫn. Nếu thuật toán 1 có $C$, $H$ và $O$ đều không lớn hơn của thuật toán 2 thì cả hai quy ước cùng xếp thuật toán 1 không tệ hơn thuật toán 2. Trong Bài 02, ta dùng $C=I+H$ của sách. Với Ví dụ 02.14 và giả sử $O=5$ MB, quy ước của trang chiếu MMDS và CS246 cho $100+2\cdot40+5=185$ MB.
:::

Muốn so hai thiết kế, chẳng hạn có và không có Combine, ta cần $H$ dưới dạng công thức. Với đếm từ, $I$ không phụ thuộc Combine vì các tác vụ Map vẫn đọc toàn bộ kho; chỉ $H$ thay đổi.

::: proposition Mệnh đề 02.35 (Lượng dữ liệu trung gian của đếm từ)
**Giả thiết.** Đếm từ theo Thuật toán 02.9 với $m$ tác vụ Map, tác vụ $j$ đọc phần $X_j$; $\mathcal W(X_j)$ là tập từ xuất hiện trong các văn bản của $X_j$; $H$ đo bằng số cặp.

**Kết luận.**

- (a) Không có Combine, $H=\sum_{i=1}^{n}\ell_i$.
- (b) Khi Combine được gọi đúng một lần cho mỗi khóa trên toàn bộ đầu ra của mỗi tác vụ Map, $H=\sum_{j=1}^{m}\lvert\mathcal W(X_j)\rvert$.
- (c) Với mọi cách hệ thống gọi Combine, $\sum_{j=1}^{m}\lvert\mathcal W(X_j)\rvert\le H\le\sum_{i=1}^{n}\ell_i$.

**Điều kiện áp dụng.** Mỗi lần gọi Combine phát đúng một cặp, như Mệnh đề 02.15.

**Phạm vi.** $I$ không đổi trong cả ba trường hợp; mệnh đề không đếm byte của mỗi cặp.
:::

::: proof
**Câu (a).** Map phát một cặp cho mỗi lần xuất hiện của một từ (Thuật toán 02.9), và văn bản $d_i$ có $\ell_i$ lần xuất hiện; không có Combine, mọi cặp đi tới Reduce.

**Câu (b).** Trong tác vụ $j$, mỗi từ $w\in\mathcal W(X_j)$ có ít nhất một cặp, và một lần gọi Combine trên toàn bộ các cặp của $w$ thay chúng bằng đúng một cặp; từ không thuộc $\mathcal W(X_j)$ không có cặp nào. Vậy tác vụ $j$ gửi $\lvert\mathcal W(X_j)\rvert$ cặp; cộng theo $j$.

**Câu (c).** Mỗi lần gọi Combine thay một danh sách khác rỗng bằng một cặp, nên không làm tăng số cặp; cận trên là (a). Combine giữ khóa, nên mỗi từ $w\in\mathcal W(X_j)$ còn ít nhất một cặp ở tác vụ $j$; cận dưới là (b). $\square$
:::

::: example Ví dụ 02.15 (Lượng truyền của đếm từ khi có Combine)
**Dữ kiện.** $d_1=$ "mèo chó mèo" ở tác vụ Map 1, $d_2=$ "chó chim" ở tác vụ Map 2; giả sử mỗi cặp chiếm 16 byte và mỗi cặp đi qua đường truyền đúng một lần.

**Không Combine.** Theo Mệnh đề 02.35(a), $H=\ell_1+\ell_2=3+2=5$ cặp, tức $5\cdot16=80$ byte.

**Có Combine.** Theo Mệnh đề 02.35(b), $H=\lvert\{\text{mèo},\text{chó}\}\rvert+\lvert\{\text{chó},\text{chim}\}\rvert=2+2=4$ cặp, tức $4\cdot16=64$ byte.

**So sánh.** Lượng truyền giảm $80-64=16$ byte, tức $16/80=20\%$; $I$ không đổi, nên $C$ giảm đúng 16 byte.

**Kiểm tra lại.** Bốn cặp là (mèo, 2), (chó, 1), (chó, 1), (chim, 1), đúng như Ví dụ 02.5.
:::

Mệnh đề 02.35 áp cho mọi bài toán có Combine gọi một lần cho mỗi khóa trong mỗi tác vụ: $H$ bằng tổng, theo tác vụ Map, số khóa phân biệt của tác vụ đó. Với nhân ma trận của Ví dụ 02.6, mỗi khối có hai khóa hàng, nên $H$ giảm từ 16 xuống $4\cdot2=8$ cặp. Combine có lợi nhiều khi mỗi tác vụ Map có ít khóa phân biệt so với số cặp nó phát, như từ phổ biến trong một khối lớn của kho web; nó không có lợi khi khóa hiếm khi lặp trong một tác vụ.

::: remark Nhận xét 02.36 (Trong thực hành: chi phí truyền thông và thời gian)
$C$ nhỏ không suy ra $T_P$ nhỏ. Giao toàn bộ công việc cho một tác vụ làm chi phí truyền thông nhỏ nhất, nhưng thời gian hoàn thành khi đó lớn (MMDS, §2.5.2, tr.55–56). Các thuật toán của MMDS chia việc đều cho các tác vụ, nên thời gian gần mức nhỏ nhất có thể với số máy cho trước. Combine giảm $H$ nhưng thêm phép cộng ở pha Map; có lợi hay không phải tính bằng $T_P$.
:::

<!-- note-topic-id: lec-02-topic-14 -->
### 4.4 Băng thông và đường nối dùng chung

$C$ đếm lượng dữ liệu nhưng không cho ra số giây. Để đổi lượng dữ liệu thành thời gian, cần biết đường truyền chuyển được bao nhiêu byte mỗi giây và bắt đầu chuyển sau bao lâu.

::: definition Định nghĩa 02.37 (Thời gian truyền và đường nối dùng chung)
- **Băng thông** (bandwidth) $B$ của một đường truyền là lượng dữ liệu tối đa đường đó chuyển được trong một giây, tính bằng MB/s. Trong mọi khoảng thời gian $T$ giây, đường truyền chuyển không quá $BT$ MB.
- Trong chương này, thời gian truyền một thông điệp $Q$ MB qua một đường truyền dành riêng có băng thông ổn định $B$ được mô hình hóa bằng
$$
T_{\text{truyền}}\approx\lambda+\frac{Q}{B},
$$
với $\lambda$ là **độ trễ khởi đầu** (latency), thời gian từ lúc gửi tới lúc byte đầu tiên tới nơi.
- Một **đường nối dùng chung** là đường truyền mà nhiều cặp máy cùng dùng, như đường nối liên tủ của Định nghĩa 02.3; băng thông $B$ của nó là băng thông của cả đường, chia cho mọi luồng dữ liệu đi qua.
:::

Mô hình có hai thành phần: $\lambda$ không phụ thuộc lượng dữ liệu và chi phối khi thông điệp nhỏ; $Q/B$ tỷ lệ với lượng dữ liệu và chi phối khi thông điệp lớn. Cần phân biệt MB (megabyte) với Mb (megabit): một gigabit mỗi giây trong Nhận xét 02.34 là $125$ MB/s.

::: example Ví dụ 02.16 (Thời gian truyền một thông điệp)
**Dữ kiện.** Giả sử $Q=100$ MB, $B=50$ MB/s, $\lambda=0{,}02$ giây.

**Tính.** $T_{\text{truyền}}\approx0{,}02+100/50=0{,}02+2=2{,}02$ giây.

**Kiểm tra lại.** Phần $Q/B=2$ giây chiếm hơn 99% tổng; với thông điệp 100 MB, độ trễ khởi đầu không đáng kể.
:::

Khi nhiều máy cùng gửi qua một đường nối dùng chung, mỗi máy không còn băng thông riêng. Mệnh đề sau cho một cận dưới chỉ phụ thuộc tổng lượng dữ liệu.

::: proposition Mệnh đề 02.38 (Cận dưới thời gian truyền qua đường nối dùng chung)
**Giả thiết.** Tổng cộng $Q$ MB phải đi qua một đường nối có băng thông $B$ MB/s, gửi từ một hay nhiều máy.

**Kết luận.** Thời gian để chuyển đủ $Q$ MB ít nhất là $Q/B$ giây.

**Điều kiện áp dụng.** Mọi dữ liệu được tính phải đi qua chính đường nối đó.

**Phạm vi.** Đây là cận dưới; độ trễ, tranh chấp và xử lý có thể làm thời gian dài hơn.
:::

::: proof
Gọi $T$ là thời gian chuyển đủ $Q$ MB. Theo định nghĩa băng thông, trong $T$ giây đường nối chuyển không quá $BT$ MB, nên $BT\ge Q$, tức $T\ge Q/B$. $\square$
:::

::: example Ví dụ 02.17 (Bốn máy gửi qua một đường nối liên tủ)
**Dữ kiện.** Giả sử bốn máy ở một tủ, mỗi máy gửi 100 MB tới một máy ở tủ khác; mọi dữ liệu đi qua một đường nối liên tủ có băng thông 100 MB/s cho cả đường.

**Cận dưới.** $Q=4\cdot100=400$ MB; theo Mệnh đề 02.38, thời gian ít nhất là $400/100=4$ giây.

**Kiểm tra lại.** Nếu hiểu nhầm 100 MB/s là băng thông của mỗi máy, ta được 1 giây, nhỏ hơn cận dưới 4 giây.
:::

![Tủ rack gửi có bốn máy, mỗi máy gửi 100 MB; tất cả đi qua một đường nối dùng chung có B = 100 MB/s tới máy nhận ở tủ rack nhận; tổng lượng truyền V = 4 × 100 = 400 MB.](img/lec-02/cost-07.svg)

Hình vẽ bốn luồng 100 MB nhập vào một đường nối; nhãn $V$ trên hình là lượng truyền $Q$ của ghi chú. Đường nối chỉ chuyển 100 MB mỗi giây dù bốn máy gửi đồng thời. Mệnh đề 02.38 giải thích yêu cầu đưa tính toán tới gần dữ liệu ở Mục 1.1: nếu tác vụ Map chạy trên máy có bản sao của khối, khối không đi qua đường nối liên tủ, nên $Q$ trên đường đó giảm và cận dưới $Q/B$ giảm theo. Vị trí dữ liệu không làm mất việc đọc khối từ đĩa: phần đó vẫn nằm trong $I$ của Định nghĩa 02.33.

<!-- note-topic-id: lec-02-topic-15 -->
### 4.5 Mức tăng tốc

Có thời gian của cả công việc, ta so được chạy trên $P$ máy với chạy trên một máy.

::: definition Định nghĩa 02.39 (Mức tăng tốc)
Cho cùng một bài toán, cùng đầu vào, cùng đầu ra và cùng phạm vi đo thời gian, gọi $T_1$ là thời gian chạy trên một máy và $T_P$ là thời gian chạy trên $P$ máy. **Mức tăng tốc** (speedup) là
$$
S_P=\frac{T_1}{T_P}.
$$
:::

$S_P>1$ nghĩa là chạy trên $P$ máy nhanh hơn; $S_P=P$ là tăng tốc tuyến tính, khi thời gian chia đều cho $P$ máy mà không có phần nào thêm vào. Điều kiện "cùng phạm vi đo" ngăn so sánh sai: nếu $T_1$ gồm cả đọc đầu vào mà $T_P$ thì không, $S_P$ phóng đại lợi ích.

::: example Ví dụ 02.18 (Mức tăng tốc của hai lịch)
**Dữ kiện.** Lịch bốn pha của Ví dụ 02.13: $T_4=10$ giây; giả sử cùng công việc chạy trên một máy mất $T_1=24$ giây. Cộng 16 số của Ví dụ 02.12: $T_4=6\tau$, $T_1=15\tau$.

**Mức tăng tốc.** Lịch bốn pha: $S_4=24/10=2{,}4$. Cộng 16 số: $S_4=15\tau/6\tau=2{,}5$.

**Kiểm tra lại.** Cả hai đều nhỏ hơn $P=4$: lịch bốn pha có điều phối và truyền, còn cộng 16 số có pha gộp tuần tự.
:::

![Hai thanh thời gian trên trục từ 0 đến 24 giây: 1 máy mất 24 giây; 4 máy mất 10 giây.](img/lec-02/cost-10.svg)

Hình so hai thanh trên cùng một trục; tỷ số độ dài hai thanh là $S_4=2{,}4$. Ví dụ sau đặt chi phí truyền, phép gộp cục bộ và mức tăng tốc vào cùng một phép tính.

::: example Ví dụ 02.19 (Thời gian của công việc có và không có Combine)
**Dữ kiện.** Giả sử một công việc chạy trên $P=3$ máy với các pha nối tiếp, bỏ qua độ trễ khởi đầu và chi phí nhóm:

- điều phối 1 giây;
- tải Map của ba máy là 2, 3 và 5 giây;
- lượng truyền $Q=120$ MB qua một đường nối có $B=40$ MB/s;
- Reduce 2 giây;
- trên một máy, $T_1=22$ giây.

Phương án thứ hai dùng Combine: lượng truyền còn 40 MB, nhưng máy Map chậm nhất mất thêm 1 giây.

**Không Combine.** $T_{\text{Map}}=\max(2,3,5)=5$ giây; $T_{\text{truyền}}=120/40=3$ giây; $T_3=1+5+3+2=11$ giây; $S_3=22/11=2$.

**Có Combine.** $T_{\text{Map}}=6$ giây; $T_{\text{truyền}}=40/40=1$ giây; $T'_3=1+6+1+2=10$ giây; $S'_3=22/10=2{,}2$.

**Kết luận.** Combine tiết kiệm 2 giây truyền và tốn thêm 1 giây Map, nên công việc nhanh hơn 1 giây.

**Kiểm tra lại.** Các mốc thời gian của phương án có Combine là 0, 1, 7, 8, 10 giây, và $1+6+1+2=10$.
:::

Nếu lấy tổng tải $2+3+5=10$ giây thay cho giá trị lớn nhất 5 giây, ta được $T_3=1+10+3+2=16$ giây, sai theo Định nghĩa 02.30.

**Trong thực hành.** Mức tăng tốc nhỏ hơn $P$ khi công việc có phần truyền, phần gộp tuần tự, điều phối hoặc lệch tải giữa các máy, vì các phần đó không chia đều cho $P$ máy (Nhận xét 02.13, Hệ quả 02.32, Mệnh đề 02.38). Muốn biết thêm máy có lợi, cần ước lượng từng phần của $T_P$ chứ không chỉ chia $T_1$ cho $P$.

::: exercise Bài tập 02.3 (Chi phí truyền thông của hai thuật toán; MMDS Bài 2.5.1(a), (c), §2.5.4, tr.59)
Tính chi phí truyền thông $C=I+H$ theo Định nghĩa 02.33 của hai thuật toán sau, theo kích thước ma trận, véc-tơ hoặc quan hệ mà chúng xử lý.

- (a) Nhân ma trận–véc-tơ khi chia dải (MMDS, §2.3.2): $A\in\mathbb R^{q\times q}$ có $N_A$ bản ghi được lưu ($N_A=q^2$ khi ma trận đặc); $A$ chia thành $b$ dải dọc cùng bề rộng $q/b$ và $v$ chia thành $b$ đoạn tương ứng; có $m$ tác vụ Map, mỗi tác vụ nhận một phần của một dải và cả đoạn $q/b$ thành phần tương ứng của $v$; Map và Reduce như Thuật toán 02.18, không dùng Combine, rồi so với khi có Combine. Đo kích thước bằng số bản ghi, mỗi thành phần của $v$ là một bản ghi.
- (c) Nhóm và gộp (MMDS, §2.3.8): quan hệ $\mathrm R(\mathrm A,\mathrm B,\mathrm C)$ là một bảng gồm $\lvert\mathrm R\rvert$ bộ $(a,b,c)$ với ba thuộc tính $\mathrm A,\mathrm B,\mathrm C$; Map phát $(a,b)$ cho mỗi bộ; Reduce áp phép gộp $\theta$, chẳng hạn SUM hay MAX, lên danh sách các giá trị $b$ của khóa $a$. Đo kích thước bằng số bộ hoặc số cặp.
:::

::: hint
Cộng kích thước đầu vào của mọi tác vụ Map, kể cả đoạn $v$ mà mỗi tác vụ đọc, rồi đếm số cặp mà Map gửi tới Reduce.
:::

::: solution
**Câu (a).** Các tác vụ Map đọc mọi bản ghi của $A$ đúng một lần, cộng mỗi tác vụ một đoạn $q/b$ thành phần của $v$:
$$
I=N_A+m\cdot\frac qb .
$$
Không có Combine, mỗi bản ghi sinh một cặp, nên $H=N_A$ và
$$
C=2N_A+m\cdot\frac qb .
$$
Nếu mỗi phần giao cho một tác vụ Map chứa ít nhất $q/b$ bản ghi của $A$, chẳng hạn ít nhất một hàng của dải với ma trận đặc, thì $mq/b\le N_A$ và $2N_A\le C\le3N_A$; khi đó $C=\Theta(N_A)$, tức $\Theta(q^2)$ với ma trận đặc. Với Combine, mỗi tác vụ Map gửi nhiều nhất một cặp cho mỗi hàng, nên $H\le\min(N_A,\ mq)$.

**Câu (c).** Mỗi bộ được một tác vụ Map đọc đúng một lần, nên $I=\lvert\mathrm R\rvert$; mỗi bộ sinh một cặp $(a,b)$, nên $H=\lvert\mathrm R\rvert$ và
$$
C=2\lvert\mathrm R\rvert .
$$
Với $\theta$ là SUM, MIN hoặc MAX, phép gộp trên các giá trị $b$ kết hợp và giao hoán, nên Combine dùng được theo Mệnh đề 02.15 và $H$ giảm còn nhiều nhất $m$ nhân số giá trị $a$ phân biệt. COUNT không có dạng $\phi(\bigoplus L)$ trên các giá trị $b$: với $L=[5,7]$, Combine bằng COUNT phát 2, và Reduce đếm danh sách $[2]$ được 1. Muốn dùng Combine cho COUNT, Map phát $(a,1)$ và $\oplus=+$. Với $\theta$ là AVG, Combine cần trạng thái $(s,\kappa)$ của Mục 3.3.

**Kiểm tra lại.** Ví dụ 02.6 là trường hợp một dải, $b=1$, với $q=4$, $N_A=16$, $m=4$: $I=16+4\cdot4=32$, $H=16$, $C=48$ bản ghi khi không có Combine; có Combine thì $H=8$ và $C=40$, khớp với 8 cặp của ví dụ.
:::

Như vậy, chúng ta đã có ba đại lượng riêng của một công việc: tổng khối lượng tính toán $W_P=n-1$ không giảm khi thêm máy (Mệnh đề 02.29); thời gian $T_P$ là tổng theo pha của tải lớn nhất, nhỏ nhất ở $P=\sqrt n$ với cộng dãy (Mệnh đề 02.31, Hệ quả 02.32); và lượng dữ liệu, đo bằng $C=I+H$ với $H$ giảm nhờ Combine (Mệnh đề 02.35) và đổi thành thời gian bằng cận $Q/B$ trên đường nối dùng chung (Mệnh đề 02.38). Mức tăng tốc $S_P$ tổng hợp các phần đó (Định nghĩa 02.39). Tuy nhiên, các thời gian điều phối, truyền và nhóm ở đây là dữ kiện cho sẵn, và số cặp của Mệnh đề 02.35 mới được tính tay. Trong Mục 5, chúng ta chạy bài đếm từ trên một cụm Hadoop và đối chiếu kết quả, số cặp với các phép tính đó.

<!-- note-topic-id: lec-02-topic-16 -->
<!-- note-collapsed -->
## Đọc thêm: Hệ thống thực thi MapReduce

Mục 4 lấy thời gian điều phối, truyền và nhóm làm dữ kiện. Các thời gian đó sinh ra từ ba việc của hệ thống: giao tác vụ cho máy, chuyển dữ liệu trung gian tới đúng tác vụ Reduce, và làm lại phần việc bị mất khi máy hỏng. Với một triệu máy, mỗi ngày khoảng 1000 máy hỏng (Nhận xét 01.3), nên việc thứ ba không phải ngoại lệ. Chúng ta theo một công việc từ lúc chia đầu vào tới lúc phục hồi. Mục 5 không dùng kết quả nào của phần đọc thêm.

### Tiến trình điều phối và giao tác vụ

::: definition Định nghĩa 02.40 (Tiến trình điều phối, tiến trình thực thi và trạng thái tác vụ)
- Chương trình của người dùng khởi tạo một **tiến trình điều phối** (Master) và nhiều **tiến trình thực thi** (Worker) trên các nút khác nhau. Tiến trình điều phối tạo $m$ tác vụ Map và $r$ tác vụ Reduce theo số do chương trình người dùng chọn, rồi giao chúng cho các tiến trình thực thi.
- Mỗi tác vụ ở một trong ba **trạng thái**: chờ (idle), đang chạy trên một tiến trình thực thi xác định, hoặc xong. Tiến trình thực thi báo cho tiến trình điều phối khi xong một tác vụ, và tiến trình điều phối giao cho nó tác vụ khác.
- Mỗi tác vụ Map được giao một hoặc nhiều khối của tệp đầu vào và tạo **một tệp trung gian cho mỗi tác vụ Reduce** trên đĩa cục bộ của máy chạy nó; tiến trình điều phối được báo vị trí, kích thước và tác vụ Reduce đích của mỗi tệp.
- Mỗi tác vụ Reduce nhận mọi tệp trung gian dành cho nó và ghi đầu ra vào một tệp của hệ thống tệp phân tán.
:::

Định nghĩa theo MMDS (§2.2.5, tr.28–29, Hình 2.3) và trang chiếu MMDS (tr.24–25). Dữ liệu trung gian nằm trên đĩa cục bộ, không có bản sao, còn đầu vào và đầu ra cuối nằm trên DFS; khác biệt đó quyết định cách phục hồi khi máy hỏng. Tiến trình điều phối khác nút chủ của DFS ở Định nghĩa 02.3: nút chủ giữ vị trí các khối của tệp, còn tiến trình điều phối giữ trạng thái các tác vụ của một công việc.

![Sáu phần dữ liệu S1 đến S6 tạo sáu tác vụ Map M1 đến M6 trên ba máy, mỗi máy chạy hai tác vụ nối tiếp: máy A chạy M1 rồi M4, máy B chạy M2 rồi M5, máy C chạy M3 rồi M6.](img/lec-02/sys-02.svg)

Hình cho thấy số tác vụ Map không phải số máy: sáu phần đầu vào $\mathrm S_1,\ldots,\mathrm S_6$, tức $X_1,\ldots,X_6$, cho sáu tác vụ trên ba máy, và máy xong tác vụ trước thì nhận tác vụ sau. Ngoài lợi ích cân bằng tải nêu ở Nhận xét 02.13, tác vụ nhỏ còn giúp phục hồi nhanh, vì một máy hỏng chỉ làm mất các tác vụ nhỏ (trang chiếu MMDS, tr.27–28).

![Hai tủ rack. Tủ 1 có máy A giữ một bản sao khối B₁ và máy B không có B₁; tủ 2 có máy C không có B₁ và máy D giữ một bản sao B₁. Map ở A hoặc D đọc tại máy; nếu Map chạy ở B thì đọc từ A trong cùng tủ; nhãn C đọc từ A đi qua đường nối giữa hai tủ.](img/lec-02/sys-03.svg)

Tiến trình điều phối ưu tiên giao tác vụ Map cho máy có bản sao khối đầu vào (trang chiếu MMDS, tr.24). Trên hình, khối đầu vào (nhãn B₁ trên hình) có bản sao ở máy $\mathrm A$ và máy $\mathrm D$, nên tác vụ Map chạy ở một trong hai máy đó đọc tại chỗ, còn chạy ở máy $\mathrm B$ thì đọc từ $\mathrm A$ qua mạng của tủ 1. Nhãn "C đọc từ A" là trường hợp bản ở $\mathrm D$ không dùng được: dữ liệu đi qua đường nối liên tủ. Tác vụ Map đọc một bản, nên hai bản sao không làm tăng số bản ghi đầu vào.

![Sơ đồ trạng thái tác vụ: Chờ chuyển sang Đang chạy khi giao việc, ghi rõ máy nhận; Đang chạy chuyển sang Hoàn tất khi báo xong, ghi vị trí đầu ra; khi mất liên lạc hoặc lỗi, tác vụ xếp lại hàng chờ.](img/lec-02/sys-07.svg)

Trạng thái "Hoàn tất" trên hình là trạng thái xong của Định nghĩa 02.40. Tiến trình điều phối định kỳ kiểm tra liên lạc với các tiến trình thực thi (MMDS, §2.2.6, tr.30); mất liên lạc quá hạn được xử lý như máy hỏng, và tác vụ đang chạy ở đó trở về hàng chờ.

<!-- note-topic-id: lec-02-topic-17 -->
### Phân phối, chuyển dữ liệu trung gian và nhóm

Hàm phân phối của Định nghĩa 02.8 được áp tại chính máy chạy Map: mỗi cặp được ghi vào tệp trung gian của tác vụ Reduce $h(k)$. Ví dụ sau tạm bỏ Combine để theo dõi từng cặp.

::: example Ví dụ 02.20 (Phân phối và chuyển trên hai văn bản)
**Dữ kiện.** $d_1=$ "mèo chó mèo" ở tác vụ Map $\mathrm M_1$, $d_2=$ "chó chim" ở $\mathrm M_2$; $r=2$ tác vụ Reduce $\mathrm R_0,\mathrm R_1$; giả sử $h(\text{mèo})=h(\text{chim})=0$, $h(\text{chó})=1$; không Combine.

**Ghi tệp trung gian.** $\mathrm M_1$ ghi tệp cho $\mathrm R_0$ gồm (mèo, 1), (mèo, 1) và tệp cho $\mathrm R_1$ gồm (chó, 1). $\mathrm M_2$ ghi tệp cho $\mathrm R_0$ gồm (chim, 1) và tệp cho $\mathrm R_1$ gồm (chó, 1).

**Chuyển.** $\mathrm R_0$ lấy tệp số 0 từ cả hai máy Map và nhận (mèo, 1), (mèo, 1), (chim, 1); $\mathrm R_1$ lấy tệp số 1 và nhận (chó, 1), (chó, 1).

**Nhóm và Reduce.** $\mathrm R_0$ nhóm thành mèo $[1,1]$, chim $[1]$ và phát (mèo, 2), (chim, 1); $\mathrm R_1$ phát (chó, 2).

**Kiểm tra lại.** Bốn tệp trung gian, đúng $m\cdot r=2\cdot2$; năm cặp, mỗi cặp ở đúng một tệp.
:::

![Quy tắc phân phối h(mèo) = 0, h(chim) = 0, h(chó) = 1. M₁ đọc d₁ = “mèo chó mèo”, tính h cho từng cặp và ghi lên đĩa cục bộ tệp cho R₀ gồm (mèo, 1), (mèo, 1) và tệp cho R₁ gồm (chó, 1). M₂ đọc d₂ = “chó chim”, ghi tệp cho R₀ gồm (chim, 1) và tệp cho R₁ gồm (chó, 1). Mũi tên dẫn các tệp tới tác vụ Reduce đích: R₀ nhận (mèo, 1), (mèo, 1), (chim, 1); R₁ nhận (chó, 1), (chó, 1).](img/lec-02/note-phan-phoi-h.svg)

Trên hình, giá trị $h$ được tính tại từng tác vụ Map, nhưng mọi tác vụ dùng cùng một hàm $h$; đó là lý do hai cặp (chó, 1) từ hai máy khác nhau cùng tới $\mathrm R_1$, đúng như giả thiết thứ tư của Mệnh đề 02.11 yêu cầu. Khung đĩa cục bộ có viền nét đứt nhắc rằng các tệp này không có bản sao.

![Đĩa của M₁ có phần 0 cho R₀ gồm mèo, mèo và phần 1 cho R₁ gồm chó; đĩa của M₂ có phần 0 gồm chim và phần 1 gồm chó. R₀ nhận mèo, mèo, chim; R₁ nhận chó, chó. Mỗi từ trên hình đại diện cho một cặp (từ, 1).](img/lec-02/sys-05.svg)

Việc mỗi tác vụ Reduce lấy các phần dành cho nó từ mọi máy Map gọi là **chuyển dữ liệu trung gian** (shuffle). Đây là bước đi qua mạng khi máy gửi và máy nhận khác nhau, và CS246 (trang chiếu 46) ghi rằng trong thực tế bước nhóm theo khóa là nút cổ chai của công việc. Nhận đủ dữ liệu chưa thay cho bước nhóm: $\mathrm R_0$ nhận hai khóa và vẫn phải tách chúng thành hai nhóm.

![R₀ sau sắp xếp có (chim,1) rồi (mèo,1), (mèo,1). Reduce theo từng khóa: chim tổng bằng 1; mèo tổng đi từ 0 lên 1 rồi 2. Kết quả (chim,1), (mèo,2). Bộ đếm đọc từng giá trị; hệ thống có thể ghép các đoạn đã sắp xếp trên đĩa.](img/lec-02/sys-06.svg)

Hệ thống sắp xếp các cặp đã nhận theo khóa, nên các cặp cùng khóa đứng liền nhau, rồi gọi Reduce cho từng đoạn. Hàm Reduce của đếm từ đọc các giá trị lần lượt và giữ một biến tổng, đi từ 0 lên 1 rồi 2 với mèo. Danh sách $L_k$ của Định nghĩa 02.8 vì vậy là một đối tượng logic: nhóm đủ phần tử nhưng không bắt buộc nằm cả trong bộ nhớ. Khi dữ liệu trung gian không vừa bộ nhớ, việc sắp xếp và ghép làm trên đĩa và tốn đọc ghi, phần đã được tính vào pha chuyển và nhóm ở Ví dụ 02.13.

<!-- note-topic-id: lec-02-topic-18 -->
### Phục hồi khi máy hỏng và tính chặn

Bảng sau ghi nơi lưu từng loại dữ liệu theo Định nghĩa 02.40 và Định nghĩa 02.3, và điều xảy ra khi mất máy lưu nó.

| Dữ liệu | Nơi lưu | Khi mất máy lưu |
|---|---|---|
| Đầu vào | DFS, có bản sao | đọc bản sao khác |
| Đầu ra Map | đĩa cục bộ của máy chạy Map | mất, phải tạo lại bằng cách chạy lại Map |
| Đầu ra Reduce đã xong | DFS, có bản sao | còn, đọc bản sao khác |

::: proposition Mệnh đề 02.41 (Phần phải chạy lại khi máy hỏng)
**Giả thiết.** Hệ thống theo Định nghĩa 02.40; mỗi khối đầu vào và mỗi tệp đầu ra còn ít nhất một bản sao đọc được; còn máy thay thế.

**Kết luận.**

- (a) Máy chạy Map hỏng: mọi tác vụ Map đã giao cho máy đó, kể cả tác vụ đã xong, trở về trạng thái chờ và được chạy lại trên máy khác; tiến trình điều phối báo cho các tác vụ Reduce vị trí mới của các tệp trung gian.
- (b) Máy chạy Reduce hỏng: các tác vụ Reduce đang chạy trên máy đó trở về trạng thái chờ và được chạy lại; tác vụ Reduce đã xong không phải chạy lại.
- (c) Máy chạy tiến trình điều phối hỏng: cả công việc phải khởi động lại.

**Điều kiện áp dụng.** Mô hình một tiến trình điều phối của MMDS.

**Phạm vi.** Mệnh đề nói phần nào phải chạy lại, không nói chạy lại cho kết quả đúng.
:::

::: proof
**Câu (a).** Đầu ra của một tác vụ Map, kể cả khi đã xong, nằm trên đĩa cục bộ của máy chạy nó (Định nghĩa 02.40), nên các tác vụ Reduce không lấy được nữa. Đầu vào của tác vụ đó còn bản sao trên DFS, nên chạy lại tác vụ ở máy khác tạo lại được đầu ra. Các tác vụ Reduce chỉ biết vị trí tệp qua tiến trình điều phối, nên tiến trình điều phối phải báo vị trí mới.

**Câu (b).** Tác vụ Reduce đã xong đã ghi đầu ra lên DFS, có bản sao, nên đầu ra còn. Tác vụ đang chạy chưa ghi xong; đầu vào của nó là các tệp trung gian, vẫn nằm trên máy Map, nên chạy lại tác vụ ở máy khác là đủ.

**Câu (c).** Trạng thái và vị trí của mọi tác vụ chỉ nằm ở tiến trình điều phối; mất nó thì không còn thông tin để biết phần nào đã xong. $\square$
:::

Kết luận theo MMDS (§2.2.6, tr.30), trang chiếu MMDS (tr.26) và CS246 (trang chiếu 47). Điểm dễ nhầm nằm ở câu (a): một tác vụ Map đã xong vẫn phải chạy lại, vì "xong" chỉ nói về trạng thái của tác vụ, còn sản phẩm của nó nằm ở nơi vừa mất. Ngược lại, tác vụ Reduce đã xong được giữ vì sản phẩm nằm trên DFS. MMDS ghi rằng một tiến trình thực thi thường chỉ chạy một loại tác vụ (§2.2.5, tr.28); một máy chạy cả tác vụ Map lẫn tác vụ Reduce mà hỏng thì áp đồng thời câu (a) và câu (b).

Chạy lại một tác vụ chỉ an toàn khi lần chạy hỏng chưa gửi một phần đầu ra cho tác vụ khác; nếu đã gửi, lần chạy lại gửi thêm một bản và đóng góp bị tính hai lần. Tính chất sau loại trừ điều đó.

::: definition Định nghĩa 02.42 (Tính chặn)
Một tác vụ có **tính chặn** (blocking property) khi nó chỉ giao đầu ra cho tác vụ kế tiếp khi chính nó đã xong.
:::

Tác vụ Map và Reduce có tính chặn (MMDS, tr.43, tr.75): tệp trung gian của một tác vụ Map chỉ được báo cho tiến trình điều phối, và do đó chỉ được tác vụ Reduce lấy, khi tác vụ Map đã xong. Một tác vụ hỏng giữa chừng vì vậy chưa giao gì cho ai.

::: proposition Mệnh đề 02.43 (Chạy lại không tính trùng)
**Giả thiết.**

- Các giả thiết của Mệnh đề 02.11.
- Mọi tác vụ có tính chặn.
- Với mỗi tác vụ, hệ thống chấp nhận đầu ra của đúng một lần chạy đã xong; với mỗi cặp tác vụ Map $j$ và tác vụ Reduce $z$, tác vụ Reduce $z$ dùng phần dành cho nó từ đúng một lần chạy đã xong của tác vụ Map $j$.

**Kết luận.** Đầu ra của công việc giống đầu ra của một lần chạy không lỗi, đến thứ tự các cặp.

**Điều kiện áp dụng.** Tiến trình điều phối không hỏng; đầu vào còn đọc được.

**Phạm vi.** Mệnh đề nói về đầu ra của công việc; tác động ra ngoài công việc của mã người dùng, như gửi thư, không được bảo đảm.
:::

::: proof
**Bước 1 (mỗi lần chạy Map cho cùng một kết quả).** Mọi lần chạy của tác vụ Map $j$ đọc cùng nội dung $X_j$, từ bản sao nào cũng vậy, và Map xác định, nên mọi lần chạy xong cho cùng các tệp trung gian như lần chạy không lỗi.

**Bước 2 (lần chạy hỏng không đóng góp).** Theo tính chặn, một lần chạy hỏng chưa giao đầu ra cho tác vụ nào. Theo giả thiết thứ ba, tác vụ Reduce $z$ nhận phần của tác vụ Map $j$ từ đúng một lần chạy đã xong. Vậy dữ liệu tác vụ Reduce $z$ nhận bằng dữ liệu của lần chạy không lỗi.

**Bước 3 (Reduce).** Mỗi lần chạy của tác vụ Reduce $z$ nhận cùng dữ liệu, và Reduce xác định, nên cho cùng đầu ra; hệ thống chấp nhận đúng một đầu ra cho mỗi tác vụ. Áp Mệnh đề 02.11 cho dữ liệu đã nhận, đầu ra là các dãy $\mathrm{Reduce}(k,L_k)$ của lần chạy không lỗi. $\square$
:::

Hai giả thiết thêm và giả thiết hàm xác định của Mệnh đề 02.11 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ tính chặn: một tác vụ Map giao (mèo, 1) đầu tiên rồi hỏng, lần chạy lại giao cả hai cặp (mèo, 1), và mèo được đếm 3.
- Bỏ "hàm xác định": một hàm Map lấy mẫu ngẫu nhiên có thể cho hai lần chạy hai mẫu khác nhau, và một tác vụ Reduce đã lấy phần của lần chạy đầu sẽ dùng mẫu khác với tác vụ Reduce lấy phần của lần chạy sau.
- Bỏ "chấp nhận một kết quả": nếu hai lần chạy xong của cùng tác vụ Reduce đều được ghi, đầu ra có hai cặp (chó, 2).

Bước 1 của chứng minh dùng giả thiết hàm xác định, Bước 2 dùng tính chặn và giả thiết thứ ba, Bước 3 dùng giả thiết thứ ba.

::: example Ví dụ 02.21 (Máy chạy Map hỏng sau khi tác vụ đã xong)
**Dữ kiện.** Như Ví dụ 02.20. Tác vụ $\mathrm M_1$ đã xong trên máy $\mathrm A$; $\mathrm R_1$ đã lấy tệp số 1 của $\mathrm M_1$, xong và ghi (chó, 2) lên DFS; máy $\mathrm A$ hỏng trước khi $\mathrm R_0$ lấy tệp số 0 của $\mathrm M_1$.

**Phần phải chạy lại.** Theo Mệnh đề 02.41(a), $\mathrm M_1$ về trạng thái chờ và chạy lại trên máy $\mathrm B$, đọc một bản sao của khối chứa $d_1$, ghi lại tệp cho $\mathrm R_0$ gồm (mèo, 1), (mèo, 1) và tệp cho $\mathrm R_1$ gồm (chó, 1). Tiến trình điều phối báo cho $\mathrm R_0$ vị trí mới; $\mathrm R_0$ lấy tệp số 0 từ máy $\mathrm B$ và từ máy chạy $\mathrm M_2$.

**Phần giữ nguyên.** $\mathrm R_1$ đã xong và đầu ra nằm trên DFS, nên theo Mệnh đề 02.41(b) không chạy lại; $\mathrm R_1$ không lấy tệp số 1 của lần chạy mới, đúng giả thiết thứ ba của Mệnh đề 02.43.

**Kiểm tra lại.** Đầu ra: (mèo, 2), (chim, 1) từ $\mathrm R_0$ và (chó, 2) từ $\mathrm R_1$, như Ví dụ 02.20; chó không bị đếm 3 dù $\mathrm M_1$ đã chạy hai lần.
:::

![Máy A hỏng; M₁ đã xong và đầu ra Map cục bộ trên máy A bị mất. Máy B còn hoạt động đọc bản sao B₁ và chạy lại M₁. Reduce đang đợi lấy phần trung gian từ địa chỉ mới. Chú thích: đầu vào còn bản sao; đầu ra trung gian đã mất phải được tính lại.](img/lec-02/sys-09.svg)

![R₀ trên máy hỏng chưa hoàn tất, đầu ra tạm bị bỏ; R₀ chạy lại trên máy khác, lấy phần trung gian, tính và ghi O₀. Hệ tệp phân tán giữ O₀ khi hoàn tất và O₁ đã có, giữ lại. Giả sử các phần trung gian Map và bản sao O₁ vẫn truy cập được.](img/lec-02/sys-10.svg)

Hình thứ nhất là câu (a) của Mệnh đề 02.41 trên Ví dụ 02.21: khối đầu vào (nhãn B₁ trên hình) còn bản sao nên $\mathrm M_1$ chạy lại được, còn đầu ra trung gian phải tính lại. Hình thứ hai là câu (b): $\mathrm R_0$ đang chạy thì máy hỏng, phần đầu ra tạm bị bỏ và $\mathrm R_0$ chạy lại từ các tệp trung gian; tệp đầu ra $\mathrm O_1$ của $\mathrm R_1$, theo nhãn trên hình, đã nằm trên DFS nên được giữ, và các tác vụ Map không phải chạy lại khi tệp trung gian của chúng còn đọc được.

::: remark Nhận xét 02.44 (Trong thực hành: máy chậm và tác vụ dự phòng)
Một máy chạy chậm, chẳng hạn vì đĩa hỏng dần hay vì chạy công việc khác, kéo dài pha chứa nó theo Định nghĩa 02.30. Gần cuối mỗi pha, hệ thống chạy thêm **bản dự phòng** (backup task) của các tác vụ còn đang chạy, và bản nào xong trước được chấp nhận (trang chiếu MMDS, tr.29). Khi đó cùng một tác vụ có hai lần chạy đồng thời, và Mệnh đề 02.43 vẫn áp được vì hệ thống chỉ chấp nhận một lần chạy. Cam kết đó chỉ áp cho đầu ra của công việc: nếu hàm Map gửi thư hay ghi vào một dịch vụ bên ngoài, hai lần chạy gửi hai lần.
:::

<!-- note-topic-id: lec-02-topic-19 -->
### Luồng công việc và Spark

Đếm từ phân biệt ở Mục 3.2 cần hai công việc nối tiếp, và PageRank ở Bài 03 cần nhiều vòng nhân ma trận–véc-tơ. Ghép nhiều công việc MapReduce khó viết, và đầu ra của mỗi công việc được ghi ra đĩa rồi công việc sau đọc lại (CS246, trang chiếu 49–50). Hệ thống **luồng công việc** mở rộng MapReduce theo hai hướng: số tầng tác vụ bất kỳ thay cho hai tầng Map, Reduce, và các hàm khác Map, Reduce (CS246, trang chiếu 51).

::: definition Định nghĩa 02.45 (Luồng công việc phi chu trình)
Một **luồng công việc phi chu trình** (acyclic workflow) là một tập hàm cùng một đồ thị có hướng không có chu trình trên các hàm đó; cung $a\to b$ nghĩa là đầu ra của hàm $a$ là một đầu vào của hàm $b$. Mỗi hàm được thực hiện bởi nhiều tác vụ, mỗi tác vụ nhận một phần đầu vào của hàm; mỗi tác vụ của hàm $a$ có một tệp đầu ra cho mỗi tác vụ của các hàm đi sau $a$.
:::

Định nghĩa theo MMDS (§2.4.1, tr.42, Hình 2.6). MapReduce là trường hợp đồ thị có hai đỉnh và một cung Map $\to$ Reduce. Trong một luồng phi chu trình, tiến trình điều phối chỉ giao tệp đầu ra của một tác vụ cho các tác vụ sau khi tác vụ đó đã xong, nên mọi tác vụ có tính chặn của Định nghĩa 02.42 và một tác vụ hỏng được chạy lại mà không lo đầu ra bị lặp (MMDS, tr.42–43). Tính chặn chỉ đúng với luồng phi chu trình (MMDS, chú thích 7, tr.43; CS246, trang chiếu 51). Mệnh đề 02.43 vì vậy áp được cho từng tác vụ của luồng.

**Spark** là một hệ luồng công việc. Dữ liệu của Spark là các **tập dữ liệu phân tán có khả năng phục hồi** (Resilient Distributed Dataset, RDD): mỗi RDD là một tệp các đối tượng cùng kiểu, chia thành các phần nằm trên nhiều máy (MMDS, §2.4.2, tr.43–44). Một chương trình Spark là dãy các **biến đổi** (transformation), mỗi biến đổi tạo một RDD từ RDD khác, kết thúc bằng các **hành động** (action), là thao tác trả một giá trị cho chương trình hoặc ghi RDD ra hệ tệp. Ba biến đổi gặp lại các hàm của chương này:

- Map của Spark áp một hàm cho mỗi phần tử và tạo đúng một phần tử; muốn mỗi văn bản sinh nhiều cặp $(w,1)$ như Map của Thuật toán 02.9, cần biến đổi **Flatmap** (MMDS, Ví dụ 2.7, tr.44);
- **Filter** giữ các phần tử thỏa một điều kiện (MMDS, Ví dụ 2.8, tr.45);
- **GroupByKey** tạo các cặp $(k,[x_1,\ldots,x_\ell])$, đúng phép nhóm theo khóa của Định nghĩa 02.8 (MMDS, tr.45–46).

Reduce của Spark là một hành động: nó gộp mọi phần tử của một RDD bằng một hàm hai ngôi và trả một giá trị; khi hàm đó kết hợp và giao hoán, kết quả không phụ thuộc thứ tự gộp (MMDS, tr.45), đúng điều Bổ đề 02.2 bảo đảm.

Spark khác MapReduce ở hai cơ chế (MMDS, §2.4.3, tr.46–47). **Tính lười** (lazy evaluation): Spark chỉ thực hiện các biến đổi khi một hành động cần kết quả, nên một phần của RDD trung gian được dùng ngay tại máy tạo ra nó và không được ghi ra đĩa hay gửi qua mạng. **Dòng dõi** (lineage): Spark ghi mỗi RDD được tạo từ RDD nào bằng biến đổi nào; khi mất một phần, Spark dựng lại phần đó từ dòng dõi thay vì đọc một bản sao. Vì vậy Spark không dựa vào tính chặn mà phục hồi bằng dòng dõi (MMDS, tr.46–47).

::: example Ví dụ 02.22 (Đếm từ bằng ba RDD và dựng lại một phần bị mất)
**Dữ kiện.** RDD $\mathcal D_0$ gồm hai văn bản $d_1=$ "mèo chó mèo" ở máy 1 và $d_2=$ "chó chim" ở máy 2, đọc từ hệ tệp. Giả sử danh sách từ cần bỏ qua là $\{\text{chim}\}$.

**Biến đổi.** Flatmap trên $\mathcal D_0$ tạo $\mathcal D_1$: phần ở máy 1 gồm (mèo, 1), (chó, 1), (mèo, 1); phần ở máy 2 gồm (chó, 1), (chim, 1). Filter bỏ các cặp có từ trong danh sách, tạo $\mathcal D_2$: phần ở máy 1 giữ nguyên ba cặp; phần ở máy 2 còn (chó, 1).

**Hành động.** Sau một biến đổi Map lấy thành phần thứ hai của mỗi cặp, hành động Reduce với phép cộng trả $1+1+1+1=4$ lần xuất hiện của các từ còn lại. Chỉ khi gặp hành động này Spark mới chạy các biến đổi, trên từng máy.

**Dựng lại.** Giả sử máy 1 hỏng sau khi tạo phần của $\mathcal D_1$ và trước khi tạo phần của $\mathcal D_2$. Dòng dõi ghi $\mathcal D_2=\mathrm{Filter}(\mathcal D_1)$, $\mathcal D_1=\mathrm{Flatmap}(\mathcal D_0)$, $\mathcal D_0$ đọc từ hệ tệp; Spark đọc lại $d_1$ từ hệ tệp trên một máy khác, chạy lại Flatmap và Filter, được lại ba cặp của phần đó.

**Kiểm tra lại.** Kho có 5 lần xuất hiện, bỏ 1 lần của chim còn 4; phần dựng lại giống phần bị mất vì hai biến đổi xác định.
:::

Phục hồi của Spark phức tạp hơn của MapReduce, đổi lại chạy nhanh hơn khi không có lỗi, và chương trình chạy càng nhanh thì càng ít khả năng gặp máy hỏng (MMDS, tr.47). CS246 (trang chiếu 60) so sánh có điều kiện: Spark xử lý dữ liệu trong bộ nhớ nên thường nhanh hơn Hadoop MapReduce, vốn ghi lại đĩa sau mỗi bước Map hay Reduce, nhưng Spark cần nhiều bộ nhớ và chậm đi khi dữ liệu không vừa bộ nhớ.

::: exercise Bài tập 02.4 (Kỳ vọng thời gian khi tác vụ hỏng; MMDS Bài 2.4.1, §2.4.7, tr.53)
Một công việc gồm $J$ tác vụ, mỗi tác vụ chạy $t_0$ giây; khi không có lỗi, tổng thời gian chạy tác vụ trên mọi máy là $Jt_0$. Xác suất một tác vụ hỏng là $\rho$ cho mỗi giây của công việc, và mỗi lần một tác vụ hỏng, việc quản lý khởi động lại thêm $10t_0$ giây vào tổng thời gian thực thi của công việc. Tính kỳ vọng của tổng thời gian thực thi. Hiểu "mỗi giây của công việc" là mỗi giây của tổng thời gian thực thi, kể cả các giây do khởi động lại thêm vào: mỗi giây như vậy có một lần hỏng với xác suất $\rho$, độc lập giữa các giây. (Sách viết $n$, $t$, $p$; ở đây ta viết $J$, $t_0$, $\rho$ vì $n$, $t_u$, $p$ đã có nghĩa khác trong chương.)
:::

::: hint
Mỗi giây của công việc, kể cả các giây do khởi động lại thêm vào, sinh trung bình $\rho$ lần hỏng. Đếm kỳ vọng số lần hỏng theo "thế hệ": lần hỏng trong $Jt_0$ giây đầu, lần hỏng trong các giây do chúng thêm vào, và cứ thế; lấy kỳ vọng có điều kiện theo số lần hỏng của thế hệ trước.
:::

::: solution
**Một khoảng cố định.** Theo tuyến tính của kỳ vọng, một khoảng cố định $\Delta$ giây có kỳ vọng $\rho\Delta$ lần hỏng.

**Số lần hỏng theo thế hệ.** Gọi $N_1$ là số lần hỏng trong $Jt_0$ giây ban đầu và $N_{\eta+1}$ là số lần hỏng trong $10t_0N_\eta$ giây do các lần hỏng của thế hệ $\eta$ thêm vào. Khi biết $N_\eta$, khoảng đó có độ dài cố định, nên
$$
\mathbb E[N_{\eta+1}\mid N_\eta]=10\rho t_0\,N_\eta .
$$
Lấy kỳ vọng hai vế, $\mathbb E[N_{\eta+1}]=10\rho t_0\,\mathbb E[N_\eta]$, với $\mathbb E[N_1]=\rho Jt_0$. Vậy $\mathbb E[N_\eta]=\rho Jt_0(10\rho t_0)^{\eta-1}$, và khi $10\rho t_0<1$, tổng số lần hỏng $N_{\text{hỏng}}=\sum_\eta N_\eta$ có kỳ vọng
$$
\begin{aligned}
\mathbb E[N_{\text{hỏng}}]&=\sum_{\eta\ge1}\rho Jt_0(10\rho t_0)^{\eta-1}\\
&=\frac{\rho Jt_0}{1-10\rho t_0}.
\end{aligned}
$$

**Tổng thời gian.** Tổng thời gian thực thi $T_{\text{tổng}}$ bằng $Jt_0$ cộng $10t_0$ nhân số lần hỏng, nên theo tuyến tính của kỳ vọng,
$$
\begin{aligned}
\mathbb E[T_{\text{tổng}}]&=Jt_0+10t_0\,\mathbb E[N_{\text{hỏng}}]\\
&=Jt_0+\frac{10\rho Jt_0^2}{1-10\rho t_0}\\
&=\frac{Jt_0}{1-10\rho t_0}.
\end{aligned}
$$
Khi $10\rho t_0\ge1$, mỗi lần hỏng sinh kỳ vọng ít nhất một lần hỏng mới, chuỗi phân kỳ và kỳ vọng không hữu hạn.

**Kiểm tra lại.** $\rho=0$ cho $\mathbb E[T_{\text{tổng}}]=Jt_0$, đúng khi không có lỗi. Với $J=100$, $t_0=10$, $\rho=0{,}001$: $10\rho t_0=0{,}1$ và $\mathbb E[T_{\text{tổng}}]=1000/0{,}9\approx1111{,}1$ giây. Nếu chỉ các giây trong $Jt_0$ giây chạy tác vụ mới có thể hỏng thì kỳ vọng là $Jt_0(1+10\rho t_0)=1100$ giây, khác kết quả trên ở các số hạng bậc hai trở lên theo $\rho t_0$.
:::

Như vậy, chúng ta đã có cơ chế đứng sau các thời gian của Mục 4: tiến trình điều phối giao tác vụ gần dữ liệu và ghi vị trí các tệp trung gian (Định nghĩa 02.40), hàm phân phối chia đầu ra Map thành $mr$ tệp trên đĩa cục bộ (Ví dụ 02.20), máy hỏng buộc chạy lại đúng các tác vụ mất sản phẩm (Mệnh đề 02.41), và tính chặn bảo đảm chạy lại không tính trùng (Định nghĩa 02.42, Mệnh đề 02.43). Luồng công việc phi chu trình giữ tính chặn cho đồ thị tổng quát hơn; Spark phục hồi bằng dòng dõi thay cho lưu dư thừa dữ liệu trung gian. Hai giới hạn còn lại: cam kết của Mệnh đề 02.43 không áp cho tác động ra ngoài công việc, và trong mô hình MMDS, tiến trình điều phối hỏng thì cả công việc phải chạy lại.

<!-- note-topic-id: lec-02-topic-20 -->
## 5. Thực hành Hadoop với Docker Compose

Theo Hệ quả 02.12, đếm từ trên $d_1=$ "mèo chó mèo" và $d_2=$ "chó chim" cho chim 1, chó 2, mèo 2; theo Ví dụ 02.5 và Mệnh đề 02.35, Map phát 5 cặp và Combine gọi một lần mỗi khóa trong mỗi tác vụ còn 4 cặp. Bộ mã nằm trong [thư mục thực hành Bài 02](examples/lec-02/hadoop-compose/README.md), tải trọn gói tại [hadoop-compose.zip](examples/lec-02/hadoop-compose.zip); hướng dẫn cài Docker và Compose ở tệp README của bộ mã.

### 5.1 Cụm sáu container trên một máy

![Cụm Hadoop gồm hai phần. HDFS lưu dữ liệu: NameNode giữ vị trí khối, DataNode 1 và DataNode 2 giữ khối và bản sao. YARN chạy tác vụ: ResourceManager cấp tài nguyên, NodeManager 1 và NodeManager 2 chạy Map và Reduce. Dòng cuối: một mạng Docker, sáu container, chung CPU và RAM của một máy.](img/lec-02/lab-cluster.svg)

Cụm gồm sáu container Docker trên một mạng: phần HDFS có NameNode, đóng vai nút chủ của Định nghĩa 02.3, và hai DataNode giữ khối với hệ số nhân bản 2; phần YARN có ResourceManager cấp tài nguyên và hai NodeManager chạy các tác vụ Map, Reduce. Container Docker là một tiến trình cô lập trên máy chủ; "container" trong giao diện YARN là đơn vị tài nguyên cấp cho một tác vụ, và số container YARN đổi theo công việc. Sáu container cùng dùng CPU, bộ nhớ và ổ đĩa của một máy, nên cụm này kiểm được tính đúng nhưng không đo được mức tăng tốc của Mục 4.5 hay mô phỏng hỏng máy độc lập.

```bash
cd hadoop-compose
docker compose pull
docker compose up -d
docker compose exec namenode hdfs dfsadmin -report
docker compose exec namenode yarn node -list
```

Lệnh `pull` tải ảnh `apache/hadoop:3.4.2-lean`, `up -d` tạo sáu container chạy nền. Cụm sẵn sàng khi báo cáo của NameNode có 2 DataNode ở trạng thái Live và danh sách của ResourceManager có 2 NodeManager ở trạng thái RUNNING; giao diện web của HDFS ở `127.0.0.1:19870`, của YARN ở `127.0.0.1:18088`.

### 5.2 Hàm Map và Reduce qua Hadoop Streaming

Hadoop Streaming cho phép viết Map và Reduce bằng một chương trình đọc dòng từ đầu vào chuẩn và in dòng ra đầu ra chuẩn. Hàm Map của Thuật toán 02.9 là tệp `mapper.py`:

```python
import sys

# Mỗi từ phân cách bởi khoảng trắng đóng góp một lần xuất hiện.
for line in sys.stdin:
    for word in line.split():
        print(f"{word}\t1")
```

Hàm Reduce là tệp `reducer.py`; cùng tệp này được khai báo làm Combine:

```python
import sys
from itertools import groupby

# Hadoop đưa các dòng cùng khóa liền nhau; đọc nhóm lần lượt.
pairs = (line.rstrip("\n").split("\t", 1) for line in sys.stdin)
for word, group in groupby(pairs, key=lambda pair: pair[0]):
    total = sum(int(value) for _, value in group)
    print(f"{word}\t{total}")
```

![Ba khối nối tiếp. Map bằng Python: stdin là các dòng văn bản, stdout là từ TAB số đếm. Hadoop: phân phối, sắp xếp, các dòng cùng khóa liền nhau. Reduce bằng Python: stdin là các dòng cùng khóa, stdout là từ TAB tổng. Ví dụ một khóa: mèo TAB 1, mèo TAB 1 cho mèo TAB 2. Hình không dùng Combine; các dòng được đọc lần lượt.](img/lec-02/lab-streaming.svg)

Hình theo một khóa qua ba khối: `mapper.py` in hai dòng `mèo TAB 1`, Hadoop phân phối và sắp xếp để hai dòng đó đứng liền nhau ở đầu vào của `reducer.py`, và `reducer.py` in `mèo TAB 2`.

::: remark Nhận xét 02.46 (Streaming hiện thực mô hình của Mục 2)
- Mỗi dòng `từ TAB 1` mà `mapper.py` in là một cặp trung gian $(w,1)$ của Định nghĩa 02.6; một dòng có $\ell$ từ cho $\ell$ dòng in ra.
- Hadoop áp hàm phân phối và sắp xếp theo khóa, nên các dòng cùng khóa tới cùng một tác vụ Reduce và đứng liền nhau; `groupby` đọc một đoạn liền nhau như một nhóm $(w,L_w)$ của Định nghĩa 02.8.
- `reducer.py` cộng lần lượt bằng một bộ sinh, không tạo danh sách cả nhóm trong bộ nhớ; đó là cách đọc $L_w$ từng phần tử của Thuật toán 02.9.
- Đầu vào và đầu ra của `reducer.py` cùng dạng `từ TAB số`, và phép cộng kết hợp, giao hoán, nên tệp này dùng được làm Combine theo Mệnh đề 02.15.
- `mapper.py` tách theo khoảng trắng và giữ chữ hoa, dấu câu; "Mèo" và "mèo," là hai từ khác "mèo". Đây là quy tắc tách từ cố định mà Định nghĩa 02.5 giả thiết.
:::

### 5.3 Nộp công việc, kết quả và bộ đếm

```bash
docker compose exec -T namenode bash /work/run-job.sh
```

Tệp `run-job.sh` chờ HDFS sẵn sàng, tạo một thư mục đầu vào mới, đưa `data/d1.txt` và `data/d2.txt` lên HDFS, rồi nộp một lệnh `hadoop jar` của Hadoop Streaming với các tham số `-mapper 'python3 mapper.py'`, `-combiner 'python3 reducer.py'`, `-reducer 'python3 reducer.py'` và `mapreduce.job.reduces=2`, tức $r=2$. Mỗi tệp nhỏ là một phần đầu vào, nên hai tệp cho $m=2$ tác vụ Map, mỗi văn bản một tác vụ như Ví dụ 02.5; tham số `split.minsize` bằng 128 MiB ngăn tách một tệp thành các phần nhỏ hơn. Mỗi lần chạy ghi vào một thư mục đầu ra mới, và `run-job.sh` in nội dung các tệp `part-*` của thư mục đó.

::: example Ví dụ 02.23 (Đối chiếu lần chạy với phép tính tay)
**Dữ kiện.** Một lần chạy `run-job.sh` với 2 tác vụ Map và 2 tác vụ Reduce; ba bộ đếm Map output records, Combine output records, Reduce output records.

**Kết quả mong đợi.** Theo README của bộ mã, ghép các tệp `part-*` được ba dòng `chim 1`, `chó 2`, `mèo 2`.

**Bộ đếm.** Map output records là 5, Combine output records là 4, Reduce output records là 3.

**Đối chiếu.** Đầu ra trùng Hệ quả 02.12 và Ví dụ 02.4. Năm cặp ra từ Map bằng $\ell_1+\ell_2=3+2$ của Mệnh đề 02.35(a); bốn cặp sau Combine bằng $2+2$ của Mệnh đề 02.35(b), tức Combine đã gộp hai cặp (mèo, 1) của $d_1$; ba cặp ra từ Reduce là ba từ phân biệt.

**Kiểm tra lại.** Mệnh đề 02.35(c) chặn $H$, tức số cặp tác vụ Reduce nhận (bộ đếm Reduce input records), giữa 4 và 5; bộ đếm Combine output records thì cộng dồn qua các lần gọi Combine và bằng 0 khi Hadoop không gọi Combine. Số 4 của lần chạy này vì vậy không cố định giữa các lần chạy, còn đầu ra cuối thì cố định theo Mệnh đề 02.15.
:::

![Ba ô bộ đếm từ lần chạy mẫu: Map tạo 5 cặp, Map output records; sau Combine 4 cặp, Combine output records; Reduce trả 3 cặp, Reduce output records. Chú thích: số bản ghi, không phải số byte hay thời gian.](img/lec-02/lab-counters.svg)

Mỗi ô trên hình là một điểm kiểm của mô hình: ô thứ nhất kiểm hàm Map, ô thứ hai kiểm Combine, ô thứ ba kiểm số khóa của bước nhóm. Bộ đếm đo số bản ghi, không đo thời gian, nên từ $5\to4$ không suy ra được Combine làm công việc nhanh hơn bao nhiêu; câu hỏi đó cần mô hình thời gian của Mục 4.

Thư mục đầu ra có hai tệp `part-*` vì $r=2$, mỗi tệp chứa các khóa mà hàm băm mặc định của Hadoop giao cho tác vụ Reduce tương ứng; một tệp có thể rỗng, và cách chia khóa không cần trùng một cách gán khóa cụ thể nào, vì Mệnh đề 02.11 chỉ cần $h$ là một hàm. Bản sao HDFS không làm tổng số đếm thành 10: mỗi khối có hai bản, nhưng mỗi phần đầu vào được một tác vụ Map đọc một lần, đúng giả thiết thứ nhất của Mệnh đề 02.11.

Như vậy, lần chạy trên cụm Hadoop cho đúng đầu ra của Hệ quả 02.12, và các bộ đếm khớp số cặp của Mệnh đề 02.35. Tuy nhiên, cụm sáu container trên một máy không đo được mức tăng tốc và không mô phỏng được hỏng máy độc lập.

<!-- note-topic-id: lec-02-topic-21 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 02.1 (Tổng kích thước trang theo máy chủ)
**Bài toán và dữ liệu.** Kho thu thập web có tệp siêu dữ liệu, mỗi dòng dạng `(URL, size, date, …)`. Cần tính, cho mỗi máy chủ, tổng số byte của mọi trang thuộc máy chủ đó (CS246, trang chiếu 62; trang chiếu MMDS, tr.34). Bốn dòng của Ví dụ 01.1, đã tách máy chủ:

- a.vn, 40 byte;
- b.vn, 25 byte;
- a.vn, 15 byte;
- c.vn, 0 byte.

**Mô hình hóa.** Map đọc một dòng và phát $(\text{máy chủ},\text{size})$; Combine và Reduce cộng các giá trị. Hàm phân phối $h(\text{máy chủ})$ giao mọi URL của một máy chủ cho cùng một tác vụ Reduce, nên cũng cho cùng một tệp đầu ra (trang chiếu MMDS, tr.32).

**Kiểm giả thiết.** Phép cộng số nguyên kết hợp, giao hoán, nên Mệnh đề 02.15 cho phép Combine với $\oplus=+$, $\phi$ đồng nhất; kích thước là số nguyên không âm theo miền đầu vào nêu sau Định nghĩa 01.1; mỗi dòng thuộc đúng một phần đầu vào, đúng giả thiết thứ nhất của Mệnh đề 02.11.

**Áp dụng.** $L_{\text{a.vn}}=[40,15]$ cho (a.vn, 55); $L_{\text{b.vn}}=[25]$ cho (b.vn, 25); $L_{\text{c.vn}}=[0]$ cho (c.vn, 0). c.vn có mặt vì Map phát cặp cả khi kích thước bằng 0.

**Chi phí.** Không Combine, $H=4$ cặp; nếu hai dòng a.vn ở cùng một tác vụ Map, Combine gộp chúng và $H=3$ cặp, theo Mệnh đề 02.35(b) với khóa là máy chủ.

**Diễn giải.** Bài 01 cần một bảng tổng đang chạy cho mọi máy chủ vừa bộ nhớ một máy; ở đây mỗi tác vụ Reduce chỉ giữ tổng của khóa đang đọc. Kiểm tra: $55+25+0=80$ bằng tổng cột kích thước.

**Giới hạn.** Số trang của các máy chủ web theo luật lũy thừa (MMDS, §1.3.6, tr.15): xếp các máy chủ theo số trang giảm dần, máy chủ thứ $\xi$ có khoảng $\beta\,\xi^{-\nu}$ trang với các hằng số $\beta,\nu>0$, nên vài máy chủ đầu có rất nhiều trang. Không có Combine, reducer của máy chủ lớn nhất có danh sách dài nhất và kéo dài pha Reduce theo Định nghĩa 02.30, hiện tượng lệch tải của Nhận xét 02.13.

**Dẫn ngược lý thuyết.** Định nghĩa 02.8, 02.30; Mệnh đề 02.11, 02.15, 02.35; Nhận xét 02.13.
:::

::: application Tình huống 02.2 (Đếm dãy năm từ)
**Bài toán và dữ liệu.** Dịch máy thống kê cần số lần xuất hiện của mọi dãy năm từ liên tiếp trong một kho văn bản lớn (CS246, trang chiếu 63; trang chiếu MMDS, tr.35).

**Mô hình hóa.** Khóa là một dãy năm từ liên tiếp trong một văn bản, giá trị là số đếm; Map phát (dãy, 1) cho mỗi vị trí bắt đầu, Combine và Reduce cộng, như Thuật toán 02.9 với "từ" thay bằng "dãy năm từ".

**Kiểm giả thiết.** Mọi văn bản dùng cùng quy tắc tách từ; Map xử lý từng văn bản, nên không dãy nào vượt qua biên giữa hai văn bản. Văn bản $d_i$ có $\ell_i$ từ sinh $\max(\ell_i-4,0)$ dãy. Chứng minh của Hệ quả 02.12 áp nguyên vẹn với $c(w)$ thay bằng số lần xuất hiện của dãy.

**Áp dụng.** Với $d_1=$ "mèo chó mèo" và $d_2=$ "chó chim", $\ell_1=3$, $\ell_2=2$, nên $\max(3-4,0)+\max(2-4,0)=0$: không có dãy năm từ nào và đầu ra rỗng, trường hợp biên $Z$ rỗng của Mệnh đề 02.11.

**Chi phí.** Không Combine, $H=\sum_i\max(\ell_i-4,0)$, và số khóa phân biệt không vượt quá số đó; đếm từ trên cùng kho có $H=\sum_i\ell_i$ và $\lvert\mathcal W\rvert$ khóa. Theo Mệnh đề 02.35(b), Combine chỉ giảm $H$ khi một dãy năm từ lặp lại trong cùng một tác vụ Map.

**Diễn giải.** Cùng khung MapReduce, chỉ đổi khóa từ một từ thành một dãy năm từ.

**Giới hạn.** Khi số dãy năm từ phân biệt gần cận $\sum_i\max(\ell_i-4,0)$, mỗi danh sách chỉ có vài phần tử, và số nhóm, số cặp đầu ra cùng gần cận đó; $H$ bằng đúng cận đó khi không Combine.

**Dẫn ngược lý thuyết.** Định nghĩa 02.5, 02.6; Hệ quả 02.12; Mệnh đề 02.11, 02.35.
:::

::: application Tình huống 02.3 (Nhân ma trận–véc-tơ khi véc-tơ không vừa bộ nhớ)
**Bài toán và dữ liệu.** Ma trận của PageRank có số chiều cỡ hàng nghìn tỷ (MMDS, tr.31), nên véc-tơ $v$ có thể không vừa bộ nhớ của một máy.

**Giả thiết bị vi phạm.** Định nghĩa 02.17 giả thiết $v$ vừa bộ nhớ của mỗi máy chạy Map.

**Hậu quả.** Mệnh đề 02.19 không dùng giả thiết bộ nhớ, nên Thuật toán 02.18 vẫn trả đúng $y$. Nhưng mỗi tác vụ Map phải đưa từng phần của $v$ từ đĩa vào bộ nhớ để nhân với các bản ghi của nó, gây rất nhiều lần truy cập đĩa (MMDS, §2.3.2, tr.32); mỗi lần là các lần truyền khối theo Định nghĩa 01.4.

**Cách sửa.** Chia $A$ thành $b$ dải dọc cùng bề rộng và $v$ thành $b$ đoạn tương ứng, chọn $b$ để một đoạn $q/b$ thành phần vừa bộ nhớ. Mỗi dải của $A$ chỉ nhân với đoạn tương ứng của $v$. Mỗi tác vụ Map nhận một phần của một dải và cả đoạn tương ứng; Map và Reduce giữ nguyên (MMDS, Hình 2.4, tr.32).

**Chi phí.** Theo Bài tập 02.3(a), với $N_A$ bản ghi và $m$ tác vụ Map, $I=N_A+mq/b$ và $H=N_A$ khi không Combine: so với Thuật toán 02.18, mỗi tác vụ Map đọc một đoạn $q/b$ thay cho cả $q$ thành phần của $v$, còn $H$ không đổi.

**Giới hạn.** PageRank lặp phép nhân, nên véc-tơ kết quả phải được chia giống véc-tơ đầu vào để làm đầu vào cho vòng sau; MMDS cho thấy khi đó chia $A$ thành các khối vuông tốt hơn chia dải (§2.3.2, tr.32; §5.2).

**Dẫn ngược lý thuyết.** Định nghĩa 02.17, 02.33; Thuật toán 02.18; Mệnh đề 02.19; Bài tập 02.3.
:::

**Ứng dụng trong các bài sau của học phần.**

- Mỗi vòng PageRank ở Bài 03 dùng dạng chia khối của Thuật toán 02.18, với Reduce có hàm hoàn tất (Mệnh đề 02.15), trên ma trận thưa và véc-tơ có thể không vừa bộ nhớ (MMDS, §2.3.1, tr.31).
- Bước nhóm theo khóa được thực hiện bằng sắp xếp và trộn các tệp đã sắp (CS246, trang chiếu 44; trang chiếu MMDS, tr.13); sắp xếp ngoài bộ nhớ là nội dung của Bài 12.
- Phép nối hai quan hệ bằng MapReduce, với khóa là thuộc tính chung, là phép nối băm song song cổ điển (MMDS, chú thích 5, tr.37); Bài 15 phân tích các thuật toán nối theo mô hình đọc ghi.

<!-- note-topic-id: lec-02-topic-22 -->
## Tóm tắt chương

Câu hỏi xuất phát của chương là đếm từ trên một kho web hơn 400 TB, mà một máy đọc ở tốc độ 35 MB/s mất khoảng 132 ngày (Ví dụ 02.1). Tính cục bộ rồi gộp cho cùng kết quả khi phép gộp kết hợp, giao hoán và mỗi phần tử góp đúng một lần (Bổ đề 02.2), còn hệ tệp phân tán lưu mỗi khối thành nhiều bản, không đặt mọi bản trong cùng một tủ (Định nghĩa 02.3). MapReduce đặc tả việc tính bằng hàm Map, hàm Reduce và phép nhóm theo khóa (Định nghĩa 02.6–02.8); khung bảo đảm mỗi khóa gặp đủ giá trị của nó đúng một lần khi đầu vào được chia theo vị trí, $h$ là một hàm và Reduce không phụ thuộc thứ tự (Mệnh đề 02.11), và Combine giữ nguyên kết quả khi Reduce có dạng $\phi(\bigoplus L)$ (Mệnh đề 02.15), trong khi trung bình trực tiếp cho 6 thay cho 5. Chọn khóa theo thành phần của đầu ra và giá trị theo trạng thái đủ để gộp cho ba thiết kế đúng: $y=(9,8,9,11)$ với khóa hàng, $D=3$ bằng hai công việc, $\mu=5$ với trạng thái $(s,\kappa)$ (Mệnh đề 02.19, 02.23, 02.26). Thêm máy không giảm tổng khối lượng tính toán $W_P=n-1$ (Mệnh đề 02.29), nhưng giảm thời gian $T_P$ khi phần truyền, gộp và điều phối không lấn át (Mệnh đề 02.31, Hệ quả 02.32); lịch bốn pha cho $S_4=2{,}4$, và Combine giảm $H$ từ 80 còn 64 byte trên hai văn bản, nên chi phí truyền thông $C=I+H$ giảm 16 byte (Mệnh đề 02.35). Trong phần đọc thêm, máy hỏng buộc chạy lại đúng các tác vụ mất sản phẩm, và tính chặn bảo đảm chạy lại không tính trùng (Mệnh đề 02.41, 02.43). Cụm Hadoop cho chim 1, chó 2, mèo 2 với 5, 4, 3 cặp ở ba bộ đếm, khớp phép tính tay. Giới hạn còn lại là các bài toán cần nhiều vòng MapReduce nối tiếp; Bài 03 dùng Thuật toán 02.18 dạng chia khối cho từng vòng PageRank.

**Định nghĩa và kết quả theo mục.**

- Mục 1: đọc kho web (Ví dụ 02.1); phép gộp kết hợp, giao hoán (Định nghĩa 02.1); gộp không phụ thuộc thứ tự và cách nhóm (Bổ đề 02.2); cụm máy và hệ tệp phân tán (Định nghĩa 02.3, Nhận xét 02.4).
- Mục 2: bài toán đếm từ (Định nghĩa 02.5); hàm Map, hàm Reduce, hàm phân phối và nhóm theo khóa (Định nghĩa 02.6–02.8); Map và Reduce cho đếm từ (Thuật toán 02.9); một công việc MapReduce (Thuật toán 02.10) và tính đúng (Mệnh đề 02.11, Hệ quả 02.12); lệch tải (Nhận xét 02.13); Combine (Định nghĩa 02.14, Mệnh đề 02.15, Nhận xét 02.16).
- Mục 3: nhân ma trận–véc-tơ (Định nghĩa 02.17, Thuật toán 02.18, Mệnh đề 02.19, Nhận xét 02.20); đếm từ phân biệt (Định nghĩa 02.21, Thuật toán 02.22, Mệnh đề 02.23); trung bình cộng (Định nghĩa 02.24, Thuật toán 02.25, Mệnh đề 02.26); quy tắc chọn khóa và trạng thái (Nhận xét 02.27).
- Mục 4: ba đại lượng chi phí (Định nghĩa 02.28); tổng khối lượng tính toán (Mệnh đề 02.29); thời gian pha và công việc (Định nghĩa 02.30, Mệnh đề 02.31, Hệ quả 02.32); chi phí truyền thông (Định nghĩa 02.33, Nhận xét 02.34, Mệnh đề 02.35, Nhận xét 02.36); thời gian truyền (Định nghĩa 02.37, Mệnh đề 02.38); mức tăng tốc (Định nghĩa 02.39).
- Đọc thêm: tiến trình điều phối và trạng thái tác vụ (Định nghĩa 02.40); phần phải chạy lại (Mệnh đề 02.41); tính chặn (Định nghĩa 02.42); chạy lại không tính trùng (Mệnh đề 02.43); tác vụ dự phòng (Nhận xét 02.44); luồng công việc phi chu trình và Spark (Định nghĩa 02.45, Ví dụ 02.22).
- Mục 5: Streaming hiện thực mô hình (Nhận xét 02.46); đối chiếu lần chạy (Ví dụ 02.23).

**Công thức và thuật toán cần nhớ.**

$$
\begin{gathered}
c(w)=\sum_{i=1}^{n}c_i(w),\\
y_i=\sum_{j=1}^{q}a_{ij}v_j,\qquad\mu=\frac{s^\ast}{\kappa^\ast}.
\end{gathered}
$$

$$
\begin{gathered}
W_P=n-1,\qquad T_{\text{pha}}=\max_ut_u,\\
T_P=\sum_{\text{pha}}T_{\text{pha}},\qquad S_P=\frac{T_1}{T_P}.
\end{gathered}
$$

$$
C=I+H,\qquad T_{\text{truyền}}\approx\lambda+\frac QB.
$$

Trên một đường nối dùng chung, chuyển $Q$ MB cần ít nhất $Q/B$ giây.

Một công việc MapReduce chia đầu vào theo vị trí, gọi Map cho mỗi cặp, nhóm các cặp theo khóa và giao nhóm $(k,L_k)$ cho tác vụ $h(k)$, rồi gọi Reduce một lần cho mỗi khóa. Combine dùng được khi Reduce là $\phi(\bigoplus L)$ với $\oplus$ kết hợp, giao hoán, và Combine phát $(k,\bigoplus L)$.

**Giả thiết hay bị bỏ quên.**

- Reduce không phụ thuộc thứ tự của $L_k$; hệ thống không bảo đảm thứ tự đó.
- Combine cần phép gộp kết hợp, giao hoán, giữ khóa và giữ kiểu $V_2$; trung bình trực tiếp không thỏa.
- Trạng thái phải đủ để gộp: trung bình cần $(s,\kappa)$, không chỉ $s/\kappa$.
- Nhân ma trận–véc-tơ giả thiết $v$ vừa bộ nhớ của mỗi máy chạy Map; bỏ giả thiết này vẫn đúng nhưng tốn đọc đĩa.
- Thời gian một pha là tải của máy chậm nhất, không phải tổng tải và không phải tác vụ dài nhất.
- $C=I+H$ của MMDS không tính đầu ra cuối; quy ước $I+2H+O$ của trang chiếu MMDS và CS246 tính.
- Cận $Q/B$ dùng băng thông của cả đường nối dùng chung, không phải của mỗi máy.
- Chạy lại không tính trùng cần tính chặn, hàm xác định và một kết quả được chấp nhận cho mỗi tác vụ (phần đọc thêm).

## Bài tập củng cố

Bài tập 02.5–02.8 nằm trong [tệp bài tập Bài 02](material-viewer.html?doc=materials/lec-02/exercises.md&deck=lecture-02-mapreduce-va-ngan-xep-xu-ly-du-lieu-lon.html), cùng gợi ý và lời giải.

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press. §2.1.1–2.1.2, tr.22–24: Mục 1.3, Định nghĩa 02.3, Nhận xét 02.4; §2.2–2.2.4, tr.25–28, Ví dụ 2.1–2.2, Hình 2.2 và hộp tr.28: Mục 2, Nhận xét 02.13, Bài tập 02.1; §2.2.5–2.2.6, tr.28–30, Hình 2.3: phần đọc thêm; §2.3, tr.30–31: Nhận xét 02.4; §2.3.1–2.3.2, tr.31–32, chú thích 3, Hình 2.4: Mục 3.1, Tình huống 02.3; §2.3.5, tr.36: Mục 3.2; chú thích 5, tr.37: mục Ứng dụng; §2.4.1–2.4.3, tr.41–47, chú thích 7, Ví dụ 2.6–2.10: phần đọc thêm; §2.5.1–2.5.2, tr.53–56: Mục 4.3, Nhận xét 02.34, 02.36; §2.7, tr.75: Định nghĩa 02.42; Bài 2.2.1, 2.3.6, 2.4.1, 2.5.1: Bài tập 02.1–02.4. Chương 1, §1.3.6, tr.15–16: Bài tập 02.1, Tình huống 02.1. Sách và trang chiếu của các tác giả: http://www.mmds.org.
- Leskovec, J., Rajaraman, A. và Ullman, J. D. Trang chiếu Chương 2 *MapReduce* của sách MMDS, bản trên http://www.mmds.org (không ghi năm). Tr.4: Ví dụ 02.1; tr.5: Mục 1.3; tr.13: Mục 2.2; tr.24–27: phần đọc thêm, Nhận xét 02.13; tr.28: Mục 4.2; tr.29: Nhận xét 02.44; tr.30: Nhận xét 02.16; tr.32: Mục 2.2, Tình huống 02.1; tr.34–35: Tình huống 02.1, 02.2; tr.38–39: Nhận xét 02.34.
- Leskovec, J. (2026). Stanford CS246, *Mining Massive Datasets*, bài 01-intro, ngày 07/01/2026. Trang chiếu 33: Mục 1.1; 35: Mục 1.3; 44: Mục 2.3; 46–47: phần đọc thêm; 49–51, 60: phần đọc thêm (luồng công việc và Spark); 62–63: Tình huống 02.1, 02.2; 67–68: Nhận xét 02.34.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press. §2.1: bất biến và quy nạp trong chứng minh Bổ đề 02.2, Mệnh đề 02.15, 02.26.
- Bộ mã thực hành `examples/lec-02/hadoop-compose/` (README, `mapper.py`, `reducer.py`, `run-job.sh`): Mục 5, Ví dụ 02.23. Lệnh và cấu hình theo tài liệu [Hadoop Streaming của Apache Hadoop 3.4.2](https://hadoop.apache.org/docs/r3.4.2/hadoop-streaming/HadoopStreaming.html).
- Ghi chú Bài 01: Định nghĩa 01.1, 01.4, 01.8, 01.13; Mệnh đề 01.5; Nhận xét 01.3; Ví dụ 01.1.
- Đọc tiếp: Bài 03 dùng Thuật toán 02.18 dạng chia khối cho từng vòng PageRank.
