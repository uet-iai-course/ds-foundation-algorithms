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

## Bổ sung trang tiêu đề mạch 2026-10-14

Căn cứ: `AGENTS.md` mục "Trang tiêu đề mạch" và hai gạch đầu dòng về mạch mở đầu, mạch kết luận trong "Mẫu RevealJS bắt buộc"; yêu cầu người dùng 2026-10-14 bổ sung trang tiêu đề mạch cho các bài đã phát hành theo từng đợt có nhật ký. Đợt 2 gồm Bài 07–15; một tác tử soạn duy nhất ghi tệp (Claude Opus 5.5; loại tác tử và effort do điều phối ghi theo lệnh gọi Agent); không commit.

Trang thêm (6), mỗi trang là `<section>` trong đầu tiên của section ngoài, `class="strand-title"`, `id="mach-N"`. Mã `<tiền tố>00` đã thuộc trang nội dung đầu mạch nên dùng `<tiền tố>T`:

| N | Mã | Tên mạch | Dòng dẫn |
|---:|---|---|---|
| 2 | FT | Đếm khóa phân biệt bằng Flajolet–Martin | Muốn đếm người dùng phân biệt với bộ nhớ cố định, phải đọc quy mô từ đuôi dài nhất của giá trị băm. |
| 3 | CT | Ước lượng tần suất bằng Count-Min Sketch | Muốn trả tần suất một khóa mà không giữ bộ đếm cho mọi khóa, phải chấp nhận nhiễu va chạm một phía. |
| 4 | MT | Mômen và ước lượng AMS | Muốn đo độ lệch của phân phối khóa, phải ước lượng mômen bậc hai từ các vị trí ngẫu nhiên. |
| 5 | DT | Đếm bit 1 trong cửa sổ bằng DGIM | Muốn đếm bit 1 gần đây với ít hơn N bit, phải gộp bit 1 thành bucket có kích thước lũy thừa của 2. |
| 6 | ET | Cửa sổ suy giảm và tổng kết | Muốn chọn cấu trúc cho dữ liệu gần đây, phải so cửa sổ suy giảm với các phác thảo đã học. |
| 7 | XT | Bài tập vận dụng | Muốn kiểm các phác thảo bằng tính tay, phải chạy chúng trên dòng ngắn và trạng thái bucket của giáo trình. |

Dòng dẫn 20–24 âm tiết; từ khóa 4–5 cụm; ghi chú diễn giả 81–100 âm tiết, viết từ nội dung các trang trong mạch. Số trang 46 → 53. Các trang nội dung đầu mạch (F00, C00, M00, D00, E00, X00) đều có nội dung, không phải trang tiêu đề phần một dòng, và tiêu đề khác tên mạch; giữ nguyên.

Trang Nội dung: bài chưa có trang này; thêm `P03` (`class="agenda-slide"`, `<h2>Nội dung</h2>`, `ol` 1–7) ngay sau trang bìa P00, tên trùng từng chữ với tên mạch; mạch 1 đặt tên "Mở đầu". Mặt trang khoảng 43 âm tiết; notes một câu cho mỗi mạch, nêu quan hệ suy luận. Mã `P03` theo dãy mã P của mạch mở đầu. Quyết định: thêm (0,5 phút lấy từ trang bìa).

Mạch 6 gộp cửa sổ suy giảm (E00–E01) với bảng tổng kết (T00–T01) như cấu trúc hiện có; tên mạch "Cửa sổ suy giảm và tổng kết" nêu cả hai.

Cố ý chưa làm (việc của đợt sau): mạch mở đầu đầy đủ (Tiên quyết và quy ước, Vấn đề trung tâm, câu luận đề trên trang bìa); chuẩn mật độ mặt trang; mạch kết luận theo khuôn mới (bảng tổng kết ba cột, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, nguồn và tài liệu đọc). Bài 09 còn khối `<style>` riêng và không mang lớp `.course-deck` (có từ trước, ngoài phạm vi). Không sửa CSS, SVG, ghi chú bài giảng, index.

Kiểm tra: section mở/đóng 60/60; 53 `data-slide-id` và 6 `id` duy nhất. Chromium Playwright trên máy chủ cục bộ cổng 8771: ở 1600×900, `#/2` … `#/7` mở đúng trang tiêu đề mạch tương ứng (`id`, số thứ tự khớp); khối tiêu đề nằm trong khung (đáy lớn nhất 729 px trên 900 px), không cuộn ngang; 0 lỗi console, 0 `.katex-error`, không yêu cầu mạng ngoài; trang Nội dung đọc ra đúng tên các mạch. Ở 390×844, RevealJS chuyển sang chế độ cuộn và bỏ qua hash khi nạp; các trang được chụp sau khi cuộn tới phần tử, không tràn ngang. Đã tự xem ảnh. `git diff --check` sạch.

### Sửa sau rà lại đợt 2 (2026-10-14)

Theo báo cáo rà lại đợt 2 (không có phát hiện chặn bàn giao, nghiêm trọng hoặc trung bình), viết lại 6 ghi chú diễn giả của trang tiêu đề mạch: bỏ các câu lấy tài liệu hoặc trang làm chủ ngữ ("Phần này …", "Trang đầu …", "trang tiếp …", "Phần cuối …", "ở phần sau") theo `AGENTS.md` "Tiêu chuẩn trang chiếu và ghi chú diễn giả"; chủ ngữ mới là đối tượng, thuật toán hoặc kết quả; giữ ba ý kế thừa, nhiệm vụ, kết quả giao và độ dài 40–100 âm tiết (no-ai-slop, chế độ Edit). Dòng từ khóa: khoảng trắng trong mỗi cụm và trước dấu "·" đổi thành khoảng trắng không ngắt (`&nbsp;`), nên dấu "·" không đứng đầu dòng và không cụm nào bị tách ở 1600×900; không sửa CSS. Ghi chú ET và ghi chú trang Nội dung P03 nay nêu đúng ba phác thảo được bài tập kiểm (Flajolet–Martin, AMS, DGIM) thay cho "từng phác thảo"; ghi chú XT nói "kiểm lại ba phác thảo". Lý do đặt P03 ngay sau bìa: P01 là trang tình huống "Một dòng, bốn quyết định", không phải trang mục tiêu; sắp lại mạch mở đầu để đợt sau. Mở: dòng dẫn mạch 6 chỉ nêu nửa đầu của mạch gộp (cửa sổ suy giảm), chưa nêu bảng tổng kết; chấp nhận tạm vì tên mạch đã nêu cả hai. Kiểm lại: section mở/đóng cân bằng; `#/2` … `#/N` mở đúng trang tiêu đề mạch ở 1600×900; 0 lỗi console, 0 `.katex-error`; `git diff --check` sạch.

## Nâng cấp ghi chú bài giảng theo chuẩn giáo trình (2026-11-04)

