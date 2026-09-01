# Bài 12 — Mô hình I/O và sắp xếp ngoài bộ nhớ

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đã biết sắp xếp trong bộ nhớ, hàng đợi ưu tiên và logarit.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Đầu ra: mô hình hóa theo khối và khung; chạy và chứng minh sắp xếp trộn ngoài; tính $r_0,k,p,C_{\mathrm{mat}},C_{\mathrm{pipe}}$; phân biệt lần truyền khối với lần định vị; chạy chọn thay thế.
- Tình huống xuyên suốt: một bảng sự kiện lớn hơn RAM cần `ORDER BY` theo khóa rồi cấp dòng đã sắp cho toán tử sau.
- Quy ước chính: $B$ là tổng số khung đệm; trộn tổng quát dành một khung đầu ra nên $k=B-1$.

## Ánh xạ nguồn

| Cụm | Nguồn chính | Quyết định |
|---|---|---|
| Khối, truy cập, đệm | *Database System Concepts* 7e, Chương 12, trang chiếu 10–11, 32–33; Chương 13, trang chiếu 2–3, 19–20 | Giữ mô hình; dùng trang 2–3 cho bản ghi cố định/biên khối; lược số liệu phần cứng có thể lỗi thời |
| Sắp xếp ngoài | Chương 15, trang chiếu 17–23 | Giữ hai pha; bổ sung giả mã đầy đủ, bất biến và ba loại chi phí |
| Vật chất hóa, truyền dòng | Chương 15, trang chiếu 51–59 | Đặt trước công thức chi phí để chốt điều kiện sau |
| Chọn thay thế | Wisconsin CS 764, bài 2, trang 16–20 | Dùng vì vết hoạt động/đóng băng rõ; đổi sức chứa heap thành $H$ |
| Vết xuyên suốt | Bài 15.1, trang in 47; lời giải PDF trang 1, trang in 111 | Dùng 12 bản ghi cho tạo dãy, hai lượt trộn và chi phí |
| Bài tập | Bài 15.1; bài 15.9 ở đề PDF 2/tr. 48 và lời giải PDF 5/tr. 115; bài 13.5 ở đề PDF 2/tr. 42 và lời giải PDF 5/tr. 95 | Dịch và chia bước, không đổi dữ kiện |

MMDS và Stanford CS246 không được dùng vì Bài 12 neo theo giáo trình cơ sở dữ liệu và Wisconsin, không thuộc các cụm MMDS trong bản đồ nguồn.

## Thuật ngữ và ký hiệu

| Ký hiệu hoặc thuật ngữ | Nghĩa |
|---|---|
| $n$ | số bản ghi của tệp |
| $N$ | số khối của tệp đầu vào |
| $B$ | tổng số khung đệm trong bộ nhớ chính |
| $k=B-1$ | số dãy đầu vào trộn đồng thời trong mô hình dành riêng một khung đầu ra |
| $r_0=\lceil N/B\rceil$ | số dãy ban đầu khi tạo theo mẻ cố định |
| $p=\lceil\log_k r_0\rceil$ | số lượt trộn, với $N>B$ và $k\ge2$ |
| $H$ | số bản ghi vừa vùng heap của chọn thay thế; chỉ có cùng giá trị số với $B$ trong vết một bản ghi/khối, $H=B=3$ |
| $b_b\in\mathbb{Z}, b_b\ge1$ | số khung dành cho mỗi dãy đầu vào trong biến thể đệm dài; chỉ chọn cấu hình cho $k\ge2$ khi cần tiếp tục giảm số dãy |
| dãy đã sắp (run) | đoạn dữ liệu có khóa không giảm |
| vật chất hóa | ghi toàn bộ kết quả thành tệp |
| truyền dòng | cấp kết quả trực tiếp cho toán tử sau |
| lần truyền khối | một lần đọc hoặc ghi một khối |
| lần định vị (seek) | thao tác đặt đầu đọc trước một đoạn truy cập |

## Vết dữ liệu chính

