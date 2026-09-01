# Nhật ký rà soát Bài 3

## Nguồn đã đọc

- `sources/source.md`: Bài 3 và quan hệ Bài 2 → Bài 3 → Bài 4.
- `sources/reference-slides/README.md`: dòng Bài 3 và quy tắc so sánh MMDS với Stanford.
- `sources/textbooks/mmds-3e-ch05-link-analysis.pdf`: mục 5.1–5.2 và bài tập.
- `sources/reference-slides/mmds/ch05-linkanalysis1.pdf`: slide chính thức MMDS, nguồn ưu tiên.
- `sources/reference-slides/stanford-cs246/09-pagerank.pdf`: trực giác người lướt và kiểu kiểm tra thay đổi cạnh.
- Mẫu, CSS và chỉ mục học phần.

## Rà soát storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B01–B03 | Ma trận xuất hiện trước khi sinh viên tự theo vết đóng góp. | Chu trình yêu cầu ví dụ chạy tay trước hình thức hóa. | Thêm B02 chạy từng đóng góp rồi chuyển nguyên trạng thái sang B03. |
| nghiêm trọng | C01–C06 | Cụm sửa lỗi không có ví dụ số cho chính nút cụt và bẫy nhện. | Đồ thị cơ sở cũ không chứa hai lỗi. | Dùng hai biến thể $y,a,m$ từ slide MMDS 39, 41, 46; chạy trước và sau sửa. |
| nghiêm trọng | E00–E02 | Cụm phân tán chỉ có một sơ đồ, chưa đủ chu trình thuật toán. | Không thấy bản ghi, cặp map, cấu trúc qua reduce, tổng toàn cục hoặc kiểm tra. | Mở thành E00–E05 với trạng thái truyền rõ. |

## Rà soát góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | C02, C03, D01, D02, E01 | Công thức thiếu dấu phân cách KaTeX. | Nội dung TeX nằm trực tiếp trong thẻ `formula`. | Bọc mọi công thức bằng `$...$` và kiểm tra tĩnh. |
| chặn bàn giao | R05 | Thiếu Hình 5.4 nên không đủ dữ kiện làm Bài 5.2.2(a). | Chỉ Hình 5.7 có SVG. | Vẽ lại Hình 5.4 và hiển thị cả hai hình. |
| nghiêm trọng | C07, D03 | $\varepsilon$ bị dùng đồng thời cho phần dư và sai số đích. | Giả mã và cận dừng không cùng nghĩa. | Dùng $\tau$ cho phần dư, $\varepsilon$ cho sai số đích; thêm $K_{\max}$ và cờ hội tụ. |
| trung bình | R00–R05 | Thời gian giao việc bị tính vào 60 phút. | Bản nháp cũ dành 4 phút riêng cho R01. | Bỏ R01; phân bổ 15+15+10+20 và tích hợp đối chiếu trong từng bài. |

## Rà soát chuyên gia giải thuật và khoa học dữ liệu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | A01 | Quy ước đa cạnh không khớp MMDS. | MMDS gộp liên kết lặp giữa cùng hai trang. | Gộp liên kết lặp, cho phép vòng tự nối, tính bậc theo đích phân biệt. |
| nghiêm trọng | E02–E04 | Một vòng PageRank bị đồng nhất với một tác vụ MapReduce; cấu trúc và nút không có cạnh vào có thể mất. | Đóng góp theo đích không tự giữ danh sách kề; $\delta$ chưa có trước reduce. | Chuyển tiếp bản ghi cấu trúc; tách pha tổng $\delta$ và tác vụ cập nhật; thu $\Delta$ sau reduce. |
| trung bình | E00 | Quy mô ví dụ có thể bị hiểu là số đo hiện tại. | MMDS slide 48 dùng $10^9$ trang để minh họa. | Ghi rõ đây là số trong nguồn, không phải phép đo Web hiện nay. |

