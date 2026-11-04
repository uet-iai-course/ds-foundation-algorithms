# Bài 09 — Dòng dữ liệu: đếm, mômen và cửa sổ

Chúng ta xây năm phác thảo (sketch) cho năm đại lượng trên cùng một dòng: số phần tử phân biệt, mômen bậc hai, tần suất của từng phần tử, số bit 1 trong một cửa sổ gần đây và tổng có trọng số giảm theo tuổi. Mỗi phác thảo dùng bộ nhớ nhỏ hơn nhiều so với lời giải chính xác nhưng chỉ cho ước lượng, và chúng ta chứng minh ước lượng đó sai bao nhiêu, với xác suất nào.

[Bộ trang chiếu Bài 09](lecture-09-dong-du-lieu-dem-momen-va-cua-so.html) trình bày cùng chủ đề.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đặc tả các đại lượng trên dòng (tần suất, mômen $F_p$, số bit 1 trong $k$ vị trí cuối, tổng suy giảm), phân biệt phạm vi toàn dòng với phạm vi cửa sổ, và chọn phác thảo theo đại lượng, bảo đảm và chi phí (Mục 1, Mục 7).
2. Chạy Flajolet–Martin với một và nhiều hàm băm; chứng minh cận hai phía của $2^R$ và cận thất bại của trung vị; giải thích vì sao phải gộp bằng trung bình trong nhóm rồi trung vị (Mục 2).
3. Chạy biến Alon–Matias–Szegedy, chứng minh $\mathbb E[X]=F_2$ và dạng tổng quát cho $F_p$; duy trì $s$ biến trên dòng chưa biết độ dài bằng lấy mẫu hồ chứa và chứng minh trung bình các biến không chệch (Mục 3).
4. Cập nhật và truy vấn Count-Min Sketch; chứng minh ước lượng không nhỏ hơn tần suất thật, cận nhiễu kỳ vọng, cận Markov và phép khuếch đại xác suất theo số hàng; chọn số ô và số hàng theo $\varepsilon$, $\delta$, $\kappa$ (Mục 4).
5. Duy trì và truy vấn biểu diễn DGIM; chứng minh cận dưới $N$ bit cho lời giải chính xác, số thùng $O(\log N)$, bộ nhớ $O(\log^2N)$ bit, cận sai số tương đối 50% và tính đúng của phép gộp dây chuyền (Mục 5).
6. Cập nhật cửa sổ suy giảm mũ, chạy thuật toán tìm phần tử phổ biến và chứng minh số điểm được duy trì nhỏ hơn $1/(c\theta)$ (Mục 6).

<!-- note-topic-id: lec-09-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `08.k` chỉ ghi chú Bài 08, `06.k` chỉ ghi chú Bài 06. Ghi chú Bài 01 và Bài 05 chưa đánh số hiệu, nên được dẫn theo mục.

Mỗi kết quả được dẫn đều được phát biểu lại dưới đây. Trong phần phát biểu lại, các chữ $n$, $k$, $j$, $b$, $r$, $s$ là biến tạm theo ký hiệu của bài được dẫn, không mang nghĩa của bảng ký hiệu Bài 09.

- **Thuật toán dòng một lượt** (Định nghĩa 08.1). Thuật toán giữ một trạng thái; phép cập nhật nhận trạng thái sau $r-1$ phần tử cùng $x_r$ và trả trạng thái sau $r$ phần tử; phép trả lời chỉ đọc trạng thái. Mỗi phần tử được đọc đúng một lần, và kho lưu trữ không được đọc để trả lời.
- **Chi phí của thuật toán dòng và số bit của bộ đếm** (Định nghĩa 08.3; Bài 08, Mục 1.4). Thuật toán được đo bằng bộ nhớ, số phép toán mỗi phần tử, số lượt đọc dòng và sai số. Một bộ đếm nhận các giá trị $0,1,\ldots,r$ cần $\lceil\log_2(r+1)\rceil$ bit.
- **Hàm băm tất định** (giả thiết của Mệnh đề 08.10; ghi chú Bài 05, Mục 9). Một hàm băm đã chọn cho cùng giá trị trên cùng đầu vào, ở mọi lần gọi và trên mọi máy; Mệnh đề 08.10(a) dùng tính chất này để hai bộ cùng khóa luôn cùng được giữ hoặc cùng bị bỏ.
- **Bloom filter không có âm giả** (Định nghĩa 08.22, Định lý 08.25). Bloom filter đặt các bit $h_1(v),\ldots,h_k(v)$ của mỗi khóa $v$ bằng 1. Dưới bốn điều kiện (không bit nào bị xóa, truy vấn dùng đúng các hàm băm và mảng đã xây, hàm băm tất định, mọi phép ghi xong trước truy vấn), mọi khóa đã chèn nhận câu trả lời "có thể thuộc"; sai số chỉ có một phía là dương giả.
- **Mật độ bit 1** (Bổ đề 08.26). Khi $kn'$ giá trị băm độc lập và đều trên $n$ ngăn, một ngăn cho trước không nhận giá trị nào với xác suất $(1-1/n)^{kn'}$.
- **Lấy mẫu hồ chứa** (Thuật toán 08.16, Định lý 08.17). Hồ chứa có $s$ ô. Phần tử thứ $r\le s$ được ghi vào ô $r$. Với $r>s$, rút $j$ đều trên $\{1,\ldots,r\}$, độc lập với các lần rút trước; nếu $j\le s$ thì phần tử thứ $r$ thay ô $j$, nếu không thì bị bỏ. Sau $r\ge s$ phần tử, mỗi phần tử đã đọc có mặt trong hồ với xác suất $s/r$.
- **Xác suất qua các dải độc lập** (Định lý 06.7, Hệ quả 06.8). Với $b$ dải độc lập, mỗi dải trùng với xác suất $s^r$, một cặp bị bỏ sót khi mọi dải cùng không trùng, với xác suất bằng tích $(1-s^r)^b$.
- **Trung bình của các phép thử độc lập** (ghi chú Bài 05, Mục 8). Phương sai của trung bình $n$ biến độc lập cùng phân phối bằng phương sai của một biến chia cho $n$.
- **Công cụ xác suất** (học phần Xác suất thống kê; phần tiên quyết Bài 08). $\Pr(\overline E)=1-\Pr(E)$; với các biến cố độc lập toàn phần, xác suất của giao bằng tích các xác suất. Tuyến tính kỳ vọng: kỳ vọng của tổng bằng tổng các kỳ vọng, không cần độc lập; $\mathbb E[\mathbf 1[E]]=\Pr(E)$. Cận hợp (union bound): $\Pr(E_1\cup\cdots\cup E_n)\le\Pr(E_1)+\cdots+\Pr(E_n)$ (Blum, Hopcroft và Kannan, *Foundations of Data Science*, viết tắt BHK, §12.5.3, tr.422).
- **Bất đẳng thức một biến** (phần tiên quyết Bài 08). Với mọi số thực $z$, $1-z\le e^{-z}$.
- **Tổng cấp số nhân** (BHK §12.3, tr.408). Với $z\ne1$ và $n\ge1$, $1+z+\cdots+z^{n-1}=(1-z^n)/(1-z)$.
- **Quy nạp và bất biến vòng lặp** (ghi chú Bài 05, Mục 10). Bất biến vòng lặp đúng trước lượt đầu, được giữ qua mỗi lượt và cho điều cần chứng minh khi vòng lặp dừng.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một mục được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $x_1,x_2,\ldots$; $x_i$ | các phần tử của dòng theo thứ tự đến; phần tử ở vị trí $i$, cũng gọi là mốc thời gian (timestamp) $i$ | phần tử của $\mathcal U$; ở Mục 5 là bit, ở Mục 6 là số thực không âm |
| $r$ | số phần tử đã đọc, cũng là mốc thời gian của phần tử mới nhất | số nguyên không âm |
| $\mathcal U$; $u$ | tập vũ trụ (universal set) gồm mọi phần tử có thể đến; một phần tử của tập này | tập hữu hạn; phần tử của $\mathcal U$ |
| $f_u$ | tần suất của $u$ trong $x_1,\ldots,x_r$ | số nguyên không âm |
| $F_p$; $p$ | mômen bậc $p$ của dòng; bậc của mômen | số nguyên không âm; $p\in\{0,1,2,\ldots\}$ |
| $d$ | số phần tử phân biệt đã đọc, $d=F_0$ | số nguyên không âm |
| $h$; $L$ | hàm băm của thuật toán Flajolet–Martin; số bit của giá trị băm | $\mathcal U\to\{0,1\}^L$; số nguyên dương |
| $\rho(\mathbf s)$; $\ell$ | độ dài đuôi của chuỗi bit $\mathbf s$; một ngưỡng độ dài đuôi | $\{0,\ldots,L\}$ |
| $R$ | độ dài đuôi lớn nhất đã thấy | $\{0,\ldots,L\}$ |
| $q$; $g$ | số hàm băm Flajolet–Martin chạy song song; số nhóm khi gộp ước lượng | số nguyên dương, $g$ lẻ và chia hết $q$ |
| $Y_j$; $\widehat d$ | ước lượng $2^{R_j}$ của hàm băm thứ $j$; ước lượng gộp | số thực dương |
| $s$ | số biến AMS, cũng là sức chứa của hồ chứa vị trí | số nguyên dương |
| $I$; $v_i$ | vị trí được chọn của một biến AMS; số lần $x_i$ xuất hiện trong $x_i,\ldots,x_r$ | $\{1,\ldots,r\}$; số nguyên dương |
| $X$ | biến AMS, $X=r(2v_I-1)$ | số nguyên dương |
| $\kappa$; $\varepsilon$; $\delta$ | tham số phần tử nặng (ngưỡng $r/\kappa$); tham số sai số; xác suất thất bại cho phép | $\kappa\ge1$; $0<\varepsilon\le1$; $0<\delta<1$ |
| $m$; $t$ | số ô mỗi hàng Count-Min; số hàng | số nguyên dương |
| $h_j$; $A_j$ | hàm băm thứ $j$ (của Flajolet–Martin ở Mục 2, của hàng $j$ Count-Min ở Mục 4); mảng đếm của hàng $j$ | $A_j$ là mảng $m$ số nguyên không âm |
| $\widehat f_u$; $Z_j$ | ước lượng Count-Min của $f_u$; nhiễu va chạm ở hàng $j$ | số nguyên không âm |
| $N$; $k$ | độ dài cửa sổ; độ dài hậu tố được hỏi | số nguyên, $1\le k\le N$ |
| $b$; $\lvert b\rvert$; $\tau_b$ | một thùng (bucket) của DGIM; kích thước của nó, là số bit 1 nó chứa; mốc phải của nó | $\lvert b\rvert\in\{1,2,4,\ldots\}$; $\tau_b\in\{r-N+1,\ldots,r\}$ |
| $b^*$; $y_k$; $\widehat y_k$ | thùng cũ nhất có mốc phải trong $k$ vị trí cuối; số bit 1 thật trong $k$ vị trí cuối; ước lượng DGIM | số nguyên không âm; bội của $1/2$ |
| $c$ | hằng số suy giảm (decay constant) | $0<c<1$ |
| $D_r$; $D_r(u)$ | giá trị cửa sổ suy giảm mũ sau $r$ phần tử; điểm phổ biến của $u$ | số thực không âm |
| $\theta$ | ngưỡng điểm của thuật toán phần tử phổ biến | $0<\theta<1$ |
| $\Pr$; $\mathbb E$; $\operatorname{Var}$; $\mathbf 1[E]$ | xác suất; kỳ vọng; phương sai; biến chỉ báo của biến cố $E$ | |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $0{,}135$. Số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $8\,110$, hoặc viết dạng lũy thừa. $\ln$ là logarit cơ số $e$; $\log_2$ là logarit cơ số 2.
- Vị trí trên dòng đánh số từ 1; ô của một hàng Count-Min đánh số từ 0. Chuỗi bit viết bit cao bên trái, nên "đuôi" là các bit bên phải.
- Tên phần tử trong ví dụ viết chữ đứng, như $\mathrm a,\mathrm b,\mathrm c,\mathrm d$, để không lẫn với ký hiệu nghiêng, chẳng hạn thùng $b$.
- Ký hiệu cục bộ được giới thiệu tại chỗ: $\mathcal S_r$, $\lambda$, $\ell_0,\ell_1,\ell_2$, $\rho_r$, $\upsilon$, $\Psi$, $\bar Y_\gamma$, $\eta$, $G$, $M$ (trung vị), $g_0$, $\Gamma$, $E_\gamma$ (Mục 2); $i_\nu$, $\xi$, $v_i^{(r)}$, $\mathcal W_r$, $\varsigma_i$, $\tilde v_i$ (Mục 3); $a$ (chỉ số ô), $z$, $\zeta$, $P$, $w$, $\alpha$, $\beta$ (Mục 4); $\mathbf w$, $\mathbf w'$ (hai cửa sổ), $T$, $\mu$, $\pi$, $J$, $\chi$, $\omega$ (Mục 5); $\widehat D_r(u)$ là điểm được duy trì, $\Lambda$ là số điểm, $\iota_r$ (Mục 6). Chữ chỉ dùng trong một lời giải bài tập được giới thiệu trong lời giải đó.
- Nguồn trục là sách *Mining of Massive Datasets* của Leskovec, Rajaraman và Ullman (viết tắt MMDS); Count-Min theo bài giảng CS514 của Đại học Massachusetts Amherst (viết tắt UMass). Ký hiệu khác nguồn: độ dài dòng $n$ của MMDS và UMass viết là $r$, như Bài 08; số phần tử phân biệt $m$ và ngưỡng đuôi $r$ của MMDS §4.4 viết là $d$ và $\ell$; tần suất $m_i$, bậc $k$, phần tử $e(i)$ và số đếm $c(i)$ của MMDS §4.5 viết là $f_u$, $p$, $x_i$ và $v_i$; tham số $k$ và ước lượng $\tilde f(x)$ của UMass viết là $\kappa$ và $\widehat f_u$; số bit 1 thật $c$ và kích thước $2^j$ của MMDS §4.6 viết là $y_k$ và $2^\mu$; dòng $a_1,\ldots,a_t$ của MMDS §4.7 viết là $x_1,\ldots,x_r$.
- Số liệu của nguồn được dẫn tại chỗ; các số không kèm nguồn (bảng giá trị băm, bảng Count-Min $2\times3$, số ngẫu nhiên của vết chạy hồ chứa, hằng $c=1/2$, dữ kiện của Ví dụ 09.20, các tình huống và các bài tập không mang số bài sách) là dữ liệu tính tay của chương.

## Bản đồ chủ đề

Nhóm **cốt lõi** tạo mạch chính; **cầu nối** phát biểu lại tiên quyết hoặc nối hai bước suy luận; **bổ sung** lấp một khoảng trống của nguồn; **đọc thêm** không cần để đạt mục tiêu.

| Chủ đề (mã) | Nhóm | Mục | Vai trò → sản phẩm dùng tiếp |
|---|---|---|---|
| Kiến thức tiên quyết (`lec-09-topic-01`) | cầu nối | Tiên quyết | Bài 08, cận hợp, cấp số nhân → Mục 1–6 |
| Năm câu hỏi, tần suất và mômen (`lec-09-topic-02`) | cốt lõi | 1 | $f_u$, $F_p$, chi phí chính xác → Mục 2–6 |
| Đếm chính xác và giới hạn bộ nhớ (`lec-09-topic-03`) | cốt lõi; cận dưới tất định là bổ sung | 2.1 | 512 MiB một dòng → nhu cầu ước lượng |
| Đuôi băm và ước lượng $2^R$ (`lec-09-topic-04`) | cốt lõi | 2.2 | $\rho$, $R$, bất biến → phân tích xác suất |
| Ngưỡng hai phía (`lec-09-topic-05`) | cốt lõi; dạng bất đẳng thức là bổ sung | 2.3 | Cận $1/\lambda$, $e^{-\lambda/2}$ → nhu cầu gộp |
| Phân phối đuôi nặng và gộp ước lượng (`lec-09-topic-06`) | cốt lõi; cận kỳ vọng và mẹo trung vị là bổ sung | 2.4 | Trung bình rồi trung vị → Mục 3.5 |
| Chi phí, hợp nhất, thực hành (`lec-09-topic-07`) | cốt lõi | 2.5 | Bộ nhớ theo bit → Tình huống 09.1 |
| Biến AMS (`lec-09-topic-08`) | cốt lõi | 3.1 | $v_i$, $X=r(2v_I-1)$ → không chệch |
| Tính không chệch (`lec-09-topic-09`) | cốt lõi; tổng các số lẻ là cầu nối | 3.2 | $\mathbb E[X]=F_2$ → Mục 3.3–3.4 |
| Mômen bậc cao (`lec-09-topic-10`) | cốt lõi, chu trình rút gọn vì cùng chứng minh | 3.3 | $r(v^p-(v-1)^p)$ → Bài tập 09.13–09.14 |
| AMS trên dòng chưa biết độ dài (`lec-09-topic-11`) | cốt lõi; bất biến giá trị và hệ quả trung bình là bổ sung | 3.4–3.5 | Hồ chứa vị trí → Tình huống 09.3 |
| Bài toán phần tử nặng (`lec-09-topic-12`) | cốt lõi, chu trình rút gọn vì là đặc tả | 4.1 | Bài toán $(\varepsilon,\kappa)$ → tham số $m$ |
| Họ băm phổ dụng, bất đẳng thức Markov (`lec-09-topic-13`) | cầu nối | 4.2 | Cận va chạm, Markov → Mục 4.4 |
| Bảng Count-Min (`lec-09-topic-14`) | cốt lõi | 4.3 | $t$ hàng, $m$ ô, cực tiểu → bảo đảm |
| Bảo đảm Count-Min (`lec-09-topic-15`) | cốt lõi; cận hợp cho mọi phần tử là bổ sung | 4.4 | Sai số $\varepsilon r/\kappa$, xác suất $\delta$ → nhu cầu cửa sổ |
| Cận dưới $N$ bit (`lec-09-topic-16`) | cốt lõi | 5.1 | Lời giải chính xác cần $N$ bit → nhu cầu xấp xỉ |
| Thùng, sáu quy tắc, bộ nhớ (`lec-09-topic-17`) | cốt lõi; chứng minh đầy đủ số thùng là bổ sung | 5.2 | $O(\log^2N)$ bit → truy vấn |
| Truy vấn và cận 50% (`lec-09-topic-18`) | cốt lõi | 5.3 | $\tfrac12y_k\le\widehat y_k\le\tfrac32y_k$ → cập nhật |
| Cập nhật DGIM (`lec-09-topic-19`) | cốt lõi; tính đúng và khấu hao là bổ sung | 5.4 | Gộp hai thùng cũ nhất → chi phí |
| Mở rộng DGIM (`lec-09-topic-20`) | đọc thêm | 5.5 | Giảm sai số, tổng số nguyên → Mục 6 |
| Cửa sổ suy giảm (`lec-09-topic-21`) | cốt lõi; tổng hữu hạn $<1/c$ là cầu nối | 6.1 | Truy hồi $D_r$ → phần tử phổ biến |
| Phần tử phổ biến hiện thời (`lec-09-topic-22`) | cốt lõi; chứng minh đầy đủ cận là bổ sung | 6.2 | Ít hơn $1/(c\theta)$ điểm → Mục 7 |
| Chọn cấu trúc theo câu hỏi (`lec-09-topic-23`) | cốt lõi | 7 | Hai bảng đối chiếu → tình huống |
| Tình huống áp dụng và ứng dụng (`lec-09-topic-24`) | cốt lõi | Tình huống | Ba bài toán, một vi phạm giả thiết → tóm tắt |
| Tóm tắt chương (`lec-09-topic-25`) | cốt lõi | Tóm tắt | Chuỗi kết quả → Bài 10 |
| Bài tập củng cố (`lec-09-topic-26`) | cốt lõi | Bài tập | Ba mức, năm bài recitation → sáu mục tiêu |
| Đọc thêm và tài liệu (`lec-09-topic-27`) | đọc thêm | Tham khảo | HyperLogLog, BHK §6.2, giảm sai số DGIM |

Quan hệ tiên quyết: Mục 1 là đầu vào của mọi mục; Mục 3 dùng phép gộp của Mục 2.4 và Định lý 08.17; Mục 4 dùng cận hợp và bất đẳng thức Markov; Mục 5 chỉ cần Mục 1 và mô hình dòng của Bài 08; Mục 6 mở từ giới hạn của cửa sổ trượt ở Mục 5; mọi nhánh gặp nhau ở Mục 7.

<!-- note-topic-id: lec-09-topic-02 -->
## 1. Năm câu hỏi trên một dòng

Bài 08 xây ba cấu trúc trên dòng: mẫu theo khóa, hồ chứa với xác suất có mặt $s/r$ (Định lý 08.17) và Bloom filter không có âm giả (Định lý 08.25). Ví dụ 08.17 của Bài 08 để ngỏ yêu cầu thứ tư, đếm số người dùng phân biệt trong tháng, vì cả ba cấu trúc đều không trả lời được.

Ở trang không yêu cầu đăng nhập, người dùng được nhận diện theo địa chỉ IP (MMDS Ví dụ 4.5, tr.142); khi đếm riêng cho từng trang, mỗi trang là một dòng, và cấu trúc chính xác cho mọi dòng không vừa bộ nhớ chính (§4.4.1, tr.142–143). Trên dòng lượt nhấp của các trang Yahoo!, hàng tỷ phần tử mỗi ngày (§4.1.2, tr.133), các câu hỏi khác gặp cùng giới hạn: phần tử nào xuất hiện nhiều, phân bố lệch đến đâu, bao nhiêu sự kiện gần đây.

Chúng ta tách năm câu hỏi như vậy, đặt cho mỗi câu hỏi một đại lượng có định nghĩa chính xác, và với mỗi đại lượng xây một phác thảo cùng bảo đảm sai số, xác suất thất bại và bộ nhớ. Hình dưới cho cấu trúc của chương.

![Sơ đồ đọc từ trên xuống: một dòng phần tử x1, x2, … đi vào năm khối song song, mỗi khối ghi câu hỏi, đại lượng, phác thảo và bảo đảm. Mục 2: bao nhiêu phần tử phân biệt, F0, Flajolet–Martin, xác suất hai phía. Mục 3: phân bố lệch đến đâu, F2, biến AMS, kỳ vọng đúng bằng F2. Mục 4: phần tử u xuất hiện bao nhiêu lần, f_u, Count-Min, không thấp và sai số nhỏ với xác suất cao. Mục 5: bao nhiêu bit 1 trong k vị trí cuối, y_k, DGIM, sai số tương đối tối đa 50%. Mục 6: phần tử nào phổ biến gần đây, D_r(u), cửa sổ suy giảm mũ, ít hơn 2/c điểm. Mục 5 và Mục 6 có nhãn gần đây, ba khối còn lại có nhãn toàn dòng; năm mũi tên hội tụ vào khối Mục 7, chọn cấu trúc theo câu hỏi.](img/lec-09/cau-truc-chuong-09.svg)

Hình đọc từ trên xuống: ba khối đầu hỏi về toàn dòng, hai khối sau về phần gần đây, và cả năm gặp lại ở Mục 7.

### 1.1 Tần suất và mômen

Chúng ta đặt năm câu hỏi trên một dòng ngắn, đủ nhỏ để tính tay mọi đại lượng.

::: example Ví dụ 09.1 (Năm câu hỏi trên dòng mười lăm phần tử)
**Dữ kiện.** Dòng gồm mười lăm phần tử, theo thứ tự đến:

$$
\begin{gathered}
\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\\
\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}.
\end{gathered}
$$

Dòng lấy từ MMDS Ví dụ 4.7 (tr.146).

**Tính.** Các vị trí của từng phần tử là

- $\mathrm a$: 1, 6, 9, 13, 14, tức 5 lần;
- $\mathrm b$: 2, 4, 10, 15, tức 4 lần;
- $\mathrm c$: 3, 7, 12, tức 3 lần;
- $\mathrm d$: 5, 8, 11, tức 3 lần.

Năm câu hỏi có năm câu trả lời:

1. Số phần tử phân biệt là 4.
2. Phần tử $\mathrm a$ xuất hiện 5 lần.
3. Tổng bình phương số lần xuất hiện là $5^2+4^2+3^2+3^2=59$.
4. Trong 8 phần tử cuối (vị trí 8 đến 15), $\mathrm a$ xuất hiện 3 lần, ở vị trí 9, 13, 14.
5. Phần tử "phổ biến gần đây" cần một định nghĩa; với định nghĩa của Mục 6 và hằng số suy giảm $c=1/2$, $\mathrm b$ đứng đầu dù $\mathrm a$ xuất hiện nhiều hơn.

**Kiểm tra lại.** $5+4+3+3=15$, bằng độ dài dòng.
:::

Câu 4 cần thêm vị trí, câu 5 cần một cách cân thời gian. Một cách trực quan, câu 1 đến câu 3 tóm tắt cùng một bảng tần suất thành một số: đếm số hàng, đọc một hàng, hay cộng bình phương các hàng. Định nghĩa 09.1 gom chúng vào một họ.

::: definition Định nghĩa 09.1 (Tần suất và mômen bậc $p$)
Cho dòng $x_1,\ldots,x_r$ gồm các phần tử của tập vũ trụ $\mathcal U$.

- **Tần suất** (frequency) của $u\in\mathcal U$ là số vị trí mang $u$:
$$
f_u=\bigl\lvert\{i\le r: x_i=u\}\bigr\rvert .
$$
- **Mômen bậc $p$** (moment of order $p$, $p$-th moment), với $p$ nguyên không âm, là
$$
F_p=\sum_{u\in\mathcal U}f_u^{\,p},
$$
với quy ước $0^0=0$.

Ba trường hợp có tên riêng: $F_0$ là **số phần tử phân biệt** (number of distinct elements), ký hiệu $d$; $F_1=r$ là độ dài dòng; $F_2$ còn gọi là **số bất ngờ** (surprise number).
:::

Tần suất $f_u$ là một hàng của bảng tần suất, còn $F_p$ cộng lũy thừa bậc $p$ của mọi hàng; quy ước $0^0=0$ khiến phần tử có $f_u=0$ không góp vào $F_0$, nên $F_0$ đếm đúng các phần tử đã xuất hiện (MMDS §4.5.1, tr.145, chú thích 4). Vì $\sum_uf_u=r$, mômen bậc một luôn bằng độ dài dòng và chỉ cần một bộ đếm.

Ví dụ 09.1 nằm trong định nghĩa ở ba chỗ: câu 1 là $F_0=d=4$, câu 2 là $f_{\mathrm a}=5$, câu 3 là $F_2=59$.

Mômen bậc hai đo độ lệch của phân bố: với cùng độ dài và cùng số phần tử phân biệt, phân bố càng lệch thì $F_2$ càng lớn. Ví dụ sau của MMDS cho hai đầu của khoảng giá trị.

::: example Ví dụ 09.2 (Hai phân bố cùng độ dài)
**Dữ kiện.** Một dòng dài $r=100$ có $d=11$ phần tử phân biệt (MMDS Ví dụ 4.6, tr.145–146).

**Phân bố đều nhất.** Một phần tử xuất hiện 10 lần, mười phần tử mỗi phần tử 9 lần:
$$
\begin{aligned}
F_2&=10^2+10\cdot9^2\\
&=100+810=910 .
\end{aligned}
$$

**Phân bố lệch nhất.** Một phần tử xuất hiện 90 lần, mười phần tử mỗi phần tử 1 lần:
$$
\begin{aligned}
F_2&=90^2+10\cdot1^2\\
&=8\,100+10=8\,110 .
\end{aligned}
$$

**Kiểm tra lại.** $10+10\cdot9=100$ và $90+10\cdot1=100$.
:::

Bài tập 09.18 chứng minh 910 và $8\,110$ là giá trị nhỏ nhất và lớn nhất của $F_2$ khi $r=100$, $d=11$; theo cùng công thức, với $r=15$, $d=4$ hai giá trị này là 57 và 147, nên $F_2=59$ cho biết dòng mười lăm phần tử gần đều.

Hai nhầm lẫn thường gặp: coi $F_0$ là độ dài dòng, trong khi độ dài là $F_1$; và coi $F_2$ là $F_1^2$, trong khi trên Ví dụ 09.1, $F_1^2=225$ còn $F_2=59$.

### 1.2 Phạm vi thời gian và chi phí của lời giải chính xác

Câu 4 và câu 5 của Ví dụ 09.1 hỏi về phần gần đây của dòng, nhưng theo hai cách: câu 4 chỉ đếm một số vị trí cuối, câu 5 cho phần tử càng cũ trọng số càng nhỏ. Định nghĩa sau đặt tên cho cách thứ nhất.

::: definition Định nghĩa 09.2 (Cửa sổ trượt)
Cho dòng $x_1,\ldots,x_r$ và số nguyên $N\ge1$. **Cửa sổ trượt** (sliding window) độ dài $N$ là đoạn $N$ phần tử cuối $x_{r-N+1},\ldots,x_r$ (cả dòng nếu $r<N$). Vị trí $i$ **còn trong cửa sổ** khi $r-N+1\le i\le r$. Mỗi phần tử mới đến làm cửa sổ dịch sang phải một vị trí.
:::

Câu 4 hỏi tần suất của $\mathrm a$ trên cửa sổ $N=8$, một đại lượng của Định nghĩa 09.1 tính trên đoạn cuối dòng, nên đổi theo $r$ ngay cả khi phần tử mới không phải $\mathrm a$.

::: remark Nhận xét 09.3 (Chi phí của lời giải chính xác và đơn vị đếm)
Bảng ghi trạng thái mà cách làm hiển nhiên giữ cho từng câu hỏi.

| Câu hỏi | Đại lượng | Lời giải chính xác | Bộ nhớ |
|---|---|---|---|
| số phần tử phân biệt | $F_0=d$ | bảng băm hoặc cây tìm kiếm chứa các phần tử đã gặp (MMDS §4.4.1, tr.142) | $d$ phần tử |
| tần suất | $f_u$ | một bộ đếm cho mỗi phần tử đã gặp | $d$ bộ đếm |
| độ lệch | $F_2$ | như trên, rồi cộng bình phương (MMDS §4.5.1, tr.146) | $d$ bộ đếm |
| bit 1 trong $k$ vị trí cuối | $y_k$ | giữ $N$ bit cuối (MMDS §4.6, tr.150) | $N$ bit |
| phần tử phổ biến gần đây | $D_r(u)$ với mọi $u$ | một điểm cho mỗi phần tử đã gặp, cập nhật theo truy hồi của Mục 6 | $d$ số |

Với tập vũ trụ là các địa chỉ IPv4, $\lvert\mathcal U\rvert=2^{32}\approx4{,}3\cdot10^9$. Một vector bit đánh dấu mọi địa chỉ đã gặp cần $2^{32}$ bit, tức $2^{29}$ byte $=512$ MiB cho mỗi dòng. Với cửa sổ $N=10^9$ lượt (trang chiếu Stanford CS246 2017, Streams 1, tr.13), giữ $N$ bit cho một URL tốn $10^9/8$ byte $=125$ MB.

Bài 08 đo bộ nhớ bằng từ máy (Định nghĩa 08.3); với Flajolet–Martin và DGIM, chúng ta đếm theo bit, vì đếm bằng từ máy sẽ che mất thừa số $\log N$ khi so $O(\log^2N)$ bit với $N$ bit.
:::

Cả năm hàng đều tỷ lệ với $d$ hoặc $N$; riêng tổng suy giảm $D_r$ của một dòng số chỉ cần một số. Với số phần tử phân biệt và số bit 1 trong cửa sổ, mọi thuật toán tất định trả đáp số chính xác đều cần chừng ấy bit (Nhận xét 09.4, Mệnh đề 09.41); vì vậy các phác thảo của chương dùng tính ngẫu nhiên hoặc chấp nhận sai số.

::: exercise Bài tập 09.1 (Các mômen của dòng mười lăm phần tử)
Cho dòng $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$ (MMDS Ví dụ 4.7). Tính $F_0$, $F_1$, $F_3$. Câu hỏi "trong 5 phần tử cuối, $\mathrm b$ xuất hiện mấy lần" có tính được từ bảng tần suất $f_u$ không? Giải thích.
:::

::: hint
Dùng bảng vị trí của Ví dụ 09.1; với câu hỏi cuối, xét một dòng khác có cùng bảng tần suất.
:::

::: solution
Tần suất là $f_{\mathrm a}=5$, $f_{\mathrm b}=4$, $f_{\mathrm c}=f_{\mathrm d}=3$. Do đó $F_0=4$, $F_1=5+4+3+3=15$ và $F_3=125+64+27+27=243$.

Câu hỏi cuối không tính được từ bảng tần suất: trên dòng đã cho, 5 phần tử cuối là $\mathrm d,\mathrm c,\mathrm a,\mathrm a,\mathrm b$, đáp số 1, còn dòng $\mathrm a,\mathrm c,\mathrm d,\mathrm a,\mathrm c,\mathrm d,\mathrm a,\mathrm d,\mathrm c,\mathrm a,\mathrm a,\mathrm b,\mathrm b,\mathrm b,\mathrm b$ có cùng bảng tần suất nhưng cho đáp số 4.
:::

