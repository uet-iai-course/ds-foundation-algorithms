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
   - Tính mật độ bit 1, xác suất nhận nhầm và dạng mũ $(1-e^{-km/n})^k$; dẫn xuất $k^*=(n/m)\ln2$ và chọn số hàm băm nguyên (Mục 4, các bài tập 4.3.1–4.3.3 của MMDS).

Ở Mục 5 và các tình huống áp dụng, ba mục tiêu được dùng cùng lúc để chọn cấu trúc theo câu hỏi cần trả lời.

<!-- note-topic-id: lec-08-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `06.k` chỉ ghi chú Bài 06. Ghi chú Bài 01 và Bài 05 chưa đánh số hiệu, nên các kết quả của hai bài đó được dẫn theo mục. Mỗi kết quả được phát biểu lại dưới đây; các chữ $c$, $c_0$, $z$, $Z$, $g$, $\alpha$, $\beta$ trong phần này là biến tạm, không mang nghĩa của bảng ký hiệu.

- **Hai bài toán dòng của Bài 01** (ghi chú Bài 01, mục "Xử lý dòng dữ liệu, lưu trữ và truy vấn"). Bài toán thứ nhất cần một mẫu của nhật ký (người dùng, truy vấn, thời điểm) vẫn đo được mức lặp truy vấn của từng người, nên đơn vị lấy mẫu là người dùng. Bài toán thứ hai nhận thư có địa chỉ gửi thuộc danh sách cho phép và bỏ thư còn lại; khi danh sách vượt bộ nhớ, mỗi thư có thể cần một lần tra đĩa.
- **Hàm băm là hàm tất định** (ghi chú Bài 05, Mục 9). Một hàm băm đã chọn cho cùng giá trị trên cùng đầu vào, ở mọi lần gọi và trên mọi máy dùng hàm đó. Tính ngẫu nhiên, nếu có, đến từ phép chọn hàm trong một họ hàm, không đến từ từng lần gọi; tính đều của phép chọn là một giả thiết riêng, được nêu tại từng kết quả cần đến nó. Hàm phân phối của MapReduce trong bộ trang chiếu Bài 02 dựa trên cùng tính chất: mọi tác vụ Map dùng chung một hàm, nên mọi cặp cùng khóa về cùng một tác vụ Reduce.
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
| $t$ | một phần tử của dòng truy vấn, là bộ (người dùng, truy vấn, thời điểm); khi cần chỉ số, $t=x_i$ | bộ nhiều thành phần |
| $\mathcal K$; $K$; $K(t)$ | miền khóa; một giá trị khóa; khóa của bộ $t$, gồm các thành phần nhận diện đơn vị thống kê | tập; phần tử của $\mathcal K$ |
| $u$; $d$ | số truy vấn khác nhau mà một người dùng gửi đúng một lần; đúng hai lần | số nguyên không âm |
| $h$ | hàm băm dùng để lấy mẫu theo khóa, cố định sau khi chọn | $\mathcal K\to\{0,\ldots,b-1\}$ |
| $b$; $a$ | số ngăn, tức số giá trị của $h$; ngưỡng, bộ $t$ được chọn khi $h(K(t))<a$, tỷ lệ $a/b$ | số nguyên, $b\ge1$, $0\le a\le b$ |
| $\tau$ | ngưỡng băm khi điều chỉnh tỷ lệ: bộ được nhận khi $h(K(t))\le\tau$, ứng với $a=\tau+1$ | số nguyên, $-1\le\tau\le b-1$ |
| $s$ | sức chứa của hồ chứa | số nguyên, $s\ge1$ |
| $W[1..s]$ | mảng hồ chứa, giữ mẫu hiện tại | mảng $s$ ô, mỗi ô chứa một phần tử của dòng |
| $j$ | số ngẫu nhiên sinh khi phần tử thứ $r>s$ đến | số nguyên đều trên $\{1,\ldots,r\}$ |
| $S$; $m$ | tập khóa được chèn vào Bloom filter; số khóa, $m=\lvert S\rvert$ | tập hữu hạn, $S\subseteq\mathcal K$; số nguyên dương |
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
- Tên phần tử trong vết chạy hồ chứa viết chữ đứng, như dòng a, x, c, y, z của slide MMDS, để không lẫn với các ký hiệu nghiêng $a$, $x_i$, $y$.
- Ký hiệu khác MMDS ở bốn chỗ, vì các chữ của sách đã mang nghĩa khác trong bảng: số truy vấn xuất hiện một lần $s$ (§4.2.1) viết là $u$; số giá trị băm $B$ và ngưỡng $t$ (§4.2.4) viết là $b$ và $\tau$; số đích $x$ và số phi tiêu $y$ (§4.3.3) là $n$ bit và $km$ phép băm; mẫu $S$ và số phần tử đã thấy $n$ trên slide hồ chứa viết là $W$ và $r$.
- Số liệu lấy từ MMDS: Hình 4.1, các Ví dụ 4.1, 4.3, 4.4, ngân sách $1/10$ dòng ở §4.2.1, các bài 4.2.1 và 4.3.1–4.3.3. Mảng 11 bit với các khóa 25, 159, 585 và truy vấn 118 lấy từ slide của Ullman cho học phần CS246 (2017). Giá trị băm của An, Bình, Chi, dãy số ngẫu nhiên của vết hồ chứa, các khóa truy vấn khác trên mảng 11 bit và dữ kiện các bài tập không mang số bài sách do học phần dựng để minh họa. Khi số in trong sách khác phép tính lại, giá trị tính lại được dùng và chỗ khác được nêu tại chỗ.

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
| Đặc tả và thuật toán hồ chứa (`lec-08-topic-07`) | cốt lõi | 3.1–3.3 | Mẫu cỡ $s$, vết chạy với $s=2$, giả mã → định lý xác suất |
| Xác suất $s/r$ và chi phí hồ chứa (`lec-08-topic-08`) | cốt lõi; số lần ghi kỳ vọng là bổ sung | 3.4–3.5 | Chứng minh quy nạp, chi phí → so sánh với mẫu theo khóa |
| Cơ chế Bloom filter (`lec-08-topic-09`) | cốt lõi | 4.1–4.3 | $10^9$ địa chỉ trong 1 GB, ví dụ 11 bit, xây và truy vấn → bảo đảm |
| Không âm giả (`lec-08-topic-10`) | cốt lõi | 4.4 | Bốn điều kiện, phản ví dụ khi xóa bit → phân tích dương giả |
| Mật độ bit và xác suất dương giả (`lec-08-topic-11`) | cốt lõi; cận dưới $q^k\le p_{FP}$ là bổ sung | 4.5 | $q$ chính xác, xấp xỉ $q^k$, dạng mũ → hàm $p(k)$ |
| Số hàm băm tối ưu (`lec-08-topic-12`) | cốt lõi; định cỡ cho 1% là bổ sung | 4.6 | $k^*=(n/m)\ln2$, chọn $k$ nguyên → định cỡ Bloom filter |
| Chọn cấu trúc theo đầu ra (`lec-08-topic-13`) | cốt lõi | 5 | Đơn vị, bảo đảm, chi phí → tình huống áp dụng |
| Tình huống áp dụng (`lec-08-topic-14`) | cốt lõi | Tình huống | Bài toán giải trọn, một tình huống vi phạm giả thiết → tóm tắt |
| Tóm tắt chương (`lec-08-topic-15`) | cốt lõi | Tóm tắt | Chuỗi kết quả, giả thiết hay bị bỏ quên → Bài 09 |
| Bài tập củng cố (`lec-08-topic-16`) | cốt lõi | Bài tập | Ba mức, gồm bốn bài MMDS → kiểm ba mục tiêu |
| Đọc thêm và tài liệu (`lec-08-topic-17`) | đọc thêm | Tham khảo | Ánh xạ mục ↔ nguồn, lấy mẫu có trọng số, Bài 09 |