## Rà soát độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B06 | “Bất khả quy là cần cho duy nhất” quá mạnh. | Chuỗi khả quy có thể có đúng một lớp đóng. | Nêu bất khả quy là điều kiện đủ; định nghĩa bằng khả năng đi đến nhau. |
| nghiêm trọng | D03 | Cận hậu nghiệm thiếu hệ số $\beta$. | Với $r^{(t)}$, tổng đuôi bắt đầu từ $\beta\Delta_t$. | Dùng $\beta\Delta_t/(1-\beta)$. |
| nghiêm trọng | C06, D04 | Ma trận slide 46 của bẫy nhện bị gán cho đồ thị cơ sở. | Slide 46 dùng vòng $m\to m$; đồ thị cơ sở dùng $m\to a$. | Tách hai ma trận và hai nghiệm; ghi rõ nguồn của từng ví dụ. |
| nghiêm trọng | C07 | Thuật toán không có giới hạn vòng hoặc hậu điều kiện khi chưa đạt ngưỡng. | Vòng lặp có thể không kết thúc trong ngân sách thực thi. | Thêm $K_{\max}$, cờ hội tụ và hai hậu điều kiện. |

## Rà soát phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | D05 | Câu hỏi thay đổi cạnh không xác định cạnh và sản phẩm. | Sinh viên không có đủ dữ kiện để kiểm tra đáp án. | Chỉ định cạnh $m\to y$, yêu cầu viết cột và đóng góp mới. |
| nghiêm trọng | E04 | $\delta$ có vẻ được cộng lần hai sau khi $P$ đã sửa cột nút cụt. | Mặt trang không giải thích chuyển từ cột đều sang triển khai thưa. | Nêu $\delta$ là triển khai tương đương, không vật chất hóa cột và không cộng hai lần. |
| nghiêm trọng | toàn bộ ghi chú | Thời lượng và nhãn quy trình xuất hiện trong ghi chú. | AGENTS.md chỉ cho phép thời lượng ở storyboard. | Xóa mọi thời lượng khỏi HTML; giữ duy nhất trong storyboard. |
| trung bình | thuật ngữ | “Đánh thuế” gây ngắt mạch so với dịch chuyển ngẫu nhiên. | Một cơ chế có hai tên trên các trang gần nhau. | Dùng “hệ số giảm” và “dịch chuyển ngẫu nhiên” nhất quán. |

## Quyết định chỉnh sửa và sai khác có chủ ý

| mức độ | trang chiếu | vấn đề hoặc bằng chứng | quyết định |
|---|---|---|---|
| nghiêm trọng | B06, D00–D03 | MMDS §5.1.2 thiếu giả thiết không chu kỳ cho hội tụ. | Nêu đủ điều kiện cho trường hợp không có hệ số giảm; chứng minh trường hợp $0<\beta<1$ bằng ánh xạ co. |
| nghiêm trọng | C02–C07, E04 | Sách trình bày cả quy ước cột nút cụt bằng 0 và quy ước chuyển đều. | Chọn PageRank chuẩn hóa: cột nút cụt là $e/n$; MapReduce tính bằng $\delta$ để tránh cột đặc. |
| nghiêm trọng | C06, D04 | Hai đồ thị $y,a,m$ có cạnh ra của $m$ khác nhau. | C06 dùng đúng bẫy $m\to m$ của slide 46; D04 dùng đồ thị cơ sở $m\to a$ và ghi là phép tính độc lập. |
| nghiêm trọng | D03 | Phần dư không bằng sai số tới nghiệm. | Dùng cận $\beta\Delta_t/(1-\beta)$; thuật toán dừng ở $\tau=(1-\beta)\varepsilon/\beta$. |
| trung bình | E02–E04 | MMDS mô tả nhân ma trận thưa nhưng không làm rõ mọi chi tiết giữ cấu trúc trong một deck độc lập. | Hiển thị cặp cấu trúc, cặp đóng góp, hai tổng toàn cục và số tác vụ; không thay đổi phép cập nhật. |

## Bài tập recitation

- Chỉ dùng trực tiếp MMDS Bài 5.1.1, 5.1.2, 5.2.1 và 5.2.2.
- Phân bổ thời gian giải: 15 + 15 + 10 + 20 = 60 phút; không tính trang chuyển hoặc logistics.
- Hình 5.4 và 5.7 được vẽ lại; không đổi cạnh hay yêu cầu.
- Đáp án và rubric chỉ nằm trong ghi chú diễn giả.

## Tài sản trực quan

| Tệp | Nguồn và cách xử lý |
|---|---|
| `do-thi-yam.svg` | Đồ thị cơ sở từ slide MMDS 19, 24 |
| `nut-cut-va-bay-nhen.svg` | Hai biến thể $y,a,m$ từ slide MMDS 39, 41 |
| `luong-pagerank-mapreduce.svg` | MMDS §5.2.2; bổ sung luồng giữ cấu trúc, $\delta$ và $\Delta$ |
| `do-thi-bai-tap-5-4.svg` | Vẽ lại MMDS Hình 5.4 |
| `do-thi-bai-tap-5-7.svg` | Vẽ lại MMDS Hình 5.7 |

