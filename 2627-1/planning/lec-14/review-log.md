# Nhật ký rà soát Bài 14

## Trạng thái chỉnh sửa

- Giữ 49 trang giảng và 9 trang recitation, tương ứng 120 + 60 phút.
- Chỉ sửa HTML, SVG và ba tệp planning của Bài 14.
- Không sửa `index.html`, CSS/RevealJS dùng chung, bài khác, nguồn, hoặc lịch sử Git.

## Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | I09–I12, X01–X03 | Phần giảng giải trước Bài 31.2 nên recitation không còn là hoạt động thiết kế | I09–I12 cũ có đặc tả, heap, giả mã, bất biến và chi phí giống X01–X03 | Dành 31.2 cho recitation; dùng I09–I12 cho vị trí/tần suất, precision/recall |
| nghiêm trọng | K03–K06 | Ví dụ xuất hiện sau hình thức và không có số | K06 cũ chỉ dùng $p^*,b,\tau$ tượng trưng | Đưa K06 trước K04–K05 và dùng một vết tọa độ nhất quán |
| nghiêm trọng | B01–B03 | Công thức đến trước ví dụ; thiếu giả mã truy vấn | B01 cũ nêu LB trước dữ kiện, B03 chỉ đặc tả nút | Đưa B02 trước B01; dùng B03 cho giả mã truy vấn đầy đủ |
| trung bình | R00–R03 | Thuật toán đến trước ví dụ và trộn lọc với kiểm hình thật | R01 cũ xuất hình thật ngay tại lá | Đổi thành R00→R02→R01→R03; tách gom ứng viên và tinh lọc |

## Báo cáo độc lập 1: Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | Z01–Z03 | Hình, công thức và tập mã vùng không nhất quán | Công thức cho (1,4)→6 và (2,3)→7; hình cũ đặt ngược, Z03 dùng 6 | Sửa đủ 16 ô và tập vùng thành {4,7,10,13}; ghi sai khác Auburn |
| nghiêm trọng | K00–K09 | Không có vết chạy tay có tọa độ, khoảng cách và thứ tự thăm | K06 cũ chỉ có nhãn tượng trưng | Thêm $q,p,s,\tau,LB$ và thứ tự thăm/cắt |
| nghiêm trọng | B00–B07 | Không có vết số và thiếu thuật toán truy vấn có thể tự học | B02 cũ chỉ liệt kê ba bước; B03 cũ chỉ nêu nút | Thêm bảng số và giả mã xử lý lá, hòa, cập nhật trạng thái |
| nghiêm trọng | I09–I12, X01–X03 | Recitation lặp lời giải trên lớp | Cùng heap, bất biến và chi phí xuất hiện hai lần | Chuyển nội dung heap hoàn toàn sang X01–X03 |
| trung bình | P02, I01–I08, K00, X02 | Thuật ngữ tiếng Anh xuất hiện trước giải thích tiếng Việt | `posting`, `exact`, `heap` xuất hiện trên mặt trang | Dùng danh sách đảo, 1-NN chính xác, đống tối thiểu lần đầu |
| trung bình | X01–X03 | Đề chưa tự chứa trường hợp rỗng và $n=1$ | Thiếu miền của $n,k$, tính duy nhất docID và chi phí khởi tạo khi $T=0$ | Nêu $n\ge1$, $1\le k\le n$, danh sách rỗng, $T$, $O(n+T\log(n+1))$ |

## Báo cáo độc lập 2: Chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | K05 | Giả mã không khởi tạo và không nhận trạng thái trả về | Hai lời gọi đệ quy cũ không gán `(best,τ)` | Thêm `nearest`, xử lý lá và gán trạng thái ở cả hai nhánh |
| nghiêm trọng | B03, B07 | Thiếu thuật toán truy vấn và lẫn chi phí dựng với truy vấn | B03 cũ chỉ đặc tả nút; B07 chỉ nêu $O(N)$ | Dùng B03 cho truy vấn; B07 tách mô hình dựng và truy vấn |
| trung bình | S00, B00 | Tình huống dữ liệu lớn còn chung | Chỉ nói dữ liệu trên bộ nhớ phụ | Dùng ảnh vệ tinh/trạm xăng của Auburn và tập huấn luyện lớn của Cornell |
| trung bình | C00 | Trộn CPU, I/O và số ứng viên | Bảng cũ chỉ có một cột trường hợp xấu | Nêu riêng nút/trang, phép đo/CPU và số ứng viên; không bịa cận I/O |

