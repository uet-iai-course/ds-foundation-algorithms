# Storyboard Bài 12

## Hành trình khái niệm

Quan hệ cần `ORDER BY` (`I00`) → khối và khung (`I01–I05`) → hai thước đo I/O (`I06–I09`) → hai pha sắp xếp (`S00–S01`) → ví dụ nguồn (`S02`) → thuật toán tạo dãy (`S03–S05`) → ví dụ trộn có refill/flush (`S06`) → tính đúng và giả mã đầy đủ (`S07–S09`) → cây lượt và số lượt (`S10–S11`) → điều kiện tiêu thụ đầu ra (`Q00–Q02`) → chi phí I/O, CPU và bộ nhớ (`S12–S17`) → chọn thay thế (`R00–R09`) → thu hồi tình huống `ORDER BY` và quyết định đầu ra (`T00–T01`) → bài nguồn (`X00–X06`).

Đầu vào xuyên suốt là bảng $N$ khối cần sắp theo khóa. Vết chính dùng nguyên 12 bản ghi của bài 15.1, một bản ghi mỗi khối, $N=12$, $B=3$, $k=2$, $r_0=4$, $p=2$. Bốn dãy ở `S02` đi vào ví dụ trộn `S06`, cây `S10`, hai công thức `S12–S14` và recitation `X01–X04`. Ký hiệu $H$ là số bản ghi vừa vùng heap; chỉ trong vết một bản ghi/khối mới có cùng giá trị số $H=B=3$.

## Bảy mạch trình bày

| Mạch | Trang | Chức năng | Kết nối vào | Kết nối ra | Đóng góp mục tiêu |
|---|---|---|---|---|---|
| Mở bài | P00–P02 | Đặt giới hạn bộ nhớ và đầu ra cần sắp | Bài 11 về biểu diễn/nén | Nhu cầu mô hình khối | Công bố bốn sản phẩm |
| Mô hình I/O | I00–I09 | Tách bản ghi, khối, khung, truyền và định vị | Tệp vượt RAM | Ngân sách $B$ và hệ số $k$ | Mô hình hóa chi phí |
| Thuật toán trộn ngoài | S00–S11 | Tạo dãy, trộn, chứng minh và đếm lượt | $N,B,k$ | Số lượt $p$ | Chạy và chứng minh thuật toán |
| Đầu ra và chi phí | Q00–Q02, S12–S17 | Chốt điều kiện sau rồi tính I/O, CPU, bộ nhớ | Một dãy cuối sau $p$ lượt | Động cơ giảm $r_0$ | Phân tích chi phí và đánh đổi |
| Chọn thay thế | R00–R09 | Tạo dãy dài hơn bằng trạng thái hoạt động/đóng băng | Chi phí phụ thuộc $p$ | Số dãy ban đầu có thể giảm | Chạy thuật toán mở rộng |
| Kết luận | T00–T01 | Thu hồi $N,B,k,r_0,p$ và quy trình giải | Hai cách tạo dãy | Nhiệm vụ luyện tập | Chọn đúng mô hình |
| Recitation | X00–X06 | Chạy vết, phân tích đệm và chọn cấu trúc tra cứu | Toàn bộ phần giảng | Sản phẩm nộp và hướng dẫn chấm | Luyện đủ 60 phút |

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
- Sản phẩm: ba dãy đúng đa tập, chi phí $O(n\log H)$ và phạm vi dùng quy tắc kinh nghiệm $2H$.

## Bản đồ từng trang

