# Nhật ký rà soát Bài 13

## Trạng thái bản nháp

- HTML: `2627-1/lecture-13-chi-muc-truyen-thong-va-bam-tinh.html`.
- Giữ 59 trang và thứ tự hiện tại: 49 trang giảng, 10 trang recitation.
- Bảy `<section>` ngoài lần lượt là `P00–A03`; `B00–B08`; `C00–D01`; `H00–H06`; `M00–M07`; `T00–T01`; `X00–X08`.
- Phần giảng giữ 120 phút, recitation giữ 60 phút. Thời lượng chỉ nằm trong storyboard, không nằm trong ghi chú diễn giả.
- `2627-1/index.html` đã có đúng một thẻ Bài 13 và liên kết đúng tới HTML; không sửa tệp chỉ mục.
- Đây là bản sau kiểm định storyboard, năm báo cáo độc lập và lượt chỉnh tuần tự; QA cuối còn thuộc điều phối viên.

## Quyết định nguồn và cấu trúc

- Dùng *Database System Concepts* 7e, Chương 14 làm trục cho chỉ mục, B+-Tree, B-Tree và băm tĩnh.
- Dùng Chương 14, trang chiếu 71–75 cho bitmap cơ sở; Chương 24, trang chiếu 11–15 cho bitmap tồn tại và NULL.
- Bài tập lấy trực tiếp từ 14.1, 14.3(b), 14.4 và 14.13. Chuẩn trang PDF: đề PDF 1/tr.43 và PDF 3/tr.45; lời giải PDF 1/tr.99, PDF 2/tr.100, PDF 4/tr.102, PDF 10–11/tr.108–109.
- Đặt wrapper theo tuyến `P+A`, `B`, `C+D`, `H`, `M`, `T`, `X`; không đổi thứ tự hoặc 59 ID.
- Không dùng MMDS hoặc Stanford CS246 vì không thuộc cụm nguồn của bài này.

## Vấn đề và quyết định bản nháp

| Mức độ | Trang | Vấn đề | Bằng chứng | Quyết định |
|---|---|---|---|---|
| chặn bàn giao | Toàn bài | Có chín wrapper ngoài | Hai cặp phần liên tiếp cùng một tuyến học thuật | Gộp hai cặp wrapper để còn bảy mạch. |
| nghiêm trọng | 59 notes | Notes chứa thời lượng | Có 61 lần nhắc thời lượng trong ghi chú | Xóa toàn bộ; giữ 120+60 trong storyboard. |
| nghiêm trọng | M00, M04, T01 | $q$ chưa loại NULL | Bitmap NULL là bitmap phụ, không thuộc $q$ bitmap giá trị/dải | Định nghĩa $q$ là số giá trị hoặc dải không NULL; dung lượng tối đa $(q+2)R$. |
| nghiêm trọng | C08 | Thứ tự xử lý thiếu lá không khớp nguồn | Nguồn thử gộp nếu hai nút vừa; nếu không mới phân phối lại | Sửa mặt slide và notes theo quy tắc nguồn. |
| nghiêm trọng | C09, X06 | Dẫn sai phần và trang lời giải | Delete 23/Delete 19 là 14.4(d,e), lời giải PDF 4/tr.102 | Sửa HTML và planning về đúng mốc. |
| nghiêm trọng | C05 | Hình chưa nói nút tràn là gốc | Ví dụ nguồn tạo gốc mới chứa 15 | Sửa HTML và SVG: gốc trong bị tràn, 15 được đẩy lên gốc mới. |
| trung bình | H01, H05 | Công thức suy ra dễ bị hiểu là phát biểu nguyên văn của nguồn | Nguồn mô tả sức chứa và chuỗi tràn, không chốt hai công thức tại trang dẫn | Ghi $\alpha=N_e/(Mc)$ và $1+t+D$ là suy ra của bài giảng. |
| trung bình | H02 | Hình có thể bị hiểu là bảng chỉ có ba ngăn | Nguồn dùng 10 ngăn nhưng hình chỉ vẽ các ngăn nhận bốn khóa | Gắn nhãn “trích ngăn 1–3 trong tổng 10 ngăn” trên slide, SVG và mô tả tiếp cận. |

## Kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| nghiêm trọng | Wrapper toàn bài | Chín phần nguồn chưa thành 5–7 mạch | Chuẩn yêu cầu 5–7 wrapper; ranh giới P/A, A/B, C/D, D/H tranh cùng chức năng | Dùng đúng bảy wrapper `P+A`, `B`, `C+D`, `H`, `M`, `T`, `X`; giữ nguyên 59 ID và thứ tự. |
| trung bình | M03–M07 | Chu trình bitmap cho sẵn kết quả trước kiểm tra và trộn bitmap cơ sở với NOT | M03 hiện đáp án trực tiếp; NOT là trường hợp biên riêng | Đổi M03 thành câu hỏi + fragment; ghi hai cụm `M00–M04` và `M05–M07`. |
| trung bình | C10–C11 | Xóa thiếu bất biến và lập luận tiến triển | Giả mã chỉ nêu mượn/gộp, chưa chứng minh nút ngoài vị trí hiện tại hợp lệ | Thêm bất biến, bảo toàn của phân phối/gộp, tiến một mức và co gốc. |
| nhẹ | Các ranh giới C11, D01, H06, M07 | Câu nối giữa mạch chưa hiện trong notes | Chuyển chủ đề cây→băm→bitmap→tổng hợp còn đột ngột | Thêm câu chuyển cụ thể ở bốn notes; đã áp dụng. |

## Năm báo cáo độc lập

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| trung bình | P01, B07 | Tiên quyết và tải ký hiệu chưa được nhắc đủ | Sinh viên cần logarit, mô hình khối và phân biệt $K,L,J,D$ | Thêm nhắc tiên quyết ở P01; B07 gom chú giải ký hiệu trên mặt slide. |
| trung bình | M03 | Đáp án xuất hiện trước thao tác | Finance AND S4 và vị trí ứng viên được cho sẵn | Đổi thành tự tính AND, liệt kê vị trí và bộ lọc dư trước fragment. |

### Chuyên gia giải thuật và khoa học dữ liệu

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| trung bình | C05 | Ví dụ tách gốc có thể bị đọc như bước tiếp của vết chèn 8 | Dữ liệu [5,10,15,20,25,30] không thuộc vết 14.4 | Gắn nhãn “ví dụ độc lập” trên mặt slide và notes. |
| trung bình | T00 | Chi phí B-Tree còn mơ hồ | “mức tìm thấy + D” không nêu số nút hay cận xấu nhất | Ghi số nút đọc đến khi thấy khóa, tối đa $d+1+D$. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| trung bình | B04, B07, T00 | RID-list chưa được phản ánh trong $K$ và I/O | Danh sách dài có thể chiếm khối ngoài lá; công thức cũ bỏ chi phí đó | Định nghĩa $K$ theo mục lá, thêm $J$ và dùng $d+1+J+D$ / $d+1+L+J+D$. |
| trung bình | H01, H05, T00 | $1+t+D$ thiếu giả thiết để là số khối chính xác | H01 chỉ nói bucket “thường” là một khối | Chốt mô hình một bucket = một khối, không bộ nhớ đệm; ghi đây là suy ra của bài giảng. |

### Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| nghiêm trọng | C10–C11 | Thuật toán xóa đúng cục bộ nhưng thiếu chứng minh đúng và dừng | Chưa nêu bất biến, hiệu lực phân phối/gộp hoặc co gốc | Bổ sung toàn bộ lập luận trên C10–C11 và giữ quy tắc gộp-nếu-vừa của C08. |
| trung bình | M04–M05 | $E$ và NULL xuất hiện không có động cơ | M04 chỉ báo dung lượng, M05 chuyển thẳng sang NOT | Thêm câu báo lỗi lật bit đã xóa/NULL trước công thức NOT. |

### Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|
| chặn bàn giao | Wrapper toàn bài | Ranh giới wrapper không đúng bảy mạch đã chốt | P đứng riêng; A+B và D+H bị gộp sai chức năng | Sửa wrapper thành đúng bảy phạm vi đã ghi; không đổi ID/thứ tự. |
| trung bình | C11→D00, D01→H00, H06→M00, M07→T00 | Đầu ra mạch trước chưa phát tín hiệu cho mạch sau | Notes thiếu câu thu hồi nhu cầu thứ tự và dạng truy vấn | Thêm bốn câu chuyển; rà hai trang lân cận, không cần đổi thứ tự. |

## Sai khác có chủ ý so với nguồn

- Chuẩn hóa $m$ là số con tối đa, $d$ là số cạnh gốc–lá, $K$ là số mục khóa ở lá, $J$ là số khối RID-list ngoài lá và $M$ là số ngăn băm.
- B+-Tree là trọng tâm; B-Tree chỉ dùng để đối chiếu vị trí dữ liệu, hệ số phân nhánh và truy vấn khoảng.
- Dùng vết $m=6$ của bài 14.3(b) xuyên suốt phần giảng và recitation; không làm 14.3(a,c).
- Tách lá sao chép khóa nhỏ nhất của lá phải; tách nút trong đẩy khóa giữa và bỏ khóa đó khỏi hai nút mới.
- Sửa lỗi in của lời giải sau Insert 8: lá phải giữ $[19,23,29,31]$, không phải $[9,23,29,31]$.
- Với 14.13(b), `Finance AND S4` chỉ tạo ứng viên; vẫn đọc bản ghi và lọc lương từ 80.000.
- $\alpha=N_e/(Mc)$ và $1+t+D$ là hai suy ra của bài giảng từ mô hình nguồn, không được trình bày như công thức nguyên văn của nguồn.
- Hình băm là trích các ngăn 1–3 trong tổng 10 ngăn. Biến thể dẫn xuất đặt $c=1$, cho Physics ở ngăn nhà 3 và Elec. Eng. ở một ngăn tràn, nên $t=1$.

