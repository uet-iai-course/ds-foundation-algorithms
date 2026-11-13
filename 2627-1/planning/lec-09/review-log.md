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

## Tệp bài tập theo chuẩn 2026-11 (đợt A1, giai đoạn 2, 2026-11-11)

Căn cứ: `AGENTS.md` §"Cấu trúc bắt buộc" mục 10 và yêu cầu người dùng giữa giai đoạn này (2026-11-11): mọi bài trong `exercises.md` lấy từ bài tập của các giáo trình là nguồn chính của bài, không dùng câu hỏi trang chiếu hay bài tự dựng (đã ghi vào `AGENTS.md` mục 10).

### Tác tử (lấy từ lời gọi công cụ)

| Vai trò | Loại | Mô hình | Effort | Ghi |
|---|---|---|---|---|
| Lập danh sách bài | general-purpose | opus | high | không |
| Soạn tệp bài tập (tác tử biên tập của giai đoạn 1, SendMessage) | general-purpose | opus | high | `exercises.md`, dòng tham khảo của ghi chú, một câu ghi chú, `storyboard.md` |
| Rà độ chính xác (ba lượt) | general-purpose | opus | high | không |
| Rà vai sinh viên năm hai (hai lượt) | general-purpose | opus | high | không |
| Rà sư phạm và văn phong, `no-ai-slop` Detect (ba lượt) | general-purpose | opus | high | không |

### Danh sách bài sau giai đoạn 2

| Bài | Nguồn | Mức | Mục tiêu |
|---|---|---|---|
| 09.10 | MMDS Bài 4.5.1, §4.5.6, tr.149 (recitation) | nhận biết | 1 |
| 09.14 | MMDS Bài 4.5.6, tr.150 (bỏ Bài 4.5.5: trùng chứng minh Bổ đề 09.21) | nhận biết | 3 |
| 09.20 | BHK Bài 6.7, §6.6, tr.204 | nhận biết | 4 |
| 09.22 | BHK Bài 6.1 câu 1, §6.6, tr.204 | nhận biết | 3 |
| 09.11 | MMDS Bài 4.4.1, §4.4.5, tr.145 (recitation) | tính toán | 2 |
| 09.12 | MMDS Bài 4.5.3, tr.150 (recitation) | tính toán | 3 |
| 09.13 | MMDS Bài 4.5.4, tr.150 | tính toán | 3 |
| 09.15 | MMDS Bài 4.6.1, §4.6.8, tr.157 (recitation) | tính toán | 5 |
| 09.16 | MMDS Bài 4.6.3, tr.157 (recitation) | tính toán | 5 |
| 09.19 | MMDS Bài 4.6.2, tr.157 | tính toán | 5 |
| 09.17 | MMDS Bài 4.4.2, tr.145 | vận dụng | 2 |
| 09.18 | MMDS Bài 4.5.2, tr.150 | vận dụng | 1 |
| 09.21 | BHK Bài 6.6, §6.6, tr.204 | vận dụng | 2 |

Mục tiêu 6 (cửa sổ suy giảm) không có bài giáo trình (MMDS §4.7 không có bài tập); dựa vào Bài tập 09.8 của ghi chú. Số hiệu không đơn điệu trong tệp vì bài xếp theo mức và giữ số đã công bố.

Bỏ khỏi tệp theo yêu cầu người dùng: 09.19 cũ (câu hỏi trang chiếu Stanford CS246 2017, Streams 1, tr.32, về ngưỡng $\theta$), 09.20 cũ (UMass CS514 bài 10 trang chiếu 8), 09.21 và 09.22 cũ (bài dựng trên Ví dụ 09.12). Số 09.19–09.22 dùng lại cho bốn bài giáo trình; deck không dẫn các số này, `storyboard.md` đã bỏ dẫn chiếu 09.19 cũ (dòng 169, 239).

Phần mở rộng có chủ đích so với sách (phép tính trên chính dữ kiện của bài): 09.12(b) ước lượng và trung bình; 09.16(b) trường hợp còn một thùng cỡ 8 cũ hơn (khớp deck X05C); 09.18(c) kiểm với hai dòng của ghi chú; 09.21(b) số lần chạy nhỏ nhất; 09.22 "$r$ chưa biết trước". Cách đọc quy tắc 4: lời giải 09.19 theo Định nghĩa 09.42 của ghi chú (đủ mọi kích thước từ 1 tới lớn nhất) cho 4 cách chia; đọc lỏng câu "one or two buckets of any given size, up to some maximum size" của MMDS (§4.6.2) cho 9 cách.

### Phát hiện chính và quyết định

