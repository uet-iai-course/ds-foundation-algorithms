# Bài 10 — Nén dữ liệu không mất thông tin

Xem bộ trang chiếu tại [Bài 10 — Nén dữ liệu không mất thông tin](../../lecture-10-nen-du-lieu-khong-mat-thong-tin.html).

Một kho dữ liệu có phân phối ký hiệu lệch có thể được biểu diễn bằng ít bit hơn so với mã có độ dài cố định, nhưng bộ giải nén chỉ khôi phục chính xác khi biết cùng bảng chữ cái, cùng mô hình xác suất, cùng quy tắc tạo mã và cùng điều kiện kết thúc. Bài này trình bày ba cặp mô hình–bộ mã trong phạm vi được học: tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học.

Người học cần biết xác suất cơ bản, logarit cơ số 2, cây nhị phân và hàng đợi ưu tiên.

## 1. Bài toán khôi phục chính xác và hai trục lựa chọn

Nén không mất thông tin nhận đầu vào là bảng chữ cái $\Sigma$, thông điệp $x_1\ldots x_n$ và tần suất hoặc xác suất của các ký hiệu, rồi sinh một dòng bit sao cho bộ giải nén tái tạo đúng thông điệp ban đầu. Không có hai thông điệp khác nhau được cho cùng một dòng bit.

Lựa chọn thuật toán được tách thành hai trục độc lập.

- **Trục mô hình xác suất.** Mô hình là cách ước lượng tần suất hay xác suất của các ký hiệu. Mô hình tĩnh đếm trước rồi dựng toàn bộ cấu trúc; mô hình cập nhật bắt đầu từ một quy ước rồi điều chỉnh dần khi đọc thông điệp.
- **Trục bộ mã hóa.** Bộ mã biến mô hình thành dòng bit. Bộ mã Huffman gán cho mỗi ký hiệu một từ mã có độ dài nguyên bit; bộ mã số học thu hẹp một khoảng cho cả chuỗi ký hiệu.

Hai trục kết hợp thành bảng lựa chọn với bốn ô. Bài này đi sâu vào ba ô: tĩnh + Huffman, cập nhật + Huffman và tĩnh + số học. Ô cập nhật + số học nằm ngoài phạm vi bài. Mô hình quyết định lượng dữ liệu thống kê phải gửi; bộ mã quyết định độ dài dòng bit. Cần tính cả hai khoản.

Vì giải mã chỉ đúng khi hai phía thống nhất, một giao thức phải mang bốn nhóm thông tin:

1. bảng chữ cái và cách biểu diễn ký hiệu mới;
2. mô hình tĩnh hoặc quy tắc cập nhật mô hình;
3. cây với nhãn nhánh, hoặc phân hoạch khoảng cùng quy tắc chuẩn hóa;
4. cách kết thúc, là ký hiệu kết thúc `EOS` hoặc độ dài thông điệp truyền kèm.

::: exercise Tự kiểm
Hai bộ cài đặt Huffman nhận cùng bảng tần suất nhưng phá hòa theo hai quy tắc khác nhau. Chỉ gửi dòng bit có đủ để bộ giải nén khôi phục thông điệp không? Nêu thông tin còn thiếu.
:::

::: solution
Không. Phá hòa có thể tạo các cây và bảng mã khác nhau dù chi phí tổng bằng nhau. Hai phía phải dùng cùng cây, hoặc cùng quy tắc dựng cây và phá hòa.
:::

## 2. Mã tiền tố và bất đẳng thức Kraft

Một mã là mã tiền tố nếu không từ mã nào là tiền tố của từ mã khác. Tính chất này cho phép đọc dòng bit từ trái sang phải và dừng đúng lúc chạm một lá của cây.

![Cây mã tiền tố với các lá 0, 10, 110, 111 và tám ô sức chứa theo Kraft](img/lec-10/prefix-tree-kraft.svg)

Mã tiền tố là điều kiện đủ thuận tiện cho giải mã duy nhất, nhưng không phải toàn bộ lớp mã giải mã duy nhất: tồn tại mã giải mã duy nhất mà không phải mã tiền tố. Vì thế không đồng nhất hai khái niệm.