Quan hệ tiên quyết giữa các mục như sau. Mô hình dòng một lượt (Mục 1) dùng phần tiên quyết và là đầu vào của cả ba nhánh. Nhánh lấy mẫu theo khóa đi tuần tự qua Mục 2.1–2.5. Nhánh hồ chứa gồm đặc tả và thuật toán (Mục 3.1–3.3) rồi xác suất $s/r$ và chi phí (Mục 3.4–3.5); phần sau cần quy nạp ở tiên quyết và so kết quả với mẫu nhất quán theo khóa (Mục 2.2). Nhánh Bloom filter đi tuần tự qua Mục 4.1–4.6 và cần giới hạn của $(1-1/c)^c$, bất đẳng thức Jensen cùng phần đạo hàm ở tiên quyết. Ba nhánh gặp nhau ở Mục 5, rồi đi qua tình huống áp dụng và tóm tắt chương; bài tập củng cố dùng mọi mục trước. Đếm số phần tử phân biệt, mômen và cửa sổ thời gian thuộc Bài 09.

<!-- note-topic-id: lec-08-topic-02 -->
## 1. Mô hình dòng một lượt

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

Không truy vấn nào cần cả lịch sử: hai truy vấn đầu giữ một hoặc hai số dù dòng dài bao nhiêu, truy vấn thứ ba giữ không quá 24 số. Ngược lại, câu hỏi "số đo thứ ba là bao nhiêu" không trả lời được từ ba trạng thái trên, vì số $2$ đã bị bỏ khi đến. Trạng thái được chọn theo truy vấn, trước khi dòng đến.

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

Một cách trực quan, mô hình dòng là một bộ xử lý đứng giữa các dòng đi vào và các câu trả lời đi ra, với hai nơi lưu có vai trò khác nhau. Hình dưới vẽ lại MMDS Hình 4.1 (tr.132) và đặt mỗi thành phần của Định nghĩa 08.1 vào một chỗ trong hệ thống.

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

**(b) Tính.** Sau 8 số: $r=8$, $\sum x_i=27$, $\sum x_i^2=1+25+4+49+16+0+9+25=129$. Do đó $\bar x_8=27/8=3{,}375$ và

$$
\sigma_8^2=\frac{129}{8}-\Bigl(\frac{27}{8}\Bigr)^2=16{,}125-11{,}390625=4{,}734375 .
$$

**Kiểm tra lại.** Tính trực tiếp, các độ lệch $x_i-3{,}375$ có bình phương $5{,}640625$; $2{,}640625$; $1{,}890625$; $13{,}140625$; $0{,}390625$; $11{,}390625$; $0{,}140625$; $2{,}640625$, tổng $37{,}875$, và $37{,}875/8=4{,}734375$.
:::

Như vậy, chúng ta đã có đặc tả chung cho các cấu trúc của chương: thuật toán dòng một lượt trả lời từ trạng thái chọn theo truy vấn (Định nghĩa 08.1) và được đo bằng bốn đại lượng trên mỗi phần tử (Định nghĩa 08.3), với Thuật toán 08.2 làm trường hợp mẫu. Các truy vấn của mục này, kể cả phương sai ở Bài tập 08.1, là những thống kê có trạng thái cỡ hằng trả lời chính xác. Câu hỏi của máy tìm kiếm thì khác: đo tỷ lệ truy vấn tìm kiếm lặp của từng người dùng khi chỉ lưu được $1/10$ dòng (MMDS §4.2.1, tr.136). Trạng thái khi đó phải là một mẫu các phần tử, và cách chọn mẫu quyết định câu trả lời có đúng không. Trong Mục 2, chúng ta xét cách chọn mẫu đó.

## 2. Lấy mẫu theo khóa

Máy tìm kiếm nhận dòng bộ $t$ dạng (người dùng, truy vấn tìm kiếm, thời điểm), chỉ lưu được $1/10$ dòng, và muốn biết tỷ lệ truy vấn lặp của người dùng điển hình trong tháng vừa qua (MMDS §4.2.1, tr.136). Mục 1 cho thấy một số thống kê trên mọi phần tử, như giá trị lớn nhất, trung bình và phương sai, có trạng thái cỡ hằng; câu hỏi này thì cần một mẫu các bộ, vì tỷ lệ lặp của một người được tính từ chính các truy vấn của người đó. Chúng ta cần chọn mẫu sao cho tỷ lệ tính trên mẫu bằng tỷ lệ thật, với trạng thái quyết định không tăng theo dòng.

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

Với An, $u=d=1$, mệnh đề cho $1/29\approx0{,}034$ thay cho $1/2$. Số này khác $1/19$ của Ví dụ 08.3 vì mẫu số tính cả truy vấn "băm". Bước 2 dùng độc lập giữa hai bộ của cùng một truy vấn, và chính sự tách rời này gây sai lệch: một truy vấn lặp bị cắt thành hai quyết định riêng.

