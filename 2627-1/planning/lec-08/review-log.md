# Nhật ký rà soát Bài 8

## Quyết định nguồn

- Dùng sách MMDS Chương 4, mục 4.1–4.3 làm nguồn chuẩn; dùng slide MMDS làm nguồn bố cục và hình cần vẽ lại.
- So sánh với Stanford CS246. K01 dùng phép đếm rõ hơn và B11 đối chiếu đường cong từ `stanford-cs246/16-streams.pdf` (CS246, ngày 26/02/2026). B05 dùng vết 11 bit từ `stanford-cs246-2017/streams-2.pdf` (Jeffrey D. Ullman, PDF tạo ngày 01/03/2017). Các mốc này được xác minh bằng nội dung và metadata PDF cục bộ; không suy đoán niên khóa khác.
- Dùng phần đáng kể của MMDS nên trang C02 ghi công và liên kết <http://www.mmds.org>.
- Loại Rejection Sampling vì không có nguồn được chỉ định; loại FM, moment, DGIM, cửa sổ và suy giảm vì thuộc Bài 9.

## Sai khác có chủ ý và sửa lỗi nguồn

- K03 dùng điều kiện $h(K)<a$ trên miền $0,\ldots,b-1$. Cách viết “at most a” trên slide sẽ chọn $a+1$ ngăn nên không được giữ.
- B07 giữ công thức mật độ bit hữu hạn $1-(1-1/n)^{km}$; B08 gọi FPR nâng lũy thừa $k$ và dạng mũ là xấp xỉ, không gọi là chính xác.
- B11 sửa ví dụ $n/m=8,k=6$ thành $(1-e^{-6/8})^6\approx0,02158$. Slide MMDS Streams 2 trang 14 in sai biểu thức và giá trị khoảng 0,0235.
- Ví dụ hồ chứa R03 dùng các phần tử của slide nguồn nhưng thêm một dãy số ngẫu nhiên minh họa để hiện trạng thái. Đây không phải bài tập recitation và không được trình bày như dữ liệu thực nghiệm.
- Ví dụ Bloom 11 bit giữ nguyên dữ kiện đã kiểm kê, định nghĩa $h_1,h_2$, đánh số bit 0–10 từ trái sang phải và kết luận từ bit 3 bằng 0. Chỉ bit 7 va chạm khi thêm 585; chú thích SVG cũ nói cả bit 2 và 5 va chạm đã được sửa.

## Bài tập và giới hạn nguồn

- X01–X04 lấy trực tiếp từ MMDS 4.2.1 và 4.3.1–4.3.3; chỉ dịch, chia bước và thêm sản phẩm/rubric. Đã bỏ yêu cầu phụ không có trong sách: điều kiện $h(K)<1$ ở X01, so sánh ở X02 và trường hợp $n/m=8$ ở X04. Quy tắc làm tròn $k$ chỉ diễn đạt cách biến nghiệm thực thành số hàm băm nguyên dương.
- Sách không có bài tập hồ chứa trực tiếp ở mục 4.2. Không tự tạo bài để lấp khoảng trống; R08 chỉ là câu kiểm tra trong phần giảng.
- Không tạo mã trình diễn hoặc notebook.

## Tài sản

- Sáu SVG trong `2627-1/img/lec-08/` đều có `role="img"`, `title`, `desc`; nhãn bằng tiếng Việt và không dùng màu làm tín hiệu duy nhất.
- Không dùng ảnh raster, phông chữ mạng hoặc thư viện ngoài kho.

## Kiểm tra bản nháp và bản cuối

- Đã tự biên tập theo `no-ai-slop/eval.md`: bỏ lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu, nhận định không có nguồn và nhịp câu lặp máy móc.
- Đã rà bằng nguyên tắc Quill mà không tạo `quill.json`: chuỗi mô hình → mẫu theo khóa → hồ chứa → Bloom; thống nhất ký hiệu, thuật ngữ và câu nối.
- Đã hoàn tất kiểm định storyboard, bốn phản biện độc lập, một vòng chỉnh sửa riêng và hai lượt rà lại storyboard/toán–thuật toán. Bản cuối không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Kiểm tĩnh: 48 trang, 48 mã duy nhất, 48 ghi chú; sáu SVG hợp lệ; mọi đường dẫn cục bộ tồn tại; không có ảnh raster; `git diff --check` sạch.
- Kiểm trình duyệt Chromium ở $1280\times720$ và $800\times600$: 48 trang, không lỗi console, lỗi trang, yêu cầu tài nguyên hỏng hoặc tràn khung. Đã xem bản liên hệ toàn bộ trang và kiểm riêng B05, B10, B11, X03, X04.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Dùng máy chủ HTTP Python đang chạy tại cổng 8765 làm phương án thay thế; URL bài giảng trả `HTTP 200`.
- Codex Slides: dự án bền vững `20260827204905-b-i-8-d-ng-d-li-u-m-h-nh-l-y-m-u-v-l-c-skiv` giữ đầy đủ tài liệu nguồn; `generated/outline.md` và `generated/brief.md` đã được ghi rồi đọc lại. Tải tệp ánh xạ nguồn vào Design Files trả HTTP 500; Browser không khả dụng; dự án vẫn ở `clarify` với 0 slide. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; bản RevealJS cục bộ là bản chuẩn đã kiểm định.

