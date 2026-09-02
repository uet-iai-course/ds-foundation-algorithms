# Storyboard Bài 3

## Hành trình khái niệm

Bảy mạch với chức năng và kết nối vào/ra:

1. Mở đầu (P/A): đặt bài toán xếp hạng trên đồ thị thưa; nhận vào Bài 2 (MapReduce), chuyển ra mạch B qua phương trình luồng A03.
2. B: chạy tay đóng góp trên cạnh rồi dựng ma trận cột và phép lặp; nhận trạng thái từ A03, chuyển đồ thị $y,a,m$ và ma trận $P$ sang C và D.
3. C: sửa nút cụt và bẫy nhện bằng hai biến thể; nhận đồ thị $y,a,m$ từ B, chuyển ma trận đã sửa $\bar P$ và $A_\beta$ sang D, và quy ước nút cụt sang E.
4. D: điều kiện hội tụ, ánh xạ co, cận dừng và kiểm tra kết quả; nhận $A_\beta$ từ C, chuyển thuật toán C07 thành điều kiện dừng và nghiệm D04 sang E và K.
5. E: tính toán thưa/MapReduce; nhận quy ước nút cụt từ C và điều kiện dừng từ D, chuyển chi phí $\Theta(n+m)$ sang K.
6. K (K00): kết luận thu hồi bài toán A00, ba khối đã xây và nối sang Bài 4.
7. R: recitation bốn bài MMDS dùng lại tài sản của phần giảng.

Đồ thị liên kết thưa tạo nhu cầu xếp hạng mà không dựng ma trận đặc. Sinh viên theo vết đóng góp trên cạnh của đồ thị $y,a,m$ trước khi chuyển sang ma trận cột. Hai biến thể nguồn của cùng đồ thị làm lộ nút cụt và bẫy nhện bằng số cụ thể. Quy ước sửa cột và hệ số giảm dẫn đến phép lặp có cận dừng. Phần cuối chuyển đúng trạng thái này sang bản ghi thưa, các pha MapReduce và hai tổng toàn cục.

## Phân bổ phần giảng: 120 phút

| Trang | Phút | Vai trò và câu nối | Nguồn |
|---|---:|---|---|
| P00 | 2 | Vị trí sau MapReduce | `sources/source.md`, Bài 3 |
| P01 | 3 | Sản phẩm quan sát được và tiên quyết | `sources/source.md`, Bài 3 |
| A00 | 3 | Đồ thị Web thưa và đầu ra theo nút | MMDS §5.1–5.2; slide 48, 53 |
| A01 | 4 | Đặc tả đồ thị đơn có vòng tự nối; gộp liên kết lặp | MMDS §5.1.1–5.1.2 |
| A02 | 3 | Trực giác người lướt ngẫu nhiên | Stanford 17–18; MMDS §5.1.2 |
| A03 | 4 | Phương trình luồng; nút cụt chưa xử lý | MMDS slide 18–21 |
| B00 | 2 | Mở phần chạy tay trước hình thức hóa | MMDS slide 18–24 |
| B01 | 4 | Đọc cạnh và bậc của đồ thị $y,a,m$ | MMDS slide 19, 24 |
| B02 | 4 | Chạy tay đóng góp ở vòng đầu | MMDS slide 18–21, 25–27 |
| B03 | 4 | Gom đúng các đóng góp thành cột ma trận | MMDS slide 21, 24 |
| B04 | 5 | Hai vòng lặp và bất biến tổng | MMDS slide 25–27 |
| B05 | 3 | Điểm cố định của đồ thị cơ sở | MMDS slide 19–20 |
| B06 | 3 | Bất khả quy, không chu kỳ và phản ví dụ hai nút với trạng thái đầu $(1,0)^T$ | MMDS §5.1.2 |
| C00 | 2 | Hai biến thể nguồn của cùng đồ thị | MMDS slide 38–46 |
| C01 | 4 | Nhận diện cạnh thay đổi ở nút cụt và bẫy nhện | MMDS slide 39, 41 |
| C02 | 5 | Chạy tay mất khối lượng tại nút cụt | MMDS slide 41 |
| C03 | 5 | Sửa cột nút cụt và chạy lại cùng trạng thái | MMDS slide 42, 44 |
| C04 | 4 | Chạy tay khối lượng mắc trong bẫy | MMDS slide 39 |
| C05 | 4 | Hình thức hóa hệ số giảm và dịch chuyển | MMDS slide 40, 44–45 |
| C06 | 5 | Chạy một vòng trên đúng biến thể bẫy nhện | MMDS slide 46 |
| C07 | 4 | Giả mã có $\tau$, $\varepsilon$, $K_{\max}\in\mathbb N$, $K_{\max}\ge1$ và cờ hội tụ; $P=\bar P$ | MMDS §5.1.2, §5.1.5; cận được làm chặt |
| D00 | 2 | Cầu nối từ bất biến sang hội tụ | MMDS §5.1.5 |
| D01 | 4 | Ma trận dương và nghiệm dừng duy nhất | MMDS §5.1.5; giả thiết bổ sung |
| D02 | 5 | Ánh xạ co theo chuẩn $L_1$ và trực giác số | Suy ra từ $P$ cột ngẫu nhiên |
| D03 | 5 | Cận hậu nghiệm và ngưỡng dừng | Tổng đuôi của dãy co |
| D04 | 3 | Nghiệm đồ thị cơ sở có hệ số giảm; phân biệt với C06; dẫn sang D05 | Tính lại độc lập |
| D05 | 4 | Kiểm tra xác định khi thêm cạnh $m\to y$ | Stanford 33–36; dữ liệu MMDS |
| E00 | 2 | Quy mô $10^9$ trong nguồn và giới hạn ma trận đặc | MMDS slide 48 |
| E01 | 3 | Biết $V$ và giữ đúng một bản ghi cấu trúc cho mọi nút, kể cả danh sách rỗng; bộ nhớ $\Theta(n+m)$ | MMDS §5.2.1; slide 53 |
| E02 | 3 | Map phát cấu trúc và đóng góp cạnh của toán tử thưa $P_0$ | MMDS §5.2.2; slide 52–55 |
| E03 | 3 | Nhóm và reduce giữ cả nút không có cạnh vào | MMDS §5.2.2 |
| E04 | 3 | $\bar P=P_0+ed^T/n$, cập nhật không cộng đôi $\delta$, $\Delta$, hai tác vụ MapReduce và hai điểm đồng bộ | Triển khai thưa của quy ước C03 |
| E05 | 3 | Chi phí mỗi vòng; kiểm tra cặp map trên đồ thị cơ sở và nút cụt của biến thể C02 | MMDS §5.2.1–5.2.2 |
| K00 | 3 | Kết luận: thu hồi bài toán A00, ba khối đã xây và nối sang Bài 4 | MMDS §5.1–5.2 |
| **Tổng** | **120** |  |  |

