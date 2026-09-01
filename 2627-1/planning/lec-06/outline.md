# Bài 6: Tìm cặp tương đồng bằng LSH

## Mục tiêu và phạm vi

Sau buổi học, sinh viên có thể:

- giải thích vì sao quét mọi cặp không phù hợp ở quy mô của MMDS Ví dụ 3.10;
- thiết kế phép phân dải trên chữ ký MinHash, tính xác suất cặp trở thành ứng viên và chọn $b,r$;
- đặc tả thuật toán tạo ứng viên, bất biến, chi phí thời gian, bộ nhớ và đối chiếu hậu kỳ;
- phát biểu đúng họ băm nhạy cảm cục bộ (LSH), khuếch đại AND/OR, đồng thời giải thích và so sánh điều kiện của các họ Hamming, cosin, Euclid;
- phân tích mô hình băm vân tay trong MMDS và phân biệt số liệu mô hình với bằng chứng thực nghiệm.

Phần cốt lõi: MMDS §§3.4, 3.6–3.8. Không gồm HNSW, lượng tử hóa tích (PQ) hoặc nội dung Bài 7.

## Tiên quyết

- Bài 5: tập shingle, Jaccard, chữ ký MinHash và $Pr[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2)$.
- Xác suất biến cố độc lập, tích vô hướng, góc giữa hai vector, khoảng cách Hamming và Euclid.
- Mô hình MapReduce của Bài 2.

## Ký hiệu khóa

| Ký hiệu | Nghĩa |
|---|---|
| $N$ | số đối tượng hoặc cột chữ ký |
| $p=br$ | số hàng chữ ký; $b$ dải, mỗi dải $r$ hàng |
| $s$ | độ tương đồng thực của một cặp |
| $q(s)$ | xác suất cặp trở thành ứng viên |
| $\tau$ | ngưỡng đối chiếu hậu kỳ |
| $C$ | tập cặp ứng viên đã loại trùng |
| $A$ | số lượt sinh cặp trước loại trùng, $A=\sum_B\binom{|B|}{2}$ |
| $F$ | phân phối trên họ hàm băm |
| $\rho$ | xác suất va chạm cơ sở của một cặp cố định |
| $\alpha_1,\alpha_2$ | cận xác suất va chạm, $\alpha_1>\alpha_2$ |
| $d_1,d_2$ | ngưỡng gần và xa, $d_1<d_2$ |
| $m$ | số chiều của vector Hamming hoặc cosin |
| $u$ | độ dịch ngẫu nhiên của các ngăn Euclid, $u\sim U[0,a)$ |

## Mạch phần giảng — 120 phút

Sáu mạch giảng tương ứng sáu `<section>` ngoài. Bảng tách hai mạch ghép thành tám cụm nội dung để ghi rõ chức năng và kết nối vào–ra:

| Cụm | Trang | Phút | Chức năng và kết nối vào–ra |
|---|---:|---:|---|
| Mở bài (tình huống + bài toán) | P00–M02 | 12 | Vào từ Bài 5 (chữ ký MinHash); nêu nút thắt $\binom N2$ và bài toán đầu vào/đầu ra; ra vào mạch phân dải. |
| Phân dải | B00–B06 | 23 | Tạo khóa dải đầy đủ và tập ứng viên; vào từ bài toán lọc, ra vào mạch xác suất qua câu hỏi biên B06. |
| Xác suất và ngưỡng | Q00–Q06 | 21 | Suy ra $q(s)$, $s_{1/2}$ và quyết định hướng chọn $b,r$ khi $p$ cố định; vào từ điều kiện phân dải, ra vào mạch thuật toán qua chi phí ứng viên. |
| Thuật toán tạo ứng viên | A00–A05 | 20 | Trực giác, vết chạy, đặc tả, bất biến, chi phí và bộ nhớ; vào từ $q(s)$, ra vào mạch họ LSH khi cần ngôn ngữ chung. |
| Họ LSH và khuếch đại | F00–F05 | 18 | Phát biểu họ LSH và phân biệt AND/OR; vào từ phân dải MinHash, ra vào mạch ba độ đo. |
| Ba độ đo | D00–D04 | 16 | Giải thích và so sánh điều kiện của các họ Hamming, cosin, Euclid; vào từ định nghĩa họ LSH, ra vào ví dụ mô hình vân tay dùng phép ghép OR–AND. |
| Vân tay | V00–V01 | 8 | Nhận diện hai tầng khuếch đại trong mô hình nguồn; vào từ AND/OR, ra vào kết luận. |
| Kết luận | C00 | 2 | Gom ba quyết định thiết kế; vào từ toàn bộ mạch, ra sang Bài 7. |

Tổng phần giảng: **120 phút**.

## Bài tập — 60 phút

| Nguồn trực tiếp | Trang | Phút | Điều chỉnh |
|---|---:|---:|---|
| MMDS Bài tập 3.4.4, tr. 96 | R01–R04 | 25 | dịch, chia bước; giữ nguyên hai công việc MapReduce |
| MMDS Bài tập 3.6.1, tr. 108 | R05–R06 | 15 | dịch, bảng công thức để trống |
| MMDS Bài tập 3.8.2, tr. 121–122 | R07–R09 | 20 | dịch, tách dữ kiện và hai phương án; không đổi số |

R00 chỉ mở phần, không tính thời lượng; hướng dẫn nhóm làm bài trước rồi mới mở ghi chú đối chiếu. Đáp án và hướng dẫn chấm chỉ nằm trong ghi chú diễn giả.

