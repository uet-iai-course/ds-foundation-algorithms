# Bài 13 — Chỉ mục truyền thống và băm tĩnh

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đã biết mô hình I/O theo khối của Bài 12, cây tìm kiếm cân bằng, hàm băm và phép toán bit.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Trọng tâm: B+-Tree; B-Tree chỉ dùng để đối chiếu ngắn.
- Đầu ra: tìm điểm và khoảng; chèn, tách, xóa, mượn và gộp trên B+-Tree; phân tích chiều sâu và I/O; chạy băm tĩnh; kết hợp Bitmap Index đúng với vị trí đã xóa và NULL.
- Tình huống xuyên suốt: một quan hệ lớn không vừa bộ nhớ cần phục vụ truy vấn điểm, khoảng và bộ lọc phân tích mà không quét toàn bộ tệp.

## Ánh xạ nguồn

| Cụm | Nguồn | Quyết định |
|---|---|---|
| Khái niệm và đánh giá chỉ mục | *Database System Concepts* 7e, Chương 14, trang chiếu 3–16 | Giữ khóa tìm kiếm, bốn thước đo và định hướng cấu trúc |
| B+-Tree | Chương 14, trang chiếu 17–45 | Làm trục; giữ bất biến, tìm, khoảng, chèn, xóa và chi phí |
| B-Tree | Chương 14, trang chiếu 46–48 | Đối chiếu hai trang; không dạy thuật toán cập nhật riêng |
| Băm tĩnh | Chương 14, trang chiếu 51–59 | Giữ ngăn băm, chuỗi tràn, giới hạn M cố định và đối chiếu truy vấn khoảng |
| Bitmap | Chương 14, trang chiếu 71–75; Chương 24, trang chiếu 11–15 | Dùng Chương 24 để bổ sung mặt nạ tồn tại và NULL cho NOT |
| Bài tập | Bài 14.1, 14.3(b), 14.4 trên cây 14.3(b), 14.13 | Đề PDF 1/tr.43 và PDF 3/tr.45; lời giải PDF 1/tr.99, PDF 2/tr.100, PDF 4/tr.102, PDF 10–11/tr.108–109; không làm 14.3(a,c) |

MMDS và Stanford CS246 không được dùng vì Bài 13 neo theo giáo trình cơ sở dữ liệu và hai nguồn này không bao phủ cấu trúc chỉ mục trên đĩa trong phạm vi yêu cầu.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $m$ | hệ số phân nhánh tối đa của nút B+-Tree; nút trong có tối đa $m$ con, lá có tối đa $m-1$ khóa |
| $K$ | số mục khóa trong lá: số khóa phân biệt với RID-list; số cặp với khóa ghép $(v,\mathrm{RID})$ |
| $d$ | số cạnh từ gốc đến lá; cây chỉ có gốc có $d=0$ |
| $f$ | $\lceil m/2\rceil$, cận dưới số con của nút trong không phải gốc; ngoại lệ ở gốc chỉ đổi hằng số trong cận $d=O(\log_f K)$ |
| $L,J,D$ | số khối lá đọc thêm, số khối danh sách RID ngoài lá và số khối dữ liệu chứa kết quả |
| $N$ | số khối của tệp dữ liệu; quét toàn tệp đọc $N$ khối |
| $M,c,N_e,t$ | số ngăn băm, sức chứa mỗi ngăn, số mục và số ngăn tràn phải đọc |
| $R$ | số vị trí bản ghi trong bitmap |
| $w$ | số bit xử lý trong một từ máy |
| $q$ | số giá trị hoặc dải không NULL được mã hóa thành bitmap |
| $E$ | bitmap tồn tại |
| $V_v$ | bitmap cho giá trị $v$ |
| $V_{\mathrm{NULL}}$ | bitmap vị trí có NULL |

Không dùng $B$ làm biến vì Bài 12 đã dùng $B$ cho tổng số khung đệm.

## Vết B+-Tree chính

- Nguồn: bài 14.3(b), $m=6$, chèn tăng dần $2,3,5,7,11,17,19,23,29,31$.
- Cây đầu recitation: gốc $[7,19]$; lá $[2,3,5]$, $[7,11,17]$, $[19,23,29,31]$.
- Chèn 9, 10: lá giữa thành $[7,9,10,11,17]$, chưa tràn.
- Chèn 8: tách $[7,8,9]$ và $[10,11,17]$; sao chép khóa phân cách 10 lên gốc $[7,10,19]$.
- Lá phải sau Insert 8 phải là $[19,23,29,31]$. Lời giải nguồn in nhầm khóa đầu thành 9; deck sửa thành 19 vì thao tác không xóa khóa 19.
- Xóa 23: lá phải $[19,29,31]$, vẫn đủ ba khóa.
- Xóa 19: $[29,31]$ thiếu; gộp với $[10,11,17]$; gốc còn $[7,10]$.