## Tự rà biên tập

- `no-ai-slop`: giữ câu ngắn, trực tiếp; không thêm số liệu, khẩu hiệu hoặc nhận định không có nguồn. Bản cuối của lượt soạn được đối chiếu `eval.md`.
- Quill: rà bảy mạch và tính liên tục của $m,d,f,K,M,c,N_e,t,L,D,R,q,w,E,V_v,V_{\mathrm{NULL}}$. Không tạo `quill.json`.

## Rà lại sau chỉnh sửa

- Tác tử độ chính xác rà lại B07, C10–C11, H01–H05 và T00: đạt. Ký hiệu $K,L,J,D$, mô hình băm một ngăn bằng một khối, tiến triển của xóa B+-Tree và các cận I/O đã có đủ giả thiết.
- Tác tử kết nối và mạch viết rà lại toàn bài sau khi gộp wrapper: đạt. Bảy mạch ngoài lần lượt là `P+A`, `B`, `C+D`, `H`, `M`, `T`, `X`; các ranh giới và câu nối không còn lỗi nghiêm trọng.

## Kiểm định cuối

- Kiểm tra tĩnh: 59 `data-slide-id` duy nhất, 59 khối ghi chú, 59 dòng storyboard đúng thứ tự, 7 `<section>` ngoài, 10 SVG có mô tả thay thế; không có ảnh raster, tài nguyên mạng cốt lõi, liên kết hỏng hoặc thời lượng hiển thị.
- Rà trực quan ban đầu phát hiện lỗi **chặn bàn giao** tại B07: thẻ `<strong>` của $f=\lceil m/2\rceil$ chưa đóng làm trình duyệt lồng các mạch sau vào B07. Đã đóng thẻ, kiểm tra DOM xác nhận đúng bảy wrapper và đúng các trang con, rồi chạy lại toàn bộ kiểm định.
- Ở M03, tiêu đề dài chạm mép trái trong khung hẹp. Đã rút từ “Tự tính tập ứng viên trước khi lọc dư” thành “Tính tập ứng viên trước lọc dư”, không đổi nội dung; ảnh chụp lại ở hai khung xác nhận đọc đủ.
- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Cổng 8765 đang thuộc một máy chủ của người dùng tại kho khác nên được giữ nguyên; dùng máy chủ dự phòng cục bộ tại cổng 8766 để kiểm định.
- Chromium 1280×720 và 800×600: đủ 59 trang, không lỗi console, không lỗi KaTeX, không tràn biên. Rà ảnh liên hệ toàn bộ và ảnh riêng B07, C10–C11, H02, M03, T00: không còn chồng lấn hoặc cắt nội dung. Điều hướng bàn phím `P00 → B00 → B01` đạt.
- Codex Slides: dự án `20260828012219-b-i-13-ch-m-c-truy-n-th-ng-v-b-m-t-nh-3hv7` vẫn ở trạng thái nháp với 0 trang; bản HTML cuối đã tải lên thành material `20260830165811833-mdaa.html`. Môi trường hiện không cung cấp bề mặt Browser trong trình soạn thảo, nên không tuyên bố đã rà trực quan bằng Codex Slides; kiểm định trực quan dùng RevealJS cục bộ như trên.
- `git diff --check` và kiểm tra phần thay đổi được chạy lại trước commit. Chỉ các tệp thuộc Bài 13 được đưa vào commit; thay đổi cấu hình và tệp người dùng ngoài phạm vi được giữ nguyên.

## Ghi chú tự học Bài 13

### Điều phối OpenRouter