Không có ảnh raster hoặc phụ thuộc mạng cốt lõi trong đầu ra.

## Trạng thái sau chỉnh sửa

- Đã xử lý mọi lỗi chặn bàn giao và nghiêm trọng trong kiểm định storyboard cùng bốn báo cáo độc lập.
- Sau khi thêm B02, đã rà lại B00–B04; sau khi thay cụm C, đã rà B05–D02; sau khi mở rộng cụm E và bỏ R01, đã rà D04–R04. Các câu nối, ký hiệu và trạng thái truyền trong các vùng lân cận đã được đồng bộ.
- Phần giảng có 120 phút trong storyboard; bài tập có 60 phút giải trực tiếp.
- HTML không chứa thời lượng trong ghi chú.
- Nội dung hiển thị và ghi chú được biên tập theo `no-ai-slop`; mạch được rà theo Outline Workflow của `quill` mà không tạo `quill.json`.
- Các thay đổi ở B06, C02–C07, D01–D03 và E02–E04 đã được tác tử độ chính xác toán học rà lại; không còn lỗi chặn bàn giao hoặc nghiêm trọng.

## Rà toán cuối sau chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | E02–E04 | Ký hiệu $P$ có thể đồng thời được hiểu là toán tử thưa và ma trận đã sửa, khiến $\delta$ có vẻ bị cộng hai lần. | Tác vụ map chỉ phát theo cạnh thật, còn C03 dùng ma trận có cột nút cụt bằng $e/n$. | Gọi toán tử thưa là $P_0$, đặt $\bar P=P_0+ed^T/n$ và viết cập nhật $\beta(P_0r+\delta e/n)+(1-\beta)e/n$. Đã xử lý. |
| trung bình | E01–E03 | Chưa nêu điều kiện bảo toàn nút cô lập và nút có danh sách rỗng. | Reduce chỉ giữ được nút nếu nhận bản ghi cấu trúc mang khóa của nút đó. | Nêu biết $V$ và có đúng một $S_i$ cho mọi $i\in V$, kể cả danh sách rỗng. Đã xử lý. |
| nhẹ | C07 | Miền của $K_{\max}$ chưa được ghi rõ. | Điều kiện $K_{\max}\ge1$ chưa loại giá trị không nguyên. | Thêm $K_{\max}\in\mathbb N$ và $K_{\max}\ge1$; nối $P=\bar P$. Đã xử lý. |
| nhẹ | R04 | Công thức ngưỡng có mẫu $\lceil\log_2n\rceil$ nhưng chưa loại $n=1$. | Với $n=1$, mẫu bằng 0. | Thêm giả thiết $n\ge2$ trên đề, ghi chú và hướng dẫn chấm. Đã xử lý. |
| nhẹ | E05 | Câu hỏi gọi $m$ là nút cụt ngay sau bảng đồ thị cơ sở có cạnh $m\to a$. | E01 và C02 dùng hai biến thể khác nhau của cùng ba nút. | Gọi rõ “biến thể nút cụt C02” và tách đáp án khỏi đồ thị cơ sở E01. Đã xử lý. |

Lượt rà toán cuối xác nhận các mục trên đã được đồng bộ trong HTML, outline và storyboard; không phát sinh lỗi chặn bàn giao hoặc nghiêm trọng.

## Kiểm định trình duyệt và Codex Slides

- Máy chủ cục bộ phục vụ tệp tại cổng `8765` và trả mã HTTP `200`.
- Chromium không giao diện duyệt đủ 38 trang ở khung $1280\times720$ và $800\times600$: không có lỗi bảng điều khiển, lỗi yêu cầu tài nguyên hoặc phần tử tràn khung. Ảnh liên hệ toàn bộ trang và các trang C07, E01–E05, R04 được kiểm tra trực quan. Kiểm định này áp dụng cho bản 38 trang trước khi thêm K00; bản 39 trang sau chu kỳ 2026-08-30 chưa được kiểm định trình duyệt.
- Kiểm tra tĩnh xác nhận 38 mã trang duy nhất, 38 ghi chú, 45 cặp thẻ `section`, mọi đường dẫn cục bộ tồn tại, năm SVG hợp lệ và không có tham chiếu ảnh raster.
- Dự án Codex Slides bền vững `20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9` vẫn ở trạng thái nháp với 0 trang. Trình duyệt tích hợp không khả dụng trong phiên này; bốn lần tải tệp thiết kế cuối vào dự án đều trả HTTP 500. Vì vậy chưa thể tuyên bố bản RevealJS đã được rà trực quan trong Codex Slides. URL bàn giao của dự án: `http://127.0.0.1:4311/project/20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9?mode=workspace&checkpoint=clarify`.

