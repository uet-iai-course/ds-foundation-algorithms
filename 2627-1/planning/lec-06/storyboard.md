# Storyboard Bài 6

## Hành trình khái niệm

- Mở bài (P00–M02): tình huống Ví dụ 3.10 → hành trình lọc–định lượng–tổng quát–đối chiếu → bài toán đầu vào/đầu ra → tiêu chí bộ lọc. Đầu vào là chữ ký MinHash của Bài 5; đầu ra là bài toán lọc cặp truyền cho mạch phân dải.
- Phân dải: vấn đề B00 → trực giác B01 → ví dụ B02 → hình thức B03 → khóa B04 → lập luận B05 → kiểm tra biên B06. Đầu vào là bài toán lọc; đầu ra là điều kiện ứng viên truyền cho mạch xác suất.
- Xác suất: vấn đề Q00 → trực giác Q01 → ví dụ Q02 → hình thức Q03 → suy ra đường cong Q04 → ngưỡng và xấp xỉ Q05 → chọn tham số/kiểm tra Q06. Đầu vào là điều kiện phân dải; đầu ra là $q(s)$ và chi phí ứng viên truyền cho mạch thuật toán.
- Tạo ứng viên: vấn đề A00 → trực giác luồng A01 → ví dụ trạng thái A02 → đặc tả A03 → bất biến giai đoạn sinh cặp A04 → chi phí, bộ nhớ phụ trợ, truyền thông MapReduce và đối chiếu A05. Giai đoạn gom ngăn hoàn tất trước khi áp dụng bất biến ở A04. Đầu vào là $q(s)$; đầu ra là thuật toán và chi phí, rồi A05 báo trước phần MapReduce được giữ cho recitation trước khi chuyển sang ngôn ngữ chung của họ LSH.
- Họ LSH: vấn đề F00 → ví dụ MinHash cụ thể F01 → định nghĩa F02 → AND F03 → OR F04 → thứ tự và kiểm tra khái niệm F05. Đầu vào là phân dải MinHash; đầu ra là định nghĩa họ LSH truyền cho mạch ba độ đo.
- Các độ đo dùng chu trình rút gọn D00–D04 vì Hamming, góc và Euclid là tiên quyết: mỗi trang nối trực giác hình học với hàm băm, xác suất và trường hợp biên. Đầu vào là định nghĩa họ LSH; D04 nối ba phép va chạm cơ sở với ví dụ vân tay dùng OR rồi AND ở V00–V01.
- Vân tay dùng chu trình rút gọn V00–V01: tình huống và mô hình → hướng đánh đổi của hai tầng khuếch đại. Phép tính được giữ cho Bài tập 3.8.2; đây là ví dụ nguồn, không phải tuyên bố hiệu năng hiện thời. Đầu ra là kết luận C00, một section riêng gom ba quyết định thiết kế và nối sang Bài 7.
- Kết luận C00 là mạch giảng thứ sáu và là section riêng: đầu vào là năm mạch trước; trang thu hồi tình huống $10^6$ chữ ký bằng các đại lượng $pN,A,|C|$, dẫn trực tiếp vào recitation, rồi mới nối sang Bài 7.

Tình huống Ví dụ 3.10 truyền $N=10^6,p=250$ từ P01 qua hành trình P02 và M00–M02, trở lại ở Q06, A01 và A05 để giải thích vì sao phải giảm số cặp. Chữ ký $p\times N$ truyền xuyên suốt B–A; $s$ truyền từ MinHash sang $q(s)$; $\tau$ chỉ xuất hiện ở đối chiếu hậu kỳ; $C$ luôn là tập ứng viên đã loại trùng. Xác suất cơ sở dùng $\rho$ để không trùng với $p=br$. Độ dịch Euclid dùng $u$, không dùng $\tau$.

## Từng trang phần giảng

