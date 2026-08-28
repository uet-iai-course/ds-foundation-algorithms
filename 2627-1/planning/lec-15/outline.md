# Bài 15 — Thuật toán kết nối dữ liệu

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đã học mô hình I/O, sắp xếp ngoài bộ nhớ, B+-Tree và băm tĩnh ở Bài 12–13.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Sản phẩm học tập: chạy Nested-Loop Join, Block Nested-Loop Join, Indexed Nested-Loop Join, Sort-Merge Join, Hash Join trong bộ nhớ và Grace Hash Join; chứng minh không bỏ hoặc lặp sai cặp kết quả; tính riêng số lần truyền khối và seek; chọn thuật toán theo điều kiện nối, bộ nhớ, thứ tự, chỉ mục và độ lệch.
- Tình huống xuyên suốt: kết nối bảng sự kiện `takes` với bảng thực thể `student` theo `ID` khi cả hai nằm trên đĩa. Nguồn cho $n_{student}=5.000$, $b_{student}=100$, $n_{takes}=10.000$, $b_{takes}=400$.
- Ngoài phạm vi: tối ưu hóa thứ tự nhiều phép nối, ước lượng lực lượng kết quả, nối song song, nối không gian, outer join, pipelining và cache-conscious join.

## Nguồn

| Cụm | Nguồn | Phạm vi dùng |
|---|---|---|
| Mô hình chi phí | Ch15 slide 7–9 | Truyền khối, seek, bộ đệm và giả thiết trường hợp xấu |
| Dữ liệu xuyên suốt | Ch15 slide 24 | `student`: 5.000 tuple, 100 khối; `takes`: 10.000 tuple, 400 khối |
| Nested và Block Nested | Ch15 slide 25–28; slide 28 bị ẩn | Giả mã, quan hệ ngoài/trong, chi phí và vùng $M-2$ |
| Indexed Nested | Ch15 slide 29–30; slide 30 bị ẩn | Tra chỉ mục, ví dụ và giới hạn chỉ mục thứ cấp |
| Sort-Merge | Ch15 slide 31–32 | Sắp hai đầu vào, ghép nhóm khóa trùng và chi phí |
| Hash/Grace | Ch15 slide 33–40; slide 35, 40 bị ẩn | Phân hoạch, build–probe, skew, đường lui hữu hạn và chi phí |
| Recitation | Practice Exercises và Solutions Ch15, Bài 15.3–15.5, trang PDF đề 2 và lời giải 112–114 | Giữ nguyên dữ kiện và yêu cầu; dịch, chia bước và thêm sản phẩm nộp |

MMDS và Stanford CS246 không áp dụng cho bài này.

## Ký hiệu và mô hình

| Ký hiệu | Nghĩa |
|---|---|
| $r,s$ | hai quan hệ đầu vào; mặc định $s$ là phía xây khi băm |
| $n_r,n_s$ | số tuple của $r,s$ |
| $b_r,b_s$ | số khối chứa $r,s$ |
| $M\ge3$ | số khối bộ nhớ dành cho phép nối |
| $M-2$ | vùng giữ nhóm ngoài hoặc phân hoạch xây; hai khối còn lại dành cho đầu vào quét và đầu ra |
| $b_b$ | số khối đọc hoặc ghi liên tiếp giữa hai seek |
| $p_h$ | số phân hoạch của Grace Hash Join |
| $t_T,t_S$ | thời gian một lần truyền khối và một seek |

Chi phí được ghi thành cặp `(truyền khối, seek)`; không cộng chi phí ghi kết quả cuối. Các công thức dùng giả thiết không có khối sẵn trong bộ đệm. Deck xét equi-join theo khóa khác `NULL`; ngữ nghĩa ba trị của SQL nằm ngoài phạm vi.

## Đặc tả trọng tâm

### Nested-Loop Join

- Điều kiện nối có thể là theta bất kỳ.
- Với mỗi tuple ngoài, quét toàn bộ quan hệ trong; xuất đúng mọi cặp thỏa điều kiện.
- Chi phí với $r$ ngoài: $b_r+n_r b_s$ lần truyền khối và $b_r+n_r$ seek theo mô hình nguồn.

### Block Nested-Loop Join

- Giữ tối đa $M-2$ khối ngoài, quét toàn bộ quan hệ trong cho mỗi nhóm.
- Chi phí với $r$ ngoài:

$$b_r+\left\lceil\frac{b_r}{M-2}\right\rceil b_s$$

và xấp xỉ $2\left\lceil b_r/(M-2)\right\rceil$ seek.