Để đo sức chứa của một cây, xét một cây nhị phân đầy đủ ở độ sâu $d$. Một từ mã độ dài $\ell$ chiếm $2^{d-\ell}$ lá ở độ sâu $d$. Vì các từ mã của một mã tiền tố không đi qua một lá đã dùng, các miền bị chiếm rời nhau. Do đó

$$\sum_{s\in\Sigma}2^{-\ell_s}\le1.$$

Đây là bất đẳng thức Kraft. Nó mô tả miền các bộ độ dài khả thi của một mã tiền tố, chứ không phải cách tìm mã tối ưu. Với bốn từ mã 0, 10, 110, 111,

$$\frac12+\frac14+\frac18+\frac18=1,$$

nghĩa là toàn bộ sức chứa của cây đã được dùng. Nếu tổng nhỏ hơn 1 thì còn miền trống để thêm từ mã; nếu lớn hơn 1 thì không mã tiền tố nào có bộ độ dài như vậy tồn tại. Bài toán tối ưu hóa độ dài diễn ra trong miền khả thi này, còn bản thân Kraft không tối ưu hóa gì.

## 3. Huffman tĩnh: dựng cây, mã hóa, giải mã và tính tối ưu

### Dựng cây từ dưới lên

Huffman tĩnh dựng cây từ các lá lên gốc, ngược với cách chia nhóm từ gốc xuống. Thuật toán dùng hàng đợi ưu tiên:

```text
Q ← các lá (ký hiệu, tần suất)
while |Q| > 1:
  u ← lấy ra nút nhẹ nhất khỏi Q
  v ← lấy ra nút nhẹ nhất còn lại khỏi Q
  w ← nút trong trọng số u.w + v.w
  gắn u, v làm hai con của w; đưa w vào Q
return nút còn lại
```

Điều kiện dừng là còn đúng một cây chứa mọi ký hiệu.

### Ví dụ năm ký hiệu A–E

Theo Nelson–Gailly, bảng tần suất là

| Ký hiệu | A | B | C | D | E |
|---|---:|---:|---:|---:|---:|
| Tần suất | 15 | 7 | 6 | 6 | 5 |

Tổng cộng 39 ký hiệu. Bốn lượt ghép lần lượt là

$$5+6=11,\qquad 6+7=13,\qquad 11+13=24,\qquad 15+24=39.$$

![Bốn lượt ghép Huffman từ A–E thành các nút 11, 13, 24, 39](img/lec-10/huffman-merge-a-e.svg)

Mỗi lượt ghép hai trọng số nhỏ nhất và giảm số cây tự do đi một, nên dựng cây dừng sau $k-1$ lượt với $k$ là số ký hiệu phân biệt. Hòa giữa C và D (cùng trọng số 6) được phá tùy ý: nó đổi từ mã cụ thể nhưng không đổi chi phí tổng nếu quy tắc được giữ nhất quán.

Từ cây, đọc từ gốc đến lá cho bảng mã của sách:

| Ký hiệu | A | B | C | D | E |
|---|---|---|---|---|---|
| Từ mã | 0 | 100 | 101 | 110 | 111 |
| Số bit đóng góp | 15 | 21 | 18 | 18 | 15 |

Số bit đóng góp là tích tần suất với độ dài từ mã. Tổng là

$$15+21+18+18+15=87\text{ bit}.$$

Cùng ví dụ mà dùng mã tám bit cho mọi ký hiệu thì cần $39\times8=312$ bit, nên Huffman giảm đáng kể.

### Giải mã bằng đường gốc–lá

![Cây Huffman A–E với đường 101 được tô nổi và kết thúc tại lá C](img/lec-10/huffman-code-decode.svg)

Giải mã là một bước đi trên cây: bắt đầu từ gốc, đọc từng bit để chọn cạnh 0 hoặc 1, dừng khi chạm lá, xuất ký hiệu rồi khởi động lại từ gốc. Vì mỗi ký hiệu nằm ở một lá và không có lá nào là tổ tiên của lá khác, không từ mã nào là tiền tố của từ mã khác. Đọc bit luôn chọn đúng một cạnh, nên ranh giới giữa các ký hiệu được xác định ngay khi chạm lá.

### Tính tối ưu

