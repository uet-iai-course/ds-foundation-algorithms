# Storyboard Bài 6

## Hành trình khái niệm

- Phân dải: vấn đề B00 → trực giác B01 → ví dụ B02 → hình thức B03 → khóa B04 → lập luận B05 → kiểm tra biên B06.
- Xác suất: vấn đề Q00 → trực giác Q01 → ví dụ Q02 → hình thức Q03 → suy ra đường cong Q04 → ngưỡng và xấp xỉ Q05 → chọn tham số/kiểm tra Q06.
- Tạo ứng viên: vấn đề A00 → trực giác luồng A01 → ví dụ trạng thái A02 → đặc tả A03 → bất biến giai đoạn sinh cặp A04 → chi phí, bộ nhớ và đối chiếu A05. Giai đoạn gom ngăn hoàn tất trước khi áp dụng bất biến ở A04.
- Họ LSH: vấn đề F00 → ví dụ MinHash cụ thể F01 → định nghĩa F02 → AND F03 → OR F04 → thứ tự và kiểm tra khái niệm F05.
- Các độ đo dùng chu trình rút gọn D00–D04 vì Hamming, góc và Euclid là tiên quyết: mỗi trang nối trực giác hình học với hàm băm, xác suất và trường hợp biên.
- Vân tay dùng chu trình rút gọn V00–V01: tình huống và mô hình → hướng đánh đổi của hai tầng khuếch đại. Phép tính được giữ cho Bài tập 3.8.2; đây là ví dụ nguồn, không phải tuyên bố hiệu năng hiện thời.

Tình huống Ví dụ 3.10 truyền $N=10^6,p=250$ từ P01 qua hành trình P02 và M00–M02, trở lại ở Q06, A01 và A05 để giải thích vì sao phải giảm số cặp. Chữ ký $p\times N$ truyền xuyên suốt B–A; $s$ truyền từ MinHash sang $q(s)$; $\tau$ chỉ xuất hiện ở đối chiếu hậu kỳ; $C$ luôn là tập ứng viên đã loại trùng. Xác suất cơ sở dùng $\rho$ để không trùng với $p=br$. Độ dịch Euclid dùng $u$, không dùng $\tau$.

## Từng trang phần giảng

