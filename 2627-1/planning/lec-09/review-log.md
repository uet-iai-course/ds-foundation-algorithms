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

## Quy trình ghi chú tự học

- Ba reader OpenRouter dùng `z-ai/glm-5.3-flash`: lập kế hoạch (session 68406), đề xuất bản đồ chủ đề (session 39960) và ánh xạ nguồn có phạm vi hẹp sau một lần chạm giới hạn công cụ (session 53830). Cả ba kết quả được điều phối viên hợp nhất vào goal trước khi soạn.
- Writer dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter. Lần đầu chạm giới hạn công cụ; lần hai ghi nguyên tử thành công nhưng bản thảo có lỗi mã hóa tiếng Việt, công thức, bảng và dữ kiện DGIM trên diện rộng. Bản thảo bị loại, không vá cục bộ.
- Năm reviewer độc lập dùng `z-ai/glm-5.3-flash` qua OpenRouter: nguồn (session 87082), toán–thuật toán (91081), sư phạm (8603), mạch viết (62611) và viewer (9207). Năm báo cáo cùng yêu cầu viết lại toàn bộ. Codex chính áp dụng các sửa có bằng chứng theo quyền người dùng đã cấp.
- Giữ các phát hiện: văn bản hỏng mã hóa; giả mã FM sai; thiếu ví dụ số AMS; sai bất biến, mốc gộp, truy vấn, chứng minh và chi phí DGIM; tên SVG không tồn tại; bảng hỏng; thiếu liên kết deck; sai bài 4.4.1; thiếu dẫn xuất truy hồi suy giảm. Bác các đề xuất đưa mã `note-topic-id` vào tài liệu công khai hoặc đổi đường dẫn hình thành `../../img/...`, vì chúng trái quy tắc planning và cơ chế phân giải của viewer.
- Sau bản viết lại, reviewer mạch (session 54820) và reviewer toán–thuật toán phạm vi hẹp (session 17107) đều trả `PASS`, với `requested_model = observed_model = z-ai/glm-5.3-flash` và `provider = OpenRouter`. Một lượt toán rộng hơn chạm giới hạn công cụ trước khi kết luận, nên không được tính là cổng đạt.
- Bác nhận xét đổi ô $h_2(2)$ của Bài 4.4.1 từ 0 thành 1: $h_2(2)=13=01101_2$ kết thúc bằng bit 1, do đó $\rho=0$ như bảng hiện tại.

## Biên tập cuối ghi chú

- `$no-ai-slop`: bỏ hoàn toàn lời dẫn quy trình, nhịp tổng kết lặp và câu chữ hỏng của bản writer; bản công khai dùng câu ngắn, động từ rõ, không có lời quảng bá hoặc câu hỏi tu từ. Các câu hỏi còn lại đều là bài tự kiểm có đáp án.
- `$quill`: rà mạch `N01→N02→N03`, `N01→N04→N05`, `N01→N06→N07→N08`, điểm hội tụ N09 và bài tập N10; không tạo `quill.json`. Ký hiệu $f_x,F_p,R,c_I,b^*,N,k,n,m,t,\varepsilon,\delta$ nhất quán với goal và deck. Việc $k$ mang nghĩa cục bộ khác nhau trong Count-Min và DGIM được giới thiệu lại trong từng đặc tả, không dùng đồng thời.
- Tài liệu công khai không chứa mã nội bộ, tên worker/reviewer, prompt, goal, thời lượng hoặc hướng dẫn quy trình. Chín đường dẫn SVG đều tồn tại; mọi khối `exercise` có `solution` cùng cấp, không lồng nhau.

## Kiểm định viewer và công bố ghi chú

- Viewer thật tải đúng tiêu đề và liên kết deck; mục lục có 32 liên kết cho 32 heading; KaTeX dựng 234 biểu thức, không có lỗi; chín SVG tải đủ và có văn bản thay thế; năm khối mã nhận đúng ngôn ngữ; 11 lời giải gập mặc định.
- Chromium đạt ở $1280\times720$ và $390\times844$: không lỗi JavaScript, lỗi tải tài nguyên hoặc tràn thân trang; liên kết bỏ qua điều hướng và thao tác mở lời giải dùng được bằng bàn phím. Ảnh toàn trang rộng/hẹp đã được xem trực tiếp.
- Chế độ in mở toàn bộ lời giải, ẩn mục lục và thanh hành động, giữ hình trong khung; PDF A4 được tạo để kiểm tra. Viewer từ chối cả đường dẫn vượt thư mục và cặp `doc`–`deck` khác số bài.
- Phép đo đầu tiên dùng `documentElement.scrollWidth` báo 99 px trên màn hình hẹp do MathML ẩn của KaTeX nằm trong vùng cuộn đã cắt. Kiểm tra trực tiếp cho thấy `body.scrollWidth = body.clientWidth` và `window.scrollX` không thể tăng khỏi 0; cổng cuối dùng tràn thân trang và đạt 0 px. Đây không phải tràn nhìn thấy hoặc cuộn ngang cấp tài liệu.
- Chỉ sau các cổng trên, mục Bài 9 trong `index.html` mới được đổi sang hai liên kết bài giảng và ghi chú.
- Kiểm tra một lần kích hoạt từ index đạt ở cả $1280\times720$ và $390\times844$: liên kết nhận focus bàn phím, mở đúng tài liệu, tải đủ chín SVG và không có lỗi KaTeX hoặc lỗi console.

## Vòng đồng bộ deck với ghi chú — 2026-09-02

