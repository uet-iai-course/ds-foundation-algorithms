# Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc

Máy tìm kiếm nhận vài trăm triệu truy vấn mỗi ngày (MMDS §4.1.2, tr.133). Các truy vấn đến thành một dòng không biết trước độ dài, mỗi phần tử chỉ được đọc một lần, và bộ nhớ làm việc không giữ được toàn bộ lịch sử. Hai bài toán trên những dòng như vậy, giữ mẫu truy vấn và lọc thư đến, đã được đặt ở ghi chú Bài 01 nhưng chưa có thuật toán. Trong chương này, chúng ta xây ba cấu trúc chỉ đọc dòng một lượt cho ba loại câu hỏi. Lấy mẫu theo khóa phục vụ thống kê theo người dùng khi chỉ lưu được $1/10$ dòng (§4.2.1, tr.136); trạng thái quyết định của nó có cỡ hằng, nhưng mẫu tăng theo dòng, với kỳ vọng khoảng một phần mười số bộ đã đọc. Lấy mẫu hồ chứa giữ một mẫu có số phần tử cố định, trong đó mọi phần tử đã đọc có cùng cơ hội có mặt. Bloom filter trả lời câu hỏi thành viên cho tập $10^9$ địa chỉ được phép bằng một mảng bit cố định trong 1 GB bộ nhớ (§4.3.1, tr.139). Với mỗi cấu trúc, chúng ta nêu giả thiết, chứng minh bảo đảm và đếm chi phí.

[Bộ trang chiếu Bài 08](lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html) trình bày cùng ký hiệu và dữ kiện.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đặc tả thuật toán dòng một lượt và chọn khóa lấy mẫu cho một thống kê theo nhóm.
   - Viết đầu vào, trạng thái, phép cập nhật, đầu ra của một thuật toán dòng và đo nó theo bốn đại lượng chi phí (Mục 1).
   - Tính sai lệch của lấy mẫu từng bộ, chọn khóa nhận diện đúng đơn vị thống kê, chạy lấy mẫu theo khóa và chứng minh mọi bộ cùng khóa nhận cùng quyết định, kể cả khi hạ ngưỡng băm (Mục 2).
2. Chạy tay lấy mẫu hồ chứa (reservoir sampling) có sức chứa $s$ và chứng minh bằng quy nạp rằng, sau khi đọc $r\ge s$ phần tử, mỗi phần tử đã đọc còn trong mẫu với xác suất $s/r$.
   - Lập vết chạy khi biết các số ngẫu nhiên đã sinh; trình bày đủ bước cơ sở, bước quy nạp và chỗ dùng giả thiết về số ngẫu nhiên; nêu chi phí bộ nhớ và thời gian mỗi phần tử (Mục 3).
3. Xây và truy vấn Bloom filter (còn gọi là bộ lọc Bloom) gồm $n$ bit, $k$ hàm băm và tập $S$ gồm $m$ khóa; tính xác suất nhận nhầm một khóa ngoài $S$ và số hàm băm tối ưu.
   - Đặt bit và trả lời truy vấn trên một mảng 11 bit; chứng minh khóa đã chèn không bị loại khi bốn điều kiện được giữ: không xóa hay đặt lại bit, truy vấn dùng đúng các hàm băm và mảng đã xây, các hàm băm tất định, mọi phép ghi bit đã xong (Mục 4).
   - Tính mật độ bit 1, xác suất nhận nhầm và dạng mũ $(1-e^{-km/n})^k$; dẫn xuất $k^*=(n/m)\ln2$ và chọn số hàm băm nguyên (Mục 4; Bài tập 08.10–08.12, tức các bài 4.3.1–4.3.3 của MMDS).

Ở Mục 5 và các tình huống áp dụng, ba mục tiêu được dùng cùng lúc để chọn cấu trúc theo câu hỏi cần trả lời.

<!-- note-topic-id: lec-08-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `06.k` chỉ ghi chú Bài 06. Ghi chú Bài 01 và Bài 05 chưa đánh số hiệu, nên các kết quả của hai bài đó được dẫn theo mục. Mỗi kết quả được phát biểu lại dưới đây; các chữ $c$, $c_0$, $z$, $Z$, $g$, $\alpha$, $\beta$ trong phần này là biến tạm, không mang nghĩa của bảng ký hiệu.

- **Hai bài toán dòng của Bài 01** (ghi chú Bài 01, mục "Xử lý dòng dữ liệu, lưu trữ và truy vấn"). Bài toán thứ nhất cần một mẫu của nhật ký (người dùng, truy vấn, thời gian) vẫn đo được mức lặp truy vấn của từng người, nên đơn vị lấy mẫu là người dùng. Bài toán thứ hai nhận thư có địa chỉ gửi thuộc danh sách cho phép và bỏ thư còn lại; khi danh sách vượt bộ nhớ, mỗi thư có thể cần một lần tra đĩa.
- **Hàm băm là hàm tất định** (ghi chú Bài 05, Mục 9). Một hàm băm đã chọn cho cùng giá trị trên cùng đầu vào, ở mọi lần gọi và trên mọi máy dùng hàm đó. Tính ngẫu nhiên, nếu có, đến từ phép chọn hàm trong một họ hàm, không đến từ từng lần gọi; tính đều của phép chọn là một giả thiết riêng, được nêu tại từng kết quả cần đến nó. Ở Bài 02, hàm phân phối của MapReduce dựa trên cùng tính chất: mọi tác vụ Map dùng chung một hàm, nên mọi cặp cùng khóa về cùng một tác vụ Reduce.
- **Phân tích xác suất thành ứng viên** (Định lý 06.7). Khi các hàm MinHash được chọn độc lập, xác suất một cặp tài liệu thành ứng viên được tính theo bốn bước: xác suất trùng ở một hàng; tích các xác suất độc lập cho xác suất trùng cả một dải; tích lần nữa trên các dải độc lập cho xác suất không dải nào trùng; rồi lấy biến cố bù. MMDS (§4.3.3, tr.140) nêu rằng phân tích Bloom filter đi theo cùng cách làm với phân tích phân dải ở §3.4.2; bước tích thứ hai ứng với biến cố không phép băm nào rơi vào một bit cho trước.
- **Công cụ xác suất** (học phần Xác suất thống kê; ghi chú Bài 01, mục "Mô hình ngẫu nhiên và giới hạn suy luận"; ghi chú Bài 05, Mục 7). Biến cố bù: $\Pr(\overline E)=1-\Pr(E)$. Với các biến cố $E_1,\ldots,E_c$ độc lập (toàn phần, không chỉ từng đôi), $\Pr(E_1\cap\cdots\cap E_c)=\Pr(E_1)\cdots\Pr(E_c)$. Quy tắc nhân: $\Pr(E\cap F)=\Pr(E)\Pr(F\mid E)$ khi $\Pr(E)>0$. Tuyến tính kỳ vọng: kỳ vọng của tổng bằng tổng các kỳ vọng, không cần độc lập; $\mathbb E[\mathbf 1[E]]=\Pr(E)$.
- **Bất đẳng thức Jensen** (học phần Xác suất thống kê; đã dùng ở Tình huống 06.2). Với hàm $g$ lồi trên một khoảng chứa mọi giá trị của biến ngẫu nhiên $Z$, $\mathbb E[g(Z)]\ge g(\mathbb E[Z])$; với $g$ lõm, bất đẳng thức đổi chiều.
- **Giới hạn của $(1-1/c)^c$** (MMDS §1.3.5; học phần Giải tích). Khi số nguyên $c$ tăng, $(1-1/c)^c$ tăng và tiến tới $e^{-1}\approx0{,}3679$; do đó với $c$ lớn và $z>0$ cố định, $(1-1/c)^{zc}\approx e^{-z}$.
- **Ba bất đẳng thức một biến** (học phần Giải tích). Với mọi số thực $z$, $1-z\le e^{-z}$; lấy $z=1/c$, $c\ge1$, rồi nâng hai vế không âm lên lũy thừa $c$ được $(1-1/c)^c\le e^{-1}$. Bất đẳng thức Bernoulli: $(1-z)^c\ge1-cz$ với $0\le z\le1$ và $c$ nguyên dương. Nếu $g$ liên tục trên $[\alpha,\beta]$, có $g''<0$ trên $(\alpha,\beta)$ và $g(\alpha)=g(\beta)=0$, thì $g>0$ trên $(\alpha,\beta)$, vì một hàm lõm chặt nằm trên dây cung nối hai đầu.
- **Đạo hàm và cực trị** (học phần Giải tích). Nếu $g$ khả vi trên $(\alpha,\beta)$, $g'<0$ trên $(\alpha,c_0)$ và $g'>0$ trên $(c_0,\beta)$, thì $g$ đạt giá trị nhỏ nhất trên $(\alpha,\beta)$ tại $c_0$. Vì $(\ln g)'=g'/g$ khi $g>0$, hai hàm $g$ và $\ln g$ có cùng điểm cực tiểu.
- **Quy nạp và bất biến vòng lặp** (ghi chú Bài 05, Mục 10; chứng minh Mệnh đề 06.5). Một khẳng định đúng cho mọi số nguyên $c\ge c_0$ khi nó đúng cho $c_0$ và đúng cho $c+1$ mỗi khi đúng cho $c$. Bất biến vòng lặp đúng trước lượt đầu (khởi tạo), được giữ qua mỗi lượt (duy trì) và cho điều cần chứng minh khi vòng lặp dừng (kết thúc).

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một chứng minh được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $x_1,x_2,\ldots$; $x_i$ | các phần tử của dòng theo thứ tự đến; phần tử ở vị trí $i$ | phần tử của miền dữ liệu; $i\ge1$ |
| $r$ | số phần tử đã đọc, tính cả phần tử vừa đến | số nguyên không âm |
| $t$ | một phần tử của dòng truy vấn, là bộ (người dùng, truy vấn, thời gian); khi cần chỉ số, $t=x_i$ | bộ nhiều thành phần |
| $\mathcal K$; $K$; $K(t)$ | miền khóa; một giá trị khóa; khóa của bộ $t$, gồm các thành phần nhận diện đơn vị thống kê | tập; phần tử của $\mathcal K$ |
| $u$; $d$ | số truy vấn khác nhau mà một người dùng gửi đúng một lần; đúng hai lần | số nguyên không âm |
| $h$ | hàm băm dùng để lấy mẫu theo khóa, cố định sau khi chọn | $\mathcal K\to\{0,\ldots,b-1\}$ |
| $b$; $a$ | số ngăn, tức số giá trị của $h$; ngưỡng, bộ $t$ được chọn khi $h(K(t))<a$, tỷ lệ $a/b$ | số nguyên, $b\ge1$, $0\le a\le b$ |
| $\tau$ | ngưỡng băm khi điều chỉnh tỷ lệ: bộ được nhận khi $h(K(t))\le\tau$, ứng với $a=\tau+1$ | số nguyên, $-1\le\tau\le b-1$ |
| $s$ | sức chứa của hồ chứa | số nguyên, $s\ge1$ |
| $W[1..s]$ | mảng hồ chứa, giữ mẫu hiện tại | mảng $s$ ô, mỗi ô chứa một phần tử của dòng |
| $j$ | số ngẫu nhiên sinh khi phần tử thứ $r>s$ đến | số nguyên đều trên $\{1,\ldots,r\}$ |
| $S$; $m$ | tập khóa được chèn vào Bloom filter; số khóa, $m=\lvert S\rvert$ | tập hữu hạn, $S\subseteq\mathcal K$; số nguyên dương |
| $v$ | một khóa được chèn vào Bloom filter, $v\in S$ | phần tử của $\mathcal K$ |
| $n$; $B[0..n-1]$ | số bit của Bloom filter; mảng bit | số nguyên dương; $\{0,1\}^n$ |
| $k$; $h_1,\ldots,h_k$ | số hàm băm của Bloom filter; các hàm băm | số nguyên dương; $\mathcal K\to\{0,\ldots,n-1\}$ |
| $y$ | khóa được truy vấn ở Bloom filter | phần tử của $\mathcal K$ |
| $X$ | số bit bằng 1 của mảng sau khi chèn $S$ | biến ngẫu nhiên trên $\{0,\ldots,n\}$ |
| $q$ | mật độ bit 1 kỳ vọng, $q=\mathbb E[X]/n=1-(1-1/n)^{km}$ khi $km$ phép băm đều và độc lập | $[0,1]$ |
| $p_{FP}$ | xác suất dương giả (false positive): một khóa $y\notin S$ cố định nhận câu trả lời "có thể thuộc" | $[0,1]$ |
| $p(k)$ | dạng mũ $(1-e^{-km/n})^k$, xét như hàm của $k$ | $(0,1)$, với $k>0$ thực |
| $k^*$ | điểm cực tiểu của $p(k)$ trên $k>0$, $k^*=(n/m)\ln2$ | số thực dương |
| $\Pr$; $\mathbb E$; $\mathbf 1[E]$ | xác suất; kỳ vọng; biến chỉ báo của biến cố $E$. Chỉ số dưới nêu nguồn ngẫu nhiên khi cần, như $\Pr_h$ | $[0,1]$; số thực; $\{0,1\}$ |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $0{,}0216$. Số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $1\,000$, hoặc viết dạng lũy thừa, ví dụ $8\cdot10^9$. Ký hiệu $\ln$ là logarit cơ số $e$.
- Vị trí trên dòng và ô của hồ chứa đánh số từ $1$; bit của mảng Bloom và giá trị băm đánh số từ $0$.
- Chữ thường và chữ hoa là hai ký hiệu khác nhau: $k$ là số hàm băm, $K$ là khóa; $b$ là số giá trị của $h$, $B$ là mảng bit.
- Ký hiệu cục bộ chỉ dùng trong một mục và được giới thiệu tại chỗ: $M$, $T$, $V_r$ (Mục 1); $G$ (Mục 2.5); $W_r$, $E_i$, $A$, $\ell$ (Mục 3); $\rho$, $z$, $\theta$, $\lambda$, $\phi$ (Mục 4). Ngoài phần tiên quyết, chữ $c$ luôn chỉ một giá trị của hàm băm: giá trị $h(K)$ ở Mục 2, vị trí bit $h_i(v)$ ở Mục 4. Chữ $\eta$, có hoặc không có chỉ số, chỉ một xác suất giữ một phần tử của mẫu (Mục 2.1, 3.5 và Bài tập 08.6).
- Tên phần tử trong vết chạy hồ chứa viết chữ đứng, như dòng a, x, c, y, z của trang chiếu MMDS (slide), để không lẫn với các ký hiệu nghiêng $a$, $x_i$, $y$.
- Ký hiệu khác MMDS ở bốn chỗ, vì các chữ của sách đã mang nghĩa khác trong bảng: số truy vấn xuất hiện một lần $s$ (§4.2.1) viết là $u$; số giá trị băm $B$ và ngưỡng $t$ (§4.2.4) viết là $b$ và $\tau$; số đích $x$ và số phi tiêu $y$ (§4.3.3) là $n$ bit và $km$ phép băm; mẫu $S$ và số phần tử đã thấy $n$ trên trang chiếu hồ chứa viết là $W$ và $r$.
- Số liệu lấy từ MMDS: Hình 4.1, các Ví dụ 4.1, 4.3, 4.4, ngân sách $1/10$ dòng ở §4.2.1, các bài 4.2.1 và 4.3.1–4.3.3. Mảng 11 bit với các khóa 25, 159, 585 và truy vấn 118 lấy từ trang chiếu của Ullman cho học phần CS246 (2017). Giá trị băm của An, Bình, Chi, dãy số ngẫu nhiên của vết hồ chứa, các khóa truy vấn khác trên mảng 11 bit và dữ kiện các bài tập không mang số bài sách do học phần dựng để minh họa. Khi số in trong sách khác phép tính lại, giá trị tính lại được dùng và chỗ khác được nêu tại chỗ.

## Bản đồ chủ đề

Nhóm **cốt lõi** tạo mạch chính; **cầu nối** phát biểu lại tiên quyết hoặc nối hai bước suy luận; **bổ sung** lấp một khoảng trống của nguồn; **đọc thêm** không cần để đạt mục tiêu.

| Chủ đề (mã) | Nhóm | Mục | Vai trò → sản phẩm dùng tiếp |
|---|---|---|---|
| Kiến thức tiên quyết (`lec-08-topic-01`) | cầu nối | Tiên quyết | Kết quả dùng lại từ Bài 01, 05, 06, công cụ xác suất, giải tích, quy nạp → Mục 1–4 |
| Mô hình dòng một lượt (`lec-08-topic-02`) | cốt lõi | 1.1–1.6 | Trạng thái, phép cập nhật, truy vấn, bốn đại lượng chi phí → đặc tả chung của ba cấu trúc |
| Sai lệch của lấy mẫu từng bộ (`lec-08-topic-03`) | cốt lõi | 2.1 | Tỷ số $d/(10u+19d)$ so với $d/(u+d)$ → nhu cầu lấy mẫu theo đơn vị thống kê |
| Mẫu nhất quán theo khóa (`lec-08-topic-04`) | cốt lõi; kích thước mẫu kỳ vọng là bổ sung | 2.2, 2.4 | Quy tắc $h(K(t))<a$, tính nhất quán, xác suất $a/b$, cỡ mẫu kỳ vọng → giới hạn về cỡ mẫu |
| Chọn khóa theo đơn vị thống kê (`lec-08-topic-05`) | cốt lõi | 2.3 | Quy trình ba bước, ba lựa chọn khóa → Bài tập 4.2.1 của MMDS |
| Ngưỡng băm khi ngân sách cố định (`lec-08-topic-06`) | cầu nối | 2.5 | Hạ ngưỡng $\tau$, bất biến của mẫu → nhu cầu mẫu cỡ cố định |
| Đặc tả và thuật toán hồ chứa (`lec-08-topic-07`) | cốt lõi | 3.1–3.2 | Mẫu cỡ $s$, vết chạy với $s=2$, giả mã → định lý xác suất |
| Xác suất $s/r$ và chi phí hồ chứa (`lec-08-topic-08`) | cốt lõi; mọi tập con đồng khả năng và số lần ghi kỳ vọng là bổ sung | 3.3–3.5 | Chứng minh quy nạp, chi phí → so sánh với mẫu theo khóa |
| Cơ chế Bloom filter (`lec-08-topic-09`) | cốt lõi | 4.1–4.3 | $10^9$ địa chỉ trong 1 GB, ví dụ 11 bit, xây và truy vấn → bảo đảm |
| Không âm giả (`lec-08-topic-10`) | cốt lõi | 4.4 | Bốn điều kiện, phản ví dụ khi xóa bit → phân tích dương giả |
| Mật độ bit và xác suất dương giả (`lec-08-topic-11`) | cốt lõi; cận dưới $q^k\le p_{FP}$ là bổ sung | 4.5 | $q$ chính xác, xấp xỉ $q^k$, dạng mũ → hàm $p(k)$ |
| Số hàm băm tối ưu (`lec-08-topic-12`) | cốt lõi | 4.6–4.7 | $k^*=(n/m)\ln2$, chọn $k$ nguyên → định cỡ Bloom filter |
| Chọn cấu trúc theo câu hỏi (`lec-08-topic-13`) | cốt lõi | 5.1–5.2 | Kết quả, giả thiết, bảo đảm, chi phí; trả lời vấn đề trung tâm → tình huống áp dụng |
| Tình huống áp dụng và ứng dụng (`lec-08-topic-14`) | cốt lõi | Tình huống | Ba bài toán giải trọn, một tình huống vi phạm giả thiết; ứng dụng ở Bài 09 → tóm tắt |
| Tóm tắt chương (`lec-08-topic-15`) | cốt lõi | Tóm tắt | Chuỗi kết quả, giả thiết hay bị bỏ quên → Bài 09 |
| Bài tập củng cố (`lec-08-topic-16`) | cốt lõi | Bài tập | Ba mức, gồm bốn bài MMDS → kiểm ba mục tiêu |
| Đọc thêm và tài liệu (`lec-08-topic-17`) | đọc thêm | Tham khảo | Ánh xạ mục ↔ nguồn, lấy mẫu có trọng số, Bài 09 |

Quan hệ tiên quyết giữa các mục như sau. Mô hình dòng một lượt (Mục 1) dùng phần tiên quyết và là đầu vào của cả ba nhánh. Nhánh lấy mẫu theo khóa đi tuần tự qua Mục 2.1–2.5. Nhánh hồ chứa gồm đặc tả và thuật toán (Mục 3.1–3.2) rồi xác suất $s/r$ và chi phí (Mục 3.3–3.5); phần sau cần quy nạp ở tiên quyết và so kết quả với mẫu nhất quán theo khóa (Mục 2.2). Nhánh Bloom filter đi tuần tự qua Mục 4.1–4.7 và cần giới hạn của $(1-1/c)^c$, bất đẳng thức Jensen cùng phần đạo hàm ở tiên quyết. Ba nhánh gặp nhau ở Mục 5, rồi đi qua tình huống áp dụng và tóm tắt chương; bài tập củng cố dùng mọi mục trước. Đếm số phần tử phân biệt, mômen và cửa sổ thời gian thuộc Bài 09.

<!-- note-topic-id: lec-08-topic-02 -->
## 1. Mô hình dòng một lượt

Ghi chú Bài 01 (mục "Xử lý dòng dữ liệu, lưu trữ và truy vấn") đặt hai bài toán trên dòng: giữ một mẫu nhật ký truy vấn vẫn đo được mức lặp của từng người dùng, và lọc thư theo danh sách địa chỉ cho phép khi danh sách vượt bộ nhớ; ghi chú đó chưa đưa ra thuật toán. Với vài trăm triệu truy vấn mỗi ngày (MMDS §4.1.2, tr.133) và $10^9$ địa chỉ được phép trong 1 GB bộ nhớ (§4.3.1, tr.139), không thể lưu cả dòng rồi xử lý. Chúng ta xây một mô hình chung cho thuật toán dòng (Mục 1), ba cấu trúc trên mô hình đó (Mục 2–4) và một quy trình chọn giữa chúng (Mục 5).

![Sơ đồ cấu trúc chương đọc từ trên xuống: khối Mục 1, mô hình dòng một lượt, đọc một lần và trả lời từ trạng thái; ba mũi tên xuống ba khối song song: Mục 2 lấy mẫu theo khóa, câu hỏi thống kê theo nhóm, bảo đảm giữ trọn từng khóa với xác suất a/b mỗi khóa; Mục 3 lấy mẫu hồ chứa, câu hỏi mẫu có cỡ cố định, bảo đảm đúng s phần tử với xác suất s/r mỗi phần tử; Mục 4 Bloom filter, câu hỏi khóa có thuộc tập không, bảo đảm không âm giả và dương giả xấp xỉ p(k); ba mũi tên hội tụ vào khối Mục 5, chọn cấu trúc theo câu hỏi dựa trên đầu ra, giả thiết và chi phí.](img/lec-08/cau-truc-chuong.svg)

Hình đọc từ trên xuống. Khối trên cùng là đặc tả chung mà mọi cấu trúc phải thỏa. Ba khối giữa là ba cấu trúc, mỗi khối ghi câu hỏi nó trả lời và bảo đảm chính sẽ được chứng minh: Mệnh đề 08.10 cho mẫu theo khóa, Định lý 08.17 cho hồ chứa, Định lý 08.25 và Mệnh đề 08.27 cho Bloom filter. Ba nhánh không phụ thuộc nhau, nên có thể đọc theo thứ tự bất kỳ sau Mục 1; chúng gặp lại ở khối dưới cùng, nơi Mục 5 đặt ba bảo đảm cạnh nhau.