Như vậy, chúng ta đã đặt năm câu hỏi thành các đại lượng có định nghĩa (Định nghĩa 09.1, 09.2) và đếm chi phí của lời giải chính xác (Nhận xét 09.3): cả năm đại lượng cần bộ nhớ tỷ lệ với số phần tử phân biệt hoặc độ dài cửa sổ. Tuy nhiên, mới chỉ có lời giải chính xác. Trong Mục 2, chúng ta bắt đầu với $F_0$ và xây một ước lượng chỉ cần một số nhỏ cho mỗi hàm băm.

## 2. Đếm phần tử phân biệt bằng Flajolet–Martin

Bài toán đếm phần tử phân biệt (count-distinct problem) hỏi $F_0=d$ của dòng đã đọc (MMDS §4.4.1, tr.142). Với dòng địa chỉ IP của một trang, vector bit chính xác cần 512 MiB (Nhận xét 09.3). Trong ba lối ra MMDS nêu (thêm máy, đưa cấu trúc xuống đĩa, hoặc chỉ ước lượng; tr.142–143), chúng ta theo lối thứ ba: giữ một số nhỏ cho mỗi hàm băm, chặn sai số của nó, rồi gộp nhiều hàm băm.

<!-- note-topic-id: lec-09-topic-03 -->
### 2.1 Đếm chính xác và giới hạn bộ nhớ

Lời giải chính xác giữ tập các phần tử đã gặp, nên bộ nhớ tăng theo $d$. Nhận xét sau cho biết không thuật toán tất định nào tránh được điều đó khi đòi đáp số đúng.

::: remark Nhận xét 09.4 (Đếm chính xác tất định cần nhiều bộ nhớ)
Mọi thuật toán tất định trả đúng số phần tử phân biệt phải dùng ít nhất $\lvert\mathcal U\rvert$ bit trên một số dòng có độ dài $\lvert\mathcal U\rvert+1$ (BHK §6.2.1, tr.183). Với ít bit hơn, hai tập phần tử khác nhau đã đọc cho cùng trạng thái. Nếu hai tập khác cỡ, thuật toán sai ngay ở một trong hai dòng; nếu cùng cỡ, đọc thêm một phần tử thuộc tập này mà không thuộc tập kia làm hai đáp số đúng khác nhau trong khi trạng thái vẫn như nhau.
:::

Với $\mathcal U$ là các địa chỉ IPv4, cận này đúng bằng 512 MiB, nên muốn ít bộ nhớ hơn, thuật toán phải dùng tính ngẫu nhiên hoặc được phép sai; Flajolet–Martin dùng cả hai.

<!-- note-topic-id: lec-09-topic-04 -->
### 2.2 Đuôi băm và ước lượng $2^R$

Một cách trực quan, càng nhiều phần tử phân biệt thì càng nhiều giá trị băm khác nhau, và càng dễ gặp một giá trị "hiếm" (MMDS §4.4.2, tr.143). Tính chất hiếm được chọn là kết thúc bằng nhiều bit 0: chuỗi ngẫu nhiên kết thúc bằng ít nhất $\ell$ bit 0 với xác suất $2^{-\ell}$, nên cần cỡ $2^\ell$ phần tử phân biệt mới có cơ hội thấy nó, và số bit 0 cuối dài nhất đã thấy cho biết cỡ của $d$. Ví dụ 09.3 tính nó trên bốn phần tử.

::: example Ví dụ 09.3 (Đuôi băm của bốn phần tử)
**Dữ kiện.** Dòng mười lăm phần tử $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$ có bốn phần tử phân biệt; một hàm băm $h_1$ cho bốn giá trị 5 bit:

| Phần tử | $\mathrm a$ | $\mathrm b$ | $\mathrm c$ | $\mathrm d$ |
|---|---|---|---|---|
| $h_1$ | $10110$ | $01011$ | $11100$ | $00111$ |
| số bit 0 ở cuối | 1 | 0 | 2 | 0 |

**Tính.** Đọc dòng từ trái sang phải, số bit 0 cuối dài nhất đã thấy là 1 sau $\mathrm a$, 1 sau $\mathrm b$, 2 sau $\mathrm c$, rồi giữ 2 đến hết dòng, vì $\mathrm d$ có đuôi 0 và các phần tử lặp lại cho đúng độ dài đuôi đã thấy. Ước lượng $2^2=4$.

**Kiểm tra lại.** Dòng có đúng 4 phần tử phân biệt.
:::

::: definition Định nghĩa 09.5 (Độ dài đuôi và ước lượng Flajolet–Martin)
Cho hàm băm $h:\mathcal U\to\{0,1\}^L$.

- **Độ dài đuôi** (tail length), còn gọi là số bit 0 ở cuối (number of trailing zeros), của chuỗi $\mathbf s\in\{0,1\}^L$ là số bit 0 liên tiếp ở cuối $\mathbf s$, ký hiệu $\rho(\mathbf s)$; với chuỗi toàn 0 đặt $\rho(0^L)=L$.
- Sau dòng $x_1,\ldots,x_r$ với $r\ge1$, **độ dài đuôi lớn nhất** là $R=\max_{1\le i\le r}\rho(h(x_i))$.
- **Ước lượng Flajolet–Martin** của $d$ là $2^R$; với dòng rỗng, ước lượng là 0.
:::

Hàm $\rho$ chỉ nhìn vào các bit cuối: $\rho(01100)=2$ (giá trị băm 12, trang chiếu MMDS, Streams 2, tr.20), còn $\rho(01011)=0$. Quy ước $\rho(0^L)=L$ cần vì chuỗi băm hữu hạn (MMDS chú thích 3, tr.144). Ước lượng $2^R$ luôn là lũy thừa của 2; Ví dụ 09.3 là trường hợp $L=5$, $R=2$.

Khác với Bloom filter (Định nghĩa 08.22), vốn ghi một bit cho mỗi giá trị băm, ước lượng Flajolet–Martin chỉ giữ một số, chiều dài của đuôi dài nhất, và số này dao động mạnh theo hàm băm.

::: example Ví dụ 09.4 (Ba hàm băm khác trên cùng dòng)
**Dữ kiện.** Dòng mười lăm phần tử của Ví dụ 09.3, $d=4$. Ba hàm băm 5 bit khác:

| Hàm | $\mathrm a$ | $\mathrm b$ | $\mathrm c$ | $\mathrm d$ | độ dài đuôi của $\mathrm a,\mathrm b,\mathrm c,\mathrm d$ | $R$ | $2^R$ |
|---|---|---|---|---|---|---:|---:|
| $h_3$ | $11001$ | $00110$ | $01011$ | $10101$ | $0,1,0,0$ | 1 | 2 |
| $h_4$ | $00011$ | $11000$ | $10101$ | $01110$ | $0,3,0,1$ | 3 | 8 |
| $h_5$ | $10001$ | $01010$ | $10000$ | $01111$ | $0,1,4,0$ | 4 | 16 |

**Tính.** Với mỗi hàm, $R$ là số lớn nhất trong bốn độ dài đuôi; ước lượng lần lượt là 2, 8 và 16.

**Diễn giải.** Một hàm ước lượng thấp một nửa, hai hàm thừa gấp 2 và gấp 4; riêng $h_5$ cho $\mathrm c$ đuôi dài 4, biến cố có xác suất $1/16$ cho một phần tử, đủ đẩy ước lượng lên 16.

**Kiểm tra lại.** $\rho(11000)=3$, $\rho(10000)=4$, $\rho(01110)=1$.
:::

Hai ví dụ trên chạy cùng một thủ tục: băm từng phần tử, lấy độ dài đuôi, giữ số lớn nhất.

::: algorithm Thuật toán 09.6 (Flajolet–Martin với một hàm băm)
**Đầu vào.** Dòng $x_1,x_2,\ldots$ gồm phần tử của $\mathcal U$; hàm băm $h:\mathcal U\to\{0,1\}^L$ chọn trước khi dòng bắt đầu.

**Đầu ra.** Khi có truy vấn, ước lượng $2^R$ của $d$.

**Giả thiết.** $h$ tất định; tính được $h(x)$ và $\rho(h(x))$ trong $O(1)$ phép trên từ máy.

1. Khởi tạo $R\gets-\infty$, nghĩa là chưa đọc phần tử nào.
2. Khi $x$ đến: tính $\ell\gets\rho(h(x))$; nếu $\ell>R$ thì đặt $R\gets\ell$.
3. Khi có truy vấn: nếu $R=-\infty$ thì trả 0; ngược lại trả $2^R$.

```text
FM(x_1, x_2, …; h)
    R ← −∞
    với mỗi phần tử x đến:
        ℓ ← số bit 0 ở cuối h(x)      (bằng L nếu h(x) toàn 0)
        nếu ℓ > R: R ← ℓ
    truy vấn: trả 0 nếu R = −∞, ngược lại trả 2^R
```

**Dừng.** Mỗi phần tử được xử lý sau số bước không đổi.

**Trường hợp biên.** Dòng rỗng trả 0. Phần tử lặp lại cho cùng $\ell$, nên không đổi $R$.

**Chi phí.** Mỗi phần tử, trong trường hợp xấu nhất: 1 phép băm, 1 phép đếm bit 0 cuối, 1 phép so sánh. Bộ nhớ: một số $R\in\{0,\ldots,L\}$, tức $\lceil\log_2(L+1)\rceil$ bit, cộng 1 bit đánh dấu chưa đọc phần tử nào và phần lưu hàm băm.
:::

Phép quyết định là phép so sánh ở bước 2, và mọi thông tin về các phần tử đã qua chỉ còn trong $R$; mệnh đề sau nói chính xác $R$ giữ điều gì.

::: proposition Mệnh đề 09.7 (Bất biến và hợp nhất của $R$)
**Giả thiết.** $h$ tất định. Ký hiệu $\mathcal S_r=\{u\in\mathcal U: f_u>0\}$ là tập phần tử phân biệt sau $r\ge1$ phần tử.

**Kết luận.**

- (a) Sau $r$ phần tử, Thuật toán 09.6 giữ $R=\max_{u\in\mathcal S_r}\rho(h(u))$; do đó $R$ chỉ phụ thuộc tập $\mathcal S_r$, không phụ thuộc thứ tự hay số lần lặp.
- (b) Nếu hai dòng được xử lý riêng bằng cùng hàm $h$, cho $R'$ và $R''$, thì giá trị $R$ của dòng ghép bằng $\max(R',R'')$.

**Điều kiện áp dụng.** Mọi dòng, không cần giả thiết xác suất.

**Phạm vi.** Mệnh đề nói về trạng thái, không nói ước lượng gần $d$.
:::

::: proof
**Bước 1 (bất biến, quy nạp theo $r$).** Đặt $\mathcal S_0=\varnothing$ và quy ước max trên tập rỗng là $-\infty$; khi đó bất biến "$R=\max_{u\in\mathcal S_r}\rho(h(u))$" đúng với $r=0$ theo bước 1 của thuật toán. Giả sử nó đúng sau $r-1$ phần tử. Với $\rho_r=\rho(h(x_r))$, bước 2 đặt

$$
\begin{aligned}
&R_{\text{mới}}\\
&\quad=\max(R,\ \rho_r)\\
&\quad=\max\Bigl(\max_{u\in\mathcal S_{r-1}}\rho(h(u)),\ \rho_r\Bigr)\\
&\quad=\max_{u\in\mathcal S_{r-1}\cup\{x_r\}}\rho(h(u))\\
&\quad=\max_{u\in\mathcal S_r}\rho(h(u)).
\end{aligned}
$$

Bốn đẳng thức lần lượt dùng bước 2 của Thuật toán 09.6, giả thiết quy nạp, max trên hợp hai tập và $\mathcal S_r=\mathcal S_{r-1}\cup\{x_r\}$.

**Bước 2 (chỉ phụ thuộc tập).** Vế phải của bất biến là một hàm của $\mathcal S_r$. Tính tất định của $h$ được dùng ở đây: cùng phần tử luôn cho cùng $\rho(h(u))$, nên một phần tử xuất hiện nhiều lần chỉ góp một giá trị.

