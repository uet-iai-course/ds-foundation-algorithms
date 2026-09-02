# Bài 1: Bài toán dữ liệu lớn và mô hình thuật toán

Một kho dữ liệu web lưu metadata của các trang. Cần tính tổng kích thước theo từng máy chủ, nhưng toàn bộ kho không vừa bộ nhớ chính. Đây là một ví dụ điển hình về vai trò của giải thuật trong Khoa học dữ liệu: phép tính cần thực hiện chỉ là cộng, còn quy mô dữ liệu khiến cách làm trực tiếp không còn khả thi. Muốn biến yêu cầu phân tích thành một lời giải chạy được, ta phải chọn mô hình truy cập, thiết kế thuật toán có thể chứng minh tính đúng và phân tích chi phí tính toán, bộ nhớ cùng truyền dữ liệu. [Bộ trang chiếu Bài 01](lecture-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.html) dùng cùng ký hiệu và ví dụ.

## Kho nhật ký không vừa bộ nhớ

Kho dữ liệu web lưu metadata của các trang dưới dạng các dòng $(u_i, s_i)$, trong đó $u_i$ là máy chủ (host) chứa trang và $s_i$ là kích thước trang tính bằng byte. Nguồn ví dụ là trang chiếu 62 của Stanford CS246 `01-intro.pdf`: với mỗi máy chủ, cần tìm tổng số byte, tức tổng kích thước của mọi URL thuộc máy chủ đó.

Gọi $D$ là kích thước toàn bộ dữ liệu và $M$ là dung lượng bộ nhớ chính khả dụng. Khi $D > M$, kho nhật ký không vừa bộ nhớ. MMDS cho biết truy cập một khối dữ liệu trên đĩa chậm hơn ít nhất năm bậc độ lớn so với đọc một từ trong bộ nhớ chính; với dữ liệu cỡ hàng trăm gigabyte hoặc terabyte, riêng việc đọc dữ liệu đã đáng kể (MMDS 3e, trang 13).

![Kho nhật ký web lớn hơn bộ nhớ chính; dữ liệu được quét một lượt từ bộ lưu trữ ngoài vào bộ nhớ nhỏ hơn, giữ một bảng tổng theo máy chủ](img/lec-01/kho-nhat-ky-bo-nho.svg)

Dữ liệu nằm ngoài bộ nhớ và được đọc tuần tự; bộ nhớ chỉ giữ một bảng tổng nhỏ. Bài toán phải xác định rõ kết quả cần tính, lập luận chứng minh tính đúng và các chi phí phải trả.

Tự kiểm tra: nếu $D > M$, phần nào của dữ liệu nằm ngoài bộ nhớ chính, và trạng thái tối thiểu cần giữ trong bộ nhớ khi tính tổng kích thước theo từng máy chủ?

## Dữ liệu hiện đại và giới hạn RAM

Tình huống trên không phải ngoại lệ. BHK chỉ rõ một giả định truyền thống của lĩnh vực thuật toán: dữ liệu đầu vào được đặt trong bộ nhớ truy cập ngẫu nhiên mà thuật toán có thể đọc đi đọc lại. Với dữ liệu khổng lồ, giả định này không khả thi, và các mô hình như mô hình dòng (streaming model) đã được xây dựng để phản ánh điều đó; trong mô hình này, lấy mẫu phải thực hiện ngay trong lúc dữ liệu trôi qua (BHK, PDF trang 10).

Cùng lúc, dữ liệu hiện đại trong xử lý thông tin, tìm kiếm và học máy thường được biểu diễn thuận lợi dưới dạng véc-tơ với số thành phần rất lớn; trực giác từ không gian hai hoặc ba chiều có thể sai lệch đáng kể khi số chiều cao (BHK, PDF trang 9). Hai dữ kiện này — dữ liệu vượt bộ nhớ và dữ liệu cao chiều — định hình hai nửa của ghi chú: nửa đầu xử lý giới hạn bộ nhớ bằng thuật toán một lượt quét, nửa sau định tuyến trực giác về không gian cao chiều.

Về dạng dữ liệu, Stanford CS246 liệt kê bốn dạng chính: dữ liệu cao chiều, dữ liệu đồ thị, dữ liệu vô hạn (dòng), và dữ liệu có nhãn; kèm theo các mô hình tính toán khác nhau như MapReduce, dòng và thuật toán trực tuyến, hoặc một máy đơn có bộ nhớ trong (Stanford CS246 `01-intro.pdf`, trang chiếu 7 và 8). Kho nhật ký của ta thuộc dạng bản ghi nhiều trường, nhưng cách tiếp cận dưới đây không phụ thuộc vào dạng cụ thể.