### Indexed Nested-Loop Join

- Chỉ áp dụng trực tiếp cho equi-join hoặc natural join khi phía trong có chỉ mục trên thuộc tính nối.
- Mỗi tuple ngoài tra chỉ mục và lấy toàn bộ tuple trong có khóa bằng nhau.
- Chỉ mục thứ cấp với nhiều bản sao có thể gây nhiều lần đọc ngẫu nhiên; biến thể nguồn nối với mục lá, sắp con trỏ theo địa chỉ vật lý rồi đọc phía trong theo thứ tự đĩa.

### Sort-Merge Join

- Hai quan hệ phải được sắp theo khóa nối; nếu chưa sắp, cộng chi phí External Merge Sort.
- Khi hai khóa bằng nhau, lấy trọn hai nhóm khóa $G_r,G_s$ và xuất $G_r\times G_s$.
- Bất biến: mọi cặp có khóa nhỏ hơn khóa tại hai con trỏ đã được xuất đúng một lần.
- Nếu một nhóm không vừa bộ nhớ, phải đánh dấu và quét lại nhóm còn lại hoặc dùng tệp tạm; cận quét một lần $b_r+b_s$ chỉ áp dụng khi mỗi nhóm khóa của ít nhất một phía được giữ theo giả thiết nguồn.

### Hash Join trong bộ nhớ

- Quan hệ xây vừa bộ nhớ. Bảng băm lưu danh sách mọi tuple theo khóa, không ghi đè bản sao.
- Băm chỉ chọn ngăn; thuật toán phải so sánh khóa thật để xử lý va chạm.
- Chi phí lý tưởng $b_r+b_s$ lần truyền khối.

### Grace Hash Join

- Dùng cùng hàm $h$ chia hai quan hệ thành các cặp $(r_i,s_i)$; chỉ nối cặp cùng chỉ số.
- Khi xử lý cặp $i$, $s_i$ phải vừa vùng xây $M-2$ khối. $r_i$ không cần vừa bộ nhớ.
- Không đệ quy và bỏ qua khối biên: $3(b_r+b_s)$ lần truyền khối.
- Nếu tính đọc/ghi lại tối đa một khối biên cho mỗi quan hệ và mỗi phân hoạch: $3(b_r+b_s)+4p_h$.
- Skew hoặc nhiều khóa trùng có thể làm $s_i$ tràn; phân hoạch lại bằng hàm khác, và dùng Block Nested-Loop Join cho phân hoạch vẫn tràn.

## Các lỗi nguồn được xử lý

- Slide 33 ghi nhầm các phân hoạch của $s$ thành $r_0,\ldots,r_n$ và trộn quy ước $0..n$ với số phân hoạch. Deck dùng $p_h$ phân hoạch, chỉ số $0..p_h-1$, gồm $r_i$ và $s_i$.
- Slide 37 gọi nhầm phân hoạch của phía dò là $s_i$; deck dùng $r_i$ và chỉ yêu cầu $s_i$ vừa vùng xây.
- Slide 39 đặt $3(b_r+b_s)+4n_h$ làm công thức duy nhất. Deck tách chi phí lý tưởng $3(b_r+b_s)$ khỏi phần tối đa $4p_h$ do các khối biên.
- Slide 40 dùng $M=20$ nhưng chia phía xây 100 khối thành năm phân hoạch 20 khối, không còn chỗ cho vùng làm việc. Deck dùng sáu phân hoạch, kích thước trung bình $100/6<18=M-2$; chi phí lý tưởng vẫn 1.500, hoặc 1.524 nếu tính $4p_h$.
- Slide 41 có câu kết bị cắt và lỗi diễn đạt. Deck chỉ giữ cơ chế hybrid cùng phép tính nguồn $1.300$ lần truyền khối cho $M=25$, không lặp phần câu hỏng.

## Phân bổ thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài | P00–P02 | 5 |
| Mô hình phép nối và chi phí | M00–M03 | 9 |
| Ba biến thể vòng lặp lồng | N00–N11 | 25 |
| Sort-Merge Join | S00–S09 | 24 |
| Hash Join và Grace Hash Join | H00–H15 | 42 |
| So sánh và chọn thuật toán | C00–C04 | 15 |
| **Tổng phần giảng** | **50 trang** | **120** |
| Bài 15.3 | X01–X04 | 35 |
| Bài 15.4 | X05–X07 | 15 |
| Bài 15.5 | X08–X09 | 10 |
| **Tổng recitation** | **10 trang kể cả X00** | **60** |