| Trang | Bước học tập | Lý do tồn tại / sản phẩm | Nguồn |
|---|---|---|---|
| P00 | mở bài | Đặt I/O làm trọng tâm | ch12.11; ch15.17 |
| P01 | mục tiêu | Chốt bốn sản phẩm quan sát được | ch15.17–23; Wisconsin 16–20 |
| P02 | mạch bài | Báo bốn nhánh theo đúng thứ tự khối → trộn → đầu ra/chi phí → dãy dài hơn | tổng hợp nguồn |
| I00 | tình huống/vấn đề | Bảng vượt RAM cần `ORDER BY` và cấp dòng | ch15.17, 51–59 |
| I01 | trực giác | Nối thiết bị–khối–khung | ch12.11; ch13.19 |
| I02 | trực giác | Phân biệt bản ghi và đơn vị truyền | ch12.11 |
| I03 | ví dụ/hình thức | Đổi số bản ghi sang số khối | ch13.2–3 |
| I04 | hình thức | Định nghĩa $B$ rồi suy ra $k=B-1$ | ch15.19–20 |
| I05 | cơ chế hệ thống | Trúng/trượt; định nghĩa nạn nhân và khối bẩn trước vết I08 | ch13.20 |
| I06 | chi phí | Định nghĩa lần truyền khối | ch15.22–23 |
| I07 | giới hạn | Tách truyền khối và lần định vị | ch12.10, 32–33 |
| I08 | ví dụ chạy tay | Theo dõi trúng, ghi bẩn và đọc | ch13.20 |
| I09 | kiểm tra | Tính $2N$ và $k$, đáp án ẩn | ch15.20, 22 |
| S00 | trực giác | Hai pha giải giới hạn bộ nhớ | ch15.17–21 |
| S01 | đặc tả | Miền, điều kiện $B\ge1$ và $B\ge3$ khi phải trộn, điều kiện sau, rỗng, khóa trùng | ch15.17–21 |
| S02 | ví dụ chạy tay | Tạo bốn dãy từ 12 bản ghi nguồn | bài 15.1 tr.47; lời giải PDF 1/tr.111 |
| S03 | thuật toán | Khái quát tạo dãy sau ví dụ | ch15.19 |
| S04 | hình thức | Suy ra $r_0$, nêu $N\le B$ | ch15.19 |
| S05 | cấu trúc dữ liệu | Phân bổ $k$ đầu vào + một đầu ra | ch15.20 |
| S06 | ví dụ chạy tay | Trộn $R_1,R_2$ với $B=3,k=2$; chạy một chu kỳ chọn–refill–flush | ch15.20; bài 15.1 |
| S07 | tính đúng | Khởi tạo–duy trì–kết thúc trên toàn phần chưa xuất | ch15.20 |
| S08 | thuật toán | Refill, flush, nhóm cuối nhỏ hơn $k$ | ch15.20–22 |
| S09 | thuật toán/dừng | Lặp lượt, $r\leftarrow\lceil r/k\rceil$, dừng ở một dãy | ch15.19–22 |
| S10 | ví dụ | Cây $4\rightarrow2\rightarrow1$ cùng vết nguồn | ch15.21; bài 15.1 |
| S11 | hình thức/chuyển ý | Suy ra $p$, rồi nêu lần ghi cuối còn phụ thuộc điều kiện đầu ra | ch15.21–22 |
| Q00 | trực giác | Phân biệt ghi tệp và truyền dòng | ch15.51–55 |
| Q01 | giới hạn | Tiêu thụ đủ đầu vào trước khi final merge phát dòng | ch15.56–59 |
| Q02 | điều kiện sau/biên | Chốt khi nào bỏ lần ghi cuối; nêu truyền trực tiếp khi $0<N\le B$ | ch15.51–59 |
| S12 | chi phí | Dẫn xuất $C_{\mathrm{mat}}$ và chính sách singleton | ch15.22, 51–53 |
| S13 | chi phí | Dẫn xuất $C_{\mathrm{pipe}}$ theo ba trường hợp $N=0$, $0<N\le B$, $p\ge1$ | ch15.51–59 |
| S14 | ứng dụng | Tính 72 và 60 trên $N=12,B=3$ | bài 15.1; ch15.22, 51–59 |
| S15 | chi phí | Tách I/O, CPU trộn qua $p$ lượt $O(np\log k)$, sắp mẻ đầu và $O(B)$ khung | ch15.19–23 |
| S16 | đánh đổi | Nối $b_b\in\mathbb{Z},b_b\ge1$, seek, $k\ge2$ và $p$; thế $B=11,b_b=2$; công thức là suy ra | bài 15.9 đề PDF 2/tr.48; lời giải PDF 5/tr.115 |
| S17 | kiểm tra | Tính đủ $k,r_0,p,C$, đáp án ẩn | ch15.19–22 |
| R00 | tình huống/chuyển ý | Đối chiếu hai đòn bẩy giảm $p$: đổi $k$ hoặc giảm $r_0$ | Wisconsin 16–20 |
| R01 | trực giác/hình thức | Hoạt động/đóng băng; nối $H$ bản ghi với vùng heap và giới hạn trường hợp $H=B=3$ | Wisconsin 16–18 |
| R02 | ví dụ | Khởi tạo $H=3$ trên dữ liệu nguồn | bài 15.1; Wisconsin |
| R03 | ví dụ | Phân loại khóa mới qua ba bước | Wisconsin 17–19 |
| R04 | ví dụ | Dãy đầu dài bảy từ $H=3$ | Wisconsin; bài 15.1 |
| R05 | kết quả | Ba dãy hợp đúng 12 khóa | dữ liệu bài 15.1; cơ chế Wisconsin 17–20; vết chạy lại |
| R06 | thuật toán/chi phí | Giả mã, dừng, $O(n\log H)$, $O(H)$ bản ghi | Wisconsin 16–20 |
| R07 | tính đúng | Bất biến không giảm và mở dãy mới | Wisconsin 17–20 |
| R08 | trung bình/biên | Tách nhận định “trung bình khoảng $2H$” của Wisconsin khỏi quy tắc sử dụng có điều kiện của bài giảng | Wisconsin 20; giới hạn sử dụng do deck nêu |
| R09 | kiểm tra | Áp dụng điều kiện đóng băng, đáp án ẩn | Wisconsin 17–19 |
| T00 | tổng hợp | Thu hồi `ORDER BY`, chuỗi $B\to(r_0,k)\to p\to C$, $H$ và hai đầu ra | tổng hợp nguồn |
| T01 | chuyển ý | Quy trình giải; giới hạn $k=B-1$ theo mô hình một khung ra; chọn vật chất hóa/truyền dòng | tổng hợp nguồn |
| X00 | giao nhiệm vụ | Ba bài nguồn, tổng 60 phút | bài 15.1, 15.9, 13.5 |
| X01 | bài 15.1 | Đọc đặc tả, khóa, $N$, sản phẩm; dữ liệu chia bốn dòng; 5 phút | bài 15.1 tr.47 |
| X02 | bài 15.1 | Tạo bốn dãy; 10 phút | lời giải PDF 1/tr.111 |
| X03 | bài 15.1 | Biến thể nguồn: đối chiếu S08, buộc nêu một tuple/khối và chứng minh lịch ba khung bằng ba bước trạng thái; 10 phút | lời giải PDF 1/tr.111; lịch I/O suy ra từ dữ kiện đề |
| X04 | bài 15.1 | Lượt cuối và chứng minh; đáp án chia hai dòng; 10 phút | lời giải PDF 1/tr.111 |
| X05 | bài 15.9 | Đánh đổi seek và fan-in; 15 phút | đề PDF 2/tr.48; lời giải PDF 5/tr.115 |
| X06 | bài 13.5 | Bảng băm tra khối; 10 phút | đề PDF 2/tr.42; lời giải PDF 5/tr.95 |

