# Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc

Xem bộ trang chiếu tại [Bài 08 — Dòng dữ liệu: mô hình, lấy mẫu và lọc](../../lecture-08-dong-du-lieu-mo-hinh-lay-mau-va-loc.html).

Dòng dữ liệu đến liên tục, chưa biết trước độ dài cuối cùng, và không thể lưu toàn bộ lịch sử trong bộ nhớ làm việc. Bài này giới thiệu ba kiểu xử lý nền tảng: lấy mẫu theo khóa, lấy mẫu hồ chứa, và bộ lọc Bloom. Ba cấu trúc này trả lời ba loại câu hỏi khác nhau, và việc chọn đúng trạng thái phụ thuộc vào đầu ra mà ta cần tính.

## 1. Mô hình dòng một lượt

### Vai trò

Dòng dữ liệu khác cơ sở dữ liệu ở chỗ ta không có toàn bộ dữ liệu khi muốn. Dữ liệu đến từng bộ và tuần tự; nếu không xử lý hoặc lưu ngay thì bộ đó có thể mất đi vĩnh viễn. Điều này xảy ra khi tốc độ đến quá nhanh, hoặc khi có quá nhiều dòng cùng lúc khiến tổng nhu cầu bộ nhớ vượt quá bộ nhớ làm việc.

### Đặc tả

Ta xem bộ xử lý dòng như một mô hình với bốn thành phần:

- **Đầu vào:** dãy bộ $x_1,x_2,\dots$ đến tuần tự; độ dài có thể chưa biết trước và mỗi bộ phải được xử lý trước khi dòng tiếp tục quá xa.
- **Trạng thái:** một lưu trữ làm việc hữu hạn, được cập nhật mỗi khi một bộ đến; ngân sách này nhỏ hơn lịch sử của dòng.
- **Kho lưu trữ:** nơi lưu dữ liệu lớn, chỉ được truy cập trong trường hợp đặc biệt và tốn thời gian; ta không dùng nó để trả lời truy vấn.
- **Đầu ra:** mẫu, quyết định lọc, hoặc thống kê, được tạo ra khi dòng chảy qua.

Hai dạng truy vấn trên dòng: truy vấn thường trực (chạy lâu dài, sinh đầu ra liên tục) và truy vấn tức thời (hỏi một lần về trạng thái hiện tại). Vì không giữ được toàn bộ lịch sử, ta không thể trả lời truy vấn tùy ý; ta chuẩn bị trạng thái cho những loại truy vấn dự kiến.

### Bốn trục chi phí

Khi so sánh thuật toán dòng, ta hỏi bốn câu sau thay vì chỉ báo độ phức tạp theo độ dài dòng:

| Trục | Câu hỏi cần trả lời |
|---|---|
| Bộ nhớ | Trạng thái tăng theo ngân sách nào? Có tăng theo độ dài dòng không? |
| Cập nhật | Mỗi bộ đến cần bao nhiêu phép băm, phép gán, truy cập bit? |
| Lượt quét | Cần một lượt hay phải đọc lại lịch sử? |
| Sai số | Xác suất hoặc đại lượng nào chỉ được xấp xỉ? |

Việc cần làm là chọn một trạng thái nhỏ phù hợp với đầu ra. Ba phần sau trình bày ba trạng thái tương ứng với ba sản phẩm: mẫu theo nhóm, mẫu theo vị trí, và phép lọc thành viên xác suất.

<div class="figure">

![Ba dòng phần tử đi vào bộ xử lý có bộ nhớ hữu hạn, trả lời truy vấn và có thể ghi kho lưu trữ](img/lec-08/stream-model.svg)

</div>

::: exercise Tự kiểm
Một thuật toán giữ trạng thái cố định nhưng phải quét lại toàn bộ lịch sử sau mỗi truy vấn có thuộc mô hình một lượt ở đây không?
:::

::: solution
Không. Thuật toán còn phải cập nhật trạng thái khi dữ liệu đến và không dựa vào việc đọc lại lịch sử.
:::

