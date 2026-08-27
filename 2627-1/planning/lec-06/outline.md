# Bài 6: Tìm cặp tương đồng bằng LSH

## Mục tiêu và phạm vi

Sau buổi học, sinh viên có thể:

- giải thích vì sao quét mọi cặp không phù hợp ở quy mô của MMDS Ví dụ 3.10;
- thiết kế phép phân dải trên chữ ký MinHash, tính xác suất cặp trở thành ứng viên và chọn $b,r$;
- đặc tả thuật toán tạo ứng viên, bất biến, chi phí thời gian, bộ nhớ và đối chiếu hậu kỳ;
- phát biểu đúng họ băm nhạy cảm cục bộ (LSH), khuếch đại AND/OR và áp dụng cho Hamming, cosin, Euclid;
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

| Cụm | Trang | Phút | Sản phẩm học tập |
|---|---:|---:|---|
| Mở bài, mục tiêu và chữ ký đầu vào | P00–M02 | 12 | nhận diện nút thắt $\binom N2$ và hành trình lọc–định lượng–đối chiếu |
| Phân dải | B00–B06 | 23 | tạo khóa dải đầy đủ và ứng viên |
| Xác suất và ngưỡng | Q00–Q06 | 21 | suy ra $q(s)$, $s_{1/2}$ và chọn $b,r$ |
| Thuật toán tạo ứng viên | A00–A05 | 20 | trực giác, vết chạy, đặc tả, bất biến, chi phí và bộ nhớ |
| Họ LSH và khuếch đại | F00–F05 | 18 | phát biểu họ LSH và phân biệt AND/OR |
| Ba độ đo | D00–D04 | 16 | chọn họ băm đúng cho Hamming, cosin, Euclid |
| Vân tay | V00–V01 | 8 | nhận diện hai tầng khuếch đại trong mô hình nguồn |
| Kết luận | C00 | 2 | nối ứng viên với đối chiếu và Bài 7 |

## Bài tập — 60 phút

| Nguồn trực tiếp | Trang | Phút | Điều chỉnh |
|---|---:|---:|---|
| MMDS Bài tập 3.4.4, tr. 96 | R01–R04 | 25 | dịch, chia bước; giữ nguyên hai công việc MapReduce |
| MMDS Bài tập 3.6.1, tr. 108 | R05–R06 | 15 | dịch, bảng công thức để trống |
| MMDS Bài tập 3.8.2, tr. 121–122 | R07–R09 | 20 | dịch, tách dữ kiện và hai phương án; không đổi số |

R00 chỉ mở phần, không tính thời lượng. Đáp án và hướng dẫn chấm chỉ nằm trong ghi chú diễn giả.

## Ánh xạ nguồn

| Cụm đích | Nguồn chính | Quyết định |
|---|---|---|
| P01–Q06 | MMDS sách tr. 92–96; slide MMDS tr. 40–59 | giữ ví dụ, phân dải và công thức; sửa lỗi slide ghi $0.3\%$ thành $0.3=30\%$; thay xấp xỉ ngưỡng bằng dạng có $\ln 2$ |
| A00–A05 | MMDS §§3.4.1, 3.4.3; Bài tập 3.4.4 | đặt luồng và vết chạy trước đặc tả; tách bất biến giai đoạn sinh cặp; nêu chi phí, bộ nhớ và đối chiếu nhưng giữ thiết kế hai công việc cho recitation |
| F00–F05 | Stanford CS246 04, cụm LSH/khuếch đại; kiểm chứng MMDS §§3.6.1–3.6.3 | dùng cách trình bày phân tầng của Stanford; thêm MMDS Ví dụ 3.18 trước định nghĩa; dùng $\rho$ cho xác suất; không phát biểu vùng giữa hoặc lộ chuỗi của Bài tập 3.6.1 |
| D00–D04 | MMDS §§3.7.1–3.7.2, 3.7.4–3.7.5; Stanford CS246 04; Datar et al. 2004 | giữ Hamming; nêu điều kiện chính xác của siêu phẳng cosin; dùng $u\sim U[0,a)$ và phát biểu xác suất Euclid có điều kiện theo hướng chiếu |
| V00–V01 | MMDS §§3.8.4–3.8.5 | giữ mô hình, tách ngăn “có” và ngăn đơn “không”; chỉ nêu hướng đánh đổi, dành phép tính cho Bài tập 3.8.2 |
| R01–R09 | MMDS Bài tập 3.4.4, 3.6.1, 3.8.2 | giữ dữ kiện và yêu cầu; chỉ chia nhỏ, đáp án ở notes |

Slide Stanford được dùng ở F00–F05 vì cách dựng từ họ băm cơ sở đến AND/OR rõ hơn slide MMDS; mọi mệnh đề được đối chiếu sách. MMDS vẫn là nguồn chính cho phân dải, độ đo và vân tay. Công thức có độ dịch của họ Euclid được đối chiếu Datar et al., “Locality-Sensitive Hashing Scheme Based on p-Stable Distributions”, 2004, DOI `10.1145/997817.997857`.

## Kiểm kê hình

Mười SVG vẽ lại: quy mô Ví dụ 3.10, chia dải, khóa dải đầy đủ, đường xác suất, luồng ứng viên, AND/OR, miền bảo đảm họ LSH, siêu phẳng cosin, Euclid có độ dịch ngẫu nhiên và mô hình vân tay. Không dùng ảnh raster.