Tự kiểm tra: giả định RAM truyền thống của lĩnh vực thuật toán là gì, và mô hình một lượt quét khác giả định đó ra sao khi $D > M$?

## Thuật toán quét–cộng dồn

Khi $D > M$ và dữ liệu chỉ đọc được một lượt, bộ nhớ không thể giữ toàn bộ dãy bản ghi mà chỉ đủ giữ bảng tổng theo máy chủ. Thuật toán vì thế phải cập nhật trạng thái ngay khi mỗi bản ghi đi qua. Nguồn Stanford mô tả thao tác "với mỗi máy chủ, tìm tổng số byte" nhưng không đặt tên thuật toán; học phần dùng tên nội bộ "quét–cộng dồn" cho cách làm một lượt quét với bảng tổng này (Stanford CS246 `01-intro.pdf`, trang chiếu 62).

### Đặc tả

- Đầu vào: dãy bản ghi $L = ((u_i, s_i))_{i=1}^{n}$, trong đó $u_i$ là tên máy chủ và $s_i \in \mathbb{N}_0$ là kích thước tính bằng byte.
- Đầu ra: với mỗi máy chủ $u$ xuất hiện trong $L$, một cặp $(u, S[u])$ với $S[u] = \sum_{i:\, u_i = u} s_i$.
- Điều kiện trước: mỗi bản ghi có máy chủ xác định và kích thước là số tự nhiên không âm; kiểu dữ liệu của tổng không bị tràn số.
- Điều kiện sau: bảng kết quả có đúng tập khóa bằng tập máy chủ đã xuất hiện, và giá trị tại mỗi khóa bằng tổng chính xác kích thước của máy chủ đó trên toàn dãy.
- Ràng buộc truy cập: dữ liệu được cấp tuần tự theo thứ tự ghi trong tệp; thuật toán được phép đọc mỗi bản ghi đúng một lần, tức một lượt quét.

Ràng buộc truy cập là phần của đặc tả, không phải chi tiết cài đặt. Nó phản ánh thực tế rằng với $D > M$, ta không thể giữ toàn bộ dữ liệu để truy cập ngẫu nhiên (BHK, PDF trang 9–12; MMDS 3e, trang 13).

### Ví dụ chạy tay

Bốn bản ghi sau là ví dụ tự dựng từ lược đồ của Stanford trang chiếu 62 để chạy tay; đây không phải dữ liệu thực nghiệm:

$$(a.\text{vn}, 40),\quad (b.\text{vn}, 25),\quad (a.\text{vn}, 15),\quad (c.\text{vn}, 0)$$

Vết chạy theo từng bước, bảng trạng thái là bảng ánh xạ từ máy chủ sang tổng đang chạy:

| Bước | Bản ghi | Bảng sau bước | Ghi chú |
|---|---|---|---|
| 1 | $(a.\text{vn}, 40)$ | $\{a.\text{vn}: 40\}$ | khóa mới, khởi tạo tổng |
| 2 | $(b.\text{vn}, 25)$ | $\{a.\text{vn}: 40,\ b.\text{vn}: 25\}$ | khóa mới |
| 3 | $(a.\text{vn}, 15)$ | $\{a.\text{vn}: 55,\ b.\text{vn}: 25\}$ | khóa cũ, cộng dồn $40 + 15$ |
| 4 | $(c.\text{vn}, 0)$ | $\{a.\text{vn}: 55,\ b.\text{vn}: 25,\ c.\text{vn}: 0\}$ | kích thước 0 hợp lệ, khóa mới |

Kết quả cuối: $S[a.\text{vn}] = 55$, $S[b.\text{vn}] = 25$, $S[c.\text{vn}] = 0$. Vết cho thấy hai hành vi cần đặc tả rõ: khóa mới được khởi tạo, khóa cũ được cộng dồn; và kích thước $0$ vẫn tạo ra khóa với giá trị $0$.

### Giả mã

```text
S ← bảng rỗng
for i = 1 to n:
    (u, s) ← bản ghi thứ i
    if u không có trong S:
        S[u] ← 0
    S[u] ← S[u] + s
return S
```

Mỗi vòng lặp xử lý đúng một bản ghi, chỉ dùng phép tra và phép gán trên bảng $S$. Thuật toán dừng sau đúng $n$ vòng vì dãy có độ dài hữu hạn $n$ và vòng lặp duyệt từ $1$ đến $n$.

### Bất biến tiền tố

Bất biến sau đây là lập luận được xây dựng từ đặc tả ở trên; nguồn Stanford không phát biểu nó dưới dạng định lý. Với mỗi $k \in \{0, 1, \dots, n\}$, sau khi xử lý $k$ bản ghi đầu:

1. Tập khóa của $S$ đúng bằng tập các máy chủ xuất hiện trong tiền tố $L_1, \dots, L_k$.
2. Với mỗi khóa $u$, giá trị $S[u]$ bằng $\sum_{i \le k,\, u_i = u} s_i$.

### Chứng minh tính đúng

Khởi tạo: với $k = 0$, bảng rỗng có tập khóa rỗng, trùng với tập máy chủ trong tiền tố rỗng; điều kiện 2 rỗng nên đúng.

Duy trì: giả sử bất biến đúng sau $k$ bản ghi. Bước $k+1$ xử lý bản ghi $(u_{k+1}, s_{k+1})$. Nếu $u_{k+1}$ chưa có trong $S$, giả mã tạo khóa với giá trị $0$ rồi cộng $s_{k+1}$, nên giá trị mới là $s_{k+1}$, đúng bằng tổng trên tiền tố dài hơn một bản ghi. Nếu $u_{k+1}$ đã có, giá trị cũ bằng tổng trên $k$ bản ghi đầu theo giả thiết quy nạp, và phép gán cộng thêm $s_{k+1}$, cho đúng tổng trên $k+1$ bản ghi. Tập khóa chỉ thay đổi bằng cách thêm đúng $u_{k+1}$ khi nó mới xuất hiện, nên điều kiện 1 vẫn đúng.

Kết thúc: với $k = n$, điều kiện 1 của bất biến cho tập khóa đúng bằng tập máy chủ trong toàn dãy, và điều kiện 2 cho giá trị $S[u] = \sum_{i:\, u_i = u} s_i$ trên toàn dãy. Đây chính là điều kiện sau của đặc tả, nên thuật toán đúng.

### Trường hợp biên và chi phí

- Dãy rỗng ($n = 0$): vòng lặp không chạy, trả bảng rỗng; điều kiện sau thỏa vì không có máy chủ nào xuất hiện.
- Kích thước $s_i = 0$ hợp lệ: bản ghi vẫn tạo khóa với giá trị $0$, như bước 4 của vết chạy.
- Máy chủ lặp lại nhiều lần: được cộng dồn đúng, như $a.\text{vn}$ ở bước 3.
- Thời gian: $O(n)$ thao tác cập nhật; nếu mỗi thao tác bảng băm có thời gian kỳ vọng $O(1)$ thì tổng là $O(n)$ kỳ vọng. Đây không phải cận trường hợp xấu: bảng băm chỉ cho bảo đảm kỳ vọng trong giả thiết đang dùng.
- Bộ nhớ: $O(h)$ với $h$ là số máy chủ phân biệt. Thuật toán chỉ khả thi trong mô hình đang xét nếu bảng $h$ khóa vừa bộ nhớ; nếu không, thuật toán đúng về mặt toán học nhưng không đáp ứng mô hình triển khai.
- Truy cập dữ liệu: đúng một lượt quét. Với băng thông đọc $b$, cận dưới thời gian truyền dữ liệu là $T_{\text{quét}} \ge D/b$ (MMDS 3e, trang 13: đĩa không truyền dữ liệu vào bộ nhớ nhanh hơn khoảng $10^8$ byte mỗi giây bất kể cách tổ chức).
- Sai số: bằng $0$ theo đặc tả, vì đầu ra là tổng chính xác.

Tự kiểm tra: sau khi xử lý ba bản ghi đầu trong ví dụ, tập khóa và giá trị nào phải có trong $S$ theo bất biến? Nếu $h$ lớn đến mức bảng tổng không vừa bộ nhớ, tính đúng và tính khả thi của thuật toán thay đổi ra sao?

## Năm tầng của một lời giải

Thuật toán trên đúng và khả thi khi bảng $O(h)$ vừa bộ nhớ. Một lời giải dữ liệu lớn còn phụ thuộc vào biểu diễn, hạ tầng thực thi và bảo đảm của kết quả. Từ cách MMDS kết hợp phần cứng, hệ thống lập trình và thuật toán trong khai phá dữ liệu (MMDS 3e, trang 1), có thể tách lời giải thành năm tầng:

| Tầng | Câu hỏi trả lời | Ví dụ ở kho nhật ký |
|---|---|---|
| Bài toán | Cần tính gì? | Tổng byte theo máy chủ |
| Biểu diễn | Dữ liệu lưu dưới dạng nào? | Các dòng $(u_i, s_i)$ trong tệp metadata |
| Thuật toán | Tính bằng bước nào? | Quét–cộng dồn với bảng tổng |
| Cài đặt | Chạy trên hạ tầng nào, với giả thiết gì? | Một máy, bảng băm trong bộ nhớ, dữ liệu trên đĩa |
| Kết quả | Bảo đảm gì kèm theo? | Tổng chính xác, một lượt quét, $O(h)$ bộ nhớ |

