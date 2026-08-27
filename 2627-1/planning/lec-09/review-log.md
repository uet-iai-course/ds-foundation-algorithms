# Nhật ký rà soát Bài 9

## Quyết định nguồn và sai khác có chủ ý

- Dùng MMDS sách làm nguồn chuẩn cho FM, AMS, DGIM và cửa sổ suy giảm; dùng slide MMDS để chọn nhịp và hình cần vẽ lại.
- So sánh với Stanford CS246 theo từng cụm. Stanford 2017 diễn đạt thứ tự gộp FM rõ và đúng với sách, nên F05 dùng cách này. MMDS Streams 2 tr.25 và Stanford 2026 tr.44 đảo thứ tự; deck không theo hai trang đó.
- Không gọi $2^R$ là ước lượng không chệch. F04 ghi rõ vấn đề đuôi nặng theo MMDS tr.144.
- Count-Min Sketch không có trong phần MMDS được chọn. Dùng duy nhất tham số của UMass CS514 Lecture 10: $m=\lceil2k/\varepsilon\rceil$, sai số $\varepsilon n/k$, một hàng thành công với xác suất ít nhất $1/2$, và $t=\lceil\log_2(1/\delta)\rceil$ hàng. Không đưa dạng tham số chuẩn khác vào deck.
- Không dạy HyperLogLog chi tiết. Tệp UMass có tên HyperLogLog chỉ trình bày FM/LogLog, thiếu cơ chế chọn thanh ghi bằng tiền tố, trung bình điều hòa và hiệu chỉnh.
- Cửa sổ suy giảm chỉ trình bày một tổng và truy hồi; không phát triển thuật toán duy trì mọi phần tử phổ biến.
- X03 gọi đúng sản phẩm là bộ đếm hậu tố $c_i$; $X_i=9(2c_i-1)$ và trung bình 21 chỉ là phép tự kiểm trong ghi chú.
- X05 dùng hình tự chứa trạng thái của Hình 4.3, ghi rõ chiều cũ → mới và phần trái chưa xác định. Nếu đã có hai bucket kích thước 8, chuỗi gộp tiếp tục tạo bucket 16 và có thể lan lên mức cao hơn.

## Kiểm tra khi soạn

- Đã tự tính lại ba bảng đuôi Ex.4.4.1: ước lượng $1,16,16$.
- Đã tính lại Ex.4.5.1: tần suất $3,2,2,2$, $F_2=21$, $F_3=51$.
- Đã tính lại Ex.4.5.3: $c_i=[2,3,2,2,1,1,2,1,1]$; ước lượng có trung bình 21.
- Đã kiểm Hình 4.2: mọi bucket kết thúc ở bit 1; ranh giới $k=10$ nằm trước vị trí 16; $k=5$ cho 3 và $k=15$ cho 10 so với số thật 9.
- Đã kiểm bất biến DGIM, thứ tự gộp hai bucket cũ nhất, mốc phải của bucket mới hơn, cận sai số 50% và bộ nhớ $O(\log^2N)$ bit.
- Đã kiểm truy hồi $S_{t+1}=(1-c)S_t+a_{t+1}$ và không đồng nhất phân bố với cửa sổ cố định $1/c$ phần tử.
- Chín hình kỹ thuật đều là SVG tự vẽ, có `role="img"`, `title`, `desc`; HTML có văn bản thay thế. Không dùng raster.

## Hợp nhất kiểm định storyboard và bốn phản biện độc lập

| Mức độ | Trang chiếu | Vấn đề và bằng chứng | Quyết định chỉnh sửa |
|---|---|---|---|
| chặn bàn giao | X05 | Đề bài nhắc Hình 4.3 nhưng không cho trạng thái; phần trái không xác định nên một đáp án duy nhất là sai. | Thêm `dgim-cascade-exercise.svg`, chiều cũ → mới, đuôi $4,4,2,2,1$, nhánh cascade qua 8, 16 và cao hơn. |
| nghiêm trọng | C01–C04 | Thiếu ví dụ số, cầu nối kỳ vọng–Markov–khuếch đại, giả thiết băm và chi phí; C03 trộn tham số không có nguồn cục bộ. | Dùng duy nhất tham số UMass; thêm $f_x=6$, nhiễu $3,1,5$, băm đôi một độc lập, hàng độc lập, chứng minh xác suất và $O(t)$/$O(mt)$. |
| nghiêm trọng | D02–D07, X04 | Hình DGIM cũ chia bucket sai, ranh giới 10 bit sai và hình bài tập lộ đáp án; truy vấn giả định biết đầu trái. | Vẽ lại Hình 4.2 theo mốc phải, tách SVG nền/truy vấn/bài tập; đặc tả tìm bucket cũ nhất có mốc phải trong hậu tố. |
| nghiêm trọng | M02–M07 | Hình thức hóa đi trước trực giác; nhánh hồ chứa thiếu trường hợp không thay nhưng khóa trùng. | Đưa vết hậu tố lên M02, ký hiệu sang M03; M07 có đủ ba nhánh và chi phí theo $q$. |
| trung bình | F01–F06 | Thiếu mô hình băm, dòng rỗng, $\rho(0)$ và chi phí theo số bản sao. | Nêu băm đều, độc lập; quy ước băm $L$ bit, $\rho(0)=L$, dòng rỗng trả 0; lượng hóa $O(q)$. |
| trung bình | E00–E01 | Câu “cùng tổng $1/c$” sai với dòng hữu hạn; thiếu tình huống và bước kiểm tra. | Sửa tổng hữu hạn thành $(1-(1-c)^t)/c$, chỉ tiến tới $1/c$; thêm vé phim và kiểm tra suy ra truy hồi. |
| trung bình | P01–A00, T00 | A00 lặp bản đồ; bảng tổng hợp chưa có chi phí. | A00 phân biệt toàn dòng/gần đây; T00 thêm cập nhật và trạng thái. |
| trung bình | X03 | “Giá trị biến AMS” nhập nhằng giữa $c_i$ và $X_i$. | Mặt trang yêu cầu rõ $c_i$ và nói không cần tính $X_i$. |