## Vết bitmap chính

- Thứ tự 12 hàng theo quan hệ `instructor` trong lời giải 14.13.
- $S_1=001000000000$; $S_2=000000000000$; $S_3=100010010000$; $S_4=010101101111$.
- `Finance` $=010000001000$.
- `Finance AND S4` $=010000001000$ chỉ tạo ứng viên Wu và Singh.
- $S_4$ biểu diễn lương từ 70.000; phải đọc bản ghi ứng viên và lọc lại điều kiện lương từ 80.000.

## Phân bổ thời lượng

| Phần | Trang | Phút |
|---|---:|---:|
| Mở bài và chọn chỉ mục | P00–A03 | 14 |
| Truy vấn B+-Tree | B00–B08 | 27 |
| Cập nhật và đối chiếu cây | C00–D01, C06A | 42 |
| Băm tĩnh | H00–H06 | 14 |
| Bitmap Index | M00–M07, M00A | 19 |
| Tổng kết | T00–T01 | 4 |
| **Tổng phần giảng** | **49 trang** | **120** |
| Bài 14.1 | X01 | 5 |
| Bài 14.3(b) | X02–X03 | 15 |
| Bài 14.4 trên cây 14.3(b) | X04–X06 | 25 |
| Bài 14.13 | X07D, X07–X08 | 15 |
| **Tổng recitation** | **10 trang kể cả X00** | **60** |

## Trường hợp biên và giả thiết

- B+-Tree rỗng có gốc là lá và không chứa khóa; gốc trong có ít nhất hai con.
- Lá và nút trong không phải gốc dùng cận sức chứa riêng; không áp cận đó cho gốc.
- Tìm khóa bằng khóa phân cách đi sang cây con bên phải theo quy ước khóa phân cách là khóa nhỏ nhất của cây con phải.
- Tách lá sao chép khóa nhỏ nhất của lá phải lên cha; tách nút trong đẩy khóa phân cách giữa lên cha và bỏ nó khỏi hai nút mới.
- Khóa trùng cần khóa ghép với mã bản ghi hoặc một mục khóa trỏ danh sách RID. Với danh sách RID, chèn RID không tăng số khóa; xóa RID chỉ xóa mục khóa khi danh sách rỗng.
- Điểm đọc $d+1+J+D$ khối; khoảng đọc $d+1+L+J+D$ khối. Đặt $J=0$ khi không có danh sách RID ngoài lá. Chỉ mục không phân cụm có thể bị $D$ chi phối.
- Xóa có thể mượn, gộp và lan lên gốc; gốc một con được thay bằng con đó.
- Mô hình chi phí băm giả sử một ngăn bằng một khối và không tính bộ nhớ đệm. Bài giảng suy ra $\alpha=N_e/(Mc)$ từ số mục và tổng sức chứa, rồi suy ra chi phí $1+t+D$ từ một khối ngăn nhà, $t$ khối ngăn tràn và $D$ khối dữ liệu. Ví dụ dẫn xuất ở H02 đặt $c=1$, nên Physics và Elec. Eng. tạo $t=1$. Nguồn mô tả các thành phần nhưng không phát biểu hai công thức này tại các trang được dẫn. Trường hợp xấu vẫn có thể tuyến tính.
- Với $q$ là số giá trị hoặc dải không NULL, các bitmap giá trị chưa nén chiếm $qR$ bit; thêm $R$ bit cho $E$ và $R$ bit cho NULL khi cần, tối đa $(q+2)R$. Một phép Boolean cần $\lceil R/w\rceil$ phép toán từ; I/O còn gồm trang bitmap và $D$ khối dữ liệu ứng viên.
- Cập nhật B+-Tree đọc $O(d+1)$ và ghi tối đa $O(d+1)$ khối.
- Bitmap NOT phải chặn vị trí đã xóa bằng $E$ và vị trí NULL bằng $V_{\mathrm{NULL}}$.
- Bitmap dải chỉ tạo ứng viên cho điều kiện hẹp hơn; mọi điều kiện dư phải được lọc trên bản ghi thật.