## Phân bổ bài tập: 60 phút giải trực tiếp

| Trang | Phút | Bài nguồn và sản phẩm |
|---|---:|---|
| R00 | 0 | Trang chuyển phần; không tính vào 60 phút |
| R02 | 15 | MMDS Bài 5.1.1, trang in 187–188, PDF 13–14: ma trận, hệ điểm cố định và vector chuẩn hóa của Hình 5.7 |
| R03 | 15 | MMDS Bài 5.1.2, trang in 188, PDF 14: phương trình với $\beta=0{,}8$, nghiệm và kiểm tra |
| R04 | 10 | MMDS Bài 5.2.1, trang in 195, PDF 21: bất đẳng thức và ngưỡng mật độ |
| R05 | 20 | MMDS Bài 5.2.2, trang in 195, PDF 21: biểu diễn Hình 5.4 và 5.7 |
| **Tổng** | **60** |  |

Việc giao nhóm và đối chiếu nằm trong khoảng của từng bài, không tính thành thời gian riêng. Mỗi block dành phần cuối để kiểm tra một sản phẩm cụ thể. Đáp án và hướng dẫn chấm chỉ nằm trong ghi chú diễn giả. R01 đã bị bỏ và id không được tái sử dụng; các trang recitation hiện là R00, R02–R05.

## Chu trình và trạng thái truyền

### PageRank cơ sở

- Tình huống: A00; vấn đề: A01; trực giác: A02–A03; ví dụ chạy tay: B01–B02; hình thức hóa: B03; phép lặp và điều kiện: B04–B06; kiểm tra: D05, R02–R03. E00–E01 không được tính hai lần: chúng thuộc chu trình phân tán; ở đây E00 chỉ thu hồi giới hạn ma trận đặc.
- Trạng thái truyền: cạnh và bậc ở B01 tạo các phần $1/6,1/3$ ở B02; các phần này trở thành cột ở B03 và hàng $t=1$ ở B04.

### Nút cụt và bẫy nhện

- Tình huống và vấn đề: C00–C02, C04; trực giác: C03, C05; ví dụ chạy tay: C02–C04, C06; hình thức hóa: C03, C05; thuật toán và lập luận: C07, D00–D03; ứng dụng và chi phí: E04; kiểm tra: C06, R05.
- Trạng thái truyền: vector đều ở C02 được dùng lại ở C03; dãy bẫy ở C04 dẫn đến $A_{0,8}$ và $r^{(1)}$ ở C06. Đồ thị cơ sở ở D04 được gọi rõ để không lẫn với biến thể bẫy.

### PageRank phân tán