Mệnh đề cần chứng minh: tồn tại một mã tiền tố tối ưu trong đó hai ký hiệu nhẹ nhất là hai lá anh em sâu nhất.

Đặt chi phí của cây $T$ là

$$\operatorname{cost}(T)=\sum_s f_s\ell_s.$$

Chứng minh dùng hai phép đổi rồi co cặp và quy nạp. Gọi $x,y$ là hai ký hiệu nhẹ nhất và $a,b$ là cặp lá anh em sâu nhất. Một phép đổi giữa trọng số nhẹ $f_x$ ở độ sâu $\ell_x$ và trọng số $f_a\ge f_x$ ở độ sâu $\ell_a\ge\ell_x$ tạo độ chênh

$$(f_x-f_a)(\ell_a-\ell_x)\le0,$$

nên đưa trọng số nhẹ xuống sâu hơn không làm tăng tổng. Sau phép đổi thứ nhất, lá còn lại trong cặp anh em vẫn ở độ sâu lớn nhất; áp dụng cùng lập luận cho ký hiệu nhẹ thứ hai. Hai phép đổi đưa $x,y$ về đúng vị trí hai lá anh em sâu nhất.

Sau đó co cặp $x,y$ thành một lá trọng số $f_x+f_y$. Nếu cây co chưa tối ưu, có một cây tốt hơn; thay nó vào sẽ cải thiện cây ban đầu, mâu thuẫn. Vậy cây con sau khi co phải tối ưu. Lặp lập luận trên bài toán nhỏ hơn là một phép quy nạp cho phép ghép hai nút nhẹ nhất ở mỗi lượt.

Phá hòa có thể đổi mã cụ thể nhưng không đổi chi phí tối ưu.

### Chi phí và đầu mục

Dựng cây với hàng đợi ưu tiên tốn $O(k\log k)$; mã hóa tuyến tính theo số bit đầu ra. Nhược điểm của mô hình tĩnh là phải gửi bảng tần suất hoặc đủ dữ liệu để tái dựng đúng cây. Đây là khoản đầu mục mà mô hình cập nhật ở phần sau sẽ tránh được.

## 4. Huffman thích nghi: đồng bộ, ESCAPE, EOS và ký hiệu mới

Huffman tĩnh cần lượt đếm trước hoặc gửi bảng tần suất. Với dòng dữ liệu chỉ đi qua một lần và chưa biết ký hiệu nào xuất hiện, phải bắt đầu từ một cây quy ước rồi cập nhật theo dữ liệu đã thấy, không biết gì về tương lai.

![Hai đường ống nén và giải nén cùng khởi tạo cây, mã hóa/giải mã rồi cập nhật cây](img/lec-10/escape-eof-pipelines.svg)

Hai phía phải cùng khởi tạo và áp dụng cùng quy tắc cập nhật theo cùng thứ tự. Vì chỉ trao đổi qua dòng bit, mỗi phía suy ra mô hình từ dữ liệu đã nhận theo quy ước chung.

Cây ban đầu chứa hai lá đặc biệt: `ESCAPE` và `EOS`, mỗi lá trọng số 1. Khi gặp một ký hiệu chưa có trong cây:

```text
Ký hiệu mới: E
1. phát mã(ESCAPE)
2. phát 01000101
3. chẻ nút nhẹ nhất; thêm lá E:0
4. UpdateModel(E): E và tổ tiên +1
```

Với ký hiệu mới: phát mã của lá `ESCAPE` như một ký hiệu thường, rồi ngay sau đó phát đúng tám bit thô của ký hiệu. Tiếp theo, chẻ nút nhẹ nhất hiện có thành một nút trong với lá cũ và lá mới trọng số 0. Sau đó cả hai phía gọi cùng quy tắc cập nhật cho E: lá E tăng từ 0 lên 1 và các tổ tiên tăng một.

Hai trọng số khác nhau: lá `ESCAPE` có sẵn trong cây với trọng số khởi tạo 1; lá ký hiệu mới vừa chèn có trọng số 0. Lá mới được cập nhật ngay trong cùng bước, trước khi bộ giải mã dùng cây cho ký hiệu kế tiếp.

`EOS` là ký hiệu kết thúc dòng. Bộ giải nén dừng khi đọc được lá này.