- Dữ liệu: 12 bản ghi của bài 15.1; một bản ghi mỗi khối.
- Quy ước phần giảng: $N=12$, $B=3$, $k=2$.
- Tạo dãy: $r_0=4$.
- Hai lượt trộn: $4\rightarrow2\rightarrow1$, nên $p=2$.
- Vật chất hóa mọi lượt: $C_{\mathrm{mat}}=72$ lần truyền khối.
- Truyền dòng ở lượt cuối: $C_{\mathrm{pipe}}=60$ lần truyền khối.
- Recitation giữ đáp án sách trộn ba dãy bằng ba khung. Đây là **biến thể nguồn**, không phải `mergeGroup` của S08: ba đầu dãy chiếm ba khung; xuất đầu nhỏ nhất làm rỗng một khung; vì một bản ghi lấp đầy một khối, khung đó chứa ngay khối đầu ra đầy, được ghi rồi nạp đầu tiếp theo của chính dãy. Không khái quát lịch này thành $k=B$.

## Phân bổ thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài | P00–P02 | 6 |
| Mô hình I/O | I00–I09 | 25 |
| Sắp xếp trộn ngoài trước chi phí | S00–S11 | 35 |
| Tiêu thụ đầu ra, chi phí và kiểm tra | Q00–Q02, S12–S17 | 25 |
| Chọn thay thế | R00–R09 | 25 |
| Tổng kết | T00–T01 | 4 |
| **Tổng phần giảng** | **46 trang** | **120** |
| Bài 15.1 | X01–X04 | 35 |
| Bài 15.9 | X05 | 15 |
| Bài 13.5 | X06 | 10 |
| **Tổng recitation** | **7 trang kể cả X00** | **60** |

## Trường hợp biên và giả thiết

- Điều kiện trước: $B\ge1$ để tạo dãy; nếu $N>B$, mô hình một khung đầu ra cần $B\ge3$ để $k=B-1\ge2$.
- $N=0$ cho tệp đầu ra rỗng; nếu $0<N\le B$, chỉ tạo một dãy và $p=0$.
- Dãy ban đầu cuối cùng và nhóm trộn cuối cùng có thể nhỏ hơn giới hạn.
- Công thức lượt trộn giả sử $B\ge3$, do đó $k\ge2$.
- Khóa trùng vẫn cho thứ tự không giảm. Thuật toán không ổn định nếu không thêm vị trí gốc làm khóa phụ.
- $C_{\mathrm{mat}}=2N(1+p)$ giả sử mỗi lượt đọc và ghi toàn bộ $N$ khối, kể cả sao chép nhóm chỉ có một dãy; nếu bỏ sao chép, đây là cận trên.
- Với truyền dòng: $C_{\mathrm{pipe}}=0$ khi $N=0$; $C_{\mathrm{pipe}}=N$ khi $0<N\le B$ và sắp trực tiếp trong bộ nhớ; $C_{\mathrm{pipe}}=N(2p+1)$ khi $p\ge1$. Không tính chi phí của toán tử nhận.
- Hai công thức trên đếm lần truyền khối, không đếm seek, CPU, khối cuối chưa đầy hay chồng lấp I/O–CPU.
- Với $b_b\in\mathbb{Z}$, $b_b\ge1$: một khung đầu ra cho $k=\lfloor(B-1)/b_b\rfloor$; nếu đầu ra cũng dùng $b_b$ khung thì $k=\lfloor B/b_b\rfloor-1$. Hai công thức được suy ra từ phân bổ khung, còn nguồn 15.9 chỉ nêu đánh đổi định tính. Chọn tham số sao cho $k\ge2$ nếu còn hơn một dãy.
- Wisconsin nêu độ dài trung bình khoảng $2H$ nhưng không đặc tả không gian xác suất. Riêng bài giảng chỉ dùng nhận định này như quy tắc kinh nghiệm cho luồng đủ dài có thứ tự đến giống ngẫu nhiên; điều kiện đó không được quy cho Wisconsin và không tạo bảo đảm trường hợp xấu nhất.