Yêu cầu người dùng (2026-11-04): rà soát ghi chú Bài 09 theo các nguyên tắc về nội dung, văn phong, bố cục và cách diễn giải của từng khối trong `../CLAUDE.md`, `CLAUDE.md` và `AGENTS.md`, giải thích chi tiết, đặc biệt các chứng minh quan trọng, dùng nguồn MMDS; sau khi ghi chú hoàn thiện mới làm lại bộ trang chiếu 09 từ ghi chú mới. Hiện trạng: ghi chú cũ 3 385 âm tiết, soạn trước chuẩn 2026-10-14, thiếu tiên quyết, bảng ký hiệu, tình huống, tóm tắt, bài tập ba mức và chứng minh chia bước. Quy trình: AGENTS.md §"Quy trình tác tử gốc cho một ghi chú bài giảng".

### Tác tử

| Tác tử | Vai trò | Loại, mô hình, effort (theo lệnh gọi `Agent`) | Đầu ra | Quyết định |
|---|---|---|---|---|
| lập kế hoạch | kế hoạch chương, chu trình tám bước, danh sách chứng minh, rủi ro (chỉ đọc) | general-purpose, opus, high | `plan-note.md` (scratchpad) | chấp nhận, trừ bảng ký hiệu 10.2 |
| phân tích nguồn | hồ sơ MMDS §4.4–4.7, slide MMDS/CS246, UMass L8/L10, BHK §6; bài tập và lời giải; lỗi nguồn (chỉ đọc) | general-purpose, opus, high | `source-dossier.md` | chấp nhận |
| bản đồ chủ đề | 28 chủ đề có nhãn và nguồn, tiên quyết, bảng ký hiệu (chỉ đọc) | general-purpose, opus, high | `topic-map.md` | chấp nhận, thứ tự mục theo kế hoạch |
| soạn, sau đó chỉnh sửa (cùng tác tử, tiếp tục bằng `SendMessage`) | viết lại ghi chú (31 485 âm tiết), 6 SVG mới, ba câu tham chiếu ở ghi chú Bài 08; vòng chỉnh sửa theo `merge1.md` | general-purpose, opus, high | `lecture-note.md`, `writer-report.md`, `editor-report-1.md` | bản nháp chấp nhận để rà; ba lượt chỉnh sửa chấp nhận sau rà lại |
| rà: sinh viên | phép thử đọc hiểu, tự giải ví dụ và bài tập | general-purpose, opus, high | `rv-student.md` (0/1/7/22) | chấp nhận, trừ D1 |
| rà: chuyên gia | giải thuật và khoa học dữ liệu | general-purpose, opus, high | `rv-expert.md` (0/2/8/8) | chấp nhận |
| rà: độ chính xác | tính lại mọi số bằng script riêng, kiểm 24 chứng minh | general-purpose, opus, high | `rv-accuracy.md` (0/0/3/13) | chấp nhận |
| rà: phản biện học thuật–giảng dạy | tám bước, từng loại khối, văn phong tác giả, no-ai-slop Detect | general-purpose, opus, high | `rv-pedagogy.md` (0/2/13/14) | chấp nhận |
| rà: mạch, nguồn và kết nối | mạch, đoạn móc nối, cấu trúc chương, trang nguồn | general-purpose, opus, high | `rv-storyline.md` (0/1/15/22) | chấp nhận |

### Quyết định trước khi soạn (điều phối viên)

- **Thứ tự mục:** Mục 1 năm câu hỏi trên một dòng → 2 Flajolet–Martin → 3 mômen và AMS → 4 Count-Min Sketch → 5 DGIM → 6 cửa sổ suy giảm và phần tử phổ biến → 7 chọn cấu trúc. Lý do: theo thứ tự MMDS §4.4–4.7; AMS dùng lại phép gộp trung bình–trung vị của FM; Count-Min không có trong MMDS nên chèn sau mômen, nơi bài toán khóa nặng nối sang phần tử phổ biến của §4.7.3. Bác thứ tự FM → Count-Min → AMS của ghi chú cũ và của bản đồ chủ đề.
- **Ký hiệu:** dùng bảng của bản đồ chủ đề vì khớp Bài 08 ($r$ độ dài dòng, $d=F_0$, bậc $p$, $\kappa$ khóa nặng, $v_i$ số đếm hậu tố AMS, $y_k$ số bit 1 DGIM, $c$ chỉ là hằng suy giảm; Count-Min giữ $m$, $t$ của UMass). Bác bảng 10.2 của kế hoạch ($n$, $w$, $d$, $T_k$) vì $d$ trùng nghĩa và $n$ khác Bài 08. Thuật ngữ "thùng (bucket)" như ghi chú Bài 06.
- **Duy trì biến AMS:** theo MMDS §4.5.5 (hồ chứa $s$ vị trí, Định lý 08.17), thay cho $q$ hồ chứa cỡ 1 của ghi chú cũ (lệch nguồn, không ghi lý do). Kéo theo sửa ba câu tham chiếu tiến trong ghi chú Bài 08.
- **Chứng minh do học phần bổ sung (được duyệt, phải qua rà toán):** cận hai phía FM; $\mathbb E[2^R]$ phân kỳ (ví dụ $d=1$: $L/2+1$); bổ đề mẹo trung vị dạng sơ cấp (ý từ UMass L8 PDF 5–7); số thùng DGIM $O(\log N)$ kể cả thùng vắt biên; tổng số lần gộp không vượt số bit 1 đã đến; tổng trọng số suy giảm $<1/c$ và số phần tử có điểm $\ge\theta$ nhỏ hơn $1/(c\theta)$.
- **Bỏ (không có nguồn):** Count-Min với cập nhật $(x,\Delta)$ và cập nhật âm; khẳng định "khấu hao $O(1)$" không chứng minh; ví dụ tự dựng FM $(4,8),(8,16),(2,4)$ và Count-Min $f_x=6$ với ô 9, 7, 11 (storyboard cũ gán nhầm cho UMass; ví dụ thật của UMass là ô 104, 78, 90 cho ước lượng 78). HyperLogLog chỉ ở đọc thêm.
- **Sửa sai của bản cũ:** thùng DGIM là đoạn vị trí liên tục (Hình 4.2 MMDS; CS246-17a tr.16); "at least one of size 8" nghĩa là có ít nhất một thùng cỡ 8; Bài tập 4.5.1 ở tr.149 (điều phối viên kiểm bằng `pdftotext`, trang PDF 19).
- **Chỗ nguồn sai, ghi đúng trong ghi chú:** MMDS tr.159 "tổng điểm là $1/c$" (đúng là $<1/c$); §4.8 dùng $e^{-ct}$ khác §4.7.2; ba bộ slide gọi FM là không chệch; MMDS-S2 tr.25 và CS246-26 tr.44 đảo thứ tự gộp (sách và CS246-17b tr.30 đúng); MMDS-S1 tr.42 thiếu "+1" trong cận DGIM (chọn CS246-17a tr.23); UMass L10 viết "$=1-2^{-t}$" thay cho "$\ge$" và không nêu giả thiết các hàng độc lập.
- **Kiểm số của điều phối viên:** phương sai biến AMS trên dòng Ví dụ 4.7 bằng 1304, $\mathbb E[X]=59$ (tính lại bằng Python).
- **Độ dài:** 24 000–31 500 âm tiết; vượt thì cắt theo danh sách ưu tiên B của bản đồ chủ đề, không cắt chứng minh chính.