### Tính chất anh em

Một cây Huffman là cây nhị phân có trọng số gán cho mọi nút. Cây thỏa tính chất anh em nếu có thể liệt kê các nút theo trọng số không giảm sao cho hai nút cùng cha đứng kề nhau. Một cây nhị phân đầy đủ là cây Huffman khi và chỉ khi nó thỏa tính chất anh em. Vì vậy, duy trì tính chất này qua mỗi lần tăng bảo đảm cây vẫn là cây Huffman trước và sau khi cập nhật.

## 5. Huffman thích nghi: tăng, đổi nút, bất biến và chống tràn

Tăng trọng số bắt đầu từ lá của ký hiệu, lên cha, rồi tới gốc. Số mức đi qua bằng độ sâu của lá đó trong cây.

### Lần tăng trong Hình 4.2

![Toàn bộ cây Hình 4.2: tăng A rồi các tổ tiên đến gốc, nhánh E giữ nguyên](img/lec-10/adaptive-sibling-increment.svg)

Trên toàn cây Hình 4.2, tăng A từ 1 lên 2, nút trong số 5 tăng từ 3 lên 4, nút số 7 tăng từ 7 lên 8 và gốc số 9 tăng từ 17 lên 18. Nút số 6 và E giữ nguyên vì chúng không nằm trên đường cập nhật. Hình thực chất là một sơ đồ chuyển tiếp: các mũi tên hiển thị đợt tăng đã xảy ra.

### Lần tăng gây vi phạm tính chất anh em

Sau trạng thái cuối Hình 4.2, A, B, C, D cùng trọng số 2. Lần quan sát A tiếp theo tăng A từ 2 lên 3:

$$A:2,\ B:2,\ C:2,\ D:2\qquad\not\to\qquad A:3,\ B:2,\ C:2,\ D:2.$$

A vượt qua khối ba nút trọng số 2 đứng sau nó trong danh sách, làm mất thứ tự không giảm của tính chất anh em. Cần đưa A lên vị trí cao hơn.

### Đổi nút rồi đi từ cha mới

![Toàn bộ cây Hình 4.3 sau khi A tăng lên ba và đổi với D, trước khi tăng các tổ tiên](img/lec-10/adaptive-swap.svg)

Khi nút vừa tăng có trọng số $W+1$ nhưng nút kế tiếp trong danh sách vẫn $W$, ta di chuyển lên danh sách tới nút cuối cùng có trọng số $W$ và đổi cho nút vừa tăng. Trong ví dụ này, A tăng từ 2 lên 3 và đổi với D. Hình 4.3 chụp ngay sau phép đổi: nút số 6 vẫn ghi 4, nút số 7 vẫn ghi 8 và gốc vẫn ghi 18, vì chỉ A đã tăng. Bước kế tiếp tăng cha mới của A là nút số 6, rồi đường cập nhật tiếp tục lên nút số 7 và gốc. Một phép đổi chỉ tráo hai cây con; không đổi một nút với tổ tiên của chính nó để tránh tạo chu trình.

### Giả mã cập nhật

```text
if gốc.w = MAX_WEIGHT:
  mọi lá.w ← (lá.w + 1) // 2
  dựng lại cây từ các lá

v ← lá của ký hiệu
loop:
  w_cũ ← v.w; v.w ← w_cũ + 1
  if v = gốc: break
  if thứ tự trọng số bị vi phạm:
    u ← nút cuối của khối w_cũ, không là tổ tiên của v
    đổi hai cây con tại u, v
  v ← cha hiện tại của v
```

Thủ tục tăng đi từ lá lên gốc, tăng nút, dừng ngay tại gốc, rồi nếu thứ tự bị vi phạm thì tìm nút cuối hợp lệ của khối trọng số cũ, đổi hai cây con và lấy cha sau phép đổi.

### Chống tràn và dựng lại