## Bản đồ chủ đề của ghi chú tự học

Ghi chú giữ cùng ký hiệu và tuyến lập luận với bộ trang chiếu, nhưng mở rộng đặc tả, vết chạy, chứng minh và các trường hợp biên. Mỗi chủ đề tạo một sản phẩm học tập có thể kiểm tra.

| `note-topic-id` | Nhãn | Chủ đề | Đầu vào | Sản phẩm học tập | Nguồn và quan hệ |
|---|---|---|---|---|---|
| `L12-N01` | cốt lõi | `ORDER BY` khi tệp vượt RAM | Sắp xếp trong bộ nhớ | Nêu đầu vào, đầu ra và giới hạn khung | `source.md`, Ch.15.17; mở N02 |
| `L12-N02` | cầu nối | Bản ghi, khối, khung và hệ số trộn | N01 | Tính $N$ và $k=B-1$ đúng đơn vị | Ch.12.10–11, Ch.13.2–3; trao mô hình cho N03 |
| `L12-N03` | cốt lõi | Bộ quản lý đệm và hai thước đo I/O | N02 | Chạy vết trúng–trượt, tách truyền khối khỏi định vị | Ch.12.32–33, Ch.13.19–20; trao chi phí cho N04 |
| `L12-N04` | cốt lõi | Đặc tả và tạo dãy ban đầu | N02–N03 | Xử lý ba trường hợp biên, tính và tạo $r_0$ dãy | Ch.15.17–19, Bài 15.1; sang N05 |
| `L12-N05` | cốt lõi | Trộn nhiều đường | Các dãy của N04 | Chạy giả mã, phát biểu bất biến và chứng minh đúng | Ch.15.20–21; tạo một lượt cho N06 |
| `L12-N06` | cốt lõi | Số lượt và cây trộn | $r_0,k$ | Tính $p$ với đúng điều kiện áp dụng | Ch.15.21–22; trao $p$ cho N07 |
| `L12-N07` | cốt lõi | Điều kiện đầu ra và chi phí | $N,p$ | Phân biệt vật chất hóa với truyền dòng; tính hai chi phí | Ch.15.22, 51–59; mở hai cách giảm lượt |
| `L12-N08` | cốt lõi | Định vị, CPU, bộ nhớ và đệm dài | N03, N07 | Phân tích đánh đổi $b_b$–$k$–$p$ | Ch.15.22–23, Bài 15.9; một nhánh tối ưu |
| `L12-N09` | cốt lõi | Chọn thay thế: trạng thái và vết chạy | Hàng đợi ưu tiên, dữ liệu Bài 15.1 | Sinh đúng ba dãy hoạt động–đóng băng | Wisconsin 16–20; giảm $r_0$ cho N10 |
| `L12-N10` | cốt lõi | Tính đúng và giới hạn của chọn thay thế | N09 | Chứng minh dãy không giảm, đúng đa tập; giới hạn nhận định $2H$ | Wisconsin 16–20; đóng nhánh tạo dãy dài |
| `L12-N11` | cầu nối | Chuỗi $B\to(r_0,k)\to p\to C$ | N01–N10 | Chọn tham số và điều kiện đầu ra theo chi phí | Tổng hợp; thu hồi tình huống `ORDER BY` |
| `L12-N12` | cốt lõi | Ba bài từ giáo trình | N03–N11 | Trình bày vết, đánh đổi và cấu trúc tra cứu | Bài 15.1, 15.9, 13.5 |

Đồ thị tiên quyết: `N01→N02→N03→N04→N05→N06→N07`; từ N07 tách thành `N08` và `N09→N10`, rồi hội tụ ở `N11→N12`. Không thêm chủ đề ngoài nguồn. Hai công thức đệm dài là hệ quả của phân bổ khung; lịch ba khung ở Bài 15.1 chỉ là biến thể nguồn trong đúng trường hợp một bản ghi mỗi khối.