## 2. Sai lệch của lấy mẫu độc lập từng bộ

### Vấn đề

Xét dòng truy vấn với bộ `(user, query, time)` và câu hỏi: "với người dùng điển hình, có bao nhiêu phần trăm truy vấn được lặp lại trong tháng vừa qua?" Ta chỉ lưu được $1/10$ dòng.

Cách tự nhiên là sinh mỗi bộ một số ngẫu nhiên trong $\{0,\dots,9\}$ và giữ bộ khi số bằng 0. Mỗi người dùng trung bình giữ lại $1/10$ truy vấn của mình. Tuy nhiên, cách này cho câu trả lời sai cho câu hỏi về tỷ lệ truy vấn lặp.

### Phép đếm

Giả sử mỗi người dùng có $x$ truy vấn phân biệt xuất hiện đúng một lần và $d$ truy vấn phân biệt xuất hiện đúng hai lần. Tỷ lệ cần ước lượng là

$$\frac{d}{x+d}.$$

Trong mẫu $1/10$, kỳ vọng chứa $x/10$ truy vấn đơn. Trong $d$ truy vấn lặp, chỉ $d/100 = \tfrac{1}{10}\cdot\tfrac{1}{10}d$ còn đủ hai bản, và $18d/100$ chỉ còn một bản (một bản nằm trong $1/10$ được chọn, một bản nằm trong $9/10$ bị bỏ). Vậy tỷ số từ số đếm kỳ vọng trong mẫu là

$$\frac{d/100}{x/10 + 18d/100 + d/100} = \frac{d}{10x + 19d}.$$

Rõ ràng $d/(x+d) \ne d/(10x+19d)$ với mọi $x,d>0$. Ví dụ với $x=d=1$, tỷ lệ đích là $1/2$ nhưng tỷ số từ số đếm kỳ vọng là $1/29$.

> Lưu ý: tỷ số thứ hai chỉ là tỷ số của hai kỳ vọng, không phải kỳ vọng chính xác của một tỷ số ngẫu nhiên. Nó cho thấy lấy mẫu độc lập từng bộ phá vỡ đơn vị thống kê: quan hệ giữa các lần xuất hiện của cùng một truy vấn bị mất.

::: exercise Tự kiểm
Sai lệch trên đến từ tỷ lệ $1/10$ hay từ việc chọn sai đơn vị?
:::

::: solution
Từ việc chọn sai đơn vị. Lấy độc lập từng lần xuất hiện có thể giữ một bản nhưng bỏ bản còn lại của cùng truy vấn.
:::

## 3. Lấy mẫu nhất quán theo khóa

### Trực giác

Thay vì lấy mẫu từng bộ độc lập, ta lấy mẫu theo **đơn vị thống kê**: chọn tập các giá trị khóa và giữ toàn bộ bộ có khóa được chọn. Với câu hỏi về truy vấn lặp theo người dùng, đơn vị là người dùng: ta chọn $10\%$ số người dùng và giữ mọi truy vấn của họ.

Hàm băm $\mathcal K\to\{0,\dots,b-1\}$ đóng vai bảng quyết định theo khóa. Cùng một khóa luôn cho cùng giá trị băm, do đó cùng quyết định, mà không cần lưu danh sách quyết định của từng khóa.

### Đặc tả

- Đầu vào: bộ $t$ có khóa $K(t)$; số nguyên $b\ge1$ và $0\le a\le b$; hàm $h:\mathcal K\to\{0,\dots,b-1\}$.
- Quy tắc: chọn $h$ sao cho mỗi giá trị trong $\{0,\dots,b-1\}$ có xác suất $1/b$, rồi giữ $t$ khi và chỉ khi $h(K(t))<a$.
- Một hàm $h$ đã chọn được giữ cố định cho toàn bộ dòng.