Hai vấn đề có thể xảy ra khi trọng số lớn dần. Thứ nhất, trọng số của gốc có thể vượt quá sức chứa bộ đếm. Thứ hai, mã dài nhất có thể vượt quá kích thước thanh ghi dùng để truyền mã. Chiều dài mã xấu nhất liên hệ với dãy Fibonacci, nên ngưỡng xuất hiện sớm hơn người ta tưởng. Khi gốc đạt ngưỡng, thay trọng số mỗi lá bằng $(w+1)//2$ rồi dựng lại cây từ các lá. Phép làm tròn này giữ mọi ký hiệu đã thấy ở trọng số dương.

Dựng lại nhằm chống tràn và giới hạn độ dài mã. Việc giảm trọng số cũng làm nhẹ ảnh hưởng của dữ liệu cũ; nguồn quan sát rằng tác dụng này đôi khi cải thiện tỷ lệ nén. Dựng lại không bảo đảm mô hình sẽ bám theo một phân phối đang thay đổi.

### Ba bất biến

Ba bất biến giữ hai phía đồng bộ:

1. Trước mỗi ký hiệu, hai phía có cùng cây.
2. Sau mỗi phép tăng, đổi hoặc dựng lại, cây giữ tính chất anh em.
3. Lá mới vào cây với trọng số 0 rồi được cập nhật ngay trong cùng bước.

Cơ sở quy nạp là cây ban đầu chứa `ESCAPE` và `EOS`. Với ký hiệu đã biết, hai phía dùng cùng cây rồi chạy cùng quy tắc cập nhật. Với ký hiệu mới, cả hai đọc cùng tám bit, chẻ cùng nút nhẹ nhất, đặt lá mới trọng số 0 rồi cập nhật từ lá đó. Khi gốc cùng đạt ngưỡng, hai phía dùng cùng phép làm tròn, cùng quy tắc phá hòa và cùng thủ tục tái dựng nên nhận lại cùng cây.

### Chi phí và giới hạn

Cập nhật thường đi theo đường từ lá đến gốc; mỗi mức có thể cần tìm cuối khối và đổi con trỏ. Dựng lại toàn cây là thao tác hiếm nhưng đắt hơn một đường cập nhật. Chi phí cụ thể phụ thuộc cách lưu danh sách nút, chỉ mục khối và con trỏ cha.

## 6. Mã số học lý tưởng với khoảng nửa mở

Huffman gán một từ mã nguyên bit cho mỗi ký hiệu. Nếu xác suất không phải là bội số cơ số 2, số bit tối ưu $-\log_2 p$ không phải số nguyên và việc làm tròn riêng từng ký hiệu là lãng phí. Mã số học tránh điều này bằng cách mã cả chuỗi thành một khoảng.

Nelson–Gailly minh họa bằng nguồn 100.000 số 0:

$$p(0)=\frac{16382}{16383},\qquad p(\mathrm{EOS})=\frac1{16383}.$$

Mã Huffman vẫn phải dùng ít nhất một bit cho mỗi ký hiệu và cho tệp ít nhất 12.501 byte; mã số học cho tệp dài 3 byte. Ví dụ này cho thấy mã khoảng có thể vượt qua ngưỡng một bit mỗi ký hiệu, không phải mọi dữ liệu đều đạt mức nén đó.

### Phân hoạch khoảng bằng xác suất tích lũy

Với mỗi ký hiệu $s$, chọn $0\le C_s<D_s\le1$ và $D_s-C_s=p_s$. Các ký hiệu phân hoạch

$$[0,1)=\bigsqcup_{s\in\Sigma}[C_s,D_s).$$

Khoảng nửa mở làm mỗi điểm biên thuộc đúng một ký hiệu. Hai phía phải dùng cùng thứ tự ký hiệu và cùng bảng tích lũy.

### Ví dụ "BILL GATES"

Bảng chín ký hiệu của Nelson–Gailly:

| Ký hiệu | Khoảng |
|---|---|
| khoảng trắng | $[0.0,0.1)$ |
| A | $[0.1,0.2)$ |
| B | $[0.2,0.3)$ |
| E | $[0.3,0.4)$ |
| G | $[0.4,0.5)$ |
| I | $[0.5,0.6)$ |
| L | $[0.6,0.8)$ |
| S | $[0.8,0.9)$ |
| T | $[0.9,1.0)$ |

![Khoảng B, BI, BIL vẽ đúng tỷ lệ trong từng mức phóng đại; khoảng cuối quá hẹp nên chỉ đánh dấu vị trí](img/lec-10/arithmetic-bill-gates.svg)