### Vòng rà 1: sáu phát hiện nghiêm trọng và quyết định

Số trong ngoặc: chặn bàn giao/nghiêm trọng/trung bình/nhẹ. Bản đóng băng md5 `58c1bdca…`. Báo cáo và bảng hợp nhất `merge1.md` lưu ở scratchpad của phiên; các phát hiện chặn và nghiêm trọng ghi lại dưới đây, không xóa.

| mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | Nhận xét 09.37; L1097, L1330 | họ băm $(\alpha w+\beta)\bmod M$ có miền $M\ge\lvert\mathcal U\rvert$, không nén được bảng Count-Min | BHK tr.184 chỉ cho họ miền $M$; UMass không cho họ có miền $m$ nhỏ (điều phối viên kiểm `fds.txt`) | giả thiết họ băm phổ dụng miền $m$ như UMass; cách dựng ngoài phạm vi, dẫn CLRS 4e Ch.11 | chấp nhận (A1) |
| nghiêm trọng | Bài tập 09.16, L2212 | "chọn $a$ lẻ" không khôi phục giả thiết độc lập | $\rho(ax+b\bmod2^k)=\rho(x+a^{-1}b\bmod2^k)$; điều phối viên kiểm lại; mô phỏng 1 000 bội của 1 024: $\Pr\approx0{,}996$ so với cận $0{,}135$ | câu cảnh báo theo chuyên gia | chấp nhận (A2) |
| nghiêm trọng | Tình huống 09.2, L1972–1976 | so 267 MB với $1{,}25\cdot10^{14}$ byte lệch nhiều bậc; cận $2\cdot10^9$ điểm vô tác dụng khi $d=10^6$ | lời giải chính xác chỉ cần bộ đệm vòng $N$ mã URL và bộ đếm mỗi URL | sửa phép so, cận $\min(d,1/(c\theta))$, chi phí kiểm hết hạn | chấp nhận (A3) |
| nghiêm trọng | L215, L279, L590, L889, L1034, L1294, L1335, L1931, L1962, L1972, L2054 | câu rào đón và ghi xuất xứ trong thân bài | trái đặc tả D3 và "The author's voice" | bỏ; giữ một câu quy ước sau bảng ký hiệu | chấp nhận (A4) |
| nghiêm trọng | L2054, phần bài tập | ba thành phần mục tiêu không có bài đo (chọn cấu trúc; gộp FM và mẹo trung vị; AMS với hồ chứa) | đối chiếu mục tiêu 1–3 với Bài tập 09.1–09.18 | thêm ba bài | chấp nhận (A5) |
| nghiêm trọng | L220 | "đáp số chính xác buộc phải tốn bộ nhớ tỷ lệ $d$ hoặc $N$" cho cả bốn đại lượng | chương chỉ có cận dưới cho $F_0$ (Nhận xét 09.3) và $y_k$ (Mệnh đề 09.38) | thu hẹp về $F_0$, $y_k$ | chấp nhận (A6) |

Trung bình được chấp nhận (B1–B19 của `merge1.md`): biến AMS từ hồ chứa chung không độc lập nên phương sai $1\,304/s$ và gộp trung vị cần $s$ hồ chứa cỡ 1 độc lập; $t$ của Hệ quả 09.35 dựa trên cận trên $r_{\max}$ chọn trước; Bài tập 09.5 dùng sai Mệnh đề 09.45(b); thùng gộp DGIM là đoạn vị trí liên tục, tách thành khối đánh số; bảng chi phí bước–số lần–chi phí–đóng góp cho mỗi thuật toán; vết chạy trước giả mã và đoạn trực giác ở 2.3, 2.4, 5.1, 5.3, 5.4, 6.2; khối định nghĩa cho mô hình băm lý tưởng và cửa sổ trượt; đoạn quan hệ sau Định lý 09.20, 09.42, 09.44, 09.52; `aligned` và chia bước; câu nối một phía ở ranh giới mục; sửa phát biểu lại Định lý 06.7 và Mệnh đề 08.10(a); dẫn tại chỗ ví dụ mưa (Stanford CS246 2017 Streams 1 tr.28, lựa chọn Stanford vì MMDS không có ví dụ số cho §4.7.1); viết lại Nhận xét 09.3 sát BHK; ký hiệu và thuật ngữ mỗi chữ một nghĩa; Ví dụ 09.20; phản ví dụ của Bổ đề 09.12 và Định lý 09.52; gọi đúng phương pháp thế năng; chi phí lưu mô hình băm lý tưởng.

Bác bỏ: cắt câu chuẩn "Các giả thiết của kết quả có vai trò riêng…" và câu "Bước … dùng …" (đề xuất của vai sinh viên), vì AGENTS.md §"Tiêu chuẩn thứ nhất" quy định đúng dạng này.

Ví dụ và số liệu do bản soạn dựng (thuật toán của nguồn, số đã tính lại bởi tác tử soạn và tác tử độ chính xác): bảng băm 5 bit $h_1$–$h_6$ của FM; $d=1\,000$, $\lambda=4$; $d=10^6$, $L=64$; $\lambda=8$ với $g=21, 41$; vết hồ chứa AMS $s=2$; bảng Count-Min $2\times3$; vết cửa sổ suy giảm với $c=1/2$; Tình huống 09.1 (đồ thị bảy đỉnh theo CS246 2017 Streams 2 tr.32–38, hàm băm của bản soạn); $10^6$ URL và $r=10^9$ ở Tình huống 09.2.

### Vòng chỉnh sửa và rà lại

| Lượt | Tác tử | Nội dung | Rà lại | Quyết định |
|---|---|---|---|---|
| chỉnh sửa 1 | tác tử soạn (SendMessage) | A1–A6, B1–B19, C theo `merge1.md`; đánh số lại (57 khối chung, 20 ví dụ, 19 bài tập, 3 tình huống); thêm Định nghĩa 09.2, 09.8, Nhận xét 09.27, 09.43; ba bài tập mới 09.3, 09.5, 09.9, bỏ hai bài cũ; năm bảng chi phí; 31 866 âm tiết | — | yêu cầu sửa: B9 làm dở (lý do độ dài không đứng được vì tách đoạn không thêm âm tiết), 21/51 công thức tràn ở 390 px |
| chỉnh sửa 1b | như trên | tách 26 đoạn thành 56; 17 chuỗi chứng minh đặt căn cứ ở câu sau công thức; 31 940 âm tiết | độ chính xác (`rc-accuracy.md`, 0/0/3/9; 15/16 phát hiện vòng 1 đã xử lý đúng), giảng dạy (`rc-pedagogy.md`, 0/0/4/15), mạch (`rc-storyline.md`, 0/0/0/14) | chấp nhận, gom phát hiện vào `merge2.md` |
| chỉnh sửa 2 | như trên | R1 `\mathbf w\'` dựng sai thành dấu sắc trên "=" (không sinh `.katex-error`); R2 Ví dụ 09.20(c) theo Hệ quả 09.38, $t=37$, 74 000 bộ đếm; R3 chỉ trung vị thuần có cận, bước trung bình nhóm chưa có cận; R4 Nhận xét 09.4 tự chứa; R5 đoạn kể Tóm tắt một đoạn 7 câu; R6 tài liệu không làm chủ ngữ; 31 972 âm tiết | độ chính xác (`rc2-accuracy.md`, 0/0/0/4), mạch (`rc2-storyline.md`, 0/0/1/5: mất câu nối sang Bài 10) | chấp nhận sau lượt 3 |
| chỉnh sửa 3 | như trên | câu nối sang Bài 10; chín phát hiện nhẹ; `outline.md` (bảng thuật ngữ, bản đồ `lec-09-topic-01…27`), `storyboard.md` (bảng 27 `note-topic-id`), thẻ Bài 9 trong `index.html` (bài giảng "Chưa có"); công thức phương sai AMS tràn 2 px do điều phối viên đo, đã tách | điều phối viên đọc diff | chấp nhận |