Dấu nhỏ hơn là để có đúng $a$ giá trị $\{0,\dots,a-1\}$ được nhận. Điều kiện để tỷ lệ là $a/b$ là $h$ phân bố **đều trên toàn miền**; nếu chỉ "gần đều" thì tỷ lệ $a/b$ không được bảo đảm.

<div class="figure">

![Các bộ cùng người dùng đi qua cùng hàm băm và được giữ toàn bộ khi giá trị băm nhỏ hơn ba](img/lec-08/key-sampling.svg)

</div>

Ví dụ $a=3, b=10$ cho tỷ lệ $30\%$: các khóa có giá trị băm $\{0,1,2\}$ được chọn. Hai bộ của cùng người dùng cùng được giữ vì có cùng khóa và cùng giá trị băm.

### Thuật toán

```text
LẤY-MẪU-THEO-KHÓA(t, a, b, h)
  K ← khóa_của(t)
  nếu h(K) < a: phát t vào dòng mẫu
  ngược lại: bỏ t
```

Điều kiện trước: $a,b$ thỏa đặc tả mẫu tỷ lệ $a/b$ và $h$ cố định. Điều kiện dừng: xử lý đúng một bộ. Hàm băm thay bảng quyết định theo khóa: mỗi lần một bộ đến chỉ cần tính $h(K)$, không cần tra cứu quyết định lưu trước.

### Tính đúng là tính nhất quán theo khóa

**Mệnh đề.** Với $b\ge1$, $0\le a\le b$ và hàm $h$ cố định, mọi bộ có cùng khóa đều được giữ hoặc đều bị bỏ.

**Lập luận.** Nếu $K(t)=K(t')$ thì $h(K(t))=h(K(t'))$; hai phép so sánh với cùng $a$ cho cùng kết quả.

Nếu $h$ được chọn sao cho mỗi giá trị trong $\{0,\dots,b-1\}$ có xác suất $1/b$, thì xác suất theo phép chọn $h$ để một khóa cố định được giữ là $a/b$.

Xác suất được hiểu theo phép chọn $h$, không theo các lần xuất hiện của khóa. Sau khi chọn, $h$ cố định. Mệnh đề không bảo đảm đúng $a/b$ số bộ khi tần suất khóa lệch: một khóa nặng có thể chiếm mọi bộ hoặc không có bộ nào.

### Chọn khóa

Khóa đi theo đơn vị thống kê mà thống kê sẽ gộp nhiều bộ:

1. Xác định đối tượng mà thống kê cần giữ trọn.
2. Chọn đủ thuộc tính để nhận diện duy nhất đối tượng đó.
3. Kiểm tra: hai bộ của cùng đối tượng phải nhận cùng quyết định theo khóa.

Nếu thống kê cần toàn bộ truy vấn của một người dùng, đơn vị là người dùng và khóa phải nhận diện người dùng. Nếu khóa gồm nhiều thành phần, hàm băm cần kết hợp các giá trị đó thành một giá trị băm duy nhất.

### Chi phí và giới hạn

- Chi phí mỗi bộ: một phép băm và một phép so sánh; trạng thái quyết định khóa là $O(1)$ ngoài dữ liệu mẫu.
- Giới hạn: mẫu tăng theo số bộ của các khóa được chọn và tăng khi dòng dài ra. Khóa "nặng" có thể chiếm nhiều bộ nhớ.

Do đó lấy mẫu theo khóa có chi phí thấp nhưng không bảo đảm kích thước mẫu cố định.

::: exercise Tự kiểm
Hàm $h$ ánh xạ vào $\{0,\dots,99\}$. Muốn chọn $20\%$ khóa, điều kiện nào đúng: $h(K)\le20$ hay $h(K)<20$? Mẫu này bảo đảm điều gì khi một khóa xuất hiện một triệu lần?
:::

::: solution
Dùng $h(K)<20$ để nhận đúng 20 ngăn. Khóa đó được giữ cả một triệu bộ hoặc bỏ cả một triệu bộ; thuật toán không bảo đảm mẫu có $20\%$ số bộ hay kích thước cố định.
:::