### Tái rà độ chính xác

| Mức độ | Trang chiếu | Vấn đề và bằng chứng | Quyết định chỉnh sửa |
|---|---|---|---|
| nghiêm trọng | D08 | Ghi chú chỉ nêu sai số nửa bucket nhưng chưa chứng minh mẫu số $c$ đủ lớn để suy ra sai số tương đối 50%. | Đặt $s=\lvert b^*\rvert$, $A$ là tổng bucket mới hơn; dùng bất biến để có $A\ge s-1$, nên $c\ge A+1\ge s$; xét riêng ước lượng thấp và cao rồi chia cho $c$. |
| nhẹ | C02–C03 | Miền tham số, khởi tạo và hai mức độc lập của băm chưa hiện rõ trên mặt trang. | Thêm $n,k,\varepsilon,\delta$, $C=0$, họ băm độc lập đôi một trong từng hàng và độc lập giữa các hàng; C03 giữ cùng $m,t$ và sai số $\varepsilon n/k$. |

Đã rà lại hai trang lân cận quanh các đổi thứ tự A00, M02–M03 và D02–D03; kết quả ghi cuối storyboard. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` trong bốn báo cáo đã được xử lý. Các đề xuất nhẹ chỉ thay đổi phong cách không được áp dụng nếu làm tăng chữ hoặc tách thêm trang mà không tạo bước học tập mới.

## Tự kiểm biên tập sau chỉnh sửa

- `no-ai-slop/eval.md`: đạt. Nội dung không thêm số liệu ngoài nguồn; câu trực tiếp, không có lời dẫn rỗng, câu hỏi tu từ hay kết luận lặp. Các câu hỏi hiển thị đều là yêu cầu kiểm tra có sản phẩm cụ thể.
- `quill` theo quy trình rà sửa: đạt. Không có `quill.json` và không khởi tạo mới. Mạch FM, Count-Min, AMS và DGIM nối dữ kiện ví dụ sang ký hiệu, thuật toán, lập luận và chi phí; thuật ngữ `mốc thời gian`, `dòng chỉ tăng`, `khóa nặng` được dùng nhất quán.
- Tiêu đề và nhãn bố cục bằng tiếng Việt; chỉ giữ tên thuật toán, tên riêng và ký hiệu chuẩn bằng tiếng Anh.

## Kiểm định cuối

- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Máy chủ HTTP Python đã có sẵn tại cổng 8765 được dùng làm phương án thay thế; URL bài giảng trả `HTTP 200`.
- Chromium duyệt đủ 46 trang ở khung $1280\times720$ và $800\times600$: không có lỗi JavaScript, lỗi tải tài nguyên hoặc trang tràn khung.
- Ảnh tổng hợp và các trang có mật độ cao đã được xem trực tiếp. Lần xem đầu phát hiện các thẻ `.math` thiếu dấu phân cách KaTeX; đã sửa toàn bộ và render lại. Lần kiểm tra sau không còn lệnh TeX thô trên mặt trang.
- Kiểm tra tĩnh cuối: 46 `data-slide-id` duy nhất, 46 ghi chú diễn giả, cấu trúc `section` cân bằng, chín SVG đều tồn tại và có mô tả, không có ảnh raster hoặc tài nguyên mạng cốt lõi; `git diff --check` sạch.
- Dự án Codex Slides `20260827213434-b-i-9-d-ng-d-li-u-m-moment-v-c-a-s-unoi` lưu đủ tài liệu nguồn. `generated/outline.md` và `generated/brief.md` đã được cập nhật và đọc lại thành công. Bề mặt Browser của Codex Slides không khả dụng; dự án vẫn ở trạng thái nháp, 0 trang, và thao tác tải thêm Design File trả HTTP 500. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; kiểm tra trực quan được thực hiện trên bản RevealJS cục bộ bằng Chromium.
