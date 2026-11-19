# Bài 11 — Nén bằng từ điển và nén mất dữ liệu

Chúng ta xây hai họ bộ nén cho hai đặc tả khác nhau. Họ thứ nhất là nén bằng từ điển (dictionary-based compression) với ba thuật toán LZ77, LZ78 và LZW, dành cho dữ liệu phải khôi phục đúng từng byte và có các cụm ký tự lặp lại. Họ thứ hai là nén mất dữ liệu (lossy compression, còn gọi là nén mất thông tin) theo đường ống biến đổi cosine rời rạc (discrete cosine transform, DCT) của chuẩn JPEG (Joint Photographic Experts Group), dành cho ảnh chụp chỉ cần khôi phục gần đúng. Với mỗi bộ nén, chúng ta chứng minh bộ giải nén trả lại đúng hoặc gần đúng dữ liệu gốc và đếm chi phí theo cỡ cửa sổ, cỡ từ điển hay độ thô của phép lượng tử hóa.

[Bộ trang chiếu Bài 11](lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html) trình bày cùng chủ đề; [tệp bài tập Bài 11](material-viewer.html?doc=materials/lec-11/exercises.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html) chứa các bài tập củng cố.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Phân biệt đặc tả khôi phục đúng với đặc tả khôi phục gần đúng, tính tốc độ bit (bit rate) và sai số căn bình phương trung bình (root mean squared error, RMS), và chứng minh rằng một bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu (Mục 1).
2. Mã hóa và giải mã LZ77 bằng bộ ba khoảng lùi–độ dài–ký tự, kể cả khi vùng nguồn chồng lên vùng đích, chứng minh bộ giải mã khôi phục đúng và đếm chi phí theo cỡ cửa sổ và cỡ vùng nhìn trước (Mục 2).
3. Mã hóa và giải mã LZ78, dựng cây từ điển và chứng minh bằng quy nạp rằng hai phía giữ cùng từ điển (Mục 3).
4. Mã hóa và giải mã LZW, xử lý mã chưa có trong từ điển của bộ giải mã và chứng minh mã đó chỉ có thể bằng mã kế tiếp (Mục 4).
5. Tính DCT, lượng tử hóa, thứ tự zigzag và mã độ dài loạt trên một khối $8\times8$, chỉ ra bước làm mất dữ liệu và chặn sai số tái tạo theo bước lượng tử (Mục 5).
6. Chọn phương pháp nén cho một kho dữ liệu theo đặc tả khôi phục, dạng dư thừa của dữ liệu và chi phí bộ nhớ (Mục 6).

<!-- note-topic-id: lec-11-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `10.k` chỉ ghi chú Bài 10, `08.k` chỉ ghi chú Bài 08, `05.k` chỉ ghi chú Bài 05.

Trong các kết quả nhắc lại dưới đây, các chữ $u$, $r$, $j$, $I$, $P$, $H$, $X$, $Y$, $\theta$, $\omega$ là biến tạm theo ký hiệu của bài được dẫn, không mang nghĩa của bảng ký hiệu Bài 11.

- **Mã giải mã duy nhất** (Định nghĩa 10.1). Một mã ký hiệu gán cho mỗi ký hiệu một chuỗi bit gọi là từ mã; mã giải mã duy nhất khi phép nối các từ mã là đơn ánh, tức hai thông điệp khác nhau luôn cho hai dòng bit khác nhau.
- **Không mã nào rút ngắn mọi thông điệp** (Mệnh đề 10.2). Nếu $\varphi$ là đơn ánh từ tập chuỗi $n$ bit vào tập chuỗi bit thì có ít nhất một chuỗi $u$ với $\lvert\varphi(u)\rvert\ge n$, vì chỉ có $2^n-1$ chuỗi bit ngắn hơn $n$ bit.
- **Mô hình, bộ mã và cách dừng** (Định nghĩa 10.3, Nhận xét 10.4). Bộ nén là một cặp mô hình–bộ mã. Mô hình có bậc $j$ khi xác suất của ký hiệu tiếp theo chỉ phụ thuộc $j$ ký hiệu ngay trước nó; mô hình bậc 0 không nhìn ký hiệu nào. Hai phía phải dùng chung bảng chữ cái, quy tắc cập nhật mô hình, quy tắc mã và cách dừng, bằng ký hiệu kết thúc dòng `EOS` hoặc bằng độ dài truyền kèm.
- **Mã tiền tố** (Định nghĩa 10.5). Không từ mã nào là tiền tố của từ mã khác; mã tiền tố giải mã được từng ký hiệu khi đọc từ trái sang phải.
- **Entropy và mã Huffman** (Định nghĩa 10.11, Thuật toán 10.14, Định lý 10.18, Hệ quả 10.19). Với phân phối $P$, mã Huffman là mã tiền tố tối ưu và có độ dài trung bình $\bar\ell$ thỏa $H(P)\le\bar\ell<H(P)+1$ bit mỗi ký hiệu.
- **Mã số học** (Định lý 10.34). Mã số học lý tưởng dùng ít hơn $I(x)+2$ bit cho thông điệp $x$, với $I(x)$ là tự thông tin của $x$ theo mô hình.
- **Số bit của một bộ đếm** (Bài 08, Mục 1.4, sau Định nghĩa 08.3). Một đại lượng nhận các giá trị $0,1,\ldots,r$ cần $\lceil\log_2(r+1)\rceil$ bit.
- **Quy nạp và bất biến vòng lặp** (chứng minh Mệnh đề 05.19; CLRS, Chương 2). Bất biến vòng lặp (loop invariant) đúng trước lượt đầu, được giữ qua mỗi lượt và cho điều cần chứng minh khi vòng lặp dừng.
- **Bảng băm và cây** (CLRS, Chương 11; học phần Cấu trúc dữ liệu và giải thuật). Với giả thiết băm đều (uniform hashing) và hệ số tải (load factor) $\alpha$ là hằng, bảng băm (hash table) tra cứu và chèn trong thời gian kỳ vọng $O(1)$. Với địa chỉ mở (open addressing) và $\alpha<1$, một lần tìm không thành công cần kỳ vọng không quá $1/(1-\alpha)$ lần dò. Cây có gốc là cây mà mỗi nút trừ gốc có đúng một cha.
- **Ma trận trực chuẩn** (học phần Đại số tuyến tính). Ma trận vuông thực $X$ là trực chuẩn (orthonormal) khi $XX^{\top}=I$, tức các hàng có độ dài 1 và đôi một vuông góc; khi đó $X^{\top}X=I$ và $X^{-1}=X^{\top}$. Vết của ma trận thỏa $\operatorname{tr}(XY)=\operatorname{tr}(YX)$, và $\operatorname{tr}(XX^{\top})$ bằng tổng bình phương các phần tử của $X$.
- **Biến tích thành tổng** (toán phổ thông). $2\sin\theta\cos\omega=\sin(\omega+\theta)-\sin(\omega-\theta)$ và $2\cos\theta\cos\omega=\cos(\theta-\omega)+\cos(\theta+\omega)$.

## Bảng ký hiệu

Các ký hiệu dưới đây dùng xuyên suốt chương. Mỗi chữ trong bảng giữ nghĩa ghi trong bảng ở cả chương; ngoài ra $i$, $j$, $t$ còn làm chỉ số chạy trong tổng, trong đoạn $x[i..j]$ và trong các bước thuật toán. Chữ chỉ dùng trong một khối được giới thiệu tại chỗ và không trùng chữ trong bảng. Ma trận DCT viết $T$; Nelson và Gailly gọi ma trận này là $C$.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\Sigma$; $\lvert\Sigma\rvert$ | bảng chữ cái; số ký hiệu | tập hữu hạn; 256 với byte |
| $x=x_1\cdots x_n$; $n$ | chuỗi đầu vào; độ dài | $x_i\in\Sigma$ |
| $x[i..j]$ | đoạn $x_i\cdots x_j$; rỗng khi $i>j$ | chuỗi con |
| $\{0,1\}^*$; $\lvert\cdot\rvert$ | tập các chuỗi bit hữu hạn; độ dài của một chuỗi | |
| $m$; $m_{\mathrm h}$, $m_{\mathrm w}$ | số mẫu của dữ liệu; số hàng, số cột của ảnh, $m=m_{\mathrm h}m_{\mathrm w}$ | số nguyên dương |
| $\varphi$; $\psi$ | bộ nén; bộ giải nén | ánh xạ |
| $y$ | đầu ra của bộ giải nén | chuỗi hoặc ảnh |
| $p$ | số ký tự đã mã hóa (vị trí con trỏ) | $0\le p\le n$ |
| $W$; $L$ | cỡ cửa sổ (lịch sử); độ dài khớp tối đa (cỡ vùng nhìn trước) | số nguyên dương |
| $(d,\ell,c)$ | bộ ba LZ77: khoảng lùi, độ dài khớp, ký tự kế | $0\le d\le W$, $0\le\ell\le L$, $c\in\Sigma$ |
| $\tau$ | số đơn vị mã (bộ ba, cặp hoặc mã) mà bộ mã hóa phát | số nguyên không âm |
| $D$; $D[i]$ | từ điển; cụm mang mã $i$ | ánh xạ từ mã sang chuỗi |
| $(i,c)$ | cặp LZ78: mã cụm, ký tự mới | $i$ là mã có trong $D$ |
| $w$ | cụm hiện tại (mã hóa) hoặc cụm vừa xuất (giải mã) | chuỗi khác rỗng |
| $k$; $\texttt{next\_code}$ | mã LZW đọc vào; mã chưa cấp nhỏ nhất | số nguyên không âm |
| $\operatorname{first}(w)$ | ký tự đầu của $w$ | $\Sigma$ |
| $M$; $b$ | số mục tối đa của từ điển; số bit mỗi mã | $M=2^b$ khi mã rộng $b$ bit |
| $\alpha$ | hệ số tải của bảng băm | $0\le\alpha<1$ với địa chỉ mở |
| `EOS` | ký hiệu kết thúc dòng | ngoài $\Sigma$ |
| $P=(P_{\xi\eta})$; $A=(A_{\xi\eta})$ | khối điểm ảnh $8\times8$; khối sau dịch mức, $A_{\xi\eta}=P_{\xi\eta}-128$ | $P_{\xi\eta}\in\{0,\ldots,255\}$; hàng $\xi$, cột $\eta\in\{0,\ldots,7\}$ |
| $T=(T_{u\xi})$ | ma trận DCT | thực, $8\times8$, trực chuẩn |
| $F=(F_{uv})$ | hệ số DCT, $F=TAT^{\top}$; $F_{00}$ là hệ số DC | thực; $u,v\in\{0,\ldots,7\}$ |
| $Q=(Q_{uv})$; $q$ | ma trận lượng tử; hệ số chất lượng | số nguyên dương; $Q_{uv}=1+(1+u+v)q$ |
| $\hat F_{uv}$; $\tilde F_{uv}$ | số nguyên lượng tử; hệ số giải lượng tử $Q_{uv}\hat F_{uv}$ | $\mathbb Z$; $\mathbb Z$ |
| $\tilde A$; $\tilde P$ | khối tái tạo trước và sau khi cộng 128, làm tròn, cắt | thực; $\{0,\ldots,255\}$ |
| $\beta(q)$ | cận sai số RMS của một khối, $\tfrac12\sqrt{\tfrac1{64}\sum_{u,v}Q_{uv}^2}$ | mức xám |
| $K$; $\kappa$; $\delta_\kappa$ | số khối của ảnh; số thứ tự khối; sai phân DC của khối $\kappa$ | $K=m/64$; $1\le\kappa\le K$; $\mathbb Z$ |
| $(r,s,a)$ | bộ ba mã độ dài loạt: số các số 0 đứng trước, số bit, biên độ | $r,s\ge0$; $a\in\mathbb Z$ |
| $E_{\mathrm{RMS}}$; $R$ | sai số căn bình phương trung bình; tốc độ bit | mức xám; bit mỗi mẫu |

Các quy ước đọc sau dùng trong cả chương.

- Số thập phân dùng dấu phẩy, ví dụ $6{,}9$; số nguyên lớn nhóm ba chữ số bằng khoảng trắng hẹp, ví dụ $64\,000$.
- Chuỗi ký tự viết trong khối mã, ví dụ `aabaacabcabcb`; một ký tự đứng riêng viết chữ đứng, như $\mathrm a,\mathrm b,\mathrm c$, để không lẫn với ký tự $c$ của bộ ba; dấu cách viết `␣`.
- Ma trận và khối đánh chỉ số từ 0, hàng trước cột; ô $(u,v)$ là hàng $u$, cột $v$.
- Mã của một byte là chính giá trị byte đó: $\mathrm a\mapsto97$, $\mathrm b\mapsto98$, $\mathrm c\mapsto99$, dấu cách $\mapsto32$.
- Bộ nén $\varphi$ và bộ giải nén $\psi$ chỉ hai phía của một phương pháp nén nói chung. Với một thuật toán cụ thể như LZ77, LZ78, LZW, hai phía đó gọi là bộ mã hóa (encoder) và bộ giải mã (decoder).
- Viết tắt nguồn: NG là sách *The Data Compression Book*, ấn bản 2, của Nelson và Gailly. CMU là bài giảng *Algorithms in the Real World: Data Compression* của Blelloch cho học phần CMU 15-499; CMU-I, CMU-LZ, CMU-L là phần nhập môn, phần LZ và phần nén mất dữ liệu. CLRS là *Introduction to Algorithms*, ấn bản 4, của Cormen, Leiserson, Rivest và Stein.

## 1. Khôi phục đúng và khôi phục gần đúng

Bài 10 xây ba bộ nén khôi phục đúng từng bit. Mã Huffman dùng trung bình không quá một bit mỗi ký hiệu trên entropy của mô hình (Hệ quả 10.19), mã số học dùng ít hơn tự thông tin của thông điệp cộng 2 bit (Định lý 10.34), và không bộ nén nào rút ngắn được mọi thông điệp (Mệnh đề 10.2). Cả ba bộ nén vẫn mã từng ký hiệu theo một mô hình đếm.

Hai kho dữ liệu sau không vừa với cách làm đó. Kho thứ nhất là kho văn bản hay nhật ký, đọc một lượt, trong đó cả cụm ký tự lặp lại: cụm "Jacob Ziv" xuất hiện bốn, năm lần rải rác trong cuốn sách của NG, và trong một danh bạ điện thoại họ "Jones" lặp lại liên tiếp nhiều dòng (NG, tr.208). Một mã từng ký hiệu trả cho mỗi lần lặp của cụm số bit tỷ lệ với độ dài cụm.

Kho thứ hai là danh mục bán hàng trực tuyến gồm $1\,000$ ảnh màn hình VGA, mỗi ảnh $320\times200$ điểm, mỗi điểm 1 byte, tức $64\,000$ byte mỗi ảnh và 64 MB cả kho (NG, tr.246). Giả sử các ảnh là ảnh xám 8 bit, như các tệp `.GS` của NG (tr.265). Trên ảnh chụp, biểu đồ tần suất (histogram) điểm ảnh gần phẳng nên mã thống kê ít lợi, nhưng mắt người không nhận ra thay đổi nhỏ của một vài điểm ảnh (NG, tr.247).

Chúng ta cần biết thuật toán nào đạt từng đặc tả trong một lượt đọc với bộ nhớ hữu hạn, và đổi lại được bao nhiêu byte: kho văn bản phải khôi phục đúng từng byte, kho ảnh chỉ cần khôi phục gần đúng. Chúng ta xây ba bộ nén bằng từ điển cho kho thứ nhất và đường ống nén ảnh dựa trên biến đổi cosine rời rạc cho kho thứ hai, như sơ đồ sau.

![Sơ đồ cấu trúc chương: Mục 1, hai đặc tả khôi phục, tách hai nhánh. Nhánh khôi phục đúng y = x gồm Mục 2 (LZ77, cửa sổ W ký tự, bộ ba d, ℓ, c), Mục 3 (LZ78, từ điển cụm, cặp i, c) và Mục 4 (LZW, từ điển nạp sẵn, chỉ phát mã), khai thác cụm lặp đúng từng ký tự. Nhánh khôi phục gần đúng sai số RMS ≤ ε gồm Mục 5 (JPEG dựa trên DCT: dịch mức, DCT, lượng tử hóa, zigzag, mã độ dài loạt), khai thác giới hạn của mắt. Hai nhánh gặp nhau ở Mục 6, chọn phương pháp nén theo đặc tả, dạng dư thừa, bộ nhớ.](img/lec-11/note-cau-truc-chuong-11.svg)

Trên sơ đồ, nhánh trái là ba thuật toán nối tiếp nhau, mỗi thuật toán sửa một giới hạn của thuật toán trước nhưng cùng giữ yêu cầu $y=x$. Nhánh phải đổi chính yêu cầu đó thành "sai số RMS không quá $\varepsilon$", nên dùng một loại dư thừa khác của dữ liệu. Khối dưới cùng đặt các kết quả của hai nhánh cạnh nhau để chọn bộ nén cho một kho cụ thể.

<!-- note-topic-id: lec-11-topic-02 -->
### 1.1 Hai đặc tả khôi phục

Ảnh CHEETAH.GS của NG có $320\times200$ điểm ảnh xám 8 bit. Một bộ nén không mất thông tin cho ảnh, như các định dạng PCX, GIF hay BMP, tiết kiệm từ 10 tới 90 phần trăm dung lượng tùy ảnh (NG, tr.246). Với ảnh chụp, phần tiết kiệm nằm ở đầu thấp của khoảng đó vì hai lý do. Biểu đồ tần suất của các điểm ảnh gần phẳng, nên mỗi giá trị xám có xác suất xấp xỉ nhau, entropy gần 8 bit, và theo Hệ quả 10.19 mã Huffman gần như không rút ngắn được gì. Ngoài ra, trong mỗi chuỗi hai mươi điểm của một đường nét, một hai điểm lệch một mức xám so với hàng trước và hàng sau (NG, tr.247), nên các chuỗi điểm ảnh hiếm khi lặp lại đúng từng byte.

Về mặt ý tưởng, nếu thay yêu cầu "bản giải nén trùng bản gốc" bằng yêu cầu "bản giải nén gần bản gốc", bộ nén được phép ánh xạ nhiều ảnh khác nhau về cùng một dòng bit, miễn là mọi ảnh trong nhóm đó đều gần ảnh mà bộ giải nén trả lại. Để làm rõ đánh đổi giữa số byte và độ gần, xem số đo sau trên chính ảnh CHEETAH.GS.

::: example Ví dụ 11.1 (Ảnh CHEETAH.GS ở ba hệ số chất lượng)
**Dữ kiện.** Ảnh CHEETAH.GS gồm $m=320\cdot200=64\,000$ điểm ảnh, mỗi điểm 1 byte, tổng $64\,000$ byte. Chương trình nén DCT của NG có một tham số gọi là hệ số chất lượng (quality factor) $q$; hệ số càng lớn thì nén càng mạnh. Ba số đo của chương trình (NG, Hình 11.14, tr.287):

- $q=1$: còn $27\,809$ byte, sai số căn bình phương trung bình $4{,}3$ mức xám;
- $q=2$: còn $18\,367$ byte, sai số $6{,}9$ mức xám;
- $q=25$: còn $5\,094$ byte, sai số $17{,}4$ mức xám.

**Số bit mỗi điểm ảnh.** Mỗi byte là 8 bit, nên số bit mỗi điểm ảnh bằng 8 nhân số byte rồi chia cho $64\,000$:

- $q=1$: $8\cdot27\,809/64\,000\approx3{,}48$;
- $q=2$: $8\cdot18\,367/64\,000\approx2{,}30$;
- $q=25$: $8\cdot5\,094/64\,000\approx0{,}64$.

**Diễn giải.** Ảnh gốc dùng 8 bit mỗi điểm. Từ $q=1$ tới $q=25$, số byte giảm khoảng $27\,809/5\,094\approx5{,}5$ lần, còn sai số tăng khoảng $17{,}4/4{,}3\approx4$ lần. Không mức nào trả lại đúng ảnh gốc.

**Kiểm tra lại.** $3{,}48\cdot64\,000/8=27\,840\approx27\,809$ và $0{,}64\cdot64\,000/8=5\,120\approx5\,094$; sai lệch do làm tròn số bit mỗi điểm tới hai chữ số thập phân.
:::

Ví dụ 11.1 dùng hai đại lượng: số bit mỗi điểm ảnh đo độ nén, còn sai số căn bình phương trung bình đo độ lệch giữa ảnh tái tạo và ảnh gốc. Hai đại lượng đó và hai đặc tả được định nghĩa như sau.

::: definition Định nghĩa 11.1 (Bộ nén, hai đặc tả khôi phục, tốc độ bit, sai số RMS)
- Dữ liệu là một bộ $m$ mẫu $x=(x_1,\ldots,x_m)$ thuộc một tập hữu hạn $\mathcal X$, ví dụ $m$ điểm ảnh với $x_i\in\{0,\ldots,255\}$, hay một chuỗi ký tự trên $\Sigma$, khi đó $m=n$. Một **bộ nén** là ánh xạ $\varphi:\mathcal X\to\{0,1\}^*$; một **bộ giải nén** là ánh xạ $\psi:\{0,1\}^*\to\mathcal X$; $y=\psi(\varphi(x))$ là dữ liệu tái tạo.
- **Tốc độ bit** (bit rate) của $\varphi$ trên $x$ là $R(x)=\lvert\varphi(x)\rvert/m$ bit mỗi mẫu; với ảnh, đơn vị là bit mỗi điểm ảnh (bits per pixel, bpp).
- **Sai số căn bình phương trung bình** (root mean squared error, RMS) giữa $x$ và $y$ là
$$
E_{\mathrm{RMS}}(x,y)=\sqrt{\frac1m\sum_{i=1}^{m}(x_i-y_i)^2}.
$$
- Cặp $(\varphi,\psi)$ thỏa **đặc tả khôi phục đúng** khi $\psi(\varphi(x))=x$ với mọi $x\in\mathcal X$. Nén theo đặc tả này gọi là nén không mất thông tin (lossless compression).
- Với ngưỡng $\varepsilon\ge0$, cặp $(\varphi,\psi)$ thỏa **đặc tả khôi phục gần đúng** (approximate reconstruction) khi $E_{\mathrm{RMS}}(x,\psi(\varphi(x)))\le\varepsilon$ với mọi $x\in\mathcal X$. Nén theo đặc tả này, với $\varepsilon>0$, gọi là nén mất dữ liệu.
:::

Ba thành phần của định nghĩa có vai trò riêng:

- tốc độ bit đo cái được: ở Ví dụ 11.1, $R$ giảm từ 8 xuống $3{,}48$, $2{,}30$ rồi $0{,}64$ bit mỗi điểm;
- sai số RMS đo cái mất, tính bằng mức xám như chính điểm ảnh;
- đặc tả cho biết bộ giải nén phải trả lại cái gì.

Vì $E_{\mathrm{RMS}}(x,y)=0$ khi và chỉ khi $x_i=y_i$ với mọi $i$, đặc tả khôi phục đúng là trường hợp $\varepsilon=0$ của đặc tả khôi phục gần đúng. Đặc tả của Bài 10 là trường hợp riêng của đặc tả khôi phục đúng: khi $\varphi$ là phép nối từ mã của một mã giải mã duy nhất (Định nghĩa 10.1), $\psi$ là ánh xạ ngược của $\varphi$ trên ảnh của nó; với mã tiền tố, đó là phép giải mã từng ký hiệu.

![Hai hàng. Hàng trên, khôi phục đúng: văn bản x qua bộ nén φ thành dòng bit, R bit mỗi mẫu, qua bộ giải nén ψ thành y, với điều kiện y = x với mọi x; chú thích: nhiều x khác nhau không bao giờ chung một dòng bit. Hàng dưới, khôi phục gần đúng: khối ảnh P qua φ và ψ thành P̃, với điều kiện sai số RMS giữa P và P̃ không quá ε; chú thích: nhiều khối được phép chung một dòng bit.](img/lec-11/note-hai-dac-ta.svg)

Hai hàng của hình có cùng hai mũi tên $\varphi$ và $\psi$, chỉ khác điều kiện ở khung bên phải. Ở hàng trên, $\varphi$ phải là đơn ánh; ở hàng dưới, $\varphi$ được gộp nhiều khối vào một dòng bit, và đó là chỗ tốc độ bit giảm được.

Một nhầm lẫn thường gặp là coi hai ảnh tái tạo có cùng sai số RMS là giống nhau về mắt. Giả sử một khối $8\times8$ được tái tạo theo hai cách. Cách thứ nhất làm mọi điểm lệch 2 mức xám, nên $E_{\mathrm{RMS}}=\sqrt{64\cdot4/64}=2$. Cách thứ hai giữ đúng 60 điểm và làm 4 điểm lệch 8 mức, nên $E_{\mathrm{RMS}}=\sqrt{4\cdot64/64}=2$. Hai cách cùng sai số, nhưng cách thứ hai tạo một đốm nhìn thấy được. NG dùng RMS để so sánh các mức nén, nhưng coi đánh giá bằng mắt là một thước đo riêng mà RMS không thay được (NG, tr.259, 266).

Ở cả ba mức của Ví dụ 11.1, bộ nén của NG đều làm sai lệch ảnh. Mọi bộ nén rút ngắn mọi ảnh đều làm sai lệch một số ảnh.

::: proposition Mệnh đề 11.2 (Bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu)
**Giả thiết.** $m\ge1$; $\mathcal X=\{0,\ldots,255\}^m$ là tập mọi ảnh $m$ điểm 8 bit; $\varphi:\mathcal X\to\{0,1\}^*$ thỏa $\lvert\varphi(x)\rvert<8m$ với mọi $x\in\mathcal X$.

**Kết luận.** Với mọi bộ giải nén $\psi$, có ảnh $x\in\mathcal X$ với $\psi(\varphi(x))\ne x$.

**Điều kiện áp dụng.** Giả thiết đòi $\lvert\varphi(x)\rvert<8m$ với mọi ảnh $x$; không cần giả thiết gì về cách tính $\varphi$ hay $\psi$.

**Phạm vi.** Mệnh đề nói về khôi phục đúng; nó không cho biết sai số nhỏ nhất đạt được ở một tốc độ bit cho trước.
:::

::: proof
**Bước 1 (có $2^{8m}$ ảnh nhưng chỉ $2^{8m}-1$ chuỗi ngắn hơn).** Mỗi ảnh là một chuỗi $8m$ bit, nên $\lvert\mathcal X\rvert=2^{8m}$. Số chuỗi bit có độ dài nhỏ hơn $8m$, kể cả chuỗi rỗng, là $\sum_{j=0}^{8m-1}2^j=2^{8m}-1$.

**Bước 2 ($\varphi$ không đơn ánh).** Theo giả thiết, $\varphi$ ánh xạ tập $2^{8m}$ phần tử vào tập $2^{8m}-1$ phần tử, nên $\varphi$ không là đơn ánh: có hai ảnh $x\ne x'$ với $\varphi(x)=\varphi(x')$. Đây chính là Mệnh đề 10.2 với $n=8m$.