| ID | Phút | Lý do tồn tại và bước tiến | Đầu vào → sản phẩm | Nguồn |
|---|---:|---|---|---|
| P00 | 0 | Nhận diện bài và phạm vi. | Bài 5 → vị trí Bài 6 | MMDS Ch.3 |
| P01 | 3 | Mở bằng nút thắt có số liệu, không trang trí. | $10^6,250$ → gần $5\cdot10^{11}$ cặp | MMDS Ví dụ 3.10, tr.92 |
| P02 | 2 | Nêu sản phẩm và hành trình lọc–định lượng–đối chiếu. | nút thắt → mục tiêu quan sát được | tổng hợp MMDS §§3.4, 3.6–3.8 |
| M00 | 3 | Chuyển tình huống thành bài toán đầu vào/đầu ra. | chữ ký → cặp có độ tương đồng $\ge\tau$ | MMDS §3.4 |
| M01 | 2 | Nhắc đúng bảo đảm MinHash và giả thiết độc lập–đều. | $s$ → xác suất trùng một hàng | MMDS §§3.3.3, 3.4.2 |
| M02 | 2 | Đặt tiêu chí cho bộ lọc ứng viên. | quét mọi cặp → lọc xác suất + hậu kiểm | MMDS §3.4.3 |
| B00 | 2 | Nêu vấn đề giảm cặp mà không đọc lại mọi cặp chữ ký. | $p\times N$ → cấu trúc dải | MMDS §3.4.1 |
| B01 | 4 | Cho trực giác chia $p=br$ trước ký hiệu xác suất. | $p$ hàng → $b$ dải, mỗi dải $r$ hàng | MMDS slide 40–43 |
| B02 | 4 | Chạy tay ba chữ ký; chỉ $D_1,D_2$ trùng trọn dải 2. | vector dải → ngăn | MMDS §3.4.1, diễn đạt lại |
| B03 | 4 | Hình thức hóa điều kiện ứng viên. | trùng mọi hàng một dải → $\{i,j\}\in C$ | MMDS §3.4.1 |
| B04 | 3 | Ngăn lỗi dùng va chạm mã băm như bằng chứng trùng khóa. | $(\ell,\text{vector})$ → ngăn theo khóa đầy đủ | MMDS §3.4.1, tr.93 |
| B05 | 3 | Lập luận bao phủ theo từng dải. | cặp trùng dải → được sinh | MMDS §3.4.3 |
| B06 | 3 | Kiểm tra trường hợp biên và giới hạn phân dải. | $b,r$ → nhận định đúng/sai | suy ra từ §3.4 |
| Q00 | 2 | Đặt câu hỏi định lượng cho một cặp cố định. | độ tương đồng $s$ → $q(s)$ | MMDS §3.4.2 |
| Q01 | 4 | Từ độc lập hàng suy ra xác suất một dải. | $s,r$ → $s^r$ | MMDS §3.4.2 |
| Q02 | 3 | Tính tay $s=.8,r=5,b=20$. | một dải → mọi dải | MMDS Ví dụ 3.12, tr.94 |
| Q03 | 3 | Hình thức hóa xác suất ít nhất một dải và nêu điều kiện độc lập, khóa đầy đủ. | $(1-s^r)^b$ → $q(s)$ | MMDS §3.4.2 |
| Q04 | 3 | Đọc đường xác suất theo cặp; chỉ gọi chữ S khi $b,r>1$. | $s$ → xác suất ứng viên | MMDS slide 48–52 |
| Q05 | 3 | Suy ra ngưỡng nửa chính xác và xấp xỉ có $\ln2$. | $q=1/2$ → $s_{1/2}$ | suy ra từ MMDS §3.4.2 |
| Q06 | 3 | Chọn $b,r$ dưới ràng buộc $p=br$ và kiểm tra cách diễn giải. | $p,\tau$ → cấu hình thử | MMDS Ví dụ 3.12 |
| A00 | 2 | Tách xác suất khỏi thuật toán hiện thực. | công thức → thao tác dữ liệu | MMDS §3.4.3 |
| A01 | 4 | Cho trực giác luồng trước kiểu dữ liệu và giả mã. | chữ ký → khóa → ngăn → $C$ → đối chiếu | MMDS §3.4.3 |
| A02 | 4 | Chạy trạng thái ngăn → $C$ trên ví dụ nhỏ. | danh sách ngăn → cặp đã loại trùng | MMDS §3.4.3, diễn đạt lại |
| A03 | 4 | Nêu kiểu, điều kiện trước, giả mã, điều kiện sau và dừng. | $\Sigma,p,N$ → $C$ | MMDS §3.4.3 |
| A04 | 3 | Chứng minh giai đoạn hai bằng bất biến sau từng ngăn đã gom. | tiền tố ngăn đã duyệt → đúng của $C$ | lập luận từ thuật toán nguồn |
| A05 | 3 | Chốt chi phí tạo ứng viên, bộ nhớ và hai mức bảo đảm hậu kiểm; chỉ nêu nhiệm vụ hai công việc. | ngăn → $A,C$ → ước lượng hoặc Jaccard đúng | MMDS §3.4.3; Bài tập 3.4.4 |
| F00 | 2 | Mở rộng từ Jaccard sang câu hỏi về một độ đo bất kỳ. | phân dải cụ thể → họ LSH | MMDS §3.6.1 |
| F01 | 4 | Chạy ví dụ MinHash $(0.3,0.6,0.7,0.4)$ trước định nghĩa. | khoảng cách Jaccard → $\rho$ | MMDS Ví dụ 3.18, tr.105 |
| F02 | 3 | Phát biểu định nghĩa đúng theo $h\sim F$, không nói vùng giữa. | $d_1,d_2$ → $\alpha_1,\alpha_2$ | MMDS §3.6.1, tr.104 |
| F03 | 3 | Hình thức hóa AND trên các phép băm độc lập. | $\rho$ → $\rho^r$ | MMDS §3.6.3 |
| F04 | 3 | Hình thức hóa OR trên các phép băm độc lập. | $\rho$ → $1-(1-\rho)^b$ | MMDS §3.6.3 |
| F05 | 3 | Kiểm tra nghĩa AND/OR mà không tính chuỗi của recitation. | mọi nhánh so với ít nhất một nhánh | MMDS §3.6.3 |
| D00 | 2 | Định tuyến ba họ theo độ đo. | loại dữ liệu → họ băm | MMDS §3.7 |
| D01 | 4 | Chứng minh xác suất Hamming bằng chọn tọa độ đều; dùng $m$ cho số chiều. | $H,m$ → $1-H/m$ | MMDS §3.7.1, tr.109 |
| D02 | 4 | Nối góc với pháp tuyến đẳng hướng; yêu cầu vector khác không. | $\theta$ → $1-\theta/\pi$ | MMDS §3.7.2; Stanford 04 |
| D03 | 4 | Nêu phép chiếu Euclid có độ dịch và giới hạn của công thức điều kiện. | $v\sim\mathcal N(0,I)$, $u\sim U[0,a)$ → ngăn | MMDS §§3.7.4–3.7.5; Datar et al. 2004 |
| D04 | 2 | So sánh bảo đảm và giới hạn của ba họ. | độ đo → lựa chọn có điều kiện | MMDS §3.7 |
| V00 | 3 | Đặt mô hình vân tay và cấu trúc ngăn đúng. | ba ô → ngăn “có”/ngăn đơn “không” | MMDS §§3.8.4–3.8.5 |
| V01 | 5 | Nêu hướng đánh đổi của OR rồi AND, không lộ phép tính recitation. | $.2,.8$ → nhiệm vụ tính ở R07–R09 | MMDS §§3.8.4–3.8.5; Bài tập 3.8.2 |
| C00 | 2 | Gom quyết định thiết kế, nối sang đối chiếu và Bài 7. | độ đo, họ băm, $b,r,\tau$ → quy trình | MMDS §§3.4,3.6–3.8; `sources/source.md` |