Không sửa (nhẹ, có lý do): tên Mục 7 giữ "cấu trúc" cho tới khi làm lại deck, để khỏi lệch nhãn trong SVG và deck; câu 125 MB đầu Mục 5 (Nhận xét 09.3 đã có số); bài nhận biết "vì sao lấy cực tiểu" không khôi phục do trần độ dài.

Thay đổi ở ghi chú Bài 08 (chỉ ba câu tham chiếu tiến): "Mục 6 và Mục 8" → "Mục 5 và Mục 6"; "Mục 5 … hồ chứa cỡ 1 … $1/r$" → "Mục 3 … hồ chứa $s$ vị trí … $s/r$, đúng Định lý 08.17"; "Mục 5 (… hồ chứa cỡ 1)" → "Mục 3 (… hồ chứa $s$ vị trí)". Tác tử chuyên gia xác nhận ba câu khớp.

### Giáo trình và nguồn đã tham khảo theo mục

| Mục | Nguồn và mục tham khảo cách diễn giải |
|---|---|
| Tiên quyết | ghi chú Bài 08, 06 (Định lý 06.7), 05 Mục 8–10; BHK Định lý 2.1 tr.13 (Markov), §12.3 tr.408, §12.5.3 tr.422 |
| 1 | MMDS §4.5.1 tr.145–146, Ví dụ 4.6–4.7; §4.4.1 tr.142–143; CS246 2017 Streams 1 tr.13 |
| 2 | MMDS §4.4 tr.142–145; slide MMDS phần 2 tr.20; CS246 2017 Streams 2 tr.27–30; BHK §6.2.1 tr.183; UMass bài 8 trang chiếu 3–5, 8 (mẹo trung vị) |
| 3 | MMDS §4.5.2–4.5.6 tr.146–150; Định lý 08.17; CS246 2017 Streams 2 tr.49 |
| 4 | UMass bài 10 trang chiếu 8–19 (đọc qua ảnh trang); BHK tr.184–185; CLRS 4e Ch.11 (đọc thêm) |
| 5 | MMDS §4.6 tr.150–157, Hình 4.2–4.3; slide MMDS phần 1 tr.29–32; CS246 2017 Streams 1 tr.13–24 (chọn cận 50% theo tr.23 vì slide MMDS phần 1 tr.42 thiếu "+1"); CLRS 4e §2.1, Ch.16 |
| 6 | MMDS §4.7 tr.157–159; CS246 2017 Streams 1 tr.27–29 (ví dụ mưa tr.28, dẫn tại chỗ) |
| 7, Tình huống | tổng hợp các nguồn trên; CS246 2017 Streams 2 tr.32–38 (Tình huống 09.1) |

Không có đoạn dịch hoặc chép: Nhận xét 09.4 (bản cũ sát BHK tr.183) đã viết lại ở vòng 1.

### Kiểm định ghi chú bài giảng (AGENTS.md §"Kiểm định ghi chú bài giảng")

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| mục tiêu ↔ kết quả ↔ bài tập | đạt | bảng mục tiêu ↔ bài tập đầu phần bài tập; rà mạch vòng 2 xác nhận phủ 19 bài |
| tám bước cho mỗi khái niệm; tính tay trước giả mã, tính đúng, chi phí | đạt | bảng tám bước của `rc-pedagogy.md`; năm bảng chi phí |
| ký hiệu trong bảng, mỗi chữ một nghĩa | đạt | bảng 25 dòng và danh sách ký hiệu cục bộ; `rc2-accuracy.md` |
| định lý bốn phần, chứng minh hoặc nguồn có trang | đạt | 24+ khối `proof`; phác thảo có nguồn: Nhận xét 09.4 (BHK tr.183), Nhận xét 09.50 (MMDS §4.6.6–4.6.7) |
| số liệu tính lại độc lập | đạt | script riêng của tác tử độ chính xác (`acc/verify*.py`): FM, AMS, Count-Min, DGIM 300 dòng ngẫu nhiên, suy giảm; điều phối viên tính lại Var $=1\,304$, 0,217/0,020, 1 020 bit/URL |
| bài tập có gợi ý và lời giải; bài sách có số bài, mục, trang | đạt | MMDS 4.4.1, 4.4.2, 4.5.1 (tr.149), 4.5.2–4.5.6, 4.6.1, 4.6.3 |
| không "xem trang chiếu", câu mảnh, bước bị bỏ | đạt | grep; năm vai rà |
| chứng minh chia bước, `aligned`, đoạn một ý | đạt | `rc-pedagogy.md`; 26 đoạn đã tách |
| số hiệu liên tục, tham chiếu đúng, khối không lồng, hiển thị | đạt | script tham chiếu chéo 0 lỗi; viewer bên dưới |
| đoạn móc nối, "Trong thực hành", nối Bài 08 và Bài 10 | đạt | `rc-storyline.md`, `rc2-storyline.md` |
| giọng kể, tài liệu không làm chủ ngữ | đạt | `rc2-storyline.md`; grep "Mục này", "chương này" 0 |
| nguồn theo mục, không dịch/chép | đạt | bảng trên |
| nhất quán với deck | chưa áp dụng | deck cũ lệch thứ tự mục, ký hiệu, ví dụ Count-Min; deck được làm lại từ ghi chú mới ở giai đoạn sau (yêu cầu người dùng), index ghi bài giảng "Chưa có" |

### Kiểm định của điều phối viên

- Ghi chú cuối: 31 990 âm tiết (`wc -w`), 27 `note-topic-id`, md5 `cb22bc78…`.
- Chromium Playwright qua `http.server` cục bộ, `material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=…`: ở 1600×900 và 390×844, 0 lỗi console/trang, 0 request hỏng, 0 tài nguyên ngoài, 0 `.katex-error`, không tràn ngang trang; 6/6 SVG tải được; 51 công thức hiển thị, ở 1600 px 0 tràn, ở 390 px chỉ dãy 25 bit của DGIM (ngoại lệ: cần giữ liền để đọc vị trí). Bản in: sau `beforeprint` 62/62 khối `details` mở; PDF 112 trang. Đã tự xem ảnh chụp đầu trang (1600) và giữa trang (390).
- `git diff --check` sạch.

## Làm lại bộ trang chiếu từ ghi chú mới (2026-11-04)