## Chu kỳ 2026-08-30

### Kế hoạch và phân tích nguồn

- Kế hoạch chu kỳ: rà lại bốn tệp Bài 3 sau lượt chỉnh sửa bị dừng; xác nhận cấu trúc 39 slide, 7 outer section và trang kết luận K00; đồng bộ outline, storyboard và HTML.
- Phân tích nguồn: MMDS 3e §5.1–5.2 và slide chính thức MMDS Ch5 part 1 vẫn là nguồn ưu tiên; Stanford CS246 09-pagerank.pdf bổ trợ trực giác và kiểu kiểm tra thay đổi cạnh. Không phát hiện dữ kiện nguồn mới cần đổi.

### Kiểm định storyboard và năm vai độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | toàn deck | Thiếu mạch kết luận; mở đầu chưa gộp P/A. | Deck kết thúc ở recitation mà không thu hồi bài toán A00 hay nối Bài 4. | Gộp P/A thành một mạch mở đầu, thêm K00 làm kết luận; vẫn giữ 7 outer section. |
| trung bình | B06 | “Ước chung lớn” thiếu “nhất”; phản ví dụ chỉ nằm trong notes. | Mặt trang B06 nêu điều kiện không chu kỳ nhưng không có trạng thái đầu của phản ví dụ. | Đổi thành “ước chung lớn nhất” và nêu trạng thái đầu $(1,0)^T$ trên mặt trang. |
| trung bình | D04 | Câu dẫn áp dụng $A_{0,8}$ cho đồ thị cơ sở và dẫn sang D05 chỉ có trong notes. | Mặt trang D04 chỉ có nghiệm và hai thẻ kiểm tra. | Thêm câu dẫn trên mặt trang. |
| nhẹ | R00 | Notes dùng từ “chuẩn hóa” khi mô tả đối chiếu nhóm. | Cụm “đối chiếu ma trận, chuẩn hóa hoặc biểu diễn”. | Bỏ từ “chuẩn hóa”, thay bằng “tổng vector”. |
| nhẹ | C07 | Dòng đầu khối giả mã chưa ghi $P$ đã sửa nút cụt. | Chỉ dòng muted bên dưới nêu $P=\bar P$. | Sửa ngay trong dòng đầu của khối giả mã. |

Kiểm định storyboard là một bước riêng, không thuộc năm vai rà soát độc lập. Bốn vai góc nhìn sinh viên, chuyên gia giải thuật và khoa học dữ liệu, độ chính xác toán học và thuật toán, cùng phản biện học thuật và giảng dạy đã rà bản 38 slide trước chỉnh sửa. Sau thay đổi cấu trúc, vai kết nối và mạch viết đã rà bản 39 slide; vai toán học cũng tái rà các vùng bị ảnh hưởng. Vì vậy bản cuối đã được kiểm tra đủ năm góc nhìn theo AGENTS.md. Bảng trên hợp nhất các phát hiện đã chấp nhận từ kiểm định storyboard và các lượt rà này, không phải toàn bộ mục mới.

### Quyết định và các sửa HTML đã làm

- Quyết định thiếu mạch kết luận: gộp P/A thành một mạch mở đầu, thêm K00 (3 phút) làm kết luận thu hồi A00 và nối Bài 4; tổng outer section vẫn là 7.
- Đã sửa HTML: B06 đổi “ước chung lớn” thành “ước chung lớn nhất” và thêm phản ví dụ với trạng thái đầu $(1,0)^T$ trên mặt trang; D04 thêm câu dẫn trên mặt trang về áp dụng $A_{0,8}$ cho đồ thị cơ sở phần B và dẫn sang D05; R00 notes bỏ từ “chuẩn hóa”; C07 dòng đầu khối giả mã ghi rõ $P$ cột ngẫu nhiên đã sửa nút cụt ($P=\bar P$). Đáp án R03 không thay đổi.
- Phạm vi cần rà lại sau các sửa trên: B05–B06, C00 (câu nối vào C), D04–D05 và R00–R03 về mạch, ký hiệu và trạng thái truyền.

