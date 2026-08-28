# Storyboard Bài 12

## Hành trình khái niệm

Quan hệ cần `ORDER BY` (`I00`) → khối và khung (`I01–I05`) → hai thước đo I/O (`I06–I09`) → hai pha sắp xếp (`S00–S01`) → ví dụ nguồn (`S02`) → thuật toán tạo dãy (`S03–S05`) → ví dụ trộn (`S06`) → tính đúng và giả mã đầy đủ (`S07–S09`) → cây lượt và số lượt (`S10–S11`) → điều kiện tiêu thụ đầu ra (`Q00–Q02`) → chi phí I/O, CPU và bộ nhớ (`S12–S17`) → chọn thay thế (`R00–R09`) → tổng kết và bài nguồn (`T00–X06`).

Đầu vào xuyên suốt là bảng $N$ khối cần sắp theo khóa. Vết chính dùng nguyên 12 bản ghi của bài 15.1, một bản ghi mỗi khối, $N=12$, $B=3$, $k=2$, $r_0=4$, $p=2$. Bốn dãy ở `S02` đi vào ví dụ trộn `S06`, cây `S10`, hai công thức `S12–S14` và recitation `X01–X04`. Ký hiệu $H$ chỉ sức chứa heap theo bản ghi trong chọn thay thế; không thay nghĩa của $B$.

## Chu trình của các khái niệm trọng tâm

### Mô hình I/O

- Tình huống/vấn đề: `I00`.
- Trực giác: `I01–I02`.
- Ví dụ và hình thức hóa: `I03–I04`.
- Cơ chế: `I05`.
- Chi phí và giới hạn: `I06–I08`.
- Kiểm tra: `I09`.
- Sản phẩm: phân biệt bản ghi/khối/khung, tính lần truyền khối và hệ số trộn.

### Sắp xếp trộn ngoài

- Tình huống/vấn đề: `I00`, `S00–S01`.
- Trực giác: `S00`.
- Ví dụ chạy tay: `S02`, rồi `S06`.
- Hình thức hóa: `S04–S05`.
- Thuật toán và tính đúng: `S03`, `S07–S09`.
- Ứng dụng và chi phí: `S10–S16`, với `Q00–Q02` đứng trước hai công thức.
- Kiểm tra: `S17`.
- Sản phẩm: dãy ban đầu, lịch trộn, bất biến, số lượt và ba loại chi phí.

### Chọn thay thế

- Tình huống: `R00`.
- Trực giác: `R01`.
- Ví dụ chạy tay: `R02–R05`.
- Hình thức hóa/thuật toán: `R06`.
- Tính đúng: `R07`.
- Chi phí và giới hạn: `R08`.
- Kiểm tra: `R09`.
- Sản phẩm: ba dãy đúng đa tập, chi phí $O(n\log H)$ và điều kiện của kỳ vọng $2H$.

## Bản đồ từng trang

