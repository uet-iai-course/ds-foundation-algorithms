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
| Khối, truy cập, đệm | *Database System Concepts* 7e, Chương 12, trang chiếu 10–11, 32–33; Chương 13, trang chiếu 19–20 | Giữ mô hình; lược số liệu phần cứng có thể lỗi thời |
| Sắp xếp ngoài | Chương 15, trang chiếu 17–23 | Giữ hai pha; bổ sung giả mã đầy đủ, bất biến và ba loại chi phí |
| Vật chất hóa, truyền dòng | Chương 15, trang chiếu 51–59 | Đặt trước công thức chi phí để chốt điều kiện sau |
| Chọn thay thế | Wisconsin CS 764, bài 2, trang 16–20 | Dùng vì vết hoạt động/đóng băng rõ; đổi sức chứa heap thành $H$ |
| Vết xuyên suốt | Bài 15.1, trang in 47; lời giải PDF trang 1, trang in 111 | Dùng 12 bản ghi cho tạo dãy, hai lượt trộn và chi phí |
| Bài tập | Bài 15.1, 15.9; Chương 13, bài 13.5 | Dịch và chia bước, không đổi dữ kiện |

MMDS và Stanford CS246 không được dùng vì Bài 12 neo theo giáo trình cơ sở dữ liệu và Wisconsin, không thuộc các cụm MMDS trong bản đồ nguồn.

## Thuật ngữ và ký hiệu

| Ký hiệu hoặc thuật ngữ | Nghĩa |
|---|---|
| $n$ | số bản ghi của tệp |
| $N$ | số khối của tệp đầu vào |
| $B$ | tổng số khung đệm trong bộ nhớ chính |
| $k=B-1$ | số dãy đầu vào trộn đồng thời khi dành một khung đầu ra |
| $r_0=\lceil N/B\rceil$ | số dãy ban đầu khi tạo theo mẻ cố định |
| $p=\lceil\log_k r_0\rceil$ | số lượt trộn, với $N>B$ và $k\ge2$ |
| $H$ | sức chứa heap của chọn thay thế, tính theo bản ghi |
| $b_b$ | số khung dành cho mỗi dãy đầu vào trong biến thể đệm dài |
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
- Recitation giữ đáp án sách trộn ba dãy bằng ba khung. Vì mỗi khối chỉ có một bản ghi, khung chứa đầu nhỏ nhất vừa rỗng được dùng ghi ngay một khối đầu ra đầy rồi nạp tiếp chính dãy đó. Đây là lịch I/O đặc biệt, không khái quát thành $k=B$.

## Phân bổ thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài | P00–P02 | 6 |
| Mô hình I/O | I00–I09 | 25 |
| Sắp xếp trộn ngoài trước chi phí | S00–S11 | 35 |
| Cách tiêu thụ đầu ra | Q00–Q02 | 7 |
| Chi phí và kiểm tra | S12–S17 | 18 |
| Chọn thay thế | R00–R09 | 25 |
| Tổng kết | T00–T01 | 4 |
| **Tổng phần giảng** | **46 trang** | **120** |
| Bài 15.1 | X01–X04 | 35 |
| Bài 15.9 | X05 | 15 |
| Bài 13.5 | X06 | 10 |
| **Tổng recitation** | **7 trang kể cả X00** | **60** |

## Trường hợp biên và giả thiết

- $N=0$ cho tệp đầu ra rỗng; nếu $0<N\le B$, chỉ tạo một dãy và $p=0$.
- Dãy ban đầu cuối cùng và nhóm trộn cuối cùng có thể nhỏ hơn giới hạn.
- Công thức lượt trộn giả sử $B\ge3$, do đó $k\ge2$.
- Khóa trùng vẫn cho thứ tự không giảm. Thuật toán không ổn định nếu không thêm vị trí gốc làm khóa phụ.
- $C_{\mathrm{mat}}=2N(1+p)$ giả sử mỗi lượt đọc và ghi toàn bộ $N$ khối, kể cả sao chép nhóm chỉ có một dãy; nếu bỏ sao chép, đây là cận trên.
- $C_{\mathrm{pipe}}=N(2p+1)$ giả sử $p\ge1$, lượt cuối có toán tử nhận trực tiếp và không tính chi phí toán tử đó.
- Hai công thức trên đếm lần truyền khối, không đếm seek, CPU, khối cuối chưa đầy hay chồng lấp I/O–CPU.
- Với $b_b$ khung trên mỗi dãy: một khung đầu ra cho $k=\lfloor(B-1)/b_b\rfloor$; nếu đầu ra cũng dùng $b_b$ khung thì $k=\lfloor B/b_b\rfloor-1$.
- Độ dài kỳ vọng khoảng $2H$ của chọn thay thế cần thứ tự đến độc lập và đủ ngẫu nhiên; đây không phải bảo đảm trường hợp xấu nhất.