| ID | Phút | Lý do tồn tại và bước tiến | Đầu vào → sản phẩm | Nguồn |
|---|---:|---|---|---|
| P00 | 0 | Nhận diện bài và phạm vi. | Bài 5 → vị trí Bài 6 | MMDS Ch.3 |
| P01 | 3 | Mở bằng nút thắt có số liệu, không trang trí. | $10^6,250$ → gần $5\cdot10^{11}$ cặp | MMDS Ví dụ 3.10, tr.92 |
| P02 | 2 | Báo trước đủ hành trình lọc–định lượng–tổng quát hóa họ/độ đo–đối chiếu. | nút thắt → bốn chặng quan sát được | tổng hợp MMDS §§3.4, 3.6–3.8 |
| M00 | 3 | Chuyển tình huống thành bài toán đầu vào/đầu ra. | chữ ký → cặp có độ tương đồng $\ge\tau$ | MMDS §3.4 |
| M01 | 2 | Nhắc đẳng thức MinHash dưới hoán vị ngẫu nhiên đều; phân biệt với họ băm thực hành cần tính chất minwise. | $s$ → xác suất trùng một hàng | MMDS §§3.3.3, 3.4.2 |
| M02 | 2 | Đặt tiêu chí cho bộ lọc ứng viên. | quét mọi cặp → lọc xác suất + hậu kiểm | MMDS §3.4.3 |
| B00 | 2 | Nêu vấn đề giảm cặp mà không đọc lại mọi cặp chữ ký. | $p\times N$ → cấu trúc dải | MMDS §3.4.1 |
| B01 | 4 | Cho trực giác chia $p=br$ trước ký hiệu xác suất; trả lời câu hỏi B00 bằng cách nhóm $r$ hàng thành dải. | $p$ hàng → $b$ dải, mỗi dải $r$ hàng | MMDS slide 40–43 |
| B02 | 4 | Chạy tay ba chữ ký; chỉ $D_1,D_2$ trùng trọn dải 2. | vector dải → ngăn | MMDS §3.4.1, diễn đạt lại |
| B03 | 4 | Hình thức hóa điều kiện ứng viên. | trùng mọi hàng một dải → $\{i,j\}\in C$ | MMDS §3.4.1 |
| B04 | 3 | Ngăn lỗi dùng va chạm mã băm như bằng chứng trùng khóa. | $(\ell,\text{vector})$ → ngăn theo khóa đầy đủ | MMDS §3.4.1, tr.93 |
| B05 | 3 | Lập luận bao phủ theo từng dải. | cặp trùng dải → được sinh | MMDS §3.4.3 |
| B06 | 3 | Kiểm tra trường hợp biên; với $p$ cố định, tăng $r$ làm $q(s)$ giảm trên $0<s<1$. | $b,r$ → đánh đổi bỏ sót–va chạm sai | suy ra từ §3.4 |
| Q00 | 2 | Đặt câu hỏi định lượng cho một cặp cố định. | độ tương đồng $s$ → $q(s)$ | MMDS §3.4.2 |
| Q01 | 4 | Từ độc lập hàng suy ra xác suất một dải. | $s,r$ → $s^r$ | MMDS §3.4.2 |
| Q02 | 3 | Tính tay $s=.8,r=5,b=20$. | một dải → mọi dải | MMDS Ví dụ 3.12, tr.94 |
| Q03 | 3 | Hình thức hóa xác suất ít nhất một dải và nêu điều kiện độc lập, khóa đầy đủ. | $(1-s^r)^b$ → $q(s)$ | MMDS §3.4.2 |
| Q04 | 3 | Đọc đường xác suất theo cặp; chỉ gọi chữ S khi $b,r>1$. | $s$ → xác suất ứng viên | MMDS slide 48–52 |
| Q05 | 3 | Suy ra ngưỡng nửa chính xác; chuyển khai triển lớn-$b$ vào notes để giảm tải. | $q=1/2$ → $s_{1/2}$ | suy ra từ MMDS §3.4.2 |
| Q06 | 3 | Buộc quyết định hướng đổi $b,r$ khi $p$ cố định và nêu cái giá bỏ sót–va chạm sai. | $p,\tau,q(s)$ → hướng chọn tham số | MMDS Ví dụ 3.12 |
| A00 | 2 | Tách xác suất khỏi thuật toán hiện thực. | công thức → thao tác dữ liệu | MMDS §3.4.3 |
| A01 | 4 | Cho trực giác luồng trước kiểu dữ liệu và giả mã. | chữ ký → khóa → ngăn → $C$ → đối chiếu | MMDS §3.4.3 |
| A02 | 4 | Mở rộng các vector dải đã quen sang tập chỉ số cột khác để chạy trạng thái ngăn → $C$. | danh sách ngăn → cặp đã loại trùng | MMDS §3.4.3, diễn đạt lại |
| A03 | 4 | Nêu kiểu, điều kiện trước, giả mã, điều kiện sau và dừng. | $\Sigma,p,N$ → $C$ | MMDS §3.4.3 |
| A04 | 3 | Chứng minh giai đoạn hai bằng bất biến sau từng ngăn đã gom. | tiền tố ngăn đã duyệt → đúng của $C$ | lập luận từ thuật toán nguồn |
| A05 | 3 | Chốt thời gian, bộ nhớ phụ trợ, $bN+A$ bản ghi và $\Theta(pN+A)$ từ truyền trung gian; báo trước thiết kế hai công việc ở recitation rồi nối sang F00. | ngăn → $A,C$ → chi phí và hậu kiểm | MMDS §3.4.3; Bài tập 3.4.4 |
| F00 | 2 | Mở rộng từ Jaccard sang câu hỏi về một độ đo bất kỳ. | phân dải cụ thể → họ LSH | MMDS §3.6.1 |
| F01 | 4 | Chạy ví dụ MinHash $(0.3,0.6,0.7,0.4)$ trước định nghĩa. | khoảng cách Jaccard → $\rho$ | MMDS §3.6.2, Ví dụ 3.18, tr.105 |
| F02 | 3 | Phát biểu định nghĩa đúng theo $h\sim F$, không nói vùng giữa. | $d_1,d_2$ → $\alpha_1,\alpha_2$ | MMDS §3.6.1, tr.104 |
| F03 | 3 | Hình thức hóa AND trên các phép băm độc lập. | $\rho$ → $\rho^r$ | MMDS §3.6.3 |
| F04 | 3 | Hình thức hóa OR trên các phép băm độc lập. | $\rho$ → $1-(1-\rho)^b$ | MMDS §3.6.3 |
| F05 | 3 | Kiểm tra nghĩa AND/OR mà không tính chuỗi của recitation. | mọi nhánh so với ít nhất một nhánh | MMDS §3.6.3 |
| D00 | 2 | Định tuyến ba họ theo độ đo. | loại dữ liệu → họ băm | MMDS §3.7 |
| D01 | 4 | Chứng minh xác suất Hamming bằng chọn tọa độ đều; nêu miền $0\le d_1<d_2\le m$. | $H,m$ → $1-H/m$ | MMDS §3.7.1, tr.109 |
| D02 | 4 | Nối góc với pháp tuyến đẳng hướng; nói rõ Rademacher không cho đẳng thức tổng quát. | $\theta$ → $1-\theta/\pi$ dưới giả thiết | MMDS §3.7.2; Stanford 04 |
| D03 | 4 | Nêu phép chiếu Euclid với $a>0$, độ dịch độc lập và giới hạn của công thức điều kiện. | $v\sim\mathcal N(0,I)$, $u\sim U[0,a)$ → ngăn | MMDS §§3.7.4–3.7.5; Datar et al. 2004 |
| D04 | 2 | So sánh điều kiện ba họ và nối phép va chạm cơ sở sang OR–AND trong mô hình vân tay. | độ đo → lựa chọn có điều kiện → V00 | MMDS §3.7 |
| V00 | 3 | Đặt mô hình vân tay và cấu trúc ngăn đúng. | ba ô → ngăn “có”/ngăn đơn “không” | MMDS §§3.8.4–3.8.5 |
| V01 | 5 | Nêu hướng đánh đổi của OR rồi AND, không lộ phép tính recitation. | giả thiết mô hình của sách → nhiệm vụ tính ở R07–R09 | MMDS §§3.8.4–3.8.5; Bài tập 3.8.2 |
| C00 | 2 | Gom quyết định thiết kế, thu hồi gần $5\cdot10^{11}$ cặp bằng $pN,A,|C|$, dẫn vào recitation rồi mới nối Bài 7. | độ đo, họ băm, $b,r,\tau$ → quy trình và bài tập | MMDS §§3.4,3.6–3.8; `sources/source.md` |