Một triệu cảm biến đo độ cao mặt biển, mỗi cảm biến gửi 10 số đo 4 byte mỗi giây, tạo $10^6\cdot10\cdot4\cdot86\,400\approx3{,}46\cdot10^{12}$ byte mỗi ngày, được sách làm tròn thành 3,5 TB (MMDS §4.1.2, tr.133). Số đo không được xử lý khi đến thì chỉ còn trong kho lưu trữ (archival store), nơi quá chậm để trả lời truy vấn (§4.1.1, tr.132). Ở Bài 02, trung bình cộng được tính bằng cặp (tổng, số lượng) thay cho danh sách các số, nhưng dữ liệu nằm trên đĩa và đọc lại được. Trên dòng, chúng ta phải chọn trước khi phần tử đầu tiên đến: giữ trạng thái nào cho truy vấn đã định, trạng thái ấy tốn bao nhiêu bộ nhớ, mỗi phần tử tốn bao nhiêu phép toán.

### 1.1 Trạng thái theo truy vấn

Chúng ta tính ba truy vấn trên một dòng ngắn và ghi phần dữ liệu mỗi truy vấn phải giữ.

::: example Ví dụ 08.1 (Ba truy vấn trên dòng cảm biến)
**Dữ kiện.** Một cảm biến gửi dòng $1,5,2,7,4,0,3,5$, theo thứ tự đến này. Dãy số là dòng đầu của MMDS Hình 4.1 (tr.132); ba truy vấn lấy từ Ví dụ 4.1 (tr.134), vốn viết cho một cảm biến nhiệt độ.

**Tính.**

| Truy vấn | Phần cần giữ | Câu trả lời sau 8 số |
|---|---|---|
| giá trị lớn nhất | giá trị lớn nhất đã gặp | $7$ |
| trung bình mọi số | tổng và số đếm | $27/8=3{,}375$ |
| trung bình 24 số gần nhất | 24 số gần nhất | $27/8$, vì mới có 8 số |

Khi số mới đến, truy vấn thứ nhất so nó với giá trị đang giữ; truy vấn thứ hai cộng nó vào tổng và tăng số đếm; truy vấn thứ ba thêm nó vào danh sách và, khi đã đủ 24 số, bỏ số cũ nhất.

**Kiểm tra lại.** $1+5+2+7+4+0+3+5=27$; số lớn nhất là $7$.
:::

Một cách trực quan, một thuật toán dòng là một trạng thái nhỏ được cập nhật khi từng phần tử đi qua, và trạng thái đó do truy vấn quyết định. Không truy vấn nào cần cả lịch sử: hai truy vấn đầu giữ một hoặc hai số dù dòng dài bao nhiêu, truy vấn thứ ba giữ không quá 24 số. Ngược lại, câu hỏi "số đo thứ ba là bao nhiêu" không trả lời được từ ba trạng thái trên, vì số $2$ đã bị bỏ khi đến. Trạng thái được chọn theo truy vấn, trước khi dòng đến.

::: definition Định nghĩa 08.1 (Thuật toán dòng một lượt)
Một **dòng** là dãy phần tử $x_1,x_2,\ldots$ đến lần lượt; độ dài không biết trước, và hệ thống không điều khiển nhịp đến. Ký hiệu $r$ là số phần tử đã đọc, tính cả phần tử vừa đến.

Một **thuật toán dòng một lượt** gồm:

- một **trạng thái** ban đầu, là dữ liệu thuật toán giữ trước khi đọc phần tử nào;
- một **phép cập nhật**, nhận trạng thái sau $r-1$ phần tử cùng $x_r$ và trả trạng thái sau $r$ phần tử;
- một **phép trả lời**, nhận trạng thái hiện tại cùng một truy vấn và trả câu trả lời.

Mỗi phần tử được đọc đúng một lần, khi nó đến. Trạng thái nằm trong **bộ nhớ làm việc** (working store), có dung lượng giới hạn, nhỏ hơn lịch sử $x_1,\ldots,x_r$ khi $r$ lớn. Dòng có thể được ghi vào **kho lưu trữ**, nhưng kho này không được đọc để trả lời.

Một **truy vấn thường trực** (standing query) được đăng ký trước và cho câu trả lời vào thời điểm định trước, chẳng hạn mỗi khi có phần tử mới; một **truy vấn tức thời** (ad-hoc query) được hỏi một lần, về trạng thái tại lúc hỏi.
:::

Phép cập nhật chỉ thấy phần tử vừa đến và trạng thái, nên thông tin cần về các phần tử trước phải đã nằm trong trạng thái. Phép trả lời chỉ thấy trạng thái, nên truy vấn không tính được từ trạng thái thì không có câu trả lời, kể cả khi dòng còn trong kho. Giả thiết về bộ nhớ loại bỏ phương án chép cả dòng.

Ví dụ 08.1 thỏa định nghĩa: ba truy vấn là truy vấn thường trực, cột "Phần cần giữ" là trạng thái, câu dưới bảng là phép cập nhật. Với truy vấn tức thời, chỉ chuẩn bị được trạng thái cho những loại câu hỏi đoán trước (MMDS §4.1.3, tr.134). Hệ quản trị cơ sở dữ liệu tự quyết tốc độ đọc đĩa (§4.1.1, tr.132); thuật toán dòng nhận phần tử theo nhịp của nguồn và không quay lại được. Trong chương, "truy vấn" có hai nghĩa: câu hỏi gửi tới bộ xử lý dòng, như trong định nghĩa trên, và phần tử của dòng truy vấn tìm kiếm ở Mục 2; khi có thể nhầm, nghĩa thứ hai được gọi là truy vấn tìm kiếm.

### 1.2 Hình mô hình dòng

Hình dưới vẽ lại MMDS Hình 4.1 (tr.132) và đặt mỗi thành phần của Định nghĩa 08.1 vào một chỗ trong hệ thống: một bộ xử lý đứng giữa các dòng đi vào và các câu trả lời đi ra, với hai nơi lưu có vai trò khác nhau.

![Các dòng đi vào bộ xử lý dòng từ bên trái; dòng trên cùng viết 5, 3, 0, 4, 7, 2, 5, 1, số 1 sát bộ xử lý là phần tử đến trước, mũi tên thời gian chỉ sang trái. Bộ xử lý chứa truy vấn thường trực; truy vấn tức thời đi vào từ phía trên, dòng kết quả đi ra bên phải; bộ xử lý đọc và ghi bộ nhớ làm việc hạn chế bằng mũi tên hai chiều, chỉ ghi vào kho lưu trữ vẽ bằng khung nét đứt, và kho này không dùng để trả lời truy vấn.](img/lec-08/mo-hinh-dong.svg)

Hình giữ quy ước của MMDS: phần tử nằm gần bộ xử lý đến trước, nên dòng $1,5,2,7,4,0,3,5$ được viết ngược thành 5, 3, 0, 4, 7, 2, 5, 1, với $x_1=1$ sát bộ xử lý. Hai mũi tên giữa bộ xử lý và hai nơi lưu mang nội dung của định nghĩa. Mũi tên hai chiều tới bộ nhớ làm việc ứng với trạng thái: phép cập nhật đọc và ghi nó, phép trả lời đọc nó. Mũi tên một chiều tới kho lưu trữ nét đứt ứng với giả thiết cuối của Định nghĩa 08.1: không có đường từ kho quay về để trả lời. Truy vấn thường trực nằm sẵn trong bộ xử lý, truy vấn tức thời đi vào từ bên ngoài, và ba dòng trên hình có nhịp, kiểu riêng nhưng dùng chung một bộ nhớ làm việc.

### 1.3 Vết chạy và thuật toán mẫu

Ví dụ sau áp Định nghĩa 08.1 cho hai truy vấn đầu của Ví dụ 08.1 và ghi trạng thái sau từng phần tử.

::: example Ví dụ 08.2 (Vết chạy của hai trạng thái)
**Dữ kiện.** Dòng $x_1,\ldots,x_8=1,5,2,7,4,0,3,5$. Truy vấn giá trị lớn nhất giữ một số $M$, ban đầu $M=-\infty$, cập nhật $M\gets\max(M,x_r)$. Truy vấn trung bình giữ tổng $T$, ban đầu $0$, cập nhật $T\gets T+x_r$, cùng số đếm $r$, và trả lời $T/r$.

**Tính.**

| $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $x_r$ | 1 | 5 | 2 | 7 | 4 | 0 | 3 | 5 |
| $M$ | 1 | 5 | 5 | 7 | 7 | 7 | 7 | 7 |
| $T$ | 1 | 6 | 8 | 15 | 19 | 19 | 22 | 27 |

**Diễn giải.** Sau tám phần tử, trạng thái của hai truy vấn là ba số $M=7$, $T=27$, $r=8$; tám số đo không còn được giữ.

**Kiểm tra lại.** Cột cuối cho lại $7$ và $27/8=3{,}375$ của Ví dụ 08.1.
:::

Truy vấn giá trị lớn nhất có đủ các thành phần của Định nghĩa 08.1, nên chúng ta dùng nó làm thuật toán mẫu khi đếm chi phí.

::: algorithm Thuật toán 08.2 (Giá trị lớn nhất trên dòng)
**Đầu vào.** Dòng số thực $x_1,x_2,\ldots$, đọc lần lượt.

**Đầu ra.** Khi có truy vấn, giá trị $M=\max\{x_1,\ldots,x_r\}$.

**Giả thiết.** Mỗi số nằm gọn trong một từ máy (machine word), đơn vị bộ nhớ mà một phép toán xử lý trong một bước.

1. Khởi tạo $M\gets-\infty$.
2. Khi $x_r$ đến: nếu $x_r>M$ thì đặt $M\gets x_r$.
3. Khi có truy vấn: trả $M$.

```text
M ← −∞
khi x_r đến:  nếu x_r > M: M ← x_r
khi có truy vấn: trả M
```

**Bất biến.** Sau bước 2 với phần tử $x_r$, $M=\max\{x_1,\ldots,x_r\}$. Với $r=1$, $x_1>-\infty$ nên $M=x_1$. Nếu bất biến đúng sau $x_r$, bước 2 đặt $M$ bằng số lớn hơn trong $\max\{x_1,\ldots,x_r\}$ và $x_{r+1}$, tức $\max\{x_1,\ldots,x_{r+1}\}$; theo quy nạp, bất biến đúng với mọi $r\ge1$.

**Dừng.** Dòng không có điểm cuối; mỗi lần gọi bước 2 hoặc bước 3 kết thúc sau số phép toán không đổi.

**Trường hợp biên.** Truy vấn trước phần tử đầu tiên ($r=0$) trả $-\infty$, nghĩa là chưa có số đo. Phần tử bằng $M$ không làm đổi $M$.

**Chi phí.** Mỗi phép toán trên một từ máy tính là 1; mô hình này được nêu đầy đủ ở Định nghĩa 08.3 (Mục 1.4).

| Bước | Số lần sau $r$ phần tử | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1 | $1$ | 1 phép gán | $1$ |
| 2 | $r$ | 1 phép so sánh, tối đa 1 phép gán | $r$ phép so sánh, tối đa $r$ phép gán |
| 3 | mỗi truy vấn | 1 phép đọc | $1$ mỗi truy vấn |
:::

### 1.4 Chi phí theo từng phần tử

Dòng không có điểm cuối, nên tổng thời gian chạy không phải một con số để so sánh. Chúng ta đo chi phí trên mỗi phần tử đến; sau $r$ phần tử, tổng công việc bằng $r$ nhân chi phí mỗi phần tử.

::: definition Định nghĩa 08.3 (Chi phí của thuật toán dòng)
**Mô hình.** Bộ nhớ đếm bằng từ máy; một từ chứa một số đo, một khóa, một chỉ số hoặc một bộ đếm. Thời gian đếm bằng số phép toán trên từ máy.

Chi phí của một thuật toán dòng gồm bốn đại lượng:

- **bộ nhớ**: số từ của trạng thái, yêu cầu nhỏ hơn lịch sử;
- **cập nhật**: số phép toán cho mỗi phần tử đến, yêu cầu không tăng theo $r$;
- **lượt đọc**: số lần đọc mỗi phần tử, bằng $1$;
- **sai số**: đại lượng nào của câu trả lời chỉ được xấp xỉ, theo tỷ lệ hay theo xác suất, và dưới giả thiết nào.
:::

Bộ nhớ quyết định thuật toán có chạy được không, cập nhật quyết định nó có theo kịp nhịp đến không, sai số nói câu trả lời đúng tới đâu. Bảng dưới đếm bốn đại lượng cho ba truy vấn của Ví dụ 08.1.

| Truy vấn | Bộ nhớ (từ) | Cập nhật mỗi phần tử | Lượt đọc | Sai số |
|---|---|---|---:|---|
| giá trị lớn nhất | $1$ | 1 phép so sánh | 1 | không |
| trung bình mọi số | $2$ | 2 phép cộng | 1 | không |
| trung bình 24 số gần nhất | $24+3$ | 4 phép | 1 | không |

Hàng đầu là Thuật toán 08.2. Ở hàng thứ hai, mỗi phần tử cộng $x_r$ vào $T$ và cộng $1$ vào $r$. Ở hàng cuối, 24 số nằm trong một bộ đệm vòng (ring buffer), tức một mảng 24 ô mà phần tử mới ghi đè ô của số cũ nhất; ba từ còn lại là tổng chạy của các số trong bộ đệm, vị trí ghi tiếp theo và số đếm $\min(r,24)$ dùng làm mẫu số. Mỗi phần tử tốn bốn phép: trừ số cũ nhất khỏi tổng khi $r>24$, hoặc tăng số đếm khi $r\le24$; cộng số mới vào tổng; ghi đè ô; tăng vị trí ghi theo modulo 24. Không hàng nào có chi phí tăng theo $r$.

Vết sau chạy tay phép cập nhật của cửa sổ, thu nhỏ còn 4 số. Dòng $1,5,2,7,4$ là năm số đầu của dòng trong MMDS Hình 4.1; cỡ cửa sổ 4 do học phần chọn để chạy tay. Sau bốn số, trạng thái gồm bộ đệm $[1,5,2,7]$ ở ô 1 đến ô 4, tổng $15$, số trong bộ đệm $4$, bằng $\min(r,4)$, và vị trí ghi tiếp là ô 1. Bất biến của trạng thái gồm hai phần: tổng bằng tổng các số trong bộ đệm, và khi bộ đệm đầy, ô ở vị trí ghi tiếp chứa số cũ nhất. Khi $x_5=4$ đến, phép cập nhật trừ số cũ nhất $1$ khỏi tổng, cộng $4$, ghi đè ô 1 và chuyển vị trí ghi tiếp sang ô 2. Tổng thành $15-1+4=18$, bộ đệm thành $[4,5,2,7]$, và ô 2 chứa số 5, nay là số cũ nhất, nên bất biến được giữ. Phép trả lời chỉ đọc trạng thái: $18/4=4{,}5$, đúng trung bình của $5,2,7,4$.

![Trạng thái sau 4 số: bộ đệm 1, 5, 2, 7 ở ô 1 đến ô 4, tổng 15, số trong bộ đệm 4, ghi tiếp ô 1; phần tử x5 bằng 4 đi vào khối cập nhật, khối này trừ 1, cộng 4, ghi đè ô 1, chuyển ghi tiếp sang ô 2; trạng thái sau 5 số: bộ đệm 4, 5, 2, 7 với ô 1 khung đậm, tổng 18, số trong bộ đệm vẫn là 4, ghi tiếp ô 2; mũi tên xuống câu trả lời 18/4 bằng 4,5; mũi tên nét đứt đưa trạng thái mới quay lại khối cập nhật, dùng khi x6 đến.](img/lec-08/trang-thai-cap-nhat.svg)

Hình đọc từ trái sang phải: trạng thái sau 4 số, khối cập nhật nhận $x_5$, trạng thái sau 5 số. Mũi tên vào khối cập nhật chỉ có hai nguồn, trạng thái cũ và phần tử vừa đến, đúng như phép cập nhật của Định nghĩa 08.1; các số $x_1,\ldots,x_4$ không được đọc lại, nên thông tin cần về chúng phải nằm sẵn trong bộ đệm và tổng. Mũi tên nét đứt đưa trạng thái mới quay lại khối cập nhật cho phần tử kế tiếp, còn mũi tên xuống câu trả lời là phép trả lời. Bốn thao tác trong khối cập nhật là bốn phép mà bảng trên đếm cho cửa sổ 24 số.

Mô hình từ máy che một chi tiết: bộ đếm $r$ cần $\lceil\log_2(r+1)\rceil$ bit, vì nó nhận $r+1$ giá trị $0,\ldots,r$. Với $r=8=1000_2$, ta cần $\lceil\log_2 9\rceil=4$ bit; một cảm biến độ cao mặt biển gửi 10 số mỗi giây trong một năm cho $r=315\,360\,000$, cần $29$ bit vì $2^{28}<r+1\le2^{29}$. Bộ đếm vừa một từ 64 bit khi $r<2^{64}$, nên mô hình tính nó là 1 từ.

### 1.5 Nhầm lẫn thường gặp và cách làm trong thực hành

::: remark Nhận xét 08.4 (Nhầm lẫn thường gặp)
- "Bộ nhớ hữu hạn" khác "bộ nhớ nhỏ hơn lịch sử": chép tám số của Ví dụ 08.1 chỉ tốn 8 từ, nhưng sau một năm một cảm biến độ cao mặt biển đã gửi hơn $3\cdot10^8$ số.
- Trạng thái khác mẫu: trạng thái của truy vấn trung bình là cặp $(27,8)$, không phải phần tử nào của dòng; mẫu ở Mục 2 và Mục 3 là trạng thái gồm các phần tử được chọn.
- "Một lượt" không có nghĩa bộ nhớ đạt yêu cầu: thuật toán chép mọi phần tử vào trạng thái cũng đọc mỗi phần tử một lần, nhưng bộ nhớ tăng theo $r$. Ngược lại, trung bình $w$ số gần nhất giữ $w$ số cùng vài từ phụ, không đổi theo $r$ nhưng tăng theo $w$.
- Có kho lưu trữ không có nghĩa đọc lại được: câu trả lời phải tính từ trạng thái.
:::

::: remark Nhận xét 08.5 (Trong thực hành)
Theo MMDS (§4.1.4, tr.135), phần tử đến nhanh nên phải xử lý ngay trong bộ nhớ chính, và nhiều dòng chậm cộng lại vẫn vượt bộ nhớ: một cảm biến độ cao mặt biển tạo khoảng 3,5 MB mỗi ngày, một triệu cảm biến tạo khoảng $3{,}46\cdot10^{12}$ byte. Cũng theo mục đó, nhiều bài toán dòng chỉ giải được trong bộ nhớ nhỏ khi chấp nhận câu trả lời xấp xỉ hoặc ngẫu nhiên. Đại lượng sai số của Định nghĩa 08.3 ghi lại phần đó; Mục 2 và Mục 4 lấy tính ngẫu nhiên từ phép chọn hàm băm, Mục 3 từ số ngẫu nhiên rút ở mỗi bước.
:::

### 1.6 Bài tập: trạng thái của phương sai

::: exercise Bài tập 08.1 (Trạng thái của phương sai)
Câu hỏi do học phần dựng trên dòng của MMDS Hình 4.1, cùng kiểu với truy vấn trung bình của Ví dụ 4.1. Một truy vấn thường trực trả phương sai của mọi số đã đọc,

$$
\sigma_r^2=\frac1r\sum_{i=1}^{r}(x_i-\bar x_r)^2,\qquad \bar x_r=\frac1r\sum_{i=1}^{r}x_i .
$$

(a) Xác định một trạng thái cỡ hằng đủ để trả lời sau mỗi phần tử, cùng phép cập nhật của nó. (b) Tính $\sigma_8^2$ trên dòng $1,5,2,7,4,0,3,5$.
:::

::: hint
Khai triển $(x_i-\bar x_r)^2$ và tách tổng thành các tổng chỉ phụ thuộc vào $x_i$, không phụ thuộc vào $\bar x_r$.
:::

::: solution
**(a) Trạng thái.** Ta biểu diễn tổng bình phương độ lệch qua các tổng của $x_i$:

$$
\begin{aligned}
\sum_{i=1}^{r}(x_i-\bar x_r)^2
&=\sum_i x_i^2-2\bar x_r\sum_i x_i+r\bar x_r^2\\
&=\sum_i x_i^2-2r\bar x_r^2+r\bar x_r^2\\
&=\sum_i x_i^2-r\bar x_r^2 .
\end{aligned}
$$

Dòng đầu khai triển bình phương, dòng thứ hai thay $\sum_i x_i=r\bar x_r$. Chia cho $r$ được $\sigma_r^2=\frac1r\sum_i x_i^2-\bar x_r^2$. Vậy trạng thái gồm ba số $r$, $\sum_i x_i$ và $\sum_i x_i^2$. Khi $x_r$ đến: tăng $r$, cộng $x_r$ vào tổng, cộng $x_r^2$ vào tổng bình phương; cập nhật tốn một phép nhân và ba phép cộng, không tăng theo $r$. Trạng thái có 3 từ.

**(b) Tính.** Trạng thái sau từng số:

| $r$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $x_r$ | 1 | 5 | 2 | 7 | 4 | 0 | 3 | 5 |
| $\sum x_i$ | 1 | 6 | 8 | 15 | 19 | 19 | 22 | 27 |
| $\sum x_i^2$ | 1 | 26 | 30 | 79 | 95 | 95 | 104 | 129 |

Sau 8 số: $r=8$, $\sum x_i=27$, $\sum x_i^2=1+25+4+49+16+0+9+25=129$. Do đó $\bar x_8=27/8=3{,}375$ và

$$
\sigma_8^2=\frac{129}{8}-\Bigl(\frac{27}{8}\Bigr)^2=16{,}125-11{,}390625=4{,}734375 .
$$

**Kiểm tra lại.** Tính trực tiếp, các độ lệch $x_i-3{,}375$ có bình phương $5{,}640625$; $2{,}640625$; $1{,}890625$; $13{,}140625$; $0{,}390625$; $11{,}390625$; $0{,}140625$; $2{,}640625$, tổng $37{,}875$, và $37{,}875/8=4{,}734375$.
:::

**Trong thực hành.** Công thức $\sigma_r^2=\frac1r\sum_i x_i^2-\bar x_r^2$ đúng trong số học thực, nhưng khi tính bằng số thực dấu phẩy động nó trừ hai số lớn gần nhau và có thể mất hết chữ số có nghĩa. Cộng $10^9$ vào mọi số của dòng $1,5,2,7,4,0,3,5$ không đổi phương sai, vẫn là $4{,}734375$. Với số thực dấu phẩy động 64 bit (float64), hai số liền nhau ở cỡ $10^{18}$ cách nhau 128, nên mỗi $x_i^2$ được làm tròn tới bội của 128: $(10^9+1)^2=10^{18}+2\cdot10^9+1$ mất số hạng $1$, và các số hạng $1,25,4,49,16,0,9,25$ đều mất như vậy. Tổng $\sum_i x_i^2$, cỡ $8\cdot10^{18}$ với khoảng cách 1 024, vì thế thiếu đúng $129$, chính là phần mang thông tin về phương sai. Khi đó $\frac1r\sum_i x_i^2$ và $\bar x_r^2$ cùng bằng $1{,}00000000675\cdot10^{18}$ trong float64; phép trừ cuối gần như không có sai số và chỉ làm lộ việc mọi chữ số đúng đã mất, với kết quả $0{,}0$ theo một lần chạy bằng Python.

Phương pháp của Welford (1962) tránh phép trừ này. Trạng thái gồm $r$, trung bình $\bar x_r$ và tổng bình phương độ lệch $V_r=\sum_{i\le r}(x_i-\bar x_r)^2$, bắt đầu từ $\bar x_0=0$, $V_0=0$, và cập nhật

$$
\bar x_r=\bar x_{r-1}+\frac{x_r-\bar x_{r-1}}r,\qquad V_r=V_{r-1}+(x_r-\bar x_{r-1})(x_r-\bar x_r),
$$

rồi trả lời $\sigma_r^2=V_r/r$. Trạng thái vẫn có cỡ hằng, ba số. Trên dòng gốc, phép cập nhật cho $V_8=37{,}875$, đúng tổng bình phương độ lệch ở phần kiểm tra lại của Bài tập 08.1, và $\sigma_8^2=37{,}875/8=4{,}734375$. Trên dòng cộng $10^9$, cùng phép tính float64 cho $4{,}7343749866$, sai số khoảng $1{,}3\cdot10^{-8}$. Phương pháp này là bổ sung ngoài nguồn chính của chương.