### Đáp án R03 và bác đề xuất sai

- Đáp án R03 $(7/27,25/81,35/81)^T$ với $\beta=0{,}8$ trên Hình 5.7 là đúng; tổng bằng 1 và thỏa $r=0{,}8Pr+0{,}2e/3$.
- Đề xuất của tác tử nguồn cho bộ số khác bị bác: tác giả đã đọc nhầm tập cạnh của Hình 5.7, dẫn đến ma trận và nghiệm sai. Không thay đổi đáp án.

### Bác cảnh báo thiếu tài sản

- Cảnh báo “thiếu SVG, RevealJS, index” bị bác: bản sao tạm trong phiên này cố ý không chứa tài sản nhị phân và thư viện; kho thật có 5 SVG trong `img/lec-03/` cùng thư viện `revealjs/` và `plugin/`. Kiểm định cuối vẫn phải xác nhận các tài sản này trên kho thật.

### Trạng thái và giới hạn của chu kỳ

- Chưa chạy trình duyệt, chưa chạy Codex Slides, chưa thực hiện kiểm định cuối, chưa commit hoặc push trong chu kỳ này.
- Lời văn được biên tập theo `no-ai-slop`: câu trực tiếp, không khuôn mẫu rỗng; mạch, thuật ngữ và ký hiệu được tự kiểm nhất quán theo quy trình Quill mà không tạo `quill.json`.

### Báo cáo tái rà theo 5 trường, chu kỳ 2026-08-30

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | B06 | Mặt trang chứa `\\ldots` (hai backslash) trước lệnh TeX, KaTeX không nhận diện. | Dòng muted của B06 trong HTML. | Đổi thành `\ldots` đúng một backslash. Đã sửa. |
| nghiêm trọng | D04 | Mặt trang chứa `\\to` (hai backslash) ở ba vị trí công thức. | Dòng muted của D04 trong HTML. | Đổi thành `\to` đúng một backslash ở cả ba vị trí. Đã sửa. |
| nhẹ | D05→E00 | Thiếu câu nối giữa phần D và phần E. | Notes E00 chưa nhắc kết quả D05. | Thêm câu nối: phép tính phần D đúng trên ví dụ ba nút; phần E nâng cùng phép lặp lên quy mô nguồn. Đã sửa. |
| nhẹ | K00→R00 | Notes R00 chưa gắn ba tài sản với phần tổng kết K00. | Notes R00 nêu ba tài sản nhưng không nói "vừa tổng kết ở K00". | Thêm rõ bốn bài dùng lại ba tài sản vừa tổng kết ở K00. Đã sửa. |

- Runtime của hai báo cáo tái rà: requested_model=observed_model=z-ai/glm-5.3-flash, provider OpenRouter.
- Hai lỗi KaTeX B06/D04 đã được chấp nhận và sửa; các phát hiện nhẹ D05→E00 và K00→R00 đã sửa bằng notes.
- Tự kiểm sau sửa: 39 id duy nhất, 39 notes, 7 outer section; không còn lỗi chặn bàn giao hoặc nghiêm trọng sau sửa. Chưa tuyên bố kiểm định trình duyệt và chưa chạy Codex Slides cho bản 39 trang.

## Kiểm định cuối chu kỳ 2026-08-30