- Tình huống: E00; vấn đề và trực giác: E01; ví dụ chạy tay: E02; hình thức hóa và thuật toán: E03–E04; chi phí và kiểm tra: E05.
- Trạng thái truyền: tập $V$ và đúng một bản ghi $S_i$ cho mỗi nút ở E01 tạo đầu vào đầy đủ, kể cả nút cô lập hoặc danh sách rỗng. Bản ghi $S_a$ tạo đúng hai cặp đóng góp của $P_0$ ở E02; cấu trúc được giữ qua E03. Vector chỉ báo $d$ gom nút cụt của C03 thành $\delta=d^Tr$ và E04 hiện thực $\bar P=P_0+ed^T/n$ mà không cộng hai lần.

## Sai khác và ranh giới

- Bất khả quy được nêu là điều kiện đủ cho nghiệm dừng duy nhất, không phải điều kiện cần.
- Cận dừng dùng hệ số $\beta/(1-\beta)$; $\tau$ là ngưỡng phần dư và $\varepsilon$ là sai số đích.
- Quy ước cột nút cụt bằng $e/n$ khác quy ước rò khối lượng ở một đoạn của sách. E04 gọi toán tử cạnh thưa là $P_0$, gọi ma trận đã sửa là $\bar P=P_0+ed^T/n$, rồi triển khai $\bar Pr=P_0r+\delta e/n$ mà không vật chất hóa cột đặc hoặc cộng $\delta$ hai lần.
- Một vòng PageRank có thể gồm hai tác vụ MapReduce khi $\delta$ cần pha tổng hợp riêng; không đồng nhất vòng thuật toán với tác vụ.
- Không dùng Topic-Sensitive PageRank, link spam, TrustRank, HITS hoặc phân khối ma trận §5.2.3. Mục §5.1.6 bị bỏ vì ngoài sản phẩm học tập và thời lượng của buổi này.
- Deck gồm 39 slide: P00–P01, A00–A03, B00–B06, C00–C07, D00–D05, E00–E05, K00 và R00, R02–R05.

## Hành trình riêng của ghi chú bài giảng

| `note-topic-id` | Kết nối vào | Thành phần trình bày | Đầu ra cho phần sau |
|---|---|---|---|
| `note-topic-03-web-graph` | Bài 02 và bài toán metadata Web | Vai trò, đặc tả $G,n,m$, giới hạn ma trận đặc, kiểm tra quy ước cạnh | Đầu vào cho mô hình người lướt |
| `note-topic-03-random-surfer` | Đồ thị có hướng | Định nghĩa phân phối, trực giác và ví dụ đóng góp một nút | Phương trình luồng |
| `note-topic-03-flow-matrix` | Đóng góp theo cạnh | Đặc tả ma trận cột, vết chạy $y,a,m$, điểm cố định, power iteration | Hai lỗi cấu trúc |
| `note-topic-03-dead-end` | Ma trận có cột tổng bằng 1 | Biến thể nút cụt, vết mất khối lượng, $\bar P$, chứng minh bảo toàn | Quy ước dùng trong triển khai thưa |
| `note-topic-03-spider-trap` | Phân phối đã được bảo toàn | Biến thể bẫy, $A_\beta$, nghiệm nguồn và kiểm tra phân biệt đồ thị | Ánh xạ co |
| `note-topic-03-convergence` | $A_\beta$ trên simplex | Mệnh đề, phản ví dụ $\beta=1$, chứng minh co và hệ quả | Cận dừng có bảo đảm |
| `note-topic-03-stopping` | Hệ số co $\beta$ | Giả mã, $\Delta_t$, cận hậu nghiệm, $\tau$, $K_{\max}$, hai hậu điều kiện | Thuật toán đủ để phân tán |
| `note-topic-03-sparse-mapreduce` | Bài 02, $P_0$, $d$, $\bar P$ | Bản ghi cấu trúc, hai pha, bất biến, ví dụ một nút, chi phí $\Theta(n+m)$ | Thu hồi tình huống mở bài |
| `note-topic-03-exercises` | Toàn bộ tuyến chính | Đề, hình, gợi ý và lời giải bốn bài nguồn | Tự đánh giá |
| `note-topic-03-boundary` | Kết luận PageRank cơ sở | Liên kết ngắn sang Bài 04 | Không tạo nội dung mới |

Ghi chú dùng cùng dữ kiện $(y,a,m)$ từ đóng góp theo cạnh tới ma trận, điểm cố định và ba biến thể. Tình huống kho metadata Web trở lại ở biểu diễn thưa, số bản ghi trung gian và chi phí mỗi vòng. Không áp dụng thời lượng hay `data-slide-id` cho hành trình này; deck chỉ được rà đồng bộ nếu bản ghi chú buộc phải đổi một ký hiệu, giả thiết, ví dụ hoặc kết luận dùng chung.
