# Storyboard Bài 5

## Bản đồ hành trình

| Cụm | Tình huống dữ liệu lớn | Vấn đề | Trực giác | Ví dụ | Hình thức | Thuật toán, lập luận đúng | Ứng dụng, chi phí | Kiểm tra | Thời lượng |
|---|---|---|---|---|---|---|---|---|---:|
| Mở bài | M00 | M01 | M02 | không áp dụng: cụm định hướng | M01 | không áp dụng | M03 | M03 | 8 phút, gồm P00–P01 và M00–M03 trong cùng một section |
| Shingling | M00 (dùng lại) | S00 | S04 | S02 | S01 | S03 | S05–S06 | S06 | 25 phút |
| Jaccard | M00 (dùng lại) | J02 | J02 | J03 | J00–J01 | J04 | J05 | J05 | 20 phút |
| MinHash lý tưởng | M00 (dùng lại) | H00 | H01 | H03 | H02,H04 | H05–H07 | H08–H09,G07 | H07,G07 | 35 phút |
| Chữ ký thực hành | M00 (dùng lại) | G00 | G02 | G04 | G01 | G03 | G05–G06 | G06 | 24 phút |
| Cầu nối | M00 | C00 | C02 | không áp dụng: trang tổng hợp | C01 | không áp dụng | C00 | C02 | 8 phút |

Ở cụm Jaccard, J02 vừa nêu vấn đề đo hai tập vừa dựng trực giác ba vùng; J05 vừa phân tích chi phí so sánh mọi cặp vừa kiểm tra giới hạn của biểu diễn. Hai trang này đảm nhiệm hai vai trong chu trình, không phải mục bị lặp.

Tình huống mở bài dùng $N=10^6$ tài liệu và $N(N-1)/2=499.999.500.000$ cặp. Con số này trở lại ở J05 và C00–C02 khi xác định phần còn thiếu là tạo ứng viên; G05 chỉ dùng tham số $N$ để phân tích kích thước chữ ký. Quy tắc chuẩn hóa S04 tạo chuỗi đầu vào cho Ví dụ 3.3 ở S02; dữ kiện đó truyền sang đặc tả S01 và bất biến S03. Ba vùng ở J02 truyền sang Ví dụ 3.1, công thức J00 và chứng minh H05–H07. G02 giới thiệu $SIG$ là bảng đang cập nhật; ma trận Hình 3.4 xuất hiện ở G04, rồi được hình thức hóa bởi G01 và bất biến G03; cùng dữ kiện trở lại ở R03–R04. Trang M00 không thuộc mọi mạch: nó nằm trong section mở bài và dữ kiện của nó được dùng lại ở các mạch sau. Toàn bộ deck có 7 section ngoài: mở bài (P00–P01, M00–M03), Shingling, Jaccard, MinHash lý tưởng, Chữ ký thực hành, Cầu nối và recitation. G07 là trang cầu thuộc cụm MinHash lý tưởng, kết thúc mạch đó trước khi sang quét thực hành.

## Bảng trang chiếu phần giảng