![Ba miền giải thuật, học máy và hệ thống cùng giao nhau tại khai phá dữ liệu lớn](img/lec-01/giao-thoa-khai-pha-du-lieu.svg)

Năm tầng trên tách rõ phần việc của giải thuật, học máy và hệ thống xử lý dữ liệu trong một lời giải cụ thể.

Mỗi tầng trả lời một câu khác nhau, và nhầm tầng là lỗi thường gặp: một thuật toán đúng (tầng thuật toán) có thể vô dụng nếu cài đặt không giữ được bảng trong bộ nhớ (tầng cài đặt), hoặc nếu biểu diễn dữ liệu không cho phép truy cập tuần tự (tầng biểu diễn). Đặc tả ở phần trước thuộc tầng bài toán và biểu diễn; chứng minh bất biến thuộc tầng thuật toán; giả thiết bảng băm và giới hạn bộ nhớ thuộc tầng cài đặt; ba chi phí và bảo đảm sai số thuộc tầng kết quả.

Tự kiểm tra: một thuật toán đúng nhưng cài đặt không giữ được bảng tổng trong bộ nhớ thì lỗi nằm ở tầng nào, và năm tầng của một lời giải gồm những gì?

## Hai loại mô hình: thống kê và theo truy vấn

Khi bài toán không phải tính tổng mà là học từ dữ liệu, sản phẩm thường là một mô hình. MMDS phân biệt hai cách nhìn. Theo cách nhìn thống kê, khai phá dữ liệu là xây dựng một mô hình thống kê, tức một phân phối nền mà từ đó dữ liệu quan sát được sinh ra (MMDS 3e, trang 2). Theo cách nhìn tính toán, mô hình dữ liệu chỉ là câu trả lời cho một truy vấn phức tạp về dữ liệu (MMDS 3e, trang 3).

MMDS liệt kê hai dạng mô hình theo truy vấn (MMDS 3e, trang 3–4):

1. Tóm tắt dữ liệu một cách súc tích và xấp xỉ, ví dụ PageRank tóm tắt cấu trúc Web bằng một số cho mỗi trang, hoặc phân cụm tóm tắt dữ liệu bằng tâm cụm.
2. Trích các đặc trưng nổi bật nhất và bỏ phần còn lại, ví dụ tập mục thường xuất hiện cùng nhau trong giỏ hàng, hoặc các cặp tập hợp tương tự nhau.

Hai loại sản phẩm này khác nhau về vai trò: mô hình thống kê khẳng định một phân phối sinh dữ liệu và các tham số của nó; mô hình dữ liệu theo truy vấn là bản tóm tắt phục vụ một lớp truy vấn, không phải một mô hình tính toán. Ví dụ lọc thư của MMDS minh họa khâu học và khâu chạy tách rời: mô hình là bộ trọng số trên các từ, dương cho từ hay xuất hiện trong thư lừa đảo và âm cho từ không xuất hiện; thuật toán chạy mô hình rất đơn giản — cộng trọng số các từ trong thư và kết luận lừa đảo khi tổng dương (MMDS 3e, Ví dụ 1.1, trang 2). Khó nằm ở khâu học trọng số, không ở khâu áp dụng.

Kiểm tra nhanh cách phân loại: một phân cụm khách hàng theo khoảng cách là mô hình tóm tắt; một phân phối Gaussian ước lượng từ dữ liệu số là mô hình thống kê (MMDS 3e, Ví dụ 1.2, trang 2); một bộ trọng số từ vựng cho lọc thư là mô hình thống kê học từ mẫu, dùng bởi một thuật toán áp dụng đơn giản.

## Ba chi phí và một bảo đảm

Quay lại kho nhật ký: tính đúng ở tầng thuật toán chưa đủ. Một lời giải dữ liệu lớn cần khai triển ba loại chi phí và một bảo đảm (MMDS 3e, trang 13; tổng hợp từ phân tích chi phí của thuật toán quét–cộng dồn):

| Thành phần | Đo bằng gì | Giá trị ở quét–cộng dồn |
|---|---|---|
| Chi phí tính toán | Số thao tác xử lý trên dữ liệu đã ở bộ nhớ | $O(n)$ kỳ vọng dưới giả thiết bảng băm |
| Chi phí bộ nhớ | Dung lượng cần giữ trong lúc chạy | $O(h)$, phải vừa $M$ |
| Chi phí truy cập dữ liệu | Số lượt quét và thời gian truyền | Một lượt, $T_{\text{quét}} \ge D/b$ |
| Bảo đảm | Độ chính xác của kết quả | Sai số bằng 0 theo đặc tả |