**Bước 3 (một trong hai ảnh bị tái tạo sai).** $\psi(\varphi(x))=\psi(\varphi(x'))$ là một ảnh duy nhất, nên nó khác ít nhất một trong hai ảnh $x$, $x'$. $\square$
:::

Mệnh đề nói rằng muốn mọi ảnh đều ngắn đi thì phải chấp nhận sai lệch trên một số ảnh. Giả thiết "mọi ảnh" là cần: một bộ nén khôi phục đúng vẫn rút ngắn được những ảnh mà mô hình của nó coi là dễ xảy ra, chẳng hạn Huffman trên ảnh có biểu đồ tần suất lệch, nhưng theo Mệnh đề 10.2 nó không rút ngắn được mọi ảnh. Trong chứng minh, giả thiết đó được dùng duy nhất ở Bước 2. Đặc tả khôi phục gần đúng chấp nhận chính hệ quả của Bước 3: nhiều ảnh dùng chung một dòng bit và nhận cùng một ảnh tái tạo.

::: remark Nhận xét 11.3 (Trong thực hành)
- Chương trình nén ảnh của NG ghi hệ số chất lượng $q$ vào đầu tệp nén, để bộ giải nén dùng đúng các số chia mà bộ nén đã dùng; giải nén với các số chia khác cho ảnh sai hoàn toàn (NG, tr.266). Đây là thành phần "quy tắc mã" của giao thức trong Nhận xét 10.4.
- Ảnh trong máy tính thường được quét từ ảnh in, nên đã là một bản xấp xỉ của ảnh thật; NG suy ra rằng một bộ nén chỉ làm lệch vài mức xám ở rải rác vài điểm vẫn giữ được nội dung mà người xem nhận ra (NG, tr.247).
- Văn bản, mã nguồn và tệp thực thi phải khôi phục đúng từng byte: một byte sai trong tệp thực thi có thể làm chương trình chạy sai. Với các dữ liệu này, đặc tả khôi phục gần đúng không áp dụng.
:::

::: exercise Bài tập 11.1 (Đọc bảng kết quả nén và tính sai số)
Hai ảnh xám CHEETAH.GS và CLOWN.GS, mỗi ảnh $64\,000$ byte, được nén bằng chương trình DCT của NG ở năm hệ số chất lượng (NG, Hình 11.14, tr.287):

| $q$ | CHEETAH.GS: byte | CHEETAH.GS: RMS | CLOWN.GS: byte | CLOWN.GS: RMS |
|---:|---:|---:|---:|---:|
| 1 | $27\,809$ | $4{,}3$ | $20\,835$ | $3{,}7$ |
| 2 | $18\,367$ | $6{,}9$ | $14\,243$ | $5{,}6$ |
| 5 | $10\,232$ | $10{,}9$ | $8\,636$ | $8{,}6$ |
| 10 | $7\,167$ | $13{,}6$ | $6\,355$ | $10{,}9$ |
| 25 | $5\,094$ | $17{,}4$ | $4\,811$ | $14{,}1$ |

(a) Tính tốc độ bit, theo bit mỗi điểm ảnh, của hai ảnh ở mỗi hệ số. (b) Với yêu cầu $E_{\mathrm{RMS}}\le10$, chọn trong năm hệ số trên hệ số lớn nhất cho mỗi ảnh và so số byte của hai ảnh. (c) Xác định hệ số chung lớn nhất trong năm hệ số trên để cả hai ảnh cùng đạt $E_{\mathrm{RMS}}\le10$, và tính số byte phải trả thêm so với chọn hệ số riêng cho từng ảnh như câu (b). (d) Hàng đầu của một khối ảnh xám là 140, 144, 147, 140, 140, 155, 179, 175; hàng tương ứng của khối tái tạo là 142, 143, 155, 141, 133, 154, 179, 179. Tính $E_{\mathrm{RMS}}$ trên tám điểm này. (e) Với $m=1$, đếm số ảnh một điểm 8 bit và số chuỗi bit ngắn hơn 8 bit, rồi giải thích theo Mệnh đề 11.2 vì sao một bộ nén rút ngắn mọi ảnh một điểm phải gán cùng dòng bit cho hai ảnh khác nhau.
:::

::: hint
Tốc độ bit bằng 8 nhân số byte rồi chia cho $64\,000$. Ở câu (b) và (c), đọc cột RMS từ trên xuống và dừng ở dòng cuối cùng còn không quá 10.
:::

::: solution
**Câu (a).** Với CHEETAH.GS: $3{,}48$; $2{,}30$; $1{,}28$; $0{,}90$; $0{,}64$ bit mỗi điểm. Với CLOWN.GS: $8\cdot20\,835/64\,000\approx2{,}60$; $1{,}78$; $1{,}08$; $0{,}79$; $0{,}60$ bit mỗi điểm.

**Câu (b).** CHEETAH.GS có RMS $6{,}9\le10$ ở $q=2$ và $10{,}9>10$ ở $q=5$, nên chọn $q=2$ với $18\,367$ byte. CLOWN.GS có RMS $8{,}6\le10$ ở $q=5$ và $10{,}9>10$ ở $q=10$, nên chọn $q=5$ với $8\,636$ byte. Cùng ngưỡng sai số, CLOWN.GS chỉ cần khoảng $8\,636/18\,367\approx47\%$ số byte của CHEETAH.GS.

**Câu (c).** Hệ số chung phải đạt ngưỡng trên cả hai ảnh, nên không lớn hơn hệ số riêng của ảnh khó hơn: $q=2$. Khi đó hai ảnh tốn $18\,367+14\,243=32\,610$ byte, so với $18\,367+8\,636=27\,003$ byte khi chọn riêng, tức trả thêm $5\,607$ byte, khoảng $21\%$, tất cả ở ảnh CLOWN.GS.

**Câu (d).** Hiệu từng điểm là −2, 1, −8, −1, 7, 1, 0, −4, tổng bình phương $4+1+64+1+49+1+0+16=136$, nên $E_{\mathrm{RMS}}=\sqrt{136/8}=\sqrt{17}\approx4{,}12$ mức xám.

**Câu (e).** Có $2^8=256$ ảnh một điểm nhưng chỉ $2^8-1=255$ chuỗi bit ngắn hơn 8 bit. Theo Bước 2 của chứng minh Mệnh đề 11.2, hai ảnh khác nhau nhận cùng một dòng bit, và bộ giải nén trả cùng một ảnh cho cả hai.

**Kiểm tra lại.** Ở mỗi ảnh, số byte giảm và RMS tăng khi $q$ tăng, nên "hệ số lớn nhất còn đạt ngưỡng" là dòng cuối cùng thỏa $E_{\mathrm{RMS}}\le10$; $5\,607/27\,003\approx0{,}208$.
:::

<!-- note-topic-id: lec-11-topic-03 -->
### 1.2 Giới hạn của nén khôi phục đúng

Với văn bản, đặc tả khôi phục gần đúng không dùng được. Theo Mệnh đề 10.2, một bộ nén khôi phục đúng không rút ngắn được mọi đầu vào; nó chỉ có lợi trên những đầu vào có dư thừa mà mô hình của nó nhận ra. Các mô hình của Bài 10 nhận ra dư thừa ở tần suất ký hiệu, có thể theo vài ký hiệu đứng trước. Văn bản còn một dạng dư thừa khác: cả cụm ký tự lặp lại. Trong chuỗi mười lăm ký tự `aacaacabcabaaac`, cụm `aac` ở vị trí 1–3 lặp lại ngay ở vị trí 4–6. Một mô hình bậc 0 gán cho chữ $\mathrm a$ ở vị trí 4 cùng xác suất như ở vị trí 1, nên mã Huffman trả cho lần lặp thứ hai của `aac` cùng số bit như lần đầu.

Như vậy, chúng ta đã có hai đặc tả khôi phục cùng hai thước đo tốc độ bit và sai số RMS (Định nghĩa 11.1), và biết rằng muốn rút ngắn mọi đầu vào thì phải chấp nhận sai lệch (Mệnh đề 11.2). Với dữ liệu phải khôi phục đúng, phần còn khai thác được là các cụm lặp, mà một mã từng ký hiệu trả số bit tỷ lệ với độ dài cụm ở mỗi lần lặp. Để mã một lần lặp bằng một số bit gần như không phụ thuộc độ dài cụm, bộ nén cần trỏ ngược tới lần xuất hiện trước của cụm đó.

## 2. Nén bằng cửa sổ trượt LZ77

Bộ mã hóa đọc chuỗi `aacaacabcabaaac`, $n=15$ ký tự trên bảng chữ cái $\{\mathrm a,\mathrm b,\mathrm c\}$, một lượt và chỉ giữ được trong bộ nhớ một đoạn hữu hạn của phần đã đọc. Trong cài đặt của NG, đoạn đó dài vài nghìn ký tự, còn phần đã đọc nhưng chưa mã hóa dài từ mười tới một trăm ký tự (NG, tr.174). Bài toán là mã mỗi lần lặp của một cụm bằng một số bit cố định, chỉ dùng đoạn được giữ, sao cho bộ giải mã dựng lại đúng chuỗi mà không cần thêm thông tin nào khác.

<!-- note-topic-id: lec-11-topic-04 -->
### 2.1 Cửa sổ, vùng nhìn trước và bộ ba

Thuật toán LZ77, do Ziv và Lempel công bố năm 1977, dùng chính phần văn bản vừa đọc làm từ điển: nó thay một cụm (phrase) có độ dài thay đổi bằng một con trỏ có cỡ cố định (NG, tr.174). Về mặt ý tưởng, mỗi bộ ba là một lệnh cho bộ giải mã: lùi lại $d$ ký tự, chép $\ell$ ký tự, rồi viết thêm ký tự $c$. Để làm rõ cách chọn $d$, $\ell$ và $c$, xem ba bước đầu trên chuỗi `aacaacabcabaaac`.

::: example Ví dụ 11.2 (Ba bộ ba đầu của chuỗi aacaacabcabaaac)
**Dữ kiện.** Chuỗi $x=$ `aacaacabcabaaac`, $n=15$. Bộ mã hóa giữ tối đa $W=6$ ký tự đã mã hóa gần nhất và so khớp tối đa $L=4$ ký tự (CMU-LZ, trang chiếu 5). Con trỏ (cursor) $p$ là số ký tự đã mã hóa, ban đầu $p=0$.

**Bước 1, $p=0$.** Chưa có ký tự nào đã mã hóa, nên không có cụm để chép. Bộ mã hóa phát $(0,0,\mathrm a)$: lùi 0, chép 0 ký tự, viết $x_1=\mathrm a$. Con trỏ lên $p=1$.

**Bước 2, $p=1$.** Phần đã mã hóa là $x[1..1]=$ `a`, phần chờ mã hóa bắt đầu bằng $x[2..5]=$ `acaa`. Chỉ có khoảng lùi $d=1$. So $x_2=\mathrm a$ với $x_1=\mathrm a$: khớp. So $x_3=\mathrm c$ với $x_2=\mathrm a$: không khớp. Vậy $\ell=1$, ký tự kế là $x_3=\mathrm c$, và bộ mã hóa phát $(1,1,\mathrm c)$. Con trỏ lên $p=1+1+1=3$.

**Bước 3, $p=3$.** Phần đã mã hóa là $x[1..3]=$ `aac`, bốn ký tự chờ là $x[4..7]=$ `aaca`. Thử ba khoảng lùi:

- $d=1$: $x_4=\mathrm a$ so với $x_3=\mathrm c$, không khớp, $\ell=0$;
- $d=2$: $x_4=\mathrm a$ khớp $x_2=\mathrm a$, rồi $x_5=\mathrm a$ so với $x_3=\mathrm c$, không khớp, $\ell=1$;
- $d=3$: $x_4,x_5,x_6,x_7=\mathrm a,\mathrm a,\mathrm c,\mathrm a$ lần lượt khớp $x_1,x_2,x_3,x_4=\mathrm a,\mathrm a,\mathrm c,\mathrm a$, $\ell=4=L$.

Khoảng lùi $d=3$ cho độ khớp dài nhất. Ký tự kế là $x_8=\mathrm b$, và bộ mã hóa phát $(3,4,\mathrm b)$. Con trỏ lên $p=3+4+1=8$.

**Kết quả.** Ba bộ ba $(0,0,\mathrm a)$, $(1,1,\mathrm c)$, $(3,4,\mathrm b)$ mô tả tám ký tự đầu `aacaacab`.

**Kiểm tra lại.** Ba bộ ba phủ $1+2+5=8$ ký tự, đúng bằng $p=8$. Ở bước 3, lần so cuối cùng đặt $x_7$ cạnh $x_4$: ký tự nguồn $x_4$ nằm ngay trong đoạn đang được mã hóa.
:::

![Chuỗi aacaacabcabaaac, mười lăm ô đánh số 1 đến 15, con trỏ p = 3 đứng sau ô 3. Ô 1–3 (aac) là lịch sử, W = 6 nhưng mới có 3 ký tự; ô 4–7 (aaca) là vùng nhìn trước L = 4, viền nét đứt; ô 8 (b) là ký tự kế. Mũi tên cong từ ô 4 lùi về ô 1 ghi lùi d = 3. Khung: bộ ba (d, ℓ, c) = (3, 4, b), vì x[4..7] = x[1..4] = aaca và x[8] = b.](img/lec-11/note-lz77-cua-so.svg)

Trên hình là trạng thái ở bước 3. Đoạn viền liền bên trái con trỏ là phần đã mã hóa mà bộ mã hóa còn giữ; đoạn viền nét đứt bên phải là các ký tự được phép so khớp. Mũi tên cong chỉ khoảng lùi $d=3$: ô 4 được so với ô 1, ô 5 với ô 2, và tiếp tục như vậy, nên ô 7 được so với ô 4, một ô nằm bên phải con trỏ. Ký tự kế $\mathrm b$ nằm ngoài bốn ô so khớp; $L$ giới hạn độ dài khớp chứ không giới hạn vị trí của ký tự kế.

::: definition Định nghĩa 11.4 (Cửa sổ, vùng nhìn trước và bộ ba LZ77)
Cho chuỗi $x=x_1\cdots x_n$ trên $\Sigma$, cỡ cửa sổ $W\ge1$, độ dài khớp tối đa $L\ge1$ và con trỏ $p$ với $0\le p<n$.

- **Cửa sổ trượt** (sliding window) tại $p$ gồm **lịch sử** (search buffer) $x[\max(1,p-W+1)..p]$, tức tối đa $W$ ký tự đã mã hóa gần nhất, và **vùng nhìn trước** (look-ahead buffer) $x[p+1..\min(p+L,n)]$.
- Một **bộ ba** (token) tại $p$ là $(d,\ell,c)$ với **khoảng lùi** (distance) $d$, **độ dài khớp** (match length) $\ell$ và **ký tự kế** $c$, thỏa:
  - $0\le\ell\le L$ và $p+\ell+1\le n$;
  - nếu $\ell=0$ thì $d=0$; nếu $\ell\ge1$ thì $1\le d\le\min(W,p)$ và $x_{p+j}=x_{p+j-d}$ với $j=1,\ldots,\ell$;
  - $c=x_{p+\ell+1}$.
- Bộ ba mô tả đoạn $x[p+1..p+\ell+1]$; sau bộ ba, con trỏ lên $p+\ell+1$.
:::

Khoảng lùi $d$ đếm từ con trỏ về bên trái; CMU gọi nó là vị trí của cụm khớp dài nhất tính tương đối với con trỏ (position relative to the cursor) (CMU-LZ, trang chiếu 4). NG ghi thay cho $d$ chỉ số của cụm trong bộ đệm cửa sổ và gọi chỉ số đó là offset (NG, tr.175); hai cách ghi chứa cùng thông tin khi hai phía biết vị trí con trỏ trong bộ đệm. Theo Định nghĩa 11.4, vùng nhìn trước không chứa ký tự kế, nên một bộ đệm nhìn trước $L+1$ ký tự như của NG ứng với độ dài khớp tối đa $L$.

Điều kiện $d\le p$ bảo đảm vị trí nguồn đầu tiên $p+1-d$ không nhỏ hơn 1. Ví dụ, bộ ba $(3,4,\mathrm b)$ hợp lệ tại $p=3$ nhưng không hợp lệ tại $p=2$, vì khi đó vị trí nguồn đầu tiên là $x_0$, không tồn tại. Định nghĩa không đòi $\ell\le d$: ở Ví dụ 11.2, bộ ba $(3,4,\mathrm b)$ có $\ell=4>d=3$, nên đoạn nguồn $x[1..4]$ chồng lên đoạn đích $x[4..7]$ ở ô 4. Điều kiện $p+\ell+1\le n$ bảo đảm bộ ba cuối cùng vẫn có một ký tự kế thật, nên dòng bộ ba không cần ký hiệu `EOS`.

Ba bước của Ví dụ 11.2 lặp lại cùng một phép: thử mọi khoảng lùi, giữ khoảng lùi cho độ khớp dài nhất, phát bộ ba và tiến con trỏ. Khi hai khoảng lùi cho cùng độ khớp dài nhất, hai phía không cần thống nhất cách chọn, vì bộ giải mã chỉ đọc $d$ đã phát; thuật toán dưới đây chọn $d$ nhỏ nhất.

::: algorithm Thuật toán 11.5 (Mã hóa LZ77 tham lam)
**Đầu vào.** Chuỗi $x=x_1\cdots x_n$ trên $\Sigma$; cỡ cửa sổ $W\ge1$; cỡ vùng nhìn trước $L\ge1$.

**Đầu ra.** Dãy bộ ba $(d_1,\ell_1,c_1),\ldots,(d_\tau,\ell_\tau,c_\tau)$ theo Định nghĩa 11.4.

**Giả thiết.** Hai phía dùng chung $W$; dòng bộ ba được đóng khung, tức bộ giải mã biết khi nào hết bộ ba (Nhận xét 10.4).

**Các bước.**

1. Đặt $p\leftarrow0$.
2. Trong khi $p<n$, lặp:
   1. Với mỗi $d=1,\ldots,\min(W,p)$, tính $\ell(d)$ là số $j$ lớn nhất trong $\{0,\ldots,\min(L,n-p-1)\}$ sao cho $x_{p+i}=x_{p+i-d}$ với mọi $i=1,\ldots,j$, bằng cách so lần lượt $i=1,2,\ldots$ tới lần đầu không khớp.
   2. Đặt $\ell\leftarrow\max_d\ell(d)$, hoặc $\ell\leftarrow0$ khi $p=0$. Nếu $\ell\ge1$, đặt $d$ là khoảng lùi nhỏ nhất có $\ell(d)=\ell$; nếu $\ell=0$, đặt $d\leftarrow0$.
   3. Phát bộ ba $(d,\ell,x_{p+\ell+1})$.
   4. Đặt $p\leftarrow p+\ell+1$.

**Dừng.** Mỗi lượt tăng $p$ ít nhất 1 và giữ $p\le n$ vì $\ell\le n-p-1$; vòng lặp dừng khi $p=n$, sau không quá $n$ lượt.

**Trường hợp biên.** Với $n=0$, dòng bộ ba rỗng. Với $p=0$, không có khoảng lùi nào và bộ ba là $(0,0,x_1)$. Gần cuối chuỗi, cận $\min(L,n-p-1)$ chừa lại ký tự kế. Độ khớp được phép vượt $d$ (sao chép chồng lấn).

**Chi phí.** Mô hình: đếm phép so sánh hai ký tự, trường hợp xấu nhất; $\tau\le n$ là số bộ ba.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2.1, so khớp mọi khoảng lùi | $\tau$ lượt | tối đa $\min(W,p)\cdot(L+1)$ phép so | $O(\tau WL)$ |
| 2.2, chọn $\ell$ và $d$ | $\tau$ | $O(W)$ | $O(\tau W)$ |
| 2.3–2.4, phát bộ ba, tiến con trỏ | $\tau$ | $O(1)$ | $O(\tau)$ |
:::

Thuật toán đúng theo bất biến sau: trước mỗi lượt, các bộ ba đã phát mô tả nối tiếp nhau đúng đoạn $x[1..p]$.

- Khởi tạo: với $p=0$, dãy rỗng mô tả đoạn rỗng.
- Duy trì: một lượt chọn $\ell(d)$ thỏa điều kiện khớp của Định nghĩa 11.4, $d\le\min(W,p)$ và $c=x_{p+\ell+1}$, nên bộ ba mới hợp lệ và mô tả đúng $x[p+1..p+\ell+1]$; sau bước 2.4, bất biến đúng với $p$ mới.
- Kết thúc: khi vòng lặp dừng, $p=n$ và dãy bộ ba mô tả cả $x$.

Bước 2.1 là phép quyết định của thuật toán và cũng là phần tốn kém: bộ mã hóa so vùng nhìn trước với mọi vị trí của cửa sổ (NG, tr.178). Thuật toán là tham lam (greedy): mỗi lượt lấy cụm khớp dài nhất mà không xét các lượt sau.

<!-- note-topic-id: lec-11-topic-05 -->
### 2.2 Giải mã và sao chép chồng lấn

Bộ giải mã không so khớp gì: nó đọc một bộ ba, chép cụm được chỉ, viết ký tự kế, rồi đọc bộ ba tiếp theo (NG, tr.176). Việc chép cần cẩn thận khi $\ell>d$, vì một phần cụm nguồn chưa có trong bản giải mã lúc bắt đầu chép; trường hợp này gọi là sao chép chồng lấn (overlapping copy).

::: example Ví dụ 11.3 (Giải mã bộ ba $(3,4,\mathrm b)$ sau aac)
**Dữ kiện.** Bản giải mã hiện có $y=y_1y_2y_3=$ `aac`, tức $p=3$. Bộ ba kế tiếp là $(d,\ell,c)=(3,4,\mathrm b)$ (Ví dụ 11.2).

**Chép từng ký tự.** Với $j=1,\ldots,4$, gán $y_{3+j}\leftarrow y_{3+j-3}=y_j$:

- $j=1$: $y_4\leftarrow y_1=\mathrm a$, được `aaca`;
- $j=2$: $y_5\leftarrow y_2=\mathrm a$, được `aacaa`;
- $j=3$: $y_6\leftarrow y_3=\mathrm c$, được `aacaac`;
- $j=4$: $y_7\leftarrow y_4=\mathrm a$, được `aacaaca`; ô nguồn $y_4$ vừa được ghi ở $j=1$.

**Ghi ký tự kế.** $y_8\leftarrow\mathrm b$, được `aacaacab`.

**Kiểm tra lại.** `aacaacab` $=x[1..8]$ của Ví dụ 11.2, và bản giải mã dài $3+4+1=8$ ký tự.
:::

![Sáu hàng mô tả giải mã (3, 4, b) khi bản giải mã là aac: j = 1, y4 ← y1 được aaca; j = 2, y5 ← y2 được aacaa; j = 3, y6 ← y3 được aacaac; j = 4, y7 ← y4 được aacaaca, ô nguồn y4 viền nét đứt với chú thích nguồn y4 vừa được ghi ở j = 1; cuối cùng ghi y8 ← b được aacaacab. Mỗi hàng có ô nguồn viền xanh, ô đích viền cam và mũi tên từ nguồn tới đích.](img/lec-11/note-lz77-chep-chong-lan.svg)

Trên hình, mỗi hàng chép đúng một ký tự, và mũi tên luôn đi từ một ô đã có sang ô ngay sau phần đã có. Ở hàng $j=4$, ô nguồn $y_4$ không tồn tại lúc bộ giải mã đọc bộ ba nhưng đã được ghi ở hàng $j=1$. NG gặp cùng hiện tượng với một trăm chữ A liên tiếp: chữ A đầu tiên được mã bằng $(0,0,\mathrm A)$, rồi một bộ ba duy nhất mã mười ký tự tiếp theo, trong khi "từ điển" mới chứa một ký tự (NG, tr.176–177).

::: algorithm Thuật toán 11.6 (Giải mã LZ77)
**Đầu vào.** Dãy bộ ba $(d_1,\ell_1,c_1),\ldots,(d_\tau,\ell_\tau,c_\tau)$.

**Đầu ra.** Chuỗi $y$.

**Giả thiết.** Dòng bộ ba được đóng khung và không bị hỏng trên đường truyền.

**Các bước.**

1. Đặt $y$ là chuỗi rỗng và $p\leftarrow0$.
2. Với mỗi $t=1,\ldots,\tau$:
   1. Nếu $\ell_t\ge1$ và $d_t>p$, báo dòng hỏng và dừng. Ngược lại, với $j=1,\ldots,\ell_t$, theo thứ tự tăng của $j$, gán $y_{p+j}\leftarrow y_{p+j-d_t}$.
   2. Gán $y_{p+\ell_t+1}\leftarrow c_t$.
   3. Đặt $p\leftarrow p+\ell_t+1$.
3. Trả về $y=y_1\cdots y_p$.

**Dừng.** Sau đúng $\tau$ lượt của bước 2, hoặc khi gặp bộ ba hỏng.

**Trường hợp biên.** Dòng rỗng cho $y$ rỗng. Bộ ba có $\ell_t=0$ chỉ ghi $c_t$ và bỏ qua $d_t$. Khi $\ell_t>d_t$, các vị trí nguồn $p+j-d_t$ với $j>d_t$ là các ô vừa ghi ở cùng lượt. Bộ ba có $\ell_t\ge1$ mà $d_t>p$ trỏ ra trước đầu chuỗi, và bước 2.1 dừng.

**Chi phí.** Mô hình: đếm phép ghi một ký tự.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2.1, chép | $\ell_t$ ở lượt $t$ | $O(1)$ | $O(\sum_t\ell_t)$ |
| 2.2–2.3, ghi $c_t$, tiến con trỏ | $\tau$ | $O(1)$ | $O(\tau)$ |
:::

Thuật toán chỉ chép, không tìm kiếm: theo bảng chi phí, nó tốn $\sum_t(\ell_t+1)$ phép ghi, còn bộ mã hóa tốn tới $\tau W(L+1)$ phép so (Thuật toán 11.5). Thời gian giải mã hầu như không đổi khi cửa sổ hay vùng nhìn trước lớn lên (NG, tr.178). Điều kiện duy nhất cần giữ là thứ tự chép tăng dần của $j$ ở bước 2.1, và thứ tự đó đủ để chép đúng cả khi đoạn nguồn chồng lên đoạn đích.

::: lemma Bổ đề 11.7 (Sao chép tuần tự)
**Giả thiết.** $0\le p<n$; $y[1..p]=x[1..p]$; $(d,\ell,c)$ là một bộ ba hợp lệ tại $p$ theo Định nghĩa 11.4 với $\ell\ge1$; bước 2.1 của Thuật toán 11.6 chép với $j=1,\ldots,\ell$ theo thứ tự tăng.

**Kết luận.** Sau bước 2.1, $y[1..p+\ell]=x[1..p+\ell]$, kể cả khi $\ell>d$.

**Điều kiện áp dụng.** Mỗi ký tự được chép trước khi ký tự kế tiếp được đọc làm nguồn.

**Phạm vi.** Bổ đề không đòi $\ell\le d$; nó không áp dụng cho phép chép cả khối một lần.
:::

::: proof
Quy nạp theo $j$, với khẳng định "sau khi chép $j$ ký tự, $y[1..p+j]=x[1..p+j]$".

**Bước 1 (cơ sở $j=0$).** Đó là giả thiết $y[1..p]=x[1..p]$.

**Bước 2 (vị trí nguồn đã được ghi).** Giả sử khẳng định đúng với $j-1$, $1\le j\le\ell$. Vị trí nguồn là $p+j-d$. Vì $d\ge1$, $p+j-d\le p+j-1$; vì $d\le p$, $p+j-d\ge j\ge1$. Vậy vị trí nguồn nằm trong đoạn $[1,p+j-1]$ đã được ghi, và theo giả thiết quy nạp $y_{p+j-d}=x_{p+j-d}$.

**Bước 3 (ký tự chép đúng).** Phép gán cho $y_{p+j}=y_{p+j-d}=x_{p+j-d}$, và theo điều kiện khớp của Định nghĩa 11.4, $x_{p+j-d}=x_{p+j}$. Vậy $y[1..p+j]=x[1..p+j]$. Với $j=\ell$ ta được kết luận. $\square$
:::

Chứng minh dùng $d\ge1$ ở Bước 2 để nguồn nằm trước đích, và dùng thứ tự tăng của $j$ để nguồn đã được ghi khi được đọc. Một nhầm lẫn thường gặp là chép cả đoạn $y[p+1-d..p+\ell-d]$ một lần bằng một lệnh chép khối. Với $(3,4,\mathrm b)$ sau `aac`, đoạn nguồn là $y[1..4]$, nhưng lúc lệnh bắt đầu chỉ có $y[1..3]$; ô $y_4$ chưa được ghi và lệnh chép khối đọc phải một giá trị không xác định. Đây là phản ví dụ cho giả thiết chép tuần tự của Bổ đề 11.7.

::: theorem Định lý 11.8 (LZ77 khôi phục đúng)
**Giả thiết.** $x\in\Sigma^n$ với $n\ge0$; $W,L\ge1$; dãy bộ ba $(d_t,\ell_t,c_t)_{t=1}^{\tau}$ do Thuật toán 11.5 sinh ra từ $x$; Thuật toán 11.6 giải dãy đó.

**Kết luận.** Thuật toán 11.6 trả về $y=x$.

**Điều kiện áp dụng.** Bộ giải mã chép tuần tự (Bổ đề 11.7) và giữ ít nhất $W$ ký tự cuối của $y$; dòng bộ ba được đóng khung và không bị hỏng.

**Phạm vi.** Định lý chỉ nói về tính đúng; nó không nói dòng bộ ba ngắn hơn $x$. Kết luận vẫn đúng với mọi dãy bộ ba hợp lệ theo Định nghĩa 11.4 nối tiếp nhau từ $p=0$ tới $p=n$, kể cả dãy không tham lam.
:::

::: proof
Đặt $p_1=0$ và $p_{t+1}=p_t+\ell_t+1$; $p_t$ là giá trị của biến $p$ ở cả hai thuật toán trước lượt $t$. Ta chứng minh bất biến: trước lượt $t$ của Thuật toán 11.6, $y=x[1..p_t]$.

**Bước 1 (khởi tạo).** Trước lượt 1, $y$ rỗng và $p_1=0$.

**Bước 2 (duy trì).** Giả sử $y=x[1..p_t]$. Theo bất biến của Thuật toán 11.5, bộ ba $(d_t,\ell_t,c_t)$ hợp lệ tại $p_t$. Nếu $\ell_t\ge1$, Bổ đề 11.7 cho $y[1..p_t+\ell_t]=x[1..p_t+\ell_t]$ sau bước 2.1; nếu $\ell_t=0$, bước 2.1 không làm gì. Bước 2.2 ghi $c_t=x_{p_t+\ell_t+1}$, nên $y=x[1..p_{t+1}]$ trước lượt $t+1$.

**Bước 3 (kết thúc).** Thuật toán 11.5 dừng khi $p=n$, nên $p_{\tau+1}=n$. Sau lượt $\tau$, $y=x[1..n]=x$. $\square$
:::

Bất biến của Định lý 11.8 đặt trên chính văn bản đã giải mã: bộ giải mã không giữ cấu trúc nào khác ngoài $W$ ký tự cuối của $y$, vì mọi khoảng lùi đều không quá $W$. Thuật toán 11.6 giữ cả $y$ nên thỏa điều kiện này. Hai điều kiện áp dụng đều được dùng ở Bước 2 của chứng minh:

- bỏ chép tuần tự: phản ví dụ chép khối sau Bổ đề 11.7, và Bổ đề 11.7 không còn áp dụng;
- bỏ "giữ ít nhất $W$ ký tự cuối": một bộ giải mã chỉ giữ $W'<W$ ký tự cuối không đọc được vị trí nguồn của bộ ba có $d>W'$.

<!-- note-topic-id: lec-11-topic-06 -->
### 2.3 Chi phí và giá của một bộ ba

Mỗi bộ ba có cỡ cố định, nên số bit của dòng nén bằng số bộ ba nhân với cỡ một bộ ba. Bộ ba $(0,0,\mathrm a)$ mã một ký tự, còn $(3,4,\mathrm b)$ mã năm ký tự với cùng số bit. Thời gian, bộ nhớ và số bit của LZ77 phụ thuộc $n$, $W$, $L$ như sau.

::: proposition Mệnh đề 11.9 (Chi phí của LZ77)
**Giả thiết.** Mô hình chi phí: đếm phép so sánh ký tự khi mã hóa và phép ghi ký tự khi giải mã, trường hợp xấu nhất. $x\in\Sigma^n$, $\lvert\Sigma\rvert=256$; Thuật toán 11.5 phát $\tau$ bộ ba; các trường của bộ ba được ghi với độ rộng cố định.

**Kết luận.**

- (a) $\tau\le n$, và Thuật toán 11.5 dùng không quá $\tau W(L+1)\le nW(L+1)$ phép so sánh, tức $O(nWL)$.
- (b) Thuật toán 11.6 dùng đúng $n$ phép ghi ký tự, tức $O(n)$.
- (c) Bộ mã hóa giữ $W+L+1$ ký tự: lịch sử, vùng nhìn trước và ký tự kế; bộ giải mã giữ $W$ ký tự.
- (d) Mỗi bộ ba tốn $\lceil\log_2W\rceil+\lceil\log_2(L+1)\rceil+8$ bit.

**Điều kiện áp dụng.** Tìm cụm khớp bằng cách so trực tiếp với mọi vị trí của cửa sổ, như bước 2.1 của Thuật toán 11.5.

**Phạm vi.** (a) là cận trên; với cấu trúc tìm kiếm khác, chi phí mã hóa thay đổi còn (b), (c), (d) giữ nguyên. Mệnh đề không cho số bộ ba $\tau$ trên một đầu vào cụ thể.
:::

::: proof
**Bước 1 (số bộ ba và phép so).** Mỗi lượt tăng $p$ ít nhất 1 và $p$ đi từ 0 tới $n$, nên $\tau\le n$. Ở một lượt, mỗi khoảng lùi $d\le W$ cần tối đa $L$ phép so khớp cộng một phép so không khớp, tức tối đa $L+1$ phép. Nhân với $\tau$ lượt cho (a).

**Bước 2 (phép ghi).** Lượt $t$ của Thuật toán 11.6 ghi $\ell_t+1$ ký tự, và $\sum_t(\ell_t+1)=p_{\tau+1}=n$ theo chứng minh Định lý 11.8. Đó là (b).

**Bước 3 (bộ nhớ).** Bộ mã hóa chỉ đọc lịch sử, tối đa $W$ ký tự, vùng nhìn trước, tối đa $L$ ký tự, và ký tự kế. Bộ giải mã chỉ đọc lại tối đa $W$ ký tự cuối của $y$. Đó là (c).

**Bước 4 (số bit).** Độ dài $\ell$ nhận $L+1$ giá trị $0,\ldots,L$, cần $\lceil\log_2(L+1)\rceil$ bit (Bài 08, Mục 1.4). Khi $\ell\ge1$, khoảng lùi $d\in\{1,\ldots,W\}$ được ghi dưới dạng $d-1\in\{0,\ldots,W-1\}$, cần $\lceil\log_2W\rceil$ bit; khi $\ell=0$, bộ giải mã bỏ qua trường này nên ghi 0. Ký tự là một byte, 8 bit. Cộng lại được (d). $\square$
:::

Với tham số của Ví dụ 11.2, $W=6$ và $L=4$, mỗi bộ ba tốn $\lceil\log_26\rceil+\lceil\log_25\rceil+8=3+3+8=14$ bit. Bộ ba $(3,4,\mathrm b)$ mã năm ký tự, 40 bit nếu ghi thô, bằng 14 bit; bộ ba $(0,0,\mathrm a)$ mã một ký tự 8 bit bằng 14 bit. LZ77 chỉ có lợi khi các bộ ba trung bình mô tả nhiều hơn $14/8=1{,}75$ ký tự.

::: remark Nhận xét 11.10 (Trong thực hành)
- **Giá của ký tự không khớp.** Với $W=4\,096$ và $L=15$, tức bộ đệm nhìn trước 16 byte của NG kể cả ký tự kế, bộ ba $(0,0,c)$ tốn $12+4+8=24$ bit cho một ký tự 8 bit (NG, tr.179).
- **LZSS.** Biến thể LZSS (Lempel–Ziv–Storer–Szymanski) phát xen kẽ hai loại mục, phân biệt bằng một bit cờ (flag bit): một cặp vị trí–độ dài $1+12+4=17$ bit, hoặc một ký tự rời $1+8=9$ bit. Cụm chỉ được mã bằng cặp khi cặp ngắn hơn các ký tự rời (NG, tr.179–180, 184).
- **Tham lam và tối ưu.** Cách tham lam không bảo đảm ít bit nhất. Trong ví dụ của NG với cụm "Go To Statement Considered Harmful", một ký tự rời tốn 9 bit và một cặp tốn 25 bit; cách tham lam mã ba cụm bằng ba cặp, hết $3\cdot25=75$ bit, còn cách tốt nhất dùng hai cặp và hai ký tự rời, hết $2\cdot25+2\cdot9=68$ bit (NG, tr.183). NG ghi nhận chênh lệch hiếm khi quá vài phần trăm, trong khi bộ mã tối ưu chậm hơn nhiều, nên phần lớn chương trình nén dùng cách tham lam (NG, tr.183–184). Chương trình gzip thì không hoàn toàn tham lam: nó có thể chọn một cụm ngắn hơn để cụm kế tiếp dài hơn (CMU-LZ, trang chiếu 8).
- **Tìm cụm nhanh hơn.** LZSS xếp các cụm của cửa sổ vào một cây tìm kiếm nhị phân (binary search tree), nên thời gian tìm tỷ lệ với $\log_2W$ nhân độ dài cụm thay cho $W$ nhân độ dài cụm của bước 2.1 (NG, tr.179). Chương trình gzip dùng một bảng băm theo mọi chuỗi con độ dài 3 trong cửa sổ, giới hạn số vị trí được thử trong mỗi ngăn (bucket), và mã vị trí, độ dài, ký tự bằng mã Huffman (CMU-LZ, trang chiếu 8–9). Vì số vị trí thử trong một ngăn bị giới hạn, mỗi byte tốn không quá một số hằng phép so; cái giá là bộ mã hóa có thể bỏ sót cụm khớp dài nhất khi một ngăn dài ra.
- **Tối ưu tiệm cận.** LZ77 với cửa sổ đủ dài đạt tỷ lệ nén tiệm cận tối ưu cho một lớp nguồn ngẫu nhiên (Wyner và Ziv, 1994; CMU-LZ, trang chiếu 10), nhưng độ dài cửa sổ cần cho kết quả này rất lớn so với cửa sổ của các chương trình thật. Chứng minh nằm ngoài phạm vi học phần.
:::

::: exercise Bài tập 11.2 (Số bit của một cặp và điểm hòa vốn)
Một bộ mã hóa LZSS mã mỗi ký tự rời bằng 9 bit và mỗi cặp vị trí–độ dài bằng 1 bit cờ cộng trường vị trí cộng trường độ dài. (a) Tính số bit của một cặp khi cửa sổ $4\,096$ byte với trường độ dài 4 bit, và khi cửa sổ $65\,536$ byte với trường độ dài 10 bit (NG, tr.208). (b) Với mỗi cấu hình, tìm độ dài $\lambda$ nhỏ nhất của một cụm sao cho mã cụm bằng một cặp tốn ít bit hơn mã $\lambda$ ký tự rời. (c) Với phép tìm vét cạn như bước 2.1 của Thuật toán 11.5, tính số lần thời gian tìm tăng lên khi cửa sổ tăng từ $4\,096$ lên $65\,536$ byte, và khi bộ đệm nhìn trước của NG, kể cả ký tự kế, tăng từ 16 lên $1\,024$ ký tự, tức $L$ tăng từ 15 lên $1\,023$.
:::

::: hint
Một cặp có lợi khi số bit của nó nhỏ hơn $9\lambda$. Ở câu (c), dùng Mệnh đề 11.9(a): số phép so tỷ lệ với $W$ và với $L+1$.
:::

::: solution
**Câu (a).** Cửa sổ $4\,096=2^{12}$ cần 12 bit vị trí, nên một cặp tốn $1+12+4=17$ bit. Cửa sổ $65\,536=2^{16}$ cần 16 bit, nên một cặp tốn $1+16+10=27$ bit, tăng khoảng 59%.

**Câu (b).** Với cặp 17 bit, cần $9\lambda>17$, tức $\lambda>17/9\approx1{,}89$, nên $\lambda=2$. Với cặp 27 bit, cần $9\lambda>27$, tức $\lambda>3$, nên $\lambda=4$; cụm 3 ký tự tốn 27 bit theo cả hai cách. Như vậy cấu hình lớn hơn mã các cụm 2 và 3 ký tự bằng ký tự rời (NG, tr.209).

**Câu (c).** Theo Mệnh đề 11.9(a), số phép so tỷ lệ với $W$ nên tăng $65\,536/4\,096=16$ lần, và tỷ lệ với $L+1$ nên tăng $1\,024/16=64$ lần (NG, tr.209).

**Kiểm tra lại.** $2\cdot9=18>17$ và $1\cdot9=9<17$; $4\cdot9=36>27$ và $3\cdot9=27$.
:::

::: exercise Bài tập 11.3 (Một trăm chữ A)
Một tệp gồm 100 chữ A liên tiếp. NG mã chữ A đầu tiên bằng $(0,0,\mathrm A)$, rồi mã chín chữ A tiếp theo cùng một chữ A kế bằng một bộ ba, ghi theo vị trí trong một bộ đệm cửa sổ là $(38,9,\mathrm A)$ (NG, tr.176). (a) Viết bộ ba thứ hai theo khoảng lùi của Định nghĩa 11.4. (b) Giải mã hai bộ ba bằng Thuật toán 11.6, ghi bản giải mã sau mỗi bước chép. (c) Với $W=4\,096$ và $L=15$, chạy Thuật toán 11.5 trên cả tệp, cho dãy bộ ba, số bộ ba và số bit theo Mệnh đề 11.9(d). (d) Dùng Bổ đề 11.7, giải thích vì sao phép chép ở câu (b) cho đúng chín chữ A dù khi bắt đầu chép bản giải mã chỉ có một chữ A.
:::

::: hint
Sau bộ ba đầu, chữ A duy nhất đã có nằm ngay trước con trỏ.
:::

::: solution
**Câu (a).** Sau $(0,0,\mathrm A)$, $p=1$ và cụm khớp bắt đầu ở $x_1$, cách con trỏ 1 ký tự, nên bộ ba là $(1,9,\mathrm A)$. Nó hợp lệ: $d=1\le p=1$ và $x_{1+j}=x_j=\mathrm A$ với $j=1,\ldots,9$.

**Câu (b).** Sau bộ ba đầu, $y=$ `A`. Bộ ba $(1,9,\mathrm A)$ chép $y_{1+j}\leftarrow y_j$ với $j=1,\ldots,9$: sau bước $j$, bản giải mã gồm $j+1$ chữ A, và với $j\ge2$, nguồn $y_j$ là ký tự vừa ghi ở bước $j-1$. Cuối cùng ghi $y_{11}\leftarrow\mathrm A$. Một bộ ba mã mười ký tự khi bản giải mã chỉ có một ký tự.

**Câu (c).** Bộ ba đầu là $(0,0,\mathrm A)$, $p=1$. Ở mỗi lượt sau, $d=1$ cho độ khớp $\min(L,n-p-1)$, lớn nhất có thể. Sáu lượt kế đều có $\ell=15$ và tiến 16 ký tự, tới $p=1+6\cdot16=97$. Lượt cuối có $\min(15,100-97-1)=2$, phát $(1,2,\mathrm A)$ và tới $p=100$. Dãy là $(0,0,\mathrm A)$, sáu lần $(1,15,\mathrm A)$, $(1,2,\mathrm A)$, tổng 8 bộ ba. Mỗi bộ ba tốn $12+\lceil\log_216\rceil+8=12+4+8=24$ bit, tổng $192$ bit so với $800$ bit của tệp gốc.

**Câu (d).** Trước bộ ba thứ hai, $y[1..1]=x[1..1]$, và theo câu (a) bộ ba $(1,9,\mathrm A)$ hợp lệ tại $p=1$. Bổ đề 11.7 cho $y[1..10]=x[1..10]$ sau phép chép: ở bước $j$, vị trí nguồn $1+j-1=j$ đã được ghi ở bước trước, hoặc là $y_1$ khi $j=1$.

**Kiểm tra lại.** $1+6\cdot16+3=100$ ký tự.
:::

Như vậy, chúng ta đã có bộ ba LZ77 (Định nghĩa 11.4), bộ mã hóa tham lam (Thuật toán 11.5), bộ giải mã chép tuần tự khôi phục đúng chuỗi (Định lý 11.8), và chi phí $O(nWL)$ khi mã hóa, $O(n)$ khi giải mã (Mệnh đề 11.9). Bảo đảm đó có giá: một cụm chỉ được dùng lại khi lần xuất hiện trước còn nằm trong $W$ ký tự cuối, và độ dài khớp bị chặn bởi $L$. Tăng $W$ và $L$ làm mỗi cặp dài thêm và làm phép tìm chậm đi nhiều lần (Bài tập 11.2), nên cần một cách nhớ cụm không gắn với khoảng cách trong văn bản.

## 3. Nén bằng từ điển cụm LZ78

Giả sử một tên riêng 9 ký tự xuất hiện ở các vị trí $1\,000$–$1\,008$ của một văn bản và lặp lại ở các vị trí $11\,000$–$11\,008$, như tên "Jacob Ziv" lặp rải rác qua nhiều chương sách của NG (tr.208). Với $W=4\,096$, khi bộ mã hóa LZ77 tới lần xuất hiện thứ hai, $p=10\,999$ và lịch sử chỉ gồm $x[6\,904..10\,999]$, nên lần xuất hiện đầu nằm ngoài cửa sổ và cả 9 ký tự phải mã lại. Bài toán là giữ một danh sách hữu hạn các cụm đã gặp, mỗi cụm mang một mã, và mã mỗi đoạn đầu vào bằng mã của một cụm trong danh sách, bất kể lần xuất hiện trước của cụm đó cách bao xa. Để chạy tay, ta dùng chuỗi `aabaacabcabcb`, $n=13$ ký tự.

**Câu hỏi.** Giữ những cụm nào, và bộ giải mã biết các cụm đó bằng cách nào khi không có cửa sổ văn bản để trỏ vào? Thuật toán LZ78, do Ziv và Lempel công bố năm 1978, trả lời cả hai ý bằng một quy tắc: mỗi lần mã một đoạn, cả hai phía thêm đúng đoạn đó vào danh sách. Bộ giải mã dựng lại danh sách từ chính dòng mã đã nhận, nên không cần truyền danh sách (NG, tr.209–210).

<!-- note-topic-id: lec-11-topic-07 -->
### 3.1 Từ điển cụm và cây từ điển

Một cách trực quan, bộ mã hóa đọc từng ký tự và kéo dài cụm hiện tại chừng nào cụm đó còn có trong danh sách. Ký tự đầu tiên làm cụm ra khỏi danh sách được gọi là ký tự phá khớp; bộ mã hóa phát mã của cụm khớp trước đó cùng ký tự phá khớp, rồi thêm "cụm khớp cộng ký tự phá khớp" làm cụm mới (NG, tr.210). Để làm rõ quy tắc này, xem bốn bước đầu trên chuỗi `aabaacabcabcb`.

::: example Ví dụ 11.4 (Bốn cặp đầu của chuỗi aabaacabcabcb)
**Dữ kiện.** Chuỗi $x=$ `aabaacabcabcb`. Danh sách ban đầu chỉ có mã 0, ứng với chuỗi rỗng (NG, tr.210; CMU-LZ, trang chiếu 11–13). Sau mỗi cặp, cụm hiện tại trở về chuỗi rỗng.

**Sáu ký tự đầu.**

| Ký tự đọc | Cụm hiện tại cộng ký tự | Có trong danh sách | Cặp phát | Mục thêm |
|---|---|---|---|---|
| $x_1=\mathrm a$ | `a` | không | $(0,\mathrm a)$ | 1 = `a` |
| $x_2=\mathrm a$ | `a` | có, mã 1 | — | — |
| $x_3=\mathrm b$ | `ab` | không | $(1,\mathrm b)$ | 2 = `ab` |
| $x_4=\mathrm a$ | `a` | có, mã 1 | — | — |
| $x_5=\mathrm a$ | `aa` | không | $(1,\mathrm a)$ | 3 = `aa` |
| $x_6=\mathrm c$ | `c` | không | $(0,\mathrm c)$ | 4 = `c` |

Ở cặp đầu, mã 0 của chuỗi rỗng đi cùng ký tự phá khớp $\mathrm a$.

**Kết quả.** Bốn cặp $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$ mô tả sáu ký tự đầu `a`·`ab`·`aa`·`c`; danh sách gồm mã 1 = `a`, 2 = `ab`, 3 = `aa`, 4 = `c`. Phần còn lại `abcabcb` được mã tiếp theo cùng quy tắc.

**Kiểm tra lại.** $1+2+2+1=6$ ký tự, và `a`·`ab`·`aa`·`c` $=$ `aabaac` $=x[1..6]$.
:::

Mỗi cụm mới là một cụm cũ cộng một ký tự, nên các cụm xếp được thành một cây: cụm `ab` là con của `a` qua cạnh $\mathrm b$, cụm `aa` là con của `a` qua cạnh $\mathrm a$. Danh sách, cặp và cây được đặt tên như sau.

::: definition Định nghĩa 11.11 (Từ điển cụm, cặp LZ78 và cây từ điển)
- Một **từ điển cụm** (phrase dictionary) là ánh xạ $D$ từ tập mã $\{0,1,\ldots,\lvert D\rvert-1\}$ vào $\Sigma^*$, với $D[0]$ là chuỗi rỗng; $\lvert D\rvert$ là số mục.
- Một **cặp** LZ78 là $(i,c)$ với $0\le i<\lvert D\rvert$ và $c\in\Sigma$; cặp mô tả chuỗi $D[i]\,c$. Sau cặp, cả hai phía **thêm mục** $D[\lvert D\rvert]\leftarrow D[i]\,c$, tức mã mới là số mục hiện có. Cặp cuối của dòng có thể là $(i,\texttt{EOS})$ với `EOS` ngoài $\Sigma$; cặp đó mô tả $D[i]$ và không thêm mục.
- **Cây từ điển** (dictionary tree, còn gọi là trie hay cây nhiều nhánh, multiway tree) của $D$ có các nút là các mã; gốc là mã 0; với mỗi mục $j\ge1$ được thêm từ cặp $(i,c)$, nút $j$ là con của nút $i$ qua cạnh mang nhãn $c$.
:::

Định nghĩa khác Định nghĩa 11.4 ở chỗ chỉ số trong cặp trỏ vào từ điển, không trỏ vào văn bản. Cặp không cần trường độ dài, vì bộ giải mã biết độ dài của $D[i]$ (NG, tr.209). Cụm của nút $j$ đọc được trên cây bằng cách nối các nhãn cạnh trên đường từ gốc tới $j$: ở Ví dụ 11.4, đường gốc $\xrightarrow{\mathrm a}1\xrightarrow{\mathrm b}2$ cho `ab`. Vì một mã chỉ có nghĩa qua cây, bộ giải mã phải giữ đúng cùng cây với bộ mã hóa: một khác biệt nhỏ cũng làm mọi cặp sau giải sai (NG, tr.213). Bộ ba của LZ77, cặp của LZ78 và mã của LZW gọi chung là đơn vị mã (token); mỗi đơn vị mã mô tả một đoạn đầu vào.

::: lemma Bổ đề 11.12 (Từ điển đóng với tiền tố)
**Giả thiết.** $D$ được dựng từ từ điển chỉ gồm mục $D[0]$, chuỗi rỗng, bằng một dãy phép thêm mục của Định nghĩa 11.11.

**Kết luận.** Mọi tiền tố của một cụm trong $D$ cũng là một cụm trong $D$. Với mỗi mã $j\ge1$, cụm $D[j]$ bỏ ký tự cuối là cụm của nút cha của $j$, nên quan hệ cha–con của Định nghĩa 11.11 là một cây có gốc 0.

**Điều kiện áp dụng.** Mỗi mục mới có dạng $D[i]\,c$ với $i$ là mã đã có.

**Phạm vi.** Bổ đề không nói các cụm đôi một khác nhau; điều đó cần thêm quy tắc chỉ thêm cụm chưa có trong $D$.
:::

::: proof
Quy nạp theo số mục thêm vào.

**Bước 1 (cơ sở).** Từ điển ban đầu chỉ có chuỗi rỗng, và tiền tố duy nhất của nó là chính nó.

**Bước 2 (bước quy nạp).** Giả sử $D$ đóng với tiền tố và mục mới là $D[i]\,c$. Mỗi tiền tố của $D[i]\,c$ hoặc là chính $D[i]\,c$, hoặc là một tiền tố của $D[i]$, và theo giả thiết quy nạp tiền tố đó có trong $D$.

**Bước 3 (cây).** Nút $j\ge1$ có đúng một cha là mã $i$ của cặp đã thêm nó, và $i<j$ vì $i$ đã là mã của $D$ khi mã $j=\lvert D\rvert$ được cấp. Đi theo cha từ $j$, mã giảm ngặt, nên sau hữu hạn bước tới gốc 0. Vậy quan hệ cha–con là một cây có gốc 0. $\square$
:::

Giả thiết "mỗi mục mới có dạng $D[i]\,c$ với $i$ đã có" được dùng ở Bước 2: một từ điển nhận cụm `ab` khi chưa có `a` không đóng với tiền tố, và nút `ab` không có cha trên cây. Bổ đề cho phép bộ mã hóa tìm cụm khớp dài nhất bằng cách đi xuống cây: mỗi ký tự đọc vào là một bước xuống một cạnh, và khi nút hiện tại không có con mang ký tự vừa đọc thì cụm hiện tại đã khớp dài nhất.

::: algorithm Thuật toán 11.13 (Mã hóa LZ78)
**Đầu vào.** Chuỗi $x=x_1\cdots x_n$ trên $\Sigma$.

**Đầu ra.** Dãy cặp $(i_1,c_1),\ldots,(i_\tau,c_\tau)$; chỉ cặp cuối có thể có $c_\tau=\texttt{EOS}$.

**Giả thiết.** Từ điển không giới hạn số mục; dòng cặp được đóng khung.

**Các bước.**

1. Đặt $D$ là từ điển chỉ gồm mục $D[0]$, chuỗi rỗng, và nút hiện tại $i\leftarrow0$.
2. Với mỗi ký tự $c=x_1,x_2,\ldots,x_n$ theo thứ tự:
   1. Nếu nút $i$ có con $j$ qua cạnh nhãn $c$, đặt $i\leftarrow j$.
   2. Nếu không, phát cặp $(i,c)$, thêm nút mới mã $\lvert D\rvert$ làm con của $i$ qua cạnh $c$, tức $D[\lvert D\rvert]\leftarrow D[i]\,c$, rồi đặt $i\leftarrow0$.
3. Nếu sau ký tự cuối $i\ne0$, phát cặp $(i,\texttt{EOS})$.

**Dừng.** Sau đúng $n$ lượt của bước 2.

**Trường hợp biên.** Với $n=0$, dòng rỗng. Nếu chuỗi kết thúc ngay sau một cặp thường thì $i=0$ và không phát cặp `EOS`. Ký tự chưa từng gặp luôn cho cặp $(0,c)$.

**Chi phí.** Mô hình: đếm phép tra con của một nút và phép thêm nút.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2.1, tra con | $n$ | một phép tra con | $n$ phép tra |
| 2.2, phát cặp, thêm nút | $\tau\le n$ | một phép thêm | $\tau$ phép thêm |
| 3, cặp `EOS` | tối đa 1 | $O(1)$ | $O(1)$ |
:::

Ở bước 2.2, cụm $D[i]\,c$ chưa có trong $D$, vì nút $i$ không có con qua $c$.

Thuật toán đúng theo bất biến sau: các cặp đã phát mô tả nối tiếp nhau một đoạn đầu $x[1..p]$ của chuỗi, và cụm $D[i]$ của nút hiện tại bằng các ký tự đã đọc sau vị trí $p$.

- Khởi tạo: $p=0$, $i=0$ và chưa đọc ký tự nào.
- Duy trì: bước 2.1 giữ bất biến vì $D[j]=D[i]\,c$; bước 2.2 phát cặp mô tả $D[i]\,c$, đúng bằng phần đã đọc sau $p$, rồi đưa $i$ về gốc.
- Kết thúc: khi hết chuỗi, bước 3 mô tả phần còn lại $D[i]$, nên dãy cặp mô tả cả $x$.

<!-- note-topic-id: lec-11-topic-08 -->
### 3.2 Đồng bộ hai từ điển

Bộ giải mã nhận dãy cặp và phải dựng lại cùng từ điển, cùng thứ tự mã như bộ mã hóa. Ta chạy bộ giải mã trên bốn cặp của Ví dụ 11.4.

::: example Ví dụ 11.5 (Giải mã bốn cặp đầu và dựng cây)
**Dữ kiện.** Dãy cặp $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$ (Ví dụ 11.4). Từ điển của bộ giải mã ban đầu chỉ có mã 0, chuỗi rỗng.

**Từng cặp.**

| Cặp | $D[i]$ | Xuất $D[i]\,c$ | Mục thêm | Bản giải mã |
|---|---|---|---|---|
| $(0,\mathrm a)$ | rỗng | `a` | 1 = `a` | `a` |
| $(1,\mathrm b)$ | `a` | `ab` | 2 = `ab` | `aab` |
| $(1,\mathrm a)$ | `a` | `aa` | 3 = `aa` | `aabaa` |
| $(0,\mathrm c)$ | rỗng | `c` | 4 = `c` | `aabaac` |

**Kiểm tra lại.** Bản giải mã `aabaac` $=x[1..6]$, và bốn mục thêm trùng bốn mục của bộ mã hóa ở Ví dụ 11.4.
:::

![Cây từ điển LZ78 sau bốn cặp đầu của aabaacabcabcb. Gốc 0 là chuỗi rỗng; cạnh a tới nút 1 (cụm a), cạnh c tới nút 4 (cụm c); từ nút 1, cạnh a tới nút 3 (cụm aa) và cạnh b tới nút 2 (cụm ab). Bên phải: cặp (0, a) thêm 1 = a; cặp (1, b) thêm 2 = ab; cặp (1, a) thêm 3 = aa; cặp (0, c) thêm 4 = c.](img/lec-11/note-lz78-cay.svg)

Trên hình là cây chung của hai phía sau bốn cặp. Mỗi cặp $(i,c)$ thêm một lá dưới nút $i$ qua cạnh $c$; mã của lá là số thứ tự của cặp. Bộ mã hóa dùng cây để đi xuống khi đọc ký tự, còn bộ giải mã dùng cây để đọc ra cụm $D[i]$ khi nhận mã $i$.

::: algorithm Thuật toán 11.14 (Giải mã LZ78)
**Đầu vào.** Dãy cặp $(i_1,c_1),\ldots,(i_\tau,c_\tau)$.

**Đầu ra.** Chuỗi $y$.

**Giả thiết.** Dòng cặp được đóng khung và không bị hỏng; hai phía dùng cùng quy tắc thêm mục của Định nghĩa 11.11.

**Các bước.**

1. Đặt $D$ là từ điển chỉ gồm mục $D[0]$, chuỗi rỗng, và $y$ là chuỗi rỗng.
2. Với mỗi cặp $(i_t,c_t)$, $t=1,\ldots,\tau$:
   1. Nếu $i_t\ge\lvert D\rvert$, báo dòng hỏng và dừng.
   2. Nếu $c_t=\texttt{EOS}$, nối $D[i_t]$ vào $y$ và dừng.
   3. Nếu không, nối $D[i_t]\,c_t$ vào $y$ và thêm $D[\lvert D\rvert]\leftarrow D[i_t]\,c_t$.
3. Trả về $y$.

**Dừng.** Sau $\tau$ cặp, hoặc ở cặp `EOS`, hoặc khi gặp mã không tồn tại.

**Trường hợp biên.** Dòng rỗng cho $y$ rỗng; cặp $(0,c)$ xuất một ký tự; cặp $(0,\texttt{EOS})$ không xuất gì.

**Chi phí.** Mô hình: đếm phép ghi một ký tự ra $y$, khi mỗi nút lưu cặp (mã cha, ký tự) và cụm $D[i_t]$ được đọc bằng cách đi từ nút $i_t$ lên gốc rồi đảo thứ tự.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2.2–2.3, đọc và xuất $D[i_t]\,c_t$ | $\tau$ | $\lvert D[i_t]\rvert+1$ phép ghi, hoặc $\lvert D[i_t]\rvert$ ở cặp `EOS` | $n$ phép ghi |
| 2.3, thêm mục | $\tau$ | $O(1)$ | $O(\tau)$ |
:::

Bộ giải mã không cần biết bộ mã hóa đã đi xuống cây ra sao; nó chỉ cần, trước mỗi cặp, có cùng từ điển, và điều đó được chứng minh bằng quy nạp theo số cặp.

::: theorem Định lý 11.15 (Đồng bộ từ điển và khôi phục đúng của LZ78)
**Giả thiết.** $x\in\Sigma^n$; dãy cặp $(i_t,c_t)_{t=1}^{\tau}$ do Thuật toán 11.13 sinh ra từ $x$; Thuật toán 11.14 giải dãy đó. Gọi $p_t$ là số ký tự của $x$ mà $t$ cặp đầu mô tả, $p_0=0$.

**Kết luận.** Với mọi $t=0,1,\ldots,\tau$, sau cặp thứ $t$: (a) từ điển $D'$ của bộ giải mã và từ điển $D$ của bộ mã hóa có cùng số mục, và $D'[j]=D[j]$ với mọi mã $j$; (b) bản giải mã là $y=x[1..p_t]$. Nói riêng, khi dừng $y=x$.

**Điều kiện áp dụng.** Hai phía bắt đầu từ cùng từ điển, thêm mục theo cùng quy tắc của Định nghĩa 11.11 và đánh mã theo cùng thứ tự; dòng cặp không bị hỏng.

**Phạm vi.** Định lý giả thiết từ điển không giới hạn; khi từ điển đầy, hai phía phải còn dùng chung cả quy tắc xử lý từ điển đầy.
:::

::: proof
Quy nạp theo $t$.

**Bước 1 (cơ sở $t=0$).** Hai từ điển chỉ có mã 0 ứng với chuỗi rỗng, và $y$ rỗng $=x[1..0]$.

**Bước 2 (cặp thường).** Giả sử (a), (b) đúng sau cặp $t-1$, và cặp $t$ là $(i_t,c_t)$ với $c_t\in\Sigma$. Bộ mã hóa phát cặp này ở bước 2.2 khi nút hiện tại là $i_t$; theo bất biến của Thuật toán 11.13, $x[p_{t-1}+1..p_t]=D[i_t]\,c_t$. Vì $i_t$ là mã có trong từ điển của bộ mã hóa trước cặp $t$, theo (a) nó cũng có trong từ điển của bộ giải mã và $D'[i_t]=D[i_t]$. Do đó bước 2.3 nối đúng $x[p_{t-1}+1..p_t]$ vào $y$, cho (b). Hai phía cùng thêm chuỗi $D[i_t]\,c_t$ ở cùng mã, là số mục hiện có, nên (a) được giữ.

**Bước 3 (cặp `EOS`).** Nếu $c_t=\texttt{EOS}$ thì $t=\tau$ và theo bước 3 của Thuật toán 11.13, $x[p_{t-1}+1..n]=D[i_t]$. Bộ giải mã nối $D'[i_t]=D[i_t]$ và dừng, nên $y=x$.

**Bước 4 (kết thúc).** Cặp cuối mô tả tới ký tự $x_n$, nên $p_\tau=n$ và $y=x$. $\square$
:::

Giả thiết "cùng quy tắc thêm mục" được dùng ở Bước 2 của chứng minh. Giả sử bộ giải mã chỉ thêm mục khi $i_t\ge1$. Sau cặp $(0,\mathrm a)$ của Ví dụ 11.5, từ điển của nó chỉ có mã 0, nên ở cặp $(1,\mathrm b)$ nó gặp mã 1 không tồn tại, trong khi bộ mã hóa đã gán mã 1 cho `a`. Một quy tắc lệch nhẹ hơn, như đánh mã mục mới từ 2, không làm bộ giải mã báo lỗi nhưng làm mọi mã sau trỏ sai cụm.

Định lý 11.15 và Định lý 11.8 cùng chứng minh bằng một bất biến, nhưng trên hai đối tượng khác nhau. LZ77 giữ bất biến trên văn bản đã giải mã, vì mỗi bộ ba trỏ vào văn bản đó. LZ78 giữ bất biến trên từ điển, vì mỗi cặp trỏ vào từ điển; văn bản đã giải mã đúng là hệ quả của từ điển đúng.

<!-- note-topic-id: lec-11-topic-09 -->
### 3.3 Chi phí và từ điển đầy

Thuật toán 11.13 đọc mỗi ký tự một lần, nhưng mỗi lần đọc là một phép tra con của một nút, và chi phí của phép đó phụ thuộc cách lưu các con. Từ điển còn lớn dần theo số cặp, nên độ rộng của mã trong cặp và bộ nhớ đều phụ thuộc số mục tối đa $M$.

::: proposition Mệnh đề 11.16 (Chi phí của LZ78)
**Giả thiết.** Mô hình chi phí: một phép tra con, một phép thêm nút, một phép ghi ký tự đều tính theo cài đặt nêu trong từng ý. $x\in\Sigma^n$; Thuật toán 11.13 phát $\tau$ cặp; mã được ghi với độ rộng cố định, đủ cho $M$ mã, và $M$ đủ chứa mọi mục.

**Kết luận.**

- (a) $\tau\le n$ và từ điển có không quá $\tau+1$ mục.
- (b) Nếu mỗi nút lưu danh sách các con, Thuật toán 11.13 tốn $O(n\lvert\Sigma\rvert)$ phép so trong trường hợp xấu nhất. Nếu các con được tìm qua một bảng băm với khóa (mã cha, ký tự), dưới giả thiết băm đều và hệ số tải hằng, thời gian kỳ vọng là $O(n)$.
- (c) Nếu mỗi nút lưu (mã cha, ký tự), Thuật toán 11.14 tốn đúng $n$ phép ghi ký tự cộng $O(\tau)$ phép thêm mục, tức $O(n)$.
- (d) Mỗi cặp tốn $\lceil\log_2M\rceil+\lceil\log_2(\lvert\Sigma\rvert+1)\rceil$ bit, trong đó trường ký tự chứa thêm `EOS`; với byte, đó là $\lceil\log_2M\rceil+9$ bit.

**Điều kiện áp dụng.** (b) phần kỳ vọng cần giả thiết băm đều của CLRS, Chương 11; trên khóa thật, hàm băm cụ thể có thể không thỏa giả thiết đó.

**Phạm vi.** Mệnh đề đếm thời gian, bộ nhớ và số bit mỗi cặp; nó không cho số cặp $\tau$ trên một đầu vào cụ thể.
:::

::: proof
**Bước 1 (số cặp, số mục).** Mỗi cặp thường mô tả ít nhất một ký tự. Cặp `EOS` chỉ được phát khi $i\ne0$, nên cũng mô tả cụm khác rỗng $D[i]$. Các cụm được mô tả nối lại thành $x$, nên $\tau\le n$. Mỗi cặp thêm tối đa một mục vào từ điển ban đầu một mục. Đó là (a).

**Bước 2 (mã hóa).** Bước 2.1 chạy đúng $n$ lần. Với danh sách con, một phép tra con so ký tự với tối đa $\lvert\Sigma\rvert$ con, tổng $O(n\lvert\Sigma\rvert)$. Với bảng băm, mỗi phép tra hoặc thêm tốn thời gian kỳ vọng $O(1)$ (CLRS, Chương 11), nên tổng kỳ vọng là $O(n+\tau)=O(n)$. Đó là (b).

**Bước 3 (giải mã).** Đọc $D[i_t]$ bằng cách đi từ nút $i_t$ lên gốc tốn $\lvert D[i_t]\rvert$ bước, mỗi bước cho một ký tự theo thứ tự ngược; đảo lại và ghi $c_t$ tốn $\lvert D[i_t]\rvert+1$ phép ghi. Tổng theo $t$ bằng số ký tự của $y$, tức $n$. Đó là (c).

**Bước 4 (số bit).** Mã cụm nhận tối đa $M$ giá trị $0,\ldots,M-1$, cần $\lceil\log_2M\rceil$ bit; trường ký tự nhận $\lvert\Sigma\rvert+1$ giá trị kể cả `EOS`, cần $\lceil\log_2(\lvert\Sigma\rvert+1)\rceil$ bit (Bài 08, Mục 1.4). Với $\lvert\Sigma\rvert=256$, $\lceil\log_2257\rceil=9$. Đó là (d). $\square$
:::

Mỗi cặp mang nguyên một ký tự ở dạng thô. Với từ điển $M=2^{16}$ mục và byte, mỗi cặp tốn $16+9=25$ bit, nên một cặp chỉ có lợi khi trung bình mô tả hơn $25/8=3{,}125$ ký tự. So với LZ77 (Mệnh đề 11.9), LZ78 thay phép so vét cạn $O(nWL)$ bằng $n$ phép tra con, kỳ vọng $O(n)$, và thay cửa sổ $W+L+1$ ký tự bằng từ điển tối đa $M$ mục; đổi lại, đơn vị mã dài hơn: 25 bit so với 24 bit của bộ ba với $W=4\,096$, $L=15$.

::: remark Nhận xét 11.17 (Trong thực hành)
- **Lưu các con.** Một mảng 256 con ở mỗi nút cho phép tra con trong $O(1)$ nhưng lãng phí vì đa số nút có rất ít con; danh sách con tiết kiệm bộ nhớ nhưng mỗi phép tra con tốn tới $O(\lvert\Sigma\rvert)$ phép so (Mệnh đề 11.16(b); NG, tr.212–213). Bảng băm với khóa (mã cha, ký tự) là lựa chọn ở giữa.
- **Từ điển đầy.** Với mã 16 bit, từ điển chứa $65\,536$ cụm kể cả chuỗi rỗng và đầy sau $65\,535$ cụm (NG, tr.212–213). NG coi việc ngừng thêm cụm là lựa chọn mặc định an toàn nhất. Chương trình `compress` của UNIX theo dõi tỷ lệ nén và xóa từ điển, bắt đầu lại từ đầu khi tỷ lệ xấu đi (NG, tr.213). Định dạng GIF bỏ từ điển khi đạt kích thước tối đa; chuẩn BTLZ của British Telecom bỏ mục ít được dùng gần đây nhất (CMU-LZ, trang chiếu 18). Mọi lựa chọn đều phải là một phần của giao thức chung, như giả thiết "cùng quy tắc" của Định lý 11.15.
- **Dữ liệu đổi bản chất.** Khi nén một tệp thực thi, phần mã lệnh và phần dữ liệu có thống kê khác hẳn nhau; từ điển dựng trên phần mã lệnh trở nên lỗi thời ở phần dữ liệu (NG, tr.213).
- **Từ điển lớn và tệp nhỏ.** LZ78 nén tốt dần khi từ điển lớn lên chỉ khi đầu vào đủ dài; với tệp nhỏ, mã rộng hơn làm mỗi cặp tốn thêm bit mà từ điển chưa kịp có cụm dài (NG, tr.212).
:::

::: exercise Bài tập 11.4 (LZ78 cho chuỗi DAD␣DADA␣DADDY␣DADO)
Chuỗi gồm 19 ký tự `DAD␣DADA␣DADDY␣DADO`, với `␣` là dấu cách (NG, tr.210–212). (a) Chạy Thuật toán 11.13, lập bảng các cặp và các mục từ điển. (b) Vẽ cây từ điển sau 19 ký tự. (c) Giải mã dãy cặp bằng Thuật toán 11.14 để kiểm tra. (d) Chứng minh bằng quy nạp theo số cặp rằng các cụm trong từ điển của Thuật toán 11.13 luôn đôi một khác nhau. (e) Kiểm rằng sau mỗi cặp ở câu (c), mục bộ giải mã thêm trùng mục bộ mã hóa thêm ở câu (a), và chỉ ra bước của chứng minh Định lý 11.15 bảo đảm điều đó.
:::

::: hint
Cặp thứ ba bắt đầu bằng `D` đã có mã 1 và dừng ở dấu cách. Ở câu (d), xét điều kiện để bước 2.2 thêm một mục.
:::

::: solution
**Câu (a).** Chín cặp và chín mục:

| Cặp | Cụm mô tả | Mục thêm |
|---|---|---|
| $(0,\mathrm D)$ | `D` | 1 = `D` |
| $(0,\mathrm A)$ | `A` | 2 = `A` |
| `(1, ␣)` | `D␣` | 3 = `D␣` |
| $(1,\mathrm A)$ | `DA` | 4 = `DA` |
| `(4, ␣)` | `DA␣` | 5 = `DA␣` |
| $(4,\mathrm D)$ | `DAD` | 6 = `DAD` |
| $(1,\mathrm Y)$ | `DY` | 7 = `DY` |
| `(0, ␣)` | `␣` | 8 = `␣` |
| $(6,\mathrm O)$ | `DADO` | 9 = `DADO` |

**Câu (b).** Gốc 0 có ba con: 1 (`D`) qua $\mathrm D$, 2 (`A`) qua $\mathrm A$, 8 (`␣`) qua dấu cách. Nút 1 có ba con: 3 qua dấu cách, 4 qua $\mathrm A$, 7 qua $\mathrm Y$. Nút 4 có hai con: 5 qua dấu cách, 6 qua $\mathrm D$. Nút 6 có một con: 9 qua $\mathrm O$.

**Câu (c).** Bộ giải mã xuất lần lượt `D`, `A`, `D␣`, `DA`, `DA␣`, `DAD`, `DY`, `␣`, `DADO` và thêm đúng chín mục ở câu (a); nối lại được chuỗi ban đầu.

**Câu (d).** Trước cặp đầu, từ điển chỉ có chuỗi rỗng. Giả sử trước một cặp, các cụm đôi một khác nhau. Bước 2.2 chỉ thêm $D[i]\,c$ khi nút $i$ không có con qua cạnh $c$. Nếu một mục $j\ge1$ đã có $D[j]=D[i]\,c$, mục đó được thêm từ một cặp $(i',c')$ với $D[i']\,c'=D[i]\,c$, nên $c'=c$ và $D[i']=D[i]$; theo giả thiết quy nạp $i'=i$, tức $j$ là con của $i$ qua $c$, trái điều kiện của bước 2.2. Vậy $D[i]\,c$ khác mọi cụm đã có. Sau cặp, các cụm vẫn đôi một khác nhau.

**Câu (e).** Ở cặp thứ $t$, bộ giải mã thêm $D'[t]=D'[i_t]\,c_t$; chẳng hạn cặp `(4, ␣)` cho $D'[5]$ là $D'[4]=$ `DA` nối dấu cách, tức `DA␣`, đúng mục 5 của câu (a), và cả chín mục đều trùng. Bước 2 của chứng minh Định lý 11.15 bảo đảm điều đó: hai phía cùng thêm chuỗi $D[i_t]\,c_t$ ở cùng mã, là số mục hiện có.

**Kiểm tra lại.** Độ dài các cụm $1+1+2+2+3+3+2+1+4=19$. Chuỗi kết thúc ngay sau cặp $(6,\mathrm O)$ nên không có cặp `EOS`.
:::

Như vậy, chúng ta đã có từ điển cụm và cây của nó (Định nghĩa 11.11, Bổ đề 11.12), bộ mã hóa và bộ giải mã LZ78 (Thuật toán 11.13, 11.14) luôn giữ cùng từ điển (Định lý 11.15), với chi phí kỳ vọng $O(n)$ khi tra con bằng bảng băm (Mệnh đề 11.16). Một cụm được nhớ bao lâu tùy từ điển, không tùy khoảng cách trong văn bản. Tuy nhiên, mỗi cặp vẫn mang một ký tự ở dạng thô, 9 bit kể cả khả năng `EOS`: trên `aabaacabcabcb`, LZ78 phát 6 cặp, tức 6 trong 13 ký tự đi qua dòng nén ở dạng thô cộng thêm mã cụm. Ký tự phá khớp của một cặp lại chính là ký tự đầu của đoạn kế tiếp, nên trường ký tự này lặp lại thông tin mà đoạn kế tiếp đã mang.

## 4. Thuật toán LZW

Bài toán là mã chuỗi `aabaacabcabcb` bằng một dãy chỉ gồm mã cụm, không kèm ký tự thô nào, sao cho bộ giải mã vẫn dựng lại được từ điển và chuỗi. Với byte và từ điển $2^{16}$ mục, bỏ được trường ký tự thì mỗi đơn vị mã còn 16 bit thay vì 25 bit. Thuật toán LZW, do Welch công bố năm 1984 trên nền LZ78, làm việc đó bằng một từ điển nạp sẵn (preloaded dictionary) mọi cụm một ký tự (NG, tr.214; CMU-LZ, trang chiếu 15).

Chúng ta dùng quy ước mã sau (NG, tr.214–215; CMU-LZ, trang chiếu 15): mã $0,\ldots,255$ là chính giá trị byte, mã đầu tiên của một cụm mới là 256, và dòng mã được đóng khung bằng số mã truyền kèm (Nhận xét 10.4), không dành mã nào cho `EOS`.

<!-- note-topic-id: lec-11-topic-10 -->
### 4.1 Từ điển nạp sẵn và mã hóa

Về mặt ý tưởng, LZW vẫn kéo dài cụm hiện tại chừng nào cụm còn trong từ điển, và vẫn thêm "cụm khớp cộng ký tự phá khớp" làm cụm mới. Khác LZ78, ký tự phá khớp không được phát kèm mã; nó trở thành ký tự đầu của cụm kế tiếp. Để làm rõ, xem toàn bộ quá trình mã hóa chuỗi `aabaacabcabcb`.

::: example Ví dụ 11.6 (Mã hóa LZW chuỗi aabaacabcabcb)
**Dữ kiện.** Chuỗi $x=$ `aabaacabcabcb`, $n=13$. Từ điển nạp sẵn 256 cụm một byte, trong đó $\mathrm a\mapsto97$, $\mathrm b\mapsto98$, $\mathrm c\mapsto99$; mã chưa cấp nhỏ nhất là 256. Cụm hiện tại $w$ ban đầu là ký tự đầu, `a`.

**Từng ký tự đọc vào.**

| Ký tự đọc | $w$ trước | $w$ + ký tự trong từ điển | Mã phát | Mục thêm | $w$ sau |
|---|---|---|---|---|---|
| $x_2=\mathrm a$ | `a` | `aa`: không | 97 | 256 = `aa` | `a` |
| $x_3=\mathrm b$ | `a` | `ab`: không | 97 | 257 = `ab` | `b` |
| $x_4=\mathrm a$ | `b` | `ba`: không | 98 | 258 = `ba` | `a` |
| $x_5=\mathrm a$ | `a` | `aa`: có (256) | — | — | `aa` |
| $x_6=\mathrm c$ | `aa` | `aac`: không | 256 | 259 = `aac` | `c` |
| $x_7=\mathrm a$ | `c` | `ca`: không | 99 | 260 = `ca` | `a` |
| $x_8=\mathrm b$ | `a` | `ab`: có (257) | — | — | `ab` |
| $x_9=\mathrm c$ | `ab` | `abc`: không | 257 | 261 = `abc` | `c` |
| $x_{10}=\mathrm a$ | `c` | `ca`: có (260) | — | — | `ca` |
| $x_{11}=\mathrm b$ | `ca` | `cab`: không | 260 | 262 = `cab` | `b` |
| $x_{12}=\mathrm c$ | `b` | `bc`: không | 98 | 263 = `bc` | `c` |
| $x_{13}=\mathrm b$ | `c` | `cb`: không | 99 | 264 = `cb` | `b` |
| hết chuỗi | `b` | — | 98 | — | — |

**Kết quả.** Dòng mã 97, 97, 98, 256, 99, 257, 260, 98, 99, 98 gồm 10 mã; các mục mới 256–264 là `aa`, `ab`, `ba`, `aac`, `ca`, `abc`, `cab`, `bc`, `cb`.

**Kiểm tra lại.** Mười mã ứng với các cụm `a`, `a`, `b`, `aa`, `c`, `ab`, `ca`, `b`, `c`, `b`; nối lại được `aabaacabcabcb`, và $1+1+1+2+1+2+2+1+1+1=13=n$. Có 9 mục mới cho 10 mã, vì mã cuối không thêm mục.
:::

Trong bảng, mã 256 được phát ở dòng thứ năm, sau khi được thêm ở dòng thứ nhất; cụm `ca` được thêm ở dòng thứ sáu và dùng lại ở dòng thứ chín. Mỗi mục thêm là cụm vừa phát nối với ký tự vừa đọc, và ký tự đó mở cụm kế tiếp.

::: definition Định nghĩa 11.18 (Từ điển LZW và mã kế tiếp)
- **Từ điển nạp sẵn** của LZW là $D[v]=$ byte có giá trị $v$, với $v=0,\ldots,255$.
- **Mã kế tiếp** $\texttt{next\_code}$ là mã chưa cấp nhỏ nhất; ban đầu $\texttt{next\_code}=256$.
- Một **dòng mã** LZW của chuỗi $x$ là dãy $k_1,\ldots,k_\tau$ với các cụm $w_t=D[k_t]$ thỏa $w_1w_2\cdots w_\tau =x$. Khi phát $k_t$ với $t<\tau$, bộ mã hóa thêm mục $D[\texttt{next\_code}]\leftarrow w_t\operatorname{first}(w_{t+1})$ rồi tăng $\texttt{next\_code}$ thêm 1; mã cuối $k_\tau$ không thêm mục.
:::

So với Định nghĩa 11.11, thành phần thay đổi là nội dung của một đơn vị mã: cặp $(i,c)$ của LZ78 thành mã $k$ của LZW. Mục được thêm vẫn là "cụm cộng một ký tự", nhưng ký tự đó, $\operatorname{first}(w_{t+1})$, lại thuộc cụm kế tiếp. Với LZ78, bộ giải mã biết mục mới ngay khi nhận cặp; với LZW, nó chỉ biết sau khi giải mã cụm kế tiếp. Hệ quả của thay đổi này nằm ở chi phí và ở bộ giải mã: trên cùng chuỗi `aabaacabcabcb`, LZW phát 10 mã, mỗi mã không mang ký tự thô.

::: algorithm Thuật toán 11.19 (Mã hóa LZW)
**Đầu vào.** Chuỗi $x=x_1\cdots x_n$ trên bảng chữ cái byte, $n\ge0$.

**Đầu ra.** Dòng mã $k_1,\ldots,k_\tau$.

**Giả thiết.** Từ điển không giới hạn số mục; dòng mã được đóng khung bằng số mã $\tau$.

**Các bước.**

1. Nạp sẵn $D[v]$ cho $v=0,\ldots,255$; đặt $\texttt{next\_code}\leftarrow256$ và $w\leftarrow x_1$.
2. Với mỗi ký tự $c=x_2,\ldots,x_n$ theo thứ tự:
   1. Nếu $w\,c$ có trong $D$, đặt $w\leftarrow w\,c$.
   2. Nếu không, phát mã của $w$; gán $D[\texttt{next\_code}]\leftarrow w\,c$ và tăng $\texttt{next\_code}$ thêm 1; đặt $w\leftarrow c$.
3. Phát mã của $w$.

**Dừng.** Sau $n-1$ lượt của bước 2 và một lần phát ở bước 3.

**Trường hợp biên.** Với $n=0$, dòng mã rỗng và không chạy bước 1. Với $n=1$, dòng mã gồm một mã là chính byte $x_1$. Một byte chưa từng gặp vẫn có mã vì từ điển được nạp sẵn.

**Chi phí.** Mô hình: một phép tra $D$ với khóa (mã của $w$, $c$), một phép thêm mục và một phép phát mã đều tính một đơn vị.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 2.1, tra $w\,c$ | $n-1$ | một phép tra | $n-1$ phép tra |
| 2.2, phát mã, thêm mục | $\tau -1$ | một phép phát, một phép thêm | $\tau -1$ mỗi loại |
| 3, phát mã cuối | 1 | một phép phát | 1 |
:::

Bước 2.1 tra khóa (mã của $w$, $c$) chứ không tra cả chuỗi $w\,c$: cụm $w\,c$ có trong $D$ khi và chỉ khi nút của $w$ trong cây từ điển có con qua cạnh $c$, giống bước 2.1 của Thuật toán 11.13. Thuật toán đúng theo bất biến: trước mỗi lượt, $w$ là một cụm có trong $D$, và các cụm của những mã đã phát nối với $w$ cho đúng đoạn đầu đã đọc của $x$. Bất biến đúng sau bước 1 vì $w=x_1$ có mã nạp sẵn. Bước 2.1 giữ nó vì $w\,c\in D$. Bước 2.2 phát mã của $w\in D$ rồi đặt $w=c$, một cụm nạp sẵn. Sau bước 3, các cụm của mọi mã nối lại thành $x$.

<!-- note-topic-id: lec-11-topic-11 -->
### 4.2 Giải mã với độ trễ một mục

Bộ giải mã nhận dòng mã 97, 97, 98, … và phải dựng lại cùng từ điển. Khi đọc mã đầu tiên, nó biết cụm `a`, nhưng chưa biết mục 256, vì mục đó cần ký tự đầu của cụm thứ hai.

::: example Ví dụ 11.7 (Giải mã LZW dòng mã của Ví dụ 11.6)
**Dữ kiện.** Dòng mã 97, 97, 98, 256, 99, 257, 260, 98, 99, 98 của Ví dụ 11.6; từ điển nạp sẵn 256 cụm một byte, $\texttt{next\_code}=256$.

**Ba mã đầu.**

- Đọc 97: xuất `a`, đặt $w=$ `a`; chưa thêm mục.
- Đọc 97: mã có sẵn, xuất `a`. Thêm $D[256]=w\operatorname{first}(\texttt{a})=$ `aa`, $\texttt{next\_code}=257$, đặt $w=$ `a`.
- Đọc 98: xuất `b`. Thêm $D[257]=$ `a`+`b` $=$ `ab`, $\texttt{next\_code}=258$, đặt $w=$ `b`.

Bộ mã hóa thêm mục 256 ngay khi phát mã thứ nhất; bộ giải mã thêm cùng mục đó sau khi đọc mã thứ hai. Bộ giải mã luôn chậm hơn bộ mã hóa một mục (CMU-LZ, trang chiếu 16).

**Bảy mã còn lại.**

| Mã đọc | $\texttt{next\_code}$ trước | Xuất | Mục thêm |
|---|---|---|---|
| 256 | 258 | `aa` | 258 = `b`+`a` = `ba` |
| 99 | 259 | `c` | 259 = `aa`+`c` = `aac` |
| 257 | 260 | `ab` | 260 = `c`+`a` = `ca` |
| 260 | 261 | `ca` | 261 = `ab`+`c` = `abc` |
| 98 | 262 | `b` | 262 = `ca`+`b` = `cab` |
| 99 | 263 | `c` | 263 = `b`+`c` = `bc` |
| 98 | 264 | `b` | 264 = `c`+`b` = `cb` |

**Kiểm tra lại.** Bản giải mã `a`·`a`·`b`·`aa`·`c`·`ab`·`ca`·`b`·`c`·`b` $=$ `aabaacabcabcb`, và các mục 256–264 trùng các mục của Ví dụ 11.6. Mọi mã đọc vào đều nhỏ hơn $\texttt{next\_code}$ lúc đó; chẳng hạn mã 260 được đọc khi $\texttt{next\_code}=261$.
:::

Độ trễ một mục đặt ra một khả năng: bộ mã hóa phát đúng mã vừa thêm, trong khi bộ giải mã chưa có mục đó. Trong Ví dụ 11.7, không mã vừa thêm nào được phát ngay; trên những đầu vào có dạng "ký tự, chuỗi, ký tự, chuỗi, ký tự" thì có (NG, tr.217). Hai trường hợp như vậy là một trường hợp của NG và một vết đầy đủ.

::: example Ví dụ 11.8 (Mã chưa có trong từ điển của bộ giải mã)
**(a) Chuỗi IWOMBAT.** Giả sử từ điển đã có mục $300=$ `IWOMBAT`, đầu vào chứa đoạn `IWOMBATIWOMBATIX`, và lúc bộ mã hóa phát 300 thì $\texttt{next\_code}=400$ (NG, tr.217).

- Bộ mã hóa khớp `IWOMBAT`, đọc `I`, thấy `IWOMBATI` chưa có. Nó phát 300, thêm mục 400 = `IWOMBATI`, và mở cụm mới từ `I`.
- Cụm mới khớp tiếp `IWOMBAT` rồi `IWOMBATI` (mục 400 vừa thêm), đọc `X` và thấy `IWOMBATIX` chưa có. Nó phát 400.
- Bộ giải mã, chậm một mục, có $\texttt{next\_code}=399$ trước khi đọc 300. Nó đọc 300, xuất `IWOMBAT` và thêm mục 399 là cụm giải mã ngay trước đó nối với `I`; lúc này $\texttt{next\_code}=400$. Mã kế tiếp là 400, chưa có trong từ điển của nó.
- Cụm của mã 400 là cụm vừa xuất nối với ký tự đầu của chính nó: `IWOMBAT` + `I` $=$ `IWOMBATI`, đúng cụm bộ mã hóa đã thêm.

**(b) Vết đầy đủ.** Giả sử đầu vào là `abababa`, với $\mathrm a\mapsto97$, $\mathrm b\mapsto98$.

- Mã hóa: phát 97, thêm 256 = `ab`; phát 98, thêm 257 = `ba`; khớp `ab` rồi phát 256, thêm 258 = `aba`; khớp `ab`, `aba`, hết chuỗi, phát 258. Dòng mã là $97,98,256,258$.
- Giải mã: đọc 97, xuất `a`; đọc 98, xuất `b`, thêm 256 = `ab`; đọc 256, xuất `ab`, thêm 257 = `b`+`a` = `ba`; $\texttt{next\_code}=258$.
- Đọc 258 $=\texttt{next\_code}$: mã chưa có. Cụm vừa xuất là $w=$ `ab`, nên cụm mới là $w\operatorname{first}(w)=$ `ab`+`a` $=$ `aba`; xuất `aba` và thêm 258 = `ab`+`a` = `aba`.

**Kiểm tra lại.** `a`·`b`·`ab`·`aba` $=$ `abababa`, và mục 258 của hai phía cùng là `aba`. Đoạn `ababa` từ vị trí 3 có dạng ký tự $\mathrm a$, chuỗi `b`, ký tự $\mathrm a$, chuỗi `b`, ký tự $\mathrm a$, với cụm `ab` đã có mã 256.
:::

![Hai hàng bốn cột cho đầu vào giả sử abababa với a = 97, b = 98. Bộ mã hóa: phát 97, thêm 256 = ab; phát 98, thêm 257 = ba; phát 256, thêm 258 = aba; phát 258. Bộ giải mã: đọc 97, xuất a; đọc 98, xuất b, thêm 256 = ab; đọc 256, xuất ab, thêm 257 = ba; ô cuối viền nét đứt: đọc 258 bằng next_code, xuất ab + a = aba, thêm 258 = aba. Mũi tên chéo nối mỗi mục bộ mã hóa thêm với cột kế tiếp của bộ giải mã.](img/lec-11/note-lzw-ma-chua-co.svg)

Trên hình, mỗi mũi tên chéo nối một mục bộ mã hóa thêm với cột mà bộ giải mã thêm cùng mục đó, luôn lệch sang phải một cột. Ở cột cuối, bộ mã hóa phát mã 258 mà nó vừa thêm ở cột trước, nên bộ giải mã nhận mã 258 trước khi kịp thêm mục 258. Thuật toán giải mã dưới đây có một nhánh riêng cho trường hợp đó.

::: algorithm Thuật toán 11.20 (Giải mã LZW)
**Đầu vào.** Dòng mã $k_1,\ldots,k_\tau$.

**Đầu ra.** Chuỗi $y$.

**Giả thiết.** Dòng mã được đóng khung và không bị hỏng; hai phía dùng cùng từ điển nạp sẵn và cùng mã đầu 256.

**Các bước.**

1. Nạp sẵn $D[v]$ cho $v=0,\ldots,255$; đặt $\texttt{next\_code}\leftarrow256$. Nếu $\tau =0$, trả về $y$ rỗng.
2. Nếu $k_1\ge256$, báo dòng hỏng và dừng. Ngược lại, đặt $w\leftarrow D[k_1]$ và $y\leftarrow w$.
3. Với mỗi $t=2,\ldots,\tau$, với $k=k_t$:
   1. Nếu $k<\texttt{next\_code}$, đặt $e\leftarrow D[k]$.
   2. Nếu $k=\texttt{next\_code}$, đặt $e\leftarrow w\operatorname{first}(w)$.
   3. Nếu $k>\texttt{next\_code}$, báo dòng hỏng và dừng.
   4. Nối $e$ vào $y$; gán $D[\texttt{next\_code}]\leftarrow w\operatorname{first}(e)$, tăng $\texttt{next\_code}$ thêm 1; đặt $w\leftarrow e$.
4. Trả về $y$.

**Dừng.** Sau $\tau$ mã, hoặc khi gặp mã hỏng.

**Trường hợp biên.** $\tau =1$ chỉ xuất một byte. Ở nhánh 3.2, $\operatorname{first}(e)=\operatorname{first}(w)$, nên mục thêm ở bước 3.4 cũng là $w\operatorname{first}(w)=e$.

**Chi phí.** Mô hình: đếm phép ghi một ký tự, khi mỗi mục lưu (mã cha, ký tự) và cụm được đọc bằng cách đi lên gốc rồi đảo thứ tự.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| 3.1–3.2, dựng $e$ | $\tau -1$ | $\lvert e\rvert$ bước đi lên, hoặc chép $w$ | $O(n)$ |
| 3.4, nối $e$, thêm mục | $\tau -1$ | $\lvert e\rvert$ phép ghi cộng $O(1)$ | $O(n)$ |
:::

Nhánh 3.2 dựa vào khẳng định rằng khi mã chưa có, cụm của nó phải là $w\operatorname{first}(w)$. Nhánh 3.3 dựa vào khẳng định rằng mã lớn hơn $\texttt{next\_code}$ không bao giờ xuất hiện trong một dòng đúng. Hai khẳng định đó được chứng minh như sau.

::: lemma Bổ đề 11.21 (Độ trễ một mục)
**Giả thiết.** $k_1,\ldots,k_\tau$ là dòng mã do Thuật toán 11.19 sinh ra từ $x$, với các cụm $w_t=D[k_t]$; từ điển không giới hạn.

**Kết luận.**

- (a) Với $1\le t<\tau$, bộ mã hóa thêm mục $255+t$ khi phát $k_t$, và $D[255+t]=w_t\operatorname{first}(w_{t+1})$.
- (b) Với $1\le t<\tau$, $k_{t+1}\le255+t$.
- (c) Khi Thuật toán 11.20 đọc $k_{t+1}$, nó đã thêm đúng $t-1$ mục, nên $\texttt{next\_code}=255+t$.

**Điều kiện áp dụng.** Hai phía bắt đầu với $\texttt{next\_code}=256$ và mỗi mã trừ mã cuối thêm đúng một mục.

**Phạm vi.** Bổ đề chỉ đếm mục; nó không nói nội dung các mục của bộ giải mã đúng.
:::

::: proof
**Bước 1 (mục thứ $t$ của bộ mã hóa).** Bộ mã hóa thêm một mục mỗi lần phát mã ở bước 2.2, bắt đầu từ mã 256, nên khi phát $k_t$ nó thêm mục $256+(t-1)=255+t$. Mục đó là $w\,c$ với $w=w_t$ và $c$ là ký tự vừa đọc; sau đó $w\leftarrow c$, nên cụm kế tiếp $w_{t+1}$ bắt đầu bằng $c$, tức $c=\operatorname{first}(w_{t+1})$. Đó là (a).

**Bước 2 (mã lớn nhất có thể).** Khi bộ mã hóa phát $k_{t+1}$, nó đã thêm các mục $256,\ldots,255+t$ ở $t$ lần phát trước, và $w_{t+1}$ là một cụm có trong $D$ lúc đó. Vậy $k_{t+1}\le255+t$. Đó là (b).

**Bước 3 (bộ giải mã).** Thuật toán 11.20 không thêm mục khi đọc $k_1$ và thêm đúng một mục khi đọc mỗi $k_2,\ldots,k_t$. Trước khi đọc $k_{t+1}$, nó đã thêm $t-1$ mục, nên $\texttt{next\_code}=256+(t-1)=255+t$. Đó là (c). $\square$
:::

Điều kiện "mỗi mã trừ mã cuối thêm đúng một mục" được dùng ở Bước 1 và Bước 3. Khi từ điển đầy và hai phía ngừng thêm mục, công thức $255+t$ không còn đúng, và độ trễ một mục chỉ còn giữ tới lúc từ điển đầy.

::: proposition Mệnh đề 11.22 (Mã chưa có trong từ điển của bộ giải mã)
**Giả thiết.** Như Bổ đề 11.21; $1\le t<\tau$.

**Kết luận.** (a) Thuật toán 11.20 không bao giờ đọc mã $k_{t+1}>\texttt{next\_code}$. (b) Nếu $k_{t+1}=\texttt{next\_code}=255+t$ thì $w_{t+1}=w_t\operatorname{first}(w_t)$.

**Điều kiện áp dụng.** Dòng mã do Thuật toán 11.19 sinh ra và không bị hỏng.

**Phạm vi.** Mã $k_{t+1}=255+t$ chỉ xảy ra khi đầu vào có đoạn $\chi\,S\,\chi\,S\,\chi$, với $\chi$ là một ký tự, $S$ là một chuỗi và cụm $\chi\,S$ đã có trong từ điển; trên dòng hỏng, mọi mã đều có thể xuất hiện.
:::

::: proof
**Bước 1 (không có mã lớn hơn).** Theo Bổ đề 11.21(b) và (c), $k_{t+1}\le255+t=\texttt{next\_code}$. Đó là (a).

**Bước 2 (cụm bắt đầu bằng $w_t$).** Nếu $k_{t+1}=255+t$, theo Bổ đề 11.21(a),
$$
\begin{aligned}
w_{t+1}&=D[255+t]\\
&=w_t\operatorname{first}(w_{t+1}),
\end{aligned}
$$
nên $w_{t+1}$ bắt đầu bằng $w_t$.

**Bước 3 (ký tự cuối).** Vì $w_t$ khác rỗng và là tiền tố của $w_{t+1}$, $\operatorname{first}(w_{t+1})=\operatorname{first}(w_t)$. Thay vào đẳng thức của Bước 2 được $w_{t+1}=w_t\operatorname{first}(w_t)$. Đó là (b). $\square$
:::

Đặt $\chi=\operatorname{first}(w_t)$ và $w_t=\chi\,S$. Mệnh đề 11.22(b) cho $w_{t+1}=\chi\,S\,\chi$, nên đầu vào chứa liền nhau $w_tw_{t+1}=\chi\,S\,\chi\,S\,\chi$, đúng dạng "ký tự, chuỗi, ký tự, chuỗi, ký tự" của NG. Ở Ví dụ 11.8(b), $w_t=$ `ab`, $\chi=\mathrm a$, $S=$ `b`. Vì vậy nhánh 3.2 trả về cụm duy nhất phù hợp với dòng mã.

::: theorem Định lý 11.23 (LZW khôi phục đúng)
**Giả thiết.** $x$ là chuỗi byte độ dài $n\ge1$; $k_1,\ldots,k_\tau$ là dòng mã do Thuật toán 11.19 sinh ra từ $x$ với các cụm $w_t=D[k_t]$; Thuật toán 11.20 giải dòng mã đó.

**Kết luận.** Với mọi $t=1,\ldots,\tau$, sau khi Thuật toán 11.20 xử lý $k_t$: (a) $y=w_1\cdots w_t$; (b) $w=w_t$; (c) các mục $256,\ldots,254+t$ của bộ giải mã trùng các mục cùng mã của bộ mã hóa. Nói riêng, Thuật toán 11.20 trả về $y=x$.

**Điều kiện áp dụng.** Hai phía dùng cùng từ điển nạp sẵn, cùng mã đầu 256, cùng quy tắc thêm mục; dòng mã được đóng khung và không bị hỏng trên đường truyền.

**Phạm vi.** Định lý giả thiết từ điển không giới hạn; với từ điển $M$ mục, hai phía còn phải dùng chung quy tắc xử lý từ điển đầy.
:::

::: proof
Quy nạp theo $t$.

**Bước 1 (cơ sở $t=1$).** Khi bộ mã hóa phát $k_1$, từ điển chỉ có các cụm một byte, nên $w_1=x_1$ và $k_1<256$. Bước 2 của Thuật toán 11.20 đặt $w=y=D[k_1]=w_1$. Với $t=1$, dãy mục $256,\ldots,255$ rỗng nên (c) đúng.

**Bước 2 (cụm $e$ đúng).** Giả sử (a), (b), (c) đúng sau $k_t$, $t<\tau$. Khi đọc $k_{t+1}$, theo Bổ đề 11.21(c), $\texttt{next\_code}=255+t$, và theo Mệnh đề 11.22(a), $k_{t+1}\le255+t$.

- Nếu $k_{t+1}<255+t$, mục $k_{t+1}$ có trong từ điển của bộ giải mã và theo (c) trùng mục của bộ mã hóa, nên $e=D[k_{t+1}]=w_{t+1}$.
- Nếu $k_{t+1}=255+t$, nhánh 3.2 cho $e=w\operatorname{first}(w)=w_t\operatorname{first}(w_t)$ theo (b), và theo Mệnh đề 11.22(b) đó là $w_{t+1}$.

**Bước 3 (mục mới đúng).** Bước 3.4 nối $e=w_{t+1}$ vào $y$, cho (a) với $t+1$, và đặt $w=w_{t+1}$, cho (b). Mục thêm có mã $255+t$ và nội dung $w_t\operatorname{first}(w_{t+1})$, theo Bổ đề 11.21(a) trùng mục $255+t$ của bộ mã hóa, cho (c).

**Bước 4 (kết thúc).** Sau $k_\tau$, $y=w_1\cdots w_\tau =x$ theo Định nghĩa 11.18. $\square$
:::

Các điều kiện của định lý được dùng ở Bước 2 và Bước 3 của chứng minh:

- bỏ "cùng mã đầu 256": Bổ đề 11.21(c) không còn đúng và mọi mã cụm lệch nhau; một bộ giải mã dành mã 256 cho kết thúc dòng đọc mã 256 của Ví dụ 11.6 thành lệnh dừng;
- bỏ "không bị hỏng": một mã lớn hơn $\texttt{next\_code}$ có thể xuất hiện, Mệnh đề 11.22(a) không áp dụng, và nhánh 3.3 dừng thay vì trả chuỗi sai;
- bỏ nhánh 3.2 khỏi bộ giải mã: dòng $97,98,256,258$ của Ví dụ 11.8(b) không giải được, vì Bước 2 cần Mệnh đề 11.22(b) cho mã 258.

So với Định lý 11.15, bất biến (c) chậm một mục: sau mã thứ $t$, bộ giải mã LZW mới có các mục tới $254+t$. Giá phải trả cho việc bỏ ký tự thô là nhánh 3.2 cùng Mệnh đề 11.22.

<!-- note-topic-id: lec-11-topic-12 -->
### 4.3 Chi phí và độ rộng mã cố định

Thuật toán 11.19 và 11.20 có cùng cấu trúc với LZ78, nên chi phí thời gian cũng tuyến tính kỳ vọng. Số bit thì khác: mỗi mã chỉ có một trường, rộng $b$ bit với từ điển $M=2^b$ mục.

::: proposition Mệnh đề 11.24 (Chi phí của LZW)
**Giả thiết.** Như Định lý 11.23; dòng có $\tau$ mã, mỗi mã rộng $b$ bit với $M=2^b$ đủ chứa mọi mục; phép tra ở bước 2.1 của Thuật toán 11.19 dùng bảng băm với khóa (mã cha, ký tự), dưới giả thiết băm đều và hệ số tải không quá một hằng $\alpha<1$; mỗi mục lưu (mã, mã cha, ký tự).

**Kết luận.**

- (a) Mã hóa tốn $n-1$ phép tra và $\tau -1$ phép thêm, thời gian kỳ vọng $O(n)$.
- (b) Giải mã tốn $O(n)$ phép ghi ký tự trong trường hợp xấu nhất.
- (c) Bộ nhớ của mỗi phía là $O(M)$ mục.
- (d) Dòng mã dài $\tau b$ bit, với $\tau \le n$.

**Điều kiện áp dụng.** Phần kỳ vọng của (a) cần giả thiết băm đều (CLRS, Chương 11).

**Phạm vi.** Mệnh đề không cho $\tau$ trên một đầu vào cụ thể; $\tau$ nhỏ khi đầu vào có cụm lặp dài.
:::

::: proof
**Bước 1 (mã hóa).** Theo bảng chi phí của Thuật toán 11.19, có $n-1$ phép tra và $\tau -1$ phép thêm, mỗi phép tốn thời gian kỳ vọng $O(1)$ với bảng băm có hệ số tải hằng (CLRS, Chương 11). Vì $\tau \le n$, tổng kỳ vọng là $O(n)$.

**Bước 2 (giải mã).** Mỗi mã $k_t$ với $t\ge2$ cho cụm $e=w_t$; đọc $e$ bằng cách đi lên cây tốn $\lvert w_t\rvert$ bước, rồi ghi $\lvert w_t\rvert$ ký tự theo thứ tự đảo bằng một ngăn xếp (NG, tr.221). Ở nhánh 3.2, $e$ được chép từ $w$ cộng một ký tự, cũng $\lvert w_t\rvert$ phép ghi. Tổng $\sum_t\lvert w_t\rvert=n$.

**Bước 3 (bộ nhớ và số bit).** Từ điển có tối đa $M$ mục, mỗi mục ba trường. Mỗi mã chiếm $b$ bit; mỗi cụm khác rỗng nên $\tau \le n$. $\square$
:::

Trên `aabaacabcabcb`, nếu hai phía thống nhất mã 9 bit, dòng mã dài $10\cdot9=90$ bit, so với $13\cdot8=104$ bit của chuỗi gốc. Một cụm có lợi khi nó dài hơn $9/8$ ký tự, tức ít nhất hai ký tự; ở Ví dụ 11.6 chỉ ba trong mười mã ứng với cụm hai ký tự.

::: remark Nhận xét 11.25 (Trong thực hành)
- **LZW12.** Chương trình LZW12.C của NG dùng mã cố định $b=12$ bit, tức $4\,096$ mã. Nó dành mã 256 cho `END_OF_STREAM`, nên mã cụm đầu tiên là 257 và mọi mã cụm lệch thêm 1 so với mã cụm đầu tiên 256; khi $\texttt{next\_code}$ vượt $4\,095$, chương trình ngừng thêm mục (NG, tr.220–224).
- **Bảng băm.** Mỗi nút của cây lưu (mã, mã cha, ký tự) trong một mảng băm cỡ $5\,021$, một số nguyên tố lớn hơn $2^{12}$ ít nhất 20%; xung đột được giải bằng địa chỉ mở (NG, tr.218–219). Mảng chứa tối đa $4\,095-257+1=3\,839$ cụm, nên hệ số tải $\alpha$ không quá $3\,839/5\,021\approx0{,}765$. Nếu hàm băm thỏa giả thiết băm đều, một lần tìm không thành công cần kỳ vọng không quá $1/(1-\alpha)\approx4{,}25$ lần dò (CLRS, Chương 11). Hàm băm của LZW12.C ghép mã cha với ký tự bằng phép dịch bit và phép XOR, nên không thỏa giả thiết đó; NG chỉ ghi nhận nó chạy khá tốt (NG, tr.219).
- **Tệp ngắn.** Với mã 9 bit, chuỗi 19 ký tự `␣WED␣WE␣WEE␣WEB␣WET` còn 13,5 byte vì chuỗi này có nhiều cụm lặp; trên dữ liệu thật, LZW thường chỉ bắt đầu nén sau khi đã đọc khoảng một trăm byte (NG, tr.215). Mã rộng hơn cho phép từ điển lớn hơn nhưng làm tệp nhỏ thiệt (NG, tr.212).
- **Ứng dụng.** Chương trình `compress` của UNIX dùng LZW (NG, tr.214); định dạng ảnh GIF dùng một biến thể LZW (NG, tr.170).
:::

::: exercise Bài tập 11.5 (LZW cho chuỗi ␣WED␣WE␣WEE␣WEB␣WET)
Chuỗi gồm 19 ký tự `␣WED␣WE␣WEE␣WEB␣WET`, bắt đầu bằng một dấu cách và không có dấu cách ở cuối (NG, tr.214–215). Mã byte: dấu cách $=32$, $\mathrm B=66$, $\mathrm D=68$, $\mathrm E=69$, $\mathrm T=84$, $\mathrm W=87$. (a) Chạy Thuật toán 11.19, lập bảng mã phát và mục thêm. (b) Giải mã dòng mã bằng Thuật toán 11.20 và xác định các mã đi qua nhánh 3.2. (c) Tính số bit của dòng mã với mã 9 bit và so với chuỗi gốc.
:::

::: hint
Mục 256 là `␣W`; ở từ thứ hai, cụm `␣W` đã có mã.
:::

::: solution
**Câu (a).** Dòng mã gồm 12 mã: 32, 87, 69, 68, 256, 69, 260, 261, 257, 66, 260, 84. Các cụm tương ứng là `␣`, `W`, `E`, `D`, `␣W`, `E`, `␣WE`, `E␣`, `WE`, `B`, `␣WE`, `T`. Mười một mục mới là 256 = `␣W`, 257 = `WE`, 258 = `ED`, 259 = `D␣`, 260 = `␣WE`, 261 = `E␣`, 262 = `␣WEE`, 263 = `E␣W`, 264 = `WEB`, 265 = `B␣`, 266 = `␣WET`.

**Câu (b).** Bộ giải mã thêm lần lượt các mục 256–266 như câu (a), chậm hơn bộ mã hóa một mục. Khi đọc mã 260 lần đầu, nó đã có mục 260, vì mục này được thêm khi đọc mã 69 đứng trước; mọi mã đọc vào đều nhỏ hơn $\texttt{next\_code}$, nên không mã nào đi qua nhánh 3.2.

**Câu (c).** $12\cdot9=108$ bit, tức 13,5 byte, so với 19 byte của chuỗi gốc. Năm mã là cụm nhiều ký tự và bảy mã là ký tự đơn (NG, tr.215).

**Kiểm tra lại.** Độ dài các cụm $1+1+1+1+2+1+3+2+2+1+3+1=19$.
:::

::: exercise Bài tập 11.6 (Chuỗi toàn chữ a)
Chuỗi $x$ gồm $n$ chữ $\mathrm a$, mã $\mathrm a\mapsto97$. (a) Với $n=6$, chạy Thuật toán 11.19 và cho dòng mã. (b) Giải mã dòng đó bằng Thuật toán 11.20, chỉ ra mã nào đi qua nhánh 3.2. (c) Chứng minh rằng với $n=\nu(\nu+1)/2$, dòng mã gồm $\nu$ mã và mọi mã từ mã thứ hai đi qua nhánh 3.2.
:::

::: hint
Chứng minh bằng quy nạp rằng cụm thứ $t$ là $\mathrm a^t$, chuỗi gồm $t$ chữ $\mathrm a$.
:::

::: solution
**Câu (a).** Phát 97, thêm 256 = `aa`; khớp `aa`, đọc $\mathrm a$, `aaa` chưa có: phát 256, thêm 257 = `aaa`; khớp `aaa`, hết chuỗi: phát 257. Dòng mã là $97,256,257$, với các cụm `a`, `aa`, `aaa` dài $1+2+3=6$.

**Câu (b).** Đọc 97, xuất `a`. Đọc 256 khi $\texttt{next\_code}=256$: nhánh 3.2 cho `a`+`a` $=$ `aa`, thêm 256 = `aa`. Đọc 257 khi $\texttt{next\_code}=257$: nhánh 3.2 cho `aa`+`a` $=$ `aaa`, thêm 257 = `aaa`. Cả hai mã sau đi qua nhánh 3.2.

**Câu (c).** Khẳng định: nếu còn đủ ký tự, cụm thứ $t$ là $w_t=\mathrm a^t$ và trước khi phát nó, từ điển chứa đúng các cụm toàn chữ $\mathrm a$ dài $1,\ldots,t$. Với $t=1$, từ điển chỉ có `a`. Nếu khẳng định đúng với $t$, cụm khớp dài nhất là $\mathrm a^t$, và mục thêm khi phát nó là $\mathrm a^t\mathrm a=\mathrm a^{t+1}$, nên cụm kế tiếp là $\mathrm a^{t+1}$. Với $n=1+2+\cdots+\nu=\nu(\nu+1)/2$, có đúng $\nu$ cụm. Theo Bổ đề 11.21(a), $\mathrm a^{t+1}$ là mục $255+t$, nên $k_{t+1}=255+t$, bằng $\texttt{next\_code}$ của bộ giải mã theo Bổ đề 11.21(c). Vậy mọi mã từ mã thứ hai đi qua nhánh 3.2.

**Kiểm tra lại.** Với $\nu=3$, $n=6$ và dòng $97,256,257$ khớp câu (a); mã thứ $t+1$ là $255+t$: $256=255+1$, $257=255+2$.
:::

Như vậy, chúng ta đã có LZW với từ điển nạp sẵn (Định nghĩa 11.18, Thuật toán 11.19), bộ giải mã chậm hơn một mục (Bổ đề 11.21) xử lý được mã chưa có nhờ Mệnh đề 11.22, và chứng minh hai phía khôi phục đúng chuỗi (Định lý 11.23) với chi phí kỳ vọng $O(n)$ (Mệnh đề 11.24). Cả ba thuật toán LZ77, LZ78, LZW chỉ khai thác cụm khớp đúng từng ký tự. Trên ảnh chụp, cùng một đường nét ở hai hàng liên tiếp lệch nhau một mức xám ở một hai điểm trong mỗi hai mươi điểm (NG, tr.247), nên cụm khớp đúng rất ngắn và mã từ điển gần như không rút ngắn được ảnh. Với ảnh, phải đổi chính đặc tả: chấp nhận sai lệch nhỏ để bỏ những phần mà mắt không nhận ra.

## 5. Nén ảnh JPEG dựa trên DCT

Ảnh CHEETAH.GS gồm $64\,000$ điểm ảnh xám 8 bit. Bài toán là nén ảnh này, và mọi ảnh của danh mục $1\,000$ ảnh khi giả sử chúng là ảnh xám, xuống một tốc độ bit thấp sao cho sai số RMS của ảnh tái tạo không vượt một ngưỡng chọn trước, với bộ nhớ đủ cho vài hàng điểm ảnh và thời gian tỷ lệ với số điểm ảnh. Ở Ví dụ 11.1, chương trình của NG đưa ảnh xuống $18\,367$ byte với sai số $6{,}9$ mức xám. Chuẩn JPEG làm việc đó qua ba giai đoạn: DCT, lượng tử hóa các hệ số, và mã không mất thông tin các hệ số đã lượng tử (NG, tr.250–251). Chúng ta xét ảnh xám; JPEG nén ảnh màu như ba ảnh xám riêng, mỗi ảnh một thành phần màu như đỏ, lục, lam (NG, tr.264).

![Hai hàng sáu khối. Hàng nén: khối P điểm ảnh 8 bit; dịch mức A = P − 128; DCT F = T A Tᵀ; lượng tử hóa F̂ = F/Q làm tròn, khối viền nét đứt đậm ghi bước duy nhất làm mất dữ liệu; sai phân DC, zigzag; mã hóa độ dài loạt, entropy; ra dòng bit có ghi q. Hàng giải nén chạy ngược: giải mã entropy, độ dài loạt; đảo zigzag, cộng dồn DC; giải lượng tử F̃ = Q F̂; IDCT Ã = Tᵀ F̃ T; cộng 128, làm tròn; khối P̃ cắt về [0, 255].](img/lec-11/note-jpeg-duong-ong.svg)

Trên hình, hàng trên là bộ nén và hàng dưới là bộ giải nén, đi ngược chiều. Mỗi khối của hàng dưới đảo ngược khối đứng thẳng phía trên nó, trừ khối lượng tử hóa: từ $\hat F$ chỉ dựng lại được $\tilde F=Q\hat F$, không dựng lại được $F$. Khi DCT và IDCT tính bằng số thực chính xác, lượng tử hóa là bước duy nhất làm mất thông tin; phần còn lại chỉ là sai số làm tròn nhỏ ở DCT, IDCT và ở điểm ảnh.

<!-- note-topic-id: lec-11-topic-13 -->
### 5.1 Khối $8\times8$, dịch mức và DCT

Theo định nghĩa trực tiếp, mỗi hệ số của phép biến đổi một khối là một tổng qua mọi điểm của khối: với khối $8\times8$, mỗi hệ số có 64 số hạng; với khối $256\times256$, mỗi hệ số có $65\,536$ số hạng và cả khối cần $256^4\approx4{,}3\cdot10^9$ số hạng. Biến đổi cả ảnh một lần vì vậy gần như không làm được, và ngay một khối $256\times256$ cũng đã quá tốn (NG, tr.255). Mặt khác, tương quan giữa các điểm ảnh giảm nhanh theo khoảng cách: các điểm cách nhau mười lăm, hai mươi vị trí hầu như không giúp đoán nhau, nên khối lớn ít lợi thêm. JPEG chọn khối $8\times8$ để cài đặt được bằng công nghệ thời đó; cách làm này gọi là mã hóa theo khối (block coding) (NG, tr.255).

Về mặt ý tưởng, phép biến đổi viết lại khối $8\times8$ thành tổng của 64 mẫu cosine có tần số tăng dần theo hai chiều. Trên ảnh chụp, các điểm trong một khối gần nhau, nên phần lớn năng lượng của khối, tức tổng bình phương các giá trị, dồn vào vài hệ số tần số thấp, còn các hệ số tần số cao nhỏ (NG, tr.254; CMU-L, trang chiếu 9, 12). Để làm rõ, xem hệ số đầu tiên của một khối thật.

::: example Ví dụ 11.9 (Khối $8\times8$ của CHEETAH.GS và hệ số DC)
**Dữ kiện.** Khối Hình 11.9 của NG, một khối điểm ảnh $P=(P_{\xi\eta})$ của ảnh CHEETAH.GS, hàng $\xi$, cột $\eta$ (NG, Hình 11.9, tr.258):
$$
P=\begin{bmatrix}
140&144&147&140&140&155&179&175\\
144&152&140&147&140&148&167&179\\
152&155&136&167&163&162&152&172\\
168&145&156&160&152&155&136&160\\
162&148&156&148&140&136&147&162\\
147&167&140&155&155&140&136&162\\
136&156&123&167&162&144&140&147\\
148&155&136&155&152&147&147&136
\end{bmatrix}.
$$

**Trung bình điểm ảnh.** Tổng tám hàng là $1\,220+1\,217+1\,259+1\,232+1\,199+1\,202+1\,175+1\,176=9\,680$, nên trung bình là $9\,680/64=151{,}25$.

**Dịch mức.** Trừ 128 ở mọi điểm, $A_{\xi\eta}=P_{\xi\eta}-128$; trung bình của khối mới là $151{,}25-128=23{,}25$ và tổng là $64\cdot23{,}25=1\,488$.

**Hệ số DC.** Mẫu tần số 0 của mỗi chiều gồm tám giá trị bằng nhau $1/\sqrt8$, để mẫu có độ dài 1. Hệ số tần số 0 theo cả hai chiều vì vậy là tổng của khối nhân với $\tfrac1{\sqrt8}\cdot\tfrac1{\sqrt8}=\tfrac18$:
$$
\begin{aligned}
F_{00}&=\frac18\sum_{\xi=0}^{7}\sum_{\eta=0}^{7}A_{\xi\eta}\\
&=\frac{1\,488}{8}=186 .
\end{aligned}
$$

**Kiểm tra lại.** Ma trận DCT của khối này trong NG (Hình 11.9) có $186$ ở ô $(0,0)$; $186=8\cdot23{,}25$.
:::

Hệ số $F_{00}$ bằng tám lần độ sáng trung bình của khối sau dịch mức. Các hệ số còn lại đo khối lệch khỏi trung bình theo các mẫu cosine, và cả 64 hệ số được định nghĩa như sau.

::: definition Định nghĩa 11.26 (Dịch mức, DCT và IDCT của khối $8\times8$)
- **Dịch mức** (level shift): với khối điểm ảnh $P=(P_{\xi\eta})$, $P_{\xi\eta}\in\{0,\ldots,255\}$, đặt $A_{\xi\eta}=P_{\xi\eta}-128$, tức $A=P-128$ với giá trị trong $\{-128,\ldots,127\}$ (NG, tr.268).
- **Ma trận DCT** $T=(T_{u\xi})$, $u,\xi\in\{0,\ldots,7\}$:
$$
\begin{aligned}
T_{0\xi}&=\frac1{\sqrt8},\\
T_{u\xi}&=\frac12\cos\frac{(2\xi+1)u\pi}{16}\quad(u\ge1).
\end{aligned}
$$
- **Biến đổi cosine rời rạc** (DCT) của $A$ là ma trận hệ số $F=TAT^{\top}$, tức
$$
\begin{aligned}
F_{uv}&=\gamma(u)\gamma(v)\sum_{\xi=0}^{7}\sum_{\eta=0}^{7}A_{\xi\eta}\\
&\qquad\cdot\cos\tfrac{(2\xi+1)u\pi}{16}\cos\tfrac{(2\eta+1)v\pi}{16},
\end{aligned}
$$
với $\gamma(0)=1/\sqrt8$ và $\gamma(u)=1/2$ khi $u\ge1$. Hệ số $F_{00}$ gọi là **hệ số DC** (DC coefficient).
- **Biến đổi ngược** (inverse DCT, IDCT) của một ma trận hệ số $G$ là $T^{\top}GT$.
:::

Định nghĩa dùng dạng ma trận, như NG ở Hình 11.8 (tr.255–256). Dạng tổng kép thu được khi khai triển $F_{uv}=\sum_\xi\sum_\eta T_{u\xi}A_{\xi\eta}T_{v\eta}$ và thay $T_{u\xi}=\gamma(u)\cos\frac{(2\xi+1)u\pi}{16}$.

Hàng $u$ của $T$ là một mẫu cosine tần số $u$ lấy tại tám điểm $\xi=0,\ldots,7$: hàng 0 là hằng số, hàng 1 đổi dấu một lần, hàng 7 đổi dấu bảy lần. Hệ số $F_{uv}$ đo mức khối giống mẫu tần số $u$ theo chiều dọc và tần số $v$ theo chiều ngang; hàng 0 và cột 0 của $F$ ứng với tần số 0 theo một trong hai chiều (NG, tr.254).

![Tám ô nhỏ xếp hai hàng; ô thứ u vẽ tám cột là các phần tử hàng u của ma trận DCT T tại ξ = 0 đến 7, cột lên là dương, xuống là âm. Ô u = 0: tám cột bằng nhau 0,35. Ô u = 1: giảm từ 0,49 xuống −0,49, đổi dấu một lần. Ô u có u lần đổi dấu. Cột cao nhất khoảng 0,49.](img/lec-11/note-dct-ham-co-so.svg)

Trên hình là tám hàng của $T$. Đếm số lần đổi dấu trong một ô cho đúng chỉ số tần số $u$; ô $u=0$ có tám cột bằng nhau $1/\sqrt8\approx0{,}354$, nên $F_{00}$ là tổng của khối chia cho 8, như ở Ví dụ 11.9. Muốn IDCT đảo ngược DCT, các hàng này phải đôi một vuông góc và có độ dài 1, và việc kiểm điều đó dựa trên một tổng cosine.

::: lemma Bổ đề 11.27 (Tổng cosine)
**Giả thiết.** $\mu\in\{1,\ldots,15\}$ và $\theta=\mu\pi/16$.

**Kết luận.** $\displaystyle\sum_{\xi=0}^{7}\cos\big((2\xi+1)\theta\big)=0$.

**Điều kiện áp dụng.** $\mu$ nguyên, $0<\mu <16$, để $\sin\theta\ne0$ và $\sin16\theta=0$.

**Phạm vi.** Với $\mu=0$ tổng bằng 8; với $\mu=16$ tổng bằng $-8$.
:::

::: proof
**Bước 1 (tích với $2\sin\theta$ là hiệu hai sin).** Vì $0<\theta<\pi$, $\sin\theta\ne0$. Theo công thức biến tích thành tổng với góc $\theta$ và $\omega=(2\xi+1)\theta$,
$$
\begin{aligned}
&2\sin\theta\cos\big((2\xi+1)\theta\big)\\
&\quad=\sin\big((2\xi+2)\theta\big)-\sin(2\xi\theta).
\end{aligned}
$$

**Bước 2 (tổng xếp lồng bằng $\sin\mu\pi=0$).** Cộng theo $\xi=0,\ldots,7$, các số hạng giữa triệt tiêu từng cặp:
$$
\begin{aligned}
&2\sin\theta\sum_{\xi=0}^{7}\cos\big((2\xi+1)\theta\big)\\
&\quad=\sum_{\xi=0}^{7}\Big(\sin\big((2\xi+2)\theta\big)-\sin(2\xi\theta)\Big)\\
&\quad=\sin16\theta-\sin0=\sin\mu\pi=0 .
\end{aligned}
$$

**Bước 3 (tổng cosine bằng 0).** Chia hai vế cho $2\sin\theta\ne0$ được kết luận. $\square$
:::

::: proposition Mệnh đề 11.28 (DCT trực chuẩn)
**Giả thiết.** $T$ là ma trận DCT của Định nghĩa 11.26; $A$ là ma trận thực $8\times8$ và $F=TAT^{\top}$.

**Kết luận.** (a) $TT^{\top}=I$. (b) IDCT đảo ngược DCT: $T^{\top}FT=A$. (c) Bảo toàn năng lượng (energy conservation): $\sum_{u,v}F_{uv}^2=\sum_{\xi,\eta}A_{\xi\eta}^2$.

**Điều kiện áp dụng.** Tính toán trên số thực chính xác.

**Phạm vi.** Mệnh đề nói DCT không làm mất thông tin; nó cũng không rút ngắn dữ liệu: với $A$ nguyên trong $[-128;127]$, các hệ số nằm trong khoảng từ $-1\,024$ tới $1\,023$ và cần 11 bit mỗi hệ số, nhiều hơn 8 bit mỗi điểm ảnh (NG, tr.258).
:::

::: proof
**Bước 1 (tích hai hàng).** Phần tử $(u,v)$ của $TT^{\top}$ là $\sum_{\xi=0}^{7}T_{u\xi}T_{v\xi}$. Xét ba trường hợp.

- $u=v=0$: $\sum_\xi\tfrac18=1$.
- $u=0$, $v\ge1$: $\tfrac1{\sqrt8}\cdot\tfrac12\sum_\xi\cos\frac{(2\xi+1)v\pi}{16}=0$ theo Bổ đề 11.27 với $\mu=v\in\{1,\ldots,7\}$; trường hợp $u\ge1$, $v=0$ tương tự.
- $u,v\ge1$: theo công thức $2\cos\theta\cos\omega=\cos(\theta-\omega)+\cos(\theta+\omega)$,
$$
\begin{aligned}
&\sum_\xi T_{u\xi}T_{v\xi}\\
&\quad=\frac18\sum_\xi\cos\frac{(2\xi+1)(u-v)\pi}{16}\\
&\qquad+\frac18\sum_\xi\cos\frac{(2\xi+1)(u+v)\pi}{16}.
\end{aligned}
$$
Vì $2\le u+v\le14$, tổng thứ hai bằng 0 theo Bổ đề 11.27. Nếu $u\ne v$, $\lvert u-v\rvert\in\{1,\ldots,6\}$ và cosin là hàm chẵn, nên tổng thứ nhất cũng bằng 0. Nếu $u=v$, tổng thứ nhất là $\sum_\xi\cos0=8$, và phần tử bằng $8/8=1$.

Vậy $TT^{\top}=I$, đó là (a).

**Bước 2 (đảo ngược).** Với ma trận vuông, $TT^{\top}=I$ kéo theo $T^{\top}T=I$. Do đó
$$
T^{\top}FT=T^{\top}T\,A\,T^{\top}T=A,
$$
đó là (b).

**Bước 3 (năng lượng).** Tổng bình phương các phần tử của một ma trận $X$ bằng $\operatorname{tr}(XX^{\top})$. Dùng $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ và $T^{\top}T=I$:
$$
\begin{aligned}
\sum_{u,v}F_{uv}^2&=\operatorname{tr}\big(TAT^{\top}\,TA^{\top}T^{\top}\big)\\
&=\operatorname{tr}\big(TAA^{\top}T^{\top}\big)\\
&=\operatorname{tr}\big(AA^{\top}T^{\top}T\big)\\
&=\operatorname{tr}(AA^{\top})=\sum_{\xi,\eta}A_{\xi\eta}^2,
\end{aligned}
$$
đó là (c). $\square$
:::

Ma trận $T^{\top}$ cũng trực chuẩn, nên (c) áp dụng được cho IDCT: với mọi ma trận $G$, tổng bình phương các phần tử của $T^{\top}GT$ bằng tổng bình phương các phần tử của $G$. Giả thiết "số thực chính xác" có vai trò: chương trình của NG làm tròn mỗi hệ số DCT về số nguyên, và trên khối của Ví dụ 11.9, IDCT của ma trận đã làm tròn cộng 128 rồi làm tròn lệch khối gốc tối đa 1 mức xám. NG gọi bước DCT là không mất thông tin ngoài sai số làm tròn nhỏ (NG, tr.260).

::: example Ví dụ 11.10 (Năng lượng của khối CHEETAH.GS)
**Dữ kiện.** Khối $A=P-128$ của Ví dụ 11.9. Ma trận DCT của nó, làm tròn tới số nguyên:
$$
F\approx\begin{bmatrix}
186&-18&15&-9&23&-9&-14&-19\\
21&-34&26&-9&-11&11&14&7\\
-10&-24&-2&6&-18&3&-20&-1\\
-8&-5&14&-15&-8&-3&-3&8\\
-3&10&8&1&-11&18&18&15\\
4&-2&-18&8&8&-4&1&-7\\
9&1&-3&4&-1&-7&-1&-2\\
0&-8&-2&2&1&4&-6&0
\end{bmatrix}.
$$

**Năng lượng của khối.** $\sum_{\xi,\eta}A_{\xi\eta}^2=43\,372$.

**Năng lượng của hệ số.** Với hệ số chính xác, $\sum_{u,v}F_{uv}^2=43\,372$, đúng như Mệnh đề 11.28(c). Với các hệ số đã làm tròn ở trên, tổng là $43\,333$; chênh $39$, tức dưới $0{,}1\%$, do làm tròn.

**Năng lượng dồn về tần số thấp.** Riêng hệ số DC có $186^2=34\,596$, khoảng $80\%$ của $43\,333$. Sáu hệ số có $u+v\le2$ chiếm $36\,842$, khoảng $85\%$; hai mươi tám hệ số có $u+v\ge8$ chỉ chiếm $1\,925$, khoảng $4{,}4\%$.

**Kiểm tra lại.** $F_{00}=186$ trùng Ví dụ 11.9. Hàng 0 của $F$ tính chính xác là $186$; $-18{,}00$; $14{,}78$; $-8{,}98$; $23{,}25$; $-9{,}23$; $-13{,}97$; $-18{,}94$, làm tròn ra hàng 0 ở trên.
:::

DCT không rút ngắn khối, nhưng chuyển 64 điểm ảnh gần như ngang nhau thành 64 hệ số rất không đều: một hệ số lớn và nhiều hệ số nhỏ. Giữ nguyên các hệ số chỉ tốn thêm bit theo phần Phạm vi của Mệnh đề 11.28; để nén, phải giảm độ chính xác của chúng.

<!-- note-topic-id: lec-11-topic-14 -->
### 5.2 Lượng tử hóa và sai số tái tạo

Bài toán là chọn cho mỗi hệ số của ma trận $F$ ở Ví dụ 11.10 một số chia, chia rồi làm tròn để giảm số bit, và chặn sai số mà phép làm tròn gây ra trên điểm ảnh. Hệ số càng xa ô $(0,0)$ thì đóng góp vào ảnh càng ít, nên được chia cho số càng lớn (NG, tr.259).

Một cách trực quan, lượng tử hóa giống đo một đoạn thẳng bằng thước có vạch thưa: mọi độ dài giữa hai vạch được ghi bằng vạch gần nhất, và sai số đo không quá nửa khoảng cách giữa hai vạch. Khoảng cách đó là bước lượng tử, và mỗi hệ số có thước riêng.

Ví dụ, hệ số $F_{01}=-18$ chia cho 5 được $-3{,}6$, làm tròn thành $-4$, nhân lại với 5 được $-20$, lệch 2. Mọi hệ số trong $(-22{,}5;\,-17{,}5]$ cho cùng kết quả $-4$, nên từ $-4$ không dựng lại được $-18$. Hệ số $F_{77}=0$ chia cho 31 được 0 và tái tạo đúng.

::: definition Định nghĩa 11.29 (Ma trận lượng tử, lượng tử hóa và giải lượng tử)
- Một **ma trận lượng tử** (quantization matrix) là ma trận $Q=(Q_{uv})$ các số nguyên dương; $Q_{uv}$ gọi là **bước lượng tử** (step size, quantum) của hệ số $(u,v)$. Với **hệ số chất lượng** (quality factor) $q\ge0$ nguyên, ma trận của NG là
$$
Q_{uv}=1+(1+u+v)\,q .
$$
- **Lượng tử hóa** (quantization) hệ số $F_{uv}$ cho số nguyên $\hat F_{uv}=\operatorname{round}(F_{uv}/Q_{uv})$, trong đó $\operatorname{round}$ làm tròn tới số nguyên gần nhất, và làm tròn xa số 0 khi phần lẻ đúng bằng $\tfrac12$.
- **Giải lượng tử** (dequantization) cho $\tilde F_{uv}=Q_{uv}\hat F_{uv}$.
:::

Bước lượng tử tăng dần theo đường chéo $u+v$: các ô cùng đường chéo có cùng bước, và mỗi đường chéo xa gốc hơn có bước lớn hơn đường trước đúng $q$ (NG, tr.260). Với $q=0$, mọi bước bằng 1 và lượng tử hóa chỉ làm tròn. Hệ số $q$ được ghi vào tệp nén (Nhận xét 11.3), nên bộ giải nén dựng lại đúng $Q$. ISO công bố một bộ bảng lượng tử chuẩn, dựng từ thử nghiệm của các thành viên ủy ban JPEG (NG, tr.259–260); bảng đó được chia đều cho một hệ số chất lượng (CMU-L, trang chiếu 15). Các ví dụ dùng ma trận của NG.

::: example Ví dụ 11.11 (Lượng tử hóa khối CHEETAH.GS ở hệ số chất lượng 2)
**Dữ kiện.** Ma trận $F$ của Ví dụ 11.10 và ma trận lượng tử với $q=2$, $Q_{uv}=3+2(u+v)$ (NG, Hình 11.10, tr.260):
$$
Q=\begin{bmatrix}
3&5&7&9&11&13&15&17\\
5&7&9&11&13&15&17&19\\
7&9&11&13&15&17&19&21\\
9&11&13&15&17&19&21&23\\
11&13&15&17&19&21&23&25\\
13&15&17&19&21&23&25&27\\
15&17&19&21&23&25&27&29\\
17&19&21&23&25&27&29&31
\end{bmatrix}.
$$

**Một số ô.**

- Ô $(0,0)$: $186/3=62$, nên $\hat F_{00}=62$.
- Ô $(0,1)$: $-18/5=-3{,}6$, làm tròn được $-4$.
- Ô $(0,2)$: $15/7\approx2{,}14$, được $2$.
- Ô $(0,7)$: $-19/17\approx-1{,}12$, được $-1$.
- Ô $(4,7)$: $15/25=0{,}6$, được $1$.
- Ô $(1,1)$: $-34/7\approx-4{,}86$, được $-5$.
- Ô $(2,2)$: $-2/11\approx-0{,}18$, được $0$.

**Cả khối.** Làm như vậy với cả 64 ô được ma trận số nguyên lượng tử
$$
\hat F=\begin{bmatrix}
62&-4&2&-1&2&-1&-1&-1\\
4&-5&3&-1&-1&1&1&0\\
-1&-3&0&0&-1&0&-1&0\\
-1&0&1&-1&0&0&0&0\\
0&1&1&0&-1&1&1&1\\
0&0&-1&0&0&0&0&0\\
1&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&0
\end{bmatrix}.
$$

**Diễn giải.** Có 30 số khác 0 và 34 số 0; hàng cuối toàn số 0, và giá trị tuyệt đối lớn nhất ngoài ô DC là 5.

**Kiểm tra lại.** $30+34=64$. Ô $(7,7)$ có $F_{77}=0$ và $Q_{77}=31$; một hệ số ở ô này chỉ khác 0 sau lượng tử hóa khi $\lvert F_{77}\rvert\ge31/2$, tức ít nhất 16 với hệ số nguyên (NG, tr.260).
:::

Phép chia và làm tròn ở Ví dụ 11.11 không đảo ngược được: biết $\hat F_{01}=-4$ và $Q_{01}=5$, ta chỉ biết $F_{01}\in(-22{,}5;\,-17{,}5]$.

::: proposition Mệnh đề 11.30 (Lượng tử hóa không khả nghịch và sai số mỗi hệ số)
**Giả thiết.** $F_{uv}$ là số thực, $Q_{uv}\ge1$ nguyên; $\hat F_{uv}$, $\tilde F_{uv}$ như Định nghĩa 11.29.

**Kết luận.**

- (a) Với mỗi số nguyên $h\ge1$, mọi $F_{uv}$ trong $[Q_{uv}(h-\tfrac12);\,Q_{uv}(h+\tfrac12))$ cho cùng $\hat F_{uv}=h$; khoảng tương ứng với $h\le-1$ đối xứng qua 0, và $\hat F_{uv}=0$ đúng khi $\lvert F_{uv}\rvert<Q_{uv}/2$. Lượng tử hóa là ánh xạ nhiều–một.
- (b) $\lvert F_{uv}-\tilde F_{uv}\rvert\le Q_{uv}/2$.
- (c) Nếu $\lvert F_{uv}\rvert<Q_{uv}/2$ thì $\hat F_{uv}=0$; khi tăng $Q_{uv}$, một hệ số đã về 0 vẫn bằng 0.

**Điều kiện áp dụng.** Làm tròn tới số nguyên gần nhất như Định nghĩa 11.29.

**Phạm vi.** Với phép cắt về 0 thay cho làm tròn, (b) thành $\lvert F_{uv}-\tilde F_{uv}\rvert<Q_{uv}$ và (c) thành "$\lvert F_{uv}\rvert<Q_{uv}$".
:::

::: proof
**Bước 1 (mỗi giá trị $h$ ứng với một khoảng).** Với $h\ge1$, $\operatorname{round}(z)=h$ khi và chỉ khi $h-\tfrac12\le z<h+\tfrac12$, vì phần lẻ $\tfrac12$ được làm tròn xa 0, tức lên $h$. Với $z=F_{uv}/Q_{uv}$ và $Q_{uv}>0$, điều này tương đương $F_{uv}\in[Q_{uv}(h-\tfrac12);\,Q_{uv}(h+\tfrac12))$. Trường hợp $h\le-1$ đối xứng, và $\operatorname{round}(z)=0$ khi và chỉ khi $\lvert z\rvert<\tfrac12$. Mỗi khoảng chứa vô số số thực nhưng cho một giá trị $h$, đó là (a).

**Bước 2 (sai số không quá nửa bước).** Với mọi $z$, $\lvert z-\operatorname{round}(z)\rvert\le\tfrac12$. Nhân với $Q_{uv}$:
$$
\begin{aligned}
\lvert F_{uv}-\tilde F_{uv}\rvert&=Q_{uv}\,\Big\lvert\frac{F_{uv}}{Q_{uv}}-\hat F_{uv}\Big\rvert\\
&\le\frac{Q_{uv}}2,
\end{aligned}
$$
đó là (b).

**Bước 3 (hệ số nhỏ về 0).** Nếu $\lvert F_{uv}\rvert<Q_{uv}/2$ thì $\lvert F_{uv}/Q_{uv}\rvert<\tfrac12$ nên $\hat F_{uv}=0$. Với $Q'_{uv}\ge Q_{uv}$, $\lvert F_{uv}\rvert<Q_{uv}/2\le Q'_{uv}/2$, nên hệ số vẫn về 0. Đó là (c). $\square$
:::

Mệnh đề không nói mọi hệ số đều bị sai lệch: một hệ số là bội của bước được tái tạo đúng. Khối $8\times8$ đầu tiên của CHEETAH.GS có hệ số $-84$ ở ô $(2,0)$, với bước 7; $-84/7=-12$ đúng là số nguyên, nên $\tilde F_{20}=-84$ (NG, Hình 11.11, tr.261). Ở cùng khối, ô $(0,2)$ có hệ số $-9$ và bước 7: $-9/7\approx-1{,}29$ làm tròn thành $-1$, tái tạo $-7$, lệch 2, không quá $7/2$.

Một nhầm lẫn thường gặp là coi lượng tử hóa "chỉ làm tròn" nên không đáng kể: với bước 31 ở ô $(7,7)$, mọi hệ số từ $-15$ tới $15$ đều thành 0.

Sai số trên từng hệ số bị chặn bởi nửa bước. Điểm ảnh tái tạo được tính từ cả 64 hệ số qua IDCT, nên cần biết sai số trên hệ số chuyển thành sai số trên điểm ảnh ra sao; Mệnh đề 11.28(c) cho câu trả lời.

::: theorem Định lý 11.31 (Sai số tái tạo của một khối bị chặn bởi bước lượng tử)
**Giả thiết.** $A$ là khối $8\times8$ sau dịch mức; $F=TAT^{\top}$ tính chính xác; $\hat F$, $\tilde F$ theo Định nghĩa 11.29 với ma trận lượng tử $Q$; khối tái tạo là $\tilde A=T^{\top}\tilde FT$, chưa làm tròn và chưa cắt.

**Kết luận.**
$$
\begin{aligned}
E_{\mathrm{RMS}}(A,\tilde A)&=\sqrt{\frac1{64}\sum_{u,v}\big(F_{uv}-\tilde F_{uv}\big)^2}\\
&\le\frac12\sqrt{\frac1{64}\sum_{u,v}Q_{uv}^2}.
\end{aligned}
$$

**Điều kiện áp dụng.** DCT và IDCT tính bằng số thực chính xác; lượng tử hóa làm tròn tới số nguyên gần nhất.

**Phạm vi.** Định lý chặn sai số, không cho số bit: số bit phụ thuộc các bước mã hóa sau lượng tử hóa và đo trên từng ảnh. Cận đạt được khi mọi hệ số lệch đúng nửa bước. Với phép cắt về 0, cận nhân đôi.
:::

::: proof
**Bước 1 (sai số khối là IDCT của sai số hệ số).** Theo Mệnh đề 11.28(b), $A=T^{\top}FT$. Do đó
$$
\begin{aligned}
A-\tilde A&=T^{\top}FT-T^{\top}\tilde FT\\
&=T^{\top}(F-\tilde F)T .
\end{aligned}
$$

**Bước 2 (bảo toàn năng lượng).** Ma trận $T^{\top}$ trực chuẩn, nên áp dụng Mệnh đề 11.28(c) cho $T^{\top}$ và $G=F-\tilde F$:
$$
\begin{aligned}
&\sum_{\xi,\eta}(A_{\xi\eta}-\tilde A_{\xi\eta})^2\\
&\quad=\sum_{u,v}(F_{uv}-\tilde F_{uv})^2 .
\end{aligned}
$$
Chia cho 64 và lấy căn được đẳng thức của kết luận.

**Bước 3 (chặn từng hệ số).** Theo Mệnh đề 11.30(b), $(F_{uv}-\tilde F_{uv})^2\le Q_{uv}^2/4$ với mọi $(u,v)$. Cộng lại, chia cho 64 và lấy căn được bất đẳng thức. $\square$
:::

Định lý tách rõ hai việc. Đẳng thức nói rằng sai số trung bình trên điểm ảnh bằng đúng sai số trung bình trên hệ số, nhờ tính trực chuẩn của DCT. Bất đẳng thức nói rằng sai số trên hệ số bị chặn bởi bước lượng tử. Mỗi giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều làm cận thay đổi:

- Bỏ "DCT trực chuẩn": Bước 2 không còn đúng. Ví dụ, với biến đổi $F'=\tfrac12TAT^{\top}$, có nghịch đảo $A=2T^{\top}F'T$, cùng một sai số lượng tử trên $F'$ thành sai số gấp đôi trên điểm ảnh.
- Bỏ "làm tròn tới số nguyên gần nhất": với phép cắt về 0, Bước 3 chỉ cho $(F_{uv}-\tilde F_{uv})^2<Q_{uv}^2$, nên cận nhân đôi.
- Bỏ "chưa làm tròn và chưa cắt": điểm ảnh tái tạo $\tilde P$ là $\tilde A+128$ làm tròn rồi cắt về $[0;255]$. Phép cắt không làm sai số của một điểm tăng lên, vì điểm gốc nằm trong $[0;255]$. Phép làm tròn đổi mỗi điểm không quá $\tfrac12$, nên theo bất đẳng thức tam giác cho chuẩn Euclid, $E_{\mathrm{RMS}}(P,\tilde P)$ lớn hơn $E_{\mathrm{RMS}}(A,\tilde A)$ không quá $\tfrac12$.

Khi $Q$ dựng từ hệ số chất lượng $q$, cận của Định lý 11.31 viết là $\beta(q)$. Với $q=2$, $\sum_{u,v}Q_{uv}^2=21\,184$, nên $\beta(2)=\tfrac12\sqrt{21\,184/64}\approx9{,}10$ mức xám.

::: example Ví dụ 11.12 (IDCT và sai số của khối CHEETAH.GS)
**Dữ kiện.** Ma trận $\hat F$ và ma trận $Q$ với $q=2$ của Ví dụ 11.11; khối gốc $P$ của Ví dụ 11.9.

**Giải lượng tử.** $\tilde F_{uv}=Q_{uv}\hat F_{uv}$; hàng 0 là 186, −20, 14, −9, 22, −13, −15, −17, so với hàng 0 của $F$ là 186, −18, 15, −9, 23, −9, −14, −19.

**Sai số trên hệ số.** Với $F$ nguyên của Ví dụ 11.10, $\sum_{u,v}(F_{uv}-\tilde F_{uv})^2=1\,086$, nên sai số RMS trên hệ số là $\sqrt{1\,086/64}\approx4{,}12$. Tỷ số $\lvert F_{uv}-\tilde F_{uv}\rvert/Q_{uv}$ lớn nhất là $8/17\approx0{,}47$, ở ô $(3,4)$: $F_{34}=-8$, $Q_{34}=17$, $\tilde F_{34}=0$; mọi ô thỏa Mệnh đề 11.30(b). Với $F$ tính chính xác, chưa làm tròn, sai số RMS trên hệ số là $4{,}18$.

**IDCT, cộng 128, làm tròn, cắt.** Bốn phép này cho khối tái tạo
$$
\tilde P=\begin{bmatrix}
142&143&155&141&133&154&179&179\\
139&152&129&151&144&154&163&181\\
150&156&139&166&162&163&154&172\\
164&145&160&153&151&153&145&154\\
168&150&156&145&140&140&141&159\\
148&164&133&164&158&140&136&163\\
130&159&123&164&165&140&135&146\\
148&156&140&148&159&146&153&141
\end{bmatrix}.
$$
Hàng 0 của khối gốc là 140, 144, 147, 140, 140, 155, 179, 175; hiệu $P_{0\eta}-\tilde P_{0\eta}$ là −2, 1, −8, −1, 7, 1, 0, −4.

**Sai số trên điểm ảnh.** $E_{\mathrm{RMS}}(P,\tilde P)\approx4{,}21$ mức xám; điểm lệch nhiều nhất lệch 11 mức.

**Diễn giải.** Sai số $4{,}21$ nhỏ hơn nhiều so với cận $9{,}10$ của Định lý 11.31: cận giả sử mọi hệ số lệch đúng nửa bước, còn ở đây nhiều hệ số lệch ít hơn. Trước khi làm tròn điểm ảnh, $E_{\mathrm{RMS}}(A,\tilde A)=4{,}18$, bằng đúng sai số RMS trên hệ số tính với $F$ chính xác, như đẳng thức của Định lý 11.31. Chênh lệch giữa $4{,}21$, $4{,}18$ và $4{,}12$ đến từ hai phép làm tròn nằm ngoài giả thiết của định lý: làm tròn các hệ số DCT và làm tròn điểm ảnh.

**Kiểm tra lại.** $4{,}12<9{,}10$ trên hệ số và $4{,}21<9{,}10$ trên điểm ảnh. Tốc độ bit không đo được trên một khối mà chỉ trên cả ảnh: với $q=2$, NG đo được $2{,}30$ bit mỗi điểm và sai số $6{,}9$ trên cả CHEETAH.GS (Ví dụ 11.1).
:::

<!-- note-topic-id: lec-11-topic-15 -->
### 5.3 Sai phân DC, thứ tự zigzag và mã độ dài loạt

Ma trận $\hat F$ của Ví dụ 11.11 có 30 số khác 0 rải trong 64 ô: các số khác 0 tập trung ở góc trên trái, hàng cuối toàn số 0. Trên cả ảnh, các khối kề nhau thường có độ sáng trung bình gần nhau, nên hệ số DC của chúng gần nhau (NG, tr.261). Bài toán là sắp các số nguyên đã lượng tử của mỗi khối thành một dãy sao cho các số 0 đứng liền nhau thành loạt dài, rồi mã dãy đó mà không làm mất thêm thông tin.

Về mặt ý tưởng, nếu đọc các ô theo đường chéo từ góc trên trái xuống góc dưới phải, các hệ số lớn đứng đầu dãy và các số 0 dồn về cuối; thay mỗi loạt số 0 bằng độ dài của loạt sẽ rút ngắn dãy. Với hệ số DC, ghi hiệu so với khối trước cho một số nhỏ (NG, tr.261–262). Kết quả được mã tiếp bằng một mã không mất thông tin gọi là mã entropy (entropy coding), như mã Huffman hay mã số học.

Trên ma trận $\hat F$ của khối Hình 11.9 (Ví dụ 11.11), đọc theo đường chéo, mười bốn số đầu là 62, −4, 4, −1, −5, 2, −1, 3, −3, −1, 0, 0, 0, −1. Ba số 0 liền nhau đứng trước $-1$ được ghi gọn thành "ba số 0, rồi $-1$", tức bộ $(3,1,-1)$ với 1 là số bit của $\lvert-1\rvert$. Nếu khối liền trước có hệ số DC lượng tử bằng 60, khối này chỉ cần ghi hiệu $62-60=2$ thay cho 62.

::: definition Định nghĩa 11.32 (Hệ số AC, sai phân DC, thứ tự zigzag và mã độ dài loạt)
- **Hệ số AC** (AC coefficients) là 63 hệ số $\hat F_{uv}$ với $(u,v)\ne(0,0)$.
- Các khối của ảnh được xử lý theo thứ tự đọc: từng dải 8 hàng từ trên xuống, trong mỗi dải từ trái sang phải. Với các khối $\kappa=1,2,\ldots,K$ theo thứ tự đó, **sai phân DC** (DC difference) là $\delta_1=\hat F_{00}^{(1)}$ và $\delta_\kappa=\hat F_{00}^{(\kappa)}-\hat F_{00}^{(\kappa-1)}$ với $\kappa\ge2$, trong đó chỉ số trên chỉ khối.
- **Thứ tự zigzag** (zig-zag sequence) xếp 64 ô $(u,v)$ theo đường chéo, tức theo $u+v$ tăng dần từ 0 tới 14; trong một đường chéo, $u$ tăng dần khi $u+v$ lẻ và giảm dần khi $u+v$ chẵn. Vị trí của một ô trong thứ tự này, đếm từ 1, gọi là **vị trí zigzag** của ô.
- **Dãy của khối** $\kappa$ gồm 64 số nguyên: $\delta_\kappa$ ở vị trí 1, rồi 63 hệ số AC theo vị trí zigzag 2 tới 64.
- **Mã độ dài loạt** (run-length encoding, RLE) thay dãy của mỗi khối bằng một dãy bộ, đọc từ đầu tới khi đủ 64 số:
  - mỗi số khác 0 $a$ cho một bộ ba $(r,s,a)$, với $r$ là số các số 0 đứng ngay trước $a$ kể từ số khác 0 trước đó trong khối, hoặc từ đầu khối, và $s=\lfloor\log_2\lvert a\rvert\rfloor+1$ là số bit để ghi $\lvert a\rvert$ (NG, tr.263–264);
  - nếu khối kết thúc bằng một loạt $r$ số 0, khối được đóng bằng bộ $(r,0)$, trong đó số bit 0 báo một loạt số 0 không kèm biên độ; bộ đóng khối này là quy ước của chương.
:::

Thứ tự zigzag đi theo đúng các đường chéo mà trên đó bước lượng tử bằng nhau, nên nó đọc các hệ số theo bước tăng dần (NG, tr.262–263). Trong bộ ba, $r$ và $s$ là hai số nhỏ, $a$ được ghi bằng đúng $s$ bit: $s=1$ cho $\pm1$, $s=2$ cho $\pm2,\pm3$, $s=3$ cho $\pm4,\ldots,\pm7$, và tiếp tục như vậy tới $s=10$ cho các hệ số AC có giá trị tuyệt đối từ 512 tới $1\,023$ (NG, tr.264). Sai phân DC là hiệu của hai hệ số DC nên có thể cần tới $s=11$.

::: proposition Mệnh đề 11.33 (Các bước sau lượng tử hóa khôi phục đúng)
**Giả thiết.** Mỗi khối có đúng 64 số; bộ giải mã nhận, theo thứ tự khối, các bộ của mã độ dài loạt theo Định nghĩa 11.32.

**Kết luận.** Bộ giải mã dựng lại đúng dãy 64 số của mỗi khối, rồi đúng ma trận $\hat F^{(\kappa)}$ của mọi khối $\kappa$. Do đó trong đường ống dịch mức, DCT, lượng tử hóa, sai phân DC, zigzag, mã độ dài loạt và mã entropy, lượng tử hóa là bước duy nhất làm mất dữ liệu.

**Điều kiện áp dụng.** Các bộ được truyền đúng; khi chúng được mã tiếp bằng mã Huffman (Định nghĩa 10.1, 10.5) hoặc mã số học (Định lý 10.34), bộ giải mã cũng lấy lại đúng các bộ.

**Phạm vi.** Mệnh đề không nói gì về số bit của dãy bộ; số đó phụ thuộc số loạt và cách mã $(r,s)$.
:::

::: proof
**Bước 1 (dãy của khối được dựng lại).** Bộ giải mã đọc các bộ của khối theo thứ tự. Một bộ ba $(r,s,a)$ cho $r$ số 0 rồi số $a$; một bộ $(r,0)$ cho $r$ số 0. Bộ giải mã dừng khối khi đã có đủ 64 số, nên biết bộ kế tiếp thuộc khối sau. Mỗi số được ghi đúng vị trí vì $r$ đếm đúng các số 0 đứng trước.

**Bước 2 (các hệ số AC về đúng ô).** Mỗi ô $(u,v)$ thuộc đúng một đường chéo và có đúng một vị trí trong đường chéo đó, nên thứ tự zigzag là một song ánh từ 64 ô lên các vị trí $1,\ldots,64$. Đặt số ở vị trí $i$ vào ô có vị trí zigzag $i$ cho lại các hệ số AC.

**Bước 3 (hệ số DC được dựng lại).** $\hat F_{00}^{(\kappa)}=\delta_1+\delta_2+\cdots+\delta_\kappa$, vì tổng xếp lồng $\sum_{i\le\kappa}\delta_i$ triệt tiêu mọi số hạng trừ $\hat F_{00}^{(\kappa)}$. Bộ giải mã cộng dồn các $\delta_\kappa$ theo thứ tự khối. $\square$
:::

Bước DCT đứng trước lượng tử hóa chỉ mất phần làm tròn nhỏ và bước mã hóa đứng sau không mất gì, nên lượng tử hóa là chỗ duy nhất dữ liệu bị bỏ (NG, tr.260). Giả thiết "mỗi khối có đúng 64 số" được dùng ở Bước 1: nhờ nó, bộ giải mã biết khi nào một khối kết thúc, và bộ $(r,0)$ đủ để điền các số 0 cuối khối.

::: example Ví dụ 11.13 (Dãy zigzag và loạt số 0 của khối đã lượng tử)
**Dữ kiện.** Ma trận $\hat F$ của Ví dụ 11.11 cho khối Hình 11.9. Giả sử khối liền trước có $\hat F_{00}=60$, nên sai phân DC là $\delta=62-60=2$.

**Thứ tự zigzag.** Mười lăm vị trí đầu là các ô $(0,0)$, $(0,1)$, $(1,0)$, $(2,0)$, $(1,1)$, $(0,2)$, $(0,3)$, $(1,2)$, $(2,1)$, $(3,0)$, $(4,0)$, $(3,1)$, $(2,2)$, $(1,3)$, $(0,4)$; ô $(0,2)$ ở vị trí 6 và ô $(0,4)$ ở vị trí 15.

**Dãy 64 số.**

- vị trí 1–8: 2, −4, 4, −1, −5, 2, −1, 3;
- vị trí 9–16: −3, −1, 0, 0, 0, −1, 2, −1;
- vị trí 17–24: −1, 0, 1, 1, 0, 1, 0, 1;
- vị trí 25–32: −1, −1, 1, −1, −1, 1, 0, 0;
- vị trí 33–40: 0, −1, 0, 0, 0, 0, 0, −1;
- vị trí 41–48: 0, −1, 0, 0, 0, 1, 0, 0;
- vị trí 49–56: 0, 0, 0, 0, 1, 0, 1, 0;
- vị trí 57–64: 0, 0, 0, 0, 0, 0, 0, 0.

**Bộ ba của mười lăm vị trí đầu.** Sai phân DC cho $(0,2,2)$ vì $2\le2<2^2$. Các vị trí 2–10 không có số 0 xen giữa: $(0,3,-4)$, $(0,3,4)$, $(0,1,-1)$, $(0,3,-5)$, $(0,2,2)$, $(0,1,-1)$, $(0,2,3)$, $(0,2,-3)$, $(0,1,-1)$. Vị trí 11–13 là ba số 0, nên vị trí 14 cho $(3,1,-1)$; vị trí 15 cho $(0,2,2)$.

**Cả khối.** Số khác 0 cuối cùng ở vị trí 55, tức ô $(4,7)$; chín vị trí 56–64 là số 0 và cho bộ $(9,0)$. Khối cho 31 bộ: 30 bộ ba, gồm một bộ ba DC và 29 bộ ba AC, cùng bộ $(9,0)$. Phần biên độ tốn $2$ bit cho DC và $39$ bit cho 29 hệ số AC; phần $(r,s)$ của mỗi bộ được mã tiếp bằng mã entropy.

**Kiểm tra lại.** Số bộ ba bằng số khác 0 của $\hat F$, 30 (Ví dụ 11.11), và vị trí cuối $55+9=64$. Ở vị trí 6, ô $(0,2)$ có $\hat F_{02}=2$, khớp số thứ sáu của dãy.
:::

![Lưới 8 × 8 các hệ số đã lượng tử của khối Hình 11.9 với q = 2, hàng u từ trên xuống, cột v từ trái sang phải. Mỗi ô ghi vị trí zigzag ở góc trên trái và giá trị khác 0 ở góc dưới phải; ô khác 0 tô nền. Đường gấp khúc mảnh nối tâm các ô theo thứ tự zigzag. Ba ô viền đậm: vị trí 6 là ô (0, 2), vị trí 15 là ô (0, 4), vị trí 55 là ô (4, 7), số khác 0 cuối cùng.](img/lec-11/note-zigzag-khoi-luong-tu.svg)

Trên hình, đường gấp khúc đi qua các ô theo từng đường chéo, đổi chiều sau mỗi đường chéo. Các ô khác 0 tập trung ở nửa trên trái, nơi đường gấp khúc đi qua trước; sau vị trí 30, chỉ còn sáu ô khác 0 rải rác, mỗi ô có giá trị $\pm1$. Các ô viền đậm ứng với ba vị trí nêu ở Ví dụ 11.13.

<!-- note-topic-id: lec-11-topic-16 -->
### 5.4 Đường ống mã hóa, giải mã và chi phí

Ví dụ 11.9 tới 11.13 đã chạy tay mọi bước trừ mã entropy trên một khối. Ảnh CHEETAH.GS có $320/8\cdot200/8=40\cdot25=1\,000$ khối, và chương trình của NG đọc ảnh từng dải 8 hàng, mỗi dải 320 điểm, để không phải giữ cả ảnh trong bộ nhớ (NG, tr.267). Ghép các bước lại được bộ nén và bộ giải nén cho cả ảnh.

::: algorithm Thuật toán 11.34 (Nén và giải nén một ảnh xám theo khối $8\times8$)
**Đầu vào.** Khi nén: ảnh xám $m_{\mathrm h}$ hàng, $m_{\mathrm w}$ cột, điểm ảnh 8 bit; hệ số chất lượng $q$. Khi giải nén: dòng bit do bộ nén tạo ra.

**Đầu ra.** Khi nén: dòng bit có ghi $q$. Khi giải nén: ảnh $\tilde P$ cùng cỡ, điểm ảnh 8 bit.

**Giả thiết.** $m_{\mathrm h}$ và $m_{\mathrm w}$ chia hết cho 8, và hai phía biết hai số này; hai phía dùng cùng $T$, cùng công thức $Q$ theo $q$, cùng thứ tự zigzag và cùng mã entropy.

**Các bước nén.**

1. Ghi $q$ vào đầu dòng bit; dựng $Q$ và $T$.
2. Với mỗi dải 8 hàng, từ trên xuống, và mỗi khối $8\times8$ trong dải, từ trái sang phải, với $\kappa$ là số thứ tự của khối:
   1. Dịch mức: $A=P-128$.
   2. DCT: $F=TAT^{\top}$.
   3. Lượng tử hóa: $\hat F_{uv}=\operatorname{round}(F_{uv}/Q_{uv})$.
   4. Sai phân DC: $\delta_\kappa=\hat F_{00}^{(\kappa)}-\hat F_{00}^{(\kappa-1)}$, với $\hat F_{00}^{(0)}=0$.
   5. Lập dãy của khối gồm $\delta_\kappa$ và 63 hệ số AC theo thứ tự zigzag; phát các bộ ba $(r,s,a)$ và, nếu khối kết thúc bằng số 0, bộ $(r,0)$; mã các bộ bằng mã entropy.

**Các bước giải nén.**

1. Đọc $q$; dựng $Q$ và $T$.
2. Với mỗi khối $\kappa=1,\ldots,K$, $K=m/64$, theo thứ tự:
   1. Giải mã entropy và mã độ dài loạt tới khi đủ 64 số của khối (Mệnh đề 11.33).
   2. Cộng dồn $\hat F_{00}^{(\kappa)}=\hat F_{00}^{(\kappa-1)}+\delta_\kappa$ và đặt các hệ số AC về ô theo thứ tự zigzag.
   3. Giải lượng tử: $\tilde F_{uv}=Q_{uv}\hat F_{uv}$.
   4. IDCT: $\tilde A=T^{\top}\tilde FT$.
   5. Đặt $\tilde P$ là $\tilde A+128$ làm tròn rồi cắt về $[0;255]$.

**Dừng.** Sau $K$ khối ở mỗi phía.

**Trường hợp biên.** Ảnh có cạnh không chia hết cho 8 nằm ngoài giả thiết của thuật toán. Khối có mọi hệ số AC bằng 0 cho một bộ ba DC cùng bộ $(63,0)$, hoặc chỉ bộ $(64,0)$ khi $\delta_\kappa=0$. Với $q=0$, mọi bước lượng tử bằng 1 và sai số chỉ còn phần làm tròn.

**Chi phí.** Mô hình: đếm phép nhân số thực ở DCT và IDCT, phép chia ở lượng tử hóa, và phép xử lý một hệ số ở các bước còn lại; $K=m/64$ khối.

| Bước | Số lần | Chi phí mỗi lần | Đóng góp |
|---|---|---|---|
| dịch mức | $K$ khối | 64 phép trừ | $m$ |
| DCT, hai phép nhân ma trận $8\times8$ | $K$ | $2\cdot8\cdot8\cdot8=1\,024$ phép nhân | $16m$ |
| lượng tử hóa | $K$ | 64 phép chia | $m$ |
| sai phân DC, zigzag, loạt, mã entropy | $K$ | $O(64)$ | $O(m)$ |
| giải nén: giải lượng tử, IDCT, làm tròn, cắt | $K$ | 64 phép nhân, $1\,024$ phép nhân, $O(64)$ | $O(m)$ |
:::

Thuật toán thỏa đặc tả khôi phục gần đúng theo nghĩa sau. Theo Mệnh đề 11.33, bộ giải nén nhận lại đúng $\hat F^{(\kappa)}$ của mọi khối. Theo Định lý 11.31, mỗi khối có $E_{\mathrm{RMS}}(A^{(\kappa)},\tilde A^{(\kappa)})\le\beta(q)$, cùng một cận cho mọi khối vì mọi khối dùng chung $Q$. Mọi khối có 64 điểm, nên bình phương sai số RMS của cả ảnh là trung bình bình phương sai số RMS của các khối:
$$
\begin{aligned}
E_{\mathrm{RMS}}(A,\tilde A)^2&=\frac1K\sum_{\kappa=1}^{K}E_{\mathrm{RMS}}(A^{(\kappa)},\tilde A^{(\kappa)})^2\\
&\le\beta(q)^2 .
\end{aligned}
$$
Cộng phần làm tròn điểm ảnh, ảnh tái tạo thỏa Định nghĩa 11.1 với $\varepsilon=\beta(q)+\tfrac12$, khi DCT và IDCT được tính chính xác.

Phép quyết định của thuật toán là bước lượng tử hóa: nó là bước duy nhất phụ thuộc $q$, và nó quyết định cả số bộ ba lẫn sai số. Các bước khác cố định.

Theo bảng, cả bộ nén lẫn bộ giải nén tốn thời gian $\Theta(m)$ với khối cố định $8\times8$; bộ nhớ là một dải $8\times m_{\mathrm w}$ điểm ảnh cộng $O(1)$ khối. Nếu DCT được tính trực tiếp theo tổng kép, mỗi hệ số cần 64 số hạng, mỗi số hạng hai phép nhân, nên một khối tốn $64\cdot64\cdot2=8\,192$ phép nhân, gấp 8 lần dạng ma trận (NG, tr.255–256). Trên CHEETAH.GS, DCT dạng ma trận tốn $1\,000\cdot1\,024=1\,024\,000$ phép nhân.

Định lý 11.31 chặn sai số theo $q$ nhưng không cho số byte; số byte chỉ đo được trên từng ảnh. Hình sau vẽ tám số đo của NG trên CHEETAH.GS theo hệ số chất lượng.

![Hai biểu đồ đường cạnh nhau cho ảnh CHEETAH.GS 64 000 byte theo hệ số chất lượng q bằng 1, 2, 3, 4, 5, 10, 15, 25. Biểu đồ trái, số byte sau nén: 27 809; 18 367; 14 084; 11 731; 10 232; 7 167; 6 074; 5 094, giảm dần. Biểu đồ phải, sai số RMS: 4,3; 6,9; 8,6; 9,9; 10,9; 13,6; 15,2; 17,4, tăng dần.](img/lec-11/note-cheetah-byte-rms.svg)

Hai biểu đồ vẽ đánh đổi tốc độ bit–sai số (rate–distortion trade-off): khi $q$ tăng, số byte giảm và sai số tăng. Phần lớn số byte giảm xảy ra ở các giá trị $q$ nhỏ: từ $q=1$ tới $q=5$, số byte giảm $17\,577$ còn sai số tăng $6{,}6$ mức xám; từ $q=5$ tới $q=25$, số byte chỉ giảm thêm $5\,138$ trong khi sai số tăng thêm $6{,}5$ mức xám.

::: remark Nhận xét 11.35 (Trong thực hành)
- **Hệ số chất lượng.** Trên phần lớn trong năm ảnh xám của NG, hệ số chất lượng tới 5 chỉ làm giảm nhẹ độ nét; trên 5, ảnh bắt đầu lộ hiện tượng khối (blocking artifacts), tức đường biên giữa các khối $8\times8$ nhìn thấy được (NG, tr.287). Với CHEETAH.GS, $q=5$ cho $10\,232$ byte và RMS $10{,}9$ (NG, Hình 11.14).
- **Chương trình mẫu và chuẩn JPEG.** Chương trình DCT của NG không mã sai phân DC và không dùng mã Huffman; nó dùng một dạng mã độ dài loạt riêng với mã số nguyên độ dài thay đổi (NG, tr.265). Chương trình đó đếm loạt số 0 xuyên qua ranh giới khối, ghi mỗi loạt dài 1 tới 16 bằng số bit 0 kèm 4 bit độ dài, và xả loạt cuối ở cuối tệp (NG, tr.267, 270–271). Phép lượng tử trong chương trình chia hai số nguyên, tức cắt thương về 0 (NG, tr.261, 269); chương trình còn làm tròn hệ số DCT về số nguyên và làm tròn điểm ảnh. Mỗi hệ số vì vậy lệch không quá $Q_{uv}-\tfrac12$, và cận sai số của chương trình là $\sqrt{\tfrac1{64}\sum_{u,v}(Q_{uv}-\tfrac12)^2}+\tfrac12$, khoảng $9{,}60$; $18{,}23$; $44{,}12$ với $q=1,2,5$. Các số đo ở Hình 11.14 của NG là số đo của chương trình đó.
- **Mã entropy.** JPEG mã các bộ ba bằng mã Huffman hoặc mã số học, các bộ mã của Bài 10 (NG, tr.261; CMU-L, trang chiếu 14).
- **Tỷ lệ nén thường gặp.** JPEG thường nén khoảng 10 lần (CMU-L, trang chiếu 13); một ví dụ của CMU trên ảnh màu đạt $0{,}125$ bit mỗi điểm ảnh, khoảng 200 lần so với 24 bit mỗi điểm, vì $24/0{,}125=192$ (CMU-L, trang chiếu 17).
:::

::: exercise Bài tập 11.7 (Ngưỡng của ô $(7,7)$)
Với ma trận lượng tử $Q_{uv}=1+(1+u+v)q$ và lượng tử hóa làm tròn của Định nghĩa 11.29: (a) tính $Q_{77}$ với $q=2$ và giá trị nguyên nhỏ nhất của $\lvert F_{77}\rvert$ để $\hat F_{77}\ne0$; (b) làm lại với $q=5$ và $q=25$; (c) viết công thức ngưỡng theo $q$.
:::

::: hint
Theo Mệnh đề 11.30(a), $\hat F_{77}\ne0$ khi và chỉ khi $\lvert F_{77}\rvert\ge Q_{77}/2$.
:::

::: solution
**Câu (a).** $Q_{77}=1+15\cdot2=31$. Cần $\lvert F_{77}\rvert\ge15{,}5$, tức ít nhất 16 với hệ số nguyên; $16/31\approx0{,}52$ làm tròn thành 1 (NG, tr.260).

**Câu (b).** $q=5$: $Q_{77}=76$, ngưỡng $38$. $q=25$: $Q_{77}=376$, ngưỡng $188$.

**Câu (c).** $Q_{77}=1+15q$, nên $\hat F_{77}\ne0$ khi và chỉ khi $\lvert F_{77}\rvert\ge(1+15q)/2$.

**Kiểm tra lại.** Với $q=25$, ngưỡng $188$ vượt $186$, hệ số lớn nhất của khối ở Ví dụ 11.10, nên trên khối đó $\hat F_{77}=0$.
:::

::: exercise Bài tập 11.8 (Ba ô của khối hệ số đầu tiên)
Khối $8\times8$ đầu tiên của CHEETAH.GS có ba hệ số DCT $F_{02}=-9$, $F_{04}=3$, $F_{20}=-84$ (NG, Hình 11.11, tr.261). Với $q=2$: (a) tính bước lượng tử, $\hat F$ và $\tilde F$ của ba ô; (b) kiểm tra Mệnh đề 11.30(b) và chỉ ra ô được tái tạo đúng; (c) cho vị trí zigzag của ba ô.
:::

::: hint
Với $q=2$, $Q_{uv}=3+2(u+v)$.
:::

::: solution
**Câu (a).**

- Ô $(0,2)$: $Q_{02}=7$; $-9/7\approx-1{,}29$, nên $\hat F_{02}=-1$ và $\tilde F_{02}=-7$.
- Ô $(0,4)$: $Q_{04}=11$; $3/11\approx0{,}27$, nên $\hat F_{04}=0$ và $\tilde F_{04}=0$.
- Ô $(2,0)$: $Q_{20}=7$; $-84/7=-12$, nên $\hat F_{20}=-12$ và $\tilde F_{20}=-84$.

**Câu (b).** Sai số lần lượt là $2\le3{,}5$, $3\le5{,}5$ và $0\le3{,}5$. Ô $(2,0)$ được tái tạo đúng vì $-84$ là bội của 7.

**Câu (c).** Theo thứ tự zigzag, ô $(2,0)$ ở vị trí 4, ô $(0,2)$ ở vị trí 6, ô $(0,4)$ ở vị trí 15.

**Kiểm tra lại.** Ba ô cho cùng kết quả nếu thay làm tròn bằng cắt về 0: $-1$, $0$, $-12$.
:::

::: exercise Bài tập 11.9 (Cận sai số và số đo trên CHEETAH.GS)
Với $Q_{uv}=1+(1+u+v)q$: (a) tính cận $\beta(q)=\tfrac12\sqrt{\tfrac1{64}\sum_{u,v}Q_{uv}^2}$ của Định lý 11.31 với $q=1,2,5$. (b) Một ảnh có $K$ khối, và khối $\kappa$ có $E_{\mathrm{RMS}}\le\rho_\kappa$, chẳng hạn vì các vùng ảnh dùng ma trận lượng tử khác nhau. Chứng minh $E_{\mathrm{RMS}}$ của cả ảnh không quá $\sqrt{\tfrac1K\sum_\kappa\rho_\kappa^2}$, và do đó không quá $\max_\kappa\rho_\kappa$. (c) Chương trình của NG cắt thương về 0 khi lượng tử hóa, làm tròn hệ số DCT về số nguyên và làm tròn điểm ảnh, nên mỗi hệ số lệch không quá $Q_{uv}-\tfrac12$; trên CHEETAH.GS, chương trình đo được các sai số $4{,}3$; $6{,}9$; $10{,}9$ với $q=1,2,5$ (NG, Hình 11.14). Tính cận $\sqrt{\tfrac1{64}\sum_{u,v}(Q_{uv}-\tfrac12)^2}+\tfrac12$ với $q=1,2,5$ và so với số đo.
:::

::: hint
Ở câu (a), $\sum_{u,v}Q_{uv}^2=\sum_{\sigma=0}^{14}N_\sigma(1+(1+\sigma)q)^2$, với $N_\sigma$ là số ô trên đường chéo $u+v=\sigma$: $N_\sigma=\sigma+1$ khi $\sigma\le7$ và $N_\sigma=15-\sigma$ khi $\sigma\ge8$.
:::

::: solution
**Câu (a).** Tính theo gợi ý được $\sum Q_{uv}^2=5\,856$, $21\,184$, $124\,384$ với $q=1,2,5$, nên
$$
\begin{aligned}
\beta(1)&\approx4{,}78,\\
\beta(2)&\approx9{,}10,\\
\beta(5)&\approx22{,}04 .
\end{aligned}
$$

**Câu (b).** Mỗi khối có 64 điểm, nên tổng bình phương sai số của ảnh là tổng của $K$ khối, và
$$
\begin{aligned}
E_{\mathrm{RMS}}^2&=\frac1{64K}\sum_{\kappa=1}^{K}64\,E_{\mathrm{RMS},\kappa}^2\\
&\le\frac1K\sum_{\kappa=1}^{K}\rho_\kappa^2\le\max_\kappa\rho_\kappa^2,
\end{aligned}
$$
với $E_{\mathrm{RMS},\kappa}$ là sai số của khối $\kappa$. Lấy căn được hai bất đẳng thức cần chứng minh. Khi mọi khối dùng chung $Q$, cả hai cận bằng $\beta(q)$, như lập luận sau Thuật toán 11.34.

**Câu (c).** Cận của chương trình là khoảng $9{,}60$; $18{,}23$; $44{,}12$ với $q=1,2,5$. Số đo $4{,}3$; $6{,}9$; $10{,}9$ đều dưới cận, và tỷ số số đo trên cận giảm khi $q$ tăng: khoảng $0{,}45$; $0{,}38$; $0{,}25$. Cận giả sử mọi hệ số lệch gần trọn một bước; với $q$ lớn, phần lớn hệ số nhỏ hơn bước nhiều lần nên bị đưa về 0 với sai số chỉ bằng chính giá trị nhỏ của chúng.

**Kiểm tra lại.** Với $q=2$, $\beta=\tfrac12\sqrt{21\,184/64}=\tfrac12\sqrt{331}\approx9{,}10$, khớp Ví dụ 11.12.
:::

::: exercise Bài tập 11.10 (Một hệ số DCT và một đoạn mã độ dài loạt)
Khối Hình 11.9 của NG sau dịch mức có tổng theo cột $\sum_\xi A_{\xi\eta}$ lần lượt là 173, 198, 110, 215, 180, 163, 180, 269 với $\eta=0,\ldots,7$. Hàng 1 của $T$, làm tròn tới ba chữ số thập phân, là $0{,}490$; $0{,}416$; $0{,}278$; $0{,}098$; $-0{,}098$; $-0{,}278$; $-0{,}416$; $-0{,}490$. (a) Chứng minh $F_{01}=\tfrac1{\sqrt8}\sum_\eta T_{1\eta}\sum_\xi A_{\xi\eta}$, rồi tính $F_{01}$. (b) Trong dãy zigzag của khối đó sau lượng tử hóa với $q=2$, số ở vị trí 15 khác 0, và các vị trí 16–30 là −1, −1, 0, 1, 1, 0, 1, 0, 1, −1, −1, 1, −1, −1, 1. Lập các bộ ba $(r,s,a)$ của mã độ dài loạt cho mười lăm vị trí này.
:::

::: hint
Ở câu (a), mọi phần tử của hàng 0 của $T$ bằng $1/\sqrt8$.
:::

::: solution
**Câu (a).** Theo Định nghĩa 11.26, $F_{01}=\sum_\xi\sum_\eta T_{0\xi}A_{\xi\eta}T_{1\eta}$. Vì $T_{0\xi}=1/\sqrt8$ với mọi $\xi$, tổng theo $\xi$ chỉ còn tổng cột, nên $F_{01}=\tfrac1{\sqrt8}\sum_\eta T_{1\eta}\sum_\xi A_{\xi\eta}$. Tám tích là $84{,}77$; $82{,}37$; $30{,}58$; $21{,}07$; $-17{,}64$; $-45{,}31$; $-74{,}88$; $-131{,}81$, tổng $-50{,}86$, nên
$$
F_{01}\approx\frac{-50{,}86}{2{,}828}\approx-17{,}98 .
$$

**Câu (b).** Vị trí 15 khác 0 nên loạt đầu bắt đầu từ vị trí 16. Mười hai số khác 0 cho mười hai bộ ba: $(0,1,-1)$, $(0,1,-1)$, $(1,1,1)$, $(0,1,1)$, $(1,1,1)$, $(1,1,1)$, $(0,1,-1)$, $(0,1,-1)$, $(0,1,1)$, $(0,1,-1)$, $(0,1,-1)$, $(0,1,1)$.

**Kiểm tra lại.** Ở câu (a), giá trị chính xác là $-18{,}00$ (Ví dụ 11.10); sai lệch $0{,}02$ do làm tròn hàng của $T$. Ở câu (b), mười hai số khác 0 cộng ba số 0 ở các vị trí 18, 21, 23 là 15 vị trí.
:::

Như vậy, chúng ta đã có DCT trực chuẩn (Định nghĩa 11.26, Mệnh đề 11.28), lượng tử hóa với sai số mỗi hệ số không quá nửa bước (Định nghĩa 11.29, Mệnh đề 11.30), cận sai số của khối tái tạo theo bước lượng tử (Định lý 11.31), các bước mã hóa không mất thêm thông tin (Mệnh đề 11.33), và đường ống cho cả ảnh trong thời gian $\Theta(m)$ (Thuật toán 11.34). Số byte sau nén chỉ đo được trên từng ảnh: ở $q=2$, chương trình của NG cho $18\,367$ byte trên CHEETAH.GS và $14\,243$ byte trên CLOWN.GS. Chúng ta có hai họ bộ nén với hai đặc tả và hai loại bảo đảm; để dùng chúng cho một kho cụ thể, cần đặt các bảo đảm đó cạnh nhau.

<!-- note-topic-id: lec-11-topic-17 -->
## 6. Chọn phương pháp nén

Một kho dữ liệu hỗn hợp gồm nhật ký văn bản, tệp thực thi và một danh mục $1\,000$ ảnh, mỗi ảnh $64\,000$ byte, tổng 64 MB (NG, tr.208, 213, 246). Bài toán là chọn cho mỗi loại dữ liệu một bộ nén của chương, nêu kết quả bảo đảm cho lựa chọn đó, đếm chi phí và cho biết đổi lại được bao nhiêu byte. Chúng ta so ba bộ nén từ điển trên cùng chuỗi `aabaacabcabcb`.

::: example Ví dụ 11.14 (Ba bộ nén từ điển trên chuỗi aabaacabcabcb)
**Dữ kiện.** Chuỗi $x=$ `aabaacabcabcb`, $n=13$, tức $104$ bit nếu ghi 8 bit mỗi ký tự.

**LZ77 với $W=6$, $L=4$.** Thuật toán 11.5 cho năm bộ ba:

- $p=0$: $(0,0,\mathrm a)$;
- $p=1$: $x_2=\mathrm a$ khớp $x_1$, $x_3=\mathrm b$ không khớp, nên $(1,1,\mathrm b)$;
- $p=3$: với $d=3$, $x_4x_5=$ `aa` khớp $x_1x_2$, $x_6=\mathrm c$ khác $x_3=\mathrm b$; các khoảng lùi khác khớp ít hơn; nên $(3,2,\mathrm c)$;
- $p=6$: với $d=5$, $x_7x_8=$ `ab` khớp $x_2x_3$, $x_9=\mathrm c$ khác $x_4=\mathrm a$; nên $(5,2,\mathrm c)$;
- $p=9$: với $d=3$, $x_{10}x_{11}x_{12}=$ `abc` khớp $x_7x_8x_9$, và $\min(L,n-p-1)=3$; nên $(3,3,\mathrm b)$.

Theo Mệnh đề 11.9(d), mỗi bộ ba tốn 14 bit, tổng $5\cdot14=70$ bit.

**LZ78.** Thuật toán 11.13 cho sáu cặp: bốn cặp $(0,\mathrm a)$, $(1,\mathrm b)$, $(1,\mathrm a)$, $(0,\mathrm c)$ của Ví dụ 11.4, rồi:

- đọc `a`, `ab` (mã 2), rồi $\mathrm c$: `abc` chưa có, phát $(2,\mathrm c)$, thêm 5 = `abc`;
- đọc `a`, `ab`, `abc` (mã 5), rồi $\mathrm b$: `abcb` chưa có, phát $(5,\mathrm b)$, thêm 6 = `abcb`.

Chuỗi kết thúc ngay sau cặp thứ sáu nên không có cặp `EOS`. Giả sử hai phía thống nhất mã cụm 3 bit, đủ cho các mã 0 tới 7. Theo Mệnh đề 11.16(d), mỗi cặp tốn $3+9=12$ bit, tổng $72$ bit.

**LZW.** Thuật toán 11.19 cho 10 mã (Ví dụ 11.6). Từ điển nạp sẵn 256 mã một byte và thêm tới mã 264, nên mã cần ít nhất 9 bit; với mã 9 bit, tổng là $90$ bit (Mệnh đề 11.24(d)).

**Diễn giải.** Trên chuỗi 13 ký tự này, LZ77 tốn 70 bit, LZ78 72 bit, LZW 90 bit, so với 104 bit. Mỗi mã LZW, 9 bit, rẻ hơn một cặp LZ78, 12 bit, nhưng LZW phát 10 mã so với 6 cặp, vì từ điển chưa kịp có cụm dài và bảy trong mười mã là một ký tự. LZ77 tốn ít nhất vì mọi lần lặp nằm trong cửa sổ 6 ký tự. Kết luận chỉ đúng cho chuỗi ngắn này; LZ78 và LZW có lợi khi cụm lặp cách xa hơn $W$ và từ điển có đủ thời gian chứa cụm dài (Nhận xét 11.25).

**Kiểm tra lại.** Các bộ ba LZ77 phủ $1+2+3+3+4=13$ ký tự; các cặp LZ78 phủ $1+2+2+1+3+4=13$ ký tự; mười mã LZW phủ 13 ký tự (Ví dụ 11.6).
:::

Mỗi bộ nén từ điển chỉ rút ngắn dữ liệu khi một đơn vị mã trung bình mô tả nhiều hơn số ký tự hòa vốn, bằng số bit của đơn vị mã chia cho 8:

- LZ77 với $W=6$, $L=4$: $14/8=1{,}75$ ký tự; với $W=4\,096$, $L=15$: $24/8=3$ ký tự (Mệnh đề 11.9(d));
- LZ78 với $M=2^{16}$: $25/8=3{,}125$ ký tự (Mệnh đề 11.16(d));
- LZW với mã 9 bit: $9/8=1{,}125$ ký tự; với mã 12 bit: $12/8=1{,}5$ ký tự (Mệnh đề 11.24(d)).

Ở Ví dụ 11.14, một bộ ba LZ77 mô tả trung bình $13/5=2{,}6$ ký tự, một cặp LZ78 $13/6\approx2{,}17$ ký tự so với điểm hòa vốn $12/8=1{,}5$, một mã LZW $1{,}3$ ký tự; cả ba đều vượt điểm hòa vốn của mình. Trong bảng sau, các kết quả của Mục 2–5 được đặt cạnh nhau với cùng ký hiệu: $n$ là độ dài chuỗi, $W$, $L$ là cỡ cửa sổ và độ dài khớp tối đa, $M=2^b$ là số mục của từ điển, $m$ là số điểm ảnh.

| Phương pháp | Đặc tả | Dư thừa khai thác | Trạng thái | Bảo đảm | Chi phí |
|---|---|---|---|---|---|
| LZ77 (Thuật toán 11.5, 11.6) | khôi phục đúng | cụm lặp trong $W$ ký tự gần nhất | $W+L+1$ ký tự | $y=x$ (Định lý 11.8) | mã hóa $O(nWL)$ khi so vét cạn, giải mã $O(n)$; bộ ba $\lceil\log_2W\rceil+\lceil\log_2(L+1)\rceil+8$ bit (Mệnh đề 11.9) |
| LZ78 (Thuật toán 11.13, 11.14) | khôi phục đúng | cụm lặp ở mọi khoảng cách | cây từ điển $\le M$ mục | hai từ điển trùng nhau, $y=x$ (Định lý 11.15) | kỳ vọng $O(n)$ với bảng băm; cặp $b+9$ bit (Mệnh đề 11.16) |
| LZW (Thuật toán 11.19, 11.20) | khôi phục đúng | như LZ78, không truyền ký tự thô | từ điển nạp sẵn, $\le M$ mục | $y=x$, kể cả mã chưa có (Định lý 11.23) | kỳ vọng $O(n)$; mã $b$ bit (Mệnh đề 11.24) |
| Đường ống DCT kiểu JPEG (Thuật toán 11.34) | khôi phục gần đúng | năng lượng dồn về tần số thấp; mắt bỏ qua sai lệch nhỏ | một dải $8\times m_{\mathrm w}$ điểm | $E_{\mathrm{RMS}}\le\beta(q)$ mỗi khối (Định lý 11.31) | $\Theta(m)$, $1\,024$ phép nhân mỗi khối cho DCT |

::: remark Nhận xét 11.36 (Dấu hiệu chọn phương pháp)
- Mọi biến thể LZ đều giữ một "từ điển" các chuỗi đã gặp; chúng khác nhau ở cách lưu từ điển, cách mở rộng, cách đánh chỉ số và cách bỏ bớt mục (CMU-LZ, trang chiếu 20). Nén bằng từ điển là một dạng mô hình thống kê trá hình: nó rút ngắn những cụm mà nó đoán là sẽ lặp lại (NG, tr.247).
- Lặp gần, như họ "Jones" trên các dòng liền nhau của danh bạ, hợp với LZ77; lặp xa, như một tên riêng rải rác trong cả cuốn sách, hợp với LZ78 và LZW (NG, tr.208). LZ77 từng nén tốt hơn nhưng chậm hơn LZ78; bản gzip của LZ77 dùng bảng băm nên chạy nhanh gần bằng các bản LZ78 (CMU-LZ, trang chiếu 3).
- Dữ liệu phải khôi phục đúng từng byte loại hẳn nén mất dữ liệu (Định nghĩa 11.1). Ảnh chụp, nơi cụm khớp đúng rất ngắn nhưng mắt chấp nhận sai lệch nhỏ, hợp với đường ống DCT–lượng tử hóa.
:::

::: exercise Bài tập 11.11 (Chọn phương pháp cho ba kho)
Ba kho dữ liệu: (i) nhật ký văn bản của một máy chủ, các dòng liền nhau thường lặp cùng tên dịch vụ; (ii) các tệp thực thi, mỗi tệp gồm phần mã lệnh rồi phần dữ liệu (NG, tr.213); (iii) danh mục $1\,000$ ảnh $320\times200$ điểm, 1 byte mỗi điểm (NG, tr.246), giả sử là ảnh xám. (a) Với mỗi kho, chọn một bộ nén của chương, nêu đặc tả và kết quả bảo đảm cho lựa chọn. (b) Với mỗi kho, loại ít nhất một phương án và nêu lý do. (c) Với kho (iii), tính dung lượng gốc và dung lượng khi mỗi ảnh được nén bằng LZSS mà không cụm nào đủ dài, mỗi điểm ảnh tốn 9 bit. (d) So bộ nhớ của bộ mã hóa LZ77 với $W=4\,096$, $L=15$ với bộ nhớ của bảng băm LZW12 gồm $5\,021$ nút, mỗi nút lưu mã, mã cha và ký tự; giả sử mã và mã cha mỗi trường 2 byte, ký tự 1 byte.
:::

::: hint
Kho (ii) có hai phần với thống kê khác nhau; xem Nhận xét 11.17 về từ điển lỗi thời. Ở câu (d), dùng Mệnh đề 11.9(c).
:::

::: solution
**Câu (a).** Kho (i): LZ77, vì cụm lặp nằm gần nhau và Định lý 11.8 bảo đảm khôi phục đúng; chi phí giải mã $O(n)$ theo Mệnh đề 11.9. Kho (ii): LZ78 hoặc LZW với quy tắc xóa từ điển khi tỷ lệ nén xấu đi, như `compress`. Định lý 11.15 và 11.23 giả thiết từ điển không giới hạn; khi hai phía xóa từ điển cùng lúc, mỗi đoạn giữa hai lần xóa là một lần chạy mới của thuật toán, và hai định lý áp dụng cho từng đoạn. Kho (iii): Thuật toán 11.34, với đặc tả khôi phục gần đúng và cận sai số của Định lý 11.31.

**Câu (b).** Kho (i), (ii): loại nén mất dữ liệu, vì một byte sai làm hỏng dòng nhật ký hay chương trình (Nhận xét 11.3). Kho (ii): một từ điển LZ78 không bao giờ xóa sẽ lỗi thời khi chuyển sang phần dữ liệu (NG, tr.213). Kho (iii): loại nén từ điển, vì các chuỗi điểm ảnh hiếm khi lặp đúng từng byte (NG, tr.247).

**Câu (c).** Dung lượng gốc là $1\,000\cdot64\,000=64\,000\,000$ byte, khoảng 64 MB. Với 9 bit mỗi điểm, mỗi ảnh tốn $64\,000\cdot9/8=72\,000$ byte, cả kho $72\,000\,000$ byte, lớn hơn bản gốc $12{,}5\%$.

**Câu (d).** Theo Mệnh đề 11.9(c), bộ mã hóa LZ77 giữ $W+L+1=4\,112$ byte. Bảng băm LZW12 cần $5\,021\cdot(2+2+1)=25\,105$ byte, khoảng sáu lần; đổi lại, LZW nhớ được cụm ở mọi khoảng cách.

**Kiểm tra lại.** $9/8=1{,}125$; $64\cdot1{,}125=72$; $4\,096+15+1=4\,112$.
:::

Với kho văn bản phải khôi phục đúng từng byte, chúng ta có ba bộ nén một lượt với bộ nhớ hữu hạn, cả ba khôi phục đúng (Định lý 11.8, 11.15, 11.23). LZ77 với cửa sổ $W$ hợp với cụm lặp gần; nó mã hóa trong $O(nWL)$ khi so vét cạn và giải mã trong $O(n)$ (Mệnh đề 11.9). LZ78 và LZW với từ điển $M$ mục hợp với cụm lặp xa và chạy trong thời gian kỳ vọng $O(n)$ khi dùng bảng băm (Mệnh đề 11.16, 11.24). Mỗi bộ nén chỉ rút ngắn văn bản khi một đơn vị mã trung bình mô tả nhiều hơn số ký tự hòa vốn ở trên; trên bộ dữ liệu chuẩn Calgary, gzip, một biến thể LZ77, đạt 2,59 bit mỗi ký tự so với 8 bit (CMU-I, trang chiếu 10).

Với kho ảnh chỉ cần khôi phục gần đúng, đường ống DCT–lượng tử hóa có sai số mỗi khối không quá $\beta(q)$ (Định lý 11.31) và chạy trong thời gian $\Theta(m)$; chương trình của NG đưa CHEETAH.GS từ $64\,000$ byte xuống $18\,367$ byte với sai số đo được $6{,}9$ mức xám ở $q=2$. Nén từ điển cho ảnh chụp vẫn khôi phục đúng (Định lý 11.8) nhưng không rút ngắn được ảnh, vì cụm khớp đúng rất ngắn; nén mất dữ liệu cho văn bản vi phạm đặc tả khôi phục đúng (Định nghĩa 11.1).

<!-- note-topic-id: lec-11-topic-18 -->
## Tình huống áp dụng và ứng dụng

- Tình huống 11.1: danh mục ảnh thỏa giả thiết của Định lý 11.31 và Thuật toán 11.34.
- Tình huống 11.2: nén từ điển cho ảnh chụp vi phạm giả thiết cụm khớp dài mà lợi ích của LZ77 cần.
- Tình huống 11.3: LZW trên tệp ngắn vi phạm giả thiết từ điển đã có cụm dài.
- Tình huống 11.4: kho văn bản thỏa giả thiết cụm lặp của LZ77.

::: application Tình huống 11.1 (Danh mục $1\,000$ ảnh)
**Bài toán và dữ liệu.** Một danh mục bán hàng trực tuyến có $1\,000$ ảnh, mỗi ảnh $320\times200$ điểm, 1 byte mỗi điểm, tổng 64 MB (NG, tr.246). Giả sử các ảnh là ảnh xám 8 bit. Yêu cầu: giảm dung lượng sao cho mỗi ảnh tái tạo có sai số RMS không quá 10 mức xám.

**Mô hình hóa.** Mỗi ảnh là dữ liệu $m=64\,000$ mẫu của Định nghĩa 11.1 với đặc tả khôi phục gần đúng, $\varepsilon=10$; bộ nén là Thuật toán 11.34 với hệ số chất lượng $q$.

**Kiểm giả thiết.** Ảnh chụp chấp nhận sai lệch nhỏ mà mắt không nhận ra (NG, tr.247); cạnh $320$ và $200$ chia hết cho 8. Định lý 11.31 cần DCT chính xác và lượng tử hóa làm tròn.

**Áp dụng.** Với bộ nén làm tròn đúng như Thuật toán 11.34, sai số của mỗi ảnh không quá $\beta(q)+\tfrac12$. Với $q=2$, $\beta(2)+\tfrac12\approx9{,}10+0{,}5=9{,}60\le10$, nên $q=2$ bảo đảm ngưỡng cho mọi ảnh trước khi nén; với $q=5$, cận là $22{,}04+0{,}5$ và không bảo đảm gì. Chương trình của NG thì cắt thương về 0, và cận của nó ở $q=2$ là khoảng $18{,}2$ (Nhận xét 11.35), lớn hơn 10. Với chương trình đó, $q$ phải chọn theo số đo: trên CHEETAH.GS, $q=2$ cho $18\,367$ byte và sai số đo được $6{,}9$, còn $q=5$ cho $10\,232$ byte nhưng sai số $10{,}9$ (NG, Hình 11.14). Giả sử mọi ảnh có số đo như CHEETAH.GS; chương trình của NG với $q=2$ đưa cả kho xuống khoảng $18{,}4$ MB.

**Chi phí.** Mỗi ảnh có $1\,000$ khối; DCT tốn $1\,000\cdot1\,024=1\,024\,000$ phép nhân mỗi ảnh, khoảng $1{,}02\cdot10^9$ phép nhân cho cả kho; bộ nhớ là một dải $8\cdot320=2\,560$ điểm ảnh.

**Diễn giải và giới hạn.** Cận của Định lý 11.31 cho phép chọn $q$ trước khi nén, vì nó không phụ thuộc nội dung ảnh; số byte thì phụ thuộc nội dung. Ở cùng $q=5$, chương trình của NG đưa ảnh LISAW.GS xuống $5\,941$ byte với sai số $3{,}7$, còn CHEETAH.GS xuống $10\,232$ byte với sai số $10{,}9$ (NG, Hình 11.14). Một bộ nén đo sai số từng ảnh rồi chọn $q$ lớn nhất còn đạt ngưỡng sẽ tiết kiệm hơn, như Bài tập 11.1. Trên $q=5$ ảnh lộ hiện tượng khối (NG, tr.287), và RMS không thay được đánh giá bằng mắt (NG, tr.266).

**Dẫn ngược lý thuyết.** Định nghĩa 11.1, Định lý 11.31, Thuật toán 11.34, Nhận xét 11.35, Bài tập 11.1, 11.9.
:::

::: application Tình huống 11.2 (Nén từ điển cho ảnh chụp)
**Bài toán và dữ liệu.** Nén ảnh CHEETAH.GS, $64\,000$ byte, bằng LZ77 với $W=4\,096$ và $L=15$, như cài đặt của NG (tr.179).

**Mô hình hóa.** Dữ liệu là chuỗi $n=64\,000$ byte; bộ mã hóa là Thuật toán 11.5; mỗi bộ ba tốn $12+4+8=24$ bit (Mệnh đề 11.9(d)), nên chỉ có lợi khi mô tả trung bình hơn $24/8=3$ ký tự.

**Kiểm giả thiết.** Định lý 11.8 vẫn đúng: bộ giải mã trả lại đúng ảnh. Giả thiết bị vi phạm là giả thiết mà lợi ích của LZ77 cần: các cụm khớp phải dài. Trên ảnh chụp, trong mỗi chuỗi hai mươi điểm của một đường nét, một hai điểm lệch một mức xám so với hàng trước và hàng sau, nên cụm khớp đúng thường ngắn (NG, tr.247).

**Áp dụng và chi phí.** Giả sử mỗi bộ ba chỉ khớp $\ell=1$ ký tự, tức mô tả 2 điểm ảnh. Khi đó có $32\,000$ bộ ba, tổng $32\,000\cdot24=768\,000$ bit, tức $96\,000$ byte, gấp $1{,}5$ ảnh gốc. Với LZSS, một cụm 1 ký tự được mã như ký tự rời 9 bit (Nhận xét 11.10), nên mỗi điểm tốn 9 bit, tổng $72\,000$ byte, lớn hơn ảnh gốc $12{,}5\%$. Bộ mã hóa vét cạn tốn không quá $32\,000\cdot4\,096\cdot16\approx2{,}1\cdot10^9$ phép so, theo cận xấu nhất của Mệnh đề 11.9(a).

**Hậu quả.** Dòng nén dài hơn ảnh gốc. Theo Mệnh đề 10.2, không bộ nén khôi phục đúng nào rút ngắn được mọi đầu vào; ảnh chụp nằm trong nhóm đầu vào mà mô hình "cụm lặp đúng từng byte" không rút ngắn được.

**Dẫn ngược lý thuyết.** Mệnh đề 10.2, Định nghĩa 11.4, Thuật toán 11.5, Định lý 11.8, Mệnh đề 11.9, Nhận xét 11.10.
:::

::: application Tình huống 11.3 (LZW cho tệp ngắn)
**Bài toán và dữ liệu.** Nén tệp 19 byte `␣WED␣WE␣WEE␣WEB␣WET` bằng chương trình LZW12 của NG: mã 12 bit, mã 256 là `END_OF_STREAM`, mã cụm đầu là 257 (NG, tr.215, 220–224).

**Mô hình hóa.** Dòng mã của Thuật toán 11.19 với mọi mã cụm tăng thêm 1, cộng mã `END_OF_STREAM` ở cuối (Nhận xét 11.25). Theo Mệnh đề 11.24(d), một mã 12 bit chỉ có lợi khi mô tả trung bình hơn $12/8=1{,}5$ ký tự.

**Kiểm giả thiết.** Định lý 11.23 bảo đảm khôi phục đúng. Lợi ích về số bit cần từ điển đã có những cụm dài so với độ rộng mã, tức đầu vào đủ dài; một tệp 19 byte không thỏa giả thiết đó.

**Áp dụng và chi phí.** Theo Bài tập 11.5, có 12 mã cho 19 ký tự; cộng mã kết thúc là 13 mã, trung bình $19/13\approx1{,}46$ ký tự mỗi mã, dưới điểm hòa vốn. Mỗi mã 12 bit, tổng $156$ bit, tức $19{,}5$ byte, dài hơn tệp gốc 19 byte. Với mã 9 bit và không có mã kết thúc, cùng chuỗi tốn $108$ bit, tức $13{,}5$ byte. Thời gian là $18$ phép tra và $11$ phép thêm vào từ điển (Mệnh đề 11.24).

**Hậu quả.** Với mã 12 bit, tệp ngắn bị kéo dài. Trên dữ liệu thật, LZW thường chỉ bắt đầu nén sau khoảng một trăm byte, và mã rộng làm tệp nhỏ thiệt (NG, tr.212, 215).

**Dẫn ngược lý thuyết.** Thuật toán 11.19, Định lý 11.23, Mệnh đề 11.24, Nhận xét 11.25, Bài tập 11.5.
:::

::: application Tình huống 11.4 (Kho văn bản)
**Bài toán và dữ liệu.** Một kho văn bản gồm các loại tệp của bộ dữ liệu chuẩn Calgary (Calgary corpus): hai cuốn sách, năm bài báo, một thư mục tài liệu, một tập tin tức, ba chương trình, một phiên làm việc trên thiết bị đầu cuối, hai tệp mã đối tượng, một tệp dữ liệu địa vật lý và một ảnh hai màu (CMU-I, trang chiếu 9). Giả sử kho dài $n=10^9$ byte và phải khôi phục đúng từng byte.

**Mô hình hóa.** Dòng byte đọc một lượt; bộ mã hóa là biến thể LZ77 của gzip (Nhận xét 11.10), bộ giải mã chép tuần tự như Thuật toán 11.6.

**Kiểm giả thiết.** Văn bản và chương trình có nhiều cụm lặp gần, như từ, tên biến và dòng lệnh, nên giả thiết cụm khớp dài mà lợi ích của LZ77 cần được thỏa. Gzip không hoàn toàn tham lam và mã các trường bằng mã Huffman. Mỗi đơn vị mã của gzip là một ký tự rời hoặc một cặp vị trí–độ dài thỏa điều kiện khớp của Định nghĩa 11.4, nên lập luận của Bổ đề 11.7 và Định lý 11.8 áp dụng cho từng đơn vị; mã Huffman giải mã duy nhất, nên bộ giải mã vẫn khôi phục đúng.

**Áp dụng.** Trên bộ Calgary, gzip đạt $2{,}59$ bit mỗi ký tự và LZ77 gốc đạt $3{,}94$ bit mỗi ký tự (CMU-I, trang chiếu 10). Với kho giả sử, gzip cho khoảng $10^9\cdot2{,}59/8\approx3{,}2\cdot10^8$ byte, tiết kiệm khoảng $68\%$; LZ77 gốc cho khoảng $4{,}9\cdot10^8$ byte, tiết kiệm khoảng $51\%$.

**Chi phí.** Gzip giới hạn số vị trí thử trong mỗi ngăn băm nên mỗi byte tốn một số hằng phép so (Nhận xét 11.10). Để so sánh, Thuật toán 11.5 với tìm vét cạn và cấu hình giả sử $W=4\,096$, $L=15$, khác cấu hình của gzip, có cận $10^9\cdot4\,096\cdot16\approx6{,}6\cdot10^{13}$ phép so (Mệnh đề 11.9(a)). Giải mã tốn đúng $10^9$ phép ghi ký tự (Mệnh đề 11.9(b)).

**Diễn giải và giới hạn.** Các số đo là của một bộ dữ liệu chuẩn; một kho nhật ký cụ thể cho tỷ lệ khác, tùy số cụm lặp nằm trong cửa sổ.

**Dẫn ngược lý thuyết.** Thuật toán 11.5, 11.6, Định lý 11.8, Mệnh đề 11.9, Nhận xét 11.10.
:::

**Ứng dụng.**

- Chương trình gzip dùng một biến thể LZ77 với bảng băm theo chuỗi 3 ký tự và mã Huffman cho vị trí, độ dài, ký tự (CMU-LZ, trang chiếu 3, 8).
- Chương trình `compress` của UNIX dùng LZW (NG, tr.214), định dạng GIF dùng một biến thể LZW (NG, tr.170); chuẩn nén của ổ băng từ QIC-122 và chuẩn modem V.42bis là các phương pháp nén bằng từ điển (NG, tr.170–171).
- JPEG nối đường ống DCT–lượng tử hóa với mã Huffman hoặc mã số học của Bài 10 (NG, tr.261).

<!-- note-topic-id: lec-11-topic-19 -->
## Tóm tắt chương

Bài 10 cho các bộ nén mã từng ký hiệu, không rút ngắn được mọi thông điệp; điểm xuất phát của Bài 11 là hai đặc tả, khôi phục đúng và khôi phục gần đúng, đo bằng tốc độ bit và sai số RMS (Định nghĩa 11.1), cùng sự kiện rằng một bộ nén rút ngắn mọi đầu vào phải làm mất dữ liệu (Mệnh đề 11.2). Với khôi phục đúng, LZ77 thay cụm lặp bằng bộ ba khoảng lùi–độ dài–ký tự trỏ vào cửa sổ $W$ ký tự (Định nghĩa 11.4, Thuật toán 11.5); bộ giải mã chép tuần tự, kể cả khi đoạn nguồn chồng lên đoạn đích, trả lại đúng chuỗi (Thuật toán 11.6, Bổ đề 11.7, Định lý 11.8), với chi phí mã hóa $O(nWL)$ và giải mã $O(n)$ (Mệnh đề 11.9). LZ78 bỏ cửa sổ, giữ một từ điển cụm có cấu trúc cây mà hai phía dựng giống hệt nhau từ chính dòng cặp (Thuật toán 11.13, 11.14, Bổ đề 11.12, Định lý 11.15), với chi phí kỳ vọng $O(n)$ khi tra con bằng bảng băm (Mệnh đề 11.16). LZW nạp sẵn mọi cụm một byte để bỏ ký tự thô khỏi mỗi đơn vị mã (Thuật toán 11.19); bộ giải mã chậm hơn một mục (Thuật toán 11.20, Bổ đề 11.21), mã chưa có trong từ điển của nó luôn là $w\operatorname{first}(w)$ (Mệnh đề 11.22, Định lý 11.23), và chi phí kỳ vọng vẫn là $O(n)$ (Mệnh đề 11.24). Với khôi phục gần đúng, DCT trực chuẩn không làm mất gì (Mệnh đề 11.28) và trên khối Hình 11.9 dồn khoảng $80\%$ năng lượng vào hệ số DC (Ví dụ 11.10); lượng tử hóa là bước duy nhất bỏ dữ liệu (Mệnh đề 11.30, 11.33), sai số RMS của khối tái tạo không quá $\beta(q)$ (Định lý 11.31), và cả đường ống chạy trong $\Theta(m)$ (Thuật toán 11.34). Trên chuỗi `aabaacabcabcb`, LZ77, LZ78, LZW tốn 70, 72, 90 bit so với 104 bit; trên ảnh CHEETAH.GS, chương trình của NG đưa $64\,000$ byte xuống $18\,367$ byte với sai số $6{,}9$ mức xám ở $q=2$.

**Định nghĩa và kết quả theo mục.**

- Mục 1: hai đặc tả, tốc độ bit, sai số RMS (Định nghĩa 11.1); rút ngắn mọi đầu vào buộc mất dữ liệu (Mệnh đề 11.2); thực hành (Nhận xét 11.3).
- Mục 2: bộ ba LZ77 (Định nghĩa 11.4); mã hóa tham lam (Thuật toán 11.5); giải mã (Thuật toán 11.6); sao chép tuần tự (Bổ đề 11.7); khôi phục đúng (Định lý 11.8); chi phí (Mệnh đề 11.9); LZSS, gzip (Nhận xét 11.10).
- Mục 3: từ điển cụm và cây (Định nghĩa 11.11, Bổ đề 11.12); mã hóa, giải mã LZ78 (Thuật toán 11.13, 11.14); đồng bộ (Định lý 11.15); chi phí (Mệnh đề 11.16); từ điển đầy (Nhận xét 11.17).
- Mục 4: từ điển nạp sẵn (Định nghĩa 11.18); mã hóa, giải mã LZW (Thuật toán 11.19, 11.20); độ trễ một mục (Bổ đề 11.21); mã chưa có (Mệnh đề 11.22); khôi phục đúng (Định lý 11.23); chi phí (Mệnh đề 11.24); LZW12 (Nhận xét 11.25).
- Mục 5: DCT (Định nghĩa 11.26, Bổ đề 11.27, Mệnh đề 11.28); lượng tử hóa (Định nghĩa 11.29, Mệnh đề 11.30); cận sai số (Định lý 11.31); sai phân DC, zigzag, mã độ dài loạt (Định nghĩa 11.32, Mệnh đề 11.33); đường ống (Thuật toán 11.34, Nhận xét 11.35).
- Mục 6: điểm hòa vốn của ba bộ nén từ điển; bảng chọn phương pháp; dấu hiệu chọn (Nhận xét 11.36).

**Công thức và thuật toán cần nhớ.**

Bộ ba LZ77 tại con trỏ $p$ và số bit của nó:
$$
\begin{gathered}
x_{p+j}=x_{p+j-d}\ (j=1,\ldots,\ell),\\
c=x_{p+\ell+1},\\
\lceil\log_2W\rceil+\lceil\log_2(L+1)\rceil+8\ \text{bit}.
\end{gathered}
$$

Mục thêm và mã chưa có của LZW:
$$
\begin{gathered}
D[255+t]=w_t\operatorname{first}(w_{t+1}),\\
k_{t+1}=\texttt{next\_code}\\
\Rightarrow\ w_{t+1}=w_t\operatorname{first}(w_t).
\end{gathered}
$$

DCT, lượng tử hóa và cận sai số:
$$
\begin{gathered}
F=TAT^{\top},\qquad A=T^{\top}FT,\\
\hat F_{uv}=\operatorname{round}(F_{uv}/Q_{uv}),\\
\tilde F_{uv}=Q_{uv}\hat F_{uv},\\
E_{\mathrm{RMS}}(A,\tilde A)\le\beta(q)=\tfrac12\sqrt{\tfrac1{64}\textstyle\sum_{u,v}Q_{uv}^2}.
\end{gathered}
$$

LZ77 thử mọi khoảng lùi và lấy cụm khớp dài nhất; bộ giải mã chép từng ký tự theo thứ tự. LZ78 và LZW đi xuống cây từ điển theo ký tự đọc vào và thêm "cụm khớp cộng ký tự phá khớp" khi phát mã. JPEG làm dịch mức, DCT, lượng tử hóa, sai phân DC, zigzag, mã độ dài loạt và mã entropy trên từng khối $8\times8$, rồi chạy ngược khi giải nén.

**Giả thiết hay bị bỏ quên.**

- Bộ giải mã LZ77 phải chép từng ký tự theo thứ tự; chép cả khối một lần sai khi $\ell>d$.
- LZ78 và LZW chỉ đúng khi hai phía dùng cùng quy tắc thêm mục, cùng cách đánh mã và cùng quy tắc xử lý từ điển đầy.
- Bộ giải mã LZW cần nhánh $k=\texttt{next\_code}$; mã lớn hơn $\texttt{next\_code}$ chỉ xuất hiện khi dòng bị hỏng.
- Định lý 11.31 cần DCT chính xác và lượng tử hóa làm tròn; làm tròn điểm ảnh cộng thêm tối đa $\tfrac12$, còn phép cắt về 0 của chương trình NG gần như nhân đôi cận, nên số đo của chương trình đó không được bảo đảm bởi $\beta(q)$.
- Cận sai số không cho số byte; số byte và sai số đo được phụ thuộc nội dung ảnh.

<!-- note-topic-id: lec-11-topic-20 -->
## Bài tập củng cố

Bài tập 11.12–11.17 nằm trong [tệp bài tập Bài 11](material-viewer.html?doc=materials/lec-11/exercises.md&deck=lecture-11-nen-bang-tu-dien-va-nen-mat-du-lieu.html), cùng gợi ý và lời giải.

<!-- note-topic-id: lec-11-topic-21 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

Bản điện tử của sách Nelson và Gailly không in số trang, nên số trang ghi dưới đây là số trang của bản điện tử; tên chương và tên mục của sách giúp tra trên bản in. Số trang chiếu của CMU là số in dưới mỗi trang chiếu.

- Nelson, M. và Gailly, J.-L. (1995). *The Data Compression Book*, ấn bản 2, M&T Books.
  - Chương 7 "Dictionary-Based Compression", tr.170–171: phần Ứng dụng.
  - Chương 8 "Sliding Window Compression", các mục "The Algorithm", "Problems with LZ77", "An Encoding Problem", "LZSS Compression", "Greedy vs. Best Possible", tr.174–185: Mục 2, Nhận xét 11.10, Bài tập 11.2, 11.3, Tình huống 11.2.
  - Chương 9 "LZ78 Compression", các mục "Can LZ77 Improve?", "LZ78 Details", "LZ78 Implementation", "An Effective Variant", "Decompression", "The Catch", "LZW Implementation", tr.208–226: Mục 3, Mục 4, Nhận xét 11.17, 11.25, Bài tập 11.4, 11.5, Tình huống 11.3.
  - Chương 11 "Lossy Graphics Compression", các mục "Statistical and Dictionary Compression Methods", "JPEG Compression", "The DCT", "Quantization", "Coding", "The Zig-Zag Sequence", "Entropy Encoding", "The Sample Program", "Some Compression Results", tr.245–289: Mục 1, Mục 5, Ví dụ 11.1, 11.9–11.13, Bài tập 11.1, 11.7–11.10, Tình huống 11.1.
- Blelloch, G. CMU 15-499, *Algorithms in the Real World: Data Compression*.
  - Phần nhập môn (CMU-I), trang chiếu 9–10: Mục 6, Tình huống 11.4.
  - Phần nén bằng từ điển (CMU-LZ), trang chiếu 3–20: Mục 2–4, Mục 6, Ví dụ 11.2, 11.4–11.7, Nhận xét 11.10, 11.17, 11.36.
  - Phần nén mất dữ liệu (CMU-L), trang chiếu 9–17: Mục 5, Mệnh đề 11.28, Nhận xét 11.35.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L. và Stein, C. (2022). *Introduction to Algorithms*, ấn bản 4, MIT Press. Chương 2 (bất biến vòng lặp): cách chứng minh Định lý 11.8, 11.15, 11.23. Chương 11 (bảng băm, địa chỉ mở): Mệnh đề 11.16, 11.24, Nhận xét 11.25.
- Bài báo gốc, theo NG: Ziv, J. và Lempel, A. (1977), "A Universal Algorithm for Sequential Data Compression", *IEEE Transactions on Information Theory* (NG, tr.174); Ziv, J. và Lempel, A. (1978), "Compression of Individual Sequences via Variable-Rate Coding", *IEEE Transactions on Information Theory* (NG, tr.209); Welch, T. (1984), "A Technique for High-Performance Data Compression", *IEEE Computer* (NG, tr.214).
- Chứng minh nằm ngoài phạm vi học phần: tính tối ưu tiệm cận của LZ77 với cửa sổ trượt, Wyner và Ziv (1994), theo CMU-LZ, trang chiếu 10.
- Đọc thêm, không cần cho bài tập: cây tìm kiếm nhị phân của LZSS và các cải tiến của nó (NG, tr.179–183, 200–201); cài đặt LZW12.C đầy đủ (NG, tr.218–226); mã nguồn chương trình DCT (NG, tr.265–286).
- Ghi chú Bài 10 (Định nghĩa 10.1, 10.3, 10.5, 10.11, Mệnh đề 10.2, Nhận xét 10.4, Thuật toán 10.14, Định lý 10.18, Hệ quả 10.19, Định lý 10.34), Bài 08 (Mục 1.4) và Bài 05 (Mệnh đề 05.19): các kết quả nhắc lại ở phần kiến thức tiên quyết.