- Ba reader `z-ai/glm-5.3-flash`: kế hoạch `11965`, nguồn `31332`, bản đồ chủ đề `78833`. Codex chính giữ 11 chủ đề; gộp nhắc tiên quyết vào N01, bác bảng lỗi lặp và mục đọc thêm ngoài phạm vi.
- Writer `deepseek/deepseek-v4-flash-0731` phiên `94655` đã ghi bản nháp trước khi chạm giới hạn công cụ. Codex chính chỉ hợp nhất phần đã ghi và kiểm chứng, rồi trực tiếp áp dụng các sửa được reviewer phê duyệt.
- Năm reviewer GLM: nguồn `60597`, toán–thuật toán `29726`, sư phạm `81489`, mạch `64599`, viewer `42582`. Lượt sư phạm đầu chạm giới hạn công cụ; lượt thu hẹp đọc đúng `goal.md` và bản cuối trả `PASS`.
- Tái kiểm toán–thuật toán `8408` và mạch viết `73590` đều `PASS`. Gốc tạm không chứa `.env`, bí mật hoặc thông tin xác thực.

### Phát hiện và quyết định

| Mức | Phát hiện | Quyết định |
|---|---|---|
| nghiêm trọng | Writer tính cận lá $m=6$ thành 2–5 và ghi $d=2$ cho cây gốc nối trực tiếp tới lá | Sửa thành 3–5 khóa và $d=1$; bổ sung cận $d=O(\log_f K)$ cùng giả thiết gốc |
| nghiêm trọng | Vết xóa 19 gọi việc gốc còn ba con là “co gốc” | Sửa thành gộp lá, xóa phân cách 19 và giữ gốc $[7,10]$; co gốc chỉ khi còn một con |
| trung bình | Giả mã chèn coi cha có $m$ con là tràn; giả mã xóa thiếu nhánh khóa vắng | Tràn chỉ khi có hơn $m$ con; khóa vắng dừng và cây không đổi |
| trung bình | Ghi chú dùng vị trí bitmap 1–12 trong khi deck dùng 0–11 | Chuẩn hóa toàn bộ ghi chú về 0–11; Wu ở 1, Singh ở 8; chuỗi bit không đổi |
| trung bình | Cơ chế tách lá cứng hóa 3–3 và bảng tổng hợp bỏ $L$ | Viết $\lceil m/2\rceil$–$\lfloor m/2\rfloor$, vết $m=6$ là 3–3; truy vấn khoảng gồm dò và quét thêm $L$ lá |
| nhẹ | Hai SVG được lặp với chú thích không đúng nội dung cụ thể; hint 14.4 nói co gốc | Chỉ dùng mỗi SVG một lần; sửa hint thành thiếu và gộp lá |

Hai đề xuất không áp dụng:

- Không chèn `note-topic-id` vào ghi chú công khai; mã nội bộ chỉ thuộc outline, storyboard và review log theo AGENTS.md.
- Không đổi liên kết deck trong Markdown thành `../../...`; viewer tải Markdown tại `2627-1/material-viewer.html`, nên liên kết hiện tại phân giải đúng. Liên kết riêng ở header và kiểm thử Chromium đều mở đúng deck.

### Biên tập và tính liên tục

- `$no-ai-slop`: bỏ nhịp dẫn máy móc, Việt hóa “đống”, “ngăn”, “chuỗi tràn”, “mã định danh bản ghi”; giữ tên thuật toán và thuật ngữ chuẩn khi cần. Không thêm dữ kiện hoặc làm mạnh hơn kết luận nguồn.
- `$quill`: rà tuyến N01–N11; thống nhất $m,f,K,d,L,J,D,M,c,N_e,t,R,w,q,E,V_v,V_{\mathrm{NULL}}$; giữ cùng quy ước vị trí 0-based với deck. Không tạo `quill.json`.

### Kiểm định viewer và index

- Chromium ở $1280\times720$ và $390\times844$: 31 heading khớp 31 liên kết mục lục, 249 biểu thức KaTeX, không lỗi KaTeX, 10 SVG không hỏng, 5 khối mã `text`, 28 khối gập đóng mặc định, không tràn ngang hoặc lỗi console.
- Bàn phím đạt cho liên kết bỏ qua nội dung và khối gập. Viewer từ chối đường dẫn vượt thư mục và ghép tài liệu với deck khác số bài.
- Bản in A4 dài 24 trang; mọi `hint`/`solution` tự mở, mục lục và thanh thao tác bị ẩn, không có hình vượt khung. Ảnh chụp toàn trang rộng và hẹp được xem trực quan, không thấy nội dung bị cắt.
- Chỉ sau khi viewer đạt mới thêm liên kết Bài 13 vào index. Kiểm thử từ index ở hai khung xác nhận đúng một liên kết, nhận focus bàn phím, mở đúng deck/tài liệu, 10 ảnh và KaTeX không lỗi.
- Kiểm tra tĩnh: một H1; 14 `exercise`, 14 `hint`, 14 `solution`, 42 dấu đóng; 5 khối mã; 10 SVG XML hợp lệ; không delimiter toán bị cấm; `git diff --check` đạt.
