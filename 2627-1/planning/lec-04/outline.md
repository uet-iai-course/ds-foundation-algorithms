# Bài 4: PageRank theo chủ đề, liên kết rác và HITS

## Phạm vi và sản phẩm học tập

- Vị trí: Bài 4 theo thứ tự đề xuất, giữ ngay sau PageRank cơ sở để dùng lại $P$, $\beta$, phép lặp và chuẩn $L_1$.
- Nguồn trục: MMDS 3e, Chương 5, mục 5.3–5.5; slide chính thức MMDS Chương 5, phần 2.
- Phạm vi: PageRank theo chủ đề, cụm thao túng liên kết, TrustRank, khối lượng rác và HITS.
- Loại khỏi bài: phân loại chủ đề bằng Jaccard ở mục 5.3.4; nội dung này thuộc mạch tương đồng ở Bài 5–6.
- Sản phẩm: tính một vector PageRank theo chủ đề; phân tích đúng công thức hạng của trang đích; diễn giải TrustRank và khối lượng rác; chạy HITS và nêu điều kiện hội tụ; so sánh bốn mô hình.
- Thời lượng: 120 phút giảng và 60 phút bài tập trên lớp.

## Mạch nội dung

1. PageRank theo chủ đề: bắt đầu từ truy vấn đa nghĩa “jaguar”, thay vector dịch chuyển đều bằng $q_S$, rồi chọn hoặc phối hợp các vector đã tính.
2. Liên kết rác: theo vết luồng hạng trong Hình 5.16, phân biệt công thức chính xác với xấp xỉ của sách và thay số theo Ví dụ 5.11.
3. TrustRank: dùng tập tin cậy làm tập dịch chuyển; khối lượng rác là tỷ số chẩn đoán, không phải xác suất.
4. HITS: hai vai trò, ma trận hàng nguồn, hai phép nhân thưa, chuẩn hóa vô cùng và điều kiện dừng.
5. So sánh: chọn mô hình theo phạm vi đồ thị, tín hiệu khởi tạo, đầu ra và chi phí.

## Chu trình học tập

| Cụm | Tình huống → vấn đề | Trực giác → ví dụ | Hình thức → tính đúng | Chi phí → kiểm tra |
|---|---|---|---|---|
| PageRank theo chủ đề | T00 | T01–T04 | T02, T05 | T06–T07 |
| Cụm thao túng liên kết | S00–S02 | S03 | S04 | S05 |
| TrustRank và khối lượng rác | K00–K02 | K04 | K03 | K05 |
| HITS | H00–H01 | H03, H06–H07 | H02, H04–H05, H08 | H09 |
| So sánh và tổng kết | Z00 | Z01 | Z02 | Z03 |
| Bài tập trên lớp | R00 | R01 | R02 | R03–R04 |

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $G=(V,E)$, $n=|V|$, $m_G=|E|$ | Đồ thị, số nút và số cạnh |
| $P$ | Ma trận chuyển cột ngẫu nhiên đã sửa nút cụt từ Bài 3 |
| $S\ne\varnothing$, $e_S$, $q_S=e_S/|S|$ | Tập dịch chuyển theo chủ đề, vector chỉ báo và phân phối chủ đề |
| $r^{(t+1)}=\beta Pr^{(t)}+(1-\beta)q_S$ | Phép lặp PageRank theo chủ đề |
| $N,q,x,y$ | Tổng số trang Web, số trang hỗ trợ, đóng góp ngoài đã có hệ số giảm và hạng trang đích trong Hình 5.16 |
| $T\ne\varnothing$, $q_T=e_T/|T|$, $t$ | Tập tin cậy, phân phối dịch chuyển tin cậy và vector TrustRank |
| $r_p,t_p,s_p$ | PageRank cơ sở, TrustRank và khối lượng rác của trang $p$ |
| $L$ | Ma trận liên kết Boolean của HITS; hàng là nguồn |
| $h,a$ | Vector trang trung tâm và trang thẩm quyền |
| $K_{\max},\tau$ | Giới hạn vòng và ngưỡng dừng HITS, $0&lt;\tau&lt;1$ |

## Hàng ID Z và R