| mức độ | bài | vấn đề | quyết định |
|---|---|---|---|
| trung bình | 09.17 và ghi chú (Nhận xét 09.17) | câu "khi $\alpha$ lẻ, giả thiết độc lập không thỏa trên dữ liệu có cấu trúc" ngụ ý độc lập đúng với dữ liệu khác; với $\alpha$ cố định hiệu $h(x)-h(x')$ không phụ thuộc $\beta$ | chấp nhận: sửa cả ghi chú (câu này vào ghi chú ở giai đoạn 1, commit `2f5c961`) và lời giải |
| trung bình | 09.17 | ví dụ "bội của 1 024" mâu thuẫn $L=5$ | chấp nhận: ví dụ bội của 4 |
| trung bình | 09.16 | đề và lời giải mâu thuẫn về thùng cỡ 8 | chấp nhận: tách (a), (b) |
| trung bình | 09.19 cũ | lời giải lặp Định lý 09.56, thiếu vị trí 4 | đã sửa rồi bỏ bài theo quy tắc mới |
| trung bình | 09.14, 09.20, 09.19 cũ | xếp sai mức | chấp nhận |
| trung bình | 09.22 cũ | thiếu lý do độc lập của ba chỉ báo | đã sửa rồi bỏ bài theo quy tắc mới |
| trung bình | 09.20 mới | gợi ý là lời giải, đoạn hệ quả Count-Min lặp ghi chú | chấp nhận: gợi ý mở đầu, một câu dẫn phản ví dụ sau Định lý 09.37 |
| trung bình | 09.19 mới | câu bàn chữ của MMDS là ý bên lề | chấp nhận: cắt, ghi ở đây |
| nhẹ | nhiều bài | "Câu (a)", "Kiểm tra lại" có tác dụng, đề tự chứa, ký hiệu theo ghi chú ($n_j$, $m$, $x_1,\ldots,x_r$), lý do dừng và cực trị ở 09.18, đơn điệu ở 09.21 | chấp nhận |
| — | đề nghị rút "Điều kiện áp dụng" của Định lý 09.56 hoặc đổi tham số bài 09.19 cũ | bác bỏ: không đổi ghi chú đã duyệt, không đổi dữ kiện bài có nguồn |
| — | đánh số lại theo thứ tự trong tệp | bác bỏ: ghi chú và deck dẫn số hiện tại |

### Kết quả kiểm tra

- Tính lại độc lập của ba lượt rà: mọi số của 13 bài đúng (vét cạn cách chia DGIM của 09.19: 4 cách; tổng nhị thức của 09.21: $q=15$ thất bại $0{,}2131$, $q=17$ thất bại $0{,}1989$, nên $q=17$; điều phối viên tính lại bảng $q=1,\ldots,19$).
- `exercises.md`: 3 728 âm tiết, 13 bài, 13 hint, 13 solution; 36 dẫn chiếu "Loại 0X.k" đều trỏ tới khối có thật (ghi chú Bài 08, Bài 09); không "Đáp án", "hãy", câu hỏi tu từ hay câu nguồn gốc số liệu.
- Ghi chú: câu Nhận xét 09.17 về $\alpha$ lẻ; câu Bài tập củng cố "09.10–09.22"; dòng tham khảo MMDS, BHK, Stanford, UMass cập nhật.
- Trình duyệt (`http.server`, Playwright Chromium): ghi chú và `exercises.md` ở 1600×900 và 390×844, 0 lỗi console, 0 request hỏng, 0 `.katex-error`, không tràn ngang, khối gập mở khi in.
- `index.html`: thẻ Bài 9 thêm liên kết "Bài tập".
- Lệch với deck (không sửa trong goal): ghi chú diễn giả X01–X05C ghi "Bài tập 09.1x của ghi chú" cho các bài nay ở tệp bài tập; số hiệu không đổi.


## Rà soát deck theo nguyên tắc deck mới và đối chiếu ghi chú bài giảng (2026-11-13)

**Bối cảnh.** Yêu cầu người dùng (2026-11-13): kiểm tra các deck 01–10 xem deck nào chưa tuân thủ các nguyên tắc của deck mới và chưa khớp với ghi chú bài giảng, ghi bảng phát hiện đầy đủ vào `review-log.md` của từng bài, thời điểm phát hiện là ngày 2026-11-13. Đợt này chỉ đọc: deck, ghi chú và `exercises.md` không đổi (HEAD `45ddcf9`; md5 deck `1ec1af40`, ghi chú `a24d6a3e`, `exercises.md` `acf20a0f`, trùng nhau lúc bắt đầu và lúc kết thúc lượt rà).

**Căn cứ.** `AGENTS.md` dòng 1–190 và 381–650; `slide_authoring_standard.md`; `CLAUDE.md` của học phần ("Course-specific rules", "Writing", "Deck structure and content"); `../CLAUDE.md` ("Writing course content", "The author's voice", gồm các luật 2026-11-04 và 2026-11-09); quy ước tác giả 2026-10-28/29 (`planning/lec-08/review-log.md` mục "Trang bài toán đầu mạch", `planning/lec-08/danh-gia-giang-day.md` "Định hướng chung"); quy ước của deck làm lại từ ghi chú (Bài 09 ngày 2026-11-04, Bài 10 ngày 2026-11-08): deck là bản tóm lược của ghi chú, ký hiệu theo bảng ký hiệu của ghi chú, mục tiêu khớp ghi chú, trang bài toán có hình sau mỗi trang tiêu đề mạch, chứng minh tách trang, mỗi bài recitation có trang "Lời giải:", dẫn chiếu khối ghi chú và bài tập trỏ đúng khối hiện tại.

**Tác tử (theo lời gọi công cụ).** Vai trò: rà soát chỉ đọc (quy tắc deck mới và đối chiếu ghi chú), một tác tử riêng cho Bài 09; loại `general-purpose`, mô hình `opus` (Opus 5.5), effort `high`; `no-ai-slop` chế độ Detect. Không ghi tệp trong kho, không commit. Mười tác tử của mười bài chạy song song (đều chỉ đọc). Điều phối viên: phiên Opus 5.5.

**Quét cơ học của điều phối viên** (Playwright, 1600×900 và 390×844, máy chủ tĩnh cục bộ): 109 trang, 7 section ngoài; trang tiêu đề mạch `mach-2…7` mở đúng `#/2…7`; 0 lỗi console/trang, 0 request hỏng, 0 `.katex-error`, 0 `fragment`; mã nguồn không có `<style>`, `style=""`, `.dense`; dẫn chiếu `09.k` của deck so với khối hiện có của ghi chú và `exercises.md` (đều tồn tại; loại khối và nội dung do tác tử kiểm). Các cờ quét được tác tử kiểm lại; cờ giả ghi ở mục "Đã kiểm" bên dưới.

**Điều phối viên kiểm lại trên tệp gốc:** ghi chú diễn giả F14 (html:62): "trung vị hai số là trung bình của chúng nên vẫn được 5". Điều phối viên tính lại: trung vị ba nhóm $(4,4)$, $(2,8)$, $(16,4)$ là $4,5,10$, trung bình là $19/3\approx6{,}33$, không phải 5. Xác nhận phát hiện nghiêm trọng.

**Quyết định của điều phối viên:** **chấp nhận** báo cáo làm bảng phát hiện của bài. Mọi phát hiện ở trạng thái **mở**; deck chưa được sửa. Cột "phát hiện" ghi thời điểm phát hiện.

**Kết luận:** cần sửa. Cấu trúc deck mới, mọi số hiệu 09.k và năm bài recitation đều đúng; còn một lời giải sai trong ghi chú diễn giả F14, các dẫn chiếu "Bài tập 09.1x của ghi chú" đã cũ sau đợt A1, một dẫn chiếu Bài 05 sai, một câu về họ $\alpha x+\beta$ trái ghi chú đã sửa, và các câu xuất xứ số liệu, bình nguồn, từ làm mềm mà ghi chú đã cắt ở đợt A1.

**Số phát hiện:** chặn bàn giao 0 · nghiêm trọng 1 · trung bình 7 · nhẹ 11.

Chế độ `no-ai-slop`: Detect. Dòng `html:` là dòng của tệp deck (mỗi trang chiếm một hoặc vài dòng dài); `note:` là dòng của ghi chú; `ex:` của `exercises.md`.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | phát hiện |
|---|---|---|---|---|---|
| nghiêm trọng | F14 | Lệch ghi chú; sai toán học trong lời giải ở ghi chú diễn giả. Gộp theo thứ tự ngược (trung vị trong nhóm cỡ 2, rồi trung bình) cho $(4+5+10)/3=19/3\approx6{,}33$, bằng trung bình thuần $38/6$, không phải 5. | html:62 "Câu hỏi: gộp theo thứ tự ngược, trung vị trong nhóm rồi trung bình, được bao nhiêu? Lời giải: trung vị hai số là trung bình của chúng nên vẫn được 5 ở đây"; note:561 (trung bình nhóm 4, 5, 10; trung bình thuần $38/6\approx6{,}33$); note:708 | "Lời giải: trung vị hai số là trung bình của chúng, nên ba nhóm cho 4, 5, 10, và bước cuối lấy trung bình được $19/3\approx6{,}33$, đúng bằng trung bình thuần $38/6$: giá trị 16 lại kéo lệch kết quả, và bước cuối không còn bảo đảm của mẹo trung vị (Nhận xét 09.18)." | 2026-11-13 |
| trung bình | XT, X01, X01C, X02, X02B, X03, X03B, X04, X05 | Lệch ghi chú: dẫn chiếu bài tập trỏ sai nơi. Sau đợt A1, Bài tập 09.10–09.22 nằm trong `exercises.md`, không còn trong ghi chú; deck vẫn ghi "của ghi chú", "trong ghi chú". Số hiệu và loại khối đúng. | html:234 "Lời giải đầy đủ ở các Bài tập 09.11, 09.10, 09.12, 09.15, 09.16 của ghi chú bài giảng"; html:236, 239, 241, 243, 245 "Bài tập 09.1x của ghi chú"; html:238 "(Bài tập 09.17 trong ghi chú)", html:240 "(Bài tập 09.18 trong ghi chú)", html:242 "(Bài tập 09.13 trong ghi chú)"; note:2281; ex:3; review-log:402, 478 (đã ghi là việc của lần sửa deck sau) | Đổi "của ghi chú (bài giảng)" và "trong ghi chú" thành "của tệp bài tập" ở 9 chỗ, theo cách ghi chú viết ở note:162 "(Bài tập 09.18, tệp bài tập)". | 2026-11-13 |
| trung bình | M08 | Lệch ghi chú: dẫn chiếu Bài 05 sai. Ghi chú Bài 05 chỉ có Mục 1–5; kết quả phương sai của trung bình là Mệnh đề 05.14 (Mục 4). | html:99 "Trung bình của $s$ biến độc lập có phương sai $1\,304/s$ (ghi chú Bài 05, Mục 8)"; note:947 "(Bước 2 trong chứng minh Mệnh đề 05.14)"; `materials/lec-05/lecture-note.md`:790 | Thay bằng "(Bước 2 trong chứng minh Mệnh đề 05.14)". | 2026-11-13 |
| trung bình | X01C | Lệch ghi chú: câu về họ $\alpha x+\beta\bmod2^L$ với $\alpha$ lẻ là đúng câu mà đợt A1 giai đoạn 2 đã sửa vì ngụ ý các giá trị băm độc lập trên dữ liệu không có cấu trúc. Ghi chú và lời giải 09.17 nói: với $\alpha$ cố định, hiệu $h(x)-h(x')$ không phụ thuộc $\beta$, nên các giá trị băm không độc lập. | html:238 "dù vậy họ này chỉ xấp xỉ mô hình lý tưởng khi dữ liệu không có cấu trúc theo các bit thấp"; note:700; ex:253; review-log (giai đoạn 2, bảng phát hiện, dòng 09.17) | "chọn $\alpha$ lẻ và $2^L$ lớn hơn cỡ tập vũ trụ; với $\alpha$ cố định, hiệu $h(x)-h(x')=\alpha(x-x')\bmod2^L$ không phụ thuộc $\beta$, nên các giá trị băm không độc lập và mức sai phụ thuộc cấu trúc bit thấp của dữ liệu." | 2026-11-13 |
| trung bình | F03, M11, C06, E06 | Quy tắc: không câu xuất xứ số liệu (luật tác giả; quyết định 2026-11-11 đã xóa các câu này khỏi ghi chú, nguyên văn chuyển vào review-log). | html:42 "giá trị băm là dữ liệu tính tay của học phần"; html:102 "các số ngẫu nhiên là dữ liệu tính tay của học phần"; html:131 "hai hàm băm là dữ liệu tính tay của học phần"; html:194 "Hằng $c=1/2$ là dữ liệu tính tay của học phần; giá trị lớn làm trọng số giảm nhanh để thấy hiệu ứng trên dòng ngắn"; review-log:406 | Cắt các mệnh đề xuất xứ, giữ phần nội dung: F03 "Ví dụ 09.3; chuỗi bit viết bit cao bên trái nên đuôi là các bit bên phải."; M11 "Ví dụ 09.10; mỗi số $\xi$ đều trên $\{1,\ldots,r\}$."; C06 "Ví dụ 09.12: $h_1$ đưa …"; E06 "Với $c=1/2$, trọng số giảm một nửa mỗi bước, nên bốn điểm khác nhau rõ trên dòng mười lăm phần tử." | 2026-11-13 |
| trung bình | C11, D12, D06, T07, F09, F15, T05, C13, D08, E04, D15, E03 | Quy tắc: câu bình nguồn và đính chính sách (đợt A1 cắt khoảng 35 câu cùng loại khỏi ghi chú, mức trung bình); `no-ai-slop`: nguồn làm chủ ngữ thay cho nội dung. | html:142 "UMass (trang chiếu 17) dùng nó mà không phát biểu, và viết dấu bằng ở chỗ đúng ra là bất đẳng thức"; html:172 "Trang chiếu MMDS (Streams 1, tr.42) phát biểu cận này nhưng bỏ sót bit của chính thùng biên"; html:159 "Nhãn 'có ít nhất một đoạn có 8 bit 1' của MMDS nói về số đoạn"; html:225 "vì trang chiếu MMDS đảo thứ tự"; html:57 "MMDS (tr.143) chỉ có hai kết luận định tính"; html:71 "bước trung bình nhóm chỉ được MMDS lập luận định tính"; html:223 "bước trung bình nhóm có lập luận định tính của MMDS"; html:144 "UMass (trang chiếu 19) có một cơ chế nhưng không chứng minh"; html:162 "MMDS không có"; html:192 "vì MMDS không có ví dụ số"; html:174 "Cách chú thích từng hàng theo trang chiếu Stanford"; html:191 "Hình vẽ lại ý của MMDS Hình 4.4"; review-log:390 | Viết nội dung trước, nguồn trong ngoặc, như ghi chú: C11 "Tính độc lập giữa các hàng không suy ra từ tính phổ dụng của từng hàm (UMass, trang chiếu 17)" (note:1403); D12 "Số hạng '+1' là bit mốc phải của chính $b^*$ (Stanford CS246 2017, Streams 1, tr.23)"; F09 "Phần (a) cho hai giới hạn (MMDS, tr.143): …" (note:436); T07 "thứ tự gộp theo MMDS tr.144 và Streams 2, tr.30"; C13, T05 "Hệ quả không nói cách liệt kê các phần tử đã xuất hiện mà không lưu chúng" (note:1448); cắt câu ở D06, D08, D15, E04 ("vì MMDS không có ví dụ số"), E03 ("Hình vẽ lại …"). | 2026-11-13 |
| trung bình | P07 | Quy tắc: mật độ. Trang bảng chi phí (trần 80) có 90 âm tiết theo cách đếm của `CLAUDE.md` (tiêu đề cột tính); storyboard ghi 79 và không có ngoại lệ. | Đếm tay: dòng Mô hình 13, tiêu đề cột 10, năm hàng 14+10+10+8+12, dòng cuối 13 = 90; storyboard:53 "79 (8, 15)"; storyboard:243 | Rút dòng Mô hình thành "**Mô hình:** bộ nhớ, đơn vị ở cột cuối." (−4); "bảng băm các phần tử đã gặp" → "bảng băm phần tử đã gặp" (−1); "một bộ đếm mỗi phần tử" → "bộ đếm mỗi phần tử" (−1); "một điểm mỗi phần tử" → "điểm mỗi phần tử" (−1); dòng cuối → "IPv4: $2^{32}$ bit, tức 512 MiB mỗi trang; $N=10^9$: 125 MB mỗi URL." (−4): còn 79; ghi lại số đếm trong storyboard. | 2026-11-13 |
| trung bình | P02 | Lệch ghi chú: mục tiêu học tập. Mục tiêu trên deck rút gọn và bỏ một số ý của mục tiêu ghi chú, dù các trang phục vụ có trong deck. | html:18; note:11–16. Thiếu: phân biệt phạm vi toàn dòng với cửa sổ, chọn theo bảo đảm và chi phí (MT1); "dạng tổng quát cho $F_p$", "trung bình các biến không chệch" (MT3, trang M09, M13); "cận nhiễu kỳ vọng, cận Markov, khuếch đại theo số hàng" (MT4, C10–C12); "cận dưới $N$ bit", "số thùng $O(\log N)$", "tính đúng của phép gộp dây chuyền" (MT5, D03–D04, D08, D17–D17B); "chạy thuật toán tìm phần tử phổ biến", "nhỏ hơn $1/(c\theta)$" (MT6, E07–E10) | Viết sáu mục tiêu theo động từ và đối tượng của note:11–16, ví dụ MT5 "Duy trì, truy vấn DGIM; chứng minh cận dưới $N$ bit, bộ nhớ $O(\log^2N)$, cận 50% và tính đúng của phép gộp."; MT6 "Cập nhật cửa sổ suy giảm, chạy thuật toán phần tử phổ biến; chứng minh số điểm nhỏ hơn $1/(c\theta)$."; giữ ≤ 80 âm tiết (hiện 69). | 2026-11-13 |
| nhẹ | F16 | Quy tắc: không rào đón về vị thế, nói nội dung dương (luật 2026-11-04); Lệch ghi chú: ghi chú nêu điều kiện định lượng thay cho "chỉ có lập luận định tính". | html:72 "**Lưu ý:** hệ quả áp cho nhóm cỡ 1; bước trung bình trong nhóm chỉ có lập luận định tính."; note:661 | "**Lưu ý:** hệ quả là cận của Thuật toán 09.13 khi $g=q$; với nhóm lớn hơn, bổ đề cần mỗi trung bình nhóm ra ngoài $G$ với xác suất dưới $1/4$." | 2026-11-13 |
| nhẹ | P04B, M09, X01C, C10 | Quy tắc: từ làm mềm không có nội dung định lượng khi có số hoặc điều kiện (luật 2026-11-09). | html:23 "hiếm khi thừa nhiều", "cửa sổ suy giảm giữ ít điểm"; html:100 "ba biến lệch xa hơn so với bậc hai" (note:992 có 32% và 7%); html:238 "cả ba ước lượng 1, 16, 16 đều sai xa"; html:141 "nhiễu là một số cố định có thể rất lớn" | P04B "… hàng độc lập: thừa quá $\varepsilon r/\kappa$ với xác suất không quá $\delta$." và "… cửa sổ suy giảm giữ ít hơn $1/(c\theta)$ điểm." (đo lại mật độ, ngoại lệ 80); M09 "ba biến cho 165, thấp hơn $F_3$ khoảng 32%, so với 7% ở bậc hai"; X01C "ba ước lượng 1, 16, 16 so với 7 phần tử phân biệt."; C10 "với một hàm cố định, nhiễu là một số cố định, tới $r-f_u$ khi mọi phần tử chung ô với $u$." | 2026-11-13 |
| nhẹ | C10 | Lệch ghi chú: ý bên lề mà đợt A1 cắt có chủ ý khỏi ghi chú. | html:141 "Cận kỳ vọng thành đẳng thức khi họ độc lập từng cặp."; review-log:404 | Cắt câu. | 2026-11-13 |
| nhẹ | F13, C03 | Lệch ghi chú: hai điều kiện toán học được thêm ở đợt A1 chưa vào deck. Không có "(lẻ)", trung vị của số chẵn ước lượng có thể là $(256+512)/2=384$; với $m=1$ hàm hằng vẫn thỏa $\Pr\le1/m$. | html:61 "dù dùng bao nhiêu hàm băm" (note:544 "dù dùng bao nhiêu (lẻ) hàm băm"); html:128 "Họ chỉ gồm một hàm hằng làm mọi cặp trùng với xác suất 1, nên không phổ dụng." (note:1205 "với $m\ge2$") | F13 "dù dùng bao nhiêu hàm băm, với số hàm lẻ"; C03 "Với $m\ge2$, họ chỉ gồm một hàm hằng …". | 2026-11-13 |
| nhẹ | F03 | Lệch ghi chú: phát biểu xác suất thiếu giả thiết "ngẫu nhiên đều"; với hàm băm tất định cố định, câu sai. | html:42 "Giá trị băm kết thúc bằng $\ge\ell$ bit 0 với xác suất $2^{-\ell}$"; note:230 "chuỗi ngẫu nhiên kết thúc bằng ít nhất $\ell$ bit 0 với xác suất $2^{-\ell}$" | "Chuỗi bit ngẫu nhiên đều kết thúc bằng $\ge\ell$ bit 0 với xác suất $2^{-\ell}$: …" | 2026-11-13 |
| nhẹ | P04, F04, M08, M15, E10 | Quy tắc: giải thích đi thẳng vào ý (luật 2026-11-09), không chỉ đường, không bình kỹ thuật; `no-ai-slop` Detect: câu lặp, phủ định thay cho khẳng định, tương phản nhị phân. | html:22 "Hai khối cuối cùng hỏi về phần gần đây của dòng." (lặp câu "hai câu sau hỏi về phần gần đây" cùng đoạn); html:46 "như ví dụ ba hàm băm cho thấy trên cùng dòng"; html:99 "Ví dụ ba biến cho 55 là một lần rút cụ thể, không mâu thuẫn với kỳ vọng 59."; html:115 "Ý nghĩa: hậu tố được dùng vì thuật toán dòng chỉ đếm được từ vị trí đã chọn về sau, không phải vì tiền tố sai." (không có trong ghi chú); html:207 "Điều kiện $\theta<1$ không phải giả thiết của cận; nó chỉ cần để phần tử mới được theo dõi quá một bước" | P04: cắt câu cuối. F04: "Số này dao động mạnh theo hàm băm: ba hàm băm khác cho 2, 8, 16 trên cùng dòng." M08: "Ví dụ ba biến cho 55 ở một lần rút; kỳ vọng trên mọi lần rút là 59." M15: "Thuật toán dòng chỉ đếm được từ vị trí đã chọn về sau, nên dùng hậu tố; theo bài này, tiền tố cũng cho kỳ vọng $F_2$." E10: "Cận (b) đúng với mọi $\theta>0$; với $\theta=1$, điểm 1 thành $1-c<1$ ở bước kế tiếp và bị xóa (note:2050)." | 2026-11-13 |
| nhẹ | M03 | Quy tắc: trang "Ví dụ: …" có dòng "Tính …" (quy ước 2026-10-28/29). | html:87 dòng đầu "Chọn vị trí đều, đếm số lần phần tử ở đó xuất hiện từ vị trí đó về sau." | "Chọn vị trí 3, 8, 13; tính bộ đếm và ước lượng $r(2v-1)$ của ba biến." | 2026-11-13 |
| nhẹ | F17 | Quy tắc: ghi chú diễn giả dẫn "Bước 2", "Bước 3", "Bước 4" mà mặt trang chỉ ghi nhãn "Bước 1:". | html:73 mặt trang: "Bước 1: …", hai dòng sau không nhãn; ghi chú: "Bước 2: nếu ít nhất…", "Bước 3 dùng cận hợp…; Bước 4 dùng…" | Gắn nhãn "Bước 2:" (phủ bằng tập chỉ số), "Bước 3:" (cận hợp, độc lập, rút gọn) trên mặt trang và gộp tham chiếu trong ghi chú cho khớp. | 2026-11-13 |
| nhẹ | X03, X05 | Lệch ghi chú: đề recitation trên mặt trang khác cấu trúc câu hỏi của `exercises.md` (lời giải trên deck vẫn khớp). | html:241 chỉ hỏi bộ đếm; ex:130–131 có (a) bộ đếm, (b) ước lượng $9(2v_i-1)$ và trung bình. html:245 một câu hỏi và giả thiết "không bit 1 nào … rời cửa sổ"; ex:194–195 tách (a) thùng cỡ 8 duy nhất, (b) còn một thùng cỡ 8 cũ hơn | X03: thêm dòng "(b) Tính ước lượng $9(2v_i-1)$ của từng biến và trung bình của chúng." X05: viết (a), (b) như ex:194–195 (X05C đã giải cả hai nhánh). | 2026-11-13 |
| nhẹ | T02 | Quy tắc: mật độ. Ngoại lệ T02 ghi 70 âm tiết (không tính tiêu đề cột); tính tiêu đề cột là 81, vượt trần 80 một âm tiết. | storyboard:247 "trần âm tiết 80 của bảng tổng kết được giữ"; đếm: tiêu đề 12 + bảy hàng 10, 9, 8, 15, 12, 3, 12 = 81 | Đổi "nhân với $1-c$" → "nhân $1-c$" (−1, còn 80) và cập nhật số đếm trong ngoại lệ T02 (đếm cả tiêu đề cột). | 2026-11-13 |
| nhẹ | P06, F16, X05C | Quy tắc: chính tả công thức; dấu chấm câu nằm trong KaTeX. | html:28 "$N=8.$"; html:72 "$\Pr[M\notin(d/8,8d)]\le0{,}0029.$"; html:247 "$13+3=16=8+4+2+1+1.$" | Đưa dấu chấm ra ngoài `$…$`. | 2026-11-13 |

### Đã kiểm, không lỗi / bác bỏ cờ quét

- **Dẫn chiếu 09.k.** 116 lần xuất hiện số `09.k` (refcheck đếm 123 theo mẫu có tên khối): mọi tên khối và số trùng khối hiện tại của ghi chú hoặc `exercises.md`; đợt A1 không đánh số lại (review-log: 99 khối trùng khít loại, số, tiêu đề). Đã đối chiếu nội dung từng dẫn chiếu với khối: Định nghĩa 09.1, 09.2, 09.5, 09.8, 09.19, 09.30, 09.31, 09.33, 09.42, 09.52; Nhận xét 09.3, 09.4, 09.12, 09.17, 09.27–09.29, 09.39, 09.43, 09.51, 09.54, 09.57; Thuật toán 09.6, 09.13, 09.20, 09.24, 09.34, 09.45, 09.47, 09.55; Mệnh đề 09.7, 09.11, 09.16, 09.25, 09.41, 09.44, 09.49, 09.53; Bổ đề 09.9, 09.14, 09.21, 09.32, 09.35, 09.36; Định lý 09.10, 09.22, 09.37, 09.46, 09.48, 09.56; Hệ quả 09.15, 09.23, 09.26, 09.38; Ví dụ 09.2–09.20; Tình huống 09.1, 09.3; Bài tập 09.2, 09.4, 09.6, 09.7, 09.8, 09.10–09.13, 09.15–09.18. Dẫn chiếu ngoài bài (Định nghĩa 08.1, 08.22, Thuật toán 08.16, Định lý 08.17, 08.25, Bổ đề 08.26, Ví dụ 08.17, Định lý 06.7) tồn tại. Lỗi duy nhất về nơi chốn: "của ghi chú" (hàng 2) và "Bài 05, Mục 8" (hàng 3).
- **Bài tập recitation** (MMDS 4.4.1 = 09.11, 4.5.1 = 09.10, 4.5.3 = 09.12, 4.6.1 = 09.15, 4.6.3 = 09.16): dữ kiện, giá trị băm, độ dài đuôi, $R$, $F_2=21$, $F_3=51$, $v_i$, tổng 189, $F_3$ qua 09.13 ($459/9=51$), $\widehat y_5=3$, $\widehat y_{15}=10$ so với 9, dây chuyền ba lượt gộp và nhánh thùng cỡ 16 khớp `exercises.md`; mỗi bài có số bài, mục, trang trên trang đề, trang "Lời giải:" cùng tiêu đề, hướng dẫn chấm trong ghi chú diễn giả.
- **Tính lại số:** độ dài đuôi $h_1$–$h_6$; $\Pr[R\ge12]\approx0{,}217$, $\Pr[R<8]\approx0{,}020$, $0{,}763$, $0{,}615$ và các cột hình F12; $L/2+1=33$, cận 17, 28%; $4,5,10\to5$; $\eta\approx0{,}1433$, $0{,}573^{10{,}5}\approx0{,}0029$; $420\cdot7+1=2\,941$ bit; $0{,}115$, $0{,}0004$ (F19); $v_i$, $\sum(2v_i-1)^2=319$, $\operatorname{Var}=1\,304$, $36{,}1$; 285, 105, 165, 125; 93; vết M11; $2F_2-F_1=103$; bảng Count-Min, 14 000 và 74 000 bộ đếm, $t=37$; 8, 4, 3, 8 (C14); vị trí bit 1 của Hình 4.2; 2 130 bit, 266 byte; $\widehat y_{10}=6$; 6,51; bốn điểm $D_{15}$; vết E07–E07B; E12; cận 21 và 39 (X02B).
- **Cấu trúc deck mới:** 7 mạch; mạch mở đầu đủ (bìa có luận đề, Nhắc lại/Ký hiệu, Mục tiêu, Nội dung có Đọc trước, Vấn đề trung tâm có hình và trang trả lời có điều kiện); sáu trang tiêu đề mạch có dòng dẫn "Muốn …, phải …" 19–24 âm tiết, ≤ 5 từ khóa, ghi chú 86–97 âm tiết; sau mỗi trang tiêu đề có trang bài toán có hình (F01, M01, C01, D01, T01, X01); cụm thuật toán đủ (giới hạn có số, so với thuật toán đã biết, chạy tay, Đầu vào/Đầu ra, giả mã, đọc giả mã, tính đúng bằng quy nạp/bất biến, Mô hình và bảng đếm); mỗi mạch nội dung có bài tập có lời giải (F19, M15, C14, D19, E12); mạch kết luận có hai bảng, trả lời có điều kiện (T05), "Câu hỏi tự kiểm tra" mở đúng câu, nguồn có ghi công `http://www.mmds.org`, liên kết viewer, câu nối Bài 10 khớp note:2226. Nhãn in đậm đều thuộc danh sách cho phép; "Bước k:" không in đậm; không mã nội bộ, không thời lượng.
- **Mạch 5 gộp Mục 5 và Mục 6** của ghi chú: có lý do ở storyboard:19 (giới hạn 7 mạch, nhóm "gần đây"); không phải lỗi.
- **C14** (bài tập không mang số của ghi chú): quyết định "giữ" ở storyboard:116, 239; nội dung lấy từ note:1433 và note:1462–1464, nên đạt quy tắc "nội dung chỉ từ ghi chú".
- **Mật độ:** các trang trên 60 âm tiết đều thuộc loại trần 80 hoặc có ngoại lệ: P02 69 (mục tiêu), P04B 73 (ngoại lệ K8, storyboard:249), F13 63 (bảng so sánh), F18 69, M14 73, D18 67 (bảng chi phí), T04 70 (bảng so sánh). Chỉ P07 và T02 bị nêu ở bảng. Ghi chú diễn giả trên 150 âm tiết đều dưới 250 và đã liệt kê ở storyboard:251.
- **Từ làm mềm giữ lại:** "sai nhiều" (D06, html:159) có trong note:1543; "có lẽ" (E01, html:189) trích MMDS như note:1858; "gần như mọi giá trị" (F15) có ở note:595.
- **Cờ quét:** `style_blocks=1` là cờ giả; `overflow_1600` rỗng; 0 lỗi console, 0 request hỏng, 0 `.katex-error`, không cuộn ngang ở 390. Ảnh P07, T02, F14, X01B ở 1600×900 và 390×844 (`SP/shots-09/`): `scrollHeight=clientHeight`, nội dung vừa khung; P07 và T02 dễ đọc dù vượt trần âm tiết.

### Quyết định của người dùng (2026-11-13)

- Quyết định của người dùng (2026-11-13): thống nhất thuật ngữ "véc-tơ" cho deck và ghi chú (tên tiếng Anh "vector" chỉ trong ngoặc ở lần dùng đầu). Deck 09 (4 chỗ) và ghi chú 09 (3 chỗ) viết "vector": đổi thành "véc-tơ" trừ tên tiếng Anh trong ngoặc.

## Thuật ngữ "véc-tơ" trong ghi chú (2026-11-13)

Theo quyết định người dùng 2026-11-13 ("dùng 'véc-tơ'"), tác tử chỉnh sửa ghi chú (`general-purpose`, `opus` (Opus 5.5), effort `high`, `no-ai-slop` chế độ Edit) đổi "vector" thành "véc-tơ" trong ghi chú; tên tiếng Anh giữ trong ngoặc ở lần dùng đầu. Chạy trước đợt sửa deck, không chạy cùng tác tử deck. Điều phối viên đọc word-diff (chỉ có thay thuật ngữ và chú thích tiếng Anh), `git diff --check` sạch; trình xem ở 1440×900 và 390×844: 0 lỗi console, 0 request hỏng, 0 `.katex-error`, không cuộn ngang. Quyết định: chấp nhận.
- Ghi chú 09: 3/3 chỗ đổi; lần đầu "véc-tơ bit (bit vector)". `img/lec-09/fm-bai-toan.svg` (chỉ deck dùng) còn "vector" trong `desc`: sửa ở đợt sửa deck.

## Sửa deck theo bảng phát hiện 2026-11-13

**Tác tử.** Vai trò: tác tử sửa deck (writer) Bài 09, theo `edit-decisions.md` của điều phối viên (G1–G18, D09); `no-ai-slop` chế độ Edit, tự kiểm theo `eval.md`. Loại, mô hình và effort do điều phối viên ghi từ lời gọi công cụ. Không commit.

**Phạm vi đã ghi.** Deck `lecture-09-dong-du-lieu-dem-momen-va-cua-so.html` (109 → 111 trang); `img/lec-09/fm-bai-toan.svg` (sinh lại bằng `tools/courses/ds-foundation-algorithms/2627-1/img/lec-09/generate_deck_svg.py`, hàm `fm_bai_toan`: desc "véc-tơ bit", bỏ nhãn "hình khái niệm"); `storyboard.md`, `outline.md`, mục này. Ghi chú bài giảng và `exercises.md` không đổi.

**Ngoài bảng phát hiện.**
- G5 (danh sách recitation): mục tiêu 4 (Count-Min) chưa có bài recitation, `exercises.md` có Bài tập 09.20 (BHK Bài 6.7, §6.6, tr.204). Thêm X06 (đề) và X06B ("Lời giải:", khớp lời giải 09.20), đặt sau X03B theo thứ tự mạch; XT (dòng dẫn, từ khóa, ghi chú diễn giả), P02 (ghi chú diễn giả), T07 (BHK §6.6) cập nhật theo. Thời gian recitation giữ 60 phút: X01C 5 → 4, X02B 5 → 4, X03B 8 → 6, X04B 8 → 7, X05B 6 → 5; X06 2, X06B 4.
- G13: bốn chỗ "vector" (P07 mặt trang và ghi chú diễn giả, ghi chú diễn giả FT, `alt` F01) và `desc` của `fm-bai-toan.svg` đổi thành "véc-tơ"; lần dùng đầu (ghi chú diễn giả P07) là "véc-tơ bit (bit vector)". Mặt trang P07 bỏ hẳn chữ này khi rút dòng cuối.
- G14: T07 thêm liên kết `exercises.md` qua trình xem, như deck 10.
- G6: thêm "Giả định" → "Giả sử" (F18); ghi chú diễn giả F16 đặt nguồn Chernoff trong ngoặc. Xuất xứ dữ liệu tính tay đã ghi ở mục "Sửa ghi chú theo chuẩn 2026-11" (nguyên văn câu đã xóa), không ghi lại.
- Kiểm hình: P04B dòng Count-Min bỏ "bao giờ" để "$\le\delta$" không rơi xuống dòng riêng ở 1600×900; X05 chuyển danh sách thùng xuống ghi chú diễn giả để trang vừa khung.

| phát hiện | xử lý | trang | ghi chú |
|---|---|---|---|
| nghiêm trọng · lời giải "đảo thứ tự gộp" sai (5) | sửa | F14 | Ghi chú diễn giả: ba nhóm cho 4, 5, 10; trung bình $19/3\approx6{,}33$, bằng trung bình thuần $38/6$; bước cuối không còn là trung vị nên mất bảo đảm của mẹo trung vị (Nhận xét 09.18). Tính lại: $(4+5+10)/3=19/3=38/6$. |
| trung bình · "Bài tập 09.1x của ghi chú" sau đợt A1 | sửa | XT, X01, X01C, X02, X02B, X03, X03B, X04, X05 | Chín chỗ viết "Bài tập 09.k" không kèm "của ghi chú"/"của tệp bài tập", theo G4 (khác đề xuất "của tệp bài tập"); refcheck 130 đúng, 0 sai. |
| trung bình · dẫn chiếu "ghi chú Bài 05, Mục 8" | sửa | M08 | Thay bằng "(Bước 2 trong chứng minh Mệnh đề 05.14)" như note:947, kèm điều kiện độc lập ở Nhận xét 09.27. |
| trung bình · họ $\alpha x+\beta\bmod2^L$ trái ghi chú | sửa | X01C | Ghi chú diễn giả theo lời giải 09.17: với $\alpha$ cố định, $h(x)-h(x')=\alpha(x-x')\bmod2^L$ không phụ thuộc $\beta$, nên các giá trị băm không độc lập. |
| trung bình · câu xuất xứ số liệu | sửa | F03, M11, C06, E06 | Cắt bốn mệnh đề "dữ liệu tính tay của học phần"; E06 còn "Với $c=1/2$, trọng số giảm một nửa sau mỗi phần tử mới" (không dùng "khác nhau rõ" của đề xuất vì là từ làm mềm). |
| trung bình · câu bình nguồn, đính chính sách | sửa | C11, D12, D06, T07, F09, F15, T05, C13, D08, E04, D15, E03 | C11 theo note:1403; D12 chỉ còn nguồn chứng minh (số hạng "+1" đã giải thích ở D13); F09 theo note:436; T07 thứ tự gộp theo MMDS tr.144 và Streams 2, tr.30; T05, C13 "Phạm vi" theo note:1448 và điều kiện $1/4$ theo note:661; D08 nguồn trong ngoặc; cắt câu ở D06, D15, F15, E04 ("vì MMDS không có ví dụ số"); E03 "Theo Nhận xét 09.54 (MMDS Hình 4.4)". |
| trung bình · P07 90 âm tiết, trần 80 | sửa | P07 | Áp đủ bốn phép rút của đề xuất: 90 → 79 (script, tính tiêu đề cột); storyboard ghi số mới. |
| trung bình · mục tiêu P02 thiếu ý của ghi chú | sửa | P02 | Sáu mục tiêu theo động từ, đối tượng của note:11–16: thêm $y_k$, $D_r$, phạm vi, phép gộp, dạng $F_p$, không chệch với hồ chứa, Markov và hàng độc lập, cận dưới $N$ bit, phép gộp đúng, tìm phần tử phổ biến, $1/(c\theta)$; 69 → 79 âm tiết (đếm tay 79). Không ghi đủ "cận nhiễu kỳ vọng", "số thùng $O(\log N)$" để giữ ≤ 80; các trang C10, D08 phục vụ. |
| nhẹ · "chỉ có lập luận định tính" | sửa | F16 | Lưu ý: "hệ quả là cận của phép gộp khi $g=q$; với nhóm lớn hơn, bổ đề cần $\Pr[\bar Y_\gamma\notin G]<1/4$" (note:661); 55 → 53 âm tiết. |
| nhẹ · từ làm mềm | sửa | P04B, M09, X01C, C10 | P04B "thừa quá $\varepsilon r/\kappa$ với xác suất $\le\delta$", "điểm $\ge\theta$ … ít hơn $1/(c\theta)$ điểm" (73 → 71); M09 165, 32%, 7%; X01C "so với ba ước lượng 1, 16, 16"; C10 "tới $r-f_u$ khi mọi phần tử chung ô với $u$". |
| nhẹ · ý bên lề đã cắt khỏi ghi chú | sửa | C10 | Cắt "Cận kỳ vọng thành đẳng thức khi họ độc lập từng cặp." |
| nhẹ · thiếu "(lẻ)" và "$m\ge2$" | sửa | F13, C03 | F13 ghi chú diễn giả "với số hàm lẻ"; C03 mặt trang "Với $m\ge2$, …" (53 → 54). |
| nhẹ · thiếu "ngẫu nhiên đều" | sửa | F03 | "Chuỗi bit ngẫu nhiên đều kết thúc bằng $\ge\ell$ bit 0 …" (53 → 55, dòng 20 âm tiết). |
| nhẹ · giải thích vòng, chỉ đường | sửa | P04, F04, M08, M15, E10 | P04 cắt câu lặp; F04 nêu 2, 8, 16; M08 "55 ở một lần rút; kỳ vọng trên mọi lần rút là 59"; M15 "… nên dùng hậu tố; theo câu (a), đếm ở tiền tố cũng cho kỳ vọng $F_2$"; E10 theo note:2050 (thêm "trừ khi xuất hiện lại ngay"). |
| nhẹ · trang "Ví dụ:" thiếu dòng "Tính" | sửa | M03 | "Chọn vị trí 3, 8, 13; tính bộ đếm $v$, số lần phần tử ở đó xuất hiện từ đó về sau, và $r(2v-1)$." (19 âm tiết). |
| nhẹ · nhãn Bước trên mặt trang | sửa | F17 | Thêm "Bước 2:" (phủ bằng tập chỉ số) và "Bước 3–4:" (cận hợp, độc lập, rút gọn), khớp bốn bước chứng minh của ghi chú và ghi chú diễn giả (Bước 3 thêm $\Pr[E_\gamma]\le\eta$); 43 → 46. |
| nhẹ · đề recitation khác cấu trúc `exercises.md` | sửa | X03, X03B, X05, X05B, X05C | X03 (a) bộ đếm, (b) ước lượng $9(2v_i-1)$ và trung bình (ex:130–131); X05 (a), (b) như ex:194–195; trang lời giải gắn nhãn (a), (b); X05C (b) ghi $(16,r-23)$, trạng thái nhìn thấy trong ghi chú diễn giả. |
| nhẹ · T02 81 âm tiết | sửa | T02 | "nhân với $1-c$" → "nhân $1-c$": 81 → 80; ngoại lệ T02 trong storyboard ghi số tính cả tiêu đề cột. |
| nhẹ · dấu chấm trong KaTeX | sửa | P06, F16, X05C, D13 | Đưa dấu chấm ra ngoài `$…$`; thêm D13 (Bước 1, "$\lvert b^*\rvert.$") cùng loại. Dấu chấm cuối công thức hiển thị giữ. |

**Kiểm G17** (máy chủ 8796, `check_deck.py`, ảnh chụp 1600×900 và 390×844): 111 trang, 7 section ngoài, 0 lỗi console/trang, 0 request hỏng, 0 request ngoài, 0 `.katex-error`, 0 `fragment`, `style_blocks=1` (thẻ runtime), `overflow_1600` rỗng, không cuộn ngang ở 390, `hash_strand` `mach-2…7` đúng `#/2…7`, phím mũi tên chạy. Trang trên 60 âm tiết: P02 79, P04B 71, P07 79, F13 63, F18 69, M14 73, D18 67, T02 80, T04 70 (đều loại trần 80). `disp_gt3`, `notes_gt250`, `notes_lt40` rỗng. `refcheck.py 09`: 130 đúng, 0 sai. `git diff --check` sạch trên deck, hình, kế hoạch. Đã xem ảnh P02, P04B, P07, F01, F03, F14, F16, F17, M03, C03, T02, T07, XT, X01C, X03, X03B, X06, X06B, X05, X05B, X05C.

**Trạng thái.** Mọi phát hiện nghiêm trọng, trung bình và nhẹ đã xử lý; chờ điều phối viên rà và quyết định.

### Lượt sửa sau kiểm lại (2026-11-13)

Theo 16 mục đã duyệt của điều phối viên (`SP/fix/lec-09/merge-09.md`); X06/X06B được chấp nhận. Cùng tác tử sửa, cùng phạm vi ghi (G18). Không commit.

| mục | xử lý | trang |
|---|---|---|
| 1. C11: nguồn UMass | sửa: "… không suy ra từ tính phổ dụng của từng hàm. Bảo đảm theo UMass, trang chiếu 17." | C11 |
| 2. "bổ đề cần … $<1/4$" | sửa: mặt trang F16 "Với nhóm lớn hơn, bổ đề cho cận có nội dung khi $\Pr[\bar Y_\gamma\notin G]<1/4$" (tách thành dòng riêng để dòng ≤ 20 âm tiết; 53 → 58); T05 "mẹo trung vị cho cận có nội dung khi …" | F16, T05 |
| 3. P07 dòng cuối | sửa: "Véc-tơ bit IPv4: $2^{32}$ bit $=512$ MiB mỗi trang; …"; bù bằng "giữ $N$ bit cuối" → "$N$ bit cuối"; 79 (đếm tay 79 token, 80 nếu tách "véc-tơ" thành hai âm tiết) | P07 |
| 4. MT1 "theo đại lượng, phạm vi" | không thêm: sau mục 7 trang ở 79 âm tiết, thêm "đại lượng" lên 81; dòng 1 đã liệt kê bốn đại lượng $f_u$, $F_p$, $y_k$, $D_r$ | P02 |
| 5. thời lượng recitation | sửa storyboard: 13, 7, 10, 6, 11, 13, tổng 60 (khớp phút theo trang) | storyboard |
| 6. bản đồ mạch 7 và XT | sửa storyboard: kiểm mục tiêu 1–5; sản phẩm thêm "một họ hằng và hai phép tính xác suất (X06)"; đầu vào thêm mạch 4 (Định nghĩa 09.31, Định lý 09.37) | storyboard (mạch 7, XT) |
| 7. P02 thuật ngữ hai nghĩa | sửa: MT2 "giải thích thứ tự gộp", MT3 "Chạy Alon–Matias–Szegedy (AMS)" và bỏ "tính" trước "không chệch", MT5 "gộp dây chuyền đúng"; ghi chú diễn giả giải nghĩa hai cụm, cắt câu mở (155 → 146 âm tiết); đếm tay 79 | P02 |
| 8. XT | sửa: dòng dẫn "trên bài tập của giáo trình"; ghi chú diễn giả thêm "Sáu bài sau chạy bằng tay các phác thảo của bảng tổng kết và kiểm giả thiết của chúng.", rút câu về BHK 6.7 (92 âm tiết) | XT |
| 9. F16 câu lặp | sửa: cắt câu điều kiện $1/4$ trong ghi chú diễn giả | F16 |
| 10. E10 | sửa: ghi chú diễn giả mở bằng "Với $\theta=1$, phần tử mới …" | E10 |
| 11. C10 | sửa: gộp thành một câu ở chỗ thứ nhất: "Bổ đề cần $h_j$ ngẫu nhiên: với một hàm cố định, như ở ví dụ, nhiễu là một số cố định, tới $r-f_u$ …"; cắt câu cuối | C10 |
| 12. F13 | sửa: "miễn số hàm lẻ" | F13 |
| 13. C03 | sửa: "Cận Count-Min chỉ cần cận va chạm $\Pr[h(u)=h(u')]\le1/m$ (UMass, trang chiếu 14)." | C03 |
| 14. storyboard P04B | sửa: ngoại lệ P04B ghi 71 âm tiết | storyboard |
| 15. X06 hai điều kiện | sửa: "(i) Với mọi $x$ … đều trên $\{0,\ldots,m-1\}$." và "(ii) $\mathcal H$ không độc lập từng cặp."; 44 → 46 | X06 |
| 16. X01C | sửa: "Ba ước lượng 1, 16, 16; dòng có 7 phần tử phân biệt $\{1,2,3,4,5,6,9\}$."; 23 → 21 | X01C |

**Kiểm G17 lại** (máy chủ 8796, `check_deck.py`): 111 trang, 0 lỗi console/trang, 0 request hỏng hoặc ngoài, 0 `.katex-error`, `overflow_1600` rỗng, không cuộn ngang ở 390, `hash_strand` đúng `mach-2…7`; trang trên 60 âm tiết: P02 79, P04B 71, P07 79, F13 63, F18 69, M14 73, D18 67, T02 80, T04 70; `disp_gt3`, `notes_gt250`, `notes_lt40` rỗng. `refcheck.py 09`: 130 đúng, 0 sai. `git diff --check` sạch. Ảnh đã xem: P02, P07, F16, XT, X06, X01C (1600×900).

### Kiểm lại và duyệt của điều phối viên (2026-11-13)

**Tác tử (theo lời gọi công cụ).** Sửa deck: `general-purpose`, `opus` (Opus 5.5), effort `high`, `no-ai-slop` chế độ Edit; lượt sửa sau kiểm lại do cùng tác tử (tiếp tục bằng `SendMessage`). Kiểm lại vai A (độ chính xác và khớp ghi chú) và vai B (mạch, cấu trúc, văn phong, `no-ai-slop` Detect): mỗi vai một tác tử `general-purpose`, `opus` (Opus 5.5), effort `high`, chỉ đọc.

| vai | kết luận | phát hiện (chặn/nghiêm trọng/trung bình/nhẹ) | quyết định |
|---|---|---|---|
| A | đạt | 0/0/0/4 | chấp nhận; bốn mục vào `merge-09.md` (mục 1–4) |
| B | cần sửa | 0/0/3/8 | chấp nhận; mười một mục vào `merge-09.md` (mục 5–16) |

Lượt sửa sau kiểm lại: 15/16 mục làm, mục 4 không làm có lý do (P02 lên 81 âm tiết) — chấp nhận. X06/X06B (Bài tập 09.20) chấp nhận theo G5. Đề nghị sửa ghi chú để lại cho người dùng: `exercises.md` dòng 3 thêm 09.20 vào danh sách recitation.

Kiểm của điều phối viên sau lượt sửa: `check_deck.py` (Playwright, 1600×900 và 390×844) 111 trang, ID không trùng, 0 lỗi console/trang, 0 request hỏng hoặc ra ngoài, 0 `.katex-error`, không tràn khung, không cuộn ngang ở 390 px, `#/2…7` mở đúng `mach-2…7`, phím mũi tên chạy; chín trang trên 60 âm tiết đều thuộc loại trần 80 (P02 79, P04B 71, P07 79, F13 63, F18 69, M14 73, D18 67, T02 80, T04 70); không trang nào quá 3 công thức hiển thị hay ghi chú diễn giả quá 250 âm tiết. `refcheck.py`: 130 dẫn chiếu `09.k`, 0 sai. `git diff --check` sạch. Điều phối viên tự xem ảnh P02, X06 (1600×900); tính lại F14 ($19/3$). SVG `decision-map.svg` không trang nào dùng (từ trước đợt này), giữ vì `planning/lec-01/storyboard.md` còn ghi tên.

Quyết định: **chấp nhận**; mọi phát hiện của bảng 2026-11-13 đã đóng.