**Bước 3 (hợp nhất).** Tập phần tử phân biệt của dòng ghép là $\mathcal S'\cup\mathcal S''$, nên theo Bước 1, $R=\max_{u\in\mathcal S'\cup\mathcal S''}\rho(h(u))=\max(R',R'')$. $\square$
:::

Bỏ tính tất định thì (a) sai: nếu mỗi lần gọi $h$ trả một chuỗi ngẫu nhiên mới, một phần tử xuất hiện $10^6$ lần có $10^6$ cơ hội cho đuôi dài, và $R$ đo độ dài dòng thay cho $d$. Bỏ "cùng hàm $h$" ở (b) thì max của $R'$ và $R''$ không phải $R$ của dòng ghép.

<!-- note-topic-id: lec-09-topic-05 -->
### 2.3 Xác suất của một đuôi dài

Ví dụ 09.4 cho ba ước lượng 2, 8, 16 trên cùng $d=4$. Chúng ta tính xác suất để $2^R$ lệch khỏi $d$ quá một hệ số cho trước; MMDS (tr.143) chỉ trả lời định tính.

Một cách trực quan, mỗi phần tử phân biệt là một lần thử độc lập để có đuôi dài $\ell$, mỗi lần thành công với xác suất $2^{-\ell}$. Với $d$ lần thử, gần như chắc chắn có thành công khi $2^\ell$ nhỏ hơn nhiều $d$, và gần như chắc chắn không khi $2^\ell$ lớn hơn nhiều $d$. Định nghĩa 09.8 nói rõ "ngẫu nhiên" và "độc lập" nghĩa là gì.

::: definition Định nghĩa 09.8 (Mô hình băm lý tưởng)
Hàm $h:\mathcal U\to\{0,1\}^L$ được chọn ngẫu nhiên trước dòng. Dưới **mô hình băm lý tưởng**, với mọi tập $d$ phần tử phân biệt $u_1,\ldots,u_d$, các giá trị $h(u_1),\ldots,h(u_d)$ độc lập và mỗi giá trị đều trên $\{0,1\}^L$. Xác suất lấy theo phép chọn $h$; dòng được coi là cố định.
:::

Mô hình này là mô hình phi tiêu mà Bài 08 dùng cho Bloom filter (Bổ đề 08.26), với $2^L$ đích thay cho $n$ ngăn. Nó mạnh hơn tính tất định của hàm băm: tất định nói một phần tử luôn cho cùng giá trị, còn mô hình nói các phần tử khác nhau cho các giá trị độc lập.

::: lemma Bổ đề 09.9 (Xác suất một đuôi dài)
**Giả thiết.** $h(u)$ đều trên $\{0,1\}^L$; $\ell$ là số nguyên, $0\le\ell\le L$.

**Kết luận.** $\Pr[\rho(h(u))\ge\ell]=2^{-\ell}$.

**Điều kiện áp dụng.** Chỉ cần phân phối của một giá trị băm.

**Phạm vi.** Với $\ell>L$, xác suất bằng 0, vì $\rho\le L$.
:::

::: proof
Biến cố $\rho(h(u))\ge\ell$ xảy ra khi và chỉ khi $\ell$ bit cuối của $h(u)$ đều bằng 0; với $\ell=L$ điều này gồm cả chuỗi $0^L$, có $\rho=L$ theo quy ước. Có đúng $2^{L-\ell}$ chuỗi $L$ bit có $\ell$ bit cuối bằng 0, vì $L-\ell$ bit đầu tùy ý. Vì $h(u)$ đều trên $2^L$ chuỗi,

$$
\begin{aligned}
\Pr[\rho(h(u))\ge\ell]&=\frac{2^{L-\ell}}{2^L}\\
&=2^{-\ell}.\qquad\square
\end{aligned}
$$
:::

Bổ đề cho mỗi phần tử một xác suất. Định lý sau ghép $d$ phần tử: phía trên dùng cận hợp, phía dưới dùng tính độc lập cùng bất đẳng thức $1-z\le e^{-z}$. Ký hiệu $\lambda\ge2$ là hệ số sai lệch cho phép.

::: theorem Định lý 09.10 (Ngưỡng hai phía của $2^R$)
**Giả thiết.** Dòng có $d\ge1$ phần tử phân biệt $u_1,\ldots,u_d$, với $d\le2^L$. Hàm $h$ theo mô hình băm lý tưởng (Định nghĩa 09.8). Số thực $\lambda\ge2$.

**Kết luận.**

- (a) Với mọi số nguyên $0\le\ell\le L$: $\Pr[R\ge\ell]=1-(1-2^{-\ell})^d$.
- (b) $\Pr[2^R\ge\lambda d]\le1/\lambda$.
- (c) $\Pr[2^R\le d/\lambda]\le e^{-\lambda/2}$.

Do đó $\Pr[d/\lambda<2^R<\lambda d]\ge1-1/\lambda-e^{-\lambda/2}$.

**Điều kiện áp dụng.** Phần (b) chỉ cần mỗi giá trị băm đều; phần (a) và (c) cần thêm tính độc lập.

**Phạm vi.** Định lý nói về một hàm băm và về xác suất lệch quá hệ số $\lambda$; nó không chặn kỳ vọng của $2^R$ (Mệnh đề 09.11).
:::

::: proof
Theo Mệnh đề 09.7(a), $R=\max_{1\le i\le d}\rho(h(u_i))$, nên các phần tử lặp lại không thêm biến ngẫu nhiên nào.

**Bước 1 (phần (a), biến cố bù).** $R<\ell$ khi và chỉ khi mọi $u_i$ có $\rho(h(u_i))<\ell$. Các biến cố này độc lập vì các giá trị băm độc lập, và mỗi biến cố có xác suất $1-2^{-\ell}$ theo Bổ đề 09.9. Do đó $\Pr[R<\ell]=(1-2^{-\ell})^d$; lấy biến cố bù được (a).

**Bước 2 (cận trên cho một ngưỡng).** $R\ge\ell$ khi và chỉ khi có ít nhất một $i$ với $\rho(h(u_i))\ge\ell$. Theo cận hợp và Bổ đề 09.9,

$$
\begin{aligned}
&\Pr[R\ge\ell]\\
&\quad\le\sum_{i=1}^{d}\Pr[\rho(h(u_i))\ge\ell]\\
&\quad=d\,2^{-\ell}.
\end{aligned}
$$

Bước này không dùng tính độc lập.

**Bước 3 (phần (b)).** Đặt $\ell_1=\lceil\log_2(\lambda d)\rceil$. Vì $R$ nguyên, $2^R\ge\lambda d$ khi và chỉ khi $R\ge\log_2(\lambda d)$, khi và chỉ khi $R\ge\ell_1$. Nếu $\ell_1>L$ thì biến cố không xảy ra, vì $R\le L$. Nếu $\ell_1\le L$ thì

$$
\begin{aligned}
&\Pr[2^R\ge\lambda d]\\
&\quad=\Pr[R\ge\ell_1]\\
&\quad\le d\,2^{-\ell_1}\\
&\quad\le\frac{d}{\lambda d}=\frac1\lambda.
\end{aligned}
$$

Bất đẳng thức thứ nhất dùng Bước 2, bất đẳng thức thứ hai dùng $2^{\ell_1}\ge\lambda d$.

**Bước 4 (phần (c), trường hợp biên).** Nếu $d/\lambda<1$ thì $2^R\ge1>d/\lambda$, nên xác suất bằng $0\le e^{-\lambda/2}$.

**Bước 5 (phần (c), trường hợp $d/\lambda\ge1$).** Đặt $\ell_2=\lfloor\log_2(d/\lambda)\rfloor+1\ge1$. Vì $R$ nguyên, $2^R\le d/\lambda$ khi và chỉ khi $R\le\lfloor\log_2(d/\lambda)\rfloor$, tức $R<\ell_2$. Ta có $\ell_2\le\log_2(d/\lambda)+1\le\log_2d\le L$, vì $\lambda\ge2$ và $d\le2^L$; do đó (a) áp dụng được cho $\ell_2$. Hơn nữa $2^{\ell_2}=2\cdot2^{\lfloor\log_2(d/\lambda)\rfloor}\le2d/\lambda$, nên $d\,2^{-\ell_2}\ge\lambda/2$. Suy ra

$$
\begin{aligned}
&\Pr[2^R\le d/\lambda]\\
&\quad=\Pr[R<\ell_2]\\
&\quad=(1-2^{-\ell_2})^d\\
&\quad\le\bigl(e^{-2^{-\ell_2}}\bigr)^d\\
&\quad=e^{-d\,2^{-\ell_2}}\\
&\quad\le e^{-\lambda/2}.
\end{aligned}
$$

Đẳng thức thứ hai dùng Bước 1; bất đẳng thức thứ nhất dùng $1-z\le e^{-z}$ với hai vế không âm, bất đẳng thức thứ hai dùng $d\,2^{-\ell_2}\ge\lambda/2$.

**Bước 6 (gộp).** Biến cố $d/\lambda<2^R<\lambda d$ là phần bù của hợp hai biến cố ở (b) và (c); theo cận hợp, xác suất của hợp không vượt $1/\lambda+e^{-\lambda/2}$. $\square$
:::

Với một hàm băm lý tưởng, ước lượng vượt $\lambda$ lần giá trị thật với xác suất không quá $1/\lambda$, và thấp hơn $\lambda$ lần với xác suất không quá $e^{-\lambda/2}$; xác suất lệch xuống giảm theo hàm mũ của $\lambda$, xác suất lệch lên chỉ giảm như $1/\lambda$.

Hai kết luận định tính của MMDS (tr.143) là giới hạn của (a): khi $d\gg2^\ell$, $(1-2^{-\ell})^d\le e^{-d2^{-\ell}}$ gần 0, nên gần như chắc chắn thấy đuôi dài $\ell$; khi $d\ll2^\ell$, xác suất đó không quá $d2^{-\ell}$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "mỗi giá trị băm đều": nếu mọi hàm trong họ đều cho giá trị chẵn, chẳng hạn $h(x)=2x\bmod32$ trên mã số nguyên, thì $\rho(h(u))\ge1$ với mọi $u$. Với $d=1$, $\Pr[2^R\ge2d]=1$, trái với cận $1/2$ của (b) khi $\lambda=2$.
- Bỏ "độc lập": nếu mọi phần tử nhận cùng một giá trị băm, thì $\Pr[R\ge\ell]=2^{-\ell}$ không phụ thuộc $d$. Với $d=1\,024$, $\lambda=4$: $\Pr[2^R\le256]=\Pr[R\le8]=1-2^{-9}\approx0{,}998$, trong khi cận (c) là $e^{-2}\approx0{,}135$.
- Bỏ "$d\le2^L$": với $L=5$, $d=128$, $\lambda=2$, luôn có $2^R\le32<64=d/\lambda$, nên xác suất ở (c) bằng 1.

Bước 1 và Bước 5 dùng tính độc lập; Bước 2, 3 chỉ dùng tính đều qua Bổ đề 09.9; Bước 5 dùng $d\le2^L$ và $\lambda\ge2$ để Bổ đề 09.9 áp dụng được.

::: example Ví dụ 09.5 (Đọc Định lý 09.10 với $d=1\,000$, $\lambda=4$)
**Dữ kiện.** $d=1\,000$ phần tử phân biệt, giá trị băm $L=64$ bit; MMDS (tr.143) nêu 64 bit là đủ để băm URL. Hệ số $\lambda=4$.

**Cận của định lý.** $\Pr[2^R\ge4\,000]\le1/4=0{,}25$ và $\Pr[2^R\le250]\le e^{-2}\approx0{,}135$; do đó $\Pr[250<2^R<4\,000]\ge0{,}615$.

**Giá trị chính xác theo (a).** $\ell_1=\lceil\log_2 4\,000\rceil=12$, nên $\Pr[2^R\ge4\,000]=\Pr[R\ge12]=1-(1-2^{-12})^{1\,000}\approx0{,}217$. $\ell_2=\lfloor\log_2250\rfloor+1=8$, nên $\Pr[2^R\le250]=(1-2^{-8})^{1\,000}\approx0{,}020$. Xác suất nằm giữa là $1-0{,}217-0{,}020\approx0{,}763$.

**Diễn giải.** Ước lượng rơi vào một trong bốn giá trị 256, 512, 1 024, 2 048 với xác suất khoảng $76\%$; cận của định lý thấp hơn nhưng cùng bậc.

**Kiểm tra lại.** $0{,}217\le0{,}25$ và $0{,}020\le0{,}135$.
:::

![Đồ thị cột của Pr[R ≥ ℓ] theo ngưỡng độ dài đuôi ℓ từ 0 đến 20, với d bằng 1000: bằng 1 tới ℓ bằng 6; 0,98 tại 8; 0,86 tại 9; 0,62 tại 10; 0,39 tại 11; 0,22 tại 12; 0,11 tại 13; gần 0 từ 16. Đường đứng nét đứt tại log2 d xấp xỉ 9,97. Vùng tô nhạt bên trái, ℓ nhỏ hơn hoặc bằng 7, có nhãn xác suất gần 1; vùng bên phải, ℓ lớn hơn hoặc bằng 12, có nhãn xác suất nhỏ.](img/lec-09/fm-nguong-hai-phia.svg)

Hình vẽ công thức (a) với $d=1\,000$. Cột giảm từ gần 1 xuống gần 0 trong một khoảng hẹp quanh $\ell=\log_2d\approx9{,}97$, nên $R$ tập trung quanh $\log_2d$ và $2^R$ cho cỡ của $d$. Khoảng chuyển tiếp rộng chừng bốn giá trị $\ell$, nên một hàm băm chỉ cho cỡ chứ không cho giá trị chính xác.

Như vậy, với một hàm băm lý tưởng, $2^R$ nằm trong khoảng $(d/\lambda,\lambda d)$ với xác suất ít nhất $1-1/\lambda-e^{-\lambda/2}$ (Định lý 09.10). Hệ số $\lambda=4$ chỉ cho xác suất khoảng $0{,}6$ đến $0{,}76$, quá thấp để dùng. Cách hiển nhiên để làm tốt hơn là chạy nhiều hàm băm và gộp các ước lượng, nhưng cách gộp phải chọn theo phân phối của $2^R$.

<!-- note-topic-id: lec-09-topic-06 -->
### 2.4 Phân phối đuôi nặng và gộp nhiều hàm băm

Chạy sáu hàm băm trên dòng mười lăm phần tử cho sáu ước lượng $4,4,2,8,16,4$ (bảng đủ ở Ví dụ 09.6). Trung bình của chúng là $38/6\approx6{,}33$, lớn hơn $d=4$ gần $60\%$, và phần lớn độ lệch đến từ một giá trị 16. Theo MMDS (§4.4.3, tr.144), một giá trị quá lớn hiếm khi xảy ra nhưng kéo trung bình đi rất xa; mệnh đề sau lượng hóa điều đó.

::: proposition Mệnh đề 09.11 (Kỳ vọng của $2^R$ quá lớn)
**Giả thiết.** Mô hình băm lý tưởng như Định lý 09.10: $d\ge1$ phần tử phân biệt, $d\le2^L$, các giá trị băm độc lập và đều trên $\{0,1\}^L$.

**Kết luận.**

- (a) Khi $d=1$: $\mathbb E[2^R]=L/2+1$.
- (b) Với mọi $d$: đặt $\ell_0=\max(1,\lceil\log_2d\rceil)$, khi đó
$$
\mathbb E[2^R]\ge1+\tfrac d4(L-\ell_0+1)\!.
$$

**Điều kiện áp dụng.** Như Định lý 09.10.

**Phạm vi.** Với $d$ cố định, $\mathbb E[2^R]$ tăng không giới hạn khi $L$ tăng, trong khi Định lý 09.10 cho thấy $2^R$ thường nằm gần $d$.
:::

::: proof
**Bước 1 (phân phối của một độ dài đuôi).** Theo Bổ đề 09.9, với $0\le\ell<L$,
$$
\begin{aligned}
&\Pr[\rho=\ell]\\
&\quad=\Pr[\rho\ge\ell]-\Pr[\rho\ge\ell+1]\\
&\quad=2^{-\ell}-2^{-(\ell+1)}=2^{-(\ell+1)},
\end{aligned}
$$
và $\Pr[\rho=L]=2^{-L}$, trong đó $\rho=\rho(h(u))$ của một phần tử.

**Bước 2 (phần (a)).** Với $d=1$, $R=\rho$. Theo Bước 1 và định nghĩa kỳ vọng,

$$
\begin{aligned}
&\mathbb E[2^R]\\
&\quad=\sum_{\ell=0}^{L-1}2^\ell\cdot2^{-(\ell+1)}+2^L\cdot2^{-L}\\
&\quad=\sum_{\ell=0}^{L-1}\frac12+1=\frac L2+1.
\end{aligned}
$$

**Bước 3 (viết $2^R$ thành tổng chỉ báo).** Vì $1+\sum_{\ell=1}^{R}2^{\ell-1}=1+(2^R-1)=2^R$ (tổng cấp số nhân) và $R\le L$,
$$
2^R=1+\sum_{\ell=1}^{L}2^{\ell-1}\,\mathbf 1[R\ge\ell],
$$
nên theo tuyến tính kỳ vọng và $\mathbb E[\mathbf 1[E]]=\Pr(E)$,
$$
\mathbb E[2^R]=1+\sum_{\ell=1}^{L}2^{\ell-1}\Pr[R\ge\ell].
$$

**Bước 4 (một bất đẳng thức một biến).** Với $0\le\upsilon\le1$, $1-e^{-\upsilon}\ge\upsilon/2$. Thật vậy, hàm $\Psi(\upsilon)=1-\upsilon+\upsilon^2/2-e^{-\upsilon}$ có $\Psi(0)=0$ và $\Psi'(\upsilon)=-1+\upsilon+e^{-\upsilon}\ge0$ vì $e^{-\upsilon}\ge1-\upsilon$. Do đó $\Psi\ge0$ trên $[0,\infty)$, tức $1-e^{-\upsilon}\ge\upsilon-\upsilon^2/2$, và với $\upsilon\le1$, $\upsilon-\upsilon^2/2\ge\upsilon/2$.

**Bước 5 (chặn từng số hạng).** Xét $\ell$ với $\ell_0\le\ell\le L$ và đặt $\upsilon=d\,2^{-\ell}$. Vì $2^\ell\ge2^{\lceil\log_2d\rceil}\ge d$, ta có $\upsilon\le1$. Khi đó

$$
\begin{aligned}
&\Pr[R\ge\ell]\\
&\quad=1-(1-2^{-\ell})^d\\
&\quad\ge1-e^{-d2^{-\ell}}=1-e^{-\upsilon}\\
&\quad\ge\upsilon/2=d\,2^{-\ell-1},
\end{aligned}
$$

theo Định lý 09.10(a), bất đẳng thức $1-z\le e^{-z}$ và Bước 4. Do đó số hạng thứ $\ell$ của Bước 3 không nhỏ hơn $2^{\ell-1}\cdot d\,2^{-\ell-1}=d/4$.

**Bước 6 (cộng lại).** Các số hạng với $\ell<\ell_0$ không âm. Có $L-\ell_0+1$ giá trị $\ell$ trong $[\ell_0,L]$, mỗi giá trị góp ít nhất $d/4$, nên $\mathbb E[2^R]\ge1+\frac d4(L-\ell_0+1)$. $\square$
:::

Với $d=1$ và $L=64$, kỳ vọng của ước lượng là $L/2+1=33$ dù chỉ có một phần tử; cận (b) với $\ell_0=1$ chỉ cho $1+64/4=17$. Với $d=10^6$ và $L=64$, $\ell_0=20$, nên $\mathbb E[2^R]>1{,}1\cdot10^7$, tức ít nhất khoảng $11d$; tính trực tiếp theo Bước 3 cho khoảng $22{,}6d$.

Mỗi số hạng của Bước 3 góp ít nhất $d/4$ bất kể $\ell$: xác suất có đuôi dài thêm 1 giảm một nửa, nhưng $2^R$ tăng gấp đôi (MMDS tr.144, chú thích 3). Do đó trung bình của nhiều ước lượng $2^{R_j}$ hội tụ về $\mathbb E[2^R]$, lớn hơn $d$ nhiều khi $L$ lớn hơn nhiều $\log_2d$, chứ không về $d$.

Một lựa chọn khác là lấy trung vị, vốn không bị một giá trị cực lớn kéo đi. Nhận xét sau chỉ ra giới hạn của nó.

::: remark Nhận xét 09.12 (Trung vị của các lũy thừa của 2)
Trung vị của một số lẻ giá trị là một trong các giá trị đó. Mọi ước lượng $2^{R_j}$ là lũy thừa của 2, nên trung vị của chúng cũng là lũy thừa của 2. Khi $d=400$ (MMDS tr.144), hai lũy thừa của 2 gần nhất là 256 và 512, nên trung vị sai ít nhất $\min(400-256,\,512-400)=112$, tức sai số tương đối ít nhất $112/400=28\%$, dù dùng bao nhiêu hàm băm.
:::

Trung bình cho được mọi giá trị nhưng bị phân phối đuôi nặng (heavy-tailed distribution) kéo lệch; trung vị không bị kéo lệch nhưng chỉ cho lũy thừa của 2. Về mặt ý tưởng, nếu lấy trung bình trong từng nhóm nhỏ, một giá trị quá lớn chỉ làm hỏng nhóm chứa nó, và trung vị của các nhóm bỏ qua nhóm đó. Ví dụ 09.6 kết hợp hai phép theo thứ tự của MMDS (tr.144).

::: example Ví dụ 09.6 (Gộp sáu ước lượng)
**Dữ kiện.** Dòng mười lăm phần tử của Ví dụ 09.3, $d=4$. Sáu hàm băm 5 bit; hàng $h_1$ đã có ở Ví dụ 09.3, ba hàng $h_3$, $h_4$, $h_5$ ở Ví dụ 09.4.

| Hàm | $\mathrm a$ | $\mathrm b$ | $\mathrm c$ | $\mathrm d$ | độ dài đuôi | $Y_j=2^{R_j}$ |
|---|---|---|---|---|---|---:|
| $h_1$ | $10110$ | $01011$ | $11100$ | $00111$ | $1,0,2,0$ | 4 |
| $h_2$ | $01101$ | $10100$ | $00111$ | $11010$ | $0,2,0,1$ | 4 |
| $h_3$ | $11001$ | $00110$ | $01011$ | $10101$ | $0,1,0,0$ | 2 |
| $h_4$ | $00011$ | $11000$ | $10101$ | $01110$ | $0,3,0,1$ | 8 |
| $h_5$ | $10001$ | $01010$ | $10000$ | $01111$ | $0,1,4,0$ | 16 |
| $h_6$ | $01001$ | $10111$ | $11010$ | $01100$ | $0,0,1,2$ | 4 |

**Tính.** Với $g=3$ nhóm cỡ 2, các nhóm là $(4,4)$, $(2,8)$, $(16,4)$, có trung bình $\bar Y_1=4$, $\bar Y_2=5$, $\bar Y_3=10$. Trung vị là $\widehat d=5$. Trung bình thuần của sáu số là $38/6\approx6{,}33$.

**Diễn giải.** Giá trị 16 chỉ làm lệch nhóm thứ ba, và phép trung vị bỏ qua nhóm đó; kết quả 5 không phải lũy thừa của 2.

**Kiểm tra lại.** $4+4+2+8+16+4=38$; ba trung bình nhóm sắp tăng là $4,5,10$.
:::

::: algorithm Thuật toán 09.13 (Gộp: trung bình trong nhóm, rồi trung vị)
**Đầu vào.** Dòng $x_1,x_2,\ldots$; $q$ hàm băm $h_1,\ldots,h_q:\mathcal U\to\{0,1\}^L$ chọn độc lập trước dòng; số nhóm $g$ lẻ, chia hết $q$.

**Đầu ra.** Ước lượng $\widehat d$ của $d$.

**Giả thiết.** Như Thuật toán 09.6 cho từng hàm băm.

1. Chạy Thuật toán 09.6 song song cho $h_1,\ldots,h_q$, giữ $R_1,\ldots,R_q$.
2. Khi có truy vấn, đặt $Y_j=2^{R_j}$ với $j=1,\ldots,q$.
3. Chia $Y_1,\ldots,Y_q$ thành $g$ nhóm liên tiếp, mỗi nhóm $q/g$ giá trị; ký hiệu $\bar Y_\gamma$ là trung bình của nhóm $\gamma$, $\gamma=1,\ldots,g$.
4. Trả $\widehat d$ là trung vị của $\bar Y_1,\ldots,\bar Y_g$.

**Dừng.** Như Thuật toán 09.6; phép trả lời dừng sau bước 4.

**Trường hợp biên.** Dòng rỗng trả 0. Với $g=q$ (mỗi nhóm một giá trị), thuật toán trả trung vị thuần; với $g=1$, nó trả trung bình thuần.

**Chi phí.** Mô hình: mỗi phép băm, đếm bit 0 cuối, so sánh, cộng tốn $O(1)$; trường hợp xấu nhất.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| băm và cập nhật $R_j$ (bước 1) | $q$ mỗi phần tử | $O(1)$ | $O(q)$ mỗi phần tử |
| tính $Y_j$ và trung bình nhóm (bước 2–3) | $q$ mỗi truy vấn | $O(1)$ | $O(q)$ mỗi truy vấn |
| trung vị của $g$ số (bước 4) | 1 mỗi truy vấn | $O(g\log g)$ | $O(g\log g)$ |

MMDS (tr.144) khuyên cỡ nhóm $q/g$ ít nhất là một bội nhỏ của $\log_2d$, với $d$ thay bằng một cận trên dự kiến.
:::

Ví dụ 09.6 là một lượt chạy với $q=6$, $g=3$. Trung bình trong nhóm đủ lớn nhận được gần như mọi giá trị, khắc phục Nhận xét 09.12; trung vị ở bước cuối loại các nhóm bị kéo lệch, khắc phục Mệnh đề 09.11 (MMDS tr.144).

Bổ đề sau lượng hóa phần thứ hai bằng một phép đếm; UMass (bài 8, trang chiếu 3–5) chứng minh cùng nguyên lý, mẹo trung vị (median trick), bằng cận Chernoff. Ký hiệu $\eta$ là cận xác suất thất bại của một đại lượng.

::: lemma Bổ đề 09.14 (Mẹo trung vị)
**Giả thiết.** $g$ là số nguyên dương lẻ. $\bar Y_1,\ldots,\bar Y_g$ là các biến ngẫu nhiên độc lập. $G$ là một khoảng của trục số, và $\Pr[\bar Y_\gamma\notin G]\le\eta$ với mọi $\gamma$, trong đó $0\le\eta\le1$.

**Kết luận.** Gọi $M$ là trung vị của $\bar Y_1,\ldots,\bar Y_g$. Khi đó $\Pr[M\notin G]\le(4\eta)^{g/2}$.

**Điều kiện áp dụng.** Kết luận có ích khi $\eta<1/4$; khi đó cận giảm theo hàm mũ của $g$.

**Phạm vi.** Bổ đề không cần các $\bar Y_\gamma$ cùng phân phối, chỉ cần độc lập và cùng cận $\eta$.
:::

::: proof
Đặt $g_0=(g+1)/2$ và gọi $E_\gamma$ là biến cố $\bar Y_\gamma\notin G$.

**Bước 1 (trung vị ra ngoài kéo theo nhiều giá trị ra ngoài).** Sắp các giá trị tăng dần; $M$ đứng ở vị trí $g_0$. Nếu $M$ nằm bên trái khoảng $G$, thì $M$ cùng $g_0-1$ giá trị đứng trước nó đều nhỏ hơn hoặc bằng $M$, nên đều nằm bên trái $G$; đó là $g_0$ giá trị ngoài $G$. Nếu $M$ nằm bên phải $G$, lập luận đối xứng với $M$ và $g_0-1$ giá trị đứng sau nó. Vì $G$ là một khoảng, một điểm ngoài $G$ nằm bên trái hoặc bên phải $G$. Vậy biến cố $M\notin G$ kéo theo: có ít nhất $g_0$ chỉ số $\gamma$ để $E_\gamma$ xảy ra.

**Bước 2 (phủ bằng các tập con).** Nếu ít nhất $g_0$ biến cố $E_\gamma$ xảy ra, thì mọi biến cố trong một tập chỉ số $\Gamma$ nào đó có đúng $g_0$ phần tử cùng xảy ra. Do đó
$$
\{M\notin G\}\subseteq\bigcup_{\lvert\Gamma\rvert=g_0}\ \bigcap_{\gamma\in\Gamma}E_\gamma .
$$

**Bước 3 (cận hợp và độc lập).**

$$
\begin{aligned}
&\Pr[M\notin G]\\
&\quad\le\sum_{\lvert\Gamma\rvert=g_0}\Pr\Bigl[\bigcap_{\gamma\in\Gamma}E_\gamma\Bigr]\\
&\quad=\sum_{\lvert\Gamma\rvert=g_0}\prod_{\gamma\in\Gamma}\Pr[E_\gamma]\\
&\quad\le\binom{g}{g_0}\eta^{g_0}.
\end{aligned}
$$

Ba quan hệ lần lượt dùng cận hợp, tính độc lập của các $\bar Y_\gamma$ và $\Pr[E_\gamma]\le\eta$.

**Bước 4 (rút gọn).** $\binom{g}{g_0}\le\sum_{i=0}^{g}\binom gi=2^g$, và vì $0\le\eta\le1$, $g_0\ge g/2$, ta có $\eta^{g_0}\le\eta^{g/2}$. Do đó $\Pr[M\notin G]\le2^g\eta^{g/2}=(4\eta)^{g/2}$. $\square$
:::

Áp bổ đề cho chính các ước lượng $Y_j$, tức nhóm cỡ 1, ta được một bảo đảm cho trung vị thuần.

::: corollary Hệ quả 09.15 (Trung vị của các ước lượng độc lập)
**Giả thiết.** $q$ lẻ; $q$ hàm băm được chọn độc lập, mỗi hàm thỏa giả thiết của Định lý 09.10 với cùng $d$; $\lambda\ge8$.

**Kết luận.** Trung vị $M$ của $Y_1,\ldots,Y_q$ (tức $g=q$ nhóm cỡ 1) thỏa
$$
\begin{aligned}
\Pr\bigl[M\notin(d/\lambda,\lambda d)\bigr]&\le(4\eta)^{q/2},\\
\eta=\frac1\lambda+e^{-\lambda/2}&\le0{,}144 .
\end{aligned}
$$

**Điều kiện áp dụng.** Các hàm băm độc lập với nhau.

**Phạm vi.** Hệ quả chỉ nói về sai số theo hệ số $\lambda$; nó không khắc phục Nhận xét 09.12.
:::

::: proof
**Bước 1 (độc lập).** Các hàm băm được chọn độc lập, nên $Y_1,\ldots,Y_q$ độc lập.

**Bước 2 (cận $\eta$).** Theo Định lý 09.10, mỗi $Y_j$ nằm ngoài khoảng $G=(d/\lambda,\lambda d)$ với xác suất không quá $\eta=1/\lambda+e^{-\lambda/2}$. Hàm này giảm theo $\lambda$, nên với $\lambda\ge8$, $\eta\le1/8+e^{-4}\approx0{,}1433<1/4$.

**Bước 3 (áp bổ đề).** Bổ đề 09.14 với $g=q$ và khoảng $G$ cho kết luận. $\square$
:::

Mọi $\lambda\ge6$ đã cho $\eta<1/4$, vì $1/6+e^{-3}\approx0{,}216$. Với $\lambda=8$, $4\eta\approx0{,}573$, nên với $q=21$ hàm băm, xác suất trung vị lệch quá 8 lần không quá $0{,}573^{10{,}5}\approx0{,}0029$. Các trung bình nhóm của Thuật toán 09.13 cũng độc lập, nhưng cận $\eta$ cho một trung bình nhóm đòi phân tích phân phối của trung bình, mà MMDS (tr.144) chỉ lập luận định tính.

Các giả thiết của Bổ đề 09.14 có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "độc lập": nếu cả $g$ hàm băm là cùng một hàm, mọi $Y_j$ bằng nhau, nên $\Pr[M\notin G]=\Pr[Y_1\notin G]$, không giảm theo $g$.
- Bỏ "$G$ là khoảng": lấy $g=3$, $G=(-\infty,1)\cup(3,\infty)$, $\bar Y_1=0$ và $\bar Y_3=4$ chắc chắn, $\bar Y_2=2$ với xác suất $\eta$ và bằng 0 với xác suất $1-\eta$. Mỗi $\Pr[\bar Y_\gamma\notin G]\le\eta$, nhưng trung vị bằng $2\notin G$ đúng khi $\bar Y_2=2$, nên $\Pr[M\notin G]=\eta$, lớn hơn $(4\eta)^{3/2}=8\eta^{3/2}$ khi $\eta<1/64$.

Ngưỡng $\eta<1/4$ là giá của phép chặn $\binom g{g_0}\le2^g$ ở Bước 4; khi $\eta\ge1/4$, cận $(4\eta)^{g/2}\ge1$ chỉ không cho thông tin.

Để xác suất thất bại của trung vị giảm theo $g$, cần $\eta<1/2$: nếu mỗi $\bar Y_\gamma$ nằm bên phải $G$ với xác suất đúng $1/2$, độc lập, thì trung vị nằm bên phải $G$ khi và chỉ khi ít nhất $g_0=(g+1)/2$ giá trị nằm bên phải, và do phân phối nhị thức với xác suất $1/2$ đối xứng, xác suất này bằng $1/2$ với mọi $g$ lẻ.

Bước 1 dùng tính chất khoảng của $G$; Bước 3 dùng tính độc lập.

<!-- note-topic-id: lec-09-topic-07 -->
### 2.5 Chi phí, nhầm lẫn và thực hành

::: proposition Mệnh đề 09.16 (Chi phí của Flajolet–Martin)
**Giả thiết.** Thuật toán 09.13 với $q$ hàm băm, $g$ nhóm, giá trị băm $L$ bit; tính một giá trị băm và độ dài đuôi của nó tốn $O(1)$ phép trên từ máy.

**Kết luận.** Bộ nhớ cho trạng thái là $q\lceil\log_2(L+1)\rceil+1$ bit (một cờ chung cho dòng rỗng), cộng phần lưu $q$ hàm băm. Mỗi phần tử tốn $O(q)$ phép; mỗi truy vấn tốn $O(q+g\log g)$ phép.

**Điều kiện áp dụng.** Không cần giả thiết xác suất.

**Phạm vi.** Bộ nhớ không phụ thuộc độ dài dòng hay $d$, trừ việc chọn $L$ đủ lớn để $d\le2^L$.
:::

::: proof
**Bước 1 (bộ nhớ).** Mỗi $R_j$ nhận giá trị trong $\{0,\ldots,L\}$, nên cần $\lceil\log_2(L+1)\rceil$ bit theo số bit của bộ đếm ở phần tiên quyết; trạng thái "chưa đọc phần tử nào" chung cho mọi $j$ nên chỉ cần một bit cờ.

**Bước 2 (mỗi phần tử).** Mỗi phần tử gọi bước 2 của Thuật toán 09.6 cho $q$ hàm, mỗi lần $O(1)$ phép.

**Bước 3 (truy vấn).** Truy vấn tính $q$ lũy thừa và $q$ phép cộng cho $g$ trung bình, rồi sắp $g$ số để lấy trung vị. $\square$
:::

Với $L=64$, mỗi $R_j$ cần 7 bit. Nếu $d$ khoảng $10^6$, $\log_2d\approx20$; $g=21$ nhóm cỡ 20 cho $q=420$ hàm băm và $2\,941$ bit, khoảng 368 byte cho một dòng, so với 512 MiB của vector bit (Nhận xét 09.3).

::: remark Nhận xét 09.17 (Trong thực hành)
Mỗi trang có một bộ $q$ số nguyên nhỏ $R_j$; theo MMDS (§4.4.4, tr.144–145), giới hạn thực tế là thời gian tính $q$ giá trị băm mỗi phần tử.

Mô hình băm lý tưởng là giả thiết phân tích: một hàm thực sự ngẫu nhiên trên địa chỉ IPv4 với $L=64$ cần $\lvert\mathcal U\rvert L$ bit, tức 32 GiB, nên phép so 368 byte với 512 MiB giả thiết các hàm băm có mô tả ngắn, và họ $\alpha x+\beta\bmod2^L$ có thể vi phạm nặng (Bài tập 09.11, 09.17).

Khi dòng phân tán trên nhiều máy dùng cùng các hàm $h_j$, Mệnh đề 09.7(b) cho phép ghép các phác thảo bằng phép lấy max từng $R_j$, tính chất mà UMass (bài 8, trang chiếu 8) gọi là phác thảo hợp nhất được (mergeable sketch).
:::

::: remark Nhận xét 09.18 (Nhầm lẫn thường gặp)
- $2^R$ không phải ước lượng không chệch của $d$ (Mệnh đề 09.11).
- $d$ là số phần tử phân biệt, không phải độ dài dòng: theo Mệnh đề 09.7, phần tử lặp lại không đổi $R$.
- Đảo thứ tự gộp (trung vị trong nhóm rồi trung bình) làm mất bảo đảm của Bổ đề 09.14, vốn cần bước cuối là trung vị.
:::

::: exercise Bài tập 09.2 (Phần tử lặp và ngưỡng hai phía)
- (a) Trên một dòng, phần tử $u$ xuất hiện $10^6$ lần. Vì sao $u$ chỉ góp một giá trị vào $R$ của Thuật toán 09.6?
- (b) Dưới giả thiết của Định lý 09.10 với $d=2\,000$, $L=64$, $\lambda=8$, cho cận trên của $\Pr[2^R\ge16\,000]$ và $\Pr[2^R\le250]$, rồi tính giá trị chính xác của hai xác suất theo Định lý 09.10(a).
:::

::: hint
(a) Dùng Mệnh đề 09.7. (b) Đổi mỗi biến cố về $R\ge\ell_1$ và $R<\ell_2$ như Bước 3 và Bước 5 của chứng minh Định lý 09.10.
:::

::: solution
(a) Hàm $h$ tất định, nên mọi lần xuất hiện của $u$ cho cùng $\rho(h(u))$; theo Mệnh đề 09.7(a), $R$ là max trên tập phần tử phân biệt, trong đó $u$ có mặt một lần.

(b) Cận của định lý: $\Pr[2^R\ge16\,000]\le1/8=0{,}125$ và $\Pr[2^R\le250]\le e^{-4}\approx0{,}018$. Giá trị chính xác: $\ell_1=\lceil\log_216\,000\rceil=14$, vì $2^{13}=8\,192<16\,000\le16\,384=2^{14}$, nên $\Pr[R\ge14]=1-(1-2^{-14})^{2\,000}\approx0{,}115$. $\ell_2=\lfloor\log_2250\rfloor+1=8$, nên $\Pr[R<8]=(1-2^{-8})^{2\,000}\approx0{,}0004$.

**Kiểm tra lại.** $0{,}115\le0{,}125$ và $0{,}0004\le0{,}018$.
:::

::: exercise Bài tập 09.3 (Gộp ước lượng và mẹo trung vị)
Chín ước lượng $2,4,4,8,4,64,4,2,8$ được tính trên dòng có $d=4$.

- (a) Tính ước lượng gộp của Thuật toán 09.13 với $g=1$, $g=3$ và $g=9$. Vì sao không dùng $g=2$?
- (b) Với $\lambda=8$, dùng Hệ quả 09.15 chặn xác suất trung vị của $q=11$ ước lượng độc lập lệch quá 8 lần. Số lẻ $q$ nhỏ nhất nào làm cận này không vượt $10^{-3}$?
- (c) Với $d=400$, vì sao trung vị của 25 ước lượng sai ít nhất $28\%$, và bước nào của Thuật toán 09.13 khắc phục điều đó?
:::

::: hint
(a) Thuật toán cần $g$ lẻ. (b) Giải $0{,}5733^{q/2}\le10^{-3}$. (c) Nhận xét 09.12.
:::

::: solution
(a) Với $g=1$: trung bình $100/9\approx11{,}1$. Với $g=3$: các nhóm $(2,4,4)$, $(8,4,64)$, $(4,2,8)$ có trung bình $10/3$, $76/3$, $14/3$, trung vị $14/3\approx4{,}67$. Với $g=9$: trung vị thuần 4. Với $g=2$: thuật toán đòi $g$ lẻ và chia hết $q=9$; hơn nữa trung vị của hai số không phải một giá trị duy nhất.

(b) $4\eta\le0{,}5733$, nên với $q=11$ cận là $0{,}5733^{5{,}5}\approx0{,}047$. Điều kiện $0{,}5733^{q/2}\le10^{-3}$ tương đương $q\ge2\ln(10^{-3})/\ln0{,}5733\approx24{,}8$, nên $q=25$.

(c) Trung vị của các lũy thừa của 2 là một lũy thừa của 2 (Nhận xét 09.12); bước trung bình trong nhóm cho các giá trị khác.

**Kiểm tra lại.** $0{,}5733^{12{,}5}\approx9{,}5\cdot10^{-4}\le10^{-3}<0{,}5733^{11{,}5}\approx1{,}7\cdot10^{-3}$.
:::

Như vậy, chúng ta đã có một ước lượng cho $F_0$ chỉ cần một số nhỏ cho mỗi hàm băm (Thuật toán 09.6), với cận xác suất hai phía (Định lý 09.10); vì kỳ vọng quá lớn (Mệnh đề 09.11) và trung vị chỉ cho lũy thừa của 2 (Nhận xét 09.12), các ước lượng được gộp bằng trung bình trong nhóm rồi trung vị (Thuật toán 09.13), với bước trung vị có bảo đảm giảm theo hàm mũ (Bổ đề 09.14). Tuy nhiên, $F_0$ không cho biết phân bố tần suất lệch đến đâu. Trong Mục 3, chúng ta ước lượng $F_2$ và dùng lại đúng phép gộp này.

## 3. Mômen bậc hai và ước lượng AMS

Hai dòng của Ví dụ 09.2 có cùng độ dài 100 và cùng 11 phần tử phân biệt, nhưng số bất ngờ là 910 và $8\,110$. Lời giải chính xác cho $F_2$ giữ $d$ bộ đếm (Nhận xét 09.3), với địa chỉ IPv4 là tới $2^{32}$ bộ đếm. Chúng ta ước lượng $F_2$ bằng thuật toán Alon–Matias–Szegedy (AMS, MMDS §4.5.2–4.5.5): giữ $s$ biến, mỗi biến một cặp (phần tử, bộ đếm), với trung bình có kỳ vọng đúng bằng $F_2$.

<!-- note-topic-id: lec-09-topic-08 -->
### 3.1 Biến AMS

Một cách trực quan, chọn một vị trí ngẫu nhiên của dòng, rồi đếm số lần phần tử ở vị trí đó xuất hiện từ vị trí đó trở về sau. Phần tử xuất hiện nhiều vừa dễ được chọn, vừa có bộ đếm lớn, nên một hàm tăng của bộ đếm phản ánh $\sum_uf_u^2$ chứ không chỉ $\sum_uf_u$. Ví dụ 09.7, theo MMDS, chạy nó trên dòng mười lăm phần tử.

::: example Ví dụ 09.7 (Ba biến trên dòng mười lăm phần tử)
**Dữ kiện.** Dòng $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$, độ dài $r=15$, có $F_2=59$ (Ví dụ 09.1). Ba biến được chọn ở vị trí 3, 8, 13 (MMDS Ví dụ 4.7, tr.146–147).

**Vết chạy.** Mỗi biến ghi phần tử ở vị trí của nó và một bộ đếm, rồi tăng bộ đếm mỗi khi phần tử đó xuất hiện lại.

| Vị trí | Phần tử | Biến 1 | Biến 2 | Biến 3 |
|---:|---|---|---|---|
| 3 | $\mathrm c$ | $(\mathrm c,1)$ | — | — |
| 7 | $\mathrm c$ | $(\mathrm c,2)$ | — | — |
| 8 | $\mathrm d$ | $(\mathrm c,2)$ | $(\mathrm d,1)$ | — |
| 11 | $\mathrm d$ | $(\mathrm c,2)$ | $(\mathrm d,2)$ | — |
| 12 | $\mathrm c$ | $(\mathrm c,3)$ | $(\mathrm d,2)$ | — |
| 13 | $\mathrm a$ | $(\mathrm c,3)$ | $(\mathrm d,2)$ | $(\mathrm a,1)$ |
| 14 | $\mathrm a$ | $(\mathrm c,3)$ | $(\mathrm d,2)$ | $(\mathrm a,2)$ |

Các vị trí không ghi trong bảng không đổi biến nào; vị trí 15 mang $\mathrm b$, không có biến nào giữ $\mathrm b$.

**Ước lượng.** Từ bộ đếm $v$, mỗi biến cho ước lượng $r(2v-1)$ (MMDS Ví dụ 4.8, tr.147): biến 1 cho $15\cdot(2\cdot3-1)=75$, biến 2 và biến 3 cho $15\cdot3=45$. Trung bình ba ước lượng là $(75+45+45)/3=55$.

**Kiểm tra lại.** $\mathrm c$ ở các vị trí 3, 7, 12; $\mathrm d$ ở 8, 11; $\mathrm a$ ở 13, 14 trong đoạn từ vị trí 13; khớp ba bộ đếm 3, 2, 2.
:::

![Mười lăm ô vị trí 1 đến 15 chứa dòng a b c b d a c d a b d c a a b; ba ô 3, 8 và 13 được tô đậm. Từ mỗi ô được chọn, một mũi tên sang phải đánh dấu các lần xuất hiện về sau: c ở 3, 7, 12, v3 bằng 3, ước lượng 15 nhân 5 bằng 75; d ở 8, 11, v8 bằng 2, ước lượng 45; a ở 13, 14, v13 bằng 2, ước lượng 45. Dòng cuối: trung bình 55, giá trị thật F2 bằng 59.](img/lec-09/ams-ba-bien.svg)

Hình vẽ lại vết chạy trên trục vị trí. Mỗi mũi tên chỉ đếm các lần xuất hiện từ vị trí được chọn về sau: $\mathrm a$ ở vị trí 1, 6, 9 không được biến 3 đếm. Bộ đếm vì thế không phải tần suất, và định nghĩa sau gọi tên đại lượng nó đo.

::: definition Định nghĩa 09.19 (Số lần xuất hiện ở hậu tố và biến AMS)
Cho dòng $x_1,\ldots,x_r$ với $r\ge1$ đã biết.

- Với mỗi vị trí $i\in\{1,\ldots,r\}$, **số lần xuất hiện ở hậu tố** của $x_i$ là
$$
v_i=\bigl\lvert\{i'\ge i: x_{i'}=x_i\}\bigr\rvert .
$$
- Một **biến AMS** chọn vị trí $I$ đều trên $\{1,\ldots,r\}$, giữ cặp $(x_I,v_I)$ và cho ước lượng
$$
X=r\,(2v_I-1).
$$
:::

Số $v_i$ đếm cả chính vị trí $i$, nên $v_i\ge1$; lần xuất hiện cuối của một phần tử có $v_i=1$, lần đầu có $v_i=f_{x_i}$. Ví dụ, vị trí 6 mang $\mathrm a$ và $\mathrm a$ xuất hiện ở 6, 9, 13, 14 từ đó về sau, nên $v_6=4$ (MMDS Ví dụ 4.9, tr.147), dù $f_{\mathrm a}=5$.

Ví dụ 09.7 là ba biến AMS với $I=3,8,13$ và $v_I=3,2,2$;

Vị trí $I$ chọn đều trên mọi vị trí, giống hồ chứa cỡ 1 của Bài 08 (trường hợp $s=1$ của Định lý 08.17), nên phần tử $u$ được chọn với xác suất $f_u/r$.

Thay $v_I$ bằng $f_{x_I}$ thì ước lượng bị chệch: trên dòng mười lăm phần tử, kỳ vọng thành 103 thay cho 59. Thuật toán sau giữ $s$ biến khi biết trước $r$.

::: algorithm Thuật toán 09.20 (AMS khi biết độ dài dòng)
**Đầu vào.** Dòng $x_1,\ldots,x_r$ với $r$ biết trước; số biến $s\ge1$.

**Đầu ra.** Khi dòng kết thúc, $s$ ước lượng $X_1,\ldots,X_s$ của $F_2$ và trung bình của chúng.

**Giả thiết.** $s$ vị trí $I_1,\ldots,I_s$ được rút trước dòng, mỗi vị trí đều trên $\{1,\ldots,r\}$.

1. Rút $I_1,\ldots,I_s$. Mỗi biến ban đầu chưa có phần tử.
2. Khi $x_i$ đến ở vị trí $i$: với mỗi biến đã có phần tử bằng $x_i$, tăng bộ đếm thêm 1; với mỗi biến có vị trí đúng bằng $i$, ghi phần tử $x_i$ và đặt bộ đếm bằng 1.
3. Khi dòng kết thúc: với mỗi biến có bộ đếm $v$, trả $r(2v-1)$; trả thêm trung bình của $s$ ước lượng.

```text
AMS-BIẾT-ĐỘ-DÀI(x_1, …, x_r; s)
    rút I_1, …, I_s đều trên {1, …, r}
    với i = 1, …, r:
        với mỗi biến V đã có phần tử:  nếu V.phần_tử = x_i: V.đếm ← V.đếm + 1
        với mỗi biến V có V.vị_trí = i: V.phần_tử ← x_i;  V.đếm ← 1
    trả r(2·V.đếm − 1) cho mỗi biến V, và trung bình của chúng
```

**Dừng.** Sau $r$ phần tử.

**Trường hợp biên.** Hai biến có thể rút trùng vị trí; khi đó chúng giữ cùng phần tử và cùng bộ đếm.

**Chi phí.** Mỗi phần tử: $O(s)$ phép so sánh trong trường hợp xấu nhất. Bộ nhớ: $s$ cặp (phần tử, bộ đếm), mỗi bộ đếm $\lceil\log_2(r+1)\rceil$ bit.
:::

Bất biến của bước 2: sau khi đọc $x_1,\ldots,x_i$, một biến có vị trí $I\le i$ giữ $x_I$ và bộ đếm bằng số lần $x_I$ xuất hiện trong $x_I,\ldots,x_i$; nó đúng khi biến được tạo và được giữ vì bộ đếm tăng đúng khi phần tử mới bằng $x_I$. Khi $i=r$, bộ đếm bằng $v_I$.

<!-- note-topic-id: lec-09-topic-09 -->
### 3.2 Tính không chệch

Trung bình 55 của Ví dụ 09.7 khác 59. Chúng ta chứng minh rằng trung bình trên mọi cách chọn vị trí bằng đúng 59; chứng minh dùng đồng nhất thức về tổng các số lẻ của MMDS Bài tập 4.5.5 (tr.150).

::: lemma Bổ đề 09.21 (Tổng các số lẻ)
**Giả thiết.** $f$ là số nguyên dương.

**Kết luận.** $1+3+5+\cdots+(2f-1)=\sum_{v=1}^{f}(2v-1)=f^2$.

**Điều kiện áp dụng.** Mọi $f\ge1$; với $f=0$ tổng rỗng bằng $0=0^2$.

**Phạm vi.** Đồng nhất thức trên số nguyên, cho tổng các số lẻ liên tiếp từ 1.
:::

::: proof
**Bước 1 (cơ sở).** Với $f=1$, tổng bằng $1=1^2$.

**Bước 2 (bước quy nạp).** Giả sử $\sum_{v=1}^{f}(2v-1)=f^2$; khi đó

$$
\begin{aligned}
&\sum_{v=1}^{f+1}(2v-1)\\
&\quad=f^2+\bigl(2(f+1)-1\bigr)\\
&\quad=f^2+2f+1=(f+1)^2 .
\end{aligned}
$$

Theo quy nạp, đồng nhất thức đúng với mọi $f\ge1$. $\square$
:::

::: theorem Định lý 09.22 (Biến AMS không chệch)
**Giả thiết.** Dòng $x_1,\ldots,x_r$ cố định, $r\ge1$. Vị trí $I$ đều trên $\{1,\ldots,r\}$. Bộ đếm của biến bằng đúng $v_I$, số lần $x_I$ xuất hiện trong $x_I,\ldots,x_r$.

**Kết luận.** $\mathbb E[X]=\mathbb E[r(2v_I-1)]=F_2$.

**Điều kiện áp dụng.** Xác suất lấy theo phép chọn $I$; độ dài $r$ phải biết khi trả lời để nhân với $2v_I-1$.

**Phạm vi.** Định lý chỉ nói về kỳ vọng. Nó không nói một biến gần $F_2$: ở Ví dụ 09.7, một biến cho 75 trong khi $F_2=59$.
:::

::: proof
**Bước 1 (lấy kỳ vọng theo $I$).** $I$ nhận mỗi giá trị $i\in\{1,\ldots,r\}$ với xác suất $1/r$, nên

$$
\begin{aligned}
\mathbb E[X]
&=\sum_{i=1}^{r}\frac1r\cdot r\,(2v_i-1)\\
&=\sum_{i=1}^{r}(2v_i-1).
\end{aligned}
$$

**Bước 2 (nhóm các vị trí theo phần tử).** Mỗi vị trí mang đúng một phần tử, nên tổng theo vị trí bằng tổng theo phần tử $u$ của tổng trên các vị trí mang $u$. Với $u$ có $f_u\ge1$, gọi các vị trí mang $u$ là $i_1<i_2<\cdots<i_{f_u}$. Đoạn $x_{i_\nu},\ldots,x_r$ chứa đúng các lần xuất hiện $i_\nu,i_{\nu+1},\ldots,i_{f_u}$ của $u$, nên
$$
v_{i_\nu}=f_u-\nu+1
$$
với $\nu=1,\ldots,f_u$. Khi $\nu$ chạy từ $f_u$ về 1, $v_{i_\nu}$ chạy từ 1 lên $f_u$. Bước này dùng giả thiết bộ đếm bằng số lần xuất hiện ở hậu tố.

**Bước 3 (áp dụng Bổ đề 09.21).** Với mỗi $u$,
$$
\begin{aligned}
\sum_{\nu=1}^{f_u}\bigl(2v_{i_\nu}-1\bigr)&=\sum_{v=1}^{f_u}(2v-1)\\
&=f_u^2 .
\end{aligned}
$$

**Bước 4 (cộng theo phần tử).** Phần tử có $f_u=0$ không có vị trí nào và góp $0=f_u^2$. Do đó

$$
\begin{aligned}
&\mathbb E[X]\\
&\quad=\sum_{i=1}^{r}(2v_i-1)\\
&\quad=\sum_{u\in\mathcal U}\ \sum_{\nu=1}^{f_u}\bigl(2v_{i_\nu}-1\bigr)\\
&\quad=\sum_{u\in\mathcal U}f_u^2=F_2.
\end{aligned}
$$