Tổng phần giảng: **120 phút**.

## Từng trang bài tập

| ID | Phút | Vai trò và sản phẩm hiển thị | Đáp án trong notes | Nguồn |
|---|---:|---|---|---|
| R00 | 0 | Mở phần; tái kích hoạt hợp đồng map → trộn/nhóm → reduce của Bài 2; nêu ba sản phẩm nhóm. | không áp dụng | MMDS Ch.2–3 |
| R01 | 4 | Dữ kiện Bài 3.4.4 và hợp đồng vào/ra. | tiêu chí khóa | tr.96 |
| R02 | 7 | Khung trống mapper/reducer công việc 1. | lời giải công việc 1, 3 điểm; va chạm mã băm không là mục chấm riêng | tr.96 |
| R03 | 7 | Khung trống bộ ánh xạ/bộ giảm của công việc 2. | lời giải công việc 2, 3 điểm | tr.96 |
| R04 | 7 | Bảng kiểm trống và sản phẩm thiết kế hai job. | bốn điều kiện đúng, 4 điểm | tr.96 |
| R05 | 7 | Dữ kiện Bài 3.6.1; dùng nhất quán $\rho$ và khung (a),(b). | hai hàm xác suất, 4 điểm | tr.108 |
| R06 | 8 | Khung (c),(d), yêu cầu ghi các giá trị trung gian để giảm tải ký hiệu lồng. | hai hàm, 6 điểm | tr.108 |
| R07 | 5 | Dữ kiện mô hình Bài 3.8.2; phân biệt độc lập giữa ô, giữa hai dấu và giữa các hàm. | $.004096,.000064$, 2 điểm | tr.121–122 |
| R08 | 7 | Bảng trống phương án OR 2048. | TP/FN/FP, 4 điểm | tr.121–122 |
| R09 | 8 | Bảng trống phương án AND của hai nhóm OR 1024 và lựa chọn. | TP/FN/FP + so sánh, 4 điểm | tr.121–122 |

Tổng recitation: **60 phút**. Mặt trang không lộ kết quả; toàn bộ số, lời giải và rubric ở ghi chú.

## Ghi chú chu trình rút gọn và kết nối

- Chu trình F (vấn đề → ví dụ → định nghĩa → biến đổi) được rút gọn ở D00–D04 và V00–V01 vì đây là khung tổng quát đã dựng đầy đủ ở F00–F05, và chi phí hệ thống đã chốt ở A05; hai cụm này chỉ cần nối trực giác hình học với hàm băm và hướng đánh đổi.
- P01 nêu phép tính số cặp; A05 chốt chi phí tạo ứng viên. Hai trang này không lặp nhau: P01 mở tình huống, A05 định lượng chi phí thuật toán.
- Kết nối MapReduce: A05 phân biệt $bN+A$ bản ghi với dung lượng $\Theta(pN+A)$ từ trung gian nhưng giữ thiết kế cho recitation; R00 tái kích hoạt hợp đồng map → trộn/nhóm → reduce của Bài 2 trước Bài tập 3.4.4.
