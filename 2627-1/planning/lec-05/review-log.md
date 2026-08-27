# Nhật ký rà soát Bài 5

## Nguồn và quyết định biên tập

- Phạm vi cốt lõi giữ ở MMDS 3e §§3.1–3.3. Lược Jaccard đa tập, shingle dựa trên từ và tối ưu chia khối hàng §§3.3.6–3.3.7 vì không cần cho chuẩn đầu ra và làm quá tải 120 phút. LSH, banding và các độ đo khoảng cách chuyển sang Bài 6 hoặc bài sau.
- MMDS là nguồn chính cho định nghĩa, ví dụ, chứng minh, thuật toán và bài tập.
- Mở bài M00 ưu tiên slide MMDS trang 15 và 24; Stanford CS246 `03-lsh.pdf`, trang 14 chỉ đối chiếu cách trình bày vì hai nguồn tương đương.
- Trực giác MinHash ưu tiên MMDS §3.3 và slide MMDS trang 32–35. Stanford trang 26–27 chỉ đối chiếu hình quét; trang 28 chỉ dùng xác nhận quy ước lưu nhãn hàng hoặc hạng trong hoán vị.
- Stanford `04-lsh_theory.pdf`, trang 3–7 chỉ dùng đối chiếu giả thiết và thuật ngữ; không lấy nội dung LSH.
- Dùng liên kết ghi công `http://www.mmds.org` trong ghi chú mở bài.

## Sai khác có chủ ý

- Bổ sung trường hợp $k>n$, tập shingle rỗng, điều kiện $C_1\cup C_2\ne\varnothing$ và cột rỗng. Các chi tiết này hoàn chỉnh đặc tả, không đổi định nghĩa nguồn.
- Dùng $p$ cho số hàng chữ ký, giữ $k$ cho độ dài shingle; dùng $u=|U|$ và $z$ cho số phần tử 1 để tránh xung đột ký hiệu.
- Sửa câu về kỳ vọng trong §3.3.4: số hàng trùng có kỳ vọng $pJ$; tỷ lệ hàng trùng có kỳ vọng $J$. Bản sách thiếu hệ số $p$ khi nói “expected number”.
- Tách rõ định lý cho hoán vị đều khỏi hàm băm thực hành. Va chạm có thể tạo trùng giả; Bài tập 3.3.3 được dùng để kiểm tra giới hạn này.
- Thuật toán Jaccard trên hai danh sách sắp và phân tích $O(pu+pz)$ được bổ sung từ định nghĩa để làm rõ chi phí; không thêm mệnh đề ngoài phạm vi.
- Sửa J04 thành ba nhánh loại trừ; hợp rỗng trả “không xác định”, không chia cho 0.
- Luồng M02 chỉ còn $D_i\to C_i\to\sigma(C_i)$; Jaccard và tỷ lệ hàng chữ ký trùng là phép so sánh, không phải đầu vào MinHash.
- Nêu $U$ hữu hạn, $u=|U|$. Cột chữ ký toàn $\infty$ bị đánh dấu không hợp lệ và không được tính $\infty=\infty$ là một hàng trùng.
- S03 ghi chi phí gồm kiểm tra biên là $\Theta(1+k\max(0,n-k+1))$, khả năng dùng băm lăn hoặc mã định danh và bộ nhớ theo số shingle phân biệt.
- G02 giới thiệu $SIG$ là bảng chữ ký đang cập nhật trước vết chạy G04; G01 mới đặc tả đầy đủ, nên không phải đảo lại thứ tự.
- G01/G03 yêu cầu danh sách thưa nhóm theo hàng hoặc luồng có mốc đổi hàng, với miền mã $0,\ldots,u-1$. G05 ghi $O(pu+pz)$ dưới giả thiết thao tác $O(1)$ và $\Theta(pN\log(u+1))$ bit cho $u$ mã cùng dấu canh $\infty$.
- Không dùng số liệu Ví dụ 3.10 vì ví dụ đó thuộc §3.4, ngoài phạm vi cốt lõi.
- Đổi thứ tự để trực giác và ví dụ đứng trước hình thức: `S00→S04→S02→S01→S03→S05→S06`; `J02→J03→J00→J01→J04→J05`; `H00→H01→H03→H02→H04→H05→H06→H07→H08→H09→G07`; `G00→G02→G04→G01→G03→G05→G06`. Đã rà lại câu nối và hai trang lân cận mỗi phía.

## Bài tập

- Giữ nguyên dữ kiện và yêu cầu của Bài tập 3.1.1, 3.2.3, 3.3.2 và 3.3.3.
- Chỉ dịch sang tiếng Việt, chép lại ma trận để bài tự đủ dữ kiện và tách trang giao bài khỏi trang chữa.
- J03 phần giảng dùng Ví dụ 3.1 với kết quả $3/8$, không dùng dữ kiện Bài tập 3.1.1.
- R04, R07 và R08 chỉ hiển thị bảng làm việc trống. Lời giải, phân bổ thời gian và hướng dẫn chấm nằm trong ghi chú diễn giả; tổng 60 phút.
- R03–R04 giữ đúng yêu cầu Bài tập 3.3.2: tính hai hàm và thêm hai hàng chữ ký; đã bỏ yêu cầu cùng điểm chấm kiểm tra hoán vị.
- R02 bổ sung lập luận đạt cận bằng một đoạn chuỗi de Bruijn có các cửa sổ độ dài $k$ khác nhau.
- R07–R08 giải thích hai nguyên nhân: $h_1,h_2$ có va chạm và bộ ba hàm không được lấy độc lập–đều từ họ mọi hoán vị.

## Tài sản và ngoại lệ