::: remark Nhận xét 08.7 (Nhầm lẫn thường gặp)
- Mỗi người dùng vẫn giữ trung bình $1/10$ số truy vấn của mình; sai lệch không nằm ở tỷ lệ giữ mà ở đơn vị bị cắt. Với tỷ lệ giữ $p$ bất kỳ, cùng phép đếm cho tỷ số $dp/(u+(2-p)d)$, vẫn khác $d/(u+d)$ khi $p<1$; với $p=1/10$ ta được lại $d/(10u+19d)$.
- $d/(10u+19d)$ là tỷ số của hai số đếm kỳ vọng, không phải kỳ vọng của tỷ lệ tính trên mẫu.
:::

<!-- note-topic-id: lec-08-topic-04 -->
### 2.2 Mẫu nhất quán theo khóa

Mệnh đề 08.6 chỉ ra đơn vị cần giữ trọn là người dùng: giữ hoặc bỏ cả lịch sử truy vấn của mỗi người. MMDS (§4.2.2, tr.137) nêu một phương án trực tiếp: lần đầu gặp một người dùng, rút một số đều trong $\{0,\ldots,9\}$, ghi nhãn "giữ" nếu số là $0$ và "bỏ" nếu khác; bộ đến sau tra bảng nhãn và vào mẫu khi nhãn là "giữ".

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

Hình dùng $b=10$ ngăn, ngưỡng $a=1$, tức giữ bộ khi $h=0$; cả ba bộ của An vào mẫu. Các giá trị $h(\text{An})=0$, $h(\text{Bình})=7$, $h(\text{Chi})=4$ là một hàm minh họa, chọn trùng số rút của Ví dụ 08.4 nên hai phương án cho cùng mẫu, nhưng không có bảng nào được lưu. Slide MMDS (Streams 1, tr.15–16) minh họa cùng cơ chế với tỷ lệ 30%, tức giữ khi giá trị băm thuộc $\{0,1,2\}$.

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
2. Tính $v\gets h(K(t))$.
3. Nếu $v<a$ thì đưa $t$ vào mẫu; nếu không thì bỏ $t$.

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
**Giả thiết.** $b\ge1$, $0\le a\le b$, $h:\mathcal K\to\{0,\ldots,b-1\}$ cố định suốt dòng. Cho phần (b): $h$ được chọn ngẫu nhiên từ một họ hàm sao cho với mỗi khóa $K$ và mỗi $v\in\{0,\ldots,b-1\}$, $\Pr_h[h(K)=v]=1/b$.

**Kết luận.**

(a) Với mọi hai bộ $t$, $t'$ có $K(t)=K(t')$, Thuật toán 08.9 giữ cả hai hoặc bỏ cả hai.

(b) Mỗi khóa $K$ được giữ với xác suất $\Pr_h[h(K)<a]=a/b$.

**Điều kiện áp dụng.** Phần (a) đúng với mọi hàm $h$, kể cả hàm không đều. Phần (b) là xác suất theo phép chọn $h$, không theo các lần xuất hiện của khóa.

**Phạm vi.** Mệnh đề nói về từng khóa. Nó không khẳng định mẫu chứa đúng $a/b$ số khóa hay $a/b$ số bộ.
:::

::: proof
**Bước 1 (nhất quán).** Nếu $K(t)=K(t')$ thì $h(K(t))=h(K(t'))$, vì $h$ là một hàm cố định. Hai phép so sánh ở bước 3 so cùng một số với cùng $a$, nên cho cùng kết quả.

**Bước 2 (xác suất).** Biến cố $h(K)<a$ là hợp rời của $a$ biến cố $h(K)=v$, $v=0,\ldots,a-1$. Theo giả thiết, mỗi biến cố có xác suất $1/b$, nên

$$
\Pr_h[h(K)<a]=\sum_{v=0}^{a-1}\Pr_h[h(K)=v]=\frac ab. \qquad\square
$$
:::

Phần (a) là bảo đảm tất định thay cho bảng nhãn: mọi truy vấn tìm kiếm của một người được giữ đều có trong mẫu, nên tỷ lệ lặp của người đó tính đúng, như $1/2$ của An. Phần (b) cho mỗi người cùng xác suất $a/b$ được chọn, nên mọi tổng tính trên mẫu chia cho $a/b$ có kỳ vọng bằng tổng thật; Hệ quả 08.12 ở Mục 2.4 là một trường hợp. Để số người được chọn tập trung quanh $a/b$ số người, cần thêm giả thiết các khóa khác nhau nhận giá trị băm độc lập. Tính đều theo từng khóa không đủ: họ gồm $b$ hàm hằng $h\equiv c$, với $c$ chọn đều trong $\{0,\ldots,b-1\}$, thỏa giả thiết của phần (b), nhưng mẫu hoặc chứa mọi người dùng, hoặc rỗng.

Các giả thiết của kết quả có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "$h$ cố định": nếu hàm băm được chọn lại mỗi giờ, hai bộ của An ở hai giờ khác nhau có thể nhận hai quyết định khác nhau, và mẫu quay lại cắt rời đơn vị như Mục 2.1.
- Bỏ "đều theo cách chọn $h$": với $1\le a<b$, họ hàm chỉ gồm hàm luôn trả $0$ vẫn cho phần (a), nhưng mọi khóa được giữ với xác suất $1$, không phải $a/b$.
- Bỏ "khóa nhận diện đúng đơn vị": nếu khóa là cặp (người dùng, thời điểm), mỗi bộ có khóa riêng, và Mục 2.3 chỉ ra hậu quả.

Bước 1 dùng tính cố định của $h$; Bước 2 dùng tính đều theo từng khóa.

::: remark Nhận xét 08.11 (Trong thực hành)
Hàm $h$ là một hàm băm có tham số, chẳng hạn hạt giống, chọn một lần khi khởi động và dùng chung trên mọi máy xử lý dòng; đổi tham số giữa chừng phá phần (a) của Mệnh đề 08.10. Máy tìm kiếm thật nhận địa chỉ IP chứ không nhận người dùng; MMDS (§4.2.1, chú thích tr.136) giả định mỗi địa chỉ ứng với một người, điều chỉ đúng gần đúng, và khi nhiều người chung một địa chỉ, tỷ lệ lặp đo được là của cả nhóm. Tính đều theo từng khóa là giả thiết về phép chọn hàm, không kiểm được trên một hàm đã chọn.
:::

<!-- note-topic-id: lec-08-topic-05 -->
### 2.3 Chọn khóa theo đơn vị thống kê