Theo yêu cầu người dùng, deck được làm lại sau khi ghi chú hoàn thiện (commit `0c13fdc`). Quy trình: CLAUDE.md khóa học "Sub-agents (course settings)" và AGENTS.md §"Quy trình đa tác tử cho bộ trang chiếu".

### Tác tử

| Tác tử | Vai trò | Loại, mô hình, effort (theo lệnh gọi `Agent`) | Đầu ra | Quyết định |
|---|---|---|---|---|
| lập kế hoạch deck | bản đồ mạch, danh sách trang, thời gian, rủi ro mật độ, ánh xạ trang ↔ chủ đề (chỉ đọc) | general-purpose, opus, high | `plan-deck.md` (scratchpad) | chấp nhận với phương án gọn |
| phân tích nguồn deck | ánh xạ ghi chú → trang, MMDS vs CS246 theo cụm, kiểm kê hình, recitation (chỉ đọc) | general-purpose, opus, high | `source-deck.md` | chấp nhận, trừ ba đề xuất thêm ví dụ ngoài ghi chú |
| soạn deck, sau đó sửa theo kiểm định (SendMessage) | deck 107 trang (94 giảng, 13 recitation), 18 SVG mới qua `generate_deck_svg.py`, `git rm` 8 SVG cũ, outline, storyboard | general-purpose, opus, high | `writer-deck-report.md`, `writer-deck-report-2.md` | chấp nhận để rà |
| kiểm định storyboard | lý do mỗi trang, chu trình, trang tiêu đề mạch, mật độ, thời gian (chỉ đọc) | general-purpose, opus, high | `gate.md`: đạt có điều kiện (0/0/6/12) | chấp nhận toàn bộ |

### Quyết định trước khi soạn

- **Bảy section ngoài, đếm cả recitation như Bài 08:** Mở đầu · Flajolet–Martin · AMS · Count-Min Sketch · Cửa sổ trượt và cửa sổ suy giảm mũ · Tổng kết và tự kiểm tra · Bài tập vận dụng. Mục 5 và Mục 6 của ghi chú cùng vào mạch 5 vì MMDS §4.6–4.7 trình bày liền nhau hai cách giữ dữ liệu gần đây; bác phương án gộp cửa sổ suy giảm vào kết luận như deck cũ (mạch kết luận không có khái niệm mới, AGENTS.md) và phương án tám section ngoài.
- **Số trang:** phương án gọn khoảng 90 trang giảng và 13 trang recitation (áp chín trong mười một phép gộp của kế hoạch; giữ trang chứng minh cửa sổ suy giảm và trang chi phí AMS). Bài có năm thuật toán trọng tâm, mỗi thuật toán đủ chu trình, trang bài toán có hình và chứng minh tách trang theo quy ước tác giả 2026-10-28/29; bảng thời gian ghi trong storyboard.
- **Nguồn theo cụm:** trình tự trang theo slide MMDS; bảy chỗ chọn Stanford CS246 2017 (thứ tự gộp FM 17b tr.30 vì MMDS-S2 tr.25 đảo; thùng là đoạn liên tục 17a tr.16–17; cận 50% có "+1" 17a tr.23; số thùng 17a tr.24; quy mô URL $N=10^9$ 17a tr.13; ví dụ mưa và câu hỏi ngưỡng 17a tr.28, 32; lân cận đồ thị 17b tr.32–38); Count-Min theo UMass bài 10 trang chiếu 8–19.
- **Bác (không có trong ghi chú):** ví dụ DGIM `101111→110000` (MMDS tr.156), ví dụ số cận 50% $k=13$ do tác tử nguồn tự tính, hình vùng tăng theo lũy thừa (MMDS-S1 tr.29–31). Deck là bản tóm lược của ghi chú.
- **Hình:** dùng lại ba SVG của ghi chú, tạo bản trang chiếu cho ba SVG khác, vẽ mới hình bài toán đầu mạch và bảng Count-Min 104/78/90; bỏ chín SVG cũ (nhãn "≥ 8" đọc sai, khung thùng sai, số tự dựng không nguồn ở `count-min.svg` và `fm-trace.svg`, đường suy giảm không phải hàm mũ, sơ đồ thiếu nhánh).
- **CSS:** lớp gốc `course-deck lecture-stream` dùng chung thành phần đã có của Bài 08; không sửa `lecture-course.css`.
- **Việc để lại cho ghi chú:** câu "hàng tỷ bộ đếm" (Mục 3) chưa có số gốc; sửa sau khi deck xong, cùng lượt đồng bộ deck–ghi chú.

### Bản nháp và kiểm định storyboard

Bản nháp: 107 trang; bốn trang tách thêm so với đích (P04B hình vấn đề trung tâm; D07B, D17B vì vượt trần; E07B tách bảng vết 9 hàng thay cho ngoại lệ) — chấp nhận. Ba bản SVG `-trang-chieu` của hình ghi chú (nhãn dưới 18 px khi chiếu) — chấp nhận. `decision-map.svg` giữ lại vì `planning/lec-01/storyboard.md` dòng 229 còn ghi tên. Kiểm của điều phối viên (`check_deck.py`, http.server cục bộ): 107 trang, mã không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, `#/2`…`#/7` mở đúng trang tiêu đề mạch; xem ảnh D01, F09.

| mức độ | trang chiếu | vấn đề | quyết định |
|---|---|---|---|
| trung bình | CT | dòng dẫn 26 âm tiết | sửa (23) |
| trung bình | D19, T01, T05 | `note-topic-id` sai | sửa |
| trung bình | storyboard | 27 hàng thiếu hành động sinh viên hoặc sản phẩm và bằng chứng | sửa, thêm cột kiến thức đầu vào |
| trung bình | storyboard | quyết định `thêm` không lý do | sửa |
| trung bình | E06–E08 | thiếu giới hạn "$d$ số" và ý "tổng $<1/c$" | sửa ở E07 |
| trung bình | P04B | ký hiệu dùng trước định nghĩa | sửa: viết bằng lời |
| nhẹ | 12 mục G7–G18 | ghi chú trang tiêu đề mạch dài, thiếu dòng đọc giả mã/câu chi phí, giới hạn không số, câu chỉ đường, nhãn "Câu hỏi cho lớp", ví dụ D07 trùng D06… | sửa, trừ G16 (C03 giữ hai công cụ trên một trang, mỗi công cụ một dòng, chỉ dùng ở C10) |
| điều phối viên | D01 | hình dùng "=" thay "là"; dòng cuối lặp 125 MB của hình | sửa (số chỉ ở một nơi; F01 áp tương tự) |

### Nguyên tắc không rào đón về vị thế của đoạn văn (yêu cầu người dùng 2026-11-04)