Như vậy, chúng ta đã có đặc tả chung cho các cấu trúc của chương: thuật toán dòng một lượt trả lời từ trạng thái chọn theo truy vấn (Định nghĩa 08.1) và được đo bằng bốn đại lượng trên mỗi phần tử (Định nghĩa 08.3), với Thuật toán 08.2 làm trường hợp mẫu. Các truy vấn của mục này, kể cả phương sai ở Bài tập 08.1, là những thống kê có trạng thái cỡ hằng trả lời chính xác. Câu hỏi của máy tìm kiếm thì khác: đo tỷ lệ truy vấn tìm kiếm lặp của từng người dùng khi chỉ lưu được $1/10$ dòng (MMDS §4.2.1, tr.136). Trạng thái khi đó phải là một mẫu các phần tử, và cách chọn mẫu quyết định câu trả lời có đúng không. Trong Mục 2, chúng ta xét cách chọn mẫu đó.

## 2. Lấy mẫu theo khóa

Máy tìm kiếm nhận dòng bộ $t$ dạng (người dùng, truy vấn tìm kiếm, thời gian), chỉ lưu được $1/10$ dòng, và muốn biết tỷ lệ truy vấn lặp của người dùng điển hình trong tháng vừa qua (MMDS §4.2.1, tr.136). Mục 1 cho thấy một số thống kê trên mọi phần tử, như giá trị lớn nhất, trung bình và phương sai, có trạng thái cỡ hằng; câu hỏi này thì cần một mẫu các bộ, vì tỷ lệ lặp của một người được tính từ chính các truy vấn của người đó. Chúng ta cần chọn mẫu sao cho tỷ lệ tính trên mẫu bằng tỷ lệ thật, với trạng thái quyết định không tăng theo dòng.

<!-- note-topic-id: lec-08-topic-03 -->
### 2.1 Sai lệch của lấy mẫu từng bộ

Cách làm đầu tiên nghĩ tới là rút cho mỗi bộ một số đều trong $\{0,\ldots,9\}$ và giữ bộ khi số bằng $0$. Mỗi người dùng khi đó giữ trung bình $1/10$ số truy vấn của mình (MMDS §4.2.1, tr.136). Ví dụ sau tính điều xảy ra với tỷ lệ lặp.

::: example Ví dụ 08.3 (Ba bộ truy vấn của An)
**Dữ kiện.** An gõ "đồ thị" hai lần và "băm" một lần, nên tỷ lệ lặp của An, tức số truy vấn phân biệt xuất hiện hai lần chia cho số truy vấn phân biệt, là $1/2$. Mỗi bộ được giữ độc lập với xác suất $1/10$. Ba bộ này do học phần dựng.

**Tính.** Hai bộ "đồ thị" được giữ độc lập, nên

| Biến cố | Xác suất |
|---|---|
| giữ cả hai bộ "đồ thị" | $\frac1{10}\cdot\frac1{10}=\frac1{100}$ |
| giữ đúng một bộ "đồ thị" | $2\cdot\frac1{10}\cdot\frac9{10}=\frac{18}{100}$ |
| không giữ bộ "đồ thị" nào | $\frac9{10}\cdot\frac9{10}=\frac{81}{100}$ |
| giữ bộ "băm" | $\frac1{10}$ |

![Cây xác suất cho hai bộ đồ thị: bộ thứ nhất giữ với xác suất 1/10 hoặc bỏ với 9/10, rồi bộ thứ hai giữ 1/10 hoặc bỏ 9/10; bốn lá: giữ, giữ 1/100 đủ hai bản (khung kép); giữ, bỏ 9/100 đúng một bản; bỏ, giữ 9/100 đúng một bản; bỏ, bỏ 81/100 vắng mặt (khung nét đứt); đúng một bản 9/100 + 9/100 = 18/100; có mặt 1/100 + 18/100 = 19/100.](img/lec-08/cay-hai-bo-do-thi.svg)

Cây vẽ cùng phép tính theo hai tầng: tầng một là bộ "đồ thị" thứ nhất, tầng hai là bộ thứ hai, mỗi nhánh giữ với xác suất $1/10$ và bỏ với $9/10$. Bốn lá có xác suất $1/100$, $9/100$, $9/100$, $81/100$; hệ số 2 trong $18/100$ đến từ hai lá "giữ, bỏ" và "bỏ, giữ". "Đồ thị" có mặt ở ba lá đầu, tổng $19/100$, và chỉ lá đầu có đủ hai bản.

**Diễn giải.** Với điều kiện "đồ thị" có mặt trong mẫu, xác suất nó xuất hiện hai lần là $\frac{1/100}{1/100+18/100}=\frac1{19}$. Mẫu thường thấy "đồ thị" một lần và tính nó là truy vấn không lặp.

**Kiểm tra lại.** $\frac1{100}+\frac{18}{100}+\frac{81}{100}=1$.
:::

Phép đếm sau làm cho một người dùng bất kỳ, theo MMDS (§4.2.1, tr.136–137); sách viết $s$ cho số truy vấn xuất hiện một lần, ở đây là $u$.

::: proposition Mệnh đề 08.6 (Tỷ số từ số đếm kỳ vọng)
**Giả thiết.** Một người dùng có $u\ge0$ truy vấn phân biệt xuất hiện đúng một lần và $d>0$ truy vấn phân biệt xuất hiện đúng hai lần, không truy vấn nào nhiều hơn hai lần. Mỗi bộ được giữ độc lập với xác suất $1/10$.

**Kết luận.** Số kỳ vọng các truy vấn phân biệt thấy hai lần trong mẫu là $d/100$, thấy đúng một lần là $u/10+18d/100$, và tỷ số

$$
\frac{d/100}{d/100+u/10+18d/100}=\frac{d}{10u+19d}
$$

khác tỷ lệ thật $d/(u+d)$.

**Điều kiện áp dụng.** Xác suất lấy theo các số rút cho từng bộ; dòng của người dùng cố định.

**Phạm vi.** Mệnh đề so tỷ số của hai số đếm kỳ vọng với tỷ lệ thật; nó không tính kỳ vọng của tỷ số ngẫu nhiên trên mẫu.
:::

::: proof
**Bước 1 (truy vấn một lần).** Mỗi truy vấn trong $u$ truy vấn một lần có mặt trong mẫu với xác suất $1/10$, và khi có mặt thì xuất hiện một lần. Theo tuyến tính kỳ vọng, số kỳ vọng là $u/10$.

**Bước 2 (truy vấn hai lần).** Với mỗi truy vấn trong $d$ truy vấn hai lần, hai bộ được giữ độc lập, nên xác suất thấy hai lần là $1/100$ và thấy đúng một lần là $2\cdot\frac1{10}\cdot\frac9{10}=18/100$. Theo tuyến tính kỳ vọng, hai số kỳ vọng là $d/100$ và $18d/100$.

**Bước 3 (tỷ số).** Nhân tử số và mẫu số với $100$ được $d/(10u+19d)$.

**Bước 4 (so sánh).** Vì $d>0$,

$$
\frac{d}{u+d}=\frac{d}{10u+19d}
\iff 10u+19d=u+d
\iff 9u+18d=0,
$$

không xảy ra với $u\ge0$, $d>0$. $\square$
:::

Với An, $u=d=1$, mệnh đề cho $1/29\approx0{,}034$ thay cho $1/2$. Số này khác $1/19$ của Ví dụ 08.3 vì mẫu số tính cả truy vấn "băm". Bước 2 dùng độc lập giữa hai bộ của cùng một truy vấn, và sai lệch đến từ chỗ một truy vấn lặp bị cắt thành hai quyết định riêng.

::: remark Nhận xét 08.7 (Nhầm lẫn thường gặp)
- Mỗi người dùng vẫn giữ trung bình $1/10$ số truy vấn của mình, và sai lệch đến từ việc đơn vị bị cắt. Với tỷ lệ giữ $\eta$ bất kỳ, cùng phép đếm cho tỷ số $d\eta/(u+(2-\eta)d)$, vẫn khác $d/(u+d)$ khi $\eta<1$; với $\eta=1/10$ ta được lại $d/(10u+19d)$, và với $\eta=1$, khi mọi bộ được giữ, tỷ số về đúng $d/(u+d)$.
- $d/(10u+19d)$ là tỷ số của hai số đếm kỳ vọng, không phải kỳ vọng của tỷ lệ tính trên mẫu. Với An, $1/29=\frac{1/100}{1/10+19/100}$ chia hai kỳ vọng; tỷ lệ tính trên mẫu là một biến ngẫu nhiên, không xác định khi mẫu không có truy vấn nào của An, nên không thể viết kỳ vọng của nó bằng $1/29$.
:::

<!-- note-topic-id: lec-08-topic-04 -->
### 2.2 Mẫu nhất quán theo khóa

Mệnh đề 08.6 chỉ ra đơn vị cần giữ trọn là người dùng: giữ hoặc bỏ cả lịch sử truy vấn của mỗi người. Mỗi người dùng cùng mọi bộ của người đó tạo thành một cụm, và mẫu cần chọn hoặc bỏ cả cụm. MMDS (§4.2.2, tr.137) nêu một phương án trực tiếp: lần đầu gặp một người dùng, rút một số đều trong $\{0,\ldots,9\}$, ghi nhãn "giữ" nếu số là $0$ và "bỏ" nếu khác; bộ đến sau tra bảng nhãn và vào mẫu khi nhãn là "giữ".

::: example Ví dụ 08.4 (Bảng nhãn trên năm bộ)
**Dữ kiện.** Năm bộ đến theo thứ tự (An, "đồ thị"), (Bình, "lọc"), (An, "băm"), (An, "đồ thị"), (Chi, "lọc"); ba bộ của An là ba bộ của Ví dụ 08.3. Các số rút cho người dùng mới lần lượt là $0$, $7$, $4$, một lần chạy minh họa do học phần dựng. Dòng năm bộ này được dùng lại ở Ví dụ 08.5 và 08.7.

**Tính.**

| $r$ | Người dùng | Thao tác | Bảng sau bước | Vào mẫu? |
|---:|---|---|---|---|
| 1 | An | mới, rút $0$, ghi "giữ" | An: giữ | có |
| 2 | Bình | mới, rút $7$, ghi "bỏ" | An: giữ; Bình: bỏ | không |
| 3 | An | đã có, tra "giữ" | không đổi | có |
| 4 | An | đã có, tra "giữ" | không đổi | có |
| 5 | Chi | mới, rút $4$, ghi "bỏ" | An: giữ; Bình: bỏ; Chi: bỏ | không |

**Diễn giải.** Mẫu gồm đủ ba bộ của An: "đồ thị" hai lần, "băm" một lần, nên tỷ lệ lặp của An tính trên mẫu là $1/2$, đúng tỷ lệ thật. Bảng có 3 hàng sau 5 bộ.

**Kiểm tra lại.** Số hàng bằng số người dùng phân biệt trong An, Bình, An, An, Chi, tức $3$.
:::

![Năm bộ (An, đồ thị), (Bình, lọc), (An, băm), (An, đồ thị), (Chi, lọc) đi vào bảng tra; sau năm bộ bảng có ba hàng, một hàng cho mỗi người dùng: An rút số 0 và nhãn giữ, Bình rút số 7 và nhãn bỏ, Chi rút số 4 và nhãn bỏ; các lần gặp lại An chỉ tra bảng, mỗi người dùng mới thêm một hàng.](img/lec-08/bang-theo-nguoi-dung.svg)

Phương án đúng về xác suất: mỗi người dùng nhận nhãn "giữ" với xác suất $1/10$, và mọi bộ của người đó tra cùng một hàng. Nhưng bảng có một hàng cho mỗi người dùng phân biệt đã gặp, tối đa $r$ hàng, nên vi phạm giả thiết bộ nhớ của Định nghĩa 08.1. Với $10^8$ người dùng và 16 byte mỗi hàng, một giả định của học phần để có cỡ, bảng chiếm $10^8\cdot16=1{,}6\cdot10^9$ byte; đưa bảng ra đĩa cũng không được, vì không có thời gian ra đĩa cho mỗi bộ đến (MMDS §4.2.2, tr.137).

Một cách trực quan, hàm băm làm việc của bảng mà không lưu bảng: một hàm cố định cho cùng giá trị mỗi khi gặp lại cùng tên (Kiến thức tiên quyết), nên quyết định được tính lại ở mỗi bộ thay vì tra lại. MMDS (§4.2.2, tr.137) gọi hàm băm là bộ sinh số ngẫu nhiên có thêm tính chất này. Mô tả này chưa phải định nghĩa: nó chưa nói hàm băm phải thỏa điều kiện gì để tỷ lệ đúng $1/10$.

![Năm bộ (An, đồ thị), (Bình, lọc), (An, băm), (An, đồ thị), (Chi, lọc) đi qua cùng một hàm băm h trên tên người dùng, giá trị trong 0 đến 9; giữ khi h bằng 0: h(An) = 0 nên giữ cả ba bộ của An, h(Bình) = 7 và h(Chi) = 4 nên bỏ; không lưu bảng theo người dùng.](img/lec-08/bam-theo-nguoi-dung.svg)

Hình dùng $b=10$ ngăn, ngưỡng $a=1$, tức giữ bộ khi $h=0$; cả ba bộ của An vào mẫu. Các giá trị $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$ là một hàm minh họa, chọn trùng số rút của Ví dụ 08.4 nên hai phương án cho cùng mẫu, nhưng không có bảng nào được lưu. Trang chiếu MMDS (Streams 1, tr.15–16) minh họa cùng cơ chế với tỷ lệ 30%, tức giữ khi giá trị băm thuộc $\{0,1,2\}$.

::: definition Định nghĩa 08.8 (Mẫu theo khóa với tỷ lệ $a/b$)
Cho dòng bộ $t$, mỗi bộ có khóa $K(t)$ trong miền khóa $\mathcal K$. Cho số ngăn $b\ge1$, ngưỡng $a$ nguyên với $0\le a\le b$, và hàm băm $h:\mathcal K\to\{0,\ldots,b-1\}$ được chọn một lần trước khi dòng bắt đầu rồi giữ cố định.

**Mẫu theo khóa với tỷ lệ $a/b$** là tập các bộ $t$ đã đọc có $h(K(t))<a$.
:::

Khóa là thành phần của bộ nhận diện đơn vị mà thống kê gộp; ở dòng truy vấn tìm kiếm, khóa là người dùng. Dấu "$<$" nhận đúng $a$ giá trị $0,\ldots,a-1$, nên tỷ lệ giá trị được nhận là $a/b$; $a=0$ cho mẫu rỗng, $a=b$ giữ mọi bộ. Ví dụ dẫn nhập ứng với $b=10$, $a=1$. So với mẫu từng bộ của Mục 2.1, đơn vị quyết định đổi từ bộ sang khóa; so với bảng nhãn của Ví dụ 08.4, quyết định được tính lại từ $h$ thay vì tra bảng.

::: example Ví dụ 08.5 (Ba ngưỡng trên cùng hàm băm)
**Dữ kiện.** Dòng năm bộ của Ví dụ 08.4: ba bộ của An, một của Bình, một của Chi; $b=10$; $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$. Xét $a=1$, $a=5$, $a=8$.

**Tính.**

| $a$ | Khóa có $h<a$ | Bộ trong mẫu |
|---:|---|---:|
| $1$ | An | $3$ |
| $5$ | An, Chi | $4$ |
| $8$ | An, Bình, Chi | $5$ |

**Diễn giải.** Với mọi $a$, ba bộ của An cùng có mặt hoặc cùng vắng. Tăng $a$ chỉ thêm khóa, không bỏ khóa nào đã có; tính chất này được dùng ở Mục 2.5.

**Kiểm tra lại.** Với $a=8$, cả ba giá trị $0$, $7$, $4$ đều nhỏ hơn $8$, nên mẫu chứa cả năm bộ: $3+1+1=5$.
:::

::: algorithm Thuật toán 08.9 (Lấy mẫu theo khóa)
**Đầu vào.** Dòng bộ $t$ có khóa $K(t)$; số ngăn $b\ge1$, ngưỡng $0\le a\le b$; hàm $h:\mathcal K\to\{0,\ldots,b-1\}$.

**Đầu ra.** Mẫu gồm đúng các bộ $t$ có $h(K(t))<a$.

**Giả thiết.** $h$ cố định suốt dòng. Để có xác suất $a/b$, với mỗi khóa $K$, $h(K)$ đều trên $\{0,\ldots,b-1\}$ theo cách chọn $h$.

1. Khi bộ $t$ đến: tính khóa $K(t)$.
2. Tính $c\gets h(K(t))$.
3. Nếu $c<a$ thì đưa $t$ vào mẫu; nếu không thì bỏ $t$.

```text
LẤY-MẪU-THEO-KHÓA(t; a, h)
    nếu h(K(t)) < a: đưa t vào mẫu
```

**Dừng.** Mỗi bộ được xử lý sau ba bước; thuật toán chạy chừng nào dòng còn phần tử.

**Trường hợp biên.** $a=0$: không bộ nào vào mẫu. $a=b$: mọi bộ vào mẫu. Khóa gồm nhiều thành phần: $h$ kết hợp các thành phần thành một giá trị (MMDS §4.2.3, tr.137).

**Chi phí.** Theo mô hình của Định nghĩa 08.3:

| Bước | Số lần sau $r$ bộ | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 1–2: tính khóa và băm | $r$ | 1 phép băm | $r$ phép băm |
| 3: so sánh với $a$, có thể ghi bộ | $r$ | 1 phép so sánh | $r$ phép so sánh |

Trạng thái quyết định gồm tham số của $h$ cùng $a$, $b$, không tăng theo $r$ hay theo số khóa.
:::

Phép quyết định là so sánh $h(K(t))$ với $a$, và thuật toán không lưu gì theo khóa; tính đều của mẫu phụ thuộc cách chọn $h$. Mệnh đề sau, dựa trên tính tất định của hàm băm ở phần tiên quyết, cho biết mẫu giữ trọn từng khóa và giữ mỗi khóa với xác suất bao nhiêu.

::: proposition Mệnh đề 08.10 (Tính nhất quán theo khóa và xác suất $a/b$)
**Giả thiết.** $b\ge1$, $0\le a\le b$, $h:\mathcal K\to\{0,\ldots,b-1\}$ cố định suốt dòng. Cho phần (b): $h$ được chọn ngẫu nhiên từ một họ hàm sao cho với mỗi khóa $K$ và mỗi $c\in\{0,\ldots,b-1\}$, $\Pr_h[h(K)=c]=1/b$.

**Kết luận.**

(a) Với mọi hai bộ $t$, $t'$ có $K(t)=K(t')$, Thuật toán 08.9 giữ cả hai hoặc bỏ cả hai.

(b) Mỗi khóa $K$ được giữ với xác suất $\Pr_h[h(K)<a]=a/b$.

**Điều kiện áp dụng.** Phần (a) đúng với mọi hàm $h$, kể cả hàm không đều. Phần (b) là xác suất theo phép chọn $h$, không theo các lần xuất hiện của khóa.

**Phạm vi.** Mệnh đề nói về từng khóa. Nó không khẳng định mẫu chứa đúng $a/b$ số khóa hay $a/b$ số bộ.
:::

::: proof
**Bước 1 (nhất quán).** Nếu $K(t)=K(t')$ thì $h(K(t))=h(K(t'))$, vì $h$ là một hàm cố định. Hai phép so sánh ở bước 3 so cùng một số với cùng $a$, nên cho cùng kết quả.

**Bước 2 (xác suất).** Biến cố $h(K)<a$ là hợp rời của $a$ biến cố $h(K)=c$, $c=0,\ldots,a-1$. Theo giả thiết, mỗi biến cố có xác suất $1/b$, nên

$$
\Pr_h[h(K)<a]=\sum_{c=0}^{a-1}\Pr_h[h(K)=c]=\frac ab. \qquad\square
$$
:::

Phần (a) là bảo đảm tất định thay cho bảng nhãn: mọi truy vấn tìm kiếm của một người được giữ đều có trong mẫu, nên tỷ lệ lặp của người đó tính đúng, như $1/2$ của An. Phần (b) cho mỗi người cùng xác suất $a/b$ được chọn, nên mọi tổng tính trên mẫu chia cho $a/b$ có kỳ vọng bằng tổng thật; Hệ quả 08.12 ở Mục 2.4 là một trường hợp. Để số người được chọn tập trung quanh $a/b$ số người, cần thêm giả thiết các khóa khác nhau nhận giá trị băm độc lập. Tính đều theo từng khóa không đủ: họ gồm $b$ hàm hằng $h\equiv c$, với $c$ chọn đều trong $\{0,\ldots,b-1\}$, thỏa giả thiết của phần (b), nhưng mẫu hoặc chứa mọi người dùng, hoặc rỗng. Vì vậy số khóa được giữ trong một lần chạy là ngẫu nhiên; $a/b$ là xác suất cho từng khóa, không phải tỷ lệ chắc chắn đạt trong mỗi lần chạy.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "$h$ cố định": nếu hàm băm được chọn lại mỗi giờ, hai bộ của An ở hai giờ khác nhau có thể nhận hai quyết định khác nhau, và mẫu quay lại cắt rời đơn vị như Mục 2.1.
- Bỏ "đều theo cách chọn $h$": với $1\le a<b$, họ hàm chỉ gồm hàm luôn trả $0$ vẫn cho phần (a), nhưng mọi khóa được giữ với xác suất $1$, không phải $a/b$.
- Bỏ "khóa nhận diện đúng đơn vị": nếu khóa là cặp (người dùng, thời gian), mỗi bộ có khóa riêng, và Mục 2.3 chỉ ra hậu quả.

Bước 1 dùng tính cố định của $h$; Bước 2 dùng tính đều theo từng khóa.

::: remark Nhận xét 08.11 (Trong thực hành)
Hàm $h$ là một hàm băm có tham số, chẳng hạn hạt giống, chọn ngẫu nhiên một lần trước khi dòng bắt đầu rồi cố định và dùng chung trên mọi máy xử lý dòng; đổi tham số giữa chừng phá phần (a) của Mệnh đề 08.10. Tính ngẫu nhiên chỉ nằm ở lần chọn đó, khác với hồ chứa ở Mục 3, nơi một số mới được rút cho mỗi phần tử. Máy tìm kiếm thật nhận địa chỉ IP chứ không nhận người dùng; MMDS (§4.2.1, chú thích tr.136) giả định mỗi địa chỉ ứng với một người, điều chỉ đúng gần đúng, và khi nhiều người chung một địa chỉ, tỷ lệ lặp đo được là của cả nhóm. Tính đều theo từng khóa là giả thiết về phép chọn hàm, không kiểm được trên một hàm đã chọn.
:::

<!-- note-topic-id: lec-08-topic-05 -->
### 2.3 Chọn khóa theo đơn vị thống kê

Mệnh đề 08.10 giữ trọn từng khóa, nên khóa quyết định thống kê nào tính đúng trên mẫu. MMDS (§4.2.3, tr.137) nêu rằng cùng dòng (người dùng, truy vấn, thời gian) có thể lấy mẫu theo người dùng, theo truy vấn hoặc theo cặp (người dùng, truy vấn). Ba lựa chọn này phục vụ ba thống kê khác nhau.

| Thống kê | Khóa |
|---|---|
| tỷ lệ truy vấn lặp của mỗi người | người dùng |
| số người gõ mỗi truy vấn | truy vấn |
| số lần một người gõ lại một truy vấn | (người dùng, truy vấn) |

Quy trình chọn khóa có ba bước:

1. Xác định đơn vị mà thống kê gộp các bộ, tức đối tượng phải được giữ trọn.
2. Chọn đủ thành phần của bộ để nhận diện duy nhất đơn vị đó.
3. Kiểm: hai bộ của cùng đơn vị phải có cùng khóa, và hai đơn vị khác nhau phải có khóa khác nhau.