Mỗi ký hiệu thu hẹp khoảng. Sau B:

$$[0.2,\ 0.3),$$

sau I:

$$[0.25,\ 0.26),$$

sau L:

$$[0.256,\ 0.258).$$

Toàn bộ thông điệp rơi về

$$[0.2572167752,\ 0.2572167756).$$

### Công thức thu hẹp

Với khoảng hiện tại $[L,H)$ và ký hiệu $s$,

$$L'=L+(H-L)C_s,\qquad H'=L+(H-L)D_s.$$

Điều kiện trước là $0\le C_s<D_s\le1$. Cần lưu $L$ cũ khi tính $H$ và $L$ mới.

Bất biến: sau $t$ ký hiệu, $[L_t,H_t)$ chứa đúng các số đại diện cho thông điệp có tiền tố đã mã hóa. Cơ sở là mọi thông điệp nằm trong $[0,1)$. Bước quy nạp ánh xạ đoạn $[C_s,D_s)$ vào khoảng hiện tại. Vì các đoạn con rời nhau, một số trong khoảng cuối xác định duy nhất chuỗi khi biết cách dừng.

### Giải mã và cách dừng

![Giải mã số 0,2572167752 thành B rồi chuẩn hóa để nhận I](img/lec-10/arithmetic-decode-normalize.svg)

Giải mã chọn khoảng chứa giá trị $x$ rồi chuẩn hóa ngược:

$$x'=\frac{x-C_s}{D_s-C_s}.$$

Với $x=0.2572167752$, điểm này thuộc khoảng của B là $[0.2,0.3)$; trừ 0,2 rồi chia 0,1 cho $x'=0.572167752$, thuộc khoảng của I là $[0.5,0.6)$. Lặp phép chọn và chuẩn hóa để nhận BILL GATES.

Giải mã cần biết khi nào dừng. Hai cách phổ biến là dùng ký hiệu kết thúc `EOS` (thêm một khoảng riêng) hoặc truyền kèm độ dài thông điệp rồi giải mã đúng số ký hiệu. Nếu thiếu cả hai, cùng một tiền tố bit có thể cho nhiều cách dừng. Cách chọn chuỗi bit đại diện và xử lý các bit chờ được nêu ở phần 7.

## 7. Chuẩn hóa hữu hạn, tiền tố chung, underflow và bit chờ

Học phần này tách rõ mô hình lý tưởng khỏi cài đặt số nguyên hữu hạn. Giả mã dưới đây viết các ngưỡng trên khoảng chuẩn hóa $[0,1)$. Trong cài đặt, $L$, $H$ và các ngưỡng $1/4$, $1/2$, $3/4$ được nhân với cùng kích thước thanh ghi để trở thành số nguyên. Sau mỗi ký hiệu, bộ mã phát tiền tố bit đã xác định, dịch và mở rộng khoảng; bộ giải nén thực hiện cùng các phép dịch.

Trạng thái chuẩn hóa dùng biến `pending` khởi tạo đúng một lần trước toàn bộ thông điệp và được giữ xuyên các ký hiệu. Sau mỗi lần thu hẹp, kiểm tra ba nhánh theo thứ tự loại trừ:

```text
pending ← 0
lặp sau mỗi lần thu hẹp:
  if E1 (H ≤ 1/2):
    phát 0 rồi pending bit 1
    [L,H) ← [2L, 2H)
    pending ← 0
  else if E2 (L ≥ 1/2):
    phát 1 rồi pending bit 0
    [L,H) ← [2L−1, 2H−1)
    pending ← 0
  else if E3 (L ≥ 1/4, H ≤ 3/4):
    pending++; [L,H) ← [2L−1/2, 2H−1/2)
  else: dừng chuẩn hóa
```

![Ba nhánh E1, E2 và E3 theo thứ tự kiểm tra với phép biến đổi khoảng nửa mở](img/lec-10/arithmetic-renormalization.svg)