Ba đẳng thức lần lượt dùng Bước 1, Bước 2, và Bước 3 cùng Định nghĩa 09.1. $\square$
:::

Chạy biến AMS nhiều lần với các vị trí rút độc lập, trung bình các ước lượng tiến về $F_2$, dù mỗi lần chỉ giữ một phần tử và một bộ đếm. Phần tử $u$ được chọn với xác suất $f_u/r$, và khi đó trung bình của $2v_I-1$ là $f_u$, nên $u$ góp $r\cdot(f_u/r)\cdot f_u=f_u^2$. Chứng minh theo MMDS (§4.5.3, tr.147–148).

So với Định lý 09.10, Định lý 09.22 cho một bảo đảm loại khác: kỳ vọng đúng bằng đại lượng cần ước lượng, không cần giả thiết băm, nhưng không chặn xác suất lệch của một biến; đổi lại, mỗi biến tốn một bộ đếm cỡ $\lceil\log_2(r+1)\rceil$ bit thay cho một số cỡ $\log_2L$ bit.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "$I$ đều trên $\{1,\ldots,r\}$": nếu $I$ đều trên 5 vị trí đầu của dòng mười lăm phần tử, với $v_1,\ldots,v_5=5,4,3,3,3$, thì $\mathbb E[X]=\frac15\cdot15\cdot(9+7+5+5+5)=93$ thay cho 59.
- Bỏ "bộ đếm là số lần xuất hiện ở hậu tố": nếu bộ đếm là tần suất $f_{x_I}$ của cả dòng, thì $\mathbb E[r(2f_{x_I}-1)]=\sum_uf_u(2f_u-1)=2F_2-F_1$, bằng $118-15=103$ trên dòng mười lăm phần tử.

Bước 1 dùng tính đều của $I$; Bước 2 dùng định nghĩa hậu tố của bộ đếm.

::: example Ví dụ 09.8 (Kiểm trên mọi vị trí và độ phân tán của một biến)
**Dữ kiện.** Dòng $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$, $r=15$, $F_2=59$.

**Tính.** Số lần xuất hiện ở hậu tố tại các vị trí 1 đến 15 là
$$
\begin{aligned}
v_1,\ldots,v_8&=5,4,3,3,3,4,2,2,\\
v_9,\ldots,v_{15}&=3,2,1,1,2,1,1 .
\end{aligned}
$$
Các giá trị $2v_i-1$ là $9,7,5,5,5,7,3,3,5,3,1,1,3,1,1$, tổng bằng 59, nên trung bình của $X=15(2v_I-1)$ trên 15 vị trí đồng khả năng là $15\cdot59/15=59$, đúng như Định lý 09.22. Theo nhóm phần tử: các vị trí của $\mathrm a$ góp $9+7+5+3+1=25$, của $\mathrm b$ góp $7+5+3+1=16$, của $\mathrm c$ và của $\mathrm d$ mỗi phần tử góp $5+3+1=9$.

**Độ phân tán.** Tổng bình phương $\sum_i(2v_i-1)^2=319$, nên
$$
\begin{aligned}
&\mathbb E[X^2]\\
&\quad=\frac1{15}\sum_{i=1}^{15}\bigl(15(2v_i-1)\bigr)^2\\
&\quad=15\cdot319=4\,785,\\
&\operatorname{Var}(X)=4\,785-59^2\\
&\quad=1\,304,
\end{aligned}
$$
và độ lệch chuẩn của một biến là $\sqrt{1\,304}\approx36{,}1$.

**Diễn giải.** Độ lệch chuẩn của một biến khoảng $61\%$ của $F_2$; trung bình của $s$ biến độc lập có phương sai $1\,304/s$ (ghi chú Bài 05, Mục 8), với điều kiện về độc lập ở Nhận xét 09.27.

**Kiểm tra lại.** $25+16+9+9=59$; $\sum_iv_i=37$ và $\sum_i(2v_i-1)=2\cdot37-15=59$.
:::

<!-- note-topic-id: lec-09-topic-10 -->
### 3.3 Mômen bậc cao

Chứng minh Định lý 09.22 chỉ dùng $\sum_{v=1}^{f}(2v-1)=f^2$. MMDS (§4.5.4, tr.148) viết $2v-1=v^2-(v-1)^2$ và đổi bình phương thành lũy thừa bậc $p$.

::: corollary Hệ quả 09.23 (Ước lượng mômen bậc $p$)
**Giả thiết.** Như Định lý 09.22; $p\ge2$ là số nguyên.

**Kết luận.** $X_p=r\bigl(v_I^{\,p}-(v_I-1)^p\bigr)$ thỏa $\mathbb E[X_p]=F_p$. Với $p=3$, $X_3=r(3v_I^2-3v_I+1)$.

**Điều kiện áp dụng.** Biến AMS và thuật toán không đổi; chỉ phép trả lời đổi.

**Phạm vi.** Như Định lý 09.22: chỉ nói về kỳ vọng.
:::

::: proof
**Bước 1 (rút về một tổng).** Bước 1 và Bước 2 của chứng minh Định lý 09.22 không dùng dạng của hàm $2v-1$, nên cho $\mathbb E[X_p]=\sum_u\sum_{v=1}^{f_u}\bigl(v^p-(v-1)^p\bigr)$.

**Bước 2 (tổng lồng nhau).** Tổng trong là tổng lồng nhau (telescoping):

$$
\begin{aligned}
&\sum_{v=1}^{f_u}\bigl(v^p-(v-1)^p\bigr)\\
&=(1^p-0^p)+(2^p-1^p)+\cdots\\
&\quad+\bigl(f_u^{\,p}-(f_u-1)^p\bigr)\\
&=f_u^{\,p}-0^p=f_u^{\,p}.
\end{aligned}
$$

Các số hạng giữa triệt tiêu, và $0^p=0$ vì $p\ge2$. Cộng theo $u$ được $F_p$.

**Bước 3 (trường hợp $p=3$).** $v^3-(v-1)^3=v^3-(v^3-3v^2+3v-1)=3v^2-3v+1$. $\square$
:::

::: example Ví dụ 09.9 (Mômen bậc ba của dòng mười lăm phần tử)
**Dữ kiện.** Dòng $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$ của Ví dụ 09.7; $F_3=5^3+4^3+3^3+3^3=243$.

**Tính.** Ba biến ở vị trí 3, 8, 13 có $v=3,2,2$, cho $X_3=15\cdot19=285$, $15\cdot7=105$, $15\cdot7=105$; trung bình 165. Trên cả 15 vị trí, $3v_i^2-3v_i+1$ nhận các giá trị 61, 37, 19, 19, 19, 37, 7, 7, 19, 7, 1, 1, 7, 1, 1, tổng 243.

**Diễn giải.** Kỳ vọng đúng bằng $F_3$, nhưng ba biến cho 165, lệch xa hơn bậc hai.

**Kiểm tra lại.** Phần của $\mathrm a$: $61+37+19+7+1=125=5^3$.
:::

<!-- note-topic-id: lec-09-topic-11 -->
### 3.4 Dòng chưa biết độ dài

Thuật toán 09.20 rút vị trí trước dòng, nên cần biết $r$. Theo MMDS (§4.5.5, tr.148), phép nhân với $r$ không khó, vì chỉ cần giữ $r$ riêng; khó ở vị trí: chọn vị trí một lần cho mãi thì các vị trí sớm được ưu tiên và ước lượng quá lớn, như kỳ vọng 93 thay cho 59 khi bỏ giả thiết $I$ đều của Định lý 09.22.

Về mặt ý tưởng, các vị trí bắt đầu của $s$ biến cần là một mẫu đều của các vị trí đã đọc ở mọi thời điểm, đúng yêu cầu mà hồ chứa của Bài 08 thỏa (Định lý 08.17). Ví dụ 09.10 chạy nó với hai biến. Ký hiệu $\xi$ là số ngẫu nhiên rút khi phần tử thứ $r>s$ đến.

::: example Ví dụ 09.10 (Vết chạy với hai biến trên năm phần tử đầu)
**Dữ kiện.** Năm phần tử đầu của dòng mười lăm phần tử: $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d$. Số biến $s=2$. Các số ngẫu nhiên đã rút: $\xi=3$ khi $r=3$, $\xi=1$ khi $r=4$, $\xi=4$ khi $r=5$, mỗi số đều trên $\{1,\ldots,r\}$.

**Vết chạy.** Mỗi biến ghi (vị trí, phần tử, bộ đếm). Ở mỗi bước, bộ đếm được tăng trước, rồi mới xét thay biến.

| $r$ | $x_r$ | tăng bộ đếm | $\xi$ | thay | biến 1 | biến 2 |
|---:|---|---|---:|---|---|---|
| 1 | $\mathrm a$ | — | — | tạo biến 1 | $(1,\mathrm a,1)$ | — |
| 2 | $\mathrm b$ | — | — | tạo biến 2 | $(1,\mathrm a,1)$ | $(2,\mathrm b,1)$ |
| 3 | $\mathrm c$ | — | 3 | bỏ, vì $\xi>2$ | $(1,\mathrm a,1)$ | $(2,\mathrm b,1)$ |
| 4 | $\mathrm b$ | biến 2 | 1 | thay biến 1 | $(4,\mathrm b,1)$ | $(2,\mathrm b,2)$ |
| 5 | $\mathrm d$ | — | 4 | bỏ, vì $\xi>2$ | $(4,\mathrm b,1)$ | $(2,\mathrm b,2)$ |

**Ước lượng.** Với $r=5$: biến 1 cho $5\cdot(2\cdot1-1)=5$, biến 2 cho $5\cdot(2\cdot2-1)=15$, trung bình 10. Mômen bậc hai của tiền tố $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d$ là $1+4+1+1=7$.

**Kiểm tra lại.** Trong tiền tố độ dài 5, $\mathrm b$ ở vị trí 2 và 4: từ vị trí 4 có 1 lần, từ vị trí 2 có 2 lần, khớp hai bộ đếm.
:::

::: algorithm Thuật toán 09.24 (AMS trên dòng chưa biết độ dài)
**Đầu vào.** Dòng $x_1,x_2,\ldots$ độ dài không biết trước; số biến $s\ge1$; bộ sinh số nguyên đều.

**Đầu ra.** Khi có truy vấn sau $r$ phần tử, $s$ ước lượng của $F_2$ của tiền tố $x_1,\ldots,x_r$ và trung bình của chúng (hoặc giá trị gộp ở Mục 3.5).

**Giả thiết.** Với $r>s$, $\xi$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước.

1. Khởi tạo $r\gets0$; chưa có biến nào.
2. Khi phần tử $x$ đến: tăng $r$ thêm 1; với mỗi biến có phần tử bằng $x$, tăng bộ đếm thêm 1.
3. Nếu $r\le s$: tạo biến thứ $r$ với (vị trí $r$, phần tử $x$, bộ đếm 1).
4. Nếu $r>s$: rút $\xi$; nếu $\xi\le s$ thì thay biến thứ $\xi$ bằng (vị trí $r$, phần tử $x$, bộ đếm 1), nếu không thì không tạo biến.
5. Khi có truy vấn: mỗi biến có bộ đếm $v$ cho $r(2v-1)$.

**Dừng.** Mỗi phần tử được xử lý sau $O(s)$ bước; thuật toán chạy chừng nào dòng còn phần tử.

**Trường hợp biên.** Khi $r<s$, chỉ có $r$ biến, mỗi vị trí một biến. Vị trí không cần lưu để tính ước lượng; nó chỉ dùng trong phân tích.

**Chi phí.** Mô hình: mỗi phép so sánh, tăng bộ đếm, rút số ngẫu nhiên, ghi tốn $O(1)$; trường hợp xấu nhất.

| Bước | Số lần mỗi phần tử | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| tăng $r$ và so phần tử với $s$ biến (bước 2) | $s$ | $O(1)$ | $O(s)$ |
| rút $\xi$ (bước 4) | tối đa 1 | $O(1)$ | $O(1)$ |
| ghi biến mới (bước 3–4) | tối đa 1 | $O(1)$ | $O(1)$ |
| trả lời (bước 5) | 1 mỗi truy vấn | $O(s)$ | $O(s)$ |

Bộ nhớ: $s$ cặp (phần tử, bộ đếm) và bộ đếm $r$.
:::

Bước 4 là quy tắc của MMDS (tr.149), nhận phần tử thứ $r$ với xác suất $s/r$ và thay một biến chọn đều: $\xi\le s$ với xác suất $s/r$, và với điều kiện đó, $\xi$ đều trên $\{1,\ldots,s\}$. Đây là Thuật toán 08.16 áp cho vị trí; Ví dụ 09.10 là một lượt chạy với $s=2$.

Ký hiệu $v_i^{(r)}$ là số lần $x_i$ xuất hiện trong $x_i,\ldots,x_r$, tức $v_i$ của Định nghĩa 09.19 tính trên tiền tố độ dài $r$.

::: proposition Mệnh đề 09.25 (Vị trí và giá trị của các biến)
**Giả thiết.** Như Thuật toán 09.24; $r\ge s$.

**Kết luận.**

- (a) Các biến giữ $s$ vị trí khác nhau; gọi tập các vị trí đó là $\mathcal W_r$. Với mọi $i\le r$, $\Pr[i\in\mathcal W_r]=s/r$.
- (b) Biến có vị trí $i$ giữ phần tử $x_i$ và bộ đếm $v_i^{(r)}$.

**Điều kiện áp dụng.** Xác suất lấy theo các lần rút $\xi$; dòng cố định.

**Phạm vi.** (a) nói về từng vị trí, không nói các biến độc lập.
:::

::: proof
**Bước 1 (phần (a)).** Các bước 3 và 4 của Thuật toán 09.24 thao tác trên vị trí đúng như Thuật toán 08.16 thao tác trên phần tử: $s$ vị trí đầu được ghi vào $s$ biến, và với $r>s$, vị trí $r$ thay biến thứ $\xi$ khi $\xi\le s$. Theo Định lý 08.17, sau $r\ge s$ bước, có đúng $s$ vị trí được giữ, mỗi vị trí $i\le r$ có mặt với xác suất $s/r$. Mỗi biến giữ một vị trí, nên các vị trí khác nhau.

**Bước 2 (phần (b), quy nạp theo $r$).** Khẳng định (b) đúng trước khi có phần tử nào. Giả sử (b) đúng sau $r-1$ phần tử. Khi $x_r$ đến, xét một biến còn lại sau bước $r$.

- Nếu biến được tạo ở bước $r$, vị trí của nó là $r$, phần tử là $x_r$, bộ đếm 1; và $v_r^{(r)}=1$ vì đoạn $x_r,\ldots,x_r$ chỉ có một vị trí.
- Nếu biến có vị trí $i<r$, theo giả thiết quy nạp nó giữ $x_i$ và $v_i^{(r-1)}$ trước bước $r$. Bước 2 tăng bộ đếm đúng khi $x_r=x_i$, còn $v_i^{(r)}=v_i^{(r-1)}+\mathbf 1[x_r=x_i]$ theo định nghĩa. Hai đại lượng tăng như nhau.

Biến bị thay ở bước $r$ không còn, nên không cần xét. Theo quy nạp, (b) đúng với mọi $r$. $\square$
:::

::: corollary Hệ quả 09.26 (Trung bình $s$ biến không chệch)
**Giả thiết.** Như Mệnh đề 09.25. Gọi $\bar X$ là trung bình của $s$ ước lượng $r(2v-1)$ của các biến sau $r\ge s$ phần tử.

**Kết luận.** $\mathbb E[\bar X]=F_2$, trong đó $F_2$ là mômen bậc hai của tiền tố $x_1,\ldots,x_r$.

**Điều kiện áp dụng.** Như Mệnh đề 09.25.

**Phạm vi.** Hệ quả nói về trung bình $s$ biến. Từng biến riêng lẻ không có vị trí đều: với $r=s$, biến thứ $i$ chắc chắn giữ vị trí $i$.
:::

::: proof
Theo Mệnh đề 09.25(b), tổng $s$ ước lượng viết được theo các vị trí. Với $\varsigma_i=r\bigl(2v_i^{(r)}-1\bigr)$,

$$
\begin{aligned}
&\mathbb E\Bigl[\,\sum_{\text{biến}}r\bigl(2v-1\bigr)\Bigr]\\
&\quad=\mathbb E\Bigl[\,\sum_{i=1}^{r}\mathbf 1[i\in\mathcal W_r]\,\varsigma_i\Bigr]\\
&\quad=\sum_{i=1}^{r}\Pr[i\in\mathcal W_r]\,\varsigma_i\\
&\quad=\sum_{i=1}^{r}\frac sr\,\varsigma_i\\
&\quad=s\sum_{i=1}^{r}\bigl(2v_i^{(r)}-1\bigr)=s\,F_2.
\end{aligned}
$$

Ba đẳng thức sau lần lượt dùng tuyến tính kỳ vọng, Mệnh đề 09.25(a) và Bước 2–4 của chứng minh Định lý 09.22. Chia cho $s$ được $\mathbb E[\bar X]=F_2$. $\square$
:::

Với Ví dụ 09.10, hệ quả cho $\mathbb E[\bar X]=7$ sau $r=5$; lượt chạy cụ thể cho 10.

### 3.5 Gộp biến, chi phí và nhầm lẫn

::: remark Nhận xét 09.27 (Các biến của một hồ chứa chung không độc lập)
Hệ quả 09.26 chỉ dùng tuyến tính kỳ vọng, nên đúng dù các biến không độc lập. Phương sai $1\,304/s$ của Ví dụ 09.8 và Bổ đề 09.14 thì cần các biến độc lập. Các biến của Thuật toán 09.24 luôn giữ $s$ vị trí khác nhau, nên vị trí của một biến làm đổi phân phối vị trí của biến khác.

Muốn có các biến độc lập, ta chạy $s$ hồ chứa cỡ 1 độc lập, mỗi hồ một lần rút cho mỗi phần tử; theo Định lý 08.17 với $s=1$, mỗi biến có vị trí đều. Giá phải trả là $s$ lần rút mỗi phần tử, và hai biến có thể trùng vị trí.
:::

::: remark Nhận xét 09.28 (Trong thực hành: gộp biến và chi phí)
MMDS (§4.8, tr.160) gộp các ước lượng AMS như của Flajolet–Martin (Thuật toán 09.13); trang chiếu Stanford CS246 (2017, Streams 2, tr.49) gợi ý dùng khoảng 100 biến. Bộ nhớ là $s$ mã phần tử cộng $s+1$ bộ đếm $\lceil\log_2(r+1)\rceil$ bit; số ngẫu nhiên $\xi$ lấy từ bộ sinh số giả ngẫu nhiên (Nhận xét 08.21).
:::

::: remark Nhận xét 09.29 (Nhầm lẫn thường gặp)
- Bộ đếm $v_I$ không phải tần suất $f_{x_I}$; dùng $f_{x_I}$ cho kỳ vọng $2F_2-F_1$.
- Không chệch không có nghĩa từng biến gần $F_2$: một biến có độ lệch chuẩn khoảng 36 khi $F_2=59$ (Ví dụ 09.8).
- Trong Thuật toán 09.24, chỉ trung bình $s$ biến có kỳ vọng $F_2$, không phải từng biến (Hệ quả 09.26).
:::

::: exercise Bài tập 09.4 (Đếm ở tiền tố thay cho hậu tố)
Cho dòng $x_1,\ldots,x_r$ cố định và $I$ đều trên $\{1,\ldots,r\}$. Đặt $\tilde v_I$ là số lần $x_I$ xuất hiện trong $x_1,\ldots,x_I$ (đếm từ đầu dòng tới vị trí $I$, kể cả $I$).
- (a) Chứng minh $\mathbb E[r(2\tilde v_I-1)]=F_2$.
- (b) Kiểm lại trên dòng $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d,\mathrm a,\mathrm c,\mathrm d,\mathrm a,\mathrm b,\mathrm d,\mathrm c,\mathrm a,\mathrm a,\mathrm b$ bằng cách tính $\tilde v_1,\ldots,\tilde v_{15}$.
:::

::: hint
(a) Lặp lại Bước 2 của chứng minh Định lý 09.22: trên các vị trí $i_1<\cdots<i_{f_u}$ của $u$, $\tilde v_{i_\nu}=\nu$.
:::

::: solution
(a) Như Bước 1, $\mathbb E[r(2\tilde v_I-1)]=\sum_{i=1}^r(2\tilde v_i-1)$. Với $u$ có các vị trí $i_1<\cdots<i_{f_u}$, đoạn $x_1,\ldots,x_{i_\nu}$ chứa đúng $\nu$ lần xuất hiện của $u$, nên $\tilde v_{i_\nu}=\nu$. Tổng trên các vị trí của $u$ là $\sum_{\nu=1}^{f_u}(2\nu-1)=f_u^2$ (Bổ đề 09.21); cộng theo $u$ được $F_2$.

(b) $\tilde v_1,\ldots,\tilde v_{15}=1,1,1,2,1,2,2,2,3,3,3,3,4,5,4$. Các giá trị $2\tilde v_i-1$ có tổng $1+1+1+3+1+3+3+3+5+5+5+5+7+9+7=59$.

**Kiểm tra lại.** Phần của $\mathrm a$ (vị trí 1, 6, 9, 13, 14): $\tilde v=1,2,3,4,5$, góp $1+3+5+7+9=25=5^2$.
:::

::: exercise Bài tập 09.5 (Hồ chứa vị trí cho hai biến AMS)
Chạy Thuật toán 09.24 với $s=2$ trên sáu phần tử đầu $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d,\mathrm a$ của dòng mười lăm phần tử, với $\xi=1$ khi $r=3$, $\xi=4$ khi $r=4$, $\xi=2$ khi $r=5$, $\xi=6$ khi $r=6$. Lập vết chạy, tính ước lượng trung bình sau $r=6$, kiểm Mệnh đề 09.25(b), và tính $\mathbb E[\bar X]$ theo Hệ quả 09.26 cùng xác suất vị trí 1 còn được giữ.
:::

::: hint
Ở mỗi bước, tăng bộ đếm trước rồi mới xét thay biến.
:::

::: solution
| $r$ | $x_r$ | tăng bộ đếm | $\xi$ | biến 1 | biến 2 |
|---:|---|---|---:|---|---|
| 1 | $\mathrm a$ | — | — | $(1,\mathrm a,1)$ | — |
| 2 | $\mathrm b$ | — | — | $(1,\mathrm a,1)$ | $(2,\mathrm b,1)$ |
| 3 | $\mathrm c$ | — | 1 | $(3,\mathrm c,1)$ | $(2,\mathrm b,1)$ |
| 4 | $\mathrm b$ | biến 2 | 4 | $(3,\mathrm c,1)$ | $(2,\mathrm b,2)$ |
| 5 | $\mathrm d$ | — | 2 | $(3,\mathrm c,1)$ | $(5,\mathrm d,1)$ |
| 6 | $\mathrm a$ | — | 6 | $(3,\mathrm c,1)$ | $(5,\mathrm d,1)$ |

Với $r=6$, mỗi biến cho $6\cdot1=6$, trung bình 6. Trong tiền tố, $\mathrm c$ chỉ ở vị trí 3 và $\mathrm d$ chỉ ở vị trí 5, nên $v_3^{(6)}=v_5^{(6)}=1$, khớp hai bộ đếm. Tiền tố có $F_2=4+4+1+1=10$, nên $\mathbb E[\bar X]=10$; vị trí 1 còn được giữ với xác suất $s/r=1/3$.

**Kiểm tra lại.** $v^{(6)}=2,2,1,1,1,1$ và $\sum_i(2v_i^{(6)}-1)=10=F_2$.
:::

Như vậy, chúng ta đã có một ước lượng không chệch cho $F_2$ chỉ bằng một cặp (phần tử, bộ đếm) cho mỗi biến (Định nghĩa 09.19, Định lý 09.22), mở rộng cho mọi $F_p$ (Hệ quả 09.23) và cho dòng chưa biết độ dài bằng hồ chứa vị trí (Thuật toán 09.24, Mệnh đề 09.25, Hệ quả 09.26). Tuy nhiên, $F_2$ không cho biết phần tử nào chiếm phần lớn dòng hay một phần tử cho trước xuất hiện bao nhiêu lần. Trong Mục 4, chúng ta ước lượng $f_u$ bằng một bảng đếm nhỏ.

## 4. Ước lượng tần suất bằng Count-Min Sketch

Câu hỏi thứ hai của Ví dụ 09.1 là tần suất $f_u$ của một phần tử. Theo UMass (bài 10, trang chiếu 9), bài toán gần với nó là tìm phần tử nặng (heavy hitters, còn gọi là frequent items): địa chỉ IP gửi rất nhiều yêu cầu trong một tấn công từ chối dịch vụ (denial of service, DoS), hay sản phẩm đang được tìm nhiều.

Lời giải chính xác giữ $d$ bộ đếm (Nhận xét 09.3); chúng ta cần một phác thảo có cỡ không phụ thuộc $d$, trả lời được $f_u$ cho mọi $u$, kèm cận sai số. Count-Min được trình bày theo UMass (bài 10).

<!-- note-topic-id: lec-09-topic-12 -->
### 4.1 Bài toán phần tử nặng

Trên dòng $x_1,\ldots,x_r$, bài toán $\kappa$-phần tử nặng hỏi mọi phần tử xuất hiện ít nhất $r/\kappa$ lần (UMass, trang chiếu 8). Vì $\sum_uf_u=r$, có nhiều nhất $\kappa$ phần tử như vậy. Trên dòng mười lăm phần tử với $\kappa=3$, ngưỡng là $15/3=5$ và chỉ $\mathrm a$ đạt.

UMass (trang chiếu 11) chỉ ra rằng với bộ nhớ nhỏ, khó phân biệt phần tử xuất hiện $r/\kappa$ lần, phải có trong đáp số, với phần tử xuất hiện $r/\kappa-1$ lần, không được có trong đáp số; vì vậy bài toán được nới lỏng như sau.

::: definition Định nghĩa 09.30 (Bài toán $(\varepsilon,\kappa)$-phần tử nặng)
Cho dòng $x_1,\ldots,x_r$, số thực $\kappa\ge1$ và $0<\varepsilon\le1$. Một lời giải của **bài toán $(\varepsilon,\kappa)$-phần tử nặng** ($(\varepsilon,\kappa)$-frequent items problem) là một tập $\mathcal F\subseteq\mathcal U$ sao cho

- mọi $u$ có $f_u\ge r/\kappa$ thuộc $\mathcal F$;
- mọi $u\in\mathcal F$ có $f_u\ge(1-\varepsilon)r/\kappa$.
:::

Phần tử có tần suất trong $[(1-\varepsilon)r/\kappa,\,r/\kappa)$ thuộc hay không thuộc $\mathcal F$ đều được; UMass gọi đây là bài toán có hứa hẹn (promise problem). Trên dòng mười lăm phần tử với $\kappa=3$, $\varepsilon=1/4$, ngưỡng dưới là $3{,}75$, nên $\mathcal F$ phải chứa $\mathrm a$, được chứa $\mathrm b$, không được chứa $\mathrm c$, $\mathrm d$. Một ước lượng không thấp hơn $f_u$ và thừa ít hơn $\varepsilon r/\kappa$ đủ để giải bài toán này (Hệ quả 09.38).

<!-- note-topic-id: lec-09-topic-13 -->
### 4.2 Họ băm phổ dụng và bất đẳng thức Markov

Phân tích Count-Min cần một cận cho xác suất hai phần tử khác nhau trùng giá trị băm và một cận cho xác suất một biến không âm lớn hơn nhiều kỳ vọng của nó. Tính đều của từng giá trị băm (Mệnh đề 08.10(b)) không đủ: gán cùng một giá trị ngẫu nhiên đều cho mọi phần tử thỏa nó mà làm mọi cặp trùng nhau.

::: definition Định nghĩa 09.31 (Họ băm phổ dụng và họ độc lập từng cặp)
Cho họ $\mathcal H$ các hàm $\mathcal U\to\{0,\ldots,m-1\}$; hàm $h$ được chọn đều từ $\mathcal H$.