Thêm thành phần thừa làm hỏng bước 3 vế đầu: một đơn vị bị tách thành nhiều khóa. Thiếu thành phần làm hỏng vế sau: nhiều đơn vị bị gộp, như mã sinh viên chỉ duy nhất trong một trường.

::: exercise Bài tập 08.2 (Khóa người dùng và thời gian)
Với dòng truy vấn tìm kiếm và tỷ lệ $a/b=1/10$, dùng khóa là cặp (người dùng, thời gian) thay cho người dùng. Mẫu có cho tỷ lệ truy vấn lặp của mỗi người không lệch không?
:::

::: hint
Xét hai bộ "đồ thị" của An: chúng có cùng khóa không?
:::

::: solution
Không. Hai bộ của cùng một người có thời gian khác nhau, nên có hai khóa khác nhau, và Mệnh đề 08.10(a) không ràng buộc quyết định của chúng. Nếu các khóa khác nhau nhận giá trị băm độc lập theo cách chọn $h$, mỗi bộ được giữ độc lập với xác suất $1/10$, đúng giả thiết của Mệnh đề 08.6; tỷ số tính trên mẫu là $d/(10u+19d)$, với An là $1/29$. Thành phần thời điểm tách một đơn vị thành nhiều khóa, vi phạm bước 3 của quy trình.
:::

### 2.4 Chi phí và cỡ mẫu

Thuật toán 08.9 tốn một phép băm và một phép so sánh mỗi bộ, và trạng thái quyết định cỡ hằng. Mẫu đã lưu thì khác: mỗi bộ được giữ thêm vào mẫu, nên cỡ mẫu tăng theo dòng. Hệ quả sau đo tốc độ tăng đó.

::: corollary Hệ quả 08.12 (Cỡ mẫu kỳ vọng)
**Giả thiết.** Như Mệnh đề 08.10(b); dòng đã có $r$ bộ.

**Kết luận.** Số bộ trong mẫu có kỳ vọng $ar/b$ theo cách chọn $h$.

**Điều kiện áp dụng.** Không cần các khóa khác nhau nhận giá trị băm độc lập.

**Phạm vi.** Kết luận nói về kỳ vọng; cỡ mẫu thực có thể lệch xa kỳ vọng khi một khóa có nhiều bộ.
:::

::: proof
Với bộ thứ $i$, đặt biến chỉ báo $\mathbf 1[h(K(t_i))<a]$. Theo Mệnh đề 08.10(b), biến này có kỳ vọng $a/b$. Cỡ mẫu là tổng $r$ biến chỉ báo, nên theo tuyến tính kỳ vọng, không cần độc lập, cỡ mẫu có kỳ vọng $r\cdot a/b$. $\square$
:::

::: example Ví dụ 08.6 (Khóa nhiều bộ)
**Dữ kiện.** Dòng có $r=1\,001\,000$ bộ: một khóa có $10^6$ bộ và $1\,000$ khóa, mỗi khóa một bộ. Tỷ lệ $a/b=1/5$. Số liệu do học phần dựng.

**Tính.** Theo Hệ quả 08.12, cỡ mẫu kỳ vọng là $1\,001\,000/5=200\,200$ bộ. Theo Mệnh đề 08.10, khóa nhiều bộ được giữ trọn với xác suất $1/5$ và bị bỏ trọn với xác suất $4/5$. Nếu được giữ, mẫu có ít nhất $10^6$ bộ; nếu bị bỏ, mẫu có không quá $1\,000$ bộ.

**Diễn giải.** Cỡ mẫu thực hoặc ít nhất $10^6$, hoặc không quá $1\,000$, nên không bao giờ gần $200\,200$.

**Kiểm tra lại.** $\frac15\cdot10^6+\frac15\cdot1\,000=200\,000+200=200\,200$.
:::

::: exercise Bài tập 08.3 (Ngưỡng 20% và khóa nhiều bộ)
Hàm $h$ nhận giá trị trong $\{0,\ldots,99\}$. Để chọn 20% khóa, giữ bộ khi $h(K)\le20$ hay khi $h(K)<20$? Một khóa có $10^6$ bộ: mẫu bảo đảm gì về các bộ đó, và có bảo đảm mẫu chứa 20% số bộ không?
:::

::: hint
Đếm số giá trị được nhận ở mỗi điều kiện; với khóa nhiều bộ, dùng Mệnh đề 08.10(a).
:::

::: solution
$h(K)<20$ nhận đúng 20 giá trị $0,\ldots,19$, tức tỷ lệ $20/100$; $h(K)\le20$ nhận 21 giá trị, tức 21%. Theo Mệnh đề 08.10(a), khóa có $10^6$ bộ được giữ trọn hoặc bỏ trọn. Mẫu không bảo đảm 20% số bộ, vì tỷ lệ $a/b$ áp dụng cho khóa, không cho bộ (Ví dụ 08.6). Câu hỏi do học phần dựng theo MMDS §4.2.3, tr.137–138.
:::

<!-- note-topic-id: lec-08-topic-06 -->
### 2.5 Ngưỡng băm khi ngân sách cố định

Với tỷ lệ cố định $1/10$, mẫu giữ mọi truy vấn của người dùng được chọn mãi mãi, và người mới được chọn tiếp tục xuất hiện (MMDS §4.2.4, tr.138). Khi chỉ có ngân sách cố định cho số bộ trong mẫu, tỷ lệ khóa phải giảm dần. Ví dụ 08.5 đã cho thấy hạ ngưỡng chỉ bỏ khóa, không thêm khóa; MMDS dùng đúng tính chất này. Sách viết $B$ cho số giá trị băm và $t$ cho ngưỡng; ở đây là $b$ và $\tau$.

::: algorithm Thuật toán 08.13 (Lấy mẫu theo khóa với ngưỡng giảm dần)
**Đầu vào.** Dòng bộ $t$ có khóa $K(t)$; hàm $h:\mathcal K\to\{0,\ldots,b-1\}$ với $b$ lớn; ngân sách $G\ge0$ bộ.

**Đầu ra.** Sau mỗi bộ, mẫu gồm các bộ đã đọc có $h(K(t))\le\tau$, với không quá $G$ bộ.

**Giả thiết.** $h$ cố định. Mẫu có chỉ mục có thứ tự theo giá trị băm, chẳng hạn cây tìm kiếm cân bằng trên các giá trị băm đang có trong mẫu, mỗi giá trị trỏ tới danh sách các bộ mang giá trị đó.

1. Khởi tạo $\tau\gets b-1$ và mẫu rỗng.
2. Khi bộ $t$ đến: nếu $h(K(t))\le\tau$ thì đưa $t$ vào mẫu và vào chỉ mục.
3. Chừng nào mẫu có hơn $G$ bộ: lấy $c$ là giá trị băm lớn nhất trong mẫu (tra chỉ mục), xóa mọi bộ có giá trị băm $c$, rồi đặt $\tau\gets c-1$.

**Dừng.** Mỗi lần lặp ở bước 3 xóa ít nhất một bộ, nên bước 3 dừng sau không quá số bộ đang có trong mẫu.

**Trường hợp biên.** Một khóa có hơn $G$ bộ buộc $\tau$ xuống dưới giá trị băm của nó, nên khóa đó bị bỏ trọn. Bước 3 hạ $\tau$ nhiều đơn vị một lần, qua các giá trị băm không có bộ nào, theo gợi ý của MMDS (§4.2.4, tr.138).

**Chi phí.**

| Thành phần | Số lần sau $r$ bộ | Chi phí mỗi lần |
|---|---|---|
| băm và so sánh ở bước 2 | $r$ | 1 phép băm, 1 phép so sánh |
| đưa vào chỉ mục | không quá $r$ | $O(\log G)$ |
| lần dọn ở bước 3 | không quá số giá trị băm phân biệt từng có trong mẫu | $O(\log G)$ để tra $c$ |
| xóa một bộ | không quá $r$ | $O(1)$ trên danh sách của $c$ |

Mỗi bộ bị xóa nhiều nhất một lần; mỗi lần dọn loại hẳn một giá trị băm, vì $\tau$ xuống dưới giá trị đó và không tăng lại. Chỉ mục giữ không quá $G+1$ bộ, nên mỗi phép tra tốn $O(\log G)$. Sau mỗi lần dọn, bộ nhớ gồm tối đa $G$ bộ cùng chỉ mục.
:::

Ký hiệu $G$ (ngân sách) chỉ dùng trong thuật toán này và Ví dụ 08.7. Ngưỡng $\tau$ ứng với ngưỡng $a=\tau+1$ của Định nghĩa 08.8, vì $h(K)\le\tau$ tương đương $h(K)<\tau+1$.

::: example Ví dụ 08.7 (Hạ ngưỡng trên năm bộ)
**Dữ kiện.** Dòng năm bộ của Ví dụ 08.4: (An, "đồ thị"), (Bình, "lọc"), (An, "băm"), (An, "đồ thị"), (Chi, "lọc"); $b=10$; $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$; ngân sách $G=3$ bộ.

**Tính.**

| $r$ | Bộ | $\tau$ trước | Thao tác | Mẫu sau bước | $\tau$ sau |
|---:|---|---:|---|---|---:|
| 1 | An | 9 | đưa vào | An | 9 |
| 2 | Bình | 9 | đưa vào | An, Bình | 9 |
| 3 | An | 9 | đưa vào | An, Bình, An | 9 |
| 4 | An | 9 | đưa vào; 4 bộ vượt $G$: $c=7$, xóa bộ của Bình | An, An, An | 6 |
| 5 | Chi | 6 | $4\le6$, đưa vào; 4 bộ vượt $G$: $c=4$, xóa bộ của Chi | An, An, An | 3 |

**Diễn giải.** Sau bước 5, mẫu là mẫu theo khóa với $a=\tau+1=4$: giữ trọn An, bỏ trọn Bình và Chi. Ở bước 4, ngưỡng nhảy từ 9 xuống 6, bỏ qua các giá trị 9 và 8 không có bộ nào.

**Kiểm tra lại.** Các bộ đã đọc có $h\le3$ là ba bộ của An, đúng mẫu sau bước 5; mẫu có 3 bộ, bằng $G$.
:::

::: proposition Mệnh đề 08.14 (Bất biến của mẫu theo ngưỡng)
**Giả thiết.** Thuật toán 08.13 với $h$ cố định.

**Kết luận.** Sau mỗi bước, mẫu đúng bằng tập các bộ đã đọc có $h(K(t))\le\tau$. Do đó mẫu luôn là mẫu theo khóa với ngưỡng $a=\tau+1$, và $\tau$ không tăng.

**Điều kiện áp dụng.** Bước 3 xóa đúng các bộ có giá trị băm lớn nhất $c$ trong mẫu trước khi đặt $\tau\gets c-1$.

**Phạm vi.** Mệnh đề không nói gì về xác suất; tỷ lệ khóa $(\tau+1)/b$ giảm dần theo dòng.
:::

::: proof
**Bước 1 (khởi tạo).** Trước bộ đầu tiên, mẫu rỗng và chưa có bộ nào được đọc.

**Bước 2 (đưa bộ vào).** Giả sử bất biến đúng trước khi $t$ đến. Bước 2 đưa $t$ vào đúng khi $h(K(t))\le\tau$, nên bất biến đúng sau bước 2.

**Bước 3 (hạ ngưỡng).** Giả sử mẫu bằng tập các bộ đã đọc có $h\le\tau$ và mẫu khác rỗng. Gọi $c$ là giá trị băm lớn nhất trong mẫu, nên $c\le\tau$. Không bộ nào trong mẫu có giá trị trong khoảng $(c,\tau]$; theo bất biến, cũng không bộ đã đọc nào có giá trị trong khoảng đó. Xóa các bộ có giá trị $c$ để lại đúng các bộ đã đọc có $h\le c-1$, nên đặt $\tau\gets c-1$ giữ bất biến, và $\tau$ giảm. Theo quy nạp trên số bước, bất biến đúng sau mọi bước; $\tau$ chỉ thay đổi ở bước 3, và ở đó nó giảm. $\square$
:::

**Trong thực hành.** Chỉ mục có thứ tự trên giá trị băm là một cây tìm kiếm cân bằng mà mỗi nút giữ danh sách các bộ cùng giá trị, nên tra giá trị lớn nhất và xóa cả danh sách đều nhanh. Ngân sách thường tính bằng byte; khi các bộ có độ dài khác nhau, $G$ là số bộ tối đa vừa ngân sách đó. Tình huống 08.1 áp dụng thuật toán cho ngân sách $10^8$ bộ.

Như vậy, chúng ta đã chỉ ra lấy mẫu từng bộ làm sai tỷ lệ lặp (Mệnh đề 08.6), thay bảng nhãn bằng hàm băm cố định (Định nghĩa 08.8, Thuật toán 08.9), chứng minh mẫu giữ trọn từng khóa và giữ mỗi khóa với xác suất $a/b$ (Mệnh đề 08.10), tính cỡ mẫu kỳ vọng $ar/b$ (Hệ quả 08.12), và giữ ngân sách bằng ngưỡng giảm dần (Thuật toán 08.13, Mệnh đề 08.14). Tuy nhiên, cỡ mẫu theo khóa phụ thuộc vào số bộ của các khóa được chọn: với tỷ lệ cố định, nó tăng theo dòng; với ngân sách cố định, tỷ lệ khóa giảm dần và một khóa nhiều bộ có thể bị đẩy trọn ra khỏi mẫu. Trong Mục 3, chúng ta đổi đơn vị chọn từ khóa sang vị trí trên dòng và xây lấy mẫu hồ chứa với cỡ mẫu cố định.

## 3. Lấy mẫu hồ chứa

Mẫu theo khóa của Mục 2 không chặn cỡ: ở Ví dụ 08.6, một khóa có $10^6$ bộ chiếm $10^6$ ô của mẫu khi được giữ, và cỡ mẫu kỳ vọng $ar/b$ tăng theo dòng (Hệ quả 08.12). Nhiều phân tích chỉ cần một mẫu đại diện có đúng $s$ phần tử ở mọi thời điểm, trong đó mọi phần tử đã đọc có cùng cơ hội có mặt. Chúng ta cần một thuật toán dòng giữ đúng $s$ phần tử mà không biết trước độ dài dòng.

<!-- note-topic-id: lec-08-topic-07 -->
### 3.1 Mẫu cỡ cố định và ý tưởng hồ chứa

::: example Ví dụ 08.8 (Mẫu hai phần tử trên dòng mười phần tử)
**Dữ kiện.** Dòng a, x, c, y, z, k, c, d, e, g của trang chiếu MMDS (Streams 1, tr.18); cần giữ $s=2$ phần tử. Đơn vị chọn là vị trí: chữ c ở vị trí 3 và vị trí 7 là hai phần tử khác nhau.

**Tính.** Sau $r=5$ phần tử, mỗi phần tử trong a, x, c, y, z cần có mặt với xác suất $2/5$. Sau $r=7$ phần tử, mỗi phần tử trong bảy phần tử đầu cần xác suất $2/7$. Cách trực tiếp là lưu cả $r$ phần tử rồi rút ngẫu nhiên $2$ phần tử; cách này cho đúng xác suất nhưng bộ nhớ tăng theo $r$.

**Diễn giải.** Xác suất cần đạt giảm khi dòng dài ra, nên phần tử đã giữ phải có lúc bị thay.

**Kiểm tra lại.** Với $r=5$, tổng các xác suất có mặt là $5\cdot\frac25=2=s$, đúng số ô.
:::

Một cách trực quan, hồ chứa (reservoir) giống mẫu theo khóa ở quy tắc ngưỡng: giữ khi một số đều không vượt ngưỡng, $j\le s$ thay cho $h(K)<a$. Nó khác ở hai chỗ: số được rút lại ở mỗi vị trí thay vì băm từ khóa, và một phần tử đã giữ có thể bị thay. Khi phần tử thứ $r>s$ đến, rút một số nguyên $j$ đều trong $\{1,\ldots,r\}$ và thay ô $j$ của hồ chứa khi $j\le s$. Một số $j$ gộp hai quyết định của trang chiếu MMDS (Streams 1, tr.19). Thứ nhất, $x_r$ được nhận với xác suất $s/r$, vì đúng $s$ trong $r$ giá trị đồng khả năng thỏa $j\le s$. Thứ hai, với điều kiện $x_r$ được nhận, $j$ đều trên $\{1,\ldots,s\}$, nên ô bị thay được chọn đều trong $s$ ô. Mô tả này chưa cho biết xác suất có mặt của các phần tử cũ; Định nghĩa 08.15 nêu yêu cầu đó.

::: example Ví dụ 08.9 (Vết chạy hồ chứa hai ô)
**Dữ kiện.** Dòng a, x, c, y, z; $s=2$; một lần rút do học phần dựng cho $j=2,4,1$ ở $r=3,4,5$.

**Tính.**

| $r$ | Phần tử | $j$ | Thao tác | Hồ chứa sau bước |
|---:|---|---:|---|---|
| 1 | a | — | $r\le s$, ghi ô 1 | [a] |
| 2 | x | — | $r\le s$, ghi ô 2 | [a, x] |
| 3 | c | 2 | $2\le2$, c thay ô 2 | [a, c] |
| 4 | y | 4 | $4>2$, bỏ y | [a, c] |
| 5 | z | 1 | $1\le2$, z thay ô 1 | [z, c] |

**Diễn giải.** Theo quy tắc, c được nhận với xác suất $2/3$, y với $2/4$, z với $2/5$; lần rút này nhận c và z, bỏ y. Các số $j$ là một kết cục của bộ sinh, không phải xác suất.

**Kiểm tra lại.** Mỗi $j$ nằm trong miền của nó: $2\in\{1,2,3\}$, $4\in\{1,\ldots,4\}$, $1\in\{1,\ldots,5\}$; hồ chứa luôn có $\min(r,2)$ phần tử.
:::

![Bảng vết với s bằng 2 trên dòng a, x, c, y, z: r bằng 1 ghi a vào ô 1; r bằng 2 ghi x vào ô 2; r bằng 3 rút j bằng 2, c thay ô 2; r bằng 4 rút j bằng 4 lớn hơn s nên bỏ y; r bằng 5 rút j bằng 1, z thay ô 1; hồ cuối là z, c.](img/lec-08/reservoir-trace.svg)

Hình đọc theo hàng giống bảng trên: mỗi hàng là một bước $r$, cột $j$ ghi số rút, và ô bị thay được tô đậm. Ở $r=4$, hồ chứa không đổi vì $j$ rơi ra ngoài $\{1,2\}$.

### 3.2 Đặc tả và thuật toán

::: definition Định nghĩa 08.15 (Mẫu hồ chứa cỡ $s$)
Cho dòng $x_1,x_2,\ldots$, số nguyên $s\ge1$ gọi là sức chứa, và một bộ sinh số ngẫu nhiên. Một **mẫu hồ chứa cỡ $s$** là mảng $W[1..s]$ được cập nhật sau mỗi phần tử sao cho:

- sau $r\le s$ phần tử, $W$ chứa đúng $r$ phần tử đã đọc;
- sau $r\ge s$ phần tử, $W$ chứa đúng $s$ phần tử đã đọc, và $\Pr[x_i\in W]=s/r$ với mọi $i\le r$.

Xác suất lấy theo các số do bộ sinh tạo ra; dòng được coi là cố định, không ngẫu nhiên.
:::

Định nghĩa đòi một tính chất về từng phần tử riêng lẻ. Nó không đòi các biến cố $x_i\in W$ độc lập; chúng không thể độc lập, vì tổng số phần tử có mặt luôn đúng bằng $s$. Nó cũng không đòi mọi tập con $s$ phần tử có cùng xác suất; tính chất mạnh hơn này là nội dung của Mệnh đề 08.18. Với Ví dụ 08.8, định nghĩa đòi đúng $2/5$ sau $r=5$ và $2/7$ sau $r=7$. So với mẫu theo khóa (Định nghĩa 08.8), đơn vị chọn là vị trí thay cho khóa, và cỡ mẫu cố định thay cho tỷ lệ cố định.

::: algorithm Thuật toán 08.16 (Lấy mẫu hồ chứa)
**Đầu vào.** Dòng $x_1,x_2,\ldots$; sức chứa $s\ge1$; bộ sinh số nguyên đều, độc lập với các lần rút trước.

**Đầu ra.** Sau $r$ phần tử, mảng $W$ chứa $\min(r,s)$ phần tử đã đọc.

**Giả thiết.** Mỗi lần rút, $j$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước, do đó độc lập với nội dung $W$.

1. Khởi tạo $r\gets0$ và $W$ rỗng.
2. Khi phần tử $x$ đến: tăng $r$ thêm 1.
3. Nếu $r\le s$: đặt $W[r]\gets x$.
4. Nếu $r>s$: rút $j$ đều trong $\{1,\ldots,r\}$; nếu $j\le s$ thì đặt $W[j]\gets x$, nếu không thì bỏ $x$.

```text
HỒ-CHỨA(x_1, x_2, …; s)
    r ← 0
    với mỗi phần tử x đến:
        r ← r + 1
        nếu r ≤ s: W[r] ← x
        ngược lại:
            j ← số nguyên đều trong {1, …, r}
            nếu j ≤ s: W[j] ← x
```

**Dừng.** Mỗi phần tử được xử lý sau số bước không đổi; thuật toán chạy chừng nào dòng còn phần tử.

**Trường hợp biên.** Khi $r\le s$, hồ chứa cả $r$ phần tử đã đọc. Với $s=1$, phần tử thứ $r$ thay ô duy nhất khi $j=1$, với xác suất $1/r$, và hồ là một phần tử chọn đều trong $r$ phần tử.

**Chi phí.** Mỗi phần tử: 1 phép tăng $r$, tối đa 1 lần rút và 1 lần ghi; chi tiết ở Mệnh đề 08.19.
:::

Một số $j$ vừa quyết định có nhận $x_r$ hay không ($j\le s$), vừa chọn ô bị thay. Điều còn phải chứng minh là phần tử cũ, sau nhiều lần có thể bị thay, vẫn có đúng xác suất $s/r$.

<!-- note-topic-id: lec-08-topic-08 -->
### 3.3 Xác suất $s/r$

Chứng minh của định lý sau dùng quy nạp theo $r$ và quy tắc nhân của xác suất có điều kiện (Kiến thức tiên quyết). Ký hiệu $W_r$ là nội dung hồ chứa sau phần tử thứ $r$; ký hiệu này chỉ dùng trong mục này.

::: theorem Định lý 08.17 (Xác suất có mặt $s/r$)
**Giả thiết.** $s\ge1$. Ở mỗi bước $r>s$, số $j$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước, do đó độc lập với nội dung $W$.

**Kết luận.** Với mọi $r\ge s$, $\lvert W_r\rvert=s$ và $\Pr[x_i\in W_r]=s/r$ với mọi $i\le r$.

**Điều kiện áp dụng.** Xác suất lấy theo các lần rút $j$; dòng cố định.

**Phạm vi.** Định lý nói về từng phần tử riêng lẻ. Nó không khẳng định các biến cố $x_i\in W_r$ độc lập.
:::

::: proof Chứng minh Định lý 08.17 (Xác suất có mặt)
**Bước 1 (cơ sở, $r=s$).** Các bước 1 đến $s$ ghi $x_1,\ldots,x_s$ vào $s$ ô khác nhau, nên $\lvert W_s\rvert=s$ và $\Pr[x_i\in W_s]=1=s/s$ với mọi $i\le s$.

**Bước 2 (giả thiết quy nạp).** Giả sử với một $r\ge s$, $\lvert W_r\rvert=s$ và $\Pr[x_i\in W_r]=s/r$ với mọi $i\le r$.

**Bước 3 (phần tử mới).** Ở bước $r+1$, $j$ đều trên $\{1,\ldots,r+1\}$ và $x_{r+1}$ vào hồ khi $j\le s$, đúng $s$ trong $r+1$ giá trị đồng khả năng. Do đó $\Pr[x_{r+1}\in W_{r+1}]=s/(r+1)$. Bước này không dùng giả thiết quy nạp.