- Nhánh E1 (tiền tố chung trái) xảy ra khi cả khoảng nằm ở nửa dưới; phát bit 0 rồi các bit bù 1 đang chờ, dịch trái.
- Nhánh E2 (tiền tố chung phải) xảy ra khi cả khoảng nằm ở nửa trên; phát bit 1 rồi các bit bù 0 đang chờ, dịch trái và trừ 1.
- Nhánh E3 (underflow) xảy ra khi khoảng nằm gọn giữa 1/4 và 3/4; chỉ tăng `pending` mà chưa phát bit, rồi dịch giữa.

Khi `EOS` hoặc độ dài đã biết kết thúc thông điệp, bộ mã chọn một chuỗi bit nhị phân biểu diễn một điểm nằm trong khoảng cuối. Sau đó nó phát bit đã xác định cùng các bit bù đang chờ và đệm theo định dạng mà hai phía đã thống nhất. Bộ giải nén phản chiếu các phép dịch và dùng cùng quy tắc hoàn tất.

## 8. Độ rộng khoảng, tự thông tin và entropy

Mã hóa số học thu hẹp khoảng theo đúng xác suất của chuỗi, nên độ rộng khoảng cuối bằng $P(x_1\ldots x_n)$. Số bit cần để chỉ ra một điểm trong khoảng hẹp tỷ lệ với âm logarit độ rộng. Điều này nối chuẩn hóa hữu hạn với chi phí của một chuỗi cụ thể.

Tự thông tin của một chuỗi cụ thể $x=x_1\ldots x_n$ là

$$I(x)=-\log_2 P(x_1\ldots x_n).$$

Đây là đại lượng gắn với một thông điệp cụ thể, không phải giá trị trung bình. Entropy của phân phối $P$ là trung bình theo phân phối:

$$H(P)=\sum_s p(s)(-\log_2 p(s)).$$

Hai đại lượng khác nhau: một chuỗi hiếm có tự thông tin cao dù entropy của nguồn thấp. Khoảng cuối có độ rộng đúng $P(x_1\ldots x_n)$, vậy số bit của một chuỗi cụ thể gắn với $I(x)$ của chuỗi đó.

Chỉ với nguồn không nhớ, xác suất chuỗi mới tách thành tích theo từng ký hiệu và

$$I(x_1\ldots x_n)=\sum_{i=1}^n-\log_2 p(x_i).$$

Nếu nguồn không nhớ chưa được nêu, không được giả định phép tách này: phải dùng xác suất của cả chuỗi.

## 9. So sánh ba cặp mô hình–bộ mã và điều kiện giao thức

| Cặp lựa chọn | Bộ nhớ | Công việc chính | Điều kiện giao thức |
|---|---|---|---|
| Tĩnh + Huffman | $O(k)$ cho cây/bảng | đi một đường mã | truyền hoặc tái dựng cây |
| Cập nhật + Huffman | $O(k)$ cho cây và tra cứu lá | đi đường cao $h$; có thể đổi nút | cùng khởi tạo, cập nhật và dựng lại |
| Tĩnh + số học | $O(k)$ cho bảng tích lũy | tìm khoảng và chuẩn hóa | cùng số học hữu hạn và cách dừng |

Ở đây $k$ là số ký hiệu trong mô hình và $h$ là số mức trên đường đang xử lý. Bảng chỉ nêu cấu trúc được lưu và các thao tác nguồn mô tả; thời gian tìm cuối khối, tìm khoảng hoặc dựng lại phụ thuộc cách cài đặt. Không suy ra một cặp luôn tốt hơn từ bảng này.

Bốn nhóm thông tin giao thức ở phần 1 áp dụng xuyên suốt. Chọn cặp nào phải viện dẫn ràng buộc cụ thể rồi nêu đủ điều hai phía cần thống nhất: cây hay bảng tích lũy, quy tắc cập nhật và cách dừng.

## 10. Bài tập củng cố

Ba bài dưới đây giữ nguyên dữ kiện của nguồn; lời giải được trình bày để tự kiểm.

::: exercise
**Bài luyện từ Nelson–Gailly — Dựng mã Huffman cho A–E.** Cho tần suất A=15, B=7, C=6, D=6, E=5.

1. Ghi bốn lượt ghép.
2. Vẽ cây, chọn nhánh 0/1 và lập bảng mã.
3. Mã hóa đầy đủ 39 ký hiệu theo tần suất và tính tổng số bit.
4. Nêu ảnh hưởng của cách phá hòa C–D.
:::