## Báo cáo độc lập 3: Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | Z01–Z03 | Hoán vị 6/7 làm sai vết Morton | $z=1+\sum(2u_j+v_j)4^j$ cho ma trận khác hình nguồn ở hai ô | Giữ công thức chuẩn, sửa hình, tập mã và ghi lỗi nguồn |
| nghiêm trọng | R01 | Bước lọc tuyên bố xuất nghiệm trước khi kiểm hình | MBR giao Q chỉ là điều kiện cần | Chỉ gom ứng viên; thêm bước tinh lọc và chứng minh không bỏ nghiệm |
| nghiêm trọng | K04–K07 | Ký hiệu $N$ vừa là tập/số điểm/nút; chứng minh thiếu trạng thái hòa | Công thức cũ dùng $N$ ở nhiều vai trò | Dùng $n$ cho số điểm, $U$ cho nút; cắt với dấu `>` và giữ mọi hòa |
| nghiêm trọng | B02–B06 | Thiếu ca LB=$\tau$, lá, dừng và gán trạng thái sau đệ quy | Giả mã truy vấn không tồn tại | Bổ sung vết LB 2/3/2,5 và giả mã đầy đủ |
| trung bình | X06–X08 | Chứng minh Bài 25.3 phụ thuộc vùng tròn đóng nhưng đề không nói | Với vùng mở, điểm đúng bán kính có thể nằm ngoài A | Chốt vùng đóng và chứng minh dừng/đúng |

## Báo cáo độc lập 4: Học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | R00–R03 | Ví dụ đứng sau thuật toán | R01 cũ trước R02 | Đặt R02 trước R01 và giữ data-slide-id theo nội dung |
| nghiêm trọng | K03–K06, B01–B03 | Công thức/thuật toán đúng riêng lẻ nhưng thiếu cầu từ ví dụ | Không có dữ kiện truyền sang giả mã và chứng minh | Dùng cùng trạng thái qua ví dụ→hình thức→giả mã→đúng |
| nghiêm trọng | I09–I12 | Thứ tự làm mất nhiệm vụ khám phá của recitation | Lời giải 31.2 đã lộ trước bài tập | Thay bằng nội dung Ch31 về tìm kiếm toàn văn và đánh giá |
| trung bình | C02, X00 | Hai trang chuyển phần lặp chức năng | C02 cũ liệt kê đúng ba bài ở X00 | Biến C02 thành kiểm tra tổng hợp có sản phẩm cụ thể |

## Quyết định hợp nhất

- Đã xử lý toàn bộ mục chặn bàn giao và nghiêm trọng.
- Sửa Z-order theo công thức Morton; ma trận từ trên xuống là `6,8,14,16 / 5,7,13,15 / 2,4,10,12 / 1,3,9,11`.
- Đổi thứ tự R-tree, kd-tree và ball tree đúng chu trình ví dụ trước hình thức/giả mã.
- Loại toàn bộ lời giải Bài 31.2 khỏi phần giảng; recitation vẫn 30+10+20 phút.
- Làm rõ vùng tròn đóng, miền $n,k$, danh sách rỗng, docID duy nhất và trường hợp $n=1$.
- Không thêm slide mới vì 58 slide hiện có đủ chứa sửa đổi mà vẫn giữ thời lượng. Không thêm Hilbert, cận I/O R-tree hoặc số liệu quy mô vì nguồn không hỗ trợ.
- Không dùng lại `kofn-heap.svg` trong phần giảng; tệp vẫn thuộc bộ tài sản cũ nhưng HTML không tham chiếu. Không xóa để tránh một thao tác hủy không cần thiết.

## Ảnh hưởng của no-ai-slop và Quill

- `no-ai-slop`: đổi tiêu đề và câu hiển thị sang tiếng Việt trực tiếp; bỏ `exact`, `workload`, `posting` dùng thay thuật ngữ Việt; cắt câu dẫn và kết luận lặp; không thêm số liệu.
- `quill`: khóa ký hiệu $n,U,p,q,\delta,\tau,LB$; nối cùng dữ kiện qua ví dụ, giả mã và chứng minh; cập nhật câu nối giữa các cụm. Không tạo `quill.json`.

