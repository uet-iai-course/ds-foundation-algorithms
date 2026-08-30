# Storyboard Bài 4

## Hành trình khái niệm

Bài dùng lại phép lặp PageRank của Bài 3, chỉ thay vector dịch chuyển để tạo xếp hạng theo chủ đề. Cùng cơ chế đó dẫn đến TrustRank, còn cụm thao túng liên kết cho thấy điểm toàn cục có thể bị dồn bằng cấu trúc liên kết. HITS đổi cả đầu ra lẫn quy ước ma trận: hai vector trên đồ thị con truy vấn, hàng của $L$ là nút nguồn. Trang Z03 thu hồi các sản phẩm học tập của P01 rồi nối sang phần bài tập; trang R00 mở section bài tập trên lớp. Trang Z01 buộc người học chọn mô hình theo mục tiêu thay vì coi bốn tên là các biến thể tương đương.

## Phân bổ phần giảng: 120 phút

| Trang | Phút | Vai trò và câu nối | Nguồn |
|---|---:|---|---|
| P00 | 2 | Nối ký hiệu và điều kiện từ Bài 3 | `sources/source.md`; Bài 3 |
| P01 | 3 | Sản phẩm quan sát được | `sources/source.md`, Bài 4 |
| T00 | 3 | Truy vấn “jaguar” đa nghĩa rồi đến giới hạn vector riêng cho mỗi người | MMDS §5.3.1 |
| T01 | 4 | Trực giác dịch chuyển về tập mẫu rồi mới định nghĩa $S,e_S,q_S$ | MMDS §5.3.2 |
| T02 | 3 | Hình thức hóa phép cập nhật chỉ thay vector dịch chuyển | MMDS §5.3.2 |
| T03 | 3 | Hình 5.15, $S=\{B,D\}$ | MMDS Hình 5.15 |
| T04 | 5 | Bảng đóng góp cạnh, dịch chuyển và kết quả một vòng; không nêu điểm cố định gần đúng | MMDS Ví dụ 5.10 |
| T05 | 3 | Chứng minh co $L_1$ | Công thức MMDS, điều kiện từ Bài 3 |
| T06 | 3 | Chi phí $k$ vector | MMDS §5.3.1–5.3.3 |
| T07 | 4 | Bộ phân loại bên ngoài → chọn/phối hợp vector → xếp hạng; nối sang Bài 5 | MMDS §5.3.3–5.3.4 |
| S00 | 2 | Tình huống liên kết rác | MMDS §5.4.1 |
| S01 | 3 | Hình 5.16 và ba vùng trang | MMDS Hình 5.16 |
| S02 | 3 | Định nghĩa $N,q,x,y$; phân biệt $n,m_G$ của đồ thị | MMDS §5.4.2 |
| S03 | 4 | Luồng hạng qua một trang hỗ trợ; tách hai nguồn hạng trên mặt trang | MMDS §5.4.2 |
| S04 | 5 | Suy ra công thức chính xác với $N,q$; hiện phương trình mở rộng trước khi giải | Tính lại từ hệ nguồn |
| S05 | 5 | Ví dụ 5.11, xấp xỉ, sai số và kiểm tra ba nguồn hạng | MMDS Ví dụ 5.11 |
| K00 | 3 | TrustRank là PageRank theo chủ đề; hiện $q_T$, khởi tạo $t^{(0)}=q_T$ và phương trình | MMDS §5.4.3–5.4.4 |
| K01 | 4 | Hai cách chọn hạt giống | MMDS §5.4.4 |
| K02 | 3 | Giới hạn của tập tin cậy | MMDS §5.4.4 |
| K03 | 4 | Đặc tả khối lượng rác | MMDS §5.4.5 |
| K04 | 5 | Bảng Hình 5.17; cảnh báo hai thiết lập nguồn khác nhau ngay trên mặt trang | MMDS Hình 5.17 |
| K05 | 4 | Kiểm tra dấu và giới hạn diễn giải | MMDS §5.4.5 |
| H00 | 3 | Đồ thị con thưa của kết quả truy vấn; câu nối một điểm → hai vai trò; không dựng ma trận đặc toàn Web | MMDS §5.5 |
| H01 | 3 | Trực giác hai vai trò | MMDS §5.5.1 |
| H03 | 4 | Hình 5.18; định nghĩa $a$ và $h$ trên mặt trang; chạy tay hai tổng trên cạnh trước ma trận | MMDS Hình 5.18 |
| H02 | 4 | Quy ước $L$ hàng nguồn, khác $P$; nối từ tổng trên cạnh | MMDS §5.5.2 |
| H04 | 3 | Chỉ hiển thị $L$ của Hình 5.19; quy tắc chuẩn hóa trên mặt trang | MMDS Hình 5.19 |
| H06 | 4 | Vòng 1 của Hình 5.20 | MMDS Hình 5.20 |
| H07 | 4 | Vòng 2 của Hình 5.20 | MMDS Hình 5.20 |
| H05 | 5 | Giả mã sau ví dụ; dừng, cờ, hai nhánh vector 0 và điều kiện $0&lt;\tau&lt;1$ trên mặt trang | MMDS §5.5.2, bổ sung đặc tả |
| H08 | 3 | Dạng trị riêng và điều kiện hội tụ | MMDS §5.5.2, điều kiện làm chặt |
| H09 | 3 | Công việc $\Theta(n+m_G)$, hai chuẩn hóa và kiểm tra chiều cập nhật | Suy ra từ hai phép nhân thưa |
| Z00 | 1 | Mở phần so sánh | Tổng hợp §5.3–5.5 |
| Z01 | 3 | So sánh $P$ chia bậc với $L,L^T$ Boolean; thêm $a^{(0)}=0$ và $t^{(0)}=q_T$ | Tổng hợp §5.3–5.5 |
| Z02 | 2 | Chi phí, đầu ra và câu hỏi chọn mô hình | Tổng hợp §5.3–5.5 |
| Z03 | 2 | Thu hồi sản phẩm P01 và nối sang phần bài tập | Tổng hợp §5.3–5.5 |
| **Tổng** | **120** |  |  |