- $\mathcal H$ là **họ băm phổ dụng** (universal hash family) nếu với mọi $u\ne u'$ thuộc $\mathcal U$: $\Pr_h[h(u)=h(u')]\le1/m$.
- $\mathcal H$ là **họ độc lập từng cặp** (pairwise independent family) nếu với mọi $u\ne u'$ và mọi $a,a'\in\{0,\ldots,m-1\}$: $\Pr_h[h(u)=a,\ h(u')=a']=1/m^2$.
:::

Họ độc lập từng cặp là họ băm phổ dụng, vì $\Pr[h(u)=h(u')]=\sum_{a=0}^{m-1}\Pr[h(u)=a,h(u')=a]=m\cdot\frac1{m^2}=\frac1m$. UMass (trang chiếu 14) cho biết cận Count-Min chỉ cần cận va chạm của họ băm phổ dụng. Phản ví dụ của họ băm phổ dụng là họ chỉ có một hàm hằng: mọi cặp trùng với xác suất 1.

BHK (tr.184) gọi họ độc lập từng cặp là 2-universal; tính chất đó mạnh hơn và kéo theo cận va chạm.

BHK (§6.2.1, tr.184–185) cho một ví dụ họ độc lập từng cặp: mã hóa phần tử thành số nguyên $w\in\{0,\ldots,P-1\}$ với $P$ nguyên tố, $P\ge\lvert\mathcal U\rvert$, và lấy $h_{\alpha,\beta}(w)=(\alpha w+\beta)\bmod P$ với $\alpha,\beta$ rút đều. Với $w\ne w'$, hệ hai đồng dư tuyến tính theo $(\alpha,\beta)$ có đúng một nghiệm vì $w-w'$ khả nghịch theo modulo $P$, nên mỗi cặp giá trị có xác suất $1/P^2$.

Miền giá trị có $P\ge\lvert\mathcal U\rvert$ phần tử, nên họ này không nén được bảng đếm; cách dựng họ băm phổ dụng có miền $\{0,\ldots,m-1\}$ nhỏ nằm ngoài phạm vi học phần.

Bất đẳng thức sau là BHK Định lý 2.1 (tr.13), viết cho biến rời rạc.

::: lemma Bổ đề 09.32 (Bất đẳng thức Markov)
**Giả thiết.** $Z$ là biến ngẫu nhiên không âm nhận hữu hạn giá trị; $z>0$.

**Kết luận.** $\Pr[Z\ge z]\le\mathbb E[Z]/z$.

**Điều kiện áp dụng.** Chỉ cần $Z\ge0$; không cần độc lập hay phân phối cụ thể.

**Phạm vi.** Phát biểu cho biến nhận hữu hạn giá trị; cận chỉ có ích khi $z>\mathbb E[Z]$.
:::

::: proof
$$
\begin{aligned}
&\mathbb E[Z]\\
&\quad=\sum_{\zeta}\zeta\Pr[Z=\zeta]\\
&\quad\ge\sum_{\zeta\ge z}\zeta\Pr[Z=\zeta]\\
&\quad\ge z\sum_{\zeta\ge z}\Pr[Z=\zeta]\\
&\quad=z\Pr[Z\ge z].
\end{aligned}
$$
Các tổng lấy trên các giá trị $\zeta$ của $Z$. Đẳng thức đầu là định nghĩa kỳ vọng; bất đẳng thức thứ nhất bỏ các số hạng $\zeta<z$, không âm vì $Z\ge0$; bất đẳng thức thứ hai dùng $\zeta\ge z$. Chia hai vế cho $z>0$. $\square$
:::

Bỏ giả thiết không âm thì bổ đề sai: $Z=10$ hoặc $-10$ với xác suất $1/2$ mỗi giá trị có $\mathbb E[Z]=0$ nhưng $\Pr[Z\ge10]=1/2$. Bất đẳng thức thứ nhất của chứng minh dùng đúng giả thiết này.

<!-- note-topic-id: lec-09-topic-14 -->
### 4.3 Bảng $t\times m$ và phép lấy cực tiểu

Một cách trực quan, nhiều phần tử dùng chung một bộ đếm trong một mảng nhỏ qua một hàm băm, nên bộ đếm của $u$ bằng $f_u$ cộng tần suất của các phần tử va chạm, không bao giờ nhỏ hơn $f_u$. Với nhiều mảng và hàm băm độc lập, bộ đếm nhỏ nhất là bộ đếm ít nhiễu nhất (UMass, trang chiếu 12–16). Ví dụ 09.11, theo UMass, cho thấy phép lấy cực tiểu.

::: example Ví dụ 09.11 (Ba ô của một phần tử)
**Dữ kiện.** Theo UMass (bài 10, trang chiếu 16), ba ô mà phần tử $u$ được băm tới ở hàng 1, 2, 3 của một bảng ba hàng chứa lần lượt 104, 78 và 90.

**Tính.** Mỗi ô bằng $f_u$ cộng một lượng không âm, nên $f_u\le104$, $f_u\le78$ và $f_u\le90$. Cận chặt nhất cho ước lượng $\widehat f_u=\min(104,78,90)=78$.

**Kiểm tra lại.** Mọi ô đều $\ge78$, nên 78 là cận trên nhỏ nhất trong ba cận.
:::

::: definition Định nghĩa 09.33 (Count-Min Sketch)
Cho số ô mỗi hàng $m\ge1$ và số hàng $t\ge1$. Một **Count-Min Sketch** gồm $t$ hàm băm $h_1,\ldots,h_t:\mathcal U\to\{0,\ldots,m-1\}$ và $t$ mảng $A_1,\ldots,A_t$, mỗi mảng $m$ số nguyên. Sau dòng $x_1,\ldots,x_r$, ô $a$ của hàng $j$ bằng
$$
A_j[a]=\sum_{u\in\mathcal U:\ h_j(u)=a}f_u ,
$$
và **ước lượng tần suất** của $u$ là $\widehat f_u=\min_{1\le j\le t}A_j[h_j(u)]$.
:::

Mỗi hàng là một bảng tần suất "nén": ô $A_j[h_j(u)]$ chứa $f_u$ cộng tần suất của các phần tử va chạm với $u$, và tổng các ô của một hàng bằng $r$. Ví dụ 09.11 là trường hợp $t=3$.

So với Bloom filter (Định nghĩa 08.22), Count-Min cũng dùng nhiều hàm băm và ô dùng chung, nhưng thay bit bằng bộ đếm và phép "mọi bit bằng 1" bằng phép lấy cực tiểu (UMass, trang chiếu 12).

::: example Ví dụ 09.12 (Bảng $2\times3$ trên dòng mười lăm phần tử)
**Dữ kiện.** Dòng của Ví dụ 09.1; $f_{\mathrm a}=5$, $f_{\mathrm b}=4$, $f_{\mathrm c}=f_{\mathrm d}=3$. Bảng có $t=2$ hàng, $m=3$ ô. Hai hàm băm:

| | $\mathrm a$ | $\mathrm b$ | $\mathrm c$ | $\mathrm d$ |
|---|---:|---:|---:|---:|
| $h_1$ | 0 | 1 | 2 | 0 |
| $h_2$ | 1 | 2 | 1 | 0 |

**Năm bước đầu.** Mỗi phần tử tăng một ô ở mỗi hàng.

| $r$ | $x_r$ | $A_1$ | $A_2$ |
|---:|---|---|---|
| 1 | $\mathrm a$ | $[1,0,0]$ | $[0,1,0]$ |
| 2 | $\mathrm b$ | $[1,1,0]$ | $[0,1,1]$ |
| 3 | $\mathrm c$ | $[1,1,1]$ | $[0,2,1]$ |
| 4 | $\mathrm b$ | $[1,2,1]$ | $[0,2,2]$ |
| 5 | $\mathrm d$ | $[2,2,1]$ | $[1,2,2]$ |

**Cuối dòng.** Theo Định nghĩa 09.33, $A_1=[f_{\mathrm a}+f_{\mathrm d},\,f_{\mathrm b},\,f_{\mathrm c}]=[8,4,3]$ và $A_2=[f_{\mathrm d},\,f_{\mathrm a}+f_{\mathrm c},\,f_{\mathrm b}]=[3,8,4]$. Ước lượng:

- $\widehat f_{\mathrm a}=\min(A_1[0],A_2[1])=\min(8,8)=8$, thật là 5;
- $\widehat f_{\mathrm b}=\min(A_1[1],A_2[2])=\min(4,4)=4$, đúng;
- $\widehat f_{\mathrm c}=\min(A_1[2],A_2[1])=\min(3,8)=3$, đúng;
- $\widehat f_{\mathrm d}=\min(A_1[0],A_2[0])=\min(8,3)=3$, đúng.

**Diễn giải.** $\mathrm a$ va chạm với $\mathrm d$ ở hàng 1 và với $\mathrm c$ ở hàng 2, nên cả hai ô của nó đều có nhiễu 3. $\mathrm c$ và $\mathrm d$ có một hàng không va chạm, và phép lấy cực tiểu chọn đúng hàng đó.

**Kiểm tra lại.** Mỗi hàng có tổng $8+4+3=3+8+4=15=r$.
:::

::: algorithm Thuật toán 09.34 (Cập nhật và truy vấn Count-Min)
**Đầu vào.** Dòng $x_1,x_2,\ldots$; tham số $m$, $t$; hàm băm $h_1,\ldots,h_t$ chọn trước dòng.

**Đầu ra.** Khi được hỏi về $u$, ước lượng $\widehat f_u$.

**Giả thiết.** Mỗi phần tử của dòng làm tăng tần suất của nó thêm đúng 1 (UMass, trang chiếu 12).

1. Khởi tạo $A_j[a]\gets0$ với mọi $j\in\{1,\ldots,t\}$, $a\in\{0,\ldots,m-1\}$.
2. Khi $x$ đến: với $j=1,\ldots,t$, đặt $A_j[h_j(x)]\gets A_j[h_j(x)]+1$.
3. Khi được hỏi về $u$: trả $\min_{1\le j\le t}A_j[h_j(u)]$.

```text
COUNT-MIN(x_1, x_2, …; m, t, h_1, …, h_t)
    A_j[a] ← 0  với mọi j, a
    với mỗi phần tử x đến:
        với j = 1, …, t:  A_j[h_j(x)] ← A_j[h_j(x)] + 1
    truy vấn u:  trả min_j A_j[h_j(u)]
```

**Dừng.** Mỗi phần tử và mỗi truy vấn được xử lý sau $t$ bước.

**Trường hợp biên.** Phần tử chưa từng xuất hiện có $f_u=0$ nhưng có thể nhận ước lượng dương do va chạm.

**Chi phí.** Mô hình: mỗi phép băm, cộng, đọc, so sánh tốn $O(1)$; trường hợp xấu nhất.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| khởi tạo (bước 1) | $mt$ ô, một lần | $O(1)$ | $O(mt)$ |
| cập nhật (bước 2) | $t$ mỗi phần tử | $O(1)$ | $O(t)$ mỗi phần tử |
| truy vấn (bước 3) | $t$ mỗi truy vấn | $O(1)$ | $O(t)$ mỗi truy vấn |

Bộ nhớ: $mt$ bộ đếm, mỗi bộ đếm $\lceil\log_2(r+1)\rceil$ bit, cộng phần lưu $t$ hàm băm.
:::

Mọi thông tin về dòng nằm trong $mt$ bộ đếm, và phép lấy cực tiểu ở bước 3 quyết định câu trả lời. Ví dụ 09.12 là một lượt chạy với $t=2$, $m=3$.

<!-- note-topic-id: lec-09-topic-15 -->
### 4.4 Bảo đảm của Count-Min

Trong Ví dụ 09.12, $\mathrm a$ bị ước lượng thừa 3 đơn vị. Chúng ta cần hai điều: ước lượng không bao giờ thấp hơn giá trị thật, và với xác suất cao không thừa quá $\varepsilon r/\kappa$. Điều thứ nhất là tất định; điều thứ hai dùng hai công cụ của Mục 4.2.

::: lemma Bổ đề 09.35 (Ô không nhỏ hơn tần suất)
**Giả thiết.** Thuật toán 09.34 trên dòng $x_1,\ldots,x_r$.

**Kết luận.** Với mọi $j$ và $a$, $A_j[a]=\sum_{u:\,h_j(u)=a}f_u$. Do đó, với mọi $u$ và $j$,
$$
\begin{aligned}
A_j[h_j(u)]&=f_u+Z_j,\\
Z_j&=\sum_{\substack{u'\ne u\\ h_j(u')=h_j(u)}}f_{u'}\ \ge0,
\end{aligned}
$$
và $\widehat f_u=f_u+\min_jZ_j\ge f_u$.

**Điều kiện áp dụng.** Mọi dòng và mọi hàm băm; không cần giả thiết xác suất.

**Phạm vi.** Kết luận dựa vào việc bộ đếm chỉ tăng: mỗi phần tử cộng 1 vào tần suất của nó.
:::

::: proof
**Bước 1 (bất biến, quy nạp theo $r$).** Với $r=0$, mọi ô bằng 0 và mọi $f_u=0$. Giả sử đẳng thức đúng sau $r-1$ phần tử. Phần tử $x_r$ tăng $f_{x_r}$ thêm 1 và tăng đúng một ô ở hàng $j$, ô $h_j(x_r)$, là ô có tổng chứa $f_{x_r}$. Hai vế của đẳng thức ô tăng như nhau ở mọi hàng.

**Bước 2 (tách số hạng của $u$).** Trong tổng $\sum_{u'':\,h_j(u'')=h_j(u)}f_{u''}$ có số hạng $u''=u$; phần còn lại là $Z_j$, một tổng các tần suất, nên $Z_j\ge0$.

**Bước 3 (lấy cực tiểu).** $\widehat f_u=\min_j(f_u+Z_j)=f_u+\min_jZ_j\ge f_u$. $\square$
:::

::: lemma Bổ đề 09.36 (Nhiễu của một hàng)
**Giả thiết.** Như Bổ đề 09.35; $h_j$ được chọn đều từ một họ băm phổ dụng $\mathcal U\to\{0,\ldots,m-1\}$; $u$ cố định; $r\ge1$.

**Kết luận.** $\mathbb E[Z_j]\le(r-f_u)/m\le r/m$ và $\Pr\bigl[Z_j\ge2r/m\bigr]\le1/2$.

**Điều kiện áp dụng.** Chỉ cần cận va chạm từng cặp của Định nghĩa 09.31.

**Phạm vi.** Một hàng, một phần tử cố định.
:::

::: proof
**Bước 1 (kỳ vọng).** Viết $Z_j=\sum_{u'\ne u}f_{u'}\,\mathbf 1[h_j(u')=h_j(u)]$. Các tần suất cố định, vì dòng cố định; chỉ $h_j$ ngẫu nhiên. Do đó

$$
\begin{aligned}
&\mathbb E[Z_j]\\
&\quad=\sum_{u'\ne u}f_{u'}\Pr[h_j(u')=h_j(u)]\\
&\quad\le\sum_{u'\ne u}f_{u'}\cdot\frac1m\\
&\quad=\frac{r-f_u}{m}\le\frac rm.
\end{aligned}
$$

Đẳng thức đầu dùng tuyến tính kỳ vọng và $\mathbb E[\mathbf 1[E]]=\Pr(E)$, bất đẳng thức tiếp theo dùng tính phổ dụng của họ băm, đẳng thức cuối dùng $\sum_{u'}f_{u'}=r$.

**Bước 2 (Markov).** $Z_j\ge0$ (Bổ đề 09.35) và nhận hữu hạn giá trị. Theo Bổ đề 09.32 với $z=2r/m$,
$$
\begin{aligned}
\Pr[Z_j\ge2r/m]&\le\frac{\mathbb E[Z_j]}{2r/m}\\
&\le\frac{r/m}{2r/m}\\
&=\frac12.\qquad\square
\end{aligned}
$$
:::

Cận kỳ vọng thành đẳng thức khi họ độc lập từng cặp. Một hàng cho sai số không quá $2r/m$ với xác suất ít nhất $1/2$, chưa đủ để dùng. Định lý sau khuếch đại xác suất bằng các hàng độc lập, theo cùng bước tích của Định lý 06.7.

::: theorem Định lý 09.37 (Bảo đảm của Count-Min)
**Giả thiết.** Dòng $x_1,\ldots,x_r$ cố định, $r\ge1$, mỗi phần tử cộng 1 vào tần suất của nó. Tham số $\kappa\ge1$, $0<\varepsilon\le1$, $0<\delta<1$; $m=\lceil2\kappa/\varepsilon\rceil$, $t=\lceil\log_2(1/\delta)\rceil$. Các hàm $h_1,\ldots,h_t$ được chọn độc lập với nhau, mỗi hàm đều từ một họ băm phổ dụng $\mathcal U\to\{0,\ldots,m-1\}$ (Định nghĩa 09.31).

**Kết luận.** Với mỗi $u\in\mathcal U$ cố định: $\widehat f_u\ge f_u$ chắc chắn, và
$$
\Pr\Bigl[\widehat f_u\ge f_u+\frac{\varepsilon r}{\kappa}\Bigr]\le2^{-t}\le\delta .
$$

**Điều kiện áp dụng.** Xác suất lấy theo phép chọn các hàm băm. Tính độc lập giữa các hàng là giả thiết riêng; UMass (trang chiếu 17) dùng nó mà không phát biểu.

**Phạm vi.** Bảo đảm cho từng phần tử cố định. Sai số tính theo $r$, nên tăng khi dòng dài ra; với phần tử có $f_u$ nhỏ hơn nhiều $\varepsilon r/\kappa$, ước lượng có thể lớn hơn $f_u$ nhiều lần. Bộ nhớ $mt=O\bigl(\frac\kappa\varepsilon\log\frac1\delta\bigr)$ bộ đếm không phụ thuộc $d$ (UMass, trang chiếu 18).
:::

::: proof
**Bước 1 (cận dưới).** Bổ đề 09.35 cho $\widehat f_u=f_u+\min_jZ_j\ge f_u$ với mọi lựa chọn hàm băm.

**Bước 2 (đổi về nhiễu).** Biến cố $\widehat f_u\ge f_u+\varepsilon r/\kappa$ đúng khi $\min_jZ_j\ge\varepsilon r/\kappa$, tức khi mọi $Z_j\ge\varepsilon r/\kappa$. Vì $m\ge2\kappa/\varepsilon$, ta có $2r/m\le\varepsilon r/\kappa$, nên mỗi $Z_j\ge\varepsilon r/\kappa$ kéo theo $Z_j\ge2r/m$.

**Bước 3 (tích trên các hàng).** $Z_j$ chỉ phụ thuộc $h_j$, và các $h_j$ độc lập, nên các biến cố $\{Z_j\ge2r/m\}$ độc lập. Do đó

$$
\begin{aligned}
&\Pr\Bigl[\widehat f_u\ge f_u+\frac{\varepsilon r}\kappa\Bigr]\\
&\quad\le\Pr\Bigl[\,\bigcap_{j=1}^{t}\{Z_j\ge2r/m\}\Bigr]\\
&\quad=\prod_{j=1}^{t}\Pr[Z_j\ge2r/m]\\
&\quad\le2^{-t}\\
&\quad\le\delta.
\end{aligned}
$$

Bốn quan hệ lần lượt dùng Bước 2, tính độc lập của các hàng, Bổ đề 09.36 và $2^t\ge2^{\log_2(1/\delta)}=1/\delta$. $\square$
:::

Count-Min không bao giờ báo ít hơn tần suất thật, và với $\delta=0{,}01$, trong 100 lần dựng bảng với các hàm băm chọn độc lập, ít nhất khoảng 99 lần ước lượng của phần tử được hỏi có sai số dưới $\varepsilon r/\kappa$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "họ băm phổ dụng": nếu mọi hàng dùng một hàm hằng, mọi phần tử va chạm ở mọi hàng, $Z_j=r-f_u$, và trên dòng mười lăm phần tử mọi ước lượng bằng 15.
- Bỏ "các hàng độc lập": nếu mọi hàng dùng cùng một hàm $h_1$, thì $\widehat f_u=A_1[h_1(u)]$ và xác suất thất bại bằng xác suất của một hàng, không giảm theo $t$. Trong Ví dụ 09.12, nếu hàng 2 dùng $h_1$, các ước lượng thành $8,4,3,8$ thay cho $8,4,3,3$.
- Bỏ "$m\ge2\kappa/\varepsilon$": với $m$ nhỏ hơn, Bước 2 không còn đúng; ví dụ $m=1$ cho mọi ô bằng $r$ và sai số $r-f_u$ chắc chắn.

Bước 2 dùng điều kiện về $m$; Bước 3 dùng tính độc lập giữa các hàng; Bổ đề 09.36, được gọi ở Bước 3, dùng tính phổ dụng.

::: corollary Hệ quả 09.38 (Mọi phần tử cùng lúc và bài toán phần tử nặng)
**Giả thiết.** Như Định lý 09.37, nhưng $t=\lceil\log_2(r_{\max}/\delta)\rceil$, với $r_{\max}$ là một cận trên của độ dài dòng, chọn trước khi dựng bảng; $r\le r_{\max}$.

**Kết luận.**

- (a) Với xác suất ít nhất $1-\delta$, mọi phần tử đã xuất hiện trên dòng đồng thời thỏa $f_u\le\widehat f_u<f_u+\varepsilon r/\kappa$.
- (b) Khi biến cố ở (a) xảy ra, tập $\mathcal F$ gồm các phần tử đã xuất hiện có $\widehat f_u\ge r/\kappa$ là một lời giải của bài toán $(\varepsilon,\kappa)$-phần tử nặng (Định nghĩa 09.30).

**Điều kiện áp dụng.** Như Định lý 09.37.

**Phạm vi.** Hệ quả không nói cách liệt kê các phần tử đã xuất hiện mà không lưu chúng. Nếu dòng dài hơn $r_{\max}$, bảo đảm (a) không còn được chứng minh.
:::

::: proof
**Bước 1 (cận hợp).** Có $d\le r$ phần tử đã xuất hiện. Với mỗi phần tử, chứng minh Định lý 09.37 với $t=\lceil\log_2(r_{\max}/\delta)\rceil$ cho xác suất thất bại không quá $2^{-t}\le\delta/r_{\max}\le\delta/r$. Theo cận hợp, xác suất có ít nhất một phần tử thất bại không quá $d\cdot\delta/r\le\delta$.

**Bước 2 (phần tử nặng).** Nếu $f_u\ge r/\kappa$ thì $\widehat f_u\ge f_u\ge r/\kappa$, nên $u\in\mathcal F$; điều này đúng chắc chắn. Nếu $f_u<(1-\varepsilon)r/\kappa$ thì, khi biến cố ở (a) xảy ra, $\widehat f_u<f_u+\varepsilon r/\kappa<r/\kappa$, nên $u\notin\mathcal F$. $\square$
:::

Hệ quả 09.38(a) trả lời câu hỏi của UMass (trang chiếu 18) về $\delta$ để mọi phần tử cùng tốt với xác suất $99\%$: $\delta=0{,}01/r_{\max}$. Trong Ví dụ 09.12, hai hàm băm đã cố định, nên nhiễu của $\mathrm a$ là số quan sát được $Z_1=Z_2=3$. Bổ đề 09.36 nói về phép chọn ngẫu nhiên hàm băm: với $u=\mathrm a$, $\mathbb E[Z_j]\le(r-f_{\mathrm a})/m=10/3$, chặt hơn $r/m=5$ vì đã trừ tần suất của chính $\mathrm a$, và ngưỡng Markov là $2r/m=10$.

::: remark Nhận xét 09.39 (Vì sao lấy cực tiểu; quan hệ với Bloom filter và với Mục 2)
Mọi ô $A_j[h_j(u)]$ đều là ước lượng thừa (Bổ đề 09.35), nên ô nhỏ nhất gần $f_u$ nhất; trung bình hay trung vị của các ô không nhỏ hơn cực tiểu (UMass, trang chiếu 16).

Flajolet–Martin lấy trung vị vì sai số có hai phía (Định lý 09.10); Count-Min lấy cực tiểu vì sai số chỉ có một phía, như Bloom filter không bao giờ loại một khóa đã chèn (Định lý 08.25). Cả hai cùng dựa vào việc ô chỉ được tăng.
:::

::: remark Nhận xét 09.40 (Trong thực hành)
Khi tìm địa chỉ IP gửi nhiều yêu cầu (UMass, trang chiếu 9), địa chỉ có $\widehat f_u\ge r/\kappa$ vào danh sách nghi vấn, và Bổ đề 09.35 bảo đảm không phần tử nặng nào bị bỏ sót. Để liệt kê phần tử nặng, UMass (trang chiếu 19) giữ các phần tử có ước lượng ít nhất $i/\kappa$ tại bước $i$, chỉ $O(\kappa)$ phần tử, nhưng không chứng minh cơ chế này.
:::

::: exercise Bài tập 09.6 (Định cỡ Count-Min)
- (a) Chọn $m$, $t$ và số bộ đếm cho $\varepsilon=0{,}1$, $\kappa=100$, $\delta=0{,}01$. Sai số cho phép bằng bao nhiêu phần của $r$?
- (b) Dòng có tối đa $r_{\max}=10^9$ phần tử. Theo Hệ quả 09.38, cần bao nhiêu hàng để mọi phần tử đã xuất hiện cùng có sai số dưới $\varepsilon r/\kappa$ với xác suất $99\%$? Tổng số bộ đếm là bao nhiêu? So với một bảng tần suất chính xác cho $10^6$ phần tử phân biệt.
:::

::: hint
Dùng $m=\lceil2\kappa/\varepsilon\rceil$; ở (b) dùng $t=\lceil\log_2(r_{\max}/\delta)\rceil$ với $\delta=0{,}01$.
:::

::: solution
(a) $m=\lceil2\cdot100/0{,}1\rceil=2\,000$; $t=\lceil\log_2100\rceil=7$, vì $2^6=64<100\le128=2^7$. Bảng có $2\,000\cdot7=14\,000$ bộ đếm. Sai số cho phép là $\varepsilon r/\kappa=0{,}001\,r$.

(b) $t=\lceil\log_2(10^9/0{,}01)\rceil=\lceil\log_210^{11}\rceil=37$, vì $\log_210^{11}\approx36{,}54$. Bảng có $2\,000\cdot37=74\,000$ bộ đếm. Bảng tần suất chính xác cần $10^6$ bộ đếm cùng $10^6$ mã phần tử và tăng theo $d$; Count-Min không phụ thuộc $d$ nhưng có sai số tới $0{,}001r=10^6$.

**Kiểm tra lại.** $2^{37}\approx1{,}37\cdot10^{11}\ge10^{11}>2^{36}\approx6{,}9\cdot10^{10}$.
:::

Như vậy, Count-Min không bao giờ ước lượng thấp (Bổ đề 09.35), mỗi hàng có nhiễu kỳ vọng không quá $r/m$ (Bổ đề 09.36), và $t$ hàng độc lập đưa xác suất thừa quá $\varepsilon r/\kappa$ xuống dưới $\delta$ (Định lý 09.37), đủ để giải bài toán phần tử nặng (Hệ quả 09.38). Tuy nhiên, mọi đại lượng tới đây tính trên toàn dòng: một phần tử nặng cách đây một năm vẫn nặng hôm nay. Trong Mục 5, chúng ta hỏi về phần gần đây của dòng.

## 5. Đếm bit 1 trong cửa sổ bằng DGIM

Câu 4 của Ví dụ 09.1 hỏi số lần $\mathrm a$ xuất hiện trong 8 vị trí cuối. Thay mỗi $x_i$ bằng bit $\mathbf 1[x_i=\mathrm a]$, ta được dòng bit $1,0,0,0,0,1,0,0,1,0,0,0,1,1,0$, và câu hỏi thành số bit 1 trong 8 bit cuối, bằng 3.

MMDS (§4.6, tr.150) hỏi số bit 1 trong $k$ bit cuối với mọi $k\le N$. Chúng ta chứng minh rằng đáp số chính xác cần $N$ bit, rồi xây biểu diễn Datar–Gionis–Indyk–Motwani (DGIM) chỉ dùng $O(\log^2N)$ bit với sai số tương đối không quá 50%.

Trong Mục 5, $x_i\in\{0,1\}$ là bit ở vị trí $i$, $r$ là vị trí của bit mới nhất, cửa sổ là các vị trí $r-N+1,\ldots,r$, và $y_k$ là số bit 1 trong $k$ vị trí cuối $r-k+1,\ldots,r$.

<!-- note-topic-id: lec-09-topic-16 -->
### 5.1 Cận dưới $N$ bit cho lời giải chính xác

Một cách trực quan, nếu hai cửa sổ khác nhau lại cho cùng một trạng thái, thuật toán không thể trả lời đúng cho cả hai ở mọi truy vấn; với $2^N$ cửa sổ có thể, trạng thái phải có ít nhất $2^N$ giá trị. Ví dụ 09.13, theo MMDS, cho hai cặp cửa sổ có thể bị nhầm.

::: example Ví dụ 09.13 (Hai cửa sổ khác nhau)
**Dữ kiện.** Cửa sổ độ dài $N=4$, bit mới nhất bên phải (MMDS Ví dụ 4.10, tr.151).

**Cặp thứ nhất.** $\mathbf w=0101$ và $\mathbf w'=1010$ khác nhau ngay ở bit cuối, nên với $k=1$: $y_1(\mathbf w)=1$, $y_1(\mathbf w')=0$.

**Cặp thứ hai.** $\mathbf w=1001$ và $\mathbf w'=0101$ trùng hai bit cuối ($01$), khác ở bit thứ ba tính từ phải. Với $k=3$: ba bit cuối là $001$ và $101$, nên $y_3(\mathbf w)=1$, $y_3(\mathbf w')=2$.

**Diễn giải.** Một biểu diễn cho $\mathbf w$ và $\mathbf w'$ cùng trạng thái sẽ sai ở một trong hai cửa sổ với $k=3$. Thêm một bit 0 vào cả hai, cửa sổ thành $0010$ và $1010$, chỉ khác ở bit trái cùng, với tổng số bit 1 là 1 và 2.

Hai cửa sổ của mỗi cặp có cùng số bit 1 là 2, nên chỉ truy vấn hậu tố phân biệt được chúng.

**Kiểm tra lại.** $0010$ có một bit 1, $1010$ có hai.
:::

::: proposition Mệnh đề 09.41 (Đếm chính xác trong cửa sổ cần $N$ bit)
**Giả thiết.** Một thuật toán dòng một lượt tất định (Định nghĩa 08.1) đọc dòng bit, giữ trạng thái gồm ít hơn $N$ bit.

**Kết luận.**

- (a) Có một dòng và một $k\le N$ mà thuật toán trả sai $y_k$.
- (b) Kết luận (a) vẫn đúng khi thuật toán chỉ phải trả lời $k=N$, tức số bit 1 trong cả cửa sổ.

**Điều kiện áp dụng.** Phép trả lời chỉ đọc trạng thái; phép cập nhật là hàm của trạng thái và bit mới.

**Phạm vi.** Mệnh đề nói về lời giải chính xác; nó không cấm xấp xỉ với ít bộ nhớ.
:::

::: proof
**Bước 1 (hai cửa sổ cùng trạng thái).** Xét các dòng gồm đúng $N$ bit; mỗi dòng như vậy là một cửa sổ, và có $2^N$ cửa sổ khác nhau. Trạng thái ít hơn $N$ bit nhận ít hơn $2^N$ giá trị. Theo nguyên lý Dirichlet (nguyên lý chuồng bồ câu, pigeonhole principle), có hai cửa sổ $\mathbf w\ne\mathbf w'$ cho cùng một trạng thái.

**Bước 2 (phần (a)).** Gọi $k$ là vị trí, tính từ phải, của bit khác nhau đầu tiên giữa $\mathbf w$ và $\mathbf w'$; khi đó $k-1$ bit cuối của chúng trùng nhau và bit thứ $k$ khác nhau, nên $y_k(\mathbf w)$ và $y_k(\mathbf w')$ hơn kém nhau đúng 1. Thuật toán trả lời từ trạng thái, cùng cho $\mathbf w$ và $\mathbf w'$, nên cho cùng một số, và sai ở ít nhất một cửa sổ.

**Bước 3 (phần (b)).** Từ hai dòng $\mathbf w$ và $\mathbf w'$, đọc thêm cùng $N-k$ bit bất kỳ. Phép cập nhật chỉ phụ thuộc trạng thái và bit mới, nên hai dòng vẫn có cùng trạng thái sau mỗi bit. Sau $N-k$ bit, bit thứ $k$ cũ trở thành bit trái cùng của cửa sổ, các bit cũ hơn đã ra khỏi cửa sổ, còn $N-1$ bit còn lại của hai cửa sổ trùng nhau ($k-1$ bit cuối cũ và $N-k$ bit mới). Hai cửa sổ có tổng số bit 1 hơn kém nhau 1 nhưng cùng trạng thái, nên câu trả lời cho $k=N$ sai ở một trong hai. $\square$
:::

Chứng minh theo MMDS (§4.6.1, tr.151), cùng kiểu lập luận đếm của Nhận xét 09.4. Bỏ giả thiết "ít hơn $N$ bit" thì kết luận sai, vì giữ đủ $N$ bit cuối trả lời đúng mọi $k$.

<!-- note-topic-id: lec-09-topic-17 -->
### 5.2 Thùng, sáu quy tắc và bộ nhớ

Về mặt ý tưởng, tóm tắt các đoạn có độ dài tăng theo lũy thừa của 2 sai nhiều khi các bit 1 dồn vào một đoạn dài mà ta chỉ biết tổng (trang chiếu MMDS, Streams 1, tr.29–31); DGIM chọn các đoạn sao cho **số bit 1** mỗi đoạn là lũy thừa của 2 và không giảm về quá khứ (tr.32). Ví dụ 09.14 đọc trạng thái mà MMDS vẽ ở Hình 4.2.

::: example Ví dụ 09.14 (Trạng thái của MMDS Hình 4.2)
**Dữ kiện.** Hai mươi lăm bit cuối của dòng, từ cũ sang mới, ở các vị trí $r-24,\ldots,r$ (MMDS Hình 4.2, tr.152):
$$
1\,0\,1\,1\,0\,1\,1\,0\,0\,0\,1\,0\,1\,1\,1\,0\,1\,1\,0\,0\,1\,0\,1\,1\,0 .
$$
Các bit 1 nằm ở vị trí $r-24,\ r-22,\ r-21,\ r-19,\ r-18,\ r-14,\ r-12,\ r-11,\ r-10,\ r-8,\ r-7,\ r-4,\ r-2,\ r-1$.

**Các đoạn của hình.** Đọc từ mới về cũ:

| Đoạn | Các bit 1 trong đoạn | Số bit 1 | Vị trí bit 1 mới nhất |
|---|---|---:|---|
| 1 | $r-1$ | 1 | $r-1$ |
| 2 | $r-2$ | 1 | $r-2$ |
| 3 | $r-7,\ r-4$ | 2 | $r-4$ |
| 4 | $r-12,\ r-11,\ r-10,\ r-8$ | 4 | $r-8$ |
| 5 | $r-21,\ r-19,\ r-18,\ r-14$ | 4 | $r-14$ |
| 6 | $r-24,\ r-22$ và phần bên trái không vẽ | 8 | $r-22$ |

Bit 0 ở $r$, ở $r-3$ và ở $r-13$ nằm giữa hai đoạn. Đoạn 3 phủ bốn vị trí $r-7,\ldots,r-4$ nhưng chỉ chứa hai bit 1 (MMDS Ví dụ 4.11, tr.153).

**Kiểm tra lại.** Phần nhìn thấy có 14 bit 1, gồm $1+1+2+4+4=12$ bit của năm đoạn đầu và 2 bit thấy được của đoạn 6.
:::

Nhãn "có ít nhất một đoạn cỡ 8" của MMDS nói về số đoạn: phần không vẽ có thể chứa thêm một đoạn cỡ 8, và đoạn 6 có 6 bit 1 bên trái phần hình.

![Hai mươi lăm ô bit từ cũ bên trái sang mới bên phải, dãy 1011011000101110110010110, vị trí r trừ 24 tới r. Sáu khung bao các thùng, tam giác đánh dấu mốc phải: khung cỡ 8, mốc r trừ 22, bị cắt ở mép trái; hai khung cỡ 4, mốc r trừ 14 và r trừ 8; khung cỡ 2, mốc r trừ 4, phủ bốn ô 1001; hai khung cỡ 1, mốc r trừ 2 và r trừ 1. Bit 0 ở r trừ 13, r trừ 3 và r nằm ngoài mọi khung. Đường đứng nét đứt trước r trừ 9 đánh dấu mười vị trí cuối.](img/lec-09/dgim-trang-thai.svg)

Hình vẽ lại MMDS Hình 4.2 với mốc thời gian; cỡ ghi trên khung là số bit 1, không phải số ô, và đi từ phải sang trái cỡ là $1,1,2,4,4,8$, không giảm.

::: definition Định nghĩa 09.42 (Thùng và biểu diễn DGIM)
Cho cửa sổ độ dài $N$ và vị trí hiện tại $r$; vị trí $i$ còn trong cửa sổ khi $r-N+1\le i\le r$.

- Một **thùng** (bucket) $b$ là một đoạn vị trí liên tiếp của dòng kết thúc ở một bit 1. **Mốc phải** $\tau_b$ là vị trí cuối của đoạn; **kích thước** $\lvert b\rvert$ là số bit 1 trong đoạn. Thùng được lưu bằng hai số: $\tau_b\bmod N$ và $\log_2\lvert b\rvert$.
- Một **biểu diễn DGIM** của cửa sổ là một tập thùng có mốc phải nằm trong cửa sổ và thỏa sáu quy tắc (MMDS §4.6.2, tr.152):
  1. mốc phải của mỗi thùng là một vị trí có bit 1;
  2. mọi vị trí có bit 1 trong cửa sổ thuộc một thùng;
  3. không vị trí nào thuộc hai thùng;
  4. mỗi kích thước có một hoặc hai thùng, từ kích thước 1 tới một kích thước lớn nhất;
  5. mọi kích thước là lũy thừa của 2;
  6. đi về quá khứ, kích thước các thùng không giảm.
:::

Thùng là một đoạn liên tục, có thể chứa bit 0 bên trong, và giữa hai thùng có thể có bit 0 không thuộc thùng nào. Thùng ở đây khác thùng băm của Bài 06, vốn là tập các khóa cùng giá trị băm (MMDS chú thích 5, tr.152). Ví dụ 09.14 là một biểu diễn DGIM với các kích thước $1,1,2,4,4,8$.

::: remark Nhận xét 09.43 (Các thùng phủ các bit 1 thành nhóm liên tiếp)
Trong một biểu diễn DGIM, giữa hai thùng liền nhau theo thời gian không có bit 1 nào. Thật vậy, giả sử có một bit 1 như vậy. Nó đứng sau mốc phải của thùng cũ hơn, mà mốc này nằm trong cửa sổ, nên bit đó cũng nằm trong cửa sổ và theo quy tắc 2 thuộc một thùng nào đó. Theo quy tắc 3 và vì mỗi thùng là một đoạn liên tục, thùng này nằm trọn giữa hai thùng đã cho, trái với giả thiết hai thùng liền nhau.

Do đó các thùng chia các bit 1 gần đây thành những nhóm liên tiếp theo thời gian, và chỉ thùng cũ nhất có thể vắt qua biên trái của cửa sổ.
:::

Hai biểu diễn sau không hợp lệ: ba thùng cỡ 1 (vi phạm quy tắc 4), và thùng cỡ 2 đứng mới hơn một thùng cỡ 1 (vi phạm quy tắc 6).

::: proposition Mệnh đề 09.44 (Số thùng và bộ nhớ)
**Giả thiết.** Một biểu diễn DGIM của cửa sổ độ dài $N\ge1$.

**Kết luận.** Kích thước lớn nhất $2^J$ thỏa $J\le\lfloor\log_2N\rfloor$. Có nhiều nhất $2(\lfloor\log_2N\rfloor+1)$ thùng, mỗi thùng lưu bằng $\lceil\log_2N\rceil+\lceil\log_2(\lfloor\log_2N\rfloor+1)\rceil$ bit, nên tổng bộ nhớ là $O(\log^2N)$ bit, cộng $\lceil\log_2N\rceil$ bit cho $r\bmod N$.

**Điều kiện áp dụng.** Chỉ dùng sáu quy tắc và điều kiện mốc phải trong cửa sổ.

**Phạm vi.** Đếm bit của trạng thái, không nói về thời gian xử lý.
:::

::: proof
**Bước 1 (các thùng nhỏ nằm trọn trong cửa sổ).** Gọi $b$ là một thùng cỡ lớn nhất $2^J$. Theo quy tắc 4, mỗi kích thước $2^0,\ldots,2^{J-1}$ có ít nhất một thùng; theo quy tắc 6, các thùng này mới hơn $b$, nên mọi vị trí của chúng đứng sau $\tau_b$, mà $\tau_b$ nằm trong cửa sổ. Vậy chúng nằm trọn trong cửa sổ và chứa ít nhất $1+2+\cdots+2^{J-1}=2^J-1$ bit 1 (tổng cấp số nhân).

**Bước 2 (kích thước lớn nhất).** Theo quy tắc 1 và 3, $\tau_b$ là một bit 1 trong cửa sổ không thuộc các thùng ở Bước 1. Cửa sổ vì thế có ít nhất $2^J-1+1=2^J$ bit 1, mà cửa sổ chỉ có $N$ vị trí. Do đó $2^J\le N$, tức $J\le\lfloor\log_2N\rfloor$.

**Bước 3 (số thùng).** Các kích thước là $2^0,\ldots,2^J$ (quy tắc 4, 5), tức nhiều nhất $\lfloor\log_2N\rfloor+1$ kích thước, mỗi kích thước nhiều nhất hai thùng.

**Bước 4 (bit).** Mốc phải lưu theo modulo $N$ cần $\lceil\log_2N\rceil$ bit; cùng với $r\bmod N$, nó xác định vị trí thật trong cửa sổ, vì cửa sổ có đúng $N$ vị trí liên tiếp. Số mũ $\log_2\lvert b\rvert\in\{0,\ldots,\lfloor\log_2N\rfloor\}$ cần $\lceil\log_2(\lfloor\log_2N\rfloor+1)\rceil$ bit. Nhân với số thùng ở Bước 3 được $O(\log N)\cdot O(\log N)=O(\log^2N)$. $\square$
:::

Bước 1–2 xử lý cả trường hợp thùng cũ nhất vắt qua biên trái. Với $N=10^9$: $\lfloor\log_2N\rfloor=29$, nhiều nhất 60 thùng, mỗi thùng $30+5=35$ bit, tổng $2\,100$ bit cộng 30 bit cho $r\bmod N$, khoảng 266 byte so với 125 MB. Bỏ quy tắc 4 thì số thùng không còn bị chặn bởi $O(\log N)$: $N$ thùng cỡ 1 thỏa mọi quy tắc khác.

<!-- note-topic-id: lec-09-topic-18 -->
### 5.3 Truy vấn và cận sai số 50%

Biểu diễn chỉ giữ mốc phải và kích thước, nên một thùng vắt qua biên của $k$ vị trí cuối chỉ cho biết một phần bit 1 của nó nằm trong hậu tố. Về mặt ý tưởng, mọi thùng mới hơn thùng chứa biên được cộng đủ, còn thùng chứa biên chỉ được đoán một nửa; quy tắc 4 bảo đảm phần đã cộng đủ lớn để lỗi đoán không vượt một nửa đáp số. Ví dụ 09.15, theo MMDS, cho thấy cách làm.

::: example Ví dụ 09.15 (Mười vị trí cuối của Hình 4.2)
**Dữ kiện.** Trạng thái của Ví dụ 09.14: các thùng (kích thước, mốc phải) là $(1,r-1)$, $(1,r-2)$, $(2,r-4)$, $(4,r-8)$, $(4,r-14)$, $(8,r-22)$. Truy vấn $k=10$, tức các vị trí $r-9,\ldots,r$ (MMDS Ví dụ 4.12, tr.153–154).

**Tính.** Thùng cũ nhất có mốc phải trong mười vị trí cuối là thùng $(4,r-8)$. Ba thùng mới hơn nó nằm trọn trong hậu tố, góp $1+1+2=4$. Thùng $(4,r-8)$ chỉ có một phần trong hậu tố; ta cộng một nửa kích thước của nó. Ước lượng là $4+4/2=6$. Thùng $(4,r-14)$ có mốc phải ngoài hậu tố, nên không góp.

**Kiểm tra lại.** Mười bit cuối là $0110010110$, có 5 bit 1, ở $r-8$, $r-7$, $r-4$, $r-2$, $r-1$. Ước lượng thừa 1, sai số tương đối $1/5$.
:::

::: algorithm Thuật toán 09.45 (Truy vấn DGIM)
**Đầu vào.** Biểu diễn DGIM của cửa sổ; $k$ với $1\le k\le N$.

**Đầu ra.** Ước lượng $\widehat y_k$ của $y_k$.

**Giả thiết.** Biểu diễn thỏa Định nghĩa 09.42.

1. Gọi $b^*$ là thùng cũ nhất có $\tau_b\ge r-k+1$. Nếu không có thùng nào như vậy, trả $\widehat y_k=0$.
2. Đặt $T$ là tổng kích thước của các thùng mới hơn $b^*$.
3. Trả $\widehat y_k=T+\lvert b^*\rvert/2$.

**Dừng.** Sau một lượt qua các thùng.

**Trường hợp biên.** Với $k=N$ và $b^*$ là thùng cũ nhất vắt qua biên trái, thuật toán vẫn chỉ dùng mốc phải của $b^*$.

**Chi phí.** Mô hình: mỗi phép đọc và cộng tốn $O(1)$; trường hợp xấu nhất. Bước 1 và 2 duyệt nhiều nhất $2(\lfloor\log_2N\rfloor+1)$ thùng (Mệnh đề 09.44), mỗi thùng $O(1)$ phép; bước 3 tốn $O(1)$. Tổng $O(\log N)$ mỗi truy vấn.
:::

Ký hiệu $\mu$ là số mũ với $\lvert b^*\rvert=2^\mu$. Ví dụ 09.15 là trường hợp $b^*=(4,r-8)$, $T=4$, $\mu=2$.

::: theorem Định lý 09.46 (Cận sai số 50%)
**Giả thiết.** Biểu diễn DGIM thỏa Định nghĩa 09.42; $1\le k\le N$.

**Kết luận.** Nếu $y_k=0$ thì $\widehat y_k=0$. Nếu $y_k>0$ thì
$$
\tfrac12\,y_k\le\widehat y_k\le\tfrac32\,y_k .
$$

**Điều kiện áp dụng.** Tất định: đúng cho mọi dòng và mọi $k$.

**Phạm vi.** Cận là sai số tương đối. Sai số tuyệt đối có thể lớn khi $y_k$ lớn.
:::

::: proof
**Bước 1 (cấu trúc của hậu tố).** Các thùng mới hơn $b^*$ có mọi vị trí đứng sau $\tau_{b^*}\ge r-k+1$, nên nằm trọn trong hậu tố. Các thùng cũ hơn $b^*$ có mốc phải trước $r-k+1$, nên không có vị trí nào trong hậu tố. Hậu tố nằm trong cửa sổ vì $k\le N$, nên mọi bit 1 của nó thuộc một thùng (quy tắc 2). Do đó
$$
y_k=T+\pi,
$$
trong đó $\pi$ là số bit 1 của $b^*$ nằm trong hậu tố. Theo quy tắc 1, $\tau_{b^*}$ là một bit 1 trong hậu tố, nên $1\le\pi\le2^\mu$.

**Bước 2 (chặn dưới $T$).** Theo quy tắc 4, mỗi kích thước $2^0,\ldots,2^{\mu-1}$ có ít nhất một thùng; theo quy tắc 6, các thùng này mới hơn $b^*$. Do đó $T\ge1+2+\cdots+2^{\mu-1}=2^\mu-1$, và theo Bước 1, $y_k\ge2^\mu-1+1=2^\mu$.

**Bước 3 (sai số tuyệt đối).** $\widehat y_k-y_k=2^{\mu-1}-\pi$. Vì $1\le\pi\le2^\mu$,
$$
-2^{\mu-1}\le\widehat y_k-y_k\le2^{\mu-1}-1 .
$$
Trường hợp ước lượng thấp xấu nhất là $\pi=2^\mu$, mọi bit 1 của $b^*$ nằm trong hậu tố; trường hợp ước lượng cao xấu nhất là $\pi=1$, chỉ mốc phải của $b^*$ nằm trong hậu tố. Đây là hai trường hợp của MMDS (§4.6.4, tr.154).

**Bước 4 (sai số tương đối).** Theo Bước 2 và Bước 3, $\lvert\widehat y_k-y_k\rvert\le2^{\mu-1}=\frac12\cdot2^\mu\le\frac12y_k$, tương đương $\frac12y_k\le\widehat y_k\le\frac32y_k$.

**Bước 5 (biên $y_k=0$).** Nếu có thùng với mốc phải trong hậu tố thì theo quy tắc 1 hậu tố có bit 1. Phản đảo: $y_k=0$ thì không thùng nào có mốc phải trong hậu tố, và bước 1 của Thuật toán 09.45 trả 0. Ngược lại, nếu $y_k>0$, bit 1 trong hậu tố thuộc một thùng có mốc phải ở sau nó, cũng trong hậu tố, nên $b^*$ tồn tại. $\square$
:::

DGIM không bao giờ sai quá một nửa số bit 1 thật trong hậu tố được hỏi, với mọi $k\le N$, và trả đúng 0 khi hậu tố không có bit 1. Số hạng "+1" ở Bước 2, bit mốc phải của chính $b^*$, giữ cho tỷ số không vượt $1/2$.

So với Mệnh đề 09.41, Định lý 09.46 bỏ yêu cầu đáp số chính xác và đổi lại sai số tương đối 50%; bộ nhớ giảm từ $N$ bit xuống $O(\log^2N)$ bit. Khác với Định lý 09.10 và 09.37, bảo đảm này tất định, đúng với mọi dòng và không cần hàm băm.

Trong thực hành, mỗi URL giữ một danh sách thùng, mỗi truy vấn tốn $O(\log N)$ phép (Thuật toán 09.45), và số lượt thật trong $N$ lượt cuối nằm giữa $2/3$ và $2$ lần số mà DGIM trả.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ quy tắc 4 (mỗi kích thước nhỏ hơn có mặt): trạng thái chỉ gồm một thùng cỡ 8 và một thùng cỡ 1 mới hơn. Với hậu tố chứa thùng cỡ 1 và đúng mốc phải của thùng cỡ 8, $y_k=2$ nhưng $\widehat y_k=1+4=5$, thừa $150\%$.
- Bỏ quy tắc 1 (mốc phải là bit 1): một thùng cỡ 2 có mốc phải là bit 0 trong hậu tố, còn cả hai bit 1 của nó nằm ngoài hậu tố. Khi đó $y_k=0$ nhưng $\widehat y_k=1$.

Bước 1 và Bước 5 dùng quy tắc 1, 2, 3 và điều kiện mốc phải trong cửa sổ; Bước 2 dùng quy tắc 4, 5 và 6.

<!-- note-topic-id: lec-09-topic-19 -->
### 5.4 Cập nhật và gộp dây chuyền

Định lý 09.46 giả sử biểu diễn thỏa sáu quy tắc, nên phép cập nhật khi một bit mới đến phải giữ chúng. Một cách trực quan, bit 1 mới là một thùng cỡ 1, và khi một kích thước có ba thùng, hai thùng cũ nhất hợp thành một thùng cỡ gấp đôi, giống phép nhớ khi cộng 1 vào một số nhị phân. Ví dụ 09.16, theo MMDS, thêm một bit 1 vào trạng thái của Hình 4.2.

::: example Ví dụ 09.16 (Một bit 1 mới trên Hình 4.2)
**Dữ kiện.** Các thùng (kích thước, mốc phải) $(8,r-22)$, $(4,r-14)$, $(4,r-8)$, $(2,r-4)$, $(1,r-2)$, $(1,r-1)$ của Ví dụ 09.14. Bit 1 đến ở vị trí $r+1$; thùng cũ nhất chưa ra khỏi cửa sổ (MMDS Ví dụ 4.13, tr.155).

**Tính.**

1. Tạo thùng $(1,r+1)$. Có ba thùng cỡ 1: mốc $r-2$, $r-1$, $r+1$.
2. Gộp hai thùng cỡ 1 cũ nhất, mốc $r-2$ và $r-1$, thành thùng $(2,r-1)$; mốc phải là mốc của thùng mới hơn trong hai.
3. Có hai thùng cỡ 2, mốc $r-4$ và $r-1$; quy tắc 4 thỏa, dừng.

Trạng thái mới, viết theo vị trí hiện tại $r'=r+1$: $(8,r'-23)$, $(4,r'-15)$, $(4,r'-9)$, $(2,r'-5)$, $(2,r'-2)$, $(1,r')$, đúng MMDS Hình 4.3.

**Kiểm tra lại.** Số bit 1 của phần nhìn thấy tăng từ 14 lên 15; tổng kích thước các thùng ngoài thùng cỡ 8 tăng từ 12 lên 13.
:::

![Hai dải thùng, cũ bên trái, mới bên phải. Dải trên, trước khi gộp: cỡ 8, 4, 4, 2, 1, 1, 1 với mốc r trừ 22, r trừ 14, r trừ 8, r trừ 4, r trừ 2, r trừ 1, r cộng 1; khung cuối là thùng mới của bit 1 ở r cộng 1. Hai khung cỡ 1 mốc r trừ 2 và r trừ 1 viền nét đứt, có nhãn gộp hai thùng cỡ 1 cũ nhất và mũi tên xuống khung cỡ 2 mốc r trừ 1. Dải dưới, sau cập nhật: cỡ 8, 4, 4, 2, 2, 1 với mốc r trừ 22, r trừ 14, r trừ 8, r trừ 4, r trừ 1, r cộng 1. Chú thích: kích thước từ mới về cũ không giảm, mỗi kích thước có một hoặc hai thùng.](img/lec-09/dgim-cap-nhat.svg)

Trên hình, chỉ hai thùng cỡ 1 cũ nhất đổi; thùng cỡ 2 vừa tạo đứng giữa thùng cỡ 2 cũ và thùng cỡ 1 mới, nên kích thước vẫn không giảm về quá khứ.

::: algorithm Thuật toán 09.47 (Cập nhật DGIM)
**Đầu vào.** Biểu diễn DGIM sau vị trí $r-1$; bit mới $x_r$.

**Đầu ra.** Biểu diễn DGIM sau vị trí $r$.

**Giả thiết.** Biểu diễn đầu vào thỏa Định nghĩa 09.42 với cửa sổ $r-N,\ldots,r-1$.

1. **Hết hạn.** Nếu thùng cũ nhất có $\tau_b\le r-N$, xóa nó.
2. Nếu $x_r=0$: dừng.
3. Nếu $x_r=1$: tạo thùng $(1,r)$ và đặt $\chi\gets0$.
4. **Gộp.** Trong khi có ba thùng cỡ $2^\chi$: thay hai thùng cũ nhất trong ba bằng một thùng cỡ $2^{\chi+1}$, với mốc phải là mốc của thùng mới hơn trong hai; đặt $\chi\gets\chi+1$.

```text
CẬP-NHẬT-DGIM(các thùng; r, x_r, N)
    nếu thùng cũ nhất có τ ≤ r − N: xóa nó
    nếu x_r = 0: dừng
    thêm thùng (cỡ 1, mốc r);  χ ← 0
    trong khi có ba thùng cỡ 2^χ:
        b', b'' ← hai thùng cỡ 2^χ cũ nhất (b' cũ hơn)
        thay b', b'' bằng thùng (cỡ 2^(χ+1), mốc τ_b'')
        χ ← χ + 1
```

**Dừng.** Mỗi lượt gộp làm giảm số thùng đi 1, nên vòng lặp dừng; Mệnh đề 09.49 cho số lượt cụ thể.

**Trường hợp biên.** Chỉ thùng cũ nhất có thể hết hạn, và nhiều nhất một thùng mỗi bước, vì các mốc phải khác nhau và trước bước $r$ đều $\ge r-N$. Dây chuyền gộp có thể lan tới kích thước lớn nhất.

**Chi phí.** Mô hình: các thùng giữ trong danh sách theo thời gian, mỗi phép trên một thùng tốn $O(1)$.

| Bước | Số lần mỗi bit | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| hết hạn (bước 1) | 1 | $O(1)$ | $O(1)$ |
| tạo thùng (bước 3) | tối đa 1 | $O(1)$ | $O(1)$ |
| gộp (bước 4) | tối đa $\lfloor\log_2N\rfloor+1$; trung bình tối đa 1 mỗi bit 1 | $O(1)$ | xấu nhất $O(\log N)$, khấu hao $O(1)$ |

Hai cận của hàng cuối là Mệnh đề 09.49.
:::

MMDS (§4.6.5, tr.154) gộp hai thùng **cũ nhất** ở bước 4. Gộp hai thùng mới nhất sẽ phá quy tắc 6: với các kích thước từ cũ sang mới $2,2,2,1$, gộp hai thùng cỡ 2 mới nhất cho $2,4,1$, và đi về quá khứ kích thước giảm từ 4 xuống 2.

::: theorem Định lý 09.48 (Tính đúng của cập nhật DGIM)
**Giả thiết.** Biểu diễn trước bước $r$ thỏa Định nghĩa 09.42 với cửa sổ $r-N,\ldots,r-1$.

**Kết luận.** Thuật toán 09.47 dừng và trả một biểu diễn thỏa Định nghĩa 09.42 với cửa sổ $r-N+1,\ldots,r$.

**Điều kiện áp dụng.** Mọi dòng bit; tất định.

**Phạm vi.** Định lý nói về sáu quy tắc; cận sai số khi đó do Định lý 09.46 cho.
:::

::: proof
Chứng minh đi qua ba phần của thuật toán, theo khuôn khởi tạo, duy trì và kết thúc của bất biến vòng lặp.

**Bước 1 (hết hạn).** Mọi mốc phải trước bước $r$ đều $\ge r-N$, và chúng khác nhau (quy tắc 1, 3), nên nhiều nhất một thùng có $\tau_b=r-N$, và đó là thùng cũ nhất. Mọi bit 1 của nó nằm ở vị trí $\le r-N$, ngoài cửa sổ mới, nên xóa nó không phá quy tắc 2. Thùng cũ nhất có kích thước lớn nhất (quy tắc 6); nếu nó là thùng duy nhất cỡ đó, kích thước lớn nhất giảm một bậc và các kích thước nhỏ hơn vẫn có một hoặc hai thùng, nên quy tắc 4 giữ. Quy tắc 1, 3, 5, 6 không bị ảnh hưởng khi xóa một thùng. Mọi mốc phải còn lại $\ge r-N+1$.

**Bước 2 (bit 0).** Vị trí mới không có bit 1, nên quy tắc 2 giữ; các quy tắc khác không đổi.

**Bước 3 (bit 1, khởi tạo vòng gộp).** Thùng $(1,r)$ thỏa quy tắc 1 và 5, phủ bit 1 mới (quy tắc 2), không chung vị trí với thùng nào (quy tắc 3), và là thùng mới nhất với kích thước nhỏ nhất (quy tắc 6). Xét bất biến $\mathcal I_\chi$ tại đầu mỗi lượt kiểm của vòng gộp: quy tắc 1, 2, 3, 5, 6 thỏa; mỗi kích thước $2^i$ với $i<\chi$ có một hoặc hai thùng; kích thước $2^\chi$ có một, hai hoặc ba thùng; các kích thước $2^i$ với $i>\chi$ có số thùng như sau Bước 1. $\mathcal I_0$ đúng: chỉ kích thước 1 có thể đã tăng lên ba thùng.

**Bước 4 (duy trì).** Giả sử $\mathcal I_\chi$ đúng và kích thước $2^\chi$ có ba thùng. Theo quy tắc 6, giữa hai thùng cỡ $2^\chi$ không có thùng cỡ khác, nên ba thùng này liền nhau theo thời gian; gọi chúng là $b'$, $b''$, $b'''$ từ cũ sang mới. Thùng gộp là đoạn vị trí liên tục từ vị trí đầu của $b'$ tới $\tau_{b''}$, gồm cả các bit 0 nằm giữa hai thùng; theo Nhận xét 09.43, giữa $b'$ và $b''$ không có bit 1 nào, nên đoạn này chứa đúng $2^{\chi+1}$ bit 1, với bit mới nhất ở $\tau_{b''}$.

Thùng gộp thỏa quy tắc 1 (mốc $\tau_{b''}$ là bit 1), quy tắc 5, và giữ nguyên tập bit 1 được phủ (quy tắc 2, 3). Về quy tắc 6: mọi thùng cũ hơn $b'$ có kích thước $\ge2^\chi$ và không phải một trong ba thùng, nên có kích thước $\ge2^{\chi+1}$; thùng gộp mới hơn chúng và cũ hơn $b'''$ cùng các thùng nhỏ hơn.

Sau lượt gộp, kích thước $2^\chi$ còn một thùng và kích thước $2^{\chi+1}$ tăng thêm một thùng, từ 0, 1 hoặc 2 lên 1, 2 hoặc 3. Do đó $\mathcal I_{\chi+1}$ đúng.

**Bước 5 (kết thúc).** Vòng lặp dừng khi kích thước $2^\chi$ có một hoặc hai thùng. Khi đó mọi kích thước $2^i$ với $i\le\chi$ có một hoặc hai thùng theo $\mathcal I_\chi$, và các kích thước lớn hơn giữ số thùng như sau Bước 1: một hoặc hai cho mọi kích thước tới kích thước lớn nhất, 0 cho các kích thước lớn hơn; quy tắc 4 thỏa. Vòng lặp chắc chắn dừng vì mỗi lượt giảm số thùng đi 1. Mọi mốc phải nằm trong cửa sổ mới, nên biểu diễn thỏa Định nghĩa 09.42. $\square$
:::

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "gộp hai thùng cũ nhất" (thay bằng hai thùng mới nhất): trạng thái $2,2,2,1$ thành $2,4,1$, phá quy tắc 6.
- Bỏ bước hết hạn: sau $N$ bit 0, thùng cũ nhất còn mốc phải ngoài cửa sổ, trái Định nghĩa 09.42, và Mệnh đề 09.44 không còn chặn được số thùng.

Bước 1 dùng quy tắc 1, 3 và 6; Bước 4 dùng quy tắc 6 và Nhận xét 09.43.

Định lý 09.48 là điều kiện để Mệnh đề 09.44 và Định lý 09.46 áp dụng được sau mọi bước: hai kết quả đó giả sử sáu quy tắc, còn Định lý 09.48 chứng minh phép cập nhật giữ chúng.

::: proposition Mệnh đề 09.49 (Chi phí cập nhật)
**Giả thiết.** Thuật toán 09.47 chạy từ trạng thái rỗng trên dòng $x_1,\ldots,x_r$; các thùng giữ trong danh sách theo thời gian.

**Kết luận.**

- (a) Một bit gây nhiều nhất $\lfloor\log_2N\rfloor+1$ lượt gộp, nên xử lý một bit tốn $O(\log N)$ phép trong trường hợp xấu nhất.
- (b) Tổng số lượt gộp sau $r$ bit không vượt số bit 1 trong $x_1,\ldots,x_r$; do đó chi phí khấu hao (amortized cost) là nhiều nhất một lượt gộp cho mỗi bit 1.

**Điều kiện áp dụng.** Tất định.

**Phạm vi.** (b) là cận cho tổng tính từ trạng thái rỗng, không cho từng bit hay từng đoạn.
:::

::: proof
**Bước 1 (phần (a)).** Một lượt gộp ở mức $\chi$ cần ba thùng cỡ $2^\chi$, trong đó ít nhất hai thùng có từ trạng thái trước bước $r$, vì lượt gộp ở mức thấp hơn chỉ tạo một thùng mới ở mức kế tiếp. Trạng thái trước thỏa Định nghĩa 09.42 (Định lý 09.48), nên theo Mệnh đề 09.44 mọi kích thước của nó $\le2^{\lfloor\log_2N\rfloor}$. Vậy các mức gộp là $\chi\in\{0,\ldots,\lfloor\log_2N\rfloor\}$, mỗi mức nhiều nhất một lượt.

**Bước 2 (phần (b), đếm số thùng).** Mỗi bit 1 tạo đúng một thùng; mỗi lượt gộp giảm số thùng đi 1; mỗi lần hết hạn giảm số thùng đi 1; bit 0 không đổi số thùng. Sau $r$ bit, số thùng bằng số bit 1 đã đến trừ số lượt gộp trừ số lần hết hạn, và số thùng không âm. Vậy số lượt gộp không vượt số bit 1 đã đến. $\square$
:::

MMDS (§4.6.5, tr.155) nêu cận $O(\log N)$ cho một bit. Phần (b) là phân tích khấu hao theo phương pháp thế năng (potential method) của CLRS 4e, Chương 16, với thế năng là số thùng: chi phí khấu hao của một bit, bằng số lượt gộp cộng mức tăng thế năng, là 1 trừ số thùng hết hạn (không quá 1) cho bit 1 và không dương cho bit 0; thế năng ban đầu bằng 0 và luôn không âm.

<!-- note-topic-id: lec-09-topic-20 -->
### 5.5 Mở rộng, nhầm lẫn và thực hành

::: remark Nhận xét 09.50 (Đọc thêm: giảm sai số và tổng các số nguyên)
MMDS cho mỗi kích thước từ $\omega-1$ đến $\omega$ thùng, $\omega>2$, và lập luận rằng sai số tương đối khi đó không quá $1/(\omega-1)$ (§4.6.6, tr.155–156); tổng các số nguyên dương được đếm bằng một biểu diễn DGIM cho mỗi vị trí bit, còn khi có cả số âm, sai số tương đối không bị chặn (§4.6.7, tr.156–157).
:::

::: remark Nhận xét 09.51 (Trong thực hành và nhầm lẫn thường gặp)
Mỗi biểu diễn DGIM giữ thêm $r\bmod N$ để đổi mốc lưu về vị trí thật (MMDS tr.152). Nhầm lẫn thường gặp:

- thùng là đoạn liên tục có thể chứa bit 0, và kích thước là số bit 1, không phải số vị trí (đoạn 3 của Ví dụ 09.14);
- bộ nhớ là $O(\log^2N)$ bit: $O(\log N)$ thùng, mỗi thùng $O(\log N)$ bit;
- phép gộp chọn hai thùng cũ nhất; chọn hai thùng mới nhất phá quy tắc 6.
:::

::: exercise Bài tập 09.7 (Hai bit 1 liên tiếp)
Một biểu diễn DGIM có các thùng (kích thước, mốc phải), từ cũ sang mới: $(4,r-9)$, $(2,r-6)$, $(2,r-3)$, $(1,r-1)$; cửa sổ đủ dài để không thùng nào hết hạn. Bit 1 đến ở vị trí $r+1$ rồi $r+2$. Ghi trạng thái sau mỗi bit, các lượt gộp, và kiểm sáu quy tắc. So số lượt gộp với số bit 1 mới bằng phép đếm số thùng ở Bước 2 của chứng minh Mệnh đề 09.49.
:::

::: hint
Sau bit thứ nhất có hai thùng cỡ 1. Sau bit thứ hai, dây chuyền gộp đi qua hai mức.
:::

::: solution
**Bit 1 ở $r+1$.** Tạo $(1,r+1)$; có hai thùng cỡ 1, không gộp. Trạng thái: $(4,r-9)$, $(2,r-6)$, $(2,r-3)$, $(1,r-1)$, $(1,r+1)$.

**Bit 1 ở $r+2$.** Tạo $(1,r+2)$; ba thùng cỡ 1 có mốc $r-1$, $r+1$, $r+2$. Gộp hai thùng cũ nhất thành $(2,r+1)$. Nay ba thùng cỡ 2 có mốc $r-6$, $r-3$, $r+1$; gộp hai thùng cũ nhất thành $(4,r-3)$. Có hai thùng cỡ 4, dừng. Trạng thái: $(4,r-9)$, $(4,r-3)$, $(2,r+1)$, $(1,r+2)$.

**Kiểm sáu quy tắc.** Mốc phải là bit 1 (quy tắc 1); gộp chỉ hợp hai nhóm liền nhau nên không bit 1 nào bị bỏ hay phủ hai lần (quy tắc 2, 3); kích thước 1, 2, 4 có 1, 1, 2 thùng (quy tắc 4, 5); từ mới về cũ là $1,2,4,4$ (quy tắc 6).

**Chi phí.** Không có thùng hết hạn, nên số lượt gộp bằng số bit 1 mới trừ số thùng tăng thêm: $2-(4-4)=2$, cả hai lượt do bit thứ hai. Mệnh đề 09.49(b) không áp trực tiếp cho đoạn này, vì đoạn không bắt đầu từ trạng thái rỗng; với trạng thái đầu khác, một bit 1 có thể gây nhiều lượt gộp hơn số bit 1 mới.

**Kiểm tra lại.** Tổng kích thước tăng từ $4+2+2+1=9$ lên $4+4+2+1=11$, đúng hai bit 1 mới.
:::

Như vậy, đáp số chính xác cho câu hỏi cửa sổ cần $N$ bit (Mệnh đề 09.41), còn biểu diễn DGIM dùng $O(\log^2N)$ bit (Mệnh đề 09.44), trả lời mọi $k\le N$ với sai số tương đối không quá 50% (Định lý 09.46) và được duy trì đúng bằng phép gộp dây chuyền (Định lý 09.48) với chi phí khấu hao một lượt gộp cho mỗi bit 1 (Mệnh đề 09.49). Tuy nhiên, câu hỏi thứ năm của Ví dụ 09.1 cần một biểu diễn cho mỗi phần tử, và cửa sổ trượt coi vị trí $r-N+1$ quan trọng như vị trí mới nhất còn vị trí $r-N$ không đáng kể. Trong Mục 6, chúng ta thay biên của cửa sổ bằng trọng số giảm theo tuổi.

## 6. Cửa sổ suy giảm mũ và phần tử phổ biến

MMDS (§4.7.1, tr.157–158) xét dòng vé xem phim bán trên toàn thế giới và hỏi phim nào phổ biến "hiện nay": một phim bán đều đặn mỗi tuần trong mười tuần gần nhất có lẽ phổ biến hơn một phim bán gấp đôi số đó trong tuần trước mà không bán trước đó.

Với sản phẩm của Amazon hay người dùng Twitter, số phần tử quá nhiều để giữ một biểu diễn DGIM cho mỗi phần tử (tr.158). Chúng ta cần một đại lượng không có biên cứng, cập nhật bằng một phép tính, và một cách chỉ giữ nó cho các phần tử đáng giữ.

<!-- note-topic-id: lec-09-topic-21 -->
### 6.1 Trọng số giảm theo tuổi

Một cách trực quan, mỗi phần tử mang trọng số 1 khi vừa đến, và mỗi khi có thêm một phần tử mới, mọi trọng số cũ nhân với $1-c$ cho một hằng số nhỏ $c$. Phần tử càng cũ càng nhẹ nhưng không bao giờ bị cắt hẳn. Ví dụ 09.17 áp nó cho hai phim, với đơn vị thời gian là tuần.

::: example Ví dụ 09.17 (Mười tuần so với một tuần)
**Dữ kiện.** Đo số vé theo một đơn vị chung: phim A bán 1 đơn vị mỗi tuần trong 10 tuần gần nhất; phim B bán 2 đơn vị tuần gần nhất và không bán trước đó (MMDS §4.7.1, tr.158). Mỗi tuần là một phần tử mang số vé của tuần; $c=0{,}1$ mỗi tuần.

**Tính.** Tuần cách đây $i$ tuần có trọng số $0{,}9^i$, nên phim A có tổng
$$
\begin{aligned}
&1+0{,}9+\cdots+0{,}9^9\\
&\quad=\frac{1-0{,}9^{10}}{0{,}1}\approx6{,}51,
\end{aligned}
$$
phim B có tổng 2.

**Diễn giải.** Với trọng số giảm theo tuổi, A đứng trên B; cửa sổ trượt một tuần cho B đứng trên (2 so với 1).

**Kiểm tra lại.** $0{,}9^{10}\approx0{,}349$, nên $(1-0{,}349)/0{,}1\approx6{,}51$.
:::

::: definition Định nghĩa 09.52 (Cửa sổ suy giảm mũ)
Cho dòng số thực không âm $x_1,x_2,\ldots$ và **hằng số suy giảm** (decay constant) $c$ với $0<c<1$. **Cửa sổ suy giảm mũ** (exponentially decaying window, gọi tắt là decaying window) sau $r$ phần tử là
$$
\begin{aligned}
D_r&=\sum_{i=0}^{r-1}x_{r-i}\,(1-c)^i,\\
D_0&=0 .
\end{aligned}
$$
Với dòng phần tử của $\mathcal U$ và $u\in\mathcal U$, **điểm phổ biến** của $u$, ký hiệu $D_r(u)$, là $D_r$ tính trên dòng chỉ báo $\mathbf 1[x_1=u],\mathbf 1[x_2=u],\ldots$.
:::

Phần tử có tuổi $i$, tức $x_{r-i}$, mang trọng số $(1-c)^i$. MMDS (§4.7.2, tr.158) dùng $c$ nhỏ, như $10^{-6}$ hay $10^{-9}$. Ví dụ 09.17 là trường hợp $x_i$ là số vé của tuần $i$ và $c=0{,}1$.

So với cửa sổ trượt (Định nghĩa 09.2), mọi phần tử đều góp nhưng với trọng số khác nhau; so với tần suất, $D_r(u)$ là tần suất có trọng số, và $D_r(u)\to f_u$ khi $c\to0$.

::: proposition Mệnh đề 09.53 (Truy hồi và tổng trọng số)
**Giả thiết.** Như Định nghĩa 09.52; $r\ge1$.

**Kết luận.**

- (a) $D_r=(1-c)\,D_{r-1}+x_r$.
- (b) $\displaystyle\sum_{i=0}^{r-1}(1-c)^i=\frac{1-(1-c)^r}{c}<\frac1c$; do đó nếu mọi $x_i\in[0,1]$ thì $D_r<1/c$.
- (c) Với dòng phần tử, $\displaystyle\sum_{u\in\mathcal U}D_r(u)=\frac{1-(1-c)^r}{c}$.

**Điều kiện áp dụng.** Tất định, mọi $r$.

**Phạm vi.** (b) là cận cho dòng hữu hạn; $1/c$ là giới hạn khi $r\to\infty$.
:::

::: proof
**Bước 1 (phần (a)).** Tách số hạng $i=0$:

$$
\begin{aligned}
&D_r\\
&\quad=x_r+\sum_{i=1}^{r-1}x_{r-i}(1-c)^i\\
&\quad=x_r+(1-c)\,D_{r-1}.
\end{aligned}
$$

Đẳng thức thứ hai rút thừa số $1-c$ khỏi tổng rồi dùng Định nghĩa 09.52 với chỉ số $i-1$ thay cho $i$. Với $r=1$, tổng rỗng và $D_0=0$.

**Bước 2 (phần (b)).** Theo công thức tổng cấp số nhân với công bội $1-c\ne1$, $\sum_{i=0}^{r-1}(1-c)^i=\frac{1-(1-c)^r}{1-(1-c)}=\frac{1-(1-c)^r}{c}$, nhỏ hơn $1/c$ vì $(1-c)^r>0$. Nếu $0\le x_i\le1$, mỗi số hạng của $D_r$ không vượt $(1-c)^i$.

**Bước 3 (phần (c)).** Đổi thứ tự tổng: $\sum_uD_r(u)=\sum_{i=0}^{r-1}(1-c)^i\sum_u\mathbf 1[x_{r-i}=u]$. Mỗi vị trí mang đúng một phần tử, nên tổng trong bằng 1, và kết quả là tổng ở (b). $\square$
:::

Phần (a) là phép cập nhật của MMDS (tr.159): nhân tổng hiện tại với $1-c$ rồi cộng phần tử mới. Với dòng mưa mỗi ngày ($x_i=1$) và $c=0{,}1$ (trang chiếu Stanford CS246 2017, Streams 1, tr.28), (a) cho $D_1=1$, $D_2=1{,}9$, $D_3=2{,}71$, và theo (b) $D_r=10(1-0{,}9^r)$ tăng tới 10 mà không đạt.

::: example Ví dụ 09.18 (Điểm của bốn phần tử)
**Dữ kiện.** Dòng mười lăm phần tử của Ví dụ 09.1, $c=1/2$; phần tử ở vị trí $i$ có tuổi $15-i$ và trọng số $2^{-(15-i)}$.

**Tính.** $\mathrm a$ ở vị trí 1, 6, 9, 13, 14, tuổi $i=14,9,6,2,1$:
$$
\begin{aligned}
&D_{15}(\mathrm a)=\sum_{i\in\{1,2,6,9,14\}}2^{-i}\\
&\quad=\frac{12\,577}{16\,384}\approx0{,}768 .
\end{aligned}
$$
$\mathrm b$ ở vị trí 2, 4, 10, 15, tuổi 13, 11, 5, 0: $D_{15}(\mathrm b)=1+2^{-5}+2^{-11}+2^{-13}=8\,453/8\,192\approx1{,}032$. Tương tự $D_{15}(\mathrm c)=2^{-3}+2^{-8}+2^{-12}\approx0{,}129$ và $D_{15}(\mathrm d)=2^{-4}+2^{-7}+2^{-10}\approx0{,}071$.

**Diễn giải.** $\mathrm b$ đứng đầu dù $f_{\mathrm a}=5>f_{\mathrm b}=4$, vì $\mathrm b$ vừa xuất hiện ở vị trí cuối. Đây là câu trả lời cho câu hỏi thứ năm của Ví dụ 09.1 với $c=1/2$.

**Kiểm tra lại.** Tổng bốn điểm bằng $32\,767/16\,384=2(1-2^{-15})<2=1/c$, đúng Mệnh đề 09.53(c).
:::

![Đồ thị cột trọng số theo tuổi phần tử, tuổi 30 bên trái, tuổi 0 (hiện tại) bên phải, với c bằng 0,1: tuổi 0 cao 1, tuổi 1 cao 0,9, tuổi 5 cao 0,59, tuổi 10 cao 0,35, tuổi 20 cao 0,12, tuổi 30 cao 0,04. Khung nét đứt cao 1 phủ 10 tuổi cuối, nhãn cửa sổ cố định độ dài 1/c bằng 10, trọng số 1 bên trong, 0 bên ngoài.](img/lec-09/cua-so-suy-giam.svg)

::: remark Nhận xét 09.54 (So với cửa sổ trượt cùng tổng trọng số)
Hình vẽ lại ý của MMDS Hình 4.4 (tr.158) với $c=0{,}1$. Cửa sổ trượt độ dài $1/c$ cho trọng số 1 cho $1/c$ phần tử mới nhất và 0 cho phần còn lại, tổng trọng số $1/c$, bằng giới hạn ở Mệnh đề 09.53(b); cửa sổ suy giảm trải tổng đó lên mọi tuổi, và phần tử ở tuổi $1/c$ còn trọng số $(1-c)^{1/c}\le e^{-1}\approx0{,}37$. Với $c=10^{-9}$, nó xấp xỉ cửa sổ $10^9$ phần tử gần nhất (MMDS tr.159) mà không cần biết phần tử nào rời đi.
:::

<!-- note-topic-id: lec-09-topic-22 -->
### 6.2 Duy trì các phần tử phổ biến

Giữ $D_r(u)$ cho mọi $u$ tốn $d$ số. Một cách trực quan, tổng mọi điểm nhỏ hơn $1/c$ (Mệnh đề 09.53(c)), nên chỉ ít phần tử có điểm lớn, và các phần tử còn lại có thể quên mà chỉ mất phần điểm nhỏ.

Để tìm các phần tử phổ biến (most popular elements), MMDS (§4.7.3, tr.159) chỉ giữ điểm đạt một ngưỡng. Ký hiệu $\widehat D_r(u)$ là điểm được duy trì của $u$ sau $r$ phần tử; ví dụ sau dùng ngưỡng $\theta=1/2$ của MMDS.

::: example Ví dụ 09.19 (Vết chạy với $c=1/2$, ngưỡng $1/2$)
**Dữ kiện.** Dòng mười lăm phần tử của Ví dụ 09.1; $c=1/2$; ngưỡng $\theta=1/2$. Mỗi bước: nhân mọi điểm đang giữ với $1/2$; cộng 1 vào điểm của phần tử vừa đến, hoặc tạo điểm 1 nếu chưa có; xóa mọi điểm nhỏ hơn $1/2$.

**Vết chạy.**

| $r$ | $x_r$ | điểm được giữ sau bước $r$ | bị xóa |
|---:|---|---|---|
| 1 | $\mathrm a$ | $\mathrm a:1$ | — |
| 2 | $\mathrm b$ | $\mathrm a:1/2$, $\mathrm b:1$ | — |
| 3 | $\mathrm c$ | $\mathrm b:1/2$, $\mathrm c:1$ | $\mathrm a$ ($1/4$) |
| 4 | $\mathrm b$ | $\mathrm b:5/4$, $\mathrm c:1/2$ | — |
| 5 | $\mathrm d$ | $\mathrm b:5/8$, $\mathrm d:1$ | $\mathrm c$ ($1/4$) |
| 6 | $\mathrm a$ | $\mathrm d:1/2$, $\mathrm a:1$ | $\mathrm b$ ($5/16$) |
| 7–13 | $\mathrm c,\mathrm d,\mathrm a,\mathrm b,\mathrm d,\mathrm c,\mathrm a$ | phần tử trước $1/2$, phần tử vừa đến $1$ | phần tử có điểm $1/4$ |
| 14 | $\mathrm a$ | $\mathrm a:3/2$ | $\mathrm c$ ($1/4$) |
| 15 | $\mathrm b$ | $\mathrm a:3/4$, $\mathrm b:1$ | — |

Ở các bước 7 đến 13, phần tử vừa đến luôn khác hai phần tử trước nó, nên mỗi bước giữ đúng hai điểm: $1/2$ cho phần tử của bước trước và 1 cho phần tử vừa đến.

**Diễn giải.** Thuật toán luôn giữ nhiều nhất hai điểm. Cuối dòng, $\widehat D_{15}(\mathrm b)=1$, $\widehat D_{15}(\mathrm a)=3/4$, so với điểm thật $1{,}032$ và $0{,}768$ (Ví dụ 09.18): phần dư mất khi điểm bị xóa rồi tạo lại.

**Kiểm tra lại.** Bước 14: $\mathrm c:1/2\to1/4$ bị xóa, $\mathrm a:1\to1/2+1=3/2$. Bước 15: $\mathrm a:3/4$, $\mathrm b$ mới $1$.
:::

::: algorithm Thuật toán 09.55 (Phần tử phổ biến trong cửa sổ suy giảm)
**Đầu vào.** Dòng $x_1,x_2,\ldots$ gồm phần tử của $\mathcal U$; hằng số suy giảm $c\in(0,1)$; ngưỡng $\theta\in(0,1)$, MMDS dùng $\theta=1/2$.

**Đầu ra.** Khi có truy vấn, tập phần tử đang được theo dõi cùng điểm được duy trì $\widehat D_r(u)$.

**Giả thiết.** Phép nhân và phép cộng số thực tính là $O(1)$.

1. Khởi tạo tập điểm rỗng.
2. Khi $x_r$ đến: nhân mọi điểm đang giữ với $1-c$.
3. Nếu $x_r$ đang được theo dõi, cộng 1 vào điểm của nó; nếu không, tạo điểm $\widehat D_r(x_r)=1$.
4. Xóa mọi điểm nhỏ hơn $\theta$.

**Dừng.** Mỗi phần tử được xử lý sau một lượt qua các điểm đang giữ.

**Trường hợp biên.** Phần tử vừa tạo có điểm $1>\theta$, nên không bị xóa ở bước của chính nó.

**Chi phí.** Mô hình: điểm giữ trong bảng băm, mỗi phép nhân, cộng, tra, xóa tốn $O(1)$; trường hợp xấu nhất, $\Lambda<1/(c\theta)$ điểm đang giữ (Định lý 09.56).

| Bước | Số lần mỗi phần tử | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| nhân điểm (bước 2) | $\Lambda$ | $O(1)$ | $O(1/(c\theta))$ |
| cộng hoặc tạo điểm (bước 3) | 1 | $O(1)$ | $O(1)$ |
| xóa điểm nhỏ (bước 4) | $\Lambda+1$ phép kiểm | $O(1)$ | $O(1/(c\theta))$ |

Bộ nhớ nhỏ hơn $1/(c\theta)$ cặp (phần tử, điểm).
:::

Phép quyết định là bước 4: chỉ những phần tử có điểm đạt ngưỡng được giữ. Ví dụ 09.19 là một lượt chạy với $c=\theta=1/2$. Định lý sau cho cận số điểm được giữ, và cận này không phụ thuộc $d$.

::: theorem Định lý 09.56 (Số điểm được duy trì)
**Giả thiết.** Thuật toán 09.55 với $c\in(0,1)$ và $\theta>0$ chạy trên dòng $x_1,\ldots,x_r$.

**Kết luận.**

- (a) Với mọi $u$ đang được theo dõi, $\widehat D_r(u)\le D_r(u)$.
- (b) Sau mỗi bước, số phần tử được theo dõi nhỏ hơn $1/(c\theta)$; với $\theta=1/2$, nhỏ hơn $2/c$.

**Điều kiện áp dụng.** Tất định. Cận (b) đúng với mọi $\theta>0$. Với $\theta>1$ thuật toán không theo dõi phần tử nào; với $\theta=1$ nó chỉ giữ phần tử vừa đến, trừ khi một phần tử lặp lại liên tiếp.

**Phạm vi.** Định lý chặn số điểm; nó không khẳng định mọi phần tử có $D_r(u)\ge\theta$ đều được theo dõi, vì điểm được duy trì có thể nhỏ hơn điểm thật.
:::

::: proof
**Bước 1 (phần (a), quy nạp theo $r$).** Với $r=0$ không có điểm nào. Giả sử $\widehat D_{r-1}(u)\le D_{r-1}(u)$ cho mọi $u$ được theo dõi sau bước $r-1$. Xét $u$ được theo dõi sau bước $r$.

- Nếu $u$ được theo dõi từ trước, bước 2 và 3 cho, với $\iota_r=\mathbf 1[x_r=u]$,
$$
\begin{aligned}
&\widehat D_r(u)\\
&\quad=(1-c)\widehat D_{r-1}(u)+\iota_r\\
&\quad\le(1-c)D_{r-1}(u)+\iota_r\\
&\quad=D_r(u),
\end{aligned}
$$
trong đó bất đẳng thức dùng giả thiết quy nạp và đẳng thức cuối dùng Mệnh đề 09.53(a).
- Nếu $u$ được tạo ở bước $r$, thì $u=x_r$ và $\widehat D_r(u)=1\le(1-c)D_{r-1}(u)+1=D_r(u)$, vì $D_{r-1}(u)\ge0$.

Bước 4 chỉ xóa điểm, không đổi các điểm còn lại.

**Bước 2 (tổng các điểm được giữ).** Theo Bước 1 và Mệnh đề 09.53(c),
$$
\begin{aligned}
&\sum_{u\ \text{theo dõi}}\widehat D_r(u)\\
&\quad\le\sum_{u\ \text{theo dõi}}D_r(u)\\
&\quad\le\sum_{u\in\mathcal U}D_r(u)\\
&\quad=\frac{1-(1-c)^r}{c}<\frac1c.
\end{aligned}
$$

Ba quan hệ lần lượt dùng Bước 1, việc thêm các số hạng không âm và Mệnh đề 09.53(c).

**Bước 3 (đếm).** Sau bước 4, mọi điểm được giữ đều $\ge\theta$. Nếu có $\Lambda$ phần tử được theo dõi thì $\Lambda\theta\le\sum\widehat D_r(u)<1/c$, nên $\Lambda<1/(c\theta)$.

**Bước 4 (vì sao cần $\theta<1$).** Phần tử mới có điểm 1. Nếu $\theta>1$, nó bị xóa ngay ở bước 4, và không phần tử nào được theo dõi. Nếu $\theta=1$, nó sống qua bước của mình nhưng bị xóa ở bước kế tiếp, khi điểm thành $1-c<1$, trừ khi nó xuất hiện lại ngay. $\square$
:::

Với $c=10^{-9}$ và ngưỡng $1/2$, thuật toán giữ ít hơn $2\cdot10^9$ điểm, bất kể có bao nhiêu phần tử phân biệt; cận chỉ có tác dụng khi số phần tử phân biệt vượt xa $1/(c\theta)$ (MMDS chú thích 6, tr.159), vì số điểm không bao giờ vượt $d$.

Bước 2 dùng tổng chính xác cho dòng hữu hạn, nhỏ hơn $1/c$, nên (b) là bất đẳng thức ngặt.

So với Mệnh đề 09.53, vốn giữ chính xác một tổng $D_r$, Định lý 09.56 đổi tính chính xác của từng điểm lấy bộ nhớ: điểm được duy trì chỉ là cận dưới của $D_r(u)$, nhưng số điểm không phụ thuộc $d$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ bước 2 (không nhân với $1-c$): điểm thành tần suất $f_u$, và trên dòng gồm $r$ phần tử phân biệt thuật toán giữ $r$ điểm.
- Bỏ bước 4 (không xóa): số điểm bằng $d$.

Bước 1 dùng bước 2 của thuật toán và truy hồi của Mệnh đề 09.53; Bước 3 dùng bước 4 của thuật toán. Điều kiện $\theta<1$ không phải giả thiết của cận; nó chỉ cần để phần tử mới được theo dõi quá một bước (Bước 4).

::: remark Nhận xét 09.57 (Trong thực hành)
Mỗi điểm là một cặp (mã phần tử, số thực) trong một bảng băm, và bước 2 nhân mọi điểm, nên thời gian mỗi phần tử tỷ lệ với số điểm đang giữ. Điểm được duy trì là cận dưới của điểm thật (Định lý 09.56(a)), nên thứ hạng có thể khác thứ hạng theo điểm thật.
:::

::: exercise Bài tập 09.8 (Ngưỡng $1/4$)
Thuật toán 09.55 chạy với ngưỡng $\theta=1/4$.

- (a) Với $c=10^{-6}$, chặn số điểm được giữ.
- (b) Với $c=1/2$, chạy năm bước đầu trên dòng $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d$.
:::

::: hint
(a) Định lý 09.56(b). (b) Một điểm bị xóa khi nhỏ hơn $1/4$.
:::

::: solution
(a) Số điểm nhỏ hơn $1/(c\theta)=1/(10^{-6}\cdot1/4)=4\cdot10^6$.

(b) Bước 1: $\mathrm a:1$. Bước 2: $\mathrm a:1/2$, $\mathrm b:1$. Bước 3: $\mathrm a:1/4$, $\mathrm b:1/2$, $\mathrm c:1$; điểm $1/4$ không nhỏ hơn $1/4$ nên giữ. Bước 4: $\mathrm a:1/8$ bị xóa, $\mathrm b:1/4+1=5/4$, $\mathrm c:1/2$. Bước 5: $\mathrm b:5/8$, $\mathrm c:1/4$, $\mathrm d:1$. Cận $1/(c\theta)=8$; thuật toán giữ nhiều nhất 3 điểm.

**Kiểm tra lại.** Tổng điểm sau bước 5 là $5/8+1/4+1=15/8<2=1/c$.
:::

Như vậy, chúng ta đã thay biên cứng bằng trọng số $(1-c)^{\text{tuổi}}$ (Định nghĩa 09.52), cập nhật bằng một phép nhân và một phép cộng (Mệnh đề 09.53), và theo dõi phần tử phổ biến gần đây với ít hơn $1/(c\theta)$ điểm (Định lý 09.56). Tuy nhiên, năm phác thảo của chương có năm loại bảo đảm và năm bộ giả thiết khác nhau. Trong Mục 7, chúng ta dùng chúng cho một trang web có năm yêu cầu.

<!-- note-topic-id: lec-09-topic-23 -->
## 7. Chọn cấu trúc theo câu hỏi

Một trang web cần năm đại lượng trên cùng dòng lượt truy cập, từ số người dùng phân biệt trong tháng đến các URL phổ biến gần đây (Ví dụ 09.20); mỗi yêu cầu cần một phác thảo có giả thiết kiểm được và chi phí chấp nhận được.

### 7.1 Kết quả, giả thiết và chi phí

Bảo đảm của chương thuộc ba loại: tất định (Bổ đề 09.35, Định lý 09.46, 09.56), xác suất theo phép chọn hàm băm (Định lý 09.10, 09.37) và kỳ vọng (Định lý 09.22). Các kết quả chính được gom trong bảng đầu, cùng giả thiết mà thiếu nó kết quả sai.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Ngưỡng hai phía (Định lý 09.10) | giá trị băm đều; độc lập (cho phía dưới); $d\le2^L$ | $\Pr[2^R\ge\lambda d]\le1/\lambda$, $\Pr[2^R\le d/\lambda]\le e^{-\lambda/2}$ |
| Mẹo trung vị (Bổ đề 09.14) | các ước lượng độc lập; $G$ là khoảng | $\Pr[M\notin G]\le(4\eta)^{g/2}$, có ích khi $\eta<1/4$ |
| Biến AMS không chệch (Định lý 09.22) | $I$ đều; đếm ở hậu tố | $\mathbb E[r(2v_I-1)]=F_2$ |
| Bảo đảm Count-Min (Định lý 09.37) | mỗi phần tử cộng 1; họ băm phổ dụng; các hàng độc lập | $f_u\le\widehat f_u$; thừa $\ge\varepsilon r/\kappa$ với xác suất $\le\delta$ |
| Bộ nhớ DGIM (Mệnh đề 09.44) | sáu quy tắc; mốc phải trong cửa sổ | $\le2(\lfloor\log_2N\rfloor+1)$ thùng, $O(\log^2N)$ bit |
| Cận 50% (Định lý 09.46) | quy tắc 1–6 | $\tfrac12y_k\le\widehat y_k\le\tfrac32y_k$ |
| Số điểm được duy trì (Định lý 09.56) | nhân điểm với $1-c$; xóa điểm $<\theta$ | ít hơn $1/(c\theta)$ điểm |

Các thuật toán được đặt cạnh nhau trong bảng thứ hai.

| Thuật toán | Đại lượng | Bảo đảm | Bộ nhớ | Mỗi phần tử |
|---|---|---|---|---|
| Flajolet–Martin gộp (Thuật toán 09.13) | $F_0$ | xác suất, hai phía | $q\lceil\log_2(L+1)\rceil+1$ bit | $q$ phép băm |
| AMS (Thuật toán 09.24) | $F_2$, $F_p$ | kỳ vọng | $s$ cặp (phần tử, bộ đếm), bộ đếm $r$ | $O(s)$ phép so sánh |
| Count-Min (Thuật toán 09.34) | $f_u$ | một phía tất định, cận trên xác suất | $mt$ bộ đếm | $t$ phép băm, $t$ phép cộng |
| DGIM (Thuật toán 09.45, 09.47) | $y_k$, $k\le N$ | tất định, sai số tương đối $\le50\%$ | $O(\log^2N)$ bit | xấu nhất $O(\log N)$, khấu hao $O(1)$ lượt gộp |
| Cửa sổ suy giảm (Mệnh đề 09.53, Thuật toán 09.55) | $D_r$, $D_r(u)$ | $D_r$ chính xác; $\widehat D_r(u)\le D_r(u)$ | 1 số; ít hơn $1/(c\theta)$ điểm | $O(1)$; $O(1/(c\theta))$ |

Hai bảng cho một quy trình chọn phác thảo gồm ba bước.

1. **Xác định đại lượng và phạm vi thời gian.** Số phần tử phân biệt, độ lệch, tần suất từng phần tử, số sự kiện trong $N$ phần tử cuối, hay độ phổ biến có trọng số theo tuổi.
2. **Kiểm giả thiết** của kết quả sẽ dùng theo cột giữa của bảng đầu: hàm băm có xấp xỉ được mô hình đều, độc lập không; dòng có chỉ cộng không; vị trí có được chọn đều không.
3. **Đếm chi phí** với số liệu của bài toán theo bảng thứ hai, và so với lời giải chính xác của Nhận xét 09.3.

### 7.2 Trả lời năm câu hỏi

::: example Ví dụ 09.20 (Chọn phác thảo cho năm yêu cầu)
**Dữ kiện.** Trên dòng lượt truy cập của một trang có năm yêu cầu: (a) số người dùng phân biệt trong tháng, nhận diện theo địa chỉ IP, với $d$ khoảng $10^6$; (b) phân bố lượt truy cập theo người dùng lệch đến đâu; (c) một địa chỉ cho trước gửi bao nhiêu yêu cầu, và địa chỉ nào gửi ít nhất $1\%$ số yêu cầu; (d) một URL được truy cập bao nhiêu lần trong $10^9$ lượt gần nhất; (e) các URL phổ biến gần đây.

**Tính.**

| Yêu cầu | Đại lượng | Phác thảo | Kết quả dùng | Giả thiết cần kiểm | Chi phí |
|---|---|---|---|---|---|
| (a) | $F_0$ | Flajolet–Martin, gộp trung bình rồi trung vị | Định lý 09.10 cho từng hàm băm; bước trung bình nhóm chưa có cận định lượng | băm 64 bit xấp xỉ đều, độc lập | $q=420$, khoảng 368 byte |
| (b) | $F_2$ | biến AMS với hồ chứa vị trí | Hệ quả 09.26 | $\xi$ đều; đủ nhiều biến | $s$ cặp (phần tử, bộ đếm) |
| (c) | $f_u$; phần tử nặng $\kappa=100$ | Count-Min | Hệ quả 09.38 | các hàng độc lập; liệt kê ứng viên theo UMass (trang chiếu 19, chưa chứng minh) | $74\,000$ bộ đếm với $\varepsilon=0{,}1$, $\delta=0{,}01$, $r_{\max}=10^9$ |
| (d) | $y_k$, $N=10^9$ | DGIM cho URL được hỏi | Mệnh đề 09.44, Định lý 09.46 | sáu quy tắc | khoảng 266 byte mỗi URL |
| (e) | $D_r(u)$ | cửa sổ suy giảm, ngưỡng $1/2$ | Định lý 09.56 | chọn $c$ | không quá $d$ và ít hơn $2/c$ điểm |

**Diễn giải.** Yêu cầu (b) không dùng Flajolet–Martin, vì hai dòng của Ví dụ 09.2 có cùng $F_0$; (c) không dùng AMS, vì $F_2$ không chỉ ra phần tử nặng; (d) không dùng Count-Min, vì tần suất tính trên toàn dòng; (e) không dùng DGIM, vì xếp hạng cần đọc biểu diễn của mọi URL ở mỗi truy vấn.

**Kiểm tra lại.** (d): $60$ thùng $\times35$ bit $+30=2\,130$ bit, khoảng 266 byte, khớp Mệnh đề 09.44.
:::

::: exercise Bài tập 09.9 (Chọn phác thảo theo câu hỏi)
Chọn phác thảo, nêu kết quả bảo đảm và tính bộ nhớ: (a) số người dùng phân biệt xem từng trang trong tháng, trên $10^6$ trang, mỗi trang $d$ tới $10^6$ (MMDS §4.4.1), với $g=21$ nhóm cỡ 20 và băm 64 bit; (b) số lượt vào mỗi URL trong $N=10^6$ lượt gần nhất, cho $10^4$ URL; (c) phim phổ biến hiện thời với $c=10^{-9}$, ngưỡng $1/2$ (MMDS §4.7.3).
:::

::: hint
Theo ba bước của Mục 7.1, dùng Mệnh đề 09.16, Mệnh đề 09.44, Định lý 09.56.
:::

::: solution
(a) $F_0$ trên toàn tháng: Thuật toán 09.13; chỉ từng hàm băm (Định lý 09.10) và trung vị thuần (Hệ quả 09.15) có cận định lượng; mỗi trang $420\cdot7+1=2\,941$ bit, khoảng 368 byte (Mệnh đề 09.16), tổng khoảng 368 MB. (b) $y_N$ của một dòng bit mỗi URL: DGIM, sai số tương đối không quá 50% (Định lý 09.46), nhiều nhất $2(19+1)=40$ thùng, mỗi thùng $20+5=25$ bit, cộng 20 bit cho $r\bmod N$, tức $1\,020$ bit mỗi URL (Mệnh đề 09.44), tổng khoảng $1{,}3$ MB. (c) $D_r(u)$: Thuật toán 09.55, ít hơn $2\cdot10^9$ điểm và không quá số phim (Định lý 09.56).

**Kiểm tra lại.** $2\,941/8\approx368$; $1\,020\cdot10^4/8\approx1{,}3\cdot10^6$ byte.
:::

Như vậy, năm câu hỏi của Mục 1 có năm phác thảo với bộ nhớ không tỷ lệ với $d$ hay $N$, mỗi phác thảo kèm một bảo đảm có điều kiện.

<!-- note-topic-id: lec-09-topic-24 -->
## Tình huống áp dụng và ứng dụng

Tình huống 09.1 và 09.2 thỏa giả thiết của các kết quả được dùng; Tình huống 09.3 vi phạm giả thiết của Định lý 09.22.

::: application Tình huống 09.1 (Cỡ lân cận trong mạng xã hội)
**Bài toán và dữ liệu.** "Ảnh hưởng" của người dùng $\mathrm E$ được đo bằng cỡ lân cận $\lvert\mathcal N(\mathrm E,\Delta)\rvert$, số người cách $\mathrm E$ không quá $\Delta$ bước (Stanford CS246 2017, Streams 2, tr.32–38). Đồ thị bảy đỉnh của nguồn có các cạnh $\mathrm{A}$–$\mathrm B$, $\mathrm A$–$\mathrm C$, $\mathrm B$–$\mathrm C$, $\mathrm B$–$\mathrm D$, $\mathrm D$–$\mathrm E$, $\mathrm D$–$\mathrm F$, $\mathrm D$–$\mathrm G$, $\mathrm E$–$\mathrm F$, $\mathrm F$–$\mathrm G$. Lân cận của $\mathrm E$ là $\{\mathrm E\}$ khi $\Delta=0$, $\{\mathrm D,\mathrm E,\mathrm F\}$ khi $\Delta=1$, $\{\mathrm B,\mathrm D,\mathrm E,\mathrm F,\mathrm G\}$ khi $\Delta=2$ và cả bảy đỉnh khi $\Delta=3$; cỡ là $1,3,5,7$. Trên đồ thị lớn, giữ và hợp các tập lân cận không khả thi (tr.35).

**Mô hình hóa.** Cỡ lân cận là $F_0$ của tập đỉnh trong lân cận. Viết $u'\sim u$ khi $u'$ kề $u$. Vì $\mathcal N(u,\Delta)=\{u\}\cup\bigcup_{u'\sim u}\mathcal N(u',\Delta-1)$, Mệnh đề 09.7(b) cho truy hồi $R(u,\Delta)=\max\bigl(\rho(h(u)),\max_{u'\sim u}R(u',\Delta-1)\bigr)$ (Streams 2, tr.37), và ước lượng là $2^{R(\mathrm E,\Delta)}$.

**Kiểm giả thiết.** Mọi đỉnh dùng cùng hàm $h$ tất định, nên phép hợp tập ứng với phép max (Mệnh đề 09.7); giả thiết của Định lý 09.10 chỉ được xấp xỉ.

**Áp dụng.** Với các giá trị băm 5 bit cho sẵn $00110$, $00111$, $01000$, $01001$, $01010$, $01011$, $01100$ của $\mathrm A,\ldots,\mathrm G$, độ dài đuôi là $\mathrm A:1$, $\mathrm B:0$, $\mathrm C:3$, $\mathrm D:0$, $\mathrm E:1$, $\mathrm F:0$, $\mathrm G:2$. Truy hồi cho $R(\mathrm E,\Delta)=1,1,2,3$, ước lượng $2,2,4,8$ so với cỡ thật $1,3,5,7$.

**Chi phí.** Mỗi mức $\Delta$ là một lượt qua mọi cạnh, mỗi cạnh một phép max cho mỗi hàm băm: $O(q)$ phép cho mỗi cạnh ở mỗi mức. Bộ nhớ là $2q$ số nhỏ cho mỗi đỉnh, vì cần giữ hai mức liên tiếp $R(\cdot,\Delta-1)$ và $R(\cdot,\Delta)$ (Mệnh đề 09.16).

**Diễn giải và giới hạn.** Một hàm băm cho cỡ đúng bậc nhưng lệch tới 2 lần, như Định lý 09.10 cho phép; gộp $q$ hàm bằng Thuật toán 09.13 giảm sai lệch (Streams 2, tr.38). Ước lượng không liệt kê được các đỉnh trong lân cận.

**Dẫn ngược lý thuyết.** Định nghĩa 09.5, Mệnh đề 09.7, Định lý 09.10, Thuật toán 09.13, Mệnh đề 09.16.
:::

::: application Tình huống 09.2 (Lượt truy cập URL gần đây: DGIM và cửa sổ suy giảm)
**Bài toán và dữ liệu.** Trang web có $10^6$ URL, cần số lượt truy cập mỗi URL trong $N=10^9$ lượt gần nhất (Streams 1, tr.13) và danh sách URL phổ biến gần đây.

**Mô hình hóa và kiểm giả thiết.** Mỗi URL có một dòng bit, và câu hỏi thứ nhất là $y_N$ của dòng đó; Thuật toán 09.47 giữ sáu quy tắc (Định lý 09.48), nên Định lý 09.46 áp dụng. Câu hỏi thứ hai là các URL có điểm $D_r(u)$ lớn, với $c=10^{-9}$ ứng với khoảng $10^9$ lượt gần nhất (Nhận xét 09.54); Thuật toán 09.55 không cần giả thiết xác suất.

**Áp dụng và chi phí.** DGIM: nhiều nhất 60 thùng, khoảng 266 byte mỗi URL (Mệnh đề 09.44), tổng khoảng 266 MB, sai số tương đối $\le50\%$. Lời giải chính xác giữ $N$ mã URL cuối trong một bộ đệm vòng, $10^9\cdot20$ bit $=2{,}5$ GB, cùng một bộ đếm 30 bit cho mỗi URL, tức khoảng 9 lần DGIM.

Mỗi lượt truy cập là bit 1 cho một URL và bit 0 cho mọi URL khác, nên chạy bước hết hạn của Thuật toán 09.47 cho mọi dòng tốn $10^6$ phép kiểm mỗi lượt.

Cửa sổ suy giảm giữ không quá $\min(d,1/(c\theta))=\min(10^6,\,2\cdot10^9)=10^6$ điểm, nên cận của Định lý 09.56 không có tác dụng và có thể giữ $D_r(u)$ chính xác cho mọi URL.

**Diễn giải và giới hạn.** DGIM đếm lượt trong $N$ lượt cuối với cận tất định; cửa sổ suy giảm đo một đại lượng khác, độ phổ biến có trọng số, và mỗi lượt truy cập phải nhân mọi điểm đang giữ.

**Dẫn ngược lý thuyết.** Mệnh đề 09.44, Thuật toán 09.45, 09.47, Định lý 09.46, 09.48, Định nghĩa 09.52, Thuật toán 09.55, Định lý 09.56.
:::

::: application Tình huống 09.3 (Ước lượng mômen khi vị trí được chọn một lần)
**Bài toán và dữ liệu.** Để khỏi rút số ngẫu nhiên cho mọi phần tử, một hệ thống ước lượng $F_2$ bằng biến AMS chọn vị trí đều trong $r_0$ phần tử đầu rồi giữ các biến đó mãi. Dữ kiện: dòng $\mathrm{a},\mathrm{b},\mathrm{c},\mathrm{b},\mathrm{d},\mathrm{a},\mathrm{c},\mathrm{d},\mathrm{a},\mathrm{b},\mathrm{d},\mathrm{c},\mathrm{a},\mathrm{a},\mathrm{b}$, $r_0=5$, truy vấn tại $r=15$, $F_2=59$.

**Kiểm giả thiết.** Định lý 09.22 cần $I$ đều trên $\{1,\ldots,r\}$ tại thời điểm hỏi. Ở đây $I$ đều trên $\{1,\ldots,5\}$, nên giả thiết bị vi phạm.

**Hậu quả.** Với $v_1,\ldots,v_5=5,4,3,3,3$ (Ví dụ 09.8), kỳ vọng của một biến là
$$
\begin{aligned}
&\mathbb E[X]=\frac15\sum_{i=1}^{5}15\,(2v_i-1)\\
&\quad=3\cdot(9+7+5+5+5)\\
&\quad=93,
\end{aligned}
$$
lớn hơn $F_2=59$ khoảng $58\%$. Lấy trung bình nhiều biến không sửa được, vì mọi biến cùng lệch.

**Cách sửa, chi phí và giới hạn.** Thuật toán 09.24 tốn thêm một lần rút $\xi$ và nhiều nhất một lần ghi mỗi phần tử, và theo Hệ quả 09.26 trung bình các biến có kỳ vọng đúng $F_2$ ở mọi $r\ge s$; độ phân tán của một biến vẫn lớn (Ví dụ 09.8).

**Dẫn ngược lý thuyết.** Định lý 09.22, Thuật toán 09.24, Mệnh đề 09.25, Hệ quả 09.26, Định lý 08.17.
:::

**Ứng dụng trong các bài khác và trong nguồn.**

- Ghi chú Bài 08: hồ chứa của Định lý 08.17 là cơ chế giữ vị trí của Thuật toán 09.24; tính tất định của hàm băm, giả thiết của Mệnh đề 08.10, là điều kiện của Mệnh đề 09.7.
- Ghi chú Bài 03 (PageRank): trang chiếu Stanford CS246 (2017, Streams 2, tr.24) nêu việc đếm số trang khác nhau liên kết tới mỗi trang để hỗ trợ ước lượng PageRank, một bài toán $F_0$ trên mỗi trang.
- Trang chiếu MMDS (Streams 2, tr.18) nêu số từ khác nhau trên các trang thu thập được của một trang web như dấu hiệu của trang nhân tạo, cũng là một bài toán $F_0$.

<!-- note-topic-id: lec-09-topic-25 -->
## Tóm tắt chương

Yêu cầu Bài 08 để ngỏ, đếm số người dùng phân biệt, được mở rộng thành năm câu hỏi trên một dòng, mỗi câu hỏi có lời giải chính xác tốn bộ nhớ tỷ lệ với $d$ hoặc $N$ (Định nghĩa 09.1, Nhận xét 09.3). Cho $F_0$, Flajolet–Martin chỉ giữ độ dài đuôi lớn nhất, và $2^R$ nằm trong $(d/\lambda,\lambda d)$ với xác suất ít nhất $1-1/\lambda-e^{-\lambda/2}$ (Định lý 09.10); vì kỳ vọng của $2^R$ quá lớn (Mệnh đề 09.11), các ước lượng được gộp bằng trung bình trong nhóm rồi trung vị (Thuật toán 09.13, Bổ đề 09.14). $F_0$ không phân biệt được hai dòng lệch khác nhau, nên biến AMS ước lượng $F_2$ với kỳ vọng đúng (Định lý 09.22), duy trì được bằng hồ chứa vị trí (Hệ quả 09.26). $F_2$ không chỉ ra phần tử nặng, nên Count-Min ước lượng từng $f_u$, không bao giờ thấp và thừa quá $\varepsilon r/\kappa$ với xác suất không quá $\delta$ (Định lý 09.37). Các đại lượng đó tính trên toàn dòng, nên DGIM đếm bit 1 trong cửa sổ với $O(\log^2N)$ bit và sai số tương đối không quá 50% (Định lý 09.46, 09.48), trong khi đáp số chính xác cần $N$ bit (Mệnh đề 09.41). Cửa sổ trượt cần một biểu diễn cho mỗi phần tử, nên cửa sổ suy giảm mũ dùng trọng số $(1-c)^{\text{tuổi}}$ và theo dõi phần tử phổ biến với ít hơn $1/(c\theta)$ điểm (Định lý 09.56). Bước trung bình nhóm của Flajolet–Martin và số biến AMS cần dùng chưa có cận định lượng; Bài 10 chuyển sang dữ liệu phải lưu hoặc truyền mà khôi phục đúng từng bit.

**Định nghĩa và kết quả theo mục.**

- Mục 1: tần suất và mômen (Định nghĩa 09.1); cửa sổ trượt (Định nghĩa 09.2); chi phí lời giải chính xác (Nhận xét 09.3).
- Mục 2: Nhận xét 09.4; độ dài đuôi (Định nghĩa 09.5); Flajolet–Martin (Thuật toán 09.6, Mệnh đề 09.7); mô hình băm lý tưởng (Định nghĩa 09.8); ngưỡng hai phía (Bổ đề 09.9, Định lý 09.10); phân phối đuôi nặng (Mệnh đề 09.11, Nhận xét 09.12); gộp và mẹo trung vị (Thuật toán 09.13, Bổ đề 09.14, Hệ quả 09.15); chi phí (Mệnh đề 09.16, Nhận xét 09.17, 09.18).
- Mục 3: biến AMS (Định nghĩa 09.19, Thuật toán 09.20); tổng các số lẻ (Bổ đề 09.21); không chệch (Định lý 09.22); mômen bậc $p$ (Hệ quả 09.23); dòng chưa biết độ dài (Thuật toán 09.24, Mệnh đề 09.25, Hệ quả 09.26); độc lập, gộp và nhầm lẫn (Nhận xét 09.27, 09.28, 09.29).
- Mục 4: phần tử nặng (Định nghĩa 09.30); họ băm phổ dụng (Định nghĩa 09.31); Markov (Bổ đề 09.32); Count-Min (Định nghĩa 09.33, Thuật toán 09.34); một phía (Bổ đề 09.35); nhiễu một hàng (Bổ đề 09.36); bảo đảm (Định lý 09.37, Hệ quả 09.38); thực hành (Nhận xét 09.39, 09.40).
- Mục 5: cận dưới $N$ bit (Mệnh đề 09.41); thùng và sáu quy tắc (Định nghĩa 09.42); các thùng phủ liên tiếp (Nhận xét 09.43); bộ nhớ (Mệnh đề 09.44); truy vấn và cận 50% (Thuật toán 09.45, Định lý 09.46); cập nhật (Thuật toán 09.47, Định lý 09.48, Mệnh đề 09.49); mở rộng và thực hành (Nhận xét 09.50, 09.51).
- Mục 6: cửa sổ suy giảm (Định nghĩa 09.52, Mệnh đề 09.53, Nhận xét 09.54); phần tử phổ biến (Thuật toán 09.55, Định lý 09.56, Nhận xét 09.57).
- Mục 7: hai bảng đối chiếu và quy trình chọn phác thảo.

**Công thức và thuật toán cần nhớ.** Flajolet–Martin và biến AMS:

$$
\begin{gathered}
\Pr[2^R\ge\lambda d]\le\frac1\lambda,\\
\Pr[2^R\le d/\lambda]\le e^{-\lambda/2},\\
\mathbb E\bigl[r(2v_I-1)\bigr]=F_2 .
\end{gathered}
$$

Count-Min:

$$
\begin{gathered}
m=\Bigl\lceil\frac{2\kappa}{\varepsilon}\Bigr\rceil,\qquad t=\Bigl\lceil\log_2\frac1\delta\Bigr\rceil,\\
f_u\le\widehat f_u,\qquad \Pr\Bigl[\widehat f_u\ge f_u+\frac{\varepsilon r}{\kappa}\Bigr]\le\delta .
\end{gathered}
$$

DGIM và cửa sổ suy giảm:

$$
\begin{gathered}
\widehat y_k=T+\frac{\lvert b^*\rvert}{2},\\
\tfrac12y_k\le\widehat y_k\le\tfrac32y_k,\\
D_r=(1-c)D_{r-1}+x_r,\\
\#\text{điểm}<\frac1{c\theta}.
\end{gathered}
$$

Phép gộp DGIM: khi có ba thùng cùng cỡ, gộp hai thùng cũ nhất, giữ mốc phải của thùng mới hơn.

**Giả thiết hay bị bỏ quên.**

- Flajolet–Martin: độc lập của các giá trị băm cho phía dưới của Định lý 09.10; bước cuối của phép gộp là trung vị.
- AMS: vị trí đều trên mọi vị trí đã đọc; biến từ một hồ chứa chung không độc lập.
- Count-Min: các hàng độc lập; số hàng cho mọi phần tử phụ thuộc cận $r_{\max}$ chọn trước.
- DGIM: quy tắc 4 cho cận 50%.
- Cửa sổ suy giảm: tổng trọng số nhỏ hơn $1/c$ với mọi $r$ hữu hạn; điểm được duy trì là cận dưới của điểm thật.

<!-- note-topic-id: lec-09-topic-26 -->
## Bài tập củng cố

Bộ bài tập của chương gồm chín bài trong các mục và mười bài dưới đây. Mục tiêu 1 được kiểm bởi Bài tập 09.1, 09.9, 09.10 và 09.18; mục tiêu 2 bởi 09.2, 09.3, 09.11, 09.17; mục tiêu 3 bởi 09.4, 09.5, 09.12, 09.13, 09.14; mục tiêu 4 bởi 09.6; mục tiêu 5 bởi 09.7, 09.15, 09.16; mục tiêu 6 bởi 09.8, 09.19. Năm bài 09.10, 09.11, 09.12, 09.15 và 09.16, tức các bài 4.5.1, 4.4.1, 4.5.3, 4.6.1, 4.6.3 của MMDS, là bài của phần bài tập vận dụng trên lớp.

### Mức nhận biết

::: exercise Bài tập 09.10 (Số bất ngờ; Bài 4.5.1, MMDS §4.5.6, tr.149)
Tính số bất ngờ (mômen bậc hai) của dòng $3,1,4,1,3,4,2,1,2$. Mômen bậc ba của dòng này bằng bao nhiêu?
:::

::: hint
Lập bảng tần suất rồi áp Định nghĩa 09.1.
:::

::: solution
Tần suất: $f_1=3$ (vị trí 2, 4, 8), $f_2=2$ (7, 9), $f_3=2$ (1, 5), $f_4=2$ (3, 6). Do đó $F_2=9+4+4+4=21$ và $F_3=27+8+8+8=51$.

**Kiểm tra lại.** $3+2+2+2=9$, bằng độ dài dòng.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 09.11 (Ba hàm băm; Bài 4.4.1, MMDS §4.4.5, tr.145)
Dòng gồm các số nguyên $3,1,4,1,5,9,2,6,5$. Các hàm băm có dạng $h(x)=\alpha x+\beta\bmod32$, kết quả coi như số nhị phân 5 bit. Xác định độ dài đuôi của mỗi phần tử và ước lượng số phần tử phân biệt khi hàm băm là (a) $h(x)=2x+1\bmod32$; (b) $h(x)=3x+7\bmod32$; (c) $h(x)=4x\bmod32$.
:::

::: hint
Tính $h(x)$, viết 5 bit, đếm số bit 0 ở cuối; $R$ là số lớn nhất; ước lượng $2^R$ (Thuật toán 09.6).
:::

::: solution
| $x$ | 3 | 1 | 4 | 1 | 5 | 9 | 2 | 6 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| (a) $2x+1$ | $00111$ | $00011$ | $01001$ | $00011$ | $01011$ | $10011$ | $00101$ | $01101$ | $01011$ |
| đuôi (a) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| (b) $3x+7$ | $10000$ | $01010$ | $10011$ | $01010$ | $10110$ | $00010$ | $01101$ | $11001$ | $10110$ |
| đuôi (b) | 4 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 |
| (c) $4x$ | $01100$ | $00100$ | $10000$ | $00100$ | $10100$ | $00100$ | $01000$ | $11000$ | $10100$ |
| đuôi (c) | 2 | 2 | 4 | 2 | 2 | 2 | 3 | 3 | 2 |

(a) $R=0$, ước lượng $1$. (b) $R=4$, ước lượng $16$. (c) $R=4$, ước lượng $16$. Dòng có 7 phần tử phân biệt $\{1,2,3,4,5,6,9\}$, nên cả ba ước lượng đều sai xa. Ở (c), $h(9)=36\bmod32=4=h(1)$, nên hàm không đơn ánh.

**Kiểm tra lại.** $3\cdot3+7=16=10000_2$; $4\cdot4=16$.
:::

::: exercise Bài tập 09.12 (Giá trị các biến AMS; Bài 4.5.3, MMDS §4.5.6, tr.150)
Áp thuật toán AMS cho dòng $3,1,4,1,3,4,2,1,2$ của Bài tập 09.10 để ước lượng số bất ngờ. Với mỗi vị trí $i$, biến AMS bắt đầu ở vị trí $i$ có bộ đếm bằng bao nhiêu khi dòng kết thúc, và cho ước lượng nào?
:::

::: hint
Bộ đếm của biến bắt đầu ở $i$ là $v_i$ của Định nghĩa 09.19.
:::

::: solution
| $i$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| $x_i$ | 3 | 1 | 4 | 1 | 3 | 4 | 2 | 1 | 2 |
| $v_i$ | 2 | 3 | 2 | 2 | 1 | 1 | 2 | 1 | 1 |
| $9(2v_i-1)$ | 27 | 45 | 27 | 27 | 9 | 9 | 27 | 9 | 9 |

**Kiểm tra lại.** Tổng các ước lượng là 189, trung bình $189/9=21=F_2$, đúng Định lý 09.22.
:::

::: exercise Bài tập 09.13 (Mômen bậc ba; Bài 4.5.4, MMDS §4.5.6, tr.150)
Lặp lại Bài tập 09.12 khi các biến dùng để ước lượng mômen bậc ba. Giá trị mỗi biến khi dòng kết thúc là bao nhiêu? Mỗi biến cho ước lượng nào? Trung bình các ước lượng so với mômen bậc ba thật thế nào?
:::

::: hint
Giá trị biến không đổi; chỉ phép trả lời đổi thành $r(3v^2-3v+1)$ (Hệ quả 09.23).
:::

::: solution
Giá trị các biến vẫn là $2,3,2,2,1,1,2,1,1$. Với $r=9$: $v=1\mapsto9$, $v=2\mapsto9\cdot7=63$, $v=3\mapsto9\cdot19=171$. Các ước lượng theo vị trí: $63,171,63,63,9,9,63,9,9$, tổng 459, trung bình $51$, đúng bằng $F_3=51$ của Bài tập 09.10, vì trung bình trên mọi vị trí là kỳ vọng với $I$ đều.
:::

::: exercise Bài tập 09.14 (Tổng các số lẻ và mômen bậc bốn; Bài 4.5.5 và 4.5.6, MMDS §4.5.6, tr.150)
- (a) Chứng minh bằng quy nạp theo $f$ rằng $1+3+5+\cdots+(2f-1)=f^2$.
- (b) Muốn ước lượng mômen bậc bốn, phải đổi giá trị biến thành ước lượng như thế nào?
:::

::: hint
(a) Bổ đề 09.21. (b) Hệ quả 09.23 với $p=4$.
:::

::: solution
(a) Cơ sở $f=1$: $1=1^2$. Nếu tổng đến $2f-1$ bằng $f^2$, thì cộng thêm $2(f+1)-1=2f+1$ được $f^2+2f+1=(f+1)^2$.

(b) Với bộ đếm $v$, ước lượng là $r\bigl(v^4-(v-1)^4\bigr)=r(4v^3-6v^2+4v-1)$; nó không chệch vì $\sum_{v=1}^{f}\bigl(v^4-(v-1)^4\bigr)=f^4$ (tổng lồng nhau).
:::

::: exercise Bài tập 09.15 (Truy vấn trên Hình 4.2; Bài 4.6.1, MMDS §4.6.8, tr.157)
Cửa sổ như MMDS Hình 4.2, tức trạng thái của Ví dụ 09.14: các thùng (kích thước, mốc phải) $(1,r-1)$, $(1,r-2)$, $(2,r-4)$, $(4,r-8)$, $(4,r-14)$, $(8,r-22)$; hai mươi lăm bit cuối $1011011000101110110010110$. Ước lượng số bit 1 trong $k$ vị trí cuối với (a) $k=5$, (b) $k=15$. Mỗi ước lượng lệch bao nhiêu so với giá trị đúng?
:::

::: hint
Tìm $b^*$, thùng cũ nhất có mốc phải $\ge r-k+1$ (Thuật toán 09.45).
:::

::: solution
(a) $k=5$: các vị trí $r-4,\ldots,r$ là $10110$, có 3 bit 1. $b^*=(2,r-4)$; $T=1+1=2$; $\widehat y_5=2+2/2=3$. Đúng, sai lệch 0.

(b) $k=15$: các vị trí $r-14,\ldots,r$ là $101110110010110$, có 9 bit 1 ở $r-14$, $r-12$, $r-11$, $r-10$, $r-8$, $r-7$, $r-4$, $r-2$, $r-1$. $b^*=(4,r-14)$, chỉ mốc phải của nó trong hậu tố; $T=1+1+2+4=8$; $\widehat y_{15}=8+4/2=10$. Thừa 1, sai số tương đối $1/9\approx11\%$.

**Kiểm tra lại.** Cả hai sai số nằm trong cận 50% của Định lý 09.46; (b) là trường hợp ước lượng cao với $\pi=1$.
:::

::: exercise Bài tập 09.16 (Ba bit 1 nữa trên Hình 4.3; Bài 4.6.3, MMDS §4.6.8, tr.157)
Mô tả điều xảy ra với các thùng nếu ba bit 1 nữa đi vào cửa sổ biểu diễn ở MMDS Hình 4.3, tức các thùng (kích thước, mốc phải) từ cũ sang mới $(8,r-23)$, $(4,r-15)$, $(4,r-9)$, $(2,r-5)$, $(2,r-2)$, $(1,r)$. Có thể giả sử không bit 1 nào trong hình rời cửa sổ.
:::

::: hint
Trạng thái của Hình 4.3 là kết quả của Ví dụ 09.16. Áp Thuật toán 09.47 ba lần.
:::

::: solution
Đặt $r$ là vị trí bit mới nhất của Hình 4.3. Trạng thái đầu (kích thước, mốc phải), từ cũ sang mới: $(8,r-23)$, $(4,r-15)$, $(4,r-9)$, $(2,r-5)$, $(2,r-2)$, $(1,r)$. Giả sử ba bit 1 đến ở $r+1$, $r+2$, $r+3$; nếu xen bit 0, chỉ các mốc đổi.

1. **Bit ở $r+1$.** Tạo $(1,r+1)$; hai thùng cỡ 1, không gộp. Kích thước: $8,4,4,2,2,1,1$.
2. **Bit ở $r+2$.** Tạo $(1,r+2)$; ba thùng cỡ 1 nên gộp $(1,r)$ và $(1,r+1)$ thành $(2,r+1)$. Ba thùng cỡ 2 ($r-5$, $r-2$, $r+1$) nên gộp hai thùng cũ nhất thành $(4,r-2)$. Ba thùng cỡ 4 ($r-15$, $r-9$, $r-2$) nên gộp hai thùng cũ nhất thành $(8,r-9)$. Nay có hai thùng cỡ 8, mốc $r-23$ và $r-9$. Kích thước: $8,8,4,2,1$.
3. **Bit ở $r+3$.** Tạo $(1,r+3)$; hai thùng cỡ 1, không gộp. Trạng thái cuối: $(8,r-23)$, $(8,r-9)$, $(4,r-2)$, $(2,r+1)$, $(1,r+2)$, $(1,r+3)$.

Nhánh điều kiện: Hình 4.3 ghi "có ít nhất một thùng cỡ 8". Nếu phần không vẽ đã có thêm một thùng cỡ 8, thì ở bước 2 có ba thùng cỡ 8, hai thùng cũ nhất được gộp thành một thùng cỡ 16, và dây chuyền có thể lan tiếp tới các kích thước lớn hơn.

**Kiểm tra lại.** Phần nhìn thấy ngoài thùng cỡ 8 cũ có $4+4+2+2+1=13$ bit 1; thêm 3 thành $16=8+4+2+1+1$.
:::

### Mức vận dụng

::: exercise Bài tập 09.17 (Chọn hàm băm dạng $\alpha x+\beta\bmod2^L$; Bài 4.4.2, MMDS §4.4.5, tr.145)
Các hàm băm ở Bài tập 09.11 có vấn đề gì? Lời khuyên nào cho người định dùng hàm băm dạng $h(x)=\alpha x+\beta\bmod2^L$ (MMDS viết $ax+b\bmod2^k$)?
:::

::: hint
Xét bit thấp của $\alpha x$ khi $\alpha$ chẵn, rồi khi $\alpha$ lẻ, và so với giả thiết của Định lý 09.10.
:::

::: solution
**$\alpha$ chẵn.** Nếu $\alpha=2^{\sigma}\alpha'$ với $\alpha'$ lẻ và $\sigma\ge1$, thì $\sigma$ bit thấp của $h(x)$ bằng $\sigma$ bit thấp của $\beta$ với mọi $x$. Nếu $2^\sigma\nmid\beta$, mọi phần tử có cùng độ dài đuôi nhỏ hơn $\sigma$: câu (a) có $\sigma=1$, $\beta=1$, ước lượng luôn là 1. Nếu $2^\sigma\mid\beta$, mọi đuôi ít nhất $\sigma$: câu (c) có $\sigma=2$, $\beta=0$, ước lượng ít nhất 4 với mọi dòng. Cả hai vi phạm $\Pr[\rho\ge\ell]=2^{-\ell}$ của Bổ đề 09.9.

**$\alpha$ lẻ.** Khi đó $x\mapsto\alpha x+\beta\bmod2^L$ là song ánh, nên các phần tử phân biệt có giá trị băm phân biệt; nhưng điều đó chưa đủ. Vì $\alpha$ khả nghịch modulo $2^L$, $\alpha x+\beta\equiv\alpha(x+\tilde\beta)$ với $\tilde\beta=\alpha^{-1}\beta$, và nhân với số lẻ không đổi số bit 0 ở cuối, nên $\rho(h(x))=\rho((x+\tilde\beta)\bmod2^L)$. Hai phần tử cùng số dư theo $2^j$ có cùng độ dài đuôi khi độ dài này nhỏ hơn $j$, nên giả thiết độc lập của Định lý 09.10 không thỏa trên dữ liệu có cấu trúc: ví dụ, nếu mọi phần tử của dòng là bội của $1\,024$, mọi giá trị băm có cùng 10 bit thấp, nên với xác suất $1-2^{-10}$ theo phép chọn $\beta$, mọi phần tử có cùng độ dài đuôi nhỏ hơn 10 và ước lượng không vượt $2^9=512$ dù $d$ lớn.

**Lời khuyên.** Chọn $\alpha$ lẻ và $2^L$ vượt cỡ tập vũ trụ (MMDS tr.143); dù vậy, họ này chỉ xấp xỉ mô hình băm lý tưởng khi dữ liệu không có cấu trúc theo các bit thấp.
:::

::: exercise Bài tập 09.18 (Số bất ngờ nhỏ nhất và lớn nhất; Bài 4.5.2, MMDS §4.5.6, tr.150)
Một dòng có $r$ phần tử, trong đó $d$ phần tử phân biệt. Số bất ngờ nhỏ nhất và lớn nhất có thể là bao nhiêu, theo $d$ và $r$? Kiểm với Ví dụ 09.2 và với dòng mười lăm phần tử.
:::

::: hint
Mỗi phần tử phân biệt xuất hiện ít nhất một lần. So $F_2$ trước và sau khi chuyển một lần xuất hiện từ phần tử này sang phần tử khác.
:::

::: solution
**Phép chuyển.** Chuyển một lần xuất hiện từ phần tử có tần suất $\phi$ sang phần tử có tần suất $\psi$ đổi $F_2$ một lượng $(\phi-1)^2+(\psi+1)^2-\phi^2-\psi^2=2(\psi-\phi)+2$.

**Lớn nhất.** Nếu $\psi\ge\phi\ge2$, phép chuyển làm $F_2$ tăng, và vẫn giữ $d$ phần tử phân biệt. Lặp lại tới khi mọi phần tử trừ một có tần suất 1: $F_2^{\max}=(r-d+1)^2+(d-1)$.

**Nhỏ nhất.** Nếu $\phi\ge\psi+2$, phép chuyển làm $F_2$ giảm $2(\phi-\psi-1)>0$. Do đó ở cực tiểu, mọi tần suất hơn kém nhau nhiều nhất 1. Viết $r=Qd+Q'$ với $0\le Q'<d$: $Q'$ phần tử xuất hiện $Q+1$ lần, $d-Q'$ phần tử $Q$ lần, và $F_2^{\min}=Q'(Q+1)^2+(d-Q')Q^2$.

**Kiểm tra lại.** $r=100$, $d=11$: $Q=9$, $Q'=1$, $F_2^{\min}=100+10\cdot81=910$, $F_2^{\max}=90^2+10=8\,110$, khớp Ví dụ 09.2. $r=15$, $d=4$: $Q=3$, $Q'=3$, $F_2^{\min}=3\cdot16+9=57$, $F_2^{\max}=12^2+3=147$, và $57\le59\le147$.
:::

::: exercise Bài tập 09.19 (Vì sao ngưỡng không bằng 1 hay 2)
Trong Thuật toán 09.55, vì sao không chọn ngưỡng $\theta=1$ hay $\theta=2$? Với $c=1/2$, chạy năm phần tử đầu $\mathrm a,\mathrm b,\mathrm c,\mathrm b,\mathrm d$ với $\theta=1$ và cho biết phần tử nào còn được theo dõi sau bước 5.
:::

::: hint
Điểm của phần tử vừa tạo bằng 1; xem Bước 4 của chứng minh Định lý 09.56.
:::

::: solution
Với $\theta=2$, phần tử mới bị xóa ngay. Với $\theta=1$, nó bị xóa ở bước kế tiếp, khi điểm thành $1-c<1$, trừ khi xuất hiện lại ngay. Trên năm phần tử với $c=1/2$: bước 1 giữ $\mathrm a:1$; bước 2 xóa $\mathrm a$ ($1/2$), giữ $\mathrm b:1$; bước 3 xóa $\mathrm b$, giữ $\mathrm c:1$; bước 4 xóa $\mathrm c$, tạo lại $\mathrm b:1$; bước 5 xóa $\mathrm b$, giữ $\mathrm d:1$. Sau bước 5 chỉ còn $\mathrm d$, phần tử vừa đến: thuật toán chỉ nhớ phần tử cuối cùng.
:::

<!-- note-topic-id: lec-09-topic-27 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, Chương 4. §4.4, tr.142–145: Mục 2 (Ví dụ 4.5) và Bài tập 09.11, 09.17. §4.5, tr.145–150: Mục 1 (Ví dụ 4.6, 4.7), Mục 3 (Ví dụ 4.7–4.9) và Bài tập 09.10, 09.12–09.14, 09.18. §4.6, tr.150–157: Mục 5 (Hình 4.2, 4.3, Ví dụ 4.10–4.13) và Bài tập 09.15, 09.16. §4.7, tr.157–159: Mục 6. §4.1.2, tr.133: Mục 1; §4.8, tr.160: Nhận xét 09.28. Sách và trang chiếu tại [http://www.mmds.org](http://www.mmds.org); phần lớn sườn, ví dụ và bài tập của chương dựa trên nguồn này.
- Leskovec, J., Rajaraman, A. và Ullman, J. D., trang chiếu chương 4, *Mining Data Streams* phần 1 và 2 (tại [http://www.mmds.org](http://www.mmds.org)). Phần 1, tr.29–32: ý tưởng thùng của DGIM ở Mục 5.2. Phần 2, tr.18: phần Ứng dụng; tr.20: ví dụ độ dài đuôi ở Mục 2.2.
- Ullman, J. D. (2017). Stanford CS246, *Streams 1*, tr.13: bài toán URL với $N=10^9$ ở Mục 5 và Tình huống 09.2; tr.23: cận 50%; tr.28: ví dụ dòng mưa ở Mục 6.1. *Streams 2*, tr.24: số trang liên kết tới mỗi trang; tr.32–38: cỡ lân cận trong đồ thị (Tình huống 09.1); tr.49: số biến AMS.
- Musco, C. (2021). UMass CS514, bài 10, *Count-Min Sketch*, trang chiếu 8–19: toàn bộ Mục 4. Bài 8, trang chiếu 3–5 và 8: mẹo trung vị (Bổ đề 09.14), phác thảo hợp nhất được.
- Blum, A., Hopcroft, J. và Kannan, R., *Foundations of Data Science*, bản ngày 04/01/2018. §6.2.1, tr.183: cận dưới cho đếm chính xác (Nhận xét 09.4); tr.184–185: họ độc lập từng cặp (Định nghĩa 09.31); Định lý 2.1, tr.13: bất đẳng thức Markov; §12.3, tr.408 và §12.5.3, tr.422: cấp số nhân và cận hợp ở phần tiên quyết.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press, §2.1 (bất biến vòng lặp) và Chương 16 (phân tích khấu hao): cách trình bày Định lý 09.48 và Mệnh đề 09.49(b). Chương 11 (băm phổ dụng): họ băm phổ dụng có miền giá trị nhỏ cho các hàng Count-Min.
- Đọc thêm, không cần cho bài tập: HyperLogLog (UMass bài 8, trang chiếu 6–8); ước lượng $F_0$ bằng giá trị băm nhỏ nhất, thuật toán Frequent và phân tích phương sai của một ước lượng $F_2$ khác (BHK §6.2.1, §6.2.3, §6.2.4, tr.185–191); tập phần tử phổ biến trong cửa sổ suy giảm (trang chiếu MMDS, phần 2, tr.44–46).
- Đọc tiếp: [Bài 10](lecture-10-nen-du-lieu-khong-mat-thong-tin.html), *Nén dữ liệu không mất thông tin*.
- Ghi chú Bài 08, Bài 06 (Định lý 06.7) và Bài 05 (Mục 8–10): các kết quả nhắc lại ở phần kiến thức tiên quyết.