::: solution
Bốn lượt ghép là

$$5+6=11,\qquad 6+7=13,\qquad 11+13=24,\qquad 15+24=39.$$

Theo lựa chọn của sách, bảng mã là A=0, B=100, C=101, D=110, E=111. Số bit đóng góp lần lượt là $15,21,18,18,15$, nên

$$15+21+18+18+15=87\text{ bit}.$$

Đổi C và D khi hòa làm đổi mã cụ thể nhưng giữ độ dài bằng nhau và không đổi tổng 87 bit, miễn quy tắc nhất quán.
:::

::: exercise
**Bài luyện từ Nelson–Gailly — Cập nhật A và khôi phục tính chất anh em.** Dùng các giá trị sau mũi tên làm trạng thái đầu: A=B=C=D=2; nút số 5 = số 6 = 4; nút số 7 = 8; gốc số 9 = 18.

![Cây thích nghi ở trạng thái đầu: A, B, C, D cùng trọng số 2; hai nút trong 5 và 6 cùng trọng số 4; nút 7 trọng số 8 và gốc 9 trọng số 18](img/lec-10/adaptive-sibling-increment.svg)

1. Thực hiện một lần tăng A từ 2 lên 3.
2. Chỉ ra vi phạm và nút đổi chỗ với A.
3. Ghi cha mà thuật toán xử lý tiếp.
4. Nêu hai bất biến cần giữ ở hai phía.
:::

::: solution
Sau lần tăng A lên 3, A vượt khối trọng số 2 gồm B, C, D đứng sau nó, làm mất thứ tự không giảm của tính chất anh em. Theo quy tắc phá hòa dùng chung, di chuyển đến cuối khối trọng số 2 là D và đổi A với D. Bước tiếp theo tăng cha mới của A là nút số 6. Hai bất biến: cả hai phía có cùng cây, và cây giữ tính chất anh em sau mỗi lần cập nhật.
:::

::: exercise
**CMU Assignment 1a, Problem 3 — Giải mã một dòng bit số học.** Mô hình: $p(a)=0.1$, $p(b)=0.2$, $p(c)=0.7$ và các khoảng $[0,0.1)$, $[0.1,0.3)$, $[0.3,1)$. Dòng bit $0.01001110110_2$ biểu diễn một số. Giải mã đúng bốn ký hiệu; giải thích độ dài 11 bit.
:::

::: solution
Giá trị của dòng nhị phân là $0.3076171875$. Giải mã được là caba. Bốn khoảng toàn cục là: c: $[0.3,1)$; a: $[0.3,0.37)$; b: $[0.307,0.321)$; a: $[0.307,0.3084)$. Xác suất chuỗi bằng $0.0014$, nên tự thông tin xấp xỉ $9.48$ bit. Biểu diễn 11 bit trong đề là một biểu diễn nguồn cung cấp, không nhất thiết ngắn nhất; định dạng kết thúc và đệm quyết định chuỗi bit hoàn chỉnh.
:::

## Tóm tắt nguồn

- Nelson–Gailly, *The Data Compression Book*, Chương 3–5 là nguồn trục: dữ liệu A–E và Huffman tĩnh ở Chương 3; biến thể Huffman thích nghi ở Chương 4 và `ESCAPE`, `EOS`, tính chất anh em, phép đổi và dựng lại; ví dụ "BILL GATES", kết thúc dòng, số học hữu hạn, underflow và 100.000 số 0 ở Chương 5.
- CMU 15-499 Assignment 1a là nguồn cho bất đẳng thức Kraft (Problem 4) và bài giải mã số học Problem 3. Stanford EE398A đối chiếu Huffman, số học hữu hạn và phép dịch; Stanford CS106B hỗ trợ cách kể bằng cây và hàng đợi ưu tiên.
- Hai bài luyện Huffman dùng dữ kiện trong ví dụ của Nelson–Gailly; bài giải mã số học là CMU Assignment 1a, Problem 3.

Shannon–Fano chi tiết, các biến thể Huffman thích nghi khác, Lempel–Ziv và nén mất dữ liệu không nằm trong bài này.