| Mã | Luận điểm trung tâm | Nguồn | Thời lượng |
|---|---|---|---:|
| P00 | Vị trí của bài trong mạch tương đồng | `source.md`, Bài 5; MMDS Ch.3 | 0 |
| P01 | Năm sản phẩm học tập và tiên quyết | `source.md`, Bài 5 | 2 |
| M00 | Một triệu tài liệu tạo gần năm trăm tỷ cặp | MMDS slide 15, 24; Stanford 03 tr.14 đối chiếu | 3 |
| M01 | Bài 5 nén biểu diễn, chưa giảm số cặp | MMDS tr.73–74 | 1 |
| M02 | Luồng biểu diễn: tài liệu → shingle → chữ ký; $D_i\to C_i\to\sigma(C_i)$; Jaccard là phép so sánh | MMDS tr.73–74 | 1 |
| M03 | Ba bài toán biểu diễn, đo và nén | Tổng hợp từ MMDS §§3.1–3.3 | 1 |
| S00 | Shingle giữ dấu vết cụm từ chung | MMDS tr.78 | 2 |
| S04 | Chuẩn hóa khoảng trắng làm đổi biểu diễn | MMDS Ví dụ 3.4 | 3 |
| S02 | Quét tay Ví dụ 3.3 và loại bản lặp | MMDS Ví dụ 3.3 | 4 |
| S01 | Đặc tả $S_k(D)$ và trường hợp $k>n$ | MMDS §3.2.1 | 4 |
| S03 | Quét một lượt đúng nhờ bất biến; tạo trực tiếp tốn $\Theta(1+k\max(0,n-k+1))$ | MMDS §3.2.1; đặc tả bổ sung | 4 |
| S05 | $k$ phải đủ lớn để phân biệt | MMDS §3.2.2 | 4 |
| S06 | Băm 9-shingle khác với dùng 4-shingle | MMDS §3.2.3 | 4 |
| J02 | Chỉ vùng X và Y quyết định tỷ lệ | MMDS §§3.1.1, 3.3.3 | 3 |
| J03 | Ví dụ 3.1 có ba phần tử trong giao, tám trong hợp | MMDS Ví dụ 3.1 | 4 |
| J00 | Jaccard gọi tên tỷ lệ giao trên hợp | MMDS §3.1.1 | 3 |
| J01 | Hợp rỗng trả “không xác định” | MMDS §3.1.1; trường hợp biên bổ sung | 3 |
| J04 | Ba nhánh loại trừ tính Jaccard; cận trường hợp xấu nhất tuyến tính | Đặc tả cài đặt từ định nghĩa | 4 |
| J05 | Tính mỗi cặp nhanh vẫn còn $\Theta(N^2)$ cặp | MMDS ghi chú tr.81 | 3 |
| H00 | MinHash chọn phần tử sớm nhất theo thứ tự ngẫu nhiên | MMDS slide 32–35; Stanford 03 tr.26–27 đối chiếu | 2 |
| H01 | Ma trận đặc trưng là mô hình, không phải lưu trữ bắt buộc | MMDS §3.3.1 | 3 |
| H03 | Ví dụ 3.7 cho bốn giá trị MinHash | MMDS Ví dụ 3.7 | 4 |
| H02 | MinHash lý tưởng cần vũ trụ hữu hạn, tập không rỗng và hoán vị | MMDS §3.3.2; Stanford 03 tr.28 cho quy ước nhãn/hạng | 3 |
| H04 | Mệnh đề xác suất cần hoán vị đều | MMDS §3.3.3 | 3 |
| H05 | Bỏ hàng Z, giữ X và Y | MMDS §3.3.3 | 3 |
| H06 | Phần tử đầu trong hợp phân bố đều | MMDS §3.3.3 | 4 |
| H07 | Hàng X tương đương hai MinHash trùng | MMDS §3.3.3 | 3 |
| H08 | $p$ hoán vị độc lập tạo chữ ký | MMDS §3.3.4 | 3 |
| H09 | Số hàng trùng có kỳ vọng $pJ$; tỷ lệ có kỳ vọng $J$ | MMDS §3.3.4, sửa đơn vị | 4 |
| G07 | Tăng $p$ giảm phương sai nhưng tăng chi phí | Suy ra từ Bernoulli độc lập | 3 |
| G00 | Thực hành quét mã băm thay vì hoán vị ma trận | MMDS §3.3.5 | 2 |
| G02 | Chỉ phần tử 1 có thể hạ ô $SIG[i,c]$ của bảng chữ ký đang cập nhật | MMDS §3.3.5 | 3 |
| G04 | Ví dụ 3.8 chạy các cập nhật $SIG$ trước khi đặc tả đầy đủ | MMDS Ví dụ 3.8 | 5 |
| G01 | Đặc tả luồng thưa nhóm theo hàng và miền mã $0..u-1$ | MMDS §3.3.5 | 3 |
| G03 | Phép lấy min duy trì bất biến; cột toàn $\infty$ bị đánh dấu không hợp lệ | MMDS §3.3.5 | 4 |
| G05 | Chi phí $O(pu+pz)$ dưới giả thiết $O(1)$; bộ nhớ $\Theta(pN\log(u+1))$ bit | Phân tích từ giả mã | 4 |
| G06 | Va chạm làm mất bảo đảm chính xác của mô hình lý tưởng | MMDS §3.3.5 | 3 |
| C00 | MinHash chưa chọn ứng viên | MMDS chuyển §3.3→§3.4 | 3 |
| C01 | Bốn điều kiện cần ghi để tái lập kết quả | Tổng hợp giả thiết | 3 |
| C02 | Bài 6 thêm LSH vào sau chữ ký | MMDS §3.4 | 2 |
| **Tổng** |  |  | **120** |

## Phần bài tập dọc

| Mã | Bài nguồn và sản phẩm | Thời lượng |
|---|---|---:|
| R00 | Giao nhiệm vụ và quy tắc nộp | 0 |
| R01 | Bài tập 3.1.1: ba giao, ba hợp, ba tỷ số | 15 |
| R02 | Bài tập 3.2.3: công thức, biên, chứng minh đạt cận | 10 |
| R03 | Bài tập 3.3.2: tính hai hàm băm và lập hai hàng chữ ký | 7 |
| R04 | Bài tập 3.3.2: hoàn tất bảng chữ ký và trình bày kết quả | 8 |
| R05 | Bài tập 3.3.3: ma trận sáu hàng | 4 |
| R06 | Bài tập 3.3.3: ba yêu cầu và sản phẩm | 4 |
| R07 | Bài tập 3.3.3: bảng chữ ký trống và kiểm tra hoán vị | 6 |
| R08 | Bài tập 3.3.3: bảng sáu cặp trống và giải thích sai lệch | 6 |
| **Tổng** |  | **60** |