## Ánh xạ nguồn

| Cụm đích | Nguồn chính | Quyết định |
|---|---|---|
| P01–Q06 | MMDS sách tr. 92–96; slide MMDS tr. 40–59 | giữ ví dụ, phân dải và công thức; sửa lỗi slide ghi $0.3\%$ thành $0.3=30\%$; chuyển khai triển ngưỡng có $\ln 2$ vào notes để Q06 tập trung vào quyết định $b,r$ |
| A00–A05 | MMDS §§3.4.1, 3.4.3; Bài tập 3.4.4 | đặt luồng và vết chạy trước đặc tả; tách bất biến giai đoạn sinh cặp; phân biệt bộ nhớ phụ trợ với lưu đầu vào, số bản ghi trung gian $bN+A$ với dung lượng $\Theta(pN+A)$, nhưng giữ thiết kế hai công việc cho recitation |
| F00–F05 | Stanford CS246 04, cụm LSH/khuếch đại; kiểm chứng MMDS §§3.6.1–3.6.3 | dùng cách trình bày phân tầng của Stanford; thêm MMDS Ví dụ 3.18 trước định nghĩa; dùng $\rho$ cho xác suất; không phát biểu vùng giữa hoặc lộ chuỗi của Bài tập 3.6.1 |
| D00–D04 | MMDS §§3.7.1–3.7.2, 3.7.4–3.7.5; Stanford CS246 04; Datar et al. 2004 | giữ Hamming; nêu điều kiện chính xác của siêu phẳng cosin; dùng $u\sim U[0,a)$ và phát biểu xác suất Euclid có điều kiện theo hướng chiếu |
| V00–V01 | MMDS §§3.8.4–3.8.5 | giữ mô hình, tách ngăn “có” và ngăn đơn “không”; chỉ nêu hướng đánh đổi, dành phép tính cho Bài tập 3.8.2 |
| R01–R09 | MMDS Bài tập 3.4.4, 3.6.1, 3.8.2 | giữ dữ kiện và yêu cầu; chỉ chia nhỏ, đáp án ở notes |

Slide Stanford được dùng ở F00–F05 vì cách dựng từ họ băm cơ sở đến AND/OR rõ hơn slide MMDS; mọi mệnh đề được đối chiếu sách. MMDS vẫn là nguồn chính cho phân dải, độ đo và vân tay. Công thức có độ dịch của họ Euclid được đối chiếu Datar et al., “Locality-Sensitive Hashing Scheme Based on p-Stable Distributions”, 2004, DOI `10.1145/997817.997857`.

## Kiểm kê hình

Mười SVG vẽ lại: quy mô Ví dụ 3.10, chia dải, khóa dải đầy đủ, đường xác suất, luồng ứng viên, AND/OR, miền bảo đảm họ LSH, siêu phẳng cosin, Euclid có độ dịch ngẫu nhiên và mô hình vân tay. Không dùng ảnh raster.

## Bản đồ chủ đề ghi chú tự học

| `note-topic-id` | Nhãn | Chủ đề | Nguồn chính | Sản phẩm học tập |
|---|---|---|---|---|
| `L06-N01` | cầu nối | Chữ ký ngắn nhưng số cặp vẫn lớn | Ví dụ 3.10 | tính quy mô và xác định nút thắt |
| `L06-N02` | cốt lõi | Phân dải và khóa đầy đủ | §§3.4.1–3.4.2 | tạo ngăn và tập ứng viên đúng |
| `L06-N03` | cốt lõi | Xác suất ứng viên và ngưỡng | §3.4.2, Ví dụ 3.11–3.12 | suy ra $q(s)$, $s_{1/2}$ và đánh đổi |
| `L06-N04` | cốt lõi | Thuật toán tạo ứng viên | §§3.4.1, 3.4.3; Bài 3.4.4 | giả mã, bất biến, dừng, chi phí và hậu kiểm |
| `L06-N05` | cốt lõi | Định nghĩa họ LSH | §§3.6.1–3.6.2 | phát biểu hai miền bảo đảm đúng |
| `L06-N06` | cốt lõi | Khuếch đại AND/OR | §3.6.3; Bài 3.6.1 | suy ra và ghép đúng công thức |
| `L06-N07` | cốt lõi | Họ Hamming | §3.7.1 | chứng minh xác suất va chạm |
| `L06-N08` | cốt lõi | Họ cosin | §3.7.2 | nối hình học góc với xác suất |
| `L06-N09` | cốt lõi | Họ Euclid | §§3.7.4–3.7.5; Datar et al. §3.2 | phân biệt hai xây dựng và điều kiện áp dụng |
| `L06-N10` | cốt lõi | Mô hình vân tay | §§3.8.4–3.8.5 | tính xác suất và giới hạn mô hình |
| `L06-N11` | cầu nối | Ba bài tập và tổng hợp | Bài 3.4.4, 3.6.1, 3.8.2 | lời giải truy nguyên được và tự kiểm |

Đồ thị tiên quyết: `L06-N01 → L06-N02 → L06-N03 → L06-N04 → L06-N05 → L06-N06`; từ `L06-N06` tỏa sang `L06-N07`, `L06-N08`, `L06-N09`, rồi hội tụ ở `L06-N10 → L06-N11`. Ba phần bổ sung được giữ là kiểm khóa đầy đủ, mô hình chi phí bản ghi/từ và phép chiếu–dịch Euclid có nguồn. Không thêm nội dung của Bài 07.