- Năm hình được vẽ lại thành SVG trong `2627-1/img/lec-05/`.
- Không dùng ảnh raster, phông chữ mạng, thư viện mạng hoặc tài sản nhị phân của MMDS/Stanford trong đầu ra.
- Không có ngoại lệ raster cần người dùng duyệt.

## Tự kiểm bản soạn

- [x] Tiêu đề và nhãn hiển thị thuần Việt; giữ Shingling, MinHash, Jaccard là tên thuật ngữ chuẩn.
- [x] Mỗi thuật toán có đầu vào, đầu ra, điều kiện biên, giả mã hoặc phép cập nhật, bất biến và chi phí.
- [x] Định lý MinHash nêu hoán vị đều; chữ ký lý tưởng nêu tính độc lập.
- [x] Không đồng nhất bảo đảm lý tưởng với hàm băm có va chạm.
- [x] Bài tập lấy trực tiếp từ giáo trình.
- [x] Không lộ đáp án recitation trên mặt trang; sản phẩm R03 được ghi rõ.
- [x] Bảng và khối mã chính đạt ít nhất khoảng `0.75em` hiệu dụng (`.82×.92` trở lên).
- [x] Văn bản đã tự kiểm theo `no-ai-slop/eval.md`: bỏ lời dẫn rỗng, câu hỏi tu từ, kết luận phô trương và nhịp câu máy móc.
- [x] Mạch đã rà theo Quill: ví dụ đứng trước đặc tả; dữ kiện được truyền theo S02→S01→S03, J02→J03→J00→H05–H07 và G04→G01→G03.
- [x] H02 dùng $r$ làm biến lấy `argmin`, không trùng $u=|U|$; J04 ghi rõ cận trường hợp xấu nhất.

## Kiểm định storyboard và bốn báo cáo độc lập

Kiểm định storyboard đã rà đủ 49 trang, quan hệ trước–sau, câu nối, thời lượng và phần bài tập. Bốn báo cáo độc lập đã hoàn tất trước vòng chỉnh sửa:

| Góc rà soát | Trọng tâm | Kết quả sau chỉnh sửa |
|---|---|---|
| Sinh viên | Tiên quyết, tải nhận thức, khả năng đọc, ví dụ chạy tay và recitation | Đã xử lý lỗi lộ đáp án, cỡ bảng và thứ tự trực giác–ví dụ–hình thức. |
| Chuyên gia giải thuật và khoa học dữ liệu | Độ bao phủ, chiều sâu, thuật ngữ, chi phí và phạm vi 120 phút | Đã khóa phạm vi §§3.1–3.3, thời lượng 120 phút và mô hình đầu vào thưa. |
| Độ chính xác toán học và thuật toán | Miền, trường hợp biên, giả thiết ngẫu nhiên, kết quả số và độ phức tạp | Đã sửa J04, $U$ hữu hạn, cột rỗng, cận chi phí và yêu cầu Bài tập 3.3.2. |
| Phản biện học thuật và giảng dạy | Chu trình học tập, vị trí công thức, thuật toán, chứng minh và cầu nối | Đã sắp lại bốn chu trình và sửa luồng dữ liệu ở M02. |

Các lỗi `chặn bàn giao` và `nghiêm trọng` đã được xử lý:

- J04 dùng ba nhánh loại trừ, trả “không xác định” khi hợp rỗng và ghi cận trường hợp xấu nhất.
- J03 dùng Ví dụ 3.1; R04, R07 và R08 không lộ đáp án trên mặt trang.
- Thứ tự Shingle, Jaccard, MinHash và quét thực hành đi từ trực giác, ví dụ đến hình thức và thuật toán.
- M02 biểu diễn đúng $D_i\to C_i\to\sigma(C_i)$; Jaccard là phép so sánh.
- $U$ được nêu hữu hạn, $u=|U|$; cột toàn $\infty$ không hợp lệ để ước lượng.
- Phần giảng đủ 120 phút và recitation đủ 60 phút.
- Bảng và khối mã chính đạt cỡ chữ hiệu dụng tối thiểu; không còn bảng quá nhỏ.
- S03, G01, G03 và G05 nêu đúng chi phí, miền mã và giả thiết đầu vào thưa nhóm theo hàng.
- R03–R04 giữ đúng yêu cầu Bài tập 3.3.2: tính hai hàm và thêm hai hàng chữ ký, không thêm yêu cầu kiểm tra hoán vị.

Tái kiểm toán sau chỉnh sửa không còn lỗi `chặn bàn giao`, `nghiêm trọng` hoặc `trung bình`.

## Kiểm thử và giới hạn công cụ

- Đã kiểm 49 mã trang duy nhất, 49 ghi chú, thứ tự khớp storyboard, năm SVG hợp lệ, không có ảnh raster hay phụ thuộc mạng cốt lõi, và `git diff --check` sạch.
- `python3 -m reloadserver 8765` không chạy được vì môi trường thiếu mô-đun `reloadserver`.
- Máy chủ thay thế `python3 -m http.server 8765` đã chạy với quyền được duyệt.
- Chromium và Playwright đã duyệt đủ 49 trang ở khung $1280\times720$ và $800\times600$: không có lỗi console, lỗi request hoặc tràn nội dung.
- Đã xem contact sheet và kiểm tra riêng các trang G04, R05 và R08.
- Dự án Codex Slides có mã `20260827173151-b-i-5-bi-u-di-n-t-ng-ng-shingling-v-minh-3rca`; dàn ý cuối và bản tóm tắt đã được ghi rồi đọc lại thành công.
- Tải HTML, SVG và các tệp planning lên Codex Slides trả HTTP 500; Browser trong trình soạn thảo không khả dụng. Vì vậy, nhật ký không tuyên bố đã rà trực quan bằng Codex Slides. Kiểm định trực quan nêu trên được thực hiện bằng Chromium và Playwright cục bộ.
