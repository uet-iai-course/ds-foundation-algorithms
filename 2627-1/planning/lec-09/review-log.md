# Nhật ký rà soát Bài 9

## Quyết định nguồn và sai khác có chủ ý

- Dùng MMDS sách làm nguồn chuẩn cho FM, AMS, DGIM và cửa sổ suy giảm; dùng slide MMDS để chọn nhịp và hình cần vẽ lại.
- So sánh với Stanford CS246 theo từng cụm. Stanford 2017 diễn đạt thứ tự gộp FM rõ và đúng với sách, nên F05 dùng cách này. MMDS Streams 2 tr.25 và Stanford 2026 tr.44 đảo thứ tự; deck không theo hai trang đó.
- Không gọi $2^R$ là ước lượng không chệch. F04 ghi rõ vấn đề đuôi nặng theo MMDS tr.144.
- Count-Min Sketch không có trong phần MMDS được chọn. Dùng duy nhất tham số của UMass CS514 Lecture 10: $m=\lceil2k/\varepsilon\rceil$, sai số $\varepsilon n/k$, một hàng thành công với xác suất ít nhất $1/2$, và $t=\lceil\log_2(1/\delta)\rceil$ hàng. Không đưa dạng tham số chuẩn khác vào deck.
- Không dạy HyperLogLog chi tiết. Tệp UMass có tên HyperLogLog chỉ trình bày FM/LogLog, thiếu cơ chế chọn thanh ghi bằng tiền tố, trung bình điều hòa và hiệu chỉnh.
- Cửa sổ suy giảm chỉ trình bày một tổng và truy hồi; không phát triển thuật toán duy trì mọi phần tử phổ biến.
- X03 gọi đúng sản phẩm là bộ đếm hậu tố $c_i$; $X_i=9(2c_i-1)$ và trung bình 21 chỉ là phép tự kiểm trong ghi chú.
- F02: quy ước $\rho(0)=L$ và dòng rỗng trả $0$ là quy ước biên do deck đặt để xử lý trường hợp hữu hạn, không phải mệnh đề trích nguyên từ MMDS tr.143; ghi chú trang đã nói rõ điều này.
- M01 gắn nguồn định nghĩa và diễn giải ba mômen vào MMDS tr.146; X02 gắn MMDS Ex.4.5.1, tr.150; ba tệp quy trình (outline, storyboard, HTML) đã đồng bộ.
- C03/C02: $n$ được làm rõ là tổng mọi cập nhật của dòng chỉ tăng ($n=\lVert f\rVert_1$); bảng ký hiệu outline bổ sung $n,m,t,\varepsilon,\delta,X$ và ước lượng chính.
- T00/T01 thu hồi cửa sổ suy giảm mũ: tổng hữu hạn, cập nhật $O(1)$, không làm mặt slide quá tải.
- Cầu nối ngắn trong ghi chú: F06→Count-Min, C04→mômen/AMS, E01→tổng hợp, T00→khóa bảo đảm.
- Ghi chú P00 nêu tiên quyết: Bài 8, biến ngẫu nhiên, kỳ vọng, xác suất va chạm băm.
- A01 ghi điều kiện $c>0$ cho cận 50% của DGIM.
- Gộp P00–A02 thành mạch mở đầu và E00–T01 thành mạch kết luận; cùng mạch bài tập X00–X05, HTML có đúng bảy `<section>` ngoài. Không đổi thứ tự hay số trang.
- Tái rà mạch sau khi gộp phát hiện ba cầu nối thiếu hoặc sai chiều. Đã thêm M07→D00, sửa D09→E00 thành chuyển từ biên cứng sang trọng số giảm theo tuổi, và thêm T01→X00.
- X05 dùng hình tự chứa trạng thái của Hình 4.3, ghi rõ chiều cũ → mới và phần trái chưa xác định. Nếu đã có hai bucket kích thước 8, chuỗi gộp tiếp tục tạo bucket 16 và có thể lan lên mức cao hơn.

## Kiểm tra khi soạn

- Đã tự tính lại ba bảng đuôi Ex.4.4.1: ước lượng $1,16,16$.
- Đã tính lại Ex.4.5.1: tần suất $3,2,2,2$, $F_2=21$, $F_3=51$.
- Đã tính lại Ex.4.5.3: $c_i=[2,3,2,2,1,1,2,1,1]$; ước lượng có trung bình 21.
- Đã kiểm Hình 4.2: mọi bucket kết thúc ở bit 1; ranh giới $k=10$ nằm trước vị trí 16; $k=5$ cho 3 và $k=15$ cho 10 so với số thật 9.
- Đã kiểm bất biến DGIM, thứ tự gộp hai bucket cũ nhất, mốc phải của bucket mới hơn, cận sai số 50% và bộ nhớ $O(\log^2N)$ bit.
- Đã kiểm truy hồi $S_{t+1}=(1-c)S_t+a_{t+1}$ và không đồng nhất phân bố với cửa sổ cố định $1/c$ phần tử.
- Chín hình kỹ thuật đều là SVG tự vẽ, có `role="img"`, `title`, `desc`; HTML có văn bản thay thế. Không dùng raster.

## Hợp nhất kiểm định storyboard và năm phản biện độc lập

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