**Bước 4 (phần tử cũ).** Xét $x_i$ với $i\le r$, và gọi $E_i$ là biến cố $x_i$ bị thay ở bước $r+1$. Phần tử $x_i$ còn trong $W_{r+1}$ khi và chỉ khi nó ở trong $W_r$ và $E_i$ không xảy ra. Theo quy tắc nhân,

$$
\begin{aligned}
\Pr[x_i\in W_{r+1}]
&=\Pr[x_i\in W_r]\cdot\bigl(1-\Pr[E_i\mid x_i\in W_r]\bigr)\\
&=\frac sr\cdot\Bigl(1-\frac1{r+1}\Bigr)\\
&=\frac sr\cdot\frac r{r+1}=\frac s{r+1}.
\end{aligned}
$$

Dòng thứ hai dùng giả thiết quy nạp cho thừa số đầu. Với thừa số sau: khi $x_i\in W_r$, phần tử $x_i$ nằm ở một ô cố định và bị thay khi và chỉ khi $j$ bằng đúng số hiệu ô đó. Vì $j$ độc lập với các lần rút trước, điều kiện $x_i\in W_r$ không đổi phân phối của $j$, nên xác suất bị thay là $1/(r+1)$. MMDS (§4.5.5, tr.148–149) trình bày cùng kỹ thuật để chọn vị trí cho các biến ước lượng mômen và chứng minh $s/n$ bằng quy nạp, với $n$ của sách là $r$ ở đây. Sách và trang chiếu MMDS (Streams 1, tr.21) tính xác suất không bị thay theo hai trường hợp: $x_{r+1}$ bị bỏ, hoặc được nhận nhưng thay ô khác, cho $\bigl(1-\frac s{r+1}\bigr)+\frac s{r+1}\cdot\frac{s-1}s=\frac r{r+1}$, cùng kết quả.

**Bước 5 (cỡ).** Ở bước $r+1>s$, thuật toán giữ nguyên $W$ hoặc ghi đè đúng một ô, nên $\lvert W_{r+1}\rvert=s$.

Bước 3 đến Bước 5 cho kết luận tại $r+1$; theo quy nạp, kết luận đúng với mọi $r\ge s$. $\square$
:::

![Bước r cộng 1 bằng 5 với s bằng 2: số rút j nhận năm giá trị đồng khả năng 1 đến 5; với j bằng 1 hoặc 2, phần tử mới x5 được nhận và thay ô j, xác suất 2/5; với j từ 3 đến 5, x5 bị bỏ, xác suất 3/5; phần tử cũ ở ô 1 bị thay khi j bằng 1, xác suất 1/5, nên còn lại với xác suất 4/5.](img/lec-08/reservoir-step.svg)

Hình vẽ bước $r+1=5$ với $s=2$, đúng bước cuối của Ví dụ 08.9. Năm ô của hàng $j$ ứng với năm giá trị đồng khả năng: hai ô đầu là Bước 3, cho $\Pr[x_5\in W_5]=2/5$; ô đậm $j=1$ là Bước 4 cho phần tử cũ ở ô 1. Một phần tử cũ có mặt sau $r=4$ với xác suất $2/4$ và sống qua bước 5 với xác suất $4/5$, nên có mặt sau $r=5$ với xác suất $\frac24\cdot\frac45=\frac25$.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "$j$ đều trên $\{1,\ldots,r\}$": nếu bộ sinh luôn trả $j$ trong $\{1,\ldots,s\}$, mọi phần tử mới đều được nhận, nên $\Pr[x_{r+1}\in W_{r+1}]=1$ thay cho $s/(r+1)$, và hồ chứa giữ các phần tử gần đây nhiều hơn.
- Bỏ "độc lập với các lần rút trước": với $s=2$, cho $j$ ở bước 4 bằng $j$ của bước 3 với xác suất $3/4$ và bằng $4$ với xác suất $1/4$. Số $j$ ở bước 4 vẫn đều trên $\{1,\ldots,4\}$, nhưng nếu $x_3$ được nhận ở bước 3 thì nó bị thay trừ khi $j=4$, nên $\Pr[x_3\in W_4]=\frac23\cdot\frac14=\frac16$ thay cho $\frac12$.

Bước 3 dùng tính đều của $j$; Bước 4 dùng cả tính đều và tính độc lập.

Định lý 08.17 chỉ nói về từng phần tử. Thuật toán cho một bảo đảm mạnh hơn, mà Định nghĩa 08.15 không đòi; đây là phần bổ sung, chứng minh bằng cùng kiểu quy nạp.

::: proposition Mệnh đề 08.18 (Mọi tập con cỡ $s$ đồng khả năng)
**Giả thiết.** Như Định lý 08.17.

**Kết luận.** Với mọi $r\ge s$ và mọi tập $A$ gồm $s$ vị trí trong $\{1,\ldots,r\}$, $\Pr[W_r=A]=1/\binom rs$, trong đó $W_r=A$ nghĩa là hồ chứa đúng các phần tử ở các vị trí của $A$.

**Điều kiện áp dụng.** Như Định lý 08.17.

**Phạm vi.** Mệnh đề suy ra Định lý 08.17, vì mỗi vị trí $i$ thuộc đúng $\binom{r-1}{s-1}$ tập $A$, và $\binom{r-1}{s-1}/\binom rs=s/r$.
:::

::: proof
**Bước 1 (cơ sở).** Với $r=s$, tập duy nhất là $\{1,\ldots,s\}$, xác suất $1=1/\binom ss$.

**Bước 2 ($r+1\notin A$).** Khi đó $W_{r+1}=A$ đúng khi $W_r=A$ và $j>s$. Theo giả thiết quy nạp và tính độc lập của $j$, xác suất là $\frac1{\binom rs}\cdot\frac{r+1-s}{r+1}=\frac1{\binom{r+1}s}$, vì $\binom{r+1}s=\binom rs\frac{r+1}{r+1-s}$.

**Bước 3 ($r+1\in A$).** Đặt $A'=A\setminus\{r+1\}$, gồm $s-1$ vị trí. Khi đó $W_{r+1}=A$ đúng khi $W_r=A'\cup\{\ell\}$ với một vị trí $\ell\le r$ ngoài $A'$, và $j$ bằng ô chứa phần tử ở vị trí $\ell$. Có $r-s+1$ cách chọn $\ell$, mỗi cách có xác suất $\frac1{\binom rs}\cdot\frac1{r+1}$, nên tổng là $\frac{r+1-s}{(r+1)\binom rs}=\frac1{\binom{r+1}s}$. $\square$
:::

Với $r=4$, $s=2$, mệnh đề cho mỗi cặp vị trí xác suất $1/\binom42=1/6$. Liệt kê trực tiếp: $j$ ở bước 3 có 3 giá trị và ở bước 4 có 4 giá trị, tạo $12$ kết cục đồng khả năng, và mỗi trong 6 cặp xuất hiện đúng 2 lần.

### 3.4 Chi phí

::: proposition Mệnh đề 08.19 (Chi phí của Thuật toán 08.16)
**Giả thiết.** Mô hình của Định nghĩa 08.3: đếm phép toán mỗi phần tử, bộ nhớ đếm bằng từ máy; thêm quy ước rút một số nguyên đều trong $\{1,\ldots,r\}$ tính là 1 phép. Giả thiết của Định lý 08.17 cho phần kỳ vọng.

**Kết luận.** Bộ nhớ gồm $s$ ô và bộ đếm $r$, tức $\Theta(s)$ từ máy; mỗi phần tử tốn $O(1)$ phép trong trường hợp xấu nhất. Sau $r>s$ phần tử có đúng $r-s$ lần rút, và số lần ghi vào $W$ có kỳ vọng

$$
s+\sum_{i=s+1}^{r}\frac si,\qquad s\Bigl(1+\ln\frac{r+1}{s+1}\Bigr)\le s+\sum_{i=s+1}^{r}\frac si\le s\Bigl(1+\ln\frac rs\Bigr).
$$

**Điều kiện áp dụng.** Cận $O(1)$ dựa vào quy ước rút một số tính là 1 phép.

**Phạm vi.** Số lần ghi là kỳ vọng; một lần chạy cụ thể có thể ghi nhiều hơn.
:::

::: proof
**Bước 1 (bộ nhớ, thời gian).** Thuật toán giữ $W[1..s]$ và $r$; mỗi phần tử tốn một phép tăng, tối đa một lần rút và một lần ghi.

**Bước 2 (số lần ghi).** $s$ phần tử đầu được ghi chắc chắn. Phần tử thứ $i>s$ được ghi khi $j\le s$, với xác suất $s/i$ (Bước 3 của chứng minh Định lý 08.17). Theo tuyến tính kỳ vọng, tổng số lần ghi có kỳ vọng $s+\sum_{i=s+1}^r s/i$.

**Bước 3 (cận).** Hàm $1/z$ giảm, nên $\int_i^{i+1}\frac{dz}z\le\frac1i\le\int_{i-1}^{i}\frac{dz}z$. Cộng theo $i=s+1,\ldots,r$ được $\ln\frac{r+1}{s+1}\le\sum_{i=s+1}^r\frac1i\le\ln\frac rs$; nhân với $s$ rồi cộng $s$. $\square$
:::

::: example Ví dụ 08.10 (Số lần ghi với $s=100$, $r=10^6$)
**Dữ kiện.** Hồ chứa $s=100$ ô trên dòng $r=10^6$ phần tử.

**Tính.** Số lần thay kỳ vọng sau khi hồ đầy là $\sum_{i=101}^{10^6}\frac{100}i\approx920{,}5$, nên tổng số lần ghi kỳ vọng khoảng $1\,020{,}5$. Cận trên của Mệnh đề 08.19 là $100(1+\ln10^4)\approx1\,021{,}0$; cận dưới là $100\bigl(1+\ln\frac{1\,000\,001}{101}\bigr)\approx1\,020{,}0$.

**Diễn giải.** Hồ chứa chỉ ghi khoảng $0{,}1\%$ số phần tử; phần lớn phần tử bị bỏ sau một lần rút.

**Kiểm tra lại.** $1\,020{,}0\le1\,020{,}5\le1\,021{,}0$.
:::

### 3.5 Nhầm lẫn, thực hành và so sánh với mẫu theo khóa

::: remark Nhận xét 08.20 (Nhầm lẫn thường gặp)
- $s/r$ không phải tỷ lệ lấy mẫu cố định: nó giảm khi dòng dài ra, khác tỷ lệ $a/b$ của Mục 2. Chỉ số $r$ tính cả phần tử vừa đến.
- $s/(r+1)$ và $1/(r+1)$ là hai xác suất khác nhau ở bước $r+1$: $s/(r+1)$ là xác suất nhận $x_{r+1}$, tức có một ô nào đó bị thay; $1/(r+1)$ là xác suất thay đúng ô đang chứa một phần tử cũ $x_i$ cho trước (Bước 3 và Bước 4 của chứng minh Định lý 08.17).
- Bộ sinh lệch hoặc phụ thuộc các lần rút trước phá Định lý 08.17 mà không đổi chi phí, như hai phản ví dụ sau định lý.
- Hồ chứa không giữ trọn khóa: các vị trí được chọn riêng, nên hai bộ của cùng một người có thể bị tách. Tỷ lệ truy vấn lặp tính trên hồ chứa lệch theo cùng chiều với Mục 2.1, nhưng không theo đúng công thức $d/(10u+19d)$, vì các vị trí không được giữ độc lập. Với $\eta_1=s/r$ và $\eta_2=\frac{s(s-1)}{r(r-1)}$, xác suất hai vị trí cho trước cùng có mặt (Mệnh đề 08.18), một truy vấn hai lần còn đủ hai bản với xác suất $\eta_2$ và đúng một bản với xác suất $2\eta_1-2\eta_2$, nên tỷ số các số đếm kỳ vọng là $\frac{d\eta_2}{u\eta_1+2d\eta_1-d\eta_2}$. Với $d>0$, tỷ số này bằng $d/(u+d)$ khi và chỉ khi $\eta_2(u+2d)=\eta_1(u+2d)$, tức $\eta_2=\eta_1$; nó tăng theo $\eta_2$, và $\eta_2/\eta_1=(s-1)/(r-1)<1$ khi $s<r$, nên nó nhỏ hơn tỷ lệ thật.
:::

::: remark Nhận xét 08.21 (Trong thực hành)
Giả thiết đều và độc lập của Định lý 08.17 được xấp xỉ bằng bộ sinh số giả ngẫu nhiên có hạt giống. Khi rút $j$ trong $\{1,\ldots,r\}$ từ một số đều trên $\{0,\ldots,2^{64}-1\}$, phép lấy dư cho $r$ chỉ đều khi $r$ chia hết $2^{64}$; với $r$ khác, các giá trị nhỏ được ưu tiên một chút, và cách rút đúng loại bỏ phần dư rồi rút lại. Bộ đếm $r$ vừa một từ 64 bit khi $r<2^{64}$ (Mục 1.4). Hồ chứa có cỡ cố định nên dùng được khi ngân sách bộ nhớ chỉ cho $s$ phần tử, nhưng không trả lời được thống kê theo người dùng. MMDS (hộp "A General Stream-Sampling Problem", tr.150) nối hai cấu trúc: khi một khóa trong mẫu theo khóa có quá nhiều bộ, giữ cho khóa đó một hồ chứa $s$ ô, để số bộ của mỗi khóa không vượt $s$. Hồ chứa chọn đều trên toàn bộ lịch sử, nên phần tử vừa đến có cùng xác suất có mặt $s/r$ như một phần tử rất cũ; muốn ưu tiên giai đoạn gần đây cần một cửa sổ, như cửa sổ DGIM và cửa sổ suy giảm mũ ở ghi chú Bài 09, Mục 6 và Mục 8.
:::

Bảng dưới đặt hai cấu trúc lấy mẫu của chương cạnh nhau.

| | Mẫu theo khóa | Hồ chứa |
|---|---|---|
| Đơn vị chọn | giá trị khóa | vị trí |
| Cỡ mẫu | tăng theo dòng, kỳ vọng $ar/b$ | $\min(r,s)$ |
| Nhất quán theo khóa | có (Mệnh đề 08.10) | không |
| Xác suất | $a/b$ mỗi khóa | $s/r$ mỗi phần tử (Định lý 08.17) |

::: exercise Bài tập 08.4 (Bộ của An trong hồ chứa)
Dòng có $1\,000$ bộ, trong đó An có 10 bộ; hồ chứa có $s=100$ ô. Tính kỳ vọng số bộ của An trong hồ sau khi đọc hết dòng. Hồ có giữ trọn 10 bộ của An không? Câu hỏi do học phần dựng; các bài tập của sách (§4.5.6) không có bài về hồ chứa.
:::

::: hint
Dùng Định lý 08.17 cho từng bộ của An, rồi tuyến tính kỳ vọng.
:::

::: solution
Mỗi bộ của An nằm trong hồ với xác suất $s/r=100/1\,000=0{,}1$ (Định lý 08.17). Theo tuyến tính kỳ vọng, số bộ kỳ vọng là $10\cdot0{,}1=1$. Kỳ vọng 1 không có nghĩa mỗi lần chạy có đúng một bộ của An: theo Mệnh đề 08.18, hồ không chứa bộ nào của An với xác suất $\binom{990}{100}/\binom{1000}{100}\approx0{,}347$. Hồ cũng không bảo đảm giữ trọn 10 bộ: các vị trí được chọn riêng, và theo Mệnh đề 08.18, cả 10 bộ của An cùng nằm trong hồ với xác suất $\binom{990}{90}/\binom{1000}{100}\approx6{,}6\cdot10^{-11}$. Vì vậy tỷ lệ truy vấn lặp của An không tính đúng trên hồ chứa; thống kê theo người dùng cần mẫu theo khóa.
:::

Như vậy, chúng ta đã có cấu trúc lấy mẫu thứ hai: hồ chứa giữ đúng $\min(r,s)$ phần tử (Định nghĩa 08.15, Thuật toán 08.16), mỗi phần tử đã đọc có mặt với xác suất $s/r$ (Định lý 08.17), mọi tập con cỡ $s$ đồng khả năng (Mệnh đề 08.18), với bộ nhớ $\Theta(s)$ và thời gian $O(1)$ mỗi phần tử (Mệnh đề 08.19). Tuy nhiên, cả hai cấu trúc lấy mẫu đều trả lời câu hỏi về phân phối. Câu hỏi "địa chỉ gửi thư này có thuộc danh sách $10^9$ địa chỉ được phép không" đòi biết một khóa cụ thể có trong tập hay không, và một mẫu không trả lời được: một địa chỉ được phép vắng mặt trong mẫu vẫn là địa chỉ được phép. Trong Mục 4, chúng ta xây Bloom filter cho câu hỏi thành viên này.

## 4. Lọc thành viên bằng Bloom filter

Hai cấu trúc lấy mẫu của Mục 2 và Mục 3 trả lời câu hỏi về phân phối. Bài toán lọc thư của ghi chú Bài 01 cần một câu hỏi khác: địa chỉ gửi của thư vừa đến có thuộc tập $10^9$ địa chỉ được phép hay không. Chúng ta cần một cấu trúc trả lời câu hỏi thành viên trên dòng, với bộ nhớ cố định và không bao giờ chặn nhầm một địa chỉ được phép.

<!-- note-topic-id: lec-08-topic-09 -->
### 4.1 Lọc theo danh sách cho phép

MMDS (§4.3.1, tr.139) đặt tình huống như sau. Tập $S$ gồm $m=10^9$ địa chỉ thư được tin là không phát tán thư rác. Mỗi địa chỉ dài từ 20 byte, nên lưu $S$ cần từ 20 GB. Bộ nhớ chính chỉ có 1 GB, tức $n=8\cdot10^9$ bit, và tra $S$ trên đĩa cho mỗi thư đến thì không theo kịp nhịp đến của dòng.

Một cách trực quan, hàm băm lại thay cho bảng lưu khóa, như ở Mục 2.2; điểm khác là mọi khóa của $S$ được ghi vào cấu trúc trước khi dòng đến. Sách dùng một hàm băm từ địa chỉ vào $8\cdot10^9$ bit: mỗi địa chỉ của $S$ đặt bit của nó thành 1. Khi thư đến, nếu bit của địa chỉ gửi bằng 0 thì địa chỉ đó chắc chắn không thuộc $S$, vì mọi địa chỉ của $S$ đã đặt bit của mình. Nếu bit bằng 1, địa chỉ chỉ có thể thuộc $S$, vì nhiều địa chỉ có thể băm vào cùng một bit. Có $10^9$ địa chỉ đặt bit trên $8\cdot10^9$ bit, nên khoảng $1/8$ số bit bằng 1, và khoảng $1/8$ số địa chỉ ngoài $S$ lọt qua bước lọc. Mô tả này chưa cho biết tỷ lệ chính xác hay cách giảm tỷ lệ đó; Bloom filter dùng $k$ hàm băm thay cho một để giảm số lần nhận nhầm.

![Khóa của dòng đi qua Bloom filter, bộ lọc kiểm tra k bit; nếu có một bit bằng 0 thì khóa bị loại vì chắc chắn không thuộc S, nhánh này vẽ nét đứt; nếu mọi bit bằng 1 thì kết quả là có thể thuộc và khóa đi tiếp tới phép tra cứu chính xác trên S.](img/lec-08/bloom-pipeline.svg)

Hình đặt Bloom filter trước phép tra chính xác. Chỉ khóa nhận "có thể thuộc" mới đi tới phép tra $S$ trên đĩa, nên số lần tra đĩa bằng số khóa thuộc $S$ cộng số khóa ngoài $S$ bị nhận nhầm.

### 4.2 Ví dụ Bloom filter 11 bit

Hai ví dụ sau chạy một Bloom filter nhỏ với $n=11$ bit và $k=2$ hàm băm, theo trang chiếu của Ullman cho học phần CS246 (2017, tr.5–8). Hàm $h_1(v)$ ghép các bit ở vị trí lẻ của biểu diễn nhị phân của $v$, đếm từ phải và bắt đầu từ 1, giữ thứ tự từ cao xuống thấp, rồi lấy dư cho 11. Hàm $h_2(v)$ làm như vậy với các bit ở vị trí chẵn. Mảng $B$ hiển thị chỉ số 0 đến 10 từ trái sang phải. Cặp hàm này chỉ là một ví dụ cụ thể, không thuộc định nghĩa Bloom filter.

::: example Ví dụ 08.11 (Thêm ba khóa vào mảng 11 bit)
**Dữ kiện.** $S=\{25,159,585\}$, $n=11$, $k=2$; mảng ban đầu toàn 0.

**Tính.**

| Khóa $v$ | Nhị phân | Bit lẻ | Bit chẵn | $(h_1,h_2)$ | Mảng $B$ sau khi thêm |
|---:|---|---|---|---|---|
| 25 | $11001_2$ | $101_2=5$ | $10_2=2$ | $(5,2)$ | 00100100000 |
| 159 | $10011111_2$ | $0111_2=7$ | $1011_2=11\equiv0$ | $(7,0)$ | 10100101000 |
| 585 | $1001001001_2$ | $01001_2=9$ | $10010_2=18\equiv7$ | $(9,7)$ | 10100101010 |

**Diễn giải.** Khóa 585 đặt lại bit 7, bit mà 159 đã đặt, nên mảng không đổi ở vị trí đó. Sau ba khóa, mảng có 5 bit bằng 1.

**Kiểm tra lại.** Các bit bằng 1 là $0,2,5,7,9$, đúng hợp các vị trí $\{5,2\}\cup\{7,0\}\cup\{9,7\}$.
:::

![Mảng 11 bit, chỉ số 0 đến 10: ban đầu toàn 0; thêm 25 vào vị trí 5 và 2 được 00100100000; thêm 159 vào vị trí 7 và 0 được 10100101000; thêm 585 vào vị trí 9 và 7 được 10100101010, bit 7 đã bằng 1 nên không đổi; bit vừa đặt ở mỗi bước có khung đậm.](img/lec-08/bloom-11bit-them.svg)

::: example Ví dụ 08.12 (Kiểm tra hai khóa trên mảng 11 bit)
**Dữ kiện.** Mảng $B=10100101010$ của Ví dụ 08.11, cùng $h_1$, $h_2$. Khóa 118 lấy từ trang chiếu Ullman tr.8; khóa 29 do học phần chọn.

**Tính.**

| Khóa $y$ | Nhị phân | $(h_1,h_2)$ | Bit đọc được | Trả lời |
|---:|---|---|---|---|
| 118 | $1110110_2$ | $(14\bmod 11,5)=(3,5)$ | $B[3]=0$ (dừng) | chắc chắn không thuộc |
| 29 | $11101_2$ | $(7,2)$ | $B[7]=1$, $B[2]=1$ | có thể thuộc |

**Diễn giải.** Khóa 118 bị loại ngay ở $h_1$, dù bit 5 bằng 1. Khóa 29 không thuộc $S$ nhưng qua bộ lọc: bit 7 do 159 và 585 đặt, bit 2 do 25 đặt. Đây là một trường hợp nhận nhầm, và ứng dụng phải tra $S$ để phát hiện nó.

**Kiểm tra lại.** $29\notin\{25,159,585\}$; cả hai bit $7$ và $2$ nằm trong tập bit 1 là $\{0,2,5,7,9\}$.
:::

![Mảng 10100101010, chỉ số 0 đến 10; bit 2 và bit 7 bằng 1 có khung đậm, là hai vị trí của khóa 29; bit 3 bằng 0 có khung nét đứt, là vị trí h1 của khóa 118.](img/lec-08/bloom-11bit-mini.svg)

### 4.3 Đặc tả và thuật toán