- Kiểm tra tĩnh trên bản hiện tại: 39 data-slide-id duy nhất, 39 notes, 7 outer section; tổng storyboard 120 phút giảng + 60 phút recitation; 17 tham chiếu cục bộ, 0 thiếu; 5 SVG hợp lệ XML theo Python ElementTree, đều có `role="img"`, `title`, `desc`; 0 ảnh raster; 0 ghi chú chứa thời lượng; cỡ chữ pre và trace đều 0.75em.
- `git diff --check` đạt.
- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại vì không có module `reloadserver`. Fallback `/tmp/reloadserver.py 8765` không dùng được vì cổng 8765 đang bị tiến trình ngoài phạm vi phục vụ từ `/tmp/lec05-web.ocTbZf`; điều phối viên không dừng tiến trình đó. Đã dùng cùng server fallback ở cổng 8766.
- Chromium/Playwright duyệt đủ 39/39 trang ở 1280x720 và 800x600 trên cổng 8766: không phần tử nội dung bị cắt (clipped=0), không lỗi console/page, không request failed; bàn phím điều hướng hoạt động. Ảnh ghép toàn bộ 39 trang và ảnh B06, C07, D04, K00, R00 đã được xem trực quan, đọc được, không chồng lấn.
- Hai vai tái rà cuối sau sửa KaTeX: vai toán học kiểm B05–C00, D03–D05 và xác nhận đúng; vai kết nối kiểm bốn ranh giới và xác nhận không lỗi chặn/nghiêm trọng/trung bình. Runtime cả hai: requested_model=observed_model=z-ai/glm-5.3-flash, provider OpenRouter.
- Codex Slides: project `20260827151722-b-i-3-pagerank-m-h-nh-v-t-nh-to-n-edg9` mở được resource link nhưng state draft, 0 slides; upload Design File HTML hiện tại trả HTTP 500. Phiên không có Codex in-editor Browser callable, nên không tuyên bố đã rà deck trong Codex Slides.
- Index không cần đổi vì mục Bài 3 và liên kết đã đúng/tồn tại.
- Kết luận: mọi lỗi chặn/nghiêm trọng đã xử lý; deck đủ điều kiện commit/push, với giới hạn Codex Slides đã ghi rõ ở trên.

## Chu kỳ ghi chú bài giảng 2026-09-01

### Tiếp nhận, tác tử và quyết định phạm vi

- Đã đọc lại `sources/source.md`, bảng ánh xạ slide, MMDS 3e Chương 5, slide chính thức MMDS, slide Stanford, deck, planning, viewer và index trước khi soạn.
- Tác tử lập kế hoạch GLM hoàn tất. Tác tử nguồn GLM lần đầu vượt giới hạn 14 tool call; cùng model được chạy lại trên hồ sơ nguồn thu hẹp và hoàn tất. Một reviewer GLM độc lập đã phản biện bản đồ chủ đề. Metadata của các lượt thành công đều có requested model và observed model là `z-ai/glm-5.3-flash`, nhà cung cấp OpenRouter.
- Codex chính hợp nhất hai đề xuất và duyệt `.codex/goal_lecture_3.md` gồm đúng 13 mục. Writer được khóa ở `deepseek/deepseek-v4-flash-0731`; nguồn, phạm vi và các cổng kiểm định không đổi.
- Chỉ gửi các tệp cần thiết đã lọc tới OpenRouter; không gửi `.env`, khóa, token, mật khẩu, cookie, khóa riêng hoặc thông tin xác thực.

### Quyết định chủ đề trước khi soạn

| Quyết định | Chủ đề | Lý do |
|---|---|---|
| giữ | đồ thị Web, người lướt, phương trình luồng, nút cụt, bẫy nhện, MapReduce, bốn bài tập | Trực tiếp thực hiện chuẩn đầu ra Bài 03 |
| thêm | ánh xạ co trên simplex | Lấp khoảng trống giữa phản ví dụ hội tụ và bảo đảm cho $0<\beta<1$; chứng minh trực tiếp từ đặc tả |
| thêm | cận dừng hậu nghiệm | Phần dư giữa hai vòng chưa phải sai số đến nghiệm; cần nối thuật toán với hậu điều kiện kiểm tra được |
| gộp | điều kiện bất khả quy và không chu kỳ khi $\beta=1$ | Chỉ là cầu nối ngắn trước bảo đảm bằng hệ số giảm, không mở lý thuyết Markov tổng quát |
| đọc thêm | block-striping, combiner và tối ưu MMDS §5.2.3–5.2.5 | Không cần cho sản phẩm một vòng PageRank thưa bằng MapReduce |
| chuyển bài | Topic-Sensitive PageRank, spam, TrustRank và HITS | Thuộc Bài 04 theo `sources/source.md` |

Phần hội tụ và cận dừng là suy luận biên tập có chứng minh, không được ghi như định lý nguyên văn của MMDS. Ghi chú mặc định dùng năm SVG hiện có; chỉ thêm tài sản nếu một lập luận cần hình mà các hình này không đáp ứng.

### Lượt soạn DeepSeek