Người dùng: "các câu kiểu rào đón như 'Mô tả này chưa phải định nghĩa; ví dụ sau tính nó trên bốn phần tử.' không cần thiết, chỉ cần nói thẳng, ví dụ 'để làm rõ hơn khái niệm này, xem ví dụ sau'", rồi "ghi nguyên tắc không rào đón vào nguyên tắc chung". Nguồn của câu rào đón: AGENTS.md §"Mẫu trình bày một khái niệm", bước 2 đòi "một câu nói rõ đây chưa phải định nghĩa". Xử lý: thêm nguyên tắc vào `../CLAUDE.md` (mục "Content: cut", ghi rõ thắng câu chữ ngược lại của AGENTS.md); sửa bước 2 trong AGENTS.md của học phần này, `../rl-plan` và `../math-4-AI` (chưa commit, chờ người dùng). Ghi chú Bài 09: tác tử chỉnh sửa (SendMessage, opus, high) thay 13 câu "Mô tả này chưa phải …; ví dụ sau …" bằng câu gọi thẳng khối kế tiếp ("Ví dụ 09.3 tính nó trên bốn phần tử."), bỏ một câu "chưa phải thuật toán"; điều phối viên đọc word-diff; 31 899 âm tiết, viewer 0 `.katex-error`; commit `13f538c`, đã đẩy. Deck: tác tử soạn rà mặt trang và ghi chú diễn giả, không còn câu loại này.

### Năm lượt rà deck vòng 1 (bản đóng băng md5 `6cbf4c0c…`, 107 trang)

| Tác tử | Vai trò | Loại, mô hình, effort | Báo cáo (chặn/nghiêm trọng/trung bình/nhẹ) | Quyết định |
|---|---|---|---|---|
| rà: sinh viên | theo dõi 107 trang ở 1600×900, tự làm câu hỏi và recitation, đo mật độ độc lập | general-purpose, opus, high | `rv-student.md` (0/1/5/7) | chấp nhận |
| rà: chuyên gia | giả thiết, bảo đảm, chi phí, khẳng định quá mức | general-purpose, opus, high | `rv-expert.md` (0/1/4/6) | chấp nhận |
| rà: độ chính xác | tính lại mọi số, SVG theo tọa độ, chứng minh, giả mã, 108 tham chiếu 09.k | general-purpose, opus, high | `rv-accuracy.md` (0/0/4/8) | chấp nhận |
| rà: phản biện giảng dạy | phiếu `slide_authoring_standard.md`, chu trình, câu trên trang, ghi chú diễn giả, no-ai-slop Detect | general-purpose, opus, high | `rv-pedagogy.md` (0/1/12/22) | chấp nhận |
| rà: mạch | vai trò, kết nối vào–ra mỗi mạch, nhất quán với ghi chú | general-purpose, opus, high | `rv-storyline.md` (0/0/7/14) | chấp nhận, trừ ba đề xuất cần nội dung ngoài ghi chú |

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | P04B | "Hàng độc lập: Count-Min không ước lượng thấp" gắn kết luận tất định với giả thiết xác suất | Bổ đề 09.35 (mỗi phần tử cộng 1) không cần độc lập; độc lập chỉ cho cận thừa quá $\varepsilon r/\kappa$ | tách hai ý | chấp nhận (bốn vai cùng nêu) |
| nghiêm trọng | D06 | dòng mở ý tưởng DGIM không hiểu được; hình dùng "thùng", "mốc phải", "cỡ" trước D07 | so với ghi chú §5.2 (đoạn tóm tắt chỉ bằng tổng sai khi bit 1 dồn vào đoạn dài) | viết lại theo ghi chú | chấp nhận |

Trung bình được chấp nhận (bảng hợp nhất `merge-deck1.md`, phần D): C11 "ít nhất khoảng 99 lần"; D18 "từ trạng thái rỗng"; P07 đơn vị và hàng câu 5; D01, E08, M13 ký hiệu định nghĩa trước dùng; E01 nhãn "Nhắc lại:" chỉ chứa điều đã học; C13 đóng bài toán phần tử nặng; M14 phép gộp và điều kiện độc lập của AMS; "ba loại bảo đảm" thống nhất; nhãn in đậm "Bước k." (37 chỗ, ngoài danh sách cho phép) đổi thành "Bước k:" thường; M03 trực giác AMS; C03 tách hai công cụ (thay quyết định "giữ" của G16); lời chú của người soạn trong ghi chú diễn giả (M12, D11, E07, E07B, XT, X01, X03, X04) và câu rào đón F07; trang bài tập có năng lực và hướng dẫn chấm; 12 trang Ví dụ thêm dòng "Tính …"; F03, F13 có phép tính; X04 nhãn đè chú giải; D17B vế bất biến cho cỡ lớn hơn; X05C "hai thùng cỡ 8 cũ nhất". Bác: ba đề xuất cần nội dung ngoài ghi chú (mở rộng C07, chạy DGIM trên dòng bit của a, câu hỏi T06 mới). 390 px: Reveal co khung như Bài 08, giữ.

### Sửa ghi chú phát sinh từ rà deck (ghi chú là bản gốc nên sửa trước)

| Commit | Nội dung | Rà lại |
|---|---|---|
| `c9640d3` | "phân phối đuôi nặng" đầy đủ để "đuôi" chỉ còn nghĩa độ dài đuôi (tiêu đề §2.4 đổi); chuỗi bit của $\rho$ đổi $y$ → $\mathbf s$; Count-Min $2\times3$ tách nhiễu quan sát $Z_1=Z_2=3$ khỏi cận kỳ vọng $(r-f_{\mathrm a})/m=10/3\le r/m=5$; 266 byte (không 267); phép tính $L/2+1=33$ và cận 17; "tới $2^{32}$ bộ đếm" thay "hàng tỷ bộ đếm" | độ chính xác (`rc3-accuracy.md`): 0/0/0/1 |
| `b1d1c77` | Nhận xét 09.3: hàng câu 5 là $D_r(u)$ với mọi $u$, $d$ số (khớp §6.2); "cả năm đại lượng" | điều phối viên đọc diff; phát hiện từ vai chuyên gia ở P07 |

Ba lượt sửa ghi chú do tác tử chỉnh sửa ghi chú (opus, high, SendMessage) làm, không chạy cùng lúc với tác tử deck.

### Chỉnh sửa deck và rà lại

| Lượt | Nội dung | Rà lại | Quyết định |
|---|---|---|---|
| chỉnh sửa 1 (tác tử soạn deck) | phần D của `merge-deck1.md`: P04B, D06 viết lại; C03 tách thành C03, C03B; E08 tách bảng chi phí thành E11 sau chứng minh; P07 theo Nhận xét 09.3 mới; "Bước k:" không in đậm; trang Ví dụ có "Tính …"; theo ghi chú: "phân phối đuôi nặng", $\rho(\mathbf s)$, 266 byte, 17 so với 33, $Z_j$ quan sát và kỳ vọng; 107 → 109 trang | độ chính xác `rc-accuracy.md` (12/12 phát hiện vòng 1 đã sửa; mới 0/0/1/5: C13 lấy mọi $u$ thay vì phần tử đã xuất hiện); mạch `rc-storyline.md` (19/21, hai mục bác theo K3; 0/0/1/6: storyboard ghi E11 đã gộp); giảng dạy `rc-pedagogy.md` (0/0/2/3: lời chú người soạn X01, D04; M11 9 dòng, P05 7 dòng); sinh viên `rc-student.md` (nghiêm trọng D06 và 5 trung bình vòng 1 đã giải quyết; mới: M11) | chấp nhận, gom vào lượt 2 |
| chỉnh sửa 2 | C13 chỉ phần tử đã xuất hiện (Hệ quả 09.38(b)); storyboard E11, C03; bỏ lời chú người soạn; M11 8 dòng, P05 6 dòng; các mục nhẹ (P04B họ phổ dụng, C03 định nghĩa độc lập từng cặp, D06 `desc` và ghi chú, X04, X05 gọi lại "hai mươi lăm bit", công thức ngắt dòng) | điều phối viên đọc báo cáo; kiểm định cuối bên dưới | chấp nhận; không làm: E06 dòng "Tính …" (trang lên 7 dòng, động từ đã ở tiêu đề cột), một chỗ ngắt công thức ở D13 (nhẹ) |
| index | thẻ Bài 9: "Bài giảng" liên kết deck | kiểm định cuối | — |