| Trang | Bước học tập | Lý do tồn tại / sản phẩm | Nguồn |
|---|---|---|---|
| P00 | mở bài | Đặt I/O làm trọng tâm | ch12.11; ch15.17 |
| P01 | mục tiêu | Chốt bốn sản phẩm quan sát được | ch15.17–23; Wisconsin 16–20 |
| P02 | mạch bài | Báo bốn nhánh, chưa đưa công thức | tổng hợp nguồn |
| I00 | tình huống/vấn đề | Bảng vượt RAM cần `ORDER BY` và cấp dòng | ch15.17, 51–59 |
| I01 | trực giác | Nối thiết bị–khối–khung | ch12.11; ch13.19 |
| I02 | trực giác | Phân biệt bản ghi và đơn vị truyền | ch12.11 |
| I03 | ví dụ/hình thức | Đổi số bản ghi sang số khối | ch13.19 |
| I04 | hình thức | Định nghĩa $B$ rồi suy ra $k=B-1$ | ch15.19–20 |
| I05 | cơ chế hệ thống | Trúng/trượt, nạn nhân, khối bẩn | ch13.20 |
| I06 | chi phí | Định nghĩa lần truyền khối | ch15.22–23 |
| I07 | giới hạn | Tách truyền khối và lần định vị | ch12.10, 32–33 |
| I08 | ví dụ chạy tay | Theo dõi trúng, ghi bẩn và đọc | ch13.20 |
| I09 | kiểm tra | Tính $2N$ và $k$, đáp án ẩn | ch15.20, 22 |
| S00 | trực giác | Hai pha giải giới hạn bộ nhớ | ch15.17–21 |
| S01 | đặc tả | Miền, điều kiện sau, rỗng, khóa trùng | ch15.17–21 |
| S02 | ví dụ chạy tay | Tạo bốn dãy từ 12 bản ghi nguồn | bài 15.1 tr.47; lời giải PDF 1/tr.111 |
| S03 | thuật toán | Khái quát tạo dãy sau ví dụ | ch15.19 |
| S04 | hình thức | Suy ra $r_0$, nêu $N\le B$ | ch15.19 |
| S05 | cấu trúc dữ liệu | Phân bổ $k$ đầu vào + một đầu ra | ch15.20 |
| S06 | ví dụ chạy tay | Trộn $R_1,R_2$ với $B=3,k=2$ | ch15.20; bài 15.1 |
| S07 | tính đúng | Khởi tạo–duy trì–kết thúc trên toàn phần chưa xuất | ch15.20 |
| S08 | thuật toán | Refill, flush, nhóm cuối nhỏ hơn $k$ | ch15.20–22 |
| S09 | thuật toán/dừng | Lặp lượt, $r\leftarrow\lceil r/k\rceil$, dừng ở một dãy | ch15.19–22 |
| S10 | ví dụ | Cây $4\rightarrow2\rightarrow1$ cùng vết nguồn | ch15.21; bài 15.1 |
| S11 | hình thức | Suy ra $p$ từ tiến triển của số dãy | ch15.21–22 |
| Q00 | trực giác | Phân biệt ghi tệp và truyền dòng | ch15.51–55 |
| Q01 | giới hạn | Tiêu thụ đủ đầu vào trước khi final merge phát dòng | ch15.56–59 |
| Q02 | điều kiện sau | Chốt khi nào được bỏ lần ghi cuối | ch15.51–59 |
| S12 | chi phí | Dẫn xuất $C_{\mathrm{mat}}$ và chính sách singleton | ch15.22, 51–53 |
| S13 | chi phí | Dẫn xuất $C_{\mathrm{pipe}}$ với $p\ge1$ | ch15.51–59 |
| S14 | ứng dụng | Tính 72 và 60 trên $N=12,B=3$ | bài 15.1; ch15.22, 51–59 |
| S15 | chi phí | Tách I/O, CPU $O(n\log k)$ và $O(B)$ khung | ch15.19–23 |
| S16 | đánh đổi | Nối độ dài đệm, seek, $k$ và $p$ | bài 15.9 tr.48; lời giải tr.115 |
| S17 | kiểm tra | Tính đủ $k,r_0,p,C$, đáp án ẩn | ch15.19–22 |
| R00 | tình huống | Giảm $r_0$ để có thể giảm $p$ | Wisconsin 16–20 |
| R01 | trực giác/hình thức | Hoạt động/đóng băng; định nghĩa $H$ theo bản ghi | Wisconsin 16–18 |
| R02 | ví dụ | Khởi tạo $H=3$ trên dữ liệu nguồn | bài 15.1; Wisconsin |
| R03 | ví dụ | Phân loại khóa mới qua ba bước | Wisconsin 17–19 |
| R04 | ví dụ | Dãy đầu dài bảy từ $H=3$ | Wisconsin; bài 15.1 |
| R05 | kết quả | Ba dãy hợp đúng 12 khóa | vết đã chạy lại |
| R06 | thuật toán/chi phí | Giả mã, dừng, $O(n\log H)$, $O(H)$ bản ghi | Wisconsin 16–20 |
| R07 | tính đúng | Bất biến không giảm và mở dãy mới | Wisconsin 17–20 |
| R08 | kỳ vọng/biên | $2H$ chỉ dưới thứ tự đến ngẫu nhiên; giảm dần gần $H$ | Wisconsin 20 |
| R09 | kiểm tra | Áp dụng điều kiện đóng băng, đáp án ẩn | Wisconsin 17–19 |
| T00 | tổng hợp | Quan hệ $N,B,r_0,p$ và vai trò chọn thay thế | tổng hợp nguồn |
| T01 | chuyển ý | Quy trình giải trước recitation | tổng hợp nguồn |
| X00 | giao nhiệm vụ | Ba bài nguồn, tổng 60 phút | bài 15.1, 15.9, 13.5 |
| X01 | bài 15.1 | Đọc đặc tả, khóa, $N$, sản phẩm; 5 phút | bài 15.1 tr.47 |
| X02 | bài 15.1 | Tạo bốn dãy; 10 phút | lời giải PDF 1/tr.111 |
| X03 | bài 15.1 | Lượt đầu với ba khung luân phiên đầu dãy/đầu ra một bản ghi; 10 phút | lời giải PDF 1/tr.111 |
| X04 | bài 15.1 | Lượt cuối và chứng minh; 10 phút | lời giải PDF 1/tr.111 |
| X05 | bài 15.9 | Đánh đổi seek và fan-in; 15 phút | bài tr.48; lời giải tr.115 |
| X06 | bài 13.5 | Bảng băm tra khối; 10 phút | lời giải PDF 5/tr.95 |

## Câu nối và thay đổi thứ tự

- `I09→S00`: từ ngân sách khung sang thuật toán dùng ngân sách đó.
- `S01→S02→S03`: đặc tả → ví dụ nguồn → giả mã tạo dãy.
- `S06→S07→S08`: một lựa chọn cụ thể → chứng minh → thủ tục trộn tổng quát.
- `S11→Q00→S12`: biết số lượt → chốt cách tiêu thụ đầu ra → tính chi phí.
- `S17→R00`: chi phí phụ thuộc $p$, nên giảm số dãy ban đầu có giá trị.
- `R09→T00`: kết thúc thuật toán mở rộng rồi tổng hợp các đại lượng.
- `T01→X00`: chuyển từ bản đồ giải sang ba bài giáo trình.

So với nguồn, phần vật chất hóa/truyền dòng được đưa lên trước công thức chi phí. Ví dụ tạo dãy đứng trước giả mã. Vết $N=12,B=3,k=2$ thay các ví dụ minh họa tự tạo để giữ một chuỗi dữ liệu xuyên suốt.

## Thời lượng

Phần giảng: P 6 + I 25 + S00–S11 35 + Q 7 + S12–S17 18 + R 25 + T 4 = **120 phút**. Recitation: X01–X04 35 + X05 15 + X06 10 = **60 phút**. `X00` chỉ giao nhiệm vụ trong thời gian chuyển nhóm.