- Lượt đầu dùng đúng `deepseek/deepseek-v4-flash-0731` qua OpenRouter nhưng bốn symlink briefing bị cơ chế giới hạn đường dẫn từ chối; bản thảo đổi dữ kiện nguồn nên bị Codex chính bác, không nhập kho.
- Lượt hai vẫn dùng đúng model và nhà cung cấp trên một hồ sơ chuẩn đã vật chất hóa trong thư mục tạm hẹp. Worker ghi bản thảo đầy đủ nhưng kết thúc ở giới hạn tool call sau khi tự sửa. Codex chính chỉ nhận tệp đó như bản nháp để rà, không coi trạng thái worker là cổng chất lượng đạt.
- Kiểm tra sơ bộ trước reviewer đã đánh dấu bốn vùng bắt buộc rà: định nghĩa tập đích, diễn giải ma trận bẫy nhện, chỉ số trong cận hậu nghiệm và vị trí gom khối lượng nút cụt trong giả mã. Chưa có mục nào được xem là đã sửa ở giai đoạn này.

### Năm lượt rà độc lập cho ghi chú

Năm báo cáo hợp lệ đều dùng requested model và observed model `z-ai/glm-5.3-flash`, nhà cung cấp OpenRouter. Ba lượt đầu trên dossier rộng bị cắt do phản hồi dùng hết giới hạn token; một lượt cấu trúc gặp lỗi giải mã ở bridge. Các vai bị ảnh hưởng được chạy lại trên dossier hẹp gồm bản nháp và hồ sơ dữ kiện, không đổi model, vai hoặc tiêu chí.

| Vai | Phát hiện được chấp nhận | Quyết định |
|---|---|---|
| Góc nhìn sinh viên | giả mã không thể gom nút cụt; Bài 5.1.1 dùng sai phương trình; cận dừng lệch chỉ số; cụm kiểm bẫy nhện thiếu phép nhân; thuật ngữ gây lẫn nút cụt–bẫy nhện | sửa toàn bộ; tính lại Bài 5.1.1 từ đúng Hình 5.7 |
| Toán và giải thuật | $N^+$ bị dùng cho cả tập vào và tập ra; cận $\beta\Delta_t/(1-\beta)$ chưa được chứng minh; trả nhầm vector cũ; điều kiện trước thiếu $\beta<1$; phát biểu nút cụt “phân kỳ” không chính xác | thêm $N^-$; sửa tổng từ $k=1$; trả `r_new`; siết điều kiện; đổi sang “rò khối lượng” |
| Trung thành nguồn và phạm vi | phần cốt lõi bám đúng ba biến thể và bốn đề; giả mã, ký hiệu lân cận và cận dừng vẫn chặn; chi phí bộ nhớ diễn đạt lẫn số cạnh với tổng cấu trúc | giữ phạm vi; sửa thuật toán, ký hiệu và phân rã $\Theta(m)+\Theta(n)$ |
| Học thuật và sư phạm | diễn giải $A_{0,8}$ lấy dòng của đồ thị cơ sở; thiếu nối vào từ Bài 02; một số thuật ngữ Anh chưa có tên Việt | kiểm đúng dòng ba của biến thể bẫy; thêm câu nối MapReduce; Việt hóa “ngẫu nhiên theo cột”, “phép lặp lũy thừa” |
| Markdown và viewer | directive `solution` cuối chưa đóng; hình là liên kết thường; code fence thiếu ngôn ngữ; hai header bảng sai chính tả | đóng directive; đổi thành ảnh Markdown có alt; dùng `text`; sửa header |

Reviewer có một số kết luận trung gian tự mâu thuẫn về nghiệm Bài 5.1.1. Codex chính bác các con số không thỏa hệ và tính lại từ cạnh Hình 5.7: nghiệm không hệ số giảm là $(3/13,4/13,6/13)^T$. Nghiệm với $\beta=0{,}8$ là $(7/27,25/81,35/81)^T$ và được giữ sau khi thay trực tiếp vào ma trận.

### Sửa kỹ thuật và biên tập bản cuối