Mệnh đề 08.10 giữ trọn từng khóa, nên khóa quyết định thống kê nào tính đúng trên mẫu. MMDS (§4.2.3, tr.137) nêu rằng cùng dòng (người dùng, truy vấn, thời điểm) có thể lấy mẫu theo người dùng, theo truy vấn hoặc theo cặp (người dùng, truy vấn). Ba lựa chọn này phục vụ ba thống kê khác nhau.

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

::: exercise Bài tập 08.2 (Khóa người dùng và thời điểm)
Với dòng truy vấn tìm kiếm và tỷ lệ $a/b=1/10$, dùng khóa là cặp (người dùng, thời điểm) thay cho người dùng. Mẫu có cho tỷ lệ truy vấn lặp của mỗi người không lệch không?
:::

::: hint
Xét hai bộ "đồ thị" của An: chúng có cùng khóa không?
:::

::: solution
Không. Hai bộ của cùng một người có thời điểm khác nhau, nên có hai khóa khác nhau, và Mệnh đề 08.10(a) không ràng buộc quyết định của chúng. Nếu các khóa khác nhau nhận giá trị băm độc lập theo cách chọn $h$, mỗi bộ được giữ độc lập với xác suất $1/10$, đúng giả thiết của Mệnh đề 08.6; tỷ số tính trên mẫu là $d/(10u+19d)$, với An là $1/29$. Thành phần thời điểm tách một đơn vị thành nhiều khóa, vi phạm bước 3 của quy trình.
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

**Diễn giải.** Cỡ mẫu thực không bao giờ gần $200\,200$: kỳ vọng đúng nhưng không mô tả một lần chạy.

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
3. Chừng nào mẫu có hơn $G$ bộ: lấy $v$ là giá trị băm lớn nhất trong mẫu (tra chỉ mục), xóa mọi bộ có giá trị băm $v$, rồi đặt $\tau\gets v-1$.

**Dừng.** Mỗi lần lặp ở bước 3 xóa ít nhất một bộ, nên bước 3 dừng sau không quá số bộ đang có trong mẫu.

**Trường hợp biên.** Một khóa có hơn $G$ bộ buộc $\tau$ xuống dưới giá trị băm của nó, nên khóa đó bị bỏ trọn. Bước 3 hạ $\tau$ nhiều đơn vị một lần, qua các giá trị băm không có bộ nào, theo gợi ý của MMDS (§4.2.4, tr.138).

**Chi phí.**

| Thành phần | Số lần sau $r$ bộ | Chi phí mỗi lần |
|---|---|---|
| băm và so sánh ở bước 2 | $r$ | 1 phép băm, 1 phép so sánh |
| đưa vào chỉ mục | không quá $r$ | $O(\log G)$ |
| lần dọn ở bước 3 | không quá số giá trị băm phân biệt từng có trong mẫu | $O(\log G)$ để tra $v$ |
| xóa một bộ | không quá $r$ | $O(1)$ trên danh sách của $v$ |

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
| 4 | An | 9 | đưa vào; 4 bộ vượt $G$: $v=7$, xóa bộ của Bình | An, An, An | 6 |
| 5 | Chi | 6 | $4\le6$, đưa vào; 4 bộ vượt $G$: $v=4$, xóa bộ của Chi | An, An, An | 3 |

**Diễn giải.** Sau bước 5, mẫu là mẫu theo khóa với $a=\tau+1=4$: giữ trọn An, bỏ trọn Bình và Chi. Ở bước 4, ngưỡng nhảy từ 9 xuống 6, bỏ qua các giá trị 9 và 8 không có bộ nào.

**Kiểm tra lại.** Các bộ đã đọc có $h\le3$ là ba bộ của An, đúng mẫu sau bước 5; mẫu có 3 bộ, bằng $G$.
:::

::: proposition Mệnh đề 08.14 (Bất biến của mẫu theo ngưỡng)
**Giả thiết.** Thuật toán 08.13 với $h$ cố định.

**Kết luận.** Sau mỗi bước, mẫu đúng bằng tập các bộ đã đọc có $h(K(t))\le\tau$. Do đó mẫu luôn là mẫu theo khóa với ngưỡng $a=\tau+1$, và $\tau$ không tăng.

**Điều kiện áp dụng.** Bước 3 xóa đúng các bộ có giá trị băm lớn nhất $v$ trong mẫu trước khi đặt $\tau\gets v-1$.

**Phạm vi.** Mệnh đề không nói gì về xác suất; tỷ lệ khóa $(\tau+1)/b$ giảm dần theo dòng.
:::

::: proof
**Bước 1 (khởi tạo).** Trước bộ đầu tiên, mẫu rỗng và chưa có bộ nào được đọc.

**Bước 2 (đưa bộ vào).** Giả sử bất biến đúng trước khi $t$ đến. Bước 2 đưa $t$ vào đúng khi $h(K(t))\le\tau$, nên bất biến đúng sau bước 2.

**Bước 3 (hạ ngưỡng).** Giả sử mẫu bằng tập các bộ đã đọc có $h\le\tau$ và mẫu khác rỗng. Gọi $v$ là giá trị băm lớn nhất trong mẫu, nên $v\le\tau$. Không bộ nào trong mẫu có giá trị trong khoảng $(v,\tau]$; theo bất biến, cũng không bộ đã đọc nào có giá trị trong khoảng đó. Xóa các bộ có giá trị $v$ để lại đúng các bộ đã đọc có $h\le v-1$, nên đặt $\tau\gets v-1$ giữ bất biến, và $\tau$ giảm. Theo quy nạp trên số bước, bất biến đúng sau mọi bước; $\tau$ chỉ thay đổi ở bước 3, và ở đó nó giảm. $\square$
:::

Như vậy, chúng ta đã chỉ ra lấy mẫu từng bộ làm sai tỷ lệ lặp (Mệnh đề 08.6), thay bảng nhãn bằng hàm băm cố định (Định nghĩa 08.8, Thuật toán 08.9), chứng minh mẫu giữ trọn từng khóa và giữ mỗi khóa với xác suất $a/b$ (Mệnh đề 08.10), tính cỡ mẫu kỳ vọng $ar/b$ (Hệ quả 08.12), và giữ ngân sách bằng ngưỡng giảm dần (Thuật toán 08.13, Mệnh đề 08.14). Tuy nhiên, cỡ mẫu theo khóa phụ thuộc vào số bộ của các khóa được chọn: với tỷ lệ cố định, nó tăng theo dòng; với ngân sách cố định, tỷ lệ khóa giảm dần và một khóa nhiều bộ có thể bị đẩy trọn ra khỏi mẫu. Mẫu đại diện cho mọi phần tử đã đọc cần đúng $s$ phần tử ở mọi thời điểm. Trong Mục 3, chúng ta đổi đơn vị chọn từ khóa sang vị trí trên dòng và xây lấy mẫu hồ chứa với cỡ mẫu cố định.