- Hàng Z00–Z03 là một cụm riêng, không nằm trong bảng HITS; Z03 thu hồi các sản phẩm học tập của P01 và nối sang phần bài tập.
- ID HITS giữ thứ tự phi tuần tự có chủ ý: H00→H01→H03→H02→H04→H06→H07→H05→H08→H09, để chạy tay trên cạnh trước khi đưa ma trận và giả mã vào.
- R00 mở section bài tập trên lớp; R01–R04 phân bổ đúng 60 phút.

## Phân bổ bài tập trên lớp

| Trang | Nội dung | Phút |
|---|---|---:|
| R00 | Mở phần bài tập, bản đồ bốn bài | 0 (trong 60) |
| R01 | MMDS Bài 5.3.1 | 18 |
| R02 | Dữ kiện Bài 5.4.2 dùng cho R03 và R04 | 3 |
| R03 | MMDS Bài 5.4.2 | 19 |
| R04 | MMDS Bài 5.5.1 | 20 |

## Ánh xạ nguồn

| Nội dung | Nguồn | Quyết định |
|---|---|---|
| PageRank theo chủ đề, Hình 5.15 | MMDS §5.3.1–5.3.3; Hình 5.15; slide MMDS phần 2, 7–11 | Giữ mạch, Việt hóa và làm rõ $S\ne\varnothing$ |
| Jaccard phân loại chủ đề | MMDS §5.3.4 | Bỏ; thuộc mạch MinHash và không cần cho phép lặp |
| Cụm thao túng, Hình 5.16 | MMDS §5.4.1–5.4.2; slide MMDS phần 2, 29–35 | Đổi $n,m$ của sách thành $N,q$; nêu đẳng thức chính xác, xấp xỉ và Ví dụ 5.11 |
| TrustRank, Hình 5.17 | MMDS §5.4.3–5.4.5; slide MMDS phần 2, 37–45 | Giữ bảng HTML; bổ sung điều kiện $r_p>0$ và giới hạn diễn giải |
| HITS, Hình 5.18–5.20 | MMDS §5.5.1–5.5.2; slide MMDS phần 2, 47–60 | Vẽ lại Hình 5.18; Hình 5.19 bằng KaTeX; Hình 5.20 bằng hai bảng HTML |
| Bài tập | MMDS Bài 5.3.1, 5.4.2, 5.5.1 | Dùng đồ thị trung tính cho 5.3.1 và 5.4.2; tách dữ kiện của 5.4.2; giữ yêu cầu, đáp án chỉ trong notes |

## Điều kiện thuật toán HITS

- Đầu vào: đồ thị con cố định, thứ tự nút xác định, $L\in\{0,1\}^{n\times n}$, $K_{\max}\ge1$, $0&lt;\tau&lt;1$.
- Khởi tạo: $h^{(0)}=e$; chuẩn hóa vô cùng sau mỗi phép nhân.
- Trường hợp biên: nếu một vector thô bằng 0, trả hai vector 0 và bật cờ suy biến thay vì chia cho 0.
- Điều kiện sau: $h,a\ge0$; mỗi vector khác 0 có chuẩn vô cùng bằng 1; hai cờ phân biệt đạt ngưỡng với trường hợp suy biến.
- Hội tụ đến một hướng riêng duy nhất chỉ khi hướng riêng trội phù hợp tồn tại và khởi tạo có thành phần trên hướng đó.
- Trình tự dạy: đọc đóng góp trên cạnh của Hình 5.18, chạy hai vòng số, rồi mới chốt giả mã và điều kiện hội tụ.
- Một vòng dùng hai phép nhân thưa, công việc $\Theta(n+m_G)$ và hai phép lấy cực đại toàn cục.

## Quy trình dùng PageRank theo chủ đề

1. Một mô hình bên ngoài PageRank xác định chủ đề hoặc trọng số $\alpha_1,\ldots,\alpha_k$.
2. Chọn một vector $r^{(S_\ell)}$ hoặc phối hợp $\sum_\ell\alpha_\ell r^{(S_\ell)}$.
3. Dùng điểm này khi xếp hạng kết quả truy vấn.

Không triển khai cách suy chủ đề bằng Jaccard trong bài này; Bài 5 cung cấp tiên quyết về độ tương đồng tập hợp.
