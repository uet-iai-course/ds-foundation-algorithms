# Bài 5: Biểu diễn tương đồng — Shingling và MinHash

## Mục tiêu và phạm vi

- Tạo tập $k$-shingle từ tài liệu đã chuẩn hóa.
- Tính và diễn giải độ tương đồng Jaccard.
- Chứng minh $\Pr[h_\pi(C_1)=h_\pi(C_2)]=J(C_1,C_2)$ khi $\pi$ là hoán vị đều.
- Lập chữ ký MinHash bằng một lượt quét ma trận thưa.
- Phân biệt hoán vị lý tưởng với hàm băm thực hành có va chạm.
- Phần giảng: 120 phút. Phần bài tập: 60 phút.
- Phạm vi cốt lõi: MMDS 3e, mục 3.1–3.3. Lược Jaccard đa tập, shingle dựa trên từ và các tối ưu chia khối hàng ở §§3.3.6–3.3.7 để giữ tải 120 phút. LSH, banding, khoảng cách tổng quát và nội dung từ §3.4 thuộc Bài 6 hoặc bài sau.

## Mạch khái niệm

1. Một triệu tài liệu tạo xấp xỉ $5\times10^{11}$ cặp.
2. Chốt chuẩn hóa, chạy tay cửa sổ rồi đặc tả và tạo tập shingle.
3. Dựng trực giác giao–hợp, chạy Ví dụ 3.1 rồi hình thức hóa Jaccard.
4. Dùng hoán vị đều để định nghĩa MinHash và chứng minh định lý xác suất.
5. Ghép $p$ phép thử độc lập thành chữ ký.
6. Chạy Ví dụ 3.8 trước khi đặc tả và chứng minh bất biến quét ma trận thưa; nêu rõ giới hạn do va chạm và họ hàm không độc lập–đều.
7. Chuyển sang bài toán giảm số cặp ứng viên bằng LSH ở Bài 6.

## So sánh nguồn theo cụm

| Cụm | Nguồn chọn | Lý do |
|---|---|---|
| Mở bài quy mô | Slide MMDS Chương 3, trang 15 và 24; Stanford CS246 `03-lsh.pdf`, trang 14 để đối chiếu | Hai nguồn tương đương; ưu tiên MMDS. Stanford chỉ giúp kiểm tra cách trình bày phép đếm cặp. M00 được dùng lại ở đầu các mạch sau, không lặp lại thành trang mới. |
| Shingling, Jaccard | MMDS 3e §§3.1–3.2; slide MMDS Chương 3 | Khớp chuẩn đầu ra, có ví dụ và bài tập trực tiếp. |
| Trực giác MinHash | MMDS §3.3 và slide MMDS trang 32–35; Stanford CS246 `03-lsh.pdf`, trang 26–27 để đối chiếu | MMDS khớp ví dụ và chứng minh. Stanford trang 28 chỉ dùng kiểm tra quy ước lưu nhãn hàng hay hạng. |
| Chữ ký và quét thưa | MMDS 3e §§3.3.4–3.3.5 | Có bất biến cập nhật và Hình 3.4 để chạy tay. |
| Đối chiếu | Stanford CS246 `04-lsh_theory.pdf`, trang 3–7 | Chỉ dùng kiểm tra thuật ngữ và giả thiết; không mở rộng sang LSH. |

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $N$ | số tài liệu |
| $D_i$ | tài liệu thứ $i$ |
| $k$ | độ dài shingle |
| $C_i=S_k(D_i)$ | tập shingle của $D_i$ |
| $U$, $u=|U|$ | vũ trụ hữu hạn của shingle và số hàng |
| $A$ | ma trận đặc trưng thưa |
| $p$ | số hàng chữ ký |
| $z$ | số phần tử 1 của $A$ |
| $\pi$, $h_\pi$ | hoán vị hàng và MinHash lý tưởng |
| $SIG$ | ma trận chữ ký $p\times N$; mỗi ô thuộc $\{0,\ldots,u-1\}\cup\{\infty\}$ và cột toàn $\infty$ không hợp lệ để ước lượng |

## Bài tập trực tiếp từ giáo trình

| Bài | Nội dung | Thời lượng |
|---|---|---:|
| 3.1.1 | Tính Jaccard cho ba tập | 15 phút |
| 3.2.3 | Cận lớn nhất của số $k$-shingle | 10 phút |
| 3.3.2 | Tính hai hàm băm và thêm đúng hai hàng chữ ký vào Hình 3.4 | 15 phút |
| 3.3.3 | Chữ ký, hoán vị và sai lệch trên Hình 3.6 | 20 phút |

## Tài sản SVG

- `quy-mo-so-sanh-cap.svg`: quy mô số cặp và chuỗi biểu diễn.
- `cua-so-shingle.svg`: Ví dụ 3.3.
- `jaccard-ba-vung.svg`: ba kiểu hàng X, Y, Z.
- `minhash-hoan-vi.svg`: Ví dụ 3.7.
- `quet-ma-tran-thua.svg`: cập nhật chữ ký trên phần tử 1.

## Bản đồ chủ đề ghi chú tự học

| `note-topic-id` | Nhãn | Chủ đề | Quyết định và nguồn |
|---|---|---|---|
| `L05-N01` | cầu nối | Quy mô so sánh cặp và vai trò của biểu diễn | giữ; MMDS §§3.1–3.3 và slide mở đầu |
| `L05-N02` | cốt lõi | Chuẩn hóa và Shingling | giữ; MMDS §§3.2.1–3.2.3, Ví dụ 3.3–3.4 |
| `L05-N03` | cốt lõi | Độ tương đồng Jaccard và hai con trỏ | giữ và bổ sung đặc tả; MMDS §3.1.1, Ví dụ 3.1 |
| `L05-N04` | cốt lõi | MinHash lý tưởng và định lý xác suất | giữ; MMDS §§3.3.1–3.3.3, Ví dụ 3.7 |
| `L05-N05` | cốt lõi | Chữ ký, kỳ vọng và phương sai | giữ và làm rõ đơn vị; MMDS §3.3.4 |
| `L05-N06` | cốt lõi | Quét ma trận thưa và bất biến | giữ; MMDS §3.3.5, Ví dụ 3.8 |
| `L05-N07` | cốt lõi | Giới hạn của hàm băm thực hành | tách riêng để không lẫn với định lý lý tưởng; MMDS §3.3.5 và Bài 3.3.3 |
| `L05-N08` | cầu nối | Bốn bài tập và nối sang LSH | giữ nguyên bốn đề nguồn; chỉ nhắc LSH như đầu ra cho Bài 06 |

Các bổ sung được duyệt là quy ước hợp rỗng/cột rỗng, thuật toán hai con trỏ và suy dẫn Bernoulli cho phương sai. Không thêm Jaccard distance, Jaccard đa tập, shingle theo từ, Hình 3.5, §§3.3.6–3.3.7 hoặc nội dung LSH.