Chi phí truy cập dữ liệu thường bị đánh giá thấp. MMDS chỉ ra rằng đọc một khối đĩa tốn khoảng mười mili-giây, chậm hơn ít nhất $10^5$ lần so với đọc một từ trong bộ nhớ chính, nên nếu chỉ cần vài byte, dữ liệu ở bộ nhớ chính có lợi thế áp đảo (MMDS 3e, trang 13). BHK nhấn mạnh cùng điểm từ phía mô hình: giả định đầu vào nằm trong bộ nhớ truy cập ngẫu nhiên không khả thi với dữ liệu khổng lồ (BHK, PDF trang 9–12).

Kết quả cũng có hai loại đặc tả: chính xác hoặc xấp xỉ (MMDS 3e, trang 3–4). Quét–cộng dồn trả kết quả chính xác với sai số bằng 0. Khi $O(h)$ không vừa bộ nhớ, phép đánh đổi phải nằm trong đặc tả: giữ kết quả chính xác nhưng chấp nhận nhiều lượt quét, hoặc giảm bộ nhớ bằng cách chấp nhận sai số xấp xỉ. Câu hỏi đặt ra cho đặc tả là: bảo đảm sai số nào được chấp nhận, và chi phí nào là điểm nghẽn.

Tự kiểm tra: nếu bảng tổng không vừa bộ nhớ nhưng đầu ra vẫn phải chính xác, thành phần nào trong ba chi phí có thể phải tăng? Nếu chấp nhận đầu ra xấp xỉ, bảo đảm nào phải được ghi thêm vào đặc tả?

## Tín hiệu giả và kỳ vọng số biến cố trùng

Giới hạn của một lời giải không chỉ nằm ở chi phí tính toán. Khi khai phá tìm nhiều loại biến cố trong dữ liệu khổng lồ, một giới hạn thống kê xuất hiện: ngay trong dữ liệu hoàn toàn ngẫu nhiên, vẫn có thể kỳ vọng thấy một số biến cố trông có ý nghĩa, và số biến cố này tăng theo kích thước dữ liệu (MMDS 3e, trang 6).

### Mô hình ngẫu nhiên cho hồ sơ lưu trú

MMDS đưa ví dụ sau (MMDS 3e, mục 1.2.3, trang 7). Giả sử cần tìm các "kẻ xấu" tụ họp tại khách sạn, và dữ liệu là hồ sơ lưu trú với các giả thiết:

1. Có $P = 10^9$ người có thể là đối tượng.
2. Mỗi người đi khách sạn một ngày trong mỗi $100$ ngày, tức xác suất $q = 0{,}01$ mỗi ngày.
3. Một khách sạn chứa $100$ người, nên có $H = 10^5$ khách sạn.
4. Xem xét hồ sơ trong $T = 1000$ ngày.

Mô hình ngẫu nhiên: nếu thực sự không có kẻ xấu, mỗi người mỗi ngày quyết định đi khách sạn với xác suất $q$ độc lập với người và ngày khác, và nếu đi thì chọn đều một trong $H$ khách sạn, độc lập giữa các ngày. Một biến cố "trùng" là một cặp người và một cặp ngày khác nhau sao cho hai người cùng ở một khách sạn trong từng ngày của cặp; khách sạn hai ngày có thể khác nhau.

### Phép đếm và kỳ vọng

Số phép thử là số cặp người nhân số cặp ngày. Với $n$ lớn, $\binom{n}{2} \approx n^2/2$, nên:

$$\binom{P}{2} \approx \frac{10^{18}}{2} = 5 \times 10^{17}, \qquad \binom{T}{2} \approx \frac{10^6}{2} = 5 \times 10^{5}.$$

Xác suất một phép thử thành công: hai người cùng đi khách sạn trong một ngày có xác suất $q^2 = 10^{-4}$, và với điều kiện cả hai người đã đi, xác suất họ chọn cùng khách sạn là $1/H = 10^{-5}$, nên xác suất cùng khách sạn trong một ngày là $q^2/H = 10^{-9}$. Với hai ngày khác nhau, do độc lập giữa các ngày:

$$\left(\frac{q^2}{H}\right)^2 = (10^{-9})^2 = 10^{-18}.$$

Gọi $X$ là số biến cố trùng. Theo tính tuyến tính của kỳ vọng, kỳ vọng của tổng bằng tổng các kỳ vọng, nên không cần giả thiết thêm về phụ thuộc giữa các cặp:

$$\mathbb{E}[X] = \binom{P}{2}\binom{T}{2}\left(\frac{q^2}{H}\right)^2 = 5 \times 10^{17} \times 5 \times 10^{5} \times 10^{-18} = 250\,000.$$