Đã rà lại hai trang lân cận quanh các đổi thứ tự A00, M02–M03 và D02–D03; kết quả ghi cuối storyboard. Năm vai độc lập gồm góc nhìn sinh viên, chuyên gia giải thuật và khoa học dữ liệu, độ chính xác toán học và thuật toán, phản biện học thuật và giảng dạy, kết nối và mạch viết. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` có bằng chứng hợp lệ đã được xử lý. Các đề xuất nhẹ chỉ thay đổi phong cách không được áp dụng nếu làm tăng chữ hoặc tách thêm trang mà không tạo bước học tập mới.

### Quyết định từ năm vai ở vòng hiện tại

| Vai | Mức cao nhất có bằng chứng hợp lệ | Trang chiếu | Quyết định |
|---|---|---|---|
| Góc nhìn sinh viên | trung bình | C02–C03 | Làm rõ $n$ và bổ sung bảng ký hiệu. Không thêm ví dụ số tự soạn cho cửa sổ suy giảm vì nguồn không cung cấp dữ kiện. |
| Chuyên gia giải thuật và khoa học dữ liệu | trung bình | T00–T01 | Thu hồi cửa sổ suy giảm trong bảng tổng hợp. Bác nhận định thiếu sáu trang vì báo cáo đã bỏ sót X00–X05. |
| Độ chính xác toán học và thuật toán | nghiêm trọng | M01, X02 và ghi chú có thời lượng | Sửa nguồn thành tr.146/tr.150; xóa thời lượng khỏi ghi chú. Tái rà sau sửa: đạt, không còn lỗi chặn hoặc nghiêm trọng. |
| Phản biện học thuật và giảng dạy | nghiêm trọng | F02, A01, toàn bộ ghi chú | Ghi rõ quy ước biên của deck, thêm điều kiện $c>0$, xóa mã nội bộ khỏi lời giảng và bỏ khóa zoom. |
| Kết nối và mạch viết | nghiêm trọng | M07→D00, D09→E00, T01→X00 | Gộp về bảy mạch ngoài; sửa ba cầu nối. Tái rà đúng trang và hai phía lân cận: đạt, không còn lỗi chặn hoặc nghiêm trọng. |

## Tự kiểm biên tập sau chỉnh sửa

- `no-ai-slop/eval.md`: đạt. Nội dung không thêm số liệu ngoài nguồn; câu trực tiếp, không có lời dẫn rỗng, câu hỏi tu từ hay kết luận lặp. Các câu hỏi hiển thị đều là yêu cầu kiểm tra có sản phẩm cụ thể.
- `quill` theo quy trình rà sửa: đạt. Không có `quill.json` và không khởi tạo mới. Mạch FM, Count-Min, AMS và DGIM nối dữ kiện ví dụ sang ký hiệu, thuật toán, lập luận và chi phí; thuật ngữ `mốc thời gian`, `dòng chỉ tăng`, `khóa nặng` được dùng nhất quán.
- Tiêu đề và nhãn bố cục bằng tiếng Việt; chỉ giữ tên thuật toán, tên riêng và ký hiệu chuẩn bằng tiếng Anh.

## Bác bỏ đề xuất có lý do

- Không đổi `data-slide-id`: đây là chuẩn bắt buộc của deck và của quy trình phối hợp planning–HTML.
- Không thêm ví dụ tự soạn: nguồn đã chọn không cho phép thêm dữ kiện ngoài nguồn.
- Không thêm 6 slide: cấu trúc 46 trang (40 giảng + 6 bài tập) là bắt buộc.
- Không dịch ranh giới trong SVG: tọa độ hiện đúng theo Hình 4.2. Kiểm định Chromium phát hiện lớp nền lồng không tải trong cả D07 và X04. Đã nhúng trực tiếp trạng thái nền vào hai SVG, giữ nguyên tọa độ và dữ liệu; không còn phụ thuộc SVG lồng.
- Không giữ chín mạch ngoài của bản cũ: quy chuẩn yêu cầu 5–7. Hai cặp mạch liên tục được gộp thành mở đầu và kết luận, đưa tổng số về bảy mà không đổi 46 trang.

## Kiểm định cuối

- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Máy chủ dự phòng `/tmp/reloadserver.py` được khởi động tại đúng thư mục gốc; URL bài giảng trả `HTTP 200`.
- Kiểm tra tĩnh cuối: 46 `data-slide-id` duy nhất, 46 ghi chú diễn giả, đúng bảy `<section>` ngoài, chín SVG đều tồn tại và có mô tả; không có mã nội bộ hoặc thời lượng trong nội dung/ghi chú, ảnh raster, tài sản thiếu hay SVG lồng; `git diff --check` sạch.
- Chromium duyệt lại đủ 46 trang ở cả $1280\times720$ và $800\times600$: không có lỗi JavaScript, lỗi tải tài nguyên, lỗi KaTeX, tràn hoặc chồng khung. Điều hướng bàn phím từ P00 cho kết quả xuống P01, lên lại P00 và sang phải F00.
- Đã xem trực tiếp bốn ảnh tổng hợp của mỗi kích thước và các trang dày C02, M04, D08, T00, T01, X01, X03, X04, X05. Lần xem đầu phát hiện nền DGIM không hiện ở D07 và X04; sau khi nhúng trực tiếp trạng thái nền, đã render lại toàn bộ và xác nhận hai trang hiện đủ bit, bucket, ranh giới và nhãn ở cả hai kích thước.
- Codex Slides: dự án `20260827213434-b-i-9-d-ng-d-li-u-m-moment-v-c-a-s-unoi` vẫn là bản nháp 0 trang; tệp HTML cuối được tải thành material `20260830133414001-sxq5.html`. Bề mặt Browser nội bộ không có công cụ điều hướng trong phiên này, còn `upload_design_file` trả HTTP 500. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; bằng chứng trực quan cuối đến từ RevealJS cục bộ bằng Chromium.