::: definition Định nghĩa 08.22 (Bloom filter, dương giả, âm giả)
Cho tập $S\subseteq\mathcal K$ gồm $m$ khóa, số bit $n\ge1$ và $k\ge1$ hàm băm $h_1,\ldots,h_k:\mathcal K\to\{0,\ldots,n-1\}$. **Bloom filter** của $S$ là mảng bit $B[0..n-1]$ trong đó $B[c]=1$ khi và chỉ khi $c=h_i(v)$ với một khóa $v\in S$ và một chỉ số $i\in\{1,\ldots,k\}$. Với khóa truy vấn $y\in\mathcal K$, Bloom filter trả "chắc chắn không thuộc" nếu $B[h_i(y)]=0$ với một $i$ nào đó, và trả "có thể thuộc" nếu ngược lại.

Một **dương giả** (false positive) là một khóa $y\notin S$ nhận câu trả lời "có thể thuộc". Một **âm giả** (false negative) là một khóa $y\in S$ nhận câu trả lời "chắc chắn không thuộc".
:::

Bloom filter trả lời câu hỏi thành viên một phía. Câu trả lời "chắc chắn không thuộc" luôn đúng dưới bốn điều kiện của Định lý 08.25; câu trả lời "có thể thuộc" cần tra $S$ khi quyết định không được sai. Trong lọc thư, dương giả là lỗi chấp nhận được, vì thư rác lọt qua bước lọc sẽ bị chặn ở bước tra chính xác. Âm giả thì không chấp nhận được, vì thư hợp lệ bị chặn. Trong Ví dụ 08.11–08.12, $n=11$, $k=2$, $m=3$, và khóa 29 là một dương giả. So với mẫu theo khóa (Định nghĩa 08.8), Bloom filter cũng dựa vào tính tất định của hàm băm, nhưng ghi dấu vết của mọi khóa trong $S$ thay vì chọn một phần khóa.

::: algorithm Thuật toán 08.23 (Xây Bloom filter)
**Đầu vào.** Tập $S$ gồm $m$ khóa; số bit $n$; hàm băm $h_1,\ldots,h_k$ vào $\{0,\ldots,n-1\}$.

**Đầu ra.** Mảng $B[0..n-1]$ của Định nghĩa 08.22.

**Giả thiết.** Các hàm $h_i$ tất định và được giữ nguyên giữa lúc xây và lúc truy vấn.

1. Đặt mọi bit $B[0..n-1]$ bằng 0.
2. Với mỗi khóa $v\in S$ và mỗi $i=1,\ldots,k$: đặt $B[h_i(v)]\gets1$.
3. Trả $B$.

```text
XÂY-BLOOM(S; n, h_1, …, h_k)
    B[0 … n−1] ← 0
    với mỗi khóa v trong S:
        với i = 1, …, k: B[h_i(v)] ← 1
    trả B
```

**Dừng.** Bước 2 có đúng $km$ lượt.

**Trường hợp biên.** $S$ rỗng cho mảng toàn 0, và mọi truy vấn nhận "chắc chắn không thuộc". Hai khóa, hoặc hai hàm của cùng một khóa, đặt cùng một bit thì bit đó không đổi.

**Chi phí.** Bước 1: $n$ phép ghi bit. Bước 2: $km$ phép băm và $km$ phép ghi bit. Bộ nhớ: $n$ bit, không phụ thuộc độ dài khóa.
:::

::: algorithm Thuật toán 08.24 (Kiểm tra thành viên)
**Đầu vào.** Khóa truy vấn $y$; mảng $B$ do Thuật toán 08.23 xây; cùng $h_1,\ldots,h_k$.

**Đầu ra.** "Chắc chắn không thuộc" hoặc "có thể thuộc", theo Định nghĩa 08.22.

**Giả thiết.** Như Thuật toán 08.23; mảng chỉ được đọc.

1. Với $i=1,\ldots,k$: nếu $B[h_i(y)]=0$ thì trả "chắc chắn không thuộc" và dừng.
2. Trả "có thể thuộc".

```text
KIỂM-TRA-BLOOM(y; B, h_1, …, h_k)
    với i = 1, …, k:
        nếu B[h_i(y)] = 0: trả "chắc chắn không thuộc"
    trả "có thể thuộc"
```

**Dừng.** Vòng lặp có tối đa $k$ lượt.

**Trường hợp biên.** Khóa thuộc $S$ và khóa dương giả luôn đọc đủ $k$ bit; khóa bị loại dừng ở bit 0 đầu tiên, như 118 dừng ngay ở $h_1(118)=3$.

**Chi phí.** Trường hợp xấu nhất: $k$ phép băm và $k$ phép đọc bit.
:::

Phép quyết định của Thuật toán 08.24 là đọc bit: gặp một bit 0 thì dừng và loại $y$. Mảng chỉ đổi bit từ 0 sang 1, không bao giờ ngược lại; tính chất này là cơ sở của định lý sau.

<!-- note-topic-id: lec-08-topic-10 -->
### 4.4 Không âm giả

::: theorem Định lý 08.25 (Không có âm giả)
**Giả thiết.** Mảng $B$ được xây bằng Thuật toán 08.23 và:

1. sau khi xây, không bit nào bị xóa hay đặt lại về 0;
2. truy vấn dùng đúng các hàm $h_1,\ldots,h_k$ và đúng mảng đã xây;
3. các hàm băm tất định;
4. mọi phép ghi bit đã hoàn tất trước truy vấn.

**Kết luận.** Với mọi $y\in S$, Thuật toán 08.24 trả "có thể thuộc".

**Điều kiện áp dụng.** Định lý không dùng xác suất; nó đúng với mọi lựa chọn hàm băm thỏa điều kiện 3.

**Phạm vi.** Định lý chỉ nói về khóa thuộc $S$. Khóa ngoài $S$ vẫn có thể là dương giả, như khóa 29 của Ví dụ 08.12.
:::

::: proof
**Bước 1 (lúc xây).** Vì $y\in S$, bước 2 của Thuật toán 08.23 đặt $B[h_i(y)]\gets1$ với mọi $i$, và theo điều kiện 4 các phép ghi này đã xong trước truy vấn.

**Bước 2 (lúc truy vấn).** Theo điều kiện 1, không bit nào trở về 0. Theo điều kiện 2 và 3, vị trí đọc ở lượt $i$ của Thuật toán 08.24 chính là $h_i(y)$ đã đặt ở Bước 1. Vậy mọi bit được đọc bằng 1, vòng lặp không dừng sớm, và thuật toán trả "có thể thuộc". $\square$
:::

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ điều kiện 1: trong Ví dụ 08.11, gỡ 585 bằng cách đặt bit 9 và bit 7 về 0 làm $B[7]=0$, và khóa 159 thuộc $S$ nhận "chắc chắn không thuộc".
- Bỏ điều kiện 2: nếu truy vấn dùng $h_1(v)+1\bmod 11$ thay cho $h_1$, khóa 25 thuộc $S$ đọc bit 6 và bit 2; trên mảng 10100101010, $B[6]=0$, nên 25 nhận "chắc chắn không thuộc".
- Bỏ điều kiện 3: một hàm có thành phần ngẫu nhiên ở mỗi lần gọi có thể trả lúc truy vấn một vị trí khác lúc xây.
- Bỏ điều kiện 4: truy vấn 159 khi Thuật toán 08.23 mới ghi $B[7]$ cho 159 mà chưa ghi $B[0]$; mảng tạm 00100101000 có $B[0]=0$, nên 159 nhận "chắc chắn không thuộc".

Bước 1 dùng điều kiện 4; Bước 2 dùng điều kiện 1, 2 và 3. Trong mô hình của chương, mảng được xây xong rồi mới đọc và mỗi $h_i$ là một hàm cố định, nên điều kiện 3 và 4 tự thỏa; điều kiện 1 và 2 là hai điều kiện có thể bị vi phạm khi vận hành.

<!-- note-topic-id: lec-08-topic-11 -->
### 4.5 Mật độ bit và xác suất dương giả

Định lý 08.25 không nói gì về khóa ngoài $S$. Để biết bao nhiêu khóa ngoài $S$ lọt qua, chúng ta cần một mô hình xác suất cho các hàm băm. MMDS (§4.3.3, tr.140) dùng mô hình phi tiêu: mỗi phép băm của một khóa trong $S$ như một phi tiêu rơi đều vào một trong $n$ bia, độc lập với các phi tiêu khác. Có $km$ phi tiêu. Phân tích này đi theo cùng cách làm với Định lý 06.7 (Kiến thức tiên quyết): xác suất cho một lần thử, tích các xác suất độc lập, rồi biến cố bù.

::: example Ví dụ 08.13 (Tám bia, bốn phi tiêu)
**Dữ kiện.** $n=8$ bia, 4 phi tiêu, mỗi phi tiêu rơi đều và độc lập.

**Tính.** Một bia cố định không bị một phi tiêu trúng với xác suất $7/8$. Bốn phi tiêu độc lập, nên bia không bị trúng với xác suất $(7/8)^4=2401/4096\approx0{,}586$, và bị trúng ít nhất một lần với xác suất $\approx0{,}414$.

**Kiểm tra lại.** Kỳ vọng số bia bị trúng là $8\cdot0{,}414\approx3{,}31$, nhỏ hơn 4 vì có phi tiêu rơi trùng bia.
:::

::: lemma Bổ đề 08.26 (Mật độ bit 1)
**Giả thiết.** $km$ giá trị $h_i(v)$, $v\in S$, $i=1,\ldots,k$, độc lập và đều trên $\{0,\ldots,n-1\}$.

**Kết luận.** Với mọi vị trí $c$, $\Pr[B[c]=0]=(1-1/n)^{km}$. Số bit 1 $X$ có kỳ vọng $\mathbb E[X]=nq$, với $q=1-(1-1/n)^{km}$.

**Điều kiện áp dụng.** Xác suất lấy theo cách chọn các hàm băm; $S$ cố định.

**Phạm vi.** Bổ đề chính xác dưới mô hình phi tiêu; nó không nói các bit độc lập.
:::

::: proof
**Bước 1.** Bit $c$ bằng 0 khi và chỉ khi không giá trị băm nào bằng $c$. Mỗi giá trị khác $c$ với xác suất $1-1/n$; $km$ giá trị độc lập, nên xác suất là $(1-1/n)^{km}$.

**Bước 2.** $X=\sum_c\mathbf 1[B[c]=1]$; mỗi chỉ báo có kỳ vọng $q$, nên theo tuyến tính kỳ vọng $\mathbb E[X]=nq$. $\square$
:::