Giá trị $250\,000$ là kỳ vọng số biến cố `(cặp người, cặp ngày)` trùng. Số cặp người phân biệt xuất hiện trong ít nhất một biến cố chỉ xấp xỉ giá trị này, vì một cặp người hiếm khi trùng ở nhiều cặp ngày. Dùng tổ hợp chính xác, $\binom{P}{2}\binom{T}{2} = 499\,999\,999\,500\,000\,000 \times 499\,500$, cho kỳ vọng xấp xỉ $249\,750$; giá trị $250\,000$ là xấp xỉ theo $n^2/2$.

![Số phép thử tăng theo cặp người và cặp ngày, trong khi xác suất một phép thử thành công giảm; tích cho kỳ vọng số biến cố trùng](img/lec-01/phep-thu-va-duong-tinh-gia.svg)

Kết quả: khoảng một phần tư triệu cặp người trông như kẻ xấu dù không phải (MMDS 3e, trang 8). Nếu thực sự có $10$ cặp kẻ xấu, cảnh sát phải điều tra khoảng $250\,000$ cặp vô tội để tìm ra chúng; chi phí điều tra và sự xâm phạm lên nửa triệu người vô tội khiến cách tiếp cận này không khả thi (MMDS 3e, trang 8).

### Nguyên lý Bonferroni phi hình thức

MMDS trình bày kết luận này như một nguyên lý phi hình thức, không phải một định lý thống kê đầy đủ: hãy tính số biến cố kỳ vọng của loại mình tìm dưới giả thiết dữ liệu ngẫu nhiên; nếu số này lớn hơn đáng kể số biến cố thật mong đợi, gần như mọi thứ tìm được sẽ là hiện tượng giả, tức sản phẩm thống kê chứ không phải bằng chứng (MMDS 3e, mục 1.2.2, trang 6–7). Thống kê học có hiệu chỉnh Bonferroni để kiểm soát dương tính giả, nhưng chi tiết của hiệu chỉnh nằm ngoài phạm vi bài này (MMDS 3e, trang 6). Hệ quả thực hành là chỉ tìm các biến cố đủ hiếm trong dữ liệu ngẫu nhiên (MMDS 3e, trang 7).

Ba chi phí ở trên là giới hạn tính toán; nguyên lý Bonferroni là giới hạn thống kê. Một thuật toán có thể chạy nhanh, tốn ít bộ nhớ, và vẫn cho kết quả vô nghĩa nếu số phép thử quá lớn so với độ hiếm của biến cố cần tìm.

Tự kiểm tra: trong mô hình lưu trú, yếu tố nào đếm số phép thử và yếu tố nào cho xác suất thành công của một phép thử? Vì sao tính tuyến tính của kỳ vọng không đòi hỏi các biến cố trùng giữa những cặp người phải độc lập?

## Bài tập: thay đổi quy mô và mô hình giỏ hàng

Hai bài tập sau áp dụng nguyên lý Bonferroni vào thay đổi quy mô quan sát và trùng giỏ hàng (MMDS Bài 1.2.1 và 1.2.2, trang 8).

### Bài 1.2.1: ba thay đổi của hồ sơ lưu trú

:::exercise
Dùng thông tin từ mục 1.2.3, số cặp nghi vấn thay đổi thế nào nếu thực hiện từng thay đổi sau (các số khác giữ nguyên)? (MMDS 3e, Bài 1.2.1, trang 8)

(a) Số ngày quan sát tăng lên $2000$.

(b) Số người được quan sát tăng lên $2$ tỷ (do đó có $200\,000$ khách sạn).

(c) Chỉ báo cáo một cặp là nghi vấn nếu họ cùng ở một khách sạn vào cùng thời điểm trong ba ngày khác nhau.
:::

:::hint
Dùng công thức $\mathbb{E}[X] = \binom{P}{2}\binom{T}{2}\left(\frac{q^2}{H}\right)^k$ với $k$ là số ngày yêu cầu, và xấp xỉ $\binom{n}{2} \approx n^2/2$. Với phần (b), lưu ý $H$ tăng theo tỷ lệ với số người vì tổng số chỗ khách sạn phải chứa $1\%$ số người mỗi ngày.
:::

:::solution
Cơ sở: $\binom{P}{2} \approx 5 \times 10^{17}$, $\binom{T}{2} \approx 5 \times 10^{5}$, $q^2/H = 10^{-9}$, kỳ vọng gốc $250\,000$.

(a) $T = 2000$ nên $\binom{T}{2} \approx \frac{(2000)^2}{2} = 2 \times 10^{6}$, gấp $4$ lần giá trị cũ. Kỳ vọng mới:

$$\mathbb{E}[X] = 5 \times 10^{17} \times 2 \times 10^{6} \times 10^{-18} = 1\,000\,000.$$