## Câu nối và thay đổi thứ tự

- `I09→S00`: từ ngân sách khung sang thuật toán dùng ngân sách đó.
- `S01→S02→S03`: đặc tả → ví dụ nguồn → giả mã tạo dãy.
- `S06→S07→S08`: một lựa chọn cụ thể → chứng minh → thủ tục trộn tổng quát.
- `S11→Q00→S12`: biết số lượt chưa đủ; phải chốt lần ghi cuối theo cách tiêu thụ đầu ra rồi mới tính chi phí.
- `S15→S16`: cùng số truyền khối có thể khác seek; tăng đệm mỗi dãy đổi seek lấy fan-in.
- `S16→S17→R00`: đổi $k$ hoặc giảm $r_0$ đều nhằm giảm $p$; S17 kiểm tra chuỗi công thức trước khi sang chọn thay thế.
- `R09→T00`: kết thúc thuật toán mở rộng rồi tổng hợp các đại lượng.
- `T00→T01→X00`: thu hồi tình huống `ORDER BY`, chọn vật chất hóa/truyền dòng, rồi chuyển từ bản đồ giải sang ba bài giáo trình; X03 báo trước biến thể nguồn.

So với nguồn, phần vật chất hóa/truyền dòng được đưa lên trước công thức chi phí. Ví dụ tạo dãy đứng trước giả mã. Vết $N=12,B=3,k=2$ thay các ví dụ minh họa tự tạo để giữ một chuỗi dữ liệu xuyên suốt.

Bốn cặp được cân nhắc nhưng không gộp trang: `I01/I02` tách hệ phân cấp khỏi đơn vị logic/vật lý; `I06/I07` tách lần truyền khỏi lần định vị; `Q01/Q02` tách điều kiện phát dòng khỏi điều kiện sau; `R06/R07` tách giả mã khỏi chứng minh. Gộp từng cặp sẽ đặt hai luận điểm hoặc giả mã với chứng minh trên cùng mặt trang và tăng tải nhận thức. Chỉ gộp wrapper ngoài `Q00–Q02` với `S12–S17`; thứ tự 53 trang không đổi.

Không đổi thứ tự `S01/S02` hoặc `S07/S08`: đặc tả ở S01 cho người học biết sản phẩm cần kiểm trên ví dụ S02; vết refill/flush mới tại S06 tạo cầu nối đủ cụ thể từ thao tác sang bất biến S07 rồi giả mã S08. Không hoãn $k$ khỏi I04 hay bỏ ký hiệu khỏi sơ đồ S00 vì $k$ là sản phẩm trực tiếp của phân bổ khung và được dùng ngay ở I09; thay vào đó S01 chốt đầy đủ điều kiện trước trước khi thuật toán chạy.

## Thời lượng

Phần giảng: P 6 + I 25 + S00–S11 35 + (Q00–Q02, S12–S17) 25 + R 25 + T 4 = **120 phút**. Recitation: X01–X04 35 + X05 15 + X06 10 = **60 phút**. `X00` chỉ giao nhiệm vụ trong thời gian chuyển nhóm.