Đại lượng $q$ vì vậy là mật độ bit 1 kỳ vọng. Viết $(1-1/n)^{km}=\bigl((1-1/n)^n\bigr)^{km/n}$ và dùng giới hạn $(1-1/n)^n\approx e^{-1}$ ở phần tiên quyết, ta được $q\approx1-e^{-km/n}$ khi $n$ lớn. Các bit không độc lập. Với hai vị trí $c\ne c'$, cả hai bit bằng 0 khi không phi tiêu nào rơi vào hai vị trí đó, nên $\Pr[B[c]=B[c']=0]=(1-2/n)^{km}$; vì $1-2/n<(1-1/n)^2$, số này nhỏ hơn $\Pr[B[c]=0]\Pr[B[c']=0]=(1-1/n)^{2km}$, tức hai bit tương quan âm. Mệnh đề 08.27 không cần các bit độc lập.

Một khóa $y\notin S$ là dương giả khi cả $k$ bit $B[h_1(y)],\ldots,B[h_k(y)]$ bằng 1. Mệnh đề sau tính xác suất này và đặt nó cạnh hai xấp xỉ quen dùng.

::: proposition Mệnh đề 08.27 (Xác suất dương giả và hai xấp xỉ)
**Giả thiết.** Như Bổ đề 08.26; thêm: với $y\notin S$ cố định, $k$ giá trị $h_1(y),\ldots,h_k(y)$ độc lập, đều trên $\{0,\ldots,n-1\}$ và độc lập với các giá trị băm của $S$.

**Kết luận.**

(a) $p_{FP}=\mathbb E\bigl[(X/n)^k\bigr]$.

(b) $p(k)=\bigl(1-e^{-km/n}\bigr)^k\le q^k\le p_{FP}$; khi $k=1$, $q=p_{FP}$.

**Điều kiện áp dụng.** Xác suất lấy theo cách chọn mọi hàm băm; $S$ và $y$ cố định.

**Phạm vi.** $q^k$ và dạng mũ $p(k)$ là cận dưới của $p_{FP}$ dưới mô hình này; khi $n$ lớn, ba đại lượng gần nhau.
:::

::: proof
**Bước 1 (điều kiện theo mảng).** Cố định các giá trị băm của $S$, tức cố định mảng, có $X$ bit 1. Mỗi vị trí $h_i(y)$ đều và độc lập với mảng, nên rơi vào bit 1 với xác suất $X/n$. Các vị trí độc lập với nhau, nên cả $k$ vị trí rơi vào bit 1 với xác suất $(X/n)^k$; khi hai vị trí trùng nhau, phép tính này vẫn đúng, vì mỗi vị trí được rút độc lập.

**Bước 2 (lấy kỳ vọng).** Lấy kỳ vọng theo mảng được $p_{FP}=\mathbb E[(X/n)^k]$, tức phần (a).

**Bước 3 (Jensen).** Hàm $z\mapsto z^k$ lồi trên $[0,1]$ khi $k\ge1$. Theo bất đẳng thức Jensen và Bổ đề 08.26, $\mathbb E[(X/n)^k]\ge(\mathbb E[X]/n)^k=q^k$. Khi $k=1$, hai vế bằng nhau.

**Bước 4 (dạng mũ).** Từ $1-1/n\le e^{-1/n}$ suy ra $(1-1/n)^{km}\le e^{-km/n}$, nên $q\ge1-e^{-km/n}$ và $q^k\ge p(k)$. $\square$
:::

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "các vị trí của $y$ độc lập với các giá trị băm của $S$": nếu hàm băm chỉ đọc một phần của khóa và $y$ trùng phần đó với một khóa $v\in S$, thì $h_i(y)=h_i(v)$ với mọi $i$, và $y$ luôn lọt qua; xác suất là 1 thay cho $p_{FP}$.
- Bỏ "các $h_i(y)$ độc lập với nhau": nếu $h_1=\cdots=h_k$, mỗi khóa chỉ đặt một bit và khóa ngoài $S$ chỉ đọc một bit; với $n/m=8$, xác suất lọt qua là $1-(1-1/n)^m\approx0{,}1175$ dù $k=6$, thay cho khoảng $0{,}0216$.

Bước 1 dùng hai giả thiết này; Bước 3 dùng tính lồi của $z\mapsto z^k$; Bước 4 không dùng giả thiết xác suất nào.

Phần (a) chỉ ra nguồn gốc của sai số khi dùng $q^k$: sai số đến từ việc thay kỳ vọng của $(X/n)^k$ bằng lũy thừa của kỳ vọng, chứ không đến từ việc các vị trí truy vấn có thể trùng. Dạng mũ $p(k)$ là công thức của MMDS (tr.141) và của mọi phép định cỡ trong phần còn lại của mục.

::: example Ví dụ 08.14 (Một và hai hàm băm trên tình huống lọc thư)
**Dữ kiện.** $n=8\cdot10^9$, $m=10^9$, nên $km/n=k/8$ (MMDS Ví dụ 4.3–4.4, tr.141).

**Tính.** Với $k=1$: $p(1)=1-e^{-1/8}\approx0{,}1175$; phép tính hữu hạn $q=1-(1-1/n)^m=0{,}1175031$ trùng tới sáu chữ số, và theo Mệnh đề 08.27(b), với $k=1$ số này chính là $p_{FP}$. Với $k=2$: $p(2)=(1-e^{-1/4})^2\approx0{,}0489$.

**Diễn giải.** Hai hàm băm giảm tỷ lệ nhận nhầm từ khoảng $11{,}75\%$ xuống khoảng $4{,}89\%$, dù mảng nhận gấp đôi số phi tiêu và mật độ bit 1 tăng từ $0{,}1175$ lên $1-e^{-1/4}\approx0{,}2212$.

**Kiểm tra lại.** Ví dụ 4.4 của sách in $0{,}0493$ cho $k=2$; tính lại $(1-e^{-0{,}25})^2=0{,}048929$, nên giá trị tính lại được dùng.
:::

::: example Ví dụ 08.15 (Ba mức xấp xỉ trên mảng 11 bit)
**Dữ kiện.** $n=11$, $k=2$, $m=3$ như Ví dụ 08.11, nên có $km=6$ phi tiêu.

**Tính.** $q=1-(10/11)^6\approx0{,}4355$, nên $\mathbb E[X]=11q\approx4{,}79$. Liệt kê $11^6$ cách rơi của sáu phi tiêu cho $p_{FP}=\mathbb E[(X/11)^2]\approx0{,}1951$. Ta có $q^2\approx0{,}1897$ và $p(2)=(1-e^{-6/11})^2\approx0{,}1768$.

**Diễn giải.** Thứ tự $0{,}1768\le0{,}1897\le0{,}1951$ đúng như Mệnh đề 08.27(b); với $n=11$ ba mức còn cách nhau rõ, còn với $n=8\cdot10^9$ chúng trùng tới nhiều chữ số. Mảng cụ thể của Ví dụ 08.11 có $X=5$, nên với các hàm băm đã cố định, một khóa ngẫu nhiên ngoài $S$ lọt qua với tỷ lệ $(5/11)^2\approx0{,}2066$.

**Kiểm tra lại.** $11\cdot0{,}4355=4{,}79$ nằm giữa $0$ và $\min(11,6)=6$.
:::

<!-- note-topic-id: lec-08-topic-12 -->
### 4.6 Số hàm băm tối ưu

Ví dụ 08.14 cho thấy tăng $k$ từ 1 lên 2 làm $p$ giảm. Hai lực tác động ngược chiều. Mỗi hàm băm thêm một phép thử mà khóa ngoài $S$ phải vượt qua, nên số mũ $k$ tăng. Nhưng mỗi hàm băm cũng thêm $m$ phi tiêu, nên $q$ tăng. Với $n/m=8$, $p(1)\approx0{,}118$, $p(6)\approx0{,}022$ và $p(10)\approx0{,}034$. Khi $k\to\infty$, $p(k)\to1$: $e^{-km/n}\to0$ nhanh hơn $1/k$, nên $\ln p(k)=k\ln(1-e^{-km/n})\to0$, nghĩa là gần như mọi bit bằng 1 và mọi khóa đều lọt qua. Định lý sau tìm điểm cân bằng.

::: theorem Định lý 08.28 (Số hàm băm tối ưu)
**Giả thiết.** $n$, $m$ dương cố định; $p(k)=(1-e^{-km/n})^k$ xét như hàm của biến thực $k>0$.

**Kết luận.** $p$ giảm chặt trên $(0,k^*]$ và tăng chặt trên $[k^*,\infty)$, với $k^*=(n/m)\ln2$. Do đó $p$ đạt giá trị nhỏ nhất trên $k>0$ tại $k^*$, và $p(k^*)=2^{-k^*}$.

**Điều kiện áp dụng.** Kết luận nói về dạng mũ $p(k)$, công thức định cỡ của Mệnh đề 08.27; nó không phải mệnh đề về $p_{FP}$ chính xác.

**Phạm vi.** $k$ thực; với $k$ nguyên, xem Hệ quả 08.29.
:::

Chứng minh đưa $\ln p(k)$ về một hàm của $\theta=e^{-km/n}$, chính là xác suất một bit bằng 0 theo dạng mũ. Dấu của đạo hàm khi đó trùng dấu của một hàm $\phi(\theta)$ đổi dấu đúng tại $\theta=1/2$, nên chỉ có một điểm dừng, và việc xét dấu hai bên điểm đó cho cực tiểu toàn cục.

::: proof
**Bước 1 (đổi biến).** Đặt $\rho=m/n>0$, $z=k\rho$ và $\theta=e^{-z}$. Khi $k$ chạy trên $(0,\infty)$, $\theta$ giảm chặt từ 1 xuống 0. Đặt $\lambda(k)=\ln p(k)=k\ln(1-e^{-k\rho})$; vì $\ln$ tăng chặt, $p$ và $\lambda$ cùng tăng, cùng giảm (Kiến thức tiên quyết).

**Bước 2 (đạo hàm).** Theo quy tắc tích và quy tắc chuỗi,

$$
\begin{aligned}
\lambda'(k)
&=\ln(1-e^{-k\rho})+k\cdot\frac{\rho e^{-k\rho}}{1-e^{-k\rho}}\\
&=\ln(1-\theta)+\frac{z\theta}{1-\theta}
=\ln(1-\theta)-\frac{\theta\ln\theta}{1-\theta}\\
&=\frac{\phi(\theta)}{1-\theta},\qquad \phi(\theta)=(1-\theta)\ln(1-\theta)-\theta\ln\theta .
\end{aligned}
$$

Dòng thứ hai thay $z=-\ln\theta$. Vì $1-\theta>0$, dấu của $\lambda'(k)$ là dấu của $\phi(\theta)$.

**Bước 3 (dấu của $\phi$ trên $(0,1/2)$).** Mở rộng $\phi(0)=0$, liên tục vì $\theta\ln\theta\to0$ khi $\theta\to0^+$. Ta có $\phi(1/2)=\frac12\ln\frac12-\frac12\ln\frac12=0$. Đạo hàm cấp hai là

$$
\phi'(\theta)=-\ln(1-\theta)-\ln\theta-2,\qquad \phi''(\theta)=\frac1{1-\theta}-\frac1\theta,
$$

âm trên $(0,1/2)$ vì $1-\theta>\theta$. Theo tính chất của hàm lõm chặt ở phần tiên quyết, $\phi>0$ trên $(0,1/2)$.

**Bước 4 (dấu trên $(1/2,1)$).** Thay $\theta$ bằng $1-\theta$ được $\phi(1-\theta)=-\phi(\theta)$. Vậy $\phi<0$ trên $(1/2,1)$.

**Bước 5 (kết luận).** $\theta>1/2$ khi và chỉ khi $z<\ln2$, tức $k<k^*=\ln2/\rho=(n/m)\ln2$. Theo Bước 3 và 4, $\lambda'<0$ trên $(0,k^*)$ và $\lambda'>0$ trên $(k^*,\infty)$; theo tiêu chuẩn cực trị ở phần tiên quyết, $\lambda$, và do đó $p$, giảm chặt rồi tăng chặt, nhỏ nhất tại $k^*$. Tại $k^*$, $e^{-k^*\rho}=1/2$, nên $p(k^*)=(1/2)^{k^*}=2^{-k^*}$. Kiểm với $n/m=8$: $\theta=e^{-5/8}\approx0{,}535>1/2$ tại $k=5$ và $\theta=e^{-6/8}\approx0{,}472<1/2$ tại $k=6$, nên $\lambda'(5)<0<\lambda'(6)$, khớp $5<k^*<6$. $\square$
:::

**Ý nghĩa:** tại $k^*$, xác suất một bit bằng 0 là $e^{-k^*m/n}=1/2$, nên khoảng một nửa số bit bằng 1. Mỗi bit mà khóa ngoài $S$ đọc bằng 1 với xác suất khoảng $1/2$, và $k^*$ bit như vậy cho $p(k^*)=2^{-k^*}$.

::: corollary Hệ quả 08.29 (Số hàm băm nguyên)
**Giả thiết.** Như Định lý 08.28; $k$ phải là số nguyên dương.

**Kết luận.** Nếu $k^*\ge1$, số nguyên tốt nhất là $\lfloor k^*\rfloor$ hoặc $\lceil k^*\rceil$, chọn giá trị cho $p$ nhỏ hơn. Nếu $k^*<1$, số nguyên tốt nhất là $1$.

**Điều kiện áp dụng.** Như Định lý 08.28.

**Phạm vi.** Hệ quả không nói hai số nguyên kề cho $p$ gần nhau đến đâu; phải tính cả hai.
:::

::: proof
Theo Định lý 08.28, $p$ giảm trên $(0,k^*]$, nên mọi số nguyên $k\le\lfloor k^*\rfloor$ cho $p(k)\ge p(\lfloor k^*\rfloor)$; $p$ tăng trên $[k^*,\infty)$, nên mọi số nguyên $k\ge\lceil k^*\rceil$ cho $p(k)\ge p(\lceil k^*\rceil)$. Khi $k^*<1$, mọi số nguyên dương nằm trong $[k^*,\infty)$, nên $k=1$ tốt nhất. $\square$
:::

::: example Ví dụ 08.16 (Tám bit mỗi khóa)
**Dữ kiện.** Tình huống lọc thư: $n=8\cdot10^9$ bit, $m=10^9$ địa chỉ, $n/m=8$.

**Tính.** $k^*=8\ln2\approx5{,}545$. Theo Hệ quả 08.29, so hai số nguyên kề: $p(5)=(1-e^{-5/8})^5\approx0{,}021679$ và $p(6)=(1-e^{-6/8})^6\approx0{,}021577$. Chọn $k=6$.

**Diễn giải.** Với sáu hàm băm, khoảng $2{,}16\%$ địa chỉ ngoài $S$ lọt qua; giá trị liên tục nhỏ nhất là $2^{-5{,}545}\approx0{,}02142$, nên làm tròn $k$ chỉ tốn khoảng $0{,}0002$.

**Kiểm tra lại.** $p(6)\ge2^{-k^*}$, đúng với Định lý 08.28. Trang chiếu MMDS (Streams 2, tr.14) in $(1-e^{-1/6})^2=0{,}0235$, tức viết sai cả số mũ và lũy thừa; công thức đúng $(1-e^{-6/8})^6$ cho $0{,}0216$, như trang chiếu CS246 (2026, tr.32–33) đã sửa.
:::

![Đường cong xác suất dương giả p(k) theo số hàm băm k từ 1 đến 10, trục tung tuyến tính từ 0 đến 0,12, với tám bit mỗi khóa; đường giảm từ khoảng 0,1175 tại k bằng 1 đến nhỏ nhất tại k bằng 6 rồi tăng lại tới khoảng 0,034 tại k bằng 10; vạch đứng nét đứt tại k* xấp xỉ 5,545; k bằng 5 cho 0,02168 và k bằng 6 cho 0,02158.](img/lec-08/fpr-curve.svg)

Hình vẽ $p(k)$ với $n/m=8$. Phần bên trái vạch $k^*$ là vùng lực thứ nhất thắng, phần bên phải là vùng mảng quá đầy; hai điểm nguyên kề vạch ứng với hai giá trị so sánh ở Ví dụ 08.16.

### 4.7 Giới hạn, nhầm lẫn và cách làm trong thực hành

Thuật toán 08.23 và 08.24 cho chi phí xây $km$ phép băm và ghi bit, chi phí kiểm tra tối đa $k$ phép băm và đọc bit, và bộ nhớ $n$ bit. Bloom filter có ba giới hạn. Nó không liệt kê được các khóa của $S$, vì mảng chỉ ghi bit. Nó không xóa trực tiếp được một khóa, vì một bit có thể do nhiều khóa đặt, và Định lý 08.25 mất hiệu lực khi đặt bit về 0. Thêm khóa mà giữ nguyên $n$ làm $m$ tăng, nên $p(k)$ tăng.

::: remark Nhận xét 08.30 (Nhầm lẫn thường gặp)
- "Có thể thuộc" không có nghĩa "thuộc": khóa 29 của Ví dụ 08.12 nhận "có thể thuộc" mà không thuộc $S$.
- $p_{FP}$ là xác suất cho một khóa $y\notin S$ cố định, không phải tỷ lệ thư rác trong các thư lọt qua; tỷ lệ đó còn phụ thuộc số thư từ địa chỉ thuộc $S$ và ngoài $S$.
- Tăng $k$ không luôn tốt: với $n/m=8$, $p(10)\approx0{,}034$ lớn hơn $p(6)\approx0{,}022$.
- $q$ chính xác dưới mô hình phi tiêu, còn $q^k$ chỉ là cận dưới của $p_{FP}$ (Mệnh đề 08.27).
:::

::: remark Nhận xét 08.31 (Trong thực hành)
Mô hình phi tiêu giả định các hàm băm đều và độc lập; hàm băm thật chỉ xấp xỉ điều đó, nên $p(k)$ là con số định cỡ, không phải bảo đảm. Bảo đảm không âm giả của Định lý 08.25 thì không phụ thuộc mô hình xác suất, chỉ cần bốn điều kiện về trạng thái. Kích thước $m$ phải ước lượng trước khi xây: Ví dụ 08.16 định cỡ $n$ và $k$ cho $10^9$ địa chỉ, và Bài tập 08.5 cho thấy hậu quả khi số địa chỉ tăng gấp đôi. Khi cần gỡ địa chỉ khỏi danh sách cho phép, cách đúng với Bloom filter chuẩn là xây lại mảng.
:::

::: exercise Bài tập 08.5 (Danh sách cho phép tăng gấp đôi)
Số địa chỉ được phép tăng lên $m=2\cdot10^9$, mảng giữ $n=8\cdot10^9$ bit và $k=6$. Tính $p(6)$. Số hàm băm nguyên nào tốt hơn?
:::

::: hint
Tính $n/m$, rồi $k^*$, rồi so $p$ tại hai số nguyên kề $k^*$ theo Hệ quả 08.29.
:::

::: solution
$n/m=4$, nên $p(6)=(1-e^{-6/4})^6\approx0{,}2198$, gấp khoảng mười lần $0{,}0216$ của Ví dụ 08.16. Theo Định lý 08.28, $k^*=4\ln2\approx2{,}77$; so $p(2)=(1-e^{-1/2})^2\approx0{,}1548$ và $p(3)=(1-e^{-3/4})^3\approx0{,}1469$, nên chọn $k=3$. Ngay cả với $k=3$, khoảng $14{,}7\%$ địa chỉ ngoài $S$ lọt qua; muốn giữ khoảng $2\%$ phải tăng $n$ lên khoảng $8$ bit mỗi khóa, tức $1{,}6\cdot10^{10}$ bit.
:::

Như vậy, chúng ta đã xây Bloom filter (Định nghĩa 08.22, Thuật toán 08.23–08.24), chứng minh nó không có âm giả dưới bốn điều kiện về trạng thái (Định lý 08.25), tính mật độ bit (Bổ đề 08.26) và xác suất dương giả cùng hai cận dưới (Mệnh đề 08.27), rồi chọn số hàm băm $k^*=(n/m)\ln2$ (Định lý 08.28, Hệ quả 08.29). Tuy nhiên, Bloom filter chỉ trả lời câu hỏi thành viên, còn hai cấu trúc lấy mẫu chỉ trả lời câu hỏi về phân phối, và mỗi cấu trúc cần giả thiết riêng. Trong Mục 5, chúng ta đặt ba cấu trúc cạnh nhau theo câu hỏi mà mỗi cấu trúc trả lời.

<!-- note-topic-id: lec-08-topic-13 -->
## 5. Chọn cấu trúc theo câu hỏi

Ba cấu trúc của chương trả lời ba loại câu hỏi khác nhau, mỗi cấu trúc dưới giả thiết riêng và với chi phí riêng. Khi một câu hỏi mới đến trên dòng, chúng ta cần đối chiếu nhanh: kết quả nào đã có, giả thiết nào không được bỏ, và cấu trúc nào tốn bao nhiêu. Không có khái niệm mới ở đây; chúng ta đặt các kết quả của Mục 1–4 cạnh nhau.

### 5.1 Kết quả, giả thiết và chi phí

Bảng đầu gom các kết quả chính cùng giả thiết mà thiếu nó kết quả sai.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Thuật toán dòng một lượt (Định nghĩa 08.1) | bộ nhớ làm việc nhỏ hơn lịch sử; không đọc lại kho lưu trữ | trạng thái chọn theo truy vấn |
| Sai lệch của mẫu từng bộ (Mệnh đề 08.6) | mỗi bộ giữ độc lập với xác suất $1/10$; $d>0$ | $d/(10u+19d)\ne d/(u+d)$ |
| Mẫu nhất quán theo khóa (Mệnh đề 08.10) | $h$ cố định; $h(K)$ đều theo cách chọn $h$; khóa nhận diện đúng đơn vị | giữ khi $h(K(t))<a$; xác suất $a/b$ mỗi khóa |
| Cỡ mẫu kỳ vọng (Hệ quả 08.12) | như Mệnh đề 08.10(b) | $ar/b$ bộ |
| Bất biến theo ngưỡng (Mệnh đề 08.14) | $h$ cố định; dọn đúng giá trị băm lớn nhất | mẫu là các bộ có $h\le\tau$ |
| Xác suất có mặt (Định lý 08.17) | $j$ đều trên $\{1,\ldots,r\}$, độc lập với các lần rút trước; $r\ge s$ | $\Pr[x_i\in W]=s/r$ |
| Không âm giả (Định lý 08.25) | không xóa bit; cùng hàm băm và cùng mảng; hàm tất định; ghi xong trước truy vấn | $y\in S$ cho "có thể thuộc" |
| Xác suất dương giả (Mệnh đề 08.27) | băm đều, độc lập; $y\notin S$ cố định | $p(k)\le q^k\le p_{FP}=\mathbb E[(X/n)^k]$ |
| Số hàm băm tối ưu (Định lý 08.28) | dạng mũ $p(k)$, $k$ thực | $k^*=(n/m)\ln2$, $p(k^*)=2^{-k^*}$ |

Bảng thứ hai đặt các thuật toán cạnh nhau theo cùng mô hình chi phí của Định nghĩa 08.3.

| Thuật toán | Đầu vào | Bảo đảm | Chi phí |
|---|---|---|---|
| Lấy mẫu theo khóa (Thuật toán 08.9) | bộ $t$; $a$, $b$, $h$ | cùng khóa cùng quyết định; $a/b$ mỗi khóa | 1 phép băm, 1 phép so sánh mỗi bộ; mẫu kỳ vọng $ar/b$ bộ |
| Ngưỡng giảm dần (Thuật toán 08.13) | như trên; ngân sách $G$ | mẫu theo khóa với $a=\tau+1$, tối đa $G$ bộ | thêm $O(\log G)$ mỗi lần chèn hoặc dọn; tổng phép xóa $\le r$ |
| Lấy mẫu hồ chứa (Thuật toán 08.16) | dòng; $s$ | $\min(r,s)$ phần tử; $s/r$ mỗi phần tử | $O(1)$ phép mỗi phần tử; $\Theta(s)$ từ máy |
| Xây Bloom filter (Thuật toán 08.23) | $S$; $n$; $h_1,\ldots,h_k$ | mọi bit của khóa thuộc $S$ bằng 1 | $km$ phép băm và ghi bit; $n$ bit |
| Kiểm tra thành viên (Thuật toán 08.24) | $y$; mảng $B$ | không âm giả; dương giả với xác suất $p_{FP}$ | tối đa $k$ phép băm và đọc bit |

Hai bảng cho một quy trình chọn cấu trúc gồm ba bước.

1. Xác định đầu ra. Thống kê theo nhóm, như tỷ lệ truy vấn lặp của từng người, cần mẫu theo khóa với khóa là đơn vị của nhóm. Mẫu đại diện có cỡ cố định cần hồ chứa. Câu hỏi "khóa này có thuộc tập cho trước không" cần Bloom filter cùng phép tra chính xác cho các khóa qua bộ lọc.
2. Kiểm giả thiết của kết quả sẽ dùng, theo cột giữa của bảng đầu.
3. Đếm chi phí với số liệu của bài toán, theo bảng thứ hai, và kiểm bộ nhớ có nhỏ hơn lịch sử không.

Khi đầu ra không thuộc ba loại trên, chẳng hạn số người dùng phân biệt trong tháng, các cấu trúc của chương chưa trả lời được.

### 5.2 Trả lời vấn đề trung tâm

Đầu chương có hai bài toán: máy tìm kiếm chỉ lưu được $1/10$ dòng truy vấn, và bộ lọc thư phải xét danh sách $10^9$ địa chỉ được phép với 1 GB bộ nhớ. Câu trả lời của chương đều có điều kiện.

- Với $h$ đều theo từng khóa và cố định, băm người dùng giữ trọn mỗi người với xác suất $1/10$ (Mệnh đề 08.10), nên tỷ lệ lặp của người được giữ tính đúng; lấy $1/10$ từng bộ thì cho $1/29$ thay vì $1/2$ khi $u=d=1$ (Mệnh đề 08.6).
- Với $j$ đều và độc lập với các lần rút trước, hồ chứa giữ đúng $s$ bộ, mỗi bộ có mặt với xác suất $s/r$ khi $r\ge s$ (Định lý 08.17), nhưng không giữ trọn người dùng.
- Khi bốn điều kiện về trạng thái của Định lý 08.25 được giữ, Bloom filter $8\cdot10^9$ bit, $k=6$ không loại địa chỉ hợp lệ nào, không cần giả thiết xác suất. Với các hàm băm đều, độc lập, nó nhận nhầm khoảng $p(6)\approx0{,}0216$ địa chỉ ngoài danh sách (Ví dụ 08.16).

::: example Ví dụ 08.17 (Chọn cấu trúc cho bốn yêu cầu)
**Dữ kiện.** Trên dòng truy vấn tìm kiếm và dòng thư, có bốn yêu cầu: (a) tỷ lệ truy vấn lặp của từng người dùng khi chỉ lưu $10\%$ dòng; (b) một mẫu đúng $1\,000$ bộ cho bảng theo dõi; (c) chặn thư từ địa chỉ ngoài danh sách cho phép; (d) số người dùng phân biệt trong tháng. Bốn yêu cầu do học phần đặt.

**Tính.**

| Yêu cầu | Cấu trúc | Tham số | Kết quả dùng |
|---|---|---|---|
| (a) | mẫu theo khóa người dùng | $a/b=1/10$ | Mệnh đề 08.10, Hệ quả 08.12 |
| (b) | hồ chứa | $s=1\,000$ | Định lý 08.17 |
| (c) | Bloom filter, rồi tra chính xác | $n/m=8$, $k=6$ | Định lý 08.25, Ví dụ 08.16 |
| (d) | chưa có trong chương | — | Bài 09 |

**Diễn giải.** Yêu cầu (a) không dùng được hồ chứa, vì hồ chứa tách các bộ của một người (Nhận xét 08.20). Yêu cầu (b) không dùng được mẫu theo khóa, vì cỡ mẫu theo khóa tăng theo dòng (Hệ quả 08.12).

**Kiểm tra lại.** Mỗi lựa chọn đi qua ba bước của quy trình: đầu ra, giả thiết, chi phí.
:::

Như vậy, ba cấu trúc của chương phủ ba loại đầu ra: thống kê theo nhóm, mẫu cỡ cố định và câu hỏi thành viên, mỗi loại kèm một bảo đảm có điều kiện. Tuy nhiên, đếm số phần tử phân biệt, ước lượng mômen và trả lời theo cửa sổ thời gian gần đây không thuộc ba loại này. Bài 09 xây các cấu trúc cho những câu hỏi đó, và dùng lại hai công cụ của chương: hàm băm tất định và lấy mẫu hồ chứa.

<!-- note-topic-id: lec-08-topic-14 -->
## Tình huống áp dụng và ứng dụng

Ba tình huống dưới đây giải trọn ba bài toán bằng công cụ của chương. Tình huống 08.1 và 08.2 thỏa giả thiết của các kết quả được dùng; Tình huống 08.3 vi phạm giả thiết của Định lý 08.25 và Ví dụ 08.16, và tính hậu quả bằng số. Các số người dùng, số truy vấn và số thư trong ba tình huống là giả định của học phần để có cỡ, không phải số liệu đo được.

::: application Tình huống 08.1 (Nghiên cứu truy vấn lặp với ngân sách cố định)
**Bài toán và dữ liệu.** Máy tìm kiếm muốn đo tỷ lệ truy vấn lặp của người dùng điển hình (MMDS §4.2.1). Giả định: $10^8$ người dùng, trung bình 30 truy vấn tìm kiếm mỗi người mỗi tháng, tức $r=3\cdot10^9$ bộ mỗi tháng; ngân sách mẫu $G=10^8$ bộ.

**Mô hình hóa.** Khóa là người dùng (Mục 2.3). Mẫu theo khóa với tỷ lệ $1/10$ (Thuật toán 08.9) có cỡ kỳ vọng $ar/b=3\cdot10^8$ bộ (Hệ quả 08.12), gấp ba ngân sách, nên dùng ngưỡng giảm dần (Thuật toán 08.13) với $b=2^{32}$ giá trị băm.

**Kiểm giả thiết.** Hàm băm được chọn một lần và dùng chung trên mọi máy, nên $h$ cố định (Mệnh đề 08.10(a)). Khóa người dùng nhận diện đúng đơn vị; nếu chỉ có địa chỉ IP, đơn vị là địa chỉ, như MMDS lưu ý (Nhận xét 08.11). Tính đều theo từng khóa là giả thiết về phép chọn hàm.

**Áp dụng.** Theo Mệnh đề 08.14, mẫu luôn là mẫu theo khóa với tỷ lệ $(\tau+1)/b$. Để cỡ kỳ vọng $3\cdot10^9\cdot(\tau+1)/b$ không vượt $10^8$, tỷ lệ phải xuống khoảng $1/30$, tức $\tau+1\approx2^{32}/30\approx1{,}43\cdot10^8$, ứng với khoảng $3{,}3\cdot10^6$ người dùng được giữ trọn.

**Chi phí.** Mỗi bộ tốn 1 phép băm và 1 phép so sánh, tức $3\cdot10^9$ phép băm mỗi tháng; mỗi lần chèn hoặc dọn tốn thêm $O(\log G)$ trên chỉ mục.

**Diễn giải.** Với mỗi người được giữ, tỷ lệ lặp tính trên mẫu đúng bằng tỷ lệ thật (Mệnh đề 08.10(a)). Mệnh đề 08.10(b) chỉ áp dụng gần đúng cho ngưỡng giảm dần: ngưỡng cuối $\tau$ phụ thuộc vào giá trị băm và số bộ của các khóa, và một người dùng nhiều bộ đẩy $\tau$ xuống nên dễ tự rơi ra hơn; trường hợp cực đoan là một khóa có hơn $G$ bộ, luôn bị bỏ trọn (Thuật toán 08.13, trường hợp biên). Khi mỗi người dùng có rất ít bộ so với $G$, ở đây khoảng 30 so với $10^8$, ngưỡng gần như không phụ thuộc vào một khóa riêng lẻ, và trung bình trên những người được giữ xấp xỉ trung bình trên mọi người dùng. Lấy $1/10$ từng bộ thay vào đó sẽ cho $1/29$ với người có $u=d=1$ (Mệnh đề 08.6).

**Giới hạn.** Tỷ lệ $1/30$ chỉ đúng theo kỳ vọng; một người dùng có rất nhiều truy vấn có thể đẩy ngưỡng xuống thấp hơn (Ví dụ 08.6). Ngưỡng giảm dần trong tháng, nên người dùng bị bỏ ở cuối tháng đã có bộ trong mẫu ở đầu tháng rồi bị xóa trọn.

**Dẫn ngược lý thuyết.** Mệnh đề 08.6, Thuật toán 08.9, Mệnh đề 08.10, Hệ quả 08.12, Thuật toán 08.13, Mệnh đề 08.14, Nhận xét 08.11.
:::

::: application Tình huống 08.2 (Lọc $10^9$ địa chỉ trong 1 GB)
**Bài toán và dữ liệu.** Danh sách cho phép có $m=10^9$ địa chỉ, mỗi địa chỉ từ 20 byte; bộ nhớ chính 1 GB (MMDS §4.3.1). Giả định: mỗi ngày có $10^6$ thư từ địa chỉ ngoài danh sách.

**Mô hình hóa.** Bloom filter $n=8\cdot10^9$ bit (Định nghĩa 08.22), xây một lần bằng Thuật toán 08.23; mỗi thư đi qua Thuật toán 08.24, và chỉ thư nhận "có thể thuộc" mới tra danh sách trên đĩa.

**Kiểm giả thiết.** Mảng chỉ được đọc sau khi xây, cùng $k$ hàm băm tất định, nên Định lý 08.25 cho không âm giả. Mô hình băm đều, độc lập là giả thiết của Mệnh đề 08.27.

**Áp dụng.** $n/m=8$, $k^*=8\ln2\approx5{,}545$; theo Hệ quả 08.29 chọn $k=6$, $p(6)\approx0{,}0216$ (Ví dụ 08.16). Trong $10^6$ thư từ địa chỉ ngoài danh sách, kỳ vọng khoảng $21\,600$ thư đi tiếp tới phép tra đĩa thay vì $10^6$.

**Chi phí.** Xây tốn $km=6\cdot10^9$ phép băm và ghi bit; mỗi thư tốn tối đa 6 phép băm và đọc bit; bộ nhớ 1 GB thay cho từ 20 GB.

**Diễn giải.** Mọi thư từ địa chỉ được phép đi tiếp; khoảng $2{,}16\%$ thư từ địa chỉ ngoài danh sách cũng đi tiếp và bị chặn ở bước tra chính xác.

**Giới hạn.** $p(6)$ là dạng mũ, một cận dưới của $p_{FP}$ dưới mô hình (Mệnh đề 08.27); với $n=8\cdot10^9$ các mức xấp xỉ trùng nhau tới nhiều chữ số, nhưng hàm băm thật chỉ xấp xỉ mô hình. Số $m$ phải biết trước khi xây.

**Dẫn ngược lý thuyết.** Định nghĩa 08.22, Thuật toán 08.23–08.24, Định lý 08.25, Mệnh đề 08.27, Định lý 08.28, Hệ quả 08.29.
:::

::: application Tình huống 08.3 (Gỡ địa chỉ bằng cách xóa bit và danh sách tăng gấp đôi)
**Bài toán và dữ liệu.** Bộ lọc của Tình huống 08.2 ($n=8\cdot10^9$, $m=10^9$, $k=6$) đã chạy. Có hai thay đổi giả định: (a) cần gỡ $1\,000$ địa chỉ khỏi danh sách; (b) danh sách tăng lên $2\cdot10^9$ địa chỉ mà mảng giữ nguyên.

**Kiểm giả thiết.** Cách gỡ "đặt về 0 sáu bit của địa chỉ bị gỡ" vi phạm điều kiện 1 của Định lý 08.25. Danh sách tăng gấp đôi làm $n/m$ đổi từ 8 xuống 4, nên lựa chọn $k=6$ của Ví dụ 08.16 không còn là lựa chọn của Hệ quả 08.29.

**Áp dụng (a).** Mỗi bit bị đặt về 0 có thể là bit của địa chỉ khác. Dưới mô hình phi tiêu, mỗi bit nhận trung bình $(m-1)k/n\approx0{,}75$ phi tiêu từ các địa chỉ còn lại, nên sáu bit của một địa chỉ bị gỡ chứa trung bình khoảng $4{,}5$ phi tiêu của địa chỉ khác. Mỗi phi tiêu như vậy biến địa chỉ của nó thành một âm giả, và một địa chỉ có thể mất nhiều bit. Gỡ $1\,000$ địa chỉ vì thế làm kỳ vọng số địa chỉ hợp lệ bị chặn lên tới khoảng $4\,500$; phản ví dụ sau Định lý 08.25 cho một trường hợp nhỏ, khi gỡ 585 làm 159 bị loại.

**Áp dụng (b).** Theo Bài tập 08.5, $n/m=4$ cho $p(6)\approx0{,}2198$, nên khoảng $219\,800$ trong $10^6$ thư ngoài danh sách đi tới phép tra đĩa; số hàm băm tốt nhất đổi thành 3.

**Diễn giải.** Lỗi (a) phá bảo đảm tuyệt đối của bộ lọc: thư hợp lệ bị chặn. Lỗi (b) không phá bảo đảm đó nhưng làm bước lọc mất phần lớn tác dụng.

**Giới hạn và cách sửa.** Bloom filter chuẩn không hỗ trợ xóa; cách đúng là xây lại mảng từ danh sách mới, với $n$ định cỡ theo $m$ mới.

**Dẫn ngược lý thuyết.** Định lý 08.25 (điều kiện 1), Bổ đề 08.26, Định lý 08.28, Hệ quả 08.29, Bài tập 08.5.
:::

**Ứng dụng trong bài sau.**

- Ghi chú Bài 09, Mục 2 (Flajolet–Martin) dùng tính tất định của hàm băm, như mẫu theo khóa: cùng khóa luôn cho cùng giá trị băm, nên số phần tử phân biệt được ước lượng mà không lưu danh sách khóa.
- Ghi chú Bài 09, Mục 5 (biến AMS) chọn vị trí bắt đầu bằng lấy mẫu hồ chứa cỡ 1, nên mỗi vị trí được chọn với xác suất $1/r$, trường hợp $s=1$ của Định lý 08.17.

<!-- note-topic-id: lec-08-topic-15 -->
## Tóm tắt chương

Xuất phát điểm là hai bài toán của ghi chú Bài 01 trên một dòng không biết trước độ dài: đo tỷ lệ truy vấn lặp khi chỉ lưu được $1/10$ dòng, và lọc thư theo $10^9$ địa chỉ với 1 GB bộ nhớ. Chúng ta đặc tả thuật toán dòng một lượt, trả lời từ trạng thái chọn theo truy vấn và đo bằng bốn đại lượng chi phí mỗi phần tử (Định nghĩa 08.1, 08.3). Lấy mẫu từng bộ làm sai tỷ lệ lặp (Mệnh đề 08.6), nên chúng ta giữ trọn từng khóa bằng một hàm băm cố định (Thuật toán 08.9). Mỗi khóa được giữ với xác suất $a/b$ (Mệnh đề 08.10), cỡ mẫu kỳ vọng là $ar/b$ (Hệ quả 08.12), và ngưỡng giảm dần giữ được ngân sách cố định (Mệnh đề 08.14). Cỡ mẫu theo khóa không cố định, nên hồ chứa giữ đúng $s$ phần tử, mỗi phần tử có mặt với xác suất $s/r$ (Định lý 08.17), và mọi tập con cỡ $s$ đồng khả năng (Mệnh đề 08.18). Câu hỏi thành viên cần Bloom filter: không có âm giả dưới bốn điều kiện về trạng thái (Định lý 08.25), xác suất dương giả có các cận dưới $p(k)\le q^k$ (Mệnh đề 08.27), nhỏ nhất theo dạng mũ tại $k^*=(n/m)\ln2$ (Định lý 08.28). Với tám bit mỗi khóa và sáu hàm băm, khoảng $2{,}16\%$ địa chỉ ngoài danh sách lọt qua. Đếm phần tử phân biệt, mômen và cửa sổ thời gian vẫn chưa có cấu trúc và được xét ở Bài 09.

**Định nghĩa và kết quả theo mục.**

- Mục 1: thuật toán dòng một lượt (Định nghĩa 08.1); giá trị lớn nhất trên dòng (Thuật toán 08.2); chi phí của thuật toán dòng (Định nghĩa 08.3); nhầm lẫn và thực hành (Nhận xét 08.4, 08.5).
- Mục 2: sai lệch của mẫu từng bộ (Mệnh đề 08.6, Nhận xét 08.7); mẫu theo khóa (Định nghĩa 08.8, Thuật toán 08.9); nhất quán và xác suất $a/b$ (Mệnh đề 08.10, Nhận xét 08.11); cỡ mẫu kỳ vọng (Hệ quả 08.12); ngưỡng giảm dần (Thuật toán 08.13, Mệnh đề 08.14).
- Mục 3: mẫu hồ chứa (Định nghĩa 08.15, Thuật toán 08.16); xác suất có mặt (Định lý 08.17); mọi tập con đồng khả năng (Mệnh đề 08.18); chi phí (Mệnh đề 08.19); nhầm lẫn và thực hành (Nhận xét 08.20, 08.21).
- Mục 4: Bloom filter, dương giả, âm giả (Định nghĩa 08.22); xây và kiểm tra (Thuật toán 08.23, 08.24); không âm giả (Định lý 08.25); mật độ bit (Bổ đề 08.26); xác suất dương giả (Mệnh đề 08.27); số hàm băm tối ưu (Định lý 08.28, Hệ quả 08.29); nhầm lẫn và thực hành (Nhận xét 08.30, 08.31).
- Mục 5: hai bảng đối chiếu và quy trình chọn cấu trúc theo đầu ra.

**Công thức và thuật toán cần nhớ.** Sai lệch của mẫu từng bộ, cỡ mẫu kỳ vọng theo khóa và xác suất có mặt trong hồ chứa:

$$
\frac{d}{10u+19d}\ne\frac{d}{u+d},\qquad \frac{ar}{b},\qquad \Pr[x_i\in W]=\frac sr\quad(r\ge s).
$$

Mật độ bit, xác suất dương giả và số hàm băm tối ưu:

$$
q=1-\Bigl(1-\frac1n\Bigr)^{km},\qquad p(k)=\bigl(1-e^{-km/n}\bigr)^k\le q^k\le p_{FP},\qquad k^*=\frac nm\ln2,\quad p(k^*)=2^{-k^*}.
$$

Ba thuật toán: giữ $t$ khi $h(K(t))<a$; với $r>s$, rút $j$ đều trong $\{1,\ldots,r\}$ và thay ô $j$ khi $j\le s$; đặt $B[h_i(v)]\gets1$ khi xây, trả "chắc chắn không thuộc" khi gặp một bit 0 lúc kiểm tra.

**Giả thiết hay bị bỏ quên.**

- Mẫu theo khóa cần $h$ cố định suốt dòng; xác suất $a/b$ lấy theo cách chọn $h$, không theo các lần xuất hiện của khóa; Mệnh đề 08.10 không nói số khóa được chọn gần đúng $a/b$ số khóa (Mục 2.2).
- Khóa phải nhận diện đúng đơn vị của thống kê; khóa (người dùng, thời gian) quay lại mẫu từng bộ (Bài tập 08.2).
- Cỡ mẫu $ar/b$ là kỳ vọng; một khóa nhiều bộ làm cỡ thực lệch xa (Ví dụ 08.6).
- Hồ chứa cần $j$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước; $s/r$ chỉ đúng khi $r\ge s$ và là xác suất của từng phần tử.
- Bloom filter cần mảng chỉ được đọc sau khi xây, cùng hàm băm, và $m$ biết trước; $p(k)$ và $q^k$ là cận dưới của $p_{FP}$ dưới mô hình băm đều, độc lập.

<!-- note-topic-id: lec-08-topic-16 -->
## Bài tập củng cố

Các bài tập trong các mục và chín bài dưới đây là bộ bài tập của chương. Mục tiêu 1 được kiểm bởi Bài tập 08.1, 08.2, 08.3, 08.6 và 08.13; mục tiêu 2 bởi Bài tập 08.4, 08.7 và 08.14; mục tiêu 3 bởi Bài tập 08.5, 08.8–08.12. Bốn bài mang số bài sách (Bài tập 08.10–08.13) là bài của phần bài tập vận dụng trên lớp. Sách không in lời giải; lời giải dưới đây suy ra từ đề và từ các kết quả đã chứng minh trong chương.

### Mức nhận biết

::: exercise Bài tập 08.6 (Ngưỡng 5% và mẫu từng bộ)
Hàm $h$ nhận giá trị trong $\{0,\ldots,99\}$. Muốn giữ $5\%$ người dùng của dòng truy vấn tìm kiếm, điều kiện giữ bộ $t$ là gì? Vì sao không lấy $5\%$ từng bộ? Nêu kết quả đã dùng.
:::

::: hint
Đếm số giá trị được nhận; với mẫu từng bộ, dùng công thức tỷ lệ giữ $\eta$ ở Nhận xét 08.7.
:::

::: solution
Giữ $t$ khi $h(K(t))<5$, với $K(t)$ là người dùng: đúng 5 trong 100 giá trị, nên mỗi người được giữ với xác suất $5/100$ khi $h$ đều theo từng khóa (Mệnh đề 08.10(b)), và mọi bộ của một người nhận cùng quyết định (Mệnh đề 08.10(a)). Lấy từng bộ với xác suất $\eta=0{,}05$ cho tỷ số $\frac{d\eta}{u+(2-\eta)d}=\frac{0{,}05d}{u+1{,}95d}=\frac{d}{20u+39d}$ thay vì $\frac{d}{u+d}$ (Nhận xét 08.7, Mệnh đề 08.6). Với $u=d=1$, đó là $1/59$ thay vì $1/2$.
:::

::: exercise Bài tập 08.7 (Xác suất có mặt trong hồ chứa)
Hồ chứa có $s=50$ ô, dòng đã có $r=1\,000$ bộ. Bộ thứ 7 còn trong hồ với xác suất bao nhiêu? Cần giả thiết gì?
:::

::: hint
Kiểm $r\ge s$ rồi dùng Định lý 08.17.
:::

::: solution
Vì $r=1\,000\ge s=50$, Định lý 08.17 cho $\Pr[x_7\in W]=s/r=50/1\,000=0{,}05$. Cần mỗi số $j$ đều trên $\{1,\ldots,r\}$ và độc lập với các lần rút trước. Vị trí 7 không có vai trò riêng: mọi bộ đã đọc có cùng xác suất.
:::

::: exercise Bài tập 08.8 (Âm giả sau khi thêm khóa)
Bloom filter có thể trả "chắc chắn không thuộc" cho một khóa đã được thêm vào $S$ không? Nêu giả thiết của câu trả lời.
:::

::: hint
Xem bốn điều kiện của Định lý 08.25 và điều gì xảy ra khi bỏ điều kiện 1.
:::

::: solution
Không, khi bốn điều kiện của Định lý 08.25 được giữ: không bit nào bị xóa, truy vấn dùng đúng hàm băm và mảng đã xây, hàm băm tất định, mọi phép ghi đã xong. Nếu gỡ một khóa bằng cách đặt bit về 0, khóa khác dùng chung bit có thể bị loại: trong mảng 11 bit của Ví dụ 08.11, gỡ 585 làm 159 nhận "chắc chắn không thuộc".
:::

::: exercise Bài tập 08.9 (Gấp đôi số bit)
Giữ $m$, gấp đôi $n$. Số hàm băm tối ưu $k^*$ và giá trị $p(k^*)$ thay đổi thế nào? Tính cho $n/m$ từ 8 lên 16.
:::

::: hint
Dùng $k^*=(n/m)\ln2$ và $p(k^*)=2^{-k^*}$ của Định lý 08.28.
:::

::: solution
$k^*=(n/m)\ln2$ gấp đôi, và $p(k^*)=2^{-k^*}$ nên giá trị mới là bình phương giá trị cũ (Định lý 08.28). Với $n/m=8$: $k^*\approx5{,}545$, $p(k^*)\approx0{,}0214$. Với $n/m=16$: $k^*\approx11{,}09$, $p(k^*)\approx0{,}0214^2\approx4{,}6\cdot10^{-4}$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 08.10 (Ba và bốn hàm băm; Bài 4.3.1, MMDS §4.3.4, tr.141)
Với tình huống lọc thư, $n=8\cdot10^9$ bit và tập $S$ gồm $m=10^9$ khóa, tính xác suất dương giả khi dùng ba hàm băm, và khi dùng bốn hàm băm.
:::

::: hint
Dùng dạng mũ $p(k)=(1-e^{-km/n})^k$ với $km/n=k/8$.
:::

::: solution
$p(3)=(1-e^{-3/8})^3\approx0{,}030579$ và $p(4)=(1-e^{-1/2})^4\approx0{,}023969$. Bốn hàm băm tốt hơn ba vì $4<k^*\approx5{,}545$, trên đoạn $p$ còn giảm (Định lý 08.28). Theo Mệnh đề 08.27, đây là dạng mũ, một cận dưới của $p_{FP}$ dưới mô hình băm đều, độc lập; với $n=8\cdot10^9$, các mức xấp xỉ trùng nhau tới nhiều chữ số.

**Kiểm tra lại.** Hai số nằm giữa $p(2)\approx0{,}0489$ và $p(6)\approx0{,}0216$ của Ví dụ 08.14 và 08.16, đúng chiều giảm của $p$ trên $(0,k^*]$.
:::

::: exercise Bài tập 08.11 (Chia mảng bit; Bài 4.3.2, MMDS §4.3.4, tr.141)
Có $n$ bit bộ nhớ và tập $S$ gồm $m$ khóa. Thay vì $k$ hàm băm vào một mảng, chia $n$ bit thành $k$ mảng và băm một lần vào mỗi mảng. Theo $n$, $m$, $k$, xác suất dương giả là bao nhiêu? So với $k$ hàm băm vào một mảng chung. Quy ước của học phần, sách không nêu: $k$ chia hết $n$; các hàm băm đều và độc lập.
:::

::: hint
Một mảng con có $n/k$ bit và nhận $m$ phi tiêu. Để so sánh, dùng bất đẳng thức Bernoulli ở phần tiên quyết.
:::

::: solution
**Mảng chia.** Một bit cố định của một mảng con bằng 0 khi không khóa nào của $S$ băm vào nó; mỗi khóa trượt bit đó với xác suất $1-k/n$, nên xác suất là $(1-k/n)^m$. Một khóa $y\notin S$ đọc đúng một vị trí đều trong mỗi mảng con. Các mảng con dùng các hàm băm độc lập, nên các tỷ lệ bit 1 của chúng độc lập, và

$$
p_{\text{chia}}=\bigl[1-(1-k/n)^m\bigr]^k,
$$

đúng chính xác dưới mô hình này.

**Mảng chung.** Theo Mệnh đề 08.27, $p_{FP}=\mathbb E[(X/n)^k]\ge q^k=[1-(1-1/n)^{km}]^k$.

**So sánh.** Theo bất đẳng thức Bernoulli, $(1-1/n)^k\ge1-k/n$, nên $(1-1/n)^{km}\ge(1-k/n)^m$. Mảng chia có ít bit 0 hơn theo kỳ vọng, nên $p_{\text{chia}}\ge q^k$. Khi $n$ lớn, cả hai về $(1-e^{-km/n})^k$.

**Ví dụ số.** Với $n=64$, $m=8$, $k=4$: $p_{\text{chia}}\approx0{,}026450$; $q^k\approx0{,}024556$; giá trị chính xác của mảng chung $\mathbb E[(X/64)^4]\approx0{,}025354$, tính từ phân phối số bit 1 sau 32 phi tiêu. Với $n=8\cdot10^9$, $m=10^9$, $k=4$, hai công thức trùng tới chín chữ số có nghĩa, $0{,}023968650\ldots$

**Kiểm tra lại.** Chiều $p_{\text{chia}}\ge q^k$ được chứng minh; trong ví dụ, mảng chia còn lớn hơn giá trị chính xác của mảng chung, nhưng chương không chứng minh chiều này cho mọi $n$, $m$, $k$.
:::

::: exercise Bài tập 08.12 (Số hàm băm tối ưu; Bài 4.3.3, MMDS §4.3.4, tr.142)
Theo $n$ là số bit và $m$ là số khóa của $S$, số hàm băm nào làm nhỏ nhất xác suất dương giả? Dùng dạng mũ $p(k)=(1-e^{-km/n})^k$ với $k$ thực, rồi chọn $k$ nguyên.
:::

::: hint
Đặt $\rho=m/n$, $z=k\rho$, $\theta=e^{-z}$ và xét $\lambda(k)=\ln p(k)$. Tìm điểm làm đạo hàm bằng 0, rồi xét dấu đạo hàm ở hai phía.
:::

::: solution
Đây là Định lý 08.28 và Hệ quả 08.29. Với các biến của gợi ý, và $z=-\ln\theta$, $\lambda'(k)=\phi(\theta)/(1-\theta)$ với $\phi(\theta)=(1-\theta)\ln(1-\theta)-\theta\ln\theta$. Hàm $\phi$ dương trên $(0,1/2)$, nhờ tính lõm chặt và $\phi(0^+)=\phi(1/2)=0$, và âm trên $(1/2,1)$, nhờ $\phi(1-\theta)=-\phi(\theta)$. Vì $\theta>1/2$ khi và chỉ khi $k<(n/m)\ln2$, $p$ giảm rồi tăng và nhỏ nhất tại $k^*=(n/m)\ln2$, với $p(k^*)=2^{-k^*}$. Với $k$ nguyên, so $p$ tại $\lfloor k^*\rfloor$ và $\lceil k^*\rceil$, và lấy $k=1$ nếu $k^*<1$. Các bước đầy đủ nằm trong chứng minh Định lý 08.28.

**Kiểm tra lại.** Với $n/m=8$: $k^*\approx5{,}545$; $p(5)\approx0{,}021679>p(6)\approx0{,}021577$, nên chọn $k=6$.
:::

### Mức vận dụng

::: exercise Bài tập 08.13 (Chọn khóa lấy mẫu; Bài 4.2.1, MMDS §4.2.5, tr.138)
Dòng có lược đồ `Grades(university, courseID, studentID, grade)`. Mã trường là duy nhất; mã học phần và mã sinh viên chỉ duy nhất trong một trường. Với một mẫu $1/20$ của dữ liệu, chọn thuộc tính khóa để ước lượng:

(a) với mỗi trường, số sinh viên trung bình của một học phần;

(b) tỷ lệ sinh viên có điểm trung bình từ 3,5;

(c) tỷ lệ học phần có ít nhất nửa số sinh viên đạt "A".
:::

::: hint
Với mỗi câu, hỏi thống kê gộp các bộ theo đơn vị nào, rồi chọn thuộc tính nhận diện duy nhất đơn vị đó (quy trình ở Mục 2.3).
:::

::: solution
(a) Khóa `(university, courseID)`. Mọi bộ của một học phần cùng vào mẫu hoặc cùng bị bỏ (Mệnh đề 08.10(a)), nên số sinh viên của học phần được giữ đếm đúng, và mỗi trường còn, theo kỳ vọng, khoảng $1/20$ số học phần; trường có rất ít học phần có thể không còn học phần nào, và ước lượng cho trường đó không xác định. Khóa chỉ gồm `university` sẽ bỏ hẳn khoảng $19/20$ số trường, trong khi câu hỏi cần mọi trường.

(b) Khóa `(university, studentID)`: điểm trung bình của một sinh viên cần mọi bộ của sinh viên đó.

(c) Khóa `(university, courseID)`: tỷ lệ đạt "A" của một học phần cần mọi bộ của học phần.

Cả ba khóa phải có `university`, vì mã học phần và mã sinh viên chỉ duy nhất trong một trường; thiếu nó, hai học phần cùng mã ở hai trường bị gộp thành một đơn vị (bước 3 của quy trình ở Mục 2.3).
:::

::: exercise Bài tập 08.14 (Hồ chứa cho từng khóa)
MMDS (hộp "A General Stream-Sampling Problem", tr.150) đề xuất kết hợp hai cấu trúc: lấy mẫu theo khóa với tỷ lệ $a/b$, và với mỗi khóa được chọn, giữ các bộ của khóa đó trong một hồ chứa $s$ ô. Xét một khóa $K$ được chọn, đã có $r_K\ge s$ bộ.

(a) Một bộ cố định của $K$ nằm trong mẫu với xác suất bao nhiêu, theo các lần rút của hồ chứa của $K$?

(b) Mẫu có tối đa bao nhiêu bộ, nếu có $N_K$ khóa được chọn?

(c) Tỷ lệ truy vấn lặp của một người dùng $K$ có còn tính đúng trên mẫu không?
:::

::: hint
Áp Định lý 08.17 cho dòng con gồm các bộ của $K$; với (c), xem Nhận xét 08.20.
:::

::: solution
(a) Các bộ của $K$ tạo một dòng con, và hồ chứa của $K$ chạy Thuật toán 08.16 trên dòng con đó. Theo Định lý 08.17, với các số rút đều và độc lập với các lần rút trước, mỗi bộ của $K$ có mặt với xác suất $s/r_K$.

(b) Mỗi khóa được chọn giữ tối đa $s$ bộ, nên mẫu có tối đa $sN_K$ bộ, cộng một bộ đếm $r_K$ cho mỗi khóa. Một khóa nhiều bộ, như khóa $10^6$ bộ của Ví dụ 08.6, chỉ chiếm $s$ ô.

(c) Chỉ khi $r_K\le s$. Khi $r_K>s$, hồ chứa của $K$ chọn vị trí riêng lẻ, nên hai bộ của cùng một truy vấn có thể bị tách, và tỷ lệ lặp tính trên mẫu bị lệch xuống (Nhận xét 08.20). Cách kết hợp này đổi tính đúng của thống kê theo người dùng nặng lấy giới hạn bộ nhớ.
:::

<!-- note-topic-id: lec-08-topic-17 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- Leskovec, J., Rajaraman, A. và Ullman, J. D. (2020). *Mining of Massive Datasets*, ấn bản 3, Cambridge University Press, Chương 4. §4.1, tr.131–135: Mục 1 (Hình 4.1, Ví dụ 4.1). §4.2, tr.136–138: Mục 2 và Bài tập 08.13. §4.3, tr.139–142: Mục 4 (Ví dụ 4.3–4.4) và Bài tập 08.10–08.12. §4.5.5, tr.148–149, và hộp "A General Stream-Sampling Problem", tr.150: Mục 3 và Bài tập 08.14. §1.3.5, tr.13–14: giới hạn $(1-1/c)^c\to e^{-1}$ ở phần tiên quyết. Sách và bộ trang chiếu của các tác giả tại [http://www.mmds.org](http://www.mmds.org); phần lớn sườn, ví dụ và bài tập của chương dựa trên nguồn này.
- Trang chiếu MMDS chương 4, *Mining Data Streams* phần 1 và 2 (tại [http://www.mmds.org](http://www.mmds.org)). Phần 1, tr.6–21: mô hình dòng, lấy mẫu theo khóa (tr.12–16, ví dụ 30%), hồ chứa (tr.18–21, dòng a, x, c, y, z, k, c, d, e, g). Phần 2, tr.4–14: Bloom filter; tr.14 in $(1-e^{-1/6})^2=0{,}0235$, khác công thức đúng (Ví dụ 08.16).
- Leskovec, J. (2026). Stanford CS246, *Mining Data Streams* (26/02/2026), tr.13–14: phép đếm sai lệch của Mục 2.1; tr.32–33: đường cong $p(k)$ của Ví dụ 08.16. Hình trong ghi chú được vẽ lại.
- Ullman, J. D. (2017). Stanford CS246, *Streams 2*, tr.5–8: ví dụ Bloom filter 11 bit với các khóa 25, 159, 585 và truy vấn 118 (Ví dụ 08.11–08.12).
- Welford, B. P. (1962). Note on a method for calculating corrected sums of squares and products, *Technometrics* 4(3), 419–420. Phép cập nhật trung bình và tổng bình phương độ lệch trong đoạn "Trong thực hành" sau Bài tập 08.1; bổ sung ngoài nguồn chính.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press, §2.1. Cách phát biểu bất biến vòng lặp với ba phần khởi tạo, duy trì, kết thúc, dùng cho Thuật toán 08.2 và Mệnh đề 08.14.
- Đọc tiếp: ghi chú Bài 09, *Dòng dữ liệu: đếm, mômen và cửa sổ*, Mục 2 (Flajolet–Martin) và Mục 5 (biến AMS, dùng hồ chứa cỡ 1), ứng với MMDS §4.4–4.7. Blum, A., Hopcroft, J. và Kannan, R., *Foundations of Data Science*, bản ngày 04/01/2018, §6.1, tr.181, trình bày lấy mẫu một chỉ số với xác suất tỷ lệ trọng số bằng cùng kiểu quy nạp như Định lý 08.17; nội dung này không cần cho bài tập.
- Ghi chú Bài 01 (mục "Xử lý dòng dữ liệu, lưu trữ và truy vấn"; mục "Mô hình ngẫu nhiên và giới hạn suy luận"), ghi chú Bài 05 (Mục 7, 9, 10) và ghi chú Bài 06 (Định lý 06.7, Mệnh đề 06.5, Tình huống 06.2): các kết quả nhắc lại ở phần kiến thức tiên quyết.