(b) $P = 2 \times 10^9$ nên $\binom{P}{2} \approx 2 \times 10^{18}$, gấp $4$ lần; $H = 2 \times 10^5$ nên $q^2/H = 10^{-4}/(2 \times 10^5) = 5 \times 10^{-10}$, giảm $2$ lần; bình phương cho $(5 \times 10^{-10})^2 = 2{,}5 \times 10^{-19}$, giảm $4$ lần. Hai hệ số gấp $4$ và giảm $4$ triệt tiêu:

$$\mathbb{E}[X] = 2 \times 10^{18} \times 5 \times 10^{5} \times 2{,}5 \times 10^{-19} = 250\,000.$$

Kỳ vọng không đổi: tăng số người làm tăng số cặp phép thử đúng bốn lần, nhưng đồng thời tăng số khách sạn làm giảm xác suất trùng mỗi ngày đúng bốn lần.

(c) Với ba ngày, xác suất một cặp người và một bộ ba ngày là biến cố trùng là $(10^{-9})^3 = 10^{-27}$; số bộ ba ngày là $\binom{1000}{3} \approx \frac{10^9}{6}$. Kỳ vọng:

$$\mathbb{E}[X] = 5 \times 10^{17} \times \frac{10^9}{6} \times 10^{-27} = \frac{5}{6} \times 10^{-1} \approx 0{,}083.$$

Diễn giải: yêu cầu trùng trong ba ngày làm kỳ vọng rơi từ $250\,000$ xuống dưới $1$. Đây chính là cách làm biến cố tìm kiếm đủ hiếm để tín hiệu giả biến mất, đúng tinh thần nguyên lý Bonferroni.
:::

### Bài 1.2.2: trùng giỏ hàng

:::exercise
Giả sử có thông tin về mua sắm tại siêu thị của $100$ triệu người. Mỗi người đi siêu thị $100$ lần trong một năm và mua $10$ trong $1000$ mặt hàng mà siêu thị bán. Giả thuyết là một cặp khủng bố sẽ mua đúng cùng một tập $10$ mặt hàng (chú thích 3 của nguồn: giả thuyết này được chấp nhận như một giả thiết làm việc, không bàn liệu khủng bố có nhất thiết mua như vậy hay không). Nếu tìm các cặp người đã mua cùng một tập mặt hàng, có thể kỳ vọng những người tìm được thực sự là khủng bố không? (MMDS 3e, Bài 1.2.2 và chú thích 3, trang 8)
:::

:::hint
Đặt $X$ là số cặp lượt mua của hai người khác nhau có cùng tập $10$ mặt hàng. Đếm số phép thử là số cặp người nhân số cặp lượt mua trong năm, rồi ước lượng xác suất hai lượt mua độc lập có cùng tập $10$ mặt hàng.
:::

:::solution
Mô hình: mỗi người có $100$ lượt mua mỗi năm, mỗi lượt mua chọn một tập $10$ mặt hàng; giả thiết làm việc là các lượt mua độc lập và mỗi tập $10$ mặt hàng trong $\binom{1000}{10}$ tập khả dĩ được chọn như nhau. Đây là giả thiết mô hình hóa, không phải dữ kiện thực nghiệm.

Số phép thử: số cặp người là $\binom{10^8}{2} \approx 5 \times 10^{15}$; mỗi người có $100$ lượt mua nên số cặp lượt mua giữa hai người là $100 \times 100 = 10^4$. Tổng phép thử:

$$5 \times 10^{15} \times 10^4 = 5 \times 10^{19}.$$

Xác suất một phép thử thành công: hai lượt mua độc lập có cùng tập $10$ mặt hàng với xác suất $1/\binom{1000}{10}$. Ước lượng $\binom{1000}{10} \le 1000^{10} = 10^{30}$, nên xác suất mỗi phép thử ít nhất là $10^{-30}$ theo cận này.

Kỳ vọng:

$$\mathbb{E}[X] = 5 \times 10^{15} \times 10^4 \times \frac{1}{\binom{1000}{10}} \ge \frac{5 \times 10^{19}}{10^{30}} = 5 \times 10^{-11}$$

theo cận trên của mẫu số; dùng $\binom{1000}{10} \approx 2{,}6 \times 10^{23}$ cho giá trị thực, kỳ vọng khoảng $5 \times 10^{19} / 2{,}6 \times 10^{23} \approx 1{,}9 \times 10^{-4}$.