## 5. Lấy mẫu hồ chứa

### Vấn đề

Trong lấy mẫu theo khóa, kích thước mẫu không cố định. Ngược lại, nhiều khi ta cần giữ mẫu đúng $s$ phần tử trên một dòng có độ dài chưa biết — chẳng hạn do giới hạn bộ nhớ chính. Đơn vị chọn ở đây là vị trí trong dòng, không phải khóa.

### Đặc tả

- Đầu vào: dòng vị trí $1,2,\dots$; ngân sách nguyên $s\ge1$; bộ sinh số ngẫu nhiên đều, độc lập.
- Điều kiện sau: nếu $r\le s$ thì giữ cả $r$ vị trí. Nếu $r>s$ thì giữ đúng $s$ vị trí và mỗi vị trí trong $r$ phần tử đã thấy có xác suất biên $s/r$.
- Bảo đảm chỉ là xác suất biên của từng vị trí, không suy ra tính độc lập hay mọi tập con có cùng xác suất.

<div class="figure">

![Dòng a x c y z với các số ngẫu nhiên 2, 4, 1 và hồ chứa lần lượt đổi thành a c rồi z c](img/lec-08/reservoir-trace.svg)

</div>

Vết chạy với $s=2$, dòng a, x, c, y, z và các số ngẫu nhiên $j$ lần lượt là $j=2,4,1$:

| Bước $r$ | Phần tử | $j$ | Trạng thái $W$ |
|---|---|---|---|
| 1 | a | — | a |
| 2 | x | — | a x |
| 3 | c | 2 | a c |
| 4 | y | 4 ($>s$) | a c |
| 5 | z | 1 | z c |

Ở $r=3$ thì $j=2\le s$ nên c thay ô 2. Ở $r=4$ thì $j=4>s$ nên bỏ y. Ở $r=5$ thì $j=1$ nên z thay ô 1. Số $j$ ở đây chỉ là một lần chạy minh họa, không phải xác suất bảo đảm; chúng phụ thuộc vào bộ sinh số ngẫu nhiên.

### Thuật toán

```text
HỒ-CHỨA(x_r, r, s, W)
  nếu r ≤ s: W[r] ← x_r
  ngược lại:
    j ← số nguyên đều trong {1,…,r}
    nếu j ≤ s: W[j] ← x_r
  trả W
```

Với $r>s$, sinh $j$ đều trong $1,\dots,r$ và chèn phần tử mới vào ô $j$ khi $j\le s$ tương đương với: giữ phần tử mới với xác suất $s/r$, rồi chọn đều một trong $s$ ô để thay. Mỗi lần gọi cần phép sinh mẫu đều và độc lập có điều kiện với lịch sử.

### Bất biến và chứng minh quy nạp

**Mệnh đề.** Sau khi xử lý $r\ge s$ vị trí, hồ chứa có đúng $s$ phần tử và mỗi vị trí $i\le r$ có xác suất $s/r$ nằm trong hồ.

**Cơ sở $r=s$.** Giữ cả $s$ vị trí, nên xác suất là $1=s/s$.

Giả sử đúng với $r$. Xét bước $r+1$.

**(a) Phần tử mới.** Phần tử mới $x_{r+1}$ vào hồ khi $j\le s$:

$$\Pr[x_{r+1}\in W]=\frac{s}{r+1}.$$

**(b) Phần tử cũ.** Với điều kiện phần tử cũ đang trong $W$, nó bị thay khi $j\le s$ và $j$ đúng ô của nó:

$$\Pr[\text{bị thay}]=\frac{s}{r+1}\cdot\frac{1}{s}=\frac{1}{r+1}.$$

Vì vậy xác suất sống sót của phần tử cũ qua bước $r+1$ là

$$\frac{s}{r}\cdot\left(1-\frac{1}{r+1}\right)=\frac{s}{r}\cdot\frac{r}{r+1}=\frac{s}{r+1}.$$

Kích thước đúng $s$ được duy trì vì bước $r>s$ hoặc không đổi $W$, hoặc thay đúng một ô.

### Chi phí, giả thiết và tự kiểm

- Chi phí: $\Theta(s)$ bộ nhớ; $\Theta(1)$ thời gian mỗi phần tử trong mô hình RAM, nếu truy cập mảng $O(1)$ và các phép sinh số nguyên đều có chi phí $O(1)$.
- Giả thiết: bộ sinh số ngẫu nhiên đều trong $1,\dots,r$ và độc lập; nếu thiên lệch hoặc phụ thuộc, các xác suất $s/r$ không còn đúng.

Tự kiểm: với $s=100, r=1\,000$, xác suất một vị trí cụ thể còn lại là bao nhiêu? Đáp án: $s/r=0{,}1$.

> Hồ chứa không bảo đảm tính nhất quán theo khóa: cùng một khóa có thể được giữ một lần, nhiều lần hoặc không lần nào tùy theo các vị trí của nó. Đây là điểm khác cơ bản với lấy mẫu theo khóa.

## 6. Đặc tả và cơ chế Bloom filter

### Vai trò

Khi cần lọc dòng theo thuộc tính thành viên trong một tập $S$ đủ lớn không thể để trong bộ nhớ chính, ta dùng bộ lọc thành viên xác suất. Mô hình đến từ MMDS: tập $S$ gồm một tỷ địa chỉ thư điện tử được phép, ngân sách một gigabyte (tám tỷ bit), và mỗi bộ đến cần được lọc trước phép tra cứu đĩa chậm.

Nếu $S$ có $m=10^9$ khóa và ngân sách $n=8\cdot10^9$ bit thì trung bình có $n/m=8$ bit cho mỗi khóa. Mỗi khóa được băm một lần vào mảng bit và đặt bit tương ứng bằng 1; khi một địa chỉ đến, băm nó và chỉ cho đi nếu bit băm bằng 1.

### Đặc tả tổng quát

Một Bloom filter gồm:

- một mảng $n$ bit, ban đầu tất cả bằng 0;
- $k\ge1$ hàm băm $h_1,\dots,h_k:\mathcal K\to\{0,\dots,n-1\}$;
- một tập $S$ gồm $m$ khóa.

Mỗi khóa $x\in S$ được băm qua cả $k$ hàm và mọi bit $B[h_i(x)]$ được đặt bằng 1; các bit còn lại vẫn bằng 0. Để truy vấn khóa $y$, xét $k$ bit $B[h_i(y)]$. Nếu một trong các bit đó bằng 0 thì $y$ **chắc chắn không thuộc** $S$; nếu cả $k$ bit đều bằng 1 thì $y$ **có thể thuộc**, và cần phép kiểm tra chính xác nếu quyết định không được phép sai.

<div class="figure">

![Khóa đến qua Bloom filter; có bit không thì bị loại, còn có thể thuộc mới được tra cứu chính xác](img/lec-08/bloom-pipeline.svg)

</div>

### Ví dụ 11 bit

Với mảng $n=11$ bit, định nghĩa: $h_1(x)$ lấy các bit ở vị trí lẻ từ phải (vị trí 1-based) của biểu diễn nhị phân, giữ thứ tự từ trọng số cao xuống thấp, diễn giải thành số nguyên rồi lấy modulo 11; $h_2(x)$ làm tương tự với các bit ở vị trí chẵn.

Theo quy ước trình bày, mảng lọc hiển thị chỉ số $0,\dots,10$ từ trái qua phải. Với $x=159=10011111_2$, các bit vị trí lẻ cho $0111_2=7$ và các bit vị trí chẵn cho $1011_2=11\equiv0\pmod{11}$, nên $(h_1,h_2)=(7,0)$.

| Phần tử $x$ | $h_1$ | $h_2$ | Mảng $B$ (chỉ số 0–10) |
|---|---|---|---|
| — | | | 00000000000 |
| 25 | 5 | 2 | 00100100000 |
| 159 | 7 | 0 | 10100101000 |
| 585 | 9 | 7 | 10100101010 |

<div class="figure">

![Bit 0 đến 10 từ trái sang phải; ba khóa đặt các bit 0, 2, 5, 7, 9; khóa 118 gặp bit 3 bằng không nên chắc chắn không thuộc](img/lec-08/bloom-11bit.svg)

</div>

Chỉ bit 7 bị va chạm khi thêm 585 (đã được đặt bởi 159). Các kết quả còn lại: $25\to(5,2)$, $585\to(9,7)$, $118\to(3,5)$.

Truy vấn $y=118=1110110_2$: $(h_1,h_2)=(3,5)$. Bit 5 bằng 1 nhưng bit 3 bằng 0, nên $118$ chắc chắn không thuộc $S$.

> Cặp hàm băm ở đây chỉ là ví dụ cụ thể để cho thấy va chạm; đặc tả tổng quát ở trên không phụ thuộc vào cách chọn $h_i$ cụ thể.

### Xây dựng và truy vấn

```text
XÂY-BLOOM(S, n, h_1,…,h_k)
  B[0…n-1] ← 0
  với mỗi khóa x trong S:
    với i = 1,…,k: B[h_i(x)] ← 1
  trả B
```

```text
KIỂM-TRA-BLOOM(x, B, h_1,…,h_k)
  với i = 1,…,k:
    nếu B[h_i(x)] = 0: trả "chắc chắn không thuộc"
  trả "có thể thuộc"
```

Va chạm không tạo ô mới; đặt lại bit 1 không đổi trạng thái. Chi phí xây $\Theta(km)$ phép băm và đặt bit, bộ nhớ $n$ bit; truy vấn xấu $\Theta(k)$, nhưng dừng sớm giúp khóa âm thường rẻ hơn $k$ phép băm.

::: exercise Tự kiểm
Khi một khóa truy vấn gặp một bit 0, Bloom filter có cần kiểm các bit còn lại không?
:::

::: solution
Không. Một bit 0 đã đủ kết luận khóa chắc chắn không thuộc tập.
:::

## 7. Không âm giả và giới hạn bảo đảm

**Mệnh đề.** Nếu $x\in S$, truy vấn Bloom trả lời "có thể thuộc" khi:

- không xóa hoặc đặt lại bit sau khi xây dựng;
- dùng đúng cùng $h_1,\dots,h_k$ và cùng trạng thái mảng;
- các hàm băm xác định (cùng khóa chọn cùng bit);
- mọi phép ghi bit đã hoàn tất trước truy vấn.

Lúc xây, với mỗi $i$ thuật toán đặt $B[h_i(x)]=1$; các điều kiện trên bảo đảm những bit đó không đổi. Vì vậy mọi bit mà $x$ băm tới vẫn bằng 1 khi truy vấn.

Khóa ngoài $S$ vẫn có thể **dương giả**: cả $k$ bit băm của nó có thể đã được đặt bởi các khóa khác trong $S$. Bloom filter không hứa không có dương giả; bảo đảm không âm giả chỉ đúng khi các điều kiện trạng thái thỏa.

Ví dụ, nếu $x\in S$ đã đặt các bit 2 và 7 thì truy vấn lại $x$ đọc hai bit 1. Nếu một thao tác xóa tùy tiện đặt bit 7 về 0, chính $x$ có thể bị trả lời “chắc chắn không thuộc”.

::: exercise Tự kiểm
Điều kiện nào của mệnh đề bị vi phạm trong ví dụ trên?
:::

::: solution
Trạng thái đã bị xóa bit sau khi xây dựng. Bloom filter chuẩn trong bài không hỗ trợ thao tác xóa như vậy.
:::

## 8. Mật độ bit và xác suất dương giả

### Mật độ bit hữu hạn

Dưới mô hình mỗi phép băm đều và độc lập trên $n$ bit, mỗi phép băm đặt đúng một bit. Sau $km$ phép băm, xác suất một bit cụ thể vẫn bằng 0 là

$$\left(1-\frac1n\right)^{km},$$

và do đó xác suất bit đó bằng 1 là

$$q=1-\left(1-\frac1n\right)^{km}.$$

Đây là xác suất **chính xác** cho một bit dưới mô hình $km$ phép băm iid, và cũng là mật độ bit 1 kỳ vọng.

### Xác suất dương giả là xấp xỉ

Xác suất dương giả được tính là