R00–R08 là một phần dọc riêng sau phần giảng. Lời giải và hướng dẫn chấm chỉ nằm trong ghi chú diễn giả. Dữ kiện được chép nguyên từ MMDS; việc tách mỗi bài thành trang dữ kiện và trang chữa không đổi yêu cầu toán học.

## Câu nối

- M03 → S00: biểu diễn chuỗi thành tập trước khi chọn độ đo.
- S00 → S04 → S02: chốt chuỗi đầu vào rồi mới quét tay cửa sổ.
- S02 → S01 → S03: ví dụ cung cấp dữ kiện cho đặc tả và bất biến.
- S03 → S05: sau khi biết chi phí quét một lượt, chọn $k$ để shingle đủ phân biệt trước khi băm.
- S06 → J02 → J03 → J00: quan sát phần chung, chạy ví dụ rồi gọi tên công thức.
- S06 → J02: đã có tập shingle cho từng tài liệu; giờ đo hai tập giống nhau đến đâu.
- J01 → J04: quy ước hợp rỗng trả “không xác định” được cài thành nhánh cuối của thuật toán J04.
- J04 → J05: tính một cặp trên danh sách sắp tốn tuyến tính; nhân với $\binom N2$ cặp vẫn quá tải.
- J05 → H00: nén mỗi tập để so một cặp mà không đọc toàn bộ shingle.
- H01 → H03 → H02: nhìn ma trận và chạy tay trước khi đặc tả MinHash.
- H09 → G07 → G00: chốt sai số của mô hình lý tưởng rồi chuyển sang cách quét thực hành.
- G00 → G02 → G04 → G01 → G03: quan sát cập nhật và vết chạy trước khi đặc tả, giả mã và bất biến.
- G06 → C00: chữ ký nhỏ chưa loại được số cặp bậc hai.

## Bản đồ chủ đề cho ghi chú tự học

| `note-topic-id` | Vai trò và kết nối vào–ra | Kiến thức đầu vào | Sản phẩm học tập | Thành phần trình bày |
|---|---|---|---|---|
| `L05-N01` | Nhận tình huống kho gần trùng; cấp bài toán biểu diễn cho `L05-N02` | phép đếm cặp, ký hiệu $N$ | tính số cặp và phân biệt nén biểu diễn với tạo ứng viên | vai trò, đặc tả, ví dụ quy mô, chi phí, kiểm tra; định lý/chứng minh không áp dụng |
| `L05-N02` | Nhận tài liệu thô; trao tập shingle cho `L05-N03` | chuỗi, tập hợp, hàm băm | đặc tả và tạo $S_k(D)$; xử lý biên và va chạm | đủ chuỗi; lập luận bất biến thay cho chứng minh định lý |
| `L05-N03` | Nhận hai tập shingle; trao phép so sánh chính xác cho `L05-N04` | giao, hợp, danh sách sắp | tính Jaccard và thuật toán hai con trỏ | đủ chuỗi, gồm quy ước hợp rỗng và bất biến thuật toán |
| `L05-N04` | Nhận độ đo Jaccard; trao một phép thử không chệch cho `L05-N05` | xác suất đều, ma trận 0/1 | chạy MinHash và chứng minh định lý | đủ chuỗi, dùng X/Y/Z trong chứng minh |
| `L05-N05` | Nhận một phép thử; trao chữ ký $p$ hàng cho `L05-N06` | Bernoulli, kỳ vọng, phương sai, độc lập | suy ra kỳ vọng, phương sai và đánh đổi theo $p$ | đủ chuỗi, ví dụ gắn với hai cột chữ ký |
| `L05-N06` | Nhận chữ ký lý tưởng; trao cách tính thực hành cho `L05-N07` | dữ liệu thưa, phép lấy min | chạy Ví dụ 3.8, giả mã, bất biến, dừng và chi phí | đủ chuỗi; cột toàn $\infty$ là trường hợp biên |
| `L05-N07` | Nhận cách tính thực hành; trao giới hạn và điều kiện dùng kết quả cho bài tập | va chạm băm, hoán vị | phân biệt bảo đảm lý tưởng với xấp xỉ thực hành | vai trò, đặc tả hai mô hình, phản ví dụ, kết luận có điều kiện, lỗi và kiểm tra; không có thuật toán mới |
| `L05-N08` | Nhận toàn bộ công cụ; chốt bài và nối sang Bài 06 | `L05-N02`–`L05-N07` | lời giải bốn bài nguồn và xác định phần còn thiếu là tạo ứng viên | đặc tả đề, vết tính, kết quả, lỗi; các thành phần khác gộp vào lời giải |

Ghi chú dùng chu trình riêng: sau vai trò và nhu cầu, đặt đặc tả trước ví dụ, rồi mới trực quan, mệnh đề/thuật toán, chứng minh và kiểm tra. Thứ tự này khác có chủ ý với deck, nơi trực giác và ví dụ thường đứng trước hình thức hóa.