Kiểm tra giả thiết và giới hạn: theo bất đẳng thức Markov, với biến ngẫu nhiên không âm $X$, $\Pr(X \ge 1) \le \mathbb{E}[X]$, nên từ kỳ vọng khoảng $1{,}9\times10^{-4}$ suy ra xác suất có ít nhất một trùng ngẫu nhiên không vượt quá $1{,}9\times10^{-4}$ trong mô hình. Do đó tín hiệu giả gần như không xảy ra, và theo nguyên lý Bonferroni, nếu tìm thấy cặp trùng thì đó là tín hiệu mạnh. Kết luận này chỉ đứng vững khi giả thuyết làm việc đúng rằng kẻ khủng bố mua cùng một tập $10$ mặt hàng. Hai giới hạn của mô hình: (i) giả thiết lượt mua độc lập và chọn đều là xấp xỉ mạnh, mua sắm thực có xu hướng theo nhóm mặt hàng; (ii) kết luận phụ thuộc giả thuyết làm việc trong chú thích 3, rằng kẻ khủng bố nhất thiết mua cùng một tập $10$ mặt hàng tại một thời điểm trong năm.
:::

## Trực giác về số chiều lớn

Dữ liệu hiện đại thường được biểu diễn bằng véc-tơ số chiều lớn, nơi trực giác từ không gian hai hoặc ba chiều có thể sai đáng kể (BHK, PDF trang 9–12). Bài 01 chỉ giới thiệu hai hiện tượng để chuẩn bị cho các bài sau; phần này không thuộc mục tiêu đánh giá.

Cho $y,z\in\mathbb{R}^d$, khoảng cách Euclid giữa hai véc-tơ là một tổng của nhiều thành phần:

$$\|\mathbf{y} - \mathbf{z}\|_2^2 = \sum_{j=1}^{d} (y_j - z_j)^2.$$

Khi $d$ lớn và các tọa độ là mẫu độc lập của biến ngẫu nhiên phương sai hữu hạn, luật số lớn cho biết trung bình của các mẫu hội tụ về kỳ vọng, nên khoảng cách giữa các cặp điểm ngẫu nhiên gần như bằng nhau khi $d$ đủ lớn (BHK, PDF trang 12). Đây là hiện tượng về tổng khoảng cách.

Một hiện tượng khác liên quan thể tích. BHK Hình 2.2 minh họa rằng phần lớn thể tích của quả cầu $d$ chiều bán kính $r$ nằm trong một vành mỏng độ rộng $O(r/d)$ gần biên (BHK, PDF trang 17, Hình 2.2). Trực giác: thể tích tăng nhanh theo bán kính, nên lớp ngoài cùng dù mỏng vẫn chiếm gần hết thể tích.

![Quả cầu d chiều có phần lớn thể tích nằm trong vành mỏng gần biên, độ rộng vành tỉ lệ với r/d](img/lec-01/the-tich-gan-bien.svg)

Các chứng minh chi tiết về thể tích và vùng xích đạo nằm ngoài phạm vi Bài 01 và chỉ để đọc thêm (BHK, PDF trang 18–21).

Tự kiểm tra: công thức khoảng cách là tổng theo số chiều, còn hình vành mỏng nói về đại lượng hình học nào? Hai phát biểu này có phải cùng một hiện tượng không?

## Bản đồ học phần và chọn mô hình theo điểm nghẽn

Học phần gồm $15$ bài, gộp thành năm nhóm liền nhau: Bài 2–4, 5–7, 8–9, 10–11 và 12–15; Bài 01 là nền chung (MMDS 3e, trang 17–18; Stanford CS246 `01-intro.pdf`, trang chiếu 10).

![Bản đồ 15 bài của học phần gộp thành năm nhóm theo dòng chủ đề, Bài 01 là nền chung](img/lec-01/ban-do-hoc-phan.svg)

Bản đồ cho thấy các nhóm bài xoay quanh các mô hình dữ liệu khác nhau: dòng dữ liệu, tìm mục tương tự, mô hình giỏ hàng, đồ thị và mạng xã hội, học máy trên dữ liệu lớn (MMDS 3e, mục 1.4, trang 17–18). Bài 01 cung cấp khung chung cho tất cả: đặc tả bài toán, biểu diễn dữ liệu, thuật toán, cài đặt và kết quả.

Khi đối mặt một bài toán dữ liệu lớn, bốn phép kiểm tra giúp chọn mô hình theo điểm nghẽn:

1. Dữ liệu có vừa bộ nhớ không? Nếu không, mô hình truy cập tuần tự hoặc dòng là bắt buộc (MMDS 3e, trang 13; BHK, PDF trang 9–12).
2. Điểm nghẽn là tính toán, bộ nhớ hay truy cập dữ liệu? Xác định chi phí trội để chọn hướng tối ưu.
3. Kết quả cần chính xác hay xấp xỉ, và bảo đảm sai số nào nằm trong đặc tả? (MMDS 3e, trang 3–4)
4. Số phép thử có đủ lớn để tín hiệu giả lấn át tín hiệu thật không? Tính kỳ vọng số biến cố trùng dưới mô hình ngẫu nhiên trước khi tin kết quả (MMDS 3e, trang 6–8).