$$p_{FP}\approx\left[1-\left(1-\frac1n\right)^{km}\right]^k\approx\left(1-e^{-km/n}\right)^k.$$

Cần phân biệt hai dấu xấp xỉ:

- **Xấp xỉ chuẩn $q^k$.** Giá trị $q=1-(1-1/n)^{km}$ là mật độ biên chính xác dưới mô hình $km$ phép băm iid, nhưng trạng thái các bit phụ thuộc lẫn nhau (chúng chia sẻ các lần đặt), và các vị trí truy vấn có thể trùng nhau. Nâng $q$ lên $k$ giả định các vị trí truy vấn độc lập, nên chỉ là xấp xỉ.
- **Xấp xỉ mũ.** Dạng $(1-e^{-km/n})^k$ dùng giới hạn $(1-1/n)^n\to e^{-1}$ khi $n$ lớn, nên còn đòi hỏi thêm điều kiện $n$ lớn.

Ví dụ: $m=10^9$, $n=8\cdot10^9$. Với $k=1$: $1-e^{-1/8}\approx0{,}1175$ (so với xấp xỉ thô $1/8=0{,}125$). Với $k=2$: $(1-e^{-1/4})^2\approx0{,}0489$. Sách in 0,0493; phép tính trực tiếp cho 0,048929…, nên ghi chú dùng giá trị đã kiểm lại.

::: exercise Tự kiểm
Trong hai bước từ $q$ đến $(1-e^{-km/n})^k$, bước nào cần $n$ lớn?
:::

::: solution
Bước thay $(1-1/n)^{km}$ bằng $e^{-km/n}$ cần $n$ lớn. Việc nâng $q$ lên $k$ là một xấp xỉ khác về tính độc lập.
:::

## 9. Chọn số hàm băm

### Đánh đổi khi tăng $k$

Tăng $k$ có hai tác động ngược nhau:

- Mỗi hàm băm buộc khóa ngoài $S$ vượt thêm một phép thử, làm giảm $p_{FP}$.
- Mỗi hàm băm cũng đặt thêm bit 1, làm mảng nhanh bão hòa, tăng cơ hội bit truy vấn bằng 1.

Nếu mọi bit đã bằng 1 thì mọi truy vấn đều "có thể thuộc"; vì vậy cần chọn $k$ thay vì tăng vô hạn.

### Dẫn xuất $k^*$

Dùng dạng xấp xỉ mũ. Đặt $\rho=m/n$ (tỷ số khóa trên bit) và xét

$$\ell(k)=\ln p(k)=k\ln\left(1-e^{-k\rho}\right),\qquad k>0.$$

Vì $\ln$ đồng biến, cực tiểu của $p(k)$ cũng là cực tiểu của $\ell(k)$. Đạo hàm:

$$\ell'(k)=\ln\left(1-e^{-k\rho}\right)+\frac{k\rho}{e^{k\rho}-1}=0.$$

Đặt $x=k\rho$ và $t=e^{-x}$. Để chứng minh cực tiểu, nhân dấu của $\ell'(k)$ với $1-t>0$: dấu của $\ell'(k)$ bằng dấu của

$$F(t)=(1-t)\ln(1-t)-t\ln t.$$

Biểu thức này phản đối xứng quanh $t=1/2$: $F(t)<0$ khi $t>1/2$, $F(t)=0$ tại $t=1/2$, và $F(t)>0$ khi $t<1/2$. Vì $t=e^{-k\rho}$ giảm khi $k$ tăng, $\ell'(k)<0$ trước $k\rho=\ln2$ và $\ell'(k)>0$ sau đó. Vậy

$$k^*=\frac{n}{m}\ln2.$$

Với $k$ nguyên dương, chọn $k\ge1$ bằng cách so sánh $\max(1,\lfloor k^*\rfloor)$ và $\max(1,\lceil k^*\rceil)$: lấy khóa cho $p$ nhỏ hơn.

### Đường cong FPR

<div class="figure">

![Đường cong xác suất dương giả theo k trên trục y tuyến tính, k từ 1 đến 10; với tám bit trên mỗi khóa, xác suất dương giả nhỏ nhất tại k bằng 6](img/lec-08/fpr-curve.svg)

</div>

Với $n/m=8$: $k^*=8\ln2\approx5{,}545$, nên so sánh hai số nguyên lân cận và chọn $k=6$. Giá trị dưới đây được tính lại từ công thức, không phải số liệu chép từ bài tập:

$$p_{FP}(6)\approx\left(1-e^{-6/8}\right)^6\approx0{,}02158.$$

Đường cong trên trục y tuyến tính có cực tiểu tại $k=6$, không phải đường thẳng; tăng thêm $k$ làm $p_{FP}$ tăng trở lại.

::: exercise Tự kiểm
Vì sao tăng từ $k=6$ lên $k=10$ có thể làm Bloom filter kém hơn khi $n/m=8$?
:::

::: solution
Mỗi khóa đặt thêm bit 1 nên mảng bão hòa nhanh hơn. Sau điểm cực tiểu, tác động này lớn hơn lợi ích của việc kiểm thêm vị trí.
:::

## 10. Chọn cấu trúc theo đầu ra

Ba cấu trúc trả lời ba loại câu hỏi khác nhau; không có cấu trúc đứng đầu chung, lựa chọn theo sản phẩm cần tính.

| Cấu trúc | Đơn vị | Bảo đảm | Sai số hoặc giới hạn |
|---|---|---|---|
| Lấy mẫu theo khóa | khóa | cùng khóa cùng quyết định | kích thước số bộ không cố định |
| Hồ chứa | vị trí | mỗi vị trí có xác suất $s/r$ | không giữ quan hệ theo khóa |
| Bloom filter | khóa thành viên | không âm giả dưới giả thiết đã nêu | có dương giả, không trả phần tử |

Áp dụng lại vào dòng truy vấn mở bài:

- Phân tích truy vấn lặp theo người dùng: băm khóa người dùng và giữ mọi bộ của khóa được chọn — dùng lấy mẫu theo khóa.
- Giữ đúng $s$ sự kiện để xem nhanh tiền tố: dùng hồ chứa, chấp nhận mất quan hệ khóa.
- Loại khóa chắc chắn không thuộc danh sách cho phép: dùng Bloom filter trước phép tra cứu chính xác.

Với hệ thống thật còn phải chọn tham số và đo trên phân bố dữ liệu; bài này cung cấp đặc tả và phân tích nguồn cho ba cơ chế.