## Phân bổ bài tập: 60 phút

| Trang | Phút | Bài nguồn và sản phẩm |
|---|---:|---|
| R00 | 0 | Mở section bài tập; bản đồ bốn bài và quy ước đáp án trong notes |
| R01 | 18 | MMDS Bài 5.3.1, trang in 199, PDF 25: chia hai ý giữa nhóm rồi đối chiếu hai vector; giải thích phần dư điểm cố định $(1-\beta)q_S$ |
| R02 | 3 | Dữ kiện MMDS Bài 5.4.2: đồ thị trung tính, ma trận $P$ và PageRank cơ sở; ghi rõ dùng cho R03 và R04 |
| R03 | 19 | MMDS Bài 5.4.2, trang in 204, PDF 30: TrustRank và khối lượng rác khi chỉ B tin cậy |
| R04 | 20 | MMDS Bài 5.5.1, trang in 208, PDF 34: nối dữ kiện từ R02, phân biệt $L$ hàng nguồn với $P$ cột nguồn và HITS hai vai trò với PageRank một điểm; phân nhóm theo vết và lặp có ngưỡng $10^{-3}$ |
| **Tổng** | **60** |  |

Không có trang logistics riêng. Mỗi trang bài tập chứa đủ dữ kiện, yêu cầu và sản phẩm; đáp án cùng rubric chỉ nằm trong ghi chú diễn giả.

## Bước gộp và không áp dụng

- T01–T02 tách đặc tả khỏi trực giác để không dùng $q_S$ trước khi định nghĩa.
- S04–S05 tách đẳng thức chính xác khỏi xấp xỉ của sách; gộp sẽ che mất số hạng bị bỏ.
- K03–K04 tách định nghĩa tỷ số khỏi bảng số để tránh diễn giải bảng như xác suất.
- H03 đưa phép cộng trên cạnh trước H02–H05; H06–H07 tách Hình 5.20 thành hai bảng HTML cỡ `.75em`, rồi H05 mới chốt giả mã.
- Phân loại chủ đề bằng Jaccard ở §5.3.4: không áp dụng; nội dung cần tiên quyết từ mạch tương đồng và không tham gia phép lặp xếp hạng.
- Dựng $LL^T$ và $L^TL$: không áp dụng trong cài đặt; chỉ giữ dạng đại số ở H08 vì tích có thể đặc.

## Câu nối chính

- T07 → S00: thay nơi dịch chuyển đổi ý nghĩa điểm, nhưng cấu trúc liên kết vẫn có thể dồn hạng.
- S05 → K00: thay vì nhận diện từng cấu trúc, TrustRank đổi nơi dịch chuyển sang trang đáng tin.
- K05 → H00: TrustRank vẫn cho một điểm; H00 nối "một điểm" sang "hai vai trò" trong ngữ cảnh truy vấn.
- H09 → Z00: khác biệt về phạm vi, đầu ra và đồng bộ quyết định mô hình phù hợp.
- Z01 → Z02: cơ chế truyền điểm được chốt trước khi so chi phí và chọn mô hình.
- Z02 → Z03: thu hồi sản phẩm P01 trước khi chuyển sang bài tập.
- Z03 → R00: kết thúc phần giảng, mở section bài tập trên lớp.
- R00 → R01: bản đồ bốn bài trước khi vào bài đầu tiên.
- R02 → R03/R04: dữ kiện dùng chung cho cả hai bài; R04 phân biệt $L$ với $P$ và HITS với PageRank.

## Trạng thái truyền sau chỉnh sửa

- T00 đưa truy vấn “jaguar” sang T07: mô hình bên ngoài xác định chủ đề, PageRank chỉ cung cấp các vector đã tính.
- T03 cung cấp cạnh và tập $S$; T04 giữ riêng đóng góp cạnh, dịch chuyển và tổng để sinh viên kiểm tra từng phần; điểm cố định gần đúng đã bỏ khỏi T04, chỉ còn trong bài tập R01.
- S02 cố định $N,q,x,y$; S03 tách hai nguồn hạng trên mặt trang; S04 hiện phương trình mở rộng trước khi giải; S03–S05 không quay lại ký hiệu $n,m$ của sách.
- H03 chuyển hai tổng trên cạnh sang quy ước hàng nguồn ở H02, ma trận H04 và hai bảng vết H06–H07; H05 khái quát đúng trạng thái đã thấy với $0&lt;\tau&lt;1$.
- K00 hiện khởi tạo $t^{(0)}=q_T$; Z01 ghi $a^{(0)}=0$ và $t^{(0)}=q_T$ trong bảng so sánh.
- R00 mở section bài tập; R02 ghi rõ dùng cho R03 và R04; R04 nối dữ kiện từ R02 và phân biệt $L$ hàng nguồn với $P$ cột nguồn, hai vai trò HITS với một điểm PageRank.
- R01 và R02 dùng `hinh-5-1-trung-tinh.svg`, không mang tập $S=\{B,D\}$ của T03 sang bài có tập khác.