- Reader kế hoạch OpenRouter phiên `1878` và reader nguồn phiên `82404` đều dùng `z-ai/glm-5.3-flash` qua OpenRouter. Hai reader giữ nguyên 46 trang, 7 mạch ngoài, 40+6 trang, 120+60 phút, chín SVG và toàn bộ nội dung toán–thuật toán; phạm vi sửa chỉ gồm một quy mô ví dụ không có nguồn, nhãn index và speaker notes mang giọng quy trình.
- Writer được gọi đúng model `deepseek/deepseek-v4-flash-0731` trên dossier tạm chỉ chứa các tệp Bài 09 cần thiết. Hai lượt đều dừng ở vòng API đầu với lỗi nguyên văn `api_transport_error`, trước mọi tool call; cầu nối không trả `observed_model`, `provider` hoặc mã phiên OpenRouter hoàn chỉnh. Dossier không bị sửa.
- Theo quyền người dùng đã cấp cho pipeline sau Bài 02, Codex chính áp dụng trực tiếp đúng delta đã được hai reader phê duyệt. Không đổi nội dung hiển thị của deck ngoài nhãn tài nguyên trong index; không đổi công thức, thuật toán, chứng minh, dữ kiện, nguồn, thứ tự, ID hoặc SVG.
- `lecture-note.md` đổi “10.000 sự kiện gần nhất” thành “$N$ sự kiện gần nhất” để không gắn một quy mô không có trong nguồn. Mục Bài 09 trên index dùng nhãn thống nhất “Ghi chú bài giảng”.
- Speaker notes F06, C04, M07, D09, E01, T00 và C03 bỏ nhãn “Cầu nối”; P01, P02, A00, A02, F04, F05, M02, M04, M05, T00, T01 được biên tập tối thiểu theo `$no-ai-slop`. Các câu nối vẫn giữ tuyến FM → Count-Min → AMS → DGIM → suy giảm mũ → tổng hợp → bài tập.
- Tự kiểm `$no-ai-slop/eval.md`: đạt. Bản sửa giữ nguyên ý và chi tiết nguồn, dùng câu trực tiếp, không còn các nhãn quy trình đã khoanh vùng, không thêm số liệu hoặc nhận định.
- Rà theo Quill ở chế độ chỉnh sửa, không khởi tạo `quill.json`: đạt. Thứ tự khái niệm, thuật ngữ và ký hiệu không đổi; các ranh giới phần vẫn có đầu vào và đầu ra rõ.
- Kiểm tra tĩnh sau sửa: 46 `data-slide-id` duy nhất, 46 speaker notes, đúng 7 `<section>` ngoài và 9 đường dẫn SVG duy nhất; không còn chuỗi “Cầu nối” hoặc “10.000 sự kiện”; `git diff --check` sạch. Các cổng năm reviewer và kiểm định trình duyệt của vòng này do điều phối viên thực hiện tiếp trước khi commit.

### Năm phản biện và tái kiểm vòng đồng bộ

- Nguồn và truy nguyên, phiên `25045`: `GO`; không có lỗi chặn hoặc nghiêm trọng.
- Toán và thuật toán, phiên `41637`: `GO`; các ví dụ, cận sai số và lời giải giữ nguyên và đúng.
- Sư phạm và góc nhìn sinh viên, phiên `31093`: `GO`; mạch 46 trang, 7 phần và phân bổ 120+60 phút không đổi.
- Văn phong, phiên `30235`: yêu cầu làm rõ một số câu rút gọn. Đã sửa hẹp A01, M02, D03 và X03; tái kiểm phiên `3388` trả `GO`. Giữ nguồn MMDS 4.4–4.6 ở A01 và câu về FM/LogLog ở T00 vì khớp tài liệu đã chọn.
- Kỹ thuật, phiên đầu `22167` bị loại vì dựa trên nhận định sai rằng các tệp cục bộ không tồn tại. Phiên thay thế `85256` đọc dossier hẹp và trả `GO`.
- Cả năm cổng hợp lệ dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter. Các lượt lỗi `api_transport_error` trước khi đọc tệp bị loại khỏi cổng.
- Theo gợi ý kỹ thuật, tổng trong chứng minh DGIM được viết rõ thành $1+2+4+\cdots+s/2=s-1$ ở D08 và ghi chú bài giảng. Tái kiểm toán hẹp phiên `71981`, cùng model và provider, trả `GO` với 0 phát hiện.

### Kiểm định cuối vòng đồng bộ

- Chromium duyệt đủ 46 trang ở $1280\times720$, $800\times600$ và $720\times900$: không tràn, lỗi JavaScript, lỗi KaTeX hay tài nguyên tải thất bại. Điều hướng bàn phím đi đúng P00→P01 và sang F00; đủ 46 speaker notes. PDF deck có 46 trang.
- Viewer tải đúng tiêu đề, 32 heading, 21 liên kết mục lục, 235 biểu thức KaTeX không lỗi, 9 SVG và 11 khối gập đóng mặc định. Bản rộng và hẹp không có cuộn ngang nhìn thấy; bàn phím, bản in 18 trang, mở khối gập, từ chối vượt thư mục và từ chối cặp doc–deck khác bài đều đạt.
- Index có đúng một liên kết ghi chú Bài 09 và mở đúng deck/note, không có lỗi console.
- Đã xem trực tiếp các trang C03, T00, X05 và bản viewer hẹp; công thức, bảng và SVG đều rõ, không chồng hoặc cắt.
- Codex Slides project `20260827213434-b-i-9-d-ng-d-li-u-m-moment-v-c-a-s-unoi` vẫn ở trạng thái draft với 0 slide. Không tuyên bố đã kiểm canvas; bằng chứng hiển thị cuối là RevealJS và viewer cục bộ bằng Chromium.