## 11. Bốn bài tập từ giáo trình MMDS

Dưới đây là bốn bài tập giữ nguyên dữ kiện và yêu cầu của giáo trình *Mining of Massive Datasets* (Bài 4.2.1, 4.3.1, 4.3.2, 4.3.3). Lời giải và hướng dẫn chấm là của giảng viên suy ra từ đề, vì kho không có đáp án chính thức của sách.

::: exercise
**Bài tập 4.2.1 (tr.138).** Dòng có lược đồ `Grades(university, courseID, studentID, grade)`. Mỗi mã học phần và mã sinh viên chỉ duy nhất trong một trường; định danh `university` là duy nhất toàn cục. Với mẫu $1/20$, xác định khóa cho:

1. số sinh viên trung bình trong một học phần của mỗi trường;
2. tỷ lệ sinh viên có điểm trung bình từ 3,5;
3. tỷ lệ học phần có ít nhất nửa số sinh viên đạt A.

**Sản phẩm:** ba khóa, mỗi khóa kèm một câu giải thích.
:::

::: solution
**Lời giải.** Khóa theo đơn vị thống kê của mỗi câu hỏi:

1. Trung bình sinh viên trong một học phần của mỗi trường: đơn vị là học phần của mỗi trường, khóa `(university, courseID)`.
2. Tỷ lệ sinh viên có GPA từ 3,5: đơn vị là sinh viên của mỗi trường, khóa `(university, studentID)`.
3. Tỷ lệ học phần có ít nhất nửa sinh viên đạt A: đơn vị là học phần của mỗi trường, khóa `(university, courseID)`.

Hướng dẫn chấm: 2 điểm cho mỗi khóa đúng, 1 điểm cho mỗi giải thích, 1 điểm cho ký hiệu đồng nhất.
:::

::: exercise
**Bài tập 4.3.1 (tr.141).** Bloom filter có $n=8$ tỷ bit và tập $S$ gồm $m=1$ tỷ khóa. Tính xác suất dương giả khi dùng $k=3$ hàm băm là bao nhiêu? Khi dùng $k=4$ là bao nhiêu?

**Sản phẩm:** hai phép thế số và hai kết quả.
:::

::: solution
**Lời giải.** Dùng dạng xấp xỉ $p_k\approx(1-e^{-k/8})^k$.

- $k=3$: $p_3=(1-e^{-3/8})^3\approx0{,}030579$.
- $k=4$: $p_4=(1-e^{-1/2})^4\approx0{,}023969$.

Hướng dẫn chấm: 4 điểm cho mỗi phép thế và kết quả, 2 điểm cho ký hiệu và làm tròn nhất quán.
:::

::: exercise
**Bài tập 4.3.2 (tr.141).** Giả sử $k\mid n$. Chia $n$ bit thành $k$ mảng, mỗi mảng $n/k$ bit; mỗi khóa băm một lần vào từng mảng bằng các hàm đều, độc lập.

1. Tính xác suất dương giả theo $n,m,k$.
2. So sánh với $k$ hàm băm vào một mảng chung.

**Sản phẩm:** công thức theo $n$ hữu hạn, dạng xấp xỉ và kết luận.
:::

::: solution
**Lời giải.** Với mảng chia: mỗi mảng có $n/k$ bit và được $m$ khóa băm, xác suất một bit trong mảng con vẫn bằng 0 là $(1-k/n)^m$ (vì mỗi khóa băm một trong $n/k$ bit, tức xác suất trúng một bit là $k/n$). Xác suất dương giả mảng chia là

$$\left[1-\left(1-\frac{k}{n}\right)^m\right]^k.$$

Với mảng chung, $q^k=\left[1-(1-1/n)^{km}\right]^k$ là xấp xỉ chuẩn của FPR vì trạng thái các bit phụ thuộc và vị trí truy vấn có thể trùng. Khi $n$ lớn, cả hai dẫn đến $(1-e^{-km/n})^k$ trong xấp xỉ mũ.

Hướng dẫn chấm: 3 điểm cho xác suất bit 0 ở mảng con, 2 điểm cho FPR mảng chia, 2 điểm cho biểu thức mảng chung, 2 điểm cho so sánh hữu hạn/xấp xỉ, 1 điểm nêu giả thiết.
:::

::: exercise
**Bài tập 4.3.3 (tr.142).** Với $n$ bit và tập $S$ gồm $m$ phần tử, tìm số hàm băm tối thiểu hóa

$$p(k)=\left(1-e^{-km/n}\right)^k.$$

**Sản phẩm:** dẫn xuất và quy tắc chọn $k$.
:::

::: solution
**Lời giải.** Đặt $\rho=m/n$ và xét $\ell(k)=\ln p(k)=k\ln(1-e^{-k\rho})$ theo $k>0$. Đạo hàm:

$$\ell'(k)=\ln(1-e^{-k\rho})+\frac{k\rho}{e^{k\rho}-1}.$$

Đặt $x=k\rho$, $t=e^{-x}$. Dấu của $\ell'(k)$ bằng dấu của $(1-t)\ln(1-t)-t\ln t$, âm khi $t>1/2$, bằng 0 tại $t=1/2$, dương khi $t<1/2$. Vì $t$ giảm theo $k$, $\ell'(k)$ đổi dấu từ âm sang dương tại $k\rho=\ln2$. Vậy cực tiểu tại

$$k^*=\frac{n}{m}\ln2.$$

Với $k$ nguyên dương $k\ge1$, chọn bằng cách so sánh $\max(1,\lfloor k^*\rfloor)$ và $\max(1,\lceil k^*\rceil)$: lấy khóa cho $p$ nhỏ hơn.

Hướng dẫn chấm: 3 điểm lập log/đạo hàm, 3 điểm nghiệm, 2 điểm lập luận dấu, 2 điểm quy tắc số nguyên.
:::

> Không có bài hồ chứa trực tiếp trong phần bài tập của sách, nên phần này không thêm bài về hồ chứa.

## Tóm tắt nguồn

- Giáo trình: *Mining of Massive Datasets*, Chương 4, mục 4.1–4.3.
- Slide chính: MMDS, *Data Streams 1–2*; đối chiếu các bản PDF Stanford CS246 cục bộ cho phép đếm truy vấn và đường cong FPR, và cho ví dụ 11 bit.
- Bài tập: MMDS 4.2.1 và 4.3.1–4.3.3.

Ghi công theo yêu cầu của tác giả: <https://www.mmds.org>.