## 4. Điều chỉnh tỷ lệ mẫu bằng ngưỡng băm

Khi dòng dài dần, mẫu có thể vượt quá ngân sách. Nguồn đề xuất băm khóa vào miền lớn $\{0,\dots,B-1\}$ và duy trì ngưỡng $\tau$, ban đầu có thể là $B-1$. Mẫu gồm các bộ có khóa $K$ thỏa $h(K)\le\tau$. Đây là quy ước tương đương với điều kiện nhỏ hơn ở phần trước sau khi dịch ngưỡng một đơn vị. Khi mẫu vượt ngân sách, hạ $\tau$ và loại các bộ ở mức vừa bỏ.

Chỉ cần ngưỡng hiện tại và cùng hàm $h$ để tái lập quyết định; không cần nhớ quyết định cũ của từng khóa. Việc hạ ngưỡng làm thay đổi tập khóa được chọn. Phần tiếp theo chuyển sang yêu cầu khác: giữ mẫu kích thước cố định theo vị trí.

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

Vết chạy với $s=2$, dòng $a,x,c,y,z$ và các số ngẫu nhiên $j$ lần lượt là $j=2,4,1$:

| Bước $r$ | Phần tử | $j$ | Trạng thái $S$ |
|---|---|---|---|
| 1 | a | — | a |
| 2 | x | — | a x |
| 3 | c | 2 | a c |
| 4 | y | 4 ($>s$) | a c |
| 5 | z | 1 | z c |

Ở $r=3$ thì $j=2\le s$ nên $c$ thay ô 2. Ở $r=4$ thì $j=4>s$ nên bỏ $y$. Ở $r=5$ thì $j=1$ nên $z$ thay ô 1. Số $j$ ở đây chỉ là một lần chạy minh họa, không phải xác suất bảo đảm; chúng phụ thuộc vào bộ sinh số ngẫu nhiên.

### Thuật toán

```text
HỒ-CHỨA(x_r, r, s, S)
  nếu r ≤ s: S[r] ← x_r
  ngược lại:
    j ← số nguyên đều trong {1,…,r}
    nếu j ≤ s: S[j] ← x_r
  trả S
```

Với $r>s$, sinh $j$ đều trong $1,\dots,r$ và chèn phần tử mới vào ô $j$ khi $j\le s$ tương đương với: giữ phần tử mới với xác suất $s/r$, rồi chọn đều một trong $s$ ô để thay. Mỗi lần gọi cần phép sinh mẫu đều và độc lập có điều kiện với lịch sử.

### Bất biến và chứng minh quy nạp

**Mệnh đề.** Sau khi xử lý $r\ge s$ vị trí, hồ chứa có đúng $s$ phần tử và mỗi vị trí $i\le r$ có xác suất $s/r$ nằm trong hồ.

**Cơ sở $r=s$.** Giữ cả $s$ vị trí, nên xác suất là $1=s/s$.

Giả sử đúng với $r$. Xét bước $r+1$.

**(a) Phần tử mới.** Phần tử mới $x_{r+1}$ vào hồ khi $j\le s$:

$$\Pr[x_{r+1}\in S]=\frac{s}{r+1}.$$

**(b) Phần tử cũ.** Với điều kiện phần tử cũ đang trong $S$, nó bị thay khi $j\le s$ và $j$ đúng ô của nó:

$$\Pr[\text{bị thay}]=\frac{s}{r+1}\cdot\frac{1}{s}=\frac{1}{r+1}.$$

Vì vậy xác suất sống sót của phần tử cũ qua bước $r+1$ là

$$\frac{s}{r}\cdot\left(1-\frac{1}{r+1}\right)=\frac{s}{r}\cdot\frac{r}{r+1}=\frac{s}{r+1}.$$

Kích thước đúng $s$ được duy trì vì bước $r>s$ hoặc không đổi $S$, hoặc thay đúng một ô.

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