## Hợp nhất kiểm định storyboard và bốn phản biện

| Mức độ | Trang | Vấn đề đã hợp nhất | Quyết định chỉnh sửa |
|---|---|---|---|
| nghiêm trọng | R00–R04 | Đặc tả xuất hiện trước ví dụ, làm chu trình thiếu cầu nối trực giác. | Đổi thứ tự thành R00, R01, R03, R02, R04; R02 dẫn trực tiếp từ vết chạy và chỉ phát biểu xác suất biên. |
| nghiêm trọng | B00–B06 | Đặc tả và giả mã xuất hiện trước ví dụ. | Đổi thứ tự thành B00, B02, B05, B01, B03, B04, B06; cập nhật ghi chú chuyển ý. |
| nghiêm trọng | X01, X02, X04 | Yêu cầu/rubric thêm nội dung ngoài bài giáo trình. | Bỏ các yêu cầu phụ; giữ tổng 15+10+15+20=60 phút và rubric 10 điểm mỗi bài. |
| nghiêm trọng | K06 | Trang giảng lộ toàn bộ đáp án Ex.4.2.1. | Thay bằng quy trình xác định khóa và tình huống trực tiếp từ MMDS: giữ toàn bộ truy vấn của một người dùng. |
| nghiêm trọng | B10, X04 | Thiếu cầu nối đạo hàm, lập luận cực tiểu và quy tắc $k$ nguyên. | Thêm $\ell'(k)$, dấu đạo hàm, điều kiện biên và so hai số nguyên lân cận không nhỏ hơn 1. |
| trung bình | B10, X04 | Phần giảng và bài tập có thể trở thành lặp lại cùng lời giải. | Giữ B10 làm mẫu lập luận; tổ chức X04 như bài tái dựng độc lập, không xem lại B10, và ghi rõ sản phẩm mới trong storyboard. |
| nghiêm trọng | X03 | Thiếu $k\mid n$, giả thiết băm và phân biệt hai biểu thức hữu hạn. | Bổ sung giả thiết; ghi riêng FPR mảng chia và mảng chung, chỉ kết luận tương đương trong xấp xỉ chuẩn; thêm rubric. |
| trung bình | K01 | Chưa định nghĩa “truy vấn” là giá trị phân biệt; dễ hiểu tỷ số các kỳ vọng là kỳ vọng của tỷ số. | Định nghĩa $x,d$ theo giá trị phân biệt và gọi đúng “tỷ số từ số đếm kỳ vọng”. |
| trung bình | K03–K05 | Miền $a,b$ và không gian xác suất của bảo đảm $a/b$ chưa rõ. | Ghi $b\ge1$, $a$ nguyên, $0\le a\le b$; xác suất lấy theo phép chọn $h$, còn $h$ cố định trên dòng. |
| trung bình | R08 | Cận $\Theta(1)$ thiếu mô hình chi phí. | Nêu mô hình RAM và giả định sinh số nguyên đều, truy cập mảng là $O(1)$. |
| trung bình | B05 | Chưa định nghĩa $h_1,h_2$; chú thích va chạm sai. | Thêm định nghĩa theo biểu diễn nhị phân modulo 11; sửa SVG để chỉ bit 7 va chạm. |
| trung bình | B09, X03 | Bài chia mảng chưa được thiết lập trong phần giảng. | Thêm câu thiết lập ở B09 nhưng không đưa công thức hay đáp án. |
| trung bình | B11 | Đường cong thiếu điểm và trục không định lượng. | Vẽ lại đủ $k=1,\ldots,10$, trục y tuyến tính có vạch 0–0,12, đánh dấu riêng $k=5,6$. |
| trung bình | storyboard | Thiếu bảng chu trình chi tiết cho từng cụm. | Thêm bảng bước/mã, đầu vào–sản phẩm, dữ kiện truyền, gộp/không áp dụng, câu nối và thời lượng cho phần giảng lẫn recitation. |
| nhẹ | C02 và hồ sơ nguồn | Dẫn nguồn Stanford chưa đồng bộ, nhãn bản phát hành chưa chắc chắn. | Đồng bộ HTML, outline, storyboard và nhật ký; chỉ ghi ngày/nội dung xác minh được từ PDF cục bộ. |

Không có đề xuất `chặn bàn giao` hoặc `nghiêm trọng` nào bị từ chối. Không áp dụng việc thêm bài hồ chứa cho recitation vì giáo trình không cung cấp bài trực tiếp; đây là ràng buộc nguồn của người dùng.