- Codex chính áp dụng trực tiếp các sửa đã được reviewer phê duyệt: tách $N^+$/$N^-$; sửa phép kiểm $A_{0,8}$; sửa chứng minh cận hậu nghiệm; viết lại giả mã để gom nút cụt trên tập nút; nêu hai tác vụ MapReduce khi $\delta$ cần pha tổng hợp riêng; tính lại Bài 5.1.1; sửa ảnh, directive, code fence và bảng.
- `no-ai-slop` được dùng để bỏ lời dẫn quy trình, câu nhấn rỗng, nhịp giải thích máy móc và cách gọi “thuế” không nhất quán. Bản tự kiểm theo `no-ai-slop/eval.md` giữ nguyên dữ kiện, chứng minh, bài tập và giọng học thuật trực tiếp.
- Quill Revise/Outline Workflow được dùng ở mức dàn ý vì kho không có và không được phép tạo `quill.json`: giữ tuyến Bài 02 → mô hình → ba biến thể → hội tụ → thuật toán thưa → bài tập → ranh giới Bài 04; thống nhất ký hiệu và đưa phần bài tập về trước kết luận.
- Tác động tới deck: không đổi giả thiết, ký hiệu đã khóa, ví dụ nguồn hoặc kết luận dùng chung. Ghi chú bổ sung $N^-$ để diễn đạt tập nguồn rõ hơn nhưng không làm thay đổi công thức hay nội dung deck; chưa cần sửa HTML.

### Tái rà sau sửa

- Vai toán–giải thuật GLM tính lại cả ba biến thể, hai nghiệm có hệ số giảm, phép co, cận hậu nghiệm, giả mã, hai tác vụ MapReduce và bốn đáp án. Báo cáo xác nhận không còn lỗi chặn, nghiêm trọng hoặc trung bình.
- Vai mạch–Markdown GLM xác nhận đúng tuyến Bài 02 → mô hình → lỗi cấu trúc → hội tụ → MapReduce → bài tập → Bài 04; đúng một H1; 22 cặp directive đóng và không lồng; code fence, bảng, ảnh, alt và công thức đều hợp lệ. Phát hiện nhẹ “Kí hiệu” đã sửa thành “Ký hiệu”. Nhận xét về bốn lần nhúng hai tệp SVG bị bác vì yêu cầu là dùng đúng hai tài sản hình, không giới hạn số vị trí hiển thị.
- Hai lượt tái rà dùng requested model và observed model `z-ai/glm-5.3-flash`, nhà cung cấp OpenRouter. Sau sửa chính tả không phát sinh thay đổi kỹ thuật hoặc mạch cần mở thêm lượt rà.

### Kiểm định viewer — lần đầu

- Viewer tải được Markdown, dựng 350 công thức KaTeX không lỗi, tạo 30 liên kết mục lục, tám khối gập đóng mặc định, mở bằng bàn phím và mở toàn bộ khi in. Hai URL vượt thư mục và lệch số bài đều bị từ chối.
- Cổng thất bại vì bốn ảnh dùng đường dẫn `../../img/...`; viewer giải liên kết từ `material-viewer.html`, nên đường dẫn đúng là `img/lec-03/...`. Cùng lỗi cũng làm phát sinh hai thông báo 404 cho mỗi viewport.
- Đã sửa bốn ảnh và liên kết deck theo mô hình phát hành đã kiểm chứng ở Bài 02. Index chưa được cập nhật trước khi chạy lại toàn bộ suite.

### Kiểm định viewer — đạt

- Harness ban đầu dùng nhầm tùy chọn Playwright `viewportSize`, khiến lượt hẹp vẫn chạy ở 1280 px. Harness được sửa sang `viewport`; toàn bộ suite được chạy lại, không kế thừa kết quả hẹp giả.
- Màn hình rộng $1280\times720$ và hẹp $390\times844$: tiêu đề và trạng thái đúng; 30 heading tương ứng 30 liên kết mục lục; 350 phần tử KaTeX, 0 lỗi KaTeX; 4 ảnh tải đủ; 8 khối gập đóng mặc định; 0 lỗi console, page hoặc request; không tràn ngang.
- Bàn phím: liên kết bỏ qua điều hướng nhận focus và chuyển tới nội dung; `Enter` mở được khối gập đầu tiên.
- Bản in: mọi `details` mở; mục lục và thanh hành động ẩn; PDF A4 được tạo thành công.
- An toàn: đường dẫn vượt thư mục và cặp `doc`/`deck` lệch số bài đều hiện lỗi và giấu layout.
- Ảnh toàn trang wide/narrow đã được xem trực quan; chữ, công thức, bảng, giả mã và SVG không chồng lấn. Chỉ sau kết quả này, mục tài nguyên Bài 03 mới được thêm vào `2627-1/index.html`.
- Kiểm tra index bằng Chromium tìm đúng một liên kết Ghi chú Bài 03, nhấp liên kết và tải đúng tiêu đề, `doc`, `deck`; không có lỗi console. Index đạt cổng công bố.