### Sự cố commit `13f538c`

Commit `13f538c` (sửa câu rào đón trong ghi chú) mang theo việc xóa 8 SVG cũ mà tác tử soạn deck đã `git rm` sẵn trong vùng stage; điều phối viên không kiểm `git diff --cached --stat` trước khi commit. Hệ quả: từ `13f538c` tới commit deck mới, deck cũ trên `origin/main` thiếu hình. Không viết lại lịch sử; commit deck mới khắc phục. Biện pháp: kiểm vùng stage (`git diff --cached --stat`) trước mỗi commit.

### Kiểm định cuối deck và bàn giao

| Tác tử | Vai trò | Loại, mô hình, effort | Báo cáo | Quyết định |
|---|---|---|---|---|
| kiểm định cuối | phiếu `slide_authoring_standard.md`, kỹ thuật, mật độ đếm độc lập, trang tiêu đề mạch, hình, đồng bộ kế hoạch và ghi chú, index, git (chỉ đọc) | general-purpose, opus, high | `final-check.md`: **đạt** (0/0/1/6) | chấp nhận |

Bằng chứng của tác tử kiểm định (Chromium Playwright, http.server cục bộ): 0 lỗi console/trang, 0 request hỏng hoặc ra mạng, 0 `.katex-error`; 109 `data-slide-id` duy nhất, không lộ trên mặt trang hay ghi chú; 109 trang vừa khung 1280×720 ở 1600×900; không tràn ngang ở 390×844; phím mũi tên, Home, End hoạt động; cấu hình RevealJS và CSS đúng (`lang="vi"`, 1280×720, `controlsLayout: "edges"`, `slideNumber`, `hash`, `hashOneBasedIndex`, plugin cục bộ, không `fragment`, không `<style>`, `course-deck lecture-stream`); `#/2`…`#/7` mở đúng `mach-2`…`mach-7`, khớp trang Nội dung, đã xem sáu trang tiêu đề mạch ở hai cỡ và 13 tờ ghép đủ 109 trang; 18/18 SVG tải được, có alt cụ thể, không raster; hơn 40 số và phát biểu khớp ghi chú hiện tại (C13 theo Hệ quả 09.38(b), P07 theo Nhận xét 09.3, P04B tách ý tất định và ý xác suất); thẻ Bài 9 của index liên kết deck và ghi chú, cả hai trả 200; `git diff --check` sạch. Phiếu `slide_authoring_standard.md`: đạt mọi mục.

Phát hiện: trung bình — nhật ký chưa có mục kiểm định cuối (mục này). Nhẹ — D13 nhãn bước nhảy 2 → 5 và P05 danh sách 1, 3, 4, 5: đã sửa (D13 Bước 1–4; P05 nhãn "Câu 1–2:" … "Câu 5:"); để lại: nhãn vị trí trong bốn hình DGIM hiển thị 17,1–17,4 px (dưới mức 18 px của K5 một chút), tiêu đề mạch 4 ngắt dòng "Count-/Min", tiêu đề bìa ngắt "CỬA / SỔ", ở 390 px RevealJS chuyển chế độ cuộn và bỏ hash khi tải (giống Bài 08).

Kiểm lại của điều phối viên sau hai sửa nhãn (`check_deck.py`): 109 trang, mã không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, `#/2`…`#/7` đúng. Mật độ (đếm âm tiết theo khoảng trắng, trừ tiêu đề, KaTeX, giả mã, số trong bảng, nhãn hình, ghi chú): tám trang trên 60, đều thuộc loại trần 80 hoặc có ngoại lệ trong storyboard — P02 66 (mục tiêu), P04B 73 (trả lời có điều kiện, ngoại lệ K8), P07 79 (bảng chi phí), F18 64 (bảng chi phí), M14 66 (bảng chi phí), T02 70 (bảng tổng kết, ngoại lệ 8 dòng), T04 61 (bảng so sánh), T05 61 (trả lời có điều kiện); không dòng nào quá 20 âm tiết, không trang nào quá 3 công thức hiển thị. Bảng đếm từng trang trong storyboard (cột âm tiết).

Bàn giao: deck 109 trang (96 giảng, 120 phút; 13 recitation, 60 phút), 18 SVG mới, `outline.md`, `storyboard.md`, nhật ký này, thẻ index. Không đưa vào commit: `material-viewer.*` (thay đổi chưa commit của người khác), `AGENTS.md` (nguyên tắc không rào đón, chờ người dùng cho commit), `.claude/`, `.codex/`, `skills/`. `decision-map.svg` giữ lại (còn tên trong `planning/lec-01/storyboard.md`), không trang hay ghi chú nào dùng.

## Sửa ghi chú theo chuẩn 2026-11 (đợt A1, giai đoạn 1, 2026-11-11)

Căn cứ: `prompt_fix_lecture_notes.md` và ba quyết định của người dùng ngày 2026-11-11, đã ghi vào `AGENTS.md` §"Cấu trúc bắt buộc" mục 5, 6, 10 (commit `761469f`): ghi chú không có mục bản đồ chủ đề; không có câu nào về nguồn gốc số liệu hay đính chính sách, nguồn chỉ ở mục tài liệu tham khảo; mọi bài có `exercises.md` chứa bài tập củng cố. Điều phối viên: Claude Opus 5.5 (`claude-opus-5-5`), effort high, không soạn hay rà.

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Rà văn phong và giọng tác giả (đợt duyệt toàn học phần, bản ghi chú chưa đổi) | general-purpose | opus | high | không |
| Rà chuẩn giáo trình và kế hoạch tách bài tập | general-purpose | opus | high | không |
| Rà độ chính xác toán và thuật toán | general-purpose | opus | high | không |
| Biên tập (ba vòng, tiếp tục bằng SendMessage) | general-purpose | opus | high | ghi chú, `exercises.md`, `outline.md`, một SVG |
| Kiểm tra lại độ chính xác (hai lượt) | general-purpose | opus | high | không |
| Kiểm tra lại mạch, liên kết và văn phong (hai lượt) | general-purpose | opus | high | không |

### Phát hiện và quyết định