Tổng phần giảng: **120 phút**.

## Từng trang bài tập

| ID | Phút | Vai trò và sản phẩm hiển thị | Đáp án trong notes | Nguồn |
|---|---:|---|---|---|
| R00 | 0 | Mở phần; nêu ba sản phẩm nhóm. | không áp dụng | MMDS Ch.3 |
| R01 | 4 | Dữ kiện Bài 3.4.4 và hợp đồng vào/ra. | tiêu chí khóa | tr.96 |
| R02 | 7 | Khung trống mapper/reducer công việc 1. | lời giải công việc 1, 3 điểm; va chạm mã băm không là mục chấm riêng | tr.96 |
| R03 | 7 | Khung trống bộ ánh xạ/bộ giảm của công việc 2. | lời giải công việc 2, 3 điểm | tr.96 |
| R04 | 7 | Bảng kiểm trống và sản phẩm thiết kế hai job. | bốn điều kiện đúng, 4 điểm | tr.96 |
| R05 | 7 | Dữ kiện Bài 3.6.1; khung (a),(b). | hai hàm xác suất, 4 điểm | tr.108 |
| R06 | 8 | Khung (c),(d), giữ đúng yêu cầu tính của nguồn. | hai hàm, 6 điểm | tr.108 |
| R07 | 5 | Dữ kiện mô hình Bài 3.8.2 và bảng trống xác suất cơ sở. | $.004096,.000064$, 2 điểm | tr.121–122 |
| R08 | 7 | Bảng trống phương án OR 2048. | TP/FN/FP, 4 điểm | tr.121–122 |
| R09 | 8 | Bảng trống phương án AND của hai nhóm OR 1024 và lựa chọn. | TP/FN/FP + so sánh, 4 điểm | tr.121–122 |

Tổng recitation: **60 phút**. Mặt trang không lộ kết quả; toàn bộ số, lời giải và rubric ở ghi chú.