## Sai khác nguồn có chủ ý

- Slide Chương 31 trang 14 in OR thành giao; deck sửa thành hợp.
- Auburn PDF trang 13 đổi chỗ 6/7 so với công thức Morton; deck sửa hình và dùng {4,7,10,13}.
- Vết kd-tree và ball tree là dữ kiện nhỏ dựng từ cơ chế Cornell để chạy tay; ghi rõ trong notes và storyboard.
- Bài 25.2–25.3 dùng ấn bản 6 vì có Practice Exercises/Solutions chính thức; yêu cầu toán học không đổi.

## Giới hạn

- Không tuyên bố đã dùng Codex Slides Browser.
- Kiểm định trực quan bằng Browser và cập nhật `index.html` thuộc vòng điều phối cuối, không thuộc lượt chỉnh sửa này.

## Rà lại sau chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | X03 | Chi phí thiếu bước duyệt $n$ danh sách khi khởi tạo | Với $T=0$, biểu thức chỉ theo $T$ cho 0 dù vẫn phải kiểm tra $n$ danh sách | Dùng $O(n+T\log(n+1))$ và giải thích ca mọi danh sách rỗng |
| nghiêm trọng | B04–B06 | Phép dựng thiếu miền $S$, $\ell$, lựa chọn $x_0$ và lập luận hai nửa tiến triển | “Hai bước điểm xa” chưa xác định điểm đầu; tiến triển chưa suy ra nếu thiếu $\ell\ge1$ | Nêu $S$ hữu hạn, $\ell\ge1$, chọn $x_0\in S$, và chứng minh $|S|\ge2$ trước khi chia |
| trung bình | I08 | Quy tắc trộn chưa đủ ba quan hệ | Bảng cũ chỉ nêu trường hợp hai đầu bằng nhau và phần đuôi | Ghi rõ $<$, $=$, $>$ cho hợp và hiệu; nêu $S$ tăng nghiêm ngặt |
| trung bình | K08, C00 | Cận $O(n)$ chưa nói đơn vị và chi phí theo chiều | Một phép đo trên điểm $p$ chiều không phải chi phí hằng trong mô hình số học | Ghi $O(n)$ phép đo và $O(pn)$ phép toán số học |

Trạng thái: đã đóng cả bốn mục; HTML, outline và storyboard đã đồng bộ. Không đổi ID, thứ tự, số trang hoặc thời lượng.

## QA trực quan bằng Chromium

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | K05, B03 | Hai khối giả mã bị cắt dòng cuối trong hộp mã ở khung 1280×720 | Ảnh Chromium cho thấy phần cuối không hiện dù phần tử trang không báo tràn ngoài | Dùng lớp cục bộ `code-fit`, giữ cỡ chữ `0.84em` trong section `0.9em` (hiệu dụng `0.756em`), giảm line-height/lề/padding và bỏ max-height chỉ cho hai khối |

Trạng thái: đã sửa cục bộ K05 và B03; không đổi CSS chung hoặc kích thước chữ của slide khác.

Điều phối viên đã chạy lại Chromium sau sửa đổi `code-fit`:

- duyệt đủ 58 slide ở khung 1280×720 và 800×600;
- không có lỗi console hoặc lỗi trang, không có lỗi KaTeX và không có tràn nội dung;
- ảnh kiểm tra K05 và B03 cho thấy toàn bộ giả mã đã hiển thị trong hộp mã.

## Máy chủ cục bộ và giới hạn Codex Slides

- `python3 -m reloadserver 8765` thất bại vì môi trường không có mô-đun `reloadserver`.
- Máy chủ cục bộ hiện có đã trả HTTP 200 tại URL của bộ trang chiếu.
- Codex Slides Browser không khả dụng. `start-project` không chạy vì runtime yêu cầu bind `0.0.0.0:4311`, thao tác này bị môi trường chặn.
- Node hiện tại là 18.19.1, thấp hơn yêu cầu từ 20 trở lên; phiên bản manifest và runtime của plugin không khớp.
- Không tuyên bố đã rà bộ trang chiếu bằng Codex Slides.