| mức độ | vị trí | vấn đề | quyết định |
|---|---|---|---|
| nghiêm trọng | Bài tập củng cố | chưa nằm trong `exercises.md` | chấp nhận: 09.10–09.19 chuyển nguyên văn sang `materials/lec-09/exercises.md`, giữ số; ghi chú còn một câu kèm liên kết |
| trung bình | bản đồ chủ đề, câu nguồn gốc số liệu, danh sách ký hiệu cục bộ | trái quyết định 2026-11-11 | chấp nhận: xóa; lý do chu trình rút gọn topic-10, topic-12 chép sang `outline.md` |
| trung bình | sau Hệ quả 09.38 | $\delta=0{,}01/r_{\max}$ mâu thuẫn với nghĩa của $\delta$ trong hệ quả | chấp nhận: "xác suất thất bại $0{,}01/r_{\max}$ cho mỗi phần tử trong Định lý 09.37, tức Hệ quả 09.38 với $\delta=0{,}01$" |
| trung bình | câu mở phần tình huống | mâu thuẫn với Tình huống 09.1 (giá trị băm cố định) | chấp nhận: viết lại, thứ tự 09.1, 09.2, 09.3 |
| trung bình | kết Mục 7 | thiếu "còn thiếu gì" và câu nối | chấp nhận |
| trung bình | 2.5, 3.5, 5.5 | tiểu mục mở thẳng bằng khối | chấp nhận: thêm câu dẫn |
| trung bình | Nhận xét 09.17 | $\alpha,\beta$ chưa gọi tên | chấp nhận; thêm trường hợp $\alpha$ lẻ theo lời giải 09.17 |
| trung bình | khoảng 35 chỗ | nguồn làm chủ ngữ hoặc bình nguồn ("UMass … dùng mà không phát biểu", "MMDS chỉ trả lời định tính", "Hình vẽ lại MMDS Hình 4.2") | chấp nhận: nội dung trước, nguồn trong ngoặc, giữ mọi số trang; cắt các câu bình nguồn |
| trung bình | 708, 2193, Tóm tắt | câu về vị thế ("bảo đảm định lượng … dừng ở …", "chưa có cận") | chấp nhận: viết nội dung dương |
| trung bình | Ví dụ 09.1 | hứa năm câu trả lời, mục 5 không trả lời | chấp nhận |
| nhẹ | 7 điểm toán (Nhận xét 09.4 "không quá $\lvert\mathcal U\rvert+1$", "(lẻ)" ở Nhận xét 09.12, $m\ge2$, $\theta=1/2$ ở Tình huống 09.2, "ước lượng bị chệch", cận $\lvert\mathcal U\rvert$ bit, ký hiệu $r_{\max}$ vào bảng) | chấp nhận |
| nhẹ | alt hình cấu trúc chương và nhãn SVG | "ít hơn 2/c điểm" chỉ đúng khi $\theta=1/2$ | chấp nhận: "1/(cθ)" ở alt, nhãn và `<desc>` của `img/lec-09/cau-truc-chuong-09.svg`; bộ sinh hình trong `tools/` sửa cùng, chạy lại cho tệp trùng khít |
| nhẹ | khối `aligned` | dòng ngắn bị bẻ, dòng chứa hai quan hệ | chấp nhận: gộp 8 khối, tách 8 khối; đo ở 390 px không tràn |
| nhẹ | các điểm còn lại của ba lượt rà (câu rào đón, trỏ tiến, câu lặp 103, $\theta<1$, phân phối "ta/chúng ta", trích dẫn lặp tr.159, số trang MMDS ở Bài tập 09.9) | chấp nhận |
| trung bình | Nhận xét 09.4 | là kết quả, nên đổi thành Mệnh đề | bác bỏ: đổi nhãn khối có số hiệu, trái ràng buộc đợt A |
| nhẹ | Ví dụ 09.14–09.16, "đúng MMDS Hình 4.3" | đổi tiêu đề nhắc hình của sách | bác bỏ: tiêu đề khối giữ nguyên; Bài tập 09.15, 09.16 là bài sách làm trên chính các hình đó |
| nhẹ | Thuật toán 09.6, 09.20, 09.45 | thiếu bảng bước–số lần–chi phí | bác bỏ: phép đếm bằng lời đủ, bảng làm tăng độ dài |
| nhẹ | sau 09.10, 09.22, 09.48 | "Trong thực hành" gom vào Nhận xét 09.17, 09.28 | chấp nhận cách gom, không thêm |
| nhẹ | tiên quyết | Mệnh đề 08.10(b), Nhận xét 08.21 chưa phát biểu lại | để lại |
| trung bình | ghi chú diễn giả của deck (dòng 234–245) | ghi "Lời giải đầy đủ ở các Bài tập … của ghi chú bài giảng" | ngoài phạm vi goal (không sửa deck); số hiệu không đổi nên dẫn chiếu vẫn đúng, chỉ chữ "của ghi chú" cần đổi thành "của tệp bài tập" ở lần sửa deck sau |

Hai ý bị cắt có chủ ý ở vòng 2 (người rà độ chính xác hỏi lại): "Cận kỳ vọng thành đẳng thức khi họ độc lập từng cặp" (nhận xét bên lề không dùng lại) và "số biến AMS cần dùng chưa có cận định lượng" (câu về vị thế).

Nguồn gốc số liệu chuyển khỏi ghi chú (nguyên văn câu đã xóa): "Số liệu của nguồn được dẫn tại chỗ; các số không kèm nguồn (bảng giá trị băm, bảng Count-Min $2\times3$, số ngẫu nhiên của vết chạy hồ chứa, hằng $c=1/2$, dữ kiện của Ví dụ 09.20, các tình huống và các bài tập không mang số bài sách) là dữ liệu tính tay của chương."

### Kết quả kiểm tra

- Độ dài (`wc -w`): ghi chú 31 971 → 28 913; `exercises.md` 2 287 (10 bài, 10 hint, 10 solution); ghi chú còn 9 bài tập cuối mục, mỗi bài một hint và một solution.
- Khối có số hiệu: 99 khối trước và sau (ghi chú + `exercises.md`) trùng khít về loại, số và tiêu đề.
- Tham chiếu chéo: mọi "Loại 09.k" trỏ tới khối có thật (kiểm bằng script của người rà độ chính xác).
- Grep sau sửa: 0 "chưa phải", "do học phần", "do bài giảng", "nguyên văn", "dẫn xuất", "lỗi in", "Bản đồ chủ đề", "Bài này", "Mục này", "Đáp án", "Đáp số"; `git diff --check` sạch.
- Trình duyệt (Playwright Chromium, `http.server` cục bộ; `reloadserver` chèn script tải lại bị CSP chặn nên không dùng cho phép đo lỗi console): ghi chú và `exercises.md` ở 1600×900 và 390×844, 0 lỗi console và trang, 0 request hỏng, 0 tài nguyên ngoài, 0 `.katex-error`, không tràn ngang trang (hình rộng nằm trong khung cuộn của viewer, như Bài 10), không còn chỉ thị `:::` thô, khối gập mở khi in. Ảnh chụp đã xem trong scratchpad của phiên.
- Giai đoạn 2 (chuẩn hóa `exercises.md`: "Kiểm tra lại", "Câu (a)", bài tự chứa, bài cho mục tiêu 4) làm sau khi ghi chú được push.
